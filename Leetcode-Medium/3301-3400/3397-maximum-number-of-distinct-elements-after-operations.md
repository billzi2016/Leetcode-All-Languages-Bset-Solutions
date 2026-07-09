# 3397. Maximum Number of Distinct Elements After Operations

## Cpp

```cpp
class Solution {
public:
    int maxDistinctElements(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        long long nextAvail = LLONG_MIN / 4; // sufficiently small
        int distinct = 0;
        long long kk = k;
        for (int x : nums) {
            long long low = (long long)x - kk;
            long long high = (long long)x + kk;
            long long assign = max(low, nextAvail);
            if (assign <= high) {
                ++distinct;
                nextAvail = assign + 1; // next distinct must be larger
            }
        }
        return distinct;
    }
};
```

## Java

```java
class Solution {
    public int maxDistinctElements(int[] nums, int k) {
        int n = nums.length;
        long[][] intervals = new long[n][2];
        for (int i = 0; i < n; i++) {
            long left = (long) nums[i] - k;
            long right = (long) nums[i] + k;
            intervals[i][0] = left;
            intervals[i][1] = right;
        }
        java.util.Arrays.sort(intervals, (a, b) -> {
            if (a[1] != b[1]) return Long.compare(a[1], b[1]);
            return Long.compare(a[0], b[0]);
        });
        long last = Long.MIN_VALUE;
        int distinct = 0;
        for (long[] iv : intervals) {
            long assign = Math.max(iv[0], last + 1);
            if (assign <= iv[1]) {
                distinct++;
                last = assign;
            }
        }
        return distinct;
    }
}
```

## Python

```python
class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        last = -10**20  # smallest assigned value so far
        cnt = 0
        for x in nums:
            l = x - k
            r = x + k
            if last < l:
                last = l
                cnt += 1
            elif last + 1 <= r:
                last += 1
                cnt += 1
            # else: cannot assign a new distinct value for this element
        return cnt
```

## Python3

```python
from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        cur = -10**20  # sufficiently small
        distinct = 0
        for x in nums:
            low = x - k
            high = x + k
            if cur < low:
                cur = low
            if cur <= high:
                distinct += 1
                cur += 1
        return distinct
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    long long l;
    long long r;
} Interval;

static int cmpInterval(const void *a, const void *b) {
    const Interval *ia = (const Interval *)a;
    const Interval *ib = (const Interval *)b;
    if (ia->r < ib->r) return -1;
    if (ia->r > ib->r) return 1;
    if (ia->l < ib->l) return -1;
    if (ia->l > ib->l) return 1;
    return 0;
}

int maxDistinctElements(int* nums, int numsSize, int k) {
    if (numsSize == 0) return 0;
    Interval *arr = (Interval *)malloc(sizeof(Interval) * numsSize);
    if (!arr) return 0; // allocation failure fallback

    long long kk = (long long)k;
    for (int i = 0; i < numsSize; ++i) {
        long long val = (long long)nums[i];
        arr[i].l = val - kk;
        arr[i].r = val + kk;
    }

    qsort(arr, numsSize, sizeof(Interval), cmpInterval);

    long long cur = LLONG_MIN / 4; // sufficiently small
    int distinct = 0;

    for (int i = 0; i < numsSize; ++i) {
        if (cur < arr[i].l) {
            cur = arr[i].l;
            ++distinct;
        } else if (cur + 1 <= arr[i].r) {
            cur = cur + 1;
            ++distinct;
        }
    }

    free(arr);
    return distinct;
}
```

## Csharp

```csharp
using System;

public class Solution
{
    public int MaxDistinctElements(int[] nums, int k)
    {
        int n = nums.Length;
        var intervals = new (long l, long r)[n];
        long kk = k;
        for (int i = 0; i < n; i++)
        {
            long val = nums[i];
            intervals[i] = (val - kk, val + kk);
        }

        Array.Sort(intervals, (a, b) =>
        {
            int cmp = a.r.CompareTo(b.r);
            return cmp != 0 ? cmp : a.l.CompareTo(b.l);
        });

        long last = long.MinValue;
        int distinct = 0;

        foreach (var iv in intervals)
        {
            long assign = Math.Max(iv.l, last + 1);
            if (assign <= iv.r)
            {
                distinct++;
                last = assign;
            }
        }

        return distinct;
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
var maxDistinctElements = function(nums, k) {
    nums.sort((a, b) => a - b);
    let last = -Infinity;
    let count = 0;
    for (let i = 0; i < nums.length; ++i) {
        const l = nums[i] - k;
        const r = nums[i] + k;
        if (last < l) {
            last = l;
            ++count;
        } else if (last + 1 <= r) {
            last = last + 1;
            ++count;
        }
    }
    return count;
};
```

## Typescript

```typescript
function maxDistinctElements(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let cur = -Infinity;
    let count = 0;
    for (const v of nums) {
        const left = v - k;
        const right = v + k;
        const candidate = Math.max(left, cur + 1);
        if (candidate <= right) {
            count++;
            cur = candidate;
        }
    }
    return count;
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
    function maxDistinctElements($nums, $k) {
        sort($nums);
        $cur = PHP_INT_MIN;
        $count = 0;
        foreach ($nums as $num) {
            $candidate = max($num - $k, $cur + 1);
            if ($candidate <= $num + $k) {
                $count++;
                $cur = $candidate;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func maxDistinctElements(_ nums: [Int], _ k: Int) -> Int {
        var intervals = [(l: Int, r: Int)]()
        intervals.reserveCapacity(nums.count)
        for num in nums {
            let l = num - k
            let r = num + k
            intervals.append((l, r))
        }
        intervals.sort { $0.r < $1.r }
        
        var cur = Int.min
        var count = 0
        for interval in intervals {
            let candidate = max(interval.l, cur + 1)
            if candidate <= interval.r {
                count += 1
                cur = candidate
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxDistinctElements(nums: IntArray, k: Int): Int {
        val sorted = nums.sorted()
        var lastUsed = Long.MIN_VALUE
        var distinctCount = 0
        val kk = k.toLong()
        for (value in sorted) {
            val num = value.toLong()
            val left = num - kk
            val right = num + kk
            val candidate = maxOf(left, lastUsed + 1)
            if (candidate <= right) {
                distinctCount++
                lastUsed = candidate
            }
        }
        return distinctCount
    }
}
```

## Dart

```dart
class Solution {
  int maxDistinctElements(List<int> nums, int k) {
    int n = nums.length;
    List<List<int>> intervals = List.generate(n, (i) {
      int l = nums[i] - k;
      int r = nums[i] + k;
      return [l, r];
    });
    intervals.sort((a, b) => a[1].compareTo(b[1]));
    int count = 0;
    int lastUsed = -(1 << 60); // sufficiently small sentinel
    for (var iv in intervals) {
      int l = iv[0];
      int r = iv[1];
      if (l > lastUsed) {
        lastUsed = l;
        count++;
      } else if (lastUsed + 1 <= r) {
        lastUsed = lastUsed + 1;
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
import "sort"

type interval struct {
	l, r int64
}

func maxDistinctElements(nums []int, k int) int {
	n := len(nums)
	intervals := make([]interval, n)
	kk := int64(k)
	for i, v := range nums {
		val := int64(v)
		intervals[i] = interval{l: val - kk, r: val + kk}
	}
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i].r == intervals[j].r {
			return intervals[i].l < intervals[j].l
		}
		return intervals[i].r < intervals[j].r
	})

	const infNeg = -(1 << 60)
	cur := int64(infNeg)
	ans := 0
	for _, iv := range intervals {
		if cur < iv.l {
			cur = iv.l
			ans++
		} else if cur+1 <= iv.r {
			cur = cur + 1
			ans++
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_distinct_elements(nums, k)
  nums.sort!
  ans = 0
  cur = -(1 << 60) # sufficiently small sentinel
  nums.each do |num|
    l = num - k
    r = num + k
    cur = l if cur < l
    if cur <= r
      ans += 1
      cur += 1
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maxDistinctElements(nums: Array[Int], k: Int): Int = {
        val sorted = nums.sorted
        var cur: Long = Long.MinValue / 2
        var distinct = 0
        val kk = k.toLong
        for (num <- sorted) {
            val low = num.toLong - kk
            val high = num.toLong + kk
            val assign = math.max(low, cur)
            if (assign <= high) {
                distinct += 1
                cur = assign + 1
            }
        }
        distinct
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_distinct_elements(nums: Vec<i32>, k: i32) -> i32 {
        let mut arr: Vec<i64> = nums.iter().map(|&x| x as i64).collect();
        arr.sort_unstable();
        let kk = k as i64;
        let mut last: i64 = i64::MIN / 2; // sufficiently small sentinel
        let mut distinct: i32 = 0;
        for &num in &arr {
            let left = num - kk;
            let right = num + kk;
            let candidate = if left > last { left } else { last + 1 };
            if candidate <= right {
                distinct += 1;
                last = candidate;
            }
        }
        distinct
    }
}
```

## Racket

```racket
#lang racket

(define/contract (max-distinct-elements nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([intervals
          (map (lambda (n) (cons (- n k) (+ n k))) nums)]
         [sorted
          (sort intervals (lambda (a b) (< (cdr a) (cdr b))))])
    (let loop ((lst sorted)
               (cur -1000000000000) ; sentinel far below any possible value
               (cnt 0))
      (if (null? lst)
          cnt
          (let* ([pair (car lst)]
                 [l (car pair)]
                 [r (cdr pair)]
                 [x (max l (+ cur 1))])
            (if (<= x r)
                (loop (cdr lst) x (+ cnt 1))
                (loop (cdr lst) cur cnt)))))))
```

## Erlang

```erlang
-spec max_distinct_elements(Nums :: [integer()], K :: integer()) -> integer().
max_distinct_elements(Nums, K) ->
    Intervals = [{Num + K, Num - K} || Num <- Nums],
    Sorted = lists:sort(Intervals),
    process(Sorted, #{}, 0).

process([], _Parent, Count) ->
    Count;
process([{R, L} | Rest], Parent, Count) ->
    {Cand, P1} = find(L, Parent),
    if
        Cand =< R ->
            NewParent = maps:put(Cand, Cand + 1, P1),
            process(Rest, NewParent, Count + 1);
        true ->
            process(Rest, P1, Count)
    end.

find(X, Parent) ->
    case maps:get(X, Parent, undefined) of
        undefined ->
            {X, Parent};
        Next ->
            {Root, Updated} = find(Next, Parent),
            NewParent = maps:put(X, Root, Updated),
            {Root, NewParent}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_distinct_elements(nums :: [integer], k :: integer) :: integer
  def max_distinct_elements(nums, k) do
    sorted = Enum.sort(nums)

    {count, _} =
      Enum.reduce(sorted, {0, -1_000_000_000_000_000_000}, fn a, {cnt, cur} ->
        low = a - k
        high = a + k
        cur = if cur < low, do: low, else: cur

        if cur <= high do
          {cnt + 1, cur + 1}
        else
          {cnt, cur}
        end
      end)

    count
  end
end
```
