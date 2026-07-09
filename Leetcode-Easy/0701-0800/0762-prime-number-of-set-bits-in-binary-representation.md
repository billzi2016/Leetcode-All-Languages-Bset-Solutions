# 0762. Prime Number of Set Bits in Binary Representation

## Cpp

```cpp
class Solution {
public:
    int countPrimeSetBits(int left, int right) {
        static const bool isPrime[21] = {
            false,false,true,true,false,true,false,true,
            false,false,false,true,false,true,false,true,
            false,false,true,false,false
        };
        int ans = 0;
        for (int i = left; i <= right; ++i) {
            int bits = __builtin_popcount(i);
            if (isPrime[bits]) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countPrimeSetBits(int left, int right) {
        boolean[] isPrime = new boolean[21];
        int[] primes = {2, 3, 5, 7, 11, 13, 17, 19};
        for (int p : primes) {
            isPrime[p] = true;
        }
        int count = 0;
        for (int i = left; i <= right; i++) {
            if (isPrime[Integer.bitCount(i)]) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19}
        cnt = 0
        # Use built-in bit_count if available (Python 3.8+), else fallback to bin count
        bitcount = int.bit_count if hasattr(int, "bit_count") else lambda x: bin(x).count('1')
        for num in range(left, right + 1):
            if bitcount(num) in prime_set:
                cnt += 1
        return cnt
```

## Python3

```python
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        cnt = 0
        for num in range(left, right + 1):
            # Use built-in bit_count if available (Python 3.8+), else fallback to bin count
            bits = num.bit_count() if hasattr(num, "bit_count") else bin(num).count('1')
            if bits in primes:
                cnt += 1
        return cnt
```

## C

```c
int countPrimeSetBits(int left, int right) {
    static const int primes[] = {2, 3, 5, 7, 11, 13, 17, 19};
    int result = 0;
    for (int i = left; i <= right; ++i) {
        int bits = __builtin_popcount(i);
        for (int j = 0; j < 8; ++j) {
            if (bits == primes[j]) {
                ++result;
                break;
            }
        }
    }
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    private static readonly HashSet<int> PrimeSet = new HashSet<int>
        { 2, 3, 5, 7, 11, 13, 17, 19 };

    public int CountPrimeSetBits(int left, int right)
    {
        int result = 0;
        for (int i = left; i <= right; i++)
        {
            if (PrimeSet.Contains(PopCount(i)))
                result++;
        }
        return result;
    }

    private int PopCount(int n)
    {
        int count = 0;
        while (n != 0)
        {
            count += n & 1;
            n >>= 1;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var countPrimeSetBits = function(left, right) {
    const primeSet = new Set([2, 3, 5, 7, 11, 13, 17, 19]);
    let ans = 0;
    for (let num = left; num <= right; ++num) {
        let cnt = 0;
        let x = num;
        while (x) {
            cnt += x & 1;
            x >>>= 1;
        }
        if (primeSet.has(cnt)) ans++;
    }
    return ans;
};
```

## Typescript

```typescript
function countPrimeSetBits(left: number, right: number): number {
    const prime = new Set([2, 3, 5, 7, 11, 13, 17, 19]);
    let result = 0;
    for (let i = left; i <= right; ++i) {
        let cnt = 0;
        let x = i;
        while (x) {
            cnt += x & 1;
            x >>>= 1;
        }
        if (prime.has(cnt)) result++;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function countPrimeSetBits($left, $right) {
        $prime = [2=>true,3=>true,5=>true,7=>true,11=>true,13=>true,17=>true,19=>true];
        $result = 0;
        for ($i = $left; $i <= $right; $i++) {
            $bits = 0;
            $x = $i;
            while ($x) {
                $x &= ($x - 1);
                $bits++;
            }
            if (isset($prime[$bits])) {
                $result++;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func countPrimeSetBits(_ left: Int, _ right: Int) -> Int {
        let primeSet: Set<Int> = [2, 3, 5, 7, 11, 13, 17, 19]
        var count = 0
        for num in left...right {
            if primeSet.contains(num.nonzeroBitCount) {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPrimeSetBits(left: Int, right: Int): Int {
        val primeSet = setOf(2, 3, 5, 7, 11, 13, 17, 19)
        var count = 0
        for (num in left..right) {
            if (primeSet.contains(Integer.bitCount(num))) {
                count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countPrimeSetBits(int left, int right) {
    const Set<int> primeBits = {2, 3, 5, 7, 11, 13, 17, 19};
    int result = 0;
    for (int num = left; num <= right; ++num) {
      int bits = _popCount(num);
      if (primeBits.contains(bits)) {
        result++;
      }
    }
    return result;
  }

  int _popCount(int n) {
    int count = 0;
    while (n != 0) {
      count += n & 1;
      n >>= 1;
    }
    return count;
  }
}
```

## Golang

```go
import "math/bits"

func countPrimeSetBits(left int, right int) int {
	primes := []bool{
		false, //0
		false, //1
		true,  //2
		true,  //3
		false, //4
		true,  //5
		false, //6
		true,  //7
		false, //8
		false, //9
		false, //10
		true,  //11
		false, //12
		true,  //13
		false, //14
		false, //15
		false, //16
		true,  //17
		false, //18
		true,  //19
	}
	count := 0
	for i := left; i <= right; i++ {
		if primes[bits.OnesCount(uint(i))] {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def count_prime_set_bits(left, right)
  prime_set = {2 => true, 3 => true, 5 => true, 7 => true, 11 => true, 13 => true, 17 => true, 19 => true}
  count = 0
  (left..right).each do |num|
    bits = num.to_s(2).count('1')
    count += 1 if prime_set[bits]
  end
  count
end
```

## Scala

```scala
object Solution {
  private val primeSet = Set(2, 3, 5, 7, 11, 13, 17, 19)

  def countPrimeSetBits(left: Int, right: Int): Int = {
    var count = 0
    var i = left
    while (i <= right) {
      if (primeSet.contains(Integer.bitCount(i))) count += 1
      i += 1
    }
    count
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_prime_set_bits(left: i32, right: i32) -> i32 {
        let mut is_prime = [false; 21];
        for &p in &[2usize, 3, 5, 7, 11, 13, 17, 19] {
            is_prime[p] = true;
        }
        let mut ans = 0i32;
        for num in left..=right {
            let bits = (num as u32).count_ones() as usize;
            if is_prime[bits] {
                ans += 1;
            }
        }
        ans
    }
}
```

## Racket

```racket
(require racket/bitwise)

(define/contract (count-prime-set-bits left right)
  (-> exact-integer? exact-integer? exact-integer?)
  (for/sum ([i (in-range left (+ right 1))])
    (let ([c (bitwise-bit-count i)])
      (if (or (= c 2) (= c 3) (= c 5) (= c 7)
              (= c 11) (= c 13) (= c 17) (= c 19))
          1
          0))))
```

## Erlang

```erlang
-module(solution).
-export([count_prime_set_bits/2]).

-spec count_prime_set_bits(Left :: integer(), Right :: integer()) -> integer().
count_prime_set_bits(Left, Right) ->
    PrimeSet = #{2 => true, 3 => true, 5 => true, 7 => true,
                 11 => true, 13 => true, 17 => true, 19 => true},
    count_loop(Left, Right, PrimeSet, 0).

count_loop(Cur, Right, _PrimeSet, Acc) when Cur > Right ->
    Acc;
count_loop(Cur, Right, PrimeSet, Acc) ->
    Bits = popcnt(Cur),
    NewAcc = case maps:is_key(Bits, PrimeSet) of
                true -> Acc + 1;
                false -> Acc
             end,
    count_loop(Cur + 1, Right, PrimeSet, NewAcc).

popcnt(N) -> popcnt(N, 0).
popcnt(0, Acc) -> Acc;
popcnt(N, Acc) ->
    popcnt(N bsr 1, Acc + (N band 1)).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @prime_bits MapSet.new([2, 3, 5, 7, 11, 13, 17, 19])

  @spec count_prime_set_bits(left :: integer, right :: integer) :: integer
  def count_prime_set_bits(left, right) do
    Enum.reduce(left..right, 0, fn n, acc ->
      if MapSet.member?(@prime_bits, popcount(n)), do: acc + 1, else: acc
    end)
  end

  defp popcount(0), do: 0
  defp popcount(n), do: popcount_loop(n, 0)

  defp popcount_loop(0, cnt), do: cnt
  defp popcount_loop(n, cnt), do: popcount_loop(n &&& (n - 1), cnt + 1)
end
```
