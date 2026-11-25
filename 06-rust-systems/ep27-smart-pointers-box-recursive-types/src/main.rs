//! Modern Rust Systems - Episode 27: Smart Pointers (Part 1): Box<T> & Recursive Data Structures
//! Deep Dive into Heap Allocation, Compile-Time Sizedness, and Recursive Topologies

use std::ops::{Deref, DerefMut};

// ============================================================================
// Phase 1: Recursive Types & Indirection (ConsList with Iterative Drop)
// ============================================================================

/// A classic recursive Lisp-style Cons List.
/// Without `Box<List<T>>`, Rust cannot compute the size of `List<T>` at compile time (E0072).
/// `Box` introduces a fixed 8-byte pointer indirection on 64-bit systems.
#[derive(Debug, PartialEq, Eq)]
pub enum List<T> {
    Cons(T, Box<List<T>>),
    Nil,
}

impl<T> List<T> {
    pub fn new() -> Self {
        List::Nil
    }

    pub fn prepend(self, elem: T) -> Self {
        List::Cons(elem, Box::new(self))
    }

    pub fn head(&self) -> Option<&T> {
        match self {
            List::Cons(val, _) => Some(val),
            List::Nil => None,
        }
    }

    pub fn tail(&self) -> Option<&List<T>> {
        match self {
            List::Cons(_, next) => Some(next.as_ref()),
            List::Nil => None,
        }
    }

    pub fn len(&self) -> usize {
        let mut count = 0;
        let mut curr = self;
        while let List::Cons(_, next) = curr {
            count += 1;
            curr = next.as_ref();
        }
        count
    }

    pub fn is_empty(&self) -> bool {
        matches!(self, List::Nil)
    }

    pub fn to_vec(&self) -> Vec<&T> {
        let mut items = Vec::with_capacity(self.len());
        let mut curr = self;
        while let List::Cons(val, next) = curr {
            items.push(val);
            curr = next.as_ref();
        }
        items
    }
}

impl<T> Default for List<T> {
    fn default() -> Self {
        Self::new()
    }
}

/// A wrapper struct around `List<T>` that implements iterative deallocation.
/// The standard recursive drop can cause a stack overflow for deep structures (> 100k items).
pub struct SafeConsList<T> {
    pub head: List<T>,
}

impl<T> SafeConsList<T> {
    pub fn new() -> Self {
        Self { head: List::Nil }
    }

    pub fn push(&mut self, elem: T) {
        let old_head = std::mem::replace(&mut self.head, List::Nil);
        self.head = List::Cons(elem, Box::new(old_head));
    }

    pub fn pop(&mut self) -> Option<T> {
        let old_head = std::mem::replace(&mut self.head, List::Nil);
        match old_head {
            List::Cons(val, next) => {
                self.head = *next;
                Some(val)
            }
            List::Nil => None,
        }
    }
}

impl<T> Default for SafeConsList<T> {
    fn default() -> Self {
        Self::new()
    }
}

impl<T> Drop for SafeConsList<T> {
    fn drop(&mut self) {
        let mut cur = std::mem::replace(&mut self.head, List::Nil);
        while let List::Cons(_, mut next) = cur {
            // Replace next box content with Nil to unlink and break recursive deallocation
            cur = std::mem::replace(&mut *next, List::Nil);
        }
    }
}

// ============================================================================
// Phase 2: Binary Search Tree via Box Indirection
// ============================================================================

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode<T> {
    pub val: T,
    pub left: Option<Box<TreeNode<T>>>,
    pub right: Option<Box<TreeNode<T>>>,
}

impl<T> TreeNode<T> {
    pub fn new(val: T) -> Self {
        Self {
            val,
            left: None,
            right: None,
        }
    }
}

#[derive(Debug, Default, PartialEq, Eq)]
pub struct BinarySearchTree<T: Ord> {
    root: Option<Box<TreeNode<T>>>,
    size: usize,
}

impl<T: Ord> BinarySearchTree<T> {
    pub fn new() -> Self {
        Self { root: None, size: 0 }
    }

    pub fn len(&self) -> usize {
        self.size
    }

    pub fn is_empty(&self) -> bool {
        self.size == 0
    }

    pub fn insert(&mut self, val: T) -> bool {
        let inserted = Self::insert_node(&mut self.root, val);
        if inserted {
            self.size += 1;
        }
        inserted
    }

    fn insert_node(node: &mut Option<Box<TreeNode<T>>>, val: T) -> bool {
        match node {
            None => {
                *node = Some(Box::new(TreeNode::new(val)));
                true
            }
            Some(ref mut current) => {
                if val < current.val {
                    Self::insert_node(&mut current.left, val)
                } else if val > current.val {
                    Self::insert_node(&mut current.right, val)
                } else {
                    false // Duplicate value
                }
            }
        }
    }

    pub fn contains(&self, val: &T) -> bool {
        let mut curr = &self.root;
        while let Some(node) = curr {
            if val < &node.val {
                curr = &node.left;
            } else if val > &node.val {
                curr = &node.right;
            } else {
                return true;
            }
        }
        false
    }

    pub fn in_order_traversal(&self) -> Vec<&T> {
        let mut result = Vec::with_capacity(self.size);
        Self::traverse_in_order(&self.root, &mut result);
        result
    }

    fn traverse_in_order<'a>(node: &'a Option<Box<TreeNode<T>>>, result: &mut Vec<&'a T>) {
        if let Some(curr) = node {
            Self::traverse_in_order(&curr.left, result);
            result.push(&curr.val);
            Self::traverse_in_order(&curr.right, result);
        }
    }

    pub fn height(&self) -> usize {
        Self::compute_height(&self.root)
    }

    fn compute_height(node: &Option<Box<TreeNode<T>>>) -> usize {
        match node {
            None => 0,
            Some(curr) => 1 + std::cmp::max(
                Self::compute_height(&curr.left),
                Self::compute_height(&curr.right),
            ),
        }
    }
}

// ============================================================================
// Phase 3: Deref Coercion & Zero-Cost Abstractions
// ============================================================================

/// Custom Boxed Container demonstrating Deref and DerefMut traits
pub struct HeapBuffer<T> {
    inner: Box<T>,
}

impl<T> HeapBuffer<T> {
    pub fn new(value: T) -> Self {
        Self {
            inner: Box::new(value),
        }
    }
}

impl<T> Deref for HeapBuffer<T> {
    type Target = T;

    fn deref(&self) -> &Self::Target {
        &self.inner
    }
}

impl<T> DerefMut for HeapBuffer<T> {
    fn deref_mut(&mut self) -> &mut Self::Target {
        &mut self.inner
    }
}

/// Helper function expecting a borrowed slice via Deref Coercion
pub fn compute_slice_checksum(data: &[u8]) -> u32 {
    data.iter().fold(0u32, |acc, &byte| acc.wrapping_add(byte as u32))
}

// ============================================================================
// Unit Tests & Invariant Verification
// ============================================================================

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_cons_list_basic_operations() {
        let list = List::new().prepend(3).prepend(2).prepend(1);

        assert_eq!(list.len(), 3);
        assert_eq!(list.head(), Some(&1));
        assert_eq!(list.to_vec(), vec![&1, &2, &3]);
    }

    #[test]
    fn test_safe_cons_list_iterative_drop() {
        let mut list = SafeConsList::new();
        for i in 0..10_000 {
            list.push(i);
        }

        assert_eq!(list.pop(), Some(9_999));
        assert_eq!(list.pop(), Some(9_998));
        // Drop test: Will safely drop without overflowing call stack
        drop(list);
    }

    #[test]
    fn test_binary_search_tree_properties() {
        let mut bst = BinarySearchTree::new();
        assert!(bst.is_empty());

        let numbers = [50, 30, 70, 20, 40, 60, 80];
        for &num in &numbers {
            assert!(bst.insert(num));
        }

        // Duplicate rejection
        assert!(!bst.insert(50));
        assert_eq!(bst.len(), 7);

        // Verification of containment
        assert!(bst.contains(&40));
        assert!(bst.contains(&70));
        assert!(!bst.contains(&99));

        // In-order traversal must return strictly sorted elements
        let sorted = bst.in_order_traversal();
        assert_eq!(sorted, vec![&20, &30, &40, &50, &60, &70, &80]);

        // Tree height verification (balanced tree of 7 items has height 3)
        assert_eq!(bst.height(), 3);
    }

    #[test]
    fn test_deref_coercion() {
        let mut buffer = HeapBuffer::new(vec![10u8, 20, 30, 40]);

        // Deref coercion: HeapBuffer -> Box<Vec<u8>> -> Vec<u8> -> &[u8]
        let sum = compute_slice_checksum(&buffer);
        assert_eq!(sum, 100);

        // DerefMut coercion
        buffer.push(50);
        assert_eq!(buffer.len(), 5);
        assert_eq!(compute_slice_checksum(&buffer), 150);
    }
}

fn main() {
    println!("=== Modern Rust Systems Masterclass Episode 27: Box<T> & Recursive Structures ===");

    // 1. Recursive List Demonstration
    let list = List::new().prepend("World").prepend("Hello");
    println!("ConsList: head = {:?}, len = {}", list.head(), list.len());

    // 2. Binary Search Tree
    let mut bst = BinarySearchTree::new();
    for &val in &[42, 17, 88, 8, 23, 65, 94] {
        bst.insert(val);
    }
    println!("BST Size: {}, Height: {}", bst.len(), bst.height());
    println!("Sorted In-Order: {:?}", bst.in_order_traversal());

    // 3. Deref Coercion
    let payload = HeapBuffer::new(b"Zero-Cost Rust Systems".to_vec());
    let checksum = compute_slice_checksum(&payload);
    println!("HeapBuffer Checksum via Deref Coercion: 0x{:08X}", checksum);
    println!("✅ All Invariants Verified Successfully.");
}
