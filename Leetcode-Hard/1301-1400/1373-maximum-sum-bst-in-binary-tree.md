# 1373. Maximum Sum BST in Binary Tree

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
    int maxSumBST(TreeNode* root) {
        long long ans = 0;
        dfs(root, ans);
        return (int)ans;
    }
private:
    // returns tuple: {isBST, sum, minVal, maxVal}
    struct Info {
        bool isBst;
        long long sum;
        int mn;
        int mx;
    };
    
    Info dfs(TreeNode* node, long long& ans) {
        if (!node) {
            return {true, 0, INT_MAX, INT_MIN};
        }
        Info left = dfs(node->left, ans);
        Info right = dfs(node->right, ans);
        
        if (left.isBst && right.isBst && node->val > left.mx && node->val < right.mn) {
            long long curSum = left.sum + right.sum + node->val;
            ans = max(ans, curSum);
            int curMin = min(node->val, left.mn);
            int curMax = max(node->val, right.mx);
            return {true, curSum, curMin, curMax};
        } else {
            // Not a BST; sum value irrelevant
            return {false, 0, 0, 0};
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
    private int maxSum = 0;

    public int maxSumBST(TreeNode root) {
        dfs(root);
        return maxSum;
    }

    // returns array: [isBST (1/0), sum, minVal, maxVal]
    private int[] dfs(TreeNode node) {
        if (node == null) {
            return new int[]{1, 0, Integer.MAX_VALUE, Integer.MIN_VALUE};
        }
        int[] left = dfs(node.left);
        int[] right = dfs(node.right);

        boolean isBST = left[0] == 1 && right[0] == 1 &&
                        node.val > left[3] && node.val < right[2];

        if (isBST) {
            int sum = left[1] + right[1] + node.val;
            maxSum = Math.max(maxSum, sum);
            int minVal = Math.min(node.val, left[2]);
            int maxVal = Math.max(node.val, right[3]);
            return new int[]{1, sum, minVal, maxVal};
        } else {
            // Not a BST; values are irrelevant for parent checks
            return new int[]{0, 0, 0, 0};
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
    def maxSumBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = 0

        def dfs(node):
            if not node:
                # is BST, sum=0, min=+inf, max=-inf
                return (True, 0, float('inf'), float('-inf'))
            
            left_is_bst, left_sum, left_min, left_max = dfs(node.left)
            right_is_bst, right_sum, right_min, right_max = dfs(node.right)

            # Check BST property for current node
            if left_is_bst and right_is_bst and node.val > left_max and node.val < right_min:
                cur_sum = left_sum + right_sum + node.val
                self.max_sum = max(self.max_sum, cur_sum)
                cur_min = min(left_min, node.val)
                cur_max = max(right_max, node.val)
                return (True, cur_sum, cur_min, cur_max)
            else:
                # Not a BST; sum is irrelevant
                return (False, 0, 0, 0)

        dfs(root)
        return self.max_sum
```

## Python3

```python
import sys
from typing import Optional

sys.setrecursionlimit(10**6)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        INF = float('inf')
        
        def dfs(node):
            nonlocal ans
            if not node:
                return True, 0, INF, -INF  # isBST, sum, min, max
            
            left_is, left_sum, left_min, left_max = dfs(node.left)
            right_is, right_sum, right_min, right_max = dfs(node.right)
            
            if left_is and right_is and node.val > left_max and node.val < right_min:
                cur_sum = left_sum + right_sum + node.val
                ans = max(ans, cur_sum)
                cur_min = min(left_min, node.val)
                cur_max = max(right_max, node.val)
                return True, cur_sum, cur_min, cur_max
            else:
                # Not a BST; sum is irrelevant for parent checks
                return False, 0, 0, 0
        
        dfs(root)
        return ans
```

## C

```c
#include <stddef.h>
#include <limits.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct {
    int isBST;
    int sum;
    int minVal;
    int maxVal;
} Info;

static int bestSum;

Info dfs(struct TreeNode* node) {
    if (!node) return (Info){1, 0, INT_MAX, INT_MIN};
    
    Info left = dfs(node->left);
    Info right = dfs(node->right);
    Info cur;
    
    if (left.isBST && right.isBST &&
        node->val > left.maxVal && node->val < right.minVal) {
        cur.isBST = 1;
        cur.sum = left.sum + right.sum + node->val;
        
        int mn = node->val;
        if (left.minVal != INT_MAX && left.minVal < mn) mn = left.minVal;
        int mx = node->val;
        if (right.maxVal != INT_MIN && right.maxVal > mx) mx = right.maxVal;
        cur.minVal = mn;
        cur.maxVal = mx;
        
        if (cur.sum > bestSum) bestSum = cur.sum;
    } else {
        cur.isBST = 0;
        cur.sum = 0;
        cur.minVal = 0;
        cur.maxVal = 0;
    }
    
    return cur;
}

int maxSumBST(struct TreeNode* root) {
    bestSum = 0;
    dfs(root);
    return bestSum;
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
    private int maxSum = 0;

    public int MaxSumBST(TreeNode root)
    {
        DFS(root);
        return maxSum;
    }

    private (bool isBST, long sum, int minVal, int maxVal) DFS(TreeNode node)
    {
        if (node == null)
        {
            // An empty tree is a BST with sum 0,
            // min set to +inf and max set to -inf for comparison.
            return (true, 0L, int.MaxValue, int.MinValue);
        }

        var left = DFS(node.left);
        var right = DFS(node.right);

        bool isCurrentBST = left.isBST && right.isBST &&
                            node.val > left.maxVal && node.val < right.minVal;

        if (isCurrentBST)
        {
            long currentSum = left.sum + right.sum + node.val;
            maxSum = Math.Max(maxSum, (int)currentSum);

            int curMin = Math.Min(node.val, left.minVal);
            int curMax = Math.Max(node.val, right.maxVal);
            return (true, currentSum, curMin, curMax);
        }
        else
        {
            // Not a BST; values are irrelevant.
            return (false, 0L, 0, 0);
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
var maxSumBST = function(root) {
    let maxSum = 0;
    
    const dfs = (node) => {
        if (!node) return [true, 0, Infinity, -Infinity]; // isBST, sum, min, max
        
        const left = dfs(node.left);
        const right = dfs(node.right);
        
        const isCurrBST = left[0] && right[0] && node.val > left[3] && node.val < right[2];
        if (isCurrBST) {
            const currSum = left[1] + right[1] + node.val;
            maxSum = Math.max(maxSum, currSum);
            const currMin = Math.min(node.val, left[2]);
            const currMax = Math.max(node.val, right[3]);
            return [true, currSum, currMin, currMax];
        }
        // Not a BST
        return [false, 0, 0, 0];
    };
    
    dfs(root);
    return maxSum;
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

function maxSumBST(root: TreeNode | null): number {
    let maxSum = 0;

    // returns [isBST, sum, minVal, maxVal]
    function dfs(node: TreeNode | null): [boolean, number, number, number] {
        if (!node) {
            return [true, 0, Infinity, -Infinity];
        }

        const left = dfs(node.left);
        const right = dfs(node.right);

        const isBST = left[0] && right[0] && node.val > left[3] && node.val < right[2];

        if (isBST) {
            const sum = left[1] + right[1] + node.val;
            maxSum = Math.max(maxSum, sum);
            const minVal = Math.min(node.val, left[2]);
            const maxVal = Math.max(node.val, right[3]);
            return [true, sum, minVal, maxVal];
        } else {
            // Not a BST; values are irrelevant for parent checks
            return [false, 0, 0, 0];
        }
    }

    dfs(root);
    return maxSum;
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
    private int $maxSum = 0;

    /**
     * @param TreeNode $root
     * @return integer
     */
    function maxSumBST($root) {
        $this->maxSum = 0;
        $this->dfs($root);
        return $this->maxSum;
    }

    private function dfs(?TreeNode $node): array {
        // returns [isBST (bool), sum (int), minVal (int), maxVal (int)]
        if ($node === null) {
            return [true, 0, PHP_INT_MAX, PHP_INT_MIN];
        }

        $left = $this->dfs($node->left);
        $right = $this->dfs($node->right);

        $isBST = $left[0] && $right[0] && ($node->val > $left[3]) && ($node->val < $right[2]);

        if ($isBST) {
            $sum = $node->val + $left[1] + $right[1];
            $this->maxSum = max($this->maxSum, $sum);
            $minVal = min($node->val, $left[2]);
            $maxVal = max($node->val, $right[3]);
            return [true, $sum, $minVal, $maxVal];
        } else {
            // Not a BST; sum is irrelevant for parent checks
            return [false, 0, 0, 0];
        }
    }
}
```

## Swift

```swift
class Solution {
    private var maxSum = 0

    func maxSumBST(_ root: TreeNode?) -> Int {
        _ = dfs(root)
        return maxSum
    }

    private func dfs(_ node: TreeNode?) -> (isBST: Bool, sum: Int, minVal: Int, maxVal: Int) {
        guard let n = node else {
            return (true, 0, Int.max, Int.min)
        }
        let left = dfs(n.left)
        let right = dfs(n.right)

        if left.isBST && right.isBST && n.val > left.maxVal && n.val < right.minVal {
            let curSum = left.sum + right.sum + n.val
            maxSum = max(maxSum, curSum)
            let curMin = min(left.minVal, n.val)
            let curMax = max(right.maxVal, n.val)
            return (true, curSum, curMin, curMax)
        } else {
            return (false, 0, 0, 0)
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    private var maxSum = 0

    fun maxSumBST(root: TreeNode?): Int {
        dfs(root)
        return maxSum
    }

    private data class Info(val isBST: Boolean, val sum: Int, val min: Int, val max: Int)

    private fun dfs(node: TreeNode?): Info {
        if (node == null) {
            return Info(true, 0, Int.MAX_VALUE, Int.MIN_VALUE)
        }
        val left = dfs(node.left)
        val right = dfs(node.right)

        if (left.isBST && right.isBST && node.`val` > left.max && node.`val` < right.min) {
            val sum = left.sum + right.sum + node.`val`
            maxSum = kotlin.math.max(maxSum, sum)
            val minVal = kotlin.math.min(left.min, node.`val`)
            val maxVal = kotlin.math.max(right.max, node.`val`)
            return Info(true, sum, minVal, maxVal)
        }
        return Info(false, 0, 0, 0)
    }
}
```

## Dart

```dart
import 'dart:math' as math;

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
  int maxSumBST(TreeNode? root) {
    const int INF = 1 << 60;
    int maxSum = 0;

    List<int> dfs(TreeNode? node) {
      if (node == null) {
        return [1, 0, INF, -INF];
      }
      var left = dfs(node.left);
      var right = dfs(node.right);

      bool isLeftBST = left[0] == 1;
      bool isRightBST = right[0] == 1;

      int sumLeft = left[1];
      int sumRight = right[1];
      int minLeft = left[2];
      int maxLeft = left[3];
      int minRight = right[2];
      int maxRight = right[3];

      if (isLeftBST &&
          isRightBST &&
          node.val > maxLeft &&
          node.val < minRight) {
        int sum = sumLeft + sumRight + node.val;
        maxSum = math.max(maxSum, sum);
        int minVal = math.min(node.val, minLeft);
        int maxVal = math.max(node.val, maxRight);
        return [1, sum, minVal, maxVal];
      } else {
        return [0, 0, 0, 0];
      }
    }

    dfs(root);
    return maxSum;
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

const INF = 1 << 60

var maxSum int

func maxSumBST(root *TreeNode) int {
    maxSum = 0
    dfs(root)
    return maxSum
}

// returns (isBST, sum, minVal, maxVal)
func dfs(node *TreeNode) (bool, int, int, int) {
    if node == nil {
        return true, 0, INF, -INF
    }
    leftIsBST, leftSum, leftMin, leftMax := dfs(node.Left)
    rightIsBST, rightSum, rightMin, rightMax := dfs(node.Right)

    if leftIsBST && rightIsBST && node.Val > leftMax && node.Val < rightMin {
        sum := leftSum + rightSum + node.Val
        if sum > maxSum {
            maxSum = sum
        }
        minVal := node.Val
        if leftMin < minVal {
            minVal = leftMin
        }
        maxVal := node.Val
        if rightMax > maxVal {
            maxVal = rightMax
        }
        return true, sum, minVal, maxVal
    }
    // Not a BST
    return false, 0, 0, 0
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

def max_sum_bst(root)
  @max_sum = 0
  dfs(root)
  @max_sum
end

def dfs(node)
  return [true, 0, Float::INFINITY, -Float::INFINITY] if node.nil?

  left_is_bst, left_sum, left_min, left_max = dfs(node.left)
  right_is_bst, right_sum, right_min, right_max = dfs(node.right)

  if left_is_bst && right_is_bst && node.val > left_max && node.val < right_min
    cur_sum = left_sum + right_sum + node.val
    @max_sum = [@max_sum, cur_sum].max
    cur_min = [left_min, node.val].min
    cur_max = [right_max, node.val].max
    [true, cur_sum, cur_min, cur_max]
  else
    [false, 0, 0, 0]
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
    def maxSumBST(root: TreeNode): Int = {
        var maxSum = 0

        def dfs(node: TreeNode): (Boolean, Int, Int, Int) = {
            if (node == null) return (true, 0, Int.MaxValue, Int.MinValue)

            val left  = dfs(node.left)
            val right = dfs(node.right)

            if (left._1 && right._1 && node.value > left._4 && node.value < right._3) {
                val sum = left._2 + right._2 + node.value
                maxSum = math.max(maxSum, sum)
                val minVal = math.min(node.value, left._3)
                val maxVal = math.max(node.value, right._4)
                (true, sum, minVal, maxVal)
            } else {
                (false, 0, 0, 0)
            }
        }

        dfs(root)
        maxSum
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn max_sum_bst(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, best: &mut i32) -> (bool, i64, i32, i32) {
            if node.is_none() {
                return (true, 0, i32::MAX, i32::MIN);
            }
            let n = node.unwrap();
            let left = dfs(n.borrow().left.clone(), best);
            let right = dfs(n.borrow().right.clone(), best);
            let val = n.borrow().val as i64;
            if left.0 && right.0 && (n.borrow().val > left.3) && (n.borrow().val < right.2) {
                let sum = left.1 + right.1 + val;
                *best = (*best).max(sum as i32);
                let min_val = if left.2 == i32::MAX { n.borrow().val } else { left.2 };
                let max_val = if right.3 == i32::MIN { n.borrow().val } else { right.3 };
                (true, sum, min_val, max_val)
            } else {
                (false, 0, 0, 0)
            }
        }

        let mut ans = 0;
        dfs(root, &mut ans);
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

(define/contract (max-sum-bst root)
  (-> (or/c tree-node? #f) exact-integer?)
  (let ((max-sum 0))
    (define (dfs node)
      (if (not node)
          (values #t 0 +inf.0 -inf.0)               ; isBST sum min max
          (let-values ([(lbst lsum lmin lmax) (dfs (tree-node-left node))]
                       [(rbst rsum rmin rmax) (dfs (tree-node-right node))])
            (define val (tree-node-val node))
            (if (and lbst rbst (< lmax val) (< val rmin))
                (let* ((curr (+ val lsum rsum)))
                  (when (> curr max-sum) (set! max-sum curr))
                  (values #t curr (min lmin val) (max rmax val)))
                (values #f 0 0 0))))))
    (dfs root)
    max-sum))
```

## Erlang

```erlang
-define(INF_POS, 1 bsl 30).
-define(INF_NEG, -?INF_POS).

-spec max_sum_bst(Root :: #tree_node{} | null) -> integer().
max_sum_bst(Root) ->
    {_, _, _, _, Max} = helper(Root),
    Max.

helper(null) ->
    {true, 0, ?INF_POS, ?INF_NEG, 0};
helper(#tree_node{val = Val, left = Left, right = Right}) ->
    {LIsBST, LSum, LMin, LMax, LBest} = helper(Left),
    {RIsBST, RSum, RMin, RMax, RBest} = helper(Right),
    IsBST = LIsBST andalso RIsBST andalso Val > LMax andalso Val < RMin,
    case IsBST of
        true ->
            CurSum = LSum + RSum + Val,
            CurMin = erlang:min(Val, LMin),
            CurMax = erlang:max(Val, RMax),
            Best = erlang:max(CurSum, erlang:max(LBest, RBest));
        false ->
            CurSum = 0,
            CurMin = 0,
            CurMax = 0,
            Best = erlang:max(LBest, RBest)
    end,
    {IsBST, CurSum, CurMin, CurMax, Best}.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sum_bst(root :: TreeNode.t | nil) :: integer
  def max_sum_bst(root) do
    {_is_bst, _sum, _min, _max, best} = dfs(root)
    best
  end

  @pos_inf 1_000_000_000
  @neg_inf -1_000_000_000

  defp dfs(nil), do: {true, 0, @pos_inf, @neg_inf, 0}

  defp dfs(%TreeNode{val: v, left: l, right: r}) do
    {l_is_bst, l_sum, l_min, l_max, l_best} = dfs(l)
    {r_is_bst, r_sum, r_min, r_max, r_best} = dfs(r)

    is_bst = l_is_bst and r_is_bst and v > l_max and v < r_min

    sum = if is_bst, do: l_sum + r_sum + v, else: 0
    min_val = if is_bst, do: min(v, l_min), else: 0
    max_val = if is_bst, do: max(v, r_max), else: 0

    candidate = if is_bst, do: sum, else: @neg_inf
    best = Enum.max([l_best, r_best, candidate])

    {is_bst, sum, min_val, max_val, best}
  end
end
```
