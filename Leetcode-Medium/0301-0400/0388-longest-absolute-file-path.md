# 0388. Longest Absolute File Path

## Cpp

```cpp
class Solution {
public:
    int lengthLongestPath(string input) {
        vector<int> pathLen(256, 0); // depth up to 255 is enough for constraints
        int maxLen = 0;
        size_t i = 0;
        while (i < input.size()) {
            // Determine depth by counting '\t'
            int depth = 0;
            while (i < input.size() && input[i] == '\t') {
                ++depth;
                ++i;
            }
            // Extract the name until next '\n' or end
            size_t start = i;
            while (i < input.size() && input[i] != '\n') ++i;
            string name = input.substr(start, i - start);
            // Move past newline if present
            if (i < input.size() && input[i] == '\n') ++i;
            
            if (name.find('.') != string::npos) {
                // It's a file
                int curLen = pathLen[depth] + name.length();
                maxLen = max(maxLen, curLen);
            } else {
                // Directory: add length plus '/' separator for deeper levels
                pathLen[depth + 1] = pathLen[depth] + name.length() + 1;
            }
        }
        return maxLen;
    }
};
```

## Java

```java
class Solution {
    public int lengthLongestPath(String input) {
        String[] parts = input.split("\n");
        int[] pathLen = new int[parts.length + 1];
        int maxLen = 0;
        for (String part : parts) {
            int depth = 0;
            while (depth < part.length() && part.charAt(depth) == '\t') {
                depth++;
            }
            String name = part.substring(depth);
            if (name.contains(".")) {
                int curLen = pathLen[depth] + name.length();
                if (curLen > maxLen) {
                    maxLen = curLen;
                }
            } else {
                pathLen[depth + 1] = pathLen[depth] + name.length() + 1; // add '/' separator
            }
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        max_len = 0
        # pathlen[depth] stores total length up to this depth (including a trailing '/')
        pathlen = {-1: 0}
        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                cur_len = pathlen[depth - 1] + len(name)
                if cur_len > max_len:
                    max_len = cur_len
            else:
                # add 1 for the '/' that will separate this directory from its children
                pathlen[depth] = pathlen[depth - 1] + len(name) + 1
        return max_len
```

## Python3

```python
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        # depth -> total length up to this depth (excluding trailing '/')
        path_len = {0: 0}
        for line in input.split('\n'):
            # count leading tabs to determine depth
            depth = 0
            while depth < len(line) and line[depth] == '\t':
                depth += 1
            name = line[depth:]
            if '.' in name:  # it's a file
                cur_len = path_len[depth] + len(name)
                if cur_len > max_len:
                    max_len = cur_len
            else:  # directory
                # add length of this dir plus '/' for next level
                path_len[depth + 1] = path_len[depth] + len(name) + 1
        return max_len
```

## C

```c
#include <string.h>
#include <stdlib.h>

int lengthLongestPath(char* input) {
    int maxlen = 0;
    int n = strlen(input);
    int *depthLen = (int *)calloc(n + 2, sizeof(int));
    char *p = input;

    while (*p) {
        int depth = 0;
        while (*p == '\t') {
            depth++;
            p++;
        }

        const char *start = p;
        int isFile = 0;
        while (*p && *p != '\n') {
            if (*p == '.') isFile = 1;
            p++;
        }
        int len = (int)(p - start);

        if (isFile) {
            int total = depthLen[depth] + len;
            if (total > maxlen) maxlen = total;
        } else {
            depthLen[depth + 1] = depthLen[depth] + len + 1; // add '/' length
        }

        if (*p == '\n') p++;
    }

    free(depthLen);
    return maxlen;
}
```

## Csharp

```csharp
public class Solution
{
    public int LengthLongestPath(string input)
    {
        if (string.IsNullOrEmpty(input)) return 0;
        int maxLen = 0;
        // depth -> cumulative length up to that depth (including trailing '/')
        int[] pathLen = new int[input.Length + 1];
        string[] lines = input.Split('\n');
        foreach (var line in lines)
        {
            int depth = 0;
            while (depth < line.Length && line[depth] == '\t')
                depth++;
            string name = line.Substring(depth);
            if (name.Contains('.'))
            {
                int totalLen = pathLen[depth] + name.Length;
                if (totalLen > maxLen) maxLen = totalLen;
            }
            else
            {
                // store length up to this directory plus a '/' for children
                pathLen[depth + 1] = pathLen[depth] + name.Length + 1;
            }
        }
        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} input
 * @return {number}
 */
var lengthLongestPath = function(input) {
    const lines = input.split('\n');
    const depthLen = [0];
    let maxLen = 0;
    for (const line of lines) {
        let depth = 0;
        while (depth < line.length && line[depth] === '\t') depth++;
        const name = line.slice(depth);
        if (name.includes('.')) {
            const total = depthLen[depth] + name.length;
            if (total > maxLen) maxLen = total;
        } else {
            depthLen[depth + 1] = depthLen[depth] + name.length + 1; // add '/' length
        }
    }
    return maxLen;
};
```

## Typescript

```typescript
function lengthLongestPath(input: string): number {
    const lines = input.split('\n');
    const depthLen: number[] = [];
    let maxLen = 0;
    for (const line of lines) {
        let depth = 0;
        while (depth < line.length && line[depth] === '\t') depth++;
        const name = line.slice(depth);
        const curLen = (depth > 0 ? depthLen[depth - 1] + 1 : 0) + name.length; // add '/' if not root
        if (name.includes('.')) {
            maxLen = Math.max(maxLen, curLen);
        } else {
            depthLen[depth] = curLen;
        }
    }
    return maxLen;
}
```

## Php

```php
class Solution {
    /**
     * @param String $input
     * @return Integer
     */
    function lengthLongestPath($input) {
        $lines = explode("\n", $input);
        $stack = [];
        $maxLen = 0;
        foreach ($lines as $line) {
            $depth = 0;
            $lenLine = strlen($line);
            while ($depth < $lenLine && $line[$depth] === "\t") {
                $depth++;
            }
            $name = substr($line, $depth);
            $lenName = strlen($name);
            if (strpos($name, '.') !== false) { // file
                $parentLen = $depth > 0 ? $stack[$depth - 1] : 0;
                $total = $parentLen + $lenName;
                if ($total > $maxLen) {
                    $maxLen = $total;
                }
            } else { // directory
                $parentLen = $depth > 0 ? $stack[$depth - 1] : 0;
                $stack[$depth] = $parentLen + $lenName + 1; // add '/' separator
            }
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func lengthLongestPath(_ input: String) -> Int {
        var maxLen = 0
        let lines = input.split(separator: "\n", omittingEmptySubsequences: false)
        var dp = [Int](repeating: 0, count: lines.count + 1)
        for part in lines {
            let line = String(part)
            var depth = 0
            var idx = line.startIndex
            while idx < line.endIndex && line[idx] == "\t" {
                depth += 1
                idx = line.index(after: idx)
            }
            let name = String(line[idx...])
            let curLen: Int
            if depth == 0 {
                curLen = name.count
            } else {
                curLen = dp[depth - 1] + 1 + name.count // add '/' separator
            }
            if name.contains(".") {
                if curLen > maxLen { maxLen = curLen }
            } else {
                dp[depth] = curLen
            }
        }
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lengthLongestPath(input: String): Int {
        var maxLen = 0
        val pathLen = IntArray(input.length + 1)
        for (line in input.split('\n')) {
            var depth = 0
            while (depth < line.length && line[depth] == '\t') {
                depth++
            }
            val name = line.substring(depth)
            if (name.contains('.')) {
                maxLen = kotlin.math.max(maxLen, pathLen[depth] + name.length)
            } else {
                pathLen[depth + 1] = pathLen[depth] + name.length + 1
            }
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int lengthLongestPath(String input) {
    // Stack-like array where stack[depth] holds the total length up to that depth.
    List<int> stack = List.filled(input.length + 1, 0);
    int maxLen = 0;

    for (String line in input.split('\n')) {
      int depth = 0;
      while (depth < line.length && line.codeUnitAt(depth) == 9) { // '\t' ASCII 9
        depth++;
      }
      String name = line.substring(depth);
      if (name.contains('.')) {
        // It's a file. Total length is length up to its parent + name length.
        int curLen = stack[depth] + name.length;
        if (curLen > maxLen) maxLen = curLen;
      } else {
        // Directory: add '/' separator (+1).
        stack[depth + 1] = stack[depth] + name.length + 1;
      }
    }

    return maxLen;
  }
}
```

## Golang

```go
import "strings"

func lengthLongestPath(input string) int {
	maxLen := 0
	lines := strings.Split(input, "\n")
	cumLen := make([]int, len(lines)+1)
	for _, line := range lines {
		depth := 0
		for depth < len(line) && line[depth] == '\t' {
			depth++
		}
		name := line[depth:]
		if strings.Contains(name, ".") {
			curLen := cumLen[depth] + len(name)
			if curLen > maxLen {
				maxLen = curLen
			}
		} else {
			cumLen[depth+1] = cumLen[depth] + len(name) + 1 // add '/' separator
		}
	}
	return maxLen
}
```

## Ruby

```ruby
def length_longest_path(input)
  max_len = 0
  depth_len = Hash.new(0)
  depth_len[-1] = 0
  input.split("\n").each do |line|
    depth = line[/\A\t*/].size
    name = line[depth..-1]
    if name.include?('.')
      cur_len = depth_len[depth - 1] + name.length
      max_len = cur_len if cur_len > max_len
    else
      depth_len[depth] = depth_len[depth - 1] + name.length + 1
    end
  end
  max_len
end
```

## Scala

```scala
object Solution {
    def lengthLongestPath(input: String): Int = {
        val lines = input.split("\n")
        val depthLen = new Array[Int](lines.length + 1)
        var maxLen = 0
        for (line <- lines) {
            var i = 0
            while (i < line.length && line.charAt(i) == '\t') i += 1
            val depth = i
            val name = line.substring(i)
            if (name.contains('.')) {
                val curLen = depthLen(depth) + name.length
                if (curLen > maxLen) maxLen = curLen
            } else {
                depthLen(depth + 1) = depthLen(depth) + name.length + 1
            }
        }
        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn length_longest_path(input: String) -> i32 {
        let mut max_len: usize = 0;
        let mut path_len: Vec<usize> = Vec::new(); // cumulative lengths per depth

        for line in input.split('\n') {
            // count leading tabs to determine depth
            let bytes = line.as_bytes();
            let mut depth: usize = 0;
            while depth < bytes.len() && bytes[depth] == b'\t' {
                depth += 1;
            }
            let name = &line[depth..];
            let name_len = name.len();

            if name.contains('.') {
                // it's a file
                let total = if depth == 0 {
                    name_len
                } else {
                    path_len[depth - 1] + 1 + name_len // add '/' separator
                };
                if total > max_len {
                    max_len = total;
                }
            } else {
                // it's a directory
                let cur_len = if depth == 0 {
                    name_len
                } else {
                    path_len[depth - 1] + 1 + name_len
                };
                if path_len.len() <= depth {
                    path_len.push(cur_len);
                } else {
                    path_len[depth] = cur_len;
                }
            }
        }

        max_len as i32
    }
}
```

## Racket

```racket
(define/contract (length-longest-path input)
  (-> string? exact-integer?)
  (let* ((lines (regexp-split #rx"\n" input))
         (lens (make-vector (+ (string-length input) 1) 0))
         (maxlen 0))
    (for ([line lines])
      (let* ((len-line (string-length line))
             (depth
               (let loop ((i 0))
                 (if (and (< i len-line)
                          (char=? (string-ref line i) #\tab))
                     (loop (+ i 1))
                     i)))
             (name (substring line depth))
             (is-file (regexp-match #rx"\\." name))
             (prev (if (= depth 0) 0 (vector-ref lens (- depth 1))))
             (cur (+ prev (if (> depth 0) 1 0) (string-length name))))
        (if is-file
            (when (> cur maxlen) (set! maxlen cur))
            (vector-set! lens depth cur))))
    maxlen))
```

## Erlang

```erlang
-module(solution).
-export([length_longest_path/1]).

-spec length_longest_path(Input :: unicode:unicode_binary()) -> integer().
length_longest_path(Input) ->
    Lines = binary:split(Input, <<"\n">>, [global]),
    process(Lines, #{}, 0).

process([], _LenMap, Max) ->
    Max;
process([Line | Rest], LenMap, Max) ->
    Depth = count_tabs(Line, 0),
    Name = binary:part(Line, {Depth, byte_size(Line) - Depth}),
    NameLen = byte_size(Name),
    ParentLen =
        case Depth of
            0 -> 0;
            _ -> maps:get(Depth - 1, LenMap, 0)
        end,
    Total = ParentLen + (if Depth > 0 -> 1; true -> 0 end) + NameLen,
    IsFile = binary:match(Name, <<".">>) =/= nomatch,
    case IsFile of
        true ->
            NewMax = max(Max, Total),
            process(Rest, LenMap, NewMax);
        false ->
            NewMap = maps:put(Depth, Total, LenMap),
            process(Rest, NewMap, Max)
    end.

count_tabs(<<>>, Acc) -> Acc;
count_tabs(<<"\t", Rest/binary>>, Acc) -> count_tabs(Rest, Acc + 1);
count_tabs(_, Acc) -> Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec length_longest_path(input :: String.t()) :: integer
  def length_longest_path(input) do
    lines = String.split(input, "\n", trim: false)

    {max_len, _} =
      Enum.reduce(lines, {0, %{}}, fn line, {max_len, depths} ->
        {depth, name} = parse_line(line, 0)

        if String.contains?(name, ".") do
          parent_len = Map.get(depths, depth - 1, 0)
          total_len = parent_len + String.length(name)
          {if total_len > max_len, do: total_len, else: max_len}, depths
        else
          parent_len = Map.get(depths, depth - 1, 0)
          cur_len = parent_len + String.length(name) + 1
          {max_len, Map.put(depths, depth, cur_len)}
        end
      end)

    max_len
  end

  defp parse_line(<<?\t, rest::binary>>, depth), do: parse_line(rest, depth + 1)
  defp parse_line(line, depth), do: {depth, line}
end
```
