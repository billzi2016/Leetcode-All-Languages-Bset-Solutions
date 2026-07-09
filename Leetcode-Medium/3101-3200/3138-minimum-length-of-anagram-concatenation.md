# 3138. Minimum Length of Anagram Concatenation

## Cpp

```cpp
class Solution {
public:
    int minAnagramLength(string s) {
        int n = s.size();
        vector<int> cnt(26, 0);
        for (char ch : s) cnt[ch - 'a']++;
        int bestK = 1; // number of blocks
        for (int d = 1; d * d <= n; ++d) {
            if (n % d != 0) continue;
            int k1 = d;
            int k2 = n / d;
            auto check = [&](int k) {
                for (int c : cnt) {
                    if (c % k != 0) return false;
                }
                return true;
            };
            if (check(k1) && k1 > bestK) bestK = k1;
            if (check(k2) && k2 > bestK) bestK = k2;
        }
        return n / bestK;
    }
};
```

## Java

```java
class Solution {
    public int minAnagramLength(String s) {
        int[] cnt = new int[26];
        for (int i = 0; i < s.length(); ++i) {
            cnt[s.charAt(i) - 'a']++;
        }
        int g = 0;
        for (int c : cnt) {
            if (c > 0) {
                if (g == 0) g = c;
                else g = gcd(g, c);
            }
        }
        return s.length() / g;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def minAnagramLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        from math import gcd
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        g = 0
        for cnt in freq:
            if cnt:
                g = cnt if g == 0 else gcd(g, cnt)
        return len(s) // g
```

## Python3

```python
class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        # collect all divisors of n
        divs = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divs.append(i)
                if i != n // i:
                    divs.append(n // i)
            i += 1
        divs.sort()
        for L in divs:
            # frequency of the first block
            base = [0] * 26
            for ch in s[:L]:
                base[ord(ch) - 97] += 1
            ok = True
            for start in range(L, n, L):
                cur = [0] * 26
                segment = s[start:start + L]
                for ch in segment:
                    cur[ord(ch) - 97] += 1
                if cur != base:
                    ok = False
                    break
            if ok:
                return L
        return n
```

## C

```c
#include <string.h>

static int gcd_int(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int minAnagramLength(char* s) {
    int cnt[26] = {0};
    int n = 0;
    for (char *p = s; *p; ++p) {
        cnt[*p - 'a']++;
        n++;
    }
    int g = 0;
    for (int i = 0; i < 26; ++i) {
        if (cnt[i] > 0) {
            if (g == 0)
                g = cnt[i];
            else
                g = gcd_int(g, cnt[i]);
        }
    }
    return n / g;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinAnagramLength(string s)
    {
        int[] cnt = new int[26];
        foreach (char ch in s)
            cnt[ch - 'a']++;

        int g = 0;
        foreach (int c in cnt)
            if (c > 0)
                g = Gcd(g, c);

        return s.Length / g;
    }

    private int Gcd(int a, int b)
    {
        while (b != 0)
        {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minAnagramLength = function(s) {
    const freq = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        freq[s.charCodeAt(i) - 97]++;
    }
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    let g = 0;
    for (let cnt of freq) {
        if (cnt > 0) {
            g = g === 0 ? cnt : gcd(g, cnt);
        }
    }
    return s.length / g;
};
```

## Typescript

```typescript
function minAnagramLength(s: string): number {
    const n = s.length;
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < n; ++i) {
        cnt[s.charCodeAt(i) - 97]++;
    }

    const divisors: number[] = [];
    for (let i = 1; i * i <= n; ++i) {
        if (n % i === 0) {
            divisors.push(i);
            if (i !== n / i) divisors.push(n / i);
        }
    }
    divisors.sort((a, b) => b - a); // descending to get max k first

    for (const k of divisors) {
        let ok = true;
        for (let j = 0; j < 26; ++j) {
            if (cnt[j] % k !== 0) {
                ok = false;
                break;
            }
        }
        if (ok) return n / k;
    }

    // Fallback, should never reach because k=1 always works
    return n;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minAnagramLength($s) {
        $n = strlen($s);
        $freq = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            $freq[$idx]++;
        }

        $g = 0;
        foreach ($freq as $f) {
            if ($f > 0) {
                if ($g == 0) {
                    $g = $f;
                } else {
                    $g = $this->gcd($g, $f);
                }
            }
        }

        return intdiv($n, $g);
    }

    private function gcd(int $a, int $b): int {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }
}
```

## Swift

```swift
class Solution {
    func minAnagramLength(_ s: String) -> Int {
        let bytes = Array(s.utf8)
        let n = bytes.count
        var cnt = [Int](repeating: 0, count: 26)
        for b in bytes {
            cnt[Int(b - 97)] += 1
        }
        var divisors = [Int]()
        var i = 1
        while i * i <= n {
            if n % i == 0 {
                divisors.append(i)
                if i != n / i {
                    divisors.append(n / i)
                }
            }
            i += 1
        }
        divisors.sort()
        for L in divisors {
            let k = n / L
            var ok = true
            for c in 0..<26 {
                if cnt[c] % k != 0 {
                    ok = false
                    break
                }
            }
            if ok { return L }
        }
        return n
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minAnagramLength(s: String): Int {
        val cnt = IntArray(26)
        for (c in s) {
            cnt[c - 'a']++
        }
        var g = 0
        for (v in cnt) {
            if (v > 0) {
                g = if (g == 0) v else gcd(g, v)
            }
        }
        return s.length / g
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
  int minAnagramLength(String s) {
    int n = s.length;
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < n; ++i) {
      cnt[s.codeUnitAt(i) - 97]++;
    }
    List<int> ks = [];
    for (int i = 1; i * i <= n; ++i) {
      if (n % i == 0) {
        ks.add(i);
        int other = n ~/ i;
        if (other != i) ks.add(other);
      }
    }
    ks.sort((a, b) => b.compareTo(a)); // descending
    for (int k in ks) {
      bool ok = true;
      for (int c = 0; c < 26; ++c) {
        if (cnt[c] % k != 0) {
          ok = false;
          break;
        }
      }
      if (ok) return n ~/ k;
    }
    return n;
  }
}
```

## Golang

```go
func minAnagramLength(s string) int {
    freq := [26]int{}
    for i := 0; i < len(s); i++ {
        freq[s[i]-'a']++
    }
    g := 0
    for _, cnt := range freq[:] {
        if cnt > 0 {
            if g == 0 {
                g = cnt
            } else {
                // Euclidean algorithm
                a, b := g, cnt
                for b != 0 {
                    a, b = b, a%b
                }
                g = a
            }
        }
    }
    n := len(s)
    if g == 0 { // should not happen as s length >=1
        return n
    }
    return n / g
}
```

## Ruby

```ruby
def min_anagram_length(s)
  freq = Array.new(26, 0)
  s.each_byte { |b| freq[b - 97] += 1 }
  g = 0
  freq.each do |cnt|
    next if cnt == 0
    g = g.zero? ? cnt : g.gcd(cnt)
  end
  s.length / g
end
```

## Scala

```scala
object Solution {
    def minAnagramLength(s: String): Int = {
        val cnt = new Array[Int](26)
        s.foreach(ch => cnt(ch - 'a') += 1)
        var g = 0
        for (c <- cnt if c > 0) {
            g = if (g == 0) c else gcd(g, c)
        }
        s.length / g
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
    pub fn min_anagram_length(s: String) -> i32 {
        let mut cnt = [0i32; 26];
        for b in s.bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        let mut g = 0i32;
        for &c in cnt.iter() {
            if c > 0 {
                if g == 0 {
                    g = c;
                } else {
                    g = Self::gcd(g, c);
                }
            }
        }
        (s.len() as i32) / g
    }

    fn gcd(mut a: i32, mut b: i32) -> i32 {
        while b != 0 {
            let r = a % b;
            a = b;
            b = r;
        }
        a.abs()
    }
}
```

## Racket

```racket
(define/contract (min-anagram-length s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (counts (make-vector 26 0)))
    ;; count characters
    (for ([i (in-range n)])
      (let* ((ch (string-ref s i))
             (idx (- (char->integer ch) (char->integer #\a))))
        (vector-set! counts idx (+ (vector-ref counts idx) 1))))
    ;; predicate: all counts divisible by k
    (define (valid? k)
      (let loop ((i 0))
        (or (= i 26)
            (and (= (remainder (vector-ref counts i) k) 0)
                 (loop (+ i 1))))))
    ;; collect divisors of n
    (let* ((sqrt-n (inexact->exact (floor (sqrt n))))
           (divisors '()))
      (for ([i (in-range 1 (+ sqrt-n 1))])
        (when (= (remainder n i) 0)
          (set! divisors (cons i divisors))
          (let ((j (/ n i)))
            (unless (= i j)
              (set! divisors (cons j divisors))))))
      ;; find largest k satisfying condition
      (define maxk 1)
      (for ([k divisors])
        (when (and (> k maxk) (valid? k))
          (set! maxk k)))
      (/ n maxk))))
```

## Erlang

```erlang
-spec min_anagram_length(S :: unicode:unicode_binary()) -> integer().
min_anagram_length(S) ->
    Len = byte_size(S),
    FreqMap = count_freq(S, #{}),
    GcdVal = compute_gcd(maps:values(FreqMap)),
    Len div GcdVal.

count_freq(<<>>, Map) -> Map;
count_freq(<<C, Rest/binary>>, Map) ->
    Count = maps:get(C, Map, 0),
    count_freq(Rest, maps:put(C, Count + 1, Map)).

compute_gcd([H|T]) ->
    lists:foldl(fun(X, Acc) -> gcd(Acc, X) end, H, T).

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_anagram_length(s :: String.t()) :: integer()
  def min_anagram_length(s) do
    n = String.length(s)

    freqs =
      String.to_charlist(s)
      |> Enum.reduce(List.duplicate(0, 26), fn ch, acc ->
        idx = ch - ?a
        List.update_at(acc, idx, &(&1 + 1))
      end)

    sqrt = :math.sqrt(n) |> trunc()

    divisors =
      1..sqrt
      |> Enum.reduce([], fn i, acc ->
        if rem(n, i) == 0 do
          other = div(n, i)
          acc2 = [i | acc]
          if other != i, do: [other | acc2], else: acc2
        else
          acc
        end
      end)
      |> Enum.sort()

    Enum.find(divisors, fn len ->
      m = div(n, len)

      Enum.all?(freqs, fn f -> rem(f, m) == 0 end)
    end) || n
  end
end
```
