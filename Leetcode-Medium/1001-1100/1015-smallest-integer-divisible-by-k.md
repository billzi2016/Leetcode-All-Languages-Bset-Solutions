# 1015. Smallest Integer Divisible by K

## Cpp

```cpp
class Solution {
public:
    int smallestRepunitDivByK(int k) {
        if (k % 2 == 0 || k % 5 == 0) return -1;
        int remainder = 0;
        for (int length = 1; length <= k; ++length) {
            remainder = (remainder * 10 + 1) % k;
            if (remainder == 0) return length;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int smallestRepunitDivByK(int k) {
        if (k % 2 == 0 || k % 5 == 0) return -1;
        int remainder = 0;
        for (int len = 1; len <= k; len++) {
            remainder = (remainder * 10 + 1) % k;
            if (remainder == 0) return len;
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1
        remainder = 0
        length = 0
        for _ in range(k):
            remainder = (remainder * 10 + 1) % k
            length += 1
            if remainder == 0:
                return length
        return -1
```

## Python3

```python
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        remainder = 0
        length = 0
        for _ in range(k):
            remainder = (remainder * 10 + 1) % k
            length += 1
            if remainder == 0:
                return length
        return -1
```

## C

```c
int smallestRepunitDivByK(int k) {
    if (k % 2 == 0 || k % 5 == 0) return -1;
    int remainder = 1 % k;
    int length = 1;
    while (remainder != 0) {
        remainder = (remainder * 10 + 1) % k;
        ++length;
        if (length > k) return -1; // loop detected
    }
    return length;
}
```

## Csharp

```csharp
public class Solution {
    public int SmallestRepunitDivByK(int k) {
        if (k % 2 == 0 || k % 5 == 0) return -1;
        int remainder = 0;
        for (int length = 1; length <= k; length++) {
            remainder = (remainder * 10 + 1) % k;
            if (remainder == 0) return length;
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} k
 * @return {number}
 */
var smallestRepunitDivByK = function(k) {
    // Repunits cannot be divisible by 2 or 5
    if (k % 2 === 0 || k % 5 === 0) return -1;
    
    let remainder = 0;
    for (let length = 1; length <= k; ++length) {
        remainder = (remainder * 10 + 1) % k;
        if (remainder === 0) return length;
    }
    return -1;
};
```

## Typescript

```typescript
function smallestRepunitDivByK(k: number): number {
    // If k is divisible by 2 or 5, such a repunit can never be divisible by k
    if (k % 2 === 0 || k % 5 === 0) return -1;

    let remainder = 0;
    for (let length = 1; length <= k; ++length) {
        remainder = (remainder * 10 + 1) % k;
        if (remainder === 0) return length;
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $k
     * @return Integer
     */
    function smallestRepunitDivByK($k) {
        if ($k % 2 == 0 || $k % 5 == 0) {
            return -1;
        }
        $remainder = 0;
        for ($len = 1; $len <= $k; $len++) {
            $remainder = ($remainder * 10 + 1) % $k;
            if ($remainder === 0) {
                return $len;
            }
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func smallestRepunitDivByK(_ k: Int) -> Int {
        if k % 2 == 0 || k % 5 == 0 { return -1 }
        var remainder = 0
        for length in 1...k {
            remainder = (remainder * 10 + 1) % k
            if remainder == 0 {
                return length
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestRepunitDivByK(k: Int): Int {
        if (k % 2 == 0 || k % 5 == 0) return -1
        var remainder = 0
        for (len in 1..k) {
            remainder = (remainder * 10 + 1) % k
            if (remainder == 0) return len
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int smallestRepunitDivByK(int k) {
    if (k % 2 == 0 || k % 5 == 0) return -1;
    int rem = 0;
    for (int len = 1; len <= k; ++len) {
      rem = (rem * 10 + 1) % k;
      if (rem == 0) return len;
    }
    return -1;
  }
}
```

## Golang

```go
func smallestRepunitDivByK(k int) int {
	if k%2 == 0 || k%5 == 0 {
		return -1
	}
	remainder := 0
	for length := 1; length <= k; length++ {
		remainder = (remainder*10 + 1) % k
		if remainder == 0 {
			return length
		}
	}
	return -1
}
```

## Ruby

```ruby
def smallest_repunit_div_by_k(k)
  return -1 if k % 2 == 0 || k % 5 == 0
  rem = 0
  (1..k).each do |len|
    rem = (rem * 10 + 1) % k
    return len if rem.zero?
  end
  -1
end
```

## Scala

```scala
object Solution {
    def smallestRepunitDivByK(k: Int): Int = {
        if (k % 2 == 0 || k % 5 == 0) return -1
        var remainder = 0
        var length = 0
        for (_ <- 1 to k) {
            remainder = (remainder * 10 + 1) % k
            length += 1
            if (remainder == 0) return length
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_repunit_div_by_k(k: i32) -> i32 {
        if k % 2 == 0 || k % 5 == 0 {
            return -1;
        }
        let mut rem: i64 = 0;
        let kk = k as i64;
        for len in 1..=k {
            rem = (rem * 10 + 1) % kk;
            if rem == 0 {
                return len as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (smallest-repunit-div-by-k k)
  (-> exact-integer? exact-integer?)
  (if (or (= (modulo k 2) 0) (= (modulo k 5) 0))
      -1
      (let loop ((len 1) (rem (modulo 1 k)))
        (cond [(= rem 0) len]
              [(> len k) -1]
              [else (loop (+ len 1)
                          (modulo (+ (* rem 10) 1) k))]))))
```

## Erlang

```erlang
-spec smallest_repunit_div_by_k(K :: integer()) -> integer().
smallest_repunit_div_by_k(K) when K > 0 ->
    if
        K rem 2 =:= 0; K rem 5 =:= 0 ->
            -1;
        true ->
            find_len(K, 0, 0)
    end.

find_len(K, Rem, Len) when Len >= K -> -1;
find_len(K, Rem, Len) ->
    NewRem = (Rem * 10 + 1) rem K,
    NewLen = Len + 1,
    case NewRem of
        0 -> NewLen;
        _ -> find_len(K, NewRem, NewLen)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_repunit_div_by_k(k :: integer) :: integer
  def smallest_repunit_div_by_k(k) do
    if rem(k, 2) == 0 or rem(k, 5) == 0 do
      -1
    else
      loop(k, 0, 0, k)
    end
  end

  defp loop(_k, _rem, _len, 0), do: -1

  defp loop(k, rem, len, steps_left) when steps_left > 0 do
    new_rem = (rem * 10 + 1) |> rem(k)
    new_len = len + 1

    if new_rem == 0 do
      new_len
    else
      loop(k, new_rem, new_len, steps_left - 1)
    end
  end
end
```
