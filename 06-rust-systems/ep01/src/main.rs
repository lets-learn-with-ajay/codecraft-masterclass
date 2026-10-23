fn main() {
    // Rust's canonical entry point takes zero parameters and returns unit ()
    println!("Welcome to the Modern Rust Systems Masterclass!");
    
    let language: &str = "Rust";
    let edition: u32 = 2021;
    let is_systems_language: bool = true;

    // The exclamation point denotes a macro invocation, not a standard function
    println!("Language: {}, Edition: {}, Systems: {}", language, edition, is_systems_language);
}
