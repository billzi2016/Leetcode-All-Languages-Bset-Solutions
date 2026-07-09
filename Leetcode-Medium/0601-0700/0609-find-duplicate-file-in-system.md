# 0609. Find Duplicate File in System

## Cpp

```cpp
class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        unordered_map<string, vector<string>> contentMap;
        for (const string& entry : paths) {
            size_t spacePos = entry.find(' ');
            string dir = entry.substr(0, spacePos);
            size_t idx = spacePos + 1;
            while (idx < entry.size()) {
                size_t nextSpace = entry.find(' ', idx);
                string fileInfo = entry.substr(idx, nextSpace - idx);
                
                size_t leftParen = fileInfo.find('(');
                string filename = fileInfo.substr(0, leftParen);
                string content = fileInfo.substr(leftParen + 1, fileInfo.size() - leftParen - 2); // exclude ')'
                
                string fullPath = dir + '/' + filename;
                contentMap[content].push_back(fullPath);
                
                if (nextSpace == string::npos) break;
                idx = nextSpace + 1;
            }
        }
        
        vector<vector<string>> result;
        for (auto& kv : contentMap) {
            if (kv.second.size() > 1) {
                result.push_back(std::move(kv.second));
            }
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        Map<String, List<String>> contentMap = new HashMap<>();
        for (String entry : paths) {
            String[] parts = entry.split(" ");
            String dir = parts[0];
            for (int i = 1; i < parts.length; i++) {
                String fileInfo = parts[i];
                int idx = fileInfo.indexOf('(');
                String fileName = fileInfo.substring(0, idx);
                String content = fileInfo.substring(idx + 1, fileInfo.length() - 1); // exclude ')'
                String fullPath = dir + "/" + fileName;
                contentMap.computeIfAbsent(content, k -> new ArrayList<>()).add(fullPath);
            }
        }

        List<List<String>> result = new ArrayList<>();
        for (List<String> list : contentMap.values()) {
            if (list.size() > 1) {
                result.add(list);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        content_map = {}
        for entry in paths:
            parts = entry.split(' ')
            dir_path = parts[0]
            for file_info in parts[1:]:
                i = file_info.find('(')
                name = file_info[:i]
                content = file_info[i+1:-1]  # strip parentheses
                full_path = dir_path + '/' + name
                if content not in content_map:
                    content_map[content] = []
                content_map[content].append(full_path)
        return [files for files in content_map.values() if len(files) > 1]
```

## Python3

```python
from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)
        for entry in paths:
            parts = entry.split(' ')
            dir_path = parts[0]
            for file_info in parts[1:]:
                idx = file_info.find('(')
                filename = file_info[:idx]
                content = file_info[idx+1:-1]  # strip parentheses
                full_path = f"{dir_path}/{filename}"
                content_map[content].append(full_path)
        return [files for files in content_map.values() if len(files) > 1]
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct {
    char *content;
    char *fullPath;
} File;

static int file_cmp(const void *a, const void *b) {
    const File *fa = (const File *)a;
    const File *fb = (const File *)b;
    return strcmp(fa->content, fb->content);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** findDuplicate(char** paths, int pathsSize, int* returnSize, int** returnColumnSizes) {
    if (pathsSize == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    // Dynamic array for files
    int cap = 1024;
    int fileCount = 0;
    File *files = (File *)malloc(cap * sizeof(File));

    for (int i = 0; i < pathsSize; ++i) {
        char *lineCopy = strdup(paths[i]);          // mutable copy for strtok
        char *dir = strtok(lineCopy, " ");           // directory part

        char *token;
        while ((token = strtok(NULL, " ")) != NULL) {
            // token format: filename(content)
            char *lp = strchr(token, '(');
            char *rp = strrchr(token, ')');
            if (!lp || !rp || lp > rp) continue;     // malformed, skip

            int nameLen = lp - token;
            int contentLen = rp - lp - 1;

            char *filename = (char *)malloc(nameLen + 1);
            memcpy(filename, token, nameLen);
            filename[nameLen] = '\0';

            char *content = (char *)malloc(contentLen + 1);
            memcpy(content, lp + 1, contentLen);
            content[contentLen] = '\0';

            int pathLen = strlen(dir) + 1 + nameLen + 1;
            char *fullPath = (char *)malloc(pathLen);
            snprintf(fullPath, pathLen, "%s/%s", dir, filename);

            free(filename); // no longer needed

            if (fileCount == cap) {
                cap <<= 1;
                files = (File *)realloc(files, cap * sizeof(File));
            }
            files[fileCount].content = content;
            files[fileCount].fullPath = fullPath;
            ++fileCount;
        }
        free(lineCopy);
    }

    if (fileCount == 0) {
        free(files);
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    qsort(files, fileCount, sizeof(File), file_cmp);

    // First pass: count groups
    int groupCnt = 0;
    for (int i = 0; i < fileCount;) {
        int j = i + 1;
        while (j < fileCount && strcmp(files[i].content, files[j].content) == 0)
            ++j;
        if (j - i > 1)
            ++groupCnt;
        i = j;
    }

    if (groupCnt == 0) {
        // clean up
        for (int i = 0; i < fileCount; ++i) {
            free(files[i].content);
            free(files[i].fullPath);
        }
        free(files);
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    char ***res = (char ***)malloc(groupCnt * sizeof(char **));
    int *colSizes = (int *)malloc(groupCnt * sizeof(int));

    int idx = 0;
    for (int i = 0; i < fileCount;) {
        int j = i + 1;
        while (j < fileCount && strcmp(files[i].content, files[j].content) == 0)
            ++j;
        int sz = j - i;
        if (sz > 1) {
            colSizes[idx] = sz;
            res[idx] = (char **)malloc(sz * sizeof(char *));
            for (int k = 0; k < sz; ++k) {
                res[idx][k] = files[i + k].fullPath; // transfer ownership
            }
            ++idx;
        } else {
            // no duplicate, free its fullPath
            free(files[i].fullPath);
        }
        // free content strings (no longer needed)
        for (int k = i; k < j; ++k) {
            free(files[k].content);
        }
        i = j;
    }

    free(files);

    *returnSize = groupCnt;
    *returnColumnSizes = colSizes;
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<string>> FindDuplicate(string[] paths) {
        var contentMap = new Dictionary<string, List<string>>();
        foreach (var entry in paths) {
            var parts = entry.Split(' ', StringSplitOptions.RemoveEmptyEntries);
            if (parts.Length < 2) continue;
            string dir = parts[0];
            for (int i = 1; i < parts.Length; i++) {
                string fileInfo = parts[i];
                int leftParen = fileInfo.IndexOf('(');
                int rightParen = fileInfo.LastIndexOf(')');
                if (leftParen == -1 || rightParen == -1) continue;
                string fileName = fileInfo.Substring(0, leftParen);
                string content = fileInfo.Substring(leftParen + 1, rightParen - leftParen - 1);
                string fullPath = dir + "/" + fileName;
                if (!contentMap.TryGetValue(content, out var list)) {
                    list = new List<string>();
                    contentMap[content] = list;
                }
                list.Add(fullPath);
            }
        }

        var result = new List<IList<string>>();
        foreach (var kvp in contentMap) {
            if (kvp.Value.Count > 1) {
                result.Add(kvp.Value);
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} paths
 * @return {string[][]}
 */
var findDuplicate = function(paths) {
    const contentMap = new Map();
    
    for (const entry of paths) {
        // split by space: first part is directory, rest are files
        const parts = entry.split(' ');
        const dir = parts[0];
        for (let i = 1; i < parts.length; ++i) {
            const fileInfo = parts[i];
            const leftParenIdx = fileInfo.indexOf('(');
            const rightParenIdx = fileInfo.lastIndexOf(')');
            const filename = fileInfo.substring(0, leftParenIdx);
            const content = fileInfo.substring(leftParenIdx + 1, rightParenIdx);
            const fullPath = dir + '/' + filename;
            
            if (!contentMap.has(content)) {
                contentMap.set(content, []);
            }
            contentMap.get(content).push(fullPath);
        }
    }
    
    const result = [];
    for (const pathsList of contentMap.values()) {
        if (pathsList.length > 1) {
            result.push(pathsList);
        }
    }
    return result;
};
```

## Typescript

```typescript
function findDuplicate(paths: string[]): string[][] {
    const contentMap = new Map<string, string[]>();
    for (const line of paths) {
        const parts = line.split(' ');
        const dir = parts[0];
        for (let i = 1; i < parts.length; i++) {
            const fileInfo = parts[i];
            const leftParen = fileInfo.indexOf('(');
            const name = fileInfo.substring(0, leftParen);
            const content = fileInfo.substring(leftParen + 1, fileInfo.length - 1); // exclude ')'
            const fullPath = `${dir}/${name}`;
            if (!contentMap.has(content)) {
                contentMap.set(content, [fullPath]);
            } else {
                contentMap.get(content)!.push(fullPath);
            }
        }
    }
    const result: string[][] = [];
    for (const pathsList of contentMap.values()) {
        if (pathsList.length > 1) {
            result.push(pathsList);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $paths
     * @return String[][]
     */
    function findDuplicate($paths) {
        $contentMap = [];

        foreach ($paths as $path) {
            $parts = explode(' ', $path);
            $dir = array_shift($parts);

            foreach ($parts as $fileInfo) {
                $openPos  = strpos($fileInfo, '(');
                $closePos = strrpos($fileInfo, ')');
                if ($openPos === false || $closePos === false) {
                    continue;
                }

                $filename = substr($fileInfo, 0, $openPos);
                $content  = substr($fileInfo, $openPos + 1, $closePos - $openPos - 1);
                $fullPath = $dir . '/' . $filename;

                if (!isset($contentMap[$content])) {
                    $contentMap[$content] = [];
                }
                $contentMap[$content][] = $fullPath;
            }
        }

        $result = [];
        foreach ($contentMap as $files) {
            if (count($files) > 1) {
                $result[] = $files;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findDuplicate(_ paths: [String]) -> [[String]] {
        var contentMap = [String: [String]]()
        
        for line in paths {
            let parts = line.split(separator: " ")
            guard let dirPart = parts.first else { continue }
            let directory = String(dirPart)
            
            for fileInfoSub in parts.dropFirst() {
                // Find the '(' and ')' positions
                if let openParen = fileInfoSub.firstIndex(of: "("),
                   let closeParen = fileInfoSub.lastIndex(of: ")") {
                    let name = String(fileInfoSub[..<openParen])
                    let contentStart = fileInfoSub.index(after: openParen)
                    let content = String(fileInfoSub[contentStart..<closeParen])
                    let fullPath = "\(directory)/\(name)"
                    contentMap[content, default: []].append(fullPath)
                }
            }
        }
        
        var result = [[String]]()
        for paths in contentMap.values {
            if paths.count > 1 {
                result.append(paths)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findDuplicate(paths: Array<String>): List<List<String>> {
        val contentMap = HashMap<String, MutableList<String>>()
        for (entry in paths) {
            val parts = entry.split(" ")
            if (parts.isEmpty()) continue
            val dir = parts[0]
            for (i in 1 until parts.size) {
                val fileInfo = parts[i]
                val leftParenIdx = fileInfo.indexOf('(')
                if (leftParenIdx == -1) continue
                val name = fileInfo.substring(0, leftParenIdx)
                val content = fileInfo.substring(leftParenIdx + 1, fileInfo.length - 1)
                val fullPath = "$dir/$name"
                val list = contentMap.getOrPut(content) { mutableListOf() }
                list.add(fullPath)
            }
        }
        val result = mutableListOf<List<String>>()
        for (list in contentMap.values) {
            if (list.size > 1) {
                result.add(list)
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<String>> findDuplicate(List<String> paths) {
    final Map<String, List<String>> contentMap = {};

    for (final path in paths) {
      final parts = path.split(' ');
      final dir = parts[0];
      for (int i = 1; i < parts.length; ++i) {
        final fileInfo = parts[i];
        final leftParen = fileInfo.indexOf('(');
        final rightParen = fileInfo.lastIndexOf(')');
        final filename = fileInfo.substring(0, leftParen);
        final content = fileInfo.substring(leftParen + 1, rightParen);
        final fullPath = '$dir/$filename';
        contentMap.putIfAbsent(content, () => []).add(fullPath);
      }
    }

    final List<List<String>> result = [];
    for (final entry in contentMap.entries) {
      if (entry.value.length > 1) {
        result.add(entry.value);
      }
    }
    return result;
  }
}
```

## Golang

```go
package main

import "strings"

func findDuplicate(paths []string) [][]string {
    contentMap := make(map[string][]string)
    for _, pathInfo := range paths {
        parts := strings.Split(pathInfo, " ")
        dir := parts[0]
        for _, file := range parts[1:] {
            openIdx := strings.Index(file, "(")
            closeIdx := strings.LastIndex(file, ")")
            if openIdx == -1 || closeIdx == -1 || openIdx > closeIdx {
                continue
            }
            name := file[:openIdx]
            content := file[openIdx+1 : closeIdx]
            fullPath := dir + "/" + name
            contentMap[content] = append(contentMap[content], fullPath)
        }
    }

    var result [][]string
    for _, paths := range contentMap {
        if len(paths) > 1 {
            result = append(result, paths)
        }
    }
    return result
}
```

## Ruby

```ruby
def find_duplicate(paths)
  content_map = Hash.new { |h, k| h[k] = [] }

  paths.each do |entry|
    parts = entry.split(' ')
    dir = parts[0]
    parts[1..-1].each do |file_info|
      left_paren = file_info.index('(')
      right_paren = file_info.index(')', left_paren)
      filename = file_info[0...left_paren]
      content = file_info[(left_paren + 1)...right_paren]
      full_path = "#{dir}/#{filename}"
      content_map[content] << full_path
    end
  end

  result = []
  content_map.each_value do |list|
    result << list if list.size > 1
  end
  result
end
```

## Scala

```scala
object Solution {
    def findDuplicate(paths: Array[String]): List[List[String]] = {
        import scala.collection.mutable.{Map => MutableMap, ListBuffer}
        val contentMap = MutableMap[String, ListBuffer[String]]()
        for (entry <- paths) {
            val parts = entry.split(" ")
            if (parts.length > 1) {
                val dir = parts(0)
                var i = 1
                while (i < parts.length) {
                    val fileInfo = parts(i)
                    val idx = fileInfo.indexOf('(')
                    val filename = fileInfo.substring(0, idx)
                    val content = fileInfo.substring(idx + 1, fileInfo.length - 1) // exclude ')'
                    val fullPath = s"$dir/$filename"
                    val list = contentMap.getOrElseUpdate(content, ListBuffer[String]())
                    list += fullPath
                    i += 1
                }
            }
        }
        contentMap.values.filter(_.size > 1).map(_.toList).toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_duplicate(paths: Vec<String>) -> Vec<Vec<String>> {
        use std::collections::HashMap;
        let mut map: HashMap<String, Vec<String>> = HashMap::new();

        for line in paths.iter() {
            let mut parts = line.split_whitespace();
            if let Some(dir) = parts.next() {
                for file in parts {
                    if let Some(idx) = file.find('(') {
                        let name = &file[..idx];
                        // content is between '(' and ')'
                        let content = &file[idx + 1..file.len() - 1];
                        let full_path = format!("{}/{}", dir, name);
                        map.entry(content.to_string())
                            .or_insert_with(Vec::new)
                            .push(full_path);
                    }
                }
            }
        }

        let mut result: Vec<Vec<String>> = Vec::new();
        for paths in map.into_values() {
            if paths.len() > 1 {
                result.push(paths);
            }
        }
        result
    }
}
```

## Racket

```racket
#lang racket

(require racket/string)

(define/contract (find-duplicate paths)
  (-> (listof string?) (listof (listof string?)))
  (let ((h (make-hash)))
    (for ([line paths])
      (define parts (string-split line " "))
      (define dir (first parts))
      (for ([file-token (rest parts)])
        (define idx (string-index file-token #\()))
        (when idx
          (define filename (substring file-token 0 idx))
          (define content (substring file-token (+ idx 1) (- (string-length file-token) 1)))
          (define fullpath (string-append dir "/" filename))
          (hash-set! h content (cons fullpath (hash-ref h content '()))))))
    (let ((result '()))
      (hash-for-each
        h
        (lambda (_ paths-list)
          (when (>= (length paths-list) 2)
            (set! result (cons (reverse paths-list) result)))))
      (reverse result))))
```

## Erlang

```erlang
-module(solution).
-export([find_duplicate/1]).

-spec find_duplicate(Paths :: [unicode:unicode_binary()]) -> [[unicode:unicode_binary()]].
find_duplicate(Paths) ->
    Map = lists:foldl(fun process_path/2, #{}, Paths),
    Groups0 = [PathsList || {_Content, PathsList} <- maps:to_list(Map), length(PathsList) > 1],
    [lists:reverse(G) || G <- Groups0].

process_path(PathStr, AccMap) ->
    Tokens = binary:split(PathStr, <<" ">>, [global]),
    case Tokens of
        [] -> AccMap;
        [Dir|FileTokens] ->
            lists:foldl(fun(FileToken, M) -> add_file(Dir, FileToken, M) end,
                        AccMap, FileTokens)
    end.

add_file(Dir, FileToken, Map) ->
    case binary:split(FileToken, <<"(">>, [global]) of
        [FileName, Rest] when byte_size(Rest) > 0 ->
            Content = binary:part(Rest, 0, byte_size(Rest) - 1),
            FullPath = <<Dir/binary, "/", FileName/binary>>,
            maps:update_with(Content,
                             fun(List) -> [FullPath | List] end,
                             [FullPath],
                             Map);
        _ ->
            Map
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_duplicate(paths :: [String.t]) :: [[String.t]]
  def find_duplicate(paths) do
    content_map =
      Enum.reduce(paths, %{}, fn line, acc ->
        parts = String.split(line, " ", trim: true)
        dir = hd(parts)

        Enum.reduce(tl(parts), acc, fn file_token, acc2 ->
          [filename, content | _] = String.split(file_token, ["(", ")"], trim: true)
          full_path = dir <> "/" <> filename
          Map.update(acc2, content, [full_path], fn list -> [full_path | list] end)
        end)
      end)

    content_map
    |> Enum.filter(fn {_content, paths} -> length(paths) > 1 end)
    |> Enum.map(fn {_content, paths} -> Enum.reverse(paths) end)
  end
end
```
