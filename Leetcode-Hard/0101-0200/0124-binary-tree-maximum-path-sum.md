# 0124. Binary Tree Maximum Path Sum

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
    int maxPathSum(TreeNode* root) {
        ans = INT_MIN;
        dfs(root);
        return ans;
    }
private:
    int ans;
    int dfs(TreeNode* node) {
        if (!node) return 0;
        int left = std::max(0, dfs(node->left));
        int right = std::max(0, dfs(node->right));
        ans = std::max(ans, node->val + left + right);
        return node->val + std::max(left, right);
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
    private int maxSum;

    public int maxPathSum(TreeNode root) {
        maxSum = Integer.MIN_VALUE;
        dfs(root);
        return maxSum;
    }

    private int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }
        // Compute maximum gain from left and right subtrees; ignore negatives
        int leftGain = Math.max(dfs(node.left), 0);
        int rightGain = Math.max(dfs(node.right), 0);

        // Path sum that passes through the current node (could be a candidate for global max)
        int priceNewPath = node.val + leftGain + rightGain;

        // Update global maximum if needed
        maxSum = Math.max(maxSum, priceNewPath);

        // Return the maximum gain to parent (node plus one side)
        return node.val + Math.max(leftGain, rightGain);
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
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            current_path = node.val + left_gain + right_gain
            if current_path > self.max_sum:
                self.max_sum = current_path
            
            return node.val + (left_gain if left_gain > right_gain else right_gain)
        
        dfs(root)
        return self.max_sum
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
    def maxPathSum(self, root: Optional['TreeNode']) -> int:
        self.max_sum = -float('inf')
        
        def dfs(node: Optional['TreeNode']) -> int:
            if not node:
                return 0
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # Path that passes through the current node (could be the answer)
            current_path_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return max gain if we continue the path upward
            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        return self.max_sum
```

## C

```c
#include <limits.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

static int maxGain(struct TreeNode* node, int *maxSum) {
    if (node == NULL) return 0;

    int left = maxGain(node->left, maxSum);
    int right = maxGain(node->right, maxSum);

    if (left < 0) left = 0;
    if (right < 0) right = 0;

    int price = node->val + left + right;
    if (price > *maxSum) *maxSum = price;

    return node->val + (left > right ? left : right);
}

int maxPathSum(struct TreeNode* root) {
    int max_sum = INT_MIN;
    maxGain(root, &max_sum);
    return max_sum;
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
    private int maxSum = int.MinValue;

    private int MaxGain(TreeNode node) {
        if (node == null) return 0;
        int left = Math.Max(MaxGain(node.left), 0);
        int right = Math.Max(MaxGain(node.right), 0);
        int priceNewPath = node.val + left + right;
        maxSum = Math.Max(maxSum, priceNewPath);
        return node.val + Math.Max(left, right);
    }

    public int MaxPathSum(TreeNode root) {
        MaxGain(root);
        return maxSum;
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
var maxPathSum = function(root) {
    let globalMax = -Infinity;
    
    const dfs = (node) => {
        if (!node) return 0;
        const leftGain = Math.max(dfs(node.left), 0);
        const rightGain = Math.max(dfs(node.right), 0);
        
        // Path price where node is the highest point
        const currentPrice = node.val + leftGain + rightGain;
        if (currentPrice > globalMax) {
            globalMax = currentPrice;
        }
        
        // Return max gain if we continue the path upwards through this node
        return node.val + Math.max(leftGain, rightGain);
    };
    
    dfs(root);
    return globalMax;
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

function maxPathSum(root: TreeNode | null): number {
    let globalMax = -Infinity;
    const dfs = (node: TreeNode | null): number => {
        if (!node) return 0;
        const leftGain = Math.max(dfs(node.left), 0);
        const rightGain = Math.max(dfs(node.right), 0);
        const currentPathSum = node.val + leftGain + rightGain;
        globalMax = Math.max(globalMax, currentPathSum);
        return node.val + Math.max(leftGain, rightGain);
    };
    dfs(root);
    return globalMax;
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
     * @var int
     */
    private $maxSum;

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function maxPathSum($root) {
        $this->maxSum = PHP_INT_MIN;
        $this->dfs($root);
        return $this->maxSum;
    }

    /**
     * @param TreeNode|null $node
     * @return int
     */
    private function dfs($node) {
        if ($node === null) {
            return 0;
        }
        $leftGain = max(0, $this->dfs($node->left));
        $rightGain = max(0, $this->dfs($node->right));

        $price = $node->val + $leftGain + $rightGain;
        if ($price > $this->maxSum) {
            $this->maxSum = $price;
        }

        return $node->val + max($leftGain, $rightGain);
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
    private var maxSum = Int.min

    func maxPathSum(_ root: TreeNode?) -> Int {
        dfs(root)
        return maxSum
    }

    private func dfs(_ node: TreeNode?) -> Int {
        guard let n = node else { return 0 }
        let leftGain = max(dfs(n.left), 0)
        let rightGain = max(dfs(n.right), 0)

        let currentPath = n.val + leftGain + rightGain
        if currentPath > maxSum {
            maxSum = currentPath
        }

        return n.val + max(leftGain, rightGain)
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
    private var maxSum = Int.MIN_VALUE

    fun maxPathSum(root: TreeNode?): Int {
        dfs(root)
        return maxSum
    }

    private fun dfs(node: TreeNode?): Int {
        if (node == null) return 0
        val leftGain = kotlin.math.max(dfs(node.left), 0)
        val rightGain = kotlin.math.max(dfs(node.right), 0)

        // Path that passes through the current node as the highest point
        val priceNewPath = node.`val` + leftGain + rightGain
        if (priceNewPath > maxSum) {
            maxSum = priceNewPath
        }

        // Return max gain to parent
        return node.`val` + kotlin.math.max(leftGain, rightGain)
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
  int _maxSum = -1 << 60;

  int maxPathSum(TreeNode? root) {
    _dfs(root);
    return _maxSum;
  }

  int _dfs(TreeNode? node) {
    if (node == null) return 0;
    int leftGain = _dfs(node.left);
    int rightGain = _dfs(node.right);

    // Discard negative contributions
    leftGain = leftGain > 0 ? leftGain : 0;
    rightGain = rightGain > 0 ? rightGain : 0;

    // Path that passes through the current node
    int priceNewPath = node.val + leftGain + rightGain;
    if (priceNewPath > _maxSum) {
      _maxSum = priceNewPath;
    }

    // Return max gain to parent
    return node.val + (leftGain > rightGain ? leftGain : rightGain);
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
var maxSum int

func maxPathSum(root *TreeNode) int {
    // Initialize with a very small number to handle all-negative trees
    maxSum = -1 << 60
    dfs(root)
    return maxSum
}

// dfs returns the maximum gain from the current node to its parent.
func dfs(node *TreeNode) int {
    if node == nil {
        return 0
    }
    leftGain := dfs(node.Left)
    rightGain := dfs(node.Right)

    // Discard negative gains; they would reduce the path sum.
    if leftGain < 0 {
        leftGain = 0
    }
    if rightGain < 0 {
        rightGain = 0
    }

    // Path price where current node is the highest point (may include both children).
    price := node.Val + leftGain + rightGain
    if price > maxSum {
        maxSum = price
    }

    // Return the maximum gain to be used by parent computation.
    if leftGain > rightGain {
        return node.Val + leftGain
    }
    return node.Val + rightGain
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

def max_path_sum(root)
  @max_sum = -Float::INFINITY
  dfs = lambda do |node|
    return 0 unless node
    left_gain = [dfs.call(node.left), 0].max
    right_gain = [dfs.call(node.right), 0].max
    current_price = node.val + left_gain + right_gain
    @max_sum = current_price if current_price > @max_sum
    node.val + [left_gain, right_gain].max
  end
  dfs.call(root)
  @max_sum.to_i
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
    private var maxSum: Int = Int.MinValue

    def maxPathSum(root: TreeNode): Int = {
        maxSum = Int.MinValue
        dfs(root)
        maxSum
    }

    private def dfs(node: TreeNode): Int = {
        if (node == null) return 0
        val leftGain = Math.max(0, dfs(node.left))
        val rightGain = Math.max(0, dfs(node.right))

        // Path that passes through this node (could be the answer)
        val priceNewPath = node.value + leftGain + rightGain
        if (priceNewPath > maxSum) maxSum = priceNewPath

        // Return max gain if we continue the same path upwards
        node.value + Math.max(leftGain, rightGain)
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn max_path_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, best: &mut i32) -> i32 {
            if let Some(rc) = node {
                let n = rc.borrow();
                let left = dfs(&n.left, best).max(0);
                let right = dfs(&n.right, best).max(0);
                let cur = n.val + left + right;
                if cur > *best {
                    *best = cur;
                }
                n.val + left.max(right)
            } else {
                0
            }
        }

        let mut ans = i32::MIN;
        dfs(&root, &mut ans);
        ans
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

(define/contract (max-path-sum root)
  (-> (or/c tree-node? #f) exact-integer?)
  (define (helper node)
    (if (not node)
        (values 0 -1000000000) ; upward gain, overall max
        (let-values ([(left-up left-max)   (helper (tree-node-left node))]
                     [(right-up right-max) (helper (tree-node-right node))])
          (define val (tree-node-val node))
          (define left-contrib  (if (> left-up 0) left-up 0))
          (define right-contrib (if (> right-up 0) right-up 0))
          (define max-up (+ val (max left-contrib right-contrib)))
          (define max-through (+ val left-contrib right-contrib))
          (define overall-max (max left-max right-max max-through))
          (values max-up overall-max)))))
  (let-values ([(_ ans) (helper root)])
    ans))
```

## Erlang

```erlang
-module(solution).
-export([max_path_sum/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec max_path_sum(Root :: #tree_node{} | null) -> integer().
max_path_sum(Root) ->
    {_Gain, Max} = helper(Root),
    Max.

helper(null) ->
    {0, -10000000000};
helper(#tree_node{val = Val, left = Left, right = Right}) ->
    {GainL, MaxL} = helper(Left),
    {GainR, MaxR} = helper(Right),

    GainLPos = erlang:max(GainL, 0),
    GainRPos = erlang:max(GainR, 0),

    Through = Val + GainLPos + GainRPos,
    UpGain = erlang:max(Val, Val + erlang:max(GainLPos, GainRPos)),

    MaxSoFar = erlang:max(erlang:max(MaxL, MaxR), Through),
    {UpGain, MaxSoFar}.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_path_sum(root :: TreeNode.t | nil) :: integer
  def max_path_sum(nil), do: 0
  def max_path_sum(root) do
    {_gain, max_sum} = helper(root)
    max_sum
  end

  defp helper(nil), do: {0, -1_000_000_000}

  defp helper(%TreeNode{val: val, left: left, right: right}) do
    {left_gain, left_max} = helper(left)
    {right_gain, right_max} = helper(right)

    left_gain = if left_gain > 0, do: left_gain, else: 0
    right_gain = if right_gain > 0, do: right_gain, else: 0

    price_newpath = val + left_gain + right_gain
    current_max = Enum.max([price_newpath, left_max, right_max])

    gain_up = val + max(left_gain, right_gain)

    {gain_up, current_max}
  end
end
```
