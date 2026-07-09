# 0687. Longest Univalue Path

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
    int longestUnivaluePath(TreeNode* root) {
        ans = 0;
        dfs(root);
        return ans;
    }
private:
    int ans;
    int dfs(TreeNode* node) {
        if (!node) return 0;
        int leftLen = dfs(node->left);
        int rightLen = dfs(node->right);
        int leftPath = 0, rightPath = 0;
        if (node->left && node->left->val == node->val) {
            leftPath = leftLen + 1;
        }
        if (node->right && node->right->val == node->val) {
            rightPath = rightLen + 1;
        }
        ans = std::max(ans, leftPath + rightPath);
        return std::max(leftPath, rightPath);
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
    private int maxLen = 0;

    public int longestUnivaluePath(TreeNode root) {
        dfs(root);
        return maxLen;
    }

    private int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int left = dfs(node.left);
        int right = dfs(node.right);

        int leftPath = 0, rightPath = 0;
        if (node.left != null && node.left.val == node.val) {
            leftPath = left + 1;
        }
        if (node.right != null && node.right.val == node.val) {
            rightPath = right + 1;
        }

        maxLen = Math.max(maxLen, leftPath + rightPath);
        return Math.max(leftPath, rightPath);
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
    def longestUnivaluePath(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_len = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            left_path = right_path = 0
            if node.left and node.left.val == node.val:
                left_path = left + 1
            if node.right and node.right.val == node.val:
                right_path = right + 1

            self.max_len = max(self.max_len, left_path + right_path)
            return max(left_path, right_path)

        dfs(root)
        return self.max_len
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
    def longestUnivaluePath(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            left_len = dfs(node.left)
            right_len = dfs(node.right)

            left_path = right_path = 0
            if node.left and node.left.val == node.val:
                left_path = left_len + 1
            if node.right and node.right.val == node.val:
                right_path = right_len + 1

            self.ans = max(self.ans, left_path + right_path)
            return max(left_path, right_path)

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

int dfs(struct TreeNode* node) {
    if (!node) return 0;
    int left = dfs(node->left);
    int right = dfs(node->right);
    
    int leftPath = 0, rightPath = 0;
    if (node->left && node->left->val == node->val)
        leftPath = left + 1;
    if (node->right && node->right->val == node->val)
        rightPath = right + 1;
    
    int total = leftPath + rightPath;
    if (total > maxLen) maxLen = total;
    
    return leftPath > rightPath ? leftPath : rightPath;
}

int longestUnivaluePath(struct TreeNode* root) {
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
public class Solution
{
    private int _maxLen;

    public int LongestUnivaluePath(TreeNode root)
    {
        _maxLen = 0;
        Dfs(root);
        return _maxLen;
    }

    private int Dfs(TreeNode node)
    {
        if (node == null) return 0;

        int left = Dfs(node.left);
        int right = Dfs(node.right);

        int leftPath = 0, rightPath = 0;

        if (node.left != null && node.left.val == node.val)
            leftPath = left + 1;
        if (node.right != null && node.right.val == node.val)
            rightPath = right + 1;

        _maxLen = Math.Max(_maxLen, leftPath + rightPath);

        return Math.Max(leftPath, rightPath);
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
var longestUnivaluePath = function(root) {
    let maxLen = 0;
    
    const dfs = (node) => {
        if (!node) return 0;
        const left = dfs(node.left);
        const right = dfs(node.right);
        
        let leftPath = 0, rightPath = 0;
        if (node.left && node.left.val === node.val) {
            leftPath = left + 1;
        }
        if (node.right && node.right.val === node.val) {
            rightPath = right + 1;
        }
        
        maxLen = Math.max(maxLen, leftPath + rightPath);
        return Math.max(leftPath, rightPath);
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

function longestUnivaluePath(root: TreeNode | null): number {
    let maxLen = 0;

    const dfs = (node: TreeNode | null): number => {
        if (!node) return 0;
        const left = dfs(node.left);
        const right = dfs(node.right);

        let leftPath = 0, rightPath = 0;
        if (node.left && node.left.val === node.val) {
            leftPath = left + 1;
        }
        if (node.right && node.right.val === node.val) {
            rightPath = right + 1;
        }

        maxLen = Math.max(maxLen, leftPath + rightPath);
        return Math.max(leftPath, rightPath);
    };

    dfs(root);
    return maxLen;
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
    private int $maxPath = 0;

    /**
     * @param TreeNode|null $root
     * @return int
     */
    function longestUnivaluePath($root) {
        $this->maxPath = 0;
        $this->dfs($root);
        return $this->maxPath;
    }

    private function dfs(?TreeNode $node): int {
        if ($node === null) {
            return 0;
        }
        $leftLen = $this->dfs($node->left);
        $rightLen = $this->dfs($node->right);

        $leftPath = 0;
        $rightPath = 0;

        if ($node->left !== null && $node->left->val === $node->val) {
            $leftPath = $leftLen + 1;
        }
        if ($node->right !== null && $node->right->val === $node->val) {
            $rightPath = $rightLen + 1;
        }

        // Update the global maximum with the sum of paths through this node
        $this->maxPath = max($this->maxPath, $leftPath + $rightPath);

        // Return the longer one to parent
        return max($leftPath, $rightPath);
    }
}
?>
```

## Swift

```swift
class Solution {
    private var maxLen = 0
    
    func longestUnivaluePath(_ root: TreeNode?) -> Int {
        dfs(root)
        return maxLen
    }
    
    private func dfs(_ node: TreeNode?) -> Int {
        guard let n = node else { return 0 }
        let left = dfs(n.left)
        let right = dfs(n.right)
        
        var leftPath = 0
        var rightPath = 0
        
        if let l = n.left, l.val == n.val {
            leftPath = left + 1
        }
        if let r = n.right, r.val == n.val {
            rightPath = right + 1
        }
        
        maxLen = max(maxLen, leftPath + rightPath)
        return max(leftPath, rightPath)
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
    private var ans = 0

    fun longestUnivaluePath(root: TreeNode?): Int {
        dfs(root)
        return ans
    }

    private fun dfs(node: TreeNode?): Int {
        if (node == null) return 0
        val leftLen = dfs(node.left)
        val rightLen = dfs(node.right)

        var leftPath = 0
        var rightPath = 0

        if (node.left != null && node.left!!.`val` == node.`val`) {
            leftPath = leftLen + 1
        }
        if (node.right != null && node.right!!.`val` == node.`val`) {
            rightPath = rightLen + 1
        }

        ans = maxOf(ans, leftPath + rightPath)
        return maxOf(leftPath, rightPath)
    }
}
```

## Dart

```dart
import 'dart:math';

class TreeNode {
  int val;
  TreeNode? left;
  TreeNode? right;
  TreeNode([this.val = 0, this.left, this.right]);
}

class Solution {
  int _max = 0;

  int longestUnivaluePath(TreeNode? root) {
    _dfs(root);
    return _max;
  }

  int _dfs(TreeNode? node) {
    if (node == null) return 0;

    int leftLen = _dfs(node.left);
    int rightLen = _dfs(node.right);

    int leftPath = 0, rightPath = 0;

    if (node.left != null && node.left!.val == node.val) {
      leftPath = leftLen + 1;
    }
    if (node.right != null && node.right!.val == node.val) {
      rightPath = rightLen + 1;
    }

    _max = max(_max, leftPath + rightPath);
    return max(leftPath, rightPath);
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
func longestUnivaluePath(root *TreeNode) int {
	var ans int
	var dfs func(*TreeNode) int

	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		left := dfs(node.Left)
		right := dfs(node.Right)

		leftPath, rightPath := 0, 0
		if node.Left != nil && node.Left.Val == node.Val {
			leftPath = left + 1
		}
		if node.Right != nil && node.Right.Val == node.Val {
			rightPath = right + 1
		}

		if leftPath+rightPath > ans {
			ans = leftPath + rightPath
		}
		if leftPath > rightPath {
			return leftPath
		}
		return rightPath
	}

	dfs(root)
	return ans
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

def longest_univalue_path(root)
  max_len = 0
  dfs = nil
  dfs = ->(node) {
    return 0 unless node
    left = dfs.call(node.left)
    right = dfs.call(node.right)

    left_path = (node.left && node.left.val == node.val) ? left + 1 : 0
    right_path = (node.right && node.right.val == node.val) ? right + 1 : 0

    max_len = [max_len, left_path + right_path].max
    [left_path, right_path].max
  }
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
  def longestUnivaluePath(root: TreeNode): Int = {
    var ans = 0

    def dfs(node: TreeNode): Int = {
      if (node == null) return 0
      val leftLen = dfs(node.left)
      val rightLen = dfs(node.right)

      var leftPath = 0
      var rightPath = 0

      if (node.left != null && node.left.value == node.value) {
        leftPath = leftLen + 1
      }
      if (node.right != null && node.right.value == node.value) {
        rightPath = rightLen + 1
      }

      ans = math.max(ans, leftPath + rightPath)
      math.max(leftPath, rightPath)
    }

    dfs(root)
    ans
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn longest_univalue_path(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, ans: &mut i32) -> i32 {
            if let Some(rc_node) = node {
                let left_child = rc_node.borrow().left.clone();
                let right_child = rc_node.borrow().right.clone();

                let left_len = dfs(left_child.clone(), ans);
                let right_len = dfs(right_child.clone(), ans);

                let mut left_path = 0;
                let mut right_path = 0;

                if let Some(lc) = left_child {
                    if lc.borrow().val == rc_node.borrow().val {
                        left_path = left_len + 1;
                    }
                }

                if let Some(rc) = right_child {
                    if rc.borrow().val == rc_node.borrow().val {
                        right_path = right_len + 1;
                    }
                }

                *ans = (*ans).max(left_path + right_path);
                std::cmp::max(left_path, right_path)
            } else {
                0
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
(define/contract (longest-univalue-path root)
  (-> (or/c tree-node? #f) exact-integer?)
  (let ((ans 0))
    (define (dfs node)
      (if (not node)
          0
          (let* ((left-arm  (dfs (tree-node-left node)))
                 (right-arm (dfs (tree-node-right node)))
                 (left-path 0)
                 (right-path 0))
            (when (and (tree-node-left node)
                       (= (tree-node-val (tree-node-left node)) (tree-node-val node)))
              (set! left-path (+ left-arm 1)))
            (when (and (tree-node-right node)
                       (= (tree-node-val (tree-node-right node)) (tree-node-val node)))
              (set! right-path (+ right-arm 1)))
            (set! ans (max ans (+ left-path right-path)))
            (max left-path right-path))))
    (dfs root)
    ans))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec longest_univalue_path(Root :: #tree_node{} | null) -> integer().
longest_univalue_path(null) ->
    0;
longest_univalue_path(Root) ->
    {Ans, _} = longest_univalue_path_helper(Root),
    Ans.

%% helper returns {BestPathLength, UpwardLength}
-spec longest_univalue_path_helper(Node :: #tree_node{} | null) -> {integer(), integer()}.
longest_univalue_path_helper(null) ->
    {0, 0};
longest_univalue_path_helper(Node) ->
    #tree_node{val = Val, left = Left, right = Right} = Node,
    {LeftBest, LeftUp}   = longest_univalue_path_helper(Left),
    {RightBest, RightUp} = longest_univalue_path_helper(Right),

    LeftLen = case Left of
        null -> 0;
        #tree_node{val = LVal} when LVal =:= Val -> LeftUp + 1;
        _ -> 0
    end,
    RightLen = case Right of
        null -> 0;
        #tree_node{val = RVal} when RVal =:= Val -> RightUp + 1;
        _ -> 0
    end,

    CurrentBest = erlang:max(LeftBest, erlang:max(RightBest, LeftLen + RightLen)),
    UpLen       = erlang:max(LeftLen, RightLen),
    {CurrentBest, UpLen}.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_univalue_path(root :: TreeNode.t | nil) :: integer
  def longest_univalue_path(root) do
    {_down, max_len} = dfs(root)
    max_len
  end

  defp dfs(nil), do: {0, 0}

  defp dfs(%TreeNode{val: val, left: left, right: right}) do
    {left_down, left_max} = dfs(left)
    {right_down, right_max} = dfs(right)

    left_arm =
      case left do
        %TreeNode{val: lval} when lval == val -> left_down + 1
        _ -> 0
      end

    right_arm =
      case right do
        %TreeNode{val: rval} when rval == val -> right_down + 1
        _ -> 0
      end

    current_max = max(left_max, right_max)
    current_max = max(current_max, left_arm + right_arm)

    {max(left_arm, right_arm), current_max}
  end
end
```
