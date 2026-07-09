# 1457. Pseudo-Palindromic Paths in a Binary Tree

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
    int pseudoPalindromicPaths (TreeNode* root) {
        if (!root) return 0;
        int ans = 0;
        dfs(root, 0, ans);
        return ans;
    }
private:
    void dfs(TreeNode* node, int mask, int& ans) {
        // toggle the bit corresponding to node->val
        mask ^= (1 << node->val);
        
        // if leaf, check palindrome condition
        if (!node->left && !node->right) {
            if ((mask & (mask - 1)) == 0) ++ans; // at most one bit set
            return;
        }
        if (node->left) dfs(node->left, mask, ans);
        if (node->right) dfs(node->right, mask, ans);
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
    public int pseudoPalindromicPaths (TreeNode root) {
        return dfs(root, 0);
    }
    
    private int dfs(TreeNode node, int mask) {
        if (node == null) {
            return 0;
        }
        // toggle the bit corresponding to node.val
        mask ^= (1 << node.val);
        
        // if it's a leaf, check the mask condition
        if (node.left == null && node.right == null) {
            // at most one bit set in mask
            return ((mask & (mask - 1)) == 0) ? 1 : 0;
        }
        
        int leftCount = dfs(node.left, mask);
        int rightCount = dfs(node.right, mask);
        return leftCount + rightCount;
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
    def pseudoPalindromicPaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, mask):
            if not node:
                return 0
            mask ^= (1 << node.val)
            # leaf node
            if not node.left and not node.right:
                return 1 if mask & (mask - 1) == 0 else 0
            return dfs(node.left, mask) + dfs(node.right, mask)

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

from typing import Optional

class Solution:
    def pseudoPalindromicPaths(self, root: Optional['TreeNode']) -> int:
        def dfs(node: Optional['TreeNode'], mask: int) -> int:
            if not node:
                return 0
            mask ^= 1 << node.val
            # leaf check
            if not node.left and not node.right:
                return 1 if mask & (mask - 1) == 0 else 0
            return dfs(node.left, mask) + dfs(node.right, mask)
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
static int dfs(struct TreeNode* node, int mask) {
    if (!node) return 0;
    mask ^= (1 << node->val);
    if (!node->left && !node->right) {
        return (mask & (mask - 1)) == 0 ? 1 : 0;
    }
    int left = dfs(node->left, mask);
    int right = dfs(node->right, mask);
    return left + right;
}

int pseudoPalindromicPaths(struct TreeNode* root) {
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
    public int PseudoPalindromicPaths(TreeNode root) {
        return Dfs(root, 0);
    }

    private int Dfs(TreeNode node, int mask) {
        if (node == null) return 0;

        // Toggle the bit corresponding to node.val
        mask ^= (1 << node.val);

        // If it's a leaf, check if at most one bit is set in mask
        if (node.left == null && node.right == null) {
            return (mask & (mask - 1)) == 0 ? 1 : 0;
        }

        int leftCount = Dfs(node.left, mask);
        int rightCount = Dfs(node.right, mask);
        return leftCount + rightCount;
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
var pseudoPalindromicPaths = function(root) {
    if (!root) return 0;
    let count = 0;
    const stack = [[root, 0]];
    while (stack.length) {
        const [node, mask] = stack.pop();
        const newMask = mask ^ (1 << node.val);
        // leaf check
        if (!node.left && !node.right) {
            if ((newMask & (newMask - 1)) === 0) count++;
        } else {
            if (node.right) stack.push([node.right, newMask]);
            if (node.left)  stack.push([node.left,  newMask]);
        }
    }
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

function pseudoPalindromicPaths(root: TreeNode | null): number {
    const dfs = (node: TreeNode | null, mask: number): number => {
        if (!node) return 0;
        // toggle the bit corresponding to node.val
        mask ^= (1 << node.val);
        // if leaf node, check if at most one bit is set
        if (!node.left && !node.right) {
            return (mask & (mask - 1)) === 0 ? 1 : 0;
        }
        const leftCount = dfs(node.left, mask);
        const rightCount = dfs(node.right, mask);
        return leftCount + rightCount;
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
    function pseudoPalindromicPaths ($root) {
        return $this->dfs($root, 0);
    }

    private function dfs($node, $path) {
        if ($node === null) {
            return 0;
        }
        // toggle the bit corresponding to node's value
        $path ^= (1 << $node->val);

        // leaf node: check if at most one bit is set
        if ($node->left === null && $node->right === null) {
            return (($path & ($path - 1)) == 0) ? 1 : 0;
        }

        $count = 0;
        if ($node->left !== null) {
            $count += $this->dfs($node->left, $path);
        }
        if ($node->right !== null) {
            $count += $this->dfs($node->right, $path);
        }
        return $count;
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
    func pseudoPalindromicPaths(_ root: TreeNode?) -> Int {
        return dfs(root, 0)
    }

    private func dfs(_ node: TreeNode?, _ mask: Int) -> Int {
        guard let n = node else { return 0 }
        let newMask = mask ^ (1 << n.val)
        if n.left == nil && n.right == nil {
            // leaf node
            return (newMask & (newMask - 1)) == 0 ? 1 : 0
        }
        let leftCount = dfs(n.left, newMask)
        let rightCount = dfs(n.right, newMask)
        return leftCount + rightCount
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
    fun pseudoPalindromicPaths(root: TreeNode?): Int {
        var result = 0

        fun dfs(node: TreeNode?, mask: Int) {
            if (node == null) return
            val newMask = mask xor (1 shl node.`val`)
            if (node.left == null && node.right == null) {
                // leaf node: check if at most one bit is set
                if ((newMask and (newMask - 1)) == 0) {
                    result++
                }
            } else {
                dfs(node.left, newMask)
                dfs(node.right, newMask)
            }
        }

        dfs(root, 0)
        return result
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
  int pseudoPalindromicPaths(TreeNode? root) {
    int count = 0;

    void dfs(TreeNode? node, int pathMask) {
      if (node == null) return;
      pathMask ^= (1 << node.val);
      if (node.left == null && node.right == null) {
        // leaf node: check if at most one bit is set
        if ((pathMask & (pathMask - 1)) == 0) count++;
      } else {
        dfs(node.left, pathMask);
        dfs(node.right, pathMask);
      }
    }

    dfs(root, 0);
    return count;
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
func pseudoPalindromicPaths(root *TreeNode) int {
    var dfs func(node *TreeNode, mask int) int
    dfs = func(node *TreeNode, mask int) int {
        if node == nil {
            return 0
        }
        mask ^= 1 << node.Val
        if node.Left == nil && node.Right == nil {
            if mask&(mask-1) == 0 {
                return 1
            }
            return 0
        }
        return dfs(node.Left, mask) + dfs(node.Right, mask)
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

def pseudo_palindromic_paths(root)
  dfs = lambda do |node, mask|
    return 0 unless node
    mask ^= (1 << node.val)
    if node.left.nil? && node.right.nil?
      (mask & (mask - 1)).zero? ? 1 : 0
    else
      dfs.call(node.left, mask) + dfs.call(node.right, mask)
    end
  end
  dfs.call(root, 0)
end
```

## Scala

```scala
object Solution {
    def pseudoPalindromicPaths(root: TreeNode): Int = {
        def dfs(node: TreeNode, mask: Int): Int = {
            if (node == null) return 0
            val newMask = mask ^ (1 << node.value)
            if (node.left == null && node.right == null) {
                if ((newMask & (newMask - 1)) == 0) 1 else 0
            } else {
                dfs(node.left, newMask) + dfs(node.right, newMask)
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
    pub fn pseudo_palindromic_paths(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, mask: i32) -> i32 {
            if let Some(rc_node) = node {
                let node_ref = rc_node.borrow();
                let val = node_ref.val;
                let new_mask = mask ^ (1 << val);
                let left = node_ref.left.clone();
                let right = node_ref.right.clone();
                if left.is_none() && right.is_none() {
                    if new_mask & (new_mask - 1) == 0 { 1 } else { 0 }
                } else {
                    dfs(left, new_mask) + dfs(right, new_mask)
                }
            } else {
                0
            }
        }

        dfs(root, 0)
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

(define/contract (pseudo-palindromic-paths root)
  (-> (or/c tree-node? #f) exact-integer?)
  (let loop ((stack (if root (list (cons root 0)) '())) ; each element is (node . mask)
             (cnt   0))
    (if (null? stack)
        cnt
        (let* ((pair      (car stack))
               (rest      (cdr stack))
               (node      (car pair))
               (mask      (cdr pair))
               (new-mask  (bitwise-xor mask (arithmetic-shift 1 (tree-node-val node)))))
          (if (and (not (tree-node-left node)) (not (tree-node-right node)))
              (let ((add (if (= (bitwise-and new-mask (sub1 new-mask)) 0) 1 0)))
                (loop rest (+ cnt add)))
              (let ((stack2 rest))
                (when (tree-node-right node)
                  (set! stack2 (cons (cons (tree-node-right node) new-mask) stack2)))
                (when (tree-node-left node)
                  (set! stack2 (cons (cons (tree-node-left node) new-mask) stack2)))
                (loop stack2 cnt)))))))
```

## Erlang

```erlang
-module(solution).
-export([pseudo_palindromic_paths/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec pseudo_palindromic_paths(Root :: #tree_node{} | null) -> integer().
pseudo_palindromic_paths(Root) ->
    dfs(Root, 0).

dfs(null, _Mask) ->
    0;
dfs(Node, Mask) ->
    NewMask = Mask bxor (1 bsl Node#tree_node.val),
    case {Node#tree_node.left, Node#tree_node.right} of
        {null, null} ->
            if
                (NewMask band (NewMask - 1)) == 0 -> 1;
                true -> 0
            end;
        _ ->
            dfs(Node#tree_node.left, NewMask) + dfs(Node#tree_node.right, NewMask)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec pseudo_palindromic_paths(root :: TreeNode.t() | nil) :: integer()
  def pseudo_palindromic_paths(root) do
    dfs(root, 0)
  end

  defp dfs(nil, _mask), do: 0

  defp dfs(%TreeNode{val: v, left: l, right: r}, mask) do
    new_mask = mask ^^^ (1 <<< v)

    if l == nil and r == nil do
      if (new_mask &&& (new_mask - 1)) == 0, do: 1, else: 0
    else
      dfs(l, new_mask) + dfs(r, new_mask)
    end
  end
end
```
