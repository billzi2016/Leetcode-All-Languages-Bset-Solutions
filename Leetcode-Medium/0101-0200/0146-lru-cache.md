# 0146. LRU Cache

## Cpp

```cpp
class LRUCache {
    int cap;
    std::list<std::pair<int,int>> dll; // front = most recent
    std::unordered_map<int, std::list<std::pair<int,int>>::iterator> mp;
public:
    LRUCache(int capacity) : cap(capacity) {}
    
    int get(int key) {
        auto it = mp.find(key);
        if (it == mp.end()) return -1;
        // move to front
        dll.splice(dll.begin(), dll, it->second);
        return it->second->second;
    }
    
    void put(int key, int value) {
        if (cap == 0) return;
        auto it = mp.find(key);
        if (it != mp.end()) {
            // update and move to front
            it->second->second = value;
            dll.splice(dll.begin(), dll, it->second);
        } else {
            if ((int)dll.size() == cap) {
                auto del = dll.back();
                mp.erase(del.first);
                dll.pop_back();
            }
            dll.emplace_front(key, value);
            mp[key] = dll.begin();
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```

## Java

```java
class LRUCache {
    private static class Node {
        int key, value;
        Node prev, next;
        Node(int k, int v) { key = k; value = v; }
    }

    private final int capacity;
    private final java.util.HashMap<Integer, Node> map;
    private final Node head, tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.map = new java.util.HashMap<>(capacity * 2);
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        Node node = map.get(key);
        if (node == null) return -1;
        moveToHead(node);
        return node.value;
    }

    public void put(int key, int value) {
        Node node = map.get(key);
        if (node != null) {
            node.value = value;
            moveToHead(node);
        } else {
            Node newNode = new Node(key, value);
            map.put(key, newNode);
            addToHead(newNode);
            if (map.size() > capacity) {
                Node tailPrev = popTail();
                map.remove(tailPrev.key);
            }
        }
    }

    private void addToHead(Node node) {
        node.prev = head;
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
    }

    private void removeNode(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void moveToHead(Node node) {
        removeNode(node);
        addToHead(node);
    }

    private Node popTail() {
        Node res = tail.prev;
        removeNode(res);
        return res;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
```

## Python

```python
import collections

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value  # re-insert as most recently used
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # remove least recently used
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

## Python3

```python
import collections

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value  # re-insert to mark as most recently used
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # remove least recently used
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

## C

```c
typedef struct Node {
    int key;
    int value;
    struct Node *prev;
    struct Node *next;
    struct Node *hnext;   // next in hash bucket
} Node;

typedef struct {
    int capacity;
    int size;
    int hashSize;
    Node **table;          // hash table array
    Node *head;            // dummy head of doubly linked list
    Node *tail;            // dummy tail of doubly linked list
} LRUCache;

/* Hash function */
static inline int hashIdx(LRUCache *cache, int key) {
    int idx = key % cache->hashSize;
    if (idx < 0) idx += cache->hashSize;
    return idx;
}

/* Remove node from doubly linked list */
static void removeNode(LRUCache *cache, Node *node) {
    node->prev->next = node->next;
    node->next->prev = node->prev;
}

/* Insert node right after head (most recently used position) */
static void addToHead(LRUCache *cache, Node *node) {
    node->next = cache->head->next;
    node->prev = cache->head;
    cache->head->next->prev = node;
    cache->head->next = node;
}

/* Move existing node to head (most recent) */
static void moveToHead(LRUCache *cache, Node *node) {
    removeNode(cache, node);
    addToHead(cache, node);
}

/* Pop the least recently used node (node before tail) */
static Node* popTail(LRUCache *cache) {
    Node *node = cache->tail->prev;
    if (node == cache->head) return NULL; // empty
    removeNode(cache, node);
    return node;
}

/* Find node in hash table */
static Node* findNode(LRUCache *cache, int key) {
    int idx = hashIdx(cache, key);
    Node *cur = cache->table[idx];
    while (cur) {
        if (cur->key == key) return cur;
        cur = cur->hnext;
    }
    return NULL;
}

/* Insert node into hash table */
static void insertHash(LRUCache *cache, Node *node) {
    int idx = hashIdx(cache, node->key);
    node->hnext = cache->table[idx];
    cache->table[idx] = node;
}

/* Remove node from hash table */
static void removeHash(LRUCache *cache, Node *node) {
    int idx = hashIdx(cache, node->key);
    Node *cur = cache->table[idx];
    Node *prev = NULL;
    while (cur) {
        if (cur == node) {
            if (prev)
                prev->hnext = cur->hnext;
            else
                cache->table[idx] = cur->hnext;
            break;
        }
        prev = cur;
        cur = cur->hnext;
    }
}

/* Create LRUCache */
LRUCache* lRUCacheCreate(int capacity) {
    if (capacity <= 0) capacity = 1;
    LRUCache *cache = (LRUCache*)malloc(sizeof(LRUCache));
    cache->capacity = capacity;
    cache->size = 0;
    /* Choose a prime number larger than twice the max capacity for hash table */
    int hs = 4099; // sufficient for given constraints
    while (hs < capacity * 2) hs = hs * 2 + 1;
    cache->hashSize = hs;
    cache->table = (Node**)calloc(cache->hashSize, sizeof(Node*));
    /* Dummy head and tail */
    cache->head = (Node*)malloc(sizeof(Node));
    cache->tail = (Node*)malloc(sizeof(Node));
    cache->head->prev = NULL;
    cache->head->next = cache->tail;
    cache->tail->prev = cache->head;
    cache->tail->next = NULL;
    return cache;
}

/* Get value */
int lRUCacheGet(LRUCache* obj, int key) {
    Node *node = findNode(obj, key);
    if (!node) return -1;
    moveToHead(obj, node);
    return node->value;
}

/* Put key-value pair */
void lRUCachePut(LRUCache* obj, int key, int value) {
    Node *node = findNode(obj, key);
    if (node) {
        node->value = value;
        moveToHead(obj, node);
        return;
    }
    /* Create new node */
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->key = key;
    newNode->value = value;
    addToHead(obj, newNode);
    insertHash(obj, newNode);
    obj->size++;
    if (obj->size > obj->capacity) {
        Node *tailNode = popTail(obj);
        if (tailNode) {
            removeHash(obj, tailNode);
            free(tailNode);
            obj->size--;
        }
    }
}

/* Free cache */
void lRUCacheFree(LRUCache* obj) {
    /* Free all nodes via doubly linked list */
    Node *cur = obj->head;
    while (cur) {
        Node *next = cur->next;
        free(cur);
        cur = next;
    }
    free(obj->table);
    free(obj);
}
```

## Csharp

```csharp
public class LRUCache
{
    private class Node
    {
        public int Key;
        public int Value;
        public Node Prev;
        public Node Next;
        public Node(int key, int value)
        {
            Key = key;
            Value = value;
        }
    }

    private readonly int _capacity;
    private readonly Dictionary<int, Node> _cache;
    private readonly Node _head;
    private readonly Node _tail;

    public LRUCache(int capacity)
    {
        _capacity = capacity;
        _cache = new Dictionary<int, Node>(capacity);
        _head = new Node(0, 0);
        _tail = new Node(0, 0);
        _head.Next = _tail;
        _tail.Prev = _head;
    }

    public int Get(int key)
    {
        if (!_cache.TryGetValue(key, out var node))
            return -1;

        MoveToHead(node);
        return node.Value;
    }

    public void Put(int key, int value)
    {
        if (_capacity == 0) return;

        if (_cache.TryGetValue(key, out var node))
        {
            node.Value = value;
            MoveToHead(node);
        }
        else
        {
            var newNode = new Node(key, value);
            _cache[key] = newNode;
            AddNode(newNode);

            if (_cache.Count > _capacity)
            {
                var tailPrev = PopTail();
                _cache.Remove(tailPrev.Key);
            }
        }
    }

    private void AddNode(Node node)
    {
        // Insert right after head
        node.Prev = _head;
        node.Next = _head.Next;
        _head.Next.Prev = node;
        _head.Next = node;
    }

    private void RemoveNode(Node node)
    {
        var prev = node.Prev;
        var next = node.Next;
        prev.Next = next;
        next.Prev = prev;
    }

    private void MoveToHead(Node node)
    {
        RemoveNode(node);
        AddNode(node);
    }

    private Node PopTail()
    {
        var res = _tail.Prev;
        RemoveNode(res);
        return res;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */
```

## Javascript

```javascript
/**
 * @param {number} capacity
 */
var LRUCache = function (capacity) {
    this.capacity = capacity;
    this.map = new Map(); // key -> node

    // dummy head and tail nodes to avoid edge checks
    this.head = {};
    this.tail = {};
    this.head.next = this.tail;
    this.tail.prev = this.head;
};

/**
 * Add node right after head (most recent)
 * @param {Object} node
 */
LRUCache.prototype._addNode = function (node) {
    node.prev = this.head;
    node.next = this.head.next;

    this.head.next.prev = node;
    this.head.next = node;
};

/**
 * Remove an existing node from the list
 * @param {Object} node
 */
LRUCache.prototype._removeNode = function (node) {
    const prev = node.prev;
    const next = node.next;

    prev.next = next;
    next.prev = prev;
};

/**
 * Move given node to head (most recent)
 * @param {Object} node
 */
LRUCache.prototype._moveToHead = function (node) {
    this._removeNode(node);
    this._addNode(node);
};

/**
 * Pop the least recently used node (right before tail)
 * @return {Object}
 */
LRUCache.prototype._popTail = function () {
    const node = this.tail.prev;
    this._removeNode(node);
    return node;
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function (key) {
    if (!this.map.has(key)) return -1;

    const node = this.map.get(key);
    // move accessed node to head
    this._moveToHead(node);
    return node.value;
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function (key, value) {
    if (this.map.has(key)) {
        const node = this.map.get(key);
        node.value = value;
        this._moveToHead(node);
    } else {
        const newNode = { key: key, value: value };
        this.map.set(key, newNode);
        this._addNode(newNode);

        if (this.map.size > this.capacity) {
            const tail = this._popTail();
            this.map.delete(tail.key);
        }
    }
};
```

## Typescript

```typescript
class LRUCache {
    private capacity: number;
    private map: Map<number, Node>;
    private head: Node;
    private tail: Node;

    constructor(capacity: number) {
        this.capacity = capacity;
        this.map = new Map();
        // dummy head and tail
        this.head = new Node(0, 0);
        this.tail = new Node(0, 0);
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    get(key: number): number {
        const node = this.map.get(key);
        if (!node) return -1;
        this.moveToHead(node);
        return node.value;
    }

    put(key: number, value: number): void {
        let node = this.map.get(key);
        if (node) {
            node.value = value;
            this.moveToHead(node);
        } else {
            const newNode = new Node(key, value);
            this.map.set(key, newNode);
            this.addNode(newNode);
            if (this.map.size > this.capacity) {
                const tail = this.popTail();
                if (tail) {
                    this.map.delete(tail.key);
                }
            }
        }
    }

    private addNode(node: Node): void {
        // always add right after head
        node.prev = this.head;
        node.next = this.head.next;
        if (this.head.next) this.head.next.prev = node;
        this.head.next = node;
    }

    private removeNode(node: Node): void {
        const prev = node.prev!;
        const next = node.next!;
        prev.next = next;
        next.prev = prev;
    }

    private moveToHead(node: Node): void {
        this.removeNode(node);
        this.addNode(node);
    }

    private popTail(): Node | null {
        // real tail is before dummy tail
        const res = this.tail.prev!;
        if (res === this.head) return null; // empty
        this.removeNode(res);
        return res;
    }
}

class Node {
    key: number;
    value: number;
    prev: Node | null = null;
    next: Node | null = null;
    constructor(key: number, value: number) {
        this.key = key;
        this.value = value;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

## Php

```php
<?php
class Node {
    public int $key;
    public int $val;
    public ?Node $prev = null;
    public ?Node $next = null;

    function __construct(int $key = 0, int $val = 0) {
        $this->key = $key;
        $this->val = $val;
    }
}

class LRUCache {
    private int $capacity;
    /** @var array<int, Node> */
    private array $cache = [];
    private Node $head;
    private Node $tail;

    function __construct($capacity) {
        $this->capacity = (int)$capacity;
        $this->head = new Node();
        $this->tail = new Node();
        $this->head->next = $this->tail;
        $this->tail->prev = $this->head;
    }

    function get($key) {
        $k = (int)$key;
        if (!isset($this->cache[$k])) {
            return -1;
        }
        $node = $this->cache[$k];
        $this->removeNode($node);
        $this->addNode($node);
        return $node->val;
    }

    function put($key, $value) {
        $k = (int)$key;
        $v = (int)$value;
        if (isset($this->cache[$k])) {
            $node = $this->cache[$k];
            $node->val = $v;
            $this->removeNode($node);
            $this->addNode($node);
        } else {
            $newNode = new Node($k, $v);
            $this->cache[$k] = $newNode;
            $this->addNode($newNode);
            if (count($this->cache) > $this->capacity) {
                $lru = $this->tail->prev;
                if ($lru !== null && $lru !== $this->head) {
                    $this->removeNode($lru);
                    unset($this->cache[$lru->key]);
                }
            }
        }
    }

    private function addNode(Node $node): void {
        $node->prev = $this->head;
        $node->next = $this->head->next;
        $this->head->next->prev = $node;
        $this->head->next = $node;
    }

    private function removeNode(Node $node): void {
        $prev = $node->prev;
        $next = $node->next;
        if ($prev !== null) {
            $prev->next = $next;
        }
        if ($next !== null) {
            $next->prev = $prev;
        }
        $node->prev = null;
        $node->next = null;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * $obj = new LRUCache($capacity);
 * $ret_1 = $obj->get($key);
 * $obj->put($key, $value);
 */
?>
```

## Swift

```swift
class LRUCache {
    private class Node {
        var key: Int
        var value: Int
        var prev: Node?
        var next: Node?
        init(_ key: Int, _ value: Int) {
            self.key = key
            self.value = value
        }
    }

    private let capacity: Int
    private var cache: [Int: Node] = [:]
    private let head = Node(0, 0)
    private let tail = Node(0, 0)

    init(_ capacity: Int) {
        self.capacity = capacity
        head.next = tail
        tail.prev = head
    }

    func get(_ key: Int) -> Int {
        guard let node = cache[key] else { return -1 }
        moveToHead(node)
        return node.value
    }

    func put(_ key: Int, _ value: Int) {
        if let node = cache[key] {
            node.value = value
            moveToHead(node)
        } else {
            let newNode = Node(key, value)
            cache[key] = newNode
            addNode(newNode)

            if cache.count > capacity {
                if let tailNode = popTail() {
                    cache.removeValue(forKey: tailNode.key)
                }
            }
        }
    }

    // MARK: - Helper methods

    private func addNode(_ node: Node) {
        node.prev = head
        node.next = head.next
        head.next?.prev = node
        head.next = node
    }

    private func removeNode(_ node: Node) {
        let prev = node.prev
        let next = node.next
        prev?.next = next
        next?.prev = prev
    }

    private func moveToHead(_ node: Node) {
        removeNode(node)
        addNode(node)
    }

    private func popTail() -> Node? {
        guard let node = tail.prev, node !== head else { return nil }
        removeNode(node)
        return node
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache(capacity)
 * let ret_1: Int = obj.get(key)
 * obj.put(key, value)
 */
```

## Kotlin

```kotlin
class LRUCache(capacity: Int) {

    private val cap = capacity
    private data class Node(var key: Int, var value: Int, var prev: Node? = null, var next: Node? = null)

    private val map = HashMap<Int, Node>()
    private val head = Node(0, 0)
    private val tail = Node(0, 0)

    init {
        head.next = tail
        tail.prev = head
    }

    private fun addNode(node: Node) {
        node.prev = head
        node.next = head.next
        head.next?.prev = node
        head.next = node
    }

    private fun removeNode(node: Node) {
        val prev = node.prev
        val next = node.next
        prev?.next = next
        next?.prev = prev
    }

    private fun moveToHead(node: Node) {
        removeNode(node)
        addNode(node)
    }

    private fun popTail(): Node? {
        val res = tail.prev
        if (res == head) return null
        removeNode(res!!)
        return res
    }

    fun get(key: Int): Int {
        val node = map[key] ?: return -1
        moveToHead(node)
        return node.value
    }

    fun put(key: Int, value: Int) {
        val node = map[key]
        if (node != null) {
            node.value = value
            moveToHead(node)
        } else {
            val newNode = Node(key, value)
            map[key] = newNode
            addNode(newNode)
            if (map.size > cap) {
                popTail()?.let { map.remove(it.key) }
            }
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

## Dart

```dart
class Node {
  int key;
  int value;
  Node? prev;
  Node? next;
  Node(this.key, this.value);
}

class LRUCache {
  final int _capacity;
  final Map<int, Node> _cache = {};
  late final Node _head;
  late final Node _tail;

  LRUCache(int capacity) : _capacity = capacity {
    _head = Node(0, 0);
    _tail = Node(0, 0);
    _head.next = _tail;
    _tail.prev = _head;
  }

  int get(int key) {
    final node = _cache[key];
    if (node == null) return -1;
    _moveToHead(node);
    return node.value;
  }

  void put(int key, int value) {
    if (_capacity == 0) return;
    final node = _cache[key];
    if (node != null) {
      node.value = value;
      _moveToHead(node);
    } else {
      if (_cache.length >= _capacity) {
        final lru = _popTail();
        if (lru != null) {
          _cache.remove(lru.key);
        }
      }
      final newNode = Node(key, value);
      _addNode(newNode);
      _cache[key] = newNode;
    }
  }

  void _addNode(Node node) {
    node.prev = _head;
    node.next = _head.next;
    _head.next?.prev = node;
    _head.next = node;
  }

  void _removeNode(Node node) {
    final prev = node.prev;
    final next = node.next;
    if (prev != null) prev.next = next;
    if (next != null) next.prev = prev;
  }

  void _moveToHead(Node node) {
    _removeNode(node);
    _addNode(node);
  }

  Node? _popTail() {
    final lru = _tail.prev;
    if (lru == null || lru == _head) return null;
    _removeNode(lru);
    return lru;
  }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = LRUCache(capacity);
 * int param1 = obj.get(key);
 * obj.put(key,value);
 */
```

## Golang

```go
type node struct {
	key  int
	val  int
	prev *node
	next *node
}

type LRUCache struct {
	capacity int
	cache    map[int]*node
	head     *node
	tail     *node
}

func Constructor(capacity int) LRUCache {
	h := &node{}
	t := &node{}
	h.next = t
	t.prev = h
	return LLRUCache{
		capacity: capacity,
		cache:    make(map[int]*node),
		head:     h,
		tail:     t,
	}
}

func (this *LRUCache) addNode(n *node) {
	n.prev = this.head
	n.next = this.head.next
	this.head.next.prev = n
	this.head.next = n
}

func (this *LRUCache) removeNode(n *node) {
	prev := n.prev
	next := n.next
	prev.next = next
	next.prev = prev
}

func (this *LRUCache) moveToHead(n *node) {
	this.removeNode(n)
	this.addNode(n)
}

func (this *LRUCache) popTail() *node {
	n := this.tail.prev
	this.removeNode(n)
	return n
}

func (this *LRUCache) Get(key int) int {
	if n, ok := this.cache[key]; ok {
		this.moveToHead(n)
		return n.val
	}
	return -1
}

func (this *LRUCache) Put(key int, value int) {
	if n, ok := this.cache[key]; ok {
		n.val = value
		this.moveToHead(n)
		return
	}
	newNode := &node{key: key, val: value}
	this.cache[key] = newNode
	this.addNode(newNode)

	if len(this.cache) > this.capacity {
		tail := this.popTail()
		delete(this.cache, tail.key)
	}
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
```

## Ruby

```ruby
class LRUCache
  Node = Struct.new(:key, :val, :prev, :next)

=begin
    :type capacity: Integer
=end
  def initialize(capacity)
    @capacity = capacity
    @map = {}
    @head = Node.new(nil, nil, nil, nil) # dummy head
    @tail = Node.new(nil, nil, nil, nil) # dummy tail
    @head.next = @tail
    @tail.prev = @head
  end

=begin
    :type key: Integer
    :rtype: Integer
=end
  def get(key)
    node = @map[key]
    return -1 unless node
    _remove(node)
    _add_to_head(node)
    node.val
  end

=begin
    :type key: Integer
    :type value: Integer
    :rtype: Void
=end
  def put(key, value)
    if (node = @map[key])
      node.val = value
      _remove(node)
      _add_to_head(node)
    else
      if @capacity == 0
        return
      end
      if @map.size >= @capacity
        lru = @tail.prev
        _remove(lru)
        @map.delete(lru.key)
      end
      new_node = Node.new(key, value, nil, nil)
      _add_to_head(new_node)
      @map[key] = new_node
    end
  end

  private

  def _remove(node)
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node
  end

  def _add_to_head(node)
    first = @head.next
    node.next = first
    node.prev = @head
    @head.next = node
    first.prev = node
  end
end
```

## Scala

```scala
import scala.collection.mutable

class LRUCache(_capacity: Int) {

  private class Node(val key: Int, var value: Int) {
    var prev: Node = _
    var next: Node = _
  }

  private val capacity: Int = _capacity
  private val cache = mutable.HashMap.empty[Int, Node]
  private val head: Node = new Node(0, 0) // dummy head
  private val tail: Node = new Node(0, 0) // dummy tail

  // initialize the double linked list
  head.next = tail
  tail.prev = head

  private def addNode(node: Node): Unit = {
    node.prev = head
    node.next = head.next
    head.next.prev = node
    head.next = node
  }

  private def removeNode(node: Node): Unit = {
    val prevNode = node.prev
    val nextNode = node.next
    prevNode.next = nextNode
    nextNode.prev = prevNode
  }

  private def moveToHead(node: Node): Unit = {
    removeNode(node)
    addNode(node)
  }

  private def popTail(): Node = {
    val res = tail.prev
    removeNode(res)
    res
  }

  def get(key: Int): Int = {
    cache.get(key) match {
      case Some(node) =>
        moveToHead(node)
        node.value
      case None => -1
    }
  }

  def put(key: Int, value: Int): Unit = {
    cache.get(key) match {
      case Some(node) =>
        node.value = value
        moveToHead(node)
      case None =>
        val newNode = new Node(key, value)
        cache.put(key, newNode)
        addNode(newNode)

        if (cache.size > capacity) {
          val tailNode = popTail()
          cache.remove(tailNode.key)
        }
    }
  }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * val obj = new LRUCache(capacity)
 * val param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

## Rust

```rust
use std::cell::RefCell;
use std::collections::HashMap;

struct Node {
    key: i32,
    prev: Option<*mut Node>,
    next: Option<*mut Node>,
}

pub struct LRUCache {
    capacity: usize,
    map: RefCell<HashMap<i32, (i32, *mut Node)>>,
    head: *mut Node,
    tail: *mut Node,
    // keep dummy nodes owned so they are not dropped
    _head_dummy: Box<Node>,
    _tail_dummy: Box<Node>,
}

impl LRUCache {
    fn new(capacity: i32) -> Self {
        let mut head = Box::new(Node { key: 0, prev: None, next: None });
        let mut tail = Box::new(Node { key: 0, prev: None, next: None });

        let head_ptr: *mut Node = &mut *head;
        let tail_ptr: *mut Node = &mut *tail;

        unsafe {
            (*head_ptr).next = Some(tail_ptr);
            (*tail_ptr).prev = Some(head_ptr);
        }

        LRUCache {
            capacity: capacity as usize,
            map: RefCell::new(HashMap::new()),
            head: head_ptr,
            tail: tail_ptr,
            _head_dummy: head,
            _tail_dummy: tail,
        }
    }

    fn get(&self, key: i32) -> i32 {
        let mut map = self.map.borrow_mut();
        if let Some((value, node_ptr)) = map.get(&key).cloned() {
            // move accessed node to front
            unsafe {
                // detach
                let prev = (*node_ptr).prev.unwrap();
                let next = (*node_ptr).next.unwrap();
                (*prev).next = Some(next);
                (*next).prev = Some(prev);

                // insert after head
                let first = (*self.head).next.unwrap();
                (*node_ptr).prev = Some(self.head);
                (*node_ptr).next = Some(first);
                (*first).prev = Some(node_ptr);
                (*self.head).next = Some(node_ptr);
            }
            value
        } else {
            -1
        }
    }

    fn put(&self, key: i32, value: i32) {
        let mut map = self.map.borrow_mut();

        if let Some((_old_val, node_ptr)) = map.get_mut(&key) {
            // update value
            *_old_val = value;
            // move to front
            unsafe {
                // detach
                let prev = (*node_ptr).prev.unwrap();
                let next = (*node_ptr).next.unwrap();
                (*prev).next = Some(next);
                (*next).prev = Some(prev);

                // insert after head
                let first = (*self.head).next.unwrap();
                (*node_ptr).prev = Some(self.head);
                (*node_ptr).next = Some(first);
                (*first).prev = Some(node_ptr);
                (*self.head).next = Some(node_ptr);
            }
            return;
        }

        // need to insert new node
        if map.len() == self.capacity && self.capacity > 0 {
            // evict least recently used (node before tail)
            unsafe {
                let lru_node = (*self.tail).prev.unwrap();
                let lru_key = (*lru_node).key;

                let prev = (*lru_node).prev.unwrap();
                (*prev).next = Some(self.tail);
                (*self.tail).prev = Some(prev);

                map.remove(&lru_key);
                // memory leak of the evicted node is acceptable for this problem
            }
        }

        // create new node (leaked)
        let mut boxed = Box::new(Node {
            key,
            prev: None,
            next: None,
        });
        let node_ptr: *mut Node = &mut *boxed;
        std::mem::forget(boxed); // leak to keep it alive

        unsafe {
            // insert after head
            let first = (*self.head).next.unwrap();
            (*node_ptr).prev = Some(self.head);
            (*node_ptr).next = Some(first);
            (*first).prev = Some(node_ptr);
            (*self.head).next = Some(node_ptr);
        }

        map.insert(key, (value, node_ptr));
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache::new(capacity);
 * let ret_1: i32 = obj.get(key);
 * obj.put(key, value);
 */
```

## Racket

```racket
(struct node (key value prev next) #:mutable)

(define lru-cache%
  (class object%
    (init-field capacity)
    (field
      [hash (make-hash)]
      [head #f]
      [tail #f])

    (super-new)

    ;; Initialize sentinel head and tail nodes
    (let* ([h (node #f 0 #f #f)]
           [t (node #f 0 #f #f)])
      (set-node-prev! t h)
      (set-node-next! h t)
      (set! head h)
      (set! tail t))

    ;; Remove a node from its current position
    (define (remove-node n)
      (let ([p (node-prev n)]
            [ne (node-next n)])
        (when p (set-node-next! p ne))
        (when ne (set-node-prev! ne p))))

    ;; Insert a node right after head (most recently used)
    (define (add-to-front n)
      (let ([first (node-next head)])
        (set-node-prev! n head)
        (set-node-next! n first)
        (set-node-prev! first n)
        (set-node-next! head n)))

    ;; Move an existing node to the front
    (define (move-to-front n)
      (remove-node n)
      (add-to-front n))

    ;; Get value for key, or -1 if not present
    (define/public (get key)
      (let ([n (hash-ref hash key #f)])
        (if n
            (begin
              (move-to-front n)
              (node-value n))
            -1)))

    ;; Put key/value pair into cache
    (define/public (put key value)
      (let ([existing (hash-ref hash key #f)])
        (if existing
            (begin
              (set-node-value! existing value)
              (move-to-front existing))
            (begin
              (when (= (hash-count hash) capacity)
                ;; Evict least recently used node (just before tail)
                (let ([lru (node-prev tail)])
                  (remove-node lru)
                  (hash-remove! hash (node-key lru))))
              (let ([new-node (node key value #f #f)])
                (add-to-front new-node)
                (hash-set! hash key new-node))))))

    ))
```

## Erlang

```erlang
-module(lru_cache).
-export([lru_cache_init_/1, lru_cache_get/1, lru_cache_put/2]).

%% Initialization
lru_cache_init_(Capacity) ->
    catch ets:delete(lru_cache_tab),
    catch ets:delete(lru_list_tab),
    ets:new(lru_cache_tab, [named_table, public]),
    ets:new(lru_list_tab, [named_table, public]),
    put(lru_capacity, Capacity),
    put(lru_size, 0),
    put(lru_head, undefined),
    put(lru_tail, undefined),
    put(lru_next_id, 0).

%% Get operation
lru_cache_get(Key) ->
    case ets:lookup(lru_cache_tab, Key) of
        [] -> -1;
        [{Key,{Value,NodeId}}] ->
            move_to_front(NodeId),
            Value
    end.

%% Put operation
lru_cache_put(Key, Value) ->
    case ets:lookup(lru_cache_tab, Key) of
        [{Key,{_, NodeId}}] ->
            ets:insert(lru_cache_tab, {Key,{Value,NodeId}}),
            move_to_front(NodeId);
        [] ->
            Capacity = get(lru_capacity),
            Size = get(lru_size),
            if Size >= Capacity ->
                    evict_tail(),
                    put(lru_size, get(lru_size) - 1);
               true -> ok
            end,
            add_node(Key, Value)
    end.

%% Helper: Evict least recently used (tail)
evict_tail() ->
    TailNode = get(lru_tail),
    case ets:lookup(lru_list_tab, TailNode) of
        [{TailNode,{Prev, undefined, EvictKey}}] ->
            ets:delete(lru_cache_tab, EvictKey),
            case Prev of
                undefined ->
                    put(lru_head, undefined),
                    put(lru_tail, undefined);
                _ ->
                    ets:update_element(lru_list_tab, Prev, {2, undefined}),
                    put(lru_tail, Prev)
            end,
            ets:delete(lru_list_tab, TailNode);
        [] -> ok
    end.

%% Helper: Add new node as most recent (head)
add_node(Key, Value) ->
    NodeId = get(lru_next_id),
    put(lru_next_id, NodeId + 1),

    Head = get(lru_head),
    ets:insert(lru_list_tab, {NodeId,{undefined, Head, Key}}),

    case Head of
        undefined -> ok;
        _ -> ets:update_element(lru_list_tab, Head, {1, NodeId})
    end,

    put(lru_head, NodeId),
    case get(lru_tail) of
        undefined -> put(lru_tail, NodeId);
        _ -> ok
    end,

    ets:insert(lru_cache_tab, {Key,{Value,NodeId}}),
    put(lru_size, get(lru_size) + 1).

%% Helper: Move accessed node to front (head)
move_to_front(NodeId) ->
    Head = get(lru_head),
    if NodeId == Head ->
            ok;
       true ->
            [{NodeId,{Prev, Next, _Key}}] = ets:lookup(lru_list_tab, NodeId),

            % Detach from current position
            case Prev of
                undefined -> ok;
                _ -> ets:update_element(lru_list_tab, Prev, {2, Next})
            end,
            case Next of
                undefined ->
                    put(lru_tail, Prev);
                _ -> ets:update_element(lru_list_tab, Next, {1, Prev})
            end,

            % Attach at front
            OldHead = Head,
            ets:update_element(lru_list_tab, NodeId, [{1, undefined}, {2, OldHead}]),
            case OldHead of
                undefined -> ok;
                _ -> ets:update_element(lru_list_tab, OldHead, {1, NodeId})
            end,
            put(lru_head, NodeId)
    end.
```

## Elixir

```elixir
defmodule LRUCache do
  @spec init_(capacity :: integer) :: any
  def init_(capacity) do
    state = %{
      cap: capacity,
      map: %{},
      prev: %{},
      next: %{},
      head: nil,
      tail: nil
    }

    Process.put(:lru_state, state)
  end

  @spec get(key :: integer) :: integer
  def get(key) do
    state = get_state()

    case Map.fetch(state.map, key) do
      :error ->
        -1

      {:ok, value} ->
        state = move_to_head(state, key)
        set_state(state)
        value
    end
  end

  @spec put(key :: integer, value :: integer) :: any
  def put(key, value) do
    state = get_state()

    if Map.has_key?(state.map, key) do
      state = %{state | map: Map.put(state.map, key, value)}
      state = move_to_head(state, key)
      set_state(state)
    else
      state =
        if map_size(state.map) == state.cap do
          remove_tail(state)
        else
          state
        end

      state = insert_head(state, key, value)
      set_state(state)
    end
  end

  # ------------------------------------------------------------------
  # Private helpers
  defp get_state do
    Process.get(:lru_state) || %{}
  end

  defp set_state(state) do
    Process.put(:lru_state, state)
  end

  defp move_to_head(state, key) do
    if state.head == key do
      state
    else
      state = detach(state, key)
      value = Map.fetch!(state.map, key)
      insert_head(state, key, value)
    end
  end

  defp detach(state, key) do
    p = Map.get(state.prev, key)
    n = Map.get(state.next, key)

    prev_map =
      if p != nil do
        Map.put(state.prev, p, n)
      else
        state.prev
      end

    next_map =
      if n != nil do
        Map.put(state.next, n, p)
      else
        state.next
      end

    # remove key's own entries
    prev_map = Map.delete(prev_map, key)
    next_map = Map.delete(next_map, key)

    head = if state.head == key, do: n, else: state.head
    tail = if state.tail == key, do: p, else: state.tail

    %{state |
      prev: prev_map,
      next: next_map,
      head: head,
      tail: tail}
  end

  defp insert_head(state, key, value) do
    prev_map = Map.put(state.prev, key, nil)
    next_map = Map.put(state.next, key, state.head)

    {prev_map, new_head} =
      case state.head do
        nil ->
          {prev_map, key}

        old_head ->
          {Map.put(prev_map, old_head, key), key}
      end

    new_tail = if state.tail == nil, do: key, else: state.tail

    %{state |
      map: Map.put(state.map, key, value),
      prev: prev_map,
      next: next_map,
      head: new_head,
      tail: new_tail}
  end

  defp remove_tail(state) do
    evict_key = state.tail
    state = detach(state, evict_key)
    %{state | map: Map.delete(state.map, evict_key)}
  end
end
```
