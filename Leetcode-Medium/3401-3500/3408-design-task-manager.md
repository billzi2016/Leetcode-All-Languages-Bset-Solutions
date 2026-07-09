# 3408. Design Task Manager

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class TaskManager {
    struct Node {
        int priority;
        int userId;
        int taskId;
    };
    struct Cmp {
        bool operator()(const Node& a, const Node& b) const {
            if (a.priority != b.priority) return a.priority < b.priority; // max priority
            if (a.userId != b.userId)   return a.userId < b.userId;       // larger userId first
            return a.taskId < b.taskId;                                 // larger taskId first
        }
    };
    
    unordered_map<int, pair<int,int>> mp; // taskId -> {priority, userId}
    priority_queue<Node, vector<Node>, Cmp> pq;
public:
    TaskManager(vector<vector<int>>& tasks) {
        for (auto &t : tasks) {
            int userId = t[0], taskId = t[1], priority = t[2];
            mp[taskId] = {priority, userId};
            pq.push({priority, userId, taskId});
        }
    }
    
    void add(int userId, int taskId, int priority) {
        mp[taskId] = {priority, userId};
        pq.push({priority, userId, taskId});
    }
    
    void edit(int taskId, int newPriority) {
        auto it = mp.find(taskId);
        if (it == mp.end()) return;
        int userId = it->second.second;
        it->second.first = newPriority;
        pq.push({newPriority, userId, taskId});
    }
    
    void rmv(int taskId) {
        mp.erase(taskId);
    }
    
    int execTop() {
        while (!pq.empty()) {
            Node cur = pq.top();
            auto it = mp.find(cur.taskId);
            if (it == mp.end() ||
                it->second.first != cur.priority ||
                it->second.second != cur.userId) {
                pq.pop(); // stale entry
                continue;
            }
            int resUser = cur.userId;
            pq.pop();
            mp.erase(cur.taskId);
            return resUser;
        }
        return -1; // should not happen per problem guarantees
    }
};

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager* obj = new TaskManager(tasks);
 * obj->add(userId,taskId,priority);
 * obj->edit(taskId,newPriority);
 * obj->rmv(taskId);
 * int param_4 = obj->execTop();
 */
```

## Java

```java
import java.util.*;

class TaskManager {
    private static class Entry {
        int priority;
        int taskId;
        int userId;
        boolean valid;

        Entry(int userId, int taskId, int priority) {
            this.userId = userId;
            this.taskId = taskId;
            this.priority = priority;
            this.valid = true;
        }
    }

    private final PriorityQueue<Entry> heap;
    private final Map<Integer, Entry> map;

    public TaskManager(List<List<Integer>> tasks) {
        Comparator<Entry> cmp = (a, b) -> {
            if (a.priority != b.priority) {
                return Integer.compare(b.priority, a.priority); // higher priority first
            }
            return Integer.compare(a.taskId, b.taskId); // smaller taskId first
        };
        heap = new PriorityQueue<>(cmp);
        map = new HashMap<>();
        for (List<Integer> t : tasks) {
            int userId = t.get(0);
            int taskId = t.get(1);
            int priority = t.get(2);
            addInternal(userId, taskId, priority);
        }
    }

    private void addInternal(int userId, int taskId, int priority) {
        Entry e = new Entry(userId, taskId, priority);
        map.put(taskId, e);
        heap.offer(e);
    }

    public void add(int userId, int taskId, int priority) {
        addInternal(userId, taskId, priority);
    }

    public void edit(int taskId, int newPriority) {
        Entry old = map.get(taskId);
        if (old == null) return;
        old.valid = false;
        Entry e = new Entry(old.userId, taskId, newPriority);
        map.put(taskId, e);
        heap.offer(e);
    }

    public void rmv(int taskId) {
        Entry e = map.remove(taskId);
        if (e != null) {
            e.valid = false;
        }
    }

    public int execTop() {
        while (!heap.isEmpty()) {
            Entry e = heap.poll();
            if (!e.valid) continue;
            // ensure this is the current entry for the taskId
            Entry cur = map.get(e.taskId);
            if (cur != e) continue;
            map.remove(e.taskId);
            return e.userId;
        }
        return -1; // should not happen per problem guarantees
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager obj = new TaskManager(tasks);
 * obj.add(userId,taskId,priority);
 * obj.edit(taskId,newPriority);
 * obj.rmv(taskId);
 * int param_4 = obj.execTop();
 */
```

## Python

```python
class TaskManager(object):
    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        import heapq
        self.heap = []                     # stores (-priority, -taskId)
        self.info = {}                     # taskId -> (priority, userId)
        for userId, taskId, priority in tasks:
            self.info[taskId] = (priority, userId)
            heapq.heappush(self.heap, (-priority, -taskId))

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        import heapq
        self.info[taskId] = (priority, userId)
        heapq.heappush(self.heap, (-priority, -taskId))

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        import heapq
        if taskId in self.info:
            _, userId = self.info[taskId]
            self.info[taskId] = (newPriority, userId)
            heapq.heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        if taskId in self.info:
            del self.info[taskId]

    def execTop(self):
        """
        :rtype: int
        """
        import heapq
        while self.heap:
            p_neg, t_neg = self.heap[0]
            taskId = -t_neg
            if taskId not in self.info:
                heapq.heappop(self.heap)
                continue
            curPriority, userId = self.info[taskId]
            if -p_neg != curPriority:
                heapq.heappop(self.heap)
                continue
            # valid top task
            heapq.heappop(self.heap)
            del self.info[taskId]
            return userId
        return -1  # no tasks available
```

## Python3

```python
import heapq
from typing import List

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.heap = []  # elements are (-priority, userId, taskId)
        self.task_map = {}  # taskId -> (userId, priority)
        for userId, taskId, priority in tasks:
            self.task_map[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, userId, taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, userId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId not in self.task_map:
            return
        userId, _ = self.task_map[taskId]
        self.task_map[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, userId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        while self.heap:
            negPrio, userId, taskId = self.heap[0]
            if taskId not in self.task_map:
                heapq.heappop(self.heap)
                continue
            curUser, curPrio = self.task_map[taskId]
            if curUser != userId or curPrio != -negPrio:
                heapq.heappop(self.heap)
                continue
            # valid top task
            heapq.heappop(self.heap)
            del self.task_map[taskId]
            return userId
        return -1  # should not happen per problem constraints
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int userId;
    int taskId;
    long long priority;
} Node;

typedef struct {
    Node *heap;
    int size;
    int capacity;
    int *pos;          // index of taskId in heap, -1 if not present
} TaskManager;

/* compare two nodes: return 1 if a has higher priority than b,
   or same priority but smaller taskId (to make ordering deterministic) */
static int cmp(const Node *a, const Node *b) {
    if (a->priority != b->priority)
        return a->priority > b->priority;
    return a->taskId < b->taskId;
}

static void swapNodes(TaskManager *obj, int i, int j) {
    Node tmp = obj->heap[i];
    obj->heap[i] = obj->heap[j];
    obj->heap[j] = tmp;
    obj->pos[obj->heap[i].taskId] = i;
    obj->pos[obj->heap[j].taskId] = j;
}

static void siftUp(TaskManager *obj, int idx) {
    while (idx > 0) {
        int parent = (idx - 1) >> 1;
        if (cmp(&obj->heap[idx], &obj->heap[parent])) {
            swapNodes(obj, idx, parent);
            idx = parent;
        } else break;
    }
}

static void siftDown(TaskManager *obj, int idx) {
    while (1) {
        int left = (idx << 1) + 1;
        if (left >= obj->size) break;
        int right = left + 1;
        int best = left;
        if (right < obj->size && cmp(&obj->heap[right], &obj->heap[left]))
            best = right;
        if (cmp(&obj->heap[best], &obj->heap[idx])) {
            swapNodes(obj, idx, best);
            idx = best;
        } else break;
    }
}

static void ensureCapacity(TaskManager *obj) {
    if (obj->size < obj->capacity) return;
    int newCap = obj->capacity * 2 + 1;
    Node *newHeap = (Node *)realloc(obj->heap, sizeof(Node) * newCap);
    if (!newHeap) exit(1);
    obj->heap = newHeap;
    obj->capacity = newCap;
}

/* internal insert without duplicate check */
static void heapInsert(TaskManager *obj, int userId, int taskId, long long priority) {
    ensureCapacity(obj);
    int idx = obj->size;
    obj->heap[idx].userId = userId;
    obj->heap[idx].taskId = taskId;
    obj->heap[idx].priority = priority;
    obj->pos[taskId] = idx;
    obj->size++;
    siftUp(obj, idx);
}

/* public API */
TaskManager* taskManagerCreate(int** tasks, int tasksSize, int* tasksColSize) {
    TaskManager *obj = (TaskManager *)malloc(sizeof(TaskManager));
    obj->size = 0;
    obj->capacity = tasksSize > 0 ? tasksSize : 1;
    obj->heap = (Node *)malloc(sizeof(Node) * obj->capacity);
    int maxId = 100000; // per constraints
    obj->pos = (int *)malloc(sizeof(int) * (maxId + 1));
    for (int i = 0; i <= maxId; ++i) obj->pos[i] = -1;
    for (int i = 0; i < tasksSize; ++i) {
        int userId = tasks[i][0];
        int taskId = tasks[i][1];
        int priority = tasks[i][2];
        heapInsert(obj, userId, taskId, priority);
    }
    return obj;
}

void taskManagerAdd(TaskManager* obj, int userId, int taskId, int priority) {
    if (obj->pos[taskId] != -1) return; // assume unique, ignore if exists
    heapInsert(obj, userId, taskId, priority);
}

void taskManagerEdit(TaskManager* obj, int taskId, int newPriority) {
    int idx = obj->pos[taskId];
    if (idx == -1) return;
    long long old = obj->heap[idx].priority;
    obj->heap[idx].priority = newPriority;
    if (newPriority > old)
        siftUp(obj, idx);
    else
        siftDown(obj, idx);
}

void taskManagerRmv(TaskManager* obj, int taskId) {
    int idx = obj->pos[taskId];
    if (idx == -1) return;
    int lastIdx = obj->size - 1;
    if (idx != lastIdx) {
        swapNodes(obj, idx, lastIdx);
    }
    obj->pos[taskId] = -1;
    obj->size--;
    if (idx < obj->size) {
        siftUp(obj, idx);
        siftDown(obj, idx);
    }
}

int taskManagerExecTop(TaskManager* obj) {
    if (obj->size == 0) return -1;
    int userId = obj->heap[0].userId;
    int topTaskId = obj->heap[0].taskId;
    taskManagerRmv(obj, topTaskId);
    return userId;
}

void taskManagerFree(TaskManager* obj) {
    if (!obj) return;
    free(obj->heap);
    free(obj->pos);
    free(obj);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class TaskManager
{
    private struct Node
    {
        public int Priority;
        public int TaskId;
        public Node(int priority, int taskId)
        {
            Priority = priority;
            TaskId = taskId;
        }
    }

    private class NodeComparer : IComparer<Node>
    {
        public int Compare(Node a, Node b)
        {
            int cmp = b.Priority.CompareTo(a.Priority); // higher priority first
            if (cmp != 0) return cmp;
            return b.TaskId.CompareTo(a.TaskId); // larger taskId first
        }
    }

    private readonly SortedSet<Node> _set;
    private readonly Dictionary<int, (int userId, int priority)> _map;

    public TaskManager(IList<IList<int>> tasks)
    {
        _set = new SortedSet<Node>(new NodeComparer());
        _map = new Dictionary<int, (int, int)>();
        foreach (var t in tasks)
        {
            int userId = t[0];
            int taskId = t[1];
            int priority = t[2];
            _map[taskId] = (userId, priority);
            _set.Add(new Node(priority, taskId));
        }
    }

    public void Add(int userId, int taskId, int priority)
    {
        if (_map.ContainsKey(taskId)) return;
        _map[taskId] = (userId, priority);
        _set.Add(new Node(priority, taskId));
    }

    public void Edit(int taskId, int newPriority)
    {
        if (!_map.TryGetValue(taskId, out var info)) return;
        // remove old node
        _set.Remove(new Node(info.priority, taskId));
        // update
        _map[taskId] = (info.userId, newPriority);
        _set.Add(new Node(newPriority, taskId));
    }

    public void Rmv(int taskId)
    {
        if (!_map.TryGetValue(taskId, out var info)) return;
        _set.Remove(new Node(info.priority, taskId));
        _map.Remove(taskId);
    }

    public int ExecTop()
    {
        if (_set.Count == 0) return -1;
        Node top = _set.Min; // due to comparer, this is the highest priority
        _set.Remove(top);
        var info = _map[top.TaskId];
        _map.Remove(top.TaskId);
        return info.userId;
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager obj = new TaskManager(tasks);
 * obj.Add(userId,taskId,priority);
 * obj.Edit(taskId,newPriority);
 * obj.Rmv(taskId);
 * int param_4 = obj.ExecTop();
 */
```

## Javascript

```javascript
/**
 * @param {number[][]} tasks
 */
var TaskManager = function(tasks) {
    this.taskMap = new Map(); // taskId -> {userId, priority, time}
    this.heap = []; // max-heap of [priority, time, taskId]
    this.time = 0;

    const push = (node) => {
        this.heap.push(node);
        let i = this.heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this._compare(this.heap[i], this.heap[p]) <= 0) break;
            [this.heap[i], this.heap[p]] = [this.heap[p], this.heap[i]];
            i = p;
        }
    };

    for (const [userId, taskId, priority] of tasks) {
        const t = ++this.time;
        this.taskMap.set(taskId, { userId, priority, time: t });
        push([priority, t, taskId]);
    }

    // bind heap helper
    this._push = push;
};

/** internal compare: return positive if a > b */
TaskManager.prototype._compare = function(a, b) {
    if (a[0] !== b[0]) return a[0] - b[0];          // priority
    return a[1] - b[1];                              // time (larger is newer)
};

/** internal heap pop */
TaskManager.prototype._popHeap = function() {
    const heap = this.heap;
    if (heap.length === 0) return null;
    const top = heap[0];
    const last = heap.pop();
    if (heap.length > 0) {
        heap[0] = last;
        let i = 0;
        while (true) {
            let left = i * 2 + 1, right = left + 1, largest = i;
            if (left < heap.length && this._compare(heap[left], heap[largest]) > 0) largest = left;
            if (right < heap.length && this._compare(heap[right], heap[largest]) > 0) largest = right;
            if (largest === i) break;
            [heap[i], heap[largest]] = [heap[largest], heap[i]];
            i = largest;
        }
    }
    return top;
};

/** 
 * @param {number} userId 
 * @param {number} taskId 
 * @param {number} priority
 * @return {void}
 */
TaskManager.prototype.add = function(userId, taskId, priority) {
    const t = ++this.time;
    this.taskMap.set(taskId, { userId, priority, time: t });
    this._push([priority, t, taskId]);
};

/** 
 * @param {number} taskId 
 * @param {number} newPriority
 * @return {void}
 */
TaskManager.prototype.edit = function(taskId, newPriority) {
    if (!this.taskMap.has(taskId)) return;
    const info = this.taskMap.get(taskId);
    const t = ++this.time;
    info.priority = newPriority;
    info.time = t;
    // update map entry
    this.taskMap.set(taskId, info);
    this._push([newPriority, t, taskId]);
};

/** 
 * @param {number} taskId
 * @return {void}
 */
TaskManager.prototype.rmv = function(taskId) {
    this.taskMap.delete(taskId);
};

/**
 * @return {number}
 */
TaskManager.prototype.execTop = function() {
    while (this.heap.length > 0) {
        const top = this.heap[0];
        const [priority, time, taskId] = top;
        const info = this.taskMap.get(taskId);
        if (info && info.priority === priority && info.time === time) {
            // valid entry
            this._popHeap(); // remove from heap
            this.taskMap.delete(taskId); // execute -> remove task
            return info.userId;
        }
        // stale entry
        this._popHeap();
    }
    return -1; // no tasks available
};

/** 
 * Your TaskManager object will be instantiated and called as such:
 * var obj = new TaskManager(tasks)
 * obj.add(userId,taskId,priority)
 * obj.edit(taskId,newPriority)
 * obj.rmv(taskId)
 * var param_4 = obj.execTop()
 */
```

## Typescript

```typescript
class TaskManager {
    private heap: {priority: number, taskId: number, userId: number}[] = [];
    private pos: Map<number, number> = new Map(); // taskId -> index in heap

    constructor(tasks: number[][]) {
        for (const [userId, taskId, priority] of tasks) {
            this._push({priority, taskId, userId});
        }
    }

    add(userId: number, taskId: number, priority: number): void {
        this._push({priority, taskId, userId});
    }

    edit(taskId: number, newPriority: number): void {
        const idx = this.pos.get(taskId);
        if (idx === undefined) return;
        const old = this.heap[idx];
        const oldPriority = old.priority;
        old.priority = newPriority;
        if (newPriority > oldPriority) {
            this._heapifyUp(idx);
        } else if (newPriority < oldPriority) {
            this._heapifyDown(idx);
        }
    }

    rmv(taskId: number): void {
        const idx = this.pos.get(taskId);
        if (idx === undefined) return;
        const lastIdx = this.heap.length - 1;
        this._swap(idx, lastIdx);
        this.heap.pop();
        this.pos.delete(taskId);
        if (idx < this.heap.length) {
            this._heapifyUp(idx);
            this._heapifyDown(idx);
        }
    }

    execTop(): number {
        if (this.heap.length === 0) return -1;
        const top = this.heap[0];
        const lastIdx = this.heap.length - 1;
        this._swap(0, lastIdx);
        this.heap.pop();
        this.pos.delete(top.taskId);
        if (this.heap.length > 0) {
            this._heapifyDown(0);
        }
        return top.userId;
    }

    // ----- heap helpers -----
    private _push(node: {priority: number, taskId: number, userId: number}): void {
        const idx = this.heap.length;
        this.heap.push(node);
        this.pos.set(node.taskId, idx);
        this._heapifyUp(idx);
    }

    private _compare(a: {priority: number, taskId: number}, b: {priority: number, taskId: number}): boolean {
        if (a.priority !== b.priority) return a.priority > b.priority;
        // tie-breaker: smaller taskId wins
        return a.taskId < b.taskId;
    }

    private _heapifyUp(idx: number): void {
        while (idx > 0) {
            const parent = (idx - 1) >> 1;
            if (this._compare(this.heap[idx], this.heap[parent])) {
                this._swap(idx, parent);
                idx = parent;
            } else break;
        }
    }

    private _heapifyDown(idx: number): void {
        const n = this.heap.length;
        while (true) {
            let left = idx * 2 + 1;
            let right = left + 1;
            let largest = idx;

            if (left < n && this._compare(this.heap[left], this.heap[largest])) {
                largest = left;
            }
            if (right < n && this._compare(this.heap[right], this.heap[largest])) {
                largest = right;
            }
            if (largest !== idx) {
                this._swap(idx, largest);
                idx = largest;
            } else break;
        }
    }

    private _swap(i: number, j: number): void {
        const tmp = this.heap[i];
        this.heap[i] = this.heap[j];
        this.heap[j] = tmp;
        this.pos.set(this.heap[i].taskId, i);
        this.pos.set(this.heap[j].taskId, j);
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * var obj = new TaskManager(tasks)
 * obj.add(userId,taskId,priority)
 * obj.edit(taskId,newPriority)
 * obj.rmv(taskId)
 * var param_4 = obj.execTop()
 */
```

## Php

```php
class TaskManager {
    private $tasks = []; // taskId => ['user'=>int,'priority'=>int]
    private $heap;

    /**
     * @param Integer[][] $tasks
     */
    function __construct($tasks) {
        $this->heap = new class extends SplPriorityQueue {
            public function compare($p1, $p2) {
                if ($p1['priority'] === $p2['priority']) {
                    if ($p1['taskId'] === $p2['taskId']) return 0;
                    // smaller taskId has higher priority when priorities are equal
                    return ($p1['taskId'] < $p2['taskId']) ? 1 : -1;
                }
                return ($p1['priority'] > $p2['priority']) ? 1 : -1;
            }
        };
        $this->heap->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        foreach ($tasks as $t) {
            [$userId, $taskId, $priority] = $t;
            $this->tasks[$taskId] = ['user' => $userId, 'priority' => $priority];
            $this->heap->insert($taskId, ['priority' => $priority, 'taskId' => $taskId]);
        }
    }

    /**
     * @param Integer $userId
     * @param Integer $taskId
     * @param Integer $priority
     * @return NULL
     */
    function add($userId, $taskId, $priority) {
        $this->tasks[$taskId] = ['user' => $userId, 'priority' => $priority];
        $this->heap->insert($taskId, ['priority' => $priority, 'taskId' => $taskId]);
    }

    /**
     * @param Integer $taskId
     * @param Integer $newPriority
     * @return NULL
     */
    function edit($taskId, $newPriority) {
        if (!isset($this->tasks[$taskId])) return;
        $this->tasks[$taskId]['priority'] = $newPriority;
        $this->heap->insert($taskId, ['priority' => $newPriority, 'taskId' => $taskId]);
    }

    /**
     * @param Integer $taskId
     * @return NULL
     */
    function rmv($taskId) {
        unset($this->tasks[$taskId]);
    }

    /**
     * @return Integer
     */
    function execTop() {
        while (!$this->heap->isEmpty()) {
            $elem = $this->heap->extract();
            $tid = $elem['data'];
            if (!isset($this->tasks[$tid])) continue;
            $curPriority = $this->tasks[$tid]['priority'];
            if ($curPriority !== $elem['priority']['priority']) {
                // stale entry
                continue;
            }
            $userId = $this->tasks[$tid]['user'];
            unset($this->tasks[$tid]);
            return $userId;
        }
        return -1; // should not happen per constraints
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * $obj = new TaskManager($tasks);
 * $obj->add($userId, $taskId, $priority);
 * $obj->edit($taskId, $newPriority);
 * $obj->rmv($taskId);
 * $ret = $obj->execTop();
 */
```

## Swift

```swift
class TaskManager {
    struct Node {
        var priority: Int
        var taskId: Int
        var userId: Int
    }
    
    private var heap: [Node] = []
    private var map: [Int: (priority: Int, userId: Int)] = [:]
    
    init(_ tasks: [[Int]]) {
        for t in tasks {
            let userId = t[0], taskId = t[1], priority = t[2]
            map[taskId] = (priority, userId)
            heapAppend(Node(priority: priority, taskId: taskId, userId: userId))
        }
    }
    
    func add(_ userId: Int, _ taskId: Int, _ priority: Int) {
        map[taskId] = (priority, userId)
        heapAppend(Node(priority: priority, taskId: taskId, userId: userId))
    }
    
    func edit(_ taskId: Int, _ newPriority: Int) {
        if let info = map[taskId] {
            map[taskId] = (newPriority, info.userId)
            heapAppend(Node(priority: newPriority, taskId: taskId, userId: info.userId))
        }
    }
    
    func rmv(_ taskId: Int) {
        map.removeValue(forKey: taskId)
    }
    
    func execTop() -> Int {
        while !heap.isEmpty {
            let top = heap[0]
            if let cur = map[top.taskId],
               cur.priority == top.priority && cur.userId == top.userId {
                _ = heapRemoveRoot()
                map.removeValue(forKey: top.taskId)
                return top.userId
            } else {
                _ = heapRemoveRoot()
            }
        }
        return -1
    }
    
    // MARK: - Heap helpers
    
    private func higher(_ a: Node, _ b: Node) -> Bool {
        if a.priority != b.priority { return a.priority > b.priority }
        return a.taskId < b.taskId
    }
    
    private func heapAppend(_ node: Node) {
        heap.append(node)
        siftUp(heap.count - 1)
    }
    
    private func heapRemoveRoot() -> Node? {
        guard !heap.isEmpty else { return nil }
        let root = heap[0]
        let last = heap.removeLast()
        if !heap.isEmpty {
            heap[0] = last
            siftDown(0)
        }
        return root
    }
    
    private func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) / 2
            if higher(heap[child], heap[parent]) {
                heap.swapAt(child, parent)
                child = parent
            } else { break }
        }
    }
    
    private func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var candidate = parent
            if left < heap.count && higher(heap[left], heap[candidate]) {
                candidate = left
            }
            if right < heap.count && higher(heap[right], heap[candidate]) {
                candidate = right
            }
            if candidate == parent { break }
            heap.swapAt(parent, candidate)
            parent = candidate
        }
    }
}
```

## Kotlin

```kotlin
class TaskManager(tasks: List<List<Int>>) {
    private data class Info(var userId: Int, var priority: Int)
    private data class Node(val priority: Int, val taskId: Int)

    private val map = HashMap<Int, Info>()
    private val set = java.util.TreeSet<Node>(java.util.Comparator { a, b ->
        if (a.priority != b.priority) {
            // higher priority first
            b.priority - a.priority
        } else {
            a.taskId - b.taskId
        }
    })

    init {
        for (t in tasks) {
            val userId = t[0]
            val taskId = t[1]
            val priority = t[2]
            map[taskId] = Info(userId, priority)
            set.add(Node(priority, taskId))
        }
    }

    fun add(userId: Int, taskId: Int, priority: Int) {
        if (map.containsKey(taskId)) return
        map[taskId] = Info(userId, priority)
        set.add(Node(priority, taskId))
    }

    fun edit(taskId: Int, newPriority: Int) {
        val info = map[taskId] ?: return
        set.remove(Node(info.priority, taskId))
        info.priority = newPriority
        set.add(Node(newPriority, taskId))
    }

    fun rmv(taskId: Int) {
        val info = map.remove(taskId) ?: return
        set.remove(Node(info.priority, taskId))
    }

    fun execTop(): Int {
        val node = set.pollFirst()
        val info = map.remove(node.taskId)!!
        return info.userId
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * var obj = TaskManager(tasks)
 * obj.add(userId,taskId,priority)
 * obj.edit(taskId,newPriority)
 * obj.rmv(taskId)
 * var param_4 = obj.execTop()
 */
```

## Dart

```dart
class TaskManager {
  // Mapping from taskId to [userId, priority]
  final Map<int, List<int>> _taskMap = {};
  // Max-heap stored as a list
  final List<_Node> _heap = [];
  int _seq = 0; // insertion sequence for tie-breaking if needed

  TaskManager(List<List<int>> tasks) {
    for (var t in tasks) {
      int userId = t[0];
      int taskId = t[1];
      int priority = t[2];
      _addInternal(userId, taskId, priority);
    }
  }

  void add(int userId, int taskId, int priority) {
    _addInternal(userId, taskId, priority);
  }

  void edit(int taskId, int newPriority) {
    var info = _taskMap[taskId];
    if (info == null) return; // task does not exist
    int userId = info[0];
    // update map
    _taskMap[taskId] = [userId, newPriority];
    // push new entry to heap
    _push(_Node(newPriority, userId, taskId, _seq++));
  }

  void rmv(int taskId) {
    _taskMap.remove(taskId);
    // stale entries will be ignored during execTop
  }

  int execTop() {
    while (_heap.isNotEmpty) {
      var top = _heap[0];
      var info = _taskMap[top.taskId];
      if (info == null || info[1] != top.priority) {
        // stale entry, remove it
        _pop();
        continue;
      }
      // valid top task
      _pop(); // remove from heap
      _taskMap.remove(top.taskId); // execute -> delete
      return top.userId;
    }
    return -1; // no tasks available
  }

  // Internal helper to add a task without extra checks
  void _addInternal(int userId, int taskId, int priority) {
    _taskMap[taskId] = [userId, priority];
    _push(_Node(priority, userId, taskId, _seq++));
  }

  // Heap operations (max-heap)
  void _push(_Node node) {
    _heap.add(node);
    int i = _heap.length - 1;
    while (i > 0) {
      int p = (i - 1) >> 1;
      if (_compare(_heap[i], _heap[p])) {
        var tmp = _heap[i];
        _heap[i] = _heap[p];
        _heap[p] = tmp;
        i = p;
      } else {
        break;
      }
    }
  }

  _Node _pop() {
    int n = _heap.length - 1;
    var top = _heap[0];
    if (n == 0) {
      _heap.removeLast();
      return top;
    }
    _heap[0] = _heap[n];
    _heap.removeLast();
    _siftDown(0);
    return top;
  }

  void _siftDown(int i) {
    int n = _heap.length;
    while (true) {
      int left = i * 2 + 1;
      int right = left + 1;
      int largest = i;

      if (left < n && _compare(_heap[left], _heap[largest])) {
        largest = left;
      }
      if (right < n && _compare(_heap[right], _heap[largest])) {
        largest = right;
      }
      if (largest == i) break;
      var tmp = _heap[i];
      _heap[i] = _heap[largest];
      _heap[largest] = tmp;
      i = largest;
    }
  }

  // Return true if a should be above b in max-heap
  bool _compare(_Node a, _Node b) {
    if (a.priority != b.priority) return a.priority > b.priority;
    if (a.userId != b.userId) return a.userId > b.userId;
    return a.seq > b.seq; // more recent wins if all else equal
  }
}

class _Node {
  final int priority;
  final int userId;
  final int taskId;
  final int seq;
  _Node(this.priority, this.userId, this.taskId, this.seq);
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager obj = TaskManager(tasks);
 * obj.add(userId,taskId,priority);
 * obj.edit(taskId,newPriority);
 * obj.rmv(taskId);
 * int param4 = obj.execTop();
 */
```

## Golang

```go
package main

import (
	"container/heap"
)

type taskInfo struct {
	userId   int
	priority int
}

type entry struct {
	priority int
	taskId   int
	userId   int
}

// max-heap based on priority, then smaller taskId
type priorityQueue []entry

func (pq priorityQueue) Len() int { return len(pq) }
func (pq priorityQueue) Less(i, j int) bool {
	if pq[i].priority != pq[j].priority {
		return pq[i].priority > pq[j].priority
	}
	return pq[i].taskId < pq[j].taskId
}
func (pq priorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }

func (pq *priorityQueue) Push(x interface{}) {
	*pq = append(*pq, x.(entry))
}

func (pq *priorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	it := old[n-1]
	*pq = old[:n-1]
	return it
}

// TaskManager definition
type TaskManager struct {
	tasks map[int]*taskInfo // taskId -> info
	pq    priorityQueue
}

func Constructor(tasks [][]int) TaskManager {
	tm := TaskManager{
		tasks: make(map[int]*taskInfo),
		pq:    make(priorityQueue, 0),
	}
	for _, t := range tasks {
		if len(t) != 3 {
			continue
		}
		userId, taskId, priority := t[0], t[1], t[2]
		tm.tasks[taskId] = &taskInfo{userId: userId, priority: priority}
		heap.Push(&tm.pq, entry{priority: priority, taskId: taskId, userId: userId})
	}
	heap.Init(&tm.pq)
	return tm
}

func (this *TaskManager) Add(userId int, taskId int, priority int) {
	if _, exists := this.tasks[taskId]; exists {
		return
	}
	this.tasks[taskId] = &taskInfo{userId: userId, priority: priority}
	heap.Push(&this.pq, entry{priority: priority, taskId: taskId, userId: userId})
}

func (this *TaskManager) Edit(taskId int, newPriority int) {
	if info, ok := this.tasks[taskId]; ok {
		info.priority = newPriority
		heap.Push(&this.pq, entry{priority: newPriority, taskId: taskId, userId: info.userId})
	}
}

func (this *TaskManager) Rmv(taskId int) {
	delete(this.tasks, taskId)
}

func (this *TaskManager) ExecTop() int {
	for this.pq.Len() > 0 {
		top := heap.Pop(&this.pq).(entry)
		if info, ok := this.tasks[top.taskId]; ok && info.priority == top.priority {
			delete(this.tasks, top.taskId)
			return top.userId
		}
	}
	return -1
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * obj := Constructor(tasks);
 * obj.Add(userId,taskId,priority);
 * obj.Edit(taskId,newPriority);
 * obj.Rmv(taskId);
 * param_4 := obj.ExecTop();
 */
```

## Ruby

```ruby
class TaskManager
  def initialize(tasks)
    @task_info = {} # task_id => [user_id, priority]
    @heap = []      # max-heap of [priority, task_id]

    tasks.each do |u, t, p|
      @task_info[t] = [u, p]
      heap_push(p, t)
    end
  end

  def add(user_id, task_id, priority)
    @task_info[task_id] = [user_id, priority]
    heap_push(priority, task_id)
  end

  def edit(task_id, new_priority)
    info = @task_info[task_id]
    return unless info
    user_id = info[0]
    @task_info[task_id] = [user_id, new_priority]
    heap_push(new_priority, task_id)
  end

  def rmv(task_id)
    @task_info.delete(task_id)
  end

  def exec_top
    while !@heap.empty?
      pr, tid = @heap[0]
      info = @task_info[tid]
      if info && info[1] == pr
        return info[0]
      else
        heap_pop_invalid
      end
    end
    -1
  end

  private

  def compare(a, b)
    # a and b are [priority, task_id]
    if a[0] != b[0]
      a[0] <=> b[0]
    else
      a[1] <=> b[1]
    end
  end

  def heap_push(priority, task_id)
    @heap << [priority, task_id]
    i = @heap.size - 1
    while i > 0
      parent = (i - 1) / 2
      break unless compare(@heap[i], @heap[parent]) > 0
      @heap[i], @heap[parent] = @heap[parent], @heap[i]
      i = parent
    end
  end

  def heap_pop_invalid
    return if @heap.empty?
    last = @heap.pop
    return if @heap.empty?
    @heap[0] = last
    i = 0
    n = @heap.size
    loop do
      left = i * 2 + 1
      right = left + 1
      largest = i
      if left < n && compare(@heap[left], @heap[largest]) > 0
        largest = left
      end
      if right < n && compare(@heap[right], @heap[largest]) > 0
        largest = right
      end
      break if largest == i
      @heap[i], @heap[largest] = @heap[largest], @heap[i]
      i = largest
    end
  end
end
```

## Scala

```scala
class TaskManager(_tasks: List[List[Int]]) {
  import scala.collection.mutable

  private case class Entry(priority: Int, userId: Int, taskId: Int)

  private implicit val entryOrdering: Ordering[Entry] =
    Ordering.by((e: Entry) => (e.priority, e.userId))

  private val pq = mutable.PriorityQueue.empty[Entry]
  private val taskMap = mutable.Map[Int, (Int, Int)]() // taskId -> (priority, userId)

  _tasks.foreach {
    case List(userId, taskId, priority) =>
      taskMap(taskId) = (priority, userId)
      pq.enqueue(Entry(priority, userId, taskId))
    case _ => ()
  }

  def add(userId: Int, taskId: Int, priority: Int): Unit = {
    if (!taskMap.contains(taskId)) {
      taskMap(taskId) = (priority, userId)
      pq.enqueue(Entry(priority, userId, taskId))
    }
  }

  def edit(taskId: Int, newPriority: Int): Unit = {
    taskMap.get(taskId).foreach { case (_, userId) =>
      taskMap(taskId) = (newPriority, userId)
      pq.enqueue(Entry(newPriority, userId, taskId))
    }
  }

  def rmv(taskId: Int): Unit = {
    taskMap.remove(taskId)
  }

  def execTop(): Int = {
    while (pq.nonEmpty) {
      val top = pq.head
      taskMap.get(top.taskId) match {
        case Some((p, u)) if p == top.priority && u == top.userId =>
          pq.dequeue()
          taskMap.remove(top.taskId)
          return top.userId
        case _ => pq.dequeue() // stale entry
      }
    }
    -1
  }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * val obj = new TaskManager(tasks)
 * obj.add(userId,taskId,priority)
 * obj.edit(taskId,newPriority)
 * obj.rmv(taskId)
 * val param_4 = obj.execTop()
 */
```

## Rust

```rust
use std::collections::{BinaryHeap, HashMap};
use std::cmp::Ordering;

#[derive(Clone, Copy)]
struct Entry {
    priority: i32,
    user_id: i32,
    task_id: i32,
}

impl PartialEq for Entry {
    fn eq(&self, other: &Self) -> bool {
        self.priority == other.priority
            && self.user_id == other.user_id
            && self.task_id == other.task_id
    }
}
impl Eq for Entry {}

impl PartialOrd for Entry {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Entry {
    fn cmp(&self, other: &Self) -> Ordering {
        match self.priority.cmp(&other.priority) {
            Ordering::Equal => match self.user_id.cmp(&other.user_id) {
                Ordering::Equal => self.task_id.cmp(&other.task_id),
                ord => ord,
            },
            ord => ord,
        }
    }
}

struct TaskManager {
    map: HashMap<i32, (i32, i32)>, // task_id -> (user_id, priority)
    heap: BinaryHeap<Entry>,
}

impl TaskManager {
    fn new(tasks: Vec<Vec<i32>>) -> Self {
        let mut map = HashMap::new();
        let mut heap = BinaryHeap::new();
        for t in tasks {
            let user_id = t[0];
            let task_id = t[1];
            let priority = t[2];
            map.insert(task_id, (user_id, priority));
            heap.push(Entry {
                priority,
                user_id,
                task_id,
            });
        }
        TaskManager { map, heap }
    }

    fn add(&mut self, user_id: i32, task_id: i32, priority: i32) {
        self.map.insert(task_id, (user_id, priority));
        self.heap.push(Entry {
            priority,
            user_id,
            task_id,
        });
    }

    fn edit(&mut self, task_id: i32, new_priority: i32) {
        if let Some(&(user_id, _)) = self.map.get(&task_id) {
            self.map.insert(task_id, (user_id, new_priority));
            self.heap.push(Entry {
                priority: new_priority,
                user_id,
                task_id,
            });
        }
    }

    fn rmv(&mut self, task_id: i32) {
        self.map.remove(&task_id);
    }

    fn exec_top(&mut self) -> i32 {
        while let Some(entry) = self.heap.pop() {
            if let Some(&(user_id, priority)) = self.map.get(&entry.task_id) {
                if user_id == entry.user_id && priority == entry.priority {
                    self.map.remove(&entry.task_id);
                    return entry.user_id;
                }
            }
        }
        -1
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * let obj = TaskManager::new(tasks);
 * obj.add(userId, taskId, priority);
 * obj.edit(taskId, newPriority);
 * obj.rmv(taskId);
 * let ret_4: i32 = obj.exec_top();
 */
```

## Racket

```racket
(struct heap-entry (priority task-id user-id) #:transparent)

(define task-manager%
  (class object%
    (super-new)
    
    (init-field tasks)
    
    ;; internal data structures
    (define task-map (make-hash))          ; task-id -> (list user-id priority)
    (define heap (make-vector 4))          ; dynamic array for max-heap
    (define size 0)                       ; current number of elements
    
    ;; comparison: higher priority first, tie‑break by larger task-id
    (define (higher? a b)
      (or (> (heap-entry-priority a) (heap-entry-priority b))
          (and (= (heap-entry-priority a) (heap-entry-priority b))
               (> (heap-entry-task-id a) (heap-entry-task-id b)))))
    
    (define (swap i j)
      (let ((tmp (vector-ref heap i)))
        (vector-set! heap i (vector-ref heap j))
        (vector-set! heap j tmp)))
    
    (define (sift-up idx)
      (let loop ((i idx))
        (when (> i 0)
          (define parent (quotient (- i 1) 2))
          (when (higher? (vector-ref heap i) (vector-ref heap parent))
            (swap i parent)
            (loop parent)))))
    
    (define (sift-down idx)
      (let loop ((i idx))
        (define left (+ (* 2 i) 1))
        (define right (+ left 1))
        (define largest i)
        (when (and (< left size) (higher? (vector-ref heap left) (vector-ref heap largest)))
          (set! largest left))
        (when (and (< right size) (higher? (vector-ref heap right) (vector-ref heap largest)))
          (set! largest right))
        (if (= largest i)
            (void)
            (begin
              (swap i largest)
              (loop largest)))))
    
    (define (ensure-capacity)
      (when (= size (vector-length heap))
        (define new-cap (* 2 (max 1 size)))
        (set! heap (vector-append heap (make-vector new-cap)))))
    
    (define (push-entry e)
      (ensure-capacity)
      (vector-set! heap size e)
      (set! size (+ size 1))
      (sift-up (- size 1)))
    
    (define (pop-root)
      (when (> size 0)
        (define top (vector-ref heap 0))
        (set! size (- size 1))
        (if (= size 0)
            (void)
            (begin
              (vector-set! heap 0 (vector-ref heap size))
              (sift-down 0)))
        top))
    
    ;; initialize with given tasks
    (for-each (lambda (t)
                (define user-id (list-ref t 0))
                (define task-id (list-ref t 1))
                (define priority (list-ref t 2))
                (hash-set! task-map task-id (list user-id priority))
                (push-entry (heap-entry priority task-id user-id)))
              tasks)
    
    ;; public API
    (define/public (add user-id task-id priority)
      (hash-set! task-map task-id (list user-id priority))
      (push-entry (heap-entry priority task-id user-id)))
    
    (define/public (edit task-id new-priority)
      (define val (hash-ref task-map task-id #f))
      (when val
        (define user-id (first val))
        (hash-set! task-map task-id (list user-id new-priority))
        (push-entry (heap-entry new-priority task-id user-id))))
    
    (define/public (rmv task-id)
      (hash-remove! task-map task-id))
    
    (define/public (exec-top)
      (let loop ()
        (when (> size 0)
          (define e (vector-ref heap 0))
          (define stored (hash-ref task-map (heap-entry-task-id e) #f))
          (if (and stored (= (second stored) (heap-entry-priority e)))
              (begin
                (hash-remove! task-map (heap-entry-task-id e))
                (pop-root)
                (heap-entry-user-id e))
              (begin
                (pop-root)
                (loop))))))
    ))
```

## Erlang

```erlang
-spec task_manager_init_(Tasks :: [[integer()]]) -> any().
task_manager_init_(Tasks) ->
    put(task_tree, gb_trees:empty()),
    put(task_map, #{}),
    lists:foreach(fun([UserId, TaskId, Priority]) ->
        add_task(UserId, TaskId, Priority)
    end, Tasks).

-spec task_manager_add(UserId :: integer(), TaskId :: integer(), Priority :: integer()) -> any().
task_manager_add(UserId, TaskId, Priority) ->
    add_task(UserId, TaskId, Priority).

-spec task_manager_edit(TaskId :: integer(), NewPriority :: integer()) -> any().
task_manager_edit(TaskId, NewPriority) ->
    Map = get(task_map),
    case maps:find(TaskId, Map) of
        error -> ok;
        {ok, {UserId, OldPri}} ->
            Tree = get(task_tree),
            OldKey = {-OldPri, -TaskId},
            TmpTree = gb_trees:delete(OldKey, Tree),
            NewKey = {-NewPriority, -TaskId},
            NewTree = gb_trees:insert(NewKey, UserId, TmpTree),
            NewMap = maps:put(TaskId, {UserId, NewPriority}, Map),
            put(task_tree, NewTree),
            put(task_map, NewMap)
    end.

-spec task_manager_rmv(TaskId :: integer()) -> any().
task_manager_rmv(TaskId) ->
    Map = get(task_map),
    case maps:find(TaskId, Map) of
        error -> ok;
        {ok, {UserId, Pri}} ->
            Tree = get(task_tree),
            Key = {-Pri, -TaskId},
            NewTree = gb_trees:delete(Key, Tree),
            NewMap = maps:remove(TaskId, Map),
            put(task_tree, NewTree),
            put(task_map, NewMap)
    end.

-spec task_manager_exec_top() -> integer().
task_manager_exec_top() ->
    Tree = get(task_tree),
    case gb_trees:is_empty(Tree) of
        true -> -1;
        false ->
            {_Key, UserId} = gb_trees:smallest(Tree),
            UserId
    end.

%% internal helper
add_task(UserId, TaskId, Priority) ->
    Tree = get(task_tree),
    Map = get(task_map),
    Key = {-Priority, -TaskId},
    NewTree = gb_trees:insert(Key, UserId, Tree),
    NewMap = maps:put(TaskId, {UserId, Priority}, Map),
    put(task_tree, NewTree),
    put(task_map, NewMap).
```

## Elixir

```elixir
defmodule TaskManager do
  @spec init_(tasks :: [[integer]]) :: any
  def init_(tasks) do
    # Delete existing tables if they exist
    (if :ets.whereis(:task_info) != :undefined, do: :ets.delete(:task_info))
    (if :ets.whereis(:priority_idx) != :undefined, do: :ets.delete(:priority_idx))

    # Create ETS tables
    :ets.new(:task_info, [:named_table, :public, read_concurrency: true])
    :ets.new(:priority_idx, [:named_table, :ordered_set, :public, read_concurrency: true])

    Enum.each(tasks, fn [user_id, task_id, priority] ->
      :ets.insert(:task_info, {task_id, {user_id, priority}})
      key = {-priority, task_id}
      :ets.insert(:priority_idx, {key, user_id})
    end)

    nil
  end

  @spec add(user_id :: integer, task_id :: integer, priority :: integer) :: any
  def add(user_id, task_id, priority) do
    :ets.insert(:task_info, {task_id, {user_id, priority}})
    key = {-priority, task_id}
    :ets.insert(:priority_idx, {key, user_id})
    nil
  end

  @spec edit(task_id :: integer, new_priority :: integer) :: any
  def edit(task_id, new_priority) do
    case :ets.lookup(:task_info, task_id) do
      [{^task_id, {user_id, old_priority}}] ->
        old_key = {-old_priority, task_id}
        :ets.delete(:priority_idx, old_key)

        new_key = {-new_priority, task_id}
        :ets.insert(:priority_idx, {new_key, user_id})
        :ets.insert(:task_info, {task_id, {user_id, new_priority}})
      _ ->
        :ok
    end

    nil
  end

  @spec rmv(task_id :: integer) :: any
  def rmv(task_id) do
    case :ets.lookup(:task_info, task_id) do
      [{^task_id, {_user_id, priority}}] ->
        key = {-priority, task_id}
        :ets.delete(:priority_idx, key)
        :ets.delete(:task_info, task_id)
      _ -> :ok
    end

    nil
  end

  @spec exec_top() :: integer
  def exec_top() do
    case :ets.first(:priority_idx) do
      :"$end_of_table" ->
        -1

      key ->
        [{^key, user_id}] = :ets.lookup(:priority_idx, key)
        {_neg_pri, task_id} = key
        :ets.delete(:priority_idx, key)
        :ets.delete(:task_info, task_id)
        user_id
    end
  end
end
```
