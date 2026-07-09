# 1317. Convert Integer to the Sum of Two No-Zero Integers

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isNoZero(int x) {
        while (x > 0) {
            if (x % 10 == 0) return false;
            x /= 10;
        }
        return true;
    }
    
    vector<int> getNoZeroIntegers(int n) {
        for (int a = 1; a < n; ++a) {
            int b = n - a;
            if (isNoZero(a) && isNoZero(b)) {
                return {a, b};
            }
        }
        return {}; // guaranteed never reached
    }
};
```

## Java

```java
class Solution {
    public int[] getNoZeroIntegers(int n) {
        for (int a = 1; a < n; a++) {
            int b = n - a;
            if (!hasZero(a) && !hasZero(b)) {
                return new int[]{a, b};
            }
        }
        // According to problem constraints, this line should never be reached.
        return new int[0];
    }

    private boolean hasZero(int x) {
        while (x > 0) {
            if (x % 10 == 0) {
                return true;
            }
            x /= 10;
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def is_no_zero(x):
            while x:
                if x % 10 == 0:
                    return False
                x //= 10
            return True

        for a in range(1, n):
            b = n - a
            if is_no_zero(a) and is_no_zero(b):
                return [a, b]
```

## Python3

```python
from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def is_no_zero(x: int) -> bool:
            while x:
                if x % 10 == 0:
                    return False
                x //= 10
            return True

        for a in range(1, n):
            b = n - a
            if is_no_zero(a) and is_no_zero(b):
                return [a, b]
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getNoZeroIntegers(int n, int* returnSize) {
    // Helper lambda-like function to check for zero digits
    int isNoZero(int x) {
        while (x > 0) {
            if (x % 10 == 0) return 0;
            x /= 10;
        }
        return 1;
    }

    int *res = (int *)malloc(2 * sizeof(int));
    for (int a = 1; a < n; ++a) {
        int b = n - a;
        if (isNoZero(a) && isNoZero(b)) {
            res[0] = a;
            res[1] = b;
            break;
        }
    }
    *returnSize = 2;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] GetNoZeroIntegers(int n)
    {
        for (int a = 1; a < n; a++)
        {
            int b = n - a;
            if (IsNoZero(a) && IsNoZero(b))
                return new int[] { a, b };
        }
        // According to problem constraints, this line will never be reached.
        return new int[0];
    }

    private bool IsNoZero(int x)
    {
        while (x > 0)
        {
            if (x % 10 == 0) return false;
            x /= 10;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number[]}
 */
var getNoZeroIntegers = function(n) {
    const isNoZero = (num) => {
        while (num > 0) {
            if (num % 10 === 0) return false;
            num = Math.floor(num / 10);
        }
        return true;
    };
    
    for (let a = 1; a < n; ++a) {
        const b = n - a;
        if (isNoZero(a) && isNoZero(b)) {
            return [a, b];
        }
    }
    // According to problem constraints, this line should never be reached.
    return [];
};
```

## Typescript

```typescript
function getNoZeroIntegers(n: number): number[] {
    const isNoZero = (x: number): boolean => {
        while (x > 0) {
            if (x % 10 === 0) return false;
            x = Math.floor(x / 10);
        }
        return true;
    };
    for (let a = 1; a < n; ++a) {
        const b = n - a;
        if (isNoZero(a) && isNoZero(b)) {
            return [a, b];
        }
    }
    // According to problem constraints, this line should never be reached.
    return [];
}
```

## Php

```php
class Solution {

    /**
     * @param int $n
     * @return int[]
     */
    function getNoZeroIntegers($n) {
        for ($a = 1; $a < $n; $a++) {
            $b = $n - $a;
            if ($this->isNoZero($a) && $this->isNoZero($b)) {
                return [$a, $b];
            }
        }
        return [];
    }

    private function isNoZero(int $num): bool {
        while ($num > 0) {
            if ($num % 10 == 0) {
                return false;
            }
            $num = intdiv($num, 10);
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func getNoZeroIntegers(_ n: Int) -> [Int] {
        func isNoZero(_ x: Int) -> Bool {
            var num = x
            while num > 0 {
                if num % 10 == 0 { return false }
                num /= 10
            }
            return true
        }
        
        for a in 1..<n {
            let b = n - a
            if isNoZero(a) && isNoZero(b) {
                return [a, b]
            }
        }
        return []
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getNoZeroIntegers(n: Int): IntArray {
        fun isNoZero(x: Int): Boolean {
            var v = x
            while (v > 0) {
                if (v % 10 == 0) return false
                v /= 10
            }
            return true
        }
        for (a in 1 until n) {
            val b = n - a
            if (isNoZero(a) && isNoZero(b)) {
                return intArrayOf(a, b)
            }
        }
        return intArrayOf()
    }
}
```

## Dart

```dart
class Solution {
  List<int> getNoZeroIntegers(int n) {
    bool isNoZero(int x) {
      while (x > 0) {
        if (x % 10 == 0) return false;
        x ~/= 10;
      }
      return true;
    }

    for (int a = 1; a < n; ++a) {
      int b = n - a;
      if (isNoZero(a) && isNoZero(b)) {
        return [a, b];
      }
    }
    // According to problem constraints, this line will never be reached.
    return [];
  }
}
```

## Golang

```go
func getNoZeroIntegers(n int) []int {
	isNoZero := func(x int) bool {
		for x > 0 {
			if x%10 == 0 {
				return false
			}
			x /= 10
		}
		return true
	}
	for a := 1; a < n; a++ {
		b := n - a
		if isNoZero(a) && isNoZero(b) {
			return []int{a, b}
		}
	}
	return nil
}
```

## Ruby

```ruby
def get_no_zero_integers(n)
  no_zero = ->(x) { !x.to_s.include?('0') }
  (1...n).each do |a|
    b = n - a
    return [a, b] if no_zero.call(a) && no_zero.call(b)
  end
end
```

## Scala

```scala
object Solution {
    def getNoZeroIntegers(n: Int): Array[Int] = {
        def isNoZero(x: Int): Boolean = {
            var num = x
            while (num > 0) {
                if (num % 10 == 0) return false
                num /= 10
            }
            true
        }

        for (a <- 1 until n) {
            val b = n - a
            if (isNoZero(a) && isNoZero(b)) {
                return Array(a, b)
            }
        }
        // According to problem constraints, this line should never be reached.
        Array()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_no_zero_integers(n: i32) -> Vec<i32> {
        for a in 1..n {
            let b = n - a;
            if Self::no_zero(a) && Self::no_zero(b) {
                return vec![a, b];
            }
        }
        Vec::new()
    }

    fn no_zero(mut x: i32) -> bool {
        while x > 0 {
            if x % 10 == 0 {
                return false;
            }
            x /= 10;
        }
        true
    }
}
```

## Racket

```racket
(define/contract (get-no-zero-integers n)
  (-> exact-integer? (listof exact-integer?))
  (define (no-zero? x)
    (let loop ((y x))
      (cond [(zero? y) #t]
            [(= (remainder y 10) 0) #f]
            [else (loop (quotient y 10))])))
  (define (search i)
    (cond [(> i n) (error "no solution")]
          [(and (no-zero? i) (no-zero? (- n i))) (list i (- n i))]
          [else (search (+ i 1))]))
  (search 1))
```

## Erlang

```erlang
-spec get_no_zero_integers(N :: integer()) -> [integer()].
get_no_zero_integers(N) ->
    find(N, 1).

find(N, I) when I < N ->
    A = I,
    B = N - I,
    case {is_no_zero(A), is_no_zero(B)} of
        {true, true} -> [A, B];
        _ -> find(N, I + 1)
    end;
find(_, _) ->
    [].

is_no_zero(X) ->
    not lists:member($0, integer_to_list(X)).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_no_zero_integers(n :: integer) :: [integer]
  def get_no_zero_integers(n) do
    Enum.find_value(1..(n - 1), fn a ->
      b = n - a

      if no_zero?(a) and no_zero?(b) do
        [a, b]
      else
        nil
      end
    end)
  end

  defp no_zero?(x) do
    not Integer.digits(x) |> Enum.any?(&(&1 == 0))
  end
end
```
