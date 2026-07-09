# 0956. Tallest Billboard

## Cpp

```cpp
class Solution {
public:
    int tallestBillboard(vector<int>& rods) {
        int total = accumulate(rods.begin(), rods.end(), 0);
        const int INF_NEG = -1;
        vector<int> dp(total + 1, INF_NEG);
        dp[0] = 0; // diff 0, taller height 0
        
        for (int r : rods) {
            vector<int> ndp(dp);
            for (int d = 0; d <= total; ++d) {
                if (dp[d] < 0) continue;
                int taller = dp[d];
                
                // Add rod to the taller side
                int diff1 = d + r;
                int taller1 = taller + r;
                if (ndp[diff1] < taller1) ndp[diff1] = taller1;
                
                // Add rod to the shorter side
                int diff2 = abs(d - r);
                int shorterPlusR = taller - d + r; // shorter = taller - d
                int taller2 = max(taller, shorterPlusR);
                if (ndp[diff2] < taller2) ndp[diff2] = taller2;
            }
            dp.swap(ndp);
        }
        return dp[0];
    }
};
```

## Java

```java
class Solution {
    public int tallestBillboard(int[] rods) {
        java.util.Map<Integer, Integer> dp = new java.util.HashMap<>();
        dp.put(0, 0);
        for (int r : rods) {
            java.util.Map<Integer, Integer> next = new java.util.HashMap<>(dp);
            for (java.util.Map.Entry<Integer, Integer> entry : dp.entrySet()) {
                int diff = entry.getKey();
                int taller = entry.getValue();

                // Add rod to the taller side
                int ndiff1 = diff + r;
                int ntaller1 = taller + r;
                next.merge(ndiff1, ntaller1, Math::max);

                // Add rod to the shorter side
                int shorter = taller - diff;
                int newShorter = shorter + r;
                int ndiff2 = Math.abs(taller - newShorter);
                int ntaller2 = Math.max(taller, newShorter);
                next.merge(ndiff2, ntaller2, Math::max);
            }
            dp = next;
        }
        return dp.getOrDefault(0, 0);
    }
}
```

## Python

```python
class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        dp = {0: 0}  # diff -> taller height
        for r in rods:
            new_dp = dp.copy()
            for diff, taller in dp.items():
                # add to the taller side
                ndiff = diff + r
                ntaller = taller + r
                if new_dp.get(ndiff, 0) < ntaller:
                    new_dp[ndiff] = ntaller

                # add to the shorter side
                shorter = taller - diff
                ndiff2 = abs(shorter + r - taller)
                ntaller2 = max(taller, shorter + r)
                if new_dp.get(ndiff2, 0) < ntaller2:
                    new_dp[ndiff2] = ntaller2
            dp = new_dp
        return dp.get(0, 0)
```

## Python3

```python
from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}  # diff -> taller height
        for r in rods:
            cur_items = list(dp.items())
            new_dp = dp.copy()
            for diff, taller in cur_items:
                shorter = taller - diff

                # add to taller side
                ndiff = diff + r
                ntaller = taller + r
                if ntaller > new_dp.get(ndiff, 0):
                    new_dp[ndiff] = ntaller

                # add to shorter side
                new_shorter = shorter + r
                if new_shorter >= taller:
                    ndiff2 = new_shorter - taller
                    ntaller2 = new_shorter
                else:
                    ndiff2 = taller - new_shorter
                    ntaller2 = taller
                if ntaller2 > new_dp.get(ndiff2, 0):
                    new_dp[ndiff2] = ntaller2

            dp = new_dp
        return dp.get(0, 0)
```

## C

```c
#include <stdlib.h>
#include <string.h>

int tallestBillboard(int* rods, int rodsSize) {
    int total = 0;
    for (int i = 0; i < rodsSize; ++i) total += rods[i];
    
    int *dp = (int*)malloc((total + 1) * sizeof(int));
    int *ndp = (int*)malloc((total + 1) * sizeof(int));
    const int NEG = -1000000;
    for (int i = 0; i <= total; ++i) dp[i] = NEG;
    dp[0] = 0;
    
    for (int idx = 0; idx < rodsSize; ++idx) {
        int r = rods[idx];
        memcpy(ndp, dp, (total + 1) * sizeof(int));
        for (int diff = 0; diff <= total; ++diff) {
            if (dp[diff] < 0) continue;
            int taller = dp[diff];
            int shorter = taller - diff;
            
            // add to taller side
            int ndiff = diff + r;
            if (ndiff <= total && ndp[ndiff] < taller + r)
                ndp[ndiff] = taller + r;
            
            // add to shorter side
            int newShorter = shorter + r;
            int newTaller, newDiff;
            if (newShorter > taller) {
                newTaller = newShorter;
                newDiff = newShorter - taller;
            } else {
                newTaller = taller;
                newDiff = taller - newShorter;
            }
            if (ndp[newDiff] < newTaller)
                ndp[newDiff] = newTaller;
        }
        int *tmp = dp; dp = ndp; ndp = tmp;
    }
    
    int result = dp[0];
    free(dp);
    free(ndp);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int TallestBillboard(int[] rods) {
        var dp = new Dictionary<int, int>();
        dp[0] = 0;
        foreach (int r in rods) {
            var next = new Dictionary<int, int>(dp);
            foreach (var kvp in dp) {
                int diff = kvp.Key;
                int taller = kvp.Value;

                // Add rod to the taller side
                int ndiff1 = diff + r;
                int ntaller1 = taller + r;
                if (!next.ContainsKey(ndiff1) || next[ndiff1] < ntaller1)
                    next[ndiff1] = ntaller1;

                // Add rod to the shorter side
                int shorter = taller - diff; // because taller - shorter = diff
                int newShorter = shorter + r;
                int ndiff2 = Math.Abs(newShorter - taller);
                int ntaller2 = Math.Max(taller, newShorter);
                if (!next.ContainsKey(ndiff2) || next[ndiff2] < ntaller2)
                    next[ndiff2] = ntaller2;
            }
            dp = next;
        }
        return dp.TryGetValue(0, out int result) ? result : 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} rods
 * @return {number}
 */
var tallestBillboard = function(rods) {
    const dp = new Map();
    dp.set(0, 0); // diff -> taller height

    for (const r of rods) {
        const snapshot = Array.from(dp.entries());
        for (const [diff, taller] of snapshot) {
            // add rod to the taller side
            let ndiff = diff + r;
            let ntaller = taller + r;
            if (!dp.has(ndiff) || dp.get(ndiff) < ntaller) {
                dp.set(ndiff, ntaller);
            }

            // add rod to the shorter side
            const short = taller - diff; // current shorter height
            const newShort = short + r;
            const newTaller = Math.max(taller, newShort);
            ndiff = Math.abs(diff - r); // |taller - (short+r)|
            ntaller = newTaller;
            if (!dp.has(ndiff) || dp.get(ndiff) < ntaller) {
                dp.set(ndiff, ntaller);
            }
        }
    }

    return dp.get(0) ?? 0;
};
```

## Typescript

```typescript
function tallestBillboard(rods: number[]): number {
    const dp = new Map<number, number>();
    dp.set(0, 0); // diff -> taller height

    for (const r of rods) {
        const cur = new Map(dp); // copy current states
        for (const [diff, taller] of dp.entries()) {
            const shorter = taller - diff;

            // add rod to the taller side
            let ndiff = diff + r;
            let ntaller = taller + r;
            const prev1 = cur.get(ndiff);
            if (prev1 === undefined || ntaller > prev1) {
                cur.set(ndiff, ntaller);
            }

            // add rod to the shorter side
            const newShorter = shorter + r;
            if (newShorter >= taller) {
                ndiff = newShorter - taller;
                ntaller = newShorter;
            } else {
                ndiff = taller - newShorter;
                ntaller = taller;
            }
            const prev2 = cur.get(ndiff);
            if (prev2 === undefined || ntaller > prev2) {
                cur.set(ndiff, ntaller);
            }
        }
        dp.clear();
        for (const [k, v] of cur.entries()) dp.set(k, v);
    }

    return dp.get(0) ?? 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $rods
     * @return Integer
     */
    function tallestBillboard($rods) {
        $dp = [0 => 0]; // diff => taller height
        foreach ($rods as $r) {
            $new = $dp; // copy current states (skip case)
            foreach ($dp as $diff => $taller) {
                // Add rod to the taller side
                $ndiff = $diff + $r;
                $ntaller = $taller + $r;
                if (!isset($new[$ndiff]) || $new[$ndiff] < $ntaller) {
                    $new[$ndiff] = $ntaller;
                }

                // Add rod to the shorter side
                $shorter = $taller - $diff; // because taller - shorter = diff
                $newShorter = $shorter + $r;
                $newTaller = max($taller, $newShorter);
                $ndiff2 = abs($diff - $r); // new difference after adding to shorter side
                if (!isset($new[$ndiff2]) || $new[$ndiff2] < $newTaller) {
                    $new[$ndiff2] = $newTaller;
                }
            }
            $dp = $new;
        }
        return $dp[0];
    }
}
```

## Swift

```swift
class Solution {
    func tallestBillboard(_ rods: [Int]) -> Int {
        var dp: [Int: Int] = [0: 0]   // diff -> taller height
        for r in rods {
            var newDP = dp
            for (diff, taller) in dp {
                // Add rod to the taller side
                let ndiff1 = diff + r
                let ntaller1 = taller + r
                if let cur = newDP[ndiff1] {
                    if ntaller1 > cur { newDP[ndiff1] = ntaller1 }
                } else {
                    newDP[ndiff1] = ntaller1
                }
                
                // Add rod to the shorter side
                let shorter = taller - diff
                let newShorter = shorter + r
                let ndiff2 = abs(newShorter - taller)
                let ntaller2 = max(newShorter, taller)
                if let cur = newDP[ndiff2] {
                    if ntaller2 > cur { newDP[ndiff2] = ntaller2 }
                } else {
                    newDP[ndiff2] = ntaller2
                }
            }
            dp = newDP
        }
        return dp[0] ?? 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun tallestBillboard(rods: IntArray): Int {
        val total = rods.sum()
        var dp = IntArray(total + 1) { -1 }
        dp[0] = 0
        for (r in rods) {
            val newDp = dp.clone()
            for (diff in 0..total) {
                val taller = dp[diff]
                if (taller < 0) continue
                // add rod to the taller side
                val ndiff = diff + r
                if (ndiff <= total && newDp[ndiff] < taller + r) {
                    newDp[ndiff] = taller + r
                }
                // add rod to the shorter side
                val ndiff2 = kotlin.math.abs(diff - r)
                val newTaller = if (r > diff) taller - diff + r else taller
                if (newDp[ndiff2] < newTaller) {
                    newDp[ndiff2] = newTaller
                }
            }
            dp = newDp
        }
        return dp[0]
    }
}
```

## Dart

```dart
class Solution {
  int tallestBillboard(List<int> rods) {
    Map<int, int> dp = {0: 0};
    for (int r in rods) {
      Map<int, int> cur = Map.from(dp);
      for (var entry in dp.entries) {
        int diff = entry.key;
        int taller = entry.value;

        // Add rod to the taller side
        int ndiff1 = diff + r;
        int ntaller1 = taller + r;
        if (!cur.containsKey(ndiff1) || cur[ndiff1]! < ntaller1) {
          cur[ndiff1] = ntaller1;
        }

        // Add rod to the shorter side
        int shorter = taller - diff;
        int newShorter = shorter + r;
        int ndiff2 = (taller - newShorter).abs();
        int ntaller2 = taller > newShorter ? taller : newShorter;
        if (!cur.containsKey(ndiff2) || cur[ndiff2]! < ntaller2) {
          cur[ndiff2] = ntaller2;
        }
      }
      dp = cur;
    }
    return dp[0] ?? 0;
  }
}
```

## Golang

```go
func tallestBillboard(rods []int) int {
    dp := map[int]int{0: 0}
    for _, r := range rods {
        newDP := make(map[int]int, len(dp))
        for d, t := range dp {
            newDP[d] = t
        }
        for diff, taller := range dp {
            // add rod to the taller side
            ndiff := diff + r
            ntaller := taller + r
            if cur, ok := newDP[ndiff]; !ok || ntaller > cur {
                newDP[ndiff] = ntaller
            }

            // add rod to the shorter side
            shorter := taller - diff
            newShorter := shorter + r
            var ndiff2, ntaller2 int
            if newShorter > taller {
                ndiff2 = newShorter - taller
                ntaller2 = newShorter
            } else {
                ndiff2 = taller - newShorter
                ntaller2 = taller
            }
            if cur, ok := newDP[ndiff2]; !ok || ntaller2 > cur {
                newDP[ndiff2] = ntaller2
            }
        }
        dp = newDP
    }
    return dp[0]
}
```

## Ruby

```ruby
def tallest_billboard(rods)
  dp = {0 => 0}
  rods.each do |r|
    next_dp = dp.dup
    dp.each do |diff, taller|
      shorter = taller - diff

      # add rod to the taller side
      ndiff1 = diff + r
      ntaller1 = taller + r
      if !next_dp.key?(ndiff1) || next_dp[ndiff1] < ntaller1
        next_dp[ndiff1] = ntaller1
      end

      # add rod to the shorter side
      new_shorter = shorter + r
      ndiff2 = (taller - new_shorter).abs
      ntaller2 = [taller, new_shorter].max
      if !next_dp.key?(ndiff2) || next_dp[ndiff2] < ntaller2
        next_dp[ndiff2] = ntaller2
      end
    end
    dp = next_dp
  end
  dp[0]
end
```

## Scala

```scala
object Solution {
  def tallestBillboard(rods: Array[Int]): Int = {
    import scala.collection.mutable

    val dp = mutable.Map[Int, Int](0 -> 0)

    def upd(m: mutable.Map[Int, Int], key: Int, value: Int): Unit = {
      m.get(key) match {
        case Some(old) if value > old => m.update(key, value)
        case None                     => m.update(key, value)
        case _                        => // no update needed
      }
    }

    for (r <- rods) {
      val snapshot = dp.clone()
      for ((diff, tall) <- snapshot) {
        val short = tall - diff

        // add rod to the taller side
        upd(dp, diff + r, tall + r)

        // add rod to the shorter side
        val newShort = short + r
        if (newShort > tall) {
          upd(dp, newShort - tall, newShort)
        } else {
          upd(dp, tall - newShort, tall)
        }
      }
    }

    dp.getOrElse(0, 0)
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn tallest_billboard(rods: Vec<i32>) -> i32 {
        let mut dp: HashMap<i32, i32> = HashMap::new();
        dp.insert(0, 0);
        for &r in rods.iter() {
            let current = dp.clone();
            let mut ndp = dp.clone();
            for (&diff, &taller) in current.iter() {
                // add rod to the taller side
                let new_diff = diff + r;
                let new_taller = taller + r;
                ndp.entry(new_diff)
                    .and_modify(|v| if new_taller > *v { *v = new_taller })
                    .or_insert(new_taller);
                
                // add rod to the shorter side
                let shorter = taller - diff; // since taller - shorter = diff
                let new_shorter = shorter + r;
                let new_diff2 = (new_shorter - taller).abs();
                let new_taller2 = if new_shorter > taller { new_shorter } else { taller };
                ndp.entry(new_diff2)
                    .and_modify(|v| if new_taller2 > *v { *v = new_taller2 })
                    .or_insert(new_taller2);
            }
            dp = ndp;
        }
        *dp.get(&0).unwrap_or(&0)
    }
}
```

## Racket

```racket
(define/contract (tallest-billboard rods)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((rs rods) (dp (hash 0 0)))
    (if (null? rs)
        (hash-ref dp 0 0)
        (let* ((r (car rs))
               (new-dp (hash-copy dp)))
          (for ([kv (in-list (hash->list dp))])
            (define diff (car kv))
            (define taller (cdr kv))
            ;; add to the taller side
            (define nd (+ diff r))
            (define nt (+ taller r))
            (when (> nt (hash-ref new-dp nd -1))
              (hash-set! new-dp nd nt))
            ;; add to the shorter side
            (define short (- taller diff))
            (define cand-taller (max taller (+ short r)))
            (define cand-diff (abs (- taller (+ short r))))
            (when (> cand-taller (hash-ref new-dp cand-diff -1))
              (hash-set! new-dp cand-diff cand-taller)))
          (loop (cdr rs) new-dp)))))
```

## Erlang

```erlang
-module(solution).
-export([tallest_billboard/1]).

-spec tallest_billboard(Rods :: [integer()]) -> integer().
tallest_billboard(Rods) ->
    DP0 = #{0 => 0},
    FinalDP = lists:foldl(fun(R, DP) ->
        maps:fold(fun(Diff, Taller, Acc) ->
            Diff1 = Diff + R,
            Tall1 = Taller + R,
            Acc1 = update_map(Acc, Diff1, Tall1),
            Shorter = Taller - Diff,
            NewShorter = Shorter + R,
            Tall2 = max(Taller, NewShorter),
            Diff2 = abs(Tall2 - NewShorter),
            update_map(Acc1, Diff2, Tall2)
        end, DP, DP)
    end, DP0, Rods),
    maps:get(0, FinalDP).

update_map(Map, Key, Val) ->
    case maps:is_key(Key, Map) of
        true ->
            Existing = maps:get(Key, Map),
            MaxVal = max(Existing, Val),
            maps:put(Key, MaxVal, Map);
        false ->
            maps:put(Key, Val, Map)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec tallest_billboard(rods :: [integer]) :: integer
  def tallest_billboard(rods) do
    dp_initial = %{0 => 0}

    final_dp =
      Enum.reduce(rods, dp_initial, fn r, dp ->
        Enum.reduce(dp, dp, fn {diff, taller}, acc ->
          # Add rod to the taller side
          diff1 = diff + r
          taller1 = taller + r

          acc =
            case Map.get(acc, diff1) do
              nil -> Map.put(acc, diff1, taller1)
              existing when existing < taller1 -> Map.put(acc, diff1, taller1)
              _ -> acc
            end

          # Add rod to the shorter side
          shorter = taller - diff
          new_shorter = shorter + r

          {diff2, taller2} =
            if new_shorter > taller do
              {new_shorter - taller, new_shorter}
            else
              {taller - new_shorter, taller}
            end

          case Map.get(acc, diff2) do
            nil -> Map.put(acc, diff2, taller2)
            existing when existing < taller2 -> Map.put(acc, diff2, taller2)
            _ -> acc
          end
        end)
      end)

    Map.get(final_dp, 0, 0)
  end
end
```
