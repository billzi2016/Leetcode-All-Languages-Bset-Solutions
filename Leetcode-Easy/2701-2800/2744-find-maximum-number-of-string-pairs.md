# 2744. Find Maximum Number of String Pairs

## Cpp

```cpp
class Solution {
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        unordered_set<string> st(words.begin(), words.end());
        int pairs = 0;
        for (const string& w : words) {
            if (!st.count(w)) continue;
            string rev = {w[1], w[0]};
            if (st.count(rev)) {
                ++pairs;
                st.erase(w);
                st.erase(rev);
            }
        }
        return pairs;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
        Set<String> set = new HashSet<>(Arrays.asList(words));
        int pairs = 0;
        for (String w : words) {
            if (!set.contains(w)) continue;
            String rev = new StringBuilder(w).reverse().toString();
            if (!rev.equals(w) && set.contains(rev)) {
                pairs++;
                set.remove(w);
                set.remove(rev);
            }
        }
        return pairs;
    }
}
```

## Python

```python
class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word_set = set(words)
        pairs = 0
        for w in list(word_set):
            rev = w[::-1]
            if rev in word_set and rev != w:
                pairs += 1
                word_set.discard(w)
                word_set.discard(rev)
        return pairs
```

## Python3

```python
class Solution:
    def maximumNumberOfStringPairs(self, words):
        remaining = set(words)
        pairs = 0
        for w in words:
            if w not in remaining:
                continue
            rev = w[::-1]
            if rev != w and rev in remaining:
                pairs += 1
                remaining.remove(w)
                remaining.remove(rev)
        return pairs
```

## C

```c
int maximumNumberOfStringPairs(char** words, int wordsSize) {
    int used[55] = {0};
    int ans = 0;
    for (int i = 0; i < wordsSize; ++i) {
        if (used[i]) continue;
        for (int j = i + 1; j < wordsSize; ++j) {
            if (used[j]) continue;
            if (words[i][0] == words[j][1] && words[i][1] == words[j][0]) {
                ans++;
                used[i] = used[j] = 1;
                break;
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumNumberOfStringPairs(string[] words) {
        var remaining = new HashSet<string>(words);
        int count = 0;
        foreach (var w in words) {
            if (!remaining.Contains(w)) continue;
            string rev = new string(new char[] { w[1], w[0] });
            if (rev != w && remaining.Contains(rev)) {
                count++;
                remaining.Remove(w);
                remaining.Remove(rev);
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var maximumNumberOfStringPairs = function(words) {
    const set = new Set(words);
    let count = 0;
    for (const w of words) {
        if (!set.has(w)) continue;
        const rev = w[1] + w[0];
        if (rev !== w && set.has(rev)) {
            count++;
            set.delete(w);
            set.delete(rev);
        }
    }
    return count;
};
```

## Typescript

```typescript
function maximumNumberOfStringPairs(words: string[]): number {
    const wordSet = new Set<string>(words);
    let pairCount = 0;
    for (const w of words) {
        if (w[0] === w[1]) continue; // palindrome cannot form a pair with itself
        const rev = w[1] + w[0];
        if (wordSet.has(rev)) {
            pairCount++;
        }
    }
    return Math.floor(pairCount / 2);
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function maximumNumberOfStringPairs($words) {
        // map each word to a placeholder (e.g., its index)
        $available = array_flip($words);
        $pairs = 0;

        foreach ($words as $w) {
            if (!isset($available[$w])) {
                continue; // already used in a pair
            }
            $rev = strrev($w);
            if ($rev !== $w && isset($available[$rev])) {
                $pairs++;
                unset($available[$w]);
                unset($available[$rev]);
            }
        }

        return $pairs;
    }
}
```

## Swift

```swift
class Solution {
    func maximumNumberOfStringPairs(_ words: [String]) -> Int {
        var remaining = Set(words)
        var pairs = 0
        for w in words {
            if !remaining.contains(w) { continue }
            let rev = String(w.reversed())
            if rev != w && remaining.contains(rev) {
                pairs += 1
                remaining.remove(w)
                remaining.remove(rev)
            }
        }
        return pairs
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumNumberOfStringPairs(words: Array<String>): Int {
        val pending = HashSet<String>()
        var pairs = 0
        for (w in words) {
            val rev = w.reversed()
            if (pending.remove(rev)) {
                pairs++
            } else {
                pending.add(w)
            }
        }
        return pairs
    }
}
```

## Dart

```dart
class Solution {
  int maximumNumberOfStringPairs(List<String> words) {
    final Set<String> remaining = {...words};
    int count = 0;
    for (final word in words) {
      if (!remaining.contains(word)) continue;
      String rev = '${word[1]}${word[0]}';
      if (rev != word && remaining.contains(rev)) {
        count++;
        remaining.remove(word);
        remaining.remove(rev);
      }
    }
    return count;
  }
}
```

## Golang

```go
func maximumNumberOfStringPairs(words []string) int {
    seen := make(map[string]struct{})
    pairs := 0
    for _, w := range words {
        rev := string([]byte{w[1], w[0]})
        if _, ok := seen[rev]; ok {
            pairs++
            delete(seen, rev)
        } else {
            seen[w] = struct{}{}
        }
    }
    return pairs
}
```

## Ruby

```ruby
require 'set'

def maximum_number_of_string_pairs(words)
  remaining = Set.new(words)
  pairs = 0

  words.each do |w|
    next unless remaining.include?(w)
    rev = w.reverse
    if rev != w && remaining.include?(rev)
      pairs += 1
      remaining.delete(w)
      remaining.delete(rev)
    end
  end

  pairs
end
```

## Scala

```scala
object Solution {
    def maximumNumberOfStringPairs(words: Array[String]): Int = {
        val seen = scala.collection.mutable.HashSet[String]()
        var pairs = 0
        for (w <- words) {
            val rev = w.reverse
            if (seen.contains(rev)) {
                pairs += 1
                seen.remove(rev)
            } else {
                seen.add(w)
            }
        }
        pairs
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn maximum_number_of_string_pairs(words: Vec<String>) -> i32 {
        let mut set: HashSet<String> = words.into_iter().collect();
        let mut pairs = 0;
        // Iterate over a snapshot of the current set
        for w in set.clone().into_iter() {
            if !set.contains(&w) {
                continue; // already used in a previous pair
            }
            let rev: String = w.chars().rev().collect();
            if rev != w && set.contains(&rev) {
                pairs += 1;
                set.remove(&w);
                set.remove(&rev);
            }
        }
        pairs as i32
    }
}
```

## Racket

```racket
(define/contract (maximum-number-of-string-pairs words)
  (-> (listof string?) exact-integer?)
  (let* ((word-set (for/hash ([w words]) (values w #t)))
         (used (make-hash))
         (pair-count 0))
    (for ([w words])
      (unless (hash-ref used w #f)
        (define rev (string-append (substring w 1) (substring w 0 1)))
        (when (and (hash-has-key? word-set rev) (not (hash-ref used rev #f)))
          (set! pair-count (+ pair-count 1))
          (hash-set! used w #t)
          (hash-set! used rev #t))))
    pair-count))
```

## Erlang

```erlang
-spec maximum_number_of_string_pairs(Words :: [unicode:unicode_binary()]) -> integer().
maximum_number_of_string_pairs(Words) ->
    Set = maps:from_list([{W, true} || W <- Words]),
    max_pairs(Words, Set, 0).

max_pairs([], _Map, Count) -> Count;
max_pairs([W|Rest], Map, Count) ->
    case maps:is_key(W, Map) of
        false ->
            max_pairs(Rest, Map, Count);
        true ->
            Rev = reverse_word(W),
            if Rev =:= W ->
                    max_pairs(Rest, Map, Count);
               true,
               maps:is_key(Rev, Map) ->
                    NewMap = maps:remove(W, maps:remove(Rev, Map)),
                    max_pairs(Rest, NewMap, Count + 1);
               true ->
                    max_pairs(Rest, Map, Count)
            end
    end.

reverse_word(<<A, B>>) -> <<B, A>>.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_number_of_string_pairs(words :: [String.t()]) :: integer()
  def maximum_number_of_string_pairs(words) do
    set = MapSet.new(words)

    Enum.reduce(words, 0, fn word, acc ->
      rev = String.reverse(word)

      if rev != word and MapSet.member?(set, rev) and word < rev do
        acc + 1
      else
        acc
      end
    end)
  end
end
```
