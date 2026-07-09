# 1338. Reduce Array Size to The Half

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minSetSize(vector<int>& arr) {
        unordered_map<int,int> freq;
        for (int x : arr) ++freq[x];
        vector<int> counts;
        counts.reserve(freq.size());
        for (auto &p : freq) counts.push_back(p.second);
        sort(counts.rbegin(), counts.rend());
        int need = arr.size() / 2;
        int removed = 0, ans = 0;
        for (int c : counts) {
            removed += c;
            ++ans;
            if (removed >= need) break;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minSetSize(int[] arr) {
        java.util.HashMap<Integer, Integer> map = new java.util.HashMap<>();
        for (int num : arr) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        int m = map.size();
        int[] freq = new int[m];
        int idx = 0;
        for (int count : map.values()) {
            freq[idx++] = count;
        }
        java.util.Arrays.sort(freq); // ascending
        int half = arr.length / 2;
        int removed = 0, setSize = 0;
        for (int i = m - 1; i >= 0 && removed < half; i--) {
            removed += freq[i];
            setSize++;
        }
        return setSize;
    }
}
```

## Python

```python
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter
        freq = Counter(arr)
        counts = sorted(freq.values(), reverse=True)
        target = len(arr) // 2
        removed = 0
        ans = 0
        for c in counts:
            removed += c
            ans += 1
            if removed >= target:
                return ans
        return ans
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        counts = sorted(freq.values(), reverse=True)
        target = len(arr) // 2
        removed = 0
        ans = 0
        for c in counts:
            removed += c
            ans += 1
            if removed >= target:
                return ans
        return ans
```

## C

```c
#include <stdlib.h>

static int freq[100001];

static int cmp_desc(const void *a, const void *b) {
    int ai = *(const int *)a;
    int bi = *(const int *)b;
    return bi - ai;
}

int minSetSize(int* arr, int arrSize) {
    int maxVal = 0;
    for (int i = 0; i < arrSize; ++i) {
        int v = arr[i];
        freq[v]++;
        if (v > maxVal) maxVal = v;
    }

    int distinct = 0;
    int *list = (int *)malloc(sizeof(int) * arrSize);
    for (int i = 0; i <= maxVal; ++i) {
        if (freq[i] > 0) {
            list[distinct++] = freq[i];
        }
    }

    qsort(list, distinct, sizeof(int), cmp_desc);

    int removed = 0;
    int setSize = 0;
    int target = arrSize / 2;
    for (int i = 0; i < distinct && removed < target; ++i) {
        removed += list[i];
        ++setSize;
    }

    for (int i = 0; i <= maxVal; ++i) {
        if (freq[i] > 0) freq[i] = 0;
    }
    free(list);
    return setSize;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinSetSize(int[] arr) {
        var freq = new Dictionary<int, int>();
        foreach (int num in arr) {
            if (freq.ContainsKey(num))
                freq[num]++;
            else
                freq[num] = 1;
        }

        var counts = new List<int>(freq.Values);
        counts.Sort((a, b) => b.CompareTo(a)); // descending

        int target = arr.Length / 2;
        int removed = 0;
        int setSize = 0;

        foreach (int cnt in counts) {
            if (removed >= target) break;
            removed += cnt;
            setSize++;
        }

        return setSize;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var minSetSize = function(arr) {
    const freqMap = new Map();
    for (const num of arr) {
        freqMap.set(num, (freqMap.get(num) || 0) + 1);
    }
    const frequencies = Array.from(freqMap.values());
    frequencies.sort((a, b) => b - a);
    
    const target = arr.length / 2;
    let removed = 0;
    let count = 0;
    for (const f of frequencies) {
        removed += f;
        count++;
        if (removed >= target) break;
    }
    return count;
};
```

## Typescript

```typescript
function minSetSize(arr: number[]): number {
    const freqMap = new Map<number, number>();
    for (const num of arr) {
        freqMap.set(num, (freqMap.get(num) ?? 0) + 1);
    }
    const freqs = Array.from(freqMap.values());
    freqs.sort((a, b) => b - a);
    
    const target = arr.length / 2;
    let removed = 0;
    let count = 0;
    for (const f of freqs) {
        removed += f;
        count++;
        if (removed >= target) break;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function minSetSize($arr) {
        $freq = [];
        foreach ($arr as $num) {
            if (!isset($freq[$num])) {
                $freq[$num] = 0;
            }
            $freq[$num]++;
        }

        $counts = array_values($freq);
        rsort($counts); // descending order

        $target = intdiv(count($arr), 2);
        $removed = 0;
        $setSize = 0;

        foreach ($counts as $c) {
            $removed += $c;
            $setSize++;
            if ($removed >= $target) {
                break;
            }
        }

        return $setSize;
    }
}
```

## Swift

```swift
class Solution {
    func minSetSize(_ arr: [Int]) -> Int {
        var freq = [Int: Int]()
        for num in arr {
            freq[num, default: 0] += 1
        }
        let sortedFreqs = freq.values.sorted(by: >)
        var removed = 0
        var count = 0
        let target = arr.count / 2
        for f in sortedFreqs {
            removed += f
            count += 1
            if removed >= target {
                return count
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSetSize(arr: IntArray): Int {
        val freq = HashMap<Int, Int>()
        for (num in arr) {
            freq[num] = (freq[num] ?: 0) + 1
        }
        val counts = freq.values.sortedDescending()
        var removed = 0
        var setSize = 0
        val target = arr.size / 2
        for (c in counts) {
            removed += c
            setSize++
            if (removed >= target) break
        }
        return setSize
    }
}
```

## Dart

```dart
class Solution {
  int minSetSize(List<int> arr) {
    final Map<int, int> freq = {};
    for (var v in arr) {
      freq[v] = (freq[v] ?? 0) + 1;
    }
    List<int> counts = freq.values.toList();
    counts.sort((a, b) => b.compareTo(a));
    int need = arr.length ~/ 2;
    int removed = 0;
    int setSize = 0;
    for (var c in counts) {
      if (removed >= need) break;
      removed += c;
      setSize++;
    }
    return setSize;
  }
}
```

## Golang

```go
import "sort"

func minSetSize(arr []int) int {
    freq := make(map[int]int)
    for _, v := range arr {
        freq[v]++
    }
    counts := make([]int, 0, len(freq))
    for _, c := range freq {
        counts = append(counts, c)
    }
    sort.Slice(counts, func(i, j int) bool { return counts[i] > counts[j] })
    target := len(arr) / 2
    removed, ans := 0, 0
    for _, c := range counts {
        if removed >= target {
            break
        }
        removed += c
        ans++
    }
    return ans
}
```

## Ruby

```ruby
def min_set_size(arr)
  freq = Hash.new(0)
  arr.each { |num| freq[num] += 1 }
  counts = freq.values.sort.reverse
  need = arr.length / 2
  removed = 0
  result = 0
  counts.each do |c|
    removed += c
    result += 1
    break if removed >= need
  end
  result
end
```

## Scala

```scala
object Solution {
    def minSetSize(arr: Array[Int]): Int = {
        val freq = scala.collection.mutable.Map[Int, Int]()
        arr.foreach { x =>
            freq.update(x, freq.getOrElse(x, 0) + 1)
        }
        val counts = freq.values.toArray.sorted(Ordering.Int.reverse)
        var removed = 0
        var setSize = 0
        val target = arr.length / 2
        while (removed < target && setSize < counts.length) {
            removed += counts(setSize)
            setSize += 1
        }
        setSize
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_set_size(arr: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        let n = arr.len();
        let mut freq: HashMap<i32, usize> = HashMap::new();
        for v in arr {
            *freq.entry(v).or_insert(0) += 1;
        }
        let mut counts: Vec<usize> = freq.values().cloned().collect();
        counts.sort_unstable_by(|a, b| b.cmp(a));
        let mut removed = 0usize;
        let mut ans = 0i32;
        for c in counts {
            removed += c;
            ans += 1;
            if removed >= n / 2 {
                break;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-set-size arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length arr))
         (freq (make-hash)))
    (for ([x arr])
      (hash-set! freq x (+ 1 (hash-ref freq x 0))))
    (define counts (sort (hash-values freq) >))
    (let loop ((removed 0) (set-size 0) (cs counts))
      (if (>= removed (quotient n 2))
          set-size
          (loop (+ removed (first cs)) (add1 set-size) (rest cs))))))
```

## Erlang

```erlang
-module(solution).
-export([min_set_size/1]).

-spec min_set_size(Arr :: [integer()]) -> integer().
min_set_size(Arr) ->
    FreqMap = freq_map(Arr, #{}),
    Counts = maps:values(FreqMap),
    Sorted = lists:sort(fun(A,B) -> A > B end, Counts),
    Half = length(Arr) div 2,
    min_needed(Sorted, 0, 0, Half).

freq_map([], Map) ->
    Map;
freq_map([H|T], Map) ->
    NewMap = maps:update_with(H, fun(C) -> C + 1 end, 1, Map),
    freq_map(T, NewMap).

min_needed(_, Removed, Used, Target) when Removed >= Target ->
    Used;
min_needed([Count|Rest], Removed, Used, Target) ->
    min_needed(Rest, Removed + Count, Used + 1, Target).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_set_size(arr :: [integer]) :: integer
  def min_set_size(arr) do
    freq_map =
      Enum.reduce(arr, %{}, fn x, acc ->
        Map.update(acc, x, 1, &(&1 + 1))
      end)

    freqs = freq_map |> Map.values() |> Enum.sort(&(>=/2))
    target = div(length(arr), 2)

    {count, _} =
      Enum.reduce_while(freqs, {0, 0}, fn f, {cnt, removed} ->
        new_removed = removed + f
        new_cnt = cnt + 1

        if new_removed >= target do
          {:halt, {new_cnt, new_removed}}
        else
          {:cont, {new_cnt, new_removed}}
        end
      end)

    count
  end
end
```
