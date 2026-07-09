# 1423. Maximum Points You Can Obtain from Cards

## Cpp

```cpp
class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int n = cardPoints.size();
        long long total = 0;
        for (int p : cardPoints) total += p;
        if (k == n) return (int)total;
        
        int windowSize = n - k;
        long long curSum = 0;
        for (int i = 0; i < windowSize; ++i) curSum += cardPoints[i];
        long long minSub = curSum;
        for (int i = windowSize; i < n; ++i) {
            curSum += cardPoints[i] - cardPoints[i - windowSize];
            if (curSum < minSub) minSub = curSum;
        }
        return (int)(total - minSub);
    }
};
```

## Java

```java
class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length;
        int total = 0;
        for (int p : cardPoints) total += p;
        if (k == n) return total;

        int windowSize = n - k;
        int curSum = 0;
        for (int i = 0; i < windowSize; i++) {
            curSum += cardPoints[i];
        }
        int minSum = curSum;

        for (int i = windowSize; i < n; i++) {
            curSum += cardPoints[i] - cardPoints[i - windowSize];
            if (curSum < minSum) minSum = curSum;
        }

        return total - minSum;
    }
}
```

## Python

```python
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        total = sum(cardPoints)
        if k == n:
            return total
        window_len = n - k
        curr = sum(cardPoints[:window_len])
        min_sum = curr
        for i in range(window_len, n):
            curr += cardPoints[i] - cardPoints[i - window_len]
            if curr < min_sum:
                min_sum = curr
        return total - min_sum
```

## Python3

```python
from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window_len = n - k
        if window_len == 0:
            return total
        
        current_sum = sum(cardPoints[:window_len])
        min_subarray_sum = current_sum
        
        for i in range(window_len, n):
            current_sum += cardPoints[i] - cardPoints[i - window_len]
            if current_sum < min_subarray_sum:
                min_subarray_sum = current_sum
        
        return total - min_subarray_sum
```

## C

```c
int maxScore(int* cardPoints, int cardPointsSize, int k) {
    long long total = 0;
    for (int i = 0; i < cardPointsSize; ++i) {
        total += cardPoints[i];
    }
    if (k == cardPointsSize) return (int)total;

    int window = cardPointsSize - k;
    long long cur = 0;
    for (int i = 0; i < window; ++i) {
        cur += cardPoints[i];
    }
    long long minSum = cur;

    for (int i = window; i < cardPointsSize; ++i) {
        cur += cardPoints[i];
        cur -= cardPoints[i - window];
        if (cur < minSum) minSum = cur;
    }

    return (int)(total - minSum);
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxScore(int[] cardPoints, int k)
    {
        int n = cardPoints.Length;
        long total = 0;
        foreach (int p in cardPoints) total += p;

        if (k == n) return (int)total;

        int windowSize = n - k;
        long windowSum = 0;
        for (int i = 0; i < windowSize; i++)
            windowSum += cardPoints[i];

        long minWindow = windowSum;
        for (int i = windowSize; i < n; i++)
        {
            windowSum += cardPoints[i] - cardPoints[i - windowSize];
            if (windowSum < minWindow) minWindow = windowSum;
        }

        return (int)(total - minWindow);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} cardPoints
 * @param {number} k
 * @return {number}
 */
var maxScore = function(cardPoints, k) {
    const n = cardPoints.length;
    let total = 0;
    for (let v of cardPoints) total += v;
    if (k === n) return total;

    const windowSize = n - k;
    let curSum = 0;
    for (let i = 0; i < windowSize; ++i) {
        curSum += cardPoints[i];
    }
    let minSum = curSum;

    for (let i = windowSize; i < n; ++i) {
        curSum += cardPoints[i] - cardPoints[i - windowSize];
        if (curSum < minSum) minSum = curSum;
    }

    return total - minSum;
};
```

## Typescript

```typescript
function maxScore(cardPoints: number[], k: number): number {
    const n = cardPoints.length;
    if (k >= n) {
        let sumAll = 0;
        for (const v of cardPoints) sumAll += v;
        return sumAll;
    }

    let total = 0;
    for (const v of cardPoints) total += v;

    const windowSize = n - k;
    let curr = 0;
    for (let i = 0; i < windowSize; i++) {
        curr += cardPoints[i];
    }
    let minSum = curr;

    for (let i = windowSize; i < n; i++) {
        curr += cardPoints[i] - cardPoints[i - windowSize];
        if (curr < minSum) minSum = curr;
    }

    return total - minSum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $cardPoints
     * @param Integer $k
     * @return Integer
     */
    function maxScore($cardPoints, $k) {
        $n = count($cardPoints);
        $total = array_sum($cardPoints);
        if ($k >= $n) {
            return $total;
        }
        $windowSize = $n - $k;
        $currSum = 0;
        for ($i = 0; $i < $windowSize; $i++) {
            $currSum += $cardPoints[$i];
        }
        $minSum = $currSum;
        for ($i = $windowSize; $i < $n; $i++) {
            $currSum += $cardPoints[$i] - $cardPoints[$i - $windowSize];
            if ($currSum < $minSum) {
                $minSum = $currSum;
            }
        }
        return $total - $minSum;
    }
}
```

## Swift

```swift
class Solution {
    func maxScore(_ cardPoints: [Int], _ k: Int) -> Int {
        let n = cardPoints.count
        if k >= n { return cardPoints.reduce(0, +) }
        let windowSize = n - k
        
        var total = 0
        for v in cardPoints { total += v }
        
        var currentSum = 0
        for i in 0..<windowSize {
            currentSum += cardPoints[i]
        }
        var minSum = currentSum
        
        for i in windowSize..<n {
            currentSum += cardPoints[i] - cardPoints[i - windowSize]
            if currentSum < minSum { minSum = currentSum }
        }
        
        return total - minSum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxScore(cardPoints: IntArray, k: Int): Int {
        val n = cardPoints.size
        if (k == n) {
            var sumAll = 0L
            for (v in cardPoints) sumAll += v
            return sumAll.toInt()
        }
        var total = 0L
        for (v in cardPoints) total += v

        val windowSize = n - k
        var curSum = 0L
        for (i in 0 until windowSize) {
            curSum += cardPoints[i]
        }
        var minSum = curSum

        for (i in windowSize until n) {
            curSum += cardPoints[i].toLong() - cardPoints[i - windowSize].toLong()
            if (curSum < minSum) minSum = curSum
        }

        return (total - minSum).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxScore(List<int> cardPoints, int k) {
    int n = cardPoints.length;
    int total = 0;
    for (int p in cardPoints) total += p;
    if (k >= n) return total;

    int windowSize = n - k;
    int current = 0;
    for (int i = 0; i < windowSize; ++i) {
      current += cardPoints[i];
    }
    int minSum = current;

    for (int i = windowSize; i < n; ++i) {
      current += cardPoints[i] - cardPoints[i - windowSize];
      if (current < minSum) minSum = current;
    }

    return total - minSum;
  }
}
```

## Golang

```go
func maxScore(cardPoints []int, k int) int {
    n := len(cardPoints)
    total := 0
    for _, v := range cardPoints {
        total += v
    }
    if k == n {
        return total
    }
    windowSize := n - k
    cur := 0
    for i := 0; i < windowSize; i++ {
        cur += cardPoints[i]
    }
    minSum := cur
    for i := windowSize; i < n; i++ {
        cur += cardPoints[i] - cardPoints[i-windowSize]
        if cur < minSum {
            minSum = cur
        }
    }
    return total - minSum
}
```

## Ruby

```ruby
def max_score(card_points, k)
  n = card_points.length
  total = card_points.sum
  window_len = n - k
  return total if window_len == 0

  curr = card_points[0...window_len].sum
  min_sum = curr

  (window_len...n).each do |i|
    curr += card_points[i] - card_points[i - window_len]
    min_sum = [min_sum, curr].min
  end

  total - min_sum
end
```

## Scala

```scala
object Solution {
    def maxScore(cardPoints: Array[Int], k: Int): Int = {
        val n = cardPoints.length
        if (k >= n) return cardPoints.sum
        var total: Long = 0L
        for (v <- cardPoints) total += v

        val windowSize = n - k
        var curr: Long = 0L
        for (i <- 0 until windowSize) {
            curr += cardPoints(i)
        }
        var minSum = curr
        var left = 0
        for (right <- windowSize until n) {
            curr += cardPoints(right)
            curr -= cardPoints(left)
            left += 1
            if (curr < minSum) minSum = curr
        }
        (total - minSum).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_score(card_points: Vec<i32>, k: i32) -> i32 {
        let n = card_points.len();
        let k_usize = k as usize;
        if k_usize == n {
            return card_points.iter().sum();
        }
        let window_len = n - k_usize;
        let total: i32 = card_points.iter().sum();

        let mut curr_sum: i32 = card_points.iter().take(window_len).sum();
        let mut min_sum = curr_sum;

        for i in window_len..n {
            curr_sum += card_points[i];
            curr_sum -= card_points[i - window_len];
            if curr_sum < min_sum {
                min_sum = curr_sum;
            }
        }

        total - min_sum
    }
}
```

## Racket

```racket
(define/contract (max-score cardPoints k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length cardPoints))
         (arr (list->vector cardPoints))
         (total
          (let loop ((i 0) (sum 0))
            (if (= i n)
                sum
                (loop (+ i 1) (+ sum (vector-ref arr i))))))
         (window-size (- n k)))
    (if (= window-size 0)
        total
        (let* ((initial-sum
                (let loop ((i 0) (sum 0))
                  (if (= i window-size)
                      sum
                      (loop (+ i 1) (+ sum (vector-ref arr i))))))
               (min-sum
                (let loop ((i 0) (curr initial-sum) (best initial-sum))
                  (if (= i (- n window-size))
                      best
                      (let* ((out (vector-ref arr i))
                             (in (vector-ref arr (+ i window-size)))
                             (new-sum (+ (- curr out) in))
                             (new-best (min best new-sum)))
                        (loop (+ i 1) new-sum new-best))))))
          (- total min-sum)))))
```

## Erlang

```erlang
-module(solution).
-export([max_score/2]).

-spec max_score(CardPoints :: [integer()], K :: integer()) -> integer().
max_score(CardPoints, K) ->
    Total = lists:foldl(fun(X, Acc) -> X + Acc end, 0, CardPoints),
    N = length(CardPoints),
    W = N - K,
    case W of
        0 -> Total;
        _ ->
            Tuple = list_to_tuple(CardPoints),
            InitSum = init_sum(1, W, Tuple, 0),
            MaxStart = N - W + 1,
            {_, MinSum} = slide(2, MaxStart, W, Tuple, InitSum, InitSum),
            Total - MinSum
    end.

init_sum(I, End, Tuple, Acc) when I > End ->
    Acc;
init_sum(I, End, Tuple, Acc) ->
    init_sum(I + 1, End, Tuple, Acc + element(I, Tuple)).

slide(Start, MaxStart, _W, _Tuple, PrevSum, MinSoFar) when Start > MaxStart ->
    {PrevSum, MinSoFar};
slide(Start, MaxStart, W, Tuple, PrevSum, MinSoFar) ->
    OutIdx = Start - 1,
    InIdx = Start + W - 1,
    NewSum = PrevSum - element(OutIdx, Tuple) + element(InIdx, Tuple),
    NewMin = if NewSum < MinSoFar -> NewSum; true -> MinSoFar end,
    slide(Start + 1, MaxStart, W, Tuple, NewSum, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_score(card_points :: [integer], k :: integer) :: integer
  def max_score(card_points, k) do
    n = length(card_points)
    total = Enum.sum(card_points)
    window_len = n - k

    if window_len == 0 do
      total
    else
      arr = List.to_tuple(card_points)

      init_sum =
        0..(window_len - 1)
        |> Enum.reduce(0, fn i, acc -> acc + elem(arr, i) end)

      {_, min_sum} =
        1..(n - window_len)
        |> Enum.reduce({init_sum, init_sum}, fn i, {curr, min_sofar} ->
          out_val = elem(arr, i - 1)
          in_val = elem(arr, i + window_len - 1)
          new_curr = curr - out_val + in_val
          new_min = if new_curr < min_sofar, do: new_curr, else: min_sofar
          {new_curr, new_min}
        end)

      total - min_sum
    end
  end
end
```
