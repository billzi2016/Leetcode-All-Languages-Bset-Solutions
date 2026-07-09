# 0044. Wildcard Matching

## Cpp

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.size(), m = p.size();
        int i = 0, j = 0;
        int starIdx = -1, matchIdx = -1;
        while (i < n) {
            if (j < m && (p[j] == '?' || p[j] == s[i])) {
                ++i; ++j;
            } else if (j < m && p[j] == '*') {
                starIdx = j;
                matchIdx = i;
                ++j;
            } else if (starIdx != -1) {
                j = starIdx + 1;
                ++matchIdx;
                i = matchIdx;
            } else {
                return false;
            }
        }
        while (j < m && p[j] == '*') ++j;
        return j == m;
    }
};
```

## Java

```java
class Solution {
    public boolean isMatch(String s, String p) {
        int n = s.length();
        int m = p.length();
        boolean[] prev = new boolean[m + 1];
        boolean[] cur = new boolean[m + 1];
        prev[0] = true;
        for (int j = 1; j <= m; ++j) {
            if (p.charAt(j - 1) == '*') {
                prev[j] = prev[j - 1];
            }
        }
        for (int i = 1; i <= n; ++i) {
            cur[0] = false;
            for (int j = 1; j <= m; ++j) {
                char pc = p.charAt(j - 1);
                if (pc == '*') {
                    cur[j] = cur[j - 1] || prev[j];
                } else if (pc == '?' || pc == s.charAt(i - 1)) {
                    cur[j] = prev[j - 1];
                } else {
                    cur[j] = false;
                }
            }
            boolean[] tmp = prev;
            prev = cur;
            cur = tmp;
        }
        return prev[m];
    }
}
```

## Python

```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = j = 0
        star_idx = -1
        match_i = 0
        while i < len(s):
            if j < len(p) and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                star_idx = j
                match_i = i
                j += 1
            elif star_idx != -1:
                # backtrack: use previous '*' to match one more character
                j = star_idx + 1
                match_i += 1
                i = match_i
            else:
                return False
        # consume remaining '*' in pattern
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)
```

## Python3

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        star = -1
        match = 0
        n, m = len(s), len(p)
        while i < n:
            if j < m and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            elif j < m and p[j] == '*':
                star = j
                match = i
                j += 1
            elif star != -1:
                j = star + 1
                match += 1
                i = match
            else:
                return False
        while j < m and p[j] == '*':
            j += 1
        return j == m
```

## C

```c
#include <stdbool.h>

bool isMatch(char* s, char* p) {
    int i = 0, j = 0;
    int starIdx = -1;
    int matchIdx = 0;

    while (s[i] != '\0') {
        if (p[j] == s[i] || p[j] == '?') {
            i++;
            j++;
        } else if (p[j] == '*') {
            starIdx = j;
            matchIdx = i;
            j++; // consider '*' matches empty sequence for now
        } else if (starIdx != -1) {
            // backtrack: let previous '*' match one more character
            j = starIdx + 1;
            matchIdx++;
            i = matchIdx;
        } else {
            return false;
        }
    }

    // skip remaining '*' in pattern
    while (p[j] == '*') {
        j++;
    }

    return p[j] == '\0';
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsMatch(string s, string p)
    {
        int sLen = s.Length, pLen = p.Length;
        int sIdx = 0, pIdx = 0;
        int starIdx = -1, match = 0;

        while (sIdx < sLen)
        {
            if (pIdx < pLen && (p[pIdx] == '?' || p[pIdx] == s[sIdx]))
            {
                sIdx++;
                pIdx++;
            }
            else if (pIdx < pLen && p[pIdx] == '*')
            {
                starIdx = pIdx;
                match = sIdx;
                pIdx++;
            }
            else if (starIdx != -1)
            {
                pIdx = starIdx + 1;
                match++;
                sIdx = match;
            }
            else
            {
                return false;
            }
        }

        while (pIdx < pLen && p[pIdx] == '*')
        {
            pIdx++;
        }

        return pIdx == pLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    let i = 0, j = 0;
    let starIdx = -1, matchIdx = 0;

    while (i < s.length) {
        if (j < p.length && (p[j] === '?' || p[j] === s[i])) {
            i++;
            j++;
        } else if (j < p.length && p[j] === '*') {
            starIdx = j;
            matchIdx = i;
            j++; // treat * as matching empty sequence for now
        } else if (starIdx !== -1) {
            // backtrack: let * consume one more character
            j = starIdx + 1;
            matchIdx++;
            i = matchIdx;
        } else {
            return false;
        }
    }

    // skip remaining '*' in pattern
    while (j < p.length && p[j] === '*') {
        j++;
    }

    return j === p.length;
};
```

## Typescript

```typescript
function isMatch(s: string, p: string): boolean {
    let i = 0; // index in s
    let j = 0; // index in p
    let starIdx = -1; // last position of '*' in p
    let match = 0;   // position in s corresponding to the character after the matched '*'

    while (i < s.length) {
        if (j < p.length && (p[j] === '?' || p[j] === s[i])) {
            i++;
            j++;
        } else if (j < p.length && p[j] === '*') {
            starIdx = j;
            match = i;
            j++; // treat '*' as matching empty sequence for now
        } else if (starIdx !== -1) {
            // backtrack: let the previous '*' consume one more character
            j = starIdx + 1;
            match++;
            i = match;
        } else {
            return false;
        }
    }

    // skip remaining '*' in pattern
    while (j < p.length && p[j] === '*') {
        j++;
    }

    return j === p.length;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $p
     * @return Boolean
     */
    function isMatch($s, $p) {
        $n = strlen($s);
        $m = strlen($p);

        // dp[j] means s[0..i) matches p[0..j)
        $dp = array_fill(0, $m + 1, false);
        $dp[0] = true;

        // Initialize for empty s
        for ($j = 1; $j <= $m; $j++) {
            if ($p[$j - 1] === '*') {
                $dp[$j] = $dp[$j - 1];
            }
        }

        for ($i = 1; $i <= $n; $i++) {
            $new = array_fill(0, $m + 1, false);
            // new[0] stays false because non‑empty s cannot match empty pattern
            for ($j = 1; $j <= $m; $j++) {
                if ($p[$j - 1] === '*') {
                    // '*' matches empty (new[j-1]) or one more char (dp[j])
                    $new[$j] = $new[$j - 1] || $dp[$j];
                } else {
                    $match = ($p[$j - 1] === $s[$i - 1] || $p[$j - 1] === '?');
                    $new[$j] = $match && $dp[$j - 1];
                }
            }
            $dp = $new;
        }

        return $dp[$m];
    }
}
```

## Swift

```swift
class Solution {
    func isMatch(_ s: String, _ p: String) -> Bool {
        let sArr = Array(s)
        let pArr = Array(p)
        var i = 0
        var j = 0
        var starIdx = -1
        var iIdx = -1
        
        while i < sArr.count {
            if j < pArr.count && (pArr[j] == "?" || pArr[j] == sArr[i]) {
                i += 1
                j += 1
            } else if j < pArr.count && pArr[j] == "*" {
                starIdx = j
                iIdx = i
                j += 1
            } else if starIdx != -1 {
                j = starIdx + 1
                iIdx += 1
                i = iIdx
            } else {
                return false
            }
        }
        
        while j < pArr.count && pArr[j] == "*" {
            j += 1
        }
        return j == pArr.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isMatch(s: String, p: String): Boolean {
        var i = 0
        var j = 0
        var starIdx = -1
        var iIdx = -1
        val n = s.length
        val m = p.length
        while (i < n) {
            if (j < m && (p[j] == '?' || p[j] == s[i])) {
                i++
                j++
            } else if (j < m && p[j] == '*') {
                starIdx = j
                iIdx = i
                j++
            } else if (starIdx != -1) {
                j = starIdx + 1
                iIdx++
                i = iIdx
            } else {
                return false
            }
        }
        while (j < m && p[j] == '*') {
            j++
        }
        return j == m
    }
}
```

## Dart

```dart
class Solution {
  bool isMatch(String s, String p) {
    int i = 0, j = 0;
    int starIdx = -1;
    int match = 0;

    while (i < s.length) {
      if (j < p.length && (p[j] == '?' || p[j] == s[i])) {
        i++;
        j++;
      } else if (j < p.length && p[j] == '*') {
        starIdx = j;
        match = i;
        j++;
      } else if (starIdx != -1) {
        j = starIdx + 1;
        match++;
        i = match;
      } else {
        return false;
      }
    }

    while (j < p.length && p[j] == '*') {
      j++;
    }

    return j == p.length;
  }
}
```

## Golang

```go
func isMatch(s string, p string) bool {
    i, j := 0, 0
    starIdx, iIdx := -1, -1
    n, m := len(s), len(p)

    for i < n {
        if j < m && (p[j] == s[i] || p[j] == '?') {
            i++
            j++
        } else if j < m && p[j] == '*' {
            starIdx = j
            iIdx = i
            j++
        } else if starIdx != -1 {
            j = starIdx + 1
            iIdx++
            i = iIdx
        } else {
            return false
        }
    }

    for j < m && p[j] == '*' {
        j++
    }
    return j == m
}
```

## Ruby

```ruby
def is_match(s, p)
  i = 0
  j = 0
  star_idx = -1
  s_tmp_idx = -1
  s_len = s.length
  p_len = p.length
  q_code = '?'.ord
  star_code = '*'.ord

  while i < s_len
    if j < p_len && (p.getbyte(j) == s.getbyte(i) || p.getbyte(j) == q_code)
      i += 1
      j += 1
    elsif j < p_len && p.getbyte(j) == star_code
      star_idx = j
      s_tmp_idx = i
      j += 1
    elsif star_idx != -1
      j = star_idx + 1
      s_tmp_idx += 1
      i = s_tmp_idx
    else
      return false
    end
  end

  while j < p_len && p.getbyte(j) == star_code
    j += 1
  end

  j == p_len
end
```

## Scala

```scala
object Solution {
    def isMatch(s: String, p: String): Boolean = {
        val n = s.length
        val m = p.length
        var i = 0          // index for s
        var j = 0          // index for p
        var starIdx = -1   // most recent '*' position in p
        var iTmp = -1      // position in s corresponding to the character after the last matched '*'

        while (i < n) {
            if (j < m && (p.charAt(j) == '?' || p.charAt(j) == s.charAt(i))) {
                i += 1
                j += 1
            } else if (j < m && p.charAt(j) == '*') {
                starIdx = j
                iTmp = i
                j += 1
            } else if (starIdx != -1) {
                // backtrack: let '*' match one more character
                j = starIdx + 1
                iTmp += 1
                i = iTmp
            } else {
                return false
            }
        }

        while (j < m && p.charAt(j) == '*') {
            j += 1
        }

        j == m
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_match(s: String, p: String) -> bool {
        let s_bytes = s.as_bytes();
        let p_bytes = p.as_bytes();
        let (mut i, mut j) = (0usize, 0usize);
        let (mut star_idx, mut match_idx) = (None::<usize>, 0usize);

        while i < s_bytes.len() {
            if j < p_bytes.len()
                && (p_bytes[j] == b'?' || p_bytes[j] == s_bytes[i])
            {
                i += 1;
                j += 1;
            } else if j < p_bytes.len() && p_bytes[j] == b'*' {
                star_idx = Some(j);
                match_idx = i;
                j += 1; // treat '*' as matching empty sequence for now
            } else if let Some(star) = star_idx {
                // backtrack: let previous '*' consume one more character
                j = star + 1;
                match_idx += 1;
                i = match_idx;
            } else {
                return false;
            }
        }

        // skip remaining '*' in pattern
        while j < p_bytes.len() && p_bytes[j] == b'*' {
            j += 1;
        }

        j == p_bytes.len()
    }
}
```

## Racket

```racket
(define/contract (is-match s p)
  (-> string? string? boolean?)
  (let* ((n (string-length s))
         (m (string-length p))
         (init-dp (make-vector (+ m 1) #f)))
    (vector-set! init-dp 0 #t)
    ;; first row: pattern vs empty string
    (for ([j (in-range 1 (+ m 1))])
      (let ((pc (string-ref p (sub1 j))))
        (if (char=? pc #\*)
            (vector-set! init-dp j (vector-ref init-dp (sub1 j)))
            (vector-set! init-dp j #f))))
    ;; DP over characters of s
    (let loop ((i 1) (prev init-dp))
      (if (> i n)
          (vector-ref prev m)
          (let ((curr (make-vector (+ m 1) #f)))
            (vector-set! curr 0 #f)
            (for ([j (in-range 1 (+ m 1))])
              (let* ((pc (string-ref p (sub1 j)))
                     (val
                      (cond
                        [(char=? pc #\*)
                         (or (vector-ref curr (sub1 j))
                             (vector-ref prev j))]
                        [(or (char=? pc #\?)
                             (char=? pc (string-ref s (sub1 i))))
                         (vector-ref prev (sub1 j))]
                        [else #f])))
                (vector-set! curr j val)))
            (loop (+ i 1) curr))))))
```

## Erlang

```erlang
-spec is_match(S :: unicode:unicode_binary(), P :: unicode:unicode_binary()) -> boolean().
is_match(S, P) ->
    loop(S, P, 0, 0, -1, 0).

loop(_S, _P, I, J, _StarIdx, _IStar) when I == byte_size(_S), J == byte_size(_P) ->
    true;
loop(S, P, I, J, StarIdx, IStar) ->
    LenS = byte_size(S),
    LenP = byte_size(P),
    case {I < LenS, J < LenP} of
        {true, true} ->
            CharS = binary:at(S, I),
            CharP = binary:at(P, J),
            if CharP == $* ->
                    %% record position of '*', move pattern pointer
                    loop(S, P, I, J + 1, J, I);
               CharP == $? orelse CharP == CharS ->
                    %% direct match or '?'
                    loop(S, P, I + 1, J + 1, StarIdx, IStar);
               true ->
                    if StarIdx =/= -1 ->
                           NewIStar = IStar + 1,
                           %% backtrack: use previous '*', consume one more char from S
                           loop(S, P, NewIStar, StarIdx + 1, StarIdx, NewIStar);
                       true ->
                           false
                    end
            end;
        {true, false} ->
            %% pattern exhausted but string remains
            if StarIdx =/= -1 ->
                   NewIStar = IStar + 1,
                   loop(S, P, NewIStar, StarIdx + 1, StarIdx, NewIStar);
               true ->
                   false
            end;
        {false, true} ->
            %% string exhausted; remaining pattern must be all '*'
            is_all_stars(P, J);
        {false, false} ->
            true
    end.

is_all_stars(_P, J) when J >= byte_size(_P) -> true;
is_all_stars(P, J) ->
    case binary:at(P, J) of
        $* -> is_all_stars(P, J + 1);
        _  -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_match(String.t(), String.t()) :: boolean()
  def is_match(s, p) do
    s_len = byte_size(s)
    p_len = byte_size(p)
    match(s, p, s_len, p_len, 0, 0, -1, -1)
  end

  # Both string and pattern consumed
  defp match(_s, _p, s_len, p_len, i, j, _star_idx, _i_idx) when i == s_len and j == p_len do
    true
  end

  # String consumed: remaining pattern must be all '*'
  defp match(s, p, s_len, p_len, i, j, _star_idx, _i_idx) when i == s_len do
    all_stars?(p, j, p_len)
  end

  # Pattern consumed but string remains: try to use previous '*'
  defp match(s, p, s_len, p_len, i, j, star_idx, i_idx) when j == p_len do
    if star_idx != -1 do
      match(s, p, s_len, p_len, i_idx + 1, star_idx + 1, star_idx, i_idx + 1)
    else
      false
    end
  end

  # General case
  defp match(s, p, s_len, p_len, i, j, star_idx, i_idx) do
    pc = :binary.at(p, j)

    cond do
      pc == ?* ->
        # Record position of '*', keep string index unchanged
        match(s, p, s_len, p_len, i, j + 1, j, i)

      true ->
        sc = :binary.at(s, i)

        if pc == ?? or sc == pc do
          match(s, p, s_len, p_len, i + 1, j + 1, star_idx, i_idx)
        else
          if star_idx != -1 do
            # Mismatch: backtrack to last '*', consume one more char from string
            match(s, p, s_len, p_len, i_idx + 1, star_idx + 1, star_idx, i_idx + 1)
          else
            false
          end
        end
    end
  end

  defp all_stars?(_p, idx, len) when idx >= len, do: true

  defp all_stars?(p, idx, len) do
    case :binary.at(p, idx) do
      ?* -> all_stars?(p, idx + 1, len)
      _ -> false
    end
  end
end
```
