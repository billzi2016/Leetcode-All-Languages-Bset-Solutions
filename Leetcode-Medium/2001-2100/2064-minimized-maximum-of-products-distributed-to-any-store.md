# 2064. Minimized Maximum of Products Distributed to Any Store

## Cpp

```cpp
class Solution {
public:
    int minimizedMaximum(int n, vector<int>& quantities) {
        int left = 1;
        int right = *max_element(quantities.begin(), quantities.end());
        auto can = [&](int x)->bool{
            long long needed = 0;
            for (int q : quantities) {
                needed += (q + x - 1) / x; // ceil division
                if (needed > n) return false;
            }
            return needed <= n;
        };
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (can(mid))
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
};
```

## Java

```java
class Solution {
    public int minimizedMaximum(int n, int[] quantities) {
        int left = 1;
        int right = 0;
        for (int q : quantities) {
            if (q > right) right = q;
        }
        while (left < right) {
            int mid = left + (right - left) / 2;
            long needed = 0;
            for (int q : quantities) {
                needed += (q + mid - 1) / mid; // ceil division
                if (needed > n) break;
            }
            if (needed <= n) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}
```

## Python

```python
class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            needed = 0
            for q in quantities:
                # ceil division without overflow
                needed += (q + mid - 1) // mid
                if needed > n:   # early break to save time
                    break
            if needed <= n:
                right = mid
            else:
                left = mid + 1
        return left
```

## Python3

```python
class Solution:
    def minimizedMaximum(self, n: int, quantities):
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            required = sum((q + mid - 1) // mid for q in quantities)
            if required <= n:
                right = mid
            else:
                left = mid + 1
        return left
```

## C

```c
int minimizedMaximum(int n, int* quantities, int quantitiesSize) {
    int maxQ = 0;
    for (int i = 0; i < quantitiesSize; ++i) {
        if (quantities[i] > maxQ) maxQ = quantities[i];
    }
    int left = 1, right = maxQ;
    while (left < right) {
        int mid = left + (right - left) / 2;
        long long needed = 0;
        for (int i = 0; i < quantitiesSize; ++i) {
            needed += (quantities[i] + mid - 1) / mid;
            if (needed > n) break;
        }
        if (needed <= n)
            right = mid;
        else
            left = mid + 1;
    }
    return left;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimizedMaximum(int n, int[] quantities)
    {
        int left = 1;
        int right = 0;
        foreach (int q in quantities)
            if (q > right) right = q;

        while (left < right)
        {
            int mid = left + (right - left) / 2;
            long needed = 0;
            foreach (int q in quantities)
                needed += (q + mid - 1) / mid; // ceil division

            if (needed <= n)
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} quantities
 * @return {number}
 */
var minimizedMaximum = function(n, quantities) {
    let left = 1;
    let right = Math.max(...quantities);
    
    const canDistribute = (limit) => {
        let needed = 0;
        for (const q of quantities) {
            needed += Math.floor((q + limit - 1) / limit); // ceil(q/limit)
            if (needed > n) return false;
        }
        return true;
    };
    
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (canDistribute(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
};
```

## Typescript

```typescript
function minimizedMaximum(n: number, quantities: number[]): number {
    let left = 1;
    let right = Math.max(...quantities);
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        let needed = 0;
        for (const q of quantities) {
            needed += Math.ceil(q / mid);
            if (needed > n) break;
        }
        if (needed <= n) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $quantities
     * @return Integer
     */
    function minimizedMaximum($n, $quantities) {
        $low = 1;
        $high = max($quantities);
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            $required = 0;
            foreach ($quantities as $q) {
                // ceil division: (q + mid - 1) / mid
                $required += intdiv($q + $mid - 1, $mid);
                if ($required > $n) {
                    break; // no need to continue, already infeasible
                }
            }
            if ($required <= $n) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }
        return $low;
    }
}
```

## Swift

```swift
class Solution {
    func minimizedMaximum(_ n: Int, _ quantities: [Int]) -> Int {
        var left = 1
        var right = quantities.max()!
        while left < right {
            let mid = (left + right) / 2
            var needed = 0
            for q in quantities {
                needed += (q + mid - 1) / mid
                if needed > n { break }
            }
            if needed <= n {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimizedMaximum(n: Int, quantities: IntArray): Int {
        var left = 1
        var right = quantities.maxOrNull() ?: 0

        fun can(k: Int): Boolean {
            var needed = 0L
            for (q in quantities) {
                needed += ((q + k - 1) / k)
                if (needed > n) return false
            }
            return needed <= n
        }

        while (left < right) {
            val mid = left + (right - left) / 2
            if (can(mid)) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}
```

## Dart

```dart
class Solution {
  int minimizedMaximum(int n, List<int> quantities) {
    int left = 1;
    int right = quantities.reduce((a, b) => a > b ? a : b);
    while (left < right) {
      int mid = left + ((right - left) >> 1);
      if (_can(mid, n, quantities)) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return left;
  }

  bool _can(int limit, int n, List<int> quantities) {
    int needed = 0;
    for (int q in quantities) {
      needed += (q + limit - 1) ~/ limit;
      if (needed > n) return false;
    }
    return true;
  }
}
```

## Golang

```go
func minimizedMaximum(n int, quantities []int) int {
	maxQ := 0
	for _, q := range quantities {
		if q > maxQ {
			maxQ = q
		}
	}
	left, right := 1, maxQ
	for left < right {
		mid := (left + right) / 2
		needed := 0
		for _, q := range quantities {
			needed += (q + mid - 1) / mid
			if needed > n {
				break
			}
		}
		if needed <= n {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
}
```

## Ruby

```ruby
def minimized_maximum(n, quantities)
  left = 1
  right = quantities.max
  while left < right
    mid = (left + right) / 2
    required = 0
    quantities.each do |q|
      required += (q + mid - 1) / mid
      break if required > n
    end
    if required <= n
      right = mid
    else
      left = mid + 1
    end
  end
  left
end
```

## Scala

```scala
object Solution {
  def minimizedMaximum(n: Int, quantities: Array[Int]): Int = {
    var low = 1
    var high = quantities.max
    while (low < high) {
      val mid = (low + high) >>> 1
      var storesNeeded: Long = 0L
      var i = 0
      while (i < quantities.length && storesNeeded <= n) {
        storesNeeded += (quantities(i) + mid - 1) / mid
        i += 1
      }
      if (storesNeeded <= n) high = mid else low = mid + 1
    }
    low
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimized_maximum(n: i32, quantities: Vec<i32>) -> i32 {
        let n = n as i64;
        let mut left: i64 = 1;
        let mut right: i64 = *quantities.iter().max().unwrap() as i64;

        while left < right {
            let mid = (left + right) / 2;
            let mut needed: i64 = 0;
            for &q in quantities.iter() {
                needed += (q as i64 + mid - 1) / mid;
                if needed > n {
                    break;
                }
            }
            if needed <= n {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        left as i32
    }
}
```

## Racket

```racket
(define/contract (minimized-maximum n quantities)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (let* ((maxq (apply max quantities)))
    (define (can? limit)
      (let loop ((idx 0) (used 0))
        (if (= idx (length quantities))
            (<= used n)
            (let* ((q (list-ref quantities idx))
                   (need (+ used (quotient (+ q (- 1 limit)) limit))))
              (if (> need n)
                  #false
                  (loop (+ idx 1) need))))))
    (let rec ((lo 1) (hi maxq))
      (if (= lo hi)
          lo
          (let ((mid (quotient (+ lo hi) 2)))
            (if (can? mid)
                (rec lo mid)
                (rec (+ mid 1) hi)))))))
```

## Erlang

```erlang
-module(solution).
-export([minimized_maximum/2]).

-spec minimized_maximum(N :: integer(), Quantities :: [integer()]) -> integer().
minimized_maximum(N, Quantities) ->
    MaxQ = lists:max(Quantities),
    bin_search(1, MaxQ, N, Quantities).

bin_search(Low, High, _N, _Qs) when Low >= High ->
    Low;
bin_search(Low, High, N, Qs) ->
    Mid = (Low + High) div 2,
    Needed = needed_stores(Mid, Qs),
    if
        Needed =< N -> bin_search(Low, Mid, N, Qs);
        true       -> bin_search(Mid + 1, High, N, Qs)
    end.

needed_stores(X, Qs) ->
    lists:foldl(fun(Q, Acc) -> Acc + ((Q + X - 1) div X) end, 0, Qs).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimized_maximum(n :: integer, quantities :: [integer]) :: integer
  def minimized_maximum(n, quantities) do
    max_q = Enum.max(quantities)
    binary_search(1, max_q, n, quantities)
  end

  defp binary_search(lo, hi, n, quantities) when lo < hi do
    mid = div(lo + hi, 2)

    needed =
      Enum.reduce(quantities, 0, fn q, acc ->
        acc + div(q + mid - 1, mid)
      end)

    if needed <= n do
      binary_search(lo, mid, n, quantities)
    else
      binary_search(mid + 1, hi, n, quantities)
    end
  end

  defp binary_search(lo, _hi, _n, _quantities), do: lo
end
```
