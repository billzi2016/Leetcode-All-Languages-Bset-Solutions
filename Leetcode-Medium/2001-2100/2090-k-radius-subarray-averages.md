# 2090. K Radius Subarray Averages

## Cpp

```cpp
class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ans(n, -1);
        if (k == 0) {
            return nums;
        }
        long long windowSize = 2LL * k + 1;
        if (windowSize > n) {
            return ans;
        }
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + nums[i];
        }
        for (int i = k; i <= n - k - 1; ++i) {
            long long sum = pref[i + k + 1] - pref[i - k];
            ans[i] = static_cast<int>(sum / windowSize);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] getAverages(int[] nums, int k) {
        int n = nums.length;
        int[] ans = new int[n];
        java.util.Arrays.fill(ans, -1);
        if (k == 0) {
            System.arraycopy(nums, 0, ans, 0, n);
            return ans;
        }
        long windowSize = 2L * k + 1;
        if (n < windowSize) {
            return ans;
        }
        long sum = 0;
        for (int i = 0; i < windowSize; i++) {
            sum += nums[i];
        }
        int center = k;
        ans[center] = (int) (sum / windowSize);
        for (int i = center + 1; i <= n - k - 1; i++) {
            sum += nums[i + k];
            sum -= nums[i - k - 1];
            ans[i] = (int) (sum / windowSize);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        if k == 0:
            return nums[:]
        window = 2 * k + 1
        if window > n:
            return res
        # prefix sums
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        for i in range(k, n - k):
            total = pref[i + k + 1] - pref[i - k]
            res[i] = total // window
        return res
```

## Python3

```python
from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 0:
            return nums[:]
        window = 2 * k + 1
        if window > n:
            return [-1] * n

        pref = [0] * (n + 1)
        for i, v in enumerate(nums):
            pref[i + 1] = pref[i] + v

        res = [-1] * n
        for i in range(k, n - k):
            total = pref[i + k + 1] - pref[i - k]
            res[i] = total // window
        return res
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getAverages(int* nums, int numsSize, int k, int* returnSize) {
    *returnSize = numsSize;
    int *avgs = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) avgs[i] = -1;

    long long windowLen = 2LL * k + 1;
    if (windowLen > numsSize) return avgs;          // not enough elements for any average
    if (k == 0) {                                   // each element is its own average
        for (int i = 0; i < numsSize; ++i) avgs[i] = nums[i];
        return avgs;
    }

    long long sum = 0;
    for (int i = 0; i < windowLen; ++i) sum += nums[i];   // initial window [0, 2k]

    int center = k;
    avgs[center] = (int)(sum / windowLen);

    for (int i = k + 1; i <= numsSize - k - 1; ++i) {
        // slide window: remove leftmost element and add new rightmost
        sum = sum - nums[i - k - 1] + nums[i + k];
        avgs[i] = (int)(sum / windowLen);
    }

    return avgs;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int[] GetAverages(int[] nums, int k) {
        int n = nums.Length;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = -1;

        if (k == 0) {
            for (int i = 0; i < n; i++) ans[i] = nums[i];
            return ans;
        }

        long windowSize = 2L * k + 1;
        if (windowSize > n) return ans;

        long sum = 0;
        for (int i = 0; i < windowSize; i++) {
            sum += nums[i];
        }
        ans[k] = (int)(sum / windowSize);

        for (int i = k + 1; i <= n - k - 1; i++) {
            sum += nums[i + k];
            sum -= nums[i - k - 1];
            ans[i] = (int)(sum / windowSize);
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
 * @return {number[]}
 */
var getAverages = function(nums, k) {
    const n = nums.length;
    const result = new Array(n).fill(-1);
    
    if (k === 0) {
        // radius zero means each element is its own average
        for (let i = 0; i < n; ++i) result[i] = nums[i];
        return result;
    }
    
    const windowSize = 2 * k + 1;
    if (windowSize > n) return result; // all remain -1
    
    // prefix sums
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + nums[i];
    }
    
    for (let i = k; i <= n - k - 1; ++i) {
        const total = pref[i + k + 1] - pref[i - k];
        result[i] = Math.trunc(total / windowSize);
    }
    
    return result;
};
```

## Typescript

```typescript
function getAverages(nums: number[], k: number): number[] {
    const n = nums.length;
    const res = new Array<number>(n).fill(-1);
    if (k === 0) {
        for (let i = 0; i < n; ++i) res[i] = nums[i];
        return res;
    }
    const windowSize = 2 * k + 1;
    if (windowSize > n) return res;

    // Prefix sums
    const pref = new Array<number>(n + 1);
    pref[0] = 0;
    for (let i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + nums[i];
    }

    for (let i = k; i <= n - k - 1; ++i) {
        const sum = pref[i + k + 1] - pref[i - k];
        res[i] = Math.floor(sum / windowSize);
    }
    return res;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function getAverages($nums, $k) {
        $n = count($nums);
        $res = array_fill(0, $n, -1);
        $window = 2 * $k + 1;
        if ($window > $n) {
            return $res;
        }
        $sum = 0;
        for ($i = 0; $i < $window; $i++) {
            $sum += $nums[$i];
        }
        $center = $k;
        $res[$center] = intdiv($sum, $window);
        for ($center = $k + 1; $center <= $n - $k - 1; $center++) {
            $leftIdx = $center - $k - 1;
            $rightIdx = $center + $k;
            $sum = $sum - $nums[$leftIdx] + $nums[$rightIdx];
            $res[$center] = intdiv($sum, $window);
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func getAverages(_ nums: [Int], _ k: Int) -> [Int] {
        let n = nums.count
        var result = Array(repeating: -1, count: n)
        if k == 0 {
            return nums
        }
        let windowSize = 2 * k + 1
        if windowSize > n {
            return result
        }
        var prefix = [Int64](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + Int64(nums[i])
        }
        let divisor = Int64(windowSize)
        for i in k..<(n - k) {
            let total = prefix[i + k + 1] - prefix[i - k]
            result[i] = Int(total / divisor)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getAverages(nums: IntArray, k: Int): IntArray {
        val n = nums.size
        val ans = IntArray(n) { -1 }
        if (k == 0) {
            for (i in 0 until n) ans[i] = nums[i]
            return ans
        }
        val window = 2 * k + 1
        if (n < window) return ans

        var sum: Long = 0
        for (i in 0 until window) {
            sum += nums[i].toLong()
        }
        ans[k] = (sum / window).toInt()

        for (i in k + 1 until n - k) {
            sum -= nums[i - k - 1].toLong()
            sum += nums[i + k].toLong()
            ans[i] = (sum / window).toInt()
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> getAverages(List<int> nums, int k) {
    int n = nums.length;
    List<int> ans = List.filled(n, -1);
    if (k == 0) return List.from(nums);
    int w = 2 * k + 1;
    if (w > n) return ans;

    int sum = 0;
    for (int i = 0; i < w; ++i) {
      sum += nums[i];
    }
    ans[k] = sum ~/ w;

    for (int center = k + 1; center <= n - k - 1; ++center) {
      sum -= nums[center - k - 1];
      sum += nums[center + k];
      ans[center] = sum ~/ w;
    }
    return ans;
  }
}
```

## Golang

```go
func getAverages(nums []int, k int) []int {
    n := len(nums)
    res := make([]int, n)
    for i := range res {
        res[i] = -1
    }
    if k == 0 {
        copy(res, nums)
        return res
    }
    window := 2*k + 1
    if n < window {
        return res
    }
    pref := make([]int64, n+1)
    for i, v := range nums {
        pref[i+1] = pref[i] + int64(v)
    }
    for i := k; i <= n-1-k; i++ {
        sum := pref[i+k+1] - pref[i-k]
        res[i] = int(sum / int64(window))
    }
    return res
}
```

## Ruby

```ruby
def get_averages(nums, k)
  n = nums.length
  res = Array.new(n, -1)
  window = 2 * k + 1
  return res if window > n

  sum = 0
  (0...window).each { |i| sum += nums[i] }

  i_center = k
  while i_center < n - k
    res[i_center] = sum / window
    if i_center + k + 1 < n
      sum += nums[i_center + k + 1]
      sum -= nums[i_center - k]
    end
    i_center += 1
  end

  res
end
```

## Scala

```scala
object Solution {
    def getAverages(nums: Array[Int], k: Int): Array[Int] = {
        val n = nums.length
        val res = Array.fill[Int](n)(-1)
        if (k == 0) {
            for (i <- 0 until n) res(i) = nums(i)
            return res
        }
        val w = 2 * k + 1
        if (w > n) return res

        var sum: Long = 0L
        for (i <- 0 until w) {
            sum += nums(i).toLong
        }
        res(k) = (sum / w).toInt

        var i = k + 1
        while (i <= n - k - 1) {
            sum -= nums(i - k - 1).toLong
            sum += nums(i + k).toLong
            res(i) = (sum / w).toInt
            i += 1
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_averages(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let mut result = vec![-1; n];
        if k == 0 {
            return nums;
        }
        let radius = k as usize;
        let window_len = 2 * radius + 1;
        if window_len > n {
            return result;
        }

        // initial sum of the first window
        let mut sum: i64 = 0;
        for i in 0..window_len {
            sum += nums[i] as i64;
        }

        // slide the window across valid centers
        for center in radius..=n - radius - 1 {
            result[center] = (sum / window_len as i64) as i32;
            if center + 1 <= n - radius - 1 {
                sum -= nums[center - radius] as i64;
                sum += nums[center + radius + 1] as i64;
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (get-averages nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((n (length nums))
         (window (+ (* 2 k) 1)))
    (if (> window n)
        (make-list n -1)
        (let* ((vec (list->vector nums))
               (result (make-vector n -1))
               (initial-sum
                 (let loop ((i 0) (s 0))
                   (if (= i window)
                       s
                       (loop (+ i 1) (+ s (vector-ref vec i))))))
               )
          (let loop ((center k) (sum initial-sum))
            (when (<= center (- n k 1))
              (vector-set! result center (quotient sum window))
              (if (< center (- n k 1))
                  (let* ((out-index (- center k))
                         (in-index (+ center k 1))
                         (new-sum (+ (- sum (vector-ref vec out-index)) (vector-ref vec in-index))))
                    (loop (+ center 1) new-sum))
                  (void))))
          (vector->list result))))))
```

## Erlang

```erlang
-module(solution).
-export([get_averages/2]).

-spec get_averages(Nums :: [integer()], K :: integer()) -> [integer()].
get_averages(Nums, K) ->
    Len = length(Nums),
    case K of
        0 ->
            Nums;
        _ ->
            Window = 2 * K + 1,
            if
                Window > Len ->
                    lists:duplicate(Len, -1);
                true ->
                    T = list_to_tuple(Nums),
                    Sum0 = sum_range(T, 1, Window, 0),
                    AveragesRev = slide(T, Len, K, Window, K, Sum0, []),
                    Averages = lists:reverse(AveragesRev),
                    PrefixNeg = lists:duplicate(K, -1),
                    SuffixNeg = lists:duplicate(K, -1),
                    PrefixNeg ++ Averages ++ SuffixNeg
            end
    end.

% sum_range(Tuple, Index, MaxIdx, Acc) -> Sum of elements from Index to MaxIdx (inclusive)
sum_range(_T, I, Max, Acc) when I > Max ->
    Acc;
sum_range(T, I, Max, Acc) ->
    Elem = element(I, T),
    sum_range(T, I + 1, Max, Acc + Elem).

% slide(Tuple, Len, K, Window, CenterIdx, Sum, Acc) -> list of averages (reversed)
slide(_T, _Len, _K, _Window, CenterIdx, _Sum, Acc) when CenterIdx > _Len - 1 ->
    Acc;
slide(T, Len, K, Window, CenterIdx, Sum, Acc) ->
    MaxCenter = Len - K - 1,
    if
        CenterIdx > MaxCenter ->
            Acc;
        true ->
            Avg = Sum div Window,
            NewAcc = [Avg | Acc],
            case CenterIdx < MaxCenter of
                true ->
                    LeftIdx0 = CenterIdx - K,          % index leaving window (0‑based)
                    RightIdx0 = CenterIdx + K + 1,     % index entering window (0‑based)
                    LeftVal = element(LeftIdx0 + 1, T),
                    RightVal = element(RightIdx0 + 1, T),
                    NewSum = Sum - LeftVal + RightVal,
                    slide(T, Len, K, Window, CenterIdx + 1, NewSum, NewAcc);
                false ->
                    NewAcc
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_averages(nums :: [integer], k :: integer) :: [integer]
  def get_averages(nums, k) do
    n = length(nums)
    size = 2 * k + 1

    if size > n do
      List.duplicate(-1, n)
    else
      # Prefix sums: pref[i] = sum of nums[0..i-1], pref has length n+1
      pref_list =
        Enum.reduce(nums, [0], fn val, acc ->
          [val + hd(acc) | acc]
        end)
        |> Enum.reverse()

      pref = List.to_tuple(pref_list)

      for i <- 0..(n - 1) do
        if i - k < 0 or i + k >= n do
          -1
        else
          sum = elem(pref, i + k + 1) - elem(pref, i - k)
          div(sum, size)
        end
      end
    end
  end
end
```
