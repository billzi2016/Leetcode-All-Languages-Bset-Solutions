# 3508. Implement Router

## Cpp

```cpp
class Router {
public:
    struct Packet {
        int source;
        int destination;
        int timestamp;
    };
    
    struct TripleHash {
        size_t operator()(const std::array<int,3>& a) const noexcept {
            uint64_t h = (static_cast<uint64_t>(a[0]) << 42) ^
                         (static_cast<uint64_t>(a[1]) << 21) ^
                         static_cast<uint64_t>(a[2]);
            return std::hash<uint64_t>{}(h);
        }
    };
    
    Router(int memoryLimit) : limit(memoryLimit) {}
    
    bool addPacket(int source, int destination, int timestamp) {
        std::array<int,3> key{source, destination, timestamp};
        if (exist.find(key) != exist.end()) return false;
        
        if ((int)queue.size() == limit) {
            // evict oldest
            const Packet &old = queue.front();
            std::array<int,3> oldKey{old.source, old.destination, old.timestamp};
            exist.erase(oldKey);
            auto itMap = destMap.find(old.destination);
            if (itMap != destMap.end()) {
                auto &ms = itMap->second;
                auto itMs = ms.find(old.timestamp);
                if (itMs != ms.end()) ms.erase(itMs);
                if (ms.empty()) destMap.erase(itMap);
            }
            queue.pop_front();
        }
        
        Packet p{source, destination, timestamp};
        queue.push_back(p);
        exist.insert(key);
        destMap[destination].insert(timestamp);
        return true;
    }
    
    std::vector<int> forwardPacket() {
        if (queue.empty()) return {};
        const Packet &p = queue.front();
        std::array<int,3> key{p.source, p.destination, p.timestamp};
        exist.erase(key);
        auto itMap = destMap.find(p.destination);
        if (itMap != destMap.end()) {
            auto &ms = itMap->second;
            auto itMs = ms.find(p.timestamp);
            if (itMs != ms.end()) ms.erase(itMs);
            if (ms.empty()) destMap.erase(itMap);
        }
        std::vector<int> res{p.source, p.destination, p.timestamp};
        queue.pop_front();
        return res;
    }
    
    int getCount(int destination, int startTime, int endTime) {
        auto it = destMap.find(destination);
        if (it == destMap.end()) return 0;
        const std::multiset<int> &ms = it->second;
        auto lo = ms.lower_bound(startTime);
        auto hi = ms.upper_bound(endTime);
        return static_cast<int>(std::distance(lo, hi));
    }
    
private:
    int limit;
    std::deque<Packet> queue;
    std::unordered_set<std::array<int,3>, TripleHash> exist;
    std::unordered_map<int, std::multiset<int>> destMap;
};

/**
 * Your Router object will be instantiated and called as such:
 * Router* obj = new Router(memoryLimit);
 * bool param_1 = obj->addPacket(source,destination,timestamp);
 * vector<int> param_2 = obj->forwardPacket();
 * int param_3 = obj->getCount(destination,startTime,endTime);
 */
```

## Java

```java
class Router {
    private static class Packet {
        int source;
        int destination;
        int timestamp;
        Packet(int s, int d, int t) {
            this.source = s;
            this.destination = d;
            this.timestamp = t;
        }
    }

    private final int capacity;
    private final java.util.ArrayDeque<Packet> queue;
    private final java.util.HashSet<Long> set;
    private final java.util.HashMap<Integer, java.util.TreeMap<Integer, Integer>> destMap;

    public Router(int memoryLimit) {
        this.capacity = memoryLimit;
        this.queue = new java.util.ArrayDeque<>();
        this.set = new java.util.HashSet<>();
        this.destMap = new java.util.HashMap<>();
    }

    private long encode(int source, int destination, int timestamp) {
        return ((long) source << 50) | ((long) destination << 30) | (long) timestamp;
    }

    public boolean addPacket(int source, int destination, int timestamp) {
        long key = encode(source, destination, timestamp);
        if (set.contains(key)) {
            return false;
        }
        // Evict oldest if at capacity
        if (queue.size() == capacity) {
            Packet old = queue.pollFirst();
            long oldKey = encode(old.source, old.destination, old.timestamp);
            set.remove(oldKey);
            java.util.TreeMap<Integer, Integer> tm = destMap.get(old.destination);
            int cnt = tm.get(old.timestamp);
            if (cnt == 1) {
                tm.remove(old.timestamp);
            } else {
                tm.put(old.timestamp, cnt - 1);
            }
            if (tm.isEmpty()) {
                destMap.remove(old.destination);
            }
        }
        // Add new packet
        Packet p = new Packet(source, destination, timestamp);
        queue.offerLast(p);
        set.add(key);
        java.util.TreeMap<Integer, Integer> tm = destMap.computeIfAbsent(destination, k -> new java.util.TreeMap<>());
        tm.put(timestamp, tm.getOrDefault(timestamp, 0) + 1);
        return true;
    }

    public int[] forwardPacket() {
        if (queue.isEmpty()) {
            return new int[0];
        }
        Packet p = queue.pollFirst();
        long key = encode(p.source, p.destination, p.timestamp);
        set.remove(key);
        java.util.TreeMap<Integer, Integer> tm = destMap.get(p.destination);
        int cnt = tm.get(p.timestamp);
        if (cnt == 1) {
            tm.remove(p.timestamp);
        } else {
            tm.put(p.timestamp, cnt - 1);
        }
        if (tm.isEmpty()) {
            destMap.remove(p.destination);
        }
        return new int[]{p.source, p.destination, p.timestamp};
    }

    public int getCount(int destination, int startTime, int endTime) {
        java.util.TreeMap<Integer, Integer> tm = destMap.get(destination);
        if (tm == null) {
            return 0;
        }
        java.util.NavigableMap<Integer, Integer> sub = tm.subMap(startTime, true, endTime, true);
        int sum = 0;
        for (int v : sub.values()) {
            sum += v;
        }
        return sum;
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * Router obj = new Router(memoryLimit);
 * boolean param_1 = obj.addPacket(source,destination,timestamp);
 * int[] param_2 = obj.forwardPacket();
 * int param_3 = obj.getCount(destination,startTime,endTime);
 */
```

## Python

```python
import bisect
from collections import deque, defaultdict

class Router(object):
    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.limit = memoryLimit
        self.q = deque()                     # store (source, destination, timestamp)
        self.exist = set()                   # set of packets for duplicate check
        self.dest_map = defaultdict(list)    # destination -> sorted list of timestamps

    def _remove_packet(self, packet):
        src, dst, ts = packet
        self.exist.remove(packet)
        lst = self.dest_map[dst]
        idx = bisect.bisect_left(lst, ts)
        # remove one occurrence
        lst.pop(idx)
        if not lst:
            del self.dest_map[dst]

    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        pkt = (source, destination, timestamp)
        if pkt in self.exist:
            return False

        if len(self.q) == self.limit:
            oldest = self.q.popleft()
            self._remove_packet(oldest)

        self.q.append(pkt)
        self.exist.add(pkt)
        bisect.insort(self.dest_map[destination], timestamp)
        return True

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if not self.q:
            return []
        pkt = self.q.popleft()
        self._remove_packet(pkt)
        return [pkt[0], pkt[1], pkt[2]]

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        lst = self.dest_map.get(destination)
        if not lst:
            return 0
        left = bisect.bisect_left(lst, startTime)
        right = bisect.bisect_right(lst, endTime)
        return right - left
```

## Python3

```python
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque()                     # stores (source, destination, timestamp)
        self.packets = set()                     # set of tuples for duplicate detection
        self.dest_ts = defaultdict(list)         # destination -> list of timestamps (in insertion order)
        self.start_idx = defaultdict(int)        # destination -> index of first valid timestamp in dest_ts[d]

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.packets:
            return False

        if len(self.queue) == self.limit:
            old_source, old_dest, old_ts = self.queue.popleft()
            old_key = (old_source, old_dest, old_ts)
            self.packets.remove(old_key)
            # logically remove the oldest timestamp for that destination
            self.start_idx[old_dest] += 1

        self.queue.append((source, destination, timestamp))
        self.packets.add(key)
        self.dest_ts[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        src, dst, ts = self.queue.popleft()
        key = (src, dst, ts)
        self.packets.remove(key)
        self.start_idx[dst] += 1
        return [src, dst, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.dest_ts.get(destination, [])
        if not timestamps:
            return 0

        left = bisect_left(timestamps, startTime)
        right = bisect_right(timestamps, endTime)

        start = self.start_idx.get(destination, 0)
        # adjust bounds to ignore evicted prefix
        left = max(left, start)
        right = min(right, len(timestamps))
        return max(0, right - left)
```

## C

```c
#include <stdlib.h>
#include <stdint.h>

typedef struct {
    int source;
    int destination;
    int timestamp;
} Packet;

/* Treap node for multiset of timestamps */
typedef struct TreapNode {
    int key;                /* timestamp */
    int cnt;                /* multiplicity of this key */
    int size;               /* total count in subtree (including multiplicities) */
    unsigned priority;
    struct TreapNode *left, *right;
} TreapNode;

/* Router structure */
typedef struct {
    int capacity;
    int size;
    Packet *buf;
    int head, tail;

    /* hash set for existence check */
    uint64_t *hs_keys;
    char *hs_state;         /* 0 = empty, 1 = occupied, 2 = deleted */
    int hs_mask;            /* tableSize-1, tableSize is power of two */

    TreapNode **destRoots;  /* array indexed by destination (max 200000) */
} Router;

/* ---------- treap utilities ---------- */
static int nodeSize(TreapNode *n) { return n ? n->size : 0; }

static void update(TreapNode *n) {
    if (n) n->size = n->cnt + nodeSize(n->left) + nodeSize(n->right);
}

static TreapNode* newNode(int key) {
    TreapNode *n = (TreapNode*)malloc(sizeof(TreapNode));
    n->key = key;
    n->cnt = 1;
    n->size = 1;
    n->priority = ((unsigned)rand() << 16) ^ (unsigned)rand();
    n->left = n->right = NULL;
    return n;
}

/* rotate right */
static TreapNode* rotateRight(TreapNode *y) {
    TreapNode *x = y->left;
    y->left = x->right;
    x->right = y;
    update(y);
    update(x);
    return x;
}

/* rotate left */
static TreapNode* rotateLeft(TreapNode *x) {
    TreapNode *y = x->right;
    x->right = y->left;
    y->left = x;
    update(x);
    update(y);
    return y;
}

static TreapNode* treapInsert(TreapNode *root, int key) {
    if (!root) return newNode(key);
    if (key == root->key) {
        root->cnt++;
    } else if (key < root->key) {
        root->left = treapInsert(root->left, key);
        if (root->left->priority > root->priority)
            root = rotateRight(root);
    } else {
        root->right = treapInsert(root->right, key);
        if (root->right->priority > root->priority)
            root = rotateLeft(root);
    }
    update(root);
    return root;
}

/* erase one occurrence of key */
static TreapNode* treapErase(TreapNode *root, int key) {
    if (!root) return NULL;
    if (key == root->key) {
        if (root->cnt > 1) {
            root->cnt--;
        } else {
            /* remove node */
            if (!root->left && !root->right) {
                free(root);
                return NULL;
            } else if (!root->right || (root->left && root->left->priority > root->right->priority)) {
                root = rotateRight(root);
                root->right = treapErase(root->right, key);
            } else {
                root = rotateLeft(root);
                root->left = treapErase(root->left, key);
            }
        }
    } else if (key < root->key) {
        root->left = treapErase(root->left, key);
    } else {
        root->right = treapErase(root->right, key);
    }
    update(root);
    return root;
}

/* count of keys <= val */
static int treapCountLE(TreapNode *root, int val) {
    if (!root) return 0;
    if (val < root->key) {
        return treapCountLE(root->left, val);
    } else {
        return nodeSize(root->left) + root->cnt + treapCountLE(root->right, val);
    }
}

/* free whole treap */
static void freeTreap(TreapNode *root) {
    if (!root) return;
    freeTreap(root->left);
    freeTreap(root->right);
    free(root);
}

/* ---------- hash set utilities ---------- */
static int hs_nextPowerOfTwo(int n) {
    int p = 1;
    while (p < n) p <<= 1;
    return p;
}

static Router* routerCreate(int memoryLimit) {
    Router *obj = (Router*)malloc(sizeof(Router));
    obj->capacity = memoryLimit;
    obj->size = 0;
    obj->buf = (Packet*)malloc(sizeof(Packet) * memoryLimit);
    obj->head = obj->tail = 0;

    int hsSize = hs_nextPowerOfTwo(memoryLimit * 4 + 1);
    obj->hs_mask = hsSize - 1;
    obj->hs_keys = (uint64_t*)calloc(hsSize, sizeof(uint64_t));
    obj->hs_state = (char*)calloc(hsSize, sizeof(char)); /* all zero */

    const int MAX_DEST = 200000;
    obj->destRoots = (TreapNode**)calloc(MAX_DEST + 1, sizeof(TreapNode*));

    return obj;
}

/* combine attributes into a unique 64‑bit key */
static inline uint64_t packKey(int source, int destination, int timestamp) {
    return ((uint64_t)(uint32_t)source << 48) |
           ((uint64_t)(uint32_t)destination << 32) |
           (uint64_t)(uint32_t)timestamp;
}

/* find index of key or -1 if not present */
static int hs_find(Router *obj, uint64_t key) {
    int mask = obj->hs_mask;
    int idx = (int)(key & mask);
    while (obj->hs_state[idx]) {
        if (obj->hs_state[idx] == 1 && obj->hs_keys[idx] == key)
            return idx;
        idx = (idx + 1) & mask;
    }
    return -1;
}

/* insert key, return false if already exists */
static bool hs_insert(Router *obj, uint64_t key) {
    int mask = obj->hs_mask;
    int idx = (int)(key & mask);
    while (obj->hs_state[idx] == 1) {
        if (obj->hs_keys[idx] == key)
            return false;               /* already present */
        idx = (idx + 1) & mask;
    }
    /* empty or deleted slot */
    obj->hs_keys[idx] = key;
    obj->hs_state[idx] = 1;
    return true;
}

/* erase key, assumes it exists */
static void hs_erase(Router *obj, uint64_t key) {
    int idx = hs_find(obj, key);
    if (idx >= 0)
        obj->hs_state[idx] = 2;   /* mark as deleted */
}

/* ---------- Router operations ---------- */
bool routerAddPacket(Router* obj, int source, int destination, int timestamp) {
    uint64_t key = packKey(source, destination, timestamp);
    if (!hs_insert(obj, key))
        return false;                     /* duplicate */

    /* evict if full */
    if (obj->size == obj->capacity) {
        Packet old = obj->buf[obj->head];
        uint64_t oldKey = packKey(old.source, old.destination, old.timestamp);
        hs_erase(obj, oldKey);
        obj->destRoots[old.destination] = treapErase(obj->destRoots[old.destination], old.timestamp);
        obj->head = (obj->head + 1) % obj->capacity;
        obj->size--;
    }

    /* insert new packet */
    obj->buf[obj->tail].source = source;
    obj->buf[obj->tail].destination = destination;
    obj->buf[obj->tail].timestamp = timestamp;
    obj->tail = (obj->tail + 1) % obj->capacity;
    obj->size++;

    obj->destRoots[destination] = treapInsert(obj->destRoots[destination], timestamp);
    return true;
}

int* routerForwardPacket(Router* obj, int* retSize) {
    if (obj->size == 0) {
        *retSize = 0;
        return NULL;
    }
    Packet pkt = obj->buf[obj->head];
    obj->head = (obj->head + 1) % obj->capacity;
    obj->size--;

    uint64_t key = packKey(pkt.source, pkt.destination, pkt.timestamp);
    hs_erase(obj, key);
    obj->destRoots[pkt.destination] = treapErase(obj->destRoots[pkt.destination], pkt.timestamp);

    int *ans = (int*)malloc(3 * sizeof(int));
    ans[0] = pkt.source;
    ans[1] = pkt.destination;
    ans[2] = pkt.timestamp;
    *retSize = 3;
    return ans;
}

int routerGetCount(Router* obj, int destination, int startTime, int endTime) {
    if (destination < 0 || destination > 200000)
        return 0;
    TreapNode *root = obj->destRoots[destination];
    if (!root) return 0;
    int cntEnd = treapCountLE(root, endTime);
    int cntStartMinus1 = treapCountLE(root, startTime - 1);
    return cntEnd - cntStartMinus1;
}

void routerFree(Router* obj) {
    if (!obj) return;
    free(obj->buf);
    free(obj->hs_keys);
    free(obj->hs_state);
    for (int i = 0; i <= 200000; ++i) {
        if (obj->destRoots[i])
            freeTreap(obj->destRoots[i]);
    }
    free(obj->destRoots);
    free(obj);
}

/* The struct and functions are ready to be used by LeetCode. */
```

## Csharp

```csharp
public class Router
{
    private readonly int _capacity;
    private readonly Queue<Packet> _queue;
    private readonly HashSet<(int source, int dest, int time)> _set;
    private readonly Dictionary<int, DestInfo> _destMap;

    public Router(int memoryLimit)
    {
        _capacity = memoryLimit;
        _queue = new Queue<Packet>();
        _set = new HashSet<(int, int, int)>();
        _destMap = new Dictionary<int, DestInfo>();
    }

    public bool AddPacket(int source, int destination, int timestamp)
    {
        var key = (source, destination, timestamp);
        if (_set.Contains(key))
            return false;

        if (_queue.Count == _capacity)
            EvictOldest();

        var pkt = new Packet { Source = source, Dest = destination, Time = timestamp };
        _queue.Enqueue(pkt);
        _set.Add(key);

        if (!_destMap.TryGetValue(destination, out var info))
        {
            info = new DestInfo();
            _destMap[destination] = info;
        }
        info.Timestamps.Add(timestamp);
        return true;
    }

    private void EvictOldest()
    {
        var old = _queue.Dequeue();
        var key = (old.Source, old.Dest, old.Time);
        _set.Remove(key);

        if (_destMap.TryGetValue(old.Dest, out var info))
        {
            info.Offset++;
            TrimIfNeeded(info);
        }
    }

    public int[] ForwardPacket()
    {
        if (_queue.Count == 0)
            return new int[0];

        var pkt = _queue.Dequeue();
        var key = (pkt.Source, pkt.Dest, pkt.Time);
        _set.Remove(key);

        if (_destMap.TryGetValue(pkt.Dest, out var info))
        {
            info.Offset++;
            TrimIfNeeded(info);
        }

        return new[] { pkt.Source, pkt.Dest, pkt.Time };
    }

    public int GetCount(int destination, int startTime, int endTime)
    {
        if (!_destMap.TryGetValue(destination, out var info))
            return 0;

        int off = info.Offset;
        int total = info.Timestamps.Count;
        if (off >= total)
            return 0;

        // lower bound for startTime
        int l = off, r = total;
        while (l < r)
        {
            int m = (l + r) >> 1;
            if (info.Timestamps[m] < startTime)
                l = m + 1;
            else
                r = m;
        }
        int leftIdx = l;

        // upper bound for endTime (first > endTime)
        l = off; r = total;
        while (l < r)
        {
            int m = (l + r) >> 1;
            if (info.Timestamps[m] <= endTime)
                l = m + 1;
            else
                r = m;
        }
        int rightIdx = l;

        return Math.Max(0, rightIdx - leftIdx);
    }

    private void TrimIfNeeded(DestInfo info)
    {
        // optional cleanup to avoid unbounded growth of the list prefix
        if (info.Offset > 100 && info.Offset * 2 >= info.Timestamps.Count)
        {
            var newList = info.Timestamps.GetRange(info.Offset, info.Timestamps.Count - info.Offset);
            info.Timestamps = newList;
            info.Offset = 0;
        }
    }

    private class Packet
    {
        public int Source;
        public int Dest;
        public int Time;
    }

    private class DestInfo
    {
        public List<int> Timestamps = new List<int>();
        public int Offset = 0;
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * Router obj = new Router(memoryLimit);
 * bool param_1 = obj.AddPacket(source,destination,timestamp);
 * int[] param_2 = obj.ForwardPacket();
 * int param_3 = obj.GetCount(destination,startTime,endTime);
 */
```

## Javascript

```javascript
/**
 * @param {number} memoryLimit
 */
var Router = function(memoryLimit) {
    this.limit = memoryLimit;
    this.queue = [];          // stores packets in order of insertion
    this.head = 0;            // index of the first valid packet in queue
    this.size = 0;            // current number of stored packets

    this.packetSet = new Set();   // to detect duplicates, key: "src,dest,ts"

    // destination -> array of timestamps (in insertion order)
    this.destMap = new Map();
    // destination -> start index within its timestamp array (elements before are removed)
    this.destHead = new Map();
};

/** 
 * @param {number} source 
 * @param {number} destination 
 * @param {number} timestamp
 * @return {boolean}
 */
Router.prototype.addPacket = function(source, destination, timestamp) {
    const key = `${source},${destination},${timestamp}`;
    if (this.packetSet.has(key)) return false;

    // If memory is full, evict the oldest packet
    if (this.size === this.limit) {
        const oldPkt = this.queue[this.head];
        this.head++;
        this.size--;

        const oldKey = `${oldPkt.src},${oldPkt.dest},${oldPkt.ts}`;
        this.packetSet.delete(oldKey);

        // remove timestamp from its destination list
        const d = oldPkt.dest;
        const headIdx = (this.destHead.get(d) || 0) + 1;
        this.destHead.set(d, headIdx);
        const arr = this.destMap.get(d);
        if (headIdx >= arr.length) {
            this.destMap.delete(d);
            this.destHead.delete(d);
        }
    }

    // Add new packet
    const pkt = {src: source, dest: destination, ts: timestamp};
    this.queue.push(pkt);
    this.size++;
    this.packetSet.add(key);

    if (!this.destMap.has(destination)) {
        this.destMap.set(destination, []);
        this.destHead.set(destination, 0);
    }
    this.destMap.get(destination).push(timestamp);
    return true;
};

/**
 * @return {number[]}
 */
Router.prototype.forwardPacket = function() {
    if (this.size === 0) return [];

    const pkt = this.queue[this.head];
    this.head++;
    this.size--;

    const key = `${pkt.src},${pkt.dest},${pkt.ts}`;
    this.packetSet.delete(key);

    // update destination timestamps
    const d = pkt.dest;
    const headIdx = (this.destHead.get(d) || 0) + 1;
    this.destHead.set(d, headIdx);
    const arr = this.destMap.get(d);
    if (headIdx >= arr.length) {
        this.destMap.delete(d);
        this.destHead.delete(d);
    }

    return [pkt.src, pkt.dest, pkt.ts];
};

/** 
 * @param {number} destination 
 * @param {number} startTime 
 * @param {number} endTime
 * @return {number}
 */
Router.prototype.getCount = function(destination, startTime, endTime) {
    const arr = this.destMap.get(destination);
    if (!arr) return 0;
    const startIdx = this.destHead.get(destination) || 0;

    // lower bound for startTime
    let l = startIdx, r = arr.length;
    while (l < r) {
        const m = (l + r) >> 1;
        if (arr[m] >= startTime) r = m;
        else l = m + 1;
    }
    const left = l;

    // upper bound for endTime (first > endTime)
    l = startIdx; r = arr.length;
    while (l < r) {
        const m = (l + r) >> 1;
        if (arr[m] > endTime) r = m;
        else l = m + 1;
    }
    const right = l;

    return Math.max(0, right - left);
};

/** 
 * Your Router object will be instantiated and called as such:
 * var obj = new Router(memoryLimit)
 * var param_1 = obj.addPacket(source,destination,timestamp)
 * var param_2 = obj.forwardPacket()
 * var param_3 = obj.getCount(destination,startTime,endTime)
 */
```

## Typescript

```typescript
class Router {
    private limit: number;
    private queue: { src: number; dst: number; ts: number }[];
    private head: number;
    private keySet: Set<string>;
    private destMap: Map<number, { arr: number[]; headIdx: number }>;

    constructor(memoryLimit: number) {
        this.limit = memoryLimit;
        this.queue = [];
        this.head = 0;
        this.keySet = new Set();
        this.destMap = new Map();
    }

    addPacket(source: number, destination: number, timestamp: number): boolean {
        const key = `${source},${destination},${timestamp}`;
        if (this.keySet.has(key)) return false;

        // Evict oldest if at capacity
        if (this.queue.length - this.head >= this.limit) {
            const old = this.queue[this.head];
            this.head++;
            const oldKey = `${old.src},${old.dst},${old.ts}`;
            this.keySet.delete(oldKey);
            const info = this.destMap.get(old.dst);
            if (info) {
                info.headIdx++;
                if (info.headIdx === info.arr.length) {
                    this.destMap.delete(old.dst);
                }
            }
        }

        // Add new packet
        this.queue.push({ src: source, dst: destination, ts: timestamp });
        this.keySet.add(key);

        let info = this.destMap.get(destination);
        if (!info) {
            info = { arr: [timestamp], headIdx: 0 };
            this.destMap.set(destination, info);
        } else {
            info.arr.push(timestamp);
        }
        return true;
    }

    forwardPacket(): number[] {
        if (this.queue.length === this.head) return [];
        const pkt = this.queue[this.head];
        this.head++;

        const key = `${pkt.src},${pkt.dst},${pkt.ts}`;
        this.keySet.delete(key);

        const info = this.destMap.get(pkt.dst);
        if (info) {
            info.headIdx++;
            if (info.headIdx === info.arr.length) {
                this.destMap.delete(pkt.dst);
            }
        }

        return [pkt.src, pkt.dst, pkt.ts];
    }

    getCount(destination: number, startTime: number, endTime: number): number {
        const info = this.destMap.get(destination);
        if (!info) return 0;
        const arr = info.arr;
        let l = info.headIdx,
            r = arr.length;

        // lower bound for startTime
        let lo = l,
            hi = r;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] >= startTime) hi = mid;
            else lo = mid + 1;
        }
        const left = lo;

        // upper bound for endTime
        lo = l;
        hi = r;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] > endTime) hi = mid;
            else lo = mid + 1;
        }
        const right = lo;

        return Math.max(0, right - left);
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * var obj = new Router(memoryLimit)
 * var param_1 = obj.addPacket(source,destination,timestamp)
 * var param_2 = obj.forwardPacket()
 * var param_3 = obj.getCount(destination,startTime,endTime)
 */
```

## Php

```php
class Router {
    private int $memoryLimit;
    private array $queue = [];
    private int $head = 0;
    private int $size = 0;
    private array $set = [];          // to detect duplicates
    private array $destMap = [];      // destination => ['arr'=>[], 'head'=>int]

    public function __construct($memoryLimit) {
        $this->memoryLimit = (int)$memoryLimit;
    }

    public function addPacket($source, $destination, $timestamp) {
        $key = $source . ',' . $destination . ',' . $timestamp;
        if (isset($this->set[$key])) {
            return false;
        }

        // Evict oldest if at capacity
        if ($this->size == $this->memoryLimit) {
            $oldPacket = $this->queue[$this->head];
            $this->removeOldest($oldPacket);
            $this->head++;
        }

        // Add new packet
        $packet = [(int)$source, (int)$destination, (int)$timestamp];
        $this->queue[] = $packet;
        $this->set[$key] = true;

        if (!isset($this->destMap[$destination])) {
            $this->destMap[$destination] = ['arr' => [], 'head' => 0];
        }
        $this->destMap[$destination]['arr'][] = (int)$timestamp;
        $this->size++;

        return true;
    }

    private function removeOldest(array $packet): void {
        [$source, $destination, $timestamp] = $packet;
        $key = $source . ',' . $destination . ',' . $timestamp;
        unset($this->set[$key]);

        if (isset($this->destMap[$destination])) {
            $info =& $this->destMap[$destination];
            $info['head']++;
            // Clean up if no timestamps remain
            if ($info['head'] >= count($info['arr'])) {
                $info['arr'] = [];
                $info['head'] = 0;
            }
        }

        $this->size--;
    }

    public function forwardPacket() {
        if ($this->size == 0) {
            return [];
        }

        $packet = $this->queue[$this->head];
        $this->removeOldest($packet);
        $this->head++;

        return [$packet[0], $packet[1], $packet[2]];
    }

    public function getCount($destination, $startTime, $endTime) {
        if (!isset($this->destMap[$destination])) {
            return 0;
        }
        $info = $this->destMap[$destination];
        $arr = $info['arr'];
        $head = $info['head'];
        $n = count($arr);
        if ($head >= $n) {
            return 0;
        }

        // lower bound for startTime
        $l = $head;
        $r = $n;
        while ($l < $r) {
            $mid = intdiv($l + $r, 2);
            if ($arr[$mid] < $startTime) {
                $l = $mid + 1;
            } else {
                $r = $mid;
            }
        }
        $lb = $l;

        // upper bound for endTime (first > endTime)
        $l = $head;
        $r = $n;
        while ($l < $r) {
            $mid = intdiv($l + $r, 2);
            if ($arr[$mid] <= $endTime) {
                $l = $mid + 1;
            } else {
                $r = $mid;
            }
        }
        $ub = $l;

        $cnt = $ub - $lb;
        return $cnt > 0 ? $cnt : 0;
    }
}
```

## Swift

```swift
class Router {
    struct Packet {
        let source: Int
        let destination: Int
        let timestamp: Int
    }
    
    struct PacketKey: Hashable {
        let s: Int
        let d: Int
        let t: Int
    }
    
    struct DestInfo {
        var timestamps: [Int]
        var head: Int
    }
    
    private let limit: Int
    private var queue: [Packet] = []
    private var headIdx: Int = 0
    private var packetSet = Set<PacketKey>()
    private var destMap = [Int: DestInfo]()
    
    init(_ memoryLimit: Int) {
        self.limit = memoryLimit
    }
    
    func addPacket(_ source: Int, _ destination: Int, _ timestamp: Int) -> Bool {
        let key = PacketKey(s: source, d: destination, t: timestamp)
        if packetSet.contains(key) { return false }
        
        while queue.count - headIdx >= limit {
            let old = queue[headIdx]
            headIdx += 1
            packetSet.remove(PacketKey(s: old.source, d: old.destination, t: old.timestamp))
            if var info = destMap[old.destination] {
                info.head += 1
                destMap[old.destination] = info
            }
        }
        
        let pkt = Packet(source: source, destination: destination, timestamp: timestamp)
        queue.append(pkt)
        packetSet.insert(key)
        var info = destMap[destination] ?? DestInfo(timestamps: [], head: 0)
        info.timestamps.append(timestamp)
        destMap[destination] = info
        return true
    }
    
    func forwardPacket() -> [Int] {
        if queue.count - headIdx == 0 { return [] }
        let pkt = queue[headIdx]
        headIdx += 1
        packetSet.remove(PacketKey(s: pkt.source, d: pkt.destination, t: pkt.timestamp))
        if var info = destMap[pkt.destination] {
            info.head += 1
            destMap[pkt.destination] = info
        }
        return [pkt.source, pkt.destination, pkt.timestamp]
    }
    
    func getCount(_ destination: Int, _ startTime: Int, _ endTime: Int) -> Int {
        guard let info = destMap[destination] else { return 0 }
        let timestamps = info.timestamps
        if timestamps.isEmpty { return 0 }
        let l = lowerBound(timestamps, startTime)
        let r = upperBound(timestamps, endTime)
        let effectiveL = max(l, info.head)
        let cnt = r - effectiveL
        return cnt > 0 ? cnt : 0
    }
    
    private func lowerBound(_ arr: [Int], _ target: Int) -> Int {
        var l = 0, r = arr.count
        while l < r {
            let m = (l + r) >> 1
            if arr[m] < target {
                l = m + 1
            } else {
                r = m
            }
        }
        return l
    }
    
    private func upperBound(_ arr: [Int], _ target: Int) -> Int {
        var l = 0, r = arr.count
        while l < r {
            let m = (l + r) >> 1
            if arr[m] <= target {
                l = m + 1
            } else {
                r = m
            }
        }
        return l
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * let obj = Router(memoryLimit)
 * let ret_1: Bool = obj.addPacket(source, destination, timestamp)
 * let ret_2: [Int] = obj.forwardPacket()
 * let ret_3: Int = obj.getCount(destination, startTime, endTime)
 */
```

## Kotlin

```kotlin
class Router(memoryLimit: Int) {

    private val limit = memoryLimit
    private val queue: ArrayDeque<Packet> = ArrayDeque()
    private val existing = HashSet<Long>()

    private data class DestData(val timestamps: MutableList<Int>, var head: Int)

    private val destMap = HashMap<Int, DestData>()

    private data class Packet(val source: Int, val destination: Int, val timestamp: Int)

    private fun packKey(s: Int, d: Int, t: Int): Long {
        // s,d <= 2*10^5 (<2^18), t <= 10^9 (<2^30)
        return (s.toLong() shl 40) xor (d.toLong() shl 20) xor t.toLong()
    }

    fun addPacket(source: Int, destination: Int, timestamp: Int): Boolean {
        val key = packKey(source, destination, timestamp)
        if (!existing.add(key)) return false

        if (queue.size == limit) {
            val old = queue.removeFirst()
            existing.remove(packKey(old.source, old.destination, old.timestamp))
            val dataOld = destMap[old.destination]!!
            dataOld.head++
            if (dataOld.head >= dataOld.timestamps.size) {
                destMap.remove(old.destination)
            }
        }

        queue.addLast(Packet(source, destination, timestamp))
        val dData = destMap.getOrPut(destination) { DestData(mutableListOf(), 0) }
        dData.timestamps.add(timestamp)
        return true
    }

    fun forwardPacket(): IntArray {
        if (queue.isEmpty()) return intArrayOf()
        val p = queue.removeFirst()
        existing.remove(packKey(p.source, p.destination, p.timestamp))
        val data = destMap[p.destination]!!
        data.head++
        if (data.head >= data.timestamps.size) {
            destMap.remove(p.destination)
        }
        return intArrayOf(p.source, p.destination, p.timestamp)
    }

    fun getCount(destination: Int, startTime: Int, endTime: Int): Int {
        val data = destMap[destination] ?: return 0
        val list = data.timestamps
        var l = data.head
        var r = list.size - 1
        var leftIdx = -1
        while (l <= r) {
            val m = (l + r) ushr 1
            if (list[m] >= startTime) {
                leftIdx = m
                r = m - 1
            } else {
                l = m + 1
            }
        }
        if (leftIdx == -1) return 0
        l = leftIdx
        r = list.size - 1
        var rightIdx = -1
        while (l <= r) {
            val m = (l + r) ushr 1
            if (list[m] <= endTime) {
                rightIdx = m
                l = m + 1
            } else {
                r = m - 1
            }
        }
        return if (rightIdx == -1) 0 else rightIdx - leftIdx + 1
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * var obj = Router(memoryLimit)
 * var param_1 = obj.addPacket(source,destination,timestamp)
 * var param_2 = obj.forwardPacket()
 * var param_3 = obj.getCount(destination,startTime,endTime)
 */
```

## Dart

```dart
import 'dart:collection';

class _Packet {
  final int source;
  final int destination;
  final int timestamp;
  _Packet(this.source, this.destination, this.timestamp);
}

class Router {
  final int memoryLimit;
  final Queue<_Packet> _queue = Queue<_Packet>();
  final Set<String> _packetSet = <String>{};
  final Map<int, List<int>> _destTimes = <int, List<int>>{};
  final Map<int, int> _destStartIdx = <int, int>{};

  Router(this.memoryLimit);

  bool addPacket(int source, int destination, int timestamp) {
    String key = '${source}_$destination_$timestamp';
    if (_packetSet.contains(key)) return false;

    if (_queue.length == memoryLimit) {
      // Evict oldest packet
      _evictOldest();
    }

    // Add new packet
    var pkt = _Packet(source, destination, timestamp);
    _queue.addLast(pkt);
    _packetSet.add(key);

    _destTimes.putIfAbsent(destination, () => <int>[]).add(timestamp);
    return true;
  }

  List<int> forwardPacket() {
    if (_queue.isEmpty) return [];
    var pkt = _queue.removeFirst();
    String key = '${pkt.source}_${pkt.destination}_${pkt.timestamp}';
    _packetSet.remove(key);

    // Remove timestamp from destination list (front)
    int dest = pkt.destination;
    List<int> lst = _destTimes[dest]!;
    int startIdx = _destStartIdx[dest] ?? 0;
    if (startIdx < lst.length && lst[startIdx] == pkt.timestamp) {
      _destStartIdx[dest] = startIdx + 1;
    } else {
      // Fallback linear removal (should not happen under FIFO guarantees)
      for (int i = startIdx; i < lst.length; i++) {
        if (lst[i] == pkt.timestamp) {
          lst.removeAt(i);
          break;
        }
      }
    }

    return [pkt.source, pkt.destination, pkt.timestamp];
  }

  int getCount(int destination, int startTime, int endTime) {
    List<int>? lst = _destTimes[destination];
    if (lst == null) return 0;
    int startIdx = _destStartIdx[destination] ?? 0;
    int n = lst.length;

    // lower bound for startTime
    int lo = startIdx, hi = n;
    while (lo < hi) {
      int mid = (lo + hi) >> 1;
      if (lst[mid] >= startTime) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }
    int left = lo;

    // upper bound for endTime
    lo = startIdx;
    hi = n;
    while (lo < hi) {
      int mid = (lo + hi) >> 1;
      if (lst[mid] > endTime) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }
    int right = lo;

    return right - left;
  }

  void _evictOldest() {
    var pkt = _queue.removeFirst();
    String key = '${pkt.source}_${pkt.destination}_${pkt.timestamp}';
    _packetSet.remove(key);

    // Remove timestamp from destination list (front)
    int dest = pkt.destination;
    List<int> lst = _destTimes[dest]!;
    int startIdx = _destStartIdx[dest] ?? 0;
    if (startIdx < lst.length && lst[startIdx] == pkt.timestamp) {
      _destStartIdx[dest] = startIdx + 1;
    } else {
      // Fallback linear removal
      for (int i = startIdx; i < lst.length; i++) {
        if (lst[i] == pkt.timestamp) {
          lst.removeAt(i);
          break;
        }
      }
    }
  }
}

/**
 * Your Router object will be instantiated and called as such:
 * Router obj = Router(memoryLimit);
 * bool param1 = obj.addPacket(source,destination,timestamp);
 * List<int> param2 = obj.forwardPacket();
 * int param3 = obj.getCount(destination,startTime,endTime);
 */
```

## Golang

```go
type Packet struct {
	src, dst, ts int
}

type Router struct {
	limit      int
	queue      []Packet
	head       int
	present    map[int64]struct{}
	destTimes  map[int][]int
	destStart  map[int]int
	size       int
}

// Constructor initializes the router with a memory limit.
func Constructor(memoryLimit int) Router {
	return Router{
		limit:     memoryLimit,
		queue:     make([]Packet, 0),
		present:   make(map[int64]struct{}),
		destTimes: make(map[int][]int),
		destStart: make(map[int]int),
	}
}

// encode creates a unique key for a packet.
func encode(src, dst, ts int) int64 {
	return (int64(src) << 40) | (int64(dst) << 20) | int64(ts)
}

// internal method to remove the front packet without returning it.
func (this *Router) popFront() {
	if this.size == 0 {
		return
	}
	p := this.queue[this.head]
	key := encode(p.src, p.dst, p.ts)
	delete(this.present, key)

	// advance destination timestamp start index
	startIdx := this.destStart[p.dst]
	this.destStart[p.dst] = startIdx + 1

	this.head++
	this.size--
}

// AddPacket adds a packet if not duplicate; evicts oldest when full.
func (this *Router) AddPacket(source int, destination int, timestamp int) bool {
	key := encode(source, destination, timestamp)
	if _, ok := this.present[key]; ok {
		return false
	}
	if this.size == this.limit {
		this.popFront()
	}
	// add packet
	p := Packet{src: source, dst: destination, ts: timestamp}
	this.queue = append(this.queue, p)
	this.present[key] = struct{}{}
	this.destTimes[destination] = append(this.destTimes[destination], timestamp)
	this.size++
	return true
}

// ForwardPacket removes and returns the next packet in FIFO order.
func (this *Router) ForwardPacket() []int {
	if this.size == 0 {
		return []int{}
	}
	p := this.queue[this.head]
	this.popFront()
	return []int{p.src, p.dst, p.ts}
}

// GetCount returns number of packets with given destination and timestamp range.
func (this *Router) GetCount(destination int, startTime int, endTime int) int {
	times, ok := this.destTimes[destination]
	if !ok {
		return 0
	}
	startIdx := this.destStart[destination]
	eff := times[startIdx:]

	// binary search for left bound (first >= startTime)
	left := sort.Search(len(eff), func(i int) bool { return eff[i] >= startTime })
	// right bound (first > endTime)
	right := sort.Search(len(eff), func(i int) bool { return eff[i] > endTime })
	return right - left
}

/**
 * Your Router object will be instantiated and called as such:
 * obj := Constructor(memoryLimit);
 * param_1 := obj.AddPacket(source,destination,timestamp);
 * param_2 := obj.ForwardPacket();
 * param_3 := obj.GetCount(destination,startTime,endTime);
 */
```

## Ruby

```ruby
class Router
  def initialize(memory_limit)
    @capacity = memory_limit
    @queue = []          # stores [source, destination, timestamp]
    @front = 0           # index of the current front in @queue
    @size = 0            # number of packets currently stored
    @packet_set = {}     # key => true for duplicate detection
    @dest_info = Hash.new { |h, k| h[k] = { arr: [], head: 0 } }
  end

  def add_packet(source, destination, timestamp)
    key = [source, destination, timestamp]
    return false if @packet_set.key?(key)

    # insert packet
    @queue << [source, destination, timestamp]
    @size += 1
    @packet_set[key] = true
    info = @dest_info[destination]
    info[:arr] << timestamp

    # evict oldest if over capacity
    if @size > @capacity
      evicted = @queue[@front]
      @front += 1
      @size -= 1
      s, d, t = evicted
      @packet_set.delete([s, d, t])
      ev_info = @dest_info[d]
      if ev_info[:arr][ev_info[:head]] == t
        ev_info[:head] += 1
      else
        idx = ev_info[:arr].index(t, ev_info[:head])
        ev_info[:arr].delete_at(idx) if idx
      end
    end

    true
  end

  def forward_packet
    return [] if @size == 0

    pkt = @queue[@front]
    @front += 1
    @size -= 1
    s, d, t = pkt
    @packet_set.delete([s, d, t])

    info = @dest_info[d]
    if info[:arr][info[:head]] == t
      info[:head] += 1
    else
      idx = info[:arr].index(t, info[:head])
      info[:arr].delete_at(idx) if idx
    end

    [s, d, t]
  end

  def get_count(destination, start_time, end_time)
    info = @dest_info[destination]
    return 0 unless info && info[:arr].length > info[:head]

    arr = info[:arr]
    head = info[:head]

    # lower bound for start_time
    lo = head
    hi = arr.length
    while lo < hi
      mid = (lo + hi) / 2
      if arr[mid] < start_time
        lo = mid + 1
      else
        hi = mid
      end
    end
    left = lo

    # upper bound for end_time
    lo = head
    hi = arr.length
    while lo < hi
      mid = (lo + hi) / 2
      if arr[mid] <= end_time
        lo = mid + 1
      else
        hi = mid
      end
    end
    right = lo

    right - left
  end
end
```

## Scala

```scala
import scala.collection.mutable.{ArrayDeque, ArrayBuffer, HashMap, HashSet}

class Router(_memoryLimit: Int) {

  private case class Packet(source: Int, destination: Int, timestamp: Int)

  private val capacity = _memoryLimit
  private val queue = new ArrayDeque[Packet]()
  private val packetSet = new HashSet[(Int, Int, Int)]()
  private val destTimestamps = new HashMap[Int, ArrayBuffer[Int]]()
  private val destStartIdx = new HashMap[Int, Int]()

  def addPacket(source: Int, destination: Int, timestamp: Int): Boolean = {
    val key = (source, destination, timestamp)
    if (packetSet.contains(key)) return false

    if (queue.length == capacity) {
      val old = queue.removeHead()
      discard(old)
    }

    val pkt = Packet(source, destination, timestamp)
    queue.append(pkt)
    packetSet.add(key)

    val buf = destTimestamps.getOrElseUpdate(destination, new ArrayBuffer[Int]())
    buf.append(timestamp)

    true
  }

  def forwardPacket(): Array[Int] = {
    if (queue.isEmpty) return Array.emptyIntArray
    val pkt = queue.removeHead()
    packetSet.remove((pkt.source, pkt.destination, pkt.timestamp))
    incrementStart(pkt.destination)
    Array(pkt.source, pkt.destination, pkt.timestamp)
  }

  def getCount(destination: Int, startTime: Int, endTime: Int): Int = {
    destTimestamps.get(destination) match {
      case None => 0
      case Some(buf) =>
        val offset = destStartIdx.getOrElse(destination, 0)
        if (offset >= buf.length) return 0

        // lower bound for startTime
        var l = offset
        var r = buf.length
        while (l < r) {
          val m = (l + r) >>> 1
          if (buf(m) >= startTime) r = m else l = m + 1
        }
        val leftIdx = l

        // upper bound for endTime (first > endTime)
        l = offset
        r = buf.length
        while (l < r) {
          val m = (l + r) >>> 1
          if (buf(m) > endTime) r = m else l = m + 1
        }
        val rightIdx = l

        math.max(0, rightIdx - leftIdx)
    }
  }

  private def discard(pkt: Packet): Unit = {
    packetSet.remove((pkt.source, pkt.destination, pkt.timestamp))
    incrementStart(pkt.destination)
  }

  private def incrementStart(dest: Int): Unit = {
    val cur = destStartIdx.getOrElse(dest, 0)
    destStartIdx.update(dest, cur + 1)
  }
}

/**
 * Your Router object will be instantiated and called as such:
 * val obj = new Router(memoryLimit)
 * val param_1 = obj.addPacket(source,destination,timestamp)
 * val param_2 = obj.forwardPacket()
 * val param_3 = obj.getCount(destination,startTime,endTime)
 */
```

## Rust

```rust
use std::collections::{HashMap, HashSet, VecDeque};
use std::cell::RefCell;

#[derive(Clone)]
struct Packet {
    source: i32,
    destination: i32,
    timestamp: i32,
}

struct DestInfo {
    timestamps: Vec<i32>,
    start: usize,
}

pub struct Router {
    memory_limit: usize,
    queue: RefCell<VecDeque<Packet>>,
    set: RefCell<HashSet<(i32, i32, i32)>>,
    dest_map: RefCell<HashMap<i32, DestInfo>>,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Router {

    fn new(memoryLimit: i32) -> Self {
        Router {
            memory_limit: memoryLimit as usize,
            queue: RefCell::new(VecDeque::new()),
            set: RefCell::new(HashSet::new()),
            dest_map: RefCell::new(HashMap::new()),
        }
    }
    
    fn add_packet(&self, source: i32, destination: i32, timestamp: i32) -> bool {
        let key = (source, destination, timestamp);
        if self.set.borrow().contains(&key) {
            return false;
        }

        // evict if needed
        if self.queue.borrow().len() == self.memory_limit {
            let old = self.queue.borrow_mut().pop_front().unwrap();
            self.set.borrow_mut().remove(&(old.source, old.destination, old.timestamp));
            if let Some(info) = self.dest_map.borrow_mut().get_mut(&old.destination) {
                info.start += 1;
                // occasional cleanup to avoid unbounded growth
                if info.start > 1024 && info.start * 2 > info.timestamps.len() {
                    info.timestamps.drain(0..info.start);
                    info.start = 0;
                }
            }
        }

        // insert new packet
        self.queue.borrow_mut().push_back(Packet { source, destination, timestamp });
        self.set.borrow_mut().insert(key);
        let mut map_ref = self.dest_map.borrow_mut();
        let entry = map_ref.entry(destination).or_insert(DestInfo {
            timestamps: Vec::new(),
            start: 0,
        });
        entry.timestamps.push(timestamp);
        true
    }
    
    fn forward_packet(&self) -> Vec<i32> {
        if let Some(p) = self.queue.borrow_mut().pop_front() {
            self.set.borrow_mut().remove(&(p.source, p.destination, p.timestamp));
            if let Some(info) = self.dest_map.borrow_mut().get_mut(&p.destination) {
                info.start += 1;
                if info.start > 1024 && info.start * 2 > info.timestamps.len() {
                    info.timestamps.drain(0..info.start);
                    info.start = 0;
                }
            }
            vec![p.source, p.destination, p.timestamp]
        } else {
            Vec::new()
        }
    }
    
    fn get_count(&self, destination: i32, start_time: i32, end_time: i32) -> i32 {
        if let Some(info) = self.dest_map.borrow().get(&destination) {
            let slice = &info.timestamps[info.start..];
            let left = match slice.binary_search(&start_time) {
                Ok(idx) => idx,
                Err(idx) => idx,
            };
            // use end_time + 1 to find first greater than end_time
            let right = match slice.binary_search(&(end_time.wrapping_add(1))) {
                Ok(idx) => idx,
                Err(idx) => idx,
            };
            (right - left) as i32
        } else {
            0
        }
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * let obj = Router::new(memoryLimit);
 * let ret_1: bool = obj.add_packet(source, destination, timestamp);
 * let ret_2: Vec<i32> = obj.forward_packet();
 * let ret_3: i32 = obj.get_count(destination, startTime, endTime);
 */
```

## Racket

```racket
(struct dest-info (buf head size) #:mutable)

(define (make-dest-info)
  (dest-info (make-vector 4) 0 0))

(define (dest-add! info ts)
  (let* ([buf (dest-info-buf info)]
         [len (vector-length buf)])
    (when (= (dest-info-size info) len)
      (let* ([new-len (* 2 len)]
             [new-buf (make-vector new-len)])
        (for ([i (in-range (dest-info-size info))])
          (vector-set! new-buf i
                       (vector-ref buf (modulo (+ (dest-info-head info) i) len))))
        (set-dest-info-buf! info new-buf)
        (set-dest-info-head! info 0)))
    (let* ([pos (modulo (+ (dest-info-head info) (dest-info-size info))
                       (vector-length (dest-info-buf info)))])
      (vector-set! (dest-info-buf info) pos ts)
      (set-dest-info-size! info (+ (dest-info-size info) 1)))))

(define (dest-remove-front! info)
  (when (> (dest-info-size info) 0)
    (set-dest-info-head! info
                         (modulo (+ (dest-info-head info) 1)
                                 (vector-length (dest-info-buf info))))
    (set-dest-info-size! info (- (dest-info-size info) 1))))

(define (dest-get info i)
  (vector-ref (dest-info-buf info)
              (modulo (+ (dest-info-head info) i)
                      (vector-length (dest-info-buf info)))))

(define (dest-lower-bound info target)
  (let loop ([lo 0] [hi (dest-info-size info)])
    (if (= lo hi)
        lo
        (let* ([mid (quotient (+ lo hi) 2)]
               [val (dest-get info mid)])
          (if (< val target)
              (loop (+ mid 1) hi)
              (loop lo mid))))))

(define (dest-upper-bound info target)
  (let loop ([lo 0] [hi (dest-info-size info)])
    (if (= lo hi)
        lo
        (let* ([mid (quotient (+ lo hi) 2)]
               [val (dest-get info mid)])
          (if (<= val target)
              (loop (+ mid 1) hi)
              (loop lo mid))))))

(define router%
  (class object%
    (super-new)

    (init-field memory-limit)

    ;; internal state
    (define capacity memory-limit)
    (define buf (make-vector capacity))
    (define head 0)
    (define size 0)
    (define dup (make-hash))          ; duplicate detection
    (define dest-map (make-hash))     ; destination -> dest-info

    ;; helper: packet at logical index i
    (define (packet-at i)
      (vector-ref buf (modulo (+ head i) capacity)))

    ;; add-packet
    (define/public (add-packet source destination timestamp)
      (let ([key (format "~a#~a#~a" source destination timestamp)])
        (if (hash-has-key? dup key)
            #f
            (begin
              ;; evict if full
              (when (= size capacity)
                (let* ([old-pkt (packet-at 0)]
                       [old-src (list-ref old-pkt 0)]
                       [old-dst (list-ref old-pkt 1)]
                       [old-ts (list-ref old-pkt 2)]
                       [old-key (format "~a#~a#~a" old-src old-dst old-ts)])
                  (hash-remove! dup old-key)
                  (let ([info (hash-ref dest-map old-dst #f)])
                    (when info
                      (dest-remove-front! info)
                      (when (= (dest-info-size info) 0)
                        (hash-remove! dest-map old-dst))))
                  (set! head (modulo (+ head 1) capacity))
                  (set! size (- size 1))))
              ;; insert new packet at tail
              (let ([pos (modulo (+ head size) capacity)])
                (vector-set! buf pos (list source destination timestamp)))
              (hash-set! dup key #t)
              ;; update destination info
              (let* ([info (hash-ref dest-map destination
                                      (lambda ()
                                        (define ni (make-dest-info))
                                        (hash-set! dest-map destination ni)
                                        ni))])
                (dest-add! info timestamp))
              (set! size (+ size 1))
              #t)))))

    ;; forward-packet
    (define/public (forward-packet)
      (if (= size 0)
          '()
          (let* ([pkt (packet-at 0)]
                 [src (list-ref pkt 0)]
                 [dst (list-ref pkt 1)]
                 [ts (list-ref pkt 2)]
                 [key (format "~a#~a#~a" src dst ts)])
            (hash-remove! dup key)
            (let ([info (hash-ref dest-map dst #f)])
              (when info
                (dest-remove-front! info)
                (when (= (dest-info-size info) 0)
                  (hash-remove! dest-map dst))))
            (set! head (modulo (+ head 1) capacity))
            (set! size (- size 1))
            (list src dst ts)))))

    ;; get-count
    (define/public (get-count destination start-time end-time)
      (let ([info (hash-ref dest-map destination #f)])
        (if (not info)
            0
            (let* ([lb (dest-lower-bound info start-time)]
                   [ub (dest-upper-bound info end-time)])
              (- ub lb)))))

    ))
```

## Erlang

```erlang
-spec router_init_(MemoryLimit :: integer()) -> any().
router_init_(MemoryLimit) ->
    put(memory_limit, MemoryLimit),
    put(queue, queue:new()),
    put(dest_map, #{}),
    put(current_size, 0),
    put(packet_set, #{}) .

-spec router_add_packet(Source :: integer(), Destination :: integer(), Timestamp :: integer()) -> boolean().
router_add_packet(Source, Destination, Timestamp) ->
    PacketKey = {Source, Destination, Timestamp},
    PacketSet = get(packet_set),
    case maps:is_key(PacketKey, PacketSet) of
        true ->
            false;
        false ->
            Limit = get(memory_limit),
            Size = get(current_size),
            Queue0 = get(queue),
            DestMap0 = get(dest_map),

            %% Evict if needed
            {Queue1, DestMap1, NewSize, NewPacketSet} =
                if Size < Limit ->
                        Q2 = queue:in(PacketKey, Queue0),
                        DM2 = insert_timestamp(DestMap0, Destination, Timestamp),
                        {Q2, DM2, Size + 1, maps:put(PacketKey, true, PacketSet)};
                   true ->
                        {{value, OldPkt}, Qtemp} = queue:out(Queue0),
                        %% Remove old packet from structures
                        {OldSrc, OldDst, OldTs} = OldPkt,
                        OldKey = OldPkt,
                        DM2 = delete_timestamp(DestMap0, OldDst, OldTs),
                        DM3 = insert_timestamp(DM2, Destination, Timestamp),
                        UpdatedSet = maps:remove(OldKey, PacketSet),
                        Q2 = queue:in(PacketKey, Qtemp),
                        {Q2, DM3, Size, maps:put(PacketKey, true, UpdatedSet)}
                end,

            put(queue, Queue1),
            put(dest_map, DestMap1),
            put(current_size, NewSize),
            put(packet_set, NewPacketSet),
            true
    end.

-spec router_forward_packet() -> [integer()].
router_forward_packet() ->
    Queue = get(queue),
    case queue:out(Queue) of
        {empty, _} ->
            [];
        {{value, {Source, Destination, Timestamp}}, Q2} ->
            put(queue, Q2),
            Size = get(current_size) - 1,
            put(current_size, Size),

            DestMap0 = get(dest_map),
            DestMap1 = delete_timestamp(DestMap0, Destination, Timestamp),
            put(dest_map, DestMap1),

            PacketSet = get(packet_set),
            NewSet = maps:remove({Source, Destination, Timestamp}, PacketSet),
            put(packet_set, NewSet),

            [Source, Destination, Timestamp]
    end.

-spec router_get_count(Destination :: integer(), StartTime :: integer(), EndTime :: integer()) -> integer().
router_get_count(Destination, StartTime, EndTime) ->
    DestMap = get(dest_map),
    case maps:find(Destination, DestMap) of
        error -> 0;
        {ok, Tree} ->
            Iterator = gb_trees:iterator_from(StartTime, Tree),
            count_range(Iterator, EndTime, 0)
    end.

%% Helper to insert timestamp with count handling
insert_timestamp(DestMap, Destination, Timestamp) ->
    Tree = maps:get(Destination, DestMap, gb_trees:empty()),
    NewTree =
        case gb_trees:lookup(Timestamp, Tree) of
            {value, C} -> gb_trees:enter(Timestamp, C + 1, Tree);
            none -> gb_trees:enter(Timestamp, 1, Tree)
        end,
    maps:put(Destination, NewTree, DestMap).

%% Helper to delete timestamp with count handling
delete_timestamp(DestMap, Destination, Timestamp) ->
    case maps:find(Destination, DestMap) of
        error -> DestMap;
        {ok, Tree} ->
            case gb_trees:lookup(Timestamp, Tree) of
                {value, 1} ->
                    NewTree = gb_trees:delete_any(Timestamp, Tree);
                {value, C} when C > 1 ->
                    NewTree = gb_trees:enter(Timestamp, C - 1, Tree)
            end,
            case gb_trees:is_empty(NewTree) of
                true -> maps:remove(Destination, DestMap);
                false -> maps:put(Destination, NewTree, DestMap)
            end
    end.

%% Count timestamps in range [Start, End] using iterator
count_range(Iter, EndTime, Acc) ->
    case gb_trees:next(Iter) of
        none -> Acc;
        {Key, Value, NextIter} ->
            if Key > EndTime ->
                    Acc;
               true ->
                    count_range(NextIter, EndTime, Acc + Value)
            end
    end.
```

## Elixir

```elixir
defmodule Router do
  @spec init_(memory_limit :: integer) :: any
  def init_(memory_limit) do
    case :ets.info(:router_state) do
      :undefined -> :ok
      _ -> :ets.delete(:router_state)
    end

    :ets.new(:router_state, [:named_table, :public])
    state = %{
      limit: memory_limit,
      size: 0,
      queue: :queue.new(),
      set: MapSet.new(),
      dest_map: %{}
    }

    :ets.insert(:router_state, {:state, state})
    nil
  end

  @spec add_packet(source :: integer, destination :: integer, timestamp :: integer) :: boolean
  def add_packet(source, destination, timestamp) do
    state = get_state()
    key = {source, destination, timestamp}

    if MapSet.member?(state.set, key) do
      false
    else
      {state, evicted} =
        if state.size == state.limit do
          {{:value, ev}, q} = :queue.out(state.queue)
          ev_key = ev
          new_set = MapSet.delete(state.set, ev_key)

          {esrc, edest, ets} = ev_key
          tree = Map.get(state.dest_map, edest, :gb_trees.empty())
          new_tree =
            case :gb_trees.lookup(ets, tree) do
              {:value, cnt} when cnt > 1 -> :gb_trees.update(ets, cnt - 1, tree)
              {:value, 1} -> :gb_trees.delete_any(ets, tree)
              :none -> tree
            end

          new_dest_map =
            if :gb_trees.is_empty(new_tree) do
              Map.delete(state.dest_map, edest)
            else
              Map.put(state.dest_map, edest, new_tree)
            end

          {%{
             state |
             queue: q,
             set: new_set,
             dest_map: new_dest_map
           }, ev_key}
        else
          {state, nil}
        end

      # add new packet
      new_queue = :queue.in(key, state.queue)
      new_set = MapSet.put(state.set, key)

      tree = Map.get(state.dest_map, destination, :gb_trees.empty())
      new_tree =
        case :gb_trees.lookup(timestamp, tree) do
          {:value, cnt} -> :gb_trees.update(timestamp, cnt + 1, tree)
          :none -> :gb_trees.insert(timestamp, 1, tree)
        end

      new_dest_map = Map.put(state.dest_map, destination, new_tree)

      new_size =
        if state.size == state.limit do
          state.size
        else
          state.size + 1
        end

      new_state = %{
        state |
        queue: new_queue,
        set: new_set,
        dest_map: new_dest_map,
        size: new_size
      }

      put_state(new_state)
      true
    end
  end

  @spec forward_packet() :: [integer]
  def forward_packet() do
    state = get_state()

    if :queue.is_empty(state.queue) do
      []
    else
      {{:value, pkt}, q} = :queue.out(state.queue)
      {src, dest, ts} = pkt

      new_set = MapSet.delete(state.set, pkt)

      tree = Map.get(state.dest_map, dest, :gb_trees.empty())
      new_tree =
        case :gb_trees.lookup(ts, tree) do
          {:value, cnt} when cnt > 1 -> :gb_trees.update(ts, cnt - 1, tree)
          {:value, 1} -> :gb_trees.delete_any(ts, tree)
          :none -> tree
        end

      new_dest_map =
        if :gb_trees.is_empty(new_tree) do
          Map.delete(state.dest_map, dest)
        else
          Map.put(state.dest_map, dest, new_tree)
        end

      new_state = %{
        state |
        queue: q,
        set: new_set,
        dest_map: new_dest_map,
        size: state.size - 1
      }

      put_state(new_state)
      [src, dest, ts]
    end
  end

  @spec get_count(destination :: integer, start_time :: integer, end_time :: integer) :: integer
  def get_count(destination, start_time, end_time) do
    state = get_state()

    case Map.get(state.dest_map, destination) do
      nil -> 0
      tree ->
        iter = :gb_trees.iterator_from(start_time, tree)
        count_range(iter, end_time, 0)
    end
  end

  # Helper functions
  defp get_state do
    [{:state, state}] = :ets.lookup(:router_state, :state)
    state
  end

  defp put_state(state) do
    :ets.insert(:router_state, {:state, state})
  end

  defp count_range(iter, end_time, acc) do
    case :gb_trees.next(iter) do
      {:ok, {key, val}, next_iter} when key <= end_time ->
        count_range(next_iter, end_time, acc + val)

      _ ->
        acc
    end
  end
end
```
