# 0707. Design Linked List

## Cpp

```cpp
class MyLinkedList {
private:
    struct Node {
        int val;
        Node* next;
        Node(int v) : val(v), next(nullptr) {}
    };
    Node* dummy; // sentinel head
    int sz;
public:
    MyLinkedList() {
        dummy = new Node(0);
        sz = 0;
    }
    
    ~MyLinkedList() {
        Node* cur = dummy;
        while (cur) {
            Node* nxt = cur->next;
            delete cur;
            cur = nxt;
        }
    }
    
    int get(int index) {
        if (index < 0 || index >= sz) return -1;
        Node* cur = dummy->next;
        for (int i = 0; i < index; ++i) cur = cur->next;
        return cur->val;
    }
    
    void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    void addAtTail(int val) {
        addAtIndex(sz, val);
    }
    
    void addAtIndex(int index, int val) {
        if (index > sz) return;
        if (index < 0) index = 0;
        Node* prev = dummy;
        for (int i = 0; i < index; ++i) prev = prev->next;
        Node* node = new Node(val);
        node->next = prev->next;
        prev->next = node;
        ++sz;
    }
    
    void deleteAtIndex(int index) {
        if (index < 0 || index >= sz) return;
        Node* prev = dummy;
        for (int i = 0; i < index; ++i) prev = prev->next;
        Node* del = prev->next;
        prev->next = del->next;
        delete del;
        --sz;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
```

## Java

```java
class MyLinkedList {
    private static class Node {
        int val;
        Node next;
        Node(int v) { this.val = v; }
    }
    
    private final Node dummy;
    private int size;
    
    public MyLinkedList() {
        dummy = new Node(0);
        size = 0;
    }
    
    public int get(int index) {
        if (index < 0 || index >= size) return -1;
        Node cur = dummy.next;
        for (int i = 0; i < index; i++) {
            cur = cur.next;
        }
        return cur.val;
    }
    
    public void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    public void addAtTail(int val) {
        addAtIndex(size, val);
    }
    
    public void addAtIndex(int index, int val) {
        if (index > size) return;
        if (index < 0) index = 0;
        Node pred = dummy;
        for (int i = 0; i < index; i++) {
            pred = pred.next;
        }
        Node toAdd = new Node(val);
        toAdd.next = pred.next;
        pred.next = toAdd;
        size++;
    }
    
    public void deleteAtIndex(int index) {
        if (index < 0 || index >= size) return;
        Node pred = dummy;
        for (int i = 0; i < index; i++) {
            pred = pred.next;
        }
        pred.next = pred.next.next;
        size--;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
```

## Python

```python
class MyLinkedList(object):
    class Node:
        __slots__ = ('val', 'next')
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy = MyLinkedList.Node(0)  # dummy head
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummy.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val as the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        new_node = MyLinkedList.Node(val, prev.next)
        prev.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.size -= 1
```

## Python3

```python
class MyLinkedList:
    class Node:
        __slots__ = ('val', 'next')
        def __init__(self, val: int = 0, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = self.Node()  # dummy head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        pred = self.head
        for _ in range(index):
            pred = pred.next
        node = self.Node(val, pred.next)
        pred.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next
        self.size -= 1
```

## C

```c
#include <stdlib.h>

typedef struct ListNode {
    int val;
    struct ListNode* next;
} ListNode;

typedef struct {
    ListNode* dummy; // sentinel node before head
    int size;
} MyLinkedList;

/** Initialize your data structure here. */
MyLinkedList* myLinkedListCreate() {
    MyLinkedList* obj = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    if (!obj) return NULL;
    obj->dummy = (ListNode*)malloc(sizeof(ListNode));
    obj->dummy->next = NULL;
    obj->size = 0;
    return obj;
}

/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
int myLinkedListGet(MyLinkedList* obj, int index) {
    if (index < 0 || index >= obj->size) return -1;
    ListNode* cur = obj->dummy->next;
    while (index--) {
        cur = cur->next;
    }
    return cur->val;
}

/** Add a node of value val before the first element of the linked list. */
void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
    // Insert at index 0
    ListNode* newNode = (ListNode*)malloc(sizeof(ListNode));
    newNode->val = val;
    newNode->next = obj->dummy->next;
    obj->dummy->next = newNode;
    obj->size++;
}

/** Append a node of value val to the last element of the linked list. */
void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
    // Insert at index size
    ListNode* prev = obj->dummy;
    while (prev->next != NULL) {
        prev = prev->next;
    }
    ListNode* newNode = (ListNode*)malloc(sizeof(ListNode));
    newNode->val = val;
    newNode->next = NULL;
    prev->next = newNode;
    obj->size++;
}

/** Add a node of value val before the index-th node in the linked list. */
void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    if (index < 0 || index > obj->size) return;
    ListNode* prev = obj->dummy;
    while (index--) {
        prev = prev->next;
    }
    ListNode* newNode = (ListNode*)malloc(sizeof(ListNode));
    newNode->val = val;
    newNode->next = prev->next;
    prev->next = newNode;
    obj->size++;
}

/** Delete the index-th node in the linked list, if the index is valid. */
void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
    if (index < 0 || index >= obj->size) return;
    ListNode* prev = obj->dummy;
    while (index--) {
        prev = prev->next;
    }
    ListNode* del = prev->next;
    prev->next = del->next;
    free(del);
    obj->size--;
}

/** Free all memory associated with the linked list. */
void myLinkedListFree(MyLinkedList* obj) {
    ListNode* cur = obj->dummy;
    while (cur != NULL) {
        ListNode* nxt = cur->next;
        free(cur);
        cur = nxt;
    }
    free(obj);
}
```

## Csharp

```csharp
public class MyLinkedList {
    private class Node {
        public int val;
        public Node next;
        public Node(int v) { val = v; }
    }

    private readonly Node dummy;
    private int size;

    public MyLinkedList() {
        dummy = new Node(0);
        size = 0;
    }

    public int Get(int index) {
        if (index < 0 || index >= size) return -1;
        Node cur = dummy.next;
        for (int i = 0; i < index; i++) {
            cur = cur.next;
        }
        return cur.val;
    }

    public void AddAtHead(int val) {
        AddAtIndex(0, val);
    }

    public void AddAtTail(int val) {
        AddAtIndex(size, val);
    }

    public void AddAtIndex(int index, int val) {
        if (index > size) return;
        if (index < 0) index = 0;
        Node prev = dummy;
        for (int i = 0; i < index; i++) {
            prev = prev.next;
        }
        Node node = new Node(val);
        node.next = prev.next;
        prev.next = node;
        size++;
    }

    public void DeleteAtIndex(int index) {
        if (index < 0 || index >= size) return;
        Node prev = dummy;
        for (int i = 0; i < index; i++) {
            prev = prev.next;
        }
        Node toDelete = prev.next;
        prev.next = toDelete.next;
        size--;
    }
}
```

## Javascript

```javascript
var MyLinkedList = function() {
    this.dummy = { val: 0, next: null };
    this.size = 0;
};

MyLinkedList.prototype.get = function(index) {
    if (index < 0 || index >= this.size) return -1;
    let cur = this.dummy.next;
    for (let i = 0; i < index; i++) {
        cur = cur.next;
    }
    return cur.val;
};

MyLinkedList.prototype.addAtHead = function(val) {
    this.addAtIndex(0, val);
};

MyLinkedList.prototype.addAtTail = function(val) {
    this.addAtIndex(this.size, val);
};

MyLinkedList.prototype.addAtIndex = function(index, val) {
    if (index > this.size) return;
    if (index < 0) index = 0;
    let pred = this.dummy;
    for (let i = 0; i < index; i++) {
        pred = pred.next;
    }
    const node = { val: val, next: pred.next };
    pred.next = node;
    this.size++;
};

MyLinkedList.prototype.deleteAtIndex = function(index) {
    if (index < 0 || index >= this.size) return;
    let pred = this.dummy;
    for (let i = 0; i < index; i++) {
        pred = pred.next;
    }
    pred.next = pred.next.next;
    this.size--;
};
```

## Typescript

```typescript
class MyLinkedList {
    private head: ListNode | null = null;
    private size: number = 0;

    constructor() {}

    get(index: number): number {
        if (index < 0 || index >= this.size) return -1;
        let cur = this.head!;
        for (let i = 0; i < index; i++) {
            cur = cur.next!;
        }
        return cur.val;
    }

    addAtHead(val: number): void {
        const node = new ListNode(val, this.head);
        this.head = node;
        this.size++;
    }

    addAtTail(val: number): void {
        this.addAtIndex(this.size, val);
    }

    addAtIndex(index: number, val: number): void {
        if (index < 0 || index > this.size) return;
        if (index === 0) {
            this.addAtHead(val);
            return;
        }
        let prev = this.head!;
        for (let i = 0; i < index - 1; i++) {
            prev = prev.next!;
        }
        const node = new ListNode(val, prev.next);
        prev.next = node;
        this.size++;
    }

    deleteAtIndex(index: number): void {
        if (index < 0 || index >= this.size) return;
        if (index === 0) {
            this.head = this.head?.next ?? null;
        } else {
            let prev = this.head!;
            for (let i = 0; i < index - 1; i++) {
                prev = prev.next!;
            }
            prev.next = prev.next?.next ?? null;
        }
        this.size--;
    }
}

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val: number, next: ListNode | null = null) {
        this.val = val;
        this.next = next;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = new MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */
```

## Php

```php
class ListNode {
    public $val;
    public $next;

    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}

class MyLinkedList {
    /**
     * @var ListNode
     */
    private $dummy;
    /**
     * @var int
     */
    private $size;

    function __construct() {
        $this->dummy = new ListNode(0);
        $this->size = 0;
    }

    /**
     * @param Integer $index
     * @return Integer
     */
    function get($index) {
        if ($index < 0 || $index >= $this->size) {
            return -1;
        }
        $curr = $this->dummy->next;
        for ($i = 0; $i < $index; $i++) {
            $curr = $curr->next;
        }
        return $curr->val;
    }

    /**
     * @param Integer $val
     * @return NULL
     */
    function addAtHead($val) {
        $this->addAtIndex(0, $val);
    }

    /**
     * @param Integer $val
     * @return NULL
     */
    function addAtTail($val) {
        $this->addAtIndex($this->size, $val);
    }

    /**
     * @param Integer $index
     * @param Integer $val
     * @return NULL
     */
    function addAtIndex($index, $val) {
        if ($index > $this->size) {
            return;
        }
        if ($index < 0) {
            $index = 0;
        }
        $prev = $this->dummy;
        for ($i = 0; $i < $index; $i++) {
            $prev = $prev->next;
        }
        $node = new ListNode($val);
        $node->next = $prev->next;
        $prev->next = $node;
        $this->size++;
    }

    /**
     * @param Integer $index
     * @return NULL
     */
    function deleteAtIndex($index) {
        if ($index < 0 || $index >= $this->size) {
            return;
        }
        $prev = $this->dummy;
        for ($i = 0; $i < $index; $i++) {
            $prev = $prev->next;
        }
        $toDelete = $prev->next;
        $prev->next = $toDelete->next;
        $this->size--;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * $obj = new MyLinkedList();
 * $ret_1 = $obj->get($index);
 * $obj->addAtHead($val);
 * $obj->addAtTail($val);
 * $obj->addAtIndex($index, $val);
 * $obj->deleteAtIndex($index);
 */
```

## Swift

```swift
class MyLinkedList {
    private class Node {
        var val: Int
        var next: Node?
        init(_ val: Int) {
            self.val = val
            self.next = nil
        }
    }
    
    private let dummy: Node
    private var size: Int
    
    init() {
        dummy = Node(0)
        size = 0
    }
    
    func get(_ index: Int) -> Int {
        if index < 0 || index >= size { return -1 }
        var cur = dummy.next
        for _ in 0..<index {
            cur = cur?.next
        }
        return cur?.val ?? -1
    }
    
    func addAtHead(_ val: Int) {
        addAtIndex(0, val)
    }
    
    func addAtTail(_ val: Int) {
        addAtIndex(size, val)
    }
    
    func addAtIndex(_ index: Int, _ val: Int) {
        if index < 0 || index > size { return }
        var prev = dummy
        for _ in 0..<index {
            if let next = prev.next {
                prev = next
            }
        }
        let node = Node(val)
        node.next = prev.next
        prev.next = node
        size += 1
    }
    
    func deleteAtIndex(_ index: Int) {
        if index < 0 || index >= size { return }
        var prev = dummy
        for _ in 0..<index {
            if let next = prev.next {
                prev = next
            }
        }
        let del = prev.next
        prev.next = del?.next
        size -= 1
    }
}
```

## Kotlin

```kotlin
class MyLinkedList() {
    private data class Node(var `val`: Int, var next: Node? = null)

    private val dummy = Node(0)
    private var size = 0

    fun get(index: Int): Int {
        if (index < 0 || index >= size) return -1
        var cur = dummy.next
        var i = 0
        while (i < index && cur != null) {
            cur = cur.next
            i++
        }
        return cur?.`val` ?: -1
    }

    fun addAtHead(`val`: Int) {
        addAtIndex(0, `val`)
    }

    fun addAtTail(`val`: Int) {
        addAtIndex(size, `val`)
    }

    fun addAtIndex(index: Int, `val`: Int) {
        var idx = index
        if (idx > size) return
        if (idx < 0) idx = 0
        var prev = dummy
        var i = 0
        while (i < idx) {
            prev = prev.next!!
            i++
        }
        val node = Node(`val`)
        node.next = prev.next
        prev.next = node
        size++
    }

    fun deleteAtIndex(index: Int) {
        if (index < 0 || index >= size) return
        var prev = dummy
        var i = 0
        while (i < index) {
            prev = prev.next!!
            i++
        }
        val toDelete = prev.next
        prev.next = toDelete?.next
        size--
    }
}
```

## Dart

```dart
class Node {
  int val;
  Node? next;
  Node(this.val, [this.next]);
}

class MyLinkedList {
  Node _dummy = Node(0);
  int _size = 0;

  MyLinkedList() {}

  int get(int index) {
    if (index < 0 || index >= _size) return -1;
    Node? cur = _dummy.next;
    for (int i = 0; i < index; i++) {
      cur = cur!.next;
    }
    return cur!.val;
  }

  void addAtHead(int val) {
    addAtIndex(0, val);
  }

  void addAtTail(int val) {
    addAtIndex(_size, val);
  }

  void addAtIndex(int index, int val) {
    if (index < 0 || index > _size) return;
    Node pred = _dummy;
    for (int i = 0; i < index; i++) {
      pred = pred.next!;
    }
    Node newNode = Node(val, pred.next);
    pred.next = newNode;
    _size++;
  }

  void deleteAtIndex(int index) {
    if (index < 0 || index >= _size) return;
    Node pred = _dummy;
    for (int i = 0; i < index; i++) {
      pred = pred.next!;
    }
    pred.next = pred.next!.next;
    _size--;
  }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = MyLinkedList();
 * int param1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
```

## Golang

```go
type Node struct {
	val  int
	next *Node
}

type MyLinkedList struct {
	head *Node
	size int
}

/** Initialize your data structure here. */
func Constructor() MyLinkedList {
	// dummy head simplifies edge operations
	return MyLinkedList{
		head: &Node{},
		size: 0,
	}
}

/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
func (this *MyLinkedList) Get(index int) int {
	if index < 0 || index >= this.size {
		return -1
	}
	curr := this.head.next
	for i := 0; i < index; i++ {
		curr = curr.next
	}
	return curr.val
}

/** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
func (this *MyLinkedList) AddAtHead(val int) {
	this.AddAtIndex(0, val)
}

/** Append a node of value val to the last element of the linked list. */
func (this *MyLinkedList) AddAtTail(val int) {
	this.AddAtIndex(this.size, val)
}

/** Add a node of value val before the index-th node in the linked list.
If index equals to the length of linked list, the node will be appended to the end of linked list.
If index is greater than the length, the node will not be inserted. */
func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index > this.size {
		return
	}
	if index < 0 {
		index = 0
	}
	prev := this.head
	for i := 0; i < index; i++ {
		prev = prev.next
	}
	newNode := &Node{val: val, next: prev.next}
	prev.next = newNode
	this.size++
}

/** Delete the index-th node in the linked list, if the index is valid. */
func (this *MyLinkedList) DeleteAtIndex(index int) {
	if index < 0 || index >= this.size {
		return
	}
	prev := this.head
	for i := 0; i < index; i++ {
		prev = prev.next
	}
	// remove node
	prev.next = prev.next.next
	this.size--
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */
```

## Ruby

```ruby
class MyLinkedList
  def initialize()
    @data = []
  end

=begin
    :type index: Integer
    :rtype: Integer
=end
  def get(index)
    return -1 unless index.between?(0, @data.length - 1)
    @data[index]
  end

=begin
    :type val: Integer
    :rtype: Void
=end
  def add_at_head(val)
    @data.unshift(val)
  end

=begin
    :type val: Integer
    :rtype: Void
=end
  def add_at_tail(val)
    @data.push(val)
  end

=begin
    :type index: Integer
    :type val: Integer
    :rtype: Void
=end
  def add_at_index(index, val)
    if index > @data.length
      return
    elsif index <= 0
      @data.unshift(val)
    else
      @data.insert(index, val)
    end
  end

=begin
    :type index: Integer
    :rtype: Void
=end
  def delete_at_index(index)
    return unless index.between?(0, @data.length - 1)
    @data.delete_at(index)
  end
end
```

## Scala

```scala
class MyLinkedList() {

  private class Node(var value: Int, var next: Node)

  private val dummy = new Node(0, null)
  private var size = 0

  def get(index: Int): Int = {
    if (index < 0 || index >= size) -1
    else {
      var cur = dummy.next
      var i = 0
      while (i < index) {
        cur = cur.next
        i += 1
      }
      cur.value
    }
  }

  def addAtHead(`val`: Int): Unit = addAtIndex(0, `val`)

  def addAtTail(`val`: Int): Unit = addAtIndex(size, `val`)

  def addAtIndex(index: Int, `val`: Int): Unit = {
    if (index < 0 || index > size) return
    var prev = dummy
    var i = 0
    while (i < index) {
      prev = prev.next
      i += 1
    }
    val node = new Node(`val`, prev.next)
    prev.next = node
    size += 1
  }

  def deleteAtIndex(index: Int): Unit = {
    if (index < 0 || index >= size) return
    var prev = dummy
    var i = 0
    while (i < index) {
      prev = prev.next
      i += 1
    }
    prev.next = prev.next.next
    size -= 1
  }

}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * val obj = new MyLinkedList()
 * val param_1 = obj.get(index)
 * obj.addAtHead(`val`)
 * obj.addAtTail(`val`)
 * obj.addAtIndex(index,`val`)
 * obj.deleteAtIndex(index)
 */
```

## Rust

```rust
struct MyLinkedList {
    data: Vec<i32>,
}

impl MyLinkedList {
    fn new() -> Self {
        MyLinkedList { data: Vec::new() }
    }

    fn get(&self, index: i32) -> i32 {
        if index < 0 {
            return -1;
        }
        let idx = index as usize;
        if idx >= self.data.len() {
            -1
        } else {
            self.data[idx]
        }
    }

    fn add_at_head(&mut self, val: i32) {
        self.data.insert(0, val);
    }

    fn add_at_tail(&mut self, val: i32) {
        self.data.push(val);
    }

    fn add_at_index(&mut self, index: i32, val: i32) {
        if index < 0 {
            return;
        }
        let idx = index as usize;
        if idx > self.data.len() {
            return;
        }
        self.data.insert(idx, val);
    }

    fn delete_at_index(&mut self, index: i32) {
        if index < 0 {
            return;
        }
        let idx = index as usize;
        if idx >= self.data.len() {
            return;
        }
        self.data.remove(idx);
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * let mut obj = MyLinkedList::new();
 * let ret_1: i32 = obj.get(index);
 * obj.add_at_head(val);
 * obj.add_at_tail(val);
 * obj.add_at_index(index, val);
 * obj.delete_at_index(index);
 */
```

## Racket

```racket
(struct node ([val #:mutable] [next #:mutable]) #:transparent)

(define my-linked-list%
  (class object%
    (super-new)
    (field [head #f]
           [tail #f]
           [size 0])

    ; get : exact-integer? -> exact-integer?
    (define/public (get index)
      (if (or (< index 0) (>= index size))
          -1
          (let loop ((cur head) (i index))
            (if (= i 0)
                (node-val cur)
                (loop (node-next cur) (- i 1))))))

    ; add-at-head : exact-integer? -> void?
    (define/public (add-at-head val)
      (let ([new-node (node val #f)])
        (set-node-next! new-node head)
        (set! head new-node)
        (when (= size 0) (set! tail new-node))
        (set! size (+ size 1))))

    ; add-at-tail : exact-integer? -> void?
    (define/public (add-at-tail val)
      (if (= size 0)
          (add-at-head val)
          (let ([new-node (node val #f)])
            (set-node-next! tail new-node)
            (set! tail new-node)
            (set! size (+ size 1)))))

    ; add-at-index : exact-integer? exact-integer? -> void?
    (define/public (add-at-index index val)
      (cond
        [(> index size) (void)]
        [(<= index 0) (add-at-head val)]
        [(= index size) (add-at-tail val)]
        [else
         (let loop ((prev head) (i (- index 1)))
           (if (= i 0)
               (let ([new-node (node val #f)])
                 (set-node-next! new-node (node-next prev))
                 (set-node-next! prev new-node)
                 (set! size (+ size 1)))
               (loop (node-next prev) (- i 1))))]))

    ; delete-at-index : exact-integer? -> void?
    (define/public (delete-at-index index)
      (when (and (>= index 0) (< index size))
        (cond
          [(= index 0)
           (set! head (node-next head))
           (when (= size 1) (set! tail #f))]
          [else
           (let loop ((prev head) (i (- index 1)))
             (if (= i 0)
                 (let ([to-delete (node-next prev)])
                   (set-node-next! prev (node-next to-delete))
                   (when (= index (- size 1)) ; deleting tail
                     (set! tail prev)))
                 (loop (node-next prev) (- i 1))))])
        (set! size (- size 1))))
    ))
```

## Erlang

```erlang
-module(my_linked_list).
-export([my_linked_list_init_/0,
         my_linked_list_get/1,
         my_linked_list_add_at_head/1,
         my_linked_list_add_at_tail/1,
         my_linked_list_add_at_index/2,
         my_linked_list_delete_at_index/1]).

-define(TABLE, my_ll_table).

%% Initialization
my_linked_list_init_() ->
    ets:new(?TABLE, [named_table, public, set]),
    ets:insert(?TABLE, [{list_head, undefined},
                        {list_size, 0},
                        {counter, 1}]),
    ok.

%% Get value at index
my_linked_list_get(Index) when is_integer(Index) ->
    Size = get_size(),
    if Index < 0 orelse Index >= Size ->
            -1;
       true ->
            Head = get_head(),
            get_val_at(Head, Index)
    end.

get_val_at(undefined, _) -> -1;
get_val_at(NodeId, 0) ->
    case ets:lookup(?TABLE, NodeId) of
        [{NodeId, Val, _}] -> Val;
        [] -> -1
    end;
get_val_at(NodeId, N) when N > 0 ->
    case ets:lookup(?TABLE, NodeId) of
        [{NodeId, _, Next}] -> get_val_at(Next, N-1);
        [] -> -1
    end.

%% Add at head
my_linked_list_add_at_head(Val) when is_integer(Val) ->
    Head = get_head(),
    Id = new_id(),
    ets:insert(?TABLE, {Id, Val, Head}),
    set_head(Id),
    inc_size(),
    ok.

%% Add at tail
my_linked_list_add_at_tail(Val) when is_integer(Val) ->
    Size = get_size(),
    case Size of
        0 -> my_linked_list_add_at_head(Val);
        _ ->
            Head = get_head(),
            TailId = find_tail(Head),
            Id = new_id(),
            ets:insert(?TABLE, {Id, Val, undefined}),
            ets:update_element(?TABLE, TailId, {3, Id}),
            inc_size(),
            ok
    end.

find_tail(NodeId) ->
    case ets:lookup(?TABLE, NodeId) of
        [{NodeId, _, undefined}] -> NodeId;
        [{NodeId, _, Next}] -> find_tail(Next)
    end.

%% Add at index
my_linked_list_add_at_index(Index, Val) when is_integer(Index), is_integer(Val) ->
    Size = get_size(),
    Cond = 
        if Index > Size -> ignore;
           Index =< 0 -> my_linked_list_add_at_head(Val);
           Index == Size -> my_linked_list_add_at_tail(Val);
           true -> insert_middle(Index, Val)
        end,
    case Cond of
        ignore -> ok;
        _ -> ok
    end.

insert_middle(Index, Val) ->
    PrevId = node_at_index(Index - 1),
    [{PrevId, _, Next}] = ets:lookup(?TABLE, PrevId),
    Id = new_id(),
    ets:insert(?TABLE, {Id, Val, Next}),
    ets:update_element(?TABLE, PrevId, {3, Id}),
    inc_size().

%% Delete at index
my_linked_list_delete_at_index(Index) when is_integer(Index) ->
    Size = get_size(),
    if Index < 0 orelse Index >= Size ->
            ok;
       Index == 0 ->
            Head = get_head(),
            case ets:lookup(?TABLE, Head) of
                [{Head, _, Next}] ->
                    set_head(Next),
                    ets:delete(?TABLE, Head),
                    dec_size(),
                    ok
            end;
       true ->
            PrevId = node_at_index(Index - 1),
            [{PrevId, _, TargetId}] = ets:lookup(?TABLE, PrevId),
            case ets:lookup(?TABLE, TargetId) of
                [{TargetId, _, NextId}] ->
                    ets:update_element(?TABLE, PrevId, {3, NextId}),
                    ets:delete(?TABLE, TargetId),
                    dec_size(),
                    ok
            end
    end.

%% Helper functions
get_head() ->
    case ets:lookup(?TABLE, list_head) of
        [{list_head, H}] -> H
    end.

set_head(H) ->
    ets:insert(?TABLE, {list_head, H}).

get_size() ->
    case ets:lookup(?TABLE, list_size) of
        [{list_size, S}] -> S
    end.

inc_size() ->
    Size = get_size(),
    ets:insert(?TABLE, {list_size, Size + 1}).

dec_size() ->
    Size = get_size(),
    ets:insert(?TABLE, {list_size, Size - 1}).

new_id() ->
    [{counter, Id}] = ets:lookup(?TABLE, counter),
    ets:insert(?TABLE, {counter, Id + 1}),
    Id.

node_at_index(Index) when Index >= 0 ->
    Head = get_head(),
    node_at_index(Head, Index).

node_at_index(undefined, _) -> undefined;
node_at_index(NodeId, 0) -> NodeId;
node_at_index(NodeId, N) when N > 0 ->
    [{NodeId, _, Next}] = ets:lookup(?TABLE, NodeId),
    node_at_index(Next, N - 1).
```

## Elixir

```elixir
defmodule MyLinkedList do
  @spec init_() :: any
  def init_() do
    case Process.whereis(__MODULE__) do
      nil -> :ok
      pid -> Agent.stop(pid)
    end

    {:ok, _pid} = Agent.start_link(fn -> %{head: nil, size: 0} end, name: __MODULE__)
    nil
  end

  @spec get(index :: integer) :: integer
  def get(index) do
    Agent.get(__MODULE__, fn state ->
      if index < 0 or index >= state.size do
        -1
      else
        traverse(state.head, index)
      end
    end)
  end

  @spec add_at_head(val :: integer) :: any
  def add_at_head(val) do
    Agent.update(__MODULE__, fn state ->
      new_node = %{val: val, next: state.head}
      %{head: new_node, size: state.size + 1}
    end)

    nil
  end

  @spec add_at_tail(val :: integer) :: any
  def add_at_tail(val) do
    Agent.update(__MODULE__, fn state ->
      cond do
        state.head == nil ->
          %{head: %{val: val, next: nil}, size: 1}

        true ->
          new_head = append_tail(state.head, val)
          %{head: new_head, size: state.size + 1}
      end
    end)

    nil
  end

  @spec add_at_index(index :: integer, val :: integer) :: any
  def add_at_index(index, val) do
    Agent.update(__MODULE__, fn state ->
      cond do
        index <= 0 ->
          %{head: %{val: val, next: state.head}, size: state.size + 1}

        index == state.size ->
          new_head =
            if state.head == nil do
              %{val: val, next: nil}
            else
              append_tail(state.head, val)
            end

          %{head: new_head, size: state.size + 1}

        index > state.size ->
          state

        true ->
          new_head = insert_at(state.head, index, val)
          %{head: new_head, size: state.size + 1}
      end
    end)

    nil
  end

  @spec delete_at_index(index :: integer) :: any
  def delete_at_index(index) do
    Agent.update(__MODULE__, fn state ->
      cond do
        index < 0 or index >= state.size ->
          state

        index == 0 ->
          %{head: (state.head && state.head.next), size: state.size - 1}

        true ->
          new_head = delete_at(state.head, index)
          %{head: new_head, size: state.size - 1}
      end
    end)

    nil
  end

  # Helper functions

  defp traverse(nil, _), do: -1
  defp traverse(%{val: v}, 0), do: v
  defp traverse(%{next: nxt}, i) when i > 0, do: traverse(nxt, i - 1)

  defp append_tail(%{next: nil} = node, val) do
    %{node | next: %{val: val, next: nil}}
  end

  defp append_tail(%{next: nxt} = node, val) do
    %{node | next: append_tail(nxt, val)}
  end

  defp insert_at(node, 0, val) do
    %{val: val, next: node}
  end

  defp insert_at(%{next: nxt} = node, idx, val) when idx > 0 do
    %{node | next: insert_at(nxt, idx - 1, val)}
  end

  defp delete_at(%{next: nxt}, 1) do
    %{next: (nxt && nxt.next)}
  end

  defp delete_at(%{next: nxt} = node, idx) when idx > 1 do
    %{node | next: delete_at(nxt, idx - 1)}
  end
end
```
