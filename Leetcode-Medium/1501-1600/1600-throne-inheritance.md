# 1600. Throne Inheritance

## Cpp

```cpp
class ThroneInheritance {
public:
    struct Node {
        string name;
        vector<Node*> children;
        bool alive = true;
        Node(const string& n) : name(n) {}
    };
    
    ThroneInheritance(string kingName) {
        root = new Node(kingName);
        nodes[kingName] = root;
    }
    
    void birth(string parentName, string childName) {
        Node* parent = nodes[parentName];
        Node* child = new Node(childName);
        parent->children.push_back(child);
        nodes[childName] = child;
    }
    
    void death(string name) {
        Node* node = nodes[name];
        if (node) node->alive = false;
    }
    
    vector<string> getInheritanceOrder() {
        vector<string> order;
        // iterative preorder traversal
        vector<pair<Node*, size_t>> stack;
        stack.emplace_back(root, 0);
        while (!stack.empty()) {
            Node* cur = stack.back().first;
            size_t idx = stack.back().second;
            if (idx == 0) { // first time we see this node
                if (cur->alive) order.push_back(cur->name);
            }
            if (idx < cur->children.size()) {
                // go to next child
                Node* child = cur->children[idx];
                ++stack.back().second; // increment index for current node
                stack.emplace_back(child, 0);
            } else {
                stack.pop_back();
            }
        }
        return order;
    }
    
private:
    Node* root;
    unordered_map<string, Node*> nodes;
};

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance* obj = new ThroneInheritance(kingName);
 * obj->birth(parentName,childName);
 * obj->death(name);
 * vector<string> param_3 = obj->getInheritanceOrder();
 */
```

## Java

```java
import java.util.*;

class ThroneInheritance {
    private final String king;
    private final Map<String, List<String>> children = new HashMap<>();
    private final Set<String> dead = new HashSet<>();

    public ThroneInheritance(String kingName) {
        this.king = kingName;
        children.put(kingName, new ArrayList<>());
    }

    public void birth(String parentName, String childName) {
        children.computeIfAbsent(parentName, k -> new ArrayList<>()).add(childName);
        children.put(childName, new ArrayList<>());
    }

    public void death(String name) {
        dead.add(name);
    }

    public List<String> getInheritanceOrder() {
        List<String> order = new ArrayList<>();
        dfs(king, order);
        return order;
    }

    private void dfs(String cur, List<String> order) {
        if (!dead.contains(cur)) {
            order.add(cur);
        }
        List<String> childs = children.get(cur);
        if (childs != null) {
            for (String child : childs) {
                dfs(child, order);
            }
        }
    }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance obj = new ThroneInheritance(kingName);
 * obj.birth(parentName,childName);
 * obj.death(name);
 * List<String> param_3 = obj.getInheritanceOrder();
 */
```

## Python

```python
class ThroneInheritance(object):
    def __init__(self, kingName):
        """
        :type kingName: str
        """
        self.king = kingName
        self.children = {kingName: []}
        self.dead = set()

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        if parentName not in self.children:
            self.children[parentName] = []
        self.children[parentName].append(childName)
        self.children[childName] = []

    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        self.dead.add(name)

    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        """
        order = []
        stack = [self.king]
        while stack:
            person = stack.pop()
            if person not in self.dead:
                order.append(person)
            for child in reversed(self.children.get(person, [])):
                stack.append(child)
        return order
```

## Python3

```python
from typing import List, Dict
from collections import defaultdict

class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = kingName
        self.children: Dict[str, List[str]] = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order: List[str] = []
        stack = [self.king]
        while stack:
            node = stack.pop()
            if node not in self.dead:
                order.append(node)
            # push children in reverse to preserve birth order
            for child in reversed(self.children.get(node, [])):
                stack.append(child)
        return order
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct Node {
    char *name;
    bool alive;
    struct Node **children;
    int childCount;
    int childCap;
    struct Node *parent;
} Node;

typedef struct Entry {
    char *key;
    Node *node;
    struct Entry *next;
} Entry;

struct ThroneInheritance {
    Node *king;
    Entry **table;
    int size;          // hash bucket count
    int nodeCount;     // total nodes created
};

/* ---------- utility functions ---------- */
static unsigned long hash_str(const char *s) {
    unsigned long h = 5381;
    int c;
    while ((c = (unsigned char)*s++))
        h = ((h << 5) + h) + c; /* h * 33 + c */
    return h;
}

static char *strDup(const char *s) {
    size_t len = strlen(s) + 1;
    char *p = (char *)malloc(len);
    if (p) memcpy(p, s, len);
    return p;
}

/* ---------- hashmap operations ---------- */
static Node *findNode(ThroneInheritance *obj, const char *name) {
    unsigned long idx = hash_str(name) % obj->size;
    Entry *e = obj->table[idx];
    while (e) {
        if (strcmp(e->key, name) == 0)
            return e->node;
        e = e->next;
    }
    return NULL;
}

static void insertNode(ThroneInheritance *obj, Node *node) {
    unsigned long idx = hash_str(node->name) % obj->size;
    Entry *e = (Entry *)malloc(sizeof(Entry));
    e->key = node->name;
    e->node = node;
    e->next = obj->table[idx];
    obj->table[idx] = e;
}

/* ---------- API implementation ---------- */
ThroneInheritance* throneInheritanceCreate(char* kingName) {
    ThroneInheritance *obj = (ThroneInheritance *)malloc(sizeof(ThroneInheritance));
    obj->size = 131071; // a prime > 1e5
    obj->table = (Entry **)calloc(obj->size, sizeof(Entry *));
    obj->nodeCount = 0;

    Node *king = (Node *)malloc(sizeof(Node));
    king->name = strDup(kingName);
    king->alive = true;
    king->children = NULL;
    king->childCount = 0;
    king->childCap = 0;
    king->parent = NULL;

    obj->king = king;
    insertNode(obj, king);
    obj->nodeCount = 1;
    return obj;
}

void throneInheritanceBirth(ThroneInheritance* obj, char* parentName, char* childName) {
    Node *parent = findNode(obj, parentName);
    if (!parent) return; // should not happen per constraints

    Node *child = (Node *)malloc(sizeof(Node));
    child->name = strDup(childName);
    child->alive = true;
    child->children = NULL;
    child->childCount = 0;
    child->childCap = 0;
    child->parent = parent;

    if (parent->childCap == 0) {
        parent->childCap = 2;
        parent->children = (Node **)malloc(sizeof(Node *) * parent->childCap);
    } else if (parent->childCount == parent->childCap) {
        parent->childCap <<= 1;
        parent->children = (Node **)realloc(parent->children, sizeof(Node *) * parent->childCap);
    }
    parent->children[parent->childCount++] = child;

    insertNode(obj, child);
    obj->nodeCount++;
}

void throneInheritanceDeath(ThroneInheritance* obj, char* name) {
    Node *node = findNode(obj, name);
    if (node) node->alive = false;
}

char** throneInheritanceGetInheritanceOrder(ThroneInheritance* obj, int* retSize) {
    char **order = (char **)malloc(sizeof(char *) * obj->nodeCount);
    int idx = 0;

    Node **stack = (Node **)malloc(sizeof(Node *) * obj->nodeCount);
    int top = 0;
    stack[top++] = obj->king;

    while (top) {
        Node *cur = stack[--top];
        if (cur->alive) order[idx++] = cur->name;
        for (int i = cur->childCount - 1; i >= 0; --i)
            stack[top++] = cur->children[i];
    }

    free(stack);
    *retSize = idx;
    return order;
}

void throneInheritanceFree(ThroneInheritance* obj) {
    // Free all nodes via hashmap entries
    for (int i = 0; i < obj->size; ++i) {
        Entry *e = obj->table[i];
        while (e) {
            Entry *next = e->next;
            Node *node = e->node;
            if (node->children) free(node->children);
            free(node->name);
            free(node);
            free(e);
            e = next;
        }
    }
    free(obj->table);
    free(obj);
}

/* The struct and functions are ready for LeetCode usage. */
```

## Csharp

```csharp
public class ThroneInheritance
{
    private class Node
    {
        public string Name;
        public bool Alive = true;
        public readonly List<Node> Children = new List<Node>();
        public Node(string name) => Name = name;
    }

    private readonly Node _king;
    private readonly Dictionary<string, Node> _nodes = new Dictionary<string, Node>();

    public ThroneInheritance(string kingName)
    {
        _king = new Node(kingName);
        _nodes[kingName] = _king;
    }

    public void Birth(string parentName, string childName)
    {
        var parentNode = _nodes[parentName];
        var childNode = new Node(childName);
        parentNode.Children.Add(childNode);
        _nodes[childName] = childNode;
    }

    public void Death(string name)
    {
        if (_nodes.TryGetValue(name, out var node))
            node.Alive = false;
    }

    public IList<string> GetInheritanceOrder()
    {
        var order = new List<string>();
        DFS(_king, order);
        return order;
    }

    private void DFS(Node node, List<string> order)
    {
        if (node.Alive)
            order.Add(node.Name);
        foreach (var child in node.Children)
            DFS(child, order);
    }
}
```

## Javascript

```javascript
var ThroneInheritance = function(kingName) {
    this.king = kingName;
    this.children = new Map();
    this.children.set(kingName, []);
    this.dead = new Set();
};

ThroneInheritance.prototype.birth = function(parentName, childName) {
    if (!this.children.has(parentName)) {
        this.children.set(parentName, []);
    }
    this.children.get(parentName).push(childName);
    this.children.set(childName, []);
};

ThroneInheritance.prototype.death = function(name) {
    this.dead.add(name);
};

ThroneInheritance.prototype.getInheritanceOrder = function() {
    const order = [];
    const dfs = (name) => {
        if (!this.dead.has(name)) order.push(name);
        const childs = this.children.get(name) || [];
        for (const child of childs) {
            dfs(child);
        }
    };
    dfs(this.king);
    return order;
};
```

## Typescript

```typescript
class ThroneInheritance {
    private king: string;
    private children: Map<string, string[]>;
    private dead: Set<string>;

    constructor(kingName: string) {
        this.king = kingName;
        this.children = new Map();
        this.dead = new Set();
        this.children.set(kingName, []);
    }

    birth(parentName: string, childName: string): void {
        if (!this.children.has(parentName)) {
            this.children.set(parentName, []);
        }
        this.children.get(parentName)!.push(childName);
        this.children.set(childName, []);
    }

    death(name: string): void {
        this.dead.add(name);
    }

    getInheritanceOrder(): string[] {
        const order: string[] = [];
        const stack: string[] = [this.king];
        while (stack.length) {
            const cur = stack.pop()!;
            if (!this.dead.has(cur)) {
                order.push(cur);
            }
            const childs = this.children.get(cur);
            if (childs) {
                for (let i = childs.length - 1; i >= 0; i--) {
                    stack.push(childs[i]);
                }
            }
        }
        return order;
    }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * var obj = new ThroneInheritance(kingName)
 * obj.birth(parentName,childName)
 * obj.death(name)
 * var param_3 = obj.getInheritanceOrder()
 */
```

## Php

```php
class ThroneInheritance {
    private string $king;
    /** @var array<string, array> */
    private array $children = [];
    /** @var array<string, bool> */
    private array $dead = [];

    /**
     * @param String $kingName
     */
    function __construct($kingName) {
        $this->king = $kingName;
        $this->children[$kingName] = [];
    }

    /**
     * @param String $parentName
     * @param String $childName
     * @return NULL
     */
    function birth($parentName, $childName) {
        if (!isset($this->children[$parentName])) {
            $this->children[$parentName] = [];
        }
        $this->children[$parentName][] = $childName;
        $this->children[$childName] = []; // initialize child's list
    }

    /**
     * @param String $name
     * @return NULL
     */
    function death($name) {
        $this->dead[$name] = true;
    }

    /**
     * @return String[]
     */
    function getInheritanceOrder() {
        $order = [];
        $stack = [$this->king];
        while (!empty($stack)) {
            $node = array_pop($stack);
            if (!isset($this->dead[$node])) {
                $order[] = $node;
            }
            if (isset($this->children[$node])) {
                $childList = $this->children[$node];
                for ($i = count($childList) - 1; $i >= 0; $i--) {
                    $stack[] = $childList[$i];
                }
            }
        }
        return $order;
    }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * $obj = new ThroneInheritance($kingName);
 * $obj->birth($parentName, $childName);
 * $obj->death($name);
 * $ret_3 = $obj->getInheritanceOrder();
 */
```

## Swift

```swift
class ThroneInheritance {
    private class Person {
        let name: String
        var children: [Person] = []
        var alive: Bool = true
        init(_ name: String) { self.name = name }
    }
    
    private let king: Person
    private var dict: [String: Person] = [:]
    
    init(_ kingName: String) {
        let k = Person(kingName)
        self.king = k
        dict[kingName] = k
    }
    
    func birth(_ parentName: String, _ childName: String) {
        guard let parent = dict[parentName] else { return }
        let child = Person(childName)
        parent.children.append(child)
        dict[childName] = child
    }
    
    func death(_ name: String) {
        dict[name]?.alive = false
    }
    
    func getInheritanceOrder() -> [String] {
        var order: [String] = []
        var stack: [Person] = [king]
        while let node = stack.popLast() {
            if node.alive { order.append(node.name) }
            for child in node.children.reversed() {
                stack.append(child)
            }
        }
        return order
    }
}
```

## Kotlin

```kotlin
class ThroneInheritance(kingName: String) {
    private class Node(val name: String) {
        val children = mutableListOf<Node>()
        var alive = true
    }

    private val nodes = HashMap<String, Node>()
    private val king: Node

    init {
        king = Node(kingName)
        nodes[kingName] = king
    }

    fun birth(parentName: String, childName: String) {
        val parent = nodes[parentName]!!
        val child = Node(childName)
        parent.children.add(child)
        nodes[childName] = child
    }

    fun death(name: String) {
        nodes[name]?.alive = false
    }

    fun getInheritanceOrder(): List<String> {
        val order = mutableListOf<String>()
        fun dfs(node: Node) {
            if (node.alive) order.add(node.name)
            for (child in node.children) dfs(child)
        }
        dfs(king)
        return order
    }
}
```

## Dart

```dart
class _Node {
  String name;
  bool alive = true;
  List<_Node> children = [];

  _Node(this.name);
}

class ThroneInheritance {
  final Map<String, _Node> _nodes = {};
  late final _Node _king;

  ThroneInheritance(String kingName) {
    _king = _Node(kingName);
    _nodes[kingName] = _king;
  }

  void birth(String parentName, String childName) {
    final parent = _nodes[parentName]!;
    final child = _Node(childName);
    parent.children.add(child);
    _nodes[childName] = child;
  }

  void death(String name) {
    final node = _nodes[name]!;
    node.alive = false;
  }

  List<String> getInheritanceOrder() {
    final List<String> order = [];
    final List<_Node> stack = [_king];
    while (stack.isNotEmpty) {
      final node = stack.removeLast();
      if (node.alive) order.add(node.name);
      for (int i = node.children.length - 1; i >= 0; --i) {
        stack.add(node.children[i]);
      }
    }
    return order;
  }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance obj = ThroneInheritance(kingName);
 * obj.birth(parentName,childName);
 * obj.death(name);
 * List<String> param3 = obj.getInheritanceOrder();
 */
```

## Golang

```go
type Node struct {
	name     string
	children []*Node
	alive    bool
}

type ThroneInheritance struct {
	king  *Node
	nodes map[string]*Node
}

/**
 * @param kingName: The name of the king.
 * @return: nothing
 */
func Constructor(kingName string) ThroneInheritance {
	king := &Node{name: kingName, alive: true}
	m := make(map[string]*Node)
	m[kingName] = king
	return ThroneInheritance{
		king:  king,
		nodes: m,
	}
}

/**
 * @param parentName: name of the parent.
 * @param childName: name of the child.
 * @return: nothing
 */
func (this *ThroneInheritance) Birth(parentName string, childName string) {
	parent := this.nodes[parentName]
	child := &Node{name: childName, alive: true}
	parent.children = append(parent.children, child)
	this.nodes[childName] = child
}

/**
 * @param name: name of the person who dies.
 * @return: nothing
 */
func (this *ThroneInheritance) Death(name string) {
	if node, ok := this.nodes[name]; ok {
		node.alive = false
	}
}

/**
 * @return: return the current order of inheritance.
 */
func (this *ThroneInheritance) GetInheritanceOrder() []string {
	var order []string
	var dfs func(*Node)
	dfs = func(node *Node) {
		if node.alive {
			order = append(order, node.name)
		}
		for _, child := range node.children {
			dfs(child)
		}
	}
	dfs(this.king)
	return order
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * obj := Constructor(kingName);
 * obj.Birth(parentName,childName);
 * obj.Death(name);
 * param_3 := obj.GetInheritanceOrder();
 */
```

## Ruby

```ruby
require 'set'

class ThroneInheritance
  # :type king_name: String
  def initialize(king_name)
    @king = king_name
    @children = Hash.new { |h, k| h[k] = [] }
    @dead = Set.new
  end

  # :type parent_name: String
  # :type child_name: String
  # :rtype: Void
  def birth(parent_name, child_name)
    @children[parent_name] << child_name
  end

  # :type name: String
  # :rtype: Void
  def death(name)
    @dead.add(name)
  end

  # :rtype: String[]
  def get_inheritance_order()
    order = []
    stack = [@king]
    while !stack.empty?
      cur = stack.pop
      order << cur unless @dead.include?(cur)
      childs = @children[cur]
      (childs.length - 1).downto(0) { |i| stack << childs[i] }
    end
    order
  end
end
```

## Scala

```scala
class ThroneInheritance(_kingName: String) {
  private val king = _kingName
  private val children = scala.collection.mutable.Map[String, scala.collection.mutable.ListBuffer[String]]()
  private val dead = scala.collection.mutable.Set[String]()

  // initialize the king's entry
  children(king) = scala.collection.mutable.ListBuffer.empty

  def birth(parentName: String, childName: String): Unit = {
    val list = children.getOrElseUpdate(parentName, scala.collection.mutable.ListBuffer.empty)
    list += childName
    children(childName) = scala.collection.mutable.ListBuffer.empty
  }

  def death(name: String): Unit = {
    dead.add(name)
  }

  def getInheritanceOrder(): List[String] = {
    val order = scala.collection.mutable.ListBuffer[String]()
    def dfs(name: String): Unit = {
      if (!dead.contains(name)) order += name
      for (c <- children.getOrElse(name, scala.collection.mutable.ListBuffer.empty)) {
        dfs(c)
      }
    }
    dfs(king)
    order.toList
  }
}
```

## Rust

```rust
use std::collections::{HashMap, HashSet};

pub struct ThroneInheritance {
    king: String,
    children: HashMap<String, Vec<String>>,
    dead: HashSet<String>,
}

impl ThroneInheritance {
    pub fn new(kingName: String) -> Self {
        let mut children = HashMap::new();
        children.insert(kingName.clone(), Vec::new());
        ThroneInheritance {
            king: kingName,
            children,
            dead: HashSet::new(),
        }
    }

    pub fn birth(&mut self, parent_name: String, child_name: String) {
        self.children
            .entry(parent_name)
            .or_insert_with(Vec::new)
            .push(child_name.clone());
        // Ensure the child has an entry for future births.
        self.children.entry(child_name).or_insert_with(Vec::new);
    }

    pub fn death(&mut self, name: String) {
        self.dead.insert(name);
    }

    pub fn get_inheritance_order(&self) -> Vec<String> {
        let mut order = Vec::new();
        let mut stack = Vec::new();
        stack.push(self.king.clone());

        while let Some(name) = stack.pop() {
            if !self.dead.contains(&name) {
                order.push(name.clone());
            }
            if let Some(children) = self.children.get(&name) {
                for child in children.iter().rev() {
                    stack.push(child.clone());
                }
            }
        }

        order
    }
}

/*
Example usage:
let mut t = ThroneInheritance::new("king".to_string());
t.birth("king".to_string(), "andy".to_string());
t.birth("king".to_string(), "bob".to_string());
// ...
*/
```

## Racket

```racket
(define throne-inheritance%
  (class object%
    (init-field king-name)
    (super-new)

    ;; mutable node structure
    (struct node (children alive) #:mutable)

    ;; hash table: name -> node
    (define nodes (make-hash))

    ;; initialize the king
    (hash-set! nodes king-name (node '() #t))

    (define/public (birth parent-name child-name)
      (let ([parent-node (hash-ref nodes parent-name)])
        (set-node-children! parent-node
                            (append (node-children parent-node) (list child-name)))
        (hash-set! nodes child-name (node '() #t))))

    (define/public (death name)
      (let ([n (hash-ref nodes name)])
        (set-node-alive! n #f)))

    (define/public (get-inheritance-order)
      ;; depth‑first traversal building list in reverse order for efficiency
      (define (dfs name acc)
        (let* ([cur (hash-ref nodes name)]
               [acc1 (if (node-alive cur) (cons name acc) acc)])
          (for/fold ([a acc1]) ([child (in-list (reverse (node-children cur)))])
            (dfs child a))))
      (reverse (dfs king-name '())))))
```

## Erlang

```erlang
-spec throne_inheritance_init_(KingName :: unicode:unicode_binary()) -> any().
throne_inheritance_init_(KingName) ->
    put(king, KingName),
    put(children, #{KingName => []}),
    put(dead, sets:new()),
    ok.

-spec throne_inheritance_birth(ParentName :: unicode:unicode_binary(), ChildName :: unicode:unicode_binary()) -> any().
throne_inheritance_birth(ParentName, ChildName) ->
    ChildrenMap = get(children),
    ParentChildren = maps:get(ParentName, ChildrenMap, []),
    UpdatedParentChildren = ParentChildren ++ [ChildName],
    TempMap = maps:put(ParentName, UpdatedParentChildren, ChildrenMap),
    NewChildrenMap = maps:put(ChildName, [], TempMap),
    put(children, NewChildrenMap),
    ok.

-spec throne_inheritance_death(Name :: unicode:unicode_binary()) -> any().
throne_inheritance_death(Name) ->
    DeadSet = get(dead),
    NewDead = sets:add_element(Name, DeadSet),
    put(dead, NewDead),
    ok.

-spec throne_inheritance_get_inheritance_order() -> [unicode:unicode_binary()].
throne_inheritance_get_inheritance_order() ->
    King = get(king),
    ChildrenMap = get(children),
    DeadSet = get(dead),
    traverse(King, ChildrenMap, DeadSet).

traverse(Name, ChildrenMap, DeadSet) ->
    Prefix = case sets:is_element(Name, DeadSet) of
        true -> [];
        false -> [Name]
    end,
    ChildList = maps:get(Name, ChildrenMap, []),
    lists:foldl(fun(Child, Acc) -> Acc ++ traverse(Child, ChildrenMap, DeadSet) end,
                Prefix,
                ChildList).
```

## Elixir

```elixir
defmodule ThroneInheritance do
  @spec init_(king_name :: String.t) :: any
  def init_(king_name) do
    state = %{
      king: king_name,
      children: %{king_name => []},
      dead: MapSet.new()
    }

    Process.put(:throne_state, state)
  end

  @spec birth(parent_name :: String.t, child_name :: String.t) :: any
  def birth(parent_name, child_name) do
    state = Process.get(:throne_state)

    parent_children = Map.get(state.children, parent_name, [])
    updated_parent_children = parent_children ++ [child_name]

    new_children =
      state.children
      |> Map.put(parent_name, updated_parent_children)
      |> Map.put(child_name, [])

    new_state = %{state | children: new_children}
    Process.put(:throne_state, new_state)
  end

  @spec death(name :: String.t) :: any
  def death(name) do
    state = Process.get(:throne_state)

    new_dead = MapSet.put(state.dead, name)
    Process.put(:throne_state, %{state | dead: new_dead})
  end

  @spec get_inheritance_order() :: [String.t]
  def get_inheritance_order() do
    state = Process.get(:throne_state)
    preorder(state.king, state)
  end

  defp preorder(node, state) do
    children = Map.get(state.children, node, [])
    rest = Enum.flat_map(children, fn child -> preorder(child, state) end)

    if MapSet.member?(state.dead, node) do
      rest
    else
      [node | rest]
    end
  end
end
```
