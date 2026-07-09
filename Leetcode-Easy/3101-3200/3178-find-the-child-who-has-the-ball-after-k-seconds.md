# 3178. Find the Child Who Has the Ball After K Seconds

## Cpp

```cpp
class Solution {
public:
    int numberOfChild(int n, int k) {
        int period = 2 * (n - 1);
        int m = k % period;
        if (m <= n - 1) return m;
        return period - m;
    }
};
```

## Java

```java
class Solution {
    public int numberOfChild(int n, int k) {
        int period = 2 * (n - 1);
        int m = k % period;
        if (m <= n - 1) {
            return m;
        } else {
            return period - m;
        }
    }
}
```

## Python

```python
class Solution(object):
    def numberOfChild(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        period = 2 * (n - 1)
        k %= period
        if k <= n - 1:
            return k
        else:
            return period - k
```

## Python3

```python
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        period = 2 * (n - 1)
        k %= period
        if k <= n - 1:
            return k
        else:
            return period - k
```

## C

```c
int numberOfChild(int n, int k) {
    int period = 2 * (n - 1);
    int t = k % period;
    if (t <= n - 1) return t;
    return period - t;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfChild(int n, int k) {
        int period = 2 * (n - 1);
        int m = k % period;
        if (m <= n - 1) return m;
        return period - m;
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
var numberOfChild = function(n, k) {
    const cycle = 2 * (n - 1);
    const t = k % cycle;
    if (t <= n - 1) return t;
    return cycle - t;
};
```

## Typescript

```typescript
function numberOfChild(n: number, k: number): number {
    const cycle = 2 * (n - 1);
    const r = k % cycle;
    return r <= n - 1 ? r : cycle - r;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function numberOfChild($n, $k) {
        $period = 2 * ($n - 1);
        $m = $k % $period;
        if ($m <= $n - 1) {
            return $m;
        } else {
            return $period - $m;
        }
    }
}
```

## Swift

```swift
class Solution {
    func numberOfChild(_ n: Int, _ k: Int) -> Int {
        let period = 2 * (n - 1)
        let t = k % period
        if t <= n - 1 {
            return t
        } else {
            return period - t
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfChild(n: Int, k: Int): Int {
        val period = 2 * (n - 1)
        val t = k % period
        return if (t <= n - 1) t else period - t
    }
}
```

## Dart

```dart
class Solution {
  int numberOfChild(int n, int k) {
    int period = 2 * (n - 1);
    int m = k % period;
    if (m <= n - 1) return m;
    return period - m;
  }
}
```

## Golang

```go
func numberOfChild(n int, k int) int {
	period := 2 * (n - 1)
	m := k % period
	if m <= n-1 {
		return m
	}
	return period - m
}
```

## Ruby

```ruby
def number_of_child(n, k)
  period = 2 * (n - 1)
  t = k % period
  if t <= n - 1
    t
  else
    period - t
  end
end
```

## Scala

```scala
object Solution {
    def numberOfChild(n: Int, k: Int): Int = {
        val period = 2 * (n - 1)
        val t = k % period
        if (t <= n - 1) t else period - t
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_child(n: i32, k: i32) -> i32 {
        let period = 2 * (n - 1);
        let t = k % period;
        if t <= n - 1 { t } else { period - t }
    }
}
```

## Racket

```racket
(define/contract (number-of-child n k)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ([period (* 2 (- n 1))]
         [m (remainder k period)])
    (if (<= m (- n 1))
        m
        (- period m))))
```

## Erlang

```erlang
-spec number_of_child(N :: integer(), K :: integer()) -> integer().
number_of_child(N, K) ->
    Cycle = 2 * (N - 1),
    Steps = K rem Cycle,
    if
        Steps =< N - 1 -> Steps;
        true -> Cycle - Steps
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_child(n :: integer, k :: integer) :: integer
  def number_of_child(n, k) do
    period = 2 * (n - 1)
    r = rem(k, period)

    if r <= n - 1 do
      r
    else
      period - r
    end
  end
end
```
