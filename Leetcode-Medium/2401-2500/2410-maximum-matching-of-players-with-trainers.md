# 2410. Maximum Matching of Players With Trainers

## Cpp

```cpp
class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        sort(players.begin(), players.end());
        sort(trainers.begin(), trainers.end());
        int i = 0, j = 0, matches = 0;
        while (i < (int)players.size() && j < (int)trainers.size()) {
            if (trainers[j] >= players[i]) {
                ++matches;
                ++i;
                ++j;
            } else {
                ++j;
            }
        }
        return matches;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        Arrays.sort(players);
        Arrays.sort(trainers);
        int i = 0, j = 0, matches = 0;
        while (i < players.length && j < trainers.length) {
            if (trainers[j] >= players[i]) {
                matches++;
                i++;
                j++;
            } else {
                j++;
            }
        }
        return matches;
    }
}
```

## Python

```python
class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        i = j = cnt = 0
        n, m = len(players), len(trainers)
        while i < n and j < m:
            if trainers[j] >= players[i]:
                cnt += 1
                i += 1
                j += 1
            else:
                j += 1
        return cnt
```

## Python3

```python
class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        i = j = 0
        matches = 0
        while i < len(players) and j < len(trainers):
            if trainers[j] >= players[i]:
                matches += 1
                i += 1
                j += 1
            else:
                j += 1
        return matches
```

## C

```c
#include <stdlib.h>

static int cmpInt(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int matchPlayersAndTrainers(int* players, int playersSize, int* trainers, int trainersSize) {
    qsort(players, (size_t)playersSize, sizeof(int), cmpInt);
    qsort(trainers, (size_t)trainersSize, sizeof(int), cmpInt);
    
    int i = 0, j = 0, matches = 0;
    while (i < playersSize && j < trainersSize) {
        if (trainers[j] >= players[i]) {
            ++matches;
            ++i;
            ++j;
        } else {
            ++j;
        }
    }
    return matches;
}
```

## Csharp

```csharp
public class Solution {
    public int MatchPlayersAndTrainers(int[] players, int[] trainers) {
        System.Array.Sort(players);
        System.Array.Sort(trainers);
        int i = 0, j = 0, matches = 0;
        while (i < players.Length && j < trainers.Length) {
            if (trainers[j] >= players[i]) {
                matches++;
                i++;
                j++;
            } else {
                j++;
            }
        }
        return matches;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} players
 * @param {number[]} trainers
 * @return {number}
 */
var matchPlayersAndTrainers = function(players, trainers) {
    players.sort((a, b) => a - b);
    trainers.sort((a, b) => a - b);
    let i = 0, j = 0, matches = 0;
    while (i < players.length && j < trainers.length) {
        if (trainers[j] >= players[i]) {
            matches++;
            i++;
            j++;
        } else {
            j++;
        }
    }
    return matches;
};
```

## Typescript

```typescript
function matchPlayersAndTrainers(players: number[], trainers: number[]): number {
    players.sort((a, b) => a - b);
    trainers.sort((a, b) => a - b);
    let i = 0, j = 0, matches = 0;
    while (i < players.length && j < trainers.length) {
        if (trainers[j] >= players[i]) {
            matches++;
            i++;
            j++;
        } else {
            j++;
        }
    }
    return matches;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $players
     * @param Integer[] $trainers
     * @return Integer
     */
    function matchPlayersAndTrainers($players, $trainers) {
        sort($players);
        sort($trainers);
        $i = 0;
        $j = 0;
        $matches = 0;
        $pCount = count($players);
        $tCount = count($trainers);
        while ($i < $pCount && $j < $tCount) {
            if ($players[$i] <= $trainers[$j]) {
                $matches++;
                $i++;
                $j++;
            } else {
                $j++;
            }
        }
        return $matches;
    }
}
```

## Swift

```swift
class Solution {
    func matchPlayersAndTrainers(_ players: [Int], _ trainers: [Int]) -> Int {
        let sortedPlayers = players.sorted()
        let sortedTrainers = trainers.sorted()
        var i = 0
        var j = 0
        var matches = 0
        while i < sortedPlayers.count && j < sortedTrainers.count {
            if sortedTrainers[j] >= sortedPlayers[i] {
                matches += 1
                i += 1
                j += 1
            } else {
                j += 1
            }
        }
        return matches
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun matchPlayersAndTrainers(players: IntArray, trainers: IntArray): Int {
        java.util.Arrays.sort(players)
        java.util.Arrays.sort(trainers)
        var i = 0
        var j = 0
        var matches = 0
        while (i < players.size && j < trainers.size) {
            if (players[i] <= trainers[j]) {
                matches++
                i++
                j++
            } else {
                j++
            }
        }
        return matches
    }
}
```

## Dart

```dart
class Solution {
  int matchPlayersAndTrainers(List<int> players, List<int> trainers) {
    players.sort();
    trainers.sort();

    int i = 0;
    int j = 0;
    int matches = 0;

    while (i < players.length && j < trainers.length) {
      if (trainers[j] >= players[i]) {
        matches++;
        i++;
        j++;
      } else {
        j++;
      }
    }

    return matches;
  }
}
```

## Golang

```go
package main

import "sort"

func matchPlayersAndTrainers(players []int, trainers []int) int {
	sort.Ints(players)
	sort.Ints(trainers)

	i, j, count := 0, 0, 0
	for i < len(players) && j < len(trainers) {
		if trainers[j] >= players[i] {
			count++
			i++
			j++
		} else {
			j++
		}
	}
	return count
}
```

## Ruby

```ruby
def match_players_and_trainers(players, trainers)
  players.sort!
  trainers.sort!
  i = 0
  j = 0
  matches = 0
  while i < players.length && j < trainers.length
    if trainers[j] >= players[i]
      matches += 1
      i += 1
      j += 1
    else
      j += 1
    end
  end
  matches
end
```

## Scala

```scala
object Solution {
    def matchPlayersAndTrainers(players: Array[Int], trainers: Array[Int]): Int = {
        val p = players.sorted
        val t = trainers.sorted
        var i = 0
        var j = 0
        var cnt = 0
        while (i < p.length && j < t.length) {
            if (t(j) >= p(i)) {
                cnt += 1
                i += 1
                j += 1
            } else {
                j += 1
            }
        }
        cnt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn match_players_and_trainers(mut players: Vec<i32>, mut trainers: Vec<i32>) -> i32 {
        players.sort_unstable();
        trainers.sort_unstable();
        let (mut i, mut j) = (0usize, 0usize);
        let mut cnt = 0i32;
        while i < players.len() && j < trainers.len() {
            if trainers[j] >= players[i] {
                cnt += 1;
                i += 1;
                j += 1;
            } else {
                j += 1;
            }
        }
        cnt
    }
}
```

## Racket

```racket
(define/contract (match-players-and-trainers players trainers)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ([p-sorted (sort players <)]
         [t-sorted (sort trainers <)]
         [pvec (list->vector p-sorted)]
         [tvec (list->vector t-sorted)]
         [plen (vector-length pvec)]
         [tlen (vector-length tvec)])
    (let loop ([i 0] [j 0] [cnt 0])
      (cond
        [(or (= i plen) (= j tlen)) cnt]
        [(<= (vector-ref pvec i) (vector-ref tvec j))
         (loop (+ i 1) (+ j 1) (+ cnt 1))]
        [else
         (loop i (+ j 1) cnt)]))))
```

## Erlang

```erlang
-module(solution).
-export([match_players_and_trainers/2]).

-spec match_players_and_trainers(Players :: [integer()], Trainers :: [integer()]) -> integer().
match_players_and_trainers(Players, Trainers) ->
    SortedP = lists:sort(Players),
    SortedT = lists:sort(Trainers),
    match(SortedP, SortedT, 0).

-spec match([integer()], [integer()], integer()) -> integer().
match([], _Trainers, Count) -> Count;
match(_Players, [], Count) -> Count;
match([P|Ps]=Players, [T|Ts]=Trainers, Count) when T >= P ->
    match(Ps, Ts, Count + 1);
match(Players, [_T|Ts], Count) ->
    match(Players, Ts, Count).
```

## Elixir

```elixir
defmodule Solution do
  @spec match_players_and_trainers(players :: [integer], trainers :: [integer]) :: integer
  def match_players_and_trainers(players, trainers) do
    p = Enum.sort(players)
    t = Enum.sort(trainers)
    count(p, t, 0)
  end

  defp count([], _trainers, acc), do: acc
  defp count(_players, [], acc), do: acc
  defp count([p_head | p_tail] = players, [t_head | t_tail] = trainers, acc) do
    if t_head >= p_head do
      count(p_tail, t_tail, acc + 1)
    else
      count(players, t_tail, acc)
    end
  end
end
```
