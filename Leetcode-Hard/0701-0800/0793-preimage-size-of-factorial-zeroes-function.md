# 0793. Preimage Size of Factorial Zeroes Function

## Cpp

```cpp
class Solution {
public:
    long long zeros(long long x) {
        long long cnt = 0;
        while (x) {
            x /= 5;
            cnt += x;
        }
        return cnt;
    }
    
    int preimageSizeFZF(int k) {
        long long low = 0, high = 5LL * (k + 1);
        while (low < high) {
            long long mid = low + (high - low) / 2;
            if (zeros(mid) >= k)
                high = mid;
            else
                low = mid + 1;
        }
        return zeros(low) == k ? 5 : 0;
    }
};
```

## Java

```java
class Solution {
    public int preimageSizeFZF(int k) {
        long target = k;
        long low = 0, high = 5L * target + 5; // sufficient upper bound
        while (low < high) {
            long mid = low + (high - low) / 2;
            if (trailingZeros(mid) >= target) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return trailingZeros(low) == target ? 5 : 0;
    }

    private long trailingZeros(long x) {
        long cnt = 0;
        while (x > 0) {
            x /= 5;
            cnt += x;
        }
        return cnt;
    }
}
```

## Python

```python
class Solution(object):
    def preimageSizeFZF(self, k):
        """
        :type k: int
        :rtype: int
        """
        def zeros(x):
            cnt = 0
            while x:
                x //= 5
                cnt += x
            return cnt

        low, high = 0, 5 * (k + 1)
        while low < high:
            mid = (low + high) // 2
            if zeros(mid) < k:
                low = mid + 1
            else:
                high = mid
        return 5 if zeros(low) == k else 0
```

## Python3

```python
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zeros(n: int) -> int:
            cnt = 0
            while n:
                n //= 5
                cnt += n
            return cnt

        lo, hi = 0, 5 * (k + 1)
        while lo < hi:
            mid = (lo + hi) // 2
            if zeros(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return 5 if zeros(lo) == k else 0
```

## C

```c
int preimageSizeFZF(int k) {
    auto zeros = [](long long x) -> long long {
        long long cnt = 0;
        while (x) {
            x /= 5;
            cnt += x;
        }
        return cnt;
    };
    
    long long target = k;
    long long lo = 0, hi = 5LL * (target + 1); // upper bound sufficient
    
    // find first x with zeros(x) >= k
    while (lo < hi) {
        long long mid = lo + (hi - lo) / 2;
        if (zeros(mid) >= target) hi = mid;
        else lo = mid + 1;
    }
    if (zeros(lo) != target) return 0;
    long long first = lo;
    
    // find first x with zeros(x) > k
    lo = first; 
    hi = 5LL * (target + 1);
    while (lo < hi) {
        long long mid = lo + (hi - lo) / 2;
        if (zeros(mid) > target) hi = mid;
        else lo = mid + 1;
    }
    long long last = lo - 1;
    
    return (int)(last - first + 1);
}
```

## Csharp

```csharp
public class Solution {
    public int PreimageSizeFZF(int k) {
        long target = k;
        long left = 0;
        long right = 5L * target + 5; // sufficient upper bound
        
        while (left < right) {
            long mid = left + (right - left) / 2;
            if (CountZeros(mid) < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        return CountZeros(left) == target ? 5 : 0;
    }
    
    private long CountZeros(long n) {
        long cnt = 0;
        while (n > 0) {
            n /= 5;
            cnt += n;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} k
 * @return {number}
 */
var preimageSizeFZF = function(k) {
    const trailingZeros = (x) => {
        let cnt = 0;
        while (x > 0) {
            x = Math.floor(x / 5);
            cnt += x;
        }
        return cnt;
    };
    
    let low = 0, high = 5 * (k + 1);
    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (trailingZeros(mid) >= k) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return trailingZeros(low) === k ? 5 : 0;
};
```

## Typescript

```typescript
function preimageSizeFZF(k: number): number {
    const trailingZeros = (x: number): number => {
        let cnt = 0;
        while (x > 0) {
            x = Math.floor(x / 5);
            cnt += x;
        }
        return cnt;
    };

    let lo = 0;
    let hi = 5 * (k + 1); // sufficient upper bound

    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (trailingZeros(mid) >= k) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }

    return trailingZeros(lo) === k ? 5 : 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $k
     * @return Integer
     */
    function preimageSizeFZF($k) {
        $left = 0;
        // Upper bound: for each extra zero we need at most 5 numbers, plus some margin
        $right = 5 * ($k + 1);
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            $z = $this->trailingZeros($mid);
            if ($z < $k) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }
        return $this->trailingZeros($left) == $k ? 5 : 0;
    }

    private function trailingZeros($x) {
        $cnt = 0;
        while ($x > 0) {
            $x = intdiv($x, 5);
            $cnt += $x;
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func preimageSizeFZF(_ k: Int) -> Int {
        var low = 0
        var high = 5 * (k + 1)
        while low < high {
            let mid = low + (high - low) / 2
            if trailingZeros(mid) >= k {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return trailingZeros(low) == k ? 5 : 0
    }
    
    private func trailingZeros(_ x: Int) -> Int {
        var n = x
        var count = 0
        while n > 0 {
            n /= 5
            count += n
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun preimageSizeFZF(k: Int): Int {
        val target = k.toLong()
        var low = 0L
        var high = 5L * target + 5L  // sufficient upper bound

        while (low < high) {
            val mid = (low + high) ushr 1
            if (trailingZeros(mid) >= target) {
                high = mid
            } else {
                low = mid + 1
            }
        }

        return if (trailingZeros(low) == target) 5 else 0
    }

    private fun trailingZeros(x: Long): Long {
        var cnt = 0L
        var div = x / 5
        while (div > 0) {
            cnt += div
            div /= 5
        }
        return cnt
    }
}
```

## Dart

```dart
class Solution {
  int preimageSizeFZF(int k) {
    int low = 0;
    int high = 5 * (k + 1);
    while (low < high) {
      int mid = low + ((high - low) >> 1);
      if (_zeros(mid) >= k) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return _zeros(low) == k ? 5 : 0;
  }

  int _zeros(int n) {
    int cnt = 0;
    while (n > 0) {
      n ~/= 5;
      cnt += n;
    }
    return cnt;
  }
}
```

## Golang

```go
func preimageSizeFZF(k int) int {
	low, high := int64(0), int64(5*int64(k)+5)
	target := int64(k)
	for low < high {
		mid := (low + high) / 2
		if trailingZeros(mid) >= target {
			high = mid
		} else {
			low = mid + 1
		}
	}
	if trailingZeros(low) != target {
		return 0
	}
	return 5
}

func trailingZeros(n int64) int64 {
	var cnt int64
	for n > 0 {
		n /= 5
		cnt += n
	}
	return cnt
}
```

## Ruby

```ruby
def trailing_zeros(n)
  cnt = 0
  while n > 0
    n /= 5
    cnt += n
  end
  cnt
end

def preimage_size_fzf(k)
  left = 0
  right = 5 * (k + 1)
  while left < right
    mid = (left + right) / 2
    if trailing_zeros(mid) >= k
      right = mid
    else
      left = mid + 1
    end
  end
  trailing_zeros(left) == k ? 5 : 0
end
```

## Scala

```scala
object Solution {
    def preimageSizeFZF(k: Int): Int = {
        def trailingZeros(x: Long): Long = {
            var cnt = 0L
            var div = x / 5
            while (div > 0) {
                cnt += div
                div /= 5
            }
            cnt
        }

        var lo = 0L
        var hi = 5L * (k.toLong + 1)
        while (lo < hi) {
            val mid = (lo + hi) >>> 1
            if (trailingZeros(mid) < k) lo = mid + 1
            else hi = mid
        }
        if (trailingZeros(lo) == k) 5 else 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn preimage_size_fzf(k: i32) -> i32 {
        fn trailing_zeros(mut n: i64) -> i64 {
            let mut cnt = 0i64;
            while n > 0 {
                n /= 5;
                cnt += n;
            }
            cnt
        }

        let k_i64 = k as i64;
        // Upper bound sufficient for given constraints
        let mut lo: i64 = 0;
        let mut hi: i64 = 5 * (k_i64 + 1); // ensures tz(hi) >= k

        while lo < hi {
            let mid = (lo + hi) / 2;
            if trailing_zeros(mid) >= k_i64 {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }

        if trailing_zeros(lo) == k_i64 { 5 } else { 0 }
    }
}
```

## Racket

```racket
(define (tz x)
  (let loop ((p 5) (sum 0))
    (if (> p x)
        sum
        (loop (* p 5) (+ sum (quotient x p))))))

(define/contract (preimage-size-fzf k)
  (-> exact-integer? exact-integer?)
  (let* ((high (* 5 (+ k 1)))
         (search
          (let loop ((low 0) (high high))
            (if (< low high)
                (let* ((mid (quotient (+ low high) 2))
                       (z (tz mid)))
                  (if (>= z k)
                      (loop low mid)
                      (loop (+ mid 1) high)))
                low))))
    (if (= (tz search) k) 5 0)))
```

## Erlang

```erlang
-spec preimage_size_fzf(K :: integer()) -> integer().
preimage_size_fzf(K) ->
    Low = binary_search(K, 0, 5*K + 5),
    case zeros(Low) of
        K -> 5;
        _ -> 0
    end.

binary_search(_K, Low, High) when Low >= High -> Low;
binary_search(K, Low, High) ->
    Mid = (Low + High) div 2,
    Z = zeros(Mid),
    if Z < K ->
            binary_search(K, Mid + 1, High);
       true ->
            binary_search(K, Low, Mid)
    end.

zeros(N) -> zeros(N, 5).
zeros(N, P) when P =< N ->
    N div P + zeros(N, P * 5);
zeros(_, _) -> 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec preimage_size_fzf(k :: integer) :: integer
  def preimage_size_fzf(k) do
    left = 0
    right = 5 * (k + 1)
    x = binary_search(left, right, k)

    if trailing_zeros(x) == k, do: 5, else: 0
  end

  defp binary_search(l, r, k) when l < r do
    m = div(l + r, 2)

    if trailing_zeros(m) >= k do
      binary_search(l, m, k)
    else
      binary_search(m + 1, r, k)
    end
  end

  defp binary_search(l, _r, _k), do: l

  defp trailing_zeros(n) do
    do_trailing_zeros(n, 0)
  end

  defp do_trailing_zeros(0, acc), do: acc

  defp do_trailing_zeros(n, acc) do
    q = div(n, 5)
    do_trailing_zeros(q, acc + q)
  end
end
```
