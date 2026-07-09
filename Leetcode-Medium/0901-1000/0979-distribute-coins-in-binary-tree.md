# 0979. Distribute Coins in Binary Tree

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
    int moves = 0;
    
    int dfs(TreeNode* node) {
        if (!node) return 0;
        int left = dfs(node->left);
        int right = dfs(node->right);
        moves += std::abs(left) + std::abs(right);
        // net coins to pass to parent
        return node->val - 1 + left + right;
    }
    
    int distributeCoins(TreeNode* root) {
        moves = 0;
        dfs(root);
        return moves;
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
    private int moves = 0;

    public int distributeCoins(TreeNode root) {
        dfs(root);
        return moves;
    }

    // Returns net excess coins of the subtree rooted at node
    private int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int leftExcess = dfs(node.left);
        int rightExcess = dfs(node.right);
        moves += Math.abs(leftExcess) + Math.abs(rightExcess);
        // Node keeps one coin, so net excess is its value minus 1 plus children's excess
        return node.val - 1 + leftExcess + rightExcess;
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
    def distributeCoins(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.moves = 0

        def dfs(node):
            if not node:
                return 0
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            self.moves += abs(left_excess) + abs(right_excess)
            # net excess coins to pass to parent
            return node.val - 1 + left_excess + right_excess

        dfs(root)
        return self.moves
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
    def distributeCoins(self, root: Optional['TreeNode']) -> int:
        moves = 0

        def dfs(node: Optional['TreeNode']) -> int:
            nonlocal moves
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            moves += abs(left) + abs(right)
            # net excess coins to pass to parent
            return node.val - 1 + left + right

        dfs(root)
        return moves
```

## C

```c
#include <stdlib.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

static int totalMoves;

static int dfs(struct TreeNode* node) {
    if (!node) return 0;
    int left = dfs(node->left);
    int right = dfs(node->right);
    totalMoves += abs(left) + abs(right);
    return node->val - 1 + left + right;
}

int distributeCoins(struct TreeNode* root) {
    totalMoves = 0;
    dfs(root);
    return totalMoves;
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
    private int moves = 0;

    public int DistributeCoins(TreeNode root)
    {
        dfs(root);
        return moves;
    }

    private int dfs(TreeNode node)
    {
        if (node == null) return 0;

        int left = dfs(node.left);
        int right = dfs(node.right);

        moves += System.Math.Abs(left) + System.Math.Abs(right);

        // Net excess coins to pass to parent
        return node.val - 1 + left + right;
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
var distributeCoins = function(root) {
    let moves = 0;
    const dfs = (node) => {
        if (!node) return 0;
        const left = dfs(node.left);
        const right = dfs(node.right);
        moves += Math.abs(left) + Math.abs(right);
        // surplus coins to pass to parent
        return node.val - 1 + left + right;
    };
    dfs(root);
    return moves;
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

function distributeCoins(root: TreeNode | null): number {
    let moves = 0;
    const dfs = (node: TreeNode | null): number => {
        if (!node) return 0;
        const left = dfs(node.left);
        const right = dfs(node.right);
        moves += Math.abs(left) + Math.abs(right);
        // surplus coins to pass to parent
        return node.val - 1 + left + right;
    };
    dfs(root);
    return moves;
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
     * @return int
     */
    function distributeCoins($root) {
        $moves = 0;
        $this->dfs($root, $moves);
        return $moves;
    }

    private function dfs($node, &$moves) {
        if ($node === null) {
            return 0;
        }
        $left = $this->dfs($node->left, $moves);
        $right = $this->dfs($node->right, $moves);
        $moves += abs($left) + abs($right);
        // Net excess coins to pass to parent
        return $node->val - 1 + $left + $right;
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
    func distributeCoins(_ root: TreeNode?) -> Int {
        var moves = 0
        
        func dfs(_ node: TreeNode?) -> Int {
            guard let n = node else { return 0 }
            let left = dfs(n.left)
            let right = dfs(n.right)
            moves += abs(left) + abs(right)
            // net coins to pass to parent
            return n.val - 1 + left + right
        }
        
        _ = dfs(root)
        return moves
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
    private var moves = 0

    fun distributeCoins(root: TreeNode?): Int {
        dfs(root)
        return moves
    }

    private fun dfs(node: TreeNode?): Int {
        if (node == null) return 0
        val left = dfs(node.left)
        val right = dfs(node.right)
        moves += kotlin.math.abs(left) + kotlin.math.abs(right)
        return node.`val` - 1 + left + right
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
  int distributeCoins(TreeNode? root) {
    int moves = 0;

    int dfs(TreeNode? node) {
      if (node == null) return 0;
      int left = dfs(node.left);
      int right = dfs(node.right);
      moves += left.abs() + right.abs();
      return node.val - 1 + left + right;
    }

    dfs(root);
    return moves;
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
func distributeCoins(root *TreeNode) int {
	var moves int
	var dfs func(*TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		left := dfs(node.Left)
		right := dfs(node.Right)
		moves += abs(left) + abs(right)
		return node.Val - 1 + left + right
	}
	dfs(root)
	return moves
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

def distribute_coins(root)
  moves = 0
  dfs = ->(node) {
    return 0 unless node
    left_excess = dfs.call(node.left)
    right_excess = dfs.call(node.right)
    moves += left_excess.abs + right_excess.abs
    node.val - 1 + left_excess + right_excess
  }
  dfs.call(root)
  moves
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
  def distributeCoins(root: TreeNode): Int = {
    var moves = 0

    def dfs(node: TreeNode): Int = {
      if (node == null) return 0
      val left = dfs(node.left)
      val right = dfs(node.right)
      moves += math.abs(left) + math.abs(right)
      node.value - 1 + left + right
    }

    dfs(root)
    moves
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

pub struct Solution;

impl Solution {
    pub fn distribute_coins(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, moves: &mut i32) -> i32 {
            if let Some(rc_node) = node {
                let left = dfs(rc_node.borrow().left.clone(), moves);
                let right = dfs(rc_node.borrow().right.clone(), moves);
                *moves += left.abs() + right.abs();
                rc_node.borrow().val + left + right - 1
            } else {
                0
            }
        }

        let mut moves = 0;
        dfs(root, &mut moves);
        moves
    }
}
```

## Racket

```racket
(define/contract (distribute-coins root)
  (-> (or/c tree-node? #f) exact-integer?)
  (let ([moves (box 0)])
    (define (dfs node)
      (if (not node)
          0
          (let* ((left  (dfs (tree-node-left node)))
                 (right (dfs (tree-node-right node)))
                 (total (+ (- (tree-node-val node) 1) left right)))
            (set-box! moves (+ (unbox moves) (abs left) (abs right)))
            total)))
    (dfs root)
    (unbox moves)))
```

## Erlang

```erlang
-module(solution).
-export([distribute_coins/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec distribute_coins(Root :: #tree_node{} | null) -> integer().
distribute_coins(Root) ->
    {_Bal, Moves} = dfs(Root),
    Moves.

-spec dfs(Node :: #tree_node{} | null) -> {integer(), integer()}.
dfs(null) ->
    {0, 0};
dfs(Node) ->
    {LBal, LMoves} = dfs(Node#tree_node.left),
    {RBal, RMoves} = dfs(Node#tree_node.right),
    Moves = LMoves + RMoves + abs(LBal) + abs(RBal),
    Balance = Node#tree_node.val - 1 + LBal + RBal,
    {Balance, Moves}.
```

## Elixir

```elixir
defmodule Solution do
  @spec distribute_coins(root :: TreeNode.t() | nil) :: integer
  def distribute_coins(root) do
    {_excess, moves} = dfs(root)
    moves
  end

  defp dfs(nil), do: {0, 0}

  defp dfs(%TreeNode{val: val, left: left, right: right}) do
    {left_excess, left_moves} = dfs(left)
    {right_excess, right_moves} = dfs(right)

    moves = left_moves + right_moves + abs(left_excess) + abs(right_excess)
    excess = val - 1 + left_excess + right_excess

    {excess, moves}
  end
end
```
