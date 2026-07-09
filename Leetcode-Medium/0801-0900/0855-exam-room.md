# 0855. Exam Room

## Cpp

```cpp
class ExamRoom {
    int N;
    std::set<int> occ;
public:
    ExamRoom(int n) : N(n) {}
    
    int seat() {
        if (occ.empty()) {
            occ.insert(0);
            return 0;
        }
        int bestSeat = 0;
        long long maxDist = -1;
        
        // distance from start
        int first = *occ.begin();
        if (first != 0) {
            maxDist = first;
            bestSeat = 0;
        }
        
        // between occupied seats
        auto prevIt = occ.begin();
        for (auto it = std::next(occ.begin()); it != occ.end(); ++it) {
            int a = *prevIt;
            int b = *it;
            long long dist = (b - a) / 2;
            int candSeat = a + dist;
            if (dist > maxDist || (dist == maxDist && candSeat < bestSeat)) {
                maxDist = dist;
                bestSeat = candSeat;
            }
            prevIt = it;
        }
        
        // distance to end
        int last = *occ.rbegin();
        long long distEnd = N - 1 - last;
        if (distEnd > maxDist || (distEnd == maxDist && N - 1 < bestSeat)) {
            bestSeat = N - 1;
        }
        
        occ.insert(bestSeat);
        return bestSeat;
    }
    
    void leave(int p) {
        occ.erase(p);
    }
};

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom* obj = new ExamRoom(n);
 * int param_1 = obj->seat();
 * obj->leave(p);
 */
```

## Java

```java
import java.util.*;

class ExamRoom {
    private final int N;
    private final TreeSet<Integer> occupied = new TreeSet<>();
    private final PriorityQueue<Interval> pq;

    public ExamRoom(int n) {
        this.N = n;
        this.pq = new PriorityQueue<>((a, b) -> {
            long d1 = a.getDist();
            long d2 = b.getDist();
            if (d1 != d2) return Long.compare(d2, d1); // larger distance first
            int s1 = a.getSeat();
            int s2 = b.getSeat();
            return Integer.compare(s1, s2); // smaller seat number first
        });
        addInterval(-1, N);
    }

    public int seat() {
        while (!pq.isEmpty()) {
            Interval cur = pq.peek();
            if (isValid(cur)) break;
            pq.poll(); // discard invalid interval
        }
        Interval best = pq.poll();
        int seat = best.getSeat();
        occupied.add(seat);

        // left interval
        addInterval(best.l, seat);
        // right interval
        addInterval(seat, best.r);

        return seat;
    }

    public void leave(int p) {
        if (!occupied.remove(p)) return;
        Integer left = occupied.lower(p);
        Integer right = occupied.higher(p);
        int l = (left == null) ? -1 : left;
        int r = (right == null) ? N : right;
        addInterval(l, r);
    }

    private void addInterval(int l, int r) {
        // No free seat in this interval
        if (l == -1 && r == 0) return;
        if (r == N && l == N - 1) return;
        if (l != -1 && r != N && r - l <= 1) return;

        Interval iv = new Interval(l, r);
        pq.offer(iv);
    }

    private boolean isValid(Interval iv) {
        Integer afterLeft;
        if (iv.l == -1) {
            afterLeft = occupied.isEmpty() ? null : occupied.first();
        } else {
            afterLeft = occupied.higher(iv.l);
        }
        return Objects.equals(afterLeft, iv.r);
    }

    private class Interval {
        int l; // left occupied seat index, -1 means virtual left wall
        int r; // right occupied seat index, N means virtual right wall

        Interval(int l, int r) {
            this.l = l;
            this.r = r;
        }

        int getSeat() {
            if (l == -1) return 0;
            if (r == N) return N - 1;
            return l + (r - l) / 2;
        }

        long getDist() {
            if (l == -1) return r; // distance from seat 0 to first occupied
            if (r == N) return N - 1 - l;
            return (r - l) / 2;
        }
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(n);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */
```

## Python

```python
import heapq, bisect

class ExamRoom(object):
    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.heap = []               # elements are (-dist, start, end)
        self.intervals = set()       # active intervals (start, end)
        self.seats = []              # sorted occupied seats
        self._add_interval(-1, n)

    def _distance(self, start, end):
        if start == -1:
            return end
        if end == self.n:
            return self.n - 1 - start
        return (end - start) // 2

    def _add_interval(self, start, end):
        if start == end:
            return
        dist = self._distance(start, end)
        heapq.heappush(self.heap, (-dist, start, end))
        self.intervals.add((start, end))

    def _remove_interval(self, start, end):
        self.intervals.discard((start, end))

    def seat(self):
        """
        :rtype: int
        """
        while True:
            _, start, end = heapq.heappop(self.heap)
            if (start, end) in self.intervals:
                break
        self._remove_interval(start, end)

        if start == -1:
            pos = 0
        elif end == self.n:
            pos = self.n - 1
        else:
            pos = (start + end) // 2

        bisect.insort(self.seats, pos)
        self._add_interval(start, pos)
        self._add_interval(pos, end)
        return pos

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        idx = bisect.bisect_left(self.seats, p)
        self.seats.pop(idx)

        left = self.seats[idx - 1] if idx - 1 >= 0 else -1
        right = self.seats[idx] if idx < len(self.seats) else self.n

        self._remove_interval(left, p)
        self._remove_interval(p, right)
        self._add_interval(left, right)
```

## Python3

```python
class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.occupied = []  # sorted list of occupied seats
        import heapq
        self.heap = []
        self.valid = set()  # set of (start, end) intervals currently valid

        # initial interval covering whole room with virtual boundaries -1 and n
        start, end = -1, n
        dist = self._distance(start, end)
        heapq.heappush(self.heap, (-dist, start, end))
        self.valid.add((start, end))

    def _distance(self, s: int, e: int) -> int:
        if s == -1:
            return e  # distance from seat 0 to first occupied at e
        if e == self.n:
            return self.n - 1 - s  # distance from last occupied s to seat n-1
        return (e - s) // 2

    def _seat_position(self, s: int, e: int) -> int:
        if s == -1:
            return 0
        if e == self.n:
            return self.n - 1
        return (s + e) // 2

    def seat(self) -> int:
        import heapq, bisect
        # get the best valid interval
        while True:
            neg_dist, s, e = self.heap[0]
            if (s, e) in self.valid:
                break
            heapq.heappop(self.heap)  # discard invalid entry

        heapq.heappop(self.heap)
        self.valid.remove((s, e))

        p = self._seat_position(s, e)

        # insert seat into occupied list
        bisect.insort(self.occupied, p)

        # create new intervals [s, p] and [p, e]
        for ns, ne in ((s, p), (p, e)):
            if ns < ne:
                dist = self._distance(ns, ne)
                heapq.heappush(self.heap, (-dist, ns, ne))
                self.valid.add((ns, ne))

        return p

    def leave(self, p: int) -> None:
        import bisect, heapq
        idx = bisect.bisect_left(self.occupied, p)
        # find neighbors
        left = self.occupied[idx - 1] if idx > 0 else -1
        right = self.occupied[idx + 1] if idx + 1 < len(self.occupied) else self.n

        # remove p from occupied list
        self.occupied.pop(idx)

        # invalidate intervals (left, p) and (p, right)
        for interval in ((left, p), (p, right)):
            if interval in self.valid:
                self.valid.remove(interval)

        # add merged interval (left, right)
        if left < right:
            dist = self._distance(left, right)
            heapq.heappush(self.heap, (-dist, left, right))
            self.valid.add((left, right))
```

## C

```c
#include <stdlib.h>

typedef struct {
    int n;          // total seats
    int *seats;     // sorted occupied seats
    int size;       // current number of occupied seats
    int capacity;   // allocated capacity for seats array
} ExamRoom;

static void ensure_capacity(ExamRoom *obj) {
    if (obj->size >= obj->capacity) {
        int newCap = obj->capacity ? obj->capacity * 2 : 4;
        int *newArr = (int *)realloc(obj->seats, newCap * sizeof(int));
        if (!newArr) exit(1); // allocation failure
        obj->seats = newArr;
        obj->capacity = newCap;
    }
}

/* binary search: returns index of target if found,
   otherwise returns -insertion_point-1 (like Java's Arrays.binarySearch) */
static int find_index(ExamRoom *obj, int p) {
    int lo = 0, hi = obj->size - 1;
    while (lo <= hi) {
        int mid = lo + ((hi - lo) >> 1);
        if (obj->seats[mid] == p) return mid;
        else if (obj->seats[mid] < p) lo = mid + 1;
        else hi = mid - 1;
    }
    return -(lo + 1);
}

ExamRoom* examRoomCreate(int n) {
    ExamRoom *obj = (ExamRoom *)malloc(sizeof(ExamRoom));
    obj->n = n;
    obj->seats = NULL;
    obj->size = 0;
    obj->capacity = 0;
    return obj;
}

int examRoomSeat(ExamRoom* obj) {
    int seatPos;
    if (obj->size == 0) {
        seatPos = 0;
    } else {
        int bestDist = -1;
        int bestSeat = 0;

        // first gap
        int dist = obj->seats[0];
        if (dist > bestDist) {
            bestDist = dist;
            bestSeat = 0;
        }

        // middle gaps
        for (int i = 0; i < obj->size - 1; ++i) {
            int a = obj->seats[i];
            int b = obj->seats[i + 1];
            int d = (b - a) / 2;
            int cand = a + d;
            if (d > bestDist || (d == bestDist && cand < bestSeat)) {
                bestDist = d;
                bestSeat = cand;
            }
        }

        // last gap
        dist = obj->n - 1 - obj->seats[obj->size - 1];
        if (dist > bestDist) {
            bestDist = dist;
            bestSeat = obj->n - 1;
        } else if (dist == bestDist && (obj->n - 1) < bestSeat) {
            bestSeat = obj->n - 1;
        }

        seatPos = bestSeat;
    }

    // insert seatPos into sorted array
    ensure_capacity(obj);
    int idx = find_index(obj, seatPos);
    if (idx >= 0) {
        // should not happen as seatPos is free
    } else {
        idx = -idx - 1; // insertion point
    }
    for (int i = obj->size; i > idx; --i) {
        obj->seats[i] = obj->seats[i - 1];
    }
    obj->seats[idx] = seatPos;
    obj->size++;
    return seatPos;
}

void examRoomLeave(ExamRoom* obj, int p) {
    int idx = find_index(obj, p);
    if (idx < 0) return; // not found, should not happen
    for (int i = idx; i < obj->size - 1; ++i) {
        obj->seats[i] = obj->seats[i + 1];
    }
    obj->size--;
}

void examRoomFree(ExamRoom* obj) {
    if (!obj) return;
    free(obj->seats);
    free(obj);
}

/**
 * Your ExamRoom struct will be instantiated and called as such:
 * ExamRoom* obj = examRoomCreate(n);
 * int param_1 = examRoomSeat(obj);
 * 
 * examRoomLeave(obj, p);
 * 
 * examRoomFree(obj);
 */
```

## Csharp

```csharp
public class ExamRoom
{
    private readonly int _n;
    private readonly SortedSet<int> _occupied;

    public ExamRoom(int n)
    {
        _n = n;
        _occupied = new SortedSet<int>();
    }

    public int Seat()
    {
        if (_occupied.Count == 0)
        {
            _occupied.Add(0);
            return 0;
        }

        int bestSeat = 0;
        int maxDist = -1;

        // Check distance from start (seat 0) to first occupied seat
        int firstOcc = _occupied.Min;
        int distStart = firstOcc; // distance if sit at 0
        if (distStart > maxDist)
        {
            maxDist = distStart;
            bestSeat = 0;
        }

        // Check intervals between occupied seats
        int prev = -1;
        foreach (int seat in _occupied)
        {
            if (prev == -1)
            {
                prev = seat;
                continue;
            }
            int gap = seat - prev;
            int candDist = gap / 2;
            int candSeat = prev + candDist;
            if (candDist > maxDist || (candDist == maxDist && candSeat < bestSeat))
            {
                maxDist = candDist;
                bestSeat = candSeat;
            }
            prev = seat;
        }

        // Check distance from last occupied seat to end (seat n-1)
        int lastOcc = _occupied.Max;
        int distEnd = (_n - 1) - lastOcc;
        if (distEnd > maxDist || (distEnd == maxDist && (_n - 1) < bestSeat))
        {
            maxDist = distEnd;
            bestSeat = _n - 1;
        }

        _occupied.Add(bestSeat);
        return bestSeat;
    }

    public void Leave(int p)
    {
        _occupied.Remove(p);
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(n);
 * int param_1 = obj.Seat();
 * obj.Leave(p);
 */
```

## Javascript

```javascript
var ExamRoom = function(n) {
    this.n = n;
    this.seats = []; // sorted occupied seats
};

ExamRoom.prototype.seat = function() {
    if (this.seats.length === 0) {
        this.seats.push(0);
        return 0;
    }
    let maxDist = -1;
    let seatPos = 0;

    const first = this.seats[0];
    if (first !== 0) {
        maxDist = first; // distance from seat 0 to first occupied
        seatPos = 0;
    }

    for (let i = 0; i < this.seats.length - 1; i++) {
        const a = this.seats[i];
        const b = this.seats[i + 1];
        const dist = Math.floor((b - a) / 2);
        const cand = a + dist;
        if (dist > maxDist || (dist === maxDist && cand < seatPos)) {
            maxDist = dist;
            seatPos = cand;
        }
    }

    const last = this.seats[this.seats.length - 1];
    const endDist = this.n - 1 - last;
    if (endDist > maxDist) {
        seatPos = this.n - 1;
        maxDist = endDist;
    }

    // insert seatPos into sorted array
    let lo = 0, hi = this.seats.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (this.seats[mid] < seatPos) lo = mid + 1;
        else hi = mid;
    }
    this.seats.splice(lo, 0, seatPos);
    return seatPos;
};

ExamRoom.prototype.leave = function(p) {
    let lo = 0, hi = this.seats.length - 1;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (this.seats[mid] === p) {
            this.seats.splice(mid, 1);
            return;
        } else if (this.seats[mid] < p) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
};
```

## Typescript

```typescript
class ExamRoom {
    private n: number;
    private seats: number[];

    constructor(n: number) {
        this.n = n;
        this.seats = [];
    }

    seat(): number {
        if (this.seats.length === 0) {
            this.seats.push(0);
            return 0;
        }

        let maxDist = -1;
        let bestSeat = 0;

        // Check the first gap
        const first = this.seats[0];
        if (first !== 0) {
            const dist = first; // distance to the nearest occupied seat
            if (dist > maxDist) {
                maxDist = dist;
                bestSeat = 0;
            }
        }

        // Check middle gaps
        for (let i = 0; i < this.seats.length - 1; i++) {
            const a = this.seats[i];
            const b = this.seats[i + 1];
            const dist = Math.floor((b - a) / 2);
            const seatPos = a + dist;
            if (dist > maxDist) {
                maxDist = dist;
                bestSeat = seatPos;
            }
        }

        // Check the last gap
        const last = this.seats[this.seats.length - 1];
        if (last !== this.n - 1) {
            const dist = this.n - 1 - last;
            if (dist > maxDist) {
                maxDist = dist;
                bestSeat = this.n - 1;
            }
        }

        // Insert the chosen seat into the sorted list
        const idx = this.findInsertPos(bestSeat);
        this.seats.splice(idx, 0, bestSeat);
        return bestSeat;
    }

    leave(p: number): void {
        const idx = this.seats.indexOf(p);
        if (idx !== -1) {
            this.seats.splice(idx, 1);
        }
    }

    private findInsertPos(val: number): number {
        let lo = 0, hi = this.seats.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (this.seats[mid] < val) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * var obj = new ExamRoom(n)
 * var param_1 = obj.seat()
 * obj.leave(p)
 */
```

## Php

```php
class ExamRoom {
    private int $n;
    private array $occupied = [];
    private SplPriorityQueue $heap;
    private array $intervalMap = [];

    public function __construct($n) {
        $this->n = $n;
        $this->heap = new SplPriorityQueue();
        $this->heap->setExtractFlags(SplPriorityQueue::EXTR_DATA);
    }

    private function computeDistance(int $s, int $e): int {
        if ($s == -1) {
            return $e;
        }
        if ($e == $this->n) {
            return $this->n - 1 - $s;
        }
        return intdiv($e - $s, 2);
    }

    private function addInterval(int $s, int $e): void {
        // ensure there is at least one empty seat in the interval
        if ($s == -1) {
            if ($e <= 0) return;
        } elseif ($e == $this->n) {
            if ($e - $s <= 1) return;
        } else {
            if ($e - $s <= 1) return;
        }
        $key = $s . ':' . $e;
        $this->intervalMap[$key] = true;
        $dist = $this->computeDistance($s, $e);
        $priority = [$dist, -$s]; // larger distance first, then smaller start
        $this->heap->insert([$s, $e], $priority);
    }

    private function insertOccupied(int $p): void {
        $lo = 0;
        $hi = count($this->occupied);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->occupied[$mid] < $p) {
                $lo = $mid + 1;
            } else {
                $hi = $mid;
            }
        }
        array_splice($this->occupied, $lo, 0, [$p]);
    }

    public function seat() {
        if (empty($this->occupied)) {
            $this->insertOccupied(0);
            $this->addInterval(0, $this->n);
            return 0;
        }

        while (!$this->heap->isEmpty()) {
            $interval = $this->heap->extract(); // [s, e]
            $key = $interval[0] . ':' . $interval[1];
            if (!isset($this->intervalMap[$key])) {
                continue; // stale interval
            }
            unset($this->intervalMap[$key]);
            [$s, $e] = $interval;

            if ($s == -1) {
                $p = 0;
            } elseif ($e == $this->n) {
                $p = $this->n - 1;
            } else {
                $p = $s + intdiv($e - $s, 2);
            }

            $this->insertOccupied($p);

            // left interval
            if ($s != -1 && $p - $s > 0) {
                $this->addInterval($s, $p);
            } elseif ($s == -1 && $p > 0) {
                $this->addInterval(-1, $p);
            }

            // right interval
            if ($e != $this->n && $e - $p > 0) {
                $this->addInterval($p, $e);
            } elseif ($e == $this->n && $p < $this->n - 1) {
                $this->addInterval($p, $this->n);
            }

            return $p;
        }
        return -1; // should never reach here
    }

    public function leave($p) {
        // locate index of p in occupied list
        $idx = null;
        $lo = 0;
        $hi = count($this->occupied) - 1;
        while ($lo <= $hi) {
            $mid = intdiv(($lo + $hi), 2);
            if ($this->occupied[$mid] == $p) {
                $idx = $mid;
                break;
            } elseif ($this->occupied[$mid] < $p) {
                $lo = $mid + 1;
            } else {
                $hi = $mid - 1;
            }
        }

        // determine neighbors
        $left = -1;
        if ($idx > 0) {
            $left = $this->occupied[$idx - 1];
        }
        $right = $this->n;
        if ($idx < count($this->occupied) - 1) {
            $right = $this->occupied[$idx + 1];
        }

        // remove p from occupied
        array_splice($this->occupied, $idx, 1);

        // invalidate old intervals
        $key1 = $left . ':' . $p;
        $key2 = $p . ':' . $right;
        unset($this->intervalMap[$key1]);
        unset($this->intervalMap[$key2]);

        // add merged interval
        $this->addInterval($left, $right);
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * $obj = new ExamRoom($n);
 * $ret_1 = $obj->seat();
 * $obj->leave($p);
 */
```

## Swift

```swift
class ExamRoom {
    private let n: Int
    private var occupied: [Int] = []
    private var heap: MaxHeap
    private var active: Set<Pair> = Set()
    
    init(_ n: Int) {
        self.n = n
        let N = n
        func dist(_ interval: Interval) -> Int {
            if interval.l == -1 {
                return interval.r
            } else if interval.r == N {
                return N - 1 - interval.l
            } else {
                return (interval.r - interval.l) / 2
            }
        }
        let cmp: (Interval, Interval) -> Bool = { a, b in
            let da = dist(a)
            let db = dist(b)
            if da != db {
                return da > db
            } else {
                return a.l < b.l
            }
        }
        heap = MaxHeap(compare: cmp)
        let initInterval = Interval(l: -1, r: N)
        heap.push(initInterval)
        active.insert(Pair(l: -1, r: N))
    }
    
    func seat() -> Int {
        while true {
            guard let top = heap.peek() else { fatalError("Heap is empty") }
            let key = Pair(l: top.l, r: top.r)
            if active.contains(key) {
                _ = heap.pop()
                active.remove(key)
                
                var seatPos: Int
                if top.l == -1 {
                    seatPos = 0
                } else if top.r == n {
                    seatPos = n - 1
                } else {
                    seatPos = (top.l + top.r) / 2
                }
                
                let idx = lowerBound(occupied, seatPos)
                occupied.insert(seatPos, at: idx)
                
                // left interval
                if top.l == -1 && seatPos > 0 {
                    let left = Interval(l: -1, r: seatPos)
                    heap.push(left)
                    active.insert(Pair(l: left.l, r: left.r))
                } else if top.l != -1 && seatPos - top.l > 0 {
                    let left = Interval(l: top.l, r: seatPos)
                    heap.push(left)
                    active.insert(Pair(l: left.l, r: left.r))
                }
                
                // right interval
                if top.r == n && seatPos < n - 1 {
                    let right = Interval(l: seatPos, r: n)
                    heap.push(right)
                    active.insert(Pair(l: right.l, r: right.r))
                } else if top.r != n && top.r - seatPos > 0 {
                    let right = Interval(l: seatPos, r: top.r)
                    heap.push(right)
                    active.insert(Pair(l: right.l, r: right.r))
                }
                
                return seatPos
            } else {
                _ = heap.pop()
            }
        }
    }
    
    func leave(_ p: Int) {
        let idx = lowerBound(occupied, p)
        var leftNeighbor = -1
        var rightNeighbor = n
        if idx > 0 {
            leftNeighbor = occupied[idx - 1]
        }
        if idx + 1 < occupied.count {
            rightNeighbor = occupied[idx + 1]
        }
        occupied.remove(at: idx)
        
        let leftKey = Pair(l: leftNeighbor, r: p)
        active.remove(leftKey)
        let rightKey = Pair(l: p, r: rightNeighbor)
        active.remove(rightKey)
        
        let merged = Interval(l: leftNeighbor, r: rightNeighbor)
        heap.push(merged)
        active.insert(Pair(l: merged.l, r: merged.r))
    }
}

struct Interval {
    let l: Int
    let r: Int
}

struct Pair: Hashable {
    let l: Int
    let r: Int
}

struct MaxHeap {
    private var arr: [Interval] = []
    private let compare: (Interval, Interval) -> Bool
    
    init(compare: @escaping (Interval, Interval) -> Bool) {
        self.compare = compare
    }
    
    mutating func push(_ x: Interval) {
        arr.append(x)
        siftUp(arr.count - 1)
    }
    
    mutating func pop() -> Interval? {
        guard !arr.isEmpty else { return nil }
        let top = arr[0]
        let last = arr.removeLast()
        if !arr.isEmpty {
            arr[0] = last
            siftDown(0)
        }
        return top
    }
    
    func peek() -> Interval? {
        return arr.first
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if compare(arr[child], arr[parent]) {
                arr.swapAt(child, parent)
                child = parent
            } else { break }
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var candidate = parent
            if left < arr.count && compare(arr[left], arr[candidate]) {
                candidate = left
            }
            if right < arr.count && compare(arr[right], arr[candidate]) {
                candidate = right
            }
            if candidate == parent { break }
            arr.swapAt(parent, candidate)
            parent = candidate
        }
    }
}

func lowerBound(_ arr: [Int], _ target: Int) -> Int {
    var lo = 0
    var hi = arr.count
    while lo < hi {
        let mid = (lo + hi) >> 1
        if arr[mid] < target {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    return lo
}
```

## Kotlin

```kotlin
class ExamRoom(n: Int) {
    private val nSeats = n
    private val occupied = java.util.TreeSet<Int>()

    fun seat(): Int {
        if (occupied.isEmpty()) {
            occupied.add(0)
            return 0
        }

        var bestSeat = 0
        var maxDist = -1

        // Check the leftmost gap (seat 0)
        val first = occupied.first()
        if (first != 0) {
            val dist = first
            if (dist > maxDist) {
                maxDist = dist
                bestSeat = 0
            }
        }

        // Check the rightmost gap (seat n-1)
        val last = occupied.last()
        if (last != nSeats - 1) {
            val dist = (nSeats - 1) - last
            if (dist > maxDist) {
                maxDist = dist
                bestSeat = nSeats - 1
            }
        }

        // Check internal gaps
        var prev = first
        val iterator = occupied.tailSet(first, false).iterator()
        while (iterator.hasNext()) {
            val cur = iterator.next()
            val gap = cur - prev
            if (gap > 0) {
                val dist = gap / 2
                val candSeat = prev + dist
                if (dist > maxDist || (dist == maxDist && candSeat < bestSeat)) {
                    maxDist = dist
                    bestSeat = candSeat
                }
            }
            prev = cur
        }

        occupied.add(bestSeat)
        return bestSeat
    }

    fun leave(p: Int) {
        occupied.remove(p)
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * var obj = ExamRoom(n)
 * var param_1 = obj.seat()
 * obj.leave(p)
 */
```

## Dart

```dart
class ExamRoom {
  final int n;
  final List<int> _occupied = [];

  ExamRoom(this.n);

  int seat() {
    if (_occupied.isEmpty) {
      _occupied.add(0);
      return 0;
    }

    int bestSeat = 0;
    int maxDist = _occupied[0]; // distance from seat 0 to first occupied

    // Check rightmost interval
    int distRight = n - 1 - _occupied.last;
    if (distRight > maxDist) {
      maxDist = distRight;
      bestSeat = n - 1;
    }

    // Check middle intervals
    for (int i = 0; i < _occupied.length - 1; ++i) {
      int a = _occupied[i];
      int b = _occupied[i + 1];
      int d = (b - a) ~/ 2;
      int candidate = a + d;
      if (d > maxDist || (d == maxDist && candidate < bestSeat)) {
        maxDist = d;
        bestSeat = candidate;
      }
    }

    // Insert the chosen seat maintaining sorted order
    int idx = _findInsertIndex(bestSeat);
    _occupied.insert(idx, bestSeat);
    return bestSeat;
  }

  void leave(int p) {
    int idx = _binarySearch(p);
    if (idx >= 0 && idx < _occupied.length && _occupied[idx] == p) {
      _occupied.removeAt(idx);
    }
  }

  // Returns first index where element >= x
  int _findInsertIndex(int x) {
    int l = 0, r = _occupied.length;
    while (l < r) {
      int m = (l + r) >> 1;
      if (_occupied[m] < x) {
        l = m + 1;
      } else {
        r = m;
      }
    }
    return l;
  }

  // Returns index of x, or insertion point if not found
  int _binarySearch(int x) {
    int l = 0, r = _occupied.length - 1;
    while (l <= r) {
      int m = (l + r) >> 1;
      if (_occupied[m] == x) return m;
      if (_occupied[m] < x) {
        l = m + 1;
      } else {
        r = m - 1;
      }
    }
    return l; // not found, returns insertion point
  }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = ExamRoom(n);
 * int param1 = obj.seat();
 * obj.leave(p);
 */
```

## Golang

```go
import "sort"

type ExamRoom struct {
	n     int
	seats []int
}

func Constructor(n int) ExamRoom {
	return ExamRoom{n: n, seats: []int{}}
}

func (this *ExamRoom) Seat() int {
	if len(this.seats) == 0 {
		this.seats = append(this.seats, 0)
		return 0
	}

	bestDist := this.seats[0] // distance from seat 0 to first occupied
	bestSeat := 0

	// Check the gap at the end
	lastIdx := len(this.seats) - 1
	endDist := this.n - 1 - this.seats[lastIdx]
	if endDist > bestDist {
		bestDist = endDist
		bestSeat = this.n - 1
	}

	// Check middle gaps
	for i := 0; i < lastIdx; i++ {
		left := this.seats[i]
		right := this.seats[i+1]
		if right-left <= 1 {
			continue
		}
		candDist := (right - left) / 2
		candSeat := left + candDist
		if candDist > bestDist || (candDist == bestDist && candSeat < bestSeat) {
			bestDist = candDist
			bestSeat = candSeat
		}
	}

	// Insert the chosen seat maintaining sorted order
	idx := sort.SearchInts(this.seats, bestSeat)
	this.seats = append(this.seats, 0)
	copy(this.seats[idx+1:], this.seats[idx:])
	this.seats[idx] = bestSeat

	return bestSeat
}

func (this *ExamRoom) Leave(p int) {
	idx := sort.SearchInts(this.seats, p)
	if idx < len(this.seats) && this.seats[idx] == p {
		this.seats = append(this.seats[:idx], this.seats[idx+1:]...)
	}
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Seat();
 * obj.Leave(p);
 */
```

## Ruby

```ruby
Interval = Struct.new(:left, :right)

class MaxHeap
  def initialize(&comp)
    @data = []
    @comp = comp
  end

  def push(item)
    @data << item
    sift_up(@data.size - 1)
  end

  def pop
    return nil if @data.empty?
    top = @data[0]
    last = @data.pop
    unless @data.empty?
      @data[0] = last
      sift_down(0)
    end
    top
  end

  private

  def better?(a, b)
    @comp.call(a, b)
  end

  def sift_up(idx)
    while idx > 0
      parent = (idx - 1) / 2
      break unless better?(@data[idx], @data[parent])
      @data[idx], @data[parent] = @data[parent], @data[idx]
      idx = parent
    end
  end

  def sift_down(idx)
    size = @data.size
    loop do
      left = idx * 2 + 1
      right = left + 1
      largest = idx
      if left < size && better?(@data[left], @data[largest])
        largest = left
      end
      if right < size && better?(@data[right], @data[largest])
        largest = right
      end
      break if largest == idx
      @data[idx], @data[largest] = @data[largest], @data[idx]
      idx = largest
    end
  end
end

class ExamRoom
=begin
    :type n: Integer
=end
  def initialize(n)
    @n = n
    @occupied = []                     # sorted array of occupied seats
    @intervals = {}                    # map from "left,right" => true (valid intervals)
    @heap = MaxHeap.new do |a, b|
      da = interval_distance(a)
      db = interval_distance(b)
      if da != db
        da > db
      else
        a.left < b.left
      end
    end
    init_intv = Interval.new(-1, @n)
    key = interval_key(init_intv)
    @intervals[key] = true
    @heap.push(init_intv)
  end

=begin
    :rtype: Integer
=end
  def seat()
    loop do
      intv = @heap.pop
      raise "No available interval" if intv.nil?
      key = interval_key(intv)
      next unless @intervals[key]          # discard stale intervals
      @intervals.delete(key)

      s = if intv.left == -1
            0
          elsif intv.right == @n
            @n - 1
          else
            intv.left + (intv.right - intv.left) / 2
          end

      idx = @occupied.bsearch_index { |x| x > s } || @occupied.size
      @occupied.insert(idx, s)

      if intv.left != s
        left_intv = Interval.new(intv.left, s)
        lk = interval_key(left_intv)
        @intervals[lk] = true
        @heap.push(left_intv)
      end

      if s != intv.right
        right_intv = Interval.new(s, intv.right)
        rk = interval_key(right_intv)
        @intervals[rk] = true
        @heap.push(right_intv)
      end

      return s
    end
  end

=begin
    :type p: Integer
    :rtype: Void
=end
  def leave(p)
    idx = @occupied.bsearch_index { |x| x >= p }
    return unless idx && @occupied[idx] == p

    left = idx > 0 ? @occupied[idx - 1] : -1
    right = (idx + 1) < @occupied.size ? @occupied[idx + 1] : @n

    @occupied.delete_at(idx)

    intv_left = Interval.new(left, p)
    @intervals.delete(interval_key(intv_left))

    intv_right = Interval.new(p, right)
    @intervals.delete(interval_key(intv_right))

    merged = Interval.new(left, right)
    mk = interval_key(merged)
    @intervals[mk] = true
    @heap.push(merged)
  end

  private

  def interval_key(intv)
    "#{intv.left},#{intv.right}"
  end

  def interval_distance(intv)
    if intv.left == -1
      intv.right
    elsif intv.right == @n
      @n - 1 - intv.left
    else
      (intv.right - intv.left) / 2
    end
  end
end

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom.new(n)
# param_1 = obj.seat()
# obj.leave(p)
```

## Scala

```scala
import java.util.TreeSet

class ExamRoom(_n: Int) {
  private val n: Int = _n
  private val occupied = new TreeSet[Int]()

  def seat(): Int = {
    if (occupied.isEmpty) {
      occupied.add(0)
      return 0
    }

    var bestSeat = 0
    var maxDist = -1

    // left edge
    val first = occupied.first()
    maxDist = first
    bestSeat = 0

    // intervals between occupied seats
    val it = occupied.iterator()
    var prev = it.next() // first element already considered
    while (it.hasNext) {
      val cur = it.next()
      val dist = (cur - prev) / 2
      if (dist > maxDist) {
        maxDist = dist
        bestSeat = prev + dist
      }
      prev = cur
    }

    // right edge
    val last = occupied.last()
    val rightDist = n - 1 - last
    if (rightDist > maxDist) {
      bestSeat = n - 1
    }

    occupied.add(bestSeat)
    bestSeat
  }

  def leave(p: Int): Unit = {
    occupied.remove(p)
  }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * val obj = new ExamRoom(n)
 * val param_1 = obj.seat()
 * obj.leave(p)
 */
```

## Rust

```rust
use std::collections::BTreeSet;

pub struct ExamRoom {
    n: i32,
    occupied: BTreeSet<i32>,
}

impl ExamRoom {
    pub fn new(n: i32) -> Self {
        ExamRoom {
            n,
            occupied: BTreeSet::new(),
        }
    }

    pub fn seat(&mut self) -> i32 {
        if self.occupied.is_empty() {
            self.occupied.insert(0);
            return 0;
        }

        let mut best_seat = 0;
        let mut max_dist: i64 = -1;

        // distance from start (seat 0)
        let first = *self.occupied.iter().next().unwrap();
        let dist_start = first as i64;
        if dist_start > max_dist {
            max_dist = dist_start;
            best_seat = 0;
        }

        // check gaps between occupied seats
        let mut prev = first;
        for &curr in self.occupied.iter().skip(1) {
            let gap = curr - prev;
            let cand = prev + gap / 2;
            let dist = (gap / 2) as i64;
            if dist > max_dist || (dist == max_dist && cand < best_seat) {
                max_dist = dist;
                best_seat = cand;
            }
            prev = curr;
        }

        // distance from end (seat n-1)
        let last = *self.occupied.iter().next_back().unwrap();
        let dist_end = (self.n - 1 - last) as i64;
        if dist_end > max_dist {
            best_seat = self.n - 1;
        }

        self.occupied.insert(best_seat);
        best_seat
    }

    pub fn leave(&mut self, p: i32) {
        self.occupied.remove(&p);
    }
}

/*
Your ExamRoom object will be instantiated and called as such:
let mut obj = ExamRoom::new(n);
let ret_1: i32 = obj.seat();
obj.leave(p);
*/
```

## Racket

```racket
(define exam-room%
  (class object%
    (super-new)
    (init-field n)

    (define seats '())

    (define (insert-seat s)
      (let loop ((prev '()) (rest seats))
        (cond
          [(null? rest) (set! seats (append (reverse prev) (list s)))]
          [(< s (car rest))
           (set! seats (append (reverse prev) (cons s rest)))]
          [else (loop (cons (car rest) prev) (cdr rest))])))

    (define (remove-seat p)
      (let loop ((prev '()) (rest seats))
        (cond
          [(null? rest) (set! seats (reverse prev))]
          [(= (car rest) p)
           (set! seats (append (reverse prev) (cdr rest)))]
          [else (loop (cons (car rest) prev) (cdr rest))])))

    (define/public (seat)
      (if (null? seats)
          (begin
            (set! seats (list 0))
            0)
          (let* ((best-seat -1)
                 (best-dist -1))
            (define first (car seats))
            (when (> first best-dist)
              (set! best-dist first)
              (set! best-seat 0))
            (let loop ((prev first) (rest (cdr seats)))
              (unless (null? rest)
                (define cur (car rest))
                (define d (quotient (- cur prev) 2))
                (define cand (+ prev d))
                (when (> d best-dist)
                  (set! best-dist d)
                  (set! best-seat cand))
                (loop cur (cdr rest))))
            (define last (car (reverse seats)))
            (define dist-end (- (- n 1) last))
            (when (> dist-end best-dist)
              (set! best-dist dist-end)
              (set! best-seat (- n 1)))
            (insert-seat best-seat)
            best-seat)))

    (define/public (leave p)
      (remove-seat p))))
```

## Erlang

```erlang
-spec exam_room_init_(N :: integer()) -> any().
exam_room_init_(N) ->
    put(state, {N, []}),
    ok.

-spec exam_room_seat() -> integer().
exam_room_seat() ->
    State = get(state),
    {N, Seats} = State,
    case Seats of
        [] ->
            NewSeats = [0],
            put(state, {N, NewSeats}),
            0;
        _ ->
            {BestSeat, _Dist} = find_best(N, Seats),
            NewSeats = insert_sorted(BestSeat, Seats),
            put(state, {N, NewSeats}),
            BestSeat
    end.

-spec exam_room_leave(P :: integer()) -> any().
exam_room_leave(P) ->
    State = get(state),
    {N, Seats} = State,
    NewSeats = lists:delete(P, Seats),
    put(state, {N, NewSeats}),
    ok.

%% helper functions

find_best(N, Seats) ->
    First = hd(Seats),
    StartDist = First,
    StartSeat = 0,
    Last = lists:last(Seats),
    EndDist = N - 1 - Last,
    {BestSoFar, MaxDist} = iter_gaps(Seats, StartSeat, StartDist),
    case EndDist > MaxDist orelse (EndDist == MaxDist andalso (N-1) < BestSoFar) of
        true -> {(N-1), EndDist};
        false -> {BestSoFar, MaxDist}
    end.

iter_gaps([_], BestSeat, MaxDist) ->
    {BestSeat, MaxDist};
iter_gaps([A,B|Rest], BestSeat, MaxDist) ->
    Gap = B - A,
    Dist = Gap div 2,
    Cand = A + Dist,
    {NewBestSeat, NewMaxDist} =
        if
            Dist > MaxDist -> {Cand, Dist};
            Dist == MaxDist andalso Cand < BestSeat -> {Cand, Dist};
            true -> {BestSeat, MaxDist}
        end,
    iter_gaps([B|Rest], NewBestSeat, NewMaxDist).

insert_sorted(Seat, []) ->
    [Seat];
insert_sorted(Seat, [H|T]) when Seat < H ->
    [Seat, H | T];
insert_sorted(Seat, [H|T]) ->
    [H | insert_sorted(Seat, T)].
```

## Elixir

```elixir
defmodule ExamRoom do
  @spec init_(n :: integer) :: any
  def init_(n) do
    :erlang.put(:exam_room_state, %{n: n, occ: []})
  end

  @spec seat() :: integer
  def seat() do
    state = :erlang.get(:exam_room_state)
    n = state.n
    occ = state.occ

    seat =
      if occ == [] do
        0
      else
        # start edge
        first = hd(occ)
        max_dist = first
        best_seat = 0

        # middle intervals
        {max_dist, best_seat} =
          Enum.reduce(Enum.chunk_every(occ, 2, 1, []), {max_dist, best_seat}, fn [a, b], acc ->
            candidate = div(a + b, 2)
            dist = candidate - a

            case acc do
              {cur_max, cur_best} when dist > cur_max -> {dist, candidate}
              _ -> acc
            end
          end)

        # end edge
        last = List.last(occ)
        dist_end = n - 1 - last

        if dist_end > max_dist do
          n - 1
        else
          best_seat
        end
      end

    new_occ = insert_sorted(state.occ, seat)
    :erlang.put(:exam_room_state, %{state | occ: new_occ})
    seat
  end

  @spec leave(p :: integer) :: any
  def leave(p) do
    state = :erlang.get(:exam_room_state)
    new_occ = List.delete(state.occ, p)
    :erlang.put(:exam_room_state, %{state | occ: new_occ})
  end

  # Helper to insert while keeping the list sorted
  defp insert_sorted([], v), do: [v]

  defp insert_sorted([h | _] = list, v) when v < h, do: [v | list]

  defp insert_sorted([h | t], v), do: [h | insert_sorted(t, v)]
end
```
