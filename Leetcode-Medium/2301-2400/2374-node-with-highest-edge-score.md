# 2374. Node With Highest Edge Score

## Cpp

```cpp
class Solution {
public:
    int edgeScore(vector<int>& edges) {
        int n = edges.size();
        vector<long long> score(n, 0);
        for (int i = 0; i < n; ++i) {
            score[edges[i]] += i;
        }
        long long maxScore = -1;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (score[i] > maxScore) {
                maxScore = score[i];
                ans = i;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int edgeScore(int[] edges) {
        int n = edges.length;
        long[] scores = new long[n];
        for (int i = 0; i < n; i++) {
            scores[edges[i]] += i;
        }
        int bestNode = 0;
        long maxScore = scores[0];
        for (int i = 1; i < n; i++) {
            if (scores[i] > maxScore) {
                maxScore = scores[i];
                bestNode = i;
            }
        }
        return bestNode;
    }
}
```

## Python

```python
class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        n = len(edges)
        scores = [0] * n
        for i, v in enumerate(edges):
            scores[v] += i
        max_score = -1
        answer = 0
        for idx, sc in enumerate(scores):
            if sc > max_score:
                max_score = sc
                answer = idx
        return answer
```

## Python3

```python
from typing import List

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0] * n
        for i, v in enumerate(edges):
            scores[v] += i
        max_score = -1
        ans = 0
        for i, s in enumerate(scores):
            if s > max_score:
                max_score = s
                ans = i
        return ans
```

## C

```c
#include <stdlib.h>

int edgeScore(int* edges, int edgesSize) {
    long long *score = (long long *)calloc(edgesSize, sizeof(long long));
    for (int i = 0; i < edgesSize; ++i) {
        int dest = edges[i];
        score[dest] += i;
    }
    long long maxScore = -1;
    int ans = 0;
    for (int i = 0; i < edgesSize; ++i) {
        if (score[i] > maxScore) {
            maxScore = score[i];
            ans = i;
        }
    }
    free(score);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int EdgeScore(int[] edges)
    {
        int n = edges.Length;
        long[] scores = new long[n];
        for (int i = 0; i < n; i++)
        {
            scores[edges[i]] += i;
        }

        long maxScore = -1;
        int result = 0;
        for (int i = 0; i < n; i++)
        {
            if (scores[i] > maxScore)
            {
                maxScore = scores[i];
                result = i;
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} edges
 * @return {number}
 */
var edgeScore = function(edges) {
    const n = edges.length;
    const scores = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        scores[edges[i]] += i;
    }
    let maxScore = -1;
    let answer = 0;
    for (let i = 0; i < n; i++) {
        if (scores[i] > maxScore) {
            maxScore = scores[i];
            answer = i;
        }
    }
    return answer;
};
```

## Typescript

```typescript
function edgeScore(edges: number[]): number {
    const n = edges.length;
    const scores = new Array<number>(n).fill(0);
    for (let i = 0; i < n; i++) {
        scores[edges[i]] += i;
    }
    let maxScore = -1;
    let answer = 0;
    for (let i = 0; i < n; i++) {
        if (scores[i] > maxScore) {
            maxScore = scores[i];
            answer = i;
        }
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $edges
     * @return Integer
     */
    function edgeScore($edges) {
        $n = count($edges);
        $score = array_fill(0, $n, 0);
        foreach ($edges as $i => $dest) {
            $score[$dest] += $i;
        }
        $maxScore = -1;
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($score[$i] > $maxScore) {
                $maxScore = $score[$i];
                $ans = $i;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func edgeScore(_ edges: [Int]) -> Int {
        let n = edges.count
        var scores = Array(repeating: 0, count: n)
        for i in 0..<n {
            let dest = edges[i]
            scores[dest] += i
        }
        var maxScore = -1
        var result = 0
        for i in 0..<n {
            if scores[i] > maxScore {
                maxScore = scores[i]
                result = i
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun edgeScore(edges: IntArray): Int {
        val n = edges.size
        val scores = LongArray(n)
        for (i in 0 until n) {
            scores[edges[i]] += i.toLong()
        }
        var maxIdx = 0
        var maxScore = scores[0]
        for (i in 1 until n) {
            if (scores[i] > maxScore) {
                maxScore = scores[i]
                maxIdx = i
            }
        }
        return maxIdx
    }
}
```

## Dart

```dart
class Solution {
  int edgeScore(List<int> edges) {
    final n = edges.length;
    final scores = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      scores[edges[i]] += i;
    }
    int maxScore = -1;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      if (scores[i] > maxScore) {
        maxScore = scores[i];
        ans = i;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func edgeScore(edges []int) int {
    n := len(edges)
    scores := make([]int64, n)
    for i, v := range edges {
        scores[v] += int64(i)
    }
    maxScore := scores[0]
    ans := 0
    for i := 1; i < n; i++ {
        if scores[i] > maxScore {
            maxScore = scores[i]
            ans = i
        }
    }
    return ans
}
```

## Ruby

```ruby
# @param {Integer[]} edges
# @return {Integer}
def edge_score(edges)
  n = edges.length
  scores = Array.new(n, 0)
  edges.each_with_index do |to, i|
    scores[to] += i
  end

  max_score = -1
  result_node = 0
  scores.each_with_index do |score, idx|
    if score > max_score
      max_score = score
      result_node = idx
    end
  end
  result_node
end
```

## Scala

```scala
object Solution {
    def edgeScore(edges: Array[Int]): Int = {
        val n = edges.length
        val scores = new Array[Long](n)
        var i = 0
        while (i < n) {
            val dest = edges(i)
            scores(dest) += i.toLong
            i += 1
        }
        var bestIdx = 0
        var bestScore = scores(0)
        var idx = 1
        while (idx < n) {
            if (scores(idx) > bestScore) {
                bestScore = scores(idx)
                bestIdx = idx
            }
            idx += 1
        }
        bestIdx
    }
}
```

## Rust

```rust
impl Solution {
    pub fn edge_score(edges: Vec<i32>) -> i32 {
        let n = edges.len();
        let mut scores = vec![0i64; n];
        for (i, &to) in edges.iter().enumerate() {
            scores[to as usize] += i as i64;
        }
        let mut best_idx = 0usize;
        let mut best_score = scores[0];
        for i in 1..n {
            if scores[i] > best_score {
                best_score = scores[i];
                best_idx = i;
            }
        }
        best_idx as i32
    }
}
```

## Racket

```racket
(define/contract (edge-score edges)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length edges))
         (edges-vec (list->vector edges))
         (scores (make-vector n 0)))
    ;; accumulate edge scores
    (for ([i (in-range n)])
      (let* ((t (vector-ref edges-vec i))
             (cur (vector-ref scores t)))
        (vector-set! scores t (+ cur i))))
    ;; find node with highest score, preferring smaller index on ties
    (let loop ((i 1) (best-index 0) (best-score (vector-ref scores 0)))
      (if (= i n)
          best-index
          (let ((s (vector-ref scores i)))
            (if (> s best-score)
                (loop (+ i 1) i s)
                (loop (+ i 1) best-index best-score)))))))
```

## Erlang

```erlang
-spec edge_score(Edges :: [integer()]) -> integer().
edge_score(Edges) ->
    N = length(Edges),
    Indexed = lists:zip(lists:seq(0, N - 1), Edges),
    ScoresMap = lists:foldl(
        fun({Idx, To}, Acc) ->
            maps:update_with(To,
                fun(V) -> V + Idx end,
                Idx,
                Acc)
        end,
        #{},
        Indexed),
    InitScore = maps:get(0, ScoresMap, 0),
    {BestNode, _} = lists:foldl(
        fun(I, {BestNodeAcc, BestScoreAcc}) ->
            Score = maps:get(I, ScoresMap, 0),
            if
                Score > BestScoreAcc -> {I, Score};
                Score == BestScoreAcc, I < BestNodeAcc -> {I, Score};
                true -> {BestNodeAcc, BestScoreAcc}
            end
        end,
        {0, InitScore},
        lists:seq(1, N - 1)),
    BestNode.
```

## Elixir

```elixir
defmodule Solution do
  @spec edge_score(edges :: [integer]) :: integer
  def edge_score(edges) do
    scores =
      Enum.with_index(edges)
      |> Enum.reduce(%{}, fn {to, from}, acc ->
        Map.update(acc, to, from, &(&1 + from))
      end)

    n = length(edges)

    {best_node, _} =
      0..(n - 1)
      |> Enum.reduce({0, Map.get(scores, 0, 0)}, fn i, {cur_node, cur_score} ->
        s = Map.get(scores, i, 0)

        cond do
          s > cur_score -> {i, s}
          s == cur_score and i < cur_node -> {i, s}
          true -> {cur_node, cur_score}
        end
      end)

    best_node
  end
end
```
