# 1486. XOR Operation in an Array

## Cpp

```cpp
class Solution {
public:
    int xorOperation(int n, int start) {
        int result = 0;
        for (int i = 0; i < n; ++i) {
            result ^= (start + 2 * i);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int xorOperation(int n, int start) {
        int result = 0;
        for (int i = 0; i < n; i++) {
            result ^= start + (i << 1);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        result = 0
        for i in range(n):
            result ^= start + (i << 1)
        return result
```

## Python3

```python
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + (i << 1)
        return res
```

## C

```c
int xorOperation(int n, int start) {
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        ans ^= (start + (i << 1));
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int XorOperation(int n, int start)
    {
        int xor = 0;
        for (int i = 0; i < n; i++)
        {
            xor ^= start + 2 * i;
        }
        return xor;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} start
 * @return {number}
 */
var xorOperation = function(n, start) {
    let result = 0;
    for (let i = 0; i < n; i++) {
        result ^= (start + 2 * i);
    }
    return result;
};
```

## Typescript

```typescript
function xorOperation(n: number, start: number): number {
    let result = 0;
    for (let i = 0; i < n; i++) {
        result ^= start + 2 * i;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $start
     * @return Integer
     */
    function xorOperation($n, $start) {
        $result = 0;
        for ($i = 0; $i < $n; $i++) {
            $result ^= $start + 2 * $i;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func xorOperation(_ n: Int, _ start: Int) -> Int {
        var result = 0
        for i in 0..<n {
            result ^= (start + 2 * i)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun xorOperation(n: Int, start: Int): Int {
        var ans = 0
        for (i in 0 until n) {
            ans = ans xor (start + i * 2)
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int xorOperation(int n, int start) {
    int result = 0;
    for (int i = 0; i < n; i++) {
      result ^= (start + 2 * i);
    }
    return result;
  }
}
```

## Golang

```go
func xorOperation(n int, start int) int {
    result := 0
    for i := 0; i < n; i++ {
        result ^= start + 2*i
    }
    return result
}
```

## Ruby

```ruby
def xor_operation(n, start)
  result = 0
  i = 0
  while i < n
    result ^= (start + (i << 1))
    i += 1
  end
  result
end
```

## Scala

```scala
object Solution {
    def xorOperation(n: Int, start: Int): Int = {
        var res = 0
        var i = 0
        while (i < n) {
            res ^= (start + 2 * i)
            i += 1
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn xor_operation(n: i32, start: i32) -> i32 {
        let mut ans = 0;
        for i in 0..n {
            ans ^= start + 2 * i;
        }
        ans
    }
}
```

## Racket

```racket
#lang racket
(require racket/bitwise)

(define/contract (xor-operation n start)
  (-> exact-integer? exact-integer? exact-integer?)
  (let loop ((i 0) (acc 0))
    (if (= i n)
        acc
        (loop (add1 i) (bitwise-xor acc (+ start (* 2 i)))))))
```

## Erlang

```erlang
-spec xor_operation(N :: integer(), Start :: integer()) -> integer().
xor_operation(N, Start) ->
    xor_seq(N, Start, 0).

xor_seq(0, _Start, Acc) -> 
    Acc;
xor_seq(N, Start, Acc) ->
    Value = Start + 2 * (N - 1),
    xor_seq(N - 1, Start, Acc bxor Value).
```

## Elixir

```elixir
defmodule Solution do
  @spec xor_operation(n :: integer, start :: integer) :: integer
  def xor_operation(n, start) do
    require Bitwise

    Enum.reduce(0..(n - 1), 0, fn i, acc ->
      Bitwise.bxor(acc, start + 2 * i)
    end)
  end
end
```
