# 1487. Making File Names Unique

## Cpp

```cpp
class Solution {
public:
    vector<string> getFolderNames(vector<string>& names) {
        unordered_map<string, int> nxt;
        vector<string> result;
        result.reserve(names.size());
        for (const string& name : names) {
            if (!nxt.count(name)) {
                result.push_back(name);
                nxt[name] = 1;
            } else {
                int k = nxt[name];
                string newName;
                while (true) {
                    newName = name + "(" + to_string(k) + ")";
                    if (!nxt.count(newName)) break;
                    ++k;
                }
                result.push_back(newName);
                nxt[newName] = 1;
                nxt[name] = k + 1;
            }
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public String[] getFolderNames(String[] names) {
        int n = names.length;
        String[] result = new String[n];
        java.util.HashMap<String, Integer> map = new java.util.HashMap<>();
        for (int i = 0; i < n; i++) {
            String name = names[i];
            if (!map.containsKey(name)) {
                result[i] = name;
                map.put(name, 1);
            } else {
                int k = map.get(name);
                String newName;
                while (true) {
                    newName = name + "(" + k + ")";
                    if (!map.containsKey(newName)) break;
                    k++;
                }
                result[i] = newName;
                map.put(name, k + 1);
                map.put(newName, 1);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        nxt = {}
        res = []
        for name in names:
            if name not in nxt:
                res.append(name)
                nxt[name] = 1
            else:
                k = nxt[name]
                while True:
                    new_name = f"{name}({k})"
                    if new_name not in nxt:
                        break
                    k += 1
                res.append(new_name)
                nxt[new_name] = 1
                nxt[name] = k + 1
        return res
```

## Python3

```python
from typing import List

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        nxt = {}
        result = []
        for name in names:
            if name not in nxt:
                result.append(name)
                nxt[name] = 1
            else:
                k = nxt[name]
                while True:
                    new_name = f"{name}({k})"
                    if new_name not in nxt:
                        break
                    k += 1
                result.append(new_name)
                nxt[name] = k + 1
                nxt[new_name] = 1
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define HASH_SIZE 131071  // a prime number > 2*5e4

typedef struct Entry {
    char *key;
    int val;               // next suffix to try
    struct Entry *next;
} Entry;

static unsigned long hash_func(const char *s) {
    unsigned long h = 5381;
    while (*s) {
        h = ((h << 5) + h) + (unsigned char)(*s);
        s++;
    }
    return h;
}

static char *str_dup(const char *s) {
    size_t len = strlen(s);
    char *p = (char *)malloc(len + 1);
    if (p) memcpy(p, s, len + 1);
    return p;
}

/* hashmap operations */
static Entry *table[HASH_SIZE];

static Entry *find_entry(const char *key) {
    unsigned long idx = hash_func(key) % HASH_SIZE;
    Entry *e = table[idx];
    while (e) {
        if (strcmp(e->key, key) == 0) return e;
        e = e->next;
    }
    return NULL;
}

static int hashmap_get(const char *key, int *out_val) {
    Entry *e = find_entry(key);
    if (e) {
        *out_val = e->val;
        return 1;
    }
    return 0;
}

static void hashmap_put(const char *key, int val) {
    unsigned long idx = hash_func(key) % HASH_SIZE;
    Entry *e = table[idx];
    while (e) {
        if (strcmp(e->key, key) == 0) {
            e->val = val;
            return;
        }
        e = e->next;
    }
    // not found, create new
    Entry *new_e = (Entry *)malloc(sizeof(Entry));
    new_e->key = str_dup(key);
    new_e->val = val;
    new_e->next = table[idx];
    table[idx] = new_e;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** getFolderNames(char** names, int namesSize, int* returnSize) {
    char **ans = (char **)malloc(namesSize * sizeof(char *));
    for (int i = 0; i < namesSize; ++i) {
        const char *cur = names[i];
        int dummy;
        if (!hashmap_get(cur, &dummy)) {
            ans[i] = str_dup(cur);
            hashmap_put(cur, 1);               // next suffix starts at 1
        } else {
            int k = dummy;                     // start from stored next suffix
            char newName[64];
            while (1) {
                snprintf(newName, sizeof(newName), "%s(%d)", cur, k);
                if (!hashmap_get(newName, &dummy)) {
                    ans[i] = str_dup(newName);
                    hashmap_put(cur, k + 1);   // update original name's next suffix
                    hashmap_put(newName, 1);   // register the new name
                    break;
                }
                ++k;
            }
        }
    }
    *returnSize = namesSize;
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public string[] GetFolderNames(string[] names) {
        var next = new Dictionary<string, int>();
        var ans = new string[names.Length];
        for (int i = 0; i < names.Length; i++) {
            string name = names[i];
            if (!next.ContainsKey(name)) {
                ans[i] = name;
                next[name] = 1;
            } else {
                int k = next[name];
                string newName;
                while (true) {
                    newName = $"{name}({k})";
                    if (!next.ContainsKey(newName)) break;
                    k++;
                }
                ans[i] = newName;
                next[name] = k + 1;
                next[newName] = 1;
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} names
 * @return {string[]}
 */
var getFolderNames = function(names) {
    const used = new Map();
    const ans = [];
    for (const name of names) {
        if (!used.has(name)) {
            ans.push(name);
            used.set(name, 1);
        } else {
            let k = used.get(name);
            let newName;
            while (true) {
                newName = `${name}(${k})`;
                if (!used.has(newName)) break;
                k++;
            }
            ans.push(newName);
            used.set(name, k + 1);
            used.set(newName, 1);
        }
    }
    return ans;
};
```

## Typescript

```typescript
function getFolderNames(names: string[]): string[] {
    const used = new Map<string, number>();
    const ans: string[] = [];
    for (const name of names) {
        if (!used.has(name)) {
            ans.push(name);
            used.set(name, 1);
        } else {
            let k = used.get(name)!;
            let newName = `${name}(${k})`;
            while (used.has(newName)) {
                k++;
                newName = `${name}(${k})`;
            }
            ans.push(newName);
            used.set(name, k + 1);
            used.set(newName, 1);
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $names
     * @return String[]
     */
    function getFolderNames($names) {
        $map = [];
        $result = [];

        foreach ($names as $name) {
            if (!isset($map[$name])) {
                $result[] = $name;
                $map[$name] = 1;
            } else {
                $k = $map[$name];
                while (true) {
                    $newName = $name . '(' . $k . ')';
                    if (!isset($map[$newName])) {
                        break;
                    }
                    $k++;
                }
                $result[] = $newName;
                $map[$newName] = 1;
                $map[$name] = $k + 1;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func getFolderNames(_ names: [String]) -> [String] {
        var nextIndex = [String: Int]()
        var result = [String]()
        
        for name in names {
            if nextIndex[name] == nil {
                // Name is unused
                result.append(name)
                nextIndex[name] = 1
            } else {
                var k = nextIndex[name]!   // start from the smallest candidate
                var newName: String
                while true {
                    newName = "\(name)(\(k))"
                    if nextIndex[newName] == nil {
                        break
                    }
                    k += 1
                }
                result.append(newName)
                // Update the next available suffix for the original name
                nextIndex[name] = k + 1
                // Record the newly created name as used
                nextIndex[newName] = 1
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getFolderNames(names: Array<String>): Array<String> {
        val next = HashMap<String, Int>()
        val result = ArrayList<String>(names.size)
        for (name in names) {
            if (!next.containsKey(name)) {
                result.add(name)
                next[name] = 1
            } else {
                var k = next[name]!!
                var newName: String
                while (true) {
                    newName = "$name($k)"
                    if (!next.containsKey(newName)) break
                    k++
                }
                result.add(newName)
                next[name] = k + 1
                next[newName] = 1
            }
        }
        return result.toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<String> getFolderNames(List<String> names) {
    final Map<String, int> next = {};
    final List<String> result = [];

    for (var name in names) {
      if (!next.containsKey(name)) {
        result.add(name);
        next[name] = 1;
      } else {
        int k = next[name]!;
        String newName;
        while (true) {
          newName = '$name($k)';
          if (!next.containsKey(newName)) break;
          k++;
        }
        result.add(newName);
        next[name] = k + 1; // next candidate for the original name
        next[newName] = 1;   // register the new unique name
      }
    }

    return result;
  }
}
```

## Golang

```go
package main

import "fmt"

func getFolderNames(names []string) []string {
	next := make(map[string]int)
	res := make([]string, 0, len(names))
	for _, name := range names {
		if _, ok := next[name]; !ok {
			res = append(res, name)
			next[name] = 1
		} else {
			k := next[name]
			var newName string
			for {
				newName = fmt.Sprintf("%s(%d)", name, k)
				if _, exists := next[newName]; !exists {
					break
				}
				k++
			}
			res = append(res, newName)
			next[name] = k + 1
			next[newName] = 1
		}
	}
	return res
}
```

## Ruby

```ruby
def get_folder_names(names)
  seen = {}
  result = []

  names.each do |name|
    if !seen.key?(name)
      result << name
      seen[name] = 1
    else
      k = seen[name]
      loop do
        new_name = "#{name}(#{k})"
        unless seen.key?(new_name)
          result << new_name
          seen[new_name] = 1
          seen[name] = k + 1
          break
        end
        k += 1
      end
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def getFolderNames(names: Array[String]): Array[String] = {
        val nextIdx = scala.collection.mutable.HashMap[String, Int]()
        val result = new Array[String](names.length)
        for (i <- names.indices) {
            var name = names(i)
            if (!nextIdx.contains(name)) {
                result(i) = name
                nextIdx(name) = 1
            } else {
                var k = nextIdx(name)
                var newName = s"$name($k)"
                while (nextIdx.contains(newName)) {
                    k += 1
                    newName = s"$name($k)"
                }
                result(i) = newName
                nextIdx(name) = k + 1
                nextIdx(newName) = 1
            }
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_folder_names(names: Vec<String>) -> Vec<String> {
        use std::collections::HashMap;
        let mut next_suffix: HashMap<String, i32> = HashMap::new();
        let mut result: Vec<String> = Vec::with_capacity(names.len());

        for name in names.into_iter() {
            if !next_suffix.contains_key(&name) {
                result.push(name.clone());
                next_suffix.insert(name, 1);
            } else {
                let mut k = *next_suffix.get(&name).unwrap();
                loop {
                    let candidate = format!("{}({})", name, k);
                    if !next_suffix.contains_key(&candidate) {
                        result.push(candidate.clone());
                        next_suffix.insert(name.clone(), k + 1);
                        next_suffix.insert(candidate, 1);
                        break;
                    } else {
                        k += 1;
                    }
                }
            }
        }

        result
    }
}
```

## Racket

```racket
#lang racket

(provide get-folder-names)

(define/contract (get-folder-names names)
  (-> (listof string?) (listof string?))
  (let ((used (make-hash))
        (next-suffix (make-hash)))
    (map
     (lambda (s)
       (if (hash-has-key? used s)
           (let loop ((k (hash-ref next-suffix s 1)))
             (define candidate (string-append s "(" (number->string k) ")"))
             (if (hash-has-key? used candidate)
                 (loop (+ k 1))
                 (begin
                   (hash-set! used candidate #t)
                   (hash-set! next-suffix s (+ k 1))
                   (unless (hash-has-key? next-suffix candidate)
                     (hash-set! next-suffix candidate 1))
                   candidate)))
           (begin
             (hash-set! used s #t)
             (unless (hash-has-key? next-suffix s)
               (hash-set! next-suffix s 1))
             s)))
     names)))
```

## Erlang

```erlang
-spec get_folder_names(Names :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
get_folder_names(Names) ->
    process(Names, #{}, []).

process([], _Map, Acc) ->
    lists:reverse(Acc);
process([N|Rest], Map, Acc) ->
    case maps:is_key(N, Map) of
        false ->
            NewMap = maps:put(N, 1, Map),
            process(Rest, NewMap, [N|Acc]);
        true ->
            K0 = maps:get(N, Map),
            {NewName, UpdatedMap} = find_unique(N, K0, Map),
            process(Rest, UpdatedMap, [NewName|Acc])
    end.

find_unique(Base, K, Map) ->
    NewName = <<Base/binary, "(", (integer_to_binary(K))/binary, ")">>,
    case maps:is_key(NewName, Map) of
        false ->
            Map1 = maps:put(NewName, 1, Map),
            Map2 = maps:put(Base, K + 1, Map1),
            {NewName, Map2};
        true ->
            find_unique(Base, K + 1, Map)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_folder_names(names :: [String.t]) :: [String.t]
  def get_folder_names(names) do
    {result_rev, _map} =
      Enum.reduce(names, {[], %{}}, fn name, {acc, mp} ->
        case Map.fetch(mp, name) do
          :error ->
            { [name | acc], Map.put(mp, name, 1) }

          {:ok, k} ->
            {new_name, next_k, updated_mp} = find_unique(name, k, mp)
            new_map =
              updated_mp
              |> Map.put(name, next_k)
              |> Map.put(new_name, 1)

            {[new_name | acc], new_map}
        end
      end)

    Enum.reverse(result_rev)
  end

  defp find_unique(base, k, mp) do
    candidate = base <> "(" <> Integer.to_string(k) <> ")"

    if Map.has_key?(mp, candidate) do
      find_unique(base, k + 1, mp)
    else
      {candidate, k + 1, mp}
    end
  end
end
```
