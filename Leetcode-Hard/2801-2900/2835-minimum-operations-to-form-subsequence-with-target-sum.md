# 2835. Minimum Operations to Form Subsequence With Target Sum

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int target) {
        long long total = 0;
        for (int v : nums) total += v;
        if (total < target) return -1;

        const int MAXB = 31; // up to 2^30
        vector<long long> cnt(MAXB, 0);
        for (int v : nums) {
            int b = __builtin_ctz(v); // since v is power of two
            cnt[b]++;
        }

        int ops = 0;
        for (int bit = 0; bit < MAXB; ++bit) {
            if ((target >> bit) & 1) {
                if (cnt[bit] > 0) {
                    cnt[bit]--;
                } else {
                    int j = bit + 1;
                    while (j < MAXB && cnt[j] == 0) ++j;
                    if (j == MAXB) return -1; // should not happen given total >= target
                    while (j > bit) {
                        cnt[j]--;
                        cnt[j - 1] += 2;
                        ++ops;
                        --j;
                    }
                    cnt[bit]--; // use one after splitting
                }
            }
            if (bit + 1 < MAXB) {
                cnt[bit + 1] += cnt[bit] / 2;
            }
        }
        return ops;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(java.util.List<Integer> nums, int target) {
        long total = 0;
        int[] cnt = new int[31];
        for (int v : nums) {
            total += v;
            int exp = Integer.numberOfTrailingZeros(v);
            cnt[exp]++;
        }
        if (total < target) return -1;

        int ops = 0;
        for (int i = 0; i < 31; i++) {
            if (((target >> i) & 1) == 1) {
                if (cnt[i] > 0) {
                    cnt[i]--;
                } else {
                    int j = i + 1;
                    while (j < 31 && cnt[j] == 0) j++;
                    // split down from level j to i
                    while (j > i) {
                        cnt[j]--;
                        cnt[j - 1] += 2;
                        ops++;
                        j--;
                    }
                    cnt[i]--; // use one piece of size 2^i
                }
            }
            if (i < 30) {
                cnt[i + 1] += cnt[i] / 2;
            }
        }
        return ops;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        MAX_BIT = 31  # up to 2^30
        cnt = [0] * MAX_BIT
        total = 0
        for x in nums:
            b = x.bit_length() - 1
            cnt[b] += 1
            total += x
        if total < target:
            return -1

        ops = 0
        for i in range(MAX_BIT):
            need = (target >> i) & 1
            if need:
                if cnt[i] == 0:
                    j = i + 1
                    while j < MAX_BIT and cnt[j] == 0:
                        j += 1
                    # split down from j to i
                    while j > i:
                        cnt[j] -= 1
                        cnt[j - 1] += 2
                        ops += 1
                        j -= 1
                cnt[i] -= 1  # use one element of value 2^i
            if i + 1 < MAX_BIT:
                cnt[i + 1] += cnt[i] // 2  # pair up leftovers for higher bits
        return ops
```

## Python3

```python
from typing import List

class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        MAX_BIT = 31  # enough for values up to 2^30 and target < 2^31
        cnt = [0] * (MAX_BIT + 1)
        for x in nums:
            b = x.bit_length() - 1
            cnt[b] += 1

        ops = 0
        for i in range(MAX_BIT):
            if (target >> i) & 1:
                if cnt[i]:
                    cnt[i] -= 1
                else:
                    j = i + 1
                    while j < MAX_BIT and cnt[j] == 0:
                        j += 1
                    if j == MAX_BIT:
                        return -1
                    while j > i:
                        cnt[j] -= 1
                        cnt[j - 1] += 2
                        ops += 1
                        j -= 1
                    cnt[i] -= 1  # use one of the newly created pieces
            cnt[i + 1] += cnt[i] // 2
        return ops
```

## C

```c
int minOperations(int* nums, int numsSize, int target) {
    long long cnt[31] = {0};
    long long total = 0;
    for (int i = 0; i < numsSize; ++i) {
        total += nums[i];
        int exp = __builtin_ctz((unsigned int)nums[i]);
        cnt[exp]++;
    }
    if (total < target) return -1;

    int ops = 0;
    for (int bit = 0; bit <= 30; ++bit) {
        if ((target >> bit) & 1) {
            int j = bit;
            while (j <= 30 && cnt[j] == 0) ++j;
            // split down from j to bit
            while (j > bit) {
                cnt[j]--;
                cnt[j - 1] += 2;
                ++ops;
                --j;
            }
            cnt[bit]--; // use one piece of size 2^bit
        }
        if (bit < 30) {
            cnt[bit + 1] += cnt[bit] / 2; // combine pairs for higher bits
        }
    }
    return ops;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Numerics;

public class Solution {
    public int MinOperations(IList<int> nums, int target) {
        long total = 0;
        foreach (int v in nums) total += v;
        if (total < target) return -1;

        int[] cnt = new int[32];
        foreach (int v in nums) {
            int idx = BitOperations.TrailingZeroCount((uint)v);
            cnt[idx]++;
        }

        int operations = 0;
        long need = 0; // number of pieces of size 2^i still required

        for (int i = 0; i < 31; i++) {
            if (((target >> i) & 1) == 1) need++;

            long have = cnt[i];
            if (have >= need) {
                long surplus = have - need;
                need = 0;
                cnt[i + 1] += (int)(surplus / 2);
            } else {
                // not enough pieces at this level
                need -= have;

                // find the next higher power with available piece
                int j = i + 1;
                while (j < 32 && cnt[j] == 0) j++;
                if (j == 32) return -1; // should not happen due to total check

                operations += (j - i);
                cnt[j]--;
                for (int k = j - 1; k >= i; k--) {
                    cnt[k]++;
                }
                i--; // reprocess this bit after splitting
            }
        }

        return operations;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var minOperations = function(nums, target) {
    const MAX_BIT = 31; // handle up to 2^30, plus one extra for carries
    const cnt = new Array(MAX_BIT + 1).fill(0);
    let total = 0;
    for (let num of nums) {
        total += num;
        const p = Math.floor(Math.log2(num));
        cnt[p]++;
    }
    if (total < target) return -1;

    let ops = 0;
    for (let i = 0; i < MAX_BIT; i++) {
        // need this bit in target?
        if ((target >> i) & 1) {
            if (cnt[i] > 0) {
                cnt[i]--;
            } else {
                // find a higher power to split
                let j = i + 1;
                while (j <= MAX_BIT && cnt[j] === 0) j++;
                if (j > MAX_BIT) return -1; // impossible

                for (; j > i; j--) {
                    cnt[j]--;
                    cnt[j - 1] += 2;
                    ops++;
                }
                cnt[i]--; // use one after splitting
            }
        }
        // combine pairs of current size into next higher size without extra cost
        cnt[i + 1] += Math.floor(cnt[i] / 2);
    }
    return ops;
};
```

## Typescript

```typescript
function minOperations(nums: number[], target: number): number {
    const MAX = 31;
    const cnt = new Array(MAX).fill(0);
    let total = 0;
    for (const x of nums) {
        // x is a power of two, find its exponent
        let b = 0;
        let v = x;
        while (v > 1) {
            v >>= 1;
            b++;
        }
        cnt[b]++;
        total += x;
    }
    if (total < target) return -1;

    let ops = 0;
    let have = 0; // available pieces at current bit level
    for (let i = 0; i < MAX; i++) {
        have += cnt[i];
        if ((target >> i) & 1) {
            if (have > 0) {
                have--; // use one piece to satisfy this bit
            } else {
                // need to split a larger power of two
                let j = i + 1;
                while (j < MAX && cnt[j] === 0) j++;
                // split down from j to i
                while (j > i) {
                    cnt[j]--;
                    cnt[j - 1] += 2;
                    ops++;
                    j--;
                }
                have += 2; // two pieces created at level i
                have--;    // use one for the target bit
            }
        }
        // pair up remaining pieces to form higher bits
        have = Math.floor(have / 2);
    }
    return ops;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function minOperations($nums, $target) {
        $total = 0;
        foreach ($nums as $v) {
            $total += $v;
        }
        if ($total < $target) {
            return -1;
        }

        // count frequencies of each power of two (up to 2^30)
        $cnt = array_fill(0, 31, 0);
        foreach ($nums as $v) {
            // $v is guaranteed to be a power of two
            $bit = (int)log($v, 2);
            $cnt[$bit]++;
        }

        $ops = 0;
        $carry = 0; // available units of size 2^i (including those from lower bits)

        for ($i = 0; $i < 31; $i++) {
            $carry += $cnt[$i];

            if ((($target >> $i) & 1) == 1) { // need one unit of 2^i
                if ($carry > 0) {
                    $carry--; // use it
                } else {
                    // find a larger power to split
                    $j = $i + 1;
                    while ($j < 31 && $cnt[$j] == 0) {
                        $j++;
                    }
                    if ($j == 31) {
                        return -1; // should not happen given total >= target
                    }

                    // split down from j to i
                    while ($j > $i) {
                        $cnt[$j]--;
                        $cnt[$j - 1] += 2;
                        $ops++;
                        $j--;
                    }
                    // after splitting, we have two units of size 2^i
                    $carry += 2; // add the newly created units
                    $carry--;   // use one for the target bit
                }
            }

            // combine pairs of remaining units to form higher powers (free)
            $carry = intdiv($carry, 2);
        }

        return $ops;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int], _ target: Int) -> Int {
        var cnt = Array(repeating: 0, count: 31)
        var total: Int64 = 0
        for num in nums {
            let pos = num.trailingZeroBitCount
            cnt[pos] += 1
            total += Int64(num)
        }
        if total < Int64(target) { return -1 }
        
        var ans = 0
        var carry = 0
        
        for i in 0..<31 {
            cnt[i] += carry
            let need = (target >> i) & 1
            if need == 1 {
                if cnt[i] > 0 {
                    cnt[i] -= 1
                } else {
                    var j = i + 1
                    while j < 31 && cnt[j] == 0 { j += 1 }
                    // split down from j to i
                    while j > i {
                        cnt[j] -= 1
                        ans += 1
                        cnt[j - 1] += 2
                        j -= 1
                    }
                    cnt[i] -= 1
                }
            }
            carry = cnt[i] / 2
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums: List<Int>, target: Int): Int {
        val freq = IntArray(31)
        var total = 0L
        for (v in nums) {
            val exp = Integer.numberOfTrailingZeros(v)
            freq[exp]++
            total += v.toLong()
        }
        if (total < target) return -1

        var ops = 0
        var carry = 0L
        for (i in 0..30) {
            var cnt = freq[i].toLong() + carry
            if ((target shr i) and 1 == 1) {
                if (cnt > 0) {
                    cnt--
                } else {
                    var j = i + 1
                    while (j < 31 && freq[j] == 0) j++
                    if (j == 31) return -1
                    ops += (j - i)
                    freq[j]--
                    for (k in i until j) {
                        freq[k]++
                    }
                    cnt = freq[i].toLong()
                    cnt-- // use one piece after splitting
                }
            }
            carry = cnt / 2
        }
        return ops
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums, int target) {
    int total = 0;
    for (int v in nums) total += v;
    if (total < target) return -1;

    const int MAX_BIT = 31; // up to 2^30
    List<int> freq = List.filled(MAX_BIT, 0);
    for (int v in nums) {
      int bit = _bitPosition(v);
      freq[bit]++;
    }

    int ops = 0;
    for (int i = 0; i < MAX_BIT; ++i) {
      if ((target & (1 << i)) != 0) {
        if (freq[i] > 0) {
          freq[i]--;
        } else {
          int j = i + 1;
          while (j < MAX_BIT && freq[j] == 0) j++;
          // split from j down to i
          while (j > i) {
            freq[j]--;
            freq[j - 1] += 2;
            ops++;
            j--;
          }
          // now we have at least one at bit i
          freq[i]--;
        }
      }
      if (i + 1 < MAX_BIT) {
        freq[i + 1] += freq[i] ~/ 2;
      }
    }
    return ops;
  }

  int _bitPosition(int x) {
    // x is a power of two, returns its exponent
    int pos = 0;
    while ((x >> 1) > 0) {
      x >>= 1;
      pos++;
    }
    return pos;
  }
}
```

## Golang

```go
package main

import (
	"math/bits"
)

func minOperations(nums []int, target int) int {
	const MAX = 31
	cnt := make([]int, MAX)
	var total int64
	for _, v := range nums {
		bit := bits.Len(uint(v)) - 1
		cnt[bit]++
		total += int64(v)
	}
	if total < int64(target) {
		return -1
	}
	ans := 0
	for i := 0; i < MAX; i++ {
		if (target>>i)&1 == 1 {
			if cnt[i] > 0 {
				cnt[i]--
			} else {
				j := i + 1
				for j < MAX && cnt[j] == 0 {
					j++
				}
				if j == MAX {
					return -1
				}
				for j > i {
					cnt[j]--
					cnt[j-1] += 2
					ans++
					j--
				}
				cnt[i]--
			}
		}
		if i+1 < MAX {
			cnt[i+1] += cnt[i] / 2
		}
	}
	return ans
}
```

## Ruby

```ruby
def min_operations(nums, target)
  max_bit = 31
  cnt = Array.new(max_bit, 0)
  total = 0
  nums.each do |x|
    idx = x.bit_length - 1
    cnt[idx] += 1
    total += x
  end
  return -1 if total < target

  ans = 0
  carry = 0
  (0...max_bit).each do |i|
    need = (target >> i) & 1
    available = cnt[i] + carry
    if need == 1
      if available >= 1
        available -= 1
      else
        j = i + 1
        while j < max_bit && cnt[j] == 0
          j += 1
        end
        return -1 if j == max_bit
        while j > i
          cnt[j] -= 1
          ans += 1
          cnt[j - 1] += 2
          j -= 1
        end
        available = cnt[i] + carry - 1
      end
    end
    carry = available / 2
  end
  ans
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: List[Int], target: Int): Int = {
        val MAX = 31
        val cnt = Array.fill[Long](MAX)(0L)
        for (num <- nums) {
            val exp = Integer.numberOfTrailingZeros(num)
            cnt(exp) += 1
        }
        var ans = 0
        var carry: Long = 0
        var t = target
        for (i <- 0 until MAX) {
            carry += cnt(i)
            if ((t & 1) == 1) {
                if (carry > 0) {
                    carry -= 1
                } else {
                    var j = i + 1
                    while (j < MAX && cnt(j) == 0) j += 1
                    if (j == MAX) return -1
                    while (j > i) {
                        cnt(j) -= 1
                        cnt(j - 1) += 2
                        ans += 1
                        j -= 1
                    }
                    // after splitting we have two pieces of size 2^i, use one, leave one
                    carry = 1
                }
            }
            carry /= 2
            t >>= 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>, target: i32) -> i32 {
        const MAX_BITS: usize = 31; // up to 2^30
        let mut cnt = vec![0i64; MAX_BITS];
        let mut total: i64 = 0;
        for v in nums {
            let bit = (v as u32).trailing_zeros() as usize;
            cnt[bit] += 1;
            total += v as i64;
        }
        if total < target as i64 {
            return -1;
        }

        let mut ans: i32 = 0;

        for i in 0..MAX_BITS {
            // need this bit in target?
            if (target >> i) & 1 == 1 {
                if cnt[i] > 0 {
                    cnt[i] -= 1;
                } else {
                    // find next larger power with available count
                    let mut j = i + 1;
                    while j < MAX_BITS && cnt[j] == 0 {
                        j += 1;
                    }
                    // split one element from level j down to i
                    ans += (j - i) as i32;
                    cnt[j] -= 1;
                    let added = 1i64 << (j - i); // number of pieces of size 2^i obtained
                    cnt[i] += added;
                    cnt[i] -= 1; // use one piece for the target bit
                }
            }
            // combine leftover pieces to next level
            if i + 1 < MAX_BITS {
                cnt[i + 1] += cnt[i] / 2;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (min-operations nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([max-bit 60]
         [cnt (make-vector (+ max-bit 2) 0)])
    ;; count occurrences of each power of two
    (for ([num nums])
      (let ([e (- (integer-length num) 1)])
        (vector-set! cnt e (+ (vector-ref cnt e) 1))))
    (define ops 0)
    (define impossible #f)
    (for ([i (in-range (+ max-bit 1))] #:break impossible)
      ;; if target needs this bit
      (when (= (bitwise-and target (arithmetic-shift 1 i)) 1)
        (if (> (vector-ref cnt i) 0)
            (vector-set! cnt i (- (vector-ref cnt i) 1))
            (let loop ((j (+ i 1)))
              (cond [(> j max-bit)
                     (set! impossible #t)]
                    [(> (vector-ref cnt j) 0)
                     ;; split one element from level j down to i
                     (for ([k (in-range j i -1)])
                       (vector-set! cnt k (- (vector-ref cnt k) 1))
                       (vector-set! cnt (- k 1)
                                    (+ (vector-ref cnt (- k 1)) 2))
                       (set! ops (+ ops 1)))
                     ;; use one piece of size i
                     (vector-set! cnt i (- (vector-ref cnt i) 1))]
                    [else (loop (+ j 1))]))))
      ;; combine leftover pairs upward
      (let* ([c (vector-ref cnt i)]
             [pairs (quotient c 2)])
        (when (> pairs 0)
          (vector-set! cnt (+ i 1)
                       (+ (vector-ref cnt (+ i 1)) pairs)))))
    (if impossible -1 ops)))
```

## Erlang

```erlang
-define(MAX_BIT, 30).
-export([min_operations/2]).

min_operations(Nums, Target) ->
    Sum = lists:foldl(fun(X, Acc) -> Acc + X end, 0, Nums),
    if
        Sum < Target -> -1;
        true ->
            Counts0 = build_counts(Nums, #{}),
            process(0, ?MAX_BIT, Target, Counts0, 0)
    end.

build_counts([], M) -> M;
build_counts([H|T], M) ->
    Exp = exp_of_power(H, 0),
    NewM = maps:update_with(
        Exp,
        fun(V) -> V + 1 end,
        1,
        M
    ),
    build_counts(T, NewM).

exp_of_power(1, E) -> E;
exp_of_power(N, E) -> exp_of_power(N bsr 1, E + 1).

process(I, MaxBit, _Target, Counts, Ops) when I > MaxBit ->
    Ops;
process(I, MaxBit, Target, Counts, Ops) ->
    Need = (Target bsr I) band 1,
    {CountsAfterNeed, OpsAfterNeed} =
        if
            Need == 1 ->
                C = maps:get(I, Counts, 0),
                if
                    C > 0 ->
                        {maps:put(I, C - 1, Counts), Ops};
                    true ->
                        case find_next(I + 1, Counts) of
                            none -> {Counts, -1};
                            J when is_integer(J) ->
                                {CountsSplit, AddedOps} = split_down(J, I, Counts),
                                C2 = maps:get(I, CountsSplit, 0),
                                {maps:put(I, C2 - 1, CountsSplit), Ops + AddedOps}
                        end
                end;
            true -> {Counts, Ops}
        end,
    case OpsAfterNeed of
        -1 -> -1;
        _ ->
            Ccur = maps:get(I, CountsAfterNeed, 0),
            Pairs = Ccur div 2,
            Rem = Ccur rem 2,
            TmpCounts = maps:put(I, Rem, CountsAfterNeed),
            NextIdx = I + 1,
            Cnext = maps:get(NextIdx, TmpCounts, 0) + Pairs,
            NewCounts = maps:put(NextIdx, Cnext, TmpCounts),
            process(NextIdx, MaxBit, Target, NewCounts, OpsAfterNeed)
    end.

find_next(Bit, Counts) ->
    find_next(Bit, Counts, ?MAX_BIT).

find_next(Bit, _Counts, Max) when Bit > Max -> none;
find_next(Bit, Counts, Max) ->
    C = maps:get(Bit, Counts, 0),
    if
        C > 0 -> Bit;
        true -> find_next(Bit + 1, Counts, Max)
    end.

split_down(J, I, Counts) when J == I ->
    {Counts, 0};
split_down(J, I, Counts) ->
    Cj = maps:get(J, Counts, 0),
    Counts1 = maps:put(J, Cj - 1, Counts),
    CiMinus = maps:get(J - 1, Counts1, 0),
    Counts2 = maps:put(J - 1, CiMinus + 2, Counts1),
    {Counts3, Ops} = split_down(J - 1, I, Counts2),
    {Counts3, Ops + 1}.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer], target :: integer) :: integer
  def min_operations(nums, target) do
    total = Enum.sum(nums)

    if total < target do
      -1
    else
      max_bit = 30
      # frequency array for bits 0..max_bit+1
      freq =
        List.duplicate(0, max_bit + 2)
        |> Enum.reduce(nums, fn x, acc ->
          idx = trunc(:math.log2(x))
          List.update_at(acc, idx, &(&1 + 1))
        end)

      process(0, max_bit, target, freq, 0)
    end
  end

  defp process(i, max_bit, _target, freq, ans) when i > max_bit do
    ans
  end

  defp process(i, max_bit, target, freq, ans) do
    need = ((target >>> i) &&& 1) == 1

    {freq, ans} =
      if need do
        if Enum.at(freq, i) > 0 do
          freq = List.update_at(freq, i, &(&1 - 1))
          {freq, ans}
        else
          # find the next higher bit with available element
          j = find_next(i + 1, max_bit, freq)

          {freq, ans} =
            Enum.reduce(Enum.to_list(j..(i + 1)) |> Enum.reverse, {freq, ans}, fn k,
                                                                                 {f, a} ->
              f = List.update_at(f, k, &(&1 - 1))
              f = List.update_at(f, k - 1, &(&1 + 2))
              {f, a + 1}
            end)

          freq = List.update_at(freq, i, &(&1 - 1))
          {freq, ans}
        end
      else
        {freq, ans}
      end

    # combine pairs to the next higher bit
    cnt = Enum.at(freq, i)
    add = div(cnt, 2)

    freq =
      if add > 0 do
        freq = List.update_at(freq, i, &(rem(&1, 2)))
        List.update_at(freq, i + 1, &(&1 + add))
      else
        freq
      end

    process(i + 1, max_bit, target, freq, ans)
  end

  defp find_next(start, max_bit, freq) do
    Enum.find(start..max_bit, fn idx -> Enum.at(freq, idx) > 0 end)
  end
end
```
