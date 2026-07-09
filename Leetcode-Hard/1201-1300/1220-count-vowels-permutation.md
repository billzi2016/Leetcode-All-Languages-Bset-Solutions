# 1220. Count Vowels Permutation

## Cpp

```cpp
class Solution {
public:
    int countVowelPermutation(int n) {
        const int MOD = 1000000007;
        long long a = 1, e = 1, i = 1, o = 1, u = 1; // length 1
        for (int len = 2; len <= n; ++len) {
            long long na = e % MOD;
            long long ne = (a + i) % MOD;
            long long ni = (a + e + o + u) % MOD;
            long long no = (i + u) % MOD;
            long long nu = a % MOD;
            a = na; e = ne; i = ni; o = no; u = nu;
        }
        long long result = (a + e + i + o + u) % MOD;
        return static_cast<int>(result);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int countVowelPermutation(int n) {
        long a = 1, e = 1, i = 1, o = 1, u = 1; // length 1
        for (int len = 2; len <= n; ++len) {
            long na = e % MOD;
            long ne = (a + i) % MOD;
            long ni = (a + e + o + u) % MOD;
            long no = (i + u) % MOD;
            long nu = a % MOD;
            a = na;
            e = ne;
            i = ni;
            o = no;
            u = nu;
        }
        long result = (a + e + i + o + u) % MOD;
        return (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        a = e = i = o = u = 1  # length 1 counts
        for _ in range(2, n + 1):
            na = (e + i + u) % MOD
            ne = (a + i) % MOD
            ni = (e + o) % MOD
            no = i % MOD
            nu = (i + o) % MOD
            a, e, i, o, u = na, ne, ni, no, nu
        return (a + e + i + o + u) % MOD
```

## Python3

```python
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        # dp for a, e, i, o, u respectively
        a = e = i = o = u = 1
        for _ in range(2, n + 1):
            na = e % MOD
            ne = (a + i) % MOD
            ni = (a + e + o + u) % MOD
            no = (i + u) % MOD
            nu = a % MOD
            a, e, i, o, u = na, ne, ni, no, nu
        return (a + e + i + o + u) % MOD
```

## C

```c
int countVowelPermutation(int n) {
    const int MOD = 1000000007;
    long long a = 1, e = 1, i = 1, o = 1, u = 1;
    for (int len = 2; len <= n; ++len) {
        long long na = (e + i + u) % MOD;
        long long ne = (a + i) % MOD;
        long long ni = (e + o) % MOD;
        long long no = i % MOD;
        long long nu = (i + o) % MOD;
        a = na; e = ne; i = ni; o = no; u = nu;
    }
    return (int)((a + e + i + o + u) % MOD);
}
```

## Csharp

```csharp
public class Solution {
    public int CountVowelPermutation(int n) {
        const long MOD = 1000000007L;
        // counts for strings ending with a, e, i, o, u respectively
        long a = 1, e = 1, i = 1, o = 1, u = 1;
        for (int len = 2; len <= n; ++len) {
            long na = (e + u) % MOD;
            long ne = (a + i) % MOD;
            long ni = (a + e + o + u) % MOD;
            long no = i % MOD;
            long nu = (i + o) % MOD;
            a = na; e = ne; i = ni; o = no; u = nu;
        }
        long result = (a + e + i + o + u) % MOD;
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countVowelPermutation = function(n) {
    const MOD = 1000000007;
    // dp for length 1
    let a = 1, e = 1, i = 1, o = 1, u = 1;
    for (let len = 2; len <= n; ++len) {
        const na = e % MOD;
        const ne = (a + i) % MOD;
        const ni = (a + e + o + u) % MOD;
        const no = i % MOD;
        const nu = (a + o) % MOD;
        a = na; e = ne; i = ni; o = no; u = nu;
    }
    return ((a + e + i + o + u) % MOD);
};
```

## Typescript

```typescript
function countVowelPermutation(n: number): number {
    const MOD = 1_000_000_007;
    let a = 1, e = 1, i = 1, o = 1, u = 1;
    for (let len = 2; len <= n; ++len) {
        const na = (e + u) % MOD;
        const ne = (a + i) % MOD;
        const ni = (e + o) % MOD;
        const no = i % MOD;
        const nu = (i + o) % MOD;
        a = na; e = ne; i = ni; o = no; u = nu;
    }
    return ((a + e + i + o + u) % MOD);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countVowelPermutation($n) {
        $mod = 1000000007;
        if ($n == 1) return 5;

        $a = $e = $i = $o = $u = 1; // length 1 counts

        for ($len = 2; $len <= $n; $len++) {
            $na = ($e + $i + $u) % $mod;
            $ne = ($a + $i) % $mod;
            $ni = ($e + $o) % $mod;
            $no = $i % $mod;
            $nu = ($i + $o) % $mod;

            $a = $na;
            $e = $ne;
            $i = $ni;
            $o = $no;
            $u = $nu;
        }

        return (int)(($a + $e + $i + $o + $u) % $mod);
    }
}
```

## Swift

```swift
class Solution {
    func countVowelPermutation(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        var a = 1, e = 1, i = 1, o = 1, u = 1
        if n == 1 { return (a + e + i + o + u) % MOD }
        for _ in 2...n {
            let newA = (e + i + u) % MOD
            let newE = (a + i) % MOD
            let newI = (e + o) % MOD
            let newO = i % MOD
            let newU = (i + o) % MOD
            a = newA
            e = newE
            i = newI
            o = newO
            u = newU
        }
        return ((a + e + i + o + u) % MOD)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countVowelPermutation(n: Int): Int {
        val MOD = 1_000_000_007L
        var a = 1L
        var e = 1L
        var i = 1L
        var o = 1L
        var u = 1L
        for (step in 2..n) {
            val na = e % MOD
            val ne = (a + i) % MOD
            val ni = (a + e + o + u) % MOD
            val no = (i + u) % MOD
            val nu = o % MOD
            a = na
            e = ne
            i = ni
            o = no
            u = nu
        }
        return ((a + e + i + o + u) % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int countVowelPermutation(int n) {
    const int MOD = 1000000007;
    if (n == 0) return 0;
    int a = 1, e = 1, i = 1, o = 1, u = 1;
    for (int len = 2; len <= n; ++len) {
      int na = e % MOD;
      int ne = (a + i) % MOD;
      int ni = ((a + e) % MOD + (o + u) % MOD) % MOD;
      int no = (i + u) % MOD;
      int nu = a % MOD;
      a = na;
      e = ne;
      i = ni;
      o = no;
      u = nu;
    }
    return ((a + e) % MOD + (i + o) % MOD + u) % MOD;
  }
}
```

## Golang

```go
func countVowelPermutation(n int) int {
	const MOD int64 = 1000000007
	var a, e, i, o, u int64 = 1, 1, 1, 1, 1 // counts for 'a','e','i','o','u' at current length

	for step := 2; step <= n; step++ {
		newA := e % MOD
		newE := (a + i) % MOD
		newI := (a + e + o + u) % MOD
		newO := (i + u) % MOD
		newU := o % MOD

		a, e, i, o, u = newA, newE, newI, newO, newU
	}
	total := (a + e + i + o + u) % MOD
	return int(total)
}
```

## Ruby

```ruby
def count_vowel_permutation(n)
  mod = 1_000_000_007
  a = e = i = o = u = 1
  (2..n).each do
    na = e % mod
    ne = (a + i) % mod
    ni = (a + e + o + u) % mod
    no = (i + u) % mod
    nu = a % mod
    a, e, i, o, u = na, ne, ni, no, nu
  end
  (a + e + i + o + u) % mod
end
```

## Scala

```scala
object Solution {
    def countVowelPermutation(n: Int): Int = {
        val MOD = 1000000007L
        var a = 1L
        var e = 1L
        var i = 1L
        var o = 1L
        var u = 1L
        for (_ <- 2 to n) {
            val na = (e + i + u) % MOD
            val ne = (a + i) % MOD
            val ni = (e + o) % MOD
            val no = i % MOD
            val nu = (i + o) % MOD
            a = na; e = ne; i = ni; o = no; u = nu
        }
        ((a + e + i + o + u) % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_vowel_permutation(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut a: i64 = 1;
        let mut e: i64 = 1;
        let mut i_v: i64 = 1;
        let mut o: i64 = 1;
        let mut u: i64 = 1;

        for _ in 2..=n {
            let na = (e + i_v + u) % MOD;
            let ne = (a + i_v) % MOD;
            let ni = (e + o) % MOD;
            let no = i_v % MOD;
            let nu = (i_v + o) % MOD;

            a = na;
            e = ne;
            i_v = ni;
            o = no;
            u = nu;
        }

        ((a + e + i_v + o + u) % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (count-vowel-permutation n)
  (-> exact-integer? exact-integer?)
  (let loop ((idx 2)
             (a 1)   ; strings ending with 'a'
             (e 1)   ; strings ending with 'e'
             (i 1)   ; strings ending with 'i'
             (o 1)   ; strings ending with 'o'
             (u 1))  ; strings ending with 'u'
    (if (> idx n)
        (modulo (+ a e i o u) MOD)
        (let* ((new-a (modulo (+ e u) MOD))
               (new-e (modulo (+ a i) MOD))
               (new-i (modulo (+ a e o u) MOD))
               (new-o (modulo (+ i u) MOD))
               (new-u (modulo a MOD)))
          (loop (+ idx 1) new-a new-e new-i new-o new-u)))))
```

## Erlang

```erlang
-module(solution).
-export([count_vowel_permutation/1]).

-spec count_vowel_permutation(N :: integer()) -> integer().
count_vowel_permutation(1) ->
    5;
count_vowel_permutation(N) when N > 1 ->
    Mod = 1000000007,
    Steps = N - 1,
    {A, E, I, O, U} = loop(Steps, 1, 1, 1, 1, 1, Mod),
    (A + E + I + O + U) rem Mod.

loop(0, A, E, I, O, U, _Mod) ->
    {A, E, I, O, U};
loop(K, A, E, I, O, U, Mod) ->
    NewA = (E + I + U) rem Mod,
    NewE = (A + I) rem Mod,
    NewI = (E + O) rem Mod,
    NewO = I rem Mod,
    NewU = (I + O) rem Mod,
    loop(K - 1, NewA, NewE, NewI, NewO, NewU, Mod).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_vowel_permutation(n :: integer) :: integer
  def count_vowel_permutation(n) do
    mod = 1_000_000_007

    if n == 1 do
      5
    else
      {a, e, i, o, u} =
        Enum.reduce(2..n, {1, 1, 1, 1, 1}, fn _, {a, e, i, o, u} ->
          na = e
          ne = rem(a + i, mod)
          ni = rem(a + e + o + u, mod)
          no = rem(i + u, mod)
          nu = o
          {na, ne, ni, no, nu}
        end)

      rem(a + e + i + o + u, mod)
    end
  end
end
```
