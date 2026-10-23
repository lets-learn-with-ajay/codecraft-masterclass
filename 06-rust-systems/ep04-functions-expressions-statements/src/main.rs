pub fn calculate_network_latency(rtt_microseconds: u32, packet_loss_basis_points: u16) -> u64 {
    let base_penalty: u64 = if packet_loss_basis_points > 500 {
        15_000
    } else {
        0
    };
    (rtt_microseconds as u64) + base_penalty
}

pub fn format_endpoint(host: &str, port: u16) -> String {
    format!("{}:{}", host, port)
}

fn main() {
    let latency = calculate_network_latency(450, 120);
    let addr = format_endpoint("10.0.0.1", 8080);
    println!("Target {} has computed latency: {} us", addr, latency);
}
