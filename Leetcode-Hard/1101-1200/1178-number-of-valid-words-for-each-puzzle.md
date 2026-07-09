# 1178. Number of Valid Words for Each Puzzle

## Cpp

```cpp
class Solution {
public:
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        unordered_map<int,int> freq;
        freq.reserve(words.size()*2);
        for (const string& w : words) {
            int mask = 0;
            for (char c : w) mask |= 1 << (c - 'a');
            ++freq[mask];
        }
        vector<int> ans;
        ans.reserve(puzzles.size());
        for (const string& p : puzzles) {
            int puzzleMask = 0;
            for (char c : p) puzzleMask |= 1 << (c - 'a');
            int firstBit = 1 << (p[0] - 'a');
            int sub = puzzleMask;
            int total = 0;
            while (true) {
                if (sub & firstBit) {
                    auto it = freq.find(sub);
                    if (it != freq.end()) total += it->second;
                }
                if (sub == firstBit) break;
                sub = (sub - 1) & puzzleMask;
            }
            ans.push_back(total);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public List<Integer> findNumOfValidWords(String[] words, String[] puzzles) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (String w : words) {
            int mask = 0;
            for (int i = 0; i < w.length(); i++) {
                mask |= 1 << (w.charAt(i) - 'a');
            }
            if (Integer.bitCount(mask) <= 7) {
                freq.put(mask, freq.getOrDefault(mask, 0) + 1);
            }
        }

        List<Integer> result = new ArrayList<>(puzzles.length);
        for (String p : puzzles) {
            int puzzleMask = 0;
            for (int i = 0; i < 7; i++) {
                puzzleMask |= 1 << (p.charAt(i) - 'a');
            }
            int firstBit = 1 << (p.charAt(0) - 'a');

            int submask = puzzleMask;
            int count = 0;
            while (submask != 0) {
                if ((submask & firstBit) != 0) {
                    count += freq.getOrDefault(submask, 0);
                }
                submask = (submask - 1) & puzzleMask;
            }
            result.add(count);
        }

        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        from collections import Counter

        # Build frequency map of word bitmasks (ignore duplicate letters in a word)
        freq = Counter()
        for w in words:
            mask = 0
            for ch in set(w):
                mask |= 1 << (ord(ch) - 97)
            # A valid word must have at most 7 distinct letters to match any puzzle
            if bin(mask).count('1') <= 7:
                freq[mask] += 1

        ans = []
        for p in puzzles:
            first_bit = 1 << (ord(p[0]) - 97)
            # mask of all letters in the puzzle
            puzzle_mask = 0
            for ch in p:
                puzzle_mask |= 1 << (ord(ch) - 97)

            # bits excluding the mandatory first letter
            submask = puzzle_mask ^ first_bit

            total = 0
            s = submask
            while True:
                candidate = s | first_bit
                total += freq.get(candidate, 0)
                if s == 0:
                    break
                s = (s - 1) & submask
            ans.append(total)

        return ans
```

## Python3

```python
from typing import List
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        from collections import Counter

        # Count frequency of each word mask (ignore masks with >7 bits)
        word_cnt = Counter()
        for w in words:
            mask = 0
            for ch in set(w):  # unique letters only
                mask |= 1 << (ord(ch) - ord('a'))
            if bin(mask).count('1') <= 7:  # only relevant masks
                word_cnt[mask] += 1

        res = []
        for p in puzzles:
            first_bit = 1 << (ord(p[0]) - ord('a'))
            puzzle_mask = 0
            for ch in p:
                puzzle_mask |= 1 << (ord(ch) - ord('a'))

            submask = puzzle_mask
            total = 0
            while submask:
                if submask & first_bit:
                    total += word_cnt.get(submask, 0)
                submask = (submask - 1) & puzzle_mask
            res.append(total)
        return res
```

## C

```c
#include <stdlib.h>
#include <stdint.h>

static uint32_t *hash_keys;
static int *hash_vals;
static char *hash_used;
static uint32_t hash_cap;

static inline void hashmap_inc(uint32_t key) {
    uint32_t idx = (key * 2654435761u) & (hash_cap - 1);
    while (hash_used[idx]) {
        if (hash_keys[idx] == key) {
            ++hash_vals[idx];
            return;
        }
        idx = (idx + 1) & (hash_cap - 1);
    }
    hash_used[idx] = 1;
    hash_keys[idx] = key;
    hash_vals[idx] = 1;
}

static inline int hashmap_get(uint32_t key) {
    uint32_t idx = (key * 2654435761u) & (hash_cap - 1);
    while (hash_used[idx]) {
        if (hash_keys[idx] == key) return hash_vals[idx];
        idx = (idx + 1) & (hash_cap - 1);
    }
    return 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findNumOfValidWords(char** words, int wordsSize, char** puzzles, int puzzlesSize, int* returnSize) {
    /* Build hashmap of word masks */
    uint32_t cap = 1;
    while (cap < (uint32_t)wordsSize * 2) cap <<= 1;
    hash_cap = cap;
    hash_keys = (uint32_t*)calloc(cap, sizeof(uint32_t));
    hash_vals = (int*)calloc(cap, sizeof(int));
    hash_used = (char*)calloc(cap, sizeof(char));

    for (int i = 0; i < wordsSize; ++i) {
        uint32_t mask = 0;
        char *w = words[i];
        while (*w) {
            mask |= 1u << (*w - 'a');
            ++w;
        }
        hashmap_inc(mask);
    }

    int *result = (int*)malloc(puzzlesSize * sizeof(int));
    for (int i = 0; i < puzzlesSize; ++i) {
        char *p = puzzles[i];
        uint32_t firstMask = 1u << (p[0] - 'a');
        uint32_t otherMasks[6];
        for (int j = 0; j < 6; ++j)
            otherMasks[j] = 1u << (p[j + 1] - 'a');

        int total = 0;
        for (int sub = 0; sub < (1 << 6); ++sub) {
            uint32_t cur = firstMask;
            for (int j = 0; j < 6; ++j)
                if (sub & (1 << j)) cur |= otherMasks[j];
            total += hashmap_get(cur);
        }
        result[i] = total;
    }

    free(hash_keys);
    free(hash_vals);
    free(hash_used);

    *returnSize = puzzlesSize;
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> FindNumOfValidWords(string[] words, string[] puzzles) {
        var freq = new Dictionary<int, int>();
        foreach (var w in words) {
            int mask = 0;
            foreach (char c in w) {
                mask |= 1 << (c - 'a');
            }
            if (PopCount(mask) <= 7) {
                if (freq.ContainsKey(mask))
                    freq[mask]++;
                else
                    freq[mask] = 1;
            }
        }

        var result = new List<int>(puzzles.Length);
        foreach (var p in puzzles) {
            int firstBit = 1 << (p[0] - 'a');
            int puzzleMask = 0;
            foreach (char c in p) {
                puzzleMask |= 1 << (c - 'a');
            }

            int sub = puzzleMask;
            int total = 0;
            while (true) {
                if ((sub & firstBit) != 0 && freq.TryGetValue(sub, out int cnt)) {
                    total += cnt;
                }
                if (sub == 0) break;
                sub = (sub - 1) & puzzleMask;
            }

            result.Add(total);
        }

        return result;
    }

    private int PopCount(int x) {
        int count = 0;
        while (x != 0) {
            x &= x - 1;
            count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {string[]} puzzles
 * @return {number[]}
 */
var findNumOfValidWords = function(words, puzzles) {
    const freq = new Map();

    // helper to compute bitmask of a string
    const getMask = (s) => {
        let mask = 0;
        for (let i = 0; i < s.length; ++i) {
            mask |= 1 << (s.charCodeAt(i) - 97);
        }
        return mask;
    };

    // count word masks, ignore those with >7 distinct letters
    const bitCount = (x) => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            ++cnt;
        }
        return cnt;
    };

    for (const w of words) {
        const m = getMask(w);
        if (bitCount(m) <= 7) {
            freq.set(m, (freq.get(m) || 0) + 1);
        }
    }

    const res = [];

    for (const p of puzzles) {
        const firstBit = 1 << (p.charCodeAt(0) - 97);
        let puzzleMask = 0;
        for (let i = 0; i < 7; ++i) {
            puzzleMask |= 1 << (p.charCodeAt(i) - 97);
        }

        let total = 0;
        // iterate all subsets of puzzleMask
        for (let sub = puzzleMask; sub; sub = (sub - 1) & puzzleMask) {
            if ((sub & firstBit) !== 0) {
                const cnt = freq.get(sub);
                if (cnt !== undefined) total += cnt;
            }
        }
        // also need to consider the subset that is exactly firstBit when loop ends at 0
        // but the above loop already includes it because sub will eventually become firstBit.
        res.push(total);
    }

    return res;
};
```

## Typescript

```typescript
function findNumOfValidWords(words: string[], puzzles: string[]): number[] {
    const freq = new Map<number, number>();
    for (const w of words) {
        let mask = 0;
        for (let i = 0; i < w.length; i++) {
            mask |= 1 << (w.charCodeAt(i) - 97);
        }
        freq.set(mask, (freq.get(mask) ?? 0) + 1);
    }

    const result: number[] = [];
    for (const p of puzzles) {
        let puzzleMask = 0;
        for (let i = 0; i < p.length; i++) {
            puzzleMask |= 1 << (p.charCodeAt(i) - 97);
        }
        const firstBit = 1 << (p.charCodeAt(0) - 97);
        let sub = puzzleMask;
        let count = 0;
        while (sub) {
            if ((sub & firstBit) !== 0) {
                const c = freq.get(sub);
                if (c !== undefined) count += c;
            }
            sub = (sub - 1) & puzzleMask;
        }
        result.push(count);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @param String[] $puzzles
     * @return Integer[]
     */
    function findNumOfValidWords($words, $puzzles) {
        $freq = [];
        foreach ($words as $w) {
            $mask = 0;
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) {
                $mask |= 1 << (ord($w[$i]) - 97);
            }
            if (!isset($freq[$mask])) {
                $freq[$mask] = 0;
            }
            $freq[$mask]++;
        }

        $result = [];
        foreach ($puzzles as $p) {
            $firstBit = 1 << (ord($p[0]) - 97);
            $pMask = 0;
            for ($i = 0; $i < 7; $i++) {
                $pMask |= 1 << (ord($p[$i]) - 97);
            }

            $count = 0;
            $submask = $pMask;
            while ($submask) {
                if (($submask & $firstBit) && isset($freq[$submask])) {
                    $count += $freq[$submask];
                }
                $submask = ($submask - 1) & $pMask;
            }

            $result[] = $count;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findNumOfValidWords(_ words: [String], _ puzzles: [String]) -> [Int] {
        var freq = [Int:Int]()
        for w in words {
            var mask = 0
            for ch in w {
                let bit = 1 << (ch.unicodeScalars.first!.value - 97)
                mask |= Int(bit)
            }
            if mask.nonzeroBitCount <= 7 {
                freq[mask, default: 0] += 1
            }
        }
        
        var result = [Int]()
        for p in puzzles {
            let chars = Array(p)
            var puzzleMask = 0
            for ch in chars {
                let bit = 1 << (ch.unicodeScalars.first!.value - 97)
                puzzleMask |= Int(bit)
            }
            let firstBit = 1 << (chars[0].unicodeScalars.first!.value - 97)
            
            var submask = puzzleMask
            var count = 0
            while true {
                if (submask & firstBit) != 0, let c = freq[submask] {
                    count += c
                }
                if submask == 0 { break }
                submask = (submask - 1) & puzzleMask
            }
            result.append(count)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findNumOfValidWords(words: Array<String>, puzzles: Array<String>): List<Int> {
        val freq = HashMap<Int, Int>()
        for (w in words) {
            var mask = 0
            for (c in w) {
                mask = mask or (1 shl (c - 'a'))
            }
            if (Integer.bitCount(mask) <= 7) {
                freq[mask] = (freq[mask] ?: 0) + 1
            }
        }

        val ans = IntArray(puzzles.size)
        for ((i, p) in puzzles.withIndex()) {
            var puzzleMask = 0
            for (c in p) {
                puzzleMask = puzzleMask or (1 shl (c - 'a'))
            }
            val firstBit = 1 shl (p[0] - 'a')
            var submask = puzzleMask
            var count = 0
            while (true) {
                if ((submask and firstBit) != 0) {
                    count += freq[submask] ?: 0
                }
                if (submask == 0) break
                submask = (submask - 1) and puzzleMask
            }
            ans[i] = count
        }
        return ans.toList()
    }
}
```

## Dart

```dart
class Solution {
  List<int> findNumOfValidWords(List<String> words, List<String> puzzles) {
    final Map<int, int> freq = {};
    for (final w in words) {
      int mask = 0;
      for (int i = 0; i < w.length; ++i) {
        mask |= 1 << (w.codeUnitAt(i) - 97);
      }
      if (_bitCount(mask) <= 7) {
        freq[mask] = (freq[mask] ?? 0) + 1;
      }
    }

    final List<int> ans = [];
    for (final p in puzzles) {
      int puzzleMask = 0;
      for (int i = 0; i < p.length; ++i) {
        puzzleMask |= 1 << (p.codeUnitAt(i) - 97);
      }
      int firstMask = 1 << (p.codeUnitAt(0) - 97);
      int sub = puzzleMask;
      int total = 0;
      while (true) {
        if ((sub & firstMask) != 0) {
          total += freq[sub] ?? 0;
        }
        if (sub == firstMask) break;
        sub = (sub - 1) & puzzleMask;
      }
      ans.add(total);
    }

    return ans;
  }

  int _bitCount(int x) {
    int cnt = 0;
    while (x != 0) {
      x &= x - 1;
      cnt++;
    }
    return cnt;
  }
}
```

## Golang

```go
import "math/bits"

func findNumOfValidWords(words []string, puzzles []string) []int {
	freq := make(map[int]int)
	for _, w := range words {
		mask := 0
		for i := 0; i < len(w); i++ {
			mask |= 1 << (w[i] - 'a')
		}
		if bits.OnesCount(uint(mask)) <= 7 {
			freq[mask]++
		}
	}

	ans := make([]int, len(puzzles))
	for i, p := range puzzles {
		firstBit := 1 << (p[0] - 'a')
		otherMask := 0
		for j := 1; j < 7; j++ {
			otherMask |= 1 << (p[j] - 'a')
		}
		sub := otherMask
		total := 0
		for {
			candidate := sub | firstBit
			if cnt, ok := freq[candidate]; ok {
				total += cnt
			}
			if sub == 0 {
				break
			}
			sub = (sub - 1) & otherMask
		}
		ans[i] = total
	}
	return ans
}
```

## Ruby

```ruby
# @param {String[]} words
# @param {String[]} puzzles
# @return {Integer[]}
def find_num_of_valid_words(words, puzzles)
  mask_counts = Hash.new(0)

  words.each do |w|
    mask = 0
    w.each_byte { |b| mask |= 1 << (b - 97) }
    mask_counts[mask] += 1
  end

  result = []

  puzzles.each do |p|
    first_bit = 1 << (p.getbyte(0) - 97)
    puzzle_mask = 0
    p.each_byte { |b| puzzle_mask |= 1 << (b - 97) }

    rest = puzzle_mask ^ first_bit
    sub = rest
    count = 0

    loop do
      candidate = sub | first_bit
      count += mask_counts[candidate]
      break if sub == 0
      sub = (sub - 1) & rest
    end

    result << count
  end

  result
end
```

## Scala

```scala
object Solution {
    def findNumOfValidWords(words: Array[String], puzzles: Array[String]): List[Int] = {
        val wordMap = scala.collection.mutable.Map[Int, Int]()
        for (w <- words) {
            var mask = 0
            for (c <- w) {
                mask |= 1 << (c - 'a')
            }
            if (Integer.bitCount(mask) <= 7) {
                wordMap.update(mask, wordMap.getOrElse(mask, 0) + 1)
            }
        }

        val result = new Array[Int](puzzles.length)

        for ((puzzle, idx) <- puzzles.zipWithIndex) {
            var puzzleMask = 0
            for (c <- puzzle) {
                puzzleMask |= 1 << (c - 'a')
            }
            val firstBit = 1 << (puzzle.charAt(0) - 'a')

            var sub = puzzleMask
            while (sub > 0) {
                if ((sub & firstBit) != 0) {
                    result(idx) += wordMap.getOrElse(sub, 0)
                }
                sub = (sub - 1) & puzzleMask
            }
        }

        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_num_of_valid_words(words: Vec<String>, puzzles: Vec<String>) -> Vec<i32> {
        use std::collections::HashMap;
        let mut freq: HashMap<u32, i32> = HashMap::new();
        for w in words.iter() {
            let mut mask: u32 = 0;
            for &b in w.as_bytes() {
                mask |= 1u32 << ((b - b'a') as u32);
            }
            *freq.entry(mask).or_insert(0) += 1;
        }

        let mut ans: Vec<i32> = Vec::with_capacity(puzzles.len());
        for p in puzzles.iter() {
            let bytes = p.as_bytes();
            let first_bit = 1u32 << ((bytes[0] - b'a') as u32);
            let mut puzzle_mask: u32 = 0;
            for &b in bytes {
                puzzle_mask |= 1u32 << ((b - b'a') as u32);
            }
            let mask_without_first = puzzle_mask ^ first_bit;

            let mut sub = mask_without_first;
            let mut total: i32 = 0;
            loop {
                let candidate = sub | first_bit;
                if let Some(&cnt) = freq.get(&candidate) {
                    total += cnt;
                }
                if sub == 0 {
                    break;
                }
                sub = (sub - 1) & mask_without_first;
            }
            ans.push(total);
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (find-num-of-valid-words words puzzles)
  (-> (listof string?) (listof string?) (listof exact-integer?))
  (letrec
      ((char-index
        (lambda (c) (- (char->integer c) (char->integer #\a))))
       
       (string->mask
        (lambda (s)
          (let loop ((i 0) (len (string-length s)) (m 0))
            (if (= i len)
                m
                (let* ((bit (char-index (string-ref s i)))
                       (new-m (bitwise-ior m (arithmetic-shift 1 bit))))
                  (loop (+ i 1) len new-m))))))
       
       (popcount
        (lambda (n)
          (let loop ((x n) (c 0))
            (if (= x 0)
                c
                (loop (arithmetic-shift x -1)
                      (+ c (if (= (bitwise-and x 1) 1) 1 0)))))))
       
       (build-word-hash
        (lambda ()
          (let ((h (make-hash)))
            (for ([w words])
              (let ((mask (string->mask w)))
                (when (<= (popcount mask) 7)
                  (hash-update! h mask add1 0))))
            h)))
       
       (word-hash (build-word-hash))
       
       (process-puzzle
        (lambda (puz)
          (let* ((p-mask (string->mask puz))
                 (first-bit (arithmetic-shift 1 (char-index (string-ref puz 0)))))
            (let loop ((sub p-mask) (total 0))
              (if (= sub 0)
                  total
                  (let ((new-total
                         (if (not (= (bitwise-and sub first-bit) 0))
                             (+ total (hash-ref word-hash sub 0))
                             total)))
                    (loop (bitwise-and (- sub 1) p-mask) new-total))))))))
    (let loop ((ps puzzles) (acc '()))
      (if (null? ps)
          (reverse acc)
          (loop (cdr ps) (cons (process-puzzle (car ps)) acc))))) )
```

## Erlang

```erlang
-module(solution).
-export([find_num_of_valid_words/2]).

-spec find_num_of_valid_words(Words :: [unicode:unicode_binary()], Puzzles :: [unicode:unicode_binary()]) -> [integer()].
find_num_of_valid_words(Words, Puzzles) ->
    WordMap = build_word_map(Words),
    lists:map(fun(Puzzle) -> count_for_puzzle(Puzzle, WordMap) end, Puzzles).

%% Build a map from word bitmask to its frequency
build_word_map(Words) ->
    lists:foldl(
        fun(Word, Acc) ->
            Mask = word_mask(Word),
            Count = maps:get(Mask, Acc, 0),
            maps:put(Mask, Count + 1, Acc)
        end,
        #{},
        Words).

%% Convert a word to its bitmask (unique letters)
word_mask(Bin) -> word_mask(Bin, 0).
word_mask(<<>>, Acc) -> Acc;
word_mask(<<C, Rest/binary>>, Acc) ->
    NewAcc = Acc bor (1 bsl (C - $a)),
    word_mask(Rest, NewAcc).

%% Count valid words for a single puzzle
count_for_puzzle(PuzzleBin, WordMap) ->
    <<FChar, L1, L2, L3, L4, L5, L6>> = PuzzleBin,
    FirstMask = 1 bsl (FChar - $a),
    OthersMasks = [
        1 bsl (L1 - $a),
        1 bsl (L2 - $a),
        1 bsl (L3 - $a),
        1 bsl (L4 - $a),
        1 bsl (L5 - $a),
        1 bsl (L6 - $a)
    ],
    count_subsets(0, OthersMasks, FirstMask, WordMap).

%% Iterate over all subsets of the six remaining letters (2^6 = 64)
count_subsets(Index, Masks, FirstMask, Map) when Index =< 63 ->
    Mask = build_mask_from_subset(Index, Masks, FirstMask),
    Count = maps:get(Mask, Map, 0),
    Count + count_subsets(Index + 1, Masks, FirstMask, Map);
count_subsets(_, _, _, _) -> 0.

%% Build mask for a particular subset index
build_mask_from_subset(SubIdx, Masks, FirstMask) ->
    lists:foldl(
        fun({Pos, M}, Acc) ->
            case (SubIdx band (1 bsl Pos)) of
                0 -> Acc;
                _ -> Acc bor M
            end
        end,
        FirstMask,
        lists:zip(lists:seq(0,5), Masks)).
```

## Elixir

```elixir
defmodule Solution do
  require Bitwise

  @spec find_num_of_valid_words(words :: [String.t()], puzzles :: [String.t()]) :: [integer()]
  def find_num_of_valid_words(words, puzzles) do
    freq =
      Enum.reduce(words, %{}, fn word, acc ->
        mask = word_to_mask(word)

        Map.update(acc, mask, 1, &(&1 + 1))
      end)

    Enum.map(puzzles, fn puzzle ->
      first_char = String.at(puzzle, 0) |> :binary.first()
      first_bit = 1 <<< (first_char - ?a)
      rest_mask = rest_to_mask(String.slice(puzzle, 1, 6))

      count_submasks(rest_mask, first_bit, freq)
    end)
  end

  defp word_to_mask(word) do
    word
    |> String.to_charlist()
    |> Enum.reduce(0, fn c, acc -> Bitwise.bor(acc, 1 <<< (c - ?a)) end)
  end

  defp rest_to_mask(rest) do
    rest
    |> String.to_charlist()
    |> Enum.reduce(0, fn c, acc -> Bitwise.bor(acc, 1 <<< (c - ?a)) end)
  end

  defp count_submasks(mask_rest, first_bit, freq) do
    do_count(mask_rest, mask_rest, first_bit, freq, 0)
  end

  defp do_count(0, _mask_rest, first_bit, freq, acc) do
    candidate = Bitwise.bor(0, first_bit)
    acc + Map.get(freq, candidate, 0)
  end

  defp do_count(submask, mask_rest, first_bit, freq, acc) do
    candidate = Bitwise.bor(submask, first_bit)
    new_acc = acc + Map.get(freq, candidate, 0)

    next_submask = Bitwise.band(submask - 1, mask_rest)
    do_count(next_submask, mask_rest, first_bit, freq, new_acc)
  end
end
```
