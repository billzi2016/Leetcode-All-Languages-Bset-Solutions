# 3347. Maximum Frequency of an Element After Performing Operations II

## Cpp

```cpp
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        using ll = long long;
        int n = nums.size();
        unordered_map<ll,int> freq;
        vector<ll> cand;
        cand.reserve(3LL*n);
        for (int x : nums) {
            ll v = x;
            freq[v]++;
            cand.push_back(v);
            cand.push_back(v - (ll)k);
            cand.push_back(v + (ll)k);
        }
        sort(cand.begin(), cand.end());
        cand.erase(unique(cand.begin(), cand.end()), cand.end());

        vector<pair<ll,int>> events;
        events.reserve(2LL*n);
        for (int x : nums) {
            ll a = (ll)x - k;
            ll b = (ll)x + k;
            events.emplace_back(a, 1);
            events.emplace_back(b + 1, -1); // exclusive end
        }
        sort(events.begin(), events.end());

        int best = 0;
        ll cur = 0;
        size_t eIdx = 0;
        for (ll v : cand) {
            while (eIdx < events.size() && events[eIdx].first <= v) {
                cur += events[eIdx].second;
                ++eIdx;
            }
            ll totalWithin = cur; // intervals covering v
            int exact = 0;
            auto it = freq.find(v);
            if (it != freq.end()) exact = it->second;
            ll other = totalWithin - exact;
            ll achievable = exact + min<ll>(numOperations, other);
            if (achievable > best) best = (int)achievable;
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int maxFrequency(int[] nums, int k, int numOperations) {
        int n = nums.length;
        int[] sorted = nums.clone();
        java.util.Arrays.sort(sorted);
        java.util.HashMap<Integer, Integer> freq = new java.util.HashMap<>();
        for (int v : nums) {
            freq.put(v, freq.getOrDefault(v, 0) + 1);
        }
        java.util.HashSet<Long> seen = new java.util.HashSet<>(n * 3);
        int answer = 0;
        for (int v : nums) {
            long[] candidates = {v, (long)v - k, (long)v + k};
            for (long x : candidates) {
                if (!seen.add(x)) continue; // already processed
                int left = lowerBound(sorted, x - k);
                int right = upperBound(sorted, x + k);
                int totalCovered = right - left;
                int eq = 0;
                if (x >= Integer.MIN_VALUE && x <= Integer.MAX_VALUE) {
                    eq = freq.getOrDefault((int)x, 0);
                }
                long possible = Math.min((long)eq + numOperations, (long)totalCovered);
                if (possible > answer) answer = (int)possible;
            }
        }
        return answer;
    }

    private int lowerBound(int[] arr, long target) {
        int l = 0, r = arr.length;
        while (l < r) {
            int m = (l + r) >>> 1;
            if ((long)arr[m] < target) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return l;
    }

    private int upperBound(int[] arr, long target) {
        int l = 0, r = arr.length;
        while (l < r) {
            int m = (l + r) >>> 1;
            if ((long)arr[m] <= target) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return l;
    }
}
```

## Python

```python
class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        from collections import defaultdict

        freq = defaultdict(int)
        events = defaultdict(int)
        candidates = set()

        for x in nums:
            freq[x] += 1
            start = x - k
            end = x + k
            events[start] += 1               # interval starts (inclusive)
            events[end + 1] -= 1             # interval ends after 'end'
            candidates.add(x)
            candidates.add(start)
            candidates.add(end)

        points = sorted(set(events.keys()) | candidates)

        active = 0
        ans = 0
        for p in points:
            if p in events:
                active += events[p]          # apply delta before evaluation (intervals are inclusive)
            if p in candidates:
                eq = freq.get(p, 0)
                total = active               # intervals covering p
                cur = eq + min(numOperations, total - eq)
                if cur > ans:
                    ans = cur

        return ans
```

## Python3

```python
from typing import List
import bisect

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        candidates = set()
        for x in nums:
            candidates.add(x)
            candidates.add(x - k)
            candidates.add(x + k)

        ans = 0
        for v in candidates:
            left = bisect.bisect_left(nums, v - k)
            right = bisect.bisect_right(nums, v + k)
            total_in_range = right - left

            cnt_eq = bisect.bisect_right(nums, v) - bisect.bisect_left(nums, v)

            eligible_to_change = total_in_range - cnt_eq
            freq = cnt_eq + min(numOperations, eligible_to_change)
            if freq > ans:
                ans = freq

        return ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

int maxFrequency(int* nums, int numsSize, int k, int numOperations) {
    vector<long long> a(numsSize);
    for (int i = 0; i < numsSize; ++i) a[i] = nums[i];
    sort(a.begin(), a.end());

    unordered_set<long long> cand;
    cand.reserve((size_t)numsSize * 3);
    for (long long v : a) {
        cand.insert(v);
        cand.insert(v - (long long)k);
        cand.insert(v + (long long)k);
    }

    int ans = 0;
    for (long long v : cand) {
        long long leftVal = v - (long long)k;
        long long rightVal = v + (long long)k;

        auto itL = lower_bound(a.begin(), a.end(), leftVal);
        auto itR = upper_bound(a.begin(), a.end(), rightVal);
        int total = (int)(itR - itL);

        if (total <= ans) continue; // cannot improve

        auto eqL = lower_bound(a.begin(), a.end(), v);
        auto eqR = upper_bound(a.begin(), a.end(), v);
        int equalCnt = (int)(eqR - eqL);

        int opsNeeded = total - equalCnt;
        if (opsNeeded <= numOperations) {
            ans = max(ans, total);
        }
    }

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MaxFrequency(int[] nums, int k, int numOperations) {
        int n = nums.Length;
        long[] sorted = new long[n];
        for (int i = 0; i < n; i++) sorted[i] = nums[i];
        Array.Sort(sorted);

        // frequency of each original value
        var freq = new Dictionary<long, int>();
        foreach (int x in nums) {
            long v = x;
            if (!freq.ContainsKey(v)) freq[v] = 0;
            freq[v]++;
        }

        // collect candidate target values: num, num-k, num+k
        var candidates = new HashSet<long>();
        foreach (int x in nums) {
            long v = x;
            candidates.Add(v);
            candidates.Add(v - k);
            candidates.Add(v + k);
        }

        int best = 0;

        foreach (long target in candidates) {
            // count of elements within [target - k, target + k]
            long leftVal = target - k;
            long rightVal = target + k;

            int leftIdx = LowerBound(sorted, leftVal);
            int rightIdx = UpperBound(sorted, rightVal); // first > rightVal
            int totalInRange = rightIdx - leftIdx;

            int exactFreq = freq.ContainsKey(target) ? freq[target] : 0;
            int reachableNotEqual = totalInRange - exactFreq;

            int possible = exactFreq + Math.Min(numOperations, reachableNotEqual);
            if (possible > best) best = possible;
        }

        return best;
    }

    private int LowerBound(long[] arr, long target) {
        int l = 0, r = arr.Length;
        while (l < r) {
            int m = (l + r) >> 1;
            if (arr[m] < target) l = m + 1;
            else r = m;
        }
        return l;
    }

    private int UpperBound(long[] arr, long target) {
        int l = 0, r = arr.Length;
        while (l < r) {
            int m = (l + r) >> 1;
            if (arr[m] <= target) l = m + 1;
            else r = m;
        }
        return l;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} numOperations
 * @return {number}
 */
var maxFrequency = function(nums, k, numOperations) {
    const n = nums.length;
    if (n === 0) return 0;
    nums.sort((a, b) => a - b);
    
    // frequency map of original values
    const freqMap = new Map();
    for (const v of nums) {
        freqMap.set(v, (freqMap.get(v) || 0) + 1);
    }
    
    // collect candidate target values: num, num-k, num+k
    const candidates = new Set();
    for (const v of nums) {
        candidates.add(v);
        candidates.add(v - k);
        candidates.add(v + k);
    }
    
    // binary search helpers
    const lowerBound = (arr, target) => {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] >= target) r = m;
            else l = m + 1;
        }
        return l;
    };
    
    const upperBound = (arr, target) => {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] > target) r = m;
            else l = m + 1;
        }
        return l;
    };
    
    let answer = 0;
    for (const v of candidates) {
        const left = v - k;
        const right = v + k;
        const lo = lowerBound(nums, left);
        const hi = upperBound(nums, right);
        const reachable = hi - lo; // total elements that can be turned into v
        if (reachable === 0) continue;
        const already = freqMap.get(v) || 0;
        const opsNeeded = reachable - already;
        if (opsNeeded <= numOperations) {
            if (reachable > answer) answer = reachable;
        }
    }
    
    return answer;
};
```

## Typescript

```typescript
function maxFrequency(nums: number[], k: number, numOperations: number): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const firstPos = new Array<number>(n);
    for (let i = 0; i < n; i++) {
        if (i === 0 || nums[i] !== nums[i - 1]) firstPos[i] = i;
        else firstPos[i] = firstPos[i - 1];
    }
    let left = 0;
    let answer = 0;
    for (let right = 0; right < n; right++) {
        while (nums[right] - nums[left] > k) left++;
        const windowSize = right - left + 1;
        const startEqual = Math.max(left, firstPos[right]);
        const cntEqual = right - startEqual + 1;
        const nonEqual = windowSize - cntEqual;
        const possible = cntEqual + Math.min(numOperations, nonEqual);
        if (possible > answer) answer = possible;
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $numOperations
     * @return Integer
     */
    function maxFrequency($nums, $k, $numOperations) {
        sort($nums);
        $origCount = [];
        foreach ($nums as $v) {
            if (!isset($origCount[$v])) {
                $origCount[$v] = 0;
            }
            $origCount[$v]++;
        }

        $candidates = [];
        foreach ($nums as $v) {
            $candidates[] = $v;
            $candidates[] = $v - $k;
            $candidates[] = $v + $k;
        }
        sort($candidates);
        $candidates = array_values(array_unique($candidates, SORT_NUMERIC));

        $n = count($nums);
        $l = 0;
        $r = 0;
        $ans = 0;

        foreach ($candidates as $x) {
            $low = $x - $k;
            $high = $x + $k;

            while ($l < $n && $nums[$l] < $low) {
                $l++;
            }
            while ($r < $n && $nums[$r] <= $high) {
                $r++;
            }

            $cover = $r - $l;
            $orig = $origCount[$x] ?? 0;
            $possible = min($cover, $orig + $numOperations);
            if ($possible > $ans) {
                $ans = $possible;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxFrequency(_ nums: [Int], _ k: Int, _ numOperations: Int) -> Int {
        var baseCount = [Int64:Int]()
        var events = [(pos: Int64, delta: Int)]()
        var pointsSet = Set<Int64>()
        let kk = Int64(k)
        for v in nums {
            let val = Int64(v)
            baseCount[val, default: 0] += 1
            let a = val - kk
            let b = val + kk
            events.append((pos: a, delta: 1))
            events.append((pos: b + 1, delta: -1))
            pointsSet.insert(a)
            pointsSet.insert(val)
            pointsSet.insert(b)
        }
        events.sort { $0.pos < $1.pos }
        var points = Array(pointsSet)
        points.sort()
        var idx = 0
        var cover: Int64 = 0
        var ans: Int64 = 0
        let ops = Int64(numOperations)
        for p in points {
            while idx < events.count && events[idx].pos <= p {
                cover += Int64(events[idx].delta)
                idx += 1
            }
            let base = Int64(baseCount[p] ?? 0)
            let freq = min(cover, base + ops)
            if freq > ans { ans = freq }
        }
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
import java.util.HashMap

class Solution {
    fun maxFrequency(nums: IntArray, k: Int, numOperations: Int): Int {
        if (nums.isEmpty()) return 0
        val n = nums.size
        val arr = nums.clone()
        arr.sort()

        // count occurrences of each value
        val cntMap = HashMap<Int, Int>()
        for (v in arr) {
            cntMap[v] = (cntMap[v] ?: 0) + 1
        }

        fun lowerBound(target: Long): Int {
            var l = 0
            var r = n
            while (l < r) {
                val m = (l + r) ushr 1
                if (arr[m].toLong() >= target) r = m else l = m + 1
            }
            return l
        }

        fun upperBound(target: Long): Int {
            var l = 0
            var r = n
            while (l < r) {
                val m = (l + r) ushr 1
                if (arr[m].toLong() > target) r = m else l = m + 1
            }
            return l
        }

        var answer = 0
        for (i in 0 until n) {
            val base = arr[i].toLong()
            val deltas = longArrayOf(0L, -k.toLong(), k.toLong())
            for (d in deltas) {
                val target = base + d
                // interval [target - k, target + k]
                val leftVal = target - k.toLong()
                val rightVal = target + k.toLong()
                val lIdx = lowerBound(leftVal)
                val rIdx = upperBound(rightVal) - 1
                if (lIdx > rIdx) continue
                val segSize = rIdx - lIdx + 1
                val cntEq = cntMap[target.toInt()] ?: 0
                val possible = kotlin.math.min(segSize, cntEq + numOperations)
                if (possible > answer) answer = possible
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maxFrequency(List<int> nums, int k, int numOperations) {
    if (nums.isEmpty) return 0;
    nums.sort();
    final Map<int, int> freq = {};
    for (var v in nums) {
      freq[v] = (freq[v] ?? 0) + 1;
    }

    final Set<int> candidates = <int>{};
    for (var v in nums) {
      candidates.add(v);
      candidates.add(v - k);
      candidates.add(v + k);
    }

    int lowerBound(List<int> a, int target) {
      int l = 0, r = a.length;
      while (l < r) {
        final m = (l + r) >> 1;
        if (a[m] < target) {
          l = m + 1;
        } else {
          r = m;
        }
      }
      return l;
    }

    int upperBound(List<int> a, int target) {
      int l = 0, r = a.length;
      while (l < r) {
        final m = (l + r) >> 1;
        if (a[m] <= target) {
          l = m + 1;
        } else {
          r = m;
        }
      }
      return l;
    }

    int ans = 0;
    for (final v in candidates) {
      final left = lowerBound(nums, v - k);
      final right = upperBound(nums, v + k);
      final total = right - left;
      final existing = freq[v] ?? 0;
      final possible = total < existing + numOperations ? total : existing + numOperations;
      if (possible > ans) ans = possible;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

func maxFrequency(nums []int, k int, numOperations int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}
	sorted := make([]int, n)
	copy(sorted, nums)
	sort.Ints(sorted)

	freq := make(map[int]int, n)
	for _, v := range nums {
		freq[v]++
	}

	candidates := make(map[int]struct{}, 3*n)
	for _, v := range nums {
		candidates[v] = struct{}{}
		candidates[v-k] = struct{}{}
		candidates[v+k] = struct{}{}
	}

	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	ans := 0
	for v := range candidates {
		leftVal := v - k
		rightVal := v + k

		l := sort.Search(n, func(i int) bool { return sorted[i] >= leftVal })
		r := sort.Search(n, func(i int) bool { return sorted[i] > rightVal }) - 1

		totalReach := 0
		if l <= r {
			totalReach = r - l + 1
		}

		already := freq[v]
		canConvert := totalReach - already
		if canConvert < 0 {
			canConvert = 0
		}
		possible := already + min(numOperations, canConvert)
		if possible > ans {
			ans = possible
		}
	}
	return ans
}
```

## Ruby

```ruby
require 'set'

def max_frequency(nums, k, num_operations)
  n = nums.length
  sorted = nums.sort
  freq = Hash.new(0)
  nums.each { |v| freq[v] += 1 }

  candidates = Set.new
  nums.each do |v|
    candidates.add(v)
    candidates.add(v - k)
    candidates.add(v + k)
  end

  ans = 0
  candidates.each do |t|
    lower = sorted.bsearch_index { |x| x >= t - k } || n
    upper = sorted.bsearch_index { |x| x > t + k } || n
    total = upper - lower
    cnt_eq = freq[t] || 0
    possible = cnt_eq + [num_operations, total - cnt_eq].min
    ans = possible if possible > ans
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maxFrequency(nums: Array[Int], k: Int, numOperations: Int): Int = {
        val n = nums.length
        if (n == 0) return 0

        // frequency map of original values
        val freq = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
        for (v <- nums) {
            freq(v) = freq(v) + 1
        }

        // sorted copy for binary search
        val sorted = nums.clone()
        java.util.Arrays.sort(sorted)

        def lowerBound(arr: Array[Int], target: Long): Int = {
            var l = 0
            var r = arr.length
            while (l < r) {
                val m = (l + r) >>> 1
                if (arr(m).toLong >= target) r = m else l = m + 1
            }
            l
        }

        def upperBound(arr: Array[Int], target: Long): Int = {
            var l = 0
            var r = arr.length
            while (l < r) {
                val m = (l + r) >>> 1
                if (arr(m).toLong > target) r = m else l = m + 1
            }
            l
        }

        var answer = 0
        val kLong = k.toLong

        for (i <- 0 until n) {
            val base = nums(i).toLong
            val deltas = Array(0L, -kLong, kLong)
            for (d <- deltas) {
                val t = base + d
                // count of elements within [t - k, t + k]
                val leftIdx = lowerBound(sorted, t - kLong)
                val rightIdx = upperBound(sorted, t + kLong)
                val cntTotal = rightIdx - leftIdx

                val existing = if (t >= Int.MinValue && t <= Int.MaxValue) freq.getOrElse(t.toInt, 0) else 0
                val possible = math.min(cntTotal, existing + numOperations)

                if (possible > answer) answer = possible
            }
        }

        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_frequency(nums: Vec<i32>, k: i32, num_operations: i32) -> i32 {
        let mut nums = nums;
        nums.sort_unstable();
        // Build distinct values with their frequencies
        let mut distinct: Vec<(i32, usize)> = Vec::new();
        for &v in &nums {
            if let Some(last) = distinct.last_mut() {
                if last.0 == v {
                    last.1 += 1;
                    continue;
                }
            }
            distinct.push((v, 1));
        }

        let n = nums.len();
        let mut answer: i32 = 0;

        for &(val, freq) in &distinct {
            // compute range [val - k, val + k]
            let left_val = (val as i64 - k as i64).max(i32::MIN as i64) as i32;
            let right_val = (val as i64 + k as i64).min(i32::MAX as i64) as i32;

            // lower bound: first index >= left_val
            let l = nums.partition_point(|&x| x < left_val);
            // upper bound: first index > right_val
            let r = nums.partition_point(|&x| x <= right_val);

            let count_in_range = (r - l) as i32;
            let possible = std::cmp::min(count_in_range, freq as i32 + num_operations);
            if possible > answer {
                answer = possible;
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (max-frequency nums k numOperations)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((arr (list->vector (sort nums <)))
         (n (vector-length arr))
         ;; generate candidate target values: nums[i] - k, nums[i], nums[i] + k
         (candidates
          (let loop ((lst nums) (acc '()))
            (if (null? lst)
                acc
                (loop (cdr lst)
                      (cons (+ (car lst) k)
                            (cons (car lst)
                                  (cons (- (car lst) k) acc))))))))
    ;; binary search: first index >= target
    (define (lower-bound vec target)
      (let loop ((lo 0) (hi n))
        (if (= lo hi)
            lo
            (let* ((mid (quotient (+ lo hi) 2))
                   (val (vector-ref vec mid)))
              (if (< val target)
                  (loop (+ mid 1) hi)
                  (loop lo mid))))))
    ;; binary search: first index > target
    (define (upper-bound vec target)
      (let loop ((lo 0) (hi n))
        (if (= lo hi)
            lo
            (let* ((mid (quotient (+ lo hi) 2))
                   (val (vector-ref vec mid)))
              (if (<= val target)
                  (loop (+ mid 1) hi)
                  (loop lo mid))))))
    ;; count of elements exactly equal to target
    (define (count-eq vec target)
      (let* ((lb (lower-bound vec target))
             (ub (upper-bound vec target)))
        (- ub lb)))
    ;; evaluate each candidate
    (let loop ((cands candidates) (best 0))
      (if (null? cands)
          best
          (let* ((t (car cands))
                 (left (lower-bound arr (- t k)))   ; first >= t-k
                 (right (upper-bound arr (+ t k))) ; first > t+k
                 (total (- right left))             ; elements within [t-k, t+k]
                 (eq (count-eq arr t))
                 (near (- total eq))
                 (freq (+ eq (min numOperations near))))
            (loop (cdr cands) (max best freq)))))))
```

## Erlang

```erlang
-spec max_frequency([integer()], integer(), integer()) -> integer().
max_frequency(Nums, K, NumOperations) ->
    Sorted = lists:sort(Nums),
    Arr = array:from_list(Sorted),
    Size = array:size(Arr),

    CountMap = build_count_map(Nums, #{}),

    CandSet = gen_candidates(Nums, K, #{}),

    CandidateVals = maps:keys(CandSet),

    lists:foldl(
      fun(V, Acc) ->
          L = lower_bound(Arr, Size, V - K),
          R = upper_bound(Arr, Size, V + K),
          Total = R - L,
          Orig = maps:get(V, CountMap, 0),
          Convertible = Total - Orig,
          Freq = Orig + min(NumOperations, Convertible),
          if Freq > Acc -> Freq; true -> Acc end
      end,
      0,
      CandidateVals).

build_count_map([], M) ->
    M;
build_count_map([H | T], M) ->
    NewM = maps:update_with(H, fun(C) -> C + 1 end, 1, M),
    build_count_map(T, NewM).

gen_candidates([], _K, Set) ->
    Set;
gen_candidates([Num | Rest], K, Set) ->
    S1 = maps:put(Num, true, Set),
    S2 = maps:put(Num + K, true, S1),
    S3 = maps:put(Num - K, true, S2),
    gen_candidates(Rest, K, S3).

lower_bound(Arr, Size, Target) ->
    lower_bound(0, Size, Arr, Target).

lower_bound(Low, High, _Arr, _Target) when Low >= High ->
    Low;
lower_bound(Low, High, Arr, Target) ->
    Mid = (Low + High) div 2,
    case array:get(Mid, Arr) >= Target of
        true -> lower_bound(Low, Mid, Arr, Target);
        false -> lower_bound(Mid + 1, High, Arr, Target)
    end.

upper_bound(Arr, Size, Target) ->
    upper_bound(0, Size, Arr, Target).

upper_bound(Low, High, _Arr, _Target) when Low >= High ->
    Low;
upper_bound(Low, High, Arr, Target) ->
    Mid = (Low + High) div 2,
    case array:get(Mid, Arr) > Target of
        true -> upper_bound(Low, Mid, Arr, Target);
        false -> upper_bound(Mid + 1, High, Arr, Target)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_frequency(nums :: [integer], k :: integer, num_operations :: integer) :: integer
  def max_frequency(nums, k, num_operations) do
    sorted = Enum.sort(nums)
    arr = List.to_tuple(sorted)
    len = tuple_size(arr)

    freq_map =
      Enum.reduce(nums, %{}, fn x, acc ->
        Map.update(acc, x, 1, &(&1 + 1))
      end)

    candidates =
      nums
      |> Enum.flat_map(fn x -> [x, x - k, x + k] end)
      |> Enum.uniq()

    Enum.reduce(candidates, 0, fn v, best ->
      lb = lower_bound(arr, len, v - k)
      ub = upper_bound(arr, len, v + k)
      total_in_range = ub - lb
      cnt_eq = Map.get(freq_map, v, 0)
      cnt_near = total_in_range - cnt_eq
      freq = cnt_eq + min(num_operations, cnt_near)
      if freq > best, do: freq, else: best
    end)
  end

  defp lower_bound(arr, len, target) do
    do_lower(0, len, arr, target)
  end

  defp do_lower(low, high, _arr, _target) when low >= high, do: low

  defp do_lower(low, high, arr, target) do
    mid = div(low + high, 2)
    val = :erlang.element(mid + 1, arr)

    if val < target do
      do_lower(mid + 1, high, arr, target)
    else
      do_lower(low, mid, arr, target)
    end
  end

  defp upper_bound(arr, len, target) do
    do_upper(0, len, arr, target)
  end

  defp do_upper(low, high, _arr, _target) when low >= high, do: low

  defp do_upper(low, high, arr, target) do
    mid = div(low + high, 2)
    val = :erlang.element(mid + 1, arr)

    if val <= target do
      do_upper(mid + 1, high, arr, target)
    else
      do_upper(low, mid, arr, target)
    end
  end
end
```
