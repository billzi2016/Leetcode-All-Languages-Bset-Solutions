# 0654. Maximum Binary Tree

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
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        std::vector<TreeNode*> st;
        for (int v : nums) {
            TreeNode* cur = new TreeNode(v);
            while (!st.empty() && st.back()->val < v) {
                cur->left = st.back();
                st.pop_back();
            }
            if (!st.empty()) {
                st.back()->right = cur;
            }
            st.push_back(cur);
        }
        // The first element in the stack is the root
        return st.front();
    }
};
```

## Java

```java
import java.util.ArrayDeque;
import java.util.Deque;

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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode root = null;
        for (int num : nums) {
            TreeNode cur = new TreeNode(num);
            TreeNode leftChild = null;
            while (!stack.isEmpty() && stack.peek().val < num) {
                leftChild = stack.pop();
            }
            cur.left = leftChild;
            if (!stack.isEmpty()) {
                stack.peek().right = cur;
            } else {
                root = cur;
            }
            stack.push(cur);
        }
        return root;
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
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []
        for num in nums:
            node = TreeNode(num)
            # Attach smaller nodes as left children
            while stack and stack[-1].val < num:
                node.left = stack.pop()
            # The current node becomes the right child of the last larger element
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0] if stack else None
```

## Python3

```python
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(l: int, r: int) -> Optional[TreeNode]:
            if l >= r:
                return None
            # find index of max element in nums[l:r]
            max_idx = l
            for i in range(l + 1, r):
                if nums[i] > nums[max_idx]:
                    max_idx = i
            node = TreeNode(nums[max_idx])
            node.left = build(l, max_idx)
            node.right = build(max_idx + 1, r)
            return node

        return build(0, len(nums))
```

## C

```c
#include <stdlib.h>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
static struct TreeNode* build(int *nums, int l, int r) {
    if (l >= r) return NULL;
    int maxIdx = l;
    for (int i = l + 1; i < r; ++i) {
        if (nums[i] > nums[maxIdx]) maxIdx = i;
    }
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = nums[maxIdx];
    node->left = build(nums, l, maxIdx);
    node->right = build(nums, maxIdx + 1, r);
    return node;
}

struct TreeNode* constructMaximumBinaryTree(int* nums, int numsSize) {
    return build(nums, 0, numsSize);
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
    public TreeNode ConstructMaximumBinaryTree(int[] nums) {
        return Build(nums, 0, nums.Length);
    }

    private TreeNode Build(int[] nums, int l, int r) {
        if (l >= r) return null;

        // Find index of maximum element in [l, r)
        int maxIdx = l;
        for (int i = l + 1; i < r; i++) {
            if (nums[i] > nums[maxIdx]) {
                maxIdx = i;
            }
        }

        TreeNode node = new TreeNode(nums[maxIdx]);
        node.left = Build(nums, l, maxIdx);
        node.right = Build(nums, maxIdx + 1, r);
        return node;
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
 * @param {number[]} nums
 * @return {TreeNode}
 */
var constructMaximumBinaryTree = function(nums) {
    const stack = [];
    for (let i = 0; i < nums.length; i++) {
        const node = new TreeNode(nums[i]);
        while (stack.length && stack[stack.length - 1].val < node.val) {
            node.left = stack.pop();
        }
        if (stack.length) {
            stack[stack.length - 1].right = node;
        }
        stack.push(node);
    }
    return stack[0] || null;
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

function constructMaximumBinaryTree(nums: number[]): TreeNode | null {
    const n = nums.length;
    if (n === 0) return null;

    function build(l: number, r: number): TreeNode | null { // [l, r)
        if (l >= r) return null;
        let maxIdx = l;
        for (let i = l + 1; i < r; i++) {
            if (nums[i] > nums[maxIdx]) maxIdx = i;
        }
        const node = new TreeNode(nums[maxIdx]);
        node.left = build(l, maxIdx);
        node.right = build(maxIdx + 1, r);
        return node;
    }

    return build(0, n);
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
     * @param Integer[] $nums
     * @return TreeNode
     */
    function constructMaximumBinaryTree($nums) {
        return $this->build($nums, 0, count($nums));
    }

    private function build(&$nums, $l, $r) {
        if ($l >= $r) {
            return null;
        }
        $maxIdx = $l;
        for ($i = $l + 1; $i < $r; $i++) {
            if ($nums[$i] > $nums[$maxIdx]) {
                $maxIdx = $i;
            }
        }
        $node = new TreeNode($nums[$maxIdx]);
        $node->left = $this->build($nums, $l, $maxIdx);
        $node->right = $this->build($nums, $maxIdx + 1, $r);
        return $node;
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
    func constructMaximumBinaryTree(_ nums: [Int]) -> TreeNode? {
        return build(nums, 0, nums.count)
    }

    private func build(_ nums: [Int], _ l: Int, _ r: Int) -> TreeNode? {
        if l >= r { return nil }
        var maxIdx = l
        for i in (l + 1)..<r {
            if nums[i] > nums[maxIdx] {
                maxIdx = i
            }
        }
        let node = TreeNode(nums[maxIdx])
        node.left = build(nums, l, maxIdx)
        node.right = build(nums, maxIdx + 1, r)
        return node
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun constructMaximumBinaryTree(nums: IntArray): TreeNode? {
        return build(nums, 0, nums.size)
    }

    private fun build(nums: IntArray, left: Int, right: Int): TreeNode? {
        if (left >= right) return null
        var maxIdx = left
        for (i in left + 1 until right) {
            if (nums[i] > nums[maxIdx]) maxIdx = i
        }
        val node = TreeNode(nums[maxIdx])
        node.left = build(nums, left, maxIdx)
        node.right = build(nums, maxIdx + 1, right)
        return node
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
  TreeNode? constructMaximumBinaryTree(List<int> nums) {
    return _build(nums, 0, nums.length);
  }

  TreeNode? _build(List<int> nums, int left, int right) {
    if (left >= right) return null;
    int maxIdx = left;
    for (int i = left + 1; i < right; ++i) {
      if (nums[i] > nums[maxIdx]) maxIdx = i;
    }
    TreeNode node = TreeNode(nums[maxIdx]);
    node.left = _build(nums, left, maxIdx);
    node.right = _build(nums, maxIdx + 1, right);
    return node;
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
func constructMaximumBinaryTree(nums []int) *TreeNode {
    var build func(l, r int) *TreeNode
    build = func(l, r int) *TreeNode {
        if l >= r {
            return nil
        }
        maxIdx := l
        for i := l + 1; i < r; i++ {
            if nums[i] > nums[maxIdx] {
                maxIdx = i
            }
        }
        node := &TreeNode{Val: nums[maxIdx]}
        node.Left = build(l, maxIdx)
        node.Right = build(maxIdx+1, r)
        return node
    }
    return build(0, len(nums))
}
```

## Ruby

```ruby
def construct_maximum_binary_tree(nums)
  return nil if nums.empty?
  max_val = nums.max
  max_idx = nums.index(max_val)
  left_sub = nums[0...max_idx]
  right_sub = nums[(max_idx + 1)..-1] || []
  left_node = construct_maximum_binary_tree(left_sub)
  right_node = construct_maximum_binary_tree(right_sub)
  TreeNode.new(max_val, left_node, right_node)
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
  def constructMaximumBinaryTree(nums: Array[Int]): TreeNode = {
    def build(l: Int, r: Int): TreeNode = {
      if (l >= r) return null
      var maxIdx = l
      var i = l + 1
      while (i < r) {
        if (nums(i) > nums(maxIdx)) maxIdx = i
        i += 1
      }
      val node = new TreeNode(nums(maxIdx))
      node.left = build(l, maxIdx)
      node.right = build(maxIdx + 1, r)
      node
    }
    build(0, nums.length)
  }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn construct_maximum_binary_tree(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        fn build(nums: &[i32], l: usize, r: usize) -> Option<Rc<RefCell<TreeNode>>> {
            if l >= r {
                return None;
            }
            let mut max_i = l;
            for i in l + 1..r {
                if nums[i] > nums[max_i] {
                    max_i = i;
                }
            }
            let node = Rc::new(RefCell::new(TreeNode::new(nums[max_i])));
            let left = build(nums, l, max_i);
            let right = build(nums, max_i + 1, r);
            node.borrow_mut().left = left;
            node.borrow_mut().right = right;
            Some(node)
        }
        if nums.is_empty() {
            None
        } else {
            build(&nums, 0, nums.len())
        }
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (construct-maximum-binary-tree nums)
  (-> (listof exact-integer?) (or/c tree-node? #f))
  (if (null? nums)
      #f
      (let* ((max-val (apply max nums))
             (idx (let loop ((lst nums) (i 0))
                    (cond [(null? lst) -1]
                          [(= (car lst) max-val) i]
                          [else (loop (cdr lst) (+ i 1))])))
             (left-list (take nums idx))
             (right-list (drop nums (+ idx 1)))
             (node (make-tree-node max-val)))
        (set-tree-node-left! node (construct-maximum-binary-tree left-list))
        (set-tree-node-right! node (construct-maximum-binary-tree right-list))
        node)))
```

## Erlang

```erlang
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec construct_maximum_binary_tree(Nums :: [integer()]) -> #tree_node{} | null.
construct_maximum_binary_tree(Nums) ->
    build(Nums).

build([]) -> 
    null;
build(Nums) ->
    [First|Rest] = Nums,
    {Max, Index} = max_elem(Rest, 1, First, 0),
    LeftList = lists:sublist(Nums, Index),
    RightList = lists:nthtail(Index + 1, Nums),
    #tree_node{
        val = Max,
        left = build(LeftList),
        right = build(RightList)
    }.

max_elem([], _Pos, CurMax, CurIdx) ->
    {CurMax, CurIdx};
max_elem([H|T], Pos, CurMax, CurIdx) ->
    if H > CurMax ->
            max_elem(T, Pos + 1, H, Pos);
       true ->
            max_elem(T, Pos + 1, CurMax, CurIdx)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec construct_maximum_binary_tree(nums :: [integer]) :: TreeNode.t() | nil
  def construct_maximum_binary_tree(nums) do
    build(nums, 0, length(nums))
  end

  defp build(_nums, l, r) when l >= r, do: nil

  defp build(nums, l, r) do
    {max_i, max_val} =
      Enum.reduce(l..(r - 1), {l, Enum.at(nums, l)}, fn i, {mi, mv} ->
        v = Enum.at(nums, i)

        if v > mv do
          {i, v}
        else
          {mi, mv}
        end
      end)

    %TreeNode{
      val: max_val,
      left: build(nums, l, max_i),
      right: build(nums, max_i + 1, r)
    }
  end
end
```
