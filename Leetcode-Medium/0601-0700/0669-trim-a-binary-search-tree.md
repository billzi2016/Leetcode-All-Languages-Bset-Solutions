# 0669. Trim a Binary Search Tree

## Cpp

```cpp
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
    TreeNode* trimBST(TreeNode* root, int low, int high) {
        if (!root) return nullptr;
        if (root->val < low) {
            // Current node and its left subtree are too small
            return trimBST(root->right, low, high);
        }
        if (root->val > high) {
            // Current node and its right subtree are too large
            return trimBST(root->left, low, high);
        }
        // Node is within range; recursively trim children
        root->left = trimBST(root->left, low, high);
        root->right = trimBST(root->right, low, high);
        return root;
    }
};
```

## Java

```java
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
    public TreeNode trimBST(TreeNode root, int low, int high) {
        if (root == null) return null;
        if (root.val < low) {
            // Current node and its left subtree are too small
            return trimBST(root.right, low, high);
        }
        if (root.val > high) {
            // Current node and its right subtree are too large
            return trimBST(root.left, low, high);
        }
        // Node is within range; recursively trim both subtrees
        root.left = trimBST(root.left, low, high);
        root.right = trimBST(root.right, low, high);
        return root;
    }
}
```

## Python

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
```

## Python3

```python
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional['TreeNode'], low: int, high: int) -> Optional['TreeNode']:
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
```

## C

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* trimBST(struct TreeNode* root, int low, int high) {
    if (!root) return NULL;
    
    // If current node's value is less than low, discard left subtree
    if (root->val < low) {
        struct TreeNode* rightTrimmed = trimBST(root->right, low, high);
        return rightTrimmed;
    }
    
    // If current node's value is greater than high, discard right subtree
    if (root->val > high) {
        struct TreeNode* leftTrimmed = trimBST(root->left, low, high);
        return leftTrimmed;
    }
    
    // Node is within range; recursively trim its children
    root->left = trimBST(root->left, low, high);
    root->right = trimBST(root->right, low, high);
    return root;
}
```

## Csharp

```csharp
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
    public TreeNode TrimBST(TreeNode root, int low, int high) {
        if (root == null) return null;

        if (root.val < low) {
            // Current node and its left subtree are too small
            return TrimBST(root.right, low, high);
        }

        if (root.val > high) {
            // Current node and its right subtree are too large
            return TrimBST(root.left, low, high);
        }

        // Node is within range; recursively trim both subtrees
        root.left = TrimBST(root.left, low, high);
        root.right = TrimBST(root.right, low, high);
        return root;
    }
}
```

## Javascript

```javascript
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} low
 * @param {number} high
 * @return {TreeNode}
 */
var trimBST = function(root, low, high) {
    if (!root) return null;
    if (root.val < low) {
        // Current node and its left subtree are too small; discard them.
        return trimBST(root.right, low, high);
    }
    if (root.val > high) {
        // Current node and its right subtree are too large; discard them.
        return trimBST(root.left, low, high);
    }
    // Node is within range; recursively trim left and right subtrees.
    root.left = trimBST(root.left, low, high);
    root.right = trimBST(root.right, low, high);
    return root;
};
```

## Typescript

```typescript
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

function trimBST(root: TreeNode | null, low: number, high: number): TreeNode | null {
    if (!root) return null;
    if (root.val < low) {
        return trimBST(root.right, low, high);
    }
    if (root.val > high) {
        return trimBST(root.left, low, high);
    }
    root.left = trimBST(root.left, low, high);
    root.right = trimBST(root.right, low, high);
    return root;
}
```

## Php

```php
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
     * @param TreeNode $root
     * @param Integer $low
     * @param Integer $high
     * @return TreeNode|null
     */
    function trimBST($root, $low, $high) {
        if ($root === null) {
            return null;
        }
        if ($root->val < $low) {
            return $this->trimBST($root->right, $low, $high);
        }
        if ($root->val > $high) {
            return $this->trimBST($root->left, $low, $high);
        }
        $root->left = $this->trimBST($root->left, $low, $high);
        $root->right = $this->trimBST($root->right, $low, $high);
        return $root;
    }
}
```

## Swift

```swift
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func trimBST(_ root: TreeNode?, _ low: Int, _ high: Int) -> TreeNode? {
        guard let node = root else { return nil }
        if node.val < low {
            return trimBST(node.right, low, high)
        } else if node.val > high {
            return trimBST(node.left, low, high)
        } else {
            node.left = trimBST(node.left, low, high)
            node.right = trimBST(node.right, low, high)
            return node
        }
    }
}
```

## Kotlin

```kotlin
/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun trimBST(root: TreeNode?, low: Int, high: Int): TreeNode? {
        if (root == null) return null
        return when {
            root.`val` < low -> trimBST(root.right, low, high)
            root.`val` > high -> trimBST(root.left, low, high)
            else -> {
                root.left = trimBST(root.left, low, high)
                root.right = trimBST(root.right, low, high)
                root
            }
        }
    }
}
```

## Dart

```dart
/ **
 * Definition for a binary tree node.
 * class TreeNode {
 *   int val;
 *   TreeNode? left;
 *   TreeNode? right;
 *   TreeNode([this.val = 0, this.left, this.right]);
 * }
 */
class Solution {
  TreeNode? trimBST(TreeNode? root, int low, int high) {
    if (root == null) return null;
    if (root.val < low) {
      // Current node and its left subtree are too small.
      return trimBST(root.right, low, high);
    }
    if (root.val > high) {
      // Current node and its right subtree are too large.
      return trimBST(root.left, low, high);
    }
    // Node is within range; recursively trim both subtrees.
    root.left = trimBST(root.left, low, high);
    root.right = trimBST(root.right, low, high);
    return root;
  }
}
```

## Golang

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func trimBST(root *TreeNode, low int, high int) *TreeNode {
    if root == nil {
        return nil
    }
    if root.Val < low {
        return trimBST(root.Right, low, high)
    }
    if root.Val > high {
        return trimBST(root.Left, low, high)
    }
    root.Left = trimBST(root.Left, low, high)
    root.Right = trimBST(root.Right, low, high)
    return root
}
```

## Ruby

```ruby
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end

def trim_bst(root, low, high)
  return nil if root.nil?
  
  if root.val < low
    # Current node and its left subtree are too small; discard them.
    return trim_bst(root.right, low, high)
  elsif root.val > high
    # Current node and its right subtree are too large; discard them.
    return trim_bst(root.left, low, high)
  else
    # Node is within range; recursively trim both subtrees.
    root.left = trim_bst(root.left, low, high)
    root.right = trim_bst(root.right, low, high)
    return root
  end
end
```

## Scala

```scala
/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def trimBST(root: TreeNode, low: Int, high: Int): TreeNode = {
        if (root == null) return null
        if (root.value < low) {
            // Current node and its left subtree are too small; discard them.
            return trimBST(root.right, low, high)
        }
        if (root.value > high) {
            // Current node and its right subtree are too large; discard them.
            return trimBST(root.left, low, high)
        }
        // Node is within range; recursively trim left and right subtrees.
        root.left = trimBST(root.left, low, high)
        root.right = trimBST(root.right, low, high)
        root
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

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
    pub fn trim_bst(root: Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> Option<Rc<RefCell<TreeNode>>> {
        match root {
            None => None,
            Some(node_rc) => {
                let val = node_rc.borrow().val;
                if val < low {
                    return Self::trim_bst(node_rc.borrow().right.clone(), low, high);
                }
                if val > high {
                    return Self::trim_bst(node_rc.borrow().left.clone(), low, high);
                }
                let left_trimmed = Self::trim_bst(node_rc.borrow().left.clone(), low, high);
                let right_trimmed = Self::trim_bst(node_rc.borrow().right.clone(), low, high);
                {
                    let mut node = node_rc.borrow_mut();
                    node.left = left_trimmed;
                    node.right = right_trimmed;
                }
                Some(node_rc)
            }
        }
    }
}
```

## Racket

```racket
#|
; Definition for a binary tree node.
; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))
|#

(define/contract (trim-bst root low high)
  (-> (or/c tree-node? #f) exact-integer? exact-integer? (or/c tree-node? #f))
  (cond
    [(not root) #f]
    [(< (tree-node-val root) low)
     (trim-bst (tree-node-right root) low high)]
    [(> (tree-node-val root) high)
     (trim-bst (tree-node-left root) low high)]
    [else
     (set-tree-node-left! root (trim-bst (tree-node-left root) low high))
     (set-tree-node-right! root (trim-bst (tree-node-right root) low high))
     root]))
```

## Erlang

```erlang
-spec trim_bst(Root :: #tree_node{} | null, Low :: integer(), High :: integer()) -> #tree_node{} | null.
trim_bst(null, _Low, _High) ->
    null;
trim_bst(Node = #tree_node{val = Val, left = Left, right = Right}, Low, High) when Val < Low ->
    trim_bst(Right, Low, High);
trim_bst(Node = #tree_node{val = Val, left = Left, right = Right}, Low, High) when Val > High ->
    trim_bst(Left, Low, High);
trim_bst(Node = #tree_node{left = Left, right = Right}, Low, High) ->
    NewLeft = trim_bst(Left, Low, High),
    NewRight = trim_bst(Right, Low, High),
    Node#tree_node{left = NewLeft, right = NewRight}.
```

## Elixir

```elixir
defmodule Solution do
  @spec trim_bst(root :: TreeNode.t | nil, low :: integer, high :: integer) :: TreeNode.t | nil
  def trim_bst(nil, _low, _high), do: nil

  def trim_bst(%TreeNode{val: v} = node, low, high) when v < low do
    trim_bst(node.right, low, high)
  end

  def trim_bst(%TreeNode{val: v} = node, low, high) when v > high do
    trim_bst(node.left, low, high)
  end

  def trim_bst(%TreeNode{val: v, left: l, right: r}, low, high) do
    %TreeNode{
      val: v,
      left: trim_bst(l, low, high),
      right: trim_bst(r, low, high)
    }
  end
end
```
