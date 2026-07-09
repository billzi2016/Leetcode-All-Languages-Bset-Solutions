# 3488. Closest Equal Element Queries

## Cpp

```cpp
class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();
        unordered_map<int, vector<int>> pos;
        pos.reserve(n * 2);
        for (int i = 0; i < n; ++i) {
            pos[nums[i]].push_back(i);
        }
        vector<int> ans;
        ans.reserve(queries.size());
        for (int idx : queries) {
            const vector<int>& v = pos[nums[idx]];
            if (v.size() <= 1) {
                ans.push_back(-1);
                continue;
            }
            // forward distance
            auto it = lower_bound(v.begin(), v.end(), idx);
            int forwardDist;
            if (it != v.end() && *it == idx) ++it; // skip self
            if (it != v.end()) {
                forwardDist = (*it - idx + n) % n;
            } else {
                forwardDist = (v.front() - idx + n) % n;
            }
            // backward distance
            auto it2 = lower_bound(v.begin(), v.end(), idx);
            int backwardDist;
            if (it2 == v.begin()) {
                // wrap to last element
                backwardDist = (idx - v.back() + n) % n;
            } else {
                if (it2 != v.end() && *it2 == idx) --it2; // move to previous distinct
                else --it2;
                backwardDist = (idx - *it2 + n) % n;
            }
            ans.push_back(min(forwardDist, backwardDist));
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> solveQueries(int[] nums, int[] queries) {
        int n = nums.length;
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
        List<Integer> result = new ArrayList<>(queries.length);
        for (int q : queries) {
            int val = nums[q];
            List<Integer> list = map.get(val);
            if (list.size() == 1) {
                result.add(-1);
                continue;
            }
            int idx = Collections.binarySearch(list, q);
            int best = Integer.MAX_VALUE;
            if (idx >= 0) { // exact position found
                // left neighbor
                if (idx > 0) {
                    best = Math.min(best, circularDist(q, list.get(idx - 1), n));
                } else {
                    best = Math.min(best, circularDist(q, list.get(list.size() - 1), n));
                }
                // right neighbor
                if (idx + 1 < list.size()) {
                    best = Math.min(best, circularDist(q, list.get(idx + 1), n));
                } else {
                    best = Math.min(best, circularDist(q, list.get(0), n));
                }
            } else { // not found, get insertion point
                int insertPos = -idx - 1;
                // left neighbor (wrap to last if needed)
                if (insertPos > 0) {
                    best = Math.min(best, circularDist(q, list.get(insertPos - 1), n));
                } else {
                    best = Math.min(best, circularDist(q, list.get(list.size() - 1), n));
                }
                // right neighbor (wrap to first if needed)
                if (insertPos < list.size()) {
                    best = Math.min(best, circularDist(q, list.get(insertPos), n));
                } else {
                    best = Math.min(best, circularDist(q, list.get(0), n));
                }
            }
            result.add(best);
        }
        return result;
    }

    private int circularDist(int a, int b, int n) {
        int diff = Math.abs(a - b);
        return Math.min(diff, n - diff);
    }
}
```

## Python

```python
class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        from bisect import bisect_left
        n = len(nums)
        pos_dict = {}
        for idx, val in enumerate(nums):
            pos_dict.setdefault(val, []).append(idx)

        # ensure each list is sorted (they are built in order)
        ans = []
        for i in queries:
            val = nums[i]
            lst = pos_dict[val]
            if len(lst) == 1:
                ans.append(-1)
                continue
            p = bisect_left(lst, i)
            # right neighbor (including wrap)
            if p < len(lst) - 1:
                right_idx = lst[p + 1]
                d_right = min((right_idx - i) % n, (i - right_idx) % n)
            else:
                right_idx = lst[0]
                d_right = min((right_idx - i) % n, (i - right_idx) % n)
            # left neighbor (including wrap)
            if p > 0:
                left_idx = lst[p - 1]
                d_left = min((left_idx - i) % n, (i - left_idx) % n)
            else:
                left_idx = lst[-1]
                d_left = min((left_idx - i) % n, (i - left_idx) % n)

            ans.append(min(d_left, d_right))
        return ans
```

## Python3

```python
from bisect import bisect_left
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos_map = {}
        for i, v in enumerate(nums):
            pos_map.setdefault(v, []).append(i)

        # Ensure each list is sorted (they are built in order of indices)
        ans = []
        for idx in queries:
            lst = pos_map[nums[idx]]
            if len(lst) == 1:
                ans.append(-1)
                continue
            p = bisect_left(lst, idx)
            best = n  # max possible distance is n-1
            # right neighbor (including possibly same index if duplicate at same position, but we need other index)
            if p < len(lst):
                r = lst[p]
                if r != idx:
                    diff = abs(r - idx)
                    best = min(best, diff, n - diff)
                else:
                    # same index, check next if exists
                    if p + 1 < len(lst):
                        r = lst[p + 1]
                        diff = abs(r - idx)
                        best = min(best, diff, n - diff)
            # left neighbor
            if p > 0:
                l = lst[p - 1]
                if l != idx:
                    diff = abs(l - idx)
                    best = min(best, diff, n - diff)
                else:
                    # same index, check previous if exists
                    if p - 2 >= 0:
                        l = lst[p - 2]
                        diff = abs(l - idx)
                        best = min(best, diff, n - diff)
            ans.append(best if best != n else -1)
        return ans
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* solveQueries(int* nums, int numsSize, int* queries, int queriesSize, int* returnSize){
    // Find maximum value to size auxiliary arrays
    int maxVal = 0;
    for (int i = 0; i < numsSize; ++i)
        if (nums[i] > maxVal) maxVal = nums[i];
    
    // Count frequencies
    int *freq = (int*)calloc(maxVal + 1, sizeof(int));
    for (int i = 0; i < numsSize; ++i)
        freq[nums[i]]++;
    
    // Allocate storage for positions of each value
    int **pos = (int**)malloc((maxVal + 1) * sizeof(int*));
    int *fillIdx = (int*)calloc(maxVal + 1, sizeof(int));
    for (int v = 0; v <= maxVal; ++v){
        if (freq[v] > 0){
            pos[v] = (int*)malloc(freq[v] * sizeof(int));
        }else{
            pos[v] = NULL;
        }
    }
    
    // Fill positions (they become sorted because we traverse nums in order)
    for (int i = 0; i < numsSize; ++i){
        int v = nums[i];
        pos[v][fillIdx[v]++] = i;
    }
    
    // Answer queries
    int *ans = (int*)malloc(queriesSize * sizeof(int));
    for (int qi = 0; qi < queriesSize; ++qi){
        int idx = queries[qi];               // queried index in nums
        int val = nums[idx];
        int cnt = freq[val];
        if (cnt <= 1){
            ans[qi] = -1;
            continue;
        }
        int *arr = pos[val];
        // binary search to locate idx within arr
        int lo = 0, hi = cnt - 1, midPos = -1;
        while (lo <= hi){
            int mid = (lo + hi) >> 1;
            if (arr[mid] == idx){
                midPos = mid;
                break;
            }else if (arr[mid] < idx){
                lo = mid + 1;
            }else{
                hi = mid - 1;
            }
        }
        // midPos must be found
        int predIdx = (midPos - 1 + cnt) % cnt;
        int succIdx = (midPos + 1) % cnt;
        int pred = arr[predIdx];
        int succ = arr[succIdx];
        
        int diffPred = idx > pred ? idx - pred : pred - idx;
        int distPred = diffPred < numsSize - diffPred ? diffPred : numsSize - diffPred;
        int diffSucc = idx > succ ? idx - succ : succ - idx;
        int distSucc = diffSucc < numsSize - diffSucc ? diffSucc : numsSize - diffSucc;
        
        ans[qi] = distPred < distSucc ? distPred : distSucc;
    }
    
    // Clean up auxiliary structures (optional, as program ends after return)
    free(freq);
    free(fillIdx);
    for (int v = 0; v <= maxVal; ++v){
        if (pos[v]) free(pos[v]);
    }
    free(pos);
    
    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> SolveQueries(int[] nums, int[] queries) {
        int n = nums.Length;
        var map = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            if (!map.TryGetValue(nums[i], out var list)) {
                list = new List<int>();
                map[nums[i]] = list;
            }
            list.Add(i);
        }

        var result = new List<int>(queries.Length);
        foreach (int q in queries) {
            int val = nums[q];
            var lst = map[val];
            if (lst.Count == 1) {
                result.Add(-1);
                continue;
            }
            int pos = lst.BinarySearch(q); // guaranteed to find
            int cnt = lst.Count;

            int prevIdx = lst[(pos - 1 + cnt) % cnt];
            int nextIdx = lst[(pos + 1) % cnt];

            int diffPrev = Math.Abs(q - prevIdx);
            int distPrev = Math.Min(diffPrev, n - diffPrev);

            int diffNext = Math.Abs(q - nextIdx);
            int distNext = Math.Min(diffNext, n - diffNext);

            result.Add(Math.Min(distPrev, distNext));
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} queries
 * @return {number[]}
 */
var solveQueries = function(nums, queries) {
    const n = nums.length;
    // map value -> sorted list of indices
    const posMap = new Map();
    for (let i = 0; i < n; ++i) {
        const v = nums[i];
        if (!posMap.has(v)) posMap.set(v, []);
        posMap.get(v).push(i);
    }
    // binary search helpers
    function lowerBound(arr, target) {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] < target) l = m + 1;
            else r = m;
        }
        return l;
    }
    function upperBound(arr, target) {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] <= target) l = m + 1;
            else r = m;
        }
        return l;
    }

    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; ++qi) {
        const idx = queries[qi];
        const val = nums[idx];
        const list = posMap.get(val);
        if (list.length === 1) {
            ans[qi] = -1;
            continue;
        }
        // distance to next occurrence (strictly after idx)
        let ub = upperBound(list, idx);
        let distNext;
        if (ub < list.length) {
            distNext = list[ub] - idx;
        } else {
            distNext = n - idx + list[0];
        }
        // distance to previous occurrence (strictly before idx)
        let lb = lowerBound(list, idx);
        let distPrev;
        if (lb > 0) {
            const prevIdx = list[lb - 1];
            distPrev = idx - prevIdx;
        } else {
            const prevIdx = list[list.length - 1];
            distPrev = idx + n - prevIdx;
        }
        ans[qi] = Math.min(distNext, distPrev);
    }
    return ans;
};
```

## Typescript

```typescript
function solveQueries(nums: number[], queries: number[]): number[] {
    const n = nums.length;
    const idxMap = new Map<number, number[]>();
    for (let i = 0; i < n; i++) {
        const v = nums[i];
        if (!idxMap.has(v)) idxMap.set(v, []);
        idxMap.get(v)!.push(i);
    }

    const result: number[] = [];

    for (const q of queries) {
        const val = nums[q];
        const arr = idxMap.get(val)!;
        if (arr.length === 1) {
            result.push(-1);
            continue;
        }

        // lower bound to find position of q
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] < q) l = m + 1;
            else r = m;
        }
        const pos = l; // arr[pos] == q

        // forward neighbor
        const nextIdx = (pos + 1 < arr.length) ? arr[pos + 1] : arr[0];
        // backward neighbor
        const prevIdx = (pos - 1 >= 0) ? arr[pos - 1] : arr[arr.length - 1];

        const forwardDist = (nextIdx - q + n) % n;
        const backwardDist = (q - prevIdx + n) % n;

        result.push(Math.min(forwardDist, backwardDist));
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $queries
     * @return Integer[]
     */
    function solveQueries($nums, $queries) {
        $n = count($nums);
        $map = []; // value => list of indices

        for ($i = 0; $i < $n; $i++) {
            $v = $nums[$i];
            if (!isset($map[$v])) {
                $map[$v] = [];
            }
            $map[$v][] = $i;
        }

        // position of each index inside its value's list
        $posInList = array_fill(0, $n, 0);
        foreach ($map as $val => &$list) {
            foreach ($list as $idxPos => $idx) {
                $posInList[$idx] = $idxPos;
            }
        }
        unset($list); // break reference

        $answer = [];
        foreach ($queries as $q) {
            $value = $nums[$q];
            $list = $map[$value];
            $cnt = count($list);
            if ($cnt <= 1) {
                $answer[] = -1;
                continue;
            }
            $pos = $posInList[$q];
            $prevIdx = $list[($pos - 1 + $cnt) % $cnt];
            $nextIdx = $list[($pos + 1) % $cnt];

            $distPrev = ($q - $prevIdx + $n) % $n;
            $distNext = ($nextIdx - $q + $n) % $n;

            $answer[] = min($distPrev, $distNext);
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func solveQueries(_ nums: [Int], _ queries: [Int]) -> [Int] {
        let n = nums.count
        var positionsByValue = [Int: [Int]]()
        for (i, v) in nums.enumerated() {
            positionsByValue[v, default: []].append(i)
        }
        
        func lowerBound(_ arr: [Int], _ target: Int) -> Int {
            var l = 0
            var r = arr.count
            while l < r {
                let m = (l + r) >> 1
                if arr[m] < target {
                    l = m + 1
                } else {
                    r = m
                }
            }
            return l
        }
        
        var answer = [Int]()
        answer.reserveCapacity(queries.count)
        
        for q in queries {
            let val = nums[q]
            guard let list = positionsByValue[val] else {
                answer.append(-1)
                continue
            }
            if list.count == 1 {
                answer.append(-1)
                continue
            }
            let pos = lowerBound(list, q)
            var best = n
            
            // next occurrence (wrap around)
            let candNext = list[pos % list.count]
            let distNext = min((candNext - q + n) % n, (q - candNext + n) % n)
            if distNext < best { best = distNext }
            
            // previous occurrence
            let prevIdx = (pos - 1 + list.count) % list.count
            let candPrev = list[prevIdx]
            let distPrev = min((candPrev - q + n) % n, (q - candPrev + n) % n)
            if distPrev < best { best = distPrev }
            
            answer.append(best)
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
import kotlin.math.abs
import kotlin.math.min

class Solution {
    fun solveQueries(nums: IntArray, queries: IntArray): List<Int> {
        val n = nums.size
        val map = HashMap<Int, MutableList<Int>>()
        for (i in 0 until n) {
            map.computeIfAbsent(nums[i]) { mutableListOf() }.add(i)
        }

        fun circularDist(a: Int, b: Int): Int {
            val diff = abs(a - b)
            return min(diff, n - diff)
        }

        val answer = ArrayList<Int>(queries.size)
        for (q in queries) {
            val value = nums[q]
            val list = map[value]!!
            if (list.size == 1) {
                answer.add(-1)
                continue
            }
            var pos = list.binarySearch(q)
            // binarySearch should find exact position
            if (pos < 0) pos = -(pos + 1) // fallback, though shouldn't happen

            var best = Int.MAX_VALUE

            // previous element (with wrap)
            val prevIdx = if (pos > 0) list[pos - 1] else list[list.size - 1]
            best = min(best, circularDist(q, prevIdx))

            // next element (with wrap)
            val nextIdx = if (pos < list.size - 1) list[pos + 1] else list[0]
            best = min(best, circularDist(q, nextIdx))

            answer.add(best)
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> solveQueries(List<int> nums, List<int> queries) {
    int n = nums.length;
    Map<int, List<int>> indexMap = {};
    for (int i = 0; i < n; i++) {
      indexMap.putIfAbsent(nums[i], () => []).add(i);
    }

    List<int> result = [];
    for (int q in queries) {
      int val = nums[q];
      List<int> positions = indexMap[val]!;
      if (positions.length == 1) {
        result.add(-1);
        continue;
      }

      // binary search to find the position of q in the sorted list
      int lo = 0, hi = positions.length - 1;
      while (lo < hi) {
        int mid = (lo + hi) >> 1;
        if (positions[mid] < q) {
          lo = mid + 1;
        } else {
          hi = mid;
        }
      }
      int idxPos = lo; // positions[idxPos] == q

      // successor (next occurrence)
      int succIdx = (idxPos + 1) % positions.length;
      int succPos = positions[succIdx];
      int forwardDist = (succPos - q + n) % n;

      // predecessor (previous occurrence)
      int predIdx = (idxPos - 1 + positions.length) % positions.length;
      int predPos = positions[predIdx];
      int backwardDist = (q - predPos + n) % n;

      result.add(forwardDist < backwardDist ? forwardDist : backwardDist);
    }

    return result;
  }
}
```

## Golang

```go
func solveQueries(nums []int, queries []int) []int {
    n := len(nums)
    mp := make(map[int][]int)
    for i, v := range nums {
        mp[v] = append(mp[v], i)
    }

    abs := func(a int) int {
        if a < 0 {
            return -a
        }
        return a
    }

    ans := make([]int, len(queries))
    for idx, q := range queries {
        v := nums[q]
        lst := mp[v]
        if len(lst) == 1 {
            ans[idx] = -1
            continue
        }
        // position of q in the sorted list lst (lst is already sorted)
        pos := sort.SearchInts(lst, q)

        pred := lst[(pos-1+len(lst))%len(lst)]
        succ := lst[(pos+1)%len(lst)]

        d1 := abs(q - pred)
        if d1 > n-d1 {
            d1 = n - d1
        }
        d2 := abs(q - succ)
        if d2 > n-d2 {
            d2 = n - d2
        }

        if d1 < d2 {
            ans[idx] = d1
        } else {
            ans[idx] = d2
        }
    }
    return ans
}
```

## Ruby

```ruby
def solve_queries(nums, queries)
  n = nums.length
  index_map = Hash.new { |h, k| h[k] = [] }
  nums.each_with_index do |val, idx|
    index_map[val] << idx
  end

  answers = queries.map do |q|
    val = nums[q]
    positions = index_map[val]
    if positions.size == 1
      -1
    else
      # binary search to find the position of q in positions (sorted)
      left = 0
      right = positions.size - 1
      pos = nil
      while left <= right
        mid = (left + right) / 2
        if positions[mid] < q
          left = mid + 1
        elsif positions[mid] > q
          right = mid - 1
        else
          pos = mid
          break
        end
      end

      len = positions.size
      pred = positions[(pos - 1) % len]
      succ = positions[(pos + 1) % len]

      d1 = (q - pred).abs
      d1 = [d1, n - d1].min
      d2 = (succ - q).abs
      d2 = [d2, n - d2].min

      [d1, d2].min
    end
  end

  answers
end
```

## Scala

```scala
object Solution {
    def solveQueries(nums: Array[Int], queries: Array[Int]): List[Int] = {
        val n = nums.length
        val temp = scala.collection.mutable.Map[Int, scala.collection.mutable.ArrayBuffer[Int]]()
        for (i <- 0 until n) {
            val v = nums(i)
            val buf = temp.getOrElseUpdate(v, scala.collection.mutable.ArrayBuffer[Int]())
            buf.append(i)
        }
        val posMap: Map[Int, Array[Int]] = temp.map { case (k, v) => k -> v.toArray }.toMap

        val result = new scala.collection.mutable.ListBuffer[Int]()
        for (q <- queries) {
            val v = nums(q)
            val arr = posMap(v)
            if (arr.length == 1) {
                result.append(-1)
            } else {
                val idxInArr = java.util.Arrays.binarySearch(arr, q) // guaranteed >=0
                val prevIdx = if (idxInArr > 0) arr(idxInArr - 1) else arr(arr.length - 1)
                val nextIdx = if (idxInArr < arr.length - 1) arr(idxInArr + 1) else arr(0)

                val distPrev = (q - prevIdx + n) % n
                val distNext = (nextIdx - q + n) % n
                result.append(math.min(distPrev, distNext))
            }
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn solve_queries(nums: Vec<i32>, queries: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        use std::collections::HashMap;
        let mut map: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in nums.iter().enumerate() {
            map.entry(v).or_insert_with(Vec::new).push(i);
        }
        let mut ans = Vec::with_capacity(queries.len());
        for &q in queries.iter() {
            let idx = q as usize;
            let val = nums[idx];
            let positions = map.get(&val).unwrap();
            if positions.len() == 1 {
                ans.push(-1);
                continue;
            }
            let pos_idx = match positions.binary_search(&idx) {
                Ok(p) => p,
                Err(_) => unreachable!(),
            };
            let len = positions.len();
            let pred = positions[(pos_idx + len - 1) % len];
            let succ = positions[(pos_idx + 1) % len];
            let forward = (succ + n - idx) % n;
            let backward = (idx + n - pred) % n;
            let min_dist = if forward < backward { forward } else { backward };
            ans.push(min_dist as i32);
        }
        ans
    }
}
```

## Racket

```racket
(define (binary-find vec target)
  (let loop ((lo 0) (hi (- (vector-length vec) 1)))
    (if (> lo hi)
        -1
        (let ((mid (quotient (+ lo hi) 2))
              (midval (vector-ref vec mid)))
          (cond [(= midval target) mid]
                [(< midval target) (loop (+ mid 1) hi)]
                [else (loop lo (- mid 1))])))))

(define (circular-dist a b n)
  (let ((diff (abs (- a b))))
    (if (< diff (- n diff)) diff (- n diff))))

(define/contract (solve-queries nums queries)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length nums))
         (vec (list->vector nums))
         (h (make-hash)))
    ;; build map from value to list of indices (in reverse order)
    (for ([i (in-range n)])
      (let ((val (vector-ref vec i)))
        (hash-update! h val (lambda (lst) (cons i lst)) '())))
    ;; convert each list to a sorted vector of indices
    (define idx-map (make-hash))
    (hash-for-each h (lambda (k v)
                       (hash-set! idx-map k (list->vector (reverse v)))))
    ;; answer each query
    (for/list ([q queries])
      (let* ((val (vector-ref vec q))
             (idxs (hash-ref idx-map val))
             (len (vector-length idxs)))
        (if (= len 1)
            -1
            (let* ((pos (binary-find idxs q))
                   (prev (if (= pos 0) (vector-ref idxs (- len 1)) (vector-ref idxs (- pos 1))))
                   (next (if (= pos (- len 1)) (vector-ref idxs 0) (vector-ref idxs (+ pos 1))))
                   (d1 (circular-dist q prev n))
                   (d2 (circular-dist q next n)))
              (min d1 d2)))))))
```

## Erlang

```erlang
-module(solution).
-export([solve_queries/2]).

-spec solve_queries(Nums :: [integer()], Queries :: [integer()]) -> [integer()].
solve_queries(Nums, Queries) ->
    N = length(Nums),
    UnsMap = build_map(Nums, 0, #{}),
    SortedMap = maps:map(
        fun(_Key, List) ->
            Sorted = lists:sort(List),
            Tuple = list_to_tuple(Sorted),
            {Tuple, tuple_size(Tuple)}
        end,
        UnsMap
    ),
    process_queries(Queries, Nums, SortedMap, N).

build_map([], _Idx, Map) -> Map;
build_map([H|T], Idx, Map) ->
    Updated = maps:update_with(
        H,
        fun(L) -> [Idx | L] end,
        [Idx],
        Map
    ),
    build_map(T, Idx + 1, Updated).

process_queries([], _Nums, _Map, _N) -> [];
process_queries([QIdx|Rest], Nums, Map, N) ->
    Value = lists:nth(QIdx + 1, Nums),
    {Tuple, Len} = maps:get(Value, Map),
    Answer =
        if
            Len == 1 ->
                -1;
            true ->
                UpperPos = upper_bound(Tuple, Len, QIdx),
                NextIdx =
                    if UpperPos =< Len ->
                        element(UpperPos, Tuple);
                       true ->
                        element(1, Tuple) + N
                    end,
                LowerPos = lower_bound(Tuple, Len, QIdx),
                PrevIdx =
                    if LowerPos > 1 ->
                        element(LowerPos - 1, Tuple);
                       true ->
                        element(Len, Tuple) - N
                    end,
                ForwardDist = NextIdx - QIdx,
                BackwardDist = QIdx - PrevIdx,
                case ForwardDist < BackwardDist of
                    true -> ForwardDist;
                    false -> BackwardDist
                end
        end,
    [Answer | process_queries(Rest, Nums, Map, N)].

upper_bound(Tuple, Len, Target) ->
    upper_bound(Tuple, 1, Len, Target).

upper_bound(_Tuple, Low, High, _Target) when Low > High -> Low;
upper_bound(Tuple, Low, High, Target) ->
    Mid = (Low + High) div 2,
    MidVal = element(Mid, Tuple),
    if
        MidVal =< Target ->
            upper_bound(Tuple, Mid + 1, High, Target);
        true ->
            upper_bound(Tuple, Low, Mid - 1, Target)
    end.

lower_bound(Tuple, Len, Target) ->
    lower_bound(Tuple, 1, Len, Target).

lower_bound(_Tuple, Low, High, _Target) when Low > High -> Low;
lower_bound(Tuple, Low, High, Target) ->
    Mid = (Low + High) div 2,
    MidVal = element(Mid, Tuple),
    if
        MidVal < Target ->
            lower_bound(Tuple, Mid + 1, High, Target);
        true ->
            lower_bound(Tuple, Low, Mid - 1, Target)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec solve_queries(nums :: [integer], queries :: [integer]) :: [integer]
  def solve_queries(nums, queries) do
    n = length(nums)
    nums_tuple = List.to_tuple(nums)

    # Build map from value to tuple of sorted indices
    idx_map =
      Enum.reduce(Enum.with_index(nums), %{}, fn {val, i}, acc ->
        Map.update(acc, val, [i], fn lst -> [i | lst] end)
      end)
      |> Enum.map(fn {k, v} -> {k, List.to_tuple(Enum.reverse(v))} end)
      |> Enum.into(%{})

    Enum.map(queries, fn q ->
      val = :erlang.element(q + 1, nums_tuple)
      indices = Map.fetch!(idx_map, val)
      len = tuple_size(indices)

      if len == 1 do
        -1
      else
        pos = find_position(indices, q)

        prev_pos = if pos == 0, do: len - 1, else: pos - 1
        next_pos = if pos == len - 1, do: 0, else: pos + 1

        idx_prev = :erlang.element(prev_pos + 1, indices)
        idx_next = :erlang.element(next_pos + 1, indices)

        d1 = circ_dist(q, idx_prev, n)
        d2 = circ_dist(q, idx_next, n)

        if d1 < d2, do: d1, else: d2
      end
    end)
  end

  defp find_position(tuple, target) do
    do_find_position(tuple, target, 0, tuple_size(tuple) - 1)
  end

  defp do_find_position(_tuple, _target, low, high) when low > high, do: -1

  defp do_find_position(tuple, target, low, high) do
    mid = div(low + high, 2)
    val = :erlang.element(mid + 1, tuple)

    cond do
      val == target ->
        mid

      val < target ->
        do_find_position(tuple, target, mid + 1, high)

      true ->
        do_find_position(tuple, target, low, mid - 1)
    end
  end

  defp circ_dist(a, b, n) do
    diff = abs(a - b)
    rem = n - diff
    if diff < rem, do: diff, else: rem
  end
end
```
