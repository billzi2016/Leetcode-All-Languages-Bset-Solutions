# 2331. Evaluate Boolean Binary Tree

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
    bool evaluateTree(TreeNode* root) {
        if (!root->left && !root->right) {
            // leaf node: 0 -> false, 1 -> true
            return root->val == 1;
        }
        bool leftVal = evaluateTree(root->left);
        bool rightVal = evaluateTree(root->right);
        if (root->val == 2) {          // OR operation
            return leftVal || rightVal;
        } else {                       // AND operation, val == 3
            return leftVal && rightVal;
        }
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
    public boolean evaluateTree(TreeNode root) {
        // Leaf node: value 0 (false) or 1 (true)
        if (root.left == null && root.right == null) {
            return root.val == 1;
        }
        // Recursively evaluate children
        boolean left = evaluateTree(root.left);
        boolean right = evaluateTree(root.right);
        // Non-leaf node: 2 -> OR, 3 -> AND
        if (root.val == 2) { // OR
            return left || right;
        } else { // AND (val == 3)
            return left && right;
        }
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
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        # Leaf node
        if not root.left and not root.right:
            return bool(root.val)
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        if root.val == 2:  # OR operation
            return left_val or right_val
        else:              # AND operation (root.val == 3)
            return left_val and right_val
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
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return root.val == 1
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        if root.val == 2:   # OR
            return left_val or right_val
        else:               # AND (root.val == 3)
            return left_val and right_val
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
bool evaluateTree(struct TreeNode* root) {
    if (!root) return false;
    if (!root->left && !root->right) {
        return root->val == 1;
    }
    bool left = evaluateTree(root->left);
    bool right = evaluateTree(root->right);
    if (root->val == 2) { // OR
        return left || right;
    } else { // AND (value 3)
        return left && right;
    }
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
    public bool EvaluateTree(TreeNode root) {
        return Eval(root);
    }

    private bool Eval(TreeNode node) {
        // Leaf node: value 0 -> false, 1 -> true
        if (node.left == null && node.right == null) {
            return node.val == 1;
        }
        // Non-leaf node: evaluate children first
        bool left = Eval(node.left);
        bool right = Eval(node.right);
        // 2 => OR, 3 => AND
        if (node.val == 2) {
            return left || right;
        } else { // node.val == 3
            return left && right;
        }
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
var evaluateTree = function(root) {
    // Base case: leaf node
    if (!root.left && !root.right) {
        return root.val === 1;
    }
    const leftVal = evaluateTree(root.left);
    const rightVal = evaluateTree(root.right);
    if (root.val === 2) { // OR operation
        return leftVal || rightVal;
    } else { // AND operation, root.val === 3
        return leftVal && rightVal;
    }
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

function evaluateTree(root: TreeNode | null): boolean {
    if (!root) return false;
    // Leaf node
    if (!root.left && !root.right) {
        return root.val === 1;
    }
    const leftVal = evaluateTree(root.left);
    const rightVal = evaluateTree(root.right);
    if (root.val === 2) { // OR operation
        return leftVal || rightVal;
    } else { // AND operation (val === 3)
        return leftVal && rightVal;
    }
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
    function evaluateTree($root) {
        if ($root === null) {
            return false;
        }
        // Leaf node: value 0 (false) or 1 (true)
        if ($root->left === null && $root->right === null) {
            return $root->val == 1;
        }
        // Recursively evaluate children
        $leftVal = $this->evaluateTree($root->left);
        $rightVal = $this->evaluateTree($root->right);
        // Non-leaf node: 2 => OR, 3 => AND
        if ($root->val == 2) {
            return $leftVal || $rightVal;
        } else { // $root->val == 3
            return $leftVal && $rightVal;
        }
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
    func evaluateTree(_ root: TreeNode?) -> Bool {
        guard let node = root else { return false }
        // Leaf node: value 0 (false) or 1 (true)
        if node.left == nil && node.right == nil {
            return node.val == 1
        }
        let leftResult = evaluateTree(node.left)
        let rightResult = evaluateTree(node.right)
        // Non-leaf node: 2 => OR, 3 => AND
        if node.val == 2 {
            return leftResult || rightResult
        } else { // node.val == 3
            return leftResult && rightResult
        }
    }
}
```

## Kotlin

```kotlin
/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun evaluateTree(root: TreeNode?): Boolean {
        if (root == null) return false
        // Leaf node
        if (root.left == null && root.right == null) {
            return root.`val` == 1
        }
        val leftVal = evaluateTree(root.left)
        val rightVal = evaluateTree(root.right)
        return when (root.`val`) {
            2 -> leftVal || rightVal   // OR
            else -> leftVal && rightVal // AND (value 3)
        }
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
  bool evaluateTree(TreeNode? root) {
    if (root == null) return false;
    // Leaf node: value is 0 (false) or 1 (true)
    if (root.left == null && root.right == null) {
      return root.val == 1;
    }
    // Recursively evaluate children
    bool left = evaluateTree(root.left);
    bool right = evaluateTree(root.right);
    // Non-leaf node: 2 => OR, 3 => AND
    if (root.val == 2) {
      return left || right;
    } else { // root.val == 3
      return left && right;
    }
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
func evaluateTree(root *TreeNode) bool {
    if root == nil {
        return false
    }
    // Leaf node: value 0 (false) or 1 (true)
    if root.Left == nil && root.Right == nil {
        return root.Val == 1
    }
    left := evaluateTree(root.Left)
    right := evaluateTree(root.Right)
    if root.Val == 2 { // OR operation
        return left || right
    }
    // AND operation (root.Val == 3)
    return left && right
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

def evaluate_tree(root)
  return false if root.nil?
  # Leaf node: value is 0 (false) or 1 (true)
  if root.left.nil? && root.right.nil?
    return root.val == 1
  end

  left_val = evaluate_tree(root.left)
  right_val = evaluate_tree(root.right)

  case root.val
  when 2 # OR
    left_val || right_val
  when 3 # AND
    left_val && right_val
  else
    false
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
    def evaluateTree(root: TreeNode): Boolean = {
        if (root == null) false
        else if (root.left == null && root.right == null) {
            root.value == 1
        } else {
            val leftVal = evaluateTree(root.left)
            val rightVal = evaluateTree(root.right)
            root.value match {
                case 2 => leftVal || rightVal   // OR
                case _ => leftVal && rightVal   // AND (value == 3)
            }
        }
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn evaluate_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn eval(node: &Rc<RefCell<TreeNode>>) -> bool {
            let n = node.borrow();
            match (n.left.clone(), n.right.clone()) {
                (None, None) => n.val == 1,
                (Some(l), Some(r)) => {
                    let left = eval(&l);
                    let right = eval(&r);
                    if n.val == 2 { left || right } else { left && right }
                },
                _ => false,
            }
        }

        match root {
            Some(node) => eval(&node),
            None => false,
        }
    }
}
```

## Racket

```racket
; Definition for a binary tree node.
#|
; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))
|#

(define/contract (evaluate-tree root)
  (-> (or/c tree-node? #f) boolean?)
  (letrec ((dfs
            (lambda (node)
              (cond
                [(not node) #false]
                [(and (not (tree-node-left node))
                      (not (tree-node-right node)))
                 (= (tree-node-val node) 1)]
                [else
                 (let ((l (dfs (tree-node-left node)))
                       (r (dfs (tree-node-right node))))
                   (case (tree-node-val node)
                     [(2) (or l r)]   ; OR
                     [(3) (and l r)]  ; AND
                     [else #false]))]))))
    (dfs root)))
```

## Erlang

```erlang
%% Definition for a binary tree node.
-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-export([evaluate_tree/1]).

-spec evaluate_tree(Root :: #tree_node{} | null) -> boolean().
evaluate_tree(null) ->
    false;
evaluate_tree(Root) when is_record(Root, tree_node) ->
    case {Root#tree_node.left, Root#tree_node.right} of
        {null, null} ->
            Root#tree_node.val =:= 1;
        _ ->
            L = evaluate_tree(Root#tree_node.left),
            R = evaluate_tree(Root#tree_node.right),
            case Root#tree_node.val of
                2 -> L orelse R;   % OR operation
                3 -> L andalso R   % AND operation
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec evaluate_tree(root :: TreeNode.t | nil) :: boolean
  def evaluate_tree(nil), do: false

  def evaluate_tree(%TreeNode{left: nil, right: nil, val: v}) do
    v == 1
  end

  def evaluate_tree(%TreeNode{val: v, left: l, right: r}) do
    left = evaluate_tree(l)
    right = evaluate_tree(r)

    case v do
      2 -> left or right
      3 -> left and right
    end
  end
end
```
