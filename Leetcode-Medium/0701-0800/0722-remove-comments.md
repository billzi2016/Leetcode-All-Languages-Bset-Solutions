# 0722. Remove Comments

## Cpp

```cpp
class Solution {
public:
    vector<string> removeComments(vector<string>& source) {
        vector<string> ans;
        bool inBlock = false;
        string newline;
        for (const string& line : source) {
            int n = line.size();
            int i = 0;
            if (!inBlock) newline.clear();
            while (i < n) {
                if (!inBlock && i + 1 < n && line[i] == '/' && line[i + 1] == '*') {
                    inBlock = true;
                    i += 2;
                } else if (inBlock && i + 1 < n && line[i] == '*' && line[i + 1] == '/') {
                    inBlock = false;
                    i += 2;
                } else if (!inBlock && i + 1 < n && line[i] == '/' && line[i + 1] == '/') {
                    break; // ignore rest of the line
                } else {
                    if (!inBlock) newline.push_back(line[i]);
                    ++i;
                }
            }
            if (!inBlock && !newline.empty()) {
                ans.push_back(newline);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<String> removeComments(String[] source) {
        java.util.List<String> ans = new java.util.ArrayList<>();
        boolean inBlock = false;
        StringBuilder sb = new StringBuilder();
        for (String line : source) {
            int i = 0;
            char[] chars = line.toCharArray();
            if (!inBlock) {
                sb.setLength(0);
            }
            while (i < chars.length) {
                if (!inBlock && i + 1 < chars.length && chars[i] == '/' && chars[i + 1] == '*') {
                    inBlock = true;
                    i += 2;
                } else if (inBlock && i + 1 < chars.length && chars[i] == '*' && chars[i + 1] == '/') {
                    inBlock = false;
                    i += 2;
                } else if (!inBlock && i + 1 < chars.length && chars[i] == '/' && chars[i + 1] == '/') {
                    break;
                } else {
                    if (!inBlock) {
                        sb.append(chars[i]);
                    }
                    i++;
                }
            }
            if (!inBlock && sb.length() > 0) {
                ans.add(sb.toString());
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        in_block = False
        ans = []
        for line in source:
            i = 0
            if not in_block:
                newline = []
            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                    in_block = True
                    i += 2
                elif in_block and i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                    in_block = False
                    i += 2
                elif not in_block and i + 1 < len(line) and line[i] == '/' and line[i+1] == '/':
                    break
                else:
                    if not in_block:
                        newline.append(line[i])
                    i += 1
            if not in_block and newline:
                ans.append(''.join(newline))
        return ans
```

## Python3

```python
class Solution:
    def removeComments(self, source):
        ans = []
        in_block = False
        newline = []
        for line in source:
            i = 0
            if not in_block:
                newline = []
            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                    in_block = True
                    i += 1
                elif in_block and i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                    in_block = False
                    i += 1
                elif not in_block and i + 1 < len(line) and line[i] == '/' and line[i+1] == '/':
                    break
                elif not in_block:
                    newline.append(line[i])
                i += 1
            if not in_block and newline:
                ans.append(''.join(newline))
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** removeComments(char** source, int sourceSize, int* returnSize) {
    char **ans = (char **)malloc(sourceSize * sizeof(char *));
    int ansCount = 0;

    // buffer for the current line being built
    int bufCap = 128;
    char *buf = (char *)malloc(bufCap);
    int bufLen = 0;

    bool inBlock = false;

    for (int i = 0; i < sourceSize; ++i) {
        char *line = source[i];
        int n = strlen(line);
        int j = 0;
        while (j < n) {
            if (!inBlock) {
                // check for line comment
                if (j + 1 < n && line[j] == '/' && line[j + 1] == '/') {
                    break; // ignore rest of the line
                }
                // check for block comment start
                if (j + 1 < n && line[j] == '/' && line[j + 1] == '*') {
                    inBlock = true;
                    j += 2;
                    continue;
                }
                // regular character
                if (bufLen + 1 >= bufCap) {
                    bufCap *= 2;
                    buf = (char *)realloc(buf, bufCap);
                }
                buf[bufLen++] = line[j];
                ++j;
            } else { // inside block comment
                // check for block comment end
                if (j + 1 < n && line[j] == '*' && line[j + 1] == '/') {
                    inBlock = false;
                    j += 2;
                } else {
                    ++j; // skip character inside block comment
                }
            }
        }

        // at the end of each source line, if we are not inside a block comment,
        // and we have accumulated characters, finalize the current line.
        if (!inBlock && bufLen > 0) {
            char *outLine = (char *)malloc(bufLen + 1);
            memcpy(outLine, buf, bufLen);
            outLine[bufLen] = '\0';
            ans[ansCount++] = outLine;
            bufLen = 0; // reset buffer for next line
        }
    }

    free(buf);
    *returnSize = ansCount;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public IList<string> RemoveComments(string[] source) {
        var result = new List<string>();
        bool inBlock = false;
        var sb = new System.Text.StringBuilder();

        foreach (var line in source) {
            int i = 0;
            int n = line.Length;
            if (!inBlock) sb.Clear();

            while (i < n) {
                if (!inBlock && i + 1 < n && line[i] == '/' && line[i + 1] == '*') {
                    inBlock = true;
                    i += 2;
                } else if (inBlock && i + 1 < n && line[i] == '*' && line[i + 1] == '/') {
                    inBlock = false;
                    i += 2;
                } else if (!inBlock && i + 1 < n && line[i] == '/' && line[i + 1] == '/') {
                    break; // ignore rest of the line
                } else {
                    if (!inBlock) sb.Append(line[i]);
                    i++;
                }
            }

            if (!inBlock && sb.Length > 0) {
                result.Add(sb.ToString());
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} source
 * @return {string[]}
 */
var removeComments = function(source) {
    const result = [];
    let inBlock = false;
    let newline = [];

    for (const line of source) {
        let i = 0;
        if (!inBlock) newline = [];

        while (i < line.length) {
            if (!inBlock && i + 1 < line.length && line[i] === '/' && line[i + 1] === '*') {
                inBlock = true;
                i += 2;
            } else if (inBlock && i + 1 < line.length && line[i] === '*' && line[i + 1] === '/') {
                inBlock = false;
                i += 2;
            } else if (!inBlock && i + 1 < line.length && line[i] === '/' && line[i + 1] === '/') {
                break; // ignore rest of the line
            } else {
                if (!inBlock) newline.push(line[i]);
                i++;
            }
        }

        if (!inBlock && newline.length > 0) {
            result.push(newline.join(''));
        }
    }

    return result;
};
```

## Typescript

```typescript
function removeComments(source: string[]): string[] {
    const result: string[] = [];
    let inBlock = false;
    let newline: string[] = [];

    for (const line of source) {
        let i = 0;
        if (!inBlock) newline = [];

        while (i < line.length) {
            if (!inBlock && i + 1 < line.length && line[i] === '/' && line[i + 1] === '*') {
                inBlock = true;
                i += 2;
            } else if (inBlock && i + 1 < line.length && line[i] === '*' && line[i + 1] === '/') {
                inBlock = false;
                i += 2;
            } else if (!inBlock && i + 1 < line.length && line[i] === '/' && line[i + 1] === '/') {
                break;
            } else {
                if (!inBlock) newline.push(line[i]);
                i++;
            }
        }

        if (!inBlock && newline.length > 0) {
            result.push(newline.join(''));
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $source
     * @return String[]
     */
    function removeComments($source) {
        $inBlock = false;
        $result = [];

        foreach ($source as $line) {
            $i = 0;
            $len = strlen($line);
            if (!$inBlock) {
                $newline = '';
            }

            while ($i < $len) {
                // start of block comment
                if (!$inBlock && $i + 1 < $len && $line[$i] === '/' && $line[$i + 1] === '*') {
                    $inBlock = true;
                    $i += 2;
                    continue;
                }
                // end of block comment
                if ($inBlock && $i + 1 < $len && $line[$i] === '*' && $line[$i + 1] === '/') {
                    $inBlock = false;
                    $i += 2;
                    continue;
                }
                // line comment
                if (!$inBlock && $i + 1 < $len && $line[$i] === '/' && $line[$i + 1] === '/') {
                    break; // ignore rest of the line
                }

                // regular character
                if (!$inBlock) {
                    $newline .= $line[$i];
                }
                $i++;
            }

            if (!$inBlock && isset($newline) && $newline !== '') {
                $result[] = $newline;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func removeComments(_ source: [String]) -> [String] {
        var inBlock = false
        var result = [String]()
        var currentLine = ""
        
        for line in source {
            let chars = Array(line)
            var i = 0
            if !inBlock { currentLine = "" }
            
            while i < chars.count {
                if !inBlock && i + 1 < chars.count && chars[i] == "/" && chars[i + 1] == "*" {
                    inBlock = true
                    i += 2
                } else if inBlock && i + 1 < chars.count && chars[i] == "*" && chars[i + 1] == "/" {
                    inBlock = false
                    i += 2
                } else if !inBlock && i + 1 < chars.count && chars[i] == "/" && chars[i + 1] == "/" {
                    break
                } else {
                    if !inBlock {
                        currentLine.append(chars[i])
                    }
                    i += 1
                }
            }
            
            if !inBlock && !currentLine.isEmpty {
                result.append(currentLine)
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeComments(source: Array<String>): List<String> {
        val result = mutableListOf<String>()
        var inBlock = false
        var sb = StringBuilder()
        for (line in source) {
            var i = 0
            if (!inBlock) sb = StringBuilder()
            while (i < line.length) {
                if (!inBlock && i + 1 < line.length && line[i] == '/' && line[i + 1] == '*') {
                    inBlock = true
                    i += 2
                } else if (inBlock && i + 1 < line.length && line[i] == '*' && line[i + 1] == '/') {
                    inBlock = false
                    i += 2
                } else if (!inBlock && i + 1 < line.length && line[i] == '/' && line[i + 1] == '/') {
                    break
                } else {
                    if (!inBlock) sb.append(line[i])
                    i++
                }
            }
            if (!inBlock && sb.isNotEmpty()) {
                result.add(sb.toString())
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> removeComments(List<String> source) {
    bool inBlock = false;
    List<String> result = [];
    StringBuffer? buffer;

    for (String line in source) {
      int i = 0;
      if (!inBlock) {
        buffer = StringBuffer();
      }
      while (i < line.length) {
        if (!inBlock && i + 1 < line.length && line[i] == '/' && line[i + 1] == '*') {
          inBlock = true;
          i += 2;
        } else if (inBlock && i + 1 < line.length && line[i] == '*' && line[i + 1] == '/') {
          inBlock = false;
          i += 2;
        } else if (!inBlock && i + 1 < line.length && line[i] == '/' && line[i + 1] == '/') {
          break; // ignore rest of the line
        } else {
          if (!inBlock) {
            buffer!.write(line[i]);
          }
          i++;
        }
      }
      if (!inBlock && buffer != null && buffer.isNotEmpty) {
        result.add(buffer.toString());
      }
    }

    return result;
  }
}
```

## Golang

```go
package main

import (
	"strings"
)

func removeComments(source []string) []string {
	var ans []string
	inBlock := false
	var sb strings.Builder

	for _, line := range source {
		i := 0
		if !inBlock {
			sb.Reset()
		}
		for i < len(line) {
			if !inBlock && i+1 < len(line) && line[i] == '/' && line[i+1] == '*' {
				inBlock = true
				i += 2
				continue
			}
			if inBlock && i+1 < len(line) && line[i] == '*' && line[i+1] == '/' {
				inBlock = false
				i += 2
				continue
			}
			if !inBlock && i+1 < len(line) && line[i] == '/' && line[i+1] == '/' {
				break
			}
			if !inBlock {
				sb.WriteByte(line[i])
			}
			i++
		}
		if !inBlock && sb.Len() > 0 {
			ans = append(ans, sb.String())
		}
	}
	return ans
}
```

## Ruby

```ruby
def remove_comments(source)
  in_block = false
  result = []
  current_line = ''
  source.each do |line|
    i = 0
    current_line = '' unless in_block
    while i < line.length
      if !in_block && i + 1 < line.length && line.getbyte(i) == ?/ && line.getbyte(i + 1) == ?*
        in_block = true
        i += 1
      elsif in_block && i + 1 < line.length && line.getbyte(i) == ?* && line.getbyte(i + 1) == ?/
        in_block = false
        i += 1
      elsif !in_block && i + 1 < line.length && line.getbyte(i) == ?/ && line.getbyte(i + 1) == ?/
        break
      elsif !in_block
        current_line << line[i]
      end
      i += 1
    end
    result << current_line unless in_block || current_line.empty?
  end
  result
end
```

## Scala

```scala
object Solution {
  def removeComments(source: Array[String]): List[String] = {
    val result = scala.collection.mutable.ListBuffer[String]()
    var inBlock = false
    val sb = new StringBuilder

    for (line <- source) {
      var i = 0
      if (!inBlock) sb.clear()
      while (i < line.length) {
        if (!inBlock && i + 1 < line.length && line.charAt(i) == '/' && line.charAt(i + 1) == '*') {
          inBlock = true
          i += 2
        } else if (inBlock && i + 1 < line.length && line.charAt(i) == '*' && line.charAt(i + 1) == '/') {
          inBlock = false
          i += 2
        } else if (!inBlock && i + 1 < line.length && line.charAt(i) == '/' && line.charAt(i + 1) == '/') {
          // line comment, ignore rest of the line
          i = line.length
        } else {
          if (!inBlock) sb.append(line.charAt(i))
          i += 1
        }
      }
      if (!inBlock && sb.nonEmpty) {
        result += sb.toString()
      }
    }

    result.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_comments(source: Vec<String>) -> Vec<String> {
        let mut ans = Vec::new();
        let mut in_block = false;
        let mut newline = String::new();

        for line in source.iter() {
            let bytes = line.as_bytes();
            let mut i = 0;
            if !in_block {
                newline.clear();
            }
            while i < bytes.len() {
                if !in_block && i + 1 < bytes.len() && bytes[i] == b'/' && bytes[i + 1] == b'*' {
                    in_block = true;
                    i += 2;
                } else if in_block && i + 1 < bytes.len() && bytes[i] == b'*' && bytes[i + 1] == b'/' {
                    in_block = false;
                    i += 2;
                } else if !in_block && i + 1 < bytes.len() && bytes[i] == b'/' && bytes[i + 1] == b'/' {
                    break;
                } else if !in_block {
                    newline.push(bytes[i] as char);
                    i += 1;
                } else {
                    // inside block comment, skip character
                    i += 1;
                }
            }
            if !in_block && !newline.is_empty() {
                ans.push(newline.clone());
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (remove-comments source)
  (-> (listof string?) (listof string?))
  (let loop ((lines source) (in-block? #f) (out '()))
    (if (null? lines)
        (reverse out)
        (let* ((line (car lines))
               (len (string-length line)))
          (call-with-values
              (lambda ()
                (letrec ((process
                          (lambda (i acc in-block)
                            (cond
                              [(>= i len)
                               (if (and (not in-block) (not (null? acc)))
                                   (values in-block (list->string (reverse acc)))
                                   (values in-block #f))]
                              [else
                               (let ((ch (string-ref line i))
                                     (next (if (< (+ i 1) len)
                                               (string-ref line (+ i 1))
                                               #\null)))
                                 (cond
                                   [(and (not in-block) (char=? ch #\/) (char=? next #\*))
                                    (process (+ i 2) acc #t)]
                                   [(and in-block (char=? ch #\*) (char=? next #\/))
                                    (process (+ i 2) acc #f)]
                                   [(and (not in-block) (char=? ch #\/) (char=? next #\/))
                                    (if (null? acc)
                                        (values in-block #f)
                                        (values in-block (list->string (reverse acc))))]
                                   [else
                                    (if in-block
                                        (process (+ i 1) acc in-block)
                                        (process (+ i 1) (cons ch acc) in-block))])))])))
                  (process 0 '() in-block?))
              (lambda (new-in-block maybe-line)
                (loop (cdr lines) new-in-block
                      (if maybe-line (cons maybe-line out) out)))))))))
```

## Erlang

```erlang
-module(solution).
-export([remove_comments/1]).

-spec remove_comments(Source :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
remove_comments(Source) ->
    process(Source, false, [], []).

process([], _InBlock, _CurrAcc, ResAcc) ->
    lists:reverse(ResAcc);
process([Bin|Rest], InBlock, CurrAcc, ResAcc) ->
    Line = binary_to_list(Bin),
    {NewInBlock, NewCurrAcc} = parse_line(Line, InBlock, CurrAcc),
    case NewInBlock of
        false ->
            case NewCurrAcc of
                [] ->
                    process(Rest, false, [], ResAcc);
                _ ->
                    NewResAcc = [list_to_binary(lists:reverse(NewCurrAcc)) | ResAcc],
                    process(Rest, false, [], NewResAcc)
            end;
        true ->
            process(Rest, true, NewCurrAcc, ResAcc)
    end.

parse_line([], InBlock, Acc) ->
    {InBlock, Acc};
parse_line([$/,$/|_Rest], false, Acc) ->
    {false, Acc};
parse_line([$/,$*|Rest], false, Acc) ->
    parse_line(Rest, true, Acc);
parse_line([$/,$*|Rest], true, Acc) ->
    parse_line(Rest, true, Acc);
parse_line([$*, $/ | Rest], true, Acc) ->
    parse_line(Rest, false, Acc);
parse_line([Char|Rest], false, Acc) ->
    parse_line(Rest, false, [Char|Acc]);
parse_line([_Char|Rest], true, Acc) ->
    parse_line(Rest, true, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_comments(source :: [String.t]) :: [String.t]
  def remove_comments(source) do
    {rev_result, _} =
      Enum.reduce(source, {[], false}, fn line, {out_rev, in_block} ->
        {buf, new_in_block} = process_line(line, in_block)

        if not new_in_block and buf != [] do
          {[IO.iodata_to_binary(buf) | out_rev], new_in_block}
        else
          {out_rev, new_in_block}
        end
      end)

    Enum.reverse(rev_result)
  end

  defp process_line(line, in_block) do
    do_process(line, in_block, [])
  end

  # End of binary
  defp do_process(<<>>, in_block, acc) do
    {Enum.reverse(acc), in_block}
  end

  # Start block comment when not already inside one
  defp do_process(<<"/", "*", rest::binary>>, false, acc) do
    do_process(rest, true, acc)
  end

  # End block comment when inside one
  defp do_process(<<"*", "/", rest::binary>>, true, acc) do
    do_process(rest, false, acc)
  end

  # Line comment start when not in a block comment
  defp do_process(<<"/", "/", _rest::binary>>, false, acc) do
    {Enum.reverse(acc), false}
  end

  # Regular character when not inside a block comment
  defp do_process(<<c, rest::binary>>, false, acc) do
    do_process(rest, false, [<<c>> | acc])
  end

  # Inside a block comment, skip current character
  defp do_process(<<_c, rest::binary>>, true, acc) do
    do_process(rest, true, acc)
  end
end
```
