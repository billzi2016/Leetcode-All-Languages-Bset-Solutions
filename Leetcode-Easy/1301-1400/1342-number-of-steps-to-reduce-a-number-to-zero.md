# 1342. Number of Steps to Reduce a Number to Zero

## Cpp

```cpp
class Solution {
public:
    int numberOfSteps(int num) {
        int steps = 0;
        while (num > 0) {
            if ((num & 1) == 0)
                num >>= 1;
            else
                --num;
            ++steps;
        }
        return steps;
    }
};
```

## Java

```java
class Solution {
    public int numberOfSteps(int num) {
        int steps = 0;
        while (num > 0) {
            if ((num & 1) == 0) {
                num >>= 1;
            } else {
                num--;
            }
            steps++;
        }
        return steps;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            steps += 1
        return steps
```

## Python3

```python
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            steps += 1
        return steps
```

## C

```c
int numberOfSteps(int num) {
    int steps = 0;
    while (num > 0) {
        if ((num & 1) == 0)
            num >>= 1;
        else
            num--;
        steps++;
    }
    return steps;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfSteps(int num) {
        int steps = 0;
        while (num > 0) {
            if ((num & 1) == 0) {
                num >>= 1;
            } else {
                num--;
            }
            steps++;
        }
        return steps;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    let steps = 0;
    while (num > 0) {
        if ((num & 1) === 0) {
            num >>= 1; // divide by 2 when even
        } else {
            num -= 1;   // subtract 1 when odd
        }
        steps++;
    }
    return steps;
};
```

## Typescript

```typescript
function numberOfSteps(num: number): number {
    let steps = 0;
    while (num > 0) {
        if ((num & 1) === 0) {
            num >>= 1;
        } else {
            num--;
        }
        steps++;
    }
    return steps;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function numberOfSteps($num) {
        $steps = 0;
        while ($num > 0) {
            if (($num & 1) == 0) {
                $num >>= 1;
            } else {
                $num--;
            }
            $steps++;
        }
        return $steps;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfSteps(_ num: Int) -> Int {
        var steps = 0
        var n = num
        while n > 0 {
            if n & 1 == 0 {
                n >>= 1
            } else {
                n -= 1
            }
            steps += 1
        }
        return steps
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfSteps(num: Int): Int {
        var n = num
        var steps = 0
        while (n > 0) {
            if ((n and 1) == 0) {
                n = n shr 1
            } else {
                n--
            }
            steps++
        }
        return steps
    }
}
```

## Dart

```dart
class Solution {
  int numberOfSteps(int num) {
    int steps = 0;
    while (num > 0) {
      if ((num & 1) == 0) {
        num >>= 1;
      } else {
        num -= 1;
      }
      steps++;
    }
    return steps;
  }
}
```

## Golang

```go
func numberOfSteps(num int) int {
	steps := 0
	for num > 0 {
		if num%2 == 0 {
			num /= 2
		} else {
			num--
		}
		steps++
	}
	return steps
}
```

## Ruby

```ruby
def number_of_steps(num)
  steps = 0
  while num > 0
    if (num & 1) == 0
      num >>= 1
    else
      num -= 1
    end
    steps += 1
  end
  steps
end
```

## Scala

```scala
object Solution {
    def numberOfSteps(num: Int): Int = {
        var n = num
        var steps = 0
        while (n > 0) {
            if ((n & 1) == 0) n >>= 1 else n -= 1
            steps += 1
        }
        steps
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_steps(num: i32) -> i32 {
        let mut n = num;
        let mut steps = 0;
        while n > 0 {
            if n & 1 == 0 {
                n >>= 1;
            } else {
                n -= 1;
            }
            steps += 1;
        }
        steps
    }
}
```

## Racket

```racket
(define/contract (number-of-steps num)
  (-> exact-integer? exact-integer?)
  (let loop ((n num) (cnt 0))
    (if (= n 0)
        cnt
        (loop (if (even? n) (/ n 2) (- n 1)) (+ cnt 1)))))
```

## Erlang

```erlang
-spec number_of_steps(Num :: integer()) -> integer().
number_of_steps(Num) ->
    number_of_steps(Num, 0).

number_of_steps(0, Acc) -> Acc;
number_of_steps(N, Acc) when N rem 2 =:= 0 ->
    number_of_steps(N div 2, Acc + 1);
number_of_steps(N, Acc) ->
    number_of_steps(N - 1, Acc + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_steps(num :: integer) :: integer
  def number_of_steps(num) do
    steps(num, 0)
  end

  defp steps(0, acc), do: acc
  defp steps(n, acc) when rem(n, 2) == 0 do
    steps(div(n, 2), acc + 1)
  end
  defp steps(n, acc) do
    steps(n - 1, acc + 1)
  end
end
```
