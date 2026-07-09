# 0432. All O`one Data Structure

## Cpp

```cpp
class AllOne {
private:
    struct Node {
        int cnt;
        std::unordered_set<std::string> keys;
        Node* prev;
        Node* next;
        Node(int c) : cnt(c), prev(nullptr), next(nullptr) {}
    };
    
    Node* head;
    Node* tail;
    std::unordered_map<std::string, Node*> keyNode;
    
    void insertAfter(Node* cur, Node* node) {
        node->prev = cur;
        node->next = cur->next;
        cur->next->prev = node;
        cur->next = node;
    }
    
    void removeNode(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
        delete node;
    }
    
public:
    AllOne() {
        head = new Node(0); // dummy head
        tail = new Node(0); // dummy tail
        head->next = tail;
        tail->prev = head;
    }
    
    void inc(std::string key) {
        if (keyNode.find(key) == keyNode.end()) {
            // New key, need count 1 node
            Node* first = head->next;
            if (first == tail || first->cnt != 1) {
                Node* n = new Node(1);
                insertAfter(head, n);
                first = n;
            }
            first->keys.insert(key);
            keyNode[key] = first;
        } else {
            Node* cur = keyNode[key];
            int c = cur->cnt;
            Node* nxt = cur->next;
            if (nxt == tail || nxt->cnt != c + 1) {
                Node* n = new Node(c + 1);
                insertAfter(cur, n);
                nxt = n;
            }
            nxt->keys.insert(key);
            keyNode[key] = nxt;
            cur->keys.erase(key);
            if (cur->keys.empty()) removeNode(cur);
        }
    }
    
    void dec(std::string key) {
        auto it = keyNode.find(key);
        if (it == keyNode.end()) return; // should not happen per constraints
        Node* cur = it->second;
        int c = cur->cnt;
        cur->keys.erase(key);
        if (c == 1) {
            keyNode.erase(it);
        } else {
            Node* prev = cur->prev;
            if (prev == head || prev->cnt != c - 1) {
                Node* n = new Node(c - 1);
                insertAfter(prev, n);
                prev = n;
            }
            prev->keys.insert(key);
            keyNode[key] = prev;
        }
        if (cur->keys.empty()) removeNode(cur);
    }
    
    std::string getMaxKey() {
        if (tail->prev == head) return "";
        return *(tail->prev->keys.begin());
    }
    
    std::string getMinKey() {
        if (head->next == tail) return "";
        return *(head->next->keys.begin());
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */
```

## Java

```java
class AllOne {
    private static class Node {
        int count;
        java.util.HashSet<String> keys;
        Node prev, next;
        Node(int c) {
            count = c;
            keys = new java.util.HashSet<>();
        }
    }

    private final Node head;
    private final Node tail;
    private final java.util.HashMap<String, Node> keyNodeMap;

    public AllOne() {
        head = new Node(0);
        tail = new Node(0);
        head.next = tail;
        tail.prev = head;
        keyNodeMap = new java.util.HashMap<>();
    }

    public void inc(String key) {
        if (!keyNodeMap.containsKey(key)) {
            // need count 1 node
            Node first = head.next;
            if (first == tail || first.count != 1) {
                Node n = new Node(1);
                insertAfter(head, n);
                first = n;
            }
            first.keys.add(key);
            keyNodeMap.put(key, first);
        } else {
            Node cur = keyNodeMap.get(key);
            Node nxt = cur.next;
            int newCnt = cur.count + 1;
            if (nxt == tail || nxt.count != newCnt) {
                Node n = new Node(newCnt);
                insertAfter(cur, n);
                nxt = n;
            }
            cur.keys.remove(key);
            nxt.keys.add(key);
            keyNodeMap.put(key, nxt);
            if (cur.keys.isEmpty()) {
                removeNode(cur);
            }
        }
    }

    public void dec(String key) {
        Node cur = keyNodeMap.get(key); // guaranteed to exist
        int newCnt = cur.count - 1;
        if (newCnt == 0) {
            keyNodeMap.remove(key);
        } else {
            Node prev = cur.prev;
            if (prev == head || prev.count != newCnt) {
                Node n = new Node(newCnt);
                insertAfter(prev, n);
                prev = n;
            }
            cur.keys.remove(key);
            prev.keys.add(key);
            keyNodeMap.put(key, prev);
        }
        if (cur.keys.isEmpty()) {
            removeNode(cur);
        }
    }

    public String getMaxKey() {
        if (tail.prev == head) return "";
        Node maxNode = tail.prev;
        // any element
        for (String k : maxNode.keys) {
            return k;
        }
        return "";
    }

    public String getMinKey() {
        if (head.next == tail) return "";
        Node minNode = head.next;
        for (String k : minNode.keys) {
            return k;
        }
        return "";
    }

    private void insertAfter(Node node, Node newNode) {
        newNode.prev = node;
        newNode.next = node.next;
        node.next.prev = newNode;
        node.next = newNode;
    }

    private void removeNode(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne();
 * obj.inc(key);
 * obj.dec(key);
 * String param_3 = obj.getMaxKey();
 * String param_4 = obj.getMinKey();
 */
```

## Python

```python
class Node:
    __slots__ = ('freq', 'keys', 'prev', 'next')
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)   # dummy head
        self.tail = Node(0)   # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key2node = {}

    def _add_node_after(self, node, prev):
        """Insert node right after prev."""
        nxt = prev.next
        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node

    def _remove_node(self, node):
        """Detach node from the list."""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        if key not in self.key2node:
            # need a node with freq 1 right after head
            if self.head.next != self.tail and self.head.next.freq == 1:
                node = self.head.next
            else:
                node = Node(1)
                self._add_node_after(node, self.head)
            node.keys.add(key)
            self.key2node[key] = node
        else:
            cur = self.key2node[key]
            nxt = cur.next
            new_freq = cur.freq + 1
            if nxt != self.tail and nxt.freq == new_freq:
                target = nxt
            else:
                target = Node(new_freq)
                self._add_node_after(target, cur)
            target.keys.add(key)
            self.key2node[key] = target

            cur.keys.remove(key)
            if not cur.keys:
                self._remove_node(cur)

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        cur = self.key2node[key]
        cur.keys.remove(key)
        if cur.freq == 1:
            del self.key2node[key]
        else:
            prev = cur.prev
            new_freq = cur.freq - 1
            if prev != self.head and prev.freq == new_freq:
                target = prev
            else:
                target = Node(new_freq)
                self._add_node_after(target, prev)   # insert before cur
            target.keys.add(key)
            self.key2node[key] = target

        if not cur.keys:
            self._remove_node(cur)

    def getMaxKey(self):
        """
        :rtype: str
        """
        if self.tail.prev == self.head:
            return ""
        # return any key from the max freq node
        node = self.tail.prev
        return next(iter(node.keys))

    def getMinKey(self):
        """
        :rtype: str
        """
        if self.head.next == self.tail:
            return ""
        node = self.head.next
        return next(iter(node.keys))
```

## Python3

```python
class Node:
    __slots__ = ('freq', 'keys', 'prev', 'next')
    def __init__(self, freq: int):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.head = Node(0)          # dummy head (freq less than any real node)
        self.tail = Node(0)          # dummy tail (freq greater than any real node)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key2node = {}           # key -> Node

    def _add_node_after(self, new_node: Node, prev_node: Node):
        nxt = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = nxt
        nxt.prev = new_node

    def _remove_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def inc(self, key: str) -> None:
        if key not in self.key2node:
            # need a node with freq 1 right after head
            first = self.head.next
            if first is self.tail or first.freq != 1:
                new_node = Node(1)
                self._add_node_after(new_node, self.head)
                target = new_node
            else:
                target = first
            target.keys.add(key)
            self.key2node[key] = target
        else:
            cur = self.key2node[key]
            nxt = cur.next
            if nxt is self.tail or nxt.freq != cur.freq + 1:
                new_node = Node(cur.freq + 1)
                self._add_node_after(new_node, cur)
                target = new_node
            else:
                target = nxt
            target.keys.add(key)
            self.key2node[key] = target

            cur.keys.remove(key)
            if not cur.keys:
                self._remove_node(cur)

    def dec(self, key: str) -> None:
        cur = self.key2node[key]
        if cur.freq == 1:
            del self.key2node[key]
        else:
            prev = cur.prev
            if prev is self.head or prev.freq != cur.freq - 1:
                new_node = Node(cur.freq - 1)
                self._add_node_after(new_node, prev)
                target = new_node
            else:
                target = prev
            target.keys.add(key)
            self.key2node[key] = target

        cur.keys.remove(key)
        if not cur.keys:
            self._remove_node(cur)

    def getMaxKey(self) -> str:
        if self.tail.prev is self.head:
            return ""
        # return any key from the max frequency node
        node = self.tail.prev
        return next(iter(node.keys))

    def getMinKey(self) -> str:
        if self.head.next is self.tail:
            return ""
        node = self.head.next
        return next(iter(node.keys))
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct Node Node;
typedef struct Entry Entry;

struct Node {
    int freq;
    Node *prev, *next;
    Entry *khead;               // head of keys list for this frequency
};

struct Entry {
    char *key;
    Node *node;                 // pointer to its frequency node
    Entry *hnext;               // next in hash bucket
    Entry *knext, *kprev;       // links inside the node's key list
};

typedef struct {
    Node *head, *tail;          // dummy head and tail
    Entry **table;
    int cap;
} AllOne;

/* ---------- Helper Functions ---------- */

static unsigned int hash_str(const char *s) {
    unsigned long h = 5381;
    while (*s)
        h = ((h << 5) + h) + (unsigned char)*s++;
    return (unsigned int)h;
}

static Node* create_node(int freq) {
    Node *n = (Node*)malloc(sizeof(Node));
    n->freq = freq;
    n->prev = n->next = NULL;
    n->khead = NULL;
    return n;
}

static void insert_after(Node *cur, Node *node) {
    node->prev = cur;
    node->next = cur->next;
    cur->next->prev = node;
    cur->next = node;
}

static void insert_before(Node *cur, Node *node) {
    node->next = cur;
    node->prev = cur->prev;
    cur->prev->next = node;
    cur->prev = node;
}

static void remove_node(Node *node) {
    node->prev->next = node->next;
    node->next->prev = node->prev;
}

/* key list operations */
static void add_key_to_node(Entry *e, Node *n) {
    e->node = n;
    e->kprev = NULL;
    e->knext = n->khead;
    if (n->khead) n->khead->kprev = e;
    n->khead = e;
}

static void remove_key_from_node(Entry *e) {
    Node *n = e->node;
    if (e->kprev)
        e->kprev->knext = e->knext;
    else
        n->khead = e->knext;
    if (e->knext)
        e->knext->kprev = e->kprev;
    e->kprev = e->knext = NULL;
}

/* hash table delete */
static void delete_entry(AllOne *obj, Entry *e) {
    unsigned int idx = hash_str(e->key) % obj->cap;
    Entry *cur = obj->table[idx];
    Entry *prev = NULL;
    while (cur) {
        if (cur == e) {
            if (prev)
                prev->hnext = cur->hnext;
            else
                obj->table[idx] = cur->hnext;
            free(cur->key);
            free(cur);
            return;
        }
        prev = cur;
        cur = cur->hnext;
    }
}

/* ---------- API Functions ---------- */

AllOne* allOneCreate() {
    AllOne *obj = (AllOne*)malloc(sizeof(AllOne));
    obj->cap = 131071;                     // a prime > 1e5
    obj->table = (Entry**)calloc(obj->cap, sizeof(Entry*));

    obj->head = create_node(-1);
    obj->tail = create_node(-1);
    obj->head->next = obj->tail;
    obj->tail->prev = obj->head;

    return obj;
}

void allOneInc(AllOne* obj, char* key) {
    unsigned int idx = hash_str(key) % obj->cap;
    Entry *e = obj->table[idx];
    while (e && strcmp(e->key, key) != 0) e = e->hnext;

    if (!e) {   // new key
        e = (Entry*)malloc(sizeof(Entry));
        e->key = strdup(key);
        e->node = NULL;
        e->knext = e->kprev = NULL;
        e->hnext = obj->table[idx];
        obj->table[idx] = e;

        Node *first = obj->head->next;
        if (first == obj->tail || first->freq != 1) {
            Node *n = create_node(1);
            insert_after(obj->head, n);
            first = n;
        }
        add_key_to_node(e, first);
    } else {   // existing key
        Node *cur = e->node;
        int newFreq = cur->freq + 1;

        remove_key_from_node(e);

        Node *nxt = cur->next;
        if (nxt == obj->tail || nxt->freq != newFreq) {
            Node *n = create_node(newFreq);
            insert_after(cur, n);
            nxt = n;
        }
        add_key_to_node(e, nxt);

        if (cur->khead == NULL) {
            remove_node(cur);
            free(cur);
        }
    }
}

void allOneDec(AllOne* obj, char* key) {
    unsigned int idx = hash_str(key) % obj->cap;
    Entry *e = obj->table[idx];
    while (e && strcmp(e->key, key) != 0) e = e->hnext;

    if (!e) return;   // should not happen per constraints

    Node *cur = e->node;
    int freq = cur->freq;

    remove_key_from_node(e);

    if (freq == 1) {
        delete_entry(obj, e);
    } else {
        int newFreq = freq - 1;
        Node *prev = cur->prev;
        if (prev == obj->head || prev->freq != newFreq) {
            Node *n = create_node(newFreq);
            insert_before(cur, n);
            prev = n;
        }
        add_key_to_node(e, prev);
    }

    if (cur->khead == NULL) {
        remove_node(cur);
        free(cur);
    }
}

char* allOneGetMaxKey(AllOne* obj) {
    Node *n = obj->tail->prev;
    if (n == obj->head) return "";
    return strdup(n->khead->key);
}

char* allOneGetMinKey(AllOne* obj) {
    Node *n = obj->head->next;
    if (n == obj->tail) return "";
    return strdup(n->khead->key);
}

void allOneFree(AllOne* obj) {
    // free hash entries
    for (int i = 0; i < obj->cap; ++i) {
        Entry *e = obj->table[i];
        while (e) {
            Entry *next = e->hnext;
            free(e->key);
            free(e);
            e = next;
        }
    }
    free(obj->table);

    // free nodes
    Node *cur = obj->head;
    while (cur) {
        Node *next = cur->next;
        free(cur);
        cur = next;
    }

    free(obj);
}

/**
 * Your AllOne struct will be instantiated and called as such:
 * AllOne* obj = allOneCreate();
 * allOneInc(obj, key);
 * allOneDec(obj, key);
 * char* param_3 = allOneGetMaxKey(obj);
 * char* param_4 = allOneGetMinKey(obj);
 * allOneFree(obj);
 */
```

## Csharp

```csharp
using System.Collections.Generic;

public class AllOne
{
    private class Node
    {
        public int Count;
        public HashSet<string> Keys;
        public Node Prev;
        public Node Next;

        public Node(int count)
        {
            Count = count;
            Keys = new HashSet<string>();
        }
    }

    private readonly Dictionary<string, Node> _keyNode;
    private readonly Node _head;
    private readonly Node _tail;

    public AllOne()
    {
        _keyNode = new Dictionary<string, Node>();
        _head = new Node(0);
        _tail = new Node(0);
        _head.Next = _tail;
        _tail.Prev = _head;
    }

    public void Inc(string key)
    {
        if (!_keyNode.TryGetValue(key, out var cur))
        {
            // New key, need count 1 node
            var first = _head.Next;
            if (first == _tail || first.Count != 1)
            {
                var n = new Node(1);
                InsertAfter(_head, n);
                first = n;
            }
            first.Keys.Add(key);
            _keyNode[key] = first;
        }
        else
        {
            int newCount = cur.Count + 1;
            var nxt = cur.Next;
            if (nxt == _tail || nxt.Count != newCount)
            {
                var n = new Node(newCount);
                InsertAfter(cur, n);
                nxt = n;
            }
            nxt.Keys.Add(key);
            _keyNode[key] = nxt;

            cur.Keys.Remove(key);
            if (cur.Keys.Count == 0)
                RemoveNode(cur);
        }
    }

    public void Dec(string key)
    {
        var cur = _keyNode[key];
        cur.Keys.Remove(key);

        if (cur.Count == 1)
        {
            _keyNode.Remove(key);
        }
        else
        {
            int newCount = cur.Count - 1;
            var prev = cur.Prev;
            if (prev == _head || prev.Count != newCount)
            {
                var n = new Node(newCount);
                InsertAfter(prev, n);
                prev = n;
            }
            prev.Keys.Add(key);
            _keyNode[key] = prev;
        }

        if (cur.Keys.Count == 0)
            RemoveNode(cur);
    }

    public string GetMaxKey()
    {
        var node = _tail.Prev;
        if (node == _head) return "";
        foreach (var k in node.Keys)
            return k;
        return "";
    }

    public string GetMinKey()
    {
        var node = _head.Next;
        if (node == _tail) return "";
        foreach (var k in node.Keys)
            return k;
        return "";
    }

    private void InsertAfter(Node node, Node newNode)
    {
        newNode.Prev = node;
        newNode.Next = node.Next;
        node.Next.Prev = newNode;
        node.Next = newNode;
    }

    private void RemoveNode(Node node)
    {
        node.Prev.Next = node.Next;
        node.Next.Prev = node.Prev;
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne();
 * obj.Inc(key);
 * obj.Dec(key);
 * string param_3 = obj.GetMaxKey();
 * string param_4 = obj.GetMinKey();
 */
```

## Javascript

```javascript
var AllOne = function() {
    // Dummy head and tail nodes
    this.head = {freq: 0, prev: null, next: null, keys: new Set()};
    this.tail = {freq: 0, prev: null, next: null, keys: new Set()};
    this.head.next = this.tail;
    this.tail.prev = this.head;
    // key -> node mapping
    this.keyMap = new Map();
};

AllOne.prototype._addNodeAfter = function(prevNode, newNode) {
    newNode.prev = prevNode;
    newNode.next = prevNode.next;
    prevNode.next.prev = newNode;
    prevNode.next = newNode;
};

AllOne.prototype._removeNode = function(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
};

AllOne.prototype.inc = function(key) {
    if (!this.keyMap.has(key)) {
        // Insert into frequency 1
        let first = this.head.next;
        if (first === this.tail || first.freq !== 1) {
            const newNode = {freq: 1, prev: null, next: null, keys: new Set()};
            this._addNodeAfter(this.head, newNode);
            first = newNode;
        }
        first.keys.add(key);
        this.keyMap.set(key, first);
    } else {
        const cur = this.keyMap.get(key);
        let nxt = cur.next;
        if (nxt === this.tail || nxt.freq !== cur.freq + 1) {
            const newNode = {freq: cur.freq + 1, prev: null, next: null, keys: new Set()};
            this._addNodeAfter(cur, newNode);
            nxt = newNode;
        }
        nxt.keys.add(key);
        this.keyMap.set(key, nxt);
        cur.keys.delete(key);
        if (cur.keys.size === 0) {
            this._removeNode(cur);
        }
    }
};

AllOne.prototype.dec = function(key) {
    const cur = this.keyMap.get(key); // guaranteed to exist
    cur.keys.delete(key);
    if (cur.freq === 1) {
        this.keyMap.delete(key);
    } else {
        let prev = cur.prev;
        if (prev === this.head || prev.freq !== cur.freq - 1) {
            const newNode = {freq: cur.freq - 1, prev: null, next: null, keys: new Set()};
            this._addNodeAfter(prev, newNode);
            prev = newNode;
        }
        prev.keys.add(key);
        this.keyMap.set(key, prev);
    }
    if (cur.keys.size === 0) {
        this._removeNode(cur);
    }
};

AllOne.prototype.getMaxKey = function() {
    const node = this.tail.prev;
    if (node === this.head) return "";
    for (let k of node.keys) {
        return k;
    }
    return "";
};

AllOne.prototype.getMinKey = function() {
    const node = this.head.next;
    if (node === this.tail) return "";
    for (let k of node.keys) {
        return k;
    }
    return "";
};
```

## Typescript

```typescript
class Node {
    freq: number;
    prev: Node | null = null;
    next: Node | null = null;
    keys: Set<string>;

    constructor(freq: number) {
        this.freq = freq;
        this.keys = new Set();
    }
}

class AllOne {
    private head: Node;
    private tail: Node;
    private keyMap: Map<string, Node>;

    constructor() {
        this.head = new Node(0); // dummy head
        this.tail = new Node(0); // dummy tail
        this.head.next = this.tail;
        this.tail.prev = this.head;
        this.keyMap = new Map();
    }

    private addNodeAfter(node: Node, newNode: Node): void {
        newNode.prev = node;
        newNode.next = node.next;
        if (node.next) node.next.prev = newNode;
        node.next = newNode;
    }

    private removeNode(node: Node): void {
        if (node.prev) node.prev.next = node.next;
        if (node.next) node.next.prev = node.prev;
        node.prev = null;
        node.next = null;
    }

    inc(key: string): void {
        const existingNode = this.keyMap.get(key);
        if (!existingNode) {
            // need freq 1 node after head
            let first = this.head.next!;
            if (first === this.tail || first.freq !== 1) {
                const newNode = new Node(1);
                this.addNodeAfter(this.head, newNode);
                first = newNode;
            }
            first.keys.add(key);
            this.keyMap.set(key, first);
        } else {
            const cur = existingNode;
            let nxt = cur.next!;
            if (nxt === this.tail || nxt.freq !== cur.freq + 1) {
                const newNode = new Node(cur.freq + 1);
                this.addNodeAfter(cur, newNode);
                nxt = newNode;
            }
            nxt.keys.add(key);
            this.keyMap.set(key, nxt);
            cur.keys.delete(key);
            if (cur.keys.size === 0) {
                this.removeNode(cur);
            }
        }
    }

    dec(key: string): void {
        const cur = this.keyMap.get(key)!; // guaranteed to exist
        cur.keys.delete(key);
        if (cur.freq === 1) {
            this.keyMap.delete(key);
        } else {
            let prev = cur.prev!;
            if (prev === this.head || prev.freq !== cur.freq - 1) {
                const newNode = new Node(cur.freq - 1);
                this.addNodeAfter(prev, newNode);
                prev = newNode;
            }
            prev.keys.add(key);
            this.keyMap.set(key, prev);
        }
        if (cur.keys.size === 0) {
            this.removeNode(cur);
        }
    }

    getMaxKey(): string {
        if (this.tail.prev === this.head) return "";
        const keys = this.tail.prev!.keys;
        for (const k of keys) {
            return k;
        }
        return "";
    }

    getMinKey(): string {
        if (this.head.next === this.tail) return "";
        const keys = this.head.next!.keys;
        for (const k of keys) {
            return k;
        }
        return "";
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * var obj = new AllOne()
 * obj.inc(key)
 * obj.dec(key)
 * var param_3 = obj.getMaxKey()
 * var param_4 = obj.getMinKey()
 */
```

## Php

```php
class Node {
    public int $freq;
    public ?Node $prev = null;
    public ?Node $next = null;
    /** @var array<string,bool> */
    public array $keys;

    public function __construct(int $freq) {
        $this->freq = $freq;
        $this->keys = [];
    }
}

class AllOne {
    private Node $head;
    private Node $tail;
    /** @var array<string,Node> */
    private array $keyNodeMap = [];

    /**
     * Initialize your data structure here.
     */
    function __construct() {
        $this->head = new Node(0); // dummy head
        $this->tail = new Node(0); // dummy tail
        $this->head->next = $this->tail;
        $this->tail->prev = $this->head;
    }

    /**
     * @param String $key
     * @return NULL
     */
    function inc($key) {
        if (!isset($this->keyNodeMap[$key])) {
            // new key, frequency should be 1
            $first = $this->head->next;
            if ($first === $this->tail || $first->freq !== 1) {
                $newNode = new Node(1);
                $this->addNodeAfter($this->head, $newNode);
                $target = $newNode;
            } else {
                $target = $first;
            }
            $target->keys[$key] = true;
            $this->keyNodeMap[$key] = $target;
        } else {
            $cur = $this->keyNodeMap[$key];
            $next = $cur->next;
            $newFreq = $cur->freq + 1;
            if ($next === $this->tail || $next->freq !== $newFreq) {
                $newNode = new Node($newFreq);
                $this->addNodeAfter($cur, $newNode);
                $target = $newNode;
            } else {
                $target = $next;
            }
            $target->keys[$key] = true;
            $this->keyNodeMap[$key] = $target;

            unset($cur->keys[$key]);
            if (empty($cur->keys)) {
                $this->removeNode($cur);
            }
        }
    }

    /**
     * @param String $key
     * @return NULL
     */
    function dec($key) {
        if (!isset($this->keyNodeMap[$key])) {
            return;
        }
        $cur = $this->keyNodeMap[$key];
        $prev = $cur->prev;
        $newFreq = $cur->freq - 1;

        unset($cur->keys[$key]);

        if ($newFreq == 0) {
            // key should be removed completely
            unset($this->keyNodeMap[$key]);
        } else {
            if ($prev === $this->head || $prev->freq !== $newFreq) {
                $newNode = new Node($newFreq);
                $this->addNodeAfter($prev, $newNode);
                $target = $newNode;
            } else {
                $target = $prev;
            }
            $target->keys[$key] = true;
            $this->keyNodeMap[$key] = $target;
        }

        if (empty($cur->keys)) {
            $this->removeNode($cur);
        }
    }

    /**
     * @return String
     */
    function getMaxKey() {
        if ($this->tail->prev === $this->head) {
            return "";
        }
        foreach ($this->tail->prev->keys as $k => $_) {
            return $k;
        }
        return "";
    }

    /**
     * @return String
     */
    function getMinKey() {
        if ($this->head->next === $this->tail) {
            return "";
        }
        foreach ($this->head->next->keys as $k => $_) {
            return $k;
        }
        return "";
    }

    private function addNodeAfter(Node $node, Node $newNode): void {
        $newNode->prev = $node;
        $newNode->next = $node->next;
        $node->next->prev = $newNode;
        $node->next = $newNode;
    }

    private function removeNode(Node $node): void {
        $node->prev->next = $node->next;
        $node->next->prev = $node->prev;
        // help GC
        $node->prev = null;
        $node->next = null;
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * $obj = new AllOne();
 * $obj->inc($key);
 * $obj->dec($key);
 * $ret_3 = $obj->getMaxKey();
 * $ret_4 = $obj->getMinKey();
 */
```

## Swift

```swift
class AllOne {
    private class Node {
        var freq: Int
        var keys: Set<String>
        var prev: Node?
        var next: Node?
        init(freq: Int) {
            self.freq = freq
            self.keys = Set<String>()
        }
    }

    private let head: Node
    private let tail: Node
    private var keyMap: [String: Node]

    init() {
        head = Node(freq: 0)
        tail = Node(freq: 0)
        head.next = tail
        tail.prev = head
        keyMap = [:]
    }

    func inc(_ key: String) {
        if let curNode = keyMap[key] {
            // existing key, increase frequency
            let newFreq = curNode.freq + 1
            curNode.keys.remove(key)

            var nextNode = curNode.next!
            if nextNode === tail || nextNode.freq != newFreq {
                // create a new node for newFreq
                let newNode = Node(freq: newFreq)
                let afterNode = curNode.next!
                newNode.prev = curNode
                newNode.next = afterNode
                curNode.next = newNode
                afterNode.prev = newNode
                nextNode = newNode
            }
            nextNode.keys.insert(key)
            keyMap[key] = nextNode

            if curNode.keys.isEmpty {
                remove(node: curNode)
            }
        } else {
            // new key, frequency becomes 1
            var firstNode = head.next!
            if firstNode === tail || firstNode.freq != 1 {
                let newNode = Node(freq: 1)
                let afterNode = head.next!
                newNode.prev = head
                newNode.next = afterNode
                head.next = newNode
                afterNode.prev = newNode
                firstNode = newNode
            }
            firstNode.keys.insert(key)
            keyMap[key] = firstNode
        }
    }

    func dec(_ key: String) {
        guard let curNode = keyMap[key] else { return } // guaranteed to exist per problem statement

        let newFreq = curNode.freq - 1
        curNode.keys.remove(key)

        if newFreq == 0 {
            // remove key completely
            keyMap.removeValue(forKey: key)
        } else {
            var prevNode = curNode.prev!
            if prevNode === head || prevNode.freq != newFreq {
                // create a node for newFreq
                let newNode = Node(freq: newFreq)
                let beforeNode = curNode.prev!
                newNode.next = curNode
                newNode.prev = beforeNode
                beforeNode.next = newNode
                curNode.prev = newNode
                prevNode = newNode
            }
            prevNode.keys.insert(key)
            keyMap[key] = prevNode
        }

        if curNode.keys.isEmpty {
            remove(node: curNode)
        }
    }

    func getMaxKey() -> String {
        if tail.prev === head { return "" }
        return tail.prev!.keys.first!
    }

    func getMinKey() -> String {
        if head.next === tail { return "" }
        return head.next!.keys.first!
    }

    private func remove(node: Node) {
        let prevNode = node.prev!
        let nextNode = node.next!
        prevNode.next = nextNode
        nextNode.prev = prevNode
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * let obj = AllOne()
 * obj.inc(key)
 * obj.dec(key)
 * let ret_3: String = obj.getMaxKey()
 * let ret_4: String = obj.getMinKey()
 */
```

## Kotlin

```kotlin
import java.util.HashMap
import java.util.HashSet

class AllOne() {

    private class Node(val freq: Int) {
        var prev: Node? = null
        var next: Node? = null
        val keys: MutableSet<String> = HashSet()
    }

    private val head = Node(0)
    private val tail = Node(0)
    private val keyNodeMap = HashMap<String, Node>()

    init {
        head.next = tail
        tail.prev = head
    }

    fun inc(key: String) {
        val curNode = keyNodeMap[key]
        if (curNode == null) {
            var node = head.next
            if (node === tail || node!!.freq != 1) {
                val newNode = Node(1)
                insertAfter(head, newNode)
                node = newNode
            }
            node.keys.add(key)
            keyNodeMap[key] = node
        } else {
            var nextNode = curNode.next
            if (nextNode === tail || nextNode!!.freq != curNode.freq + 1) {
                val newNode = Node(curNode.freq + 1)
                insertAfter(curNode, newNode)
                newNode.keys.add(key)
                keyNodeMap[key] = newNode
            } else {
                nextNode.keys.add(key)
                keyNodeMap[key] = nextNode
            }
            curNode.keys.remove(key)
            if (curNode.keys.isEmpty()) {
                remove(curNode)
            }
        }
    }

    fun dec(key: String) {
        val curNode = keyNodeMap[key] ?: return
        if (curNode.freq == 1) {
            curNode.keys.remove(key)
            keyNodeMap.remove(key)
        } else {
            var prevNode = curNode.prev
            if (prevNode === head || prevNode!!.freq != curNode.freq - 1) {
                val newNode = Node(curNode.freq - 1)
                insertAfter(prevNode!!, newNode)
                newNode.keys.add(key)
                keyNodeMap[key] = newNode
            } else {
                prevNode.keys.add(key)
                keyNodeMap[key] = prevNode
            }
            curNode.keys.remove(key)
        }
        if (curNode.keys.isEmpty()) {
            remove(curNode)
        }
    }

    fun getMaxKey(): String {
        val node = tail.prev
        return if (node === head) "" else node!!.keys.iterator().next()
    }

    fun getMinKey(): String {
        val node = head.next
        return if (node === tail) "" else node!!.keys.iterator().next()
    }

    private fun insertAfter(prevNode: Node, newNode: Node) {
        newNode.prev = prevNode
        newNode.next = prevNode.next
        prevNode.next?.prev = newNode
        prevNode.next = newNode
    }

    private fun remove(node: Node) {
        node.prev?.next = node.next
        node.next?.prev = node.prev
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * var obj = AllOne()
 * obj.inc(key)
 * obj.dec(key)
 * var param_3 = obj.getMaxKey()
 * var param_4 = obj.getMinKey()
 */
```

## Dart

```dart
class AllOne {
  final Map<String, Node> _keyNode = {};
  final Node _head;
  final Node _tail;

  AllOne()
      : _head = Node(0),
        _tail = Node(0) {
    _head.next = _tail;
    _tail.prev = _head;
  }

  void inc(String key) {
    if (!_keyNode.containsKey(key)) {
      Node? first = _head.next;
      if (first == _tail || first!.freq != 1) {
        Node newNode = Node(1);
        _addNodeAfter(newNode, _head);
        first = newNode;
      }
      first!.keys.add(key);
      _keyNode[key] = first;
    } else {
      Node cur = _keyNode[key]!;
      int newFreq = cur.freq + 1;
      Node? nxt = cur.next;
      cur.keys.remove(key);
      if (nxt == _tail || nxt!.freq != newFreq) {
        Node newNode = Node(newFreq);
        _addNodeAfter(newNode, cur);
        nxt = newNode;
      }
      nxt!.keys.add(key);
      _keyNode[key] = nxt;
      if (cur.keys.isEmpty) {
        _removeNode(cur);
      }
    }
  }

  void dec(String key) {
    Node cur = _keyNode[key]!; // guaranteed to exist
    int newFreq = cur.freq - 1;
    cur.keys.remove(key);
    if (newFreq == 0) {
      _keyNode.remove(key);
    } else {
      Node? prev = cur.prev;
      if (prev == _head || prev!.freq != newFreq) {
        Node newNode = Node(newFreq);
        _addNodeAfter(newNode, cur.prev!);
        prev = newNode;
      }
      prev!.keys.add(key);
      _keyNode[key] = prev;
    }
    if (cur.keys.isEmpty) {
      _removeNode(cur);
    }
  }

  String getMaxKey() {
    if (_tail.prev == _head) return "";
    Node maxNode = _tail.prev!;
    return maxNode.keys.first;
  }

  String getMinKey() {
    if (_head.next == _tail) return "";
    Node minNode = _head.next!;
    return minNode.keys.first;
  }

  void _addNodeAfter(Node node, Node prev) {
    node.prev = prev;
    node.next = prev.next;
    prev.next!.prev = node;
    prev.next = node;
  }

  void _removeNode(Node node) {
    node.prev!.next = node.next;
    node.next!.prev = node.prev;
    node.prev = null;
    node.next = null;
  }
}

class Node {
  int freq;
  Set<String> keys = <String>{};
  Node? prev;
  Node? next;
  Node(this.freq);
}

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = AllOne();
 * obj.inc(key);
 * obj.dec(key);
 * String param3 = obj.getMaxKey();
 * String param4 = obj.getMinKey();
 */
```

## Golang

```go
type Node struct {
	freq int
	prev *Node
	next *Node
	keys map[string]struct{}
}

type AllOne struct {
	head  *Node
	tail  *Node
	nodes map[string]*Node // key -> node containing the key
}

/** Initialize your data structure here. */
func Constructor() AllOne {
	head := &Node{freq: 0, keys: make(map[string]struct{})}
	tail := &Node{freq: 0, keys: make(map[string]struct{})}
	head.next = tail
	tail.prev = head
	return AllOne{
		head:  head,
		tail:  tail,
		nodes: make(map[string]*Node),
	}
}

/** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
func (this *AllOne) Inc(key string) {
	if node, ok := this.nodes[key]; !ok {
		// New key, should be placed in freq=1 node
		first := this.head.next
		if first == this.tail || first.freq != 1 {
			newNode := &Node{freq: 1, keys: make(map[string]struct{})}
			this.addNodeAfter(newNode, this.head)
			first = newNode
		}
		first.keys[key] = struct{}{}
		this.nodes[key] = first
	} else {
		curFreq := node.freq
		nextNode := node.next

		delete(node.keys, key)

		if nextNode == this.tail || nextNode.freq != curFreq+1 {
			newNode := &Node{freq: curFreq + 1, keys: make(map[string]struct{})}
			this.addNodeAfter(newNode, node)
			nextNode = newNode
		}
		nextNode.keys[key] = struct{}{}
		this.nodes[key] = nextNode

		if len(node.keys) == 0 {
			this.removeNode(node)
		}
	}
}

/** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
func (this *AllOne) Dec(key string) {
	node := this.nodes[key]
	curFreq := node.freq

	delete(node.keys, key)

	if curFreq == 1 {
		delete(this.nodes, key)
	} else {
		prevNode := node.prev
		if prevNode == this.head || prevNode.freq != curFreq-1 {
			newNode := &Node{freq: curFreq - 1, keys: make(map[string]struct{})}
			this.addNodeAfter(newNode, node.prev)
			prevNode = newNode
		}
		prevNode.keys[key] = struct{}{}
		this.nodes[key] = prevNode
	}

	if len(node.keys) == 0 {
		this.removeNode(node)
	}
}

/** Returns one of the keys with maximal value. */
func (this *AllOne) GetMaxKey() string {
	if this.tail.prev == this.head {
		return ""
	}
	for k := range this.tail.prev.keys {
		return k
	}
	return ""
}

/** Returns one of the keys with Minimal value. */
func (this *AllOne) GetMinKey() string {
	if this.head.next == this.tail {
		return ""
	}
	for k := range this.head.next.keys {
		return k
	}
	return ""
}

// helper to insert newNode after prevNode
func (this *AllOne) addNodeAfter(newNode, prevNode *Node) {
	newNode.prev = prevNode
	newNode.next = prevNode.next
	prevNode.next.prev = newNode
	prevNode.next = newNode
}

// helper to remove a node from the list
func (this *AllOne) removeNode(node *Node) {
	node.prev.next = node.next
	node.next.prev = node.prev
}

/**
 * Your AllOne object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Inc(key);
 * obj.Dec(key);
 * param_3 := obj.GetMaxKey();
 * param_4 := obj.GetMinKey();
 */
```

## Ruby

```ruby
require 'set'

class Node
  attr_accessor :freq, :prev, :nxt, :keys

  def initialize(freq)
    @freq = freq
    @prev = nil
    @nxt = nil
    @keys = Set.new
  end
end

class AllOne
  def initialize()
    @head = Node.new(0)   # dummy head
    @tail = Node.new(0)   # dummy tail
    @head.nxt = @tail
    @tail.prev = @head
    @key_node = {}        # key => node
  end

=begin
    :type key: String
    :rtype: Void
=end
  def inc(key)
    if !@key_node.key?(key)
      first = @head.nxt
      if first == @tail || first.freq != 1
        node = Node.new(1)
        insert_after(@head, node)
      else
        node = first
      end
      node.keys.add(key)
      @key_node[key] = node
    else
      cur = @key_node[key]
      nxt = cur.nxt
      if nxt == @tail || nxt.freq != cur.freq + 1
        newnode = Node.new(cur.freq + 1)
        insert_after(cur, newnode)
        nxt = newnode
      end
      nxt.keys.add(key)
      @key_node[key] = nxt
      cur.keys.delete(key)
      remove_node(cur) if cur.keys.empty?
    end
  end

=begin
    :type key: String
    :rtype: Void
=end
  def dec(key)
    cur = @key_node[key]
    if cur.freq == 1
      cur.keys.delete(key)
      @key_node.delete(key)
    else
      prev = cur.prev
      if prev == @head || prev.freq != cur.freq - 1
        newnode = Node.new(cur.freq - 1)
        insert_before(cur, newnode)
        prev = newnode
      end
      prev.keys.add(key)
      @key_node[key] = prev
      cur.keys.delete(key)
    end
    remove_node(cur) if cur.keys.empty?
  end

=begin
    :rtype: String
=end
  def get_max_key()
    return "" if @head.nxt == @tail
    node = @tail.prev
    node.keys.each { |k| return k }
    ""
  end

=begin
    :rtype: String
=end
  def get_min_key()
    return "" if @head.nxt == @tail
    node = @head.nxt
    node.keys.each { |k| return k }
    ""
  end

  private

  def insert_after(node, new_node)
    new_node.prev = node
    new_node.nxt = node.nxt
    node.nxt.prev = new_node
    node.nxt = new_node
  end

  def insert_before(node, new_node)
    insert_after(node.prev, new_node)
  end

  def remove_node(node)
    node.prev.nxt = node.nxt
    node.nxt.prev = node.prev
  end
end
```

## Scala

```scala
import scala.collection.mutable

class AllOne() {

  private class Node(val freq: Int) {
    var prev: Node = _
    var next: Node = _
    val keys: mutable.HashSet[String] = mutable.HashSet.empty
  }

  private val head: Node = new Node(0)
  private val tail: Node = new Node(0)
  private val keyNode: mutable.HashMap[String, Node] = mutable.HashMap.empty

  // initialize dummy list
  head.next = tail
  tail.prev = head

  private def addNodeAfter(prevNode: Node, newNode: Node): Unit = {
    newNode.prev = prevNode
    newNode.next = prevNode.next
    prevNode.next.prev = newNode
    prevNode.next = newNode
  }

  private def removeNode(node: Node): Unit = {
    node.prev.next = node.next
    node.next.prev = node.prev
  }

  def inc(key: String): Unit = {
    if (!keyNode.contains(key)) {
      var node = head.next
      if (node == tail || node.freq != 1) {
        val newNode = new Node(1)
        addNodeAfter(head, newNode)
        node = newNode
      }
      node.keys.add(key)
      keyNode.put(key, node)
    } else {
      val cur = keyNode(key)
      var nextNode = cur.next
      if (nextNode == tail || nextNode.freq != cur.freq + 1) {
        val newNode = new Node(cur.freq + 1)
        addNodeAfter(cur, newNode)
        nextNode = newNode
      }
      nextNode.keys.add(key)
      keyNode.update(key, nextNode)

      cur.keys.remove(key)
      if (cur.keys.isEmpty) removeNode(cur)
    }
  }

  def dec(key: String): Unit = {
    val cur = keyNode(key)
    if (cur.freq == 1) {
      // remove completely
      keyNode -= key
    } else {
      var prevNode = cur.prev
      if (prevNode == head || prevNode.freq != cur.freq - 1) {
        val newNode = new Node(cur.freq - 1)
        addNodeAfter(cur.prev, newNode)
        prevNode = newNode
      }
      prevNode.keys.add(key)
      keyNode.update(key, prevNode)
    }

    cur.keys.remove(key)
    if (cur.keys.isEmpty) removeNode(cur)
  }

  def getMaxKey(): String = {
    if (tail.prev == head) ""
    else tail.prev.keys.head
  }

  def getMinKey(): String = {
    if (head.next == tail) ""
    else head.next.keys.head
  }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * val obj = new AllOne()
 * obj.inc(key)
 * obj.dec(key)
 * val param_3 = obj.getMaxKey()
 * val param_4 = obj.getMinKey()
 */
```

## Rust

```rust
use std::cell::RefCell;
use std::collections::{HashMap, HashSet};
use std::rc::Rc;

struct Node {
    freq: i32,
    keys: HashSet<String>,
    prev: Option<Rc<RefCell<Node>>>,
    next: Option<Rc<RefCell<Node>>>,
}

pub struct AllOne {
    head: Rc<RefCell<Node>>,
    tail: Rc<RefCell<Node>>,
    key_node: RefCell<HashMap<String, Rc<RefCell<Node>>>>,
}

impl AllOne {
    fn new() -> Self {
        let head = Rc::new(RefCell::new(Node {
            freq: i32::MIN,
            keys: HashSet::new(),
            prev: None,
            next: None,
        }));
        let tail = Rc::new(RefCell::new(Node {
            freq: i32::MAX,
            keys: HashSet::new(),
            prev: Some(head.clone()),
            next: None,
        }));
        head.borrow_mut().next = Some(tail.clone());
        AllOne {
            head,
            tail,
            key_node: RefCell::new(HashMap::new()),
        }
    }

    fn insert_node_after(&self, node: Rc<RefCell<Node>>, new_node: Rc<RefCell<Node>>) {
        let next_opt = node.borrow().next.clone();
        {
            let mut new_mut = new_node.borrow_mut();
            new_mut.prev = Some(node.clone());
            new_mut.next = next_opt.clone();
        }
        if let Some(next_rc) = &next_opt {
            next_rc.borrow_mut().prev = Some(new_node.clone());
        }
        node.borrow_mut().next = Some(new_node);
    }

    fn insert_node_before(&self, node: Rc<RefCell<Node>>, new_node: Rc<RefCell<Node>>) {
        if let Some(prev_rc) = node.borrow().prev.clone() {
            self.insert_node_after(prev_rc, new_node);
        }
    }

    fn remove_node(&self, node: Rc<RefCell<Node>>) {
        let prev_opt = node.borrow().prev.clone();
        let next_opt = node.borrow().next.clone();
        if let (Some(prev_rc), Some(next_rc)) = (prev_opt, next_opt) {
            prev_rc.borrow_mut().next = Some(next_rc.clone());
            next_rc.borrow_mut().prev = Some(prev_rc);
        }
    }

    fn inc(&self, key: String) {
        let mut map_ref = self.key_node.borrow_mut();
        if let Some(cur_node_rc) = map_ref.get(&key).cloned() {
            let cur_freq = cur_node_rc.borrow().freq;
            cur_node_rc.borrow_mut().keys.remove(&key);
            // determine target node
            let need_new = match cur_node_rc.borrow().next.clone() {
                Some(next_rc) => next_rc.borrow().freq != cur_freq + 1,
                None => true,
            };
            let target_node_rc = if need_new {
                let new_node = Rc::new(RefCell::new(Node {
                    freq: cur_freq + 1,
                    keys: HashSet::new(),
                    prev: None,
                    next: None,
                }));
                self.insert_node_after(cur_node_rc.clone(), new_node.clone());
                new_node
            } else {
                cur_node_rc.borrow().next.clone().unwrap()
            };
            target_node_rc.borrow_mut().keys.insert(key.clone());
            map_ref.insert(key, target_node_rc);
            if cur_node_rc.borrow().keys.is_empty() {
                self.remove_node(cur_node_rc);
            }
        } else {
            // new key with freq 1
            let need_new = match self.head.borrow().next.clone() {
                Some(next_rc) => next_rc.borrow().freq != 1,
                None => true,
            };
            let target_node_rc = if need_new {
                let new_node = Rc::new(RefCell::new(Node {
                    freq: 1,
                    keys: HashSet::new(),
                    prev: None,
                    next: None,
                }));
                self.insert_node_after(self.head.clone(), new_node.clone());
                new_node
            } else {
                self.head.borrow().next.clone().unwrap()
            };
            target_node_rc.borrow_mut().keys.insert(key.clone());
            map_ref.insert(key, target_node_rc);
        }
    }

    fn dec(&self, key: String) {
        let mut map_ref = self.key_node.borrow_mut();
        if let Some(cur_node_rc) = map_ref.get(&key).cloned() {
            let cur_freq = cur_node_rc.borrow().freq;
            cur_node_rc.borrow_mut().keys.remove(&key);
            if cur_freq == 1 {
                map_ref.remove(&key);
            } else {
                // move to freq-1 node
                let need_new = match cur_node_rc.borrow().prev.clone() {
                    Some(prev_rc) => prev_rc.borrow().freq != cur_freq - 1,
                    None => true,
                };
                let target_node_rc = if need_new {
                    let new_node = Rc::new(RefCell::new(Node {
                        freq: cur_freq - 1,
                        keys: HashSet::new(),
                        prev: None,
                        next: None,
                    }));
                    self.insert_node_before(cur_node_rc.clone(), new_node.clone());
                    new_node
                } else {
                    cur_node_rc.borrow().prev.clone().unwrap()
                };
                target_node_rc.borrow_mut().keys.insert(key.clone());
                map_ref.insert(key, target_node_rc);
            }
            if cur_node_rc.borrow().keys.is_empty() {
                self.remove_node(cur_node_rc);
            }
        }
    }

    fn get_max_key(&self) -> String {
        let tail_prev_opt = self.tail.borrow().prev.clone();
        if let Some(node_rc) = tail_prev_opt {
            if Rc::ptr_eq(&node_rc, &self.head) {
                return "".to_string();
            }
            if let Some(k) = node_rc.borrow().keys.iter().next() {
                return k.clone();
            }
        }
        "".to_string()
    }

    fn get_min_key(&self) -> String {
        let head_next_opt = self.head.borrow().next.clone();
        if let Some(node_rc) = head_next_opt {
            if Rc::ptr_eq(&node_rc, &self.tail) {
                return "".to_string();
            }
            if let Some(k) = node_rc.borrow().keys.iter().next() {
                return k.clone();
            }
        }
        "".to_string()
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * let obj = AllOne::new();
 * obj.inc(key);
 * obj.dec(key);
 * let ret_3: String = obj.get_max_key();
 * let ret_4: String = obj.get_min_key();
 */
```

## Racket

```racket
#lang racket

(struct node ([freq #:mutable] [prev #:mutable] [next #:mutable] [keys #:mutable]))

(define all-one%
  (class object%
    (super-new)

    ;; sentinel head and tail nodes
    (field [head (let ([h (node 0 #f #f (make-hash))]) h)])
    (field [tail (let ([t (node 0 #f #f (make-hash))]) t)])

    (begin
      (set-node-next! head tail)
      (set-node-prev! tail head))

    ;; map from key string to its current node
    (field [key->node (make-hash)])

    ;; helpers ----------------------------------------------------
    (define (add-key-to-node n k)
      (hash-set! (node-keys n) k #t))

    (define (remove-key-from-node n k)
      (hash-remove! (node-keys n) k))

    (define (node-empty? n)
      (= (hash-count (node-keys n)) 0))

    (define (insert-node-after prev new)
      (let ([next (node-next prev)])
        (set-node-prev! new prev)
        (set-node-next! new next)
        (set-node-next! prev new)
        (when next
          (set-node-prev! next new))))

    (define (remove-node n)
      (let ([prev (node-prev n)]
            [next (node-next n)])
        (when prev (set-node-next! prev next))
        (when next (set-node-prev! next prev))))
    ;; -----------------------------------------------------------

    ;; inc : string? -> void?
    (define/public (inc key)
      (cond
        [(hash-has-key? key->node key)
         (let* ([cur   (hash-ref key->node key)]
                [freq  (node-freq cur)]
                [next  (node-next cur)])
           (remove-key-from-node cur key)
           (define target
             (if (and next (not (eq? next tail)) (= (node-freq next) (+ freq 1)))
                 next
                 (let ([new (node (+ freq 1) #f #f (make-hash))])
                   (insert-node-after cur new)
                   new)))
           (add-key-to-node target key)
           (hash-set! key->node key target)
           (when (node-empty? cur) (remove-node cur)))]
        [else
         (let* ([first (node-next head)])
           (define target
             (if (and first (not (eq? first tail)) (= (node-freq first) 1))
                 first
                 (let ([new (node 1 #f #f (make-hash))])
                   (insert-node-after head new)
                   new)))
           (add-key-to-node target key)
           (hash-set! key->node key target))]))

    ;; dec : string? -> void?
    (define/public (dec key)
      (when (hash-has-key? key->node key)
        (let* ([cur   (hash-ref key->node key)]
               [freq  (node-freq cur)])
          (remove-key-from-node cur key)
          (if (= freq 1)
              (hash-remove! key->node key)
              (let* ([prev   (node-prev cur)]
                     [target (if (and prev (not (eq? prev head)) (= (node-freq prev) (- freq 1)))
                                 prev
                                 (let ([new (node (- freq 1) #f #f (make-hash))])
                                   (insert-node-after (node-prev cur) new)
                                   new))])
                (add-key-to-node target key)
                (hash-set! key->node key target)))
          (when (node-empty? cur) (remove-node cur)))))

    ;; get-max-key : -> string?
    (define/public (get-max-key)
      (let ([last (node-prev tail)])
        (if (or (eq? last head) (= (hash-count (node-keys last)) 0))
            ""
            (car (hash-keys (node-keys last))))))

    ;; get-min-key : -> string?
    (define/public (get-min-key)
      (let ([first (node-next head)])
        (if (or (eq? first tail) (= (hash-count (node-keys first)) 0))
            ""
            (car (hash-keys (node-keys first))))))

    ))
```

## Erlang

```erlang
-spec all_one_init_() -> any().
all_one_init_() ->
    HeadId = 0,
    TailId = 1,
    Nodes = #{
        HeadId => #{freq => 0, prev => undefined, next => TailId, keys => #{}},
        TailId => #{freq => 0, prev => HeadId, next => undefined, keys => #{}}
    },
    State = #{
        key_node => #{},
        nodes => Nodes,
        head => HeadId,
        tail => TailId,
        nid => 2
    },
    erlang:put(state, State).

-spec all_one_inc(Key :: unicode:unicode_binary()) -> any().
all_one_inc(Key) ->
    State0 = erlang:get(state),
    KeyNodeMap = maps:get(key_node, State0),
    case maps:find(Key, KeyNodeMap) of
        error ->
            %% new key, target freq = 1 after head
            HeadId = maps:get(head, State0),
            FirstId = (maps:get(HeadId, State0#nodes)).next,
            {TargetId, State1} =
                case FirstId of
                    undefined ->
                        add_node(1, HeadId, State0);
                    _ ->
                        FirstNode = node(FirstId, State0),
                        if FirstNode.freq == 1 ->
                                {FirstId, State0};
                           true ->
                                add_node(1, HeadId, State0)
                        end
                end,
            TargetNode = node(TargetId, State1),
            NewKeys = maps:put(Key, true, TargetNode.keys),
            UpdatedTarget = TargetNode#{keys => NewKeys},
            State2 = update_node(TargetId, UpdatedTarget, State1),
            NewKeyMap = maps:put(Key, TargetId, State2.key_node),
            erlang:put(state, State2#{key_node => NewKeyMap});
        {ok, NodeId} ->
            CurNode = node(NodeId, State0),
            CurFreq = CurNode.freq,
            NextId = CurNode.next,
            {TargetId, State1} =
                case NextId of
                    undefined ->
                        add_node(CurFreq + 1, NodeId, State0);
                    _ ->
                        NextNode = node(NextId, State0),
                        if NextNode.freq == CurFreq + 1 ->
                                {NextId, State0};
                           true ->
                                add_node(CurFreq + 1, NodeId, State0)
                        end
                end,
            %% move key from cur to target
            CurKeys2 = maps:remove(Key, CurNode.keys),
            UpdatedCur = CurNode#{keys => CurKeys2},
            State2 = update_node(NodeId, UpdatedCur, State1),

            TargetNode = node(TargetId, State2),
            TKeys2 = maps:put(Key, true, TargetNode.keys),
            UpdatedTarget = TargetNode#{keys => TKeys2},
            State3 = update_node(TargetId, UpdatedTarget, State2),

            NewKeyMap = maps:put(Key, TargetId, State3.key_node),

            %% remove cur node if empty
            FinalState =
                case CurKeys2 of
                    #{} -> remove_node(NodeId, State3);
                    _   -> State3
                end,
            erlang:put(state, FinalState#{key_node => NewKeyMap})
    end.

-spec all_one_dec(Key :: unicode:unicode_binary()) -> any().
all_one_dec(Key) ->
    State0 = erlang:get(state),
    KeyNodeMap = maps:get(key_node, State0),
    {ok, NodeId} = maps:find(Key, KeyNodeMap),
    CurNode = node(NodeId, State0),
    CurFreq = CurNode.freq,
    %% remove key from current node
    CurKeys2 = maps:remove(Key, CurNode.keys),
    UpdatedCur = CurNode#{keys => CurKeys2},
    State1 = update_node(NodeId, UpdatedCur, State0),

    if CurFreq == 1 ->
            NewKeyMap = maps:remove(Key, State1.key_node),
            TempState = State1;
       true ->
            PrevId = CurNode.prev,
            HeadId = maps:get(head, State0),
            {TargetId, StateTmp} =
                case PrevId of
                    undefined -> add_node(CurFreq - 1, HeadId, State1);
                    _ ->
                        PrevNode = node(PrevId, State1),
                        if PrevNode.freq == CurFreq - 1 ->
                                {PrevId, State1};
                           true ->
                                add_node(CurFreq - 1, PrevId, State1)
                        end
                end,
            TargetNode = node(TargetId, StateTmp),
            TKeys2 = maps:put(Key, true, TargetNode.keys),
            UpdatedTarget = TargetNode#{keys => TKeys2},
            State2 = update_node(TargetId, UpdatedTarget, StateTmp),
            NewKeyMap = maps:put(Key, TargetId, State2.key_node),
            TempState = State2
    end,

    FinalState =
        case CurKeys2 of
            #{} -> remove_node(NodeId, TempState);
            _   -> TempState
        end,
    erlang:put(state, FinalState#{key_node => NewKeyMap}).

-spec all_one_get_max_key() -> unicode:unicode_binary().
all_one_get_max_key() ->
    State = erlang:get(state),
    TailId = maps:get(tail, State),
    PrevId = (maps:get(TailId, State#nodes)).prev,
    case PrevId of
        undefined -> <<>>;
        _ when PrevId == maps:get(head, State) -> <<>>;
        _ ->
            Node = node(PrevId, State),
            case maps:keys(Node.keys) of
                [] -> <<>>;
                [K | _] -> K
            end
    end.

-spec all_one_get_min_key() -> unicode:unicode_binary().
all_one_get_min_key() ->
    State = erlang:get(state),
    HeadId = maps:get(head, State),
    NextId = (maps:get(HeadId, State#nodes)).next,
    case NextId of
        undefined -> <<>>;
        _ when NextId == maps:get(tail, State) -> <<>>;
        _ ->
            Node = node(NextId, State),
            case maps:keys(Node.keys) of
                [] -> <<>>;
                [K | _] -> K
            end
    end.

%% Helper functions

node(Id, State) ->
    maps:get(Id, State#nodes).

update_node(Id, NodeMap, State) ->
    Nodes = State#nodes,
    NewNodes = maps:put(Id, NodeMap, Nodes),
    State#{nodes => NewNodes}.

add_node(Freq, PrevId, State) ->
    PrevNode = node(PrevId, State),
    NextId = PrevNode.next,
    NewId = State.nid,
    NewNode = #{freq => Freq, prev => PrevId, next => NextId, keys => #{}},
    Nodes1 = maps:put(NewId, NewNode, State#nodes),
    State1 = State#{nodes => Nodes1, nid => NewId + 1},
    %% link Prev
    UpdatedPrev = PrevNode#{next => NewId},
    State2 = update_node(PrevId, UpdatedPrev, State1),
    %% link Next if exists
    State3 =
        case NextId of
            undefined -> State2;
            _ ->
                NextNode = node(NextId, State2),
                UpdatedNext = NextNode#{prev => NewId},
                update_node(NextId, UpdatedNext, State2)
        end,
    {NewId, State3}.

remove_node(Id, State) ->
    Node = node(Id, State),
    PrevId = Node.prev,
    NextId = Node.next,
    %% link prev and next
    State1 =
        case PrevId of
            undefined -> State;
            _ ->
                PrevNode = node(PrevId, State),
                UpdatedPrev = PrevNode#{next => NextId},
                update_node(PrevId, UpdatedPrev, State)
        end,
    State2 =
        case NextId of
            undefined -> State1;
            _ ->
                NextNode = node(NextId, State1),
                UpdatedNext = NextNode#{prev => PrevId},
                update_node(NextId, UpdatedNext, State1)
        end,
    Nodes2 = maps:remove(Id, State2#nodes),
    State2#{nodes => Nodes2}.
```

## Elixir

```elixir
defmodule AllOne do
  @moduledoc false

  defstruct key_to_freq: %{}, freq_nodes: %{}, head: nil, tail: nil

  # Public API --------------------------------------------------------------

  @spec init_() :: any
  def init_() do
    Process.put(:all_one_state, %AllOne{})
    :ok
  end

  @spec inc(key :: String.t()) :: any
  def inc(key) do
    state = get_state()
    if Map.has_key?(state.key_to_freq, key) do
      cur = state.key_to_freq[key]
      {state, cur_exists} = remove_key_from_node(state, cur, key)

      new_freq = cur + 1

      state =
        if Map.has_key?(state.freq_nodes, new_freq) do
          add_key_to_node(state, new_freq, key)
        else
          prev_freq = if cur_exists, do: cur, else: (state.freq_nodes[cur] && state.freq_nodes[cur].prev)
          next_freq =
            case prev_freq do
              nil -> state.head
              _ -> (Map.get(state.freq_nodes, prev_freq) || %{})[:next]
            end

          state = insert_node(state, new_freq, prev_freq, next_freq)
          add_key_to_node(state, new_freq, key)
        end

      state = %{state | key_to_freq: Map.put(state.key_to_freq, key, new_freq)}
      put_state(state)
    else
      # new key with freq 1
      state =
        if Map.has_key?(state.freq_nodes, 1) do
          add_key_to_node(state, 1, key)
        else
          state = insert_node(state, 1, nil, state.head)
          add_key_to_node(state, 1, key)
        end

      state = %{state | key_to_freq: Map.put(state.key_to_freq, key, 1)}
      put_state(state)
    end
  end

  @spec dec(key :: String.t()) :: any
  def dec(key) do
    state = get_state()
    cur = state.key_to_freq[key]
    {state, cur_exists} = remove_key_from_node(state, cur, key)

    if cur == 1 do
      # key removed completely
      state = %{state | key_to_freq: Map.delete(state.key_to_freq, key)}
      put_state(state)
    else
      new_freq = cur - 1

      state =
        if Map.has_key?(state.freq_nodes, new_freq) do
          add_key_to_node(state, new_freq, key)
        else
          next_freq = if cur_exists, do: cur, else: (state.freq_nodes[cur] && state.freq_nodes[cur].next)
          prev_freq =
            case next_freq do
              nil -> state.tail
              _ -> (Map.get(state.freq_nodes, next_freq) || %{})[:prev]
            end

          state = insert_node(state, new_freq, prev_freq, next_freq)
          add_key_to_node(state, new_freq, key)
        end

      state = %{state | key_to_freq: Map.put(state.key_to_freq, key, new_freq)}
      put_state(state)
    end
  end

  @spec get_max_key() :: String.t()
  def get_max_key() do
    state = get_state()
    case state.tail do
      nil -> ""
      freq ->
        node = state.freq_nodes[freq]
        node.keys |> Enum.take(1) |> List.first() || ""
    end
  end

  @spec get_min_key() :: String.t()
  def get_min_key() do
    state = get_state()
    case state.head do
      nil -> ""
      freq ->
        node = state.freq_nodes[freq]
        node.keys |> Enum.take(1) |> List.first() || ""
    end
  end

  # Private helpers ---------------------------------------------------------

  defp get_state do
    Process.get(:all_one_state, %AllOne{})
  end

  defp put_state(state), do: Process.put(:all_one_state, state)

  defp add_key_to_node(state, freq, key) do
    node = state.freq_nodes[freq]
    updated = %{node | keys: MapSet.put(node.keys, key)}
    %{state | freq_nodes: Map.put(state.freq_nodes, freq, updated)}
  end

  defp remove_key_from_node(state, freq, key) do
    node = state.freq_nodes[freq]
    new_keys = MapSet.delete(node.keys, key)
    freq_nodes = Map.put(state.freq_nodes, freq, %{node | keys: new_keys})
    state = %{state | freq_nodes: freq_nodes}

    if MapSet.size(new_keys) == 0 do
      prev = node.prev
      nxt = node.next
      freq_nodes2 = Map.delete(state.freq_nodes, freq)

      freq_nodes2 =
        if prev != nil do
          pnode = freq_nodes2[prev]
          Map.put(freq_nodes2, prev, %{pnode | next: nxt})
        else
          freq_nodes2
        end

      freq_nodes2 =
        if nxt != nil do
          nnode = freq_nodes2[nxt]
          Map.put(freq_nodes2, nxt, %{nnode | prev: prev})
        else
          freq_nodes2
        end

      head = if state.head == freq, do: nxt, else: state.head
      tail = if state.tail == freq, do: prev, else: state.tail

      {%{state | freq_nodes: freq_nodes2, head: head, tail: tail}, false}
    else
      {state, true}
    end
  end

  defp insert_node(state, freq, prev_freq, next_freq) do
    node = %{freq: freq, keys: MapSet.new(), prev: prev_freq, next: next_freq}
    freq_nodes = Map.put(state.freq_nodes, freq, node)

    freq_nodes =
      if prev_freq != nil do
        pnode = freq_nodes[prev_freq]
        Map.put(freq_nodes, prev_freq, %{pnode | next: freq})
      else
        freq_nodes
      end

    freq_nodes =
      if next_freq != nil do
        nnode = freq_nodes[next_freq]
        Map.put(freq_nodes, next_freq, %{nnode | prev: freq})
      else
        freq_nodes
      end

    head = if prev_freq == nil, do: freq, else: state.head
    tail = if next_freq == nil, do: freq, else: state.tail

    %{state | freq_nodes: freq_nodes, head: head, tail: tail}
  end
end
```
