# 0526. Beautiful Arrangement

## Cpp

```cpp
class Solution {
public:
    int countArrangement(int n) {
        this->n = n;
        memo.assign(1 << n, -1);
        return dfs(0);
    }
private:
    int n;
    vector<int> memo;
    
    int dfs(int mask) {
        int pos = __builtin_popcount(mask) + 1; // current position (1-indexed)
        if (pos > n) return 1;                  // all positions filled
        int &res = memo[mask];
        if (res != -1) return res;
        res = 0;
        for (int i = 1; i <= n; ++i) {
            int bit = 1 << (i - 1);
            if ((mask & bit) == 0 && (i % pos == 0 || pos % i == 0)) {
                res += dfs(mask | bit);
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int countArrangement(int n) {
        int totalMask = 1 << n;
        int[] memo = new int[totalMask];
        for (int i = 0; i < totalMask; i++) {
            memo[i] = -1;
        }
        return dfs(0, n, memo);
    }

    private int dfs(int mask, int n, int[] memo) {
        if (mask == (1 << n) - 1) {
            return 1;
        }
        if (memo[mask] != -1) {
            return memo[mask];
        }
        int pos = Integer.bitCount(mask) + 1; // current position (1-indexed)
        int ways = 0;
        for (int i = 1; i <= n; i++) {
            int bit = 1 << (i - 1);
            if ((mask & bit) == 0 && (i % pos == 0 || pos % i == 0)) {
                ways += dfs(mask | bit, n, memo);
            }
        }
        memo[mask] = ways;
        return ways;
    }
}
```

## Python

```python
class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        from functools import lru_cache

        @lru_cache(None)
        def dfs(pos, mask):
            if pos > n:
                return 1
            total = 0
            for num in range(1, n + 1):
                bit = 1 << (num - 1)
                if not (mask & bit) and (num % pos == 0 or pos % num == 0):
                    total += dfs(pos + 1, mask | bit)
            return total

        return dfs(1, 0)
```

## Python3

```python
class Solution:
    def countArrangement(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(pos: int, mask: int) -> int:
            if pos > n:
                return 1
            total = 0
            for i in range(1, n + 1):
                bit = 1 << i
                if not (mask & bit) and (i % pos == 0 or pos % i == 0):
                    total += dfs(pos + 1, mask | bit)
            return total

        return dfs(1, 0)
```

## C

```c
#include <stdlib.h>

static int dfs(int n, int mask, int *dp) {
    if (mask == (1 << n) - 1) return 1;
    if (dp[mask] != -1) return dp[mask];
    int pos = __builtin_popcount((unsigned)mask) + 1;
    int total = 0;
    for (int i = 1; i <= n; ++i) {
        if (!(mask & (1 << (i - 1))) && ((i % pos == 0) || (pos % i == 0))) {
            total += dfs(n, mask | (1 << (i - 1)), dp);
        }
    }
    dp[mask] = total;
    return total;
}

int countArrangement(int n) {
    int size = 1 << n;
    int *dp = (int *)malloc(size * sizeof(int));
    for (int i = 0; i < size; ++i) dp[i] = -1;
    int ans = dfs(n, 0, dp);
    free(dp);
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution
{
    private int n;
    private int[] memo;

    public int CountArrangement(int n)
    {
        this.n = n;
        int size = 1 << n;
        memo = new int[size];
        for (int i = 0; i < size; i++) memo[i] = -1;
        return Dfs(0);
    }

    private int Dfs(int mask)
    {
        int pos = BitCount(mask) + 1; // current position (1-indexed)
        if (pos > n) return 1;

        if (memo[mask] != -1) return memo[mask];

        int total = 0;
        for (int i = 1; i <= n; i++)
        {
            int bit = 1 << (i - 1);
            if ((mask & bit) == 0 && (i % pos == 0 || pos % i == 0))
            {
                total += Dfs(mask | bit);
            }
        }

        memo[mask] = total;
        return total;
    }

    private int BitCount(int x)
    {
        // Kernighan's algorithm
        int count = 0;
        while (x != 0)
        {
            x &= (x - 1);
            count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countArrangement = function(n) {
    const totalMask = (1 << n) - 1;
    const memo = new Array(1 << n).fill(-1);
    
    const bitCount = (x) => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    };
    
    const dfs = (mask) => {
        if (mask === totalMask) return 1;
        if (memo[mask] !== -1) return memo[mask];
        
        const pos = bitCount(mask) + 1; // current position (1-indexed)
        let ways = 0;
        for (let i = 1; i <= n; i++) {
            const bit = 1 << (i - 1);
            if ((mask & bit) === 0 && (i % pos === 0 || pos % i === 0)) {
                ways += dfs(mask | bit);
            }
        }
        memo[mask] = ways;
        return ways;
    };
    
    return dfs(0);
};
```

## Typescript

```typescript
function countArrangement(n: number): number {
    const totalMask = 1 << n;
    const memo = new Array<number>(totalMask).fill(-1);
    function popcnt(x: number): number {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    }
    function dfs(mask: number): number {
        const pos = popcnt(mask) + 1;
        if (pos > n) return 1;
        if (memo[mask] !== -1) return memo[mask];
        let ans = 0;
        for (let i = 1; i <= n; i++) {
            const bit = 1 << (i - 1);
            if ((mask & bit) === 0 && (i % pos === 0 || pos % i === 0)) {
                ans += dfs(mask | bit);
            }
        }
        memo[mask] = ans;
        return ans;
    }
    return dfs(0);
}
```

## Php

```php
class Solution {
    private $n;
    private $memo = [];

    /**
     * @param Integer $n
     * @return Integer
     */
    public function countArrangement($n) {
        $this->n = $n;
        $this->memo = [];
        return $this->dfs(0);
    }

    private function dfs($mask) {
        if ($mask == (1 << $this->n) - 1) {
            return 1;
        }
        if (isset($this->memo[$mask])) {
            return $this->memo[$mask];
        }
        $pos = $this->popcount($mask) + 1; // current position (1-indexed)
        $total = 0;
        for ($i = 1; $i <= $this->n; $i++) {
            $bit = 1 << ($i - 1);
            if (($mask & $bit) === 0 && ($i % $pos == 0 || $pos % $i == 0)) {
                $total += $this->dfs($mask | $bit);
            }
        }
        $this->memo[$mask] = $total;
        return $total;
    }

    private function popcount($x) {
        $cnt = 0;
        while ($x) {
            $x &= ($x - 1);
            $cnt++;
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    private var n = 0
    private var memo: [Int] = []
    
    func countArrangement(_ n: Int) -> Int {
        self.n = n
        let totalMasks = 1 << n
        memo = Array(repeating: -1, count: totalMasks)
        return dfs(0)
    }
    
    private func dfs(_ mask: Int) -> Int {
        if mask == (1 << n) - 1 { // all numbers placed
            return 1
        }
        if memo[mask] != -1 {
            return memo[mask]
        }
        let position = mask.nonzeroBitCount + 1
        var ways = 0
        for i in 1...n {
            let bit = 1 << (i - 1)
            if (mask & bit) == 0 && (i % position == 0 || position % i == 0) {
                ways += dfs(mask | bit)
            }
        }
        memo[mask] = ways
        return ways
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countArrangement(n: Int): Int {
        val fullMask = (1 shl n) - 1
        val memo = IntArray(1 shl n) { -1 }
        fun dfs(mask: Int): Int {
            if (mask == fullMask) return 1
            val cached = memo[mask]
            if (cached != -1) return cached
            var total = 0
            val pos = Integer.bitCount(mask) + 1
            for (i in 0 until n) {
                if ((mask and (1 shl i)) == 0) {
                    val num = i + 1
                    if (num % pos == 0 || pos % num == 0) {
                        total += dfs(mask or (1 shl i))
                    }
                }
            }
            memo[mask] = total
            return total
        }
        return dfs(0)
    }
}
```

## Dart

```dart
class Solution {
  int countArrangement(int n) {
    int dfs(int pos, int mask) {
      if (pos > n) return 1;
      int total = 0;
      for (int i = 1; i <= n; ++i) {
        int bit = 1 << (i - 1);
        if ((mask & bit) == 0 && (i % pos == 0 || pos % i == 0)) {
          total += dfs(pos + 1, mask | bit);
        }
      }
      return total;
    }

    return dfs(1, 0);
  }
}
```

## Golang

```go
import "math/bits"

func countArrangement(n int) int {
    memo := make(map[int]int)
    fullMask := (1 << n) - 1

    var dfs func(mask int) int
    dfs = func(mask int) int {
        if mask == fullMask {
            return 1
        }
        if v, ok := memo[mask]; ok {
            return v
        }
        pos := bits.OnesCount(uint(mask)) + 1
        total := 0
        for i := 1; i <= n; i++ {
            bit := 1 << (i - 1)
            if mask&bit == 0 && (i%pos == 0 || pos%i == 0) {
                total += dfs(mask | bit)
            }
        }
        memo[mask] = total
        return total
    }

    return dfs(0)
}
```

## Ruby

```ruby
def count_arrangement(n)
  @n = n
  @memo = {}
  dfs(1, 0)
end

def dfs(pos, mask)
  return 1 if pos > @n
  key = [pos, mask]
  return @memo[key] if @memo.key?(key)

  total = 0
  (1..@n).each do |num|
    bit = 1 << (num - 1)
    next if (mask & bit) != 0
    if num % pos == 0 || pos % num == 0
      total += dfs(pos + 1, mask | bit)
    end
  end

  @memo[key] = total
end
```

## Scala

```scala
object Solution {
    def countArrangement(n: Int): Int = {
        val totalMask = 1 << n
        val memo = Array.fill[Int](totalMask)(-1)

        def dfs(pos: Int, mask: Int): Int = {
            if (pos > n) return 1
            if (memo(mask) != -1) return memo(mask)
            var count = 0
            var num = 1
            while (num <= n) {
                val bit = 1 << (num - 1)
                if ((mask & bit) == 0 && (num % pos == 0 || pos % num == 0)) {
                    count += dfs(pos + 1, mask | bit)
                }
                num += 1
            }
            memo(mask) = count
            count
        }

        dfs(1, 0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_arrangement(n: i32) -> i32 {
        let n = n as usize;
        let total_masks = 1usize << n;
        // -1 indicates uncomputed
        let mut memo = vec![-1i32; total_masks];
        fn dfs(mask: u32, n: usize, memo: &mut Vec<i32>) -> i32 {
            if mask == (1u32 << n) - 1 {
                return 1;
            }
            let idx = mask as usize;
            if memo[idx] != -1 {
                return memo[idx];
            }
            let pos = (mask.count_ones() + 1) as usize; // current position (1-indexed)
            let mut total = 0i32;
            for num in 1..=n {
                let bit = 1u32 << (num - 1);
                if mask & bit == 0 {
                    if num % pos == 0 || pos % num == 0 {
                        total += dfs(mask | bit, n, memo);
                    }
                }
            }
            memo[idx] = total;
            total
        }
        dfs(0, n, &mut memo)
    }
}
```

## Racket

```racket
(define/contract (count-arrangement n)
  (-> exact-integer? exact-integer?)
  (letrec ((dfs
            (lambda (pos mask)
              (if (> pos n)
                  1
                  (let loop ((j 1) (cnt 0))
                    (if (> j n)
                        cnt
                        (let ((bit (arithmetic-shift 1 (- j 1))))
                          (if (zero? (bitwise-and mask bit))
                              (if (or (= (remainder j pos) 0)
                                      (= (remainder pos j) 0))
                                  (loop (+ j 1)
                                        (+ cnt (dfs (+ pos 1) (bitwise-ior mask bit))))
                                  (loop (+ j 1) cnt))
                              (loop (+ j 1) cnt)))))))))
    (dfs 1 0)))
```

## Erlang

```erlang
-module(solution).
-export([count_arrangement/1]).

-spec count_arrangement(N :: integer()) -> integer().
count_arrangement(N) ->
    {Result, _} = dfs(1, 0, N, #{}),
    Result.

dfs(Pos, Mask, N, Memo) ->
    case maps:find(Mask, Memo) of
        {ok, Val} ->
            {Val, Memo};
        error ->
            if Pos > N ->
                    NewMemo = maps:put(Mask, 1, Memo),
                    {1, NewMemo};
               true ->
                    {Total, FinalMemo} = loop(1, N, Pos, Mask, N, Memo, 0),
                    UpdatedMemo = maps:put(Mask, Total, FinalMemo),
                    {Total, UpdatedMemo}
            end
    end.

loop(I, MaxI, Pos, Mask, N, Memo, Acc) when I > MaxI ->
    {Acc, Memo};
loop(I, MaxI, Pos, Mask, N, Memo, Acc) ->
    Bit = 1 bsl (I - 1),
    if ((Mask band Bit) == 0) andalso ((I rem Pos) == 0 orelse (Pos rem I) == 0) ->
            {SubCount, NewMemo} = dfs(Pos + 1, Mask bor Bit, N, Memo),
            loop(I + 1, MaxI, Pos, Mask, N, NewMemo, Acc + SubCount);
       true ->
            loop(I + 1, MaxI, Pos, Mask, N, Memo, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec count_arrangement(n :: integer) :: integer
  def count_arrangement(n) do
    max_mask = 1 <<< n
    base_dp = %{max_mask - 1 => 1}

    Enum.reduce(Enum.reverse(0..(max_mask - 2)), base_dp, fn mask, acc ->
      pos = bit_count(mask) + 1

      total =
        1..n
        |> Enum.reduce(0, fn num, sum ->
          bit = 1 <<< (num - 1)

          if (mask &&& bit) == 0 and (rem(num, pos) == 0 or rem(pos, num) == 0) do
            sum + Map.get(acc, mask ||| bit, 0)
          else
            sum
          end
        end)

      Map.put(acc, mask, total)
    end)
    |> Map.get(0)
  end

  defp bit_count(0), do: 0
  defp bit_count(x) do
    (x &&& 1) + bit_count(x >>> 1)
  end
end
```
