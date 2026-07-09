# 3029. Minimum Time to Revert Word to Initial State I

## Cpp

```cpp
class Solution {
public:
    int minimumTimeToInitialState(string word, int k) {
        int n = word.size();
        // Check for t where some original suffix remains and matches prefix
        for (int t = 1; t * k <= n; ++t) {
            int len = n - t * k; // length of remaining suffix/prefix
            if (word.substr(t * k, len) == word.substr(0, len))
                return t;
        }
        // Otherwise we need to overwrite the whole string
        return (n + k - 1) / k; // ceil(n/k)
    }
};
```

## Java

```java
class Solution {
    public int minimumTimeToInitialState(String word, int k) {
        int n = word.length();
        for (int t = 1; ; t++) {
            int d = t * k;
            if (d < n) {
                boolean ok = true;
                for (int i = 0; i < n - d; i++) {
                    if (word.charAt(i) != word.charAt(i + d)) {
                        ok = false;
                        break;
                    }
                }
                if (ok) return t;
            } else {
                return t;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def minimumTimeToInitialState(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        n = len(word)
        for t in range(1, n + 2):  # enough upper bound
            removed = t * k
            if removed >= n:
                return t
            L = n - removed
            if word[:L] == word[-L:]:
                return t
        return n  # fallback, should never reach here
```

## Python3

```python
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        max_t = n // k
        for t in range(1, max_t + 1):
            remain = n - t * k
            if word[:remain] == word[t * k:]:
                return t
        # If no overlap works, need enough steps to overwrite the whole string
        return (n + k - 1) // k
```

## C

```c
int minimumTimeToInitialState(char* word, int k) {
    int n = 0;
    while (word[n] != '\0') ++n;
    for (int L = n - 1; L >= 0; --L) {
        // check if prefix of length L equals suffix of length L
        int ok = 1;
        for (int i = 0; i < L; ++i) {
            if (word[i] != word[n - L + i]) { ok = 0; break; }
        }
        if (ok && ((n - L) % k == 0)) {
            return (n - L) / k;
        }
    }
    // fallback, should never reach because L=0 always works
    return n / k + (n % k != 0);
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumTimeToInitialState(string word, int k) {
        int n = word.Length;
        for (int t = 1; ; ++t) {
            long mLong = (long)t * k;
            if (mLong > n) break;
            int m = (int)mLong;
            int L = n - m;
            bool ok = true;
            for (int i = 0; i < L; ++i) {
                if (word[i] != word[m + i]) {
                    ok = false;
                    break;
                }
            }
            if (ok) return t;
        }
        return n / Gcd(n, k);
    }

    private int Gcd(int a, int b) {
        while (b != 0) {
            int tmp = a % b;
            a = b;
            b = tmp;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var minimumTimeToInitialState = function(word, k) {
    const n = word.length;
    for (let t = 1; ; ++t) {
        const removed = t * k;
        if (removed >= n) return t;
        const rem = n - removed;
        if (word.slice(0, rem) === word.slice(n - rem)) return t;
    }
};
```

## Typescript

```typescript
function minimumTimeToInitialState(word: string, k: number): number {
    const n = word.length;
    for (let L = n - 1; L >= 0; --L) {
        if (word.substring(0, L) === word.substring(n - L)) {
            const diff = n - L;
            if (diff % k === 0) return diff / k;
        }
    }
    return Math.ceil(n / k);
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @param Integer $k
     * @return Integer
     */
    function minimumTimeToInitialState($word, $k) {
        $n = strlen($word);
        $maxT = intdiv($n + $k - 1, $k); // ceil(n / k)
        for ($t = 1; $t <= $maxT; $t++) {
            $d = $t * $k;
            if ($d >= $n) {
                return $t;
            }
            $suffix = substr($word, $d);
            $prefix = substr($word, 0, $n - $d);
            if ($suffix === $prefix) {
                return $t;
            }
        }
        return $maxT;
    }
}
```

## Swift

```swift
class Solution {
    func minimumTimeToInitialState(_ word: String, _ k: Int) -> Int {
        let chars = Array(word)
        let n = chars.count
        var d = k
        while d <= n {
            let len = n - d
            if len == 0 || Array(chars[d..<n]) == Array(chars[0..<len]) {
                return d / k
            }
            d += k
        }
        // No suitable border found within the word length.
        return (n + k - 1) / k
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumTimeToInitialState(word: String, k: Int): Int {
        val n = word.length
        for (l in n - 1 downTo 0) {
            if (word.substring(0, l) == word.substring(n - l)) {
                if ((n - l) % k == 0) return (n - l) / k
            }
        }
        return (n + k - 1) / k
    }
}
```

## Dart

```dart
class Solution {
  int minimumTimeToInitialState(String word, int k) {
    int n = word.length;
    int maxT = (n + k - 1) ~/ k; // ceil(n / k)
    for (int t = 1; t < maxT; ++t) {
      int removed = k * t;
      if (word.substring(removed) == word.substring(0, n - removed)) {
        return t;
      }
    }
    return maxT;
  }
}
```

## Golang

```go
func minimumTimeToInitialState(word string, k int) int {
    n := len(word)
    // Compute prefix function (KMP failure array)
    pi := make([]int, n)
    for i := 1; i < n; i++ {
        j := pi[i-1]
        for j > 0 && word[i] != word[j] {
            j = pi[j-1]
        }
        if word[i] == word[j] {
            j++
        }
        pi[i] = j
    }

    // Find the longest border length L where (n-L) is divisible by k
    l := n
    for {
        if l == 0 {
            break
        }
        l = pi[l-1] // next shorter border
        if (n-l)%k == 0 && l != n {
            return (n - l) / k
        }
    }

    // If no suitable border, need enough steps to remove all original characters
    if n%k == 0 {
        return n / k
    }
    return (n + k - 1) / k
}
```

## Ruby

```ruby
def minimum_time_to_initial_state(word, k)
  n = word.length
  max_t = (n + k - 1) / k
  (1..max_t).each do |t|
    l = n - t * k
    if l >= 0
      return t if word[0, l] == word[t * k, l]
    else
      break
    end
  end
  max_t
end
```

## Scala

```scala
object Solution {
    def minimumTimeToInitialState(word: String, k: Int): Int = {
        val n = word.length
        // helper gcd
        def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)
        var answer = n / gcd(n, k) // fallback using pure rotation

        // search for the largest border length L (< n) satisfying condition
        var found = false
        var L = n - 1
        while (L >= 0 && !found) {
            if (word.substring(0, L) == word.substring(n - L)) {
                val diff = n - L
                if (diff % k == 0) {
                    answer = diff / k
                    found = true
                }
            }
            L -= 1
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_time_to_initial_state(word: String, k: i32) -> i32 {
        let bytes = word.as_bytes();
        let n = bytes.len();
        let k_usize = k as usize;
        for l in (0..n).rev() {
            if &bytes[0..l] == &bytes[n - l..] && (n - l) % k_usize == 0 {
                return ((n - l) / k_usize) as i32;
            }
        }
        // According to problem constraints, this point should never be reached.
        unreachable!()
    }
}
```

## Racket

```racket
(define/contract (minimum-time-to-initial-state word k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length word))
         ;; compute all border lengths including 0 and n
         (borders (let ((tbl (make-hash)))
                    (for ([len (in-range 0 (+ n 1))])
                      (when (string=? (substring word 0 len)
                                      (substring word (- n len) n))
                        (hash-set! tbl len #t)))
                    tbl)))
    ;; search minimal t > 0
    (let loop ((t 1))
      (define m (modulo (* t k) n))          ; removed modulo n
      (define L (- n m))                     ; remaining original suffix length
      (if (hash-has-key? borders L)
          t
          (loop (+ t 1)))))))
```

## Erlang

```erlang
-spec minimum_time_to_initial_state(Word :: unicode:unicode_binary(), K :: integer()) -> integer().
minimum_time_to_initial_state(Word, K) ->
    N = byte_size(Word),
    MaxT = (N + K - 1) div K,
    find(N, Word, K, 1, MaxT).

find(_N, _Word, _K, T, MaxT) when T > MaxT -> MaxT;
find(N, Word, K, T, MaxT) ->
    Removed = T * K,
    if
        Removed >= N ->
            MaxT;
        true ->
            Len = N - Removed,
            Prefix = binary:part(Word, 0, Len),
            Suffix = binary:part(Word, Removed, Len),
            case Prefix == Suffix of
                true -> T;
                false -> find(N, Word, K, T + 1, MaxT)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_time_to_initial_state(word :: String.t(), k :: integer) :: integer
  def minimum_time_to_initial_state(word, k) do
    n = String.length(word)
    bin = word

    # Find smallest i (i >=1) such that d = i*k <= n and prefix of length n-d equals suffix starting at d
    t =
      Enum.find_value(1..div(n, k), fn i ->
        d = i * k
        l = n - d

        if l > 0 do
          prefix = :binary.part(bin, 0, l)
          suffix = :binary.part(bin, d, l)

          if prefix == suffix, do: i, else: nil
        else
          nil
        end
      end)

    case t do
      nil -> div(n + k - 1, k)   # ceil(n / k)
      _ -> t
    end
  end
end
```
