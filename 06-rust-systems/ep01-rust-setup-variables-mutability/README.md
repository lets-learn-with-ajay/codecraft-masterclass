# Episode 01: The Rust Mental Model: Stack vs Heap & The Zero-Cost Philosophy

> **Series**: 06-rust-systems | **Watch**: [YouTube](https://youtube.com/@letslearnwithajay)

## Overview
Deconstructing memory layout, pointer mechanics, and why garbage collectors introduce latency spikes. How the Rust compiler enforces safety at zero runtime cost.

## Key Takeaways
- Stack memory offers instantaneous pointer allocation; Heap memory requires dynamic OS allocator calls
- Zero-cost abstractions guarantee that idiomatic high-level Rust compiles down to optimized machine code equivalent to hand-written C
- Rust enforces memory safety at compile time without any garbage collection stop-the-world pauses

## Running the Code
Follow instructions in the track root README.
