# 2957. Remove Adjacent Almost-Equal Characters

## Cpp

```cpp
class Solution {
public:
    int removeAlmostEqualCharacters(string word) {
        const int INF = 1e9;
        int n = word.size();
        vector<vector<int>> dp(n, vector<int>(26, INF));
        for (int c = 0; c < 26; ++c) {
            dp[0][c] = (c != word[0] - 'a');
        }
        for (int i = 1; i < n; ++i) {
            int orig = word[i] - 'a';
            for (int c = 0; c < 26; ++c) {
                int cost = (c != orig);
                int best = INF;
                for (int p = 0; p < 26; ++p) {
                    if (abs(c - p) > 1) {
                        best = min(best, dp[i-1][p]);
                    }
                }
                dp[i][c] = best + cost;
            }
        }
        int ans = INF;
        for (int c = 0; c < 26; ++c) ans = min(ans, dp[n-1][c]);
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int removeAlmostEqualCharacters(String word) {
        int n = word.length();
        int[][] dp = new int[n][26];
        final int INF = 1_000_000;
        // Initialize first character
        for (int c = 0; c < 26; ++c) {
            dp[0][c] = (word.charAt(0) - 'a' == c) ? 0 : 1;
        }
        // DP transition
        for (int i = 1; i < n; ++i) {
            for (int c = 0; c < 26; ++c) {
                int cost = (word.charAt(i) - 'a' == c) ? 0 : 1;
                int best = INF;
                for (int p = 0; p < 26; ++p) {
                    if (Math.abs(c - p) > 1) { // not almost equal
                        if (dp[i - 1][p] < best) best = dp[i - 1][p];
                    }
                }
                dp[i][c] = cost + best;
            }
        }
        int ans = INF;
        for (int c = 0; c < 26; ++c) {
            ans = Math.min(ans, dp[n - 1][c]);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def removeAlmostEqualCharacters(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        ops = 0
        prev = None  # character after possible modifications at previous position
        
        for i in range(n):
            cur = word[i]
            if prev is not None and abs(ord(cur) - ord(prev)) <= 1:
                # need to change current character
                ops += 1
                nxt = word[i + 1] if i + 1 < n else None
                # find a replacement that is not almost equal to prev nor nxt
                for cand in (chr(c) for c in range(ord('a'), ord('z') + 1)):
                    if abs(ord(cand) - ord(prev)) > 1 and (nxt is None or abs(ord(cand) - ord(nxt)) > 1):
                        prev = cand
                        break
            else:
                prev = cur
        return ops
```

## Python3

```python
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        if not word:
            return 0
        ops = 0
        prev = word[0]
        for i in range(1, len(word)):
            if abs(ord(word[i]) - ord(prev)) <= 1:
                ops += 1
                prev = '#'
            else:
                prev = word[i]
        return ops
```

## C

```c
#include <string.h>
#include <stdlib.h>

int removeAlmostEqualCharacters(char* word) {
    int n = strlen(word);
    if (n == 0) return 0;
    int ops = 0;
    char prev = word[0];
    for (int i = 1; i < n; ++i) {
        char cur = word[i];
        if (abs(cur - prev) <= 1) {
            ++ops;
            prev = '#'; // sentinel far from any lowercase letter
        } else {
            prev = cur;
        }
    }
    return ops;
}
```

## Csharp

```csharp
public class Solution {
    public int RemoveAlmostEqualCharacters(string word) {
        int n = word.Length;
        if (n == 0) return 0;
        int ops = 0;
        char prev = word[0];
        for (int i = 1; i < n; i++) {
            char cur = word[i];
            if (Math.Abs(cur - prev) <= 1) {
                ops++;
                prev = '{'; // character after 'z', safe placeholder
            } else {
                prev = cur;
            }
        }
        return ops;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var removeAlmostEqualCharacters = function(word) {
    const n = word.length;
    if (n === 0) return 0;
    let ops = 0;
    let prev = word[0];
    for (let i = 1; i < n; ++i) {
        const cur = word[i];
        if (Math.abs(cur.charCodeAt(0) - prev.charCodeAt(0)) <= 1) {
            ++ops;
            // use a placeholder that is far from any lowercase letter
            prev = '#';
        } else {
            prev = cur;
        }
    }
    return ops;
};
```

## Typescript

```typescript
function removeAlmostEqualCharacters(word: string): number {
    const n = word.length;
    if (n <= 1) return 0;
    let operations = 0;
    let prev = word[0];
    for (let i = 1; i < n; i++) {
        const cur = word[i];
        if (Math.abs(cur.charCodeAt(0) - prev.charCodeAt(0)) <= 1) {
            operations++;
            // Use a sentinel character outside 'a'-'z' range
            prev = '{';
        } else {
            prev = cur;
        }
    }
    return operations;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function removeAlmostEqualCharacters($word) {
        $n = strlen($word);
        if ($n <= 1) return 0;
        $cnt = 0;
        $prev = $word[0];
        for ($i = 1; $i < $n; $i++) {
            $curr = $word[$i];
            if (abs(ord($curr) - ord($prev)) <= 1) {
                $cnt++;
                // change current character to a sentinel that is far from any lowercase letter
                $prev = '#';
            } else {
                $prev = $curr;
            }
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func removeAlmostEqualCharacters(_ word: String) -> Int {
        let scalars = Array(word.unicodeScalars)
        let n = scalars.count
        var w = [Int]()
        for s in scalars {
            w.append(Int(s.value - UnicodeScalar("a").value))
        }
        let INF = 1_000_000
        var dpPrev = Array(repeating: INF, count: 26)
        // initialize for first character
        for c in 0..<26 {
            dpPrev[c] = (w[0] == c) ? 0 : 1
        }
        if n == 1 { return dpPrev.min()! }
        for i in 1..<n {
            var dpCurr = Array(repeating: INF, count: 26)
            for c in 0..<26 {
                let cost = (w[i] == c) ? 0 : 1
                var best = INF
                for p in 0..<26 where abs(c - p) > 1 {
                    if dpPrev[p] < best { best = dpPrev[p] }
                }
                dpCurr[c] = cost + best
            }
            dpPrev = dpCurr
        }
        return dpPrev.min()!
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeAlmostEqualCharacters(word: String): Int {
        var operations = 0
        var prev = word[0]
        for (i in 1 until word.length) {
            val cur = word[i]
            if (isAlmostEqual(prev, cur)) {
                operations++
                // Change current character to a sentinel that never causes conflict
                prev = '#'
            } else {
                prev = cur
            }
        }
        return operations
    }

    private fun isAlmostEqual(a: Char, b: Char): Boolean {
        if (a !in 'a'..'z' || b !in 'a'..'z') return false
        val diff = kotlin.math.abs(a - b)
        return diff <= 1
    }
}
```

## Dart

```dart
class Solution {
  int removeAlmostEqualCharacters(String word) {
    int n = word.length;
    if (n == 0) return 0;
    const int sentinel = 123; // character after 'z'
    int ans = 0;
    int prev = word.codeUnitAt(0);
    for (int i = 1; i < n; ++i) {
      int cur = word.codeUnitAt(i);
      if ((cur - prev).abs() <= 1) {
        ans++;
        prev = sentinel;
      } else {
        prev = cur;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func removeAlmostEqualCharacters(word string) int {
    n := len(word)
    if n == 0 {
        return 0
    }
    ans := 0
    prev := word[0]
    for i := 1; i < n; i++ {
        cur := word[i]
        diff := int(prev) - int(cur)
        if diff < 0 {
            diff = -diff
        }
        if diff <= 1 {
            ans++
            // Use a sentinel character that is not adjacent to any lowercase letter.
            prev = '{'
        } else {
            prev = cur
        }
    }
    return ans
}
```

## Ruby

```ruby
def remove_almost_equal_characters(word)
  ans = 0
  prev = nil
  word.each_char do |c|
    if !prev.nil? && (c.ord - prev.ord).abs <= 1
      ans += 1
      prev = nil
    else
      prev = c
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def removeAlmostEqualCharacters(word: String): Int = {
        var ops = 0
        var prev: Char = word.charAt(0)
        for (i <- 1 until word.length) {
            val cur = word.charAt(i)
            if (math.abs(prev - cur) <= 1) {
                ops += 1
                prev = '#'
            } else {
                prev = cur
            }
        }
        ops
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_almost_equal_characters(word: String) -> i32 {
        let bytes = word.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return 0;
        }
        const SENTINEL: u8 = b'*'; // a character far from any lowercase letter
        let mut ans = 0;
        let mut prev = bytes[0];
        for i in 1..n {
            let cur = bytes[i];
            if (cur as i32 - prev as i32).abs() <= 1 {
                ans += 1;
                prev = SENTINEL;
            } else {
                prev = cur;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (remove-almost-equal-characters word)
  (-> string? exact-integer?)
  (let loop ((chars (string->list word))
             (prev #\space) ; sentinel not a lowercase letter
             (cnt 0))
    (if (null? chars)
        cnt
        (let ((c (car chars)))
          (if (<= (abs (- (char->integer prev) (char->integer c))) 1)
              (loop (cdr chars) #\space (+ cnt 1)) ; change current char
              (loop (cdr chars) c cnt))))))
```

## Erlang

```erlang
-module(solution).
-export([remove_almost_equal_characters/1]).

remove_almost_equal_characters(Word) ->
    CharCodes = unicode:characters_to_list(Word),
    OrigIndices = [C - $a || C <- CharCodes],
    case OrigIndices of
        [] -> 0;
        [First | Rest] ->
            DP0 = [if C == First -> 0; true -> 1 end || C <- lists:seq(0, 25)],
            FinalDP = lists:foldl(
                fun(CurOrig, PrevDP) ->
                    [ (if C == CurOrig -> 0; true -> 1 end) + min_allowed(C, PrevDP)
                      || C <- lists:seq(0, 25)]
                end,
                DP0,
                Rest
            ),
            lists:min(FinalDP)
    end.

min_allowed(C, PrevDP) ->
    lists:foldl(
        fun({P, Val}, Min) ->
            if abs(C - P) > 1, Val < Min -> Val;
               true -> Min
            end
        end,
        1000000,
        lists:zip(lists:seq(0, 25), PrevDP)
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_almost_equal_characters(word :: String.t()) :: integer()
  def remove_almost_equal_characters(word) do
    {cnt, _} =
      word
      |> String.to_charlist()
      |> Enum.reduce({0, nil}, fn c, {cnt, prev} ->
        if not is_nil(prev) and almost_equal(prev, c) do
          {cnt + 1, ?#}
        else
          {cnt, c}
        end
      end)

    cnt
  end

  defp almost_equal(a, b) do
    diff = abs(a - b)
    diff <= 1
  end
end
```
