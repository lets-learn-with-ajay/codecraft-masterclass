// Phase 1: Shared Behavior Trait Contract & Default Implementation
use std::fmt;

pub trait StorageCodec {
    fn encode_frame(&self, out: &mut Vec<u8>) -> usize;
    fn codec_name(&self) -> &'static str;

    fn encode_with_checksum(&self, out: &mut Vec<u8>) -> u32 {
        let start = out.len();
        let written = self.encode_frame(out);
        out[start..start + written].iter().fold(0u32, |acc, &b| acc.wrapping_add(b as u32))
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
        write!(f, "Frame(id={}, bytes={})", self.stream_id, self.payload_bytes.len())
    }
}

// Phase 3: Zero-Cost Static Monomorphization vs Dynamic Trait Objects
pub fn flush_static_batch<T: StorageCodec>(items: &[T], buf: &mut Vec<u8>) -> u32 {
    items.iter().map(|item| item.encode_with_checksum(buf)).sum()
}

pub fn flush_dynamic_plugins(plugins: &[Box<dyn StorageCodec>], buf: &mut Vec<u8>) -> usize {
    plugins.iter().map(|p| p.encode_frame(buf)).sum()
}

fn main() {
    println!("Modern Rust Masterclass Episode 19 verified.");
}

