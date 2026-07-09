# 0992. Subarrays with K Different Integers

## Cpp

```cpp
class Solution {
public:
    long long atMost(const std::vector<int>& nums, int k) {
        if (k <= 0) return 0;
        std::unordered_map<int,int> cnt;
        int left = 0;
        long long res = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            if (cnt[nums[right]]++ == 0) --k;
            while (k < 0) {
                if (--cnt[nums[left]] == 0) ++k;
                ++left;
            }
            res += right - left + 1;
        }
        return res;
    }

    int subarraysWithKDistinct(std::vector<int>& nums, int k) {
        long long ans = atMost(nums, k) - atMost(nums, k - 1);
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }
    
    private int atMost(int[] nums, int k) {
        if (k == 0) return 0;
        java.util.Map<Integer, Integer> freq = new java.util.HashMap<>();
        int left = 0;
        long count = 0;
        for (int right = 0; right < nums.length; ++right) {
            freq.put(nums[right], freq.getOrDefault(nums[right], 0) + 1);
            while (freq.size() > k) {
                int val = nums[left];
                int c = freq.get(val);
                if (c == 1) {
                    freq.remove(val);
                } else {
                    freq.put(val, c - 1);
                }
                left++;
            }
            count += right - left + 1;
        }
        return (int) count;
    }
}
```

## Python

```python
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def at_most(k_limit):
            if k_limit < 0:
                return 0
            count = {}
            left = 0
            res = 0
            distinct = 0
            for right, val in enumerate(nums):
                if count.get(val, 0) == 0:
                    distinct += 1
                count[val] = count.get(val, 0) + 1
                while distinct > k_limit:
                    left_val = nums[left]
                    count[left_val] -= 1
                    if count[left_val] == 0:
                        distinct -= 1
                        del count[left_val]
                    left += 1
                res += right - left + 1
            return res

        return at_most(k) - at_most(k - 1)
```

## Python3

```python
class Solution:
    def subarraysWithKDistinct(self, nums, k):
        from collections import defaultdict

        def at_most(K):
            if K == 0:
                return 0
            count = defaultdict(int)
            left = res = 0
            distinct = 0
            for right, val in enumerate(nums):
                if count[val] == 0:
                    distinct += 1
                count[val] += 1
                while distinct > K:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        distinct -= 1
                    left += 1
                res += right - left + 1
            return res

        return at_most(k) - at_most(k - 1)
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmpInt(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

static long long atMostK(int *comp, int n, int uniq, int K) {
    if (K == 0) return 0LL;
    int *freq = (int *)calloc(uniq, sizeof(int));
    int left = 0, distinct = 0;
    long long total = 0;
    for (int right = 0; right < n; ++right) {
        int idx = comp[right];
        if (freq[idx] == 0) ++distinct;
        ++freq[idx];
        while (distinct > K) {
            int lidx = comp[left];
            --freq[lidx];
            if (freq[lidx] == 0) --distinct;
            ++left;
        }
        total += right - left + 1;
    }
    free(freq);
    return total;
}

int subarraysWithKDistinct(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;

    /* Coordinate compression */
    int *sorted = (int *)malloc(numsSize * sizeof(int));
    memcpy(sorted, nums, numsSize * sizeof(int));
    qsort(sorted, numsSize, sizeof(int), cmpInt);

    int uniq = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (i == 0 || sorted[i] != sorted[i - 1]) {
            sorted[uniq++] = sorted[i];
        }
    }

    int *comp = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        int lo = 0, hi = uniq - 1;
        while (lo <= hi) {
            int mid = (lo + hi) >> 1;
            if (sorted[mid] == nums[i]) {
                comp[i] = mid;
                break;
            } else if (sorted[mid] < nums[i]) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
    }

    long long ans = atMostK(comp, numsSize, uniq, k) -
                    atMostK(comp, numsSize, uniq, k - 1);

    free(sorted);
    free(comp);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int SubarraysWithKDistinct(int[] nums, int k)
    {
        return (int)(AtMost(nums, k) - AtMost(nums, k - 1));
    }

    private long AtMost(int[] nums, int k)
    {
        if (k == 0) return 0;
        var freq = new Dictionary<int, int>();
        int left = 0;
        int distinct = 0;
        long count = 0;

        for (int right = 0; right < nums.Length; right++)
        {
            int val = nums[right];
            if (!freq.ContainsKey(val) || freq[val] == 0)
                distinct++;
            freq[val] = freq.GetValueOrDefault(val) + 1;

            while (distinct > k)
            {
                int leftVal = nums[left];
                freq[leftVal]--;
                if (freq[leftVal] == 0)
                {
                    distinct--;
                    freq.Remove(leftVal);
                }
                left++;
            }

            count += right - left + 1;
        }

        return count;
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
var subarraysWithKDistinct = function(nums, k) {
    const atMost = (limit) => {
        if (limit === 0) return 0;
        const freq = new Map();
        let left = 0;
        let count = 0;
        for (let right = 0; right < nums.length; ++right) {
            const val = nums[right];
            freq.set(val, (freq.get(val) || 0) + 1);
            while (freq.size > limit) {
                const lval = nums[left];
                const cnt = freq.get(lval) - 1;
                if (cnt === 0) {
                    freq.delete(lval);
                } else {
                    freq.set(lval, cnt);
                }
                left++;
            }
            count += right - left + 1;
        }
        return count;
    };
    return atMost(k) - atMost(k - 1);
};
```

## Typescript

```typescript
function subarraysWithKDistinct(nums: number[], k: number): number {
    const atMost = (limit: number): number => {
        if (limit < 0) return 0;
        const freq = new Map<number, number>();
        let left = 0;
        let distinct = 0;
        let total = 0;

        for (let right = 0; right < nums.length; ++right) {
            const valR = nums[right];
            const cntR = (freq.get(valR) ?? 0) + 1;
            freq.set(valR, cntR);
            if (cntR === 1) distinct++;

            while (distinct > limit) {
                const valL = nums[left];
                const cntL = (freq.get(valL) ?? 0) - 1;
                if (cntL === 0) {
                    freq.delete(valL);
                    distinct--;
                } else {
                    freq.set(valL, cntL);
                }
                left++;
            }

            total += right - left + 1;
        }
        return total;
    };

    return atMost(k) - atMost(k - 1);
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
    function subarraysWithKDistinct($nums, $k) {
        return $this->atMost($nums, $k) - $this->atMost($nums, $k - 1);
    }

    private function atMost($nums, $k) {
        if ($k < 0) return 0;
        $freq = [];
        $left = 0;
        $distinct = 0;
        $res = 0;

        foreach ($nums as $right => $val) {
            if (!isset($freq[$val]) || $freq[$val] == 0) {
                $distinct++;
            }
            $freq[$val] = ($freq[$val] ?? 0) + 1;

            while ($distinct > $k) {
                $leftVal = $nums[$left];
                $freq[$leftVal]--;
                if ($freq[$leftVal] == 0) {
                    $distinct--;
                    unset($freq[$leftVal]);
                }
                $left++;
            }

            $res += $right - $left + 1;
        }

        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func subarraysWithKDistinct(_ nums: [Int], _ k: Int) -> Int {
        return atMost(nums, k) - atMost(nums, k - 1)
    }
    
    private func atMost(_ nums: [Int], _ K: Int) -> Int {
        if K < 0 { return 0 }
        var freq = [Int:Int]()
        var left = 0
        var distinct = 0
        var result = 0
        
        for right in 0..<nums.count {
            let val = nums[right]
            if let cnt = freq[val] {
                freq[val] = cnt + 1
            } else {
                freq[val] = 1
                distinct += 1
            }
            
            while distinct > K {
                let lval = nums[left]
                if let cnt = freq[lval] {
                    if cnt == 1 {
                        freq.removeValue(forKey: lval)
                        distinct -= 1
                    } else {
                        freq[lval] = cnt - 1
                    }
                }
                left += 1
            }
            
            result += right - left + 1
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun subarraysWithKDistinct(nums: IntArray, k: Int): Int {
        fun atMost(limit: Int): Long {
            if (limit == 0) return 0L
            val freq = HashMap<Int, Int>()
            var left = 0
            var count = 0L
            for (right in nums.indices) {
                val v = nums[right]
                freq[v] = (freq[v] ?: 0) + 1
                while (freq.size > limit) {
                    val lv = nums[left]
                    val cnt = freq[lv]!! - 1
                    if (cnt == 0) {
                        freq.remove(lv)
                    } else {
                        freq[lv] = cnt
                    }
                    left++
                }
                count += (right - left + 1).toLong()
            }
            return count
        }
        val result = atMost(k) - atMost(k - 1)
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int subarraysWithKDistinct(List<int> nums, int k) {
    return _atMost(nums, k) - _atMost(nums, k - 1);
  }

  int _atMost(List<int> nums, int k) {
    if (k <= 0) return 0;
    final Map<int, int> freq = {};
    int left = 0;
    int distinct = 0;
    int total = 0;

    for (int right = 0; right < nums.length; ++right) {
      int val = nums[right];
      int cnt = (freq[val] ?? 0) + 1;
      freq[val] = cnt;
      if (cnt == 1) distinct++;

      while (distinct > k) {
        int leftVal = nums[left];
        int leftCnt = freq[leftVal]! - 1;
        if (leftCnt == 0) {
          freq.remove(leftVal);
          distinct--;
        } else {
          freq[leftVal] = leftCnt;
        }
        left++;
      }

      total += right - left + 1;
    }

    return total;
  }
}
```

## Golang

```go
func subarraysWithKDistinct(nums []int, k int) int {
	if k == 0 {
		return 0
	}
	atMost := func(limit int) int {
		if limit == 0 {
			return 0
		}
		freq := make(map[int]int)
		left, distinct, count := 0, 0, 0
		for right, v := range nums {
			if freq[v] == 0 {
				distinct++
			}
			freq[v]++
			for distinct > limit {
				x := nums[left]
				freq[x]--
				if freq[x] == 0 {
					delete(freq, x)
					distinct--
				}
				left++
			}
			count += right - left + 1
		}
		return count
	}
	return atMost(k) - atMost(k-1)
}
```

## Ruby

```ruby
def subarrays_with_k_distinct(nums, k)
  at_most = lambda do |limit|
    return 0 if limit <= 0
    count = Hash.new(0)
    left = 0
    distinct = 0
    res = 0
    nums.each_with_index do |num, right|
      count[num] += 1
      distinct += 1 if count[num] == 1
      while distinct > limit
        left_num = nums[left]
        count[left_num] -= 1
        distinct -= 1 if count[left_num] == 0
        left += 1
      end
      res += right - left + 1
    end
    res
  end

  at_most.call(k) - at_most.call(k - 1)
end
```

## Scala

```scala
object Solution {
  def subarraysWithKDistinct(nums: Array[Int], k: Int): Int = {
    def atMost(distinctK: Int): Long = {
      if (distinctK < 0) return 0L
      val freq = scala.collection.mutable.HashMap[Int, Int]()
      var left = 0
      var count: Long = 0
      for (right <- nums.indices) {
        val v = nums(right)
        freq.put(v, freq.getOrElse(v, 0) + 1)
        while (freq.size > distinctK) {
          val lv = nums(left)
          val cnt = freq(lv) - 1
          if (cnt == 0) freq -= lv else freq.update(lv, cnt)
          left += 1
        }
        count += (right - left + 1)
      }
      count
    }

    (atMost(k) - atMost(k - 1)).toInt
  }
}
```

## Rust

```rust
use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn subarrays_with_k_distinct(nums: Vec<i32>, k: i32) -> i32 {
        fn at_most(nums: &Vec<i32>, k: i32) -> i64 {
            if k <= 0 {
                return 0;
            }
            let mut freq: HashMap<i32, i32> = HashMap::new();
            let mut left: usize = 0;
            let mut distinct: i32 = 0;
            let mut total: i64 = 0;

            for right in 0..nums.len() {
                let entry = freq.entry(nums[right]).or_insert(0);
                if *entry == 0 {
                    distinct += 1;
                }
                *entry += 1;

                while distinct > k {
                    let val = nums[left];
                    if let Some(cnt) = freq.get_mut(&val) {
                        *cnt -= 1;
                        if *cnt == 0 {
                            distinct -= 1;
                        }
                    }
                    left += 1;
                }

                total += (right - left + 1) as i64;
            }

            total
        }

        let result = at_most(&nums, k) - at_most(&nums, k - 1);
        result as i32
    }
}
```

## Racket

```racket
(define/contract (subarrays-with-k-distinct nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ([arr (list->vector nums)])
    (define (at-most limit)
      (if (<= limit 0) 0
          (let* ([n (vector-length arr)]
                 [freq (make-hash)]
                 [left 0]
                 [distinct 0]
                 [total 0])
            (for ([right (in-range n)])
              (define val (vector-ref arr right))
              (define cnt (hash-ref freq val 0))
              (when (= cnt 0) (set! distinct (+ distinct 1)))
              (hash-set! freq val (+ cnt 1))
              (while (> distinct limit)
                (define lval (vector-ref arr left))
                (define lcnt (hash-ref freq lval))
                (if (= lcnt 1)
                    (begin
                      (hash-remove! freq lval)
                      (set! distinct (- distinct 1)))
                    (hash-set! freq lval (- lcnt 1)))
                (set! left (+ left 1)))
              (set! total (+ total (+ (- right left) 1))))
            total)))
    (- (at-most k) (at-most (- k 1)))))
```

## Erlang

```erlang
-module(solution).
-export([subarrays_with_k_distinct/2]).

-spec subarrays_with_k_distinct(Nums :: [integer()], K :: integer()) -> integer().
subarrays_with_k_distinct(Nums, K) ->
    Len = length(Nums),
    Tuple = list_to_tuple(Nums),
    AtMostK = at_most(Tuple, Len, K),
    AtMostKm1 = at_most(Tuple, Len, K - 1),
    AtMostK - AtMostKm1.

-spec at_most(tuple(), integer(), integer()) -> integer().
at_most(_Tuple, _Len, K) when K =< 0 ->
    0;
at_most(Tuple, Len, K) ->
    at_most_loop(0, 0, #{}, 0, 0, Tuple, Len, K).

-spec at_most_loop(integer(), integer(), map(), integer(), integer(),
                   tuple(), integer(), integer()) -> integer().
at_most_loop(Right, Left, FreqMap, Distinct, Total,
             _Tuple, Len, _K) when Right == Len ->
    Total;
at_most_loop(Right, Left, FreqMap, Distinct, Total,
             Tuple, Len, K) ->
    Val = element(Right + 1, Tuple),
    case maps:is_key(Val, FreqMap) of
        true ->
            NewFreq = maps:get(Val, FreqMap) + 1,
            FreqMap1 = maps:put(Val, NewFreq, FreqMap),
            Distinct1 = Distinct;
        false ->
            FreqMap1 = maps:put(Val, 1, FreqMap),
            Distinct1 = Distinct + 1
    end,
    {Left2, FreqMap2, Distinct2} = shrink_window(Left, FreqMap1, Distinct1, Tuple, K),
    Total2 = Total + (Right - Left2 + 1),
    at_most_loop(Right + 1, Left2, FreqMap2, Distinct2, Total2,
                 Tuple, Len, K).

-spec shrink_window(integer(), map(), integer(),
                   tuple(), integer()) -> {integer(), map(), integer()}.
shrink_window(Left, FreqMap, Distinct, _Tuple, K) when Distinct =< K ->
    {Left, FreqMap, Distinct};
shrink_window(Left, FreqMap, Distinct, Tuple, K) ->
    LeftVal = element(Left + 1, Tuple),
    CurrFreq = maps:get(LeftVal, FreqMap) - 1,
    case CurrFreq of
        0 ->
            NewMap = maps:remove(LeftVal, FreqMap),
            shrink_window(Left + 1, NewMap, Distinct - 1, Tuple, K);
        _ ->
            NewMap = maps:put(LeftVal, CurrFreq, FreqMap),
            shrink_window(Left + 1, NewMap, Distinct, Tuple, K)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec subarrays_with_k_distinct(nums :: [integer], k :: integer) :: integer
  def subarrays_with_k_distinct(nums, k) do
    at_most(nums, k) - at_most(nums, k - 1)
  end

  defp at_most(nums, distinct_limit) when distinct_limit < 0 do
    0
  end

  defp at_most(nums, distinct_limit) do
    tup = List.to_tuple(nums)
    n = tuple_size(tup)

    {_, _, total} =
      0..(n - 1)
      |> Enum.reduce({%{}, 0, 0}, fn right, {freq, left, acc} ->
        num = elem(tup, right)
        freq = Map.update(freq, num, 1, &(&1 + 1))

        {freq, left} =
          if map_size(freq) > distinct_limit do
            shrink(freq, left, tup, distinct_limit)
          else
            {freq, left}
          end

        acc = acc + (right - left + 1)
        {freq, left, acc}
      end)

    total
  end

  defp shrink(freq, left, tup, limit) do
    if map_size(freq) <= limit do
      {freq, left}
    else
      num_left = elem(tup, left)

      freq =
        case Map.get(freq, num_left) do
          1 -> Map.delete(freq, num_left)
          v -> Map.put(freq, num_left, v - 1)
        end

      shrink(freq, left + 1, tup, limit)
    end
  end
end
```
