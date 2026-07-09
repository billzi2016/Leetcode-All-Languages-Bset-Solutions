# 2571. Minimum Operations to Reduce an Integer to 0

## Cpp

```cpp
class Solution {
public:
    int minOperations(int n) {
        const int INF = 1e9;
        int dp0 = 0;          // no pending carry
        int dp1 = INF;        // pending carry (added 1 at previous lower bit)
        for (int i = 0; i < 31; ++i) {   // enough for n <= 1e5, safe for int range
            int b = (n >> i) & 1;
            int ndp0 = INF, ndp1 = INF;
            // transition from state with no carry
            if (b == 0) {
                ndp0 = std::min(ndp0, dp0);               // nothing needed
            } else { // b == 1
                ndp0 = std::min(ndp0, dp0 + 1);           // subtract 2^i
                ndp1 = std::min(ndp1, dp0 + 1);           // add 2^i -> carry forward
            }
            // transition from state with a pending carry
            if (dp1 != INF) {
                int total = b + 1; // current bit after applying the carry
                if (total == 0) { // impossible for binary bits, but keep for completeness
                    ndp0 = std::min(ndp0, dp1);
                } else if (total == 1) {
                    ndp0 = std::min(ndp0, dp1 + 1);       // subtract to clear this bit
                    ndp1 = std::min(ndp1, dp1 + 1);       // add and keep carry
                } else { // total == 2
                    // becomes 0 with a carry to next higher bit
                    ndp1 = std::min(ndp1, dp1);
                }
            }
            dp0 = ndp0;
            dp1 = ndp1;
        }
        return std::min(dp0, dp1 + 1); // if a carry remains, one extra operation clears it
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int n) {
        int ops = 0;
        while (n != 0) {
            if ((n & 1) == 0) {
                n >>= 1;
            } else {
                // n is odd
                if (n == 3 || (n & 3) == 1) {
                    n--;
                } else {
                    n++;
                }
                ops++;
            }
        }
        return ops;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        ops = 0
        while n:
            if n & 1 == 0:
                n >>= 1
            else:
                # Choose to add or subtract based on lower bits
                if n == 3 or (n & 3) == 1:
                    n -= 1
                else:
                    n += 1
                ops += 1
        return ops
```

## Python3

```python
class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        carry = 0
        while n:
            cur = (n & 1) + carry
            if cur == 0:
                pass
            elif cur == 1:
                ans += 1
                # decide whether to propagate a carry
                if n & 2:
                    carry = 1
                else:
                    carry = 0
            else:  # cur == 2
                # no operation needed, just propagate the carry
                carry = 1
            n >>= 1
        if carry:
            ans += 1
        return ans
```

## C

```c
int minOperations(int n) {
    int ans = 0;
    while (n > 0) {
        if ((n & 1) == 0) {
            n >>= 1;
        } else {
            if (n == 3 || (n & 3) == 1) {
                ++ans;
                n -= 1;
            } else {
                ++ans;
                n += 1;
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int n) {
        int ops = 0;
        while (n > 0) {
            if ((n & 1) == 0) {
                n >>= 1;
            } else {
                // n is odd
                if (n % 4 == 1 || n == 1) {
                    n--;
                } else {
                    n++;
                }
                ops++;
            }
        }
        return ops;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var minOperations = function(n) {
    let ops = 0;
    while (n > 0) {
        if ((n & 1) === 0) {
            n >>= 1; // divide by 2 when even
        } else {
            if (n === 1 || ((n >> 1) & 1) === 0) {
                // better to subtract 1
                ops++;
                n--;
            } else {
                // better to add 1
                ops++;
                n++;
            }
        }
    }
    return ops;
};
```

## Typescript

```typescript
function minOperations(n: number): number {
    const INF = Number.MAX_SAFE_INTEGER;
    let dp0 = 0, dp1 = INF; // dp[carry]
    for (let i = 0; i < 60; ++i) {
        const bit = (n >> i) & 1;
        let ndp0 = INF, ndp1 = INF;
        // carry = 0
        if (dp0 !== INF) {
            const sum = bit;
            // no operation
            const nc0 = Math.floor(sum / 2);
            if (nc0 === 0) ndp0 = Math.min(ndp0, dp0);
            else ndp1 = Math.min(ndp1, dp0);
            // if sum is odd, we can add or subtract 1
            if (sum % 2 === 1) {
                const ncSub = Math.floor((sum - 1) / 2);
                const ncAdd = Math.floor((sum + 1) / 2);
                if (ncSub === 0) ndp0 = Math.min(ndp0, dp0 + 1);
                else ndp1 = Math.min(ndp1, dp0 + 1);
                if (ncAdd === 0) ndp0 = Math.min(ndp0, dp0 + 1);
                else ndp1 = Math.min(ndp1, dp0 + 1);
            }
        }
        // carry = 1
        if (dp1 !== INF) {
            const sum = bit + 1;
            const nc0 = Math.floor(sum / 2);
            if (nc0 === 0) ndp0 = Math.min(ndp0, dp1);
            else ndp1 = Math.min(ndp1, dp1);
            if (sum % 2 === 1) {
                const ncSub = Math.floor((sum - 1) / 2);
                const ncAdd = Math.floor((sum + 1) / 2);
                if (ncSub === 0) ndp0 = Math.min(ndp0, dp1 + 1);
                else ndp1 = Math.min(ndp1, dp1 + 1);
                if (ncAdd === 0) ndp0 = Math.min(ndp0, dp1 + 1);
                else ndp1 = Math.min(ndp1, dp1 + 1);
            }
        }
        dp0 = ndp0;
        dp1 = ndp1;
    }
    return dp0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function minOperations($n) {
        $ans = 0;
        while ($n > 0) {
            if (($n & 1) == 0) {
                // n is even, divide by 2 (right shift)
                $n >>= 1;
            } else {
                // n is odd, perform an operation
                $ans++;
                // Choose to add or subtract based on the lower two bits,
                // with a special case for n == 3.
                if ($n % 4 == 1 || $n == 3) {
                    $n--;
                } else {
                    $n++;
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ n: Int) -> Int {
        let INF = Int.max / 2
        var dpNoCarry = 0          // minimum ops with no incoming carry at current bit
        var dpCarry = INF          // minimum ops with an incoming carry (i.e., we have added 1 to this position)

        for i in 0..<63 {   // enough bits for 64‑bit integers
            let bit = (n >> i) & 1
            var nextNoCarry = INF
            var nextCarry = INF

            // Transition from state without carry
            if dpNoCarry < INF {
                if bit == 0 {
                    nextNoCarry = min(nextNoCarry, dpNoCarry)
                } else { // bit == 1
                    // Subtract 2^i
                    nextNoCarry = min(nextNoCarry, dpNoCarry + 1)
                    // Add 2^i -> creates a carry to the next higher bit
                    nextCarry = min(nextCarry, dpNoCarry + 1)
                }
            }

            // Transition from state with a carry (value at this position is bit + 1)
            if dpCarry < INF {
                let cur = bit + 1
                if cur == 1 {
                    // Need one operation to make it zero (subtract or add another power of two)
                    nextNoCarry = min(nextNoCarry, dpCarry + 1)
                    nextCarry = min(nextCarry, dpCarry + 1)
                } else if cur == 2 {
                    // Already zero with a carry forward; no extra operation needed
                    nextCarry = min(nextCarry, dpCarry)
                }
            }

            dpNoCarry = nextNoCarry
            dpCarry = nextCarry
        }

        var answer = dpNoCarry
        if dpCarry < INF {
            // If a carry remains after the most significant bit, one extra operation is required
            answer = min(answer, dpCarry + 1)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(n: Int): Int {
        var x = n.toLong()
        var ops = 0
        while (x != 0L) {
            if ((x and 1L) == 0L) {
                // even, just shift right (divide by 2) without counting an operation
                x = x shr 1
            } else {
                // odd number: decide to add or subtract 1
                if (x == 3L || (x and 3L) == 1L) {
                    // better to subtract 1
                    x--
                } else {
                    // better to add 1
                    x++
                }
                ops++
            }
        }
        return ops
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(int n) {
    int ans = 0;
    int carry = 0;
    for (int i = 0; i < 63; ++i) {
      int bit = (n >> i) & 1;
      int cur = bit + carry;
      if (cur == 0) {
        // do nothing
      } else if (cur == 1) {
        ans++;
        int nextBit = (n >> (i + 1)) & 1;
        if (nextBit == 1) {
          carry = 1; // add operation, propagate carry
        } else {
          carry = 0; // subtract operation
        }
      } else { // cur == 2
        carry = 1; // effectively zero with a carry forward
      }
    }
    if (carry > 0) ans++;
    return ans;
  }
}
```

## Golang

```go
func minOperations(n int) int {
    cnt := 0
    x := int64(n)
    for x > 0 {
        if x&1 == 0 {
            x >>= 1
        } else {
            if x == 1 || (x&3) == 1 {
                cnt++
                x--
            } else {
                cnt++
                x++
            }
        }
    }
    return cnt
}
```

## Ruby

```ruby
def min_operations(n)
  ops = 0
  while n > 0
    if (n & 1) == 0
      n >>= 1
    else
      ops += 1
      if n == 1 || (n & 3) == 1
        n -= 1
      else
        n += 1
      end
    end
  end
  ops
end
```

## Scala

```scala
object Solution {
    def minOperations(n: Int): Int = {
        var x: Long = n.toLong
        var ops = 0
        while (x != 0) {
            if ((x & 1L) == 0) {
                x >>= 1
            } else {
                if (x == 1 || ((x >> 1) & 1L) == 0) {
                    x -= 1
                } else {
                    x += 1
                }
                ops += 1
            }
        }
        ops
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(n: i32) -> i32 {
        let mut x = n as i64;
        let mut ans = 0i32;
        while x != 0 {
            if (x & 1) == 0 {
                // even, just shift right (no operation needed)
                x >>= 1;
            } else {
                // odd
                if x == 1 {
                    ans += 1; // subtract 2^0
                    break;
                }
                // decide whether to add or subtract 1 (i.e., 2^0) based on next two bits
                // if the lower two bits are 01 or the number is 3, better to decrement
                if (x & 3) == 1 || x == 3 {
                    x -= 1;
                } else {
                    x += 1;
                }
                ans += 1;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-operations n)
  (-> exact-integer? exact-integer?)
  (let loop ((x n) (cnt 0))
    (if (= x 0)
        cnt
        (if (zero? (bitwise-and x 1))               ; even
            (loop (arithmetic-shift x -1) cnt)     ; divide by 2
            (let* ((is-three (= x 3))
                   (mod4 (bitwise-and x 3))
                   (x' (if (or is-three (= mod4 1))
                           (- x 1)                ; subtract 1
                           (+ x 1))))             ; add 1
              (loop (arithmetic-shift x' -1) (+ cnt 1)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_operations/1]).

-spec min_operations(N :: integer()) -> integer().
min_operations(N) ->
    min_ops(N, 0).

%% internal recursive helper
min_ops(0, Acc) -> Acc;
min_ops(1, Acc) -> Acc + 1;
min_ops(N, Acc) when (N band 1) =:= 0 ->
    min_ops(N bsr 1, Acc);
min_ops(N, Acc) ->
    case N of
        3 ->
            % optimal to decrement
            min_ops((N - 1) bsr 1, Acc + 1);
        _ ->
            case (N band 3) of
                1 -> % ends with ...01
                    min_ops((N - 1) bsr 1, Acc + 1);
                _ -> % ends with ...11
                    min_ops((N + 1) bsr 1, Acc + 1)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(n :: integer) :: integer
  def min_operations(n) do
    helper(n, 0)
  end

  defp helper(0, acc), do: acc

  defp helper(n, acc) when rem(n, 2) == 0 do
    helper(div(n, 2), acc)
  end

  defp helper(n, acc) do
    if n == 3 or rem(div(n, 2), 2) == 0 do
      # subtract 1
      helper(div(n - 1, 2), acc + 1)
    else
      # add 1
      helper(div(n + 1, 2), acc + 1)
    end
  end
end
```
