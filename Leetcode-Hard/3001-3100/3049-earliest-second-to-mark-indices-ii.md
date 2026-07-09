# 3049. Earliest Second to Mark Indices II

## Cpp

```cpp
class Solution {
public:
    int earliestSecondToMarkIndices(vector<int>& nums, vector<int>& changeIndices) {
        int n = nums.size();
        int m = changeIndices.size();
        const long long INF = 1e18;
        vector<long long> firstPos(n, INF);
        for (int i = 0; i < m; ++i) {
            int idx = changeIndices[i] - 1;
            if (firstPos[idx] == INF) firstPos[idx] = i + 1; // 1-indexed seconds
        }
        long long sumNums = 0;
        for (int v : nums) sumNums += v;
        long long baseTime = sumNums + n; // total seconds needed without any change
        
        auto feasible = [&](int x)->bool{
            if (x < n) return false; // need at least one second per mark
            long long requiredReduction = baseTime - x;
            if (requiredReduction <= 0) return true; // already enough time
            vector<long long> savings;
            savings.reserve(n);
            for (int i = 0; i < n; ++i) {
                if (nums[i] > 0 && firstPos[i] != INF && firstPos[i] <= x - 1) {
                    savings.push_back((long long)nums[i] - 1);
                }
            }
            if (savings.empty()) return false;
            sort(savings.begin(), savings.end(), greater<long long>());
            long long canChange = x - n; // number of seconds available for change operations
            long long totalSaving = 0;
            int limit = (int)min<long long>(canChange, savings.size());
            for (int i = 0; i < limit; ++i) {
                totalSaving += savings[i];
                if (totalSaving >= requiredReduction) return true;
            }
            return totalSaving >= requiredReduction;
        };
        
        int lo = n, hi = m, ans = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (feasible(mid)) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int earliestSecondToMarkIndices(int[] nums, int[] changeIndices) {
        int n = nums.length;
        int m = changeIndices.length;
        long sum = 0;
        for (int v : nums) sum += v;
        long totalNeeded = sum + n; // without any savings

        // binary search on answer
        int lo = 1, hi = m, ans = -1;
        while (lo <= hi) {
            int mid = (lo + hi) >>> 1;
            if (can(mid, nums, changeIndices, totalNeeded)) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    }

    private boolean can(int x, int[] nums, int[] changeIndices, long totalNeeded) {
        int n = nums.length;
        int[] cnt = new int[n];
        for (int i = 0; i < x; ++i) {
            cnt[changeIndices[i] - 1]++;
        }
        long saved = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == 0) {
                if (cnt[i] == 0) return false; // need at least one second to mark
            } else {
                if (cnt[i] < 2) return false; // need two seconds: set to zero and later mark
                saved += nums[i] - 1L;
            }
        }
        return totalNeeded - saved <= x;
    }
}
```

## Python

```python
class Solution(object):
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        """
        :type nums: List[int]
        :type changeIndices: List[int]
        :rtype: int
        """
        n = len(nums)
        m = len(changeIndices)
        total_needed = sum(nums) + n  # total seconds if only decrement by one each time

        # binary search earliest second x where possible
        lo, hi = 1, m
        ans = -1

        # preconvert to 0-indexed for speed
        change = [c - 1 for c in changeIndices]

        while lo <= hi:
            mid = (lo + hi) // 2
            if self._can(mid, n, total_needed, nums, change):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans

    def _can(self, x, n, total_needed, nums, change):
        # need at least n seconds to mark each index
        if x < n:
            return False

        cnt = [0] * n
        benefits = []  # benefit = nums[i] - 1 for indices that appear at least twice in first x seconds

        # scan from right to left within the first x operations
        for i in range(x - 1, -1, -1):
            idx = change[i]
            cnt[idx] += 1
            if cnt[idx] == 2:          # this occurrence has a later one for marking
                b = nums[idx] - 1
                if b > 0:
                    benefits.append(b)

        # we can use at most (x - n) zero‑setting operations
        k = x - n
        if not benefits or k <= 0:
            return total_needed <= x

        benefits.sort(reverse=True)
        reduction = sum(benefits[:min(k, len(benefits))])
        return total_needed - reduction <= x
```

## Python3

```python
import heapq
from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n = len(nums)
        m = len(changeIndices)
        firstPos = [m + 1] * n
        for i, idx in enumerate(changeIndices):
            pos = i + 1
            j = idx - 1
            if firstPos[j] > m:
                firstPos[j] = pos

        total_sum = sum(nums)

        # If some positive value never appears, impossible altogether
        for i, v in enumerate(nums):
            if v > 0 and firstPos[i] > m:
                return -1

        def feasible(x: int) -> bool:
            if x < n:
                return False
            allowed = x - n
            # each positive index must appear at least once within first x seconds
            for i, v in enumerate(nums):
                if v > 0 and firstPos[i] > x:
                    return False

            heap = []
            total_in_heap = 0
            # iterate seconds x..1 (0-indexed)
            for t in range(x - 1, -1, -1):
                idx = changeIndices[t] - 1
                val = nums[idx]
                if val > 0:
                    heapq.heappush(heap, val)
                    total_in_heap += val
                    if len(heap) > allowed:
                        smallest = heapq.heappop(heap)
                        total_in_heap -= smallest

            # reduction achieved by selected changes: sum(val-1) = total_in_heap - len(heap)
            reduction = total_in_heap - len(heap)
            needed_time = total_sum + n - reduction
            return needed_time <= x

        lo, hi = 1, m
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
```

## C

```c
#include <stdlib.h>

int earliestSecondToMarkIndices(int* nums, int numsSize, int* changeIndices, int changeIndicesSize) {
    long long sum = 0;
    for (int i = 0; i < numsSize; ++i) sum += nums[i];
    long long total_needed = sum + numsSize; // sum of decrements plus one mark per index

    char *seen = (char *)calloc(numsSize, sizeof(char));
    long long saved = 0;

    for (int s = 1; s <= changeIndicesSize; ++s) {
        int idx = changeIndices[s - 1] - 1;
        if (!seen[idx]) {
            seen[idx] = 1;
            if (nums[idx] > 0) saved += (long long)nums[idx] - 1;
        }
        if (total_needed - saved <= s) {
            free(seen);
            return s;
        }
    }

    free(seen);
    return -1;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int EarliestSecondToMarkIndices(int[] nums, int[] changeIndices) {
        int n = nums.Length;
        int m = changeIndices.Length;
        const int INF = int.MaxValue;
        int[] firstPos = new int[n];
        for (int i = 0; i < n; i++) firstPos[i] = INF;
        for (int i = 0; i < m; i++) {
            int idx = changeIndices[i] - 1;
            if (firstPos[idx] == INF) firstPos[idx] = i + 1; // seconds are 1-indexed
        }
        long sumNums = 0;
        foreach (int v in nums) sumNums += v;

        bool Can(int x) {
            if (x < n) return false;
            long requiredSaving = sumNums + n - x;
            if (requiredSaving <= 0) return true;
            int maxChanges = x - n;
            List<long> savings = new List<long>();
            for (int i = 0; i < n; i++) {
                if (firstPos[i] != INF && firstPos[i] < x && nums[i] > 0) {
                    savings.Add((long)nums[i] - 1);
                }
            }
            if (savings.Count == 0) return false;
            savings.Sort((a, b) => b.CompareTo(a)); // descending
            long total = 0;
            int take = Math.Min(maxChanges, savings.Count);
            for (int i = 0; i < take; i++) {
                total += savings[i];
                if (total >= requiredSaving) return true;
            }
            return total >= requiredSaving;
        }

        int lo = 1, hi = m, ans = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (Can(mid)) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/ **
 * @param {number[]} nums
 * @param {number[]} changeIndices
 * @return {number}
 */
var earliestSecondToMarkIndices = function(nums, changeIndices) {
    const n = nums.length;
    const m = changeIndices.length;
    const totalSum = nums.reduce((a, b) => a + b, 0);
    
    // binary search on answer
    let lo = 1, hi = m, ans = -1;
    while (lo <= hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (can(mid)) {
            ans = mid;
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    return ans;
    
    function can(x) {
        if (x < n) return false; // need at least n seconds to mark all indices
        const cnt = new Array(n).fill(0);
        for (let i = 0; i < x; ++i) {
            const idx = changeIndices[i] - 1;
            cnt[idx]++;
        }
        // every positive value must have at least one chance to be changed
        for (let i = 0; i < n; ++i) {
            if (nums[i] > 0 && cnt[i] === 0) return false;
        }
        const extraSlots = x - n; // seconds available for change operations
        const benefits = [];
        for (let i = 0; i < n; ++i) {
            if (cnt[i] >= 1 && nums[i] > 0) {
                benefits.push(nums[i] - 1); // saving when we set this index to zero directly
            }
        }
        benefits.sort((a, b) => b - a);
        let saved = 0;
        const limit = Math.min(extraSlots, benefits.length);
        for (let i = 0; i < limit; ++i) {
            saved += benefits[i];
        }
        const needed = totalSum + n - saved;
        return needed <= x;
    }
};
```

## Typescript

```typescript
function earliestSecondToMarkIndices(nums: number[], changeIndices: number[]): number {
    const n = nums.length;
    const m = changeIndices.length;
    const sumNums = nums.reduce((a, b) => a + b, 0);
    const totalNeededBase = sumNums + n; // without any beneficial changes

    class MinHeap {
        private data: number[] = [];
        size(): number { return this.data.length; }
        push(val: number): void {
            const arr = this.data;
            arr.push(val);
            let i = arr.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (arr[p] <= arr[i]) break;
                [arr[p], arr[i]] = [arr[i], arr[p]];
                i = p;
            }
        }
        pop(): number {
            const arr = this.data;
            const n = arr.length;
            if (n === 0) return undefined as any;
            const top = arr[0];
            const last = arr.pop()!;
            if (arr.length > 0) {
                arr[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1;
                    let r = l + 1;
                    let smallest = i;
                    if (l < arr.length && arr[l] < arr[smallest]) smallest = l;
                    if (r < arr.length && arr[r] < arr[smallest]) smallest = r;
                    if (smallest === i) break;
                    [arr[i], arr[smallest]] = [arr[smallest], arr[i]];
                    i = smallest;
                }
            }
            return top;
        }
    }

    const canFinish = (x: number): boolean => {
        const seen = new Uint8Array(n);
        let marksAvailable = 0;
        const heap = new MinHeap();
        let benefitSum = 0; // sum of nums values stored in heap

        for (let i = x - 1; i >= 0; --i) {
            const idx = changeIndices[i] - 1;
            if (!seen[idx]) {
                seen[idx] = 1;
                marksAvailable++;
            } else {
                // this occurrence can be used as a change operation
                if (nums[idx] > 1) { // only beneficial if value > 1
                    heap.push(nums[idx]);
                    benefitSum += nums[idx];
                    if (heap.size() > marksAvailable) {
                        const removed = heap.pop();
                        benefitSum -= removed;
                    }
                }
            }
        }

        const saved = benefitSum - heap.size(); // each contributes (value-1)
        return totalNeededBase - saved <= x;
    };

    let left = 1, right = m, answer = -1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (canFinish(mid)) {
            answer = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return answer;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer[] $changeIndices
     * @return Integer
     */
    function earliestSecondToMarkIndices($nums, $changeIndices) {
        $n = count($nums);
        $m = count($changeIndices);
        $totalNeeded = array_sum($nums) + $n; // sum of decrements + markings

        $left = 1;
        $right = $m;
        $ans = -1;

        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);
            if ($this->canMarkAll($mid, $nums, $changeIndices, $totalNeeded, $n)) {
                $ans = $mid;
                $right = $mid - 1;
            } else {
                $left = $mid + 1;
            }
        }

        return $ans;
    }

    private function canMarkAll($x, $nums, $changeIndices, $totalNeeded, $n) {
        $capacity = $x - $n; // maximum number of shortcut changes we may use
        if ($capacity < 0) {
            return false;
        }

        $heap = new SplMinHeap(); // stores selected savings (min-heap)
        $saved = 0;
        $seen = array_fill(0, $n + 1, false); // 1-indexed

        for ($t = $x; $t >= 1; --$t) {
            $idx = $changeIndices[$t - 1]; // 1-indexed
            if (!$seen[$idx]) {
                $seen[$idx] = true;
                $v = $nums[$idx - 1];
                $saving = $v - 1; // benefit of setting to zero directly
                if ($saving > 0) {
                    $heap->insert($saving);
                    $saved += $saving;
                    if ($heap->count() > $capacity) {
                        $removed = $heap->extract(); // remove smallest saving
                        $saved -= $removed;
                    }
                }
            }
        }

        return ($totalNeeded - $saved <= $x);
    }
}
```

## Swift

```swift
class Solution {
    func earliestSecondToMarkIndices(_ nums: [Int], _ changeIndices: [Int]) -> Int {
        let n = nums.count
        let m = changeIndices.count
        var sumNums = 0
        for v in nums { sumNums += v }
        let baseTotal = sumNums + n
        
        func canFinish(_ x: Int) -> Bool {
            var visited = [Bool](repeating: false, count: n)
            var heap = MaxHeap()
            var needMarks = 0          // distinct indices seen so far
            var extraSlots = 0         // processed seconds - needMarks
            var total = baseTotal
            
            for s in stride(from: x - 1, through: 0, by: -1) {
                let idx = changeIndices[s] - 1
                if !visited[idx] {
                    visited[idx] = true
                    needMarks += 1
                    let save = nums[idx] - 1
                    if save > 0 { heap.push(save) }
                }
                // one more processed second
                extraSlots += 1
                // use any available extra slot for the best saving
                while extraSlots > 0 && !heap.isEmpty {
                    let best = heap.pop()
                    total -= best
                    extraSlots -= 1
                }
            }
            return total <= x
        }
        
        var left = 1, right = m, answer = -1
        while left <= right {
            let mid = (left + right) >> 1
            if canFinish(mid) {
                answer = mid
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return answer
    }
}

// Max-heap for Int values
struct MaxHeap {
    private var data: [Int] = []
    
    var isEmpty: Bool { data.isEmpty }
    
    mutating func push(_ value: Int) {
        data.append(value)
        siftUp(from: data.count - 1)
    }
    
    mutating func pop() -> Int {
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(from: 0)
        }
        return top
    }
    
    private mutating func siftUp(from index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) >> 1
            if data[parent] >= data[child] { break }
            data.swapAt(parent, child)
            child = parent
        }
    }
    
    private mutating func siftDown(from index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var largest = parent
            if left < data.count && data[left] > data[largest] { largest = left }
            if right < data.count && data[right] > data[largest] { largest = right }
            if largest == parent { break }
            data.swapAt(parent, largest)
            parent = largest
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun earliestSecondToMarkIndices(nums: IntArray, changeIndices: IntArray): Int {
        val n = nums.size
        val m = changeIndices.size
        var sum: Long = 0L
        for (v in nums) sum += v.toLong()
        val totalNeeded = sum + n // long

        fun can(x: Int): Boolean {
            var need = totalNeeded
            val cnt = IntArray(n)
            val pq = java.util.PriorityQueue<Long>(java.util.Collections.reverseOrder())
            for (i in x - 1 downTo 0) {
                val idx = changeIndices[i] - 1
                cnt[idx]++
                if (cnt[idx] >= 2) {
                    val save = nums[idx].toLong() - 1L
                    if (save > 0) pq.add(save)
                }
                while (need > (i + 1).toLong() && !pq.isEmpty()) {
                    need -= pq.poll()
                }
            }
            return need <= x.toLong()
        }

        var left = 1
        var right = m
        var ans = -1
        while (left <= right) {
            val mid = (left + right) ushr 1
            if (can(mid)) {
                ans = mid
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int earliestSecondToMarkIndices(List<int> nums, List<int> changeIndices) {
    int n = nums.length;
    int m = changeIndices.length;
    if (m < n) return -1;

    int totalNums = 0;
    for (int v in nums) totalNums += v;

    bool can(int x) {
      // min-heap for savings (nums[i] - 1)
      List<int> heap = [];
      List<bool> seen = List.filled(n, false);

      void heapPush(int val) {
        heap.add(val);
        int i = heap.length - 1;
        while (i > 0) {
          int p = (i - 1) >> 1;
          if (heap[p] <= heap[i]) break;
          int tmp = heap[p];
          heap[p] = heap[i];
          heap[i] = tmp;
          i = p;
        }
      }

      int heapPop() {
        int ret = heap[0];
        int last = heap.removeLast();
        if (heap.isNotEmpty) {
          heap[0] = last;
          int i = 0;
          while (true) {
            int l = i * 2 + 1;
            int r = l + 1;
            int smallest = i;
            if (l < heap.length && heap[l] < heap[smallest]) smallest = l;
            if (r < heap.length && heap[r] < heap[smallest]) smallest = r;
            if (smallest == i) break;
            int tmp = heap[i];
            heap[i] = heap[smallest];
            heap[smallest] = tmp;
            i = smallest;
          }
        }
        return ret;
      }

      for (int i = x - 1; i >= 0; --i) {
        int idx = changeIndices[i] - 1;
        if (!seen[idx] && nums[idx] > 0) {
          seen[idx] = true;
          heapPush(nums[idx] - 1);
        }
        int maxChangesAllowed = x - (i + 1); // seconds after current position
        while (heap.length > maxChangesAllowed) {
          heapPop(); // discard smallest saving
        }
      }

      int saved = 0;
      for (int v in heap) saved += v;

      return (totalNums + n - saved) <= x;
    }

    int left = n, right = m, ans = -1;
    while (left <= right) {
      int mid = (left + right) >> 1;
      if (can(mid)) {
        ans = mid;
        right = mid - 1;
      } else {
        left = mid + 1;
      }
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

type IntMinHeap []int

func (h IntMinHeap) Len() int           { return len(h) }
func (h IntMinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntMinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntMinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntMinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func earliestSecondToMarkIndices(nums []int, changeIndices []int) int {
	n := len(nums)
	m := len(changeIndices)

	totalSum := 0
	for _, v := range nums {
		totalSum += v
	}
	baseNeeded := totalSum + n // sum(nums) + n

	can := func(x int) bool {
		seen := make([]bool, n)
		distinct := 0
		h := &IntMinHeap{}
		heap.Init(h)
		sumV := 0 // sum of values kept in heap (selected change operations)

		for i := x; i >= 1; i-- {
			idx := changeIndices[i-1] - 1
			if !seen[idx] {
				seen[idx] = true
				distinct++
			} else {
				v := nums[idx]
				heap.Push(h, v)
				sumV += v
			}
			totalSec := x - i + 1
			capacity := totalSec - distinct // slots available for change operations

			for h.Len() > capacity {
				w := heap.Pop(h).(int)
				sumV -= w
			}
		}

		k := h.Len()
		// reduction = sumV - k (each selected saves nums[i]-1)
		if baseNeeded-(sumV-k) <= x {
			return true
		}
		return false
	}

	if !can(m) {
		return -1
	}
	lo, hi := 1, m
	ans := m
	for lo <= hi {
		mid := (lo + hi) / 2
		if can(mid) {
			ans = mid
			hi = mid - 1
		} else {
			lo = mid + 1
		}
	}
	return ans
}
```

## Ruby

```ruby
def earliest_second_to_mark_indices(nums, change_indices)
  n = nums.size
  m = change_indices.size
  total_needed = nums.sum + n

  left = 1
  right = m
  answer = -1

  while left <= right
    mid = (left + right) / 2
    if feasible?(mid, nums, change_indices, total_needed)
      answer = mid
      right = mid - 1
    else
      left = mid + 1
    end
  end

  answer
end

def feasible?(seconds, nums, change_indices, total_needed)
  need = total_needed - seconds
  return true if need <= 0

  n = nums.size
  limit = seconds - n
  return false if limit < 0

  seen = Array.new(n, false)
  savings = []

  (seconds - 1).downto(0) do |i|
    idx = change_indices[i] - 1
    next if seen[idx]

    seen[idx] = true
    val = nums[idx]
    savings << (val - 1) if val > 0
  end

  return false if limit <= 0 && need > 0

  savings.sort!.reverse!
  saved = 0
  savings[0, limit].each { |v| saved += v }

  saved >= need
end
```

## Scala

```scala
object Solution {
    def earliestSecondToMarkIndices(nums: Array[Int], changeIndices: Array[Int]): Int = {
        val n = nums.length
        val m = changeIndices.length

        var totalSum: Long = 0L
        for (v <- nums) totalSum += v
        val base: Long = totalSum + n // sum of values plus one mark per index

        // first occurrence (1-indexed) of each index in changeIndices
        val INF = Int.MaxValue
        val firstPos = Array.fill[Int](n)(INF)
        var sec = 1
        for (idx <- changeIndices) {
            val i = idx - 1
            if (firstPos(i) == INF) firstPos(i) = sec
            sec += 1
        }

        def feasible(x: Int): Boolean = {
            if (x < n) return false                     // need at least n seconds to mark all indices
            val needReduction = base - x                 // how much total time we must save
            if (needReduction <= 0) return true

            val maxZeroOps = x - n                       // seconds available for zeroing operations
            if (maxZeroOps <= 0) return false

            val savings = new scala.collection.mutable.ArrayBuffer[Long]()
            var i = 0
            while (i < n) {
                if (firstPos(i) <= x && nums(i) > 0) {
                    savings += (nums(i).toLong - 1)
                }
                i += 1
            }

            // take the largest up to maxZeroOps savings
            val arr = savings.toArray
            scala.util.Sorting.quickSort(arr) // ascending
            var sum: Long = 0L
            var taken = 0
            var idx = arr.length - 1
            while (taken < maxZeroOps && idx >= 0) {
                sum += arr(idx)
                if (sum >= needReduction) return true
                taken += 1
                idx -= 1
            }
            sum >= needReduction
        }

        var lo = 1
        var hi = m
        var ans = -1
        while (lo <= hi) {
            val mid = (lo + hi) >>> 1
            if (feasible(mid)) {
                ans = mid
                hi = mid - 1
            } else {
                lo = mid + 1
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn earliest_second_to_mark_indices(nums: Vec<i32>, change_indices: Vec<i32>) -> i32 {
        let n = nums.len();
        let nums_i64: Vec<i64> = nums.iter().map(|&v| v as i64).collect();
        let m = change_indices.len();
        let ch: Vec<usize> = change_indices.iter().map(|&v| (v as usize) - 1).collect();

        fn feasible(x: usize, nums: &Vec<i64>, ch: &Vec<usize>) -> bool {
            use std::cmp::Reverse;
            use std::collections::BinaryHeap;

            let n = nums.len();
            let mut visited = vec![false; n];
            let mut heap: BinaryHeap<Reverse<i64>> = BinaryHeap::new();
            let mut saved: i64 = 0;

            for i in (1..=x).rev() {
                let idx = ch[i - 1];
                if !visited[idx] {
                    visited[idx] = true;
                    heap.push(Reverse(nums[idx]));
                }
                if let Some(Reverse(v)) = heap.pop() {
                    if v > 0 {
                        saved += v - 1;
                    }
                }
            }

            let total: i64 = nums.iter().sum::<i64>() + n as i64;
            total - saved <= x as i64
        }

        if !feasible(m, &nums_i64, &ch) {
            return -1;
        }

        let mut lo = 1usize;
        let mut hi = m;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if feasible(mid, &nums_i64, &ch) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }
}
```

## Racket

```racket
(define (earliest-second-to-mark-indices nums changeIndices)
  (let* ((n (length nums))
         (m (length changeIndices))
         (nums-vec (list->vector nums))
         (chg-vec (list->vector changeIndices))
         (total-sum (apply + nums)))
    (define (feasible x)
      (if (< x n)
          #f
          (let* ((capacity (- x n))
                 (required (- (+ total-sum n) x))) ; need this much saved time
            (if (<= required 0)
                #t
                (let ((seen (make-vector n 0))
                      (candidates '()))
                  ;; iterate seconds x .. 1 (indices x-1 down to 0)
                  (for ([i (in-range (sub1 x) -1 -1)])
                    (let* ((idx (- (vector-ref chg-vec i) 1))) ; zero‑based index
                      (when (> (vector-ref seen idx) 0)
                        (let ((val (- (vector-ref nums-vec idx) 1)))
                          (when (> val 0)
                            (set! candidates (cons val candidates)))))
                      (vector-set! seen idx (+ (vector-ref seen idx) 1))))
                  (define sorted (sort candidates >))
                  (let loop ((k capacity) (lst sorted) (saved 0))
                    (if (or (= k 0) (null? lst))
                        (>= saved required)
                        (loop (- k 1) (cdr lst) (+ saved (car lst))))))))))
    (let search ((lo 1) (hi m) (ans -1))
      (if (> lo hi)
          ans
          (let ((mid (quotient (+ lo hi) 2)))
            (if (feasible mid)
                (search lo (- mid 1) mid)
                (search (+ mid 1) hi ans)))))))
```

## Erlang

```erlang
-spec earliest_second_to_mark_indices(Nums :: [integer()], ChangeIndices :: [integer()]) -> integer().
earliest_second_to_mark_indices(Nums, ChangeIndices) ->
    N = length(Nums),
    M = length(ChangeIndices),
    NumsT = list_to_tuple(Nums),
    ChangeT = list_to_tuple(ChangeIndices),

    % binary search on answer
    SearchFun = fun(Low, High, Ans) ->
        case Low =< High of
            false -> Ans;
            true ->
                Mid = (Low + High) div 2,
                case can_mark_all(N, NumsT, ChangeT, Mid) of
                    true -> SearchFun(Low, Mid - 1, Mid);
                    false -> SearchFun(Mid + 1, High, Ans)
                end
        end
    end,
    SearchFun(1, M, -1).

%% check if all indices can be marked within X seconds
-spec can_mark_all(integer(), tuple(), tuple(), integer()) -> boolean().
can_mark_all(N, NumsT, ChangeT, X) ->
    Total0 = sum_tuple(NumsT, N) + N,
    loop_check(X, 0, Total0, [], #{}, NumsT, ChangeT, X).

%% recursive processing from second X down to 1
-spec loop_check(integer(), integer(), integer(), [integer()], map(),
                 tuple(), tuple(), integer()) -> boolean().
loop_check(0, _Cnt, Total, _Savings, _Seen, _NumsT, _ChangeT, X) ->
    Total =< X;
loop_check(T, Cnt, Total, Savings, Seen, NumsT, ChangeT, X) ->
    Idx = element(T, ChangeT),
    {NewSavings, NewSeen} =
        case maps:is_key(Idx, Seen) of
            true -> {Savings, Seen};
            false ->
                Save = element(Idx, NumsT) - 1,
                if Save > 0 ->
                        {[Save | Savings], maps:put(Idx, true, Seen)};
                   true ->
                        {Savings, maps:put(Idx, true, Seen)}
                end
        end,
    NewCnt = Cnt + 1,
    {ReducedTotal, ReducedSavings} = reduce_total(Total, NewCnt, NewSavings),
    loop_check(T - 1, NewCnt, ReducedTotal, ReducedSavings, NewSeen, NumsT, ChangeT, X).

%% apply largest savings while total needed exceeds available seconds
-spec reduce_total(integer(), integer(), [integer()]) -> {integer(), [integer()]}.
reduce_total(Total, Cnt, Savings) ->
    if Total =< Cnt orelse Savings == [] ->
            {Total, Savings};
       true ->
            Max = lists:max(Savings),
            NewSavings = lists:delete(Max, Savings),
            reduce_total(Total - Max, Cnt, NewSavings)
    end.

%% sum elements of a tuple from 1 to N
-spec sum_tuple(tuple(), integer()) -> integer().
sum_tuple(Tuple, N) ->
    sum_tuple(Tuple, 1, N, 0).

-spec sum_tuple(tuple(), integer(), integer(), integer()) -> integer().
sum_tuple(_Tuple, I, N, Acc) when I > N -> Acc;
sum_tuple(Tuple, I, N, Acc) ->
    sum_tuple(Tuple, I + 1, N, element(I, Tuple) + Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec earliest_second_to_mark_indices(nums :: [integer], change_indices :: [integer]) :: integer
  def earliest_second_to_mark_indices(nums, change_indices) do
    n = length(nums)
    m = length(change_indices)

    total_needed_base = Enum.sum(nums) + n

    # binary search on answer
    {ans, _} =
      1..m
      |> Enum.reduce({-1, :none}, fn _, {best, _} ->
        # placeholder not used; we'll implement manual binary search instead
        {best, :none}
      end)

    low = 1
    high = m
    best = -1

    while low <= high do
      mid = div(low + high, 2)
      if feasible?(mid, nums, change_indices, total_needed_base) do
        best = mid
        high = mid - 1
      else
        low = mid + 1
      end
    end

    best
  end

  defp feasible?(x, nums, change_indices, base_needed) do
    n = length(nums)

    # count occurrences of each index in first x seconds
    cnt =
      Enum.reduce(1..x, :array.new(n + 1, default: 0), fn s, acc ->
        idx = Enum.at(change_indices, s - 1)
        cur = :array.get(idx, acc)
        :array.set(idx, cur + 1, acc)
      end)

    # compute total extra slots and possible savings
    case Enum.reduce_while(1..n, {:ok, 0, []}, fn i, {:ok, extra_acc, sav_acc} ->
           c = :array.get(i, cnt)

           if c == 0 do
             {:halt, :impossible}
           else
             extra = max(c - 1, 0)
             new_extra = extra_acc + extra

             num_i = Enum.at(nums, i - 1)

             new_sav =
               if c >= 2 and num_i > 0 do
                 [num_i - 1 | sav_acc]
               else
                 sav_acc
               end

             {:cont, {:ok, new_extra, new_sav}}
           end
         end) do
      :impossible ->
        false

      {:ok, total_extra, savings} ->
        # take the largest savings up to total_extra slots
        sorted = Enum.sort(savings, &>=/2)
        sum_save =
          sorted
          |> Enum.take(min(total_extra, length(sorted)))
          |> Enum.sum()

        required = base_needed - sum_save
        required <= x
    end
  end

  # simple while loop macro for readability
  defp while(condition, do: block) do
    if condition do
      block
      while(condition, do: block)
    else
      :ok
    end
  end
end
```
