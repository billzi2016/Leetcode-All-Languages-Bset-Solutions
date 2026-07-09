# 2579. Count Total Number of Colored Cells

## Cpp

```cpp
class Solution {
public:
    long long coloredCells(int n) {
        long long nn = n;
        return 1 + 2 * nn * (nn - 1);
    }
};
```

## Java

```java
class Solution {
    public long coloredCells(int n) {
        long nl = n;
        return 1L + 2L * nl * (nl - 1);
    }
}
```

## Python

```python
class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 1 + 2 * n * (n - 1)
```

## Python3

```python
class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * n * (n - 1)
```

## C

```c
long long coloredCells(int n) {
    long long nn = n;
    return 1 + 2LL * nn * (nn - 1);
}
```

## Csharp

```csharp
public class Solution
{
    public long ColoredCells(int n)
    {
        long nn = n;
        return 1 + 2 * nn * (nn - 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var coloredCells = function(n) {
    return 1 + 2 * n * (n - 1);
};
```

## Typescript

```typescript
function coloredCells(n: number): number {
    return 1 + 2 * n * (n - 1);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function coloredCells($n) {
        return 1 + 2 * $n * ($n - 1);
    }
}
```

## Swift

```swift
class Solution {
    func coloredCells(_ n: Int) -> Int {
        return 1 + 2 * n * (n - 1)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun coloredCells(n: Int): Long {
        val nn = n.toLong()
        return 1L + 2L * nn * (nn - 1)
    }
}
```

## Dart

```dart
class Solution {
  int coloredCells(int n) {
    return 1 + 2 * n * (n - 1);
  }
}
```

## Golang

```go
func coloredCells(n int) int64 {
	nn := int64(n)
	return 1 + 2*nn*(nn-1)
}
```

## Ruby

```ruby
def colored_cells(n)
  1 + 2 * n * (n - 1)
end
```

## Scala

```scala
object Solution {
    def coloredCells(n: Int): Long = {
        val nn = n.toLong
        1L + 2L * nn * (nn - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn colored_cells(n: i32) -> i64 {
        let n = n as i64;
        1 + 2 * n * (n - 1)
    }
}
```

## Racket

```racket
(define/contract (colored-cells n)
  (-> exact-integer? exact-integer?)
  (+ 1 (* 2 n (- n 1))))
```

## Erlang

```erlang
-spec colored_cells(N :: integer()) -> integer().
colored_cells(N) when N >= 1 ->
    1 + 2 * N * (N - 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec colored_cells(n :: integer) :: integer
  def colored_cells(n) do
    1 + 2 * n * (n - 1)
  end
end
```
