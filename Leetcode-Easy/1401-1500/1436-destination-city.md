# 1436. Destination City

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_set<string> hasOutgoing;
        for (const auto& p : paths) {
            hasOutgoing.insert(p[0]);
        }
        for (const auto& p : paths) {
            if (!hasOutgoing.count(p[1])) return p[1];
        }
        return "";
    }
};
```

## Java

```java
class Solution {
    public String destCity(List<List<String>> paths) {
        java.util.HashSet<String> outgoing = new java.util.HashSet<>();
        for (List<String> path : paths) {
            outgoing.add(path.get(0));
        }
        for (List<String> path : paths) {
            String destination = path.get(1);
            if (!outgoing.contains(destination)) {
                return destination;
            }
        }
        return "";
    }
}
```

## Python

```python
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        outgoing = {a for a, _ in paths}
        for _, b in paths:
            if b not in outgoing:
                return b
```

## Python3

```python
class Solution:
    def destCity(self, paths):
        outgoing = {a for a, _ in paths}
        for _, b in paths:
            if b not in outgoing:
                return b
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* destCity(char*** paths, int pathsSize, int* pathsColSize) {
    for (int i = 0; i < pathsSize; ++i) {
        char *candidate = paths[i][1];
        int found = 0;
        for (int j = 0; j < pathsSize; ++j) {
            if (strcmp(paths[j][0], candidate) == 0) {
                found = 1;
                break;
            }
        }
        if (!found) {
            char *res = (char *)malloc(strlen(candidate) + 1);
            strcpy(res, candidate);
            return res;
        }
    }
    return NULL; // Should never reach here as per problem guarantee
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public string DestCity(IList<IList<string>> paths) {
        var outgoing = new HashSet<string>();
        foreach (var path in paths) {
            outgoing.Add(path[0]);
        }
        foreach (var path in paths) {
            if (!outgoing.Contains(path[1])) {
                return path[1];
            }
        }
        return "";
    }
}
```

## Javascript

```javascript
/**
 * @param {string[][]} paths
 * @return {string}
 */
var destCity = function(paths) {
    const hasOutgoing = new Set();
    for (const [src] of paths) {
        hasOutgoing.add(src);
    }
    for (const [, dst] of paths) {
        if (!hasOutgoing.has(dst)) {
            return dst;
        }
    }
    // Should never reach here as per problem guarantee
    return "";
};
```

## Typescript

```typescript
function destCity(paths: string[][]): string {
    const outgoing = new Set<string>();
    for (const [from] of paths) {
        outgoing.add(from);
    }
    for (const [, to] of paths) {
        if (!outgoing.has(to)) return to;
    }
    return "";
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $paths
     * @return String
     */
    function destCity($paths) {
        $outgoing = [];
        foreach ($paths as $path) {
            $outgoing[$path[0]] = true;
        }
        foreach ($paths as $path) {
            if (!isset($outgoing[$path[1]])) {
                return $path[1];
            }
        }
        return "";
    }
}
```

## Swift

```swift
class Solution {
    func destCity(_ paths: [[String]]) -> String {
        var outgoing = Set<String>()
        for path in paths {
            if let from = path.first {
                outgoing.insert(from)
            }
        }
        for path in paths {
            if path.count == 2 {
                let to = path[1]
                if !outgoing.contains(to) {
                    return to
                }
            }
        }
        return ""
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun destCity(paths: List<List<String>>): String {
        val outgoing = HashSet<String>()
        for (p in paths) {
            outgoing.add(p[0])
        }
        for (p in paths) {
            val dest = p[1]
            if (!outgoing.contains(dest)) return dest
        }
        return ""
    }
}
```

## Dart

```dart
class Solution {
  String destCity(List<List<String>> paths) {
    final Set<String> outgoing = {};
    for (var path in paths) {
      outgoing.add(path[0]);
    }
    for (var path in paths) {
      if (!outgoing.contains(path[1])) {
        return path[1];
      }
    }
    return "";
  }
}
```

## Golang

```go
func destCity(paths [][]string) string {
    outgoing := make(map[string]struct{})
    for _, p := range paths {
        outgoing[p[0]] = struct{}{}
    }
    for _, p := range paths {
        if _, ok := outgoing[p[1]]; !ok {
            return p[1]
        }
    }
    return ""
}
```

## Ruby

```ruby
require 'set'

def dest_city(paths)
  outgoing = Set.new
  paths.each { |a, _| outgoing.add(a) }
  paths.each do |_, b|
    return b unless outgoing.include?(b)
  end
end
```

## Scala

```scala
object Solution {
  def destCity(paths: List[List[String]]): String = {
    val outgoing = scala.collection.mutable.HashSet[String]()
    for (p <- paths) {
      outgoing += p.head
    }
    for (p <- paths) {
      val dest = p(1)
      if (!outgoing.contains(dest)) return dest
    }
    ""
  }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn dest_city(paths: Vec<Vec<String>>) -> String {
        let mut starts: HashSet<String> = HashSet::new();
        for p in &paths {
            // each path has exactly two cities
            starts.insert(p[0].clone());
        }
        for p in &paths {
            if !starts.contains(&p[1]) {
                return p[1].clone();
            }
        }
        String::new()
    }
}
```

## Racket

```racket
(define/contract (dest-city paths)
  (-> (listof (listof string?)) string?)
  (let ((starts (make-hash)))
    (for-each (lambda (p) (hash-set! starts (first p) #t)) paths)
    (let loop ((remaining paths))
      (cond [(null? remaining)
             (error "Destination city not found")]
            [else
             (define dest (second (car remaining)))
             (if (hash-has-key? starts dest)
                 (loop (cdr remaining))
                 dest)]))))
```

## Erlang

```erlang
-spec dest_city(Paths :: [[unicode:unicode_binary()]]) -> unicode:unicode_binary().
dest_city(Paths) ->
    Starts = lists:foldl(
        fun([From,_], Acc) -> maps:put(From, true, Acc) end,
        #{},
        Paths
    ),
    case lists:filter(fun([_,To]) -> not maps:is_key(To, Starts) end, Paths) of
        [[_,Dest]|_] -> Dest;
        [] -> <<>>
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec dest_city(paths :: [[String.t]]) :: String.t
  def dest_city(paths) do
    starts = Enum.reduce(paths, MapSet.new(), fn [a, _b], acc -> MapSet.put(acc, a) end)

    Enum.find_value(paths, fn [_a, b] ->
      unless MapSet.member?(starts, b), do: b
    end)
  end
end
```
