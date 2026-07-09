# 1014. Best Sightseeing Pair

## Cpp

```cpp
class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int maxLeft = values[0]; // values[0] + 0
        int best = INT_MIN;
        for (int j = 1; j < (int)values.size(); ++j) {
            int current = maxLeft + values[j] - j;
            if (current > best) best = current;
            int leftScore = values[j] + j;
            if (leftScore > maxLeft) maxLeft = leftScore;
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        int maxLeft = values[0]; // values[0] + 0
        int maxScore = Integer.MIN_VALUE;
        for (int i = 1; i < values.length; i++) {
            int rightScore = values[i] - i;
            maxScore = Math.max(maxScore, maxLeft + rightScore);
            int leftScore = values[i] + i;
            if (leftScore > maxLeft) {
                maxLeft = leftScore;
            }
        }
        return maxScore;
    }
}
```

## Python

```python
class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        max_left = values[0]  # values[0] + 0
        max_score = 0
        for i in range(1, len(values)):
            # compute score with the best left spot so far
            current_score = max_left + values[i] - i
            if current_score > max_score:
                max_score = current_score
            # update best left spot (values[i] + i)
            left_candidate = values[i] + i
            if left_candidate > max_left:
                max_left = left_candidate
        return max_score
```

## Python3

```python
from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_left = values[0]  # values[i] + i where i=0
        best = 0
        for j in range(1, len(values)):
            # score with current right spot j and best left spot so far
            best = max(best, max_left + values[j] - j)
            # update best left value (values[i] + i) up to index j
            max_left = max(max_left, values[j] + j)
        return best
```

## C

```c
int maxScoreSightseeingPair(int* values, int valuesSize) {
    int maxLeft = values[0]; // values[0] + 0
    int maxScore = 0;
    for (int i = 1; i < valuesSize; ++i) {
        int currentScore = maxLeft + values[i] - i;
        if (currentScore > maxScore) {
            maxScore = currentScore;
        }
        int leftCandidate = values[i] + i;
        if (leftCandidate > maxLeft) {
            maxLeft = leftCandidate;
        }
    }
    return maxScore;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxScoreSightseeingPair(int[] values)
    {
        int maxLeft = values[0]; // values[0] + 0
        int maxScore = int.MinValue;

        for (int i = 1; i < values.Length; i++)
        {
            int currentScore = maxLeft + values[i] - i;
            if (currentScore > maxScore)
                maxScore = currentScore;

            int leftCandidate = values[i] + i;
            if (leftCandidate > maxLeft)
                maxLeft = leftCandidate;
        }

        return maxScore;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} values
 * @return {number}
 */
var maxScoreSightseeingPair = function(values) {
    let maxLeft = values[0]; // values[0] + 0
    let maxScore = Number.NEGATIVE_INFINITY;
    for (let i = 1; i < values.length; i++) {
        const currentScore = maxLeft + values[i] - i;
        if (currentScore > maxScore) maxScore = currentScore;
        const leftCandidate = values[i] + i;
        if (leftCandidate > maxLeft) maxLeft = leftCandidate;
    }
    return maxScore;
};
```

## Typescript

```typescript
function maxScoreSightseeingPair(values: number[]): number {
    let maxLeft = values[0]; // values[0] + 0
    let maxScore = -Infinity;
    for (let j = 1; j < values.length; ++j) {
        const rightScore = values[j] - j;
        maxScore = Math.max(maxScore, maxLeft + rightScore);
        const leftScore = values[j] + j;
        if (leftScore > maxLeft) {
            maxLeft = leftScore;
        }
    }
    return maxScore;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $values
     * @return Integer
     */
    function maxScoreSightseeingPair($values) {
        $n = count($values);
        // Initialize best left score (values[i] + i) with first element
        $maxLeft = $values[0]; // since i = 0, values[0] + 0
        $maxScore = PHP_INT_MIN;

        for ($i = 1; $i < $n; ++$i) {
            // Current pair score using best left so far and current right (values[i] - i)
            $currentScore = $maxLeft + $values[$i] - $i;
            if ($currentScore > $maxScore) {
                $maxScore = $currentScore;
            }

            // Update best left score for future pairs
            $leftScore = $values[$i] + $i;
            if ($leftScore > $maxLeft) {
                $maxLeft = $leftScore;
            }
        }

        return $maxScore;
    }
}
```

## Swift

```swift
class Solution {
    func maxScoreSightseeingPair(_ values: [Int]) -> Int {
        var maxLeft = values[0] // values[0] + 0
        var best = Int.min
        for j in 1..<values.count {
            let current = maxLeft + values[j] - j
            if current > best { best = current }
            let leftScore = values[j] + j
            if leftScore > maxLeft { maxLeft = leftScore }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxScoreSightseeingPair(values: IntArray): Int {
        var maxLeft = values[0] // values[i] + i for i = 0
        var result = 0
        for (j in 1 until values.size) {
            val currentScore = maxLeft + values[j] - j
            if (currentScore > result) result = currentScore
            val leftScore = values[j] + j
            if (leftScore > maxLeft) maxLeft = leftScore
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int maxScoreSightseeingPair(List<int> values) {
    int n = values.length;
    int maxLeft = values[0] + 0; // values[i] + i
    int best = 0;
    for (int j = 1; j < n; ++j) {
      int currentScore = maxLeft + values[j] - j; // values[i] + i + values[j] - j
      if (currentScore > best) best = currentScore;
      int leftCandidate = values[j] + j;
      if (leftCandidate > maxLeft) maxLeft = leftCandidate;
    }
    return best;
  }
}
```

## Golang

```go
func maxScoreSightseeingPair(values []int) int {
	if len(values) < 2 {
		return 0
	}
	maxLeft := values[0] // values[0] + 0
	maxScore := 0
	for j := 1; j < len(values); j++ {
		current := maxLeft + values[j] - j
		if current > maxScore {
			maxScore = current
		}
		leftScore := values[j] + j
		if leftScore > maxLeft {
			maxLeft = leftScore
		}
	}
	return maxScore
}
```

## Ruby

```ruby
def max_score_sightseeing_pair(values)
  max_left = values[0]
  max_score = 0
  (1...values.length).each do |i|
    cur = values[i] - i
    score = max_left + cur
    max_score = score if score > max_score
    left = values[i] + i
    max_left = left if left > max_left
  end
  max_score
end
```

## Scala

```scala
object Solution {
    def maxScoreSightseeingPair(values: Array[Int]): Int = {
        var maxLeft = values(0) // values[0] + 0
        var maxScore = Int.MinValue
        for (i <- 1 until values.length) {
            val rightScore = values(i) - i
            maxScore = math.max(maxScore, maxLeft + rightScore)
            val leftScore = values(i) + i
            if (leftScore > maxLeft) maxLeft = leftScore
        }
        maxScore
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_score_sightseeing_pair(values: Vec<i32>) -> i32 {
        let n = values.len();
        if n < 2 {
            return 0;
        }
        let mut max_left = values[0]; // values[0] + 0
        let mut best = i32::MIN;
        for j in 1..n {
            let right_score = values[j] - j as i32;
            let current = max_left + right_score;
            if current > best {
                best = current;
            }
            let left_candidate = values[j] + j as i32;
            if left_candidate > max_left {
                max_left = left_candidate;
            }
        }
        best
    }
}
```

## Racket

```racket
(define/contract (max-score-sightseeing-pair values)
  (-> (listof exact-integer?) exact-integer?)
  (if (< (length values) 2)
      (error "values must contain at least two elements")
      (let* ((first (car values))
             (initial-max-left (+ first 0))) ; values[0] + 0
        (let loop ((rest (cdr values))          ; remaining elements
                   (idx 1)                     ; current index j
                   (max-left initial-max-left) ; max_{i<j} (values[i] + i)
                   (max-score -1000000))       ; sufficiently small sentinel
          (if (null? rest)
              max-score
              (let* ((v (car rest))
                     (current (+ max-left (- v idx)))               ; max-left + values[j] - j
                     (new-max-score (if (> current max-score) current max-score))
                     (candidate-left (+ v idx))                      ; values[j] + j
                     (new-max-left (if (> candidate-left max-left) candidate-left max-left)))
                (loop (cdr rest) (add1 idx) new-max-left new-max-score)))))))
```

## Erlang

```erlang
-spec max_score_sightseeing_pair(Values :: [integer()]) -> integer().
max_score_sightseeing_pair(Values) ->
    case Values of
        [] -> 0;
        [_] -> 0;
        [First | Rest] ->
            InitMaxLeft = First,
            {_, MaxScore} =
                lists:foldl(
                    fun({V, I}, {CurMaxLeft, CurMaxScore}) ->
                        Right = V - I,
                        Candidate = CurMaxLeft + Right,
                        NewMaxScore = erlang:max(CurMaxScore, Candidate),
                        Left = V + I,
                        NewMaxLeft = erlang:max(CurMaxLeft, Left),
                        {NewMaxLeft, NewMaxScore}
                    end,
                    {InitMaxLeft, 0},
                    lists:zip(Rest, lists:seq(1, length(Rest)))
                ),
            MaxScore
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_score_sightseeing_pair(values :: [integer]) :: integer
  def max_score_sightseeing_pair(values) do
    [first | rest] = values
    init_max_left = first

    {max_score, _} =
      Enum.with_index(rest, 1)
      |> Enum.reduce({-1_000_000_000, init_max_left}, fn {val, idx}, {cur_max, max_left} ->
        score = max_left + val - idx
        new_max = if score > cur_max, do: score, else: cur_max
        new_max_left = if val + idx > max_left, do: val + idx, else: max_left
        {new_max, new_max_left}
      end)

    max_score
  end
end
```
