# 2440. Create Components With Same Value

## Cpp

```cpp
class Solution {
public:
    int componentValue(vector<int>& nums, vector<vector<int>>& edges) {
        int n = nums.size();
        long long total = 0;
        for (int v : nums) total += v;
        
        vector<vector<int>> adj(n);
        for (auto &e : edges) {
            int a = e[0], b = e[1];
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
        
        // collect divisors of total sum
        vector<long long> divs;
        for (long long i = 1; i * i <= total; ++i) {
            if (total % i == 0) {
                divs.push_back(i);
                if (i != total / i) divs.push_back(total / i);
            }
        }
        sort(divs.begin(), divs.end());
        
        for (long long target : divs) {
            bool ok = true;
            function<long long(int,int)> dfs = [&](int u, int p) -> long long {
                long long cur = nums[u];
                for (int v : adj[u]) if (v != p) {
                    long long child = dfs(v, u);
                    if (!ok) return 0;
                    cur += child;
                }
                if (cur > target) { ok = false; return 0; }
                if (cur == target) {
                    // this subtree forms a component and is detached
                    return 0;
                }
                return cur;
            };
            
            long long rem = dfs(0, -1);
            if (ok && rem == 0) {
                long long components = total / target;
                return (int)(components - 1); // maximum deletions
            }
        }
        return 0; // fallback, should never reach because total itself always works
    }
};
```

## Java

```java
class Solution {
    private List<Integer>[] graph;
    private int[] vals;

    public int componentValue(int[] nums, int[][] edges) {
        int n = nums.length;
        vals = nums;
        graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }

        long total = 0;
        int maxVal = 0;
        for (int v : nums) {
            total += v;
            if (v > maxVal) maxVal = v;
        }

        List<Integer> divisors = new ArrayList<>();
        for (int i = 1; (long) i * i <= total; i++) {
            if (total % i == 0) {
                divisors.add(i);
                if ((int) (total / i) != i) divisors.add((int) (total / i));
            }
        }
        Collections.sort(divisors);

        int best = 0;
        for (int target : divisors) {
            if (target < maxVal) continue; // impossible, component must contain at least the largest node
            long remainder = dfs(0, -1, target);
            if (remainder == 0) {
                int components = (int) (total / target);
                best = Math.max(best, components - 1);
            }
        }
        return best;
    }

    private long dfs(int u, int parent, int target) {
        long sum = vals[u];
        for (int v : graph[u]) {
            if (v == parent) continue;
            long child = dfs(v, u, target);
            if (child == -1) return -1;
            sum += child;
            if (sum > target) return -1; // exceeds target, cannot partition
        }
        if (sum == target) return 0; // this subtree forms a component and is cut off
        return sum; // less than target, propagate upward
    }
}
```

## Python

```python
class Solution(object):
    def componentValue(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        import sys
        sys.setrecursionlimit(30000)
        n = len(nums)
        total = sum(nums)
        max_num = max(nums)

        # build adjacency list
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        # generate divisors of total (possible component sums)
        divs = []
        i = 1
        while i * i <= total:
            if total % i == 0:
                divs.append(i)
                if i != total // i:
                    divs.append(total // i)
            i += 1
        # sort ascending to try smallest component sum first (most components)
        divs.sort()

        def feasible(target):
            """return True if we can split tree into components each summing to target"""
            def dfs(u, p):
                cur = nums[u]
                for v in g[u]:
                    if v == p:
                        continue
                    child = dfs(v, u)
                    if child == -1:   # impossible downstream
                        return -1
                    cur += child
                if cur == target:
                    return 0          # cut here, component formed
                if cur < target:
                    return cur        # propagate upward
                return -1              # exceeds target -> impossible

            root_res = dfs(0, -1)
            return root_res == 0

        for comp_sum in divs:
            if comp_sum < max_num:
                continue
            if feasible(comp_sum):
                components = total // comp_sum
                return components - 1
        return 0
```

## Python3

```python
from typing import List
import sys

class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        total = sum(nums)
        if n == 1:
            return 0

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        sys.setrecursionlimit(10 ** 6)

        def can_partition(target: int) -> bool:
            feasible = True

            def dfs(u: int, parent: int) -> int:
                nonlocal feasible
                cur = nums[u]
                for v in graph[u]:
                    if v == parent:
                        continue
                    sub = dfs(v, u)
                    cur += sub
                if cur == target:
                    return 0
                if cur > target:
                    feasible = False
                return cur

            root_sum = dfs(0, -1)
            return feasible and root_sum == 0

        # collect all possible component counts (divisors of total)
        comps = []
        i = 1
        while i * i <= total:
            if total % i == 0:
                comps.append(i)
                if i != total // i:
                    comps.append(total // i)
            i += 1
        comps.sort(reverse=True)

        for c in comps:
            if c > n:   # cannot have more components than nodes
                continue
            target = total // c
            if can_partition(target):
                return c - 1  # deletions = components - 1

        return 0
```

## C

```c
#include <stdlib.h>

static int n;
static int *nodeVals;
static int *head;
static int *toArr;
static int *nextArr;
static int compCount;

static long long dfs(int u, int parent, int target) {
    long long sum = nodeVals[u];
    for (int e = head[u]; e != -1; e = nextArr[e]) {
        int v = toArr[e];
        if (v == parent) continue;
        sum += dfs(v, u, target);
    }
    if (sum == target) {
        compCount++;
        return 0;
    }
    return sum;
}

int componentValue(int* nums, int numsSize, int** edges, int edgesSize, int* edgesColSize){
    n = numsSize;
    nodeVals = nums;

    // Build adjacency list
    head = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;
    int m = edgesSize;               // n-1
    int maxE = 2 * m;
    toArr   = (int*)malloc(maxE * sizeof(int));
    nextArr = (int*)malloc(maxE * sizeof(int));

    int idx = 0;
    for (int i = 0; i < m; ++i) {
        int a = edges[i][0];
        int b = edges[i][1];
        toArr[idx] = b; nextArr[idx] = head[a]; head[a] = idx++; // a -> b
        toArr[idx] = a; nextArr[idx] = head[b]; head[b] = idx++; // b -> a
    }

    long long total = 0;
    int maxVal = 0;
    for (int i = 0; i < n; ++i) {
        total += nodeVals[i];
        if (nodeVals[i] > maxVal) maxVal = nodeVals[i];
    }

    // Try component counts from n down to 1
    for (int c = n; c >= 1; --c) {
        if (total % c != 0) continue;
        int target = (int)(total / c);
        if (target < maxVal) continue;

        compCount = 0;
        long long rem = dfs(0, -1, target);
        if (rem == 0 && compCount == c) {
            // clean up
            free(head);
            free(toArr);
            free(nextArr);
            return c - 1;   // number of deletions
        }
    }

    // clean up
    free(head);
    free(toArr);
    free(nextArr);
    return 0;
}
```

## Csharp

```csharp
public class Solution {
    public int ComponentValue(int[] nums, int[][] edges) {
        int n = nums.Length;
        long totalSumLong = 0;
        foreach (var v in nums) totalSumLong += v;
        int totalSum = (int)totalSumLong; // fits within int constraints

        // Build adjacency list
        List<int>[] graph = new List<int>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<int>();
        foreach (var e in edges) {
            int a = e[0], b = e[1];
            graph[a].Add(b);
            graph[b].Add(a);
        }

        // Prepare parent array and postorder traversal order
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = -2;
        List<int> order = new List<int>(n);
        Stack<int> stack = new Stack<int>();
        stack.Push(0);
        parent[0] = -1;
        while (stack.Count > 0) {
            int u = stack.Pop();
            order.Add(u);
            foreach (int v in graph[u]) {
                if (parent[v] == -2) {
                    parent[v] = u;
                    stack.Push(v);
                }
            }
        }
        order.Reverse(); // now children before parents

        // Get all divisors of totalSum sorted ascending
        List<int> divisors = new List<int>();
        for (int i = 1; i * (long)i <= totalSum; i++) {
            if (totalSum % i == 0) {
                divisors.Add(i);
                if (i != totalSum / i) divisors.Add(totalSum / i);
            }
        }
        divisors.Sort();

        foreach (int target in divisors) {
            int[] sum = (int[])nums.Clone();
            bool ok = true;
            foreach (int node in order) {
                foreach (int nb in graph[node]) {
                    if (nb == parent[node]) continue;
                    sum[node] += sum[nb];
                }
                if (sum[node] == target) {
                    sum[node] = 0; // cut here
                } else if (sum[node] > target) {
                    ok = false;
                    break;
                }
            }
            if (ok && sum[0] == 0) {
                int components = totalSum / target;
                return components - 1;
            }
        }

        return 0; // fallback, should not reach because totalSum itself is always a divisor
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} edges
 * @return {number}
 */
var componentValue = function(nums, edges) {
    const n = nums.length;
    const adj = Array.from({length: n}, () => []);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
    }

    // Build parent array and post-order traversal list
    const parent = new Array(n).fill(-1);
    parent[0] = 0;
    const order = [];
    const stack = [0];
    while (stack.length) {
        const u = stack.pop();
        order.push(u);
        for (const v of adj[u]) {
            if (parent[v] === -1) {
                parent[v] = u;
                stack.push(v);
            }
        }
    }
    order.reverse(); // post-order: children before parent

    const totalSum = nums.reduce((a, b) => a + b, 0);

    // Get all divisors of totalSum (possible component sums)
    const divisors = [];
    for (let i = 1; i * i <= totalSum; ++i) {
        if (totalSum % i === 0) {
            divisors.push(i);
            if (i !== totalSum / i) divisors.push(totalSum / i);
        }
    }

    let maxComponents = 1; // at least the whole tree

    for (const target of divisors) {
        const compCount = totalSum / target;
        if (compCount <= maxComponents) continue; // we need more components
        const sumArr = new Array(n);
        for (let i = 0; i < n; ++i) sumArr[i] = nums[i];
        let ok = true;
        for (const u of order) {
            if (sumArr[u] > target) { ok = false; break; }
            if (sumArr[u] === target) sumArr[u] = 0;
            if (u !== 0) sumArr[parent[u]] += sumArr[u];
        }
        if (ok && sumArr[0] === 0) {
            maxComponents = compCount;
        }
    }

    return maxComponents - 1; // edges removed
};
```

## Typescript

```typescript
function componentValue(nums: number[], edges: number[][]): number {
    const n = nums.length;
    if (n === 1) return 0;

    // build adjacency list
    const graph: number[][] = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        graph[a].push(b);
        graph[b].push(a);
    }

    // root the tree at node 0 and get parent & order (preorder)
    const parent = new Int32Array(n).fill(-1);
    const order: number[] = [];
    const stack: number[] = [0];
    while (stack.length) {
        const u = stack.pop()!;
        order.push(u);
        for (const v of graph[u]) {
            if (v !== parent[u]) {
                parent[v] = u;
                stack.push(v);
            }
        }
    }

    const totalSum = nums.reduce((a, b) => a + b, 0);

    // collect all divisors of totalSum
    const divs: number[] = [];
    for (let i = 1; i * i <= totalSum; ++i) {
        if (totalSum % i === 0) {
            divs.push(i);
            if (i !== totalSum / i) divs.push(totalSum / i);
        }
    }
    divs.sort((a, b) => a - b); // ascending component sum

    const sums = new Int32Array(n);

    for (const target of divs) {
        // try to partition with each component sum = target
        let ok = true;
        for (let i = order.length - 1; i >= 0; --i) {
            const u = order[i];
            let cur = nums[u];
            for (const v of graph[u]) {
                if (v === parent[u]) continue;
                cur += sums[v];
            }
            if (cur === target) {
                sums[u] = 0; // cut here
            } else if (cur > target) {
                ok = false;
                break;
            } else {
                sums[u] = cur;
            }
        }
        if (ok && sums[0] === 0) {
            const components = totalSum / target;
            return components - 1; // deletions = components - 1
        }
    }

    return 0;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer[][] $edges
     * @return Integer
     */
    function componentValue($nums, $edges) {
        $n = count($nums);
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }
        $total = array_sum($nums);
        $divs = [];
        for ($i = 1; $i * $i <= $total; $i++) {
            if ($total % $i == 0) {
                $divs[] = $i;
                if ($i != intdiv($total, $i)) {
                    $divs[] = intdiv($total, $i);
                }
            }
        }
        sort($divs);
        foreach ($divs as $d) {
            if ($this->canPartition($d, $nums, $adj, $n)) {
                return intdiv($total, $d) - 1;
            }
        }
        return 0;
    }

    private function canPartition($d, $nums, $adj, $n) {
        $parent = array_fill(0, $n, -2);
        $order = [];
        $stack = [0];
        $parent[0] = -1;
        while (!empty($stack)) {
            $node = array_pop($stack);
            $order[] = $node;
            foreach ($adj[$node] as $nei) {
                if ($nei === $parent[$node]) continue;
                $parent[$nei] = $node;
                $stack[] = $nei;
            }
        }
        $rem = array_fill(0, $n, 0);
        for ($idx = count($order) - 1; $idx >= 0; $idx--) {
            $u = $order[$idx];
            $sum = $nums[$u] % $d;
            foreach ($adj[$u] as $v) {
                if ($parent[$v] === $u) { // child
                    $sum = ($sum + $rem[$v]) % $d;
                }
            }
            $rem[$u] = $sum;
        }
        return $rem[0] == 0;
    }
}
```

## Swift

```swift
class Solution {
    func componentValue(_ nums: [Int], _ edges: [[Int]]) -> Int {
        let n = nums.count
        var adj = Array(repeating: [Int](), count: n)
        for e in edges {
            let a = e[0]
            let b = e[1]
            adj[a].append(b)
            adj[b].append(a)
        }
        
        // Build parent array and traversal order (preorder)
        var parent = Array(repeating: -1, count: n)
        var stack = [Int]()
        var order = [Int]()
        stack.append(0)
        while let node = stack.popLast() {
            order.append(node)
            for nb in adj[node] where nb != parent[node] {
                parent[nb] = node
                stack.append(nb)
            }
        }
        
        let total = nums.reduce(0, +)
        var divisors = [Int]()
        var i = 1
        while i * i <= total {
            if total % i == 0 {
                divisors.append(i)
                if i != total / i {
                    divisors.append(total / i)
                }
            }
            i += 1
        }
        divisors.sort()
        
        let maxNum = nums.max()!
        var bestComponents = 1   // at least whole tree as one component
        
        for v in divisors {
            if v < maxNum { continue }          // a single node cannot exceed component sum
            var sums = nums                     // mutable copy
            var ok = true
            // process nodes bottom‑up
            for node in order.reversed() {
                let cur = sums[node]
                if cur == v {
                    sums[node] = 0               // cut here
                } else if cur > v {
                    ok = false
                    break
                }
                let p = parent[node]
                if p != -1 && sums[node] != 0 {
                    sums[p] += sums[node]
                }
            }
            if ok && sums[0] == 0 {
                // successful partition, number of components = total / v
                bestComponents = total / v
                break   // smallest v gives maximum deletions
            }
        }
        return bestComponents - 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun componentValue(nums: IntArray, edges: Array<IntArray>): Int {
        val n = nums.size
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val a = e[0]
            val b = e[1]
            adj[a].add(b)
            adj[b].add(a)
        }

        val total = nums.sum()
        // collect all divisors of total
        val divs = mutableListOf<Int>()
        var i = 1
        while (i * i <= total) {
            if (total % i == 0) {
                divs.add(i)
                if (i != total / i) divs.add(total / i)
            }
            i++
        }
        divs.sort()

        fun can(target: Int): Boolean {
            var ok = true
            fun dfs(u: Int, p: Int): Int {
                var cur = nums[u]
                for (v in adj[u]) {
                    if (v == p) continue
                    val child = dfs(v, u)
                    cur += child
                }
                if (cur > target) {
                    ok = false
                    return 0
                }
                return if (cur == target) 0 else cur
            }
            val rootRem = dfs(0, -1)
            return ok && rootRem == 0
        }

        var answer = 0
        for (target in divs) {
            if (can(target)) {
                answer = total / target - 1
                break
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int componentValue(List<int> nums, List<List<int>> edges) {
    int n = nums.length;
    List<List<int>> g = List.generate(n, (_) => []);
    for (var e in edges) {
      int a = e[0];
      int b = e[1];
      g[a].add(b);
      g[b].add(a);
    }

    int total = 0;
    for (int v in nums) total += v;

    List<int> divisors = [];
    for (int i = 1; i * i <= total; ++i) {
      if (total % i == 0) {
        divisors.add(i);
        if (i != total ~/ i) divisors.add(total ~/ i);
      }
    }
    divisors.sort();

    bool canPartition(int target) {
      bool ok = true;
      int dfs(int u, int p) {
        int sum = nums[u];
        for (int v in g[u]) {
          if (v == p) continue;
          int sub = dfs(v, u);
          sum += sub;
        }
        if (sum == target) return 0;
        if (sum > target) ok = false;
        return sum;
      }

      int rootSum = dfs(0, -1);
      return ok && rootSum == 0;
    }

    for (int d in divisors) {
      if (canPartition(d)) {
        return total ~/ d - 1;
      }
    }
    return 0;
  }
}
```

## Golang

```go
func componentValue(nums []int, edges [][]int) int {
    n := len(nums)
    adj := make([][]int, n)
    for _, e := range edges {
        a, b := e[0], e[1]
        adj[a] = append(adj[a], b)
        adj[b] = append(adj[b], a)
    }

    total := 0
    maxVal := 0
    for _, v := range nums {
        total += v
        if v > maxVal {
            maxVal = v
        }
    }

    // collect divisors of total sum
    divs := make([]int, 0)
    for i := 1; i*i <= total; i++ {
        if total%i == 0 {
            divs = append(divs, i)
            if i != total/i {
                divs = append(divs, total/i)
            }
        }
    }
    sort.Ints(divs)

    var dfs func(int, int, int) int
    possible := true

    dfs = func(u, parent, target int) int {
        sum := nums[u]
        for _, v := range adj[u] {
            if v == parent {
                continue
            }
            childSum := dfs(v, u, target)
            if !possible {
                return 0
            }
            sum += childSum
        }
        if sum == target {
            return 0 // this subtree forms a component
        }
        if sum < target {
            return sum
        }
        possible = false
        return 0
    }

    for _, d := range divs {
        if d < maxVal {
            continue
        }
        possible = true
        rootRem := dfs(0, -1, d)
        if possible && rootRem == 0 {
            components := total / d
            return components - 1
        }
    }
    return 0
}
```

## Ruby

```ruby
def component_value(nums, edges)
  n = nums.length
  adj = Array.new(n) { [] }
  edges.each do |a, b|
    adj[a] << b
    adj[b] << a
  end

  parent = Array.new(n, -1)
  order = []
  stack = [0]
  while (node = stack.pop)
    order << node
    adj[node].each do |nb|
      next if nb == parent[node]
      parent[nb] = node
      stack << nb
    end
  end

  total = nums.sum
  divisors = []
  i = 1
  while i * i <= total
    if total % i == 0
      divisors << i
      d2 = total / i
      divisors << d2 if d2 != i
    end
    i += 1
  end
  divisors.sort!

  divisors.each do |target|
    components = total / target
    next if components > n

    sum = Array.new(n, 0)
    possible = true
    order.reverse_each do |node|
      cur = nums[node]
      adj[node].each do |nb|
        next if nb == parent[node]
        cur += sum[nb]
      end
      if cur == target
        sum[node] = 0
      elsif cur < target
        sum[node] = cur
      else
        possible = false
        break
      end
    end

    return components - 1 if possible && sum[0] == 0
  end

  0
end
```

## Scala

```scala
object Solution {
  def componentValue(nums: Array[Int], edges: Array[Array[Int]]): Int = {
    val n = nums.length
    if (n == 1) return 0

    // build adjacency list
    val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
    for (e <- edges) {
      val a = e(0)
      val b = e(1)
      adj(a).append(b)
      adj(b).append(a)
    }

    // parent array and traversal order (preorder, later used reversed for postorder)
    val parent = new Array[Int](n)
    val order = new scala.collection.mutable.ArrayBuffer[Int]()
    val stack = new scala.collection.mutable.Stack[Int]()
    stack.push(0)
    parent(0) = -1
    while (stack.nonEmpty) {
      val u = stack.pop()
      order.append(u)
      for (v <- adj(u)) {
        if (v != parent(u)) {
          parent(v) = u
          stack.push(v)
        }
      }
    }

    // function to test if we can partition with component sum = target
    def can(target: Int): Boolean = {
      val cur = new Array[Int](n)
      var i = order.length - 1
      while (i >= 0) {
        val u = order(i)
        var subtotal = nums(u)
        for (v <- adj(u)) {
          if (v != parent(u)) {
            subtotal += cur(v)
          }
        }
        if (subtotal == target) {
          cur(u) = 0
        } else if (subtotal < target) {
          cur(u) = subtotal
        } else {
          return false
        }
        i -= 1
      }
      cur(0) == 0
    }

    val total = nums.sum
    var answer = 0

    // enumerate all divisors of total sum
    val divs = new scala.collection.mutable.ArrayBuffer[Int]()
    var d = 1
    while (d * d <= total) {
      if (total % d == 0) {
        divs.append(d)
        if (d != total / d) divs.append(total / d)
      }
      d += 1
    }

    for (target <- divs) {
      val components = total / target
      // deletions = components - 1
      if (components - 1 > answer && can(target)) {
        answer = components - 1
      }
    }

    answer
  }
}
```

## Rust

```rust
impl Solution {
    pub fn component_value(nums: Vec<i32>, edges: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        if n == 1 {
            return 0;
        }
        // build adjacency list
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in edges.iter() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            adj[a].push(b);
            adj[b].push(a);
        }

        // root the tree at 0, get parent array and traversal order
        let mut parent: Vec<usize> = vec![n; n];
        let mut order: Vec<usize> = Vec::with_capacity(n);
        let mut stack: Vec<usize> = vec![0];
        parent[0] = n;
        while let Some(u) = stack.pop() {
            order.push(u);
            for &v in adj[u].iter() {
                if v == parent[u] {
                    continue;
                }
                parent[v] = u;
                stack.push(v);
            }
        }

        // total sum
        let total: i32 = nums.iter().sum();

        // collect all divisors of total
        let mut divs: Vec<i32> = Vec::new();
        let limit = (total as f64).sqrt() as i32;
        for d in 1..=limit {
            if total % d == 0 {
                divs.push(d);
                if d != total / d {
                    divs.push(total / d);
                }
            }
        }
        divs.sort_unstable(); // ascending component sum

        // helper to test a candidate component sum
        let mut feasible = |target: i32| -> bool {
            let mut residual: Vec<i32> = vec![0; n];
            for &u in order.iter().rev() {
                let mut sum = nums[u];
                for &v in adj[u].iter() {
                    if v == parent[u] {
                        continue;
                    }
                    sum += residual[v];
                }
                if sum == target {
                    residual[u] = 0; // cut here
                } else if sum < target {
                    residual[u] = sum;
                } else {
                    return false;
                }
            }
            residual[0] == 0
        };

        for &v in divs.iter() {
            if feasible(v) {
                let components = total / v;
                return (components - 1) as i32;
            }
        }
        0
    }
}
```

## Racket

```racket
(define (component-value nums edges)
  (let* ((n (length nums))
         (vals (list->vector nums))
         (adj (make-vector n '()))
         (_ (for-each (lambda (e)
                        (let ((a (first e)) (b (second e)))
                          (vector-set! adj a (cons b (vector-ref adj a)))
                          (vector-set! adj b (cons a (vector-ref adj b)))))
                      edges))
         (total (apply + nums))
         (divisors
           (let loop ((i 1) (res '()))
             (if (> (* i i) total)
                 (sort res <)
                 (let ((new-res (if (= (remainder total i) 0)
                                    (let ((j (/ total i)))
                                      (if (= i j) (cons i res) (cons i (cons j res))))
                                    res)))
                   (loop (+ i 1) new-res)))))
         (max-deletions 0))
    (for ([t divisors])
      (when (< t total)
        (define cnt (box 0))
        (define (dfs u parent)
          (let ((sum (vector-ref vals u)))
            (for ([v (vector-ref adj u)])
              (unless (= v parent)
                (let ((child-sum (dfs v u)))
                  (cond
                    [(= child-sum -1) (set! sum -1)]
                    [(and (not (= sum -1)) (not (= child-sum -1)))
                     (set! sum (+ sum child-sum))]))))
            (cond
              [(= sum -1) -1]
              [(= sum t)
               (set-box! cnt (+ (unbox cnt) 1))
               0]
              [(< sum t) sum]
              [else -1])))
        (let ((root-sum (dfs 0 -1)))
          (when (and (= root-sum 0) (> (unbox cnt) 0))
            (set! max-deletions (max max-deletions (- (unbox cnt) 1)))))))
    max-deletions))
```

## Erlang

```erlang
-spec component_value(Nums :: [integer()], Edges :: [[integer()]]) -> integer().
component_value(Nums, Edges) ->
    N = length(Nums),
    Adj0 = maps:from_list([{I, []} || I <- lists:seq(0, N - 1)]),
    Adj = build_adj(Adj0, Edges),
    Total = lists:sum(Nums),
    Divs = divisors(Total),
    SortedDivs = lists:sort(Divs),
    NumTuple = list_to_tuple(Nums),
    find_max_deletions(SortedDivs, Total, Adj, NumTuple).

%% Build adjacency map
build_adj(Map, []) -> Map;
build_adj(Map, [[A, B] | Rest]) ->
    Map1 = maps:update_with(A,
            fun(L) -> [B | L] end,
            [B],
            Map),
    Map2 = maps:update_with(B,
            fun(L) -> [A | L] end,
            [A],
            Map1),
    build_adj(Map2, Rest).

%% All divisors of S
divisors(S) -> divisors(1, S, []).

divisors(I, S, Acc) when I * I > S ->
    Acc;
divisors(I, S, Acc) ->
    if S rem I =:= 0 ->
            D1 = I,
            D2 = S div I,
            NewAcc = [D1 | Acc],
            FinalAcc = if D2 =/= D1 -> [D2 | NewAcc]; true -> NewAcc end,
            divisors(I + 1, S, FinalAcc);
       true ->
            divisors(I + 1, S, Acc)
    end.

%% Find maximal deletions
find_max_deletions([], _Total, _Adj, _NumTuple) -> 0;
find_max_deletions([Target | Rest], Total, Adj, NumTuple) ->
    case Target of
        Total -> 0; % cannot delete any edge
        _ ->
            case check(Target, Adj, NumTuple, 0, -1) of
                error -> find_max_deletions(Rest, Total, Adj, NumTuple);
                {ok, _} -> (Total div Target) - 1
            end
    end.

%% Check feasibility for a given target sum
check(Target, Adj, NumTuple, Node, Parent) ->
    Neigh = maps:get(Node, Adj),
    case process_children(Neigh, Target, Adj, NumTuple, Node, Parent, 0) of
        error -> error;
        {ok, SumMod} ->
            Value = element(Node + 1, NumTuple),
            TotalMod = (SumMod + Value) rem Target,
            if TotalMod =:= 0 -> {ok, 0};
               true -> {ok, TotalMod}
            end
    end.

process_children([], _Target, _Adj, _NumTuple, _Node, _Parent, Acc) ->
    {ok, Acc};
process_children([Child | Rest], Target, Adj, NumTuple, Node, Parent, Acc) ->
    if Child =:= Parent ->
            process_children(Rest, Target, Adj, NumTuple, Node, Parent, Acc);
       true ->
            case check(Target, Adj, NumTuple, Child, Node) of
                error -> error;
                {ok, Mod} ->
                    NewAcc = (Acc + Mod) rem Target,
                    process_children(Rest, Target, Adj, NumTuple, Node, Parent, NewAcc)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec component_value(nums :: [integer], edges :: [[integer]]) :: integer
  def component_value(nums, edges) do
    n = length(nums)
    total_sum = Enum.sum(nums)

    # Build adjacency map
    adj =
      Enum.reduce(edges, %{}, fn [a, b], acc ->
        acc
        |> Map.update(a, [b], &[b | &1])
        |> Map.update(b, [a], &[a | &1])
      end)

    # Build parent array and postorder list using iterative DFS
    {parent_arr, order} = build_parent_and_order(adj, n)

    postorder = Enum.reverse(order)

    # Get all divisors of total_sum sorted ascending
    divisors =
      1..:math.floor(:math.sqrt(total_sum)) |> Enum.reduce([], fn i, acc ->
        if rem(total_sum, i) == 0 do
          d2 = div(total_sum, i)
          acc = [i | acc]
          if d2 != i, do: [d2 | acc], else: acc
        else
          acc
        end
      end)
      |> Enum.uniq()
      |> Enum.sort()

    # Try each divisor as target component sum
    Enum.reduce_while(divisors, 0, fn t, _acc ->
      if possible?(t, nums, parent_arr, postorder) do
        components = div(total_sum, t)
        deletions = components - 1
        {:halt, deletions}
      else
        {:cont, 0}
      end
    end)
  end

  defp build_parent_and_order(adj, n) do
    parent_arr = :array.new(n, -1)
    stack = [0]
    order = []

    {parent_arr, order} =
      Enum.reduce_while(stack, {parent_arr, order}, fn _ , acc ->
        # This reduce_while is just to use a loop; we'll implement manually
        {:halt, acc}
      end)

    # Manual iterative DFS
    parent_arr = :array.set(0, -2, parent_arr) # root has no parent
    stack = [0]
    order = []

    while_stack = fn ->
      case stack do
        [] -> :done
        [u | rest] ->
          stack = rest
          order = [u | order]
          neighbors = Map.get(adj, u, [])
          Enum.each(neighbors, fn v ->
            if :array.get(v, parent_arr) == -1 do
              parent_arr = :array.set(v, u, parent_arr)
              stack = [v | stack]
            end
          end)
          {:continue, {parent_arr, order, stack}}
      end
    end

    # Loop simulation
    loop = fn loop_fun ->
      case while_stack.() do
        :done -> :ok
        {:continue, state} -> loop_fun.(loop_fun)
      end
    end

    loop.(fn f -> f.(f) end)

    {parent_arr, order}
  end

  defp possible?(t, nums, parent_arr, postorder) do
    # Initialize residues array with nums mod t
    residues =
      Enum.map(nums, fn v -> rem(v, t) end)
      |> :array.from_list()

    residues = Enum.reduce(postorder, residues, fn u, res_arr ->
      r = :array.get(u, res_arr)

      if u != 0 do
        p = :array.get(u, parent_arr)
        new_val = rem(:array.get(p, res_arr) + r, t)
        :array.set(p, new_val, res_arr)
      else
        res_arr
      end
    end)

    :array.get(0, residues) == 0
  end
end
```
