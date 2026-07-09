# 2106. Maximum Fruits Harvested After at Most K Steps

## Cpp

```cpp
class Solution {
public:
    int maxTotalFruits(vector<vector<int>>& fruits, int startPos, int k) {
        int n = fruits.size();
        auto stepsNeeded = [&](int lIdx, int rIdx) -> long long {
            long long leftPos = fruits[lIdx][0];
            long long rightPos = fruits[rIdx][0];
            if (startPos <= leftPos) {
                return rightPos - startPos;
            } else if (startPos >= rightPos) {
                return startPos - leftPos;
            } else {
                return (rightPos - leftPos) + min(startPos - leftPos, rightPos - startPos);
            }
        };
        
        long long curSum = 0;
        int ans = 0;
        int l = 0;
        for (int r = 0; r < n; ++r) {
            curSum += fruits[r][1];
            while (l <= r && stepsNeeded(l, r) > k) {
                curSum -= fruits[l][1];
                ++l;
            }
            ans = max(ans, (int)curSum);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxTotalFruits(int[][] fruits, int startPos, int k) {
        int n = fruits.length;
        long curSum = 0;
        int left = 0;
        int ans = 0;
        for (int right = 0; right < n; ++right) {
            curSum += fruits[right][1];
            while (left <= right && stepsNeeded(fruits, left, right, startPos) > k) {
                curSum -= fruits[left][1];
                left++;
            }
            ans = Math.max(ans, (int) curSum);
        }
        return ans;
    }

    private long stepsNeeded(int[][] f, int l, int r, int start) {
        int leftPos = f[l][0];
        int rightPos = f[r][0];
        long interval = (long) rightPos - leftPos;
        long extra = Math.min(Math.abs(start - leftPos), Math.abs(rightPos - start));
        return interval + extra;
    }
}
```

## Python

```python
class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        n = len(fruits)
        left = 0
        cur_sum = 0
        best = 0

        for right in range(n):
            cur_sum += fruits[right][1]
            # shrink window until it fits within k steps
            while left <= right:
                lpos = fruits[left][0]
                rpos = fruits[right][0]
                needed = (rpos - lpos) + min(abs(startPos - lpos), abs(startPos - rpos))
                if needed <= k:
                    break
                cur_sum -= fruits[left][1]
                left += 1
            if cur_sum > best:
                best = cur_sum

        return best
```

## Python3

```python
class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        pos = [p for p, _ in fruits]
        amt = [a for _, a in fruits]

        left = 0
        cur_sum = 0
        best = 0

        for right in range(n):
            cur_sum += amt[right]
            while left <= right:
                lpos = pos[left]
                rpos = pos[right]
                steps = rpos - lpos + min(abs(startPos - lpos), abs(startPos - rpos))
                if steps <= k:
                    break
                cur_sum -= amt[left]
                left += 1
            if cur_sum > best:
                best = cur_sum

        return best
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int maxTotalFruits(int** fruits, int fruitsSize, int* fruitsColSize, int startPos, int k) {
    long long sum = 0, best = 0;
    int left = 0;
    for (int right = 0; right < fruitsSize; ++right) {
        sum += fruits[right][1];
        while (left <= right) {
            long long lpos = fruits[left][0];
            long long rpos = fruits[right][0];
            long long distL = llabs((long long)startPos - lpos);
            long long distR = llabs((long long)startPos - rpos);
            long long steps = (rpos - lpos) + (distL < distR ? distL : distR);
            if (steps <= k) break;
            sum -= fruits[left][1];
            ++left;
        }
        if (sum > best) best = sum;
    }
    return (int)best;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxTotalFruits(int[][] fruits, int startPos, int k)
    {
        int n = fruits.Length;
        long sum = 0;
        int left = 0;
        int best = 0;

        for (int right = 0; right < n; ++right)
        {
            sum += fruits[right][1];

            while (left <= right)
            {
                int lPos = fruits[left][0];
                int rPos = fruits[right][0];
                long steps = (long)rPos - lPos + Math.Min(Math.Abs(startPos - lPos), Math.Abs(startPos - rPos));
                if (steps <= k) break;
                sum -= fruits[left][1];
                left++;
            }

            best = Math.Max(best, (int)sum);
        }

        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} fruits
 * @param {number} startPos
 * @param {number} k
 * @return {number}
 */
var maxTotalFruits = function(fruits, startPos, k) {
    const n = fruits.length;
    let left = 0;
    let curSum = 0;
    let best = 0;

    const neededSteps = (lPos, rPos) => {
        const totalDist = rPos - lPos; // positions are sorted, so non‑negative
        const extra = Math.min(Math.abs(startPos - lPos), Math.abs(startPos - rPos));
        return totalDist + extra;
    };

    for (let right = 0; right < n; ++right) {
        curSum += fruits[right][1];
        while (left <= right && neededSteps(fruits[left][0], fruits[right][0]) > k) {
            curSum -= fruits[left][1];
            ++left;
        }
        if (curSum > best) best = curSum;
    }

    return best;
};
```

## Typescript

```typescript
function maxTotalFruits(fruits: number[][], startPos: number, k: number): number {
    const n = fruits.length;
    let left = 0;
    let sum = 0;
    let best = 0;

    const stepsNeeded = (lIdx: number, rIdx: number): number => {
        const lPos = fruits[lIdx][0];
        const rPos = fruits[rIdx][0];
        if (startPos <= lPos) {
            // interval completely to the right
            return rPos - startPos;
        }
        if (startPos >= rPos) {
            // interval completely to the left
            return startPos - lPos;
        }
        // startPos inside [lPos, rPos]
        return (rPos - lPos) + Math.min(startPos - lPos, rPos - startPos);
    };

    for (let right = 0; right < n; ++right) {
        sum += fruits[right][1];
        while (left <= right && stepsNeeded(left, right) > k) {
            sum -= fruits[left][1];
            left++;
        }
        if (sum > best) best = sum;
    }

    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $fruits
     * @param Integer $startPos
     * @param Integer $k
     * @return Integer
     */
    function maxTotalFruits($fruits, $startPos, $k) {
        $n = count($fruits);
        $left = 0;
        $currentSum = 0;
        $maxSum = 0;

        for ($right = 0; $right < $n; $right++) {
            $currentSum += $fruits[$right][1];

            while ($left <= $right) {
                $leftPos = $fruits[$left][0];
                $rightPos = $fruits[$right][0];
                $steps = $rightPos - $leftPos + min(abs($startPos - $leftPos), abs($startPos - $rightPos));
                if ($steps <= $k) {
                    break;
                }
                $currentSum -= $fruits[$left][1];
                $left++;
            }

            if ($currentSum > $maxSum) {
                $maxSum = $currentSum;
            }
        }

        return $maxSum;
    }
}
```

## Swift

```swift
class Solution {
    func maxTotalFruits(_ fruits: [[Int]], _ startPos: Int, _ k: Int) -> Int {
        let n = fruits.count
        var positions = [Int]()
        var amounts = [Int]()
        positions.reserveCapacity(n)
        amounts.reserveCapacity(n)
        for f in fruits {
            positions.append(f[0])
            amounts.append(f[1])
        }
        
        var left = 0
        var currentSum = 0
        var answer = 0
        
        for right in 0..<n {
            currentSum += amounts[right]
            
            while left <= right {
                let distance = positions[right] - positions[left]
                let extra = min(abs(startPos - positions[left]), abs(startPos - positions[right]))
                let stepsNeeded = distance + extra
                if stepsNeeded <= k {
                    break
                }
                currentSum -= amounts[left]
                left += 1
            }
            
            answer = max(answer, currentSum)
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxTotalFruits(fruits: Array<IntArray>, startPos: Int, k: Int): Int {
        var left = 0
        var currentSum = 0L
        var best = 0L
        val n = fruits.size
        for (right in 0 until n) {
            currentSum += fruits[right][1].toLong()
            while (left <= right && stepsNeeded(fruits[left][0], fruits[right][0], startPos) > k.toLong()) {
                currentSum -= fruits[left][1].toLong()
                left++
            }
            if (currentSum > best) best = currentSum
        }
        return best.toInt()
    }

    private fun stepsNeeded(leftPos: Int, rightPos: Int, startPos: Int): Long {
        val intervalDist = (rightPos - leftPos).toLong()
        val extra = kotlin.math.min(kotlin.math.abs(startPos - leftPos), kotlin.math.abs(startPos - rightPos)).toLong()
        return intervalDist + extra
    }
}
```

## Dart

```dart
class Solution {
  int maxTotalFruits(List<List<int>> fruits, int startPos, int k) {
    int n = fruits.length;
    List<int> pos = List.filled(n, 0);
    List<int> amt = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      pos[i] = fruits[i][0];
      amt[i] = fruits[i][1];
    }

    int left = 0;
    int curSum = 0;
    int best = 0;

    for (int right = 0; right < n; ++right) {
      curSum += amt[right];
      while (left <= right && _steps(pos[left], pos[right], startPos) > k) {
        curSum -= amt[left];
        left++;
      }
      if (curSum > best) best = curSum;
    }

    return best;
  }

  int _steps(int leftPos, int rightPos, int startPos) {
    if (startPos <= leftPos) {
      // interval completely to the right of start
      return rightPos - startPos;
    } else if (startPos >= rightPos) {
      // interval completely to the left of start
      return startPos - leftPos;
    } else {
      // start inside the interval
      int totalDist = rightPos - leftPos;
      int extra = (startPos - leftPos) < (rightPos - startPos)
          ? (startPos - leftPos)
          : (rightPos - startPos);
      return totalDist + extra;
    }
  }
}
```

## Golang

```go
func maxTotalFruits(fruits [][]int, startPos int, k int) int {
	n := len(fruits)
	left, curSum, best := 0, 0, 0

	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}

	stepsNeeded := func(l, r int) int {
		lPos, rPos := fruits[l][0], fruits[r][0]
		span := rPos - lPos
		dL := abs(startPos - lPos)
		dR := abs(startPos - rPos)
		if dL < dR {
			return span + dL
		}
		return span + dR
	}

	for right := 0; right < n; right++ {
		curSum += fruits[right][1]
		for left <= right && stepsNeeded(left, right) > k {
			curSum -= fruits[left][1]
			left++
		}
		if curSum > best {
			best = curSum
		}
	}
	return best
}
```

## Ruby

```ruby
def max_total_fruits(fruits, start_pos, k)
  n = fruits.length
  pos = Array.new(n)
  amt = Array.new(n)
  fruits.each_with_index do |f, i|
    pos[i] = f[0]
    amt[i] = f[1]
  end

  steps_needed = lambda do |l, r|
    left_pos = pos[l]
    right_pos = pos[r]
    if start_pos <= left_pos
      right_pos - start_pos
    elsif start_pos >= right_pos
      start_pos - left_pos
    else
      (right_pos - left_pos) + [start_pos - left_pos, right_pos - start_pos].min
    end
  end

  left = 0
  cur_sum = 0
  best = 0

  (0...n).each do |right|
    cur_sum += amt[right]
    while left <= right && steps_needed.call(left, right) > k
      cur_sum -= amt[left]
      left += 1
    end
    best = [best, cur_sum].max
  end

  best
end
```

## Scala

```scala
object Solution {
  def maxTotalFruits(fruits: Array[Array[Int]], startPos: Int, k: Int): Int = {
    val n = fruits.length
    val pos = new Array[Int](n)
    val amt = new Array[Long](n)
    var i = 0
    while (i < n) {
      pos(i) = fruits(i)(0)
      amt(i) = fruits(i)(1).toLong
      i += 1
    }

    var left = 0
    var curSum: Long = 0L
    var best: Long = 0L
    var right = 0

    while (right < n) {
      curSum += amt(right)

      while (left <= right && (pos(right) - pos(left) + Math.min(Math.abs(startPos - pos(left)), Math.abs(startPos - pos(right))) > k)) {
        curSum -= amt(left)
        left += 1
      }

      if (curSum > best) best = curSum
      right += 1
    }

    best.toInt
  }
}
```

## Rust

```rust
use std::cmp::{max, min};

impl Solution {
    pub fn max_total_fruits(fruits: Vec<Vec<i32>>, start_pos: i32, k: i32) -> i32 {
        let n = fruits.len();
        if n == 0 {
            return 0;
        }
        let mut left_idx: usize = 0;
        let mut cur_sum: i64 = 0;
        let mut answer: i64 = 0;
        for right_idx in 0..n {
            cur_sum += fruits[right_idx][1] as i64;
            while left_idx <= right_idx
                && Self::steps_needed(
                    fruits[left_idx][0],
                    fruits[right_idx][0],
                    start_pos,
                ) > k as i64
            {
                cur_sum -= fruits[left_idx][1] as i64;
                left_idx += 1;
            }
            answer = max(answer, cur_sum);
        }
        answer as i32
    }

    fn steps_needed(left: i32, right: i32, start: i32) -> i64 {
        if start <= left {
            (right - start) as i64
        } else if start >= right {
            (start - left) as i64
        } else {
            let total = (right - left) as i64;
            let extra = min(start - left, right - start) as i64;
            total + extra
        }
    }
}
```

## Racket

```racket
(define/contract (max-total-fruits fruits startPos k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer?)
  (let* ((n (length fruits))
         (fruits-vec (list->vector fruits)))
    (define (pos i) (first (vector-ref fruits-vec i)))
    (define (amt i) (second (vector-ref fruits-vec i)))
    (define (steps-needed l r)
      (let ((pL (pos l))
            (pR (pos r)))
        (cond [(<= startPos pL) (- pR startPos)]
              [(>= startPos pR) (- startPos pL)]
              [else (+ (- pR pL)
                       (min (- startPos pL) (- pR startPos)))])))
    (let ((left 0)
          (curSum 0)
          (ans 0))
      (for ([right (in-range n)])
        (set! curSum (+ curSum (amt right)))
        ;; shrink while the interval cannot be covered within k steps
        (let loop ()
          (when (and (<= left right) (> (steps-needed left right) k))
            (set! curSum (- curSum (amt left)))
            (set! left (+ left 1))
            (loop)))
        (when (and (<= left right) (<= (steps-needed left right) k))
          (when (> curSum ans)
            (set! ans curSum))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([max_total_fruits/3]).

-spec max_total_fruits(Fruits :: [[integer()]], StartPos :: integer(), K :: integer()) -> integer().
max_total_fruits(Fruits, StartPos, K) ->
    Positions = list_to_tuple([Pos || [Pos,_] <- Fruits]),
    Amounts   = list_to_tuple([Amt || [_ ,Amt] <- Fruits]),
    N = tuple_size(Positions),
    iter(N, -1, 0, 0, 0, Positions, Amounts, StartPos, K).

%% iter(N, RightIdx, LeftIdx, CurSum, MaxSum, PosTuple, AmtTuple, StartPos, K)
iter(N, Right, _Left, _Sum, Max, _Pos, _Amt, _StartPos, _K) when Right + 1 == N ->
    Max;
iter(N, Right, Left, Sum, Max, Pos, Amt, StartPos, K) ->
    NewRight = Right + 1,
    AmtR = element(NewRight + 1, Amt),
    NewSum = Sum + AmtR,
    {NewLeft, TrimmedSum} = shrink(Left, NewRight, NewSum, Pos, Amt, StartPos, K),
    NewMax = erlang:max(Max, TrimmedSum),
    iter(N, NewRight, NewLeft, TrimmedSum, NewMax, Pos, Amt, StartPos, K).

%% shrink(LeftIdx, RightIdx, CurSum, PosTuple, AmtTuple, StartPos, K) -> {NewLeftIdx, NewSum}
shrink(Left, Right, Sum, Pos, Amt, StartPos, K) ->
    case Left =< Right of
        false ->
            {Left, Sum};
        true ->
            PosL = element(Left + 1, Pos),
            PosR = element(Right + 1, Pos),
            Span = PosR - PosL,
            DistNear = erlang:min(erlang:abs(StartPos - PosL), erlang:abs(StartPos - PosR)),
            Steps = Span + DistNear,
            if
                Steps =< K ->
                    {Left, Sum};
                true ->
                    AmtL = element(Left + 1, Amt),
                    shrink(Left + 1, Right, Sum - AmtL, Pos, Amt, StartPos, K)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_total_fruits(fruits :: [[integer]], start_pos :: integer, k :: integer) :: integer
  def max_total_fruits(fruits, start_pos, k) do
    n = length(fruits)

    positions =
      fruits
      |> Enum.map(fn [p, _] -> p end)
      |> List.to_tuple()

    amounts =
      fruits
      |> Enum.map(fn [_ ,a] -> a end)
      |> List.to_tuple()

    iterate(0, 0, 0, 0, n, positions, amounts, start_pos, k)
  end

  defp iterate(r, l, cur_sum, max_sum, n, positions, amounts, start_pos, k) do
    if r == n do
      max_sum
    else
      new_cur = cur_sum + :erlang.element(r + 1, amounts)

      {new_l, new_cur2} =
        shrink(l, new_cur, positions, amounts, start_pos, k, r)

      new_max = if new_cur2 > max_sum, do: new_cur2, else: max_sum
      iterate(r + 1, new_l, new_cur2, new_max, n, positions, amounts, start_pos, k)
    end
  end

  defp shrink(l, cur_sum, positions, amounts, start_pos, k, r) do
    if l <= r && step(positions, start_pos, l, r) > k do
      new_sum = cur_sum - :erlang.element(l + 1, amounts)
      shrink(l + 1, new_sum, positions, amounts, start_pos, k, r)
    else
      {l, cur_sum}
    end
  end

  defp step(positions, start_pos, l, r) do
    left_pos = :erlang.element(l + 1, positions)
    right_pos = :erlang.element(r + 1, positions)

    cond do
      start_pos <= left_pos ->
        right_pos - start_pos

      start_pos >= right_pos ->
        start_pos - left_pos

      true ->
        (right_pos - left_pos) +
          min(start_pos - left_pos, right_pos - start_pos)
    end
  end
end
```
