# 0319. Bulb Switcher

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int bulbSwitch(int n) {
        return static_cast<int>(sqrt(static_cast<double>(n)));
    }
};
```

## Java

```java
class Solution {
    public int bulbSwitch(int n) {
        return (int) Math.sqrt(n);
    }
}
```

## Python

```python
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return math.isqrt(n)
```

## Python3

```python
import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.isqrt(n)
```

## C

```c
#include <math.h>

int bulbSwitch(int n) {
    return (int)sqrt((double)n);
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int BulbSwitch(int n) {
        return (int)Math.Sqrt(n);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var bulbSwitch = function(n) {
    return Math.floor(Math.sqrt(n));
};
```

## Typescript

```typescript
function bulbSwitch(n: number): number {
    return Math.floor(Math.sqrt(n));
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function bulbSwitch($n) {
        return (int)sqrt($n);
    }
}
```

## Swift

```swift
class Solution {
    func bulbSwitch(_ n: Int) -> Int {
        return Int(Double(n).squareRoot())
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun bulbSwitch(n: Int): Int {
        return kotlin.math.sqrt(n.toDouble()).toInt()
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int bulbSwitch(int n) {
    return sqrt(n).toInt();
  }
}
```

## Golang

```go
package main

import "math"

func bulbSwitch(n int) int {
	return int(math.Sqrt(float64(n)))
}
```

## Ruby

```ruby
def bulb_switch(n)
  Math.sqrt(n).to_i
end
```

## Scala

```scala
object Solution {
    def bulbSwitch(n: Int): Int = {
        math.sqrt(n.toDouble).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn bulb_switch(n: i32) -> i32 {
        ((n as f64).sqrt()) as i32
    }
}
```

## Racket

```racket
(define/contract (bulb-switch n)
  (-> exact-integer? exact-integer?)
  (let loop ((lo 0) (hi n))
    (if (> lo hi)
        hi
        (let* ((mid (quotient (+ lo hi) 2))
               (sq (* mid mid)))
          (cond [(= sq n) mid]
                [(< sq n) (loop (+ mid 1) hi)]
                [else (loop lo (- mid 1))])))))
```

## Erlang

```erlang
-module(solution).
-export([bulb_switch/1]).

-spec bulb_switch(N :: integer()) -> integer().
bulb_switch(N) when N >= 0 ->
    trunc(math:sqrt(N)).
```

## Elixir

```elixir
defmodule Solution do
  @spec bulb_switch(n :: integer) :: integer
  def bulb_switch(n) do
    :math.sqrt(n) |> trunc()
  end
end
```
