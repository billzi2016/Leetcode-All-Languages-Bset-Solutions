# 1207. Unique Number of Occurrences

## Cpp

```cpp
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> freq;
        for (int x : arr) ++freq[x];
        unordered_set<int> seen;
        for (const auto& p : freq) {
            if (!seen.insert(p.second).second) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        java.util.Map<Integer, Integer> freq = new java.util.HashMap<>();
        for (int num : arr) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        java.util.Set<Integer> seen = new java.util.HashSet<>();
        for (int count : freq.values()) {
            if (!seen.add(count)) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        counts = set()
        for cnt in freq.values():
            if cnt in counts:
                return False
            counts.add(cnt)
        return True
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        occurrences = freq.values()
        return len(occurrences) == len(set(occurrences))
```

## C

```c
#include <stdbool.h>

bool uniqueOccurrences(int* arr, int arrSize) {
    const int OFFSET = 1000;
    int freq[2001] = {0};
    
    for (int i = 0; i < arrSize; ++i) {
        freq[arr[i] + OFFSET]++;
    }
    
    bool seen[1001] = {false}; // maximum possible frequency is arrSize <= 1000
    for (int i = 0; i < 2001; ++i) {
        int cnt = freq[i];
        if (cnt > 0) {
            if (seen[cnt]) return false;
            seen[cnt] = true;
        }
    }
    
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool UniqueOccurrences(int[] arr)
    {
        var freq = new System.Collections.Generic.Dictionary<int, int>();
        foreach (int num in arr)
        {
            if (freq.ContainsKey(num))
                freq[num]++;
            else
                freq[num] = 1;
        }

        var seen = new System.Collections.Generic.HashSet<int>();
        foreach (var count in freq.Values)
        {
            if (!seen.Add(count))
                return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    const freq = new Map();
    for (const num of arr) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }
    const seen = new Set();
    for (const count of freq.values()) {
        if (seen.has(count)) return false;
        seen.add(count);
    }
    return true;
};
```

## Typescript

```typescript
function uniqueOccurrences(arr: number[]): boolean {
    const freq = new Map<number, number>();
    for (const num of arr) {
        freq.set(num, (freq.get(num) ?? 0) + 1);
    }
    const seen = new Set<number>();
    for (const count of freq.values()) {
        if (seen.has(count)) return false;
        seen.add(count);
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function uniqueOccurrences($arr) {
        $freq = [];
        foreach ($arr as $num) {
            if (!isset($freq[$num])) {
                $freq[$num] = 0;
            }
            $freq[$num]++;
        }

        $seen = [];
        foreach ($freq as $count) {
            if (isset($seen[$count])) {
                return false;
            }
            $seen[$count] = true;
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func uniqueOccurrences(_ arr: [Int]) -> Bool {
        var frequency = [Int: Int]()
        for num in arr {
            frequency[num, default: 0] += 1
        }
        var seen = Set<Int>()
        for count in frequency.values {
            if seen.contains(count) {
                return false
            }
            seen.insert(count)
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun uniqueOccurrences(arr: IntArray): Boolean {
        val freq = mutableMapOf<Int, Int>()
        for (num in arr) {
            freq[num] = (freq[num] ?: 0) + 1
        }
        val seen = HashSet<Int>()
        for (count in freq.values) {
            if (!seen.add(count)) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool uniqueOccurrences(List<int> arr) {
    final Map<int, int> freq = {};
    for (var v in arr) {
      freq[v] = (freq[v] ?? 0) + 1;
    }
    final Set<int> seen = {};
    for (var count in freq.values) {
      if (!seen.add(count)) return false;
    }
    return true;
  }
}
```

## Golang

```go
func uniqueOccurrences(arr []int) bool {
	freq := make(map[int]int)
	for _, v := range arr {
		freq[v]++
	}
	seen := make(map[int]struct{})
	for _, cnt := range freq {
		if _, ok := seen[cnt]; ok {
			return false
		}
		seen[cnt] = struct{}{}
	}
	return true
}
```

## Ruby

```ruby
def unique_occurrences(arr)
  freq = Hash.new(0)
  arr.each { |num| freq[num] += 1 }
  counts = freq.values
  counts.uniq.length == counts.length
end
```

## Scala

```scala
object Solution {
    def uniqueOccurrences(arr: Array[Int]): Boolean = {
        val freq = scala.collection.mutable.Map[Int, Int]()
        for (x <- arr) {
            freq(x) = freq.getOrElse(x, 0) + 1
        }
        val counts = freq.values
        counts.toSet.size == counts.size
    }
}
```

## Rust

```rust
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let mut freq = HashMap::new();
        for x in arr {
            *freq.entry(x).or_insert(0) += 1;
        }
        let mut seen = HashSet::new();
        for &cnt in freq.values() {
            if !seen.insert(cnt) {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(require racket/contract)

(define/contract (unique-occurrences arr)
  (-> (listof exact-integer?) boolean?)
  (let ([freq (make-hash)])
    (for ([x arr])
      (hash-set! freq x (+ 1 (hash-ref freq x 0))))
    (let ([seen (make-hash)])
      (define duplicate?
        (for/or ([c (hash-values freq)])
          (if (hash-has-key? seen c)
              #t
              (begin (hash-set! seen c #t) #f))))
      (not duplicate?))))
```

## Erlang

```erlang
-spec unique_occurrences([integer()]) -> boolean().
unique_occurrences(Arr) ->
    FreqMap = count_map(Arr, #{}),
    Counts = maps:values(FreqMap),
    length(Counts) =:= length(lists:usort(Counts)).

count_map([], M) -> M;
count_map([H|T], M) ->
    NewM = case maps:is_key(H, M) of
        true -> maps:update_with(H, fun(C) -> C + 1 end, M);
        false -> maps:put(H, 1, M)
    end,
    count_map(T, NewM).
```

## Elixir

```elixir
defmodule Solution do
  @spec unique_occurrences(arr :: [integer]) :: boolean
  def unique_occurrences(arr) do
    freq =
      Enum.reduce(arr, %{}, fn x, acc ->
        Map.update(acc, x, 1, &(&1 + 1))
      end)

    counts = Map.values(freq)
    MapSet.size(MapSet.new(counts)) == length(counts)
  end
end
```
