# 0728. Self Dividing Numbers

## Cpp

```cpp
class Solution {
public:
    bool isSelfDividing(int n) {
        int x = n;
        while (x > 0) {
            int d = x % 10;
            if (d == 0 || n % d != 0) return false;
            x /= 10;
        }
        return true;
    }
    
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> res;
        for (int i = left; i <= right; ++i) {
            if (isSelfDividing(i)) res.push_back(i);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> result = new ArrayList<>();
        for (int num = left; num <= right; num++) {
            if (isSelfDividing(num)) {
                result.add(num);
            }
        }
        return result;
    }

    private boolean isSelfDividing(int n) {
        int temp = n;
        while (temp > 0) {
            int digit = temp % 10;
            if (digit == 0 || n % digit != 0) {
                return false;
            }
            temp /= 10;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_self(num):
            n = num
            while n:
                d = n % 10
                if d == 0 or num % d != 0:
                    return False
                n //= 10
            return True

        res = []
        for x in range(left, right + 1):
            if is_self(x):
                res.append(x)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self(num: int) -> bool:
            n = num
            while n > 0:
                d = n % 10
                if d == 0 or num % d != 0:
                    return False
                n //= 10
            return True

        result = []
        for num in range(left, right + 1):
            if is_self(num):
                result.append(num)
        return result
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* selfDividingNumbers(int left, int right, int* returnSize) {
    int capacity = right - left + 1;
    int *result = (int *)malloc(sizeof(int) * capacity);
    int count = 0;

    for (int num = left; num <= right; ++num) {
        int temp = num;
        bool ok = true;
        while (temp > 0) {
            int digit = temp % 10;
            if (digit == 0 || num % digit != 0) {
                ok = false;
                break;
            }
            temp /= 10;
        }
        if (ok) {
            result[count++] = num;
        }
    }

    *returnSize = count;
    result = (int *)realloc(result, sizeof(int) * count);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<int> SelfDividingNumbers(int left, int right)
    {
        var result = new List<int>();
        for (int i = left; i <= right; i++)
        {
            if (IsSelfDividing(i))
                result.Add(i);
        }
        return result;
    }

    private bool IsSelfDividing(int num)
    {
        int n = num;
        while (n > 0)
        {
            int digit = n % 10;
            if (digit == 0 || num % digit != 0)
                return false;
            n /= 10;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    const res = [];
    for (let n = left; n <= right; ++n) {
        if (isSelfDividing(n)) res.push(n);
    }
    return res;
};

function isSelfDividing(num) {
    let x = num;
    while (x > 0) {
        const digit = x % 10;
        if (digit === 0 || num % digit !== 0) return false;
        x = Math.floor(x / 10);
    }
    return true;
}
```

## Typescript

```typescript
function selfDividingNumbers(left: number, right: number): number[] {
    const result: number[] = [];
    
    const isSelfDividing = (n: number): boolean => {
        let temp = n;
        while (temp > 0) {
            const digit = temp % 10;
            if (digit === 0 || n % digit !== 0) return false;
            temp = Math.floor(temp / 10);
        }
        return true;
    };
    
    for (let i = left; i <= right; i++) {
        if (isSelfDividing(i)) result.push(i);
    }
    
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $left
     * @param Integer $right
     * @return Integer[]
     */
    function selfDividingNumbers($left, $right) {
        $result = [];
        for ($num = $left; $num <= $right; $num++) {
            if ($this->isSelfDividing($num)) {
                $result[] = $num;
            }
        }
        return $result;
    }

    private function isSelfDividing(int $n): bool {
        $temp = $n;
        while ($temp > 0) {
            $digit = $temp % 10;
            if ($digit == 0 || $n % $digit != 0) {
                return false;
            }
            $temp = intdiv($temp, 10);
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func selfDividingNumbers(_ left: Int, _ right: Int) -> [Int] {
        var res = [Int]()
        for num in left...right {
            if isSelfDividing(num) {
                res.append(num)
            }
        }
        return res
    }
    
    private func isSelfDividing(_ n: Int) -> Bool {
        var x = n
        while x > 0 {
            let digit = x % 10
            if digit == 0 || n % digit != 0 {
                return false
            }
            x /= 10
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun selfDividingNumbers(left: Int, right: Int): List<Int> {
        val result = ArrayList<Int>()
        for (num in left..right) {
            if (isSelfDividing(num)) {
                result.add(num)
            }
        }
        return result
    }

    private fun isSelfDividing(n: Int): Boolean {
        var x = n
        while (x > 0) {
            val d = x % 10
            if (d == 0 || n % d != 0) return false
            x /= 10
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  List<int> selfDividingNumbers(int left, int right) {
    bool isSelfDividing(int n) {
      int temp = n;
      while (temp > 0) {
        int digit = temp % 10;
        if (digit == 0 || n % digit != 0) return false;
        temp ~/= 10;
      }
      return true;
    }

    List<int> result = [];
    for (int i = left; i <= right; i++) {
      if (isSelfDividing(i)) result.add(i);
    }
    return result;
  }
}
```

## Golang

```go
func selfDividingNumbers(left int, right int) []int {
    res := []int{}
    for i := left; i <= right; i++ {
        if isSelfDividing(i) {
            res = append(res, i)
        }
    }
    return res
}

func isSelfDividing(num int) bool {
    n := num
    for n > 0 {
        d := n % 10
        if d == 0 || num%d != 0 {
            return false
        }
        n /= 10
    }
    return true
}
```

## Ruby

```ruby
def self_dividing_numbers(left, right)
  result = []
  (left..right).each do |num|
    n = num
    valid = true
    while n > 0
      digit = n % 10
      if digit == 0 || (num % digit != 0)
        valid = false
        break
      end
      n /= 10
    end
    result << num if valid
  end
  result
end
```

## Scala

```scala
import scala.collection.mutable.ListBuffer

object Solution {
  def selfDividingNumbers(left: Int, right: Int): List[Int] = {
    val result = ListBuffer[Int]()
    for (num <- left to right) {
      var n = num
      var ok = true
      while (n > 0 && ok) {
        val d = n % 10
        if (d == 0 || num % d != 0) ok = false
        n /= 10
      }
      if (ok) result += num
    }
    result.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn self_dividing_numbers(left: i32, right: i32) -> Vec<i32> {
        fn is_self(num: i32) -> bool {
            let mut x = num;
            while x > 0 {
                let d = x % 10;
                if d == 0 || num % d != 0 {
                    return false;
                }
                x /= 10;
            }
            true
        }

        let mut result = Vec::new();
        for n in left..=right {
            if is_self(n) {
                result.push(n);
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (self-dividing-numbers left right)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  (define (self-div? n)
    (let loop ((x n))
      (if (= x 0)
          #t
          (let ([d (remainder x 10)])
            (and (not (= d 0))
                 (= (modulo n d) 0)
                 (loop (quotient x 10)))))))
  (for/list ([i (in-range left (+ right 1))]
             #:when (self-div? i))
    i))
```

## Erlang

```erlang
-module(solution).
-export([self_dividing_numbers/2]).

-spec self_dividing_numbers(Left :: integer(), Right :: integer()) -> [integer()].
self_dividing_numbers(Left, Right) ->
    lists:filter(fun is_self/1, lists:seq(Left, Right)).

is_self(N) ->
    check(N, N).

check(0, _) -> true;
check(Num, Orig) ->
    D = Num rem 10,
    case D of
        0 -> false;
        _ when Orig rem D =/= 0 -> false;
        _ -> check(Num div 10, Orig)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec self_dividing_numbers(left :: integer, right :: integer) :: [integer]
  def self_dividing_numbers(left, right) do
    left..right |> Enum.filter(&self_dividing?/1)
  end

  defp self_dividing?(n), do: check(n, n)

  defp check(0, _original), do: true

  defp check(num, original) do
    digit = rem(num, 10)

    if digit == 0 or rem(original, digit) != 0 do
      false
    else
      check(div(num, 10), original)
    end
  end
end
```
