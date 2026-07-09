# 1897. Redistribute Characters to Make All Strings Equal

## Cpp

```cpp
class Solution {
public:
    bool makeEqual(vector<string>& words) {
        int n = words.size();
        array<int, 26> cnt{};
        for (const string& w : words) {
            for (char c : w) {
                ++cnt[c - 'a'];
            }
        }
        for (int v : cnt) {
            if (v % n != 0) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean makeEqual(String[] words) {
        int[] cnt = new int[26];
        for (String w : words) {
            for (int i = 0; i < w.length(); i++) {
                cnt[w.charAt(i) - 'a']++;
            }
        }
        int n = words.length;
        for (int c : cnt) {
            if (c % n != 0) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n = len(words)
        counts = [0] * 26
        for w in words:
            for ch in w:
                counts[ord(ch) - ord('a')] += 1
        for cnt in counts:
            if cnt % n != 0:
                return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        counts = [0] * 26
        for word in words:
            for c in word:
                counts[ord(c) - ord('a')] += 1
        return all(v % n == 0 for v in counts)
```

## C

```c
#include <stdbool.h>

bool makeEqual(char** words, int wordsSize) {
    int cnt[26] = {0};
    for (int i = 0; i < wordsSize; ++i) {
        char *p = words[i];
        while (*p) {
            cnt[*p - 'a']++;
            ++p;
        }
    }
    for (int i = 0; i < 26; ++i) {
        if (cnt[i] % wordsSize != 0) return false;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool MakeEqual(string[] words) {
        int[] cnt = new int[26];
        foreach (var w in words) {
            foreach (char c in w) {
                cnt[c - 'a']++;
            }
        }
        int n = words.Length;
        foreach (int v in cnt) {
            if (v % n != 0) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
var makeEqual = function(words) {
    const n = words.length;
    const cnt = new Array(26).fill(0);
    for (const w of words) {
        for (let i = 0; i < w.length; i++) {
            cnt[w.charCodeAt(i) - 97]++;
        }
    }
    for (let i = 0; i < 26; i++) {
        if (cnt[i] % n !== 0) return false;
    }
    return true;
};
```

## Typescript

```typescript
function makeEqual(words: string[]): boolean {
    const cnt = new Array(26).fill(0);
    for (const w of words) {
        for (let i = 0; i < w.length; ++i) {
            cnt[w.charCodeAt(i) - 97]++;
        }
    }
    const n = words.length;
    for (const c of cnt) {
        if (c % n !== 0) return false;
    }
    return true;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $words
     * @return Boolean
     */
    function makeEqual($words) {
        $cnt = array_fill(0, 26, 0);
        foreach ($words as $word) {
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $idx = ord($word[$i]) - 97;
                $cnt[$idx]++;
            }
        }
        $n = count($words);
        foreach ($cnt as $v) {
            if ($v % $n !== 0) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func makeEqual(_ words: [String]) -> Bool {
        var counts = Array(repeating: 0, count: 26)
        let aValue = Character("a").unicodeScalars.first!.value
        for word in words {
            for scalar in word.unicodeScalars {
                let idx = Int(scalar.value - aValue)
                counts[idx] += 1
            }
        }
        let n = words.count
        for cnt in counts {
            if cnt % n != 0 {
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
    fun makeEqual(words: Array<String>): Boolean {
        val counts = IntArray(26)
        for (word in words) {
            for (c in word) {
                counts[c - 'a']++
            }
        }
        val n = words.size
        for (cnt in counts) {
            if (cnt % n != 0) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool makeEqual(List<String> words) {
    int n = words.length;
    List<int> cnt = List.filled(26, 0);
    for (var w in words) {
      for (int i = 0; i < w.length; ++i) {
        cnt[w.codeUnitAt(i) - 97]++;
      }
    }
    for (int c in cnt) {
      if (c % n != 0) return false;
    }
    return true;
  }
}
```

## Golang

```go
func makeEqual(words []string) bool {
    var cnt [26]int
    for _, w := range words {
        for _, ch := range w {
            cnt[ch-'a']++
        }
    }
    n := len(words)
    for _, v := range cnt {
        if v%n != 0 {
            return false
        }
    }
    return true
}
```

## Ruby

```ruby
def make_equal(words)
  counts = Array.new(26, 0)
  words.each do |w|
    w.each_byte { |b| counts[b - 97] += 1 }
  end
  n = words.length
  counts.all? { |c| c % n == 0 }
end
```

## Scala

```scala
object Solution {
    def makeEqual(words: Array[String]): Boolean = {
        val n = words.length
        val counts = new Array[Int](26)
        for (word <- words; c <- word) {
            counts(c - 'a') += 1
        }
        for (cnt <- counts) {
            if (cnt % n != 0) return false
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn make_equal(words: Vec<String>) -> bool {
        let n = words.len();
        let mut cnt = [0usize; 26];
        for w in &words {
            for &b in w.as_bytes() {
                cnt[(b - b'a') as usize] += 1;
            }
        }
        for &c in cnt.iter() {
            if c % n != 0 {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (make-equal words)
  (-> (listof string?) boolean?)
  (let* ([n (length words)]
         [counts (make-vector 26 0)])
    (for ([w words])
      (let ([len (string-length w)])
        (for ([i (in-range len)])
          (let* ([c (string-ref w i)]
                 [idx (- (char->integer c) (char->integer #\a))])
            (vector-set! counts idx (+ 1 (vector-ref counts idx)))))))
    (for/and ([cnt (in-vector counts)])
      (= (remainder cnt n) 0))))
```

## Erlang

```erlang
-module(solution).
-export([make_equal/1]).

-spec make_equal(Words :: [unicode:unicode_binary()]) -> boolean().
make_equal(Words) ->
    N = length(Words),
    TotalMap = lists:foldl(fun add_word/2, #{}, Words),
    maps:fold(
        fun(_Key, Val, true) when Val rem N == 0 -> true;
           (_Key, _Val, _) -> false
        end,
        true,
        TotalMap).

add_word(Word, Acc) ->
    lists:foldl(fun(C, M) -> maps:update_with(C, fun(V) -> V + 1 end, 1, M) end,
                Acc,
                binary_to_list(Word)).
```

## Elixir

```elixir
defmodule Solution do
  @spec make_equal(words :: [String.t]) :: boolean
  def make_equal(words) do
    n = length(words)

    counts =
      Enum.reduce(words, List.duplicate(0, 26), fn word, acc ->
        Enum.reduce(String.to_charlist(word), acc, fn c, a ->
          idx = c - ?a
          List.update_at(a, idx, &(&1 + 1))
        end)
      end)

    Enum.all?(counts, fn cnt -> rem(cnt, n) == 0 end)
  end
end
```
