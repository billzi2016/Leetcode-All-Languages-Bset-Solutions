# 1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K

## Cpp

```cpp
class Solution {
public:
    int findMinFibonacciNumbers(int k) {
        vector<int> fib = {1, 1};
        while (true) {
            long long nxt = (long long)fib[fib.size() - 1] + fib[fib.size() - 2];
            if (nxt > k) break;
            fib.push_back((int)nxt);
        }
        int cnt = 0;
        while (k > 0) {
            int idx = upper_bound(fib.begin(), fib.end(), k) - fib.begin() - 1;
            k -= fib[idx];
            ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int findMinFibonacciNumbers(int k) {
        // Generate Fibonacci numbers up to k
        java.util.List<Integer> fib = new java.util.ArrayList<>();
        fib.add(1);
        fib.add(2);
        while (true) {
            int sz = fib.size();
            long next = (long)fib.get(sz - 1) + fib.get(sz - 2);
            if (next > k) break;
            fib.add((int)next);
        }

        int count = 0;
        int remaining = k;
        while (remaining > 0) {
            // Find the largest Fibonacci number <= remaining
            for (int i = fib.size() - 1; i >= 0; i--) {
                if (fib.get(i) <= remaining) {
                    remaining -= fib.get(i);
                    count++;
                    break;
                }
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        # Generate Fibonacci numbers up to k
        fib = [1, 1]
        while fib[-1] + fib[-2] <= k:
            fib.append(fib[-1] + fib[-2])

        import bisect
        count = 0
        remaining = k
        while remaining > 0:
            idx = bisect.bisect_right(fib, remaining) - 1
            remaining -= fib[idx]
            count += 1
        return count
```

## Python3

```python
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # Generate Fibonacci numbers up to k
        fib = [1, 2]
        while fib[-1] + fib[-2] <= k:
            fib.append(fib[-1] + fib[-2])

        import bisect
        count = 0
        while k > 0:
            idx = bisect.bisect_right(fib, k) - 1
            k -= fib[idx]
            count += 1
        return count
```

## C

```c
int findMinFibonacciNumbers(int k) {
    int fib[50];
    fib[0] = 1;
    fib[1] = 1;
    int n = 2;
    while (1) {
        long long nxt = (long long)fib[n - 1] + fib[n - 2];
        if (nxt > k) break;
        fib[n++] = (int)nxt;
    }
    int cnt = 0;
    for (int i = n - 1; i >= 0 && k > 0; --i) {
        if (fib[i] <= k) {
            k -= fib[i];
            ++cnt;
        }
    }
    return cnt;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindMinFibonacciNumbers(int k)
    {
        var fib = new List<int> { 1, 1 };
        while (true)
        {
            long next = (long)fib[fib.Count - 1] + fib[fib.Count - 2];
            if (next > k) break;
            fib.Add((int)next);
        }

        int count = 0;
        int remaining = k;
        for (int i = fib.Count - 1; i >= 0 && remaining > 0; i--)
        {
            if (fib[i] <= remaining)
            {
                remaining -= fib[i];
                count++;
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} k
 * @return {number}
 */
var findMinFibonacciNumbers = function(k) {
    const fib = [1, 1];
    while (fib[fib.length - 1] < k) {
        fib.push(fib[fib.length - 1] + fib[fib.length - 2]);
    }
    let count = 0;
    let idx = fib.length - 1;
    while (k > 0) {
        if (fib[idx] > k) {
            idx--;
        } else {
            k -= fib[idx];
            count++;
        }
    }
    return count;
};
```

## Typescript

```typescript
function findMinFibonacciNumbers(k: number): number {
    const fib: number[] = [1, 2];
    while (fib[fib.length - 1] + fib[fib.length - 2] <= k) {
        fib.push(fib[fib.length - 1] + fib[fib.length - 2]);
    }
    let count = 0;
    let idx = fib.length - 1;
    while (k > 0) {
        while (fib[idx] > k) idx--;
        k -= fib[idx];
        count++;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $k
     * @return Integer
     */
    function findMinFibonacciNumbers($k) {
        // Generate unique Fibonacci numbers up to k (starting with 1, 2)
        $fib = [1, 2];
        while (true) {
            $next = $fib[count($fib) - 1] + $fib[count($fib) - 2];
            if ($next > $k) {
                break;
            }
            $fib[] = $next;
        }

        $count = 0;
        while ($k > 0) {
            // Pick the largest Fibonacci number not exceeding k
            for ($i = count($fib) - 1; $i >= 0; $i--) {
                if ($fib[$i] <= $k) {
                    $k -= $fib[$i];
                    $count++;
                    break;
                }
            }
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func findMinFibonacciNumbers(_ k: Int) -> Int {
        var fib = [1, 2]
        while true {
            let next = fib[fib.count - 1] + fib[fib.count - 2]
            if next > k { break }
            fib.append(next)
        }
        var remaining = k
        var count = 0
        for i in stride(from: fib.count - 1, through: 0, by: -1) {
            if fib[i] <= remaining {
                remaining -= fib[i]
                count += 1
                if remaining == 0 { break }
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMinFibonacciNumbers(k: Int): Int {
        val fibs = mutableListOf<Int>()
        var a = 1
        var b = 1
        while (a <= k) {
            fibs.add(a)
            val c = a + b
            a = b
            b = c
        }
        var remaining = k
        var count = 0
        var idx = fibs.size - 1
        while (remaining > 0) {
            if (fibs[idx] <= remaining) {
                remaining -= fibs[idx]
                count++
            } else {
                idx--
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int findMinFibonacciNumbers(int k) {
    // Generate Fibonacci numbers up to k
    List<int> fib = [1, 2];
    while (fib.last + fib[fib.length - 2] <= k) {
      fib.add(fib.last + fib[fib.length - 2]);
    }

    int count = 0;
    int remaining = k;

    // Greedy: take the largest possible Fibonacci number each step
    for (int i = fib.length - 1; i >= 0 && remaining > 0; i--) {
      if (fib[i] <= remaining) {
        remaining -= fib[i];
        count++;
      }
    }

    return count;
  }
}
```

## Golang

```go
package main

func findMinFibonacciNumbers(k int) int {
	// Generate all Fibonacci numbers up to k.
	fib := []int{1, 2}
	for {
		next := fib[len(fib)-1] + fib[len(fib)-2]
		if next > k {
			break
		}
		fib = append(fib, next)
	}

	count := 0
	remaining := k
	for remaining > 0 {
		// Pick the largest Fibonacci number not exceeding the remaining value.
		for i := len(fib) - 1; i >= 0; i-- {
			if fib[i] <= remaining {
				remaining -= fib[i]
				count++
				break
			}
		}
	}
	return count
}
```

## Ruby

```ruby
def find_min_fibonacci_numbers(k)
  fib = [1, 1]
  while (next_fib = fib[-1] + fib[-2]) <= k
    fib << next_fib
  end

  count = 0
  i = fib.length - 1
  remaining = k

  while remaining > 0 && i >= 0
    if fib[i] <= remaining
      remaining -= fib[i]
      count += 1
    else
      i -= 1
    end
  end

  count
end
```

## Scala

```scala
object Solution {
    def findMinFibonacciNumbers(k: Int): Int = {
        val fib = scala.collection.mutable.ArrayBuffer[Int](1, 1)
        while (true) {
            val next = fib(fib.length - 1).toLong + fib(fib.length - 2)
            if (next > k) {
                // stop generating
                break
            } else {
                fib += next.toInt
            }
        }

        var remaining = k
        var count = 0
        for (i <- fib.indices.reverse) {
            while (remaining >= fib(i)) {
                remaining -= fib(i)
                count += 1
            }
            if (remaining == 0) return count
        }
        count
    }

    // Helper to break out of while loop since Scala doesn't have built-in break
    private def break = throw new RuntimeException("break")
    try {
        // dummy block to allow break usage above
    } catch {
        case _: RuntimeException => ()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_min_fibonacci_numbers(k: i32) -> i32 {
        let mut fibs = vec![1i64, 2];
        while *fibs.last().unwrap() <= k as i64 {
            let n = fibs.len();
            let next = fibs[n - 1] + fibs[n - 2];
            if next > k as i64 {
                break;
            }
            fibs.push(next);
        }

        let mut remaining = k as i64;
        let mut count = 0i32;

        for &f in fibs.iter().rev() {
            while remaining >= f {
                remaining -= f;
                count += 1;
            }
            if remaining == 0 {
                break;
            }
        }

        count
    }
}
```

## Racket

```racket
(define/contract (find-min-fibonacci-numbers k)
  (-> exact-integer? exact-integer?)
  (let* ((fib
          (let gen ((a 1) (b 2) (acc '()))
            (if (> a k)
                (reverse acc)
                (gen b (+ a b) (cons a acc)))))
         (desc-fib (reverse fib)))
    (let loop ((rem k) (cnt 0))
      (if (= rem 0)
          cnt
          (let find ((lst desc-fib))
            (cond [(<= (car lst) rem)
                   (loop (- rem (car lst)) (+ cnt 1))]
                  [else (find (cdr lst))]))))))
```

## Erlang

```erlang
-module(solution).
-export([find_min_fibonacci_numbers/1]).

-spec find_min_fibonacci_numbers(K :: integer()) -> integer().
find_min_fibonacci_numbers(K) ->
    FibList = gen_fibs(K),
    greedy(lists:reverse(FibList), K, 0).

gen_fibs(Max) when Max < 1 -> [];
gen_fibs(1) -> [1];
gen_fibs(Max) ->
    gen_fibs_loop(1, 2, Max, [1, 2]).

gen_fibs_loop(A, B, Max, Acc) ->
    Next = A + B,
    if
        Next =< Max ->
            gen_fibs_loop(B, Next, Max, Acc ++ [Next]);
        true ->
            Acc
    end.

greedy([], _Rem, Count) -> Count;
greedy([H|T] = List, Rem, Count) ->
    case H =< Rem of
        true  -> greedy(List, Rem - H, Count + 1);
        false -> greedy(T, Rem, Count)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_min_fibonacci_numbers(k :: integer) :: integer
  def find_min_fibonacci_numbers(k) do
    fibs = generate_fibs(k)

    {count, _remaining} =
      Enum.reduce(Enum.reverse(fibs), {0, k}, fn fib, {cnt, rem} ->
        if rem >= fib do
          q = div(rem, fib)
          {cnt + q, rem - q * fib}
        else
          {cnt, rem}
        end
      end)

    count
  end

  defp generate_fibs(limit) do
    gen(limit, 1, 2, [])
  end

  defp gen(limit, a, _b, acc) when a > limit, do: Enum.reverse(acc)
  defp gen(limit, a, b, acc), do: gen(limit, b, a + b, [a | acc])
end
```
