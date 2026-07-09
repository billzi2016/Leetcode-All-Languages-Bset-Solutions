# 1123. Lowest Common Ancestor of Deepest Leaves

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
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        return dfs(root).second;
    }
private:
    // returns {depth of subtree rooted at node, LCA of deepest leaves in this subtree}
    std::pair<int, TreeNode*> dfs(TreeNode* node) {
        if (!node) return {0, nullptr};
        auto left = dfs(node->left);
        auto right = dfs(node->right);
        if (left.first > right.first) {
            return {left.first + 1, left.second};
        } else if (right.first > left.first) {
            return {right.first + 1, right.second};
        } else {
            // depths equal, current node is LCA
            return {left.first + 1, node};
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
    private static class Result {
        int depth;
        TreeNode node;
        Result(int d, TreeNode n) {
            this.depth = d;
            this.node = n;
        }
    }

    public TreeNode lcaDeepestLeaves(TreeNode root) {
        return dfs(root).node;
    }

    private Result dfs(TreeNode root) {
        if (root == null) {
            return new Result(0, null);
        }
        Result left = dfs(root.left);
        Result right = dfs(root.right);
        if (left.depth > right.depth) {
            return new Result(left.depth + 1, left.node);
        } else if (right.depth > left.depth) {
            return new Result(right.depth + 1, right.node);
        } else {
            return new Result(left.depth + 1, root);
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
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node:
                return 0, None
            ld, ln = dfs(node.left)
            rd, rn = dfs(node.right)
            if ld > rd:
                return ld + 1, ln
            elif rd > ld:
                return rd + 1, rn
            else:
                return ld + 1, node
        return dfs(root)[1]
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
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0, None
            ld, ln = dfs(node.left)
            rd, rn = dfs(node.right)
            if ld > rd:
                return ld + 1, ln
            elif rd > ld:
                return rd + 1, rn
            else:
                return ld + 1, node
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

struct TreeNode* lcaDeepestLeaves(struct TreeNode* root) {
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
    public TreeNode LcaDeepestLeaves(TreeNode root)
    {
        return Dfs(root).node;
    }

    private (int depth, TreeNode node) Dfs(TreeNode node)
    {
        if (node == null)
            return (0, null);

        var left = Dfs(node.left);
        var right = Dfs(node.right);

        if (left.depth > right.depth)
            return (left.depth + 1, left.node);
        else if (right.depth > left.depth)
            return (right.depth + 1, right.node);
        else
            return (left.depth + 1, node);
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
var lcaDeepestLeaves = function(root) {
    const dfs = (node) => {
        if (!node) return [0, null];
        const [ld, leftLCA] = dfs(node.left);
        const [rd, rightLCA] = dfs(node.right);
        if (ld > rd) {
            return [ld + 1, leftLCA];
        } else if (rd > ld) {
            return [rd + 1, rightLCA];
        } else {
            return [ld + 1, node];
        }
    };
    return dfs(root)[1];
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

function lcaDeepestLeaves(root: TreeNode | null): TreeNode | null {
    function dfs(node: TreeNode | null): [number, TreeNode | null] {
        if (!node) return [0, null];
        const [ld, leftAns] = dfs(node.left);
        const [rd, rightAns] = dfs(node.right);
        if (ld > rd) {
            return [ld + 1, leftAns];
        } else if (rd > ld) {
            return [rd + 1, rightAns];
        } else {
            return [ld + 1, node];
        }
    }
    return dfs(root)[1];
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
    function lcaDeepestLeaves($root) {
        $res = $this->dfs($root);
        return $res[1];
    }

    private function dfs($node) {
        if ($node === null) {
            return [0, null];
        }
        list($ldepth, $lnode) = $this->dfs($node->left);
        list($rdepth, $rnode) = $this->dfs($node->right);

        if ($ldepth > $rdepth) {
            return [$ldepth + 1, $lnode];
        } elseif ($rdepth > $ldepth) {
            return [$rdepth + 1, $rnode];
        } else {
            return [$ldepth + 1, $node];
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
    func lcaDeepestLeaves(_ root: TreeNode?) -> TreeNode? {
        return dfs(root).node
    }
    
    private func dfs(_ node: TreeNode?) -> (depth: Int, node: TreeNode?) {
        guard let n = node else { return (0, nil) }
        let left = dfs(n.left)
        let right = dfs(n.right)
        
        if left.depth > right.depth {
            return (left.depth + 1, left.node)
        } else if right.depth > left.depth {
            return (right.depth + 1, right.node)
        } else {
            // depths equal
            return (left.depth + 1, n)
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
    fun lcaDeepestLeaves(root: TreeNode?): TreeNode? {
        return dfs(root).second
    }

    private fun dfs(node: TreeNode?): Pair<Int, TreeNode?> {
        if (node == null) return Pair(0, null)
        val left = dfs(node.left)
        val right = dfs(node.right)

        return when {
            left.first > right.first -> Pair(left.first + 1, left.second)
            right.first > left.first -> Pair(right.first + 1, right.second)
            else -> Pair(left.first + 1, node) // depths equal
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
  TreeNode? lcaDeepestLeaves(TreeNode? root) {
    MapEntry<int, TreeNode?> dfs(TreeNode? node) {
      if (node == null) return MapEntry(0, null);
      final left = dfs(node.left);
      final right = dfs(node.right);
      if (left.key > right.key) {
        return MapEntry(left.key + 1, left.value);
      } else if (right.key > left.key) {
        return MapEntry(right.key + 1, right.value);
      } else {
        return MapEntry(left.key + 1, node);
      }
    }

    return dfs(root).value;
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
func lcaDeepestLeaves(root *TreeNode) *TreeNode {
    var dfs func(*TreeNode) (int, *TreeNode)
    dfs = func(node *TreeNode) (int, *TreeNode) {
        if node == nil {
            return 0, nil
        }
        ld, ln := dfs(node.Left)
        rd, rn := dfs(node.Right)
        if ld > rd {
            return ld + 1, ln
        } else if rd > ld {
            return rd + 1, rn
        }
        return ld + 1, node
    }
    _, ans := dfs(root)
    return ans
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

def lca_deepest_leaves(root)
  return nil unless root
  dfs = lambda do |node|
    return [0, nil] if node.nil?
    left_depth, left_node = dfs.call(node.left)
    right_depth, right_node = dfs.call(node.right)

    if left_depth > right_depth
      [left_depth + 1, left_node]
    elsif right_depth > left_depth
      [right_depth + 1, right_node]
    else
      [left_depth + 1, node]
    end
  end

  _, ans = dfs.call(root)
  ans
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
  def lcaDeepestLeaves(root: TreeNode): TreeNode = {
    def dfs(node: TreeNode): (Int, TreeNode) = {
      if (node == null) return (0, null)
      val (ld, ln) = dfs(node.left)
      val (rd, rn) = dfs(node.right)
      if (ld > rd) (ld + 1, ln)
      else if (rd > ld) (rd + 1, rn)
      else (ld + 1, node)
    }
    dfs(root)._2
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
    pub fn lca_deepest_leaves(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>) -> (i32, Option<Rc<RefCell<TreeNode>>>) {
            match node {
                None => (0, None),
                Some(rc) => {
                    let left = rc.borrow().left.clone();
                    let right = rc.borrow().right.clone();
                    let (ldepth, lnode) = dfs(left);
                    let (rdepth, rnode) = dfs(right);
                    if ldepth > rdepth {
                        (ldepth + 1, lnode)
                    } else if rdepth > ldepth {
                        (rdepth + 1, rnode)
                    } else {
                        (ldepth + 1, Some(rc.clone()))
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
(define (lca-deepest-leaves root)
  (define (helper node)
    (if (not node)
        (values 0 #f)
        (let-values ([(ld ln) (helper (tree-node-left node))]
                     [(rd rn) (helper (tree-node-right node))])
          (cond
            [(> ld rd) (values (+ ld 1) ln)]
            [(< ld rd) (values (+ rd 1) rn)]
            [else      (values (+ ld 1) node)]))))
  (let-values ([_ ans] (helper root))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([lca_deepest_leaves/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec lca_deepest_leaves(Root :: #tree_node{} | null) -> #tree_node{} | null.
lca_deepest_leaves(Root) ->
    {_, LCA} = helper(Root),
    LCA.

helper(null) ->
    {0, null};
helper(Node = #tree_node{left = Left, right = Right}) ->
    {LD, LN} = helper(Left),
    {RD, RN} = helper(Right),
    case LD > RD of
        true -> {LD + 1, LN};
        false when LD < RD -> {RD + 1, RN};
        false -> {LD + 1, Node}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec lca_deepest_leaves(root :: TreeNode.t() | nil) :: TreeNode.t() | nil
  def lca_deepest_leaves(root) do
    {_depth, node} = dfs(root)
    node
  end

  defp dfs(nil), do: {0, nil}

  defp dfs(%TreeNode{left: left, right: right} = current) do
    {ld, ln} = dfs(left)
    {rd, rn} = dfs(right)

    cond do
      ld > rd -> {ld + 1, ln}
      rd > ld -> {rd + 1, rn}
      true   -> {ld + 1, current}
    end
  end
end
```
