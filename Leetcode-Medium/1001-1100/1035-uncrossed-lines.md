# 1035. Uncrossed Lines

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size(), n2 = nums2.size();
        vector<int> dp(n2 + 1, 0), prev(n2 + 1, 0);
        for (int i = 1; i <= n1; ++i) {
            for (int j = 1; j <= n2; ++j) {
                if (nums1[i - 1] == nums2[j - 1])
                    dp[j] = 1 + prev[j - 1];
                else
                    dp[j] = max(dp[j - 1], prev[j]);
            }
            prev.swap(dp);
        }
        return prev[n2];
    }
};
```

## Java

```java
class Solution {
    public int maxUncrossedLines(int[] nums1, int[] nums2) {
        int n1 = nums1.length;
        int n2 = nums2.length;
        int[] prev = new int[n2 + 1];
        int[] cur = new int[n2 + 1];

        for (int i = 1; i <= n1; i++) {
            for (int j = 1; j <= n2; j++) {
                if (nums1[i - 1] == nums2[j - 1]) {
                    cur[j] = 1 + prev[j - 1];
                } else {
                    cur[j] = Math.max(cur[j - 1], prev[j]);
                }
            }
            // swap references for next iteration
            int[] temp = prev;
            prev = cur;
            cur = temp;
        }

        return prev[n2];
    }
}
```

## Python

```python
class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n1, n2 = len(nums1), len(nums2)
        dp = [0] * (n2 + 1)
        for i in range(1, n1 + 1):
            prev = 0
            for j in range(1, n2 + 1):
                temp = dp[j]
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp
        return dp[n2]
```

## Python3

```python
from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [0] * (n2 + 1)
        for i in range(1, n1 + 1):
            prev = 0
            for j in range(1, n2 + 1):
                cur = dp[j]
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = cur
        return dp[n2]
```

## C

```c
#include <stdlib.h>

int maxUncrossedLines(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int *prev = (int*)calloc(nums2Size + 1, sizeof(int));
    int *cur  = (int*)calloc(nums2Size + 1, sizeof(int));

    for (int i = 1; i <= nums1Size; ++i) {
        for (int j = 1; j <= nums2Size; ++j) {
            if (nums1[i - 1] == nums2[j - 1]) {
                cur[j] = prev[j - 1] + 1;
            } else {
                cur[j] = (cur[j - 1] > prev[j]) ? cur[j - 1] : prev[j];
            }
        }
        int *tmp = prev;
        prev = cur;
        cur = tmp;
    }

    int result = prev[nums2Size];
    free(prev);
    free(cur);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxUncrossedLines(int[] nums1, int[] nums2)
    {
        int n1 = nums1.Length;
        int n2 = nums2.Length;
        int[,] dp = new int[n1 + 1, n2 + 1];

        for (int i = 1; i <= n1; i++)
        {
            for (int j = 1; j <= n2; j++)
            {
                if (nums1[i - 1] == nums2[j - 1])
                {
                    dp[i, j] = dp[i - 1, j - 1] + 1;
                }
                else
                {
                    dp[i, j] = dp[i - 1, j] > dp[i, j - 1] ? dp[i - 1, j] : dp[i, j - 1];
                }
            }
        }

        return dp[n1, n2];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var maxUncrossedLines = function(nums1, nums2) {
    const n2 = nums2.length;
    let dpPrev = new Array(n2 + 1).fill(0);
    let dp = new Array(n2 + 1).fill(0);
    
    for (let i = 1; i <= nums1.length; i++) {
        for (let j = 1; j <= n2; j++) {
            if (nums1[i - 1] === nums2[j - 1]) {
                dp[j] = dpPrev[j - 1] + 1;
            } else {
                dp[j] = Math.max(dp[j - 1], dpPrev[j]);
            }
        }
        // prepare for next iteration
        const temp = dpPrev;
        dpPrev = dp;
        dp = temp; // reuse the old array as the new dp buffer
    }
    
    return dpPrev[n2];
};
```

## Typescript

```typescript
function maxUncrossedLines(nums1: number[], nums2: number[]): number {
    const n1 = nums1.length;
    const n2 = nums2.length;
    let prev = new Array(n2 + 1).fill(0);
    let curr = new Array(n2 + 1).fill(0);

    for (let i = 1; i <= n1; i++) {
        curr[0] = 0;
        for (let j = 1; j <= n2; j++) {
            if (nums1[i - 1] === nums2[j - 1]) {
                curr[j] = prev[j - 1] + 1;
            } else {
                curr[j] = Math.max(curr[j - 1], prev[j]);
            }
        }
        // swap references for next iteration
        const temp = prev;
        prev = curr;
        curr = temp;
    }

    return prev[n2];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function maxUncrossedLines($nums1, $nums2) {
        $n1 = count($nums1);
        $n2 = count($nums2);

        // DP with two rows to save space
        $prev = array_fill(0, $n2 + 1, 0);
        $curr = array_fill(0, $n2 + 1, 0);

        for ($i = 1; $i <= $n1; $i++) {
            for ($j = 1; $j <= $n2; $j++) {
                if ($nums1[$i - 1] === $nums2[$j - 1]) {
                    $curr[$j] = $prev[$j - 1] + 1;
                } else {
                    $curr[$j] = max($curr[$j - 1], $prev[$j]);
                }
            }
            // swap rows for next iteration
            $temp = $prev;
            $prev = $curr;
            $curr = $temp;
        }

        return $prev[$n2];
    }
}
```

## Swift

```swift
class Solution {
    func maxUncrossedLines(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n1 = nums1.count
        let n2 = nums2.count
        var prev = [Int](repeating: 0, count: n2 + 1)
        var cur = [Int](repeating: 0, count: n2 + 1)

        for i in 1...n1 {
            for j in 1...n2 {
                if nums1[i - 1] == nums2[j - 1] {
                    cur[j] = 1 + prev[j - 1]
                } else {
                    cur[j] = max(cur[j - 1], prev[j])
                }
            }
            swap(&prev, &cur)
        }

        return prev[n2]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxUncrossedLines(nums1: IntArray, nums2: IntArray): Int {
        val n1 = nums1.size
        val n2 = nums2.size
        val dp = Array(n1 + 1) { IntArray(n2 + 1) }
        for (i in 1..n1) {
            for (j in 1..n2) {
                if (nums1[i - 1] == nums2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1
                } else {
                    dp[i][j] = kotlin.math.max(dp[i - 1][j], dp[i][j - 1])
                }
            }
        }
        return dp[n1][n2]
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maxUncrossedLines(List<int> nums1, List<int> nums2) {
    int n1 = nums1.length;
    int n2 = nums2.length;
    List<List<int>> dp = List.generate(n1 + 1, (_) => List.filled(n2 + 1, 0));

    for (int i = 1; i <= n1; i++) {
      for (int j = 1; j <= n2; j++) {
        if (nums1[i - 1] == nums2[j - 1]) {
          dp[i][j] = dp[i - 1][j - 1] + 1;
        } else {
          dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
      }
    }

    return dp[n1][n2];
  }
}
```

## Golang

```go
func maxUncrossedLines(nums1 []int, nums2 []int) int {
	n1, n2 := len(nums1), len(nums2)
	if n1 == 0 || n2 == 0 {
		return 0
	}
	dpPrev := make([]int, n2+1)
	dp := make([]int, n2+1)

	for i := 1; i <= n1; i++ {
		for j := 1; j <= n2; j++ {
			if nums1[i-1] == nums2[j-1] {
				dp[j] = dpPrev[j-1] + 1
			} else {
				if dp[j-1] > dpPrev[j] {
					dp[j] = dp[j-1]
				} else {
					dp[j] = dpPrev[j]
				}
			}
		}
		copy(dpPrev, dp)
	}
	return dpPrev[n2]
}
```

## Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def max_uncrossed_lines(nums1, nums2)
  n2 = nums2.length
  prev = Array.new(n2 + 1, 0)
  curr = Array.new(n2 + 1, 0)

  nums1.each do |a|
    (1..n2).each do |j|
      if a == nums2[j - 1]
        curr[j] = prev[j - 1] + 1
      else
        curr[j] = [curr[j - 1], prev[j]].max
      end
    end
    prev, curr = curr, prev
  end

  prev[n2]
end
```

## Scala

```scala
object Solution {
    def maxUncrossedLines(nums1: Array[Int], nums2: Array[Int]): Int = {
        val n1 = nums1.length
        val n2 = nums2.length
        val dp = Array.ofDim[Int](n1 + 1, n2 + 1)
        var i = 1
        while (i <= n1) {
            var j = 1
            while (j <= n2) {
                if (nums1(i - 1) == nums2(j - 1))
                    dp(i)(j) = dp(i - 1)(j - 1) + 1
                else
                    dp(i)(j) = math.max(dp(i - 1)(j), dp(i)(j - 1))
                j += 1
            }
            i += 1
        }
        dp(n1)(n2)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_uncrossed_lines(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n1 = nums1.len();
        let n2 = nums2.len();
        if n1 == 0 || n2 == 0 {
            return 0;
        }
        let mut dp_prev = vec![0usize; n2 + 1];
        let mut dp = vec![0usize; n2 + 1];

        for i in 1..=n1 {
            for j in 1..=n2 {
                if nums1[i - 1] == nums2[j - 1] {
                    dp[j] = dp_prev[j - 1] + 1;
                } else {
                    dp[j] = std::cmp::max(dp[j - 1], dp_prev[j]);
                }
            }
            // Prepare for next iteration
            std::mem::swap(&mut dp, &mut dp_prev);
        }

        dp_prev[n2] as i32
    }
}
```

## Racket

```racket
(define/contract (max-uncrossed-lines nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n1 (length nums1))
         (n2 (length nums2))
         (v1 (list->vector nums1))
         (v2 (list->vector nums2))
         (dpPrev (make-vector (+ n2 1) 0))
         (dp (make-vector (+ n2 1) 0)))
    (for ([i (in-range 1 (+ n1 1))])
      (for ([j (in-range 1 (+ n2 1))])
        (if (= (vector-ref v1 (- i 1)) (vector-ref v2 (- j 1)))
            (vector-set! dp j (+ 1 (vector-ref dpPrev (- j 1))))
            (let ((left (vector-ref dp (- j 1)))
                  (up   (vector-ref dpPrev j)))
              (vector-set! dp j (if (> left up) left up)))))
      (let ((tmp dpPrev))
        (set! dpPrev dp)
        (set! dp tmp)))
    (vector-ref dpPrev n2)))
```

## Erlang

```erlang
-module(solution).
-export([max_uncrossed_lines/2]).

-spec max_uncrossed_lines(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
max_uncrossed_lines(Nums1, Nums2) ->
    Len2 = length(Nums2),
    InitPrev = lists:duplicate(Len2 + 1, 0),
    FinalPrev = lists:foldl(fun(A, PrevRow) -> dp_row(A, Nums2, PrevRow) end,
                            InitPrev, Nums1),
    lists:nth(Len2 + 1, FinalPrev).

dp_row(A, BList, PrevRow) ->
    Prev0 = hd(PrevRow),
    {CurrRev, _} = dp_row_loop(A, BList, tl(PrevRow), [0], 0, Prev0),
    lists:reverse(CurrRev).

dp_row_loop(_A, [], _PrevTail, CurrAcc, _LeftVal, _PrevPrev) ->
    {CurrAcc, ok};
dp_row_loop(A, [B|Bs], [PrevJ|PrevRest], CurrAcc, LeftVal, PrevPrev) ->
    NewVal = if A == B -> 1 + PrevPrev;
                true -> max(LeftVal, PrevJ)
             end,
    dp_row_loop(A, Bs, PrevRest, [NewVal | CurrAcc], NewVal, PrevJ).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_uncrossed_lines(nums1 :: [integer], nums2 :: [integer]) :: integer
  def max_uncrossed_lines(nums1, nums2) do
    n1 = length(nums1)
    n2 = length(nums2)

    t1 = List.to_tuple(nums1)
    t2 = List.to_tuple(nums2)

    # initial DP row (all zeros), index 0..n2
    dp_initial = :array.new(n2 + 1, default: 0)

    compute(1, n1, t1, n2, t2, dp_initial)
  end

  defp compute(i, n1, _t1, _n2, _t2, dp_prev) when i > n1 do
    # answer is in the last cell of the final DP row
    :array.get(n2 = length(dp_prev) - 1, dp_prev)
  end

  defp compute(i, n1, t1, n2, t2, dp_prev) do
    a = :erlang.element(i, t1)

    {dp_cur, _} =
      Enum.reduce(1..n2, {:array.new(n2 + 1, default: 0), 0}, fn j, {cur_arr, left} ->
        b = :erlang.element(j, t2)
        up = :array.get(j, dp_prev)

        new_val =
          if a == b do
            1 + :array.get(j - 1, dp_prev)
          else
            max(left, up)
          end

        { :array.set(j, new_val, cur_arr), new_val }
      end)

    compute(i + 1, n1, t1, n2, t2, dp_cur)
  end
end
```
