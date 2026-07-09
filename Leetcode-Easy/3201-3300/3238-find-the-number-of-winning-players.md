# 3238. Find the Number of Winning Players

## Cpp

```cpp
class Solution {
public:
    int winningPlayerCount(int n, vector<vector<int>>& pick) {
        vector<unordered_map<int,int>> cnt(n);
        for (const auto& p : pick) {
            int x = p[0];
            int y = p[1];
            ++cnt[x][y];
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int mx = 0;
            for (const auto& kv : cnt[i]) {
                mx = max(mx, kv.second);
            }
            if (mx > i) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int winningPlayerCount(int n, int[][] pick) {
        // Array of hash maps to count color frequencies for each player
        java.util.HashMap<Integer, Integer>[] counts = new java.util.HashMap[n];
        for (int i = 0; i < n; i++) {
            counts[i] = new java.util.HashMap<>();
        }
        // Populate the counts
        for (int[] p : pick) {
            int player = p[0];
            int color = p[1];
            java.util.HashMap<Integer, Integer> map = counts[player];
            map.put(color, map.getOrDefault(color, 0) + 1);
        }
        // Determine winning players
        int winners = 0;
        for (int i = 0; i < n; i++) {
            int maxFreq = 0;
            for (int freq : counts[i].values()) {
                if (freq > maxFreq) {
                    maxFreq = freq;
                }
            }
            if (maxFreq > i) {
                winners++;
            }
        }
        return winners;
    }
}
```

## Python

```python
class Solution(object):
    def winningPlayerCount(self, n, pick):
        """
        :type n: int
        :type pick: List[List[int]]
        :rtype: int
        """
        # Initialize list of dictionaries for each player to count colors
        counts = [dict() for _ in range(n)]
        for player, color in pick:
            d = counts[player]
            d[color] = d.get(color, 0) + 1

        win = 0
        for i in range(n):
            # Find the maximum count of any color for player i
            if not counts[i]:
                continue
            max_cnt = max(counts[i].values())
            if max_cnt > i:
                win += 1
        return win
```

## Python3

```python
from typing import List
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        # counts[player][color] = number of balls of that color picked by player
        counts = [dict() for _ in range(n)]
        for player, color in pick:
            d = counts[player]
            d[color] = d.get(color, 0) + 1

        win = 0
        for i in range(n):
            if not counts[i]:
                continue
            max_cnt = max(counts[i].values())
            if max_cnt > i:
                win += 1
        return win
```

## C

```c
int winningPlayerCount(int n, int** pick, int pickSize, int* pickColSize) {
    int cnt[10][11] = {0};
    for (int i = 0; i < pickSize; ++i) {
        int xi = pick[i][0];
        int yi = pick[i][1];
        cnt[xi][yi]++;
    }
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        int maxc = 0;
        for (int c = 0; c < 11; ++c) {
            if (cnt[i][c] > maxc) maxc = cnt[i][c];
        }
        if (maxc > i) ans++;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int WinningPlayerCount(int n, int[][] pick) {
        var playerColors = new Dictionary<int, int>[n];
        for (int i = 0; i < n; i++) {
            playerColors[i] = new Dictionary<int, int>();
        }

        foreach (var p in pick) {
            int player = p[0];
            int color = p[1];
            var dict = playerColors[player];
            if (dict.ContainsKey(color))
                dict[color]++;
            else
                dict[color] = 1;
        }

        int winningCount = 0;
        for (int i = 0; i < n; i++) {
            int maxSameColor = 0;
            foreach (var kv in playerColors[i]) {
                if (kv.Value > maxSameColor) maxSameColor = kv.Value;
            }
            if (maxSameColor > i) winningCount++;
        }

        return winningCount;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} pick
 * @return {number}
 */
var winningPlayerCount = function(n, pick) {
    const playerCounts = Array.from({ length: n }, () => ({}));
    for (const [x, y] of pick) {
        const map = playerCounts[x];
        map[y] = (map[y] || 0) + 1;
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const map = playerCounts[i];
        for (const cnt of Object.values(map)) {
            if (cnt > i) {
                ans++;
                break;
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function winningPlayerCount(n: number, pick: number[][]): number {
    const playerMaps: Map<number, number>[] = Array.from({ length: n }, () => new Map());
    
    for (const [x, y] of pick) {
        const m = playerMaps[x];
        m.set(y, (m.get(y) ?? 0) + 1);
    }
    
    let result = 0;
    for (let i = 0; i < n; i++) {
        let maxCnt = 0;
        for (const cnt of playerMaps[i].values()) {
            if (cnt > maxCnt) maxCnt = cnt;
        }
        if (maxCnt > i) result++;
    }
    
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $pick
     * @return Integer
     */
    function winningPlayerCount($n, $pick) {
        // Initialize an array for each player to store color counts
        $playerColors = array_fill(0, $n, []);
        
        foreach ($pick as $p) {
            $x = $p[0];
            $y = $p[1];
            if (!isset($playerColors[$x][$y])) {
                $playerColors[$x][$y] = 0;
            }
            $playerColors[$x][$y]++;
        }
        
        $wins = 0;
        for ($i = 0; $i < $n; $i++) {
            foreach ($playerColors[$i] as $cnt) {
                if ($cnt > $i) {
                    $wins++;
                    break; // player i wins, no need to check other colors
                }
            }
        }
        
        return $wins;
    }
}
```

## Swift

```swift
class Solution {
    func winningPlayerCount(_ n: Int, _ pick: [[Int]]) -> Int {
        var playerColorCounts = Array(repeating: [Int: Int](), count: n)
        for entry in pick {
            let player = entry[0]
            let color = entry[1]
            playerColorCounts[player][color, default: 0] += 1
        }
        var winCount = 0
        for i in 0..<n {
            if let maxFreq = playerColorCounts[i].values.max(), maxFreq > i {
                winCount += 1
            }
        }
        return winCount
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun winningPlayerCount(n: Int, pick: Array<IntArray>): Int {
        val playerMaps = Array(n) { mutableMapOf<Int, Int>() }
        for (p in pick) {
            val x = p[0]
            val y = p[1]
            val map = playerMaps[x]
            map[y] = (map[y] ?: 0) + 1
        }
        var result = 0
        for (i in 0 until n) {
            var maxCnt = 0
            for (cnt in playerMaps[i].values) {
                if (cnt > maxCnt) maxCnt = cnt
            }
            if (maxCnt > i) result++
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int winningPlayerCount(int n, List<List<int>> pick) {
    List<Map<int, int>> cnt = List.generate(n, (_) => <int, int>{});
    for (var p in pick) {
      int x = p[0];
      int y = p[1];
      var map = cnt[x];
      map[y] = (map[y] ?? 0) + 1;
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
      int maxc = 0;
      for (var v in cnt[i].values) {
        if (v > maxc) maxc = v;
      }
      if (maxc > i) ans++;
    }
    return ans;
  }
}
```

## Golang

```go
func winningPlayerCount(n int, pick [][]int) int {
    counts := make([]map[int]int, n)
    for _, p := range pick {
        x, y := p[0], p[1]
        if counts[x] == nil {
            counts[x] = make(map[int]int)
        }
        counts[x][y]++
    }
    ans := 0
    for i := 0; i < n; i++ {
        maxc := 0
        for _, c := range counts[i] {
            if c > maxc {
                maxc = c
            }
        }
        if maxc > i {
            ans++
        }
    }
    return ans
}
```

## Ruby

```ruby
def winning_player_count(n, pick)
  counts = Array.new(n) { Hash.new(0) }
  pick.each do |x, y|
    counts[x][y] += 1
  end

  win = 0
  (0...n).each do |i|
    max_cnt = counts[i].values.max || 0
    win += 1 if max_cnt > i
  end
  win
end
```

## Scala

```scala
object Solution {
    def winningPlayerCount(n: Int, pick: Array[Array[Int]]): Int = {
        val playerMaps = Array.fill(n)(scala.collection.mutable.Map[Int, Int]())
        for (p <- pick) {
            val player = p(0)
            val color = p(1)
            val m = playerMaps(player)
            m(color) = m.getOrElse(color, 0) + 1
        }
        var result = 0
        for (i <- 0 until n) {
            var win = false
            val it = playerMaps(i).valuesIterator
            while (!win && it.hasNext) {
                if (it.next() > i) win = true
            }
            if (win) result += 1
        }
        result
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn winning_player_count(n: i32, pick: Vec<Vec<i32>>) -> i32 {
        let n_usize = n as usize;
        let mut player_maps: Vec<HashMap<i32, i32>> = vec![HashMap::new(); n_usize];
        for p in pick.iter() {
            let player = p[0] as usize;
            let color = p[1];
            *player_maps[player].entry(color).or_insert(0) += 1;
        }
        let mut result = 0;
        for i in 0..n_usize {
            let max_cnt = player_maps[i].values().cloned().max().unwrap_or(0);
            if max_cnt > i as i32 {
                result += 1;
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (winning-player-count n pick)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let ((players (for/vector ([i (in-range n)]) (make-hash))))
    (for ([p pick])
      (match-define (list xi yi) p)
      (let* ((h (vector-ref players xi))
             (cnt (hash-ref h yi 0)))
        (hash-set! h yi (+ cnt 1))))
    (let loop ((i 0) (ans 0))
      (if (= i n)
          ans
          (let ((h (vector-ref players i)))
            (define win? (for/or ([cnt (in-hash-values h)]) (> cnt i)))
            (loop (+ i 1) (if win? (+ ans 1) ans)))))))
```

## Erlang

```erlang
-spec winning_player_count(N :: integer(), Pick :: [[integer()]]) -> integer().
winning_player_count(N, Pick) ->
    PlayerMap = lists:foldl(
        fun([X, Y], Acc) ->
            Colors = maps:get(X, Acc, #{}),
            Count = maps:get(Y, Colors, 0) + 1,
            NewColors = maps:put(Y, Count, Colors),
            maps:put(X, NewColors, Acc)
        end,
        #{},
        Pick
    ),
    lists:foldl(
        fun(I, Acc) ->
            ColorsMap = maps:get(I, PlayerMap, #{}),
            MaxCount = case maps:values(ColorsMap) of
                [] -> 0;
                Vals -> lists:max(Vals)
            end,
            if MaxCount > I -> Acc + 1; true -> Acc end
        end,
        0,
        lists:seq(0, N - 1)
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec winning_player_count(n :: integer, pick :: [[integer]]) :: integer
  def winning_player_count(n, pick) do
    # Count occurrences for each (player, color) pair
    counts =
      Enum.reduce(pick, %{}, fn [x, y], acc ->
        Map.update(acc, {x, y}, 1, &(&1 + 1))
      end)

    0..(n - 1)
    |> Enum.count(fn i ->
      max_cnt =
        Enum.reduce(counts, 0, fn
          {{player, _color}, cnt}, acc when player == i and cnt > acc -> cnt
          _, acc -> acc
        end)

      max_cnt > i
    end)
  end
end
```
