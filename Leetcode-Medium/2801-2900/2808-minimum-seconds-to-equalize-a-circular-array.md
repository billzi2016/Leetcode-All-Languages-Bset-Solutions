# 2808. Minimum Seconds to Equalize a Circular Array

## Cpp

```cpp
class Solution {
public:
    int minimumSeconds(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, vector<int>> pos;
        pos.reserve(n * 2);
        for (int i = 0; i < n; ++i) {
            pos[nums[i]].push_back(i);
        }
        int ans = n; // upper bound
        for (auto& kv : pos) {
            const vector<int>& v = kv.second;
            int maxGap = 0;
            for (size_t i = 1; i < v.size(); ++i) {
                maxGap = max(maxGap, v[i] - v[i-1]);
            }
            // wrap-around gap
            maxGap = max(maxGap, v[0] + n - v.back());
            ans = min(ans, maxGap / 2);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumSeconds(List<Integer> nums) {
        int n = nums.size();
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int v = nums.get(i);
            map.computeIfAbsent(v, k -> new ArrayList<>()).add(i);
        }
        int answer = Integer.MAX_VALUE;
        for (List<Integer> positions : map.values()) {
            int maxGap = 0;
            for (int i = 0; i < positions.size() - 1; i++) {
                int gap = positions.get(i + 1) - positions.get(i) - 1;
                if (gap > maxGap) maxGap = gap;
            }
            // wrap-around gap
            int first = positions.get(0);
            int last = positions.get(positions.size() - 1);
            int wrapGap = n - (last - first + 1); // elements between last and first circularly
            if (wrapGap > maxGap) maxGap = wrapGap;
            int seconds = (maxGap + 1) / 2; // ceil division
            answer = Math.min(answer, seconds);
        }
        return answer == Integer.MAX_VALUE ? 0 : answer;
    }
}
```

## Python

```python
class Solution(object):
    def minimumSeconds(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pos = {}
        for i, v in enumerate(nums):
            pos.setdefault(v, []).append(i)

        ans = n  # upper bound
        for idxs in pos.values():
            max_half_gap = 0
            m = len(idxs)
            for i in range(m):
                cur = idxs[i]
                nxt = idxs[(i + 1) % m] if i + 1 < m else idxs[0] + n
                diff = nxt - cur
                max_half_gap = max(max_half_gap, diff // 2)
            ans = min(ans, max_half_gap)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        positions = {}
        for i, v in enumerate(nums):
            positions.setdefault(v, []).append(i)

        answer = float('inf')
        for idxs in positions.values():
            max_gap = 0
            prev = idxs[-1] - n  # handle circular wrap
            for cur in idxs:
                gap = cur - prev - 1  # number of non‑v elements between occurrences
                if gap > max_gap:
                    max_gap = gap
                prev = cur
            seconds = (max_gap + 1) // 2
            if seconds < answer:
                answer = seconds
        return answer
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int val;
    int idx;
} Pair;

static int cmpPair(const void *a, const void *b) {
    const Pair *p1 = (const Pair *)a;
    const Pair *p2 = (const Pair *)b;
    if (p1->val != p2->val)
        return (p1->val < p2->val) ? -1 : 1;
    if (p1->idx != p2->idx)
        return (p1->idx < p2->idx) ? -1 : 1;
    return 0;
}

int minimumSeconds(int* nums, int numsSize) {
    if (numsSize <= 1) return 0;

    Pair *arr = (Pair *)malloc(sizeof(Pair) * numsSize);
    for (int i = 0; i < numsSize; ++i) {
        arr[i].val = nums[i];
        arr[i].idx = i;
    }

    qsort(arr, numsSize, sizeof(Pair), cmpPair);

    int answer = INT_MAX;

    int i = 0;
    while (i < numsSize) {
        int curVal = arr[i].val;
        int firstIdx = arr[i].idx;
        int prevIdx = firstIdx;
        int maxGap = 0;
        ++i;
        while (i < numsSize && arr[i].val == curVal) {
            int gap = arr[i].idx - prevIdx;
            if (gap > maxGap) maxGap = gap;
            prevIdx = arr[i].idx;
            ++i;
        }
        // circular gap
        int circGap = firstIdx + numsSize - prevIdx;
        if (circGap > maxGap) maxGap = circGap;

        int secondsNeeded = maxGap / 2; // floor division
        if (secondsNeeded < answer) answer = secondsNeeded;
    }

    free(arr);
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumSeconds(IList<int> nums) {
        int n = nums.Count;
        var dict = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            int v = nums[i];
            if (!dict.TryGetValue(v, out var list)) {
                list = new List<int>();
                dict[v] = list;
            }
            list.Add(i);
        }

        int answer = int.MaxValue;

        foreach (var kvp in dict) {
            var positions = kvp.Value;
            int maxGap = 0;
            for (int i = 1; i < positions.Count; i++) {
                int gap = positions[i] - positions[i - 1] - 1;
                if (gap > maxGap) maxGap = gap;
            }
            // wrap-around gap
            int wrapGap = n - positions[positions.Count - 1] + positions[0] - 1;
            if (wrapGap > maxGap) maxGap = wrapGap;

            int seconds = (maxGap + 1) / 2; // ceil(gap/2)
            if (seconds < answer) answer = seconds;
        }

        return answer == int.MaxValue ? 0 : answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumSeconds = function(nums) {
    const n = nums.length;
    const posMap = new Map();
    for (let i = 0; i < n; i++) {
        const v = nums[i];
        if (!posMap.has(v)) posMap.set(v, []);
        posMap.get(v).push(i);
    }
    let answer = Infinity;
    for (const positions of posMap.values()) {
        let seconds;
        if (positions.length === 1) {
            seconds = Math.floor(n / 2);
        } else {
            let maxSec = 0;
            for (let i = 0; i < positions.length - 1; i++) {
                const diff = positions[i + 1] - positions[i];
                maxSec = Math.max(maxSec, Math.floor(diff / 2));
            }
            const wrapDiff = positions[0] + n - positions[positions.length - 1];
            maxSec = Math.max(maxSec, Math.floor(wrapDiff / 2));
            seconds = maxSec;
        }
        answer = Math.min(answer, seconds);
    }
    return answer === Infinity ? 0 : answer;
};
```

## Typescript

```typescript
function minimumSeconds(nums: number[]): number {
    const n = nums.length;
    const posMap = new Map<number, number[]>();
    for (let i = 0; i < n; i++) {
        const v = nums[i];
        if (!posMap.has(v)) posMap.set(v, []);
        posMap.get(v)!.push(i);
    }
    let answer = Number.MAX_SAFE_INTEGER;
    for (const positions of posMap.values()) {
        const m = positions.length;
        if (m === n) {
            return 0; // all elements already equal
        }
        let maxGap = 0;
        for (let i = 1; i < m; i++) {
            const gap = positions[i] - positions[i - 1] - 1;
            if (gap > maxGap) maxGap = gap;
        }
        const wrapGap = (positions[0] + n) - positions[m - 1] - 1;
        if (wrapGap > maxGap) maxGap = wrapGap;
        const seconds = Math.ceil(maxGap / 2);
        if (seconds < answer) answer = seconds;
    }
    return answer === Number.MAX_SAFE_INTEGER ? 0 : answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumSeconds($nums) {
        $n = count($nums);
        $posMap = [];
        foreach ($nums as $i => $val) {
            if (!isset($posMap[$val])) {
                $posMap[$val] = [];
            }
            $posMap[$val][] = $i;
        }

        $answer = PHP_INT_MAX;

        foreach ($posMap as $indices) {
            $maxNeeded = 0;
            $len = count($indices);
            // gaps between consecutive occurrences
            for ($k = 1; $k < $len; ++$k) {
                $dist = $indices[$k] - $indices[$k - 1];
                $need = intdiv($dist, 2);
                if ($need > $maxNeeded) {
                    $maxNeeded = $need;
                }
            }
            // circular gap
            $dist = $indices[0] + $n - $indices[$len - 1];
            $need = intdiv($dist, 2);
            if ($need > $maxNeeded) {
                $maxNeeded = $need;
            }

            if ($maxNeeded < $answer) {
                $answer = $maxNeeded;
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func minimumSeconds(_ nums: [Int]) -> Int {
        var positionsByValue = [Int: [Int]]()
        for (idx, val) in nums.enumerated() {
            positionsByValue[val, default: []].append(idx)
        }
        let n = nums.count
        var result = Int.max
        
        for (_, pos) in positionsByValue {
            let m = pos.count
            var maxSec = 0
            if m == 1 {
                // whole circle distance is n
                maxSec = n / 2
            } else {
                // gaps between consecutive occurrences
                for i in 0..<(m - 1) {
                    let dist = pos[i + 1] - pos[i]
                    let sec = dist / 2   // floor((j-i)/2)
                    if sec > maxSec { maxSec = sec }
                }
                // wrap‑around gap
                let wrapDist = (n - pos[m - 1]) + pos[0]
                let secWrap = wrapDist / 2
                if secWrap > maxSec { maxSec = secWrap }
            }
            if maxSec < result {
                result = maxSec
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumSeconds(nums: List<Int>): Int {
        val posMap = HashMap<Int, MutableList<Int>>()
        for (i in nums.indices) {
            val v = nums[i]
            posMap.computeIfAbsent(v) { mutableListOf() }.add(i)
        }
        var answer = Int.MAX_VALUE
        val n = nums.size
        for (list in posMap.values) {
            var maxSec = 0
            // gaps between consecutive occurrences
            for (i in 0 until list.size - 1) {
                val gap = list[i + 1] - list[i] - 1
                if (gap > 0) {
                    val sec = (gap + 1) / 2
                    if (sec > maxSec) maxSec = sec
                }
            }
            // circular gap
            val first = list[0]
            val last = list[list.size - 1]
            val circGap = n - last + first - 1
            if (circGap > 0) {
                val sec = (circGap + 1) / 2
                if (sec > maxSec) maxSec = sec
            }
            if (maxSec < answer) answer = maxSec
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minimumSeconds(List<int> nums) {
    int n = nums.length;
    Map<int, List<int>> positions = {};
    for (int i = 0; i < n; i++) {
      positions.putIfAbsent(nums[i], () => []).add(i);
    }

    int answer = n; // upper bound
    for (var entry in positions.entries) {
      List<int> idx = entry.value;
      int m = idx.length;
      int maxTime = 0;
      for (int i = 0; i < m; i++) {
        int cur = idx[i];
        int next = (i + 1 < m) ? idx[i + 1] : idx[0] + n;
        int dist = next - cur;
        int time = dist ~/ 2;
        if (time > maxTime) maxTime = time;
      }
      if (maxTime < answer) answer = maxTime;
    }

    return answer;
  }
}
```

## Golang

```go
func minimumSeconds(nums []int) int {
    n := len(nums)
    positions := make(map[int][]int)
    for i, v := range nums {
        positions[v] = append(positions[v], i)
    }
    ans := n
    for _, pos := range positions {
        maxGap := 0
        m := len(pos)
        for i := 0; i < m; i++ {
            var d int
            if i == m-1 {
                d = (pos[0] + n) - pos[i]
            } else {
                d = pos[i+1] - pos[i]
            }
            cur := d / 2 // floor division
            if cur > maxGap {
                maxGap = cur
            }
        }
        if maxGap < ans {
            ans = maxGap
        }
    }
    return ans
}
```

## Ruby

```ruby
def minimum_seconds(nums)
  n = nums.length
  positions = Hash.new { |h, k| h[k] = [] }
  nums.each_with_index { |v, i| positions[v] << i }

  answer = Float::INFINITY

  positions.each_value do |idxs|
    max_gap = 0
    m = idxs.length
    (0...m).each do |i|
      cur = idxs[i]
      nxt = (i + 1 < m) ? idxs[i + 1] : idxs[0] + n
      dist = nxt - cur
      gap = dist / 2
      max_gap = gap if gap > max_gap
    end
    answer = max_gap if max_gap < answer
  end

  answer.to_i
end
```

## Scala

```scala
object Solution {
    def minimumSeconds(nums: List[Int]): Int = {
        val n = nums.length
        val posMap = scala.collection.mutable.Map[Int, scala.collection.mutable.ArrayBuffer[Int]]()
        for (i <- nums.indices) {
            val v = nums(i)
            posMap.getOrElseUpdate(v, scala.collection.mutable.ArrayBuffer()) += i
        }
        var answer = Int.MaxValue
        for ((_, arr) <- posMap) {
            var maxSec = 0
            val sz = arr.size
            for (k <- 0 until sz) {
                val cur = arr(k)
                val next = if (k == sz - 1) arr(0) + n else arr(k + 1)
                val diff = next - cur
                val secs = diff / 2
                if (secs > maxSec) maxSec = secs
            }
            if (maxSec < answer) answer = maxSec
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_seconds(nums: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        let n = nums.len();
        let mut map: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in nums.iter().enumerate() {
            map.entry(v).or_default().push(i);
        }
        let mut answer = i32::MAX;
        for positions in map.values() {
            if positions.len() == n {
                return 0;
            }
            let mut max_gap: usize = 0;
            for w in positions.windows(2) {
                let gap = w[1] - w[0] - 1;
                if gap > max_gap {
                    max_gap = gap;
                }
            }
            // circular gap
            let circ_gap = positions[0] + n - positions[positions.len() - 1] - 1;
            if circ_gap > max_gap {
                max_gap = circ_gap;
            }
            let seconds = ((max_gap as i32) + 1) / 2;
            if seconds < answer {
                answer = seconds;
            }
        }
        answer
    }
}
```

## Racket

```racket
(define/contract (minimum-seconds nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((vec (list->vector nums))
         (n (vector-length vec))
         (hash (make-hash)))
    ;; collect positions for each value
    (for ([i (in-range n)])
      (let* ((val (vector-ref vec i))
             (lst (hash-ref hash val '())))
        (hash-set! hash val (cons i lst))))
    (define best n) ; upper bound
    ;; evaluate each distinct value
    (for ([key (in-hash-keys hash)])
      (let* ((pos-list (reverse (hash-ref hash key))) ; sorted ascending
             ;; compute maximal gap between consecutive occurrences
             (max-gap
              (let loop ((prev (car pos-list))
                         (rest (cdr pos-list))
                         (mx 0))
                (if (null? rest)
                    (let* ((first (car pos-list))
                           (last prev)
                           (gap-circ (- (+ first n) last 1))) ; circular gap
                      (if (> gap-circ mx) gap-circ mx))
                    (let* ((curr (car rest))
                           (gap (- curr prev 1))
                           (new-mx (if (> gap mx) gap mx)))
                      (loop curr (cdr rest) new-mx)))))
             (seconds (quotient (+ max-gap 1) 2))) ; ceil(gap/2)
        (when (< seconds best)
          (set! best seconds))))
    best))
```

## Erlang

```erlang
-spec minimum_seconds(Nums :: [integer()]) -> integer().
minimum_seconds(Nums) ->
    N = length(Nums),
    Map = build_map(Nums, 0, #{}),
    maps:fold(
        fun(_Key, RevPosList, undefined) ->
                PosList = lists:reverse(RevPosList),
                compute_needed(PosList, N);
           (_Key, RevPosList, Acc) ->
                PosList = lists:reverse(RevPosList),
                Needed = compute_needed(PosList, N),
                erlang:min(Acc, Needed)
        end,
        undefined,
        Map).

build_map([], _Idx, Map) -> Map;
build_map([H|T], Idx, Map) ->
    Prev = maps:get(H, Map, []),
    NewMap = maps:put(H, [Idx|Prev], Map),
    build_map(T, Idx + 1, NewMap).

compute_needed(PosList, N) ->
    InternalMax = internal_max_gap(PosList, 0),
    First = hd(PosList),
    Last = lists:last(PosList),
    WrapGap = (First + N) - Last,
    WrapSec = WrapGap div 2,
    erlang:max(InternalMax, WrapSec).

internal_max_gap([_], Max) -> Max;
internal_max_gap([A,B|Rest], Max) ->
    Gap = B - A,
    Sec = Gap div 2,
    NewMax = erlang:max(Max, Sec),
    internal_max_gap([B|Rest], NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_seconds(nums :: [integer]) :: integer
  def minimum_seconds(nums) do
    n = length(nums)

    idx_map =
      nums
      |> Enum.with_index()
      |> Enum.reduce(%{}, fn {val, idx}, acc ->
        Map.update(acc, val, [idx], fn lst -> [idx | lst] end)
      end)

    # Initialize answer with worst case (n seconds)
    Enum.reduce(idx_map, n, fn {_val, rev_positions}, best ->
      positions = Enum.reverse(rev_positions)
      max_sec = max_seconds(positions, n)
      if max_sec < best, do: max_sec, else: best
    end)
  end

  defp max_seconds([first | _] = positions, n) do
    # Process consecutive pairs
    {max_gap, last_pos} =
      Enum.reduce(tl(positions), {0, first}, fn pos, {mx, prev} ->
        dist = pos - prev
        sec = div(dist, 2)
        new_mx = if sec > mx, do: sec, else: mx
        {new_mx, pos}
      end)

    # Wrap-around gap
    last = List.last(positions)
    wrap_dist = (first + n) - last
    wrap_sec = div(wrap_dist, 2)

    if wrap_sec > max_gap, do: wrap_sec, else: max_gap
  end
end
```
