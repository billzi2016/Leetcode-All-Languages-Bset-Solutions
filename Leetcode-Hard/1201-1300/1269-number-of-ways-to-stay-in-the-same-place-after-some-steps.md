# 1269. Number of Ways to Stay in the Same Place After Some Steps

## Cpp

```cpp
class Solution {
public:
    int numWays(int steps, int arrLen) {
        const int MOD = 1000000007;
        int limit = std::min(arrLen - 1, steps);
        std::vector<int> prev(limit + 1, 0), cur(limit + 1, 0);
        prev[0] = 1;
        for (int s = 1; s <= steps; ++s) {
            int maxPos = std::min(s, limit);
            std::fill(cur.begin(), cur.end(), 0);
            for (int pos = 0; pos <= maxPos; ++pos) {
                long long ways = prev[pos];
                if (pos > 0) ways += prev[pos - 1];
                if (pos < limit) ways += prev[pos + 1];
                cur[pos] = ways % MOD;
            }
            std::swap(prev, cur);
        }
        return prev[0];
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int numWays(int steps, int arrLen) {
        // The farthest position we can reach is limited by both steps and array length
        int maxPos = Math.min(arrLen - 1, steps);
        int[] prev = new int[maxPos + 1];
        prev[0] = 1; // base case: 0 steps at position 0
        
        for (int step = 1; step <= steps; step++) {
            int[] cur = new int[maxPos + 1];
            for (int pos = 0; pos <= maxPos; pos++) {
                long ways = prev[pos]; // stay
                if (pos > 0) {
                    ways += prev[pos - 1]; // move from left
                }
                if (pos < maxPos) {
                    ways += prev[pos + 1]; // move from right
                }
                cur[pos] = (int)(ways % MOD);
            }
            prev = cur;
        }
        return prev[0];
    }
}
```

## Python

```python
class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        MOD = 10**9 + 7
        size = min(arrLen, steps + 1)  # positions we can actually reach
        prev = [0] * size
        prev[0] = 1

        for _ in range(1, steps + 1):
            cur = [0] * size
            for pos in range(size):
                val = prev[pos]
                if pos > 0:
                    val += prev[pos - 1]
                if pos + 1 < size:
                    val += prev[pos + 1]
                cur[pos] = val % MOD
            prev = cur

        return prev[0]
```

## Python3

```python
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        max_pos = min(steps, arrLen - 1)
        prev = [0] * (max_pos + 1)
        prev[0] = 1

        for _ in range(1, steps + 1):
            cur = [0] * (max_pos + 1)
            for pos in range(max_pos + 1):
                val = prev[pos]
                if pos > 0:
                    val += prev[pos - 1]
                if pos < max_pos:
                    val += prev[pos + 1]
                cur[pos] = val % MOD
            prev = cur

        return prev[0]
```

## C

```c
#include <stdlib.h>

int numWays(int steps, int arrLen) {
    const int MOD = 1000000007;
    int sz = (arrLen < steps + 1) ? arrLen : steps + 1;

    int *prev = (int *)calloc(sz, sizeof(int));
    int *cur  = (int *)calloc(sz, sizeof(int));
    if (!prev || !cur) return 0; // safety check

    prev[0] = 1;

    for (int s = 1; s <= steps; ++s) {
        for (int i = 0; i < sz; ++i) {
            long long sum = prev[i];
            if (i > 0)       sum += prev[i - 1];
            if (i + 1 < sz)  sum += prev[i + 1];
            cur[i] = (int)(sum % MOD);
        }
        int *tmp = prev;
        prev = cur;
        cur = tmp;
    }

    int result = prev[0];
    free(prev);
    free(cur);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1000000007;

    public int NumWays(int steps, int arrLen)
    {
        if (steps == 0) return 1;
        int maxPos = Math.Min(arrLen, steps);
        int[] prev = new int[maxPos];
        prev[0] = 1;

        for (int s = 1; s <= steps; s++)
        {
            int[] cur = new int[maxPos];
            // The farthest reachable position after s steps is at most s,
            // but maxPos already caps it, so we can iterate all.
            for (int pos = 0; pos < maxPos; pos++)
            {
                long ways = prev[pos];
                if (pos > 0) ways += prev[pos - 1];
                if (pos + 1 < maxPos) ways += prev[pos + 1];
                cur[pos] = (int)(ways % MOD);
            }
            prev = cur;
        }

        return prev[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} steps
 * @param {number} arrLen
 * @return {number}
 */
var numWays = function(steps, arrLen) {
    const MOD = 1000000007;
    // The farthest index we can reach is limited by both steps and array length.
    const maxPos = Math.min(arrLen - 1, steps);
    const size = maxPos + 1;

    let prev = new Array(size).fill(0);
    prev[0] = 1; // base case: 0 steps at position 0

    for (let s = 1; s <= steps; ++s) {
        const cur = new Array(size).fill(0);
        for (let i = 0; i < size; ++i) {
            let val = prev[i]; // stay
            if (i > 0) {
                val += prev[i - 1]; // move from left
            }
            if (i + 1 < size) {
                val += prev[i + 1]; // move from right
            }
            cur[i] = val % MOD;
        }
        prev = cur;
    }

    return prev[0];
};
```

## Typescript

```typescript
function numWays(steps: number, arrLen: number): number {
    const MOD = 1_000_000_007;
    // The farthest position we can reach is limited by steps and array length
    const maxPos = Math.min(arrLen - 1, steps);
    let prev = new Array(maxPos + 1).fill(0);
    prev[0] = 1;

    for (let s = 1; s <= steps; s++) {
        const cur = new Array(maxPos + 1).fill(0);
        for (let i = 0; i <= maxPos; i++) {
            let val = prev[i];
            if (i > 0) {
                val += prev[i - 1];
                if (val >= MOD) val -= MOD;
            }
            if (i < maxPos) {
                val += prev[i + 1];
                if (val >= MOD) val -= MOD;
            }
            cur[i] = val % MOD;
        }
        prev = cur;
    }

    return prev[0] % MOD;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $steps
     * @param Integer $arrLen
     * @return Integer
     */
    function numWays($steps, $arrLen) {
        $MOD = 1000000007;
        // Effective maximum position we need to consider
        $maxPos = min($arrLen - 1, $steps);
        $size = $maxPos + 1;

        // dp for remain = 0
        $prev = array_fill(0, $size, 0);
        $prev[0] = 1;

        for ($s = 1; $s <= $steps; $s++) {
            $curr = array_fill(0, $size, 0);
            for ($pos = 0; $pos < $size; $pos++) {
                $val = $prev[$pos];
                if ($pos > 0) {
                    $val += $prev[$pos - 1];
                }
                if ($pos + 1 < $size) {
                    $val += $prev[$pos + 1];
                }
                $curr[$pos] = $val % $MOD;
            }
            $prev = $curr;
        }

        return $prev[0] % $MOD;
    }
}
```

## Swift

```swift
class Solution {
    func numWays(_ steps: Int, _ arrLen: Int) -> Int {
        let MOD = 1_000_000_007
        let maxPos = min(steps, arrLen - 1)
        var prev = [Int](repeating: 0, count: maxPos + 1)
        prev[0] = 1
        
        if steps == 0 {
            return 1
        }
        
        for _ in 1...steps {
            var cur = [Int](repeating: 0, count: maxPos + 1)
            for pos in 0...maxPos {
                var ways = prev[pos]
                if pos > 0 {
                    ways += prev[pos - 1]
                }
                if pos < maxPos {
                    ways += prev[pos + 1]
                }
                if ways >= MOD {
                    ways %= MOD
                }
                cur[pos] = ways % MOD
            }
            prev = cur
        }
        
        return prev[0] % MOD
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numWays(steps: Int, arrLen: Int): Int {
        val MOD = 1_000_000_007L
        // The farthest position we can reach is limited by steps and array length.
        val maxPos = kotlin.math.min(arrLen - 1, steps)
        val size = maxPos + 1

        var prev = LongArray(size)
        prev[0] = 1L

        for (s in 1..steps) {
            val cur = LongArray(size)
            var pos = 0
            while (pos < size) {
                var ways = prev[pos]
                if (pos > 0) ways += prev[pos - 1]
                if (pos + 1 < size) ways += prev[pos + 1]
                cur[pos] = ways % MOD
                pos++
            }
            prev = cur
        }
        return (prev[0] % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int numWays(int steps, int arrLen) {
    int m = arrLen < steps ? arrLen : steps;
    List<int> prev = List.filled(m, 0);
    prev[0] = 1;

    for (int s = 1; s <= steps; ++s) {
      List<int> cur = List.filled(m, 0);
      for (int i = 0; i < m; ++i) {
        int val = prev[i];
        if (i > 0) {
          val += prev[i - 1];
          if (val >= _mod) val -= _mod;
        }
        if (i + 1 < m) {
          val += prev[i + 1];
          if (val >= _mod) val -= _mod;
        }
        cur[i] = val % _mod;
      }
      prev = cur;
    }

    return prev[0] % _mod;
  }
}
```

## Golang

```go
func numWays(steps int, arrLen int) int {
	const mod = 1000000007
	// The farthest position we need to consider is limited by steps and array length.
	maxPos := steps
	if arrLen-1 < maxPos {
		maxPos = arrLen - 1
	}
	// Further limit: you cannot be farther than steps/2 from start and still return.
	if steps/2 < maxPos {
		maxPos = steps / 2
	}
	size := maxPos + 1

	prev := make([]int, size)
	prev[0] = 1

	for s := 1; s <= steps; s++ {
		cur := make([]int, size)
		for pos := 0; pos < size; pos++ {
			sum := int64(prev[pos])
			if pos > 0 {
				sum += int64(prev[pos-1])
			}
			if pos+1 < size {
				sum += int64(prev[pos+1])
			}
			cur[pos] = int(sum % mod)
		}
		prev = cur
	}
	return prev[0]
}
```

## Ruby

```ruby
def num_ways(steps, arr_len)
  mod = 1_000_000_007
  max_pos = [arr_len, steps].min
  prev = Array.new(max_pos, 0)
  prev[0] = 1
  cur = Array.new(max_pos, 0)

  (1..steps).each do |_|
    i = 0
    while i < max_pos
      cur[i] = 0
      i += 1
    end

    i = 0
    while i < max_pos
      val = prev[i]
      val += prev[i - 1] if i > 0
      val += prev[i + 1] if i + 1 < max_pos
      cur[i] = val % mod
      i += 1
    end

    prev, cur = cur, prev
  end

  prev[0] % mod
end
```

## Scala

```scala
object Solution {
    def numWays(steps: Int, arrLen: Int): Int = {
        val MOD = 1000000007L
        val m = Math.min(arrLen, steps)
        var prev = new Array[Long](m)
        prev(0) = 1L
        for (_ <- 1 to steps) {
            val cur = new Array[Long](m)
            var pos = 0
            while (pos < m) {
                var ans = prev(pos)
                if (pos > 0) ans = (ans + prev(pos - 1)) % MOD
                if (pos + 1 < m) ans = (ans + prev(pos + 1)) % MOD
                cur(pos) = ans
                pos += 1
            }
            prev = cur
        }
        (prev(0) % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_ways(steps: i32, arr_len: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let steps_usize = steps as usize;
        // maximum reachable index is min(arr_len - 1, steps)
        let max_pos = std::cmp::min((arr_len as usize).saturating_sub(1), steps_usize);
        let size = max_pos + 1;

        let mut prev = vec![0i64; size];
        prev[0] = 1;

        for _ in 1..=steps_usize {
            let mut cur = vec![0i64; size];
            for pos in 0..size {
                let mut val = prev[pos];
                if pos > 0 {
                    val += prev[pos - 1];
                }
                if pos + 1 < size {
                    val += prev[pos + 1];
                }
                cur[pos] = val % MOD;
            }
            prev = cur;
        }

        prev[0] as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (num-ways steps arrLen)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ([m (min arrLen (+ steps 1))]
         [prev (make-vector m 0)])
    (vector-set! prev 0 1)
    (for ([s (in-range 1 (add1 steps))])
      (let ([cur (make-vector m 0)])
        (for ([i (in-range m)])
          (define left (if (> i 0) (vector-ref prev (- i 1)) 0))
          (define right (if (< i (sub1 m)) (vector-ref prev (+ i 1)) 0))
          (define val (modulo (+ (vector-ref prev i) left right) MOD))
          (vector-set! cur i val))
        (set! prev cur)))
    (vector-ref prev 0)))
```

## Erlang

```erlang
-module(solution).
-export([num_ways/2]).

-define(MOD, 1000000007).

-spec num_ways(Steps :: integer(), ArrLen :: integer()) -> integer().
num_ways(0, _ArrLen) ->
    1;
num_ways(Steps, ArrLen) ->
    Len = erlang:min(ArrLen, Steps),
    Prev = list_to_tuple([1 | lists:duplicate(Len-1, 0)]),
    Final = loop(Steps, Prev, Len),
    element(1, Final).

loop(0, Prev, _Len) -> Prev;
loop(Step, Prev, Len) ->
    CurrList = [calc(I, Prev, Len) || I <- lists:seq(0, Len-1)],
    Curr = list_to_tuple(CurrList),
    loop(Step - 1, Curr, Len).

calc(Index, Prev, Len) ->
    Val = element(Index + 1, Prev),
    Left = if Index > 0 -> element(Index, Prev); true -> 0 end,
    Right = if Index < Len - 1 -> element(Index + 2, Prev); true -> 0 end,
    (Val + Left + Right) rem ?MOD.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_ways(steps :: integer, arr_len :: integer) :: integer
  def num_ways(steps, arr_len) do
    mod = 1_000_000_007
    limit = min(arr_len - 1, steps)
    size = limit + 1

    prev =
      List.duplicate(0, size)
      |> List.to_tuple()
      |> put_elem(0, 1)

    dp =
      Enum.reduce(1..steps, prev, fn _step, prev_dp ->
        0..limit
        |> Enum.map(fn i ->
          cur = elem(prev_dp, i)
          left = if i > 0, do: elem(prev_dp, i - 1), else: 0
          right = if i < limit, do: elem(prev_dp, i + 1), else: 0
          rem(cur + left + right, mod)
        end)
        |> List.to_tuple()
      end)

    elem(dp, 0)
  end
end
```
