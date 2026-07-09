# 2865. Beautiful Towers I

## Cpp

```cpp
class Solution {
public:
    long long maximumSumOfHeights(vector<int>& heights) {
        int n = heights.size();
        long long best = 0;
        for (int peak = 0; peak < n; ++peak) {
            long long sum = heights[peak];
            long long cur = heights[peak];
            // left side
            for (int i = peak - 1; i >= 0; --i) {
                cur = min<long long>(heights[i], cur);
                sum += cur;
            }
            // right side
            cur = heights[peak];
            for (int i = peak + 1; i < n; ++i) {
                cur = min<long long>(heights[i], cur);
                sum += cur;
            }
            best = max(best, sum);
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public long maximumSumOfHeights(int[] heights) {
        int n = heights.length;
        long best = 0L;
        for (int peak = 0; peak < n; ++peak) {
            long sum = 0L;
            long cur = heights[peak];
            // left side including peak
            for (int i = peak; i >= 0; --i) {
                cur = Math.min(cur, heights[i]);
                sum += cur;
            }
            // right side excluding peak
            cur = heights[peak];
            for (int i = peak + 1; i < n; ++i) {
                cur = Math.min(cur, heights[i]);
                sum += cur;
            }
            if (sum > best) best = sum;
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def maximumSumOfHeights(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        best = 0
        for i in range(n):
            # left side including i
            cur = heights[i]
            left_sum = 0
            for j in range(i, -1, -1):
                if heights[j] < cur:
                    cur = heights[j]
                left_sum += cur

            # right side including i
            cur = heights[i]
            right_sum = 0
            for j in range(i, n):
                if heights[j] < cur:
                    cur = heights[j]
                right_sum += cur

            total = left_sum + right_sum - heights[i]  # peak counted twice
            if total > best:
                best = total
        return best
```

## Python3

```python
class Solution:
    def maximumSumOfHeights(self, heights):
        n = len(heights)
        left = [0] * n
        right = [0] * n

        # compute left sums: sum of minima for subarrays ending at i
        stack = []  # each element is (value, count)
        cur_sum = 0
        for i, h in enumerate(heights):
            cnt = 1
            while stack and stack[-1][0] > h:
                val, c = stack.pop()
                cur_sum -= val * c
                cnt += c
            stack.append((h, cnt))
            cur_sum += h * cnt
            left[i] = cur_sum

        # compute right sums: sum of minima for subarrays starting at i
        stack.clear()
        cur_sum = 0
        for i in range(n - 1, -1, -1):
            h = heights[i]
            cnt = 1
            while stack and stack[-1][0] > h:
                val, c = stack.pop()
                cur_sum -= val * c
                cnt += c
            stack.append((h, cnt))
            cur_sum += h * cnt
            right[i] = cur_sum

        ans = 0
        for i in range(n):
            total = left[i] + right[i] - heights[i]
            if total > ans:
                ans = total
        return ans
```

## C

```c
long long maximumSumOfHeights(int* heights, int heightsSize) {
    int n = heightsSize;
    if (n == 0) return 0;
    
    long long *left = (long long*)malloc(sizeof(long long) * n);
    long long *right = (long long*)malloc(sizeof(long long) * n);
    
    // Compute left sums
    long long *stackVal = (long long*)malloc(sizeof(long long) * n);
    int *stackCnt = (int*)malloc(sizeof(int) * n);
    int top = 0;
    long long cur = 0;
    for (int i = 0; i < n; ++i) {
        long long cnt = 1;
        while (top > 0 && stackVal[top - 1] > heights[i]) {
            cur -= stackVal[top - 1] * (long long)stackCnt[top - 1];
            cnt += stackCnt[top - 1];
            --top;
        }
        stackVal[top] = heights[i];
        stackCnt[top] = (int)cnt;
        ++top;
        cur += (long long)heights[i] * cnt;
        left[i] = cur;
    }
    
    // Compute right sums
    top = 0;
    cur = 0;
    for (int i = n - 1; i >= 0; --i) {
        long long cnt = 1;
        while (top > 0 && stackVal[top - 1] > heights[i]) {
            cur -= stackVal[top - 1] * (long long)stackCnt[top - 1];
            cnt += stackCnt[top - 1];
            --top;
        }
        stackVal[top] = heights[i];
        stackCnt[top] = (int)cnt;
        ++top;
        cur += (long long)heights[i] * cnt;
        right[i] = cur;
    }
    
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        long long total = left[i] + right[i] - heights[i];
        if (total > ans) ans = total;
    }
    
    free(left);
    free(right);
    free(stackVal);
    free(stackCnt);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MaximumSumOfHeights(int[] heights) {
        int n = heights.Length;
        long[] left = new long[n];
        long[] right = new long[n];

        var stack = new Stack<(int h, int cnt)>();
        long cur = 0;
        for (int i = 0; i < n; i++) {
            int h = heights[i];
            int cnt = 1;
            while (stack.Count > 0 && stack.Peek().h > h) {
                var top = stack.Pop();
                cur -= (long)top.h * top.cnt;
                cnt += top.cnt;
            }
            stack.Push((h, cnt));
            cur += (long)h * cnt;
            left[i] = cur;
        }

        stack.Clear();
        cur = 0;
        for (int i = n - 1; i >= 0; i--) {
            int h = heights[i];
            int cnt = 1;
            while (stack.Count > 0 && stack.Peek().h > h) {
                var top = stack.Pop();
                cur -= (long)top.h * top.cnt;
                cnt += top.cnt;
            }
            stack.Push((h, cnt));
            cur += (long)h * cnt;
            right[i] = cur;
        }

        long ans = 0;
        for (int i = 0; i < n; i++) {
            long total = left[i] + right[i] - heights[i];
            if (total > ans) ans = total;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} heights
 * @return {number}
 */
var maximumSumOfHeights = function(heights) {
    const n = heights.length;
    const left = new Array(n);
    let stack = [];
    let sum = 0;

    // compute left contributions
    for (let i = 0; i < n; i++) {
        let cnt = 1;
        while (stack.length && stack[stack.length - 1][0] > heights[i]) {
            const [h, c] = stack.pop();
            sum -= h * c;
            cnt += c;
        }
        stack.push([heights[i], cnt]);
        sum += heights[i] * cnt;
        left[i] = sum;
    }

    // compute right contributions
    const right = new Array(n);
    stack = [];
    sum = 0;
    for (let i = n - 1; i >= 0; i--) {
        let cnt = 1;
        while (stack.length && stack[stack.length - 1][0] > heights[i]) {
            const [h, c] = stack.pop();
            sum -= h * c;
            cnt += c;
        }
        stack.push([heights[i], cnt]);
        sum += heights[i] * cnt;
        right[i] = sum;
    }

    // combine results
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const total = left[i] + right[i] - heights[i];
        if (total > ans) ans = total;
    }
    return ans;
};
```

## Typescript

```typescript
function maximumSumOfHeights(heights: number[]): number {
    const n = heights.length;
    let best = 0;
    for (let peak = 0; peak < n; ++peak) {
        let total = 0;
        // left side including peak
        let cur = heights[peak];
        total += cur;
        for (let i = peak - 1; i >= 0; --i) {
            cur = Math.min(heights[i], cur);
            total += cur;
        }
        // right side
        cur = heights[peak];
        for (let i = peak + 1; i < n; ++i) {
            cur = Math.min(heights[i], cur);
            total += cur;
        }
        if (total > best) best = total;
    }
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $heights
     * @return Integer
     */
    function maximumSumOfHeights($heights) {
        $n = count($heights);
        $maxSum = 0;
        for ($i = 0; $i < $n; ++$i) {
            $sum = $heights[$i];
            // left side
            $prev = $heights[$i];
            for ($j = $i - 1; $j >= 0; --$j) {
                $curr = min($heights[$j], $prev);
                $sum += $curr;
                $prev = $curr;
            }
            // right side
            $prev = $heights[$i];
            for ($j = $i + 1; $j < $n; ++$j) {
                $curr = min($heights[$j], $prev);
                $sum += $curr;
                $prev = $curr;
            }
            if ($sum > $maxSum) {
                $maxSum = $sum;
            }
        }
        return $maxSum;
    }
}
```

## Swift

```swift
class Solution {
    func maximumSumOfHeights(_ heights: [Int]) -> Int {
        let n = heights.count
        var left = Array(repeating: 0, count: n)
        var stack: [(value: Int, index: Int)] = []
        
        for i in 0..<n {
            while !stack.isEmpty && stack.last!.value >= heights[i] {
                stack.removeLast()
            }
            if let last = stack.last {
                let prevIdx = last.index
                left[i] = left[prevIdx] + heights[i] * (i - prevIdx)
            } else {
                left[i] = heights[i] * (i + 1)
            }
            stack.append((heights[i], i))
        }
        
        var right = Array(repeating: 0, count: n)
        stack.removeAll()
        for i in stride(from: n - 1, through: 0, by: -1) {
            while !stack.isEmpty && stack.last!.value >= heights[i] {
                stack.removeLast()
            }
            if let last = stack.last {
                let nextIdx = last.index
                right[i] = right[nextIdx] + heights[i] * (nextIdx - i)
            } else {
                right[i] = heights[i] * (n - i)
            }
            stack.append((heights[i], i))
        }
        
        var answer = 0
        for i in 0..<n {
            let total = left[i] + right[i] - heights[i]
            if total > answer {
                answer = total
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumSumOfHeights(heights: IntArray): Long {
        val n = heights.size
        val left = LongArray(n)
        for (i in 0 until n) {
            var cur = heights[i].toLong()
            var sum = cur
            for (j in i - 1 downTo 0) {
                cur = kotlin.math.min(cur, heights[j].toLong())
                sum += cur
            }
            left[i] = sum
        }
        val right = LongArray(n)
        for (i in n - 1 downTo 0) {
            var cur = heights[i].toLong()
            var sum = cur
            for (j in i + 1 until n) {
                cur = kotlin.math.min(cur, heights[j].toLong())
                sum += cur
            }
            right[i] = sum
        }
        var ans = 0L
        for (i in 0 until n) {
            val total = left[i] + right[i] - heights[i]
            if (total > ans) ans = total
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maximumSumOfHeights(List<int> heights) {
    int n = heights.length;
    int best = 0;
    for (int i = 0; i < n; ++i) {
      List<int> cur = List.filled(n, 0);
      cur[i] = heights[i];
      // Build left side (non‑decreasing towards i)
      for (int j = i - 1; j >= 0; --j) {
        cur[j] = min(heights[j], cur[j + 1]);
      }
      // Build right side (non‑increasing after i)
      for (int j = i + 1; j < n; ++j) {
        cur[j] = min(heights[j], cur[j - 1]);
      }
      int sum = 0;
      for (int v in cur) sum += v;
      if (sum > best) best = sum;
    }
    return best;
  }
}
```

## Golang

```go
func maximumSumOfHeights(heights []int) int64 {
	n := len(heights)
	var best int64
	for peak := 0; peak < n; peak++ {
		sum := int64(heights[peak])

		// left side: non‑decreasing towards the peak
		prev := heights[peak]
		for i := peak - 1; i >= 0; i-- {
			if heights[i] < prev {
				prev = heights[i]
			}
			sum += int64(prev)
		}

		// right side: non‑increasing after the peak
		prev = heights[peak]
		for i := peak + 1; i < n; i++ {
			if heights[i] < prev {
				prev = heights[i]
			}
			sum += int64(prev)
		}

		if sum > best {
			best = sum
		}
	}
	return best
}
```

## Ruby

```ruby
def maximum_sum_of_heights(heights)
  n = heights.size
  max_total = 0

  (0...n).each do |i|
    # left side including i
    cur = heights[i]
    sum_left = cur
    (i - 1).downto(0) do |j|
      cur = [heights[j], cur].min
      sum_left += cur
    end

    # right side including i
    cur = heights[i]
    sum_right = cur
    (i + 1...n).each do |j|
      cur = [heights[j], cur].min
      sum_right += cur
    end

    total = sum_left + sum_right - heights[i] # peak counted twice
    max_total = total if total > max_total
  end

  max_total
end
```

## Scala

```scala
object Solution {
    def maximumSumOfHeights(heights: Array[Int]): Long = {
        val n = heights.length
        var best: Long = 0L
        for (i <- 0 until n) {
            // left side including i
            var cur: Long = heights(i).toLong
            var leftSum: Long = cur
            var j = i - 1
            while (j >= 0) {
                cur = Math.min(heights(j).toLong, cur)
                leftSum += cur
                j -= 1
            }
            // right side including i
            cur = heights(i).toLong
            var rightSum: Long = cur
            j = i + 1
            while (j < n) {
                cur = Math.min(heights(j).toLong, cur)
                rightSum += cur
                j += 1
            }
            val total = leftSum + rightSum - heights(i).toLong
            if (total > best) best = total
        }
        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_sum_of_heights(heights: Vec<i32>) -> i64 {
        let n = heights.len();
        if n == 0 {
            return 0;
        }
        let mut left = vec![0i64; n];
        let mut stack: Vec<usize> = Vec::new();

        // left[i] = sum of minima for all subarrays ending at i
        for i in 0..n {
            while let Some(&top) = stack.last() {
                if heights[top] > heights[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            if let Some(&prev) = stack.last() {
                let cnt = (i - prev) as i64;
                left[i] = heights[i] as i64 * cnt + left[prev];
            } else {
                let cnt = (i + 1) as i64;
                left[i] = heights[i] as i64 * cnt;
            }
            stack.push(i);
        }

        // right[i] = sum of minima for all subarrays starting at i
        let mut right = vec![0i64; n];
        stack.clear();
        for i_rev in (0..n).rev() {
            while let Some(&top) = stack.last() {
                if heights[top] > heights[i_rev] {
                    stack.pop();
                } else {
                    break;
                }
            }
            if let Some(&next) = stack.last() {
                let cnt = (next - i_rev) as i64;
                right[i_rev] = heights[i_rev] as i64 * cnt + right[next];
            } else {
                let cnt = (n - i_rev) as i64;
                right[i_rev] = heights[i_rev] as i64 * cnt;
            }
            stack.push(i_rev);
        }

        // compute maximum mountain sum
        let mut ans: i64 = 0;
        for i in 0..n {
            let total = left[i] + right[i] - heights[i] as i64;
            if total > ans {
                ans = total;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-sum-of-heights heights)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector heights))
         (n (vector-length v)))
    (let loop-i ((i 0) (best 0))
      (if (= i n)
          best
          (let* ((left-sum
                  (let loop-left ((j i) (limit (vector-ref v i)) (acc 0))
                    (if (< j 0)
                        acc
                        (loop-left (- j 1) (min limit (vector-ref v j)) (+ acc limit)))))
                 (right-sum
                  (let loop-right ((j i) (limit (vector-ref v i)) (acc 0))
                    (if (>= j n)
                        acc
                        (loop-right (+ j 1) (min limit (vector-ref v j)) (+ acc limit)))))
                 (total (- (+ left-sum right-sum) (vector-ref v i))))
            (loop-i (+ i 1) (max best total)))))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_sum_of_heights/1]).

-spec maximum_sum_of_heights(Heights :: [integer()]) -> integer().
maximum_sum_of_heights(Heights) ->
    Tuple = list_to_tuple(Heights),
    N = tuple_size(Tuple),
    max_sum_loop(Tuple, N, 0, 0).

max_sum_loop(_Tuple, N, Idx, Max) when Idx >= N ->
    Max;
max_sum_loop(Tuple, N, Idx, Max) ->
    PeakHeight = element(Idx + 1, Tuple),
    LeftSum = left_sum(Tuple, Idx, PeakHeight, 0),
    RightSum = right_sum(Tuple, N, Idx, PeakHeight, 0),
    Total = LeftSum + RightSum - PeakHeight,
    NewMax = if Total > Max -> Total; true -> Max end,
    max_sum_loop(Tuple, N, Idx + 1, NewMax).

left_sum(_Tuple, Index, _CurMin, Acc) when Index < 0 ->
    Acc;
left_sum(Tuple, Index, CurMin, Acc) ->
    H = element(Index + 1, Tuple),
    NewCur = erlang:min(CurMin, H),
    left_sum(Tuple, Index - 1, NewCur, Acc + NewCur).

right_sum(_Tuple, N, Index, _CurMin, Acc) when Index >= N ->
    Acc;
right_sum(Tuple, N, Index, CurMin, Acc) ->
    H = element(Index + 1, Tuple),
    NewCur = erlang:min(CurMin, H),
    right_sum(Tuple, N, Index + 1, NewCur, Acc + NewCur).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_sum_of_heights(heights :: [integer]) :: integer
  def maximum_sum_of_heights(heights) do
    n = length(heights)

    Enum.reduce(0..(n - 1), 0, fn i, best ->
      peak = Enum.at(heights, i)

      left_total =
        left_sum(heights, i - 1, peak, 0)

      right_total =
        right_sum(heights, i + 1, peak, 0, n)

      total = left_total + right_total + peak
      if total > best, do: total, else: best
    end)
  end

  defp left_sum(_heights, idx, _prev, acc) when idx < 0, do: acc

  defp left_sum(heights, idx, prev, acc) do
    cur = min(Enum.at(heights, idx), prev)
    left_sum(heights, idx - 1, cur, acc + cur)
  end

  defp right_sum(_heights, idx, _prev, acc, n) when idx >= n, do: acc

  defp right_sum(heights, idx, prev, acc, n) do
    cur = min(Enum.at(heights, idx), prev)
    right_sum(heights, idx + 1, cur, acc + cur, n)
  end
end
```
