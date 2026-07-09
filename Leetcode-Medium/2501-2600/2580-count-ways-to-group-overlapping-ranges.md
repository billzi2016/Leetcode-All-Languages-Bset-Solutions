# 2580. Count Ways to Group Overlapping Ranges

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1000000007;
    
    long long modPow(long long base, long long exp) {
        long long res = 1;
        while (exp > 0) {
            if (exp & 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return res;
    }
    
    int countWays(vector<vector<int>>& ranges) {
        if (ranges.empty()) return 1;
        sort(ranges.begin(), ranges.end(),
             [](const vector<int>& a, const vector<int>& b){
                 if (a[0] != b[0]) return a[0] < b[0];
                 return a[1] < b[1];
             });
        
        int components = 1;
        long long curEnd = ranges[0][1];
        for (size_t i = 1; i < ranges.size(); ++i) {
            if (ranges[i][0] <= curEnd) {
                curEnd = max<long long>(curEnd, ranges[i][1]);
            } else {
                ++components;
                curEnd = ranges[i][1];
            }
        }
        return (int)modPow(2, components);
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    
    public int countWays(int[][] ranges) {
        java.util.Arrays.sort(ranges, (a, b) -> Integer.compare(a[0], b[0]));
        int components = 0;
        long curEnd = -1;
        for (int[] r : ranges) {
            if (components == 0 || r[0] > curEnd) {
                components++;
                curEnd = r[1];
            } else {
                curEnd = Math.max(curEnd, (long) r[1]);
            }
        }
        long result = 1;
        long base = 2;
        int exp = components;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * base) % MOD;
            }
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def countWays(self, ranges):
        """
        :type ranges: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        if not ranges:
            return 1
        ranges.sort(key=lambda x: x[0])
        components = 0
        cur_end = -1
        for start, end in ranges:
            if start > cur_end:
                components += 1
                cur_end = end
            else:
                if end > cur_end:
                    cur_end = end
        return pow(2, components, MOD)
```

## Python3

```python
from typing import List

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        ranges.sort(key=lambda x: (x[0], x[1]))
        components = 0
        cur_end = -1
        for s, e in ranges:
            if s > cur_end:
                components += 1
                cur_end = e
            else:
                if e > cur_end:
                    cur_end = e
        return pow(2, components, MOD)
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007

typedef struct {
    int start;
    int end;
} Interval;

static int cmpInterval(const void *a, const void *b) {
    const Interval *ia = (const Interval *)a;
    const Interval *ib = (const Interval *)b;
    if (ia->start != ib->start)
        return ia->start - ib->start;
    return ia->end - ib->end;
}

static long long modPow(long long base, long long exp) {
    long long res = 1 % MOD;
    while (exp) {
        if (exp & 1LL) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1LL;
    }
    return res;
}

int countWays(int** ranges, int rangesSize, int* rangesColSize){
    if (rangesSize == 0) return 1; // no intervals, only one way

    Interval *arr = (Interval *)malloc(sizeof(Interval) * rangesSize);
    for (int i = 0; i < rangesSize; ++i) {
        arr[i].start = ranges[i][0];
        arr[i].end   = ranges[i][1];
    }

    qsort(arr, rangesSize, sizeof(Interval), cmpInterval);

    int components = 0;
    long long curEnd = arr[0].end;

    for (int i = 1; i < rangesSize; ++i) {
        if ((long long)arr[i].start > curEnd) {
            components++;
            curEnd = arr[i].end;
        } else {
            if (arr[i].end > curEnd) curEnd = arr[i].end;
        }
    }

    int totalComponents = components + 1; // include the first component
    long long ans = modPow(2LL, totalComponents);

    free(arr);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int CountWays(int[][] ranges) {
        const int MOD = 1000000007;
        Array.Sort(ranges, (a, b) => {
            if (a[0] == b[0]) return a[1].CompareTo(b[1]);
            return a[0].CompareTo(b[0]);
        });

        long curEnd = -1;
        int components = 0;

        foreach (var r in ranges) {
            int start = r[0];
            int end = r[1];
            if (start > curEnd) {
                components++;
                curEnd = end;
            } else {
                if (end > curEnd) curEnd = end;
            }
        }

        long ans = 1, baseVal = 2;
        int exp = components;
        while (exp > 0) {
            if ((exp & 1) == 1) ans = (ans * baseVal) % MOD;
            baseVal = (baseVal * baseVal) % MOD;
            exp >>= 1;
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} ranges
 * @return {number}
 */
var countWays = function(ranges) {
    const MOD = 1000000007n;
    if (ranges.length === 0) return 1; // not needed per constraints
    
    ranges.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
    
    let components = 0;
    let curEnd = -1;
    
    for (let i = 0; i < ranges.length; ++i) {
        const [s, e] = ranges[i];
        if (components === 0 || s > curEnd) { // start new component
            components++;
            curEnd = e;
        } else { // overlap with current component
            if (e > curEnd) curEnd = e;
        }
    }
    
    let exp = BigInt(components);
    let base = 2n;
    let result = 1n;
    while (exp > 0n) {
        if (exp & 1n) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1n;
    }
    
    return Number(result);
};
```

## Typescript

```typescript
function countWays(ranges: number[][]): number {
    const MOD = 1000000007;
    ranges.sort((a, b) => a[0] - b[0]);

    let components = 0;
    let curEnd = -1;

    for (let i = 0; i < ranges.length; i++) {
        const [s, e] = ranges[i];
        if (components === 0) {
            components = 1;
            curEnd = e;
        } else {
            if (s <= curEnd) {
                if (e > curEnd) curEnd = e;
            } else {
                components++;
                curEnd = e;
            }
        }
    }

    let ans = 1;
    for (let i = 0; i < components; i++) {
        ans = (ans * 2) % MOD;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $ranges
     * @return Integer
     */
    function countWays($ranges) {
        $mod = 1000000007;
        usort($ranges, function($a, $b) {
            if ($a[0] == $b[0]) {
                return $a[1] <=> $b[1];
            }
            return $a[0] <=> $b[0];
        });

        $n = count($ranges);
        if ($n == 0) {
            return 1; // empty set, only one way (both groups empty)
        }

        $components = 1;
        $curEnd = $ranges[0][1];

        for ($i = 1; $i < $n; ++$i) {
            $s = $ranges[$i][0];
            $e = $ranges[$i][1];
            if ($s <= $curEnd) {
                // overlapping, merge
                if ($e > $curEnd) {
                    $curEnd = $e;
                }
            } else {
                // new component
                $components++;
                $curEnd = $e;
            }
        }

        return $this->modPow(2, $components, $mod);
    }

    private function modPow($base, $exp, $mod) {
        $result = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD = 1_000_000_007

    func countWays(_ ranges: [[Int]]) -> Int {
        if ranges.isEmpty { return 1 }
        let sorted = ranges.sorted {
            if $0[0] == $1[0] { return $0[1] < $1[1] }
            return $0[0] < $1[0]
        }

        var components = 0
        var curEnd = sorted[0][1]

        for i in 1..<sorted.count {
            let start = sorted[i][0]
            let end = sorted[i][1]
            if start > curEnd {          // new non‑overlapping component
                components += 1
                curEnd = end
            } else {
                curEnd = max(curEnd, end) // merge into current component
            }
        }
        components += 1   // count the last component

        var result: Int64 = 1
        var base: Int64 = 2
        var exp = components
        let mod = Int64(MOD)

        while exp > 0 {
            if exp & 1 == 1 {
                result = (result * base) % mod
            }
            base = (base * base) % mod
            exp >>= 1
        }

        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countWays(ranges: Array<IntArray>): Int {
        val MOD = 1_000_000_007L
        if (ranges.isEmpty()) return 1

        val sorted = ranges.sortedWith(compareBy<IntArray> { it[0] }.thenBy { it[1] })

        var components = 0
        var curEnd = -1L

        for (interval in sorted) {
            val start = interval[0].toLong()
            val end = interval[1].toLong()
            if (components == 0 || start > curEnd) {
                // start a new merged component
                components++
                curEnd = end
            } else {
                // extend current merged component
                if (end > curEnd) curEnd = end
            }
        }

        var result = 1L
        var base = 2L
        var exp = components
        while (exp > 0) {
            if ((exp and 1) == 1) {
                result = (result * base) % MOD
            }
            base = (base * base) % MOD
            exp = exp shr 1
        }

        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int countWays(List<List<int>> ranges) {
    if (ranges.isEmpty) return 1;
    ranges.sort((a, b) => a[0].compareTo(b[0]));

    int components = 1;
    int curEnd = ranges[0][1];

    for (int i = 1; i < ranges.length; i++) {
      int s = ranges[i][0];
      int e = ranges[i][1];
      if (s > curEnd) {
        components++;
        curEnd = e;
      } else if (e > curEnd) {
        curEnd = e;
      }
    }

    int result = 1;
    int base = 2;
    int exp = components;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * base) % _mod;
      }
      base = (base * base) % _mod;
      exp >>= 1;
    }
    return result;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

const MOD int64 = 1000000007

func countWays(ranges [][]int) int {
	if len(ranges) == 0 {
		return 1
	}
	sort.Slice(ranges, func(i, j int) bool {
		if ranges[i][0] == ranges[j][0] {
			return ranges[i][1] < ranges[j][1]
		}
		return ranges[i][0] < ranges[j][0]
	})

	comp := 0
	curStart, curEnd := -1, -1
	for _, r := range ranges {
		start, end := r[0], r[1]
		if comp == 0 && curStart == -1 { // first interval initialization
			curStart, curEnd = start, end
			comp = 1
			continue
		}
		if start > curEnd {
			// new component
			comp++
			curStart, curEnd = start, end
		} else {
			if end > curEnd {
				curEnd = end
			}
		}
	}

	// compute 2^comp mod MOD
	res := int64(1)
	base := int64(2)
	exp := int64(comp)
	for exp > 0 {
		if exp&1 == 1 {
			res = (res * base) % MOD
		}
		base = (base * base) % MOD
		exp >>= 1
	}
	return int(res)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(base, exp, mod)
  result = 1
  b = base % mod
  e = exp
  while e > 0
    result = (result * b) % mod if (e & 1) == 1
    b = (b * b) % mod
    e >>= 1
  end
  result
end

def count_ways(ranges)
  sorted = ranges.sort_by { |s, _| s }
  components = 0
  cur_end = -1
  sorted.each do |s, e|
    if s > cur_end
      components += 1
      cur_end = e
    else
      cur_end = e if e > cur_end
    end
  end
  mod_pow(2, components, MOD)
end
```

## Scala

```scala
object Solution {
  private val MOD = 1000000007L

  def countWays(ranges: Array[Array[Int]]): Int = {
    if (ranges.isEmpty) return 1
    val sorted = ranges.sortBy(arr => (arr(0), arr(1)))
    var components = 1
    var curEnd = sorted(0)(1).toLong

    var i = 1
    while (i < sorted.length) {
      val start = sorted(i)(0).toLong
      val end   = sorted(i)(1).toLong
      if (start > curEnd) {
        components += 1
        curEnd = end
      } else {
        if (end > curEnd) curEnd = end
      }
      i += 1
    }

    modPow(2L, components, MOD).toInt
  }

  private def modPow(base: Long, exp: Int, mod: Long): Long = {
    var b = base % mod
    var e = exp
    var res = 1L
    while (e > 0) {
      if ((e & 1) == 1) res = (res * b) % mod
      b = (b * b) % mod
      e >>= 1
    }
    res
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_ways(ranges: Vec<Vec<i32>>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        if ranges.is_empty() {
            return 1;
        }
        let mut intervals = ranges;
        intervals.sort_by(|a, b| a[0].cmp(&b[0]));
        let mut components: i64 = 0;
        let mut cur_start = intervals[0][0] as i64;
        let mut cur_end = intervals[0][1] as i64;
        for i in 1..intervals.len() {
            let s = intervals[i][0] as i64;
            let e = intervals[i][1] as i64;
            if s > cur_end {
                components += 1;
                cur_start = s;
                cur_end = e;
            } else if e > cur_end {
                cur_end = e;
            }
        }
        components += 1; // last merged interval

        let mut result: i64 = 1;
        let mut base: i64 = 2;
        let mut exp = components;
        while exp > 0 {
            if exp & 1 == 1 {
                result = result * base % MOD;
            }
            base = base * base % MOD;
            exp >>= 1;
        }
        result as i32
    }
}
```

## Racket

```racket
(require racket/list)

(define MOD 1000000007)

(: pow-mod (Integer Integer -> Integer))
(define (pow-mod base exp)
  (let loop ((b (modulo base MOD)) (e exp) (res 1))
    (if (= e 0)
        res
        (let ((res2 (if (odd? e) (modulo (* res b) MOD) res)))
          (loop (modulo (* b b) MOD) (quotient e 2) res2)))))

(define/contract (count-ways ranges)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((sorted
           (sort ranges
                 (lambda (a b)
                   (or (< (first a) (first b))
                       (and (= (first a) (first b))
                            (< (second a) (second b)))))))
         (components
          (let loop ((lst sorted) (cur-end -1) (cnt 0))
            (if (null? lst)
                cnt
                (let* ((rng (car lst))
                       (s (first rng))
                       (e (second rng)))
                  (if (> s cur-end)
                      (loop (cdr lst) e (+ cnt 1))      ; new component
                      (loop (cdr lst) (max cur-end e) cnt)))))))
    (pow-mod 2 components)))
```

## Erlang

```erlang
-module(solution).
-export([count_ways/1]).

-define(MOD, 1000000007).

-spec count_ways(Ranges :: [[integer()]]) -> integer().
count_ways(Ranges) ->
    Sorted = lists:sort(fun([S1,_],[S2,_]) -> S1 =< S2 end, Ranges),
    Components = case Sorted of
        [] -> 0;
        [[Start, End]|Rest] ->
            loop(Rest, End, 1)
    end,
    powmod(2, Components, ?MOD).

loop([], _CurMax, Count) -> Count;
loop([[S,E]|Rest], CurMax, Count) ->
    if S > CurMax ->
            loop(Rest, E, Count + 1);
       true ->
            NewMax = erlang:max(CurMax, E),
            loop(Rest, NewMax, Count)
    end.

powmod(Base, Exp, Mod) ->
    powmod_loop(Base rem Mod, Exp, 1, Mod).

powmod_loop(_, 0, Acc, _Mod) -> Acc;
powmod_loop(B, E, Acc, Mod) ->
    Acc1 = case (E band 1) of
        1 -> (Acc * B) rem Mod;
        _ -> Acc
    end,
    B2 = (B * B) rem Mod,
    powmod_loop(B2, E bsr 1, Acc1, Mod).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @moduledoc false
  @spec count_ways(ranges :: [[integer]]) :: integer
  def count_ways(ranges) do
    mod = 1_000_000_007

    sorted = Enum.sort_by(ranges, fn [s, _] -> s end)

    {components, _} =
      Enum.reduce(sorted, {0, nil}, fn [s, e], {cnt, cur} ->
        case cur do
          nil ->
            {cnt + 1, {s, e}}

          {c_start, c_end} ->
            if s > c_end do
              {cnt + 1, {s, e}}
            else
              {cnt, {c_start, max(c_end, e)}}
            end
        end
      end)

    pow_mod(2, components, mod)
  end

  defp pow_mod(_base, 0, _mod), do: 1

  defp pow_mod(base, exp, mod) do
    do_pow(rem(base, mod), exp, mod, 1)
  end

  defp do_pow(_base, 0, _mod, acc), do: acc

  defp do_pow(base, exp, mod, acc) do
    acc = if (exp &&& 1) == 1, do: rem(acc * base, mod), else: acc
    base = rem(base * base, mod)
    do_pow(base, exp >>> 1, mod, acc)
  end
end
```
