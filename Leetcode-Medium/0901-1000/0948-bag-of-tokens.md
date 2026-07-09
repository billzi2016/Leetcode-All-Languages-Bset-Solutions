# 0948. Bag of Tokens

## Cpp

```cpp
class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        sort(tokens.begin(), tokens.end());
        int l = 0, r = (int)tokens.size() - 1;
        int score = 0, maxScore = 0;
        while (l <= r) {
            if (power >= tokens[l]) {
                power -= tokens[l];
                ++score;
                ++l;
                maxScore = max(maxScore, score);
            } else if (score > 0) {
                power += tokens[r];
                --score;
                --r;
            } else {
                break;
            }
        }
        return maxScore;
    }
};
```

## Java

```java
class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        java.util.Arrays.sort(tokens);
        int low = 0;
        int high = tokens.length - 1;
        int score = 0;
        int maxScore = 0;

        while (low <= high) {
            if (power >= tokens[low]) {
                power -= tokens[low];
                score++;
                low++;
                if (score > maxScore) {
                    maxScore = score;
                }
            } else if (score > 0 && low < high) {
                power += tokens[high];
                score--;
                high--;
            } else {
                break;
            }
        }

        return maxScore;
    }
}
```

## Python

```python
class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        l, r = 0, len(tokens) - 1
        score = max_score = 0

        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
                if score > max_score:
                    max_score = score
            elif score > 0 and l < r:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break

        return max_score
```

## Python3

```python
from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1
        score = max_score = 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
                if score > max_score:
                    max_score = score
            elif score > 0 and l < r:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
        return max_score
```

## C

```c
int compareInt(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int bagOfTokensScore(int* tokens, int tokensSize, int power) {
    if (tokensSize == 0) return 0;
    qsort(tokens, (size_t)tokensSize, sizeof(int), compareInt);
    
    int low = 0, high = tokensSize - 1;
    int score = 0, maxScore = 0;
    
    while (low <= high && (power >= tokens[low] || score > 0)) {
        if (power >= tokens[low]) {
            power -= tokens[low];
            ++score;
            ++low;
            if (score > maxScore) maxScore = score;
        } else {
            power += tokens[high];
            --score;
            --high;
        }
    }
    
    return maxScore;
}
```

## Csharp

```csharp
public class Solution
{
    public int BagOfTokensScore(int[] tokens, int power)
    {
        if (tokens == null || tokens.Length == 0) return 0;
        Array.Sort(tokens);
        int low = 0;
        int high = tokens.Length - 1;
        int score = 0;
        int maxScore = 0;

        while (low <= high)
        {
            if (power >= tokens[low])
            {
                power -= tokens[low];
                score++;
                low++;
                if (score > maxScore) maxScore = score;
            }
            else if (score > 0 && low < high)
            {
                power += tokens[high];
                score--;
                high--;
            }
            else
            {
                break;
            }
        }

        return maxScore;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} tokens
 * @param {number} power
 * @return {number}
 */
var bagOfTokensScore = function(tokens, power) {
    if (!tokens || tokens.length === 0) return 0;
    tokens.sort((a, b) => a - b);
    let low = 0;
    let high = tokens.length - 1;
    let score = 0;
    let maxScore = 0;
    
    while (low <= high) {
        if (power >= tokens[low]) {
            power -= tokens[low];
            score++;
            low++;
            if (score > maxScore) maxScore = score;
        } else if (score > 0 && low < high) {
            power += tokens[high];
            score--;
            high--;
        } else {
            break;
        }
    }
    
    return maxScore;
};
```

## Typescript

```typescript
function bagOfTokensScore(tokens: number[], power: number): number {
    tokens.sort((a, b) => a - b);
    let low = 0;
    let high = tokens.length - 1;
    let score = 0;
    let maxScore = 0;

    while (low <= high) {
        if (power >= tokens[low]) {
            power -= tokens[low];
            score++;
            maxScore = Math.max(maxScore, score);
            low++;
        } else if (score > 0 && low < high) {
            power += tokens[high];
            score--;
            high--;
        } else {
            break;
        }
    }

    return maxScore;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $tokens
     * @param Integer $power
     * @return Integer
     */
    function bagOfTokensScore($tokens, $power) {
        sort($tokens);
        $low = 0;
        $high = count($tokens) - 1;
        $score = 0;
        $maxScore = 0;

        while ($low <= $high) {
            if ($power >= $tokens[$low]) {
                $power -= $tokens[$low];
                $score++;
                $low++;
                if ($score > $maxScore) {
                    $maxScore = $score;
                }
            } elseif ($score > 0) {
                $power += $tokens[$high];
                $score--;
                $high--;
            } else {
                break;
            }
        }

        return $maxScore;
    }
}
```

## Swift

```swift
class Solution {
    func bagOfTokensScore(_ tokens: [Int], _ power: Int) -> Int {
        let sorted = tokens.sorted()
        var low = 0
        var high = sorted.count - 1
        var curPower = power
        var score = 0
        var maxScore = 0

        while low <= high && low < sorted.count {
            if curPower >= sorted[low] {
                curPower -= sorted[low]
                score += 1
                low += 1
                if score > maxScore { maxScore = score }
            } else if score > 0 {
                curPower += sorted[high]
                score -= 1
                high -= 1
            } else {
                break
            }
        }

        return maxScore
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun bagOfTokensScore(tokens: IntArray, power: Int): Int {
        if (tokens.isEmpty()) return 0
        tokens.sort()
        var low = 0
        var high = tokens.lastIndex
        var curPower = power
        var score = 0
        var maxScore = 0

        while (low <= high) {
            if (curPower >= tokens[low]) {
                curPower -= tokens[low]
                score++
                low++
                if (score > maxScore) maxScore = score
            } else if (score > 0 && low < high) {
                curPower += tokens[high]
                score--
                high--
            } else {
                break
            }
        }

        return maxScore
    }
}
```

## Dart

```dart
class Solution {
  int bagOfTokensScore(List<int> tokens, int power) {
    tokens.sort();
    int low = 0;
    int high = tokens.length - 1;
    int score = 0;
    int maxScore = 0;

    while (low <= high) {
      if (power >= tokens[low]) {
        power -= tokens[low];
        score++;
        low++;
        if (score > maxScore) maxScore = score;
      } else if (score > 0 && low < high) {
        power += tokens[high];
        score--;
        high--;
      } else {
        break;
      }
    }

    return maxScore;
  }
}
```

## Golang

```go
import "sort"

func bagOfTokensScore(tokens []int, power int) int {
	if len(tokens) == 0 {
		return 0
	}
	sort.Ints(tokens)
	low, high := 0, len(tokens)-1
	score, maxScore := 0, 0

	for low <= high {
		if power >= tokens[low] {
			power -= tokens[low]
			score++
			low++
			if score > maxScore {
				maxScore = score
			}
		} else if score > 0 && low < high {
			power += tokens[high]
			score--
			high--
		} else {
			break
		}
	}
	return maxScore
}
```

## Ruby

```ruby
def bag_of_tokens_score(tokens, power)
  tokens.sort!
  low = 0
  high = tokens.length - 1
  score = 0
  max_score = 0

  while low <= high
    if power >= tokens[low]
      power -= tokens[low]
      score += 1
      low += 1
      max_score = score if score > max_score
    elsif score > 0 && low < high
      power += tokens[high]
      score -= 1
      high -= 1
    else
      break
    end
  end

  max_score
end
```

## Scala

```scala
object Solution {
  def bagOfTokensScore(tokens: Array[Int], power: Int): Int = {
    val sorted = tokens.sorted
    var low = 0
    var high = sorted.length - 1
    var curPower = power
    var score = 0
    var maxScore = 0

    while (low <= high && (curPower >= sorted(low) || score > 0)) {
      if (curPower >= sorted(low)) {
        curPower -= sorted(low)
        score += 1
        low += 1
        if (score > maxScore) maxScore = score
      } else {
        // need to trade score for power
        curPower += sorted(high)
        score -= 1
        high -= 1
      }
    }

    maxScore
  }
}
```

## Rust

```rust
impl Solution {
    pub fn bag_of_tokens_score(mut tokens: Vec<i32>, mut power: i32) -> i32 {
        if tokens.is_empty() {
            return 0;
        }
        tokens.sort();
        let n = tokens.len();
        let mut low = 0usize;
        let mut high = n - 1;
        let mut score = 0i32;
        let mut max_score = 0i32;

        while low <= high {
            if power >= tokens[low] {
                power -= tokens[low];
                score += 1;
                if score > max_score {
                    max_score = score;
                }
                low += 1;
            } else if score > 0 && low < high {
                power += tokens[high];
                score -= 1;
                // low < high guarantees high > 0
                high -= 1;
            } else {
                break;
            }
        }

        max_score
    }
}
```

## Racket

```racket
(define/contract (bag-of-tokens-score tokens power)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted (sort tokens <))
         (v (list->vector sorted))
         (n (vector-length v)))
    (let loop ((low 0) (high (sub1 n)) (p power) (score 0) (max-score 0))
      (if (> low high)
          max-score
          (cond
            [(>= p (vector-ref v low))
             (loop (+ low 1) high (- p (vector-ref v low)) (+ score 1)
                   (max max-score (+ score 1)))]
            [(and (> score 0) (< low high))
             (loop low (- high 1) (+ p (vector-ref v high)) (- score 1) max-score)]
            [else max-score])))))
```

## Erlang

```erlang
-spec bag_of_tokens_score(Tokens :: [integer()], Power :: integer()) -> integer().
bag_of_tokens_score(Tokens, Power) ->
    Sorted = lists:sort(Tokens),
    N = length(Sorted),
    loop(Sorted, Power, 0, 0, 0, N - 1).

loop(_Sorted, _Power, _Score, MaxScore, Low, High) when Low > High ->
    MaxScore;
loop(Sorted, Power, Score, MaxScore, Low, High) ->
    TokenLow = lists:nth(Low + 1, Sorted),
    case Power >= TokenLow of
        true ->
            NewPower = Power - TokenLow,
            NewScore = Score + 1,
            NewMax = erlang:max(NewScore, MaxScore),
            loop(Sorted, NewPower, NewScore, NewMax, Low + 1, High);
        false ->
            case (Score > 0) andalso (Low < High) of
                true ->
                    TokenHigh = lists:nth(High + 1, Sorted),
                    NewPower2 = Power + TokenHigh,
                    NewScore2 = Score - 1,
                    loop(Sorted, NewPower2, NewScore2, MaxScore, Low, High - 1);
                false ->
                    MaxScore
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec bag_of_tokens_score(tokens :: [integer], power :: integer) :: integer
  def bag_of_tokens_score(tokens, power) do
    sorted = Enum.sort(tokens)
    len = length(sorted)

    loop(sorted, 0, len - 1, power, 0, 0)
  end

  defp loop(_tokens, low, high, _power, _score, max_score) when low > high,
    do: max_score

  defp loop(tokens, low, high, power, score, max_score) do
    cond do
      power >= Enum.at(tokens, low) ->
        new_power = power - Enum.at(tokens, low)
        new_score = score + 1
        new_max = if new_score > max_score, do: new_score, else: max_score
        loop(tokens, low + 1, high, new_power, new_score, new_max)

      score > 0 and low < high ->
        new_power = power + Enum.at(tokens, high)
        new_score = score - 1
        loop(tokens, low, high - 1, new_power, new_score, max_score)

      true ->
        max_score
    end
  end
end
```
