# 0783. Minimum Distance Between BST Nodes

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
    int minDiffInBST(TreeNode* root) {
        prev = -1;
        ans = INT_MAX;
        inorder(root);
        return ans;
    }
private:
    int prev;
    int ans;
    void inorder(TreeNode* node) {
        if (!node) return;
        inorder(node->left);
        if (prev != -1) {
            ans = std::min(ans, node->val - prev);
        }
        prev = node->val;
        inorder(node->right);
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
    private int prev = -1;
    private int minDiff = Integer.MAX_VALUE;

    public int minDiffInBST(TreeNode root) {
        inorder(root);
        return minDiff;
    }

    private void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
        if (prev != -1) {
            minDiff = Math.min(minDiff, node.val - prev);
        }
        prev = node.val;
        inorder(node.right);
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
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.prev = None
        self.min_diff = float('inf')
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                diff = node.val - self.prev
                if diff < self.min_diff:
                    self.min_diff = diff
            self.prev = node.val
            inorder(node.right)
        
        inorder(root)
        return self.min_diff
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
    def minDiffInBST(self, root):
        self.prev = None
        self.min_diff = float('inf')
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                diff = node.val - self.prev
                if diff < self.min_diff:
                    self.min_diff = diff
            self.prev = node.val
            inorder(node.right)
        
        inorder(root)
        return self.min_diff
```

## C

```c
#include <limits.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
static void inorder(struct TreeNode* node, int* prev, int* minDiff) {
    if (!node) return;
    inorder(node->left, prev, minDiff);
    if (*prev != -1) {
        int diff = node->val - *prev;
        if (diff < *minDiff) *minDiff = diff;
    }
    *prev = node->val;
    inorder(node->right, prev, minDiff);
}

int minDiffInBST(struct TreeNode* root) {
    int prev = -1;
    int minDiff = INT_MAX;
    inorder(root, &prev, &minDiff);
    return minDiff;
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
    private int _prevVal;
    private bool _hasPrev;
    private int _minDiff;

    public int MinDiffInBST(TreeNode root)
    {
        _minDiff = int.MaxValue;
        _hasPrev = false;
        Inorder(root);
        return _minDiff;
    }

    private void Inorder(TreeNode node)
    {
        if (node == null) return;

        Inorder(node.left);

        if (_hasPrev)
        {
            int diff = node.val - _prevVal;
            if (diff < _minDiff) _minDiff = diff;
        }
        _prevVal = node.val;
        _hasPrev = true;

        Inorder(node.right);
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
var minDiffInBST = function(root) {
    let prev = null;
    let minDiff = Infinity;
    
    const inorder = (node) => {
        if (!node) return;
        inorder(node.left);
        if (prev !== null) {
            const diff = node.val - prev;
            if (diff < minDiff) minDiff = diff;
        }
        prev = node.val;
        inorder(node.right);
    };
    
    inorder(root);
    return minDiff;
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

function minDiffInBST(root: TreeNode | null): number {
    let prev: number | null = null;
    let minDiff = Number.MAX_SAFE_INTEGER;

    function inorder(node: TreeNode | null): void {
        if (!node) return;
        inorder(node.left);
        if (prev !== null) {
            const diff = node.val - prev;
            if (diff < minDiff) minDiff = diff;
        }
        prev = node.val;
        inorder(node.right);
    }

    inorder(root);
    return minDiff;
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
    function minDiffInBST($root) {
        $stack = [];
        $prev = null;
        $min = PHP_INT_MAX;
        $curr = $root;
        while (!empty($stack) || $curr !== null) {
            while ($curr !== null) {
                $stack[] = $curr;
                $curr = $curr->left;
            }
            $node = array_pop($stack);
            if ($prev !== null) {
                $diff = $node->val - $prev;
                if ($diff < $min) {
                    $min = $diff;
                }
            }
            $prev = $node->val;
            $curr = $node->right;
        }
        return $min;
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
    private var prev: Int?
    private var minDiff = Int.max

    func minDiffInBST(_ root: TreeNode?) -> Int {
        inorder(root)
        return minDiff
    }

    private func inorder(_ node: TreeNode?) {
        guard let n = node else { return }
        inorder(n.left)
        if let p = prev {
            let diff = n.val - p
            if diff < minDiff {
                minDiff = diff
            }
        }
        prev = n.val
        inorder(n.right)
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
    fun minDiffInBST(root: TreeNode?): Int {
        var prev = -1
        var minDiff = Int.MAX_VALUE

        fun inorder(node: TreeNode?) {
            if (node == null) return
            inorder(node.left)
            if (prev != -1) {
                val diff = node.`val` - prev
                if (diff < minDiff) minDiff = diff
            }
            prev = node.`val`
            inorder(node.right)
        }

        inorder(root)
        return minDiff
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
  int _minDiff = 0x7fffffff;
  int? _prev;

  void _inorder(TreeNode? node) {
    if (node == null) return;
    _inorder(node.left);
    if (_prev != null) {
      final diff = node.val - _prev!;
      if (diff < _minDiff) _minDiff = diff;
    }
    _prev = node.val;
    _inorder(node.right);
  }

  int minDiffInBST(TreeNode? root) {
    _minDiff = 0x7fffffff;
    _prev = null;
    _inorder(root);
    return _minDiff;
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
func minDiffInBST(root *TreeNode) int {
	const INF = int(^uint(0) >> 1)
	minDiff := INF
	var prevVal int
	hasPrev := false

	var inorder func(node *TreeNode)
	inorder = func(node *TreeNode) {
		if node == nil {
			return
		}
		inorder(node.Left)
		if hasPrev {
			diff := node.Val - prevVal
			if diff < minDiff {
				minDiff = diff
			}
		}
		prevVal = node.Val
		hasPrev = true
		inorder(node.Right)
	}

	inorder(root)
	return minDiff
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

def min_diff_in_bst(root)
  prev = nil
  min_diff = Float::INFINITY

  inorder = lambda do |node|
    return if node.nil?
    inorder.call(node.left)

    if !prev.nil?
      diff = node.val - prev
      min_diff = diff if diff < min_diff
    end
    prev = node.val

    inorder.call(node.right)
  end

  inorder.call(root)
  min_diff.to_i
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
    def minDiffInBST(root: TreeNode): Int = {
        var prev: Option[Int] = None
        var minDiff: Int = Int.MaxValue

        def inorder(node: TreeNode): Unit = {
            if (node == null) return
            inorder(node.left)

            prev match {
                case Some(p) =>
                    val diff = node.value - p
                    if (diff < minDiff) minDiff = diff
                case None => // first node, nothing to compare
            }
            prev = Some(node.value)

            inorder(node.right)
        }

        inorder(root)
        minDiff
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn min_diff_in_bst(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn inorder(node: &Option<Rc<RefCell<TreeNode>>>, prev: &mut Option<i32>, min_diff: &mut i32) {
            if let Some(rc_node) = node {
                let left = rc_node.borrow().left.clone();
                inorder(&left, prev, min_diff);
                let val = rc_node.borrow().val;
                if let Some(p) = *prev {
                    let diff = (val - p).abs();
                    if diff < *min_diff {
                        *min_diff = diff;
                    }
                }
                *prev = Some(val);
                let right = rc_node.borrow().right.clone();
                inorder(&right, prev, min_diff);
            }
        }

        let mut prev: Option<i32> = None;
        let mut ans = i32::MAX;
        inorder(&root, &mut prev, &mut ans);
        ans
    }
}
```

## Racket

```racket
; Definition for a binary tree node.
#|

; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))

|#

(define/contract (min-diff-in-bst root)
  (-> (or/c tree-node? #f) exact-integer?)
  (let ([INFINT 1000000]) ; sufficiently large sentinel
    (define (traverse node prev mindiff)
      (if (not node)
          (values prev mindiff)
          (let-values ([(prev1 mindiff1) (traverse (tree-node-left node) prev mindiff)])
            (define cur (tree-node-val node))
            (define new-mindiff
              (if prev1
                  (min mindiff1 (abs (- cur prev1)))
                  mindiff1))
            (let-values ([(prev2 mindiff2) (traverse (tree-node-right node) cur new-mindiff)])
              (values prev2 mindiff2)))))
    (define-values (_ result) (traverse root #f INFINT))
    result))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec min_diff_in_bst(Root :: #tree_node{} | null) -> integer().
min_diff_in_bst(Root) ->
    {_, MinDiff} = inorder(Root, undefined, 1000000),
    MinDiff.

inorder(null, Prev, Min) ->
    {Prev, Min};
inorder(#tree_node{val = V, left = L, right = R}, Prev, Min) ->
    {Prev1, Min1} = inorder(L, Prev, Min),
    NewMin = case Prev1 of
                undefined -> Min1;
                _ ->
                    Diff = V - Prev1,
                    if Diff < Min1 -> Diff; true -> Min1 end
            end,
    {Prev2, Min2} = inorder(R, V, NewMin),
    {Prev2, Min2}.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_diff_in_bst(root :: TreeNode.t() | nil) :: integer
  def min_diff_in_bst(root) do
    {_prev, min_diff} = inorder(root, nil, 1_000_000)
    min_diff
  end

  defp inorder(nil, prev, min_diff), do: {prev, min_diff}

  defp inorder(%TreeNode{left: left, val: val, right: right}, prev, min_diff) do
    # traverse left subtree
    {prev, min_diff} = inorder(left, prev, min_diff)

    # process current node
    {new_prev, new_min_diff} =
      case prev do
        nil -> {val, min_diff}
        _ ->
          diff = val - prev
          {val, if(diff < min_diff, do: diff, else: min_diff)}
      end

    # traverse right subtree
    inorder(right, new_prev, new_min_diff)
  end
end
```
