# 3364. Minimum Positive Sum Subarray

## Cpp

```cpp
class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int n = nums.size();
        vector<int> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];
        const int INF = INT_MAX;
        int ans = INF;
        for (int start = 0; start < n; ++start) {
            for (int len = l; len <= r; ++len) {
                int end = start + len;
                if (end > n) break;
                int sum = pref[end] - pref[start];
                if (sum > 0 && sum < ans) ans = sum;
            }
        }
        return ans == INF ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumSumSubarray(java.util.List<Integer> nums, int l, int r) {
        int n = nums.size();
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums.get(i);
        }
        int answer = Integer.MAX_VALUE;
        for (int start = 0; start < n; start++) {
            int minEnd = start + l - 1;
            int maxEnd = Math.min(start + r - 1, n - 1);
            if (minEnd > maxEnd) continue;
            for (int end = minEnd; end <= maxEnd; end++) {
                long sum = prefix[end + 1] - prefix[start];
                if (sum > 0 && sum < answer) {
                    answer = (int) sum;
                }
            }
        }
        return answer == Integer.MAX_VALUE ? -1 : answer;
    }
}
```

## Python

```python
class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        best = None
        for start in range(n):
            min_end = start + l - 1
            max_end = min(start + r - 1, n - 1)
            if min_end > max_end:
                continue
            for end in range(min_end, max_end + 1):
                s = pref[end + 1] - pref[start]
                if s > 0:
                    if best is None or s < best:
                        best = s

        return best if best is not None else -1
```

## Python3

```python
from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        best = None
        for i in range(n):
            cur_sum = 0
            for j in range(i, min(n, i + r)):
                cur_sum += nums[j]
                length = j - i + 1
                if length >= l and cur_sum > 0:
                    if best is None or cur_sum < best:
                        best = cur_sum
        return best if best is not None else -1
```

## C

```c
#include <limits.h>

int minimumSumSubarray(int* nums, int numsSize, int l, int r) {
    int pref[101];
    pref[0] = 0;
    for (int i = 0; i < numsSize; ++i) {
        pref[i + 1] = pref[i] + nums[i];
    }
    int ans = INT_MAX;
    for (int i = 0; i < numsSize; ++i) {
        for (int len = l; len <= r && i + len <= numsSize; ++len) {
            int sum = pref[i + len] - pref[i];
            if (sum > 0 && sum < ans) {
                ans = sum;
            }
        }
    }
    return ans == INT_MAX ? -1 : ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumSumSubarray(IList<int> nums, int l, int r) {
        int n = nums.Count;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + nums[i];
        }
        long best = long.MaxValue;
        for (int start = 0; start < n; start++) {
            for (int len = l; len <= r; len++) {
                int end = start + len;
                if (end > n) break;
                long sum = pref[end] - pref[start];
                if (sum > 0 && sum < best) {
                    best = sum;
                }
            }
        }
        return best == long.MaxValue ? -1 : (int)best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var minimumSumSubarray = function(nums, l, r) {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    let ans = Infinity;
    for (let start = 0; start < n; ++start) {
        const minLen = l;
        const maxLen = r;
        const maxEnd = Math.min(n, start + maxLen);
        for (let end = start + minLen; end <= maxEnd; ++end) {
            const sum = prefix[end] - prefix[start];
            if (sum > 0 && sum < ans) {
                ans = sum;
            }
        }
    }
    return ans === Infinity ? -1 : ans;
};
```

## Typescript

```typescript
function minimumSumSubarray(nums: number[], l: number, r: number): number {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    let ans = Number.MAX_SAFE_INTEGER;
    for (let start = 0; start < n; ++start) {
        for (let len = l; len <= r; ++len) {
            const end = start + len - 1;
            if (end >= n) break;
            const sum = prefix[end + 1] - prefix[start];
            if (sum > 0 && sum < ans) {
                ans = sum;
            }
        }
    }
    return ans === Number.MAX_SAFE_INTEGER ? -1 : ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $l
     * @param Integer $r
     * @return Integer
     */
    function minimumSumSubarray($nums, $l, $r) {
        $n = count($nums);
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $pref[$i + 1] = $pref[$i] + $nums[$i];
        }

        $ans = PHP_INT_MAX;
        for ($start = 0; $start < $n; $start++) {
            $minEnd = $start + $l;
            $maxEnd = min($start + $r, $n);
            for ($end = $minEnd; $end <= $maxEnd; $end++) {
                $sum = $pref[$end] - $pref[$start];
                if ($sum > 0 && $sum < $ans) {
                    $ans = $sum;
                }
            }
        }

        return $ans === PHP_INT_MAX ? -1 : $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumSumSubarray(_ nums: [Int], _ l: Int, _ r: Int) -> Int {
        let n = nums.count
        var prefix = [0]
        for num in nums {
            prefix.append(prefix.last! + num)
        }
        var answer = Int.max
        for start in 0..<n {
            for length in l...r {
                let end = start + length - 1
                if end >= n { break }
                let sum = prefix[end + 1] - prefix[start]
                if sum > 0 && sum < answer {
                    answer = sum
                }
            }
        }
        return answer == Int.max ? -1 : answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumSumSubarray(nums: List<Int>, l: Int, r: Int): Int {
        val n = nums.size
        val pref = IntArray(n + 1)
        for (i in 0 until n) {
            pref[i + 1] = pref[i] + nums[i]
        }
        var ans = Int.MAX_VALUE
        for (start in 0 until n) {
            for (len in l..r) {
                val end = start + len - 1
                if (end >= n) break
                val sum = pref[end + 1] - pref[start]
                if (sum > 0 && sum < ans) {
                    ans = sum
                }
            }
        }
        return if (ans == Int.MAX_VALUE) -1 else ans
    }
}
```

## Dart

```dart
class Solution {
  int minimumSumSubarray(List<int> nums, int l, int r) {
    int n = nums.length;
    List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      prefix[i + 1] = prefix[i] + nums[i];
    }
    int ans = 1 << 60; // large value
    bool found = false;
    for (int start = 0; start < n; start++) {
      for (int end = start; end < n; end++) {
        int len = end - start + 1;
        if (len < l || len > r) continue;
        int sum = prefix[end + 1] - prefix[start];
        if (sum > 0 && sum < ans) {
          ans = sum;
          found = true;
        }
      }
    }
    return found ? ans : -1;
  }
}
```

## Golang

```go
func minimumSumSubarray(nums []int, l int, r int) int {
    n := len(nums)
    pref := make([]int, n+1)
    for i := 0; i < n; i++ {
        pref[i+1] = pref[i] + nums[i]
    }
    ans := -1
    for start := 0; start < n; start++ {
        maxLen := r
        if start+maxLen > n {
            maxLen = n - start
        }
        for length := l; length <= maxLen; length++ {
            end := start + length
            sum := pref[end] - pref[start]
            if sum > 0 && (ans == -1 || sum < ans) {
                ans = sum
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def minimum_sum_subarray(nums, l, r)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = prefix[i] + nums[i] }

  min_pos = nil
  (0...n).each do |i|
    start_j = i + l - 1
    end_j = [i + r - 1, n - 1].min
    next if start_j > end_j

    (start_j..end_j).each do |j|
      sum = prefix[j + 1] - prefix[i]
      if sum > 0
        min_pos = sum if min_pos.nil? || sum < min_pos
      end
    end
  end

  min_pos ? min_pos : -1
end
```

## Scala

```scala
object Solution {
    def minimumSumSubarray(nums: List[Int], l: Int, r: Int): Int = {
        val arr = nums.toArray
        val n = arr.length
        val pref = new Array[Int](n + 1)
        for (i <- 0 until n) pref(i + 1) = pref(i) + arr(i)

        var best = Int.MaxValue

        for (start <- 0 until n) {
            val maxLenPossible = math.min(r, n - start)
            for (len <- l to maxLenPossible) {
                val sum = pref(start + len) - pref(start)
                if (sum > 0 && sum < best) best = sum
            }
        }

        if (best == Int.MaxValue) -1 else best
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn minimum_sum_subarray(nums: Vec<i32>, l: i32, r: i32) -> i32 {
        let n = nums.len();
        let l_usize = l as usize;
        let r_usize = r as usize;
        let mut best: i64 = i64::MAX;

        for start in 0..n {
            let mut sum: i64 = 0;
            for end in start..n {
                sum += nums[end] as i64;
                let len = end - start + 1;
                if len > r_usize {
                    break;
                }
                if len >= l_usize && sum > 0 && sum < best {
                    best = sum;
                }
            }
        }

        if best == i64::MAX { -1 } else { best as i32 }
    }
}
```

## Racket

```racket
(define/contract (minimum-sum-subarray nums l r)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((n (length nums))
         (pref (make-vector (+ n 1) 0)))
    ;; prefix sums
    (for ([i (in-range n)])
      (vector-set! pref (add1 i)
                   (+ (vector-ref pref i) (list-ref nums i))))
    (define min-pos #f)
    (for* ([i (in-range n)]
           [len (in-range l (add1 r))])
      (let ((j (+ i len)))
        (when (<= j n)
          (let ((sum (- (vector-ref pref j) (vector-ref pref i))))
            (when (> sum 0)
              (if (or (not min-pos) (< sum min-pos))
                  (set! min-pos sum)))))))
    (if min-pos min-pos -1)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_sum_subarray/3]).

-spec minimum_sum_subarray(Nums :: [integer()], L :: integer(), R :: integer()) -> integer().
minimum_sum_subarray(Nums, L, R) ->
    Prefix = prefix_sums(Nums),
    N = length(Nums),
    find_min_loop(0, N, L, R, Prefix, -1).

%% Build prefix sums with an initial 0.
prefix_sums(Nums) ->
    Rev = prefix_rev(Nums, [0]),
    lists:reverse(Rev).

prefix_rev([], Acc) -> Acc;
prefix_rev([H|T], [Prev|_]=Acc) ->
    New = Prev + H,
    prefix_rev(T, [New|Acc]).

%% Iterate over start indices.
find_min_loop(I, N, _L, _R, _Prefix, Curr) when I >= N ->
    Curr;
find_min_loop(I, N, L, R, Prefix, Curr) ->
    NewCurr = check_lengths(I, L, R, N, Prefix, Curr),
    find_min_loop(I + 1, N, L, R, Prefix, NewCurr).

%% Check all valid lengths for a given start index.
check_lengths(I, L, R, N, Prefix, Curr) ->
    MaxLen = erlang:min(R, N - I),
    check_len_loop(L, I, MaxLen, Prefix, Curr).

check_len_loop(Len, _I, MaxLen, _Prefix, Curr) when Len > MaxLen ->
    Curr;
check_len_loop(Len, I, MaxLen, Prefix, Curr) ->
    Sum = get_sum(Prefix, I, I + Len - 1),
    NewCurr = case (Sum > 0) andalso (Curr == -1 orelse Sum < Curr) of
                  true -> Sum;
                  false -> Curr
              end,
    check_len_loop(Len + 1, I, MaxLen, Prefix, NewCurr).

%% Retrieve subarray sum using prefix sums.
get_sum(Prefix, I, J) ->
    % Prefix list has an extra leading zero at position 1.
    SumJ = lists:nth(J + 2, Prefix),
    SumI = lists:nth(I + 1, Prefix),
    SumJ - SumI.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_sum_subarray(nums :: [integer], l :: integer, r :: integer) :: integer
  def minimum_sum_subarray(nums, l, r) do
    n = length(nums)

    pref_tuple =
      nums
      |> Enum.reduce([0], fn x, [prev | rest] -> [prev + x, prev | rest] end)
      |> Enum.reverse()
      |> List.to_tuple()

    best =
      0..(n - 1)
      |> Enum.reduce(:infinity, fn i, acc_best ->
        max_len = min(r, n - i)

        if max_len < l do
          acc_best
        else
          l..max_len
          |> Enum.reduce(acc_best, fn len, cur_best ->
            j = i + len - 1
            sum = elem(pref_tuple, j + 1) - elem(pref_tuple, i)

            if sum > 0 and sum < cur_best do
              sum
            else
              cur_best
            end
          end)
        end
      end)

    case best do
      :infinity -> -1
      v -> v
    end
  end
end
```
