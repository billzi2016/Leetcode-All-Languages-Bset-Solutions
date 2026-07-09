# 2212. Maximum Points in an Archery Competition

## Cpp

```cpp
class Solution {
public:
    vector<int> maximumBobPoints(int numArrows, vector<int>& aliceArrows) {
        const int n = 12;
        int bestScore = -1;
        int bestMask = 0;
        int bestRemain = 0;
        for (int mask = 0; mask < (1 << n); ++mask) {
            int need = 0, score = 0;
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) {
                    need += aliceArrows[i] + 1;
                    score += i;
                }
            }
            if (need > numArrows) continue;
            if (score > bestScore) {
                bestScore = score;
                bestMask = mask;
                bestRemain = numArrows - need;
            }
        }
        vector<int> bobArrows(n, 0);
        for (int i = 0; i < n; ++i) {
            if (bestMask & (1 << i)) {
                bobArrows[i] = aliceArrows[i] + 1;
            }
        }
        // put remaining arrows into section 0 (any section works)
        bobArrows[0] += bestRemain;
        return bobArrows;
    }
};
```

## Java

```java
class Solution {
    public int[] maximumBobPoints(int numArrows, int[] aliceArrows) {
        int n = 12;
        int bestMask = 0;
        int maxScore = -1;
        for (int mask = 0; mask < (1 << n); mask++) {
            int need = 0;
            int score = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    need += aliceArrows[i] + 1;
                    score += i;
                }
            }
            if (need > numArrows) continue;
            if (score > maxScore) {
                maxScore = score;
                bestMask = mask;
            }
        }
        int[] bob = new int[n];
        int used = 0;
        for (int i = 0; i < n; i++) {
            if ((bestMask & (1 << i)) != 0) {
                bob[i] = aliceArrows[i] + 1;
                used += bob[i];
            }
        }
        bob[0] += numArrows - used;
        return bob;
    }
}
```

## Python

```python
class Solution(object):
    def maximumBobPoints(self, numArrows, aliceArrows):
        """
        :type numArrows: int
        :type aliceArrows: List[int]
        :rtype: List[int]
        """
        n = 12
        bestScore = -1
        bestBob = None

        for mask in range(1 << n):
            bob = [0] * n
            used = 0
            # allocate arrows to win selected sections
            for i in range(n):
                if (mask >> i) & 1:
                    need = aliceArrows[i] + 1
                    used += need
                    if used > numArrows:
                        break
                    bob[i] = need
            else:  # only executed if inner loop didn't break
                if used > numArrows:
                    continue
                leftover = numArrows - used
                bob[0] += leftover  # put remaining arrows in section 0 (score 0)

                # compute Bob's total points
                score = 0
                for i in range(n):
                    if bob[i] > aliceArrows[i]:
                        score += i

                if score > bestScore:
                    bestScore = score
                    bestBob = bob[:]

        return bestBob
```

## Python3

```python
from typing import List

class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        n = 12
        best_score = -1
        best_mask = 0

        # Precompute needed arrows and points for each index
        need = [a + 1 for a in aliceArrows]
        pts = list(range(n))

        for mask in range(1 << n):
            total_need = 0
            total_pts = 0
            # early prune could be added but not necessary for 4096 masks
            for i in range(n):
                if mask >> i & 1:
                    total_need += need[i]
                    total_pts += pts[i]
            if total_need > numArrows:
                continue
            if total_pts > best_score:
                best_score = total_pts
                best_mask = mask

        # Build result based on best_mask
        bob = [0] * n
        used = 0
        for i in range(n):
            if best_mask >> i & 1:
                bob[i] = need[i]
                used += need[i]

        # Put remaining arrows into index 0 (any section works)
        bob[0] += numArrows - used
        return bob
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maximumBobPoints(int numArrows, int* aliceArrows, int aliceArrowsSize, int* returnSize) {
    int n = aliceArrowsSize;               // should be 12
    int bestMask = 0;
    int bestScore = -1;

    for (int mask = 0; mask < (1 << n); ++mask) {
        int need = 0;
        int score = 0;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                need += aliceArrows[i] + 1;
                score += i;
            }
        }
        if (need <= numArrows && score > bestScore) {
            bestScore = score;
            bestMask = mask;
        }
    }

    int* res = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) res[i] = 0;

    int used = 0;
    for (int i = 0; i < n; ++i) {
        if (bestMask & (1 << i)) {
            res[i] = aliceArrows[i] + 1;
            used += res[i];
        }
    }

    int remain = numArrows - used;
    if (remain > 0) {
        // put remaining arrows into section 0 (does not affect total points)
        res[0] += remain;
    }

    *returnSize = n;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] MaximumBobPoints(int numArrows, int[] aliceArrows) {
        const int n = 12;
        int bestMask = 0;
        int bestScore = -1;

        for (int mask = 0; mask < (1 << n); mask++) {
            int need = 0;
            int score = 0;
            for (int i = 0; i < n; i++) {
                if ((mask >> i & 1) == 1) {
                    need += aliceArrows[i] + 1;
                    score += i;
                }
            }
            if (need > numArrows) continue;
            if (score > bestScore) {
                bestScore = score;
                bestMask = mask;
            }
        }

        int[] bob = new int[n];
        int remaining = numArrows;
        for (int i = 0; i < n; i++) {
            if ((bestMask >> i & 1) == 1) {
                bob[i] = aliceArrows[i] + 1;
                remaining -= bob[i];
            }
        }
        // Put any leftover arrows into section 0
        bob[0] += remaining;

        return bob;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} numArrows
 * @param {number[]} aliceArrows
 * @return {number[]}
 */
var maximumBobPoints = function(numArrows, aliceArrows) {
    const n = 12;
    let bestScore = -1;
    let bestArr = new Array(n).fill(0);
    
    const totalMasks = 1 << n; // 4096
    for (let mask = 0; mask < totalMasks; ++mask) {
        let need = 0;
        let score = 0;
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                need += aliceArrows[i] + 1;
                score += i;
            }
        }
        if (need > numArrows) continue;
        
        const cur = new Array(n).fill(0);
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                cur[i] = aliceArrows[i] + 1;
            }
        }
        // put remaining arrows into section 0 (any section works)
        cur[0] += numArrows - need;
        
        if (score > bestScore) {
            bestScore = score;
            bestArr = cur;
        }
    }
    
    return bestArr;
};
```

## Typescript

```typescript
function maximumBobPoints(numArrows: number, aliceArrows: number[]): number[] {
    const n = 12;
    let bestScore = -1;
    let bestDist = new Array(n).fill(0);
    const totalMasks = 1 << n;

    for (let mask = 0; mask < totalMasks; ++mask) {
        let required = 0;
        let score = 0;
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                required += aliceArrows[i] + 1;
                score += i;
                if (required > numArrows) break;
            }
        }
        if (required > numArrows) continue;

        const dist = new Array(n).fill(0);
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                dist[i] = aliceArrows[i] + 1;
            }
        }
        dist[0] += numArrows - required;

        if (score > bestScore) {
            bestScore = score;
            bestDist = dist;
        }
    }

    return bestDist;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $numArrows
     * @param Integer[] $aliceArrows
     * @return Integer[]
     */
    function maximumBobPoints($numArrows, $aliceArrows) {
        $n = 12;
        $maxScore = -1;
        $bestMask = 0;

        $totalMasks = 1 << $n;
        for ($mask = 0; $mask < $totalMasks; ++$mask) {
            $need = 0;
            $score = 0;
            for ($i = 0; $i < $n; ++$i) {
                if (($mask >> $i) & 1) {
                    $need += $aliceArrows[$i] + 1;
                    $score += $i;
                    if ($need > $numArrows) break; // early stop
                }
            }
            if ($need <= $numArrows && $score > $maxScore) {
                $maxScore = $score;
                $bestMask = $mask;
            }
        }

        $bob = array_fill(0, $n, 0);
        $used = 0;
        for ($i = 0; $i < $n; ++$i) {
            if (($bestMask >> $i) & 1) {
                $bob[$i] = $aliceArrows[$i] + 1;
                $used += $bob[$i];
            }
        }

        // put remaining arrows into section 0
        $bob[0] += $numArrows - $used;

        return $bob;
    }
}
```

## Swift

```swift
class Solution {
    func maximumBobPoints(_ numArrows: Int, _ aliceArrows: [Int]) -> [Int] {
        let n = 12
        var bestScore = -1
        var bestMask = 0
        
        for mask in 0..<(1 << n) {
            var need = 0
            var score = 0
            for i in 0..<n {
                if (mask >> i) & 1 == 1 {
                    need += aliceArrows[i] + 1
                    score += i
                }
            }
            if need <= numArrows && score > bestScore {
                bestScore = score
                bestMask = mask
            }
        }
        
        var bob = Array(repeating: 0, count: n)
        var used = 0
        for i in 0..<n {
            if (bestMask >> i) & 1 == 1 {
                let cnt = aliceArrows[i] + 1
                bob[i] = cnt
                used += cnt
            }
        }
        bob[0] += numArrows - used
        return bob
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumBobPoints(numArrows: Int, aliceArrows: IntArray): IntArray {
        var bestMask = 0
        var bestScore = -1
        for (mask in 0 until (1 shl 12)) {
            var need = 0
            var score = 0
            for (i in 0..11) {
                if ((mask and (1 shl i)) != 0) {
                    need += aliceArrows[i] + 1
                    score += i
                }
            }
            if (need <= numArrows && score > bestScore) {
                bestScore = score
                bestMask = mask
            }
        }
        val bob = IntArray(12)
        var used = 0
        for (i in 0..11) {
            if ((bestMask and (1 shl i)) != 0) {
                bob[i] = aliceArrows[i] + 1
                used += bob[i]
            }
        }
        val remain = numArrows - used
        bob[0] += remain
        return bob
    }
}
```

## Dart

```dart
class Solution {
  List<int> maximumBobPoints(int numArrows, List<int> aliceArrows) {
    int bestMask = 0;
    int bestScore = -1;

    for (int mask = 0; mask < (1 << 12); ++mask) {
      int need = 0;
      int score = 0;
      for (int i = 0; i < 12; ++i) {
        if ((mask & (1 << i)) != 0) {
          need += aliceArrows[i] + 1;
          score += i;
        }
      }
      if (need > numArrows) continue;
      if (score > bestScore) {
        bestScore = score;
        bestMask = mask;
      }
    }

    List<int> bob = List.filled(12, 0);
    int used = 0;
    for (int i = 0; i < 12; ++i) {
      if ((bestMask & (1 << i)) != 0) {
        bob[i] = aliceArrows[i] + 1;
        used += bob[i];
      }
    }

    int leftover = numArrows - used;
    bob[0] += leftover;

    return bob;
  }
}
```

## Golang

```go
func maximumBobPoints(numArrows int, aliceArrows []int) []int {
	const n = 12
	bestScore := -1
	bestMask := 0
	bestReq := 0

	for mask := 0; mask < (1 << n); mask++ {
		req := 0
		score := 0
		for i := 0; i < n; i++ {
			if mask>>i&1 == 1 {
				req += aliceArrows[i] + 1
				score += i
			}
		}
		if req > numArrows {
			continue
		}
		if score > bestScore {
			bestScore = score
			bestMask = mask
			bestReq = req
		}
	}

	bob := make([]int, n)
	for i := 0; i < n; i++ {
		if bestMask>>i&1 == 1 {
			bob[i] = aliceArrows[i] + 1
		}
	}
	leftover := numArrows - bestReq
	bob[0] += leftover

	return bob
}
```

## Ruby

```ruby
def maximum_bob_points(num_arrows, alice_arrows)
  best_score = -1
  best_dist = nil
  (0...(1 << 12)).each do |mask|
    total_needed = 0
    dist = Array.new(12, 0)
    score = 0
    12.times do |i|
      if (mask & (1 << i)) != 0
        need = alice_arrows[i] + 1
        total_needed += need
        dist[i] = need
        score += i
      end
    end
    next if total_needed > num_arrows
    dist[0] += num_arrows - total_needed
    if score > best_score
      best_score = score
      best_dist = dist
    end
  end
  best_dist
end
```

## Scala

```scala
object Solution {
    def maximumBobPoints(numArrows: Int, aliceArrows: Array[Int]): Array[Int] = {
        val n = 12
        var bestScore = -1
        var bestArr: Array[Int] = new Array[Int](n)

        val totalMasks = 1 << n
        for (mask <- 0 until totalMasks) {
            var required = 0
            var score = 0
            // first pass to compute required arrows and score
            var i = 0
            while (i < n) {
                if ((mask >> i) & 1 == 1) {
                    required += aliceArrows(i) + 1
                    score += i
                }
                i += 1
            }
            if (required > numArrows) {
                // not enough arrows for this subset
                continue
            }

            val arr = new Array[Int](n)
            i = 0
            while (i < n) {
                if ((mask >> i) & 1 == 1) {
                    arr(i) = aliceArrows(i) + 1
                }
                i += 1
            }
            val remaining = numArrows - required
            // put all leftover arrows into slot 0 (any slot works)
            arr(0) += remaining

            if (score > bestScore) {
                bestScore = score
                bestArr = arr.clone()
            }
        }

        bestArr
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_bob_points(num_arrows: i32, alice_arrows: Vec<i32>) -> Vec<i32> {
        let n = 12;
        let mut best_mask: u32 = 0;
        let mut max_points: i32 = -1;
        for mask in 0..(1 << n) {
            let mut req = 0i32;
            let mut points = 0i32;
            for i in 0..n {
                if (mask >> i) & 1 == 1 {
                    req += alice_arrows[i] + 1;
                    points += i as i32;
                }
            }
            if req <= num_arrows && points > max_points {
                max_points = points;
                best_mask = mask as u32;
            }
        }

        let mut res = vec![0i32; n];
        let mut used = 0i32;
        for i in 0..n {
            if (best_mask >> i) & 1 == 1 {
                let val = alice_arrows[i] + 1;
                res[i] = val;
                used += val;
            }
        }
        // allocate remaining arrows to section 0
        res[0] += num_arrows - used;
        res
    }
}
```

## Racket

```racket
#lang racket

(define/contract (maximum-bob-points numArrows aliceArrows)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?))
  (let* ((v (list->vector aliceArrows))
         (total-masks (expt 2 12)))
    ;; helper to compute required arrows and points for a mask
    (define (mask-info mask)
      (let ((req 0) (pts 0))
        (for ([i (in-range 12)])
          (when (not (= 0 (bitwise-and mask (arithmetic-shift 1 i))))
            (set! req (+ req (+ (vector-ref v i) 1)))
            (set! pts (+ pts i))))
        (values req pts)))
    ;; find best mask
    (define best-mask 0)
    (define best-points -1)
    (for ([mask (in-range total-masks)])
      (let-values ([(req pts) (mask-info mask)])
        (when (and (<= req numArrows) (> pts best-points))
          (set! best-points pts)
          (set! best-mask mask))))
    ;; construct bob's arrows
    (define bob (make-vector 12 0))
    (for ([i (in-range 12)])
      (when (not (= 0 (bitwise-and best-mask (arithmetic-shift 1 i))))
        (vector-set! bob i (+ (vector-ref v i) 1))))
    ;; allocate remaining arrows to index 0
    (define used
      (let ((sum 0))
        (for ([i (in-range 12)])
          (set! sum (+ sum (vector-ref bob i))))
        sum))
    (define remaining (- numArrows used))
    (vector-set! bob 0 (+ (vector-ref bob 0) remaining))
    (vector->list bob)))
```

## Erlang

```erlang
-module(solution).
-export([maximum_bob_points/2]).

maximum_bob_points(NumArrows, AliceArrows) ->
    AliceTuple = list_to_tuple(AliceArrows),
    MaxMask = (1 bsl 12) - 1,
    {_, BestBob} = loop_masks(0, MaxMask, NumArrows, AliceTuple, -1, []),
    BestBob.

loop_masks(CurrentMask, MaxMask, _NumArrows, _AliceTuple, BestScore, BestBob)
        when CurrentMask > MaxMask ->
    {BestScore, BestBob};
loop_masks(CurrentMask, MaxMask, NumArrows, AliceTuple, BestScore, BestBob) ->
    BobBase = [case (CurrentMask band (1 bsl I)) of
                  0 -> 0;
                  _ -> element(I+1, AliceTuple) + 1
              end || I <- lists:seq(0,11)],
    Required = lists:sum(BobBase),
    if Required =< NumArrows ->
            Remaining = NumArrows - Required,
            [First|Rest] = BobBase,
            BobList = [First + Remaining | Rest],
            Score = compute_score(CurrentMask),
            case Score > BestScore of
                true -> loop_masks(CurrentMask+1, MaxMask, NumArrows,
                                   AliceTuple, Score, BobList);
                false -> loop_masks(CurrentMask+1, MaxMask, NumArrows,
                                    AliceTuple, BestScore, BestBob)
            end;
       true ->
            loop_masks(CurrentMask+1, MaxMask, NumArrows,
                       AliceTuple, BestScore, BestBob)
    end.

compute_score(Mask) -> compute_score(Mask, 0, 0).

compute_score(0, _Idx, Acc) -> Acc;
compute_score(Mask, Idx, Acc) ->
    Bit = Mask band 1,
    NewAcc = if Bit =:= 1 -> Acc + Idx; true -> Acc end,
    compute_score(Mask bsr 1, Idx+1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec maximum_bob_points(num_arrows :: integer, alice_arrows :: [integer]) :: [integer]
  def maximum_bob_points(num_arrows, alice_arrows) do
    n = 12
    alice = List.to_tuple(alice_arrows)
    max_mask = 1 <<< n

    {best_mask, _} =
      Enum.reduce(0..(max_mask - 1), {0, -1}, fn mask, {cur_best_mask, cur_best_score} ->
        {required, score} =
          Enum.reduce(0..(n - 1), {0, 0}, fn i, {req, sc} ->
            if (mask &&& (1 <<< i)) != 0 do
              {req + elem(alice, i) + 1, sc + i}
            else
              {req, sc}
            end
          end)

        if required <= num_arrows and score > cur_best_score do
          {mask, score}
        else
          {cur_best_mask, cur_best_score}
        end
      end)

    bob =
      for i <- 0..(n - 1) do
        if (best_mask &&& (1 <<< i)) != 0 do
          elem(alice, i) + 1
        else
          0
        end
      end

    leftover = num_arrows - Enum.sum(bob)
    List.update_at(bob, 0, fn v -> v + leftover end)
  end
end
```
