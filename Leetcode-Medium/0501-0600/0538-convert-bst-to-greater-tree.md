# 0538. Convert BST to Greater Tree

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
    TreeNode* convertBST(TreeNode* root) {
        long long sum = 0;
        std::function<void(TreeNode*)> dfs = [&](TreeNode* node) {
            if (!node) return;
            dfs(node->right);
            sum += node->val;
            node->val = static_cast<int>(sum);
            dfs(node->left);
        };
        dfs(root);
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
    private int sum = 0;
    
    public TreeNode convertBST(TreeNode root) {
        traverse(root);
        return root;
    }
    
    private void traverse(TreeNode node) {
        if (node == null) {
            return;
        }
        traverse(node.right);
        sum += node.val;
        node.val = sum;
        traverse(node.left);
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
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        total = 0
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
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
    def convertBST(self, root: Optional['TreeNode']) -> Optional['TreeNode']:
        total = 0
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
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
static void dfs(struct TreeNode* node, long long *sum) {
    if (!node) return;
    dfs(node->right, sum);
    *sum += node->val;
    node->val = (int)(*sum);
    dfs(node->left, sum);
}

struct TreeNode* convertBST(struct TreeNode* root) {
    long long sum = 0;
    dfs(root, &sum);
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
    private int _sum = 0;
    
    public TreeNode ConvertBST(TreeNode root) {
        Traverse(root);
        return root;
    }
    
    private void Traverse(TreeNode node) {
        if (node == null) return;
        // Visit right subtree first (greater values)
        Traverse(node.right);
        // Update cumulative sum and node value
        _sum += node.val;
        node.val = _sum;
        // Then visit left subtree
        Traverse(node.left);
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
 * @return {TreeNode}
 */
var convertBST = function(root) {
    let sum = 0;
    const dfs = (node) => {
        if (!node) return;
        dfs(node.right);
        sum += node.val;
        node.val = sum;
        dfs(node.left);
    };
    dfs(root);
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

function convertBST(root: TreeNode | null): TreeNode | null {
    let sum = 0;
    const dfs = (node: TreeNode | null): void => {
        if (!node) return;
        dfs(node.right);
        sum += node.val;
        node.val = sum;
        dfs(node.left);
    };
    dfs(root);
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
    private int $sum = 0;

    /**
     * @param TreeNode|null $root
     * @return TreeNode|null
     */
    function convertBST($root) {
        $this->dfs($root);
        return $root;
    }

    private function dfs(?TreeNode $node): void {
        if ($node === null) {
            return;
        }
        $this->dfs($node->right);
        $this->sum += $node->val;
        $node->val = $this->sum;
        $this->dfs($node->left);
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
    func convertBST(_ root: TreeNode?) -> TreeNode? {
        var sum = 0
        func traverse(_ node: TreeNode?) {
            guard let n = node else { return }
            traverse(n.right)
            sum += n.val
            n.val = sum
            traverse(n.left)
        }
        traverse(root)
        return root
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
    fun convertBST(root: TreeNode?): TreeNode? {
        var sum = 0
        fun dfs(node: TreeNode?) {
            if (node == null) return
            dfs(node.right)
            sum += node.`val`
            node.`val` = sum
            dfs(node.left)
        }
        dfs(root)
        return root
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
  int _sum = 0;

  TreeNode? convertBST(TreeNode? root) {
    _traverse(root);
    return root;
  }

  void _traverse(TreeNode? node) {
    if (node == null) return;
    _traverse(node.right);
    _sum += node.val;
    node.val = _sum;
    _traverse(node.left);
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
func convertBST(root *TreeNode) *TreeNode {
	var sum int
	var dfs func(*TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		dfs(node.Right)
		sum += node.Val
		node.Val = sum
		dfs(node.Left)
	}
	dfs(root)
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

def convert_bst(root)
  sum = 0
  dfs = nil
  dfs = ->(node) {
    return if node.nil?
    dfs.call(node.right)
    sum += node.val
    node.val = sum
    dfs.call(node.left)
  }
  dfs.call(root)
  root
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
    def convertBST(root: TreeNode): TreeNode = {
        var sum = 0
        def dfs(node: TreeNode): Unit = {
            if (node == null) return
            dfs(node.right)
            sum += node.value
            node.value = sum
            dfs(node.left)
        }
        dfs(root)
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

impl Solution {
    pub fn convert_bst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        fn dfs(node_opt: Option<Rc<RefCell<TreeNode>>>, sum: &mut i32) {
            if let Some(rc_node) = node_opt {
                // Process right subtree first
                let right = { rc_node.borrow().right.clone() };
                dfs(right, sum);
                
                // Update current node and then process left subtree
                let left = {
                    let mut node = rc_node.borrow_mut();
                    *sum += node.val;
                    node.val = *sum;
                    node.left.clone()
                };
                dfs(left, sum);
            }
        }

        let mut acc = 0;
        dfs(root.clone(), &mut acc);
        root
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

(define/contract (convert-bst root)
  (-> (or/c tree-node? #f) (or/c tree-node? #f))
  (let ((sum 0))
    (define (dfs node)
      (when node
        (dfs (tree-node-right node))
        (set-tree-node-val! node (+ (tree-node-val node) sum))
        (set! sum (tree-node-val node))
        (dfs (tree-node-left node))))
    (dfs root)
    root))
```

## Erlang

```erlang
-module(solution).
-export([convert_bst/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec convert_bst(Root :: #tree_node{} | null) -> #tree_node{} | null.
convert_bst(null) ->
    null;
convert_bst(Root) ->
    {NewRoot, _} = convert(Root, 0),
    NewRoot.

convert(null, Acc) ->
    {null, Acc};
convert(Node, Acc) ->
    {RightNode, Acc1} = convert(Node#tree_node.right, Acc),
    NewVal = Node#tree_node.val + Acc1,
    {LeftNode, Acc2} = convert(Node#tree_node.left, NewVal),
    NewNode = #tree_node{val = NewVal, left = LeftNode, right = RightNode},
    {NewNode, Acc2}.
```

## Elixir

```elixir
defmodule Solution do
  @spec convert_bst(root :: TreeNode.t | nil) :: TreeNode.t | nil
  def convert_bst(root) do
    {new_root, _} = traverse(root, 0)
    new_root
  end

  defp traverse(nil, acc), do: {nil, acc}

  defp traverse(%TreeNode{val: val, left: left, right: right} = node, acc) do
    {right_node, acc1} = traverse(right, acc)
    new_val = val + acc1
    {left_node, acc2} = traverse(left, new_val)

    {%TreeNode{node | val: new_val, left: left_node, right: right_node}, acc2}
  end
end
```
