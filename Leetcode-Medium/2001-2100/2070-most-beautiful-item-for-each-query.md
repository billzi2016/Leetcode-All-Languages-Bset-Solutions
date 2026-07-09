# 2070. Most Beautiful Item for Each Query

## Cpp

```cpp
class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        sort(items.begin(), items.end(),
             [](const vector<int>& a, const vector<int>& b) { return a[0] < b[0]; });
        
        int n = queries.size();
        vector<pair<int,int>> q;
        q.reserve(n);
        for (int i = 0; i < n; ++i) q.emplace_back(queries[i], i);
        sort(q.begin(), q.end());
        
        vector<int> ans(n);
        long long maxBeauty = 0;
        size_t it = 0;
        for (auto [price, idx] : q) {
            while (it < items.size() && items[it][0] <= price) {
                maxBeauty = max(maxBeauty, (long long)items[it][1]);
                ++it;
            }
            ans[idx] = (int)maxBeauty;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int[] maximumBeauty(int[][] items, int[] queries) {
        // Sort items by price
        Arrays.sort(items, (a, b) -> Integer.compare(a[0], b[0]));

        int n = queries.length;
        int[][] qIdx = new int[n][2];
        for (int i = 0; i < n; i++) {
            qIdx[i][0] = queries[i]; // price
            qIdx[i][1] = i;          // original index
        }

        // Sort queries by price
        Arrays.sort(qIdx, (a, b) -> Integer.compare(a[0], b[0]));

        int[] ans = new int[n];
        int maxBeauty = 0;
        int itemPtr = 0;

        for (int[] q : qIdx) {
            int price = q[0];
            while (itemPtr < items.length && items[itemPtr][0] <= price) {
                if (items[itemPtr][1] > maxBeauty) {
                    maxBeauty = items[itemPtr][1];
                }
                itemPtr++;
            }
            ans[q[1]] = maxBeauty;
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        # Sort items by price
        items.sort(key=lambda x: x[0])
        # Pair each query with its original index and sort by query value
        q_with_idx = sorted(((q, i) for i, q in enumerate(queries)), key=lambda x: x[0])

        ans = [0] * len(queries)
        max_beauty = 0
        item_ptr = 0
        n_items = len(items)

        for price_limit, orig_idx in q_with_idx:
            while item_ptr < n_items and items[item_ptr][0] <= price_limit:
                if items[item_ptr][1] > max_beauty:
                    max_beauty = items[item_ptr][1]
                item_ptr += 1
            ans[orig_idx] = max_beauty

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        q_with_idx = sorted([(price, i) for i, price in enumerate(queries)], key=lambda x: x[0])
        ans = [0] * len(queries)
        max_beauty = 0
        i = 0
        n = len(items)
        for price, idx in q_with_idx:
            while i < n and items[i][0] <= price:
                if items[i][1] > max_beauty:
                    max_beauty = items[i][1]
                i += 1
            ans[idx] = max_beauty
        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int price;
    int beauty;
} Item;

typedef struct {
    int price;
    int idx;
} Query;

static int cmpItem(const void *a, const void *b) {
    const Item *ia = (const Item *)a;
    const Item *ib = (const Item *)b;
    if (ia->price < ib->price) return -1;
    if (ia->price > ib->price) return 1;
    return 0;
}

static int cmpQuery(const void *a, const void *b) {
    const Query *qa = (const Query *)a;
    const Query *qb = (const Query *)b;
    if (qa->price < qb->price) return -1;
    if (qa->price > qb->price) return 1;
    return 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maximumBeauty(int** items, int itemsSize, int* itemsColSize, int* queries, int queriesSize, int* returnSize) {
    Item *its = (Item *)malloc(itemsSize * sizeof(Item));
    for (int i = 0; i < itemsSize; ++i) {
        its[i].price = items[i][0];
        its[i].beauty = items[i][1];
    }
    qsort(its, itemsSize, sizeof(Item), cmpItem);
    
    Query *qs = (Query *)malloc(queriesSize * sizeof(Query));
    for (int i = 0; i < queriesSize; ++i) {
        qs[i].price = queries[i];
        qs[i].idx = i;
    }
    qsort(qs, queriesSize, sizeof(Query), cmpQuery);
    
    int *ans = (int *)malloc(queriesSize * sizeof(int));
    int maxBeauty = 0;
    int itemIdx = 0;
    for (int i = 0; i < queriesSize; ++i) {
        int curPrice = qs[i].price;
        while (itemIdx < itemsSize && its[itemIdx].price <= curPrice) {
            if (its[itemIdx].beauty > maxBeauty)
                maxBeauty = its[itemIdx].beauty;
            ++itemIdx;
        }
        ans[qs[i].idx] = maxBeauty;
    }
    
    free(its);
    free(qs);
    
    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] MaximumBeauty(int[][] items, int[] queries)
    {
        // Sort items by price ascending
        Array.Sort(items, (a, b) => a[0].CompareTo(b[0]));

        int n = queries.Length;
        var sortedQueries = new (int value, int index)[n];
        for (int i = 0; i < n; i++)
            sortedQueries[i] = (queries[i], i);

        // Sort queries by their price values
        Array.Sort(sortedQueries, (a, b) => a.value.CompareTo(b.value));

        int[] answer = new int[n];
        int itemIdx = 0;
        int maxBeauty = 0;

        foreach (var (value, idx) in sortedQueries)
        {
            while (itemIdx < items.Length && items[itemIdx][0] <= value)
            {
                if (items[itemIdx][1] > maxBeauty)
                    maxBeauty = items[itemIdx][1];
                itemIdx++;
            }
            answer[idx] = maxBeauty;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} items
 * @param {number[]} queries
 * @return {number[]}
 */
var maximumBeauty = function(items, queries) {
    // Sort items by price
    items.sort((a, b) => a[0] - b[0]);

    const n = items.length;
    const prices = new Array(n);
    const prefMax = new Array(n);
    let curMax = 0;

    for (let i = 0; i < n; ++i) {
        const [p, b] = items[i];
        prices[i] = p;
        if (b > curMax) curMax = b;
        prefMax[i] = curMax;
    }

    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        const q = queries[i];
        // binary search for last price <= q
        let l = 0, r = n - 1, idx = -1;
        while (l <= r) {
            const mid = (l + r) >> 1;
            if (prices[mid] <= q) {
                idx = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        ans[i] = idx === -1 ? 0 : prefMax[idx];
    }

    return ans;
};
```

## Typescript

```typescript
function maximumBeauty(items: number[][], queries: number[]): number[] {
    // Sort items by price ascending
    items.sort((a, b) => a[0] - b[0]);

    // Pair each query with its original index and sort by query value
    const qWithIdx: [number, number][] = queries.map((v, i) => [v, i]);
    qWithIdx.sort((a, b) => a[0] - b[0]);

    const ans: number[] = new Array(queries.length);
    let maxBeauty = 0;
    let itemIdx = 0;

    for (const [price, originalIdx] of qWithIdx) {
        while (itemIdx < items.length && items[itemIdx][0] <= price) {
            if (items[itemIdx][1] > maxBeauty) {
                maxBeauty = items[itemIdx][1];
            }
            itemIdx++;
        }
        ans[originalIdx] = maxBeauty;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $items
     * @param Integer[] $queries
     * @return Integer[]
     */
    function maximumBeauty($items, $queries) {
        // Sort items by price ascending
        usort($items, function($a, $b) {
            return $a[0] <=> $b[0];
        });

        // Pair each query with its original index
        $qWithIdx = [];
        foreach ($queries as $idx => $val) {
            $qWithIdx[] = [$val, $idx];
        }
        // Sort queries by price ascending
        usort($qWithIdx, function($a, $b) {
            return $a[0] <=> $b[0];
        });

        $ans = array_fill(0, count($queries), 0);
        $itemPos = 0;
        $maxBeauty = 0;
        $nItems = count($items);

        foreach ($qWithIdx as $pair) {
            $priceLimit = $pair[0];
            $origIdx = $pair[1];

            while ($itemPos < $nItems && $items[$itemPos][0] <= $priceLimit) {
                if ($items[$itemPos][1] > $maxBeauty) {
                    $maxBeauty = $items[$itemPos][1];
                }
                $itemPos++;
            }

            $ans[$origIdx] = $maxBeauty;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumBeauty(_ items: [[Int]], _ queries: [Int]) -> [Int] {
        let sortedItems = items.sorted { $0[0] < $1[0] }
        var queryPairs: [(value: Int, idx: Int)] = []
        for (i, q) in queries.enumerated() {
            queryPairs.append((q, i))
        }
        queryPairs.sort { $0.value < $1.value }
        
        var ans = Array(repeating: 0, count: queries.count)
        var maxBeauty = 0
        var itemIdx = 0
        let nItems = sortedItems.count
        
        for qp in queryPairs {
            while itemIdx < nItems && sortedItems[itemIdx][0] <= qp.value {
                if sortedItems[itemIdx][1] > maxBeauty {
                    maxBeauty = sortedItems[itemIdx][1]
                }
                itemIdx += 1
            }
            ans[qp.idx] = maxBeauty
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumBeauty(items: Array<IntArray>, queries: IntArray): IntArray {
        // Sort items by price ascending
        items.sortWith(compareBy { it[0] })
        val n = queries.size

        data class Query(val price: Int, val idx: Int)

        // Pair each query with its original index and sort by price
        val sortedQueries = Array(n) { i -> Query(queries[i], i) }
        sortedQueries.sortWith(compareBy { it.price })

        var itemIdx = 0
        var maxBeauty = 0
        val answer = IntArray(n)

        for (q in sortedQueries) {
            while (itemIdx < items.size && items[itemIdx][0] <= q.price) {
                if (items[itemIdx][1] > maxBeauty) {
                    maxBeauty = items[itemIdx][1]
                }
                itemIdx++
            }
            answer[q.idx] = maxBeauty
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> maximumBeauty(List<List<int>> items, List<int> queries) {
    // Sort items by price
    items.sort((a, b) => a[0].compareTo(b[0]));

    // Pair each query with its original index
    List<List<int>> qWithIdx = List.generate(
        queries.length, (i) => [queries[i], i],
        growable: false);

    // Sort queries by price
    qWithIdx.sort((a, b) => a[0].compareTo(b[0]));

    int nItems = items.length;
    int itemIdx = 0;
    int maxBeauty = 0;

    List<int> ans = List.filled(queries.length, 0);

    for (var q in qWithIdx) {
      int priceLimit = q[0];
      int originalIdx = q[1];

      while (itemIdx < nItems && items[itemIdx][0] <= priceLimit) {
        if (items[itemIdx][1] > maxBeauty) {
          maxBeauty = items[itemIdx][1];
        }
        itemIdx++;
      }

      ans[originalIdx] = maxBeauty;
    }

    return ans;
  }
}
```

## Golang

```go
import "sort"

func maximumBeauty(items [][]int, queries []int) []int {
	sort.Slice(items, func(i, j int) bool { return items[i][0] < items[j][0] })
	type query struct{ price, idx int }
	qs := make([]query, len(queries))
	for i, v := range queries {
		qs[i] = query{price: v, idx: i}
	}
	sort.Slice(qs, func(i, j int) bool { return qs[i].price < qs[j].price })
	ans := make([]int, len(queries))
	maxB, itemIdx := 0, 0
	for _, q := range qs {
		for itemIdx < len(items) && items[itemIdx][0] <= q.price {
			if items[itemIdx][1] > maxB {
				maxB = items[itemIdx][1]
			}
			itemIdx++
		}
		ans[q.idx] = maxB
	}
	return ans
}
```

## Ruby

```ruby
def maximum_beauty(items, queries)
  items.sort_by! { |price, _| price }
  q_with_idx = queries.each_with_index.map { |q, i| [q, i] }
  q_with_idx.sort_by! { |price, _| price }

  ans = Array.new(queries.length, 0)
  max_beauty = 0
  i = 0

  q_with_idx.each do |query_price, original_idx|
    while i < items.length && items[i][0] <= query_price
      max_beauty = [max_beauty, items[i][1]].max
      i += 1
    end
    ans[original_idx] = max_beauty
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maximumBeauty(items: Array[Array[Int]], queries: Array[Int]): Array[Int] = {
        // Sort items by price
        val sortedItems = items.sortBy(_(0))
        // Pair each query with its original index and sort by query value
        val qWithIdx = queries.zipWithIndex.sortBy(_._1)

        val ans = new Array[Int](queries.length)
        var itemPtr = 0
        var maxBeauty = 0

        for ((price, idx) <- qWithIdx) {
            while (itemPtr < sortedItems.length && sortedItems(itemPtr)(0) <= price) {
                if (sortedItems(itemPtr)(1) > maxBeauty) {
                    maxBeauty = sortedItems(itemPtr)(1)
                }
                itemPtr += 1
            }
            ans(idx) = maxBeauty
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_beauty(items: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        // Convert items to (price, beauty) tuples and sort by price
        let mut items_vec: Vec<(i32, i32)> = items.into_iter().map(|v| (v[0], v[1])).collect();
        items_vec.sort_by_key(|&(price, _)| price);

        // Pair each query with its original index and sort by query value
        let mut queries_with_idx: Vec<(i32, usize)> = queries
            .iter()
            .cloned()
            .enumerate()
            .map(|(idx, q)| (q, idx))
            .collect();
        queries_with_idx.sort_by_key(|&(price, _)| price);

        let mut answer = vec![0; queries.len()];
        let mut max_beauty = 0;
        let mut item_ptr = 0usize;

        for &(query_price, original_idx) in &queries_with_idx {
            while item_ptr < items_vec.len() && items_vec[item_ptr].0 <= query_price {
                if items_vec[item_ptr].1 > max_beauty {
                    max_beauty = items_vec[item_ptr].1;
                }
                item_ptr += 1;
            }
            answer[original_idx] = max_beauty;
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (maximum-beauty items queries)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?))
  (let* ((sorted-items (sort items (lambda (a b) (< (first a) (first b)))))
         (items-vec   (list->vector sorted-items))
         (n           (length queries))
         (queries-with-index
          (for/list ([q queries] [i (in-naturals)]) (list q i)))
         (sorted-queries (sort queries-with-index (lambda (a b) (< (first a) (first b))))))
    (let ((ans        (make-vector n))
          (item-idx   0)
          (max-beauty 0)
          (m          (vector-length items-vec)))
      (for ([q-pair sorted-queries])
        (define q-price (first q-pair))
        (define orig-idx (second q-pair))
        (let loop ()
          (when (and (< item-idx m)
                     (<= (first (vector-ref items-vec item-idx)) q-price))
            (set! max-beauty
                  (max max-beauty (second (vector-ref items-vec item-idx))))
            (set! item-idx (+ item-idx 1))
            (loop)))
        (vector-set! ans orig-idx max-beauty))
      (let loop ((i (- n 1)) (res '()))
        (if (< i 0)
            res
            (loop (- i 1) (cons (vector-ref ans i) res)))))))
```

## Erlang

```erlang
-spec maximum_beauty(Items :: [[integer()]], Queries :: [integer()]) -> [integer()].
maximum_beauty(Items, Queries) ->
    ItemTuples = [{P, B} || [P, B] <- Items],
    SortedItems = lists:sort(ItemTuples),
    Indices = lists:seq(0, length(Queries) - 1),
    IndexedQueries0 = [{Q, Idx} || {Q, Idx} <- lists:zip(Queries, Indices)],
    SortedQueries = lists:sort(IndexedQueries0),
    AnswerPairs = process(SortedItems, SortedQueries, 0, []),
    SortedAns = lists:keysort(1, AnswerPairs),
    [Ans || {_Idx, Ans} <- SortedAns].

process([], Queries, MaxBeauty, Acc) ->
    Remaining = [{Idx, MaxBeauty} || {_, Idx} <- Queries],
    Remaining ++ Acc;
process(_, [], _MaxBeauty, Acc) ->
    Acc;
process(Items = [{P, B} | RestItems], Queries = [{Q, Idx} | RestQueries], MaxBeauty, Acc) ->
    if
        P =< Q ->
            NewMax = erlang:max(MaxBeauty, B),
            process(RestItems, Queries, NewMax, Acc);
        true ->
            process(Items, RestQueries, MaxBeauty, [{Idx, MaxBeauty} | Acc])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_beauty(items :: [[integer]], queries :: [integer]) :: [integer]
  def maximum_beauty(items, queries) do
    sorted_items =
      Enum.sort_by(items, fn [price, _beauty] -> price end)

    sorted_queries =
      queries
      |> Enum.with_index()
      |> Enum.map(fn {q, i} -> {q, i} end)
      |> Enum.sort_by(fn {q, _i} -> q end)

    pairs = process(sorted_queries, sorted_items, 0, [])
    answers_map = Enum.into(pairs, %{})
    n = length(queries)

    for i <- 0..(n - 1), do: Map.get(answers_map, i)
  end

  defp process([], _items, _max_beauty, acc), do: Enum.reverse(acc)

  defp process([{q_price, q_idx} | rest_q], items, cur_max, acc) do
    {remaining_items, new_max} = consume(items, q_price, cur_max)
    process(rest_q, remaining_items, new_max, [{q_idx, new_max} | acc])
  end

  defp consume([], _limit, max_beauty), do: {[], max_beauty}

  defp consume([[price, beauty] | rest] = items, limit, cur_max) when price <= limit do
    next_max = if beauty > cur_max, do: beauty, else: cur_max
    consume(rest, limit, next_max)
  end

  defp consume(items, _limit, max_beauty), do: {items, max_beauty}
end
```
