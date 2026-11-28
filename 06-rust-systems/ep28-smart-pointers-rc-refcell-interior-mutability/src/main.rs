//! Modern Rust Systems - Episode 28: Smart Pointers (Part 2)
//! Shared Ownership with Rc<T>, Interior Mutability with RefCell<T>, and Cycle Prevention via Weak<T>

use std::cell::RefCell;
use std::rc::{Rc, Weak};

// ============================================================================
// Phase 1: Shared Ownership with Rc<T> in Directed Acyclic Graphs
// ============================================================================

#[derive(Debug)]
pub struct DAGNode<T> {
    pub value: T,
    pub dependencies: Vec<Rc<DAGNode<T>>>,
}

impl<T> DAGNode<T> {
    pub fn new(value: T) -> Self {
        Self {
            value,
            dependencies: Vec::new(),
        }
    }

    pub fn add_dependency(&mut self, dep: Rc<DAGNode<T>>) {
        self.dependencies.push(dep);
    }
}

// ============================================================================
// Phase 2: Interior Mutability with RefCell<T> & Shared Mutation
// ============================================================================

#[derive(Debug)]
pub struct ObservableState<T> {
    state: RefCell<T>,
    mutation_count: RefCell<usize>,
}

impl<T: Clone> ObservableState<T> {
    pub fn new(initial: T) -> Self {
        Self {
            state: RefCell::new(initial),
            mutation_count: RefCell::new(0),
        }
    }

    pub fn get(&self) -> T {
        self.state.borrow().clone()
    }

    pub fn set(&self, new_val: T) {
        *self.state.borrow_mut() = new_val;
        *self.mutation_count.borrow_mut() += 1;
    }

    pub fn mutations(&self) -> usize {
        *self.mutation_count.borrow()
    }

    pub fn try_mutate<F>(&self, f: F) -> Result<(), &'static str>
    where
        F: FnOnce(&mut T),
    {
        if let Ok(mut borrow) = self.state.try_borrow_mut() {
            f(&mut *borrow);
            *self.mutation_count.borrow_mut() += 1;
            Ok(())
        } else {
            Err("BorrowMutError: Resource is currently borrowed")
        }
    }
}

// ============================================================================
// Phase 3: Graph Trees with Weak<T> to Prevent Reference Cycles
// ============================================================================

#[derive(Debug)]
pub struct TreeNode<T> {
    pub value: T,
    pub parent: RefCell<Weak<TreeNode<T>>>,
    pub children: RefCell<Vec<Rc<TreeNode<T>>>>,
}

impl<T> TreeNode<T> {
    pub fn new(value: T) -> Rc<Self> {
        Rc::new(Self {
            value,
            parent: RefCell::new(Weak::new()),
            children: RefCell::new(Vec::new()),
        })
    }

    pub fn add_child(parent: &Rc<Self>, child: &Rc<Self>) {
        // Child's parent pointer is Weak
        *child.parent.borrow_mut() = Rc::downgrade(parent);
        // Parent's child pointer is Strong
        parent.children.borrow_mut().push(Rc::clone(child));
    }

    pub fn get_parent(&self) -> Option<Rc<TreeNode<T>>> {
        self.parent.borrow().upgrade()
    }
}

fn main() {
    println!("=== Rust Episode 28: Rc<T> & RefCell<T> Masterclass ===");

    // 1. Shared ownership
    let leaf = Rc::new(DAGNode::new("Build Artifact"));
    println!("Leaf initial strong count: {}", Rc::strong_count(&leaf));

    let mut task_a = DAGNode::new("Lint Worker");
    task_a.add_dependency(Rc::clone(&leaf));
    println!("After task A clone strong count: {}", Rc::strong_count(&leaf));

    let mut task_b = DAGNode::new("Test Worker");
    task_b.add_dependency(Rc::clone(&leaf));
    println!("After task B clone strong count: {}", Rc::strong_count(&leaf));

    // 2. Interior mutability
    let config = Rc::new(ObservableState::new(100));
    config.set(200);
    println!("Observable config: {} (Mutations: {})", config.get(), config.mutations());

    // 3. Tree hierarchy with Weak parent pointers
    let root = TreeNode::new("Root Router");
    let child = TreeNode::new("Auth Middleware");
    TreeNode::add_child(&root, &child);

    println!("Root strong count: {}", Rc::strong_count(&root));
    println!("Child parent: {:?}", child.get_parent().map(|p| p.value));
}

// ============================================================================
// Verification Suite
// ============================================================================

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_rc_strong_count_tracking() {
        let base = Rc::new(DAGNode::new(42));
        assert_eq!(Rc::strong_count(&base), 1);

        {
            let mut consumer = DAGNode::new(100);
            consumer.add_dependency(Rc::clone(&base));
            assert_eq!(Rc::strong_count(&base), 2);
        }
        // Consumer dropped: strong count returns to 1
        assert_eq!(Rc::strong_count(&base), 1);
    }

    #[test]
    fn test_refcell_interior_mutability() {
        let state = ObservableState::new(String::from("v1.0.0"));
        assert_eq!(state.get(), "v1.0.0");
        assert_eq!(state.mutations(), 0);

        state.set(String::from("v1.1.0"));
        assert_eq!(state.get(), "v1.1.0");
        assert_eq!(state.mutations(), 1);
    }

    #[test]
    fn test_refcell_borrow_collision_safety() {
        let state = ObservableState::new(10);
        // Active immutable borrow
        let borrow = state.state.borrow();

        // Attempting mutable borrow while borrowed should return Err
        let res = state.try_mutate(|val| *val += 1);
        assert!(res.is_err());
        assert_eq!(res.unwrap_err(), "BorrowMutError: Resource is currently borrowed");

        drop(borrow);
        // Now mutable borrow succeeds
        assert!(state.try_mutate(|val| *val += 5).is_ok());
        assert_eq!(state.get(), 15);
    }

    #[test]
    fn test_weak_pointer_no_reference_cycle() {
        let parent = TreeNode::new("ClusterManager");
        let worker = TreeNode::new("WorkerNode");

        TreeNode::add_child(&parent, &worker);

        // Parent strong count is 1 (worker holds only a Weak pointer)
        assert_eq!(Rc::strong_count(&parent), 1);
        assert_eq!(Rc::weak_count(&parent), 1);

        // Worker can upgrade weak pointer to read parent
        let upgraded = worker.get_parent().expect("Parent should exist");
        assert_eq!(upgraded.value, "ClusterManager");

        // When parent is dropped, upgrade returns None
        drop(upgraded);
        drop(parent);
        assert!(worker.get_parent().is_none());
    }
}
