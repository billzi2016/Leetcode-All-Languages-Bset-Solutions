# 1686. Stone Game VI

## Cpp

```cpp
class Solution {
public:
    int stoneGameVI(vector<int>& aliceValues, vector<int>& bobValues) {
        int n = aliceValues.size();
        vector<pair<int,int>> stones;
        stones.reserve(n);
        for (int i = 0; i < n; ++i) {
            stones.emplace_back(aliceValues[i] + bobValues[i], i);
        }
        sort(stones.begin(), stones.end(),
             [](const pair<int,int>& a, const pair<int,int>& b){
                 return a.first > b.first;
             });
        long long aliceScore = 0, bobScore = 0;
        for (int turn = 0; turn < n; ++turn) {
            int idx = stones[turn].second;
            if ((turn & 1) == 0) { // Alice's turn
                aliceScore += aliceValues[idx];
            } else { // Bob's turn
                bobScore += bobValues[idx];
            }
        }
        if (aliceScore > bobScore) return 1;
        if (aliceScore < bobScore) return -1;
        return 0;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int stoneGameVI(int[] aliceValues, int[] bobValues) {
        int n = aliceValues.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) {
            idx[i] = i;
        }
        Arrays.sort(idx, (i, j) -> Integer.compare(aliceValues[j] + bobValues[j],
                                                   aliceValues[i] + bobValues[i]));
        long aliceScore = 0;
        long bobScore = 0;
        for (int turn = 0; turn < n; turn++) {
            int i = idx[turn];
            if ((turn & 1) == 0) {
                aliceScore += aliceValues[i];
            } else {
                bobScore += bobValues[i];
            }
        }
        return Long.compare(aliceScore, bobScore);
    }
}
```

## Python

```python
class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        combined = [a + b for a, b in zip(aliceValues, bobValues)]
        # sort indices by combined value descending
        idx = sorted(range(len(combined)), key=lambda i: combined[i], reverse=True)
        alice_score = 0
        bob_score = 0
        for turn, i in enumerate(idx):
            if turn % 2 == 0:
                alice_score += aliceValues[i]
            else:
                bob_score += bobValues[i]
        if alice_score > bob_score:
            return 1
        elif alice_score < bob_score:
            return -1
        else:
            return 0
```

## Python3

```python
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        stones = sorted(zip(aliceValues, bobValues), key=lambda x: x[0] + x[1], reverse=True)
        alice_score = 0
        bob_score = 0
        for i, (a, b) in enumerate(stones):
            if i % 2 == 0:
                alice_score += a
            else:
                bob_score += b
        if alice_score > bob_score:
            return 1
        if alice_score < bob_score:
            return -1
        return 0
```

## C

```c
#include <stdlib.h>

typedef struct {
    int total;
    int a;
    int b;
} Stone;

static int cmpStone(const void *p1, const void *p2) {
    const Stone *s1 = (const Stone *)p1;
    const Stone *s2 = (const Stone *)p2;
    return s2->total - s1->total; // descending order
}

int stoneGameVI(int* aliceValues, int aliceValuesSize, int* bobValues, int bobValuesSize) {
    int n = aliceValuesSize;
    Stone *stones = (Stone *)malloc(sizeof(Stone) * n);
    for (int i = 0; i < n; ++i) {
        stones[i].total = aliceValues[i] + bobValues[i];
        stones[i].a = aliceValues[i];
        stones[i].b = bobValues[i];
    }
    
    qsort(stones, n, sizeof(Stone), cmpStone);
    
    long long aliceScore = 0, bobScore = 0;
    for (int i = 0; i < n; ++i) {
        if ((i & 1) == 0)
            aliceScore += stones[i].a;
        else
            bobScore += stones[i].b;
    }
    
    free(stones);
    
    if (aliceScore > bobScore) return 1;
    if (aliceScore < bobScore) return -1;
    return 0;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int StoneGameVI(int[] aliceValues, int[] bobValues) {
        int n = aliceValues.Length;
        int[] idx = new int[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Array.Sort(idx, (i, j) => {
            int sumI = aliceValues[i] + bobValues[i];
            int sumJ = aliceValues[j] + bobValues[j];
            return sumJ.CompareTo(sumI); // descending
        });
        long aliceScore = 0, bobScore = 0;
        for (int turn = 0; turn < n; turn++) {
            int i = idx[turn];
            if ((turn & 1) == 0) {
                aliceScore += aliceValues[i];
            } else {
                bobScore += bobValues[i];
            }
        }
        if (aliceScore > bobScore) return 1;
        if (aliceScore < bobScore) return -1;
        return 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} aliceValues
 * @param {number[]} bobValues
 * @return {number}
 */
var stoneGameVI = function(aliceValues, bobValues) {
    const n = aliceValues.length;
    const idx = new Array(n);
    for (let i = 0; i < n; ++i) idx[i] = i;
    idx.sort((a, b) => (bobValues[b] + aliceValues[b]) - (bobValues[a] + aliceValues[a]));
    
    let aScore = 0, bScore = 0;
    for (let turn = 0; turn < n; ++turn) {
        const i = idx[turn];
        if ((turn & 1) === 0) {
            aScore += aliceValues[i];
        } else {
            bScore += bobValues[i];
        }
    }
    
    if (aScore > bScore) return 1;
    if (aScore < bScore) return -1;
    return 0;
};
```

## Typescript

```typescript
function stoneGameVI(aliceValues: number[], bobValues: number[]): number {
    const n = aliceValues.length;
    const order = Array.from({ length: n }, (_, i) => i);
    order.sort((i, j) => (bobValues[j] + aliceValues[j]) - (bobValues[i] + aliceValues[i]));
    let aliceScore = 0, bobScore = 0;
    for (let turn = 0; turn < n; ++turn) {
        const idx = order[turn];
        if (turn % 2 === 0) {
            aliceScore += aliceValues[idx];
        } else {
            bobScore += bobValues[idx];
        }
    }
    return aliceScore > bobScore ? 1 : aliceScore < bobScore ? -1 : 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $aliceValues
     * @param Integer[] $bobValues
     * @return Integer
     */
    function stoneGameVI($aliceValues, $bobValues) {
        $n = count($aliceValues);
        $indices = range(0, $n - 1);
        usort($indices, function ($i, $j) use ($aliceValues, $bobValues) {
            $sumI = $aliceValues[$i] + $bobValues[$i];
            $sumJ = $aliceValues[$j] + $bobValues[$j];
            if ($sumI == $sumJ) return 0;
            return ($sumI > $sumJ) ? -1 : 1; // descending order
        });

        $aliceScore = 0;
        $bobScore = 0;
        foreach ($indices as $k => $idx) {
            if (($k & 1) == 0) { // Alice's turn
                $aliceScore += $aliceValues[$idx];
            } else { // Bob's turn
                $bobScore += $bobValues[$idx];
            }
        }

        if ($aliceScore > $bobScore) return 1;
        if ($aliceScore < $bobScore) return -1;
        return 0;
    }
}
```

## Swift

```swift
class Solution {
    func stoneGameVI(_ aliceValues: [Int], _ bobValues: [Int]) -> Int {
        let n = aliceValues.count
        var indices = Array(0..<n)
        indices.sort { (i, j) -> Bool in
            return (aliceValues[i] + bobValues[i]) > (aliceValues[j] + bobValues[j])
        }
        var aliceScore = 0
        var bobScore = 0
        for (turn, idx) in indices.enumerated() {
            if turn % 2 == 0 {
                aliceScore += aliceValues[idx]
            } else {
                bobScore += bobValues[idx]
            }
        }
        if aliceScore > bobScore { return 1 }
        if aliceScore < bobScore { return -1 }
        return 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun stoneGameVI(aliceValues: IntArray, bobValues: IntArray): Int {
        val n = aliceValues.size
        val order = (0 until n).toMutableList()
        order.sortWith { i, j ->
            val sumI = aliceValues[i] + bobValues[i]
            val sumJ = aliceValues[j] + bobValues[j]
            when {
                sumI > sumJ -> -1
                sumI < sumJ -> 1
                else -> 0
            }
        }
        var aliceScore = 0L
        var bobScore = 0L
        for (k in order.indices) {
            val idx = order[k]
            if ((k and 1) == 0) {
                aliceScore += aliceValues[idx].toLong()
            } else {
                bobScore += bobValues[idx].toLong()
            }
        }
        return when {
            aliceScore > bobScore -> 1
            aliceScore < bobScore -> -1
            else -> 0
        }
    }
}
```

## Dart

```dart
class Solution {
  int stoneGameVI(List<int> aliceValues, List<int> bobValues) {
    int n = aliceValues.length;
    List<int> idx = List.generate(n, (i) => i);
    idx.sort((a, b) {
      int sumA = aliceValues[a] + bobValues[a];
      int sumB = aliceValues[b] + bobValues[b];
      return sumB.compareTo(sumA); // descending order
    });
    int aliceScore = 0;
    int bobScore = 0;
    for (int turn = 0; turn < n; ++turn) {
      int i = idx[turn];
      if (turn % 2 == 0) {
        aliceScore += aliceValues[i];
      } else {
        bobScore += bobValues[i];
      }
    }
    if (aliceScore > bobScore) return 1;
    if (aliceScore < bobScore) return -1;
    return 0;
  }
}
```

## Golang

```go
package main

import "sort"

func stoneGameVI(aliceValues []int, bobValues []int) int {
	n := len(aliceValues)
	type pair struct{ sum, idx int }
	arr := make([]pair, n)
	for i := 0; i < n; i++ {
		arr[i] = pair{aliceValues[i] + bobValues[i], i}
	}
	sort.Slice(arr, func(i, j int) bool { return arr[i].sum > arr[j].sum })
	aliceScore, bobScore := 0, 0
	for turn, p := range arr {
		if turn%2 == 0 {
			aliceScore += aliceValues[p.idx]
		} else {
			bobScore += bobValues[p.idx]
		}
	}
	if aliceScore > bobScore {
		return 1
	}
	if aliceScore < bobScore {
		return -1
	}
	return 0
}
```

## Ruby

```ruby
def stone_game_vi(alice_values, bob_values)
  n = alice_values.length
  indices = (0...n).to_a
  indices.sort! do |i, j|
    (alice_values[j] + bob_values[j]) <=> (alice_values[i] + bob_values[i])
  end

  a_score = 0
  b_score = 0
  indices.each_with_index do |idx, turn|
    if turn.even?
      a_score += alice_values[idx]
    else
      b_score += bob_values[idx]
    end
  end

  return 1 if a_score > b_score
  return -1 if a_score < b_score
  0
end
```

## Scala

```scala
object Solution {
    def stoneGameVI(aliceValues: Array[Int], bobValues: Array[Int]): Int = {
        val n = aliceValues.length
        val order = (0 until n).toArray.sortWith { (i, j) =>
            val si = aliceValues(i) + bobValues(i)
            val sj = aliceValues(j) + bobValues(j)
            if (si != sj) si > sj else i < j
        }
        var aScore: Long = 0L
        var bScore: Long = 0L
        for (k <- order.indices) {
            val idx = order(k)
            if ((k & 1) == 0) aScore += aliceValues(idx)
            else bScore += bobValues(idx)
        }
        if (aScore > bScore) 1 else if (aScore < bScore) -1 else 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn stone_game_vi(alice_values: Vec<i32>, bob_values: Vec<i32>) -> i32 {
        let n = alice_values.len();
        let mut idxs: Vec<usize> = (0..n).collect();
        idxs.sort_by(|&i, &j| {
            let sum_i = alice_values[i] + bob_values[i];
            let sum_j = alice_values[j] + bob_values[j];
            sum_j.cmp(&sum_i) // descending
        });
        let mut a_score: i64 = 0;
        let mut b_score: i64 = 0;
        for (turn, &i) in idxs.iter().enumerate() {
            if turn % 2 == 0 {
                a_score += alice_values[i] as i64;
            } else {
                b_score += bob_values[i] as i64;
            }
        }
        if a_score > b_score {
            1
        } else if a_score < b_score {
            -1
        } else {
            0
        }
    }
}
```

## Racket

```racket
(define/contract (stone-game-vi aliceValues bobValues)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((triples
          (for/list ([a aliceValues] [b bobValues])
            (list (+ a b) a b)))
         (sorted (sort triples (lambda (x y) (> (first x) (first y))))))
    (let loop ((i 0) (alice 0) (bob 0) (lst sorted))
      (if (null? lst)
          (cond [(> alice bob) 1]
                [(= alice bob) 0]
                [else -1])
          (match (first lst)
            [(list _ a b)
             (if (even? i)
                 (loop (+ i 1) (+ alice a) bob (rest lst))
                 (loop (+ i 1) alice (+ bob b) (rest lst)))])))))
```

## Erlang

```erlang
-module(solution).
-export([stone_game_vi/2]).

-spec stone_game_vi(AliceValues :: [integer()], BobValues :: [integer()]) -> integer().
stone_game_vi(AliceValues, BobValues) ->
    List = build_list(AliceValues, BobValues, []),
    Sorted = lists:sort(fun({S1,_,_}, {S2,_,_}) -> S1 > S2 end, List),
    {AScore, BScore, _} = lists:foldl(
        fun({_, A, B}, {As, Bs, Turn}) ->
            case Turn of
                0 -> {As + A, Bs, 1};
                1 -> {As, Bs + B, 0}
            end
        end,
        {0, 0, 0},
        Sorted),
    compare(AScore, BScore).

build_list([], [], Acc) ->
    lists:reverse(Acc);
build_list([A|As], [B|Bs], Acc) ->
    Sum = A + B,
    build_list(As, Bs, [{Sum, A, B} | Acc]).

compare(A, B) when A > B -> 1;
compare(A, B) when A < B -> -1;
compare(_, _) -> 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec stone_game_vi(alice_values :: [integer], bob_values :: [integer]) :: integer
  def stone_game_vi(alice_values, bob_values) do
    combined =
      Enum.zip([alice_values, bob_values])
      |> Enum.map(fn {a, b} -> {a + b, a, b} end)

    sorted = Enum.sort_by(combined, fn {sum, _, _} -> -sum end)

    {alice_score, bob_score} =
      Enum.reduce(Enum.with_index(sorted), {0, 0}, fn {{_sum, a, b}, idx},
                                                    {ascore, bscore} ->
        if rem(idx, 2) == 0 do
          {ascore + a, bscore}
        else
          {ascore, bscore + b}
        end
      end)

    cond do
      alice_score > bob_score -> 1
      alice_score < bob_score -> -1
      true -> 0
    end
  end
end
```
