//! Modern Rust Systems Masterclass: Episode 24
//! Struct Lifetimes, Multiple Lifetimes & The 'static Lifetime Guide

// Phase 1: Structs Holding References & Borrow Invariants
#[derive(Debug)]
pub struct BufferReader<'a> {
    pub raw: &'a [u8],
    pub position: usize,
}

impl<'a> BufferReader<'a> {
    pub fn new(raw: &'a [u8]) -> Self {
        Self { raw, position: 0 }
    }

    pub fn read_bytes(&mut self, count: usize) -> Option<&'a [u8]> {
        if self.position + count <= self.raw.len() {
            let slice = &self.raw[self.position..self.position + count];
            self.position += count;
            Some(slice)
        } else {
            None
        }
    }
}

// Phase 2: Multiple Distinct Lifetime Parameters
#[derive(Debug)]
pub struct DualSlice<'a, 'b> {
    pub header: &'a str,
    pub payload: &'b [u8],
}

impl<'a, 'b> DualSlice<'a, 'b> {
    pub fn new(header: &'a str, payload: &'b [u8]) -> Self {
        Self { header, payload }
    }

    pub fn summary(&self) -> String {
        format!("{}: {} bytes", self.header, self.payload.len())
    }
}

// Phase 3: The 'static Lifetime & Thread Bounds (T: 'static)
use std::thread;

pub fn spawn_worker<T>(val: T) -> thread::JoinHandle<T>
where
    T: Send + 'static,
{
    thread::spawn(move || val)
}

fn main() {
    println!("=== Modern Rust Systems Masterclass: Ep 24 ===");
    println!("Struct Lifetimes, Multiple Lifetimes & The 'static Lifetime\n");

    // Phase 1 Demo
    let buffer = b"PROTO_HEADER_DATA_STREAM";
    let mut reader = BufferReader::new(buffer);
    if let Some(chunk) = reader.read_bytes(12) {
        println!("Reader Chunk 1: {:?}", std::str::from_utf8(chunk).unwrap());
    }
    println!("Remaining bytes: {}", buffer.len() - reader.position);

    // Phase 2 Demo: Dual Lifetimes
    let static_header: &'static str = "GLOBAL_METRICS";
    let local_data = vec![1, 2, 3, 4, 5];
    let dual = DualSlice::new(static_header, &local_data);
    println!("DualSlice Summary: {}", dual.summary());

    // Phase 3 Demo: T: 'static Thread Spawning
    let payload = String::from("Owned Heap Data satisfies 'static bound");
    let handle = spawn_worker(payload);
    let result = handle.join().expect("Worker thread succeeded");
    println!("Thread Result: {}", result);

    println!("\n✅ Ep 24 Struct Lifetimes & 'static successfully verified!");
}
