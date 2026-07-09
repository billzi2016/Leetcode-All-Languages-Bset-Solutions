# 0214. Shortest Palindrome

## Cpp

```cpp
class Solution {
public:
    string shortestPalindrome(string s) {
        string rev = s;
        reverse(rev.begin(), rev.end());
        string combined = s + "#" + rev;
        vector<int> pi(combined.size(), 0);
        for (int i = 1; i < (int)combined.size(); ++i) {
            int j = pi[i - 1];
            while (j > 0 && combined[i] != combined[j]) {
                j = pi[j - 1];
            }
            if (combined[i] == combined[j]) ++j;
            pi[i] = j;
        }
        int palLen = pi.back();
        string suffix = s.substr(palLen);
        reverse(suffix.begin(), suffix.end());
        return suffix + s;
    }
};
```

## Java

```java
class Solution {
    public String shortestPalindrome(String s) {
        if (s == null || s.length() <= 1) return s;
        String rev = new StringBuilder(s).reverse().toString();
        String combined = s + "#" + rev;
        int[] lps = new int[combined.length()];
        for (int i = 1; i < combined.length(); i++) {
            int len = lps[i - 1];
            while (len > 0 && combined.charAt(i) != combined.charAt(len)) {
                len = lps[len - 1];
            }
            if (combined.charAt(i) == combined.charAt(len)) {
                len++;
            }
            lps[i] = len;
        }
        int palPrefixLen = lps[combined.length() - 1];
        String suffix = s.substring(palPrefixLen);
        return new StringBuilder(suffix).reverse().toString() + s;
    }
}
```

## Python

```python
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        rev = s[::-1]
        combined = s + "#" + rev
        pi = [0] * len(combined)
        for i in range(1, len(combined)):
            j = pi[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = pi[j - 1]
            if combined[i] == combined[j]:
                j += 1
            pi[i] = j
        l = pi[-1]  # length of longest palindromic prefix
        to_add = rev[:len(s) - l]
        return to_add + s
```

## Python3

```python
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        rev = s[::-1]
        combined = s + "#" + rev
        pi = [0] * len(combined)
        for i in range(1, len(combined)):
            j = pi[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = pi[j - 1]
            if combined[i] == combined[j]:
                j += 1
            pi[i] = j
        l = pi[-1]
        return rev[:len(s) - l] + s
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* shortestPalindrome(char* s) {
    int n = strlen(s);
    if (n == 0) {
        char *empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    // reverse of s
    char *rev = (char*)malloc(n + 1);
    for (int i = 0; i < n; ++i) rev[i] = s[n - 1 - i];
    rev[n] = '\0';

    // combined string: s + "#" + rev
    int m = 2 * n + 1;
    char *combined = (char*)malloc(m + 1);
    memcpy(combined, s, n);
    combined[n] = '#';
    memcpy(combined + n + 1, rev, n);
    combined[m] = '\0';

    // KMP prefix table
    int *pi = (int*)calloc(m, sizeof(int));
    for (int i = 1; i < m; ++i) {
        int j = pi[i - 1];
        while (j > 0 && combined[i] != combined[j]) {
            j = pi[j - 1];
        }
        if (combined[i] == combined[j]) ++j;
        pi[i] = j;
    }

    int palLen = pi[m - 1];               // longest palindromic prefix length
    int addLen = n - palLen;              // characters to prepend

    char *res = (char*)malloc(2 * n - palLen + 1);
    int pos = 0;
    for (int i = addLen - 1; i >= 0; --i) {
        res[pos++] = s[i];
    }
    memcpy(res + pos, s, n);
    pos += n;
    res[pos] = '\0';

    free(rev);
    free(combined);
    free(pi);
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string ShortestPalindrome(string s)
    {
        if (string.IsNullOrEmpty(s) || s.Length == 1)
            return s;

        char[] revArr = s.ToCharArray();
        System.Array.Reverse(revArr);
        string rev = new string(revArr);

        string combined = s + "#" + rev;
        int n = combined.Length;
        int[] pi = new int[n];

        for (int i = 1; i < n; i++)
        {
            int j = pi[i - 1];
            while (j > 0 && combined[i] != combined[j])
                j = pi[j - 1];
            if (combined[i] == combined[j])
                j++;
            pi[i] = j;
        }

        int longestPalPrefixLen = pi[n - 1];
        string suffix = s.Substring(longestPalPrefixLen);
        char[] suffixArr = suffix.ToCharArray();
        System.Array.Reverse(suffixArr);
        string revSuffix = new string(suffixArr);

        return revSuffix + s;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var shortestPalindrome = function(s) {
    if (s.length === 0) return "";
    const rev = s.split('').reverse().join('');
    const combined = s + "#" + rev;
    const lps = new Array(combined.length).fill(0);
    for (let i = 1; i < combined.length; i++) {
        let len = lps[i - 1];
        while (len > 0 && combined[i] !== combined[len]) {
            len = lps[len - 1];
        }
        if (combined[i] === combined[len]) {
            len++;
        }
        lps[i] = len;
    }
    const palPrefixLen = lps[combined.length - 1];
    const suffix = s.slice(palPrefixLen);
    const prefixToAdd = suffix.split('').reverse().join('');
    return prefixToAdd + s;
};
```

## Typescript

```typescript
function shortestPalindrome(s: string): string {
    if (s.length === 0) return "";
    const rev = s.split("").reverse().join("");
    const combined = s + "#" + rev;
    const lps = new Array(combined.length).fill(0);
    for (let i = 1; i < combined.length; i++) {
        let len = lps[i - 1];
        while (len > 0 && combined[i] !== combined[len]) {
            len = lps[len - 1];
        }
        if (combined[i] === combined[len]) {
            len++;
        }
        lps[i] = len;
    }
    const palLen = lps[combined.length - 1];
    const suffix = s.substring(palLen);
    const add = suffix.split("").reverse().join("");
    return add + s;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function shortestPalindrome($s) {
        $n = strlen($s);
        if ($n === 0) {
            return "";
        }
        $rev = strrev($s);
        $combined = $s . "#" . $rev;
        $m = strlen($combined);
        $lps = array_fill(0, $m, 0);

        for ($i = 1; $i < $m; $i++) {
            $len = $lps[$i - 1];
            while ($len > 0 && $combined[$i] !== $combined[$len]) {
                $len = $lps[$len - 1];
            }
            if ($combined[$i] === $combined[$len]) {
                $len++;
            }
            $lps[$i] = $len;
        }

        $palLen = $lps[$m - 1];
        $suffix = substr($s, $palLen);
        return strrev($suffix) . $s;
    }
}
```

## Swift

```swift
class Solution {
    func shortestPalindrome(_ s: String) -> String {
        if s.isEmpty { return "" }
        let rev = String(s.reversed())
        let combined = s + "#" + rev
        let chars = Array(combined)
        var lps = [Int](repeating: 0, count: chars.count)
        
        for i in 1..<chars.count {
            var length = lps[i - 1]
            while length > 0 && chars[i] != chars[length] {
                length = lps[length - 1]
            }
            if chars[i] == chars[length] {
                length += 1
            }
            lps[i] = length
        }
        
        let palLen = lps[chars.count - 1]
        let startIdx = s.index(s.startIndex, offsetBy: palLen)
        let suffix = s[startIdx...]
        let prefixToAdd = String(suffix.reversed())
        return prefixToAdd + s
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shortestPalindrome(s: String): String {
        if (s.isEmpty()) return s
        val rev = s.reversed()
        val combined = s + "#" + rev
        val lps = IntArray(combined.length)
        for (i in 1 until combined.length) {
            var len = lps[i - 1]
            while (len > 0 && combined[i] != combined[len]) {
                len = lps[len - 1]
            }
            if (combined[i] == combined[len]) {
                len++
            }
            lps[i] = len
        }
        val palLen = lps[combined.length - 1]
        val suffix = s.substring(palLen)
        return suffix.reversed() + s
    }
}
```

## Dart

```dart
class Solution {
  String shortestPalindrome(String s) {
    if (s.isEmpty) return s;
    String rev = s.split('').reversed.join();
    String combined = s + "#" + rev;
    int n = combined.length;
    List<int> lps = List.filled(n, 0);
    for (int i = 1; i < n; ++i) {
      int len = lps[i - 1];
      while (len > 0 && combined.codeUnitAt(i) != combined.codeUnitAt(len)) {
        len = lps[len - 1];
      }
      if (combined.codeUnitAt(i) == combined.codeUnitAt(len)) {
        len++;
      }
      lps[i] = len;
    }
    int palLen = lps[n - 1];
    String suffix = s.substring(palLen);
    String revSuffix = suffix.split('').reversed.join();
    return revSuffix + s;
  }
}
```

## Golang

```go
func shortestPalindrome(s string) string {
	if len(s) == 0 {
		return s
	}
	rev := reverseString(s)
	combined := s + "#" + rev

	pi := make([]int, len(combined))
	for i := 1; i < len(combined); i++ {
		j := pi[i-1]
		for j > 0 && combined[i] != combined[j] {
			j = pi[j-1]
		}
		if combined[i] == combined[j] {
			j++
		}
		pi[i] = j
	}

	palLen := pi[len(combined)-1]
	suffix := s[palLen:]
	return reverseString(suffix) + s
}

func reverseString(str string) string {
	b := []byte(str)
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i]
	}
	return string(b)
}
```

## Ruby

```ruby
def shortest_palindrome(s)
  return s if s.empty?
  rev = s.reverse
  combined = s + "#" + rev
  lps = Array.new(combined.length, 0)

  (1...combined.length).each do |i|
    len = lps[i - 1]
    while len > 0 && combined[i] != combined[len]
      len = lps[len - 1]
    end
    len += 1 if combined[i] == combined[len]
    lps[i] = len
  end

  pal_len = lps[-1]
  suffix = s[pal_len..-1] || ""
  suffix.reverse + s
end
```

## Scala

```scala
object Solution {
    def shortestPalindrome(s: String): String = {
        if (s.isEmpty) return s
        val rev = s.reverse
        val combined = s + "#" + rev
        val n = combined.length
        val pi = new Array[Int](n)
        for (i <- 1 until n) {
            var j = pi(i - 1)
            while (j > 0 && combined.charAt(i) != combined.charAt(j)) {
                j = pi(j - 1)
            }
            if (combined.charAt(i) == combined.charAt(j)) j += 1
            pi(i) = j
        }
        val l = pi(n - 1)
        val suffix = s.substring(l)
        val add = new StringBuilder(suffix).reverse.toString
        add + s
    }
}
```

## Rust

```rust
impl Solution {
    pub fn shortest_palindrome(s: String) -> String {
        if s.is_empty() {
            return s;
        }
        let bytes = s.as_bytes();
        let rev_bytes: Vec<u8> = bytes.iter().rev().cloned().collect();
        // combined = s + "#" + reverse(s)
        let mut combined: Vec<u8> = Vec::with_capacity(bytes.len() * 2 + 1);
        combined.extend_from_slice(bytes);
        combined.push(b'#');
        combined.extend_from_slice(&rev_bytes);

        let m = combined.len();
        let mut pi = vec![0usize; m];
        for i in 1..m {
            let mut j = pi[i - 1];
            while j > 0 && combined[i] != combined[j] {
                j = pi[j - 1];
            }
            if combined[i] == combined[j] {
                j += 1;
            }
            pi[i] = j;
        }

        let pal_len = pi[m - 1]; // length of longest palindromic prefix
        let suffix = &s[pal_len..];
        let rev_suffix: String = suffix.chars().rev().collect();
        format!("{}{}", rev_suffix, s)
    }
}
```

## Racket

```racket
(define/contract (shortest-palindrome s)
  (-> string? string?)
  (let* ((len (string-length s))
         (rev (list->string (reverse (string->list s)))))
    (if (= len 0)
        ""
        (let* ((combined (string-append s "#" rev))
               (m (string-length combined))
               (pi (make-vector m 0)))
          ;; build prefix table
          (let loop ((i 1) (j 0))
            (when (< i m)
              (if (char=? (string-ref combined i) (string-ref combined j))
                  (begin
                    (set! j (+ j 1))
                    (vector-set! pi i j)
                    (loop (+ i 1) j))
                  (if (> j 0)
                      (let ((newj (vector-ref pi (- j 1))))
                        (set! j newj)
                        (loop i j))
                      (begin
                        (vector-set! pi i 0)
                        (loop (+ i 1) 0))))))
          (let* ((pal-prefix-len (vector-ref pi (- m 1)))
                 (suffix (substring s pal-prefix-len len))
                 (rev-suffix (list->string (reverse (string->list suffix)))))
            (string-append rev-suffix s))))))
```

## Erlang

```erlang
-module(solution).
-export([shortest_palindrome/1]).

-spec shortest_palindrome(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
shortest_palindrome(<<>>) ->
    <<>>;
shortest_palindrome(S) ->
    L = binary_to_list(S),
    RevL = lists:reverse(L),
    CombinedList = L ++ [$#] ++ RevL,
    N = length(CombinedList),
    Tuple = list_to_tuple(CombinedList),
    Pi0 = array:new(N, {default, 0}),
    Len = kmp_loop(Tuple, N, 1, 0, Pi0),
    {_Prefix, Rest} = lists:split(Len, L),
    Result = lists:reverse(Rest) ++ L,
    list_to_binary(Result).

kmp_loop(_Tuple, _N, I, Len, _Pi) when I >= _N ->
    Len;
kmp_loop(Tuple, N, I, Len, Pi) ->
    CharI = element(I + 1, Tuple),
    NewLen = adjust_len(CharI, Len, Tuple, Pi),
    FinalLen =
        case CharI == element(NewLen + 1, Tuple) of
            true -> NewLen + 1;
            false -> NewLen
        end,
    Pi2 = array:set(I, FinalLen, Pi),
    kmp_loop(Tuple, N, I + 1, FinalLen, Pi2).

adjust_len(_CharI, 0, _Tuple, _Pi) ->
    0;
adjust_len(CharI, Len, Tuple, Pi) when Len > 0 ->
    CharLen = element(Len + 1, Tuple),
    case CharI == CharLen of
        true -> Len;
        false ->
            PrevLen = array:get(Len - 1, Pi),
            adjust_len(CharI, PrevLen, Tuple, Pi)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_palindrome(s :: String.t()) :: String.t()
  def shortest_palindrome(s) do
    rev = String.reverse(s)
    combined = s <> "#" <> rev

    table = build_prefix(combined)
    len_combined = byte_size(combined)
    longest = :array.get(len_combined - 1, table)

    suffix_len = byte_size(s) - longest
    suffix = if suffix_len > 0, do: String.slice(s, longest, suffix_len), else: ""
    String.reverse(suffix) <> s
  end

  defp build_prefix(combined) do
    len = byte_size(combined)
    init_table = :array.new(len, default: 0)

    if len <= 1 do
      init_table
    else
      {final_table, _} =
        Enum.reduce(1..(len - 1), {init_table, 0}, fn i, {tbl, j} ->
          j2 = update_j(i, j, combined, tbl)

          j3 =
            if :binary.at(combined, i) == :binary.at(combined, j2) do
              j2 + 1
            else
              j2
            end

          new_tbl = :array.set(i, j3, tbl)
          {new_tbl, j3}
        end)

      final_table
    end
  end

  defp update_j(i, j, combined, table) do
    if j > 0 and :binary.at(combined, i) != :binary.at(combined, j) do
      new_j = :array.get(j - 1, table)
      update_j(i, new_j, combined, table)
    else
      j
    end
  end
end
```
