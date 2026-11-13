// Phase 1: Struct Modeling, Default Construction & Derive Macros
use std::fmt;

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ClusterNode {
    pub node_id: String,
    pub bind_addr: String,
    pub max_connections: usize,
    pub auth_secret: String,
}

impl Default for ClusterNode {
    fn default() -> Self {
        Self {
            node_id: "node-primary-01".to_string(),
            bind_addr: "0.0.0.0:8080".to_string(),
            max_connections: 10_000,
            auth_secret: "prod_enc_key_994".to_string(),
        }
    }
}

// Phase 2: Programmer Diagnostics (Debug) vs End-User Formatting (Display)
impl fmt::Display for ClusterNode {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "ClusterNode(id='{}', addr='{}', pool_limit={})",
            self.node_id, self.bind_addr, self.max_connections
        )
    }
}

pub fn spawn_node_with_overrides(bind_addr: Option<String>) -> ClusterNode {
    let base = ClusterNode::default();
    match bind_addr {
        Some(addr) => ClusterNode { bind_addr: addr, ..base },
        None => base,
    }
}

// Phase 3: Clone vs Copy Semantics & Macro Derive Code Generation
pub trait ConfigurableNode: Clone + Default + fmt::Display {
    fn validate_bounds(&self) -> bool;
}

impl ConfigurableNode for ClusterNode {
    fn validate_bounds(&self) -> bool {
        !self.node_id.is_empty() && self.max_connections > 0
    }
}

pub fn duplicate_cluster_nodes<T: ConfigurableNode>(node: &T, count: usize) -> Vec<T> {
    (0..count).map(|_| node.clone()).collect()
}

fn main() {
    println!("Modern Rust Masterclass Episode 20 verified.");
}

