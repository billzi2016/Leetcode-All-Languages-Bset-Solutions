# 3370. Smallest Number With All Set Bits

## Cpp

```cpp
class Solution {
public:
    int smallestNumber(int n) {
        // If n already has all bits set (i.e., n+1 is a power of two)
        if ((n & (n + 1)) == 0) return n;
        int p = 1;
        while (p <= n) {
            p <<= 1;
        }
        return p - 1;
    }
};
```

## Java

```java
class Solution {
    public int smallestNumber(int n) {
        // Number of bits needed to represent n
        int bits = 32 - Integer.numberOfLeadingZeros(n);
        // For numbers that are already all ones, this gives the correct result.
        return (1 << bits) - 1;
    }
}
```

## Python

```python
class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # If n already has all bits set (i.e., of form 2^k - 1)
        if n & (n + 1) == 0:
            return n
        # Next power of two greater than n, then subtract 1
        next_pow = 1 << n.bit_length()
        return next_pow - 1
```

## Python3

```python
class Solution:
    def smallestNumber(self, n: int) -> int:
        k = n.bit_length()
        cand = (1 << k) - 1
        if cand >= n:
            return cand
        return (1 << (k + 1)) - 1
```

## C

```c
int smallestNumber(int n) {
    int x = 1;
    while (x < n) {
        x = (x << 1) | 1;
    }
    return x;
}
```

## Csharp

```csharp
public class Solution {
    public int SmallestNumber(int n) {
        // If n already has all bits set (e.g., 3 -> 11b, 7 -> 111b)
        if ((n & (n + 1)) == 0) return n;
        int p = 1;
        while (p <= n) {
            p <<= 1; // find the smallest power of two greater than n
        }
        return p - 1; // all lower bits set
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var smallestNumber = function(n) {
    if ((n & (n + 1)) === 0) return n;
    let p = 1;
    while (p <= n) {
        p <<= 1;
    }
    return p - 1;
};
```

## Typescript

```typescript
function smallestNumber(n: number): number {
    // If n already has all bits set, return it.
    if ((n & (n + 1)) === 0) {
        return n;
    }
    let p = 1;
    while (p <= n) {
        p <<= 1;
    }
    return p - 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function smallestNumber($n) {
        // Find number of bits needed to represent n
        $len = 0;
        $temp = $n;
        while ($temp > 0) {
            $len++;
            $temp >>= 1;
        }
        // Candidate with all ones of length $len
        $candidate = (1 << $len) - 1;
        if ($candidate >= $n) {
            return $candidate;
        }
        // Next length
        return ((1 << ($len + 1)) - 1);
    }
}
```

## Swift

```swift
class Solution {
    func smallestNumber(_ n: Int) -> Int {
        var power = 1
        while power < n + 1 {
            power <<= 1
        }
        return power - 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestNumber(n: Int): Int {
        if ((n and (n + 1)) == 0) return n
        var p = 1
        while (p <= n) {
            p = p shl 1
        }
        return p - 1
    }
}
```

## Dart

```dart
class Solution {
  int smallestNumber(int n) {
    if ((n & (n + 1)) == 0) return n;
    int p = 1;
    while (p <= n) {
      p <<= 1;
    }
    return p - 1;
  }
}
```

## Golang

```go
func smallestNumber(n int) int {
	// If n already has all bits set, return it.
	if n&(n+1) == 0 {
		return n
	}
	// Find the next power of two greater than n.
	p := 1
	for p <= n {
		p <<= 1
	}
	return p - 1
}
```

## Ruby

```ruby
def smallest_number(n)
  k = n.bit_length
  x = (1 << k) - 1
  x >= n ? x : ((1 << (k + 1)) - 1)
end
```

## Scala

```scala
object Solution {
    def smallestNumber(n: Int): Int = {
        var x = 1
        while (x < n) {
            x = (x << 1) | 1
        }
        x
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_number(n: i32) -> i32 {
        let mut p = 1i32;
        while p <= n {
            p <<= 1;
        }
        p - 1
    }
}
```

## Racket

```racket
(define/contract (smallest-number n)
  (-> exact-integer? exact-integer?)
  (let* ([k (integer-length n)]
         [candidate (sub1 (expt 2 k))])
    candidate))
```

## Erlang

```erlang
-module(solution).
-export([smallest_number/1]).

-spec smallest_number(N :: integer()) -> integer().
smallest_number(N) ->
    Target = N + 1,
    P = next_power_of_two(Target, 1),
    P - 1.

next_power_of_two(Target, Acc) when Acc >= Target ->
    Acc;
next_power_of_two(Target, Acc) ->
    next_power_of_two(Target, Acc * 2).
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_number(n :: integer) :: integer
  def smallest_number(n) do
    Enum.reduce_while(0..60, nil, fn k, _ ->
      cand = (1 <<< k) - 1
      if cand >= n do
        {:halt, cand}
      else
        {:cont, nil}
      end
    end)
  end
end
```
