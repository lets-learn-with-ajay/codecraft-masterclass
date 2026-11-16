// Phase 1: Shared Behavior Trait Contract & Default Implementation
use std::fmt;
use std::io::Write;

pub trait StorageCodec {
    fn encode_frame(&self, out: &mut Vec<u8>) -> usize;
    fn codec_name(&self) -> &'static str;

    fn encode_with_checksum(&self, out: &mut Vec<u8>) -> u32 {
        let start = out.len();
        let written = self.encode_frame(out);
        out[start..start + written]
            .iter()
            .fold(0u32, |acc, &b| acc.wrapping_add(b as u32))
    }
}

#[derive(Debug, Clone, Default, PartialEq, Eq)]
pub struct TelemetryFrame {
    pub stream_id: u64,
    pub payload_bytes: Vec<u8>,
}

// Phase 2: Concrete Trait Implementation & Display Diagnostics
impl StorageCodec for TelemetryFrame {
    fn encode_frame(&self, out: &mut Vec<u8>) -> usize {
        out.extend_from_slice(&self.stream_id.to_le_bytes());
        out.extend_from_slice(&self.payload_bytes);
        8 + self.payload_bytes.len()
    }

    fn codec_name(&self) -> &'static str {
        "telemetry_le_v1"
    }
}

impl fmt::Display for TelemetryFrame {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "Frame(id={}, bytes={})",
            self.stream_id,
            self.payload_bytes.len()
        )
    }
}

// Phase 3: Static Monomorphization (impl Trait / Where Clauses) vs Dynamic Dispatch (dyn Trait)
pub fn flush_static_batch<T, W>(items: &[T], sink: &mut W) -> usize
where
    T: StorageCodec + Clone + fmt::Display,
    W: Write,
{
    let mut written = 0;
    for item in items {
        let mut buf = Vec::with_capacity(64);
        item.encode_frame(&mut buf);
        sink.write_all(&buf).ok();
        written += buf.len();
    }
    written
}

pub fn flush_dynamic_plugins(plugins: &[Box<dyn StorageCodec>], buf: &mut Vec<u8>) -> usize {
    plugins.iter().map(|p| p.encode_frame(buf)).sum()
}

fn main() {
    println!("=== Modern Rust Systems Masterclass: Ep 22 ===");
    println!("Static Monomorphization vs Dynamic Dispatch: impl Trait vs dyn Trait\n");

    let frame = TelemetryFrame {
        stream_id: 42,
        payload_bytes: vec![0xDE, 0xAD, 0xBE, 0xEF],
    };

    println!("1. Static Monomorphization (Zero-Cost Inlining):");
    let mut static_sink = Vec::new();
    let static_bytes = flush_static_batch(&[frame.clone()], &mut static_sink);
    println!("   Static batch flushed {} bytes to sink.", static_bytes);

    println!("\n2. Dynamic Dispatch (vtable pointer indirection for heterogeneous collections):");
    let plugins: Vec<Box<dyn StorageCodec>> = vec![Box::new(frame.clone())];
    let mut dyn_buf = Vec::new();
    let dyn_bytes = flush_dynamic_plugins(&plugins, &mut dyn_buf);
    println!("   Dynamic plugins dispatched {} bytes to buffer.", dyn_bytes);

    assert_eq!(static_bytes, dyn_bytes);
    println!("\n✅ Ep 22 Static vs Dynamic Dispatch successfully verified!");
}
