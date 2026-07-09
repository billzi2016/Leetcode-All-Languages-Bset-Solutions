# 2108. Find First Palindromic String in the Array

## Cpp

```cpp
class Solution {
public:
    bool isPalindrome(const std::string& s) {
        int i = 0, j = (int)s.size() - 1;
        while (i < j) {
            if (s[i] != s[j]) return false;
            ++i;
            --j;
        }
        return true;
    }

    std::string firstPalindrome(std::vector<std::string>& words) {
        for (const auto& w : words) {
            if (isPalindrome(w)) return w;
        }
        return "";
    }
};
```

## Java

```java
class Solution {
    public String firstPalindrome(String[] words) {
        for (String word : words) {
            if (isPalindrome(word)) {
                return word;
            }
        }
        return "";
    }

    private boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left++) != s.charAt(right--)) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for s in words:
            if s == s[::-1]:
                return s
        return ""
```

## Python3

```python
from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ""
```

## C

```c
#include <string.h>
#include <stdbool.h>

char* firstPalindrome(char** words, int wordsSize) {
    for (int i = 0; i < wordsSize; ++i) {
        char *s = words[i];
        int left = 0;
        int right = (int)strlen(s) - 1;
        bool isPal = true;
        while (left < right) {
            if (s[left] != s[right]) {
                isPal = false;
                break;
            }
            ++left;
            --right;
        }
        if (isPal) return s;
    }
    static char empty[] = "";
    return empty;
}
```

## Csharp

```csharp
public class Solution
{
    public string FirstPalindrome(string[] words)
    {
        foreach (var word in words)
        {
            if (IsPalindrome(word))
                return word;
        }
        return "";
    }

    private bool IsPalindrome(string s)
    {
        int left = 0, right = s.Length - 1;
        while (left < right)
        {
            if (s[left] != s[right])
                return false;
            left++;
            right--;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {string}
 */
var firstPalindrome = function(words) {
    const isPal = (s) => {
        let i = 0, j = s.length - 1;
        while (i < j) {
            if (s[i] !== s[j]) return false;
            i++;
            j--;
        }
        return true;
    };
    
    for (const w of words) {
        if (isPal(w)) return w;
    }
    return "";
};
```

## Typescript

```typescript
function firstPalindrome(words: string[]): string {
    const isPalindrome = (s: string): boolean => {
        let left = 0, right = s.length - 1;
        while (left < right) {
            if (s[left] !== s[right]) return false;
            left++;
            right--;
        }
        return true;
    };
    for (const w of words) {
        if (isPalindrome(w)) return w;
    }
    return "";
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return String
     */
    function firstPalindrome($words) {
        foreach ($words as $s) {
            if ($s === strrev($s)) {
                return $s;
            }
        }
        return "";
    }
}
```

## Swift

```swift
class Solution {
    func firstPalindrome(_ words: [String]) -> String {
        for word in words {
            if word == String(word.reversed()) {
                return word
            }
        }
        return ""
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun firstPalindrome(words: Array<String>): String {
        for (word in words) {
            if (isPalindrome(word)) return word
        }
        return ""
    }

    private fun isPalindrome(s: String): Boolean {
        var left = 0
        var right = s.length - 1
        while (left < right) {
            if (s[left] != s[right]) return false
            left++
            right--
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  String firstPalindrome(List<String> words) {
    for (var word in words) {
      if (_isPalindrome(word)) {
        return word;
      }
    }
    return "";
  }

  bool _isPalindrome(String s) {
    int left = 0, right = s.length - 1;
    while (left < right) {
      if (s.codeUnitAt(left) != s.codeUnitAt(right)) {
        return false;
      }
      left++;
      right--;
    }
    return true;
  }
}
```

## Golang

```go
func firstPalindrome(words []string) string {
	for _, w := range words {
		if isPalindrome(w) {
			return w
		}
	}
	return ""
}

func isPalindrome(s string) bool {
	i, j := 0, len(s)-1
	for i < j {
		if s[i] != s[j] {
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
def first_palindrome(words)
  words.each do |s|
    i = 0
    j = s.length - 1
    palindrome = true
    while i < j
      if s[i] != s[j]
        palindrome = false
        break
      end
      i += 1
      j -= 1
    end
    return s if palindrome
  end
  ""
end
```

## Scala

```scala
object Solution {
    def firstPalindrome(words: Array[String]): String = {
        for (w <- words) {
            var i = 0
            var j = w.length - 1
            var ok = true
            while (i < j && ok) {
                if (w.charAt(i) != w.charAt(j)) ok = false
                i += 1
                j -= 1
            }
            if (ok) return w
        }
        ""
    }
}
```

## Rust

```rust
impl Solution {
    pub fn first_palindrome(words: Vec<String>) -> String {
        for w in words {
            if Self::is_pal(&w) {
                return w;
            }
        }
        String::new()
    }

    fn is_pal(s: &str) -> bool {
        let bytes = s.as_bytes();
        let mut i = 0usize;
        let mut j = bytes.len() - 1;
        while i < j {
            if bytes[i] != bytes[j] {
                return false;
            }
            i += 1;
            j -= 1;
        }
        true
    }
}
```

## Racket

```racket
#lang racket

(require rackunit)

(define (pal? s)
  (let loop ((i 0) (j (- (string-length s) 1)))
    (cond [(>= i j) #t]
          [(char=? (string-ref s i) (string-ref s j))
           (loop (+ i 1) (- j 1))]
          [else #f])))

(define/contract (first-palindrome words)
  (-> (listof string?) string?)
  (let loop ((lst words))
    (cond [(null? lst) ""]
          [else (let ((s (car lst)))
                  (if (pal? s) s (loop (cdr lst))))])))
```

## Erlang

```erlang
-spec first_palindrome(Words :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
first_palindrome([]) ->
    <<>>;
first_palindrome([H|T]) ->
    case is_palindrome(H) of
        true -> H;
        false -> first_palindrome(T)
    end.

is_palindrome(Bin) ->
    List = unicode:characters_to_list(Bin),
    List == lists:reverse(List).
```

## Elixir

```elixir
defmodule Solution do
  @spec first_palindrome(words :: [String.t]) :: String.t
  def first_palindrome(words) do
    Enum.find_value(words, "", fn word ->
      if word == String.reverse(word), do: word, else: nil
    end)
  end
end
```
