# 2595. Number of Even and Odd Bits

## Cpp

```cpp
class Solution {
public:
    vector<int> evenOddBit(int n) {
        int even = 0, odd = 0;
        int idx = 0;
        while (n > 0) {
            if (n & 1) {
                if ((idx & 1) == 0) ++even;
                else ++odd;
            }
            n >>= 1;
            ++idx;
        }
        return {even, odd};
    }
};
```

## Java

```java
class Solution {
    public int[] evenOddBit(int n) {
        int even = 0, odd = 0;
        int idx = 0;
        while (n > 0) {
            if ((n & 1) == 1) {
                if ((idx & 1) == 0) {
                    even++;
                } else {
                    odd++;
                }
            }
            n >>= 1;
            idx++;
        }
        return new int[]{even, odd};
    }
}
```

## Python

```python
class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        even = odd = 0
        idx = 0
        while n:
            if n & 1:
                if idx % 2 == 0:
                    even += 1
                else:
                    odd += 1
            n >>= 1
            idx += 1
        return [even, odd]
```

## Python3

```python
from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = odd = 0
        idx = 0
        while n:
            if n & 1:
                if idx % 2 == 0:
                    even += 1
                else:
                    odd += 1
            n >>= 1
            idx += 1
        return [even, odd]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* evenOddBit(int n, int* returnSize) {
    int even = 0, odd = 0;
    int idx = 0;
    while (n > 0) {
        if (n & 1) {
            if ((idx & 1) == 0)
                even++;
            else
                odd++;
        }
        n >>= 1;
        idx++;
    }
    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = even;
    result[1] = odd;
    *returnSize = 2;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] EvenOddBit(int n) {
        int even = 0, odd = 0;
        int index = 0;
        while (n > 0) {
            if ((n & 1) == 1) {
                if ((index & 1) == 0) {
                    even++;
                } else {
                    odd++;
                }
            }
            n >>= 1;
            index++;
        }
        return new int[] { even, odd };
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number[]}
 */
var evenOddBit = function(n) {
    let even = 0, odd = 0;
    let idx = 0;
    while (n > 0) {
        if ((n & 1) === 1) {
            if ((idx & 1) === 0) {
                even++;
            } else {
                odd++;
            }
        }
        n >>= 1;
        idx++;
    }
    return [even, odd];
};
```

## Typescript

```typescript
function evenOddBit(n: number): number[] {
    let even = 0;
    let odd = 0;
    let idx = 0;
    while (n > 0) {
        if ((n & 1) === 1) {
            if (idx % 2 === 0) {
                even++;
            } else {
                odd++;
            }
        }
        n >>= 1;
        idx++;
    }
    return [even, odd];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function evenOddBit($n) {
        $even = 0;
        $odd = 0;
        $idx = 0;
        while ($n > 0) {
            if ($n & 1) {
                if (($idx & 1) == 0) {
                    $even++;
                } else {
                    $odd++;
                }
            }
            $n >>= 1;
            $idx++;
        }
        return [$even, $odd];
    }
}
```

## Swift

```swift
class Solution {
    func evenOddBit(_ n: Int) -> [Int] {
        var even = 0
        var odd = 0
        var index = 0
        var num = n
        while num > 0 {
            if (num & 1) == 1 {
                if index % 2 == 0 {
                    even += 1
                } else {
                    odd += 1
                }
            }
            num >>= 1
            index += 1
        }
        return [even, odd]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun evenOddBit(n: Int): IntArray {
        var num = n
        var index = 0
        var even = 0
        var odd = 0
        while (num > 0) {
            if ((num and 1) == 1) {
                if (index % 2 == 0) {
                    even++
                } else {
                    odd++
                }
            }
            num = num shr 1
            index++
        }
        return intArrayOf(even, odd)
    }
}
```

## Dart

```dart
class Solution {
  List<int> evenOddBit(int n) {
    int even = 0, odd = 0;
    int index = 0;
    while (n > 0) {
      if ((n & 1) == 1) {
        if (index % 2 == 0) {
          even++;
        } else {
          odd++;
        }
      }
      n >>= 1;
      index++;
    }
    return [even, odd];
  }
}
```

## Golang

```go
func evenOddBit(n int) []int {
    even, odd := 0, 0
    idx := 0
    for n > 0 {
        if n&1 == 1 {
            if idx%2 == 0 {
                even++
            } else {
                odd++
            }
        }
        n >>= 1
        idx++
    }
    return []int{even, odd}
}
```

## Ruby

```ruby
def even_odd_bit(n)
  even = 0
  odd = 0
  idx = 0
  while n > 0
    if (n & 1) == 1
      if idx.even?
        even += 1
      else
        odd += 1
      end
    end
    n >>= 1
    idx += 1
  end
  [even, odd]
end
```

## Scala

```scala
object Solution {
    def evenOddBit(n: Int): Array[Int] = {
        var num = n
        var idx = 0
        var even = 0
        var odd = 0
        while (num > 0) {
            if ((num & 1) == 1) {
                if ((idx & 1) == 0) even += 1 else odd += 1
            }
            num >>= 1
            idx += 1
        }
        Array(even, odd)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn even_odd_bit(n: i32) -> Vec<i32> {
        let mut even = 0;
        let mut odd = 0;
        let mut idx = 0;
        let mut num = n;
        while num > 0 {
            if (num & 1) == 1 {
                if idx % 2 == 0 {
                    even += 1;
                } else {
                    odd += 1;
                }
            }
            num >>= 1;
            idx += 1;
        }
        vec![even, odd]
    }
}
```

## Racket

```racket
(define/contract (even-odd-bit n)
  (-> exact-integer? (listof exact-integer?))
  (let loop ((x n) (idx 0) (even 0) (odd 0))
    (if (= x 0)
        (list even odd)
        (let* ((bit (bitwise-and x 1))
               (new-even (if (and (= bit 1) (even? idx)) (+ even 1) even))
               (new-odd (if (and (= bit 1) (odd? idx)) (+ odd 1) odd)))
          (loop (arithmetic-shift x -1) (+ idx 1) new-even new-odd)))))
```

## Erlang

```erlang
-spec even_odd_bit(N :: integer()) -> [integer()].
even_odd_bit(N) ->
    even_odd_bit(N, 0, 0, 0).

even_odd_bit(0, _Idx, Even, Odd) ->
    [Even, Odd];
even_odd_bit(N, Idx, Even, Odd) ->
    Bit = N band 1,
    {NewEven, NewOdd} =
        case Bit of
            1 ->
                if (Idx rem 2) =:= 0 -> {Even + 1, Odd};
                   true -> {Even, Odd + 1}
                end;
            _ -> {Even, Odd}
        end,
    even_odd_bit(N bsr 1, Idx + 1, NewEven, NewOdd).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec even_odd_bit(n :: integer) :: [integer]
  def even_odd_bit(n) do
    count_bits(n, 0, 0, 0)
  end

  defp count_bits(0, _pos, even, odd), do: [even, odd]

  defp count_bits(n, pos, even, odd) do
    bit = n &&& 1

    {new_even, new_odd} =
      if bit == 1 do
        if rem(pos, 2) == 0 do
          {even + 1, odd}
        else
          {even, odd + 1}
        end
      else
        {even, odd}
      end

    count_bits(n >>> 1, pos + 1, new_even, new_odd)
  end
end
```
