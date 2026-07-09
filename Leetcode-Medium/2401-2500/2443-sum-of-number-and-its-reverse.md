# 2443. Sum of Number and Its Reverse

## Cpp

```cpp
class Solution {
public:
    int rev(int x) {
        int r = 0;
        while (x > 0) {
            r = r * 10 + x % 10;
            x /= 10;
        }
        return r;
    }
    
    bool sumOfNumberAndReverse(int num) {
        for (int i = 0; i <= num; ++i) {
            if (i + rev(i) == num) return true;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean sumOfNumberAndReverse(int num) {
        for (int i = 0; i <= num; i++) {
            if (i + reverse(i) == num) {
                return true;
            }
        }
        return false;
    }

    private int reverse(int x) {
        int rev = 0;
        while (x > 0) {
            rev = rev * 10 + (x % 10);
            x /= 10;
        }
        return rev;
    }
}
```

## Python

```python
class Solution(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for x in range(num + 1):
            rev = int(str(x)[::-1])
            if x + rev == num:
                return True
        return False
```

## Python3

```python
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def rev(x: int) -> int:
            return int(str(x)[::-1])
        for x in range(num + 1):
            if x + rev(x) == num:
                return True
        return False
```

## C

```c
#include <stdbool.h>

static int reverseInt(int n) {
    int rev = 0;
    while (n > 0) {
        rev = rev * 10 + n % 10;
        n /= 10;
    }
    return rev;
}

bool sumOfNumberAndReverse(int num) {
    for (int x = 0; x <= num; ++x) {
        if (x + reverseInt(x) == num) {
            return true;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool SumOfNumberAndReverse(int num) {
        for (int i = 0; i <= num; i++) {
            int rev = Reverse(i);
            if (i + rev == num) return true;
        }
        return false;
    }

    private int Reverse(int x) {
        int rev = 0;
        while (x > 0) {
            rev = rev * 10 + (x % 10);
            x /= 10;
        }
        return rev;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {boolean}
 */
var sumOfNumberAndReverse = function(num) {
    const reverse = (n) => {
        return parseInt(n.toString().split('').reverse().join(''), 10);
    };
    for (let i = 0; i <= num; ++i) {
        if (i + reverse(i) === num) {
            return true;
        }
    }
    return false;
};
```

## Typescript

```typescript
function sumOfNumberAndReverse(num: number): boolean {
    for (let i = 0; i <= num; i++) {
        const rev = Number(String(i).split('').reverse().join(''));
        if (i + rev === num) return true;
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return Boolean
     */
    function sumOfNumberAndReverse($num) {
        for ($i = 0; $i <= $num; $i++) {
            $rev = intval(strrev((string)$i));
            if ($i + $rev == $num) {
                return true;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func sumOfNumberAndReverse(_ num: Int) -> Bool {
        for i in 0...num {
            if i + reverse(i) == num {
                return true
            }
        }
        return false
    }
    
    private func reverse(_ x: Int) -> Int {
        var n = x
        var rev = 0
        while n > 0 {
            rev = rev * 10 + n % 10
            n /= 10
        }
        return rev
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumOfNumberAndReverse(num: Int): Boolean {
        for (x in 0..num) {
            var n = x
            var rev = 0
            while (n > 0) {
                rev = rev * 10 + n % 10
                n /= 10
            }
            if (x + rev == num) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool sumOfNumberAndReverse(int num) {
    for (int i = 0; i <= num; i++) {
      if (i + _reverse(i) == num) return true;
    }
    return false;
  }

  int _reverse(int x) {
    int rev = 0;
    while (x > 0) {
      rev = rev * 10 + x % 10;
      x ~/= 10;
    }
    return rev;
  }
}
```

## Golang

```go
func sumOfNumberAndReverse(num int) bool {
	for i := 0; i <= num; i++ {
		if i+reverse(i) == num {
			return true
		}
	}
	return false
}

func reverse(x int) int {
	rev := 0
	for x > 0 {
		rev = rev*10 + x%10
		x /= 10
	}
	return rev
}
```

## Ruby

```ruby
def sum_of_number_and_reverse(num)
  (0..num).each do |x|
    rev = x.to_s.reverse.to_i
    return true if x + rev == num
  end
  false
end
```

## Scala

```scala
object Solution {
    def sumOfNumberAndReverse(num: Int): Boolean = {
        def reverse(n: Int): Int = {
            var rev = 0
            var x = n
            while (x > 0) {
                rev = rev * 10 + (x % 10)
                x /= 10
            }
            rev
        }

        for (x <- 0 to num) {
            if (x + reverse(x) == num) return true
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_of_number_and_reverse(num: i32) -> bool {
        let target = num;
        for x in 0..=target {
            let mut n = x;
            let mut rev = 0i32;
            while n > 0 {
                rev = rev * 10 + (n % 10);
                n /= 10;
            }
            if x + rev == target {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (sum-of-number-and-reverse num)
  (-> exact-integer? boolean?)
  (define (reverse-num n)
    (string->number
      (list->string (reverse (string->list (number->string n))))))
  (let loop ((i 0))
    (cond [(> i num) #f]
          [(= (+ i (reverse-num i)) num) #t]
          [else (loop (add1 i))])))
```

## Erlang

```erlang
-module(solution).
-export([sum_of_number_and_reverse/1]).

-spec sum_of_number_and_reverse(Num :: integer()) -> boolean().
sum_of_number_and_reverse(Num) ->
    check(Num, 0).

check(Num, X) when X =< Num ->
    case X + rev_int(X) of
        Num -> true;
        _   -> check(Num, X + 1)
    end;
check(_, _) ->
    false.

rev_int(N) -> rev(N, 0).

rev(0, Acc) -> Acc;
rev(N, Acc) ->
    rev(N div 10, Acc * 10 + N rem 10).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_of_number_and_reverse(num :: integer) :: boolean
  def sum_of_number_and_reverse(num) do
    0..num
    |> Enum.any?(fn x -> x + reverse_int(x) == num end)
  end

  defp reverse_int(n) do
    n
    |> Integer.to_string()
    |> String.reverse()
    |> String.to_integer()
  end
end
```
