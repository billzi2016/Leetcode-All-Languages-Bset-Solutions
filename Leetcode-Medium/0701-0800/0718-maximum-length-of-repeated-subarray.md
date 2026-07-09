# 0718. Maximum Length of Repeated Subarray

## Cpp

```cpp
class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size();
        vector<int> dp(n + 1, 0);
        int ans = 0;
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (nums1[i] == nums2[j]) {
                    dp[j] = dp[j + 1] + 1;
                    ans = max(ans, dp[j]);
                } else {
                    dp[j] = 0;
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
    public int findLength(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        int[][] dp = new int[m + 1][n + 1];
        int ans = 0;
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (nums1[i] == nums2[j]) {
                    dp[i][j] = dp[i + 1][j + 1] + 1;
                    if (dp[i][j] > ans) ans = dp[i][j];
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    if dp[i][j] > ans:
                        ans = dp[i][j]
        return ans
```

## Python3

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp_next = [0] * (n + 1)   # dp for i+1 row
        ans = 0
        for i in range(m - 1, -1, -1):
            dp_cur = [0] * (n + 1)
            a_val = nums1[i]
            for j in range(n - 1, -1, -1):
                if a_val == nums2[j]:
                    dp_cur[j] = dp_next[j + 1] + 1
                    if dp_cur[j] > ans:
                        ans = dp_cur[j]
            dp_next = dp_cur
        return ans
```

## C

```c
#include <stdlib.h>

int findLength(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int *dp = (int *)calloc(nums2Size + 1, sizeof(int));
    int ans = 0;
    for (int i = nums1Size - 1; i >= 0; --i) {
        int prev = 0; // holds dp[j+1] from previous row
        for (int j = nums2Size - 1; j >= 0; --j) {
            int temp = dp[j];
            if (nums1[i] == nums2[j]) {
                dp[j] = prev + 1;
                if (dp[j] > ans) ans = dp[j];
            } else {
                dp[j] = 0;
            }
            prev = temp;
        }
    }
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindLength(int[] nums1, int[] nums2)
    {
        int m = nums1.Length;
        int n = nums2.Length;
        int[] dp = new int[n + 1];
        int maxLen = 0;

        for (int i = 1; i <= m; i++)
        {
            for (int j = n; j >= 1; j--)
            {
                if (nums1[i - 1] == nums2[j - 1])
                {
                    dp[j] = dp[j - 1] + 1;
                    if (dp[j] > maxLen) maxLen = dp[j];
                }
                else
                {
                    dp[j] = 0;
                }
            }
        }

        return maxLen;
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
var findLength = function(nums1, nums2) {
    const m = nums1.length;
    const n = nums2.length;
    let prev = new Array(n + 1).fill(0);
    let cur = new Array(n + 1).fill(0);
    let ans = 0;
    for (let i = m - 1; i >= 0; --i) {
        for (let j = n - 1; j >= 0; --j) {
            if (nums1[i] === nums2[j]) {
                cur[j] = prev[j + 1] + 1;
                if (cur[j] > ans) ans = cur[j];
            } else {
                cur[j] = 0;
            }
        }
        // swap rows for next iteration
        const temp = prev;
        prev = cur;
        cur = temp;
    }
    return ans;
};
```

## Typescript

```typescript
function findLength(nums1: number[], nums2: number[]): number {
    const m = nums1.length;
    const n = nums2.length;
    let prev = new Array(n + 1).fill(0);
    let curr = new Array(n + 1).fill(0);
    let ans = 0;

    for (let i = m - 1; i >= 0; --i) {
        for (let j = n - 1; j >= 0; --j) {
            if (nums1[i] === nums2[j]) {
                curr[j] = prev[j + 1] + 1;
                if (curr[j] > ans) ans = curr[j];
            } else {
                curr[j] = 0;
            }
        }
        const temp = prev;
        prev = curr;
        curr = temp;
    }

    return ans;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function findLength($nums1, $nums2) {
        $n = count($nums1);
        $m = count($nums2);
        $dp = array_fill(0, $m + 1, 0);
        $ans = 0;
        for ($i = $n - 1; $i >= 0; --$i) {
            $new = array_fill(0, $m + 1, 0);
            for ($j = $m - 1; $j >= 0; --$j) {
                if ($nums1[$i] === $nums2[$j]) {
                    $new[$j] = $dp[$j + 1] + 1;
                    if ($new[$j] > $ans) {
                        $ans = $new[$j];
                    }
                }
            }
            $dp = $new;
        }
        return $ans;
    }
}
?>
```

## Swift

```swift
class Solution {
    func findLength(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let m = nums1.count
        let n = nums2.count
        var dp = Array(repeating: 0, count: n + 1)
        var maxLen = 0
        
        for i in stride(from: m - 1, through: 0, by: -1) {
            var prevDiag = 0
            for j in stride(from: n - 1, through: 0, by: -1) {
                let temp = dp[j]
                if nums1[i] == nums2[j] {
                    dp[j] = prevDiag + 1
                    if dp[j] > maxLen { maxLen = dp[j] }
                } else {
                    dp[j] = 0
                }
                prevDiag = temp
            }
        }
        
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findLength(nums1: IntArray, nums2: IntArray): Int {
        val n = nums1.size
        val m = nums2.size
        var ans = 0
        val dp = IntArray(m + 1)
        for (i in n - 1 downTo 0) {
            var prev = 0
            for (j in m - 1 downTo 0) {
                val temp = dp[j]
                if (nums1[i] == nums2[j]) {
                    dp[j] = prev + 1
                    if (dp[j] > ans) ans = dp[j]
                } else {
                    dp[j] = 0
                }
                prev = temp
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int findLength(List<int> nums1, List<int> nums2) {
    int m = nums1.length;
    int n = nums2.length;
    if (m == 0 || n == 0) return 0;

    // dp[j] will represent the length of longest common subarray
    // starting at nums1[i+1] and nums2[j] for the previous i iteration.
    List<int> dp = List.filled(n + 1, 0);
    int maxLen = 0;

    for (int i = m - 1; i >= 0; i--) {
      int prevDiag = 0; // corresponds to dp[i+1][j+1] before update
      for (int j = n - 1; j >= 0; j--) {
        int temp = dp[j];
        if (nums1[i] == nums2[j]) {
          dp[j] = prevDiag + 1;
          if (dp[j] > maxLen) maxLen = dp[j];
        } else {
          dp[j] = 0;
        }
        prevDiag = temp; // move diagonal for next j-1
      }
    }

    return maxLen;
  }
}
```

## Golang

```go
func findLength(nums1 []int, nums2 []int) int {
    m, n := len(nums1), len(nums2)
    dp := make([]int, n+1)
    maxLen := 0
    for i := 1; i <= m; i++ {
        for j := n; j >= 1; j-- {
            if nums1[i-1] == nums2[j-1] {
                dp[j] = dp[j-1] + 1
                if dp[j] > maxLen {
                    maxLen = dp[j]
                }
            } else {
                dp[j] = 0
            }
        }
    }
    return maxLen
}
```

## Ruby

```ruby
def find_length(nums1, nums2)
  m = nums1.length
  n = nums2.length
  dp = Array.new(n + 1, 0)
  max_len = 0

  (m - 1).downto(0) do |i|
    prev = 0
    (n - 1).downto(0) do |j|
      temp = dp[j]
      if nums1[i] == nums2[j]
        dp[j] = prev + 1
        max_len = dp[j] if dp[j] > max_len
      else
        dp[j] = 0
      end
      prev = temp
    end
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def findLength(nums1: Array[Int], nums2: Array[Int]): Int = {
        val m = nums1.length
        val n = nums2.length
        var ans = 0
        val dp = new Array[Int](n + 1) // extra column of zeros

        for (i <- (m - 1) to 0 by -1) {
            var prev = 0 // holds dp[i+1][j+1] from previous row
            for (j <- (n - 1) to 0 by -1) {
                val temp = dp(j) // this is dp[i+1][j]
                if (nums1(i) == nums2(j)) {
                    dp(j) = prev + 1
                    if (dp(j) > ans) ans = dp(j)
                } else {
                    dp(j) = 0
                }
                prev = temp // move diagonal for next j
            }
        }

        ans
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn find_length(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let m = nums1.len();
        let n = nums2.len();
        let mut prev = vec![0usize; n + 1];
        let mut cur = vec![0usize; n + 1];
        let mut ans = 0usize;

        for i in (0..m).rev() {
            for j in (0..n).rev() {
                if nums1[i] == nums2[j] {
                    cur[j] = prev[j + 1] + 1;
                    if cur[j] > ans {
                        ans = cur[j];
                    }
                } else {
                    cur[j] = 0;
                }
            }
            std::mem::swap(&mut prev, &mut cur);
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (find-length nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((v1 (list->vector nums1))
         (v2 (list->vector nums2))
         (m (vector-length v1))
         (n (vector-length v2))
         (prev (make-vector (+ n 1) 0))
         (curr (make-vector (+ n 1) 0)))
    (let loop-i ((i (- m 1)) (ans 0) (prev prev) (curr curr))
      (if (< i 0)
          ans
          (begin
            ;; ensure the sentinel at position n is zero
            (vector-set! curr n 0)
            (let inner-loop ((j (- n 1)) (best ans))
              (if (< j 0)
                  (loop-i (- i 1) best curr prev) ; swap rows for next iteration
                  (begin
                    (if (= (vector-ref v1 i) (vector-ref v2 j))
                        (let ((val (+ 1 (vector-ref prev (+ j 1)))))
                          (vector-set! curr j val)
                          (inner-loop (- j 1) (max best val)))
                        (begin
                          (vector-set! curr j 0)
                          (inner-loop (- j 1) best)))))))))))
```

## Erlang

```erlang
-module(solution).
-export([find_length/2]).

-spec find_length(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
find_length(Nums1, Nums2) ->
    Len1 = length(Nums1),
    Len2 = length(Nums2),
    Num1Arr = list_to_array(Nums1),
    Num2Arr = list_to_array(Nums2),
    NextRow0 = array:new(Len2 + 1, {default, 0}),
    find_i(Len1 - 1, Len2, Num1Arr, Num2Arr, NextRow0, 0).

%% iterate over indices of the first array from high to low
find_i(-1, _Len2, _Num1Arr, _Num2Arr, _NextRow, Max) ->
    Max;
find_i(I, Len2, Num1Arr, Num2Arr, NextRow, MaxAcc) ->
    Ai = array:get(I, Num1Arr),
    CurrRow0 = array:new(Len2 + 1, {default, 0}),
    {CurrRow, NewMax} = build_row(Len2 - 1, Ai, Num2Arr, NextRow, CurrRow0, MaxAcc),
    find_i(I - 1, Len2, Num1Arr, Num2Arr, CurrRow, NewMax).

%% build a row of DP values for a fixed i, iterating j from high to low
build_row(J, _Ai, _Num2Arr, _NextRow, CurrRow, Max) when J < 0 ->
    {CurrRow, Max};
build_row(J, Ai, Num2Arr, NextRow, CurrRow, MaxSoFar) ->
    Bj = array:get(J, Num2Arr),
    Val = if
        Ai == Bj -> 1 + array:get(J + 1, NextRow);
        true      -> 0
    end,
    UpdatedRow = array:set(J, Val, CurrRow),
    NewMax = max(MaxSoFar, Val),
    build_row(J - 1, Ai, Num2Arr, NextRow, UpdatedRow, NewMax).

%% convert a list to an array indexed from 0
list_to_array(List) ->
    list_to_array(List, 0, array:new()).

list_to_array([], _Idx, Arr) ->
    Arr;
list_to_array([H | T], Idx, Arr) ->
    NewArr = array:set(Idx, H, Arr),
    list_to_array(T, Idx + 1, NewArr).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_length(nums1 :: [integer], nums2 :: [integer]) :: integer
  def find_length(nums1, nums2) do
    m = length(nums1)
    n = length(nums2)

    if m == 0 or n == 0 do
      0
    else
      a = List.to_tuple(nums1)
      b = List.to_tuple(nums2)

      dp_initial = :array.new(n, default: 0)

      {_, max_len} =
        Enum.reduce(Enum.reverse(0..m - 1), {dp_initial, 0}, fn i, {dp_acc, cur_max} ->
          ai = elem(a, i)

          {new_dp, new_max, _prev} =
            Enum.reduce(Enum.reverse(0..n - 1), {dp_acc, cur_max, 0}, fn j,
                                                                      {dp_inner, max_inner,
                                                                       prev} ->
              bj = elem(b, j)
              temp = :array.get(j, dp_inner)

              new_val =
                if ai == bj do
                  prev + 1
                else
                  0
                end

              updated_dp = :array.set(j, new_val, dp_inner)
              max_updated = if new_val > max_inner, do: new_val, else: max_inner
              {updated_dp, max_updated, temp}
            end)

          {new_dp, new_max}
        end)

      max_len
    end
  end
end
```
