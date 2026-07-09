# 3407. Substring Matching Pattern

## Cpp

```cpp
class Solution {
public:
    bool hasMatch(string s, string p) {
        size_t star = p.find('*');
        string left = p.substr(0, star);
        string right = p.substr(star + 1);
        
        if (left.empty() && right.empty()) return true;
        if (left.empty()) {
            return s.find(right) != string::npos;
        }
        if (right.empty()) {
            return s.find(left) != string::npos;
        }
        
        for (size_t i = 0; i + left.size() <= s.size(); ++i) {
            if (s.compare(i, left.size(), left) == 0) {
                size_t startSearch = i + left.size();
                size_t pos = s.find(right, startSearch);
                if (pos != string::npos) return true;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean hasMatch(String s, String p) {
        int star = p.indexOf('*');
        String pre = p.substring(0, star);
        String suf = p.substring(star + 1);
        int n = s.length();
        for (int i = 0; i <= n - pre.length(); i++) {
            if (!s.startsWith(pre, i)) continue;
            int startAfterPre = i + pre.length();
            for (int j = startAfterPre; j <= n - suf.length(); j++) {
                if (s.startsWith(suf, j)) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def hasMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        star = p.find('*')
        pre = p[:star]
        suf = p[star+1:]

        # If both parts are empty, pattern is "*", which matches any substring (including empty)
        if not pre and not suf:
            return True

        # If prefix is empty, just need suffix somewhere
        if not pre:
            return suf in s

        # If suffix is empty, just need prefix somewhere
        if not suf:
            return pre in s

        n = len(s)
        lp, ls = len(pre), len(suf)

        for i in range(n - lp + 1):
            if s[i:i+lp] != pre:
                continue
            start_search = i + lp
            # Search for suffix at or after start_search
            idx = s.find(suf, start_search)
            if idx != -1:
                return True
        return False
```

## Python3

```python
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        star = p.find('*')
        pre = p[:star]
        suf = p[star + 1 :]
        n = len(s)
        min_len = len(pre) + len(suf)
        for i in range(n):
            for j in range(i + min_len, n + 1):
                sub = s[i:j]
                if (not pre or sub.startswith(pre)) and (not suf or sub.endswith(suf)):
                    return True
        return False
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool hasMatch(char* s, char* p) {
    int n = strlen(s);
    int m = strlen(p);
    int starIdx = -1;
    for (int i = 0; i < m; ++i) {
        if (p[i] == '*') { starIdx = i; break; }
    }
    int preLen = starIdx;               // length before '*'
    int sufLen = m - starIdx - 1;       // length after '*'

    // pattern is just "*"
    if (preLen == 0 && sufLen == 0) return true;

    for (int i = 0; i <= n - preLen; ++i) {
        // check prefix match
        bool okPref = true;
        for (int k = 0; k < preLen; ++k) {
            if (s[i + k] != p[k]) { okPref = false; break; }
        }
        if (!okPref) continue;

        int startSuffixMin = i + preLen;
        for (int j = startSuffixMin; j <= n - sufLen; ++j) {
            // check suffix match
            bool okSuf = true;
            for (int k = 0; k < sufLen; ++k) {
                if (s[j + k] != p[starIdx + 1 + k]) { okSuf = false; break; }
            }
            if (okSuf) return true;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool HasMatch(string s, string p) {
        int starIdx = p.IndexOf('*');
        string left = p.Substring(0, starIdx);
        string right = p.Substring(starIdx + 1);

        // Both parts empty -> pattern is "*", always matches
        if (left.Length == 0 && right.Length == 0) return true;

        // Only left part exists: need left as a substring
        if (right.Length == 0) {
            return s.Contains(left);
        }

        // Only right part exists: need right as a substring
        if (left.Length == 0) {
            return s.Contains(right);
        }

        for (int i = 0; i <= s.Length - left.Length; ++i) {
            if (!s.Substring(i, left.Length).Equals(left)) continue;
            int startSearch = i + left.Length;
            for (int j = startSearch; j <= s.Length - right.Length; ++j) {
                if (s.Substring(j, right.Length).Equals(right)) {
                    return true;
                }
            }
        }

        return false;
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
var hasMatch = function(s, p) {
    const starIdx = p.indexOf('*');
    const left = p.slice(0, starIdx);
    const right = p.slice(starIdx + 1);
    
    for (let i = 0; i <= s.length - left.length; i++) {
        if (s.substr(i, left.length) === left) {
            const afterLeft = i + left.length;
            const idxRight = s.indexOf(right, afterLeft);
            if (idxRight !== -1) {
                return true;
            }
        }
    }
    return false;
};
```

## Typescript

```typescript
function hasMatch(s: string, p: string): boolean {
    const starIdx = p.indexOf('*');
    const pre = p.slice(0, starIdx);
    const suf = p.slice(starIdx + 1);

    // Both parts empty -> always true (empty substring)
    if (pre.length === 0 && suf.length === 0) return true;

    // Only suffix needed
    if (pre.length === 0) {
        return s.includes(suf);
    }

    // Only prefix needed
    if (suf.length === 0) {
        return s.includes(pre);
    }

    const n = s.length;
    for (let i = 0; i <= n - pre.length; ++i) {
        if (s.substr(i, pre.length) !== pre) continue;
        const startSearch = i + pre.length;
        if (s.indexOf(suf, startSearch) !== -1) return true;
    }
    return false;
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
    function hasMatch($s, $p) {
        list($pref, $suf) = explode('*', $p, 2);
        $lenPref = strlen($pref);
        $lenSuf = strlen($suf);
        $n = strlen($s);

        // If both parts are empty, pattern is "*" which always matches
        if ($lenPref == 0 && $lenSuf == 0) {
            return true;
        }

        for ($i = 0; $i <= $n - $lenPref; $i++) {
            if (substr($s, $i, $lenPref) !== $pref) {
                continue;
            }
            // Position where suffix can start
            for ($j = $i + $lenPref; $j <= $n - $lenSuf; $j++) {
                if (substr($s, $j, $lenSuf) === $suf) {
                    return true;
                }
            }
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func hasMatch(_ s: String, _ p: String) -> Bool {
        let parts = p.split(separator: "*", omittingEmptySubsequences: false)
        let pre = String(parts[0])
        let suf = String(parts[1])

        let sArr = Array(s)
        let n = sArr.count
        let preArr = Array(pre)
        let sufArr = Array(suf)
        let preLen = preArr.count
        let sufLen = sufArr.count

        // pattern is just "*"
        if preLen == 0 && sufLen == 0 { return true }
        // prefix longer than s cannot match any substring
        if preLen > n { return false }

        for i in 0...n - preLen {
            var matchesPre = true
            if preLen > 0 {
                for k in 0..<preLen {
                    if sArr[i + k] != preArr[k] {
                        matchesPre = false
                        break
                    }
                }
            }
            if !matchesPre { continue }

            let afterPre = i + preLen

            // suffix empty -> always match
            if sufLen == 0 { return true }

            if afterPre > n - sufLen { continue }

            var j = afterPre
            while j <= n - sufLen {
                var matchesSuf = true
                for k in 0..<sufLen {
                    if sArr[j + k] != sufArr[k] {
                        matchesSuf = false
                        break
                    }
                }
                if matchesSuf { return true }
                j += 1
            }
        }

        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun hasMatch(s: String, p: String): Boolean {
        val star = p.indexOf('*')
        val pre = p.substring(0, star)
        val suf = p.substring(star + 1)

        if (pre.isEmpty() && suf.isEmpty()) return true
        if (pre.isEmpty()) return s.contains(suf)
        if (suf.isEmpty()) return s.contains(pre)

        var startIdx = 0
        while (true) {
            val i = s.indexOf(pre, startIdx)
            if (i == -1) break
            val afterPre = i + pre.length
            if (s.indexOf(suf, afterPre) != -1) return true
            startIdx = i + 1
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool hasMatch(String s, String p) {
    int star = p.indexOf('*');
    String pre = p.substring(0, star);
    String suf = p.substring(star + 1);
    int n = s.length;

    if (pre.isEmpty && suf.isEmpty) return true;

    for (int start = 0; start <= n - pre.length; ++start) {
      if (pre.isNotEmpty && !s.startsWith(pre, start)) continue;
      int afterPre = start + pre.length;
      if (suf.isEmpty) return true;
      for (int pos = afterPre; pos <= n - suf.length; ++pos) {
        if (s.startsWith(suf, pos)) return true;
      }
    }
    return false;
  }
}
```

## Golang

```go
import "strings"

func hasMatch(s string, p string) bool {
	star := strings.Index(p, "*")
	pre := p[:star]
	suf := p[star+1:]

	if len(pre) == 0 && len(suf) == 0 {
		return true
	}
	if len(pre) == 0 {
		return strings.Contains(s, suf)
	}
	if len(suf) == 0 {
		return strings.Contains(s, pre)
	}

	start := 0
	for {
		idx := strings.Index(s[start:], pre)
		if idx == -1 {
			break
		}
		i := start + idx
		after := i + len(pre)
		if after <= len(s) && strings.Contains(s[after:], suf) {
			return true
		}
		start = i + 1
	}
	return false
}
```

## Ruby

```ruby
def has_match(s, p)
  star_idx = p.index('*')
  left = p[0...star_idx]
  right = p[(star_idx + 1)..-1] || ''
  l_len = left.length
  r_len = right.length

  return true if l_len == 0 && r_len == 0

  (0..s.length - l_len).each do |i|
    next unless s[i, l_len] == left
    start = i + l_len
    if r_len == 0
      return true
    else
      sub = s[start..-1] || ''
      return true if sub.index(right)
    end
  end

  false
end
```

## Scala

```scala
object Solution {
    def hasMatch(s: String, p: String): Boolean = {
        val starIdx = p.indexOf('*')
        val left = p.substring(0, starIdx)
        val right = p.substring(starIdx + 1)

        if (left.isEmpty && right.isEmpty) return true

        val n = s.length
        val leftLen = left.length

        for (start <- 0 to n - leftLen) {
            if (s.startsWith(left, start)) {
                val idx = s.indexOf(right, start + leftLen)
                if (idx != -1) return true
            }
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn has_match(s: String, p: String) -> bool {
        let s_bytes = s.as_bytes();
        let p_bytes = p.as_bytes();

        // locate the single '*'
        let star_idx = match p_bytes.iter().position(|&c| c == b'*') {
            Some(idx) => idx,
            None => return false, // per problem this won't happen
        };

        let pre = &p_bytes[..star_idx];
        let suf = &p_bytes[star_idx + 1..];

        // both parts empty -> always matches (empty substring)
        if pre.is_empty() && suf.is_empty() {
            return true;
        }

        // only prefix part exists
        if suf.is_empty() {
            if pre.len() > s_bytes.len() {
                return false;
            }
            for i in 0..=s_bytes.len() - pre.len() {
                if &s_bytes[i..i + pre.len()] == pre {
                    return true;
                }
            }
            return false;
        }

        // only suffix part exists
        if pre.is_empty() {
            if suf.len() > s_bytes.len() {
                return false;
            }
            for i in 0..=s_bytes.len() - suf.len() {
                if &s_bytes[i..i + suf.len()] == suf {
                    return true;
                }
            }
            return false;
        }

        // both prefix and suffix are non‑empty
        if pre.len() + suf.len() > s_bytes.len() {
            return false;
        }

        for i in 0..=s_bytes.len() - pre.len() {
            if &s_bytes[i..i + pre.len()] != pre {
                continue;
            }
            let start = i + pre.len();
            // search for suffix starting at or after 'start'
            for j in start..=s_bytes.len() - suf.len() {
                if &s_bytes[j..j + suf.len()] == suf {
                    return true;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (has-match s p)
  (-> string? string? boolean?)
  (let* ([star-pos (string-index-of p "*")]
         [pre (substring p 0 star-pos)]
         [post (substring p (+ star-pos 1) (string-length p))]
         [len-pre (string-length pre)]
         [len-post (string-length post)])
    (cond
      [(and (= len-pre 0) (= len-post 0)) #t] ; pattern "*"
      [(= len-pre 0)
       (if (= len-post 0)
           #t
           (not (eq? (string-index-of s post) #f)))]
      [(= len-post 0)
       (not (eq? (string-index-of s pre) #f))]
      [else
       (let loop ((i 0))
         (if (> i (- (string-length s) len-pre))
             #f
             (if (string=? (substring s i (+ i len-pre)) pre)
                 (let ((pos (string-index-of s post (+ i len-pre))))
                   (if pos
                       #t
                       (loop (+ i 1))))
                 (loop (+ i 1)))))])))
```

## Erlang

```erlang
-spec has_match(S :: unicode:unicode_binary(), P :: unicode:unicode_binary()) -> boolean().
has_match(S, P) ->
    %% Find position of '*'
    [{StarIdx,_}] = binary:match(P, <<"*">>),
    Prefix = binary:part(P, 0, StarIdx),
    Suffix = binary:part(P, StarIdx + 1, byte_size(P) - StarIdx - 1),

    LenPre = byte_size(Prefix),
    LenSuf = byte_size(Suffix),
    LenS   = byte_size(S),

    case {LenPre, LenSuf} of
        {0,0} ->
            true;
        {0,_} ->
            case binary:match(S, Suffix) of
                [] -> false;
                _  -> true
            end;
        {_,0} ->
            case binary:match(S, Prefix) of
                [] -> false;
                _  -> true
            end;
        _ ->
            %% both prefix and suffix are non‑empty
            PrefixMatches = binary:matches(S, Prefix),
            has_match_loop(PrefixMatches, S, LenS, LenPre, Suffix)
    end.

%% Helper: iterate over all occurrences of the prefix
-spec has_match_loop(
          [{non_neg_integer(), non_neg_integer()}],
          unicode:unicode_binary(),
          non_neg_integer(),
          non_neg_integer(),
          unicode:unicode_binary()
        ) -> boolean().
has_match_loop([], _, _, _, _) ->
    false;
has_match_loop([{Pos,_}|Rest], S, LenS, LenPre, Suffix) ->
    After = Pos + LenPre,
    if
        After > LenS ->
            has_match_loop(Rest, S, LenS, LenPre, Suffix);
        true ->
            TailLen = LenS - After,
            Tail = binary:part(S, After, TailLen),
            case binary:match(Tail, Suffix) of
                [] -> has_match_loop(Rest, S, LenS, LenPre, Suffix);
                _  -> true
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec has_match(s :: String.t(), p :: String.t()) :: boolean()
  def has_match(s, p) do
    [pre, suf] = String.split(p, "*", parts: 2)
    s_len = byte_size(s)
    pre_len = byte_size(pre)
    suf_len = byte_size(suf)

    max_i = s_len - pre_len

    Enum.any?(0..max_i, fn i ->
      :binary.part(s, i, pre_len) == pre and
        Enum.any?((i + pre_len)..(s_len - suf_len), fn k ->
          :binary.part(s, k, suf_len) == suf
        end)
    end)
  end
end
```
