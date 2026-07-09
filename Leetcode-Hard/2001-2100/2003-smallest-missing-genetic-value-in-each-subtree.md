# 2003. Smallest Missing Genetic Value in Each Subtree

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> smallestMissingValueSubtree(vector<int>& parents, vector<int>& nums) {
        int n = parents.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; ++i) {
            children[parents[i]].push_back(i);
        }
        
        int pos = -1;
        for (int i = 0; i < n; ++i) if (nums[i] == 1) { pos = i; break; }
        vector<int> ans(n, 1);
        if (pos == -1) return ans; // 1 missing everywhere
        
        const int MAXV = 200005;
        vector<char> present(MAXV, false);
        vector<char> visitedNode(n, false);
        
        auto addSubtree = [&](int start) {
            stack<int> st;
            st.push(start);
            while (!st.empty()) {
                int u = st.top(); st.pop();
                if (visitedNode[u]) continue;
                visitedNode[u] = true;
                present[nums[u]] = true;
                for (int v : children[u]) {
                    if (!visitedNode[v]) st.push(v);
                }
            }
        };
        
        int mex = 1;
        int cur = pos;
        while (cur != -1) {
            addSubtree(cur);
            while (mex < MAXV && present[mex]) ++mex;
            ans[cur] = mex;
            cur = parents[cur];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] smallestMissingValueSubtree(int[] parents, int[] nums) {
        int n = parents.length;
        @SuppressWarnings("unchecked")
        java.util.ArrayList<Integer>[] children = new java.util.ArrayList[n];
        for (int i = 0; i < n; i++) children[i] = new java.util.ArrayList<>();
        for (int i = 1; i < n; i++) {
            children[parents[i]].add(i);
        }

        int nodeWithOne = -1;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                nodeWithOne = i;
                break;
            }
        }

        int[] ans = new int[n];
        if (nodeWithOne == -1) {
            java.util.Arrays.fill(ans, 1);
            return ans;
        }

        int maxVal = 100001; // given constraint
        boolean[] seenVal = new boolean[maxVal + 2]; // index up to 100001 inclusive
        boolean[] visitedNode = new boolean[n];
        int mex = 1;

        int cur = nodeWithOne;
        while (cur != -1) {
            java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();
            stack.push(cur);
            while (!stack.isEmpty()) {
                int u = stack.pop();
                if (visitedNode[u]) continue;
                visitedNode[u] = true;
                int val = nums[u];
                if (val < seenVal.length) seenVal[val] = true;
                for (int v : children[u]) {
                    if (!visitedNode[v]) stack.push(v);
                }
            }
            while (mex < seenVal.length && seenVal[mex]) mex++;
            ans[cur] = mex;
            cur = parents[cur];
        }

        for (int i = 0; i < n; i++) {
            if (ans[i] == 0) ans[i] = 1;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def smallestMissingValueSubtree(self, parents, nums):
        """
        :type parents: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(parents)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)

        ans = [1] * n
        try:
            node_one = nums.index(1)
        except ValueError:
            return ans  # 1 not present anywhere

        MAXV = 200005  # enough for all possible missing values
        present = [False] * (MAXV + 1)
        visited = [False] * n
        cur_missing = 1

        def add_subtree(root):
            stack = [root]
            while stack:
                v = stack.pop()
                if visited[v]:
                    continue
                visited[v] = True
                val = nums[v]
                if val <= MAXV:
                    present[val] = True
                for c in children[v]:
                    stack.append(c)

        node = node_one
        while node != -1:
            add_subtree(node)
            while cur_missing <= MAXV and present[cur_missing]:
                cur_missing += 1
            ans[node] = cur_missing
            node = parents[node]

        return ans
```

## Python3

```python
class Solution:
    def smallestMissingValueSubtree(self, parents, nums):
        n = len(parents)
        # Build children adjacency list
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = parents[i]
            children[p].append(i)

        # If 1 is not present, answer is all 1s
        try:
            node_one = nums.index(1)
        except ValueError:
            return [1] * n

        max_val = max(nums) + 2  # enough space for mex beyond existing values
        seen = [False] * (max_val + 5)
        visited_node = [False] * n

        cur_mex = 1
        ans = [1] * n

        def add_subtree(root):
            nonlocal cur_mex
            stack = [root]
            while stack:
                v = stack.pop()
                if visited_node[v]:
                    continue
                visited_node[v] = True
                val = nums[v]
                if val < len(seen):
                    seen[val] = True
                # advance mex
                while cur_mex < len(seen) and seen[cur_mex]:
                    cur_mex += 1
                for ch in children[v]:
                    stack.append(ch)

        node = node_one
        while node != -1:
            add_subtree(node)
            ans[node] = cur_mex
            node = parents[node]

        return ans
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* smallestMissingValueSubtree(int* parents, int parentsSize, int* nums, int numsSize, int* returnSize) {
    int n = parentsSize;
    *returnSize = n;
    int* ans = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) ans[i] = 1;   // default answer

    // find node that contains value 1
    int start = -1;
    for (int i = 0; i < n; ++i) {
        if (nums[i] == 1) { start = i; break; }
    }
    if (start == -1) return ans;   // 1 missing everywhere

    /* build children adjacency list */
    int* childCnt = (int*)calloc(n, sizeof(int));
    for (int i = 1; i < n; ++i) {
        childCnt[parents[i]]++;
    }
    int** children = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; ++i) {
        if (childCnt[i] > 0)
            children[i] = (int*)malloc(childCnt[i] * sizeof(int));
        else
            children[i] = NULL;
    }
    int* pos = (int*)calloc(n, sizeof(int));
    for (int i = 1; i < n; ++i) {
        int p = parents[i];
        children[p][pos[p]++] = i;
    }

    const int MAXV = 100000;
    char* present = (char*)calloc(MAXV + 2, sizeof(char));   // presence of values
    char* nodeAdded = (char*)calloc(n, sizeof(char));       // whether node's value already processed

    int curMissing = 1;
    int cur = start;

    int* stack = (int*)malloc(n * sizeof(int));

    while (cur != -1) {
        int top = 0;
        stack[top++] = cur;
        while (top) {
            int u = stack[--top];
            if (nodeAdded[u]) continue;
            nodeAdded[u] = 1;
            present[nums[u]] = 1;
            for (int i = 0; i < childCnt[u]; ++i) {
                int v = children[u][i];
                stack[top++] = v;
            }
        }
        while (present[curMissing]) ++curMissing;
        ans[cur] = curMissing;
        cur = parents[cur];
    }

    free(stack);
    for (int i = 0; i < n; ++i) if (children[i]) free(children[i]);
    free(children);
    free(childCnt);
    free(pos);
    free(present);
    free(nodeAdded);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] SmallestMissingValueSubtree(int[] parents, int[] nums) {
        int n = parents.Length;
        var children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        for (int i = 1; i < n; i++) {
            children[parents[i]].Add(i);
        }

        int idxOne = -1;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) { idxOne = i; break; }
        }

        var ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = 1;
        if (idxOne == -1) return ans;

        const int MAXV = 100000 + 5;
        bool[] present = new bool[MAXV];
        bool[] visitedNode = new bool[n];

        int mex = 1;
        int cur = idxOne;
        while (cur != -1) {
            // add all nodes in subtree of cur that are not yet visited
            var stack = new Stack<int>();
            stack.Push(cur);
            while (stack.Count > 0) {
                int node = stack.Pop();
                if (visitedNode[node]) continue;
                visitedNode[node] = true;
                present[nums[node]] = true;
                foreach (int child in children[node]) {
                    if (!visitedNode[child]) stack.Push(child);
                }
            }

            while (mex < MAXV && present[mex]) mex++;
            ans[cur] = mex;

            cur = parents[cur];
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} parents
 * @param {number[]} nums
 * @return {number[]}
 */
var smallestMissingValueSubtree = function(parents, nums) {
    const n = parents.length;
    const children = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; ++i) {
        children[parents[i]].push(i);
    }

    let idxOne = -1;
    for (let i = 0; i < n; ++i) {
        if (nums[i] === 1) { idxOne = i; break; }
    }

    const ans = new Array(n).fill(1);
    if (idxOne === -1) return ans;

    const MAXV = 100000 + 2;
    const present = new Uint8Array(MAXV);
    let curMissing = 1;

    function addSubtree(root) {
        const stack = [root];
        while (stack.length) {
            const v = stack.pop();
            const val = nums[v];
            if (present[val] === 0) present[val] = 1;
            for (const ch of children[v]) stack.push(ch);
        }
    }

    // Process the subtree containing value 1
    addSubtree(idxOne);
    while (curMissing < MAXV && present[curMissing]) ++curMissing;
    ans[idxOne] = curMissing;

    let node = idxOne;
    while (parents[node] !== -1) {
        const p = parents[node];
        // Add all sibling subtrees of the current node
        for (const sib of children[p]) {
            if (sib === node) continue;
            addSubtree(sib);
        }
        // Add the parent itself
        const valP = nums[p];
        if (present[valP] === 0) present[valP] = 1;

        while (curMissing < MAXV && present[curMissing]) ++curMissing;
        ans[p] = curMissing;
        node = p;
    }

    return ans;
};
```

## Typescript

```typescript
function smallestMissingValueSubtree(parents: number[], nums: number[]): number[] {
    const n = parents.length;
    const children: number[][] = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; i++) {
        children[parents[i]].push(i);
    }

    const idxOne = nums.indexOf(1);
    if (idxOne === -1) {
        return new Array(n).fill(1);
    }

    const ans: number[] = new Array(n).fill(1);
    const MAXV = 200005;
    const present = new Uint8Array(MAXV);
    const addedNode = new Uint8Array(n);

    let mex = 1;
    let cur = idxOne;

    while (cur !== -1) {
        const stack: number[] = [cur];
        while (stack.length) {
            const u = stack.pop()!;
            if (addedNode[u]) continue;
            addedNode[u] = 1;
            present[nums[u]] = 1;
            for (const v of children[u]) {
                if (!addedNode[v]) stack.push(v);
            }
        }
        while (present[mex]) mex++;
        ans[cur] = mex;
        cur = parents[cur];
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $parents
     * @param Integer[] $nums
     * @return Integer[]
     */
    function smallestMissingValueSubtree($parents, $nums) {
        $n = count($parents);
        // build children list
        $children = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) {
            $p = $parents[$i];
            $children[$p][] = $i;
        }

        // find node with value 1
        $pos = -1;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] == 1) {
                $pos = $i;
                break;
            }
        }

        // if 1 not present, answer is all 1
        if ($pos == -1) {
            return array_fill(0, $n, 1);
        }

        $ans = array_fill(0, $n, 1);
        $maxVal = 100001; // given constraint
        $present = array_fill(0, $maxVal + 2, false); // index up to maxVal+1
        $visitedNode = array_fill(0, $n, false);

        $cur = 1;
        $node = $pos;
        while ($node != -1) {
            // add all unvisited nodes in the subtree of current node
            $stack = [$node];
            while (!empty($stack)) {
                $v = array_pop($stack);
                if ($visitedNode[$v]) continue;
                $visitedNode[$v] = true;
                $val = $nums[$v];
                $present[$val] = true;
                foreach ($children[$v] as $c) {
                    $stack[] = $c;
                }
            }

            while ($cur <= $maxVal + 1 && $present[$cur]) {
                $cur++;
            }
            $ans[$node] = $cur;

            $node = $parents[$node];
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func smallestMissingValueSubtree(_ parents: [Int], _ nums: [Int]) -> [Int] {
        let n = parents.count
        var children = [[Int]](repeating: [], count: n)
        for i in 1..<n {
            let p = parents[i]
            children[p].append(i)
        }
        
        // Find node with value 1
        var nodeOne = -1
        for i in 0..<n {
            if nums[i] == 1 {
                nodeOne = i
                break
            }
        }
        if nodeOne == -1 {
            return [Int](repeating: 1, count: n)
        }
        
        let maxVal = 100_001
        var present = [Bool](repeating: false, count: maxVal + 2)
        var ans = [Int](repeating: 0, count: n)
        
        func addSubtree(_ start: Int) {
            var stack = [Int]()
            stack.append(start)
            while let v = stack.popLast() {
                if present[nums[v]] { continue }
                present[nums[v]] = true
                for child in children[v] {
                    stack.append(child)
                }
            }
        }
        
        var curMissing = 1
        var node = nodeOne
        while true {
            addSubtree(node)
            while present[curMissing] {
                curMissing += 1
            }
            ans[node] = curMissing
            if parents[node] == -1 { break }
            node = parents[node]
        }
        
        for i in 0..<n {
            if ans[i] == 0 {
                ans[i] = 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestMissingValueSubtree(parents: IntArray, nums: IntArray): IntArray {
        val n = parents.size
        val children = Array(n) { mutableListOf<Int>() }
        for (i in 1 until n) {
            children[parents[i]].add(i)
        }

        var nodeOne = -1
        for (i in 0 until n) {
            if (nums[i] == 1) {
                nodeOne = i
                break
            }
        }

        val ans = IntArray(n) { 1 } // default answer is 1

        if (nodeOne == -1) return ans

        val limit = 200005   // enough for all possible missing values
        val present = BooleanArray(limit)
        val visitedNode = BooleanArray(n)

        var curMissing = 1
        var cur = nodeOne
        while (cur != -1) {
            // add all nodes in the subtree of cur that haven't been processed yet
            val stack = java.util.ArrayDeque<Int>()
            stack.add(cur)
            while (!stack.isEmpty()) {
                val v = stack.poll()
                if (visitedNode[v]) continue
                visitedNode[v] = true
                val value = nums[v]
                if (value < limit) present[value] = true
                for (child in children[v]) {
                    if (!visitedNode[child]) stack.add(child)
                }
            }

            while (curMissing < limit && present[curMissing]) curMissing++
            ans[cur] = curMissing

            cur = parents[cur]
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> smallestMissingValueSubtree(List<int> parents, List<int> nums) {
    int n = parents.length;
    // Build children adjacency list
    List<List<int>> children = List.generate(n, (_) => []);
    for (int i = 1; i < n; i++) {
      children[parents[i]].add(i);
    }

    // Find node with genetic value 1
    int start = -1;
    for (int i = 0; i < n; i++) {
      if (nums[i] == 1) {
        start = i;
        break;
      }
    }

    List<int> ans = List.filled(n, 1);
    if (start == -1) return ans; // value 1 missing everywhere

    const int maxVal = 200005; // sufficient upper bound
    List<bool> present = List.filled(maxVal, false);
    List<bool> visitedNode = List.filled(n, false);

    void dfs(int root) {
      var stack = <int>[root];
      while (stack.isNotEmpty) {
        int node = stack.removeLast();
        if (visitedNode[node]) continue;
        visitedNode[node] = true;
        int val = nums[node];
        if (val < maxVal) present[val] = true;
        for (int child in children[node]) {
          if (!visitedNode[child]) stack.add(child);
        }
      }
    }

    int cur = start;
    int mex = 1;
    while (cur != -1) {
      dfs(cur);
      while (mex < maxVal && present[mex]) mex++;
      ans[cur] = mex;
      cur = parents[cur];
    }

    return ans;
  }
}
```

## Golang

```go
func smallestMissingValueSubtree(parents []int, nums []int) []int {
    n := len(parents)
    children := make([][]int, n)
    for i := 1; i < n; i++ {
        p := parents[i]
        children[p] = append(children[p], i)
    }

    idxOne := -1
    for i, v := range nums {
        if v == 1 {
            idxOne = i
            break
        }
    }

    ans := make([]int, n)
    if idxOne == -1 {
        for i := range ans {
            ans[i] = 1
        }
        return ans
    }

    const maxVal = 100000
    visited := make([]bool, maxVal+2) // up to 100001 inclusive
    curMissing := 1
    node := idxOne

    for node != -1 {
        stack := []int{node}
        for len(stack) > 0 {
            v := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            if visited[nums[v]] {
                continue
            }
            visited[nums[v]] = true
            for _, c := range children[v] {
                stack = append(stack, c)
            }
        }

        for curMissing <= maxVal+1 && visited[curMissing] {
            curMissing++
        }
        ans[node] = curMissing
        node = parents[node]
    }

    for i := 0; i < n; i++ {
        if ans[i] == 0 {
            ans[i] = 1
        }
    }
    return ans
}
```

## Ruby

```ruby
def smallest_missing_value_subtree(parents, nums)
  n = parents.size
  children = Array.new(n) { [] }
  (1...n).each do |i|
    p = parents[i]
    children[p] << i
  end

  ans = Array.new(n, 1)

  idx_one = nums.index(1)
  return ans if idx_one.nil?

  max_val = 100_001
  visited = Array.new(max_val + 2, false)
  node_added = Array.new(n, false)

  cur_missing = 1

  add_subtree = lambda do |root|
    stack = [root]
    while (u = stack.pop)
      next if node_added[u]
      node_added[u] = true
      visited[nums[u]] = true
      children[u].each { |v| stack << v }
    end
  end

  cur = idx_one
  while cur != -1
    add_subtree.call(cur)
    cur_missing += 1 while visited[cur_missing]
    ans[cur] = cur_missing
    cur = parents[cur]
  end

  ans
end
```

## Scala

```scala
object Solution {
    def smallestMissingValueSubtree(parents: Array[Int], nums: Array[Int]): Array[Int] = {
        val n = parents.length
        // Build children adjacency list
        val children = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
        var i = 1
        while (i < n) {
            val p = parents(i)
            children(p).append(i)
            i += 1
        }

        // Find node with value 1
        var idx = -1
        i = 0
        while (i < n) {
            if (nums(i) == 1) { idx = i; }
            i += 1
        }
        if (idx == -1) return Array.fill(n)(1)

        // Prepare structures
        val maxVal = 100005   // enough for values up to 10^5 + possible missing
        val present = new Array[Boolean](maxVal)
        val seenNode = new Array[Boolean](n)
        val ans = new Array[Int](n)

        var curMissing = 1
        var v = idx
        while (v != -1) {
            // Add all nodes in subtree of v that are not yet added
            val stack = new scala.collection.mutable.Stack[Int]()
            if (!seenNode(v)) stack.push(v)
            while (stack.nonEmpty) {
                val u = stack.pop()
                if (!seenNode(u)) {
                    seenNode(u) = true
                    present(nums(u)) = true
                    var j = 0
                    val childList = children(u)
                    while (j < childList.length) {
                        val c = childList(j)
                        if (!seenNode(c)) stack.push(c)
                        j += 1
                    }
                }
            }
            // Update smallest missing value
            while (curMissing < maxVal && present(curMissing)) curMissing += 1
            ans(v) = curMissing
            v = parents(v)
        }

        // Nodes whose subtree does not contain 1 have answer 1
        i = 0
        while (i < n) {
            if (ans(i) == 0) ans(i) = 1
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_missing_value_subtree(parents: Vec<i32>, nums: Vec<i32>) -> Vec<i32> {
        let n = parents.len();
        // Build children adjacency list
        let mut children: Vec<Vec<usize>> = vec![Vec::new(); n];
        for i in 1..n {
            let p = parents[i] as usize;
            children[p].push(i);
        }

        // Find node with genetic value 1
        let mut start_opt = None;
        for (i, &v) in nums.iter().enumerate() {
            if v == 1 {
                start_opt = Some(i);
                break;
            }
        }
        if start_opt.is_none() {
            return vec![1; n];
        }
        let mut cur = start_opt.unwrap();

        // Data structures for presence and visited nodes
        const MAX_VAL: usize = 200_005; // enough for mex up to 100001
        let mut present = vec![false; MAX_VAL];
        let mut visited = vec![false; n];
        let mut ans = vec![0i32; n];

        let mut mex: usize = 1;

        loop {
            // Iterative DFS to add all values in the subtree of cur that are not yet added
            let mut stack = Vec::new();
            stack.push(cur);
            while let Some(u) = stack.pop() {
                if visited[u] {
                    continue;
                }
                visited[u] = true;
                let val = nums[u] as usize;
                if val < MAX_VAL {
                    present[val] = true;
                }
                for &v in &children[u] {
                    if !visited[v] {
                        stack.push(v);
                    }
                }
            }

            // Update mex
            while mex < MAX_VAL && present[mex] {
                mex += 1;
            }
            ans[cur] = mex as i32;

            // Move to parent
            if parents[cur] == -1 {
                break;
            }
            cur = parents[cur] as usize;
        }

        // Nodes not on the path from value-1 node have answer 1
        for i in 0..n {
            if ans[i] == 0 {
                ans[i] = 1;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (smallest-missing-value-subtree parents nums)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length parents))
         (parent-vec (list->vector parents))
         (nums-vec (list->vector nums))
         ;; build children adjacency
         (child-vec (make-vector n '()))
         ( _ (for ([i (in-range 1 n)])
                (let* ((p (vector-ref parent-vec i))
                       (old (vector-ref child-vec p)))
                  (vector-set! child-vec p (cons i old)))))
         ;; find node containing value 1
         (start (let loop ((i 0) (found -1))
                  (if (>= i n)
                      found
                      (if (= (vector-ref nums-vec i) 1)
                          i
                          (loop (+ i 1) found))))))
    (if (= start -1)
        (make-list n 1)
        (let* ((present (make-vector (+ n 5) #f))
               (node-seen (make-vector n #f))
               (ans-vec (make-vector n 1))
               ;; depth‑first marking of subtree values
               (dfs (lambda (root)
                      (let recur ((stack (list root)))
                        (when (pair? stack)
                          (define node (car stack))
                          (define rest (cdr stack))
                          (if (vector-ref node-seen node)
                              (recur rest)
                              (begin
                                (vector-set! node-seen node #t)
                                (let ((val (vector-ref nums-vec node)))
                                  (when (< val (vector-length present))
                                    (vector-set! present val #t)))
                                (define children (vector-ref child-vec node))
                                (recur (foldl (lambda (c acc) (cons c acc)) rest children))))))))
               (mex 1)
               (cur start))
          ;; process path from the node with value 1 up to root
          (let loop ()
            (when (>= cur 0)
              (dfs cur)
              ;; update mex
              (let inner ((m mex))
                (if (vector-ref present m)
                    (begin (set! mex (+ m 1)) (inner mex))
                    (void)))
              (vector-set! ans-vec cur mex)
              (set! cur (vector-ref parent-vec cur))
              (loop)))
          (vector->list ans-vec))))
```

## Erlang

```erlang
-export([smallest_missing_value_subtree/2]).

-spec smallest_missing_value_subtree(Parents :: [integer()], Nums :: [integer()]) -> [integer()].
smallest_missing_value_subtree(Parents, Nums) ->
    N = length(Parents),
    ChildrenMap = build_children(Parents, 0, #{ }),
    ParentsTuple = list_to_tuple(Parents),
    NumsTuple = list_to_tuple(Nums),

    case find_one(Nums, 0) of
        undefined ->
            lists:duplicate(N, 1);
        StartNode ->
            Seen0 = #{},
            Seen1 = add_subtree([StartNode], ChildrenMap, NumsTuple, Seen0),
            Mex0 = find_mex(Seen1, 1),
            AnsMap0 = maps:put(StartNode, Mex0, #{}),
            FinalAnsMap = walk_up(StartNode, ParentsTuple, ChildrenMap, NumsTuple, Seen1, Mex0, AnsMap0),
            [maps:get(I, FinalAnsMap, 1) || I <- lists:seq(0, N-1)]
    end.

%% Build children adjacency map
build_children([], _Idx, Acc) -> Acc;
build_children([P|Rest], Idx, Acc) ->
    case P of
        -1 ->
            build_children(Rest, Idx+1, Acc);
        Parent ->
            Prev = maps:get(Parent, Acc, []),
            NewAcc = maps:put(Parent, [Idx | Prev], Acc),
            build_children(Rest, Idx+1, NewAcc)
    end.

%% Find index of value 1
find_one([], _Idx) -> undefined;
find_one([V|Rest], Idx) ->
    if V =:= 1 -> Idx;
       true -> find_one(Rest, Idx+1)
    end.

%% Add all nodes in a subtree to Seen set (stack based)
add_subtree([], _ChildrenMap, _NumsTuple, Seen) -> Seen;
add_subtree([Node|Stack], ChildrenMap, NumsTuple, Seen0) ->
    Val = element(Node+1, NumsTuple),
    Seen1 = maps:put(Val, true, Seen0),
    ChildList = maps:get(Node, ChildrenMap, []),
    NewStack = ChildList ++ Stack,
    add_subtree(NewStack, ChildrenMap, NumsTuple, Seen1).

%% Find smallest missing positive integer starting from Cur
find_mex(Seen, Cur) ->
    case maps:is_key(Cur, Seen) of
        true -> find_mex(Seen, Cur+1);
        false -> Cur
    end.

%% Walk up ancestors, updating Seen and answers
walk_up(Node, ParentsTuple, ChildrenMap, NumsTuple, Seen, CurMex, AnsMap) ->
    Parent = element(Node+1, ParentsTuple),
    case Parent of
        -1 -> AnsMap;
        _ ->
            ValParent = element(Parent+1, NumsTuple),
            Seen1 = maps:put(ValParent, true, Seen),

            ChildList = maps:get(Parent, ChildrenMap, []),
            Siblings = [C || C <- ChildList, C =/= Node],

            Seen2 = lists:foldl(
                        fun(C, AccSeen) ->
                            add_subtree([C], ChildrenMap, NumsTuple, AccSeen)
                        end,
                        Seen1,
                        Siblings),

            NewMex = find_mex(Seen2, CurMex),
            AnsMap1 = maps:put(Parent, NewMex, AnsMap),
            walk_up(Parent, ParentsTuple, ChildrenMap, NumsTuple, Seen2, NewMex, AnsMap1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_missing_value_subtree(parents :: [integer], nums :: [integer]) :: [integer]
  def smallest_missing_value_subtree(parents, nums) do
    n = length(parents)

    pos_one = Enum.find_index(nums, fn v -> v == 1 end)

    if is_nil(pos_one) do
      List.duplicate(1, n)
    else
      parents_t = List.to_tuple(parents)
      nums_t = List.to_tuple(nums)

      # build children map
      children =
        Enum.reduce(1..(n - 1), %{}, fn i, acc ->
          p = elem(parents_t, i)
          Map.update(acc, p, [i], fn lst -> [i | lst] end)
        end)

      seen = MapSet.new()
      visited = MapSet.new()
      ans = List.duplicate(0, n)

      cur_missing = 1
      node = pos_one

      # process ancestors of the node containing value 1
      while true do
        {seen, visited} = dfs([node], children, nums_t, seen, visited)
        cur_missing = next_missing(cur_missing, seen)
        ans = List.replace_at(ans, node, cur_missing)

        if node == 0 do
          break()
        else
          node = elem(parents_t, node)
        end
      end

      # nodes not in the processed ancestor chain have answer 1
      Enum.map(Enum.with_index(ans), fn {v, _i} -> if v == 0, do: 1, else: v end)
    end
  end

  defp dfs([], _children, _nums_t, seen, visited), do: {seen, visited}

  defp dfs([x | rest], children, nums_t, seen, visited) do
    if MapSet.member?(visited, x) do
      dfs(rest, children, nums_t, seen, visited)
    else
      visited = MapSet.put(visited, x)
      val = elem(nums_t, x)
      seen = MapSet.put(seen, val)

      child_list = Map.get(children, x, [])
      stack = child_list ++ rest
      dfs(stack, children, nums_t, seen, visited)
    end
  end

  defp next_missing(cur, seen) do
    if MapSet.member?(seen, cur) do
      next_missing(cur + 1, seen)
    else
      cur
    end
  end
end
```
