# 1530. Number of Good Leaf Nodes Pairs

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
    int countPairs(TreeNode* root, int distance) {
        ans = 0;
        dfs(root, distance);
        return ans;
    }
private:
    int ans;
    vector<int> dfs(TreeNode* node, int D) {
        if (!node) return vector<int>(D + 1, 0);
        // leaf
        if (!node->left && !node->right) {
            vector<int> cnt(D + 1, 0);
            cnt[0] = 1;
            return cnt;
        }
        vector<int> leftCnt = dfs(node->left, D);
        vector<int> rightCnt = dfs(node->right, D);
        // count good pairs crossing this node
        for (int i = 0; i <= D; ++i) {
            if (leftCnt[i] == 0) continue;
            for (int j = 0; j <= D; ++j) {
                if (rightCnt[j] == 0) continue;
                if (i + j + 2 <= D) {
                    ans += leftCnt[i] * rightCnt[j];
                }
            }
        }
        // build current distance counts
        vector<int> cur(D + 1, 0);
        for (int i = 0; i < D; ++i) { // shift by one edge up to parent
            cur[i + 1] = leftCnt[i] + rightCnt[i];
        }
        return cur;
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
    private int result = 0;

    public int countPairs(TreeNode root, int distance) {
        dfs(root, distance);
        return result;
    }

    private int[] dfs(TreeNode node, int distance) {
        if (node == null) {
            return new int[distance + 1];
        }
        // leaf node
        if (node.left == null && node.right == null) {
            int[] arr = new int[distance + 1];
            arr[0] = 1;
            return arr;
        }

        int[] left = dfs(node.left, distance);
        int[] right = dfs(node.right, distance);

        // count good pairs passing through this node
        for (int i = 0; i <= distance; i++) {
            if (left[i] == 0) continue;
            for (int j = 0; j <= distance; j++) {
                if (right[j] == 0) continue;
                if (i + j + 2 <= distance) {
                    result += left[i] * right[j];
                }
            }
        }

        // build array of distances from current node
        int[] cur = new int[distance + 1];
        for (int i = 0; i < distance; i++) {
            cur[i + 1] = left[i] + right[i];
        }
        return cur;
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
    def countPairs(self, root, distance):
        """
        :type root: Optional[TreeNode]
        :type distance: int
        :rtype: int
        """
        self.distance = distance
        self.ans = 0

        def dfs(node):
            if not node:
                return [0] * (distance + 1)
            # leaf node
            if not node.left and not node.right:
                arr = [0] * (distance + 1)
                arr[0] = 1
                return arr

            left = dfs(node.left)
            right = dfs(node.right)

            # count good pairs crossing this node
            for i in range(distance):
                for j in range(distance - i - 1):
                    self.ans += left[i] * right[j]

            # build distance array for current node
            cur = [0] * (distance + 1)
            for d in range(1, distance + 1):
                cur[d] = left[d - 1] + right[d - 1]
            return cur

        dfs(root)
        return self.ans
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
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return [0] * (distance + 1)
            # leaf node
            if not node.left and not node.right:
                cnt = [0] * (distance + 1)
                cnt[0] = 1
                return cnt

            left = dfs(node.left)
            right = dfs(node.right)

            # count good pairs crossing this node
            for i in range(distance):
                if left[i] == 0:
                    continue
                for j in range(distance):
                    if right[j] == 0:
                        continue
                    if i + j + 2 <= distance:
                        self.ans += left[i] * right[j]

            # build distance array for current node (shift by 1)
            cur = [0] * (distance + 1)
            for d in range(1, distance + 1):
                cur[d] = left[d - 1] + right[d - 1]
            return cur

        dfs(root)
        return self.ans
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

static int* dfs(struct TreeNode* node, int distance, int *ans) {
    if (!node) return NULL;
    if (!node->left && !node->right) {
        int *arr = (int*)calloc(distance + 1, sizeof(int));
        arr[0] = 1;
        return arr;
    }
    int *left = dfs(node->left, distance, ans);
    int *right = dfs(node->right, distance, ans);

    if (left && right) {
        for (int i = 0; i <= distance; ++i) {
            if (!left[i]) continue;
            for (int j = 0; j <= distance; ++j) {
                if (!right[j]) continue;
                if (i + j + 2 <= distance) {
                    *ans += left[i] * right[j];
                }
            }
        }
    }

    int *cur = (int*)calloc(distance + 1, sizeof(int));
    for (int i = 0; i < distance; ++i) {
        if (left) cur[i + 1] += left[i];
        if (right) cur[i + 1] += right[i];
    }

    free(left);
    free(right);
    return cur;
}

int countPairs(struct TreeNode* root, int distance) {
    int ans = 0;
    int *tmp = dfs(root, distance, &ans);
    free(tmp);
    return ans;
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
    private int _maxDist;
    private int _answer;

    public int CountPairs(TreeNode root, int distance) {
        _maxDist = distance;
        _answer = 0;
        Dfs(root);
        return _answer;
    }

    private int[] Dfs(TreeNode node) {
        if (node == null) {
            return new int[_maxDist + 1];
        }
        // leaf node
        if (node.left == null && node.right == null) {
            var arr = new int[_maxDist + 1];
            arr[0] = 1;
            return arr;
        }

        var left = Dfs(node.left);
        var right = Dfs(node.right);

        // count good pairs crossing this node
        for (int i = 0; i <= _maxDist; i++) {
            if (left[i] == 0) continue;
            for (int j = 0; j <= _maxDist; j++) {
                if (right[j] == 0) continue;
                if (i + j + 2 <= _maxDist) {
                    _answer += left[i] * right[j];
                }
            }
        }

        // build distance array for current node
        var cur = new int[_maxDist + 1];
        for (int d = 1; d <= _maxDist; d++) {
            cur[d] = left[d - 1] + right[d - 1];
        }
        return cur;
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
 * @param {number} distance
 * @return {number}
 */
var countPairs = function(root, distance) {
    let result = 0;
    
    const dfs = (node) => {
        if (!node) return new Array(distance + 1).fill(0);
        
        // leaf node
        if (!node.left && !node.right) {
            const arr = new Array(distance + 1).fill(0);
            arr[0] = 1; // distance 0 from itself
            return arr;
        }
        
        const left = dfs(node.left);
        const right = dfs(node.right);
        
        // count good pairs crossing this node
        for (let i = 0; i <= distance; ++i) {
            if (!left[i]) continue;
            for (let j = 0; j <= distance; ++j) {
                if (!right[j]) continue;
                if (i + j + 2 <= distance) {
                    result += left[i] * right[j];
                }
            }
        }
        
        // build current distance array
        const cur = new Array(distance + 1).fill(0);
        for (let i = 0; i < distance; ++i) {
            if (left[i]) cur[i + 1] += left[i];
            if (right[i]) cur[i + 1] += right[i];
        }
        return cur;
    };
    
    dfs(root);
    return result;
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

function countPairs(root: TreeNode | null, distance: number): number {
    let ans = 0;

    const dfs = (node: TreeNode | null): number[] => {
        if (!node) return [];

        // leaf node
        if (!node.left && !node.right) {
            const arr = new Array(distance + 1).fill(0);
            arr[0] = 1;
            return arr;
        }

        const left = dfs(node.left);
        const right = dfs(node.right);

        // count good pairs crossing this node
        for (let i = 0; i < left.length; i++) {
            if (!left[i]) continue;
            for (let j = 0; j < right.length; j++) {
                if (!right[j]) continue;
                if (i + j + 2 <= distance) {
                    ans += left[i] * right[j];
                }
            }
        }

        // build distance array for current node
        const cur = new Array(distance + 1).fill(0);
        for (let i = 0; i < distance; i++) {
            if (left[i]) cur[i + 1] += left[i];
            if (right[i]) cur[i + 1] += right[i];
        }
        return cur;
    };

    dfs(root);
    return ans;
}
```

## Php

```php
<?php
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
    private $ans = 0;

    /**
     * @param TreeNode $root
     * @param Integer $distance
     * @return Integer
     */
    function countPairs($root, $distance) {
        $this->ans = 0;
        $this->dfs($root, $distance);
        return $this->ans;
    }

    private function dfs($node, $dist) {
        if ($node === null) {
            return array_fill(0, $dist + 1, 0);
        }
        // leaf node
        if ($node->left === null && $node->right === null) {
            $arr = array_fill(0, $dist + 1, 0);
            $arr[0] = 1;
            return $arr;
        }

        $left = $this->dfs($node->left, $dist);
        $right = $this->dfs($node->right, $dist);

        // count good pairs crossing this node
        for ($i = 0; $i <= $dist; $i++) {
            if ($left[$i] == 0) continue;
            for ($j = 0; $j <= $dist; $j++) {
                if ($right[$j] == 0) continue;
                if ($i + $j + 2 <= $dist) {
                    $this->ans += $left[$i] * $right[$j];
                }
            }
        }

        // build distance array for current node
        $res = array_fill(0, $dist + 1, 0);
        for ($i = 0; $i < $dist; $i++) {
            $res[$i + 1] = $left[$i] + $right[$i];
        }
        return $res;
    }
}
?>
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
    func countPairs(_ root: TreeNode?, _ distance: Int) -> Int {
        var answer = 0
        _ = dfs(root, distance, &answer)
        return answer
    }

    private func dfs(_ node: TreeNode?, _ distance: Int, _ ans: inout Int) -> [Int] {
        guard let node = node else {
            return Array(repeating: 0, count: distance + 1)
        }
        // Leaf node
        if node.left == nil && node.right == nil {
            var arr = Array(repeating: 0, count: distance + 1)
            arr[0] = 1
            return arr
        }

        let leftArr = dfs(node.left, distance, &ans)
        let rightArr = dfs(node.right, distance, &ans)

        // Count good pairs crossing this node
        for l in 0...distance {
            if leftArr[l] == 0 { continue }
            for r in 0...distance {
                if rightArr[r] == 0 { continue }
                if l + r + 2 <= distance {
                    ans += leftArr[l] * rightArr[r]
                }
            }
        }

        // Build current distance array (shift by 1)
        var cur = Array(repeating: 0, count: distance + 1)
        for i in 0..<distance { // i+1 must be <= distance
            let leftCount = leftArr[i]
            if leftCount > 0 {
                cur[i + 1] += leftCount
            }
            let rightCount = rightArr[i]
            if rightCount > 0 {
                cur[i + 1] += rightCount
            }
        }

        return cur
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
    private var answer = 0

    fun countPairs(root: TreeNode?, distance: Int): Int {
        dfs(root, distance)
        return answer
    }

    private fun dfs(node: TreeNode?, d: Int): IntArray {
        val cnt = IntArray(d + 1)
        if (node == null) return cnt
        if (node.left == null && node.right == null) {
            cnt[0] = 1
            return cnt
        }

        val left = dfs(node.left, d)
        val right = dfs(node.right, d)

        // count good pairs formed by leaves from left and right subtrees
        for (i in 0..d) {
            if (left[i] == 0) continue
            for (j in 0..d) {
                if (right[j] == 0) continue
                if (i + j + 2 <= d) {
                    answer += left[i] * right[j]
                }
            }
        }

        // propagate distances up by one edge
        for (i in 0 until d) {
            cnt[i + 1] = left[i] + right[i]
        }
        return cnt
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
  int _ans = 0;

  List<int> _dfs(TreeNode? node, int distance) {
    if (node == null) {
      return List.filled(distance + 1, 0);
    }
    // leaf node
    if (node.left == null && node.right == null) {
      var arr = List.filled(distance + 1, 0);
      arr[0] = 1;
      return arr;
    }

    var left = _dfs(node.left, distance);
    var right = _dfs(node.right, distance);

    // count good pairs passing through this node
    for (int i = 0; i <= distance; ++i) {
      if (left[i] == 0) continue;
      for (int j = 0; j <= distance; ++j) {
        if (right[j] == 0) continue;
        if (i + j + 2 <= distance) {
          _ans += left[i] * right[j];
        }
      }
    }

    // build current distance array
    var cur = List.filled(distance + 1, 0);
    for (int i = 0; i < distance; ++i) {
      cur[i + 1] += left[i];
      cur[i + 1] += right[i];
    }
    return cur;
  }

  int countPairs(TreeNode? root, int distance) {
    _ans = 0;
    _dfs(root, distance);
    return _ans;
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
func countPairs(root *TreeNode, distance int) int {
    ans := 0

    var dfs func(node *TreeNode) []int
    dfs = func(node *TreeNode) []int {
        if node == nil {
            return make([]int, distance+1)
        }
        // leaf node
        if node.Left == nil && node.Right == nil {
            arr := make([]int, distance+1)
            arr[0] = 1
            return arr
        }

        left := dfs(node.Left)
        right := dfs(node.Right)

        // count good pairs passing through this node
        for i := 0; i <= distance; i++ {
            if left[i] == 0 {
                continue
            }
            for j := 0; j <= distance; j++ {
                if right[j] == 0 {
                    continue
                }
                if i+j+2 <= distance {
                    ans += left[i] * right[j]
                }
            }
        }

        // build array of leaf distances from current node
        cur := make([]int, distance+1)
        for d := 0; d < distance; d++ { // shift by 1 edge upward
            cur[d+1] = left[d] + right[d]
        }
        return cur
    }

    dfs(root)
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

def count_pairs(root, distance)
  @distance = distance
  @ans = 0

  dfs = lambda do |node|
    return Array.new(@distance + 1, 0) if node.nil?

    # leaf node
    if node.left.nil? && node.right.nil?
      arr = Array.new(@distance + 1, 0)
      arr[0] = 1
      return arr
    end

    left_counts  = dfs.call(node.left)
    right_counts = dfs.call(node.right)

    # count good pairs crossing this node
    (0..@distance).each do |i|
      next if left_counts[i].zero?
      (0..@distance).each do |j|
        next if right_counts[j].zero?
        @ans += left_counts[i] * right_counts[j] if i + j + 2 <= @distance
      end
    end

    # build counts for current node (shift distances by 1)
    cur = Array.new(@distance + 1, 0)
    (0...@distance).each do |i|
      cur[i + 1] = left_counts[i] + right_counts[i]
    end
    cur
  end

  dfs.call(root)
  @ans
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
  def countPairs(root: TreeNode, distance: Int): Int = {
    var answer = 0

    def dfs(node: TreeNode): Array[Int] = {
      if (node == null) return new Array[Int](distance + 1)

      // leaf node
      if (node.left == null && node.right == null) {
        val arr = new Array[Int](distance + 1)
        arr(0) = 1
        return arr
      }

      val leftArr = dfs(node.left)
      val rightArr = dfs(node.right)

      // count good pairs passing through this node
      for (i <- 0 to distance) {
        if (leftArr(i) == 0) {}
        for (j <- 0 to distance) {
          if (rightArr(j) == 0) {}
          if (i + j + 2 <= distance) {
            answer += leftArr(i) * rightArr(j)
          }
        }
      }

      // build array of distances from current node
      val cur = new Array[Int](distance + 1)
      for (i <- 0 until distance) {
        cur(i + 1) = leftArr(i) + rightArr(i)
      }
      cur
    }

    dfs(root)
    answer
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
    pub fn count_pairs(root: Option<Rc<RefCell<TreeNode>>>, distance: i32) -> i32 {
        let mut ans = 0;
        Self::dfs(root, distance as usize, &mut ans);
        ans
    }

    fn dfs(node: Option<Rc<RefCell<TreeNode>>>, dist: usize, ans: &mut i32) -> Vec<i32> {
        if node.is_none() {
            return vec![0; dist + 1];
        }
        let n = node.unwrap();
        let left_opt = n.borrow().left.clone();
        let right_opt = n.borrow().right.clone();

        // leaf node
        if left_opt.is_none() && right_opt.is_none() {
            let mut v = vec![0; dist + 1];
            v[0] = 1;
            return v;
        }

        let left = Self::dfs(left_opt, dist, ans);
        let right = Self::dfs(right_opt, dist, ans);

        // count good pairs crossing this node
        for i in 0..=dist {
            if left[i] == 0 { continue; }
            for j in 0..=dist {
                if right[j] == 0 { continue; }
                if i + j + 2 <= dist {
                    *ans += left[i] * right[j];
                }
            }
        }

        // build vector for parent (distance increased by 1)
        let mut cur = vec![0; dist + 1];
        for i in 0..dist { // i+1 will be within bounds
            if left[i] > 0 {
                cur[i + 1] += left[i];
            }
            if right[i] > 0 {
                cur[i + 1] += right[i];
            }
        }
        cur
    }
}
```

## Racket

```racket
#lang racket

; Definition for a binary tree node.
(struct tree-node
  (val left right) #:mutable #:transparent)

(define/contract (count-pairs root distance)
  (-> (or/c tree-node? #f) exact-integer? exact-integer?)
  (let ((ans 0))
    (define (dfs node)
      (if (not node)
          (make-vector (+ distance 1) 0)
          (let ((left-child (tree-node-left node))
                (right-child (tree-node-right node)))
            (cond
              [(and (not left-child) (not right-child)) ; leaf
               (define v (make-vector (+ distance 1) 0))
               (vector-set! v 0 1)
               v]
              [else
               (define leftv (dfs left-child))
               (define rightv (dfs right-child))
               ;; count good pairs crossing this node
               (for ([i (in-range 0 (+ distance 1))])
                 (for ([j (in-range 0 (+ distance 1))])
                   (when (<= (+ i j 2) distance)
                     (set! ans (+ ans (* (vector-ref leftv i)
                                         (vector-ref rightv j)))))))
               ;; build vector for this node
               (define cur (make-vector (+ distance 1) 0))
               (for ([k (in-range 0 distance)]) ; k up to distance-1
                 (vector-set! cur (add1 k)
                              (+ (vector-ref leftv k)
                                 (vector-ref rightv k))))
               cur])))))
    (void (dfs root))   ; trigger traversal
    ans))
```

## Erlang

```erlang
-module(solution).
-export([count_pairs/2]).

-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec count_pairs(Root :: #tree_node{} | null, Distance :: integer()) -> integer().
count_pairs(Root, Distance) ->
    {_Counts, Pairs} = dfs(Root, Distance),
    Pairs.

dfs(null, D) ->
    {lists:duplicate(D + 1, 0), 0};
dfs(Node, D) when Node#tree_node.left == null, Node#tree_node.right == null ->
    {[1 | lists:duplicate(D, 0)], 0};
dfs(Node, D) ->
    {LCounts, LPairs} = dfs(Node#tree_node.left, D),
    {RCounts, RPairs} = dfs(Node#tree_node.right, D),
    PairAdd = cross(LCounts, RCounts, D),
    TotalPairs = LPairs + RPairs + PairAdd,
    ShiftL = [0] ++ lists:sublist(LCounts, D),
    ShiftR = [0] ++ lists:sublist(RCounts, D),
    NewCounts = lists:zipwith(fun(A, B) -> A + B end, ShiftL, ShiftR),
    {NewCounts, TotalPairs}.

cross(L, R, D) ->
    lists:foldl(
      fun(I, AccI) ->
          Li = lists:nth(I + 1, L),
          lists:foldl(
            fun(J, AccJ) ->
                if I + J + 2 =< D ->
                       AccJ + Li * lists:nth(J + 1, R);
                   true -> AccJ
                end
            end,
            AccI,
            lists:seq(0, D - 1)
          )
      end,
      0,
      lists:seq(0, D - 1)
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_pairs(root :: TreeNode.t | nil, distance :: integer) :: integer
  def count_pairs(root, distance) do
    {_counts, pairs} = dfs(root, distance)
    pairs
  end

  defp dfs(nil, distance) do
    {List.duplicate(0, distance + 1), 0}
  end

  defp dfs(%TreeNode{left: nil, right: nil}, distance) do
    counts = [1] ++ List.duplicate(0, distance)
    {counts, 0}
  end

  defp dfs(%TreeNode{left: left, right: right}, distance) do
    {l_counts, l_pairs} = dfs(left, distance)
    {r_counts, r_pairs} = dfs(right, distance)

    cross =
      Enum.reduce(0..distance - 1, 0, fn i, acc ->
        lc = Enum.at(l_counts, i)

        if lc == 0 do
          acc
        else
          max_j = distance - i - 2

          if max_j < 0 do
            acc
          else
            add =
              Enum.reduce(0..max_j, 0, fn j, inner_acc ->
                rc = Enum.at(r_counts, j)
                inner_acc + lc * rc
              end)

            acc + add
          end
        end
      end)

    total_pairs = l_pairs + r_pairs + cross

    new_counts =
      for i <- 0..distance do
        if i == 0 do
          0
        else
          Enum.at(l_counts, i - 1) + Enum.at(r_counts, i - 1)
        end
      end

    {new_counts, total_pairs}
  end
end
```
