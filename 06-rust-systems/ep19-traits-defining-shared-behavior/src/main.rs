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

fn main() {
    println!("Modern Rust Masterclass Episode 19 initialized.");
}

