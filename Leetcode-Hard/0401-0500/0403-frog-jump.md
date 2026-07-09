# 0403. Frog Jump

## Cpp

```cpp
class Solution {
public:
    bool canCross(vector<int>& stones) {
        int n = stones.size();
        unordered_map<int,int> posIndex;
        for (int i = 0; i < n; ++i) posIndex[stones[i]] = i;
        
        vector<unordered_set<int>> dp(n);
        dp[0].insert(0); // starting point, previous jump length 0
        
        for (int i = 0; i < n; ++i) {
            for (int k : dp[i]) {
                for (int delta = -1; delta <= 1; ++delta) {
                    int nextJump = k + delta;
                    if (nextJump <= 0) continue;
                    int nextPos = stones[i] + nextJump;
                    auto it = posIndex.find(nextPos);
                    if (it != posIndex.end()) {
                        dp[it->second].insert(nextJump);
                    }
                }
            }
        }
        return !dp[n-1].empty();
    }
};
```

## Java

```java
class Solution {
    public boolean canCross(int[] stones) {
        int n = stones.length;
        if (n == 0) return false;
        if (n > 1 && stones[1] != 1) return false;

        java.util.Map<Integer, Integer> indexMap = new java.util.HashMap<>();
        for (int i = 0; i < n; i++) {
            indexMap.put(stones[i], i);
        }

        java.util.List<java.util.Set<Integer>> dp = new java.util.ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            dp.add(new java.util.HashSet<>());
        }
        dp.get(0).add(0);

        for (int i = 0; i < n; i++) {
            for (int k : dp.get(i)) {
                for (int step = k - 1; step <= k + 1; step++) {
                    if (step <= 0) continue;
                    int nextPos = stones[i] + step;
                    Integer idx = indexMap.get(nextPos);
                    if (idx != null) {
                        if (idx == n - 1) return true;
                        dp.get(idx).add(step);
                    }
                }
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        stone_set = set(stones)
        last = stones[-1]
        dp = {stones[0]: {0}}  # position -> possible jump sizes to reach it

        for pos in stones:
            if pos not in dp:
                continue
            for k in dp[pos]:
                for nxt in (k - 1, k, k + 1):
                    if nxt <= 0:
                        continue
                    next_pos = pos + nxt
                    if next_pos == last:
                        return True
                    if next_pos in stone_set:
                        if next_pos not in dp:
                            dp[next_pos] = set()
                        dp[next_pos].add(nxt)
        return False
```

## Python3

```python
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) < 2 or stones[1] != 1:
            return False
        stone_set = set(stones)
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        for pos in stones:
            for k in dp[pos]:
                for step in (k - 1, k, k + 1):
                    if step > 0 and (next_pos := pos + step) in stone_set:
                        dp[next_pos].add(step)
                        if next_pos == stones[-1]:
                            return True
        return bool(dp[stones[-1]])
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

static int findIndex(int *stones, int size, int target) {
    int l = 0, r = size - 1;
    while (l <= r) {
        int m = l + ((r - l) >> 1);
        if (stones[m] == target) return m;
        if (stones[m] < target) l = m + 1;
        else r = m - 1;
    }
    return -1;
}

bool canCross(int* stones, int stonesSize) {
    if (stonesSize == 0) return false;
    int lastIdx = stonesSize - 1;
    int stride = stonesSize + 1; // possible jump lengths from 0..stonesSize
    unsigned char *dp = calloc((size_t)stonesSize * stride, sizeof(unsigned char));
    if (!dp) return false; // allocation failure, treat as impossible

    dp[0 * stride + 0] = 1; // start at first stone with previous jump 0

    for (int i = 0; i < stonesSize; ++i) {
        for (int k = 0; k <= stonesSize; ++k) {
            if (!dp[i * stride + k]) continue;
            for (int d = -1; d <= 1; ++d) {
                int jump = k + d;
                if (jump <= 0) continue;
                int nextPos = stones[i] + jump;
                int j = findIndex(stones, stonesSize, nextPos);
                if (j != -1) {
                    dp[j * stride + jump] = 1;
                }
            }
        }
    }

    bool can = false;
    for (int k = 0; k <= stonesSize; ++k) {
        if (dp[lastIdx * stride + k]) {
            can = true;
            break;
        }
    }

    free(dp);
    return can;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CanCross(int[] stones)
    {
        int n = stones.Length;
        // Quick check: the first jump must be to position 1
        if (n > 1 && stones[1] != 1) return false;

        var stoneSet = new HashSet<int>(stones);
        var reachMap = new Dictionary<int, HashSet<int>>();
        foreach (int s in stones)
            reachMap[s] = new HashSet<int>();

        // start from position 0 with a "previous jump" of 0
        reachMap[0].Add(0);

        for (int i = 0; i < n; i++)
        {
            int pos = stones[i];
            var jumps = reachMap[pos];

            foreach (int k in jumps)
            {
                for (int step = k - 1; step <= k + 1; step++)
                {
                    if (step <= 0) continue;
                    int nextPos = pos + step;

                    if (nextPos == stones[n - 1])
                        return true;

                    if (reachMap.ContainsKey(nextPos))
                        reachMap[nextPos].Add(step);
                }
            }
        }

        // If we never reached the last stone
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} stones
 * @return {boolean}
 */
var canCross = function(stones) {
    const n = stones.length;
    if (n === 0) return false;
    // The first jump must be 1 unit.
    if (stones[1] !== 1) return false;

    const stoneSet = new Set(stones);
    const dp = new Map(); // position -> Set of possible last jumps reaching it
    for (const s of stones) {
        dp.set(s, new Set());
    }
    dp.get(0).add(0); // start with a "virtual" jump size 0 at position 0

    const target = stones[n - 1];

    for (let i = 0; i < n; i++) {
        const pos = stones[i];
        const jumps = dp.get(pos);
        for (const k of jumps) {
            for (let step = k - 1; step <= k + 1; step++) {
                if (step <= 0) continue;
                const nextPos = pos + step;
                if (nextPos === target) return true;
                if (stoneSet.has(nextPos)) {
                    dp.get(nextPos).add(step);
                }
            }
        }
    }

    // Check if the last stone was reachable via any jump size
    return dp.get(target).size > 0;
};
```

## Typescript

```typescript
function canCross(stones: number[]): boolean {
    const n = stones.length;
    if (n === 0) return false;

    const stoneSet = new Set<number>(stones);
    const dp = new Map<number, Set<number>>();
    for (const s of stones) dp.set(s, new Set<number>());

    // start from position 0 with a previous jump of 0
    dp.get(0)!.add(0);

    for (let i = 0; i < n; i++) {
        const pos = stones[i];
        const jumps = dp.get(pos)!;
        for (const k of jumps) {
            for (let step = k - 1; step <= k + 1; step++) {
                if (step <= 0) continue;
                const nextPos = pos + step;
                if (!stoneSet.has(nextPos)) continue;
                if (nextPos === stones[n - 1]) return true;
                dp.get(nextPos)!.add(step);
            }
        }
    }

    return dp.get(stones[n - 1])!.size > 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @return Boolean
     */
    function canCross($stones) {
        $n = count($stones);
        if ($n == 0) return false;
        // Map stone position to its index for quick lookup
        $stoneIndex = array_flip($stones);
        // DP: position => set of jump sizes that can land here
        $dp = [];
        foreach ($stones as $pos) {
            $dp[$pos] = [];
        }
        // Start from first stone with a "previous jump" of 0
        $dp[0][0] = true;

        foreach ($stones as $pos) {
            foreach ($dp[$pos] as $k => $_) {
                for ($step = $k - 1; $step <= $k + 1; $step++) {
                    if ($step <= 0) continue;
                    $nextPos = $pos + $step;
                    if (isset($stoneIndex[$nextPos])) {
                        $dp[$nextPos][$step] = true;
                    }
                }
            }
        }

        // If there is any jump size that reaches the last stone, return true
        return !empty($dp[$stones[$n - 1]]);
    }
}
```

## Swift

```swift
class Solution {
    func canCross(_ stones: [Int]) -> Bool {
        guard stones.count > 1 else { return true }
        let lastStone = stones.last!
        var stoneSet = Set<Int>(stones)
        var dp = [Int: Set<Int>]()
        dp[0] = [0]
        
        for stone in stones {
            guard let jumps = dp[stone] else { continue }
            for k in jumps {
                for step in (k-1)...(k+1) {
                    if step <= 0 { continue }
                    let nextPos = stone + step
                    if nextPos == lastStone {
                        return true
                    }
                    if stoneSet.contains(nextPos) {
                        var set = dp[nextPos] ?? Set<Int>()
                        set.insert(step)
                        dp[nextPos] = set
                    }
                }
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canCross(stones: IntArray): Boolean {
        val n = stones.size
        if (n < 2) return false
        if (stones[1] != 1) return false

        val indexMap = HashMap<Int, Int>(n * 2)
        for (i in stones.indices) {
            indexMap[stones[i]] = i
        }

        val dp = Array(n) { mutableSetOf<Int>() }
        dp[0].add(0)

        for (i in 0 until n) {
            for (k in dp[i]) {
                val nextSteps = intArrayOf(k - 1, k, k + 1)
                for (step in nextSteps) {
                    if (step <= 0) continue
                    val nextPos = stones[i] + step
                    val idx = indexMap[nextPos]
                    if (idx != null) {
                        dp[idx].add(step)
                    }
                }
            }
        }

        return dp[n - 1].isNotEmpty()
    }
}
```

## Dart

```dart
class Solution {
  bool canCross(List<int> stones) {
    int n = stones.length;
    if (n < 2 || stones[1] != 1) return false;

    // Map each stone position to a set of jump sizes that can land on it.
    final Map<int, Set<int>> dp = {};
    for (final pos in stones) {
      dp[pos] = <int>{};
    }
    dp[0]!.add(0); // start with a "virtual" jump size 0 at the first stone.

    for (final stone in stones) {
      final jumps = dp[stone]!;
      if (jumps.isEmpty) continue;

      for (final k in jumps) {
        for (int step = k - 1; step <= k + 1; ++step) {
          if (step <= 0) continue;
          final nextPos = stone + step;
          if (dp.containsKey(nextPos)) {
            dp[nextPos]!.add(step);
          }
        }
      }
    }

    return dp[stones.last]!.isNotEmpty;
  }
}
```

## Golang

```go
func canCross(stones []int) bool {
	n := len(stones)
	if n == 0 {
		return false
	}
	posIdx := make(map[int]int, n)
	for i, p := range stones {
		posIdx[p] = i
	}
	dp := make([]map[int]struct{}, n)
	for i := range dp {
		dp[i] = make(map[int]struct{})
	}
	dp[0][0] = struct{}{}
	for i := 0; i < n; i++ {
		for k := range dp[i] {
			if k-1 > 0 {
				if idx, ok := posIdx[stones[i]+k-1]; ok {
					dp[idx][k-1] = struct{}{}
				}
			}
			if k > 0 {
				if idx, ok := posIdx[stones[i]+k]; ok {
					dp[idx][k] = struct{}{}
				}
			}
			if idx, ok := posIdx[stones[i]+k+1]; ok && k+1 > 0 {
				dp[idx][k+1] = struct{}{}
			}
		}
	}
	return len(dp[n-1]) > 0
}
```

## Ruby

```ruby
require 'set'

# @param {Integer[]} stones
# @return {Boolean}
def can_cross(stones)
  stone_map = {}
  stones.each { |pos| stone_map[pos] = Set.new }
  stone_map[0].add(0)

  stones.each do |stone|
    stone_map[stone].each do |k|
      (k - 1).upto(k + 1) do |step|
        next if step <= 0
        nxt = stone + step
        if stone_map.key?(nxt)
          stone_map[nxt].add(step)
        end
      end
    end
  end

  !stone_map[stones[-1]].empty?
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable.{HashMap, HashSet}

    def canCross(stones: Array[Int]): Boolean = {
        val n = stones.length
        if (n == 0) return false
        // Quick check for the first jump requirement
        if (stones(1) != 1) return false

        val stoneSet = stones.toSet
        val dp = new HashMap[Int, HashSet[Int]]()
        for (s <- stones) {
            dp(s) = new HashSet[Int]()
        }
        dp(0).add(0)

        for (i <- 0 until n) {
            val pos = stones(i)
            val jumps = dp(pos)
            if (jumps.nonEmpty) {
                for (k <- jumps) {
                    for (step <- List(k - 1, k, k + 1)) {
                        if (step > 0) {
                            val nextPos = pos + step
                            if (nextPos == stones(n - 1)) return true
                            if (stoneSet.contains(nextPos)) {
                                dp(nextPos).add(step)
                            }
                        }
                    }
                }
            }
        }

        dp(stones(n - 1)).nonEmpty
    }
}
```

## Rust

```rust
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn can_cross(stones: Vec<i32>) -> bool {
        let n = stones.len();
        if n < 2 || stones[1] != 1 {
            return false;
        }

        let mut pos_to_idx: HashMap<i32, usize> = HashMap::new();
        for (i, &p) in stones.iter().enumerate() {
            pos_to_idx.insert(p, i);
        }

        let mut dp: Vec<HashSet<i32>> = vec![HashSet::new(); n];
        dp[0].insert(0);

        for i in 0..n {
            let cur_pos = stones[i];
            let jumps: Vec<i32> = dp[i].iter().cloned().collect();
            for k in jumps {
                for step in [k - 1, k, k + 1].iter() {
                    if *step <= 0 {
                        continue;
                    }
                    let next_pos = cur_pos + *step;
                    if let Some(&next_idx) = pos_to_idx.get(&next_pos) {
                        dp[next_idx].insert(*step);
                    }
                }
            }
        }

        !dp[n - 1].is_empty()
    }
}
```

## Racket

```racket
(define/contract (can-cross stones)
  (-> (listof exact-integer?) boolean?)
  (let* ((stone-map (make-hash))
         (n (length stones)))
    ;; initialize a hash for each stone position
    (for ([s stones])
      (hash-set! stone-map s (make-hash)))
    ;; start from the first stone with a virtual jump of size 0
    (when (hash-has-key? stone-map 0)
      (let ((h (hash-ref stone-map 0)))
        (hash-set! h 0 #t)))
    ;; propagate reachable jumps
    (for ([pos stones])
      (define jumps (hash-ref stone-map pos))
      (for ([k (hash-keys jumps)])
        (for ([d (list (- k 1) k (+ k 1))])
          (when (> d 0)
            (define next-pos (+ pos d))
            (when (hash-has-key? stone-map next-pos)
              (define nxt (hash-ref stone-map next-pos))
              (hash-set! nxt d #t))))))
    ;; check if the last stone has any reachable jump size
    (let ((last-pos (list-ref stones (- n 1))))
      (> (hash-count (hash-ref stone-map last-pos)) 0))))
```

## Erlang

```erlang
-spec can_cross(Stones :: [integer()]) -> boolean().
can_cross(Stones) ->
    case Stones of
        [0, 1 | _] -> ok;
        _ -> false
    end,
    EmptyMap = maps:from_list([{Pos, sets:new()} || Pos <- Stones]),
    Map0 = maps:put(0, sets:add_element(1, sets:new()), EmptyMap),
    FinalMap = process(Stones, Map0),
    LastPos = lists:last(Stones),
    case maps:get(LastPos, FinalMap) of
        Set when sets:is_empty(Set) -> false;
        _ -> true
    end.

process([], Map) ->
    Map;
process([Pos | Rest], Map) ->
    JumpSet = maps:get(Pos, Map),
    NewMap = propagate(JumpSet, Pos, Map),
    process(Rest, NewMap).

propagate(JumpSet, Pos, Map) ->
    lists:foldl(
      fun(Jump, AccMap) ->
          Deltas = [Jump - 1, Jump, Jump + 1],
          lists:foldl(
            fun(Delta, M) ->
                case Delta > 0 of
                    true ->
                        NextPos = Pos + Delta,
                        case maps:is_key(NextPos, M) of
                            true ->
                                UpdatedSet = sets:add_element(Delta,
                                            maps:get(NextPos, M)),
                                maps:put(NextPos, UpdatedSet, M);
                            false -> M
                        end;
                    false -> M
                end
            end,
            AccMap,
            Deltas)
      end,
      Map,
      sets:to_list(JumpSet)).
```

## Elixir

```elixir
defmodule Solution do
  @spec can_cross(stones :: [integer]) :: boolean
  def can_cross(stones) do
    case stones do
      [_first, second | _] when second != 1 ->
        false

      _ ->
        pos_index = Enum.into(Enum.with_index(stones), %{}, fn {pos, idx} -> {pos, idx} end)
        last = List.last(stones)

        result =
          Enum.reduce_while(stones, %{0 => MapSet.new([0])}, fn pos, dp ->
            jumps = Map.get(dp, pos, MapSet.new())

            if MapSet.size(jumps) == 0 do
              {:cont, dp}
            else
              new_dp =
                Enum.reduce(jumps, dp, fn k, acc_dp ->
                  Enum.reduce([k - 1, k, k + 1], acc_dp, fn step, inner_acc ->
                    if step > 0 do
                      next_pos = pos + step

                      if Map.has_key?(pos_index, next_pos) do
                        set = Map.get(inner_acc, next_pos, MapSet.new())
                        updated_set = MapSet.put(set, step)
                        Map.put(inner_acc, next_pos, updated_set)
                      else
                        inner_acc
                      end
                    else
                      inner_acc
                    end
                  end)
                end)

              if Map.has_key?(new_dp, last) do
                {:halt, true}
              else
                {:cont, new_dp}
              end
            end
          end)

        case result do
          true -> true
          _ -> false
        end
    end
  end
end
```
