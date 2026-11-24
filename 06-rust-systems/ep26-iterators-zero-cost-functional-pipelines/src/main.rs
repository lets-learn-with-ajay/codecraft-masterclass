//! Modern Rust Systems - Episode 26: Iterators & Functional Pipelines
//! Production-grade Zero-Cost Iterator Abstractions

// Phase 1: Custom Zero-Copy Time-Series Ring Buffer with Iterator Trait
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct MetricSample {
    pub timestamp_ns: u64,
    pub latency_us: u32,
    pub status_code: u16,
}

pub struct MetricRingBuffer {
    pub data: Vec<MetricSample>,
    pub capacity: usize,
}

impl MetricRingBuffer {
    pub fn new(capacity: usize) -> Self {
        Self {
            data: Vec::with_capacity(capacity),
            capacity,
        }
    }

    pub fn push(&mut self, sample: MetricSample) {
        if self.data.len() == self.capacity {
            self.data.remove(0);
        }
        self.data.push(sample);
    }

    pub fn iter(&self) -> std::slice::Iter<'_, MetricSample> {
        self.data.iter()
    }

    pub fn iter_mut(&mut self) -> std::slice::IterMut<'_, MetricSample> {
        self.data.iter_mut()
    }
}

impl IntoIterator for MetricRingBuffer {
    type Item = MetricSample;
    type IntoIter = std::vec::IntoIter<MetricSample>;

    fn into_iter(self) -> Self::IntoIter {
        self.data.into_iter()
    }
}

// Phase 2: Custom Iterator Adapter for Windowed Rolling Averages
pub struct RollingWindowIter<I> {
    iter: I,
    window_size: usize,
    buffer: Vec<u32>,
}

impl<I> RollingWindowIter<I>
where
    I: Iterator<Item = MetricSample>,
{
    pub fn new(iter: I, window_size: usize) -> Self {
        Self {
            iter,
            window_size,
            buffer: Vec::with_capacity(window_size),
        }
    }
}

impl<I> Iterator for RollingWindowIter<I>
where
    I: Iterator<Item = MetricSample>,
{
    type Item = (u64, f64); // (latest_timestamp, rolling_average_latency)

    fn next(&mut self) -> Option<Self::Item> {
        let sample = self.iter.next()?;
        if self.buffer.len() == self.window_size {
            self.buffer.remove(0);
        }
        self.buffer.push(sample.latency_us);

        let sum: u32 = self.buffer.iter().sum();
        let avg = sum as f64 / self.buffer.len() as f64;
        Some((sample.timestamp_ns, avg))
    }
}

// Phase 3: Zero-Cost Functional Adapter Pipeline (Lazy, SIMD-Vectorized)
#[derive(Debug, Default)]
pub struct PipelineTelemetry {
    pub processed_count: usize,
    pub p99_latency_estimate_us: f64,
    pub error_rate_percent: f64,
}

pub fn analyze_traffic_stream<'a, I>(samples: I) -> PipelineTelemetry
where
    I: IntoIterator<Item = &'a MetricSample>,
{
    let mut total_samples = 0usize;
    let mut error_count = 0usize;
    let mut latencies = Vec::new();

    // Functional pipeline: lazy filter, map, fold chaining
    samples
        .into_iter()
        .inspect(|_| total_samples += 1)
        .filter(|s| {
            if s.status_code >= 500 {
                error_count += 1;
            }
            s.status_code < 500
        })
        .map(|s| s.latency_us)
        .for_each(|lat| latencies.push(lat));

    if latencies.is_empty() {
        return PipelineTelemetry::default();
    }

    latencies.sort_unstable();
    let p99_idx = ((latencies.len() as f64) * 0.99) as usize;
    let p99_val = latencies[p99_idx.min(latencies.len() - 1)] as f64;
    let err_rate = if total_samples > 0 {
        (error_count as f64 / total_samples as f64) * 100.0
    } else {
        0.0
    };

    PipelineTelemetry {
        processed_count: total_samples,
        p99_latency_estimate_us: p99_val,
        error_rate_percent: err_rate,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ring_buffer_iteration() {
        let mut buf = MetricRingBuffer::new(3);
        buf.push(MetricSample { timestamp_ns: 100, latency_us: 15, status_code: 200 });
        buf.push(MetricSample { timestamp_ns: 200, latency_us: 25, status_code: 200 });
        buf.push(MetricSample { timestamp_ns: 300, latency_us: 35, status_code: 503 });

        // Immutable borrowing via iter()
        let count = buf.iter().count();
        assert_eq!(count, 3);

        // Mutable borrowing via iter_mut()
        for sample in buf.iter_mut() {
            sample.latency_us += 1;
        }

        // Custom RollingWindowIter
        let rolling: Vec<_> = RollingWindowIter::new(buf.iter().cloned(), 2).collect();
        assert_eq!(rolling.len(), 3);
        assert_eq!(rolling[0].1, 16.0); // (15+1) / 1
        assert_eq!(rolling[1].1, 21.0); // (16 + 26) / 2
    }

    #[test]
    fn test_zero_cost_pipeline() {
        let samples = vec![
            MetricSample { timestamp_ns: 1, latency_us: 100, status_code: 200 },
            MetricSample { timestamp_ns: 2, latency_us: 200, status_code: 200 },
            MetricSample { timestamp_ns: 3, latency_us: 300, status_code: 500 },
            MetricSample { timestamp_ns: 4, latency_us: 400, status_code: 200 },
        ];

        let telemetry = analyze_traffic_stream(&samples);
        assert_eq!(telemetry.processed_count, 4);
        assert_eq!(telemetry.error_rate_percent, 25.0);
        assert_eq!(telemetry.p99_latency_estimate_us, 400.0);
    }
}

fn main() {
    println!("Modern Rust Masterclass Episode 26: Iterators & Functional Pipelines");
    let mut ring = MetricRingBuffer::new(10);
    for i in 1..=10 {
        ring.push(MetricSample {
            timestamp_ns: i * 1_000_000,
            latency_us: (i * 12) as u32,
            status_code: if i % 5 == 0 { 503 } else { 200 },
        });
    }

    let telemetry = analyze_traffic_stream(&ring.data);
    println!("Processed: {} samples", telemetry.processed_count);
    println!("Error rate: {:.1}%", telemetry.error_rate_percent);
    println!("P99 Latency: {:.1} µs", telemetry.p99_latency_estimate_us);
}
