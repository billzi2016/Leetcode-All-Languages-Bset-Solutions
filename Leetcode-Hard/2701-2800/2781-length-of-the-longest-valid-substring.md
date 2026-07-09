# 2781. Length of the Longest Valid Substring

## Cpp

```cpp
class Solution {
public:
    int longestValidSubstring(string word, vector<string>& forbidden) {
        unordered_set<string> forbSet(forbidden.begin(), forbidden.end());
        int n = word.size();
        int left = 0;
        int best = 0;
        const int LMAX = 10;
        for (int i = 0; i < n; ++i) {
            for (int len = 1; len <= LMAX && len <= i + 1; ++len) {
                string sub = word.substr(i - len + 1, len);
                if (forbSet.find(sub) != forbSet.end()) {
                    left = max(left, i - len + 2); // move start past this forbidden substring
                }
            }
            best = max(best, i - left + 1);
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int longestValidSubstring(String word, List<String> forbidden) {
        Set<String> forbSet = new HashSet<>(forbidden);
        int n = word.length();
        int left = 0;
        int maxLen = 0;
        for (int right = 0; right < n; ++right) {
            // examine substrings that end at 'right' with length up to 10
            for (int len = 1; len <= 10 && len <= right + 1; ++len) {
                int start = right - len + 1;
                String sub = word.substring(start, right + 1);
                if (forbSet.contains(sub)) {
                    left = Math.max(left, start + 1);
                }
            }
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def longestValidSubstring(self, word, forbidden):
        """
        :type word: str
        :type forbidden: List[str]
        :rtype: int
        """
        fset = set(forbidden)
        max_len = max((len(s) for s in forbidden), default=0)
        left = 0
        ans = 0
        n = len(word)
        for i in range(n):
            limit = min(max_len, i + 1)
            for l in range(1, limit + 1):
                if word[i - l + 1:i + 1] in fset:
                    left = max(left, i - l + 2)  # move start right after forbidden substring
            ans = max(ans, i - left + 1)
        return ans
```

## Python3

```python
class Solution:
    def longestValidSubstring(self, word: str, forbidden):
        forbid_set = set(forbidden)
        max_len = max((len(s) for s in forbidden), default=0)
        left = 0
        ans = 0
        n = len(word)
        for i in range(n):
            # check substrings ending at i with length up to max_len
            limit = min(max_len, i + 1)
            for l in range(1, limit + 1):
                if word[i - l + 1:i + 1] in forbid_set:
                    left = max(left, i - l + 2)  # start after the forbidden substring
            ans = max(ans, i - left + 1)
        return ans
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FORBIDDEN_LEN 10
#define HASH_BASE 131
#define TABLE_SIZE 200003   // a prime larger than 2 * 1e5

typedef struct Node {
    char str[MAX_FORBIDDEN_LEN + 1];
    int next;
} Node;

static unsigned int hash_str(const char *s) {
    unsigned long long h = 0;
    while (*s) {
        h = h * HASH_BASE + (unsigned char)(*s);
        s++;
    }
    return (unsigned int)(h % TABLE_SIZE);
}

int longestValidSubstring(char* word, char** forbidden, int forbiddenSize) {
    // Build hash table for forbidden strings
    Node *nodes = (Node *)malloc(sizeof(Node) * (size_t)forbiddenSize);
    int *head = (int *)malloc(sizeof(int) * TABLE_SIZE);
    for (int i = 0; i < TABLE_SIZE; ++i) head[i] = -1;

    for (int i = 0; i < forbiddenSize; ++i) {
        unsigned int h = hash_str(forbidden[i]);
        nodes[i].next = head[h];
        strncpy(nodes[i].str, forbidden[i], MAX_FORBIDDEN_LEN);
        nodes[i].str[MAX_FORBIDDEN_LEN] = '\0';
        head[h] = i;
    }

    // Helper lambda for existence check
    int exists(const char *s) {
        unsigned int h = hash_str(s);
        for (int idx = head[h]; idx != -1; idx = nodes[idx].next) {
            if (strcmp(nodes[idx].str, s) == 0) return 1;
        }
        return 0;
    }

    int n = (int)strlen(word);
    int left = 0, ans = 0;
    char buf[MAX_FORBIDDEN_LEN + 1];

    for (int i = 0; i < n; ++i) {
        int maxLen = (i + 1 < MAX_FORBIDDEN_LEN) ? (i + 1) : MAX_FORBIDDEN_LEN;
        for (int len = 1; len <= maxLen; ++len) {
            int start = i - len + 1;
            memcpy(buf, word + start, (size_t)len);
            buf[len] = '\0';
            if (exists(buf)) {
                int newLeft = start + 1; // i - len + 2
                if (newLeft > left) left = newLeft;
            }
        }
        int curLen = i - left + 1;
        if (curLen > ans) ans = curLen;
    }

    free(nodes);
    free(head);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int LongestValidSubstring(string word, IList<string> forbidden) {
        var forbidSet = new HashSet<string>(forbidden);
        int n = word.Length;
        int left = 0;
        int best = 0;
        for (int i = 0; i < n; i++) {
            int maxLen = Math.Min(10, i + 1);
            for (int len = 1; len <= maxLen; len++) {
                int start = i - len + 1;
                string sub = word.Substring(start, len);
                if (forbidSet.Contains(sub)) {
                    left = Math.Max(left, start + 1);
                }
            }
            best = Math.Max(best, i - left + 1);
        }
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @param {string[]} forbidden
 * @return {number}
 */
var longestValidSubstring = function(word, forbidden) {
    const forbidSet = new Set(forbidden);
    let maxForbiddenLen = 0;
    for (const s of forbidden) {
        if (s.length > maxForbiddenLen) maxForbiddenLen = s.length;
    }
    let left = 0;
    let best = 0;
    const n = word.length;
    for (let i = 0; i < n; ++i) {
        for (let len = 1; len <= maxForbiddenLen && i - len + 1 >= 0; ++len) {
            const sub = word.substring(i - len + 1, i + 1);
            if (forbidSet.has(sub)) {
                left = Math.max(left, i - len + 2);
            }
        }
        best = Math.max(best, i - left + 1);
    }
    return best;
};
```

## Typescript

```typescript
function longestValidSubstring(word: string, forbidden: string[]): number {
    const lenMap = new Map<number, Set<string>>();
    let maxLen = 0;
    for (const f of forbidden) {
        const l = f.length;
        if (!lenMap.has(l)) lenMap.set(l, new Set());
        lenMap.get(l)!.add(f);
        if (l > maxLen) maxLen = l;
    }
    let left = 0; // earliest allowed start index
    let ans = 0;
    const n = word.length;
    for (let i = 0; i < n; i++) {
        const limit = Math.min(maxLen, i + 1);
        for (let l = 1; l <= limit; l++) {
            const set = lenMap.get(l);
            if (!set) continue;
            const sub = word.substring(i - l + 1, i + 1);
            if (set.has(sub)) {
                left = Math.max(left, i - l + 2);
            }
        }
        ans = Math.max(ans, i - left + 1);
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @param String[] $forbidden
     * @return Integer
     */
    function longestValidSubstring($word, $forbidden) {
        // Group forbidden strings by their length for O(1) lookup
        $byLen = [];
        foreach ($forbidden as $f) {
            $l = strlen($f);
            if (!isset($byLen[$l])) {
                $byLen[$l] = [];
            }
            $byLen[$l][$f] = true;
        }

        // List of distinct lengths (max 10)
        $lenList = array_keys($byLen);

        $n = strlen($word);
        $left = 0;   // start index of current valid window
        $maxLen = 0;

        for ($i = 0; $i < $n; ++$i) {
            foreach ($lenList as $l) {
                $start = $i - $l + 1;
                if ($start < 0) {
                    continue;
                }
                // Extract substring of length $l ending at position $i
                $sub = substr($word, $start, $l);
                if (isset($byLen[$l][$sub])) {
                    // Move left bound to exclude the forbidden pattern
                    $left = max($left, $start + 1);
                }
            }
            $currLen = $i - $left + 1;
            if ($currLen > $maxLen) {
                $maxLen = $currLen;
            }
        }

        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func longestValidSubstring(_ word: String, _ forbidden: [String]) -> Int {
        let chars = Array(word)
        var forbidSet = Set<String>(forbidden)
        var left = 0
        var maxLen = 0
        let n = chars.count
        
        for i in 0..<n {
            var length = 1
            while length <= 10 && i - length + 1 >= 0 {
                let startIdx = i - length + 1
                let subStr = String(chars[startIdx...i])
                if forbidSet.contains(subStr) {
                    // Move left bound to the position after the start of this forbidden occurrence
                    let newLeft = startIdx + 1
                    if newLeft > left { left = newLeft }
                }
                length += 1
            }
            let curLen = i - left + 1
            if curLen > maxLen {
                maxLen = curLen
            }
        }
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class Node {
        val next = IntArray(26) { -1 }
        var fail: Int = 0
        val out = mutableListOf<Int>()
    }

    fun longestValidSubstring(word: String, forbidden: List<String>): Int {
        // Build trie of forbidden strings
        val nodes = ArrayList<Node>()
        nodes.add(Node()) // root at index 0
        for (pat in forbidden) {
            var cur = 0
            for (ch in pat) {
                val idx = ch - 'a'
                if (nodes[cur].next[idx] == -1) {
                    nodes.add(Node())
                    nodes[cur].next[idx] = nodes.size - 1
                }
                cur = nodes[cur].next[idx]
            }
            nodes[cur].out.add(pat.length)
        }

        // Build failure links using BFS
        val queue: ArrayDeque<Int> = ArrayDeque()
        for (c in 0 until 26) {
            val child = nodes[0].next[c]
            if (child != -1) {
                nodes[child].fail = 0
                queue.add(child)
            }
        }

        while (queue.isNotEmpty()) {
            val v = queue.removeFirst()
            for (c in 0 until 26) {
                val child = nodes[v].next[c]
                if (child != -1) {
                    var f = nodes[v].fail
                    while (f != 0 && nodes[f].next[c] == -1) {
                        f = nodes[f].fail
                    }
                    if (nodes[f].next[c] != -1) {
                        f = nodes[f].next[c]
                    }
                    nodes[child].fail = f
                    queue.add(child)
                }
            }
        }

        var left = 0          // start index of current valid window
        var best = 0
        var state = 0

        for (i in word.indices) {
            val idx = word[i] - 'a'
            var cur = state
            while (cur != 0 && nodes[cur].next[idx] == -1) {
                cur = nodes[cur].fail
            }
            if (nodes[cur].next[idx] != -1) {
                cur = nodes[cur].next[idx]
            } else {
                cur = 0
            }
            state = cur

            // Check all patterns ending at position i via output links
            var temp = state
            while (temp != 0) {
                for (len in nodes[temp].out) {
                    val newLeft = i - len + 2   // first index after the forbidden substring
                    if (newLeft > left) left = newLeft
                }
                temp = nodes[temp].fail
            }

            val currentLen = i - left + 1
            if (currentLen > best) best = currentLen
        }

        return best
    }
}
```

## Dart

```dart
class Solution {
  int longestValidSubstring(String word, List<String> forbidden) {
    final Set<String> forbSet = {...forbidden};
    int maxLen = 0;
    int left = 0;
    int n = word.length;

    int maxForbiddenLen = 0;
    for (var s in forbidden) {
      if (s.length > maxForbiddenLen) maxForbiddenLen = s.length;
    }

    for (int i = 0; i < n; ++i) {
      int limit = maxForbiddenLen;
      if (limit > i + 1) limit = i + 1;

      for (int len = 1; len <= limit; ++len) {
        String sub = word.substring(i - len + 1, i + 1);
        if (forbSet.contains(sub)) {
          int newLeft = i - len + 2;
          if (newLeft > left) left = newLeft;
        }
      }

      int curLen = i - left + 1;
      if (curLen > maxLen) maxLen = curLen;
    }

    return maxLen;
  }
}
```

## Golang

```go
func longestValidSubstring(word string, forbidden []string) int {
    forbidSet := make(map[string]struct{}, len(forbidden))
    maxLen := 0
    for _, s := range forbidden {
        forbidSet[s] = struct{}{}
        if len(s) > maxLen {
            maxLen = len(s)
        }
    }

    left, ans := 0, 0
    n := len(word)

    for i := 0; i < n; i++ {
        limit := maxLen
        if limit > i+1 {
            limit = i + 1
        }
        for l := 1; l <= limit; l++ {
            start := i - l + 1
            sub := word[start : i+1]
            if _, ok := forbidSet[sub]; ok && left < start+1 {
                left = start + 1
            }
        }
        curLen := i - left + 1
        if curLen > ans {
            ans = curLen
        }
    }

    return ans
}
```

## Ruby

```ruby
def longest_valid_substring(word, forbidden)
  children = []
  fail = []
  out = []

  children << Array.new(26, -1)
  fail << 0
  out << []

  forbidden.each do |pat|
    node = 0
    pat.each_byte do |b|
      c = b - 97
      nxt = children[node][c]
      if nxt == -1
        nxt = children.size
        children << Array.new(26, -1)
        fail << 0
        out << []
        children[node][c] = nxt
      end
      node = nxt
    end
    out[node] << pat.length
  end

  queue = []
  26.times do |c|
    child = children[0][c]
    if child != -1
      fail[child] = 0
      queue << child
    else
      children[0][c] = 0
    end
  end

  head = 0
  while head < queue.size
    r = queue[head]
    head += 1
    26.times do |c|
      child = children[r][c]
      if child != -1
        f = fail[r]
        fail_child = children[f][c]
        fail[child] = fail_child
        out[child].concat(out[fail_child]) unless out[fail_child].empty?
        queue << child
      else
        children[r][c] = children[fail[r]][c]
      end
    end
  end

  left = 0
  ans = 0
  node = 0
  word.each_byte.with_index do |b, i|
    c = b - 97
    node = children[node][c]
    out[node].each do |len|
      start_pos = i - len + 1
      left = start_pos + 1 if left < start_pos + 1
    end
    cur_len = i - left + 1
    ans = cur_len if cur_len > ans
  end

  ans
end
```

## Scala

```scala
object Solution {
    def longestValidSubstring(word: String, forbidden: List[String]): Int = {
        val forbidSet = forbidden.toHashSet
        var left = 0
        var best = 0
        val n = word.length
        for (i <- 0 until n) {
            var len = 1
            while (len <= 10 && i - len + 1 >= 0) {
                val sub = word.substring(i - len + 1, i + 1)
                if (forbidSet.contains(sub)) {
                    left = math.max(left, i - len + 2)
                }
                len += 1
            }
            best = math.max(best, i - left + 1)
        }
        best
    }
}
```

## Rust

```rust
use std::collections::HashSet;

#[derive(Clone)]
struct Node {
    next: [usize; 26],
    end: bool,
}
impl Node {
    fn new() -> Self {
        Node {
            next: [usize::MAX; 26],
            end: false,
        }
    }
}

impl Solution {
    pub fn longest_valid_substring(word: String, forbidden: Vec<String>) -> i32 {
        // Build reversed trie of forbidden strings
        let mut nodes = Vec::new();
        nodes.push(Node::new()); // root at index 0

        let mut max_len = 0usize;
        for f in &forbidden {
            let bytes = f.as_bytes();
            if bytes.len() > max_len {
                max_len = bytes.len();
            }
            let mut cur = 0usize;
            for &b in bytes.iter().rev() {
                let idx = (b - b'a') as usize;
                let nxt = nodes[cur].next[idx];
                if nxt == usize::MAX {
                    nodes.push(Node::new());
                    let new_idx = nodes.len() - 1;
                    nodes[cur].next[idx] = new_idx;
                    cur = new_idx;
                } else {
                    cur = nxt;
                }
            }
            nodes[cur].end = true;
        }

        let wbytes = word.as_bytes();
        let n = wbytes.len();
        let mut left: usize = 0; // earliest allowed start index
        let mut best: usize = 0;

        for i in 0..n {
            let mut cur = 0usize;
            // walk backwards up to max_len characters
            for offset in 0..max_len {
                if i < offset {
                    break;
                }
                let j = i - offset; // current character index moving leftwards
                let idx = (wbytes[j] - b'a') as usize;
                let nxt = nodes[cur].next[idx];
                if nxt == usize::MAX {
                    break;
                }
                cur = nxt;
                if nodes[cur].end {
                    // forbidden substring of length offset+1 ends at i, starts at j
                    // move left to j + 1
                    let new_left = j + 1;
                    if new_left > left {
                        left = new_left;
                    }
                    break; // shortest match found, no need to check longer ones
                }
            }
            let cur_len = i + 1 - left;
            if cur_len > best {
                best = cur_len;
            }
        }

        best as i32
    }
}
```

## Racket

```racket
(define/contract (longest-valid-substring word forbidden)
  (-> string? (listof string?) exact-integer?)
  (let* ([n (string-length word)]
         [forbidden-set
          (let ([hs (make-hash)])
            (for ([s (in-list forbidden)])
              (hash-set! hs s #t))
            hs)]
         [max-len 10])
    (let loop ((i 0) (left 0) (best 0))
      (if (= i n)
          best
          (let* ([limit (if (< (+ i 1) max-len) (+ i 1) max-len)]
                 [new-left
                  (let inner ((len 1) (cur-left left))
                    (if (> len limit)
                        cur-left
                        (let* ([start (- i (sub1 len))]
                               [substr (substring word start (+ i 1))])
                          (if (hash-has-key? forbidden-set substr)
                              (inner (add1 len) (max cur-left (add1 start)))
                              (inner (add1 len) cur-left)))))]
                 [new-best (max best (- i new-left + 1))])
            (loop (add1 i) new-left new-best))))))
```

## Erlang

```erlang
-spec longest_valid_substring(Word :: unicode:unicode_binary(), Forbidden :: [unicode:unicode_binary()]) -> integer().
longest_valid_substring(Word, Forbidden) ->
    Set = maps:from_list([{F, true} || F <- Forbidden]),
    N = byte_size(Word),
    loop(0, 0, 0, Word, Set, N).

loop(Index, Left, MaxLen, _Word, _Set, N) when Index >= N ->
    MaxLen;
loop(Index, Left, MaxLen, Word, Set, N) ->
    NewLeft = update_left(Index, Left, Word, Set),
    CurrLen = Index - NewLeft + 1,
    NewMax = if CurrLen > MaxLen -> CurrLen; true -> MaxLen end,
    loop(Index + 1, NewLeft, NewMax, Word, Set, N).

update_left(Index, Left, Word, Set) ->
    MaxCheck = erlang:min(10, Index + 1),
    update_len(1, MaxCheck, Index, Left, Word, Set).

update_len(Len, MaxLen, _Index, CurLeft, _Word, _Set) when Len > MaxLen ->
    CurLeft;
update_len(Len, MaxLen, Index, CurLeft, Word, Set) ->
    Start = Index - Len + 1,
    Sub = binary:part(Word, Start, Len),
    case maps:is_key(Sub, Set) of
        true ->
            NewLeft = erlang:max(CurLeft, Index - Len + 2),
            update_len(Len + 1, MaxLen, Index, NewLeft, Word, Set);
        false ->
            update_len(Len + 1, MaxLen, Index, CurLeft, Word, Set)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_valid_substring(word :: String.t(), forbidden :: [String.t()]) :: integer()
  def longest_valid_substring(word, forbidden) do
    forbid_set = MapSet.new(forbidden)
    n = byte_size(word)

    {_left, max_len} =
      Enum.reduce(0..(n - 1), {0, 0}, fn i, {left, best} ->
        max_check = min(10, i + 1)

        new_left =
          Enum.reduce(1..max_check, left, fn l, acc ->
            start = i - l + 1
            sub = :binary.part(word, start, l)

            if MapSet.member?(forbid_set, sub) do
              max(acc, start + 1)
            else
              acc
            end
          end)

        cur_len = i - new_left + 1
        new_best = if cur_len > best, do: cur_len, else: best
        {new_left, new_best}
      end)

    max_len
  end
end
```
