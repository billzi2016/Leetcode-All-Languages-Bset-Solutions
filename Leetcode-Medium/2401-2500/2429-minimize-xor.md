# 2429. Minimize XOR

## Cpp

```cpp
class Solution {
public:
    int minimizeXor(int num1, int num2) {
        int need = __builtin_popcount(num2);
        int x = 0;
        // Match set bits of num1 from most significant to least
        for (int i = 31; i >= 0 && need > 0; --i) {
            if ((num1 >> i) & 1) {
                x |= (1 << i);
                --need;
            }
        }
        // If still need bits, set them from least significant positions
        for (int i = 0; i < 32 && need > 0; ++i) {
            if (!((x >> i) & 1)) {
                x |= (1 << i);
                --need;
            }
        }
        return x;
    }
};
```

## Java

```java
class Solution {
    public int minimizeXor(int num1, int num2) {
        int targetBits = Integer.bitCount(num2);
        int curBits = Integer.bitCount(num1);
        int result = num1;
        if (curBits > targetBits) {
            int diff = curBits - targetBits;
            for (int i = 0; i < 31 && diff > 0; i++) {
                if ((result & (1 << i)) != 0) {
                    result &= ~(1 << i);
                    diff--;
                }
            }
        } else if (curBits < targetBits) {
            int diff = targetBits - curBits;
            for (int i = 0; i < 31 && diff > 0; i++) {
                if ((result & (1 << i)) == 0) {
                    result |= (1 << i);
                    diff--;
                }
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        k = bin(num2).count('1')
        res = 0
        cnt = 0
        for i in range(31, -1, -1):
            if cnt == k:
                break
            # bits remaining below i are i positions (0..i-1)
            need = k - cnt
            bit_set = (num1 >> i) & 1
            if bit_set:
                res |= (1 << i)
                cnt += 1
            elif need > i:  # must set to have enough bits left
                res |= (1 << i)
                cnt += 1
        return res
```

## Python3

```python
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        need = bin(num2).count('1')
        ans = 0
        # Match high bits of num1 first
        for i in range(31, -1, -1):
            if need == 0:
                break
            if (num1 >> i) & 1:
                ans |= 1 << i
                need -= 1
        # Fill remaining bits from LSB upwards
        i = 0
        while need > 0:
            if ((ans >> i) & 1) == 0:
                ans |= 1 << i
                need -= 1
            i += 1
        return ans
```

## C

```c
int minimizeXor(int num1, int num2) {
    int target = __builtin_popcount(num2);
    int cur = __builtin_popcount(num1);
    int res = num1;
    
    if (cur > target) {
        int need = cur - target;               // bits to turn off
        for (int i = 0; i < 31 && need > 0; ++i) {
            if (res & (1 << i)) {
                res &= ~(1 << i);
                --need;
            }
        }
    } else if (cur < target) {
        int need = target - cur;               // bits to turn on
        for (int i = 0; i < 31 && need > 0; ++i) {
            if ((res & (1 << i)) == 0) {
                res |= (1 << i);
                --need;
            }
        }
    }
    
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimizeXor(int num1, int num2) {
        int need = CountBits(num2);
        int result = 0;
        int taken = 0;

        // Copy set bits from num1 starting from most significant bit
        for (int i = 31; i >= 0 && taken < need; --i) {
            long mask = 1L << i;
            if ((num1 & mask) != 0) {
                result |= (int)mask;
                taken++;
            }
        }

        // If still need bits, set the lowest unset positions
        for (int i = 0; i <= 31 && taken < need; ++i) {
            long mask = 1L << i;
            if ((result & mask) == 0) {
                result |= (int)mask;
                taken++;
            }
        }

        return result;
    }

    private int CountBits(int x) {
        int cnt = 0;
        while (x != 0) {
            cnt += x & 1;
            x >>= 1;
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
var minimizeXor = function(num1, num2) {
    const popcount = (x) => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    };
    
    let need = popcount(num2);
    let ans = 0;
    
    // Keep as many high bits of num1 as possible
    for (let i = 31; i >= 0 && need > 0; i--) {
        if ((num1 >>> i) & 1) {
            ans |= (1 << i);
            need--;
        }
    }
    
    // Fill remaining bits from least significant side
    for (let i = 0; i < 32 && need > 0; i++) {
        if (((ans >>> i) & 1) === 0) {
            ans |= (1 << i);
            need--;
        }
    }
    
    return ans >>> 0;
};
```

## Typescript

```typescript
function minimizeXor(num1: number, num2: number): number {
    // Count set bits in num2
    let need = 0;
    let temp = num2;
    while (temp) {
        need++;
        temp &= temp - 1;
    }

    let result = 0;

    // Align with set bits of num1 from most significant to least
    for (let i = 31; i >= 0 && need > 0; i--) {
        if ((num1 >>> i) & 1) {
            result |= (1 << i);
            need--;
        }
    }

    // Fill remaining needed bits in the lowest positions
    for (let i = 0; i < 32 && need > 0; i++) {
        if (((result >>> i) & 1) === 0) {
            result |= (1 << i);
            need--;
        }
    }

    return result;
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
    function minimizeXor($num1, $num2) {
        // count set bits needed
        $need = 0;
        $tmp = $num2;
        while ($tmp > 0) {
            $need += $tmp & 1;
            $tmp >>= 1;
        }

        $result = 0;
        $cnt = 0;

        // try to copy set bits from num1 starting from most significant bit
        for ($i = 31; $i >= 0 && $cnt < $need; $i--) {
            if ((($num1 >> $i) & 1) === 1) {
                $result |= (1 << $i);
                $cnt++;
            }
        }

        // if still need bits, set them from least significant positions
        for ($i = 0; $i <= 31 && $cnt < $need; $i++) {
            if ((($result >> $i) & 1) === 0) {
                $result |= (1 << $i);
                $cnt++;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func minimizeXor(_ num1: Int, _ num2: Int) -> Int {
        var need = num2.nonzeroBitCount
        var ans = 0

        // Match high bits of num1 first
        for i in stride(from: 31, through: 0, by: -1) {
            if need == 0 { break }
            if ((num1 >> i) & 1) == 1 {
                ans |= (1 << i)
                need -= 1
            }
        }

        // Fill remaining bits from least significant side
        var i = 0
        while need > 0 {
            if ((ans >> i) & 1) == 0 {
                ans |= (1 << i)
                need -= 1
            }
            i += 1
        }

        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimizeXor(num1: Int, num2: Int): Int {
        val targetBits = Integer.bitCount(num2)
        var result = num1
        var currentBits = Integer.bitCount(result)

        if (currentBits > targetBits) {
            var needToClear = currentBits - targetBits
            for (i in 0..31) {
                if (((result shr i) and 1) == 1) {
                    result = result and ((1 shl i).inv())
                    needToClear--
                    if (needToClear == 0) break
                }
            }
        } else if (currentBits < targetBits) {
            var needToSet = targetBits - currentBits
            for (i in 0..31) {
                if (((result shr i) and 1) == 0) {
                    result = result or (1 shl i)
                    needToSet--
                    if (needToSet == 0) break
                }
            }
        }

        return result
    }
}
```

## Dart

```dart
class Solution {
  int _popCount(int x) {
    int cnt = 0;
    while (x > 0) {
      x &= x - 1;
      cnt++;
    }
    return cnt;
  }

  int minimizeXor(int num1, int num2) {
    int need = _popCount(num2);
    int ans = 0;

    // First try to keep bits same as num1 from high to low
    for (int i = 31; i >= 0 && need > 0; i--) {
      if ((num1 >> i) & 1 == 1) {
        ans |= (1 << i);
        need--;
      }
    }

    // If still need bits, set the lowest unset bits
    for (int i = 0; i <= 31 && need > 0; i++) {
      if ((ans >> i) & 1 == 0) {
        ans |= (1 << i);
        need--;
      }
    }

    return ans;
  }
}
```

## Golang

```go
import "math/bits"

func minimizeXor(num1 int, num2 int) int {
	k := bits.OnesCount(uint(num2))
	res := 0
	cnt := 0

	// Match set bits of num1 from most significant to least.
	for i := 31; i >= 0 && cnt < k; i-- {
		if (num1>>i)&1 == 1 {
			res |= 1 << i
			cnt++
		}
	}

	// If still need bits, set the lowest unset positions.
	for i := 0; i <= 31 && cnt < k; i++ {
		if ((res >> i) & 1) == 0 {
			res |= 1 << i
			cnt++
		}
	}
	return res
}
```

## Ruby

```ruby
def minimize_xor(num1, num2)
  k = num2.to_s(2).count('1')
  res = 0
  31.downto(0) do |i|
    if ((num1 >> i) & 1) == 1 && k > 0
      res |= (1 << i)
      k -= 1
    end
  end
  0.upto(31) do |i|
    break if k == 0
    if ((res >> i) & 1) == 0
      res |= (1 << i)
      k -= 1
    end
  end
  res
end
```

## Scala

```scala
object Solution {
    def minimizeXor(num1: Int, num2: Int): Int = {
        val targetBits = Integer.bitCount(num2)
        var need = targetBits
        var result = 0

        // Try to keep the high bits same as num1
        for (i <- 31 to 0 by -1 if need > 0) {
            if (((num1 >> i) & 1) == 1) {
                result |= (1 << i)
                need -= 1
            }
        }

        // Fill remaining bits from least significant side
        var i = 0
        while (need > 0) {
            if (((result >> i) & 1) == 0) {
                result |= (1 << i)
                need -= 1
            }
            i += 1
        }

        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimize_xor(num1: i32, num2: i32) -> i32 {
        let mut ans = num1 as u32;
        let target = (num2 as u32).count_ones();
        let mut cur = ans.count_ones();

        if cur > target {
            let mut need = cur - target;
            for i in 0..32 {
                if need == 0 { break; }
                if (ans >> i) & 1 == 1 {
                    ans &= !(1u32 << i);
                    need -= 1;
                }
            }
        } else if cur < target {
            let mut need = target - cur;
            for i in 0..32 {
                if need == 0 { break; }
                if (ans >> i) & 1 == 0 {
                    ans |= 1u32 << i;
                    need -= 1;
                }
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (minimize-xor num1 num2)
  (-> exact-integer? exact-integer? exact-integer?)
  (letrec ((popcnt
            (lambda (n)
              (let loop ((x n) (c 0))
                (if (= x 0)
                    c
                    (loop (arithmetic-shift x -1)
                          (+ c (if (= (bitwise-and x 1) 1) 1 0))))))))
    (let* ((target (popcnt num2))
           (res0   num1)
           (cnt0   (popcnt num1)))
      (cond
        [(> cnt0 target)
         (let loop ((i 0) (r res0) (c cnt0))
           (if (= c target)
               r
               (if (= (bitwise-and r (arithmetic-shift 1 i)) (arithmetic-shift 1 i))
                   (loop (+ i 1) (bitwise-and r (bitwise-not (arithmetic-shift 1 i))) (- c 1))
                   (loop (+ i 1) r c))))]
        [(< cnt0 target)
         (let loop ((i 0) (r res0) (c cnt0))
           (if (= c target)
               r
               (if (= (bitwise-and r (arithmetic-shift 1 i)) 0)
                   (loop (+ i 1) (bitwise-ior r (arithmetic-shift 1 i)) (+ c 1))
                   (loop (+ i 1) r c))))]
        [else res0]))))
```

## Erlang

```erlang
-module(solution).
-export([minimize_xor/2]).

-spec popcount(integer()) -> integer().
popcount(0) -> 0;
popcount(N) -> 1 + popcount(N band (N-1)).

-spec high_pass(integer(), integer(), integer(), integer()) -> {integer(), integer()}.
high_pass(-1, _Num1, Rem, Res) -> {Rem, Res};
high_pass(_I, _Num1, 0, Res) -> {0, Res};
high_pass(I, Num1, Rem, Res) ->
    case (Num1 bsr I) band 1 of
        1 ->
            NewRes = Res bor (1 bsl I),
            high_pass(I-1, Num1, Rem-1, NewRes);
        _ ->
            high_pass(I-1, Num1, Rem, Res)
    end.

-spec low_pass(integer(), integer(), integer()) -> integer().
low_pass(_I, 0, Res) -> Res;
low_pass(I, Rem, Res) when I =< 31 ->
    case (Res bsr I) band 1 of
        0 ->
            NewRes = Res bor (1 bsl I),
            low_pass(I+1, Rem-1, NewRes);
        _ ->
            low_pass(I+1, Rem, Res)
    end;
low_pass(_I, _Rem, Res) -> Res.

-spec minimize_xor(integer(), integer()) -> integer().
minimize_xor(Num1, Num2) ->
    K = popcount(Num2),
    {Rem, Partial} = high_pass(31, Num1, K, 0),
    low_pass(0, Rem, Partial).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimize_xor(num1 :: integer, num2 :: integer) :: integer
  def minimize_xor(num1, num2) do
    import Bitwise

    needed = :erlang.popcount(num2)

    {partial, remaining} =
      Enum.reduce(31..0, {0, needed}, fn i, {acc, cnt} ->
        if cnt > 0 && ((num1 >>> i) &&& 1) == 1 do
          {acc ||| (1 <<< i), cnt - 1}
        else
          {acc, cnt}
        end
      end)

    {result, _} =
      Enum.reduce(0..31, {partial, remaining}, fn i, {acc, cnt} ->
        if cnt > 0 && ((acc >>> i) &&& 1) == 0 do
          {acc ||| (1 <<< i), cnt - 1}
        else
          {acc, cnt}
        end
      end)

    result
  end
end
```
