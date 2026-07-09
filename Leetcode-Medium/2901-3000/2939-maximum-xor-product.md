# 2939. Maximum Xor Product

## Cpp

```cpp
class Solution {
public:
    int maximumXorProduct(long long a, long long b, int n) {
        const long long MOD = 1000000007LL;
        unsigned long long A = (unsigned long long)a;
        unsigned long long B = (unsigned long long)b;
        for (int i = n - 1; i >= 0; --i) {
            unsigned long long mask = 1ULL << i;
            int ai = (a >> i) & 1LL;
            int bi = (b >> i) & 1LL;
            if (ai == bi) {
                A |= mask;
                B |= mask;
            } else {
                if (A < B) {
                    A |= mask;          // give 1 to A
                    B &= ~mask;         // ensure 0 for B
                } else {
                    B |= mask;          // give 1 to B
                    A &= ~mask;         // ensure 0 for A
                }
            }
        }
        long long aMod = (long long)(A % MOD);
        long long bMod = (long long)(B % MOD);
        long long result = (long long)((__int128)aMod * bMod % MOD);
        return (int)result;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    public int maximumXorProduct(long a, long b, int n) {
        long A = a;
        long B = b;
        for (int i = n - 1; i >= 0; --i) {
            long mask = 1L << i;
            int ai = (int) ((a >> i) & 1L);
            int bi = (int) ((b >> i) & 1L);
            if (ai == bi) {
                // make both bits 1
                A |= mask;
                B |= mask;
            } else {
                if (A < B) {
                    // give the 1 to A, 0 to B at this bit
                    A |= mask;
                    B &= ~mask;
                } else {
                    // give the 1 to B, 0 to A at this bit
                    B |= mask;
                    A &= ~mask;
                }
            }
        }
        java.math.BigInteger prod = java.math.BigInteger.valueOf(A)
                .multiply(java.math.BigInteger.valueOf(B))
                .mod(java.math.BigInteger.valueOf(MOD));
        return prod.intValue();
    }
}
```

## Python

```python
class Solution(object):
    def maximumXorProduct(self, a, b, n):
        """
        :type a: int
        :type b: int
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        prefA = 0
        prefB = 0
        for i in range(n - 1, -1, -1):
            abit = (a >> i) & 1
            bbit = (b >> i) & 1
            if abit == bbit:
                # make both bits 1
                prefA = (prefA << 1) | 1
                prefB = (prefB << 1) | 1
            else:
                # give the 1 to the currently smaller number
                if prefA <= prefB:
                    prefA = (prefA << 1) | 1
                    prefB = (prefB << 1)
                else:
                    prefA = (prefA << 1)
                    prefB = (prefB << 1) | 1
        return (prefA * prefB) % MOD
```

## Python3

```python
class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10**9 + 7
        # Preserve bits above n (they are unchanged because x < 2^n)
        A = (a >> n) << n
        B = (b >> n) << n

        for i in range(n - 1, -1, -1):
            ai = (a >> i) & 1
            bi = (b >> i) & 1
            if ai == bi:
                # we can make both bits 1
                A |= (1 << i)
                B |= (1 << i)
            else:
                # give the high bit to the currently smaller number
                if A < B:
                    A |= (1 << i)
                else:
                    B |= (1 << i)

        return (A % MOD) * (B % MOD) % MOD
```

## C

```c
int maximumXorProduct(long long a, long long b, int n) {
    const long long MOD = 1000000007LL;
    unsigned long long mask = (n == 0) ? 0ULL : ((1ULL << n) - 1);
    unsigned long long p = ((unsigned long long)a) & ~mask; // high bits stay unchanged
    unsigned long long q = ((unsigned long long)b) & ~mask;
    for (int i = n - 1; i >= 0; --i) {
        unsigned long long bit = 1ULL << i;
        int ai = (a >> i) & 1LL;
        int bi = (b >> i) & 1LL;
        if (ai == bi) {
            p |= bit;
            q |= bit;
        } else {
            if (p < q) {
                p |= bit;
            } else {
                q |= bit;
            }
        }
    }
    long long res = (long long)((__int128)p * (__int128)q % MOD);
    return (int)res;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const long MOD = 1_000_000_007L;
    
    private static int BitLength(long v) {
        if (v == 0) return 0;
        int len = 0;
        while (v != 0) {
            len++;
            v >>= 1;
        }
        return len;
    }

    public int MaximumXorProduct(long a, long b, int n) {
        // If n is zero, x can only be 0
        if (n == 0) {
            long res = ((a % MOD) * (b % MOD)) % MOD;
            return (int)res;
        }

        int lenA = BitLength(a);
        int lenB = BitLength(b);
        int maxBit = Math.Max(Math.Max(lenA, lenB), n) - 1; // highest index to process

        long A = 0, B = 0;

        for (int i = maxBit; i >= 0; i--) {
            int ai = ((a >> i) & 1L) == 1L ? 1 : 0;
            int bi = ((b >> i) & 1L) == 1L ? 1 : 0;

            int bitA, bitB;

            if (i >= n) {
                // x's bit forced to 0, values stay as original
                bitA = ai;
                bitB = bi;
            } else {
                if (ai == bi) {
                    // make both bits 1 by flipping if needed
                    bitA = 1;
                    bitB = 1;
                } else {
                    // give the 1 to the currently smaller number
                    if (A < B) {
                        bitA = 1;
                        bitB = 0;
                    } else {
                        bitA = 0;
                        bitB = 1;
                    }
                }
            }

            A = (A << 1) | bitA;
            B = (B << 1) | bitB;
        }

        long result = ((A % MOD) * (B % MOD)) % MOD;
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @param {number} n
 * @return {number}
 */
var maximumXorProduct = function(a, b, n) {
    const MOD = 1000000007n;
    if (n === 0) return Number((BigInt(a) * BigInt(b)) % MOD);
    let A = BigInt(a), B = BigInt(b);
    let p = 0n, q = 0n;
    for (let i = n - 1; i >= 0; --i) {
        const mask = 1n << BigInt(i);
        const bitA = (A >> BigInt(i)) & 1n;
        const bitB = (B >> BigInt(i)) & 1n;
        if (bitA === bitB) {
            p |= mask;
            q |= mask;
        } else {
            if (p < q) {
                p |= mask;
            } else {
                q |= mask;
            }
        }
    }
    return Number((p * q) % MOD);
};
```

## Typescript

```typescript
function maximumXorProduct(a: number, b: number, n: number): number {
    const MOD = 1000000007n;
    let A = 0n, B = 0n;
    const aBig = BigInt(a);
    const bBig = BigInt(b);
    for (let i = n - 1; i >= 0; i--) {
        const mask = 1n << BigInt(i);
        const aBit = (aBig >> BigInt(i)) & 1n;
        const bBit = (bBig >> BigInt(i)) & 1n;
        if (aBit === bBit) {
            A |= mask;
            B |= mask;
        } else {
            if (A < B) {
                A |= mask;
            } else {
                B |= mask;
            }
        }
    }
    const result = ((A % MOD) * (B % MOD)) % MOD;
    return Number(result);
}
```

## Php

```php
class Solution {
    const MOD = 1000000007;

    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $n
     * @return Integer
     */
    function maximumXorProduct($a, $b, $n) {
        if ($n == 0) {
            return $this->mulMod($a % self::MOD, $b % self::MOD, self::MOD);
        }

        $curA = 0;
        $curB = 0;

        for ($i = $n - 1; $i >= 0; $i--) {
            $ai = ($a >> $i) & 1;
            $bi = ($b >> $i) & 1;
            if ($ai == $bi) {
                $curA = ($curA << 1) | 1;
                $curB = ($curB << 1) | 1;
            } else {
                if ($curA < $curB) {
                    $curA = ($curA << 1) | 1;
                    $curB = ($curB << 1);
                } else {
                    $curA = ($curA << 1);
                    $curB = ($curB << 1) | 1;
                }
            }
        }

        $mask   = (1 << $n) - 1;          // lower n bits set
        $upperA = $a & (~$mask);           // bits above n unchanged
        $upperB = $b & (~$mask);

        $finalA = $upperA | $curA;
        $finalB = $upperB | $curB;

        return $this->mulMod($finalA % self::MOD, $finalB % self::MOD, self::MOD);
    }

    private function mulMod($a, $b, $mod) {
        $result = 0;
        while ($b > 0) {
            if ($b & 1) {
                $result = ($result + $a) % $mod;
            }
            $a = ($a << 1) % $mod;
            $b >>= 1;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func maximumXorProduct(_ a: Int, _ b: Int, _ n: Int) -> Int {
        let MOD = 1_000_000_007
        if n == 0 {
            let res = (Int64(a % MOD) * Int64(b % MOD)) % Int64(MOD)
            return Int(res)
        }
        let aU = UInt64(a)
        let bU = UInt64(b)
        let lowMask: UInt64 = ((UInt64(1) << n) - 1)
        var p: UInt64 = aU & ~lowMask
        var q: UInt64 = bU & ~lowMask
        
        for i in stride(from: n - 1, through: 0, by: -1) {
            let bitMask: UInt64 = UInt64(1) << i
            let aBit = (aU >> i) & 1
            let bBit = (bU >> i) & 1
            if aBit == bBit {
                p |= bitMask
                q |= bitMask
            } else {
                if p < q {
                    p |= bitMask
                } else {
                    q |= bitMask
                }
            }
        }
        
        let pMod = Int64(p % UInt64(MOD))
        let qMod = Int64(q % UInt64(MOD))
        let ans = (pMod * qMod) % Int64(MOD)
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumXorProduct(a: Long, b: Long, n: Int): Int {
        val MOD = 1_000_000_007L
        var A = a
        var B = b
        for (i in n - 1 downTo 0) {
            val mask = 1L shl i
            val ai = (a and mask) != 0L
            val bi = (b and mask) != 0L
            if (ai == bi) {
                A = A or mask
                B = B or mask
            } else {
                if (A < B) {
                    A = A or mask
                    B = B and mask.inv()
                } else {
                    B = B or mask
                    A = A and mask.inv()
                }
            }
        }
        val result = ((A % MOD) * (B % MOD)) % MOD
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;
  int maximumXorProduct(int a, int b, int n) {
    int maskLow = n == 0 ? 0 : ((1 << n) - 1);
    int curA = a & (~maskLow);
    int curB = b & (~maskLow);
    for (int i = n - 1; i >= 0; --i) {
      int ai = (a >> i) & 1;
      int bi = (b >> i) & 1;
      if (ai == bi) {
        curA |= (1 << i);
        curB |= (1 << i);
      } else {
        if (curA < curB) {
          curA |= (1 << i);
        } else {
          curB |= (1 << i);
        }
      }
    }
    return ((curA % _MOD) * (curB % _MOD)) % _MOD;
  }
}
```

## Golang

```go
func maximumXorProduct(a int64, b int64, n int) int {
	const MOD int64 = 1000000007
	var x int64 = 0
	for i := n - 1; i >= 0; i-- {
		ai := (a >> i) & 1
		bi := (b >> i) & 1
		if ai == bi {
			if ai == 0 { // both zero, set this bit to make both 1
				x |= int64(1) << i
			}
			// both one -> keep x's bit 0
		} else {
			curA := (a ^ x) >> (i + 1)
			curB := (b ^ x) >> (i + 1)
			if curA < curB {
				// give a the 1 at this position
				if ai == 0 {
					x |= int64(1) << i
				}
			} else {
				// give b the 1 at this position
				if bi == 0 {
					x |= int64(1) << i
				}
			}
		}
	}
	A := (a ^ x) % MOD
	B := (b ^ x) % MOD
	return int((A * B) % MOD)
}
```

## Ruby

```ruby
def maximum_xor_product(a, b, n)
  mod = 1_000_000_007
  a_val = a
  b_val = b
  A = 0
  B = 0
  (n - 1).downto(0) do |i|
    mask = 1 << i
    a_bit = (a_val & mask) != 0
    b_bit = (b_val & mask) != 0
    if a_bit == b_bit
      A |= mask
      B |= mask
    else
      if A < B
        A |= mask
      else
        B |= mask
      end
    end
  end
  ((A % mod) * (B % mod)) % mod
end
```

## Scala

```scala
object Solution {
    def maximumXorProduct(a: Long, b: Long, n: Int): Int = {
        val MOD = 1000000007L
        if (n == 0) return ((a % MOD) * (b % MOD) % MOD).toInt

        var A = 0L
        var B = 0L
        var i = n - 1
        while (i >= 0) {
            val mask = 1L << i
            val ai = (a >> i) & 1L
            val bi = (b >> i) & 1L
            if (ai == bi) {
                A |= mask
                B |= mask
            } else {
                if (A < B) {
                    A |= mask
                } else {
                    B |= mask
                }
            }
            i -= 1
        }
        ((A % MOD) * (B % MOD) % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_xor_product(a: i64, b: i64, n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut p = a;
        let mut q = b;
        for i in (0..n).rev() {
            let mask: i64 = 1_i64 << i;
            let ai = (a >> i) & 1;
            let bi = (b >> i) & 1;
            if ai == bi {
                // make both bits 1
                p |= mask;
                q |= mask;
            } else {
                // assign the 1 to the currently smaller number
                if p < q {
                    p |= mask;          // set bit in p
                    q &= !mask;         // clear bit in q
                } else {
                    q |= mask;          // set bit in q
                    p &= !mask;         // clear bit in p
                }
            }
        }
        let prod = ((p as i128) * (q as i128)) % MOD as i128;
        prod as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (maximum-xor-product a b n)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((c (bitwise-xor a b))
         (loop
          (lambda (i A B)
            (if (< i 0)
                (modulo (* A B) MOD)
                (let* ((mask (arithmetic-shift 1 i))
                       (ci (if (= (bitwise-and (arithmetic-shift c i) 1) 0) 0 1)))
                  (if (= ci 0)
                      (loop (sub1 i) (bitwise-ior A mask) (bitwise-ior B mask))
                      (if (< A B)
                          (loop (sub1 i) (bitwise-ior A mask) (bitwise-and B (bitwise-not mask)))
                          (loop (sub1 i) (bitwise-and A (bitwise-not mask)) (bitwise-ior B mask)))))))))
    (loop (sub1 n) a b)))
```

## Erlang

```erlang
-spec maximum_xor_product(A :: integer(), B :: integer(), N :: integer()) -> integer().
maximum_xor_product(A, B, N) ->
    Mod = 1000000007,
    MaskN = (1 bsl N) - 1,
    HighMask = bnot(MaskN),
    HighA = A band HighMask,
    HighB = B band HighMask,
    {LowA, LowB} = max_bits(N - 1, A, B, 0, 0),
    FA = HighA bor LowA,
    FB = HighB bor LowB,
    (FA * FB) rem Mod.

max_bits(-1, _A, _B, CurA, CurB) ->
    {CurA, CurB};
max_bits(I, A, B, CurA, CurB) ->
    Mask = 1 bsl I,
    Ai = (A band Mask) =/= 0,
    Bi = (B band Mask) =/= 0,
    if
        Ai == Bi ->
            NewA = CurA bor Mask,
            NewB = CurB bor Mask,
            max_bits(I - 1, A, B, NewA, NewB);
        true ->
            if
                CurA < CurB ->
                    NewA = CurA bor Mask,
                    max_bits(I - 1, A, B, NewA, CurB);
                true ->
                    NewB = CurB bor Mask,
                    max_bits(I - 1, A, B, CurA, NewB)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @moduledoc false
  @spec maximum_xor_product(a :: integer, b :: integer, n :: integer) :: integer
  def maximum_xor_product(a, b, n) do
    mod = 1_000_000_007

    if n == 0 do
      Integer.mod(a * b, mod)
    else
      {p, q} =
        Enum.reduce((n - 1)..0, {0, 0}, fn i, {pa, pb} ->
          ai = (a >>> i) &&& 1
          bi = (b >>> i) &&& 1

          if ai == bi do
            {(pa <<< 1) ||| 1, (pb <<< 1) ||| 1}
          else
            if pa < pb do
              {(pa <<< 1) ||| 1, (pb <<< 1)}
            else
              {(pa <<< 1), (pb <<< 1) ||| 1}
            end
          end
        end)

      Integer.mod(p * q, mod)
    end
  end
end
```
