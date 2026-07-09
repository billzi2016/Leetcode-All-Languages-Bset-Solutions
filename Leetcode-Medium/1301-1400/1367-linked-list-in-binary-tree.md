# 1367. Linked List in Binary Tree

## Cpp

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        return dfsTree(root, head);
    }
private:
    // Try to match the list starting from current tree node
    bool dfsMatch(TreeNode* node, ListNode* cur) {
        if (!cur) return true;               // all list nodes matched
        if (!node) return false;             // reached leaf without finishing list
        if (node->val != cur->val) return false;
        return dfsMatch(node->left, cur->next) || dfsMatch(node->right, cur->next);
    }
    
    // Traverse the tree and attempt to start matching from each node
    bool dfsTree(TreeNode* node, ListNode* head) {
        if (!node) return false;
        if (dfsMatch(node, head)) return true;
        return dfsTree(node->left, head) || dfsTree(node->right, head);
    }
};
```

## Java

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSubPath(ListNode head, TreeNode root) {
        if (root == null) return false;
        // Try to match starting from current node
        if (matches(root, head)) return true;
        // Otherwise, continue searching in left and right subtrees
        return isSubPath(head, root.left) || isSubPath(head, root.right);
    }
    
    private boolean matches(TreeNode node, ListNode list) {
        if (list == null) return true;          // all list nodes matched
        if (node == null) return false;         // tree path ended prematurely
        if (node.val != list.val) return false; // value mismatch
        
        // Continue matching down either left or right child
        return matches(node.left, list.next) || matches(node.right, list.next);
    }
}
```

## Python

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: Optional[ListNode]
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        import sys
        sys.setrecursionlimit(10000)

        def match(tree_node, list_node):
            if not list_node:
                return True
            if not tree_node:
                return False
            if tree_node.val != list_node.val:
                return False
            return match(tree_node.left, list_node.next) or match(tree_node.right, list_node.next)

        def dfs(node):
            if not node:
                return False
            if match(node, head):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
```

## Python3

```python
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubPath(self, head: Optional['ListNode'], root: Optional['TreeNode']) -> bool:
        if not head:
            return True
        if not root:
            return False

        def match(node: Optional['TreeNode'], lst: Optional['ListNode']) -> bool:
            if not lst:
                return True
            if not node:
                return False
            if node.val != lst.val:
                return False
            return match(node.left, lst.next) or match(node.right, lst.next)

        # check current root as starting point, otherwise recurse on children
        return (match(root, head) or
                self.isSubPath(head, root.left) or
                self.isSubPath(head, root.right))
```

## C

```c
#include <stdbool.h>

/* Definition for singly-linked list. */
struct ListNode {
    int val;
    struct ListNode *next;
};

/* Definition for a binary tree node. */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static bool matchPath(struct TreeNode *node, struct ListNode *head) {
    if (!head) return true;
    if (!node) return false;
    if (node->val != head->val) return false;
    return matchPath(node->left, head->next) || matchPath(node->right, head->next);
}

bool isSubPath(struct ListNode* head, struct TreeNode* root) {
    if (!head) return true;
    if (!root) return false;
    if (matchPath(root, head)) return true;
    return isSubPath(head, root->left) || isSubPath(head, root->right);
}
```

## Csharp

```csharp
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public bool IsSubPath(ListNode head, TreeNode root) {
        if (head == null) return true;
        return Check(root, head);
    }

    private bool Check(TreeNode node, ListNode head) {
        if (node == null) return false;
        if (Match(node, head)) return true;
        return Check(node.left, head) || Check(node.right, head);
    }

    private bool Match(TreeNode node, ListNode list) {
        if (list == null) return true;
        if (node == null) return false;
        if (node.val != list.val) return false;
        return Match(node.left, list.next) || Match(node.right, list.next);
    }
}
```

## Javascript

```javascript
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {ListNode} head
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSubPath = function(head, root) {
    // Try to match the list starting from a given tree node
    const matchFrom = (node, list) => {
        if (!list) return true;               // all list nodes matched
        if (!node) return false;              // reached leaf without finishing list
        if (node.val !== list.val) return false;
        return matchFrom(node.left, list.next) || matchFrom(node.right, list.next);
    };
    
    const dfs = (node) => {
        if (!node) return false;
        if (matchFrom(node, head)) return true;
        return dfs(node.left) || dfs(node.right);
    };
    
    return dfs(root);
};
```

## Typescript

```typescript
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isSubPath(head: ListNode | null, root: TreeNode | null): boolean {
    if (!head) return true;

    const match = (node: TreeNode | null, list: ListNode | null): boolean => {
        if (!list) return true;
        if (!node) return false;
        if (node.val !== list.val) return false;
        return match(node.left, list.next) || match(node.right, list.next);
    };

    const dfsRoot = (node: TreeNode | null): boolean => {
        if (!node) return false;
        if (match(node, head)) return true;
        return dfsRoot(node.left) || dfsRoot(node.right);
    };

    return dfsRoot(root);
}
```

## Php

```php
<?php
/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {

    /**
     * @param ListNode $head
     * @param TreeNode $root
     * @return Boolean
     */
    function isSubPath($head, $root) {
        if ($root === null) {
            return false;
        }
        // Check if the path starts at current root
        if ($this->dfsMatch($root, $head)) {
            return true;
        }
        // Otherwise, try in left and right subtrees
        return $this->isSubPath($head, $root->left) || $this->isSubPath($head, $root->right);
    }

    /**
     * @param TreeNode $node
     * @param ListNode $listNode
     * @return Boolean
     */
    private function dfsMatch($node, $listNode) {
        if ($listNode === null) {
            return true; // all list nodes matched
        }
        if ($node === null) {
            return false;
        }
        if ($node->val !== $listNode->val) {
            return false;
        }
        // Continue matching the next list node with either child
        return $this->dfsMatch($node->left, $listNode->next) || $this->dfsMatch($node->right, $listNode->next);
    }
}
?>
```

## Swift

```swift
class Solution {
    func isSubPath(_ head: ListNode?, _ root: TreeNode?) -> Bool {
        guard let root = root else { return false }
        if match(root, head) {
            return true
        }
        return isSubPath(head, root.left) || isSubPath(head, root.right)
    }
    
    private func match(_ node: TreeNode?, _ list: ListNode?) -> Bool {
        if list == nil { return true }
        guard let node = node else { return false }
        if node.val != list!.val { return false }
        return match(node.left, list?.next) || match(node.right, list?.next)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isSubPath(head: ListNode?, root: TreeNode?): Boolean {
        if (root == null) return false
        return match(root, head) || isSubPath(head, root.left) || isSubPath(head, root.right)
    }

    private fun match(node: TreeNode?, list: ListNode?): Boolean {
        if (list == null) return true
        if (node == null) return false
        if (node.`val` != list.`val`) return false
        return match(node.left, list.next) || match(node.right, list.next)
    }
}
```

## Dart

```dart
/**
 * Definition for singly-linked list.
 * class ListNode {
 *   int val;
 *   ListNode? next;
 *   ListNode([this.val = 0, this.next]);
 * }
 */
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *   int val;
 *   TreeNode? left;
 *   TreeNode? right;
 *   TreeNode([this.val = 0, this.left, this.right]);
 * }
 */
class Solution {
  bool isSubPath(ListNode? head, TreeNode? root) {
    if (head == null) return true;
    if (root == null) return false;
    if (_match(root, head)) return true;
    return isSubPath(head, root.left) || isSubPath(head, root.right);
  }

  bool _match(TreeNode? node, ListNode? list) {
    if (list == null) return true;
    if (node == null) return false;
    if (node.val != list.val) return false;
    return _match(node.left, list.next) || _match(node.right, list.next);
  }
}
```

## Golang

```go
func isSubPath(head *ListNode, root *TreeNode) bool {
	var dfs func(*TreeNode, *ListNode) bool
	dfs = func(node *TreeNode, list *ListNode) bool {
		if list == nil {
			return true
		}
		if node == nil || node.Val != list.Val {
			return false
		}
		return dfs(node.Left, list.Next) || dfs(node.Right, list.Next)
	}

	var traverse func(*TreeNode) bool
	traverse = func(node *TreeNode) bool {
		if node == nil {
			return false
		}
		if dfs(node, head) {
			return true
		}
		return traverse(node.Left) || traverse(node.Right)
	}

	return traverse(root)
}
```

## Ruby

```ruby
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end

def is_sub_path(head, root)
  return false if root.nil?
  return true if match(root, head)
  is_sub_path(head, root.left) || is_sub_path(head, root.right)
end

def match(node, list_node)
  return true if list_node.nil?
  return false if node.nil? || node.val != list_node.val
  match(node.left, list_node.next) || match(node.right, list_node.next)
end
```

## Scala

```scala
/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
  def isSubPath(head: ListNode, root: TreeNode): Boolean = {
    if (head == null) true
    else if (root == null) false
    else dfs(root, head) || isSubPath(head, root.left) || isSubPath(head, root.right)
  }

  private def dfs(node: TreeNode, list: ListNode): Boolean = {
    if (list == null) true
    else if (node == null) false
    else if (node.value != list.x) false
    else dfs(node.left, list.next) || dfs(node.right, list.next)
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }

pub struct Solution;

impl Solution {
    pub fn is_sub_path(head: Option<Box<ListNode>>, root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::dfs_tree(root, &head)
    }

    fn dfs_tree(node_opt: Option<Rc<RefCell<TreeNode>>>, head: &Option<Box<ListNode>>) -> bool {
        if let Some(node_rc) = node_opt {
            if Self::match_from(node_rc.clone(), head) {
                return true;
            }
            let left = node_rc.borrow().left.clone();
            let right = node_rc.borrow().right.clone();
            if Self::dfs_tree(left, head) {
                return true;
            }
            if Self::dfs_tree(right, head) {
                return true;
            }
        }
        false
    }

    fn match_from(node: Rc<RefCell<TreeNode>>, head: &Option<Box<ListNode>>) -> bool {
        // If the list is fully matched
        if head.is_none() {
            return true;
        }
        let node_ref = node.borrow();
        let list_node = match head.as_ref() {
            Some(n) => n,
            None => return true,
        };
        if node_ref.val != list_node.val {
            return false;
        }
        // Prepare for next recursion
        let next_head = &list_node.next;
        if next_head.is_none() {
            return true;
        }
        let left = node_ref.left.clone();
        let right = node_ref.right.clone();
        drop(node_ref); // release borrow before recursive calls

        if let Some(l) = left {
            if Self::match_from(l, next_head) {
                return true;
            }
        }
        if let Some(r) = right {
            if Self::match_from(r, next_head) {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
#lang racket

;; Definition for singly-linked list:
(struct list-node (val next) #:mutable #:transparent)
(define (make-list-node [val 0]) (list-node val #f))

;; Definition for a binary tree node.
(struct tree-node (val left right) #:mutable #:transparent)
(define (make-tree-node [val 0]) (tree-node val #f #f))

(: is-sub-path (-> (or/c list-node? #f) (or/c tree-node? #f) boolean?))
(define (is-sub-path head root)
  ;; helper: try to match the linked list starting from a given tree node
  (define (dfs-match t l)
    (cond [(not l) #t]                     ; all list nodes matched
          [(not t) #f]                     ; tree path ended early
          [else
           (if (= (tree-node-val t) (list-node-val l))
               (or (dfs-match (tree-node-left t) (list-node-next l))
                   (dfs-match (tree-node-right t) (list-node-next l)))
               #f)]))
  ;; main recursion: explore every tree node as a potential start
  (letrec ((search
            (lambda (node)
              (cond [(not node) #f]
                    [else (or (dfs-match node head)
                              (search (tree-node-left node))
                              (search (tree-node-right node)))]))))
    (search root)))
```

## Erlang

```erlang
-module(solution).
-export([is_sub_path/2]).

-record(list_node, {val = 0 :: integer(),
                    next = null :: 'null' | #list_node{}}).

-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec is_sub_path(Head :: #list_node{} | null, Root :: #tree_node{} | null) -> boolean().
is_sub_path(null, _) ->
    true;
is_sub_path(_, null) ->
    false;
is_sub_path(Head, Root) ->
    dfs(Root, Head).

-spec dfs(#tree_node{} | null, #list_node{} | null) -> boolean().
dfs(null, _) ->
    false;
dfs(Node, Head) ->
    match(Node, Head) orelse
    dfs(Node#tree_node.left, Head) orelse
    dfs(Node#tree_node.right, Head).

-spec match(#tree_node{} | null, #list_node{} | null) -> boolean().
match(_, null) ->
    true;
match(null, _) ->
    false;
match(Node, List) when Node#tree_node.val =:= List#list_node.val ->
    match(Node#tree_node.left, List#list_node.next) orelse
    match(Node#tree_node.right, List#list_node.next);
match(_, _) ->
    false.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_sub_path(head :: ListNode.t() | nil, root :: TreeNode.t() | nil) :: boolean()
  def is_sub_path(nil, _), do: true
  def is_sub_path(_, nil), do: false
  def is_sub_path(head, root), do: check(root, head)

  # Check each tree node as a possible start of the list
  defp check(nil, _head), do: false

  defp check(%TreeNode{left: left, right: right} = node, head) do
    dfs(node, head) or check(left, head) or check(right, head)
  end

  # Try to match the list starting from this tree node
  defp dfs(_, nil), do: true
  defp dfs(nil, _list), do: false

  defp dfs(%TreeNode{val: v, left: l, right: r}, %ListNode{val: hv, next: nxt}) do
    if v == hv do
      dfs(l, nxt) or dfs(r, nxt)
    else
      false
    end
  end
end
```
