# 1002. Find Common Characters

## Cpp

```cpp
class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        if (words.empty()) return {};
        vector<int> common(26, 0);
        for (char c : words[0]) ++common[c - 'a'];
        
        for (size_t i = 1; i < words.size(); ++i) {
            vector<int> cnt(26, 0);
            for (char c : words[i]) ++cnt[c - 'a'];
            for (int j = 0; j < 26; ++j)
                common[j] = min(common[j], cnt[j]);
        }
        
        vector<string> result;
        for (int i = 0; i < 26; ++i) {
            while (common[i]-- > 0)
                result.push_back(string(1, char('a' + i)));
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public List<String> commonChars(String[] words) {
        int[] common = new int[26];
        for (char c : words[0].toCharArray()) {
            common[c - 'a']++;
        }
        for (int i = 1; i < words.length; i++) {
            int[] cur = new int[26];
            for (char c : words[i].toCharArray()) {
                cur[c - 'a']++;
            }
            for (int j = 0; j < 26; j++) {
                common[j] = Math.min(common[j], cur[j]);
            }
        }
        List<String> result = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            while (common[i]-- > 0) {
                result.add(String.valueOf((char) ('a' + i)));
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Initialize frequency counts with the first word
        common = [0] * 26
        for ch in words[0]:
            common[ord(ch) - ord('a')] += 1

        # Intersect with frequencies of each subsequent word
        for w in words[1:]:
            cur = [0] * 26
            for ch in w:
                cur[ord(ch) - ord('a')] += 1
            for i in range(26):
                if common[i] > cur[i]:
                    common[i] = cur[i]

        # Build result list based on the final common frequencies
        res = []
        for i, cnt in enumerate(common):
            res.extend([chr(i + ord('a'))] * cnt)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = [0] * 26
        for ch in words[0]:
            common[ord(ch) - 97] += 1
        for w in words[1:]:
            cur = [0] * 26
            for ch in w:
                cur[ord(ch) - 97] += 1
            for i in range(26):
                if common[i] > cur[i]:
                    common[i] = cur[i]
        result = []
        for i, cnt in enumerate(common):
            result.extend([chr(i + 97)] * cnt)
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>

char** commonChars(char** words, int wordsSize, int* returnSize) {
    if (wordsSize == 0) {
        *returnSize = 0;
        return NULL;
    }
    
    int common[26];
    memset(common, 0, sizeof(common));
    
    // Initialize with counts from the first word
    for (char *p = words[0]; *p; ++p) {
        common[*p - 'a']++;
    }
    
    // Intersect with each subsequent word
    for (int i = 1; i < wordsSize; ++i) {
        int cur[26] = {0};
        for (char *p = words[i]; *p; ++p) {
            cur[*p - 'a']++;
        }
        for (int j = 0; j < 26; ++j) {
            if (common[j] > cur[j]) common[j] = cur[j];
        }
    }
    
    // Count total common characters
    int total = 0;
    for (int j = 0; j < 26; ++j) total += common[j];
    
    char **result = (char **)malloc(total * sizeof(char *));
    int idx = 0;
    for (int j = 0; j < 26; ++j) {
        while (common[j]-- > 0) {
            char *s = (char *)malloc(2 * sizeof(char));
            s[0] = 'a' + j;
            s[1] = '\0';
            result[idx++] = s;
        }
    }
    
    *returnSize = total;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<string> CommonChars(string[] words)
    {
        int[] common = new int[26];
        foreach (char c in words[0])
            common[c - 'a']++;

        for (int w = 1; w < words.Length; w++)
        {
            int[] cur = new int[26];
            foreach (char c in words[w])
                cur[c - 'a']++;

            for (int i = 0; i < 26; i++)
                common[i] = Math.Min(common[i], cur[i]);
        }

        List<string> result = new List<string>();
        for (int i = 0; i < 26; i++)
            for (int cnt = 0; cnt < common[i]; cnt++)
                result.Add(((char)('a' + i)).ToString());

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {string[]}
 */
var commonChars = function(words) {
    const common = new Array(26).fill(Infinity);
    for (const w of words) {
        const cnt = new Array(26).fill(0);
        for (let i = 0; i < w.length; ++i) {
            cnt[w.charCodeAt(i) - 97]++;
        }
        for (let i = 0; i < 26; ++i) {
            common[i] = Math.min(common[i], cnt[i]);
        }
    }
    const result = [];
    for (let i = 0; i < 26; ++i) {
        while (common[i]-- > 0) {
            result.push(String.fromCharCode(i + 97));
        }
    }
    return result;
};
```

## Typescript

```typescript
function commonChars(words: string[]): string[] {
    const common = new Array(26).fill(0);
    for (const ch of words[0]) {
        common[ch.charCodeAt(0) - 97]++;
    }
    for (let i = 1; i < words.length; i++) {
        const cur = new Array(26).fill(0);
        for (const ch of words[i]) {
            cur[ch.charCodeAt(0) - 97]++;
        }
        for (let j = 0; j < 26; j++) {
            common[j] = Math.min(common[j], cur[j]);
        }
    }
    const result: string[] = [];
    for (let i = 0; i < 26; i++) {
        while (common[i] > 0) {
            result.push(String.fromCharCode(97 + i));
            common[i]--;
        }
    }
    return result;
};
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return String[]
     */
    function commonChars($words) {
        $common = array_fill(0, 26, 0);
        // Initialize with first word counts
        $first = $words[0];
        $len = strlen($first);
        for ($i = 0; $i < $len; $i++) {
            $idx = ord($first[$i]) - 97;
            $common[$idx]++;
        }
        // Process remaining words
        $n = count($words);
        for ($w = 1; $w < $n; $w++) {
            $cnt = array_fill(0, 26, 0);
            $word = $words[$w];
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $idx = ord($word[$i]) - 97;
                $cnt[$idx]++;
            }
            // Update common with minimum counts
            for ($j = 0; $j < 26; $j++) {
                $common[$j] = min($common[$j], $cnt[$j]);
            }
        }
        // Build result list
        $result = [];
        for ($i = 0; $i < 26; $i++) {
            while ($common[$i] > 0) {
                $result[] = chr(97 + $i);
                $common[$i]--;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func commonChars(_ words: [String]) -> [String] {
        guard let first = words.first else { return [] }
        var common = Array(repeating: 0, count: 26)
        for byte in first.utf8 {
            common[Int(byte - 97)] += 1
        }
        if words.count > 1 {
            for idx in 1..<words.count {
                var cur = Array(repeating: 0, count: 26)
                for byte in words[idx].utf8 {
                    cur[Int(byte - 97)] += 1
                }
                for i in 0..<26 {
                    common[i] = min(common[i], cur[i])
                }
            }
        }
        var result = [String]()
        for i in 0..<26 {
            let cnt = common[i]
            if cnt > 0 {
                let ch = String(UnicodeScalar(i + 97)!)
                for _ in 0..<cnt {
                    result.append(ch)
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun commonChars(words: Array<String>): List<String> {
        val common = IntArray(26)
        for (c in words[0]) {
            common[c - 'a']++
        }
        for (i in 1 until words.size) {
            val cur = IntArray(26)
            for (c in words[i]) {
                cur[c - 'a']++
            }
            for (j in 0..25) {
                common[j] = kotlin.math.min(common[j], cur[j])
            }
        }
        val result = mutableListOf<String>()
        for (j in 0..25) {
            repeat(common[j]) {
                result.add(('a' + j).toString())
            }
        }
        return result
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  List<String> commonChars(List<String> words) {
    List<int> common = List.filled(26, 0);
    for (int i = 0; i < words[0].length; i++) {
      int idx = words[0].codeUnitAt(i) - 97;
      common[idx]++;
    }
    for (int w = 1; w < words.length; w++) {
      List<int> cur = List.filled(26, 0);
      String word = words[w];
      for (int i = 0; i < word.length; i++) {
        int idx = word.codeUnitAt(i) - 97;
        cur[idx]++;
      }
      for (int i = 0; i < 26; i++) {
        common[i] = min(common[i], cur[i]);
      }
    }
    List<String> result = [];
    for (int i = 0; i < 26; i++) {
      while (common[i] > 0) {
        result.add(String.fromCharCode(i + 97));
        common[i]--;
      }
    }
    return result;
  }
}
```

## Golang

```go
func commonChars(words []string) []string {
	if len(words) == 0 {
		return []string{}
	}
	minCounts := make([]int, 26)
	for _, ch := range words[0] {
		minCounts[int(ch-'a')]++
	}
	curCounts := make([]int, 26)
	for i := 1; i < len(words); i++ {
		for j := 0; j < 26; j++ {
			curCounts[j] = 0
		}
		for _, ch := range words[i] {
			curCounts[int(ch-'a')]++
		}
		for j := 0; j < 26; j++ {
			if curCounts[j] < minCounts[j] {
				minCounts[j] = curCounts[j]
			}
		}
	}
	res := []string{}
	for i := 0; i < 26; i++ {
		for c := 0; c < minCounts[i]; c++ {
			res = append(res, string('a'+i))
		}
	}
	return res
}
```

## Ruby

```ruby
def common_chars(words)
  common = Array.new(26, Float::INFINITY)

  words.each do |word|
    cur = Array.new(26, 0)
    word.each_char { |c| cur[c.ord - 97] += 1 }
    26.times { |i| common[i] = [common[i], cur[i]].min }
  end

  result = []
  26.times do |i|
    cnt = common[i]
    next if cnt == Float::INFINITY || cnt.zero?
    cnt.times { result << (i + 97).chr }
  end
  result
end
```

## Scala

```scala
object Solution {
    def commonChars(words: Array[String]): List[String] = {
        if (words.isEmpty) return Nil
        val common = new Array[Int](26)
        for (c <- words(0)) {
            common(c - 'a') += 1
        }
        for (i <- 1 until words.length) {
            val cur = new Array[Int](26)
            for (c <- words(i)) {
                cur(c - 'a') += 1
            }
            var j = 0
            while (j < 26) {
                common(j) = math.min(common(j), cur(j))
                j += 1
            }
        }
        val result = scala.collection.mutable.ListBuffer[String]()
        var k = 0
        while (k < 26) {
            var cnt = common(k)
            while (cnt > 0) {
                result += ((('a' + k).toChar).toString)
                cnt -= 1
            }
            k += 1
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn common_chars(words: Vec<String>) -> Vec<String> {
        if words.is_empty() {
            return Vec::new();
        }
        let mut common = [0usize; 26];
        // Initialize with the first word's frequencies
        for &b in words[0].as_bytes() {
            common[(b - b'a') as usize] += 1;
        }
        // Intersect with each subsequent word
        for w in words.iter().skip(1) {
            let mut cur = [0usize; 26];
            for &b in w.as_bytes() {
                cur[(b - b'a') as usize] += 1;
            }
            for i in 0..26 {
                common[i] = std::cmp::min(common[i], cur[i]);
            }
        }
        // Build result list
        let mut res = Vec::new();
        for (i, &cnt) in common.iter().enumerate() {
            for _ in 0..cnt {
                res.push(((b'a' + i as u8) as char).to_string());
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (common-chars words)
  (-> (listof string?) (listof string?))
  (if (null? words)
      '()
      (let* ((first (car words))
             (common (make-vector 26 0)))
        ;; count characters in the first word
        (for ([idx (in-range (string-length first))])
          (let* ((c (string-ref first idx))
                 (pos (- (char->integer c) (char->integer #\a))))
            (vector-set! common pos (+ 1 (vector-ref common pos)))))
        ;; process remaining words
        (for ([w (in-list (cdr words))])
          (define current (make-vector 26 0))
          (for ([idx (in-range (string-length w))])
            (let* ((c (string-ref w idx))
                   (pos (- (char->integer c) (char->integer #\a))))
              (vector-set! current pos (+ 1 (vector-ref current pos)))))
          (for ([i (in-range 26)])
            (vector-set! common i
                         (min (vector-ref common i)
                              (vector-ref current i)))))
        ;; build result list
        (let loop ((i 0) (acc '()))
          (if (= i 26)
              (reverse acc)
              (let* ((cnt (vector-ref common i))
                     (ch (integer->char (+ i (char->integer #\a))))
                     (new-acc (let repeat ((n cnt) (lst acc))
                                (if (= n 0)
                                    lst
                                    (repeat (- n 1) (cons (string ch) lst))))))
                (loop (+ i 1) new-acc)))))))
```

## Erlang

```erlang
-spec common_chars(Words :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
common_chars(Words) ->
    case Words of
        [] -> [];
        [First | Rest] ->
            Common0 = count_word(First),
            Common = lists:foldl(
                fun(Word, Acc) ->
                    Curr = count_word(Word),
                    min_lists(Acc, Curr)
                end,
                Common0,
                Rest
            ),
            build_result(Common)
    end.

%% Count occurrences of each letter a-z in a word.
count_word(Word) ->
    Init = lists:duplicate(26, 0),
    binary_to_list(Word) |> lists:foldl(
        fun(Char, Acc) ->
            Idx = Char - $a + 1,
            inc_at(Idx, Acc)
        end,
        Init
    ).

%% Increment the value at position Index (1‑based) in a list.
inc_at(Index, List) ->
    {Prefix, [Val | Suffix]} = lists:split(Index - 1, List),
    Prefix ++ [Val + 1] ++ Suffix.

%% Element‑wise minimum of two count lists.
min_lists(L1, L2) ->
    lists:zipwith(fun(A, B) -> erlang:min(A, B) end, L1, L2).

%% Build the result list from final counts.
build_result(Counts) ->
    Result = build_result(Counts, 1, []),
    lists:reverse(Result).

build_result([], _Idx, Acc) ->
    Acc;
build_result([C | Rest], Idx, Acc) when C > 0 ->
    CharBin = <<($a + Idx - 1)>>,
    NewAcc = add_n(CharBin, C, Acc),
    build_result(Rest, Idx + 1, NewAcc);
build_result([_C | Rest], Idx, Acc) ->
    build_result(Rest, Idx + 1, Acc).

add_n(_Char, 0, Acc) -> Acc;
add_n(Char, N, Acc) when N > 0 ->
    add_n(Char, N - 1, [Char | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec common_chars(words :: [String.t]) :: [String.t]
  def common_chars(words) do
    [first | rest] = words

    common = freq(first)

    final_counts =
      Enum.reduce(rest, common, fn w, acc ->
        cur = freq(w)

        Enum.map(0..25, fn i ->
          min(Enum.at(acc, i), Enum.at(cur, i))
        end)
      end)

    Enum.with_index(final_counts)
    |> Enum.flat_map(fn {cnt, idx} ->
      if cnt > 0 do
        char = <<(?a + idx)::utf8>>
        List.duplicate(char, cnt)
      else
        []
      end
    end)
  end

  defp freq(word) do
    init = List.duplicate(0, 26)

    Enum.reduce(String.graphemes(word), init, fn ch, acc ->
      <<codepoint::utf8>> = ch
      idx = codepoint - ?a
      List.update_at(acc, idx, &(&1 + 1))
    end)
  end
end
```
