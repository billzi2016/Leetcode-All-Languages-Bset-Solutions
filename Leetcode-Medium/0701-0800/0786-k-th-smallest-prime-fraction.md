# 0786. K-th Smallest Prime Fraction

## Cpp

```cpp
class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        int n = arr.size();
        int bestNumIdx = 0, bestDenIdx = 1;
        double left = 0.0, right = 1.0;
        for (int iter = 0; iter < 60; ++iter) { // sufficient precision
            double mid = (left + right) / 2.0;
            int cnt = 0;
            int i = 0;
            int curNumIdx = 0, curDenIdx = 1;
            for (int j = 1; j < n; ++j) {
                while (i < j && static_cast<double>(arr[i]) / arr[j] <= mid) {
                    ++i;
                }
                cnt += i;
                if (i > 0) {
                    // candidate fraction arr[i-1]/arr[j]
                    if (static_cast<double>(arr[i - 1]) / arr[j] >
                        static_cast<double>(arr[curNumIdx]) / arr[curDenIdx]) {
                        curNumIdx = i - 1;
                        curDenIdx = j;
                    }
                }
            }
            if (cnt == k) {
                return {arr[curNumIdx], arr[curDenIdx]};
            }
            if (cnt < k) {
                left = mid;
            } else {
                right = mid;
                bestNumIdx = curNumIdx;
                bestDenIdx = curDenIdx;
            }
        }
        return {arr[bestNumIdx], arr[bestDenIdx]};
    }
};
```

## Java

```java
class Solution {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        int n = arr.length;
        int bestNum = 0, bestDen = 1;
        double lo = 0.0, hi = 1.0;
        // binary search on the value of the fraction
        while (hi - lo > 1e-12) { // sufficient precision
            double mid = (lo + hi) / 2.0;
            int count = 0;
            int maxNum = 0, maxDen = 1;
            int j = n - 1; // denominator index
            for (int i = 0; i < n; ++i) {
                while (j > i && (double) arr[i] / arr[j] > mid) {
                    --j;
                }
                if (j == i) break; // no valid denominator for this numerator
                count += j - i;
                // keep the largest fraction <= mid seen so far
                if ((long) arr[i] * maxDen > (long) maxNum * arr[j]) {
                    maxNum = arr[i];
                    maxDen = arr[j];
                }
            }
            if (count < k) {
                lo = mid;
            } else {
                hi = mid;
                bestNum = maxNum;
                bestDen = maxDen;
            }
        }
        return new int[]{bestNum, bestDen};
    }
}
```

## Python

```python
class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(arr)
        left, right = 0.0, 1.0
        ans = [0, 1]

        for _ in range(40):  # sufficient precision
            mid = (left + right) / 2.0
            count = 0
            best_num, best_den = 0, 1
            i = 0

            for j in range(1, n):
                while i < j and arr[i] / arr[j] <= mid:
                    i += 1
                count += i
                if i > 0:
                    # candidate fraction is arr[i-1] / arr[j]
                    if best_num * arr[j] < arr[i - 1] * best_den:
                        best_num, best_den = arr[i - 1], arr[j]

            if count < k:
                left = mid
            else:
                right = mid
                ans = [best_num, best_den]

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0.0, 1.0
        ans_num, ans_den = 0, 1

        for _ in range(60):  # sufficient precision
            mid = (left + right) / 2.0
            count = 0
            i = 0
            best_numer = 0
            best_denom = 1

            for j in range(1, n):
                while i < j and arr[i] / arr[j] <= mid:
                    i += 1
                if i > 0:
                    count += i
                    # candidate fraction arr[i-1] / arr[j]
                    if best_numer * arr[j] < arr[i - 1] * best_denom:
                        best_numer = arr[i - 1]
                        best_denom = arr[j]

            if count >= k:
                right = mid
                ans_num, ans_den = best_numer, best_denom
            else:
                left = mid

        return [ans_num, ans_den]
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* kthSmallestPrimeFraction(int* arr, int arrSize, int k, int* returnSize) {
    int n = arrSize;
    double lo = 0.0, hi = 1.0;
    int ans_i = 0, ans_j = 1;   // default answer
    
    for (int iter = 0; iter < 60; ++iter) {   // enough precision
        double mid = (lo + hi) * 0.5;
        int cnt = 0;
        int best_i = -1, best_j = -1;
        int j = n - 1;
        
        for (int i = 0; i < n; ++i) {
            while (j > i && (double)arr[i] > mid * arr[j]) {
                --j;
            }
            if (j == i) break;               // no valid denominator
            cnt += (j - i);
            
            if (best_i == -1 || (long long)arr[i] * arr[best_j] > (long long)arr[best_i] * arr[j]) {
                best_i = i;
                best_j = j;
            }
        }
        
        if (cnt >= k) {          // mid is large enough, keep it and record candidate
            hi = mid;
            ans_i = best_i;
            ans_j = best_j;
        } else {                 // need larger fractions
            lo = mid;
        }
    }
    
    int* res = (int*)malloc(2 * sizeof(int));
    res[0] = arr[ans_i];
    res[1] = arr[ans_j];
    *returnSize = 2;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] KthSmallestPrimeFraction(int[] arr, int k)
    {
        int n = arr.Length;
        double lo = 0.0, hi = 1.0;
        int ansNum = 0, ansDen = 1;

        for (int iter = 0; iter < 60; ++iter)
        {
            double mid = (lo + hi) / 2.0;
            int count = 0;
            int bestI = 0, bestJ = 1;
            int j = n - 1;

            for (int i = 0; i < n - 1; ++i)
            {
                while (j > i && (double)arr[i] / arr[j] > mid)
                    --j;

                if (j == i) break;

                count += n - j;

                // keep the largest fraction <= mid
                if ((long)arr[i] * arr[bestJ] > (long)arr[bestI] * arr[j])
                {
                    bestI = i;
                    bestJ = j;
                }
            }

            if (count < k)
                lo = mid;
            else
            {
                hi = mid;
                ansNum = arr[bestI];
                ansDen = arr[bestJ];
            }
        }

        return new int[] { ansNum, ansDen };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number[]}
 */
var kthSmallestPrimeFraction = function(arr, k) {
    const n = arr.length;
    let left = 0, right = 1;
    let bestNum = 0, bestDen = 1;

    for (let iter = 0; iter < 40; ++iter) { // sufficient precision
        const mid = (left + right) / 2;
        let cnt = 0;
        let curNum = 0, curDen = 1;
        let j = n - 1;

        for (let i = 0; i < n - 1; ++i) {
            while (j > i && arr[i] / arr[j] > mid) {
                --j;
            }
            if (j === i) break;
            cnt += n - j - 1; // fractions with denominator > j are <= mid
            // candidate fraction arr[i]/arr[j] is the largest <= mid for this i
            if (arr[i] * curDen > curNum * arr[j]) {
                curNum = arr[i];
                curDen = arr[j];
            }
        }

        if (cnt < k) {
            left = mid;
        } else {
            right = mid;
            bestNum = curNum;
            bestDen = curDen;
        }
    }

    return [bestNum, bestDen];
};
```

## Typescript

```typescript
function kthSmallestPrimeFraction(arr: number[], k: number): number[] {
    const n = arr.length;
    let left = 0.0, right = 1.0;
    let bestNum = 0, bestDen = 1;

    for (let iter = 0; iter < 40; ++iter) {
        const mid = (left + right) / 2;
        let count = 0;
        let maxNum = 0, maxDen = 1;
        let i = 0;

        for (let j = 1; j < n; ++j) {
            while (i < j && arr[i] / arr[j] <= mid) {
                if (arr[i] * maxDen > maxNum * arr[j]) {
                    maxNum = arr[i];
                    maxDen = arr[j];
                }
                i++;
            }
            count += i;
        }

        if (count < k) {
            left = mid;
        } else {
            right = mid;
            bestNum = maxNum;
            bestDen = maxDen;
        }
    }

    return [bestNum, bestDen];
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer[]
     */
    function kthSmallestPrimeFraction($arr, $k) {
        $n = count($arr);
        $low = 0.0;
        $high = 1.0;
        $bestNum = 0;
        $bestDen = 1;

        for ($iter = 0; $iter < 40; $iter++) { // sufficient precision
            $mid = ($low + $high) / 2.0;
            $count = 0;
            $maxNum = 0;
            $maxDen = 1;
            $i = 0;

            for ($j = 1; $j < $n; $j++) {
                while ($i < $j && $arr[$i] / $arr[$j] <= $mid) {
                    $i++;
                }
                $count += $i;
                if ($i > 0) {
                    $num = $arr[$i - 1];
                    $den = $arr[$j];
                    // keep the largest fraction <= mid
                    if ($maxNum * $den < $num * $maxDen) {
                        $maxNum = $num;
                        $maxDen = $den;
                    }
                }
            }

            if ($count == $k) {
                return [$maxNum, $maxDen];
            } elseif ($count < $k) {
                $low = $mid;
            } else {
                $high = $mid;
                $bestNum = $maxNum;
                $bestDen = $maxDen;
            }
        }

        return [$bestNum, $bestDen];
    }
}
```

## Swift

```swift
class Solution {
    func kthSmallestPrimeFraction(_ arr: [Int], _ k: Int) -> [Int] {
        let n = arr.count
        var low = 0.0
        var high = 1.0
        var ansNum = 0
        var ansDen = 1
        
        for _ in 0..<60 { // sufficient precision
            let mid = (low + high) / 2.0
            var count = 0
            var maxNum = 0
            var maxDen = 1
            var j = 1
            
            for i in 0..<(n - 1) {
                if j <= i { j = i + 1 }
                while j < n && Double(arr[i]) / Double(arr[j]) > mid {
                    j += 1
                }
                if j == n { break }
                count += (n - j)
                
                let curNum = arr[i]
                let curDen = arr[j]
                if Double(curNum) / Double(curDen) > Double(maxNum) / Double(maxDen) {
                    maxNum = curNum
                    maxDen = curDen
                }
            }
            
            if count < k {
                low = mid
            } else {
                high = mid
                ansNum = maxNum
                ansDen = maxDen
            }
        }
        
        return [ansNum, ansDen]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kthSmallestPrimeFraction(arr: IntArray, k: Int): IntArray {
        val n = arr.size
        var low = 0.0
        var high = 1.0
        var ansNum = 0
        var ansDen = 1

        repeat(60) { // sufficient for double precision
            val mid = (low + high) / 2.0
            var count = 0
            var bestNum = 0
            var bestDen = 1
            var i = -1
            for (j in 1 until n) {
                while (i + 1 < j && arr[i + 1].toDouble() / arr[j] <= mid) {
                    i++
                }
                if (i >= 0) {
                    count += i + 1
                    // update best fraction <= mid
                    if (arr[i] * bestDen > bestNum * arr[j]) {
                        bestNum = arr[i]
                        bestDen = arr[j]
                    }
                }
            }

            if (count < k) {
                low = mid
            } else {
                ansNum = bestNum
                ansDen = bestDen
                high = mid
            }
        }
        return intArrayOf(ansNum, ansDen)
    }
}
```

## Dart

```dart
class Solution {
  List<int> kthSmallestPrimeFraction(List<int> arr, int k) {
    int n = arr.length;
    double low = 0.0, high = 1.0;
    int ansNum = 0, ansDen = 1;

    while (high - low > 1e-12) {
      double mid = (low + high) / 2.0;
      int count = 0;
      int i = 0;
      ansNum = 0;
      ansDen = 1;

      for (int j = 1; j < n; ++j) {
        while (i < j && arr[i].toDouble() < mid * arr[j]) {
          i++;
        }
        count += i;
        if (i > 0) {
          int numIdx = i - 1;
          // keep the largest fraction <= mid
          if (ansNum == 0 || arr[numIdx] * ansDen > ansNum * arr[j]) {
            ansNum = arr[numIdx];
            ansDen = arr[j];
          }
        }
      }

      if (count == k) {
        break;
      } else if (count < k) {
        low = mid;
      } else {
        high = mid;
      }
    }

    return [ansNum, ansDen];
  }
}
```

## Golang

```go
func kthSmallestPrimeFraction(arr []int, k int) []int {
    n := len(arr)
    lo, hi := 0.0, 1.0
    var ansNum, ansDen int = 0, 1
    for iter := 0; iter < 60; iter++ {
        mid := (lo + hi) / 2.0
        cnt := 0
        bestNum, bestDen := 0, 1
        j := 1
        for i := 0; i < n-1; i++ {
            if j <= i {
                j = i + 1
            }
            for j < n && float64(arr[i])/float64(arr[j]) > mid {
                j++
            }
            if j == n {
                break
            }
            cnt += n - j
            if bestNum*arr[j] < arr[i]*bestDen {
                bestNum = arr[i]
                bestDen = arr[j]
            }
        }
        if cnt == k {
            return []int{bestNum, bestDen}
        } else if cnt < k {
            lo = mid
        } else {
            hi = mid
            ansNum = bestNum
            ansDen = bestDen
        }
    }
    return []int{ansNum, ansDen}
}
```

## Ruby

```ruby
def kth_smallest_prime_fraction(arr, k)
  n = arr.length
  left = 0.0
  right = 1.0
  ans_num = 0
  ans_den = 1

  while right - left > 1e-12
    mid = (left + right) / 2.0
    count = 0
    max_num = 0
    max_den = 1
    i = -1

    (1...n).each do |j|
      while i + 1 < j && arr[i + 1].to_f / arr[j] <= mid
        i += 1
      end
      if i >= 0
        count += i + 1
        # keep the largest fraction <= mid
        if max_num * arr[j] < arr[i] * max_den
          max_num = arr[i]
          max_den = arr[j]
        end
      end
    end

    if count >= k
      ans_num = max_num
      ans_den = max_den
      right = mid
    else
      left = mid
    end
  end

  [ans_num, ans_den]
end
```

## Scala

```scala
object Solution {
    def kthSmallestPrimeFraction(arr: Array[Int], k: Int): Array[Int] = {
        var left = 0.0
        var right = 1.0
        var ansNum = 0
        var ansDen = 1

        for (_ <- 0 until 60) { // sufficient precision
            val mid = (left + right) / 2.0
            var count = 0
            var i = 0
            var bestNum = 0
            var bestDen = 1

            var j = 1
            while (j < arr.length) {
                while (i < j && arr(i).toDouble / arr(j) <= mid) {
                    i += 1
                }
                val cnt = i
                count += cnt
                if (cnt > 0) {
                    val num = arr(i - 1)
                    val den = arr(j)
                    if (bestNum.toLong * den < num.toLong * bestDen) {
                        bestNum = num
                        bestDen = den
                    }
                }
                j += 1
            }

            if (count < k) {
                left = mid
            } else {
                right = mid
                ansNum = bestNum
                ansDen = bestDen
            }
        }

        Array(ansNum, ansDen)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn kth_smallest_prime_fraction(arr: Vec<i32>, k: i32) -> Vec<i32> {
        let n = arr.len();
        let mut low = 0.0_f64;
        let mut high = 1.0_f64;
        let (mut ans_num, mut ans_den) = (0_i32, 1_i32);
        for _ in 0..60 {
            let mid = (low + high) / 2.0;
            let mut count: usize = 0;
            let mut i: usize = 0;
            let mut best_num = 0_i32;
            let mut best_den = 1_i32;
            for j in 1..n {
                while i < j && (arr[i] as f64) / (arr[j] as f64) <= mid {
                    i += 1;
                }
                count += i;
                if i > 0 {
                    let num = arr[i - 1];
                    let den = arr[j];
                    // compare num/den with best_num/best_den
                    if (num as i64) * (best_den as i64) > (best_num as i64) * (den as i64) {
                        best_num = num;
                        best_den = den;
                    }
                }
            }
            if count < k as usize {
                low = mid;
            } else {
                ans_num = best_num;
                ans_den = best_den;
                high = mid;
            }
        }
        vec![ans_num, ans_den]
    }
}
```

## Racket

```racket
(define/contract (kth-smallest-prime-fraction arr k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((v (list->vector arr))
         (n (vector-length v)))
    (let loop ((left 0.0) (right 1.0) (best-num 0) (best-den 1))
      (if (< (- right left) 1e-12)
          (list best-num best-den)
          (let* ((mid (/ (+ left right) 2.0)))
            (let ((count 0)
                  (max-num 0)
                  (max-den 1)
                  (i 0))
              (for ([j (in-range 1 n)])
                ;; advance i while fraction <= mid
                (let loop-i ()
                  (when (and (< i j)
                             (<= (/ (vector-ref v i) (vector-ref v j)) mid))
                    (set! i (+ i 1))
                    (loop-i)))
                (set! count (+ count i))
                (when (> i 0)
                  (let ((num (vector-ref v (- i 1)))
                        (den (vector-ref v j)))
                    (when (> (* num max-den) (* max-num den))
                      (set! max-num num)
                      (set! max-den den)))))
              (if (< count k)
                  (loop mid right best-num best-den)   ; move left
                  (loop left mid max-num max-den)))))))))
```

## Erlang

```erlang
-module(solution).
-export([kth_smallest_prime_fraction/2]).

-spec kth_smallest_prime_fraction(Arr :: [integer()], K :: integer()) -> [integer()].
kth_smallest_prime_fraction(Arr, K) ->
    ArrTuple = list_to_tuple(Arr),
    N = tuple_size(ArrTuple),
    {Num, Den} = binary_loop(60, 0.0, 1.0, K, ArrTuple, N, 0, 1),
    [Num, Den].

binary_loop(0, _Left, _Right, _K, _ArrTuple, _N, BestNum, BestDen) ->
    {BestNum, BestDen};
binary_loop(Iter, Left, Right, K, ArrTuple, N, BestNum, BestDen) when Iter > 0 ->
    Mid = (Left + Right) / 2,
    {Count, CurBestNum, CurBestDen} = count_best(1, -1, 0, 0, 1, ArrTuple, N, Mid),
    if Count < K ->
        binary_loop(Iter-1, Mid, Right, K, ArrTuple, N, BestNum, BestDen);
       true ->
        binary_loop(Iter-1, Left, Mid, K, ArrTuple, N, CurBestNum, CurBestDen)
    end.

count_best(J, _I, CountAcc, BestNum, BestDen, _ArrTuple, N, _Mid) when J >= N ->
    {CountAcc, BestNum, BestDen};
count_best(J, I, CountAcc, BestNum, BestDen, ArrTuple, N, Mid) ->
    I1 = advance_i(I, J, Mid, ArrTuple),
    NewCount = CountAcc + (I1 + 1),
    {NewBestNum, NewBestDen} =
        if I1 >= 0 ->
            Num = element(I1+1, ArrTuple),
            Den = element(J+1, ArrTuple),
            case BestNum * Den < Num * BestDen of
                true -> {Num, Den};
                false -> {BestNum, BestDen}
            end;
           true ->
            {BestNum, BestDen}
        end,
    count_best(J+1, I1, NewCount, NewBestNum, NewBestDen, ArrTuple, N, Mid).

advance_i(I, J, Mid, ArrTuple) ->
    case ((I + 1) < J) andalso (element(I + 2, ArrTuple) / element(J + 1, ArrTuple) =< Mid) of
        true -> advance_i(I + 1, J, Mid, ArrTuple);
        false -> I
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec kth_smallest_prime_fraction(arr :: [integer], k :: integer) :: [integer]
  def kth_smallest_prime_fraction(arr, k) do
    {num, den} = binary_search(arr, k, 0.0, 1.0, 60, {0, 1})
    [num, den]
  end

  defp binary_search(_arr, _k, _left, _right, 0, acc), do: acc

  defp binary_search(arr, k, left, right, iter, {_ans_num, _ans_den} = acc) do
    mid = (left + right) / 2.0
    {cnt, best_num, best_den} = count_less_than_mid(arr, mid)

    if cnt >= k do
      binary_search(arr, k, left, mid, iter - 1, {best_num, best_den})
    else
      binary_search(arr, k, mid, right, iter - 1, acc)
    end
  end

  defp count_less_than_mid(arr, mid) do
    a = List.to_tuple(arr)
    n = tuple_size(a)

    # iterate denominators j from 1 to n-1
    {total_cnt, best_num, best_den, _i} =
      Enum.reduce(1..(n - 1), {0, 0, 1, 0}, fn j,
                                            {cnt_acc, bn_acc, bd_acc, i_ptr} ->
        i_new = advance_i(a, i_ptr, j, mid)

        cnt_new = cnt_acc + i_new

        {bn_new, bd_new} =
          if i_new > 0 do
            num = elem(a, i_new - 1)
            den = elem(a, j)

            if num * bd_acc > bn_acc * den do
              {num, den}
            else
              {bn_acc, bd_acc}
            end
          else
            {bn_acc, bd_acc}
          end

        {cnt_new, bn_new, bd_new, i_new}
      end)

    {total_cnt, best_num, best_den}
  end

  defp advance_i(a, i, j, mid) do
    if i < j and elem(a, i) < mid * elem(a, j) do
      advance_i(a, i + 1, j, mid)
    else
      i
    end
  end
end
```
