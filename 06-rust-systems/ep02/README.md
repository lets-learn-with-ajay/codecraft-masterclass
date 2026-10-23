# Episode 02: Rust's Primitive Scalar Types: Integers, Floats, Booleans & Characters

> **Series**: 06-rust-systems | **Watch**: [YouTube](https://youtube.com/@letslearnwithajay)

## Overview
Mastering Rust scalar types: signed and unsigned integers (i8 to u128, isize/usize), integer overflow behavior (debug panic vs release wrapping), IEEE 754 floats (f32/f64), booleans, and 4-byte Unicode characters.

## Key Takeaways
- Rust requires explicit integer widths to ensure predictable cross-platform memory layout
- Debug builds trigger runtime panics on integer overflow; release builds wrap using two's complement
- char in Rust is a 4-byte Unicode Scalar Value, supporting emojis and international scripts out of the box

## Running the Code
Follow instructions in the track root README.
