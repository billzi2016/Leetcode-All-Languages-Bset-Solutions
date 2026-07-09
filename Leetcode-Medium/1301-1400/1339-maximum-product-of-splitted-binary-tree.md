# 1339. Maximum Product of Splitted Binary Tree

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
    const long long MOD = 1'000'000'007LL;
    
    long long dfs(TreeNode* node, std::vector<long long>& sums) {
        if (!node) return 0;
        long long left = dfs(node->left, sums);
        long long right = dfs(node->right, sums);
        long long total = node->val + left + right;
        sums.push_back(total);
        return total;
    }
    
    int maxProduct(TreeNode* root) {
        std::vector<long long> sums;
        long long totalSum = dfs(root, sums);
        long long best = 0;
        for (long long sub : sums) {
            if (sub == totalSum) continue; // skip the whole tree
            long long product = sub * (totalSum - sub);
            if (product > best) best = product;
        }
        return static_cast<int>(best % MOD);
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
    private static final long MOD = 1_000_000_007L;
    private long totalSum;
    private long maxProduct;

    public int maxProduct(TreeNode root) {
        totalSum = computeSum(root);
        maxProduct = 0;
        computeMax(root);
        return (int)(maxProduct % MOD);
    }

    private long computeSum(TreeNode node) {
        if (node == null) return 0L;
        long left = computeSum(node.left);
        long right = computeSum(node.right);
        return node.val + left + right;
    }

    private long computeMax(TreeNode node) {
        if (node == null) return 0L;
        long left = computeMax(node.left);
        long right = computeMax(node.right);
        long subSum = node.val + left + right;
        long product = subSum * (totalSum - subSum);
        if (product > maxProduct) {
            maxProduct = product;
        }
        return subSum;
    }
}
```

## Python

```python
import sys

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        sys.setrecursionlimit(10 ** 6)
        MOD = 10**9 + 7
        subtree_sums = []

        def dfs(node):
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            subtree_sums.append(total)
            return total

        total_sum = dfs(root)
        max_product = 0
        for s in subtree_sums:
            product = s * (total_sum - s)
            if product > max_product:
                max_product = product
        return max_product % MOD
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys
sys.setrecursionlimit(10**6)

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        subtree_sums = []
        
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            total = node.val + left_sum + right_sum
            subtree_sums.append(total)
            return total
        
        total_sum = dfs(root)
        max_prod = 0
        for s in subtree_sums:
            max_prod = max(max_prod, s * (total_sum - s))
        return max_prod % MOD
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
static long long totalSum;
static long long maxProd;

static long long dfs_sum(struct TreeNode* node) {
    if (!node) return 0;
    long long left = dfs_sum(node->left);
    long long right = dfs_sum(node->right);
    return node->val + left + right;
}

static long long dfs_compute(struct TreeNode* node) {
    if (!node) return 0;
    long long left = dfs_compute(node->left);
    long long right = dfs_compute(node->right);
    long long sum = node->val + left + right;
    long long product = sum * (totalSum - sum);
    if (product > maxProd) maxProd = product;
    return sum;
}

int maxProduct(struct TreeNode* root) {
    const long long MOD = 1000000007LL;
    totalSum = dfs_sum(root);
    maxProd = 0;
    dfs_compute(root);
    return (int)(maxProd % MOD);
}
```

## Csharp

```csharp
using System;
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
    private const int MOD = 1000000007;
    
    public int MaxProduct(TreeNode root) {
        // First pass: compute total sum of all nodes
        long totalSum = 0;
        var stack = new Stack<TreeNode>();
        stack.Push(root);
        while (stack.Count > 0) {
            var node = stack.Pop();
            totalSum += node.val;
            if (node.left != null) stack.Push(node.left);
            if (node.right != null) stack.Push(node.right);
        }
        
        // Second pass: post-order to compute subtree sums and max product
        long maxProd = 0;
        var subSums = new Dictionary<TreeNode, long>();
        var postStack = new Stack<(TreeNode node, bool visited)>();
        postStack.Push((root, false));
        
        while (postStack.Count > 0) {
            var (node, visited) = postStack.Pop();
            if (node == null) continue;
            
            if (visited) {
                long leftSum = node.left != null ? subSums[node.left] : 0;
                long rightSum = node.right != null ? subSums[node.right] : 0;
                long curSum = node.val + leftSum + rightSum;
                subSums[node] = curSum;
                
                // Consider cutting the edge above this node (except for root where product is zero)
                long prod = curSum * (totalSum - curSum);
                if (prod > maxProd) maxProd = prod;
            } else {
                postStack.Push((node, true));
                if (node.right != null) postStack.Push((node.right, false));
                if (node.left != null) postStack.Push((node.left, false));
            }
        }
        
        return (int)(maxProd % MOD);
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
var maxProduct = function(root) {
    const MOD = 1000000007n;
    const subs = [];
    
    function dfs(node) {
        if (!node) return 0n;
        const leftSum = dfs(node.left);
        const rightSum = dfs(node.right);
        const curSum = BigInt(node.val) + leftSum + rightSum;
        subs.push(curSum);
        return curSum;
    }
    
    const total = dfs(root); // total sum of the whole tree (root's subtree)
    let maxProd = 0n;
    
    for (let i = 0; i < subs.length - 1; i++) { // exclude the root itself
        const s = subs[i];
        const prod = s * (total - s);
        if (prod > maxProd) maxProd = prod;
    }
    
    return Number(maxProd % MOD);
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

function maxProduct(root: TreeNode | null): number {
    if (!root) return 0;
    const MOD = 1000000007n;
    const sums: number[] = [];

    function dfs(node: TreeNode | null): number {
        if (!node) return 0;
        const leftSum = dfs(node.left);
        const rightSum = dfs(node.right);
        const total = node.val + leftSum + rightSum;
        sums.push(total);
        return total;
    }

    const totalSum = dfs(root);
    let maxProd = 0n;

    for (const s of sums) {
        const prod = BigInt(s) * BigInt(totalSum - s);
        if (prod > maxProd) maxProd = prod;
    }

    return Number(maxProd % MOD);
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
    const MOD = 1000000007;

    /**
     * @param TreeNode $root
     * @return int
     */
    function maxProduct($root) {
        $subSums = [];
        $total = $this->dfs($root, $subSums);
        $maxProd = 0;
        foreach ($subSums as $s) {
            $prod = $s * ($total - $s);
            if ($prod > $maxProd) {
                $maxProd = $prod;
            }
        }
        return $maxProd % self::MOD;
    }

    private function dfs($node, &$list) {
        if ($node === null) {
            return 0;
        }
        $leftSum = $this->dfs($node->left, $list);
        $rightSum = $this->dfs($node->right, $list);
        $curSum = $node->val + $leftSum + $rightSum;
        $list[] = $curSum;
        return $curSum;
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
    func maxProduct(_ root: TreeNode?) -> Int {
        var subSums = [Int64]()
        
        func dfs(_ node: TreeNode?) -> Int64 {
            guard let n = node else { return 0 }
            let left = dfs(n.left)
            let right = dfs(n.right)
            let sum = left + right + Int64(n.val)
            subSums.append(sum)
            return sum
        }
        
        let total = dfs(root)
        var maxProd: Int64 = 0
        for s in subSums {
            let prod = s * (total - s)
            if prod > maxProd { maxProd = prod }
        }
        let MOD: Int64 = 1_000_000_007
        return Int(maxProd % MOD)
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
    private val MOD = 1_000_000_007L

    fun maxProduct(root: TreeNode?): Int {
        if (root == null) return 0

        // First collect nodes in a order that allows post‑order processing
        val stack = java.util.ArrayDeque<TreeNode>()
        val order = java.util.ArrayList<TreeNode>()
        stack.add(root)
        while (!stack.isEmpty()) {
            val node = stack.poll()
            order.add(node)
            node.left?.let { stack.add(it) }
            node.right?.let { stack.add(it) }
        }

        // Compute subtree sums using the reverse of the collected order
        val sumMap = java.util.HashMap<TreeNode, Long>()
        val subSums = java.util.ArrayList<Long>()
        for (i in order.size - 1 downTo 0) {
            val node = order[i]
            var s = node.`val`.toLong()
            node.left?.let { s += sumMap[it]!! }
            node.right?.let { s += sumMap[it]!! }
            sumMap[node] = s
            subSums.add(s)
        }

        val total = subSums.last()
        var maxProd = 0L
        // All subtree sums are in subSums; the last one corresponds to the whole tree.
        for (i in 0 until subSums.size - 1) {
            val part = subSums[i]
            val prod = part * (total - part)
            if (prod > maxProd) maxProd = prod
        }

        return (maxProd % MOD).toInt()
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
  static const int _mod = 1000000007;
  late int _totalSum;
  final List<int> _subSums = [];

  int maxProduct(TreeNode? root) {
    _totalSum = _dfs(root);
    int maxProd = 0;
    for (final s in _subSums) {
      int prod = s * (_totalSum - s);
      if (prod > maxProd) maxProd = prod;
    }
    return maxProd % _mod;
  }

  int _dfs(TreeNode? node) {
    if (node == null) return 0;
    int left = _dfs(node.left);
    int right = _dfs(node.right);
    int cur = node.val + left + right;
    _subSums.add(cur);
    return cur;
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
func maxProduct(root *TreeNode) int {
	const MOD int64 = 1_000_000_007

	var subtreeSums []int64

	var dfs func(*TreeNode) int64
	dfs = func(node *TreeNode) int64 {
		if node == nil {
			return 0
		}
		left := dfs(node.Left)
		right := dfs(node.Right)
		sum := int64(node.Val) + left + right
		subtreeSums = append(subtreeSums, sum)
		return sum
	}

	total := dfs(root)

	var maxProd int64
	for _, s := range subtreeSums {
		prod := s * (total - s)
		if prod > maxProd {
			maxProd = prod
		}
	}
	return int(maxProd % MOD)
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

def max_product(root)
  mod = 1_000_000_007
  sums = {}
  stack = [[root, false]]
  while !stack.empty?
    node, visited = stack.pop
    next if node.nil?
    if visited
      left_sum = node.left ? sums[node.left.object_id] : 0
      right_sum = node.right ? sums[node.right.object_id] : 0
      sums[node.object_id] = node.val + left_sum + right_sum
    else
      stack << [node, true]
      stack << [node.right, false] if node.right
      stack << [node.left, false] if node.left
    end
  end

  total = sums[root.object_id]
  max_prod = 0
  sums.each_value do |sub|
    prod = sub * (total - sub)
    max_prod = prod if prod > max_prod
  end
  max_prod % mod
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
  def maxProduct(root: TreeNode): Int = {
    val MOD: Long = 1000000007L

    // First pass: compute total sum of all node values
    var total: Long = 0L
    val stack1 = new scala.collection.mutable.Stack[TreeNode]()
    stack1.push(root)
    while (stack1.nonEmpty) {
      val node = stack1.pop()
      total += node.value.toLong
      if (node.left != null) stack1.push(node.left)
      if (node.right != null) stack1.push(node.right)
    }

    // Second pass: post-order traversal to compute subtree sums and max product
    var maxProd: Long = 0L
    val stack = new scala.collection.mutable.Stack[(TreeNode, Boolean)]()
    stack.push((root, false))

    while (stack.nonEmpty) {
      val (node, visited) = stack.pop()
      if (!visited) {
        // push node back as visited after its children
        stack.push((node, true))
        if (node.right != null) stack.push((node.right, false))
        if (node.left != null)  stack.push((node.left, false))
      } else {
        var sum: Long = node.value.toLong
        if (node.left != null)  sum += node.left.value.toLong
        if (node.right != null) sum += node.right.value.toLong

        // consider split at edge to parent (skip root)
        if (node ne root) {
          val prod = sum * (total - sum)
          if (prod > maxProd) maxProd = prod
        }

        // store subtree sum back into the node (fits in Int per constraints)
        node.value = sum.toInt
      }
    }

    (maxProd % MOD).toInt
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn max_product(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        const MOD: i64 = 1_000_000_007;

        fn subtree_sum(node: &Option<Rc<RefCell<TreeNode>>>) -> i64 {
            if let Some(rc) = node {
                let n = rc.borrow();
                let left = subtree_sum(&n.left);
                let right = subtree_sum(&n.right);
                left + right + n.val as i64
            } else {
                0
            }
        }

        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, total: i64, best: &mut i64) -> i64 {
            if let Some(rc) = node {
                let n = rc.borrow();
                let left = dfs(&n.left, total, best);
                let right = dfs(&n.right, total, best);
                let cur = left + right + n.val as i64;
                let prod = cur * (total - cur);
                if prod > *best {
                    *best = prod;
                }
                cur
            } else {
                0
            }
        }

        let total = subtree_sum(&root);
        let mut ans: i64 = 0;
        dfs(&root, total, &mut ans);
        (ans % MOD) as i32
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

(define/contract (max-product root)
  (-> (or/c tree-node? #f) exact-integer?)
  (if (not root)
      0
      (let ((MOD 1000000007)
            (sums '()))
        ;; post‑order traversal to collect subtree sums
        (define (dfs node)
          (if (not node)
              0
              (let* ((left-sum  (dfs (tree-node-left node)))
                     (right-sum (dfs (tree-node-right node)))
                     (sub-sum   (+ (tree-node-val node) left-sum right-sum)))
                (set! sums (cons sub-sum sums))
                sub-sum)))
        (define total (dfs root))
        (define max-prod 0)
        (for ([s sums])
          (when (< s total)               ; ignore the whole tree itself
            (let ((prod (* s (- total s))))
              (when (> prod max-prod)
                (set! max-prod prod)))))
        (modulo max-prod MOD))))
```

## Erlang

```erlang
-module(solution).
-export([max_product/1]).

%% Definition for a binary tree node.
-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec max_product(Root :: #tree_node{} | null) -> integer().
max_product(Root) ->
    Mod = 1000000007,
    {Total, Sums} = collect(Root),
    MaxProd = lists:foldl(fun(S, Acc) ->
                Prod = S * (Total - S),
                if Prod > Acc -> Prod; true -> Acc end
            end, 0, Sums),
    MaxProd rem Mod.

collect(Node) ->
    {Sum, RevList} = collect_sums(Node, []),
    {Sum, lists:reverse(RevList)}.

collect_sums(null, Acc) ->
    {0, Acc};
collect_sums(Node, Acc) ->
    {Lsum, Acc1} = collect_sums(Node#tree_node.left, Acc),
    {Rsum, Acc2} = collect_sums(Node#tree_node.right, Acc1),
    Sum = Node#tree_node.val + Lsum + Rsum,
    {Sum, [Sum | Acc2]}.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @mod 1_000_000_007

  @spec max_product(root :: TreeNode.t() | nil) :: integer()
  def max_product(root) do
    {total, sums} = dfs(root, [])
    max_prod =
      Enum.reduce(sums, 0, fn s, acc ->
        prod = s * (total - s)
        if prod > acc, do: prod, else: acc
      end)

    rem(max_prod, @mod)
  end

  defp dfs(nil, acc), do: {0, acc}

  defp dfs(%TreeNode{val: v, left: l, right: r}, acc) do
    {left_sum, acc1} = dfs(l, acc)
    {right_sum, acc2} = dfs(r, acc1)
    cur = v + left_sum + right_sum
    {cur, [cur | acc2]}
  end
end
```
