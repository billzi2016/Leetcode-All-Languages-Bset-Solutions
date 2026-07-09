# 0668. Kth Smallest Number in Multiplication Table

## Cpp

```cpp
class Solution {
public:
    int findKthNumber(int m, int n, int k) {
        long long lo = 1, hi = 1LL * m * n;
        while (lo < hi) {
            long long mid = lo + (hi - lo) / 2;
            long long cnt = 0;
            for (int i = 1; i <= m; ++i) {
                cnt += std::min(mid / i, (long long)n);
                if (cnt >= k) break;
            }
            if (cnt >= k) hi = mid;
            else lo = mid + 1;
        }
        return (int)lo;
    }
};
```

## Java

```java
class Solution {
    public int findKthNumber(int m, int n, int k) {
        int lo = 1;
        int hi = m * n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (enough(mid, m, n, k)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    private boolean enough(int x, int m, int n, int k) {
        long cnt = 0;
        for (int i = 1; i <= m; i++) {
            cnt += Math.min(n, x / i);
            if (cnt >= k) {
                return true;
            }
        }
        return cnt >= k;
    }
}
```

## Python

```python
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        lo, hi = 1, m * n

        while lo < hi:
            mid = (lo + hi) // 2
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(mid // i, n)
                if cnt >= k:  # early stop to avoid unnecessary work
                    break
            if cnt >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo
```

## Python3

```python
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo, hi = 1, m * n
        while lo < hi:
            mid = (lo + hi) // 2
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(mid // i, n)
                if cnt >= k:  # early stop to avoid unnecessary work
                    break
            if cnt >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## C

```c
int findKthNumber(int m, int n, int k) {
    int lo = 1;
    int hi = m * n;  // product fits in 32-bit (max 9e8)
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        long long cnt = 0;
        for (int i = 1; i <= m; ++i) {
            int add = mid / i;
            if (add > n) add = n;
            cnt += add;
            if (cnt >= k) break; // no need to count further
        }
        if (cnt >= k)
            hi = mid;
        else
            lo = mid + 1;
    }
    return lo;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindKthNumber(int m, int n, int k)
    {
        int low = 1;
        int high = m * n;
        while (low < high)
        {
            int mid = low + (high - low) / 2;
            long cnt = 0;
            for (int i = 1; i <= m; i++)
            {
                cnt += Math.Min(mid / i, n);
                if (cnt >= k) break; // early exit
            }
            if (cnt >= k)
                high = mid;
            else
                low = mid + 1;
        }
        return low;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findKthNumber = function(m, n, k) {
    const enough = (x) => {
        let cnt = 0;
        for (let i = 1; i <= m; ++i) {
            cnt += Math.min(Math.floor(x / i), n);
            if (cnt >= k) return true;
        }
        return false;
    };
    
    let lo = 1, hi = m * n;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (enough(mid)) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    return lo;
};
```

## Typescript

```typescript
function findKthNumber(m: number, n: number, k: number): number {
    let low = 1;
    let high = m * n;

    while (low < high) {
        const mid = Math.floor((low + high) / 2);
        let cnt = 0;
        for (let i = 1; i <= m; ++i) {
            cnt += Math.min(Math.floor(mid / i), n);
            if (cnt >= k) break; // early exit
        }
        if (cnt >= k) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }

    return low;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function findKthNumber($m, $n, $k) {
        $lo = 1;
        $hi = $m * $n;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            $cnt = 0;
            for ($i = 1; $i <= $m; $i++) {
                $cnt += min(intdiv($mid, $i), $n);
                if ($cnt >= $k) { // early stop to avoid unnecessary work
                    break;
                }
            }
            if ($cnt >= $k) {
                $hi = $mid;
            } else {
                $lo = $mid + 1;
            }
        }
        return $lo;
    }
}
```

## Swift

```swift
class Solution {
    func findKthNumber(_ m: Int, _ n: Int, _ k: Int) -> Int {
        var low = 1
        var high = m * n
        
        while low < high {
            let mid = (low + high) / 2
            var count = 0
            for i in 1...m {
                count += min(n, mid / i)
                if count >= k { break }
            }
            if count >= k {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findKthNumber(m: Int, n: Int, k: Int): Int {
        var low = 1
        var high = m * n
        while (low < high) {
            val mid = low + (high - low) / 2
            var count = 0L
            for (i in 1..m) {
                count += kotlin.math.min(mid / i, n).toLong()
                if (count >= k) break
            }
            if (count >= k) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }
}
```

## Dart

```dart
class Solution {
  int findKthNumber(int m, int n, int k) {
    int low = 1;
    int high = m * n;
    while (low < high) {
      int mid = (low + high) >> 1;
      int cnt = 0;
      for (int i = 1; i <= m; ++i) {
        int add = mid ~/ i;
        if (add > n) add = n;
        cnt += add;
        if (cnt >= k) break; // early exit
      }
      if (cnt >= k) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
func findKthNumber(m int, n int, k int) int {
	lo, hi := 1, m*n
	for lo < hi {
		mid := (lo + hi) / 2
		cnt := 0
		for i := 1; i <= m; i++ {
			val := mid / i
			if val > n {
				val = n
			}
			cnt += val
			if cnt >= k { // early stop to avoid unnecessary work
				break
			}
		}
		if cnt >= k {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}
```

## Ruby

```ruby
def find_kth_number(m, n, k)
  lo = 1
  hi = m * n
  while lo < hi
    mid = (lo + hi) / 2
    cnt = 0
    i = 1
    while i <= m && cnt < k
      cnt += [mid / i, n].min
      i += 1
    end
    if cnt >= k
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
```

## Scala

```scala
object Solution {
  def findKthNumber(m: Int, n: Int, k: Int): Int = {
    var low: Long = 1L
    var high: Long = m.toLong * n.toLong

    while (low < high) {
      val mid = (low + high) / 2
      var cnt: Long = 0L
      var i = 1
      while (i <= m && cnt < k) {
        cnt += Math.min(n.toLong, mid / i)
        i += 1
      }
      if (cnt >= k) high = mid else low = mid + 1
    }

    low.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_kth_number(m: i32, n: i32, k: i32) -> i32 {
        let m = m as i64;
        let n = n as i64;
        let k = k as i64;
        let mut lo = 1i64;
        let mut hi = m * n;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if Self::enough(mid, m, n, k) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }

    fn enough(x: i64, m: i64, n: i64, k: i64) -> bool {
        let mut cnt = 0i64;
        for i in 1..=m {
            cnt += std::cmp::min(n, x / i);
            if cnt >= k {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (find-kth-number m n k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ([lo 1]
         [hi (* m n)])
    (let loop ((low lo) (high hi))
      (if (= low high)
          low
          (let* ([mid (quotient (+ low high) 2)]
                 [cnt (let sum ((i 1) (acc 0))
                        (if (> i m)
                            acc
                            (let ([add (min n (quotient mid i))])
                              (sum (add1 i) (+ acc add)))) )])
            (if (>= cnt k)
                (loop low mid)
                (loop (add1 mid) high)))))))
```

## Erlang

```erlang
-spec find_kth_number(integer(), integer(), integer()) -> integer().
find_kth_number(M, N, K) ->
    bs(1, M * N, M, N, K).

bs(Low, High, _M, _N, _K) when Low >= High ->
    Low;
bs(Low, High, M, N, K) ->
    Mid = (Low + High) div 2,
    case enough(Mid, M, N, K) of
        true -> bs(Low, Mid, M, N, K);
        false -> bs(Mid + 1, High, M, N, K)
    end.

enough(X, M, N, K) ->
    Count = count_leq(X, 1, M, N, 0),
    Count >= K.

count_leq(_X, I, M, _N, Acc) when I > M ->
    Acc;
count_leq(X, I, M, N, Acc) ->
    Row = X div I,
    Add = if Row > N -> N; true -> Row end,
    count_leq(X, I + 1, M, N, Acc + Add).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_kth_number(m :: integer, n :: integer, k :: integer) :: integer
  def find_kth_number(m, n, k) do
    binary_search(1, m * n, m, n, k)
  end

  defp binary_search(lo, hi, _m, _n, _k) when lo == hi, do: lo

  defp binary_search(lo, hi, m, n, k) do
    mid = div(lo + hi, 2)
    cnt = count_leq(mid, m, n)

    if cnt >= k do
      binary_search(lo, mid, m, n, k)
    else
      binary_search(mid + 1, hi, m, n, k)
    end
  end

  defp count_leq(x, m, n) do
    1..m
    |> Enum.reduce(0, fn i, acc ->
      acc + min(div(x, i), n)
    end)
  end
end
```
