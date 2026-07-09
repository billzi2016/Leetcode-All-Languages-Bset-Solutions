# 2195. Append K Integers With Minimal Sum

## Cpp

```cpp
class Solution {
public:
    long long minimalKSum(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        long long ans = 0;
        long long cur = 1;
        for (int i = 0; i < (int)nums.size() && k > 0; ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            long long val = nums[i];
            if (val > cur) {
                long long gap = val - cur;
                long long take = min<long long>(gap, k);
                long long last = cur + take - 1;
                ans += (cur + last) * take / 2;
                k -= (int)take;
                if (k == 0) break;
            }
            cur = max(cur, val + 1);
        }
        if (k > 0) {
            long long last = cur + k - 1;
            ans += (cur + last) * (long long)k / 2;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long minimalKSum(int[] nums, int k) {
        java.util.Arrays.sort(nums);
        long ans = 0;
        long cur = 1L;
        long remaining = k;
        for (int i = 0; i < nums.length && remaining > 0; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; // skip duplicates
            long val = nums[i];
            if (val > cur) {
                long gap = val - cur;
                long take = Math.min(remaining, gap);
                ans += (cur + (cur + take - 1)) * take / 2;
                remaining -= take;
                if (remaining == 0) break;
            }
            cur = Math.max(cur, val + 1L);
        }
        if (remaining > 0) {
            ans += (cur + (cur + remaining - 1)) * remaining / 2;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        uniq = sorted(set(nums))
        ans = 0
        prev = 0
        for num in uniq:
            if k == 0:
                break
            gap = num - prev - 1
            if gap > 0:
                take = k if k < gap else gap
                start = prev + 1
                end = start + take - 1
                ans += (start + end) * take // 2
                k -= take
            prev = num
        if k > 0:
            start = prev + 1
            end = start + k - 1
            ans += (start + end) * k // 2
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        uniq = sorted(set(nums))
        ans = 0
        cur = 1
        for val in uniq:
            if val > cur:
                cnt = min(k, val - cur)
                # sum of arithmetic sequence from cur to cur+cnt-1
                ans += (2 * cur + cnt - 1) * cnt // 2
                k -= cnt
                if k == 0:
                    return ans
            cur = max(cur, val + 1)
        if k > 0:
            ans += (2 * cur + k - 1) * k // 2
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

long long minimalKSum(int* nums, int numsSize, int k) {
    qsort(nums, numsSize, sizeof(int), cmp_int);
    
    long long ans = 0;
    long long cur = 1;          // smallest candidate integer
    long long remain = k;       // how many numbers still need to be taken
    
    for (int i = 0; i < numsSize && remain > 0; ++i) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;   // skip duplicates
        
        long long val = nums[i];
        if (val < cur) continue;                         // already passed this value
        
        if (val > cur) {
            long long gap = val - cur;                   // missing numbers before val
            long long take = gap < remain ? gap : remain;
            // sum of arithmetic sequence: cur .. cur+take-1
            ans += take * (2 * cur + (take - 1)) / 2;
            remain -= take;
            if (remain == 0) break;
        }
        cur = val + 1;                                   // next candidate after current num
    }
    
    if (remain > 0) {
        long long take = remain;
        ans += take * (2 * cur + (take - 1)) / 2;
    }
    
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long MinimalKSum(int[] nums, int k) {
        Array.Sort(nums);
        long ans = 0;
        long remaining = k;
        long prev = 0;
        foreach (int n in nums) {
            if ((long)n == prev) continue; // skip duplicates
            long gap = (long)n - prev - 1;
            if (gap > 0) {
                long take = Math.Min(gap, remaining);
                long start = prev + 1;
                long end = start + take - 1;
                ans += (start + end) * take / 2;
                remaining -= take;
                if (remaining == 0) return ans;
            }
            prev = n;
        }
        if (remaining > 0) {
            long start = prev + 1;
            long end = start + remaining - 1;
            ans += (start + end) * remaining / 2;
        }
        return ans;
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
var minimalKSum = function(nums, k) {
    // Remove duplicates and sort
    const unique = Array.from(new Set(nums));
    unique.sort((a, b) => a - b);
    
    let ans = 0;
    let prev = 0; // last considered number
    
    for (let i = 0; i < unique.length && k > 0; ++i) {
        const cur = unique[i];
        if (cur > prev + 1) {
            const gap = cur - prev - 1;
            const take = Math.min(gap, k);
            const start = prev + 1;
            const end = start + take - 1;
            ans += ((start + end) * take) / 2;
            k -= take;
        }
        // update prev to the current number (even if we didn't use any from gap)
        prev = cur;
    }
    
    if (k > 0) {
        const start = prev + 1;
        const end = start + k - 1;
        ans += ((start + end) * k) / 2;
    }
    
    return ans;
};
```

## Typescript

```typescript
function minimalKSum(nums: number[], k: number): number {
    const unique = Array.from(new Set(nums));
    unique.sort((a, b) => a - b);
    let ans = 0;
    let prev = 0;
    let remaining = k;

    for (const num of unique) {
        if (num > prev + 1) {
            const gap = num - prev - 1;
            const take = Math.min(gap, remaining);
            const start = prev + 1;
            const end = prev + take;
            ans += ((start + end) * take) / 2;
            remaining -= take;
            if (remaining === 0) return ans;
        }
        if (num > prev) {
            prev = num;
        }
    }

    if (remaining > 0) {
        const start = prev + 1;
        const end = prev + remaining;
        ans += ((start + end) * remaining) / 2;
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
    function minimalKSum($nums, $k) {
        sort($nums);
        $prev = 0;
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n && $k > 0; $i++) {
            $num = $nums[$i];
            if ($i > 0 && $num == $nums[$i - 1]) {
                continue; // skip duplicates
            }
            if ($num > $prev + 1) {
                $gap = $num - $prev - 1;
                $take = min($k, $gap);
                $start = $prev + 1;
                $end = $start + $take - 1;
                $sum = ($start + $end) * $take;
                $ans += intdiv($sum, 2);
                $k -= $take;
            }
            $prev = $num;
        }
        if ($k > 0) {
            $start = $prev + 1;
            $end = $start + $k - 1;
            $sum = ($start + $end) * $k;
            $ans += intdiv($sum, 2);
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimalKSum(_ nums: [Int], _ k: Int) -> Int {
        var sorted = Array(Set(nums)).sorted()
        var remaining = Int64(k)
        var ans: Int64 = 0
        var prev: Int64 = 0

        for num in sorted {
            let cur = Int64(num)
            if cur > prev + 1 && remaining > 0 {
                let gap = cur - prev - 1
                let take = min(gap, remaining)
                let start = prev + 1
                ans += take * (2 * start + (take - 1)) / 2
                remaining -= take
            }
            if remaining == 0 { break }
            prev = cur
        }

        if remaining > 0 {
            let start = prev + 1
            let take = remaining
            ans += take * (2 * start + (take - 1)) / 2
        }

        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimalKSum(nums: IntArray, k: Int): Long {
        val sorted = nums.distinct().sorted()
        var remaining = k.toLong()
        var prev = 0L
        var sum = 0L
        for (value in sorted) {
            val cur = value.toLong()
            if (cur > prev + 1) {
                val gap = cur - prev - 1
                val take = if (remaining < gap) remaining else gap
                val start = prev + 1
                val end = start + take - 1
                sum += (start + end) * take / 2
                remaining -= take
                if (remaining == 0L) return sum
            }
            if (cur > prev) {
                prev = cur
            }
        }
        if (remaining > 0) {
            val start = prev + 1
            val end = start + remaining - 1
            sum += (start + end) * remaining / 2
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int minimalKSum(List<int> nums, int k) {
    var unique = nums.toSet().toList()..sort();
    int start = 1;
    int remaining = k;
    int ans = 0;
    for (var num in unique) {
      if (remaining == 0) break;
      if (num > start) {
        int cnt = num - start;
        if (cnt > remaining) cnt = remaining;
        int end = start + cnt - 1;
        ans += ((start + end) * cnt) ~/ 2;
        remaining -= cnt;
      }
      if (num >= start) {
        start = num + 1;
      }
    }
    if (remaining > 0) {
      int end = start + remaining - 1;
      ans += ((start + end) * remaining) ~/ 2;
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func minimalKSum(nums []int, k int) int64 {
	sort.Ints(nums)
	var ans int64
	cur := int64(1)
	remaining := int64(k)

	n := len(nums)
	i := 0
	for i < n && remaining > 0 {
		val := int64(nums[i])
		j := i + 1
		for j < n && nums[j] == nums[i] {
			j++
		}
		if val >= cur {
			gap := val - cur
			if gap > 0 {
				cnt := remaining
				if gap < cnt {
					cnt = gap
				}
				ans += cnt * (2*cur + cnt - 1) / 2
				remaining -= cnt
			}
			cur = val + 1
		}
		i = j
	}

	if remaining > 0 {
		ans += remaining * (2*cur + remaining - 1) / 2
	}
	return ans
}
```

## Ruby

```ruby
def minimal_k_sum(nums, k)
  sorted = nums.uniq.sort
  ans = 0
  prev = 0

  sorted.each do |num|
    break if k <= 0
    gap = num - prev - 1
    next if gap <= 0

    take = [gap, k].min
    # sum of numbers from prev+1 to prev+take
    ans += take * (2 * prev + take + 1) / 2
    k -= take
    prev = num
  end

  if k > 0
    start = prev + 1
    ans += k * (2 * start + k - 1) / 2
  end

  ans
end
```

## Scala

```scala
object Solution {
    def minimalKSum(nums: Array[Int], k: Int): Long = {
        val sorted = nums.distinct.sorted
        var remaining = k.toLong
        var cur = 1L
        var ans = 0L

        for (numInt <- sorted) {
            val num = numInt.toLong
            if (num > cur) {
                val gap = num - cur
                val take = math.min(remaining, gap)
                // sum of arithmetic series from cur to cur + take - 1
                ans += (cur + (cur + take - 1)) * take / 2
                remaining -= take
                if (remaining == 0) return ans
            }
            cur = Math.max(cur, num + 1)
        }

        if (remaining > 0) {
            val start = cur
            val end = cur + remaining - 1
            ans += (start + end) * remaining / 2
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimal_k_sum(nums: Vec<i32>, k: i32) -> i64 {
        let mut arr = nums;
        arr.sort_unstable();
        arr.dedup();

        let mut remaining = k as i64;
        let mut start: i64 = 1;
        let mut ans: i64 = 0;

        for &v in &arr {
            let val = v as i64;
            if val < start {
                continue;
            }
            if val > start {
                let gap = val - start;
                let take = remaining.min(gap);
                ans += (start + (start + take - 1)) * take / 2;
                remaining -= take;
                if remaining == 0 {
                    return ans;
                }
            }
            start = val + 1;
        }

        if remaining > 0 {
            ans += (start + (start + remaining - 1)) * remaining / 2;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (minimal-k-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted (sort nums <))
         (range-sum
          (lambda (start cnt)
            (/ (* cnt (+ (* 2 start) (- cnt 1))) 2))))
    (let loop ((lst sorted) (cur 1) (rem k) (ans 0))
      (cond
        [(= rem 0) ans]
        [(null? lst) (+ ans (range-sum cur rem))]
        [else
         (define x (car lst))
         (cond
           [(= x cur)
            (loop (cdr lst) (+ cur 1) rem ans)]
           [(< x cur)
            (loop (cdr lst) cur rem ans)]
           [else ; x > cur
            (define gap (- x cur))
            (define take (if (< gap rem) gap rem))
            (define sum-take (range-sum cur take))
            (define new-ans (+ ans sum-take))
            (define new-rem (- rem take))
            (if (= new-rem 0)
                new-ans
                (loop (cdr lst) (+ x 1) new-rem new-ans))])])))))
```

## Erlang

```erlang
-module(solution).
-export([minimal_k_sum/2]).

-spec minimal_k_sum(Nums :: [integer()], K :: integer()) -> integer().
minimal_k_sum(Nums, K) ->
    Sorted = lists:usort(Nums),
    process(Sorted, 1, K, 0).

process([], Start, K, Acc) when K > 0 ->
    Acc + arithmetic_sum(Start, K);
process(_, _Start, 0, Acc) ->
    Acc;
process([H|T], Start, K, Acc) ->
    case H < Start of
        true ->
            process(T, Start, K, Acc);
        false ->
            Gap = H - Start,
            if Gap == 0 ->
                    NewStart = H + 1,
                    process(T, NewStart, K, Acc);
               true ->
                    Take = erlang:min(Gap, K),
                    SumTake = arithmetic_sum(Start, Take),
                    NewK = K - Take,
                    case NewK of
                        0 -> Acc + SumTake;
                        _ ->
                            NewStart = H + 1,
                            process(T, NewStart, NewK, Acc + SumTake)
                    end
            end
    end.

arithmetic_sum(Start, Count) ->
    Count * (2*Start + Count - 1) div 2.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimal_k_sum(nums :: [integer], k :: integer) :: integer
  def minimal_k_sum(nums, k) do
    uniq_sorted = nums |> Enum.uniq() |> Enum.sort()

    {sum, left, start} =
      Enum.reduce_while(uniq_sorted, {0, k, 1}, fn num, {acc, remaining, cur_start} ->
        if remaining == 0 do
          {:halt, {acc, remaining, cur_start}}
        else
          if num > cur_start do
            cnt = min(remaining, num - cur_start)
            added = cnt * (2 * cur_start + cnt - 1) |> div(2)
            new_acc = acc + added
            new_remaining = remaining - cnt

            if new_remaining == 0 do
              {:halt, {new_acc, new_remaining, cur_start}}
            else
              {:cont, {new_acc, new_remaining, num + 1}}
            end
          else
            {:cont, {acc, remaining, max(cur_start, num + 1)}}
          end
        end
      end)

    if left > 0 do
      added = left * (2 * start + left - 1) |> div(2)
      sum + added
    else
      sum
    end
  end
end
```
