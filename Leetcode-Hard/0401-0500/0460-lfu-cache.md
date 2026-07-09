# 0460. LFU Cache

## Cpp

```cpp
class LFUCache {
private:
    struct Node {
        int value;
        int freq;
        std::list<int>::iterator it;
    };
    
    int capacity_;
    int minFreq_;
    std::unordered_map<int, Node> keyNode_;                 // key -> node
    std::unordered_map<int, std::list<int>> freqList_;      // freq -> list of keys (LRU order)
    
    void increaseFreq(int key) {
        auto &node = keyNode_[key];
        int curFreq = node.freq;
        
        // remove from current frequency list
        freqList_[curFreq].erase(node.it);
        if (freqList_[curFreq].empty()) {
            freqList_.erase(curFreq);
            if (minFreq_ == curFreq) ++minFreq_;
        }
        
        // add to next frequency list
        int newFreq = ++node.freq;
        freqList_[newFreq].push_back(key);
        node.it = std::prev(freqList_[newFreq].end());
    }
    
public:
    LFUCache(int capacity) : capacity_(capacity), minFreq_(0) {}
    
    int get(int key) {
        if (capacity_ == 0 || keyNode_.find(key) == keyNode_.end())
            return -1;
        increaseFreq(key);
        return keyNode_[key].value;
    }
    
    void put(int key, int value) {
        if (capacity_ == 0) return;
        
        auto it = keyNode_.find(key);
        if (it != keyNode_.end()) {
            // update existing key
            it->second.value = value;
            increaseFreq(key);
            return;
        }
        
        if ((int)keyNode_.size() >= capacity_) {
            // evict least frequently used and least recently used within that freq
            int evictKey = freqList_[minFreq_].front();
            freqList_[minFreq_].pop_front();
            if (freqList_[minFreq_].empty())
                freqList_.erase(minFreq_);
            keyNode_.erase(evictKey);
        }
        
        // insert new key with freq 1
        minFreq_ = 1;
        freqList_[1].push_back(key);
        Node node{value, 1, std::prev(freqList_[1].end())};
        keyNode_[key] = node;
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```

## Java

```java
import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.Map;

class LFUCache {
    private static class Node {
        int key, value, freq;
        Node(int k, int v) {
            key = k;
            value = v;
            freq = 1;
        }
    }

    private final int capacity;
    private int minFreq;
    private final Map<Integer, Node> cache;                 // key -> node
    private final Map<Integer, LinkedHashSet<Integer>> freqMap; // freq -> keys (ordered by recency)

    public LFUCache(int capacity) {
        this.capacity = capacity;
        this.minFreq = 0;
        this.cache = new HashMap<>();
        this.freqMap = new HashMap<>();
    }

    public int get(int key) {
        Node node = cache.get(key);
        if (node == null) return -1;

        // Remove from current frequency list
        LinkedHashSet<Integer> oldSet = freqMap.get(node.freq);
        oldSet.remove(key);
        if (oldSet.isEmpty()) {
            freqMap.remove(node.freq);
            if (minFreq == node.freq) {
                minFreq++;
            }
        }

        // Add to next frequency list
        node.freq++;
        freqMap.computeIfAbsent(node.freq, k -> new LinkedHashSet<>()).add(key);

        return node.value;
    }

    public void put(int key, int value) {
        if (capacity == 0) return;

        Node existing = cache.get(key);
        if (existing != null) {
            existing.value = value;
            get(key); // update frequency
            return;
        }

        if (cache.size() == capacity) {
            LinkedHashSet<Integer> minFreqSet = freqMap.get(minFreq);
            int evictKey = minFreqSet.iterator().next();
            minFreqSet.remove(evictKey);
            if (minFreqSet.isEmpty()) {
                freqMap.remove(minFreq);
            }
            cache.remove(evictKey);
        }

        Node newNode = new Node(key, value);
        cache.put(key, newNode);
        minFreq = 1;
        freqMap.computeIfAbsent(1, k -> new LinkedHashSet<>()).add(key);
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
```

## Python

```python
import collections

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.minfreq = 0
        self.key2valfreq = {}               # key -> (value, freq)
        self.freq2keys = collections.defaultdict(collections.OrderedDict)  # freq -> keys in LRU order

    def _update(self, key):
        value, freq = self.key2valfreq[key]
        # remove from current frequency list
        del self.freq2keys[freq][key]
        if not self.freq2keys[freq]:
            del self.freq2keys[freq]
            if self.minfreq == freq:
                self.minfreq += 1
        # add to next frequency list
        newfreq = freq + 1
        self.key2valfreq[key] = (value, newfreq)
        self.freq2keys[newfreq][key] = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2valfreq:
            return -1
        self._update(key)
        return self.key2valfreq[key][0]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return
        if key in self.key2valfreq:
            # update value and increase frequency
            _, freq = self.key2valfreq[key]
            self.key2valfreq[key] = (value, freq)
            self._update(key)
            return
        if len(self.key2valfreq) >= self.capacity:
            # evict least frequently used key (LRU within that freq)
            evict_key, _ = self.freq2keys[self.minfreq].popitem(last=False)
            del self.key2valfreq[evict_key]
            if not self.freq2keys[self.minfreq]:
                del self.freq2keys[self.minfreq]
        # insert new key with freq 1
        self.key2valfreq[key] = (value, 1)
        self.freq2keys[1][key] = None
        self.minfreq = 1
```

## Python3

```python
import collections

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minfreq = 0
        self.key2valfreq = {}  # key -> (value, freq)
        self.freq2keys = collections.defaultdict(collections.OrderedDict)

    def _update(self, key: int) -> None:
        value, freq = self.key2valfreq[key]
        # remove from current frequency list
        del self.freq2keys[freq][key]
        if not self.freq2keys[freq]:
            del self.freq2keys[freq]
            if self.minfreq == freq:
                self.minfreq += 1
        # add to next frequency list
        newfreq = freq + 1
        self.freq2keys[newfreq][key] = None
        self.key2valfreq[key] = (value, newfreq)

    def get(self, key: int) -> int:
        if key not in self.key2valfreq:
            return -1
        self._update(key)
        return self.key2valfreq[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.key2valfreq:
            # update value and increase frequency
            _, freq = self.key2valfreq[key]
            self.key2valfreq[key] = (value, freq)
            self._update(key)
            return
        if len(self.key2valfreq) >= self.capacity:
            # evict least frequently used key (LRU within same freq)
            lfu_keys = self.freq2keys[self.minfreq]
            evict_key, _ = lfu_keys.popitem(last=False)
            del self.key2valfreq[evict_key]
            if not lfu_keys:
                del self.freq2keys[self.minfreq]
        # insert new key with freq 1
        self.key2valfreq[key] = (value, 1)
        self.freq2keys[1][key] = None
        self.minfreq = 1
```

## C

```c
#include <stdlib.h>
#include "uthash.h"

typedef struct Node {
    int key;
    int value;
    int freq;
    struct Node *prev, *next;   // doubly linked list within a frequency bucket
    UT_hash_handle hh;          // hash handle for key -> node map
} Node;

typedef struct FreqList {
    int freq;                   // frequency (hash key)
    Node *head;                 // dummy head of circular doubly linked list
    UT_hash_handle hh;          // hash handle for freq -> list map
} FreqList;

typedef struct {
    int capacity;
    int size;
    int minFreq;
    Node *key_table;            // hashmap: key -> Node*
    FreqList *freq_table;       // hashmap: freq -> FreqList*
} LFUCache;

/* Helper functions for doubly linked list */
static void addNode(FreqList *list, Node *node) {
    node->prev = list->head->prev;
    node->next = list->head;
    list->head->prev->next = node;
    list->head->prev = node;
}

static void removeNode(FreqList *list, Node *node) {
    node->prev->next = node->next;
    node->next->prev = node->prev;
}

static int isEmpty(FreqList *list) {
    return list->head->next == list->head;
}

/* Increase frequency of a node */
static void increaseFreq(LFUCache *obj, Node *node) {
    int oldFreq = node->freq;
    FreqList *oldList = NULL;
    HASH_FIND_INT(obj->freq_table, &oldFreq, oldList);
    if (oldList) {
        removeNode(oldList, node);
        if (isEmpty(oldList)) {
            HASH_DEL(obj->freq_table, oldList);
            free(oldList->head);
            free(oldList);
            if (obj->minFreq == oldFreq)
                obj->minFreq = oldFreq + 1;
        }
    }

    node->freq++;
    int newFreq = node->freq;
    FreqList *newList = NULL;
    HASH_FIND_INT(obj->freq_table, &newFreq, newList);
    if (!newList) {
        newList = (FreqList *)malloc(sizeof(FreqList));
        newList->freq = newFreq;
        Node *dummy = (Node *)malloc(sizeof(Node));
        dummy->prev = dummy->next = dummy;
        newList->head = dummy;
        HASH_ADD_INT(obj->freq_table, freq, newList);
    }
    addNode(newList, node);
}

/* Create LFUCache */
LFUCache* lFUCacheCreate(int capacity) {
    LFUCache *obj = (LFUCache *)malloc(sizeof(LFUCache));
    obj->capacity = capacity;
    obj->size = 0;
    obj->minFreq = 0;
    obj->key_table = NULL;
    obj->freq_table = NULL;
    return obj;
}

/* Get value */
int lFUCacheGet(LFUCache* obj, int key) {
    Node *node = NULL;
    HASH_FIND_INT(obj->key_table, &key, node);
    if (!node)
        return -1;
    increaseFreq(obj, node);
    return node->value;
}

/* Put key-value */
void lFUCachePut(LFUCache* obj, int key, int value) {
    if (obj->capacity == 0)
        return;

    Node *node = NULL;
    HASH_FIND_INT(obj->key_table, &key, node);
    if (node) {
        node->value = value;
        increaseFreq(obj, node);
        return;
    }

    if (obj->size == obj->capacity) {
        int minF = obj->minFreq;
        FreqList *list = NULL;
        HASH_FIND_INT(obj->freq_table, &minF, list);
        Node *evict = list->head->next;  // LRU within min frequency
        removeNode(list, evict);
        if (isEmpty(list)) {
            HASH_DEL(obj->freq_table, list);
            free(list->head);
            free(list);
        }
        HASH_DEL(obj->key_table, evict);
        free(evict);
        obj->size--;
    }

    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->key = key;
    newNode->value = value;
    newNode->freq = 1;
    HASH_ADD_INT(obj->key_table, key, newNode);

    FreqList *list1 = NULL;
    int one = 1;
    HASH_FIND_INT(obj->freq_table, &one, list1);
    if (!list1) {
        list1 = (FreqList *)malloc(sizeof(FreqList));
        list1->freq = 1;
        Node *dummy = (Node *)malloc(sizeof(Node));
        dummy->prev = dummy->next = dummy;
        list1->head = dummy;
        HASH_ADD_INT(obj->freq_table, freq, list1);
    }
    addNode(list1, newNode);
    obj->minFreq = 1;
    obj->size++;
}

/* Free LFUCache */
void lFUCacheFree(LFUCache* obj) {
    Node *curr_node, *tmp_node;
    HASH_ITER(hh, obj->key_table, curr_node, tmp_node) {
        HASH_DEL(obj->key_table, curr_node);
        free(curr_node);
    }

    FreqList *curr_list, *tmp_list;
    HASH_ITER(hh, obj->freq_table, curr_list, tmp_list) {
        HASH_DEL(obj->freq_table, curr_list);
        free(curr_list->head);
        free(curr_list);
    }
    free(obj);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class LFUCache
{
    private class Entry
    {
        public int Key;
        public int Value;
        public int Frequency;
        public LinkedListNode<int> NodeInFreqList;
    }

    private readonly int capacity;
    private int minFrequency;
    private readonly Dictionary<int, Entry> keyToEntry;
    private readonly Dictionary<int, LinkedList<int>> freqToKeys;

    public LFUCache(int capacity)
    {
        this.capacity = capacity;
        minFrequency = 0;
        keyToEntry = new Dictionary<int, Entry>();
        freqToKeys = new Dictionary<int, LinkedList<int>>();
    }

    public int Get(int key)
    {
        if (!keyToEntry.TryGetValue(key, out var entry))
            return -1;

        // Remove from current frequency list
        var oldFreq = entry.Frequency;
        var oldList = freqToKeys[oldFreq];
        oldList.Remove(entry.NodeInFreqList);
        if (oldList.Count == 0)
        {
            freqToKeys.Remove(oldFreq);
            if (minFrequency == oldFreq)
                minFrequency++;
        }

        // Add to next frequency list
        entry.Frequency++;
        var newFreq = entry.Frequency;
        if (!freqToKeys.TryGetValue(newFreq, out var newList))
        {
            newList = new LinkedList<int>();
            freqToKeys[newFreq] = newList;
        }
        entry.NodeInFreqList = newList.AddLast(key);

        return entry.Value;
    }

    public void Put(int key, int value)
    {
        if (capacity == 0)
            return;

        if (keyToEntry.TryGetValue(key, out var existing))
        {
            existing.Value = value;
            // Update frequency via Get to keep O(1) logic
            Get(key);
            return;
        }

        if (keyToEntry.Count >= capacity)
        {
            // Evict least frequently used key (LRU within same freq)
            var list = freqToKeys[minFrequency];
            int evictKey = list.First.Value;
            list.RemoveFirst();
            if (list.Count == 0)
                freqToKeys.Remove(minFrequency);
            keyToEntry.Remove(evictKey);
        }

        // Insert new key with frequency 1
        var entry = new Entry
        {
            Key = key,
            Value = value,
            Frequency = 1
        };
        if (!freqToKeys.TryGetValue(1, out var freqList))
        {
            freqList = new LinkedList<int>();
            freqToKeys[1] = freqList;
        }
        entry.NodeInFreqList = freqList.AddLast(key);
        keyToEntry[key] = entry;
        minFrequency = 1;
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */
```

## Javascript

```javascript
/**
 * @param {number} capacity
 */
var LFUCache = function (capacity) {
    this.capacity = capacity;
    this.minFreq = 0;
    // key -> {value, freq}
    this.keyMap = new Map();
    // freq -> Set of keys (in insertion order => LRU)
    this.freqMap = new Map();
};

/** 
 * @param {number} key
 * @return {number}
 */
LFUCache.prototype.get = function (key) {
    if (!this.keyMap.has(key)) return -1;
    const node = this.keyMap.get(key);
    const oldFreq = node.freq;
    const newFreq = oldFreq + 1;

    // remove from old frequency set
    const oldSet = this.freqMap.get(oldFreq);
    oldSet.delete(key);
    if (oldSet.size === 0) {
        this.freqMap.delete(oldFreq);
        if (this.minFreq === oldFreq) this.minFreq++;
    }

    // add to new frequency set
    let newSet = this.freqMap.get(newFreq);
    if (!newSet) {
        newSet = new Set();
        this.freqMap.set(newFreq, newSet);
    }
    newSet.add(key);

    node.freq = newFreq;
    return node.value;
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LFUCache.prototype.put = function (key, value) {
    if (this.capacity === 0) return;

    if (this.keyMap.has(key)) {
        const node = this.keyMap.get(key);
        node.value = value;
        // increase frequency using get logic
        this.get(key);
        return;
    }

    if (this.keyMap.size >= this.capacity) {
        // evict least frequently used, LRU within that freq
        const evictSet = this.freqMap.get(this.minFreq);
        const evictKey = evictSet.values().next().value;
        evictSet.delete(evictKey);
        if (evictSet.size === 0) {
            this.freqMap.delete(this.minFreq);
        }
        this.keyMap.delete(evictKey);
    }

    // insert new key with freq 1
    const node = { value: value, freq: 1 };
    this.keyMap.set(key, node);
    let setOne = this.freqMap.get(1);
    if (!setOne) {
        setOne = new Set();
        this.freqMap.set(1, setOne);
    }
    setOne.add(key);
    this.minFreq = 1;
};
```

## Typescript

```typescript
class LFUCache {
    private capacity: number;
    private minFreq: number;
    private keyToNode: Map<number, { value: number; freq: number }>;
    private freqMap: Map<number, Set<number>>;

    constructor(capacity: number) {
        this.capacity = capacity;
        this.minFreq = 0;
        this.keyToNode = new Map();
        this.freqMap = new Map();
    }

    get(key: number): number {
        const node = this.keyToNode.get(key);
        if (!node) return -1;
        this.updateFreq(key, node);
        return node.value;
    }

    put(key: number, value: number): void {
        if (this.capacity === 0) return;

        if (this.keyToNode.has(key)) {
            const node = this.keyToNode.get(key)!;
            node.value = value;
            this.updateFreq(key, node);
            return;
        }

        if (this.keyToNode.size >= this.capacity) {
            const keys = this.freqMap.get(this.minFreq)!;
            const evictKey = keys.values().next().value as number;
            keys.delete(evictKey);
            if (keys.size === 0) this.freqMap.delete(this.minFreq);
            this.keyToNode.delete(evictKey);
        }

        const node = { value, freq: 1 };
        this.keyToNode.set(key, node);
        let set = this.freqMap.get(1);
        if (!set) {
            set = new Set<number>();
            this.freqMap.set(1, set);
        }
        set.add(key);
        this.minFreq = 1;
    }

    private updateFreq(key: number, node: { value: number; freq: number }): void {
        const oldFreq = node.freq;
        const oldSet = this.freqMap.get(oldFreq)!;
        oldSet.delete(key);
        if (oldSet.size === 0) {
            this.freqMap.delete(oldFreq);
            if (this.minFreq === oldFreq) this.minFreq++;
        }

        node.freq++;
        let newSet = this.freqMap.get(node.freq);
        if (!newSet) {
            newSet = new Set<number>();
            this.freqMap.set(node.freq, newSet);
        }
        newSet.add(key);
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * var obj = new LFUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

## Php

```php
class Node {
    public $key;
    public $prev = null;
    public $next = null;
    public function __construct($key) {
        $this->key = $key;
    }
}

class DoublyLinkedList {
    private $head;
    private $tail;

    public function __construct() {
        $this->head = new Node(null);
        $this->tail = new Node(null);
        $this->head->next = $this->tail;
        $this->tail->prev = $this->head;
    }

    public function addNodeToTail($node) {
        $node->prev = $this->tail->prev;
        $node->next = $this->tail;
        $this->tail->prev->next = $node;
        $this->tail->prev = $node;
    }

    public function removeNode($node) {
        $node->prev->next = $node->next;
        $node->next->prev = $node->prev;
        $node->prev = null;
        $node->next = null;
    }

    public function popFront() {
        if ($this->isEmpty()) {
            return null;
        }
        $node = $this->head->next;
        $this->removeNode($node);
        return $node;
    }

    public function isEmpty() {
        return $this->head->next === $this->tail;
    }
}

class LFUCache {
    private $capacity = 0;
    private $minFreq = 0;
    /** @var array key => ['value'=>int,'freq'=>int,'node'=>Node] */
    private $keyMap = [];
    /** @var array freq => DoublyLinkedList */
    private $freqMap = [];

    /**
     * @param Integer $capacity
     */
    function __construct($capacity) {
        $this->capacity = $capacity;
        $this->minFreq = 0;
    }

    /**
     * @param Integer $key
     * @return Integer
     */
    function get($key) {
        if (!isset($this->keyMap[$key])) {
            return -1;
        }
        $value = $this->keyMap[$key]['value'];
        $this->increaseFreq($key);
        return $value;
    }

    /**
     * @param Integer $key
     * @param Integer $value
     * @return NULL
     */
    function put($key, $value) {
        if ($this->capacity <= 0) {
            return;
        }
        if (isset($this->keyMap[$key])) {
            // Update value and increase frequency
            $this->keyMap[$key]['value'] = $value;
            $this->increaseFreq($key);
            return;
        }

        if (count($this->keyMap) >= $this->capacity) {
            // Evict least frequently used key (LRU within same freq)
            $list = $this->freqMap[$this->minFreq];
            $evictNode = $list->popFront();
            if ($evictNode !== null) {
                $evictKey = $evictNode->key;
                unset($this->keyMap[$evictKey]);
                // Clean up empty freq list
                if ($list->isEmpty()) {
                    unset($this->freqMap[$this->minFreq]);
                }
            }
        }

        // Insert new key with freq 1
        $node = new Node($key);
        $entry = ['value' => $value, 'freq' => 1, 'node' => $node];
        $this->keyMap[$key] = $entry;
        if (!isset($this->freqMap[1])) {
            $this->freqMap[1] = new DoublyLinkedList();
        }
        $this->freqMap[1]->addNodeToTail($node);
        $this->minFreq = 1;
    }

    private function increaseFreq($key) {
        $entry = &$this->keyMap[$key];
        $oldFreq = $entry['freq'];
        $node = $entry['node'];

        // Remove from old frequency list
        $oldList = $this->freqMap[$oldFreq];
        $oldList->removeNode($node);
        if ($oldList->isEmpty()) {
            unset($this->freqMap[$oldFreq]);
            if ($this->minFreq == $oldFreq) {
                $this->minFreq++;
            }
        }

        // Add to new frequency list
        $newFreq = $oldFreq + 1;
        if (!isset($this->freqMap[$newFreq])) {
            $this->freqMap[$newFreq] = new DoublyLinkedList();
        }
        $this->freqMap[$newFreq]->addNodeToTail($node);
        $entry['freq'] = $newFreq;
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * $obj = new LFUCache($capacity);
 * $ret_1 = $obj->get($key);
 * $obj->put($key, $value);
 */
```

## Swift

```swift
import Foundation

class Node {
    var key: Int
    var value: Int
    var freq: Int
    var prev: Node?
    var next: Node?
    
    init(_ key: Int, _ value: Int) {
        self.key = key
        self.value = value
        self.freq = 1
    }
}

class DoubleLinkedList {
    private let head: Node
    private let tail: Node
    
    init() {
        head = Node(0, 0)
        tail = Node(0, 0)
        head.next = tail
        tail.prev = head
    }
    
    var isEmpty: Bool {
        return head.next === tail
    }
    
    func addLast(_ node: Node) {
        node.prev = tail.prev
        node.next = tail
        tail.prev?.next = node
        tail.prev = node
    }
    
    func remove(_ node: Node) {
        node.prev?.next = node.next
        node.next?.prev = node.prev
        node.prev = nil
        node.next = nil
    }
    
    func popFirst() -> Node? {
        if isEmpty { return nil }
        guard let first = head.next else { return nil }
        remove(first)
        return first
    }
}

class LFUCache {
    private let capacity: Int
    private var minFreq: Int = 0
    private var keyNode: [Int: Node] = [:]
    private var freqList: [Int: DoubleLinkedList] = [:]
    
    init(_ capacity: Int) {
        self.capacity = capacity
    }
    
    func get(_ key: Int) -> Int {
        guard let node = keyNode[key] else { return -1 }
        update(node)
        return node.value
    }
    
    func put(_ key: Int, _ value: Int) {
        if capacity == 0 { return }
        
        if let node = keyNode[key] {
            node.value = value
            update(node)
            return
        }
        
        if keyNode.count >= capacity {
            if let list = freqList[minFreq], let evictNode = list.popFirst() {
                keyNode.removeValue(forKey: evictNode.key)
                if list.isEmpty {
                    freqList.removeValue(forKey: minFreq)
                }
            }
        }
        
        let newNode = Node(key, value) // freq starts at 1
        keyNode[key] = newNode
        minFreq = 1
        let list = freqList[1] ?? DoubleLinkedList()
        list.addLast(newNode)
        freqList[1] = list
    }
    
    private func update(_ node: Node) {
        let curFreq = node.freq
        if let list = freqList[curFreq] {
            list.remove(node)
            if list.isEmpty {
                freqList.removeValue(forKey: curFreq)
                if minFreq == curFreq { minFreq += 1 }
            }
        }
        
        node.freq += 1
        let newFreq = node.freq
        let newList = freqList[newFreq] ?? DoubleLinkedList()
        newList.addLast(node)
        freqList[newFreq] = newList
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * let obj = LFUCache(capacity)
 * let ret_1: Int = obj.get(key)
 * obj.put(key, value)
 */
```

## Kotlin

```kotlin
class LFUCache(capacity: Int) {
    private val capacity = capacity
    private var minFreq = 0

    private data class Node(var key: Int, var value: Int, var freq: Int)

    private val keyNode = HashMap<Int, Node>()
    private val freqMap = HashMap<Int, LinkedHashSet<Int>>()

    fun get(key: Int): Int {
        val node = keyNode[key] ?: return -1
        val oldFreq = node.freq
        freqMap[oldFreq]?.remove(key)
        if (freqMap[oldFreq]?.isEmpty() == true) {
            freqMap.remove(oldFreq)
            if (minFreq == oldFreq) minFreq++
        }
        node.freq = oldFreq + 1
        val set = freqMap.getOrPut(node.freq) { LinkedHashSet() }
        set.add(key)
        return node.value
    }

    fun put(key: Int, value: Int) {
        if (capacity <= 0) return
        if (keyNode.containsKey(key)) {
            keyNode[key]!!.value = value
            get(key)
            return
        }
        if (keyNode.size >= capacity) {
            val evictSet = freqMap[minFreq]!!
            val evictKey = evictSet.iterator().next()
            evictSet.remove(evictKey)
            if (evictSet.isEmpty()) {
                freqMap.remove(minFreq)
            }
            keyNode.remove(evictKey)
        }
        val node = Node(key, value, 1)
        keyNode[key] = node
        minFreq = 1
        val set = freqMap.getOrPut(1) { LinkedHashSet() }
        set.add(key)
    }
}
```

## Dart

```dart
import 'dart:collection';

class _Node {
  int value;
  int freq;
  _Node(this.value, this.freq);
}

class LFUCache {
  final int capacity;
  int _minFreq = 0;
  final Map<int, _Node> _keyToNode = {};
  final Map<int, LinkedHashSet<int>> _freqMap = {};

  LFUCache(this.capacity);

  int get(int key) {
    if (!_keyToNode.containsKey(key)) return -1;
    var node = _keyToNode[key]!;
    int oldFreq = node.freq;

    // Remove from current frequency set
    var oldSet = _freqMap[oldFreq];
    oldSet?.remove(key);
    if (oldSet != null && oldSet.isEmpty) {
      _freqMap.remove(oldFreq);
      if (_minFreq == oldFreq) _minFreq++;
    }

    // Add to next frequency set
    node.freq++;
    _freqMap.putIfAbsent(node.freq, () => LinkedHashSet<int>()).add(key);

    return node.value;
  }

  void put(int key, int value) {
    if (capacity <= 0) return;

    if (_keyToNode.containsKey(key)) {
      // Update value and increase frequency
      var node = _keyToNode[key]!;
      node.value = value;
      get(key);
      return;
    }

    if (_keyToNode.length >= capacity) {
      // Evict least frequently used key (LRU within same freq)
      var evictSet = _freqMap[_minFreq]!;
      int evictKey = evictSet.first;
      evictSet.remove(evictKey);
      if (evictSet.isEmpty) {
        _freqMap.remove(_minFreq);
      }
      _keyToNode.remove(evictKey);
    }

    // Insert new key with frequency 1
    var node = _Node(value, 1);
    _keyToNode[key] = node;
    _freqMap.putIfAbsent(1, () => LinkedHashSet<int>()).add(key);
    _minFreq = 1;
  }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = LFUCache(capacity);
 * int param1 = obj.get(key);
 * obj.put(key,value);
 */
```

## Golang

```go
package main

import "container/list"

type node struct {
	key   int
	value int
	freq  int
	elem  *list.Element
}

type LFUCache struct {
	capacity int
	minFreq  int
	keys     map[int]*node          // key -> node
	freqs    map[int]*list.List    // freq -> list of nodes (LRU order)
}

// Constructor initializes the LFU cache with given capacity.
func Constructor(capacity int) LFUCache {
	return LFUCache{
		capacity: capacity,
		keys:     make(map[int]*node),
		freqs:    make(map[int]*list.List),
	}
}

// Get returns the value of the key if present, otherwise -1.
// It also updates the node's frequency.
func (c *LFUCache) Get(key int) int {
	if c.capacity == 0 {
		return -1
	}
	n, ok := c.keys[key]
	if !ok {
		return -1
	}
	c.increment(n)
	return n.value
}

// Put inserts or updates the value of the key.
// If the cache reaches its capacity, it evicts the LFU (and LRU among ties) entry.
func (c *LFUCache) Put(key int, value int) {
	if c.capacity == 0 {
		return
	}
	if n, ok := c.keys[key]; ok {
		n.value = value
		c.increment(n)
		return
	}
	if len(c.keys) >= c.capacity {
		// Evict least frequently used key (LRU within that freq)
		listAtMinFreq := c.freqs[c.minFreq]
		evictElem := listAtMinFreq.Front()
		if evictElem != nil {
			evictNode := evictElem.Value.(*node)
			delete(c.keys, evictNode.key)
			listAtMinFreq.Remove(evictElem)
			if listAtMinFreq.Len() == 0 {
				delete(c.freqs, c.minFreq)
			}
		}
	}
	// Insert new node with freq = 1
	newNode := &node{
		key:   key,
		value: value,
		freq:  1,
	}
	if _, ok := c.freqs[1]; !ok {
		c.freqs[1] = list.New()
	}
	elem := c.freqs[1].PushBack(newNode)
	newNode.elem = elem
	c.keys[key] = newNode
	c.minFreq = 1
}

// increment updates the node's frequency and moves it to the appropriate list.
func (c *LFUCache) increment(n *node) {
	oldFreq := n.freq
	// Remove from old frequency list
	if lst, ok := c.freqs[oldFreq]; ok {
		lst.Remove(n.elem)
		if lst.Len() == 0 {
			delete(c.freqs, oldFreq)
			if c.minFreq == oldFreq {
				c.minFreq++
			}
		}
	}
	// Add to new frequency list
	n.freq++
	if _, ok := c.freqs[n.freq]; !ok {
		c.freqs[n.freq] = list.New()
	}
	newElem := c.freqs[n.freq].PushBack(n)
	n.elem = newElem
}
```

## Ruby

```ruby
class Node
  attr_accessor :key, :value, :freq, :prev, :next

  def initialize(key = nil, value = nil, freq = 0)
    @key = key
    @value = value
    @freq = freq
    @prev = nil
    @next = nil
  end
end

class DLinkedList
  def initialize
    @head = Node.new
    @tail = Node.new
    @head.next = @tail
    @tail.prev = @head
  end

  def empty?
    @head.next == @tail
  end

  def add_node(node)
    node.prev = @tail.prev
    node.next = @tail
    @tail.prev.next = node
    @tail.prev = node
  end

  def remove_node(node)
    node.prev.next = node.next
    node.next.prev = node.prev
    node.prev = nil
    node.next = nil
  end

  def pop_front
    return nil if empty?
    node = @head.next
    remove_node(node)
    node
  end
end

class LFUCache
  # :type capacity: Integer
  def initialize(capacity)
    @capacity = capacity
    @min_freq = 0
    @key_table = {}                     # key => Node
    @freq_table = Hash.new { |h, k| h[k] = DLinkedList.new } # freq => DLinkedList
  end

  # :type key: Integer
  # :rtype: Integer
  def get(key)
    return -1 unless @key_table.key?(key)

    node = @key_table[key]
    update(node)
    node.value
  end

  # :type key: Integer
  # :type value: Integer
  # :rtype: Void
  def put(key, value)
    return if @capacity == 0

    if @key_table.key?(key)
      node = @key_table[key]
      node.value = value
      update(node)
      return
    end

    if @key_table.size >= @capacity
      lfu_list = @freq_table[@min_freq]
      evicted_node = lfu_list.pop_front
      @key_table.delete(evicted_node.key) if evicted_node
    end

    new_node = Node.new(key, value, 1)
    @key_table[key] = new_node
    @freq_table[1].add_node(new_node)
    @min_freq = 1
  end

  private

  def update(node)
    old_freq = node.freq
    @freq_table[old_freq].remove_node(node)

    if @freq_table[old_freq].empty? && @min_freq == old_freq
      @min_freq += 1
    end

    node.freq += 1
    @freq_table[node.freq].add_node(node)
  end
end
```

## Scala

```scala
import java.util.{LinkedHashSet, Iterator}
import scala.collection.mutable

class LFUCache(_capacity: Int) {

  private val capacity = _capacity
  private var minFreq = 0

  // key -> (value, freq)
  private val cache = mutable.HashMap.empty[Int, (Int, Int)]

  // freq -> keys with this freq, ordered by recency (LRU within same freq)
  private val freqMap = mutable.HashMap.empty[Int, LinkedHashSet[Int]]

  def get(key: Int): Int = {
    cache.get(key) match {
      case None => -1
      case Some((value, freq)) =>
        // remove from current frequency set
        val oldSet = freqMap(freq)
        oldSet.remove(key)
        if (oldSet.isEmpty) {
          freqMap.remove(freq)
          if (minFreq == freq) minFreq += 1
        }

        // add to next frequency set
        val newFreq = freq + 1
        val newSet = freqMap.getOrElseUpdate(newFreq, new LinkedHashSet[Int]())
        newSet.add(key)

        // update cache entry
        cache.update(key, (value, newFreq))

        value
    }
  }

  def put(key: Int, value: Int): Unit = {
    if (capacity <= 0) return

    if (cache.contains(key)) {
      // update value and treat as accessed to increase frequency
      val (_, freq) = cache(key)
      cache.update(key, (value, freq))
      get(key) // ignore returned value
      return
    }

    if (cache.size >= capacity) {
      // evict least frequently used key (LRU within same freq)
      val lfuSet = freqMap(minFreq)
      val it: Iterator[Int] = lfuSet.iterator()
      if (it.hasNext) {
        val evictKey = it.next()
        lfuSet.remove(evictKey)
        if (lfuSet.isEmpty) {
          freqMap.remove(minFreq)
        }
        cache.remove(evictKey)
      }
    }

    // insert new key with frequency 1
    minFreq = 1
    val set = freqMap.getOrElseUpdate(1, new LinkedHashSet[Int]())
    set.add(key)
    cache.put(key, (value, 1))
  }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * val obj = new LFUCache(capacity)
 * val param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

## Rust

```rust
use std::cell::RefCell;
use std::collections::{HashMap, VecDeque};

#[derive(Clone)]
struct Entry {
    value: i32,
    freq: i32,
}

pub struct LFUCache {
    capacity: usize,
    min_freq: RefCell<i32>,
    key_map: RefCell<HashMap<i32, Entry>>,
    freq_map: RefCell<HashMap<i32, VecDeque<i32>>>,
}

impl LFUCache {
    pub fn new(capacity: i32) -> Self {
        LFUCache {
            capacity: capacity as usize,
            min_freq: RefCell::new(0),
            key_map: RefCell::new(HashMap::new()),
            freq_map: RefCell::new(HashMap::new()),
        }
    }

    fn clean_min(&self) {
        loop {
            let cur_min = *self.min_freq.borrow();
            if cur_min == 0 {
                break;
            }
            let mut fm = self.freq_map.borrow_mut();
            if let Some(dq) = fm.get_mut(&cur_min) {
                while let Some(&key) = dq.front() {
                    let km = self.key_map.borrow();
                    if let Some(e) = km.get(&key) {
                        if e.freq == cur_min {
                            break;
                        }
                    }
                    dq.pop_front(); // stale entry
                }
                if dq.is_empty() {
                    fm.remove(&cur_min);
                    *self.min_freq.borrow_mut() += 1;
                    continue;
                } else {
                    break;
                }
            } else {
                *self.min_freq.borrow_mut() += 1;
            }
        }
    }

    pub fn get(&self, key: i32) -> i32 {
        let mut km = self.key_map.borrow_mut();
        if let Some(entry) = km.get_mut(&key) {
            let old_freq = entry.freq;
            entry.freq += 1;
            let new_freq = entry.freq;
            let val = entry.value;
            drop(km);

            let mut fm = self.freq_map.borrow_mut();
            fm.entry(new_freq)
                .or_insert_with(VecDeque::new)
                .push_back(key);
            drop(fm);

            if old_freq == *self.min_freq.borrow() {
                self.clean_min();
            }
            val
        } else {
            -1
        }
    }

    pub fn put(&self, key: i32, value: i32) {
        if self.capacity == 0 {
            return;
        }

        // If key exists, update its value and frequency.
        {
            let mut km = self.key_map.borrow_mut();
            if let Some(entry) = km.get_mut(&key) {
                entry.value = value;
                let old_freq = entry.freq;
                entry.freq += 1;
                let new_freq = entry.freq;
                drop(km);

                let mut fm = self.freq_map.borrow_mut();
                fm.entry(new_freq)
                    .or_insert_with(VecDeque::new)
                    .push_back(key);
                drop(fm);

                if old_freq == *self.min_freq.borrow() {
                    self.clean_min();
                }
                return;
            }
        }

        // Need to insert new key.
        {
            let mut km = self.key_map.borrow_mut();
            if km.len() == self.capacity {
                // Evict least frequently used, LRU among them.
                self.clean_min();
                let min = *self.min_freq.borrow();
                let mut fm = self.freq_map.borrow_mut();
                if let Some(dq) = fm.get_mut(&min) {
                    while let Some(ev_key) = dq.pop_front() {
                        let mut km2 = self.key_map.borrow_mut();
                        if let Some(e) = km2.get(&ev_key) {
                            if e.freq == min {
                                km2.remove(&ev_key);
                                break;
                            }
                        }
                        // stale entry, continue
                    }
                }
            }

            // Insert the new key with freq 1.
            km.insert(key, Entry { value, freq: 1 });
        }

        let mut fm = self.freq_map.borrow_mut();
        fm.entry(1).or_insert_with(VecDeque::new).push_back(key);
        *self.min_freq.borrow_mut() = 1;
    }
}
```

## Racket

```racket
(define-struct node (key value freq prev next) #:mutable)
(define-struct dlist (head tail))

(define lfu-cache%
  (class object%
    (super-new)

    (init-field capacity)

    (define key-node (make-hash))      ; key -> node
    (define freq-list (make-hash))     ; freq -> dlist
    (define minfreq 0)                 ; current minimum frequency

    ;; create an empty doubly linked list with dummy head/tail
    (define (make-dlist)
      (let* ([head (node #f #f 0 #f #f)]
             [tail (node #f #f 0 #f #f)])
        (set-node-next! head tail)
        (set-node-prev! tail head)
        (dlist head tail)))

    ;; obtain the dlist for a frequency, creating if absent
    (define (get-dlist freq)
      (hash-ref freq-list freq
                (lambda ()
                  (let ([dl (make-dlist)])
                    (hash-set! freq-list freq dl)
                    dl))))

    ;; unlink a node from its list
    (define (remove-node n)
      (let ([p (node-prev n)]
            [ne (node-next n)])
        (when p (set-node-next! p ne))
        (when ne (set-node-prev! ne p))))

    ;; insert node just before the tail (most recent)
    (define (append-to-dlist dl n)
      (let* ([tail (dlist-tail dl)]
             [prev (node-prev tail)])
        (set-node-prev! n prev)
        (set-node-next! n tail)
        (when prev (set-node-next! prev n))
        (set-node-prev! tail n)))

    ;; pop the least-recently-used node (first real after head)
    (define (pop-head dl)
      (let ([head (dlist-head dl)]
            [tail (dlist-tail dl)])
        (let ([first (node-next head)])
          (if (eq? first tail)
              #f
              (begin
                (remove-node first)
                first)))))

    ;; public get
    (define/public (get key)
      (if (hash-has-key? key-node key)
          (let* ([n (hash-ref key-node key)]
                 [val (node-value n)]
                 [freq (node-freq n)])
            ;; remove from current frequency list
            (let ([dl (hash-ref freq-list freq)])
              (remove-node n))
            ;; if this was the only node with minfreq, advance minfreq
            (when (and (= minfreq freq)
                       (let* ([dl (hash-ref freq-list freq)]
                              [head (dlist-head dl)]
                              [tail (dlist-tail dl)])
                         (eq? (node-next head) tail)))
              (set! minfreq (+ minfreq 1)))
            ;; increase frequency
            (let ([newfreq (+ freq 1)])
              (set-node-freq! n newfreq)
              (let ([newdl (get-dlist newfreq)])
                (append-to-dlist newdl n)))
            val)
          -1))

    ;; public put
    (define/public (put key value)
      (when (> capacity 0)
        (if (hash-has-key? key-node key)
            (begin
              (let ([n (hash-ref key-node key)])
                (set-node-value! n value))
              (send this get key))   ; increase frequency
            (begin
              ;; evict if at capacity
              (when (= (hash-count key-node) capacity)
                (let* ([dl (hash-ref freq-list minfreq)]
                       [evict-node (pop-head dl)])
                  (when evict-node
                    (hash-remove! key-node (node-key evict-node)))))
              ;; insert new node with frequency 1
              (set! minfreq 1)
              (let* ([n (node key value 1 #f #f)]
                     [dl (get-dlist 1)])
                (append-to-dlist dl n)
                (hash-set! key-node key n))))))

    ))
```

## Erlang

```erlang
-module(lfu_cache).
-export([lfu_cache_init_/1, lfu_cache_get/1, lfu_cache_put/2]).

%% Initialization
-spec lfu_cache_init_(Capacity :: integer()) -> any().
lfu_cache_init_(Capacity) ->
    State = #{capacity => Capacity,
              size => 0,
              minfreq => 0,
              key_map => #{},
              freq_map => #{}},
    erlang:put(lfu_state, State),
    ok.

%% Get operation
-spec lfu_cache_get(Key :: integer()) -> integer().
lfu_cache_get(Key) ->
    case erlang:get(lfu_state) of
        undefined -> -1;
        State0 ->
            KeyMap = maps:get(key_map, State0),
            case maps:find(Key, KeyMap) of
                error -> -1;
                {ok, Node} ->
                    Value = maps:get(value, Node),
                    NewState = increase_freq(Key, Node, State0),
                    erlang:put(lfu_state, NewState),
                    Value
            end
    end.

%% Put operation
-spec lfu_cache_put(Key :: integer(), Value :: integer()) -> any().
lfu_cache_put(Key, Value) ->
    case erlang:get(lfu_state) of
        undefined -> ok;
        State0 ->
            Cap = maps:get(capacity, State0),
            if Cap == 0 ->
                    ok;
               true ->
                    KeyMap = maps:get(key_map, State0),
                    case maps:find(Key, KeyMap) of
                        {ok, Node} ->
                            UpdatedNode = maps:put(value, Value, Node),
                            KM1 = maps:put(Key, UpdatedNode, KeyMap),
                            TempState = State0#{key_map => KM1},
                            NewState = increase_freq(Key, UpdatedNode, TempState),
                            erlang:put(lfu_state, NewState);
                        error ->
                            Size = maps:get(size, State0),
                            State1 = if Size == Cap -> evict(State0); true -> State0 end,
                            NewState = add_new_key(Key, Value, State1),
                            erlang:put(lfu_state, NewState)
                    end
            end
    end,
    ok.

%% Helper: increase frequency of a key
increase_freq(Key, Node, State) ->
    OldFreq = maps:get(freq, Node),
    NewFreq = OldFreq + 1,
    KeyMap0 = maps:get(key_map, State),
    FreqMap0 = maps:get(freq_map, State),

    Prev = maps:get(prev, Node, undefined),
    Next = maps:get(next, Node, undefined),

    %% Update neighbors
    KeyMap1 = case Prev of
        undefined -> KeyMap0;
        _ ->
            PrevNode = maps:get(Prev, KeyMap0),
            UpdatedPrev = maps:put(next, Next, PrevNode),
            maps:put(Prev, UpdatedPrev, KeyMap0)
    end,
    KeyMap2 = case Next of
        undefined -> KeyMap1;
        _ ->
            NextNode = maps:get(Next, KeyMap1),
            UpdatedNext = maps:put(prev, Prev, NextNode),
            maps:put(Next, UpdatedNext, KeyMap1)
    end,

    %% Update old frequency list metadata
    {HeadOld, TailOld} =
        case maps:find(OldFreq, FreqMap0) of
            error -> {undefined, undefined};
            {ok, Seg} -> {maps:get(head, Seg), maps:get(tail, Seg)}
        end,
    NewHeadOld = if HeadOld == Key -> Next; true -> HeadOld end,
    NewTailOld = if TailOld == Key -> Prev; true -> TailOld end,
    FreqMap1 = case {NewHeadOld, NewTailOld} of
        {undefined, undefined} -> maps:remove(OldFreq, FreqMap0);
        _ -> maps:put(OldFreq, #{head => NewHeadOld, tail => NewTailOld}, FreqMap0)
    end,

    %% Insert into new frequency list at tail
    BaseNode = Node#{freq => NewFreq},
    {_, KeyMap3, FreqMap2} = insert_into_freq_tail(Key, BaseNode, NewFreq, KeyMap2, FreqMap1),

    %% Adjust minfreq if needed
    MinFreq0 = maps:get(minfreq, State),
    MinFreq1 = case (OldFreq == MinFreq0) andalso not maps:is_key(OldFreq, FreqMap2) of
        true -> NewFreq;
        false -> MinFreq0
    end,
    State#{key_map => KeyMap3, freq_map => FreqMap2, minfreq => MinFreq1}.

%% Helper: insert a key into frequency list tail
insert_into_freq_tail(Key, Node0, Freq, KeyMap, FreqMap) ->
    case maps:find(Freq, FreqMap) of
        error ->
            Node = Node0#{prev => undefined, next => undefined},
            NewKeyMap = maps:put(Key, Node, KeyMap),
            NewFreqMap = maps:put(Freq, #{head => Key, tail => Key}, FreqMap),
            {Node, NewKeyMap, NewFreqMap};
        {ok, Seg} ->
            TailKey = maps:get(tail, Seg),
            OldTailNode = maps:get(TailKey, KeyMap),
            UpdatedOldTail = maps:put(next, Key, OldTailNode),
            KM1 = maps:put(TailKey, UpdatedOldTail, KeyMap),

            Node = Node0#{prev => TailKey, next => undefined},
            KM2 = maps:put(Key, Node, KM1),

            NewSeg = Seg#{tail => Key},
            FM2 = maps:put(Freq, NewSeg, FreqMap),
            {Node, KM2, FM2}
    end.

%% Helper: evict least frequently used key
evict(State) ->
    MinFreq = maps:get(minfreq, State),
    FreqMap = maps:get(freq_map, State),
    #{head := EvictKey} = maps:get(MinFreq, FreqMap),

    KeyMap0 = maps:get(key_map, State),
    EvictNode = maps:get(EvictKey, KeyMap0),
    Next = maps:get(next, EvictNode, undefined),

    case Next of
        undefined ->
            NewFreqMap = maps:remove(MinFreq, FreqMap),
            NewKeyMap = maps:remove(EvictKey, KeyMap0);
        _ ->
            %% Update next node's prev to undefined
            NextNode = maps:get(Next, KeyMap0),
            UpdatedNext = maps:put(prev, undefined, NextNode),
            NewKeyMapTmp = maps:put(Next, UpdatedNext, maps:remove(EvictKey, KeyMap0)),
            Seg = maps:get(MinFreq, FreqMap),
            NewSeg = Seg#{head => Next},
            NewFreqMap = maps:put(MinFreq, NewSeg, FreqMap),
            NewKeyMap = NewKeyMapTmp
    end,
    State#{key_map => NewKeyMap, freq_map => NewFreqMap, size => maps:get(size, State) - 1}.

%% Helper: add a new key with frequency 1
add_new_key(Key, Value, State) ->
    Node0 = #{value => Value, freq => 1},
    {_, KM, FM} = insert_into_freq_tail(Key, Node0, 1,
        maps:get(key_map, State), maps:get(freq_map, State)),
    NewSize = maps:get(size, State) + 1,
    State#{key_map => KM, freq_map => FM, size => NewSize, minfreq => 1}.
```

## Elixir

```elixir
defmodule LFUCache do
  @spec init_(capacity :: integer) :: any
  def init_(capacity) do
    state = %{
      capacity: capacity,
      size: 0,
      min_freq: 0,
      key_map: %{},   # key => {value, freq}
      freq_map: %{},  # freq => %{head: key | nil, tail: key | nil}
      node_map: %{}   # key => %{prev: key | nil, next: key | nil}
    }

    Process.put(:lfu_state, state)
    nil
  end

  @spec get(key :: integer) :: integer
  def get(key) do
    state = Process.get(:lfu_state)

    case Map.fetch(state.key_map, key) do
      :error ->
        -1

      {:ok, {value, freq}} ->
        {state, _} = increase_freq(state, key, value, freq)
        Process.put(:lfu_state, state)
        value
    end
  end

  @spec put(key :: integer, value :: integer) :: any
  def put(key, value) do
    state = Process.get(:lfu_state)

    if state.capacity == 0 do
      nil
    else
      case Map.fetch(state.key_map, key) do
        {:ok, {_old_val, freq}} ->
          # update value and increase frequency
          state = %{state | key_map: Map.put(state.key_map, key, {value, freq})}
          {state, _} = increase_freq(state, key, value, freq)
          Process.put(:lfu_state, state)
          nil

        :error ->
          # need to insert new key
          state =
            if state.size == state.capacity do
              # evict least frequently used and LRU among them
              minf = state.min_freq
              %{head: evict_key} = Map.get(state.freq_map, minf)
              state = remove_node(state, minf, evict_key)
              key_map = Map.delete(state.key_map, evict_key)
              %{state | key_map: key_map, size: state.size - 1}
            else
              state
            end

          # insert new key with freq 1
          state = add_node_to_tail(state, 1, key)
          key_map = Map.put(state.key_map, key, {value, 1})
          %{state | key_map: key_map, min_freq: 1, size: state.size + 1}
          |> (fn s -> Process.put(:lfu_state, s); nil end).()
      end
    end
  end

  # Helpers

  defp increase_freq(state, key, value, freq) do
    state = remove_node(state, freq, key)
    new_freq = freq + 1
    state = add_node_to_tail(state, new_freq, key)

    key_map = Map.put(state.key_map, key, {value, new_freq})
    state = %{state | key_map: key_map}

    # adjust min_freq if needed
    state =
      if state.min_freq == freq do
        case Map.get(state.freq_map, freq) do
          nil -> %{state | min_freq: new_freq}
          _ -> state
        end
      else
        state
      end

    {state, :ok}
  end

  defp add_node_to_tail(state, freq, key) do
    freq_map = state.freq_map
    node_map = state.node_map

    case Map.get(freq_map, freq) do
      nil ->
        # first node in this frequency list
        entry = %{head: key, tail: key}
        node = %{prev: nil, next: nil}
        %{state |
          freq_map: Map.put(freq_map, freq, entry),
          node_map: Map.put(node_map, key, node)
        }

      %{head: head, tail: tail} = entry ->
        # append to tail
        prev_tail_node = Map.get(node_map, tail)
        updated_prev_tail = %{prev_tail_node | next: key}
        node_map = Map.put(node_map, tail, updated_prev_tail)

        node = %{prev: tail, next: nil}
        node_map = Map.put(node_map, key, node)

        new_entry = %{head: head, tail: key}
        freq_map = Map.put(freq_map, freq, new_entry)

        %{state | freq_map: freq_map, node_map: node_map}
    end
  end

  defp remove_node(state, freq, key) do
    node = state.node_map[key]
    prev = node.prev
    nxt = node.next
    freq_entry = state.freq_map[freq]

    node_map = Map.delete(state.node_map, key)

    cond do
      prev == nil and nxt == nil ->
        # only node in the list; remove frequency entry
        freq_map = Map.delete(state.freq_map, freq)
        %{state | freq_map: freq_map, node_map: node_map}

      prev == nil ->
        # head node
        next_node = Map.get(state.node_map, nxt)
        updated_next = %{next_node | prev: nil}
        node_map = Map.put(node_map, nxt, updated_next)

        new_entry = %{head: nxt, tail: freq_entry.tail}
        freq_map = Map.put(state.freq_map, freq, new_entry)

        %{state | freq_map: freq_map, node_map: node_map}

      nxt == nil ->
        # tail node
        prev_node = Map.get(state.node_map, prev)
        updated_prev = %{prev_node | next: nil}
        node_map = Map.put(node_map, prev, updated_prev)

        new_entry = %{head: freq_entry.head, tail: prev}
        freq_map = Map.put(state.freq_map, freq, new_entry)

        %{state | freq_map: freq_map, node_map: node_map}

      true ->
        # middle node
        prev_node = Map.get(state.node_map, prev)
        next_node = Map.get(state.node_map, nxt)

        updated_prev = %{prev_node | next: nxt}
        updated_next = %{next_node | prev: prev}

        node_map =
          node_map
          |> Map.put(prev, updated_prev)
          |> Map.put(nxt, updated_next)

        # frequency entry unchanged
        %{state | node_map: node_map}
    end
  end
end
```
