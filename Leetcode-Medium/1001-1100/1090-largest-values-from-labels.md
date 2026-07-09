# 1090. Largest Values From Labels

## Cpp

```cpp
class Solution {
public:
    int largestValsFromLabels(vector<int>& values, vector<int>& labels, int numWanted, int useLimit) {
        int n = values.size();
        vector<pair<int,int>> items;
        items.reserve(n);
        for (int i = 0; i < n; ++i) {
            items.emplace_back(values[i], labels[i]);
        }
        sort(items.begin(), items.end(),
             [](const pair<int,int>& a, const pair<int,int>& b){ return a.first > b.first; });
        
        unordered_map<int,int> cnt;
        int taken = 0;
        long long sum = 0;
        for (auto& it : items) {
            if (taken == numWanted) break;
            int val = it.first, lab = it.second;
            if (cnt[lab] < useLimit) {
                sum += val;
                ++cnt[lab];
                ++taken;
            }
        }
        return static_cast<int>(sum);
    }
};
```

## Java

```java
class Solution {
    public int largestValsFromLabels(int[] values, int[] labels, int numWanted, int useLimit) {
        int n = values.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        java.util.Arrays.sort(idx, (a, b) -> Integer.compare(values[b], values[a]));
        
        java.util.HashMap<Integer, Integer> count = new java.util.HashMap<>();
        int taken = 0;
        int sum = 0;
        for (int i : idx) {
            if (taken == numWanted) break;
            int label = labels[i];
            int cur = count.getOrDefault(label, 0);
            if (cur < useLimit) {
                sum += values[i];
                taken++;
                count.put(label, cur + 1);
            }
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type numWanted: int
        :type useLimit: int
        :rtype: int
        """
        # Pair each value with its label and sort by value descending
        items = sorted(zip(values, labels), key=lambda x: -x[0])
        count = {}
        total = 0
        taken = 0

        for val, lab in items:
            if taken >= numWanted:
                break
            used = count.get(lab, 0)
            if used < useLimit:
                total += val
                taken += 1
                count[lab] = used + 1

        return total
```

## Python3

```python
from typing import List
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), key=lambda x: -x[0])
        label_count = {}
        total = 0
        taken = 0
        for val, lab in items:
            if taken == numWanted:
                break
            cnt = label_count.get(lab, 0)
            if cnt < useLimit:
                total += val
                taken += 1
                label_count[lab] = cnt + 1
        return total
```

## C

```c
#include <stdlib.h>

typedef struct {
    int value;
    int label;
} Item;

static int cmpDesc(const void *a, const void *b) {
    int va = ((Item *)a)->value;
    int vb = ((Item *)b)->value;
    return vb - va;  // descending order
}

int largestValsFromLabels(int* values, int valuesSize, int* labels, int labelsSize, int numWanted, int useLimit) {
    int n = valuesSize;
    Item *items = (Item *)malloc(n * sizeof(Item));
    int maxLabel = 0;
    for (int i = 0; i < n; ++i) {
        items[i].value = values[i];
        items[i].label = labels[i];
        if (labels[i] > maxLabel) maxLabel = labels[i];
    }

    qsort(items, n, sizeof(Item), cmpDesc);

    int *cnt = (int *)calloc(maxLabel + 1, sizeof(int));
    long long sum = 0;
    int taken = 0;

    for (int i = 0; i < n && taken < numWanted; ++i) {
        int lab = items[i].label;
        if (cnt[lab] < useLimit) {
            sum += items[i].value;
            cnt[lab]++;
            taken++;
        }
    }

    free(items);
    free(cnt);
    return (int)sum;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int LargestValsFromLabels(int[] values, int[] labels, int numWanted, int useLimit) {
        int n = values.Length;
        var items = new List<(int val, int lbl)>(n);
        for (int i = 0; i < n; i++) {
            items.Add((values[i], labels[i]));
        }
        items.Sort((a, b) => b.val.CompareTo(a.val)); // descending by value

        var used = new Dictionary<int, int>();
        int taken = 0;
        int sum = 0;

        foreach (var item in items) {
            if (taken >= numWanted) break;
            int cnt = 0;
            if (used.TryGetValue(item.lbl, out cnt) && cnt >= useLimit) continue;
            // take this item
            sum += item.val;
            taken++;
            used[item.lbl] = cnt + 1;
        }

        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} values
 * @param {number[]} labels
 * @param {number} numWanted
 * @param {number} useLimit
 * @return {number}
 */
var largestValsFromLabels = function(values, labels, numWanted, useLimit) {
    const items = [];
    for (let i = 0; i < values.length; ++i) {
        items.push({ v: values[i], l: labels[i] });
    }
    items.sort((a, b) => b.v - a.v);
    
    const usedCount = Object.create(null);
    let taken = 0;
    let sum = 0;
    
    for (const {v, l} of items) {
        if (taken >= numWanted) break;
        const cnt = usedCount[l] || 0;
        if (cnt < useLimit) {
            sum += v;
            usedCount[l] = cnt + 1;
            ++taken;
        }
    }
    
    return sum;
};
```

## Typescript

```typescript
function largestValsFromLabels(values: number[], labels: number[], numWanted: number, useLimit: number): number {
    const items = values.map((v, i) => ({ value: v, label: labels[i] }));
    items.sort((a, b) => b.value - a.value);
    const labelCount = new Map<number, number>();
    let selected = 0;
    let sum = 0;
    for (const { value, label } of items) {
        if (selected === numWanted) break;
        const cnt = labelCount.get(label) ?? 0;
        if (cnt < useLimit) {
            sum += value;
            selected++;
            labelCount.set(label, cnt + 1);
        }
    }
    return sum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $values
     * @param Integer[] $labels
     * @param Integer $numWanted
     * @param Integer $useLimit
     * @return Integer
     */
    function largestValsFromLabels($values, $labels, $numWanted, $useLimit) {
        $n = count($values);
        $items = [];
        for ($i = 0; $i < $n; $i++) {
            $items[] = [$values[$i], $labels[$i]];
        }
        usort($items, function($a, $b) {
            return $b[0] <=> $a[0];
        });
        $cnt = [];
        $total = 0;
        $taken = 0;
        foreach ($items as $item) {
            if ($taken >= $numWanted) {
                break;
            }
            [$val, $lab] = $item;
            $cur = $cnt[$lab] ?? 0;
            if ($cur < $useLimit) {
                $total += $val;
                $cnt[$lab] = $cur + 1;
                $taken++;
            }
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func largestValsFromLabels(_ values: [Int], _ labels: [Int], _ numWanted: Int, _ useLimit: Int) -> Int {
        let n = values.count
        var items = [(value: Int, label: Int)]()
        items.reserveCapacity(n)
        for i in 0..<n {
            items.append((values[i], labels[i]))
        }
        items.sort { $0.value > $1.value }
        
        var labelCount = [Int: Int]()
        var taken = 0
        var sum = 0
        
        for item in items {
            if taken == numWanted { break }
            let cnt = labelCount[item.label] ?? 0
            if cnt < useLimit {
                sum += item.value
                taken += 1
                labelCount[item.label] = cnt + 1
            }
        }
        return sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestValsFromLabels(values: IntArray, labels: IntArray, numWanted: Int, useLimit: Int): Int {
        val items = values.indices.map { i -> intArrayOf(values[i], labels[i]) }
            .sortedWith(compareByDescending<IntArray> { it[0] })
        val labelCount = HashMap<Int, Int>()
        var selected = 0
        var total = 0L
        for (item in items) {
            if (selected == numWanted) break
            val label = item[1]
            val cnt = labelCount.getOrDefault(label, 0)
            if (cnt < useLimit) {
                total += item[0].toLong()
                selected++
                labelCount[label] = cnt + 1
            }
        }
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int largestValsFromLabels(List<int> values, List<int> labels, int numWanted, int useLimit) {
    int n = values.length;
    List<int> idx = List.generate(n, (i) => i);
    idx.sort((a, b) => values[b].compareTo(values[a])); // descending by value

    Map<int, int> used = {};
    int sum = 0;
    int taken = 0;

    for (int i in idx) {
      if (taken == numWanted) break;
      int label = labels[i];
      int cnt = used[label] ?? 0;
      if (cnt < useLimit) {
        sum += values[i];
        taken++;
        used[label] = cnt + 1;
      }
    }

    return sum;
  }
}
```

## Golang

```go
package main

import "sort"

func largestValsFromLabels(values []int, labels []int, numWanted int, useLimit int) int {
	n := len(values)
	items := make([]struct{ value, label int }, n)
	for i := 0; i < n; i++ {
		items[i] = struct{ value, label int }{values[i], labels[i]}
	}
	sort.Slice(items, func(i, j int) bool {
		return items[i].value > items[j].value
	})

	count := make(map[int]int)
	sum := 0
	selected := 0

	for _, it := range items {
		if selected >= numWanted {
			break
		}
		if count[it.label] < useLimit {
			sum += it.value
			count[it.label]++
			selected++
		}
	}
	return sum
}
```

## Ruby

```ruby
def largest_vals_from_labels(values, labels, num_wanted, use_limit)
  items = values.each_with_index.map { |v, i| [v, labels[i]] }
  items.sort_by! { |v, _| -v }

  count = Hash.new(0)
  total = 0
  taken = 0

  items.each do |value, label|
    break if taken == num_wanted
    next if count[label] >= use_limit

    total += value
    count[label] += 1
    taken += 1
  end

  total
end
```

## Scala

```scala
object Solution {
    def largestValsFromLabels(values: Array[Int], labels: Array[Int], numWanted: Int, useLimit: Int): Int = {
        val items = values.zip(labels).sortBy(-_._1)
        val count = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
        var total = 0
        var taken = 0
        for ((v, l) <- items if taken < numWanted) {
            if (count(l) < useLimit) {
                total += v
                taken += 1
                count(l) = count(l) + 1
            }
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_vals_from_labels(values: Vec<i32>, labels: Vec<i32>, num_wanted: i32, use_limit: i32) -> i32 {
        let mut items: Vec<(i32, i32)> = values.into_iter().zip(labels.into_iter()).collect();
        items.sort_by(|a, b| b.0.cmp(&a.0));
        use std::collections::HashMap;
        let mut used: HashMap<i32, i32> = HashMap::new();
        let mut total: i64 = 0;
        let mut taken = 0;
        for (value, label) in items {
            if taken >= num_wanted {
                break;
            }
            let cnt = *used.get(&label).unwrap_or(&0);
            if cnt < use_limit {
                total += value as i64;
                used.insert(label, cnt + 1);
                taken += 1;
            }
        }
        total as i32
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (largest-vals-from-labels values labels numWanted useLimit)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((pairs (map cons values labels))
         (sorted-pairs (sort pairs (lambda (a b) (> (car a) (car b))))))
    (let loop ((remaining sorted-pairs)
               (selected 0)
               (sum 0)
               (counts (make-hash)))
      (if (or (= selected numWanted) (null? remaining))
          sum
          (let* ((pair (car remaining))
                 (val (car pair))
                 (lab (cdr pair))
                 (cnt (hash-ref counts lab 0)))
            (if (< cnt useLimit)
                (begin
                  (hash-set! counts lab (+ cnt 1))
                  (loop (cdr remaining) (+ selected 1) (+ sum val) counts))
                (loop (cdr remaining) selected sum counts)))))))
```

## Erlang

```erlang
-module(solution).
-export([largest_vals_from_labels/4]).

largest_vals_from_labels(Values, Labels, NumWanted, UseLimit) ->
    Items = lists:zip(Values, Labels),
    Sorted = lists:reverse(lists:keysort(1, Items)),
    select(Sorted, NumWanted, UseLimit, 0, 0, #{}).

select(_, NumWanted, _UseLimit, Sum, Count, _) when Count >= NumWanted ->
    Sum;
select([], _NumWanted, _UseLimit, Sum, _Count, _Map) ->
    Sum;
select([{Val, Lab}|Rest], NumWanted, UseLimit, Sum, Count, Map) ->
    Used = maps:get(Lab, Map, 0),
    if
        Used < UseLimit andalso Count < NumWanted ->
            NewMap = maps:put(Lab, Used + 1, Map),
            select(Rest, NumWanted, UseLimit, Sum + Val, Count + 1, NewMap);
        true ->
            select(Rest, NumWanted, UseLimit, Sum, Count, Map)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_vals_from_labels(values :: [integer], labels :: [integer], num_wanted :: integer, use_limit :: integer) :: integer
  def largest_vals_from_labels(values, labels, num_wanted, use_limit) do
    items =
      Enum.zip(values, labels)
      |> Enum.sort_by(fn {v, _} -> v end, :desc)

    result =
      Enum.reduce_while(items, {0, %{}, 0}, fn {value, label},
                                            {sum, cnts, taken} ->
        if taken == num_wanted do
          {:halt, sum}
        else
          used = Map.get(cnts, label, 0)

          if used < use_limit do
            {:cont,
             {sum + value, Map.put(cnts, label, used + 1), taken + 1}}
          else
            {:cont, {sum, cnts, taken}}
          end
        end
      end)

    case result do
      sum when is_integer(sum) -> sum
      {sum, _cnts, _taken} -> sum
    end
  end
end
```
