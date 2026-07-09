# 0717. 1-bit and 2-bit Characters

## Cpp

```cpp
class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        int n = bits.size();
        int i = 0;
        while (i < n - 1) {
            if (bits[i] == 0)
                ++i;
            else
                i += 2;
        }
        return i == n - 1;
    }
};
```

## Java

```java
class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int i = 0;
        while (i < bits.length - 1) {
            if (bits[i] == 0) {
                i++;
            } else {
                i += 2;
            }
        }
        return i == bits.length - 1;
    }
}
```

## Python

```python
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        n = len(bits)
        while i < n - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return i == n - 1
```

## Python3

```python
from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        while i < n - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return i == n - 1
```

## C

```c
#include <stdbool.h>

bool isOneBitCharacter(int* bits, int bitsSize) {
    int i = 0;
    while (i < bitsSize - 1) {
        if (bits[i] == 0)
            i += 1;
        else
            i += 2;
    }
    return i == bitsSize - 1;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsOneBitCharacter(int[] bits)
    {
        int i = 0;
        int n = bits.Length;
        while (i < n - 1)
        {
            if (bits[i] == 0)
                i++;
            else
                i += 2;
        }
        return i == n - 1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} bits
 * @return {boolean}
 */
var isOneBitCharacter = function(bits) {
    let i = 0;
    const n = bits.length;
    while (i < n - 1) {
        if (bits[i] === 0) {
            i += 1;
        } else {
            i += 2;
        }
    }
    return i === n - 1;
};
```

## Typescript

```typescript
function isOneBitCharacter(bits: number[]): boolean {
    let i = 0;
    const n = bits.length;
    while (i < n - 1) {
        i += bits[i] === 0 ? 1 : 2;
    }
    return i === n - 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $bits
     * @return Boolean
     */
    function isOneBitCharacter($bits) {
        $i = 0;
        $n = count($bits);
        while ($i < $n - 1) {
            if ($bits[$i] == 0) {
                $i += 1;
            } else {
                $i += 2;
            }
        }
        return $i == $n - 1;
    }
}
```

## Swift

```swift
class Solution {
    func isOneBitCharacter(_ bits: [Int]) -> Bool {
        var i = 0
        while i < bits.count - 1 {
            if bits[i] == 0 {
                i += 1
            } else {
                i += 2
            }
        }
        return i == bits.count - 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isOneBitCharacter(bits: IntArray): Boolean {
        var i = 0
        while (i < bits.size - 1) {
            i += if (bits[i] == 0) 1 else 2
        }
        return i == bits.size - 1
    }
}
```

## Dart

```dart
class Solution {
  bool isOneBitCharacter(List<int> bits) {
    int i = 0;
    while (i < bits.length - 1) {
      if (bits[i] == 0) {
        i += 1;
      } else {
        i += 2;
      }
    }
    return i == bits.length - 1;
  }
}
```

## Golang

```go
func isOneBitCharacter(bits []int) bool {
    i := 0
    n := len(bits)
    for i < n-1 {
        if bits[i] == 0 {
            i++
        } else {
            i += 2
        }
    }
    return i == n-1
}
```

## Ruby

```ruby
def is_one_bit_character(bits)
  i = 0
  n = bits.length
  while i < n - 1
    if bits[i] == 0
      i += 1
    else
      i += 2
    end
  end
  i == n - 1
end
```

## Scala

```scala
object Solution {
    def isOneBitCharacter(bits: Array[Int]): Boolean = {
        var i = 0
        while (i < bits.length - 1) {
            if (bits(i) == 0) i += 1 else i += 2
        }
        i == bits.length - 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        let n = bits.len();
        let mut i = 0;
        while i < n - 1 {
            if bits[i] == 0 {
                i += 1;
            } else {
                i += 2;
            }
        }
        i == n - 1
    }
}
```

## Racket

```racket
(define/contract (is-one-bit-character bits)
  (-> (listof exact-integer?) boolean?)
  (let loop ((lst bits))
    (if (null? (cdr lst))               ; only the last bit remains
        #t
        (if (= (car lst) 0)
            (loop (cdr lst))           ; one‑bit character
            (loop (cddr lst))))))      ; two‑bit character)
```

## Erlang

```erlang
-spec is_one_bit_character(Bits :: [integer()]) -> boolean().
is_one_bit_character([]) -> false;
is_one_bit_character([0]) -> true;
is_one_bit_character([0|Rest]) -> is_one_bit_character(Rest);
is_one_bit_character([1,_|Rest]) -> is_one_bit_character(Rest).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_one_bit_character(bits :: [integer]) :: boolean
  def is_one_bit_character(bits) do
    n = length(bits)
    {prefix, [_last]} = Enum.split(bits, n - 1)
    parse(prefix)
  end

  defp parse([]), do: true
  defp parse([0 | rest]), do: parse(rest)
  defp parse([1, _next | rest]), do: parse(rest)
  defp parse([1]), do: false
end
```
