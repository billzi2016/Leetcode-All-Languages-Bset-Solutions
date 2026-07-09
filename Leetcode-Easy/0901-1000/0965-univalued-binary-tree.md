# 0965. Univalued Binary Tree

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
    bool isUnivalTree(TreeNode* root) {
        if (!root) return true;
        int target = root->val;
        return dfs(root, target);
    }
private:
    bool dfs(TreeNode* node, int target) {
        if (!node) return true;
        if (node->val != target) return false;
        return dfs(node->left, target) && dfs(node->right, target);
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
    public boolean isUnivalTree(TreeNode root) {
        if (root == null) return true;
        return dfs(root, root.val);
    }

    private boolean dfs(TreeNode node, int val) {
        if (node == null) return true;
        if (node.val != val) return false;
        return dfs(node.left, val) && dfs(node.right, val);
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
    def isUnivalTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        target = root.val

        def dfs(node):
            if not node:
                return True
            if node.val != target:
                return False
            return dfs(node.left) and dfs(node.right)

        return dfs(root)
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
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        target = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != target:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True
```

## C

```c
#include <stdbool.h>

static bool dfs(struct TreeNode* node, int val) {
    if (node == NULL) return true;
    if (node->val != val) return false;
    return dfs(node->left, val) && dfs(node->right, val);
}

bool isUnivalTree(struct TreeNode* root) {
    if (root == NULL) return true;
    return dfs(root, root->val);
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
    public bool IsUnivalTree(TreeNode root) {
        if (root == null) return true;
        int target = root.val;
        return Check(root, target);
    }

    private bool Check(TreeNode node, int val) {
        if (node == null) return true;
        if (node.val != val) return false;
        return Check(node.left, val) && Check(node.right, val);
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
var isUnivalTree = function(root) {
    if (!root) return true;
    const target = root.val;
    const dfs = (node) => {
        if (!node) return true;
        if (node.val !== target) return false;
        return dfs(node.left) && dfs(node.right);
    };
    return dfs(root);
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

function isUnivalTree(root: TreeNode | null): boolean {
    if (!root) return true;
    const target = root.val;
    const stack: TreeNode[] = [root];
    while (stack.length) {
        const node = stack.pop()!;
        if (node.val !== target) return false;
        if (node.left) stack.push(node.left);
        if (node.right) stack.push(node.right);
    }
    return true;
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
    function isUnivalTree($root) {
        if ($root === null) {
            return true;
        }
        $value = $root->val;
        return $this->dfs($root, $value);
    }

    private function dfs($node, $value) {
        if ($node === null) {
            return true;
        }
        if ($node->val !== $value) {
            return false;
        }
        return $this->dfs($node->left, $value) && $this->dfs($node->right, $value);
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
    func isUnivalTree(_ root: TreeNode?) -> Bool {
        guard let root = root else { return true }
        let target = root.val
        
        func dfs(_ node: TreeNode?) -> Bool {
            guard let node = node else { return true }
            if node.val != target { return false }
            return dfs(node.left) && dfs(node.right)
        }
        
        return dfs(root)
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
    fun isUnivalTree(root: TreeNode?): Boolean {
        if (root == null) return true
        val target = root.`val`
        fun dfs(node: TreeNode?): Boolean {
            if (node == null) return true
            if (node.`val` != target) return false
            return dfs(node.left) && dfs(node.right)
        }
        return dfs(root)
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
  bool isUnivalTree(TreeNode? root) {
    if (root == null) return true;
    final int target = root.val;

    bool dfs(TreeNode? node) {
      if (node == null) return true;
      if (node.val != target) return false;
      return dfs(node.left) && dfs(node.right);
    }

    return dfs(root);
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
func isUnivalTree(root *TreeNode) bool {
	if root == nil {
		return true
	}
	var dfs func(node *TreeNode, val int) bool
	dfs = func(node *TreeNode, val int) bool {
		if node == nil {
			return true
		}
		if node.Val != val {
			return false
		}
		return dfs(node.Left, val) && dfs(node.Right, val)
	}
	return dfs(root, root.Val)
}
```

## Ruby

```ruby
def is_unival_tree(root)
  return true unless root
  target = root.val
  stack = [root]
  until stack.empty?
    node = stack.pop
    return false if node.val != target
    stack << node.left if node.left
    stack << node.right if node.right
  end
  true
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
    def isUnivalTree(root: TreeNode): Boolean = {
        if (root == null) true
        else {
            val target = root.value
            def dfs(node: TreeNode): Boolean = {
                if (node == null) true
                else node.value == target && dfs(node.left) && dfs(node.right)
            }
            dfs(root)
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
    pub fn is_unival_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, target: i32) -> bool {
            match node {
                Some(rc) => {
                    let n = rc.borrow();
                    if n.val != target {
                        return false;
                    }
                    dfs(&n.left, target) && dfs(&n.right, target)
                }
                None => true,
            }
        }

        match &root {
            Some(rc) => {
                let val = rc.borrow().val;
                dfs(&root, val)
            }
            None => true,
        }
    }
}
```

## Racket

```racket
; Definition for a binary tree node.
#|
(struct tree-node
  (val left right) #:mutable #:transparent)

(define (make-tree-node [val 0])
  (tree-node val #f #f))
|#

(define/contract (is-unival-tree root)
  (-> (or/c tree-node? #f) boolean?)
  (if (not root)
      #t
      (let ([target (tree-node-val root)])
        (let recur ((node root))
          (cond [(not node) #t]
                [(= (tree-node-val node) target)
                 (and (recur (tree-node-left node))
                      (recur (tree-node-right node)))]
                [else #f])))))
```

## Erlang

```erlang
-spec is_unival_tree(Root :: #tree_node{} | null) -> boolean().
is_unival_tree(null) ->
    true;
is_unival_tree(Root) ->
    Val = Root#tree_node.val,
    check(Root, Val).

check(null, _) ->
    true;
check(#tree_node{val = V, left = L, right = R}, Val) when V =:= Val ->
    check(L, Val) andalso check(R, Val);
check(_, _) ->
    false.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_unival_tree(root :: TreeNode.t() | nil) :: boolean
  def is_unival_tree(nil), do: true

  def is_unival_tree(%TreeNode{val: val} = root) do
    check(root, val)
  end

  defp check(nil, _target), do: true

  defp check(%TreeNode{val: v, left: l, right: r}, target) do
    if v != target do
      false
    else
      check(l, target) and check(r, target)
    end
  end
end
```
