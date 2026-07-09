# 2140. Solving Questions With Brainpower

## Cpp

```cpp
class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        int n = questions.size();
        vector<long long> dp(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            long long points = questions[i][0];
            int brain = questions[i][1];
            long long take = points;
            int nextIdx = i + brain + 1;
            if (nextIdx <= n) take += dp[nextIdx];
            long long skip = dp[i + 1];
            dp[i] = max(take, skip);
        }
        return dp[0];
    }
};
```

## Java

```java
class Solution {
    public long mostPoints(int[][] questions) {
        int n = questions.length;
        long[] dp = new long[n + 1];
        for (int i = n - 1; i >= 0; --i) {
            int points = questions[i][0];
            int brainpower = questions[i][1];
            int nextIdx = i + brainpower + 1;
            long take = points + (nextIdx < n ? dp[nextIdx] : 0L);
            long skip = dp[i + 1];
            dp[i] = Math.max(take, skip);
        }
        return dp[0];
    }
}
```

## Python

```python
class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dp = [0] * (n + 1)  # dp[i]: max points starting from question i
        for i in range(n - 1, -1, -1):
            pts, brain = questions[i]
            next_idx = i + brain + 1
            solve = pts + (dp[next_idx] if next_idx <= n else 0)
            skip = dp[i + 1]
            dp[i] = solve if solve > skip else skip
        return dp[0]
```

## Python3

```python
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # dp[i] = max points starting from i
        for i in range(n - 1, -1, -1):
            pts, skip = questions[i]
            next_idx = i + skip + 1
            take = pts + (dp[next_idx] if next_idx <= n else 0)
            dp[i] = max(take, dp[i + 1])
        return dp[0]
```

## C

```c
#include <stdlib.h>

long long mostPoints(int** questions, int questionsSize, int* questionsColSize) {
    long long *dp = (long long *)calloc(questionsSize + 1, sizeof(long long));
    for (int i = questionsSize - 1; i >= 0; --i) {
        long long points = questions[i][0];
        int brain = questions[i][1];
        long long skip = dp[i + 1];
        int nextIdx = i + brain + 1;
        long long take = points + (nextIdx < questionsSize ? dp[nextIdx] : 0);
        dp[i] = skip > take ? skip : take;
    }
    long long result = dp[0];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public long MostPoints(int[][] questions)
    {
        int n = questions.Length;
        long[] dp = new long[n + 1]; // dp[i] = max points starting from i

        for (int i = n - 1; i >= 0; i--)
        {
            long points = questions[i][0];
            int brain = questions[i][1];

            int nextIdx = i + brain + 1;
            if (nextIdx > n) nextIdx = n;

            long solve = points + dp[nextIdx];
            long skip = dp[i + 1];

            dp[i] = solve > skip ? solve : skip;
        }

        return dp[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} questions
 * @return {number}
 */
var mostPoints = function(questions) {
    const n = questions.length;
    const dp = new Array(n + 1).fill(0); // dp[i] = max points starting from i
    
    for (let i = n - 1; i >= 0; --i) {
        const [points, brainpower] = questions[i];
        const nextIdx = i + brainpower + 1;
        const take = points + (nextIdx <= n ? dp[nextIdx] : 0);
        const skip = dp[i + 1];
        dp[i] = Math.max(take, skip);
    }
    
    return dp[0];
};
```

## Typescript

```typescript
function mostPoints(questions: number[][]): number {
    const n = questions.length;
    const dp = new Array<number>(n + 1).fill(0);
    for (let i = n - 1; i >= 0; i--) {
        const [points, brainpower] = questions[i];
        const nextIdx = i + brainpower + 1;
        const take = points + (nextIdx < n ? dp[nextIdx] : 0);
        const skip = dp[i + 1];
        dp[i] = take > skip ? take : skip;
    }
    return dp[0];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $questions
     * @return Integer
     */
    function mostPoints($questions) {
        $n = count($questions);
        $dp = array_fill(0, $n + 1, 0); // dp[i] = max points starting from i

        for ($i = $n - 1; $i >= 0; --$i) {
            [$points, $brainpower] = $questions[$i];
            $nextIdx = $i + $brainpower + 1;
            if ($nextIdx > $n) {
                $nextIdx = $n;
            }
            $solve = $points + $dp[$nextIdx];
            $skip = $dp[$i + 1];
            $dp[$i] = max($solve, $skip);
        }

        return $dp[0];
    }
}
```

## Swift

```swift
class Solution {
    func mostPoints(_ questions: [[Int]]) -> Int {
        let n = questions.count
        var dp = Array(repeating: 0, count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            let points = questions[i][0]
            let brainpower = questions[i][1]
            let nextIdx = i + brainpower + 1
            let solve = points + (nextIdx < n ? dp[nextIdx] : 0)
            let skip = dp[i + 1]
            dp[i] = max(solve, skip)
        }
        return dp[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mostPoints(questions: Array<IntArray>): Long {
        val n = questions.size
        val dp = LongArray(n + 1)
        for (i in n - 1 downTo 0) {
            val points = questions[i][0].toLong()
            val brain = questions[i][1]
            val nextIdx = i + brain + 1
            val take = points + if (nextIdx < n) dp[nextIdx] else 0L
            val skip = dp[i + 1]
            dp[i] = if (take > skip) take else skip
        }
        return dp[0]
    }
}
```

## Dart

```dart
class Solution {
  int mostPoints(List<List<int>> questions) {
    final n = questions.length;
    final dp = List<int>.filled(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
      final points = questions[i][0];
      final brainpower = questions[i][1];
      final nextIdx = i + brainpower + 1;
      final solve = points + dp[nextIdx < n ? nextIdx : n];
      final skip = dp[i + 1];
      dp[i] = solve > skip ? solve : skip;
    }
    return dp[0];
  }
}
```

## Golang

```go
func mostPoints(questions [][]int) int64 {
	n := len(questions)
	dp := make([]int64, n+1) // dp[n] = 0 by default

	for i := n - 1; i >= 0; i-- {
		points := int64(questions[i][0])
		brain := questions[i][1]

		nextIdx := i + brain + 1
		if nextIdx > n {
			nextIdx = n
		}
		solve := points + dp[nextIdx]
		skip := dp[i+1]

		if solve > skip {
			dp[i] = solve
		} else {
			dp[i] = skip
		}
	}
	return dp[0]
}
```

## Ruby

```ruby
def most_points(questions)
  n = questions.length
  dp = Array.new(n + 1, 0)

  i = n - 1
  while i >= 0
    points, brain = questions[i]
    next_idx = i + brain + 1
    next_idx = n if next_idx > n

    solve = points + dp[next_idx]
    skip = dp[i + 1]

    dp[i] = solve > skip ? solve : skip
    i -= 1
  end

  dp[0]
end
```

## Scala

```scala
object Solution {
    def mostPoints(questions: Array[Array[Int]]): Long = {
        val n = questions.length
        val dp = new Array[Long](n + 1) // dp[n] = 0 by default
        var i = n - 1
        while (i >= 0) {
            val points = questions(i)(0).toLong
            val brain = questions(i)(1)
            val skip = dp(i + 1)
            val nextIdx = i + brain + 1
            val take = points + (if (nextIdx <= n) dp(nextIdx) else 0L)
            dp(i) = if (skip > take) skip else take
            i -= 1
        }
        dp(0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn most_points(questions: Vec<Vec<i32>>) -> i64 {
        let n = questions.len();
        let mut dp = vec![0i64; n + 1];
        for i in (0..n).rev() {
            let points = questions[i][0] as i64;
            let brain = questions[i][1] as usize;
            let next = i + brain + 1;
            let take = points + if next < n { dp[next] } else { 0 };
            let skip = dp[i + 1];
            dp[i] = if take > skip { take } else { skip };
        }
        dp[0]
    }
}
```

## Racket

```racket
(define/contract (most-points questions)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((qvec (list->vector questions))
         (n (vector-length qvec))
         (dp (make-vector (+ n 1) 0))) ; dp[n] = 0
    (for ([i (in-range (- n 1) -1 -1)])
      (define pair (vector-ref qvec i))
      (define points (first pair))
      (define brain (second pair))
      (define next-index (+ i brain 1))
      (define take (+ points (if (< next-index n) (vector-ref dp next-index) 0)))
      (define skip (vector-ref dp (+ i 1)))
      (vector-set! dp i (max take skip)))
    (vector-ref dp 0)))
```

## Erlang

```erlang
-module(solution).
-export([most_points/1]).
-spec most_points(Questions :: [[integer()]]) -> integer().
most_points(Questions) ->
    N = length(Questions),
    QTuple = list_to_tuple(Questions),
    DP0 = array:new(N, {default, 0}),
    DP = fill_dp(N - 1, QTuple, DP0, N),
    array:get(0, DP).

fill_dp(-1, _QTuple, DP, _N) ->
    DP;
fill_dp(I, QTuple, DP, N) ->
    [Points, Brain] = element(I + 1, QTuple),
    NextIdx = I + Brain + 1,
    Solve = Points + (if NextIdx < N -> array:get(NextIdx, DP); true -> 0 end),
    Skip = if I + 1 < N -> array:get(I + 1, DP); true -> 0 end,
    Best = if Solve > Skip -> Solve; true -> Skip end,
    DP2 = array:set(I, Best, DP),
    fill_dp(I - 1, QTuple, DP2, N).
```

## Elixir

```elixir
defmodule Solution do
  @spec most_points(questions :: [[integer]]) :: integer
  def most_points(questions) do
    n = length(questions)
    q_arr = :array.from_list(questions)
    dp0 = :array.new(n + 1, default: 0)

    dp_final = dp_loop(n - 1, n, q_arr, dp0)
    :array.get(0, dp_final)
  end

  defp dp_loop(i, _n, _q_arr, dp) when i < 0 do
    dp
  end

  defp dp_loop(i, n, q_arr, dp) do
    [points, brain] = :array.get(i, q_arr)

    next_idx = i + brain + 1
    solve =
      points +
        if next_idx <= n do
          :array.get(next_idx, dp)
        else
          0
        end

    skip = :array.get(i + 1, dp)
    best = if solve > skip, do: solve, else: skip

    dp2 = :array.set(i, best, dp)
    dp_loop(i - 1, n, q_arr, dp2)
  end
end
```
