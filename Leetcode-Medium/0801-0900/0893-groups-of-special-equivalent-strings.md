# 0893. Groups of Special-Equivalent Strings

## Cpp

```cpp
class Solution {
public:
    int numSpecialEquivGroups(vector<string>& words) {
        unordered_set<string> groups;
        for (const string& w : words) {
            string even, odd;
            even.reserve((w.size()+1)/2);
            odd.reserve(w.size()/2);
            for (size_t i = 0; i < w.size(); ++i) {
                if ((i & 1) == 0)
                    even.push_back(w[i]);
                else
                    odd.push_back(w[i]);
            }
            sort(even.begin(), even.end());
            sort(odd.begin(), odd.end());
            groups.insert(even + "#" + odd);
        }
        return static_cast<int>(groups.size());
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int numSpecialEquivGroups(String[] words) {
        Set<String> unique = new HashSet<>();
        for (String w : words) {
            int len = w.length();
            char[] evens = new char[(len + 1) / 2];
            char[] odds = new char[len / 2];
            int ei = 0, oi = 0;
            for (int i = 0; i < len; i++) {
                if ((i & 1) == 0) {
                    evens[ei++] = w.charAt(i);
                } else {
                    odds[oi++] = w.charAt(i);
                }
            }
            Arrays.sort(evens);
            Arrays.sort(odds);
            String key = new String(evens) + "#" + new String(odds);
            unique.add(key);
        }
        return unique.size();
    }
}
```

## Python

```python
class Solution(object):
    def numSpecialEquivGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        groups = set()
        for w in words:
            even_chars = sorted(w[0::2])
            odd_chars = sorted(w[1::2])
            # Use a tuple as the canonical representation
            groups.add((''.join(even_chars), ''.join(odd_chars)))
        return len(groups)
```

## Python3

```python
from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()
        for w in words:
            even_chars = sorted(w[0::2])
            odd_chars = sorted(w[1::2])
            key = (''.join(even_chars), ''.join(odd_chars))
            groups.add(key)
        return len(groups)
```

## C

```c
#include <string.h>
#include <stdlib.h>

int numSpecialEquivGroups(char** words, int wordsSize) {
    if (wordsSize == 0) return 0;
    int len = strlen(words[0]);
    char **signatures = (char **)malloc(sizeof(char *) * wordsSize);
    int uniq = 0;

    for (int i = 0; i < wordsSize; ++i) {
        int cntEven[26] = {0}, cntOdd[26] = {0};
        const char *w = words[i];
        for (int j = 0; j < len; ++j) {
            if ((j & 1) == 0)
                cntEven[w[j] - 'a']++;
            else
                cntOdd[w[j] - 'a']++;
        }

        char buf[45]; // max length 20 + delimiter + 20 + '\0'
        int pos = 0;
        for (int c = 0; c < 26; ++c) {
            for (int k = 0; k < cntEven[c]; ++k)
                buf[pos++] = 'a' + c;
        }
        buf[pos++] = '|';
        for (int c = 0; c < 26; ++c) {
            for (int k = 0; k < cntOdd[c]; ++k)
                buf[pos++] = 'a' + c;
        }
        buf[pos] = '\0';

        int found = 0;
        for (int s = 0; s < uniq; ++s) {
            if (strcmp(signatures[s], buf) == 0) {
                found = 1;
                break;
            }
        }
        if (!found) {
            char *copy = (char *)malloc(strlen(buf) + 1);
            strcpy(copy, buf);
            signatures[uniq++] = copy;
        }
    }

    for (int i = 0; i < uniq; ++i)
        free(signatures[i]);
    free(signatures);
    return uniq;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int NumSpecialEquivGroups(string[] words) {
        var signatures = new HashSet<string>();
        foreach (var word in words) {
            var evenChars = new List<char>();
            var oddChars = new List<char>();
            for (int i = 0; i < word.Length; i++) {
                if ((i & 1) == 0)
                    evenChars.Add(word[i]);
                else
                    oddChars.Add(word[i]);
            }
            evenChars.Sort();
            oddChars.Sort();
            string key = new string(evenChars.ToArray()) + "|" + new string(oddChars.ToArray());
            signatures.Add(key);
        }
        return signatures.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var numSpecialEquivGroups = function(words) {
    const seen = new Set();
    for (const w of words) {
        const even = [];
        const odd = [];
        for (let i = 0; i < w.length; ++i) {
            if ((i & 1) === 0) even.push(w[i]);
            else odd.push(w[i]);
        }
        even.sort();
        odd.sort();
        seen.add(even.join('') + '_' + odd.join(''));
    }
    return seen.size;
};
```

## Typescript

```typescript
function numSpecialEquivGroups(words: string[]): number {
    const seen = new Set<string>();
    for (const w of words) {
        const even: string[] = [];
        const odd: string[] = [];
        for (let i = 0; i < w.length; i++) {
            if ((i & 1) === 0) {
                even.push(w[i]);
            } else {
                odd.push(w[i]);
            }
        }
        even.sort();
        odd.sort();
        seen.add(even.join('') + '_' + odd.join(''));
    }
    return seen.size;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function numSpecialEquivGroups($words) {
        $unique = [];
        foreach ($words as $word) {
            $even = [];
            $odd = [];
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                if (($i & 1) === 0) {
                    $even[] = $word[$i];
                } else {
                    $odd[] = $word[$i];
                }
            }
            sort($even);
            sort($odd);
            $key = implode('', $even) . implode('', $odd);
            $unique[$key] = true;
        }
        return count($unique);
    }
}
```

## Swift

```swift
class Solution {
    func numSpecialEquivGroups(_ words: [String]) -> Int {
        var uniqueKeys = Set<String>()
        for word in words {
            var evenChars: [Character] = []
            var oddChars: [Character] = []
            let characters = Array(word)
            for (index, ch) in characters.enumerated() {
                if index % 2 == 0 {
                    evenChars.append(ch)
                } else {
                    oddChars.append(ch)
                }
            }
            evenChars.sort()
            oddChars.sort()
            let key = String(evenChars) + "|" + String(oddChars)
            uniqueKeys.insert(key)
        }
        return uniqueKeys.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numSpecialEquivGroups(words: Array<String>): Int {
        val groups = HashSet<String>()
        for (word in words) {
            val evens = mutableListOf<Char>()
            val odds = mutableListOf<Char>()
            for (i in word.indices) {
                if (i % 2 == 0) evens.add(word[i]) else odds.add(word[i])
            }
            evens.sort()
            odds.sort()
            val key = evens.joinToString("") + "|" + odds.joinToString("")
            groups.add(key)
        }
        return groups.size
    }
}
```

## Dart

```dart
class Solution {
  int numSpecialEquivGroups(List<String> words) {
    final Set<String> groups = <String>{};
    for (final word in words) {
      groups.add(_canonical(word));
    }
    return groups.length;
  }

  String _canonical(String s) {
    final List<String> even = [];
    final List<String> odd = [];
    for (int i = 0; i < s.length; i++) {
      if ((i & 1) == 0) {
        even.add(s[i]);
      } else {
        odd.add(s[i]);
      }
    }
    even.sort();
    odd.sort();
    return '${even.join()}_${odd.join()}';
  }
}
```

## Golang

```go
func numSpecialEquivGroups(words []string) int {
	type void struct{}
	seen := make(map[string]void)

	for _, w := range words {
		even := make([]byte, 0, len(w)/2+1)
		odd := make([]byte, 0, len(w)/2+1)
		for i := 0; i < len(w); i++ {
			if i%2 == 0 {
				even = append(even, w[i])
			} else {
				odd = append(odd, w[i])
			}
		}
		sort.Slice(even, func(i, j int) bool { return even[i] < even[j] })
		sort.Slice(odd, func(i, j int) bool { return odd[i] < odd[j] })
		key := string(even) + "|" + string(odd)
		seen[key] = void{}
	}
	return len(seen)
}
```

## Ruby

```ruby
require 'set'

def num_special_equiv_groups(words)
  groups = Set.new
  words.each do |word|
    evens = []
    odds = []
    word.chars.each_with_index do |ch, idx|
      if idx.even?
        evens << ch
      else
        odds << ch
      end
    end
    evens.sort!
    odds.sort!
    groups.add(evens.join + "|" + odds.join)
  end
  groups.size
end
```

## Scala

```scala
object Solution {
  def numSpecialEquivGroups(words: Array[String]): Int = {
    val seen = scala.collection.mutable.HashSet[String]()
    for (w <- words) {
      val even = new StringBuilder
      val odd = new StringBuilder
      var i = 0
      while (i < w.length) {
        if ((i & 1) == 0) even.append(w.charAt(i))
        else odd.append(w.charAt(i))
        i += 1
      }
      val evSorted = even.result().toCharArray.sorted.mkString
      val odSorted = odd.result().toCharArray.sorted.mkString
      seen.add(evSorted + "#" + odSorted)
    }
    seen.size
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn num_special_equiv_groups(words: Vec<String>) -> i32 {
        let mut unique = HashSet::new();
        for w in words.iter() {
            let mut evens = Vec::new();
            let mut odds = Vec::new();
            for (i, ch) in w.chars().enumerate() {
                if i % 2 == 0 {
                    evens.push(ch);
                } else {
                    odds.push(ch);
                }
            }
            evens.sort_unstable();
            odds.sort_unstable();
            let key = format!("{}#{}", evens.iter().collect::<String>(), odds.iter().collect::<String>());
            unique.insert(key);
        }
        unique.len() as i32
    }
}
```

## Racket

```racket
(define (canonical s)
  (let* ((len (string-length s))
         (evens '())
         (odds '()))
    (for ([i (in-range len)])
      (let ((ch (string-ref s i)))
        (if (even? i)
            (set! evens (cons ch evens))
            (set! odds (cons ch odds)))))
    (define sorted-ev (sort evens char<?))
    (define sorted-od (sort odds char<?))
    (string-append (list->string sorted-ev) "|" (list->string sorted-od))))

(define/contract (num-special-equiv-groups words)
  (-> (listof string?) exact-integer?)
  (let ((seen (make-hash)))
    (for ([w (in-list words)])
      (hash-set! seen (canonical w) #t))
    (hash-count seen)))
```

## Erlang

```erlang
-module(solution).
-export([num_special_equiv_groups/1]).

-spec num_special_equiv_groups(Words :: [unicode:unicode_binary()]) -> integer().
num_special_equiv_groups(Words) ->
    Signatures = [signature(Word) || Word <- Words],
    length(lists:usort(Signatures)).

signature(Word) ->
    Chars = binary_to_list(Word),
    Indexed = lists:zip(Chars, lists:seq(0, length(Chars) - 1)),
    Even = [C || {C, I} <- Indexed, (I rem 2) =:= 0],
    Odd = [C || {C, I} <- Indexed, (I rem 2) =:= 1],
    {lists:sort(Even), lists:sort(Odd)}.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_special_equiv_groups(words :: [String.t]) :: integer
  def num_special_equiv_groups(words) do
    words
    |> Enum.reduce(MapSet.new(), fn word, set ->
      chars = String.graphemes(word)

      {even, odd} =
        Enum.with_index(chars)
        |> Enum.reduce({[], []}, fn {c, i}, {e, o} ->
          if rem(i, 2) == 0 do
            {[c | e], o}
          else
            {e, [c | o]}
          end
        end)

      sorted_even = even |> Enum.sort() |> Enum.join()
      sorted_odd = odd |> Enum.sort() |> Enum.join()
      canonical = sorted_even <> "|" <> sorted_odd

      MapSet.put(set, canonical)
    end)
    |> MapSet.size()
  end
end
```
