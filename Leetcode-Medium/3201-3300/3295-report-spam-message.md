# 3295. Report Spam Message

## Cpp

```cpp
class Solution {
public:
    bool reportSpam(vector<string>& message, vector<string>& bannedWords) {
        unordered_set<string> banned(bannedWords.begin(), bannedWords.end());
        int cnt = 0;
        for (const string& w : message) {
            if (banned.find(w) != banned.end()) {
                ++cnt;
                if (cnt >= 2) return true;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean reportSpam(String[] message, String[] bannedWords) {
        java.util.HashSet<String> bannedSet = new java.util.HashSet<>();
        for (String w : bannedWords) {
            bannedSet.add(w);
        }
        int matches = 0;
        for (String w : message) {
            if (bannedSet.contains(w)) {
                if (++matches >= 2) return true;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def reportSpam(self, message, bannedWords):
        """
        :type message: List[str]
        :type bannedWords: List[str]
        :rtype: bool
        """
        banned_set = set(bannedWords)
        count = 0
        for word in message:
            if word in banned_set:
                count += 1
                if count >= 2:
                    return True
        return False
```

## Python3

```python
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned_set = set(bannedWords)
        count = 0
        for word in message:
            if word in banned_set:
                count += 1
                if count >= 2:
                    return True
        return False
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int cmp_str(const void *a, const void *b) {
    const char *const *pa = (const char *const *)a;
    const char *const *pb = (const char *const *)b;
    return strcmp(*pa, *pb);
}

bool reportSpam(char** message, int messageSize, char** bannedWords, int bannedWordsSize) {
    if (messageSize == 0 || bannedWordsSize == 0) return false;

    qsort(bannedWords, bannedWordsSize, sizeof(char*), cmp_str);

    int matches = 0;
    for (int i = 0; i < messageSize; ++i) {
        void *found = bsearch(&message[i], bannedWords, bannedWordsSize,
                              sizeof(char*), cmp_str);
        if (found) {
            if (++matches >= 2) return true;
        }
    }
    return false;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public bool ReportSpam(string[] message, string[] bannedWords) {
        var bannedSet = new HashSet<string>(bannedWords);
        int count = 0;
        foreach (var word in message) {
            if (bannedSet.Contains(word)) {
                count++;
                if (count >= 2) return true;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} message
 * @param {string[]} bannedWords
 * @return {boolean}
 */
var reportSpam = function(message, bannedWords) {
    const bannedSet = new Set(bannedWords);
    let count = 0;
    for (const word of message) {
        if (bannedSet.has(word)) {
            count++;
            if (count >= 2) return true;
        }
    }
    return false;
};
```

## Typescript

```typescript
function reportSpam(message: string[], bannedWords: string[]): boolean {
    const bannedSet = new Set<string>(bannedWords);
    let matches = 0;
    for (const word of message) {
        if (bannedSet.has(word)) {
            matches++;
            if (matches >= 2) return true;
        }
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $message
     * @param String[] $bannedWords
     * @return Boolean
     */
    function reportSpam($message, $bannedWords) {
        $bannedSet = array_flip($bannedWords);
        $matches = 0;
        foreach ($message as $word) {
            if (isset($bannedSet[$word])) {
                $matches++;
                if ($matches >= 2) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func reportSpam(_ message: [String], _ bannedWords: [String]) -> Bool {
        let bannedSet = Set(bannedWords)
        var matchCount = 0
        for word in message {
            if bannedSet.contains(word) {
                matchCount += 1
                if matchCount >= 2 {
                    return true
                }
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reportSpam(message: Array<String>, bannedWords: Array<String>): Boolean {
        val bannedSet = HashSet<String>(bannedWords.size * 2)
        for (word in bannedWords) {
            bannedSet.add(word)
        }
        var count = 0
        for (word in message) {
            if (bannedSet.contains(word)) {
                count++
                if (count >= 2) return true
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool reportSpam(List<String> message, List<String> bannedWords) {
    final Set<String> bannedSet = bannedWords.toSet();
    int count = 0;
    for (final word in message) {
      if (bannedSet.contains(word)) {
        count++;
        if (count >= 2) return true;
      }
    }
    return false;
  }
}
```

## Golang

```go
func reportSpam(message []string, bannedWords []string) bool {
	set := make(map[string]struct{}, len(bannedWords))
	for _, w := range bannedWords {
		set[w] = struct{}{}
	}
	count := 0
	for _, w := range message {
		if _, ok := set[w]; ok {
			count++
			if count >= 2 {
				return true
			}
		}
	}
	return false
}
```

## Ruby

```ruby
require 'set'

# @param {String[]} message
# @param {String[]} banned_words
# @return {Boolean}
def report_spam(message, banned_words)
  banned_set = Set.new(banned_words)
  matches = 0
  message.each do |word|
    if banned_set.include?(word)
      matches += 1
      return true if matches >= 2
    end
  end
  false
end
```

## Scala

```scala
object Solution {
    def reportSpam(message: Array[String], bannedWords: Array[String]): Boolean = {
        val banned = bannedWords.toSet
        var count = 0
        for (word <- message) {
            if (banned.contains(word)) {
                count += 1
                if (count >= 2) return true
            }
        }
        false
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn report_spam(message: Vec<String>, banned_words: Vec<String>) -> bool {
        let mut banned_set = HashSet::with_capacity(banned_words.len());
        for w in banned_words {
            banned_set.insert(w);
        }
        let mut count = 0;
        for word in message.iter() {
            if banned_set.contains(word) {
                count += 1;
                if count >= 2 {
                    return true;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (report-spam message bannedWords)
  (-> (listof string?) (listof string?) boolean?)
  (let ([banned-set (make-hash)])
    (for-each (lambda (w) (hash-set! banned-set w #t)) bannedWords)
    (let loop ((lst message) (cnt 0))
      (cond
        [(>= cnt 2) #t]
        [(null? lst) #f]
        [else (loop (cdr lst)
                    (if (hash-has-key? banned-set (car lst))
                        (+ cnt 1)
                        cnt))]))))
```

## Erlang

```erlang
-spec report_spam(Message :: [unicode:unicode_binary()], BannedWords :: [unicode:unicode_binary()]) -> boolean().
report_spam(Message, BannedWords) ->
    Set = maps:from_list([{W, true} || W <- BannedWords]),
    check(Message, Set, 0).

check(_, _, C) when C >= 2 -> true;
check([], _, _) -> false;
check([H|T], Set, C) ->
    case maps:is_key(H, Set) of
        true -> check(T, Set, C + 1);
        false -> check(T, Set, C)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec report_spam(message :: [String.t()], banned_words :: [String.t()]) :: boolean()
  def report_spam(message, banned_words) do
    banned_set = MapSet.new(banned_words)

    count =
      Enum.reduce_while(message, 0, fn word, acc ->
        if MapSet.member?(banned_set, word) do
          new_acc = acc + 1

          if new_acc >= 2 do
            {:halt, new_acc}
          else
            {:cont, new_acc}
          end
        else
          {:cont, acc}
        end
      end)

    count >= 2
  end
end
```
