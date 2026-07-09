# 2660. Determine the Winner of a Bowling Game

## Cpp

```cpp
class Solution {
public:
    int calculateScore(const vector<int>& a) {
        int n = a.size();
        int total = 0;
        for (int i = 0; i < n; ++i) {
            int val = a[i];
            if ((i - 1 >= 0 && a[i - 1] == 10) || (i - 2 >= 0 && a[i - 2] == 10)) {
                val *= 2;
            }
            total += val;
        }
        return total;
    }

    int isWinner(vector<int>& player1, vector<int>& player2) {
        int score1 = calculateScore(player1);
        int score2 = calculateScore(player2);
        if (score1 > score2) return 1;
        if (score2 > score1) return 2;
        return 0;
    }
};
```

## Java

```java
class Solution {
    public int isWinner(int[] player1, int[] player2) {
        int score1 = calculateScore(player1);
        int score2 = calculateScore(player2);
        if (score1 > score2) return 1;
        if (score2 > score1) return 2;
        return 0;
    }
    
    private int calculateScore(int[] pins) {
        int total = 0;
        for (int i = 0; i < pins.length; i++) {
            int val = pins[i];
            if ((i > 0 && pins[i - 1] == 10) || (i > 1 && pins[i - 2] == 10)) {
                val *= 2;
            }
            total += val;
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """
        def score(arr):
            total = 0
            n = len(arr)
            for i in range(n):
                mult = 1
                if (i >= 1 and arr[i-1] == 10) or (i >= 2 and arr[i-2] == 10):
                    mult = 2
                total += arr[i] * mult
            return total

        s1, s2 = score(player1), score(player2)
        if s1 > s2:
            return 1
        elif s2 > s1:
            return 2
        else:
            return 0
```

## Python3

```python
from typing import List

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(arr: List[int]) -> int:
            total = 0
            n = len(arr)
            for i in range(n):
                pins = arr[i]
                total += pins
                if pins != 10 and ((i > 0 and arr[i - 1] == 10) or (i > 1 and arr[i - 2] == 10)):
                    total += pins
            return total

        s1, s2 = score(player1), score(player2)
        if s1 > s2:
            return 1
        if s2 > s1:
            return 2
        return 0
```

## C

```c
int isWinner(int* player1, int player1Size, int* player2, int player2Size) {
    long long score1 = 0, score2 = 0;
    for (int i = 0; i < player1Size; ++i) {
        int mult = 1;
        if ((i > 0 && player1[i - 1] == 10) || (i > 1 && player1[i - 2] == 10))
            mult = 2;
        score1 += (long long)player1[i] * mult;
    }
    for (int i = 0; i < player2Size; ++i) {
        int mult = 1;
        if ((i > 0 && player2[i - 1] == 10) || (i > 1 && player2[i - 2] == 10))
            mult = 2;
        score2 += (long long)player2[i] * mult;
    }
    if (score1 > score2) return 1;
    if (score2 > score1) return 2;
    return 0;
}
```

## Csharp

```csharp
public class Solution {
    public int IsWinner(int[] player1, int[] player2) {
        long Score(int[] arr) {
            long total = 0;
            for (int i = 0; i < arr.Length; i++) {
                total += arr[i];
                bool bonus = (i > 0 && arr[i - 1] == 10) || (i > 1 && arr[i - 2] == 10);
                if (bonus) total += arr[i];
            }
            return total;
        }

        long s1 = Score(player1);
        long s2 = Score(player2);

        if (s1 > s2) return 1;
        if (s2 > s1) return 2;
        return 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} player1
 * @param {number[]} player2
 * @return {number}
 */
var isWinner = function(player1, player2) {
    const score = (arr) => {
        let total = 0;
        for (let i = 0; i < arr.length; i++) {
            let val = arr[i];
            if (i > 0 && arr[i - 1] === 10) {
                val *= 2;
            } else if (i > 1 && arr[i - 2] === 10) {
                val *= 2;
            }
            total += val;
        }
        return total;
    };
    
    const s1 = score(player1);
    const s2 = score(player2);
    
    if (s1 > s2) return 1;
    if (s2 > s1) return 2;
    return 0;
};
```

## Typescript

```typescript
function isWinner(player1: number[], player2: number[]): number {
    const score = (arr: number[]): number => {
        let total = 0;
        for (let i = 0; i < arr.length; i++) {
            const hit = arr[i];
            const double = (i >= 1 && arr[i - 1] === 10) || (i >= 2 && arr[i - 2] === 10);
            total += double ? hit * 2 : hit;
        }
        return total;
    };
    
    const s1 = score(player1);
    const s2 = score(player2);
    
    if (s1 > s2) return 1;
    if (s2 > s1) return 2;
    return 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $player1
     * @param Integer[] $player2
     * @return Integer
     */
    function isWinner($player1, $player2) {
        $calc = function($arr) {
            $total = 0;
            $n = count($arr);
            for ($i = 0; $i < $n; $i++) {
                $val = $arr[$i];
                if (($i > 0 && $arr[$i - 1] == 10) || ($i > 1 && $arr[$i - 2] == 10)) {
                    $val *= 2;
                }
                $total += $val;
            }
            return $total;
        };
        $score1 = $calc($player1);
        $score2 = $calc($player2);
        if ($score1 > $score2) return 1;
        if ($score2 > $score1) return 2;
        return 0;
    }
}
```

## Swift

```swift
class Solution {
    func isWinner(_ player1: [Int], _ player2: [Int]) -> Int {
        func score(_ arr: [Int]) -> Int {
            var total = 0
            for i in 0..<arr.count {
                total += arr[i]
                if i >= 1 && arr[i - 1] == 10 {
                    total += arr[i]
                } else if i >= 2 && arr[i - 2] == 10 {
                    total += arr[i]
                }
            }
            return total
        }
        let s1 = score(player1)
        let s2 = score(player2)
        if s1 > s2 { return 1 }
        if s1 < s2 { return 2 }
        return 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isWinner(player1: IntArray, player2: IntArray): Int {
        fun score(arr: IntArray): Int {
            var total = 0
            for (i in arr.indices) {
                val base = arr[i]
                val doubled = (i >= 1 && arr[i - 1] == 10) || (i >= 2 && arr[i - 2] == 10)
                total += if (doubled) base * 2 else base
            }
            return total
        }
        val s1 = score(player1)
        val s2 = score(player2)
        return when {
            s1 > s2 -> 1
            s2 > s1 -> 2
            else -> 0
        }
    }
}
```

## Dart

```dart
class Solution {
  int isWinner(List<int> player1, List<int> player2) {
    int score(List<int> p) {
      int total = 0;
      for (int i = 0; i < p.length; i++) {
        bool doubleTurn = false;
        if (i >= 1 && p[i - 1] == 10) doubleTurn = true;
        if (!doubleTurn && i >= 2 && p[i - 2] == 10) doubleTurn = true;
        total += p[i] * (doubleTurn ? 2 : 1);
      }
      return total;
    }

    int s1 = score(player1);
    int s2 = score(player2);
    if (s1 > s2) return 1;
    if (s2 > s1) return 2;
    return 0;
  }
}
```

## Golang

```go
func isWinner(player1 []int, player2 []int) int {
	calc := func(arr []int) int {
		sum := 0
		for i, v := range arr {
			mult := 1
			if i-1 >= 0 && arr[i-1] == 10 {
				mult = 2
			}
			if i-2 >= 0 && arr[i-2] == 10 {
				mult = 2
			}
			sum += v * mult
		}
		return sum
	}

	score1 := calc(player1)
	score2 := calc(player2)

	if score1 > score2 {
		return 1
	}
	if score2 > score1 {
		return 2
	}
	return 0
}
```

## Ruby

```ruby
def is_winner(player1, player2)
  calc_score = lambda do |arr|
    total = 0
    n = arr.length
    (0...n).each do |i|
      if arr[i] == 10
        total += 10
      elsif (i >= 1 && arr[i - 1] == 10) || (i >= 2 && arr[i - 2] == 10)
        total += 2 * arr[i]
      else
        total += arr[i]
      end
    end
    total
  end

  s1 = calc_score.call(player1)
  s2 = calc_score.call(player2)

  return 0 if s1 == s2
  s1 > s2 ? 1 : 2
end
```

## Scala

```scala
object Solution {
    def isWinner(player1: Array[Int], player2: Array[Int]): Int = {
        def total(arr: Array[Int]): Int = {
            var sum = 0
            for (i <- arr.indices) {
                if (i > 0 && arr(i - 1) == 10) sum += 2 * arr(i)
                else sum += arr(i)
            }
            sum
        }
        val s1 = total(player1)
        val s2 = total(player2)
        if (s1 > s2) 1
        else if (s2 > s1) 2
        else 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_winner(player1: Vec<i32>, player2: Vec<i32>) -> i32 {
        fn score(pins: &Vec<i32>) -> i32 {
            let mut total = 0;
            for i in 0..pins.len() {
                let doubled = (i >= 1 && pins[i - 1] == 10) || (i >= 2 && pins[i - 2] == 10);
                total += if doubled { 2 * pins[i] } else { pins[i] };
            }
            total
        }

        let s1 = score(&player1);
        let s2 = score(&player2);
        if s1 > s2 {
            1
        } else if s2 > s1 {
            2
        } else {
            0
        }
    }
}
```

## Racket

```racket
(define/contract (is-winner player1 player2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (define (score lst)
    (let* ((n (length lst))
           (vec (list->vector lst)))
      (let loop ((i 0) (total 0))
        (if (= i n)
            total
            (let* ((val (vector-ref vec i))
                   (double? (or (and (> i 0) (= (vector-ref vec (- i 1)) 10))
                                (and (> i 1) (= (vector-ref vec (- i 2)) 10)))))
              (loop (+ i 1) (+ total (if double? (* 2 val) val))))))))
  (let ((s1 (score player1))
        (s2 (score player2)))
    (cond [(> s1 s2) 1]
          [(< s1 s2) 2]
          [else 0])))
```

## Erlang

```erlang
-module(solution).
-export([is_winner/2]).

-spec is_winner(Player1 :: [integer()], Player2 :: [integer()]) -> integer().
is_winner(Player1, Player2) ->
    Score1 = score(Player1, -1, -1),
    Score2 = score(Player2, -1, -1),
    case Score1 > Score2 of
        true -> 1;
        false ->
            case Score1 < Score2 of
                true -> 2;
                false -> 0
            end
    end.

score([], _, _) -> 0;
score([X|Rest], Prev1, Prev2) ->
    Add = if (Prev1 == 10) orelse (Prev2 == 10) -> 2 * X; true -> X end,
    Add + score(Rest, X, Prev1).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_winner(player1 :: [integer], player2 :: [integer]) :: integer
  def is_winner(player1, player2) do
    s1 = score(player1)
    s2 = score(player2)

    cond do
      s1 > s2 -> 1
      s2 > s1 -> 2
      true -> 0
    end
  end

  defp score(pins) do
    {total, _, _} =
      Enum.reduce(pins, {0, nil, nil}, fn pin, {sum, prev1, prev2} ->
        double = (prev1 == 10) or (prev2 == 10)
        new_sum = sum + if double, do: pin * 2, else: pin
        {new_sum, pin, prev1}
      end)

    total
  end
end
```
