#[derive(Debug, Clone)]
pub struct PacketHeader {
    pub seq_id: u64,
    pub timestamp_ns: u128,
    pub flags: u16,
}

pub struct NetworkBuffer {
    pub header: PacketHeader,
    pub payload: Box<[u8]>,
}

pub fn process_stream(buffers: &[NetworkBuffer]) -> u64 {
    buffers
        .iter()
        .filter(|b| b.header.flags & 0x01 != 0)
        .map(|b| b.header.seq_id)
        .fold(0u64, |acc, id| acc.wrapping_add(id))
}

fn main() {
    let packet = NetworkBuffer {
        header: PacketHeader { seq_id: 1001, timestamp_ns: 0, flags: 0x01 },
        payload: vec![0u8; 1024].into_boxed_slice(),
    };
    let count = process_stream(&[packet]);
    println!("Processed stream total: {}", count);
}
