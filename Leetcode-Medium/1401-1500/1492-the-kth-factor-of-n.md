# 1492. The kth Factor of n

## Cpp

```cpp
class Solution {
public:
    int kthFactor(int n, int k) {
        int count = 0;
        std::vector<int> large;
        for (int i = 1; i * i <= n; ++i) {
            if (n % i == 0) {
                ++count;
                if (count == k) return i;
                int j = n / i;
                if (i != j) large.push_back(j);
            }
        }
        if (k > count && k <= count + (int)large.size()) {
            // the needed factor is from the large divisors in descending order
            return large[large.size() - (k - count)];
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int kthFactor(int n, int k) {
        java.util.List<Integer> large = new java.util.ArrayList<>();
        int sqrt = (int) Math.sqrt(n);
        for (int i = 1; i <= sqrt; i++) {
            if (n % i == 0) {
                k--;
                if (k == 0) return i;
                int other = n / i;
                if (other != i) {
                    large.add(other);
                }
            }
        }
        for (int i = large.size() - 1; i >= 0; i--) {
            k--;
            if (k == 0) return large.get(i);
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        small = []
        large = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                small.append(i)
                if i != n // i:
                    large.append(n // i)
            i += 1

        if k <= len(small):
            return small[k - 1]
        # large factors are collected in decreasing order
        idx = k - len(small) - 1
        if idx < len(large):
            return large[-(idx + 1)]
        return -1
```

## Python3

```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        large = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
                j = n // i
                if j != i:
                    large.append(j)
            i += 1
        for val in reversed(large):
            k -= 1
            if k == 0:
                return val
        return -1
```

## C

```c
#include <math.h>

int kthFactor(int n, int k) {
    int count = 0;
    int limit = (int)sqrt((double)n);
    
    // Count small factors in ascending order
    for (int i = 1; i <= limit; ++i) {
        if (n % i == 0) {
            ++count;
            if (count == k) return i;
        }
    }
    
    // Count corresponding large factors in ascending order
    for (int i = limit; i >= 1; --i) {
        if (n % i == 0) {
            int j = n / i;
            if (j != i) {               // avoid duplicate sqrt factor
                ++count;
                if (count == k) return j;
            }
        }
    }
    
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int KthFactor(int n, int k) {
        var small = new System.Collections.Generic.List<int>();
        var large = new System.Collections.Generic.List<int>();
        
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                small.Add(i);
                if (i != n / i) {
                    large.Add(n / i);
                }
            }
        }
        
        if (k <= small.Count) {
            return small[k - 1];
        }
        
        int remaining = k - small.Count;
        if (remaining <= large.Count) {
            // large is in descending order relative to the full sorted list
            return large[large.Count - remaining];
        }
        
        return -1;
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
var kthFactor = function(n, k) {
    const small = [];
    const large = [];
    for (let i = 1; i * i <= n; i++) {
        if (n % i === 0) {
            small.push(i);
            if (i !== n / i) {
                large.push(n / i);
            }
        }
    }
    if (k <= small.length) {
        return small[k - 1];
    }
    k -= small.length;
    large.reverse();
    return k <= large.length ? large[k - 1] : -1;
};
```

## Typescript

```typescript
function kthFactor(n: number, k: number): number {
    const small: number[] = [];
    const large: number[] = [];
    for (let i = 1; i * i <= n; i++) {
        if (n % i === 0) {
            small.push(i);
            if (i !== n / i) large.push(n / i);
        }
    }
    const factors = small.concat(large.reverse());
    return k - 1 < factors.length ? factors[k - 1] : -1;
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
    function kthFactor($n, $k) {
        $small = [];
        $large = [];
        for ($i = 1; $i * $i <= $n; $i++) {
            if ($n % $i == 0) {
                $small[] = $i;
                if ($i != intdiv($n, $i)) {
                    $large[] = intdiv($n, $i);
                }
            }
        }
        $factors = array_merge($small, array_reverse($large));
        return (count($factors) >= $k) ? $factors[$k - 1] : -1;
    }
}
```

## Swift

```swift
class Solution {
    func kthFactor(_ n: Int, _ k: Int) -> Int {
        var small = [Int]()
        var large = [Int]()
        var i = 1
        while i * i <= n {
            if n % i == 0 {
                small.append(i)
                let other = n / i
                if other != i {
                    large.append(other)
                }
            }
            i += 1
        }
        if k <= small.count {
            return small[k - 1]
        }
        let total = small.count + large.count
        if k > total {
            return -1
        } else {
            // large needs to be accessed in ascending order, which is reverse of collection order
            let idx = k - small.count - 1
            return large.reversed()[idx]
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kthFactor(n: Int, k: Int): Int {
        val small = mutableListOf<Int>()
        val large = mutableListOf<Int>()
        var i = 1
        while (i * i <= n) {
            if (n % i == 0) {
                small.add(i)
                val other = n / i
                if (other != i) {
                    large.add(other)
                }
            }
            i++
        }
        val total = small.size + large.size
        if (k > total) return -1
        return if (k <= small.size) {
            small[k - 1]
        } else {
            val idxInLargeReversed = k - small.size - 1
            large[large.size - 1 - idxInLargeReversed]
        }
    }
}
```

## Dart

```dart
class Solution {
  int kthFactor(int n, int k) {
    List<int> small = [];
    List<int> large = [];

    for (int i = 1; i * i <= n; ++i) {
      if (n % i == 0) {
        small.add(i);
        int other = n ~/ i;
        if (other != i) {
          large.add(other);
        }
      }
    }

    int total = small.length + large.length;
    if (k > total) return -1;

    if (k <= small.length) {
      return small[k - 1];
    } else {
      int idxFromEnd = k - small.length; // 1-based index in reversed large
      return large[large.length - idxFromEnd];
    }
  }
}
```

## Golang

```go
func kthFactor(n int, k int) int {
    small := []int{}
    large := []int{}
    for i := 1; i*i <= n; i++ {
        if n%i == 0 {
            small = append(small, i)
            if i != n/i {
                large = append(large, n/i)
            }
        }
    }
    total := len(small) + len(large)
    if k > total {
        return -1
    }
    if k <= len(small) {
        return small[k-1]
    }
    // large is in decreasing order; need the (k-len(small))th smallest among them,
    // which corresponds to reverse indexing.
    idx := len(large) - (k - len(small))
    return large[idx]
}
```

## Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def kth_factor(n, k)
  small = []
  large = []
  i = 1
  while i * i <= n
    if n % i == 0
      small << i
      j = n / i
      large << j unless j == i
    end
    i += 1
  end
  factors = small + large.reverse
  return -1 if k > factors.size
  factors[k - 1]
end
```

## Scala

```scala
object Solution {
    def kthFactor(n: Int, k: Int): Int = {
        val small = scala.collection.mutable.ArrayBuffer[Int]()
        val large = scala.collection.mutable.Stack[Int]()
        val limit = math.sqrt(n).toInt
        for (i <- 1 to limit) {
            if (n % i == 0) {
                small += i
                val other = n / i
                if (other != i) large.push(other)
            }
        }
        val factors = small ++ large.reverse
        if (k <= factors.length) factors(k - 1) else -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn kth_factor(n: i32, k: i32) -> i32 {
        let mut small = Vec::new();
        let mut large = Vec::new();

        let limit = (n as f64).sqrt() as i32;
        for i in 1..=limit {
            if n % i == 0 {
                small.push(i);
                let other = n / i;
                if other != i {
                    large.push(other);
                }
            }
        }

        let total_factors = small.len() + large.len();
        if (k as usize) > total_factors {
            return -1;
        }

        if (k as usize) <= small.len() {
            return small[(k - 1) as usize];
        } else {
            large.sort(); // ascending order
            let idx = (k as usize) - small.len() - 1;
            return large[idx];
        }
    }
}
```

## Racket

```racket
(define/contract (kth-factor n k)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ((limit (exact-floor (sqrt n)))
         (small '())
         (large '()))
    (for ([i (in-range 1 (+ limit 1))])
      (when (= (remainder n i) 0)
        (set! small (cons i small))
        (let ((j (/ n i)))
          (when (not (= i j))
            (set! large (cons j large))))))
    (let* ((factors (append (reverse small) large))
           (len (length factors)))
      (if (>= len k)
          (list-ref factors (- k 1))
          -1))))
```

## Erlang

```erlang
-export([kth_factor/2]).
-spec kth_factor(integer(), integer()) -> integer().
kth_factor(N, K) ->
    Acc = collect_factors(N, 1, []),
    Factors = lists:sort(Acc),
    case length(Factors) >= K of
        true -> lists:nth(K, Factors);
        false -> -1
    end.

collect_factors(_N, I, Acc) when I*I > _N ->
    Acc;
collect_factors(N, I, Acc) ->
    if N rem I =:= 0 ->
            Counter = N div I,
            NewAcc = case Counter == I of
                        true -> [I|Acc];
                        false -> [I,Counter|Acc]
                     end,
            collect_factors(N, I+1, NewAcc);
       true ->
            collect_factors(N, I+1, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec kth_factor(n :: integer, k :: integer) :: integer
  def kth_factor(n, k) do
    limit = :math.sqrt(n) |> trunc()

    {small_rev, large_rev} =
      Enum.reduce(1..limit, {[], []}, fn i, {s, l} ->
        if rem(n, i) == 0 do
          s = [i | s]
          other = div(n, i)

          l = if other != i, do: [other | l], else: l
          {s, l}
        else
          {s, l}
        end
      end)

    small = Enum.reverse(small_rev)
    large = Enum.reverse(large_rev)
    factors = small ++ large

    if k <= length(factors), do: Enum.at(factors, k - 1), else: -1
  end
end
```
