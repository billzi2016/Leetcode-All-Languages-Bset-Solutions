# 1022. Sum of Root To Leaf Binary Numbers

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
    int sumRootToLeaf(TreeNode* root) {
        return dfs(root, 0);
    }
private:
    int dfs(TreeNode* node, int cur) {
        if (!node) return 0;
        cur = (cur << 1) | node->val;
        if (!node->left && !node->right) {
            return cur;
        }
        return dfs(node->left, cur) + dfs(node->right, cur);
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
    private int total = 0;

    public int sumRootToLeaf(TreeNode root) {
        dfs(root, 0);
        return total;
    }

    private void dfs(TreeNode node, int cur) {
        if (node == null) {
            return;
        }
        cur = (cur << 1) | node.val;
        if (node.left == null && node.right == null) {
            total += cur;
            return;
        }
        dfs(node.left, cur);
        dfs(node.right, cur);
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
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, cur):
            if not node:
                return 0
            cur = (cur << 1) | node.val
            # leaf check
            if not node.left and not node.right:
                return cur
            return dfs(node.left, cur) + dfs(node.right, cur)
        
        return dfs(root, 0)
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
    def sumRootToLeaf(self, root: Optional['TreeNode']) -> int:
        if not root:
            return 0
        total = 0
        stack = [(root, root.val)]
        while stack:
            node, cur = stack.pop()
            # If leaf node, add current value to total
            if not node.left and not node.right:
                total += cur
            else:
                if node.right:
                    stack.append((node.right, (cur << 1) | node.right.val))
                if node.left:
                    stack.append((node.left, (cur << 1) | node.left.val))
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
static int dfs(struct TreeNode* node, int cur) {
    if (!node) return 0;
    cur = (cur << 1) | node->val;
    if (!node->left && !node->right) {
        return cur;
    }
    return dfs(node->left, cur) + dfs(node->right, cur);
}

int sumRootToLeaf(struct TreeNode* root) {
    return dfs(root, 0);
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
    public int SumRootToLeaf(TreeNode root) {
        return Dfs(root, 0);
    }

    private int Dfs(TreeNode node, int current) {
        if (node == null) return 0;
        current = (current << 1) | node.val;
        if (node.left == null && node.right == null) {
            return current;
        }
        return Dfs(node.left, current) + Dfs(node.right, current);
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
var sumRootToLeaf = function(root) {
    let total = 0;
    const dfs = (node, cur) => {
        if (!node) return;
        cur = (cur << 1) | node.val; // build binary number
        if (!node.left && !node.right) {
            total += cur;
        } else {
            dfs(node.left, cur);
            dfs(node.right, cur);
        }
    };
    dfs(root, 0);
    return total;
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

function sumRootToLeaf(root: TreeNode | null): number {
    let total = 0;
    const dfs = (node: TreeNode | null, cur: number): void => {
        if (!node) return;
        cur = (cur << 1) | node.val;
        if (!node.left && !node.right) {
            total += cur;
        } else {
            dfs(node.left, cur);
            dfs(node.right, cur);
        }
    };
    dfs(root, 0);
    return total;
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
    function sumRootToLeaf($root) {
        return $this->dfs($root, 0);
    }

    private function dfs($node, $current) {
        if ($node === null) {
            return 0;
        }
        $current = ($current << 1) | $node->val;
        if ($node->left === null && $node->right === null) {
            return $current;
        }
        $sum = 0;
        if ($node->left !== null) {
            $sum += $this->dfs($node->left, $current);
        }
        if ($node->right !== null) {
            $sum += $this->dfs($node->right, $current);
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
    func sumRootToLeaf(_ root: TreeNode?) -> Int {
        var total = 0
        func dfs(_ node: TreeNode?, _ current: Int) {
            guard let n = node else { return }
            let newVal = (current << 1) | n.val
            if n.left == nil && n.right == nil {
                total += newVal
            } else {
                dfs(n.left, newVal)
                dfs(n.right, newVal)
            }
        }
        dfs(root, 0)
        return total
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
    fun sumRootToLeaf(root: TreeNode?): Int {
        var total = 0
        fun dfs(node: TreeNode?, cur: Int) {
            if (node == null) return
            val next = (cur shl 1) or node.`val`
            if (node.left == null && node.right == null) {
                total += next
            } else {
                dfs(node.left, next)
                dfs(node.right, next)
            }
        }
        dfs(root, 0)
        return total
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
  int sumRootToLeaf(TreeNode? root) {
    return _dfs(root, 0);
  }

  int _dfs(TreeNode? node, int cur) {
    if (node == null) return 0;
    int next = ((cur << 1) | node.val);
    if (node.left == null && node.right == null) {
      return next;
    }
    return _dfs(node.left, next) + _dfs(node.right, next);
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
func sumRootToLeaf(root *TreeNode) int {
    var dfs func(node *TreeNode, cur int) int
    dfs = func(node *TreeNode, cur int) int {
        if node == nil {
            return 0
        }
        cur = (cur << 1) | node.Val
        if node.Left == nil && node.Right == nil {
            return cur
        }
        return dfs(node.Left, cur) + dfs(node.Right, cur)
    }
    return dfs(root, 0)
}
```

## Ruby

```ruby
def sum_root_to_leaf(root)
  return 0 unless root
  sum = 0
  stack = [[root, 0]]
  until stack.empty?
    node, val = stack.pop
    cur = (val << 1) | node.val
    if node.left.nil? && node.right.nil?
      sum += cur
    else
      stack << [node.right, cur] if node.right
      stack << [node.left, cur] if node.left
    end
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
    def sumRootToLeaf(root: TreeNode): Int = {
        var total = 0
        def dfs(node: TreeNode, cur: Int): Unit = {
            if (node == null) return
            val newVal = (cur << 1) | node.value
            if (node.left == null && node.right == null) {
                total += newVal
            } else {
                if (node.left != null) dfs(node.left, newVal)
                if (node.right != null) dfs(node.right, newVal)
            }
        }
        dfs(root, 0)
        total
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn sum_root_to_leaf(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, cur: i32) -> i32 {
            if let Some(rc) = node {
                let n = rc.borrow();
                let new_cur = (cur << 1) | n.val;
                if n.left.is_none() && n.right.is_none() {
                    return new_cur;
                }
                dfs(&n.left, new_cur) + dfs(&n.right, new_cur)
            } else {
                0
            }
        }
        dfs(&root, 0)
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

(define/contract (sum-root-to-leaf root)
  (-> (or/c tree-node? #f) exact-integer?)
  (let loop ((node root) (curr 0))
    (if (not node)
        0
        (let* ((new-val (bitwise-ior (arithmetic-shift curr 1)
                                     (tree-node-val node))))
          (if (and (false? (tree-node-left node))
                   (false? (tree-node-right node)))
              new-val
              (+ (loop (tree-node-left node) new-val)
                 (loop (tree-node-right node) new-val)))))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec sum_root_to_leaf(Root :: #tree_node{} | null) -> integer().
sum_root_to_leaf(null) ->
    0;
sum_root_to_leaf(Root) ->
    sum_root_to_leaf(Root, 0).

%% internal helper with accumulated binary value
-spec sum_root_to_leaf(#tree_node{}, integer()) -> integer().
sum_root_to_leaf(#tree_node{val = V, left = L, right = R}, Acc) ->
    NewAcc = (Acc bsl 1) bor V,
    case {L, R} of
        {null, null} ->
            NewAcc;
        _ ->
            LeftSum = case L of
                null -> 0;
                _ -> sum_root_to_leaf(L, NewAcc)
            end,
            RightSum = case R of
                null -> 0;
                _ -> sum_root_to_leaf(R, NewAcc)
            end,
            LeftSum + RightSum
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec sum_root_to_leaf(root :: TreeNode.t | nil) :: integer
  def sum_root_to_leaf(root) do
    dfs(root, 0)
  end

  defp dfs(nil, _), do: 0

  defp dfs(%TreeNode{val: v, left: l, right: r}, cur) do
    new_cur = (cur <<< 1) ||| v

    if l == nil and r == nil do
      new_cur
    else
      dfs(l, new_cur) + dfs(r, new_cur)
    end
  end
end
```
