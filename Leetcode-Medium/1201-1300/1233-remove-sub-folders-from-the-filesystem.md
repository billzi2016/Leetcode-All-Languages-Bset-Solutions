# 1233. Remove Sub-Folders from the Filesystem

## Cpp

```cpp
class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        sort(folder.begin(), folder.end());
        vector<string> result;
        for (const string& f : folder) {
            if (!result.empty()) {
                const string& last = result.back();
                // Check if current folder is a subfolder of the last added folder
                if (f.size() > last.size() && 
                    f.compare(0, last.size(), last) == 0 && 
                    f[last.size()] == '/') {
                    continue;
                }
            }
            result.push_back(f);
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> removeSubfolders(String[] folder) {
        Arrays.sort(folder);
        List<String> result = new ArrayList<>();
        String prev = "";
        for (String f : folder) {
            if (prev.isEmpty() || !f.startsWith(prev + "/")) {
                result.add(f);
                prev = f;
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        res = []
        for f in folder:
            if not res or not f.startswith(res[-1] + '/'):
                res.append(f)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        last = ""
        for f in folder:
            if not last or not f.startswith(last + "/"):
                result.append(f)
                last = f
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>

/* Comparator for qsort */
static int cmpStr(const void *a, const void *b) {
    const char *sa = *(const char **)a;
    const char *sb = *(const char **)b;
    return strcmp(sa, sb);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** removeSubfolders(char** folder, int folderSize, int* returnSize) {
    if (folderSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    /* Sort folders lexicographically */
    qsort(folder, folderSize, sizeof(char *), cmpStr);

    char **result = (char **)malloc(sizeof(char *) * folderSize);
    int cnt = 0;

    for (int i = 0; i < folderSize; ++i) {
        if (cnt == 0) {
            result[cnt++] = folder[i];
            continue;
        }
        const char *prev = result[cnt - 1];
        size_t len = strlen(prev);
        /* Check if current folder is a subfolder of prev */
        if (strncmp(folder[i], prev, len) == 0 && folder[i][len] == '/') {
            continue;   // it's a subfolder, skip
        }
        result[cnt++] = folder[i];
    }

    *returnSize = cnt;
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> RemoveSubfolders(string[] folder) {
        Array.Sort(folder, StringComparer.Ordinal);
        List<string> result = new List<string>();
        foreach (string f in folder) {
            if (result.Count == 0) {
                result.Add(f);
                continue;
            }
            string last = result[result.Count - 1];
            if (!f.StartsWith(last + "/")) {
                result.Add(f);
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} folder
 * @return {string[]}
 */
var removeSubfolders = function(folder) {
    folder.sort();
    const result = [];
    for (const f of folder) {
        if (!result.length) {
            result.push(f);
            continue;
        }
        const prev = result[result.length - 1];
        // If current folder does not start with previous folder + '/', it's not a subfolder
        if (!f.startsWith(prev + '/')) {
            result.push(f);
        }
    }
    return result;
};
```

## Typescript

```typescript
function removeSubfolders(folder: string[]): string[] {
    folder.sort();
    const result: string[] = [];
    for (const path of folder) {
        if (result.length === 0) {
            result.push(path);
        } else {
            const last = result[result.length - 1];
            if (!path.startsWith(last + '/')) {
                result.push(path);
            }
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $folder
     * @return String[]
     */
    function removeSubfolders($folder) {
        sort($folder, SORT_STRING);
        $result = [];
        foreach ($folder as $path) {
            if (empty($result)) {
                $result[] = $path;
                continue;
            }
            $last = end($result);
            $prefix = $last . '/';
            if (strpos($path, $prefix) === 0) {
                // sub-folder, skip
                continue;
            }
            $result[] = $path;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func removeSubfolders(_ folder: [String]) -> [String] {
        let sortedFolders = folder.sorted()
        var result: [String] = []
        for path in sortedFolders {
            if let last = result.last, path.hasPrefix(last + "/") {
                continue
            }
            result.append(path)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeSubfolders(folder: Array<String>): List<String> {
        val sorted = folder.sorted()
        val result = mutableListOf<String>()
        for (path in sorted) {
            if (result.isEmpty() || !path.startsWith(result.last() + "/")) {
                result.add(path)
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> removeSubfolders(List<String> folder) {
    folder.sort();
    List<String> result = [];
    for (var f in folder) {
      if (result.isEmpty || !f.startsWith(result.last + '/')) {
        result.add(f);
      }
    }
    return result;
  }
}
```

## Golang

```go
import (
	"sort"
	"strings"
)

func removeSubfolders(folder []string) []string {
	sort.Strings(folder)
	var res []string
	prev := ""
	for _, f := range folder {
		if prev == "" || !strings.HasPrefix(f, prev+"/") {
			res = append(res, f)
			prev = f
		}
	}
	return res
}
```

## Ruby

```ruby
def remove_subfolders(folder)
  folder.sort!
  result = []
  folder.each do |path|
    if result.empty? || !path.start_with?(result[-1] + '/')
      result << path
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def removeSubfolders(folder: Array[String]): List[String] = {
        val sorted = folder.sorted
        val result = scala.collection.mutable.ListBuffer[String]()
        for (path <- sorted) {
            if (result.isEmpty || !path.startsWith(result.last + "/")) {
                result += path
            }
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_subfolders(folder: Vec<String>) -> Vec<String> {
        let mut folders = folder;
        folders.sort();
        let mut result: Vec<String> = Vec::new();

        for f in folders.into_iter() {
            if let Some(last) = result.last() {
                // Build the prefix of the last folder with a trailing slash
                let prefix = format!("{}/", last);
                if f.starts_with(&prefix) {
                    continue; // it's a subfolder, skip it
                }
            }
            result.push(f);
        }

        result
    }
}
```

## Racket

```racket
#lang racket

(require racket/contract
         racket/string)

(define/contract (remove-subfolders folder)
  (-> (listof string?) (listof string?))
  (let ((sorted (sort folder string<?)))
    (let loop ((lst sorted) (prev #f) (acc '()))
      (cond [(null? lst) (reverse acc)]
            [else
             (define cur (car lst))
             (if (and prev (string-prefix? (string-append prev "/") cur))
                 (loop (cdr lst) prev acc)
                 (loop (cdr lst) cur (cons cur acc)))]))))
```

## Erlang

```erlang
-spec remove_subfolders(Folder :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
remove_subfolders(Folder) ->
    Sorted = lists:sort(Folder),
    filter(Sorted, []).

filter([], Acc) -> lists:reverse(Acc);
filter([H|T], []) ->
    filter(T, [H]);
filter([H|T], [Last|Rest]=Acc) ->
    case is_subfolder(Last, H) of
        true  -> filter(T, Acc);
        false -> filter(T, [H|Acc])
    end.

is_subfolder(Parent, Path) ->
    PL = byte_size(Parent),
    case byte_size(Path) > PL of
        true ->
            Prefix = binary:part(Path, {0, PL}),
            if Prefix == Parent,
               binary:at(Path, PL) =:= $/ -> true;
               true -> false
            end;
        false -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_subfolders(folder :: [String.t]) :: [String.t]
  def remove_subfolders(folder) do
    sorted = Enum.sort(folder)

    {result_rev, _} =
      Enum.reduce(sorted, {[], nil}, fn path, {acc, last} ->
        if last && String.starts_with?(path, last <> "/") do
          {acc, last}
        else
          {[path | acc], path}
        end
      end)

    Enum.reverse(result_rev)
  end
end
```
