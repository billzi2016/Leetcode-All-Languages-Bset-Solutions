# 1551. Minimum Operations to Make Array Equal

## Cpp

```cpp
class Solution {
public:
    int minOperations(int n) {
        if (n % 2 == 0) {
            int k = n / 2;
            return k * k;
        } else {
            int k = (n - 1) / 2;
            return k * (k + 1);
        }
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int n) {
        int half = n / 2;
        if (n % 2 == 0) {
            return half * half;
        } else {
            return half * (half + 1);
        }
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
        k = n // 2
        if n % 2 == 0:
            return k * k
        else:
            return k * (k + 1)
```

## Python3

```python
class Solution:
    def minOperations(self, n: int) -> int:
        k = n // 2
        if n % 2 == 0:
            return k * k
        else:
            return k * (k + 1)
```

## C

```c
int minOperations(int n) {
    if (n % 2 == 0) {
        int half = n / 2;
        return half * half;
    } else {
        int m = n / 2; // floor(n/2)
        return m * (m + 1);
    }
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int n) {
        int k = n / 2;
        return k * (n - k);
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
    const half = Math.floor(n / 2);
    return half * (n - half);
};
```

## Typescript

```typescript
function minOperations(n: number): number {
    const a = Math.floor(n / 2);
    const b = Math.ceil(n / 2);
    return a * b;
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
        $k = intdiv($n, 2);
        return $k * ($n - $k);
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ n: Int) -> Int {
        let k = n / 2
        if n % 2 == 0 {
            return k * k
        } else {
            return k * (k + 1)
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(n: Int): Int {
        var ops = 0
        for (i in n / 2 until n) {
            ops += (2 * i + 1 - n)
        }
        return ops
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(int n) {
    int start = (n + 1) ~/ 2;
    return start * (n - start);
  }
}
```

## Golang

```go
func minOperations(n int) int {
    k := n / 2
    if n%2 == 0 {
        return k * k
    }
    return k * (k + 1)
}
```

## Ruby

```ruby
def min_operations(n)
  half = n / 2
  n.even? ? half * half : half * (half + 1)
end
```

## Scala

```scala
object Solution {
    def minOperations(n: Int): Int = {
        val a = n / 2
        val b = (n + 1) / 2
        a * b
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(n: i32) -> i32 {
        let n64 = n as i64;
        if n % 2 == 0 {
            (n64 * n64 / 4) as i32
        } else {
            ((n64 * n64 - 1) / 4) as i32
        }
    }
}
```

## Racket

```racket
(define/contract (min-operations n)
  (-> exact-integer? exact-integer?)
  (if (even? n)
      (let ([m (quotient n 2)])
        (* m m))
      (let* ([m (quotient n 2)]
             [next (+ m 1)])
        (* m next))))
```

## Erlang

```erlang
-spec min_operations(N :: integer()) -> integer().
min_operations(N) ->
    Half = N div 2,
    case N rem 2 of
        0 -> Half * Half;
        _ -> Half * (Half + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(n :: integer) :: integer
  def min_operations(n) do
    div(n, 2) * div(n + 1, 2)
  end
end
```
