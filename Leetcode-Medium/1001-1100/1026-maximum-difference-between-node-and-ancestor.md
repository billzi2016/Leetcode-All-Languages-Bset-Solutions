# 1026. Maximum Difference Between Node and Ancestor

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
    int maxAncestorDiff(TreeNode* root) {
        if (!root) return 0;
        int ans = 0;
        dfs(root, root->val, root->val, ans);
        return ans;
    }
private:
    void dfs(TreeNode* node, int curMin, int curMax, int& ans) {
        if (!node) return;
        // update answer with current node
        ans = std::max(ans, std::max(std::abs(node->val - curMin), std::abs(node->val - curMax)));
        // update min and max for children
        int newMin = std::min(curMin, node->val);
        int newMax = std::max(curMax, node->val);
        if (node->left) dfs(node->left, newMin, newMax, ans);
        if (node->right) dfs(node->right, newMin, newMax, ans);
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
    private int maxDiff = 0;

    public int maxAncestorDiff(TreeNode root) {
        if (root == null) return 0;
        dfs(root, root.val, root.val);
        return maxDiff;
    }

    private void dfs(TreeNode node, int curMin, int curMax) {
        if (node == null) return;

        // Update the answer with current node's difference to min/max ancestors
        int diff1 = Math.abs(node.val - curMin);
        int diff2 = Math.abs(node.val - curMax);
        maxDiff = Math.max(maxDiff, Math.max(diff1, diff2));

        // Update path min and max for children
        int newMin = Math.min(curMin, node.val);
        int newMax = Math.max(curMax, node.val);

        if (node.left != null) dfs(node.left, newMin, newMax);
        if (node.right != null) dfs(node.right, newMin, newMax);
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
    def maxAncestorDiff(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        def dfs(node, cur_min, cur_max):
            # current difference with the path's min and max ancestors
            diff = max(abs(node.val - cur_min), abs(node.val - cur_max))
            # update min and max for children
            new_min = min(cur_min, node.val)
            new_max = max(cur_max, node.val)

            left_diff = dfs(node.left, new_min, new_max) if node.left else 0
            right_diff = dfs(node.right, new_min, new_max) if node.right else 0

            return max(diff, left_diff, right_diff)

        return dfs(root, root.val, root.val)
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
    def maxAncestorDiff(self, root: Optional['TreeNode']) -> int:
        if not root:
            return 0
        
        def dfs(node: 'TreeNode', cur_min: int, cur_max: int) -> int:
            # Update current path min and max with this node's value
            cur_min = min(cur_min, node.val)
            cur_max = max(cur_max, node.val)
            
            # If leaf, the difference for this path is cur_max - cur_min
            if not node.left and not node.right:
                return cur_max - cur_min
            
            left_diff = dfs(node.left, cur_min, cur_max) if node.left else 0
            right_diff = dfs(node.right, cur_min, cur_max) if node.right else 0
            return max(left_diff, right_diff)
        
        return dfs(root, root.val, root.val)
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
#include <stdlib.h>

static void dfs(struct TreeNode* node, int curMin, int curMax, int *ans) {
    if (!node) return;
    
    int diff1 = abs(node->val - curMin);
    int diff2 = abs(node->val - curMax);
    if (diff1 > *ans) *ans = diff1;
    if (diff2 > *ans) *ans = diff2;
    
    if (node->val < curMin) curMin = node->val;
    if (node->val > curMax) curMax = node->val;
    
    dfs(node->left, curMin, curMax, ans);
    dfs(node->right, curMin, curMax, ans);
}

int maxAncestorDiff(struct TreeNode* root) {
    if (!root) return 0;
    int ans = 0;
    dfs(root, root->val, root->val, &ans);
    return ans;
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
    private int maxDiff = 0;

    public int MaxAncestorDiff(TreeNode root) {
        if (root == null) return 0;
        Dfs(root, root.val, root.val);
        return maxDiff;
    }

    private void Dfs(TreeNode node, int curMin, int curMax) {
        if (node == null) return;

        // Update the maximum difference using current path extremes
        int diffMin = Math.Abs(node.val - curMin);
        int diffMax = Math.Abs(node.val - curMax);
        maxDiff = Math.Max(maxDiff, Math.Max(diffMin, diffMax));

        // Update path extremes for children
        int newMin = Math.Min(curMin, node.val);
        int newMax = Math.Max(curMax, node.val);

        Dfs(node.left, newMin, newMax);
        Dfs(node.right, newMin, newMax);
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
var maxAncestorDiff = function(root) {
    let maxDiff = 0;
    const dfs = (node, curMin, curMax) => {
        if (!node) return;
        maxDiff = Math.max(maxDiff, Math.abs(node.val - curMin), Math.abs(node.val - curMax));
        const newMin = Math.min(curMin, node.val);
        const newMax = Math.max(curMax, node.val);
        dfs(node.left, newMin, newMax);
        dfs(node.right, newMin, newMax);
    };
    dfs(root, root.val, root.val);
    return maxDiff;
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

function maxAncestorDiff(root: TreeNode | null): number {
    let answer = 0;
    const dfs = (node: TreeNode | null, curMin: number, curMax: number): void => {
        if (!node) return;
        // Update the global maximum difference using current path extremes
        answer = Math.max(
            answer,
            Math.abs(node.val - curMin),
            Math.abs(node.val - curMax)
        );
        const newMin = Math.min(curMin, node.val);
        const newMax = Math.max(curMax, node.val);
        dfs(node.left, newMin, newMax);
        dfs(node.right, newMin, newMax);
    };
    if (root) {
        dfs(root, root.val, root.val);
    }
    return answer;
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

    private $maxDiff = 0;

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function maxAncestorDiff($root) {
        if ($root === null) {
            return 0;
        }
        $this->dfs($root, $root->val, $root->val);
        return $this->maxDiff;
    }

    private function dfs($node, $curMin, $curMax) {
        if ($node === null) {
            return;
        }
        // Update the maximum difference using current min and max ancestors
        $diff1 = abs($node->val - $curMin);
        $diff2 = abs($node->val - $curMax);
        $this->maxDiff = max($this->maxDiff, $diff1, $diff2);

        // Update the path's min and max values
        $newMin = min($curMin, $node->val);
        $newMax = max($curMax, $node->val);

        if ($node->left !== null) {
            $this->dfs($node->left, $newMin, $newMax);
        }
        if ($node->right !== null) {
            $this->dfs($node->right, $newMin, $newMax);
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
    private var maxDiff = 0
    
    func maxAncestorDiff(_ root: TreeNode?) -> Int {
        guard let node = root else { return 0 }
        dfs(node, node.val, node.val)
        return maxDiff
    }
    
    private func dfs(_ node: TreeNode?, _ curMin: Int, _ curMax: Int) {
        guard let n = node else { return }
        
        // Update the maximum difference using current min and max from ancestors
        let diff1 = abs(n.val - curMin)
        let diff2 = abs(n.val - curMax)
        maxDiff = max(maxDiff, max(diff1, diff2))
        
        let newMin = min(curMin, n.val)
        let newMax = max(curMax, n.val)
        
        dfs(n.left, newMin, newMax)
        dfs(n.right, newMin, newMax)
    }
}
```

## Kotlin

```kotlin
import kotlin.math.abs

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
    private var maxDiff = 0

    fun maxAncestorDiff(root: TreeNode?): Int {
        if (root == null) return 0
        dfs(root, root.`val`, root.`val`)
        return maxDiff
    }

    private fun dfs(node: TreeNode?, curMin: Int, curMax: Int) {
        if (node == null) return
        val diff = maxOf(abs(node.`val` - curMin), abs(node.`val` - curMax))
        if (diff > maxDiff) maxDiff = diff

        val newMin = minOf(curMin, node.`val`)
        val newMax = maxOf(curMax, node.`val`)

        dfs(node.left, newMin, newMax)
        dfs(node.right, newMin, newMax)
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
  int maxAncestorDiff(TreeNode? root) {
    if (root == null) return 0;
    int ans = 0;

    void dfs(TreeNode? node, int curMin, int curMax) {
      if (node == null) return;
      ans = math.max(ans, math.max(curMax - node.val, node.val - curMin));
      int newMin = math.min(curMin, node.val);
      int newMax = math.max(curMax, node.val);
      dfs(node.left, newMin, newMax);
      dfs(node.right, newMin, newMax);
    }

    dfs(root, root.val, root.val);
    return ans;
  }
}
```

## Golang

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 */
var maxDiff int

func maxAncestorDiff(root *TreeNode) int {
	if root == nil {
		return 0
	}
	maxDiff = 0
	dfs(root, root.Val, root.Val)
	return maxDiff
}

func dfs(node *TreeNode, curMin, curMax int) {
	if node == nil {
		return
	}
	if d := abs(node.Val - curMin); d > maxDiff {
		maxDiff = d
	}
	if d := abs(node.Val - curMax); d > maxDiff {
		maxDiff = d
	}
	newMin, newMax := curMin, curMax
	if node.Val < newMin {
		newMin = node.Val
	}
	if node.Val > newMax {
		newMax = node.Val
	}
	dfs(node.Left, newMin, newMax)
	dfs(node.Right, newMin, newMax)
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

def max_ancestor_diff(root)
  return 0 unless root
  ans = 0
  stack = [[root, root.val, root.val]]
  until stack.empty?
    node, cur_min, cur_max = stack.pop
    diff = [(cur_max - node.val).abs, (node.val - cur_min).abs].max
    ans = [ans, diff].max
    new_min = [cur_min, node.val].min
    new_max = [cur_max, node.val].max
    stack << [node.left, new_min, new_max] if node.left
    stack << [node.right, new_min, new_max] if node.right
  end
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
  def maxAncestorDiff(root: TreeNode): Int = {
    var answer = 0

    def dfs(node: TreeNode, curMin: Int, curMax: Int): Unit = {
      if (node == null) return
      // compute difference with current path extremes
      val diffLow  = Math.abs(node.value - curMin)
      val diffHigh = Math.abs(node.value - curMax)
      answer = math.max(answer, math.max(diffLow, diffHigh))

      val newMin = math.min(curMin, node.value)
      val newMax = math.max(curMax, node.value)

      dfs(node.left, newMin, newMax)
      dfs(node.right, newMin, newMax)
    }

    dfs(root, root.value, root.value)
    answer
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn max_ancestor_diff(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, cur_min: i32, cur_max: i32) -> i32 {
            if let Some(rc_node) = node {
                let val = rc_node.borrow().val;
                let diff1 = (cur_max - val).abs();
                let diff2 = (cur_min - val).abs();
                let new_min = cur_min.min(val);
                let new_max = cur_max.max(val);
                let left = dfs(&rc_node.borrow().left, new_min, new_max);
                let right = dfs(&rc_node.borrow().right, new_min, new_max);
                *[diff1, diff2, left, right].iter().max().unwrap()
            } else {
                0
            }
        }

        if let Some(rc_root) = &root {
            let val = rc_root.borrow().val;
            dfs(&root, val, val)
        } else {
            0
        }
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

(define/contract (max-ancestor-diff root)
  (-> (or/c tree-node? #f) exact-integer?)
  (let ([ans (box 0)])
    (define (dfs node)
      (if (not node)
          (values +inf.0 -inf.0)               ; sentinel for empty subtree
          (let-values ([(lmin lmax) (dfs (tree-node-left node))]
                       [(rmin rmax) (dfs (tree-node-right node))])
            (define cur (tree-node-val node))
            (define child-min (min lmin rmin))
            (define child-max (max lmax rmax))
            (when (< child-min +inf.0)           ; there exists at least one descendant
              (let ([diff1 (abs (- cur child-min))]
                    [diff2 (abs (- cur child-max))])
                (for ([d (list diff1 diff2)])
                  (when (> d (unbox ans))
                    (set-box! ans d)))))
            (values (min cur child-min) (max cur child-max)))))
    (if (not root)
        0
        (begin
          (dfs root)
          (unbox ans)))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-export([max_ancestor_diff/1]).

-spec max_ancestor_diff(Root :: #tree_node{} | null) -> integer().
max_ancestor_diff(null) ->
    0;
max_ancestor_diff(#tree_node{val = V} = Root) ->
    helper(Root, V, V).

-spec helper(Node :: #tree_node{} | null, MinSoFar :: integer(), MaxSoFar :: integer()) -> integer().
helper(null, _Min, _Max) ->
    0;
helper(#tree_node{val = V, left = L, right = R}, CurMin, CurMax) ->
    Diff1 = abs(V - CurMin),
    Diff2 = abs(V - CurMax),
    CurrDiff = max(Diff1, Diff2),
    NewMin = min(CurMin, V),
    NewMax = max(CurMax, V),
    LeftDiff = helper(L, NewMin, NewMax),
    RightDiff = helper(R, NewMin, NewMax),
    SubMax = max(LeftDiff, RightDiff),
    max(CurrDiff, SubMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_ancestor_diff(root :: TreeNode.t | nil) :: integer
  def max_ancestor_diff(nil), do: 0

  def max_ancestor_diff(%TreeNode{val: v} = root) do
    traverse(root, v, v)
  end

  defp traverse(nil, _min, _max), do: 0

  defp traverse(%TreeNode{val: val, left: left, right: right}, cur_min, cur_max) do
    diff = max(abs(val - cur_min), abs(val - cur_max))
    new_min = min(cur_min, val)
    new_max = max(cur_max, val)

    left_diff = traverse(left, new_min, new_max)
    right_diff = traverse(right, new_min, new_max)

    Enum.max([diff, left_diff, right_diff])
  end
end
```
