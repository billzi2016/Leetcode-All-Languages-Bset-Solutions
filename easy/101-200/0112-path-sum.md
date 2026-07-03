# 0112. Path Sum

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
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (!root) return false;
        if (!root->left && !root->right) return root->val == targetSum;
        int remaining = targetSum - root->val;
        return hasPathSum(root->left, remaining) || hasPathSum(root->right, remaining);
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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        // If it's a leaf node, check if the remaining sum equals node's value
        if (root.left == null && root.right == null) {
            return targetSum == root.val;
        }
        int newTarget = targetSum - root.val;
        return hasPathSum(root.left, newTarget) || hasPathSum(root.right, newTarget);
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
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        # If it's a leaf node, check if the remaining sum equals node's value
        if not root.left and not root.right:
            return targetSum == root.val
        # Recurse on children with updated sum
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
```

## Python3

```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # If it's a leaf node, check the remaining sum.
        if not root.left and not root.right:
            return root.val == targetSum
        # Recurse on children with updated target sum.
        new_sum = targetSum - root.val
        return (self.hasPathSum(root.left, new_sum) or
                self.hasPathSum(root.right, new_sum))
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
bool hasPathSum(struct TreeNode* root, int targetSum) {
    if (!root) return false;
    if (!root->left && !root->right)
        return targetSum == root->val;
    int remaining = targetSum - root->val;
    return hasPathSum(root->left, remaining) || hasPathSum(root->right, remaining);
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
    public bool HasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        if (root.left == null && root.right == null) {
            return targetSum == root.val;
        }
        int remaining = targetSum - root.val;
        return HasPathSum(root.left, remaining) || HasPathSum(root.right, remaining);
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
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
    if (!root) return false;
    if (!root.left && !root.right) {
        return root.val === targetSum;
    }
    const remaining = targetSum - root.val;
    return hasPathSum(root.left, remaining) || hasPathSum(root.right, remaining);
};
```

## Typescript

```typescript
function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
    if (root === null) return false;
    if (root.left === null && root.right === null) {
        return root.val === targetSum;
    }
    const remaining = targetSum - root.val;
    return hasPathSum(root.left, remaining) || hasPathSum(root.right, remaining);
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
     * @param Integer $targetSum
     * @return Boolean
     */
    function hasPathSum($root, $targetSum) {
        if ($root === null) {
            return false;
        }
        // If it's a leaf node, check if the remaining sum equals node's value
        if ($root->left === null && $root->right === null) {
            return $root->val == $targetSum;
        }
        $remaining = $targetSum - $root->val;
        return $this->hasPathSum($root->left, $remaining) || $this->hasPathSum($root->right, $remaining);
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
    func hasPathSum(_ root: TreeNode?, _ targetSum: Int) -> Bool {
        guard let node = root else { return false }
        if node.left == nil && node.right == nil {
            return node.val == targetSum
        }
        let remaining = targetSum - node.val
        return hasPathSum(node.left, remaining) || hasPathSum(node.right, remaining)
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
    fun hasPathSum(root: TreeNode?, targetSum: Int): Boolean {
        if (root == null) return false
        // If it's a leaf, check the remaining sum.
        if (root.left == null && root.right == null) {
            return root.`val` == targetSum
        }
        val nextTarget = targetSum - root.`val`
        return hasPathSum(root.left, nextTarget) || hasPathSum(root.right, nextTarget)
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
  bool hasPathSum(TreeNode? root, int targetSum) {
    if (root == null) return false;
    if (root.left == null && root.right == null) {
      return targetSum == root.val;
    }
    int remaining = targetSum - root.val;
    return hasPathSum(root.left, remaining) || hasPathSum(root.right, remaining);
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
func hasPathSum(root *TreeNode, targetSum int) bool {
    if root == nil {
        return false
    }
    if root.Left == nil && root.Right == nil {
        return targetSum == root.Val
    }
    remaining := targetSum - root.Val
    return hasPathSum(root.Left, remaining) || hasPathSum(root.Right, remaining)
}
```

## Ruby

```ruby
def has_path_sum(root, target_sum)
  return false if root.nil?
  if root.left.nil? && root.right.nil?
    return root.val == target_sum
  end
  remaining = target_sum - root.val
  has_path_sum(root.left, remaining) || has_path_sum(root.right, remaining)
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
    def hasPathSum(root: TreeNode, targetSum: Int): Boolean = {
        if (root == null) return false
        if (root.left == null && root.right == null) {
            return root.value == targetSum
        }
        val remaining = targetSum - root.value
        hasPathSum(root.left, remaining) || hasPathSum(root.right, remaining)
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

impl Solution {
    pub fn has_path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> bool {
        match root {
            None => false,
            Some(node_rc) => {
                let node = node_rc.borrow();
                let val = node.val;
                if node.left.is_none() && node.right.is_none() {
                    return val == target_sum;
                }
                let remaining = target_sum - val;
                Solution::has_path_sum(node.left.clone(), remaining)
                    || Solution::has_path_sum(node.right.clone(), remaining)
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

(define/contract (has-path-sum root targetSum)
  (-> (or/c tree-node? #f) exact-integer? boolean?)
  (if (not root)
      #f
      (let ((val   (tree-node-val root))
            (left  (tree-node-left root))
            (right (tree-node-right root)))
        (if (and (not left) (not right))
            (= val targetSum)
            (or (has-path-sum left (- targetSum val))
                (has-path-sum right (- targetSum val)))))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec has_path_sum(Root :: #tree_node{} | null, TargetSum :: integer()) -> boolean().
has_path_sum(null, _) ->
    false;
has_path_sum(#tree_node{val = Val, left = Left, right = Right}, Target) ->
    Remaining = Target - Val,
    case {Left, Right} of
        {null, null} ->
            Remaining == 0;
        _ ->
            has_path_sum(Left, Remaining) orelse has_path_sum(Right, Remaining)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec has_path_sum(root :: TreeNode.t() | nil, target_sum :: integer) :: boolean
  def has_path_sum(nil, _), do: false

  def has_path_sum(%TreeNode{val: v, left: nil, right: nil}, target) do
    v == target
  end

  def has_path_sum(%TreeNode{val: v, left: l, right: r}, target) do
    new_target = target - v
    has_path_sum(l, new_target) or has_path_sum(r, new_target)
  end
end
```
