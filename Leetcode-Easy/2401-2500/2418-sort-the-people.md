# 2418. Sort the People

## Cpp

```cpp
class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        int n = names.size();
        vector<pair<int, string>> people;
        people.reserve(n);
        for (int i = 0; i < n; ++i) {
            people.emplace_back(heights[i], names[i]);
        }
        sort(people.begin(), people.end(),
             [](const pair<int, string>& a, const pair<int, string>& b) {
                 return a.first > b.first;
             });
        vector<string> result;
        result.reserve(n);
        for (auto& p : people) {
            result.push_back(p.second);
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        int n = names.length;
        Integer[] indices = new Integer[n];
        for (int i = 0; i < n; i++) {
            indices[i] = i;
        }
        Arrays.sort(indices, (a, b) -> Integer.compare(heights[b], heights[a]));
        String[] result = new String[n];
        for (int i = 0; i < n; i++) {
            result[i] = names[indices[i]];
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # Pair each height with its corresponding name and sort by height descending
        paired = sorted(zip(heights, names), reverse=True)
        return [name for _, name in paired]
```

## Python3

```python
from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Pair each height with its corresponding name and sort by height descending
        sorted_pairs = sorted(zip(heights, names), reverse=True)
        # Extract the names in the new order
        return [name for _, name in sorted_pairs]
```

## C

```c
#include <stdlib.h>

typedef struct {
    char *name;
    int height;
} Person;

static int cmpPerson(const void *a, const void *b) {
    const Person *pa = (const Person *)a;
    const Person *pb = (const Person *)b;
    return pb->height - pa->height;  // descending order
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** sortPeople(char** names, int namesSize, int* heights, int heightsSize, int* returnSize) {
    int n = namesSize;
    Person *people = (Person *)malloc(n * sizeof(Person));
    for (int i = 0; i < n; ++i) {
        people[i].name = names[i];
        people[i].height = heights[i];
    }

    qsort(people, n, sizeof(Person), cmpPerson);

    char **result = (char **)malloc(n * sizeof(char *));
    for (int i = 0; i < n; ++i) {
        result[i] = people[i].name;
    }

    free(people);
    *returnSize = n;
    return result;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public string[] SortPeople(string[] names, int[] heights) {
        int n = names.Length;
        int[] indices = new int[n];
        for (int i = 0; i < n; i++) {
            indices[i] = i;
        }
        Array.Sort(indices, (a, b) => heights[b].CompareTo(heights[a]));
        string[] result = new string[n];
        for (int i = 0; i < n; i++) {
            result[i] = names[indices[i]];
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 */
var sortPeople = function(names, heights) {
    const paired = heights.map((h, i) => [h, names[i]]);
    paired.sort((a, b) => b[0] - a[0]);
    return paired.map(p => p[1]);
};
```

## Typescript

```typescript
function sortPeople(names: string[], heights: number[]): string[] {
    const combined: [number, string][] = [];
    for (let i = 0; i < names.length; i++) {
        combined.push([heights[i], names[i]]);
    }
    combined.sort((a, b) => b[0] - a[0]);
    return combined.map(pair => pair[1]);
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $names
     * @param Integer[] $heights
     * @return String[]
     */
    function sortPeople($names, $heights) {
        $n = count($names);
        $people = [];
        for ($i = 0; $i < $n; $i++) {
            $people[] = ['name' => $names[$i], 'height' => $heights[$i]];
        }
        usort($people, function ($a, $b) {
            return $b['height'] <=> $a['height'];
        });
        $result = [];
        foreach ($people as $p) {
            $result[] = $p['name'];
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func sortPeople(_ names: [String], _ heights: [Int]) -> [String] {
        let paired = (0..<names.count).map { (heights[$0], names[$0]) }
        let sorted = paired.sorted { $0.0 > $1.0 }
        return sorted.map { $0.1 }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sortPeople(names: Array<String>, heights: IntArray): Array<String> {
        val order = names.indices.sortedByDescending { heights[it] }
        return Array(names.size) { i -> names[order[i]] }
    }
}
```

## Dart

```dart
class Solution {
  List<String> sortPeople(List<String> names, List<int> heights) {
    int n = names.length;
    List<int> indices = List<int>.generate(n, (i) => i);
    indices.sort((a, b) => heights[b].compareTo(heights[a]));
    return indices.map((i) => names[i]).toList();
  }
}
```

## Golang

```go
package main

import "sort"

func sortPeople(names []string, heights []int) []string {
	type person struct {
		name   string
		height int
	}
	n := len(names)
	people := make([]person, n)
	for i := 0; i < n; i++ {
		people[i] = person{name: names[i], height: heights[i]}
	}
	sort.Slice(people, func(i, j int) bool {
		return people[i].height > people[j].height
	})
	res := make([]string, n)
	for i, p := range people {
		res[i] = p.name
	}
	return res
}
```

## Ruby

```ruby
def sort_people(names, heights)
  pairs = names.each_with_index.map { |name, i| [heights[i], name] }
  pairs.sort! { |a, b| b[0] <=> a[0] }
  pairs.map { |_, name| name }
end
```

## Scala

```scala
object Solution {
    def sortPeople(names: Array[String], heights: Array[Int]): Array[String] = {
        (0 until names.length)
          .sortWith((i, j) => heights(i) > heights(j))
          .map(names(_))
          .toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sort_people(names: Vec<String>, heights: Vec<i32>) -> Vec<String> {
        let mut combined: Vec<(i32, String)> = heights.into_iter().zip(names).collect();
        combined.sort_by(|a, b| b.0.cmp(&a.0));
        combined.into_iter().map(|(_, name)| name).collect()
    }
}
```

## Racket

```racket
(define/contract (sort-people names heights)
  (-> (listof string?) (listof exact-integer?) (listof string?))
  (let* ((pairs (map cons names heights))
         (sorted-pairs (sort pairs (lambda (a b) (> (cdr a) (cdr b))))))
    (map car sorted-pairs)))
```

## Erlang

```erlang
-module(solution).
-export([sort_people/2]).

-spec sort_people(Names :: [unicode:unicode_binary()], Heights :: [integer()]) -> [unicode:unicode_binary()].
sort_people(Names, Heights) ->
    Pairs = lists:zip(Heights, Names),
    SortedPairs = lists:sort(fun({H1,_}, {H2,_}) -> H1 > H2 end, Pairs),
    [Name || {_Height, Name} <- SortedPairs].
```

## Elixir

```elixir
defmodule Solution do
  @spec sort_people(names :: [String.t()], heights :: [integer]) :: [String.t()]
  def sort_people(names, heights) do
    Enum.zip(heights, names)
    |> Enum.sort_by(fn {h, _} -> h end, :desc)
    |> Enum.map(fn {_h, n} -> n end)
  end
end
```
