# 0938. Range Sum of BST

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
    int rangeSumBST(TreeNode* root, int low, int high) {
        if (!root) return 0;
        if (root->val < low) {
            // current value too small, skip left subtree
            return rangeSumBST(root->right, low, high);
        }
        if (root->val > high) {
            // current value too large, skip right subtree
            return rangeSumBST(root->left, low, high);
        }
        // within range, include it and explore both sides
        return root->val + 
               rangeSumBST(root->left, low, high) + 
               rangeSumBST(root->right, low, high);
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
    public int rangeSumBST(TreeNode root, int low, int high) {
        if (root == null) return 0;
        int sum = 0;
        if (root.val >= low && root.val <= high) {
            sum += root.val;
        }
        if (root.val > low) {
            sum += rangeSumBST(root.left, low, high);
        }
        if (root.val < high) {
            sum += rangeSumBST(root.right, low, high);
        }
        return sum;
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
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        total = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if low <= node.val <= high:
                total += node.val
            if node.val > low:
                stack.append(node.left)
            if node.val < high:
                stack.append(node.right)
        return total
```

## Python3

```python
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional['TreeNode'], low: int, high: int) -> int:
        total = 0
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            if not node:
                continue
            if low <= node.val <= high:
                total += node.val
            if node.val > low and node.left:
                stack.append(node.left)
            if node.val < high and node.right:
                stack.append(node.right)
        return total
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
int rangeSumBST(struct TreeNode* root, int low, int high) {
    if (!root) return 0;
    if (root->val < low)
        return rangeSumBST(root->right, low, high);
    if (root->val > high)
        return rangeSumBST(root->left, low, high);
    return root->val + 
           rangeSumBST(root->left, low, high) + 
           rangeSumBST(root->right, low, high);
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
    public int RangeSumBST(TreeNode root, int low, int high) {
        if (root == null) return 0;
        int sum = 0;
        if (root.val >= low && root.val <= high) sum += root.val;
        if (root.val > low) sum += RangeSumBST(root.left, low, high);
        if (root.val < high) sum += RangeSumBST(root.right, low, high);
        return sum;
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
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var rangeSumBST = function(root, low, high) {
    if (!root) return 0;
    let sum = 0;
    const stack = [root];
    while (stack.length) {
        const node = stack.pop();
        if (!node) continue;
        if (node.val < low) {
            if (node.right) stack.push(node.right);
        } else if (node.val > high) {
            if (node.left) stack.push(node.left);
        } else {
            sum += node.val;
            if (node.left) stack.push(node.left);
            if (node.right) stack.push(node.right);
        }
    }
    return sum;
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

function rangeSumBST(root: TreeNode | null, low: number, high: number): number {
    if (!root) return 0;
    if (root.val < low) {
        // Current value too small, skip left subtree
        return rangeSumBST(root.right, low, high);
    }
    if (root.val > high) {
        // Current value too large, skip right subtree
        return rangeSumBST(root.left, low, high);
    }
    // Within range, include current and explore both sides
    return root.val + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high);
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
     * @param Integer $low
     * @param Integer $high
     * @return Integer
     */
    function rangeSumBST($root, $low, $high) {
        return $this->dfs($root, $low, $high);
    }

    private function dfs($node, $low, $high) {
        if ($node === null) {
            return 0;
        }
        $sum = 0;
        if ($node->val >= $low && $node->val <= $high) {
            $sum += $node->val;
        }
        if ($node->val > $low) {
            $sum += $this->dfs($node->left, $low, $high);
        }
        if ($node->val < $high) {
            $sum += $this->dfs($node->right, $low, $high);
        }
        return $sum;
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
    func rangeSumBST(_ root: TreeNode?, _ low: Int, _ high: Int) -> Int {
        guard let node = root else { return 0 }
        var sum = 0
        if node.val >= low && node.val <= high {
            sum += node.val
        }
        if node.val > low {
            sum += rangeSumBST(node.left, low, high)
        }
        if node.val < high {
            sum += rangeSumBST(node.right, low, high)
        }
        return sum
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
    fun rangeSumBST(root: TreeNode?, low: Int, high: Int): Int {
        if (root == null) return 0
        var sum = 0
        val v = root.`val`
        if (v in low..high) sum += v
        if (v > low) sum += rangeSumBST(root.left, low, high)
        if (v < high) sum += rangeSumBST(root.right, low, high)
        return sum
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
  int rangeSumBST(TreeNode? root, int low, int high) {
    if (root == null) return 0;
    if (root.val < low) {
      return rangeSumBST(root.right, low, high);
    }
    if (root.val > high) {
      return rangeSumBST(root.left, low, high);
    }
    return root.val +
        rangeSumBST(root.left, low, high) +
        rangeSumBST(root.right, low, high);
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
func rangeSumBST(root *TreeNode, low int, high int) int {
	if root == nil {
		return 0
	}
	if root.Val < low {
		return rangeSumBST(root.Right, low, high)
	}
	if root.Val > high {
		return rangeSumBST(root.Left, low, high)
	}
	return root.Val + rangeSumBST(root.Left, low, high) + rangeSumBST(root.Right, low, high)
}
```

## Ruby

```ruby
def range_sum_bst(root, low, high)
  sum = 0
  stack = [root]
  until stack.empty?
    node = stack.pop
    next unless node
    if node.val >= low && node.val <= high
      sum += node.val
    end
    stack << node.left if node.val > low
    stack << node.right if node.val < high
  end
  sum
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
    def rangeSumBST(root: TreeNode, low: Int, high: Int): Int = {
        def dfs(node: TreeNode): Int = {
            if (node == null) return 0
            var sum = 0
            if (node.value >= low && node.value <= high) sum += node.value
            if (node.value > low) sum += dfs(node.left)
            if (node.value < high) sum += dfs(node.right)
            sum
        }
        dfs(root)
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }

impl Solution {
    pub fn range_sum_bst(root: Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32 {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32, acc: &mut i32) {
            if let Some(rc) = node {
                let n = rc.borrow();
                let val = n.val;
                if val >= low && val <= high {
                    *acc += val;
                }
                if val > low {
                    dfs(&n.left, low, high, acc);
                }
                if val < high {
                    dfs(&n.right, low, high, acc);
                }
            }
        }

        let mut sum = 0;
        dfs(&root, low, high, &mut sum);
        sum
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

(define/contract (range-sum-bst root low high)
  (-> (or/c tree-node? #f) exact-integer? exact-integer? exact-integer?)
  (let recur ((node root))
    (if (not node)
        0
        (let* ((v   (tree-node-val node))
               (l   (tree-node-left node))
               (r   (tree-node-right node)))
          (cond
            [(< v low) (recur r)]
            [(> v high) (recur l)]
            [else (+ v (recur l) (recur r))])))))
```

## Erlang

```erlang
-record(tree_node, {val = 0 :: integer(),
                      left = null  :: 'null' | #tree_node{},
                      right = null :: 'null' | #tree_node{}}).

-spec range_sum_bst(Root :: #tree_node{} | null, Low :: integer(), High :: integer()) -> integer().
range_sum_bst(null, _Low, _High) ->
    0;
range_sum_bst(#tree_node{val = Val, left = Left, right = Right}, Low, High) ->
    case Val of
        V when V < Low ->
            range_sum_bst(Right, Low, High);
        V when V > High ->
            range_sum_bst(Left, Low, High);
        _ ->
            Val + range_sum_bst(Left, Low, High) + range_sum_bst(Right, Low, High)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec range_sum_bst(root :: TreeNode.t() | nil, low :: integer, high :: integer) :: integer
  def range_sum_bst(nil, _low, _high), do: 0

  def range_sum_bst(%TreeNode{val: v, left: l, right: r}, low, high) do
    cond do
      v < low -> range_sum_bst(r, low, high)
      v > high -> range_sum_bst(l, low, high)
      true ->
        v + range_sum_bst(l, low, high) + range_sum_bst(r, low, high)
    end
  end
end
```
