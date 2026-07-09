# 1997. First Day Where You Have Been in All the Rooms

## Cpp

```cpp
class Solution {
public:
    int firstDayBeenInAllRooms(vector<int>& nextVisit) {
        const long long MOD = 1000000007LL;
        int n = nextVisit.size();
        vector<long long> dp(n);
        dp[0] = 0;
        for (int i = 1; i < n; ++i) {
            long long val = (2 * dp[i - 1]) % MOD;
            val = (val - dp[nextVisit[i - 1]] + MOD) % MOD;
            val = (val + 2) % MOD;
            dp[i] = val;
        }
        return (int)dp[n - 1];
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int firstDayBeenInAllRooms(int[] nextVisit) {
        int n = nextVisit.length;
        long[] dp = new long[n];
        dp[0] = 0; // day when room 0 is first visited
        
        for (int i = 1; i < n; i++) {
            long val = (2L * dp[i - 1]) % MOD;
            val = (val - dp[nextVisit[i - 1]] + MOD) % MOD;
            val = (val + 2) % MOD;
            dp[i] = val;
        }
        return (int) dp[n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def firstDayBeenInAllRooms(self, nextVisit):
        """
        :type nextVisit: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nextVisit)
        dp = [0] * n
        # dp[0] is day 0 (already in room 0)
        for i in range(1, n):
            # recurrence: dp[i] = (2*dp[i-1] - dp[nextVisit[i-1]] + 2) mod MOD
            val = (2 * dp[i - 1]) % MOD
            val = (val - dp[nextVisit[i - 1]]) % MOD
            dp[i] = (val + 2) % MOD
        return dp[-1]
```

## Python3

```python
from typing import List

class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nextVisit)
        dp = [0] * n
        for i in range(1, n):
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % MOD
        return dp[-1]
```

## C

```c
#include <stdlib.h>

int firstDayBeenInAllRooms(int* nextVisit, int nextVisitSize) {
    const long long MOD = 1000000007LL;
    long long *dp = (long long *)malloc(sizeof(long long) * nextVisitSize);
    if (!dp) return 0;
    dp[0] = 0; // day when room 0 is first visited
    for (int i = 1; i < nextVisitSize; ++i) {
        long long twoPrev = (2LL * dp[i - 1]) % MOD;
        long long sub = dp[nextVisit[i - 1]];
        long long cur = (twoPrev - sub + MOD) % MOD; // ensure non‑negative
        cur = (cur + 2) % MOD;                       // add the two extra days
        dp[i] = cur;
    }
    int ans = (int)(dp[nextVisitSize - 1] % MOD);
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int FirstDayBeenInAllRooms(int[] nextVisit) {
        const long MOD = 1000000007L;
        int n = nextVisit.Length;
        long[] dp = new long[n];
        dp[0] = 0;
        for (int i = 1; i < n; i++) {
            int j = nextVisit[i - 1];
            long val = (2 * dp[i - 1]) % MOD;
            val = (val - dp[j] + MOD) % MOD;
            val = (val + 2) % MOD;
            dp[i] = val;
        }
        return (int)(dp[n - 1] % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nextVisit
 * @return {number}
 */
var firstDayBeenInAllRooms = function(nextVisit) {
    const MOD = 1000000007;
    const n = nextVisit.length;
    const dp = new Array(n);
    dp[0] = 0;
    for (let i = 0; i < n - 1; i++) {
        const j = nextVisit[i];
        let val = ( (2 * dp[i]) % MOD - dp[j] + MOD ) % MOD;
        val = (val + 2) % MOD;
        dp[i + 1] = val;
    }
    return dp[n - 1];
};
```

## Typescript

```typescript
function firstDayBeenInAllRooms(nextVisit: number[]): number {
    const MOD = 1_000_000_007;
    const n = nextVisit.length;
    const dp = new Array<number>(n);
    dp[0] = 0;
    for (let i = 1; i < n; i++) {
        const prev = dp[i - 1];
        const sub = dp[nextVisit[i - 1]];
        let val = ((2 * prev) % MOD - sub + MOD) % MOD;
        val = (val + 2) % MOD;
        dp[i] = val;
    }
    return dp[n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nextVisit
     * @return Integer
     */
    function firstDayBeenInAllRooms($nextVisit) {
        $mod = 1000000007;
        $n = count($nextVisit);
        $dp = array_fill(0, $n, 0); // dp[0] = 0 by default

        for ($i = 1; $i < $n; $i++) {
            $val = (2 * $dp[$i - 1]) % $mod;
            $val = ($val - $dp[$nextVisit[$i - 1]]) % $mod;
            $val = ($val + 2) % $mod;
            if ($val < 0) {
                $val += $mod;
            }
            $dp[$i] = $val;
        }

        return $dp[$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func firstDayBeenInAllRooms(_ nextVisit: [Int]) -> Int {
        let MOD = 1_000_000_007
        let n = nextVisit.count
        var dp = Array(repeating: 0, count: n)
        for i in 1..<n {
            let prev = dp[i - 1]
            let back = dp[nextVisit[i - 1]]
            var cur = (2 * prev) % MOD
            cur = (cur - back + MOD) % MOD
            cur = (cur + 2) % MOD
            dp[i] = cur
        }
        return dp[n - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun firstDayBeenInAllRooms(nextVisit: IntArray): Int {
        val MOD = 1_000_000_007L
        val n = nextVisit.size
        val dp = LongArray(n)
        for (i in 1 until n) {
            val cur = ((2 * dp[i - 1] % MOD - dp[nextVisit[i - 1]] + MOD) % MOD + 2) % MOD
            dp[i] = cur
        }
        return dp[n - 1].toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int firstDayBeenInAllRooms(List<int> nextVisit) {
    int n = nextVisit.length;
    List<int> dp = List.filled(n, 0);
    dp[0] = 0;
    for (int i = 1; i < n; i++) {
      int prev = dp[i - 1];
      int nxt = dp[nextVisit[i - 1]];
      int val = ((2 * prev) % _MOD - nxt) % _MOD;
      if (val < 0) val += _MOD;
      val = (val + 2) % _MOD;
      dp[i] = val;
    }
    return dp[n - 1];
  }
}
```

## Golang

```go
func firstDayBeenInAllRooms(nextVisit []int) int {
	const MOD int64 = 1000000007
	n := len(nextVisit)
	dp := make([]int64, n)
	for i := 1; i < n; i++ {
		prev := dp[i-1]
		val := (2*prev%MOD - dp[nextVisit[i-1]] + 2) % MOD
		if val < 0 {
			val += MOD
		}
		dp[i] = val
	}
	return int(dp[n-1])
}
```

## Ruby

```ruby
def first_day_been_in_all_rooms(next_visit)
  mod = 1_000_000_007
  n = next_visit.length
  dp = Array.new(n, 0)
  (0...n - 1).each do |i|
    val = (2 * dp[i]) % mod
    val = (val - dp[next_visit[i]]) % mod
    val = (val + 2) % mod
    dp[i + 1] = val
  end
  dp[n - 1]
end
```

## Scala

```scala
object Solution {
    def firstDayBeenInAllRooms(nextVisit: Array[Int]): Int = {
        val MOD = 1000000007L
        val n = nextVisit.length
        val dp = new Array[Long](n)
        dp(0) = 0L
        for (i <- 1 until n) {
            val prev = dp(i - 1)
            val sub = dp(nextVisit(i - 1))
            var cur = (2 * prev % MOD - sub + MOD) % MOD
            cur = (cur + 2) % MOD
            dp(i) = cur
        }
        (dp(n - 1) % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn first_day_been_in_all_rooms(next_visit: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = next_visit.len();
        let mut dp = vec![0i64; n];
        for i in 1..n {
            let prev = i - 1;
            let nv = next_visit[prev] as usize;
            let mut val = (2 * dp[prev]) % MOD;
            val = (val - dp[nv] + MOD) % MOD;
            val = (val + 2) % MOD;
            dp[i] = val;
        }
        dp[n - 1] as i32
    }
}
```

## Racket

```racket
(define/contract (first-day-been-in-all-rooms nextVisit)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((MOD 1000000007)
         (n (length nextVisit))
         (nextVec (list->vector nextVisit))
         (dp (make-vector n 0)))
    (for ([i (in-range 1 n)])
      (let* ((prev (vector-ref dp (- i 1)))
             (nextIdx (vector-ref nextVec i))
             (val (modulo (+ (- (* 2 prev) (vector-ref dp nextIdx)) 2) MOD)))
        (vector-set! dp i val)))
    (vector-ref dp (- n 1))))
```

## Erlang

```erlang
-spec first_day_been_in_all_rooms(NextVisit :: [integer()]) -> integer().
first_day_been_in_all_rooms(NextVisit) ->
    Mod = 1000000007,
    N = length(NextVisit),
    NextTuple = list_to_tuple(NextVisit),
    DP0 = #{0 => 0},
    Indices = lists:seq(1, N - 1),
    DPFinal = lists:foldl(
        fun(I, Acc) ->
            Prev = I - 1,
            DPPrev = maps:get(Prev, Acc),
            NextIdx = element(Prev + 1, NextTuple),
            DPNextVisit = maps:get(NextIdx, Acc),
            Temp = (2 * DPPrev rem Mod - DPNextVisit + 2) rem Mod,
            Val = if Temp < 0 -> Temp + Mod; true -> Temp end,
            Acc#{I => Val}
        end,
        DP0,
        Indices),
    maps:get(N - 1, DPFinal).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @spec first_day_been_in_all_rooms(next_visit :: [integer]) :: integer
  def first_day_been_in_all_rooms(next_visit) do
    mod = 1_000_000_007
    n = length(next_visit)

    # Initialize an Erlang array with default 0, size n
    dp = :array.new(n, default: 0)

    dp =
      Enum.reduce(1..(n - 1), dp, fn i, arr ->
        prev = :array.get(i - 1, arr)
        next_idx = Enum.at(next_visit, i - 1)
        nxt = :array.get(next_idx, arr)

        # (2 * prev) % mod
        two_prev = rem(2 * prev, mod)

        # (two_prev - nxt) modulo mod (ensure non‑negative)
        diff =
          if two_prev >= nxt do
            two_prev - nxt
          else
            two_prev + mod - nxt
          end

        cur = rem(diff + 2, mod)
        :array.set(i, cur, arr)
      end)

    :array.get(n - 1, dp)
  end
end
```
