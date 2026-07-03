# 0145. Binary Tree Postorder Traversal

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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        dfs(root, res);
        return res;
    }
private:
    void dfs(TreeNode* node, vector<int>& res) {
        if (!node) return;
        dfs(node->left, res);
        dfs(node->right, res);
        res.push_back(node->val);
    }
};
```

## Java

```java
import java.util.ArrayList;
import java.util.List;

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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        traverse(root, result);
        return result;
    }

    private void traverse(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }
        traverse(node.left, result);
        traverse(node.right, result);
        result.add(node.val);
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
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res
```

## Python3

```python
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
        dfs(root)
        return result
```

## C

```c
#include <stdlib.h>

/* Definition for a binary tree node. */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static int countNodes(struct TreeNode* root) {
    if (!root) return 0;
    return 1 + countNodes(root->left) + countNodes(root->right);
}

static void fillPostorder(struct TreeNode* root, int *out, int *idx) {
    if (!root) return;
    fillPostorder(root->left, out, idx);
    fillPostorder(root->right, out, idx);
    out[(*idx)++] = root->val;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* postorderTraversal(struct TreeNode* root, int* returnSize) {
    if (!root) {
        *returnSize = 0;
        return NULL;
    }
    int total = countNodes(root);
    int *result = (int*)malloc(sizeof(int) * total);
    *returnSize = 0;
    fillPostorder(root, result, returnSize);
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

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
    public IList<int> PostorderTraversal(TreeNode root) {
        var result = new List<int>();
        Postorder(root, result);
        return result;
    }

    private void Postorder(TreeNode node, List<int> res) {
        if (node == null) return;
        Postorder(node.left, res);
        Postorder(node.right, res);
        res.Add(node.val);
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
 * @return {number[]}
 */
var postorderTraversal = function(root) {
    const result = [];
    const dfs = (node) => {
        if (!node) return;
        dfs(node.left);
        dfs(node.right);
        result.push(node.val);
    };
    dfs(root);
    return result;
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

function postorderTraversal(root: TreeNode | null): number[] {
    const result: number[] = [];
    const dfs = (node: TreeNode | null): void => {
        if (!node) return;
        dfs(node.left);
        dfs(node.right);
        result.push(node.val);
    };
    dfs(root);
    return result;
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
     * @return Integer[]
     */
    function postorderTraversal($root) {
        $result = [];
        $this->dfs($root, $result);
        return $result;
    }

    private function dfs($node, &$res) {
        if ($node === null) {
            return;
        }
        $this->dfs($node->left, $res);
        $this->dfs($node->right, $res);
        $res[] = $node->val;
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
    func postorderTraversal(_ root: TreeNode?) -> [Int] {
        var result = [Int]()
        func dfs(_ node: TreeNode?) {
            guard let n = node else { return }
            dfs(n.left)
            dfs(n.right)
            result.append(n.val)
        }
        dfs(root)
        return result
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
    fun postorderTraversal(root: TreeNode?): List<Int> {
        val result = mutableListOf<Int>()
        dfs(root, result)
        return result
    }

    private fun dfs(node: TreeNode?, res: MutableList<Int>) {
        if (node == null) return
        dfs(node.left, res)
        dfs(node.right, res)
        res.add(node.`val`)
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
  List<int> postorderTraversal(TreeNode? root) {
    final List<int> result = [];
    void dfs(TreeNode? node) {
      if (node == null) return;
      dfs(node.left);
      dfs(node.right);
      result.add(node.val);
    }

    dfs(root);
    return result;
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
func postorderTraversal(root *TreeNode) []int {
	var res []int
	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		dfs(node.Left)
		dfs(node.Right)
		res = append(res, node.Val)
	}
	dfs(root)
	return res
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

def postorder_traversal(root)
  result = []
  dfs = lambda do |node|
    return unless node
    dfs.call(node.left)
    dfs.call(node.right)
    result << node.val
  end
  dfs.call(root)
  result
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
    def postorderTraversal(root: TreeNode): List[Int] = {
        val result = scala.collection.mutable.ListBuffer[Int]()
        def dfs(node: TreeNode): Unit = {
            if (node == null) return
            dfs(node.left)
            dfs(node.right)
            result += node.value
        }
        dfs(root)
        result.toList
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
    pub fn postorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, out: &mut Vec<i32>) {
            if let Some(rc) = node {
                // Clone children before recursive calls to avoid borrowing issues
                let left = rc.borrow().left.clone();
                let right = rc.borrow().right.clone();
                dfs(left, out);
                dfs(right, out);
                out.push(rc.borrow().val);
            }
        }

        let mut result = Vec::new();
        dfs(root, &mut result);
        result
    }
}
```

## Racket

```racket
#|
Definition for a binary tree node.
|#
(struct tree-node
  (val left right) #:mutable #:transparent)

(define (make-tree-node [val 0])
  (tree-node val #f #f))

(define/contract (postorder-traversal root)
  (-> (or/c tree-node? #f) (listof exact-integer?))
  (letrec ((traverse
            (lambda (node acc)
              (if (not node)
                  acc
                  (let* ((acc-left (traverse (tree-node-left node) acc))
                         (acc-right (traverse (tree-node-right node) acc-left)))
                    (cons (tree-node-val node) acc-right))))))
    (reverse (traverse root '()))))
```

## Erlang

```erlang
-module(solution).
-export([postorder_traversal/1]).

%% Definition for a binary tree node.
-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec postorder_traversal(Root :: #tree_node{} | null) -> [integer()].
postorder_traversal(null) ->
    [];
postorder_traversal(Node) when is_record(Node, tree_node) ->
    LeftVals = postorder_traversal(Node#tree_node.left),
    RightVals = postorder_traversal(Node#tree_node.right),
    LeftVals ++ RightVals ++ [Node#tree_node.val].
```

## Elixir

```elixir
defmodule Solution do
  @spec postorder_traversal(root :: TreeNode.t | nil) :: [integer]
  def postorder_traversal(nil), do: []

  def postorder_traversal(root) do
    root
    |> traverse([])
    |> Enum.reverse()
  end

  defp traverse(nil, acc), do: acc

  defp traverse(%TreeNode{val: v, left: l, right: r}, acc) do
    acc = traverse(l, acc)
    acc = traverse(r, acc)
    [v | acc]
  end
end
```
