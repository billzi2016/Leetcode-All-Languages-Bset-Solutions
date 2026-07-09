# 0805. Split Array With Same Average

## Cpp

```cpp
class Solution {
public:
    bool splitArraySameAverage(vector<int>& nums) {
        int n = nums.size();
        int total = accumulate(nums.begin(), nums.end(), 0);
        // dp[k] stores all possible sums using exactly k elements
        vector<unordered_set<int>> dp(n + 1);
        dp[0].insert(0);
        for (int num : nums) {
            // iterate sizes in reverse to avoid reuse within same iteration
            for (int k = n - 1; k >= 0; --k) {
                if (dp[k].empty()) continue;
                for (int s : dp[k]) {
                    dp[k + 1].insert(s + num);
                }
            }
        }
        // only need to check up to n/2 due to symmetry
        for (int k = 1; k <= n / 2; ++k) {
            if ((long long)total * k % n != 0) continue;
            int target = total * k / n;
            if (dp[k].find(target) != dp[k].end()) return true;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean splitArraySameAverage(int[] nums) {
        int n = nums.length;
        if (n == 1) return false;
        int total = 0;
        for (int v : nums) total += v;

        // dp[k] stores all possible sums using exactly k elements
        java.util.List<java.util.Set<Integer>> dp = new java.util.ArrayList<>(n + 1);
        for (int i = 0; i <= n; ++i) {
            dp.add(new java.util.HashSet<>());
        }
        dp.get(0).add(0);

        for (int num : nums) {
            for (int k = n; k >= 1; --k) {
                java.util.Set<Integer> prev = dp.get(k - 1);
                if (prev.isEmpty()) continue;
                java.util.Set<Integer> cur = dp.get(k);
                for (int s : prev) {
                    cur.add(s + num);
                }
            }
        }

        for (int k = 1; k < n; ++k) {
            if ((total * k) % n != 0) continue;
            int target = (total * k) / n;
            if (dp.get(k).contains(target)) return true;
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def splitArraySameAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return False
        total = sum(nums)
        # dp[k] is a bitmask where bit s is set iff a subset of size k with sum s exists
        dp = [0] * (n + 1)
        dp[0] = 1  # only sum 0 achievable with 0 elements
        for x in nums:
            # update sizes descending to avoid reuse within same iteration
            for k in range(n, 0, -1):
                if dp[k-1]:
                    dp[k] |= dp[k-1] << x
        for k in range(1, n):
            if (total * k) % n != 0:
                continue
            target = (total * k) // n
            if (dp[k] >> target) & 1:
                return True
        return False
```

## Python3

```python
from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        total = sum(nums)

        # dp[k] = set of possible sums using exactly k elements
        dp = [set() for _ in range(n + 1)]
        dp[0].add(0)

        for num in nums:
            # iterate sizes descending to avoid reuse within same iteration
            for sz in range(n - 1, -1, -1):
                if not dp[sz]:
                    continue
                new_sz = sz + 1
                for s in dp[sz]:
                    dp[new_sz].add(s + num)

        # check each possible subset size
        for k in range(1, n):
            if (k * total) % n != 0:
                continue
            target = (k * total) // n
            if target in dp[k]:
                return True
        return False
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool splitArraySameAverage(int* nums, int numsSize) {
    if (numsSize < 2) return false;

    int total = 0;
    for (int i = 0; i < numsSize; ++i) total += nums[i];

    int n1 = numsSize / 2;
    int n2 = numsSize - n1;
    int maxSum = total;

    /* right half possible sums per subset size */
    char **rightPos = (char **)malloc((n2 + 1) * sizeof(char *));
    for (int i = 0; i <= n2; ++i)
        rightPos[i] = (char *)calloc(maxSum + 1, sizeof(char));

    int totalRightMask = 1 << n2;
    for (int mask = 0; mask < totalRightMask; ++mask) {
        int sum = 0, cnt = 0;
        for (int j = 0; j < n2; ++j)
            if (mask & (1 << j)) {
                sum += nums[n1 + j];
                ++cnt;
            }
        rightPos[cnt][sum] = 1;
    }

    /* left half subsets */
    int totalLeftMask = 1 << n1;
    int *leftSum = (int *)malloc(totalLeftMask * sizeof(int));
    char *leftCnt = (char *)malloc(totalLeftMask * sizeof(char));
    for (int mask = 0; mask < totalLeftMask; ++mask) {
        int sum = 0, cnt = 0;
        for (int j = 0; j < n1; ++j)
            if (mask & (1 << j)) {
                sum += nums[j];
                ++cnt;
            }
        leftSum[mask] = sum;
        leftCnt[mask] = (char)cnt;
    }

    /* try each possible subset size */
    for (int k = 1; k <= numsSize / 2; ++k) {
        if ((long long)total * k % numsSize != 0) continue;
        int target = (int)((long long)total * k / numsSize);

        for (int mask = 0; mask < totalLeftMask; ++mask) {
            int cntL = leftCnt[mask];
            if (cntL > k) continue;
            int need = target - leftSum[mask];
            if (need < 0 || need > maxSum) continue;
            if (rightPos[k - cntL][need]) {
                /* clean up */
                for (int i = 0; i <= n2; ++i) free(rightPos[i]);
                free(rightPos);
                free(leftSum);
                free(leftCnt);
                return true;
            }
        }
    }

    for (int i = 0; i <= n2; ++i) free(rightPos[i]);
    free(rightPos);
    free(leftSum);
    free(leftCnt);
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool SplitArraySameAverage(int[] nums) {
        int n = nums.Length;
        if (n == 1) return false;
        int total = 0;
        foreach (int x in nums) total += x;

        // dp[size] = set of achievable sums with that many elements
        var dp = new List<HashSet<int>>(n + 1);
        for (int i = 0; i <= n; i++) dp.Add(new HashSet<int>());
        dp[0].Add(0);

        for (int idx = 0; idx < n; idx++) {
            int num = nums[idx];
            // iterate sizes descending to avoid using the same element multiple times
            for (int size = Math.Min(idx, n - 1); size >= 0; size--) {
                foreach (int s in dp[size]) {
                    dp[size + 1].Add(s + num);
                }
            }
        }

        // Only need to check subset sizes up to n/2 due to symmetry
        for (int k = 1; k <= n / 2; k++) {
            if ((long)total * k % n != 0) continue;
            int target = (int)((long)total * k / n);
            if (dp[k].Contains(target)) return true;
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var splitArraySameAverage = function(nums) {
    const n = nums.length;
    if (n < 2) return false;
    const total = nums.reduce((a, b) => a + b, 0);
    const maxK = Math.floor(n / 2);

    // dp[k] stores all possible sums using exactly k elements
    const dp = Array.from({ length: n + 1 }, () => new Set());
    dp[0].add(0);

    for (const num of nums) {
        // iterate sizes in reverse to avoid reuse within same iteration
        for (let k = n - 1; k >= 0; --k) {
            if (dp[k].size === 0) continue;
            const nextSet = dp[k + 1];
            for (const s of dp[k]) {
                nextSet.add(s + num);
            }
        }
    }

    for (let k = 1; k <= maxK; ++k) {
        if ((total * k) % n !== 0) continue;
        const target = (total * k) / n;
        if (dp[k].has(target)) return true;
    }
    return false;
};
```

## Typescript

```typescript
function splitArraySameAverage(nums: number[]): boolean {
    const n = nums.length;
    const total = nums.reduce((a, b) => a + b, 0);
    const n1 = Math.floor(n / 2);
    const n2 = n - n1;
    const arr1 = nums.slice(0, n1);
    const arr2 = nums.slice(n1);

    const sumsBySize1: number[][] = Array.from({ length: n1 + 1 }, () => []);
    for (let mask = 0; mask < (1 << n1); ++mask) {
        let sum = 0, cnt = 0;
        for (let i = 0; i < n1; ++i) {
            if ((mask >> i) & 1) {
                sum += arr1[i];
                ++cnt;
            }
        }
        sumsBySize1[cnt].push(sum);
    }

    const sumsSetBySize2: Set<number>[] = Array.from({ length: n2 + 1 }, () => new Set());
    for (let mask = 0; mask < (1 << n2); ++mask) {
        let sum = 0, cnt = 0;
        for (let i = 0; i < n2; ++i) {
            if ((mask >> i) & 1) {
                sum += arr2[i];
                ++cnt;
            }
        }
        sumsSetBySize2[cnt].add(sum);
    }

    for (let k = 1; k <= n - 1; ++k) {
        if ((total * k) % n !== 0) continue;
        const target = (total * k) / n;

        const minI = Math.max(0, k - n2);
        const maxI = Math.min(k, n1);
        for (let i = minI; i <= maxI; ++i) {
            const j = k - i;
            const set2 = sumsSetBySize2[j];
            if (!set2.size) continue;

            for (const s1 of sumsBySize1[i]) {
                if (set2.has(target - s1)) return true;
            }
        }
    }

    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function splitArraySameAverage($nums) {
        $n = count($nums);
        if ($n < 2) return false;
        $total = array_sum($nums);

        // dp[size] => associative set of achievable sums
        $dp = array_fill(0, $n + 1, []);
        $dp[0][0] = true;

        foreach ($nums as $num) {
            for ($size = $n - 1; $size >= 0; $size--) {
                if (empty($dp[$size])) continue;
                foreach ($dp[$size] as $sum => $_) {
                    $newSize = $size + 1;
                    $newSum = $sum + $num;
                    $dp[$newSize][$newSum] = true;
                }
            }
        }

        for ($k = 1; $k < $n; $k++) {
            if (($total * $k) % $n !== 0) continue;
            $target = intdiv($total * $k, $n);
            if (isset($dp[$k][$target])) return true;
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func splitArraySameAverage(_ nums: [Int]) -> Bool {
        let n = nums.count
        if n == 1 { return false }
        let total = nums.reduce(0, +)
        var dp = Array(repeating: Set<Int>(), count: n + 1)
        dp[0].insert(0)

        for num in nums {
            for size in stride(from: n - 1, through: 0, by: -1) {
                if dp[size].isEmpty { continue }
                let newSize = size + 1
                for sum in dp[size] {
                    dp[newSize].insert(sum + num)
                }
            }
        }

        for k in 1..<n {
            if (total * k) % n != 0 { continue }
            let target = (total * k) / n
            if dp[k].contains(target) {
                return true
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun splitArraySameAverage(nums: IntArray): Boolean {
        val n = nums.size
        val total = nums.sum()
        // dp[size] holds all possible sums using exactly 'size' elements
        val dp = Array(n + 1) { HashSet<Int>() }
        dp[0].add(0)
        for (num in nums) {
            for (size in n - 1 downTo 0) {
                if (dp[size].isNotEmpty()) {
                    val newSums = ArrayList<Int>(dp[size].size)
                    for (s in dp[size]) {
                        newSums.add(s + num)
                    }
                    dp[size + 1].addAll(newSums)
                }
            }
        }
        for (k in 1 until n) {
            if ((total.toLong() * k) % n != 0L) continue
            val target = ((total.toLong() * k) / n).toInt()
            if (dp[k].contains(target)) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool splitArraySameAverage(List<int> nums) {
    int n = nums.length;
    if (n == 1) return false;
    int totalSum = nums.reduce((a, b) => a + b);

    // valid subset sizes and their required sums
    List<int> ks = [];
    Map<int, int> targetForK = {};
    for (int k = 1; k < n; ++k) {
      if ((totalSum * k) % n == 0) {
        ks.add(k);
        targetForK[k] = (totalSum * k) ~/ n;
      }
    }
    if (ks.isEmpty) return false;

    int m = n ~/ 2;
    List<int> left = nums.sublist(0, m);
    List<int> right = nums.sublist(m);

    // map: subset size -> set of possible sums for the left half
    Map<int, Set<int>> leftMap = {0: {0}};
    int leftSize = left.length;
    int totalLeftMask = 1 << leftSize;
    for (int mask = 1; mask < totalLeftMask; ++mask) {
      int cnt = 0;
      int sum = 0;
      for (int i = 0; i < leftSize; ++i) {
        if ((mask >> i & 1) == 1) {
          cnt++;
          sum += left[i];
        }
      }
      leftMap.putIfAbsent(cnt, () => <int>{}).add(sum);
    }

    int rightSize = right.length;
    int totalRightMask = 1 << rightSize;
    for (int mask = 0; mask < totalRightMask; ++mask) {
      int cntR = 0;
      int sumR = 0;
      for (int i = 0; i < rightSize; ++i) {
        if ((mask >> i & 1) == 1) {
          cntR++;
          sumR += right[i];
        }
      }

      for (int k in ks) {
        int needCntLeft = k - cntR;
        if (needCntLeft < 0 || needCntLeft > leftSize) continue;
        int target = targetForK[k]!;
        int neededSumLeft = target - sumR;
        Set<int>? sumsSet = leftMap[needCntLeft];
        if (sumsSet != null && sumsSet.contains(neededSumLeft)) {
          return true;
        }
      }
    }

    return false;
  }
}
```

## Golang

```go
package main

import (
	"math/bits"
)

func splitArraySameAverage(nums []int) bool {
	n := len(nums)
	if n < 2 {
		return false
	}
	total := 0
	for _, v := range nums {
		total += v
	}

	// quick feasibility check
	feasible := false
	for k := 1; k < n; k++ {
		if (total*k)%n == 0 {
			feasible = true
			break
		}
	}
	if !feasible {
		return false
	}

	mid := n / 2
	first := nums[:mid]
	second := nums[mid:]
	n1, n2 := len(first), len(second)

	// subsets of first half: store sums per size
	firstSums := make([][]int, n1+1)
	for mask := 0; mask < (1 << n1); mask++ {
		sz := bits.OnesCount(uint(mask))
		sum := 0
		for i := 0; i < n1; i++ {
			if (mask>>i)&1 == 1 {
				sum += first[i]
			}
		}
		firstSums[sz] = append(firstSums[sz], sum)
	}

	// subsets of second half: store sums per size in a set for O(1) lookup
	secondSet := make([]map[int]struct{}, n2+1)
	for i := 0; i <= n2; i++ {
		secondSet[i] = make(map[int]struct{})
	}
	for mask := 0; mask < (1 << n2); mask++ {
		sz := bits.OnesCount(uint(mask))
		sum := 0
		for i := 0; i < n2; i++ {
			if (mask>>i)&1 == 1 {
				sum += second[i]
			}
		}
		secondSet[sz][sum] = struct{}{}
	}

	// try each possible subset size k
	for k := 1; k < n; k++ {
		if (total*k)%n != 0 {
			continue
		}
		target := (total * k) / n

		minI := max(0, k-n2)
		maxI := min(k, n1)
		for i := minI; i <= maxI; i++ {
			j := k - i
			for _, s := range firstSums[i] {
				if _, ok := secondSet[j][target-s]; ok {
					return true
				}
			}
		}
	}

	return false
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
```

## Ruby

```ruby
require 'set'

def split_array_same_average(nums)
  n = nums.size
  return false if n < 2

  total = nums.sum
  dp = Array.new(n + 1) { Set.new }
  dp[0] << 0

  nums.each do |num|
    (n - 1).downto(0) do |size|
      next if dp[size].empty?
      dp[size + 1].merge(dp[size].map { |s| s + num })
    end
  end

  (1...n).each do |k|
    next unless total * k % n == 0
    target = total * k / n
    return true if dp[k].include?(target)
  end
  false
end
```

## Scala

```scala
object Solution {
  def splitArraySameAverage(nums: Array[Int]): Boolean = {
    val n = nums.length
    val total = nums.sum
    // dp[k][s] indicates whether we can pick k elements with sum s
    val dp = Array.ofDim[Boolean](n + 1, total + 1)
    dp(0)(0) = true

    for (num <- nums) {
      var k = n - 1
      while (k >= 0) {
        val maxS = total - num
        var s = 0
        while (s <= maxS) {
          if (dp(k)(s)) dp(k + 1)(s + num) = true
          s += 1
        }
        k -= 1
      }
    }

    for (k <- 1 until n) {
      if ((total * k) % n == 0) {
        val target = (total * k) / n
        if (dp(k)(target)) return true
      }
    }
    false
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn split_array_same_average(nums: Vec<i32>) -> bool {
        let n = nums.len();
        if n <= 1 {
            return false;
        }
        let total_sum: i64 = nums.iter().map(|&x| x as i64).sum();

        // Split into two halves
        let len_l = n / 2;
        let len_r = n - len_l;
        let left = &nums[0..len_l];
        let right = &nums[len_l..];

        // All subset sums for the left half, grouped by size
        let mut left_sums: Vec<Vec<i64>> = vec![Vec::new(); len_l + 1];
        for mask in 0usize..(1usize << len_l) {
            let mut sum = 0i64;
            let mut cnt = 0usize;
            for i in 0..len_l {
                if (mask >> i) & 1 == 1 {
                    sum += left[i] as i64;
                    cnt += 1;
                }
            }
            left_sums[cnt].push(sum);
        }

        // All subset sums for the right half, stored in hash sets for O(1) lookup
        let mut right_sets: Vec<HashSet<i64>> = vec![HashSet::new(); len_r + 1];
        for mask in 0usize..(1usize << len_r) {
            let mut sum = 0i64;
            let mut cnt = 0usize;
            for i in 0..len_r {
                if (mask >> i) & 1 == 1 {
                    sum += right[i] as i64;
                    cnt += 1;
                }
            }
            right_sets[cnt].insert(sum);
        }

        // Try every possible subset size k (excluding empty and whole array)
        for k in 1usize..n {
            if (total_sum * k as i64) % n as i64 != 0 {
                continue;
            }
            let target = (total_sum * k as i64) / n as i64;

            // left part size can range so that right part size is valid
            let min_left = if k > len_r { k - len_r } else { 0 };
            let max_left = std::cmp::min(k, len_l);
            for lsize in min_left..=max_left {
                let rsize = k - lsize;
                for &s in &left_sums[lsize] {
                    let need = target - s;
                    if right_sets[rsize].contains(&need) {
                        return true;
                    }
                }
            }
        }

        false
    }
}
```

## Racket

```racket
(require racket/list)
(require racket/set)

(define/contract (split-array-same-average nums)
  (-> (listof exact-integer?) boolean?)
  (let* ((n (length nums))
         (total (apply + nums)))
    (if (= n 1)
        #false
        (let loop-k ((k 1))
          (cond
            [(> k (- n 1)) #false]
            [else
             (if (= (remainder (* total k) n) 0)
                 (let* ((target (/ (* total k) n)))
                   (define dp (make-vector (+ n 1) (set))) ; dp[0] = {0}
                   (vector-set! dp 0 (set 0))
                   (for ([x nums])
                     (for ([size (in-range (- n 1) -1 -1)])
                       (let ((prev-set (vector-ref dp size)))
                         (when (not (set-empty? prev-set))
                           (define new-sums (set-map (lambda (s) (+ s x)) prev-set))
                           (vector-set! dp (+ size 1)
                                        (set-union (vector-ref dp (+ size 1)) new-sums))))))
                   (if (set-member? (vector-ref dp k) target)
                       #true
                       (loop-k (+ k 1)))))
                 (loop-k (+ k 1)))))))))
```

## Erlang

```erlang
-spec split_array_same_average(Nums :: [integer()]) -> boolean().
split_array_same_average(Nums) ->
    N = length(Nums),
    case N of
        1 -> false;
        _ ->
            Total = lists:sum(Nums),
            Len1 = N div 2,
            FirstHalf = lists:sublist(Nums, 1, Len1),
            SecondHalf = lists:nthtail(Len1, Nums),
            Map1 = build_map(FirstHalf),
            Map2 = build_map(SecondHalf),
            Len2 = N - Len1,
            check_k(N, Total, Map1, Map2, Len1, Len2)
    end.

build_map(List) ->
    InitialMap = #{0 => sets:add_element(0, sets:new())},
    lists:foldl(fun(X, Map) ->
        OldMap = Map,
        maps:fold(fun(Size, SumSet, NewMap) ->
            NewSize = Size + 1,
            ShiftedSet = sets:fold(
                fun(Sum, Acc) -> sets:add_element(Sum + X, Acc) end,
                sets:new(),
                SumSet),
            case maps:get(NewSize, NewMap, undefined) of
                undefined -> maps:put(NewSize, ShiftedSet, NewMap);
                ExistingSet -> maps:put(NewSize, sets:union(ExistingSet, ShiftedSet), NewMap)
            end
        end, Map, OldMap)
    end, InitialMap, List).

check_k(N, Total, Map1, Map2, Len1, Len2) ->
    lists:any(fun(K) ->
        case (Total * K) rem N of
            0 ->
                Target = (Total * K) div N,
                MinI = erlang:max(0, K - Len2),
                MaxI = erlang:min(K, Len1),
                exists_split(K, Target, Map1, Map2, MinI, MaxI);
            _ -> false
        end
    end, lists:seq(1, N-1)).

exists_split(_K, _Target, _Map1, _Map2, I, MaxI) when I > MaxI ->
    false;
exists_split(K, Target, Map1, Map2, I, MaxI) ->
    case maps:get(I, Map1, undefined) of
        undefined ->
            exists_split(K, Target, Map1, Map2, I+1, MaxI);
        Set1 ->
            case maps:get(K - I, Map2, undefined) of
                undefined ->
                    exists_split(K, Target, Map1, Map2, I+1, MaxI);
                Set2 ->
                    Found = sets:fold(
                        fun(Sum1, Acc) ->
                            if Acc -> true;
                               true ->
                                   Complement = Target - Sum1,
                                   sets:is_element(Complement, Set2)
                            end
                        end,
                        false,
                        Set1),
                    case Found of
                        true -> true;
                        false -> exists_split(K, Target, Map1, Map2, I+1, MaxI)
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec split_array_same_average(nums :: [integer]) :: boolean
  def split_array_same_average(nums) do
    n = length(nums)
    total = Enum.sum(nums)

    # Find subset sizes k where the required sum is integer
    possible_ks =
      for k <- 1..(n - 1), rem(total * k, n) == 0, do: k

    if possible_ks == [] do
      false
    else
      # dp[size] = MapSet of achievable sums with that size
      initial_dp = %{0 => MapSet.new([0])}

      final_dp =
        Enum.reduce(nums, initial_dp, fn num, dp ->
          sizes_desc = Enum.sort(Map.keys(dp), &>=/2)

          Enum.reduce(sizes_desc, dp, fn size, acc ->
            sums = Map.get(acc, size)
            new_sums = Enum.map(sums, &(&1 + num))

            updated_set =
              new_sums
              |> Enum.reduce(Map.get(acc, size + 1, MapSet.new()), fn s, set ->
                MapSet.put(set, s)
              end)

            Map.put(acc, size + 1, updated_set)
          end)
        end)

      Enum.any?(possible_ks, fn k ->
        target = div(total * k, n)

        case Map.get(final_dp, k) do
          nil -> false
          set -> MapSet.member?(set, target)
        end
      end)
    end
  end
end
```
