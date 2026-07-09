# 3092. Most Frequent IDs

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<long long> mostFrequentIDs(vector<int>& nums, vector<int>& freq) {
        int n = nums.size();
        vector<long long> ans(n);
        unordered_map<int,long long> cnt;
        multiset<long long> ms; // stores frequencies of IDs currently present
        
        for (int i = 0; i < n; ++i) {
            int id = nums[i];
            long long delta = freq[i];
            
            long long old = 0;
            auto it = cnt.find(id);
            if (it != cnt.end()) old = it->second;
            
            if (old > 0) {
                auto mit = ms.find(old);
                if (mit != ms.end()) ms.erase(mit);
            }
            
            long long now = old + delta; // guaranteed non‑negative
            if (now > 0) {
                cnt[id] = now;
                ms.insert(now);
            } else {
                if (it != cnt.end()) cnt.erase(it);
            }
            
            ans[i] = ms.empty() ? 0 : *ms.rbegin();
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long[] mostFrequentIDs(int[] nums, int[] freq) {
        int n = nums.length;
        long[] ans = new long[n];
        Map<Integer, Long> idCount = new HashMap<>();
        TreeMap<Long, Integer> countFreq = new TreeMap<>();

        for (int i = 0; i < n; i++) {
            int id = nums[i];
            long delta = freq[i];

            long oldCnt = idCount.getOrDefault(id, 0L);
            long newCnt = oldCnt + delta;

            if (oldCnt > 0) {
                int occ = countFreq.get(oldCnt);
                if (occ == 1) {
                    countFreq.remove(oldCnt);
                } else {
                    countFreq.put(oldCnt, occ - 1);
                }
            }

            if (newCnt > 0) {
                countFreq.merge(newCnt, 1, Integer::sum);
                idCount.put(id, newCnt);
            } else {
                idCount.remove(id);
            }

            ans[i] = countFreq.isEmpty() ? 0L : countFreq.lastKey();
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def mostFrequentIDs(self, nums, freq):
        """
        :type nums: List[int]
        :type freq: List[int]
        :rtype: List[int]
        """
        import heapq
        cnt = {}
        heap = []  # max-heap via negative counts, stores ( -count , id )
        n = len(nums)
        ans = [0] * n

        for i in range(n):
            id_ = nums[i]
            delta = freq[i]

            old = cnt.get(id_, 0)
            new = old + delta

            if new > 0:
                cnt[id_] = new
                heapq.heappush(heap, (-new, id_))
            else:  # new == 0 (cannot be negative per problem guarantee)
                if id_ in cnt:
                    del cnt[id_]

            # Clean up stale entries at the top of the heap
            while heap:
                neg_c, iid = heap[0]
                cur = cnt.get(iid, 0)
                if cur == 0 or -neg_c != cur:
                    heapq.heappop(heap)
                else:
                    break

            ans[i] = -heap[0][0] if heap else 0

        return ans
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        id_cnt = {}
        max_heap = []  # store (-count, id) for max-heap behavior
        ans = []
        for num, delta in zip(nums, freq):
            old = id_cnt.get(num, 0)
            new = old + delta
            if new == 0:
                if num in id_cnt:
                    del id_cnt[num]
            else:
                id_cnt[num] = new
                heapq.heappush(max_heap, (-new, num))

            # Clean up stale entries and obtain current maximum count
            while max_heap:
                neg_c, top_id = max_heap[0]
                cur_c = id_cnt.get(top_id, 0)
                if cur_c > 0 and -neg_c == cur_c:
                    ans.append(cur_c)
                    break
                heapq.heappop(max_heap)
            else:
                ans.append(0)

        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    long long cnt;
    int id;
} Node;

static void heapSwap(Node *a, Node *b) {
    Node tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(Node *heap, int *size, Node node) {
    int i = (*size)++;
    heap[i] = node;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].cnt >= heap[i].cnt) break;
        heapSwap(&heap[p], &heap[i]);
        i = p;
    }
}

static void heapPop(Node *heap, int *size) {
    if (*size == 0) return;
    heap[0] = heap[--(*size)];
    int i = 0;
    while (1) {
        int l = (i << 1) + 1;
        int r = l + 1;
        int largest = i;
        if (l < *size && heap[l].cnt > heap[largest].cnt) largest = l;
        if (r < *size && heap[r].cnt > heap[largest].cnt) largest = r;
        if (largest == i) break;
        heapSwap(&heap[i], &heap[largest]);
        i = largest;
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* mostFrequentIDs(int* nums, int numsSize, int* freq, int freqSize, int* returnSize) {
    int n = numsSize;  // same as freqSize
    *returnSize = n;
    long long *ans = (long long*)malloc(sizeof(long long) * n);
    
    int maxId = 0;
    for (int i = 0; i < n; ++i)
        if (nums[i] > maxId) maxId = nums[i];
    
    long long *cur = (long long*)calloc(maxId + 1, sizeof(long long));
    
    Node *heap = (Node*)malloc(sizeof(Node) * (n + 5));
    int heapSize = 0;
    
    for (int i = 0; i < n; ++i) {
        int id = nums[i];
        long long newCnt = cur[id] + freq[i];   // guaranteed non‑negative
        cur[id] = newCnt;
        
        Node nd = {newCnt, id};
        heapPush(heap, &heapSize, nd);
        
        while (heapSize > 0) {
            Node top = heap[0];
            if (cur[top.id] != top.cnt)
                heapPop(heap, &heapSize);
            else
                break;
        }
        
        ans[i] = (heapSize == 0) ? 0 : heap[0].cnt;
    }
    
    free(cur);
    free(heap);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long[] MostFrequentIDs(int[] nums, int[] freq) {
        int n = nums.Length;
        long[] ans = new long[n];
        var idCount = new Dictionary<int, long>();
        var countFreq = new Dictionary<long, int>();
        var heap = new PriorityQueue<long, long>(); // element: count, priority: -count for max-heap

        for (int i = 0; i < n; i++) {
            int id = nums[i];
            long delta = freq[i];

            long oldCount = 0;
            if (idCount.TryGetValue(id, out var oc)) oldCount = oc;

            long newCount = oldCount + delta; // guaranteed >= 0

            // remove old count contribution
            if (oldCount > 0) {
                int cf = countFreq[oldCount];
                if (cf == 1) countFreq.Remove(oldCount);
                else countFreq[oldCount] = cf - 1;
            }

            // add new count contribution
            if (newCount > 0) {
                idCount[id] = newCount;
                if (countFreq.TryGetValue(newCount, out var cfNew))
                    countFreq[newCount] = cfNew + 1;
                else
                    countFreq[newCount] = 1;

                heap.Enqueue(newCount, -newCount);
            } else {
                // count becomes zero, remove id entry
                idCount.Remove(id);
            }

            long curMax = 0;
            while (heap.TryPeek(out var top, out _)) {
                if (countFreq.ContainsKey(top) && countFreq[top] > 0) {
                    curMax = top;
                    break;
                }
                heap.Dequeue(); // discard stale entry
            }

            ans[i] = curMax;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} freq
 * @return {number[]}
 */
var mostFrequentIDs = function(nums, freq) {
    class MaxHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        peek() { return this.heap[0]; }
        push(val) {
            const h = this.heap;
            h.push(val);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p] >= h[i]) break;
                [h[p], h[i]] = [h[i], h[p]];
                i = p;
            }
        }
        pop() {
            const h = this.heap;
            if (h.length === 0) return undefined;
            const top = h[0];
            const last = h.pop();
            if (h.length > 0) {
                h[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1,
                        r = l + 1,
                        largest = i;
                    if (l < h.length && h[l] > h[largest]) largest = l;
                    if (r < h.length && h[r] > h[largest]) largest = r;
                    if (largest === i) break;
                    [h[i], h[largest]] = [h[largest], h[i]];
                    i = largest;
                }
            }
            return top;
        }
    }

    const idCount = new Map();          // id -> current count
    const countFreq = new Map();        // count -> number of ids having this count
    const heap = new MaxHeap();
    const n = nums.length;
    const ans = new Array(n);

    for (let i = 0; i < n; ++i) {
        const id = nums[i];
        const delta = freq[i];

        const oldCnt = idCount.get(id) || 0;
        const newCnt = oldCnt + delta; // guaranteed >= 0

        if (oldCnt > 0) {
            const c = countFreq.get(oldCnt);
            if (c === 1) countFreq.delete(oldCnt);
            else countFreq.set(oldCnt, c - 1);
        }

        if (newCnt > 0) {
            idCount.set(id, newCnt);
            const c2 = (countFreq.get(newCnt) || 0) + 1;
            countFreq.set(newCnt, c2);
            heap.push(newCnt);
        } else {
            // newCnt == 0, remove the id entry
            if (oldCnt > 0) {
                // already handled removal from countFreq above
            }
            idCount.delete(id);
        }

        while (heap.size() && !countFreq.has(heap.peek())) heap.pop();

        ans[i] = heap.size() ? heap.peek() : 0;
    }

    return ans;
};
```

## Typescript

```typescript
function mostFrequentIDs(nums: number[], freq: number[]): number[] {
    const n = nums.length;
    const ans: number[] = new Array(n);
    
    // map from id to its current count
    const idCount = new Map<number, number>();
    // map from count to how many ids have this count
    const countFreq = new Map<number, number>();
    
    class MaxHeap {
        private data: number[] = [];
        size(): number { return this.data.length; }
        peek(): number | undefined { return this.data[0]; }
        push(val: number): void {
            const a = this.data;
            a.push(val);
            let i = a.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (a[p] >= a[i]) break;
                [a[p], a[i]] = [a[i], a[p]];
                i = p;
            }
        }
        pop(): number | undefined {
            const a = this.data;
            if (a.length === 0) return undefined;
            const top = a[0];
            const last = a.pop()!;
            if (a.length > 0) {
                a[0] = last;
                let i = 0;
                while (true) {
                    let left = i * 2 + 1;
                    let right = left + 1;
                    let largest = i;
                    if (left < a.length && a[left] > a[largest]) largest = left;
                    if (right < a.length && a[right] > a[largest]) largest = right;
                    if (largest === i) break;
                    [a[i], a[largest]] = [a[largest], a[i]];
                    i = largest;
                }
            }
            return top;
        }
    }
    
    const heap = new MaxHeap();
    
    for (let i = 0; i < n; ++i) {
        const id = nums[i];
        const delta = freq[i];
        const oldCnt = idCount.get(id) ?? 0;
        const newCnt = oldCnt + delta; // guaranteed >= 0
        
        if (oldCnt > 0) {
            const cfOld = countFreq.get(oldCnt)! - 1;
            if (cfOld === 0) countFreq.delete(oldCnt);
            else countFreq.set(oldCnt, cfOld);
        }
        if (newCnt > 0) {
            idCount.set(id, newCnt);
            const cfNew = (countFreq.get(newCnt) ?? 0) + 1;
            countFreq.set(newCnt, cfNew);
            heap.push(newCnt);
        } else {
            // newCnt == 0, remove the id completely
            if (oldCnt > 0) idCount.delete(id);
        }
        
        // Clean up heap top if its count no longer exists
        while (heap.size() > 0) {
            const top = heap.peek()!;
            if ((countFreq.get(top) ?? 0) > 0) break;
            heap.pop();
        }
        
        ans[i] = heap.size() === 0 ? 0 : heap.peek()!;
    }
    
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $freq
     * @return Integer[]
     */
    function mostFrequentIDs($nums, $freq) {
        $n = count($nums);
        $cntMap = [];      // id => current count
        $freqCount = [];   // count => number of ids having this count
        $maxCount = 0;
        $ans = [];

        for ($i = 0; $i < $n; ++$i) {
            $id = $nums[$i];
            $delta = $freq[$i];

            $old = $cntMap[$id] ?? 0;
            $new = $old + $delta; // guaranteed non‑negative

            if ($old > 0) {
                $freqCount[$old]--;
                if ($freqCount[$old] == 0) {
                    unset($freqCount[$old]);
                }
            }

            if ($new > 0) {
                $cntMap[$id] = $new;
                $freqCount[$new] = ($freqCount[$new] ?? 0) + 1;
            } else {
                // count becomes zero, remove the id
                unset($cntMap[$id]);
            }

            if ($new > $maxCount) {
                $maxCount = $new;
            } else {
                while ($maxCount > 0 && (!isset($freqCount[$maxCount]) || $freqCount[$maxCount] == 0)) {
                    $maxCount--;
                }
            }

            $ans[] = $maxCount;
        }

        return $ans;
    }
}
```

## Swift

```swift
class MaxHeap {
    private var heap: [(cnt: Int, id: Int)] = []
    
    var isEmpty: Bool { heap.isEmpty }
    var peek: (cnt: Int, id: Int)? { heap.first }
    
    func push(_ element: (cnt: Int, id: Int)) {
        heap.append(element)
        siftUp(heap.count - 1)
    }
    
    @discardableResult
    func pop() -> (cnt: Int, id: Int)? {
        guard !heap.isEmpty else { return nil }
        let top = heap[0]
        let last = heap.removeLast()
        if !heap.isEmpty {
            heap[0] = last
            siftDown(0)
        }
        return top
    }
    
    private func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if heap[child].cnt > heap[parent].cnt {
                heap.swapAt(child, parent)
                child = parent
            } else {
                break
            }
        }
    }
    
    private func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var largest = parent
            if left < heap.count && heap[left].cnt > heap[largest].cnt {
                largest = left
            }
            if right < heap.count && heap[right].cnt > heap[largest].cnt {
                largest = right
            }
            if largest == parent { break }
            heap.swapAt(parent, largest)
            parent = largest
        }
    }
}

class Solution {
    func mostFrequentIDs(_ nums: [Int], _ freq: [Int]) -> [Int] {
        let n = nums.count
        var ans = [Int]()
        ans.reserveCapacity(n)
        var countDict = [Int: Int]()   // id -> current count
        let heap = MaxHeap()
        
        for i in 0..<n {
            let id = nums[i]
            let delta = freq[i]
            let newCount = (countDict[id] ?? 0) + delta
            
            if newCount > 0 {
                countDict[id] = newCount
                heap.push((cnt: newCount, id: id))
            } else {
                countDict.removeValue(forKey: id)
            }
            
            var currentMax = 0
            while let top = heap.peek {
                if let cur = countDict[top.id], cur == top.cnt {
                    currentMax = top.cnt
                    break
                } else {
                    _ = heap.pop()
                }
            }
            ans.append(currentMax)
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mostFrequentIDs(nums: IntArray, freq: IntArray): LongArray {
        val n = nums.size
        val ans = LongArray(n)
        val idToCount = HashMap<Int, Long>()
        val countFreq = java.util.TreeMap<Long, Int>()

        fun inc(c: Long) {
            countFreq[c] = (countFreq[c] ?: 0) + 1
        }

        fun dec(c: Long) {
            val cur = countFreq[c] ?: return
            if (cur == 1) countFreq.remove(c) else countFreq[c] = cur - 1
        }

        for (i in 0 until n) {
            val id = nums[i]
            val delta = freq[i].toLong()
            val old = idToCount[id] ?: 0L
            if (old > 0L) dec(old)

            val newCnt = old + delta
            if (newCnt > 0L) {
                inc(newCnt)
                idToCount[id] = newCnt
            } else {
                idToCount.remove(id)
            }

            ans[i] = if (countFreq.isEmpty()) 0L else countFreq.lastKey()
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  List<int> mostFrequentIDs(List<int> nums, List<int> freq) {
    int n = nums.length;
    Map<int, int> cnt = {};
    SplayTreeMap<int, int> freqCount = SplayTreeMap();
    List<int> ans = List.filled(n, 0);

    for (int i = 0; i < n; i++) {
      int id = nums[i];
      int delta = freq[i];

      int old = cnt[id] ?? 0;
      int now = old + delta; // guaranteed >= 0

      if (old > 0) {
        int c = freqCount[old]!;
        if (c == 1) {
          freqCount.remove(old);
        } else {
          freqCount[old] = c - 1;
        }
      }

      if (now == 0) {
        cnt.remove(id);
      } else {
        cnt[id] = now;
        freqCount[now] = (freqCount[now] ?? 0) + 1;
      }

      ans[i] = freqCount.isEmpty ? 0 : freqCount.lastKey();
    }

    return ans;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type IntMaxHeap []int

func (h IntMaxHeap) Len() int           { return len(h) }
func (h IntMaxHeap) Less(i, j int) bool { return h[i] > h[j] } // max-heap
func (h IntMaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntMaxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntMaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func mostFrequentIDs(nums []int, freq []int) []int64 {
	n := len(nums)
	ans := make([]int64, n)

	idCount := make(map[int]int)   // id -> current count
	freqCnt := make(map[int]int)   // frequency -> number of ids having this frequency
	h := &IntMaxHeap{}
	heap.Init(h)

	for i := 0; i < n; i++ {
		id := nums[i]
		delta := freq[i]

		old := idCount[id]          // 0 if not present
		newVal := old + delta

		// update idCount map
		if newVal == 0 {
			delete(idCount, id)
		} else {
			idCount[id] = newVal
		}

		// adjust frequency counts for old value
		if old > 0 {
			if c := freqCnt[old] - 1; c == 0 {
				delete(freqCnt, old)
			} else {
				freqCnt[old] = c
			}
		}
		// adjust for new value
		if newVal > 0 {
			freqCnt[newVal]++
			heap.Push(h, newVal)
		}

		// obtain current maximum frequency
		curMax := 0
		for h.Len() > 0 {
			top := (*h)[0]
			if cnt, ok := freqCnt[top]; ok && cnt > 0 {
				curMax = top
				break
			}
			heap.Pop(h) // discard stale entry
		}

		if len(idCount) == 0 {
			ans[i] = 0
		} else {
			ans[i] = int64(curMax)
		}
	}
	return ans
}
```

## Ruby

```ruby
def most_frequent_i_ds(nums, freq)
  n = nums.length
  counts = {}
  heap = []
  ans = Array.new(n)

  push = lambda do |pair|
    heap << pair
    idx = heap.size - 1
    while idx > 0
      parent = (idx - 1) / 2
      break if heap[parent][0] >= heap[idx][0]
      heap[parent], heap[idx] = heap[idx], heap[parent]
      idx = parent
    end
  end

  pop_root = lambda do
    return nil if heap.empty?
    top = heap[0]
    last = heap.pop
    unless heap.empty?
      heap[0] = last
      idx = 0
      size = heap.size
      loop do
        left = idx * 2 + 1
        right = left + 1
        break if left >= size
        larger = left
        larger = right if right < size && heap[right][0] > heap[left][0]
        break if heap[idx][0] >= heap[larger][0]
        heap[idx], heap[larger] = heap[larger], heap[idx]
        idx = larger
      end
    end
    top
  end

  (0...n).each do |i|
    id = nums[i]
    delta = freq[i]
    new_cnt = (counts[id] || 0) + delta
    if new_cnt > 0
      counts[id] = new_cnt
      push.call([new_cnt, id])
    else
      counts.delete(id)
    end

    while !heap.empty?
      cnt, iid = heap[0]
      if counts[iid] && counts[iid] == cnt
        ans[i] = cnt
        break
      else
        pop_root.call
      end
    end
    ans[i] = 0 if heap.empty?
  end

  ans
end
```

## Scala

```scala
object Solution {
    def mostFrequentIDs(nums: Array[Int], freq: Array[Int]): Array[Long] = {
        import scala.collection.mutable

        val n = nums.length
        val ans = new Array[Long](n)

        // id -> current count
        val cnt = mutable.Map.empty[Int, Long]

        // count -> number of ids having this count, ordered descending by count
        val countMap = mutable.TreeMap.empty[Long, Int](Ordering.Long.reverse)

        def inc(key: Long): Unit = {
            countMap.update(key, countMap.getOrElse(key, 0) + 1)
        }

        def dec(key: Long): Unit = {
            val cur = countMap.getOrElse(key, 0)
            if (cur <= 1) countMap -= key
            else countMap.update(key, cur - 1)
        }

        var i = 0
        while (i < n) {
            val id = nums(i)
            val delta = freq(i).toLong

            val oldCnt = cnt.getOrElse(id, 0L)
            if (oldCnt > 0) dec(oldCnt)

            val newCnt = oldCnt + delta
            if (newCnt > 0) {
                cnt.update(id, newCnt)
                inc(newCnt)
            } else {
                cnt -= id
            }

            ans(i) = if (countMap.isEmpty) 0L else countMap.head._1
            i += 1
        }

        ans
    }
}
```

## Rust

```rust
use std::collections::{HashMap, BTreeMap};

impl Solution {
    pub fn most_frequent_i_ds(nums: Vec<i32>, freq: Vec<i32>) -> Vec<i64> {
        let n = nums.len();
        let mut id_cnt: HashMap<i32, i64> = HashMap::with_capacity(n);
        let mut cnt_freq: BTreeMap<i64, i32> = BTreeMap::new();

        fn update_multiset(map: &mut BTreeMap<i64, i32>, count: i64, delta: i32) {
            if count == 0 {
                return;
            }
            let entry = map.entry(count).or_insert(0);
            *entry += delta;
            if *entry == 0 {
                map.remove(&count);
            }
        }

        let mut ans: Vec<i64> = Vec::with_capacity(n);
        for i in 0..n {
            let id = nums[i];
            let change = freq[i] as i64; // can be negative

            let old_cnt = *id_cnt.get(&id).unwrap_or(&0);
            if old_cnt > 0 {
                update_multiset(&mut cnt_freq, old_cnt, -1);
            }

            let new_cnt = old_cnt + change;
            if new_cnt > 0 {
                id_cnt.insert(id, new_cnt);
                update_multiset(&mut cnt_freq, new_cnt, 1);
            } else {
                // count becomes zero, remove entry
                id_cnt.remove(&id);
            }

            let cur_max = match cnt_freq.keys().next_back() {
                Some(&v) => v,
                None => 0,
            };
            ans.push(cur_max);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (most-frequent-i-ds nums freq)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length nums))
         (ans (make-vector n))
         (id-count (make-hash))          ; id -> current count
         (count-num (make-hash))         ; count -> number of ids having this count
         (maxCount 0))
    (for ([i (in-range n)])
      (define id (list-ref nums i))
      (define delta (list-ref freq i))
      (define old (hash-ref id-count id 0))
      (define new (+ old delta))
      ;; update id -> count
      (hash-set! id-count id new)
      ;; decrement frequency of old count
      (when (> old 0)
        (define oldFreq (hash-ref count-num old))
        (if (= oldFreq 1)
            (hash-remove! count-num old)
            (hash-set! count-num old (- oldFreq 1))))
      ;; increment frequency of new count
      (when (> new 0)
        (define newFreq (hash-ref count-num new 0))
        (hash-set! count-num new (+ newFreq 1)))
      ;; adjust maxCount
      (cond
        [(> new maxCount) (set! maxCount new)]
        [(and (= old maxCount)
              (not (hash-has-key? count-num maxCount)))
         (let loop ((c (- maxCount 1)))
           (if (or (zero? c) (hash-has-key? count-num c))
               (set! maxCount c)
               (loop (- c 1))))])
      (vector-set! ans i maxCount))
    (vector->list ans)))
```

## Erlang

```erlang
-spec most_frequent_i_ds(Nums :: [integer()], Freq :: [integer()]) -> [integer()].
most_frequent_i_ds(Nums, Freq) ->
    process(Nums, Freq, #{}, gb_trees:empty(), []).

process([], [], _IdMap, _CountTree, Acc) ->
    lists:reverse(Acc);
process([Num | RestN], [Delta | RestF], IdMap, CountTree, Acc) ->
    OldCnt = maps:get(Num, IdMap, 0),
    NewCnt = OldCnt + Delta,
    %% remove old count contribution
    CountTree1 =
        if OldCnt > 0 ->
                update_count_tree(CountTree, OldCnt, -1);
           true -> CountTree
        end,
    %% add new count contribution and update IdMap
    {IdMap2, CountTree2} =
        if NewCnt > 0 ->
                IdMapTmp = maps:put(Num, NewCnt, IdMap),
                TreeTmp = update_count_tree(CountTree1, NewCnt, 1),
                {IdMapTmp, TreeTmp};
           true ->
                IdMapTmp = maps:remove(Num, IdMap),
                {IdMapTmp, CountTree1}
        end,
    MaxFreq =
        case gb_trees:is_empty(CountTree2) of
            true -> 0;
            false ->
                {Key, _} = gb_trees:largest(CountTree2),
                Key
        end,
    process(RestN, RestF, IdMap2, CountTree2, [MaxFreq | Acc]).

update_count_tree(Tree, Count, Delta) ->
    case gb_trees:lookup(Count, Tree) of
        {value, V} ->
            NewV = V + Delta,
            if NewV > 0 ->
                    gb_trees:update(Count, NewV, Tree);
               true ->
                    gb_trees:delete(Count, Tree)
            end;
        none ->
            %% Delta should be positive here
            gb_trees:insert(Count, Delta, Tree)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec most_frequent_i_ds(nums :: [integer], freq :: [integer]) :: [integer]
  def most_frequent_i_ds(nums, freq) do
    Enum.zip(nums, freq)
    |> Enum.reduce({%{}, :gb_trees.empty(), []}, fn {id, delta},
                                                   {id_map, tree, acc} ->
      old_cnt = Map.get(id_map, id, 0)
      new_cnt = old_cnt + delta

      # remove old count from tree
      tree =
        if old_cnt > 0 do
          case :gb_trees.lookup(old_cnt, tree) do
            {:value, 1} -> :gb_trees.delete(old_cnt, tree)
            {:value, v} -> :gb_trees.update(old_cnt, v - 1, tree)
            :none -> tree
          end
        else
          tree
        end

      # add new count to tree if positive
      tree =
        if new_cnt > 0 do
          case :gb_trees.lookup(new_cnt, tree) do
            {:value, v} -> :gb_trees.update(new_cnt, v + 1, tree)
            :none -> :gb_trees.insert(new_cnt, 1, tree)
          end
        else
          tree
        end

      # update id map
      id_map =
        if new_cnt > 0 do
          Map.put(id_map, id, new_cnt)
        else
          Map.delete(id_map, id)
        end

      max_val =
        if :gb_trees.is_empty(tree) do
          0
        else
          {max_key, _} = :gb_trees.largest(tree)
          max_key
        end

      {id_map, tree, [max_val | acc]}
    end)
    |> elem(2)
    |> Enum.reverse()
  end
end
```
