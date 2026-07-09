# 0473. Matchsticks to Square

## Cpp

```cpp
class Solution {
public:
    bool makesquare(vector<int>& matchsticks) {
        int n = matchsticks.size();
        if (n < 4) return false;
        long long sum = 0;
        for (int v : matchsticks) sum += v;
        if (sum % 4 != 0) return false;
        int target = sum / 4;
        sort(matchsticks.rbegin(), matchsticks.rend());
        if (matchsticks[0] > target) return false;
        vector<int> sides(4, 0);
        function<bool(int)> dfs = [&](int idx) -> bool {
            if (idx == n) {
                // all sticks placed, check if all sides equal target
                return sides[0] == target && sides[1] == target &&
                       sides[2] == target && sides[3] == target;
            }
            int cur = matchsticks[idx];
            for (int i = 0; i < 4; ++i) {
                if (sides[i] + cur > target) continue;
                sides[i] += cur;
                if (dfs(idx + 1)) return true;
                sides[i] -= cur;
                // pruning: if this side was empty before placing cur,
                // no need to try other empty sides (avoid symmetric states)
                if (sides[i] == 0) break;
            }
            return false;
        };
        return dfs(0);
    }
};
```

## Java

```java
class Solution {
    public boolean makesquare(int[] matchsticks) {
        int n = matchsticks.length;
        if (n < 4) return false;
        long sum = 0;
        for (int v : matchsticks) sum += v;
        if (sum % 4 != 0) return false;
        int target = (int)(sum / 4);
        java.util.Arrays.sort(matchsticks);
        for (int i = 0; i < n / 2; ++i) {
            int tmp = matchsticks[i];
            matchsticks[i] = matchsticks[n - 1 - i];
            matchsticks[n - 1 - i] = tmp;
        }
        if (matchsticks[0] > target) return false;
        int[] sides = new int[4];
        return dfs(0, matchsticks, sides, target);
    }

    private boolean dfs(int index, int[] sticks, int[] sides, int target) {
        if (index == sticks.length) {
            return sides[0] == target && sides[1] == target &&
                   sides[2] == target && sides[3] == target;
        }
        int cur = sticks[index];
        for (int i = 0; i < 4; ++i) {
            if (sides[i] + cur <= target) {
                boolean duplicate = false;
                for (int j = 0; j < i; ++j) {
                    if (sides[j] == sides[i]) {
                        duplicate = true;
                        break;
                    }
                }
                if (duplicate) continue;
                sides[i] += cur;
                if (dfs(index + 1, sticks, sides, target)) return true;
                sides[i] -= cur;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        if len(matchsticks) < 4:
            return False
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False

        sides = [0] * 4

        def dfs(index):
            if index == len(matchsticks):
                # all sticks used, check if all sides equal target
                return sides[0] == sides[1] == sides[2] == target
            cur = matchsticks[index]
            for i in range(4):
                if sides[i] + cur <= target:
                    sides[i] += cur
                    if dfs(index + 1):
                        return True
                    sides[i] -= cur
                # if this side is still 0 after trying, no need to try other empty sides (symmetry)
                if sides[i] == 0:
                    break
            return False

        return dfs(0)
```

## Python3

```python
from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0 or len(matchsticks) < 4:
            return False
        side_len = total // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > side_len:
            return False

        sides = [0, 0, 0, 0]

        def dfs(idx: int) -> bool:
            if idx == len(matchsticks):
                # All sticks placed; since we never exceed side_len,
                # reaching here means a valid square.
                return sides[0] == sides[1] == sides[2] == side_len
            stick = matchsticks[idx]
            for i in range(4):
                if sides[i] + stick <= side_len:
                    sides[i] += stick
                    if dfs(idx + 1):
                        return True
                    sides[i] -= stick
                # If this side is still zero after trying, no need to try other empty sides (symmetry)
                if sides[i] == 0:
                    break
            return False

        return dfs(0)
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

static int target;
static int *sticks;
static int n;
static int sides[4];

static int cmp_desc(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return vb - va; // descending
}

static bool dfs(int idx) {
    if (idx == n) {
        // All sticks placed successfully
        return true;
    }
    int cur = sticks[idx];
    for (int i = 0; i < 4; ++i) {
        if (sides[i] + cur <= target) {
            sides[i] += cur;
            if (dfs(idx + 1))
                return true;
            sides[i] -= cur;
        }
        // If this side is empty, no need to try other empty sides
        if (sides[i] == 0)
            break;
    }
    return false;
}

bool makesquare(int* matchsticks, int matchsticksSize) {
    if (matchsticksSize < 4)
        return false;

    long long sum = 0;
    for (int i = 0; i < matchsticksSize; ++i)
        sum += matchsticks[i];

    if (sum % 4 != 0)
        return false;

    target = (int)(sum / 4);
    sticks = matchsticks;
    n = matchsticksSize;

    qsort(sticks, n, sizeof(int), cmp_desc);

    if (sticks[0] > target)
        return false;

    for (int i = 0; i < 4; ++i)
        sides[i] = 0;

    return dfs(0);
}
```

## Csharp

```csharp
public class Solution
{
    public bool Makesquare(int[] matchsticks)
    {
        if (matchsticks == null || matchsticks.Length < 4)
            return false;

        long total = 0;
        foreach (int stick in matchsticks)
            total += stick;

        if (total % 4 != 0)
            return false;

        int sideLength = (int)(total / 4);
        Array.Sort(matchsticks);
        Array.Reverse(matchsticks); // descending order

        if (matchsticks[0] > sideLength)
            return false;

        int[] sides = new int[4];
        return Dfs(0, matchsticks, sides, sideLength);
    }

    private bool Dfs(int index, int[] sticks, int[] sides, int target)
    {
        if (index == sticks.Length)
        {
            // All sticks placed; since we never exceed target,
            // reaching here means all sides equal target.
            return true;
        }

        int stick = sticks[index];
        for (int i = 0; i < 4; i++)
        {
            if (sides[i] + stick <= target)
            {
                sides[i] += stick;
                if (Dfs(index + 1, sticks, sides, target))
                    return true;
                sides[i] -= stick;
            }

            // If this side is still 0 after trying, no need to try other empty sides
            if (sides[i] == 0)
                break;
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} matchsticks
 * @return {boolean}
 */
var makesquare = function(matchsticks) {
    const total = matchsticks.reduce((a, b) => a + b, 0);
    if (total % 4 !== 0) return false;
    const target = total / 4;

    // Sort in descending order to prune early
    matchsticks.sort((a, b) => b - a);
    if (matchsticks[0] > target) return false;

    const sides = new Array(4).fill(0);

    function dfs(idx) {
        if (idx === matchsticks.length) {
            // All sticks placed; all sides must equal target
            return sides[0] === target && sides[1] === target &&
                   sides[2] === target && sides[3] === target;
        }
        const stick = matchsticks[idx];
        for (let i = 0; i < 4; i++) {
            if (sides[i] + stick <= target) {
                sides[i] += stick;
                if (dfs(idx + 1)) return true;
                sides[i] -= stick;
            }
            // If this side is still zero, placing the current stick in any other empty side
            // would be symmetric; break to avoid duplicate work.
            if (sides[i] === 0) break;
        }
        return false;
    }

    return dfs(0);
};
```

## Typescript

```typescript
function makesquare(matchsticks: number[]): boolean {
    const n = matchsticks.length;
    if (n < 4) return false;

    const total = matchsticks.reduce((sum, len) => sum + len, 0);
    if (total % 4 !== 0) return false;
    const target = total / 4;

    // If any stick is longer than the side length, impossible
    for (const len of matchsticks) {
        if (len > target) return false;
    }

    // Sort descending to place larger sticks first (prunes faster)
    matchsticks.sort((a, b) => b - a);

    const sides = new Array(4).fill(0);

    function dfs(index: number): boolean {
        if (index === n) {
            // All sticks placed; all sides must equal target
            return sides[0] === target && sides[1] === target && sides[2] === target && sides[3] === target;
        }

        const stick = matchsticks[index];
        for (let i = 0; i < 4; i++) {
            if (sides[i] + stick <= target) {
                sides[i] += stick;
                if (dfs(index + 1)) return true;
                sides[i] -= stick;
            }
            // If this side is still 0 after trying, no need to try other empty sides
            if (sides[i] === 0) break;
        }
        return false;
    }

    return dfs(0);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $matchsticks
     * @return Boolean
     */
    function makesquare($matchsticks) {
        $n = count($matchsticks);
        if ($n < 4) return false;
        $sum = array_sum($matchsticks);
        if ($sum % 4 !== 0) return false;
        $target = intdiv($sum, 4);
        rsort($matchsticks); // descending order for better pruning
        if ($matchsticks[0] > $target) return false;
        $sides = [0, 0, 0, 0];
        return $this->dfs(0, $matchsticks, $target, $sides);
    }

    private function dfs($index, $sticks, $target, &$sides) {
        if ($index === count($sticks)) {
            // all sticks placed; sides must all equal target
            return $sides[0] === $target && $sides[1] === $target &&
                   $sides[2] === $target && $sides[3] === $target;
        }
        $len = $sticks[$index];
        for ($i = 0; $i < 4; $i++) {
            if ($sides[$i] + $len <= $target) {
                $sides[$i] += $len;
                if ($this->dfs($index + 1, $sticks, $target, $sides)) {
                    return true;
                }
                $sides[$i] -= $len;
            }
            // If this side is still zero after trying, no need to try other empty sides
            if ($sides[$i] === 0) break;
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func makesquare(_ matchsticks: [Int]) -> Bool {
        let n = matchsticks.count
        if n < 4 { return false }
        let total = matchsticks.reduce(0, +)
        if total % 4 != 0 { return false }
        let target = total / 4
        
        var sticks = matchsticks.sorted(by: >)
        if sticks[0] > target { return false }
        
        var sides = [Int](repeating: 0, count: 4)
        
        func dfs(_ index: Int) -> Bool {
            if index == n {
                return sides.allSatisfy { $0 == target }
            }
            let stick = sticks[index]
            var usedLengths = Set<Int>()
            for i in 0..<4 {
                if sides[i] + stick <= target && !usedLengths.contains(sides[i]) {
                    usedLengths.insert(sides[i])
                    sides[i] += stick
                    if dfs(index + 1) { return true }
                    sides[i] -= stick
                }
                // If this side is still zero after trying, no need to try other empty sides
                if sides[i] == 0 { break }
            }
            return false
        }
        
        return dfs(0)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun makesquare(matchsticks: IntArray): Boolean {
        val total = matchsticks.sum()
        if (total % 4 != 0) return false
        val target = total / 4

        matchsticks.sort()
        val n = matchsticks.size
        if (matchsticks[n - 1] > target) return false

        val sides = IntArray(4)

        fun dfs(idx: Int): Boolean {
            if (idx < 0) {
                // all sticks placed, check if each side reached the target
                return sides[0] == target && sides[1] == target &&
                       sides[2] == target && sides[3] == target
            }
            val stick = matchsticks[idx]
            for (i in 0..3) {
                if (sides[i] + stick <= target) {
                    sides[i] += stick
                    if (dfs(idx - 1)) return true
                    sides[i] -= stick
                }
                // If this side is still zero after trying, no need to try other empty sides
                if (sides[i] == 0) break
            }
            return false
        }

        return dfs(n - 1)
    }
}
```

## Dart

```dart
class Solution {
  bool makesquare(List<int> matchsticks) {
    if (matchsticks.isEmpty) return false;
    int total = matchsticks.reduce((a, b) => a + b);
    if (total % 4 != 0) return false;
    int target = total ~/ 4;

    // If any stick is longer than the side length, impossible.
    for (int len in matchsticks) {
      if (len > target) return false;
    }

    // Sort descending to improve pruning.
    matchsticks.sort((a, b) => b.compareTo(a));

    List<int> sides = List.filled(4, 0);

    bool dfs(int index) {
      if (index == matchsticks.length) {
        // All sticks placed; check if all sides equal target.
        return sides[0] == target &&
            sides[1] == target &&
            sides[2] == target &&
            sides[3] == target;
      }
      int stick = matchsticks[index];
      for (int i = 0; i < 4; i++) {
        if (sides[i] + stick <= target) {
          sides[i] += stick;
          if (dfs(index + 1)) return true;
          sides[i] -= stick;
        }
        // If this side is still zero after trying, no need to try other empty sides.
        if (sides[i] == 0) break;
      }
      return false;
    }

    return dfs(0);
  }
}
```

## Golang

```go
package main

import "sort"

func makesquare(matchsticks []int) bool {
	n := len(matchsticks)
	if n < 4 {
		return false
	}
	sum := 0
	for _, v := range matchsticks {
		sum += v
	}
	if sum%4 != 0 {
		return false
	}
	side := sum / 4

	sort.Slice(matchsticks, func(i, j int) bool { return matchsticks[i] > matchsticks[j] })
	if matchsticks[0] > side {
		return false
	}

	sides := make([]int, 4)

	var dfs func(int) bool
	dfs = func(idx int) bool {
		if idx == n {
			return sides[0] == side && sides[1] == side && sides[2] == side && sides[3] == side
		}
		cur := matchsticks[idx]
		for i := 0; i < 4; i++ {
			if sides[i]+cur <= side {
				sides[i] += cur
				if dfs(idx + 1) {
					return true
				}
				sides[i] -= cur
			}
			// if this side is still zero after trying, no need to try other empty sides
			if sides[i] == 0 {
				break
			}
		}
		return false
	}

	return dfs(0)
}
```

## Ruby

```ruby
def makesquare(matchsticks)
  total = matchsticks.sum
  return false if total % 4 != 0
  side = total / 4

  matchsticks.sort!.reverse!
  return false if matchsticks[0] > side

  sides = [0, 0, 0, 0]

  dfs = lambda do |idx|
    if idx == matchsticks.length
      return sides.all? { |s| s == side }
    end

    stick = matchsticks[idx]
    (0...4).each do |i|
      next if sides[i] + stick > side

      # skip duplicate states
      duplicate = false
      (0...i).each do |j|
        if sides[j] == sides[i]
          duplicate = true
          break
        end
      end
      next if duplicate

      sides[i] += stick
      return true if dfs.call(idx + 1)
      sides[i] -= stick
    end
    false
  end

  dfs.call(0)
end
```

## Scala

```scala
object Solution {
  def makesquare(matchsticks: Array[Int]): Boolean = {
    val total = matchsticks.sum
    if (total % 4 != 0) return false
    val target = total / 4

    // sort in descending order to improve pruning
    val sticks = matchsticks.sorted(Ordering[Int].reverse)
    if (sticks.isEmpty || sticks(0) > target) return false

    val sides = new Array[Int](4)

    def dfs(index: Int): Boolean = {
      if (index == sticks.length) return true // all sticks placed, sides must be equal to target
      val stick = sticks(index)
      var i = 0
      while (i < 4) {
        if (sides(i) + stick <= target) {
          sides(i) += stick
          if (dfs(index + 1)) return true
          sides(i) -= stick
        }
        // If this side is still zero after trying, no need to try other empty sides (symmetry pruning)
        if (sides(i) == 0) i = 4 else i += 1
      }
      false
    }

    dfs(0)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn makesquare(mut matchsticks: Vec<i32>) -> bool {
        let n = matchsticks.len();
        if n < 4 {
            return false;
        }
        let sum: i32 = matchsticks.iter().sum();
        if sum % 4 != 0 {
            return false;
        }
        let target = sum / 4;
        matchsticks.sort_unstable_by(|a, b| b.cmp(a));
        if matchsticks[0] > target {
            return false;
        }

        fn dfs(idx: usize, sticks: &Vec<i32>, sides: &mut [i32; 4], target: i32) -> bool {
            if idx == sticks.len() {
                return true;
            }
            let stick = sticks[idx];
            for i in 0..4 {
                if sides[i] + stick <= target {
                    sides[i] += stick;
                    if dfs(idx + 1, sticks, sides, target) {
                        return true;
                    }
                    sides[i] -= stick;
                }
                // If this side is still zero after trying, no need to try other empty sides
                if sides[i] == 0 {
                    break;
                }
            }
            false
        }

        let mut sides = [0i32; 4];
        dfs(0, &matchsticks, &mut sides, target)
    }
}
```

## Racket

```racket
(define/contract (makesquare matchsticks)
  (-> (listof exact-integer?) boolean?)
  (let* ((n (length matchsticks))
         (total (apply + matchsticks)))
    (if (or (< n 4) (not (= (remainder total 4) 0)))
        #false
        (let* ((target (/ total 4))
               (sorted (sort > matchsticks))
               (sides (make-vector 4 0)))
          (define (dfs idx)
            (if (= idx n)
                #true
                (let ((stick (list-ref sorted idx)))
                  (let loop ((i 0))
                    (cond
                      [(>= i 4) #false]
                      [else
                       (let ((cur (vector-ref sides i)))
                         (if (> (+ cur stick) target)
                             (loop (add1 i))
                             (begin
                               (vector-set! sides i (+ cur stick))
                               (if (dfs (add1 idx))
                                   #true
                                   (begin
                                     (vector-set! sides i cur)
                                     (if (or (= cur 0) (= (+ cur stick) target))
                                         #false
                                         (loop (add1 i)))))))))])))
          (dfs 0)))))
```

## Erlang

```erlang
-module(solution).
-export([makesquare/1]).

-spec makesquare(Matchsticks :: [integer()]) -> boolean().
makesquare(Matchsticks) ->
    Sum = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Matchsticks),
    case Sum rem 4 of
        0 ->
            Target = Sum div 4,
            Sorted = lists:reverse(lists:sort(Matchsticks)),
            case lists:any(fun(X) -> X > Target end, Sorted) of
                true -> false;
                false ->
                    InitialSides = {0,0,0,0},
                    dfs(0, InitialSides, Sorted, Target)
            end;
        _ -> false
    end.

dfs(Index, Sides, Sorted, Target) ->
    Len = length(Sorted),
    if Index == Len ->
            true;
       true ->
            Stick = lists:nth(Index + 1, Sorted),
            try_place(Stick, 1, Sides, Index, Sorted, Target)
    end.

try_place(_Stick, Pos, _Sides, _Index, _Sorted, _Target) when Pos > 4 ->
    false;
try_place(Stick, Pos, Sides, Index, Sorted, Target) ->
    Curr = element(Pos, Sides),
    if Curr + Stick =< Target ->
            NewSides = setelement(Pos, Sides, Curr + Stick),
            case dfs(Index + 1, NewSides, Sorted, Target) of
                true -> true;
                false -> try_place(Stick, Pos + 1, Sides, Index, Sorted, Target)
            end;
       true ->
            try_place(Stick, Pos + 1, Sides, Index, Sorted, Target)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec makesquare(matchsticks :: [integer]) :: boolean
  def makesquare(matchsticks) do
    total = Enum.sum(matchsticks)

    if rem(total, 4) != 0 do
      false
    else
      target = div(total, 4)
      sticks = Enum.sort(matchsticks, &>=/2)
      dfs(0, sticks, [0, 0, 0, 0], target)
    end
  end

  defp dfs(i, sticks, sides, target) do
    if i == length(sticks) do
      true
    else
      stick = Enum.at(sticks, i)
      try_side(0, stick, sides, target, i, sticks)
    end
  end

  defp try_side(idx, _stick, _sides, _target, _i, _sticks) when idx > 3, do: false

  defp try_side(idx, stick, sides, target, i, sticks) do
    cur = Enum.at(sides, idx)

    if cur + stick <= target and not side_used?(sides, idx, cur) do
      new_sides = List.replace_at(sides, idx, cur + stick)

      if dfs(i + 1, sticks, new_sides, target) do
        true
      else
        try_side(idx + 1, stick, sides, target, i, sticks)
      end
    else
      try_side(idx + 1, stick, sides, target, i, sticks)
    end
  end

  defp side_used?(sides, idx, cur) do
    Enum.any?(Enum.take(sides, idx), fn x -> x == cur end)
  end
end
```
