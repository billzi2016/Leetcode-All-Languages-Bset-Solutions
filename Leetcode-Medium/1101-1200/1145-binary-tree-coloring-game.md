# 1145. Binary Tree Coloring Game

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
    bool btreeGameWinningMove(TreeNode* root, int n, int x) {
        target = x;
        dfs(root);
        int parentSide = n - (leftCount + rightCount + 1);
        int maxRegion = std::max({leftCount, rightCount, parentSide});
        return maxRegion > n / 2;
    }
private:
    int target;
    int leftCount = 0;
    int rightCount = 0;
    
    int dfs(TreeNode* node) {
        if (!node) return 0;
        int l = dfs(node->left);
        int r = dfs(node->right);
        if (node->val == target) {
            leftCount = l;
            rightCount = r;
        }
        return l + r + 1;
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
    private int x;
    private int leftSubSize;
    private int rightSubSize;

    public boolean btreeGameWinningMove(TreeNode root, int n, int x) {
        this.x = x;
        dfs(root);
        int parentSide = n - (leftSubSize + rightSubSize + 1);
        int half = n / 2; // n is odd, so > half means winning
        return leftSubSize > half || rightSubSize > half || parentSide > half;
    }

    private int dfs(TreeNode node) {
        if (node == null) return 0;
        int left = dfs(node.left);
        int right = dfs(node.right);
        if (node.val == x) {
            leftSubSize = left;
            rightSubSize = right;
        }
        return left + right + 1;
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
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: Optional[TreeNode]
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.left_sub = 0
        self.right_sub = 0

        def dfs(node):
            if not node:
                return 0
            left_sz = dfs(node.left)
            right_sz = dfs(node.right)
            if node.val == x:
                self.left_sub = left_sz
                self.right_sub = right_sz
            return left_sz + right_sz + 1

        dfs(root)

        parent_side = n - (self.left_sub + self.right_sub + 1)
        max_region = max(self.left_sub, self.right_sub, parent_side)
        return max_region > n // 2
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
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        self.left_sub = 0
        self.right_sub = 0

        def dfs(node):
            if not node:
                return 0
            left_sz = dfs(node.left)
            right_sz = dfs(node.right)
            if node.val == x:
                self.left_sub = left_sz
                self.right_sub = right_sz
            return left_sz + right_sz + 1

        dfs(root)

        parent_region = n - (self.left_sub + self.right_sub + 1)
        max_region = max(self.left_sub, self.right_sub, parent_region)
        return max_region > n // 2
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
#include <stdbool.h>

static int leftCount = 0;
static int rightCount = 0;

static int dfs(struct TreeNode* node, int x) {
    if (!node) return 0;
    int l = dfs(node->left, x);
    int r = dfs(node->right, x);
    if (node->val == x) {
        leftCount = l;
        rightCount = r;
    }
    return l + r + 1;
}

bool btreeGameWinningMove(struct TreeNode* root, int n, int x) {
    leftCount = rightCount = 0;
    dfs(root, x);
    int parentRegion = n - (leftCount + rightCount + 1);
    int half = n / 2;
    return (leftCount > half) || (rightCount > half) || (parentRegion > half);
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
    private int leftCount;
    private int rightCount;

    public bool BtreeGameWinningMove(TreeNode root, int n, int x) {
        leftCount = 0;
        rightCount = 0;
        CountSubtrees(root, x);
        int parentCount = n - (leftCount + rightCount + 1);
        int half = n / 2;
        return Math.Max(Math.Max(leftCount, rightCount), parentCount) > half;
    }

    private int CountSubtrees(TreeNode node, int x) {
        if (node == null) return 0;
        int left = CountSubtrees(node.left, x);
        int right = CountSubtrees(node.right, x);
        if (node.val == x) {
            leftCount = left;
            rightCount = right;
        }
        return left + right + 1;
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
 * @param {number} n
 * @param {number} x
 * @return {boolean}
 */
var btreeGameWinningMove = function(root, n, x) {
    let leftCount = 0;
    let rightCount = 0;

    const dfs = (node) => {
        if (!node) return 0;
        const l = dfs(node.left);
        const r = dfs(node.right);
        if (node.val === x) {
            leftCount = l;
            rightCount = r;
        }
        return l + r + 1;
    };

    dfs(root);

    const parentSide = n - (leftCount + rightCount + 1);
    const maxRegion = Math.max(leftCount, rightCount, parentSide);
    return maxRegion > Math.floor(n / 2);
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

function btreeGameWinningMove(root: TreeNode | null, n: number, x: number): boolean {
    let leftSub = 0;
    let rightSub = 0;

    const dfs = (node: TreeNode | null): number => {
        if (!node) return 0;
        const leftSize = dfs(node.left);
        const rightSize = dfs(node.right);
        if (node.val === x) {
            leftSub = leftSize;
            rightSub = rightSize;
        }
        return leftSize + rightSize + 1;
    };

    dfs(root);

    const parentSide = n - (leftSub + rightSub + 1);
    const maxRegion = Math.max(leftSub, rightSub, parentSide);
    return maxRegion > Math.floor(n / 2);
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
    private $targetX = 0;
    private $leftCount = 0;
    private $rightCount = 0;

    /**
     * @param TreeNode $root
     * @param Integer $n
     * @param Integer $x
     * @return Boolean
     */
    function btreeGameWinningMove($root, $n, $x) {
        $this->targetX = $x;
        $this->leftCount = 0;
        $this->rightCount = 0;
        $this->dfs($root);
        $rest = $n - ($this->leftCount + $this->rightCount + 1);
        $maxRegion = max($this->leftCount, $this->rightCount, $rest);
        return $maxRegion > intdiv($n, 2);
    }

    private function dfs($node) {
        if ($node === null) {
            return 0;
        }
        $leftSize = $this->dfs($node->left);
        $rightSize = $this->dfs($node->right);
        if ($node->val == $this->targetX) {
            $this->leftCount = $leftSize;
            $this->rightCount = $rightSize;
        }
        return $leftSize + $rightSize + 1;
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
    private var target = 0
    private var leftCount = 0
    private var rightCount = 0

    private func dfs(_ node: TreeNode?) -> Int {
        guard let node = node else { return 0 }
        let l = dfs(node.left)
        let r = dfs(node.right)
        if node.val == target {
            leftCount = l
            rightCount = r
        }
        return l + r + 1
    }

    func btreeGameWinningMove(_ root: TreeNode?, _ n: Int, _ x: Int) -> Bool {
        target = x
        _ = dfs(root)
        let parentSide = n - (leftCount + rightCount + 1)
        let maxRegion = max(max(leftCount, rightCount), parentSide)
        return maxRegion > n / 2
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
    private var leftSize = 0
    private var rightSize = 0
    private var target = 0

    fun btreeGameWinningMove(root: TreeNode?, n: Int, x: Int): Boolean {
        target = x
        dfs(root)
        val parentSize = n - (leftSize + rightSize + 1)
        val maxRegion = maxOf(leftSize, rightSize, parentSize)
        return maxRegion > n / 2
    }

    private fun dfs(node: TreeNode?): Int {
        if (node == null) return 0
        val left = dfs(node.left)
        val right = dfs(node.right)
        if (node.`val` == target) {
            leftSize = left
            rightSize = right
        }
        return left + right + 1
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
  bool btreeGameWinningMove(TreeNode? root, int n, int x) {
    int leftSize = 0;
    int rightSize = 0;

    int dfs(TreeNode? node) {
      if (node == null) return 0;
      int l = dfs(node.left);
      int r = dfs(node.right);
      if (node.val == x) {
        leftSize = l;
        rightSize = r;
      }
      return l + r + 1;
    }

    dfs(root);
    int parentSize = n - (leftSize + rightSize + 1);
    int maxRegion = leftSize;
    if (rightSize > maxRegion) maxRegion = rightSize;
    if (parentSize > maxRegion) maxRegion = parentSize;

    return maxRegion > n ~/ 2;
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
func btreeGameWinningMove(root *TreeNode, n int, x int) bool {
    var leftSize, rightSize int

    var dfs func(*TreeNode) int
    dfs = func(node *TreeNode) int {
        if node == nil {
            return 0
        }
        l := dfs(node.Left)
        r := dfs(node.Right)
        if node.Val == x {
            leftSize = l
            rightSize = r
        }
        return l + r + 1
    }

    dfs(root)

    parentSize := n - (leftSize + rightSize + 1)
    maxRegion := leftSize
    if rightSize > maxRegion {
        maxRegion = rightSize
    }
    if parentSize > maxRegion {
        maxRegion = parentSize
    }

    return maxRegion > n/2
}
```

## Ruby

```ruby
def subtree_size(node)
  return 0 unless node
  1 + subtree_size(node.left) + subtree_size(node.right)
end

def find_node(node, x)
  return nil unless node
  return node if node.val == x
  left = find_node(node.left, x)
  return left if left
  find_node(node.right, x)
end

def btree_game_winning_move(root, n, x)
  target = find_node(root, x)
  left_cnt = subtree_size(target.left)
  right_cnt = subtree_size(target.right)
  parent_cnt = n - (left_cnt + right_cnt + 1)

  [left_cnt, right_cnt, parent_cnt].max > n / 2
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
    def btreeGameWinningMove(root: TreeNode, n: Int, x: Int): Boolean = {
        var leftSize = 0
        var rightSize = 0

        def dfs(node: TreeNode): Int = {
            if (node == null) return 0
            val l = dfs(node.left)
            val r = dfs(node.right)
            if (node.value == x) {
                leftSize = l
                rightSize = r
            }
            l + r + 1
        }

        dfs(root)

        val parentSize = n - (leftSize + rightSize + 1)
        val maxRegion = Math.max(parentSize, Math.max(leftSize, rightSize))
        maxRegion > n / 2
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn btree_game_winning_move(root: Option<Rc<RefCell<TreeNode>>>, n: i32, x: i32) -> bool {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, x: i32, left_sz: &mut i32, right_sz: &mut i32) -> i32 {
            if let Some(rc_node) = node {
                let node_ref = rc_node.borrow();
                let lsize = dfs(node_ref.left.clone(), x, left_sz, right_sz);
                let rsize = dfs(node_ref.right.clone(), x, left_sz, right_sz);
                let total = lsize + rsize + 1;
                if node_ref.val == x {
                    *left_sz = lsize;
                    *right_sz = rsize;
                }
                total
            } else {
                0
            }
        }

        let mut left = 0;
        let mut right = 0;
        let subtree_size = dfs(root, x, &mut left, &mut right);
        let parent = n - subtree_size;
        let max_region = *[left, right, parent].iter().max().unwrap();
        max_region > n / 2
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

(define/contract (btree-game-winning-move root n x)
  (-> (or/c tree-node? #f) exact-integer? exact-integer? boolean?)
  (let ((left-size (box 0))
        (right-size (box 0)))
    (define (dfs node)
      (if (not node)
          0
          (let* ((l (dfs (tree-node-left node)))
                 (r (dfs (tree-node-right node))))
            (when (= (tree-node-val node) x)
              (set-box! left-size l)
              (set-box! right-size r))
            (+ 1 l r))))
    (void (dfs root))
    (define rest (- n (unbox left-size) (unbox right-size) 1))
    (> (max (unbox left-size) (unbox right-size) rest) (quotient n 2))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec btree_game_winning_move(Root :: #tree_node{} | null, N :: integer(), X :: integer()) -> boolean().
btree_game_winning_move(Root, N, X) ->
    {_, Info} = size_and_find(Root, X),
    case Info of
        none -> false;
        {LeftSize, RightSize} ->
            ParentSize = N - (1 + LeftSize + RightSize),
            MaxRegion = erlang:max(LeftSize, erlang:max(RightSize, ParentSize)),
            MaxRegion > N div 2
    end.

size_and_find(null, _X) ->
    {0, none};
size_and_find(Node, X) ->
    {Lsize, Linfo} = size_and_find(Node#tree_node.left, X),
    {Rsize, Rinfo} = size_and_find(Node#tree_node.right, X),
    Size = 1 + Lsize + Rsize,
    Info =
        if Node#tree_node.val == X ->
                {Lsize, Rsize};
           true ->
                case Linfo of
                    none -> Rinfo;
                    _ -> Linfo
                end
        end,
    {Size, Info}.
```

## Elixir

```elixir
defmodule Solution do
  @spec btree_game_winning_move(root :: TreeNode.t() | nil, n :: integer, x :: integer) :: boolean
  def btree_game_winning_move(root, n, x) do
    case find_sizes(root, x) do
      {left_sz, right_sz} ->
        parent_sz = n - (left_sz + right_sz + 1)
        max_region = Enum.max([left_sz, right_sz, parent_sz])
        max_region > div(n, 2)

      nil -> false
    end
  end

  defp find_sizes(nil, _x), do: nil

  defp find_sizes(%TreeNode{val: val, left: l, right: r} = node, x) do
    if val == x do
      {subtree_size(l), subtree_size(r)}
    else
      case find_sizes(l, x) do
        nil ->
          case find_sizes(r, x) do
            nil -> nil
            res -> res
          end

        res -> res
      end
    end
  end

  defp subtree_size(nil), do: 0
  defp subtree_size(%TreeNode{left: l, right: r}), do: 1 + subtree_size(l) + subtree_size(r)
end
```
