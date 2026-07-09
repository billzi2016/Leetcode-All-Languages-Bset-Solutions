# 0218. The Skyline Problem

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<pair<long long,int>> events;
        events.reserve(buildings.size()*2);
        for (auto &b : buildings) {
            int l = b[0], r = b[1], h = b[2];
            events.emplace_back(l, -h); // left edge
            events.emplace_back(r,  h); // right edge
        }
        sort(events.begin(), events.end(), [](const auto& a, const auto& b){
            if (a.first != b.first) return a.first < b.first;
            return a.second < b.second; // negative heights before positive, higher left before lower left
        });
        
        multiset<int> heights;
        heights.insert(0);
        int prev = 0;
        vector<vector<int>> result;
        for (auto &e : events) {
            long long x = e.first;
            int h = e.second;
            if (h < 0) { // entering building
                heights.insert(-h);
            } else { // leaving building
                auto it = heights.find(h);
                if (it != heights.end()) heights.erase(it);
            }
            int cur = *heights.rbegin();
            if (cur != prev) {
                result.push_back({(int)x, cur});
                prev = cur;
            }
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<int[]> events = new ArrayList<>();
        for (int[] b : buildings) {
            // start event has negative height
            events.add(new int[]{b[0], -b[2]});
            // end event has positive height
            events.add(new int[]{b[1], b[2]});
        }
        Collections.sort(events, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(a[1], b[1]); // start (-h) before end (+h), higher start first
        });

        TreeMap<Integer, Integer> heightCount = new TreeMap<>(Collections.reverseOrder());
        heightCount.put(0, 1);
        int prevMax = 0;
        List<List<Integer>> result = new ArrayList<>();

        for (int[] e : events) {
            int x = e[0];
            int h = e[1];
            if (h < 0) { // start
                int height = -h;
                heightCount.put(height, heightCount.getOrDefault(height, 0) + 1);
            } else { // end
                int cnt = heightCount.get(h);
                if (cnt == 1) {
                    heightCount.remove(h);
                } else {
                    heightCount.put(h, cnt - 1);
                }
            }
            int curMax = heightCount.firstKey();
            if (curMax != prevMax) {
                result.add(Arrays.asList(x, curMax));
                prevMax = curMax;
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        import heapq
        # Create events: (x, height, right)
        # start event has negative height to ensure it comes before end at same x
        events = []
        for L, R, H in buildings:
            events.append((L, -H, R))  # entering building
            events.append((R, H, None))  # leaving building
        events.sort(key=lambda x: (x[0], x[1]))
        
        result = []
        # heap stores (-height, right)
        live = [(0, float('inf'))]  # ground
        prev_height = 0
        i = 0
        n = len(events)
        while i < n:
            cur_x = events[i][0]
            # process all events at cur_x
            while i < n and events[i][0] == cur_x:
                x, h, r = events[i]
                if h < 0:  # start event
                    heapq.heappush(live, (h, r))
                else:
                    # end event; actual removal is lazy via right coordinate check later
                    pass
                i += 1
            # remove buildings that have ended before or at cur_x
            while live and live[0][1] <= cur_x:
                heapq.heappop(live)
            curr_height = -live[0][0]
            if curr_height != prev_height:
                result.append([cur_x, curr_height])
                prev_height = curr_height
        return result
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create events: (x, height, right)
        # start event has negative height to ensure it comes before end at same x
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))
        events.sort()
        
        result = []
        # heap of (neg_height, right)
        live = [(0, float('inf'))]  # ground
        for x, h, r in events:
            if h < 0:  # start of building
                heapq.heappush(live, (h, r))
            else:      # end of building
                # remove buildings that have ended before or at x
                while live and live[0][1] <= x:
                    heapq.heappop(live)
            current_height = -live[0][0]
            if not result or result[-1][1] != current_height:
                result.append([x, current_height])
        return result
```

## C

```c
#include <stdlib.h>

struct Event {
    int x;
    int h;   // negative for start, positive for end
    int r;   // right coordinate for start events
};

static int cmpEvent(const void *a, const void *b) {
    const struct Event *e1 = (const struct Event *)a;
    const struct Event *e2 = (const struct Event *)b;
    if (e1->x != e2->x) return e1->x < e2->x ? -1 : 1;
    if (e1->h != e2->h) return e1->h < e2->h ? -1 : 1;
    return 0;
}

/* Max-heap for building heights with right endpoints */
struct Node {
    int h;   // height
    int r;   // right coordinate
};

struct Heap {
    struct Node *data;
    int size;
    int cap;
};

static void heapInit(struct Heap *hp) {
    hp->cap = 64;
    hp->size = 0;
    hp->data = (struct Node *)malloc(hp->cap * sizeof(struct Node));
}

static void heapSwap(struct Node *a, struct Node *b) {
    struct Node tmp = *a;
    *a = *b;
    *b = tmp;
}

static void heapPush(struct Heap *hp, int h, int r) {
    if (hp->size == hp->cap) {
        hp->cap <<= 1;
        hp->data = (struct Node *)realloc(hp->data, hp->cap * sizeof(struct Node));
    }
    int i = hp->size++;
    hp->data[i].h = h;
    hp->data[i].r = r;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (hp->data[p].h >= hp->data[i].h) break;
        heapSwap(&hp->data[p], &hp->data[i]);
        i = p;
    }
}

static void heapPop(struct Heap *hp) {
    if (hp->size == 0) return;
    hp->data[0] = hp->data[--hp->size];
    int i = 0;
    while (1) {
        int l = i * 2 + 1;
        int r = l + 1;
        if (l >= hp->size) break;
        int largest = l;
        if (r < hp->size && hp->data[r].h > hp->data[l].h) largest = r;
        if (hp->data[i].h >= hp->data[largest].h) break;
        heapSwap(&hp->data[i], &hp->data[largest]);
        i = largest;
    }
}

static int heapTopHeight(struct Heap *hp) {
    return hp->size ? hp->data[0].h : 0;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** getSkyline(int** buildings, int buildingsSize, int* buildingsColSize,
                 int* returnSize, int*** returnColumnSizes) {
    (void)buildingsColSize;  // unused

    if (buildingsSize == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    int eventsCount = buildingsSize * 2;
    struct Event *events = (struct Event *)malloc(eventsCount * sizeof(struct Event));
    for (int i = 0; i < buildingsSize; ++i) {
        int l = buildings[i][0];
        int r = buildings[i][1];
        int h = buildings[i][2];
        events[2 * i]     = (struct Event){l, -h, r}; // start
        events[2 * i + 1] = (struct Event){r,  h, 0}; // end
    }

    qsort(events, eventsCount, sizeof(struct Event), cmpEvent);

    struct Heap hp;
    heapInit(&hp);

    int maxPoints = eventsCount + 1;
    int **result = (int **)malloc(maxPoints * sizeof(int *));
    int *colSizes = (int *)malloc(maxPoints * sizeof(int));
    int resCnt = 0;

    int idx = 0;
    while (idx < eventsCount) {
        int curX = events[idx].x;

        /* Process all events at curX */
        while (idx < eventsCount && events[idx].x == curX) {
            if (events[idx].h < 0) { // start event
                heapPush(&hp, -events[idx].h, events[idx].r);
            }
            /* end events are handled lazily */
            ++idx;
        }

        /* Remove buildings that have ended */
        while (hp.size && hp.data[0].r <= curX) {
            heapPop(&hp);
        }

        int curH = heapTopHeight(&hp);
        if (resCnt == 0 || result[resCnt - 1][1] != curH) {
            int *pt = (int *)malloc(2 * sizeof(int));
            pt[0] = curX;
            pt[1] = curH;
            result[resCnt] = pt;
            colSizes[resCnt] = 2;
            ++resCnt;
        }
    }

    free(events);
    free(hp.data);

    *returnSize = resCnt;
    *returnColumnSizes = &colSizes;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public IList<IList<int>> GetSkyline(int[][] buildings) {
        // Event structure: x coordinate and height (negative for start, positive for end)
        var events = new List<(int x, int h)>();
        foreach (var b in buildings) {
            int left = b[0], right = b[1], height = b[2];
            events.Add((left, -height)); // building start
            events.Add((right, height)); // building end
        }
        // Sort by x, then by h so that starts (-h) come before ends (+h) at same x,
        // and taller starts processed before shorter ones.
        events.Sort((a, b) => {
            if (a.x != b.x) return a.x - b.x;
            return a.h - b.h;
        });

        // Multiset of active heights with descending order to get max quickly
        var heights = new SortedDictionary<int, int>(Comparer<int>.Create((a, b) => b.CompareTo(a)));
        heights[0] = 1; // ground

        var result = new List<IList<int>>();
        int prevMax = 0;
        int i = 0;
        while (i < events.Count) {
            int curX = events[i].x;
            // Process all events at the same x-coordinate
            while (i < events.Count && events[i].x == curX) {
                int h = events[i].h;
                if (h < 0) { // start of building
                    int height = -h;
                    if (heights.ContainsKey(height))
                        heights[height]++;
                    else
                        heights[height] = 1;
                } else { // end of building
                    int height = h;
                    if (heights.ContainsKey(height)) {
                        if (--heights[height] == 0)
                            heights.Remove(height);
                    }
                }
                i++;
            }

            int curMax = heights.First().Key; // highest active height
            if (curMax != prevMax) {
                result.Add(new List<int> { curX, curMax });
                prevMax = curMax;
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} buildings
 * @return {number[][]}
 */
var getSkyline = function(buildings) {
    // Max-heap implementation for [height, right] pairs
    class MaxHeap {
        constructor() {
            this.heap = [];
        }
        size() {
            return this.heap.length;
        }
        peek() {
            return this.heap[0];
        }
        push(item) {
            const h = this.heap;
            h.push(item);
            let i = h.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p][0] >= h[i][0]) break;
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
                    if (l < h.length && h[l][0] > h[largest][0]) largest = l;
                    if (r < h.length && h[r][0] > h[largest][0]) largest = r;
                    if (largest === i) break;
                    [h[i], h[largest]] = [h[largest], h[i]];
                    i = largest;
                }
            }
            return top;
        }
    }

    const events = [];
    for (const b of buildings) {
        const [L, R, H] = b;
        events.push([L, -H, R]); // start event
        events.push([R, H, 0]);   // end event
    }
    events.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        return a[1] - b[1]; // negative heights before positive; higher starts first
    });

    const heap = new MaxHeap();
    heap.push([0, Infinity]); // ground sentinel

    let prevHeight = 0;
    const result = [];

    for (const ev of events) {
        const [x, h, r] = ev;
        if (h < 0) {
            // start event: add building
            heap.push([-h, r]);
        }
        // remove buildings that have ended before or at current x
        while (heap.size() && heap.peek()[1] <= x) {
            heap.pop();
        }
        const curHeight = heap.peek()[0];
        if (curHeight !== prevHeight) {
            result.push([x, curHeight]);
            prevHeight = curHeight;
        }
    }

    return result;
};
```

## Typescript

```typescript
function getSkyline(buildings: number[][]): number[][] {
    const events: [number, number][] = [];
    for (const b of buildings) {
        const [l, r, h] = b;
        events.push([l, -h]); // start event
        events.push([r, h]);  // end event
    }
    events.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);

    class MaxHeap {
        data: number[] = [];
        peek(): number { return this.data.length ? this.data[0] : 0; }
        push(val: number): void {
            const arr = this.data;
            arr.push(val);
            let i = arr.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (arr[p] >= arr[i]) break;
                [arr[p], arr[i]] = [arr[i], arr[p]];
                i = p;
            }
        }
        pop(): number | undefined {
            const arr = this.data;
            if (!arr.length) return undefined;
            const top = arr[0];
            const last = arr.pop()!;
            if (arr.length) {
                arr[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1,
                        r = l + 1,
                        largest = i;
                    if (l < arr.length && arr[l] > arr[largest]) largest = l;
                    if (r < arr.length && arr[r] > arr[largest]) largest = r;
                    if (largest === i) break;
                    [arr[i], arr[largest]] = [arr[largest], arr[i]];
                    i = largest;
                }
            }
            return top;
        }
    }

    const heap = new MaxHeap();
    const toRemove = new Map<number, number>();
    const result: number[][] = [];
    let prevHeight = 0;

    for (const [x, h] of events) {
        if (h < 0) {
            heap.push(-h);
        } else {
            toRemove.set(h, (toRemove.get(h) ?? 0) + 1);
        }

        while (heap.data.length) {
            const top = heap.peek();
            const cnt = toRemove.get(top);
            if (cnt) {
                if (cnt === 1) toRemove.delete(top);
                else toRemove.set(top, cnt - 1);
                heap.pop();
            } else break;
        }

        const curHeight = heap.peek() || 0;
        if (curHeight !== prevHeight) {
            result.push([x, curHeight]);
            prevHeight = curHeight;
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $buildings
     * @return Integer[][]
     */
    function getSkyline($buildings) {
        $events = [];
        foreach ($buildings as $b) {
            [$L, $R, $H] = $b;
            // start event with negative height to ensure it comes before end at same x
            $events[] = [$L, -$H];
            // end event with positive height
            $events[] = [$R, $H];
        }

        usort($events, function ($a, $b) {
            if ($a[0] == $b[0]) {
                return $a[1] <=> $b[1]; // start (-h) before end (+h)
            }
            return $a[0] <=> $b[0];
        });

        // Max-heap using SplMaxHeap
        $heap = new class extends SplMaxHeap {
            protected function compare($value1, $value2) {
                // default max behavior
                if ($value1 === $value2) return 0;
                return ($value1 < $value2) ? -1 : 1;
            }
        };
        $heap->insert(0);
        $counter = [0 => 1]; // height => count

        $result = [];
        $prevHeight = 0;
        $n = count($events);
        $i = 0;

        while ($i < $n) {
            $x = $events[$i][0];
            // process all events at the same x
            while ($i < $n && $events[$i][0] == $x) {
                $h = $events[$i][1];
                if ($h < 0) { // start
                    $height = -$h;
                    $heap->insert($height);
                    $counter[$height] = ($counter[$height] ?? 0) + 1;
                } else { // end
                    $height = $h;
                    if (isset($counter[$height])) {
                        $counter[$height]--;
                        if ($counter[$height] == 0) {
                            unset($counter[$height]);
                        }
                    }
                }
                $i++;
            }

            // lazy removal of heights no longer present
            while (!$heap->isEmpty()) {
                $top = $heap->current();
                if (isset($counter[$top])) {
                    break;
                }
                $heap->extract();
            }

            $currHeight = $heap->isEmpty() ? 0 : $heap->current();

            if ($currHeight != $prevHeight) {
                $result[] = [$x, $currHeight];
                $prevHeight = $currHeight;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    struct MaxHeap {
        private var data: [(height: Int, right: Int)] = []
        
        mutating func push(_ element: (Int, Int)) {
            data.append(element)
            var idx = data.count - 1
            while idx > 0 {
                let parent = (idx - 1) >> 1
                if data[parent].height >= data[idx].height { break }
                data.swapAt(parent, idx)
                idx = parent
            }
        }
        
        mutating func pop() -> (Int, Int)? {
            guard !data.isEmpty else { return nil }
            let top = data[0]
            let last = data.removeLast()
            if !data.isEmpty {
                data[0] = last
                var idx = 0
                while true {
                    let left = idx * 2 + 1
                    let right = left + 1
                    var largest = idx
                    if left < data.count && data[left].height > data[largest].height {
                        largest = left
                    }
                    if right < data.count && data[right].height > data[largest].height {
                        largest = right
                    }
                    if largest == idx { break }
                    data.swapAt(idx, largest)
                    idx = largest
                }
            }
            return top
        }
        
        func peek() -> (Int, Int)? {
            return data.first
        }
    }
    
    func getSkyline(_ buildings: [[Int]]) -> [[Int]] {
        var events: [(x: Int, h: Int, r: Int)] = []
        for b in buildings {
            let left = b[0], right = b[1], height = b[2]
            events.append((left, -height, right))   // start event
            events.append((right, 0, 0))           // end event placeholder
        }
        events.sort {
            if $0.x != $1.x { return $0.x < $1.x }
            return $0.h < $1.h          // start (-h) before end (0)
        }
        
        var heap = MaxHeap()
        var result: [[Int]] = []
        var i = 0
        while i < events.count {
            let curX = events[i].x
            // process all events at curX
            while i < events.count && events[i].x == curX {
                let h = events[i].h
                if h < 0 {                     // start event
                    heap.push((-h, events[i].r))
                }
                // end events are handled by lazy removal
                i += 1
            }
            // remove buildings that have ended
            while let top = heap.peek(), top.right <= curX {
                _ = heap.pop()
            }
            let currentHeight = heap.peek()?.height ?? 0
            if result.isEmpty || result.last![1] != currentHeight {
                result.append([curX, currentHeight])
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getSkyline(buildings: Array<IntArray>): List<List<Int>> {
        val events = mutableListOf<Pair<Int, Int>>()
        for (b in buildings) {
            val l = b[0]
            val r = b[1]
            val h = b[2]
            events.add(Pair(l, -h)) // start event
            events.add(Pair(r, h))  // end event
        }
        events.sortWith { a, b ->
            if (a.first != b.first) a.first - b.first else a.second - b.second
        }

        val pq = java.util.PriorityQueue<Int>(compareByDescending { it })
        pq.offer(0)
        val toRemove = java.util.HashMap<Int, Int>()
        var prevHeight = 0
        val result = mutableListOf<List<Int>>()

        for ((x, h) in events) {
            if (h < 0) {
                pq.offer(-h)
            } else {
                toRemove[h] = toRemove.getOrDefault(h, 0) + 1
            }

            while (true) {
                val top = pq.peek() ?: break
                val cnt = toRemove[top]
                if (cnt != null && cnt > 0) {
                    pq.poll()
                    if (cnt == 1) toRemove.remove(top) else toRemove[top] = cnt - 1
                } else {
                    break
                }
            }

            val curHeight = pq.peek() ?: 0
            if (curHeight != prevHeight) {
                result.add(listOf(x, curHeight))
                prevHeight = curHeight
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> getSkyline(List<List<int>> buildings) {
    // Create events: start with negative height, end with positive height
    List<List<int>> events = [];
    for (var b in buildings) {
      int l = b[0], r = b[1], h = b[2];
      events.add([l, -h]); // start event
      events.add([r, h]);  // end event
    }
    // Sort by x, then by height
    events.sort((a, b) {
      if (a[0] != b[0]) return a[0] - b[0];
      return a[1] - b[1];
    });

    // Max-heap implementation
    List<int> heap = [];
    void heapPush(int val) {
      heap.add(val);
      int idx = heap.length - 1;
      while (idx > 0) {
        int parent = (idx - 1) >> 1;
        if (heap[parent] >= heap[idx]) break;
        int tmp = heap[parent];
        heap[parent] = heap[idx];
        heap[idx] = tmp;
        idx = parent;
      }
    }

    void heapPop() {
      int n = heap.length;
      if (n == 0) return;
      if (n == 1) {
        heap.removeLast();
        return;
      }
      heap[0] = heap.removeLast();
      int idx = 0;
      while (true) {
        int left = idx * 2 + 1;
        int right = left + 1;
        int largest = idx;
        if (left < heap.length && heap[left] > heap[largest]) largest = left;
        if (right < heap.length && heap[right] > heap[largest]) largest = right;
        if (largest == idx) break;
        int tmp = heap[idx];
        heap[idx] = heap[largest];
        heap[largest] = tmp;
        idx = largest;
      }
    }

    int heapPeek() => heap[0];

    // Height counter for lazy removal
    Map<int, int> cnt = {0: 1};
    heapPush(0);

    List<List<int>> result = [];
    int i = 0;
    while (i < events.length) {
      int x = events[i][0];
      // Process all events at the same x-coordinate
      while (i < events.length && events[i][0] == x) {
        int h = events[i][1];
        if (h < 0) {
          int height = -h;
          cnt[height] = (cnt[height] ?? 0) + 1;
          heapPush(height);
        } else {
          int height = h;
          int c = cnt[height]! - 1;
          if (c == 0) {
            cnt.remove(height);
          } else {
            cnt[height] = c;
          }
        }
        i++;
      }
      // Clean up heap top that are no longer present
      while (heap.isNotEmpty && !cnt.containsKey(heapPeek())) {
        heapPop();
      }
      int curHeight = heap.isEmpty ? 0 : heapPeek();
      if (result.isEmpty || result.last[1] != curHeight) {
        result.add([x, curHeight]);
      }
    }
    return result;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
	"sort"
)

type event struct {
	x int
	h int // negative for start, positive for end
}

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

func getSkyline(buildings [][]int) [][]int {
	if len(buildings) == 0 {
		return [][]int{}
	}
	events := make([]event, 0, len(buildings)*2)
	for _, b := range buildings {
		l, r, ht := b[0], b[1], b[2]
		events = append(events, event{x: l, h: -ht}) // start
		events = append(events, event{x: r, h: ht})  // end
	}
	sort.Slice(events, func(i, j int) bool {
		if events[i].x == events[j].x {
			return events[i].h < events[j].h
		}
		return events[i].x < events[j].x
	})

	freq := make(map[int]int)
	h := &maxHeap{}
	heap.Init(h)
	heap.Push(h, 0)
	freq[0] = 1

	prevHeight := 0
	result := [][]int{}

	for _, e := range events {
		if e.h < 0 { // start
			height := -e.h
			freq[height]++
			heap.Push(h, height)
		} else { // end
			height := e.h
			freq[height]--
		}
		// clean up removed heights
		for h.Len() > 0 {
			top := (*h)[0]
			if cnt, ok := freq[top]; !ok || cnt == 0 {
				heap.Pop(h)
			} else {
				break
			}
		}
		curHeight := 0
		if h.Len() > 0 {
			curHeight = (*h)[0]
		}
		if curHeight != prevHeight {
			result = append(result, []int{e.x, curHeight})
			prevHeight = curHeight
		}
	}
	return result
}
```

## Ruby

```ruby
def get_skyline(buildings)
  events = []
  buildings.each do |l, r, h|
    events << [l, -h]
    events << [r, h]
  end
  events.sort_by! { |x, h| [x, h] }

  heap = []
  cnt = Hash.new(0)

  push = lambda do |val|
    heap << val
    i = heap.size - 1
    while i > 0
      p = (i - 1) / 2
      break if heap[p] >= heap[i]
      heap[p], heap[i] = heap[i], heap[p]
      i = p
    end
  end

  pop = lambda do
    return nil if heap.empty?
    top = heap[0]
    last = heap.pop
    unless heap.empty?
      heap[0] = last
      i = 0
      size = heap.size
      loop do
        l = i * 2 + 1
        r = l + 1
        break if l >= size
        larger = (r < size && heap[r] > heap[l]) ? r : l
        break if heap[i] >= heap[larger]
        heap[i], heap[larger] = heap[larger], heap[i]
        i = larger
      end
    end
    top
  end

  peek = lambda { heap.empty? ? nil : heap[0] }

  result = []
  events.each do |x, h|
    if h < 0
      height = -h
      push.call(height)
      cnt[height] += 1
    else
      cnt[h] -= 1
    end

    while (top = peek.call) && cnt[top] == 0
      pop.call
    end

    cur = peek.call || 0
    if result.empty? || result[-1][1] != cur
      result << [x, cur]
    end
  end

  result
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{ArrayBuffer, ListBuffer}
  import java.util.{TreeMap, Collections}

  def getSkyline(buildings: Array[Array[Int]]): List[List[Int]] = {
    val events = new ArrayBuffer[(Int, Int)]()
    for (b <- buildings) {
      val l = b(0)
      val r = b(1)
      val h = b(2)
      events += ((l, -h)) // start event
      events += ((r,  h)) // end event
    }

    val sorted = events.sortWith { case ((x1, h1), (x2, h2)) =>
      if (x1 != x2) x1 < x2 else h1 < h2
    }

    val active = new TreeMap[Int, Int](Collections.reverseOrder[Int]())
    active.put(0, 1) // ground

    var prevHeight = 0
    val result = ListBuffer[List[Int]]()

    for ((x, h) <- sorted) {
      if (h < 0) {
        val height = -h
        active.put(height, active.getOrDefault(height, 0) + 1)
      } else {
        val cnt = active.getOrDefault(h, 0) - 1
        if (cnt == 0) active.remove(h) else active.put(h, cnt)
      }

      val currHeight = active.firstKey()
      if (currHeight != prevHeight) {
        result += List(x, currHeight)
        prevHeight = currHeight
      }
    }

    result.toList
  }
}
```

## Rust

```rust
use std::collections::{BinaryHeap, HashMap};

impl Solution {
    pub fn get_skyline(buildings: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut events: Vec<(i32, i32)> = Vec::with_capacity(buildings.len() * 2);
        for b in buildings.iter() {
            let l = b[0];
            let r = b[1];
            let h = b[2];
            events.push((l, -h)); // start event
            events.push((r, h));  // end event
        }
        events.sort_by(|a, b| {
            if a.0 != b.0 {
                a.0.cmp(&b.0)
            } else {
                a.1.cmp(&b.1) // start (-h) before end (h) at same x
            }
        });

        let mut heap: BinaryHeap<i32> = BinaryHeap::new();
        heap.push(0);
        let mut to_remove: HashMap<i32, i32> = HashMap::new();
        let mut result: Vec<Vec<i32>> = Vec::new();

        for (x, h) in events {
            if h < 0 {
                heap.push(-h);
            } else {
                *to_remove.entry(h).or_insert(0) += 1;
            }

            // Clean up heights that should be removed
            while let Some(&top) = heap.peek() {
                if let Some(cnt) = to_remove.get_mut(&top) {
                    if *cnt > 0 {
                        *cnt -= 1;
                        heap.pop();
                        if *cnt == 0 {
                            to_remove.remove(&top);
                        }
                        continue;
                    }
                }
                break;
            }

            let current_max = *heap.peek().unwrap();
            if result.is_empty() || result.last().unwrap()[1] != current_max {
                result.push(vec![x, current_max]);
            }
        }

        result
    }
}
```

## Racket

```racket
#lang racket
(require racket/match)

(struct heap (data size) #:mutable)

(define (make-heap)
  (heap (make-vector 64) 0))

(define (heap-size hp) (heap-size hp))
(define (heap-data hp) (heap-data hp))

(define (heap-push! hp val)
  (let* ([size (heap-size hp)]
         [data (heap-data hp)])
    (when (= size (vector-length data))
      (define new (make-vector (* 2 (max 1 size))))
      (for ([i (in-range size)]) (vector-set! new i (vector-ref data i)))
      (set-heap-data! hp new))
    (vector-set! (heap-data hp) size val)
    (set-heap-size! hp (+ size 1))
    (let loop ([idx (- (heap-size hp) 1)])
      (when (> idx 0)
        (define parent (quotient (- idx 1) 2))
        (when (< (vector-ref (heap-data hp) parent)
                 (vector-ref (heap-data hp) idx))
          (define tmp (vector-ref (heap-data hp) parent))
          (vector-set! (heap-data hp) parent
                       (vector-ref (heap-data hp) idx))
          (vector-set! (heap-data hp) idx tmp)
          (loop parent))))))

(define (heap-pop! hp)
  (let* ([size (heap-size hp)]
         [data (heap-data hp)])
    (when (= size 0) (error "pop from empty heap"))
    (define top (vector-ref data 0))
    (set-heap-size! hp (- size 1))
    (when (> (heap-size hp) 0)
      (vector-set! data 0 (vector-ref data (heap-size hp)))
      (let loop ([idx 0])
        (define left (+ (* idx 2) 1))
        (define right (+ left 1))
        (define largest idx)
        (when (and (< left (heap-size hp))
                   (> (vector-ref data left) (vector-ref data largest)))
          (set! largest left))
        (when (and (< right (heap-size hp))
                   > (vector-ref data right) (vector-ref data largest))
          (set! largest right))
        (if (= largest idx)
            (void)
            (begin
              (define tmp (vector-ref data idx))
              (vector-set! data idx (vector-ref data largest))
              (vector-set! data largest tmp)
              (loop largest))))))
    top))

(define (heap-peek hp)
  (if (= (heap-size hp) 0) 0 (vector-ref (heap-data hp) 0)))

;; remove heights that are marked for deletion
(define (clean-top! hp removed)
  (let loop ()
    (when (> (heap-size hp) 0)
      (define cur (heap-peek hp))
      (define cnt (hash-ref removed cur #f))
      (if (and cnt (> cnt 0))
          (begin
            (hash-set! removed cur (- cnt 1))
            (when (= (hash-ref removed cur) 0)
              (hash-remove! removed cur))
            (heap-pop! hp)
            (loop))
          (void)))))

(define/contract (get-skyline buildings)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ([events
          (apply append
                 (map (lambda (b)
                        (match-define (list l r h) b)
                        (list (list l (- h)) (list r h)))
                      buildings))]
         [sorted-events
          (sort events
                (lambda (e1 e2)
                  (let ([x1 (first e1)] [h1 (second e1)]
                        [x2 (first e2)] [h2 (second e2)])
                    (if (= x1 x2)
                        (< h1 h2) ; smaller first
                        (< x1 x2)))) )]
         [hp (make-heap)]
         [removed (make-hash)])
    (heap-push! hp 0) ; sentinel ground height
    (let loop ([evs sorted-events] [prev 0] [result '()])
      (if (null? evs)
          (reverse result)
          (let* ([e (car evs)] [x (first e)] [h (second e)])
            (cond [(< h 0) ; start event
                   (heap-push! hp (- h))]
                  [else ; end event
                   (define cnt (hash-ref removed h 0))
                   (hash-set! removed h (+ cnt 1))])
            (clean-top! hp removed)
            (define cur (heap-peek hp))
            (if (= cur prev)
                (loop (cdr evs) prev result)
                (loop (cdr evs) cur (cons (list x cur) result)))))))))
```

## Erlang

```erlang
-module(solution).
-export([get_skyline/1]).

-spec get_skyline(Buildings :: [[integer()]]) -> [[integer()]].
get_skyline(Buildings) ->
    Events = build_events(Buildings, []),
    SortedEvents = lists:sort(Events),
    process(SortedEvents, gb_trees:empty(), 0, []).

build_events([], Acc) -> Acc;
build_events([[L,R,H]|Rest], Acc) ->
    build_events(Rest, [{L, -H}, {R, H} | Acc]).

process([], _Tree, _CurMax, Res) ->
    lists:reverse(Res);
process([{X,H}|Rest], Tree, CurMax, Res) when H < 0 ->
    Height = -H,
    NewTree = case gb_trees:is_defined(Height, Tree) of
        true -> Count = gb_trees:get(Height, Tree), gb_trees:update(Height, Count+1, Tree);
        false -> gb_trees:insert(Height, 1, Tree)
    end,
    NewMax = get_max(NewTree),
    if NewMax =/= CurMax ->
            process(Rest, NewTree, NewMax, [[X,NewMax]|Res]);
       true ->
            process(Rest, NewTree, CurMax, Res)
    end;
process([{X,H}|Rest], Tree, CurMax, Res) when H > 0 ->
    Height = H,
    Count = gb_trees:get(Height, Tree),
    NewCount = Count - 1,
    NewTree = if NewCount == 0 -> gb_trees:delete(Height, Tree); true -> gb_trees:update(Height, NewCount, Tree) end,
    NewMax = get_max(NewTree),
    if NewMax =/= CurMax ->
            process(Rest, NewTree, NewMax, [[X,NewMax]|Res]);
       true ->
            process(Rest, NewTree, CurMax, Res)
    end.

get_max(Tree) ->
    case gb_trees:is_empty(Tree) of
        true -> 0;
        false -> element(1, gb_trees:largest(Tree))
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_skyline(buildings :: [[integer]]) :: [[integer]]
  def get_skyline(buildings) do
    buildings
    |> skyline_rec()
    |> Enum.map(fn {x, y} -> [x, y] end)
  end

  # Recursive divide and conquer
  defp skyline_rec([]), do: []
  defp skyline_rec([b]), do: building_to_skyline(b)

  defp skyline_rec(buildings) do
    n = length(buildings)
    mid = div(n, 2)
    {left, right} = Enum.split(buildings, mid)
    left_sky = skyline_rec(left)
    right_sky = skyline_rec(right)
    merge_skylines(left_sky, right_sky)
  end

  defp building_to_skyline([l, r, h]), do: [{l, h}, {r, 0}]

  # Merge two skylines
  defp merge_skylines(s1, s2) do
    merge(s1, s2, 0, 0, [])
    |> Enum.reverse()
  end

  defp merge([], [], _h1, _h2, acc), do: acc

  # Both lists have elements
  defp merge([ {x1, y1} = p1 | t1 ] = l1,
             [ {x2, y2} = p2 | t2 ] = l2,
             h1, h2, acc) do
    cond do
      x1 < x2 ->
        new_h1 = y1
        max_h = max(new_h1, h2)
        {new_acc, _} = maybe_append({x1, max_h}, acc)
        merge(t1, l2, new_h1, h2, new_acc)

      x2 < x1 ->
        new_h2 = y2
        max_h = max(h1, new_h2)
        {new_acc, _} = maybe_append({x2, max_h}, acc)
        merge(l1, t2, h1, new_h2, new_acc)

      true -> # x1 == x2
        new_h1 = y1
        new_h2 = y2
        max_h = max(new_h1, new_h2)
        {new_acc, _} = maybe_append({x1, max_h}, acc)
        merge(t1, t2, new_h1, new_h2, new_acc)
    end
  end

  # Left list empty
  defp merge([], [{x, y} | t], h1, h2, acc) do
    max_h = max(h1, y)
    {new_acc, _} = maybe_append({x, max_h}, acc)
    merge([], t, h1, y, new_acc)
  end

  # Right list empty
  defp merge([{x, y} | t], [], h1, h2, acc) do
    max_h = max(y, h2)
    {new_acc, _} = maybe_append({x, max_h}, acc)
    merge(t, [], y, h2, new_acc)
  end

  # Append point if height changes
  defp maybe_append({_x, h}, []), do: {[{_x, h}], :added}
  defp maybe_append({x, h}, [{_, prev_h} | _] = acc) do
    if prev_h == h do
      {acc, :skip}
    else
      {[{x, h} | acc], :added}
    end
  end
end
```
