# 2828. Check if a String Is an Acronym of Words

## Cpp

```cpp
class Solution {
public:
    bool isAcronym(vector<string>& words, string s) {
        if (words.size() != s.size()) return false;
        for (size_t i = 0; i < words.size(); ++i) {
            if (words[i].empty() || words[i][0] != s[i]) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isAcronym(java.util.List<String> words, String s) {
        StringBuilder sb = new StringBuilder();
        for (String word : words) {
            sb.append(word.charAt(0));
        }
        return sb.toString().equals(s);
    }
}
```

## Python

```python
class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        return ''.join(word[0] for word in words) == s
```

## Python3

```python
from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        for w, ch in zip(words, s):
            if w[0] != ch:
                return False
        return True
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool isAcronym(char** words, int wordsSize, char* s) {
    if ((int)strlen(s) != wordsSize) return false;
    for (int i = 0; i < wordsSize; ++i) {
        if (!words[i] || words[i][0] != s[i]) return false;
    }
    return true;
}
```

## Csharp

```csharp
using System.Collections.Generic;
using System.Text;

public class Solution {
    public bool IsAcronym(IList<string> words, string s) {
        var sb = new StringBuilder();
        foreach (var word in words) {
            if (word.Length > 0) {
                sb.Append(word[0]);
            }
        }
        return sb.ToString() == s;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {string} s
 * @return {boolean}
 */
var isAcronym = function(words, s) {
    if (words.length !== s.length) return false;
    for (let i = 0; i < words.length; ++i) {
        if (words[i][0] !== s[i]) return false;
    }
    return true;
};
```

## Typescript

```typescript
function isAcronym(words: string[], s: string): boolean {
    if (s.length !== words.length) return false;
    for (let i = 0; i < words.length; i++) {
        if (words[i][0] !== s[i]) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $s
     * @return Boolean
     */
    function isAcronym($words, $s) {
        $acronym = '';
        foreach ($words as $word) {
            $acronym .= $word[0];
        }
        return $acronym === $s;
    }
}
```

## Swift

```swift
class Solution {
    func isAcronym(_ words: [String], _ s: String) -> Bool {
        var acronym = ""
        for word in words {
            if let firstChar = word.first {
                acronym.append(firstChar)
            }
        }
        return acronym == s
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isAcronym(words: List<String>, s: String): Boolean {
        if (words.size != s.length) return false
        val sb = StringBuilder()
        for (word in words) {
            sb.append(word[0])
        }
        return sb.toString() == s
    }
}
```

## Dart

```dart
class Solution {
  bool isAcronym(List<String> words, String s) {
    if (words.length != s.length) return false;
    for (int i = 0; i < words.length; i++) {
      if (words[i].isEmpty || words[i][0] != s[i]) return false;
    }
    return true;
  }
}
```

## Golang

```go
func isAcronym(words []string, s string) bool {
	if len(words) != len(s) {
		return false
	}
	for i, w := range words {
		if len(w) == 0 || w[0] != s[i] {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def is_acronym(words, s)
  acronym = words.map { |word| word[0] }.join
  acronym == s
end
```

## Scala

```scala
object Solution {
    def isAcronym(words: List[String], s: String): Boolean = {
        val acronym = words.map(_.charAt(0)).mkString
        acronym == s
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_acronym(words: Vec<String>, s: String) -> bool {
        if words.len() != s.len() {
            return false;
        }
        let s_bytes = s.as_bytes();
        for (i, w) in words.iter().enumerate() {
            // words[i] guaranteed non‑empty by constraints
            if w.as_bytes()[0] != s_bytes[i] {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (is-acronym words s)
  (-> (listof string?) string? boolean?)
  (let ([acronym (list->string (map (lambda (w) (string-ref w 0)) words))])
    (equal? acronym s)))
```

## Erlang

```erlang
-module(solution).
-export([is_acronym/2]).

-spec is_acronym(Words :: [unicode:unicode_binary()], S :: unicode:unicode_binary()) -> boolean().
is_acronym(Words, S) ->
    Acronym = list_to_binary(
        [ begin
              <<C,_/binary>> = Word,
              C
          end || Word <- Words]),
    Acronym =:= S.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_acronym(words :: [String.t()], s :: String.t()) :: boolean()
  def is_acronym(words, s) do
    acronym =
      words
      |> Enum.map(&String.first/1)
      |> Enum.join()

    acronym == s
  end
end
```
