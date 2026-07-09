# 1315. Sum of Nodes with Even-Valued Grandparent

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
    int sumEvenGrandparent(TreeNode* root) {
        long long ans = 0;
        dfs(root, -1, -1, ans);
        return static_cast<int>(ans);
    }
private:
    void dfs(TreeNode* node, int parentVal, int grandParentVal, long long& ans) {
        if (!node) return;
        if (grandParentVal != -1 && (grandParentVal & 1) == 0) {
            ans += node->val;
        }
        dfs(node->left, node->val, parentVal, ans);
        dfs(node->right, node->val, parentVal, ans);
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
    public int sumEvenGrandparent(TreeNode root) {
        return dfs(root, -1, -1);
    }

    private int dfs(TreeNode node, int parentVal, int grandParentVal) {
        if (node == null) {
            return 0;
        }
        int sum = 0;
        if ((grandParentVal & 1) == 0) { // even check
            sum += node.val;
        }
        sum += dfs(node.left, node.val, parentVal);
        sum += dfs(node.right, node.val, parentVal);
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
    def sumEvenGrandparent(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, parent_val, grandparent_val):
            if not node:
                return 0
            total = node.val if grandparent_val % 2 == 0 else 0
            total += dfs(node.left, node.val, parent_val)
            total += dfs(node.right, node.val, parent_val)
            return total

        # Use sentinel odd values for parent and grandparent of root
        return dfs(root, -1, -1)
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
    def sumEvenGrandparent(self, root: Optional['TreeNode']) -> int:
        def dfs(node: Optional['TreeNode'], parent_val: int, grandparent_val: int) -> int:
            if not node:
                return 0
            total = node.val if grandparent_val % 2 == 0 else 0
            total += dfs(node.left, node.val, parent_val)
            total += dfs(node.right, node.val, parent_val)
            return total

        # Use sentinel odd values for parent and grandparent of root
        return dfs(root, -1, -1)
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
static int dfs(struct TreeNode* node, int parent, int grandparent) {
    if (!node) return 0;
    int sum = (grandparent % 2 == 0) ? node->val : 0;
    sum += dfs(node->left, node->val, parent);
    sum += dfs(node->right, node->val, parent);
    return sum;
}

int sumEvenGrandparent(struct TreeNode* root) {
    if (!root) return 0;
    /* Use odd sentinel values for parent and grandparent of the root */
    return dfs(root, -1, -1);
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
    public int SumEvenGrandparent(TreeNode root) {
        return Dfs(root, null, null);
    }

    private int Dfs(TreeNode node, TreeNode parent, TreeNode grandParent) {
        if (node == null) return 0;

        int sum = 0;
        if (grandParent != null && grandParent.val % 2 == 0) {
            sum += node.val;
        }

        sum += Dfs(node.left, node, parent);
        sum += Dfs(node.right, node, parent);

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
 * @return {number}
 */
var sumEvenGrandparent = function(root) {
    const dfs = (node, parentVal, grandParentVal) => {
        if (!node) return 0;
        let sum = 0;
        if (grandParentVal % 2 === 0) sum += node.val;
        sum += dfs(node.left, node.val, parentVal);
        sum += dfs(node.right, node.val, parentVal);
        return sum;
    };
    // Use odd sentinel values for non‑existent ancestors
    return dfs(root, -1, -1);
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

function sumEvenGrandparent(root: TreeNode | null): number {
    let sum = 0;
    const dfs = (node: TreeNode | null, parentVal: number, grandParentVal: number): void => {
        if (!node) return;
        if (grandParentVal % 2 === 0) {
            sum += node.val;
        }
        dfs(node.left, node.val, parentVal);
        dfs(node.right, node.val, parentVal);
    };
    dfs(root, -1, -1);
    return sum;
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
    function sumEvenGrandparent($root) {
        return $this->dfs($root, -1, -1);
    }

    private function dfs($node, $parentVal, $grandParentVal) {
        if ($node === null) {
            return 0;
        }
        $sum = 0;
        if ($grandParentVal % 2 == 0) {
            $sum += $node->val;
        }
        $sum += $this->dfs($node->left, $node->val, $parentVal);
        $sum += $this->dfs($node->right, $node->val, $parentVal);
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
    func sumEvenGrandparent(_ root: TreeNode?) -> Int {
        return dfs(root, 1, 1)
    }
    
    private func dfs(_ node: TreeNode?, _ parentVal: Int, _ grandParentVal: Int) -> Int {
        guard let current = node else { return 0 }
        var sum = 0
        if grandParentVal % 2 == 0 {
            sum += current.val
        }
        sum += dfs(current.left, current.val, parentVal)
        sum += dfs(current.right, current.val, parentVal)
        return sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumEvenGrandparent(root: TreeNode?): Int {
        return dfs(root, -1, -1)
    }

    private fun dfs(node: TreeNode?, parentVal: Int, grandParentVal: Int): Int {
        if (node == null) return 0
        var sum = 0
        if (grandParentVal % 2 == 0) {
            sum += node.`val`
        }
        sum += dfs(node.left, node.`val`, parentVal)
        sum += dfs(node.right, node.`val`, parentVal)
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
  int sumEvenGrandparent(TreeNode? root) {
    return _dfs(root, null, null);
  }

  int _dfs(TreeNode? node, TreeNode? parent, TreeNode? grandParent) {
    if (node == null) return 0;
    int sum = 0;
    if (grandParent != null && grandParent.val % 2 == 0) {
      sum += node.val;
    }
    sum += _dfs(node.left, node, parent);
    sum += _dfs(node.right, node, parent);
    return sum;
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
func sumEvenGrandparent(root *TreeNode) int {
    var dfs func(node *TreeNode, parent, grand int) int
    dfs = func(node *TreeNode, parent, grand int) int {
        if node == nil {
            return 0
        }
        sum := 0
        if grand%2 == 0 {
            sum += node.Val
        }
        sum += dfs(node.Left, node.Val, parent)
        sum += dfs(node.Right, node.Val, parent)
        return sum
    }
    return dfs(root, -1, -1)
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

def sum_even_grandparent(root)
  dfs = lambda do |node, parent_val, grandparent_val|
    return 0 unless node
    total = 0
    total += node.val if grandparent_val && grandparent_val.even?
    total + dfs.call(node.left, node.val, parent_val) + dfs.call(node.right, node.val, parent_val)
  end

  dfs.call(root, nil, nil)
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
    def sumEvenGrandparent(root: TreeNode): Int = {
        def dfs(node: TreeNode, parentVal: Int, grandParentVal: Int): Int = {
            if (node == null) return 0
            var sum = 0
            if (grandParentVal % 2 == 0) sum += node.value
            sum + dfs(node.left, node.value, parentVal) + dfs(node.right, node.value, parentVal)
        }
        dfs(root, -1, -1)
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn sum_even_grandparent(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, parent: i32, grandparent: i32) -> i32 {
            if let Some(rc_node) = node {
                let val = rc_node.borrow().val;
                let mut sum = 0;
                if grandparent % 2 == 0 {
                    sum += val;
                }
                let left = rc_node.borrow().left.clone();
                let right = rc_node.borrow().right.clone();
                sum + dfs(left, val, parent) + dfs(right, val, parent)
            } else {
                0
            }
        }
        dfs(root, -1, -1)
    }
}
```

## Racket

```racket
#lang racket

;; Definition for a binary tree node.
(struct tree-node (val left right) #:mutable #:transparent)

(define/contract (sum-even-grandparent root)
  (-> (or/c tree-node? #f) exact-integer?)
  (letrec ((dfs
            (lambda (node parent grandparent)
              (if (not node)
                  0
                  (let* ((add (if (even? grandparent) (tree-node-val node) 0))
                         (left-sum (dfs (tree-node-left node) (tree-node-val node) parent))
                         (right-sum (dfs (tree-node-right node) (tree-node-val node) parent)))
                    (+ add left-sum right-sum))))))
    (dfs root -1 -1)))
```

## Erlang

```erlang
%% Definition for a binary tree node.
-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec sum_even_grandparent(Root :: #tree_node{} | null) -> integer().
sum_even_grandparent(Root) ->
    aux(Root, none, none).

aux(null, _, _) ->
    0;
aux(#tree_node{val = Val, left = L, right = R}, Parent, GrandParent) ->
    Add = case GrandParent of
        G when is_integer(G), G rem 2 =:= 0 -> Val;
        _ -> 0
    end,
    SumLeft = aux(L, Val, Parent),
    SumRight = aux(R, Val, Parent),
    Add + SumLeft + SumRight.
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_even_grandparent(root :: TreeNode.t() | nil) :: integer
  def sum_even_grandparent(root) do
    dfs(root, nil, nil)
  end

  defp dfs(nil, _parent, _grand), do: 0

  defp dfs(%TreeNode{val: v, left: l, right: r}, parent, grand) do
    add = if not is_nil(grand) and rem(grand, 2) == 0, do: v, else: 0
    add + dfs(l, v, parent) + dfs(r, v, parent)
  end
end
```
