# 2169. Count Operations to Obtain Zero

## Cpp

```cpp
class Solution {
public:
    int countOperations(int num1, int num2) {
        long long ops = 0;
        while (num1 && num2) {
            if (num1 >= num2) {
                ops += num1 / num2;
                num1 %= num2;
            } else {
                ops += num2 / num1;
                num2 %= num1;
            }
        }
        return static_cast<int>(ops);
    }
};
```

## Java

```java
class Solution {
    public int countOperations(int num1, int num2) {
        long ops = 0;
        while (num1 != 0 && num2 != 0) {
            if (num1 >= num2) {
                ops += num1 / num2;
                num1 %= num2;
            } else {
                ops += num2 / num1;
                num2 %= num1;
            }
        }
        return (int) ops;
    }
}
```

## Python

```python
class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        cnt = 0
        while num1 and num2:
            if num1 >= num2:
                cnt += num1 // num2
                num1 %= num2
            else:
                cnt += num2 // num1
                num2 %= num1
        return cnt
```

## Python3

```python
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ops = 0
        while num1 and num2:
            if num1 >= num2:
                ops += num1 // num2
                num1 %= num2
            else:
                ops += num2 // num1
                num2 %= num1
        return ops
```

## C

```c
int countOperations(int num1, int num2) {
    long long cnt = 0;
    while (num1 && num2) {
        if (num1 >= num2) {
            cnt += num1 / num2;
            num1 %= num2;
        } else {
            cnt += num2 / num1;
            num2 %= num1;
        }
    }
    return (int)cnt;
}
```

## Csharp

```csharp
public class Solution {
    public int CountOperations(int num1, int num2) {
        long operations = 0;
        while (num1 > 0 && num2 > 0) {
            if (num1 >= num2) {
                operations += num1 / num2;
                num1 %= num2;
            } else {
                operations += num2 / num1;
                num2 %= num1;
            }
        }
        return (int)operations;
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
var countOperations = function(num1, num2) {
    let ops = 0;
    while (num1 > 0 && num2 > 0) {
        if (num1 >= num2) {
            ops += Math.floor(num1 / num2);
            num1 %= num2;
        } else {
            ops += Math.floor(num2 / num1);
            num2 %= num1;
        }
    }
    return ops;
};
```

## Typescript

```typescript
function countOperations(num1: number, num2: number): number {
    let operations = 0;
    while (num1 > 0 && num2 > 0) {
        if (num1 >= num2) {
            const q = Math.floor(num1 / num2);
            operations += q;
            num1 %= num2;
        } else {
            const q = Math.floor(num2 / num1);
            operations += q;
            num2 %= num1;
        }
    }
    return operations;
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
    function countOperations($num1, $num2) {
        $cnt = 0;
        while ($num1 != 0 && $num2 != 0) {
            if ($num1 >= $num2) {
                $cnt += intdiv($num1, $num2);
                $num1 %= $num2;
            } else {
                $cnt += intdiv($num2, $num1);
                $num2 %= $num1;
            }
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func countOperations(_ num1: Int, _ num2: Int) -> Int {
        var a = num1
        var b = num2
        var operations = 0
        
        while a != 0 && b != 0 {
            if a >= b {
                operations += a / b
                a %= b
            } else {
                operations += b / a
                b %= a
            }
        }
        
        return operations
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countOperations(num1: Int, num2: Int): Int {
        var a = num1
        var b = num2
        var ops = 0L
        while (a != 0 && b != 0) {
            if (a >= b) {
                ops += a / b
                a %= b
            } else {
                ops += b / a
                b %= a
            }
        }
        return ops.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int countOperations(int num1, int num2) {
    int a = num1, b = num2;
    int ops = 0;
    while (a != 0 && b != 0) {
      if (a >= b) {
        ops += a ~/ b;
        a %= b;
      } else {
        ops += b ~/ a;
        b %= a;
      }
    }
    return ops;
  }
}
```

## Golang

```go
func countOperations(num1 int, num2 int) int {
	ops := 0
	for num1 != 0 && num2 != 0 {
		if num1 >= num2 {
			ops += num1 / num2
			num1 %= num2
		} else {
			ops += num2 / num1
			num2 %= num1
		}
	}
	return ops
}
```

## Ruby

```ruby
def count_operations(num1, num2)
  ops = 0
  while num1 != 0 && num2 != 0
    if num1 >= num2
      ops += num1 / num2
      num1 %= num2
    else
      ops += num2 / num1
      num2 %= num1
    end
  end
  ops
end
```

## Scala

```scala
object Solution {
    def countOperations(num1: Int, num2: Int): Int = {
        var a = num1
        var b = num2
        var ops: Long = 0L
        while (a != 0 && b != 0) {
            if (a >= b) {
                ops += a / b
                a = a % b
            } else {
                ops += b / a
                b = b % a
            }
        }
        ops.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_operations(num1: i32, num2: i32) -> i32 {
        let mut a = num1 as i64;
        let mut b = num2 as i64;
        let mut ops: i64 = 0;
        while a != 0 && b != 0 {
            if a >= b {
                ops += a / b;
                a %= b;
            } else {
                ops += b / a;
                b %= a;
            }
        }
        ops as i32
    }
}
```

## Racket

```racket
(define/contract (count-operations num1 num2)
  (-> exact-integer? exact-integer? exact-integer?)
  (let loop ((a num1) (b num2) (cnt 0))
    (cond
      [(or (= a 0) (= b 0)) cnt]
      [(>= a b)
       (let* ([q (quotient a b)]
              [r (remainder a b)])
         (loop r b (+ cnt q)))]
      [else
       (let* ([q (quotient b a)]
              [r (remainder b a)])
         (loop a r (+ cnt q)))])))
```

## Erlang

```erlang
-spec count_operations(Num1 :: integer(), Num2 :: integer()) -> integer().
count_operations(Num1, Num2) ->
    count_ops(Num1, Num2).

count_ops(0, _) -> 0;
count_ops(_, 0) -> 0;
count_ops(A, B) when A >= B ->
    Quot = A div B,
    Rem = A rem B,
    Quot + count_ops(Rem, B);
count_ops(A, B) ->
    Quot = B div A,
    Rem = B rem A,
    Quot + count_ops(A, Rem).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_operations(num1 :: integer, num2 :: integer) :: integer
  def count_operations(num1, num2) do
    helper(num1, num2, 0)
  end

  defp helper(0, _, acc), do: acc
  defp helper(_, 0, acc), do: acc
  defp helper(a, b, acc) when a >= b do
    q = div(a, b)
    r = rem(a, b)
    helper(r, b, acc + q)
  end
  defp helper(a, b, acc) do
    q = div(b, a)
    r = rem(b, a)
    helper(a, r, acc + q)
  end
end
```
