# 2220. Minimum Bit Flips to Convert Number

## Cpp

```cpp
class Solution {
public:
    int minBitFlips(int start, int goal) {
        return __builtin_popcount(start ^ goal);
    }
};
```

## Java

```java
class Solution {
    public int minBitFlips(int start, int goal) {
        return Integer.bitCount(start ^ goal);
    }
}
```

## Python

```python
class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        return (start ^ goal).bit_count()
```

## Python3

```python
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()
```

## C

```c
int minBitFlips(int start, int goal) {
    return __builtin_popcount(start ^ goal);
}
```

## Csharp

```csharp
public class Solution
{
    public int MinBitFlips(int start, int goal)
    {
        int xor = start ^ goal;
        int count = 0;
        while (xor != 0)
        {
            count++;
            xor &= (xor - 1);
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} start
 * @param {number} goal
 * @return {number}
 */
var minBitFlips = function(start, goal) {
    let x = start ^ goal;
    let count = 0;
    while (x !== 0) {
        x &= x - 1;
        count++;
    }
    return count;
};
```

## Typescript

```typescript
function minBitFlips(start: number, goal: number): number {
    let x = start ^ goal;
    let count = 0;
    while (x !== 0) {
        x &= x - 1;
        count++;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $start
     * @param Integer $goal
     * @return Integer
     */
    function minBitFlips($start, $goal) {
        $xor = $start ^ $goal;
        $count = 0;
        while ($xor != 0) {
            $xor &= ($xor - 1);
            $count++;
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func minBitFlips(_ start: Int, _ goal: Int) -> Int {
        return (start ^ goal).nonzeroBitCount
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minBitFlips(start: Int, goal: Int): Int {
        return Integer.bitCount(start xor goal)
    }
}
```

## Dart

```dart
class Solution {
  int minBitFlips(int start, int goal) {
    int x = start ^ goal;
    int count = 0;
    while (x != 0) {
      x &= x - 1;
      count++;
    }
    return count;
  }
}
```

## Golang

```go
package main

import "math/bits"

func minBitFlips(start int, goal int) int {
	return bits.OnesCount(uint(start ^ goal))
}
```

## Ruby

```ruby
# @param {Integer} start
# @param {Integer} goal
# @return {Integer}
def min_bit_flips(start, goal)
  (start ^ goal).to_s(2).count('1')
end
```

## Scala

```scala
object Solution {
    def minBitFlips(start: Int, goal: Int): Int = {
        Integer.bitCount(start ^ goal)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_bit_flips(start: i32, goal: i32) -> i32 {
        (start ^ goal).count_ones() as i32
    }
}
```

## Racket

```racket
#lang racket

(require racket/contract
         racket/bitwise)

(define (popcnt n)
  (let loop ((x n) (c 0))
    (if (= x 0)
        c
        (loop (bitwise-and x (- x 1)) (+ c 1)))))

(define/contract (min-bit-flips start goal)
  (-> exact-integer? exact-integer? exact-integer?)
  (popcnt (bitwise-xor start goal)))
```

## Erlang

```erlang
-module(solution).
-export([min_bit_flips/2]).

-spec min_bit_flips(integer(), integer()) -> integer().
min_bit_flips(Start, Goal) ->
    count_bits(Start bxor Goal).

count_bits(0) -> 0;
count_bits(N) ->
    1 + count_bits(N band (N - 1)).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_bit_flips(start :: integer, goal :: integer) :: integer
  def min_bit_flips(start, goal) do
    Integer.bit_count(Bitwise.bxor(start, goal))
  end
end
```
