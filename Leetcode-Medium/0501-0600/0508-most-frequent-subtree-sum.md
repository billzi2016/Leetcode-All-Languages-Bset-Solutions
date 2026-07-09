# 0508. Most Frequent Subtree Sum

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

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
    vector<int> findFrequentTreeSum(TreeNode* root) {
        unordered_map<int,int> freq;
        int maxFreq = 0;
        function<int(TreeNode*)> dfs = [&](TreeNode* node)->int{
            if (!node) return 0;
            int sum = node->val + dfs(node->left) + dfs(node->right);
            int f = ++freq[sum];
            if (f > maxFreq) maxFreq = f;
            return sum;
        };
        dfs(root);
        vector<int> ans;
        for (const auto& p : freq) {
            if (p.second == maxFreq) ans.push_back(p.first);
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
    private java.util.Map<Integer, Integer> freqMap = new java.util.HashMap<>();
    private int maxFreq = 0;

    public int[] findFrequentTreeSum(TreeNode root) {
        if (root == null) {
            return new int[0];
        }
        postOrder(root);
        java.util.List<Integer> resultList = new java.util.ArrayList<>();
        for (java.util.Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
            if (entry.getValue() == maxFreq) {
                resultList.add(entry.getKey());
            }
        }
        int[] res = new int[resultList.size()];
        for (int i = 0; i < resultList.size(); i++) {
            res[i] = resultList.get(i);
        }
        return res;
    }

    private int postOrder(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int leftSum = postOrder(node.left);
        int rightSum = postOrder(node.right);
        int curSum = node.val + leftSum + rightSum;

        int count = freqMap.getOrDefault(curSum, 0) + 1;
        freqMap.put(curSum, count);
        if (count > maxFreq) {
            maxFreq = count;
        }
        return curSum;
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
    def findFrequentTreeSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        from collections import defaultdict
        freq = defaultdict(int)
        maxfreq = 0

        def dfs(node):
            nonlocal maxfreq
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            total = node.val + left_sum + right_sum
            freq[total] += 1
            if freq[total] > maxfreq:
                maxfreq = freq[total]
            return total

        dfs(root)
        return [s for s, cnt in freq.items() if cnt == maxfreq]
```

## Python3

```python
from typing import Optional, List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        from collections import defaultdict
        freq = defaultdict(int)
        max_freq = 0

        def dfs(node):
            nonlocal max_freq
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            total = node.val + left + right
            cnt = freq[total] + 1
            freq[total] = cnt
            if cnt > max_freq:
                max_freq = cnt
            return total

        dfs(root)
        return [s for s, c in freq.items() if c == max_freq]
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

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

/* Post‑order traversal: compute subtree sum, store it in the array */
static int dfs(struct TreeNode *node, int **sums, int *size, int *capacity) {
    if (!node) return 0;
    int left = dfs(node->left, sums, size, capacity);
    int right = dfs(node->right, sums, size, capacity);
    int total = node->val + left + right;

    if (*size >= *capacity) {
        *capacity = (*capacity == 0) ? 128 : (*capacity * 2);
        *sums = realloc(*sums, (*capacity) * sizeof(int));
    }
    (*sums)[*size] = total;
    (*size)++;

    return total;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findFrequentTreeSum(struct TreeNode* root, int* returnSize) {
    if (!root) {
        *returnSize = 0;
        return NULL;
    }

    int *sums = NULL;
    int size = 0, capacity = 0;

    dfs(root, &sums, &size, &capacity);

    qsort(sums, size, sizeof(int), cmp_int);

    int maxFreq = 0;
    for (int i = 0; i < size;) {
        int j = i + 1;
        while (j < size && sums[j] == sums[i]) ++j;
        int freq = j - i;
        if (freq > maxFreq) maxFreq = freq;
        i = j;
    }

    int *result = malloc(size * sizeof(int));
    int cnt = 0;
    for (int i = 0; i < size;) {
        int j = i + 1;
        while (j < size && sums[j] == sums[i]) ++j;
        int freq = j - i;
        if (freq == maxFreq) {
            result[cnt++] = sums[i];
        }
        i = j;
    }

    *returnSize = cnt;
    free(sums);
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[] FindFrequentTreeSum(TreeNode root) {
        var freq = new Dictionary<int, int>();
        int maxFreq = 0;
        
        int PostOrder(TreeNode node) {
            if (node == null) return 0;
            int leftSum = PostOrder(node.left);
            int rightSum = PostOrder(node.right);
            int sum = node.val + leftSum + rightSum;
            
            if (freq.ContainsKey(sum))
                freq[sum]++;
            else
                freq[sum] = 1;
            
            if (freq[sum] > maxFreq) maxFreq = freq[sum];
            return sum;
        }
        
        PostOrder(root);
        
        var result = new List<int>();
        foreach (var kvp in freq) {
            if (kvp.Value == maxFreq)
                result.Add(kvp.Key);
        }
        return result.ToArray();
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
 * @return {number[]}
 */
var findFrequentTreeSum = function(root) {
    if (!root) return [];
    const freq = new Map();
    let maxFreq = 0;
    const dfs = (node) => {
        if (!node) return 0;
        const left = dfs(node.left);
        const right = dfs(node.right);
        const sum = node.val + left + right;
        const cnt = (freq.get(sum) || 0) + 1;
        freq.set(sum, cnt);
        if (cnt > maxFreq) maxFreq = cnt;
        return sum;
    };
    dfs(root);
    const res = [];
    for (const [sum, cnt] of freq.entries()) {
        if (cnt === maxFreq) res.push(sum);
    }
    return res;
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

function findFrequentTreeSum(root: TreeNode | null): number[] {
    if (!root) return [];

    const freq = new Map<number, number>();
    let maxFreq = 0;

    function dfs(node: TreeNode | null): number {
        if (!node) return 0;
        const leftSum = dfs(node.left);
        const rightSum = dfs(node.right);
        const sum = node.val + leftSum + rightSum;
        const count = (freq.get(sum) ?? 0) + 1;
        freq.set(sum, count);
        if (count > maxFreq) maxFreq = count;
        return sum;
    }

    dfs(root);

    const result: number[] = [];
    for (const [sum, cnt] of freq.entries()) {
        if (cnt === maxFreq) result.push(sum);
    }
    return result;
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
     * @return Integer[]
     */
    function findFrequentTreeSum($root) {
        if ($root === null) {
            return [];
        }
        $freq = [];
        $maxFreq = 0;
        $this->dfs($root, $freq, $maxFreq);
        $result = [];
        foreach ($freq as $sum => $cnt) {
            if ($cnt == $maxFreq) {
                $result[] = (int)$sum;
            }
        }
        return $result;
    }

    private function dfs($node, &$freq, &$maxFreq) {
        if ($node === null) {
            return 0;
        }
        $leftSum = $this->dfs($node->left, $freq, $maxFreq);
        $rightSum = $this->dfs($node->right, $freq, $maxFreq);
        $total = $node->val + $leftSum + $rightSum;

        if (!isset($freq[$total])) {
            $freq[$total] = 0;
        }
        $freq[$total]++;

        if ($freq[$total] > $maxFreq) {
            $maxFreq = $freq[$total];
        }

        return $total;
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
    func findFrequentTreeSum(_ root: TreeNode?) -> [Int] {
        var freq = [Int:Int]()
        var maxFreq = 0
        
        func dfs(_ node: TreeNode?) -> Int {
            guard let n = node else { return 0 }
            let left = dfs(n.left)
            let right = dfs(n.right)
            let sum = n.val + left + right
            let count = (freq[sum] ?? 0) + 1
            freq[sum] = count
            if count > maxFreq {
                maxFreq = count
            }
            return sum
        }
        
        _ = dfs(root)
        
        var result = [Int]()
        for (s, c) in freq where c == maxFreq {
            result.append(s)
        }
        return result
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
    fun findFrequentTreeSum(root: TreeNode?): IntArray {
        if (root == null) return intArrayOf()
        val freq = HashMap<Int, Int>()
        var maxFreq = 0

        fun dfs(node: TreeNode?): Int {
            if (node == null) return 0
            val sum = node.`val` + dfs(node.left) + dfs(node.right)
            val count = (freq[sum] ?: 0) + 1
            freq[sum] = count
            if (count > maxFreq) maxFreq = count
            return sum
        }

        dfs(root)

        val result = mutableListOf<Int>()
        for ((k, v) in freq) {
            if (v == maxFreq) result.add(k)
        }
        return result.toIntArray()
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
  List<int> findFrequentTreeSum(TreeNode? root) {
    if (root == null) return [];
    final Map<int, int> freq = {};
    int maxFreq = 0;

    int dfs(TreeNode? node) {
      if (node == null) return 0;
      final leftSum = dfs(node.left);
      final rightSum = dfs(node.right);
      final sum = node.val + leftSum + rightSum;
      final count = (freq[sum] ?? 0) + 1;
      freq[sum] = count;
      if (count > maxFreq) {
        maxFreq = count;
      }
      return sum;
    }

    dfs(root);

    final List<int> result = [];
    for (final entry in freq.entries) {
      if (entry.value == maxFreq) {
        result.add(entry.key);
      }
    }
    return result;
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
func findFrequentTreeSum(root *TreeNode) []int {
    if root == nil {
        return []int{}
    }

    freq := make(map[int]int)
    maxFreq := 0

    var dfs func(*TreeNode) int
    dfs = func(node *TreeNode) int {
        if node == nil {
            return 0
        }
        sum := node.Val + dfs(node.Left) + dfs(node.Right)
        freq[sum]++
        if freq[sum] > maxFreq {
            maxFreq = freq[sum]
        }
        return sum
    }

    dfs(root)

    result := []int{}
    for s, c := range freq {
        if c == maxFreq {
            result = append(result, s)
        }
    }
    return result
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

def find_frequent_tree_sum(root)
  return [] unless root

  freq = Hash.new(0)
  max_freq = 0

  dfs = lambda do |node|
    next 0 unless node
    left_sum = dfs.call(node.left)
    right_sum = dfs.call(node.right)
    sum = node.val + left_sum + right_sum
    freq[sum] += 1
    max_freq = [max_freq, freq[sum]].max
    sum
  end

  dfs.call(root)

  result = []
  freq.each { |s, cnt| result << s if cnt == max_freq }
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
    def findFrequentTreeSum(root: TreeNode): Array[Int] = {
        import scala.collection.mutable

        val freq = mutable.Map[Int, Int]()
        var maxFreq = 0

        def dfs(node: TreeNode): Int = {
            if (node == null) return 0
            val leftSum = dfs(node.left)
            val rightSum = dfs(node.right)
            val sum = node.value + leftSum + rightSum
            val cnt = freq.getOrElse(sum, 0) + 1
            freq.update(sum, cnt)
            if (cnt > maxFreq) maxFreq = cnt
            sum
        }

        dfs(root)

        freq.filter { case (_, v) => v == maxFreq }.keys.toArray
    }
}
```

## Rust

```rust
use std::cell::RefCell;
use std::rc::Rc;
use std::collections::HashMap;

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
    pub fn find_frequent_tree_sum(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, freq: &mut HashMap<i32, i32>) -> i32 {
            if let Some(rc) = node {
                let left_sum = dfs(&rc.borrow().left, freq);
                let right_sum = dfs(&rc.borrow().right, freq);
                let total = rc.borrow().val + left_sum + right_sum;
                *freq.entry(total).or_insert(0) += 1;
                total
            } else {
                0
            }
        }

        let mut freq: HashMap<i32, i32> = HashMap::new();
        dfs(&root, &mut freq);

        if freq.is_empty() {
            return Vec::new();
        }

        let max_count = *freq.values().max().unwrap();

        freq.into_iter()
            .filter_map(|(sum, count)| if count == max_count { Some(sum) } else { None })
            .collect()
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

(define/contract (find-frequent-tree-sum root)
  (-> (or/c tree-node? #f) (listof exact-integer?))
  (if (not root)
      '()
      (let ((freq (make-hash)))
        (letrec ((dfs (lambda (node)
                        (if (not node)
                            0
                            (let* ((left-sum  (dfs (tree-node-left node)))
                                   (right-sum (dfs (tree-node-right node)))
                                   (total (+ (tree-node-val node) left-sum right-sum)))
                              (hash-update! freq total add1 0)
                              total)))))
          (dfs root)
          ;; Determine the maximum frequency
          (define max-freq 0)
          (for ([k (in-hash-keys freq)])
            (let ((c (hash-ref freq k)))
              (when (> c max-freq) (set! max-freq c))))
          ;; Collect all sums with that frequency
          (define result '())
          (for ([k (in-hash-keys freq)])
            (when (= (hash-ref freq k) max-freq)
              (set! result (cons k result))))
          (reverse result)))))
```

## Erlang

```erlang
%% Definition for a binary tree node.
-record(tree_node, {val = 0 :: integer(),
                    left = null  :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec find_frequent_tree_sum(Root :: #tree_node{} | null) -> [integer()].
find_frequent_tree_sum(Root) ->
    {_, FreqMap} = dfs(Root, #{}),
    {_, SumsRev} = maps:fold(
        fun(Key, Count, {CurMax, Acc}) ->
            if
                Count > CurMax -> {Count, [Key]};
                Count == CurMax -> {CurMax, [Key | Acc]};
                true -> {CurMax, Acc}
            end
        end,
        {0, []},
        FreqMap),
    lists:reverse(SumsRev).

dfs(null, Map) ->
    {0, Map};
dfs(Node, Map) when is_record(Node, tree_node) ->
    {LeftSum, Map1} = dfs(Node#tree_node.left, Map),
    {RightSum, Map2} = dfs(Node#tree_node.right, Map1),
    Sum = Node#tree_node.val + LeftSum + RightSum,
    NewMap = maps:update_with(Sum, fun(C) -> C + 1 end, 1, Map2),
    {Sum, NewMap}.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_frequent_tree_sum(root :: TreeNode.t | nil) :: [integer]
  def find_frequent_tree_sum(nil), do: []

  def find_frequent_tree_sum(root) do
    {_total, sums_rev} = dfs(root, [])
    freq_map = Enum.reduce(sums_rev, %{}, fn s, acc ->
      Map.update(acc, s, 1, &(&1 + 1))
    end)

    max_freq = freq_map |> Map.values() |> Enum.max()

    freq_map
    |> Enum.filter(fn {_k, v} -> v == max_freq end)
    |> Enum.map(fn {k, _v} -> k end)
  end

  defp dfs(nil, acc), do: {0, acc}

  defp dfs(%TreeNode{val: v, left: l, right: r}, acc) do
    {lsum, acc1} = dfs(l, acc)
    {rsum, acc2} = dfs(r, acc1)
    sum = v + lsum + rsum
    {sum, [sum | acc2]}
  end
end
```
