# 0264. Ugly Number II

## Cpp

```cpp
class Solution {
public:
    int nthUglyNumber(int n) {
        std::vector<int> ugly(n);
        ugly[0] = 1;
        int i2 = 0, i3 = 0, i5 = 0;
        long next2 = 2, next3 = 3, next5 = 5;
        for (int i = 1; i < n; ++i) {
            long nextUgly = std::min(next2, std::min(next3, next5));
            ugly[i] = static_cast<int>(nextUgly);
            if (nextUgly == next2) {
                ++i2;
                next2 = 1L * ugly[i2] * 2;
            }
            if (nextUgly == next3) {
                ++i3;
                next3 = 1L * ugly[i3] * 3;
            }
            if (nextUgly == next5) {
                ++i5;
                next5 = 1L * ugly[i5] * 5;
            }
        }
        return ugly[n - 1];
    }
};
```

## Java

```java
class Solution {
    public int nthUglyNumber(int n) {
        int[] ugly = new int[n];
        ugly[0] = 1;
        int i2 = 0, i3 = 0, i5 = 0;
        int next2 = 2, next3 = 3, next5 = 5;
        for (int i = 1; i < n; i++) {
            int nextUgly = Math.min(next2, Math.min(next3, next5));
            ugly[i] = nextUgly;
            if (nextUgly == next2) {
                i2++;
                next2 = ugly[i2] * 2;
            }
            if (nextUgly == next3) {
                i3++;
                next3 = ugly[i3] * 3;
            }
            if (nextUgly == next5) {
                i5++;
                next5 = ugly[i5] * 5;
            }
        }
        return ugly[n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1] * n
        i2 = i3 = i5 = 0
        next2, next3, next5 = 2, 3, 5

        for idx in range(1, n):
            nxt = min(next2, next3, next5)
            ugly[idx] = nxt

            if nxt == next2:
                i2 += 1
                next2 = ugly[i2] * 2
            if nxt == next3:
                i3 += 1
                next3 = ugly[i3] * 3
            if nxt == next5:
                i5 += 1
                next5 = ugly[i5] * 5

        return ugly[-1]
```

## Python3

```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        i2 = i3 = i5 = 0
        next2, next3, next5 = 2, 3, 5

        for idx in range(1, n):
            nxt = min(next2, next3, next5)
            ugly[idx] = nxt

            if nxt == next2:
                i2 += 1
                next2 = ugly[i2] * 2
            if nxt == next3:
                i3 += 1
                next3 = ugly[i3] * 3
            if nxt == next5:
                i5 += 1
                next5 = ugly[i5] * 5

        return ugly[-1]
```

## C

```c
int nthUglyNumber(int n) {
    if (n <= 0) return 0;
    int *ugly = (int *)malloc(sizeof(int) * n);
    ugly[0] = 1;
    int i2 = 0, i3 = 0, i5 = 0;
    int next2 = 2, next3 = 3, next5 = 5;
    for (int i = 1; i < n; ++i) {
        int nextUgly = next2;
        if (next3 < nextUgly) nextUgly = next3;
        if (next5 < nextUgly) nextUgly = next5;
        ugly[i] = nextUgly;
        if (nextUgly == next2) {
            ++i2;
            long long val = (long long)ugly[i2] * 2;
            next2 = (int)val;
        }
        if (nextUgly == next3) {
            ++i3;
            long long val = (long long)ugly[i3] * 3;
            next3 = (int)val;
        }
        if (nextUgly == next5) {
            ++i5;
            long long val = (long long)ugly[i5] * 5;
            next5 = (int)val;
        }
    }
    int result = ugly[n - 1];
    free(ugly);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int NthUglyNumber(int n)
    {
        int[] ugly = new int[n];
        ugly[0] = 1;

        int i2 = 0, i3 = 0, i5 = 0;
        int next2 = 2, next3 = 3, next5 = 5;

        for (int i = 1; i < n; i++)
        {
            int nextUgly = Math.Min(next2, Math.Min(next3, next5));
            ugly[i] = nextUgly;

            if (nextUgly == next2)
            {
                i2++;
                next2 = ugly[i2] * 2;
            }
            if (nextUgly == next3)
            {
                i3++;
                next3 = ugly[i3] * 3;
            }
            if (nextUgly == next5)
            {
                i5++;
                next5 = ugly[i5] * 5;
            }
        }

        return ugly[n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function(n) {
    const ugly = new Array(n);
    ugly[0] = 1;
    let i2 = 0, i3 = 0, i5 = 0;
    let next2 = 2, next3 = 3, next5 = 5;

    for (let i = 1; i < n; i++) {
        const nextUgly = Math.min(next2, next3, next5);
        ugly[i] = nextUgly;

        if (nextUgly === next2) {
            i2++;
            next2 = ugly[i2] * 2;
        }
        if (nextUgly === next3) {
            i3++;
            next3 = ugly[i3] * 3;
        }
        if (nextUgly === next5) {
            i5++;
            next5 = ugly[i5] * 5;
        }
    }

    return ugly[n - 1];
};
```

## Typescript

```typescript
function nthUglyNumber(n: number): number {
    const ugly = new Array<number>(n);
    ugly[0] = 1;
    let i2 = 0, i3 = 0, i5 = 0;
    let next2 = 2, next3 = 3, next5 = 5;

    for (let i = 1; i < n; i++) {
        const nextUgly = Math.min(next2, next3, next5);
        ugly[i] = nextUgly;

        if (nextUgly === next2) {
            i2++;
            next2 = ugly[i2] * 2;
        }
        if (nextUgly === next3) {
            i3++;
            next3 = ugly[i3] * 3;
        }
        if (nextUgly === next5) {
            i5++;
            next5 = ugly[i5] * 5;
        }
    }

    return ugly[n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function nthUglyNumber($n) {
        if ($n == 1) return 1;
        $ugly = [1];
        $i2 = $i3 = $i5 = 0;

        for ($i = 1; $i < $n; $i++) {
            $next2 = $ugly[$i2] * 2;
            $next3 = $ugly[$i3] * 3;
            $next5 = $ugly[$i5] * 5;

            $nextUgly = min($next2, $next3, $next5);
            $ugly[] = $nextUgly;

            if ($nextUgly == $next2) $i2++;
            if ($nextUgly == $next3) $i3++;
            if ($nextUgly == $next5) $i5++;
        }

        return $ugly[$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func nthUglyNumber(_ n: Int) -> Int {
        if n == 1 { return 1 }
        var ugly = [Int](repeating: 0, count: n)
        ugly[0] = 1
        var i2 = 0, i3 = 0, i5 = 0
        var next2 = 2, next3 = 3, next5 = 5
        
        for idx in 1..<n {
            let nextUgly = min(next2, min(next3, next5))
            ugly[idx] = nextUgly
            
            if nextUgly == next2 {
                i2 += 1
                next2 = ugly[i2] * 2
            }
            if nextUgly == next3 {
                i3 += 1
                next3 = ugly[i3] * 3
            }
            if nextUgly == next5 {
                i5 += 1
                next5 = ugly[i5] * 5
            }
        }
        return ugly[n - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun nthUglyNumber(n: Int): Int {
        if (n == 1) return 1
        val ugly = IntArray(n)
        ugly[0] = 1
        var i2 = 0
        var i3 = 0
        var i5 = 0
        var next2 = 2
        var next3 = 3
        var next5 = 5

        for (i in 1 until n) {
            val nextUgly = minOf(next2, next3, next5)
            ugly[i] = nextUgly
            if (nextUgly == next2) {
                i2++
                next2 = ugly[i2] * 2
            }
            if (nextUgly == next3) {
                i3++
                next3 = ugly[i3] * 3
            }
            if (nextUgly == next5) {
                i5++
                next5 = ugly[i5] * 5
            }
        }
        return ugly[n - 1]
    }
}
```

## Dart

```dart
class Solution {
  int nthUglyNumber(int n) {
    List<int> ugly = List.filled(n, 0);
    ugly[0] = 1;
    int i2 = 0, i3 = 0, i5 = 0;
    int next2 = 2, next3 = 3, next5 = 5;

    for (int i = 1; i < n; i++) {
      int nextUgly = next2 < next3
          ? (next2 < next5 ? next2 : next5)
          : (next3 < next5 ? next3 : next5);
      ugly[i] = nextUgly;

      if (nextUgly == next2) {
        i2++;
        next2 = ugly[i2] * 2;
      }
      if (nextUgly == next3) {
        i3++;
        next3 = ugly[i3] * 3;
      }
      if (nextUgly == next5) {
        i5++;
        next5 = ugly[i5] * 5;
      }
    }

    return ugly[n - 1];
  }
}
```

## Golang

```go
func nthUglyNumber(n int) int {
	if n <= 0 {
		return 0
	}
	ugly := make([]int, n)
	ugly[0] = 1
	i2, i3, i5 := 0, 0, 0
	next2, next3, next5 := 2, 3, 5

	for i := 1; i < n; i++ {
		minVal := next2
		if next3 < minVal {
			minVal = next3
		}
		if next5 < minVal {
			minVal = next5
		}
		ugly[i] = minVal

		if minVal == next2 {
			i2++
			next2 = ugly[i2] * 2
		}
		if minVal == next3 {
			i3++
			next3 = ugly[i3] * 3
		}
		if minVal == next5 {
			i5++
			next5 = ugly[i5] * 5
		}
	}
	return ugly[n-1]
}
```

## Ruby

```ruby
def nth_ugly_number(n)
  return 1 if n == 1
  ugly = Array.new(n, 0)
  ugly[0] = 1
  i2 = i3 = i5 = 0
  next2 = 2
  next3 = 3
  next5 = 5

  (1...n).each do |i|
    nxt = [next2, next3, next5].min
    ugly[i] = nxt
    if nxt == next2
      i2 += 1
      next2 = ugly[i2] * 2
    end
    if nxt == next3
      i3 += 1
      next3 = ugly[i3] * 3
    end
    if nxt == next5
      i5 += 1
      next5 = ugly[i5] * 5
    end
  end

  ugly[-1]
end
```

## Scala

```scala
object Solution {
    def nthUglyNumber(n: Int): Int = {
        if (n == 1) return 1
        val ugly = new Array[Int](n)
        ugly(0) = 1
        var i2 = 0
        var i3 = 0
        var i5 = 0
        var next2 = 2
        var next3 = 3
        var next5 = 5

        for (i <- 1 until n) {
            val next = math.min(next2, math.min(next3, next5))
            ugly(i) = next
            if (next == next2) {
                i2 += 1
                next2 = ugly(i2) * 2
            }
            if (next == next3) {
                i3 += 1
                next3 = ugly(i3) * 3
            }
            if (next == next5) {
                i5 += 1
                next5 = ugly(i5) * 5
            }
        }
        ugly(n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn nth_ugly_number(n: i32) -> i32 {
        let n = n as usize;
        if n == 0 {
            return 0;
        }
        let mut ugly = vec![1i32; n];
        let (mut i2, mut i3, mut i5) = (0usize, 0usize, 0usize);
        let (mut next2, mut next3, mut next5) = (2i32, 3i32, 5i32);

        for idx in 1..n {
            let next = *[next2, next3, next5].iter().min().unwrap();
            ugly[idx] = next;

            if next == next2 {
                i2 += 1;
                next2 = ugly[i2] * 2;
            }
            if next == next3 {
                i3 += 1;
                next3 = ugly[i3] * 3;
            }
            if next == next5 {
                i5 += 1;
                next5 = ugly[i5] * 5;
            }
        }

        ugly[n - 1]
    }
}
```

## Racket

```racket
#lang racket

(define/contract (nth-ugly-number n)
  (-> exact-integer? exact-integer?)
  (let* ((n (max 1 n))
         (uglies (make-vector n))
         (i2 0) (i3 0) (i5 0))
    (vector-set! uglies 0 1)
    (for ([idx (in-range 1 n)])
      (define next2 (* 2 (vector-ref uglies i2)))
      (define next3 (* 3 (vector-ref uglies i3)))
      (define next5 (* 5 (vector-ref uglies i5)))
      (define next (min next2 next3 next5))
      (vector-set! uglies idx next)
      (when (= next next2) (set! i2 (+ i2 1)))
      (when (= next next3) (set! i3 (+ i3 1)))
      (when (= next next5) (set! i5 (+ i5 1))))
    (vector-ref uglies (- n 1))))
```

## Erlang

```erlang
-module(solution).
-export([nth_ugly_number/1]).

-spec nth_ugly_number(N :: integer()) -> integer().
nth_ugly_number(1) ->
    1;
nth_ugly_number(N) when N > 1 ->
    UglyList = generate(N, [1], 0, 0, 0),
    lists:last(UglyList).

generate(N, UglyList, I2, I3, I5) when length(UglyList) == N ->
    UglyList;
generate(N, UglyList, I2, I3, I5) ->
    U2 = lists:nth(I2 + 1, UglyList) * 2,
    U3 = lists:nth(I3 + 1, UglyList) * 3,
    U5 = lists:nth(I5 + 1, UglyList) * 5,
    NextUgly = erlang:min(U2, erlang:min(U3, U5)),
    I2New = if NextUgly == U2 -> I2 + 1; true -> I2 end,
    I3New = if NextUgly == U3 -> I3 + 1; true -> I3 end,
    I5New = if NextUgly == U5 -> I5 + 1; true -> I5 end,
    generate(N, UglyList ++ [NextUgly], I2New, I3New, I5New).
```

## Elixir

```elixir
defmodule Solution do
  @spec nth_ugly_number(n :: integer) :: integer
  def nth_ugly_number(1), do: 1

  def nth_ugly_number(n) when n > 1 do
    arr = :array.new(n, {default, 0})
    arr = :array.set(0, 1, arr)
    generate(1, n, arr, 0, 0, 0)
  end

  defp generate(pos, n, arr, i2, i3, i5) when pos == n do
    :array.get(n - 1, arr)
  end

  defp generate(pos, n, arr, i2, i3, i5) do
    next2 = :array.get(i2, arr) * 2
    next3 = :array.get(i3, arr) * 3
    next5 = :array.get(i5, arr) * 5

    min_val = Enum.min([next2, next3, next5])

    arr = :array.set(pos, min_val, arr)

    i2 = if min_val == next2, do: i2 + 1, else: i2
    i3 = if min_val == next3, do: i3 + 1, else: i3
    i5 = if min_val == next5, do: i5 + 1, else: i5

    generate(pos + 1, n, arr, i2, i3, i5)
  end
end
```
