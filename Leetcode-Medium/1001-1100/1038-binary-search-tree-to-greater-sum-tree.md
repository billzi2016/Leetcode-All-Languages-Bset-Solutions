# 1038. Binary Search Tree to Greater Sum Tree

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
    TreeNode* bstToGst(TreeNode* root) {
        sum = 0;
        dfs(root);
        return root;
    }
private:
    int sum;
    void dfs(TreeNode* node) {
        if (!node) return;
        dfs(node->right);
        sum += node->val;
        node->val = sum;
        dfs(node->left);
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
    
    public TreeNode bstToGst(TreeNode root) {
        reverseInorder(root);
        return root;
    }
    
    private void reverseInorder(TreeNode node) {
        if (node == null) return;
        reverseInorder(node.right);
        sum += node.val;
        node.val = sum;
        reverseInorder(node.left);
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
    def bstToGst(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self._sum = 0

        def reverse_inorder(node):
            if not node:
                return
            reverse_inorder(node.right)
            self._sum += node.val
            node.val = self._sum
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root
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
    def bstToGst(self, root):
        self._sum = 0

        def reverse_inorder(node):
            if not node:
                return
            reverse_inorder(node.right)
            self._sum += node.val
            node.val = self._sum
            reverse_inorder(node.left)

        reverse_inorder(root)
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
static void reverseInorder(struct TreeNode* node, int *acc) {
    if (node == NULL) return;
    reverseInorder(node->right, acc);
    *acc += node->val;
    node->val = *acc;
    reverseInorder(node->left, acc);
}

struct TreeNode* bstToGst(struct TreeNode* root) {
    int sum = 0;
    reverseInorder(root, &sum);
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
    private int sum = 0;
    
    public TreeNode BstToGst(TreeNode root) {
        Convert(root);
        return root;
    }
    
    private void Convert(TreeNode node) {
        if (node == null) return;
        Convert(node.right);
        sum += node.val;
        node.val = sum;
        Convert(node.left);
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
var bstToGst = function(root) {
    let sum = 0;
    const traverse = (node) => {
        if (!node) return;
        traverse(node.right);
        sum += node.val;
        node.val = sum;
        traverse(node.left);
    };
    traverse(root);
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

function bstToGst(root: TreeNode | null): TreeNode | null {
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
     * @param TreeNode $root
     * @return TreeNode
     */
    function bstToGst($root) {
        $sum = 0;
        $this->reverseInorder($root, $sum);
        return $root;
    }

    private function reverseInorder($node, &$sum) {
        if ($node === null) {
            return;
        }
        $this->reverseInorder($node->right, $sum);
        $sum += $node->val;
        $node->val = $sum;
        $this->reverseInorder($node->left, $sum);
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
    private var sum = 0
    
    func bstToGst(_ root: TreeNode?) -> TreeNode? {
        dfs(root)
        return root
    }
    
    private func dfs(_ node: TreeNode?) {
        guard let node = node else { return }
        dfs(node.right)
        sum += node.val
        node.val = sum
        dfs(node.left)
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
    private var sum = 0

    fun bstToGst(root: TreeNode?): TreeNode? {
        traverse(root)
        return root
    }

    private fun traverse(node: TreeNode?) {
        if (node == null) return
        traverse(node.right)
        sum += node.`val`
        node.`val` = sum
        traverse(node.left)
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

  TreeNode? bstToGst(TreeNode? root) {
    _reverseInorder(root);
    return root;
  }

  void _reverseInorder(TreeNode? node) {
    if (node == null) return;
    _reverseInorder(node.right);
    _sum += node.val;
    node.val = _sum;
    _reverseInorder(node.left);
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
func bstToGst(root *TreeNode) *TreeNode {
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
def bst_to_gst(root)
  sum = 0
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
  def bstToGst(root: TreeNode): TreeNode = {
    var sum = 0
    def reverseInorder(node: TreeNode): Unit = {
      if (node == null) return
      reverseInorder(node.right)
      sum += node.value
      node.value = sum
      reverseInorder(node.left)
    }
    reverseInorder(root)
    root
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn bst_to_gst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, acc: &mut i32) {
            if let Some(rc_node) = node {
                // Traverse right subtree first (greater values)
                let right = rc_node.borrow().right.clone();
                dfs(right, acc);
                
                // Update current node's value with accumulated sum
                {
                    let mut n = rc_node.borrow_mut();
                    *acc += n.val;
                    n.val = *acc;
                }
                
                // Then traverse left subtree
                let left = rc_node.borrow().left.clone();
                dfs(left, acc);
            }
        }

        let mut sum = 0;
        dfs(root.clone(), &mut sum);
        root
    }
}
```

## Racket

```racket
#lang racket

; Definition for a binary tree node.
(struct tree-node
  (val left right) #:mutable #:transparent)

(define/contract (bst-to-gst root)
  (-> (or/c tree-node? #f) (or/c tree-node? #f))
  (if (not root)
      #f
      (let ((sum 0))
        (let recur ((node root))
          (when node
            (recur (tree-node-right node))
            (set! sum (+ sum (tree-node-val node)))
            (set-tree-node-val! node sum)
            (recur (tree-node-left node))))
        root)))
```

## Erlang

```erlang
-module(solution).
-export([bst_to_gst/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec bst_to_gst(Root :: #tree_node{} | null) -> #tree_node{} | null.
bst_to_gst(Root) ->
    {NewRoot, _} = helper(Root, 0),
    NewRoot.

helper(null, Acc) ->
    {null, Acc};
helper(Node, Acc) when is_record(Node, tree_node) ->
    % Traverse right subtree first (greater values)
    {RightTransformed, Acc1} = helper(Node#tree_node.right, Acc),

    % Update current node's value with accumulated sum
    NewVal = Node#tree_node.val + Acc1,

    % Traverse left subtree with updated sum
    {LeftTransformed, Acc2} = helper(Node#tree_node.left, NewVal),

    % Reconstruct the node with new values and transformed children
    NewNode = #tree_node{val = NewVal,
                         left = LeftTransformed,
                         right = RightTransformed},
    {NewNode, Acc2}.
```

## Elixir

```elixir
defmodule Solution do
  @spec bst_to_gst(root :: TreeNode.t() | nil) :: TreeNode.t() | nil
  def bst_to_gst(root) do
    {new_root, _} = traverse(root, 0)
    new_root
  end

  defp traverse(nil, acc), do: {nil, acc}

  defp traverse(%TreeNode{val: v, left: l, right: r} = node, acc) do
    # Process right subtree first (greater values)
    {new_right, acc_after_right} = traverse(r, acc)

    # Update current node's value with accumulated sum
    new_val = v + acc_after_right

    # Process left subtree with updated sum
    {new_left, final_acc} = traverse(l, new_val)

    # Return the rebuilt node and the latest accumulator
    {%TreeNode{node | val: new_val, left: new_left, right: new_right}, final_acc}
  end
end
```
