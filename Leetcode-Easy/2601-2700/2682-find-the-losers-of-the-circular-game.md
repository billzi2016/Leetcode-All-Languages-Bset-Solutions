# 2682. Find the Losers of the Circular Game

## Cpp

```cpp
class Solution {
public:
    vector<int> circularGameLosers(int n, int k) {
        vector<bool> visited(n, false);
        int cur = 0;
        visited[cur] = true;
        for (int turn = 1; ; ++turn) {
            int nxt = (cur + turn * k) % n;
            if (visited[nxt]) break;
            visited[nxt] = true;
            cur = nxt;
        }
        vector<int> losers;
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) losers.push_back(i + 1);
        }
        return losers;
    }
};
```

## Java

```java
class Solution {
    public int[] circularGameLosers(int n, int k) {
        boolean[] visited = new boolean[n + 1];
        int current = 1;
        visited[current] = true;
        int step = 1;
        while (true) {
            int next = ((current - 1 + step * k) % n) + 1;
            if (visited[next]) {
                break;
            }
            visited[next] = true;
            current = next;
            step++;
        }
        java.util.List<Integer> losers = new java.util.ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (!visited[i]) {
                losers.add(i);
            }
        }
        int[] result = new int[losers.size()];
        for (int i = 0; i < losers.size(); i++) {
            result[i] = losers.get(i);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def circularGameLosers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        visited = [False] * (n + 1)
        curr = 1
        visited[curr] = True
        i = 1
        while True:
            nxt = ((curr - 1) + i * k) % n + 1
            if visited[nxt]:
                break
            visited[nxt] = True
            curr = nxt
            i += 1
        return [idx for idx in range(1, n + 1) if not visited[idx]]
```

## Python3

```python
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        visited = [False] * n
        pos = 0
        visited[pos] = True
        i = 1
        while True:
            nxt = (pos + i * k) % n
            if visited[nxt]:
                break
            visited[nxt] = True
            pos = nxt
            i += 1
        return [idx + 1 for idx, v in enumerate(visited) if not v]
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* circularGameLosers(int n, int k, int* returnSize) {
    bool visited[51] = {false};
    int cur = 0;
    visited[cur] = true;

    for (int turn = 1; ; ++turn) {
        int nxt = (cur + turn * k) % n;
        if (visited[nxt]) break;
        visited[nxt] = true;
        cur = nxt;
    }

    int cnt = 0;
    for (int i = 0; i < n; ++i)
        if (!visited[i]) ++cnt;

    int* res = (int*)malloc(cnt * sizeof(int));
    int idx = 0;
    for (int i = 0; i < n; ++i) {
        if (!visited[i])
            res[idx++] = i + 1;
    }

    *returnSize = cnt;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] CircularGameLosers(int n, int k) {
        bool[] seen = new bool[n + 1];
        seen[1] = true;
        int current = 1;
        for (int i = 1; ; i++) {
            int next = ((current - 1 + i * k) % n) + 1;
            if (seen[next]) break;
            seen[next] = true;
            current = next;
        }
        var losers = new System.Collections.Generic.List<int>();
        for (int i = 1; i <= n; i++) {
            if (!seen[i]) losers.Add(i);
        }
        return losers.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
var circularGameLosers = function(n, k) {
    const visited = new Array(n).fill(false);
    let cur = 0; // friend 1 (0-indexed)
    visited[cur] = true;
    let turn = 1;
    while (true) {
        const step = turn * k;
        cur = (cur + step) % n;
        if (visited[cur]) break;
        visited[cur] = true;
        turn++;
    }
    const losers = [];
    for (let i = 0; i < n; i++) {
        if (!visited[i]) losers.push(i + 1);
    }
    return losers;
};
```

## Typescript

```typescript
function circularGameLosers(n: number, k: number): number[] {
    const visited = new Array<boolean>(n).fill(false);
    let current = 0; // zero-based index for friend 1
    visited[current] = true;
    let turn = 1;
    while (true) {
        const next = (current + turn * k) % n;
        if (visited[next]) break;
        visited[next] = true;
        current = next;
        turn++;
    }
    const losers: number[] = [];
    for (let i = 0; i < n; i++) {
        if (!visited[i]) losers.push(i + 1);
    }
    return losers;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer[]
     */
    function circularGameLosers($n, $k) {
        $visited = array_fill(0, $n + 1, false);
        $current = 1;
        $visited[$current] = true;
        $turn = 1;
        while (true) {
            $next = ($current - 1 + $turn * $k) % $n + 1;
            if ($visited[$next]) {
                break;
            }
            $visited[$next] = true;
            $current = $next;
            $turn++;
        }
        $losers = [];
        for ($i = 1; $i <= $n; $i++) {
            if (!$visited[$i]) {
                $losers[] = $i;
            }
        }
        return $losers;
    }
}
```

## Swift

```swift
class Solution {
    func circularGameLosers(_ n: Int, _ k: Int) -> [Int] {
        var visited = Array(repeating: false, count: n + 1)
        visited[1] = true
        var current = 1
        var turn = 1
        
        while true {
            let next = ((current - 1 + turn * k) % n) + 1
            if visited[next] {
                break
            }
            visited[next] = true
            current = next
            turn += 1
        }
        
        var losers: [Int] = []
        for i in 1...n {
            if !visited[i] {
                losers.append(i)
            }
        }
        return losers
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun circularGameLosers(n: Int, k: Int): IntArray {
        val visited = BooleanArray(n + 1)
        var current = 1
        visited[current] = true
        var step = 1
        while (true) {
            val next = ((current - 1 + step * k) % n) + 1
            if (visited[next]) break
            visited[next] = true
            current = next
            step++
        }
        val losers = mutableListOf<Int>()
        for (i in 1..n) {
            if (!visited[i]) losers.add(i)
        }
        return losers.toIntArray()
    }
}
```

## Dart

```dart
class Solution {
  List<int> circularGameLosers(int n, int k) {
    List<bool> visited = List.filled(n + 1, false);
    int current = 1;
    visited[current] = true;
    for (int i = 1;; i++) {
      int next = ((current - 1 + i * k) % n) + 1;
      if (visited[next]) break;
      visited[next] = true;
      current = next;
    }
    List<int> losers = [];
    for (int i = 1; i <= n; i++) {
      if (!visited[i]) losers.add(i);
    }
    return losers;
  }
}
```

## Golang

```go
func circularGameLosers(n int, k int) []int {
	visited := make([]bool, n+1)
	cur := 1
	visited[cur] = true
	step := 1
	for {
		next := ((cur-1 + step*k) % n) + 1
		if visited[next] {
			break
		}
		visited[next] = true
		cur = next
		step++
	}
	res := []int{}
	for i := 1; i <= n; i++ {
		if !visited[i] {
			res = append(res, i)
		}
	}
	return res
}
```

## Ruby

```ruby
def circular_game_losers(n, k)
  visited = Array.new(n + 1, false)
  current = 1
  visited[current] = true
  i = 1
  loop do
    nxt = ((current - 1 + i * k) % n) + 1
    break if visited[nxt]
    visited[nxt] = true
    current = nxt
    i += 1
  end
  result = []
  (1..n).each { |idx| result << idx unless visited[idx] }
  result
end
```

## Scala

```scala
object Solution {
    def circularGameLosers(n: Int, k: Int): Array[Int] = {
        val visited = new Array[Boolean](n)
        var cur = 0
        visited(cur) = true
        var turn = 1
        while (true) {
            val next = (cur + turn * k) % n
            if (visited(next)) {
                return (for (i <- 0 until n if !visited(i)) yield i + 1).toArray
            }
            visited(next) = true
            cur = next
            turn += 1
        }
        Array.empty[Int]
    }
}
```

## Rust

```rust
impl Solution {
    pub fn circular_game_losers(n: i32, k: i32) -> Vec<i32> {
        let n_usize = n as usize;
        let mut visited = vec![false; n_usize + 1];
        let mut current = 1i32;
        visited[current as usize] = true;
        let mut turn = 1i32;

        loop {
            let next = ((current - 1 + turn * k) % n + 1) as i32;
            if visited[next as usize] {
                break;
            }
            visited[next as usize] = true;
            current = next;
            turn += 1;
        }

        let mut losers = Vec::new();
        for i in 1..=n {
            if !visited[i as usize] {
                losers.push(i);
            }
        }
        losers
    }
}
```

## Racket

```racket
(require racket/base)

(define/contract (circular-game-losers n k)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  (let ((visited (make-vector (+ n 1) #f)))
    (vector-set! visited 1 #t)
    (let loop ((current 1) (i 1))
      (define next
        (+ 1 (modulo (+ (- current 1) (* i k)) n)))
      (if (vector-ref visited next)
          (for/list ([idx (in-range 1 (add1 n))]
                     #:when (not (vector-ref visited idx)))
            idx)
          (begin
            (vector-set! visited next #t)
            (loop next (+ i 1)))))))
```

## Erlang

```erlang
-spec circular_game_losers(N :: integer(), K :: integer()) -> [integer()].
circular_game_losers(N, K) ->
    Visited0 = maps:put(1, true, #{}),
    Visited = simulate(N, K, 1, 1, Visited0),
    [X || X <- lists:seq(1, N), not maps:is_key(X, Visited)].

simulate(N, K, Pos, Turn, Visited) ->
    Next = ((Pos - 1 + Turn * K) rem N) + 1,
    case maps:is_key(Next, Visited) of
        true -> Visited;
        false ->
            NewVisited = maps:put(Next, true, Visited),
            simulate(N, K, Next, Turn + 1, NewVisited)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec circular_game_losers(n :: integer, k :: integer) :: [integer]
  def circular_game_losers(n, k) do
    visited = simulate(n, k, 1, 1, MapSet.new([1]))
    for i <- 1..n, not MapSet.member?(visited, i), do: i
  end

  defp simulate(n, k, current, i, visited) do
    next = rem(current - 1 + i * k, n) + 1

    if MapSet.member?(visited, next) do
      visited
    else
      simulate(n, k, next, i + 1, MapSet.put(visited, next))
    end
  end
end
```
