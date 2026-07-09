# 2177. Find Three Consecutive Integers That Sum to a Given Number

## Cpp

```cpp
class Solution {
public:
    vector<long long> sumOfThree(long long num) {
        if (num % 3 != 0) return {};
        long long x = num / 3;
        return {x - 1, x, x + 1};
    }
};
```

## Java

```java
class Solution {
    public long[] sumOfThree(long num) {
        if (num % 3 != 0) {
            return new long[0];
        }
        long x = num / 3;
        return new long[]{x - 1, x, x + 1};
    }
}
```

## Python

```python
class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num % 3 != 0:
            return []
        x = num // 3
        return [x - 1, x, x + 1]
```

## Python3

```python
from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        x = num // 3
        return [x - 1, x, x + 1]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* sumOfThree(long long num, int* returnSize) {
    if (num % 3 != 0) {
        *returnSize = 0;
        return NULL;
    }
    long long x = num / 3;
    long long* res = (long long*)malloc(3 * sizeof(long long));
    if (!res) {
        *returnSize = 0;
        return NULL;
    }
    res[0] = x - 1;
    res[1] = x;
    res[2] = x + 1;
    *returnSize = 3;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public long[] SumOfThree(long num) {
        if (num % 3 != 0) {
            return new long[0];
        }
        long x = num / 3;
        return new long[] { x - 1, x, x + 1 };
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {number[]}
 */
var sumOfThree = function(num) {
    if (num % 3 !== 0) return [];
    const x = num / 3;
    return [x - 1, x, x + 1];
};
```

## Typescript

```typescript
function sumOfThree(num: number): number[] {
    if (num % 3 !== 0) return [];
    const x = num / 3;
    return [x - 1, x, x + 1];
}
```

## Php

```php
class Solution {

    /**
     * @param integer $num
     * @return integer[]
     */
    function sumOfThree($num) {
        if ($num % 3 !== 0) {
            return [];
        }
        $x = intdiv($num, 3);
        return [$x - 1, $x, $x + 1];
    }
}
```

## Swift

```swift
class Solution {
    func sumOfThree(_ num: Int) -> [Int] {
        if num % 3 != 0 { return [] }
        let x = num / 3
        return [x - 1, x, x + 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumOfThree(num: Long): LongArray {
        if (num % 3L != 0L) return longArrayOf()
        val x = num / 3L
        return longArrayOf(x - 1, x, x + 1)
    }
}
```

## Dart

```dart
class Solution {
  List<int> sumOfThree(int num) {
    if (num % 3 != 0) return [];
    int x = num ~/ 3;
    return [x - 1, x, x + 1];
  }
}
```

## Golang

```go
func sumOfThree(num int64) []int64 {
	if num%3 != 0 {
		return []int64{}
	}
	x := num / 3
	return []int64{x - 1, x, x + 1}
}
```

## Ruby

```ruby
def sum_of_three(num)
  return [] unless num % 3 == 0
  x = num / 3
  [x - 1, x, x + 1]
end
```

## Scala

```scala
object Solution {
    def sumOfThree(num: Long): Array[Long] = {
        if (num % 3 != 0) Array.empty[Long]
        else {
            val x = num / 3
            Array(x - 1, x, x + 1)
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_of_three(num: i64) -> Vec<i64> {
        if num % 3 != 0 {
            Vec::new()
        } else {
            let x = num / 3;
            vec![x - 1, x, x + 1]
        }
    }
}
```

## Racket

```racket
(define/contract (sum-of-three num)
  (-> exact-integer? (listof exact-integer?))
  (if (= (remainder num 3) 0)
      (let ((x (/ num 3)))
        (list (- x 1) x (+ x 1)))
      '()))
```

## Erlang

```erlang
-module(solution).
-export([sum_of_three/1]).

-spec sum_of_three(Num :: integer()) -> [integer()].
sum_of_three(Num) when is_integer(Num) ->
    case Num rem 3 of
        0 ->
            X = Num div 3,
            [X-1, X, X+1];
        _ ->
            []
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_of_three(num :: integer) :: [integer]
  def sum_of_three(num) do
    if rem(num, 3) == 0 do
      x = div(num, 3)
      [x - 1, x, x + 1]
    else
      []
    end
  end
end
```
