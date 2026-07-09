# 0887. Super Egg Drop

## Cpp

```cpp
class Solution {
public:
    int superEggDrop(int k, int n) {
        vector<long long> dp(k + 1, 0);
        int m = 0;
        while (dp[k] < n) {
            ++m;
            for (int i = k; i >= 1; --i) {
                dp[i] = dp[i] + dp[i - 1] + 1;
            }
        }
        return m;
    }
};
```

## Java

```java
class Solution {
    public int superEggDrop(int k, int n) {
        long[] dp = new long[k + 1];
        int moves = 0;
        while (dp[k] < n) {
            moves++;
            for (int i = k; i >= 1; --i) {
                dp[i] = dp[i] + dp[i - 1] + 1;
            }
        }
        return moves;
    }
}
```

## Python

```python
class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        # dp[i] = maximum number of floors that can be checked with i eggs and m moves
        dp = [0] * (k + 1)
        moves = 0
        while dp[k] < n:
            moves += 1
            for i in range(k, 0, -1):
                dp[i] = dp[i] + dp[i - 1] + 1
        return moves
```

## Python3

```python
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp[i] = maximum number of floors that can be checked with i eggs
        dp = [0] * (k + 1)
        moves = 0
        while dp[k] < n:
            moves += 1
            for i in range(k, 0, -1):
                dp[i] = dp[i] + dp[i - 1] + 1
        return moves
```

## C

```c
#include <stdlib.h>

int superEggDrop(int k, int n) {
    long long *dp = (long long *)calloc(k + 1, sizeof(long long));
    int moves = 0;
    while (dp[k] < n) {
        ++moves;
        for (int e = k; e >= 1; --e) {
            dp[e] = dp[e] + dp[e - 1] + 1;
        }
    }
    free(dp);
    return moves;
}
```

## Csharp

```csharp
public class Solution
{
    public int SuperEggDrop(int k, int n)
    {
        // dp[e] = maximum number of floors that can be checked with current number of moves and e eggs
        int[] dp = new int[k + 1];
        int moves = 0;
        while (dp[k] < n)
        {
            moves++;
            for (int e = k; e >= 1; e--)
            {
                dp[e] = dp[e] + dp[e - 1] + 1;
            }
        }
        return moves;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} k
 * @param {number} n
 * @return {number}
 */
var superEggDrop = function(k, n) {
    const dp = new Array(k + 1).fill(0);
    let moves = 0;
    while (dp[k] < n) {
        moves++;
        for (let i = k; i >= 1; i--) {
            dp[i] = dp[i] + dp[i - 1] + 1;
        }
    }
    return moves;
};
```

## Typescript

```typescript
function superEggDrop(k: number, n: number): number {
    const dp = new Array(k + 1).fill(0);
    let moves = 0;
    while (dp[k] < n) {
        moves++;
        for (let i = k; i >= 1; i--) {
            dp[i] = dp[i] + dp[i - 1] + 1;
        }
    }
    return moves;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer $n
     * @return Integer
     */
    function superEggDrop($k, $n) {
        // dp[i] = maximum floors that can be checked with current number of moves using i eggs
        $dp = array_fill(0, $k + 1, 0);
        $moves = 0;
        while ($dp[$k] < $n) {
            $moves++;
            for ($i = $k; $i >= 1; $i--) {
                // recurrence: dp[m][i] = dp[m-1][i-1] + dp[m-1][i] + 1
                $dp[$i] = $dp[$i] + $dp[$i - 1] + 1;
            }
        }
        return $moves;
    }
}
```

## Swift

```swift
class Solution {
    func superEggDrop(_ k: Int, _ n: Int) -> Int {
        if n == 0 { return 0 }
        var dp = Array(repeating: 0, count: k + 1)
        var moves = 0
        while dp[k] < n {
            moves += 1
            for i in stride(from: k, through: 1, by: -1) {
                dp[i] = dp[i] + dp[i - 1] + 1
            }
        }
        return moves
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun superEggDrop(k: Int, n: Int): Int {
        if (n == 0) return 0
        val dp = LongArray(k + 1)
        var moves = 0
        while (dp[k] < n) {
            moves++
            for (e in k downTo 1) {
                dp[e] = dp[e] + dp[e - 1] + 1
            }
        }
        return moves
    }
}
```

## Dart

```dart
class Solution {
  int superEggDrop(int k, int n) {
    List<int> dp = List.filled(k + 1, 0);
    int moves = 0;
    while (dp[k] < n) {
      moves++;
      for (int i = k; i >= 1; --i) {
        dp[i] = dp[i] + dp[i - 1] + 1;
      }
    }
    return moves;
  }
}
```

## Golang

```go
func superEggDrop(k int, n int) int {
	if n == 0 {
		return 0
	}
	dp := make([]int, k+1)
	moves := 0
	for dp[k] < n {
		moves++
		for i := k; i >= 1; i-- {
			dp[i] = dp[i] + dp[i-1] + 1
		}
	}
	return moves
}
```

## Ruby

```ruby
def super_egg_drop(k, n)
  return n if k == 1
  dp = Array.new(k + 1, 0)
  moves = 0
  while dp[k] < n
    moves += 1
    k.downto(1) do |i|
      dp[i] = dp[i] + dp[i - 1] + 1
    end
  end
  moves
end
```

## Scala

```scala
object Solution {
    def superEggDrop(k: Int, n: Int): Int = {
        if (n == 0) return 0
        val dp = new Array[Long](k + 1)
        var moves = 0
        while (dp(k) < n) {
            moves += 1
            var i = k
            while (i >= 1) {
                dp(i) = dp(i) + dp(i - 1) + 1
                i -= 1
            }
        }
        moves
    }
}
```

## Rust

```rust
impl Solution {
    pub fn super_egg_drop(k: i32, n: i32) -> i32 {
        let k = k as usize;
        let target = n as i64;
        if target == 0 {
            return 0;
        }
        let mut dp = vec![0i64; k + 1];
        let mut moves = 0;
        while dp[k] < target {
            moves += 1;
            for e in (1..=k).rev() {
                dp[e] = dp[e] + dp[e - 1] + 1;
            }
        }
        moves as i32
    }
}
```

## Racket

```racket
(define/contract (super-egg-drop k n)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ([k (max 0 k)]
         [n (max 0 n)])
    (if (= n 0)
        0
        (let loop ((moves 0) (dp (make-vector (+ k 1) 0)))
          (let ((next (make-vector (+ k 1) 0)))
            (for ([egg (in-range 1 (+ k 1))])
              (vector-set! next egg
                (+ 1 (vector-ref dp (- egg 1))
                     (vector-ref dp egg))))
            (if (>= (vector-ref next k) n)
                (+ moves 1)
                (loop (+ moves 1) next)))))))
```

## Erlang

```erlang
-module(solution).
-export([super_egg_drop/2]).

-spec super_egg_drop(K :: integer(), N :: integer()) -> integer().
super_egg_drop(K, N) when K >= 0, N >= 0 ->
    if
        N =:= 0 -> 0;
        true ->
            Init = lists:duplicate(K + 1, 0),
            loop(K, N, 0, Init)
    end.

loop(K, N, Moves, Prev) ->
    case lists:nth(K + 1, Prev) >= N of
        true -> Moves;
        false ->
            New = new_dp(Prev, K),
            loop(K, N, Moves + 1, New)
    end.

new_dp(Prev, K) ->
    Rev = new_dp_rev(1, K, Prev, []),
    [0 | lists:reverse(Rev)].

new_dp_rev(I, K, _Prev, Acc) when I > K -> Acc;
new_dp_rev(I, K, Prev, Acc) ->
    PrevKMinus1 = lists:nth(I, Prev),
    PrevK = lists:nth(I + 1, Prev),
    NewVal = PrevKMinus1 + PrevK + 1,
    new_dp_rev(I + 1, K, Prev, [NewVal | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec super_egg_drop(k :: integer, n :: integer) :: integer
  def super_egg_drop(_k, n) when n <= 0, do: 0

  def super_egg_drop(k, n) do
    prev = :array.new(k + 1, default: 0)
    loop(1, prev, k, n)
  end

  defp loop(moves, prev, k, n) do
    cur = compute_cur(prev, k)

    if :array.get(k, cur) >= n do
      moves
    else
      loop(moves + 1, cur, k, n)
    end
  end

  defp compute_cur(prev, k) do
    cur = :array.new(k + 1, default: 0)

    Enum.reduce(1..k, cur, fn i, acc ->
      val = :array.get(i - 1, prev) + :array.get(i, prev) + 1
      :array.set(i, val, acc)
    end)
  end
end
```
