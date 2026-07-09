# 0208. Implement Trie (Prefix Tree)

## Cpp

```cpp
class Trie {
private:
    struct Node {
        bool isEnd;
        Node* child[26];
        Node() : isEnd(false) {
            for (int i = 0; i < 26; ++i) child[i] = nullptr;
        }
    };
    Node* root;
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new Node();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        Node* node = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!node->child[idx]) node->child[idx] = new Node();
            node = node->child[idx];
        }
        node->isEnd = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        Node* node = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!node->child[idx]) return false;
            node = node->child[idx];
        }
        return node->isEnd;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        Node* node = root;
        for (char c : prefix) {
            int idx = c - 'a';
            if (!node->child[idx]) return false;
            node = node->child[idx];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
```

## Java

```java
class Trie {
    private static class Node {
        Node[] child = new Node[26];
        boolean isWord;
    }

    private final Node root;

    public Trie() {
        root = new Node();
    }

    public void insert(String word) {
        Node node = root;
        for (int i = 0; i < word.length(); i++) {
            int idx = word.charAt(i) - 'a';
            if (node.child[idx] == null) {
                node.child[idx] = new Node();
            }
            node = node.child[idx];
        }
        node.isWord = true;
    }

    public boolean search(String word) {
        Node node = findNode(word);
        return node != null && node.isWord;
    }

    public boolean startsWith(String prefix) {
        return findNode(prefix) != null;
    }

    private Node findNode(String s) {
        Node node = root;
        for (int i = 0; i < s.length(); i++) {
            int idx = s.charAt(i) - 'a';
            if (node.child[idx] == null) {
                return null;
            }
            node = node.child[idx];
        }
        return node;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
```

## Python

```python
class TrieNode:
    __slots__ = ('children', 'is_word')
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
```

## Python3

```python
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['#'] = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct TrieNode {
    struct TrieNode* children[26];
    bool isEnd;
} TrieNode;

typedef struct {
    TrieNode* root;
} Trie;

static TrieNode* createNode() {
    TrieNode* node = (TrieNode*)calloc(1, sizeof(TrieNode));
    return node;
}

Trie* trieCreate() {
    Trie* obj = (Trie*)malloc(sizeof(Trie));
    if (!obj) return NULL;
    obj->root = createNode();
    return obj;
}

void trieInsert(Trie* obj, char* word) {
    TrieNode* cur = obj->root;
    for (int i = 0; word[i]; ++i) {
        int idx = word[i] - 'a';
        if (!cur->children[idx]) {
            cur->children[idx] = createNode();
        }
        cur = cur->children[idx];
    }
    cur->isEnd = true;
}

bool trieSearch(Trie* obj, char* word) {
    TrieNode* cur = obj->root;
    for (int i = 0; word[i]; ++i) {
        int idx = word[i] - 'a';
        if (!cur->children[idx]) return false;
        cur = cur->children[idx];
    }
    return cur->isEnd;
}

bool trieStartsWith(Trie* obj, char* prefix) {
    TrieNode* cur = obj->root;
    for (int i = 0; prefix[i]; ++i) {
        int idx = prefix[i] - 'a';
        if (!cur->children[idx]) return false;
        cur = cur->children[idx];
    }
    return true;
}

static void freeNode(TrieNode* node) {
    if (!node) return;
    for (int i = 0; i < 26; ++i) {
        if (node->children[i]) {
            freeNode(node->children[i]);
        }
    }
    free(node);
}

void trieFree(Trie* obj) {
    if (!obj) return;
    freeNode(obj->root);
    free(obj);
}

/**
 * Your Trie struct will be instantiated and called as such:
 * Trie* obj = trieCreate();
 * trieInsert(obj, word);
 *
 * bool param_2 = trieSearch(obj, word);
 *
 * bool param_3 = trieStartsWith(obj, prefix);
 *
 * trieFree(obj);
 */
```

## Csharp

```csharp
public class Trie
{
    private class Node
    {
        public Node[] Children = new Node[26];
        public bool IsWord;
    }

    private readonly Node _root;

    public Trie()
    {
        _root = new Node();
    }

    public void Insert(string word)
    {
        var node = _root;
        foreach (char ch in word)
        {
            int idx = ch - 'a';
            if (node.Children[idx] == null)
                node.Children[idx] = new Node();
            node = node.Children[idx];
        }
        node.IsWord = true;
    }

    public bool Search(string word)
    {
        var node = FindNode(word);
        return node != null && node.IsWord;
    }

    public bool StartsWith(string prefix)
    {
        return FindNode(prefix) != null;
    }

    private Node FindNode(string s)
    {
        var node = _root;
        foreach (char ch in s)
        {
            int idx = ch - 'a';
            if (node.Children[idx] == null)
                return null;
            node = node.Children[idx];
        }
        return node;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.Insert(word);
 * bool param_2 = obj.Search(word);
 * bool param_3 = obj.StartsWith(prefix);
 */
```

## Javascript

```javascript
var Trie = function() {
    this.root = {};
};

Trie.prototype.insert = function(word) {
    let node = this.root;
    for (let i = 0; i < word.length; i++) {
        const ch = word[i];
        if (!node[ch]) {
            node[ch] = {};
        }
        node = node[ch];
    }
    node.isEnd = true;
};

Trie.prototype.search = function(word) {
    let node = this.root;
    for (let i = 0; i < word.length; i++) {
        const ch = word[i];
        if (!node[ch]) return false;
        node = node[ch];
    }
    return !!node.isEnd;
};

Trie.prototype.startsWith = function(prefix) {
    let node = this.root;
    for (let i = 0; i < prefix.length; i++) {
        const ch = prefix[i];
        if (!node[ch]) return false;
        node = node[ch];
    }
    return true;
};
```

## Typescript

```typescript
class TrieNode {
    children: Array<TrieNode | null>;
    isEnd: boolean;
    constructor() {
        this.children = new Array(26).fill(null);
        this.isEnd = false;
    }
}

class Trie {
    private root: TrieNode;

    constructor() {
        this.root = new TrieNode();
    }

    insert(word: string): void {
        let node = this.root;
        for (let i = 0; i < word.length; i++) {
            const idx = word.charCodeAt(i) - 97;
            if (!node.children[idx]) {
                node.children[idx] = new TrieNode();
            }
            node = node.children[idx]!;
        }
        node.isEnd = true;
    }

    search(word: string): boolean {
        let node = this.root;
        for (let i = 0; i < word.length; i++) {
            const idx = word.charCodeAt(i) - 97;
            if (!node.children[idx]) return false;
            node = node.children[idx]!;
        }
        return node.isEnd;
    }

    startsWith(prefix: string): boolean {
        let node = this.root;
        for (let i = 0; i < prefix.length; i++) {
            const idx = prefix.charCodeAt(i) - 97;
            if (!node.children[idx]) return false;
            node = node.children[idx]!;
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
```

## Php

```php
class Trie {
    /**
     * @var array
     */
    private $root;

    /**
     */
    function __construct() {
        $this->root = [];
    }

    /**
     * @param String $word
     * @return NULL
     */
    function insert($word) {
        $node = &$this->root;
        $len = strlen($word);
        for ($i = 0; $i < $len; $i++) {
            $c = $word[$i];
            if (!isset($node[$c])) {
                $node[$c] = [];
            }
            $node = &$node[$c];
        }
        $node['#'] = true;
    }

    /**
     * @param String $word
     * @return Boolean
     */
    function search($word) {
        $node = $this->root;
        $len = strlen($word);
        for ($i = 0; $i < $len; $i++) {
            $c = $word[$i];
            if (!isset($node[$c])) {
                return false;
            }
            $node = $node[$c];
        }
        return isset($node['#']);
    }

    /**
     * @param String $prefix
     * @return Boolean
     */
    function startsWith($prefix) {
        $node = $this->root;
        $len = strlen($prefix);
        for ($i = 0; $i < $len; $i++) {
            $c = $prefix[$i];
            if (!isset($node[$c])) {
                return false;
            }
            $node = $node[$c];
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * $obj = new Trie();
 * $obj->insert($word);
 * $ret_2 = $obj->search($word);
 * $ret_3 = $obj->startsWith($prefix);
 */
```

## Swift

```swift
class TrieNode {
    var children: [TrieNode?] = Array(repeating: nil, count: 26)
    var isEnd: Bool = false
}

class Trie {

    private let root = TrieNode()
    
    init() { }
    
    func insert(_ word: String) {
        var node = root
        for ch in word.utf8 {
            let idx = Int(ch - 97)
            if node.children[idx] == nil {
                node.children[idx] = TrieNode()
            }
            node = node.children[idx]!
        }
        node.isEnd = true
    }
    
    func search(_ word: String) -> Bool {
        var node = root
        for ch in word.utf8 {
            let idx = Int(ch - 97)
            guard let next = node.children[idx] else { return false }
            node = next
        }
        return node.isEnd
    }
    
    func startsWith(_ prefix: String) -> Bool {
        var node = root
        for ch in prefix.utf8 {
            let idx = Int(ch - 97)
            guard let next = node.children[idx] else { return false }
            node = next
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Trie() {

    private class Node {
        val children = arrayOfNulls<Node>(26)
        var isWord: Boolean = false
    }

    private val root = Node()

    fun insert(word: String) {
        var node = root
        for (ch in word) {
            val idx = ch - 'a'
            if (node.children[idx] == null) {
                node.children[idx] = Node()
            }
            node = node.children[idx]!!
        }
        node.isWord = true
    }

    fun search(word: String): Boolean {
        var node = root
        for (ch in word) {
            val idx = ch - 'a'
            val next = node.children[idx] ?: return false
            node = next
        }
        return node.isWord
    }

    fun startsWith(prefix: String): Boolean {
        var node = root
        for (ch in prefix) {
            val idx = ch - 'a'
            val next = node.children[idx] ?: return false
            node = next
        }
        return true
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
```

## Dart

```dart
class _TrieNode {
  List<_TrieNode?> children = List.filled(26, null);
  bool isEnd = false;
}

class Trie {
  final _TrieNode _root = _TrieNode();

  Trie() {}

  void insert(String word) {
    var node = _root;
    for (int i = 0; i < word.length; i++) {
      int idx = word.codeUnitAt(i) - 97;
      node.children[idx] ??= _TrieNode();
      node = node.children[idx]!;
    }
    node.isEnd = true;
  }

  bool search(String word) {
    var node = _root;
    for (int i = 0; i < word.length; i++) {
      int idx = word.codeUnitAt(i) - 97;
      if (node.children[idx] == null) return false;
      node = node.children[idx]!;
    }
    return node.isEnd;
  }

  bool startsWith(String prefix) {
    var node = _root;
    for (int i = 0; i < prefix.length; i++) {
      int idx = prefix.codeUnitAt(i) - 97;
      if (node.children[idx] == null) return false;
      node = node.children[idx]!;
    }
    return true;
  }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = Trie();
 * obj.insert(word);
 * bool param2 = obj.search(word);
 * bool param3 = obj.startsWith(prefix);
 */
```

## Golang

```go
type TrieNode struct {
	children [26]*TrieNode
	isEnd    bool
}

type Trie struct {
	root *TrieNode
}

/** Initialize your data structure here. */
func Constructor() Trie {
	return Trie{root: &TrieNode{}}
}

/** Inserts a word into the trie. */
func (this *Trie) Insert(word string) {
	node := this.root
	for i := 0; i < len(word); i++ {
		idx := word[i] - 'a'
		if node.children[idx] == nil {
			node.children[idx] = &TrieNode{}
		}
		node = node.children[idx]
	}
	node.isEnd = true
}

/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
	node := this.root
	for i := 0; i < len(word); i++ {
		idx := word[i] - 'a'
		if node.children[idx] == nil {
			return false
		}
		node = node.children[idx]
	}
	return node.isEnd
}

/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
	node := this.root
	for i := 0; i < len(prefix); i++ {
		idx := prefix[i] - 'a'
		if node.children[idx] == nil {
			return false
		}
		node = node.children[idx]
	}
	return true
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
```

## Ruby

```ruby
class Trie
  class Node
    attr_accessor :children, :is_end
    def initialize
      @children = {}
      @is_end = false
    end
  end

  def initialize()
    @root = Node.new
  end

=begin
    :type word: String
    :rtype: Void
=end
  def insert(word)
    node = @root
    word.each_char do |ch|
      node.children[ch] ||= Node.new
      node = node.children[ch]
    end
    node.is_end = true
  end

=begin
    :type word: String
    :rtype: Boolean
=end
  def search(word)
    node = @root
    word.each_char do |ch|
      return false unless node.children.key?(ch)
      node = node.children[ch]
    end
    node.is_end
  end

=begin
    :type prefix: String
    :rtype: Boolean
=end
  def starts_with(prefix)
    node = @root
    prefix.each_char do |ch|
      return false unless node.children.key?(ch)
      node = node.children[ch]
    end
    true
  end
end
```

## Scala

```scala
class Trie() {

  private class Node {
    val children = new Array[Node](26)
    var isEnd: Boolean = false
  }

  private val root = new Node

  def insert(word: String): Unit = {
    var node = root
    for (c <- word) {
      val idx = c - 'a'
      if (node.children(idx) == null) node.children(idx) = new Node
      node = node.children(idx)
    }
    node.isEnd = true
  }

  def search(word: String): Boolean = {
    var node = root
    for (c <- word) {
      val idx = c - 'a'
      if (node.children(idx) == null) return false
      node = node.children(idx)
    }
    node.isEnd
  }

  def startsWith(prefix: String): Boolean = {
    var node = root
    for (c <- prefix) {
      val idx = c - 'a'
      if (node.children(idx) == null) return false
      node = node.children(idx)
    }
    true
  }

}

/**
 * Your Trie object will be instantiated and called as such:
 * val obj = new Trie()
 * obj.insert(word)
 * val param_2 = obj.search(word)
 * val param_3 = obj.startsWith(prefix)
 */
```

## Rust

```rust
struct Trie {
    root: Box<Node>,
}

struct Node {
    children: [Option<Box<Node>>; 26],
    is_end: bool,
}

impl Node {
    fn new() -> Self {
        Node {
            children: [None; 26],
            is_end: false,
        }
    }
}

impl Trie {
    fn new() -> Self {
        Trie { root: Box::new(Node::new()) }
    }

    fn insert(&mut self, word: String) {
        let mut node = &mut *self.root;
        for b in word.bytes() {
            let idx = (b - b'a') as usize;
            if node.children[idx].is_none() {
                node.children[idx] = Some(Box::new(Node::new()));
            }
            node = node.children[idx].as_mut().unwrap();
        }
        node.is_end = true;
    }

    fn search(&self, word: String) -> bool {
        let mut node = &*self.root;
        for b in word.bytes() {
            let idx = (b - b'a') as usize;
            match &node.children[idx] {
                Some(child) => node = child,
                None => return false,
            }
        }
        node.is_end
    }

    fn starts_with(&self, prefix: String) -> bool {
        let mut node = &*self.root;
        for b in prefix.bytes() {
            let idx = (b - b'a') as usize;
            match &node.children[idx] {
                Some(child) => node = child,
                None => return false,
            }
        }
        true
    }
}
```

## Racket

```racket
(struct node ([children #:mutable] [is-end? #:mutable]))

(define trie%
  (class object%
    (super-new)

    ; root node for each instance
    (define root (node (make-hash) #f))

    ; insert : string? -> void?
    (define/public (insert word)
      (let loop ((i 0) (curr root))
        (if (= i (string-length word))
            (set-node-is-end?! curr #t)
            (let* ((ch (string-ref word i))
                   (child (hash-ref (node-children curr) ch #f)))
              (unless child
                (set! child (node (make-hash) #f))
                (hash-set! (node-children curr) ch child))
              (loop (+ i 1) child)))))

    ; search : string? -> boolean?
    (define/public (search word)
      (let loop ((i 0) (curr root))
        (if (= i (string-length word))
            (node-is-end? curr)
            (let* ((ch (string-ref word i))
                   (child (hash-ref (node-children curr) ch #f)))
              (if child
                  (loop (+ i 1) child)
                  #f)))))

    ; starts-with : string? -> boolean?
    (define/public (starts-with prefix)
      (let loop ((i 0) (curr root))
        (if (= i (string-length prefix))
            #t
            (let* ((ch (string-ref prefix i))
                   (child (hash-ref (node-children curr) ch #f)))
              (if child
                  (loop (+ i 1) child)
                  #f)))))))
```

## Erlang

```erlang
-module(solution).
-export([trie_init_/0, trie_insert/1, trie_search/1, trie_starts_with/1]).

%% internal helper to create an empty node
empty_node() ->
    #{c => #{}, eow => false}.

%% initialize the trie (called before each test case)
trie_init_() ->
    put(trie_root, empty_node()),
    ok.

%% insert a word into the trie
trie_insert(Word) when is_binary(Word) ->
    Root = case get(trie_root) of
        undefined -> empty_node();
        R -> R
    end,
    Chars = unicode:characters_to_list(Word),
    NewRoot = insert(Root, Chars),
    put(trie_root, NewRoot),
    ok.

insert(Node, []) ->
    Node#{eow => true};
insert(Node, [H|T]) ->
    Children = maps:get(c, Node, #{}),
    ChildNode = case maps:find(H, Children) of
        {ok, CN} -> CN;
        error -> empty_node()
    end,
    UpdatedChild = insert(ChildNode, T),
    NewChildren = maps:put(H, UpdatedChild, Children),
    Node#{c => NewChildren}.

%% search for a whole word in the trie
trie_search(Word) when is_binary(Word) ->
    Root = case get(trie_root) of
        undefined -> empty_node();
        R -> R
    end,
    Chars = unicode:characters_to_list(Word),
    search(Root, Chars).

search(Node, []) ->
    maps:get(eow, Node, false);
search(Node, [H|T]) ->
    Children = maps:get(c, Node, #{}),
    case maps:find(H, Children) of
        {ok, Child} -> search(Child, T);
        error -> false
    end.

%% check if any word in the trie starts with the given prefix
trie_starts_with(Prefix) when is_binary(Prefix) ->
    Root = case get(trie_root) of
        undefined -> empty_node();
        R -> R
    end,
    Chars = unicode:characters_to_list(Prefix),
    starts(Root, Chars).

starts(_Node, []) ->
    true;
starts(Node, [H|T]) ->
    Children = maps:get(c, Node, #{}),
    case maps:find(H, Children) of
        {ok, Child} -> starts(Child, T);
        error -> false
    end.
```

## Elixir

```elixir
defmodule Trie do
  @spec init_() :: any
  def init_() do
    root = %{children: %{}, end_of_word: false}
    Process.put(:trie_root, root)
  end

  @spec insert(word :: String.t) :: any
  def insert(word) do
    root = Process.get(:trie_root)
    chars = String.graphemes(word)
    new_root = do_insert(root, chars)
    Process.put(:trie_root, new_root)
  end

  @spec search(word :: String.t) :: boolean
  def search(word) do
    root = Process.get(:trie_root)
    case traverse(root, String.graphemes(word)) do
      nil -> false
      node -> node.end_of_word
    end
  end

  @spec starts_with(prefix :: String.t) :: boolean
  def starts_with(prefix) do
    root = Process.get(:trie_root)
    case traverse(root, String.graphemes(prefix)) do
      nil -> false
      _node -> true
    end
  end

  # Private helpers

  defp do_insert(node, []), do: %{node | end_of_word: true}

  defp do_insert(node, [ch | rest]) do
    child = Map.get(node.children, ch, %{children: %{}, end_of_word: false})
    updated_child = do_insert(child, rest)
    new_children = Map.put(node.children, ch, updated_child)
    %{node | children: new_children}
  end

  defp traverse(nil, _), do: nil
  defp traverse(node, []), do: node

  defp traverse(node, [ch | rest]) do
    child = Map.get(node.children, ch)
    traverse(child, rest)
  end
end
```
