# 3597. Partition String

## Cpp

```cpp
class Solution {
public:
    struct Node {
        int child[26];
        bool end;
        Node() : end(false) { fill(child, child + 26, -1); }
    };
    
    vector<string> partitionString(string s) {
        vector<Node> trie(1); // root at index 0
        vector<string> res;
        int n = s.size();
        int i = 0;
        while (i < n) {
            int node = 0;
            int j = i;
            while (true) {
                int c = s[j] - 'a';
                if (trie[node].child[c] == -1) {
                    trie[node].child[c] = trie.size();
                    trie.emplace_back();
                }
                node = trie[node].child[c];
                if (!trie[node].end) {
                    trie[node].end = true;
                    res.push_back(s.substr(i, j - i + 1));
                    i = j + 1;
                    break;
                } else {
                    ++j; // need a longer substring
                }
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<String> partitionString(String s) {
        java.util.List<String> result = new java.util.ArrayList<>();
        java.util.Set<Character> seen = new java.util.HashSet<>();
        int start = 0;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (seen.contains(ch)) {
                result.add(s.substring(start, i));
                start = i;
                seen.clear();
            }
            seen.add(ch);
        }
        result.add(s.substring(start));
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        seen = set()
        cur_start = 0
        for i, ch in enumerate(s):
            if ch in seen:
                # end current segment before this character
                res.append(s[cur_start:i])
                cur_start = i
                seen.clear()
            seen.add(ch)
        # append the last segment
        res.append(s[cur_start:])
        return res
```

## Python3

```python
from typing import List

class Solution:
    def partitionString(self, s: str) -> List[str]:
        res = []
        seen = set()
        start = 0
        for i, ch in enumerate(s):
            if ch in seen:
                res.append(s[start:i])
                start = i
                seen.clear()
            seen.add(ch)
        res.append(s[start:])
        return res
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char** partitionString(char* s, int* returnSize) {
    int n = 0;
    while (s[n] != '\0') n++;

    // First pass: count segments
    bool seen[26] = {false};
    int segCount = 0;
    for (int i = 0; i < n; ++i) {
        int idx = s[i] - 'a';
        if (seen[idx]) {
            segCount++;
            memset(seen, 0, sizeof(seen));
        }
        seen[idx] = true;
    }
    segCount++; // last segment

    char **res = (char **)malloc(segCount * sizeof(char *));
    int curStart = 0;
    int curSeg = 0;
    memset(seen, 0, sizeof(seen));

    for (int i = 0; i < n; ++i) {
        int idx = s[i] - 'a';
        if (seen[idx]) {
            int len = i - curStart;
            char *sub = (char *)malloc((len + 1) * sizeof(char));
            memcpy(sub, s + curStart, len);
            sub[len] = '\0';
            res[curSeg++] = sub;

            // start new segment
            curStart = i;
            memset(seen, 0, sizeof(seen));
        }
        seen[idx] = true;
    }

    // last segment
    int len = n - curStart;
    char *sub = (char *)malloc((len + 1) * sizeof(char));
    memcpy(sub, s + curStart, len);
    sub[len] = '\0';
    res[curSeg++] = sub;

    *returnSize = segCount;
    return res;
}
```

## Csharp

```csharp
using System.Collections.Generic;
using System.Text;

public class Solution {
    public IList<string> PartitionString(string s) {
        var used = new HashSet<string>();
        var result = new List<string>();
        int n = s.Length;
        int i = 0;
        while (i < n) {
            var sb = new StringBuilder();
            int j = i;
            string segment = "";
            // Build the smallest possible substring starting at i that is not used yet.
            while (j < n) {
                sb.Append(s[j]);
                segment = sb.ToString();
                if (!used.Contains(segment)) {
                    break;
                }
                j++;
            }
            // If we reached the end and still have a duplicate, we keep it as the last segment.
            used.Add(segment);
            result.Add(segment);
            i = j + 1;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var partitionString = function(s) {
    const res = [];
    let seen = new Set();
    let start = 0;
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (seen.has(ch)) {
            // end current segment before duplicate
            res.push(s.slice(start, i));
            // start new segment at current character
            start = i;
            seen.clear();
        }
        seen.add(ch);
    }
    // push the final segment
    res.push(s.slice(start));
    return res;
};
```

## Typescript

```typescript
function partitionString(s: string): string[] {
    const n = s.length;
    const used = new Set<string>();
    const result: string[] = [];
    let i = 0;
    while (i < n) {
        let len = 1;
        // Find the smallest length such that the substring is not used yet
        while (i + len <= n && used.has(s.slice(i, i + len))) {
            len++;
        }
        const seg = s.slice(i, i + len);
        result.push(seg);
        used.add(seg);
        i += len;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function partitionString($s) {
        $n = strlen($s);
        $result = [];
        $current = '';
        $seen = [];

        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if (isset($seen[$ch])) {
                // duplicate character, start new segment
                $result[] = $current;
                $current = $ch;
                $seen = [$ch => true];
            } else {
                $current .= $ch;
                $seen[$ch] = true;
            }
        }

        if ($current !== '') {
            $result[] = $current;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func partitionString(_ s: String) -> [String] {
        var result = [String]()
        var seen = Set<Character>()
        var current = ""
        for ch in s {
            if seen.contains(ch) {
                result.append(current)
                current = ""
                seen.removeAll()
            }
            current.append(ch)
            seen.insert(ch)
        }
        if !current.isEmpty {
            result.append(current)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun partitionString(s: String): List<String> {
        val result = mutableListOf<String>()
        val seen = HashSet<Char>()
        var sb = StringBuilder()
        for (ch in s) {
            if (seen.contains(ch)) {
                result.add(sb.toString())
                sb = StringBuilder()
                seen.clear()
            }
            sb.append(ch)
            seen.add(ch)
        }
        if (sb.isNotEmpty()) {
            result.add(sb.toString())
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> partitionString(String s) {
    List<String> result = [];
    Set<int> seen = {};
    int start = 0;
    for (int i = 0; i < s.length; i++) {
      int ch = s.codeUnitAt(i);
      if (seen.contains(ch)) {
        result.add(s.substring(start, i));
        start = i;
        seen.clear();
        seen.add(ch);
      } else {
        seen.add(ch);
      }
    }
    if (start < s.length) {
      result.add(s.substring(start));
    }
    return result;
  }
}
```

## Golang

```go
func partitionString(s string) []string {
    var result []string
    seen := make(map[byte]bool)
    start := 0
    for i := 0; i < len(s); i++ {
        c := s[i]
        if seen[c] {
            result = append(result, s[start:i])
            start = i
            seen = make(map[byte]bool)
        }
        seen[c] = true
    }
    result = append(result, s[start:])
    return result
}
```

## Ruby

```ruby
def partition_string(s)
  result = []
  seen = {}
  start_idx = 0

  s.each_char.with_index do |ch, i|
    if seen[ch]
      result << s[start_idx...i]
      start_idx = i
      seen.clear
    end
    seen[ch] = true
  end

  result << s[start_idx..-1]
  result
end
```

## Scala

```scala
object Solution {
    def partitionString(s: String): List[String] = {
        import scala.collection.mutable.{HashSet, ListBuffer}
        val seen = HashSet.empty[String]
        val result = ListBuffer.empty[String]
        var i = 0
        val n = s.length
        while (i < n) {
            var cur = ""
            var j = i
            while (j < n && seen.contains(cur + s.charAt(j))) {
                cur += s.charAt(j)
                j += 1
            }
            if (j == n) {
                // No new unique segment can be formed; terminate.
                i = n
            } else {
                val seg = cur + s.charAt(j)
                result += seg
                seen.add(seg)
                i = j + 1
            }
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn partition_string(s: String) -> Vec<String> {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut result: Vec<String> = Vec::new();
        let mut seen = [false; 26];
        let mut start = 0;
        for i in 0..n {
            let idx = (bytes[i] - b'a') as usize;
            if seen[idx] {
                // cut before current character
                result.push(s[start..i].to_string());
                // reset for new segment
                seen = [false; 26];
                start = i;
            }
            seen[(bytes[i] - b'a') as usize] = true;
        }
        // push the last segment
        if start < n {
            result.push(s[start..n].to_string());
        }
        result
    }
}
```

## Racket

```racket
(define (partition-string s)
  (let* ((n (string-length s))
         (seen (make-hash)))
    (let loop ((i 0) (acc '()))
      (if (= i n)
          (reverse acc)
          (let inner ((j i) (cur ""))
            (if (= j n)
                (reverse acc)
                (let* ((new-cur (string-append cur (substring s j (+ j 1)))))
                  (if (hash-has-key? seen new-cur)
                      (inner (+ j 1) new-cur)
                      (begin
                        (hash-set! seen new-cur #t)
                        (loop (+ j 1) (cons new-cur acc)))))))))))
```

## Erlang

```erlang
-module(solution).
-export([partition_string/1]).

-spec partition_string(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
partition_string(S) ->
    Chars = binary_to_list(S),
    SegmentsRev = process(Chars, #{}, []),
    lists:reverse(SegmentsRev).

process([], _Trie, Acc) ->
    Acc;
process(RestChars, Trie, Acc) ->
    {Prefix, RestAfterMatch} = match_prefix(RestChars, Trie, []),
    case RestAfterMatch of
        [] ->
            Acc; % no more characters
        [NewChar | Rest] ->
            Phrase = Prefix ++ [NewChar],
            SegmentBin = list_to_binary(Phrase),
            NewTrie = insert_new(Trie, Prefix, NewChar),
            process(Rest, NewTrie, [SegmentBin | Acc])
    end.

match_prefix([], _Node, AccRev) ->
    {lists:reverse(AccRev), []};
match_prefix([C|Rest] = Input, Node, AccRev) ->
    case maps:get(C, Node, undefined) of
        undefined ->
            {lists:reverse(AccRev), Input};
        Child ->
            match_prefix(Rest, Child, [C | AccRev])
    end.

insert_new(Trie, [], NewChar) ->
    % add new leaf under current node
    case maps:is_key(NewChar, Trie) of
        true -> Trie;
        false -> maps:put(NewChar, #{}, Trie)
    end;
insert_new(Trie, [C|RestPrefix], NewChar) ->
    Child = maps:get(C, Trie, #{}),
    UpdatedChild = insert_new(Child, RestPrefix, NewChar),
    maps:put(C, UpdatedChild, Trie).
```

## Elixir

```elixir
defmodule Solution do
  @spec partition_string(s :: String.t) :: [String.t]
  def partition_string(s) do
    chars = String.graphemes(s)

    {segments_rev, cur_rev, _set} =
      Enum.reduce(chars, {[], [], MapSet.new()}, fn ch,
                                                    {segs, cur, set} ->
        if MapSet.member?(set, ch) do
          # finish current segment and start a new one with the current character
          seg = cur |> Enum.reverse() |> Enum.join("")
          {[seg | segs], [ch], MapSet.new([ch])}
        else
          # continue building the current segment
          {segs, [ch | cur], MapSet.put(set, ch)}
        end
      end)

    # add the last segment if any characters remain
    result =
      case cur_rev do
        [] -> segments_rev
        _ ->
          seg = cur_rev |> Enum.reverse() |> Enum.join("")
          [seg | segments_rev]
      end

    Enum.reverse(result)
  end
end
```
