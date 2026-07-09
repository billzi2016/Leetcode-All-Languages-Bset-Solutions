# 0779. K-th Symbol in Grammar

## Cpp

```cpp
class Solution {
public:
    int kthGrammar(int n, int k) {
        return (__builtin_popcount(k - 1) & 1);
    }
};
```

## Java

```java
class Solution {
    public int kthGrammar(int n, int k) {
        return Integer.bitCount(k - 1) & 1;
    }
}
```

## Python

```python
class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # The symbol is determined by the parity of 1-bits in (k-1)
        return bin(k - 1).count('1') & 1
```

## Python3

```python
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k - 1).count('1') & 1
```

## C

```c
int kthGrammar(int n, int k) {
    k--;                // work with zero‑based index
    int parity = 0;     // 0 for even number of set bits, 1 for odd
    while (k) {
        parity ^= (k & 1);
        k >>= 1;
    }
    return parity;
}
```

## Csharp

```csharp
public class Solution
{
    public int KthGrammar(int n, int k)
    {
        // The value depends only on the parity of set bits in (k-1).
        int flips = 0;
        k--; // work with zero‑based index
        while (k > 0)
        {
            flips ^= (k & 1);
            k >>= 1;
        }
        return flips; // 0 if even number of flips, 1 otherwise
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
var kthGrammar = function(n, k) {
    let x = k - 1;
    let parity = 0; // 0 for even flips, 1 for odd flips
    while (x) {
        parity ^= 1;          // toggle parity for each set bit
        x &= x - 1;           // remove the lowest set bit
    }
    return parity;
};
```

## Typescript

```typescript
function kthGrammar(n: number, k: number): number {
    let x = k - 1;
    let parity = 0;
    while (x > 0) {
        parity ^= (x & 1);
        x >>>= 1;
    }
    return parity;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function kthGrammar($n, $k) {
        $parity = 0;
        $x = $k - 1;
        while ($x > 0) {
            $parity ^= ($x & 1);
            $x >>= 1;
        }
        return $parity;
    }
}
?>
```

## Swift

```swift
class Solution {
    func kthGrammar(_ n: Int, _ k: Int) -> Int {
        var x = k - 1
        var parity = 0
        while x > 0 {
            parity ^= (x & 1)
            x >>= 1
        }
        return parity
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kthGrammar(n: Int, k: Int): Int {
        return Integer.bitCount(k - 1) % 2
    }
}
```

## Dart

```dart
class Solution {
  int kthGrammar(int n, int k) {
    int flips = 0;
    k -= 1;
    while (k > 0) {
      flips ^= (k & 1);
      k >>= 1;
    }
    return flips;
  }
}
```

## Golang

```go
import "math/bits"

func kthGrammar(n int, k int) int {
	if bits.OnesCount(uint(k-1))%2 == 0 {
		return 0
	}
	return 1
}
```

## Ruby

```ruby
def kth_grammar(n, k)
  ((k - 1).to_s(2).count('1')) % 2
end
```

## Scala

```scala
object Solution {
    def kthGrammar(n: Int, k: Int): Int = {
        if ((java.lang.Integer.bitCount(k - 1) & 1) == 0) 0 else 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn kth_grammar(_n: i32, k: i32) -> i32 {
        let flips = ((k - 1) as u32).count_ones();
        (flips % 2) as i32
    }
}
```

## Racket

```racket
(require racket/bitwise)

(define/contract (kth-grammar n k)
  (-> exact-integer? exact-integer? exact-integer?)
  (modulo (bitwise-bit-count (- k 1)) 2))
```

## Erlang

```erlang
-module(solution).
-export([kth_grammar/2]).

-spec kth_grammar(integer(), integer()) -> integer().
kth_grammar(_N, K) ->
    Ones = count_ones(K - 1),
    Ones band 1.

count_ones(0) -> 0;
count_ones(X) ->
    (X band 1) + count_ones(X bsr 1).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec kth_grammar(n :: integer, k :: integer) :: integer
  def kth_grammar(_n, k) do
    flips = count_ones(k - 1)
    rem(flips, 2)
  end

  defp count_ones(0), do: 0
  defp count_ones(x) do
    (x &&& 1) + count_ones(x >>> 1)
  end
end
```
