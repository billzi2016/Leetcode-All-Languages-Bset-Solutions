# 1952. Three Divisors

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isThree(int n) {
        int root = (int)sqrt(n);
        if ((long long)root * root != n) return false;
        if (root < 2) return false;
        for (int i = 2; i * i <= root; ++i) {
            if (root % i == 0) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isThree(int n) {
        int root = (int) Math.sqrt(n);
        if (root * root != n) {
            return false;
        }
        if (root < 2) {
            return false;
        }
        for (int i = 2; i * i <= root; i++) {
            if (root % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
import math

class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        root = int(math.isqrt(n))
        if root * root != n:
            return False
        if root < 2:
            return False
        if root % 2 == 0:
            return root == 2
        i = 3
        while i * i <= root:
            if root % i == 0:
                return False
            i += 2
        return True
```

## Python3

```python
class Solution:
    def isThree(self, n: int) -> bool:
        import math
        root = math.isqrt(n)
        if root * root != n:
            return False
        if root < 2:
            return False
        # check primality of root
        limit = int(math.isqrt(root))
        for i in range(2, limit + 1):
            if root % i == 0:
                return False
        return True
```

## C

```c
#include <stdbool.h>
#include <math.h>

static bool isPrime(int x) {
    if (x < 2) return false;
    if (x % 2 == 0) return x == 2;
    for (int i = 3; i * i <= x; i += 2)
        if (x % i == 0) return false;
    return true;
}

bool isThree(int n) {
    int r = (int)sqrt((double)n);
    if ((long long)r * r != n) return false;
    return isPrime(r);
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsThree(int n)
    {
        int root = (int)Math.Sqrt(n);
        if (root * root != n) return false;
        if (root < 2) return false;
        for (int i = 2; i * i <= root; i++)
        {
            if (root % i == 0) return false;
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
var isThree = function(n) {
    const r = Math.floor(Math.sqrt(n));
    if (r * r !== n) return false;
    if (r < 2) return false;
    for (let i = 2; i * i <= r; ++i) {
        if (r % i === 0) return false;
    }
    return true;
};
```

## Typescript

```typescript
function isThree(n: number): boolean {
    const root = Math.floor(Math.sqrt(n));
    if (root * root !== n) return false;
    if (root < 2) return false;
    for (let i = 2; i * i <= root; i++) {
        if (root % i === 0) return false;
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
    function isThree($n) {
        if ($n < 4) return false;
        $root = (int)sqrt($n);
        if ($root * $root !== $n) return false;
        if ($root < 2) return false;
        for ($i = 2; $i * $i <= $root; $i++) {
            if ($root % $i === 0) return false;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isThree(_ n: Int) -> Bool {
        let root = Int(Double(n).squareRoot())
        if root * root != n { return false }
        if root < 2 { return false }
        var i = 2
        while i * i <= root {
            if root % i == 0 { return false }
            i += 1
        }
        return true
    }
}
```

## Kotlin

```kotlin
import kotlin.math.sqrt

class Solution {
    fun isThree(n: Int): Boolean {
        if (n < 4) return false
        val root = sqrt(n.toDouble()).toInt()
        if (root * root != n) return false
        return isPrime(root)
    }

    private fun isPrime(x: Int): Boolean {
        if (x < 2) return false
        if (x % 2 == 0) return x == 2
        var i = 3
        while (i * i <= x) {
            if (x % i == 0) return false
            i += 2
        }
        return true
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  bool isThree(int n) {
    int root = sqrt(n).toInt();
    if (root * root != n) return false;
    return _isPrime(root);
  }

  bool _isPrime(int x) {
    if (x < 2) return false;
    for (int i = 2; i * i <= x; ++i) {
      if (x % i == 0) return false;
    }
    return true;
  }
}
```

## Golang

```go
package main

import "math"

func isThree(n int) bool {
	if n < 4 {
		return false
	}
	root := int(math.Sqrt(float64(n)))
	if root*root != n {
		return false
	}
	for i := 2; i*i <= root; i++ {
		if root%i == 0 {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def is_three(n)
  return false if n < 4
  r = Math.sqrt(n).to_i
  return false unless r * r == n
  return false if r < 2
  i = 2
  while i * i <= r
    return false if r % i == 0
    i += 1
  end
  true
end
```

## Scala

```scala
object Solution {
    def isThree(n: Int): Boolean = {
        val r = math.sqrt(n.toDouble).toInt
        if (r * r != n) return false
        if (r < 2) return false
        var i = 2
        while (i * i <= r) {
            if (r % i == 0) return false
            i += 1
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_three(n: i32) -> bool {
        if n < 4 {
            return false;
        }
        let root = (n as f64).sqrt() as i32;
        if root * root != n {
            return false;
        }
        if root < 2 {
            return false;
        }
        let mut i = 2;
        while i * i <= root {
            if root % i == 0 {
                return false;
            }
            i += 1;
        }
        true
    }
}
```

## Racket

```racket
(define (prime? p)
  (if (< p 2)
      #false
      (let loop ((i 2))
        (cond [(> (* i i) p) #true]
              [(zero? (remainder p i)) #false]
              [else (loop (+ i 1))]))))

(define/contract (is-three n)
  (-> exact-integer? boolean?)
  (if (< n 4)
      #false
      (let* ((root (inexact->exact (floor (sqrt n))))
             (sq (* root root)))
        (and (= sq n) (prime? root)))))
```

## Erlang

```erlang
-module(solution).
-export([is_three/1]).

-spec is_three(N :: integer()) -> boolean().
is_three(N) ->
    case N of
        _ when N < 4 -> false;
        _ ->
            S = trunc(math:sqrt(N)),
            if S * S =:= N ->
                    is_prime(S);
               true -> false
            end
    end.

-spec is_prime(P :: integer()) -> boolean().
is_prime(P) when P =< 1 -> false;
is_prime(2) -> true;
is_prime(P) when P rem 2 =:= 0 -> false;
is_prime(P) ->
    Max = trunc(math:sqrt(P)),
    is_prime_loop(P, 3, Max).

-spec is_prime_loop(integer(), integer(), integer()) -> boolean().
is_prime_loop(_P, I, Max) when I > Max -> true;
is_prime_loop(P, I, Max) ->
    if P rem I =:= 0 -> false; true -> is_prime_loop(P, I + 2, Max) end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_three(n :: integer) :: boolean
  def is_three(n) do
    root = :math.sqrt(n) |> trunc()
    if root * root != n do
      false
    else
      prime?(root)
    end
  end

  defp prime?(k) when k <= 1, do: false
  defp prime?(2), do: true
  defp prime?(k) do
    limit = :math.sqrt(k) |> trunc()
    Enum.all?(2..limit, fn i -> rem(k, i) != 0 end)
  end
end
```
