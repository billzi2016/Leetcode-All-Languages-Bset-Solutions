# 0071. Simplify Path

## Cpp

```cpp
class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stk;
        int n = path.size();
        string cur;
        for (int i = 0; i <= n; ++i) {
            if (i == n || path[i] == '/') {
                if (!cur.empty()) {
                    if (cur == "..") {
                        if (!stk.empty()) stk.pop_back();
                    } else if (cur != ".") {
                        stk.push_back(cur);
                    }
                    cur.clear();
                }
            } else {
                cur += path[i];
            }
        }
        string res = "/";
        for (size_t i = 0; i < stk.size(); ++i) {
            res += stk[i];
            if (i + 1 != stk.size()) res += '/';
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String simplifyPath(String path) {
        java.util.Deque<String> stack = new java.util.ArrayDeque<>();
        for (String part : path.split("/")) {
            if (part.isEmpty() || part.equals(".")) {
                continue;
            }
            if (part.equals("..")) {
                if (!stack.isEmpty()) {
                    stack.pollLast();
                }
            } else {
                stack.addLast(part);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (String dir : stack) {
            sb.append('/').append(dir);
        }
        return sb.length() > 0 ? sb.toString() : "/";
    }
}
```

## Python

```python
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for part in path.split('/'):
            if not part or part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)
```

## Python3

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split('/'):
            if not part or part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* simplifyPath(char* path) {
    int len = strlen(path);
    // Maximum possible components is len (each char separated by '/')
    char **stack = (char **)malloc((len + 1) * sizeof(char *));
    int top = 0;

    for (int i = 0; i < len;) {
        // Skip consecutive slashes
        while (i < len && path[i] == '/') i++;
        if (i >= len) break;
        int start = i;
        while (i < len && path[i] != '/') i++;
        int segLen = i - start;

        // Extract segment
        if (segLen == 0) continue; // shouldn't happen

        // Check for "." or ".."
        if (segLen == 1 && path[start] == '.') {
            continue;
        } else if (segLen == 2 && path[start] == '.' && path[start + 1] == '.') {
            if (top > 0) {
                free(stack[--top]);
            }
            continue;
        } else {
            // Normal directory name
            char *dir = (char *)malloc(segLen + 1);
            memcpy(dir, path + start, segLen);
            dir[segLen] = '\0';
            stack[top++] = dir;
        }
    }

    if (top == 0) {
        free(stack);
        char *res = (char *)malloc(2);
        res[0] = '/';
        res[1] = '\0';
        return res;
    }

    // Compute total length
    int totalLen = 1; // leading '/'
    for (int i = 0; i < top; ++i) {
        totalLen += strlen(stack[i]) + 1; // component and '/' separator
    }
    totalLen--; // remove trailing '/'

    char *result = (char *)malloc(totalLen + 1);
    int pos = 0;
    result[pos++] = '/';
    for (int i = 0; i < top; ++i) {
        int l = strlen(stack[i]);
        memcpy(result + pos, stack[i], l);
        pos += l;
        if (i != top - 1) {
            result[pos++] = '/';
        }
        free(stack[i]); // clean up component
    }
    result[pos] = '\0';
    free(stack);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string SimplifyPath(string path)
    {
        var dirs = new System.Collections.Generic.List<string>();
        foreach (var part in path.Split('/'))
        {
            if (part.Length == 0 || part == ".")
                continue;
            if (part == "..")
            {
                if (dirs.Count > 0)
                    dirs.RemoveAt(dirs.Count - 1);
            }
            else
            {
                dirs.Add(part);
            }
        }

        var sb = new System.Text.StringBuilder();
        foreach (var dir in dirs)
        {
            sb.Append('/');
            sb.Append(dir);
        }

        return sb.Length == 0 ? "/" : sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    const stack = [];
    for (const dir of path.split('/')) {
        if (!dir || dir === '.') continue;
        if (dir === '..') {
            if (stack.length) stack.pop();
        } else {
            stack.push(dir);
        }
    }
    return '/' + stack.join('/');
};
```

## Typescript

```typescript
function simplifyPath(path: string): string {
    const stack: string[] = [];
    for (const part of path.split('/')) {
        if (!part || part === '.') continue;
        if (part === '..') {
            if (stack.length) stack.pop();
        } else {
            stack.push(part);
        }
    }
    return '/' + stack.join('/');
}
```

## Php

```php
class Solution {

    /**
     * @param String $path
     * @return String
     */
    function simplifyPath($path) {
        $parts = explode('/', $path);
        $stack = [];

        foreach ($parts as $part) {
            if ($part === '' || $part === '.') {
                continue;
            }
            if ($part === '..') {
                if (!empty($stack)) {
                    array_pop($stack);
                }
            } else {
                $stack[] = $part;
            }
        }

        return '/' . implode('/', $stack);
    }
}
```

## Swift

```swift
class Solution {
    func simplifyPath(_ path: String) -> String {
        var stack = [String]()
        let parts = path.split(separator: "/", omittingEmptySubsequences: true)
        for part in parts {
            if part == "." { continue }
            else if part == ".." {
                if !stack.isEmpty { stack.removeLast() }
            } else {
                stack.append(String(part))
            }
        }
        return "/" + stack.joined(separator: "/")
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun simplifyPath(path: String): String {
        val stack = ArrayDeque<String>()
        var i = 0
        val n = path.length
        while (i < n) {
            // skip consecutive slashes
            while (i < n && path[i] == '/') i++
            if (i >= n) break
            val start = i
            while (i < n && path[i] != '/') i++
            val token = path.substring(start, i)
            when (token) {
                "", "." -> { /* ignore */ }
                ".." -> stack.pollLast()
                else -> stack.addLast(token)
            }
        }
        return if (stack.isEmpty()) "/" else "/" + stack.joinToString("/")
    }
}
```

## Dart

```dart
class Solution {
  String simplifyPath(String path) {
    List<String> stack = [];
    for (String part in path.split('/')) {
      if (part.isEmpty || part == '.') continue;
      if (part == '..') {
        if (stack.isNotEmpty) stack.removeLast();
      } else {
        stack.add(part);
      }
    }
    return '/' + stack.join('/');
  }
}
```

## Golang

```go
import "strings"

func simplifyPath(path string) string {
	parts := strings.Split(path, "/")
	stack := []string{}
	for _, p := range parts {
		if p == "" || p == "." {
			continue
		}
		if p == ".." {
			if len(stack) > 0 {
				stack = stack[:len(stack)-1]
			}
		} else {
			stack = append(stack, p)
		}
	}
	return "/" + strings.Join(stack, "/")
}
```

## Ruby

```ruby
def simplify_path(path)
  stack = []
  path.split('/').each do |part|
    next if part.empty? || part == '.'
    if part == '..'
      stack.pop unless stack.empty?
    else
      stack << part
    end
  end
  '/' + stack.join('/')
end
```

## Scala

```scala
object Solution {
    def simplifyPath(path: String): String = {
        val stack = new scala.collection.mutable.ArrayDeque[String]()
        for (part <- path.split("/")) {
            part match {
                case "" | "." => // ignore
                case ".." =>
                    if (stack.nonEmpty) stack.removeLast()
                case _ => stack.append(part)
            }
        }
        "/" + stack.mkString("/")
    }
}
```

## Rust

```rust
impl Solution {
    pub fn simplify_path(path: String) -> String {
        let mut stack: Vec<&str> = Vec::new();
        for part in path.split('/') {
            match part {
                "" | "." => continue,
                ".." => { stack.pop(); },
                _ => stack.push(part),
            }
        }
        if stack.is_empty() {
            "/".to_string()
        } else {
            let mut result = String::from("/");
            result.push_str(&stack.join("/"));
            result
        }
    }
}
```

## Racket

```racket
#lang racket
(require racket/string)

(define/contract (simplify-path path)
  (-> string? string?)
  (let* ((parts (string-split path "/" #:trim-empty? #t))
         (stack '()))
    (for ([p parts])
      (cond
        [(or (string=? p ".") (string=? p "")) (void)]
        [(string=? p "..")
         (when (not (null? stack))
           (set! stack (cdr stack)))]
        [else
         (set! stack (cons p stack))]))
    (define rev (reverse stack))
    (string-append "/" (string-join rev "/"))))
```

## Erlang

```erlang
-spec simplify_path(Path :: unicode:unicode_binary()) -> unicode:unicode_binary().
simplify_path(Path) ->
    Tokens = binary:split(Path, <<"/">>, [global]),
    Stack = lists:foldl(
        fun(Token, Acc) ->
            case Token of
                <<>> -> Acc;
                <<".">> -> Acc;
                <<"..">> ->
                    case Acc of
                        [] -> [];
                        [_|Rest] -> Rest
                    end;
                _ -> [Token | Acc]
            end
        end,
        [],
        Tokens),
    Rev = lists:reverse(Stack),
    lists:foldl(
        fun(Seg, Acc) -> <<Acc/binary, "/", Seg/binary>> end,
        <<"/">>,
        Rev).
```

## Elixir

```elixir
defmodule Solution do
  @spec simplify_path(path :: String.t()) :: String.t()
  def simplify_path(path) do
    stack =
      path
      |> String.split("/", trim: false)
      |> Enum.reduce([], fn
        "" , acc -> acc
        "." , acc -> acc
        "..", [] -> []
        "..", [_ | rest] -> rest
        segment, acc -> [segment | acc]
      end)

    "/" <> (stack |> Enum.reverse() |> Enum.join("/"))
  end
end
```
