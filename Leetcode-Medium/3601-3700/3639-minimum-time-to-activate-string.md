# 3639. Minimum Time to Activate String

## Cpp

```cpp
class Solution {
public:
    int minTime(string s, vector<int>& order, int k) {
        int n = s.size();
        long long total = 1LL * n * (n + 1) / 2;
        if ((long long)k > total) return -1;

        auto enough = [&](int t) -> bool {
            static vector<char> star; // reuse allocation
            star.assign(n, 0);
            for (int i = 0; i <= t; ++i) star[order[i]] = 1;
            long long nonStarSub = 0;
            int len = 0;
            for (int i = 0; i < n; ++i) {
                if (!star[i]) {
                    ++len;
                } else {
                    nonStarSub += 1LL * len * (len + 1) / 2;
                    len = 0;
                }
            }
            nonStarSub += 1LL * len * (len + 1) / 2;
            long long valid = total - nonStarSub;
            return valid >= k;
        };

        int lo = 0, hi = n - 1, ans = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (enough(mid)) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minTime(String s, int[] order, int k) {
        int n = s.length();
        long total = (long) n * (n + 1) / 2;
        if (total < k) return -1;
        int low = 0, high = n - 1, ans = -1;
        while (low <= high) {
            int mid = (low + high) >>> 1;
            if (enough(mid, s, order, (long) k, total)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    private boolean enough(int t, String s, int[] order, long k, long total) {
        int n = s.length();
        boolean[] star = new boolean[n];
        for (int i = 0; i <= t; i++) {
            star[order[i]] = true;
        }
        long noStar = 0;
        int len = 0;
        for (int i = 0; i < n; i++) {
            if (star[i]) {
                if (len > 0) {
                    noStar += (long) len * (len + 1) / 2;
                    len = 0;
                }
            } else {
                len++;
            }
        }
        if (len > 0) {
            noStar += (long) len * (len + 1) / 2;
        }
        long valid = total - noStar;
        return valid >= k;
    }
}
```

## Python

```python
class Solution(object):
    def minTime(self, s, order, k):
        """
        :type s: str
        :type order: List[int]
        :type k: int
        :rtype: int
        """
        n = len(s)
        total_substrings = n * (n + 1) // 2
        if k > total_substrings:
            return -1

        # time when each position becomes '*'
        pos_time = [0] * n
        for t, idx in enumerate(order):
            pos_time[idx] = t

        def enough(t):
            invalid = 0
            cur_len = 0
            for i in range(n):
                if pos_time[i] <= t:   # this position is '*'
                    if cur_len:
                        invalid += cur_len * (cur_len + 1) // 2
                        cur_len = 0
                else:
                    cur_len += 1
            if cur_len:
                invalid += cur_len * (cur_len + 1) // 2
            return total_substrings - invalid >= k

        # check if even after all replacements it's insufficient
        if not enough(n - 1):
            return -1

        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if enough(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Python3

```python
from typing import List

class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        total_substrings = n * (n + 1) // 2

        # helper to check if at time t the string is active
        def enough(t: int) -> bool:
            star = [False] * n
            for i in range(t + 1):
                star[order[i]] = True

            no_star = 0
            run_len = 0
            for i in range(n):
                if not star[i]:
                    run_len += 1
                else:
                    if run_len:
                        no_star += run_len * (run_len + 1) // 2
                        run_len = 0
            if run_len:
                no_star += run_len * (run_len + 1) // 2

            return total_substrings - no_star >= k

        # quick check if impossible even after all replacements
        if not enough(n - 1):
            return -1

        lo, hi = 0, n - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if enough(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
```

## C

```c
#include <string.h>
#include <stdlib.h>

int minTime(char* s, int* order, int orderSize, int k) {
    int n = (int)strlen(s);
    int *pos = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) pos[order[i]] = i;

    long long total = (long long)n * (n + 1) / 2;
    if (total < k) {
        free(pos);
        return -1;
    }

    int lo = 0, hi = n - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;

        long long sumNoStar = 0, len = 0;
        for (int i = 0; i < n; ++i) {
            if (pos[i] > mid) { // not yet '*'
                ++len;
            } else {
                sumNoStar += len * (len + 1) / 2;
                len = 0;
            }
        }
        sumNoStar += len * (len + 1) / 2;

        long long valid = total - sumNoStar;
        if (valid >= k)
            hi = mid;
        else
            lo = mid + 1;
    }

    free(pos);
    return lo;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinTime(string s, int[] order, int k)
    {
        int n = s.Length;
        long totalAll = (long)n * (n + 1) / 2;
        if (k > totalAll) return -1;

        int[] whenStar = new int[n];
        for (int i = 0; i < n; i++)
            whenStar[order[i]] = i;

        bool Check(int t)
        {
            long without = 0;
            long len = 0;
            for (int i = 0; i < n; i++)
            {
                if (whenStar[i] > t) // not yet starred
                {
                    len++;
                }
                else
                {
                    if (len > 0)
                    {
                        without += len * (len + 1) / 2;
                        len = 0;
                    }
                }
            }
            if (len > 0)
                without += len * (len + 1) / 2;

            long valid = totalAll - without;
            return valid >= k;
        }

        int lo = 0, hi = n - 1, ans = -1;
        while (lo <= hi)
        {
            int mid = lo + ((hi - lo) >> 1);
            if (Check(mid))
            {
                ans = mid;
                hi = mid - 1;
            }
            else
            {
                lo = mid + 1;
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number[]} order
 * @param {number} k
 * @return {number}
 */
var minTime = function(s, order, k) {
    const n = s.length;
    const totalSub = n * (n + 1) / 2;
    if (k > totalSub) return -1;

    // time[i] = moment when position i becomes '*'
    const time = new Array(n);
    for (let t = 0; t < n; ++t) {
        time[order[t]] = t;
    }

    const validCount = (mid) => {
        let invalid = 0;
        let run = 0;
        for (let i = 0; i < n; ++i) {
            if (time[i] > mid) { // still not '*'
                ++run;
            } else {
                if (run > 0) {
                    invalid += run * (run + 1) / 2;
                    run = 0;
                }
            }
        }
        if (run > 0) invalid += run * (run + 1) / 2;
        return totalSub - invalid;
    };

    // If even after all replacements it's insufficient
    if (validCount(n - 1) < k) return -1;

    let lo = 0, hi = n - 1, ans = n - 1;
    while (lo <= hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (validCount(mid) >= k) {
            ans = mid;
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minTime(s: string, order: number[], k: number): number {
    const n = s.length;
    const totalSub = n * (n + 1) / 2;
    if (totalSub < k) return -1;

    // when[i] = time step at which position i becomes '*'
    const when = new Array<number>(n);
    for (let t = 0; t < n; ++t) {
        when[order[t]] = t;
    }

    function enough(t: number): boolean {
        let invalid = 0;
        let run = 0;
        for (let i = 0; i < n; ++i) {
            if (when[i] <= t) { // this position is '*'
                if (run > 0) {
                    invalid += run * (run + 1) / 2;
                    run = 0;
                }
            } else {
                run++;
            }
        }
        if (run > 0) {
            invalid += run * (run + 1) / 2;
        }
        const valid = totalSub - invalid;
        return valid >= k;
    }

    let lo = 0, hi = n - 1, ans = -1;
    while (lo <= hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (enough(mid)) {
            ans = mid;
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[] $order
     * @param Integer $k
     * @return Integer
     */
    function minTime($s, $order, $k) {
        $n = strlen($s);
        $total = $n * ($n + 1) / 2;
        if ($total < $k) {
            return -1;
        }

        // timeAt[i] = step when position i becomes '*'
        $timeAt = array_fill(0, $n, 0);
        foreach ($order as $t => $idx) {
            $timeAt[$idx] = $t;
        }

        $left = 0;
        $right = $n - 1;
        $answer = -1;

        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);

            // compute number of substrings without any '*'
            $invalid = 0;
            $len = 0;
            for ($i = 0; $i < $n; $i++) {
                if ($timeAt[$i] > $mid) { // still not a '*'
                    $len++;
                } else {
                    if ($len > 0) {
                        $invalid += $len * ($len + 1) / 2;
                        $len = 0;
                    }
                }
            }
            if ($len > 0) {
                $invalid += $len * ($len + 1) / 2;
            }

            $valid = $total - $invalid;

            if ($valid >= $k) {
                $answer = $mid;
                $right = $mid - 1;
            } else {
                $left = $mid + 1;
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func minTime(_ s: String, _ order: [Int], _ k: Int) -> Int {
        let n = s.count
        var timeAtPos = Array(repeating: 0, count: n)
        for (step, idx) in order.enumerated() {
            timeAtPos[idx] = step
        }
        let total = Int64(n) * Int64(n + 1) / 2
        if Int64(k) > total { return -1 }
        
        func validCount(_ t: Int) -> Int64 {
            var invalid: Int64 = 0
            var runLen = 0
            for i in 0..<n {
                if timeAtPos[i] > t {
                    runLen += 1
                } else {
                    if runLen > 0 {
                        let L = Int64(runLen)
                        invalid += L * (L + 1) / 2
                        runLen = 0
                    }
                }
            }
            if runLen > 0 {
                let L = Int64(runLen)
                invalid += L * (L + 1) / 2
            }
            return total - invalid
        }
        
        var low = 0, high = n - 1
        var answer = -1
        while low <= high {
            let mid = (low + high) / 2
            if validCount(mid) >= Int64(k) {
                answer = mid
                high = mid - 1
            } else {
                low = mid + 1
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minTime(s: String, order: IntArray, k: Int): Int {
        val n = s.length
        val total = n.toLong() * (n + 1).toLong() / 2
        if (k.toLong() > total) return -1

        val starTime = IntArray(n)
        for (i in order.indices) {
            starTime[order[i]] = i
        }

        var lo = 0
        var hi = n - 1
        var ans = -1
        while (lo <= hi) {
            val mid = (lo + hi) ushr 1

            var sumInvalid = 0L
            var len = 0
            for (i in 0 until n) {
                if (starTime[i] > mid) {
                    len++
                } else {
                    if (len > 0) {
                        sumInvalid += len.toLong() * (len + 1).toLong() / 2
                        len = 0
                    }
                }
            }
            if (len > 0) {
                sumInvalid += len.toLong() * (len + 1).toLong() / 2
            }

            val valid = total - sumInvalid
            if (valid >= k.toLong()) {
                ans = mid
                hi = mid - 1
            } else {
                lo = mid + 1
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minTime(String s, List<int> order, int k) {
    int n = s.length;
    int total = n * (n + 1) ~/ 2;
    if (total < k) return -1;

    bool isActive(int t) {
      List<bool> star = List.filled(n, false);
      for (int i = 0; i <= t; i++) {
        star[order[i]] = true;
      }
      int invalid = 0;
      int len = 0;
      for (int i = 0; i < n; i++) {
        if (!star[i]) {
          len++;
        } else {
          if (len > 0) {
            invalid += len * (len + 1) ~/ 2;
            len = 0;
          }
        }
      }
      if (len > 0) {
        invalid += len * (len + 1) ~/ 2;
      }
      int valid = total - invalid;
      return valid >= k;
    }

    int lo = 0, hi = n - 1, ans = -1;
    while (lo <= hi) {
      int mid = (lo + hi) >> 1;
      if (isActive(mid)) {
        ans = mid;
        hi = mid - 1;
      } else {
        lo = mid + 1;
      }
    }
    return ans;
  }
}
```

## Golang

```go
package main

func minTime(s string, order []int, k int) int {
	n := len(s)
	total := int64(n) * (int64(n) + 1) / 2
	if int64(k) > total {
		return -1
	}
	targetInvalidMax := total - int64(k)

	parent := make([]int, n)
	sizeArr := make([]int, n)
	active := make([]bool, n)

	var find func(int) int
	find = func(x int) int {
		if parent[x] != x {
			parent[x] = find(parent[x])
		}
		return parent[x]
	}

	invalid := int64(0)
	answer := -1

	for i := n - 1; i >= 0; i-- {
		pos := order[i]
		active[pos] = true
		parent[pos] = pos
		sizeArr[pos] = 1
		invalid += 1 // contribution of length 1

		// left neighbor
		if pos > 0 && active[pos-1] {
			r1 := find(pos)
			r2 := find(pos - 1)
			if r1 != r2 {
				sz1 := sizeArr[r1]
				sz2 := sizeArr[r2]
				invalid -= int64(sz1) * (int64(sz1) + 1) / 2
				invalid -= int64(sz2) * (int64(sz2) + 1) / 2
				if sz1 < sz2 {
					r1, r2 = r2, r1
					sz1, sz2 = sz2, sz1
				}
				parent[r2] = r1
				sizeArr[r1] = sz1 + sz2
				newSize := sizeArr[r1]
				invalid += int64(newSize) * (int64(newSize) + 1) / 2
			}
		}

		// right neighbor
		if pos+1 < n && active[pos+1] {
			r1 := find(pos)
			r2 := find(pos + 1)
			if r1 != r2 {
				sz1 := sizeArr[r1]
				sz2 := sizeArr[r2]
				invalid -= int64(sz1) * (int64(sz1) + 1) / 2
				invalid -= int64(sz2) * (int64(sz2) + 1) / 2
				if sz1 < sz2 {
					r1, r2 = r2, r1
					sz1, sz2 = sz2, sz1
				}
				parent[r2] = r1
				sizeArr[r1] = sz1 + sz2
				newSize := sizeArr[r1]
				invalid += int64(newSize) * (int64(newSize) + 1) / 2
			}
		}

		if invalid > targetInvalidMax {
			answer = i
			break
		}
	}

	if answer == -1 {
		// Should not happen, but default to 0
		return 0
	}
	return answer
}
```

## Ruby

```ruby
def min_time(s, order, k)
  n = s.length
  total = n * (n + 1) / 2
  return -1 if total < k

  left = 0
  right = n - 1
  answer = -1

  while left <= right
    mid = (left + right) / 2

    stars = Array.new(n, false)
    i = 0
    while i <= mid
      stars[order[i]] = true
      i += 1
    end

    invalid = 0
    len = 0
    j = 0
    while j < n
      if stars[j]
        if len > 0
          invalid += len * (len + 1) / 2
          len = 0
        end
      else
        len += 1
      end
      j += 1
    end
    invalid += len * (len + 1) / 2 if len > 0

    valid = total - invalid
    if valid >= k
      answer = mid
      right = mid - 1
    else
      left = mid + 1
    end
  end

  answer
end
```

## Scala

```scala
object Solution {
    def minTime(s: String, order: Array[Int], k: Int): Int = {
        val n = s.length
        val pos = new Array[Int](n)
        var i = 0
        while (i < n) {
            pos(order(i)) = i
            i += 1
        }
        val total: Long = n.toLong * (n + 1L) / 2L
        val kk: Long = k.toLong

        def valid(t: Int): Long = {
            var invalid: Long = 0L
            var len: Long = 0L
            var idx = 0
            while (idx < n) {
                if (pos(idx) <= t) {
                    invalid += len * (len + 1) / 2
                    len = 0L
                } else {
                    len += 1L
                }
                idx += 1
            }
            invalid += len * (len + 1) / 2
            total - invalid
        }

        if (valid(n - 1) < kk) return -1

        var lo = 0
        var hi = n - 1
        var ans = -1
        while (lo <= hi) {
            val mid = lo + (hi - lo) / 2
            if (valid(mid) >= kk) {
                ans = mid
                hi = mid - 1
            } else {
                lo = mid + 1
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_time(s: String, order: Vec<i32>, k: i32) -> i32 {
        let n = s.len();
        let total: i64 = (n as i64) * (n as i64 + 1) / 2;
        let mut time_of = vec![0usize; n];
        for (t, &idx_i32) in order.iter().enumerate() {
            let idx = idx_i32 as usize;
            time_of[idx] = t;
        }

        fn ok(t: usize, time_of: &[usize], n: usize, total: i64, k: i64) -> bool {
            let mut invalid: i64 = 0;
            let mut run_len: i64 = 0;
            for i in 0..n {
                if time_of[i] > t {
                    run_len += 1;
                } else {
                    if run_len > 0 {
                        invalid += run_len * (run_len + 1) / 2;
                        run_len = 0;
                    }
                }
            }
            if run_len > 0 {
                invalid += run_len * (run_len + 1) / 2;
            }
            total - invalid >= k
        }

        let mut lo: usize = 0;
        let mut hi: usize = n; // exclusive upper bound
        while lo < hi {
            let mid = (lo + hi) / 2;
            if ok(mid, &time_of, n, total, k as i64) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }

        if lo == n { -1 } else { lo as i32 }
    }
}
```

## Racket

```racket
(define/contract (min-time s order k)
  (-> string? (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (string-length s))
         (total (/ (* n (+ n 1)) 2))) ; total substrings
    (if (> k total)
        -1
        (let* ((order-vec (list->vector order))
               (act (make-vector n)))
          ;; act[pos] = time when it becomes '*'
          (for ([i (in-range n)])
            (let ((pos (vector-ref order-vec i)))
              (vector-set! act pos i)))
          (define (valid? t)
            (let loop ((i 0) (run 0) (invalid 0))
              (if (= i n)
                  (let* ((final-invalid (+ invalid (quotient (* run (+ run 1)) 2)))
                         (valid (- total final-invalid)))
                    (>= valid k))
                  (if (<= (vector-ref act i) t) ; position is '*'
                      (let ((new-invalid (+ invalid (quotient (* run (+ run 1)) 2))))
                        (loop (+ i 1) 0 new-invalid))
                      (loop (+ i 1) (+ run 1) invalid))))))
          ;; binary search for minimal t
          (let search ((lo 0) (hi (- n 1)) (ans -1))
            (if (> lo hi)
                ans
                (let ((mid (quotient (+ lo hi) 2)))
                  (if (valid? mid)
                      (search lo (- mid 1) mid)
                      (search (+ mid 1) hi ans)))))))))
```

## Erlang

```erlang
-module(solution).
-export([min_time/3]).

min_time(S, Order, K) ->
    N = byte_size(S),
    Total = N * (N + 1) div 2,
    case K > Total of
        true -> -1;
        false ->
            PosMap = maps:from_list(lists:zip(Order, lists:seq(0, N-1))),
            binary_search(0, N-1, -1, PosMap, N, K)
    end.

binary_search(Low, High, Ans, _PosMap, _N, _K) when Low > High ->
    Ans;
binary_search(Low, High, Ans, PosMap, N, K) ->
    Mid = (Low + High) div 2,
    Valid = compute_valid(Mid, PosMap, N),
    if
        Valid >= K ->
            binary_search(Low, Mid - 1, Mid, PosMap, N, K);
        true ->
            binary_search(Mid + 1, High, Ans, PosMap, N, K)
    end.

compute_valid(T, PosMap, N) ->
    Total = N * (N + 1) div 2,
    {Acc, Run} = lists:foldl(
        fun(I, {Sum, Len}) ->
            case maps:get(I, PosMap) =< T of
                true -> % starred position
                    NewSum = Sum + Len * (Len + 1) div 2,
                    {NewSum, 0};
                false ->
                    {Sum, Len + 1}
            end
        end,
        {0, 0},
        lists:seq(0, N - 1)
    ),
    NonStar = Acc + Run * (Run + 1) div 2,
    Total - NonStar.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_time(String.t(), [integer()], integer()) :: integer()
  def min_time(s, order, k) do
    n = String.length(s)
    total = div(n * (n + 1), 2)

    low = 0
    high = n - 1
    ans = -1

    while low <= high do
      mid = div(low + high, 2)

      if active?(mid, order, total, k, n) do
        ans = mid
        high = mid - 1
      else
        low = mid + 1
      end
    end

    ans
  end

  defp active?(t, order, total, k, n) do
    stars = MapSet.new(Enum.take(order, t + 1))

    {invalid, cur_len} =
      Enum.reduce(0..(n - 1), {0, 0}, fn i, {inv, len} ->
        if MapSet.member?(stars, i) do
          {inv + div(len * (len + 1), 2), 0}
        else
          {inv, len + 1}
        end
      end)

    invalid = invalid + div(cur_len * (cur_len + 1), 2)
    valid = total - invalid
    valid >= k
  end
end
```
