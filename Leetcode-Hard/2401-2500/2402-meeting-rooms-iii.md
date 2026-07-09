# 2402. Meeting Rooms III

## Cpp

```cpp
class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end(),
             [](const vector<int>& a, const vector<int>& b){ return a[0] < b[0]; });
        
        vector<int> cnt(n, 0);
        priority_queue<int, vector<int>, greater<int>> freeRooms;
        for (int i = 0; i < n; ++i) freeRooms.push(i);
        
        using P = pair<long long,int>;
        priority_queue<P, vector<P>, greater<P>> busy; // {endTime, room}
        
        for (const auto& m : meetings) {
            long long start = m[0];
            long long end   = m[1];
            
            while (!busy.empty() && busy.top().first <= start) {
                int room = busy.top().second;
                busy.pop();
                freeRooms.push(room);
            }
            
            if (!freeRooms.empty()) {
                int room = freeRooms.top(); freeRooms.pop();
                ++cnt[room];
                busy.emplace(end, room);
            } else {
                auto cur = busy.top(); busy.pop();
                long long curEnd = cur.first;
                int room = cur.second;
                long long duration = end - start;
                long long newEnd = curEnd + duration;
                ++cnt[room];
                busy.emplace(newEnd, room);
            }
        }
        
        int best = 0;
        for (int i = 1; i < n; ++i) {
            if (cnt[i] > cnt[best]) best = i;
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int mostBooked(int n, int[][] meetings) {
        // Sort meetings by start time
        java.util.Arrays.sort(meetings, (a, b) -> Integer.compare(a[0], b[0]));
        
        // Min-heap for free rooms (by room index)
        java.util.PriorityQueue<Integer> freeRooms = new java.util.PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            freeRooms.offer(i);
        }
        
        // Min-heap for occupied rooms: [availableTime, roomIndex]
        java.util.PriorityQueue<long[]> occupied = new java.util.PriorityQueue<>(
            (a, b) -> {
                if (a[0] != b[0]) return Long.compare(a[0], b[0]);
                return Long.compare(a[1], b[1]); // tie-break by room index
            }
        );
        
        int[] count = new int[n];
        
        for (int[] m : meetings) {
            long start = m[0];
            long end = m[1];
            
            // Release rooms that have become free by the meeting's start time
            while (!occupied.isEmpty() && occupied.peek()[0] <= start) {
                long[] roomInfo = occupied.poll();
                freeRooms.offer((int)roomInfo[1]);
            }
            
            if (!freeRooms.isEmpty()) {
                int room = freeRooms.poll();
                count[room]++;
                occupied.offer(new long[]{end, room});
            } else {
                // Delay the meeting: use the room that becomes free earliest
                long[] roomInfo = occupied.poll();
                long availableTime = roomInfo[0];
                int room = (int)roomInfo[1];
                
                long duration = end - start;
                long newEnd = availableTime + duration;
                
                count[room]++;
                occupied.offer(new long[]{newEnd, room});
            }
        }
        
        // Find the room with the maximum meetings (lowest index on tie)
        int bestRoom = 0;
        for (int i = 1; i < n; i++) {
            if (count[i] > count[bestRoom]) {
                bestRoom = i;
            }
        }
        return bestRoom;
    }
}
```

## Python

```python
class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        import heapq

        # sort meetings by start time
        meetings.sort(key=lambda x: x[0])

        free_rooms = list(range(n))
        heapq.heapify(free_rooms)          # (room_number)
        occupied = []                      # (end_time, room_number)

        counts = [0] * n

        for s, e in meetings:
            # release rooms that have become free by start time s
            while occupied and occupied[0][0] <= s:
                end_time, room = heapq.heappop(occupied)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                room = heapq.heappop(free_rooms)
                counts[room] += 1
                heapq.heappush(occupied, (e, room))
            else:
                # all rooms occupied, delay meeting to earliest finishing room
                end_time, room = heapq.heappop(occupied)
                duration = e - s
                new_end = end_time + duration
                counts[room] += 1
                heapq.heappush(occupied, (new_end, room))

        # find the room with maximum meetings, tie-breaking by smallest index
        max_meetings = max(counts)
        for i in range(n):
            if counts[i] == max_meetings:
                return i
```

## Python3

```python
from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        unused = list(range(n))
        heapq.heapify(unused)
        used = []  # (end_time, room_index)
        cnt = [0] * n

        for start, end in meetings:
            while used and used[0][0] <= start:
                finish, idx = heapq.heappop(used)
                heapq.heappush(unused, idx)

            if unused:
                idx = heapq.heappop(unused)
                heapq.heappush(used, (end, idx))
                cnt[idx] += 1
            else:
                finish, idx = heapq.heappop(used)
                duration = end - start
                new_finish = finish + duration
                heapq.heappush(used, (new_finish, idx))
                cnt[idx] += 1

        max_meetings = max(cnt)
        for i in range(n):
            if cnt[i] == max_meetings:
                return i
```

## C

```c
#include <stdlib.h>

typedef struct {
    int start;
    int end;
} Meeting;

typedef struct {
    long long end;
    int room;
} Occupied;

/* ---------- free rooms min-heap (by room index) ---------- */
static void pushFree(int *heap, int *size, int room) {
    int i = (*size)++;
    heap[i] = room;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p] <= heap[i]) break;
        int tmp = heap[p];
        heap[p] = heap[i];
        heap[i] = tmp;
        i = p;
    }
}
static int popFree(int *heap, int *size) {
    int top = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0;
    while (1) {
        int l = (i << 1) + 1, r = l + 1, smallest = i;
        if (l < *size && heap[l] < heap[smallest]) smallest = l;
        if (r < *size && heap[r] < heap[smallest]) smallest = r;
        if (smallest == i) break;
        int tmp = heap[i];
        heap[i] = heap[smallest];
        heap[smallest] = tmp;
        i = smallest;
    }
    return top;
}

/* ---------- occupied rooms min-heap (by end time, then room) ---------- */
static void pushOccupied(Occupied *heap, int *size, long long end, int room) {
    int i = (*size)++;
    heap[i].end = end;
    heap[i].room = room;
    while (i > 0) {
        int p = (i - 1) >> 1;
        if (heap[p].end < heap[i].end ||
            (heap[p].end == heap[i].end && heap[p].room <= heap[i].room))
            break;
        Occupied tmp = heap[p];
        heap[p] = heap[i];
        heap[i] = tmp;
        i = p;
    }
}
static Occupied popOccupied(Occupied *heap, int *size) {
    Occupied top = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0;
    while (1) {
        int l = (i << 1) + 1, r = l + 1, smallest = i;
        if (l < *size &&
            (heap[l].end < heap[smallest].end ||
             (heap[l].end == heap[smallest].end && heap[l].room < heap[smallest].room)))
            smallest = l;
        if (r < *size &&
            (heap[r].end < heap[smallest].end ||
             (heap[r].end == heap[smallest].end && heap[r].room < heap[smallest].room)))
            smallest = r;
        if (smallest == i) break;
        Occupied tmp = heap[i];
        heap[i] = heap[smallest];
        heap[smallest] = tmp;
        i = smallest;
    }
    return top;
}

/* ---------- comparator for qsort ---------- */
static int cmpMeeting(const void *a, const void *b) {
    const Meeting *m1 = (const Meeting *)a;
    const Meeting *m2 = (const Meeting *)b;
    return m1->start - m2->start;
}

int mostBooked(int n, int** meetings, int meetingsSize, int* meetingsColSize){
    if (meetingsSize == 0) return 0;

    Meeting *arr = (Meeting*)malloc(sizeof(Meeting) * meetingsSize);
    for (int i = 0; i < meetingsSize; ++i) {
        arr[i].start = meetings[i][0];
        arr[i].end   = meetings[i][1];
    }
    qsort(arr, meetingsSize, sizeof(Meeting), cmpMeeting);

    int *freeHeap = (int*)malloc(sizeof(int) * n);
    int freeSize = 0;
    for (int i = 0; i < n; ++i) pushFree(freeHeap, &freeSize, i);

    Occupied *occHeap = (Occupied*)malloc(sizeof(Occupied) * n);
    int occSize = 0;

    int *cnt = (int*)calloc(n, sizeof(int));

    for (int i = 0; i < meetingsSize; ++i) {
        int start = arr[i].start;
        int end   = arr[i].end;
        long long duration = (long long)end - start;

        /* release rooms that have become free */
        while (occSize > 0 && occHeap[0].end <= start) {
            Occupied rel = popOccupied(occHeap, &occSize);
            pushFree(freeHeap, &freeSize, rel.room);
        }

        int room;
        long long newEnd;

        if (freeSize > 0) {
            room = popFree(freeHeap, &freeSize);
            newEnd = end;   /* meeting runs as scheduled */
        } else {
            Occupied earliest = popOccupied(occHeap, &occSize);
            room = earliest.room;
            newEnd = earliest.end + duration;   /* delayed meeting */
        }

        cnt[room]++;

        pushOccupied(occHeap, &occSize, newEnd, room);
    }

    int bestRoom = 0;
    for (int i = 1; i < n; ++i) {
        if (cnt[i] > cnt[bestRoom]) bestRoom = i;
    }

    free(arr);
    free(freeHeap);
    free(occHeap);
    free(cnt);
    return bestRoom;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MostBooked(int n, int[][] meetings) {
        Array.Sort(meetings, (a, b) => a[0].CompareTo(b[0]));
        
        var freeRooms = new SortedSet<int>();
        for (int i = 0; i < n; i++) freeRooms.Add(i);
        
        var occupied = new SortedSet<(long end, int room)>(Comparer<(long, int)>.Create((x, y) => {
            int cmp = x.end.CompareTo(y.end);
            if (cmp != 0) return cmp;
            return x.room.CompareTo(y.room);
        }));
        
        int[] count = new int[n];
        
        foreach (var m in meetings) {
            int start = m[0];
            int end   = m[1];
            
            while (occupied.Count > 0 && occupied.Min.end <= start) {
                var node = occupied.Min;
                occupied.Remove(node);
                freeRooms.Add(node.room);
            }
            
            int roomIdx;
            long finishTime;
            
            if (freeRooms.Count > 0) {
                roomIdx = freeRooms.Min;
                freeRooms.Remove(roomIdx);
                finishTime = end;
            } else {
                var node = occupied.Min;
                occupied.Remove(node);
                roomIdx = node.room;
                long duration = (long)end - start;
                finishTime = node.end + duration;
            }
            
            count[roomIdx]++;
            occupied.Add((finishTime, roomIdx));
        }
        
        int bestRoom = 0;
        for (int i = 1; i < n; i++) {
            if (count[i] > count[bestRoom]) bestRoom = i;
        }
        return bestRoom;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} meetings
 * @return {number}
 */
var mostBooked = function(n, meetings) {
    // MinHeap implementation
    class MinHeap {
        constructor(compare) {
            this.data = [];
            this.compare = compare; // returns true if a should be before b
        }
        size() {
            return this.data.length;
        }
        peek() {
            return this.data[0];
        }
        push(item) {
            const arr = this.data;
            arr.push(item);
            let idx = arr.length - 1;
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.compare(arr[parent], arr[idx])) break;
                [arr[parent], arr[idx]] = [arr[idx], arr[parent]];
                idx = parent;
            }
        }
        pop() {
            const arr = this.data;
            if (arr.length === 0) return undefined;
            const top = arr[0];
            const last = arr.pop();
            if (arr.length > 0) {
                arr[0] = last;
                let idx = 0;
                const length = arr.length;
                while (true) {
                    let left = idx * 2 + 1;
                    let right = left + 1;
                    let smallest = idx;

                    if (left < length && !this.compare(arr[smallest], arr[left])) {
                        smallest = left;
                    }
                    if (right < length && !this.compare(arr[smallest], arr[right])) {
                        smallest = right;
                    }
                    if (smallest === idx) break;
                    [arr[idx], arr[smallest]] = [arr[smallest], arr[idx]];
                    idx = smallest;
                }
            }
            return top;
        }
    }

    // Initialize heaps
    const unused = new MinHeap((a, b) => a < b);
    for (let i = 0; i < n; ++i) unused.push(i);

    const used = new MinHeap((a, b) => {
        if (a[0] !== b[0]) return a[0] < b[0];
        return a[1] < b[1];
    });

    // Sort meetings by start time
    meetings.sort((a, b) => a[0] - b[0]);

    const cnt = new Array(n).fill(0);

    for (const [start, end] of meetings) {
        const duration = end - start;

        // Release rooms that have become free by the meeting's start time
        while (used.size() && used.peek()[0] <= start) {
            const [, room] = used.pop();
            unused.push(room);
        }

        if (unused.size()) {
            const room = unused.pop();
            cnt[room]++;
            used.push([end, room]);
        } else {
            // Delay the meeting
            const [availEnd, room] = used.pop();
            const newEnd = availEnd + duration;
            cnt[room]++;
            used.push([newEnd, room]);
        }
    }

    // Find room with max meetings (lowest index on tie)
    let bestRoom = 0;
    for (let i = 1; i < n; ++i) {
        if (cnt[i] > cnt[bestRoom]) bestRoom = i;
    }
    return bestRoom;
};
```

## Typescript

```typescript
function mostBooked(n: number, meetings: number[][]): number {
    // MinHeap implementation
    class MinHeap<T> {
        private heap: T[] = [];
        private compare: (a: T, b: T) => boolean;
        constructor(compare: (a: T, b: T) => boolean) {
            this.compare = compare;
        }
        size(): number {
            return this.heap.length;
        }
        peek(): T | undefined {
            return this.heap[0];
        }
        push(item: T): void {
            this.heap.push(item);
            this.bubbleUp(this.heap.length - 1);
        }
        pop(): T | undefined {
            if (this.heap.length === 0) return undefined;
            const top = this.heap[0];
            const end = this.heap.pop()!;
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this.bubbleDown(0);
            }
            return top;
        }
        private bubbleUp(index: number): void {
            while (index > 0) {
                const parent = (index - 1) >> 1;
                if (!this.compare(this.heap[index], this.heap[parent])) break;
                [this.heap[index], this.heap[parent]] = [this.heap[parent], this.heap[index]];
                index = parent;
            }
        }
        private bubbleDown(index: number): void {
            const length = this.heap.length;
            while (true) {
                let left = index * 2 + 1;
                let right = left + 1;
                let smallest = index;

                if (left < length && this.compare(this.heap[left], this.heap[smallest])) {
                    smallest = left;
                }
                if (right < length && this.compare(this.heap[right], this.heap[smallest])) {
                    smallest = right;
                }
                if (smallest === index) break;
                [this.heap[index], this.heap[smallest]] = [this.heap[smallest], this.heap[index]];
                index = smallest;
            }
        }
    }

    // Sort meetings by start time
    meetings.sort((a, b) => a[0] - b[0]);

    // Heap for free rooms (by room number)
    const freeRooms = new MinHeap<number>((a, b) => a < b);
    for (let i = 0; i < n; ++i) freeRooms.push(i);

    // Heap for occupied rooms: [endTime, roomNumber]
    const busyRooms = new MinHeap<[number, number]>((a, b) =>
        a[0] < b[0] || (a[0] === b[0] && a[1] < b[1])
    );

    const count = new Array<number>(n).fill(0);

    for (const [start, end] of meetings) {
        const duration = end - start;

        // Release rooms that have become free by current start time
        while (busyRooms.size() > 0 && (busyRooms.peek()![0] <= start)) {
            const [, room] = busyRooms.pop()!;
            freeRooms.push(room);
        }

        if (freeRooms.size() > 0) {
            // Assign to the smallest-numbered free room
            const room = freeRooms.pop()!;
            count[room]++;
            busyRooms.push([end, room]);
        } else {
            // All rooms are busy; delay meeting
            const [availTime, room] = busyRooms.pop()!;
            const newEnd = availTime + duration;
            count[room]++;
            busyRooms.push([newEnd, room]);
        }
    }

    // Find the room with maximum meetings (lowest index on tie)
    let bestRoom = 0;
    for (let i = 1; i < n; ++i) {
        if (count[i] > count[bestRoom]) bestRoom = i;
    }
    return bestRoom;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $meetings
     * @return Integer
     */
    function mostBooked($n, $meetings) {
        usort($meetings, fn($a, $b) => $a[0] <=> $b[0]);

        // Heap for free rooms (min by room number)
        $free = new class extends SplPriorityQueue {
            public function compare($p1, $p2) {
                return $p2 <=> $p1; // smaller room gets higher priority
            }
        };
        $free->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        for ($i = 0; $i < $n; ++$i) {
            $free->insert($i, $i);
        }

        // Heap for occupied rooms (min by end time, then room number)
        $occupied = new class extends SplPriorityQueue {
            public function compare($p1, $p2) {
                // $p: [endTime, room]
                if ($p1[0] === $p2[0]) {
                    return $p2[1] <=> $p1[1]; // smaller room higher priority
                }
                return $p2[0] <=> $p1[0];     // earlier end higher priority
            }
        };
        $occupied->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        $cnt = array_fill(0, $n, 0);

        foreach ($meetings as $m) {
            [$start, $end] = $m;

            // Release rooms that have become free by current start time
            while (!$occupied->isEmpty()) {
                $top = $occupied->top(); // [room, endTime]
                if ($top[1] <= $start) {
                    $released = $occupied->extract();
                    $free->insert($released[0], $released[0]);
                } else {
                    break;
                }
            }

            if (!$free->isEmpty()) {
                // Assign to the smallest free room
                $room = $free->extract();
                ++$cnt[$room];
                $occupied->insert([$room, $end], [$end, $room]);
            } else {
                // Delay meeting: use the room that frees earliest
                $top = $occupied->extract(); // [room, endTime]
                $room = $top[0];
                $prevEnd = $top[1];
                $duration = $end - $start;
                $newEnd = $prevEnd + $duration;
                ++$cnt[$room];
                $occupied->insert([$room, $newEnd], [$newEnd, $room]);
            }
        }

        // Find room with maximum meetings (lowest index on tie)
        $maxCnt = -1;
        $ans = 0;
        for ($i = 0; $i < $n; ++$i) {
            if ($cnt[$i] > $maxCnt) {
                $maxCnt = $cnt[$i];
                $ans = $i;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
import Foundation

struct Heap<T> {
    private var elements: [T] = []
    private let priority: (T, T) -> Bool
    
    init(priority: @escaping (T, T) -> Bool) {
        self.priority = priority
    }
    
    var isEmpty: Bool { elements.isEmpty }
    
    func peek() -> T? {
        return elements.first
    }
    
    mutating func push(_ value: T) {
        elements.append(value)
        siftUp(from: elements.count - 1)
    }
    
    mutating func pop() -> T? {
        guard !elements.isEmpty else { return nil }
        if elements.count == 1 {
            return elements.removeLast()
        }
        let top = elements[0]
        elements[0] = elements.removeLast()
        siftDown(from: 0)
        return top
    }
    
    private mutating func siftUp(from index: Int) {
        var child = index
        var parent = (child - 1) / 2
        while child > 0 && priority(elements[child], elements[parent]) {
            elements.swapAt(child, parent)
            child = parent
            parent = (child - 1) / 2
        }
    }
    
    private mutating func siftDown(from index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var candidate = parent
            
            if left < elements.count && priority(elements[left], elements[candidate]) {
                candidate = left
            }
            if right < elements.count && priority(elements[right], elements[candidate]) {
                candidate = right
            }
            if candidate == parent { return }
            elements.swapAt(parent, candidate)
            parent = candidate
        }
    }
}

class Solution {
    func mostBooked(_ n: Int, _ meetings: [[Int]]) -> Int {
        var freeRooms = Heap<Int>(priority: <) // smallest room number first
        for i in 0..<n { freeRooms.push(i) }
        
        var occupied = Heap<(end: Int, room: Int)>(priority: {
            if $0.end == $1.end { return $0.room < $1.room }
            return $0.end < $1.end
        })
        
        var count = Array(repeating: 0, count: n)
        let sortedMeetings = meetings.sorted { $0[0] < $1[0] }
        
        for meeting in sortedMeetings {
            let start = meeting[0]
            let end = meeting[1]
            // release rooms that have become free
            while let top = occupied.peek(), top.end <= start {
                _ = occupied.pop()
                freeRooms.push(top.room)
            }
            
            if !freeRooms.isEmpty {
                let room = freeRooms.pop()!
                count[room] += 1
                occupied.push((end: end, room: room))
            } else {
                // delay the meeting
                var top = occupied.pop()!
                let duration = end - start
                let newEnd = top.end + duration
                count[top.room] += 1
                occupied.push((end: newEnd, room: top.room))
            }
        }
        
        var bestRoom = 0
        for i in 1..<n {
            if count[i] > count[bestRoom] {
                bestRoom = i
            }
        }
        return bestRoom
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mostBooked(n: Int, meetings: Array<IntArray>): Int {
        val sorted = meetings.sortedBy { it[0] }
        val freeRooms = java.util.PriorityQueue<Int>()
        for (i in 0 until n) freeRooms.offer(i)

        data class Room(val end: Long, val id: Int)
        val occupied = java.util.PriorityQueue<Room>(compareBy<Room> { it.end }.thenBy { it.id })
        val count = IntArray(n)

        for (m in sorted) {
            val start = m[0].toLong()
            val end = m[1].toLong()

            while (!occupied.isEmpty() && occupied.peek().end <= start) {
                val room = occupied.poll()
                freeRooms.offer(room.id)
            }

            if (freeRooms.isNotEmpty()) {
                val id = freeRooms.poll()
                count[id]++
                occupied.offer(Room(end, id))
            } else {
                val room = occupied.poll()
                val duration = end - start
                val newEnd = room.end + duration
                count[room.id]++
                occupied.offer(Room(newEnd, room.id))
            }
        }

        var best = 0
        for (i in 1 until n) {
            if (count[i] > count[best]) best = i
        }
        return best
    }
}
```

## Dart

```dart
import 'dart:math';

class _Heap<T> {
  final List<T> _data = [];
  final int Function(T a, T b) _cmp;
  _Heap(this._cmp);

  bool get isEmpty => _data.isEmpty;

  void add(T value) {
    _data.add(value);
    _siftUp(_data.length - 1);
  }

  T peek() => _data[0];

  T pop() {
    final result = _data[0];
    final last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      _siftDown(0);
    }
    return result;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      final parent = (idx - 1) >> 1;
      if (_cmp(_data[idx], _data[parent]) < 0) {
        _swap(idx, parent);
        idx = parent;
      } else {
        break;
      }
    }
  }

  void _siftDown(int idx) {
    final n = _data.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int smallest = idx;

      if (left < n && _cmp(_data[left], _data[smallest]) < 0) {
        smallest = left;
      }
      if (right < n && _cmp(_data[right], _data[smallest]) < 0) {
        smallest = right;
      }
      if (smallest == idx) break;
      _swap(idx, smallest);
      idx = smallest;
    }
  }

  void _swap(int i, int j) {
    final tmp = _data[i];
    _data[i] = _data[j];
    _data[j] = tmp;
  }
}

class _RoomInfo {
  int endTime;
  int roomIdx;
  _RoomInfo(this.endTime, this.roomIdx);
}

class Solution {
  int mostBooked(int n, List<List<int>> meetings) {
    // Sort meetings by start time
    meetings.sort((a, b) => a[0] - b[0]);

    // Free rooms heap (by room index)
    final freeRooms = _Heap<int>((a, b) => a.compareTo(b));
    for (int i = 0; i < n; ++i) {
      freeRooms.add(i);
    }

    // Occupied rooms heap (by end time then room index)
    final occupied = _Heap<_RoomInfo>((a, b) {
      if (a.endTime != b.endTime) return a.endTime - b.endTime;
      return a.roomIdx - b.roomIdx;
    });

    final counts = List<int>.filled(n, 0);

    for (var meeting in meetings) {
      int start = meeting[0];
      int end = meeting[1];
      // Release rooms that have become free by current start time
      while (!occupied.isEmpty && occupied.peek().endTime <= start) {
        final freed = occupied.pop();
        freeRooms.add(freed.roomIdx);
      }

      if (!freeRooms.isEmpty) {
        // Assign to the smallest-index free room
        int room = freeRooms.pop();
        counts[room]++;
        occupied.add(_RoomInfo(end, room));
      } else {
        // Delay meeting: take earliest finishing room
        final earliest = occupied.pop();
        int room = earliest.roomIdx;
        int duration = end - start;
        int newEnd = earliest.endTime + duration;
        counts[room]++;
        occupied.add(_RoomInfo(newEnd, room));
      }
    }

    int bestRoom = 0;
    for (int i = 1; i < n; ++i) {
      if (counts[i] > counts[bestRoom]) {
        bestRoom = i;
      }
    }
    return bestRoom;
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

type IntHeap []int

func (h IntHeap) Len() int            { return len(h) }
func (h IntHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type Node struct {
	end int
	idx int
}

type NodeHeap []Node

func (h NodeHeap) Len() int { return len(h) }
func (h NodeHeap) Less(i, j int) bool {
	if h[i].end == h[j].end {
		return h[i].idx < h[j].idx
	}
	return h[i].end < h[j].end
}
func (h NodeHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *NodeHeap) Push(x interface{}) { *h = append(*h, x.(Node)) }
func (h *NodeHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func mostBooked(n int, meetings [][]int) int {
	sort.Slice(meetings, func(i, j int) bool { return meetings[i][0] < meetings[j][0] })

	free := &IntHeap{}
	for i := 0; i < n; i++ {
		*free = append(*free, i)
	}
	heap.Init(free)

	busy := &NodeHeap{}
	heap.Init(busy)

	count := make([]int, n)

	for _, m := range meetings {
		start, end := m[0], m[1]

		// release rooms that have become free
		for busy.Len() > 0 && (*busy)[0].end <= start {
			node := heap.Pop(busy).(Node)
			heap.Push(free, node.idx)
		}

		if free.Len() > 0 {
			idx := heap.Pop(free).(int)
			count[idx]++
			heap.Push(busy, Node{end: end, idx: idx})
		} else {
			node := heap.Pop(busy).(Node)
			duration := end - start
			newEnd := node.end + duration
			count[node.idx]++
			heap.Push(busy, Node{end: newEnd, idx: node.idx})
		}
	}

	maxCnt, ans := -1, 0
	for i, c := range count {
		if c > maxCnt {
			maxCnt = c
			ans = i
		}
	}
	return ans
}
```

## Ruby

```ruby
class MinHeap
  def initialize(&comp)
    @comp = comp || ->(a, b) { a < b }
    @data = []
  end

  def empty?
    @data.empty?
  end

  def peek
    @data[0]
  end

  def push(val)
    @data << val
    idx = @data.size - 1
    while idx > 0
      parent = (idx - 1) / 2
      break unless @comp.call(@data[idx], @data[parent])
      @data[idx], @data[parent] = @data[parent], @data[idx]
      idx = parent
    end
  end

  def pop
    return nil if @data.empty?
    min = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      size = @data.size
      idx = 0
      loop do
        left = idx * 2 + 1
        right = left + 1
        smallest = idx
        if left < size && @comp.call(@data[left], @data[smallest])
          smallest = left
        end
        if right < size && @comp.call(@data[right], @data[smallest])
          smallest = right
        end
        break if smallest == idx
        @data[idx], @data[smallest] = @data[smallest], @data[idx]
        idx = smallest
      end
    end
    min
  end
end

# @param {Integer} n
# @param {Integer[][]} meetings
# @return {Integer}
def most_booked(n, meetings)
  meetings.sort_by! { |s, _e| s }

  unused = MinHeap.new { |a, b| a < b }
  (0...n).each { |i| unused.push(i) }

  used = MinHeap.new do |a, b|
    if a[0] == b[0]
      a[1] < b[1]
    else
      a[0] < b[0]
    end
  end

  counts = Array.new(n, 0)

  meetings.each do |start_time, end_time|
    while !used.empty? && used.peek[0] <= start_time
      room = used.pop[1]
      unused.push(room)
    end

    if !unused.empty?
      room = unused.pop
      counts[room] += 1
      used.push([end_time, room])
    else
      earliest_end, room = used.pop
      duration = end_time - start_time
      new_end = earliest_end + duration
      counts[room] += 1
      used.push([new_end, room])
    end
  end

  max_meetings = counts.max
  counts.each_with_index.find { |c, _i| c == max_meetings }[1]
end
```

## Scala

```scala
import java.util.{Arrays, Comparator, PriorityQueue}

object Solution {
  def mostBooked(n: Int, meetings: Array[Array[Int]]): Int = {
    // Sort meetings by start time
    Arrays.sort(meetings, new Comparator[Array[Int]] {
      override def compare(a: Array[Int], b: Array[Int]): Int = Integer.compare(a(0), b(0))
    })

    // Free rooms ordered by smallest index
    val free = new PriorityQueue[Int](new Comparator[Int] {
      override def compare(a: Int, b: Int): Int = a - b
    })
    var i = 0
    while (i < n) {
      free.add(i)
      i += 1
    }

    // Occupied rooms ordered by earliest end time, then smallest index
    val occupied = new PriorityQueue[Array[Int]](new Comparator[Array[Int]] {
      override def compare(a: Array[Int], b: Array[Int]): Int = {
        if (a(0) != b(0)) Integer.compare(a(0), b(0))
        else Integer.compare(a(1), b(1))
      }
    })

    val count = new Array[Int](n)

    var idx = 0
    while (idx < meetings.length) {
      val start = meetings(idx)(0)
      val end   = meetings(idx)(1)

      // Release rooms that have become free by the meeting's start time
      while (!occupied.isEmpty && occupied.peek()(0) <= start) {
        val roomInfo = occupied.poll()
        free.add(roomInfo(1))
      }

      if (!free.isEmpty) {
        // Assign to the smallest-index free room
        val room = free.poll()
        occupied.add(Array(end, room))
        count(room) += 1
      } else {
        // All rooms busy: delay meeting in the earliest finishing room
        val roomInfo = occupied.poll()
        val curEnd   = roomInfo(0)
        val room     = roomInfo(1)
        val newEnd   = curEnd + (end - start)
        occupied.add(Array(newEnd, room))
        count(room) += 1
      }

      idx += 1
    }

    // Find the room with maximum meetings (lowest index on tie)
    var bestRoom = 0
    var r = 1
    while (r < n) {
      if (count(r) > count(bestRoom)) bestRoom = r
      r += 1
    }
    bestRoom
  }
}
```

## Rust

```rust
impl Solution {
    pub fn most_booked(n: i32, meetings: Vec<Vec<i32>>) -> i32 {
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        let n_usize = n as usize;
        let mut meetings = meetings;
        meetings.sort_by_key(|m| m[0]);

        // free rooms min-heap by room index
        let mut free: BinaryHeap<Reverse<usize>> = (0..n_usize).map(Reverse).collect();
        // occupied rooms min-heap by (end_time, room_index)
        let mut occupied: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();

        let mut counts = vec![0i32; n_usize];

        for meeting in meetings {
            let start = meeting[0];
            let end = meeting[1];

            // release rooms that have become free by the current start time
            while let Some(&Reverse((avail_end, _))) = occupied.peek() {
                if avail_end <= start {
                    let Reverse((_e, room)) = occupied.pop().unwrap();
                    free.push(Reverse(room));
                } else {
                    break;
                }
            }

            if let Some(Reverse(room)) = free.pop() {
                // assign to a free room
                counts[room] += 1;
                occupied.push(Reverse((end, room)));
            } else {
                // delay the meeting; use the earliest finishing room
                let Reverse((avail_end, room)) = occupied.pop().unwrap();
                let duration = end - start;
                let new_end = avail_end + duration;
                counts[room] += 1;
                occupied.push(Reverse((new_end, room)));
            }
        }

        // find the room with maximum meetings (lowest index on tie)
        let mut best_room = 0usize;
        let mut best_cnt = counts[0];
        for i in 1..n_usize {
            if counts[i] > best_cnt || (counts[i] == best_cnt && i < best_room) {
                best_cnt = counts[i];
                best_room = i;
            }
        }

        best_room as i32
    }
}
```

## Racket

```racket
(define/contract (most-booked n meetings)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ((sorted
          (sort (map (lambda (m) (list (first m) (second m))) meetings)
                (lambda (a b) (< (first a) (first b)))))
         (end-times (make-vector n 0))
         (counts   (make-vector n 0)))
    (for ([meeting sorted])
      (define s (first meeting))
      (define e (second meeting))
      ;; try to find a free room (smallest index)
      (define free-room -1)
      (for ([i (in-range n)])
        (when (and (= free-room -1) (<= (vector-ref end-times i) s))
          (set! free-room i)))
      (if (>= free-room 0)
          ;; assign to free room
          (begin
            (vector-set! end-times free-room e)
            (vector-set! counts   free-room (+ 1 (vector-ref counts free-room))))
          ;; all rooms busy: pick the one that becomes free earliest
          (let* ((min-room 0)
                 (min-end  (vector-ref end-times 0)))
            (for ([i (in-range 1 n)])
              (define cur (vector-ref end-times i))
              (when (or (< cur min-end) (and (= cur min-end) (< i min-room)))
                (set! min-end cur)
                (set! min-room i)))
            (define duration (- e s))
            (vector-set! end-times min-room (+ min-end duration))
            (vector-set! counts   min-room (+ 1 (vector-ref counts min-room))))))
    ;; find room with maximum meetings, tie-breaking by smallest index
    (let ((max-count -1)
          (ans 0))
      (for ([i (in-range n)])
        (define cnt (vector-ref counts i))
        (when (or (> cnt max-count) (and (= cnt max-count) (< i ans)))
          (set! max-count cnt)
          (set! ans i)))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([most_booked/2]).

most_booked(N, Meetings) ->
    Sorted = lists:sort(fun([S1,_],[S2,_]) -> S1 < S2 end, Meetings),
    Counts0 = array:new(N, {default,0}),
    Free0 = lists:seq(0, N-1),
    Busy0 = [],
    FinalCounts = process(Sorted, Free0, Busy0, Counts0),
    max_room(N, FinalCounts).

process([], _Free, _Busy, Counts) ->
    Counts;
process([[S,E]|Rest], Free, Busy, Counts) ->
    {Released, StillBusy} = lists:partition(fun({End,_}) -> End =< S end, Busy),
    ReleasedRooms = [Room || {_End, Room} <- Released],
    NewFreeList = lists:sort(ReleasedRooms ++ Free),
    case NewFreeList of
        [] ->
            SortedBusy = lists:keysort(1, StillBusy),
            [{EarliestEnd, Room}|RestBusy] = SortedBusy,
            Duration = E - S,
            NewEnd = EarliestEnd + Duration,
            UpdatedBusy = [{NewEnd, Room} | RestBusy],
            Counts1 = inc_count(Room, Counts),
            process(Rest, [], UpdatedBusy, Counts1);
        [Room|FreeTail] ->
            UpdatedBusy = [{E, Room} | StillBusy],
            Counts1 = inc_count(Room, Counts),
            process(Rest, FreeTail, UpdatedBusy, Counts1)
    end.

inc_count(R, Counts) ->
    Old = array:get(R, Counts),
    array:set(R, Old + 1, Counts).

max_room(N, Counts) ->
    {BestIdx,_} = lists:foldl(
        fun(I,{CurIdx,CurMax}) ->
            Val = array:get(I, Counts),
            if
                Val > CurMax -> {I,Val};
                Val == CurMax, I < CurIdx -> {I,Val};
                true -> {CurIdx,CurMax}
            end
        end,
        {0, array:get(0, Counts)},
        lists:seq(1, N-1)
    ),
    BestIdx.
```

## Elixir

```elixir
defmodule Solution do
  @spec most_booked(n :: integer, meetings :: [[integer]]) :: integer
  def most_booked(n, meetings) do
    sorted = Enum.sort_by(meetings, fn [s, _] -> s end)

    init_avail = List.duplicate(0, n)
    init_cnt = List.duplicate(0, n)

    {_final_avail, final_cnt} =
      Enum.reduce(sorted, {init_avail, init_cnt}, fn [s, e], {avail, cnt} ->
        case Enum.find_index(avail, fn t -> t <= s end) do
          nil ->
            {min_time, idx} =
              avail
              |> Enum.with_index()
              |> Enum.min_by(fn {t, _i} -> t end)

            duration = e - s
            new_end = min_time + duration

            new_avail = List.replace_at(avail, idx, new_end)
            new_cnt = List.update_at(cnt, idx, &(&1 + 1))
            {new_avail, new_cnt}

          idx ->
            new_avail = List.replace_at(avail, idx, e)
            new_cnt = List.update_at(cnt, idx, &(&1 + 1))
            {new_avail, new_cnt}
        end
      end)

    {_max_cnt, best_idx} =
      final_cnt
      |> Enum.with_index()
      |> Enum.reduce({-1, 0}, fn {c, i}, {best_c, best_i} ->
        cond do
          c > best_c -> {c, i}
          c == best_c and i < best_i -> {c, i}
          true -> {best_c, best_i}
        end
      end)

    best_idx
  end
end
```
