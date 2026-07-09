# 2506. Count Pairs Of Similar Strings

## Cpp

```cpp
class Solution {
public:
    int similarPairs(vector<string>& words) {
        unordered_map<int,int> cnt;
        int ans = 0;
        for (const string& w : words) {
            int mask = 0;
            for (char c : w) mask |= 1 << (c - 'a');
            ans += cnt[mask];
            ++cnt[mask];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int similarPairs(String[] words) {
        java.util.Map<Integer, Integer> freq = new java.util.HashMap<>();
        int ans = 0;
        for (String w : words) {
            int mask = 0;
            for (int i = 0; i < w.length(); i++) {
                mask |= 1 << (w.charAt(i) - 'a');
            }
            ans += freq.getOrDefault(mask, 0);
            freq.put(mask, freq.getOrDefault(mask, 0) + 1);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mask_count = {}
        for w in words:
            mask = 0
            for ch in set(w):
                mask |= 1 << (ord(ch) - 97)
            mask_count[mask] = mask_count.get(mask, 0) + 1

        ans = 0
        for cnt in mask_count.values():
            ans += cnt * (cnt - 1) // 2
        return ans
```

## Python3

```python
from typing import List
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        mask_count = {}
        for w in words:
            mask = 0
            for ch in set(w):
                mask |= 1 << (ord(ch) - ord('a'))
            mask_count[mask] = mask_count.get(mask, 0) + 1
        ans = 0
        for cnt in mask_count.values():
            ans += cnt * (cnt - 1) // 2
        return ans
```

## C

```c
int similarPairs(char** words, int wordsSize) {
    int masks[100];
    for (int i = 0; i < wordsSize; ++i) {
        int mask = 0;
        char *p = words[i];
        while (*p) {
            mask |= 1 << (*p - 'a');
            ++p;
        }
        masks[i] = mask;
    }
    int ans = 0;
    for (int i = 0; i < wordsSize; ++i) {
        for (int j = i + 1; j < wordsSize; ++j) {
            if (masks[i] == masks[j]) {
                ++ans;
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int SimilarPairs(string[] words) {
        var freq = new Dictionary<int, int>();
        foreach (var w in words) {
            int mask = 0;
            foreach (char c in w) {
                mask |= 1 << (c - 'a');
            }
            if (freq.ContainsKey(mask))
                freq[mask]++;
            else
                freq[mask] = 1;
        }

        int result = 0;
        foreach (var count in freq.Values) {
            result += count * (count - 1) / 2;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var similarPairs = function(words) {
    const freq = new Map();
    for (const w of words) {
        let mask = 0;
        for (let i = 0; i < w.length; i++) {
            mask |= 1 << (w.charCodeAt(i) - 97);
        }
        freq.set(mask, (freq.get(mask) || 0) + 1);
    }
    let ans = 0;
    for (const cnt of freq.values()) {
        ans += cnt * (cnt - 1) / 2;
    }
    return ans;
};
```

## Typescript

```typescript
function similarPairs(words: string[]): number {
    const freq = new Map<number, number>();
    for (const word of words) {
        let mask = 0;
        for (let i = 0; i < word.length; i++) {
            mask |= 1 << (word.charCodeAt(i) - 97);
        }
        freq.set(mask, (freq.get(mask) ?? 0) + 1);
    }
    let result = 0;
    for (const count of freq.values()) {
        result += (count * (count - 1)) >> 1; // same as count*(count-1)/2
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function similarPairs($words) {
        $counts = [];
        $result = 0;
        foreach ($words as $word) {
            $mask = 0;
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $c = ord($word[$i]) - 97; // 'a' ASCII is 97
                $mask |= (1 << $c);
            }
            $key = (string)$mask;
            if (isset($counts[$key])) {
                $result += $counts[$key];
                $counts[$key]++;
            } else {
                $counts[$key] = 1;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func similarPairs(_ words: [String]) -> Int {
        var maskCount = [Int: Int]()
        for word in words {
            var mask = 0
            for byte in word.utf8 {
                let idx = Int(byte - 97) // 'a' ascii is 97
                mask |= (1 << idx)
            }
            maskCount[mask, default: 0] += 1
        }
        var result = 0
        for count in maskCount.values {
            if count > 1 {
                result += count * (count - 1) / 2
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun similarPairs(words: Array<String>): Int {
        val freq = HashMap<Int, Int>()
        for (word in words) {
            var mask = 0
            for (ch in word) {
                mask = mask or (1 shl (ch - 'a'))
            }
            freq[mask] = freq.getOrDefault(mask, 0) + 1
        }
        var result = 0
        for (count in freq.values) {
            result += count * (count - 1) / 2
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int similarPairs(List<String> words) {
    final Map<int, int> freq = {};
    int ans = 0;
    for (var w in words) {
      int mask = 0;
      for (int i = 0; i < w.length; i++) {
        mask |= 1 << (w.codeUnitAt(i) - 97);
      }
      ans += freq[mask] ?? 0;
      freq[mask] = (freq[mask] ?? 0) + 1;
    }
    return ans;
  }
}
```

## Golang

```go
func similarPairs(words []string) int {
    freq := make(map[int]int)
    res := 0
    for _, w := range words {
        mask := 0
        for i := 0; i < len(w); i++ {
            mask |= 1 << (w[i] - 'a')
        }
        if cnt, ok := freq[mask]; ok {
            res += cnt
        }
        freq[mask]++
    }
    return res
}
```

## Ruby

```ruby
def similar_pairs(words)
  freq = Hash.new(0)
  words.each do |w|
    mask = 0
    w.each_byte { |b| mask |= 1 << (b - 97) }
    freq[mask] += 1
  end
  ans = 0
  freq.each_value { |c| ans += c * (c - 1) / 2 }
  ans
end
```

## Scala

```scala
object Solution {
    def similarPairs(words: Array[String]): Int = {
        val freq = scala.collection.mutable.Map[Int, Int]()
        for (word <- words) {
            var mask = 0
            for (ch <- word) {
                mask |= 1 << (ch - 'a')
            }
            freq.update(mask, freq.getOrElse(mask, 0) + 1)
        }
        var result: Long = 0L
        for ((_, count) <- freq) {
            result += count.toLong * (count - 1) / 2
        }
        result.toInt
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn similar_pairs(words: Vec<String>) -> i32 {
        let mut freq: HashMap<u32, i32> = HashMap::new();
        for w in words.iter() {
            let mut mask: u32 = 0;
            for &b in w.as_bytes() {
                mask |= 1 << (b - b'a');
            }
            *freq.entry(mask).or_insert(0) += 1;
        }
        let mut ans = 0i32;
        for &cnt in freq.values() {
            if cnt > 1 {
                ans += cnt * (cnt - 1) / 2;
            }
        }
        ans
    }
}
```

## Racket

```racket
#lang racket

(provide similar-pairs)

(define (mask-of s)
  (let loop ((i 0) (m 0))
    (if (= i (string-length s))
        m
        (let* ((c (string-ref s i))
               (bit (- (char->integer c) (char->integer #\a)))
               (new-m (bitwise-ior m (arithmetic-shift 1 bit))))
          (loop (+ i 1) new-m)))))

(define/contract (similar-pairs words)
  (-> (listof string?) exact-integer?)
  (let ((freq (make-hash)))
    (for ([w words])
      (define m (mask-of w))
      (hash-set! freq m (+ 1 (hash-ref freq m 0))))
    (for/sum ([cnt (in-hash-values freq)])
      (quotient (* cnt (- cnt 1)) 2))))
```

## Erlang

```erlang
-module(solution).
-export([similar_pairs/1]).

-spec similar_pairs(Words :: [unicode:unicode_binary()]) -> integer().
similar_pairs(Words) ->
    Counts = lists:foldl(fun(W, Map) ->
        Mask = mask_word(W),
        maps:update_with(Mask, fun(C) -> C + 1 end, 1, Map)
    end, #{}, Words),
    lists:foldl(fun({_Mask, Cnt}, Sum) ->
        Sum + (Cnt * (Cnt - 1)) div 2
    end, 0, maps:to_list(Counts)).

mask_word(Word) -> mask_word(Word, 0).

mask_word(<<>>, Acc) -> Acc;
mask_word(<<Char:8, Rest/binary>>, Acc) ->
    Bit = Char - $a,
    NewAcc = Acc bor (1 bsl Bit),
    mask_word(Rest, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec similar_pairs(words :: [String.t]) :: integer
  def similar_pairs(words) do
    masks =
      Enum.map(words, fn word ->
        String.to_charlist(word)
        |> Enum.reduce(0, fn char, acc ->
          acc ||| (1 <<< (char - ?a))
        end)
      end)

    freq =
      Enum.reduce(masks, %{}, fn mask, map ->
        Map.update(map, mask, 1, &(&1 + 1))
      end)

    Enum.reduce(freq, 0, fn {_mask, cnt}, acc ->
      acc + div(cnt * (cnt - 1), 2)
    end)
  end
end
```
