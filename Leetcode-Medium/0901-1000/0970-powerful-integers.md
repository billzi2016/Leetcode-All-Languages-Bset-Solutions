# 0970. Powerful Integers

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> powerfulIntegers(int x, int y, int bound) {
        unordered_set<int> result;
        if (bound < 2) return {};
        
        vector<long long> xs, ys;
        long long cur = 1;
        while (cur <= bound) {
            xs.push_back(cur);
            if (x == 1) break;
            cur *= x;
        }
        cur = 1;
        while (cur <= bound) {
            ys.push_back(cur);
            if (y == 1) break;
            cur *= y;
        }
        
        for (long long a : xs) {
            for (long long b : ys) {
                long long sum = a + b;
                if (sum <= bound) result.insert((int)sum);
            }
        }
        return vector<int>(result.begin(), result.end());
    }
};
```

## Java

```java
class Solution {
    public List<Integer> powerfulIntegers(int x, int y, int bound) {
        Set<Integer> set = new HashSet<>();
        long xi = 1;
        while (xi <= bound) {
            long yj = 1;
            while (xi + yj <= bound) {
                set.add((int)(xi + yj));
                if (y == 1) break;
                yj *= y;
            }
            if (x == 1) break;
            xi *= x;
        }
        return new ArrayList<>(set);
    }
}
```

## Python

```python
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        if bound < 2:
            return []
        xs = [1]
        if x != 1:
            val = 1
            while val * x <= bound:
                val *= x
                xs.append(val)
        ys = [1]
        if y != 1:
            val = 1
            while val * y <= bound:
                val *= y
                ys.append(val)
        res = set()
        for a in xs:
            for b in ys:
                s = a + b
                if s <= bound:
                    res.add(s)
        return list(res)
```

## Python3

```python
from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound < 2:
            return []
        
        xs = [1]
        if x != 1:
            val = 1
            while True:
                val *= x
                if val > bound:
                    break
                xs.append(val)
        
        ys = [1]
        if y != 1:
            val = 1
            while True:
                val *= y
                if val > bound:
                    break
                ys.append(val)
        
        result = set()
        for a in xs:
            for b in ys:
                s = a + b
                if s <= bound:
                    result.add(s)
        return list(result)
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* powerfulIntegers(int x, int y, int bound, int* returnSize) {
    // Maximum possible distinct values is small (<= 500), allocate enough space.
    int capacity = 512;
    int *result = (int *)malloc(sizeof(int) * capacity);
    int cnt = 0;

    if (bound < 2) {               // smallest possible sum is 1^0 + 1^0 = 2
        *returnSize = 0;
        return result;             // empty list
    }

    long long curX = 1;
    while (curX <= bound) {
        long long curY = 1;
        while (curX + curY <= bound) {
            int val = (int)(curX + curY);
            // check duplicate
            int dup = 0;
            for (int i = 0; i < cnt; ++i) {
                if (result[i] == val) { dup = 1; break; }
            }
            if (!dup) {
                if (cnt >= capacity) {
                    capacity *= 2;
                    result = (int *)realloc(result, sizeof(int) * capacity);
                }
                result[cnt++] = val;
            }

            if (y == 1) break;          // avoid infinite loop when y==1
            curY *= y;
        }

        if (x == 1) break;              // avoid infinite loop when x==1
        curX *= x;
    }

    *returnSize = cnt;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> PowerfulIntegers(int x, int y, int bound) {
        var xs = new List<int>();
        var ys = new List<int>();

        // Generate powers of x up to bound
        long cur = 1;
        while (cur <= bound) {
            xs.Add((int)cur);
            if (x == 1) break;
            cur *= x;
        }

        // Generate powers of y up to bound
        cur = 1;
        while (cur <= bound) {
            ys.Add((int)cur);
            if (y == 1) break;
            cur *= y;
        }

        var resultSet = new HashSet<int>();
        foreach (int a in xs) {
            foreach (int b in ys) {
                int sum = a + b;
                if (sum <= bound) {
                    resultSet.Add(sum);
                }
            }
        }

        return new List<int>(resultSet);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} x
 * @param {number} y
 * @param {number} bound
 * @return {number[]}
 */
var powerfulIntegers = function(x, y, bound) {
    const result = new Set();

    // generate all possible powers of x up to bound
    const xs = [];
    if (x === 1) {
        xs.push(1);
    } else {
        let val = 1;
        while (val <= bound) {
            xs.push(val);
            val *= x;
        }
    }

    // generate all possible powers of y up to bound
    const ys = [];
    if (y === 1) {
        ys.push(1);
    } else {
        let val = 1;
        while (val <= bound) {
            ys.push(val);
            val *= y;
        }
    }

    for (const a of xs) {
        for (const b of ys) {
            const sum = a + b;
            if (sum <= bound) result.add(sum);
        }
    }

    return Array.from(result);
};
```

## Typescript

```typescript
function powerfulIntegers(x: number, y: number, bound: number): number[] {
    const xs: number[] = [];
    let curX = 1;
    while (curX <= bound) {
        xs.push(curX);
        if (x === 1) break;
        curX *= x;
    }

    const ys: number[] = [];
    let curY = 1;
    while (curY <= bound) {
        ys.push(curY);
        if (y === 1) break;
        curY *= y;
    }

    const result = new Set<number>();
    for (const a of xs) {
        for (const b of ys) {
            const sum = a + b;
            if (sum <= bound) {
                result.add(sum);
            }
        }
    }

    return Array.from(result);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $x
     * @param Integer $y
     * @param Integer $bound
     * @return Integer[]
     */
    function powerfulIntegers($x, $y, $bound) {
        $set = [];

        // Generate all possible powers of x up to bound
        $xs = [];
        if ($x == 1) {
            $xs[] = 1;
        } else {
            $val = 1;
            while ($val <= $bound) {
                $xs[] = $val;
                $val *= $x;
            }
        }

        // Generate all possible powers of y up to bound
        $ys = [];
        if ($y == 1) {
            $ys[] = 1;
        } else {
            $val = 1;
            while ($val <= $bound) {
                $ys[] = $val;
                $val *= $y;
            }
        }

        // Combine each pair and collect sums within bound
        foreach ($xs as $a) {
            foreach ($ys as $b) {
                $sum = $a + $b;
                if ($sum <= $bound) {
                    $set[$sum] = true;
                } else {
                    // Since $ys is increasing, further b will only increase sum
                    break;
                }
            }
        }

        return array_map('intval', array_keys($set));
    }
}
```

## Swift

```swift
class Solution {
    func powerfulIntegers(_ x: Int, _ y: Int, _ bound: Int) -> [Int] {
        var result = Set<Int>()
        
        var xs = [Int]()
        var curX = 1
        while true {
            xs.append(curX)
            if x == 1 { break }
            curX *= x
            if curX > bound { break }
        }
        
        var ys = [Int]()
        var curY = 1
        while true {
            ys.append(curY)
            if y == 1 { break }
            curY *= y
            if curY > bound { break }
        }
        
        for xv in xs {
            for yv in ys {
                let sum = xv + yv
                if sum <= bound {
                    result.insert(sum)
                }
            }
        }
        
        return Array(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun powerfulIntegers(x: Int, y: Int, bound: Int): List<Int> {
        val res = mutableSetOf<Int>()
        var xi = 1L
        while (xi <= bound) {
            var yj = 1L
            while (xi + yj <= bound) {
                res.add((xi + yj).toInt())
                if (y == 1) break
                yj *= y.toLong()
            }
            if (x == 1) break
            xi *= x.toLong()
        }
        return res.toList()
    }
}
```

## Dart

```dart
class Solution {
  List<int> powerfulIntegers(int x, int y, int bound) {
    Set<int> result = {};
    if (bound < 2) return [];

    int xi = 1;
    while (xi <= bound) {
      int yj = 1;
      while (xi + yj <= bound) {
        result.add(xi + yj);
        if (y == 1) break;
        yj *= y;
      }
      if (x == 1) break;
      xi *= x;
    }

    return result.toList();
  }
}
```

## Golang

```go
func powerfulIntegers(x int, y int, bound int) []int {
	if bound < 2 {
		return []int{}
	}
	xPows := []int{}
	val := 1
	for {
		xPows = append(xPows, val)
		if x == 1 {
			break
		}
		if val > bound/x {
			break
		}
		val *= x
	}

	yPows := []int{}
	val = 1
	for {
		yPows = append(yPows, val)
		if y == 1 {
			break
		}
		if val > bound/y {
			break
		}
		val *= y
	}

	resultSet := make(map[int]struct{})
	for _, a := range xPows {
		for _, b := range yPows {
			sum := a + b
			if sum > bound {
				break
			}
			resultSet[sum] = struct{}{}
		}
	}

	res := make([]int, 0, len(resultSet))
	for v := range resultSet {
		res = append(res, v)
	}
	return res
}
```

## Ruby

```ruby
def powerful_integers(x, y, bound)
  powers_x = []
  val = 1
  loop do
    powers_x << val
    break if x == 1
    val *= x
    break if val > bound
  end

  powers_y = []
  val = 1
  loop do
    powers_y << val
    break if y == 1
    val *= y
    break if val > bound
  end

  result = {}
  powers_x.each do |a|
    powers_y.each do |b|
      sum = a + b
      next if sum > bound
      result[sum] = true
    end
  end
  result.keys
end
```

## Scala

```scala
object Solution {
  def powerfulIntegers(x: Int, y: Int, bound: Int): List[Int] = {
    if (bound < 2) return List.empty[Int]

    val xs: List[Long] = if (x == 1) List(1L) else {
      var lst = List.empty[Long]
      var cur = 1L
      while (cur <= bound) {
        lst ::= cur
        cur *= x
      }
      lst.reverse
    }

    val ys: List[Long] = if (y == 1) List(1L) else {
      var lst = List.empty[Long]
      var cur = 1L
      while (cur <= bound) {
        lst ::= cur
        cur *= y
      }
      lst.reverse
    }

    val result = scala.collection.mutable.Set[Int]()
    for (a <- xs; b <- ys) {
      val sum = a + b
      if (sum <= bound) result += sum.toInt
    }
    result.toList
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn powerful_integers(x: i32, y: i32, bound: i32) -> Vec<i32> {
        let mut xs = Vec::new();
        let mut cur = 1_i64;
        loop {
            xs.push(cur);
            if x == 1 { break; }
            cur *= x as i64;
            if cur > bound as i64 { break; }
        }

        let mut ys = Vec::new();
        let mut cur = 1_i64;
        loop {
            ys.push(cur);
            if y == 1 { break; }
            cur *= y as i64;
            if cur > bound as i64 { break; }
        }

        let mut set = HashSet::new();
        for &a in &xs {
            for &b in &ys {
                let sum = a + b;
                if sum <= bound as i64 {
                    set.insert(sum as i32);
                }
            }
        }

        set.into_iter().collect()
    }
}
```

## Racket

```racket
(require racket/contract)

(define/contract (powerful-integers x y bound)
  (-> exact-integer? exact-integer? exact-integer? (listof exact-integer?))
  (let ((result (make-hash)))
    (let loop-x ((px 1))
      (when (<= px bound)
        (let loop-y ((py 1))
          (when (<= (+ px py) bound)
            (hash-set! result (+ px py) #t))
          (if (= y 1)
              (void)
              (let ((nexty (* py y)))
                (when (<= nexty bound)
                  (loop-y nexty)))))
        (if (= x 1)
            (void)
            (let ((nextx (* px x)))
              (when (<= nextx bound)
                (loop-x nextx))))))
    (hash-keys result)))
```

## Erlang

```erlang
-spec powerful_integers(integer(), integer(), integer()) -> [integer()].
powerful_integers(X, Y, Bound) ->
    if
        Bound < 2 -> [];
        true ->
            XPs = gen_powers(X, Bound),
            YPs = gen_powers(Y, Bound),
            Map = build_map(XPs, YPs, Bound, #{}),
            maps:keys(Map)
    end.

gen_powers(Base, Bound) when Base =:= 1 ->
    [1];
gen_powers(Base, Bound) ->
    gen_powers_loop(1, Base, Bound, []).

gen_powers_loop(Current, Base, Bound, Acc) when Current =< Bound ->
    NewAcc = [Current | Acc],
    Next = Current * Base,
    gen_powers_loop(Next, Base, Bound, NewAcc);
gen_powers_loop(_, _, _, Acc) ->
    lists:reverse(Acc).

build_map([], _YPs, _Bound, Map) -> Map;
build_map([XP|RestX], YPs, Bound, Map0) ->
    Map1 = add_sums(XP, YPs, Bound, Map0),
    build_map(RestX, YPs, Bound, Map1).

add_sums(_XP, [], _Bound, Map) -> Map;
add_sums(XP, [YP|RestY], Bound, Map0) ->
    Sum = XP + YP,
    Map1 = if Sum =< Bound -> maps:put(Sum, true, Map0); true -> Map0 end,
    add_sums(XP, RestY, Bound, Map1).
```

## Elixir

```elixir
defmodule Solution do
  @spec powerful_integers(x :: integer, y :: integer, bound :: integer) :: [integer]
  def powerful_integers(x, y, bound) do
    xs = powers(x, bound)
    ys = powers(y, bound)

    Enum.reduce(xs, MapSet.new(), fn xv, acc ->
      Enum.reduce(ys, acc, fn yv, acc2 ->
        sum = xv + yv
        if sum <= bound, do: MapSet.put(acc2, sum), else: acc2
      end)
    end)
    |> MapSet.to_list()
  end

  defp powers(1, _bound), do: [1]

  defp powers(base, bound) when base > 0 do
    Stream.unfold(1, fn cur ->
      if cur > bound do
        nil
      else
        {cur, cur * base}
      end
    end)
    |> Enum.to_list()
  end
end
```
