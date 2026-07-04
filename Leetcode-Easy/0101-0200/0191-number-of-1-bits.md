# 0191. Number of 1 Bits

## Cpp

```cpp
class Solution {
public:
    int hammingWeight(int n) {
        unsigned int x = static_cast<unsigned int>(n);
        int cnt = 0;
        while (x) {
            x &= (x - 1);
            ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            count++;
            n &= (n - 1);
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
```

## Python3

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
```

## C

```c
int hammingWeight(int n) {
    unsigned int x = (unsigned int)n;
    int count = 0;
    while (x) {
        x &= (x - 1);
        count++;
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int HammingWeight(int n)
    {
        uint x = (uint)n;
        int count = 0;
        while (x != 0)
        {
            count++;
            x &= x - 1;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    let count = 0;
    while (n !== 0) {
        count++;
        n &= n - 1;
    }
    return count;
};
```

## Typescript

```typescript
function hammingWeight(n: number): number {
    let count = 0;
    while (n !== 0) {
        count += n & 1;
        // Unsigned right shift to handle sign bit correctly
        n >>>= 1;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function hammingWeight($n) {
        $count = 0;
        while ($n != 0) {
            $count++;
            $n &= ($n - 1);
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func hammingWeight(_ n: Int) -> Int {
        return n.nonzeroBitCount
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun hammingWeight(n: Int): Int {
        var count = 0
        var num = n
        while (num != 0) {
            count += num and 1
            num = num ushr 1
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int hammingWeight(int n) {
    int count = 0;
    while (n != 0) {
      count++;
      n &= n - 1;
    }
    return count;
  }
}
```

## Golang

```go
func hammingWeight(n int) int {
	count := 0
	for n != 0 {
		n &= n - 1
		count++
	}
	return count
}
```

## Ruby

```ruby
def hamming_weight(n)
  count = 0
  while n != 0
    n &= n - 1
    count += 1
  end
  count
end
```

## Scala

```scala
object Solution {
    def hammingWeight(n: Int): Int = {
        var count = 0
        var num = n
        while (num != 0) {
            count += num & 1
            num = num >>> 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn hamming_weight(n: i32) -> i32 {
        (n as u32).count_ones() as i32
    }
}
```

## Racket

```racket
(define/contract (hamming-weight n)
  (-> exact-integer? exact-integer?)
  (let loop ((x n) (cnt 0))
    (if (= x 0)
        cnt
        (loop (arithmetic-shift x -1)
              (+ cnt (bitwise-and x 1))))))
```

## Erlang

```erlang
-spec hamming_weight(N :: integer()) -> integer().
hamming_weight(0) ->
    0;
hamming_weight(N) when N > 0 ->
    (N band 1) + hamming_weight(N bsr 1).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec hamming_weight(n :: integer) :: integer
  def hamming_weight(n) do
    count_bits(n, 0)
  end

  defp count_bits(0, acc), do: acc
  defp count_bits(n, acc) do
    count_bits(n >>> 1, acc + (n &&& 1))
  end
end
```
