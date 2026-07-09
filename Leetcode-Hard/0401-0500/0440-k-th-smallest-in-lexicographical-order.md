# 0440. K-th Smallest in Lexicographical Order

## Cpp

```cpp
class Solution {
public:
    long long countSteps(int n, long long first, long long second) {
        long long steps = 0;
        while (first <= n) {
            steps += std::min((long long)n + 1, second) - first;
            first *= 10;
            second *= 10;
        }
        return steps;
    }

    int findKthNumber(int n, int k) {
        int curr = 1;
        --k; // we have counted '1' as the first number
        while (k > 0) {
            long long steps = countSteps(n, curr, (long long)curr + 1);
            if (steps <= k) {
                curr += 1;
                k -= steps;
            } else {
                curr *= 10;
                --k;
            }
        }
        return curr;
    }
};
```

## Java

```java
class Solution {
    public int findKthNumber(int n, int k) {
        long curr = 1;
        k--; // count the first number
        while (k > 0) {
            long steps = calcSteps(n, curr, curr + 1);
            if (steps <= k) {
                curr++;
                k -= steps;
            } else {
                curr *= 10;
                k--;
            }
        }
        return (int) curr;
    }

    private long calcSteps(int n, long first, long last) {
        long steps = 0;
        while (first <= n) {
            steps += Math.min((long) n + 1, last) - first;
            first *= 10;
            last *= 10;
        }
        return steps;
    }
}
```

## Python

```python
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count_steps(n, first, last):
            steps = 0
            while first <= n:
                steps += min(n + 1, last) - first
                first *= 10
                last *= 10
            return steps

        curr = 1
        k -= 1  # we have counted '1' as the first number
        while k > 0:
            steps = count_steps(n, curr, curr + 1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
        return curr
```

## Python3

```python
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(first: int, last: int) -> int:
            steps = 0
            while first <= n:
                steps += min(n + 1, last) - first
                first *= 10
                last *= 10
            return steps

        curr = 1
        k -= 1
        while k > 0:
            steps = count_steps(curr, curr + 1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
        return curr
```

## C

```c
int findKthNumber(int n, int k) {
    long long N = n;
    long long cur = 1;
    long long remaining = k - 1; // we have counted 'cur' as the first number

    while (remaining > 0) {
        long long steps = 0;
        long long first = cur;
        long long last = cur + 1;

        while (first <= N) {
            steps += (last <= N + 1 ? last : N + 1) - first;
            first *= 10;
            last *= 10;
        }

        if (steps <= remaining) {
            cur++;
            remaining -= steps;
        } else {
            cur *= 10;
            remaining--;
        }
    }

    return (int)cur;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindKthNumber(int n, int k)
    {
        long curr = 1;
        long remaining = k - 1; // we have counted 'curr' as the first number

        while (remaining > 0)
        {
            long steps = CountSteps(n, curr, curr + 1);
            if (steps <= remaining)
            {
                curr++;
                remaining -= steps;
            }
            else
            {
                curr *= 10;
                remaining--;
            }
        }

        return (int)curr;
    }

    private long CountSteps(int n, long first, long last)
    {
        long steps = 0;
        while (first <= n)
        {
            steps += Math.Min((long)n + 1, last) - first;
            first *= 10;
            last *= 10;
        }
        return steps;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findKthNumber = function(n, k) {
    const countSteps = (n, curr, next) => {
        let steps = 0;
        while (curr <= n) {
            steps += Math.min(n + 1, next) - curr;
            curr *= 10;
            next *= 10;
        }
        return steps;
    };
    
    let curr = 1;
    k -= 1; // we have counted '1' as the first number
    while (k > 0) {
        const steps = countSteps(n, curr, curr + 1);
        if (steps <= k) {
            curr += 1;
            k -= steps;
        } else {
            curr *= 10;
            k -= 1;
        }
    }
    return curr;
};
```

## Typescript

```typescript
function findKthNumber(n: number, k: number): number {
    let curr = 1;
    k--; // first number is counted

    const countSteps = (n: number, first: number, last: number): number => {
        let steps = 0;
        while (first <= n) {
            steps += Math.min(n + 1, last) - first;
            first *= 10;
            last *= 10;
        }
        return steps;
    };

    while (k > 0) {
        const steps = countSteps(n, curr, curr + 1);
        if (steps <= k) {
            curr++;
            k -= steps;
        } else {
            curr *= 10;
            k--;
        }
    }

    return curr;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function findKthNumber($n, $k) {
        $curr = 1;
        $k--; // count the first number

        while ($k > 0) {
            $steps = $this->calcSteps($n, $curr, $curr + 1);
            if ($steps <= $k) {
                $curr++;
                $k -= $steps;
            } else {
                $curr *= 10;
                $k--;
            }
        }

        return $curr;
    }

    /**
     * Count numbers between prefix $first and $last (exclusive) within [1, $n]
     *
     * @param Integer $n
     * @param Integer $first
     * @param Integer $last
     * @return Integer
     */
    private function calcSteps($n, $first, $last) {
        $steps = 0;
        while ($first <= $n) {
            $steps += min($n + 1, $last) - $first;
            $first *= 10;
            $last *= 10;
        }
        return $steps;
    }
}
```

## Swift

```swift
class Solution {
    func findKthNumber(_ n: Int, _ k: Int) -> Int {
        var curr = 1
        var remaining = k - 1
        while remaining > 0 {
            let steps = countSteps(n, curr, curr + 1)
            if steps <= remaining {
                curr += 1
                remaining -= steps
            } else {
                curr *= 10
                remaining -= 1
            }
        }
        return curr
    }

    private func countSteps(_ n: Int, _ first: Int, _ last: Int) -> Int {
        var steps = 0
        var f = first
        var l = last
        while f <= n {
            steps += min(n + 1, l) - f
            f *= 10
            l *= 10
        }
        return steps
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findKthNumber(n: Int, k: Int): Int {
        var curr = 1L
        var remaining = k - 1
        val limit = n.toLong()
        while (remaining > 0) {
            val steps = countSteps(limit, curr, curr + 1)
            if (steps <= remaining) {
                curr += 1
                remaining -= steps.toInt()
            } else {
                curr *= 10
                remaining -= 1
            }
        }
        return curr.toInt()
    }

    private fun countSteps(n: Long, first: Long, next: Long): Long {
        var steps = 0L
        var f = first
        var l = next
        while (f <= n) {
            steps += kotlin.math.min(n + 1, l) - f
            f *= 10
            l *= 10
        }
        return steps
    }
}
```

## Dart

```dart
class Solution {
  int findKthNumber(int n, int k) {
    int curr = 1;
    k -= 1;
    while (k > 0) {
      int steps = _countSteps(n, curr, curr + 1);
      if (steps <= k) {
        curr += 1;
        k -= steps;
      } else {
        curr *= 10;
        k -= 1;
      }
    }
    return curr;
  }

  int _countSteps(int n, int first, int last) {
    int steps = 0;
    while (first <= n) {
      steps += (last <= n + 1 ? last : n + 1) - first;
      first *= 10;
      last *= 10;
    }
    return steps;
  }
}
```

## Golang

```go
func findKthNumber(n int, k int) int {
    var curr int64 = 1
    k-- // we have counted the first number (1)
    for k > 0 {
        steps := calcSteps(int64(n), curr, curr+1)
        if steps <= int64(k) {
            curr++
            k -= int(steps)
        } else {
            curr *= 10
            k--
        }
    }
    return int(curr)
}

func calcSteps(limit, first, next int64) int64 {
    var steps int64 = 0
    for first <= limit {
        if next > limit+1 {
            steps += limit + 1 - first
        } else {
            steps += next - first
        }
        first *= 10
        next *= 10
    }
    return steps
}
```

## Ruby

```ruby
def find_kth_number(n, k)
  curr = 1
  k -= 1
  while k > 0
    steps = 0
    first = curr
    last = curr + 1
    while first <= n
      steps += [n + 1, last].min - first
      first *= 10
      last *= 10
    end
    if steps <= k
      curr += 1
      k -= steps
    else
      curr *= 10
      k -= 1
    end
  end
  curr
end
```

## Scala

```scala
object Solution {
  def findKthNumber(n: Int, k: Int): Int = {
    var cur: Long = 1
    var remaining: Long = k - 1 // we have already counted 'cur' as the first number

    def countSteps(limit: Long, prefix: Long, nextPrefix: Long): Long = {
      var steps: Long = 0
      var p = prefix
      var nP = nextPrefix
      while (p <= limit) {
        steps += math.min(limit + 1, nP) - p
        p *= 10
        nP *= 10
      }
      steps
    }

    val limit = n.toLong
    while (remaining > 0) {
      val steps = countSteps(limit, cur, cur + 1)
      if (steps <= remaining) {
        cur += 1
        remaining -= steps
      } else {
        cur *= 10
        remaining -= 1
      }
    }
    cur.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_kth_number(n: i32, k: i32) -> i32 {
        fn count_steps(limit: i64, cur: i64, next: i64) -> i64 {
            let mut steps = 0i64;
            let (mut first, mut last) = (cur, next);
            while first <= limit {
                steps += std::cmp::min(limit + 1, last) - first;
                first *= 10;
                last *= 10;
            }
            steps
        }

        let mut cur: i64 = 1;
        let mut remaining: i64 = k as i64 - 1; // we have counted '1' already

        while remaining > 0 {
            let steps = count_steps(n as i64, cur, cur + 1);
            if steps <= remaining {
                cur += 1;
                remaining -= steps;
            } else {
                cur *= 10;
                remaining -= 1;
            }
        }

        cur as i32
    }
}
```

## Racket

```racket
(define/contract (find-kth-number n k)
  (-> exact-integer? exact-integer? exact-integer?)
  (letrec
      ((count-steps
         (lambda (n first last)
           (let loop ((first first) (last last) (steps 0))
             (if (> first n)
                 steps
                 (loop (* first 10)
                       (* last 10)
                       (+ steps (- (min (+ n 1) last) first))))))))
    (let loop ((curr 1) (k (- k 1)))
      (if (= k 0)
          curr
          (let ((step (count-steps n curr (+ curr 1))))
            (if (<= step k)
                (loop (+ curr 1) (- k step))
                (loop (* curr 10) (- k 1)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_kth_number/2]).

-spec find_kth_number(N :: integer(), K :: integer()) -> integer().
find_kth_number(N, K) ->
    find_kth_number_loop(N, K - 1, 1).

%% Recursive loop to locate the k-th number
-spec find_kth_number_loop(integer(), integer(), integer()) -> integer().
find_kth_number_loop(_N, 0, Curr) ->
    Curr;
find_kth_number_loop(N, K, Curr) ->
    Step = count_steps(N, Curr, Curr + 1),
    if
        Step =< K ->
            find_kth_number_loop(N, K - Step, Curr + 1);
        true ->
            find_kth_number_loop(N, K - 1, Curr * 10)
    end.

%% Count numbers between prefix [first, last) within [1, N]
-spec count_steps(integer(), integer(), integer()) -> integer().
count_steps(N, First, Last) ->
    count_steps(N, First, Last, 0).

-spec count_steps(integer(), integer(), integer(), integer()) -> integer().
count_steps(N, First, Last, Acc) when First =< N ->
    NextAcc = Acc + (min(N + 1, Last) - First),
    count_steps(N, First * 10, Last * 10, NextAcc);
count_steps(_N, _First, _Last, Acc) ->
    Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_kth_number(n :: integer, k :: integer) :: integer
  def find_kth_number(n, k) do
    find_kth_number_loop(n, k - 1, 1)
  end

  defp find_kth_number_loop(_n, 0, curr), do: curr

  defp find_kth_number_loop(n, k, curr) do
    step = steps(n, curr, curr + 1)

    if step <= k do
      find_kth_number_loop(n, k - step, curr + 1)
    else
      find_kth_number_loop(n, k - 1, curr * 10)
    end
  end

  defp steps(n, first, last) when first > n, do: 0

  defp steps(n, first, last) do
    add = min(n + 1, last) - first
    add + steps(n, first * 10, last * 10)
  end
end
```
