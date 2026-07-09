# 2354. Number of Excellent Pairs

## Cpp

```cpp
class Solution {
public:
    long long countExcellentPairs(vector<int>& nums, int k) {
        unordered_set<int> uniq(nums.begin(), nums.end());
        const int MAX_BITS = 60;
        vector<long long> cnt(MAX_BITS + 1, 0);
        for (int x : uniq) {
            int bits = __builtin_popcountll((long long)x);
            cnt[bits]++;
        }
        long long ans = 0;
        for (int i = 0; i <= MAX_BITS; ++i) {
            if (cnt[i] == 0) continue;
            for (int j = 0; j <= MAX_BITS; ++j) {
                if (i + j >= k) {
                    ans += cnt[i] * cnt[j];
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long countExcellentPairs(int[] nums, int k) {
        java.util.HashSet<Integer> set = new java.util.HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        // maximum possible popcount for given constraints is 31, but we allocate up to 60 for safety
        long[] freq = new long[61];
        for (int num : set) {
            int pc = Integer.bitCount(num);
            freq[pc]++;
        }
        long[] suffix = new long[62]; // extra slot for easier handling
        for (int i = 60; i >= 0; i--) {
            suffix[i] = suffix[i + 1] + freq[i];
        }
        long ans = 0;
        for (int p = 0; p <= 60; p++) {
            if (freq[p] == 0) continue;
            int need = k - p;
            if (need < 0) need = 0;
            if (need > 60) continue; // no q can satisfy
            ans += freq[p] * suffix[need];
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countExcellentPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        uniq = set(nums)
        cnt = [0] * 61  # popcount can be at most 60 for given constraints
        for v in uniq:
            bits = v.bit_count() if hasattr(v, "bit_count") else bin(v).count("1")
            cnt[bits] += 1

        suff = [0] * 62
        for i in range(60, -1, -1):
            suff[i] = suff[i + 1] + cnt[i]

        total = 0
        for i in range(61):
            if cnt[i] == 0:
                continue
            need = k - i
            if need < 0:
                need = 0
            total += cnt[i] * suff[need]
        return total
```

## Python3

```python
from bisect import bisect_left
from typing import List

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        uniq = set(nums)
        popcounts = [x.bit_count() for x in uniq]
        popcounts.sort()
        n = len(popcounts)
        ans = 0
        for c in popcounts:
            need = k - c
            idx = bisect_left(popcounts, need) if need > 0 else 0
            ans += n - idx
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

long long countExcellentPairs(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;
    int *arr = (int *)malloc(numsSize * sizeof(int));
    memcpy(arr, nums, numsSize * sizeof(int));
    qsort(arr, numsSize, sizeof(int), cmp_int);

    long long cnt[61] = {0};
    for (int i = 0; i < numsSize; ) {
        int val = arr[i];
        // skip duplicates
        while (i < numsSize && arr[i] == val) i++;
        int pc = __builtin_popcount((unsigned)val);
        cnt[pc]++;
    }
    free(arr);

    long long ans = 0;
    for (int i = 0; i <= 60; ++i) {
        if (cnt[i] == 0) continue;
        for (int j = 0; j <= 60; ++j) {
            if (cnt[j] == 0) continue;
            if (i + j >= k) {
                ans += cnt[i] * cnt[j];
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Numerics;

public class Solution {
    public long CountExcellentPairs(int[] nums, int k) {
        var set = new HashSet<int>(nums);
        var bits = new List<int>();
        foreach (var v in set) {
            bits.Add((int)BitOperations.PopCount((uint)v));
        }
        bits.Sort();
        int n = bits.Count;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int need = k - bits[i];
            if (need <= 0) {
                ans += n;
            } else {
                int idx = LowerBound(bits, need);
                ans += n - idx;
            }
        }
        return ans;
    }

    private int LowerBound(List<int> list, int target) {
        int left = 0, right = list.Count; // [left, right)
        while (left < right) {
            int mid = left + ((right - left) >> 1);
            if (list[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countExcellentPairs = function(nums, k) {
    const uniq = Array.from(new Set(nums));
    const popcnt = (x) => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    };
    const bits = uniq.map(popcnt);
    bits.sort((a, b) => a - b);
    const n = bits.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const need = k - bits[i];
        // binary search lower bound of need
        let l = 0, r = n;
        while (l < r) {
            const m = (l + r) >> 1;
            if (bits[m] < need) l = m + 1;
            else r = m;
        }
        ans += n - l;
    }
    return ans;
};
```

## Typescript

```typescript
function countExcellentPairs(nums: number[], k: number): number {
    const unique = new Set<number>();
    for (const v of nums) unique.add(v);

    const popCounts: number[] = [];
    for (const v of unique) {
        let x = v;
        let cnt = 0;
        while (x) {
            cnt += x & 1;
            x >>>= 1;
        }
        popCounts.push(cnt);
    }

    popCounts.sort((a, b) => a - b);
    const m = popCounts.length;
    let ans = 0;

    for (let i = 0; i < m; ++i) {
        const need = k - popCounts[i];
        // lower bound for need
        let l = 0, r = m;
        while (l < r) {
            const mid = (l + r) >> 1;
            if (popCounts[mid] >= need) r = mid;
            else l = mid + 1;
        }
        ans += m - l;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function countExcellentPairs($nums, $k) {
        // Remove duplicates
        $unique = array_values(array_unique($nums));
        $bits = [];
        foreach ($unique as $num) {
            $cnt = 0;
            while ($num > 0) {
                $cnt += $num & 1;
                $num >>= 1;
            }
            $bits[] = $cnt;
        }

        sort($bits, SORT_NUMERIC);
        $n = count($bits);
        $total = 0;

        for ($i = 0; $i < $n; ++$i) {
            $need = $k - $bits[$i];
            if ($need <= 0) {
                $total += $n;
                continue;
            }
            // binary search lower bound for $need
            $left = 0;
            $right = $n;
            while ($left < $right) {
                $mid = intdiv($left + $right, 2);
                if ($bits[$mid] < $need) {
                    $left = $mid + 1;
                } else {
                    $right = $mid;
                }
            }
            $idx = $left; // first index with bits[idx] >= need
            $total += $n - $idx;
        }

        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func countExcellentPairs(_ nums: [Int], _ k: Int) -> Int {
        var unique = Set<Int>()
        for num in nums { unique.insert(num) }
        var bits = [Int]()
        bits.reserveCapacity(unique.count)
        for num in unique {
            bits.append(popcnt(num))
        }
        bits.sort()
        let m = bits.count
        var result: Int64 = 0
        for i in 0..<m {
            let need = k - bits[i]
            var idx: Int
            if need <= 0 {
                idx = 0
            } else {
                var l = 0, r = m
                while l < r {
                    let mid = (l + r) >> 1
                    if bits[mid] >= need {
                        r = mid
                    } else {
                        l = mid + 1
                    }
                }
                idx = l
            }
            result += Int64(m - idx)
        }
        return Int(result)
    }

    private func popcnt(_ x: Int) -> Int {
        var v = x
        var cnt = 0
        while v != 0 {
            cnt += 1
            v &= v - 1
        }
        return cnt
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countExcellentPairs(nums: IntArray, k: Int): Long {
        val unique = HashSet<Int>()
        for (num in nums) unique.add(num)

        val popCounts = IntArray(unique.size)
        var idx = 0
        for (num in unique) {
            popCounts[idx++] = Integer.bitCount(num)
        }
        java.util.Arrays.sort(popCounts)

        val n = popCounts.size
        var result = 0L

        for (i in 0 until n) {
            val need = k - popCounts[i]
            // binary search first index with value >= need
            var lo = 0
            var hi = n
            while (lo < hi) {
                val mid = (lo + hi) ushr 1
                if (popCounts[mid] >= need) {
                    hi = mid
                } else {
                    lo = mid + 1
                }
            }
            val cnt = n - lo
            result += cnt.toLong()
        }

        return result
    }
}
```

## Dart

```dart
class Solution {
  int countExcellentPairs(List<int> nums, int k) {
    // Deduplicate numbers because pairs are defined by values.
    final Set<int> uniqueNums = nums.toSet();
    final List<int> popList = [];
    for (final num in uniqueNums) {
      popList.add(_popCount(num));
    }
    popList.sort();
    final int m = popList.length;
    int total = 0;

    for (int p in popList) {
      int need = k - p;
      if (need <= 0) {
        total += m; // all numbers satisfy
      } else {
        int idx = _lowerBound(popList, need);
        total += m - idx;
      }
    }

    return total;
  }

  int _popCount(int x) {
    int cnt = 0;
    while (x > 0) {
      cnt += x & 1;
      x >>= 1;
    }
    return cnt;
  }

  int _lowerBound(List<int> arr, int target) {
    int left = 0, right = arr.length;
    while (left < right) {
      int mid = (left + right) >> 1;
      if (arr[mid] < target) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return left;
  }
}
```

## Golang

```go
import "math/bits"

func countExcellentPairs(nums []int, k int) int64 {
	uniq := make(map[int]struct{})
	for _, v := range nums {
		uniq[v] = struct{}{}
	}
	cnt := make([]int64, 61)
	for v := range uniq {
		pc := bits.OnesCount(uint(v))
		cnt[pc]++
	}
	suff := make([]int64, 62)
	for i := 60; i >= 0; i-- {
		suff[i] = suff[i+1] + cnt[i]
	}
	var ans int64
	for p := 0; p <= 60; p++ {
		if cnt[p] == 0 {
			continue
		}
		need := k - p
		if need < 0 {
			need = 0
		}
		if need > 60 {
			continue
		}
		ans += cnt[p] * suff[need]
	}
	return ans
}
```

## Ruby

```ruby
def count_excellent_pairs(nums, k)
  # Remove duplicate numbers because multiplicity does not affect the count
  uniq_nums = nums.uniq

  # Compute popcount for each unique number
  pcs = []
  uniq_nums.each do |x|
    cnt = 0
    while x > 0
      cnt += 1
      x &= x - 1
    end
    pcs << cnt
  end

  pcs.sort!
  n = pcs.length
  total = 0

  pcs.each do |p|
    need = k - p
    if need <= 0
      idx = 0
    else
      # binary search for first index with value >= need
      left = 0
      right = n
      while left < right
        mid = (left + right) / 2
        if pcs[mid] < need
          left = mid + 1
        else
          right = mid
        end
      end
      idx = left
    end
    total += n - idx
  end

  total
end
```

## Scala

```scala
object Solution {
    def countExcellentPairs(nums: Array[Int], k: Int): Long = {
        val unique = nums.toSet
        val freq = new Array[Long](61)
        for (num <- unique) {
            val bits = Integer.bitCount(num)
            freq(bits) += 1L
        }
        var ans: Long = 0L
        if (k <= 60) {
            for (i <- 0 to 60) {
                val fi = freq(i)
                if (fi > 0) {
                    for (j <- 0 to 60) {
                        if (i + j >= k) {
                            ans += fi * freq(j)
                        }
                    }
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
    pub fn count_excellent_pairs(nums: Vec<i32>, k: i32) -> i64 {
        use std::collections::HashSet;
        let mut uniq = HashSet::new();
        for &v in &nums {
            uniq.insert(v);
        }
        // popcount can be at most 30 for nums <= 1e9
        const MAX_BITS: usize = 31; // indices 0..30
        let mut cnt = vec![0i64; MAX_BITS];
        for &v in uniq.iter() {
            let bits = (v as u32).count_ones() as usize;
            cnt[bits] += 1;
        }
        let k_usize = if k < 0 { 0 } else { k as usize };
        let mut ans: i64 = 0;
        for b1 in 0..MAX_BITS {
            if cnt[b1] == 0 {
                continue;
            }
            for b2 in 0..MAX_BITS {
                if cnt[b2] == 0 {
                    continue;
                }
                if b1 + b2 >= k_usize {
                    ans += cnt[b1] * cnt[b2];
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(require racket/bitwise)

(define (popcnt x)
  (bitwise-bit-count x))

(define/contract (count-excellent-pairs nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((seen (make-hash))
         (unique '()))
    (for ([n nums])
      (unless (hash-has-key? seen n)
        (hash-set! seen n #t)
        (set! unique (cons n unique))))
    (define max-bits 60)
    (define cnt (make-vector (+ max-bits 1) 0))
    (for ([x unique])
      (let ((b (popcnt x)))
        (vector-set! cnt b (+ (vector-ref cnt b) 1))))
    (define ans 0)
    (for ([i (in-range (add1 max-bits))])
      (define ci (vector-ref cnt i))
      (when (> ci 0)
        (for ([j (in-range (add1 max-bits))])
          (when (>= (+ i j) k)
            (set! ans (+ ans (* ci (vector-ref cnt j))))))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([count_excellent_pairs/2]).

-spec count_excellent_pairs(Nums :: [integer()], K :: integer()) -> integer().
count_excellent_pairs(Nums, K) ->
    Unique = lists:usort(Nums),
    CountsMap = build_counts(Unique, #{}),
    MaxBits = 30,
    compute_answer(CountsMap, K, MaxBits).

build_counts([], Acc) -> Acc;
build_counts([H|T], Acc) ->
    Bits = popcnt(H),
    NewAcc = maps:update_with(Bits, fun(V) -> V + 1 end, 1, Acc),
    build_counts(T, NewAcc).

popcnt(N) when N >= 0 -> popcnt(N, 0).
popcnt(0, Acc) -> Acc;
popcnt(N, Acc) ->
    popcnt(N bsr 1, Acc + (N band 1)).

compute_answer(CountsMap, K, MaxBits) ->
    Counts = [maps:get(I, CountsMap, 0) || I <- lists:seq(0, MaxBits)],
    Indices = lists:seq(0, MaxBits),
    lists:foldl(fun({I, Ci}, AccI) ->
        SumJ = lists:foldl(fun({J, Cj}, AccJ) ->
                case I + J >= K of
                    true -> AccJ + Ci * Cj;
                    false -> AccJ
                end
            end, 0, lists:zip(Indices, Counts)),
        AccI + SumJ
    end, 0, lists:zip(Indices, Counts)).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec count_excellent_pairs(nums :: [integer], k :: integer) :: integer
  def count_excellent_pairs(nums, k) do
    unique = MapSet.new(nums)

    freq =
      Enum.reduce(unique, %{}, fn num, acc ->
        bits = popcnt(num)
        Map.update(acc, bits, 1, &(&1 + 1))
      end)

    pairs = Enum.to_list(freq)

    Enum.reduce(pairs, 0, fn {i, ci}, acc1 ->
      inner =
        Enum.reduce(pairs, 0, fn {j, cj}, acc2 ->
          if i + j >= k do
            acc2 + ci * cj
          else
            acc2
          end
        end)

      acc1 + inner
    end)
  end

  defp popcnt(0), do: 0
  defp popcnt(n) when is_integer(n) and n > 0 do
    do_popcnt(n, 0)
  end

  defp do_popcnt(0, acc), do: acc
  defp do_popcnt(n, acc) do
    do_popcnt(n >>> 1, acc + (n &&& 1))
  end
end
```
