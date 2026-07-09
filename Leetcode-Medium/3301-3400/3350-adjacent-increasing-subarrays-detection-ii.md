# 3350. Adjacent Increasing Subarrays Detection II

## Cpp

```cpp
class Solution {
public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int n = nums.size();
        vector<int> inc(n, 1);
        for (int i = n - 2; i >= 0; --i) {
            if (nums[i] < nums[i + 1]) inc[i] = inc[i + 1] + 1;
        }
        int ans = 0;
        for (int i = 0; i + 1 < n; ++i) {
            int maxK = (n - i) / 2;
            if (maxK <= ans) continue;
            int lo = ans + 1, hi = maxK;
            while (lo <= hi) {
                int mid = lo + (hi - lo) / 2;
                if (inc[i] >= mid && inc[i + mid] >= mid) {
                    ans = mid;
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
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
    public int maxIncreasingSubarrays(List<Integer> nums) {
        int n = nums.size();
        if (n < 2) return 0;
        int[] incEnd = new int[n];
        incEnd[0] = 1;
        for (int i = 1; i < n; i++) {
            if (nums.get(i) > nums.get(i - 1)) {
                incEnd[i] = incEnd[i - 1] + 1;
            } else {
                incEnd[i] = 1;
            }
        }
        int[] incStart = new int[n];
        incStart[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            if (nums.get(i) < nums.get(i + 1)) {
                incStart[i] = incStart[i + 1] + 1;
            } else {
                incStart[i] = 1;
            }
        }
        int ans = 1;
        for (int i = 0; i < n - 1; i++) {
            int k = Math.min(incEnd[i], incStart[i + 1]);
            if (k > ans) ans = k;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # inc_len[i]: length of longest strictly increasing subarray starting at i
        inc_len = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc_len[i] = inc_len[i + 1] + 1

        def possible(k):
            # need two adjacent subarrays of length k each
            limit = n - 2 * k
            for i in range(limit + 1):
                if inc_len[i] >= k and inc_len[i + k] >= k:
                    return True
            return False

        low, high = 0, n // 2
        while low < high:
            mid = (low + high + 1) // 2
            if possible(mid):
                low = mid
            else:
                high = mid - 1
        return low
```

## Python3

```python
from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        inc_end = [0] * n
        inc_start = [0] * n

        inc_end[0] = 1
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                inc_end[i] = inc_end[i - 1] + 1
            else:
                inc_end[i] = 1

        inc_start[-1] = 1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc_start[i] = inc_start[i + 1] + 1
            else:
                inc_start[i] = 1

        ans = 0
        for i in range(n - 1):
            cur = inc_end[i] if inc_end[i] < inc_start[i + 1] else inc_start[i + 1]
            if cur > ans:
                ans = cur
        return ans
```

## C

```c
#include <stddef.h>

static int feasible(int k, const int *nums, const int *inc_len, int n) {
    if (k == 0) return 1;
    for (int i = 0; i + 2 * k <= n; ++i) {
        if (inc_len[i] >= k && inc_len[i + k] >= k)
            return 1;
    }
    return 0;
}

int maxIncreasingSubarrays(int* nums, int numsSize) {
    if (numsSize < 2) return 0;

    int *inc_len = (int *)malloc(numsSize * sizeof(int));
    if (!inc_len) return 0; // allocation failure fallback

    inc_len[numsSize - 1] = 1;
    for (int i = numsSize - 2; i >= 0; --i) {
        if (nums[i] < nums[i + 1])
            inc_len[i] = inc_len[i + 1] + 1;
        else
            inc_len[i] = 1;
    }

    int low = 0, high = numsSize / 2;
    while (low < high) {
        int mid = (low + high + 1) >> 1;
        if (feasible(mid, nums, inc_len, numsSize))
            low = mid;
        else
            high = mid - 1;
    }

    free(inc_len);
    return low;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxIncreasingSubarrays(IList<int> nums) {
        int n = nums.Count;
        if (n < 2) return 0;
        int[] incStart = new int[n];
        for (int i = n - 1; i >= 0; --i) {
            if (i == n - 1) {
                incStart[i] = 1;
            } else {
                incStart[i] = nums[i] < nums[i + 1] ? incStart[i + 1] + 1 : 1;
            }
        }

        int low = 1, high = n / 2, ans = 0;
        while (low <= high) {
            int mid = low + ((high - low) >> 1);
            bool ok = false;
            for (int i = 0; i + 2 * mid <= n; ++i) {
                if (incStart[i] >= mid && incStart[i + mid] >= mid) {
                    ok = true;
                    break;
                }
            }
            if (ok) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxIncreasingSubarrays = function(nums) {
    const n = nums.length;
    const inc = new Array(n);
    inc[n - 1] = 1;
    for (let i = n - 2; i >= 0; --i) {
        inc[i] = nums[i] < nums[i + 1] ? inc[i + 1] + 1 : 1;
    }
    const maxK = Math.floor(n / 2);
    let low = 0, high = maxK;

    const can = (k) => {
        for (let i = 0; i + 2 * k <= n; ++i) {
            if (inc[i] >= k && inc[i + k] >= k) return true;
        }
        return false;
    };

    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (can(mid)) low = mid;
        else high = mid - 1;
    }
    return low;
};
```

## Typescript

```typescript
function maxIncreasingSubarrays(nums: number[]): number {
    const n = nums.length;
    const inc = new Array<number>(n);
    for (let i = 0; i < n; i++) {
        if (i > 0 && nums[i - 1] < nums[i]) inc[i] = inc[i - 1] + 1;
        else inc[i] = 1;
    }
    const startInc = new Array<number>(n);
    for (let i = n - 1; i >= 0; i--) {
        if (i + 1 < n && nums[i] < nums[i + 1]) startInc[i] = startInc[i + 1] + 1;
        else startInc[i] = 1;
    }
    let ans = 0;
    for (let i = 0; i < n - 1; i++) {
        const k = Math.min(inc[i], startInc[i + 1]);
        if (k > ans) ans = k;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxIncreasingSubarrays($nums) {
        $n = count($nums);
        if ($n < 2) return 0;

        // inc[i] = length of longest strictly increasing subarray starting at i
        $inc = array_fill(0, $n, 1);
        for ($i = $n - 2; $i >= 0; --$i) {
            if ($nums[$i] < $nums[$i + 1]) {
                $inc[$i] = $inc[$i + 1] + 1;
            } else {
                $inc[$i] = 1;
            }
        }

        // binary search on k
        $low = 0;
        $high = intdiv($n, 2);
        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2);
            if ($this->canFit($mid, $inc, $n)) {
                $low = $mid;
            } else {
                $high = $mid - 1;
            }
        }
        return $low;
    }

    private function canFit(int $k, array $inc, int $n): bool {
        if ($k == 0) return true;
        // need i such that inc[i] >= k and inc[i+k] >= k
        for ($i = 0; $i + 2 * $k <= $n; ++$i) {
            if ($inc[$i] >= $k && $inc[$i + $k] >= $k) {
                return true;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func maxIncreasingSubarrays(_ nums: [Int]) -> Int {
        let n = nums.count
        guard n >= 2 else { return 0 }
        var incStart = Array(repeating: 1, count: n)
        if n > 1 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                if nums[i] < nums[i + 1] {
                    incStart[i] = incStart[i + 1] + 1
                }
            }
        }
        var low = 1
        var high = n / 2
        var ans = 0
        while low <= high {
            let mid = (low + high) >> 1
            if possible(k: mid, incStart: incStart, n: n) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return ans
    }

    private func possible(k: Int, incStart: [Int], n: Int) -> Bool {
        if k == 0 { return true }
        let limit = n - 2 * k
        if limit < 0 { return false }
        for i in 0...limit {
            if incStart[i] >= k && incStart[i + k] >= k {
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
    fun maxIncreasingSubarrays(nums: List<Int>): Int {
        val n = nums.size
        if (n < 2) return 0
        val inc = IntArray(n)
        inc[0] = 1
        for (i in 1 until n) {
            inc[i] = if (nums[i - 1] < nums[i]) inc[i - 1] + 1 else 1
        }
        var ans = 0
        var rightLen = 1 // length of increasing subarray starting at i+1
        for (i in n - 2 downTo 0) {
            val k = if (inc[i] < rightLen) inc[i] else rightLen
            if (k > ans) ans = k
            rightLen = if (nums[i] < nums[i + 1]) rightLen + 1 else 1
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxIncreasingSubarrays(List<int> nums) {
    int n = nums.length;
    List<int> incLen = List.filled(n, 1);
    for (int i = n - 2; i >= 0; --i) {
      if (nums[i] < nums[i + 1]) {
        incLen[i] = incLen[i + 1] + 1;
      } else {
        incLen[i] = 1;
      }
    }

    int low = 1, high = n ~/ 2;
    int ans = 1;

    bool can(int k) {
      for (int i = 0; i + 2 * k <= n; ++i) {
        if (incLen[i] >= k && incLen[i + k] >= k) return true;
      }
      return false;
    }

    while (low <= high) {
      int mid = (low + high) >> 1;
      if (can(mid)) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func maxIncreasingSubarrays(nums []int) int {
	n := len(nums)
	if n < 2 {
		return 0
	}
	incStart := make([]int, n)
	incStart[n-1] = 1
	for i := n - 2; i >= 0; i-- {
		if nums[i] < nums[i+1] {
			incStart[i] = incStart[i+1] + 1
		} else {
			incStart[i] = 1
		}
	}

	feasible := func(k int) bool {
		if k == 0 {
			return true
		}
		for i := 0; i+2*k <= n; i++ {
			if incStart[i] >= k && incStart[i+k] >= k {
				return true
			}
		}
		return false
	}

	lo, hi := 0, n/2
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if feasible(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
```

## Ruby

```ruby
def max_increasing_subarrays(nums)
  n = nums.length
  start_inc = Array.new(n, 1)
  (n - 2).downto(0) do |i|
    if nums[i] < nums[i + 1]
      start_inc[i] = start_inc[i + 1] + 1
    else
      start_inc[i] = 1
    end
  end

  lo = 0
  hi = n / 2
  while lo < hi
    mid = (lo + hi + 1) / 2
    ok = false
    limit = n - 2 * mid
    i = 0
    while i <= limit
      if start_inc[i] >= mid && start_inc[i + mid] >= mid
        ok = true
        break
      end
      i += 1
    end
    if ok
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
```

## Scala

```scala
object Solution {
    def maxIncreasingSubarrays(nums: List[Int]): Int = {
        val a = nums.toArray
        val n = a.length
        if (n < 2) return 0
        val inc = Array.fill(n)(1)
        var i = n - 2
        while (i >= 0) {
            if (a(i) < a(i + 1)) inc(i) = inc(i + 1) + 1
            i -= 1
        }
        def feasible(k: Int): Boolean = {
            var start = 0
            while (start + 2 * k <= n) {
                if (inc(start) >= k && inc(start + k) >= k) return true
                start += 1
            }
            false
        }
        var low = 0
        var high = n / 2
        while (low < high) {
            val mid = (low + high + 1) >>> 1
            if (feasible(mid)) low = mid else high = mid - 1
        }
        low
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_increasing_subarrays(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 2 {
            return 0;
        }
        // inc_len[i] = length of maximal strictly increasing subarray starting at i
        let mut inc_len = vec![1usize; n];
        for i in (0..n - 1).rev() {
            if nums[i] < nums[i + 1] {
                inc_len[i] = inc_len[i + 1] + 1;
            }
        }

        fn feasible(k: usize, inc_len: &[usize], n: usize) -> bool {
            if k == 0 {
                return true;
            }
            if 2 * k > n {
                return false;
            }
            for i in 0..=n - 2 * k {
                if inc_len[i] >= k && inc_len[i + k] >= k {
                    return true;
                }
            }
            false
        }

        let mut low = 0usize;
        let mut high = n / 2;
        while low < high {
            let mid = (low + high + 1) / 2;
            if feasible(mid, &inc_len, n) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        low as i32
    }
}
```

## Racket

```racket
(define/contract (max-increasing-subarrays nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (if (< n 2)
        0
        (let ([inc (make-vector n 1)])
          ;; compute length of maximal strictly increasing subarray starting at each index
          (for ([i (in-range (- n 2) -1 -1)]) ; from n-2 down to 0
            (if (< (vector-ref v i) (vector-ref v (+ i 1)))
                (vector-set! inc i (+ 1 (vector-ref inc (+ i 1))))
                (vector-set! inc i 1)))
          ;; predicate: does there exist adjacent increasing subarrays of length k?
          (define (feasible k)
            (if (= k 0)
                #t
                (let loop ([i 0])
                  (cond [(> i (- n (* 2 k))) #f]
                        [(and (>= (vector-ref inc i) k)
                              (>= (vector-ref inc (+ i k)) k))
                         #t]
                        [else (loop (+ i 1))]))))
          ;; binary search for maximum k
          (let loop ([low 0] [high (quotient n 2)])
            (if (< low high)
                (let* ([mid (quotient (+ low high 1) 2)]) ; upper middle (ceil)
                  (if (feasible mid)
                      (loop mid high)
                      (loop low (- mid 1))))
                low))))))
```

## Erlang

```erlang
-spec max_increasing_subarrays(Nums :: [integer()]) -> integer().
max_increasing_subarrays(Nums) ->
    N = length(Nums),
    Tuple = list_to_tuple(Nums),
    IncList = build_inc_len(Tuple),
    IncTuple = list_to_tuple(IncList),
    MaxK = N div 2,
    binary_search(0, MaxK, N, IncTuple).

%% Build inc_len list where inc_len[i] is length of longest strictly increasing subarray starting at i (1‑based)
build_inc_len(Tuple) ->
    Size = tuple_size(Tuple),
    build_inc_len(Size, 0, [], Tuple).

build_inc_len(0, _Prev, Acc, _Tuple) ->
    lists:reverse(Acc);
build_inc_len(I, PrevLen, Acc, Tuple) ->
    Len = if I == tuple_size(Tuple) -> 
              1;
          true ->
              A = element(I, Tuple),
              B = element(I + 1, Tuple),
              if A < B -> PrevLen + 1; true -> 1 end
          end,
    build_inc_len(I - 1, Len, [Len | Acc], Tuple).

%% Binary search for maximum feasible k
binary_search(Low, High, N, Inc) when Low < High ->
    Mid = (Low + High + 1) div 2,
    case feasible(Mid, N, Inc) of
        true -> binary_search(Mid, High, N, Inc);
        false -> binary_search(Low, Mid - 1, N, Inc)
    end;
binary_search(Low, _High, _N, _Inc) ->
    Low.

%% Check if there exists adjacent increasing subarrays of length K
feasible(0, _N, _Inc) -> true;
feasible(K, N, Inc) when K > 0 ->
    Limit = N - 2 * K + 1,
    if Limit < 1 -> false;
       true -> feasible_loop(1, Limit, K, Inc)
    end.

feasible_loop(I, Limit, K, Inc) when I =< Limit ->
    Len1 = element(I, Inc),
    Len2 = element(I + K, Inc),
    if Len1 >= K, Len2 >= K -> true;
       true -> feasible_loop(I + 1, Limit, K, Inc)
    end;
feasible_loop(_, _, _, _) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_increasing_subarrays(nums :: [integer]) :: integer
  def max_increasing_subarrays(nums) do
    n = length(nums)
    tuple = List.to_tuple(nums)

    inc =
      :array.new(n, default: 0)
      |> Enum.reduce((n - 1)..0, fn i, acc ->
        val =
          if i == n - 1 do
            1
          else
            if elem(tuple, i) < elem(tuple, i + 1) do
              1 + :array.get(i + 1, acc)
            else
              1
            end
          end

        :array.set(i, val, acc)
      end)

    binary_search(1, div(n, 2), n, inc, 0)
  end

  defp feasible(k, n, inc) do
    max_start = n - 2 * k

    if max_start < 0 do
      false
    else
      Enum.any?(0..max_start, fn i ->
        :array.get(i, inc) >= k and :array.get(i + k, inc) >= k
      end)
    end
  end

  defp binary_search(low, high, n, inc, ans) do
    if low > high do
      ans
    else
      mid = div(low + high, 2)

      if feasible(mid, n, inc) do
        binary_search(mid + 1, high, n, inc, mid)
      else
        binary_search(low, mid - 1, n, inc, ans)
      end
    end
  end
end
```
