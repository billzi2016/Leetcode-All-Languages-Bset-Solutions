# 0127. Word Ladder

## Cpp

```cpp
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(), wordList.end());
        if (!dict.count(endWord)) return 0;
        // Remove beginWord from dict if present to avoid revisiting
        dict.erase(beginWord);
        
        unordered_set<string> beginSet{beginWord}, endSet{endWord};
        int len = 1;
        
        while (!beginSet.empty() && !endSet.empty()) {
            // Always expand the smaller frontier
            if (beginSet.size() > endSet.size())
                swap(beginSet, endSet);
            
            unordered_set<string> nextLevel;
            for (const string& word : beginSet) {
                string cur = word;
                for (int i = 0; i < (int)cur.size(); ++i) {
                    char original = cur[i];
                    for (char c = 'a'; c <= 'z'; ++c) {
                        if (c == original) continue;
                        cur[i] = c;
                        if (endSet.count(cur)) return len + 1;
                        if (dict.count(cur)) {
                            nextLevel.insert(cur);
                            dict.erase(cur); // visited
                        }
                    }
                    cur[i] = original;
                }
            }
            beginSet.swap(nextLevel);
            ++len;
        }
        return 0;
    }
};
```

## Java

```java
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<>(wordList);
        if (!wordSet.contains(endWord)) return 0;

        Set<String> beginSet = new HashSet<>();
        Set<String> endSet = new HashSet<>();
        Set<String> visited = new HashSet<>();

        beginSet.add(beginWord);
        endSet.add(endWord);
        int len = 1;
        int wordLen = beginWord.length();

        while (!beginSet.isEmpty() && !endSet.isEmpty()) {
            // always expand the smaller set
            if (beginSet.size() > endSet.size()) {
                Set<String> tmp = beginSet;
                beginSet = endSet;
                endSet = tmp;
            }

            Set<String> nextLevel = new HashSet<>();
            for (String word : beginSet) {
                char[] chars = word.toCharArray();
                for (int i = 0; i < wordLen; i++) {
                    char original = chars[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == original) continue;
                        chars[i] = c;
                        String newWord = new String(chars);
                        if (endSet.contains(newWord)) {
                            return len + 1;
                        }
                        if (!visited.contains(newWord) && wordSet.contains(newWord)) {
                            visited.add(newWord);
                            nextLevel.add(newWord);
                        }
                    }
                    chars[i] = original;
                }
            }

            beginSet = nextLevel;
            len++;
        }

        return 0;
    }
}
```

## Python

```python
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        begin_set = {beginWord}
        end_set = {endWord}
        visited = set([beginWord])
        step = 1
        L = len(beginWord)

        while begin_set and end_set:
            # always expand the smaller frontier
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            next_level = set()
            for word in begin_set:
                word_chars = list(word)
                for i in range(L):
                    original_char = word_chars[i]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == original_char:
                            continue
                        word_chars[i] = c
                        new_word = ''.join(word_chars)
                        if new_word in end_set:
                            return step + 1
                        if new_word in wordSet and new_word not in visited:
                            next_level.add(new_word)
                            visited.add(new_word)
                    word_chars[i] = original_char
            begin_set = next_level
            step += 1

        return 0
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        # Bidirectional BFS initialization
        begin_set = {beginWord}
        end_set = {endWord}
        visited = set()
        step = 1
        L = len(beginWord)

        while begin_set and end_set:
            # Always expand the smaller frontier
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            next_level = set()
            for word in begin_set:
                word_chars = list(word)
                for i in range(L):
                    original_char = word_chars[i]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == original_char:
                            continue
                        word_chars[i] = c
                        new_word = ''.join(word_chars)
                        if new_word in end_set:
                            return step + 1
                        if new_word in word_set and new_word not in visited:
                            visited.add(new_word)
                            next_level.add(new_word)
                    word_chars[i] = original_char
            begin_set = next_level
            step += 1

        return 0
```

## C

```c
#include <string.h>

static int isOneDiff(const char *a, const char *b) {
    int diff = 0;
    while (*a && *b) {
        if (*a != *b) {
            if (++diff > 1) return 0;
        }
        ++a;
        ++b;
    }
    return diff == 1;
}

int ladderLength(char* beginWord, char* endWord, char** wordList, int wordListSize) {
    // Check that endWord exists in the list
    int endIdx = -1;
    for (int i = 0; i < wordListSize; ++i) {
        if (strcmp(wordList[i], endWord) == 0) {
            endIdx = i;
            break;
        }
    }
    if (endIdx == -1) return 0;

    int visited[5005] = {0};
    int q[5005];
    int lvl[5005];
    int front = 0, rear = 0;

    // Initialize queue with words one step away from beginWord
    for (int i = 0; i < wordListSize; ++i) {
        if (isOneDiff(beginWord, wordList[i])) {
            visited[i] = 1;
            q[rear] = i;
            lvl[rear] = 2; // beginWord counts as level 1
            ++rear;
        }
    }

    while (front < rear) {
        int idx = q[front];
        int curLvl = lvl[front];
        ++front;

        if (strcmp(wordList[idx], endWord) == 0) return curLvl;

        for (int j = 0; j < wordListSize; ++j) {
            if (!visited[j] && isOneDiff(wordList[idx], wordList[j])) {
                visited[j] = 1;
                q[rear] = j;
                lvl[rear] = curLvl + 1;
                ++rear;
            }
        }
    }

    return 0;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int LadderLength(string beginWord, string endWord, IList<string> wordList) {
        var dict = new HashSet<string>(wordList);
        if (!dict.Contains(endWord)) return 0;

        var beginSet = new HashSet<string> { beginWord };
        var endSet = new HashSet<string> { endWord };
        int length = 1;

        while (beginSet.Count > 0 && endSet.Count > 0) {
            // Always expand the smaller frontier
            if (beginSet.Count > endSet.Count) {
                var temp = beginSet;
                beginSet = endSet;
                endSet = temp;
            }

            var nextLevel = new HashSet<string>();
            foreach (var word in beginSet) {
                char[] chars = word.ToCharArray();
                for (int i = 0; i < chars.Length; i++) {
                    char original = chars[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == original) continue;
                        chars[i] = c;
                        string newWord = new string(chars);

                        if (endSet.Contains(newWord)) {
                            return length + 1;
                        }

                        if (dict.Contains(newWord)) {
                            nextLevel.Add(newWord);
                            dict.Remove(newWord);
                        }
                    }
                    chars[i] = original;
                }
            }

            beginSet = nextLevel;
            length++;
        }

        return 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    const wordSet = new Set(wordList);
    if (!wordSet.has(endWord)) return 0;

    let beginSet = new Set([beginWord]);
    let endSet = new Set([endWord]);
    let visited = new Set();
    let step = 1;
    const L = beginWord.length;

    while (beginSet.size && endSet.size) {
        // always expand the smaller set
        if (beginSet.size > endSet.size) {
            [beginSet, endSet] = [endSet, beginSet];
        }

        const nextLevel = new Set();

        for (let word of beginSet) {
            const arr = word.split('');
            for (let i = 0; i < L; i++) {
                const originalChar = arr[i];
                for (let c = 97; c <= 122; c++) { // 'a' to 'z'
                    const ch = String.fromCharCode(c);
                    if (ch === originalChar) continue;
                    arr[i] = ch;
                    const newWord = arr.join('');
                    if (endSet.has(newWord)) {
                        return step + 1;
                    }
                    if (wordSet.has(newWord) && !visited.has(newWord)) {
                        visited.add(newWord);
                        nextLevel.add(newWord);
                    }
                }
                arr[i] = originalChar; // restore
            }
        }

        beginSet = nextLevel;
        step++;
    }

    return 0;
};
```

## Typescript

```typescript
function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {
    const wordSet = new Set<string>(wordList);
    if (!wordSet.has(endWord)) return 0;

    const visited = new Set<string>();
    let queue: string[] = [beginWord];
    visited.add(beginWord);
    let level = 1;
    const L = beginWord.length;

    while (queue.length > 0) {
        const nextQueue: string[] = [];
        for (const word of queue) {
            if (word === endWord) return level;

            const chars = word.split('');
            for (let i = 0; i < L; i++) {
                const originalChar = chars[i];
                for (let c = 97; c <= 122; c++) { // 'a' to 'z'
                    const ch = String.fromCharCode(c);
                    if (ch === originalChar) continue;
                    chars[i] = ch;
                    const newWord = chars.join('');
                    if (wordSet.has(newWord) && !visited.has(newWord)) {
                        visited.add(newWord);
                        nextQueue.push(newWord);
                    }
                }
                chars[i] = originalChar;
            }
        }
        queue = nextQueue;
        level++;
    }

    return 0;
}
```

## Php

```php
class Solution {

    /**
     * @param String $beginWord
     * @param String $endWord
     * @param String[] $wordList
     * @return Integer
     */
    function ladderLength($beginWord, $endWord, $wordList) {
        $wordSet = array_flip($wordList);
        if (!isset($wordSet[$endWord])) {
            return 0;
        }

        $beginSet = [$beginWord => true];
        $endSet   = [$endWord   => true];

        // optional: remove beginWord from set to avoid revisiting
        unset($wordSet[$beginWord]);

        $len = 1;
        $L   = strlen($beginWord);

        while (!empty($beginSet) && !empty($endSet)) {
            // always expand the smaller frontier
            if (count($beginSet) > count($endSet)) {
                $tmp      = $beginSet;
                $beginSet = $endSet;
                $endSet   = $tmp;
            }

            $temp = [];

            foreach ($beginSet as $word => $_) {
                for ($i = 0; $i < $L; $i++) {
                    $originalChar = $word[$i];
                    for ($c = 97; $c <= 122; $c++) { // 'a' to 'z'
                        $ch = chr($c);
                        if ($ch === $originalChar) continue;
                        $newWord = substr_replace($word, $ch, $i, 1);

                        if (isset($endSet[$newWord])) {
                            return $len + 1;
                        }

                        if (isset($wordSet[$newWord]) && !isset($temp[$newWord])) {
                            $temp[$newWord] = true;
                            // mark as visited
                            unset($wordSet[$newWord]);
                        }
                    }
                }
            }

            $beginSet = $temp;
            $len++;
        }

        return 0;
    }
}
```

## Swift

```swift
class Solution {
    func ladderLength(_ beginWord: String, _ endWord: String, _ wordList: [String]) -> Int {
        var wordSet = Set(wordList)
        if !wordSet.contains(endWord) { return 0 }
        
        let L = beginWord.count
        var allWords = wordList
        if !wordSet.contains(beginWord) {
            allWords.append(beginWord)
        }
        
        var patternMap = [String: [String]]()
        for word in allWords {
            var chars = Array(word)
            for i in 0..<L {
                let saved = chars[i]
                chars[i] = "*"
                let pattern = String(chars)
                patternMap[pattern, default: []].append(word)
                chars[i] = saved
            }
        }
        
        var queue: [(String, Int)] = [(beginWord, 1)]
        var visited: Set<String> = [beginWord]
        var index = 0
        
        while index < queue.count {
            let (current, level) = queue[index]
            index += 1
            var chars = Array(current)
            for i in 0..<L {
                let saved = chars[i]
                chars[i] = "*"
                let pattern = String(chars)
                if let neighbors = patternMap[pattern] {
                    for neighbor in neighbors {
                        if neighbor == endWord {
                            return level + 1
                        }
                        if !visited.contains(neighbor) {
                            visited.insert(neighbor)
                            queue.append((neighbor, level + 1))
                        }
                    }
                }
                chars[i] = saved
            }
        }
        
        return 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun ladderLength(beginWord: String, endWord: String, wordList: List<String>): Int {
        val dict = HashSet(wordList)
        if (!dict.contains(endWord)) return 0

        var beginSet = mutableSetOf(beginWord)
        var endSet = mutableSetOf(endWord)
        val visited = HashSet<String>()
        visited.add(beginWord)

        var steps = 1
        while (beginSet.isNotEmpty() && endSet.isNotEmpty()) {
            // Always expand the smaller frontier for efficiency
            if (beginSet.size > endSet.size) {
                val tmp = beginSet
                beginSet = endSet
                endSet = tmp
            }

            val nextLevel = mutableSetOf<String>()
            for (word in beginSet) {
                val chars = word.toCharArray()
                for (i in chars.indices) {
                    val original = chars[i]
                    for (c in 'a'..'z') {
                        if (c == original) continue
                        chars[i] = c
                        val newWord = String(chars)
                        if (endSet.contains(newWord)) {
                            return steps + 1
                        }
                        if (!visited.contains(newWord) && dict.contains(newWord)) {
                            visited.add(newWord)
                            nextLevel.add(newWord)
                        }
                    }
                    chars[i] = original
                }
            }

            beginSet = nextLevel
            steps++
        }
        return 0
    }
}
```

## Dart

```dart
class Solution {
  int ladderLength(String beginWord, String endWord, List<String> wordList) {
    final Set<String> dict = Set.from(wordList);
    if (!dict.contains(endWord)) return 0;

    Set<String> beginSet = {beginWord};
    Set<String> endSet = {endWord};
    Set<String> visited = {};

    int level = 1;
    while (beginSet.isNotEmpty && endSet.isNotEmpty) {
      // Always expand the smaller frontier
      if (beginSet.length > endSet.length) {
        final temp = beginSet;
        beginSet = endSet;
        endSet = temp;
      }

      Set<String> nextLevel = {};
      for (final word in beginSet) {
        List<int> chars = word.codeUnits;
        for (int i = 0; i < chars.length; i++) {
          int originalChar = chars[i];
          for (int c = 97; c <= 122; c++) { // 'a' to 'z'
            if (c == originalChar) continue;
            chars[i] = c;
            String newWord = String.fromCharCodes(chars);
            if (endSet.contains(newWord)) {
              return level + 1;
            }
            if (!visited.contains(newWord) && dict.contains(newWord)) {
              nextLevel.add(newWord);
              visited.add(newWord);
            }
          }
          chars[i] = originalChar; // restore
        }
      }

      beginSet = nextLevel;
      level++;
    }

    return 0;
  }
}
```

## Golang

```go
func ladderLength(beginWord string, endWord string, wordList []string) int {
	if len(wordList) == 0 {
		return 0
	}
	wordSet := make(map[string]bool, len(wordList))
	for _, w := range wordList {
		wordSet[w] = true
	}
	if !wordSet[endWord] {
		return 0
	}

	L := len(beginWord)
	allComboDict := make(map[string][]string)

	words := append(wordList, beginWord)
	for _, word := range words {
		for i := 0; i < L; i++ {
			pattern := word[:i] + "*" + word[i+1:]
			allComboDict[pattern] = append(allComboDict[pattern], word)
		}
	}

	type pair struct {
		word  string
		level int
	}
	queue := []pair{{beginWord, 1}}
	visited := map[string]bool{beginWord: true}

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		for i := 0; i < L; i++ {
			pattern := cur.word[:i] + "*" + cur.word[i+1:]
			for _, neighbor := range allComboDict[pattern] {
				if neighbor == endWord {
					return cur.level + 1
				}
				if !visited[neighbor] {
					visited[neighbor] = true
					queue = append(queue, pair{neighbor, cur.level + 1})
				}
			}
		}
	}

	return 0
}
```

## Ruby

```ruby
require 'set'

def ladder_length(begin_word, end_word, word_list)
  word_set = Set.new(word_list)
  return 0 unless word_set.include?(end_word)

  word_set.delete(begin_word)

  begin_set = Set.new([begin_word])
  end_set   = Set.new([end_word])

  steps = 1

  while !begin_set.empty? && !end_set.empty?
    if begin_set.size > end_set.size
      begin_set, end_set = end_set, begin_set
    end

    next_level = Set.new
    begin_set.each do |word|
      chars = word.chars
      (0...chars.length).each do |i|
        original = chars[i]
        ('a'..'z').each do |c|
          next if c == original
          chars[i] = c
          new_word = chars.join
          return steps + 1 if end_set.include?(new_word)
          if word_set.include?(new_word)
            next_level.add(new_word)
            word_set.delete(new_word)
          end
        end
        chars[i] = original
      end
    end

    begin_set = next_level
    steps += 1
  end

  0
end
```

## Scala

```scala
object Solution {
    def ladderLength(beginWord: String, endWord: String, wordList: List[String]): Int = {
        val wordSet = scala.collection.mutable.Set[String]() ++= wordList
        if (!wordSet.contains(endWord)) return 0

        var beginSet = scala.collection.mutable.Set[String](beginWord)
        var endSet   = scala.collection.mutable.Set[String](endWord)

        var steps = 1

        while (beginSet.nonEmpty && endSet.nonEmpty) {
            // always expand the smaller frontier
            if (beginSet.size > endSet.size) {
                val tmp = beginSet
                beginSet = endSet
                endSet = tmp
            }

            val nextLevel = scala.collection.mutable.Set[String]()

            for (word <- beginSet) {
                val chars = word.toCharArray
                for (i <- chars.indices) {
                    val original = chars(i)
                    for (c <- 'a' to 'z') {
                        if (c == original) ()
                        else {
                            chars(i) = c
                            val newWord = String.valueOf(chars)

                            if (endSet.contains(newWord)) return steps + 1

                            if (wordSet.contains(newWord)) {
                                nextLevel.add(newWord)
                                wordSet.remove(newWord)
                            }
                        }
                    }
                    chars(i) = original
                }
            }

            beginSet = nextLevel
            steps += 1
        }

        0
    }
}
```

## Rust

```rust
use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 {
        let mut word_set: HashSet<String> = word_list.into_iter().collect();
        if !word_set.contains(&end_word) {
            return 0;
        }

        let mut queue: VecDeque<(String, i32)> = VecDeque::new();
        queue.push_back((begin_word.clone(), 1));

        while let Some((word, depth)) = queue.pop_front() {
            let mut chars: Vec<char> = word.chars().collect();
            for i in 0..chars.len() {
                let original = chars[i];
                for c in b'a'..=b'z' {
                    let ch = c as char;
                    if ch == original {
                        continue;
                    }
                    chars[i] = ch;
                    let new_word: String = chars.iter().collect();

                    if new_word == end_word {
                        return depth + 1;
                    }

                    if word_set.take(&new_word).is_some() {
                        queue.push_back((new_word.clone(), depth + 1));
                    }
                }
                chars[i] = original;
            }
        }

        0
    }
}
```

## Racket

```racket
(define/contract (ladder-length beginWord endWord wordList)
  (-> string? string? (listof string?) exact-integer?)
  (let* ((len (string-length beginWord))
         (word-set (make-hash)))
    ;; populate the dictionary set
    (for ([w wordList])
      (hash-set! word-set w #t))
    ;; if endWord not in dictionary, no possible transformation
    (if (not (hash-has-key? word-set endWord))
        0
        (let ((visited (make-hash)))
          (hash-set! visited beginWord #t)
          (let bfs ((queue (list (cons beginWord 1))) (vis visited))
            (cond
              [(null? queue) 0] ; exhausted all possibilities
              [else
               (define pair (car queue))
               (define word (car pair))
               (define steps (cdr pair))
               (define rest (cdr queue))
               (if (string=? word endWord)
                   steps
                   (let ((next '()))
                     (for ([i (in-range len)])
                       (for ([c-code (in-range 26)])
                         (define c (integer->char (+ (char->integer #\a) c-code)))
                         (define new-word
                           (string-append
                            (substring word 0 i)
                            (string c)
                            (substring word (+ i 1))))
                         (when (and (hash-has-key? word-set new-word)
                                    (not (hash-has-key? vis new-word)))
                           (hash-set! vis new-word #t)
                           (set! next (cons (cons new-word (+ steps 1)) next)))))
                     (bfs (append rest (reverse next)) vis))))])))))
```

## Erlang

```erlang
-module(solution).
-export([ladder_length/3]).

-spec ladder_length(BeginWord :: unicode:unicode_binary(),
                    EndWord   :: unicode:unicode_binary(),
                    WordList  :: [unicode:unicode_binary()]) -> integer().
ladder_length(BeginWord, EndWord, WordList) ->
    SetMap = maps:from_list([{W, true} || W <- WordList]),
    case maps:is_key(EndWord, SetMap) of
        false -> 0;
        true ->
            Visited0 = maps:put(BeginWord, true, #{}),
            Queue0   = queue:new(),
            Queue1   = queue:in({BeginWord, 1}, Queue0),
            bfs(SetMap, EndWord, Queue1, Visited0)
    end.

bfs(_SetMap, _EndWord, Queue, _Visited) ->
    case queue:out(Queue) of
        {empty, _} -> 0;
        {{value, {CurrWord, Level}}, Q1} ->
            if CurrWord =:= _EndWord ->
                    Level;
               true ->
                    Neighs     = gen_neighbors(CurrWord, _SetMap, _Visited),
                    NewVis     = lists:foldl(fun(W, Acc) -> maps:put(W, true, Acc) end,
                                            _Visited, Neighs),
                    Q2         = lists:foldl(fun(W, QAcc) ->
                                                queue:in({W, Level + 1}, QAcc)
                                            end, Q1, Neighs),
                    bfs(_SetMap, _EndWord, Q2, NewVis)
            end
    end.

gen_neighbors(WordBin, SetMap, Visited) ->
    Len = byte_size(WordBin),
    Letters = lists:seq($a, $z),
    gen_neighbors_pos(0, Len, WordBin, SetMap, Visited, Letters, []).

gen_neighbors_pos(Pos, Len, _WordBin, _SetMap, _Visited, _Letters, Acc) when Pos >= Len ->
    Acc;
gen_neighbors_pos(Pos, Len, WordBin, SetMap, Visited, Letters, Acc) ->
    <<Prefix:Pos/binary, _OldChar:8, Rest/binary>> = WordBin,
    NewAcc = lists:foldl(fun(C, A) ->
                NewWord = <<Prefix/binary, C, Rest/binary>>,
                case (maps:is_key(NewWord, SetMap) andalso not maps:is_key(NewWord, Visited)) of
                    true -> [NewWord | A];
                    false -> A
                end
            end, Acc, Letters),
    gen_neighbors_pos(Pos + 1, Len, WordBin, SetMap, Visited, Letters, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec ladder_length(begin_word :: String.t(), end_word :: String.t(), word_list :: [String.t()]) :: integer()
  def ladder_length(begin_word, end_word, word_list) do
    word_set = MapSet.new(word_list)

    if not MapSet.member?(word_set, end_word) do
      0
    else
      queue = :queue.in({begin_word, 1}, :queue.new())
      visited = MapSet.new([begin_word])
      bfs(queue, visited, word_set, end_word)
    end
  end

  defp bfs(queue, visited, word_set, end_word) do
    case :queue.out(queue) do
      {:empty, _} ->
        0

      {{:value, {word, dist}}, q_rest} ->
        if word == end_word do
          dist
        else
          len = byte_size(word)

          neighbors =
            for i <- 0..len - 1,
                c <- ?a..?z do
              <<prefix::binary-size(i), _old::utf8, suffix::binary>> = word
              <<prefix::binary, c::utf8, suffix::binary>>
            end

          result =
            Enum.reduce_while(neighbors, {q_rest, visited}, fn nb, {q_acc, v_acc} ->
              cond do
                nb == end_word ->
                  {:halt, {:found, dist + 1}}

                MapSet.member?(word_set, nb) and not MapSet.member?(v_acc, nb) ->
                  {:cont,
                   {
                     :queue.in({nb, dist + 1}, q_acc),
                     MapSet.put(v_acc, nb)
                   }}

                true ->
                  {:cont, {q_acc, v_acc}}
              end
            end)

          case result do
            {:found, ans} -> ans
            {new_q, new_vis} -> bfs(new_q, new_vis, word_set, end_word)
          end
        end
    end
  end
end
```
