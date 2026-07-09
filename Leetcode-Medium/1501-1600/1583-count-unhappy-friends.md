# 1583. Count Unhappy Friends

## Cpp

```cpp
class Solution {
public:
    int unhappyFriends(int n, vector<vector<int>>& preferences, vector<vector<int>>& pairs) {
        vector<vector<int>> rank(n, vector<int>(n));
        for (int i = 0; i < n; ++i) {
            for (int idx = 0; idx < (int)preferences[i].size(); ++idx) {
                rank[i][preferences[i][idx]] = idx;
            }
        }
        vector<int> partner(n, -1);
        for (auto& p : pairs) {
            int a = p[0], b = p[1];
            partner[a] = b;
            partner[b] = a;
        }
        int unhappy = 0;
        for (int x = 0; x < n; ++x) {
            int y = partner[x];
            for (int u : preferences[x]) {
                if (u == y) break; // reached current partner
                int v = partner[u];
                if (rank[u][x] < rank[u][v]) { // u prefers x over its own partner
                    ++unhappy;
                    break;
                }
            }
        }
        return unhappy;
    }
};
```

## Java

```java
class Solution {
    public int unhappyFriends(int n, int[][] preferences, int[][] pairs) {
        int[][] rank = new int[n][n];
        for (int i = 0; i < n; i++) {
            int[] pref = preferences[i];
            for (int j = 0; j < pref.length; j++) {
                rank[i][pref[j]] = j;
            }
        }

        int[] partner = new int[n];
        for (int[] pair : pairs) {
            int a = pair[0], b = pair[1];
            partner[a] = b;
            partner[b] = a;
        }

        boolean[] unhappy = new boolean[n];
        for (int i = 0; i < n; i++) {
            int currentPartner = partner[i];
            for (int u : preferences[i]) {
                if (u == currentPartner) break;
                int v = partner[u];
                if (rank[u][i] < rank[u][v]) {
                    unhappy[i] = true;
                    break;
                }
            }
        }

        int count = 0;
        for (boolean b : unhappy) {
            if (b) count++;
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        # rank[i][j] = position of j in i's preference list (lower is better)
        rank = [[0]*n for _ in range(n)]
        for i in range(n):
            for pos, friend in enumerate(preferences[i]):
                rank[i][friend] = pos

        partner = [0]*n
        for x, y in pairs:
            partner[x] = y
            partner[y] = x

        unhappy = set()
        for x in range(n):
            y = partner[x]
            # iterate over friends that x prefers more than current partner y
            for u in preferences[x]:
                if u == y:
                    break  # reached current partner, stop
                v = partner[u]
                # check if u also prefers x over its own partner v
                if rank[u][x] < rank[u][v]:
                    unhappy.add(x)
                    break  # no need to check further for x

        return len(unhappy)
```

## Python3

```python
class Solution:
    def unhappyFriends(self, n: int, preferences: list[list[int]], pairs: list[list[int]]) -> int:
        # rank[i][j] = position of j in i's preference list (lower is more preferred)
        rank = [[0] * n for _ in range(n)]
        for i in range(n):
            for pos, friend in enumerate(preferences[i]):
                rank[i][friend] = pos

        partner = [0] * n
        for x, y in pairs:
            partner[x] = y
            partner[y] = x

        def is_unhappy(x: int, y: int) -> bool:
            # iterate over friends that x prefers more than y
            for u in preferences[x]:
                if u == y:
                    break
                v = partner[u]
                # u prefers x over its own partner v?
                if rank[u][x] < rank[u][v]:
                    return True
            return False

        unhappy = 0
        for x, y in pairs:
            if is_unhappy(x, y):
                unhappy += 1
            if is_unhappy(y, x):
                unhappy += 1
        return unhappy
```

## C

```c
int unhappyFriends(int n, int** preferences, int preferencesSize, int* preferencesColSize, int** pairs, int pairsSize, int* pairsColSize){
    static int rank[501][501];
    int partner[501];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < preferencesColSize[i]; ++j) {
            int f = preferences[i][j];
            rank[i][f] = j;
        }
    }
    for (int i = 0; i < pairsSize; ++i) {
        int a = pairs[i][0], b = pairs[i][1];
        partner[a] = b;
        partner[b] = a;
    }
    int unhappy = 0;
    for (int x = 0; x < n; ++x) {
        int y = partner[x];
        int isUnhappy = 0;
        for (int k = 0; k < preferencesColSize[x]; ++k) {
            int u = preferences[x][k];
            if (u == y) break;
            int v = partner[u];
            if (rank[u][x] < rank[u][v]) {
                isUnhappy = 1;
                break;
            }
        }
        unhappy += isUnhappy;
    }
    return unhappy;
}
```

## Csharp

```csharp
public class Solution {
    public int UnhappyFriends(int n, int[][] preferences, int[][] pairs) {
        // rank[i][j] = position of j in i's preference list (lower is more preferred)
        int[,] rank = new int[n, n];
        for (int i = 0; i < n; i++) {
            int[] pref = preferences[i];
            for (int pos = 0; pos < pref.Length; pos++) {
                rank[i, pref[pos]] = pos;
            }
        }

        // partner[x] = y
        int[] partner = new int[n];
        foreach (var p in pairs) {
            int a = p[0], b = p[1];
            partner[a] = b;
            partner[b] = a;
        }

        bool[] unhappy = new bool[n];
        for (int x = 0; x < n; x++) {
            int y = partner[x];
            foreach (int u in preferences[x]) {
                if (u == y) break; // reached current partner, stop checking lower preferences
                int v = partner[u];
                // u prefers x over its own partner v ?
                if (rank[u, x] < rank[u, v]) {
                    unhappy[x] = true;
                    break;
                }
            }
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            if (unhappy[i]) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} preferences
 * @param {number[][]} pairs
 * @return {number}
 */
var unhappyFriends = function(n, preferences, pairs) {
    // rank[i][j] = how many people i prefers over j (lower is better)
    const rank = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < n; i++) {
        const pref = preferences[i];
        for (let pos = 0; pos < pref.length; pos++) {
            rank[i][pref[pos]] = pos;
        }
    }

    // partner[x] = y
    const partner = Array(n);
    for (const [a, b] of pairs) {
        partner[a] = b;
        partner[b] = a;
    }

    let unhappy = 0;
    for (let x = 0; x < n; x++) {
        const y = partner[x];
        // check friends that x prefers over current partner
        for (const u of preferences[x]) {
            if (u === y) break; // reached current partner, stop
            const v = partner[u];
            // if u also prefers x over its own partner v, then x is unhappy
            if (rank[u][x] < rank[u][v]) {
                unhappy++;
                break;
            }
        }
    }

    return unhappy;
};
```

## Typescript

```typescript
function unhappyFriends(n: number, preferences: number[][], pairs: number[][]): number {
    const rank: number[][] = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < n; i++) {
        const pref = preferences[i];
        for (let j = 0; j < pref.length; j++) {
            rank[i][pref[j]] = j;
        }
    }

    const partner: number[] = new Array(n);
    for (const [a, b] of pairs) {
        partner[a] = b;
        partner[b] = a;
    }

    const unhappy: boolean[] = new Array(n).fill(false);

    for (let x = 0; x < n; x++) {
        const y = partner[x];
        for (const u of preferences[x]) {
            if (u === y) break;
            const v = partner[u];
            if (rank[u][x] < rank[u][v]) {
                unhappy[x] = true;
                break;
            }
        }
    }

    let count = 0;
    for (let i = 0; i < n; i++) {
        if (unhappy[i]) count++;
    }
    return count;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $preferences
     * @param Integer[][] $pairs
     * @return Integer
     */
    function unhappyFriends($n, $preferences, $pairs) {
        // rank[i][j] = how much i prefers j (lower is better)
        $rank = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            foreach ($preferences[$i] as $pos => $friend) {
                $rank[$i][$friend] = $pos;
            }
        }

        // partner mapping
        $partner = array_fill(0, $n, -1);
        foreach ($pairs as $pair) {
            $a = $pair[0];
            $b = $pair[1];
            $partner[$a] = $b;
            $partner[$b] = $a;
        }

        $unhappy = [];

        for ($x = 0; $x < $n; $x++) {
            $y = $partner[$x];
            foreach ($preferences[$x] as $friend) {
                if ($friend == $y) {
                    break; // reached current partner, stop checking further
                }
                $u = $friend;
                $v = $partner[$u];
                // u prefers x over its own partner v?
                if ($rank[$u][$x] < $rank[$u][$v]) {
                    $unhappy[$x] = true;
                    break;
                }
            }
        }

        return count($unhappy);
    }
}
```

## Swift

```swift
class Solution {
    func unhappyFriends(_ n: Int, _ preferences: [[Int]], _ pairs: [[Int]]) -> Int {
        var partner = [Int](repeating: -1, count: n)
        for p in pairs {
            let a = p[0]
            let b = p[1]
            partner[a] = b
            partner[b] = a
        }
        
        var rank = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n {
            for (pos, friend) in preferences[i].enumerated() {
                rank[i][friend] = pos
            }
        }
        
        var unhappy = 0
        for x in 0..<n {
            let y = partner[x]
            for u in preferences[x] {
                if u == y { break }
                let v = partner[u]
                if rank[u][x] < rank[u][v] {
                    unhappy += 1
                    break
                }
            }
        }
        return unhappy
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun unhappyFriends(n: Int, preferences: Array<IntArray>, pairs: Array<IntArray>): Int {
        val rank = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            val pref = preferences[i]
            for (j in pref.indices) {
                rank[i][pref[j]] = j
            }
        }

        val partner = IntArray(n)
        for (pair in pairs) {
            val a = pair[0]
            val b = pair[1]
            partner[a] = b
            partner[b] = a
        }

        var unhappy = 0
        for (x in 0 until n) {
            val y = partner[x]
            for (u in preferences[x]) {
                if (u == y) break
                val v = partner[u]
                if (rank[u][x] < rank[u][v]) {
                    unhappy++
                    break
                }
            }
        }
        return unhappy
    }
}
```

## Dart

```dart
class Solution {
  int unhappyFriends(int n, List<List<int>> preferences, List<List<int>> pairs) {
    // partner mapping
    List<int> partner = List.filled(n, -1);
    for (var p in pairs) {
      int a = p[0];
      int b = p[1];
      partner[a] = b;
      partner[b] = a;
    }

    // rank matrix: rank[i][j] = preference order of j for i (lower is better)
    List<List<int>> rank = List.generate(n, (_) => List.filled(n, 0));
    for (int i = 0; i < n; ++i) {
      var pref = preferences[i];
      for (int idx = 0; idx < pref.length; ++idx) {
        rank[i][pref[idx]] = idx;
      }
    }

    Set<int> unhappy = {};

    // check each pair
    for (var p in pairs) {
      int x = p[0];
      int y = p[1];

      // check x
      for (int u in preferences[x]) {
        if (u == y) break;
        int v = partner[u];
        if (rank[u][x] < rank[u][v]) {
          unhappy.add(x);
          break;
        }
      }

      // check y
      for (int u in preferences[y]) {
        if (u == x) break;
        int v = partner[u];
        if (rank[u][y] < rank[u][v]) {
          unhappy.add(y);
          break;
        }
      }
    }

    return unhappy.length;
  }
}
```

## Golang

```go
func unhappyFriends(n int, preferences [][]int, pairs [][]int) int {
    // rank[i][j] = position of j in i's preference list (lower is more preferred)
    rank := make([][]int, n)
    for i := 0; i < n; i++ {
        rank[i] = make([]int, n)
        for pos, friend := range preferences[i] {
            rank[i][friend] = pos
        }
    }

    // partner[x] = y
    partner := make([]int, n)
    for _, p := range pairs {
        a, b := p[0], p[1]
        partner[a] = b
        partner[b] = a
    }

    unhappy := make([]bool, n)

    for x := 0; x < n; x++ {
        y := partner[x]
        // iterate over friends that x prefers more than y
        for _, u := range preferences[x] {
            if u == y {
                break
            }
            v := partner[u]
            // check if u also prefers x over its current partner v
            if rank[u][x] < rank[u][v] {
                unhappy[x] = true
                break
            }
        }
    }

    cnt := 0
    for _, flag := range unhappy {
        if flag {
            cnt++
        }
    }
    return cnt
}
```

## Ruby

```ruby
def unhappy_friends(n, preferences, pairs)
  rank = Array.new(n) { Array.new(n, 0) }
  preferences.each_with_index do |pref, i|
    pref.each_with_index { |friend, idx| rank[i][friend] = idx }
  end

  partner = Array.new(n)
  pairs.each { |x, y| partner[x] = y; partner[y] = x }

  unhappy = Array.new(n, false)

  (0...n).each do |i|
    current_partner = partner[i]
    preferences[i].each do |u|
      break if u == current_partner
      v = partner[u]
      if rank[u][i] < rank[u][v]
        unhappy[i] = true
        unhappy[u] = true
      end
    end
  end

  unhappy.count(true)
end
```

## Scala

```scala
object Solution {
    def unhappyFriends(n: Int, preferences: Array[Array[Int]], pairs: Array[Array[Int]]): Int = {
        val rank = Array.ofDim[Int](n, n)
        for (i <- 0 until n) {
            val pref = preferences(i)
            var idx = 0
            while (idx < pref.length) {
                rank(i)(pref(idx)) = idx
                idx += 1
            }
        }

        val partner = new Array[Int](n)
        for (p <- pairs) {
            val a = p(0)
            val b = p(1)
            partner(a) = b
            partner(b) = a
        }

        var unhappyCount = 0
        for (x <- 0 until n) {
            val y = partner(x)
            val prefX = preferences(x)
            var i = 0
            var isUnhappy = false
            while (i < prefX.length && prefX(i) != y && !isUnhappy) {
                val u = prefX(i)
                val v = partner(u)
                if (rank(u)(x) < rank(u)(v)) {
                    isUnhappy = true
                }
                i += 1
            }
            if (isUnhappy) unhappyCount += 1
        }

        unhappyCount
    }
}
```

## Rust

```rust
impl Solution {
    pub fn unhappy_friends(n: i32, preferences: Vec<Vec<i32>>, pairs: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        // rank[i][j] = position of j in i's preference list (lower is more preferred)
        let mut rank = vec![vec![0usize; n]; n];
        for i in 0..n {
            for (pos, &friend) in preferences[i].iter().enumerate() {
                rank[i][friend as usize] = pos;
            }
        }

        // partner[i] = the friend paired with i
        let mut partner = vec![0usize; n];
        for p in pairs.iter() {
            let a = p[0] as usize;
            let b = p[1] as usize;
            partner[a] = b;
            partner[b] = a;
        }

        // determine unhappy friends
        let mut unhappy = vec![false; n];
        for i in 0..n {
            let y = partner[i];
            for &u_i32 in preferences[i].iter() {
                let u = u_i32 as usize;
                if u == y {
                    break;
                }
                let v = partner[u];
                // u prefers i over its own partner v?
                if rank[u][i] < rank[u][v] {
                    unhappy[i] = true;
                    break;
                }
            }
        }

        unhappy.iter().filter(|&&b| b).count() as i32
    }
}
```

## Racket

```racket
(define/contract (unhappy-friends n preferences pairs)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      exact-integer?)
  (let* ([partner (make-vector n -1)]
         [rank   (make-vector n)])
    ;; build rank matrix
    (for ([i (in-range n)])
      (let* ([pref (list-ref preferences i)]
             [rvec (make-vector n 0)])
        (for ([j (in-naturals)] [f pref])
          (vector-set! rvec f j))
        (vector-set! rank i rvec)))
    ;; fill partner information
    (for ([pair pairs])
      (let* ([x (list-ref pair 0)]
             [y (list-ref pair 1)])
        (vector-set! partner x y)
        (vector-set! partner y x)))
    ;; helper to decide if a friend is unhappy
    (define (unhappy? x)
      (let* ([y   (vector-ref partner x)]
             [pref (list-ref preferences x)])
        (let loop ((lst pref))
          (cond [(null? lst) #f]
                [(eq? (car lst) y) #f] ; reached current partner
                [else
                 (let* ([u (car lst)]
                        [v (vector-ref partner u)])
                   (if (< (vector-ref (vector-ref rank u) x)
                          (vector-ref (vector-ref rank u) v))
                       #t
                       (loop (cdr lst))))]))))
    ;; count unhappy friends
    (let loop ((i 0) (cnt 0))
      (if (= i n)
          cnt
          (loop (+ i 1) (if (unhappy? i) (+ cnt 1) cnt))))) )
```

## Erlang

```erlang
-module(solution).
-export([unhappy_friends/3]).

-spec unhappy_friends(N :: integer(), Preferences :: [[integer()]], Pairs :: [[integer()]]) -> integer().
unhappy_friends(_N, Preferences, Pairs) ->
    PartnerMap = build_partner_map(Pairs),
    RankMap = build_rank_map(Preferences),
    lists:foldl(
        fun(X, Acc) ->
            Y = maps:get(X, PartnerMap),
            PrefList = lists:nth(X + 1, Preferences),
            case is_unhappy(X, Y, PrefList, PartnerMap, RankMap) of
                true -> Acc + 1;
                false -> Acc
            end
        end,
        0,
        lists:seq(0, length(Preferences) - 1)
    ).

build_partner_map(Pairs) ->
    lists:foldl(
        fun([A, B], M) ->
            M1 = maps:put(A, B, M),
            maps:put(B, A, M1)
        end,
        #{},
        Pairs
    ).

build_rank_map(Preferences) ->
    lists:foldl(
        fun({I, PrefList}, Acc) ->
            Inner = build_inner_rank(PrefList, 0, #{}),
            maps:put(I, Inner, Acc)
        end,
        #{},
        lists:zip(lists:seq(0, length(Preferences) - 1), Preferences)
    ).

build_inner_rank([], _Pos, M) -> M;
build_inner_rank([Friend | Rest], Pos, M) ->
    NewM = maps:put(Friend, Pos, M),
    build_inner_rank(Rest, Pos + 1, NewM).

is_unhappy(_X, _Y, [], _PartnerMap, _RankMap) -> false;
is_unhappy(X, Y, [U | Rest], PartnerMap, RankMap) ->
    if
        U =:= Y ->
            false; % reached current partner, stop checking
        true ->
            V = maps:get(U, PartnerMap),
            RankU = maps:get(U, RankMap),
            RankUX = maps:get(X, RankU),
            RankUV = maps:get(V, RankU),
            if
                RankUX < RankUV -> true;
                true -> is_unhappy(X, Y, Rest, PartnerMap, RankMap)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec unhappy_friends(integer, [[integer]], [[integer]]) :: integer
  def unhappy_friends(_n, preferences, pairs) do
    # rank[i][j] = position of j in i's preference list (lower is better)
    rank =
      Enum.map(preferences, fn pref ->
        Enum.with_index(pref)
        |> Enum.reduce(%{}, fn {friend, idx}, acc -> Map.put(acc, friend, idx) end)
      end)

    # partner map: person => their paired friend
    partner_map =
      for [a, b] <- pairs, into: %{} do
        {a, b}
        {b, a}
      end

    unhappy_set =
      Enum.reduce(pairs, MapSet.new(), fn [x, y], set ->
        set = if is_unhappy(x, y, preferences, rank, partner_map), do: MapSet.put(set, x), else: set
        set = if is_unhappy(y, x, preferences, rank, partner_map), do: MapSet.put(set, y), else: set
        set
      end)

    MapSet.size(unhappy_set)
  end

  defp is_unhappy(person, current_partner, preferences, rank, partner_map) do
    Enum.reduce_while(Enum.at(preferences, person), false, fn other, _acc ->
      if other == current_partner do
        {:halt, false}
      else
        other_partner = Map.get(partner_map, other)
        rank_other = Enum.at(rank, other)

        cond do
          Map.get(rank_other, person) < Map.get(rank_other, other_partner) ->
            {:halt, true}

          true ->
            {:cont, false}
        end
      end
    end)
  end
end
```
