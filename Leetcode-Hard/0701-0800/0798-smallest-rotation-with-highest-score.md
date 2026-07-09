# 0798. Smallest Rotation with Highest Score

## Cpp

```cpp
class Solution {
public:
    int bestRotation(vector<int>& nums) {
        int n = nums.size();
        vector<int> diff(n, 0);
        int baseScore = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] <= i) ++baseScore;
            int start = (i - nums[i] + 1 + n) % n; // first rotation where this element becomes bad
            if (start <= i) {
                diff[start] -= 1;
                if (i + 1 < n) diff[i + 1] += 1;
            } else { // interval wraps around
                diff[0] -= 1;
                if (i + 1 < n) diff[i + 1] += 1;
                diff[start] -= 1;
            }
        }
        int bestIdx = 0;
        int maxScore = baseScore;
        int cur = baseScore;
        for (int k = 1; k < n; ++k) {
            cur += diff[k];
            if (cur > maxScore) {
                maxScore = cur;
                bestIdx = k;
            }
        }
        return bestIdx;
    }
};
```

## Java

```java
class Solution {
    public int bestRotation(int[] nums) {
        int n = nums.length;
        int[] diff = new int[n + 1];
        for (int i = 0; i < n; i++) {
            int val = nums[i];
            if (val == 0) continue; // no bad interval
            int start = i - val + 1;
            start %= n;
            if (start < 0) start += n;
            int end = i;
            if (start <= end) {
                diff[start] += 1;
                diff[end + 1] -= 1;
            } else {
                diff[0] += 1;
                diff[end + 1] -= 1;
                diff[start] += 1;
            }
        }
        int bestK = 0;
        int minBad = Integer.MAX_VALUE;
        int curBad = 0;
        for (int k = 0; k < n; k++) {
            curBad += diff[k];
            if (curBad < minBad) {
                minBad = curBad;
                bestK = k;
            }
        }
        return bestK;
    }
}
```

## Python

```python
class Solution(object):
    def bestRotation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        change = [0] * (n + 1)

        # initial score for k = 0
        base = 0
        for i, num in enumerate(nums):
            if num <= i:
                base += 1

            low = (i - num + 1) % n
            high = i

            if low <= high:
                change[low] -= 1
                change[high + 1] += 1
            else:
                # interval wraps around the end of the array
                change[0] -= 1
                change[high + 1] += 1
                change[low] -= 1

        best_score = base
        best_k = 0
        cur = base
        for k in range(1, n):
            cur += change[k]
            if cur > best_score:
                best_score = cur
                best_k = k

        return best_k
```

## Python3

```python
class Solution:
    def bestRotation(self, nums):
        n = len(nums)
        # initial score for k = 0
        score = sum(1 for i, v in enumerate(nums) if v <= i)

        change = [0] * n
        for i, v in enumerate(nums):
            lose = (i - v + 1) % n          # rotation where this element stops contributing
            gain = (i + 1) % n              # rotation where it starts contributing again
            change[lose] -= 1
            change[gain] += 1

        best_score = score
        best_k = 0
        cur = score
        for k in range(1, n):
            cur += change[k]
            if cur > best_score:
                best_score = cur
                best_k = k
        return best_k
```

## C

```c
int bestRotation(int* nums, int numsSize) {
    int n = numsSize;
    int *diff = (int*)calloc(n + 1, sizeof(int));
    for (int i = 0; i < n; ++i) {
        int v = nums[i];
        if (v == 0) continue;
        int low = i - v + 1;
        low %= n;
        if (low < 0) low += n;
        int high = i;
        if (low <= high) {
            diff[low] -= 1;
            diff[high + 1] += 1;
        } else {
            diff[0] -= 1;
            diff[high + 1] += 1;
            diff[low] -= 1;
            diff[n] += 1;
        }
    }
    int bestK = 0, maxScore = -1, cur = 0;
    for (int k = 0; k < n; ++k) {
        cur += diff[k];
        int score = n + cur;
        if (score > maxScore) {
            maxScore = score;
            bestK = k;
        }
    }
    free(diff);
    return bestK;
}
```

## Csharp

```csharp
public class Solution {
    public int BestRotation(int[] nums) {
        int n = nums.Length;
        int[] change = new int[n + 1];
        int baseScore = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] <= i) baseScore++;
            int low = i - nums[i] + 1;
            low %= n;
            if (low < 0) low += n;
            int high = i;
            if (low <= high) {
                change[low] -= 1;
                change[high + 1] += 1;
            } else {
                // interval wraps around
                change[0] -= 1;
                change[high + 1] += 1;
                change[low] -= 1;
            }
        }

        int maxScore = baseScore;
        int bestK = 0;
        int cur = baseScore;
        for (int k = 1; k < n; k++) {
            cur += change[k];
            if (cur > maxScore) {
                maxScore = cur;
                bestK = k;
            }
        }
        return bestK;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var bestRotation = function(nums) {
    const n = nums.length;
    // base score for k = 0
    let baseScore = 0;
    for (let i = 0; i < n; ++i) {
        if (nums[i] <= i) baseScore++;
    }
    
    const diff = new Array(n).fill(0);
    
    for (let i = 0; i < n; ++i) {
        // start of bad interval
        let l = (i - nums[i] + 1 + n) % n;
        let r = i; // inclusive
        
        if (l <= r) {
            diff[l] -= 1;
            if (r + 1 < n) diff[r + 1] += 1;
        } else {
            // interval wraps: [0, r] and [l, n-1]
            diff[0] -= 1;
            if (r + 1 < n) diff[r + 1] += 1;
            diff[l] -= 1;
            // no need to add after n-1
        }
    }
    
    let bestK = 0;
    let maxScore = -Infinity;
    let curDelta = 0;
    
    for (let k = 0; k < n; ++k) {
        curDelta += diff[k];
        const score = baseScore + curDelta;
        if (score > maxScore) {
            maxScore = score;
            bestK = k;
        }
    }
    
    return bestK;
};
```

## Typescript

```typescript
function bestRotation(nums: number[]): number {
    const n = nums.length;
    let baseScore = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] <= i) baseScore++;
    }

    const diff = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        const a = nums[i];
        let start = i - a + 1;
        start %= n;
        if (start < 0) start += n;
        const end = i;

        if (start <= end) {
            diff[start] -= 1;
            diff[end + 1] += 1;
        } else {
            diff[start] -= 1;
            diff[n] += 1;
            diff[0] -= 1;
            diff[end + 1] += 1;
        }
    }

    let bestK = 0;
    let maxScore = baseScore;
    let curDelta = 0;
    for (let k = 0; k < n; k++) {
        curDelta += diff[k];
        const score = baseScore + curDelta;
        if (score > maxScore) {
            maxScore = score;
            bestK = k;
        }
    }

    return bestK;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function bestRotation($nums) {
        $n = count($nums);
        $diff = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $v = $nums[$i];
            if ($v == 0) continue;
            $low = $i - $v + 1;
            $low %= $n;
            if ($low < 0) $low += $n;
            $high = $i;
            if ($low <= $high) {
                $diff[$low] -= 1;
                $diff[$high + 1] += 1;
            } else {
                $diff[0] -= 1;
                $diff[$high + 1] += 1;
                $diff[$low] -= 1;
            }
        }
        $maxScore = -1;
        $bestK = 0;
        $cumulative = 0;
        for ($k = 0; $k < $n; $k++) {
            $cumulative += $diff[$k];
            $score = $n + $cumulative;
            if ($score > $maxScore) {
                $maxScore = $score;
                $bestK = $k;
            }
        }
        return $bestK;
    }
}
```

## Swift

```swift
class Solution {
    func bestRotation(_ nums: [Int]) -> Int {
        let n = nums.count
        var change = [Int](repeating: 0, count: n + 1)
        var baseScore = 0
        
        for i in 0..<n {
            if nums[i] <= i { baseScore += 1 }
            let low = (i - nums[i] + 1 + n) % n
            let high = i
            if low <= high {
                change[low] -= 1
                change[high + 1] += 1
            } else {
                // interval [0, high]
                change[0] -= 1
                change[high + 1] += 1
                // interval [low, n-1]
                change[low] -= 1
                // no need to add at n (sentinel)
            }
        }
        
        var bestK = 0
        var bestScore = baseScore
        var curScore = baseScore
        
        for k in 1..<n {
            curScore += change[k]
            if curScore > bestScore {
                bestScore = curScore
                bestK = k
            }
        }
        
        return bestK
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun bestRotation(nums: IntArray): Int {
        val n = nums.size
        val diff = IntArray(n + 1)
        for (i in 0 until n) {
            val v = nums[i]
            if (v == 0) continue
            var low = i - v + 1
            low %= n
            if (low < 0) low += n
            val high = i
            if (low <= high) {
                diff[low] -= 1
                diff[high + 1] += 1
            } else {
                diff[0] -= 1
                diff[high + 1] += 1
                diff[low] -= 1
            }
        }
        var bestScore = -1
        var bestK = 0
        var cur = 0
        val base = n
        for (k in 0 until n) {
            cur += diff[k]
            val score = base + cur
            if (score > bestScore) {
                bestScore = score
                bestK = k
            }
        }
        return bestK
    }
}
```

## Dart

```dart
class Solution {
  int bestRotation(List<int> nums) {
    int n = nums.length;
    List<int> diff = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      int val = nums[i];
      if (val == 0) continue;
      int start = (i - val + 1) % n;
      if (start < 0) start += n;
      int end = i;
      if (start <= end) {
        diff[start] += 1;
        diff[end + 1] -= 1;
      } else {
        diff[0] += 1;
        diff[end + 1] -= 1;
        diff[start] += 1;
      }
    }
    int maxScore = -1;
    int bestK = 0;
    int bad = 0;
    for (int k = 0; k < n; ++k) {
      bad += diff[k];
      int score = n - bad;
      if (score > maxScore) {
        maxScore = score;
        bestK = k;
      }
    }
    return bestK;
  }
}
```

## Golang

```go
func bestRotation(nums []int) int {
    n := len(nums)
    change := make([]int, n+1)
    baseScore := 0

    for i, v := range nums {
        if v <= i {
            baseScore++
        }
        start := (i - v + 1 + n) % n
        end := i
        if start <= end {
            change[start]--
            change[end+1]++
        } else {
            // interval wraps around the end of the array
            change[start]--
            change[n]++
            change[0]--
            change[end+1]++
        }
    }

    bestK, maxScore := 0, baseScore
    cum := 0
    for k := 1; k < n; k++ {
        cum += change[k]
        score := baseScore + cum
        if score > maxScore {
            maxScore = score
            bestK = k
        }
    }
    return bestK
}
```

## Ruby

```ruby
def best_rotation(nums)
  n = nums.length
  base = 0
  diff = Array.new(n + 1, 0)

  nums.each_with_index do |val, i|
    base += 1 if val <= i

    start_idx = (i - val + 1) % n
    end_idx   = (i + 1) % n

    if start_idx <= end_idx
      diff[start_idx] -= 1
      diff[end_idx]   += 1
    else
      diff[0]        -= 1
      diff[end_idx]  += 1
      diff[start_idx] -= 1
      diff[n]        += 1
    end
  end

  max_score = base
  best_k = 0
  cur = 0
  (0...n).each do |k|
    cur += diff[k]
    score = base + cur
    if score > max_score
      max_score = score
      best_k = k
    end
  end

  best_k
end
```

## Scala

```scala
object Solution {
    def bestRotation(nums: Array[Int]): Int = {
        val n = nums.length
        val change = new Array[Int](n)
        for (i <- 0 until n) {
            val start = ((i - nums(i) + 1) % n + n) % n
            val end = (i + 1) % n
            change(start) -= 1
            change(end) += 1
            if (start > end) {
                change(0) -= 1
            }
        }
        var bestK = 0
        var bestScore = -1
        var cur = 0
        for (k <- 0 until n) {
            cur += change(k)
            val score = cur + n
            if (score > bestScore) {
                bestScore = score
                bestK = k
            }
        }
        bestK
    }
}
```

## Rust

```rust
impl Solution {
    pub fn best_rotation(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut diff = vec![0i32; n + 1];
        for i in 0..n {
            let num = nums[i] as i64;
            let start = ((i as i64 - num + 1).rem_euclid(n as i64)) as usize;
            let end = (i + 1) % n;
            if start == end {
                continue;
            }
            if start < end {
                diff[start] -= 1;
                diff[end] += 1;
            } else {
                diff[0] -= 1;
                diff[end] += 1;
                diff[start] -= 1;
            }
        }

        let mut best_k = 0usize;
        let mut best_score = -1i32;
        let mut cur = 0i32;
        for k in 0..n {
            cur += diff[k];
            let score = n as i32 + cur;
            if score > best_score {
                best_score = score;
                best_k = k;
            }
        }

        best_k as i32
    }
}
```

## Racket

```racket
(define/contract (best-rotation nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [arr (list->vector nums)]
         [diff (make-vector n 0)])
    (for ([i (in-range n)])
      (let* ([x (vector-ref arr i)]
             [start (modulo (+ i (- x) 1) n)] ; (i - x + 1) mod n
             [end i]
             [next (add1 end)])
        ;; empty bad interval when start == (end+1) mod n
        (when (not (= start (modulo next n)))
          (if (<= start end)
              (begin
                (vector-set! diff start (+ (vector-ref diff start) 1))
                (when (< next n)
                  (vector-set! diff next (- (vector-ref diff next) 1))))
              (begin
                (vector-set! diff start (+ (vector-ref diff start) 1))
                (vector-set! diff 0 (+ (vector-ref diff 0) 1))
                (when (< next n)
                  (vector-set! diff next (- (vector-ref diff next) 1))))))))
    (let loop ([k 0] [active 0] [best-score -1] [best-k 0])
      (if (= k n)
          best-k
          (let* ([active (+ active (vector-ref diff k))]
                 [score (- n active)])
            (if (> score best-score)
                (loop (add1 k) active score k)
                (loop (add1 k) active best-score best-k)))))))
```

## Erlang

```erlang
-module(solution).
-export([best_rotation/1]).

best_rotation(Nums) ->
    N = length(Nums),
    Diff = build_diff(Nums, 0, N, #{}),
    find_best(Diff, N).

build_diff([], _Idx, _N, Diff) -> Diff;
build_diff([V|Rest], I, N, Diff) ->
    Low = mod(I - V + 1, N),
    High = (I + 1) rem N,
    Diff1 = maps:put(Low, maps:get(Low, Diff, 0) + 1, Diff),
    Diff2 = maps:put(High, maps:get(High, Diff, 0) - 1, Diff1),
    build_diff(Rest, I + 1, N, Diff2).

mod(A, N) -> ((A rem N) + N) rem N.

find_best(Diff, N) ->
    find_best_loop(0, 0, -1, 0, Diff, N).

find_best_loop(K, ScoreAcc, BestScore, BestK, _Diff, N) when K =:= N ->
    BestK;
find_best_loop(K, ScoreAcc, BestScore, BestK, Diff, N) ->
    Delta = maps:get(K, Diff, 0),
    NewScore = ScoreAcc + Delta,
    {NewBestScore, NewBestK} =
        if
            NewScore > BestScore -> {NewScore, K};
            true -> {BestScore, BestK}
        end,
    find_best_loop(K + 1, NewScore, NewBestScore, NewBestK, Diff, N).
```

## Elixir

```elixir
defmodule Solution do
  @spec best_rotation(nums :: [integer]) :: integer
  def best_rotation(nums) do
    n = length(nums)
    diff = build_diff(nums, n)

    {_, best_k, _} =
      Enum.reduce(0..(n - 1), {n, 0, n}, fn k, {cur, best_k, best_score} ->
        delta = Map.get(diff, k, 0)
        cur2 = cur + delta

        if cur2 > best_score do
          {cur2, k, cur2}
        else
          {cur2, best_k, best_score}
        end
      end)

    best_k
  end

  defp build_diff(nums, n) do
    Enum.with_index(nums)
    |> Enum.reduce(%{}, fn {val, i}, acc ->
      if val > 0 do
        low = rem(i - val + 1 + n, n)
        high = i

        acc = Map.update(acc, low, -1, &(&1 - 1))

        if low <= high do
          idx = high + 1
          Map.update(acc, idx, 1, &(&1 + 1))
        else
          acc = Map.update(acc, n, 1, &(&1 + 1))
          acc = Map.update(acc, 0, -1, &(&1 - 1))
          idx = high + 1
          Map.update(acc, idx, 1, &(&1 + 1))
        end
      else
        acc
      end
    end)
  end
end
```
