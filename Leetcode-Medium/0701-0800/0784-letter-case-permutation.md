# 0784. Letter Case Permutation

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCasePermutation(string s) {
        vector<string> ans;
        backtrack(0, s, ans);
        return ans;
    }
private:
    void backtrack(int pos, string &s, vector<string>& ans) {
        if (pos == (int)s.size()) {
            ans.push_back(s);
            return;
        }
        if (isdigit(s[pos])) {
            backtrack(pos + 1, s, ans);
        } else {
            char original = s[pos];
            s[pos] = tolower(original);
            backtrack(pos + 1, s, ans);
            s[pos] = toupper(original);
            backtrack(pos + 1, s, ans);
            s[pos] = original; // restore (optional)
        }
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> letterCasePermutation(String s) {
        List<String> result = new ArrayList<>();
        if (s == null) return result;
        char[] chars = s.toCharArray();
        backtrack(chars, 0, result);
        return result;
    }

    private void backtrack(char[] chars, int index, List<String> result) {
        if (index == chars.length) {
            result.add(new String(chars));
            return;
        }
        if (Character.isLetter(chars[index])) {
            char original = chars[index];
            chars[index] = Character.toLowerCase(original);
            backtrack(chars, index + 1, result);
            chars[index] = Character.toUpperCase(original);
            backtrack(chars, index + 1, result);
            chars[index] = original; // restore (optional)
        } else {
            backtrack(chars, index + 1, result);
        }
    }
}
```

## Python

```python
class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = ['']
        for ch in s:
            if ch.isalpha():
                lower = ch.lower()
                upper = ch.upper()
                # duplicate each existing string with both cases
                res = [prev + lower for prev in res] + [prev + upper for prev in res]
            else:
                # digit, just append to all strings
                res = [prev + ch for prev in res]
        return res
```

## Python3

```python
from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res: List[str] = []
        n = len(s)

        def backtrack(i: int, path: List[str]) -> None:
            if i == n:
                res.append(''.join(path))
                return
            ch = s[i]
            if ch.isalpha():
                for c in (ch.lower(), ch.upper()):
                    path.append(c)
                    backtrack(i + 1, path)
                    path.pop()
            else:
                path.append(ch)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** letterCasePermutation(char* s, int* returnSize) {
    int n = strlen(s);
    int letters = 0;
    for (int i = 0; i < n; ++i) {
        if (isalpha((unsigned char)s[i])) letters++;
    }
    
    int total = 1 << letters;
    char **result = (char **)malloc(total * sizeof(char *));
    *returnSize = total;
    
    for (int mask = 0; mask < total; ++mask) {
        char *cur = (char *)malloc((n + 1) * sizeof(char));
        int idx = 0; // index of current letter
        for (int i = 0; i < n; ++i) {
            char c = s[i];
            if (isalpha((unsigned char)c)) {
                if ((mask >> idx) & 1)
                    cur[i] = toupper((unsigned char)c);
                else
                    cur[i] = tolower((unsigned char)c);
                idx++;
            } else {
                cur[i] = c;
            }
        }
        cur[n] = '\0';
        result[mask] = cur;
    }
    
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<string> LetterCasePermutation(string s)
    {
        var result = new List<string>();
        if (s == null) return result;
        char[] chars = s.ToCharArray();
        Backtrack(chars, 0, result);
        return result;
    }

    private void Backtrack(char[] chars, int index, IList<string> result)
    {
        if (index == chars.Length)
        {
            result.Add(new string(chars));
            return;
        }

        if (char.IsLetter(chars[index]))
        {
            char original = chars[index];

            // lowercase branch
            chars[index] = char.ToLower(original);
            Backtrack(chars, index + 1, result);

            // uppercase branch
            chars[index] = char.ToUpper(original);
            Backtrack(chars, index + 1, result);
        }
        else
        {
            Backtrack(chars, index + 1, result);
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var letterCasePermutation = function(s) {
    let result = [''];
    for (const ch of s) {
        const size = result.length;
        if (ch >= '0' && ch <= '9') {
            for (let i = 0; i < size; i++) {
                result[i] += ch;
            }
        } else {
            for (let i = 0; i < size; i++) {
                const cur = result[i];
                result[i] = cur + ch.toLowerCase();
                result.push(cur + ch.toUpperCase());
            }
        }
    }
    return result;
};
```

## Typescript

```typescript
function letterCasePermutation(s: string): string[] {
    let result: string[] = [''];
    for (const ch of s) {
        const size = result.length;
        if (/[a-zA-Z]/.test(ch)) {
            for (let i = 0; i < size; i++) {
                const base = result[i];
                result[i] = base + ch.toLowerCase();
                result.push(base + ch.toUpperCase());
            }
        } else {
            for (let i = 0; i < size; i++) {
                result[i] += ch;
            }
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function letterCasePermutation($s) {
        $results = [''];
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if (ctype_digit($ch)) {
                foreach ($results as &$str) {
                    $str .= $ch;
                }
                unset($str);
            } else { // alphabetic character
                $temp = [];
                foreach ($results as $str) {
                    $temp[] = $str . strtolower($ch);
                    $temp[] = $str . strtoupper($ch);
                }
                $results = $temp;
            }
        }
        return $results;
    }
}
```

## Swift

```swift
class Solution {
    func letterCasePermutation(_ s: String) -> [String] {
        var chars = Array(s)
        var results = [String]()
        
        func backtrack(_ index: Int) {
            if index == chars.count {
                results.append(String(chars))
                return
            }
            
            let ch = chars[index]
            if ch.isLetter {
                // Lowercase branch
                let original = chars[index]
                chars[index] = Character(String(original).lowercased())
                backtrack(index + 1)
                
                // Uppercase branch
                chars[index] = Character(String(original).uppercased())
                backtrack(index + 1)
                
                // Restore (optional)
                chars[index] = original
            } else {
                backtrack(index + 1)
            }
        }
        
        backtrack(0)
        return results
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun letterCasePermutation(s: String): List<String> {
        val result = mutableListOf<String>()
        fun backtrack(index: Int, sb: StringBuilder) {
            if (index == s.length) {
                result.add(sb.toString())
                return
            }
            val ch = s[index]
            if (ch in '0'..'9') {
                sb.append(ch)
                backtrack(index + 1, sb)
                sb.setLength(sb.length - 1)
            } else {
                // lowercase option
                sb.append(ch.lowercaseChar())
                backtrack(index + 1, sb)
                sb.setLength(sb.length - 1)

                // uppercase option
                sb.append(ch.uppercaseChar())
                backtrack(index + 1, sb)
                sb.setLength(sb.length - 1)
            }
        }
        backtrack(0, StringBuilder())
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> letterCasePermutation(String s) {
    List<String> result = [];
    void backtrack(int index, String current) {
      if (index == s.length) {
        result.add(current);
        return;
      }
      var ch = s[index];
      if (RegExp(r'[a-zA-Z]').hasMatch(ch)) {
        backtrack(index + 1, current + ch.toLowerCase());
        backtrack(index + 1, current + ch.toUpperCase());
      } else {
        backtrack(index + 1, current + ch);
      }
    }

    backtrack(0, '');
    return result;
  }
}
```

## Golang

```go
package main

import (
	"unicode"
)

func letterCasePermutation(s string) []string {
	res := []string{""}
	for _, ch := range s {
		n := len(res)
		if ch >= '0' && ch <= '9' {
			for i := 0; i < n; i++ {
				res[i] = res[i] + string(ch)
			}
		} else {
			lower := unicode.ToLower(ch)
			upper := unicode.ToUpper(ch)
			for i := 0; i < n; i++ {
				cur := res[i]
				res[i] = cur + string(lower)
				res = append(res, cur+string(upper))
			}
		}
	}
	return res
}
```

## Ruby

```ruby
def letter_case_permutation(s)
  result = ['']
  s.each_char do |ch|
    if ch =~ /\d/
      result.map! { |prefix| prefix + ch }
    else
      lower = ch.downcase
      upper = ch.upcase
      new_res = []
      result.each do |prefix|
        new_res << prefix + lower
        new_res << prefix + upper
      end
      result = new_res
    end
  end
  result
end
```

## Scala

```scala
object Solution {
  def letterCasePermutation(s: String): List[String] = {
    val result = scala.collection.mutable.ListBuffer[String]()
    val n = s.length

    def backtrack(idx: Int, sb: StringBuilder): Unit = {
      if (idx == n) {
        result += sb.toString()
        return
      }
      val ch = s.charAt(idx)
      if (ch.isLetter) {
        // lowercase branch
        sb.append(ch.toLower)
        backtrack(idx + 1, sb)
        sb.setLength(sb.length - 1)

        // uppercase branch
        sb.append(ch.toUpper)
        backtrack(idx + 1, sb)
        sb.setLength(sb.length - 1)
      } else {
        sb.append(ch)
        backtrack(idx + 1, sb)
        sb.setLength(sb.length - 1)
      }
    }

    backtrack(0, new StringBuilder())
    result.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn letter_case_permutation(s: String) -> Vec<String> {
        let mut res: Vec<String> = vec![String::new()];
        for ch in s.chars() {
            if ch.is_ascii_digit() {
                for r in &mut res {
                    r.push(ch);
                }
            } else {
                let mut next: Vec<String> = Vec::with_capacity(res.len() * 2);
                for r in &res {
                    let mut lower = r.clone();
                    lower.push(ch.to_ascii_lowercase());
                    next.push(lower);
                    let mut upper = r.clone();
                    upper.push(ch.to_ascii_uppercase());
                    next.push(upper);
                }
                res = next;
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (letter-case-permutation s)
  (-> string? (listof string?))
  (let loop ((i 0))
    (if (= i (string-length s))
        (list "")
        (let* ((c (string-ref s i))
               (rest (loop (+ i 1))))
          (cond
            [(char-alphabetic? c)
             (define lower (char-downcase c))
             (define upper (char-upcase c))
             (append
              (map (lambda (suffix) (string-append (string lower) suffix)) rest)
              (if (char=? lower upper)
                  '()
                  (map (lambda (suffix) (string-append (string upper) suffix)) rest)))]
            [else
             (map (lambda (suffix) (string-append (string c) suffix)) rest)])))) )
```

## Erlang

```erlang
-module(solution).
-export([letter_case_permutation/1]).

-spec letter_case_permutation(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
letter_case_permutation(S) ->
    Chars = unicode:characters_to_list(S),
    permute(Chars).

%% internal helpers
permute([]) ->
    [<<>>];
permute([H|T]) ->
    Rest = permute(T),
    case is_letter(H) of
        true ->
            Lower = if $A =< H, H =< $Z -> H + 16#20; true -> H end,
            Upper = if $a =< H, H =< $z -> H - 16#20; true -> H end,
            [ <<Lower/utf8, RestBin/binary>> || RestBin <- Rest ] ++
            [ <<Upper/utf8, RestBin/binary>> || RestBin <- Rest ];
        false ->
            [ <<H/utf8, RestBin/binary>> || RestBin <- Rest ]
    end.

is_letter(C) when $a =< C, C =< $z -> true;
is_letter(C) when $A =< C, C =< $Z -> true;
is_letter(_) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec letter_case_permutation(s :: String.t) :: [String.t]
  def letter_case_permutation(s) do
    chars = String.to_charlist(s)
    dfs(chars, [])
  end

  defp dfs([], acc), do: [List.to_string(Enum.reverse(acc))]

  defp dfs([h | t], acc) when h >= ?0 and h <= ?9 do
    dfs(t, [h | acc])
  end

  defp dfs([h | t], acc) do
    lower = if h >= ?a and h <= ?z, do: h, else: h + 32
    upper = if h >= ?A and h <= ?Z, do: h, else: h - 32
    dfs(t, [lower | acc]) ++ dfs(t, [upper | acc])
  end
end
```
