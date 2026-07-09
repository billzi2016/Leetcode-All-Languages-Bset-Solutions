# 1362. Closest Divisors

## Cpp

```cpp
class Solution {
public:
    vector<int> closestDivisors(int num) {
        auto getPair = [&](long long n) -> pair<int,int> {
            long long a = sqrt((double)n);
            while (a * a > n) --a;
            while (n % a != 0) --a;
            long long b = n / a;
            return {(int)a, (int)b};
        };
        
        pair<int,int> best = {0, INT_MAX}; // diff will be large
        for (long long t = (long long)num + 1; t <= (long long)num + 2; ++t) {
            auto p = getPair(t);
            int diff = p.second - p.first;
            if (diff < best.second - best.first) {
                best = p;
            }
        }
        return {best.first, best.second};
    }
};
```

## Java

```java
class Solution {
    public int[] closestDivisors(int num) {
        int bestA = 0, bestB = 0;
        long minDiff = Long.MAX_VALUE;
        for (int add = 1; add <= 2; add++) {
            long target = (long) num + add;
            long sqrt = (long) Math.sqrt(target);
            for (long i = sqrt; i >= 1; i--) {
                if (target % i == 0) {
                    long a = i;
                    long b = target / i;
                    long diff = b - a;
                    if (diff < minDiff) {
                        minDiff = diff;
                        bestA = (int) a;
                        bestB = (int) b;
                    }
                    break; // closest pair for this target found
                }
            }
        }
        return new int[]{bestA, bestB};
    }
}
```

## Python

```python
import math

class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def best_pair(n):
            r = int(math.isqrt(n))
            for d in range(r, 0, -1):
                if n % d == 0:
                    return [d, n // d]
            return [1, n]

        pair1 = best_pair(num + 1)
        pair2 = best_pair(num + 2)

        diff1 = abs(pair1[0] - pair1[1])
        diff2 = abs(pair2[0] - pair2[1])

        return pair1 if diff1 <= diff2 else pair2
```

## Python3

```python
import math
from typing import List

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        best_pair = []
        min_diff = float('inf')
        for target in (num + 1, num + 2):
            root = int(math.isqrt(target))
            for d in range(root, 0, -1):
                if target % d == 0:
                    a, b = d, target // d
                    diff = b - a
                    if diff < min_diff:
                        min_diff = diff
                        best_pair = [a, b]
                    break
        return best_pair
```

## C

```c
#include <stdlib.h>
#include <math.h>
#include <limits.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* closestDivisors(int num, int* returnSize) {
    *returnSize = 2;
    int* ans = (int*)malloc(2 * sizeof(int));
    long long bestDiff = LLONG_MAX;

    for (int add = 1; add <= 2; ++add) {
        long long target = (long long)num + add;
        long long sq = (long long)sqrt((double)target);
        for (long long i = sq; i >= 1; --i) {
            if (target % i == 0) {
                long long j = target / i;
                long long diff = llabs(i - j);
                if (diff < bestDiff) {
                    bestDiff = diff;
                    ans[0] = (int)i;
                    ans[1] = (int)j;
                }
                break; // closest pair for this target found
            }
        }
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] ClosestDivisors(int num)
    {
        long n1 = (long)num + 1;
        long n2 = (long)num + 2;

        int[] pair1 = GetClosestPair(n1);
        int[] pair2 = GetClosestPair(n2);

        int diff1 = Math.Abs(pair1[0] - pair1[1]);
        int diff2 = Math.Abs(pair2[0] - pair2[1]);

        return diff1 <= diff2 ? pair1 : pair2;
    }

    private int[] GetClosestPair(long n)
    {
        int sqrt = (int)Math.Sqrt(n);
        for (int i = sqrt; i >= 1; --i)
        {
            if (n % i == 0)
            {
                return new int[] { i, (int)(n / i) };
            }
        }
        // Fallback, should never reach because 1 always divides n
        return new int[] { 1, (int)n };
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {number[]}
 */
var closestDivisors = function(num) {
    const getClosest = (n) => {
        let i = Math.floor(Math.sqrt(n));
        for (; i >= 1; i--) {
            if (n % i === 0) {
                return [i, n / i];
            }
        }
        return [1, n];
    };
    
    const pair1 = getClosest(num + 1);
    const diff1 = Math.abs(pair1[0] - pair1[1]);
    
    const pair2 = getClosest(num + 2);
    const diff2 = Math.abs(pair2[0] - pair2[1]);
    
    return diff1 <= diff2 ? pair1 : pair2;
};
```

## Typescript

```typescript
function closestDivisors(num: number): number[] {
    const getClosest = (target: number): [number, number] => {
        let a = 1;
        let b = target;
        for (let i = Math.floor(Math.sqrt(target)); i >= 1; --i) {
            if (target % i === 0) {
                a = i;
                b = target / i;
                break;
            }
        }
        return [a, b];
    };
    
    const cand1 = getClosest(num + 1);
    const cand2 = getClosest(num + 2);
    
    const diff1 = Math.abs(cand1[0] - cand1[1]);
    const diff2 = Math.abs(cand2[0] - cand2[1]);
    
    return diff1 <= diff2 ? cand1 : cand2;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $num
     * @return Integer[]
     */
    function closestDivisors($num) {
        $pair1 = $this->closestPair($num + 1);
        $pair2 = $this->closestPair($num + 2);
        $diff1 = abs($pair1[0] - $pair1[1]);
        $diff2 = abs($pair2[0] - $pair2[1]);
        return $diff1 <= $diff2 ? $pair1 : $pair2;
    }

    private function closestPair(int $n): array {
        $i = (int)floor(sqrt($n));
        for (; $i >= 1; $i--) {
            if ($n % $i == 0) {
                return [$i, intdiv($n, $i)];
            }
        }
        return [1, $n];
    }
}
```

## Swift

```swift
class Solution {
    func closestDivisors(_ num: Int) -> [Int] {
        func bestPair(_ n: Int) -> [Int] {
            var i = Int(Double(n).squareRoot())
            while i >= 1 {
                if n % i == 0 {
                    return [i, n / i]
                }
                i -= 1
            }
            return []
        }
        
        let pair1 = bestPair(num + 1)
        let pair2 = bestPair(num + 2)
        
        let diff1 = abs(pair1[0] - pair1[1])
        let diff2 = abs(pair2[0] - pair2[1])
        
        return diff1 <= diff2 ? pair1 : pair2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun closestDivisors(num: Int): IntArray {
        var best = intArrayOf(0, 0)
        var minDiff = Int.MAX_VALUE
        for (add in 1..2) {
            val target = num + add
            var i = Math.sqrt(target.toDouble()).toInt()
            while (i >= 1) {
                if (target % i == 0) {
                    val a = i
                    val b = target / i
                    val diff = kotlin.math.abs(a - b)
                    if (diff < minDiff) {
                        minDiff = diff
                        best[0] = a
                        best[1] = b
                    }
                    break
                }
                i--
            }
        }
        return best
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  List<int> closestDivisors(int num) {
    List<int> _pair(int n) {
      int i = sqrt(n).toInt();
      for (; i >= 1; --i) {
        if (n % i == 0) {
          return [i, n ~/ i];
        }
      }
      return [1, n];
    }

    List<int> p1 = _pair(num + 1);
    List<int> p2 = _pair(num + 2);

    int diff1 = (p1[0] - p1[1]).abs();
    int diff2 = (p2[0] - p2[1]).abs();

    return diff1 <= diff2 ? p1 : p2;
  }
}
```

## Golang

```go
package main

import (
	"math"
)

func closestDivisors(num int) []int {
	get := func(t int) []int {
		sqrt := int(math.Sqrt(float64(t)))
		for i := sqrt; i >= 1; i-- {
			if t%i == 0 {
				return []int{i, t / i}
			}
		}
		return []int{1, t}
	}

	cand1 := get(num + 1)
	cand2 := get(num + 2)

	diff1 := abs(cand1[0] - cand1[1])
	diff2 := abs(cand2[0] - cand2[1])

	if diff1 <= diff2 {
		return cand1
	}
	return cand2
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
```

## Ruby

```ruby
def closest_divisors(num)
  best = nil
  best_diff = Float::INFINITY
  [num + 1, num + 2].each do |t|
    i = Math.sqrt(t).to_i
    while i > 0
      if t % i == 0
        a = i
        b = t / i
        diff = (b - a).abs
        if diff < best_diff
          best_diff = diff
          best = [a, b]
        end
        break
      end
      i -= 1
    end
  end
  best
end
```

## Scala

```scala
object Solution {
  def closestDivisors(num: Int): Array[Int] = {
    def pairFor(target: Long): Array[Int] = {
      var i = math.sqrt(target.toDouble).toLong
      while (i >= 1) {
        if (target % i == 0) {
          return Array(i.toInt, (target / i).toInt)
        }
        i -= 1
      }
      Array(1, target.toInt)
    }

    val p1 = pairFor(num.toLong + 1)
    val p2 = pairFor(num.toLong + 2)

    val diff1 = math.abs(p1(0) - p1(1))
    val diff2 = math.abs(p2(0) - p2(1))

    if (diff1 <= diff2) p1 else p2
  }
}
```

## Rust

```rust
impl Solution {
    pub fn closest_divisors(num: i32) -> Vec<i32> {
        let mut best_pair = (i32::MAX, i32::MAX);
        let mut min_diff = i32::MAX;
        for add in 1..=2 {
            let n = num as i64 + add as i64;
            let sqrt_n = (n as f64).sqrt() as i64;
            for i in (1..=sqrt_n).rev() {
                if n % i == 0 {
                    let a = i as i32;
                    let b = (n / i) as i32;
                    let diff = (b - a).abs();
                    if diff < min_diff {
                        min_diff = diff;
                        best_pair = (a, b);
                    }
                    break; // closest divisors for this n found
                }
            }
        }
        vec![best_pair.0, best_pair.1]
    }
}
```

## Racket

```racket
(define/contract (closest-divisors num)
  (-> exact-integer? (listof exact-integer?))
  (let* ((t1 (+ num 1))
         (t2 (+ num 2))
         (make-pair
          (lambda (n)
            (let loop ((i (inexact->exact (floor (sqrt n)))))
              (if (= (remainder n i) 0)
                  (list i (/ n i))
                  (loop (sub1 i))))))
         (pair1 (make-pair t1))
         (pair2 (make-pair t2))
         (diff1 (abs (- (first pair1) (second pair1))))
         (diff2 (abs (- (first pair2) (second pair2)))))
    (if (< diff1 diff2) pair1 pair2)))
```

## Erlang

```erlang
-module(solution).
-export([closest_divisors/1]).

-spec closest_divisors(Num :: integer()) -> [integer()].
closest_divisors(Num) ->
    N1 = Num + 1,
    N2 = Num + 2,
    Pair1 = find_pair(N1),
    Pair2 = find_pair(N2),
    {A1, B1} = Pair1,
    {A2, B2} = Pair2,
    Diff1 = erlang:abs(A1 - B1),
    Diff2 = erlang:abs(A2 - B2),
    case Diff1 =< Diff2 of
        true -> [A1, B1];
        false -> [A2, B2]
    end.

find_pair(N) ->
    S = trunc(math:sqrt(N)),
    find_pair(N, S).

find_pair(N, I) when I >= 1 ->
    case N rem I of
        0 -> {I, N div I};
        _ -> find_pair(N, I - 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec closest_divisors(num :: integer) :: [integer]
  def closest_divisors(num) do
    pair1 = find_pair(num + 1)
    pair2 = find_pair(num + 2)

    diff1 = abs(elem(pair1, 0) - elem(pair1, 1))
    diff2 = abs(elem(pair2, 0) - elem(pair2, 1))

    if diff1 <= diff2 do
      [elem(pair1, 0), elem(pair1, 1)]
    else
      [elem(pair2, 0), elem(pair2, 1)]
    end
  end

  defp find_pair(n) do
    limit = :math.sqrt(n) |> trunc()
    Enum.reduce_while(limit..1//-1, nil, fn i, _ ->
      if rem(n, i) == 0 do
        {:halt, {i, div(n, i)}}
      else
        {:cont, nil}
      end
    end)
  end
end
```
