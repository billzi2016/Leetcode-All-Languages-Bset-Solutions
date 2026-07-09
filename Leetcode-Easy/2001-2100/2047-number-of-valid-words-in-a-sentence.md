# 2047. Number of Valid Words in a Sentence

## Cpp

```cpp
class Solution {
public:
    bool isValid(const string& token) {
        int n = token.size();
        if (n == 0) return false;
        int hyphenCnt = 0, punctCnt = 0;
        for (int i = 0; i < n; ++i) {
            char c = token[i];
            if (c >= '0' && c <= '9') return false;
            else if (c == '-') {
                ++hyphenCnt;
                if (hyphenCnt > 1) return false;
                if (i == 0 || i == n - 1) return false;
                if (!isalpha(token[i - 1]) || !isalpha(token[i + 1])) return false;
            } else if (c == '!' || c == '.' || c == ',') {
                ++punctCnt;
                if (punctCnt > 1) return false;
                if (i != n - 1) return false;
            } else if (isalpha(c)) {
                continue;
            } else {
                return false;
            }
        }
        return true;
    }

    int countValidWords(string sentence) {
        int ans = 0;
        string token;
        std::stringstream ss(sentence);
        while (ss >> token) {
            if (isValid(token)) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countValidWords(String sentence) {
        int validCount = 0;
        String[] tokens = sentence.split(" ");
        for (String token : tokens) {
            if (token.isEmpty()) continue;
            if (isValid(token)) validCount++;
        }
        return validCount;
    }

    private boolean isValid(String token) {
        int hyphenCnt = 0, punctCnt = 0;
        int n = token.length();
        for (int i = 0; i < n; i++) {
            char c = token.charAt(i);
            if (c >= '0' && c <= '9') return false;
            if (c == '-') {
                hyphenCnt++;
                if (hyphenCnt > 1) return false;
                if (i == 0 || i == n - 1) return false;
                char prev = token.charAt(i - 1);
                char next = token.charAt(i + 1);
                if (!isLetter(prev) || !isLetter(next)) return false;
            } else if (c == '!' || c == '.' || c == ',') {
                punctCnt++;
                if (punctCnt > 1) return false;
                if (i != n - 1) return false;
            } else if (!isLetter(c)) {
                return false;
            }
        }
        return true;
    }

    private boolean isLetter(char c) {
        return c >= 'a' && c <= 'z';
    }
}
```

## Python

```python
class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        def is_valid(token):
            hyphen_used = False
            punct_used = False
            n = len(token)
            for i, ch in enumerate(token):
                if ch.isdigit():
                    return False
                if ch == '-':
                    if hyphen_used:
                        return False
                    # hyphen must be surrounded by letters
                    if i == 0 or i == n - 1:
                        return False
                    if not token[i-1].isalpha() or not token[i+1].isalpha():
                        return False
                    hyphen_used = True
                elif ch in "!.,": 
                    if punct_used:
                        return False
                    # punctuation must be at the end
                    if i != n - 1:
                        return False
                    punct_used = True
                else:
                    # letters are always fine
                    pass
            return True

        count = 0
        for token in sentence.split():
            if is_valid(token):
                count += 1
        return count
```

## Python3

```python
class Solution:
    def countValidWords(self, sentence: str) -> int:
        def is_valid(token: str) -> bool:
            if not token:
                return False
            hyphen_cnt = 0
            punct_cnt = 0
            n = len(token)
            for i, ch in enumerate(token):
                if ch.isdigit():
                    return False
                if ch == '-':
                    hyphen_cnt += 1
                    if hyphen_cnt > 1:
                        return False
                    # must be surrounded by letters
                    if i == 0 or i == n - 1:
                        return False
                    if not token[i - 1].isalpha() or not token[i + 1].isalpha():
                        return False
                elif ch in "!.,": 
                    punct_cnt += 1
                    if punct_cnt > 1:
                        return False
                    # punctuation must be at the end
                    if i != n - 1:
                        return False
                else:
                    # letters are always fine; other chars not expected per constraints
                    pass
            return True

        count = 0
        for token in sentence.split(' '):
            if is_valid(token):
                count += 1
        return count
```

## C

```c
#include <string.h>
#include <stdbool.h>

static bool isValidToken(const char *s, int len) {
    int hyphenCount = 0, punctCount = 0;
    for (int i = 0; i < len; ++i) {
        char c = s[i];
        if (c >= 'a' && c <= 'z') {
            continue;
        } else if (c >= '0' && c <= '9') {
            return false;
        } else if (c == '-') {
            hyphenCount++;
            if (hyphenCount > 1) return false;
            if (i == 0 || i == len - 1) return false;               // must be surrounded
            if (!(s[i - 1] >= 'a' && s[i - 1] <= 'z')) return false;
            if (!(s[i + 1] >= 'a' && s[i + 1] <= 'z')) return false;
        } else if (c == '!' || c == '.' || c == ',') {
            punctCount++;
            if (punctCount > 1) return false;
            if (i != len - 1) return false;                         // must be at end
        } else {
            return false;                                            // unexpected character
        }
    }
    return true;
}

int countValidWords(char* sentence) {
    int n = strlen(sentence);
    int i = 0, result = 0;
    while (i < n) {
        while (i < n && sentence[i] == ' ') ++i;          // skip spaces
        if (i >= n) break;
        int start = i;
        while (i < n && sentence[i] != ' ') ++i;          // token end
        int len = i - start;
        if (len > 0 && isValidToken(sentence + start, len))
            ++result;
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int CountValidWords(string sentence) {
        if (string.IsNullOrEmpty(sentence)) return 0;
        var tokens = sentence.Split(' ', System.StringSplitOptions.RemoveEmptyEntries);
        int validCount = 0;
        foreach (var token in tokens) {
            if (IsValid(token))
                validCount++;
        }
        return validCount;
    }

    private bool IsValid(string token) {
        bool hyphenSeen = false;
        bool punctSeen = false;
        int n = token.Length;
        for (int i = 0; i < n; i++) {
            char c = token[i];
            if (c >= '0' && c <= '9')
                return false;
            else if (c == '-') {
                if (hyphenSeen) return false;
                // hyphen must be surrounded by letters
                if (i == 0 || i == n - 1) return false;
                char prev = token[i - 1];
                char next = token[i + 1];
                if (!IsLetter(prev) || !IsLetter(next)) return false;
                hyphenSeen = true;
            } else if (c == '!' || c == '.' || c == ',') {
                // punctuation must be at the end
                if (i != n - 1) return false;
                if (punctSeen) return false;
                punctSeen = true;
            } else if (!IsLetter(c)) {
                // any other character is invalid
                return false;
            }
        }
        return true;
    }

    private bool IsLetter(char c) => c >= 'a' && c <= 'z';
}
```

## Javascript

```javascript
/**
 * @param {string} sentence
 * @return {number}
 */
var countValidWords = function(sentence) {
    const tokens = sentence.split(' ');
    let validCount = 0;
    
    const isLetter = (c) => c >= 'a' && c <= 'z';
    
    for (const token of tokens) {
        if (token.length === 0) continue;
        let hyphenCnt = 0, punctCnt = 0;
        let ok = true;
        const n = token.length;
        
        for (let i = 0; i < n && ok; i++) {
            const ch = token[i];
            if (isLetter(ch)) {
                continue;
            } else if (ch === '-') {
                hyphenCnt++;
                if (hyphenCnt > 1) { ok = false; break; }
                // must be surrounded by letters
                if (i === 0 || i === n - 1) { ok = false; break; }
                if (!isLetter(token[i - 1]) || !isLetter(token[i + 1])) {
                    ok = false; break;
                }
            } else if (ch === '!' || ch === '.' || ch === ',') {
                punctCnt++;
                if (punctCnt > 1) { ok = false; break; }
                // must be at the end
                if (i !== n - 1) { ok = false; break; }
            } else {
                // digit or any other character
                ok = false;
                break;
            }
        }
        
        if (ok) validCount++;
    }
    
    return validCount;
};
```

## Typescript

```typescript
function countValidWords(sentence: string): number {
    const tokens = sentence.split(' ');
    let validCount = 0;

    for (const token of tokens) {
        if (token.length === 0) continue;
        if (isValid(token)) validCount++;
    }

    return validCount;
}

function isValid(word: string): boolean {
    let hyphenSeen = false;
    let punctSeen = false;
    const n = word.length;

    for (let i = 0; i < n; i++) {
        const ch = word[i];
        const code = ch.charCodeAt(0);

        // digit check
        if (code >= 48 && code <= 57) return false;

        // hyphen handling
        if (ch === '-') {
            if (hyphenSeen) return false;
            // must be surrounded by letters
            if (i === 0 || i === n - 1) return false;
            const prev = word[i - 1];
            const next = word[i + 1];
            if (!isLetter(prev) || !isLetter(next)) return false;
            hyphenSeen = true;
            continue;
        }

        // punctuation handling
        if (ch === '!' || ch === '.' || ch === ',') {
            if (punctSeen) return false;
            // must be at the end
            if (i !== n - 1) return false;
            punctSeen = true;
            continue;
        }

        // letter check
        if (!isLetter(ch)) return false; // any other character invalid
    }
    return true;
}

function isLetter(ch: string): boolean {
    const code = ch.charCodeAt(0);
    return code >= 97 && code <= 122;
}
```

## Php

```php
class Solution {

    /**
     * @param String $sentence
     * @return Integer
     */
    function countValidWords($sentence) {
        $tokens = preg_split('/\s+/', trim($sentence));
        $validCount = 0;

        foreach ($tokens as $token) {
            if ($token === '') continue;
            $len = strlen($token);
            $hyphenCnt = 0;
            $punctCnt = 0;
            $isValid = true;

            for ($i = 0; $i < $len; $i++) {
                $ch = $token[$i];

                if (ctype_digit($ch)) {
                    $isValid = false;
                    break;
                } elseif ($ch === '-') {
                    $hyphenCnt++;
                    if ($hyphenCnt > 1) { $isValid = false; break; }
                    // hyphen must be surrounded by letters
                    if ($i == 0 || $i == $len - 1) { $isValid = false; break; }
                    $prev = $token[$i - 1];
                    $next = $token[$i + 1];
                    if (!ctype_lower($prev) || !ctype_lower($next)) { $isValid = false; break; }
                } elseif ($ch === '!' || $ch === '.' || $ch === ',') {
                    $punctCnt++;
                    if ($punctCnt > 1) { $isValid = false; break; }
                    // punctuation must be at the end
                    if ($i != $len - 1) { $isValid = false; break; }
                } else {
                    // must be a lowercase letter
                    if (!ctype_lower($ch)) {
                        $isValid = false;
                        break;
                    }
                }
            }

            if ($isValid) $validCount++;
        }

        return $validCount;
    }
}
```

## Swift

```swift
class Solution {
    func countValidWords(_ sentence: String) -> Int {
        let tokens = sentence.split(separator: " ")
        var result = 0
        for tokenSub in tokens {
            if isValid(String(tokenSub)) {
                result += 1
            }
        }
        return result
    }

    private func isValid(_ token: String) -> Bool {
        var hyphenCount = 0
        var punctCount = 0
        let chars = Array(token)
        for i in 0..<chars.count {
            let c = chars[i]
            if let ascii = c.unicodeScalars.first?.value, ascii >= 97 && ascii <= 122 {
                continue
            } else if c == "-" {
                hyphenCount += 1
                if hyphenCount > 1 { return false }
                if i == 0 || i == chars.count - 1 { return false }
                let prev = chars[i - 1]
                let next = chars[i + 1]
                guard let pAscii = prev.unicodeScalars.first?.value, pAscii >= 97 && pAscii <= 122 else { return false }
                guard let nAscii = next.unicodeScalars.first?.value, nAscii >= 97 && nAscii <= 122 else { return false }
            } else if c == "!" || c == "." || c == "," {
                punctCount += 1
                if punctCount > 1 { return false }
                if i != chars.count - 1 { return false }
            } else {
                return false
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countValidWords(sentence: String): Int {
        var validCount = 0
        for (token in sentence.split(" ")) {
            if (token.isEmpty()) continue
            if (isValid(token)) validCount++
        }
        return validCount
    }

    private fun isValid(token: String): Boolean {
        var hyphenCnt = 0
        var punctCnt = 0
        val n = token.length
        for (i in 0 until n) {
            val c = token[i]
            when {
                c.isDigit() -> return false
                c == '-' -> {
                    hyphenCnt++
                    if (hyphenCnt > 1) return false
                    // hyphen must be surrounded by letters
                    if (i == 0 || i == n - 1) return false
                    if (!token[i - 1].isLetter() || !token[i + 1].isLetter()) return false
                }
                c == '!' || c == '.' || c == ',' -> {
                    punctCnt++
                    if (punctCnt > 1) return false
                    // punctuation must be at the end
                    if (i != n - 1) return false
                }
                else -> {
                    // letter, nothing to check
                }
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  int countValidWords(String sentence) {
    int count = 0;
    for (var token in sentence.split(' ')) {
      if (token.isEmpty) continue;
      if (_isValid(token)) count++;
    }
    return count;
  }

  bool _isValid(String token) {
    int hyphenCount = 0;
    int punctCount = 0;
    int n = token.length;
    for (int i = 0; i < n; i++) {
      int code = token.codeUnitAt(i);
      if (code >= 97 && code <= 122) {
        // lowercase letter
        continue;
      } else if (code == 45) { // '-'
        hyphenCount++;
        if (hyphenCount > 1) return false;
        if (i == 0 || i == n - 1) return false;
        int prev = token.codeUnitAt(i - 1);
        int next = token.codeUnitAt(i + 1);
        if (!(prev >= 97 && prev <= 122)) return false;
        if (!(next >= 97 && next <= 122)) return false;
      } else if (code == 33 || code == 46 || code == 44) { // '!', '.', ','
        punctCount++;
        if (punctCount > 1) return false;
        if (i != n - 1) return false; // punctuation must be at the end
      } else {
        // digit or any other character
        return false;
      }
    }
    return true;
  }
}
```

## Golang

```go
import "strings"

func countValidWords(sentence string) int {
	tokens := strings.Fields(sentence)
	count := 0
	for _, t := range tokens {
		if isValid(t) {
			count++
		}
	}
	return count
}

func isValid(s string) bool {
	n := len(s)
	hyphenCnt, punctCnt := 0, 0
	for i := 0; i < n; i++ {
		c := s[i]
		if c >= '0' && c <= '9' {
			return false
		} else if c == '-' {
			hyphenCnt++
			if hyphenCnt > 1 || i == 0 || i == n-1 {
				return false
			}
			if !(s[i-1] >= 'a' && s[i-1] <= 'z') || !(s[i+1] >= 'a' && s[i+1] <= 'z') {
				return false
			}
		} else if c == '!' || c == '.' || c == ',' {
			punctCnt++
			if punctCnt > 1 || i != n-1 {
				return false
			}
		} else if c >= 'a' && c <= 'z' {
			// valid letter, continue
		} else {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def count_valid_words(sentence)
  def valid_token?(token)
    return false if token.empty?
    hyphen_used = false
    punct_used = false
    n = token.length

    token.each_char.with_index do |ch, i|
      case ch
      when 'a'..'z'
        next
      when '-'
        return false if hyphen_used
        return false if i == 0 || i == n - 1
        prev = token[i - 1]
        nxt = token[i + 1]
        return false unless ('a'..'z').include?(prev) && ('a'..'z').include?(nxt)
        hyphen_used = true
      when '!', '.', ','
        return false if punct_used
        return false unless i == n - 1
        punct_used = true
      else
        # digit or any other character
        return false
      end
    end
    true
  end

  count = 0
  sentence.split(' ').each do |token|
    count += 1 if valid_token?(token)
  end
  count
end
```

## Scala

```scala
object Solution {
  def countValidWords(sentence: String): Int = {
    val tokens = sentence.split(" ")
    var cnt = 0
    for (t <- tokens) {
      if (t.nonEmpty && isValid(t)) cnt += 1
    }
    cnt
  }

  private def isValid(token: String): Boolean = {
    var hyphenCnt = 0
    var punctCnt = 0
    val n = token.length
    for (i <- 0 until n) {
      val c = token.charAt(i)
      if (c >= '0' && c <= '9') return false
      else if (c == '-') {
        hyphenCnt += 1
        if (hyphenCnt > 1) return false
        if (i == 0 || i == n - 1) return false
        val prev = token.charAt(i - 1)
        val next = token.charAt(i + 1)
        if (!isLetter(prev) || !isLetter(next)) return false
      } else if (c == '!' || c == '.' || c == ',') {
        punctCnt += 1
        if (punctCnt > 1) return false
        if (i != n - 1) return false
      } else {
        if (!isLetter(c)) return false
      }
    }
    true
  }

  private def isLetter(ch: Char): Boolean = ch >= 'a' && ch <= 'z'
}
```

## Rust

```rust
impl Solution {
    pub fn count_valid_words(sentence: String) -> i32 {
        sentence
            .split_whitespace()
            .filter(|w| Self::is_valid(w))
            .count() as i32
    }

    fn is_valid(word: &str) -> bool {
        let bytes = word.as_bytes();
        let mut hyphen_cnt = 0;
        let mut punct_cnt = 0;

        for (i, &b) in bytes.iter().enumerate() {
            let c = b as char;
            if c.is_ascii_digit() {
                return false;
            } else if c == '-' {
                hyphen_cnt += 1;
                if hyphen_cnt > 1 {
                    return false;
                }
                // must have letters on both sides
                if i == 0 || i + 1 == bytes.len() {
                    return false;
                }
                let prev = bytes[i - 1] as char;
                let next = bytes[i + 1] as char;
                if !prev.is_ascii_lowercase() || !next.is_ascii_lowercase() {
                    return false;
                }
            } else if c == '!' || c == '.' || c == ',' {
                punct_cnt += 1;
                if punct_cnt > 1 {
                    return false;
                }
                // punctuation must be at the end
                if i != bytes.len() - 1 {
                    return false;
                }
            } else if c.is_ascii_lowercase() {
                continue;
            } else {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define (letter? c)
  (and (char>=? c #\a) (char<=? c #\z)))

(define (punct? c)
  (or (char=? c #\!)
      (char=? c #\.)
      (char=? c #\,)))

(define (valid-token? token)
  (let ((len (string-length token)))
    (if (= len 0) 
        #f
        (let loop ((i 0) (hyph 0) (punc 0))
          (cond
            [(= i len) #t]
            [else
             (define c (string-ref token i))
             (cond
               [(char-numeric? c) #f]
               [(char=? c #\-)
                (if (or (> hyph 0)
                        (= i 0)
                        (= i (sub1 len))
                        (not (letter? (string-ref token (sub1 i))))
                        (not (letter? (string-ref token (+ i 1)))))
                    #f
                    (loop (add1 i) (add1 hyph) punc))]
               [(punct? c)
                (if (or (> punc 0) (not (= i (sub1 len))))
                    #f
                    (loop (add1 i) hyph (add1 punc)))]
               [(letter? c) (loop (add1 i) hyph punc)]
               [else #f])])))))

(define/contract (count-valid-words sentence)
  (-> string? exact-integer?)
  (let* ((tokens (string-split sentence " " #:skip-empty? #t)))
    (for/sum ([tok tokens])
      (if (valid-token? tok) 1 0))))
```

## Erlang

```erlang
-spec count_valid_words(Sentence :: unicode:unicode_binary()) -> integer().
count_valid_words(Sentence) ->
    Tokens = string:tokens(unicode:characters_to_list(Sentence), " "),
    Pattern = "^[a-z]+(-[a-z]+)?[!.,]?$|^[!.,]$",
    lists:foldl(
        fun(Token, Acc) ->
            case re:run(Token, Pattern, [{capture, none}]) of
                match -> Acc + 1;
                nomatch -> Acc
            end
        end,
        0,
        Tokens
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_valid_words(sentence :: String.t()) :: integer()
  def count_valid_words(sentence) do
    regex = ~r/^([a-z]+(-[a-z]+)?)?[!.,]?$/

    sentence
    |> String.split(" ", trim: true)
    |> Enum.count(fn token -> Regex.match?(regex, token) end)
  end
end
```
