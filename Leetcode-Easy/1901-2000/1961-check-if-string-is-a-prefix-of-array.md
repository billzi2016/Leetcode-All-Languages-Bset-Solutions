# 1961. Check If String Is a Prefix of Array

## Cpp

```cpp
class Solution {
public:
    bool isPrefixString(string s, vector<string>& words) {
        int pos = 0;
        for (const string& w : words) {
            if (pos + (int)w.size() > (int)s.size()) return false;
            if (s.compare(pos, w.size(), w) != 0) return false;
            pos += w.size();
            if (pos == (int)s.size()) return true;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean isPrefixString(String s, String[] words) {
        StringBuilder sb = new StringBuilder();
        for (String w : words) {
            sb.append(w);
            int len = sb.length();
            if (len == s.length()) {
                return sb.toString().equals(s);
            }
            if (len > s.length()) {
                return false;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        prefix = ""
        for w in words:
            prefix += w
            if prefix == s:
                return True
            if len(prefix) > len(s):
                # No need to continue, cannot match further
                break
        return False
```

## Python3

```python
from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = []
        total_len = 0
        target_len = len(s)
        for w in words:
            total_len += len(w)
            if total_len > target_len:
                # No need to continue, cannot match exactly
                return False
            prefix.append(w)
            if total_len == target_len:
                return "".join(prefix) == s
        return False
```

## C

```c
#include <stdbool.h>

bool isPrefixString(char* s, char** words, int wordsSize) {
    int i = 0; // index for string s
    for (int w = 0; w < wordsSize; ++w) {
        char *word = words[w];
        for (int j = 0; word[j] != '\0'; ++j) {
            if (s[i] == '\0' || s[i] != word[j]) {
                return false;
            }
            ++i;
        }
        if (s[i] == '\0') {
            return true;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsPrefixString(string s, string[] words) {
        var sb = new System.Text.StringBuilder();
        foreach (var w in words) {
            sb.Append(w);
            if (sb.Length == s.Length) {
                return sb.ToString() == s;
            }
            if (sb.Length > s.Length) {
                return false;
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
 * @param {string[]} words
 * @return {boolean}
 */
var isPrefixString = function(s, words) {
    let prefix = "";
    for (const w of words) {
        prefix += w;
        if (prefix.length === s.length) {
            return prefix === s;
        }
        if (prefix.length > s.length) {
            break;
        }
    }
    return false;
};
```

## Typescript

```typescript
function isPrefixString(s: string, words: string[]): boolean {
    let prefix = "";
    for (const word of words) {
        prefix += word;
        if (prefix === s) return true;
        if (prefix.length > s.length) break;
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String[] $words
     * @return Boolean
     */
    function isPrefixString($s, $words) {
        $prefix = '';
        foreach ($words as $word) {
            $prefix .= $word;
            if ($prefix === $s) {
                return true;
            }
            if (strlen($prefix) > strlen($s)) {
                break;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func isPrefixString(_ s: String, _ words: [String]) -> Bool {
        var built = ""
        for word in words {
            built += word
            if built == s { return true }
            if built.count > s.count { break }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPrefixString(s: String, words: Array<String>): Boolean {
        val sb = StringBuilder()
        for (w in words) {
            sb.append(w)
            if (sb.length > s.length) return false
            if (sb.toString() == s) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool isPrefixString(String s, List<String> words) {
    StringBuffer sb = StringBuffer();
    for (var w in words) {
      sb.write(w);
      if (sb.length == s.length && sb.toString() == s) return true;
      if (sb.length > s.length) break;
    }
    return false;
  }
}
```

## Golang

```go
func isPrefixString(s string, words []string) bool {
	idx := 0
	for _, w := range words {
		if len(w) > len(s)-idx {
			return false
		}
		if s[idx:idx+len(w)] != w {
			return false
		}
		idx += len(w)
		if idx == len(s) {
			return true
		}
	}
	return false
}
```

## Ruby

```ruby
def is_prefix_string(s, words)
  prefix = ''
  words.each do |word|
    prefix << word
    return true if prefix == s
    return false if prefix.length > s.length
  end
  false
end
```

## Scala

```scala
object Solution {
    def isPrefixString(s: String, words: Array[String]): Boolean = {
        val sb = new StringBuilder
        for (w <- words) {
            sb.append(w)
            if (sb.length == s.length && sb.toString == s) return true
            if (sb.length > s.length) return false
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_prefix_string(s: String, words: Vec<String>) -> bool {
        let mut prefix = String::new();
        for w in words {
            prefix.push_str(&w);
            if prefix == s {
                return true;
            }
            if prefix.len() > s.len() {
                break;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (is-prefix-string s words)
  (-> string? (listof string?) boolean?)
  (let loop ((acc "") (rest words))
    (cond
      [(string=? acc s) #t]
      [(or (null? rest)
           (> (string-length acc) (string-length s))) #f]
      [else (loop (string-append acc (car rest)) (cdr rest))])))
```

## Erlang

```erlang
-module(solution).
-export([is_prefix_string/2]).

-spec is_prefix_string(S :: unicode:unicode_binary(), Words :: [unicode:unicode_binary()]) -> boolean().
is_prefix_string(S, Words) ->
    go(<<>>, S, Words).

go(_Acc, _S, []) -> false;
go(Acc, S, [Word|Rest]) ->
    NewAcc = <<Acc/binary, Word/binary>>,
    case NewAcc of
        S -> true;
        _ -> go(NewAcc, S, Rest)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_prefix_string(s :: String.t(), words :: [String.t()]) :: boolean()
  def is_prefix_string(s, words) do
    check_prefix(s, words, "")
  end

  defp check_prefix(_s, [], _acc), do: false

  defp check_prefix(s, [w | rest], acc) do
    new_acc = acc <> w

    cond do
      new_acc == s ->
        true

      String.length(new_acc) > String.length(s) ->
        false

      not String.starts_with?(s, new_acc) ->
        false

      true ->
        check_prefix(s, rest, new_acc)
    end
  end
end
```
