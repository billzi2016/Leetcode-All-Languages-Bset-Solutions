# 1535. Find the Winner of an Array Game

## Cpp

```cpp
class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        int n = arr.size();
        int maxVal = *max_element(arr.begin(), arr.end());
        if (k >= n - 1) return maxVal;
        
        int cur = arr[0];
        int streak = 0;
        for (int i = 1; i < n; ++i) {
            int opp = arr[i];
            if (cur > opp) {
                ++streak;
            } else {
                cur = opp;
                streak = 1;
            }
            if (streak == k || cur == maxVal) return cur;
        }
        return cur;
    }
};
```

## Java

```java
class Solution {
    public int getWinner(int[] arr, int k) {
        int n = arr.length;
        int max = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] > max) max = arr[i];
        }
        if (k >= n) return max;

        int cur = arr[0];
        int streak = 0;
        for (int i = 1; i < n; i++) {
            int opp = arr[i];
            if (cur > opp) {
                streak++;
            } else {
                cur = opp;
                streak = 1;
            }
            if (streak == k || cur == max) return cur;
        }
        return cur;
    }
}
```

## Python

```python
class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        if k >= n - 1:
            return max(arr)
        cur = arr[0]
        win = 0
        for i in range(1, n):
            opp = arr[i]
            if cur > opp:
                win += 1
            else:
                cur = opp
                win = 1
            if win == k:
                return cur
        return cur
```

## Python3

```python
from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_elem = max(arr)
        cur = arr[0]
        win = 0
        for opp in arr[1:]:
            if cur > opp:
                win += 1
            else:
                cur = opp
                win = 1
            if win == k or cur == max_elem:
                return cur
        return cur
```

## C

```c
int getWinner(int* arr, int arrSize, int k) {
    int maxVal = arr[0];
    for (int i = 1; i < arrSize; ++i) {
        if (arr[i] > maxVal) maxVal = arr[i];
    }
    
    int cur = arr[0];
    int winStreak = 0;
    
    for (int i = 1; i < arrSize; ++i) {
        if (cur > arr[i]) {
            ++winStreak;
        } else {
            cur = arr[i];
            winStreak = 1;
        }
        if (winStreak == k || cur == maxVal) {
            return cur;
        }
    }
    
    return cur; // cur will be the maximum element
}
```

## Csharp

```csharp
using System;
using System.Linq;

public class Solution {
    public int GetWinner(int[] arr, int k) {
        int n = arr.Length;
        int maxVal = arr.Max();

        // If k is large enough, the maximum element will inevitably win.
        if (k >= n - 1) return maxVal;

        int current = arr[0];
        int streak = 0;

        for (int i = 1; i < n; i++) {
            int opponent = arr[i];
            if (current > opponent) {
                streak++;
            } else {
                current = opponent;
                streak = 1;
            }

            if (streak == k || current == maxVal) {
                return current;
            }
        }

        // The loop should always return before reaching here.
        return current;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var getWinner = function(arr, k) {
    const n = arr.length;
    let maxVal = arr[0];
    for (let i = 1; i < n; i++) {
        if (arr[i] > maxVal) maxVal = arr[i];
    }
    // If k is large enough, the maximum element will inevitably win.
    if (k >= n) return maxVal;

    let cur = arr[0];
    let streak = 0;
    for (let i = 1; i < n; i++) {
        const opponent = arr[i];
        if (cur > opponent) {
            streak++;
        } else {
            cur = opponent;
            streak = 1;
        }
        if (streak === k || cur === maxVal) return cur;
    }
    // In practice we should have returned inside the loop.
    return cur;
};
```

## Typescript

```typescript
function getWinner(arr: number[], k: number): number {
    const n = arr.length;
    let maxVal = arr[0];
    for (let i = 1; i < n; i++) {
        if (arr[i] > maxVal) maxVal = arr[i];
    }
    if (k >= n - 1) return maxVal;

    let current = arr[0];
    let streak = 0;
    for (let i = 1; i < n; i++) {
        const opponent = arr[i];
        if (current > opponent) {
            streak++;
        } else {
            current = opponent;
            streak = 1;
        }
        if (streak === k || current === maxVal) return current;
    }
    return maxVal;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function getWinner($arr, $k) {
        $max = max($arr);
        $curr = $arr[0];
        $winStreak = 0;
        $n = count($arr);

        // If the first element is already the maximum, it will eventually win.
        if ($curr == $max) {
            return $curr;
        }

        for ($i = 1; $i < $n; $i++) {
            $opponent = $arr[$i];
            if ($curr > $opponent) {
                $winStreak++;
            } else {
                $curr = $opponent;
                $winStreak = 1;
            }

            if ($winStreak == $k || $curr == $max) {
                return $curr;
            }
        }

        // If loop finishes without returning, the maximum element is the winner.
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func getWinner(_ arr: [Int], _ k: Int) -> Int {
        let n = arr.count
        if k >= n {
            return arr.max()!
        }
        var current = arr[0]
        var winStreak = 0
        let maxElement = arr.max()!
        for i in 1..<n {
            let opponent = arr[i]
            if current > opponent {
                winStreak += 1
            } else {
                current = opponent
                winStreak = 1
            }
            if winStreak == k || current == maxElement {
                return current
            }
        }
        return maxElement
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getWinner(arr: IntArray, k: Int): Int {
        val maxVal = arr.maxOrNull()!!
        if (k >= arr.size) return maxVal
        var cur = arr[0]
        var streak = 0
        for (i in 1 until arr.size) {
            val opponent = arr[i]
            if (cur > opponent) {
                streak++
            } else {
                cur = opponent
                streak = 1
            }
            if (streak == k || cur == maxVal) return cur
        }
        return cur
    }
}
```

## Dart

```dart
class Solution {
  int getWinner(List<int> arr, int k) {
    int n = arr.length;
    int maxVal = arr[0];
    for (int i = 1; i < n; i++) {
      if (arr[i] > maxVal) maxVal = arr[i];
    }
    // If k is large enough, the maximum element will inevitably win.
    if (k >= n - 1) return maxVal;

    int current = arr[0];
    int streak = 0;

    for (int i = 1; i < n; i++) {
      int opponent = arr[i];
      if (current > opponent) {
        streak++;
      } else {
        current = opponent;
        streak = 1;
      }
      if (streak == k || current == maxVal) return current;
    }

    // The loop always returns before reaching here, but keep for completeness.
    return current;
  }
}
```

## Golang

```go
func getWinner(arr []int, k int) int {
	n := len(arr)
	// Find maximum element
	maxVal := arr[0]
	for _, v := range arr {
		if v > maxVal {
			maxVal = v
		}
	}
	// If k is large enough, the maximum will inevitably win
	if k >= n-1 {
		return maxVal
	}

	curr := arr[0]
	winStreak := 0

	for i := 1; i < n; i++ {
		opponent := arr[i]
		if curr > opponent {
			winStreak++
		} else {
			curr = opponent
			winStreak = 1
		}
		if winStreak == k || curr == maxVal {
			return curr
		}
	}
	return curr
}
```

## Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def get_winner(arr, k)
  max_val = arr.max
  curr = arr[0]
  win_streak = 0

  arr[1..-1].each do |opponent|
    if curr > opponent
      win_streak += 1
    else
      curr = opponent
      win_streak = 1
    end
    return curr if win_streak == k || curr == max_val
  end

  curr
end
```

## Scala

```scala
object Solution {
  def getWinner(arr: Array[Int], k: Int): Int = {
    val maxVal = arr.max
    var cur = arr(0)
    var streak = 0
    for (i <- 1 until arr.length) {
      val opp = arr(i)
      if (cur > opp) {
        streak += 1
      } else {
        cur = opp
        streak = 1
      }
      if (streak >= k || cur == maxVal) return cur
    }
    cur
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn get_winner(arr: Vec<i32>, k: i32) -> i32 {
        let n = arr.len();
        let max_val = *arr.iter().max().unwrap();

        if (k as usize) >= n - 1 {
            return max_val;
        }

        let mut dq: VecDeque<i32> = VecDeque::with_capacity(n - 1);
        for i in 1..n {
            dq.push_back(arr[i]);
        }

        let mut cur = arr[0];
        let mut streak = 0;

        loop {
            let opponent = dq.pop_front().unwrap();
            if cur > opponent {
                dq.push_back(opponent);
                streak += 1;
            } else {
                dq.push_back(cur);
                cur = opponent;
                streak = 1;
            }

            if streak >= k || cur == max_val {
                return cur;
            }
        }
    }
}
```

## Racket

```racket
(define/contract (get-winner arr k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length arr))
         (max-element (apply max arr)))
    (if (>= k n)
        max-element
        (let loop ((curr (first arr))
                   (streak 0)
                   (rest (rest arr)))
          (cond
            [(= curr max-element) max-element]
            [(null? rest) max-element] ; safety, should not happen
            [else
             (let ((opponent (first rest)))
               (if (> curr opponent)
                   (let ((new-streak (+ streak 1)))
                     (if (= new-streak k)
                         curr
                         (loop curr new-streak (rest rest))))
                   (let ((new-streak 1))
                     (if (= new-streak k)
                         opponent
                         (loop opponent new-streak (rest rest))))))])))))
```

## Erlang

```erlang
-module(solution).
-export([get_winner/2]).

-spec get_winner(Arr :: [integer()], K :: integer()) -> integer().
get_winner(Arr, K) ->
    Max = lists:max(Arr),
    case K >= length(Arr) of
        true -> Max;
        false ->
            [Curr | Rest] = Arr,
            loop(Curr, Rest, 0, K, Max)
    end.

loop(Curr, _Rest, _WinStreak, _K, Max) when Curr =:= Max ->
    Max;
loop(_Curr, [], _WinStreak, _K, Max) ->
    Max; % should never be reached
loop(Curr, [Opp | Tail], WinStreak, K, Max) ->
    case Curr > Opp of
        true ->
            NewWin = WinStreak + 1,
            if
                NewWin >= K -> Curr;
                true -> loop(Curr, Tail, NewWin, K, Max)
            end;
        false ->
            % Opp wins this round
            case K =:= 1 of
                true -> Opp;
                false ->
                    case Opp =:= Max of
                        true -> Max;
                        false -> loop(Opp, Tail, 1, K, Max)
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_winner(arr :: [integer], k :: integer) :: integer
  def get_winner(arr, k) do
    max_val = Enum.max(arr)
    n = length(arr)

    if k >= n - 1 do
      max_val
    else
      [curr | rest] = arr
      simulate(curr, rest, max_val, k, 0)
    end
  end

  defp simulate(_curr, [], max_val, _k, _streak), do: max_val

  defp simulate(curr, [opponent | rest], max_val, k, streak) do
    cond do
      curr > opponent ->
        new_streak = streak + 1

        if new_streak == k or curr == max_val do
          curr
        else
          simulate(curr, rest, max_val, k, new_streak)
        end

      true ->
        # opponent wins
        if 1 == k or opponent == max_val do
          opponent
        else
          simulate(opponent, rest, max_val, k, 1)
        end
    end
  end
end
```
