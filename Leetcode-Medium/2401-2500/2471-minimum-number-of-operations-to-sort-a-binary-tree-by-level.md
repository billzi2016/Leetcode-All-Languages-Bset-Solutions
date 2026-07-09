# 2471. Minimum Number of Operations to Sort a Binary Tree by Level

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
    int minimumOperations(TreeNode* root) {
        if (!root) return 0;
        std::queue<TreeNode*> q;
        q.push(root);
        long long totalSwaps = 0;
        while (!q.empty()) {
            int sz = q.size();
            std::vector<int> levelVals;
            levelVals.reserve(sz);
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front(); q.pop();
                levelVals.push_back(node->val);
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            int n = levelVals.size();
            std::vector<std::pair<int,int>> vp;
            vp.reserve(n);
            for (int i = 0; i < n; ++i) {
                vp.emplace_back(levelVals[i], i);
            }
            std::sort(vp.begin(), vp.end(),
                      [](const std::pair<int,int>& a, const std::pair<int,int>& b){
                          return a.first < b.first;
                      });
            std::vector<bool> visited(n,false);
            for (int i = 0; i < n; ++i) {
                if (visited[i] || vp[i].second == i) continue;
                int cycleLen = 0;
                int j = i;
                while (!visited[j]) {
                    visited[j] = true;
                    j = vp[j].second;
                    ++cycleLen;
                }
                totalSwaps += (cycleLen - 1);
            }
        }
        return static_cast<int>(totalSwaps);
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
    public int minimumOperations(TreeNode root) {
        if (root == null) return 0;
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        long totalSwaps = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            int[] levelVals = new int[size];
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                levelVals[i] = node.val;
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            totalSwaps += minSwaps(levelVals);
        }
        return (int) totalSwaps;
    }

    private int minSwaps(int[] arr) {
        int n = arr.length;
        int[] sorted = arr.clone();
        Arrays.sort(sorted);
        Map<Integer, Integer> targetPos = new HashMap<>(n * 2);
        for (int i = 0; i < n; i++) {
            targetPos.put(sorted[i], i);
        }
        boolean[] visited = new boolean[n];
        int swaps = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i]) continue;
            int correctIdx = targetPos.get(arr[i]);
            if (correctIdx == i) {
                visited[i] = true;
                continue;
            }
            int cycleSize = 0;
            int j = i;
            while (!visited[j]) {
                visited[j] = true;
                j = targetPos.get(arr[j]);
                cycleSize++;
            }
            swaps += cycleSize - 1;
        }
        return swaps;
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

from collections import deque

class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        def min_swaps(arr):
            sorted_arr = sorted(arr)
            pos = {v: i for i, v in enumerate(arr)}
            swaps = 0
            for i in range(len(arr)):
                correct_val = sorted_arr[i]
                if arr[i] != correct_val:
                    swaps += 1
                    cur_val = arr[i]
                    j = pos[correct_val]

                    # swap positions i and j
                    arr[i], arr[j] = arr[j], arr[i]

                    # update mapping after swap
                    pos[cur_val] = j
                    pos[correct_val] = i
            return swaps

        total_swaps = 0
        q = deque([root])
        while q:
            level_size = len(q)
            level_vals = []
            for _ in range(level_size):
                node = q.popleft()
                level_vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            total_swaps += min_swaps(level_vals)

        return total_swaps
```

## Python3

```python
from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumOperations(self, root: Optional['TreeNode']) -> int:
        if not root:
            return 0

        def min_swaps(arr):
            n = len(arr)
            # pair each value with its original index
            pairs = [(val, idx) for idx, val in enumerate(arr)]
            # sort by value to know target positions
            pairs.sort(key=lambda x: x[0])
            visited = [False] * n
            swaps = 0
            for i in range(n):
                if visited[i] or pairs[i][1] == i:
                    continue
                cycle_len = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = pairs[j][1]
                    cycle_len += 1
                swaps += cycle_len - 1
            return swaps

        total_swaps = 0
        q = deque([root])
        while q:
            level_size = len(q)
            level_vals = []
            for _ in range(level_size):
                node = q.popleft()
                level_vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            total_swaps += min_swaps(level_vals)

        return total_swaps
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
typedef struct Pair {
    int val;
    int idx;
} Pair;

static int cmpPair(const void *a, const void *b) {
    int va = ((const Pair *)a)->val;
    int vb = ((const Pair *)b)->val;
    return (va > vb) - (va < vb);
}

int minimumOperations(struct TreeNode* root) {
    if (!root) return 0;

    /* Queue for BFS */
    int capacity = 200005;                     // enough for constraints
    struct TreeNode **queue = (struct TreeNode **)malloc(sizeof(struct TreeNode *) * capacity);
    int front = 0, back = 0;
    queue[back++] = root;

    long long totalSwaps = 0;                  // result fits in int but use larger type during sum

    while (front < back) {
        int levelSize = back - front;
        Pair *pairs = (Pair *)malloc(sizeof(Pair) * levelSize);

        for (int i = 0; i < levelSize; ++i) {
            struct TreeNode *node = queue[front++];
            pairs[i].val = node->val;
            pairs[i].idx = i;

            if (node->left)  queue[back++] = node->left;
            if (node->right) queue[back++] = node->right;
        }

        qsort(pairs, levelSize, sizeof(Pair), cmpPair);

        char *visited = (char *)calloc(levelSize, sizeof(char));
        for (int i = 0; i < levelSize; ++i) {
            if (visited[i] || pairs[i].idx == i)
                continue;

            int cycleLen = 0;
            int j = i;
            while (!visited[j]) {
                visited[j] = 1;
                j = pairs[j].idx;
                ++cycleLen;
            }
            totalSwaps += cycleLen - 1;
        }

        free(visited);
        free(pairs);
    }

    free(queue);
    return (int)totalSwaps;
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
    public int MinimumOperations(TreeNode root) {
        if (root == null) return 0;
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        long totalSwaps = 0;
        while (queue.Count > 0) {
            int levelSize = queue.Count;
            int[] values = new int[levelSize];
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.Dequeue();
                values[i] = node.val;
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
            totalSwaps += MinSwaps(values);
        }
        return (int)totalSwaps;
    }

    private int MinSwaps(int[] arr) {
        int n = arr.Length;
        var pairs = new Tuple<int, int>[n];
        for (int i = 0; i < n; i++) {
            pairs[i] = Tuple.Create(arr[i], i);
        }
        Array.Sort(pairs, (a, b) => a.Item1.CompareTo(b.Item1));

        bool[] visited = new bool[n];
        int swaps = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i] || pairs[i].Item2 == i) continue;

            int cycleSize = 0;
            int j = i;
            while (!visited[j]) {
                visited[j] = true;
                j = pairs[j].Item2;
                cycleSize++;
            }
            if (cycleSize > 1) swaps += cycleSize - 1;
        }
        return swaps;
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
var minimumOperations = function(root) {
    if (!root) return 0;
    
    const minSwaps = (arr) => {
        const n = arr.length;
        const pairs = arr.map((v, i) => [v, i]);
        pairs.sort((a, b) => a[0] - b[0]); // sort by value
        const visited = new Array(n).fill(false);
        let swaps = 0;
        for (let i = 0; i < n; i++) {
            if (visited[i] || pairs[i][1] === i) continue;
            let cycleSize = 0;
            let j = i;
            while (!visited[j]) {
                visited[j] = true;
                j = pairs[j][1];
                cycleSize++;
            }
            swaps += cycleSize - 1;
        }
        return swaps;
    };
    
    const queue = [root];
    let front = 0;
    let totalSwaps = 0;
    
    while (front < queue.length) {
        const levelCount = queue.length - front; // nodes at current level
        const levelVals = [];
        for (let i = 0; i < levelCount; i++) {
            const node = queue[front++];
            levelVals.push(node.val);
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        totalSwaps += minSwaps(levelVals);
    }
    
    return totalSwaps;
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

function minimumOperations(root: TreeNode | null): number {
    if (!root) return 0;
    const queue: TreeNode[] = [root];
    let head = 0;
    let totalSwaps = 0;

    while (head < queue.length) {
        const levelSize = queue.length - head;
        const values: number[] = new Array(levelSize);
        for (let i = 0; i < levelSize; i++) {
            const node = queue[head++];
            values[i] = node.val;
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        totalSwaps += minSwapsToSort(values);
    }

    return totalSwaps;
}

function minSwapsToSort(arr: number[]): number {
    const n = arr.length;
    const pairs: [number, number][] = arr.map((val, idx) => [val, idx]);
    pairs.sort((a, b) => a[0] - b[0]); // sort by value

    const visited = new Array<boolean>(n).fill(false);
    let swaps = 0;

    for (let i = 0; i < n; i++) {
        if (visited[i] || pairs[i][1] === i) continue;
        let cycleSize = 0;
        let j = i;
        while (!visited[j]) {
            visited[j] = true;
            j = pairs[j][1];
            cycleSize++;
        }
        if (cycleSize > 0) swaps += cycleSize - 1;
    }

    return swaps;
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
     * @return int
     */
    function minimumOperations($root) {
        if ($root === null) return 0;

        $queue = new SplQueue();
        $queue->enqueue($root);
        $totalSwaps = 0;

        while (!$queue->isEmpty()) {
            $levelSize = $queue->count();
            $levelVals = [];

            for ($i = 0; $i < $levelSize; $i++) {
                /** @var TreeNode $node */
                $node = $queue->dequeue();
                $levelVals[] = $node->val;

                if ($node->left !== null) {
                    $queue->enqueue($node->left);
                }
                if ($node->right !== null) {
                    $queue->enqueue($node->right);
                }
            }

            $totalSwaps += $this->minSwaps($levelVals);
        }

        return $totalSwaps;
    }

    /**
     * Calculate minimum swaps to sort the array in strictly increasing order.
     *
     * @param int[] $arr
     * @return int
     */
    private function minSwaps(array $arr): int {
        $n = count($arr);
        if ($n <= 1) return 0;

        $sorted = $arr;
        sort($sorted, SORT_NUMERIC);

        // Map value to its current index in $arr
        $pos = [];
        foreach ($arr as $idx => $val) {
            $pos[$val] = $idx;
        }

        $swaps = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($arr[$i] != $sorted[$i]) {
                $swaps++;

                $targetVal = $sorted[$i];
                $j = $pos[$targetVal]; // index where target value currently resides

                // Swap arr[i] and arr[j]
                $temp = $arr[$i];
                $arr[$i] = $arr[$j];
                $arr[$j] = $temp;

                // Update positions in the map
                $pos[$temp] = $j;
                $pos[$targetVal] = $i;
            }
        }

        return $swaps;
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
    func minimumOperations(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }
        var queue: [TreeNode] = [root]
        var index = 0
        var totalSwaps = 0
        
        while index < queue.count {
            let levelCount = queue.count - index
            var values = [Int]()
            values.reserveCapacity(levelCount)
            
            for _ in 0..<levelCount {
                let node = queue[index]
                index += 1
                values.append(node.val)
                if let left = node.left { queue.append(left) }
                if let right = node.right { queue.append(right) }
            }
            
            totalSwaps += minSwaps(values)
        }
        
        return totalSwaps
    }
    
    private func minSwaps(_ arr: [Int]) -> Int {
        let n = arr.count
        var pairs = [(val: Int, idx: Int)]()
        pairs.reserveCapacity(n)
        for i in 0..<n {
            pairs.append((arr[i], i))
        }
        pairs.sort { $0.val < $1.val }
        
        var visited = [Bool](repeating: false, count: n)
        var swaps = 0
        
        for i in 0..<n {
            if visited[i] || pairs[i].idx == i {
                continue
            }
            var cycleSize = 0
            var j = i
            while !visited[j] {
                visited[j] = true
                j = pairs[j].idx
                cycleSize += 1
            }
            swaps += cycleSize - 1
        }
        return swaps
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
    fun minimumOperations(root: TreeNode?): Int {
        if (root == null) return 0
        val queue: ArrayDeque<TreeNode> = ArrayDeque()
        queue.add(root)
        var totalSwaps = 0
        while (queue.isNotEmpty()) {
            val levelSize = queue.size
            val levelVals = IntArray(levelSize)
            for (i in 0 until levelSize) {
                val node = queue.removeFirst()
                levelVals[i] = node.`val`
                node.left?.let { queue.add(it) }
                node.right?.let { queue.add(it) }
            }
            totalSwaps += minSwaps(levelVals)
        }
        return totalSwaps
    }

    private fun minSwaps(arr: IntArray): Int {
        val n = arr.size
        if (n <= 1) return 0
        val sorted = arr.clone()
        java.util.Arrays.sort(sorted)

        // map current value -> its index in the mutable array
        val posMap = HashMap<Int, Int>(n * 2)
        for (i in 0 until n) {
            posMap[arr[i]] = i
        }

        var swaps = 0
        val mutableArr = arr.clone()
        for (i in 0 until n) {
            if (mutableArr[i] == sorted[i]) continue
            swaps++
            val correctVal = sorted[i]
            val idxToSwap = posMap[correctVal]!!

            // perform swap
            val curVal = mutableArr[i]
            mutableArr[i] = correctVal
            mutableArr[idxToSwap] = curVal

            // update positions in map
            posMap[curVal] = idxToSwap
            posMap[correctVal] = i
        }
        return swaps
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
import 'dart:collection';

class Solution {
  int minimumOperations(TreeNode? root) {
    if (root == null) return 0;
    int totalSwaps = 0;
    Queue<TreeNode> queue = Queue<TreeNode>();
    queue.add(root);
    while (queue.isNotEmpty) {
      int levelSize = queue.length;
      List<int> values = [];
      for (int i = 0; i < levelSize; i++) {
        TreeNode node = queue.removeFirst();
        values.add(node.val);
        if (node.left != null) queue.add(node.left!);
        if (node.right != null) queue.add(node.right!);
      }
      totalSwaps += _minSwapsToSort(values);
    }
    return totalSwaps;
  }

  int _minSwapsToSort(List<int> arr) {
    int n = arr.length;
    List<int> sorted = List.from(arr)..sort();
    Map<int, int> targetPos = {};
    for (int i = 0; i < n; i++) {
      targetPos[sorted[i]] = i;
    }
    List<bool> visited = List.filled(n, false);
    int swaps = 0;
    for (int i = 0; i < n; i++) {
      if (visited[i] || targetPos[arr[i]] == i) continue;
      int cycleSize = 0;
      int j = i;
      while (!visited[j]) {
        visited[j] = true;
        j = targetPos[arr[j]]!;
        cycleSize++;
      }
      if (cycleSize > 0) swaps += cycleSize - 1;
    }
    return swaps;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func minimumOperations(root *TreeNode) int {
	if root == nil {
		return 0
	}
	queue := []*TreeNode{root}
	totalSwaps := 0

	for len(queue) > 0 {
		levelSize := len(queue)
		values := make([]int, levelSize)

		// collect current level values and enqueue children
		for i := 0; i < levelSize; i++ {
			node := queue[i]
			values[i] = node.Val
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		// remove processed nodes from the front of the slice
		queue = queue[levelSize:]

		totalSwaps += minSwaps(values)
	}

	return totalSwaps
}

// compute minimum number of swaps to sort arr (all elements unique)
func minSwaps(arr []int) int {
	n := len(arr)
	if n <= 1 {
		return 0
	}
	sorted := make([]int, n)
	copy(sorted, arr)
	sort.Ints(sorted)

	// map each value to its index in the sorted array
	pos := make(map[int]int, n)
	for i, v := range sorted {
		pos[v] = i
	}

	visited := make([]bool, n)
	swaps := 0

	for i := 0; i < n; i++ {
		if visited[i] || arr[i] == sorted[i] {
			visited[i] = true
			continue
		}
		cycleSize := 0
		j := i
		for !visited[j] {
			visited[j] = true
			val := arr[j]
			j = pos[val]
			cycleSize++
		}
		if cycleSize > 0 {
			swaps += cycleSize - 1
		}
	}
	return swaps
}
```

## Ruby

```ruby
def minimum_operations(root)
  return 0 unless root
  total = 0
  queue = [root]
  front = 0
  while front < queue.length
    level_size = queue.length - front
    values = []
    level_size.times do
      node = queue[front]
      front += 1
      values << node.val
      queue << node.left if node.left
      queue << node.right if node.right
    end
    total += min_swaps(values) if values.size > 1
  end
  total
end

def min_swaps(arr)
  n = arr.length
  pairs = arr.each_with_index.map { |v, i| [v, i] }
  pairs.sort_by! { |p| p[0] }
  visited = Array.new(n, false)
  swaps = 0
  (0...n).each do |i|
    next if visited[i] || pairs[i][1] == i
    cycle_size = 0
    j = i
    while !visited[j]
      visited[j] = true
      j = pairs[j][1]
      cycle_size += 1
    end
    swaps += cycle_size - 1 if cycle_size > 0
  end
  swaps
end
```

## Scala

```scala
import scala.collection.mutable.{Queue, ArrayBuffer}

object Solution {
  def minimumOperations(root: TreeNode): Int = {
    val queue = Queue[TreeNode]()
    queue.enqueue(root)
    var totalSwaps = 0

    while (queue.nonEmpty) {
      val size = queue.size
      val levelVals = new Array[Int](size)

      for (i <- 0 until size) {
        val node = queue.dequeue()
        levelVals(i) = node.value
        if (node.left != null) queue.enqueue(node.left)
        if (node.right != null) queue.enqueue(node.right)
      }

      totalSwaps += minSwaps(levelVals)
    }

    totalSwaps
  }

  private def minSwaps(arr: Array[Int]): Int = {
    val n = arr.length
    if (n <= 1) return 0

    // Pair each value with its original index and sort by value
    val sorted = arr.zipWithIndex.sortBy(_._1).toArray

    val visited = new Array[Boolean](n)
    var swaps = 0

    for (i <- 0 until n) {
      if (!visited(i) && sorted(i)._2 != i) {
        var cycleSize = 0
        var j = i
        while (!visited(j)) {
          visited(j) = true
          j = sorted(j)._2
          cycleSize += 1
        }
        swaps += (cycleSize - 1)
      }
    }

    swaps
  }
}
```

## Rust

```rust
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

use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn minimum_operations(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return 0;
        }
        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        queue.push_back(root.unwrap());
        let mut total_swaps: i64 = 0;

        while !queue.is_empty() {
            let level_len = queue.len();
            let mut values: Vec<i32> = Vec::with_capacity(level_len);
            for _ in 0..level_len {
                if let Some(node_rc) = queue.pop_front() {
                    let node_ref = node_rc.borrow();
                    values.push(node_ref.val);
                    if let Some(left) = &node_ref.left {
                        queue.push_back(Rc::clone(left));
                    }
                    if let Some(right) = &node_ref.right {
                        queue.push_back(Rc::clone(right));
                    }
                }
            }

            let n = values.len();
            if n > 1 {
                // Pair each value with its original index.
                let mut pairs: Vec<(i32, usize)> = values
                    .iter()
                    .cloned()
                    .enumerate()
                    .map(|(idx, val)| (val, idx))
                    .collect();

                // Sort by value to know target positions.
                pairs.sort_by_key(|k| k.0);

                let mut visited = vec![false; n];
                for i in 0..n {
                    if visited[i] || pairs[i].1 == i {
                        continue;
                    }
                    let mut cycle_size = 0usize;
                    let mut j = i;
                    while !visited[j] {
                        visited[j] = true;
                        j = pairs[j].1;
                        cycle_size += 1;
                    }
                    total_swaps += (cycle_size - 1) as i64;
                }
            }
        }

        total_swaps as i32
    }
}
```

## Racket

```racket
#lang racket
(require racket/queue)

;; Definition for a binary tree node.
(struct tree-node (val left right) #:mutable #:transparent)

(define (make-tree-node [val 0])
  (tree-node val #f #f))

;; Helper: minimum swaps to sort a vector of distinct integers
(define (min-swaps vals)
  (let* ([n (vector-length vals)]
         ;; pair each value with its original index
         [pairs (for/list ([i (in-range n)])
                  (cons (vector-ref vals i) i))]
         ;; sort pairs by value
         [sorted-pairs (sort pairs (lambda (a b) (< (car a) (car b))))]
         [sorted-vec (list->vector sorted-pairs)]
         [visited (make-vector n #f)])
    (let ([swaps 0])
      (for ([i (in-range n)])
        (when (and (not (vector-ref visited i))
                   (not (= (cdr (vector-ref sorted-vec i)) i)))
          ;; explore cycle starting at i
          (define cycle-size 0)
          (define j i)
          (let loop ()
            (unless (vector-ref visited j)
              (vector-set! visited j #t)
              (set! cycle-size (+ cycle-size 1))
              (set! j (cdr (vector-ref sorted-vec j)))
              (loop))))
        (when (> cycle-size 0)
          (set! swaps (+ swaps (- cycle-size 1)))))
      swaps)))

;; Main function
(define/contract (minimum-operations root)
  (-> (or/c tree-node? #f) exact-integer?)
  (if (not root)
      0
      (let* ([q (make-queue)]
             [total (let loop-total () 0)]) ; placeholder for mutable total
        (enqueue! q root)
        (define total-swaps 0)
        (let bfs ()
          (when (> (queue-count q) 0)
            (define level-size (queue-count q))
            (define vals (make-vector level-size))
            (for ([i (in-range level-size)])
              (define node (dequeue! q))
              (vector-set! vals i (tree-node-val node))
              (when (tree-node-left node)
                (enqueue! q (tree-node-left node)))
              (when (tree-node-right node)
                (enqueue! q (tree-node-right node))))
            (set! total-swaps (+ total-swaps (min-swaps vals)))
            (bfs)))
        total-swaps)))
```

## Erlang

```erlang
%% Definition for a binary tree node.
-record(tree_node, {val = 0 :: integer(),
                    left = null :: 'null' | #tree_node{},
                    right = null :: 'null' | #tree_node{}}).

-spec minimum_operations(Root :: #tree_node{} | null) -> integer().
minimum_operations(Root) ->
    bfs(Root).

%% Breadth‑first traversal, level by level.
bfs(null) -> 0;
bfs(Root) ->
    Queue0 = queue:new(),
    Queue1 = queue:in(Root, Queue0),
    bfs_loop(Queue1, 0).

bfs_loop(Queue, Acc) ->
    case queue:is_empty(Queue) of
        true -> Acc;
        false ->
            LevelSize = queue:len(Queue),
            {LevelVals, NewQueue} = collect_level(LevelSize, Queue, []),
            Swaps = min_swaps(LevelVals),
            bfs_loop(NewQueue, Acc + Swaps)
    end.

%% Extract exactly N nodes from the front of the queue,
%% collecting their values and enqueuing their children.
collect_level(0, Q, Acc) ->
    {lists:reverse(Acc), Q};
collect_level(N, Q, Acc) when N > 0 ->
    case queue:out(Q) of
        {{value, Node, RestQ}} ->
            Val = Node#tree_node.val,
            Left = Node#tree_node.left,
            Right = Node#tree_node.right,
            Q1 = case Left of
                     null -> RestQ;
                     _ -> queue:in(Left, RestQ)
                 end,
            Q2 = case Right of
                     null -> Q1;
                     _ -> queue:in(Right, Q1)
                 end,
            collect_level(N - 1, Q2, [Val | Acc]);
        empty ->
            {lists:reverse(Acc), Q}
    end.

%% Minimum swaps to sort a list with distinct elements.
min_swaps([]) -> 0;
min_swaps(Values) ->
    Len = length(Values),
    Indexed = lists:zip(Values, lists:seq(0, Len - 1)),
    Sorted = lists:keysort(1, Indexed),               % sort by value
    Perm = [Idx || {_Val, Idx} <- Sorted],            % original index for each sorted position
    PermMap = maps:from_list(lists:zip(lists:seq(0, Len - 1), Perm)),
    count_swaps(PermMap, Len, 0, maps:new()).

%% Count swaps by summing (cycle_len‑1) over all cycles.
count_swaps(_PermMap, Len, Pos, _Visited) when Pos >= Len ->
    0;
count_swaps(PermMap, Len, Pos, Visited) ->
    case maps:is_key(Pos, Visited) of
        true ->
            count_swaps(PermMap, Len, Pos + 1, Visited);
        false ->
            {CycleLen, NewVisited} = explore_cycle(Pos, PermMap, Visited),
            SwapsHere = if CycleLen > 0 -> CycleLen - 1; true -> 0 end,
            SwapsRest = count_swaps(PermMap, Len, Pos + 1, NewVisited),
            SwapsHere + SwapsRest
    end.

%% Follow a permutation cycle and mark visited nodes.
explore_cycle(Pos, PermMap, Visited) ->
    case maps:is_key(Pos, Visited) of
        true -> {0, Visited};
        false ->
            Next = maps:get(Pos, PermMap),
            Vis1 = maps:put(Pos, true, Visited),
            {LenRest, Vis2} = explore_cycle(Next, PermMap, Vis1),
            {LenRest + 1, Vis2}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(root :: TreeNode.t() | nil) :: integer
  def minimum_operations(nil), do: 0

  def minimum_operations(root) do
    bfs([root], 0)
  end

  defp bfs([], acc), do: acc

  defp bfs(level_nodes, acc) do
    {values_rev, next_rev} =
      Enum.reduce(level_nodes, {[], []}, fn node, {vals, nxt} ->
        vals = [node.val | vals]

        nxt =
          case node.left do
            nil -> nxt
            l -> [l | nxt]
          end

        nxt =
          case node.right do
            nil -> nxt
            r -> [r | nxt]
          end

        {vals, nxt}
      end)

    values = Enum.reverse(values_rev)
    next_level = Enum.reverse(next_rev)

    swaps = min_swaps_to_sort(values)
    bfs(next_level, acc + swaps)
  end

  defp min_swaps_to_sort(arr) do
    sorted = Enum.sort(arr)

    pos_map =
      sorted
      |> Enum.with_index()
      |> Map.new(fn {val, idx} -> {val, idx} end)

    arr_t = List.to_tuple(arr)
    len = tuple_size(arr_t)
    visited = :erlang.make_tuple(len, false)

    {total_swaps, _vis} =
      0..(len - 1)
      |> Enum.reduce({0, visited}, fn i, {cnt, vis} ->
        if :erlang.element(i + 1, vis) do
          {cnt, vis}
        else
          target_idx = Map.fetch!(pos_map, elem(arr_t, i))

          if target_idx == i do
            new_vis = put_elem(vis, i + 1, true)
            {cnt, new_vis}
          else
            {cycle_len, new_vis} = traverse_cycle(i, arr_t, pos_map, vis, 0)
            {cnt + (cycle_len - 1), new_vis}
          end
        end
      end)

    total_swaps
  end

  defp traverse_cycle(idx, arr_t, pos_map, vis, acc) do
    if :erlang.element(idx + 1, vis) do
      {acc, vis}
    else
      vis = put_elem(vis, idx + 1, true)
      val = elem(arr_t, idx)
      next_idx = Map.fetch!(pos_map, val)
      traverse_cycle(next_idx, arr_t, pos_map, vis, acc + 1)
    end
  end
end
```
