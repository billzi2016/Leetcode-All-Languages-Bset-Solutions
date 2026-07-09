# 0677. Map Sum Pairs

## Cpp

```cpp
class MapSum {
    struct TrieNode {
        TrieNode* child[26];
        int score;
        TrieNode() : score(0) {
            memset(child, 0, sizeof(child));
        }
    };
    
    TrieNode* root;
    std::unordered_map<std::string, int> kv;
public:
    MapSum() {
        root = new TrieNode();
    }
    
    void insert(std::string key, int val) {
        int delta = val - kv[key];
        kv[key] = val;
        TrieNode* node = root;
        for (char c : key) {
            int idx = c - 'a';
            if (!node->child[idx]) node->child[idx] = new TrieNode();
            node = node->child[idx];
            node->score += delta;
        }
    }
    
    int sum(std::string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            int idx = c - 'a';
            if (!node->child[idx]) return 0;
            node = node->child[idx];
        }
        return node->score;
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */
```

## Java

```java
class MapSum {
    private static class TrieNode {
        int sum;
        TrieNode[] children = new TrieNode[26];
    }

    private final TrieNode root;
    private final java.util.Map<String, Integer> map;

    public MapSum() {
        root = new TrieNode();
        map = new java.util.HashMap<>();
    }

    public void insert(String key, int val) {
        int delta = val - map.getOrDefault(key, 0);
        if (delta == 0) return;
        map.put(key, val);
        TrieNode node = root;
        node.sum += delta; // update root sum as well
        for (char c : key.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) {
                node.children[idx] = new TrieNode();
            }
            node = node.children[idx];
            node.sum += delta;
        }
    }

    public int sum(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            int idx = c - 'a';
            if (node.children[idx] == null) return 0;
            node = node.children[idx];
        }
        return node.sum;
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
```

## Python

```python
class MapSum(object):
    class TrieNode:
        __slots__ = ('children', 'score')
        def __init__(self):
            self.children = {}
            self.score = 0

    def __init__(self):
        self.root = self.TrieNode()
        self.key_vals = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        delta = val - self.key_vals.get(key, 0)
        if delta == 0:
            return
        self.key_vals[key] = val
        node = self.root
        node.score += delta
        for ch in key:
            if ch not in node.children:
                node.children[ch] = self.TrieNode()
            node = node.children[ch]
            node.score += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.score
```

## Python3

```python
class MapSum:
    class TrieNode:
        __slots__ = ('children', 'score')
        def __init__(self):
            self.children = {}
            self.score = 0

    def __init__(self):
        self.root = self.TrieNode()
        self.key_vals = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.key_vals.get(key, 0)
        if delta == 0:
            self.key_vals[key] = val
            return
        self.key_vals[key] = val
        node = self.root
        for ch in key:
            if ch not in node.children:
                node.children[ch] = self.TrieNode()
            node = node.children[ch]
            node.score += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.score
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct TrieNode {
    struct TrieNode *child[26];
    int sum;   // total value of all keys with this prefix
    int val;   // value of the key that ends at this node (0 if none)
} TrieNode;

static TrieNode* newNode(void) {
    TrieNode *node = (TrieNode*)calloc(1, sizeof(TrieNode));
    return node;
}

typedef struct {
    TrieNode *root;
} MapSum;

MapSum* mapSumCreate() {
    MapSum *obj = (MapSum*)malloc(sizeof(MapSum));
    obj->root = newNode();
    return obj;
}

void mapSumInsert(MapSum* obj, char* key, int val) {
    if (!obj || !key) return;
    TrieNode *path[55];
    int depth = 0;
    path[depth++] = obj->root;

    TrieNode *cur = obj->root;
    for (int i = 0; key[i]; ++i) {
        int idx = key[i] - 'a';
        if (!cur->child[idx]) cur->child[idx] = newNode();
        cur = cur->child[idx];
        path[depth++] = cur;
    }

    int oldVal = cur->val;
    int delta = val - oldVal;

    for (int i = 0; i < depth; ++i) {
        path[i]->sum += delta;
    }
    cur->val = val;
}

int mapSumSum(MapSum* obj, char* prefix) {
    if (!obj || !prefix) return 0;
    TrieNode *cur = obj->root;
    for (int i = 0; prefix[i]; ++i) {
        int idx = prefix[i] - 'a';
        if (!cur->child[idx]) return 0;
        cur = cur->child[idx];
    }
    return cur->sum;
}

static void freeNode(TrieNode *node) {
    if (!node) return;
    for (int i = 0; i < 26; ++i) {
        if (node->child[i]) freeNode(node->child[i]);
    }
    free(node);
}

void mapSumFree(MapSum* obj) {
    if (!obj) return;
    freeNode(obj->root);
    free(obj);
}

/**
 * Your MapSum struct will be instantiated and called as such:
 * MapSum* obj = mapSumCreate();
 * mapSumInsert(obj, key, val);
 *
 * int param_2 = mapSumSum(obj, prefix);
 *
 * mapSumFree(obj);
 */
```

## Csharp

```csharp
public class MapSum
{
    private class TrieNode
    {
        public int Score;
        public readonly Dictionary<char, TrieNode> Children = new Dictionary<char, TrieNode>();
    }

    private readonly TrieNode _root = new TrieNode();
    private readonly Dictionary<string, int> _map = new Dictionary<string, int>();

    public MapSum()
    {
    }

    public void Insert(string key, int val)
    {
        int delta = val;
        if (_map.TryGetValue(key, out int oldVal))
        {
            delta -= oldVal;
        }
        _map[key] = val;

        TrieNode node = _root;
        foreach (char c in key)
        {
            if (!node.Children.TryGetValue(c, out TrieNode child))
            {
                child = new TrieNode();
                node.Children[c] = child;
            }
            node = child;
            node.Score += delta;
        }
    }

    public int Sum(string prefix)
    {
        TrieNode node = _root;
        foreach (char c in prefix)
        {
            if (!node.Children.TryGetValue(c, out node))
                return 0;
        }
        return node.Score;
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.Insert(key,val);
 * int param_2 = obj.Sum(prefix);
 */
```

## Javascript

```javascript
var MapSum = function() {
    this.root = { children: {}, sum: 0 };
    this.map = {};
};

MapSum.prototype.insert = function(key, val) {
    const delta = val - (this.map[key] || 0);
    this.map[key] = val;
    let node = this.root;
    node.sum += delta;
    for (let i = 0; i < key.length; i++) {
        const ch = key[i];
        if (!node.children[ch]) {
            node.children[ch] = { children: {}, sum: 0 };
        }
        node = node.children[ch];
        node.sum += delta;
    }
};

MapSum.prototype.sum = function(prefix) {
    let node = this.root;
    for (let i = 0; i < prefix.length; i++) {
        const ch = prefix[i];
        if (!node.children[ch]) return 0;
        node = node.children[ch];
    }
    return node.sum;
};
```

## Typescript

```typescript
class TrieNode {
    children: Map<string, TrieNode>;
    sum: number;
    constructor() {
        this.children = new Map();
        this.sum = 0;
    }
}

class MapSum {
    private root: TrieNode;
    private keyMap: Map<string, number>;

    constructor() {
        this.root = new TrieNode();
        this.keyMap = new Map();
    }

    insert(key: string, val: number): void {
        const oldVal = this.keyMap.get(key) ?? 0;
        const delta = val - oldVal;
        if (delta === 0) return; // no change needed
        this.keyMap.set(key, val);
        let node = this.root;
        node.sum += delta;
        for (const ch of key) {
            if (!node.children.has(ch)) {
                node.children.set(ch, new TrieNode());
            }
            node = node.children.get(ch)!;
            node.sum += delta;
        }
    }

    sum(prefix: string): number {
        let node = this.root;
        for (const ch of prefix) {
            if (!node.children.has(ch)) return 0;
            node = node.children.get(ch)!;
        }
        return node.sum;
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * var obj = new MapSum()
 * obj.insert(key,val)
 * var param_2 = obj.sum(prefix)
 */
```

## Php

```php
class MapSum {
    private $root;
    private $map;

    function __construct() {
        $this->root = ['sum' => 0, 'next' => []];
        $this->map = [];
    }

    /**
     * @param String $key
     * @param Integer $val
     * @return NULL
     */
    function insert($key, $val) {
        $delta = $val - ($this->map[$key] ?? 0);
        $this->map[$key] = $val;

        $node =& $this->root;
        $node['sum'] += $delta;

        $len = strlen($key);
        for ($i = 0; $i < $len; $i++) {
            $c = $key[$i];
            if (!isset($node['next'][$c])) {
                $node['next'][$c] = ['sum' => 0, 'next' => []];
            }
            $node =& $node['next'][$c];
            $node['sum'] += $delta;
        }
    }

    /**
     * @param String $prefix
     * @return Integer
     */
    function sum($prefix) {
        $node =& $this->root;
        $len = strlen($prefix);
        for ($i = 0; $i < $len; $i++) {
            $c = $prefix[$i];
            if (!isset($node['next'][$c])) {
                return 0;
            }
            $node =& $node['next'][$c];
        }
        return $node['sum'];
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * $obj = new MapSum();
 * $obj->insert($key, $val);
 * $ret_2 = $obj->sum($prefix);
 */
```

## Swift

```swift
class MapSum {
    private var keyValues: [String: Int] = [:]
    private var prefixSums: [String: Int] = [:]

    init() { }

    func insert(_ key: String, _ val: Int) {
        let oldVal = keyValues[key] ?? 0
        let delta = val - oldVal
        if delta != 0 {
            var prefix = ""
            for ch in key {
                prefix.append(ch)
                prefixSums[prefix, default: 0] += delta
            }
        }
        keyValues[key] = val
    }

    func sum(_ prefix: String) -> Int {
        return prefixSums[prefix] ?? 0
    }
}
```

## Kotlin

```kotlin
class MapSum() {

    private data class TrieNode(var sum: Int = 0, val children: MutableMap<Char, TrieNode> = HashMap())

    private val root = TrieNode()
    private val map = HashMap<String, Int>()

    fun insert(key: String, `val`: Int) {
        val delta = `val` - (map[key] ?: 0)
        if (delta == 0) {
            map[key] = `val`
            return
        }
        map[key] = `val`
        var node = root
        node.sum += delta
        for (c in key) {
            node = node.children.getOrPut(c) { TrieNode() }
            node.sum += delta
        }
    }

    fun sum(prefix: String): Int {
        var node = root
        for (c in prefix) {
            val next = node.children[c] ?: return 0
            node = next
        }
        return node.sum
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * var obj = MapSum()
 * obj.insert(key,`val`)
 * var param_2 = obj.sum(prefix)
 */
```

## Dart

```dart
class TrieNode {
  List<TrieNode?> children = List.filled(26, null);
  int score = 0;
}

class MapSum {
  final TrieNode _root = TrieNode();
  final Map<String, int> _map = {};

  MapSum();

  void insert(String key, int val) {
    int delta = val - (_map[key] ?? 0);
    if (delta == 0) return;
    _map[key] = val;
    TrieNode node = _root;
    for (int i = 0; i < key.length; i++) {
      int idx = key.codeUnitAt(i) - 97;
      node.children[idx] ??= TrieNode();
      node = node.children[idx]!;
      node.score += delta;
    }
  }

  int sum(String prefix) {
    TrieNode? node = _root;
    for (int i = 0; i < prefix.length; i++) {
      int idx = prefix.codeUnitAt(i) - 97;
      node = node?.children[idx];
      if (node == null) return 0;
    }
    return node.score;
  }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = MapSum();
 * obj.insert(key,val);
 * int param2 = obj.sum(prefix);
 */
```

## Golang

```go
type Node struct {
	child [26]*Node
	score int
}

type MapSum struct {
	root *Node
	kv   map[string]int
}

/** Initialize your data structure here. */
func Constructor() MapSum {
	return MapSum{
		root: &Node{},
		kv:   make(map[string]int),
	}
}

func (this *MapSum) Insert(key string, val int) {
	prev := this.kv[key]
	delta := val - prev
	if delta == 0 && prev != 0 {
		this.kv[key] = val
		return
	}
	this.kv[key] = val
	node := this.root
	for _, ch := range key {
		idx := ch - 'a'
		if node.child[idx] == nil {
			node.child[idx] = &Node{}
		}
		node = node.child[idx]
		node.score += delta
	}
}

func (this *MapSum) Sum(prefix string) int {
	node := this.root
	for _, ch := range prefix {
		idx := ch - 'a'
		if node.child[idx] == nil {
			return 0
		}
		node = node.child[idx]
	}
	return node.score
}

/**
 * Your MapSum object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(key,val);
 * param_2 := obj.Sum(prefix);
 */
```

## Ruby

```ruby
class TrieNode
  attr_accessor :children, :score
  def initialize
    @children = {}
    @score = 0
  end
end

class MapSum
  def initialize()
    @root = TrieNode.new
    @map = {}
  end

=begin
    :type key: String
    :type val: Integer
    :rtype: Void
=end
  def insert(key, val)
    delta = val - (@map[key] || 0)
    @map[key] = val
    node = @root
    node.score += delta
    key.each_char do |ch|
      node.children[ch] ||= TrieNode.new
      node = node.children[ch]
      node.score += delta
    end
  end

=begin
    :type prefix: String
    :rtype: Integer
=end
  def sum(prefix)
    node = @root
    prefix.each_char do |ch|
      return 0 unless node.children.key?(ch)
      node = node.children[ch]
    end
    node.score
  end
end
```

## Scala

```scala
class MapSum() {

  private class Node {
    var sum: Int = 0
    val children: Array[Node] = new Array[Node](26)
  }

  private val root = new Node()
  private val map = scala.collection.mutable.Map[String, Int]()

  def insert(key: String, `val`: Int): Unit = {
    val delta = `val` - map.getOrElse(key, 0)
    if (delta == 0) {
      map.update(key, `val`)
      return
    }
    map.update(key, `val`)
    var node = root
    for (c <- key) {
      val idx = c - 'a'
      if (node.children(idx) == null) node.children(idx) = new Node()
      node = node.children(idx)
      node.sum += delta
    }
  }

  def sum(prefix: String): Int = {
    var node = root
    for (c <- prefix) {
      val idx = c - 'a'
      if (node.children(idx) == null) return 0
      node = node.children(idx)
    }
    node.sum
  }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * val obj = new MapSum()
 * obj.insert(key,`val`)
 * val param_2 = obj.sum(prefix)
 */
```

## Rust

```rust
use std::cell::RefCell;
use std::collections::HashMap;

struct MapSum {
    map: RefCell<HashMap<String, i32>>,
    score: RefCell<HashMap<String, i32>>,
}

impl MapSum {
    fn new() -> Self {
        MapSum {
            map: RefCell::new(HashMap::new()),
            score: RefCell::new(HashMap::new()),
        }
    }

    fn insert(&self, key: String, val: i32) {
        let mut map_ref = self.map.borrow_mut();
        let prev = *map_ref.get(&key).unwrap_or(&0);
        let delta = val - prev;
        map_ref.insert(key.clone(), val);
        drop(map_ref); // release before borrowing score

        if delta == 0 {
            return;
        }

        let mut score_ref = self.score.borrow_mut();
        for i in 1..=key.len() {
            let prefix = &key[..i];
            *score_ref.entry(prefix.to_string()).or_insert(0) += delta;
        }
    }

    fn sum(&self, prefix: String) -> i32 {
        *self.score.borrow().get(&prefix).unwrap_or(&0)
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * let obj = MapSum::new();
 * obj.insert(key, val);
 * let ret_2: i32 = obj.sum(prefix);
 */
```

## Racket

```racket
(define map-sum%
  (class object%
    (super-new)
    (init-field)
    (field [key->val (make-hash)]
           [prefix-sum (make-hash)])
    
    ; insert : string? exact-integer? -> void?
    (define/public (insert key val)
      (let* ([old (hash-ref key->val key 0)]
             [delta (- val old)])
        (when (not (= delta 0))
          (hash-set! key->val key val)
          (for ([i (in-range 1 (add1 (string-length key)))])
            (define pref (substring key 0 i))
            (hash-set! prefix-sum
                       pref
                       (+ (hash-ref prefix-sum pref 0) delta))))))
    
    ; sum : string? -> exact-integer?
    (define/public (sum prefix)
      (hash-ref prefix-sum prefix 0))))
```

## Erlang

```erlang
-module(map_sum).
-export([map_sum_init_/0, map_sum_insert/2, map_sum_sum/1]).

-spec map_sum_init_() -> any().
map_sum_init_() ->
    put(ms_key_map, #{}),
    put(ms_prefix_sum, #{}).

-spec map_sum_insert(Key :: unicode:unicode_binary(), Val :: integer()) -> any().
map_sum_insert(Key, Val) ->
    KeyMap = get(ms_key_map),
    OldVal = maps:get(Key, KeyMap, 0),
    Delta = Val - OldVal,
    NewKeyMap = maps:put(Key, Val, KeyMap),

    PrefixMap = get(ms_prefix_sum),
    UpdatedPrefixMap = update_prefixes(Key, Delta, PrefixMap),

    put(ms_key_map, NewKeyMap),
    put(ms_prefix_sum, UpdatedPrefixMap).

-spec map_sum_sum(Prefix :: unicode:unicode_binary()) -> integer().
map_sum_sum(Prefix) ->
    PrefixMap = get(ms_prefix_sum),
    maps:get(Prefix, PrefixMap, 0).

%% internal helper
update_prefixes(Key, Delta, PrefixMap) ->
    Len = byte_size(Key),
    update_prefixes(1, Len, Key, Delta, PrefixMap).

update_prefixes(I, Max, _Key, _Delta, PrefixMap) when I > Max ->
    PrefixMap;
update_prefixes(I, Max, Key, Delta, PrefixMap) ->
    Prefix = binary:part(Key, {0, I}),
    Prev = maps:get(Prefix, PrefixMap, 0),
    NewPrefixMap = maps:put(Prefix, Prev + Delta, PrefixMap),
    update_prefixes(I + 1, Max, Key, Delta, NewPrefixMap).
```

## Elixir

```elixir
defmodule MapSum do
  @spec init_() :: any
  def init_() do
    Process.put(:key_map, %{})
    Process.put(:prefix_map, %{})
    :ok
  end

  @spec insert(key :: String.t(), val :: integer) :: any
  def insert(key, val) do
    key_map = Process.get(:key_map, %{})
    old_val = Map.get(key_map, key, 0)
    delta = val - old_val

    new_key_map = Map.put(key_map, key, val)
    Process.put(:key_map, new_key_map)

    prefix_map = Process.get(:prefix_map, %{})

    updated_prefix_map =
      if delta == 0 do
        prefix_map
      else
        len = byte_size(key)

        Enum.reduce(1..len, prefix_map, fn i, acc ->
          prefix = :binary.part(key, 0, i)
          Map.update(acc, prefix, delta, &(&1 + delta))
        end)
      end

    Process.put(:prefix_map, updated_prefix_map)
    :ok
  end

  @spec sum(prefix :: String.t()) :: integer
  def sum(prefix) do
    prefix_map = Process.get(:prefix_map, %{})
    Map.get(prefix_map, prefix, 0)
  end
end
```
