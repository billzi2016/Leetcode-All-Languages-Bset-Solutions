# 0869. Reordered Power of 2

## Cpp

```cpp
class Solution {
public:
    bool reorderedPowerOf2(int n) {
        string s = to_string(n);
        sort(s.begin(), s.end());
        for (int i = 0; i <= 33; ++i) {
            long long p = 1LL << i;
            string t = to_string(p);
            sort(t.begin(), t.end());
            if (s == t) return true;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean reorderedPowerOf2(int n) {
        int[] target = digitCount(n);
        for (int i = 0; i <= 30; i++) {
            if (sameCount(target, digitCount(1 << i))) return true;
        }
        return false;
    }

    private int[] digitCount(int x) {
        int[] cnt = new int[10];
        while (x > 0) {
            cnt[x % 10]++;
            x /= 10;
        }
        return cnt;
    }

    private boolean sameCount(int[] a, int[] b) {
        for (int i = 0; i < 10; i++) {
            if (a[i] != b[i]) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        target = sorted(str(n))
        # generate powers of two up to 10 digits (since n <= 1e9)
        p = 1
        while len(str(p)) <= len(str(n)):
            if sorted(str(p)) == target:
                return True
            p <<= 1
        # also need to check the next power in case it has same length due to leading zeros not allowed,
        # but its length could be equal; we already covered up to same length.
        return False
```

## Python3

```python
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target = ''.join(sorted(str(n)))
        p = 1
        while p < 10 ** 10:
            if ''.join(sorted(str(p))) == target:
                return True
            p <<= 1
        return False
```

## C

```c
#include <stdbool.h>

bool reorderedPowerOf2(int n) {
    int cnt[10] = {0};
    int temp = n;
    while (temp > 0) {
        cnt[temp % 10]++;
        temp /= 10;
    }
    for (long long p = 1; p < 10000000000LL; p <<= 1) {
        int cnt2[10] = {0};
        long long t = p;
        while (t > 0) {
            cnt2[t % 10]++;
            t /= 10;
        }
        bool same = true;
        for (int i = 0; i < 10; ++i) {
            if (cnt[i] != cnt2[i]) {
                same = false;
                break;
            }
        }
        if (same) return true;
    }
    return false;
}
```

## Csharp

```csharp
public class Solution
{
    public bool ReorderedPowerOf2(int n)
    {
        string target = SortedDigits(n);
        for (int i = 0; i < 31; i++)
        {
            int power = 1 << i;
            if (SortedDigits(power) == target)
                return true;
        }
        return false;
    }

    private string SortedDigits(int x)
    {
        char[] chars = x.ToString().ToCharArray();
        Array.Sort(chars);
        return new string(chars);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var reorderedPowerOf2 = function(n) {
    const target = n.toString().split('').sort().join('');
    for (let i = 0; i < 31; ++i) {
        const p = Math.pow(2, i);
        if (p.toString().length !== n.toString().length) continue;
        if (p.toString().split('').sort().join('') === target) return true;
    }
    return false;
};
```

## Typescript

```typescript
function reorderedPowerOf2(n: number): boolean {
    const target = n.toString().split('').sort().join('');
    for (let i = 0; ; i++) {
        const pow = Math.pow(2, i);
        if (pow > 1e10) break;
        if (pow.toString().split('').sort().join('') === target) return true;
    }
    return false;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function reorderedPowerOf2($n) {
        $target = $this->signature($n);
        for ($i = 0; $i < 32; $i++) {
            $p = (int)pow(2, $i);
            if ($this->signature($p) === $target) {
                return true;
            }
        }
        return false;
    }

    private function signature($num) {
        $digits = str_split((string)$num);
        sort($digits);
        return implode('', $digits);
    }
}
```

## Swift

```swift
class Solution {
    func reorderedPowerOf2(_ n: Int) -> Bool {
        let target = String(n).sorted()
        var power = 1
        // Upper bound enough to cover all powers with up to 10 digits (max for n <= 1e9)
        while power <= 10_000_000_000 {
            if String(power).sorted() == target {
                return true
            }
            power <<= 1
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reorderedPowerOf2(n: Int): Boolean {
        val target = n.toString().toCharArray().sorted().joinToString("")
        for (i in 0..30) {
            val pow = 1L shl i
            if (pow.toString().toCharArray().sorted().joinToString("") == target) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool reorderedPowerOf2(int n) {
    String s = n.toString();
    List<int> cnt = List.filled(10, 0);
    for (int c in s.codeUnits) {
      cnt[c - 48]++;
    }

    int power = 1;
    while (power < 10000000000) { // up to 10 digits
      String pStr = power.toString();
      if (pStr.length == s.length) {
        List<int> cntP = List.filled(10, 0);
        for (int c in pStr.codeUnits) {
          cntP[c - 48]++;
        }
        bool same = true;
        for (int i = 0; i < 10; i++) {
          if (cnt[i] != cntP[i]) {
            same = false;
            break;
          }
        }
        if (same) return true;
      }
      power <<= 1;
    }
    return false;
  }
}
```

## Golang

```go
func reorderedPowerOf2(n int) bool {
    cntN := digitCount(int64(n))
    for i := 0; ; i++ {
        p := int64(1) << i
        if p > 10000000000 { // 10^10, exceeds max possible permutation length (10 digits)
            break
        }
        if digitCount(p) == cntN {
            return true
        }
    }
    return false
}

func digitCount(x int64) [10]int {
    var cnt [10]int
    if x == 0 {
        cnt[0] = 1
        return cnt
    }
    for x > 0 {
        cnt[x%10]++
        x /= 10
    }
    return cnt
}
```

## Ruby

```ruby
def reordered_power_of2(n)
  target = n.to_s.chars.sort.join
  pow = 1
  limit = 2_000_000_000
  while pow <= limit
    return true if pow.to_s.chars.sort.join == target
    pow <<= 1
  end
  false
end
```

## Scala

```scala
object Solution {
    def reorderedPowerOf2(n: Int): Boolean = {
        val target = n.toString.sorted
        var i = 0
        while (i < 31) {
            if ((1 << i).toString.sorted == target) return true
            i += 1
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reordered_power_of2(n: i32) -> bool {
        fn count_digits(mut x: i64) -> [i32; 10] {
            let mut cnt = [0i32; 10];
            if x == 0 {
                cnt[0] = 1;
                return cnt;
            }
            while x > 0 {
                cnt[(x % 10) as usize] += 1;
                x /= 10;
            }
            cnt
        }

        let target = count_digits(n as i64);
        let mut p: i64 = 1;
        // 2^30 = 1073741824 > 1e9, sufficient for the given constraints
        while p <= (1i64 << 30) {
            if count_digits(p) == target {
                return true;
            }
            p <<= 1;
        }
        false
    }
}
```

## Racket

```racket
(define/contract (reordered-power-of2 n)
  (-> exact-integer? boolean?)
  (let ([target
         (let ([cnt (make-vector 10 0)])
           (let loop ((x n))
             (if (= x 0)
                 cnt
                 (begin
                   (vector-set! cnt (remainder x 10)
                                (+ 1 (vector-ref cnt (remainder x 10))))
                   (loop (quotient x 10))))))])
    (define (same-count? v1 v2)
      (let loop ((i 0))
        (or (= i 10)
            (and (= (vector-ref v1 i) (vector-ref v2 i))
                 (loop (+ i 1))))))
    (let loop ((p 1))
      (cond [(> p 10000000000) #f]
            [(same-count? target
                         (let ([cnt (make-vector 10 0)])
                           (let inner ((x p))
                             (if (= x 0)
                                 cnt
                                 (begin
                                   (vector-set! cnt (remainder x 10)
                                                (+ 1 (vector-ref cnt (remainder x 10))))
                                   (inner (quotient x 10)))))))
             #t]
            [else (loop (* p 2))]))))
```

## Erlang

```erlang
-module(solution).
-export([reordered_power_of2/1]).

-spec reordered_power_of2(N :: integer()) -> boolean().
reordered_power_of2(N) ->
    Sig = signature(N),
    PowersSigs = power_two_signatures(),
    lists:any(fun(P) -> P =:= Sig end, PowersSigs).

signature(N) ->
    lists:sort(integer_to_list(N)).

power_two_signatures() ->
    generate_powers(1, []).

generate_powers(Pow, Acc) when Pow > 0 ->
    Str = integer_to_list(Pow),
    case length(Str) of
        Len when Len =< 10 ->
            Sig = lists:sort(Str),
            generate_powers(Pow * 2, [Sig | Acc]);
        _ ->
            lists:reverse(Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec reordered_power_of2(n :: integer) :: boolean
  def reordered_power_of2(n) do
    target = sort_digits(Integer.to_string(n))

    Stream.iterate(1, &(&1 * 2))
    |> Enum.take_while(fn p -> p < 10_000_000_000 end)
    |> Enum.any?(fn p ->
      sort_digits(Integer.to_string(p)) == target
    end)
  end

  defp sort_digits(str) do
    str
    |> String.graphemes()
    |> Enum.sort()
    |> Enum.join()
  end
end
```
