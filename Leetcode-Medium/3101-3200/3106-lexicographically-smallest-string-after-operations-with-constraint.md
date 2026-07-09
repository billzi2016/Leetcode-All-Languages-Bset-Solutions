# 3106. Lexicographically Smallest String After Operations With Constraint

## Cpp

```cpp
class Solution {
public:
    string getSmallestString(string s, int k) {
        int n = s.size();
        string t(n, 'a');
        int used = 0;
        for (int i = 0; i < n; ++i) {
            for (char c = 'a'; c <= 'z'; ++c) {
                int diff = abs(s[i] - c);
                if (diff > 13) diff = 26 - diff;
                if (used + diff <= k) {
                    t[i] = c;
                    used += diff;
                    break;
                }
            }
        }
        return t;
    }
};
```

## Java

```java
class Solution {
    public String getSmallestString(String s, int k) {
        StringBuilder sb = new StringBuilder();
        int used = 0;
        for (int i = 0; i < s.length(); i++) {
            char original = s.charAt(i);
            for (char c = 'a'; c <= 'z'; c++) {
                int diff = Math.abs(original - c);
                int dist = Math.min(diff, 26 - diff);
                if (used + dist <= k) {
                    sb.append(c);
                    used += dist;
                    break;
                }
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def getSmallestString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def circ_dist(a, b):
            diff = abs(ord(a) - ord(b))
            return min(diff, 26 - diff)

        res = []
        remaining = k
        for ch in s:
            for c in map(chr, range(ord('a'), ord('z') + 1)):
                d = circ_dist(ch, c)
                if d <= remaining:
                    res.append(c)
                    remaining -= d
                    break
        return ''.join(res)
```

## Python3

```python
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def dist(a: str, b: str) -> int:
            d = abs(ord(a) - ord(b))
            return min(d, 26 - d)

        res = []
        remaining = k
        for ch in s:
            for c_ord in range(ord('a'), ord('z') + 1):
                c = chr(c_ord)
                d = dist(ch, c)
                if d <= remaining:
                    res.append(c)
                    remaining -= d
                    break
        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int letterDist(char a, char b) {
    int diff = abs(a - b);
    return diff < 26 - diff ? diff : 26 - diff;
}

char* getSmallestString(char* s, int k) {
    int n = strlen(s);
    char *t = (char*)malloc(n + 1);
    for (int i = 0; i < n; ++i) {
        for (char c = 'a'; c <= 'z'; ++c) {
            int d = letterDist(s[i], c);
            if (d <= k) {
                t[i] = c;
                k -= d;
                break;
            }
        }
    }
    t[n] = '\0';
    return t;
}
```

## Csharp

```csharp
public class Solution
{
    public string GetSmallestString(string s, int k)
    {
        char[] result = new char[s.Length];
        int remaining = k;
        for (int i = 0; i < s.Length; i++)
        {
            for (char c = 'a'; c <= 'z'; c++)
            {
                int d = Distance(s[i], c);
                if (d <= remaining)
                {
                    result[i] = c;
                    remaining -= d;
                    break;
                }
            }
        }
        return new string(result);
    }

    private int Distance(char a, char b)
    {
        int diff = Math.Abs(a - b);
        return Math.Min(diff, 26 - diff);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var getSmallestString = function(s, k) {
    const n = s.length;
    let remaining = k;
    const result = [];
    for (let i = 0; i < n; i++) {
        const origCode = s.charCodeAt(i);
        for (let c = 97; c <= 122; c++) { // 'a' to 'z'
            const diff = Math.abs(origCode - c);
            const cost = Math.min(diff, 26 - diff);
            if (cost <= remaining) {
                result.push(String.fromCharCode(c));
                remaining -= cost;
                break;
            }
        }
    }
    return result.join('');
};
```

## Typescript

```typescript
function getSmallestString(s: string, k: number): string {
    const n = s.length;
    let remaining = k;
    const result: string[] = [];
    for (let i = 0; i < n; i++) {
        const origCode = s.charCodeAt(i);
        for (let c = 97; c <= 122; c++) { // 'a' to 'z'
            const diff = Math.abs(origCode - c);
            const dist = Math.min(diff, 26 - diff);
            if (dist <= remaining) {
                result.push(String.fromCharCode(c));
                remaining -= dist;
                break;
            }
        }
    }
    return result.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function getSmallestString($s, $k) {
        $rem = $k;
        $n = strlen($s);
        $res = '';
        for ($i = 0; $i < $n; $i++) {
            $orig = ord($s[$i]) - ord('a');
            for ($c = 0; $c < 26; $c++) {
                $diff = abs($orig - $c);
                $dist = min($diff, 26 - $diff);
                if ($dist <= $rem) {
                    $res .= chr(ord('a') + $c);
                    $rem -= $dist;
                    break;
                }
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func getSmallestString(_ s: String, _ k: Int) -> String {
        var remaining = k
        var result = ""
        let bytes = Array(s.utf8)
        for b in bytes {
            for cand in 97...122 { // 'a' to 'z'
                let diff = abs(Int(b) - cand)
                let dist = min(diff, 26 - diff)
                if dist <= remaining {
                    result.append(Character(UnicodeScalar(cand)!))
                    remaining -= dist
                    break
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getSmallestString(s: String, k: Int): String {
        var remaining = k
        val sb = StringBuilder()
        for (orig in s) {
            var chosen = orig
            for (c in 'a'..'z') {
                val d = distance(orig, c)
                if (d <= remaining) {
                    chosen = c
                    remaining -= d
                    break
                }
            }
            sb.append(chosen)
        }
        return sb.toString()
    }

    private fun distance(a: Char, b: Char): Int {
        val diff = kotlin.math.abs(a.code - b.code)
        return minOf(diff, 26 - diff)
    }
}
```

## Dart

```dart
class Solution {
  String getSmallestString(String s, int k) {
    const int aCode = 97; // 'a'.codeUnitAt(0)
    const int zCode = 122; // 'z'.codeUnitAt(0)
    List<int> origCodes = s.codeUnits;
    StringBuffer result = StringBuffer();

    for (int code in origCodes) {
      for (int cand = aCode; cand <= zCode; cand++) {
        int diff = (code - cand).abs();
        int dist = diff < 26 - diff ? diff : 26 - diff;
        if (dist <= k) {
          result.writeCharCode(cand);
          k -= dist;
          break;
        }
      }
    }

    return result.toString();
  }
}
```

## Golang

```go
func getSmallestString(s string, k int) string {
    n := len(s)
    res := make([]byte, n)
    for i := 0; i < n; i++ {
        orig := s[i]
        for ch := byte('a'); ch <= 'z'; ch++ {
            diff := int(ch - orig)
            if diff < 0 {
                diff += 26
            }
            d := diff
            if 26-diff < d {
                d = 26 - diff
            }
            if d <= k {
                res[i] = ch
                k -= d
                break
            }
        }
    }
    return string(res)
}
```

## Ruby

```ruby
def circular_distance(a, b)
  diff = (a.ord - b.ord).abs
  diff > 13 ? 26 - diff : diff
end

def get_smallest_string(s, k)
  remaining = k
  result = []
  s.each_char do |ch|
    ('a'..'z').each do |c|
      d = circular_distance(ch, c)
      if d <= remaining
        result << c
        remaining -= d
        break
      end
    end
  end
  result.join
end
```

## Scala

```scala
object Solution {
    def getSmallestString(s: String, k: Int): String = {
        var remaining = k
        val n = s.length
        val res = new Array[Char](n)
        for (i <- 0 until n) {
            val orig = s.charAt(i)
            var chosen = orig
            var costChosen = 0
            var ch = 'a'
            while (ch <= 'z') {
                val diff = Math.abs(orig - ch)
                val cost = Math.min(diff, 26 - diff)
                if (cost <= remaining) {
                    chosen = ch
                    costChosen = cost
                    // found the smallest possible character
                    break
                }
                ch = (ch + 1).toChar
            }
            res(i) = chosen
            remaining -= costChosen
        }
        new String(res)
    }

    // Helper to emulate break since Scala doesn't have built-in break without import
    private def break: Nothing = throw new scala.util.control.ControlThrowable {}
    
    // Wrap the while loop with try-catch to handle break
    {
        import scala.util.control.Exception._
        // Redefine getSmallestString to use break handling
        def getSmallestString(s: String, k: Int): String = {
            var remaining = k
            val n = s.length
            val res = new Array[Char](n)
            for (i <- 0 until n) {
                val orig = s.charAt(i)
                var chosen = orig
                var costChosen = 0
                try {
                    var ch = 'a'
                    while (ch <= 'z') {
                        val diff = Math.abs(orig - ch)
                        val cost = Math.min(diff, 26 - diff)
                        if (cost <= remaining) {
                            chosen = ch
                            costChosen = cost
                            throw new scala.util.control.ControlThrowable {}
                        }
                        ch = (ch + 1).toChar
                    }
                } catch {
                    case _: scala.util.control.ControlThrowable => // break
                }
                res(i) = chosen
                remaining -= costChosen
            }
            new String(res)
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_smallest_string(s: String, k: i32) -> String {
        let mut remaining = k;
        let mut res: Vec<u8> = Vec::with_capacity(s.len());
        for ch in s.bytes() {
            for cand in b'a'..=b'z' {
                let diff = if ch > cand { ch - cand } else { cand - ch };
                let cost = std::cmp::min(diff as i32, 26 - diff as i32);
                if cost <= remaining {
                    res.push(cand);
                    remaining -= cost;
                    break;
                }
            }
        }
        String::from_utf8(res).unwrap()
    }
}
```

## Racket

```racket
(define (char-dist c1 c2)
  (let* ([diff (abs (- (char->integer c1) (char->integer c2)))])
    (min diff (- 26 diff))))

(define (choose-char orig used k)
  (let loop ((code (char->integer #\a)))
    (if (> code (char->integer #\z))
        (values orig 0) ; should never happen because original always fits
        (let* ([ch (integer->char code)]
               [d (char-dist orig ch)])
          (if (<= (+ used d) k)
              (values ch d)
              (loop (+ code 1)))))))

(define/contract (get-smallest-string s k)
  (-> string? exact-integer? string?)
  (let loop ((i 0) (used 0) (acc '()))
    (if (= i (string-length s))
        (list->string (reverse acc))
        (let* ([orig (string-ref s i)]
               [values (call-with-values
                         (lambda () (choose-char orig used k))
                         list)])
          (define chosen-char (first values))
          (define cost (second values))
          (loop (+ i 1) (+ used cost) (cons chosen-char acc))))))
```

## Erlang

```erlang
-spec get_smallest_string(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
get_smallest_string(S, K) ->
    CharList = binary_to_list(S),
    {RevRes, _} = lists:foldl(
        fun(C, {Acc, RemK}) ->
            Letter = find_letter(C, RemK),
            NewRemK = RemK - dist(C, Letter),
            {[Letter | Acc], NewRemK}
        end,
        {[], K},
        CharList
    ),
    list_to_binary(lists:reverse(RevRes)).

%% Find the smallest letter (as integer code) whose cyclic distance to C does not exceed RemK.
-spec find_letter(integer(), integer()) -> integer().
find_letter(C, RemK) ->
    find_letter_loop(C, RemK, $a).

-spec find_letter_loop(integer(), integer(), integer()) -> integer().
find_letter_loop(_C, _RemK, L) when L > $z ->
    $z; % should never reach here because original character always fits
find_letter_loop(C, RemK, L) ->
    D = dist(C, L),
    if
        D =< RemK -> L;
        true -> find_letter_loop(C, RemK, L + 1)
    end.

%% Cyclic distance on the alphabet (a..z).
-spec dist(integer(), integer()) -> integer().
dist(C1, C2) ->
    Diff = abs(C1 - C2),
    case Diff > 13 of
        true -> 26 - Diff;
        false -> Diff
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_smallest_string(s :: String.t(), k :: integer()) :: String.t()
  def get_smallest_string(s, k) do
    {chars_rev, _} =
      s
      |> String.to_charlist()
      |> Enum.reduce({[], k}, fn ch, {acc, rem_k} ->
        chosen =
          Enum.find(?a..?z, fn cand ->
            d = distance(ch, cand)
            d <= rem_k
          end)

        d = distance(ch, chosen)
        {[chosen | acc], rem_k - d}
      end)

    chars_rev
    |> Enum.reverse()
    |> List.to_string()
  end

  defp distance(a, b) do
    diff = abs(a - b)
    min(diff, 26 - diff)
  end
end
```
