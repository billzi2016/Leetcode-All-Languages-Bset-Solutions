# 1664. Ways to Make a Fair Array

## Cpp

```cpp
class Solution {
public:
    int waysToMakeFair(vector<int>& nums) {
        int n = nums.size();
        vector<long long> preEven(n + 1, 0), preOdd(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            preEven[i + 1] = preEven[i];
            preOdd[i + 1] = preOdd[i];
            if (i % 2 == 0) preEven[i + 1] += nums[i];
            else preOdd[i + 1] += nums[i];
        }
        long long totalEven = preEven[n];
        long long totalOdd = preOdd[n];
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            long long evenSum = preEven[i];
            long long oddSum = preOdd[i];
            long long suffixEven = totalEven - preEven[i + 1];
            long long suffixOdd = totalOdd - preOdd[i + 1];
            long long newEven = evenSum + suffixOdd;
            long long newOdd = oddSum + suffixEven;
            if (newEven == newOdd) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int waysToMakeFair(int[] nums) {
        int n = nums.length;
        long[] prefEven = new long[n + 1];
        long[] prefOdd = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefEven[i + 1] = prefEven[i];
            prefOdd[i + 1] = prefOdd[i];
            if ((i & 1) == 0) {
                prefEven[i + 1] += nums[i];
            } else {
                prefOdd[i + 1] += nums[i];
            }
        }
        long totalEven = prefEven[n];
        long totalOdd = prefOdd[n];
        int count = 0;
        for (int i = 0; i < n; i++) {
            long evenBefore = prefEven[i];
            long oddBefore = prefOdd[i];
            long evenAfter = totalEven - prefEven[i + 1];
            long oddAfter = totalOdd - prefOdd[i + 1];
            long newEven = evenBefore + oddAfter;
            long newOdd = oddBefore + evenAfter;
            if (newEven == newOdd) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pref_even = [0] * (n + 1)
        pref_odd = [0] * (n + 1)
        for i in range(n):
            pref_even[i + 1] = pref_even[i]
            pref_odd[i + 1] = pref_odd[i]
            if i & 1:
                pref_odd[i + 1] += nums[i]
            else:
                pref_even[i + 1] += nums[i]

        total_even = pref_even[n]
        total_odd = pref_odd[n]
        ans = 0
        for i in range(n):
            left_even = pref_even[i]
            left_odd = pref_odd[i]
            suffix_even = total_even - pref_even[i + 1]
            suffix_odd = total_odd - pref_odd[i + 1]

            new_even = left_even + suffix_odd
            new_odd = left_odd + suffix_even

            if new_even == new_odd:
                ans += 1
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        pre_even = [0] * (n + 1)
        pre_odd = [0] * (n + 1)

        for i, val in enumerate(nums):
            pre_even[i + 1] = pre_even[i] + (val if i % 2 == 0 else 0)
            pre_odd[i + 1] = pre_odd[i] + (val if i % 2 == 1 else 0)

        total_even = pre_even[n]
        total_odd = pre_odd[n]

        ans = 0
        for i in range(n):
            even_after = pre_even[i] + (total_odd - pre_odd[i + 1])
            odd_after = pre_odd[i] + (total_even - pre_even[i + 1])
            if even_after == odd_after:
                ans += 1

        return ans
```

## C

```c
int waysToMakeFair(int* nums, int numsSize) {
    long long *prefEven = (long long*)malloc((numsSize + 1) * sizeof(long long));
    long long *prefOdd = (long long*)malloc((numsSize + 1) * sizeof(long long));
    prefEven[0] = prefOdd[0] = 0;
    for (int i = 0; i < numsSize; ++i) {
        prefEven[i + 1] = prefEven[i];
        prefOdd[i + 1] = prefOdd[i];
        if ((i & 1) == 0)
            prefEven[i + 1] += nums[i];
        else
            prefOdd[i + 1] += nums[i];
    }
    long long totalEven = prefEven[numsSize];
    long long totalOdd = prefOdd[numsSize];
    int ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        long long evenBefore = prefEven[i];
        long long oddBefore = prefOdd[i];
        long long evenAfter = totalEven - prefEven[i + 1];
        long long oddAfter = totalOdd - prefOdd[i + 1];
        long long newEven = evenBefore + oddAfter;
        long long newOdd = oddBefore + evenAfter;
        if (newEven == newOdd)
            ++ans;
    }
    free(prefEven);
    free(prefOdd);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int WaysToMakeFair(int[] nums) {
        int n = nums.Length;
        long totalEven = 0, totalOdd = 0;
        for (int i = 0; i < n; i++) {
            if ((i & 1) == 0) totalEven += nums[i];
            else totalOdd += nums[i];
        }

        long[] preEven = new long[n + 1];
        long[] preOdd = new long[n + 1];
        for (int i = 0; i < n; i++) {
            preEven[i + 1] = preEven[i];
            preOdd[i + 1] = preOdd[i];
            if ((i & 1) == 0) preEven[i + 1] += nums[i];
            else preOdd[i + 1] += nums[i];
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            long evenBefore = preEven[i];
            long oddBefore = preOdd[i];
            long evenAfterOriginal = totalEven - preEven[i + 1];
            long oddAfterOriginal = totalOdd - preOdd[i + 1];

            long newEven = evenBefore + oddAfterOriginal;
            long newOdd = oddBefore + evenAfterOriginal;

            if (newEven == newOdd) count++;
        }

        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var waysToMakeFair = function(nums) {
    const n = nums.length;
    const prefEven = new Array(n + 1).fill(0);
    const prefOdd = new Array(n + 1).fill(0);
    
    for (let i = 0; i < n; ++i) {
        prefEven[i + 1] = prefEven[i];
        prefOdd[i + 1] = prefOdd[i];
        if ((i & 1) === 0) {
            prefEven[i + 1] += nums[i];
        } else {
            prefOdd[i + 1] += nums[i];
        }
    }
    
    const totalEven = prefEven[n];
    const totalOdd = prefOdd[n];
    let count = 0;
    
    for (let i = 0; i < n; ++i) {
        const evenBefore = prefEven[i];
        const oddBefore = prefOdd[i];
        
        const evensAfter = totalEven - prefEven[i + 1];
        const oddsAfter = totalOdd - prefOdd[i + 1];
        
        const newEvenSum = evenBefore + oddsAfter;
        const newOddSum = oddBefore + evensAfter;
        
        if (newEvenSum === newOddSum) {
            ++count;
        }
    }
    
    return count;
};
```

## Typescript

```typescript
function waysToMakeFair(nums: number[]): number {
    const n = nums.length;
    const prefEven = new Array(n + 1).fill(0);
    const prefOdd = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        prefEven[i + 1] = prefEven[i];
        prefOdd[i + 1] = prefOdd[i];
        if ((i & 1) === 0) {
            prefEven[i + 1] += nums[i];
        } else {
            prefOdd[i + 1] += nums[i];
        }
    }
    const totalEven = prefEven[n];
    const totalOdd = prefOdd[n];
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const leftEven = prefEven[i];
        const leftOdd = prefOdd[i];
        const rightEven = totalEven - prefEven[i + 1];
        const rightOdd = totalOdd - prefOdd[i + 1];
        const newEven = leftEven + rightOdd;
        const newOdd = leftOdd + rightEven;
        if (newEven === newOdd) ans++;
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
    function waysToMakeFair($nums) {
        $n = count($nums);
        $prefEven = array_fill(0, $n + 1, 0);
        $prefOdd = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $prefEven[$i + 1] = $prefEven[$i];
            $prefOdd[$i + 1] = $prefOdd[$i];
            if (($i & 1) === 0) {
                $prefEven[$i + 1] += $nums[$i];
            } else {
                $prefOdd[$i + 1] += $nums[$i];
            }
        }
        $totalEven = $prefEven[$n];
        $totalOdd = $prefOdd[$n];
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $evenBefore = $prefEven[$i];
            $oddBefore = $prefOdd[$i];
            $evenAfter = $evenBefore + ($totalOdd - $prefOdd[$i + 1]);
            $oddAfter = $oddBefore + ($totalEven - $prefEven[$i + 1]);
            if ($evenAfter === $oddAfter) {
                $ans++;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func waysToMakeFair(_ nums: [Int]) -> Int {
        let n = nums.count
        var prefixEven = Array(repeating: 0, count: n + 1)
        var prefixOdd = Array(repeating: 0, count: n + 1)
        
        for i in 0..<n {
            prefixEven[i + 1] = prefixEven[i]
            prefixOdd[i + 1] = prefixOdd[i]
            if i % 2 == 0 {
                prefixEven[i + 1] += nums[i]
            } else {
                prefixOdd[i + 1] += nums[i]
            }
        }
        
        let totalEven = prefixEven[n]
        let totalOdd = prefixOdd[n]
        var answer = 0
        
        for i in 0..<n {
            let leftEven = prefixEven[i]
            let leftOdd = prefixOdd[i]
            let rightEvenOrig = totalEven - prefixEven[i + 1]
            let rightOddOrig = totalOdd - prefixOdd[i + 1]
            
            if leftEven + rightOddOrig == leftOdd + rightEvenOrig {
                answer += 1
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun waysToMakeFair(nums: IntArray): Int {
        val n = nums.size
        val preEven = LongArray(n + 1)
        val preOdd = LongArray(n + 1)
        var totalEven = 0L
        var totalOdd = 0L
        for (i in 0 until n) {
            preEven[i + 1] = preEven[i]
            preOdd[i + 1] = preOdd[i]
            if ((i and 1) == 0) {
                preEven[i + 1] += nums[i].toLong()
                totalEven += nums[i].toLong()
            } else {
                preOdd[i + 1] += nums[i].toLong()
                totalOdd += nums[i].toLong()
            }
        }
        var ans = 0
        for (i in 0 until n) {
            val evenBefore = preEven[i]
            val oddBefore = preOdd[i]
            val newEven = evenBefore + (totalOdd - preOdd[i + 1])
            val newOdd = oddBefore + (totalEven - preEven[i + 1])
            if (newEven == newOdd) ans++
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int waysToMakeFair(List<int> nums) {
    int n = nums.length;
    List<int> preEven = List.filled(n + 1, 0);
    List<int> preOdd = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      preEven[i + 1] = preEven[i];
      preOdd[i + 1] = preOdd[i];
      if ((i & 1) == 0) {
        preEven[i + 1] += nums[i];
      } else {
        preOdd[i + 1] += nums[i];
      }
    }
    int totalEven = preEven[n];
    int totalOdd = preOdd[n];
    int count = 0;
    for (int i = 0; i < n; i++) {
      int leftEven = preEven[i];
      int leftOdd = preOdd[i];
      int rightEven = totalOdd - preOdd[i + 1];
      int rightOdd = totalEven - preEven[i + 1];
      if (leftEven + rightEven == leftOdd + rightOdd) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func waysToMakeFair(nums []int) int {
    n := len(nums)
    prefEven := make([]int, n+1)
    prefOdd := make([]int, n+1)

    totalEven, totalOdd := 0, 0
    for i, v := range nums {
        if i%2 == 0 {
            totalEven += v
            prefEven[i+1] = prefEven[i] + v
            prefOdd[i+1] = prefOdd[i]
        } else {
            totalOdd += v
            prefOdd[i+1] = prefOdd[i] + v
            prefEven[i+1] = prefEven[i]
        }
    }

    count := 0
    for i := 0; i < n; i++ {
        leftEven := prefEven[i]
        leftOdd := prefOdd[i]

        rightEvenAfter := totalOdd - prefOdd[i+1] // original odd indices become even
        rightOddAfter := totalEven - prefEven[i+1] // original even indices become odd

        if leftEven+rightEvenAfter == leftOdd+rightOddAfter {
            count++
        }
    }

    return count
}
```

## Ruby

```ruby
def ways_to_make_fair(nums)
  total_even = 0
  total_odd = 0
  nums.each_with_index do |v, idx|
    if idx.even?
      total_even += v
    else
      total_odd += v
    end
  end

  pre_even = 0
  pre_odd = 0
  ans = 0

  nums.each_with_index do |v, i|
    if i.even?
      left_even = pre_even
      left_odd = pre_odd
      right_even = total_even - pre_even - v
      right_odd = total_odd - pre_odd
    else
      left_even = pre_even
      left_odd = pre_odd
      right_even = total_even - pre_even
      right_odd = total_odd - pre_odd - v
    end

    new_even = left_even + right_odd
    new_odd = left_odd + right_even
    ans += 1 if new_even == new_odd

    if i.even?
      pre_even += v
    else
      pre_odd += v
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def waysToMakeFair(nums: Array[Int]): Int = {
        val n = nums.length
        val preEven = new Array[Long](n + 1)
        val preOdd = new Array[Long](n + 1)

        for (i <- 0 until n) {
            preEven(i + 1) = preEven(i) + (if ((i & 1) == 0) nums(i).toLong else 0L)
            preOdd(i + 1) = preOdd(i) + (if ((i & 1) == 1) nums(i).toLong else 0L)
        }

        val totalEven = preEven(n)
        val totalOdd = preOdd(n)

        var count = 0
        for (i <- 0 until n) {
            val evenBefore = preEven(i)
            val oddBefore = preOdd(i)
            val evenAfterOriginal = totalEven - preEven(i + 1)
            val oddAfterOriginal = totalOdd - preOdd(i + 1)

            val newEven = evenBefore + oddAfterOriginal
            val newOdd = oddBefore + evenAfterOriginal

            if (newEven == newOdd) count += 1
        }

        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn ways_to_make_fair(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut pre_even = vec![0i64; n + 1];
        let mut pre_odd = vec![0i64; n + 1];

        for i in 0..n {
            pre_even[i + 1] = pre_even[i];
            pre_odd[i + 1] = pre_odd[i];
            if i % 2 == 0 {
                pre_even[i + 1] += nums[i] as i64;
            } else {
                pre_odd[i + 1] += nums[i] as i64;
            }
        }

        let total_even = pre_even[n];
        let total_odd = pre_odd[n];
        let mut ans = 0i32;

        for i in 0..n {
            let even_before = pre_even[i];
            let odd_before = pre_odd[i];

            // After removal, elements after i shift parity
            let even_after = even_before + (total_odd - pre_odd[i + 1]);
            let odd_after = odd_before + (total_even - pre_even[i + 1]);

            if even_after == odd_after {
                ans += 1;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (ways-to-make-fair nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (prefE (make-vector (+ n 1) 0))
         (prefO (make-vector (+ n 1) 0)))
    ;; build prefix sums
    (for ([i (in-range n)])
      (let* ((prevE (vector-ref prefE i))
             (prevO (vector-ref prefO i))
             (val   (vector-ref arr i))
             (next  (+ i 1)))
        (if (even? i)
            (begin
              (vector-set! prefE next (+ prevE val))
              (vector-set! prefO next prevO))
            (begin
              (vector-set! prefE next prevE)
              (vector-set! prefO next (+ prevO val))))))
    (let ((totalE (vector-ref prefE n))
          (totalO (vector-ref prefO n)))
      (let loop ((i 0) (cnt 0))
        (if (= i n)
            cnt
            (let* ((evenBefore (vector-ref prefE i))
                   (oddBefore  (vector-ref prefO i))
                   (evenAfter (- totalE (vector-ref prefE (+ i 1))))
                   (oddAfter  (- totalO (vector-ref prefO (+ i 1))))
                   (newEven   (+ evenBefore oddAfter))
                   (newOdd    (+ oddBefore evenAfter)))
              (loop (+ i 1)
                    (if (= newEven newOdd) (+ cnt 1) cnt))))))))
```

## Erlang

```erlang
-module(solution).
-export([ways_to_make_fair/1]).

ways_to_make_fair(Nums) ->
    Len = length(Nums),
    Indices = lists:seq(0, Len - 1),
    PairList = lists:zip(Indices, Nums),
    {TotalEven, TotalOdd} = lists:foldl(
        fun({Idx, Val}, {E, O}) ->
            case Idx rem 2 of
                0 -> {E + Val, O};
                _ -> {E, O + Val}
            end
        end,
        {0, 0},
        PairList),
    loop(PairList, 0, 0, TotalEven, TotalOdd, 0).

loop([], _PreE, _PreO, _TotE, _TotO, Count) ->
    Count;
loop([{Idx, Val} | Rest], PreE, PreO, TotE, TotO, Count) ->
    PostE = TotE - PreE - (case Idx rem 2 of 0 -> Val; _ -> 0 end),
    PostO = TotO - PreO - (case Idx rem 2 of 1 -> Val; _ -> 0 end),
    NewEven = PreE + PostO,
    NewOdd = PreO + PostE,
    Count1 = case NewEven == NewOdd of
        true -> Count + 1;
        false -> Count
    end,
    PreE1 = case Idx rem 2 of 0 -> PreE + Val; _ -> PreE end,
    PreO1 = case Idx rem 2 of 1 -> PreO + Val; _ -> PreO end,
    loop(Rest, PreE1, PreO1, TotE, TotO, Count1).
```

## Elixir

```elixir
defmodule Solution do
  @spec ways_to_make_fair(nums :: [integer]) :: integer
  def ways_to_make_fair(nums) do
    {total_even, total_odd} =
      nums
      |> Enum.with_index()
      |> Enum.reduce({0, 0}, fn {v, i}, {e, o} ->
        if rem(i, 2) == 0, do: {e + v, o}, else: {e, o + v}
      end)

    {ans, _left_even, _left_odd} =
      nums
      |> Enum.with_index()
      |> Enum.reduce({0, 0, 0}, fn {v, i}, {cnt, left_even, left_odd} ->
        if rem(i, 2) == 0 do
          right_even = total_even - left_even - v
          right_odd = total_odd - left_odd
          new_cnt = if left_even + right_odd == left_odd + right_even, do: cnt + 1, else: cnt
          {new_cnt, left_even + v, left_odd}
        else
          right_even = total_even - left_even
          right_odd = total_odd - left_odd - v
          new_cnt = if left_even + right_odd == left_odd + right_even, do: cnt + 1, else: cnt
          {new_cnt, left_even, left_odd + v}
        end
      end)

    ans
  end
end
```
