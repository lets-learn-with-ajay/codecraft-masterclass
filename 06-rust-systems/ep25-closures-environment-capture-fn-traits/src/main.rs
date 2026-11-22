// Phase 1: Environment Capture Modes (&T, &mut T, and move) & Closure Type Inference
pub struct MetricSample {
    pub name: String,
    pub value: f64,
}

/// Applies an immutable transformation closure (Fn) across metric samples.
pub fn filter_and_map_samples<F>(samples: &[MetricSample], predicate: F) -> Vec<f64>
where
    F: Fn(&MetricSample) -> bool,
{
    samples
        .iter()
        .filter(|s| predicate(s))
        .map(|s| s.value)
        .collect()
}

// Phase 2: The Three Fn Traits Hierarchy (FnOnce, FnMut, Fn)
pub struct AccumulatorPipeline {
    total_processed: usize,
    running_sum: f64,
}

impl AccumulatorPipeline {
    pub fn new() -> Self {
        Self {
            total_processed: 0,
            running_sum: 0.0,
        }
    }

    /// Consumes a mutating closure (FnMut) that updates internal state per element.
    pub fn process_mut<F>(&mut self, values: &[f64], mut step: F)
    where
        F: FnMut(&mut f64, f64),
    {
        for &val in values {
            step(&mut self.running_sum, val);
            self.total_processed += 1;
        }
    }

    /// Consumes the accumulator and an owning closure (FnOnce) to produce a final report.
    pub fn finalize_once<F, R>(self, finalize: F) -> R
    where
        F: FnOnce(usize, f64) -> R,
    {
        finalize(self.total_processed, self.running_sum)
    }
}

// Phase 3: Dynamic Dispatch & Thread Boundary Transfer (Box<dyn FnOnce() + Send + 'static>)
use std::sync::mpsc;
use std::thread;

pub struct TaskDispatcher;

impl TaskDispatcher {
    /// Dispatches a move closure across a thread boundary to execute asynchronously.
    pub fn spawn_and_compute<F, T>(task: F) -> T
    where
        F: FnOnce() -> T + Send + 'static,
        T: Send + 'static,
    {
        let (tx, rx) = mpsc::channel();
        thread::spawn(move || {
            let res = task();
            let _ = tx.send(res);
        });
        rx.recv().expect("Thread execution failed")
    }
}

fn main() {
    println!("=== Modern Rust Systems Ep 25: Closures & The Fn Traits ===");

    // 1. Immutable capture (&T) -> Fn
    let threshold = 50.0;
    let samples = vec![
        MetricSample { name: "cpu_usr".into(), value: 42.5 },
        MetricSample { name: "cpu_sys".into(), value: 78.2 },
        MetricSample { name: "io_wait".into(), value: 12.0 },
        MetricSample { name: "mem_pct".into(), value: 88.9 },
    ];

    let high_metrics = filter_and_map_samples(&samples, |s| s.value > threshold);
    assert_eq!(high_metrics, vec![78.2, 88.9]);
    println!("✅ Phase 1 Verified: Immutable capture (&T) correctly filtered {} samples.", high_metrics.len());

    // 2. Mutable capture (&mut T) -> FnMut & Consuming -> FnOnce
    let mut pipeline = AccumulatorPipeline::new();
    let stream = vec![10.0, 20.0, 30.0, 40.0];

    pipeline.process_mut(&stream, |acc, val| {
        *acc += val * 1.1; // 10% overhead factor
    });

    let avg = pipeline.finalize_once(|count, sum| {
        assert_eq!(count, 4);
        sum / count as f64
    });
    assert!((avg - 27.5).abs() < 1e-6);
    println!("✅ Phase 2 Verified: FnMut accumulator & FnOnce finalizer produced average: {:.2}", avg);

    // 3. Move capture across thread boundary -> FnOnce + Send + 'static
    let external_payload = vec![1, 2, 3, 4, 5];
    let computed_sum = TaskDispatcher::spawn_and_compute(move || {
        external_payload.iter().sum::<i32>()
    });
    assert_eq!(computed_sum, 15);
    println!("✅ Phase 3 Verified: Move closure across thread boundary returned sum: {}", computed_sum);

    println!("\n✅ Ep 25 Closures & Fn Traits Architecture successfully verified!");
}
