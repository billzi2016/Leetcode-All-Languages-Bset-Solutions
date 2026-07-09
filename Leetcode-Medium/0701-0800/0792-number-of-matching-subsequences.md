# 0792. Number of Matching Subsequences

## Cpp

```cpp
class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        const int ALPH = 26;
        vector<vector<pair<int,int>>> buckets(ALPH);
        for (int i = 0; i < (int)words.size(); ++i) {
            if (!words[i].empty()) {
                int c = words[i][0] - 'a';
                buckets[c].push_back({i, 0});
            }
        }
        int ans = 0;
        for (char ch : s) {
            int idx = ch - 'a';
            vector<pair<int,int>> cur;
            cur.swap(buckets[idx]); // take current waiting list
            for (auto &p : cur) {
                int wIdx = p.first;
                int pos = p.second + 1; // advance one character
                if (pos == (int)words[wIdx].size()) {
                    ++ans;
                } else {
                    int nextChar = words[wIdx][pos] - 'a';
                    buckets[nextChar].push_back({wIdx, pos});
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.ArrayDeque;

class Solution {
    private static class Node {
        String word;
        int pos;
        Node(String w, int p) { this.word = w; this.pos = p; }
    }

    public int numMatchingSubseq(String s, String[] words) {
        @SuppressWarnings("unchecked")
        ArrayDeque<Node>[] buckets = new ArrayDeque[26];
        for (int i = 0; i < 26; i++) {
            buckets[i] = new ArrayDeque<>();
        }
        for (String w : words) {
            buckets[w.charAt(0) - 'a'].add(new Node(w, 0));
        }

        int count = 0;
        for (char ch : s.toCharArray()) {
            int idx = ch - 'a';
            ArrayDeque<Node> current = buckets[idx];
            if (current.isEmpty()) continue;
            buckets[idx] = new ArrayDeque<>();
            while (!current.isEmpty()) {
                Node node = current.poll();
                node.pos++;
                if (node.pos == node.word.length()) {
                    count++;
                } else {
                    char nextChar = node.word.charAt(node.pos);
                    buckets[nextChar - 'a'].add(node);
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
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        from collections import defaultdict

        buckets = defaultdict(list)
        for w in words:
            it = iter(w)
            first = next(it, None)
            if first is not None:
                buckets[first].append(it)

        count = 0
        for ch in s:
            old_bucket = buckets[ch]
            buckets[ch] = []
            for it in old_bucket:
                nxt = next(it, None)
                if nxt is None:
                    count += 1
                else:
                    buckets[nxt].append(it)
        return count
```

## Python3

```python
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = {chr(ord('a') + i): [] for i in range(26)}
        for w in words:
            it = iter(w)
            first_char = next(it)
            buckets[first_char].append(it)

        matched = 0
        for ch in s:
            current = buckets[ch]
            buckets[ch] = []
            for it in current:
                nxt = next(it, None)
                if nxt is None:
                    matched += 1
                else:
                    buckets[nxt].append(it)
        return matched
```

## C

```c
#include <stdlib.h>

typedef struct Node {
    int idx;
    int pos;
    struct Node* next;
} Node;

int numMatchingSubseq(char* s, char** words, int wordsSize) {
    if (wordsSize == 0) return 0;

    Node* nodes = (Node*)malloc(sizeof(Node) * wordsSize);
    Node* buckets[26] = {NULL};

    for (int i = 0; i < wordsSize; ++i) {
        nodes[i].idx = i;
        nodes[i].pos = 0;
        char first = words[i][0];
        int b = first - 'a';
        nodes[i].next = buckets[b];
        buckets[b] = &nodes[i];
    }

    int count = 0;
    for (char* p = s; *p != '\0'; ++p) {
        int b = *p - 'a';
        Node* cur = buckets[b];
        buckets[b] = NULL;

        while (cur) {
            Node* nxt = cur->next;
            int idx = cur->idx;
            int newPos = cur->pos + 1;
            if (words[idx][newPos] == '\0') {
                ++count;
            } else {
                char nextChar = words[idx][newPos];
                int nb = nextChar - 'a';
                cur->pos = newPos;
                cur->next = buckets[nb];
                buckets[nb] = cur;
            }
            cur = nxt;
        }
    }

    free(nodes);
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    private class Node
    {
        public string Word;
        public int Pos;
        public Node(string word, int pos)
        {
            Word = word;
            Pos = pos;
        }
    }

    public int NumMatchingSubseq(string s, string[] words)
    {
        var buckets = new Queue<Node>[26];
        for (int i = 0; i < 26; i++) buckets[i] = new Queue<Node>();

        foreach (var w in words)
        {
            // each word has length >=1 per constraints
            int idx = w[0] - 'a';
            buckets[idx].Enqueue(new Node(w, 0));
        }

        int matched = 0;
        foreach (char c in s)
        {
            int idx = c - 'a';
            var q = buckets[idx];
            int size = q.Count;
            for (int i = 0; i < size; i++)
            {
                var node = q.Dequeue();
                node.Pos++;
                if (node.Pos == node.Word.Length)
                {
                    matched++;
                }
                else
                {
                    int nextIdx = node.Word[node.Pos] - 'a';
                    buckets[nextIdx].Enqueue(node);
                }
            }
        }

        return matched;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string[]} words
 * @return {number}
 */
var numMatchingSubseq = function(s, words) {
    const buckets = Array.from({ length: 26 }, () => []);
    for (const w of words) {
        const idx = w.charCodeAt(0) - 97;
        buckets[idx].push({ word: w, pos: 0 });
    }
    let count = 0;
    for (const ch of s) {
        const idx = ch.charCodeAt(0) - 97;
        const curBucket = buckets[idx];
        buckets[idx] = [];
        for (const node of curBucket) {
            node.pos++;
            if (node.pos === node.word.length) {
                count++;
            } else {
                const nextIdx = node.word.charCodeAt(node.pos) - 97;
                buckets[nextIdx].push(node);
            }
        }
    }
    return count;
};
```

## Typescript

```typescript
function numMatchingSubseq(s: string, words: string[]): number {
    const buckets: Array<Array<[string, number]>> = Array.from({ length: 26 }, () => []);
    
    for (const w of words) {
        if (w.length === 0) continue;
        const idx = w.charCodeAt(0) - 97;
        buckets[idx].push([w, 0]);
    }
    
    let count = 0;
    for (const ch of s) {
        const idx = ch.charCodeAt(0) - 97;
        const current = buckets[idx];
        if (current.length === 0) continue;
        buckets[idx] = [];
        for (const [word, pos] of current) {
            const nextPos = pos + 1;
            if (nextPos === word.length) {
                count++;
            } else {
                const nextIdx = word.charCodeAt(nextPos) - 97;
                buckets[nextIdx].push([word, nextPos]);
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
     * @param String $s
     * @param String[] $words
     * @return Integer
     */
    function numMatchingSubseq($s, $words) {
        $buckets = array_fill(0, 26, []);
        foreach ($words as $idx => $w) {
            $first = ord($w[0]) - 97;
            $buckets[$first][] = [$idx, 0];
        }
        $count = 0;
        $lenS = strlen($s);
        for ($i = 0; $i < $lenS; $i++) {
            $cIdx = ord($s[$i]) - 97;
            $current = $buckets[$cIdx];
            if (empty($current)) continue;
            $buckets[$cIdx] = [];
            foreach ($current as $pair) {
                [$idx, $pos] = $pair;
                $pos++;
                if ($pos == strlen($words[$idx])) {
                    $count++;
                } else {
                    $nextCharIdx = ord($words[$idx][$pos]) - 97;
                    $buckets[$nextCharIdx][] = [$idx, $pos];
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
    func numMatchingSubseq(_ s: String, _ words: [String]) -> Int {
        var buckets = Array(repeating: [(Int, Int)](), count: 26)
        var wordChars = [[Character]]()
        wordChars.reserveCapacity(words.count)
        for (i, w) in words.enumerated() {
            let chars = Array(w)
            wordChars.append(chars)
            if let first = chars.first {
                let idx = Int(first.unicodeScalars.first!.value - 97)
                buckets[idx].append((i, 0))
            }
        }
        var result = 0
        for ch in s {
            let idx = Int(ch.unicodeScalars.first!.value - 97)
            var current = buckets[idx]
            buckets[idx] = []
            for (wordIdx, pos) in current {
                let nextPos = pos + 1
                if nextPos == wordChars[wordIdx].count {
                    result += 1
                } else {
                    let nextChar = wordChars[wordIdx][nextPos]
                    let nextIdx = Int(nextChar.unicodeScalars.first!.value - 97)
                    buckets[nextIdx].append((wordIdx, nextPos))
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
    fun numMatchingSubseq(s: String, words: Array<String>): Int {
        val buckets = Array(26) { mutableListOf<Node>() }
        for (w in words) {
            if (w.isNotEmpty()) {
                buckets[w[0] - 'a'].add(Node(w, 0))
            }
        }
        var count = 0
        for (ch in s) {
            val idx = ch - 'a'
            val current = buckets[idx]
            if (current.isEmpty()) continue
            val processing = ArrayList(current)
            current.clear()
            for (node in processing) {
                node.pos++
                if (node.pos == node.word.length) {
                    count++
                } else {
                    buckets[node.word[node.pos] - 'a'].add(node)
                }
            }
        }
        return count
    }

    private data class Node(val word: String, var pos: Int)
}
```

## Dart

```dart
class _Node {
  String word;
  int pos;
  _Node(this.word, this.pos);
}

class Solution {
  int numMatchingSubseq(String s, List<String> words) {
    int count = 0;
    List<List<_Node>> buckets = List.generate(26, (_) => <_Node>[]);

    for (String w in words) {
      if (w.length > s.length) continue;
      int idx = w.codeUnitAt(0) - 97;
      buckets[idx].add(_Node(w, 0));
    }

    for (int i = 0; i < s.length; i++) {
      int idx = s.codeUnitAt(i) - 97;
      List<_Node> current = buckets[idx];
      if (current.isEmpty) continue;
      buckets[idx] = <_Node>[];
      for (_Node node in current) {
        node.pos++;
        if (node.pos == node.word.length) {
          count++;
        } else {
          int nextIdx = node.word.codeUnitAt(node.pos) - 97;
          buckets[nextIdx].add(node);
        }
      }
    }

    return count;
  }
}
```

## Golang

```go
func numMatchingSubseq(s string, words []string) int {
	type node struct {
		word string
		pos  int
	}
	buckets := make([][]node, 26)
	for _, w := range words {
		if len(w) == 0 {
			continue
		}
		idx := w[0] - 'a'
		buckets[idx] = append(buckets[idx], node{word: w, pos: 0})
	}
	count := 0
	for i := 0; i < len(s); i++ {
		cIdx := s[i] - 'a'
		cur := buckets[cIdx]
		if len(cur) == 0 {
			continue
		}
		buckets[cIdx] = nil
		for _, nd := range cur {
			nd.pos++
			if nd.pos == len(nd.word) {
				count++
			} else {
				nextIdx := nd.word[nd.pos] - 'a'
				buckets[nextIdx] = append(buckets[nextIdx], nd)
			}
		}
	}
	return count
}
```

## Ruby

```ruby
def num_matching_subseq(s, words)
  buckets = Array.new(26) { [] }
  words.each do |w|
    buckets[w.getbyte(0) - 97] << [w, 0]
  end

  count = 0
  s.each_byte do |b|
    idx = b - 97
    current = buckets[idx]
    next if current.empty?
    buckets[idx] = []
    current.each do |word, pos|
      pos += 1
      if pos == word.length
        count += 1
      else
        buckets[word.getbyte(pos) - 97] << [word, pos]
      end
    end
  end

  count
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable

  def numMatchingSubseq(s: String, words: Array[String]): Int = {
    val buckets = Array.fill(26)(mutable.Queue[(String, Int)]())
    for (w <- words) {
      if (w.nonEmpty) {
        val idx = w.charAt(0) - 'a'
        buckets(idx).enqueue((w, 0))
      }
    }

    var count = 0
    for (ch <- s) {
      val idx = ch - 'a'
      val q = buckets(idx)
      val size = q.size
      for (_ <- 0 until size) {
        val (word, pos) = q.dequeue()
        val newPos = pos + 1
        if (newPos == word.length) {
          count += 1
        } else {
          val nextIdx = word.charAt(newPos) - 'a'
          buckets(nextIdx).enqueue((word, newPos))
        }
      }
    }
    count
  }
}
```

## Rust

```rust
impl Solution {
    pub fn num_matching_subseq(s: String, words: Vec<String>) -> i32 {
        use std::mem;
        let s_bytes = s.as_bytes();
        // Convert all words to byte vectors for fast indexing
        let word_vecs: Vec<Vec<u8>> = words.iter().map(|w| w.as_bytes().to_vec()).collect();

        // Buckets for each character 'a'..'z'
        let mut buckets: Vec<Vec<(usize, usize)>> = vec![Vec::new(); 26];

        // Initialize buckets with the first needed character of each word
        for (i, w) in word_vecs.iter().enumerate() {
            if !w.is_empty() {
                let idx = (w[0] - b'a') as usize;
                buckets[idx].push((i, 0));
            }
        }

        let mut count: i32 = 0;

        for &c in s_bytes {
            let idx = (c - b'a') as usize;
            // Take the current list of waiting words for this character
            let mut cur_list = Vec::new();
            mem::swap(&mut cur_list, &mut buckets[idx]);

            for (word_idx, pos) in cur_list {
                let next_pos = pos + 1;
                if next_pos == word_vecs[word_idx].len() {
                    count += 1; // whole word matched
                } else {
                    let next_char = word_vecs[word_idx][next_pos];
                    let next_idx = (next_char - b'a') as usize;
                    buckets[next_idx].push((word_idx, next_pos));
                }
            }
        }

        count
    }
}
```

## Racket

```racket
(define-struct waiting (word idx) #:transparent)

(define/contract (num-matching-subseq s words)
  (-> string? (listof string?) exact-integer?)
  (let* ((buckets (make-vector 26 '()))
         (add-to-bucket
          (lambda (c w i)
            (let* ((ci (- (char->integer c) (char->integer #\a)))
                   (lst (vector-ref buckets ci)))
              (vector-set! buckets ci (cons (waiting w i) lst)))))
         (count 0))
    ;; initialize buckets with first needed character of each word
    (for ([w words])
      (when (> (string-length w) 0)
        (add-to-bucket (string-ref w 0) w 1)))
    ;; process the main string
    (for ([ch (in-string s)])
      (let* ((ci (- (char->integer ch) (char->integer #\a)))
             (current (vector-ref buckets ci)))
        (when current
          (vector-set! buckets ci '()))
        (let loop ((lst current))
          (cond [(null? lst) (void)]
                [else
                 (define w (waiting-word (car lst)))
                 (define i (waiting-idx (car lst)))
                 (if (= i (string-length w))
                     (set! count (+ count 1))
                     (let ((nextc (string-ref w i)))
                       (add-to-bucket nextc w (+ i 1))))
                 (loop (cdr lst))]))))
    count))
```

## Erlang

```erlang
-module(solution).
-export([num_matching_subseq/2]).

-spec num_matching_subseq(S :: unicode:unicode_binary(), Words :: [unicode:unicode_binary()]) -> integer().
num_matching_subseq(S, Words) ->
    Buckets0 = init_buckets(Words),
    process_string(S, Buckets0, 0).

%% Initialize buckets with the first needed character of each word.
init_buckets(Words) ->
    EmptyBuckets = erlang:make_tuple(26, []),
    lists:foldl(fun add_word/2, EmptyBuckets, Words).

add_word(Word, Buckets) ->
    <<First:8, Rest/binary>> = Word,
    Idx = First - $a + 1,
    Existing = element(Idx, Buckets),
    Updated = [Rest | Existing],
    setelement(Idx, Buckets, Updated).

%% Process each character of S.
process_string(<<>>, Buckets, Count) ->
    Count;
process_string(<<C:8, Rest/binary>>, Buckets, Count) ->
    Idx = C - $a + 1,
    CurrentList = element(Idx, Buckets),
    BucketsCleared = setelement(Idx, Buckets, []),
    {BucketsNext, NewCount} = process_bucket(CurrentList, BucketsCleared, Count),
    process_string(Rest, BucketsNext, NewCount).

%% Process all words waiting for the current character.
process_bucket([], Buckets, Count) ->
    {Buckets, Count};
process_bucket([Rem | Tail], Buckets, Count) ->
    case Rem of
        <<>> ->
            process_bucket(Tail, Buckets, Count + 1);
        <<Next:8, Rest/binary>> ->
            NextIdx = Next - $a + 1,
            Existing = element(NextIdx, Buckets),
            Updated = [Rest | Existing],
            BucketsUpdated = setelement(NextIdx, Buckets, Updated),
            process_bucket(Tail, BucketsUpdated, Count)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_matching_subseq(s :: String.t(), words :: [String.t()]) :: integer()
  def num_matching_subseq(s, words) do
    # Build initial buckets: map from character code to list of {word_binary, current_index}
    init_buckets =
      Enum.reduce(words, %{}, fn word, acc ->
        first_char = :binary.at(word, 0)

        Map.update(acc, first_char, [{word, 0}], fn list -> [{word, 0} | list] end)
      end)

    {count, _} =
      String.to_charlist(s)
      |> Enum.reduce({0, init_buckets}, fn char_code, {cnt, buckets} ->
        waiting = Map.get(buckets, char_code, [])
        # clear current bucket
        buckets = Map.put(buckets, char_code, [])

        {new_cnt, new_buckets} =
          Enum.reduce(waiting, {cnt, buckets}, fn {word, idx}, {c_acc, b_acc} ->
            next_idx = idx + 1

            if next_idx == byte_size(word) do
              {c_acc + 1, b_acc}
            else
              next_char = :binary.at(word, next_idx)

              updated_buckets =
                Map.update(b_acc, next_char, [{word, next_idx}], fn list ->
                  [{word, next_idx} | list]
                end)

              {c_acc, updated_buckets}
            end
          end)

        {new_cnt, new_buckets}
      end)

    count
  end
end
```
