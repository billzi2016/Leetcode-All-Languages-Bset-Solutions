# 1780. Check if Number is a Sum of Powers of Three

## Cpp

```cpp
class Solution {
public:
    bool checkPowersOfThree(int n) {
        while (n > 0) {
            if (n % 3 == 2) return false;
            n /= 3;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean checkPowersOfThree(int n) {
        while (n > 0) {
            if (n % 3 == 2) {
                return false;
            }
            n /= 3;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n:
            if n % 3 == 2:
                return False
            n //= 3
        return True
```

## Python3

```python
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 2:
                return False
            n //= 3
        return True
```

## C

```c
#include <stdbool.h>

bool checkPowersOfThree(int n) {
    while (n > 0) {
        if (n % 3 == 2) return false;
        n /= 3;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CheckPowersOfThree(int n)
    {
        while (n > 0)
        {
            if (n % 3 == 2) return false;
            n /= 3;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var checkPowersOfThree = function(n) {
    while (n > 0) {
        if (n % 3 === 2) return false;
        n = Math.floor(n / 3);
    }
    return true;
};
```

## Typescript

```typescript
function checkPowersOfThree(n: number): boolean {
    while (n > 0) {
        if (n % 3 === 2) return false;
        n = Math.floor(n / 3);
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function checkPowersOfThree($n) {
        while ($n > 0) {
            if ($n % 3 == 2) {
                return false;
            }
            $n = intdiv($n, 3);
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func checkPowersOfThree(_ n: Int) -> Bool {
        var num = n
        while num > 0 {
            if num % 3 == 2 {
                return false
            }
            num /= 3
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkPowersOfThree(n: Int): Boolean {
        var num = n
        while (num > 0) {
            if (num % 3 == 2) return false
            num /= 3
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool checkPowersOfThree(int n) {
    while (n > 0) {
      if (n % 3 == 2) return false;
      n ~/= 3;
    }
    return true;
  }
}
```

## Golang

```go
func checkPowersOfThree(n int) bool {
	for n > 0 {
		if n%3 == 2 {
			return false
		}
		n /= 3
	}
	return true
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Boolean}
def check_powers_of_three(n)
  while n > 0
    return false if n % 3 == 2
    n /= 3
  end
  true
end
```

## Scala

```scala
object Solution {
    def checkPowersOfThree(n: Int): Boolean = {
        var x = n
        while (x > 0) {
            if (x % 3 == 2) return false
            x /= 3
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_powers_of_three(n: i32) -> bool {
        let mut x = n;
        while x > 0 {
            if x % 3 == 2 {
                return false;
            }
            x /= 3;
        }
        true
    }
}
```

## Racket

```racket
(define/contract (check-powers-of-three n)
  (-> exact-integer? boolean?)
  (let loop ((x n))
    (cond [(zero? x) #t]
          [(= (remainder x 3) 2) #f]
          [else (loop (quotient x 3))])))
```

## Erlang

```erlang
-module(solution).
-export([check_powers_of_three/1]).

-spec check_powers_of_three(N :: integer()) -> boolean().
check_powers_of_three(0) ->
    true;
check_powers_of_three(N) when N > 0 ->
    case N rem 3 of
        2 -> false;
        _ -> check_powers_of_three(N div 3)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_powers_of_three(n :: integer) :: boolean
  def check_powers_of_three(0), do: true
  def check_powers_of_three(n) when n > 0, do: check(n)

  defp check(0), do: true

  defp check(num) do
    case rem(num, 3) do
      2 -> false
      _ -> check(div(num, 3))
    end
  end
end
```
