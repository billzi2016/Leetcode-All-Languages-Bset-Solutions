# 2225. Find Players With Zero or One Losses

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        unordered_map<int, int> lossCount;
        unordered_set<int> players;
        for (const auto& m : matches) {
            int winner = m[0];
            int loser = m[1];
            players.insert(winner);
            players.insert(loser);
            ++lossCount[loser];
            // ensure winner has an entry with 0 losses if not already present
            if (!lossCount.count(winner)) lossCount[winner] = 0;
        }
        vector<int> zero, one;
        for (int p : players) {
            int cnt = lossCount[p];
            if (cnt == 0) zero.push_back(p);
            else if (cnt == 1) one.push_back(p);
        }
        sort(zero.begin(), zero.end());
        sort(one.begin(), one.end());
        return {zero, one};
    }
};
```

## Java

```java
class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        Map<Integer, Integer> lossCount = new HashMap<>();
        Set<Integer> players = new HashSet<>();

        for (int[] match : matches) {
            int winner = match[0];
            int loser = match[1];
            players.add(winner);
            players.add(loser);
            lossCount.put(loser, lossCount.getOrDefault(loser, 0) + 1);
        }

        List<Integer> zeroLoss = new ArrayList<>();
        List<Integer> oneLoss = new ArrayList<>();

        for (int player : players) {
            int cnt = lossCount.getOrDefault(player, 0);
            if (cnt == 0) {
                zeroLoss.add(player);
            } else if (cnt == 1) {
                oneLoss.add(player);
            }
        }

        Collections.sort(zeroLoss);
        Collections.sort(oneLoss);

        List<List<Integer>> answer = new ArrayList<>();
        answer.add(zeroLoss);
        answer.add(oneLoss);
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        loss_counts = defaultdict(int)
        players = set()
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            loss_counts[loser] += 1
        zero_losses = []
        one_loss = []
        for p in players:
            cnt = loss_counts.get(p, 0)
            if cnt == 0:
                zero_losses.append(p)
            elif cnt == 1:
                one_loss.append(p)
        zero_losses.sort()
        one_loss.sort()
        return [zero_losses, one_loss]
```

## Python3

```python
class Solution:
    def findWinners(self, matches):
        from collections import defaultdict
        loss_count = defaultdict(int)
        players = set()
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            loss_count[loser] += 1

        zero_losses = []
        one_loss = []
        for p in players:
            cnt = loss_count.get(p, 0)
            if cnt == 0:
                zero_losses.append(p)
            elif cnt == 1:
                one_loss.append(p)

        return [sorted(zero_losses), sorted(one_loss)]
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findWinners(int** matches, int matchesSize, int* matchesColSize,
                  int* returnSize, int** returnColumnSizes) {
    (void)matchesColSize;  // unused

    int maxId = 0;
    for (int i = 0; i < matchesSize; ++i) {
        int w = matches[i][0];
        int l = matches[i][1];
        if (w > maxId) maxId = w;
        if (l > maxId) maxId = l;
    }

    int *lossCount = calloc(maxId + 1, sizeof(int));
    char *seen = calloc(maxId + 1, sizeof(char));

    for (int i = 0; i < matchesSize; ++i) {
        int w = matches[i][0];
        int l = matches[i][1];
        seen[w] = 1;
        seen[l] = 1;
        lossCount[l]++;
    }

    int cntZero = 0, cntOne = 0;
    for (int id = 1; id <= maxId; ++id) {
        if (!seen[id]) continue;
        if (lossCount[id] == 0) cntZero++;
        else if (lossCount[id] == 1) cntOne++;
    }

    int *zero = malloc(cntZero * sizeof(int));
    int *one = malloc(cntOne * sizeof(int));

    int zi = 0, oi = 0;
    for (int id = 1; id <= maxId; ++id) {
        if (!seen[id]) continue;
        if (lossCount[id] == 0) zero[zi++] = id;
        else if (lossCount[id] == 1) one[oi++] = id;
    }

    free(lossCount);
    free(seen);

    int **ans = malloc(2 * sizeof(int*));
    ans[0] = zero;
    ans[1] = one;

    *returnSize = 2;
    *returnColumnSizes = malloc(2 * sizeof(int));
    (*returnColumnSizes)[0] = cntZero;
    (*returnColumnSizes)[1] = cntOne;

    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> FindWinners(int[][] matches) {
        var lossCount = new Dictionary<int, int>();
        var players = new HashSet<int>();

        foreach (var match in matches) {
            int winner = match[0];
            int loser = match[1];

            players.Add(winner);
            players.Add(loser);

            if (lossCount.ContainsKey(loser))
                lossCount[loser]++;
            else
                lossCount[loser] = 1;
        }

        var zeroLoss = new List<int>();
        var oneLoss = new List<int>();

        foreach (var player in players) {
            int cnt = lossCount.TryGetValue(player, out int c) ? c : 0;
            if (cnt == 0)
                zeroLoss.Add(player);
            else if (cnt == 1)
                oneLoss.Add(player);
        }

        zeroLoss.Sort();
        oneLoss.Sort();

        var result = new List<IList<int>>();
        result.Add(zeroLoss);
        result.Add(oneLoss);
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} matches
 * @return {number[][]}
 */
var findWinners = function(matches) {
    const lossCount = new Map();
    const players = new Set();

    for (const [winner, loser] of matches) {
        players.add(winner);
        players.add(loser);
        lossCount.set(loser, (lossCount.get(loser) || 0) + 1);
    }

    const zeroLoss = [];
    const oneLoss = [];

    for (const p of players) {
        const cnt = lossCount.get(p) || 0;
        if (cnt === 0) zeroLoss.push(p);
        else if (cnt === 1) oneLoss.push(p);
    }

    zeroLoss.sort((a, b) => a - b);
    oneLoss.sort((a, b) => a - b);

    return [zeroLoss, oneLoss];
};
```

## Typescript

```typescript
function findWinners(matches: number[][]): number[][] {
    const lossCount = new Map<number, number>();
    for (const [winner, loser] of matches) {
        if (!lossCount.has(winner)) {
            lossCount.set(winner, 0);
        }
        lossCount.set(loser, (lossCount.get(loser) ?? 0) + 1);
    }

    const zeroLoss: number[] = [];
    const oneLoss: number[] = [];

    for (const [player, cnt] of lossCount.entries()) {
        if (cnt === 0) {
            zeroLoss.push(player);
        } else if (cnt === 1) {
            oneLoss.push(player);
        }
    }

    zeroLoss.sort((a, b) => a - b);
    oneLoss.sort((a, b) => a - b);

    return [zeroLoss, oneLoss];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $matches
     * @return Integer[][]
     */
    function findWinners($matches) {
        $losses = [];

        foreach ($matches as $match) {
            list($winner, $loser) = $match;

            if (!isset($losses[$winner])) {
                $losses[$winner] = 0;
            }
            if (!isset($losses[$loser])) {
                $losses[$loser] = 0;
            }

            $losses[$loser] += 1;
        }

        ksort($losses);

        $zeroLoss = [];
        $oneLoss = [];

        foreach ($losses as $player => $cnt) {
            if ($cnt === 0) {
                $zeroLoss[] = $player;
            } elseif ($cnt === 1) {
                $oneLoss[] = $player;
            }
        }

        return [$zeroLoss, $oneLoss];
    }
}
```

## Swift

```swift
class Solution {
    func findWinners(_ matches: [[Int]]) -> [[Int]] {
        var lossCount = [Int:Int]()
        var players = Set<Int>()
        
        for match in matches {
            let winner = match[0]
            let loser = match[1]
            players.insert(winner)
            players.insert(loser)
            lossCount[loser, default: 0] += 1
        }
        
        var zeroLoss = [Int]()
        var oneLoss = [Int]()
        
        for p in players {
            let cnt = lossCount[p] ?? 0
            if cnt == 0 {
                zeroLoss.append(p)
            } else if cnt == 1 {
                oneLoss.append(p)
            }
        }
        
        zeroLoss.sort()
        oneLoss.sort()
        return [zeroLoss, oneLoss]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findWinners(matches: Array<IntArray>): List<List<Int>> {
        val lossCount = HashMap<Int, Int>()
        val players = HashSet<Int>()
        for (match in matches) {
            val winner = match[0]
            val loser = match[1]
            players.add(winner)
            players.add(loser)
            lossCount[loser] = lossCount.getOrDefault(loser, 0) + 1
        }
        val zeroLoss = mutableListOf<Int>()
        val oneLoss = mutableListOf<Int>()
        for (p in players) {
            when (lossCount.getOrDefault(p, 0)) {
                0 -> zeroLoss.add(p)
                1 -> oneLoss.add(p)
            }
        }
        zeroLoss.sort()
        oneLoss.sort()
        return listOf(zeroLoss, oneLoss)
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> findWinners(List<List<int>> matches) {
    final Set<int> players = {};
    final Map<int, int> lossCount = {};

    for (var match in matches) {
      int winner = match[0];
      int loser = match[1];
      players.add(winner);
      players.add(loser);
      lossCount[loser] = (lossCount[loser] ?? 0) + 1;
    }

    List<int> zeroLoss = [];
    List<int> oneLoss = [];

    for (int player in players) {
      int cnt = lossCount[player] ?? 0;
      if (cnt == 0) {
        zeroLoss.add(player);
      } else if (cnt == 1) {
        oneLoss.add(player);
      }
    }

    zeroLoss.sort();
    oneLoss.sort();

    return [zeroLoss, oneLoss];
  }
}
```

## Golang

```go
import "sort"

func findWinners(matches [][]int) [][]int {
    loss := make(map[int]int)
    players := make(map[int]struct{})
    for _, m := range matches {
        w, l := m[0], m[1]
        players[w] = struct{}{}
        players[l] = struct{}{}
        loss[l]++
    }
    zero := []int{}
    one := []int{}
    for p := range players {
        cnt := loss[p]
        if cnt == 0 {
            zero = append(zero, p)
        } else if cnt == 1 {
            one = append(one, p)
        }
    }
    sort.Ints(zero)
    sort.Ints(one)
    return [][]int{zero, one}
}
```

## Ruby

```ruby
def find_winners(matches)
  loss_counts = Hash.new(0)
  players = {}

  matches.each do |winner, loser|
    players[winner] = true
    players[loser] = true
    loss_counts[loser] += 1
  end

  zero = []
  one = []

  players.keys.sort.each do |p|
    case loss_counts[p]
    when 0
      zero << p
    when 1
      one << p
    end
  end

  [zero, one]
end
```

## Scala

```scala
object Solution {
    def findWinners(matches: Array[Array[Int]]): List[List[Int]] = {
        import scala.collection.mutable.{Map, Set, ArrayBuffer}
        val lossCount: Map[Int, Int] = Map().withDefaultValue(0)
        val players: Set[Int] = Set()
        for (m <- matches) {
            val winner = m(0)
            val loser = m(1)
            players += winner
            players += loser
            lossCount(loser) = lossCount(loser) + 1
        }
        val zeroLoss = ArrayBuffer[Int]()
        val oneLoss = ArrayBuffer[Int]()
        for (p <- players) {
            lossCount.get(p) match {
                case None => zeroLoss += p
                case Some(cnt) =>
                    if (cnt == 0) zeroLoss += p
                    else if (cnt == 1) oneLoss += p
            }
        }
        List(zeroLoss.sorted.toList, oneLoss.sorted.toList)
    }
}
```

## Rust

```rust
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn find_winners(matches: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut participants: HashSet<i32> = HashSet::new();
        let mut losses: HashMap<i32, i32> = HashMap::new();

        for m in matches.iter() {
            let winner = m[0];
            let loser = m[1];
            participants.insert(winner);
            participants.insert(loser);
            *losses.entry(loser).or_insert(0) += 1;
        }

        let mut zero_loss: Vec<i32> = Vec::new();
        let mut one_loss: Vec<i32> = Vec::new();

        for &player in participants.iter() {
            match losses.get(&player) {
                Some(&cnt) if cnt == 1 => one_loss.push(player),
                None => zero_loss.push(player),
                _ => {}
            }
        }

        zero_loss.sort_unstable();
        one_loss.sort_unstable();

        vec![zero_loss, one_loss]
    }
}
```

## Racket

```racket
(define/contract (find-winners matches)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?)))
  (let ((losses (make-hash))
        (players (make-hash)))
    (for-each
     (lambda (pair)
       (define winner (first pair))
       (define loser (second pair))
       (hash-set! players winner #t)
       (hash-set! players loser #t)
       (hash-set! losses loser (+ 1 (hash-ref losses loser 0))))
     matches)
    (define zero '())
    (define one '())
    (for-each
     (lambda (kv)
       (define player (car kv))
       (define loss-count (hash-ref losses player 0))
       (cond [(= loss-count 0) (set! zero (cons player zero))]
             [(= loss-count 1) (set! one (cons player one))]))
     (hash->list players))
    (list (sort zero <) (sort one <))))
```

## Erlang

```erlang
-spec find_winners(Matches :: [[integer()]]) -> [[integer()]].
find_winners(Matches) ->
    {LossMap, PlayersSet} = lists:foldl(
        fun([W, L], {LM, PS}) ->
            LM1 = maps:put(L, maps:get(L, LM, 0) + 1, LM),
            PS1 = maps:put(W, true, PS),
            PS2 = maps:put(L, true, PS1),
            {LM1, PS2}
        end,
        {#{}, #{}},
        Matches
    ),
    Players = maps:keys(PlayersSet),
    Zero = [P || P <- Players, maps:get(P, LossMap, 0) =:= 0],
    One  = [P || P <- Players, maps:get(P, LossMap, 0) =:= 1],
    [lists:sort(Zero), lists:sort(One)].
```

## Elixir

```elixir
defmodule Solution do
  @spec find_winners(matches :: [[integer]]) :: [[integer]]
  def find_winners(matches) do
    {loss_map, players} =
      Enum.reduce(matches, {%{}, MapSet.new()}, fn [winner, loser], {lm, set} ->
        lm = Map.update(lm, loser, 1, &(&1 + 1))
        set = set |> MapSet.put(winner) |> MapSet.put(loser)
        {lm, set}
      end)

    zero_losses =
      players
      |> Enum.filter(fn p -> Map.get(loss_map, p, 0) == 0 end)
      |> Enum.sort()

    one_loss =
      players
      |> Enum.filter(fn p -> Map.get(loss_map, p, 0) == 1 end)
      |> Enum.sort()

    [zero_losses, one_loss]
  end
end
```
