# 1847. Closest Room

## Cpp

```cpp
class Solution {
public:
    vector<int> closestRoom(vector<vector<int>>& rooms, vector<vector<int>>& queries) {
        int n = rooms.size();
        int q = queries.size();
        // sort rooms by size descending
        vector<pair<int,int>> roomList;
        roomList.reserve(n);
        for (auto &r : rooms) {
            roomList.emplace_back(r[1], r[0]); // {size, id}
        }
        sort(roomList.begin(), roomList.end(),
             [](const pair<int,int>& a, const pair<int,int>& b){ return a.first > b.first; });
        
        struct Q {
            int pref;
            int minSize;
            int idx;
        };
        vector<Q> qs;
        qs.reserve(q);
        for (int i = 0; i < q; ++i) {
            qs.push_back({queries[i][0], queries[i][1], i});
        }
        sort(qs.begin(), qs.end(),
             [](const Q& a, const Q& b){ return a.minSize > b.minSize; });
        
        vector<int> ans(q, -1);
        std::set<int> ids;
        int rp = 0;
        for (const auto &cur : qs) {
            while (rp < n && roomList[rp].first >= cur.minSize) {
                ids.insert(roomList[rp].second);
                ++rp;
            }
            if (ids.empty()) {
                ans[cur.idx] = -1;
                continue;
            }
            long long bestDist = LLONG_MAX;
            int bestId = -1;
            auto it = ids.lower_bound(cur.pref);
            if (it != ids.end()) {
                long long dist = llabs((long long)*it - cur.pref);
                if (dist < bestDist || (dist == bestDist && *it < bestId)) {
                    bestDist = dist;
                    bestId = *it;
                }
            }
            if (it != ids.begin()) {
                auto it2 = prev(it);
                long long dist = llabs((long long)*it2 - cur.pref);
                if (dist < bestDist || (dist == bestDist && *it2 < bestId)) {
                    bestDist = dist;
                    bestId = *it2;
                }
            }
            ans[cur.idx] = bestId;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] closestRoom(int[][] rooms, int[][] queries) {
        int n = rooms.length;
        int q = queries.length;

        // Sort rooms by size descending
        Arrays.sort(rooms, (a, b) -> Integer.compare(b[1], a[1]));

        // Prepare query objects with original indices
        Query[] qs = new Query[q];
        for (int i = 0; i < q; i++) {
            qs[i] = new Query(queries[i][0], queries[i][1], i);
        }
        // Sort queries by minSize descending
        Arrays.sort(qs, (a, b) -> Integer.compare(b.minSize, a.minSize));

        TreeSet<Integer> eligibleIds = new TreeSet<>();
        int[] answer = new int[q];
        int roomPtr = 0;

        for (Query cur : qs) {
            // Add all rooms that satisfy the current minSize requirement
            while (roomPtr < n && rooms[roomPtr][1] >= cur.minSize) {
                eligibleIds.add(rooms[roomPtr][0]);
                roomPtr++;
            }

            if (eligibleIds.isEmpty()) {
                answer[cur.idx] = -1;
                continue;
            }

            Integer lower = eligibleIds.floor(cur.pref);
            Integer higher = eligibleIds.ceiling(cur.pref);

            int bestId = -1;
            long bestDiff = Long.MAX_VALUE;

            if (lower != null) {
                bestDiff = Math.abs((long) lower - cur.pref);
                bestId = lower;
            }
            if (higher != null) {
                long diff = Math.abs((long) higher - cur.pref);
                if (diff < bestDiff || (diff == bestDiff && higher < bestId)) {
                    bestDiff = diff;
                    bestId = higher;
                }
            }

            answer[cur.idx] = bestId;
        }

        return answer;
    }

    private static class Query {
        int pref;
        int minSize;
        int idx;

        Query(int pref, int minSize, int idx) {
            this.pref = pref;
            this.minSize = minSize;
            this.idx = idx;
        }
    }
}
```

## Python

```python
class Solution(object):
    def closestRoom(self, rooms, queries):
        """
        :type rooms: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # sort rooms by size descending
        rooms.sort(key=lambda x: -x[1])
        n = len(rooms)

        # prepare sorted list of all room ids for indexing
        ids_sorted = sorted([room[0] for room in rooms])
        id_to_idx = {rid: i+1 for i, rid in enumerate(ids_sorted)}  # 1-indexed for BIT

        class BIT:
            __slots__ = ('n', 'bit')
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 2)
            def add(self, i, delta):
                while i <= self.n:
                    self.bit[i] += delta
                    i += i & -i
            def sum(self, i):
                s = 0
                while i > 0:
                    s += self.bit[i]
                    i -= i & -i
                return s
            def total(self):
                return self.sum(self.n)
            # find smallest index such that prefix sum >= k (1-indexed k)
            def kth(self, k):
                idx = 0
                bitmask = 1 << (self.n.bit_length())
                while bitmask:
                    nxt = idx + bitmask
                    if nxt <= self.n and self.bit[nxt] < k:
                        idx = nxt
                        k -= self.bit[nxt]
                    bitmask >>= 1
                return idx + 1

        bit = BIT(n)

        # sort queries by minSize descending, keep original index
        qlist = [(pref, sz, i) for i, (pref, sz) in enumerate(queries)]
        qlist.sort(key=lambda x: -x[1])

        ans = [-1] * len(queries)
        rptr = 0

        import bisect

        for pref, minSize, qi in qlist:
            # add all rooms with size >= minSize
            while rptr < n and rooms[rptr][1] >= minSize:
                rid = rooms[rptr][0]
                bit.add(id_to_idx[rid], 1)
                rptr += 1

            if bit.total() == 0:
                ans[qi] = -1
                continue

            # predecessor (largest id <= pref)
            pred_id = None
            pos = bisect.bisect_right(ids_sorted, pref)   # number of ids <= pref
            if pos > 0:
                cnt = bit.sum(pos)
                if cnt > 0:
                    idx_pred = bit.kth(cnt)               # last present in prefix
                    pred_id = ids_sorted[idx_pred - 1]

            # successor (smallest id >= pref)
            succ_id = None
            pos2 = bisect.bisect_left(ids_sorted, pref)   # first index with id >= pref (0‑based)
            cnt_before = bit.sum(pos2)                    # present count before this position
            total_present = bit.total()
            if total_present - cnt_before > 0:
                idx_succ = bit.kth(cnt_before + 1)
                succ_id = ids_sorted[idx_succ - 1]

            # choose best answer
            if pred_id is None:
                ans[qi] = succ_id
            elif succ_id is None:
                ans[qi] = pred_id
            else:
                d1 = abs(pred_id - pref)
                d2 = abs(succ_id - pref)
                if d1 < d2:
                    ans[qi] = pred_id
                elif d2 < d1:
                    ans[qi] = succ_id
                else:
                    ans[qi] = min(pred_id, succ_id)

        return ans
```

## Python3

```python
import bisect
from typing import List

class BIT:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:  # i is 1‑based
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i: int) -> int:  # prefix sum up to i (inclusive), i is 1‑based
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def kth(self, k: int) -> int:
        """return smallest index such that prefix sum >= k (1‑based)"""
        idx = 0
        bitmask = 1 << (self.n.bit_length())
        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bitmask >>= 1
        return idx + 1

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(rooms)
        # static ordering of room ids for compression
        sorted_ids = sorted(room[0] for room in rooms)
        id_to_idx = {room_id: i for i, room_id in enumerate(sorted_ids)}

        # sort rooms by size descending
        rooms_by_size = sorted(rooms, key=lambda x: -x[1])

        # queries: (minSize, preferred, original_index) sorted by minSize descending
        qinfo = [(queries[i][1], queries[i][0], i) for i in range(len(queries))]
        qinfo.sort(key=lambda x: -x[0])

        bit = BIT(n)
        ans = [-1] * len(queries)
        rptr = 0

        for minSize, pref, qidx in qinfo:
            # add all rooms with size >= current minSize
            while rptr < n and rooms_by_size[rptr][1] >= minSize:
                room_id = rooms_by_size[rptr][0]
                idx = id_to_idx[room_id] + 1  # BIT is 1‑based
                bit.add(idx, 1)
                rptr += 1

            total_present = bit.sum(n)
            if total_present == 0:
                ans[qidx] = -1
                continue

            pos = bisect.bisect_left(sorted_ids, pref)  # position in [0, n]
            cnt_left = bit.sum(pos)  # number of present ids with index < pos

            left_id = None
            right_id = None

            if cnt_left > 0:
                idx_left = bit.kth(cnt_left) - 1
                left_id = sorted_ids[idx_left]

            if cnt_left < total_present:
                idx_right = bit.kth(cnt_left + 1) - 1
                right_id = sorted_ids[idx_right]

            best = -1
            if left_id is not None and right_id is not None:
                dleft = abs(left_id - pref)
                dright = abs(right_id - pref)
                if dleft < dright or (dleft == dright and left_id < right_id):
                    best = left_id
                else:
                    best = right_id
            elif left_id is not None:
                best = left_id
            elif right_id is not None:
                best = right_id

            ans[qidx] = best if best != -1 else -1

        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

typedef struct {
    int id;
    int size;
} Room;

typedef struct {
    int pref;
    int minSize;
    int idx;
} Query;

typedef struct {
    int n;
    int *tree;
} BIT;

static BIT* bitCreate(int n) {
    BIT *b = (BIT *)malloc(sizeof(BIT));
    b->n = n;
    b->tree = (int *)calloc(n + 2, sizeof(int));
    return b;
}
static void bitUpdate(BIT *b, int idx, int delta) { // idx: 0‑based
    for (int i = idx + 1; i <= b->n; i += i & -i)
        b->tree[i] += delta;
}
static int bitQuery(BIT *b, int idx) { // prefix sum up to idx inclusive, idx may be -1
    if (idx < 0) return 0;
    int res = 0;
    for (int i = idx + 1; i > 0; i -= i & -i)
        res += b->tree[i];
    return res;
}
static int bitFindKth(BIT *b, int k) { // 1‑based kth element present, returns 1‑based index
    int idx = 0;
    int mask = 1;
    while ((mask << 1) <= b->n) mask <<= 1;
    for (int d = mask; d; d >>= 1) {
        int next = idx + d;
        if (next <= b->n && b->tree[next] < k) {
            idx = next;
            k -= b->tree[next];
        }
    }
    return idx + 1; // convert to 1‑based position
}
static int cmpRoomDesc(const void *a, const void *b) {
    const Room *ra = (const Room *)a;
    const Room *rb = (const Room *)b;
    return rb->size - ra->size;
}
static int cmpQueryDesc(const void *a, const void *b) {
    const Query *qa = (const Query *)a;
    const Query *qb = (const Query *)b;
    return qb->minSize - qa->minSize;
}
static int lowerBound(int *arr, int n, int target) {
    int l = 0, r = n;
    while (l < r) {
        int m = (l + r) >> 1;
        if (arr[m] < target)
            l = m + 1;
        else
            r = m;
    }
    return l;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* closestRoom(int** rooms, int roomsSize, int* roomsColSize,
                 int** queries, int queriesSize, int* queriesColSize,
                 int* returnSize) {
    // Extract rooms
    Room *roomArr = (Room *)malloc(sizeof(Room) * roomsSize);
    for (int i = 0; i < roomsSize; ++i) {
        roomArr[i].id   = rooms[i][0];
        roomArr[i].size = rooms[i][1];
    }
    qsort(roomArr, roomsSize, sizeof(Room), cmpRoomDesc);

    // All ids sorted ascending for compression
    int *allIds = (int *)malloc(sizeof(int) * roomsSize);
    for (int i = 0; i < roomsSize; ++i) allIds[i] = roomArr[i].id;
    qsort(allIds, roomsSize, sizeof(int), (int (*)(const void *, const void *))strcmp); // use strcmp trick? replace with custom
    // Actually need numeric sort:
    int cmpInt(const void *a, const void *b) {
        return (*(int *)a) - (*(int *)b);
    }
    qsort(allIds, roomsSize, sizeof(int), cmpInt);

    // Prepare queries
    Query *qArr = (Query *)malloc(sizeof(Query) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        qArr[i].pref    = queries[i][0];
        qArr[i].minSize = queries[i][1];
        qArr[i].idx     = i;
    }
    qsort(qArr, queriesSize, sizeof(Query), cmpQueryDesc);

    // BIT over compressed ids
    BIT *bit = bitCreate(roomsSize);
    int *ans = (int *)malloc(sizeof(int) * queriesSize);
    int rPos = 0; // index in roomArr

    for (int i = 0; i < queriesSize; ++i) {
        Query cur = qArr[i];
        while (rPos < roomsSize && roomArr[rPos].size >= cur.minSize) {
            int compIdx = lowerBound(allIds, roomsSize, roomArr[rPos].id);
            // exact match guaranteed
            bitUpdate(bit, compIdx, 1);
            ++rPos;
        }
        int total = bitQuery(bit, roomsSize - 1);
        if (total == 0) {
            ans[cur.idx] = -1;
            continue;
        }

        int pos = lowerBound(allIds, roomsSize, cur.pref); // first id >= pref
        int predIdx = -1, succIdx = -1;

        // predecessor
        if (pos > 0) {
            int cnt = bitQuery(bit, pos - 1);
            if (cnt > 0) {
                int kthPos = bitFindKth(bit, cnt); // 1‑based
                predIdx = kthPos - 1;
            }
        }

        // successor
        int cntLess = (pos == 0) ? 0 : bitQuery(bit, pos - 1);
        if (cntLess < total) {
            int kthPos = bitFindKth(bit, cntLess + 1);
            succIdx = kthPos - 1;
        }

        long long bestDist = LLONG_MAX;
        int bestId = -1;
        if (predIdx != -1) {
            int id = allIds[predIdx];
            long long d = llabs((long long)id - cur.pref);
            bestDist = d;
            bestId = id;
        }
        if (succIdx != -1) {
            int id = allIds[succIdx];
            long long d = llabs((long long)id - cur.pref);
            if (d < bestDist || (d == bestDist && id < bestId)) {
                bestDist = d;
                bestId = id;
            }
        }
        ans[cur.idx] = bestId;
    }

    *returnSize = queriesSize;
    free(roomArr);
    free(allIds);
    free(qArr);
    free(bit->tree);
    free(bit);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] ClosestRoom(int[][] rooms, int[][] queries) {
        int n = rooms.Length;
        // Sort rooms by size descending
        System.Array.Sort(rooms, (a, b) => b[1].CompareTo(a[1]));
        
        int k = queries.Length;
        var qs = new Query[k];
        for (int i = 0; i < k; i++) {
            qs[i] = new Query { pref = queries[i][0], minSize = queries[i][1], idx = i };
        }
        // Sort queries by minSize descending
        System.Array.Sort(qs, (a, b) => b.minSize.CompareTo(a.minSize));
        
        var result = new int[k];
        var ids = new SortedSet<int>();
        int roomPtr = 0;
        
        foreach (var q in qs) {
            while (roomPtr < n && rooms[roomPtr][1] >= q.minSize) {
                ids.Add(rooms[roomPtr][0]);
                roomPtr++;
            }
            
            if (ids.Count == 0) {
                result[q.idx] = -1;
                continue;
            }
            
            int pref = q.pref;
            int? ceil = null, floor = null;
            
            var viewCeil = ids.GetViewBetween(pref, int.MaxValue);
            if (viewCeil.Count > 0) ceil = viewCeil.Min;
            
            var viewFloor = ids.GetViewBetween(int.MinValue, pref);
            if (viewFloor.Count > 0) floor = viewFloor.Max;
            
            int bestId = -1;
            long bestDiff = long.MaxValue;
            
            if (ceil.HasValue) {
                bestDiff = System.Math.Abs((long)ceil.Value - pref);
                bestId = ceil.Value;
            }
            if (floor.HasValue) {
                long diff = System.Math.Abs((long)floor.Value - pref);
                if (bestId == -1 || diff < bestDiff || (diff == bestDiff && floor.Value < bestId)) {
                    bestDiff = diff;
                    bestId = floor.Value;
                }
            }
            
            result[q.idx] = bestId;
        }
        
        return result;
    }
    
    private struct Query {
        public int pref;
        public int minSize;
        public int idx;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} rooms
 * @param {number[][]} queries
 * @return {number[]}
 */
var closestRoom = function(rooms, queries) {
    // Treap node definition
    class Node {
        constructor(key) {
            this.key = key;
            this.pri = Math.random();
            this.left = null;
            this.right = null;
        }
    }

    const rotateRight = (y) => {
        const x = y.left;
        y.left = x.right;
        x.right = y;
        return x;
    };

    const rotateLeft = (x) => {
        const y = x.right;
        x.right = y.left;
        y.left = x;
        return y;
    };

    const treapInsert = (root, key) => {
        if (!root) return new Node(key);
        if (key < root.key) {
            root.left = treapInsert(root.left, key);
            if (root.left.pri > root.pri) {
                root = rotateRight(root);
            }
        } else {
            root.right = treapInsert(root.right, key);
            if (root.right.pri > root.pri) {
                root = rotateLeft(root);
            }
        }
        return root;
    };

    const lowerBound = (root, key) => {
        let ans = null;
        while (root) {
            if (root.key >= key) {
                ans = root.key;
                root = root.left;
            } else {
                root = root.right;
            }
        }
        return ans;
    };

    const predecessor = (root, key) => {
        let ans = null;
        while (root) {
            if (root.key < key) {
                ans = root.key;
                root = root.right;
            } else {
                root = root.left;
            }
        }
        return ans;
    };

    // Sort rooms by size descending
    rooms.sort((a, b) => b[1] - a[1]);

    // Attach original index to queries and sort by minSize descending
    const qWithIdx = queries.map((q, i) => ({ pref: q[0], minSize: q[1], idx: i }));
    qWithIdx.sort((a, b) => b.minSize - a.minSize);

    let root = null;
    let rPos = 0;
    const ans = new Array(queries.length).fill(-1);

    for (const query of qWithIdx) {
        while (rPos < rooms.length && rooms[rPos][1] >= query.minSize) {
            root = treapInsert(root, rooms[rPos][0]);
            rPos++;
        }

        if (!root) {
            ans[query.idx] = -1;
            continue;
        }

        const pref = query.pref;
        const lb = lowerBound(root, pref);
        const pred = predecessor(root, pref);

        let bestId = -1;
        let bestDist = Infinity;

        if (lb !== null) {
            const d = Math.abs(lb - pref);
            if (d < bestDist || (d === bestDist && lb < bestId)) {
                bestDist = d;
                bestId = lb;
            }
        }

        if (pred !== null) {
            const d = Math.abs(pred - pref);
            if (d < bestDist || (d === bestDist && pred < bestId)) {
                bestDist = d;
                bestId = pred;
            }
        }

        ans[query.idx] = bestId;
    }

    return ans;
};
```

## Typescript

```typescript
function closestRoom(rooms: number[][], queries: number[][]): number[] {
    // Treap node definition
    class Node {
        key: number;
        prio: number;
        left: Node | null = null;
        right: Node | null = null;
        constructor(key: number) {
            this.key = key;
            this.prio = Math.random();
        }
    }

    const rotateRight = (y: Node): Node => {
        const x = y.left!;
        y.left = x.right;
        x.right = y;
        return x;
    };

    const rotateLeft = (x: Node): Node => {
        const y = x.right!;
        x.right = y.left;
        y.left = x;
        return y;
    };

    const insert = (root: Node | null, key: number): Node => {
        if (!root) return new Node(key);
        if (key < root.key) {
            root.left = insert(root.left, key);
            if (root.left.prio < root.prio) root = rotateRight(root);
        } else {
            root.right = insert(root.right, key);
            if (root.right.prio < root.prio) root = rotateLeft(root);
        }
        return root;
    };

    const lowerBound = (root: Node | null, target: number): Node | null => {
        let cur = root;
        let ans: Node | null = null;
        while (cur) {
            if (cur.key >= target) {
                ans = cur;
                cur = cur.left;
            } else {
                cur = cur.right;
            }
        }
        return ans;
    };

    const predecessor = (root: Node | null, target: number): Node | null => {
        let cur = root;
        let ans: Node | null = null;
        while (cur) {
            if (cur.key < target) {
                ans = cur;
                cur = cur.right;
            } else {
                cur = cur.left;
            }
        }
        return ans;
    };

    // Sort rooms by size descending
    rooms.sort((a, b) => b[1] - a[1]);

    // Prepare queries with original indices and sort by minSize descending
    const qObjs = queries.map((q, i) => ({ pref: q[0], minSize: q[1], idx: i }));
    qObjs.sort((a, b) => b.minSize - a.minSize);

    let root: Node | null = null;
    let rIdx = 0;
    const ans = new Array(queries.length).fill(-1);

    for (const q of qObjs) {
        while (rIdx < rooms.length && rooms[rIdx][1] >= q.minSize) {
            root = insert(root, rooms[rIdx][0]);
            rIdx++;
        }
        if (!root) {
            ans[q.idx] = -1;
            continue;
        }

        const succNode = lowerBound(root, q.pref);
        const predNode = predecessor(root, q.pref);

        let bestId = -1;
        let bestDiff = Infinity;

        if (succNode) {
            bestDiff = Math.abs(succNode.key - q.pref);
            bestId = succNode.key;
        }
        if (predNode) {
            const diff = Math.abs(predNode.key - q.pref);
            if (diff < bestDiff || (diff === bestDiff && predNode.key < bestId)) {
                bestDiff = diff;
                bestId = predNode.key;
            }
        }

        ans[q.idx] = bestId;
    }

    return ans;
}
```

## Php

```php
class TreapNode {
    public int $key;
    public int $prio;
    public ?TreapNode $left = null;
    public ?TreapNode $right = null;

    public function __construct(int $key) {
        $this->key = $key;
        // mt_rand returns up to PHP_INT_MAX, sufficient for priority
        $this->prio = mt_rand();
    }
}

class Solution {

    /**
     * @param Integer[][] $rooms
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function closestRoom($rooms, $queries) {
        // sort rooms by size descending
        usort($rooms, function($a, $b) {
            return $b[1] <=> $a[1];
        });

        // augment queries with original index and sort by minSize descending
        $q = [];
        foreach ($queries as $idx => $qr) {
            $q[] = [$qr[0], $qr[1], $idx]; // preferred, minSize, idx
        }
        usort($q, function($a, $b) {
            return $b[1] <=> $a[1];
        });

        $ans = array_fill(0, count($queries), -1);
        $root = null;
        $i = 0; // pointer for rooms

        foreach ($q as $query) {
            [$pref, $minSize, $origIdx] = $query;

            while ($i < count($rooms) && $rooms[$i][1] >= $minSize) {
                $roomId = $rooms[$i][0];
                $root = $this->treapInsert($root, $roomId);
                $i++;
            }

            if ($root === null) {
                $ans[$origIdx] = -1;
                continue;
            }

            $lb = $this->lowerBound($root, $pref);      // smallest id >= pref
            $pred = $this->predecessor($root, $pref);   // largest id < pref

            $bestId = null;
            $bestDiff = PHP_INT_MAX;

            if ($lb !== null) {
                $diff = abs($lb - $pref);
                $bestId = $lb;
                $bestDiff = $diff;
            }
            if ($pred !== null) {
                $diff = abs($pred - $pref);
                if ($diff < $bestDiff || ($diff == $bestDiff && $pred < $bestId)) {
                    $bestId = $pred;
                    $bestDiff = $diff;
                }
            }

            $ans[$origIdx] = $bestId ?? -1;
        }

        return $ans;
    }

    private function treapInsert(?TreapNode $root, int $key): TreapNode {
        if ($root === null) {
            return new TreapNode($key);
        }
        if ($key < $root->key) {
            $root->left = $this->treapInsert($root->left, $key);
            if ($root->left !== null && $root->left->prio > $root->prio) {
                $root = $this->rotateRight($root);
            }
        } else { // keys are unique, so key > root->key
            $root->right = $this->treapInsert($root->right, $key);
            if ($root->right !== null && $root->right->prio > $root->prio) {
                $root = $this->rotateLeft($root);
            }
        }
        return $root;
    }

    private function rotateRight(TreapNode $y): TreapNode {
        $x = $y->left;
        $T2 = $x->right;
        $x->right = $y;
        $y->left = $T2;
        return $x;
    }

    private function rotateLeft(TreapNode $x): TreapNode {
        $y = $x->right;
        $T2 = $y->left;
        $y->left = $x;
        $x->right = $T2;
        return $y;
    }

    // returns smallest key >= target, or null
    private function lowerBound(?TreapNode $root, int $target): ?int {
        $res = null;
        while ($root !== null) {
            if ($root->key >= $target) {
                $res = $root->key;
                $root = $root->left;
            } else {
                $root = $root->right;
            }
        }
        return $res;
    }

    // returns largest key < target, or null
    private function predecessor(?TreapNode $root, int $target): ?int {
        $res = null;
        while ($root !== null) {
            if ($root->key < $target) {
                $res = $root->key;
                $root = $root->right;
            } else {
                $root = $root->left;
            }
        }
        return $res;
    }
}
```

## Swift

```swift
import Foundation

private class Node {
    var key: Int
    var priority: UInt32
    var left: Node?
    var right: Node?
    init(_ key: Int) {
        self.key = key
        self.priority = arc4random()
    }
}

private func rotateRight(_ y: Node) -> Node {
    let x = y.left!
    y.left = x.right
    x.right = y
    return x
}

private func rotateLeft(_ x: Node) -> Node {
    let y = x.right!
    x.right = y.left
    y.left = x
    return y
}

private func insert(_ root: Node?, _ key: Int) -> Node {
    guard let node = root else { return Node(key) }
    if key < node.key {
        node.left = insert(node.left, key)
        if let left = node.left, left.priority < node.priority {
            return rotateRight(node)
        }
    } else {
        node.right = insert(node.right, key)
        if let right = node.right, right.priority < node.priority {
            return rotateLeft(node)
        }
    }
    return node
}

private func lowerBound(_ root: Node?, _ key: Int) -> Int? {
    var cur = root
    var ans: Int? = nil
    while let node = cur {
        if node.key >= key {
            ans = node.key
            cur = node.left
        } else {
            cur = node.right
        }
    }
    return ans
}

private func predecessor(_ root: Node?, _ key: Int) -> Int? {
    var cur = root
    var ans: Int? = nil
    while let node = cur {
        if node.key < key {
            ans = node.key
            cur = node.right
        } else {
            cur = node.left
        }
    }
    return ans
}

class Solution {
    func closestRoom(_ rooms: [[Int]], _ queries: [[Int]]) -> [Int] {
        let sortedRooms = rooms.sorted { $0[1] > $1[1] }   // descending size
        
        var qList: [(pref: Int, minSize: Int, idx: Int)] = []
        for (i, q) in queries.enumerated() {
            qList.append((pref: q[0], minSize: q[1], idx: i))
        }
        qList.sort { $0.minSize > $1.minSize }           // descending minSize
        
        var answers = Array(repeating: -1, count: queries.count)
        var root: Node? = nil
        var rIdx = 0
        
        for q in qList {
            while rIdx < sortedRooms.count && sortedRooms[rIdx][1] >= q.minSize {
                let roomId = sortedRooms[rIdx][0]
                root = insert(root, roomId)
                rIdx += 1
            }
            
            guard let treeRoot = root else {
                answers[q.idx] = -1
                continue
            }
            
            let pref = q.pref
            let lower = lowerBound(treeRoot, pref)      // smallest >= pref
            let pred = predecessor(treeRoot, pref)     // largest < pref
            
            var best: Int? = nil
            if let l = lower { best = l }
            if let p = pred {
                if let b = best {
                    let diffL = abs(b - pref)
                    let diffP = abs(p - pref)
                    if diffP < diffL || (diffP == diffL && p < b) {
                        best = p
                    }
                } else {
                    best = p
                }
            }
            
            answers[q.idx] = best ?? -1
        }
        
        return answers
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun closestRoom(rooms: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val sortedRooms = rooms.sortedByDescending { it[1] }
        data class Query(val pref: Int, val minSize: Int, val idx: Int)
        val qList = ArrayList<Query>(queries.size)
        for (i in queries.indices) {
            qList.add(Query(queries[i][0], queries[i][1], i))
        }
        qList.sortByDescending { it.minSize }

        val ids = java.util.TreeSet<Int>()
        var rIdx = 0
        val ans = IntArray(queries.size) { -1 }

        for (q in qList) {
            while (rIdx < sortedRooms.size && sortedRooms[rIdx][1] >= q.minSize) {
                ids.add(sortedRooms[rIdx][0])
                rIdx++
            }
            if (ids.isEmpty()) {
                ans[q.idx] = -1
                continue
            }

            var bestId = -1
            var bestDiff = Long.MAX_VALUE
            val pref = q.pref

            val floor = ids.floor(pref)
            if (floor != null) {
                val diff = kotlin.math.abs(floor - pref).toLong()
                if (diff < bestDiff || (diff == bestDiff && floor < bestId)) {
                    bestDiff = diff
                    bestId = floor
                }
            }

            val ceil = ids.ceiling(pref)
            if (ceil != null) {
                val diff = kotlin.math.abs(ceil - pref).toLong()
                if (diff < bestDiff || (diff == bestDiff && ceil < bestId)) {
                    bestDiff = diff
                    bestId = ceil
                }
            }

            ans[q.idx] = bestId
        }

        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class _TreapNode {
  int key;
  int priority;
  _TreapNode? left, right;
  _TreapNode(this.key) : priority = Random().nextInt(1 << 30);
}

class _Treap {
  _TreapNode? _root;

  void insert(int key) {
    _root = _insert(_root, _TreapNode(key));
  }

  int? predecessor(int key) {
    var cur = _root;
    int? pred;
    while (cur != null) {
      if (cur.key <= key) {
        pred = cur.key;
        cur = cur.right;
      } else {
        cur = cur.left;
      }
    }
    return pred;
  }

  int? successor(int key) {
    var cur = _root;
    int? succ;
    while (cur != null) {
      if (cur.key >= key) {
        succ = cur.key;
        cur = cur.left;
      } else {
        cur = cur.right;
      }
    }
    return succ;
  }

  bool get isEmpty => _root == null;

  _TreapNode _rotateRight(_TreapNode y) {
    var x = y.left!;
    y.left = x.right;
    x.right = y;
    return x;
  }

  _TreapNode _rotateLeft(_TreapNode x) {
    var y = x.right!;
    x.right = y.left;
    y.left = x;
    return y;
  }

  _TreapNode _insert(_TreapNode? root, _TreapNode node) {
    if (root == null) return node;
    if (node.key < root.key) {
      root.left = _insert(root.left, node);
      if ((root.left?.priority ?? -1) > root.priority) {
        root = _rotateRight(root);
      }
    } else {
      root.right = _insert(root.right, node);
      if ((root.right?.priority ?? -1) > root.priority) {
        root = _rotateLeft(root);
      }
    }
    return root;
  }
}

class Solution {
  List<int> closestRoom(List<List<int>> rooms, List<List<int>> queries) {
    // Sort rooms by size descending
    rooms.sort((a, b) => b[1].compareTo(a[1]));

    // Prepare queries with original indices and sort by minSize descending
    int q = queries.length;
    var indexedQueries = List.generate(q, (i) => [queries[i][0], queries[i][1], i]);
    indexedQueries.sort((a, b) => b[1].compareTo(a[1]));

    var treap = _Treap();
    List<int> ans = List.filled(q, -1);
    int ri = 0;
    for (var query in indexedQueries) {
      int pref = query[0];
      int minSize = query[1];
      int idx = query[2];

      // Insert all rooms with size >= minSize
      while (ri < rooms.length && rooms[ri][1] >= minSize) {
        treap.insert(rooms[ri][0]);
        ri++;
      }

      if (treap.isEmpty) {
        ans[idx] = -1;
        continue;
      }

      int? low = treap.predecessor(pref);
      int? high = treap.successor(pref);

      int best;
      if (low == null) {
        best = high!;
      } else if (high == null) {
        best = low;
      } else {
        int dLow = (pref - low).abs();
        int dHigh = (high - pref).abs();
        if (dLow < dHigh) {
          best = low;
        } else if (dHigh < dLow) {
          best = high;
        } else {
          best = min(low, high);
        }
      }
      ans[idx] = best;
    }

    return ans;
  }
}
```

## Golang

```go
package main

import (
	"math/rand"
	"sort"
	"time"
)

type treapNode struct {
	key        int
	priority   uint32
	left, right *treapNode
}

func split(root *treapNode, key int) (*treapNode, *treapNode) {
	if root == nil {
		return nil, nil
	}
	if key <= root.key {
		l, r := split(root.left, key)
		root.left = r
		return l, root
	}
	l, r := split(root.right, key)
	root.right = l
	return root, r
}

func merge(a, b *treapNode) *treapNode {
	if a == nil {
		return b
	}
	if b == nil {
		return a
	}
	if a.priority < b.priority {
		a.right = merge(a.right, b)
		return a
	}
	b.left = merge(a, b.left)
	return b
}

func insert(root *treapNode, key int) *treapNode {
	newNode := &treapNode{key: key, priority: rand.Uint32()}
	l, r := split(root, key)
	return merge(merge(l, newNode), r)
}

func lowerBound(root *treapNode, key int) (int, bool) {
	found := false
	ans := 0
	for root != nil {
		if root.key >= key {
			found = true
			ans = root.key
			root = root.left
		} else {
			root = root.right
		}
	}
	return ans, found
}

func predecessor(root *treapNode, key int) (int, bool) {
	found := false
	ans := 0
	for root != nil {
		if root.key < key {
			found = true
			ans = root.key
			root = root.right
		} else {
			root = root.left
		}
	}
	return ans, found
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

type room struct {
	size int
	id   int
}

type query struct {
	pref    int
	minSize int
	idx     int
}

func closestRoom(rooms [][]int, queries [][]int) []int {
	rand.Seed(time.Now().UnixNano())

	n := len(rooms)
	roomList := make([]room, n)
	for i, v := range rooms {
		roomList[i] = room{size: v[1], id: v[0]}
	}
	sort.Slice(roomList, func(i, j int) bool {
		return roomList[i].size > roomList[j].size
	})

	m := len(queries)
	queryList := make([]query, m)
	for i, v := range queries {
		queryList[i] = query{pref: v[0], minSize: v[1], idx: i}
	}
	sort.Slice(queryList, func(i, j int) bool {
		return queryList[i].minSize > queryList[j].minSize
	})

	ans := make([]int, m)
	var root *treapNode
	pos := 0

	for _, q := range queryList {
		for pos < n && roomList[pos].size >= q.minSize {
			root = insert(root, roomList[pos].id)
			pos++
		}
		best := -1
		bestDiff := int(^uint(0) >> 1) // max int

		if root != nil {
			if v, ok := lowerBound(root, q.pref); ok {
				d := abs(v - q.pref)
				if d < bestDiff || (d == bestDiff && v < best) {
					best = v
					bestDiff = d
				}
			}
			if v, ok := predecessor(root, q.pref); ok {
				d := abs(v - q.pref)
				if d < bestDiff || (d == bestDiff && v < best) {
					best = v
					bestDiff = d
				}
			}
		}
		ans[q.idx] = best
	}

	return ans
}
```

## Ruby

```ruby
class Treap
  Node = Struct.new(:key, :prio, :left, :right)

  def initialize
    @root = nil
  end

  def empty?
    @root.nil?
  end

  def insert(key)
    @root = _insert(@root, key)
  end

  def lower_bound(x)
    node = @root
    res = nil
    while node
      if node.key >= x
        res = node.key
        node = node.left
      else
        node = node.right
      end
    end
    res
  end

  def predecessor(x)
    node = @root
    res = nil
    while node
      if node.key < x
        res = node.key
        node = node.right
      else
        node = node.left
      end
    end
    res
  end

  private

  def _insert(node, key)
    return Node.new(key, rand(1 << 30), nil, nil) if node.nil?
    if key < node.key
      node.left = _insert(node.left, key)
      node = rotate_right(node) if node.left.prio > node.prio
    elsif key > node.key
      node.right = _insert(node.right, key)
      node = rotate_left(node) if node.right.prio > node.prio
    end
    node
  end

  def rotate_right(y)
    x = y.left
    y.left = x.right
    x.right = y
    x
  end

  def rotate_left(x)
    y = x.right
    x.right = y.left
    y.left = x
    y
  end
end

def closest_room(rooms, queries)
  rooms_sorted = rooms.sort_by { |id, size| -size }
  q_with_idx = queries.each_with_index.map { |(pref, minSize), idx| [minSize, pref, idx] }
  q_with_idx.sort_by! { |minSize, _, _| -minSize }

  treap = Treap.new
  ans = Array.new(queries.size)
  i = 0
  n = rooms_sorted.length

  q_with_idx.each do |minSize, pref, idx|
    while i < n && rooms_sorted[i][1] >= minSize
      treap.insert(rooms_sorted[i][0])
      i += 1
    end

    if treap.empty?
      ans[idx] = -1
      next
    end

    succ = treap.lower_bound(pref)
    pred = treap.predecessor(pref)

    best_id = nil
    best_diff = Float::INFINITY

    if succ
      diff = (succ - pref).abs
      best_id = succ
      best_diff = diff
    end
    if pred
      diff = (pref - pred).abs
      if diff < best_diff || (diff == best_diff && pred < best_id)
        best_id = pred
        best_diff = diff
      end
    end

    ans[idx] = best_id ? best_id : -1
  end

  ans
end
```

## Scala

```scala
object Solution {
  import java.util.TreeSet

  case class Query(pref: Int, minSize: Int, idx: Int)

  def closestRoom(rooms: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    // Sort rooms by size descending
    val sortedRooms = rooms.sortWith((a, b) => a(1) > b(1))

    // Prepare queries with original indices and sort by minSize descending
    val qs = (0 until queries.length).map { i =>
      Query(queries(i)(0), queries(i)(1), i)
    }.toArray
    val sortedQueries = qs.sortWith((a, b) => a.minSize > b.minSize)

    val set = new TreeSet[Int]()
    val ans = new Array[Int](queries.length)

    var rIdx = 0
    val n = sortedRooms.length

    for (q <- sortedQueries) {
      while (rIdx < n && sortedRooms(rIdx)(1) >= q.minSize) {
        set.add(sortedRooms(rIdx)(0))
        rIdx += 1
      }

      if (set.isEmpty) {
        ans(q.idx) = -1
      } else {
        val pref = q.pref
        var best = -1
        var bestDiff = Long.MaxValue

        val floorObj = set.floor(pref)
        if (floorObj != null) {
          val diff = Math.abs(floorObj - pref).toLong
          if (diff < bestDiff || (diff == bestDiff && floorObj < best)) {
            best = floorObj
            bestDiff = diff
          }
        }

        val ceilObj = set.ceiling(pref)
        if (ceilObj != null) {
          val diff = Math.abs(ceilObj - pref).toLong
          if (diff < bestDiff || (diff == bestDiff && ceilObj < best)) {
            best = ceilObj
            bestDiff = diff
          }
        }

        ans(q.idx) = best
      }
    }

    ans
  }
}
```

## Rust

```rust
use std::collections::BTreeSet;

impl Solution {
    pub fn closest_room(rooms: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        // rooms as (size, id) and sort descending by size
        let mut rooms_vec: Vec<(i32, i32)> = rooms.into_iter().map(|v| (v[1], v[0])).collect();
        rooms_vec.sort_by(|a, b| b.0.cmp(&a.0));

        // queries with original index, sort descending by minSize
        #[derive(Clone)]
        struct Q {
            pref: i32,
            min_size: i32,
            idx: usize,
        }
        let mut qs: Vec<Q> = queries
            .into_iter()
            .enumerate()
            .map(|(i, q)| Q {
                pref: q[0],
                min_size: q[1],
                idx: i,
            })
            .collect();
        qs.sort_by(|a, b| b.min_size.cmp(&a.min_size));

        let mut set: BTreeSet<i32> = BTreeSet::new();
        let mut ans = vec![-1; qs.len()];
        let mut r_idx = 0usize;

        for q in qs {
            while r_idx < rooms_vec.len() && rooms_vec[r_idx].0 >= q.min_size {
                set.insert(rooms_vec[r_idx].1);
                r_idx += 1;
            }

            if set.is_empty() {
                ans[q.idx] = -1;
                continue;
            }

            let pref = q.pref;

            // successor (>= pref)
            let succ_opt = set.range(pref..).next().cloned();
            // predecessor (< pref)
            let pred_opt = set.range(..pref).next_back().cloned();

            let mut best: i32 = -1;
            if let Some(s) = succ_opt {
                best = s;
            }
            if let Some(p) = pred_opt {
                if best == -1 {
                    best = p;
                } else {
                    let diff_s = (best - pref).abs();
                    let diff_p = (pref - p).abs();
                    if diff_p < diff_s || (diff_p == diff_s && p < best) {
                        best = p;
                    }
                }
            }

            ans[q.idx] = best;
        }

        ans
    }
}
```

## Racket

```racket
(require racket/list)

(struct node (key priority left right) #:mutable)

(define (make-node key)
  (node key (random) #f #f))

(define (rotate-right y)
  (let* ([x (node-left y)]
         [t2 (node-right x)])
    (set-node-right! x y)
    (set-node-left! y t2)
    x))

(define (rotate-left x)
  (let* ([y (node-right x)]
         [t2 (node-left y)])
    (set-node-left! y x)
    (set-node-right! x t2)
    y))

(define (insert root key)
  (cond
    [(not root) (make-node key)]
    [else
     (let ([k (node-key root)])
       (cond
         [(= k key) root]
         [(< key k)
          (set-node-left! root (insert (node-left root) key))
          (if (> (node-priority (node-left root)) (node-priority root))
              (rotate-right root)
              root)]
         [else
          (set-node-right! root (insert (node-right root) key))
          (if (> (node-priority (node-right root)) (node-priority root))
              (rotate-left root)
              root)]))]))

(define (predecessor root x)
  (let loop ([node root] [best #f])
    (cond
      [(not node) best]
      [(<= (node-key node) x)
       (loop (node-right node) (node-key node))]
      [else
       (loop (node-left node) best)])))

(define (successor root x)
  (let loop ([node root] [best #f])
    (cond
      [(not node) best]
      [(>= (node-key node) x)
       (loop (node-left node) (node-key node))]
      [else
       (loop (node-right node) best)])))

(define (closest-room rooms queries)
  (let* ([sorted-rooms (sort rooms (lambda (a b) (> (cadr a) (cadr b))))]
         [rooms-vec (list->vector sorted-rooms)]
         [indexed-queries
          (for/list ([q queries] [idx (in-naturals)])
            (list (first q) (second q) idx))]
         [sorted-queries (sort indexed-queries (lambda (a b) (> (cadr a) (cadr b))))]
         [n (vector-length rooms-vec)]
         [m (length queries)]
         [answers (make-vector m -1)])
    (define root #f)
    (define room-idx 0)
    (for ([q sorted-queries])
      (define pref (first q))
      (define minSize (second q))
      (define out-idx (list-ref q 2))
      ;; add eligible rooms
      (let loop ()
        (when (< room-idx n)
          (define cur-room (vector-ref rooms-vec room-idx))
          (when (>= (cadr cur-room) minSize)
            (set! root (insert root (car cur-room)))
            (set! room-idx (+ room-idx 1))
            (loop))))
      ;; find closest id
      (define pred (predecessor root pref))
      (define succ (successor root pref))
      (cond
        [(and (not pred) (not succ))
         (vector-set! answers out-idx -1)]
        [(and pred (not succ))
         (vector-set! answers out-idx pred)]
        [(and succ (not pred))
         (vector-set! answers out-idx succ)]
        [else
         (define diff-pred (abs (- pref pred)))
         (define diff-succ (abs (- succ pref)))
         (cond
           [(< diff-pred diff-succ) (vector-set! answers out-idx pred)]
           [(> diff-pred diff-succ) (vector-set! answers out-idx succ)]
           [else (vector-set! answers out-idx (min pred succ))])])))
    (vector->list answers)))
```

## Erlang

```erlang
-spec closest_room(Rooms :: [[integer()]], Queries :: [[integer()]]) -> [integer()].
closest_room(Rooms, Queries) ->
    RoomsTuples = [{RId, Sz} || [RId, Sz] <- Rooms],
    SortedRooms = lists:reverse(lists:keysort(2, RoomsTuples)),
    Indices = lists:seq(0, length(Queries) - 1),
    QueriesWithIdx = [
        begin
            [Pref, Min] = Q,
            {Min, Pref, Idx}
        end || {Q, Idx} <- lists:zip(Queries, Indices)
    ],
    SortedQueries = lists:reverse(lists:keysort(1, QueriesWithIdx)),
    Results = process_queries(SortedQueries, SortedRooms, gb_trees:empty(), []),
    SortedResults = lists:keysort(1, Results),
    [Ans || {_Idx, Ans} <- SortedResults].

process_queries([], _RoomsRem, _Tree, Acc) ->
    Acc;
process_queries([{MinSize, Preferred, Idx} | Rest], RoomsRem, Tree, Acc) ->
    {NewTree, NewRoomsRem} = add_rooms(RoomsRem, MinSize, Tree),
    Answer = find_closest(NewTree, Preferred),
    process_queries(Rest, NewRoomsRem, NewTree, [{Idx, Answer} | Acc]).

add_rooms([], _MinSize, Tree) ->
    {Tree, []};
add_rooms([{RoomId, Size} = H | T], MinSize, Tree) when Size >= MinSize ->
    NewTree = gb_trees:insert(RoomId, true, Tree),
    add_rooms(T, MinSize, NewTree);
add_rooms(Rest, _MinSize, Tree) ->
    {Tree, Rest}.

find_closest(Tree, Preferred) ->
    case gb_trees:is_empty(Tree) of
        true -> -1;
        false ->
            It = gb_trees:iterator_from(Preferred, Tree),
            Succ = case gb_trees:next(It) of
                none -> undefined;
                {SuccId, _, _} -> SuccId
            end,
            Pred = case gb_trees:prev(It) of
                none -> undefined;
                {PredId, _, _} -> PredId
            end,
            choose_best(Pred, Succ, Preferred)
    end.

choose_best(undefined, undefined, _) ->
    -1;
choose_best(Pred, undefined, _) when Pred =/= undefined ->
    Pred;
choose_best(undefined, Succ, _) when Succ =/= undefined ->
    Succ;
choose_best(Pred, Succ, Pref) ->
    DiffP = erlang:abs(Pred - Pref),
    DiffS = erlang:abs(Succ - Pref),
    if
        DiffP < DiffS -> Pred;
        DiffS < DiffP -> Succ;
        true -> % equal distance, choose smaller id
            if Pred =< Succ -> Pred; true -> Succ end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec closest_room(rooms :: [[integer]], queries :: [[integer]]) :: [integer]
  def closest_room(rooms, queries) do
    rooms_sorted = Enum.sort_by(rooms, fn [_id, size] -> -size end)

    queries_with_idx =
      queries
      |> Enum.with_index()
      |> Enum.map(fn {[pref, min], idx} ->
        %{pref: pref, min: min, idx: idx}
      end)
      |> Enum.sort_by(& &1.min, :desc)

    {answers_map, _tree, _room_idx} =
      Enum.reduce(queries_with_idx, {%{}, :gb_trees.empty(), 0}, fn q,
                                                                   {ans_map, cur_tree,
                                                                    r_idx} ->
        {new_tree, new_r_idx} = add_rooms(q.min, rooms_sorted, r_idx, cur_tree)
        best = find_best(new_tree, q.pref)
        {Map.put(ans_map, q.idx, best), new_tree, new_r_idx}
      end)

    k = length(queries)

    Enum.map(0..k - 1, fn i -> Map.get(answers_map, i) end)
  end

  defp add_rooms(min_size, rooms_sorted, r_idx, tree) do
    total = length(rooms_sorted)

    if r_idx < total do
      [id, size] = Enum.at(rooms_sorted, r_idx)

      if size >= min_size do
        new_tree = :gb_trees.insert(id, true, tree)
        add_rooms(min_size, rooms_sorted, r_idx + 1, new_tree)
      else
        {tree, r_idx}
      end
    else
      {tree, r_idx}
    end
  end

  defp find_best(tree, pref) do
    if :gb_trees.is_empty(tree) do
      -1
    else
      floor =
        case :gb_trees.prev(pref, tree) do
          :none -> nil
          {k, _v} -> k
        end

      ceil =
        case :gb_trees.next(:gb_trees.iterator_from(pref, tree)) do
          :none -> nil
          {k, _, _} -> k
        end

      cond do
        floor == nil and ceil == nil ->
          -1

        floor == nil ->
          ceil

        ceil == nil ->
          floor

        true ->
          diff_floor = abs(floor - pref)
          diff_ceil = abs(ceil - pref)

          cond do
            diff_floor < diff_ceil -> floor
            diff_floor > diff_ceil -> ceil
            true -> min(floor, ceil)
          end
      end
    end
  end
end
```
