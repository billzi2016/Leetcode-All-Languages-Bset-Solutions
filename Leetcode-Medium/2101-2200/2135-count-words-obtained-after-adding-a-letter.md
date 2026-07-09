# 2135. Count Words Obtained After Adding a Letter

## Cpp

```cpp
class Solution {
public:
    int wordCount(vector<string>& startWords, vector<string>& targetWords) {
        unordered_set<int> masks;
        for (const string& w : startWords) {
            int m = 0;
            for (char c : w) m |= 1 << (c - 'a');
            masks.insert(m);
        }
        int ans = 0;
        for (const string& w : targetWords) {
            int fullMask = 0;
            for (char c : w) fullMask |= 1 << (c - 'a');
            // try removing each letter
            for (int i = 0; i < 26; ++i) {
                if (fullMask & (1 << i)) {
                    int cand = fullMask ^ (1 << i);
                    if (masks.find(cand) != masks.end()) {
                        ++ans;
                        break;
                    }
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int wordCount(String[] startWords, String[] targetWords) {
        Set<Integer> masks = new HashSet<>();
        for (String s : startWords) {
            int mask = 0;
            for (char c : s.toCharArray()) {
                mask |= 1 << (c - 'a');
            }
            masks.add(mask);
        }

        int count = 0;
        for (String t : targetWords) {
            int mask = 0;
            for (char c : t.toCharArray()) {
                mask |= 1 << (c - 'a');
            }
            for (int i = 0; i < 26; ++i) {
                if ((mask & (1 << i)) != 0) {
                    int candidate = mask ^ (1 << i);
                    if (masks.contains(candidate)) {
                        count++;
                        break;
                    }
                }
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def wordCount(self, startWords, targetWords):
        """
        :type startWords: List[str]
        :type targetWords: List[str]
        :rtype: int
        """
        start_set = set()
        for w in startWords:
            mask = 0
            for ch in w:
                mask |= 1 << (ord(ch) - 97)
            start_set.add(mask)

        ans = 0
        for w in targetWords:
            mask = 0
            for ch in w:
                mask |= 1 << (ord(ch) - 97)
            m = mask
            while m:
                lowbit = m & -m
                if (mask ^ lowbit) in start_set:
                    ans += 1
                    break
                m ^= lowbit
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        # Convert each start word to a bitmask and store in a set
        start_masks = set()
        for w in startWords:
            mask = 0
            for ch in w:
                mask |= 1 << (ord(ch) - ord('a'))
            start_masks.add(mask)

        result = 0
        for w in targetWords:
            # Compute mask of the target word
            tmask = 0
            for ch in w:
                tmask |= 1 << (ord(ch) - ord('a'))

            # Try removing each character; if resulting mask exists, count it
            found = False
            m = tmask
            while m:
                # isolate lowest set bit
                lowbit = m & -m
                candidate = tmask ^ lowbit  # remove this letter
                if candidate in start_masks:
                    found = True
                    break
                m ^= lowbit  # clear the processed bit
            if found:
                result += 1

        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

static int exists(int *arr, int size, int key) {
    int l = 0, r = size - 1;
    while (l <= r) {
        int m = l + ((r - l) >> 1);
        if (arr[m] == key) return 1;
        if (arr[m] < key) l = m + 1;
        else r = m - 1;
    }
    return 0;
}

int wordCount(char** startWords, int startWordsSize, char** targetWords, int targetWordsSize) {
    int *startMasks = (int *)malloc(startWordsSize * sizeof(int));
    for (int i = 0; i < startWordsSize; ++i) {
        unsigned int mask = 0;
        const char *s = startWords[i];
        while (*s) {
            mask |= 1u << (*s - 'a');
            ++s;
        }
        startMasks[i] = (int)mask;
    }

    qsort(startMasks, startWordsSize, sizeof(int), cmp_int);

    int result = 0;
    for (int i = 0; i < targetWordsSize; ++i) {
        unsigned int mask = 0;
        const char *s = targetWords[i];
        while (*s) {
            mask |= 1u << (*s - 'a');
            ++s;
        }
        for (int b = 0; b < 26; ++b) {
            if (mask & (1u << b)) {
                int cand = (int)(mask ^ (1u << b));
                if (exists(startMasks, startWordsSize, cand)) {
                    ++result;
                    break;
                }
            }
        }
    }

    free(startMasks);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int WordCount(string[] startWords, string[] targetWords)
    {
        var startSet = new HashSet<int>();
        foreach (var w in startWords)
        {
            int mask = 0;
            foreach (char c in w)
                mask |= 1 << (c - 'a');
            startSet.Add(mask);
        }

        int result = 0;
        foreach (var w in targetWords)
        {
            int mask = 0;
            foreach (char c in w)
                mask |= 1 << (c - 'a');

            int temp = mask;
            while (temp != 0)
            {
                int lowbit = temp & -temp;
                int removedMask = mask ^ lowbit;
                if (startSet.Contains(removedMask))
                {
                    result++;
                    break;
                }
                temp -= lowbit;
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} startWords
 * @param {string[]} targetWords
 * @return {number}
 */
var wordCount = function(startWords, targetWords) {
    const startSet = new Set();
    for (const w of startWords) {
        let mask = 0;
        for (let i = 0; i < w.length; i++) {
            mask |= 1 << (w.charCodeAt(i) - 97);
        }
        startSet.add(mask);
    }

    let result = 0;
    for (const t of targetWords) {
        let fullMask = 0;
        for (let i = 0; i < t.length; i++) {
            fullMask |= 1 << (t.charCodeAt(i) - 97);
        }
        for (let i = 0; i < t.length; i++) {
            const bit = 1 << (t.charCodeAt(i) - 97);
            const candidate = fullMask ^ bit;
            if (startSet.has(candidate)) {
                result++;
                break;
            }
        }
    }
    return result;
};
```

## Typescript

```typescript
function wordCount(startWords: string[], targetWords: string[]): number {
    const startSet = new Set<number>();
    for (const w of startWords) {
        let mask = 0;
        for (const ch of w) {
            mask |= 1 << (ch.charCodeAt(0) - 97);
        }
        startSet.add(mask);
    }

    let count = 0;
    for (const t of targetWords) {
        let mask = 0;
        for (const ch of t) {
            mask |= 1 << (ch.charCodeAt(0) - 97);
        }
        for (let i = 0; i < 26; i++) {
            if ((mask & (1 << i)) !== 0) {
                const candidate = mask ^ (1 << i);
                if (startSet.has(candidate)) {
                    count++;
                    break;
                }
            }
        }
    }

    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $startWords
     * @param String[] $targetWords
     * @return Integer
     */
    function wordCount($startWords, $targetWords) {
        $set = [];
        foreach ($startWords as $w) {
            $chars = str_split($w);
            sort($chars);
            $key = implode('', $chars);
            $set[$key] = true;
        }

        $count = 0;
        foreach ($targetWords as $tw) {
            $len = strlen($tw);
            for ($i = 0; $i < $len; $i++) {
                $removed = substr($tw, 0, $i) . substr($tw, $i + 1);
                $chars = str_split($removed);
                sort($chars);
                $key = implode('', $chars);
                if (isset($set[$key])) {
                    $count++;
                    break;
                }
            }
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func wordCount(_ startWords: [String], _ targetWords: [String]) -> Int {
        var startSet = Set<Int>()
        for w in startWords {
            var mask = 0
            for c in w.utf8 {
                let bit = Int(c - 97)
                mask |= (1 << bit)
            }
            startSet.insert(mask)
        }
        
        var result = 0
        for t in targetWords {
            var mask = 0
            var chars: [UInt8] = []
            for c in t.utf8 {
                let bit = Int(c - 97)
                mask |= (1 << bit)
                chars.append(c)
            }
            var canForm = false
            for c in chars {
                let bit = Int(c - 97)
                let removedMask = mask ^ (1 << bit)
                if startSet.contains(removedMask) {
                    canForm = true
                    break
                }
            }
            if canForm { result += 1 }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun wordCount(startWords: Array<String>, targetWords: Array<String>): Int {
        val startMasks = HashSet<Int>()
        for (w in startWords) {
            var mask = 0
            for (c in w) {
                mask = mask or (1 shl (c - 'a'))
            }
            startMasks.add(mask)
        }

        var count = 0
        for (t in targetWords) {
            var fullMask = 0
            for (c in t) {
                fullMask = fullMask or (1 shl (c - 'a'))
            }
            var found = false
            for (c in t) {
                val maskWithout = fullMask xor (1 shl (c - 'a'))
                if (startMasks.contains(maskWithout)) {
                    found = true
                    break
                }
            }
            if (found) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int wordCount(List<String> startWords, List<String> targetWords) {
    final Set<int> startSet = {};
    for (final w in startWords) {
      int mask = 0;
      for (int i = 0; i < w.length; ++i) {
        mask |= 1 << (w.codeUnitAt(i) - 97);
      }
      startSet.add(mask);
    }

    int result = 0;
    for (final t in targetWords) {
      int mask = 0;
      for (int i = 0; i < t.length; ++i) {
        mask |= 1 << (t.codeUnitAt(i) - 97);
      }
      int temp = mask;
      while (temp != 0) {
        int lowbit = temp & -temp;
        int candidate = mask ^ lowbit;
        if (startSet.contains(candidate)) {
          result++;
          break;
        }
        temp ^= lowbit;
      }
    }

    return result;
  }
}
```

## Golang

```go
func wordCount(startWords []string, targetWords []string) int {
    masks := make(map[int]struct{}, len(startWords))
    for _, w := range startWords {
        m := 0
        for _, c := range w {
            m |= 1 << (c - 'a')
        }
        masks[m] = struct{}{}
    }

    count := 0
    for _, w := range targetWords {
        fullMask := 0
        for _, c := range w {
            fullMask |= 1 << (c - 'a')
        }
        for _, c := range w {
            reduced := fullMask ^ (1 << (c - 'a'))
            if _, ok := masks[reduced]; ok {
                count++
                break
            }
        }
    }
    return count
}
```

## Ruby

```ruby
def word_count(start_words, target_words)
  require 'set'
  start_set = Set.new
  start_words.each do |w|
    mask = 0
    w.each_byte { |b| mask |= 1 << (b - 97) }
    start_set.add(mask)
  end

  count = 0
  target_words.each do |tw|
    mask = 0
    tw.each_byte { |b| mask |= 1 << (b - 97) }
    tw.each_byte do |b|
      if start_set.include?(mask ^ (1 << (b - 97)))
        count += 1
        break
      end
    end
  end

  count
end
```

## Scala

```scala
object Solution {
  def wordCount(startWords: Array[String], targetWords: Array[String]): Int = {
    val startSet = scala.collection.mutable.HashSet[Int]()
    for (w <- startWords) {
      var mask = 0
      for (c <- w) mask |= 1 << (c - 'a')
      startSet.add(mask)
    }

    var count = 0
    for (tw <- targetWords) {
      var mask = 0
      for (c <- tw) mask |= 1 << (c - 'a')

      var found = false
      var i = 0
      while (i < 26 && !found) {
        val bit = 1 << i
        if ((mask & bit) != 0) {
          val candidate = mask ^ bit
          if (startSet.contains(candidate)) {
            count += 1
            found = true
          }
        }
        i += 1
      }
    }
    count
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn word_count(start_words: Vec<String>, target_words: Vec<String>) -> i32 {
        // Convert each start word to a bitmask and store in a hash set
        let mut start_set: HashSet<u32> = HashSet::new();
        for w in start_words.iter() {
            let mut mask: u32 = 0;
            for b in w.bytes() {
                mask |= 1 << (b - b'a');
            }
            start_set.insert(mask);
        }

        // For each target word, try removing one character and see if the resulting mask exists
        let mut count = 0i32;
        for t in target_words.iter() {
            let mut full_mask: u32 = 0;
            for b in t.bytes() {
                full_mask |= 1 << (b - b'a');
            }
            // Try removing each character
            let mut found = false;
            for b in t.bytes() {
                let mask_without = full_mask ^ (1 << (b - b'a'));
                if start_set.contains(&mask_without) {
                    found = true;
                    break;
                }
            }
            if found {
                count += 1;
            }
        }

        count
    }
}
```

## Racket

```racket
#lang racket

(define (str->mask s)
  (let loop ((i 0) (mask 0))
    (if (= i (string-length s))
        mask
        (let* ((c (string-ref s i))
               (idx (- (char->integer c) (char->integer #\a)))
               (bit (arithmetic-shift 1 idx))
               (new-mask (bitwise-ior mask bit)))
          (loop (+ i 1) new-mask)))))

(define/contract (word-count startWords targetWords)
  (-> (listof string?) (listof string?) exact-integer?)
  (let ((start-set (make-hash)))
    (for ([w startWords])
      (hash-set! start-set (str->mask w) #t))
    (define count 0)
    (for ([tw targetWords])
      (let* ((tm (str->mask tw))
             (len (string-length tw))
             (found #f))
        (for ([i (in-range len)] #:break found)
          (let* ((c (string-ref tw i))
                 (idx (- (char->integer c) (char->integer #\a)))
                 (bit (arithmetic-shift 1 idx))
                 (candidate (bitwise-xor tm bit)))
            (when (hash-has-key? start-set candidate)
              (set! count (+ count 1))
              (set! found #t))))))
    count))
```

## Erlang

```erlang
-module(solution).
-export([word_count/2]).

-spec word_count([unicode:unicode_binary()], [unicode:unicode_binary()]) -> integer().
word_count(StartWords, TargetWords) ->
    Set = lists:foldl(fun(W, M) -> maps:put(word_to_mask(W), true, M) end, #{}, StartWords),
    count_targets(TargetWords, Set, 0).

%% Convert a word (binary) to a bitmask where each bit represents a letter.
word_to_mask(Bin) when is_binary(Bin) ->
    word_to_mask(Bin, 0).

word_to_mask(<<>>, Acc) -> Acc;
word_to_mask(<<C, Rest/binary>>, Acc) ->
    Bit = C - $a,
    NewAcc = Acc bor (1 bsl Bit),
    word_to_mask(Rest, NewAcc).

%% Count how many target words can be formed.
count_targets([], _Set, Count) -> Count;
count_targets([W|Ws], Set, Count) ->
    Mask = word_to_mask(W),
    case can_form(Mask, Set) of
        true  -> count_targets(Ws, Set, Count + 1);
        false -> count_targets(Ws, Set, Count)
    end.

%% Check if removing exactly one letter from TargetMask yields a mask present in the set.
can_form(TargetMask, Set) ->
    can_form_bits(TargetMask, Set).

can_form_bits(0, _Set) -> false;
can_form_bits(Mask, Set) ->
    Bit = Mask band -Mask,
    SubMask = Mask bxor Bit,
    case maps:is_key(SubMask, Set) of
        true  -> true;
        false -> can_form_bits(Mask band bnot Bit, Set)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec word_count([String.t()], [String.t()]) :: integer
  def word_count(start_words, target_words) do
    start_set =
      start_words
      |> Enum.map(&word_mask/1)
      |> MapSet.new()

    Enum.reduce(target_words, 0, fn tw, acc ->
      mask = word_mask(tw)

      if can_form?(mask, start_set), do: acc + 1, else: acc
    end)
  end

  defp word_mask(word) do
    String.to_charlist(word)
    |> Enum.reduce(0, fn ch, acc -> acc ||| (1 <<< (ch - ?a)) end)
  end

  defp can_form?(mask, start_set) do
    0..25
    |> Enum.any?(fn i ->
      bit = 1 <<< i
      (mask &&& bit) != 0 and MapSet.member?(start_set, mask ^^^ bit)
    end)
  end
end
```
