# 2415. Reverse Odd Levels of Binary Tree

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
    TreeNode* reverseOddLevels(TreeNode* root) {
        if (!root) return nullptr;
        dfs(root->left, root->right, 1);
        return root;
    }
private:
    void dfs(TreeNode* left, TreeNode* right, int level) {
        if (!left || !right) return;
        if (level % 2 == 1) {
            std::swap(left->val, right->val);
        }
        dfs(left->left, right->right, level + 1);
        dfs(left->right, right->left, level + 1);
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
    public TreeNode reverseOddLevels(TreeNode root) {
        if (root == null) return null;
        dfs(root.left, root.right, 0);
        return root;
    }

    private void dfs(TreeNode left, TreeNode right, int level) {
        if (left == null || right == null) return;
        // level 0 corresponds to depth 1 (odd), so swap when level is even
        if (level % 2 == 0) {
            int tmp = left.val;
            left.val = right.val;
            right.val = tmp;
        }
        dfs(left.left, right.right, level + 1);
        dfs(left.right, right.left, level + 1);
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
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None

        def dfs(left, right, depth):
            if not left or not right:
                return
            # depth 0 corresponds to level 1 (odd), so swap on even depths
            if depth % 2 == 0:
                left.val, right.val = right.val, left.val
            dfs(left.left, right.right, depth + 1)
            dfs(left.right, right.left, depth + 1)

        dfs(root.left, root.right, 0)
        return root
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
    def reverseOddLevels(self, root: Optional['TreeNode']) -> Optional['TreeNode']:
        if not root:
            return None

        def dfs(left: 'TreeNode', right: 'TreeNode', depth: int) -> None:
            if not left or not right:
                return
            # depth 0 corresponds to level 1 (odd), so swap on even depths
            if depth % 2 == 0:
                left.val, right.val = right.val, left.val
            dfs(left.left, right.right, depth + 1)
            dfs(left.right, right.left, depth + 1)

        dfs(root.left, root.right, 0)
        return root
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
static void dfs(struct TreeNode* left, struct TreeNode* right, int level) {
    if (!left || !right) return;
    if (level % 2 == 1) {
        int tmp = left->val;
        left->val = right->val;
        right->val = tmp;
    }
    dfs(left->left, right->right, level + 1);
    dfs(left->right, right->left, level + 1);
}

struct TreeNode* reverseOddLevels(struct TreeNode* root) {
    if (!root) return NULL;
    dfs(root->left, root->right, 1);
    return root;
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
    public TreeNode ReverseOddLevels(TreeNode root) {
        if (root == null) return null;
        DFS(root.left, root.right, 0);
        return root;
    }

    private void DFS(TreeNode left, TreeNode right, int depth) {
        if (left == null || right == null) return;
        // depth 0 corresponds to level 1 (odd), so swap when depth is even
        if (depth % 2 == 0) {
            int tmp = left.val;
            left.val = right.val;
            right.val = tmp;
        }
        DFS(left.left, right.right, depth + 1);
        DFS(left.right, right.left, depth + 1);
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
 * @return {TreeNode}
 */
var reverseOddLevels = function(root) {
    if (!root) return null;
    
    const dfs = (leftNode, rightNode, depth) => {
        if (!leftNode || !rightNode) return;
        if (depth % 2 === 1) {
            const tmp = leftNode.val;
            leftNode.val = rightNode.val;
            rightNode.val = tmp;
        }
        dfs(leftNode.left, rightNode.right, depth + 1);
        dfs(leftNode.right, rightNode.left, depth + 1);
    };
    
    dfs(root.left, root.right, 1);
    return root;
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

function reverseOddLevels(root: TreeNode | null): TreeNode | null {
    if (!root) return null;

    const dfs = (node1: TreeNode | null, node2: TreeNode | null, level: number): void => {
        if (!node1 || !node2) return;
        if (level % 2 === 1) {
            const tmp = node1.val;
            node1.val = node2.val;
            node2.val = tmp;
        }
        dfs(node1.left, node2.right, level + 1);
        dfs(node1.right, node2.left, level + 1);
    };

    dfs(root.left, root.right, 1);
    return root;
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
     * @return TreeNode
     */
    function reverseOddLevels($root) {
        if ($root === null) {
            return null;
        }
        $this->dfs($root->left, $root->right, 0);
        return $root;
    }

    private function dfs($node1, $node2, $depth) {
        if ($node1 === null || $node2 === null) {
            return;
        }
        // depth 0 corresponds to level 1 (odd), so swap when depth is even
        if ($depth % 2 == 0) {
            $tmp = $node1->val;
            $node1->val = $node2->val;
            $node2->val = $tmp;
        }
        $this->dfs($node1->left, $node2->right, $depth + 1);
        $this->dfs($node1->right, $node2->left, $depth + 1);
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
    func reverseOddLevels(_ root: TreeNode?) -> TreeNode? {
        guard let root = root else { return nil }
        dfs(root.left, root.right, 0)
        return root
    }
    
    private func dfs(_ left: TreeNode?, _ right: TreeNode?, _ level: Int) {
        guard let l = left, let r = right else { return }
        if level % 2 == 0 {
            let temp = l.val
            l.val = r.val
            r.val = temp
        }
        dfs(l.left, r.right, level + 1)
        dfs(l.right, r.left, level + 1)
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
    fun reverseOddLevels(root: TreeNode?): TreeNode? {
        if (root == null) return null
        dfs(root.left, root.right, 0)
        return root
    }

    private fun dfs(left: TreeNode?, right: TreeNode?, level: Int) {
        if (left == null || right == null) return
        // level 0 corresponds to nodes at depth 1 (odd level), so swap on even 'level'
        if (level % 2 == 0) {
            val tmp = left.`val`
            left.`val` = right.`val`
            right.`val` = tmp
        }
        dfs(left.left, right.right, level + 1)
        dfs(left.right, right.left, level + 1)
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
  TreeNode? reverseOddLevels(TreeNode? root) {
    if (root == null) return null;

    void dfs(TreeNode? left, TreeNode? right, int level) {
      if (left == null || right == null) return;
      // level is the distance from the root's children; even level => odd tree level
      if (level % 2 == 0) {
        int tmp = left.val;
        left.val = right.val;
        right.val = tmp;
      }
      dfs(left.left, right.right, level + 1);
      dfs(left.right, right.left, level + 1);
    }

    dfs(root.left, root.right, 0);
    return root;
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
func reverseOddLevels(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	var dfs func(l, r *TreeNode, depth int)
	dfs = func(l, r *TreeNode, depth int) {
		if l == nil || r == nil {
			return
		}
		// depth 0 corresponds to tree level 1 (odd), so swap on even depths.
		if depth%2 == 0 {
			l.Val, r.Val = r.Val, l.Val
		}
		dfs(l.Left, r.Right, depth+1)
		dfs(l.Right, r.Left, depth+1)
	}
	dfs(root.Left, root.Right, 0)
	return root
}
```

## Ruby

```ruby
def reverse_odd_levels(root)
  return root if root.nil?

  dfs = nil
  dfs = lambda do |left, right, level|
    return if left.nil? || right.nil?
    if level.even?
      left.val, right.val = right.val, left.val
    end
    dfs.call(left.left, right.right, level + 1)
    dfs.call(left.right, right.left, level + 1)
  end

  dfs.call(root.left, root.right, 0)
  root
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
    def reverseOddLevels(root: TreeNode): TreeNode = {
        def dfs(l: TreeNode, r: TreeNode, depth: Int): Unit = {
            if (l == null || r == null) return
            if (depth % 2 == 1) {
                val tmp = l.value
                l.value = r.value
                r.value = tmp
            }
            dfs(l.left, r.right, depth + 1)
            dfs(l.right, r.left, depth + 1)
        }
        if (root != null) dfs(root.left, root.right, 1)
        root
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn reverse_odd_levels(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        fn dfs(left: Option<Rc<RefCell<TreeNode>>>, right: Option<Rc<RefCell<TreeNode>>>, depth: i32) {
            if left.is_none() || right.is_none() {
                return;
            }
            let l = left.unwrap();
            let r = right.unwrap();

            if depth % 2 == 1 {
                let mut l_borrow = l.borrow_mut();
                let mut r_borrow = r.borrow_mut();
                std::mem::swap(&mut l_borrow.val, &mut r_borrow.val);
            }

            let ll = l.borrow().left.clone();
            let rr = r.borrow().right.clone();
            dfs(ll, rr, depth + 1);

            let lr = l.borrow().right.clone();
            let rl = r.borrow().left.clone();
            dfs(lr, rl, depth + 1);
        }

        if root.is_none() {
            return root;
        }
        let left = root.as_ref().unwrap().borrow().left.clone();
        let right = root.as_ref().unwrap().borrow().right.clone();

        dfs(left, right, 0);

        root
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

;; helper: depth‑first traversal swapping values of symmetric nodes on odd levels
(define (dfs left right level)
  (when (and left right)
    (when (= (remainder level 2) 1)
      (let ((tmp (tree-node-val left)))
        (set-tree-node-val! left (tree-node-val right))
        (set-tree-node-val! right tmp)))
    (dfs (tree-node-left left) (tree-node-right right) (+ level 1))
    (dfs (tree-node-right left) (tree-node-left right) (+ level 1))))

(define/contract (reverse-odd-levels root)
  (-> (or/c tree-node? #f) (or/c tree-node? #f))
  (if (not root)
      #f
      (begin
        (dfs (tree-node-left root) (tree-node-right root) 1)
        root)))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec reverse_odd_levels(Root :: #tree_node{} | null) -> #tree_node{} | null.
reverse_odd_levels(null) ->
    null;
reverse_odd_levels(Root = #tree_node{left = L, right = R}) when L =/= null, R =/= null ->
    {NewL, NewR} = dfs(L, R, 0),
    Root#tree_node{left = NewL, right = NewR};
reverse_odd_levels(Root) ->
    %% root is a leaf (no children)
    Root.

%% dfs/3 traverses paired nodes and swaps values on odd levels.
-spec dfs(Left :: #tree_node{} | null,
          Right :: #tree_node{} | null,
          Level :: non_neg_integer()) -> {#tree_node{} | null, #tree_node{} | null}.
dfs(null, _, _) ->
    {null, null};
dfs(_, null, _) ->
    {null, null};
dfs(Left, Right, Level) ->
    %% Swap values when current level is even (which corresponds to odd depth).
    {SwappedL, SwappedR} =
        case Level rem 2 of
            0 ->
                ValL = Left#tree_node.val,
                ValR = Right#tree_node.val,
                {Left#tree_node{val = ValR}, Right#tree_node{val = ValL}};
            _ ->
                {Left, Right}
        end,

    %% Recurse on children in mirrored order.
    {NewLL, NewRR} = dfs(SwappedL#tree_node.left, SwappedR#tree_node.right, Level + 1),
    {NewLR, NewRL} = dfs(SwappedL#tree_node.right, SwappedR#tree_node.left, Level + 1),

    %% Reconstruct nodes with updated children.
    FinalLeft  = SwappedL#tree_node{left = NewLL, right = NewLR},
    FinalRight = SwappedR#tree_node{left = NewRL, right = NewRR},
    {FinalLeft, FinalRight}.
```

## Elixir

```elixir
defmodule Solution do
  @spec reverse_odd_levels(root :: TreeNode.t() | nil) :: TreeNode.t() | nil
  def reverse_odd_levels(nil), do: nil

  def reverse_odd_levels(root) do
    {new_left, new_right} = dfs(root.left, root.right, 1)
    %{root | left: new_left, right: new_right}
  end

  defp dfs(nil, _right, _level), do: {nil, nil}
  defp dfs(_left, nil, _level), do: {nil, nil}

  defp dfs(left, right, level) do
    {l_swapped, r_swapped} =
      if rem(level, 2) == 1 do
        l_val = left.val
        r_val = right.val
        {%{left | val: r_val}, %{right | val: l_val}}
      else
        {left, right}
      end

    {ll, rr} = dfs(l_swapped.left, r_swapped.right, level + 1)
    {lr, rl} = dfs(l_swapped.right, r_swapped.left, level + 1)

    final_left = %{l_swapped | left: ll, right: lr}
    final_right = %{r_swapped | left: rl, right: rr}

    {final_left, final_right}
  end
end
```
