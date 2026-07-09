# 1372. Longest ZigZag Path in a Binary Tree

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
    int longestZigZag(TreeNode* root) {
        ans = 0;
        dfs(root);
        return ans;
    }
private:
    int ans;
    // returns {len starting by moving left, len starting by moving right}
    std::pair<int,int> dfs(TreeNode* node){
        if (!node) return {-1, -1}; // so that leaf children give 0 when +1
        auto left = dfs(node->left);
        auto right = dfs(node->right);
        int leftStart = 1 + left.second;   // go left then need right from child
        int rightStart = 1 + right.first;  // go right then need left from child
        ans = std::max({ans, leftStart, rightStart});
        return {leftStart, rightStart};
    }
};
```

## Java

```java
class Solution {
    private int maxLen = 0;
    
    public int longestZigZag(TreeNode root) {
        dfs(root);
        return maxLen;
    }
    
    // returns int[2] where:
    // [0] = length of longest ZigZag starting by moving left from this node
    // [1] = length of longest ZigZag starting by moving right from this node
    private int[] dfs(TreeNode node) {
        if (node == null) {
            return new int[]{-1, -1}; // so that leaf nodes yield length 0
        }
        int[] left = dfs(node.left);
        int[] right = dfs(node.right);
        
        int leftLen = 1 + left[1];   // move left then must go right
        int rightLen = 1 + right[0]; // move right then must go left
        
        maxLen = Math.max(maxLen, Math.max(leftLen, rightLen));
        return new int[]{leftLen, rightLen};
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
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = 0

        def dfs(node):
            if not node:
                # return lengths for left and right moves as -1 so that leaf nodes get length 0
                return (-1, -1)
            left_left, left_right = dfs(node.left)
            right_left, right_right = dfs(node.right)

            # If we move to the left child, next must be a right move
            left_len = 1 + left_right
            # If we move to the right child, next must be a left move
            right_len = 1 + right_left

            self.ans = max(self.ans, left_len, right_len)
            return (left_len, right_len)

        dfs(root)
        return self.ans
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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        import sys
        sys.setrecursionlimit(1000000)
        self.ans = 0

        def dfs(node):
            if not node:
                # return lengths for null nodes so that leaf calculations yield 0
                return (-1, -1)   # (left_start, right_start)
            left_len_pair = dfs(node.left)
            right_len_pair = dfs(node.right)

            # start by moving left: need right-start length from left child
            left_start = 1 + left_len_pair[1]
            # start by moving right: need left-start length from right child
            right_start = 1 + right_len_pair[0]

            self.ans = max(self.ans, left_start, right_start)
            return (left_start, right_start)

        dfs(root)
        return self.ans
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

static int maxLen;

struct Pair {
    int left;   // length when the next move is to the left
    int right;  // length when the next move is to the right
};

static struct Pair dfs(struct TreeNode* node) {
    struct Pair res = {-1, -1};
    if (!node) return res;
    
    struct Pair l = dfs(node->left);
    struct Pair r = dfs(node->right);
    
    int leftZig  = 1 + l.right;   // go left then need right next
    int rightZig = 1 + r.left;    // go right then need left next
    
    if (leftZig > maxLen)  maxLen = leftZig;
    if (rightZig > maxLen) maxLen = rightZig;
    
    res.left  = leftZig;
    res.right = rightZig;
    return res;
}

int longestZigZag(struct TreeNode* root) {
    maxLen = 0;
    dfs(root);
    return maxLen;
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
    private int maxLen = 0;

    public int LongestZigZag(TreeNode root) {
        Dfs(root);
        return maxLen;
    }

    // Returns (lenIfGoLeft, lenIfGoRight)
    private (int left, int right) Dfs(TreeNode node) {
        if (node == null) {
            // -1 so that leaf nodes get length 0 when adding 1
            return (-1, -1);
        }

        var leftChild = Dfs(node.left);
        var rightChild = Dfs(node.right);

        int goLeft = 1 + leftChild.right;   // edge to left child then continue right
        int goRight = 1 + rightChild.left;  // edge to right child then continue left

        maxLen = System.Math.Max(maxLen, System.Math.Max(goLeft, goRight));

        return (goLeft, goRight);
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
var longestZigZag = function(root) {
    let maxLen = 0;
    
    const dfs = (node) => {
        if (!node) return { left: 0, right: 0 };
        
        const leftInfo = dfs(node.left);
        const rightInfo = dfs(node.right);
        
        // start by moving to the left child
        const leftLen = node.left ? 1 + leftInfo.right : 0;
        // start by moving to the right child
        const rightLen = node.right ? 1 + rightInfo.left : 0;
        
        maxLen = Math.max(maxLen, leftLen, rightLen);
        
        return { left: leftLen, right: rightLen };
    };
    
    dfs(root);
    return maxLen;
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

function longestZigZag(root: TreeNode | null): number {
    let ans = 0;
    const dfs = (node: TreeNode | null): [number, number] => {
        if (!node) return [-1, -1];
        const left = dfs(node.left);
        const right = dfs(node.right);
        const leftStart = 1 + left[1];   // go left then need to go right
        const rightStart = 1 + right[0]; // go right then need to go left
        ans = Math.max(ans, leftStart, rightStart);
        return [leftStart, rightStart];
    };
    dfs(root);
    return ans;
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
    private int $maxLen = 0;

    /**
     * @param TreeNode|null $root
     * @return int
     */
    function longestZigZag($root) {
        $this->dfs($root);
        return $this->maxLen;
    }

    /**
     * @param TreeNode|null $node
     * @return array<int,int> [leftStart, rightStart]
     */
    private function dfs($node): array {
        if ($node === null) {
            // Return -1 so that leaf nodes produce length 0 after adding 1.
            return [-1, -1];
        }

        $leftChild = $this->dfs($node->left);
        $rightChild = $this->dfs($node->right);

        // If we go left first, next must be right from the left child.
        $goLeft = $leftChild[1] + 1;
        // If we go right first, next must be left from the right child.
        $goRight = $rightChild[0] + 1;

        $this->maxLen = max($this->maxLen, $goLeft, $goRight);

        return [$goLeft, $goRight];
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
    func longestZigZag(_ root: TreeNode?) -> Int {
        var maxLen = 0
        
        func dfs(_ node: TreeNode?) -> (Int, Int) {
            guard let n = node else { return (-1, -1) } // base case
            
            let leftVals = dfs(n.left)
            let rightVals = dfs(n.right)
            
            // length when the first move is to the left
            let leftStart = 1 + leftVals.1
            // length when the first move is to the right
            let rightStart = 1 + rightVals.0
            
            maxLen = max(maxLen, max(leftStart, rightStart))
            
            return (leftStart, rightStart)
        }
        
        _ = dfs(root)
        return maxLen
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
    private var maxLen = 0

    fun longestZigZag(root: TreeNode?): Int {
        dfs(root)
        return maxLen
    }

    private fun dfs(node: TreeNode?): Pair<Int, Int> {
        if (node == null) return Pair(0, 0)

        val left = dfs(node.left)
        val right = dfs(node.right)

        // start by going left from this node
        val leftZig = if (node.left != null) 1 + left.second else 0
        // start by going right from this node
        val rightZig = if (node.right != null) 1 + right.first else 0

        maxLen = maxOf(maxLen, leftZig, rightZig)

        return Pair(leftZig, rightZig)
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
  int _maxLen = 0;

  List<int> _dfs(TreeNode? node) {
    if (node == null) return [0, 0]; // [leftStart, rightStart]

    final leftChild = _dfs(node.left);
    final rightChild = _dfs(node.right);

    int leftStart = 0;
    if (node.left != null) {
      // move to left child, next must go right
      leftStart = 1 + leftChild[1];
    }

    int rightStart = 0;
    if (node.right != null) {
      // move to right child, next must go left
      rightStart = 1 + rightChild[0];
    }

    if (leftStart > _maxLen) _maxLen = leftStart;
    if (rightStart > _maxLen) _maxLen = rightStart;

    return [leftStart, rightStart];
  }

  int longestZigZag(TreeNode? root) {
    _maxLen = 0;
    _dfs(root);
    return _maxLen;
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
func longestZigZag(root *TreeNode) int {
	var maxLen int

	var dfs func(node *TreeNode) (int, int)
	dfs = func(node *TreeNode) (int, int) {
		if node == nil {
			return -1, -1 // base: child of leaf contributes -1 so leaf gets 0 length
		}
		leftL, leftR := dfs(node.Left)
		rightL, rightR := dfs(node.Right)

		curLeft := 1 + leftR   // start by going left, next must go right
		curRight := 1 + rightL // start by going right, next must go left

		if curLeft > maxLen {
			maxLen = curLeft
		}
		if curRight > maxLen {
			maxLen = curRight
		}
		return curLeft, curRight
	}

	dfs(root)
	return maxLen
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

def longest_zig_zag(root)
  max_len = 0
  dfs = lambda do |node|
    return [-1, -1] if node.nil?
    left = dfs.call(node.left)
    right = dfs.call(node.right)

    cur_left = left[1] + 1   # go left now, next must go right
    cur_right = right[0] + 1 # go right now, next must go left

    max_len = [max_len, cur_left, cur_right].max
    [cur_left, cur_right]
  end

  dfs.call(root)
  max_len
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
  private var maxLen = 0

  def longestZigZag(root: TreeNode): Int = {
    def dfs(node: TreeNode): (Int, Int) = {
      if (node == null) return (-1, -1)
      val left = dfs(node.left)
      val right = dfs(node.right)

      // length when taking a step to the left then alternating
      val leftLen = 1 + left._2
      // length when taking a step to the right then alternating
      val rightLen = 1 + right._1

      maxLen = math.max(maxLen, math.max(leftLen, rightLen))
      (leftLen, rightLen)
    }

    dfs(root)
    maxLen
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn longest_zig_zag(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, ans: &mut i32) -> (i32, i32) {
            if let Some(rc_node) = node {
                let left_child = rc_node.borrow().left.clone();
                let right_child = rc_node.borrow().right.clone();

                let (ll, lr) = dfs(left_child, ans);
                let (rl, rr) = dfs(right_child, ans);

                let left_len = if rc_node.borrow().left.is_some() { 1 + lr } else { 0 };
                let right_len = if rc_node.borrow().right.is_some() { 1 + rl } else { 0 };

                *ans = (*ans).max(left_len).max(right_len);
                (left_len, right_len)
            } else {
                (0, 0)
            }
        }

        let mut result = 0;
        dfs(root, &mut result);
        result
    }
}
```

## Racket

```racket
(struct tree-node (val left right) #:mutable #:transparent)

(define (make-tree-node [val 0])
  (tree-node val #f #f))

(define/contract (longest-zig-zag root)
  (-> (or/c tree-node? #f) exact-integer?)
  (let ((ans 0))
    (define (dfs node)
      (if (not node)
          (list 0 0)
          (let* ((left (tree-node-left node))
                 (right (tree-node-right node))
                 (lp (dfs left))
                 (rp (dfs right))
                 (left-zig (if left (+ 1 (second lp)) 0))
                 (right-zig (if right (+ 1 (first rp)) 0)))
            (set! ans (max ans left-zig right-zig))
            (list left-zig right-zig))))
    (dfs root)
    ans))
```

## Erlang

```erlang
-module(solution).
-export([longest_zig_zag/1]).

%% Definition for a binary tree node.
-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec longest_zig_zag(Root :: #tree_node{} | null) -> integer().
longest_zig_zag(Root) ->
    {_L, _R, Ans} = dfs(Root),
    Ans.

-spec dfs(#tree_node{} | null) -> {integer(), integer(), integer()}.
dfs(null) ->
    {-1, -1, 0};
dfs(Node) ->
    Left = Node#tree_node.left,
    Right = Node#tree_node.right,
    {LL, LR, LMax} = dfs(Left),
    {RL, RR, RMax} = dfs(Right),
    LeftZig = 1 + LR,
    RightZig = 1 + RL,
    MaxHere = erlang:max(LeftZig, RightZig),
    MaxOverall = erlang:max(MaxHere, erlang:max(LMax, RMax)),
    {LeftZig, RightZig, MaxOverall}.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_zig_zag(root :: TreeNode.t | nil) :: integer
  def longest_zig_zag(root) do
    {_left, _right, ans} = dfs(root)
    ans
  end

  defp dfs(nil), do: {0, 0, 0}

  defp dfs(%TreeNode{left: left, right: right}) do
    {l_left, l_right, l_max} = dfs(left)
    {r_left, r_right, r_max} = dfs(right)

    left_zig = if left != nil, do: 1 + l_right, else: 0
    right_zig = if right != nil, do: 1 + r_left, else: 0

    cur_max = Enum.max([left_zig, right_zig, l_max, r_max])
    {left_zig, right_zig, cur_max}
  end
end
```
