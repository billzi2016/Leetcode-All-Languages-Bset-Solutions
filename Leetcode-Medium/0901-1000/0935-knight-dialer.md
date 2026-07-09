# 0935. Knight Dialer

## Cpp

```cpp
class Solution {
public:
    int knightDialer(int n) {
        const long long MOD = 1000000007LL;
        static const vector<vector<int>> moves = {
            {4,6},      // 0
            {6,8},      // 1
            {7,9},      // 2
            {4,8},      // 3
            {0,3,9},    // 4
            {},         // 5
            {0,1,7},    // 6
            {2,6},      // 7
            {1,3},      // 8
            {2,4}       // 9
        };
        vector<long long> cur(10, 1), nxt(10);
        for (int len = 2; len <= n; ++len) {
            fill(nxt.begin(), nxt.end(), 0);
            for (int d = 0; d < 10; ++d) {
                long long ways = cur[d];
                if (!ways) continue;
                for (int nb : moves[d]) {
                    nxt[nb] += ways;
                    if (nxt[nb] >= MOD) nxt[nb] -= MOD;
                }
            }
            cur.swap(nxt);
        }
        long long ans = 0;
        for (long long v : cur) {
            ans += v;
            if (ans >= MOD) ans -= MOD;
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int knightDialer(int n) {
        final int MOD = 1_000_000_007;
        if (n == 1) return 10;
        long[] prev = new long[10];
        Arrays.fill(prev, 1);
        int[][] jumps = {
            {4, 6},    // 0
            {6, 8},    // 1
            {7, 9},    // 2
            {4, 8},    // 3
            {3, 9, 0},// 4
            {},        // 5
            {1, 7, 0},// 6
            {2, 6},    // 7
            {1, 3},    // 8
            {2, 4}     // 9
        };
        for (int step = 2; step <= n; step++) {
            long[] cur = new long[10];
            for (int d = 0; d < 10; d++) {
                for (int nxt : jumps[d]) {
                    cur[d] += prev[nxt];
                }
                cur[d] %= MOD;
            }
            prev = cur;
        }
        long ans = 0;
        for (long v : prev) {
            ans += v;
        }
        return (int)(ans % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        dp = [1] * 10  # length 1
        for _ in range(1, n):
            ndp = [0] * 10
            for i in range(10):
                total = 0
                for j in moves[i]:
                    total += dp[j]
                ndp[i] = total % MOD
            dp = ndp
        return sum(dp) % MOD
```

## Python3

```python
class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 10
        jumps = [
            [4, 6],      # 0
            [6, 8],      # 1
            [7, 9],      # 2
            [4, 8],      # 3
            [0, 3, 9],   # 4
            [],          # 5
            [0, 1, 7],   # 6
            [2, 6],      # 7
            [1, 3],      # 8
            [2, 4]       # 9
        ]
        prev = [1] * 10
        for _ in range(1, n):
            cur = [0] * 10
            for i in range(10):
                s = 0
                for nb in jumps[i]:
                    s += prev[nb]
                cur[i] = s % MOD
            prev = cur
        return sum(prev) % MOD
```

## C

```c
int knightDialer(int n) {
    const int MOD = 1000000007;
    if (n == 1) return 10;

    // adjacency list: up to 3 moves per digit, -1 as sentinel
    const int adj[10][3] = {
        {4,6,-1},   //0
        {6,8,-1},   //1
        {7,9,-1},   //2
        {4,8,-1},   //3
        {0,3,9},    //4
        {-1,-1,-1}, //5 (no moves)
        {0,1,7},    //6
        {2,6,-1},   //7
        {1,3,-1},   //8
        {2,4,-1}    //9
    };
    const int cnt[10] = {2,2,2,2,3,0,3,2,2,2};

    long long dp[10];
    long long ndp[10];
    for (int i = 0; i < 10; ++i) dp[i] = 1; // length 1

    for (int step = 1; step < n; ++step) {
        for (int i = 0; i < 10; ++i) ndp[i] = 0;
        for (int d = 0; d < 10; ++d) {
            if (cnt[d] == 0) continue;
            long long ways = dp[d];
            if (!ways) continue;
            for (int k = 0; k < cnt[d]; ++k) {
                int nb = adj[d][k];
                ndp[nb] += ways;
                if (ndp[nb] >= MOD) ndp[nb] -= MOD;
            }
        }
        for (int i = 0; i < 10; ++i) dp[i] = ndp[i];
    }

    long long ans = 0;
    for (int i = 0; i < 10; ++i) {
        ans += dp[i];
        if (ans >= MOD) ans -= MOD;
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1000000007;

    public int KnightDialer(int n)
    {
        if (n == 1) return 10;

        int[][] moves = new int[10][];
        moves[0] = new[] { 4, 6 };
        moves[1] = new[] { 6, 8 };
        moves[2] = new[] { 7, 9 };
        moves[3] = new[] { 4, 8 };
        moves[4] = new[] { 0, 3, 9 };
        moves[5] = new int[] { };
        moves[6] = new[] { 0, 1, 7 };
        moves[7] = new[] { 2, 6 };
        moves[8] = new[] { 1, 3 };
        moves[9] = new[] { 2, 4 };

        long[] prev = new long[10];
        for (int i = 0; i < 10; i++) prev[i] = 1;
        long[] cur = new long[10];

        for (int step = 2; step <= n; ++step)
        {
            for (int d = 0; d < 10; ++d)
            {
                long sum = 0;
                foreach (int nxt in moves[d])
                    sum += prev[nxt];
                cur[d] = sum % MOD;
            }
            var temp = prev;
            prev = cur;
            cur = temp;
        }

        long ans = 0;
        for (int i = 0; i < 10; i++)
            ans = (ans + prev[i]) % MOD;

        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var knightDialer = function(n) {
    const MOD = 1000000007;
    if (n === 1) return 10;
    
    const moves = [
        [4,6],      // 0
        [6,8],      // 1
        [7,9],      // 2
        [4,8],      // 3
        [0,3,9],    // 4
        [],         // 5
        [0,1,7],    // 6
        [2,6],      // 7
        [1,3],      // 8
        [2,4]       // 9
    ];
    
    let dp = new Array(10).fill(1); // length 1
    
    for (let step = 2; step <= n; ++step) {
        const ndp = new Array(10).fill(0);
        for (let i = 0; i < 10; ++i) {
            for (const nxt of moves[i]) {
                ndp[i] = (ndp[i] + dp[nxt]) % MOD;
            }
        }
        dp = ndp;
    }
    
    let ans = 0;
    for (let v of dp) {
        ans = (ans + v) % MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function knightDialer(n: number): number {
    const MOD = 1_000_000_007;
    if (n === 1) return 10;

    const moves: number[][] = [
        [4, 6],    // 0
        [6, 8],    // 1
        [7, 9],    // 2
        [4, 8],    // 3
        [0, 3, 9],// 4
        [],        // 5 (unused)
        [0, 1, 7],// 6
        [2, 6],    // 7
        [1, 3],    // 8
        [2, 4]     // 9
    ];

    let dp = new Array(10).fill(1); // length 1

    for (let step = 2; step <= n; ++step) {
        const ndp = new Array(10).fill(0);
        for (let src = 0; src < 10; ++src) {
            const count = dp[src];
            if (count === 0) continue;
            for (const dst of moves[src]) {
                ndp[dst] = (ndp[dst] + count) % MOD;
            }
        }
        dp = ndp;
    }

    let ans = 0;
    for (const v of dp) {
        ans = (ans + v) % MOD;
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function knightDialer($n) {
        $MOD = 1000000007;
        if ($n == 1) return 10;

        $moves = [
            [4,6],      // 0
            [6,8],      // 1
            [7,9],      // 2
            [4,8],      // 3
            [0,3,9],    // 4
            [],         // 5
            [0,1,7],    // 6
            [2,6],      // 7
            [1,3],      // 8
            [2,4]       // 9
        ];

        $dp = array_fill(0, 10, 1); // length 1

        for ($len = 2; $len <= $n; $len++) {
            $next = array_fill(0, 10, 0);
            for ($i = 0; $i < 10; $i++) {
                foreach ($moves[$i] as $j) {
                    $next[$i] += $dp[$j];
                    if ($next[$i] >= $MOD) $next[$i] -= $MOD;
                }
            }
            $dp = $next;
        }

        $ans = 0;
        foreach ($dp as $val) {
            $ans += $val;
            if ($ans >= $MOD) $ans -= $MOD;
        }
        return $ans % $MOD;
    }
}
```

## Swift

```swift
class Solution {
    func knightDialer(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        if n == 1 { return 10 }
        let moves: [[Int]] = [
            [4,6],          // 0
            [6,8],          // 1
            [7,9],          // 2
            [4,8],          // 3
            [0,3,9],        // 4
            [],             // 5
            [0,1,7],        // 6
            [2,6],          // 7
            [1,3],          // 8
            [2,4]           // 9
        ]
        var prev = Array(repeating: 1, count: 10)   // length 1
        for _ in 1..<n {                           // perform n-1 jumps
            var cur = Array(repeating: 0, count: 10)
            for d in 0...9 {
                var sum = 0
                for nb in moves[d] {
                    sum += prev[nb]
                }
                cur[d] = sum % MOD
            }
            prev = cur
        }
        var ans = 0
        for v in prev {
            ans += v
            if ans >= MOD { ans -= MOD }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun knightDialer(n: Int): Int {
        if (n == 1) return 10
        val moves = arrayOf(
            intArrayOf(4, 6),          // 0
            intArrayOf(6, 8),          // 1
            intArrayOf(7, 9),          // 2
            intArrayOf(4, 8),          // 3
            intArrayOf(0, 3, 9),       // 4
            intArrayOf(),              // 5
            intArrayOf(0, 1, 7),       // 6
            intArrayOf(2, 6),          // 7
            intArrayOf(1, 3),          // 8
            intArrayOf(2, 4)           // 9
        )
        val MOD = 1_000_000_007L
        var prev = LongArray(10) { 1L }
        for (step in 1 until n) {
            val cur = LongArray(10)
            for (i in 0..9) {
                val cnt = prev[i]
                if (cnt == 0L) continue
                for (next in moves[i]) {
                    cur[next] = (cur[next] + cnt) % MOD
                }
            }
            prev = cur
        }
        var ans = 0L
        for (v in prev) {
            ans = (ans + v) % MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int knightDialer(int n) {
    if (n == 1) return 10;
    const List<List<int>> moves = [
      [4, 6],        // 0
      [6, 8],        // 1
      [7, 9],        // 2
      [4, 8],        // 3
      [3, 9, 0],     // 4
      [],            // 5
      [1, 7, 0],     // 6
      [2, 6],        // 7
      [1, 3],        // 8
      [2, 4]         // 9
    ];

    List<int> dp = List.filled(10, 1);
    for (int step = 1; step < n; ++step) {
      List<int> ndp = List.filled(10, 0);
      for (int i = 0; i < 10; ++i) {
        int sum = 0;
        for (int nxt in moves[i]) {
          sum += dp[nxt];
          if (sum >= _mod) sum -= _mod;
        }
        ndp[i] = sum;
      }
      dp = ndp;
    }

    int ans = 0;
    for (int v in dp) {
      ans += v;
      if (ans >= _mod) ans -= _mod;
    }
    return ans;
  }
}
```

## Golang

```go
func knightDialer(n int) int {
	const MOD int64 = 1000000007
	if n == 1 {
		return 10
	}
	moves := [][]int{
		{4, 6},       // 0
		{6, 8},       // 1
		{7, 9},       // 2
		{4, 8},       // 3
		{0, 3, 9},    // 4
		{},           // 5
		{0, 1, 7},    // 6
		{2, 6},       // 7
		{1, 3},       // 8
		{2, 4},       // 9
	}
	prev := make([]int64, 10)
	for i := 0; i < 10; i++ {
		prev[i] = 1
	}
	curr := make([]int64, 10)

	for step := 1; step < n; step++ {
		for i := 0; i < 10; i++ {
			var sum int64
			for _, nxt := range moves[i] {
				sum += prev[nxt]
			}
			curr[i] = sum % MOD
		}
		prev, curr = curr, prev
	}

	var ans int64
	for i := 0; i < 10; i++ {
		ans = (ans + prev[i]) % MOD
	}
	return int(ans)
}
```

## Ruby

```ruby
def knight_dialer(n)
  mod = 1_000_000_007
  return 10 if n == 1
  moves = [
    [4, 6],        # 0
    [6, 8],        # 1
    [7, 9],        # 2
    [4, 8],        # 3
    [0, 3, 9],     # 4
    [],            # 5
    [0, 1, 7],     # 6
    [2, 6],        # 7
    [1, 3],        # 8
    [2, 4]         # 9
  ]
  prev = Array.new(10, 1)
  (n - 1).times do
    cur = Array.new(10, 0)
    10.times do |i|
      moves[i].each { |j| cur[i] = (cur[i] + prev[j]) % mod }
    end
    prev = cur
  end
  prev.sum % mod
end
```

## Scala

```scala
object Solution {
    def knightDialer(n: Int): Int = {
        val MOD = 1000000007L
        if (n == 1) return 10
        val moves = Array(
            Array(4, 6),      // 0
            Array(6, 8),      // 1
            Array(7, 9),      // 2
            Array(4, 8),      // 3
            Array(0, 3, 9),   // 4
            Array[Int](),     // 5
            Array(0, 1, 7),   // 6
            Array(2, 6),      // 7
            Array(1, 3),      // 8
            Array(2, 4)       // 9
        )
        var prev = Array.fill[Long](10)(1L)
        for (_ <- 2 to n) {
            val cur = new Array[Long](10)
            var d = 0
            while (d < 10) {
                val cnt = prev(d)
                if (cnt != 0) {
                    val nxts = moves(d)
                    var i = 0
                    while (i < nxts.length) {
                        val nd = nxts(i)
                        cur(nd) += cnt
                        if (cur(nd) >= MOD) cur(nd) -= MOD
                        i += 1
                    }
                }
                d += 1
            }
            prev = cur
        }
        var ans = 0L
        var i = 0
        while (i < 10) {
            ans += prev(i)
            if (ans >= MOD) ans -= MOD
            i += 1
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn knight_dialer(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        if n == 1 {
            return 10;
        }
        let mut prev = [1i64; 10];
        for _ in 2..=n {
            let mut cur = [0i64; 10];
            cur[0] = (prev[4] + prev[6]) % MOD;
            cur[1] = (prev[6] + prev[8]) % MOD;
            cur[2] = (prev[7] + prev[9]) % MOD;
            cur[3] = (prev[4] + prev[8]) % MOD;
            cur[4] = (prev[0] + prev[3] + prev[9]) % MOD;
            // digit 5 has no moves, stays zero
            cur[6] = (prev[0] + prev[1] + prev[7]) % MOD;
            cur[7] = (prev[2] + prev[6]) % MOD;
            cur[8] = (prev[1] + prev[3]) % MOD;
            cur[9] = (prev[2] + prev[4]) % MOD;
            prev = cur;
        }
        let mut ans: i64 = 0;
        for &v in &prev {
            ans = (ans + v) % MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (knight-dialer n)
  (-> exact-integer? exact-integer?)
  (let ((jumps (vector (list 4 6)        ;0
                       (list 6 8)        ;1
                       (list 7 9)        ;2
                       (list 4 8)        ;3
                       (list 3 9 0)      ;4
                       '()               ;5
                       (list 1 7 0)      ;6
                       (list 2 6)        ;7
                       (list 1 3)        ;8
                       (list 2 4))))     ;9
    (let loop ((step 0)
               (prev (make-vector 10 1))) ; dp for length 1
      (if (= step (- n 1))
          (let ((ans 0))
            (for ([i (in-range 10)])
              (set! ans (modulo (+ ans (vector-ref prev i)) MOD)))
            ans)
          (let ((cur (make-vector 10 0)))
            (for ([i (in-range 10)])
              (let ((total 0))
                (for ([nbr (vector-ref jumps i)])
                  (set! total (modulo (+ total (vector-ref prev nbr)) MOD)))
                (vector-set! cur i total)))
            (loop (+ step 1) cur))))))
```

## Erlang

```erlang
-module(solution).
-export([knight_dialer/1]).
-define(MOD, 1000000007).

-spec knight_dialer(N :: integer()) -> integer().
knight_dialer(1) ->
    10;
knight_dialer(N) when N > 1 ->
    Counts = iter(N - 1, [1,1,1,1,1,1,1,1,1,1]),
    lists:foldl(fun(X, Acc) -> (X + Acc) rem ?MOD end, 0, Counts).

iter(0, Counts) ->
    Counts;
iter(Steps, [C0,C1,C2,C3,C4,_C5,C6,C7,C8,C9]) ->
    New0 = (C4 + C6) rem ?MOD,
    New1 = (C6 + C8) rem ?MOD,
    New2 = (C7 + C9) rem ?MOD,
    New3 = (C4 + C8) rem ?MOD,
    New4 = ((C0 + C3) rem ?MOD + C9) rem ?MOD,
    New5 = 0,
    New6 = ((C0 + C1) rem ?MOD + C7) rem ?MOD,
    New7 = (C2 + C6) rem ?MOD,
    New8 = (C1 + C3) rem ?MOD,
    New9 = (C2 + C4) rem ?MOD,
    iter(Steps - 1, [New0,New1,New2,New3,New4,New5,New6,New7,New8,New9]).
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @spec knight_dialer(n :: integer) :: integer
  def knight_dialer(n) do
    mod = 1_000_000_007

    if n == 1 do
      10
    else
      jumps = [
        [4, 6],       # 0
        [6, 8],       # 1
        [7, 9],       # 2
        [4, 8],       # 3
        [0, 3, 9],    # 4
        [],           # 5
        [0, 1, 7],    # 6
        [2, 6],       # 7
        [1, 3],       # 8
        [2, 4]        # 9
      ]

      prev = List.to_tuple(List.duplicate(1, 10))
      steps = n - 1

      {final_state, _} =
        Enum.reduce(1..steps, {prev, nil}, fn _, {prev_state, _} ->
          cur_list =
            for i <- 0..9 do
              Enum.reduce(jumps[i], 0, fn nxt, acc ->
                (acc + elem(prev_state, nxt + 1)) |> rem(mod)
              end)
            end

          {List.to_tuple(cur_list), nil}
        end)

      final_state
      |> Tuple.to_list()
      |> Enum.sum()
      |> rem(mod)
    end
  end
end
```
