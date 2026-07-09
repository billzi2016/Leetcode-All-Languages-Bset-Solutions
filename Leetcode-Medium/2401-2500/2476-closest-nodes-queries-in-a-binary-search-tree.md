# 2476. Closest Nodes Queries in a Binary Search Tree

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
    vector<vector<int>> closestNodes(TreeNode* root, vector<int>& queries) {
        // Inorder traversal to get sorted values
        vector<int> vals;
        vector<TreeNode*> stk;
        TreeNode* cur = root;
        while (cur || !stk.empty()) {
            while (cur) {
                stk.push_back(cur);
                cur = cur->left;
            }
            cur = stk.back();
            stk.pop_back();
            vals.push_back(cur->val);
            cur = cur->right;
        }

        vector<vector<int>> ans;
        ans.reserve(queries.size());
        for (int q : queries) {
            // floor: largest <= q
            auto up = upper_bound(vals.begin(), vals.end(), q);
            int floorVal = -1;
            if (up != vals.begin()) {
                floorVal = *(up - 1);
            }
            // ceil: smallest >= q
            auto low = lower_bound(vals.begin(), vals.end(), q);
            int ceilVal = -1;
            if (low != vals.end()) {
                ceilVal = *low;
            }
            ans.push_back({floorVal, ceilVal});
        }
        return ans;
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
    public List<List<Integer>> closestNodes(TreeNode root, List<Integer> queries) {
        // Inorder traversal to get sorted values
        List<Integer> valsList = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode cur = root;
        while (cur != null || !stack.isEmpty()) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            valsList.add(cur.val);
            cur = cur.right;
        }

        int n = valsList.size();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = valsList.get(i);
        }

        List<List<Integer>> answer = new ArrayList<>(queries.size());
        for (int q : queries) {
            int idx = java.util.Arrays.binarySearch(arr, q);
            int floor, ceil;
            if (idx >= 0) { // exact match
                floor = arr[idx];
                ceil = arr[idx];
            } else {
                int insertPos = -idx - 1; // first element greater than q
                ceil = (insertPos < n) ? arr[insertPos] : -1;
                floor = (insertPos > 0) ? arr[insertPos - 1] : -1;
            }
            List<Integer> pair = new ArrayList<>(2);
            pair.add(floor);
            pair.add(ceil);
            answer.add(pair);
        }

        return answer;
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
import bisect

class Solution(object):
    def closestNodes(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[List[int]]
        """
        # Inorder traversal to get sorted values
        vals = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            vals.append(node.val)
            node = node.right

        ans = []
        n = len(vals)
        for q in queries:
            # floor (largest <= q)
            i = bisect.bisect_right(vals, q)
            floor_val = vals[i-1] if i > 0 else -1
            # ceil (smallest >= q)
            j = bisect.bisect_left(vals, q)
            ceil_val = vals[j] if j < n else -1
            ans.append([floor_val, ceil_val])
        return ans
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
import bisect

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # Inorder traversal to get sorted values
        vals = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            vals.append(node.val)
            node = node.right

        ans = []
        n = len(vals)
        for q in queries:
            # ceil: smallest >= q
            idx_ceil = bisect.bisect_left(vals, q)
            ceil_val = vals[idx_ceil] if idx_ceil < n else -1

            # floor: largest <= q
            idx_floor = bisect.bisect_right(vals, q) - 1
            floor_val = vals[idx_floor] if idx_floor >= 0 else -1

            ans.append([floor_val, ceil_val])
        return ans
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
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** closestNodes(struct TreeNode* root, int* queries, int queriesSize, int* returnSize, int** returnColumnSizes) {
    if (!root) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    // Maximum possible nodes as per constraints
    const int MAX_NODES = 100000 + 5;

    // Inorder traversal to get sorted values
    int *vals = (int *)malloc(sizeof(int) * MAX_NODES);
    int valCount = 0;

    struct TreeNode **stack = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * MAX_NODES);
    int top = 0;
    struct TreeNode *cur = root;

    while (cur || top > 0) {
        while (cur) {
            stack[top++] = cur;
            cur = cur->left;
        }
        cur = stack[--top];
        vals[valCount++] = cur->val;
        cur = cur->right;
    }

    // Prepare result containers
    int **result = (int **)malloc(sizeof(int *) * queriesSize);
    *returnColumnSizes = (int *)malloc(sizeof(int) * queriesSize);
    *returnSize = queriesSize;

    for (int i = 0; i < queriesSize; ++i) {
        int q = queries[i];
        // Find floor (largest <= q)
        int l = 0, r = valCount - 1;
        int floorVal = -1;
        while (l <= r) {
            int m = l + ((r - l) >> 1);
            if (vals[m] <= q) {
                floorVal = vals[m];
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        // Find ceil (smallest >= q)
        l = 0; r = valCount - 1;
        int ceilVal = -1;
        while (l <= r) {
            int m = l + ((r - l) >> 1);
            if (vals[m] >= q) {
                ceilVal = vals[m];
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        int *pair = (int *)malloc(sizeof(int) * 2);
        pair[0] = floorVal;
        pair[1] = ceilVal;
        result[i] = pair;
        (*returnColumnSizes)[i] = 2;
    }

    free(vals);
    free(stack);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> ClosestNodes(TreeNode root, IList<int> queries) {
        // Inorder traversal to get sorted values
        List<int> vals = new List<int>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode curr = root;
        while (curr != null || stack.Count > 0) {
            while (curr != null) {
                stack.Push(curr);
                curr = curr.left;
            }
            curr = stack.Pop();
            vals.Add(curr.val);
            curr = curr.right;
        }

        IList<IList<int>> answer = new List<IList<int>>(queries.Count);
        foreach (int q in queries) {
            int floor = -1, ceil = -1;

            // Find floor (largest <= q)
            int left = 0, right = vals.Count - 1;
            while (left <= right) {
                int mid = left + ((right - left) >> 1);
                if (vals[mid] <= q) {
                    floor = vals[mid];
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }

            // Find ceil (smallest >= q)
            left = 0; right = vals.Count - 1;
            while (left <= right) {
                int mid = left + ((right - left) >> 1);
                if (vals[mid] >= q) {
                    ceil = vals[mid];
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }

            answer.Add(new List<int> { floor, ceil });
        }

        return answer;
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
 * @param {number[]} queries
 * @return {number[][]}
 */
var closestNodes = function(root, queries) {
    // Inorder traversal to get sorted values
    const vals = [];
    const stack = [];
    let node = root;
    while (stack.length || node) {
        while (node) {
            stack.push(node);
            node = node.left;
        }
        node = stack.pop();
        vals.push(node.val);
        node = node.right;
    }

    // binary search: first index with value >= target
    const lowerBound = (arr, target) => {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] < target) l = m + 1;
            else r = m;
        }
        return l;
    };

    const ans = [];
    for (const q of queries) {
        const idx = lowerBound(vals, q);
        // ceil
        const ceil = idx < vals.length ? vals[idx] : -1;
        // floor
        let floor;
        if (idx === vals.length) {
            floor = vals[vals.length - 1];
        } else if (vals[idx] === q) {
            floor = vals[idx];
        } else {
            floor = idx > 0 ? vals[idx - 1] : -1;
        }
        ans.push([floor, ceil]);
    }
    return ans;
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

function closestNodes(root: TreeNode | null, queries: number[]): number[][] {
    const vals: number[] = [];
    // iterative inorder traversal to get sorted values
    const stack: TreeNode[] = [];
    let node = root;
    while (stack.length || node) {
        while (node) {
            stack.push(node);
            node = node.left;
        }
        node = stack.pop()!;
        vals.push(node.val);
        node = node.right;
    }

    const lowerBound = (arr: number[], target: number): number => {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] < target) l = m + 1;
            else r = m;
        }
        return l; // first index >= target
    };

    const upperBound = (arr: number[], target: number): number => {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] <= target) l = m + 1;
            else r = m;
        }
        return l; // first index > target
    };

    const ans: number[][] = [];
    for (const q of queries) {
        const ceilIdx = lowerBound(vals, q);
        const floorIdx = upperBound(vals, q) - 1;

        const ceil = ceilIdx < vals.length ? vals[ceilIdx] : -1;
        const floor = floorIdx >= 0 ? vals[floorIdx] : -1;
        ans.push([floor, ceil]);
    }
    return ans;
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
     * @param Integer[] $queries
     * @return Integer[][]
     */
    function closestNodes($root, $queries) {
        // Inorder traversal to get sorted values
        $sorted = [];
        $stack = [];
        $node = $root;
        while ($stack || $node !== null) {
            while ($node !== null) {
                $stack[] = $node;
                $node = $node->left;
            }
            $node = array_pop($stack);
            $sorted[] = $node->val;
            $node = $node->right;
        }

        $n = count($sorted);
        $ans = [];

        foreach ($queries as $q) {
            // Find floor (largest <= q)
            $l = 0;
            $r = $n - 1;
            $floorIdx = -1;
            while ($l <= $r) {
                $mid = intdiv($l + $r, 2);
                if ($sorted[$mid] <= $q) {
                    $floorIdx = $mid;
                    $l = $mid + 1;
                } else {
                    $r = $mid - 1;
                }
            }
            $floor = $floorIdx == -1 ? -1 : $sorted[$floorIdx];

            // Find ceil (smallest >= q)
            $l = 0;
            $r = $n - 1;
            $ceilIdx = -1;
            while ($l <= $r) {
                $mid = intdiv($l + $r, 2);
                if ($sorted[$mid] >= $q) {
                    $ceilIdx = $mid;
                    $r = $mid - 1;
                } else {
                    $l = $mid + 1;
                }
            }
            $ceil = $ceilIdx == -1 ? -1 : $sorted[$ceilIdx];

            $ans[] = [$floor, $ceil];
        }

        return $ans;
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
    func closestNodes(_ root: TreeNode?, _ queries: [Int]) -> [[Int]] {
        // Inorder traversal to get sorted values
        var sorted = [Int]()
        var stack = [TreeNode]()
        var node = root
        while node != nil || !stack.isEmpty {
            while let cur = node {
                stack.append(cur)
                node = cur.left
            }
            let cur = stack.removeLast()
            sorted.append(cur.val)
            node = cur.right
        }

        var answer = [[Int]]()
        for q in queries {
            // Find floor (largest <= q)
            var lo = 0, hi = sorted.count - 1
            var floorVal = -1
            while lo <= hi {
                let mid = (lo + hi) >> 1
                if sorted[mid] <= q {
                    floorVal = sorted[mid]
                    lo = mid + 1
                } else {
                    hi = mid - 1
                }
            }

            // Find ceil (smallest >= q)
            lo = 0; hi = sorted.count - 1
            var ceilVal = -1
            while lo <= hi {
                let mid = (lo + hi) >> 1
                if sorted[mid] >= q {
                    ceilVal = sorted[mid]
                    hi = mid - 1
                } else {
                    lo = mid + 1
                }
            }

            answer.append([floorVal, ceilVal])
        }
        return answer
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
    fun closestNodes(root: TreeNode?, queries: List<Int>): List<List<Int>> {
        // Inorder traversal to get sorted values
        val vals = mutableListOf<Int>()
        val stack = java.util.ArrayDeque<TreeNode>()
        var node = root
        while (node != null || !stack.isEmpty) {
            while (node != null) {
                stack.addFirst(node)
                node = node.left
            }
            node = stack.removeFirst()
            vals.add(node.`val`)
            node = node.right
        }
        val arr = vals.toIntArray()

        fun lowerBound(target: Int): Int {
            var l = 0
            var r = arr.size
            while (l < r) {
                val m = (l + r) ushr 1
                if (arr[m] < target) l = m + 1 else r = m
            }
            return l
        }

        fun upperBound(target: Int): Int {
            var l = 0
            var r = arr.size
            while (l < r) {
                val m = (l + r) ushr 1
                if (arr[m] <= target) l = m + 1 else r = m
            }
            return l
        }

        val result = ArrayList<List<Int>>(queries.size)
        for (q in queries) {
            val floorIdx = upperBound(q) - 1
            val floorVal = if (floorIdx >= 0) arr[floorIdx] else -1
            val ceilIdx = lowerBound(q)
            val ceilVal = if (ceilIdx < arr.size) arr[ceilIdx] else -1
            result.add(listOf(floorVal, ceilVal))
        }
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
  List<List<int>> closestNodes(TreeNode? root, List<int> queries) {
    // Inorder traversal to get sorted values
    List<int> sorted = [];
    List<TreeNode> stack = [];
    TreeNode? cur = root;
    while (cur != null || stack.isNotEmpty) {
      while (cur != null) {
        stack.add(cur);
        cur = cur.left;
      }
      cur = stack.removeLast();
      sorted.add(cur.val);
      cur = cur.right;
    }

    int lowerBound(int target) {
      int l = 0, r = sorted.length;
      while (l < r) {
        int m = (l + r) >> 1;
        if (sorted[m] < target) {
          l = m + 1;
        } else {
          r = m;
        }
      }
      return l;
    }

    List<List<int>> ans = [];
    for (int q in queries) {
      int idx = lowerBound(q);
      int floorVal, ceilVal;

      if (idx < sorted.length && sorted[idx] == q) {
        floorVal = ceilVal = q;
      } else {
        floorVal = (idx == 0) ? -1 : sorted[idx - 1];
        ceilVal = (idx == sorted.length) ? -1 : sorted[idx];
      }
      ans.add([floorVal, ceilVal]);
    }

    return ans;
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
import "sort"

func closestNodes(root *TreeNode, queries []int) [][]int {
    // Inorder traversal to get sorted values
    vals := make([]int, 0)
    stack := []*TreeNode{}
    cur := root
    for cur != nil || len(stack) > 0 {
        for cur != nil {
            stack = append(stack, cur)
            cur = cur.Left
        }
        node := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        vals = append(vals, node.Val)
        cur = node.Right
    }

    ans := make([][]int, len(queries))
    for i, q := range queries {
        // floor: largest value <= q
        idxUpper := sort.Search(len(vals), func(j int) bool { return vals[j] > q })
        floor := -1
        if idxUpper > 0 {
            floor = vals[idxUpper-1]
        }

        // ceil: smallest value >= q
        idxLower := sort.Search(len(vals), func(j int) bool { return vals[j] >= q })
        ceil := -1
        if idxLower < len(vals) {
            ceil = vals[idxLower]
        }

        ans[i] = []int{floor, ceil}
    }
    return ans
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

def closest_nodes(root, queries)
  # Inorder traversal to get sorted values
  vals = []
  stack = []
  node = root
  while node || !stack.empty?
    while node
      stack << node
      node = node.left
    end
    node = stack.pop
    vals << node.val
    node = node.right
  end

  n = vals.length
  result = []

  queries.each do |q|
    # Find ceil (smallest >= q)
    l = 0
    r = n - 1
    ceil = -1
    while l <= r
      m = (l + r) >> 1
      if vals[m] >= q
        ceil = vals[m]
        r = m - 1
      else
        l = m + 1
      end
    end

    # Find floor (largest <= q)
    l = 0
    r = n - 1
    floor = -1
    while l <= r
      m = (l + r) >> 1
      if vals[m] <= q
        floor = vals[m]
        l = m + 1
      else
        r = m - 1
      end
    end

    result << [floor, ceil]
  end

  result
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
  import scala.collection.mutable.{ArrayBuffer, ListBuffer}
  import java.util.Arrays

  def closestNodes(root: TreeNode, queries: List[Int]): List[List[Int]] = {
    // Inorder traversal to get sorted values
    val vals = new ArrayBuffer[Int]()
    val stack = new java.util.ArrayDeque[TreeNode]()
    var cur: TreeNode = root
    while (cur != null || !stack.isEmpty) {
      while (cur != null) {
        stack.push(cur)
        cur = cur.left
      }
      cur = stack.pop()
      vals += cur.value
      cur = cur.right
    }

    val arr: Array[Int] = vals.toArray

    val result = new ListBuffer[List[Int]]()
    for (q <- queries) {
      val idx = Arrays.binarySearch(arr, q)
      if (idx >= 0) {
        // exact match
        result += List(q, q)
      } else {
        val insertPos = -idx - 1
        val ceil = if (insertPos < arr.length) arr(insertPos) else -1
        val floor = if (insertPos - 1 >= 0) arr(insertPos - 1) else -1
        result += List(floor, ceil)
      }
    }

    result.toList
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

pub struct Solution;

impl Solution {
    pub fn closest_nodes(root: Option<Rc<RefCell<TreeNode>>>, queries: Vec<i32>) -> Vec<Vec<i32>> {
        // Inorder traversal to get sorted values
        let mut vals = Vec::new();
        let mut stack: Vec<Rc<RefCell<TreeNode>>> = Vec::new();
        let mut cur = root.clone();

        while cur.is_some() || !stack.is_empty() {
            while let Some(node_rc) = cur {
                stack.push(node_rc.clone());
                cur = node_rc.borrow().left.clone();
            }
            let node_rc = stack.pop().unwrap();
            vals.push(node_rc.borrow().val);
            cur = node_rc.borrow().right.clone();
        }

        // Answer queries using binary search
        let mut answer: Vec<Vec<i32>> = Vec::with_capacity(queries.len());
        for q in queries {
            match vals.binary_search(&q) {
                Ok(idx) => {
                    let v = vals[idx];
                    answer.push(vec![v, v]);
                }
                Err(idx) => {
                    let pred = if idx == 0 { -1 } else { vals[idx - 1] };
                    let succ = if idx == vals.len() { -1 } else { vals[idx] };
                    answer.push(vec![pred, succ]);
                }
            }
        }

        answer
    }
}
```

## Racket

```racket
#|
Definition for a binary tree node.
|#
(struct tree-node
  (val left right) #:mutable #:transparent)

(define/contract (closest-nodes root queries)
  (-> (or/c tree-node? #f) (listof exact-integer?) (listof (listof exact-integer?)))
  ;; Collect BST values in ascending order using tail recursion.
  (define (collect node acc)
    (if (not node)
        acc
        (let ((acc-right (collect (tree-node-right node) acc)))
          (collect (tree-node-left node)
                   (cons (tree-node-val node) acc-right)))))
  (define sorted-list (collect root '()))
  (define arr (list->vector sorted-list))
  (define len (vector-length arr))

  ;; binary search: first index with value >= target
  (define (lower-bound target)
    (let loop ((l 0) (r len))
      (if (= l r)
          l
          (let* ((mid (quotient (+ l r) 2))
                 (midval (vector-ref arr mid)))
            (if (< midval target)
                (loop (+ mid 1) r)
                (loop l mid))))))
  ;; binary search: last index with value <= target, returns -1 if none
  (define (predecessor-index target)
    (let loop ((l 0) (r len))
      (if (= l r)
          (- l 1)
          (let* ((mid (quotient (+ l r) 2))
                 (midval (vector-ref arr mid)))
            (if (<= midval target)
                (loop (+ mid 1) r)
                (loop l mid))))))
  
  ;; Process each query
  (map (lambda (q)
         (let* ((pred-idx (predecessor-index q))
                (succ-idx (lower-bound q))
                (pred (if (< pred-idx 0) -1 (vector-ref arr pred-idx)))
                (succ (if (= succ-idx len) -1 (vector-ref arr succ-idx))))
           (list pred succ)))
       queries))
```

## Erlang

```erlang
-module(solution).
-export([closest_nodes/2]).

-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec closest_nodes(Root :: #tree_node{} | null, Queries :: [integer()]) -> [[integer()]].
closest_nodes(Root, Queries) ->
    NodeVals = inorder(Root),
    QIdx = enumerate(Queries, 0, []),
    SortedQs = lists:keysort(1, QIdx),
    ResTuples = process(SortedQs, NodeVals, -1),
    SortedRes = lists:keysort(1, ResTuples),
    [Pair || {_Idx, Pair} <- SortedRes].

inorder(null) -> [];
inorder(Node) ->
    inorder(Node, []).

inorder(null, Acc) -> Acc;
inorder(#tree_node{val = V, left = L, right = R}, Acc) ->
    Acc1 = inorder(R, Acc),
    Acc2 = [V | Acc1],
    inorder(L, Acc2).

enumerate([], _Idx, Acc) -> lists:reverse(Acc);
enumerate([Q|Qs], Idx, Acc) ->
    enumerate(Qs, Idx + 1, [{Q, Idx} | Acc]).

process([], _NodeVals, _Floor) -> [];
process([{Q, Idx} | Rest], NodeVals, Floor) ->
    {NewNodeVals, NewFloor} = advance(NodeVals, Floor, Q),
    Ceil = case NewNodeVals of
        [] -> -1;
        [H|_] ->
            if NewFloor == Q -> Q; true -> H end
    end,
    [{Idx, [NewFloor, Ceil]} | process(Rest, NewNodeVals, NewFloor)].

advance([], Floor, _Q) -> {[], Floor};
advance([H|T], _PrevFloor, Q) when H =< Q ->
    advance(T, H, Q);
advance(NodeVals, PrevFloor, _Q) ->
    {NodeVals, PrevFloor}.
```

## Elixir

```elixir
defmodule Solution do
  @spec closest_nodes(root :: any, queries :: [integer]) :: [[integer]]
  def closest_nodes(root, queries) do
    sorted = inorder(root)
    tup = List.to_tuple(sorted)
    len = tuple_size(tup)

    Enum.map(queries, fn q ->
      idx = lower_bound(tup, len, q)

      succ =
        if idx == len do
          -1
        else
          elem(tup, idx)
        end

      pred =
        cond do
          idx == len ->
            # all elements are smaller than q
            elem(tup, len - 1)

          elem(tup, idx) == q ->
            elem(tup, idx)

          idx == 0 ->
            -1

          true ->
            elem(tup, idx - 1)
        end

      [pred, succ]
    end)
  end

  # Inorder traversal to obtain sorted values
  defp inorder(nil), do: []

  defp inorder(root) do
    inorder_iter(root, [], [])
  end

  defp inorder_iter(nil, [], acc), do: Enum.reverse(acc)

  defp inorder_iter(nil, [node | stack], acc) do
    inorder_iter(node.right, stack, [node.val | acc])
  end

  defp inorder_iter(%{left: _} = node, stack, acc) do
    inorder_iter(node.left, [node | stack], acc)
  end

  # Binary search for first index with value >= target
  defp lower_bound(tup, len, target) do
    lb(0, len, tup, target)
  end

  defp lb(lo, hi, tup, target) when lo < hi do
    mid = div(lo + hi, 2)

    if elem(tup, mid) < target do
      lb(mid + 1, hi, tup, target)
    else
      lb(lo, mid, tup, target)
    end
  end

  defp lb(lo, _hi, _tup, _target), do: lo
end
```
