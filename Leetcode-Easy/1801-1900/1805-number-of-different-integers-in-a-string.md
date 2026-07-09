# 1805. Number of Different Integers in a String

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numDifferentIntegers(string word) {
        unordered_set<string> uniq;
        string cur;
        for (char c : word) {
            if (isdigit(c)) {
                cur.push_back(c);
            } else {
                if (!cur.empty()) {
                    int i = 0;
                    while (i < (int)cur.size() && cur[i] == '0') ++i;
                    string num = (i == (int)cur.size()) ? "0" : cur.substr(i);
                    uniq.insert(num);
                    cur.clear();
                }
            }
        }
        if (!cur.empty()) {
            int i = 0;
            while (i < (int)cur.size() && cur[i] == '0') ++i;
            string num = (i == (int)cur.size()) ? "0" : cur.substr(i);
            uniq.insert(num);
        }
        return uniq.size();
    }
};
```

## Java

```java
class Solution {
    public int numDifferentIntegers(String word) {
        java.util.Set<String> unique = new java.util.HashSet<>();
        StringBuilder cur = new StringBuilder();
        int len = word.length();
        for (int i = 0; i <= len; i++) {
            char ch = i < len ? word.charAt(i) : 'a'; // sentinel non-digit
            if (ch >= '0' && ch <= '9') {
                cur.append(ch);
            } else {
                if (cur.length() > 0) {
                    String num = cur.toString();
                    int idx = 0;
                    while (idx < num.length() && num.charAt(idx) == '0') {
                        idx++;
                    }
                    String normalized = idx == num.length() ? "0" : num.substring(idx);
                    unique.add(normalized);
                    cur.setLength(0);
                }
            }
        }
        return unique.size();
    }
}
```

## Python

```python
class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        import re
        parts = re.split(r'\D+', word)
        unique = set()
        for p in parts:
            if not p:
                continue
            stripped = p.lstrip('0')
            if stripped == '':
                stripped = '0'
            unique.add(stripped)
        return len(unique)
```

## Python3

```python
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        unique = set()
        i, n = 0, len(word)
        while i < n:
            if word[i].isdigit():
                j = i
                while j < n and word[j].isdigit():
                    j += 1
                num = word[i:j].lstrip('0')
                if not num:
                    num = '0'
                unique.add(num)
                i = j
            else:
                i += 1
        return len(unique)
```

## C

```c
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int numDifferentIntegers(char* word) {
    char *uniq[1000];
    int uniqCount = 0;

    for (int i = 0; word[i]; ) {
        if (isdigit(word[i])) {
            int start = i;
            while (word[i] && isdigit(word[i])) i++;
            int end = i; // exclusive

            int k = start;
            while (k < end && word[k] == '0') k++;

            char *norm;
            if (k == end) { // all zeros
                norm = (char *)malloc(2);
                norm[0] = '0';
                norm[1] = '\0';
            } else {
                int len = end - k;
                norm = (char *)malloc(len + 1);
                memcpy(norm, word + k, len);
                norm[len] = '\0';
            }

            int found = 0;
            for (int t = 0; t < uniqCount; ++t) {
                if (strcmp(uniq[t], norm) == 0) {
                    found = 1;
                    break;
                }
            }
            if (!found) {
                uniq[uniqCount++] = norm;
            } else {
                free(norm);
            }
        } else {
            i++;
        }
    }

    for (int t = 0; t < uniqCount; ++t) {
        free(uniq[t]);
    }
    return uniqCount;
}
```

## Csharp

```csharp
using System.Collections.Generic;
using System.Text;

public class Solution {
    public int NumDifferentIntegers(string word) {
        var unique = new HashSet<string>();
        var sb = new StringBuilder();
        foreach (char ch in word) {
            if (ch >= '0' && ch <= '9') {
                sb.Append(ch);
            } else {
                AddNumber(sb, unique);
            }
        }
        AddNumber(sb, unique); // for trailing number
        return unique.Count;
    }

    private void AddNumber(StringBuilder sb, HashSet<string> set) {
        if (sb.Length == 0) return;
        string num = TrimLeadingZeros(sb.ToString());
        set.Add(num);
        sb.Clear();
    }

    private string TrimLeadingZeros(string s) {
        int i = 0;
        while (i < s.Length && s[i] == '0') i++;
        return i == s.Length ? "0" : s.Substring(i);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var numDifferentIntegers = function(word) {
    const unique = new Set();
    const n = word.length;
    let i = 0;
    while (i < n) {
        if (word[i] >= '0' && word[i] <= '9') {
            let j = i;
            while (j < n && word[j] >= '0' && word[j] <= '9') {
                j++;
            }
            let num = word.slice(i, j).replace(/^0+/, '');
            if (num === '') num = '0';
            unique.add(num);
            i = j;
        } else {
            i++;
        }
    }
    return unique.size;
};
```

## Typescript

```typescript
function numDifferentIntegers(word: string): number {
    const unique = new Set<string>();
    let i = 0;
    const n = word.length;
    while (i < n) {
        if (word[i] >= '0' && word[i] <= '9') {
            let j = i;
            while (j < n && word[j] >= '0' && word[j] <= '9') j++;
            let num = word.slice(i, j).replace(/^0+/, '');
            if (num === '') num = '0';
            unique.add(num);
            i = j;
        } else {
            i++;
        }
    }
    return unique.size;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function numDifferentIntegers($word) {
        $unique = [];
        $len = strlen($word);
        $current = '';
        for ($i = 0; $i < $len; $i++) {
            $c = $word[$i];
            if ($c >= '0' && $c <= '9') {
                $current .= $c;
            } else {
                if ($current !== '') {
                    $num = ltrim($current, '0');
                    if ($num === '') {
                        $num = '0';
                    }
                    $unique[$num] = true;
                    $current = '';
                }
            }
        }
        if ($current !== '') {
            $num = ltrim($current, '0');
            if ($num === '') {
                $num = '0';
            }
            $unique[$num] = true;
        }
        return count($unique);
    }
}
```

## Swift

```swift
class Solution {
    func numDifferentIntegers(_ word: String) -> Int {
        var uniqueNumbers = Set<String>()
        var currentDigits = ""
        
        for ch in word {
            if ch.isNumber {
                currentDigits.append(ch)
            } else {
                if !currentDigits.isEmpty {
                    let normalized = normalize(currentDigits)
                    uniqueNumbers.insert(normalized)
                    currentDigits.removeAll()
                }
            }
        }
        
        // Process any trailing digits
        if !currentDigits.isEmpty {
            let normalized = normalize(currentDigits)
            uniqueNumbers.insert(normalized)
        }
        
        return uniqueNumbers.count
    }
    
    private func normalize(_ numStr: String) -> String {
        let trimmed = numStr.drop { $0 == "0" }
        return trimmed.isEmpty ? "0" : String(trimmed)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numDifferentIntegers(word: String): Int {
        val unique = HashSet<String>()
        var i = 0
        while (i < word.length) {
            if (word[i].isDigit()) {
                var j = i
                while (j < word.length && word[j].isDigit()) j++
                var num = word.substring(i, j)
                var k = 0
                while (k < num.length && num[k] == '0') k++
                if (k == num.length) {
                    num = "0"
                } else {
                    num = num.substring(k)
                }
                unique.add(num)
                i = j
            } else {
                i++
            }
        }
        return unique.size
    }
}
```

## Dart

```dart
class Solution {
  int numDifferentIntegers(String word) {
    final Set<String> unique = <String>{};
    StringBuffer sb = StringBuffer();

    for (int i = 0; i < word.length; i++) {
      final ch = word[i];
      if (ch.codeUnitAt(0) >= '0'.codeUnitAt(0) && ch.codeUnitAt(0) <= '9'.codeUnitAt(0)) {
        sb.write(ch);
      } else {
        if (sb.isNotEmpty) {
          String numStr = _normalize(sb.toString());
          unique.add(numStr);
          sb.clear();
        }
      }
    }

    // Process any trailing number
    if (sb.isNotEmpty) {
      String numStr = _normalize(sb.toString());
      unique.add(numStr);
    }

    return unique.length;
  }

  String _normalize(String s) {
    int i = 0;
    while (i < s.length && s[i] == '0') i++;
    if (i == s.length) return "0";
    return s.substring(i);
  }
}
```

## Golang

```go
func numDifferentIntegers(word string) int {
	m := make(map[string]struct{})
	n := len(word)
	i := 0
	for i < n {
		if word[i] >= '0' && word[i] <= '9' {
			j := i
			for j < n && word[j] >= '0' && word[j] <= '9' {
				j++
			}
			num := word[i:j]
			k := 0
			for k < len(num) && num[k] == '0' {
				k++
			}
			if k == len(num) {
				num = "0"
			} else {
				num = num[k:]
			}
			m[num] = struct{}{}
			i = j
		} else {
			i++
		}
	}
	return len(m)
}
```

## Ruby

```ruby
require 'set'

def num_different_integers(word)
  uniques = Set.new
  i = 0
  n = word.length
  while i < n
    if word[i] >= '0' && word[i] <= '9'
      j = i
      j += 1 while j < n && word[j] >= '0' && word[j] <= '9'
      num = word[i...j].sub(/^0+/, '')
      num = '0' if num.empty?
      uniques.add(num)
      i = j
    else
      i += 1
    end
  end
  uniques.size
end
```

## Scala

```scala
object Solution {
    def numDifferentIntegers(word: String): Int = {
        val distinct = scala.collection.mutable.HashSet[String]()
        var i = 0
        while (i < word.length) {
            if (word(i).isDigit) {
                val sb = new StringBuilder
                while (i < word.length && word(i).isDigit) {
                    sb.append(word(i))
                    i += 1
                }
                val numStr = sb.toString()
                val trimmed = numStr.dropWhile(_ == '0')
                if (trimmed.isEmpty) distinct.add("0") else distinct.add(trimmed)
            } else {
                i += 1
            }
        }
        distinct.size
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_different_integers(word: String) -> i32 {
        use std::collections::HashSet;
        let mut unique = HashSet::new();
        let mut cur = String::new();

        for ch in word.chars() {
            if ch.is_ascii_digit() {
                cur.push(ch);
            } else if !cur.is_empty() {
                let trimmed = cur.trim_start_matches('0');
                let norm = if trimmed.is_empty() { "0".to_string() } else { trimmed.to_string() };
                unique.insert(norm);
                cur.clear();
            }
        }

        if !cur.is_empty() {
            let trimmed = cur.trim_start_matches('0');
            let norm = if trimmed.is_empty() { "0".to_string() } else { trimmed.to_string() };
            unique.insert(norm);
        }

        unique.len() as i32
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (num-different-integers word)
  (-> string? exact-integer?)
  (let* ([parts (filter (lambda (s) (not (string-empty? s)))
                        (regexp-split #px"[^0-9]+" word))]
         [unique (make-hash)])
    (for ([p parts])
      (define norm
        (let ([t (regexp-replace* #px"^0+" p "")])
          (if (string-empty? t) "0" t)))
      (hash-set! unique norm #t))
    (hash-count unique)))
```

## Erlang

```erlang
-spec num_different_integers(unicode:unicode_binary()) -> integer().
num_different_integers(Word) ->
    Tokens = re:split(Word, "[^0-9]+", [{return, binary}]),
    collect(Tokens, #{}).

collect([], Acc) -> maps:size(Acc);
collect([<<>>|Rest], Acc) -> collect(Rest, Acc);
collect([Token|Rest], Acc) ->
    Int = erlang:binary_to_integer(Token),
    NewAcc = maps:put(Int, true, Acc),
    collect(Rest, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_different_integers(word :: String.t) :: integer
  def num_different_integers(word) do
    Regex.scan(~r/\d+/, word)
    |> List.flatten()
    |> Enum.map(fn s ->
      trimmed = String.trim_leading(s, "0")
      if trimmed == "", do: "0", else: trimmed
    end)
    |> MapSet.new()
    |> MapSet.size()
  end
end
```
