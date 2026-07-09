# 0347. Top K Frequent Elements

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> freq;
        for (int x : nums) ++freq[x];
        
        int n = nums.size();
        vector<vector<int>> bucket(n + 1);
        for (auto &p : freq) {
            bucket[p.second].push_back(p.first);
        }
        
        vector<int> result;
        for (int i = n; i >= 0 && (int)result.size() < k; --i) {
            for (int num : bucket[i]) {
                result.push_back(num);
                if ((int)result.size() == k) break;
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
    public int[] topKFrequent(int[] nums, int k) {
        // Count frequencies
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Bucket sort by frequency
        @SuppressWarnings("unchecked")
        List<Integer>[] buckets = new List[nums.length + 1];
        for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
            int num = entry.getKey();
            int freq = entry.getValue();
            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }
            buckets[freq].add(num);
        }

        // Gather top k frequent elements
        int[] result = new int[k];
        int idx = 0;
        for (int i = buckets.length - 1; i >= 0 && idx < k; i--) {
            List<Integer> bucket = buckets[i];
            if (bucket != null) {
                for (int num : bucket) {
                    result[idx++] = num;
                    if (idx == k) break;
                }
            }
        }

        return result;
    }
}
```

## Python

```python
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        import heapq

        freq = Counter(nums)
        return [num for num, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]
```

## Python3

```python
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        for num, cnt in freq.items():
            buckets[cnt].append(num)

        res: List[int] = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

typedef struct {
    int freq;
    int val;
} Pair;

static void heap_swap(Pair *a, Pair *b) {
    Pair tmp = *a;
    *a = *b;
    *b = tmp;
}

/* push into min-heap */
static void heap_push(Pair *heap, int *size, Pair p) {
    int i = (*size);
    heap[i] = p;
    while (i > 0) {
        int parent = (i - 1) >> 1;
        if (heap[parent].freq <= heap[i].freq) break;
        heap_swap(&heap[parent], &heap[i]);
        i = parent;
    }
    (*size)++;
}

/* replace root and heapify down */
static void heap_replace_root(Pair *heap, int size, Pair p) {
    heap[0] = p;
    int i = 0;
    while (1) {
        int left = (i << 1) + 1;
        int right = left + 1;
        int smallest = i;
        if (left < size && heap[left].freq < heap[smallest].freq)
            smallest = left;
        if (right < size && heap[right].freq < heap[smallest].freq)
            smallest = right;
        if (smallest == i) break;
        heap_swap(&heap[i], &heap[smallest]);
        i = smallest;
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* topKFrequent(int* nums, int numsSize, int k, int* returnSize) {
    if (numsSize == 0 || k == 0) {
        *returnSize = 0;
        return NULL;
    }

    qsort(nums, numsSize, sizeof(int), cmp_int);

    int *uniqVals = (int *)malloc(numsSize * sizeof(int));
    int *uniqFreqs = (int *)malloc(numsSize * sizeof(int));
    int uniqCount = 0;

    for (int i = 0; i < numsSize;) {
        int val = nums[i];
        int cnt = 1;
        while (i + cnt < numsSize && nums[i + cnt] == val) cnt++;
        uniqVals[uniqCount] = val;
        uniqFreqs[uniqCount] = cnt;
        uniqCount++;
        i += cnt;
    }

    Pair *heap = (Pair *)malloc(k * sizeof(Pair));
    int heapSize = 0;

    for (int i = 0; i < uniqCount; ++i) {
        Pair p = {uniqFreqs[i], uniqVals[i]};
        if (heapSize < k) {
            heap_push(heap, &heapSize, p);
        } else if (p.freq > heap[0].freq) {
            heap_replace_root(heap, heapSize, p);
        }
    }

    int *res = (int *)malloc(k * sizeof(int));
    for (int i = 0; i < k; ++i) {
        res[i] = heap[i].val;
    }

    *returnSize = k;

    free(uniqVals);
    free(uniqFreqs);
    free(heap);
    return res;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var freq = new Dictionary<int, int>();
        foreach (int num in nums) {
            if (freq.ContainsKey(num))
                freq[num]++;
            else
                freq[num] = 1;
        }

        int n = nums.Length;
        List<int>[] buckets = new List<int>[n + 1];
        foreach (var kvp in freq) {
            int f = kvp.Value;
            if (buckets[f] == null)
                buckets[f] = new List<int>();
            buckets[f].Add(kvp.Key);
        }

        var result = new List<int>(k);
        for (int i = n; i >= 0 && result.Count < k; i--) {
            if (buckets[i] != null) {
                foreach (int val in buckets[i]) {
                    result.Add(val);
                    if (result.Count == k)
                        break;
                }
            }
        }

        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const freqMap = new Map();
    for (const num of nums) {
        freqMap.set(num, (freqMap.get(num) || 0) + 1);
    }
    
    const n = nums.length;
    const buckets = Array.from({ length: n + 1 }, () => []);
    
    for (const [num, freq] of freqMap.entries()) {
        buckets[freq].push(num);
    }
    
    const result = [];
    for (let i = n; i >= 0 && result.length < k; i--) {
        if (buckets[i].length) {
            for (const num of buckets[i]) {
                result.push(num);
                if (result.length === k) break;
            }
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function topKFrequent(nums: number[], k: number): number[] {
    const freq = new Map<number, number>();
    for (const n of nums) {
        freq.set(n, (freq.get(n) ?? 0) + 1);
    }

    const buckets: number[][] = Array.from({ length: nums.length + 1 }, () => []);
    for (const [num, count] of freq.entries()) {
        buckets[count].push(num);
    }

    const result: number[] = [];
    for (let i = buckets.length - 1; i >= 0 && result.length < k; i--) {
        if (buckets[i].length) {
            for (const num of buckets[i]) {
                result.push(num);
                if (result.length === k) break;
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
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function topKFrequent($nums, $k) {
        // Count frequencies
        $freq = [];
        foreach ($nums as $num) {
            if (!isset($freq[$num])) {
                $freq[$num] = 0;
            }
            $freq[$num]++;
        }

        $n = count($nums);
        // Bucket where index is frequency
        $bucket = array_fill(0, $n + 1, []);
        foreach ($freq as $num => $cnt) {
            $bucket[$cnt][] = (int)$num;
        }

        $result = [];
        for ($i = $n; $i >= 0 && count($result) < $k; $i--) {
            if (!empty($bucket[$i])) {
                foreach ($bucket[$i] as $val) {
                    $result[] = $val;
                    if (count($result) == $k) {
                        break 2;
                    }
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var freq = [Int:Int]()
        for num in nums {
            freq[num, default: 0] += 1
        }
        
        let n = nums.count
        var buckets = Array(repeating: [Int](), count: n + 1)
        for (num, count) in freq {
            buckets[count].append(num)
        }
        
        var result = [Int]()
        var i = n
        while i >= 0 && result.count < k {
            if !buckets[i].isEmpty {
                for num in buckets[i] {
                    result.append(num)
                    if result.count == k { break }
                }
            }
            i -= 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        val freqMap = HashMap<Int, Int>()
        for (num in nums) {
            freqMap[num] = (freqMap[num] ?: 0) + 1
        }
        val n = nums.size
        val bucket = Array(n + 1) { mutableListOf<Int>() }
        for ((num, cnt) in freqMap) {
            bucket[cnt].add(num)
        }
        val result = IntArray(k)
        var idx = 0
        for (i in n downTo 1) {
            if (bucket[i].isNotEmpty()) {
                for (num in bucket[i]) {
                    result[idx++] = num
                    if (idx == k) return result
                }
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> topKFrequent(List<int> nums, int k) {
    final Map<int, int> freq = {};
    for (var n in nums) {
      freq[n] = (freq[n] ?? 0) + 1;
    }

    int maxFreq = 0;
    for (var count in freq.values) {
      if (count > maxFreq) maxFreq = count;
    }

    final List<List<int>> bucket = List.generate(maxFreq + 1, (_) => []);
    freq.forEach((num, count) {
      bucket[count].add(num);
    });

    final List<int> result = [];
    for (int i = maxFreq; i >= 0 && result.length < k; --i) {
      if (bucket[i].isNotEmpty) {
        for (var num in bucket[i]) {
          result.add(num);
          if (result.length == k) break;
        }
      }
    }

    return result;
  }
}
```

## Golang

```go
func topKFrequent(nums []int, k int) []int {
    freq := make(map[int]int)
    for _, n := range nums {
        freq[n]++
    }

    buckets := make([][]int, len(nums)+1)
    for num, f := range freq {
        buckets[f] = append(buckets[f], num)
    }

    res := make([]int, 0, k)
    for i := len(buckets) - 1; i >= 0 && len(res) < k; i-- {
        for _, num := range buckets[i] {
            res = append(res, num)
            if len(res) == k {
                break
            }
        }
    }
    return res
}
```

## Ruby

```ruby
def top_k_frequent(nums, k)
  freq = Hash.new(0)
  nums.each { |num| freq[num] += 1 }

  max_freq = freq.values.max
  buckets = Array.new(max_freq + 1) { [] }
  freq.each do |num, count|
    buckets[count] << num
  end

  result = []
  max_freq.downto(1) do |i|
    next if buckets[i].empty?
    buckets[i].each do |num|
      result << num
      return result if result.size == k
    end
  end
  result
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable

  def topKFrequent(nums: Array[Int], k: Int): Array[Int] = {
    // Count frequencies
    val freqMap = mutable.Map.empty[Int, Int]
    for (num <- nums) {
      freqMap.update(num, freqMap.getOrElse(num, 0) + 1)
    }

    // Min-heap based on frequency (smallest frequency at the top)
    implicit val ord: Ordering[(Int, Int)] = Ordering.by[(Int, Int), Int](_._2).reverse
    val heap = mutable.PriorityQueue.empty[(Int, Int)]

    for ((num, cnt) <- freqMap) {
      heap.enqueue((num, cnt))
      if (heap.size > k) heap.dequeue()
    }

    // Extract results
    val result = new Array[Int](k)
    var idx = 0
    while (heap.nonEmpty) {
      result(idx) = heap.dequeue()._1
      idx += 1
    }
    result
  }
}
```

## Rust

```rust
impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        use std::collections::HashMap;
        let mut freq: HashMap<i32, usize> = HashMap::new();
        for &num in nums.iter() {
            *freq.entry(num).or_insert(0) += 1;
        }
        let n = nums.len();
        let mut buckets: Vec<Vec<i32>> = vec![Vec::new(); n + 1];
        for (&num, &count) in freq.iter() {
            buckets[count].push(num);
        }
        let mut result = Vec::with_capacity(k as usize);
        for i in (1..=n).rev() {
            for &num in buckets[i].iter() {
                result.push(num);
                if result.len() == k as usize {
                    return result;
                }
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (top-k-frequent nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((freq (make-hash)))
    ;; count frequencies
    (for ([x nums])
      (hash-update! freq x add1 0))
    ;; maximum frequency
    (define max-freq
      (for/fold ([m 0]) ([(key val) (in-hash freq)])
        (if (> val m) val m)))
    (define buckets (make-vector (+ max-freq 1) '()))
    ;; fill buckets by frequency
    (for ([(num cnt) (in-hash freq)])
      (vector-set! buckets cnt (cons num (vector-ref buckets cnt))))
    ;; collect top k elements
    (let loop ((i max-freq) (remaining k) (acc '()))
      (cond
        [(or (= i 0) (= remaining 0)) (reverse acc)]
        [else
         (let ((bucket (vector-ref buckets i)))
           (if (null? bucket)
               (loop (- i 1) remaining acc)
               (let inner ((lst bucket) (rem remaining) (a acc))
                 (cond
                   [(= rem 0) (reverse a)]
                   [(null? lst) (loop (- i 1) rem a)]
                   [else (inner (cdr lst) (- rem 1) (cons (car lst) a))])))))])))
```

## Erlang

```erlang
-module(solution).
-export([top_k_frequent/2]).

-spec top_k_frequent(Nums :: [integer()], K :: integer()) -> [integer()].
top_k_frequent(Nums, K) ->
    FreqMap = count_freq(Nums, #{}),
    Pairs = maps:to_list(FreqMap),               % [{Num,Freq}]
    FreqPairs = [{F, N} || {N, F} <- Pairs],     % [{Freq,Num}]
    Sorted = lists:reverse(lists:keysort(1, FreqPairs)),
    TopK = take_k(Sorted, K),
    [Num || {_F, Num} <- TopK].

count_freq([], Map) -> Map;
count_freq([H|T], Map) ->
    NewMap = maps:update_with(H,
                               fun(C) -> C + 1 end,
                               1,
                               Map),
    count_freq(T, NewMap).

take_k(List, K) -> take_k(List, K, []).

take_k(_, 0, Acc) -> lists:reverse(Acc);
take_k([], _, Acc) -> lists:reverse(Acc);
take_k([H|T], N, Acc) when N > 0 ->
    take_k(T, N-1, [H|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec top_k_frequent(nums :: [integer], k :: integer) :: [integer]
  def top_k_frequent(nums, k) do
    freq_map =
      Enum.reduce(nums, %{}, fn num, acc ->
        Map.update(acc, num, 1, &(&1 + 1))
      end)

    max_freq =
      freq_map
      |> Enum.map(fn {_num, cnt} -> cnt end)
      |> Enum.max()

    buckets = :array.new(max_freq + 1, [])

    buckets =
      Enum.reduce(freq_map, buckets, fn {num, cnt}, arr ->
        list = :array.get(cnt, arr)
        :array.set(cnt, [num | list], arr)
      end)

    collect_top_k(buckets, max_freq, k, [])
  end

  defp collect_top_k(_arr, _freq, 0, result), do: Enum.reverse(result)

  defp collect_top_k(_arr, freq, _k, result) when freq < 0,
    do: Enum.reverse(result)

  defp collect_top_k(arr, freq, k, result) do
    list = :array.get(freq, arr)
    needed = min(k, length(list))
    {take, _rest} = Enum.split(list, needed)
    new_result = take ++ result

    if needed == k do
      Enum.reverse(new_result)
    else
      collect_top_k(arr, freq - 1, k - needed, new_result)
    end
  end
end
```
