# 2163. Minimum Difference in Sums After Removal of Elements

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long minimumDifference(vector<int>& nums) {
        int n = nums.size() / 3;
        int total = 3 * n;
        
        // left[k]: sum of n smallest elements in nums[0 .. n-1 + k]
        vector<long long> left(n + 1);
        priority_queue<int> maxHeap; // keep n smallest -> max heap of current candidates
        long long sumLeft = 0;
        for (int i = 0; i < n; ++i) {
            maxHeap.push(nums[i]);
            sumLeft += nums[i];
        }
        left[0] = sumLeft;
        for (int i = n; i < 2 * n; ++i) {
            maxHeap.push(nums[i]);
            sumLeft += nums[i];
            int top = maxHeap.top(); maxHeap.pop();
            sumLeft -= top;
            left[i - (n - 1)] = sumLeft; // index k = i-(n-1)
        }
        
        // right[k]: sum of n largest elements in nums[n + k .. 3n-1]
        vector<long long> right(n + 1);
        priority_queue<int, vector<int>, greater<int>> minHeap; // keep n largest -> min heap
        long long sumRight = 0;
        for (int i = 2 * n; i < total; ++i) {
            minHeap.push(nums[i]);
            sumRight += nums[i];
        }
        right[n] = sumRight; // k = n corresponds to start at index 2n
        for (int i = 2 * n - 1; i >= n; --i) {
            minHeap.push(nums[i]);
            sumRight += nums[i];
            int top = minHeap.top(); minHeap.pop();
            sumRight -= top;
            right[i - n] = sumRight; // k = i - n
        }
        
        long long ans = LLONG_MAX;
        for (int k = 0; k <= n; ++k) {
            ans = min(ans, left[k] - right[k]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long minimumDifference(int[] nums) {
        int total = nums.length;
        int n = total / 3;

        long[] left = new long[total];
        java.util.PriorityQueue<Integer> maxHeap = new java.util.PriorityQueue<>(java.util.Collections.reverseOrder());
        long sumLeft = 0;
        // first n elements
        for (int i = 0; i < n; i++) {
            maxHeap.add(nums[i]);
            sumLeft += nums[i];
        }
        left[n - 1] = sumLeft;

        // expand to indices n .. 2n-1
        for (int i = n; i < 2 * n; i++) {
            maxHeap.add(nums[i]);
            sumLeft += nums[i];
            int removed = maxHeap.poll(); // remove largest, keep smallest n
            sumLeft -= removed;
            left[i] = sumLeft;
        }

        long[] right = new long[total];
        java.util.PriorityQueue<Integer> minHeap = new java.util.PriorityQueue<>();
        long sumRight = 0;
        // last n elements
        for (int i = total - 1; i >= 2 * n; i--) {
            minHeap.add(nums[i]);
            sumRight += nums[i];
        }
        right[2 * n] = sumRight;

        // move leftwards to indices 2n-1 .. n
        for (int i = 2 * n - 1; i >= n; i--) {
            minHeap.add(nums[i]);
            sumRight += nums[i];
            int removed = minHeap.poll(); // remove smallest, keep largest n
            sumRight -= removed;
            right[i] = sumRight;
        }

        long answer = Long.MAX_VALUE;
        for (int i = n - 1; i < 2 * n; i++) {
            long diff = left[i] - right[i + 1];
            if (diff < answer) {
                answer = diff;
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        n = len(nums) // 3

        # prefix sums of smallest n elements up to each position i (i from n-1 to 2n-1)
        max_heap = [-x for x in nums[:n]]          # simulate max-heap
        heapq.heapify(max_heap)
        sum_left = sum(nums[:n])
        pref = [0] * len(nums)
        pref[n - 1] = sum_left

        for i in range(n, 2 * n):
            heapq.heappush(max_heap, -nums[i])
            sum_left += nums[i]
            # remove the largest element among current selection
            removed = -heapq.heappop(max_heap)
            sum_left -= removed
            pref[i] = sum_left

        # suffix sums of largest n elements from each position i (i from 2n down to n)
        min_heap = nums[2 * n:]                   # keep n largest -> min-heap of selected
        heapq.heapify(min_heap)
        sum_right = sum(nums[2 * n:])
        suf = [0] * len(nums)
        suf[2 * n] = sum_right

        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            sum_right += nums[i]
            # remove the smallest among selected largest elements
            removed = heapq.heappop(min_heap)
            sum_right -= removed
            suf[i] = sum_right

        ans = float('inf')
        for i in range(n - 1, 2 * n):
            diff = pref[i] - suf[i + 1]
            if diff < ans:
                ans = diff
        return ans
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        # left[i]: sum of n smallest elements in nums[0..i] for i in [n-1, 2n-1]
        left = [0] * (3 * n)
        max_heap = []
        sum_left = 0
        for x in nums[:n]:
            heapq.heappush(max_heap, -x)
            sum_left += x
        left[n - 1] = sum_left

        for i in range(n, 2 * n):
            heapq.heappush(max_heap, -nums[i])
            sum_left += nums[i]
            removed = -heapq.heappop(max_heap)   # remove largest among current
            sum_left -= removed
            left[i] = sum_left

        # right[i]: sum of n largest elements in nums[i..] for i in [n, 2n]
        right = [0] * (3 * n + 1)   # extra slot for simplicity
        min_heap = []
        sum_right = 0
        for x in nums[2 * n:]:
            heapq.heappush(min_heap, x)
            sum_right += x
        right[2 * n] = sum_right

        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            sum_right += nums[i]
            removed = heapq.heappop(min_heap)   # remove smallest among current
            sum_right -= removed
            right[i] = sum_right

        ans = float('inf')
        for i in range(n - 1, 2 * n):
            diff = left[i] - right[i + 1]
            if diff < ans:
                ans = diff
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int *data;
    int size;
} Heap;

static void maxPush(Heap *h, int val) {
    int i = ++h->size;
    h->data[i] = val;
    while (i > 1 && h->data[i >> 1] < h->data[i]) {
        int tmp = h->data[i];
        h->data[i] = h->data[i >> 1];
        h->data[i >> 1] = tmp;
        i >>= 1;
    }
}
static int maxPop(Heap *h) {
    int top = h->data[1];
    h->data[1] = h->data[h->size--];
    int i = 1;
    while (1) {
        int l = i << 1, r = l + 1, largest = i;
        if (l <= h->size && h->data[l] > h->data[largest]) largest = l;
        if (r <= h->size && h->data[r] > h->data[largest]) largest = r;
        if (largest == i) break;
        int tmp = h->data[i];
        h->data[i] = h->data[largest];
        h->data[largest] = tmp;
        i = largest;
    }
    return top;
}
static void minPush(Heap *h, int val) {
    int i = ++h->size;
    h->data[i] = val;
    while (i > 1 && h->data[i >> 1] > h->data[i]) {
        int tmp = h->data[i];
        h->data[i] = h->data[i >> 1];
        h->data[i >> 1] = tmp;
        i >>= 1;
    }
}
static int minPop(Heap *h) {
    int top = h->data[1];
    h->data[1] = h->data[h->size--];
    int i = 1;
    while (1) {
        int l = i << 1, r = l + 1, smallest = i;
        if (l <= h->size && h->data[l] < h->data[smallest]) smallest = l;
        if (r <= h->size && h->data[r] < h->data[smallest]) smallest = r;
        if (smallest == i) break;
        int tmp = h->data[i];
        h->data[i] = h->data[smallest];
        h->data[smallest] = tmp;
        i = smallest;
    }
    return top;
}

long long minimumDifference(int* nums, int numsSize) {
    int n = numsSize / 3;

    long long *left = (long long *)malloc((n + 1) * sizeof(long long));

    Heap maxh;
    maxh.size = 0;
    maxh.data = (int *)malloc((n + 5) * sizeof(int));
    long long sumLeft = 0;
    for (int i = 0; i < n; ++i) {
        sumLeft += nums[i];
        maxPush(&maxh, nums[i]);
    }
    left[0] = sumLeft; // i = n-1

    for (int i = n; i <= 2 * n - 1; ++i) {
        maxPush(&maxh, nums[i]);
        sumLeft += nums[i];
        int removed = maxPop(&maxh);
        sumLeft -= removed;
        left[i - (n - 1)] = sumLeft; // indices 1..n
    }

    Heap minh;
    minh.size = 0;
    minh.data = (int *)malloc((n + 5) * sizeof(int));
    long long sumRight = 0;
    for (int i = 2 * n; i < 3 * n; ++i) {
        sumRight += nums[i];
        minPush(&minh, nums[i]);
    }

    long long ans = LLONG_MAX;
    // partition after index 2n-1
    if (left[n] - sumRight < ans) ans = left[n] - sumRight;

    for (int i = 2 * n - 1; i >= n; --i) {
        minPush(&minh, nums[i]);
        sumRight += nums[i];
        int removed = minPop(&minh);
        sumRight -= removed;
        long long cand = left[i - n] - sumRight;
        if (cand < ans) ans = cand;
    }

    free(left);
    free(maxh.data);
    free(minh.data);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public long MinimumDifference(int[] nums)
    {
        int len = nums.Length;
        int n = len / 3;

        // left[i]: sum of the n smallest elements in nums[0..i] for i from n-1 to 2n-1
        long[] left = new long[len];
        var maxHeap = new PriorityQueue<int, int>(); // use negative priority to simulate max‑heap
        long sumLeft = 0;
        for (int i = 0; i < n; ++i)
        {
            maxHeap.Enqueue(nums[i], -nums[i]);
            sumLeft += nums[i];
        }
        left[n - 1] = sumLeft;
        for (int i = n; i <= 2 * n - 1; ++i)
        {
            maxHeap.Enqueue(nums[i], -nums[i]);
            sumLeft += nums[i];
            int removed = maxHeap.Dequeue(); // remove the largest among current elements
            sumLeft -= removed;
            left[i] = sumLeft;
        }

        // right[i]: sum of the n largest elements in nums[i..len-1] for i from n to 2n
        long[] right = new long[len];
        var minHeap = new PriorityQueue<int, int>(); // normal min‑heap
        long sumRight = 0;
        for (int i = len - n; i < len; ++i) // indices 2n .. 3n-1
        {
            minHeap.Enqueue(nums[i], nums[i]);
            sumRight += nums[i];
        }
        right[2 * n] = sumRight;
        for (int i = 2 * n - 1; i >= n; --i)
        {
            minHeap.Enqueue(nums[i], nums[i]);
            sumRight += nums[i];
            int removed = minHeap.Dequeue(); // remove the smallest to keep the largest n
            sumRight -= removed;
            right[i] = sumRight;
        }

        long answer = long.MaxValue;
        for (int i = n - 1; i <= 2 * n - 1; ++i)
        {
            long diff = left[i] - right[i + 1];
            if (diff < answer) answer = diff;
        }
        return answer;
    }
}
```

## Javascript

```javascript
class Heap {
    constructor(cmp) {
        this.cmp = cmp; // returns true if a should be before b
        this.arr = [];
    }
    size() { return this.arr.length; }
    peek() { return this.arr[0]; }
    push(val) {
        const a = this.arr;
        a.push(val);
        let i = a.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this.cmp(a[p], a[i])) break;
            [a[p], a[i]] = [a[i], a[p]];
            i = p;
        }
    }
    pop() {
        const a = this.arr;
        if (a.length === 0) return undefined;
        const top = a[0];
        const last = a.pop();
        if (a.length > 0) {
            a[0] = last;
            let i = 0;
            while (true) {
                const l = i * 2 + 1, r = l + 1;
                let best = i;
                if (l < a.length && !this.cmp(a[best], a[l])) best = l;
                if (r < a.length && !this.cmp(a[best], a[r])) best = r;
                if (best === i) break;
                [a[i], a[best]] = [a[best], a[i]];
                i = best;
            }
        }
        return top;
    }
}

/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDifference = function(nums) {
    const m = nums.length;
    const n = m / 3;

    // left[i] = sum of n smallest elements in nums[0..i]
    const left = new Array(m).fill(0);
    const maxHeap = new Heap((a, b) => a >= b); // max-heap
    let sumLeft = 0;
    for (let i = 0; i < n; ++i) {
        maxHeap.push(nums[i]);
        sumLeft += nums[i];
    }
    left[n - 1] = sumLeft;
    for (let i = n; i < 2 * n; ++i) {
        maxHeap.push(nums[i]);
        sumLeft += nums[i];
        const removed = maxHeap.pop(); // remove largest to keep smallest n
        sumLeft -= removed;
        left[i] = sumLeft;
    }

    // right[i] = sum of n largest elements in nums[i..m-1]
    const right = new Array(m).fill(0);
    const minHeap = new Heap((a, b) => a <= b); // min-heap
    let sumRight = 0;
    for (let i = 2 * n; i < m; ++i) {
        minHeap.push(nums[i]);
        sumRight += nums[i];
    }
    right[2 * n] = sumRight;
    for (let i = 2 * n - 1; i >= n; --i) {
        minHeap.push(nums[i]);
        sumRight += nums[i];
        const removed = minHeap.pop(); // remove smallest to keep largest n
        sumRight -= removed;
        right[i] = sumRight;
    }

    let ans = Infinity;
    for (let i = n - 1; i < 2 * n; ++i) {
        const diff = left[i] - right[i + 1];
        if (diff < ans) ans = diff;
    }
    return ans;
};
```

## Typescript

```typescript
class Heap {
    private data: number[];
    private cmp: (a: number, b: number) => boolean;
    constructor(cmp: (a: number, b: number) => boolean) {
        this.data = [];
        this.cmp = cmp;
    }
    size(): number {
        return this.data.length;
    }
    push(val: number): void {
        const a = this.data;
        a.push(val);
        this.siftUp(a.length - 1);
    }
    pop(): number | undefined {
        const a = this.data;
        if (a.length === 0) return undefined;
        const top = a[0];
        const last = a.pop()!;
        if (a.length > 0) {
            a[0] = last;
            this.siftDown(0);
        }
        return top;
    }
    private siftUp(idx: number): void {
        const a = this.data;
        while (idx > 0) {
            const p = (idx - 1) >> 1;
            if (this.cmp(a[p], a[idx])) break;
            [a[p], a[idx]] = [a[idx], a[p]];
            idx = p;
        }
    }
    private siftDown(idx: number): void {
        const a = this.data;
        const n = a.length;
        while (true) {
            let left = idx * 2 + 1;
            let right = left + 1;
            let best = idx;
            if (left < n && !this.cmp(a[best], a[left])) best = left;
            if (right < n && !this.cmp(a[best], a[right])) best = right;
            if (best === idx) break;
            [a[idx], a[best]] = [a[best], a[idx]];
            idx = best;
        }
    }
}

function minimumDifference(nums: number[]): number {
    const m = nums.length;
    const n = m / 3;

    // left[i] = minimal sum of n elements in nums[0..i]
    const left = new Array(2 * n);
    const maxHeap = new Heap((a, b) => a > b); // max-heap
    let sumLeft = 0;
    for (let i = 0; i < n; i++) {
        sumLeft += nums[i];
        maxHeap.push(nums[i]);
    }
    left[n - 1] = sumLeft;
    for (let i = n; i < 2 * n; i++) {
        sumLeft += nums[i];
        maxHeap.push(nums[i]);
        const removed = maxHeap.pop()!;
        sumLeft -= removed;
        left[i] = sumLeft;
    }

    // right side: maximal sum of n elements in suffix starting at i
    const minHeap = new Heap((a, b) => a < b); // min-heap
    let sumRight = 0;
    for (let i = 2 * n; i < m; i++) {
        sumRight += nums[i];
        minHeap.push(nums[i]);
    }

    let answer = Infinity;
    // initial candidate with split after index 2n-1 (i.e., suffix starts at 2n)
    answer = Math.min(answer, left[2 * n - 1] - sumRight);

    for (let i = 2 * n - 1; i >= n; i--) {
        sumRight += nums[i];
        minHeap.push(nums[i]);
        const removed = minHeap.pop()!;
        sumRight -= removed;
        // split after index i-1, suffix starts at i
        answer = Math.min(answer, left[i - 1] - sumRight);
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumDifference($nums) {
        $len = count($nums);
        $n = intdiv($len, 3);

        // Left sums: smallest n elements in prefix [0..i]
        $maxHeap = new SplMaxHeap();
        $left = array_fill(0, $len, 0);
        $sumLeft = 0;
        for ($i = 0; $i < $n; $i++) {
            $maxHeap->insert($nums[$i]);
            $sumLeft += $nums[$i];
        }
        $left[$n - 1] = $sumLeft;
        for ($i = $n; $i < 2 * $n; $i++) {
            $maxHeap->insert($nums[$i]);
            $sumLeft += $nums[$i];
            $removed = $maxHeap->extract(); // remove largest to keep smallest n
            $sumLeft -= $removed;
            $left[$i] = $sumLeft;
        }

        // Right sums: largest n elements in suffix [i..len-1]
        $minHeap = new SplMinHeap();
        $right = array_fill(0, $len, 0);
        $sumRight = 0;
        for ($i = 2 * $n; $i < $len; $i++) {
            $minHeap->insert($nums[$i]);
            $sumRight += $nums[$i];
        }
        $right[2 * $n] = $sumRight;
        for ($i = 2 * $n - 1; $i >= $n; $i--) {
            $minHeap->insert($nums[$i]);
            $sumRight += $nums[$i];
            $removed = $minHeap->extract(); // remove smallest to keep largest n
            $sumRight -= $removed;
            $right[$i] = $sumRight;
        }

        $ans = PHP_INT_MAX;
        for ($i = $n - 1; $i < 2 * $n; $i++) {
            $diff = $left[$i] - $right[$i + 1];
            if ($diff < $ans) {
                $ans = $diff;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumDifference(_ nums: [Int]) -> Int {
        let total = nums.count
        let n = total / 3

        // left sums: sum of smallest n elements in prefix up to each i (i from n-1 to 2n-1)
        var left = [Int](repeating: 0, count: total)
        var maxHeap = Heap<Int>(sort: >)   // max‑heap
        var sumLeft = 0
        for i in 0..<n {
            maxHeap.push(nums[i])
            sumLeft += nums[i]
        }
        left[n - 1] = sumLeft
        if n < total {
            for i in n..<(2 * n) {
                maxHeap.push(nums[i])
                sumLeft += nums[i]
                if let removed = maxHeap.pop() {
                    sumLeft -= removed          // remove the largest, keep smallest n
                }
                left[i] = sumLeft
            }
        }

        // right sums: sum of largest n elements in suffix starting at each i (i from n to 2n)
        var right = [Int](repeating: 0, count: total)
        var minHeap = Heap<Int>(sort: <)   // min‑heap
        var sumRight = 0
        for i in (2 * n)..<total {
            minHeap.push(nums[i])
            sumRight += nums[i]
        }
        right[2 * n] = sumRight
        if n > 0 {
            for i in stride(from: 2 * n - 1, through: n, by: -1) {
                minHeap.push(nums[i])
                sumRight += nums[i]
                if let removed = minHeap.pop() {
                    sumRight -= removed          // remove the smallest, keep largest n
                }
                right[i] = sumRight
            }
        }

        var answer = Int.max
        for i in (n - 1)...(2 * n - 1) {
            let diff = left[i] - right[i + 1]
            if diff < answer { answer = diff }
        }
        return answer
    }
}

// Generic binary heap
struct Heap<T> {
    private var elements: [T] = []
    private let priorityFunction: (T, T) -> Bool   // true means a has higher priority than b

    init(sort: @escaping (T, T) -> Bool) {
        self.priorityFunction = sort
    }

    var isEmpty: Bool { elements.isEmpty }
    var count: Int { elements.count }

    func peek() -> T? { elements.first }

    mutating func push(_ value: T) {
        elements.append(value)
        siftUp(from: elements.count - 1)
    }

    mutating func pop() -> T? {
        guard !elements.isEmpty else { return nil }
        if elements.count == 1 {
            return elements.removeLast()
        } else {
            let value = elements[0]
            elements[0] = elements.removeLast()
            siftDown(from: 0)
            return value
        }
    }

    private mutating func siftUp(from index: Int) {
        var childIdx = index
        var parentIdx = (childIdx - 1) / 2
        while childIdx > 0 && priorityFunction(elements[childIdx], elements[parentIdx]) {
            elements.swapAt(childIdx, parentIdx)
            childIdx = parentIdx
            parentIdx = (childIdx - 1) / 2
        }
    }

    private mutating func siftDown(from index: Int) {
        var parentIdx = index
        while true {
            let left = parentIdx * 2 + 1
            let right = left + 1
            var candidate = parentIdx

            if left < elements.count && priorityFunction(elements[left], elements[candidate]) {
                candidate = left
            }
            if right < elements.count && priorityFunction(elements[right], elements[candidate]) {
                candidate = right
            }
            if candidate == parentIdx { return }
            elements.swapAt(parentIdx, candidate)
            parentIdx = candidate
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumDifference(nums: IntArray): Long {
        val total = nums.size
        val n = total / 3

        val left = LongArray(total)
        val maxHeap = java.util.PriorityQueue<Int>(java.util.Collections.reverseOrder())
        var sumLeft = 0L
        for (i in 0 until n) {
            sumLeft += nums[i].toLong()
            maxHeap.add(nums[i])
        }
        left[n - 1] = sumLeft

        for (i in n until 2 * n) {
            sumLeft += nums[i].toLong()
            maxHeap.add(nums[i])
            val removed = maxHeap.poll()
            sumLeft -= removed.toLong()
            left[i] = sumLeft
        }

        val right = LongArray(total)
        val minHeap = java.util.PriorityQueue<Int>()
        var sumRight = 0L
        for (i in total - 1 downTo 2 * n) {
            sumRight += nums[i].toLong()
            minHeap.add(nums[i])
        }
        right[2 * n] = sumRight

        for (i in 2 * n - 1 downTo n) {
            sumRight += nums[i].toLong()
            minHeap.add(nums[i])
            val removed = minHeap.poll()
            sumRight -= removed.toLong()
            right[i] = sumRight
        }

        var ans = Long.MAX_VALUE
        for (i in n - 1 until 2 * n) {
            val diff = left[i] - right[i + 1]
            if (diff < ans) ans = diff
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:collection';
import 'dart:math';

class Solution {
  int minimumDifference(List<int> nums) {
    int totalLen = nums.length;
    int n = totalLen ~/ 3;

    // Left part: sum of n smallest elements in prefix [0..i]
    List<int> left = List.filled(2 * n, 0);
    var maxHeap = PriorityQueue<int>((a, b) => b.compareTo(a)); // max-heap
    int sumLeft = 0;
    for (int i = 0; i < n; ++i) {
      maxHeap.add(nums[i]);
      sumLeft += nums[i];
    }
    left[n - 1] = sumLeft;
    for (int i = n; i < 2 * n; ++i) {
      maxHeap.add(nums[i]);
      sumLeft += nums[i];
      int removed = maxHeap.removeFirst(); // largest element
      sumLeft -= removed;
      left[i] = sumLeft;
    }

    // Right part: sum of n largest elements in suffix [i..end]
    List<int> right = List.filled(2 * n + 1, 0);
    var minHeap = PriorityQueue<int>((a, b) => a.compareTo(b)); // min-heap
    int sumRight = 0;
    for (int i = 2 * n; i < 3 * n; ++i) {
      minHeap.add(nums[i]);
      sumRight += nums[i];
    }
    right[2 * n] = sumRight;
    for (int i = 2 * n - 1; i >= n; --i) {
      minHeap.add(nums[i]);
      sumRight += nums[i];
      int removed = minHeap.removeFirst(); // smallest element
      sumRight -= removed;
      right[i] = sumRight;
    }

    int answer = pow(2, 63).toInt() - 1; // large initial value
    for (int i = n - 1; i < 2 * n; ++i) {
      int diff = left[i] - right[i + 1];
      if (diff < answer) answer = diff;
    }
    return answer;
  }
}
```

## Golang

```go
import (
	"container/heap"
)

type maxHeap []int

func (h maxHeap) Len() int           { return len(h) }
func (h maxHeap) Less(i, j int) bool { return h[i] > h[j] } // max-heap
func (h maxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *maxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type minHeap []int

func (h minHeap) Len() int           { return len(h) }
func (h minHeap) Less(i, j int) bool { return h[i] < h[j] } // min-heap
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *minHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func minimumDifference(nums []int) int64 {
	n := len(nums) / 3

	left := make([]int64, 2*n)

	mh := &maxHeap{}
	heap.Init(mh)
	var sumLeft int64
	for i := 0; i < n; i++ {
		heap.Push(mh, nums[i])
		sumLeft += int64(nums[i])
	}
	left[n-1] = sumLeft

	for i := n; i < 2*n; i++ {
		heap.Push(mh, nums[i])
		sumLeft += int64(nums[i])
		top := heap.Pop(mh).(int) // remove largest
		sumLeft -= int64(top)
		left[i] = sumLeft
	}

	mih := &minHeap{}
	heap.Init(mih)
	var sumRight int64
	for i := 2 * n; i < 3*n; i++ {
		heap.Push(mih, nums[i])
		sumRight += int64(nums[i])
	}

	ans := int64(^uint64(0) >> 1) // max int64

	for i := 2*n - 1; i >= n; i-- {
		cand := left[i] - sumRight
		if cand < ans {
			ans = cand
		}
		heap.Push(mih, nums[i])
		sumRight += int64(nums[i])
		top := heap.Pop(mih).(int) // remove smallest to keep n largest
		sumRight -= int64(top)
	}

	return ans
}
```

## Ruby

```ruby
class MaxHeap
  def initialize
    @data = []
  end

  def push(val)
    idx = @data.size
    @data << val
    while idx > 0
      parent = (idx - 1) / 2
      break if @data[parent] >= @data[idx]
      @data[parent], @data[idx] = @data[idx], @data[parent]
      idx = parent
    end
  end

  def pop
    return nil if @data.empty?
    top = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      heapify_down(0)
    end
    top
  end

  private

  def heapify_down(idx)
    size = @data.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      largest = idx
      if left < size && @data[left] > @data[largest]
        largest = left
      end
      if right < size && @data[right] > @data[largest]
        largest = right
      end
      break if largest == idx
      @data[idx], @data[largest] = @data[largest], @data[idx]
      idx = largest
    end
  end
end

class MinHeap
  def initialize
    @data = []
  end

  def push(val)
    idx = @data.size
    @data << val
    while idx > 0
      parent = (idx - 1) / 2
      break if @data[parent] <= @data[idx]
      @data[parent], @data[idx] = @data[idx], @data[parent]
      idx = parent
    end
  end

  def pop
    return nil if @data.empty?
    top = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      heapify_down(0)
    end
    top
  end

  private

  def heapify_down(idx)
    size = @data.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      smallest = idx
      if left < size && @data[left] < @data[smallest]
        smallest = left
      end
      if right < size && @data[right] < @data[smallest]
        smallest = right
      end
      break if smallest == idx
      @data[idx], @data[smallest] = @data[smallest], @data[idx]
      idx = smallest
    end
  end
end

# @param {Integer[]} nums
# @return {Integer}
def minimum_difference(nums)
  len = nums.length
  n = len / 3

  # left[i]: minimal sum of n elements in nums[0..i] for i in [n-1, 2n-1]
  left = Array.new(len, 0)

  max_heap = MaxHeap.new
  sum_left = 0
  (0...n).each do |i|
    max_heap.push(nums[i])
    sum_left += nums[i]
  end
  left[n - 1] = sum_left

  (n...2 * n).each do |i|
    max_heap.push(nums[i])
    sum_left += nums[i]
    removed = max_heap.pop
    sum_left -= removed
    left[i] = sum_left
  end

  # right[i]: maximal sum of n elements in nums[i..len-1] for i in [n, 2n]
  right = Array.new(len + 1, 0)

  min_heap = MinHeap.new
  sum_right = 0
  (2 * n...len).each do |i|
    min_heap.push(nums[i])
    sum_right += nums[i]
  end
  right[2 * n] = sum_right

  (2 * n - 1).downto(n) do |i|
    min_heap.push(nums[i])
    sum_right += nums[i]
    removed = min_heap.pop
    sum_right -= removed
    right[i] = sum_right
  end

  ans = Float::INFINITY
  (n - 1...2 * n).each do |i|
    diff = left[i] - right[i + 1]
    ans = diff if diff < ans
  end
  ans.to_i
end
```

## Scala

```scala
import java.util.{PriorityQueue, Collections}

object Solution {
  def minimumDifference(nums: Array[Int]): Long = {
    val n = nums.length / 3
    val totalLen = nums.length

    // Left sums: sum of n smallest elements in prefix [0..i]
    val left = new Array[Long](totalLen)
    val maxHeap = new PriorityQueue[Int](Collections.reverseOrder[Int]())
    var sumLeft: Long = 0L
    var i = 0
    while (i < n) {
      maxHeap.add(nums(i))
      sumLeft += nums(i).toLong
      i += 1
    }
    left(n - 1) = sumLeft
    while (i < 2 * n) {
      maxHeap.add(nums(i))
      sumLeft += nums(i).toLong
      val removed = maxHeap.poll()
      sumLeft -= removed.toLong
      left(i) = sumLeft
      i += 1
    }

    // Right sums: sum of n largest elements in suffix [i..end]
    val right = new Array[Long](totalLen + 1) // extra slot for index totalLen if needed
    val minHeap = new PriorityQueue[Int]()
    var sumRight: Long = 0L
    i = 2 * n
    while (i < 3 * n) {
      minHeap.add(nums(i))
      sumRight += nums(i).toLong
      i += 1
    }
    right(2 * n) = sumRight
    i = 2 * n - 1
    while (i >= n) {
      minHeap.add(nums(i))
      sumRight += nums(i).toLong
      val removed = minHeap.poll()
      sumRight -= removed.toLong
      right(i) = sumRight
      i -= 1
    }

    var ans: Long = Long.MaxValue
    i = n - 1
    while (i < 2 * n) {
      val diff = left(i) - right(i + 1)
      if (diff < ans) ans = diff
      i += 1
    }
    ans
  }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimum_difference(nums: Vec<i32>) -> i64 {
        let m = nums.len();
        let n = m / 3;

        // left[i] = sum of n smallest elements in nums[0..=i], for i in [n-1, 2n-1]
        let mut left = vec![0i64; 2 * n];
        let mut max_heap: BinaryHeap<i32> = BinaryHeap::new();
        let mut sum_left: i64 = 0;
        for i in 0..n {
            max_heap.push(nums[i]);
            sum_left += nums[i] as i64;
        }
        left[n - 1] = sum_left;
        for i in n..2 * n {
            max_heap.push(nums[i]);
            sum_left += nums[i] as i64;
            let removed = max_heap.pop().unwrap(); // largest, discard
            sum_left -= removed as i64;
            left[i] = sum_left;
        }

        // Prepare suffix sums of n largest elements
        let mut min_heap: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
        let mut sum_right: i64 = 0;
        for i in 2 * n..3 * n {
            min_heap.push(Reverse(nums[i]));
            sum_right += nums[i] as i64;
        }

        // Evaluate answer
        let mut answer = left[2 * n - 1] - sum_right; // partition after index 2n-1

        for i in (n..2 * n).rev() {
            min_heap.push(Reverse(nums[i]));
            sum_right += nums[i] as i64;
            let removed = min_heap.pop().unwrap(); // smallest, discard
            sum_right -= removed.0 as i64;

            let cur = left[i - 1] - sum_right;
            if cur < answer {
                answer = cur;
            }
        }

        answer
    }
}
```

## Racket

```racket
(require racket/heap)

(define/contract (minimum-difference nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((arr (list->vector nums))
         (len (vector-length arr))
         (n (/ len 3)))
    ;; left side: smallest n sums up to each position
    (define left-heap (make-heap >)) ; max‑heap
    (define sum-left 0)
    (for ([i (in-range 0 n)])
      (let ((v (vector-ref arr i)))
        (heap-add! left-heap v)
        (set! sum-left (+ sum-left v))))
    (define left-vec (make-vector (+ n 1) 0))
    (vector-set! left-vec 0 sum-left) ; up to index n‑1
    (for ([i (in-range n (* 2 n))])
      (let ((v (vector-ref arr i)))
        (heap-add! left-heap v)
        (set! sum-left (+ sum-left v))
        (define max-val (heap-remove-min! left-heap)) ; remove largest
        (set! sum-left (- sum-left max-val))
        (vector-set! left-vec (- i (sub1 n)) sum-left))) ; index i‑(n‑1)

    ;; right side: largest n sums from each suffix
    (define right-heap (make-heap <)) ; min‑heap
    (define sum-right 0)
    (for ([i (in-range (* 2 n) len)])
      (let ((v (vector-ref arr i)))
        (heap-add! right-heap v)
        (set! sum-right (+ sum-right v))))
    (define right-vec (make-vector (+ n 1) 0))
    (vector-set! right-vec 0 sum-right) ; suffix starting at 2n
    (for ([i (in-range (sub1 (* 2 n)) (sub1 n) -1)]) ; from 2n‑1 down to n
      (let ((v (vector-ref arr i)))
        (heap-add! right-heap v)
        (set! sum-right (+ sum-right v))
        (define min-val (heap-remove-min! right-heap)) ; remove smallest
        (set! sum-right (- sum-right min-val))
        (vector-set! right-vec (- (* 2 n) i) sum-right))) ; index 2n‑i

    ;; compute minimal difference
    (let ((ans (- (vector-ref left-vec 0) (vector-ref right-vec n))))
      (for ([l (in-range 1 (+ n 1))])
        (define r (- n l))
        (define diff (- (vector-ref left-vec l) (vector-ref right-vec r)))
        (when (< diff ans)
          (set! ans diff)))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_difference/1]).
-spec minimum_difference(Nums :: [integer()]) -> integer().
minimum_difference(Nums) ->
    Tuple = list_to_tuple(Nums),
    Len = tuple_size(Tuple),
    N = Len div 3,
    {TreeF0, SumF0} = init_tree_sum(Tuple, 0, N - 1, gb_trees:empty()),
    PrefAcc0 = [SumF0],
    {_TF, _SF, PrefAcc} = forward_loop(Tuple, N, 2 * N - 1, TreeF0, SumF0, PrefAcc0),
    PrefList = lists:reverse(PrefAcc),

    {TreeB0, SumB0} = init_tree_sum(Tuple, 2 * N, 3 * N - 1, gb_trees:empty()),
    SuffAcc0 = [SumB0],
    {_TB, _SB, SuffAcc} = backward_loop(Tuple, 2 * N - 1, N, TreeB0, SumB0, SuffAcc0),
    SuffList = lists:reverse(SuffAcc),

    compute_min(PrefList, SuffList).

init_tree_sum(_Tuple, Start, End, _Tree) when Start > End ->
    {gb_trees:empty(), 0};
init_tree_sum(Tuple, Start, End, Tree) ->
    init_tree_sum_loop(Tuple, Start, End, Tree, 0).

init_tree_sum_loop(_Tuple, I, End, Tree, Sum) when I > End ->
    {Tree, Sum};
init_tree_sum_loop(Tuple, I, End, Tree, Sum) ->
    V = element(I + 1, Tuple),
    NewTree = add(Tree, V),
    init_tree_sum_loop(Tuple, I + 1, End, NewTree, Sum + V).

add(Tree, V) ->
    case gb_trees:lookup(V, Tree) of
        {value, C} -> gb_trees:update(V, C + 1, Tree);
        none -> gb_trees:insert(V, 1, Tree)
    end.

remove_one(Tree, V) ->
    case gb_trees:lookup(V, Tree) of
        {value, 1} -> gb_trees:delete(V, Tree);
        {value, C} when C > 1 -> gb_trees:update(V, C - 1, Tree)
    end.

forward_loop(_Tuple, I, EndI, Tree, Sum, Acc) when I > EndI ->
    {Tree, Sum, Acc};
forward_loop(Tuple, I, EndI, Tree, Sum, Acc) ->
    V = element(I + 1, Tuple),
    Tree1 = add(Tree, V),
    Sum1 = Sum + V,
    {MaxV, _} = gb_trees:largest(Tree1),
    Tree2 = remove_one(Tree1, MaxV),
    Sum2 = Sum1 - MaxV,
    forward_loop(Tuple, I + 1, EndI, Tree2, Sum2, [Sum2 | Acc]).

backward_loop(_Tuple, I, Limit, Tree, Sum, Acc) when I < Limit ->
    {Tree, Sum, Acc};
backward_loop(Tuple, I, Limit, Tree, Sum, Acc) ->
    V = element(I + 1, Tuple),
    Tree1 = add(Tree, V),
    Sum1 = Sum + V,
    {MinV, _} = gb_trees:smallest(Tree1),
    Tree2 = remove_one(Tree1, MinV),
    Sum2 = Sum1 - MinV,
    backward_loop(Tuple, I - 1, Limit, Tree2, Sum2, [Sum2 | Acc]).

compute_min([P|Ps], [S|Ss]) ->
    Diff0 = P - S,
    compute_min(Ps, Ss, Diff0).

compute_min([], [], Min) -> Min;
compute_min([P|Ps], [S|Ss], Min) ->
    D = P - S,
    NewMin = if D < Min -> D; true -> Min end,
    compute_min(Ps, Ss, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_difference(nums :: [integer]) :: integer
  def minimum_difference(nums) do
    tup = List.to_tuple(nums)
    len = tuple_size(tup)
    n = div(len, 3)

    # Left side: smallest n sums for prefixes
    {left_sums, _} =
      0..(n - 1)
      |> Enum.reduce({%{}, {:gb_trees.empty(), 0, 0}}, fn i, {map, {tree, sum, cnt}} ->
        val = elem(tup, i)
        tree = inc(tree, val)
        sum = sum + val
        cnt = cnt + 1
        map = Map.put(map, i, sum)
        {map, {tree, sum, cnt}}
      end)

    {left_sums, left_tree, left_sum, _} =
      Enum.reduce(n..(2 * n - 1), {left_sums, elem(left_sums, 0) |> elem(1), Map.fetch!(left_sums, n - 1), n}, fn i,
                                                                                                                {map, tree, sum, cnt} ->
        val = elem(tup, i)
        tree = inc(tree, val)
        sum = sum + val
        cnt = cnt + 1

        if cnt > n do
          {max_key, _} = :gb_trees.largest(tree)
          sum = sum - max_key
          tree = dec(tree, max_key)
          cnt = cnt - 1
        end

        map = Map.put(map, i, sum)
        {map, tree, sum, cnt}
      end)

    # Right side: largest n sums for suffixes
    start_idx = 2 * n
    {right_sums, _} =
      start_idx..(len - 1)
      |> Enum.reduce({%{}, {:gb_trees.empty(), 0, 0}}, fn i, {map, {tree, sum, cnt}} ->
        val = elem(tup, i)
        tree = inc(tree, val)
        sum = sum + val
        cnt = cnt + 1
        map = Map.put(map, i, sum)
        {map, {tree, sum, cnt}}
      end)

    {right_sums, _right_tree, right_sum, _} =
      Enum.reduce((start_idx - 1)..n, {right_sums, elem(right_sums, 0) |> elem(1), Map.fetch!(right_sums, start_idx), n}, fn i,
                                                                                                                    {map, tree, sum, cnt} ->
        val = elem(tup, i)
        tree = inc(tree, val)
        sum = sum + val
        cnt = cnt + 1

        if cnt > n do
          {min_key, _} = :gb_trees.smallest(tree)
          sum = sum - min_key
          tree = dec(tree, min_key)
          cnt = cnt - 1
        end

        map = Map.put(map, i, sum)
        {map, tree, sum, cnt}
      end)

    # Compute minimal difference
    Enum.reduce((n - 1)..(2 * n - 1), 1 <<< 62, fn i, acc ->
      left_val = Map.fetch!(left_sums, i)
      right_val = Map.fetch!(right_sums, i + 1)
      diff = left_val - right_val
      if diff < acc, do: diff, else: acc
    end)
  end

  defp inc(tree, key) do
    case :gb_trees.lookup(key, tree) do
      {:value, cnt} -> :gb_trees.update(key, fn _ -> cnt + 1 end, tree)
      :none -> :gb_trees.insert(key, 1, tree)
    end
  end

  defp dec(tree, key) do
    case :gb_trees.lookup(key, tree) do
      {:value, 1} -> :gb_trees.delete(key, tree)
      {:value, cnt} -> :gb_trees.update(key, fn _ -> cnt - 1 end, tree)
    end
  end
end
```
