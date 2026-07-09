# 0951. Flip Equivalent Binary Trees

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
    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        if (!root1 && !root2) return true;
        if (!root1 || !root2) return false;
        if (root1->val != root2->val) return false;
        // No flip case
        bool noFlip = flipEquiv(root1->left,  root2->left) &&
                      flipEquiv(root1->right, root2->right);
        // Flip case
        bool flip   = flipEquiv(root1->left,  root2->right) &&
                      flipEquiv(root1->right, root2->left);
        return noFlip || flip;
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
    public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) return true;
        if (root1 == null || root2 == null) return false;
        if (root1.val != root2.val) return false;
        boolean noSwap = flipEquiv(root1.left, root2.left) && flipEquiv(root1.right, root2.right);
        boolean swap   = flipEquiv(root1.left, root2.right) && flipEquiv(root1.right, root2.left);
        return noSwap || swap;
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
    def flipEquiv(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        # No flip case
        no_flip = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        # Flip case
        flip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        return no_flip or flip
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def flipEquiv(self, root1: Optional['TreeNode'], root2: Optional['TreeNode']) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        # No flip case
        no_flip = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        # Flip case
        flip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        return no_flip or flip
```

## C

```c
#include <stdbool.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool flipEquiv(struct TreeNode* root1, struct TreeNode* root2) {
    if (!root1 && !root2) return true;
    if (!root1 || !root2) return false;
    if (root1->val != root2->val) return false;
    
    bool noSwap = flipEquiv(root1->left,  root2->left) &&
                  flipEquiv(root1->right, root2->right);
    bool swap   = flipEquiv(root1->left,  root2->right) &&
                  flipEquiv(root1->right, root2->left);
    
    return noSwap || swap;
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
    public bool FlipEquiv(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) return true;
        if (root1 == null || root2 == null) return false;
        if (root1.val != root2.val) return false;

        bool noFlip = FlipEquiv(root1.left, root2.left) && FlipEquiv(root1.right, root2.right);
        bool flip   = FlipEquiv(root1.left, root2.right) && FlipEquiv(root1.right, root2.left);

        return noFlip || flip;
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
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var flipEquiv = function(root1, root2) {
    if (!root1 && !root2) return true;
    if (!root1 || !root2) return false;
    if (root1.val !== root2.val) return false;
    
    const withoutSwap = flipEquiv(root1.left, root2.left) && flipEquiv(root1.right, root2.right);
    const withSwap = flipEquiv(root1.left, root2.right) && flipEquiv(root1.right, root2.left);
    
    return withoutSwap || withSwap;
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

function flipEquiv(root1: TreeNode | null, root2: TreeNode | null): boolean {
    if (!root1 && !root2) return true;
    if (!root1 || !root2) return false;
    if (root1.val !== root2.val) return false;

    const withoutFlip = flipEquiv(root1.left, root2.left) && flipEquiv(root1.right, root2.right);
    const withFlip = flipEquiv(root1.left, root2.right) && flipEquiv(root1.right, root2.left);

    return withoutFlip || withFlip;
}
```

## Php

```php
<?php
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
     * @param TreeNode $root1
     * @param TreeNode $root2
     * @return Boolean
     */
    function flipEquiv($root1, $root2) {
        if ($root1 === null && $root2 === null) {
            return true;
        }
        if ($root1 === null || $root2 === null) {
            return false;
        }
        if ($root1->val !== $root2->val) {
            return false;
        }

        $noSwap = $this->flipEquiv($root1->left, $root2->left) && $this->flipEquiv($root1->right, $root2->right);
        $swap    = $this->flipEquiv($root1->left, $root2->right) && $this->flipEquiv($root1->right, $root2->left);

        return $noSwap || $swap;
    }
}
?>
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
    func flipEquiv(_ root1: TreeNode?, _ root2: TreeNode?) -> Bool {
        if root1 == nil && root2 == nil { return true }
        guard let node1 = root1, let node2 = root2 else { return false }
        if node1.val != node2.val { return false }
        let withoutFlip = flipEquiv(node1.left, node2.left) && flipEquiv(node1.right, node2.right)
        let withFlip = flipEquiv(node1.left, node2.right) && flipEquiv(node1.right, node2.left)
        return withoutFlip || withFlip
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
    fun flipEquiv(root1: TreeNode?, root2: TreeNode?): Boolean {
        if (root1 == null && root2 == null) return true
        if (root1 == null || root2 == null) return false
        if (root1.`val` != root2.`val`) return false

        val noFlip = flipEquiv(root1.left, root2.left) && flipEquiv(root1.right, root2.right)
        val flip = flipEquiv(root1.left, root2.right) && flipEquiv(root1.right, root2.left)

        return noFlip || flip
    }
}
```

## Dart

```dart
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
  bool flipEquiv(TreeNode? root1, TreeNode? root2) {
    if (root1 == null && root2 == null) return true;
    if (root1 == null || root2 == null) return false;
    if (root1.val != root2.val) return false;

    // No flip case
    bool noFlip = flipEquiv(root1.left, root2.left) &&
                  flipEquiv(root1.right, root2.right);
    // Flip case
    bool flip = flipEquiv(root1.left, root2.right) &&
                flipEquiv(root1.right, root2.left);

    return noFlip || flip;
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
func flipEquiv(root1 *TreeNode, root2 *TreeNode) bool {
	if root1 == nil && root2 == nil {
		return true
	}
	if root1 == nil || root2 == nil {
		return false
	}
	if root1.Val != root2.Val {
		return false
	}
	// No flip case
	noFlip := flipEquiv(root1.Left, root2.Left) && flipEquiv(root1.Right, root2.Right)
	// Flip case
	flip := flipEquiv(root1.Left, root2.Right) && flipEquiv(root1.Right, root2.Left)
	return noFlip || flip
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

def flip_equiv(root1, root2)
  return true if root1.nil? && root2.nil?
  return false if root1.nil? || root2.nil?
  return false unless root1.val == root2.val

  (flip_equiv(root1.left, root2.left) && flip_equiv(root1.right, root2.right)) ||
    (flip_equiv(root1.left, root2.right) && flip_equiv(root1.right, root2.left))
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
    def flipEquiv(root1: TreeNode, root2: TreeNode): Boolean = {
        if (root1 == null && root2 == null) true
        else if (root1 == null || root2 == null) false
        else if (root1.value != root2.value) false
        else {
            val noSwap = flipEquiv(root1.left, root2.left) && flipEquiv(root1.right, root2.right)
            val swap   = flipEquiv(root1.left, root2.right) && flipEquiv(root1.right, root2.left)
            noSwap || swap
        }
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
    pub fn flip_equiv(
        root1: Option<Rc<RefCell<TreeNode>>>,
        root2: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (root1, root2) {
            (None, None) => true,
            (Some(node1), Some(node2)) => {
                let n1 = node1.borrow();
                let n2 = node2.borrow();
                if n1.val != n2.val {
                    return false;
                }
                // No flip case
                let no_flip_left = Solution::flip_equiv(n1.left.clone(), n2.left.clone());
                let no_flip_right = Solution::flip_equiv(n1.right.clone(), n2.right.clone());
                if no_flip_left && no_flip_right {
                    return true;
                }
                // Flip case
                let flip_left = Solution::flip_equiv(n1.left.clone(), n2.right.clone());
                let flip_right = Solution::flip_equiv(n1.right.clone(), n2.left.clone());
                flip_left && flip_right
            }
            _ => false,
        }
    }
}
```

## Racket

```racket
#lang racket

; Definition for a binary tree node.
#|
(struct tree-node
  (val left right) #:mutable #:transparent)

(define (make-tree-node [val 0])
  (tree-node val #f #f))
|#

(define/contract (flip-equiv root1 root2)
  (-> (or/c tree-node? #f) (or/c tree-node? #f) boolean?)
  (cond
    [(and (not root1) (not root2)) #t]
    [(or (not root1) (not root2)) #f]
    [else
     (if (not (= (tree-node-val root1) (tree-node-val root2)))
         #f
         (let ([l1 (tree-node-left root1)]
               [r1 (tree-node-right root1)]
               [l2 (tree-node-left root2)]
               [r2 (tree-node-right root2)])
           (or (and (flip-equiv l1 l2) (flip-equiv r1 r2))
               (and (flip-equiv l1 r2) (flip-equiv r1 l2)))))]))
```

## Erlang

```erlang
%% Definition for a binary tree node.
-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec flip_equiv(Root1 :: #tree_node{} | null, Root2 :: #tree_node{} | null) -> boolean().
flip_equiv(null, null) ->
    true;
flip_equiv(null, _) ->
    false;
flip_equiv(_, null) ->
    false;
flip_equiv(#tree_node{val = V, left = L1, right = R1},
           #tree_node{val = V, left = L2, right = R2}) ->
    (flip_equiv(L1, L2) andalso flip_equiv(R1, R2)) orelse
    (flip_equiv(L1, R2) andalso flip_equiv(R1, L2));
flip_equiv(_, _) ->
    false.
```

## Elixir

```elixir
defmodule Solution do
  @spec flip_equiv(root1 :: TreeNode.t() | nil, root2 :: TreeNode.t() | nil) :: boolean()
  def flip_equiv(root1, root2), do: equiv?(root1, root2)

  defp equiv?(nil, nil), do: true
  defp equiv?(_, nil), do: false
  defp equiv?(nil, _), do: false

  defp equiv?(%TreeNode{val: v1, left: l1, right: r1}, %TreeNode{val: v2, left: l2, right: r2}) when v1 == v2 do
    (equiv?(l1, l2) and equiv?(r1, r2)) or
      (equiv?(l1, r2) and equiv?(r1, l2))
  end

  defp equiv?(_, _), do: false
end
```
