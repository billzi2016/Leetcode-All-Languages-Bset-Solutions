# 2683. Neighboring Bitwise XOR

## Cpp

```cpp
class Solution {
public:
    bool doesValidArrayExist(std::vector<int>& derived) {
        int xr = 0;
        for (int v : derived) xr ^= v;
        return xr == 0;
    }
};
```

## Java

```java
class Solution {
    public boolean doesValidArrayExist(int[] derived) {
        int xor = 0;
        for (int v : derived) {
            xor ^= v;
        }
        return xor == 0;
    }
}
```

## Python

```python
class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        xor_sum = 0
        for val in derived:
            xor_sum ^= val
        return xor_sum == 0
```

## Python3

```python
from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        x = 0
        for v in derived:
            x ^= v
        return x == 0
```

## C

```c
#include <stdbool.h>

bool doesValidArrayExist(int* derived, int derivedSize) {
    int xorAll = 0;
    for (int i = 0; i < derivedSize; ++i) {
        xorAll ^= derived[i];
    }
    return xorAll == 0;
}
```

## Csharp

```csharp
public class Solution
{
    public bool DoesValidArrayExist(int[] derived)
    {
        int xor = 0;
        foreach (int val in derived)
            xor ^= val;
        return xor == 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} derived
 * @return {boolean}
 */
var doesValidArrayExist = function(derived) {
    let x = 0;
    for (let v of derived) {
        x ^= v;
    }
    return x === 0;
};
```

## Typescript

```typescript
function doesValidArrayExist(derived: number[]): boolean {
    let xor = 0;
    for (const val of derived) {
        xor ^= val;
    }
    return xor === 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $derived
     * @return Boolean
     */
    function doesValidArrayExist($derived) {
        $xor = 0;
        foreach ($derived as $v) {
            $xor ^= $v;
        }
        return $xor === 0;
    }
}
```

## Swift

```swift
class Solution {
    func doesValidArrayExist(_ derived: [Int]) -> Bool {
        var xorSum = 0
        for value in derived {
            xorSum ^= value
        }
        return xorSum == 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun doesValidArrayExist(derived: IntArray): Boolean {
        var xorSum = 0
        for (value in derived) {
            xorSum = xorSum xor value
        }
        return xorSum == 0
    }
}
```

## Dart

```dart
class Solution {
  bool doesValidArrayExist(List<int> derived) {
    int xorSum = 0;
    for (int val in derived) {
      xorSum ^= val;
    }
    return xorSum == 0;
  }
}
```

## Golang

```go
func doesValidArrayExist(derived []int) bool {
	xor := 0
	for _, v := range derived {
		xor ^= v
	}
	return xor == 0
}
```

## Ruby

```ruby
# @param {Integer[]} derived
# @return {Boolean}
def does_valid_array_exist(derived)
  xor = 0
  derived.each { |v| xor ^= v }
  xor == 0
end
```

## Scala

```scala
object Solution {
    def doesValidArrayExist(derived: Array[Int]): Boolean = {
        var xorSum = 0
        for (v <- derived) {
            xorSum ^= v
        }
        xorSum == 0
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn does_valid_array_exist(derived: Vec<i32>) -> bool {
        let mut xor_sum = 0;
        for val in derived {
            xor_sum ^= val;
        }
        xor_sum == 0
    }
}
```

## Racket

```racket
(define/contract (does-valid-array-exist derived)
  (-> (listof exact-integer?) boolean?)
  (let loop ((xs derived) (acc 0))
    (if (null? xs)
        (= acc 0)
        (loop (cdr xs) (bitwise-xor acc (car xs))))))
```

## Erlang

```erlang
-spec does_valid_array_exist(Derived :: [integer()]) -> boolean().
does_valid_array_exist(Derived) ->
    Xor = lists:foldl(fun(Val, Acc) -> Val bxor Acc end, 0, Derived),
    Xor == 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec does_valid_array_exist(derived :: [integer]) :: boolean
  def does_valid_array_exist(derived) do
    xor = Enum.reduce(derived, 0, fn x, acc -> Bitwise.bxor(acc, x) end)
    xor == 0
  end
end
```
