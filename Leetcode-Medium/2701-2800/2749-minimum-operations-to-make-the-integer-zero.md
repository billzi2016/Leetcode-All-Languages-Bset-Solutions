# 2749. Minimum Operations to Make the Integer Zero

## Cpp

```cpp
class Solution {
public:
    int makeTheIntegerZero(int num1, int num2) {
        for (int k = 1; k <= 60; ++k) {
            long long target = (long long)num1 - (long long)k * num2;
            if (target < k) continue; // need at least k ones (each >=1)
            int bits = __builtin_popcountll(target);
            if (bits <= k && k <= target) return k;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int makeTheIntegerZero(int num1, int num2) {
        for (int k = 1; k <= 60; k++) {
            long target = (long) num1 - (long) k * num2;
            if (target < k) continue; // need at least k ones
            int bits = Long.bitCount(target);
            if (bits <= k && k <= target) {
                return k;
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        for k in range(1, 61):
            remaining = num1 - k * num2
            if remaining < 0:
                continue
            # need at least k ones to represent as sum of k powers of two
            if remaining < k:
                continue
            # popcount must not exceed k
            if bin(remaining).count('1') <= k:
                return k
        return -1
```

## Python3

```python
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            target = num1 - k * num2
            if target <= 0:
                continue
            if target >= k and bin(target).count('1') <= k:
                return k
        return -1
```

## C

```c
int makeTheIntegerZero(int num1, int num2) {
    for (int k = 1; k <= 60; ++k) {
        long long target = (long long)num1 - (long long)k * (long long)num2;
        if (target < 0) continue;
        int bits = __builtin_popcountll((unsigned long long)target);
        if (bits <= k && k <= target) return k;
    }
    return -1;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MakeTheIntegerZero(int num1, int num2) {
        if (num1 == 0) return 0;
        for (int k = 1; k <= 60; k++) {
            long target = (long)num1 - (long)k * num2;
            if (target < k) continue; // need at least k ones
            int bits = PopCount(target);
            if (bits <= k && k <= target) return k;
        }
        return -1;
    }

    private int PopCount(long x) {
        int cnt = 0;
        while (x != 0) {
            cnt++;
            x &= x - 1;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var makeTheIntegerZero = function(num1, num2) {
    for (let k = 1; k <= 60; ++k) {
        const target = num1 - k * num2;
        if (target < k) continue; // need at least k ones
        let t = BigInt(target);
        let bits = 0;
        while (t > 0n) {
            bits++;
            t &= t - 1n; // remove lowest set bit
        }
        if (bits <= k) return k;
    }
    return -1;
};
```

## Typescript

```typescript
function makeTheIntegerZero(num1: number, num2: number): number {
    const maxOps = 60;
    for (let k = 1; k <= maxOps; ++k) {
        const S = num1 - k * num2;
        if (S < k) continue; // need at least k ones (each power >= 1)
        const pc = popcnt(S);
        if (pc <= k && k <= S) return k;
    }
    return -1;
}

function popcnt(x: number): number {
    let b = BigInt(x);
    let cnt = 0;
    while (b > 0n) {
        cnt++;
        b &= b - 1n;
    }
    return cnt;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num1
     * @param Integer $num2
     * @return Integer
     */
    function makeTheIntegerZero($num1, $num2) {
        for ($k = 1; $k <= 60; $k++) {
            $target = $num1 - $k * $num2;
            if ($target < $k) {
                continue;
            }
            // count set bits in target
            $cnt = 0;
            $temp = $target;
            while ($temp > 0) {
                $cnt += $temp & 1;
                $temp >>= 1;
            }
            if ($cnt <= $k && $k <= $target) {
                return $k;
            }
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func makeTheIntegerZero(_ num1: Int, _ num2: Int) -> Int {
        let n1 = Int64(num1)
        let n2 = Int64(num2)
        for k in 1...60 {
            let target = n1 - Int64(k) * n2
            if target < Int64(k) { continue }
            if target < 0 { continue }
            let pop = (UInt64(target)).nonzeroBitCount
            if pop <= k && k <= target {
                return k
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun makeTheIntegerZero(num1: Int, num2: Int): Int {
        val n1 = num1.toLong()
        val n2 = num2.toLong()
        for (k in 0..60) {
            val target = n1 - k * n2
            if (target < 0L) continue
            if (target < k.toLong()) continue
            val pop = java.lang.Long.bitCount(target)
            if (pop <= k && k <= target) return k
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int makeTheIntegerZero(int num1, int num2) {
    if (num1 == 0) return 0;
    for (int k = 1; k <= 60; ++k) {
      int target = num1 - k * num2;
      if (target < 0) continue;
      if (target < k) continue;
      if (_popCount(target) <= k) return k;
    }
    return -1;
  }

  int _popCount(int x) {
    int cnt = 0;
    while (x > 0) {
      cnt += x & 1;
      x >>= 1;
    }
    return cnt;
  }
}
```

## Golang

```go
import "math/bits"

func makeTheIntegerZero(num1 int, num2 int) int {
	if num1 == 0 {
		return 0
	}
	for k := 1; k <= 60; k++ {
		s := int64(num1) - int64(k)*int64(num2)
		if s < 0 {
			continue
		}
		bitsCount := bits.OnesCount64(uint64(s))
		if bitsCount <= k && k <= int(s) {
			return k
		}
	}
	return -1
}
```

## Ruby

```ruby
def make_the_integer_zero(num1, num2)
  (1..60).each do |k|
    s = num1 - k * num2
    next if s < 0
    cnt = s.to_s(2).count('1')
    return k if cnt <= k && k <= s
  end
  -1
end
```

## Scala

```scala
object Solution {
    def makeTheIntegerZero(num1: Int, num2: Int): Int = {
        if (num1 == 0) return 0
        val n1 = num1.toLong
        val n2 = num2.toLong
        for (k <- 1 to 60) {
            val s = n1 - k * n2
            if (s > 0 && java.lang.Long.bitCount(s) <= k && k <= s) {
                return k
            }
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn make_the_integer_zero(num1: i32, num2: i32) -> i32 {
        let n1 = num1 as i64;
        let n2 = num2 as i64;
        for k in 1..=60 {
            let target = n1 - (k as i64) * n2;
            if target <= 0 {
                continue;
            }
            let bits = (target as u64).count_ones() as i32;
            if bits <= k && target >= k as i64 {
                return k as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
(require racket/bitwise)

(define/contract (make-the-integer-zero num1 num2)
  (-> exact-integer? exact-integer? exact-integer?)
  (if (= num1 0) 
      0
      (let loop ((t 1))
        (cond [(> t 60) -1]
              [else
               (let ([s (- num1 (* t num2))])
                 (if (or (< s 0) (= s 0))
                     (loop (+ t 1))
                     (let ([cnt (bitwise-bit-count s)])
                       (if (and (<= cnt t) (<= t s))
                           t
                           (loop (+ t 1))))))]))))
```

## Erlang

```erlang
-spec make_the_integer_zero(integer(), integer()) -> integer().
make_the_integer_zero(Num1, Num2) ->
    case find_min_ops(Num1, Num2, 0) of
        undefined -> -1;
        K -> K
    end.

find_min_ops(_Num1, _Num2, K) when K > 60 ->
    undefined;
find_min_ops(Num1, Num2, 0) ->
    if Num1 == 0 -> 0;
       true -> find_min_ops(Num1, Num2, 1)
    end;
find_min_ops(Num1, Num2, K) ->
    S = Num1 - K * Num2,
    if S >= K, popcount(S) =< K ->
            K;
       true ->
            find_min_ops(Num1, Num2, K + 1)
    end.

popcount(N) when N =< 0 -> 0;
popcount(N) ->
    (N band 1) + popcount(N bsr 1).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec make_the_integer_zero(num1 :: integer, num2 :: integer) :: integer
  def make_the_integer_zero(num1, num2) do
    max_ops = 60

    Enum.reduce_while(1..max_ops, -1, fn k, _acc ->
      s = num1 - num2 * k

      if s >= 0 do
        pc = popcnt(s)

        if pc <= k and k <= s do
          {:halt, k}
        else
          {:cont, -1}
        end
      else
        {:cont, -1}
      end
    end)
  end

  defp popcnt(0), do: 0
  defp popcnt(n) when n > 0 do
    1 + popcnt(band(n, n - 1))
  end
end
```
