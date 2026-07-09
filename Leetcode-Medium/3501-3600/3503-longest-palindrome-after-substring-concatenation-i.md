# 3503. Longest Palindrome After Substring Concatenation I

## Cpp

```cpp
class Solution {
public:
    bool isPal(const std::string& s) {
        int i = 0, j = (int)s.size() - 1;
        while (i < j) {
            if (s[i] != s[j]) return false;
            ++i; --j;
        }
        return true;
    }

    int longestPalindrome(std::string s, std::string t) {
        std::vector<std::string> subsS, subsT;
        subsS.push_back(""); // empty substring
        for (int i = 0; i < (int)s.size(); ++i) {
            for (int j = i; j < (int)s.size(); ++j) {
                subsS.emplace_back(s.substr(i, j - i + 1));
            }
        }
        subsT.push_back("");
        for (int i = 0; i < (int)t.size(); ++i) {
            for (int j = i; j < (int)t.size(); ++j) {
                subsT.emplace_back(t.substr(i, j - i + 1));
            }
        }

        int best = 0;
        for (const auto& a : subsS) {
            for (const auto& b : subsT) {
                std::string cat = a + b;
                if ((int)cat.size() <= best) continue; // quick prune
                if (isPal(cat)) {
                    best = cat.size();
                }
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int longestPalindrome(String s, String t) {
        // Generate all substrings including empty
        java.util.List<String> subsS = new java.util.ArrayList<>();
        java.util.List<String> subsT = new java.util.ArrayList<>();
        subsS.add("");
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                subsS.add(s.substring(i, j));
            }
        }
        subsT.add("");
        for (int i = 0; i < t.length(); i++) {
            for (int j = i + 1; j <= t.length(); j++) {
                subsT.add(t.substring(i, j));
            }
        }

        int maxLen = 0;
        for (String subS : subsS) {
            for (String subT : subsT) {
                int len = subS.length() + subT.length();
                if (len <= maxLen) continue; // no need to check shorter strings
                String combined = subS + subT;
                if (isPalindrome(combined)) {
                    maxLen = len;
                }
            }
        }
        return maxLen;
    }

    private boolean isPalindrome(String str) {
        int l = 0, r = str.length() - 1;
        while (l < r) {
            if (str.charAt(l++) != str.charAt(r--)) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def longestPalindrome(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        def max_pal_sub(st):
            n = len(st)
            best = 0
            for i in range(n):
                # odd length
                l = r = i
                while l >= 0 and r < n and st[l] == st[r]:
                    best = max(best, r - l + 1)
                    l -= 1
                    r += 1
                # even length
                l, r = i, i + 1
                while l >= 0 and r < n and st[l] == st[r]:
                    best = max(best, r - l + 1)
                    l -= 1
                    r += 1
            return best

        ans = max(max_pal_sub(s), max_pal_sub(t))

        n, m = len(s), len(t)
        for i in range(n):
            for j in range(i, n):
                sub_s = s[i:j+1]
                for p in range(m):
                    for q in range(p, m):
                        combined = sub_s + t[p:q+1]
                        if combined == combined[::-1]:
                            ans = max(ans, len(combined))
        return ans
```

## Python3

```python
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        subs_s = [""]
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                subs_s.append(s[i:j])
        subs_t = [""]
        m = len(t)
        for i in range(m):
            for j in range(i + 1, m + 1):
                subs_t.append(t[i:j])

        ans = 0
        for a in subs_s:
            for b in subs_t:
                combined_len = len(a) + len(b)
                if combined_len <= ans:
                    continue
                combined = a + b
                if combined == combined[::-1]:
                    ans = combined_len
        return ans
```

## C

```c
#include <string.h>
#include <stdbool.h>

static bool is_pal(const char *str, int len) {
    int l = 0, r = len - 1;
    while (l < r) {
        if (str[l] != str[r]) return false;
        ++l; --r;
    }
    return true;
}

int longestPalindrome(char* s, char* t) {
    int n = strlen(s);
    int m = strlen(t);
    int ans = 0;

    /* palindromes inside s */
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            if (is_pal(s + i, j - i + 1))
                if (j - i + 1 > ans) ans = j - i + 1;
        }
    }

    /* palindromes inside t */
    for (int i = 0; i < m; ++i) {
        for (int j = i; j < m; ++j) {
            if (is_pal(t + i, j - i + 1))
                if (j - i + 1 > ans) ans = j - i + 1;
        }
    }

    char buf[61];   // max length 30+30

    /* concatenations of non‑empty substrings from both strings */
    for (int si = 0; si < n; ++si) {
        for (int sj = si; sj < n; ++sj) {
            int idx = 0;
            for (int k = si; k <= sj; ++k) buf[idx++] = s[k];   // copy s substring

            for (int ti = 0; ti < m; ++ti) {
                for (int tj = ti; tj < m; ++tj) {
                    int cur = idx;
                    for (int k = ti; k <= tj; ++k) buf[cur++] = t[k]; // copy t substring
                    if (is_pal(buf, cur) && cur > ans) ans = cur;
                }
            }
        }
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int LongestPalindrome(string s, string t)
    {
        int n = s.Length;
        int m = t.Length;
        int best = 0;

        bool IsPal(string str)
        {
            int i = 0, j = str.Length - 1;
            while (i < j)
            {
                if (str[i] != str[j]) return false;
                i++; j--;
            }
            return true;
        }

        // substrings from s alone
        for (int i = 0; i < n; ++i)
        {
            for (int len = 1; i + len <= n; ++len)
            {
                string subS = s.Substring(i, len);
                if (IsPal(subS) && subS.Length > best) best = subS.Length;
            }
        }

        // substrings from t alone
        for (int i = 0; i < m; ++i)
        {
            for (int len = 1; i + len <= m; ++len)
            {
                string subT = t.Substring(i, len);
                if (IsPal(subT) && subT.Length > best) best = subT.Length;
            }
        }

        // concatenations: non‑empty substring from s + non‑empty substring from t
        for (int i = 0; i < n; ++i)
        {
            for (int lenS = 1; i + lenS <= n; ++lenS)
            {
                string subS = s.Substring(i, lenS);
                for (int j = 0; j < m; ++j)
                {
                    for (int lenT = 1; j + lenT <= m; ++lenT)
                    {
                        string subT = t.Substring(j, lenT);
                        string combined = subS + subT;
                        if (IsPal(combined) && combined.Length > best) best = combined.Length;
                    }
                }
            }
        }

        // also consider using only one side (empty substring on the other side)
        // already covered by the first two loops

        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var longestPalindrome = function(s, t) {
    const subsS = [];
    for (let i = 0; i < s.length; ++i) {
        for (let j = i; j < s.length; ++j) {
            subsS.push(s.slice(i, j + 1));
        }
    }
    subsS.push(""); // empty substring

    const subsT = [];
    for (let i = 0; i < t.length; ++i) {
        for (let j = i; j < t.length; ++j) {
            subsT.push(t.slice(i, j + 1));
        }
    }
    subsT.push(""); // empty substring

    const isPal = (str) => {
        let l = 0, r = str.length - 1;
        while (l < r) {
            if (str[l] !== str[r]) return false;
            ++l; --r;
        }
        return true;
    };

    let maxLen = 0;
    for (const a of subsS) {
        for (const b of subsT) {
            const combined = a + b;
            if (combined.length > maxLen && isPal(combined)) {
                maxLen = combined.length;
            }
        }
    }
    return maxLen;
};
```

## Typescript

```typescript
function longestPalindrome(s: string, t: string): number {
    const isPal = (str: string): boolean => {
        let l = 0, r = str.length - 1;
        while (l < r) {
            if (str.charCodeAt(l) !== str.charCodeAt(r)) return false;
            ++l; --r;
        }
        return true;
    };

    const n = s.length, m = t.length;
    let ans = 1; // at least one character exists

    // collect all substrings of s and t
    const subsS: string[] = [];
    for (let i = 0; i < n; ++i) {
        for (let j = i; j < n; ++j) {
            const sub = s.slice(i, j + 1);
            subsS.push(sub);
            if (isPal(sub)) ans = Math.max(ans, sub.length);
        }
    }

    const subsT: string[] = [];
    for (let i = 0; i < m; ++i) {
        for (let j = i; j < m; ++j) {
            const sub = t.slice(i, j + 1);
            subsT.push(sub);
            if (isPal(sub)) ans = Math.max(ans, sub.length);
        }
    }

    // check concatenations of a substring from s and a substring from t
    for (const subS of subsS) {
        for (const subT of subsT) {
            const combined = subS + subT;
            if (isPal(combined)) ans = Math.max(ans, combined.length);
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function longestPalindrome($s, $t) {
        $n = strlen($s);
        $m = strlen($t);
        $maxLen = 0;

        for ($i = 0; $i <= $n; $i++) {
            for ($j = $i; $j <= $n; $j++) {
                $subS = substr($s, $i, $j - $i); // may be empty
                for ($p = 0; $p <= $m; $p++) {
                    for ($q = $p; $q <= $m; $q++) {
                        $subT = substr($t, $p, $q - $p);
                        $combined = $subS . $subT;
                        if ($this->isPalindrome($combined)) {
                            $len = strlen($combined);
                            if ($len > $maxLen) {
                                $maxLen = $len;
                            }
                        }
                    }
                }
            }
        }

        return $maxLen;
    }

    private function isPalindrome(string $str): bool {
        $l = 0;
        $r = strlen($str) - 1;
        while ($l < $r) {
            if ($str[$l] !== $str[$r]) {
                return false;
            }
            $l++;
            $r--;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func longestPalindrome(_ s: String, _ t: String) -> Int {
        let sArr = Array(s)
        let tArr = Array(t)
        var maxLen = 0
        let sCount = sArr.count
        let tCount = tArr.count
        
        for i in 0...sCount {
            for j in i...sCount {
                let subS = sArr[i..<j]
                for p in 0...tCount {
                    for q in p...tCount {
                        let subT = tArr[p..<q]
                        var combined = [Character]()
                        combined.append(contentsOf: subS)
                        combined.append(contentsOf: subT)
                        
                        var l = 0
                        var r = combined.count - 1
                        var isPal = true
                        while l < r {
                            if combined[l] != combined[r] {
                                isPal = false
                                break
                            }
                            l += 1
                            r -= 1
                        }
                        if isPal && combined.count > maxLen {
                            maxLen = combined.count
                        }
                    }
                }
            }
        }
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestPalindrome(s: String, t: String): Int {
        val subsS = mutableListOf<String>()
        subsS.add("")
        for (i in 0 until s.length) {
            var sb = StringBuilder()
            for (j in i until s.length) {
                sb.append(s[j])
                subsS.add(sb.toString())
            }
        }

        val subsT = mutableListOf<String>()
        subsT.add("")
        for (i in 0 until t.length) {
            var sb = StringBuilder()
            for (j in i until t.length) {
                sb.append(t[j])
                subsT.add(sb.toString())
            }
        }

        var best = 0
        for (a in subsS) {
            for (b in subsT) {
                val combined = a + b
                if (combined.length <= best) continue
                if (isPalindrome(combined)) {
                    best = combined.length
                }
            }
        }
        return best
    }

    private fun isPalindrome(str: String): Boolean {
        var l = 0
        var r = str.length - 1
        while (l < r) {
            if (str[l] != str[r]) return false
            l++
            r--
        }
        return true
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int longestPalindrome(String s, String t) {
    bool isPal(String str) {
      int i = 0;
      int j = str.length - 1;
      while (i < j) {
        if (str.codeUnitAt(i) != str.codeUnitAt(j)) return false;
        i++;
        j--;
      }
      return true;
    }

    int n = s.length;
    int m = t.length;
    int ans = 0;

    for (int i = 0; i <= n; ++i) {
      for (int j = i; j <= n; ++j) {
        String a = s.substring(i, j);
        for (int p = 0; p <= m; ++p) {
          for (int q = p; q <= m; ++q) {
            String b = t.substring(p, q);
            String combined = a + b;
            if (isPal(combined)) {
              ans = max(ans, combined.length);
            }
          }
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
func longestPalindrome(s string, t string) int {
	n := len(s)
	m := len(t)
	maxLen := 0

	// substrings from s alone
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			if isPal(s[i : j+1]) {
				l := j - i + 1
				if l > maxLen {
					maxLen = l
				}
			}
		}
	}

	// substrings from t alone
	for i := 0; i < m; i++ {
		for j := i; j < m; j++ {
			if isPal(t[i : j+1]) {
				l := j - i + 1
				if l > maxLen {
					maxLen = l
				}
			}
		}
	}

	// substrings from both s and t (s part first)
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			subS := s[i : j+1]
			for p := 0; p < m; p++ {
				for q := p; q < m; q++ {
					combined := subS + t[p:q+1]
					if isPal(combined) {
						l := len(combined)
						if l > maxLen {
							maxLen = l
						}
					}
				}
			}
		}
	}

	if maxLen == 0 && (n > 0 || m > 0) {
		return 1
	}
	return maxLen
}

func isPal(str string) bool {
	i, j := 0, len(str)-1
	for i < j {
		if str[i] != str[j] {
			return false
		}
		i++
		j--
	}
	return true
}
```

## Ruby

```ruby
def palindrome?(s)
  i = 0
  j = s.length - 1
  while i < j
    return false if s[i] != s[j]
    i += 1
    j -= 1
  end
  true
end

# @param {String} s
# @param {String} t
# @return {Integer}
def longest_palindrome(s, t)
  subs_s = [""]
  (0...s.length).each do |i|
    (i...s.length).each do |j|
      subs_s << s[i..j]
    end
  end

  subs_t = [""]
  (0...t.length).each do |i|
    (i...t.length).each do |j|
      subs_t << t[i..j]
    end
  end

  max_len = 0
  subs_s.each do |a|
    subs_t.each do |b|
      combined = a + b
      if palindrome?(combined)
        len = combined.length
        max_len = len if len > max_len
      end
    end
  end
  max_len
end
```

## Scala

```scala
object Solution {
  def longestPalindrome(s: String, t: String): Int = {
    val n = s.length
    val m = t.length
    var best = 0

    val subsS = for {
      i <- 0 to n
      j <- i to n
    } yield s.substring(i, j)

    val subsT = for {
      i <- 0 to m
      j <- i to m
    } yield t.substring(i, j)

    for (subS <- subsS) {
      for (subT <- subsT) {
        val combined = subS + subT
        if (combined.length > best && isPalindrome(combined)) {
          best = combined.length
        }
      }
    }

    best
  }

  private def isPalindrome(str: String): Boolean = {
    var i = 0
    var j = str.length - 1
    while (i < j) {
      if (str.charAt(i) != str.charAt(j)) return false
      i += 1
      j -= 1
    }
    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_palindrome(s: String, t: String) -> i32 {
        // generate all substrings of s (including empty)
        let mut subs_s = Vec::new();
        let n = s.len();
        for i in 0..=n {
            for j in i..=n {
                subs_s.push(s[i..j].to_string());
            }
        }

        // generate all substrings of t (including empty)
        let mut subs_t = Vec::new();
        let m = t.len();
        for i in 0..=m {
            for j in i..=m {
                subs_t.push(t[i..j].to_string());
            }
        }

        let mut best = 0usize;
        for a in &subs_s {
            for b in &subs_t {
                let len = a.len() + b.len();
                if len <= best {
                    continue; // cannot improve
                }
                let combined = format!("{}{}", a, b);
                if is_palindrome(&combined) {
                    best = len;
                }
            }
        }

        best as i32
    }
}

fn is_palindrome(s: &str) -> bool {
    let bytes = s.as_bytes();
    let mut l = 0usize;
    let mut r = bytes.len();
    while l < r {
        if bytes[l] != bytes[r - 1] {
            return false;
        }
        l += 1;
        r -= 1;
    }
    true
}
```

## Racket

```racket
(define/contract (longest-palindrome s t)
  (-> string? string? exact-integer?)
  (letrec
      ((palindrome?
        (lambda (str)
          (let loop ([i 0] [j (- (string-length str) 1)])
            (or (>= i j)
                (and (char=? (string-ref str i) (string-ref str j))
                     (loop (+ i 1) (- j 1)))))))
       (substrings
        (lambda (str)
          (let* ((n (string-length str))
                 (res (list ""))) ; include empty substring
            (for ([i (in-range n)])
              (for ([j (in-range (+ i 1) (+ n 1))])
                (set! res (cons (substring str i j) res))))
            res))))
    (let ((maxlen 0))
      (for* ([sub-s (in-list (substrings s))]
             [sub-t (in-list (substrings t))])
        (let ((combined (string-append sub-s sub-t)))
          (when (palindrome? combined)
            (set! maxlen (max maxlen (string-length combined))))))
      maxlen)))
```

## Erlang

```erlang
-module(solution).
-export([longest_palindrome/2]).

-spec longest_palindrome(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
longest_palindrome(S, T) ->
    SList = unicode:characters_to_list(S),
    TList = unicode:characters_to_list(T),
    SubS = substrings(SList),
    SubT = substrings(TList),
    max_len(SubS, SubT, 0).

substrings(L) ->
    N = length(L),
    Empty = [[]],
    NonEmpty = [lists:sublist(L, I, Len) ||
                I <- lists:seq(1, N),
                Len <- lists:seq(1, N - I + 1)],
    Empty ++ NonEmpty.

max_len([], _, Max) -> Max;
max_len([Ssub|RestS], SubT, CurMax) ->
    NewMax = max_with_fixed_s(Ssub, SubT, CurMax),
    max_len(RestS, SubT, NewMax).

max_with_fixed_s(_, [], Max) -> Max;
max_with_fixed_s(Ssub, [Tsub|RestT], CurMax) ->
    Combined = Ssub ++ Tsub,
    Len = length(Combined),
    UpdatedMax =
        if
            Len > CurMax, is_palindrome(Combined) -> Len;
            true -> CurMax
        end,
    max_with_fixed_s(Ssub, RestT, UpdatedMax).

is_palindrome(L) ->
    L == lists:reverse(L).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_palindrome(s :: String.t(), t :: String.t()) :: integer()
  def longest_palindrome(s, t) do
    s_subs = substrings(s)
    t_subs = substrings(t)

    Enum.reduce(s_subs, 0, fn ss, acc ->
      Enum.reduce(t_subs, acc, fn tt, best ->
        combined = ss <> tt

        if palindrome?(combined) do
          len = String.length(combined)
          if len > best, do: len, else: best
        else
          best
        end
      end)
    end)
  end

  defp substrings(str) do
    n = String.length(str)

    subs =
      for i <- 0..(n - 1),
          j <- i..(n - 1),
          do: String.slice(str, i, j - i + 1)

    subs ++ [""]
  end

  defp palindrome?(str) do
    str == String.reverse(str)
  end
end
```
