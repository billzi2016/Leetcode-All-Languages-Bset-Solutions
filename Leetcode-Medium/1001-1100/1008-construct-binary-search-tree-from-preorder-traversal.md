# 1008. Construct Binary Search Tree from Preorder Traversal

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
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        idx = 0;
        n = preorder.size();
        this->pre = &preorder;
        return build(LLONG_MIN, LLONG_MAX);
    }
private:
    int idx;
    int n;
    vector<int>* pre;
    
    TreeNode* build(long long lower, long long upper) {
        if (idx >= n) return nullptr;
        int val = (*pre)[idx];
        if (val < lower || val > upper) return nullptr;
        ++idx;
        TreeNode* node = new TreeNode(val);
        node->left = build(lower, (long long)val - 1);
        node->right = build((long long)val + 1, upper);
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
    private int index;

    public TreeNode bstFromPreorder(int[] preorder) {
        index = 0;
        return build(preorder, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private TreeNode build(int[] preorder, long lower, long upper) {
        if (index == preorder.length) {
            return null;
        }
        int val = preorder[index];
        if (val <= lower || val >= upper) {
            return null;
        }
        index++;
        TreeNode node = new TreeNode(val);
        node.left = build(preorder, lower, val);
        node.right = build(preorder, val, upper);
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
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.idx = 0
        n = len(preorder)
        INF = float('inf')
        
        def helper(lower, upper):
            if self.idx == n:
                return None
            val = preorder[self.idx]
            if not (lower < val < upper):
                return None
            self.idx += 1
            node = TreeNode(val)
            node.left = helper(lower, val)
            node.right = helper(val, upper)
            return node
        
        return helper(-INF, INF)
```

## Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional['TreeNode']:
        self.idx = 0
        n = len(preorder)

        def build(lower: int, upper: int):
            if self.idx == n:
                return None
            val = preorder[self.idx]
            if not (lower < val < upper):
                return None
            self.idx += 1
            node = TreeNode(val)
            node.left = build(lower, val)
            node.right = build(val, upper)
            return node

        return build(float('-inf'), float('inf'))
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
#include <stdlib.h>
#include <limits.h>

static int curIdx;

static struct TreeNode* build(int *preorder, int size, long lower, long upper) {
    if (curIdx >= size)
        return NULL;
    int val = preorder[curIdx];
    if ((long)val <= lower || (long)val >= upper)
        return NULL;
    
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = val;
    curIdx++;
    node->left  = build(preorder, size, lower, (long)val);
    node->right = build(preorder, size, (long)val, upper);
    return node;
}

struct TreeNode* bstFromPreorder(int* preorder, int preorderSize) {
    curIdx = 0;
    return build(preorder, preorderSize, LONG_MIN, LONG_MAX);
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
    public TreeNode BstFromPreorder(int[] preorder) {
        int index = 0;
        TreeNode Build(long min, long max) {
            if (index == preorder.Length) return null;
            int val = preorder[index];
            if (val <= min || val >= max) return null;
            index++;
            var node = new TreeNode(val);
            node.left = Build(min, val);
            node.right = Build(val, max);
            return node;
        }
        return Build(long.MinValue, long.MaxValue);
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
 * @param {number[]} preorder
 * @return {TreeNode}
 */
var bstFromPreorder = function(preorder) {
    let idx = 0;
    const n = preorder.length;
    
    function build(min, max) {
        if (idx === n) return null;
        const val = preorder[idx];
        if (val < min || val > max) return null;
        idx++;
        const node = new TreeNode(val);
        node.left = build(min, val);
        node.right = build(val, max);
        return node;
    }
    
    return build(-Infinity, Infinity);
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

function bstFromPreorder(preorder: number[]): TreeNode | null {
    let idx = 0;
    const n = preorder.length;

    function build(lower: number, upper: number): TreeNode | null {
        if (idx === n) return null;
        const val = preorder[idx];
        if (val <= lower || val >= upper) return null;
        idx++;
        const node = new TreeNode(val);
        node.left = build(lower, val);
        node.right = build(val, upper);
        return node;
    }

    return build(-Infinity, Infinity);
};
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
    private $preorder = [];
    private $idx = 0;
    private $n = 0;

    /**
     * @param Integer[] $preorder
     * @return TreeNode|null
     */
    function bstFromPreorder($preorder) {
        $this->preorder = $preorder;
        $this->idx = 0;
        $this->n = count($preorder);
        return $this->build(-INF, INF);
    }

    private function build($lower, $upper) {
        if ($this->idx >= $this->n) {
            return null;
        }
        $val = $this->preorder[$this->idx];
        if ($val <= $lower || $val >= $upper) {
            return null;
        }
        $node = new TreeNode($val);
        $this->idx++;
        $node->left = $this->build($lower, $val);
        $node->right = $this->build($val, $upper);
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
    private var preorder: [Int] = []
    private var index: Int = 0

    func bstFromPreorder(_ preorder: [Int]) -> TreeNode? {
        self.preorder = preorder
        self.index = 0
        return build(lower: Int.min, upper: Int.max)
    }

    private func build(lower: Int, upper: Int) -> TreeNode? {
        if index >= preorder.count { return nil }
        let val = preorder[index]
        if val <= lower || val >= upper { return nil }
        index += 1
        let node = TreeNode(val)
        node.left = build(lower: lower, upper: val)
        node.right = build(lower: val, upper: upper)
        return node
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
    private var index = 0

    fun bstFromPreorder(preorder: IntArray): TreeNode? {
        index = 0
        return build(preorder, Long.MIN_VALUE, Long.MAX_VALUE)
    }

    private fun build(preorder: IntArray, lower: Long, upper: Long): TreeNode? {
        if (index >= preorder.size) return null
        val value = preorder[index].toLong()
        if (value < lower || value > upper) return null

        index++
        val node = TreeNode(value.toInt())
        node.left = build(preorder, lower, value - 1)
        node.right = build(preorder, value + 1, upper)
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
  int _idx = 0;

  TreeNode? _build(List<int> preorder, int lower, int upper) {
    if (_idx >= preorder.length) return null;
    int val = preorder[_idx];
    if (val < lower || val > upper) return null;
    _idx++;
    TreeNode node = TreeNode(val);
    node.left = _build(preorder, lower, val - 1);
    node.right = _build(preorder, val + 1, upper);
    return node;
  }

  TreeNode? bstFromPreorder(List<int> preorder) {
    if (preorder.isEmpty) return null;
    _idx = 0;
    // Values are in [1, 1000] per constraints.
    return _build(preorder, -1, 1001);
  }
}
```

## Golang

```go
package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func bstFromPreorder(preorder []int) *TreeNode {
	idx := 0
	var build func(bound int) *TreeNode
	build = func(bound int) *TreeNode {
		if idx >= len(preorder) || preorder[idx] > bound {
			return nil
		}
		val := preorder[idx]
		idx++
		node := &TreeNode{Val: val}
		node.Left = build(val)
		node.Right = build(bound)
		return node
	}
	return build(math.MaxInt32)
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

def bst_from_preorder(preorder)
  @idx = 0
  build = lambda do |low, high|
    return nil if @idx >= preorder.size
    val = preorder[@idx]
    return nil unless low < val && val < high
    @idx += 1
    node = TreeNode.new(val)
    node.left = build.call(low, val)
    node.right = build.call(val, high)
    node
  end
  build.call(-Float::INFINITY, Float::INFINITY)
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
    def bstFromPreorder(preorder: Array[Int]): TreeNode = {
        var idx = 0
        val n = preorder.length

        def build(lower: Long, upper: Long): TreeNode = {
            if (idx >= n) return null
            val v = preorder(idx)
            if (v < lower || v > upper) return null
            idx += 1
            val node = new TreeNode(v)
            node.left = build(lower, v.toLong - 1)
            node.right = build(v.toLong + 1, upper)
            node
        }

        build(Long.MinValue, Long.MaxValue)
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
    pub fn bst_from_preorder(preorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        fn build(preorder: &[i32], lower: i32, upper: i32, idx: &mut usize) -> Option<Rc<RefCell<TreeNode>>> {
            if *idx >= preorder.len() {
                return None;
            }
            let val = preorder[*idx];
            if !(lower < val && val < upper) {
                return None;
            }
            *idx += 1;
            let left = build(preorder, lower, val, idx);
            let right = build(preorder, val, upper, idx);
            Some(Rc::new(RefCell::new(TreeNode { val, left, right })))
        }

        let mut i = 0;
        build(&preorder, i32::MIN, i32::MAX, &mut i)
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

(define/contract (bst-from-preorder preorder)
  (-> (listof exact-integer?) (or/c tree-node? #f))
  (if (null? preorder)
      #f
      (let* ((len (length preorder))
             (idx (box 0)))
        (define (build bound)
          (if (or (>= (unbox idx) len)
                  (> (list-ref preorder (unbox idx)) bound))
              #f
              (let* ((val (list-ref preorder (unbox idx)))
                     (node (make-tree-node val)))
                (set-box! idx (+ (unbox idx) 1))
                (let ((left (build val))
                      (right (build bound)))
                  (set-tree-node-left! node left)
                  (set-tree-node-right! node right)
                  node))))
        (define max-bound (+ (apply max preorder) 1))
        (build max-bound))))
```

## Erlang

```erlang
-module(solution).
-export([bst_from_preorder/1]).

-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec bst_from_preorder(Preorder :: [integer()]) -> #tree_node{} | null.
bst_from_preorder(Preorder) ->
    {Root, _} = build(Preorder, 1000000),
    Root.

build([], _) ->
    {null, []};
build([Val|Rest] = All, Upper) when Val > Upper ->
    {null, All};
build([Val|Rest], Upper) ->
    {LeftNode, Rest1} = build(Rest, Val),
    {RightNode, Rest2} = build(Rest1, Upper),
    {#tree_node{val = Val, left = LeftNode, right = RightNode}, Rest2}.
```

## Elixir

```elixir
defmodule Solution do
  @spec bst_from_preorder(preorder :: [integer]) :: TreeNode.t() | nil
  def bst_from_preorder(preorder) do
    {root, _} = build(preorder, 0, -1_000_000, 1_000_000)
    root
  end

  defp build(_preorder, idx, _lower, _upper) when idx >= length(_preorder), do: {nil, idx}

  defp build(preorder, idx, lower, upper) do
    val = Enum.at(preorder, idx)

    if val < lower or val > upper do
      {nil, idx}
    else
      {left_child, next_idx} = build(preorder, idx + 1, lower, val - 1)
      {right_child, final_idx} = build(preorder, next_idx, val + 1, upper)

      {%TreeNode{val: val, left: left_child, right: right_child}, final_idx}
    end
  end
end
```
