# 1626. Best Team With No Conflicts

## Cpp

```cpp
class Solution {
public:
    int bestTeamScore(vector<int>& scores, vector<int>& ages) {
        int n = scores.size();
        vector<pair<int,int>> players;
        players.reserve(n);
        for (int i = 0; i < n; ++i) {
            players.emplace_back(ages[i], scores[i]);
        }
        sort(players.begin(), players.end(), [](const pair<int,int>& a, const pair<int,int>& b){
            if (a.first != b.first) return a.first < b.first;
            return a.second < b.second;
        });
        
        vector<long long> dp(n);
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            dp[i] = players[i].second; // start with own score
            for (int j = 0; j < i; ++j) {
                if (players[j].second <= players[i].second) {
                    dp[i] = max(dp[i], dp[j] + players[i].second);
                }
            }
            ans = max(ans, dp[i]);
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int bestTeamScore(int[] scores, int[] ages) {
        int n = scores.length;
        Player[] players = new Player[n];
        for (int i = 0; i < n; i++) {
            players[i] = new Player(ages[i], scores[i]);
        }
        Arrays.sort(players, (a, b) -> {
            if (a.age != b.age) return Integer.compare(a.age, b.age);
            return Integer.compare(a.score, b.score);
        });

        int[] dp = new int[n];
        int best = 0;
        for (int i = 0; i < n; i++) {
            dp[i] = players[i].score;
            for (int j = 0; j < i; j++) {
                if (players[j].score <= players[i].score) {
                    dp[i] = Math.max(dp[i], dp[j] + players[i].score);
                }
            }
            best = Math.max(best, dp[i]);
        }
        return best;
    }

    private static class Player {
        int age;
        int score;
        Player(int age, int score) {
            this.age = age;
            this.score = score;
        }
    }
}
```

## Python

```python
class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        players = list(zip(ages, scores))
        players.sort(key=lambda x: (x[0], x[1]))  # sort by age then score

        n = len(players)
        dp = [0] * n
        max_total = 0

        for i in range(n):
            cur_score = players[i][1]
            best = 0
            for j in range(i):
                if players[j][1] <= cur_score:
                    if dp[j] > best:
                        best = dp[j]
            dp[i] = best + cur_score
            if dp[i] > max_total:
                max_total = dp[i]

        return max_total
```

## Python3

```python
from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = list(zip(ages, scores))
        players.sort(key=lambda x: (x[0], x[1]))
        n = len(players)
        dp = [0] * n
        ans = 0
        for i in range(n):
            cur_score = players[i][1]
            best = 0
            for j in range(i):
                if players[j][1] <= cur_score:
                    if dp[j] > best:
                        best = dp[j]
            dp[i] = best + cur_score
            if dp[i] > ans:
                ans = dp[i]
        return ans
```

## C

```c
#include <stdlib.h>

struct Player {
    int age;
    int score;
};

static int cmpPlayer(const void *a, const void *b) {
    const struct Player *pa = (const struct Player *)a;
    const struct Player *pb = (const struct Player *)b;
    if (pa->age != pb->age)
        return pa->age - pb->age;
    return pa->score - pb->score;
}

int bestTeamScore(int* scores, int scoresSize, int* ages, int agesSize) {
    int n = scoresSize; // scoresSize == agesSize
    struct Player *players = (struct Player *)malloc(n * sizeof(struct Player));
    for (int i = 0; i < n; ++i) {
        players[i].age = ages[i];
        players[i].score = scores[i];
    }
    
    qsort(players, n, sizeof(struct Player), cmpPlayer);
    
    int *dp = (int *)malloc(n * sizeof(int));
    int best = 0;
    for (int i = 0; i < n; ++i) {
        dp[i] = players[i].score;
        for (int j = 0; j < i; ++j) {
            if (players[j].score <= players[i].score) {
                int cand = dp[j] + players[i].score;
                if (cand > dp[i]) dp[i] = cand;
            }
        }
        if (dp[i] > best) best = dp[i];
    }
    
    free(players);
    free(dp);
    return best;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int BestTeamScore(int[] scores, int[] ages) {
        int n = scores.Length;
        var players = new List<(int age, int score)>(n);
        for (int i = 0; i < n; i++) {
            players.Add((ages[i], scores[i]));
        }
        players.Sort((a, b) => {
            if (a.age != b.age) return a.age.CompareTo(b.age);
            return a.score.CompareTo(b.score);
        });
        
        int[] dp = new int[n];
        int best = 0;
        for (int i = 0; i < n; i++) {
            dp[i] = players[i].score;
            for (int j = 0; j < i; j++) {
                if (players[j].score <= players[i].score) {
                    dp[i] = Math.Max(dp[i], dp[j] + players[i].score);
                }
            }
            best = Math.Max(best, dp[i]);
        }
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} scores
 * @param {number[]} ages
 * @return {number}
 */
var bestTeamScore = function(scores, ages) {
    const n = scores.length;
    const players = new Array(n);
    for (let i = 0; i < n; ++i) {
        players[i] = [ages[i], scores[i]];
    }
    // sort by age asc, then score asc
    players.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        return a[1] - b[1];
    });
    
    const dp = new Array(n).fill(0);
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        const curScore = players[i][1];
        dp[i] = curScore;
        for (let j = 0; j < i; ++j) {
            if (players[j][1] <= curScore) {
                dp[i] = Math.max(dp[i], dp[j] + curScore);
            }
        }
        ans = Math.max(ans, dp[i]);
    }
    return ans;
};
```

## Typescript

```typescript
function bestTeamScore(scores: number[], ages: number[]): number {
    const n = scores.length;
    const players: [number, number][] = [];
    for (let i = 0; i < n; i++) {
        players.push([ages[i], scores[i]]);
    }
    players.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);

    const dp: number[] = new Array(n).fill(0);
    let maxScore = 0;

    for (let i = 0; i < n; i++) {
        const curScore = players[i][1];
        let bestPrev = 0;
        for (let j = 0; j < i; j++) {
            if (players[j][1] <= curScore && dp[j] > bestPrev) {
                bestPrev = dp[j];
            }
        }
        dp[i] = bestPrev + curScore;
        if (dp[i] > maxScore) maxScore = dp[i];
    }

    return maxScore;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $scores
     * @param Integer[] $ages
     * @return Integer
     */
    function bestTeamScore($scores, $ages) {
        $n = count($scores);
        $players = [];
        for ($i = 0; $i < $n; $i++) {
            $players[] = [$ages[$i], $scores[$i]];
        }
        usort($players, function ($a, $b) {
            if ($a[0] == $b[0]) {
                return $a[1] <=> $b[1];
            }
            return $a[0] <=> $b[0];
        });
        $dp = array_fill(0, $n, 0);
        $maxScore = 0;
        for ($i = 0; $i < $n; $i++) {
            $score_i = $players[$i][1];
            $dp[$i] = $score_i;
            for ($j = 0; $j < $i; $j++) {
                if ($players[$j][1] <= $score_i) {
                    $candidate = $dp[$j] + $score_i;
                    if ($candidate > $dp[$i]) {
                        $dp[$i] = $candidate;
                    }
                }
            }
            if ($dp[$i] > $maxScore) {
                $maxScore = $dp[$i];
            }
        }
        return $maxScore;
    }
}
```

## Swift

```swift
class Solution {
    func bestTeamScore(_ scores: [Int], _ ages: [Int]) -> Int {
        let n = scores.count
        var players = [(age: Int, score: Int)]()
        for i in 0..<n {
            players.append((ages[i], scores[i]))
        }
        players.sort { (a, b) -> Bool in
            if a.age == b.age {
                return a.score < b.score
            } else {
                return a.age < b.age
            }
        }
        
        var dp = [Int](repeating: 0, count: n)
        var result = 0
        
        for i in 0..<n {
            dp[i] = players[i].score
            for j in 0..<i {
                if players[j].score <= players[i].score {
                    dp[i] = max(dp[i], dp[j] + players[i].score)
                }
            }
            result = max(result, dp[i])
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun bestTeamScore(scores: IntArray, ages: IntArray): Int {
        val n = scores.size
        data class Player(val age: Int, val score: Int)
        val players = ArrayList<Player>(n)
        for (i in 0 until n) {
            players.add(Player(ages[i], scores[i]))
        }
        players.sortWith(compareBy<Player> { it.age }.thenBy { it.score })
        val dp = IntArray(n)
        var answer = 0
        for (i in 0 until n) {
            dp[i] = players[i].score
            for (j in 0 until i) {
                if (players[j].score <= players[i].score) {
                    dp[i] = maxOf(dp[i], dp[j] + players[i].score)
                }
            }
            answer = maxOf(answer, dp[i])
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int bestTeamScore(List<int> scores, List<int> ages) {
    int n = scores.length;
    List<List<int>> players = List.generate(
        n, (i) => [ages[i], scores[i]]);
    players.sort((a, b) {
      if (a[0] != b[0]) return a[0] - b[0];
      return a[1] - b[1];
    });

    List<int> dp = List.filled(n, 0);
    int best = 0;
    for (int i = 0; i < n; i++) {
      int curScore = players[i][1];
      dp[i] = curScore;
      for (int j = 0; j < i; j++) {
        if (players[j][1] <= curScore) {
          int candidate = dp[j] + curScore;
          if (candidate > dp[i]) dp[i] = candidate;
        }
      }
      if (dp[i] > best) best = dp[i];
    }
    return best;
  }
}
```

## Golang

```go
import "sort"

func bestTeamScore(scores []int, ages []int) int {
    n := len(scores)
    type player struct{ age, score int }
    players := make([]player, n)
    for i := 0; i < n; i++ {
        players[i] = player{age: ages[i], score: scores[i]}
    }

    sort.Slice(players, func(i, j int) bool {
        if players[i].age == players[j].age {
            return players[i].score < players[j].score
        }
        return players[i].age < players[j].age
    })

    dp := make([]int, n)
    ans := 0
    for i := 0; i < n; i++ {
        dp[i] = players[i].score
        for j := 0; j < i; j++ {
            if players[j].score <= players[i].score && dp[j]+players[i].score > dp[i] {
                dp[i] = dp[j] + players[i].score
            }
        }
        if dp[i] > ans {
            ans = dp[i]
        }
    }
    return ans
}
```

## Ruby

```ruby
def best_team_score(scores, ages)
  players = scores.each_with_index.map { |s, i| [ages[i], s] }
  players.sort_by! { |age, score| [age, score] }
  n = players.length
  sorted_scores = players.map { |_, score| score }

  dp = Array.new(n, 0)
  max_total = 0

  (0...n).each do |i|
    dp[i] = sorted_scores[i]
    (0...i).each do |j|
      if sorted_scores[j] <= sorted_scores[i]
        val = dp[j] + sorted_scores[i]
        dp[i] = val if val > dp[i]
      end
    end
    max_total = dp[i] if dp[i] > max_total
  end

  max_total
end
```

## Scala

```scala
object Solution {
    def bestTeamScore(scores: Array[Int], ages: Array[Int]): Int = {
        val players: Array[(Int, Int)] = ages.zip(scores).sortBy { case (age, score) => (age, score) }.toArray
        val n = players.length
        val dp = new Array[Int](n)
        var answer = 0

        for (i <- 0 until n) {
            dp(i) = players(i)._2 // start with own score
            var j = 0
            while (j < i) {
                if (players(j)._2 <= players(i)._2 && dp(j) + players(i)._2 > dp(i)) {
                    dp(i) = dp(j) + players(i)._2
                }
                j += 1
            }
            if (dp(i) > answer) answer = dp(i)
        }

        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn best_team_score(scores: Vec<i32>, ages: Vec<i32>) -> i32 {
        let mut players: Vec<(i32, i32)> = ages.into_iter().zip(scores.into_iter()).collect();
        players.sort_by(|a, b| {
            if a.0 != b.0 {
                a.0.cmp(&b.0)
            } else {
                a.1.cmp(&b.1)
            }
        });
        let n = players.len();
        let mut dp = vec![0i32; n];
        let mut ans = 0i32;
        for i in 0..n {
            let score_i = players[i].1;
            let mut best = 0i32;
            for j in 0..i {
                if players[j].1 <= score_i && dp[j] > best {
                    best = dp[j];
                }
            }
            dp[i] = best + score_i;
            if dp[i] > ans {
                ans = dp[i];
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (best-team-score scores ages)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length scores))
         (players
          (for/list ([i (in-range n)])
            (list (list-ref ages i) (list-ref scores i))))
         (sorted
          (sort players
                (lambda (p1 p2)
                  (let ((a1 (first p1)) (s1 (second p1))
                        (a2 (first p2)) (s2 (second p2)))
                    (or (< a1 a2) (and (= a1 a2) (< s1 s2)))))))
         (scores-vec (list->vector (map second sorted)))
         (dp (make-vector n 0)))
    (let loop ((i 0) (best 0))
      (if (= i n)
          best
          (let* ((cur (vector-ref scores-vec i))
                 (maxprev
                  (let inner ((j 0) (m 0))
                    (if (= j i)
                        m
                        (inner (add1 j)
                               (if (<= (vector-ref scores-vec j) cur)
                                   (max m (vector-ref dp j))
                                   m))))))
            (vector-set! dp i (+ cur maxprev))
            (loop (add1 i) (max best (vector-ref dp i))))))))
```

## Erlang

```erlang
-module(solution).
-export([best_team_score/2]).

-spec best_team_score(Scores :: [integer()], Ages :: [integer()]) -> integer().
best_team_score(Scores, Ages) ->
    Pairs = lists:zip(Ages, Scores),
    SortedPairs = lists:sort(
        fun({A1,S1}, {A2,S2}) ->
            (A1 < A2) orelse (A1 == A2 andalso S1 =< S2)
        end,
        Pairs
    ),
    SortedScores = [S || {_, S} <- SortedPairs],
    DPList = compute_dp(SortedScores, [], []),
    lists:max(DPList).

%% compute_dp(ScoreList, PrevScoresRev, DPsRev) -> DP list in original order
compute_dp([], _PrevScoresRev, DPsRev) ->
    lists:reverse(DPsRev);
compute_dp([S|Rest], PrevScoresRev, DPsRev) ->
    MaxPrev = max_compatible(S, PrevScoresRev, DPsRev),
    DP_i = S + MaxPrev,
    compute_dp(Rest, [S|PrevScoresRev], [DP_i|DPsRev]).

%% max_compatible(CurrentScore, PrevScoresRev, PrevDPsRev) -> maximum dp among previous scores <= CurrentScore
max_compatible(_Cur, [], []) ->
    0;
max_compatible(Cur, [PrevScore|RestScores], [PrevDP|RestDPs]) ->
    case PrevScore =< Cur of
        true ->
            MaxRest = max_compatible(Cur, RestScores, RestDPs),
            if PrevDP > MaxRest -> PrevDP; true -> MaxRest end;
        false ->
            max_compatible(Cur, RestScores, RestDPs)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec best_team_score(scores :: [integer], ages :: [integer]) :: integer
  def best_team_score(scores, ages) do
    players = Enum.zip(ages, scores)

    sorted =
      Enum.sort(players, fn {a1, s1}, {a2, s2} ->
        if a1 == a2, do: s1 <= s2, else: a1 <= a2
      end)

    scores_sorted = Enum.map(sorted, fn {_age, score} -> score end)

    {dp_rev, _} =
      Enum.reduce(scores_sorted, {[], []}, fn score_i, {dp_acc, scores_acc} ->
        max_prev =
          scores_acc
          |> Enum.zip(dp_acc)
          |> Enum.filter(fn {s, _dp} -> s <= score_i end)
          |> Enum.map(fn {_s, dpv} -> dpv end)
          |> (fn list -> if list == [], do: 0, else: Enum.max(list) end).()

        current = max_prev + score_i
        {[current | dp_acc], [score_i | scores_acc]}
      end)

    dp = Enum.reverse(dp_rev)
    Enum.max(dp)
  end
end
```
