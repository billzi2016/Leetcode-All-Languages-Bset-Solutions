# 1575. Count All Possible Routes

## Cpp

```cpp
class Solution {
public:
    int countRoutes(vector<int>& locations, int start, int finish, int fuel) {
        const int MOD = 1'000'000'007;
        int n = locations.size();
        vector<vector<int>> memo(n, vector<int>(fuel + 1, -1));
        
        function<int(int,int)> dfs = [&](int city, int f) -> int {
            if (memo[city][f] != -1) return memo[city][f];
            long long ways = (city == finish); // staying counts as a route
            for (int nxt = 0; nxt < n; ++nxt) {
                if (nxt == city) continue;
                int cost = abs(locations[city] - locations[nxt]);
                if (cost <= f) {
                    ways += dfs(nxt, f - cost);
                    if (ways >= MOD) ways -= MOD;
                }
            }
            return memo[city][f] = (int)(ways % MOD);
        };
        
        return dfs(start, fuel);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    private int n;
    private int[] loc;
    private int[][] memo;

    public int countRoutes(int[] locations, int start, int finish, int fuel) {
        this.n = locations.length;
        this.loc = locations;
        this.memo = new int[n][fuel + 1];
        for (int i = 0; i < n; i++) {
            java.util.Arrays.fill(memo[i], -1);
        }
        return dfs(start, fuel, finish);
    }

    private int dfs(int city, int remainingFuel, int finish) {
        if (memo[city][remainingFuel] != -1) {
            return memo[city][remainingFuel];
        }
        long ways = (city == finish) ? 1 : 0; // staying at finish counts as a valid route
        for (int next = 0; next < n; next++) {
            if (next == city) continue;
            int cost = Math.abs(loc[city] - loc[next]);
            if (cost <= remainingFuel) {
                ways += dfs(next, remainingFuel - cost, finish);
                if (ways >= MOD) ways -= MOD; // keep within range to avoid overflow
            }
        }
        ways %= MOD;
        memo[city][remainingFuel] = (int) ways;
        return memo[city][remainingFuel];
    }
}
```

## Python

```python
class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(locations)

        from functools import lru_cache

        @lru_cache(None)
        def dfs(city, remaining):
            # count routes starting from 'city' with 'remaining' fuel
            total = 1 if city == finish else 0
            for nxt in range(n):
                if nxt == city:
                    continue
                cost = abs(locations[city] - locations[nxt])
                if remaining >= cost:
                    total += dfs(nxt, remaining - cost)
            return total % MOD

        return dfs(start, fuel)
```

## Python3

```python
from typing import List
from functools import lru_cache

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        n = len(locations)

        @lru_cache(None)
        def dfs(city: int, remaining: int) -> int:
            ans = 1 if city == finish else 0
            for nxt in range(n):
                if nxt == city:
                    continue
                cost = abs(locations[city] - locations[nxt])
                if cost <= remaining:
                    ans += dfs(nxt, remaining - cost)
            return ans % MOD

        return dfs(start, fuel)
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define MOD 1000000007

static int *g_loc;
static int g_n;
static int g_finish;
static int dp[101][201];

int dfs(int city, int fuel) {
    if (dp[city][fuel] != -1) return dp[city][fuel];
    long long ans = (city == g_finish) ? 1 : 0;
    for (int nxt = 0; nxt < g_n; ++nxt) {
        if (nxt == city) continue;
        int cost = abs(g_loc[city] - g_loc[nxt]);
        if (cost <= fuel) {
            ans += dfs(nxt, fuel - cost);
            if (ans >= MOD) ans %= MOD;
        }
    }
    dp[city][fuel] = ans % MOD;
    return dp[city][fuel];
}

int countRoutes(int* locations, int locationsSize, int start, int finish, int fuel) {
    g_loc = locations;
    g_n = locationsSize;
    g_finish = finish;
    for (int i = 0; i < locationsSize; ++i)
        for (int f = 0; f <= fuel; ++f)
            dp[i][f] = -1;
    return dfs(start, fuel);
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1000000007;
    private int[] _locations;
    private int _finish;
    private int[,] _memo;

    public int CountRoutes(int[] locations, int start, int finish, int fuel)
    {
        _locations = locations;
        _finish = finish;
        int n = locations.Length;
        _memo = new int[n, fuel + 1];
        for (int i = 0; i < n; i++)
            for (int f = 0; f <= fuel; f++)
                _memo[i, f] = -1;

        return Dfs(start, fuel);
    }

    private int Dfs(int city, int remainingFuel)
    {
        if (_memo[city, remainingFuel] != -1)
            return _memo[city, remainingFuel];

        long ways = (city == _finish) ? 1 : 0;

        for (int next = 0; next < _locations.Length; next++)
        {
            if (next == city) continue;
            int cost = Math.Abs(_locations[city] - _locations[next]);
            if (remainingFuel >= cost)
            {
                ways += Dfs(next, remainingFuel - cost);
                if (ways >= MOD) ways -= MOD;
            }
        }

        _memo[city, remainingFuel] = (int)(ways % MOD);
        return _memo[city, remainingFuel];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} locations
 * @param {number} start
 * @param {number} finish
 * @param {number} fuel
 * @return {number}
 */
var countRoutes = function(locations, start, finish, fuel) {
    const MOD = 1000000007;
    const n = locations.length;
    const memo = Array.from({ length: n }, () => Array(fuel + 1).fill(-1));
    
    function dfs(city, remaining) {
        if (memo[city][remaining] !== -1) return memo[city][remaining];
        let ans = city === finish ? 1 : 0;
        for (let next = 0; next < n; ++next) {
            if (next === city) continue;
            const cost = Math.abs(locations[city] - locations[next]);
            if (cost <= remaining) {
                ans = (ans + dfs(next, remaining - cost)) % MOD;
            }
        }
        memo[city][remaining] = ans;
        return ans;
    }
    
    return dfs(start, fuel);
};
```

## Typescript

```typescript
function countRoutes(locations: number[], start: number, finish: number, fuel: number): number {
    const MOD = 1_000_000_007;
    const n = locations.length;
    const memo: number[][] = Array.from({ length: n }, () => Array(fuel + 1).fill(-1));

    function dfs(city: number, remainingFuel: number): number {
        if (memo[city][remainingFuel] !== -1) return memo[city][remainingFuel];
        let ways = city === finish ? 1 : 0;
        for (let next = 0; next < n; ++next) {
            if (next === city) continue;
            const cost = Math.abs(locations[city] - locations[next]);
            if (remainingFuel >= cost) {
                ways += dfs(next, remainingFuel - cost);
                if (ways >= MOD) ways -= MOD;
            }
        }
        memo[city][remainingFuel] = ways % MOD;
        return memo[city][remainingFuel];
    }

    return dfs(start, fuel);
}
```

## Php

```php
class Solution {
    private $locations = [];
    private $finish = 0;
    private $mod = 1000000007;
    private $n = 0;
    private $memo = [];

    /**
     * @param Integer[] $locations
     * @param Integer $start
     * @param Integer $finish
     * @param Integer $fuel
     * @return Integer
     */
    function countRoutes($locations, $start, $finish, $fuel) {
        $this->locations = $locations;
        $this->finish = $finish;
        $this->n = count($locations);
        // initialize memo with -1 (uncomputed)
        $this->memo = array_fill(0, $this->n, array_fill(0, $fuel + 1, -1));
        return $this->dfs($start, $fuel);
    }

    private function dfs($city, $fuel) {
        if ($this->memo[$city][$fuel] !== -1) {
            return $this->memo[$city][$fuel];
        }
        $ans = ($city == $this->finish) ? 1 : 0;
        for ($next = 0; $next < $this->n; $next++) {
            if ($next == $city) continue;
            $cost = abs($this->locations[$city] - $this->locations[$next]);
            if ($cost <= $fuel) {
                $ans += $this->dfs($next, $fuel - $cost);
                if ($ans >= $this->mod) $ans -= $this->mod;
            }
        }
        $this->memo[$city][$fuel] = $ans % $this->mod;
        return $this->memo[$city][$fuel];
    }
}
```

## Swift

```swift
class Solution {
    private let MOD = 1_000_000_007
    private var locations: [Int] = []
    private var finish: Int = 0
    private var memo: [[Int]] = []

    private func dfs(_ city: Int, _ fuel: Int) -> Int {
        if memo[city][fuel] != -1 { return memo[city][fuel] }
        var ans = (city == finish) ? 1 : 0
        for next in 0..<locations.count where next != city {
            let cost = abs(locations[city] - locations[next])
            if fuel >= cost {
                ans += dfs(next, fuel - cost)
                if ans >= MOD { ans -= MOD }
            }
        }
        memo[city][fuel] = ans
        return ans
    }

    func countRoutes(_ locations: [Int], _ start: Int, _ finish: Int, _ fuel: Int) -> Int {
        self.locations = locations
        self.finish = finish
        let n = locations.count
        memo = Array(repeating: Array(repeating: -1, count: fuel + 1), count: n)
        return dfs(start, fuel) % MOD
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007
    fun countRoutes(locations: IntArray, start: Int, finish: Int, fuel: Int): Int {
        val n = locations.size
        val memo = Array(n) { IntArray(fuel + 1) { -1 } }

        fun dfs(city: Int, remaining: Int): Int {
            if (memo[city][remaining] != -1) return memo[city][remaining]
            var ways = if (city == finish) 1L else 0L
            for (next in 0 until n) {
                if (next == city) continue
                val cost = kotlin.math.abs(locations[city] - locations[next])
                if (remaining >= cost) {
                    ways += dfs(next, remaining - cost)
                    if (ways >= MOD) ways %= MOD
                }
            }
            val result = (ways % MOD).toInt()
            memo[city][remaining] = result
            return result
        }

        return dfs(start, fuel)
    }
}
```

## Dart

```dart
class Solution {
  static const int MOD = 1000000007;
  late List<int> _loc;
  late List<List<int>> _memo;
  late int _finish;
  int _n = 0;

  int countRoutes(List<int> locations, int start, int finish, int fuel) {
    _loc = locations;
    _n = locations.length;
    _finish = finish;
    _memo = List.generate(_n, (_) => List.filled(fuel + 1, -1));
    return _dfs(start, fuel);
  }

  int _dfs(int city, int remainingFuel) {
    if (_memo[city][remainingFuel] != -1) {
      return _memo[city][remainingFuel];
    }
    int res = (city == _finish) ? 1 : 0;
    for (int next = 0; next < _n; ++next) {
      if (next == city) continue;
      int cost = (_loc[city] - _loc[next]).abs();
      if (remainingFuel >= cost) {
        res = (res + _dfs(next, remainingFuel - cost)) % MOD;
      }
    }
    _memo[city][remainingFuel] = res;
    return res;
  }
}
```

## Golang

```go
func countRoutes(locations []int, start int, finish int, fuel int) int {
	const MOD = 1000000007
	n := len(locations)
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, fuel+1)
		for j := 0; j <= fuel; j++ {
			dp[i][j] = -1
		}
	}

	var dfs func(int, int) int
	dfs = func(city, f int) int {
		if dp[city][f] != -1 {
			return dp[city][f]
		}
		res := 0
		if city == finish {
			res = 1
		}
		for nxt := 0; nxt < n; nxt++ {
			if nxt == city {
				continue
			}
			cost := locations[city] - locations[nxt]
			if cost < 0 {
				cost = -cost
			}
			if cost <= f {
				res += dfs(nxt, f-cost)
				if res >= MOD {
					res -= MOD
				}
			}
		}
		dp[city][f] = res % MOD
		return dp[city][f]
	}

	return dfs(start, fuel) % MOD
}
```

## Ruby

```ruby
def count_routes(locations, start, finish, fuel)
  mod = 1_000_000_007
  n = locations.size
  memo = Array.new(n) { Array.new(fuel + 1, -1) }

  dfs = nil
  dfs = lambda do |city, remaining|
    cached = memo[city][remaining]
    return cached if cached != -1

    res = (city == finish ? 1 : 0)
    n.times do |next_city|
      next if next_city == city
      cost = (locations[city] - locations[next_city]).abs
      if cost <= remaining
        res += dfs.call(next_city, remaining - cost)
        res -= mod if res >= mod
      end
    end

    memo[city][remaining] = res % mod
  end

  dfs.call(start, fuel) % mod
end
```

## Scala

```scala
object Solution {
    private val MOD = 1000000007

    def countRoutes(locations: Array[Int], start: Int, finish: Int, fuel: Int): Int = {
        val n = locations.length
        val memo = Array.ofDim[Int](n, fuel + 1)
        val seen = Array.ofDim[Boolean](n, fuel + 1)

        def dfs(city: Int, remaining: Int): Int = {
            if (seen(city)(remaining)) return memo(city)(remaining)
            var ans: Long = 0
            if (city == finish) ans += 1
            var next = 0
            while (next < n) {
                if (next != city) {
                    val cost = math.abs(locations(city) - locations(next))
                    if (cost <= remaining) {
                        ans += dfs(next, remaining - cost)
                    }
                }
                next += 1
            }
            ans %= MOD
            seen(city)(remaining) = true
            memo(city)(remaining) = ans.toInt
            ans.toInt
        }

        dfs(start, fuel)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_routes(locations: Vec<i32>, start: i32, finish: i32, fuel: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = locations.len();
        let mut memo = vec![vec![-1i64; (fuel as usize) + 1]; n];

        fn dfs(
            city: usize,
            remaining_fuel: i32,
            locations: &Vec<i32>,
            finish: usize,
            memo: &mut Vec<Vec<i64>>,
            mod_val: i64,
        ) -> i64 {
            let f = remaining_fuel as usize;
            if memo[city][f] != -1 {
                return memo[city][f];
            }
            let mut ans: i64 = if city == finish { 1 } else { 0 };
            for next in 0..locations.len() {
                if next == city {
                    continue;
                }
                let cost = (locations[city] - locations[next]).abs();
                if cost <= remaining_fuel {
                    let sub = dfs(
                        next,
                        remaining_fuel - cost,
                        locations,
                        finish,
                        memo,
                        mod_val,
                    );
                    ans += sub;
                    if ans >= mod_val {
                        ans -= mod_val;
                    }
                }
            }
            memo[city][f] = ans % mod_val;
            ans % mod_val
        }

        let result = dfs(
            start as usize,
            fuel,
            &locations,
            finish as usize,
            &mut memo,
            MOD,
        );
        (result % MOD) as i32
    }
}
```

## Racket

```racket
(define/contract (count-routes locations start finish fuel)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((locs (list->vector locations))
         (n (vector-length locs))
         (MOD 1000000007)
         (dp (for/vector ([i (in-range n)]) (make-vector (+ fuel 1) #f))))
    (letrec
        ((dfs
          (lambda (city remaining)
            (define cached (vector-ref (vector-ref dp city) remaining))
            (if cached
                cached
                (begin
                  (define base (if (= city finish) 1 0))
                  (define total
                    (let loop ((j 0) (acc base))
                      (if (= j n)
                          acc
                          (if (= j city)
                              (loop (+ j 1) acc)
                              (let* ((cost (abs (- (vector-ref locs city)
                                                   (vector-ref locs j)))))
                                (if (<= cost remaining)
                                    (loop (+ j 1)
                                          (modulo (+ acc (dfs j (- remaining cost))) MOD))
                                    (loop (+ j 1) acc)))))))
                  (vector-set! (vector-ref dp city) remaining total)
                  total)))))
      (dfs start fuel))))
```

## Erlang

```erlang
-define(MOD, 1000000007).

-spec count_routes([integer()], integer(), integer(), integer()) -> integer().
count_routes(Locations, Start, Finish, Fuel) ->
    LocsT = list_to_tuple(Locations),
    {Ans, _} = dfs(Start, Fuel, LocsT, Finish, #{}, ?MOD),
    Ans rem ?MOD.

dfs(City, FuelLeft, LocsT, Finish, Memo, Mod) ->
    Key = {City, FuelLeft},
    case maps:find(Key, Memo) of
        {ok, Val} -> {Val, Memo};
        error ->
            Base = if City == Finish -> 1; true -> 0 end,
            Size = tuple_size(LocsT),
            {Sum, NewMemo} = loop(0, Size - 1, Base, FuelLeft, City, LocsT, Finish, Memo, Mod),
            UpdatedMemo = maps:put(Key, Sum rem Mod, NewMemo),
            {Sum rem Mod, UpdatedMemo}
    end.

loop(Index, Max, Acc, _FuelLeft, _City, _LocsT, _Finish, Memo, _Mod) when Index > Max ->
    {Acc rem ?MOD, Memo};
loop(Index, Max, Acc, FuelLeft, City, LocsT, Finish, Memo, Mod) ->
    if
        Index =:= City ->
            loop(Index + 1, Max, Acc, FuelLeft, City, LocsT, Finish, Memo, Mod);
        true ->
            Dist = erlang:abs(element(City + 1, LocsT) - element(Index + 1, LocsT)),
            if
                Dist =< FuelLeft ->
                    {SubCount, UpdatedMemo} = dfs(Index, FuelLeft - Dist, LocsT, Finish, Memo, Mod),
                    NewAcc = (Acc + SubCount) rem Mod,
                    loop(Index + 1, Max, NewAcc, FuelLeft, City, LocsT, Finish, UpdatedMemo, Mod);
                true ->
                    loop(Index + 1, Max, Acc, FuelLeft, City, LocsT, Finish, Memo, Mod)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec count_routes([integer], integer, integer, integer) :: integer
  def count_routes(locations, start, finish, fuel) do
    {ans, _} = dfs(start, fuel, locations, finish, %{})
    rem(ans, @mod)
  end

  defp dfs(i, f, locs, finish, memo) do
    case Map.get(memo, {i, f}) do
      nil ->
        base = if i == finish, do: 1, else: 0
        n = length(locs)

        {total, memo2} =
          Enum.reduce(0..(n - 1), {base, memo}, fn j, {acc, mem} ->
            if j != i do
              cost = abs(Enum.at(locs, i) - Enum.at(locs, j))

              if cost <= f do
                {cnt, mem2} = dfs(j, f - cost, locs, finish, mem)
                new_acc = rem(acc + cnt, @mod)
                {new_acc, mem2}
              else
                {acc, mem}
              end
            else
              {acc, mem}
            end
          end)

        memo_final = Map.put(memo2, {i, f}, total)
        {total, memo_final}

      val ->
        {val, memo}
    end
  end
end
```
