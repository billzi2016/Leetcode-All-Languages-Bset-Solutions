# 1054. Distant Barcodes

## Cpp

```cpp
class Solution {
public:
    vector<int> rearrangeBarcodes(vector<int>& barcodes) {
        unordered_map<int,int> freq;
        for (int x : barcodes) ++freq[x];
        vector<pair<int,int>> vec;
        vec.reserve(freq.size());
        for (auto &p : freq) vec.emplace_back(p.second, p.first);
        sort(vec.begin(), vec.end(), [](const pair<int,int>& a, const pair<int,int>& b){
            return a.first > b.first;
        });
        int n = barcodes.size();
        vector<int> res(n);
        int idx = 0;
        for (auto &p : vec) {
            int cnt = p.first;
            int val = p.second;
            while (cnt--) {
                if (idx >= n) idx = 1;
                res[idx] = val;
                idx += 2;
            }
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] rearrangeBarcodes(int[] barcodes) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int b : barcodes) {
            freqMap.put(b, freqMap.getOrDefault(b, 0) + 1);
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[0] - a[0]); // [frequency, value]
        for (Map.Entry<Integer, Integer> e : freqMap.entrySet()) {
            pq.offer(new int[]{e.getValue(), e.getKey()});
        }

        int[] result = new int[barcodes.length];
        int idx = 0;

        while (pq.size() > 1) {
            int[] first = pq.poll();   // most frequent
            int[] second = pq.poll();  // second most frequent

            result[idx++] = first[1];
            result[idx++] = second[1];

            if (--first[0] > 0) {
                pq.offer(first);
            }
            if (--second[0] > 0) {
                pq.offer(second);
            }
        }

        if (!pq.isEmpty()) {
            int[] last = pq.poll();
            while (last[0]-- > 0) {
                result[idx++] = last[1];
            }
        }

        return result;
    }
}
```

## Python

```python
class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        import heapq

        freq = Counter(barcodes)
        # max-heap using negative counts
        heap = [(-cnt, val) for val, cnt in freq.items()]
        heapq.heapify(heap)

        result = []
        while heap:
            cnt1, val1 = heapq.heappop(heap)
            if not result or result[-1] != val1:
                result.append(val1)
                if cnt1 + 1 < 0:   # still have remaining occurrences
                    heapq.heappush(heap, (cnt1 + 1, val1))
            else:
                # need to use the next most frequent element
                cnt2, val2 = heapq.heappop(heap)
                result.append(val2)
                if cnt2 + 1 < 0:
                    heapq.heappush(heap, (cnt2 + 1, val2))
                # push back the first element for later use
                heapq.heappush(heap, (cnt1, val1))

        return result
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = Counter(barcodes)
        # sort values by descending frequency
        sorted_vals = sorted(freq.items(), key=lambda x: -x[1])
        n = len(barcodes)
        res = [0] * n
        idx = 0
        for val, cnt in sorted_vals:
            for _ in range(cnt):
                if idx >= n:
                    idx = 1  # switch to odd indices
                res[idx] = val
                idx += 2
        return res
```

## C

```c
#include <stdlib.h>

typedef struct {
    int val;
    int cnt;
} Pair;

static int cmp_pair(const void *a, const void *b) {
    const Pair *p1 = (const Pair *)a;
    const Pair *p2 = (const Pair *)b;
    return p2->cnt - p1->cnt;  // descending by count
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rearrangeBarcodes(int* barcodes, int barcodesSize, int* returnSize) {
    if (barcodesSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    // Frequency array since barcode values are <= 10000
    int maxVal = 10000;
    int *freq = (int *)calloc(maxVal + 1, sizeof(int));
    for (int i = 0; i < barcodesSize; ++i) {
        freq[barcodes[i]]++;
    }

    // Collect distinct values into pairs
    Pair *pairs = (Pair *)malloc(barcodesSize * sizeof(Pair));
    int pairCount = 0;
    for (int v = 1; v <= maxVal; ++v) {
        if (freq[v] > 0) {
            pairs[pairCount].val = v;
            pairs[pairCount].cnt = freq[v];
            pairCount++;
        }
    }

    // Sort by descending frequency
    qsort(pairs, pairCount, sizeof(Pair), cmp_pair);

    int *result = (int *)malloc(barcodesSize * sizeof(int));
    int idx = 0;  // start with even positions

    for (int i = 0; i < pairCount; ++i) {
        while (pairs[i].cnt > 0) {
            result[idx] = pairs[i].val;
            idx += 2;
            if (idx >= barcodesSize) {
                idx = 1; // switch to odd positions
            }
            pairs[i].cnt--;
        }
    }

    free(freq);
    free(pairs);

    *returnSize = barcodesSize;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] RearrangeBarcodes(int[] barcodes) {
        int n = barcodes.Length;
        var freq = new Dictionary<int, int>();
        foreach (int x in barcodes) {
            if (freq.ContainsKey(x)) freq[x]++;
            else freq[x] = 1;
        }
        var list = new List<(int val, int cnt)>();
        foreach (var kvp in freq) {
            list.Add((kvp.Key, kvp.Value));
        }
        list.Sort((a, b) => b.cnt.CompareTo(a.cnt)); // descending by count
        
        int[] res = new int[n];
        int idx = 0;
        foreach (var pair in list) {
            for (int i = 0; i < pair.cnt; i++) {
                if (idx >= n) idx = 1; // switch to odd positions
                res[idx] = pair.val;
                idx += 2;
            }
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} barcodes
 * @return {number[]}
 */
var rearrangeBarcodes = function(barcodes) {
    const freqMap = new Map();
    for (const num of barcodes) {
        freqMap.set(num, (freqMap.get(num) || 0) + 1);
    }
    const pairs = [];
    for (const [num, cnt] of freqMap.entries()) {
        pairs.push([num, cnt]);
    }
    // sort by descending frequency
    pairs.sort((a, b) => b[1] - a[1]);

    const n = barcodes.length;
    const result = new Array(n);
    let idx = 0;

    for (const [num, cnt] of pairs) {
        for (let i = 0; i < cnt; i++) {
            if (idx >= n) idx = 1; // switch to odd positions
            result[idx] = num;
            idx += 2;
        }
    }
    return result;
};
```

## Typescript

```typescript
function rearrangeBarcodes(barcodes: number[]): number[] {
    const freqMap = new Map<number, number>();
    for (const b of barcodes) {
        freqMap.set(b, (freqMap.get(b) ?? 0) + 1);
    }

    const entries: [number, number][] = [];
    for (const [val, cnt] of freqMap.entries()) {
        entries.push([val, cnt]);
    }
    // sort by descending frequency
    entries.sort((a, b) => b[1] - a[1]);

    const n = barcodes.length;
    const result: number[] = new Array(n);
    let idx = 0;

    for (const [val, cnt] of entries) {
        for (let i = 0; i < cnt; i++) {
            if (idx >= n) {
                idx = 1; // switch to odd positions
            }
            result[idx] = val;
            idx += 2;
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $barcodes
     * @return Integer[]
     */
    function rearrangeBarcodes($barcodes) {
        $freq = [];
        foreach ($barcodes as $b) {
            if (!isset($freq[$b])) {
                $freq[$b] = 0;
            }
            $freq[$b]++;
        }

        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        foreach ($freq as $val => $cnt) {
            $pq->insert([$val, $cnt], $cnt);
        }

        $result = [];
        while (!$pq->isEmpty()) {
            $first = $pq->extract();
            [$val1, $cnt1] = $first;

            if (empty($result) || end($result) !== $val1) {
                $result[] = $val1;
                $cnt1--;
                if ($cnt1 > 0) {
                    $pq->insert([$val1, $cnt1], $cnt1);
                }
            } else {
                // need the second most frequent
                $second = $pq->extract();
                [$val2, $cnt2] = $second;

                $result[] = $val2;
                $cnt2--;
                if ($cnt2 > 0) {
                    $pq->insert([$val2, $cnt2], $cnt2);
                }
                // push back the first element unchanged
                $pq->insert([$val1, $cnt1], $cnt1);
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func rearrangeBarcodes(_ barcodes: [Int]) -> [Int] {
        var freq = [Int:Int]()
        for b in barcodes {
            freq[b, default: 0] += 1
        }
        var pairs = [(value: Int, count: Int)]()
        pairs.reserveCapacity(freq.count)
        for (val, cnt) in freq {
            pairs.append((val, cnt))
        }
        pairs.sort { $0.count > $1.count }
        
        var result = Array(repeating: 0, count: barcodes.count)
        var idx = 0
        for pair in pairs {
            var remaining = pair.count
            while remaining > 0 {
                if idx >= barcodes.count {
                    idx = 1
                }
                result[idx] = pair.value
                idx += 2
                remaining -= 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rearrangeBarcodes(barcodes: IntArray): IntArray {
        val freqMap = HashMap<Int, Int>()
        for (code in barcodes) {
            freqMap[code] = (freqMap[code] ?: 0) + 1
        }
        val list = freqMap.entries.map { Pair(it.key, it.value) }
            .sortedWith(compareByDescending<Pair<Int, Int>> { it.second })
        val n = barcodes.size
        val result = IntArray(n)
        var idx = 0
        for ((value, count) in list) {
            repeat(count) {
                if (idx >= n) idx = 1
                result[idx] = value
                idx += 2
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> rearrangeBarcodes(List<int> barcodes) {
    int n = barcodes.length;
    final Map<int, int> freq = {};
    for (var x in barcodes) {
      freq[x] = (freq[x] ?? 0) + 1;
    }
    final entries = freq.entries.toList()
      ..sort((a, b) => b.value.compareTo(a.value));
    final List<int> res = List.filled(n, 0);
    int idx = 0;
    for (var e in entries) {
      int val = e.key;
      int cnt = e.value;
      while (cnt-- > 0) {
        if (idx >= n) idx = 1;
        res[idx] = val;
        idx += 2;
      }
    }
    return res;
  }
}
```

## Golang

```go
import "sort"

type pair struct {
	val int
	cnt int
}

func rearrangeBarcodes(barcodes []int) []int {
	freq := make(map[int]int)
	for _, v := range barcodes {
		freq[v]++
	}
	pairs := make([]pair, 0, len(freq))
	for k, c := range freq {
		pairs = append(pairs, pair{val: k, cnt: c})
	}
	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i].cnt > pairs[j].cnt
	})

	res := make([]int, len(barcodes))
	idx := 0
	for _, p := range pairs {
		for i := 0; i < p.cnt; i++ {
			if idx >= len(res) {
				idx = 1
			}
			res[idx] = p.val
			idx += 2
		}
	}
	return res
}
```

## Ruby

```ruby
def rearrange_barcodes(barcodes)
  freq = Hash.new(0)
  barcodes.each { |b| freq[b] += 1 }
  sorted = freq.sort_by { |val, cnt| -cnt }

  n = barcodes.length
  res = Array.new(n)
  idx = 0

  sorted.each do |val, cnt|
    cnt.times do
      res[idx] = val
      idx += 2
      idx = 1 if idx >= n
    end
  end

  res
end
```

## Scala

```scala
object Solution {
    def rearrangeBarcodes(barcodes: Array[Int]): Array[Int] = {
        val n = barcodes.length
        import scala.collection.mutable

        // Count frequencies
        val freqMap = mutable.Map[Int, Int]()
        for (b <- barcodes) {
            freqMap(b) = freqMap.getOrElse(b, 0) + 1
        }

        // Sort values by descending frequency and expand them according to their counts
        val sortedVals: Seq[Int] = freqMap.toSeq
          .sortBy { case (_, cnt) => -cnt }
          .flatMap { case (value, count) => List.fill(count)(value) }

        // Place values into result array at even indices first, then odd indices
        val result = new Array[Int](n)
        var idx = 0
        for (v <- sortedVals) {
            if (idx >= n) idx = 1
            result(idx) = v
            idx += 2
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn rearrange_barcodes(barcodes: Vec<i32>) -> Vec<i32> {
        use std::collections::HashMap;
        let mut freq: HashMap<i32, usize> = HashMap::new();
        for &b in &barcodes {
            *freq.entry(b).or_insert(0) += 1;
        }
        let mut pairs: Vec<(i32, usize)> = freq.into_iter().collect();
        pairs.sort_by(|a, b| b.1.cmp(&a.1)); // descending by count

        let n = barcodes.len();
        let mut res = vec![0; n];
        let mut idx = 0usize;
        for (val, cnt) in pairs {
            for _ in 0..cnt {
                if idx >= n {
                    idx = 1;
                }
                res[idx] = val;
                idx += 2;
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (rearrange-barcodes barcodes)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ([n (length barcodes)]
         [cnt (make-hash)])
    ;; count frequencies
    (for ([x barcodes])
      (hash-set! cnt x (+ 1 (hash-ref cnt x 0))))
    ;; sort values by descending frequency
    (define pairs
      (sort (hash->list cnt) (lambda (a b) (> (cdr a) (cdr b)))))
    ;; flatten into list repeated according to count
    (define flat
      (apply append
             (for/list ([p pairs])
               (let* ([val (car p)]
                      [c   (cdr p)])
                 (build-list c (lambda (_) val))))))
    ;; place values at even then odd indices
    (define res (make-vector n))
    (let loop ((idx 0) (lst flat))
      (cond [(null? lst) (void)]
            [else
             (when (>= idx n)
               (set! idx 1))
             (vector-set! res idx (car lst))
             (loop (+ idx 2) (cdr lst))]))
    (vector->list res)))
```

## Erlang

```erlang
-module(solution).
-export([rearrange_barcodes/1]).

-spec rearrange_barcodes([integer()]) -> [integer()].
rearrange_barcodes(Barcodes) ->
    FreqMap = count_freq(Barcodes, #{}),
    Heap0 = sorted_heap(FreqMap),
    rearrange_loop(Heap0, []).

count_freq([], M) -> M;
count_freq([H|T], M) ->
    NewM = maps:update_with(H,
                fun(C) -> C + 1 end,
                1,
                M),
    count_freq(T, NewM).

sorted_heap(FreqMap) ->
    lists:sort(fun({C1,_},{C2,_}) -> C1 > C2 end,
        [{Cnt, Val} || {Val,Cnt} <- maps:to_list(FreqMap)]).

rearrange_loop([], AccRev) ->
    lists:reverse(AccRev);
rearrange_loop([{C,V}], AccRev) when C >= 1 ->
    rearrange_loop([], [V | AccRev]);
rearrange_loop([{C1,V1},{C2,V2}|Rest], AccRev) ->
    Acc1 = [V2, V1 | AccRev],
    N1 = C1 - 1,
    N2 = C2 - 1,
    Heap1 = if N1 > 0 -> [{N1,V1} | Rest]; true -> Rest end,
    Heap2 = if N2 > 0 -> [{N2,V2} | Heap1]; true -> Heap1 end,
    NewHeap = lists:sort(fun({C_a,_},{C_b,_}) -> C_a > C_b end, Heap2),
    rearrange_loop(NewHeap, Acc1).
```

## Elixir

```elixir
defmodule Solution do
  @spec rearrange_barcodes(barcodes :: [integer]) :: [integer]
  def rearrange_barcodes(barcodes) do
    freq =
      Enum.reduce(barcodes, %{}, fn x, acc ->
        Map.update(acc, x, 1, &(&1 + 1))
      end)

    sorted =
      freq
      |> Map.to_list()
      |> Enum.sort_by(fn {_v, c} -> -c end)

    values =
      for {v, c} <- sorted, _ <- 1..c do
        v
      end

    n = length(barcodes)

    indices_even = for i <- 0..(n - 1), rem(i, 2) == 0, do: i
    indices_odd = for i <- 0..(n - 1), rem(i, 2) == 1, do: i
    indices = indices_even ++ indices_odd

    map =
      Enum.zip(indices, values)
      |> Enum.into(%{})

    for i <- 0..(n - 1) do
      Map.fetch!(map, i)
    end
  end
end
```
