# 2707. Extra Characters in a String

## Cpp

```cpp
class Solution {
public:
    struct TrieNode {
        int next[26];
        bool word;
        TrieNode() {
            std::fill(begin(next), end(next), -1);
            word = false;
        }
    };
    
    int minExtraChar(string s, vector<string>& dictionary) {
        // Build trie
        vector<TrieNode> trie(1); // root at index 0
        for (const string& w : dictionary) {
            int node = 0;
            for (char ch : w) {
                int idx = ch - 'a';
                if (trie[node].next[idx] == -1) {
                    trie[node].next[idx] = trie.size();
                    trie.emplace_back();
                }
                node = trie[node].next[idx];
            }
            trie[node].word = true;
        }
        
        int n = s.size();
        vector<int> dp(n + 1, 0);
        dp[n] = 0;
        for (int i = n - 1; i >= 0; --i) {
            int best = dp[i + 1] + 1; // treat s[i] as extra
            int node = 0;
            for (int j = i; j < n; ++j) {
                int idx = s[j] - 'a';
                if (trie[node].next[idx] == -1) break;
                node = trie[node].next[idx];
                if (trie[node].word) {
                    best = min(best, dp[j + 1]);
                }
            }
            dp[i] = best;
        }
        return dp[0];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minExtraChar(String s, String[] dictionary) {
        Set<String> dict = new HashSet<>(Arrays.asList(dictionary));
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[n] = 0;
        for (int i = n - 1; i >= 0; --i) {
            // Assume character at i is extra
            dp[i] = 1 + dp[i + 1];
            for (int j = i; j < n; ++j) {
                String sub = s.substring(i, j + 1);
                if (dict.contains(sub)) {
                    dp[i] = Math.min(dp[i], dp[j + 1]);
                }
            }
        }
        return dp[0];
    }
}
```

## Python

```python
class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        class TrieNode:
            __slots__ = ('children', 'is_word')
            def __init__(self):
                self.children = {}
                self.is_word = False

        root = TrieNode()
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_word = True

        n = len(s)
        dp = [0] * (n + 1)   # dp[i]: min extra chars from i to end
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            # option: treat s[i] as extra character
            best = 1 + dp[i + 1]
            node = root
            j = i
            while j < n and s[j] in node.children:
                node = node.children[s[j]]
                if node.is_word:
                    best = min(best, dp[j + 1])
                j += 1
            dp[i] = best
        return dp[0]
```

## Python3

```python
from typing import List

class TrieNode:
    __slots__ = ("children", "is_word")
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Build trie
        root = TrieNode()
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_word = True

        n = len(s)
        dp = [0] * (n + 1)   # dp[i]: min extra chars from i to end
        dp[n] = 0

        for start in range(n - 1, -1, -1):
            # option: treat s[start] as extra character
            best = dp[start + 1] + 1
            node = root
            for end in range(start, n):
                ch = s[end]
                if ch not in node.children:
                    break
                node = node.children[ch]
                if node.is_word:
                    # no extra chars added for this word
                    best = min(best, dp[end + 1])
            dp[start] = best

        return dp[0]
```

## C

```c
#include <string.h>
#include <stdlib.h>

int minExtraChar(char* s, char** dictionary, int dictionarySize) {
    int n = strlen(s);
    int *dp = (int *)malloc((n + 1) * sizeof(int));
    dp[n] = 0;
    for (int i = n - 1; i >= 0; --i) {
        dp[i] = 1 + dp[i + 1]; // treat s[i] as extra
        for (int d = 0; d < dictionarySize; ++d) {
            const char *w = dictionary[d];
            int len = strlen(w);
            if (len <= n - i && strncmp(s + i, w, len) == 0) {
                if (dp[i] > dp[i + len]) dp[i] = dp[i + len];
            }
        }
    }
    int ans = dp[0];
    free(dp);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private class TrieNode {
        public Dictionary<char, TrieNode> Children = new Dictionary<char, TrieNode>();
        public bool IsWord = false;
    }
    
    public int MinExtraChar(string s, string[] dictionary) {
        // Build trie
        TrieNode root = new TrieNode();
        foreach (var word in dictionary) {
            var node = root;
            foreach (char c in word) {
                if (!node.Children.ContainsKey(c)) {
                    node.Children[c] = new TrieNode();
                }
                node = node.Children[c];
            }
            node.IsWord = true;
        }

        int n = s.Length;
        int[] dp = new int[n + 1];
        dp[n] = 0;

        for (int start = n - 1; start >= 0; --start) {
            // Option: treat current character as extra
            dp[start] = dp[start + 1] + 1;

            TrieNode node = root;
            for (int end = start; end < n; ++end) {
                char c = s[end];
                if (!node.Children.ContainsKey(c)) break;
                node = node.Children[c];
                if (node.IsWord) {
                    dp[start] = Math.Min(dp[start], dp[end + 1]);
                }
            }
        }

        return dp[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string[]} dictionary
 * @return {number}
 */
var minExtraChar = function(s, dictionary) {
    const wordSet = new Set(dictionary);
    const n = s.length;
    const dp = new Array(n + 1).fill(0);
    // base: dp[n] = 0 (no characters left)
    for (let i = n - 1; i >= 0; i--) {
        // option: treat s[i] as extra character
        let best = dp[i + 1] + 1;
        // try all substrings starting at i
        for (let j = i; j < n; j++) {
            const sub = s.slice(i, j + 1);
            if (wordSet.has(sub)) {
                best = Math.min(best, dp[j + 1]);
            }
        }
        dp[i] = best;
    }
    return dp[0];
};
```

## Typescript

```typescript
function minExtraChar(s: string, dictionary: string[]): number {
    class TrieNode {
        children: Map<string, TrieNode>;
        isWord: boolean;
        constructor() {
            this.children = new Map();
            this.isWord = false;
        }
    }

    const root = new TrieNode();

    for (const word of dictionary) {
        let node = root;
        for (const ch of word) {
            if (!node.children.has(ch)) {
                node.children.set(ch, new TrieNode());
            }
            node = node.children.get(ch)!;
        }
        node.isWord = true;
    }

    const n = s.length;
    const dp: number[] = new Array(n + 1).fill(0);
    dp[n] = 0;

    for (let i = n - 1; i >= 0; --i) {
        let best = 1 + dp[i + 1]; // treat s[i] as extra character
        let node = root;
        for (let j = i; j < n; ++j) {
            const ch = s[j];
            if (!node.children.has(ch)) break;
            node = node.children.get(ch)!;
            if (node.isWord) {
                best = Math.min(best, dp[j + 1]);
            }
        }
        dp[i] = best;
    }

    return dp[0];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String[] $dictionary
     * @return Integer
     */
    function minExtraChar($s, $dictionary) {
        $n = strlen($s);
        // Build a hash set for O(1) lookups
        $dictSet = [];
        foreach ($dictionary as $word) {
            $dictSet[$word] = true;
        }

        // dp[i] = minimum extra characters for suffix starting at i
        $dp = array_fill(0, $n + 1, 0);
        $dp[$n] = 0;

        for ($i = $n - 1; $i >= 0; $i--) {
            // Option: treat s[i] as extra character
            $best = $dp[$i + 1] + 1;
            // Try all substrings starting at i
            for ($j = $i; $j < $n; $j++) {
                $sub = substr($s, $i, $j - $i + 1);
                if (isset($dictSet[$sub])) {
                    $best = min($best, $dp[$j + 1]);
                }
            }
            $dp[$i] = $best;
        }

        return $dp[0];
    }
}
```

## Swift

```swift
class Solution {
    func minExtraChar(_ s: String, _ dictionary: [String]) -> Int {
        let chars = Array(s)
        let n = chars.count
        let dictSet = Set(dictionary)
        var memo = Array(repeating: -1, count: n + 1)

        func dfs(_ i: Int) -> Int {
            if i == n { return 0 }
            if memo[i] != -1 { return memo[i] }

            // Option 1: treat current character as extra
            var best = 1 + dfs(i + 1)

            // Build substrings starting at i incrementally
            var cur = ""
            for j in i..<n {
                cur.append(chars[j])
                if dictSet.contains(cur) {
                    let candidate = dfs(j + 1)
                    if candidate < best {
                        best = candidate
                    }
                }
            }

            memo[i] = best
            return best
        }

        return dfs(0)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minExtraChar(s: String, dictionary: Array<String>): Int {
        val root = TrieNode()
        for (word in dictionary) {
            var node = root
            for (ch in word) {
                val idx = ch - 'a'
                if (node.children[idx] == null) node.children[idx] = TrieNode()
                node = node.children[idx]!!
            }
            node.isWord = true
        }

        val n = s.length
        val memo = IntArray(n + 1) { -1 }

        fun dfs(pos: Int): Int {
            if (pos == n) return 0
            if (memo[pos] != -1) return memo[pos]
            var ans = 1 + dfs(pos + 1) // treat s[pos] as extra character
            var node = root
            var j = pos
            while (j < n) {
                val idx = s[j] - 'a'
                node = node.children[idx] ?: break
                if (node.isWord) {
                    ans = minOf(ans, dfs(j + 1))
                }
                j++
            }
            memo[pos] = ans
            return ans
        }

        return dfs(0)
    }

    private class TrieNode(var isWord: Boolean = false) {
        val children = arrayOfNulls<TrieNode>(26)
    }
}
```

## Dart

```dart
class Solution {
  int minExtraChar(String s, List<String> dictionary) {
    final n = s.length;
    final dictSet = Set<String>.from(dictionary);
    final dp = List<int>.filled(n + 1, 0);
    // dp[n] is already 0
    for (int i = n - 1; i >= 0; --i) {
      int best = 1 + dp[i + 1]; // treat s[i] as extra character
      for (int j = i; j < n; ++j) {
        if (dictSet.contains(s.substring(i, j + 1))) {
          best = best < dp[j + 1] ? best : dp[j + 1];
        }
      }
      dp[i] = best;
    }
    return dp[0];
  }
}
```

## Golang

```go
func minExtraChar(s string, dictionary []string) int {
	n := len(s)
	dict := make(map[string]struct{}, len(dictionary))
	for _, w := range dictionary {
		dict[w] = struct{}{}
	}
	memo := make([]int, n+1)
	for i := range memo {
		memo[i] = -1
	}
	var dfs func(int) int
	dfs = func(i int) int {
		if i == n {
			return 0
		}
		if memo[i] != -1 {
			return memo[i]
		}
		best := 1 + dfs(i+1)
		for j := i; j < n; j++ {
			sub := s[i : j+1]
			if _, ok := dict[sub]; ok {
				cand := dfs(j + 1)
				if cand < best {
					best = cand
				}
			}
		}
		memo[i] = best
		return best
	}
	return dfs(0)
}
```

## Ruby

```ruby
require 'set'

def min_extra_char(s, dictionary)
  dict = Set.new(dictionary)
  n = s.length
  dp = Array.new(n + 1, 0)

  (n - 1).downto(0) do |i|
    best = 1 + dp[i + 1] # treat s[i] as extra character
    (i...n).each do |j|
      if dict.include?(s[i..j])
        cand = dp[j + 1]
        best = cand if cand < best
      end
    end
    dp[i] = best
  end

  dp[0]
end
```

## Scala

```scala
object Solution {
    def minExtraChar(s: String, dictionary: Array[String]): Int = {
        class TrieNode {
            val children: Array[TrieNode] = new Array[TrieNode](26)
            var isWord: Boolean = false
        }
        val root = new TrieNode()
        // Build trie from dictionary
        for (word <- dictionary) {
            var node = root
            for (ch <- word) {
                val idx = ch - 'a'
                if (node.children(idx) == null) node.children(idx) = new TrieNode()
                node = node.children(idx)
            }
            node.isWord = true
        }

        val n = s.length
        val dp = new Array[Int](n + 1)
        dp(n) = 0

        import scala.util.control.Breaks.{break, breakable}
        for (start <- (n - 1) to 0 by -1) {
            var best = dp(start + 1) + 1 // treat current char as extra
            var node = root
            var end = start
            breakable {
                while (end < n) {
                    val idx = s.charAt(end) - 'a'
                    if (node.children(idx) == null) break
                    node = node.children(idx)
                    if (node.isWord) {
                        best = math.min(best, dp(end + 1))
                    }
                    end += 1
                }
            }
            dp(start) = best
        }

        dp(0)
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn min_extra_char(s: String, dictionary: Vec<String>) -> i32 {
        let dict_set: HashSet<String> = dictionary.into_iter().collect();
        let n = s.len();
        let mut dp = vec![0usize; n + 1];
        dp[n] = 0;
        for i in (0..n).rev() {
            // case: treat s[i] as extra character
            let mut best = 1 + dp[i + 1];
            // try all substrings starting at i
            for j in i..n {
                // slice is safe because input consists of lowercase ASCII letters
                if dict_set.contains(&s[i..j + 1]) {
                    best = best.min(dp[j + 1]);
                }
            }
            dp[i] = best;
        }
        dp[0] as i32
    }
}
```

## Racket

```racket
#lang racket

(provide min-extra-char)

(define/contract (min-extra-char s dictionary)
  (-> string? (listof string?) exact-integer?)
  (let* ((n (string-length s))
         (dict (make-hash)))
    (for ([w dictionary])
      (hash-set! dict w #t))
    (define memo (make-vector (+ n 1) -1))
    (define (dp i)
      (if (= i n)
          0
          (let ((cached (vector-ref memo i)))
            (if (not (= cached -1))
                cached
                (let loop ((j i)
                           (best (+ 1 (dp (+ i 1))))) ; treat s[i] as extra char
                  (if (>= j n)
                      (begin
                        (vector-set! memo i best)
                        best)
                      (let* ((sub (substring s i (+ j 1)))
                             (new-best (if (hash-has-key? dict sub)
                                           (min best (dp (+ j 1)))
                                           best)))
                        (loop (+ j 1) new-best))))))))
    (dp 0)))
```

## Erlang

```erlang
-spec min_extra_char(S :: unicode:unicode_binary(), Dictionary :: [unicode:unicode_binary()]) -> integer().
min_extra_char(S, Dictionary) ->
    Len = byte_size(S),
    Set = maps:from_list([{Word, true} || Word <- Dictionary]),
    DP0 = #{Len => 0},
    FinalDP = loop(Len - 1, S, Len, Set, DP0),
    maps:get(0, FinalDP).

loop(-1, _S, _Len, _Set, DP) ->
    DP;
loop(I, S, Len, Set, DP) ->
    BaseAns = maps:get(I + 1, DP) + 1,
    MinAns = inner(I, I, BaseAns, S, Len, Set, DP),
    NewDP = maps:put(I, MinAns, DP),
    loop(I - 1, S, Len, Set, NewDP).

inner(_I, J, Ans, _S, Len, _Set, _DP) when J >= Len ->
    Ans;
inner(I, J, Ans, S, Len, Set, DP) ->
    SubLen = J - I + 1,
    Sub = binary:part(S, I, SubLen),
    NewAns = case maps:is_key(Sub, Set) of
        true ->
            Candidate = maps:get(J + 1, DP),
            erlang:min(Ans, Candidate);
        false -> Ans
    end,
    inner(I, J + 1, NewAns, S, Len, Set, DP).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_extra_char(s :: String.t(), dictionary :: [String.t()]) :: integer()
  def min_extra_char(s, dictionary) do
    dict = MapSet.new(dictionary)
    n = String.length(s)

    dp =
      Enum.reduce(Enum.reverse(0..n - 1), %{}, fn i, acc ->
        # Assume character at position i is extra
        best = Map.get(acc, i + 1, 0) + 1

        best =
          Enum.reduce(i..(n - 1), best, fn j, cur_best ->
            sub = String.slice(s, i, j - i + 1)

            if MapSet.member?(dict, sub) do
              candidate = Map.get(acc, j + 1, 0)
              min(cur_best, candidate)
            else
              cur_best
            end
          end)

        Map.put(acc, i, best)
      end)

    Map.get(dp, 0, 0)
  end
end
```
