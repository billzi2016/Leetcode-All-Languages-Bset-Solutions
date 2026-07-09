# 0953. Verifying an Alien Dictionary

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        int rank[26];
        for (int i = 0; i < 26; ++i) rank[order[i] - 'a'] = i;
        
        for (size_t i = 0; i + 1 < words.size(); ++i) {
            const string& a = words[i];
            const string& b = words[i + 1];
            size_t len = min(a.size(), b.size());
            bool diffFound = false;
            for (size_t j = 0; j < len; ++j) {
                if (a[j] != b[j]) {
                    diffFound = true;
                    if (rank[a[j] - 'a'] > rank[b[j] - 'a'])
                        return false;
                    break;
                }
            }
            if (!diffFound && a.size() > b.size())
                return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        int[] rank = new int[26];
        for (int i = 0; i < order.length(); i++) {
            rank[order.charAt(i) - 'a'] = i;
        }
        for (int i = 0; i < words.length - 1; i++) {
            String w1 = words[i];
            String w2 = words[i + 1];
            int len = Math.min(w1.length(), w2.length());
            boolean foundDiff = false;
            for (int j = 0; j < len; j++) {
                char c1 = w1.charAt(j);
                char c2 = w2.charAt(j);
                if (c1 != c2) {
                    if (rank[c1 - 'a'] > rank[c2 - 'a']) {
                        return false;
                    }
                    foundDiff = true;
                    break;
                }
            }
            if (!foundDiff && w1.length() > w2.length()) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # map each character to its rank in the alien alphabet
        rank = [0] * 26
        for i, ch in enumerate(order):
            rank[ord(ch) - ord('a')] = i

        def in_order(w1, w2):
            """return True if w1 <= w2 according to alien order"""
            l1, l2 = len(w1), len(w2)
            for i in range(min(l1, l2)):
                c1, c2 = w1[i], w2[i]
                if c1 != c2:
                    return rank[ord(c1) - ord('a')] < rank[ord(c2) - ord('a')]
            # all shared prefix equal, shorter word should come first
            return l1 <= l2

        for i in range(len(words) - 1):
            if not in_order(words[i], words[i + 1]):
                return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {c: i for i, c in enumerate(order)}
        
        def in_order(w1: str, w2: str) -> bool:
            n = min(len(w1), len(w2))
            for i in range(n):
                if w1[i] != w2[i]:
                    return rank[w1[i]] < rank[w2[i]]
            return len(w1) <= len(w2)
        
        for i in range(len(words) - 1):
            if not in_order(words[i], words[i + 1]):
                return False
        return True
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool isAlienSorted(char** words, int wordsSize, char* order) {
    int rank[26];
    for (int i = 0; i < 26; ++i) {
        rank[order[i] - 'a'] = i;
    }
    for (int i = 0; i < wordsSize - 1; ++i) {
        char *w1 = words[i];
        char *w2 = words[i + 1];
        int j = 0;
        while (w1[j] && w2[j]) {
            if (w1[j] != w2[j]) {
                if (rank[w1[j] - 'a'] > rank[w2[j] - 'a'])
                    return false;
                break;
            }
            ++j;
        }
        if (!w1[j] && w2[j]) {
            continue; // w1 is shorter, correct order
        } else if (w1[j] && !w2[j]) {
            return false; // w2 ended first, incorrect order
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsAlienSorted(string[] words, string order)
    {
        int[] rank = new int[26];
        for (int i = 0; i < order.Length; i++)
            rank[order[i] - 'a'] = i;

        for (int i = 0; i < words.Length - 1; i++)
        {
            if (!InCorrectOrder(words[i], words[i + 1], rank))
                return false;
        }
        return true;
    }

    private bool InCorrectOrder(string w1, string w2, int[] rank)
    {
        int len = Math.Min(w1.Length, w2.Length);
        for (int i = 0; i < len; i++)
        {
            if (w1[i] != w2[i])
                return rank[w1[i] - 'a'] < rank[w2[i] - 'a'];
        }
        // All characters are the same up to the length of the shorter word
        return w1.Length <= w2.Length;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
var isAlienSorted = function(words, order) {
    const rank = new Array(26);
    for (let i = 0; i < 26; ++i) {
        rank[order.charCodeAt(i) - 97] = i;
    }
    
    const compare = (a, b) => {
        const len = Math.min(a.length, b.length);
        for (let i = 0; i < len; ++i) {
            const ra = rank[a.charCodeAt(i) - 97];
            const rb = rank[b.charCodeAt(i) - 97];
            if (ra !== rb) return ra < rb;
        }
        return a.length <= b.length;
    };
    
    for (let i = 0; i < words.length - 1; ++i) {
        if (!compare(words[i], words[i + 1])) return false;
    }
    return true;
};
```

## Typescript

```typescript
function isAlienSorted(words: string[], order: string): boolean {
    const rank = new Array(26);
    for (let i = 0; i < 26; ++i) {
        rank[order.charCodeAt(i) - 97] = i;
    }

    for (let i = 0; i < words.length - 1; ++i) {
        const w1 = words[i];
        const w2 = words[i + 1];
        const minLen = Math.min(w1.length, w2.length);
        let j = 0;
        while (j < minLen && w1.charCodeAt(j) === w2.charCodeAt(j)) {
            ++j;
        }
        if (j === minLen) {
            // all compared chars are equal; shorter word should come first
            if (w1.length > w2.length) return false;
        } else {
            const c1 = w1.charCodeAt(j) - 97;
            const c2 = w2.charCodeAt(j) - 97;
            if (rank[c1] > rank[c2]) return false;
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $order
     * @return Boolean
     */
    function isAlienSorted($words, $order) {
        // Build rank map for each character in the alien alphabet
        $rank = [];
        $lenOrder = strlen($order);
        for ($i = 0; $i < $lenOrder; $i++) {
            $rank[$order[$i]] = $i;
        }

        $n = count($words);
        for ($i = 0; $i < $n - 1; $i++) {
            $w1 = $words[$i];
            $w2 = $words[$i + 1];
            $len1 = strlen($w1);
            $len2 = strlen($w2);
            $j = 0;

            // Find first differing character
            while ($j < $len1 && $j < $len2 && $w1[$j] === $w2[$j]) {
                $j++;
            }

            if ($j == $len1 || $j == $len2) {
                // One word is a prefix of the other
                if ($len1 > $len2 && $j == $len2) {
                    return false; // w2 is shorter and should come first
                }
                // otherwise correct order, continue to next pair
            } else {
                // Compare ranks of differing characters
                if ($rank[$w1[$j]] > $rank[$w2[$j]]) {
                    return false;
                }
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isAlienSorted(_ words: [String], _ order: String) -> Bool {
        var rank = [Int](repeating: 0, count: 26)
        for (i, ch) in order.enumerated() {
            let idx = Int(ch.unicodeScalars.first!.value - 97)
            rank[idx] = i
        }
        for i in 0..<(words.count - 1) {
            if !inOrder(words[i], words[i + 1], rank) {
                return false
            }
        }
        return true
    }

    private func inOrder(_ w1: String, _ w2: String, _ rank: [Int]) -> Bool {
        let a = Array(w1.utf8)
        let b = Array(w2.utf8)
        let minLen = min(a.count, b.count)
        for i in 0..<minLen {
            if a[i] != b[i] {
                return rank[Int(a[i] - 97)] < rank[Int(b[i] - 97)]
            }
        }
        return a.count <= b.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isAlienSorted(words: Array<String>, order: String): Boolean {
        val rank = IntArray(26)
        for ((i, ch) in order.withIndex()) {
            rank[ch - 'a'] = i
        }
        for (i in 0 until words.size - 1) {
            val w1 = words[i]
            val w2 = words[i + 1]
            var j = 0
            val minLen = kotlin.math.min(w1.length, w2.length)
            while (j < minLen && w1[j] == w2[j]) {
                j++
            }
            if (j == minLen) {
                // all characters are the same up to the length of the shorter word
                if (w1.length > w2.length) return false
            } else {
                val c1 = w1[j]
                val c2 = w2[j]
                if (rank[c1 - 'a'] > rank[c2 - 'a']) return false
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isAlienSorted(List<String> words, String order) {
    List<int> rank = List.filled(26, 0);
    for (int i = 0; i < 26; ++i) {
      rank[order.codeUnitAt(i) - 97] = i;
    }
    for (int i = 0; i < words.length - 1; ++i) {
      if (!_inOrder(words[i], words[i + 1], rank)) return false;
    }
    return true;
  }

  bool _inOrder(String w1, String w2, List<int> rank) {
    int len = w1.length < w2.length ? w1.length : w2.length;
    for (int i = 0; i < len; ++i) {
      int c1 = rank[w1.codeUnitAt(i) - 97];
      int c2 = rank[w2.codeUnitAt(i) - 97];
      if (c1 < c2) return true;
      if (c1 > c2) return false;
    }
    return w1.length <= w2.length;
  }
}
```

## Golang

```go
func isAlienSorted(words []string, order string) bool {
	rank := [26]int{}
	for i, ch := range order {
		rank[ch-'a'] = i
	}
	for i := 0; i < len(words)-1; i++ {
		w1, w2 := words[i], words[i+1]
		minLen := len(w1)
		if len(w2) < minLen {
			minLen = len(w2)
		}
		j := 0
		for ; j < minLen; j++ {
			c1 := rank[w1[j]-'a']
			c2 := rank[w2[j]-'a']
			if c1 < c2 {
				break
			}
			if c1 > c2 {
				return false
			}
		}
		if j == minLen && len(w1) > len(w2) {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def is_alien_sorted(words, order)
  rank = Array.new(26)
  order.each_char.with_index { |c, i| rank[c.ord - 97] = i }

  (0...words.size - 1).each do |i|
    w1 = words[i]
    w2 = words[i + 1]
    min_len = [w1.length, w2.length].min
    j = 0

    while j < min_len
      r1 = rank[w1.getbyte(j) - 97]
      r2 = rank[w2.getbyte(j) - 97]
      if r1 < r2
        break
      elsif r1 > r2
        return false
      end
      j += 1
    end

    return false if j == min_len && w1.length > w2.length
  end

  true
end
```

## Scala

```scala
object Solution {
  def isAlienSorted(words: Array[String], order: String): Boolean = {
    val rank = new Array[Int](26)
    var idx = 0
    while (idx < 26) {
      rank(order.charAt(idx) - 'a') = idx
      idx += 1
    }

    var i = 0
    while (i < words.length - 1) {
      val w1 = words(i)
      val w2 = words(i + 1)
      val minLen = math.min(w1.length, w2.length)

      var j = 0
      while (j < minLen && rank(w1.charAt(j) - 'a') == rank(w2.charAt(j) - 'a')) {
        j += 1
      }

      if (j == minLen) {
        // all compared characters are equal, shorter word should come first
        if (w1.length > w2.length) return false
      } else {
        if (rank(w1.charAt(j) - 'a') > rank(w2.charAt(j) - 'a')) return false
      }

      i += 1
    }
    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn is_alien_sorted(words: Vec<String>, order: String) -> bool {
        let mut rank = [0usize; 26];
        for (i, b) in order.bytes().enumerate() {
            rank[(b - b'a') as usize] = i;
        }

        for i in 0..words.len().saturating_sub(1) {
            let w1 = words[i].as_bytes();
            let w2 = words[i + 1].as_bytes();

            let mut j = 0;
            while j < w1.len() && j < w2.len()
                && rank[(w1[j] - b'a') as usize] == rank[(w2[j] - b'a') as usize]
            {
                j += 1;
            }

            if j == w2.len() && j < w1.len() {
                return false; // second word is a prefix of the first
            }
            if j < w1.len() && j < w2.len()
                && rank[(w1[j] - b'a') as usize] > rank[(w2[j] - b'a') as usize]
            {
                return false;
            }
        }

        true
    }
}
```

## Racket

```racket
(define/contract (is-alien-sorted words order)
  (-> (listof string?) string? boolean?)
  (let* ([rank (make-vector 26)]
         [order-chars (string->list order)])
    (for ([c order-chars] [i (in-naturals)])
      (vector-set! rank (- (char->integer c) (char->integer #\a)) i))
    (define (char-rank ch)
      (vector-ref rank (- (char->integer ch) (char->integer #\a))))
    (define (word-le? w1 w2)
      (let loop ([i 0])
        (cond
          [(= i (string-length w1)) #t]               ; w1 exhausted first or equal length
          [(= i (string-length w2)) #f]               ; w2 exhausted first -> w1 longer
          [else
           (let* ([c1 (string-ref w1 i)]
                  [c2 (string-ref w2 i)]
                  [r1 (char-rank c1)]
                  [r2 (char-rank c2)])
             (cond
               [(< r1 r2) #t]
               [(> r1 r2) #f]
               [else (loop (+ i 1))]))])))
    (let loop-words ([prev (car words)] [rest (cdr words)])
      (if (null? rest)
          #t
          (let ([curr (car rest)])
            (if (word-le? prev curr)
                (loop-words curr (cdr rest))
                #f))))))
```

## Erlang

```erlang
-spec is_alien_sorted(Words :: [unicode:unicode_binary()], Order :: unicode:unicode_binary()) -> boolean().
is_alien_sorted(Words, Order) ->
    RankMap = build_rank_map(Order),
    check_sorted(Words, RankMap).

build_rank_map(Order) ->
    Chars = binary_to_list(Order),
    lists:foldl(
        fun({Char, Idx}, Acc) -> maps:put(Char, Idx, Acc) end,
        #{},
        lists:zip(Chars, lists:seq(0, 25))
    ).

check_sorted([_], _RankMap) ->
    true;
check_sorted([W1, W2 | Rest], RankMap) ->
    case compare_words(W1, W2, RankMap) of
        true -> check_sorted([W2 | Rest], RankMap);
        false -> false
    end.

compare_words(Bin1, Bin2, RankMap) ->
    case {Bin1, Bin2} of
        {<<>>, <<>>} -> true;
        {<<>>, _} -> true;          % first word shorter
        {_, <<>>} -> false;         % second word ended first
        _ ->
            <<C1:8, Rest1/binary>> = Bin1,
            <<C2:8, Rest2/binary>> = Bin2,
            if C1 =:= C2 ->
                    compare_words(Rest1, Rest2, RankMap);
               true ->
                    Rank1 = maps:get(C1, RankMap),
                    Rank2 = maps:get(C2, RankMap),
                    Rank1 =< Rank2
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_alien_sorted(words :: [String.t()], order :: String.t()) :: boolean()
  def is_alien_sorted(words, order) do
    rank =
      order
      |> String.graphemes()
      |> Enum.with_index()
      |> Map.new(fn {ch, idx} -> {ch, idx} end)

    words
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.all?(fn [w1, w2] -> compare(w1, w2, rank) end)
  end

  defp compare(w1, w2, rank) do
    list1 = String.graphemes(w1)
    list2 = String.graphemes(w2)
    compare_lists(list1, list2, rank)
  end

  defp compare_lists([], [], _), do: true
  defp compare_lists([], _, _), do: true
  defp compare_lists(_, [], _), do: false

  defp compare_lists([h1 | t1], [h2 | t2], rank) do
    r1 = Map.get(rank, h1)
    r2 = Map.get(rank, h2)

    cond do
      r1 < r2 -> true
      r1 > r2 -> false
      true -> compare_lists(t1, t2, rank)
    end
  end
end
```
