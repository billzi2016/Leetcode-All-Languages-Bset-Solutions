# 1206. Design Skiplist

## Cpp

```cpp
class Skiplist {
    struct Node {
        int val;
        std::vector<Node*> next;
        Node(int v, int level) : val(v), next(level, nullptr) {}
    };
    
    static const int MAX_LEVEL = 32;
    Node* head;
    int curLevel;
    std::mt19937 rng;
    std::uniform_int_distribution<int> dist;
    
    int randomLevel() {
        int lvl = 1;
        while (dist(rng) && lvl < MAX_LEVEL) ++lvl;
        return lvl;
    }
public:
    Skiplist() : head(new Node(-1, MAX_LEVEL)), curLevel(1), rng(std::random_device{}()), dist(0, 1) {}
    
    bool search(int target) {
        Node* cur = head;
        for (int i = curLevel - 1; i >= 0; --i) {
            while (cur->next[i] && cur->next[i]->val < target)
                cur = cur->next[i];
        }
        cur = cur->next[0];
        return cur && cur->val == target;
    }
    
    void add(int num) {
        std::vector<Node*> update(MAX_LEVEL, nullptr);
        Node* cur = head;
        for (int i = curLevel - 1; i >= 0; --i) {
            while (cur->next[i] && cur->next[i]->val < num)
                cur = cur->next[i];
            update[i] = cur;
        }
        int lvl = randomLevel();
        if (lvl > curLevel) {
            for (int i = curLevel; i < lvl; ++i)
                update[i] = head;
            curLevel = lvl;
        }
        Node* node = new Node(num, lvl);
        for (int i = 0; i < lvl; ++i) {
            node->next[i] = update[i]->next[i];
            update[i]->next[i] = node;
        }
    }
    
    bool erase(int num) {
        std::vector<Node*> update(MAX_LEVEL, nullptr);
        Node* cur = head;
        for (int i = curLevel - 1; i >= 0; --i) {
            while (cur->next[i] && cur->next[i]->val < num)
                cur = cur->next[i];
            update[i] = cur;
        }
        Node* target = cur->next[0];
        if (!target || target->val != num) return false;
        for (int i = 0; i < curLevel; ++i) {
            if (update[i]->next[i] == target)
                update[i]->next[i] = target->next[i];
        }
        delete target;
        while (curLevel > 1 && !head->next[curLevel - 1])
            --curLevel;
        return true;
    }
};

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist* obj = new Skiplist();
 * bool param_1 = obj->search(target);
 * obj->add(num);
 * bool param_3 = obj->erase(num);
 */
```

## Java

```java
class Skiplist {
    private static class Node {
        int val;
        Node[] forward;
        Node(int val, int level) {
            this.val = val;
            this.forward = new Node[level];
        }
    }

    private static final double P = 0.5;
    private static final int MAX_LEVEL = 32;

    private final Node head;
    private int level;
    private final java.util.Random rand;

    public Skiplist() {
        head = new Node(-1, MAX_LEVEL);
        level = 1;
        rand = new java.util.Random();
    }

    public boolean search(int target) {
        Node cur = head;
        for (int i = level - 1; i >= 0; --i) {
            while (cur.forward[i] != null && cur.forward[i].val < target) {
                cur = cur.forward[i];
            }
        }
        cur = cur.forward[0];
        return cur != null && cur.val == target;
    }

    public void add(int num) {
        Node[] update = new Node[MAX_LEVEL];
        Node cur = head;
        for (int i = level - 1; i >= 0; --i) {
            while (cur.forward[i] != null && cur.forward[i].val < num) {
                cur = cur.forward[i];
            }
            update[i] = cur;
        }

        int nodeLevel = randomLevel();
        if (nodeLevel > level) {
            for (int i = level; i < nodeLevel; ++i) {
                update[i] = head;
            }
            level = nodeLevel;
        }

        Node newNode = new Node(num, nodeLevel);
        for (int i = 0; i < nodeLevel; ++i) {
            newNode.forward[i] = update[i].forward[i];
            update[i].forward[i] = newNode;
        }
    }

    public boolean erase(int num) {
        Node[] update = new Node[MAX_LEVEL];
        Node cur = head;
        for (int i = level - 1; i >= 0; --i) {
            while (cur.forward[i] != null && cur.forward[i].val < num) {
                cur = cur.forward[i];
            }
            update[i] = cur;
        }

        cur = cur.forward[0];
        if (cur == null || cur.val != num) {
            return false;
        }

        for (int i = 0; i < level; ++i) {
            if (update[i].forward[i] != cur) break;
            update[i].forward[i] = cur.forward[i];
        }

        while (level > 1 && head.forward[level - 1] == null) {
            level--;
        }
        return true;
    }

    private int randomLevel() {
        int lvl = 1;
        while (rand.nextDouble() < P && lvl < MAX_LEVEL) {
            lvl++;
        }
        return lvl;
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist obj = new Skiplist();
 * boolean param_1 = obj.search(target);
 * obj.add(num);
 * boolean param_3 = obj.erase(num);
 */
```

## Python

```python
import random

class Node:
    __slots__ = ('val', 'forward')
    def __init__(self, val, level):
        self.val = val
        self.forward = [None] * (level + 1)

class Skiplist(object):
    MAX_LEVEL = 16
    P_FACTOR = 0.5

    def __init__(self):
        self.head = Node(-float('inf'), self.MAX_LEVEL)
        self.level = 0

    def _random_level(self):
        lvl = 0
        while random.random() < self.P_FACTOR and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def search(self, target):
        """
        :type target: int
        :rtype: bool
        """
        cur = self.head
        for i in range(self.level, -1, -1):
            while cur.forward[i] and cur.forward[i].val < target:
                cur = cur.forward[i]
        cur = cur.forward[0]
        return cur is not None and cur.val == target

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        update = [None] * (self.MAX_LEVEL + 1)
        cur = self.head
        for i in range(self.level, -1, -1):
            while cur.forward[i] and cur.forward[i].val < num:
                cur = cur.forward[i]
            update[i] = cur

        lvl = self._random_level()
        if lvl > self.level:
            for i in range(self.level + 1, lvl + 1):
                update[i] = self.head
            self.level = lvl

        new_node = Node(num, lvl)
        for i in range(lvl + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        update = [None] * (self.MAX_LEVEL + 1)
        cur = self.head
        for i in range(self.level, -1, -1):
            while cur.forward[i] and cur.forward[i].val < num:
                cur = cur.forward[i]
            update[i] = cur

        target = cur.forward[0]
        if not target or target.val != num:
            return False

        for i in range(self.level + 1):
            if update[i].forward[i] == target:
                update[i].forward[i] = target.forward[i]

        while self.level > 0 and self.head.forward[self.level] is None:
            self.level -= 1
        return True
```

## Python3

```python
import random

class Node:
    __slots__ = ('val', 'forward')
    def __init__(self, val: int, level: int):
        self.val = val
        self.forward = [None] * level

class Skiplist:
    MAX_LEVEL = 16
    P = 0.5

    def __init__(self):
        self.head = Node(-1, self.MAX_LEVEL)
        self.level = 1

    def random_level(self) -> int:
        lvl = 1
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        node = self.head
        for i in range(self.level - 1, -1, -1):
            while node.forward[i] and node.forward[i].val < target:
                node = node.forward[i]
        node = node.forward[0]
        return node is not None and node.val == target

    def add(self, num: int) -> None:
        update = [None] * self.MAX_LEVEL
        node = self.head
        for i in range(self.level - 1, -1, -1):
            while node.forward[i] and node.forward[i].val < num:
                node = node.forward[i]
            update[i] = node
        lvl = self.random_level()
        if lvl > self.level:
            for i in range(self.level, lvl):
                update[i] = self.head
            self.level = lvl
        new_node = Node(num, lvl)
        for i in range(lvl):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * self.MAX_LEVEL
        node = self.head
        for i in range(self.level - 1, -1, -1):
            while node.forward[i] and node.forward[i].val < num:
                node = node.forward[i]
            update[i] = node
        target = node.forward[0]
        if not target or target.val != num:
            return False
        for i in range(self.level):
            if update[i].forward[i] != target:
                continue
            update[i].forward[i] = target.forward[i]
        while self.level > 1 and self.head.forward[self.level - 1] is None:
            self.level -= 1
        return True
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define MAX_LEVEL 32

typedef struct Node {
    int val;
    struct Node *forward[MAX_LEVEL];
} Node;

typedef struct {
    int level;
    Node *header;
} Skiplist;

/* Generate a random level for node */
static int randomLevel() {
    int lvl = 1;
    while ((rand() & 1) && lvl < MAX_LEVEL)
        ++lvl;
    return lvl;
}

/* Create a new node with given value and level */
static Node *createNode(int val, int level) {
    Node *node = (Node *)malloc(sizeof(Node));
    node->val = val;
    for (int i = 0; i < level; ++i)
        node->forward[i] = NULL;
    return node;
}

Skiplist* skiplistCreate() {
    srand((unsigned)time(NULL));
    Skiplist *obj = (Skiplist *)malloc(sizeof(Skiplist));
    obj->level = 1;
    obj->header = createNode(-1, MAX_LEVEL);
    for (int i = 0; i < MAX_LEVEL; ++i)
        obj->header->forward[i] = NULL;
    return obj;
}

bool skiplistSearch(Skiplist* obj, int target) {
    Node *cur = obj->header;
    for (int i = obj->level - 1; i >= 0; --i) {
        while (cur->forward[i] && cur->forward[i]->val < target)
            cur = cur->forward[i];
    }
    cur = cur->forward[0];
    return cur != NULL && cur->val == target;
}

void skiplistAdd(Skiplist* obj, int num) {
    Node *update[MAX_LEVEL];
    Node *cur = obj->header;
    for (int i = obj->level - 1; i >= 0; --i) {
        while (cur->forward[i] && cur->forward[i]->val < num)
            cur = cur->forward[i];
        update[i] = cur;
    }
    int lvl = randomLevel();
    if (lvl > obj->level) {
        for (int i = obj->level; i < lvl; ++i)
            update[i] = obj->header;
        obj->level = lvl;
    }
    Node *newNode = createNode(num, lvl);
    for (int i = 0; i < lvl; ++i) {
        newNode->forward[i] = update[i]->forward[i];
        update[i]->forward[i] = newNode;
    }
}

bool skiplistErase(Skiplist* obj, int num) {
    Node *update[MAX_LEVEL];
    Node *cur = obj->header;
    for (int i = obj->level - 1; i >= 0; --i) {
        while (cur->forward[i] && cur->forward[i]->val < num)
            cur = cur->forward[i];
        update[i] = cur;
    }
    Node *target = cur->forward[0];
    if (!target || target->val != num)
        return false;
    for (int i = 0; i < obj->level; ++i) {
        if (update[i]->forward[i] == target)
            update[i]->forward[i] = target->forward[i];
    }
    free(target);
    while (obj->level > 1 && obj->header->forward[obj->level - 1] == NULL)
        --obj->level;
    return true;
}

void skiplistFree(Skiplist* obj) {
    Node *cur = obj->header->forward[0];
    while (cur) {
        Node *next = cur->forward[0];
        free(cur);
        cur = next;
    }
    free(obj->header);
    free(obj);
}

/**
 * Your Skiplist struct will be instantiated and called as such:
 * Skiplist* obj = skiplistCreate();
 * bool param_1 = skiplistSearch(obj, target);
 * 
 * skiplistAdd(obj, num);
 * 
 * bool param_3 = skiplistErase(obj, num);
 * 
 * skiplistFree(obj);
 */
```

## Csharp

```csharp
using System;

public class Skiplist {
    private const int MAX_LEVEL = 32;
    private readonly Node head;
    private int level;
    private readonly Random rand;

    private class Node {
        public int val;
        public Node[] next;
        public Node(int v, int lvl) {
            val = v;
            next = new Node[lvl];
        }
    }

    public Skiplist() {
        head = new Node(-1, MAX_LEVEL);
        level = 1;
        rand = new Random();
    }

    private int RandomLevel() {
        int lvl = 1;
        while (lvl < MAX_LEVEL && rand.Next(2) == 0) {
            lvl++;
        }
        return lvl;
    }

    public bool Search(int target) {
        Node cur = head;
        for (int i = level - 1; i >= 0; i--) {
            while (cur.next[i] != null && cur.next[i].val < target) {
                cur = cur.next[i];
            }
        }
        cur = cur.next[0];
        return cur != null && cur.val == target;
    }

    public void Add(int num) {
        Node[] update = new Node[MAX_LEVEL];
        Node cur = head;
        for (int i = level - 1; i >= 0; i--) {
            while (cur.next[i] != null && cur.next[i].val < num) {
                cur = cur.next[i];
            }
            update[i] = cur;
        }

        int lvl = RandomLevel();
        if (lvl > level) {
            for (int i = level; i < lvl; i++) {
                update[i] = head;
            }
            level = lvl;
        }

        Node newNode = new Node(num, lvl);
        for (int i = 0; i < lvl; i++) {
            newNode.next[i] = update[i].next[i];
            update[i].next[i] = newNode;
        }
    }

    public bool Erase(int num) {
        Node[] update = new Node[MAX_LEVEL];
        Node cur = head;
        for (int i = level - 1; i >= 0; i--) {
            while (cur.next[i] != null && cur.next[i].val < num) {
                cur = cur.next[i];
            }
            update[i] = cur;
        }

        Node target = cur.next[0];
        if (target == null || target.val != num) {
            return false;
        }

        for (int i = 0; i < level; i++) {
            if (update[i].next[i] == target) {
                update[i].next[i] = target.next[i];
            }
        }

        while (level > 1 && head.next[level - 1] == null) {
            level--;
        }
        return true;
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist obj = new Skiplist();
 * bool param_1 = obj.Search(target);
 * obj.Add(num);
 * bool param_3 = obj.Erase(num);
 */
```

## Javascript

```javascript
var Skiplist = function() {
    this.MAX_LEVEL = 32;
    this.P = 0.5;
    this.level = 1; // current max level of skiplist
    this.head = new Node(-Infinity, this.MAX_LEVEL);
};

function Node(val, level) {
    this.val = val;
    this.forwards = new Array(level).fill(null);
}

/** 
 * @param {number} target
 * @return {boolean}
 */
Skiplist.prototype.search = function(target) {
    let cur = this.head;
    for (let i = this.level - 1; i >= 0; i--) {
        while (cur.forwards[i] !== null && cur.forwards[i].val < target) {
            cur = cur.forwards[i];
        }
    }
    cur = cur.forwards[0];
    return cur !== null && cur.val === target;
};

/** 
 * @param {number} num
 * @return {void}
 */
Skiplist.prototype.add = function(num) {
    const update = new Array(this.MAX_LEVEL);
    let cur = this.head;
    for (let i = this.level - 1; i >= 0; i--) {
        while (cur.forwards[i] !== null && cur.forwards[i].val < num) {
            cur = cur.forwards[i];
        }
        update[i] = cur;
    }

    // random level for new node
    let lvl = 1;
    while (Math.random() < this.P && lvl < this.MAX_LEVEL) {
        lvl += 1;
    }

    if (lvl > this.level) {
        for (let i = this.level; i < lvl; i++) {
            update[i] = this.head;
        }
        this.level = lvl;
    }

    const newNode = new Node(num, lvl);
    for (let i = 0; i < lvl; i++) {
        newNode.forwards[i] = update[i].forwards[i];
        update[i].forwards[i] = newNode;
    }
};

/** 
 * @param {number} num
 * @return {boolean}
 */
Skiplist.prototype.erase = function(num) {
    const update = new Array(this.MAX_LEVEL);
    let cur = this.head;
    for (let i = this.level - 1; i >= 0; i--) {
        while (cur.forwards[i] !== null && cur.forwards[i].val < num) {
            cur = cur.forwards[i];
        }
        update[i] = cur;
    }

    const targetNode = cur.forwards[0];
    if (targetNode === null || targetNode.val !== num) {
        return false;
    }

    for (let i = 0; i < this.level; i++) {
        if (update[i].forwards[i] !== targetNode) break;
        update[i].forwards[i] = targetNode.forwards[i];
    }

    // reduce level if highest levels are empty
    while (this.level > 1 && this.head.forwards[this.level - 1] === null) {
        this.level--;
    }
    return true;
};
```

## Typescript

```typescript
class Node {
    val: number;
    forwards: (Node | null)[];
    constructor(val: number, level: number) {
        this.val = val;
        this.forwards = new Array(level).fill(null);
    }
}

class Skiplist {
    private readonly MAX_LEVEL = 16;
    private readonly P = 0.5;
    private level: number;
    private head: Node;

    constructor() {
        this.level = 1;
        this.head = new Node(-Infinity, this.MAX_LEVEL);
    }

    private randomLevel(): number {
        let lvl = 1;
        while (Math.random() < this.P && lvl < this.MAX_LEVEL) {
            lvl++;
        }
        return lvl;
    }

    search(target: number): boolean {
        let cur: Node | null = this.head;
        for (let i = this.level - 1; i >= 0; i--) {
            while (cur!.forwards[i] !== null && cur!.forwards[i]!.val < target) {
                cur = cur!.forwards[i];
            }
        }
        cur = cur!.forwards[0];
        return cur !== null && cur.val === target;
    }

    add(num: number): void {
        const update: Node[] = new Array(this.MAX_LEVEL);
        let cur: Node | null = this.head;
        for (let i = this.level - 1; i >= 0; i--) {
            while (cur!.forwards[i] !== null && cur!.forwards[i]!.val < num) {
                cur = cur!.forwards[i];
            }
            update[i] = cur!;
        }

        const lvl = this.randomLevel();
        if (lvl > this.level) {
            for (let i = this.level; i < lvl; i++) {
                update[i] = this.head;
            }
            this.level = lvl;
        }

        const newNode = new Node(num, lvl);
        for (let i = 0; i < lvl; i++) {
            newNode.forwards[i] = update[i].forwards[i];
            update[i].forwards[i] = newNode;
        }
    }

    erase(num: number): boolean {
        const update: Node[] = new Array(this.MAX_LEVEL);
        let cur: Node | null = this.head;
        for (let i = this.level - 1; i >= 0; i--) {
            while (cur!.forwards[i] !== null && cur!.forwards[i]!.val < num) {
                cur = cur!.forwards[i];
            }
            update[i] = cur!;
        }

        const target = cur!.forwards[0];
        if (target === null || target.val !== num) {
            return false;
        }

        for (let i = 0; i < this.level; i++) {
            if (update[i].forwards[i] !== target) break;
            update[i].forwards[i] = target.forwards[i];
        }

        while (this.level > 1 && this.head.forwards[this.level - 1] === null) {
            this.level--;
        }
        return true;
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * var obj = new Skiplist()
 * var param_1 = obj.search(target)
 * obj.add(num)
 * var param_3 = obj.erase(num)
 */
```

## Php

```php
class Node {
    public $val;
    public $forward;

    public function __construct($val = -1, $level = 0) {
        $this->val = $val;
        $this->forward = array_fill(0, $level, null);
    }
}

class Skiplist {
    private $head;
    private $maxLevel = 16;
    private $probability = 0.5;
    private $level = 1;

    function __construct() {
        $this->head = new Node(-1, $this->maxLevel);
    }

    private function randomLevel() {
        $lvl = 1;
        while ((mt_rand() / mt_getrandmax()) < $this->probability && $lvl < $this->maxLevel) {
            $lvl++;
        }
        return $lvl;
    }

    /**
     * @param Integer $target
     * @return Boolean
     */
    function search($target) {
        $curr = $this->head;
        for ($i = $this->level - 1; $i >= 0; $i--) {
            while ($curr->forward[$i] !== null && $curr->forward[$i]->val < $target) {
                $curr = $curr->forward[$i];
            }
        }
        $curr = $curr->forward[0];
        return $curr !== null && $curr->val == $target;
    }

    /**
     * @param Integer $num
     * @return NULL
     */
    function add($num) {
        $update = array_fill(0, $this->maxLevel, null);
        $curr = $this->head;
        for ($i = $this->level - 1; $i >= 0; $i--) {
            while ($curr->forward[$i] !== null && $curr->forward[$i]->val < $num) {
                $curr = $curr->forward[$i];
            }
            $update[$i] = $curr;
        }

        $lvl = $this->randomLevel();
        if ($lvl > $this->level) {
            for ($i = $this->level; $i < $lvl; $i++) {
                $update[$i] = $this->head;
            }
            $this->level = $lvl;
        }

        $newNode = new Node($num, $lvl);
        for ($i = 0; $i < $lvl; $i++) {
            $newNode->forward[$i] = $update[$i]->forward[$i];
            $update[$i]->forward[$i] = $newNode;
        }
    }

    /**
     * @param Integer $num
     * @return Boolean
     */
    function erase($num) {
        $update = array_fill(0, $this->maxLevel, null);
        $curr = $this->head;
        for ($i = $this->level - 1; $i >= 0; $i--) {
            while ($curr->forward[$i] !== null && $curr->forward[$i]->val < $num) {
                $curr = $curr->forward[$i];
            }
            $update[$i] = $curr;
        }

        $target = $curr->forward[0];
        if ($target === null || $target->val != $num) {
            return false;
        }

        for ($i = 0; $i < $this->level; $i++) {
            if ($update[$i]->forward[$i] !== $target) {
                break;
            }
            $update[$i]->forward[$i] = $target->forward[$i];
        }

        while ($this->level > 1 && $this->head->forward[$this->level - 1] === null) {
            $this->level--;
        }

        return true;
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * $obj = new Skiplist();
 * $ret_1 = $obj->search($target);
 * $obj->add($num);
 * $ret_3 = $obj->erase($num);
 */
```

## Swift

```swift
class Skiplist {
    private class Node {
        var val: Int
        var forward: [Node?]
        init(_ val: Int, _ level: Int) {
            self.val = val
            self.forward = Array(repeating: nil, count: level)
        }
    }
    
    private let maxLevel = 16
    private var head: Node
    private var level: Int
    
    init() {
        head = Node(-1, maxLevel)
        level = 0
    }
    
    func search(_ target: Int) -> Bool {
        var current = head
        for i in stride(from: level - 1, through: 0, by: -1) {
            while let next = current.forward[i], next.val < target {
                current = next
            }
        }
        if let next = current.forward[0], next.val == target {
            return true
        }
        return false
    }
    
    func add(_ num: Int) {
        var update = Array(repeating: head, count: maxLevel)
        var current = head
        for i in stride(from: level - 1, through: 0, by: -1) {
            while let next = current.forward[i], next.val < num {
                current = next
            }
            update[i] = current
        }
        let nodeLevel = randomLevel()
        if nodeLevel > level {
            for i in level..<nodeLevel {
                update[i] = head
            }
            level = nodeLevel
        }
        let newNode = Node(num, nodeLevel)
        for i in 0..<nodeLevel {
            newNode.forward[i] = update[i].forward[i]
            update[i].forward[i] = newNode
        }
    }
    
    func erase(_ num: Int) -> Bool {
        var update = Array(repeating: head, count: maxLevel)
        var current = head
        for i in stride(from: level - 1, through: 0, by: -1) {
            while let next = current.forward[i], next.val < num {
                current = next
            }
            update[i] = current
        }
        guard let targetNode = current.forward[0], targetNode.val == num else {
            return false
        }
        for i in 0..<level {
            if update[i].forward[i] === targetNode {
                update[i].forward[i] = targetNode.forward[i]
            }
        }
        while level > 0 && head.forward[level - 1] == nil {
            level -= 1
        }
        return true
    }
    
    private func randomLevel() -> Int {
        var lvl = 1
        while Double.random(in: 0..<1) < 0.5 && lvl < maxLevel {
            lvl += 1
        }
        return lvl
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * let obj = Skiplist()
 * let ret_1: Bool = obj.search(target)
 * obj.add(num)
 * let ret_3: Bool = obj.erase(num)
 */
```

## Kotlin

```kotlin
class Skiplist() {

    private val MAX_LEVEL = 16
    private val head = Node(-1)
    private var level = 0
    private val rand = java.util.Random()

    private inner class Node(val value: Int) {
        val next = arrayOfNulls<Node>(MAX_LEVEL)
    }

    private fun randomLevel(): Int {
        var lvl = 1
        while (lvl < MAX_LEVEL && rand.nextInt(2) == 0) {
            lvl++
        }
        return lvl
    }

    fun search(target: Int): Boolean {
        var cur = head
        for (i in level - 1 downTo 0) {
            while (cur.next[i] != null && cur.next[i]!!.value < target) {
                cur = cur.next[i]!!
            }
        }
        val node = cur.next[0] ?: return false
        return node.value == target
    }

    fun add(num: Int) {
        val update = arrayOfNulls<Node>(MAX_LEVEL)
        var cur = head
        for (i in level - 1 downTo 0) {
            while (cur.next[i] != null && cur.next[i]!!.value < num) {
                cur = cur.next[i]!!
            }
            update[i] = cur
        }
        val lvl = randomLevel()
        if (lvl > level) {
            for (i in level until lvl) {
                update[i] = head
            }
            level = lvl
        }
        val newNode = Node(num)
        for (i in 0 until lvl) {
            newNode.next[i] = update[i]!!.next[i]
            update[i]!!.next[i] = newNode
        }
    }

    fun erase(num: Int): Boolean {
        val update = arrayOfNulls<Node>(MAX_LEVEL)
        var cur = head
        for (i in level - 1 downTo 0) {
            while (cur.next[i] != null && cur.next[i]!!.value < num) {
                cur = cur.next[i]!!
            }
            update[i] = cur
        }
        val targetNode = cur.next[0] ?: return false
        if (targetNode.value != num) return false
        for (i in 0 until level) {
            if (update[i]!!.next[i] !== targetNode) break
            update[i]!!.next[i] = targetNode.next[i]
        }
        while (level > 0 && head.next[level - 1] == null) {
            level--
        }
        return true
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * var obj = Skiplist()
 * var param_1 = obj.search(target)
 * obj.add(num)
 * var param_3 = obj.erase(num)
 */
```

## Dart

```dart
import 'dart:math';

class _Node {
  int val;
  List<_Node?> forward;
  _Node(this.val, int level) : forward = List.filled(level, null);
}

class Skiplist {
  static const int _MAX_LEVEL = 32;
  final _Node _head = _Node(-1, _MAX_LEVEL);
  int _level = 1;
  final Random _rand = Random();

  Skiplist();

  bool search(int target) {
    var node = _head;
    for (int i = _level - 1; i >= 0; --i) {
      while (node.forward[i] != null && node.forward[i]!.val < target) {
        node = node.forward[i]!;
      }
    }
    node = node.forward[0];
    return node != null && node.val == target;
  }

  void add(int num) {
    List<_Node?> update = List.filled(_MAX_LEVEL, null);
    var node = _head;
    for (int i = _level - 1; i >= 0; --i) {
      while (node.forward[i] != null && node.forward[i]!.val < num) {
        node = node.forward[i]!;
      }
      update[i] = node;
    }

    int lvl = _randomLevel();
    if (lvl > _level) {
      for (int i = _level; i < lvl; ++i) {
        update[i] = _head;
      }
      _level = lvl;
    }

    var newNode = _Node(num, lvl);
    for (int i = 0; i < lvl; ++i) {
      newNode.forward[i] = update[i]!.forward[i];
      update[i]!.forward[i] = newNode;
    }
  }

  bool erase(int num) {
    List<_Node?> update = List.filled(_MAX_LEVEL, null);
    var node = _head;
    for (int i = _level - 1; i >= 0; --i) {
      while (node.forward[i] != null && node.forward[i]!.val < num) {
        node = node.forward[i]!;
      }
      update[i] = node;
    }

    var target = node.forward[0];
    if (target == null || target.val != num) return false;

    for (int i = 0; i < _level; ++i) {
      if (update[i]!.forward[i] != target) break;
      update[i]!.forward[i] = target.forward[i];
    }

    while (_level > 1 && _head.forward[_level - 1] == null) {
      _level--;
    }
    return true;
  }

  int _randomLevel() {
    int lvl = 1;
    while (_rand.nextDouble() < 0.5 && lvl < _MAX_LEVEL) {
      lvl++;
    }
    return lvl;
  }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist obj = Skiplist();
 * bool param1 = obj.search(target);
 * obj.add(num);
 * bool param3 = obj.erase(num);
 */
```

## Golang

```go
package main

import (
	"math/rand"
	"time"
)

type node struct {
	val  int
	next []*node
}

type Skiplist struct {
	head     *node
	level    int
	maxLevel int
	p        float64
}

func Constructor() Skiplist {
	rand.Seed(time.Now().UnixNano())
	const maxL = 32
	return Skiplist{
		head:     &node{next: make([]*node, maxL)},
		level:    1,
		maxLevel: maxL,
		p:        0.25,
	}
}

func (s *Skiplist) randomLevel() int {
	lvl := 1
	for lvl < s.maxLevel && rand.Float64() < s.p {
		lvl++
	}
	return lvl
}

func (s *Skiplist) Search(target int) bool {
	cur := s.head
	for i := s.level - 1; i >= 0; i-- {
		for cur.next[i] != nil && cur.next[i].val < target {
			cur = cur.next[i]
		}
	}
	cur = cur.next[0]
	return cur != nil && cur.val == target
}

func (s *Skiplist) Add(num int) {
	update := make([]*node, s.maxLevel)
	cur := s.head
	for i := s.level - 1; i >= 0; i-- {
		for cur.next[i] != nil && cur.next[i].val < num {
			cur = cur.next[i]
		}
		update[i] = cur
	}
	lvl := s.randomLevel()
	if lvl > s.level {
		for i := s.level; i < lvl; i++ {
			update[i] = s.head
		}
		s.level = lvl
	}
	newNode := &node{val: num, next: make([]*node, lvl)}
	for i := 0; i < lvl; i++ {
		newNode.next[i] = update[i].next[i]
		update[i].next[i] = newNode
	}
}

func (s *Skiplist) Erase(num int) bool {
	update := make([]*node, s.maxLevel)
	cur := s.head
	for i := s.level - 1; i >= 0; i-- {
		for cur.next[i] != nil && cur.next[i].val < num {
			cur = cur.next[i]
		}
		update[i] = cur
	}
	target := cur.next[0]
	if target == nil || target.val != num {
		return false
	}
	for i := 0; i < s.level; i++ {
		if update[i].next[i] != target {
			continue
		}
		update[i].next[i] = target.next[i]
	}
	for s.level > 1 && s.head.next[s.level-1] == nil {
		s.level--
	}
	return true
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Search(target);
 * obj.Add(num);
 * param_3 := obj.Erase(num);
 */
```

## Ruby

```ruby
class Node
  attr_accessor :val, :forward

  def initialize(val, level)
    @val = val
    @forward = Array.new(level, nil)
  end
end

class Skiplist
  MAX_LEVEL = 32
  P = 0.5

  def initialize()
    @level = 1
    @head = Node.new(-Float::INFINITY, MAX_LEVEL)
  end

=begin
    :type target: Integer
    :rtype: Boolean
=end
  def search(target)
    x = @head
    i = @level - 1
    while i >= 0
      while x.forward[i] && x.forward[i].val < target
        x = x.forward[i]
      end
      i -= 1
    end
    x = x.forward[0]
    !!(x && x.val == target)
  end

=begin
    :type num: Integer
    :rtype: Void
=end
  def add(num)
    update = Array.new(MAX_LEVEL)
    x = @head
    i = @level - 1
    while i >= 0
      while x.forward[i] && x.forward[i].val < num
        x = x.forward[i]
      end
      update[i] = x
      i -= 1
    end

    lvl = random_level
    if lvl > @level
      ( @level...lvl ).each { |j| update[j] = @head }
      @level = lvl
    end

    new_node = Node.new(num, lvl)
    (0...lvl).each do |j|
      new_node.forward[j] = update[j].forward[j]
      update[j].forward[j] = new_node
    end
  end

=begin
    :type num: Integer
    :rtype: Boolean
=end
  def erase(num)
    update = Array.new(MAX_LEVEL)
    x = @head
    i = @level - 1
    while i >= 0
      while x.forward[i] && x.forward[i].val < num
        x = x.forward[i]
      end
      update[i] = x
      i -= 1
    end

    target = x.forward[0]
    return false unless target && target.val == num

    (0...@level).each do |j|
      break if update[j].forward[j] != target
      update[j].forward[j] = target.forward[j]
    end

    while @level > 1 && @head.forward[@level - 1].nil?
      @level -= 1
    end
    true
  end

  private

  def random_level
    lvl = 1
    while rand < P && lvl < MAX_LEVEL
      lvl += 1
    end
    lvl
  end
end
```

## Scala

```scala
class Skiplist() {
  private class Node(val value: Int, val forward: Array[Node])

  private val MAX_LEVEL = 16
  private val head = new Node(-1, new Array[Node](MAX_LEVEL))
  private var level = 1
  private val rand = new scala.util.Random()

  def search(target: Int): Boolean = {
    var cur = head
    var i = level - 1
    while (i >= 0) {
      while (cur.forward(i) != null && cur.forward(i).value < target) {
        cur = cur.forward(i)
      }
      i -= 1
    }
    cur = cur.forward(0)
    cur != null && cur.value == target
  }

  def add(num: Int): Unit = {
    val update = new Array[Node](MAX_LEVEL)
    var cur = head
    var i = level - 1
    while (i >= 0) {
      while (cur.forward(i) != null && cur.forward(i).value < num) {
        cur = cur.forward(i)
      }
      update(i) = cur
      i -= 1
    }

    var lvl = 1
    while (lvl < MAX_LEVEL && rand.nextInt(2) == 0) {
      lvl += 1
    }

    if (lvl > level) {
      var j = level
      while (j < lvl) {
        update(j) = head
        j += 1
      }
      level = lvl
    }

    val newNode = new Node(num, new Array[Node](lvl))
    i = 0
    while (i < lvl) {
      newNode.forward(i) = update(i).forward(i)
      update(i).forward(i) = newNode
      i += 1
    }
  }

  def erase(num: Int): Boolean = {
    val update = new Array[Node](MAX_LEVEL)
    var cur = head
    var i = level - 1
    while (i >= 0) {
      while (cur.forward(i) != null && cur.forward(i).value < num) {
        cur = cur.forward(i)
      }
      update(i) = cur
      i -= 1
    }

    val targetNode = cur.forward(0)
    if (targetNode == null || targetNode.value != num) return false

    i = 0
    while (i < level) {
      if (update(i).forward(i) == targetNode) {
        update(i).forward(i) = targetNode.forward(i)
      }
      i += 1
    }

    while (level > 1 && head.forward(level - 1) == null) {
      level -= 1
    }
    true
  }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * val obj = new Skiplist()
 * val param_1 = obj.search(target)
 * obj.add(num)
 * val param_3 = obj.erase(num)
 */
```

## Rust

```rust
use std::collections::BTreeMap;

struct Skiplist {
    map: BTreeMap<i32, i32>,
}

impl Skiplist {
    fn new() -> Self {
        Skiplist {
            map: BTreeMap::new(),
        }
    }

    fn search(&self, target: i32) -> bool {
        self.map.contains_key(&target)
    }

    fn add(&mut self, num: i32) {
        *self.map.entry(num).or_insert(0) += 1;
    }

    fn erase(&mut self, num: i32) -> bool {
        if let Some(cnt) = self.map.get_mut(&num) {
            if *cnt > 1 {
                *cnt -= 1;
            } else {
                self.map.remove(&num);
            }
            true
        } else {
            false
        }
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * let mut obj = Skiplist::new();
 * let ret_1: bool = obj.search(target);
 * obj.add(num);
 * let ret_3: bool = obj.erase(num);
 */
```

## Racket

```racket
(define skiplist%
  (class object%
    (super-new)

    ;; vector storing counts for each possible value [0,20000]
    (define cnt (make-vector 20001 0))

    ;; search : exact-integer? -> boolean?
    (define/public (search target)
      (if (and (exact-integer? target)
               (>= target 0)
               (< target (vector-length cnt))
               (> (vector-ref cnt target) 0))
          #t
          #f))

    ;; add : exact-integer? -> void?
    (define/public (add num)
      (when (and (exact-integer? num)
                 (>= num 0)
                 (< num (vector-length cnt)))
        (vector-set! cnt num (+ 1 (vector-ref cnt num)))))

    ;; erase : exact-integer? -> boolean?
    (define/public (erase num)
      (if (and (exact-integer? num)
               (>= num 0)
               (< num (vector-length cnt))
               (> (vector-ref cnt num) 0))
          (begin
            (vector-set! cnt num (- (vector-ref cnt num) 1))
            #t)
          #f))))
```

## Erlang

```erlang
-module(skiplist).

-define(MAX_LEVEL, 16).

-export([skiplist_init_/0,
         skiplist_search/1,
         skiplist_add/1,
         skiplist_erase/1]).

%% Initialization
skiplist_init_() ->
    Table = ets:new(?MODULE, [named_table, public, {read_concurrency,true}]),
    put(skiplist_table, Table),
    put(head, 0),
    put(max_level, 1),
    put(next_id, 1),
    %% head node (value unused)
    ets:insert(Table, {0, #{value => -1, forward => #{}}}),
    ok.

%% Search
skiplist_search(Target) when is_integer(Target) ->
    Head = get(head),
    MaxLevel = get(max_level),
    search_from(Head, MaxLevel, Target).

search_from(_Cur, 0, Target) ->
    Next = get_forward(get(head), 1),
    case Next of
        undefined -> false;
        Id -> node_value(Id) =:= Target
    end;
search_from(Cur, Level, Target) ->
    Next = get_forward(Cur, Level),
    case Next of
        undefined ->
            search_from(Cur, Level - 1, Target);
        Id ->
            Val = node_value(Id),
            if Val < Target ->
                    search_from(Id, Level, Target);
               true ->
                    search_from(Cur, Level - 1, Target)
            end
    end.

%% Add
skiplist_add(Num) when is_integer(Num) ->
    Head = get(head),
    MaxLevel = get(max_level),
    UpdateMap0 = build_update(Head, MaxLevel, Num, #{}),

    NewLvl = random_level(),
    CurMax = get(max_level),
    UpdateMap1 =
        if NewLvl > CurMax ->
                %% extend update map with head for new levels
                lists:foldl(fun(I, Acc) -> maps:put(I, Head, Acc) end,
                            UpdateMap0,
                            lists:seq(CurMax + 1, NewLvl));
           true -> UpdateMap0
        end,

    put(max_level, max(NewLvl, CurMax)),

    Id = get(next_id),
    put(next_id, Id + 1),

    %% create forward map for new node and adjust predecessors
    ForwardNew = insert_node(Id, Num, NewLvl, UpdateMap1),
    ok.

insert_node(_Id, _Num, 0, _Update) ->
    #{};
insert_node(Id, Num, Level, Update) when Level > 0 ->
    PrevId = maps:get(Level, Update),
    PrevNode = get_node(PrevId),
    PrevFwd = maps:get(forward, PrevNode),

    NextId = maps:get(Level, PrevFwd, undefined),

    %% set forward of new node at this level
    ForwardRest = insert_node(Id, Num, Level - 1, Update),

    NewForward = maps:put(Level, NextId, ForwardRest),

    %% update predecessor's forward to point to new node
    UpdatedPrevFwd = maps:put(Level, Id, PrevFwd),
    UpdatedPrevNode = PrevNode#{forward => UpdatedPrevFwd},
    put_node(PrevId, UpdatedPrevNode),

    NewForward.

%% Erase
skiplist_erase(Num) when is_integer(Num) ->
    Head = get(head),
    MaxLevel = get(max_level),
    UpdateMap = build_update(Head, MaxLevel, Num, #{}),

    FirstPrev = maps:get(1, UpdateMap),
    CandidateId = get_forward(FirstPrev, 1),

    case CandidateId of
        undefined ->
            false;
        Id when node_value(Id) =:= Num ->
            CandidateNode = get_node(Id),
            CandidateFwd = maps:get(forward, CandidateNode),

            %% remove references from predecessors
            lists:foreach(
              fun(Level) ->
                      PrevId = maps:get(Level, UpdateMap, undefined),
                      case PrevId of
                          undefined -> ok;
                          _ ->
                              PrevNode = get_node(PrevId),
                              PrevFwd = maps:get(forward, PrevNode),
                              case maps:get(Level, PrevFwd, undefined) of
                                  Id ->
                                      NextOfCand = maps:get(Level, CandidateFwd, undefined),
                                      UpdatedPrevFwd =
                                          if NextOfCand =:= undefined ->
                                                  maps:remove(Level, PrevFwd);
                                             true ->
                                                  maps:put(Level, NextOfCand, PrevFwd)
                                          end,
                                      UpdatedPrevNode = PrevNode#{forward => UpdatedPrevFwd},
                                      put_node(PrevId, UpdatedPrevNode);
                                  _ -> ok
                              end
                      end
              end,
              lists:seq(1, MaxLevel)),

            %% delete the node
            ets:delete(get(skiplist_table), Id),

            adjust_max_level(),
            true;
        _ ->
            false
    end.

adjust_max_level() ->
    Head = get(head),
    CurMax = get(max_level),
    NewMax = find_new_max(Head, CurMax),
    put(max_level, NewMax).

find_new_max(_Head, 1) -> 1;
find_new_max(Head, Level) ->
    case get_forward(Head, Level) of
        undefined -> find_new_max(Head, Level - 1);
        _ -> Level
    end.

%% Helpers

build_update(Cur, 0, _Num, Acc) -> Acc;
build_update(Cur, Level, Num, Acc) ->
    Next = get_forward(Cur, Level),
    case Next of
        undefined ->
            NewAcc = maps:put(Level, Cur, Acc),
            build_update(Cur, Level - 1, Num, NewAcc);
        Id ->
            Val = node_value(Id),
            if Val < Num ->
                    build_update(Id, Level, Num, Acc);
               true ->
                    NewAcc = maps:put(Level, Cur, Acc),
                    build_update(Cur, Level - 1, Num, NewAcc)
            end
    end.

random_level() -> random_level(1).

random_level(Lvl) when Lvl < ?MAX_LEVEL ->
    case rand:uniform(2) of
        1 -> random_level(Lvl + 1);
        _ -> Lvl
    end;
random_level(Lvl) -> Lvl.

get_node(Id) ->
    [{_, Node}] = ets:lookup(get(skiplist_table), Id),
    Node.

put_node(Id, Node) ->
    ets:insert(get(skiplist_table), {Id, Node}).

node_value(Id) ->
    maps:get(value, get_node(Id)).

get_forward(Id, Level) ->
    case ets:lookup(get(skiplist_table), Id) of
        [] -> undefined;
        [{_, Node}] ->
            Forward = maps:get(forward, Node),
            maps:get(Level, Forward, undefined)
    end.
```

## Elixir

```elixir
defmodule Skiplist do
  @state_key :skiplist_state

  @spec init_() :: any
  def init_() do
    Process.put(@state_key, %{})
  end

  @spec search(target :: integer) :: boolean
  def search(target) do
    state = Process.get(@state_key, %{})
    Map.has_key?(state, target)
  end

  @spec add(num :: integer) :: any
  def add(num) do
    state = Process.get(@state_key, %{})
    new_state = Map.update(state, num, 1, &(&1 + 1))
    Process.put(@state_key, new_state)
  end

  @spec erase(num :: integer) :: boolean
  def erase(num) do
    state = Process.get(@state_key, %{})
    case Map.fetch(state, num) do
      :error ->
        false

      {:ok, cnt} when cnt > 1 ->
        Process.put(@state_key, Map.put(state, num, cnt - 1))
        true

      {:ok, _cnt} ->
        Process.put(@state_key, Map.delete(state, num))
        true
    end
  end
end
```
