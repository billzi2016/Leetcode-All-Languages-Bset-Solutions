# 0997. Find the Town Judge

## Cpp

```cpp
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> score(n + 1, 0);
        for (const auto& t : trust) {
            int a = t[0], b = t[1];
            --score[a];   // trusts someone
            ++score[b];   // is trusted by someone
        }
        for (int i = 1; i <= n; ++i) {
            if (score[i] == n - 1) return i;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int findJudge(int n, int[][] trust) {
        if (n == 1 && trust.length == 0) {
            return 1;
        }
        int[] score = new int[n + 1];
        for (int[] t : trust) {
            int a = t[0], b = t[1];
            score[a]--; // a trusts someone, cannot be judge
            score[b]++; // b is trusted by someone
        }
        for (int i = 1; i <= n; i++) {
            if (score[i] == n - 1) {
                return i;
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1:
            return 1 if not trust else -1

        score = [0] * (n + 1)  # index from 1 to n

        for a, b in trust:
            score[a] -= 1   # trusts someone -> cannot be judge
            score[b] += 1   # trusted by someone

        for i in range(1, n + 1):
            if score[i] == n - 1:
                return i
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        score = [0] * (n + 1)
        for a, b in trust:
            score[a] -= 1
            score[b] += 1
        for i in range(1, n + 1):
            if score[i] == n - 1:
                return i
        return -1
```

## C

```c
#include <stdlib.h>

int findJudge(int n, int** trust, int trustSize, int* trustColSize) {
    if (n == 1 && trustSize == 0) return 1;
    int *in = calloc(n + 1, sizeof(int));
    int *out = calloc(n + 1, sizeof(int));
    for (int i = 0; i < trustSize; ++i) {
        int a = trust[i][0];
        int b = trust[i][1];
        out[a]++;
        in[b]++;
    }
    for (int i = 1; i <= n; ++i) {
        if (out[i] == 0 && in[i] == n - 1) {
            free(in);
            free(out);
            return i;
        }
    }
    free(in);
    free(out);
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int FindJudge(int n, int[][] trust) {
        if (n == 1 && (trust == null || trust.Length == 0)) return 1;
        int[] indegree = new int[n + 1];
        int[] outdegree = new int[n + 1];

        foreach (var t in trust) {
            int a = t[0];
            int b = t[1];
            outdegree[a]++;
            indegree[b]++;
        }

        for (int i = 1; i <= n; i++) {
            if (outdegree[i] == 0 && indegree[i] == n - 1) {
                return i;
            }
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
    if (n === 1 && trust.length === 0) return 1;
    
    const indegree = new Array(n + 1).fill(0);
    const outdegree = new Array(n + 1).fill(0);
    
    for (const [a, b] of trust) {
        outdegree[a]++;
        indegree[b]++;
    }
    
    for (let i = 1; i <= n; i++) {
        if (indegree[i] === n - 1 && outdegree[i] === 0) {
            return i;
        }
    }
    return -1;
};
```

## Typescript

```typescript
function findJudge(n: number, trust: number[][]): number {
    if (n === 1) return 1;
    const score = new Array(n + 1).fill(0);
    for (const [a, b] of trust) {
        score[a]--;
        score[b]++;
    }
    for (let i = 1; i <= n; i++) {
        if (score[i] === n - 1) return i;
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $trust
     * @return Integer
     */
    function findJudge($n, $trust) {
        if ($n == 1 && count($trust) == 0) {
            return 1;
        }
        $score = array_fill(0, $n + 1, 0);
        foreach ($trust as $pair) {
            $a = $pair[0];
            $b = $pair[1];
            $score[$a]--;
            $score[$b]++;
        }
        for ($i = 1; $i <= $n; $i++) {
            if ($score[$i] == $n - 1) {
                return $i;
            }
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func findJudge(_ n: Int, _ trust: [[Int]]) -> Int {
        if n == 1 {
            return trust.isEmpty ? 1 : -1
        }
        var score = Array(repeating: 0, count: n + 1)
        for pair in trust {
            let a = pair[0]
            let b = pair[1]
            score[a] -= 1
            score[b] += 1
        }
        for i in 1...n {
            if score[i] == n - 1 {
                return i
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findJudge(n: Int, trust: Array<IntArray>): Int {
        if (n == 1 && trust.isEmpty()) return 1
        val score = IntArray(n + 1)
        for (pair in trust) {
            val a = pair[0]
            val b = pair[1]
            score[a]--   // a trusts someone, cannot be judge
            score[b]++   // b is trusted by someone
        }
        for (i in 1..n) {
            if (score[i] == n - 1) return i
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int findJudge(int n, List<List<int>> trust) {
    if (n == 1 && trust.isEmpty) return 1;
    List<int> score = List.filled(n + 1, 0);
    for (var t in trust) {
      int a = t[0];
      int b = t[1];
      score[a]--;
      score[b]++;
    }
    for (int i = 1; i <= n; i++) {
      if (score[i] == n - 1) return i;
    }
    return -1;
  }
}
```

## Golang

```go
func findJudge(n int, trust [][]int) int {
    if n == 1 && len(trust) == 0 {
        return 1
    }
    indegree := make([]int, n+1)
    outdegree := make([]int, n+1)

    for _, t := range trust {
        a, b := t[0], t[1]
        outdegree[a]++
        indegree[b]++
    }

    for i := 1; i <= n; i++ {
        if outdegree[i] == 0 && indegree[i] == n-1 {
            return i
        }
    }
    return -1
}
```

## Ruby

```ruby
def find_judge(n, trust)
  indegree = Array.new(n + 1, 0)
  outdegree = Array.new(n + 1, 0)

  trust.each do |a, b|
    outdegree[a] += 1
    indegree[b] += 1
  end

  (1..n).each do |person|
    return person if indegree[person] == n - 1 && outdegree[person].zero?
  end
  -1
end
```

## Scala

```scala
object Solution {
    def findJudge(n: Int, trust: Array[Array[Int]]): Int = {
        if (n == 1 && trust.isEmpty) return 1
        val score = new Array[Int](n + 1)
        for (pair <- trust) {
            val a = pair(0)
            val b = pair(1)
            score(a) -= 1
            score(b) += 1
        }
        for (i <- 1 to n) {
            if (score(i) == n - 1) return i
        }
        -1
    }
}
```

## Rust

```rust
struct Solution;

impl Solution {
    pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
        if n == 1 && trust.is_empty() {
            return 1;
        }
        let mut score = vec![0i32; (n as usize) + 1];
        for t in &trust {
            let a = t[0] as usize;
            let b = t[1] as usize;
            score[a] -= 1;
            score[b] += 1;
        }
        for i in 1..=n as usize {
            if score[i] == n - 1 {
                return i as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (find-judge n trust)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((indeg (make-vector (+ n 1) 0))
         (outdeg (make-vector (+ n 1) 0)))
    (for ([pair trust])
      (define a (first pair))
      (define b (second pair))
      (vector-set! outdeg a (add1 (vector-ref outdeg a)))
      (vector-set! indeg b (add1 (vector-ref indeg b))))
    (let loop ((i 1))
      (cond
        [(> i n) -1]
        [(and (= (vector-ref indeg i) (- n 1))
              (= (vector-ref outdeg i) 0))
         i]
        [else (loop (add1 i))]))))
```

## Erlang

```erlang
-spec find_judge(N :: integer(), Trust :: [[integer()]]) -> integer().
find_judge(N, Trust) ->
    {Indeg, Outdeg} = lists:foldl(fun([A,B], {I,O}) ->
        O1 = maps:update_with(A, fun(V) -> V + 1 end, 1, O),
        I1 = maps:update_with(B, fun(V) -> V + 1 end, 1, I),
        {I1, O1}
    end, {#{}, #{}}, Trust),
    find_judge_loop(1, N, Indeg, Outdeg).

find_judge_loop(I, N, _Indeg, _Outdeg) when I > N ->
    -1;
find_judge_loop(I, N, Indeg, Outdeg) ->
    InCount = maps:get(I, Indeg, 0),
    OutCount = maps:get(I, Outdeg, 0),
    case {InCount == N-1, OutCount == 0} of
        {true, true} -> I;
        _ -> find_judge_loop(I + 1, N, Indeg, Outdeg)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_judge(n :: integer, trust :: [[integer]]) :: integer
  def find_judge(n, trust) do
    scores =
      Enum.reduce(trust, %{}, fn [a, b], acc ->
        acc
        |> Map.update(a, -1, &(&1 - 1))
        |> Map.update(b, 1, &(&1 + 1))
      end)

    case Enum.find(1..n, fn i -> Map.get(scores, i, 0) == n - 1 end) do
      nil -> -1
      judge -> judge
    end
  end
end
```
