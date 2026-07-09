# 1598. Crawler Log Folder

## Cpp

```cpp
class Solution {
public:
    int minOperations(std::vector<std::string>& logs) {
        int depth = 0;
        for (const auto& op : logs) {
            if (op == "../") {
                if (depth > 0) --depth;
            } else if (op != "./") {
                ++depth; // any other operation is moving into a child folder
            }
        }
        return depth;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(String[] logs) {
        int depth = 0;
        for (String log : logs) {
            if (log.equals("../")) {
                if (depth > 0) depth--;
            } else if (!log.equals("./")) {
                depth++;
            }
        }
        return depth;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        depth = 0
        for op in logs:
            if op == "../":
                if depth > 0:
                    depth -= 1
            elif op == "./":
                continue
            else:
                depth += 1
        return depth
```

## Python3

```python
from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for op in logs:
            if op == "../":
                if depth > 0:
                    depth -= 1
            elif op != "./":
                depth += 1
        return depth
```

## C

```c
#include <string.h>

int minOperations(char** logs, int logsSize) {
    int depth = 0;
    for (int i = 0; i < logsSize; ++i) {
        if (strcmp(logs[i], "../") == 0) {
            if (depth > 0) depth--;
        } else if (strcmp(logs[i], "./") != 0) {
            depth++;
        }
    }
    return depth;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinOperations(string[] logs)
    {
        int depth = 0;
        foreach (var log in logs)
        {
            if (log == "../")
            {
                if (depth > 0) depth--;
            }
            else if (log != "./")
            {
                // any other operation is moving into a child folder
                depth++;
            }
        }
        return depth;
    }
}
```

## Javascript

```javascript
var minOperations = function(logs) {
    let depth = 0;
    for (const op of logs) {
        if (op === "../") {
            if (depth > 0) depth--;
        } else if (op !== "./") {
            depth++;
        }
    }
    return depth;
};
```

## Typescript

```typescript
function minOperations(logs: string[]): number {
    let depth = 0;
    for (const op of logs) {
        if (op === "../") {
            if (depth > 0) depth--;
        } else if (op !== "./") {
            depth++;
        }
    }
    return depth;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $logs
     * @return Integer
     */
    function minOperations($logs) {
        $depth = 0;
        foreach ($logs as $op) {
            if ($op === "../") {
                if ($depth > 0) {
                    $depth--;
                }
            } elseif ($op !== "./") {
                // any other operation is moving into a child folder
                $depth++;
            }
        }
        return $depth;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ logs: [String]) -> Int {
        var depth = 0
        for log in logs {
            if log == "../" {
                if depth > 0 { depth -= 1 }
            } else if log != "./" {
                depth += 1
            }
        }
        return depth
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(logs: Array<String>): Int {
        var depth = 0
        for (log in logs) {
            when (log) {
                "../" -> if (depth > 0) depth--
                "./" -> {}
                else -> depth++
            }
        }
        return depth
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<String> logs) {
    int depth = 0;
    for (var op in logs) {
      if (op == "../") {
        if (depth > 0) depth--;
      } else if (op != "./") {
        // any other operation is moving into a child folder
        depth++;
      }
    }
    return depth;
  }
}
```

## Golang

```go
func minOperations(logs []string) int {
    depth := 0
    for _, op := range logs {
        switch op {
        case "../":
            if depth > 0 {
                depth--
            }
        case "./":
            // stay in the same folder, do nothing
        default:
            depth++
        }
    }
    return depth
}
```

## Ruby

```ruby
def min_operations(logs)
  depth = 0
  logs.each do |log|
    if log == "../"
      depth -= 1 if depth > 0
    elsif log != "./"
      depth += 1
    end
  end
  depth
end
```

## Scala

```scala
object Solution {
    def minOperations(logs: Array[String]): Int = {
        var depth = 0
        for (log <- logs) {
            if (log == "../") {
                if (depth > 0) depth -= 1
            } else if (log != "./") {
                // any other operation is moving into a child folder
                depth += 1
            }
        }
        depth
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(logs: Vec<String>) -> i32 {
        let mut depth = 0;
        for op in logs.iter() {
            if op == "../" {
                if depth > 0 {
                    depth -= 1;
                }
            } else if op != "./" {
                // any other operation is entering a child folder
                depth += 1;
            }
        }
        depth as i32
    }
}
```

## Racket

```racket
(define/contract (min-operations logs)
  (-> (listof string?) exact-integer?)
  (let loop ((lst logs) (depth 0))
    (if (null? lst)
        depth
        (let* ((op (car lst))
               (new-depth (cond [(string=? op "../") (max 0 (- depth 1))]
                                [(string=? op "./") depth]
                                [else (+ depth 1)])))
          (loop (cdr lst) new-depth)))))
```

## Erlang

```erlang
-spec min_operations([binary()]) -> integer().
min_operations(Logs) ->
    lists:foldl(
        fun(Log, Depth) ->
            case Log of
                <<"../">> -> erlang:max(Depth - 1, 0);
                <<"./">> -> Depth;
                _ -> Depth + 1
            end
        end,
        0,
        Logs
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(logs :: [String.t]) :: integer
  def min_operations(logs) do
    Enum.reduce(logs, 0, fn log, depth ->
      cond do
        log == "../" -> if depth > 0, do: depth - 1, else: 0
        log == "./" -> depth
        true -> depth + 1
      end
    end)
  end
end
```
