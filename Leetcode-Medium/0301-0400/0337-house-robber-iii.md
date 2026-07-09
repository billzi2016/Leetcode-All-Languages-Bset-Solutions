# 0337. House Robber III

## Cpp

```cpp
/ **
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
    // returns {rob_this_node, not_rob_this_node}
    std::pair<long long,long long> dfs(TreeNode* node){
        if (!node) return {0,0};
        auto left = dfs(node->left);
        auto right = dfs(node->right);
        long long rob = node->val + left.second + right.second;
        long long notRob = std::max(left.first, left.second) + std::max(right.first, right.second);
        return {rob, notRob};
    }
    
    int rob(TreeNode* root) {
        auto res = dfs(root);
        return static_cast<int>(std::max(res.first, res.second));
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
    public int rob(TreeNode root) {
        long[] res = dfs(root);
        return (int)Math.max(res[0], res[1]);
    }

    // returns [robCurrent, notRobCurrent]
    private long[] dfs(TreeNode node) {
        if (node == null) {
            return new long[]{0L, 0L};
        }
        long[] left = dfs(node.left);
        long[] right = dfs(node.right);

        long rob = node.val + left[1] + right[1];
        long notRob = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);

        return new long[]{rob, notRob};
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
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node):
            if not node:
                return (0, 0)  # (rob, not_rob)
            left = dfs(node.left)
            right = dfs(node.right)

            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            return (rob, not_rob)

        return max(dfs(root))
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
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node):
            if not node:
                return (0, 0)  # (rob, not_rob)
            left = dfs(node.left)
            right = dfs(node.right)
            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            return (rob, not_rob)

        return max(dfs(root))
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
#include <stddef.h>

typedef struct {
    long long rob;
    long long notRob;
} Result;

static Result dfs(struct TreeNode* node) {
    if (node == NULL) {
        return (Result){0, 0};
    }
    Result left = dfs(node->left);
    Result right = dfs(node->right);
    
    Result cur;
    cur.rob = (long long)node->val + left.notRob + right.notRob;
    cur.notRob = (left.rob > left.notRob ? left.rob : left.notRob) +
                (right.rob > right.notRob ? right.rob : right.notRob);
    return cur;
}

int rob(struct TreeNode* root) {
    Result ans = dfs(root);
    long long best = ans.rob > ans.notRob ? ans.rob : ans.notRob;
    return (int)best;
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
    public int Rob(TreeNode root)
    {
        var result = Dfs(root);
        return Math.Max(result.notRob, result.rob);
    }

    private (int notRob, int rob) Dfs(TreeNode node)
    {
        if (node == null)
            return (0, 0);

        var left = Dfs(node.left);
        var right = Dfs(node.right);

        int rob = node.val + left.notRob + right.notRob;
        int notRob = Math.Max(left.notRob, left.rob) + Math.Max(right.notRob, right.rob);

        return (notRob, rob);
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
var rob = function(root) {
    const dfs = (node) => {
        if (!node) return [0, 0];
        const left = dfs(node.left);
        const right = dfs(node.right);
        const include = node.val + left[1] + right[1];
        const exclude = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        return [include, exclude];
    };
    const result = dfs(root);
    return Math.max(result[0], result[1]);
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

function rob(root: TreeNode | null): number {
    const dfs = (node: TreeNode | null): [number, number] => {
        if (!node) return [0, 0];
        const left = dfs(node.left);
        const right = dfs(node.right);
        const notRob = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        const robNode = node.val + left[0] + right[0];
        return [notRob, robNode];
    };
    const result = dfs(root);
    return Math.max(result[0], result[1]);
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
    function rob($root) {
        $res = $this->dfs($root);
        return max($res[0], $res[1]);
    }

    private function dfs($node) {
        if ($node === null) {
            return [0, 0];
        }
        $left = $this->dfs($node->left);
        $right = $this->dfs($node->right);

        // If we rob this node, we cannot rob its children
        $rob = $node->val + $left[1] + $right[1];

        // If we don't rob this node, we can choose to rob or not rob each child
        $notRob = max($left[0], $left[1]) + max($right[0], $right[1]);

        return [$rob, $notRob];
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
    func rob(_ root: TreeNode?) -> Int {
        let result = dfs(root)
        return max(result.0, result.1)
    }

    private func dfs(_ node: TreeNode?) -> (Int, Int) {
        guard let n = node else { return (0, 0) }
        let left = dfs(n.left)
        let right = dfs(n.right)

        // If we rob this node, we cannot rob its children
        let robCurrent = n.val + left.1 + right.1
        // If we don't rob this node, we can choose to rob or not rob each child independently
        let skipCurrent = max(left.0, left.1) + max(right.0, right.1)

        return (robCurrent, skipCurrent)
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
    fun rob(root: TreeNode?): Int {
        val (rob, notRob) = dfs(root)
        return maxOf(rob, notRob).toInt()
    }

    private fun dfs(node: TreeNode?): Pair<Long, Long> {
        if (node == null) return Pair(0L, 0L)

        val left = dfs(node.left)
        val right = dfs(node.right)

        // If we rob this node, we cannot rob its children
        val rob = node.`val`.toLong() + left.second + right.second

        // If we don't rob this node, we can choose to rob or not rob each child independently
        val notRob = maxOf(left.first, left.second) + maxOf(right.first, right.second)

        return Pair(rob, notRob)
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
  int rob(TreeNode? root) {
    List<int> dfs(TreeNode? node) {
      if (node == null) return [0, 0];
      final left = dfs(node.left);
      final right = dfs(node.right);
      final robCurrent = node.val + left[1] + right[1];
      final notRobCurrent = (left[0] > left[1] ? left[0] : left[1]) +
          (right[0] > right[1] ? right[0] : right[1]);
      return [robCurrent, notRobCurrent];
    }

    final result = dfs(root);
    return result[0] > result[1] ? result[0] : result[1];
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
func rob(root *TreeNode) int {
    notRob, robVal := dfs(root)
    if notRob > robVal {
        return notRob
    }
    return robVal
}

func dfs(node *TreeNode) (int, int) {
    if node == nil {
        return 0, 0
    }
    leftNot, leftRob := dfs(node.Left)
    rightNot, rightRob := dfs(node.Right)

    rob := node.Val + leftNot + rightNot
    notRob := max(leftNot, leftRob) + max(rightNot, rightRob)
    return notRob, rob
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

## Ruby

```ruby
def rob(root)
  return 0 unless root
  dp = {}
  stack = [[root, false]]
  until stack.empty?
    node, visited = stack.pop
    next if node.nil?
    if visited
      left = dp[node.left] || [0, 0]
      right = dp[node.right] || [0, 0]
      rob_val = node.val + left[1] + right[1]
      not_rob_val = [left[0], left[1]].max + [right[0], right[1]].max
      dp[node] = [rob_val, not_rob_val]
    else
      stack << [node, true]
      stack << [node.right, false] if node.right
      stack << [node.left, false] if node.left
    end
  end
  dp[root].max
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
    def rob(root: TreeNode): Int = {
        def dfs(node: TreeNode): (Int, Int) = {
            if (node == null) return (0, 0)
            val left = dfs(node.left)
            val right = dfs(node.right)
            val robThis = node.value + left._2 + right._2
            val notRobThis = math.max(left._1, left._2) + math.max(right._1, right._2)
            (robThis, notRobThis)
        }
        val result = dfs(root)
        math.max(result._1, result._2)
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn rob(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>) -> (i32, i32) {
            match node {
                None => (0, 0),
                Some(rc_node) => {
                    let left = rc_node.borrow().left.clone();
                    let right = rc_node.borrow().right.clone();
                    let (l_rob, l_not) = dfs(left);
                    let (r_rob, r_not) = dfs(right);
                    let rob = rc_node.borrow().val + l_not + r_not;
                    let not_rob = std::cmp::max(l_rob, l_not) + std::cmp::max(r_rob, r_not);
                    (rob, not_rob)
                }
            }
        }
        let (rob_root, not_rob_root) = dfs(root);
        rob_root.max(not_rob_root)
    }
}
```

## Racket

```racket
(define/contract (rob root)
  (-> (or/c tree-node? #f) exact-integer?)
  (letrec ((dfs (lambda (node)
                  (if (not node)
                      (values 0 0)
                      (let-values ([(l-rob l-not) (dfs (tree-node-left node))]
                                   [(r-rob r-not) (dfs (tree-node-right node))])
                        (define rob (+ (tree-node-val node) l-not r-not))
                        (define not-rob (+ (max l-rob l-not)
                                           (max r-rob r-not)))
                        (values rob not-rob))))))
    (let-values ([(r n) (dfs root)])
      (max r n))))
```

## Erlang

```erlang
-module(solution).
-export([rob/1]).

-record(tree_node, {
    val   = 0 :: integer(),
    left  = null :: 'null' | #tree_node{},
    right = null :: 'null' | #tree_node{}
}).

-spec rob(Root :: #tree_node{} | null) -> integer().
rob(Root) ->
    {Rob, NotRob} = dfs(Root),
    erlang:max(Rob, NotRob).

dfs(null) ->
    {0, 0};
dfs(#tree_node{val = V, left = L, right = R}) ->
    {LRob, LNot} = dfs(L),
    {RRob, RNot} = dfs(R),
    Rob = V + LNot + RNot,
    NotRob = erlang:max(LRob, LNot) + erlang:max(RRob, RNot),
    {Rob, NotRob}.
```

## Elixir

```elixir
defmodule Solution do
  @spec rob(root :: TreeNode.t | nil) :: integer
  def rob(root) do
    {rob_root, not_rob_root} = dfs(root)
    max(rob_root, not_rob_root)
  end

  defp dfs(nil), do: {0, 0}

  defp dfs(%TreeNode{val: v, left: l, right: r}) do
    {l_rob, l_not} = dfs(l)
    {r_rob, r_not} = dfs(r)

    rob = v + l_not + r_not
    not_rob = max(l_rob, l_not) + max(r_rob, r_not)
    {rob, not_rob}
  end
end
```
