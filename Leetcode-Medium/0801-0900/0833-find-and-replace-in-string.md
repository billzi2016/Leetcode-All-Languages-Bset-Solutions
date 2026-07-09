# 0833. Find And Replace in String

## Cpp

```cpp
class Solution {
public:
    string findReplaceString(string s, vector<int>& indices, vector<string>& sources, vector<string>& targets) {
        int n = s.size();
        int k = indices.size();
        unordered_map<int,int> posToIdx;
        for (int i = 0; i < k; ++i) {
            posToIdx[indices[i]] = i;
        }
        string result;
        for (int i = 0; i < n; ) {
            auto it = posToIdx.find(i);
            if (it != posToIdx.end()) {
                int idx = it->second;
                const string& src = sources[idx];
                const string& tgt = targets[idx];
                if (i + (int)src.size() <= n && s.compare(i, src.size(), src) == 0) {
                    result += tgt;
                    i += src.size();
                    continue;
                }
            }
            result.push_back(s[i]);
            ++i;
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public String findReplaceString(String s, int[] indices, String[] sources, String[] targets) {
        int n = s.length();
        java.util.Map<Integer, Integer> map = new java.util.HashMap<>();
        for (int i = 0; i < indices.length; i++) {
            map.put(indices[i], i);
        }
        StringBuilder sb = new StringBuilder();
        int i = 0;
        while (i < n) {
            if (map.containsKey(i)) {
                int idx = map.get(i);
                String src = sources[idx];
                if (s.startsWith(src, i)) {
                    sb.append(targets[idx]);
                    i += src.length();
                    continue;
                }
            }
            sb.append(s.charAt(i));
            i++;
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        replace = {idx: (src, tgt) for idx, src, tgt in zip(indices, sources, targets)}
        i, n = 0, len(s)
        result = []
        while i < n:
            if i in replace:
                src, tgt = replace[i]
                if s.startswith(src, i):
                    result.append(tgt)
                    i += len(src)
                    continue
            result.append(s[i])
            i += 1
        return ''.join(result)
```

## Python3

```python
from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replace_map = {idx: (src, tgt) for idx, src, tgt in zip(indices, sources, targets)}
        i = 0
        n = len(s)
        result = []
        while i < n:
            if i in replace_map:
                src, tgt = replace_map[i]
                if s.startswith(src, i):
                    result.append(tgt)
                    i += len(src)
                    continue
            result.append(s[i])
            i += 1
        return ''.join(result)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* findReplaceString(char* s, int* indices, int indicesSize, char** sources, int sourcesSize, char** targets, int targetsSize) {
    int n = strlen(s);
    // map each position to operation index or -1
    int *opAtPos = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i) opAtPos[i] = -1;

    // store source lengths and target strings for valid operations
    int *srcLen = (int*)malloc(sizeof(int) * indicesSize);
    for (int i = 0; i < indicesSize; ++i) srcLen[i] = 0;

    for (int i = 0; i < indicesSize; ++i) {
        int idx = indices[i];
        const char *src = sources[i];
        int len = strlen(src);
        if (idx + len <= n && strncmp(s + idx, src, len) == 0) {
            opAtPos[idx] = i;
            srcLen[i] = len;
        }
    }

    // compute final length
    int totalLen = n;
    for (int i = 0; i < indicesSize; ++i) {
        if (srcLen[i] > 0) {
            totalLen += strlen(targets[i]) - srcLen[i];
        }
    }

    char *res = (char*)malloc(totalLen + 1);
    int pos = 0; // position in result
    for (int i = 0; i < n; ++i) {
        if (opAtPos[i] != -1) {
            int op = opAtPos[i];
            const char *tgt = targets[op];
            int tlen = strlen(tgt);
            memcpy(res + pos, tgt, tlen);
            pos += tlen;
            i += srcLen[op] - 1; // skip source characters
        } else {
            res[pos++] = s[i];
        }
    }
    res[pos] = '\0';

    free(opAtPos);
    free(srcLen);
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string FindReplaceString(string s, int[] indices, string[] sources, string[] targets)
    {
        int n = indices.Length;
        // Get order of operations by index ascending
        var order = new List<int>(n);
        for (int i = 0; i < n; i++) order.Add(i);
        order.Sort((a, b) => indices[a].CompareTo(indices[b]));

        var sb = new System.Text.StringBuilder();
        int pos = 0;

        foreach (var idx in order)
        {
            int start = indices[idx];
            // Append unchanged part before this operation
            if (pos < start)
            {
                sb.Append(s, pos, start - pos);
                pos = start;
            }

            string src = sources[idx];
            // Check if source matches at this position
            if (start + src.Length <= s.Length && s.Substring(start, src.Length) == src)
            {
                sb.Append(targets[idx]);
                pos = start + src.Length; // skip the source substring
            }
            else
            {
                // No replacement, keep original character(s) as they will be handled later
                // Since we didn't advance pos, continue to next operation
            }
        }

        // Append any remaining part of the original string
        if (pos < s.Length)
        {
            sb.Append(s, pos, s.Length - pos);
        }

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number[]} indices
 * @param {string[]} sources
 * @param {string[]} targets
 * @return {string}
 */
var findReplaceString = function(s, indices, sources, targets) {
    const n = s.length;
    const replaceMap = new Array(n).fill(null);
    
    for (let i = 0; i < indices.length; i++) {
        replaceMap[indices[i]] = { src: sources[i], tgt: targets[i] };
    }
    
    let result = '';
    let i = 0;
    while (i < n) {
        const info = replaceMap[i];
        if (info && s.substr(i, info.src.length) === info.src) {
            result += info.tgt;
            i += info.src.length;
        } else {
            result += s[i];
            i++;
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function findReplaceString(s: string, indices: number[], sources: string[], targets: string[]): string {
    const repl: { idx: number; src: string; tgt: string }[] = [];
    for (let i = 0; i < indices.length; i++) {
        repl.push({ idx: indices[i], src: sources[i], tgt: targets[i] });
    }
    repl.sort((a, b) => a.idx - b.idx);
    let result = '';
    let i = 0;
    for (const { idx, src, tgt } of repl) {
        while (i < idx) {
            result += s[i];
            i++;
        }
        if (s.slice(idx, idx + src.length) === src) {
            result += tgt;
            i = idx + src.length;
        }
    }
    while (i < s.length) {
        result += s[i];
        i++;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[] $indices
     * @param String[] $sources
     * @param String[] $targets
     * @return String
     */
    function findReplaceString($s, $indices, $sources, $targets) {
        $map = [];
        $k = count($indices);
        for ($i = 0; $i < $k; $i++) {
            $pos = $indices[$i];
            $map[$pos] = [$sources[$i], $targets[$i]];
        }

        $len = strlen($s);
        $result = '';
        $i = 0;
        while ($i < $len) {
            if (isset($map[$i])) {
                list($src, $tgt) = $map[$i];
                $srcLen = strlen($src);
                if (substr($s, $i, $srcLen) === $src) {
                    $result .= $tgt;
                    $i += $srcLen;
                    continue;
                }
            }
            $result .= $s[$i];
            $i++;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findReplaceString(_ s: String, _ indices: [Int], _ sources: [String], _ targets: [String]) -> String {
        let n = s.count
        var replaceMap = [Int:(String, String)]()
        for i in 0..<indices.count {
            replaceMap[indices[i]] = (sources[i], targets[i])
        }
        
        let chars = Array(s)
        var i = 0
        var result = ""
        
        while i < n {
            if let (src, tgt) = replaceMap[i] {
                if i + src.count <= n {
                    var matches = true
                    for (offset, ch) in src.enumerated() {
                        if chars[i + offset] != ch {
                            matches = false
                            break
                        }
                    }
                    if matches {
                        result += tgt
                        i += src.count
                        continue
                    }
                }
            }
            result.append(chars[i])
            i += 1
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findReplaceString(s: String, indices: IntArray, sources: Array<String>, targets: Array<String>): String {
        val map = HashMap<Int, Int>()
        for (i in indices.indices) {
            map[indices[i]] = i
        }
        val sb = StringBuilder()
        var i = 0
        while (i < s.length) {
            if (map.containsKey(i)) {
                val idx = map[i]!!
                val src = sources[idx]
                if (s.startsWith(src, i)) {
                    sb.append(targets[idx])
                    i += src.length
                    continue
                }
            }
            sb.append(s[i])
            i++
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String findReplaceString(String s, List<int> indices, List<String> sources, List<String> targets) {
    int n = indices.length;
    List<_Op> ops = [];
    for (int i = 0; i < n; i++) {
      ops.add(_Op(indices[i], sources[i], targets[i]));
    }
    ops.sort((a, b) => a.idx.compareTo(b.idx));

    StringBuffer sb = StringBuffer();
    int last = 0;
    for (var op in ops) {
      if (op.idx < last) continue; // safety for unexpected overlap
      sb.write(s.substring(last, op.idx));
      if (op.idx + op.source.length <= s.length &&
          s.substring(op.idx, op.idx + op.source.length) == op.source) {
        sb.write(op.target);
        last = op.idx + op.source.length;
      } else {
        // no replacement; keep original characters
        last = op.idx;
      }
    }
    sb.write(s.substring(last));
    return sb.toString();
  }
}

class _Op {
  int idx;
  String source;
  String target;
  _Op(this.idx, this.source, this.target);
}
```

## Golang

```go
import (
	"sort"
	"strings"
)

type operation struct {
	idx int
	src string
	tgt string
}

func findReplaceString(s string, indices []int, sources []string, targets []string) string {
	n := len(indices)
	ops := make([]operation, n)
	for i := 0; i < n; i++ {
		ops[i] = operation{indices[i], sources[i], targets[i]}
	}
	sort.Slice(ops, func(i, j int) bool { return ops[i].idx < ops[j].idx })

	var sb strings.Builder
	pos := 0
	for _, op := range ops {
		if pos > len(s) {
			break
		}
		// Append unchanged segment before current operation
		if pos <= op.idx {
			sb.WriteString(s[pos:op.idx])
			// Check if source matches at this index
			if strings.HasPrefix(s[op.idx:], op.src) {
				sb.WriteString(op.tgt)
				pos = op.idx + len(op.src)
			} else {
				// No replacement; keep original characters
				pos = op.idx
			}
		}
	}
	if pos < len(s) {
		sb.WriteString(s[pos:])
	}
	return sb.String()
}
```

## Ruby

```ruby
def find_replace_string(s, indices, sources, targets)
  replace_map = {}
  indices.each_with_index do |idx, i|
    src = sources[i]
    if s[idx, src.length] == src
      replace_map[idx] = [src, targets[i]]
    end
  end

  result = +""
  i = 0
  while i < s.length
    if replace_map.key?(i)
      src, tgt = replace_map[i]
      result << tgt
      i += src.length
    else
      result << s[i]
      i += 1
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def findReplaceString(s: String, indices: Array[Int], sources: Array[String], targets: Array[String]): String = {
        val ops = indices.indices.map(i => (indices(i), sources(i), targets(i))).sortBy(_._1)
        val sb = new StringBuilder
        var i = 0
        var opIdx = 0
        while (i < s.length) {
            if (opIdx < ops.length && i == ops(opIdx)._1) {
                val src = ops(opIdx)._2
                val tgt = ops(opIdx)._3
                if (s.startsWith(src, i)) {
                    sb.append(tgt)
                    i += src.length
                } else {
                    sb.append(s.charAt(i))
                    i += 1
                }
                opIdx += 1
            } else {
                sb.append(s.charAt(i))
                i += 1
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn find_replace_string(s: String, indices: Vec<i32>, sources: Vec<String>, targets: Vec<String>) -> String {
        let mut map: HashMap<usize, (String, String)> = HashMap::new();
        for i in 0..indices.len() {
            map.insert(indices[i] as usize, (sources[i].clone(), targets[i].clone()));
        }

        let n = s.len();
        let mut result = String::with_capacity(n);
        let mut i = 0usize;
        while i < n {
            if let Some((src, tgt)) = map.get(&i) {
                if s[i..].starts_with(src.as_str()) {
                    result.push_str(tgt);
                    i += src.len();
                    continue;
                }
            }
            // copy original character
            result.push(s.as_bytes()[i] as char);
            i += 1;
        }

        result
    }
}
```

## Racket

```racket
(define/contract (find-replace-string s indices sources targets)
  (-> string? (listof exact-integer?) (listof string?) (listof string?) string?)
  (let* ((ops (map list indices sources targets))
         (sorted-ops (sort ops (lambda (a b) (< (first a) (first b)))))
         (n (string-length s)))
    (let loop ((remaining sorted-ops)
               (pos 0)
               (parts '()))
      (if (null? remaining)
          (apply string-append (reverse (cons (substring s pos n) parts)))
          (let* ((op (car remaining))
                 (idx (first op))
                 (src (second op))
                 (tgt (third op))
                 (len-src (string-length src))
                 (pre (substring s pos idx)))
            (if (and (<= (+ idx len-src) n)
                     (string=? (substring s idx (+ idx len-src)) src))
                (loop (cdr remaining)
                      (+ idx len-src)
                      (cons tgt (cons pre parts)))
                (loop (cdr remaining)
                      idx
                      (cons pre parts))))))))
```

## Erlang

```erlang
-module(solution).
-export([find_replace_string/4]).
-spec find_replace_string(S :: unicode:unicode_binary(), Indices :: [integer()], Sources :: [unicode:unicode_binary()], Targets :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
find_replace_string(S, Indices, Sources, Targets) ->
    Ops = lists:zipwith(fun(I, Src, Tgt) -> {I, {Src, Tgt}} end, Indices, Sources, Targets),
    Map = maps:from_list(Ops),
    Len = byte_size(S),
    replace(0, Len, S, Map, []).

replace(Pos, Len, _S, _Map, Acc) when Pos >= Len ->
    iolist_to_binary(lists:reverse(Acc));
replace(Pos, Len, S, Map, Acc) ->
    case maps:find(Pos, Map) of
        {ok, {Source, Target}} ->
            SrcLen = byte_size(Source),
            if SrcLen =< (Len - Pos) andalso binary:part(S, Pos, SrcLen) == Source ->
                    replace(Pos + SrcLen, Len, S, Map, [Target | Acc]);
               true ->
                    Char = binary:part(S, Pos, 1),
                    replace(Pos + 1, Len, S, Map, [Char | Acc])
            end;
        error ->
            Char = binary:part(S, Pos, 1),
            replace(Pos + 1, Len, S, Map, [Char | Acc])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_replace_string(String.t(), [integer()], [String.t()], [String.t()]) :: String.t()
  def find_replace_string(s, indices, sources, targets) do
    map =
      Enum.reduce(0..(length(indices) - 1), %{}, fn i, acc ->
        idx = Enum.at(indices, i)
        src = Enum.at(sources, i)
        tgt = Enum.at(targets, i)

        if String.slice(s, idx, String.length(src)) == src do
          Map.put(acc, idx, {src, tgt})
        else
          acc
        end
      end)

    sorted_indices = Map.keys(map) |> Enum.sort()
    build(s, 0, sorted_indices, map, [])
  end

  defp build(s, pos, _sorted_idx, _map, acc) when pos >= byte_size(s) do
    Enum.reverse(acc) |> Enum.join()
  end

  defp build(s, pos, sorted_idx, map, acc) do
    case sorted_idx do
      [head | tail] when head == pos ->
        {src, tgt} = Map.get(map, head)
        build(s, pos + byte_size(src), tail, map, [tgt | acc])

      _ ->
        char = String.slice(s, pos, 1)
        build(s, pos + 1, sorted_idx, map, [char | acc])
    end
  end
end
```
