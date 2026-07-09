# 0049. Group Anagrams

## Cpp

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for (const string& s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            groups[key].push_back(s);
        }
        vector<vector<string>> result;
        result.reserve(groups.size());
        for (auto& kv : groups) {
            result.push_back(std::move(kv.second));
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
```

## Python

```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for s in strs:
            # Use character count as key to avoid sorting overhead
            count = [0] * 26
            for ch in s:
                count[ord(ch) - 97] += 1
            key = tuple(count)
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char **words;
    int size;
    int cap;
} Group;

typedef struct HashNode {
    char *key;               // sorted string as signature
    int groupIdx;            // index in groups array
    struct HashNode *next;
} HashNode;

static int cmpChar(const void *a, const void *b) {
    return (*(const char *)a) - (*(const char *)b);
}

static unsigned int hashString(const char *s) {
    unsigned long h = 5381;
    while (*s) {
        h = ((h << 5) + h) + (unsigned char)(*s); // h * 33 + c
        s++;
    }
    return (unsigned int)h;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** groupAnagrams(char** strs, int strsSize, int* returnSize, int** returnColumnSizes) {
    const int HASH_SIZE = 20011; // a prime number
    HashNode **table = calloc(HASH_SIZE, sizeof(HashNode *));
    
    int groupsCap = 128;
    Group *groups = malloc(groupsCap * sizeof(Group));
    int groupsCount = 0;
    
    for (int i = 0; i < strsSize; ++i) {
        const char *s = strs[i];
        int len = strlen(s);
        char *sorted = malloc(len + 1);
        strcpy(sorted, s);
        if (len > 1)
            qsort(sorted, len, sizeof(char), cmpChar);
        
        unsigned int h = hashString(sorted) % HASH_SIZE;
        HashNode *node = table[h];
        while (node && strcmp(node->key, sorted) != 0) {
            node = node->next;
        }
        
        int idx;
        if (node) {
            idx = node->groupIdx;
            free(sorted); // not needed as key already stored
        } else {
            // create new group
            if (groupsCount == groupsCap) {
                groupsCap <<= 1;
                groups = realloc(groups, groupsCap * sizeof(Group));
            }
            groups[groupsCount].size = 0;
            groups[groupsCount].cap = 4;
            groups[groupsCount].words = malloc(groups[groupsCount].cap * sizeof(char *));
            
            // insert into hash table
            HashNode *newnode = malloc(sizeof(HashNode));
            newnode->key = sorted;          // keep the sorted string as key
            newnode->groupIdx = groupsCount;
            newnode->next = table[h];
            table[h] = newnode;
            
            idx = groupsCount;
            groupsCount++;
        }
        
        Group *g = &groups[idx];
        if (g->size == g->cap) {
            g->cap <<= 1;
            g->words = realloc(g->words, g->cap * sizeof(char *));
        }
        g->words[g->size++] = strs[i];
    }
    
    // Prepare return values
    char ***result = malloc(groupsCount * sizeof(char **));
    int *colSizes = malloc(groupsCount * sizeof(int));
    for (int i = 0; i < groupsCount; ++i) {
        result[i] = groups[i].words;
        colSizes[i] = groups[i].size;
    }
    
    *returnSize = groupsCount;
    *returnColumnSizes = colSizes;
    
    // Cleanup hash table structures (keys are kept inside result)
    for (int i = 0; i < HASH_SIZE; ++i) {
        HashNode *node = table[i];
        while (node) {
            HashNode *next = node->next;
            free(node); // key memory is owned by groups' hashmap, not freed here
            node = next;
        }
    }
    free(table);
    free(groups); // only the struct array; inner words arrays are returned
    
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<IList<string>> GroupAnagrams(string[] strs)
    {
        var map = new Dictionary<string, List<string>>();
        foreach (var s in strs)
        {
            char[] chars = s.ToCharArray();
            Array.Sort(chars);
            string key = new string(chars);
            if (!map.TryGetValue(key, out var list))
            {
                list = new List<string>();
                map[key] = list;
            }
            list.Add(s);
        }

        IList<IList<string>> result = new List<IList<string>>();
        foreach (var group in map.Values)
        {
            result.Add(group);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const groups = new Map();
    for (const s of strs) {
        const key = s.split('').sort().join('');
        if (!groups.has(key)) groups.set(key, []);
        groups.get(key).push(s);
    }
    return Array.from(groups.values());
};
```

## Typescript

```typescript
function groupAnagrams(strs: string[]): string[][] {
    const groups = new Map<string, string[]>();
    for (const s of strs) {
        const key = s.split('').sort().join('');
        if (!groups.has(key)) {
            groups.set(key, []);
        }
        groups.get(key)!.push(s);
    }
    return Array.from(groups.values());
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $strs
     * @return String[][]
     */
    function groupAnagrams($strs) {
        $map = [];
        foreach ($strs as $s) {
            $chars = str_split($s);
            sort($chars);
            $key = implode('', $chars);
            if (!isset($map[$key])) {
                $map[$key] = [];
            }
            $map[$key][] = $s;
        }
        return array_values($map);
    }
}
```

## Swift

```swift
class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var groups = [String: [String]]()
        for s in strs {
            let key = String(s.sorted())
            groups[key, default: []].append(s)
        }
        return Array(groups.values)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        val map = HashMap<String, MutableList<String>>()
        for (s in strs) {
            val chars = s.toCharArray()
            chars.sort()
            val key = String(chars)
            map.getOrPut(key) { mutableListOf() }.add(s)
        }
        return map.values.toList()
    }
}
```

## Dart

```dart
class Solution {
  List<List<String>> groupAnagrams(List<String> strs) {
    final Map<String, List<String>> groups = {};
    for (final s in strs) {
      final chars = s.split('')..sort();
      final key = chars.join();
      groups.putIfAbsent(key, () => []).add(s);
    }
    return groups.values.toList();
  }
}
```

## Golang

```go
import "sort"

func groupAnagrams(strs []string) [][]string {
	m := make(map[string][]string)
	for _, s := range strs {
		b := []byte(s)
		sort.Slice(b, func(i, j int) bool { return b[i] < b[j] })
		key := string(b)
		m[key] = append(m[key], s)
	}
	res := make([][]string, 0, len(m))
	for _, v := range m {
		res = append(res, v)
	}
	return res
}
```

## Ruby

```ruby
def group_anagrams(strs)
  groups = Hash.new { |h, k| h[k] = [] }
  strs.each do |s|
    key = s.chars.sort.join
    groups[key] << s
  end
  groups.values
end
```

## Scala

```scala
object Solution {
    def groupAnagrams(strs: Array[String]): List[List[String]] = {
        val groups = scala.collection.mutable.Map[String, scala.collection.mutable.ListBuffer[String]]()
        for (s <- strs) {
            val key = s.sorted
            groups.getOrElseUpdate(key, scala.collection.mutable.ListBuffer()).append(s)
        }
        groups.values.map(_.toList).toList
    }
}
```

## Rust

```rust
use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut groups: HashMap<String, Vec<String>> = HashMap::new();
        for s in strs {
            let mut chars: Vec<char> = s.chars().collect();
            chars.sort_unstable();
            let key: String = chars.iter().collect();
            groups.entry(key).or_default().push(s);
        }
        groups.into_values().collect()
    }
}
```

## Racket

```racket
(define/contract (group-anagrams strs)
  (-> (listof string?) (listof (listof string?)))
  (let ([ht (make-hash)])
    (for-each
     (lambda (s)
       (define key (list->string (sort (string->list s) char<?)))
       (hash-set! ht key (cons s (hash-ref ht key '()))))
     strs)
    (map reverse (hash-values ht))))
```

## Erlang

```erlang
-module(solution).
-export([group_anagrams/1]).

-spec group_anagrams(Strs :: [unicode:unicode_binary()]) -> [[unicode:unicode_binary()]].
group_anagrams(Strs) ->
    Map = lists:foldl(
        fun(S, Acc) ->
            Key = sorted_key(S),
            case maps:get(Key, Acc, undefined) of
                undefined -> maps:put(Key, [S], Acc);
                List -> maps:put(Key, [S | List], Acc)
            end
        end,
        #{},
        Strs),
    lists:map(fun({_K, V}) -> V end, maps:to_list(Map)).

sorted_key(S) ->
    Chars = unicode:characters_to_list(S),
    Sorted = lists:sort(Chars),
    list_to_binary(Sorted).
```

## Elixir

```elixir
defmodule Solution do
  @spec group_anagrams(strs :: [String.t]) :: [[String.t]]
  def group_anagrams(strs) do
    strs
    |> Enum.reduce(%{}, fn s, acc ->
      key = s |> String.graphemes() |> Enum.sort() |> Enum.join()
      Map.update(acc, key, [s], &[s | &1])
    end)
    |> Map.values()
    |> Enum.map(&Enum.reverse/1)
  end
end
```
