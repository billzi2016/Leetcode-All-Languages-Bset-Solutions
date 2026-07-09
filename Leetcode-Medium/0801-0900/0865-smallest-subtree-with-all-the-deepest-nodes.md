# 0865. Smallest Subtree with all the Deepest Nodes

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
    // Returns {answer node for subtree, depth of deepest leaf in this subtree}
    pair<TreeNode*, int> dfs(TreeNode* node) {
        if (!node) return {nullptr, 0};
        auto left = dfs(node->left);
        auto right = dfs(node->right);
        if (left.second == right.second) {
            // both sides have deepest nodes at same depth
            return {node, left.second + 1};
        } else if (left.second > right.second) {
            return {left.first, left.second + 1};
        } else {
            return {right.first, right.second + 1};
        }
    }

    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        return dfs(root).first;
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
    private static class Result {
        TreeNode node;
        int depth;
        Result(TreeNode n, int d) { node = n; depth = d; }
    }

    public TreeNode subtreeWithAllDeepest(TreeNode root) {
        return dfs(root).node;
    }

    private Result dfs(TreeNode root) {
        if (root == null) {
            return new Result(null, 0);
        }
        Result left = dfs(root.left);
        Result right = dfs(root.right);
        if (left.depth == right.depth) {
            return new Result(root, left.depth + 1);
        } else if (left.depth > right.depth) {
            return new Result(left.node, left.depth + 1);
        } else {
            return new Result(right.node, right.depth + 1);
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
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node:
                return (None, 0)
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)
            if left_depth > right_depth:
                return (left_node, left_depth + 1)
            elif right_depth > left_depth:
                return (right_node, right_depth + 1)
            else:
                return (node, left_depth + 1)
        return dfs(root)[0]
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, Tuple

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, Optional[TreeNode]]:
            if not node:
                return 0, None
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)
            if left_depth == right_depth:
                return left_depth + 1, node
            elif left_depth > right_depth:
                return left_depth + 1, left_node
            else:
                return right_depth + 1, right_node

        return dfs(root)[1]
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
struct Result {
    int depth;
    struct TreeNode* node;
};

static struct Result dfs(struct TreeNode* root) {
    if (root == NULL) {
        return (struct Result){0, NULL};
    }
    struct Result left = dfs(root->left);
    struct Result right = dfs(root->right);
    
    if (left.depth > right.depth) {
        return (struct Result){left.depth + 1, left.node};
    } else if (right.depth > left.depth) {
        return (struct Result){right.depth + 1, right.node};
    } else {
        return (struct Result){left.depth + 1, root};
    }
}

struct TreeNode* subtreeWithAllDeepest(struct TreeNode* root) {
    return dfs(root).node;
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
    public TreeNode SubtreeWithAllDeepest(TreeNode root)
    {
        return Dfs(root).node;
    }

    private (TreeNode node, int depth) Dfs(TreeNode root)
    {
        if (root == null)
            return (null, 0);

        var left = Dfs(root.left);
        var right = Dfs(root.right);

        if (left.depth == right.depth)
            return (root, left.depth + 1);
        else if (left.depth > right.depth)
            return (left.node, left.depth + 1);
        else
            return (right.node, right.depth + 1);
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
var subtreeWithAllDeepest = function(root) {
    const dfs = (node) => {
        if (!node) return { depth: -1, node: null };
        const left = dfs(node.left);
        const right = dfs(node.right);
        if (left.depth === right.depth) {
            return { depth: left.depth + 1, node: node };
        } else if (left.depth > right.depth) {
            return { depth: left.depth + 1, node: left.node };
        } else {
            return { depth: right.depth + 1, node: right.node };
        }
    };
    return dfs(root).node;
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

function subtreeWithAllDeepest(root: TreeNode | null): TreeNode | null {
    function dfs(node: TreeNode | null): { node: TreeNode | null; depth: number } {
        if (!node) return { node: null, depth: 0 };
        const left = dfs(node.left);
        const right = dfs(node.right);
        if (left.depth > right.depth) {
            return { node: left.node, depth: left.depth + 1 };
        }
        if (right.depth > left.depth) {
            return { node: right.node, depth: right.depth + 1 };
        }
        // depths equal
        return { node: node, depth: left.depth + 1 };
    }

    return dfs(root).node;
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
     * @return TreeNode
     */
    function subtreeWithAllDeepest($root) {
        return $this->dfs($root)[0];
    }

    /**
     * Returns an array where:
     * [0] => TreeNode that is the smallest subtree containing all deepest nodes in this subtree
     * [1] => depth of the deepest node from current node (including current node as depth 1)
     *
     * @param TreeNode|null $node
     * @return array
     */
    private function dfs($node) {
        if ($node === null) {
            return [null, 0];
        }

        $left = $this->dfs($node->left);
        $right = $this->dfs($node->right);

        if ($left[1] == $right[1]) {
            // deepest nodes are equally deep in both subtrees
            return [$node, $left[1] + 1];
        } elseif ($left[1] > $right[1]) {
            // left side deeper
            return [$left[0], $left[1] + 1];
        } else {
            // right side deeper
            return [$right[0], $right[1] + 1];
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
    func subtreeWithAllDeepest(_ root: TreeNode?) -> TreeNode? {
        return dfs(root).0
    }

    private func dfs(_ node: TreeNode?) -> (TreeNode?, Int) {
        guard let n = node else { return (nil, 0) }
        let left = dfs(n.left)
        let right = dfs(n.right)

        if left.1 > right.1 {
            return (left.0, left.1 + 1)
        } else if right.1 > left.1 {
            return (right.0, right.1 + 1)
        } else {
            return (n, left.1 + 1)
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
    fun subtreeWithAllDeepest(root: TreeNode?): TreeNode? {
        return dfs(root).second
    }

    private fun dfs(node: TreeNode?): Pair<Int, TreeNode?> {
        if (node == null) return Pair(0, null)
        val left = dfs(node.left)
        val right = dfs(node.right)
        return when {
            left.first > right.first -> Pair(left.first + 1, left.second)
            right.first > left.first -> Pair(right.first + 1, right.second)
            else -> Pair(left.first + 1, node)
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
class Result {
  final TreeNode? node;
  final int depth;
  Result(this.node, this.depth);
}

class Solution {
  TreeNode? subtreeWithAllDeepest(TreeNode? root) {
    return _dfs(root).node;
  }

  Result _dfs(TreeNode? node) {
    if (node == null) {
      return Result(null, 0);
    }
    final left = _dfs(node.left);
    final right = _dfs(node.right);

    if (left.depth == right.depth) {
      return Result(node, left.depth + 1);
    } else if (left.depth > right.depth) {
      return Result(left.node, left.depth + 1);
    } else {
      return Result(right.node, right.depth + 1);
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
func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
    _, ans := dfs(root)
    return ans
}

func dfs(node *TreeNode) (int, *TreeNode) {
    if node == nil {
        return 0, nil
    }
    leftDepth, leftNode := dfs(node.Left)
    rightDepth, rightNode := dfs(node.Right)

    if leftDepth > rightDepth {
        return leftDepth + 1, leftNode
    } else if rightDepth > leftDepth {
        return rightDepth + 1, rightNode
    }
    // depths are equal, current node is the common ancestor
    return leftDepth + 1, node
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

def subtree_with_all_deepest(root)
  node, _ = dfs(root)
  node
end

def dfs(node)
  return [nil, 0] if node.nil?
  left_node, left_depth = dfs(node.left)
  right_node, right_depth = dfs(node.right)

  if left_depth == right_depth
    [node, left_depth + 1]
  elsif left_depth > right_depth
    [left_node, left_depth + 1]
  else
    [right_node, right_depth + 1]
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
  private case class Res(node: TreeNode, depth: Int)

  def subtreeWithAllDeepest(root: TreeNode): TreeNode = {
    dfs(root).node
  }

  private def dfs(node: TreeNode): Res = {
    if (node == null) return Res(null, 0)
    val left = dfs(node.left)
    val right = dfs(node.right)

    if (left.depth > right.depth) {
      Res(left.node, left.depth + 1)
    } else if (right.depth > left.depth) {
      Res(right.node, right.depth + 1)
    } else {
      Res(node, left.depth + 1)
    }
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn subtree_with_all_deepest(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>) -> (i32, Option<Rc<RefCell<TreeNode>>>) {
            match node {
                None => (-1, None),
                Some(rc_node) => {
                    let left = rc_node.borrow().left.clone();
                    let right = rc_node.borrow().right.clone();

                    let (ldepth, lnode) = dfs(left);
                    let (rdepth, rnode) = dfs(right);

                    if ldepth == rdepth {
                        (ldepth + 1, Some(rc_node))
                    } else if ldepth > rdepth {
                        (ldepth + 1, lnode)
                    } else {
                        (rdepth + 1, rnode)
                    }
                }
            }
        }

        let (_, ans) = dfs(root);
        ans
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

(define/contract (subtree-with-all-deepest root)
  (-> (or/c tree-node? #f) (or/c tree-node? #f))
  (define (dfs node)
    (if (not node)
        (cons #f -1)
        (let* ((left-res (dfs (tree-node-left node)))
               (right-res (dfs (tree-node-right node)))
               (l-depth (cdr left-res))
               (r-depth (cdr right-res)))
          (cond [(> l-depth r-depth) (cons (car left-res) (+ l-depth 1))]
                [(< l-depth r-depth) (cons (car right-res) (+ r-depth 1))]
                [else (cons node (+ l-depth 1))]))))
  (car (dfs root)))
```

## Erlang

```erlang
-module(solution).
-compile(export_all).

-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-export([subtree_with_all_deepest/1]).

-spec subtree_with_all_deepest(Root :: #tree_node{} | null) -> #tree_node{} | null.
subtree_with_all_deepest(Root) ->
    {Node, _Depth} = dfs(Root),
    Node.

dfs(null) ->
    {null, 0};
dfs(#tree_node{left=Left,right=Right}=Node) ->
    {LNode, LDepth} = dfs(Left),
    {RNode, RDepth} = dfs(Right),
    case compare(LDepth, RDepth) of
        left -> {LNode, LDepth + 1};
        right -> {RNode, RDepth + 1};
        equal -> {Node, LDepth + 1}
    end.

compare(A,B) when A > B -> left;
compare(A,B) when A < B -> right;
compare(_,_) -> equal.
```

## Elixir

```elixir
defmodule Solution do
  @spec subtree_with_all_deepest(root :: TreeNode.t | nil) :: TreeNode.t | nil
  def subtree_with_all_deepest(root) do
    {_depth, node} = dfs(root)
    node
  end

  defp dfs(nil), do: {0, nil}

  defp dfs(%TreeNode{left: left, right: right} = node) do
    {dl, nl} = dfs(left)
    {dr, nr} = dfs(right)

    cond do
      dl == dr -> {dl + 1, node}
      dl > dr -> {dl + 1, nl}
      true -> {dr + 1, nr}
    end
  end
end
```
