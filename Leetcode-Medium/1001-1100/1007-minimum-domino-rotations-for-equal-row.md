# 1007. Minimum Domino Rotations For Equal Row

## Cpp

```cpp
class Solution {
public:
    int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
        const int INF = 1e9;
        auto rotationsNeeded = [&](int target) -> int {
            int rotTop = 0, rotBot = 0;
            for (size_t i = 0; i < tops.size(); ++i) {
                if (tops[i] == target && bottoms[i] == target) continue;
                else if (tops[i] == target) rotBot++;
                else if (bottoms[i] == target) rotTop++;
                else return INF;
            }
            return min(rotTop, rotBot);
        };
        int ans = min(rotationsNeeded(tops[0]), rotationsNeeded(bottoms[0]));
        return ans == INF ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    public int minDominoRotations(int[] tops, int[] bottoms) {
        int candidate1 = tops[0];
        int candidate2 = bottoms[0];
        int ans = Integer.MAX_VALUE;
        
        int rotations = check(candidate1, tops, bottoms);
        if (rotations != -1) {
            ans = Math.min(ans, rotations);
        }
        rotations = check(candidate2, tops, bottoms);
        if (rotations != -1) {
            ans = Math.min(ans, rotations);
        }
        
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
    
    private int check(int target, int[] tops, int[] bottoms) {
        int rotTop = 0;     // rotations to make all tops equal target
        int rotBottom = 0;  // rotations to make all bottoms equal target
        
        for (int i = 0; i < tops.length; i++) {
            if (tops[i] != target && bottoms[i] != target) {
                return -1;
            }
            if (tops[i] != target) {
                rotTop++;
            } else if (bottoms[i] != target) {
                rotBottom++;
            }
        }
        return Math.min(rotTop, rotBottom);
    }
}
```

## Python

```python
class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        def rotations(target):
            rot_top = rot_bottom = 0
            for t, b in zip(tops, bottoms):
                if t != target and b != target:
                    return -1
                if t != target:
                    rot_top += 1
                elif b != target:
                    rot_bottom += 1
            return min(rot_top, rot_bottom)

        ans = rotations(tops[0])
        if ans != -1:
            return ans
        ans = rotations(bottoms[0])
        return ans if ans != -1 else -1
```

## Python3

```python
from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        candidates = {tops[0], bottoms[0]}
        answer = float('inf')
        
        for target in candidates:
            rot_top = rot_bottom = 0
            possible = True
            for i in range(n):
                top, bottom = tops[i], bottoms[i]
                if top != target and bottom != target:
                    possible = False
                    break
                elif top != target:   # need to rotate to bring target on top
                    rot_top += 1
                elif bottom != target:  # need to rotate to bring target on bottom
                    rot_bottom += 1
            if possible:
                answer = min(answer, rot_top, rot_bottom)
        
        return -1 if answer == float('inf') else answer
```

## C

```c
#include <limits.h>

static int rotationsForTarget(int *tops, int n, int *bottoms, int target) {
    int cntTop = 0, cntBottom = 0;
    for (int i = 0; i < n; ++i) {
        if (tops[i] == target && bottoms[i] == target) continue;
        else if (tops[i] == target) cntBottom++;
        else if (bottoms[i] == target) cntTop++;
        else return -1;
    }
    return cntTop < cntBottom ? cntTop : cntBottom;
}

int minDominoRotations(int* tops, int topsSize, int* bottoms, int bottomsSize) {
    int cand1 = tops[0];
    int cand2 = bottoms[0];
    int ans = INT_MAX;

    int res1 = rotationsForTarget(tops, topsSize, bottoms, cand1);
    if (res1 != -1 && res1 < ans) ans = res1;

    if (cand2 != cand1) {
        int res2 = rotationsForTarget(tops, topsSize, bottoms, cand2);
        if (res2 != -1 && res2 < ans) ans = res2;
    }

    return ans == INT_MAX ? -1 : ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinDominoRotations(int[] tops, int[] bottoms) {
        int n = tops.Length;
        int result = Check(tops[0], tops, bottoms);
        if (result != -1 && tops[0] == bottoms[0]) {
            return result;
        }
        int other = Check(bottoms[0], tops, bottoms);
        if (result == -1) return other;
        if (other == -1) return result;
        return Math.Min(result, other);
    }

    private int Check(int target, int[] tops, int[] bottoms) {
        int rotationsTop = 0;     // rotations needed to make all tops equal target
        int rotationsBottom = 0;  // rotations needed to make all bottoms equal target

        for (int i = 0; i < tops.Length; i++) {
            if (tops[i] != target && bottoms[i] != target) {
                return -1; // impossible for this target
            }
            if (tops[i] != target) rotationsTop++;     // need to rotate this domino to bring target on top
            if (bottoms[i] != target) rotationsBottom++; // need to rotate this domino to bring target on bottom
        }

        return Math.Min(rotationsTop, rotationsBottom);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} tops
 * @param {number[]} bottoms
 * @return {number}
 */
var minDominoRotations = function(tops, bottoms) {
    const n = tops.length;
    
    const check = (target) => {
        let rotTop = 0;   // rotations to make all tops == target
        let rotBottom = 0; // rotations to make all bottoms == target
        
        for (let i = 0; i < n; i++) {
            const t = tops[i], b = bottoms[i];
            if (t !== target && b !== target) {
                return Infinity; // impossible for this target
            }
            if (t !== target) rotTop++;      // need to rotate this domino to bring target on top
            if (b !== target) rotBottom++;   // need to rotate this domino to bring target on bottom
        }
        return Math.min(rotTop, rotBottom);
    };
    
    const ans = Math.min(check(tops[0]), check(bottoms[0]));
    return ans === Infinity ? -1 : ans;
};
```

## Typescript

```typescript
function minDominoRotations(tops: number[], bottoms: number[]): number {
    const n = tops.length;
    const candidates = [tops[0], bottoms[0]];
    let best = Number.MAX_SAFE_INTEGER;

    for (const target of candidates) {
        let rotTop = 0;
        let rotBottom = 0;
        let possible = true;

        for (let i = 0; i < n; i++) {
            const top = tops[i];
            const bottom = bottoms[i];

            if (top !== target && bottom !== target) {
                possible = false;
                break;
            }
            if (top !== target) rotTop++;
            else if (bottom !== target) rotBottom++;
        }

        if (possible) {
            best = Math.min(best, Math.min(rotTop, rotBottom));
        }
    }

    return best === Number.MAX_SAFE_INTEGER ? -1 : best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $tops
     * @param Integer[] $bottoms
     * @return Integer
     */
    function minDominoRotations($tops, $bottoms) {
        $n = count($tops);
        $candidates = [$tops[0]];
        if ($bottoms[0] !== $tops[0]) {
            $candidates[] = $bottoms[0];
        }
        $best = PHP_INT_MAX;

        foreach ($candidates as $target) {
            $rotTop = 0;
            $rotBottom = 0;
            $possible = true;
            for ($i = 0; $i < $n; $i++) {
                if ($tops[$i] !== $target && $bottoms[$i] !== $target) {
                    $possible = false;
                    break;
                }
                if ($tops[$i] !== $target) {
                    $rotTop++;
                }
                if ($bottoms[$i] !== $target) {
                    $rotBottom++;
                }
            }
            if ($possible) {
                $best = min($best, $rotTop, $rotBottom);
            }
        }

        return $best === PHP_INT_MAX ? -1 : $best;
    }
}
```

## Swift

```swift
class Solution {
    func minDominoRotations(_ tops: [Int], _ bottoms: [Int]) -> Int {
        let n = tops.count
        guard n > 0 else { return -1 }
        
        func rotationsNeeded(for target: Int) -> Int? {
            var rotTop = 0
            var rotBottom = 0
            for i in 0..<n {
                let t = tops[i]
                let b = bottoms[i]
                if t != target && b != target {
                    return nil
                } else if t != target { // need rotate to bring target on top
                    rotTop += 1
                } else if b != target { // need rotate to bring target on bottom
                    rotBottom += 1
                }
            }
            return min(rotTop, rotBottom)
        }
        
        var answer = Int.max
        if let r = rotationsNeeded(for: tops[0]) {
            answer = min(answer, r)
        }
        if let r = rotationsNeeded(for: bottoms[0]) {
            answer = min(answer, r)
        }
        return answer == Int.max ? -1 : answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDominoRotations(tops: IntArray, bottoms: IntArray): Int {
        val n = tops.size
        fun rotations(target: Int): Int {
            var topRot = 0
            var bottomRot = 0
            for (i in 0 until n) {
                if (tops[i] != target && bottoms[i] != target) return Int.MAX_VALUE
                else if (tops[i] != target) topRot++
                else if (bottoms[i] != target) bottomRot++
            }
            return kotlin.math.min(topRot, bottomRot)
        }
        val ans = kotlin.math.min(rotations(tops[0]), rotations(bottoms[0]))
        return if (ans == Int.MAX_VALUE) -1 else ans
    }
}
```

## Dart

```dart
class Solution {
  int minDominoRotations(List<int> tops, List<int> bottoms) {
    const int INF = 1000000000;
    int check(int target) {
      int rotTop = 0;
      int rotBottom = 0;
      for (int i = 0; i < tops.length; ++i) {
        if (tops[i] != target && bottoms[i] != target) {
          return INF;
        }
        if (tops[i] != target) {
          rotTop++;
        } else if (bottoms[i] != target) {
          rotBottom++;
        }
      }
      return rotTop < rotBottom ? rotTop : rotBottom;
    }

    int ans = check(tops[0]);
    int ans2 = check(bottoms[0]);
    ans = ans < ans2 ? ans : ans2;
    return ans == INF ? -1 : ans;
  }
}
```

## Golang

```go
func minDominoRotations(tops []int, bottoms []int) int {
	n := len(tops)
	if n == 0 {
		return -1
	}
	check := func(candidate int) int {
		rotTop, rotBottom := 0, 0
		for i := 0; i < n; i++ {
			top, bot := tops[i], bottoms[i]
			if top != candidate && bot != candidate {
				return -1
			}
			if top != candidate {
				rotTop++
			}
			if bot != candidate {
				rotBottom++
			}
		}
		if rotTop < rotBottom {
			return rotTop
		}
		return rotBottom
	}

	ans := check(tops[0])
	cand2 := bottoms[0]
	if cand2 != tops[0] {
		if ans2 := check(cand2); ans == -1 || (ans2 != -1 && ans2 < ans) {
			ans = ans2
		}
	}
	return ans
}
```

## Ruby

```ruby
def min_domino_rotations(tops, bottoms)
  n = tops.size
  candidates = [tops[0], bottoms[0]]
  inf = Float::INFINITY
  best = inf

  candidates.each do |target|
    rot_top = 0
    rot_bottom = 0
    possible = true

    (0...n).each do |i|
      if tops[i] != target && bottoms[i] != target
        possible = false
        break
      elsif tops[i] != target
        rot_top += 1
      elsif bottoms[i] != target
        rot_bottom += 1
      end
    end

    if possible
      best = [best, rot_top, rot_bottom].min
    end
  end

  best == inf ? -1 : best
end
```

## Scala

```scala
object Solution {
    def minDominoRotations(tops: Array[Int], bottoms: Array[Int]): Int = {
        val n = tops.length
        def rotations(target: Int): Int = {
            var topRot = 0
            var bottomRot = 0
            for (i <- 0 until n) {
                if (tops(i) != target && bottoms(i) != target) return Int.MaxValue
                else if (tops(i) != target) topRot += 1
                else if (bottoms(i) != target) bottomRot += 1
            }
            Math.min(topRot, bottomRot)
        }
        val ans = Math.min(rotations(tops(0)), rotations(bottoms(0)))
        if (ans == Int.MaxValue) -1 else ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_domino_rotations(tops: Vec<i32>, bottoms: Vec<i32>) -> i32 {
        let n = tops.len();
        if n == 0 {
            return -1;
        }
        let candidates = [tops[0], bottoms[0]];
        let mut answer = std::i32::MAX;

        for &cand in &candidates {
            let mut rot_top = 0;
            let mut rot_bottom = 0;
            let mut possible = true;

            for i in 0..n {
                if tops[i] != cand && bottoms[i] != cand {
                    possible = false;
                    break;
                }
                if tops[i] != cand {
                    rot_top += 1;
                }
                if bottoms[i] != cand {
                    rot_bottom += 1;
                }
            }

            if possible {
                let cur = std::cmp::min(rot_top, rot_bottom) as i32;
                if cur < answer {
                    answer = cur;
                }
            }
        }

        if answer == std::i32::MAX { -1 } else { answer }
    }
}
```

## Racket

```racket
(define/contract (min-domino-rotations tops bottoms)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (define (check-candidate cand n tops bottoms)
    (let loop ((i 0) (rot-top 0) (rot-bottom 0))
      (if (= i n)
          (min rot-top rot-bottom)
          (let* ((t (list-ref tops i))
                 (b (list-ref bottoms i)))
            (cond
              [(= t cand)
               (if (= b cand)
                   (loop (+ i 1) rot-top rot-bottom)
                   (loop (+ i 1) rot-top (+ rot-bottom 1)))]
              [(= b cand) (loop (+ i 1) (+ rot-top 1) rot-bottom)]
              [else #f])))))
  (let* ((n (length tops))
         (candidates (list (first tops) (first bottoms)))
         (possible
          (filter values?
                  (map (lambda (cand) (check-candidate cand n tops bottoms))
                       candidates))))
    (if (null? possible)
        -1
        (apply min possible))))
```

## Erlang

```erlang
-module(solution).
-export([min_domino_rotations/2]).

-spec min_domino_rotations(Tops :: [integer()], Bottoms :: [integer()]) -> integer().
min_domino_rotations(Tops, Bottoms) ->
    Pairs = lists:zip(Tops, Bottoms),
    Cand1 = hd(Tops),
    Cand2 = hd(Bottoms),

    Res1 = case check(Cand1, Pairs) of
               {true, RotTop, RotBottom} -> min(RotTop, RotBottom);
               _ -> undefined
           end,
    Res2 = case check(Cand2, Pairs) of
               {true, RotTop, RotBottom} -> min(RotTop, RotBottom);
               _ -> undefined
           end,

    CandidatesRes = [R || R <- [Res1, Res2], R =/= undefined],
    case CandidatesRes of
        [] -> -1;
        _ -> lists:min(CandidatesRes)
    end.

check(Cand, Pairs) ->
    check(Cand, Pairs, 0, 0).

check(_Cand, [], RotTop, RotBottom) ->
    {true, RotTop, RotBottom};
check(Cand, [{T,B}|Rest], RotTop, RotBottom) ->
    case {T == Cand, B == Cand} of
        {true,true} ->
            check(Cand, Rest, RotTop, RotBottom);
        {true,false} ->
            check(Cand, Rest, RotTop, RotBottom + 1);
        {false,true} ->
            check(Cand, Rest, RotTop + 1, RotBottom);
        {false,false} ->
            {false, 0, 0}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_domino_rotations(tops :: [integer], bottoms :: [integer]) :: integer
  def min_domino_rotations(tops, bottoms) do
    candidates = [hd(tops), hd(bottoms)] |> Enum.uniq()

    rotations =
      candidates
      |> Enum.map(&rotations_for_candidate(&1, tops, bottoms))
      |> Enum.filter(fn x -> x != :impossible end)

    case rotations do
      [] -> -1
      list -> Enum.min(list)
    end
  end

  defp rotations_for_candidate(candidate, tops, bottoms) do
    case Enum.reduce_while(Enum.zip(tops, bottoms), {0, 0}, fn {t, b}, {rot_top, rot_bottom} ->
           cond do
             t == candidate and b == candidate ->
               {:cont, {rot_top, rot_bottom}}

             t == candidate ->
               # need to rotate this domino to make bottom = candidate
               {:cont, {rot_top, rot_bottom + 1}}

             b == candidate ->
               # need to rotate this domino to make top = candidate
               {:cont, {rot_top + 1, rot_bottom}}

             true ->
               {:halt, :impossible}
           end
         end) do
      :impossible -> :impossible
      {rot_top, rot_bottom} -> min(rot_top, rot_bottom)
    end
  end
end
```
