# 0108. Convert Sorted Array to Binary Search Tree

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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return build(nums, 0, (int)nums.size() - 1);
    }
private:
    TreeNode* build(const vector<int>& nums, int l, int r) {
        if (l > r) return nullptr;
        int m = l + (r - l) / 2;
        TreeNode* node = new TreeNode(nums[m]);
        node->left = build(nums, l, m - 1);
        node->right = build(nums, m + 1, r);
        return node;
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
    public TreeNode sortedArrayToBST(int[] nums) {
        return build(nums, 0, nums.length - 1);
    }

    private TreeNode build(int[] nums, int left, int right) {
        if (left > right) {
            return null;
        }
        int mid = left + (right - left) / 2;
        TreeNode node = new TreeNode(nums[mid]);
        node.left = build(nums, left, mid - 1);
        node.right = build(nums, mid + 1, right);
        return node;
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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(nums[mid])
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(nums) - 1)
```

## Python3

```python
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(nums[mid])
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(nums) - 1)
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

static struct TreeNode* buildBST(int *nums, int left, int right) {
    if (left > right) return NULL;
    int mid = left + (right - left) / 2;
    struct TreeNode *node = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    node->val = nums[mid];
    node->left = buildBST(nums, left, mid - 1);
    node->right = buildBST(nums, mid + 1, right);
    return node;
}

struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    if (numsSize == 0) return NULL;
    return buildBST(nums, 0, numsSize - 1);
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
    public TreeNode SortedArrayToBST(int[] nums)
    {
        return Build(nums, 0, nums.Length - 1);
    }

    private TreeNode Build(int[] nums, int left, int right)
    {
        if (left > right) return null;
        int mid = left + (right - left) / 2;
        TreeNode node = new TreeNode(nums[mid]);
        node.left = Build(nums, left, mid - 1);
        node.right = Build(nums, mid + 1, right);
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
var sortedArrayToBST = function(nums) {
    const build = (l, r) => {
        if (l > r) return null;
        const mid = Math.floor((l + r) / 2);
        const node = new TreeNode(nums[mid]);
        node.left = build(l, mid - 1);
        node.right = build(mid + 1, r);
        return node;
    };
    return build(0, nums.length - 1);
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

function sortedArrayToBST(nums: number[]): TreeNode | null {
    const build = (l: number, r: number): TreeNode | null => {
        if (l > r) return null;
        const mid = Math.floor((l + r) / 2);
        const node = new TreeNode(nums[mid]);
        node.left = build(l, mid - 1);
        node.right = build(mid + 1, r);
        return node;
    };
    return build(0, nums.length - 1);
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
     * @return TreeNode|null
     */
    function sortedArrayToBST($nums) {
        return $this->buildTree($nums, 0, count($nums) - 1);
    }

    private function buildTree($nums, $left, $right) {
        if ($left > $right) {
            return null;
        }
        $mid = intdiv($left + $right, 2);
        $node = new TreeNode($nums[$mid]);
        $node->left = $this->buildTree($nums, $left, $mid - 1);
        $node->right = $this->buildTree($nums, $mid + 1, $right);
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
    func sortedArrayToBST(_ nums: [Int]) -> TreeNode? {
        func build(_ left: Int, _ right: Int) -> TreeNode? {
            if left > right { return nil }
            let mid = left + (right - left) / 2
            let node = TreeNode(nums[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node
        }
        return build(0, nums.count - 1)
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
    fun sortedArrayToBST(nums: IntArray): TreeNode? {
        if (nums.isEmpty()) return null

        fun build(left: Int, right: Int): TreeNode? {
            if (left > right) return null
            val mid = left + (right - left) / 2
            val node = TreeNode(nums[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node
        }

        return build(0, nums.lastIndex)
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
  TreeNode? sortedArrayToBST(List<int> nums) {
    TreeNode? build(int left, int right) {
      if (left > right) return null;
      int mid = (left + right) ~/ 2;
      var node = TreeNode(nums[mid]);
      node.left = build(left, mid - 1);
      node.right = build(mid + 1, right);
      return node;
    }

    return build(0, nums.length - 1);
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
func sortedArrayToBST(nums []int) *TreeNode {
    var build func(int, int) *TreeNode
    build = func(l, r int) *TreeNode {
        if l > r {
            return nil
        }
        mid := (l + r) / 2
        node := &TreeNode{Val: nums[mid]}
        node.Left = build(l, mid-1)
        node.Right = build(mid+1, r)
        return node
    }
    return build(0, len(nums)-1)
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

def sorted_array_to_bst(nums)
  build(nums, 0, nums.length - 1)
end

def build(nums, left, right)
  return nil if left > right
  mid = (left + right) / 2
  node = TreeNode.new(nums[mid])
  node.left = build(nums, left, mid - 1)
  node.right = build(nums, mid + 1, right)
  node
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
    def sortedArrayToBST(nums: Array[Int]): TreeNode = {
        def helper(l: Int, r: Int): TreeNode = {
            if (l > r) return null
            val mid = l + (r - l) / 2
            val node = new TreeNode(nums(mid))
            node.left = helper(l, mid - 1)
            node.right = helper(mid + 1, r)
            node
        }
        helper(0, nums.length - 1)
    }
}
```

## Rust

```rust
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        fn build(slice: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
            if slice.is_empty() {
                return None;
            }
            let mid = slice.len() / 2;
            let node = Rc::new(RefCell::new(TreeNode::new(slice[mid])));
            node.borrow_mut().left = build(&slice[..mid]);
            node.borrow_mut().right = build(&slice[mid + 1..]);
            Some(node)
        }
        build(&nums)
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

(define/contract (sorted-array-to-bst nums)
  (-> (listof exact-integer?) (or/c tree-node? #f))
  (let* ((vec (list->vector nums))
         (n   (vector-length vec)))
    (letrec ((build
              (lambda (l r)
                (if (>= l r)
                    #f
                    (let* ((mid  (quotient (+ l r) 2))
                           (node (make-tree-node (vector-ref vec mid))))
                      (set-tree-node-left! node (build l mid))
                      (set-tree-node-right! node (build (add1 mid) r))
                      node)))))
      (build 0 n))))
```

## Erlang

```erlang
-define(null,null).
-record(tree_node,{val=0,left=null,right=null}).

-spec sorted_array_to_bst([integer()]) -> #tree_node{} | null.
sorted_array_to_bst(Nums) ->
    case Nums of
        [] -> ?null;
        _ ->
            Tuple = list_to_tuple(Nums),
            Len = tuple_size(Tuple),
            build(Tuple, 1, Len)
    end.

build(_Tuple, Low, High) when Low > High -> ?null;
build(Tuple, Low, High) ->
    Mid = (Low + High) div 2,
    Val = element(Mid, Tuple),
    Left = build(Tuple, Low, Mid - 1),
    Right = build(Tuple, Mid + 1, High),
    #tree_node{val=Val, left=Left, right=Right}.
```

## Elixir

```elixir
defmodule Solution do
  @spec sorted_array_to_bst(nums :: [integer]) :: TreeNode.t() | nil
  def sorted_array_to_bst(nums) do
    arr = List.to_tuple(nums)
    helper(arr, 0, tuple_size(arr) - 1)
  end

  defp helper(_arr, l, r) when l > r, do: nil

  defp helper(arr, l, r) do
    m = div(l + r, 2)

    %TreeNode{
      val: elem(arr, m),
      left: helper(arr, l, m - 1),
      right: helper(arr, m + 1, r)
    }
  end
end
```
