# 2236. Root Equals Sum of Children

## Cpp

```cpp
/ **
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
    bool checkTree(TreeNode* root) {
        if (!root || !root->left || !root->right) return false;
        return root->val == root->left->val + root->right->val;
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
    public boolean checkTree(TreeNode root) {
        if (root == null || root.left == null || root.right == null) {
            return false;
        }
        return root.val == root.left.val + root.right.val;
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
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root or not root.left or not root.right:
            return False
        return root.val == root.left.val + root.right.val
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == (root.left.val + root.right.val)
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
bool checkTree(struct TreeNode* root) {
    if (!root || !root->left || !root->right) return false;
    return root->val == root->left->val + root->right->val;
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
    public bool CheckTree(TreeNode root) {
        return root != null && root.left != null && root.right != null &&
               root.val == root.left.val + root.right.val;
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
 * @return {boolean}
 */
var checkTree = function(root) {
    if (!root || !root.left || !root.right) return false;
    return root.val === root.left.val + root.right.val;
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

function checkTree(root: TreeNode | null): boolean {
    if (!root || !root.left || !root.right) return false;
    return root.val === (root.left.val + root.right.val);
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
     * @return bool
     */
    function checkTree($root) {
        return $root->val === ($root->left->val + $root->right->val);
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
    func checkTree(_ root: TreeNode?) -> Bool {
        guard let root = root,
              let leftVal = root.left?.val,
              let rightVal = root.right?.val else { return false }
        return root.val == leftVal + rightVal
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
    fun checkTree(root: TreeNode?): Boolean {
        if (root == null || root.left == null || root.right == null) return false
        return root.`val` == root.left!!.`val` + root.right!!.`val`
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
  bool checkTree(TreeNode? root) {
    if (root == null || root.left == null || root.right == null) return false;
    return root.val == (root.left!.val + root.right!.val);
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
func checkTree(root *TreeNode) bool {
    if root == nil || root.Left == nil || root.Right == nil {
        return false
    }
    return root.Val == root.Left.Val+root.Right.Val
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

def check_tree(root)
  return false unless root && root.left && root.right
  root.val == root.left.val + root.right.val
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
    def checkTree(root: TreeNode): Boolean = {
        if (root == null || root.left == null || root.right == null) false
        else root.value == root.left.value + root.right.value
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
    pub fn check_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        if let Some(rc_root) = root {
            let root_ref = rc_root.borrow();
            let left_val = root_ref.left.as_ref().map(|l| l.borrow().val).unwrap_or(0);
            let right_val = root_ref.right.as_ref().map(|r| r.borrow().val).unwrap_or(0);
            root_ref.val == left_val + right_val
        } else {
            false
        }
    }
}
```

## Racket

```racket
(define/contract (check-tree root)
  (-> (or/c tree-node? #f) boolean?)
  (and root
       (let* ([left (tree-node-left root)]
              [right (tree-node-right root)])
         (and left right
              (= (tree-node-val root)
                 (+ (tree-node-val left) (tree-node-val right)))))))
```

## Erlang

```erlang
-module(solution).
-export([check_tree/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec check_tree(Root :: #tree_node{} | null) -> boolean().
check_tree(null) ->
    false;
check_tree(#tree_node{val=V, left=L, right=R}) ->
    LV = case L of
            #tree_node{val=ValL} -> ValL;
            _ -> 0
         end,
    RV = case R of
            #tree_node{val=ValR} -> ValR;
            _ -> 0
         end,
    V =:= LV + RV.
```

## Elixir

```elixir
# Definition for a binary tree node.
#
# defmodule TreeNode do
#   @type t :: %__MODULE__{
#           val: integer,
#           left: TreeNode.t() | nil,
#           right: TreeNode.t() | nil
#         }
#   defstruct val: 0, left: nil, right: nil
# end

defmodule Solution do
  @spec check_tree(root :: TreeNode.t | nil) :: boolean
  def check_tree(nil), do: false

  def check_tree(%TreeNode{
        val: root_val,
        left: %TreeNode{val: left_val},
        right: %TreeNode{val: right_val}
      }) do
    root_val == left_val + right_val
  end

  def check_tree(_), do: false
end
```
