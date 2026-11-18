// Phase 1: Zero-Copy Lifetime-Bounded Frame Parser
#[derive(Debug, PartialEq, Eq)]
pub struct ZeroCopyFrame<'a> {
    pub topic: &'a str,
    pub body: &'a [u8],
}

impl<'a> ZeroCopyFrame<'a> {
    pub fn parse(raw: &'a [u8], split_idx: usize) -> Option<Self> {
        if split_idx >= raw.len() {
            return None;
        }
        let (head, tail) = raw.split_at(split_idx);
        let topic = std::str::from_utf8(head).ok()?;
        Some(Self { topic, body: tail })
    }

    // Phase 3: Lifetime Elision in Methods & Subtyping
    pub fn extract_preview(&self, max_len: usize) -> &[u8] {
        let len = self.body.len().min(max_len);
        &self.body[..len]
    }
}

// Phase 2: Generic Lifetime Annotations & Reference Elision
pub fn select_longer_payload<'a>(
    left: &'a ZeroCopyFrame<'a>,
    right: &'a ZeroCopyFrame<'a>,
) -> &'a [u8] {
    if left.body.len() >= right.body.len() {
        left.body
    } else {
        right.body
    }
}

fn main() {
    println!("=== Modern Rust Systems Masterclass: Ep 23 ===");
    println!("Lifetimes Fundamentals: Generic Lifetime Annotations & Elision Rules\n");

    let raw1 = b"telemetry.sensors:temp=42.1";
    let frame1 = ZeroCopyFrame::parse(raw1, 17).expect("valid frame");
    println!("Parsed Frame 1: topic='{}', body_len={}", frame1.topic, frame1.body.len());

    let raw2 = b"telemetry.alerts:warning";
    let frame2 = ZeroCopyFrame::parse(raw2, 16).expect("valid frame");
    println!("Parsed Frame 2: topic='{}', body_len={}", frame2.topic, frame2.body.len());

    let longer = select_longer_payload(&frame1, &frame2);
    println!("Longer payload: {} bytes", longer.len());

    let preview = frame1.extract_preview(5);
    println!("Frame 1 preview: {:?}", std::str::from_utf8(preview).unwrap_or(""));

    println!("\n✅ Ep 23 Lifetimes & Reference Elision successfully verified!");
}
