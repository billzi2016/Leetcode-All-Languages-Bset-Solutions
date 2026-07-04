# 0110. Balanced Binary Tree

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
    bool isBalanced(TreeNode* root) {
        return checkHeight(root) != -1;
    }
private:
    int checkHeight(TreeNode* node) {
        if (!node) return 0;
        int left = checkHeight(node->left);
        if (left == -1) return -1;
        int right = checkHeight(node->right);
        if (right == -1) return -1;
        if (abs(left - right) > 1) return -1;
        return std::max(left, right) + 1;
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
    public boolean isBalanced(TreeNode root) {
        return checkHeight(root) != -1;
    }

    private int checkHeight(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int left = checkHeight(node.left);
        if (left == -1) return -1; // left subtree unbalanced
        int right = checkHeight(node.right);
        if (right == -1) return -1; // right subtree unbalanced
        if (Math.abs(left - right) > 1) {
            return -1; // current node unbalanced
        }
        return Math.max(left, right) + 1;
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
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(node):
            if not node:
                return 0
            lh = check(node.left)
            if lh == -1:
                return -1
            rh = check(node.right)
            if rh == -1:
                return -1
            if abs(lh - rh) > 1:
                return -1
            return max(lh, rh) + 1

        return check(root) != -1
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0
            lh = check(node.left)
            if lh == -1:
                return -1
            rh = check(node.right)
            if rh == -1:
                return -1
            if abs(lh - rh) > 1:
                return -1
            return max(lh, rh) + 1

        return check(root) != -1
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

int checkHeight(struct TreeNode* node) {
    if (!node) return 0;
    int left = checkHeight(node->left);
    if (left == -1) return -1;
    int right = checkHeight(node->right);
    if (right == -1) return -1;
    if (abs(left - right) > 1) return -1;
    return (left > right ? left : right) + 1;
}

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isBalanced(struct TreeNode* root) {
    return checkHeight(root) != -1;
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
public class Solution
{
    public bool IsBalanced(TreeNode root)
    {
        return GetHeight(root) != -1;
    }

    private int GetHeight(TreeNode node)
    {
        if (node == null) return 0;

        int leftHeight = GetHeight(node.left);
        if (leftHeight == -1) return -1;

        int rightHeight = GetHeight(node.right);
        if (rightHeight == -1) return -1;

        if (System.Math.Abs(leftHeight - rightHeight) > 1) return -1;

        return System.Math.Max(leftHeight, rightHeight) + 1;
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
var isBalanced = function(root) {
    const check = (node) => {
        if (!node) return 0;
        const leftHeight = check(node.left);
        if (leftHeight === -1) return -1;
        const rightHeight = check(node.right);
        if (rightHeight === -1) return -1;
        if (Math.abs(leftHeight - rightHeight) > 1) return -1;
        return Math.max(leftHeight, rightHeight) + 1;
    };
    return check(root) !== -1;
};
```

## Typescript

```typescript
function isBalanced(root: TreeNode | null): boolean {
    const check = (node: TreeNode | null): number => {
        if (!node) return 0;
        const leftHeight = check(node.left);
        if (leftHeight === -1) return -1;
        const rightHeight = check(node.right);
        if (rightHeight === -1) return -1;
        if (Math.abs(leftHeight - rightHeight) > 1) return -1;
        return Math.max(leftHeight, rightHeight) + 1;
    };
    return check(root) !== -1;
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
     * @return Boolean
     */
    function isBalanced($root) {
        return $this->checkHeight($root) !== -1;
    }

    private function checkHeight($node) {
        if ($node === null) {
            return 0;
        }
        $left = $this->checkHeight($node->left);
        if ($left === -1) {
            return -1;
        }
        $right = $this->checkHeight($node->right);
        if ($right === -1) {
            return -1;
        }
        if (abs($left - $right) > 1) {
            return -1;
        }
        return max($left, $right) + 1;
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
    func isBalanced(_ root: TreeNode?) -> Bool {
        return checkHeight(root) != -1
    }
    
    private func checkHeight(_ node: TreeNode?) -> Int {
        guard let n = node else { return 0 }
        let leftHeight = checkHeight(n.left)
        if leftHeight == -1 { return -1 }
        let rightHeight = checkHeight(n.right)
        if rightHeight == -1 { return -1 }
        if abs(leftHeight - rightHeight) > 1 {
            return -1
        }
        return max(leftHeight, rightHeight) + 1
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
    fun isBalanced(root: TreeNode?): Boolean {
        return height(root) != -1
    }

    private fun height(node: TreeNode?): Int {
        if (node == null) return 0
        val left = height(node.left)
        if (left == -1) return -1
        val right = height(node.right)
        if (right == -1) return -1
        if (kotlin.math.abs(left - right) > 1) return -1
        return kotlin.math.max(left, right) + 1
    }
}
```

## Dart

```dart
import 'dart:math';

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
  bool isBalanced(TreeNode? root) {
    return _height(root) != -1;
  }

  int _height(TreeNode? node) {
    if (node == null) return 0;
    int left = _height(node.left);
    if (left == -1) return -1;
    int right = _height(node.right);
    if (right == -1) return -1;
    if ((left - right).abs() > 1) return -1;
    return max(left, right) + 1;
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
func isBalanced(root *TreeNode) bool {
    return checkHeight(root) != -1
}

func checkHeight(node *TreeNode) int {
    if node == nil {
        return 0
    }
    left := checkHeight(node.Left)
    if left == -1 {
        return -1
    }
    right := checkHeight(node.Right)
    if right == -1 {
        return -1
    }
    if abs(left-right) > 1 {
        return -1
    }
    if left > right {
        return left + 1
    }
    return right + 1
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
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

def is_balanced(root)
  # Returns height if subtree is balanced, otherwise -1.
  check = lambda do |node|
    return 0 unless node
    left_h = check.call(node.left)
    return -1 if left_h == -1
    right_h = check.call(node.right)
    return -1 if right_h == -1
    return -1 if (left_h - right_h).abs > 1
    [left_h, right_h].max + 1
  end

  check.call(root) != -1
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
    def isBalanced(root: TreeNode): Boolean = {
        def height(node: TreeNode): Int = {
            if (node == null) return 0
            val lh = height(node.left)
            if (lh == -1) return -1
            val rh = height(node.right)
            if (rh == -1) return -1
            if (math.abs(lh - rh) > 1) -1 else math.max(lh, rh) + 1
        }
        height(root) != -1
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
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn height(node: Option<Rc<RefCell<TreeNode>>>) -> i32 {
            match node {
                None => 0,
                Some(rc) => {
                    let left_h = height(rc.borrow().left.clone());
                    if left_h == -1 { return -1; }
                    let right_h = height(rc.borrow().right.clone());
                    if right_h == -1 { return -1; }
                    if (left_h - right_h).abs() > 1 {
                        -1
                    } else {
                        std::cmp::max(left_h, right_h) + 1
                    }
                }
            }
        }
        height(root) != -1
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

(define/contract (is-balanced root)
  (-> (or/c tree-node? #f) boolean?)
  (letrec ([check
            (lambda (node)
              (if (not node)
                  (values #t 0)
                  (let-values ([(left-bal left-h) (check (tree-node-left node))]
                               [(right-bal right-h) (check (tree-node-right node))])
                    (define bal? (and left-bal
                                      right-bal
                                      (<= (abs (- left-h right-h)) 1)))
                    (values bal? (add1 (max left-h right-h)))))))])
    (let-values ([(balanced _) (check root)])
      balanced)))
```

## Erlang

```erlang
-module(solution).
-export([is_balanced/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec is_balanced(Root :: #tree_node{} | null) -> boolean().
is_balanced(Root) ->
    {Balanced, _Height} = check(Root),
    Balanced.

check(null) ->
    {true, 0};
check(#tree_node{left=Left, right=Right}) ->
    {BalL, HL} = check(Left),
    {BalR, HR} = check(Right),
    Balanced = BalL andalso BalR andalso (abs(HL - HR) =< 1),
    Height = max(HL, HR) + 1,
    {Balanced, Height}.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_balanced(root :: TreeNode.t() | nil) :: boolean()
  def is_balanced(root) do
    {balanced, _height} = check(root)
    balanced
  end

  defp check(nil), do: {true, 0}

  defp check(%TreeNode{left: left, right: right}) do
    {bal_l, h_l} = check(left)
    {bal_r, h_r} = check(right)

    balanced = bal_l and bal_r and abs(h_l - h_r) <= 1
    height = max(h_l, h_r) + 1
    {balanced, height}
  end
end
```
