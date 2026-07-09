# 2265. Count Nodes Equal to Average of Subtree

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
    int averageOfSubtree(TreeNode* root) {
        int ans = 0;
        function<pair<long long,int>(TreeNode*)> dfs = [&](TreeNode* node) -> pair<long long,int> {
            if (!node) return {0,0};
            auto left = dfs(node->left);
            auto right = dfs(node->right);
            long long sum = left.first + right.first + node->val;
            int cnt = left.second + right.second + 1;
            if (sum / cnt == node->val) ++ans;
            return {sum, cnt};
        };
        dfs(root);
        return ans;
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
    private int answer = 0;

    public int averageOfSubtree(TreeNode root) {
        dfs(root);
        return answer;
    }

    // returns {sum of subtree, count of nodes in subtree}
    private long[] dfs(TreeNode node) {
        if (node == null) {
            return new long[]{0L, 0L};
        }
        long[] left = dfs(node.left);
        long[] right = dfs(node.right);
        long sum = left[0] + right[0] + node.val;
        long cnt = left[1] + right[1] + 1;
        if (node.val == sum / cnt) {
            answer++;
        }
        return new long[]{sum, cnt};
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
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0

        def dfs(node):
            if not node:
                return (0, 0)
            left_sum, left_cnt = dfs(node.left)
            right_sum, right_cnt = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_cnt = left_cnt + right_cnt + 1

            if node.val == total_sum // total_cnt:
                self.count += 1

            return (total_sum, total_cnt)

        dfs(root)
        return self.count
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
    def averageOfSubtree(self, root: 'TreeNode') -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return (0, 0)
            left_sum, left_cnt = dfs(node.left)
            right_sum, right_cnt = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_cnt = left_cnt + right_cnt + 1

            if node.val == total_sum // total_cnt:
                ans += 1

            return (total_sum, total_cnt)

        dfs(root)
        return ans
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

static int answer;

typedef struct {
    long long sum;
    int cnt;
} Pair;

static Pair dfs(struct TreeNode* node) {
    if (node == NULL) {
        Pair p = {0, 0};
        return p;
    }
    Pair left = dfs(node->left);
    Pair right = dfs(node->right);
    
    long long totalSum = left.sum + right.sum + node->val;
    int totalCnt = left.cnt + right.cnt + 1;
    
    if ((int)(totalSum / totalCnt) == node->val) {
        answer++;
    }
    
    Pair res;
    res.sum = totalSum;
    res.cnt = totalCnt;
    return res;
}

int averageOfSubtree(struct TreeNode* root) {
    answer = 0;
    dfs(root);
    return answer;
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
    private int _count;

    public int AverageOfSubtree(TreeNode root) {
        _count = 0;
        Dfs(root);
        return _count;
    }

    private (int sum, int cnt) Dfs(TreeNode node) {
        if (node == null) {
            return (0, 0);
        }
        var left = Dfs(node.left);
        var right = Dfs(node.right);

        int totalSum = left.sum + right.sum + node.val;
        int totalCnt = left.cnt + right.cnt + 1;

        if (totalSum / totalCnt == node.val) {
            _count++;
        }

        return (totalSum, totalCnt);
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
var averageOfSubtree = function(root) {
    let count = 0;
    const dfs = (node) => {
        if (!node) return [0, 0];
        const left = dfs(node.left);
        const right = dfs(node.right);
        const sum = left[0] + right[0] + node.val;
        const cnt = left[1] + right[1] + 1;
        if (Math.floor(sum / cnt) === node.val) count++;
        return [sum, cnt];
    };
    dfs(root);
    return count;
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

function averageOfSubtree(root: TreeNode | null): number {
    let count = 0;
    const dfs = (node: TreeNode | null): [number, number] => {
        if (!node) return [0, 0];
        const left = dfs(node.left);
        const right = dfs(node.right);
        const sum = left[0] + right[0] + node.val;
        const cnt = left[1] + right[1] + 1;
        if (Math.floor(sum / cnt) === node.val) count++;
        return [sum, cnt];
    };
    dfs(root);
    return count;
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
     * @return Integer
     */
    function averageOfSubtree($root) {
        $this->cnt = 0;
        $this->dfs($root);
        return $this->cnt;
    }

    private function dfs($node) {
        if ($node === null) {
            return [0, 0];
        }
        [$lsum, $lcnt] = $this->dfs($node->left);
        [$rsum, $rcnt] = $this->dfs($node->right);

        $sum = $lsum + $rsum + $node->val;
        $cnt = $lcnt + $rcnt + 1;

        if (intdiv($sum, $cnt) === $node->val) {
            $this->cnt++;
        }

        return [$sum, $cnt];
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
    private var count = 0
    
    func averageOfSubtree(_ root: TreeNode?) -> Int {
        dfs(root)
        return count
    }
    
    @discardableResult
    private func dfs(_ node: TreeNode?) -> (sum: Int, cnt: Int) {
        guard let n = node else { return (0, 0) }
        let left = dfs(n.left)
        let right = dfs(n.right)
        let totalSum = left.sum + right.sum + n.val
        let totalCnt = left.cnt + right.cnt + 1
        if totalSum / totalCnt == n.val {
            count += 1
        }
        return (totalSum, totalCnt)
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
    private var count = 0

    fun averageOfSubtree(root: TreeNode?): Int {
        dfs(root)
        return count
    }

    private fun dfs(node: TreeNode?): Pair<Int, Int> {
        if (node == null) return Pair(0, 0)

        val left = dfs(node.left)
        val right = dfs(node.right)

        val sum = left.first + right.first + node.`val`
        val cnt = left.second + right.second + 1

        if (sum / cnt == node.`val`) {
            count++
        }

        return Pair(sum, cnt)
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
  int _answer = 0;

  List<int> _dfs(TreeNode? node) {
    if (node == null) return [0, 0];
    final left = _dfs(node.left);
    final right = _dfs(node.right);
    final sum = left[0] + right[0] + node.val;
    final cnt = left[1] + right[1] + 1;
    if (node.val == sum ~/ cnt) {
      _answer++;
    }
    return [sum, cnt];
  }

  int averageOfSubtree(TreeNode? root) {
    _answer = 0;
    _dfs(root);
    return _answer;
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
func averageOfSubtree(root *TreeNode) int {
	var ans int
	var dfs func(*TreeNode) (int, int)
	dfs = func(node *TreeNode) (int, int) {
		if node == nil {
			return 0, 0
		}
		leftSum, leftCnt := dfs(node.Left)
		rightSum, rightCnt := dfs(node.Right)

		sum := leftSum + rightSum + node.Val
		cnt := leftCnt + rightCnt + 1

		if sum/cnt == node.Val {
			ans++
		}
		return sum, cnt
	}
	dfs(root)
	return ans
}
```

## Ruby

```ruby
# Definition for a binary tree node.
# class TreeNode
#   attr_accessor :val, :left, :right
#   def initialize(val = 0, left = nil, right = nil)
#     @val = val
#     @left = left
#     @right = right
#   end
# end

def average_of_subtree(root)
  ans = 0
  dfs = lambda do |node|
    return [0, 0] unless node
    left_sum, left_cnt = dfs.call(node.left)
    right_sum, right_cnt = dfs.call(node.right)
    total_sum = left_sum + right_sum + node.val
    total_cnt = left_cnt + right_cnt + 1
    ans += 1 if node.val == total_sum / total_cnt
    [total_sum, total_cnt]
  end
  dfs.call(root)
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
    def averageOfSubtree(root: TreeNode): Int = {
        var answer = 0

        def dfs(node: TreeNode): (Long, Int) = {
            if (node == null) return (0L, 0)
            val (leftSum, leftCnt)   = dfs(node.left)
            val (rightSum, rightCnt) = dfs(node.right)

            val totalSum = leftSum + rightSum + node.value
            val totalCnt = leftCnt + rightCnt + 1

            if (node.value == (totalSum / totalCnt).toInt) {
                answer += 1
            }
            (totalSum, totalCnt)
        }

        dfs(root)
        answer
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn average_of_subtree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, ans: &mut i32) -> (i64, i32) {
            if let Some(rc_node) = node {
                let left = rc_node.borrow().left.clone();
                let right = rc_node.borrow().right.clone();
                let (lsum, lcnt) = dfs(left, ans);
                let (rsum, rcnt) = dfs(right, ans);
                let val = rc_node.borrow().val as i64;
                let sum = lsum + rsum + val;
                let cnt = lcnt + rcnt + 1;
                if sum / cnt as i64 == val {
                    *ans += 1;
                }
                (sum, cnt)
            } else {
                (0, 0)
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
(define/contract (average-of-subtree root)
  (-> (or/c tree-node? #f) exact-integer?)
  (let ((cnt 0))
    (define (dfs node)
      (if (not node)
          (values 0 0)
          (let-values (((lsum lcnt) (dfs (tree-node-left node)))
                       ((rsum rcnt) (dfs (tree-node-right node))))
            (define sum (+ lsum rsum (tree-node-val node)))
            (define total (+ lcnt rcnt 1))
            (when (= (quotient sum total) (tree-node-val node))
              (set! cnt (+ cnt 1)))
            (values sum total))))
    (dfs root)
    cnt))
```

## Erlang

```erlang
-module(solution).
-export([average_of_subtree/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec average_of_subtree(Root :: #tree_node{} | null) -> integer().
average_of_subtree(null) ->
    0;
average_of_subtree(Root) ->
    {_, _, Count} = dfs(Root),
    Count.

dfs(null) ->
    {0, 0, 0};
dfs(#tree_node{val = Val, left = Left, right = Right}) ->
    {LSum, LCount, LMatch} = dfs(Left),
    {RSum, RCount, RMatch} = dfs(Right),
    Sum = LSum + RSum + Val,
    Count = LCount + RCount + 1,
    Avg = Sum div Count,
    Match = if
        Avg == Val -> LMatch + RMatch + 1;
        true       -> LMatch + RMatch
    end,
    {Sum, Count, Match}.
```

## Elixir

```elixir
defmodule Solution do
  @spec average_of_subtree(root :: TreeNode.t | nil) :: integer
  def average_of_subtree(root) do
    {_sum, _cnt, matches} = dfs(root)
    matches
  end

  defp dfs(nil), do: {0, 0, 0}

  defp dfs(%TreeNode{val: v, left: l, right: r}) do
    {lsum, lcnt, lmatch} = dfs(l)
    {rsum, rcnt, rmatch} = dfs(r)

    sum = lsum + rsum + v
    cnt = lcnt + rcnt + 1

    match = if div(sum, cnt) == v, do: 1, else: 0
    {sum, cnt, lmatch + rmatch + match}
  end
end
```
