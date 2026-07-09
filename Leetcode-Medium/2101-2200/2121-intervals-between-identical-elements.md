# 2121. Intervals Between Identical Elements

## Cpp

```cpp
class Solution {
public:
    vector<long long> getDistances(vector<int>& arr) {
        int n = arr.size();
        unordered_map<int, vector<int>> idxMap;
        idxMap.reserve(n * 2);
        for (int i = 0; i < n; ++i) {
            idxMap[arr[i]].push_back(i);
        }
        vector<long long> ans(n, 0);
        for (auto& kv : idxMap) {
            const vector<int>& pos = kv.second;
            int m = pos.size();
            if (m == 1) continue;
            vector<long long> pref(m + 1, 0);
            for (int i = 0; i < m; ++i) {
                pref[i + 1] = pref[i] + pos[i];
            }
            long long total = pref[m];
            for (int i = 0; i < m; ++i) {
                long long left = (long long)pos[i] * i - pref[i];
                long long right = (total - pref[i + 1]) - (long long)pos[i] * (m - 1 - i);
                ans[pos[i]] = left + right;
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long[] getDistances(int[] arr) {
        int n = arr.length;
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.computeIfAbsent(arr[i], k -> new ArrayList<>()).add(i);
        }
        long[] ans = new long[n];
        for (List<Integer> indices : map.values()) {
            int m = indices.size();
            long[] pref = new long[m + 1];
            for (int i = 0; i < m; i++) {
                pref[i + 1] = pref[i] + indices.get(i);
            }
            for (int i = 0; i < m; i++) {
                int idx = indices.get(i);
                long leftCount = i;
                long rightCount = m - 1 - i;
                long leftSum = pref[i];
                long rightSum = pref[m] - pref[i + 1];
                ans[idx] = (long) idx * leftCount - leftSum + rightSum - (long) idx * rightCount;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def getDistances(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        pos = defaultdict(list)
        for i, v in enumerate(arr):
            pos[v].append(i)

        res = [0] * len(arr)
        for indices in pos.values():
            k = len(indices)
            if k == 1:
                continue
            prefix = [0] * (k + 1)
            for i in range(k):
                prefix[i + 1] = prefix[i] + indices[i]
            total = prefix[k]
            for p, idx in enumerate(indices):
                left_cnt = p
                right_cnt = k - p - 1
                left_sum = prefix[p]
                right_sum = total - prefix[p + 1]
                res[idx] = idx * left_cnt - left_sum + right_sum - idx * right_cnt
        return res
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        groups = defaultdict(list)
        for i, v in enumerate(arr):
            groups[v].append(i)

        res = [0] * len(arr)
        for idxs in groups.values():
            m = len(idxs)
            if m == 1:
                continue
            prefix = [0] * (m + 1)
            for i in range(m):
                prefix[i + 1] = prefix[i] + idxs[i]
            total = prefix[m]
            for k, idx in enumerate(idxs):
                left_cnt = k
                right_cnt = m - k - 1
                left_sum = idx * left_cnt - prefix[k]
                right_sum = (total - prefix[k + 1]) - idx * right_cnt
                res[idx] = left_sum + right_sum
        return res
```

## C

```c
#include <stdlib.h>

typedef struct {
    int *data;
    int size;
    int cap;
} Vec;

static void vec_push(Vec *v, int val) {
    if (v->size == v->cap) {
        int newCap = v->cap ? v->cap * 2 : 4;
        int *tmp = (int *)realloc(v->data, newCap * sizeof(int));
        if (!tmp) exit(1);
        v->data = tmp;
        v->cap = newCap;
    }
    v->data[v->size++] = val;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* getDistances(int* arr, int arrSize, int* returnSize) {
    if (arrSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    /* Find maximum value to size the bucket array */
    int maxVal = 0;
    for (int i = 0; i < arrSize; ++i)
        if (arr[i] > maxVal) maxVal = arr[i];

    Vec *buckets = (Vec *)calloc(maxVal + 1, sizeof(Vec));

    /* Fill buckets with indices */
    for (int i = 0; i < arrSize; ++i) {
        vec_push(&buckets[arr[i]], i);
    }

    long long *ans = (long long *)malloc(arrSize * sizeof(long long));

    /* Process each bucket */
    for (int v = 0; v <= maxVal; ++v) {
        int k = buckets[v].size;
        if (k == 0) continue;

        long long *pref = (long long *)malloc(k * sizeof(long long));
        for (int i = 0; i < k; ++i) {
            pref[i] = buckets[v].data[i];
            if (i) pref[i] += pref[i - 1];
        }

        for (int p = 0; p < k; ++p) {
            long long idx = buckets[v].data[p];
            long long leftSum = (p > 0) ? pref[p - 1] : 0;
            long long rightSum = pref[k - 1] - pref[p];
            long long leftCnt = p;
            long long rightCnt = k - 1 - p;

            ans[idx] = idx * leftCnt - leftSum + rightSum - idx * rightCnt;
        }

        free(pref);
    }

    /* Clean up */
    for (int v = 0; v <= maxVal; ++v) {
        free(buckets[v].data);
    }
    free(buckets);

    *returnSize = arrSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public long[] GetDistances(int[] arr)
    {
        int n = arr.Length;
        var dict = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++)
        {
            if (!dict.TryGetValue(arr[i], out var list))
            {
                list = new List<int>();
                dict[arr[i]] = list;
            }
            list.Add(i);
        }

        long[] ans = new long[n];
        foreach (var kvp in dict)
        {
            var indices = kvp.Value;
            int m = indices.Count;
            long[] pref = new long[m + 1];
            for (int i = 0; i < m; i++)
                pref[i + 1] = pref[i] + indices[i];

            for (int i = 0; i < m; i++)
            {
                int idx = indices[i];
                long leftCount = i;
                long rightCount = m - i - 1;
                long leftSum = pref[i];
                long rightSum = pref[m] - pref[i + 1];
                ans[idx] = (long)idx * leftCount - leftSum + rightSum - (long)idx * rightCount;
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var getDistances = function(arr) {
    const map = new Map();
    for (let i = 0; i < arr.length; i++) {
        const v = arr[i];
        if (!map.has(v)) map.set(v, []);
        map.get(v).push(i);
    }
    const res = new Array(arr.length).fill(0);
    for (const indices of map.values()) {
        const m = indices.length;
        if (m === 1) continue;
        const prefix = new Array(m + 1);
        prefix[0] = 0;
        for (let i = 0; i < m; i++) {
            prefix[i + 1] = prefix[i] + indices[i];
        }
        const total = prefix[m];
        for (let k = 0; k < m; k++) {
            const idx = indices[k];
            const leftCount = k;
            const rightCount = m - k - 1;
            const leftSum = prefix[k];
            const rightSum = total - prefix[k + 1];
            res[idx] = idx * leftCount - leftSum + (rightSum - idx * rightCount);
        }
    }
    return res;
};
```

## Typescript

```typescript
function getDistances(arr: number[]): number[] {
    const map = new Map<number, number[]>();
    for (let i = 0; i < arr.length; i++) {
        const v = arr[i];
        if (!map.has(v)) map.set(v, []);
        map.get(v)!.push(i);
    }
    const res = new Array<number>(arr.length).fill(0);
    for (const idxs of map.values()) {
        const m = idxs.length;
        if (m <= 1) continue;
        const pref = new Array<number>(m + 1);
        pref[0] = 0;
        for (let i = 0; i < m; i++) {
            pref[i + 1] = pref[i] + idxs[i];
        }
        const totalSum = pref[m];
        for (let k = 0; k < m; k++) {
            const index = idxs[k];
            const leftCount = k;
            const rightCount = m - k - 1;
            const leftSum = pref[k];
            const rightSum = totalSum - pref[k + 1];
            res[index] = index * leftCount - leftSum + (rightSum - index * rightCount);
        }
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function getDistances($arr) {
        $n = count($arr);
        $map = [];
        for ($i = 0; $i < $n; $i++) {
            $val = $arr[$i];
            if (!isset($map[$val])) {
                $map[$val] = [];
            }
            $map[$val][] = $i;
        }

        $res = array_fill(0, $n, 0);

        foreach ($map as $indices) {
            $len = count($indices);
            $prefix = [];
            $sum = 0;
            foreach ($indices as $idx) {
                $sum += $idx;
                $prefix[] = $sum;
            }
            $total = $sum;

            for ($k = 0; $k < $len; $k++) {
                $curIdx = $indices[$k];
                $leftSum = $k > 0 ? $prefix[$k - 1] : 0;
                $rightSum = $total - $prefix[$k];
                $leftCount = $k;
                $rightCount = $len - $k - 1;

                $dist = $curIdx * $leftCount - $leftSum + $rightSum - $curIdx * $rightCount;
                $res[$curIdx] = $dist;
            }
        }

        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func getDistances(_ arr: [Int]) -> [Int] {
        var positions = [Int: [Int]]()
        for (i, v) in arr.enumerated() {
            positions[v, default: []].append(i)
        }
        
        var answer = Array(repeating: 0, count: arr.count)
        
        for (_, idxList) in positions {
            let m = idxList.count
            if m <= 1 { continue }
            
            var prefix = [Int](repeating: 0, count: m)
            prefix[0] = idxList[0]
            if m > 1 {
                for i in 1..<m {
                    prefix[i] = prefix[i - 1] + idxList[i]
                }
            }
            let totalSum = prefix[m - 1]
            
            for t in 0..<m {
                let idx = idxList[t]
                
                var left = 0
                if t > 0 {
                    left = idx * t - prefix[t - 1]
                }
                
                var right = 0
                if t < m - 1 {
                    let sumRightIndices = totalSum - prefix[t]
                    right = sumRightIndices - idx * (m - t - 1)
                }
                
                answer[idx] = left + right
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getDistances(arr: IntArray): LongArray {
        val map = HashMap<Int, MutableList<Int>>()
        for (i in arr.indices) {
            val list = map.getOrPut(arr[i]) { mutableListOf() }
            list.add(i)
        }
        val result = LongArray(arr.size)
        for ((_, indices) in map) {
            val m = indices.size
            if (m == 1) continue
            val prefix = LongArray(m)
            var sum = 0L
            for (i in 0 until m) {
                sum += indices[i].toLong()
                prefix[i] = sum
            }
            val totalSum = prefix[m - 1]
            for (i in 0 until m) {
                val idx = indices[i]
                val leftCount = i
                val rightCount = m - 1 - i
                val leftSum = if (i > 0) prefix[i - 1] else 0L
                val rightSum = totalSum - prefix[i]
                val res = (idx.toLong() * leftCount - leftSum) + (rightSum - idx.toLong() * rightCount)
                result[idx] = res
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> getDistances(List<int> arr) {
    int n = arr.length;
    List<int> ans = List.filled(n, 0);
    Map<int, List<int>> posMap = {};

    for (int i = 0; i < n; i++) {
      int val = arr[i];
      posMap.putIfAbsent(val, () => []).add(i);
    }

    for (var entry in posMap.entries) {
      List<int> idxList = entry.value;
      int m = idxList.length;
      if (m == 1) continue;

      List<int> prefix = List.filled(m, 0);
      prefix[0] = idxList[0];
      for (int i = 1; i < m; i++) {
        prefix[i] = prefix[i - 1] + idxList[i];
      }
      int total = prefix[m - 1];

      for (int k = 0; k < m; k++) {
        int idx = idxList[k];
        int leftCount = k;
        int rightCount = m - 1 - k;
        int sumLeft = k > 0 ? prefix[k - 1] : 0;
        int sumRight = total - prefix[k];
        ans[idx] = idx * leftCount - sumLeft + (sumRight - idx * rightCount);
      }
    }

    return ans;
  }
}
```

## Golang

```go
func getDistances(arr []int) []int64 {
    n := len(arr)
    ans := make([]int64, n)
    groups := make(map[int][]int)

    for i, v := range arr {
        groups[v] = append(groups[v], i)
    }

    for _, idxs := range groups {
        m := len(idxs)
        if m <= 1 {
            continue
        }
        prefix := make([]int64, m)
        for i, idx := range idxs {
            if i == 0 {
                prefix[i] = int64(idx)
            } else {
                prefix[i] = prefix[i-1] + int64(idx)
            }
        }
        total := prefix[m-1]
        for i, idx := range idxs {
            leftCount := int64(i)
            rightCount := int64(m - i - 1)

            var leftSum int64
            if i > 0 {
                leftSum = prefix[i-1]
            }
            rightSum := total - prefix[i]

            ans[idx] = int64(idx)*leftCount - leftSum + (rightSum - int64(idx)*rightCount)
        }
    }

    return ans
}
```

## Ruby

```ruby
def get_distances(arr)
  n = arr.length
  groups = Hash.new { |h, k| h[k] = [] }
  arr.each_with_index { |val, idx| groups[val] << idx }

  result = Array.new(n, 0)

  groups.each_value do |indices|
    len = indices.size
    next if len == 1

    prefix = Array.new(len)
    sum = 0
    indices.each_with_index do |idx, i|
      sum += idx
      prefix[i] = sum
    end
    total_sum = sum

    indices.each_with_index do |idx, i|
      left_count = i
      right_count = len - i - 1
      left_sum = i > 0 ? prefix[i - 1] : 0
      right_sum = total_sum - prefix[i]
      result[idx] = idx * left_count - left_sum + right_sum - idx * right_count
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def getDistances(arr: Array[Int]): Array[Long] = {
        val n = arr.length
        val map = scala.collection.mutable.HashMap[Int, scala.collection.mutable.ArrayBuffer[Int]]()
        var i = 0
        while (i < n) {
            val buf = map.getOrElseUpdate(arr(i), scala.collection.mutable.ArrayBuffer[Int]())
            buf += i
            i += 1
        }
        val ans = new Array[Long](n)
        for ((_, indices) <- map) {
            val k = indices.length
            if (k > 1) {
                val prefix = new Array[Long](k)
                var sum: Long = 0L
                var j = 0
                while (j < k) {
                    sum += indices(j).toLong
                    prefix(j) = sum
                    j += 1
                }
                val total = prefix(k - 1)
                j = 0
                while (j < k) {
                    val idx = indices(j)
                    val leftCount = j
                    val rightCount = k - j - 1
                    val leftSum = if (j > 0) prefix(j - 1) else 0L
                    val rightSum = total - prefix(j)
                    ans(idx) = idx.toLong * leftCount - leftSum + rightSum - idx.toLong * rightCount
                    j += 1
                }
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_distances(arr: Vec<i32>) -> Vec<i64> {
        use std::collections::HashMap;
        let n = arr.len();
        let mut map: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in arr.iter().enumerate() {
            map.entry(v).or_default().push(i);
        }
        let mut ans = vec![0i64; n];
        for positions in map.values() {
            let m = positions.len();
            if m <= 1 {
                continue;
            }
            // prefix sums of indices
            let mut pref: Vec<i64> = vec![0; m + 1];
            for i in 0..m {
                pref[i + 1] = pref[i] + positions[i] as i64;
            }
            for (i, &pos) in positions.iter().enumerate() {
                let left_cnt = i as i64;
                let right_cnt = (m - i - 1) as i64;
                let left_sum = pref[i];
                let right_sum = pref[m] - pref[i + 1];
                let p = pos as i64;
                ans[pos] = p * left_cnt - left_sum + right_sum - p * right_cnt;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (get-distances arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((v (list->vector arr))
         (n (vector-length v))
         (pos-hash (make-hash)))
    ;; collect indices for each value
    (for ([i (in-range n)])
      (let* ((val (vector-ref v i))
             (lst (hash-ref pos-hash val '())))
        (hash-set! pos-hash val (cons i lst))))
    ;; reverse to obtain ascending order
    (for ([key (in-hash-keys pos-hash)])
      (hash-set! pos-hash key (reverse (hash-ref pos-hash key))))
    (define res (make-vector n 0))
    ;; compute distances per value group
    (for ([indices-list (in-hash-values pos-hash)])
      (let* ((idx-vec (list->vector indices-list))
             (len (vector-length idx-vec))
             (prefix (make-vector (+ len 1) 0)))
        (for ([i (in-range len)])
          (vector-set! prefix (+ i 1)
                       (+ (vector-ref prefix i) (vector-ref idx-vec i))))
        (for ([j (in-range len)])
          (let* ((idx (vector-ref idx-vec j))
                 (left (- (* idx j) (vector-ref prefix j)))
                 (right (- (- (vector-ref prefix len)
                              (vector-ref prefix (+ j 1)))
                           (* idx (- len j 1))))
                 (total (+ left right)))
            (vector-set! res idx total)))))
    (vector->list res)))
```

## Erlang

```erlang
-module(solution).
-export([get_distances/1]).

-spec get_distances(Arr :: [integer()]) -> [integer()].
get_distances(Arr) ->
    Len = length(Arr),
    Map0 = build_map(Arr, 0, #{}),
    Map = maps:map(fun(_K, V) -> lists:reverse(V) end, Map0),
    ResultArray = array:new(Len, {default, 0}),
    FinalArray = maps:fold(
        fun(_Val, Indices, AccArr) ->
            process_indices(Indices, AccArr)
        end,
        ResultArray,
        Map),
    array:to_list(FinalArray).

build_map([], _Idx, Map) -> Map;
build_map([H|T], Idx, Map) ->
    NewMap = maps:update_with(
                H,
                fun(L) -> [Idx | L] end,
                [Idx],
                Map),
    build_map(T, Idx + 1, NewMap).

process_indices(Indices, Array) ->
    Total = lists:sum(Indices),
    K = length(Indices),
    process_loop(Indices, 0, 0, K, Total, Array).

process_loop([], _Pos, _LeftSum, _K, _Total, Array) -> Array;
process_loop([Idx | Rest], Pos, LeftSum, K, Total, Array) ->
    LeftCount = Pos,
    RightCount = K - Pos - 1,
    LeftDist = Idx * LeftCount - LeftSum,
    RightDist = (Total - LeftSum - Idx) - Idx * RightCount,
    NewArray = array:set(Idx, LeftDist + RightDist, Array),
    process_loop(Rest, Pos + 1, LeftSum + Idx, K, Total, NewArray).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_distances(arr :: [integer]) :: [integer]
  def get_distances(arr) do
    n = length(arr)

    index_map =
      arr
      |> Enum.with_index()
      |> Enum.reduce(%{}, fn {val, idx}, acc ->
        Map.update(acc, val, [idx], fn list -> [idx | list] end)
      end)

    ans_map =
      Enum.reduce(index_map, %{}, fn {_val, rev_list}, acc ->
        idxs = Enum.reverse(rev_list)
        m = length(idxs)
        sum_all = Enum.sum(idxs)

        {map_after, _} =
          Enum.with_index(idxs)
          |> Enum.reduce({acc, 0}, fn {i, p}, {map_acc, sum_before} ->
            left = i * p - sum_before
            sum_after = sum_all - sum_before - i
            right = sum_after - i * (m - p - 1)
            total = left + right
            {Map.put(map_acc, i, total), sum_before + i}
          end)

        map_after
      end)

    Enum.map(0..(n - 1), fn i -> Map.get(ans_map, i) end)
  end
end
```
