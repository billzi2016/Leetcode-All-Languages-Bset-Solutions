# 0222. Count Complete Tree Nodes

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
    int getDepth(TreeNode* node) {
        int d = 0;
        while (node) {
            ++d;
            node = node->left;
        }
        return d;
    }
    
    int countNodes(TreeNode* root) {
        if (!root) return 0;
        int leftDepth = getDepth(root->left);
        int rightDepth = getDepth(root->right);
        if (leftDepth == rightDepth) {
            // left subtree is perfect
            return (1 << leftDepth) + countNodes(root->right);
        } else {
            // right subtree is perfect but one level smaller
            return (1 << rightDepth) + countNodes(root->left);
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
    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        int leftDepth = getDepth(root.left);
        int rightDepth = getDepth(root.right);
        if (leftDepth == rightDepth) {
            // Left subtree is perfect
            return (1 << leftDepth) + countNodes(root.right);
        } else {
            // Right subtree is perfect
            return (1 << rightDepth) + countNodes(root.left);
        }
    }

    private int getDepth(TreeNode node) {
        int depth = 0;
        while (node != null) {
            depth++;
            node = node.left;
        }
        return depth;
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
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        def getDepth(node, go_left):
            depth = 0
            while node:
                depth += 1
                node = node.left if go_left else node.right
            return depth

        left_depth = getDepth(root, True)
        right_depth = getDepth(root, False)

        if left_depth == right_depth:
            # perfect binary tree
            return (1 << left_depth) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
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
    def countNodes(self, root: Optional['TreeNode']) -> int:
        def depth(node: Optional['TreeNode']) -> int:
            d = 0
            while node:
                d += 1
                node = node.left
            return d

        if not root:
            return 0

        left_depth = depth(root.left)
        right_depth = depth(root.right)

        if left_depth == right_depth:
            # left subtree is perfect
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # right subtree is perfect
            return (1 << right_depth) + self.countNodes(root.left)
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
static int leftDepth(struct TreeNode* node) {
    int d = 0;
    while (node) {
        ++d;
        node = node->left;
    }
    return d;
}

static int rightDepth(struct TreeNode* node) {
    int d = 0;
    while (node) {
        ++d;
        node = node->right;
    }
    return d;
}

int countNodes(struct TreeNode* root) {
    if (!root) return 0;
    int l = leftDepth(root);
    int r = rightDepth(root);
    if (l == r) {
        // perfect binary tree
        return (1 << l) - 1;
    }
    return 1 + countNodes(root->left) + countNodes(root->right);
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
    private int GetDepth(TreeNode node)
    {
        int depth = 0;
        while (node != null)
        {
            depth++;
            node = node.left;
        }
        return depth;
    }

    public int CountNodes(TreeNode root)
    {
        if (root == null) return 0;

        int leftDepth = GetDepth(root.left);
        int rightDepth = GetDepth(root.right);

        if (leftDepth == rightDepth)
        {
            // Left subtree is perfect
            return (1 << leftDepth) + CountNodes(root.right);
        }
        else
        {
            // Right subtree is perfect but one level smaller
            return (1 << rightDepth) + CountNodes(root.left);
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
 * @return {number}
 */
var countNodes = function(root) {
    if (!root) return 0;
    
    // compute depth of leftmost path
    let leftDepth = 0, node = root;
    while (node) {
        leftDepth++;
        node = node.left;
    }
    
    // compute depth of rightmost path
    let rightDepth = 0;
    node = root;
    while (node) {
        rightDepth++;
        node = node.right;
    }
    
    if (leftDepth === rightDepth) {
        // perfect binary tree
        return Math.pow(2, leftDepth) - 1;
    }
    
    // otherwise recurse on subtrees
    return 1 + countNodes(root.left) + countNodes(root.right);
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

function countNodes(root: TreeNode | null): number {
    if (!root) return 0;

    const getDepth = (node: TreeNode | null): number => {
        let d = 0;
        while (node) {
            d++;
            node = node.left;
        }
        return d;
    };

    const leftDepth = getDepth(root.left);
    const rightDepth = getDepth(root.right);

    if (leftDepth === rightDepth) {
        // Left subtree is perfect
        return (1 << leftDepth) + countNodes(root.right);
    } else {
        // Right subtree is perfect but one level smaller
        return (1 << rightDepth) + countNodes(root.left);
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
     * @return int
     */
    function countNodes($root) {
        if ($root === null) {
            return 0;
        }

        $leftDepth = $this->getDepth($root->left);
        $rightDepth = $this->getDepth($root->right);

        if ($leftDepth == $rightDepth) {
            // left subtree is perfect
            return (1 << $leftDepth) + $this->countNodes($root->right);
        } else {
            // right subtree is perfect
            return (1 << $rightDepth) + $this->countNodes($root->left);
        }
    }

    /**
     * Compute the depth (number of nodes) along the leftmost path.
     *
     * @param TreeNode|null $node
     * @return int
     */
    private function getDepth($node) {
        $depth = 0;
        while ($node !== null) {
            $depth++;
            $node = $node->left;
        }
        return $depth;
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
    func countNodes(_ root: TreeNode?) -> Int {
        guard let node = root else { return 0 }
        let leftDepth = depth(node, true)
        let rightDepth = depth(node, false)
        if leftDepth == rightDepth {
            return (1 << leftDepth) - 1
        } else {
            return 1 + countNodes(node.left) + countNodes(node.right)
        }
    }
    
    private func depth(_ node: TreeNode?, _ goLeft: Bool) -> Int {
        var cur = node
        var d = 0
        while let n = cur {
            d += 1
            cur = goLeft ? n.left : n.right
        }
        return d
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
    fun countNodes(root: TreeNode?): Int {
        if (root == null) return 0
        val leftDepth = getDepth(root, true)
        val rightDepth = getDepth(root, false)
        return if (leftDepth == rightDepth) {
            // perfect binary tree
            (1 shl leftDepth) - 1
        } else {
            1 + countNodes(root.left) + countNodes(root.right)
        }
    }

    private fun getDepth(node: TreeNode?, goLeft: Boolean): Int {
        var depth = 0
        var cur = node
        while (cur != null) {
            depth++
            cur = if (goLeft) cur.left else cur.right
        }
        return depth
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
  int countNodes(TreeNode? root) {
    if (root == null) return 0;
    int depth = _getDepth(root);
    if (depth == 1) return 1;

    int left = 0;
    int right = (1 << (depth - 1)) - 1; // possible nodes at last level

    while (left <= right) {
      int mid = (left + right) >> 1;
      if (_exists(mid, depth, root!)) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    // nodes above last level + nodes found in last level
    return ((1 << (depth - 1)) - 1) + left;
  }

  int _getDepth(TreeNode node) {
    int d = 0;
    while (node != null) {
      d++;
      node = node.left!;
    }
    return d;
  }

  bool _exists(int idx, int depth, TreeNode root) {
    TreeNode? node = root;
    for (int i = depth - 2; i >= 0 && node != null; i--) {
      if (((idx >> i) & 1) == 0) {
        node = node.left;
      } else {
        node = node.right;
      }
    }
    return node != null;
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
func getDepth(node *TreeNode) int {
    depth := 0
    for node != nil {
        depth++
        node = node.Left
    }
    return depth
}

func countNodes(root *TreeNode) int {
    if root == nil {
        return 0
    }
    leftDepth := getDepth(root.Left)
    rightDepth := getDepth(root.Right)

    if leftDepth == rightDepth {
        // Left subtree is perfect.
        return (1 << leftDepth) + countNodes(root.Right)
    } else {
        // Right subtree is perfect.
        return (1 << rightDepth) + countNodes(root.Left)
    }
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

def count_nodes(root)
  return 0 if root.nil?
  left_depth = depth(root.left)
  right_depth = depth(root.right)

  if left_depth == right_depth
    # Left subtree is perfect
    (1 << left_depth) + count_nodes(root.right)
  else
    # Right subtree is perfect but one level shorter
    (1 << right_depth) + count_nodes(root.left)
  end
end

def depth(node)
  d = 0
  while node
    d += 1
    node = node.left
  end
  d
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
    def countNodes(root: TreeNode): Int = {
        if (root == null) return 0

        // compute depth of leftmost path
        var leftDepth = 0
        var node = root
        while (node != null) {
            leftDepth += 1
            node = node.left
        }

        // compute depth of rightmost path
        var rightDepth = 0
        node = root
        while (node != null) {
            rightDepth += 1
            node = node.right
        }

        if (leftDepth == rightDepth) {
            // perfect binary tree
            (1 << leftDepth) - 1
        } else {
            1 + countNodes(root.left) + countNodes(root.right)
        }
    }
}
```

## Rust

```rust
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
use std::rc::Rc;
use std::cell::RefCell;

pub struct Solution;

impl Solution {
    fn depth(node: Option<Rc<RefCell<TreeNode>>>, go_left: bool) -> i32 {
        let mut cur = node;
        let mut d = 0;
        while let Some(rc) = cur {
            d += 1;
            let borrow = rc.borrow();
            cur = if go_left { borrow.left.clone() } else { borrow.right.clone() };
        }
        d
    }

    pub fn count_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match root {
            None => 0,
            Some(rc) => {
                let left_depth = Self::depth(Some(rc.clone()), true);
                let right_depth = Self::depth(Some(rc.clone()), false);
                if left_depth == right_depth {
                    // perfect binary tree
                    (2_i32.pow(left_depth as u32)) - 1
                } else {
                    1 + Self::count_nodes(rc.borrow().left.clone())
                      + Self::count_nodes(rc.borrow().right.clone())
                }
            }
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

;; helper: depth following left children
(define (depth-left node)
  (let loop ((n node) (d 0))
    (if n
        (loop (tree-node-left n) (+ d 1))
        d)))

;; helper: depth following right children
(define (depth-right node)
  (let loop ((n node) (d 0))
    (if n
        (loop (tree-node-right n) (+ d 1))
        d)))

(define/contract (count-nodes root)
  (-> (or/c tree-node? #f) exact-integer?)
  (cond [(not root) 0]
        [else
         (let ([lh (depth-left root)]
               [rh (depth-right root)])
           (if (= lh rh)
               (- (arithmetic-shift 1 lh) 1) ; full tree: 2^h - 1
               (+ 1
                  (count-nodes (tree-node-left root))
                  (count-nodes (tree-node-right root)))))]))
```

## Erlang

```erlang
-module(solution).
-export([count_nodes/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec count_nodes(Root :: #tree_node{} | null) -> integer().
count_nodes(null) ->
    0;
count_nodes(Root) ->
    L = depth_left(Root),
    R = depth_right(Root),
    if
        L == R ->
            (1 bsl L) - 1;
        true ->
            1 + count_nodes(Root#tree_node.left) + count_nodes(Root#tree_node.right)
    end.

depth_left(null) -> 0;
depth_left(Node) ->
    depth_left(Node#tree_node.left) + 1.

depth_right(null) -> 0;
depth_right(Node) ->
    depth_right(Node#tree_node.right) + 1.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_nodes(root :: TreeNode.t | nil) :: integer
  def count_nodes(nil), do: 0

  def count_nodes(root) do
    left_h = height(root.left)
    right_h = height(root.right)

    if left_h == right_h do
      :erlang.bsl(1, left_h + 1) - 1
    else
      1 + count_nodes(root.left) + count_nodes(root.right)
    end
  end

  defp height(nil), do: 0
  defp height(%TreeNode{left: l}) do
    1 + height(l)
  end
end
```
