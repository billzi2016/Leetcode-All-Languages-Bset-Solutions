# 0858. Mirror Reflection

## Cpp

```cpp
class Solution {
public:
    int mirrorReflection(int p, int q) {
        int g = std::gcd(p, q);
        long long lcm = 1LL * p / g * q;
        long long m = lcm / p; // horizontal extensions
        long long n = lcm / q; // vertical extensions
        
        if (m % 2 == 1 && n % 2 == 0) return 0;
        if (m % 2 == 1 && n % 2 == 1) return 1;
        // m even, n odd
        return 2;
    }
};
```

## Java

```java
class Solution {
    public int mirrorReflection(int p, int q) {
        int g = gcd(p, q);
        int m = p / g; // horizontal extensions
        int n = q / g; // vertical extensions
        
        if (m % 2 == 1 && n % 2 == 0) return 0;
        if (m % 2 == 1 && n % 2 == 1) return 1;
        // m even, n odd
        return 2;
    }
    
    private int gcd(int a, int b) {
        while (b != 0) {
            int tmp = a % b;
            a = b;
            b = tmp;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        # Compute greatest common divisor
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        lcm = p * q // gcd(p, q)
        k = lcm // p  # number of room extensions horizontally
        m = lcm // q  # number of room extensions vertically

        if k % 2 == 1 and m % 2 == 1:
            return 1
        elif k % 2 == 1 and m % 2 == 0:
            return 2
        else:  # k is even
            return 0
```

## Python3

```python
import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = math.gcd(p, q)
        m = p // g
        n = q // g
        if m % 2 == 0:
            return 2
        elif n % 2 == 1:
            return 1
        else:
            return 0
```

## C

```c
int mirrorReflection(int p, int q) {
    // Compute greatest common divisor
    while (q != 0) {
        int tmp = p % q;
        p = q;
        q = tmp;
    }
    int g = p; // now p holds gcd
    
    int m = p / g; // number of horizontal extensions (rooms)
    int n = q / g; // number of vertical extensions (rooms)
    
    if (m % 2 == 1 && n % 2 == 0) return 0;
    if (m % 2 == 1 && n % 2 == 1) return 1;
    // m even, n odd
    return 2;
}
```

## Csharp

```csharp
public class Solution {
    public int MirrorReflection(int p, int q) {
        int g = Gcd(p, q);
        int m = p / g; // number of room widths traversed
        int n = q / g; // number of room heights traversed

        if (m % 2 == 1 && n % 2 == 1) return 0;
        if (m % 2 == 1 && n % 2 == 0) return 1;
        // m even, n odd
        return 2;
    }

    private int Gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} p
 * @param {number} q
 * @return {number}
 */
var mirrorReflection = function(p, q) {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const g = gcd(p, q);
    const a = q / g; // horizontal extensions
    const b = p / g; // vertical extensions
    if (a % 2 === 1) {
        return b % 2 === 1 ? 1 : 2;
    }
    return 0;
};
```

## Typescript

```typescript
function mirrorReflection(p: number, q: number): number {
    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const g = gcd(p, q);
    const lcm = (p / g) * q; // avoid overflow, but numbers are small
    const m = lcm / p; // horizontal extensions
    const n = lcm / q; // vertical extensions

    if (m % 2 === 1 && n % 2 === 0) return 2;
    if (m % 2 === 1 && n % 2 === 1) return 1;
    // m even, n odd
    return 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $p
     * @param Integer $q
     * @return Integer
     */
    function mirrorReflection($p, $q) {
        // Compute greatest common divisor
        $a = $p;
        $b = $q;
        while ($b != 0) {
            $temp = $a % $b;
            $a = $b;
            $b = $temp;
        }
        $gcd = $a;

        // Least common multiple
        $lcm = intdiv($p, $gcd) * $q;

        // Number of extensions horizontally and vertically
        $m = intdiv($lcm, $p);
        $n = intdiv($lcm, $q);

        if ($m % 2 == 0) {
            return 0;
        }
        if ($n % 2 == 1) {
            return 1;
        }
        return 2;
    }
}
```

## Swift

```swift
class Solution {
    func mirrorReflection(_ p: Int, _ q: Int) -> Int {
        let g = gcd(p, q)
        let m = p / g
        let n = q / g
        if m % 2 == 1 && n % 2 == 0 {
            return 0
        } else if m % 2 == 1 && n % 2 == 1 {
            return 1
        } else {
            return 2
        }
    }
    
    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a
        var y = b
        while y != 0 {
            let temp = x % y
            x = y
            y = temp
        }
        return x
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mirrorReflection(p: Int, q: Int): Int {
        val g = gcd(p, q)
        val n = p / g
        val k = q / g
        return when {
            n % 2 == 1 && k % 2 == 0 -> 0
            n % 2 == 1 && k % 2 == 1 -> 1
            else -> 2
        }
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return x
    }
}
```

## Dart

```dart
class Solution {
  int _gcd(int a, int b) {
    while (b != 0) {
      int t = a % b;
      a = b;
      b = t;
    }
    return a;
  }

  int mirrorReflection(int p, int q) {
    int g = _gcd(p, q);
    int n = p ~/ g; // number of room extensions horizontally
    int m = q ~/ g; // number of room extensions vertically

    bool nOdd = n % 2 == 1;
    bool mOdd = m % 2 == 1;

    if (nOdd && !mOdd) return 0; // east-bottom corner
    if (nOdd && mOdd) return 1;   // east-top corner
    // n even, m odd
    return 2;                     // west-top corner
  }
}
```

## Golang

```go
func mirrorReflection(p int, q int) int {
    gcd := func(a, b int) int {
        for b != 0 {
            a, b = b, a%b
        }
        return a
    }
    g := gcd(p, q)
    m := p / g
    n := q / g
    if m%2 == 1 && n%2 == 0 {
        return 0
    }
    if m%2 == 1 && n%2 == 1 {
        return 1
    }
    return 2
}
```

## Ruby

```ruby
def mirror_reflection(p, q)
  g = p.gcd(q)
  m = q / g
  n = p / g
  if m.odd?
    n.odd? ? 1 : 0
  else
    2
  end
end
```

## Scala

```scala
object Solution {
    def mirrorReflection(p: Int, q: Int): Int = {
        val g = gcd(p, q)
        val m = p / g
        val n = q / g
        if (m % 2 == 1 && n % 2 == 0) 0
        else if (m % 2 == 1 && n % 2 == 1) 1
        else 2
    }

    private def gcd(a: Int, b: Int): Int = {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        x
    }
}
```

## Rust

```rust
impl Solution {
    pub fn mirror_reflection(p: i32, q: i32) -> i32 {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let r = a % b;
                a = b;
                b = r;
            }
            a.abs()
        }
        let g = gcd(p, q);
        let h = p / g; // number of room extensions horizontally
        let v = q / g; // number of room extensions vertically

        if h % 2 == 1 && v % 2 == 0 {
            0
        } else if h % 2 == 1 && v % 2 == 1 {
            1
        } else {
            2
        }
    }
}
```

## Racket

```racket
(define/contract (mirror-reflection p q)
  (-> exact-integer? exact-integer? exact-integer?)
  (letrec ([gcd
            (lambda (a b)
              (if (= b 0)
                  a
                  (gcd b (remainder a b))))])
    (let* ([g (gcd p q)]
           [l (/ (* p q) g)]               ; least common multiple
           [a (quotient l p)]               ; horizontal extensions
           [b (quotient l q)])              ; vertical extensions
      (cond [(and (= (remainder a 2) 1) (= (remainder b 2) 0)) 2]
            [(and (= (remainder a 2) 1) (= (remainder b 2) 1)) 1]
            [else 0]))))
```

## Erlang

```erlang
-module(solution).
-export([mirror_reflection/2]).

-spec mirror_reflection(P :: integer(), Q :: integer()) -> integer().
mirror_reflection(P, Q) ->
    G = erlang:gcd(P, Q),
    L = (P div G) * Q,
    M = L div P,
    N = L div Q,
    case {M rem 2, N rem 2} of
        {0, _} -> 0;
        {1, 1} -> 1;
        {1, 0} -> 2
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec mirror_reflection(p :: integer, q :: integer) :: integer
  def mirror_reflection(p, q) do
    g = Integer.gcd(p, q)
    lcm = div(p * q, g)
    h = div(lcm, q)
    v = div(lcm, p)

    cond do
      rem(h, 2) == 1 and rem(v, 2) == 0 -> 0
      rem(h, 2) == 1 and rem(v, 2) == 1 -> 1
      rem(h, 2) == 0 and rem(v, 2) == 1 -> 2
    end
  end
end
```
