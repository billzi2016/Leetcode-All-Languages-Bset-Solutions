# 0129. Sum Root to Leaf Numbers

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
    int sumNumbers(TreeNode* root) {
        return dfs(root, 0);
    }
private:
    int dfs(TreeNode* node, int cur) {
        if (!node) return 0;
        cur = cur * 10 + node->val;
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
    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int current) {
        if (node == null) {
            return 0;
        }
        int newVal = current * 10 + node.val;
        if (node.left == null && node.right == null) {
            return newVal;
        }
        return dfs(node.left, newVal) + dfs(node.right, newVal);
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
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        def dfs(node, cur):
            cur = cur * 10 + node.val
            # If leaf, return the number formed.
            if not node.left and not node.right:
                return cur
            total = 0
            if node.left:
                total += dfs(node.left, cur)
            if node.right:
                total += dfs(node.right, cur)
            return total

        return dfs(root, 0)
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, cur: int) -> int:
            if not node:
                return 0
            cur = cur * 10 + node.val
            if not node.left and not node.right:
                return cur
            return dfs(node.left, cur) + dfs(node.right, cur)
        return dfs(root, 0)
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
    cur = cur * 10 + node->val;
    if (!node->left && !node->right) return cur;
    return dfs(node->left, cur) + dfs(node->right, cur);
}

int sumNumbers(struct TreeNode* root) {
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
    public int SumNumbers(TreeNode root) {
        return Dfs(root, 0);
    }

    private int Dfs(TreeNode node, int current) {
        if (node == null) return 0;
        int newVal = current * 10 + node.val;
        if (node.left == null && node.right == null) {
            return newVal;
        }
        return Dfs(node.left, newVal) + Dfs(node.right, newVal);
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
var sumNumbers = function(root) {
    let total = 0;
    const dfs = (node, cur) => {
        if (!node) return;
        cur = cur * 10 + node.val;
        if (!node.left && !node.right) {
            total += cur;
            return;
        }
        if (node.left) dfs(node.left, cur);
        if (node.right) dfs(node.right, cur);
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

function sumNumbers(root: TreeNode | null): number {
    const dfs = (node: TreeNode | null, cur: number): number => {
        if (!node) return 0;
        const next = cur * 10 + node.val;
        if (!node.left && !node.right) {
            return next;
        }
        return dfs(node.left, next) + dfs(node.right, next);
    };
    return dfs(root, 0);
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
    function sumNumbers($root) {
        return $this->dfs($root, 0);
    }

    private function dfs($node, $current) {
        if ($node === null) {
            return 0;
        }
        $current = $current * 10 + $node->val;
        if ($node->left === null && $node->right === null) {
            return $current;
        }
        return $this->dfs($node->left, $current) + $this->dfs($node->right, $current);
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
    func sumNumbers(_ root: TreeNode?) -> Int {
        return dfs(root, 0)
    }
    
    private func dfs(_ node: TreeNode?, _ current: Int) -> Int {
        guard let n = node else { return 0 }
        let newVal = current * 10 + n.val
        if n.left == nil && n.right == nil {
            return newVal
        }
        return dfs(n.left, newVal) + dfs(n.right, newVal)
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
    fun sumNumbers(root: TreeNode?): Int {
        return dfs(root, 0)
    }

    private fun dfs(node: TreeNode?, cur: Int): Int {
        if (node == null) return 0
        val newVal = cur * 10 + node.`val`
        if (node.left == null && node.right == null) {
            return newVal
        }
        return dfs(node.left, newVal) + dfs(node.right, newVal)
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
  int sumNumbers(TreeNode? root) {
    return _dfs(root, 0);
  }

  int _dfs(TreeNode? node, int cur) {
    if (node == null) return 0;
    int newCur = cur * 10 + node.val;
    if (node.left == null && node.right == null) {
      return newCur;
    }
    return _dfs(node.left, newCur) + _dfs(node.right, newCur);
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
func sumNumbers(root *TreeNode) int {
	var dfs func(node *TreeNode, cur int) int
	dfs = func(node *TreeNode, cur int) int {
		if node == nil {
			return 0
		}
		cur = cur*10 + node.Val
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
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end

def sum_numbers(root)
  dfs = lambda do |node, cur|
    return 0 unless node
    cur = cur * 10 + node.val
    if node.left.nil? && node.right.nil?
      cur
    else
      dfs.call(node.left, cur) + dfs.call(node.right, cur)
    end
  end
  dfs.call(root, 0)
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
    def sumNumbers(root: TreeNode): Int = {
        def dfs(node: TreeNode, cur: Int): Int = {
            if (node == null) return 0
            val newCur = cur * 10 + node.value
            if (node.left == null && node.right == null) {
                newCur
            } else {
                dfs(node.left, newCur) + dfs(node.right, newCur)
            }
        }
        dfs(root, 0)
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn sum_numbers(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, cur: i64) -> i64 {
            if let Some(rc_node) = node {
                let n = rc_node.borrow();
                let new_cur = cur * 10 + n.val as i64;
                if n.left.is_none() && n.right.is_none() {
                    return new_cur;
                }
                let left_sum = dfs(n.left.clone(), new_cur);
                let right_sum = dfs(n.right.clone(), new_cur);
                left_sum + right_sum
            } else {
                0
            }
        }
        dfs(root, 0) as i32
    }
}
```

## Racket

```racket
(define/contract (sum-numbers root)
  (-> (or/c tree-node? #f) exact-integer?)
  (letrec ((dfs
            (lambda (node cur)
              (if (not node)
                  0
                  (let* ((new-cur (+ (* cur 10) (tree-node-val node)))
                         (left (tree-node-left node))
                         (right (tree-node-right node)))
                    (if (and (not left) (not right))
                        new-cur
                        (+ (dfs left new-cur)
                           (dfs right new-cur))))))))
    (dfs root 0)))
```

## Erlang

```erlang
-module(solution).
-export([sum_numbers/1]).

%% Definition for a binary tree node.
-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec sum_numbers(Root :: #tree_node{} | null) -> integer().
sum_numbers(null) ->
    0;
sum_numbers(Root) ->
    dfs(Root, 0).

dfs(null, _Acc) ->
    0;
dfs(Node, Acc) ->
    NewAcc = Acc * 10 + Node#tree_node.val,
    case {Node#tree_node.left, Node#tree_node.right} of
        {null, null} -> NewAcc;
        {_L, _R} ->
            dfs(Node#tree_node.left, NewAcc) + dfs(Node#tree_node.right, NewAcc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_numbers(root :: TreeNode.t | nil) :: integer
  def sum_numbers(nil), do: 0
  def sum_numbers(root) do
    dfs(root, 0)
  end

  defp dfs(%TreeNode{val: v, left: nil, right: nil}, acc) do
    acc * 10 + v
  end

  defp dfs(%TreeNode{val: v, left: l, right: r}, acc) do
    new_acc = acc * 10 + v
    sum_left = if l != nil, do: dfs(l, new_acc), else: 0
    sum_right = if r != nil, do: dfs(r, new_acc), else: 0
    sum_left + sum_right
  end
end
```
