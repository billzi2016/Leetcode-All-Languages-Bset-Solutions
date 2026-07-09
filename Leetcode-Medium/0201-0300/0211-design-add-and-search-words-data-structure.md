# 0211. Design Add and Search Words Data Structure

## Cpp

```cpp
class WordDictionary {
public:
    /** Initialize your data structure here. */
    WordDictionary() : root(new TrieNode()) {}
    
    /** Adds a word into the data structure. */
    void addWord(std::string word) {
        TrieNode* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (!node->children[idx]) node->children[idx] = new TrieNode();
            node = node->children[idx];
        }
        node->isEnd = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(std::string word) {
        return dfs(root, word, 0);
    }
    
private:
    struct TrieNode {
        TrieNode* children[26];
        bool isEnd;
        TrieNode() : isEnd(false) {
            std::fill_n(children, 26, nullptr);
        }
    };
    
    TrieNode* root;
    
    bool dfs(TrieNode* node, const std::string& word, int pos) {
        if (!node) return false;
        if (pos == (int)word.size()) return node->isEnd;
        char ch = word[pos];
        if (ch == '.') {
            for (int i = 0; i < 26; ++i) {
                if (dfs(node->children[i], word, pos + 1)) return true;
            }
            return false;
        } else {
            int idx = ch - 'a';
            return dfs(node->children[idx], word, pos + 1);
        }
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
```

## Java

```java
class WordDictionary {

    private static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd;
    }

    private final TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            int idx = ch - 'a';
            if (node.children[idx] == null) {
                node.children[idx] = new TrieNode();
            }
            node = node.children[idx];
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        return dfs(root, word.toCharArray(), 0);
    }

    private boolean dfs(TrieNode node, char[] chars, int pos) {
        if (node == null) return false;
        if (pos == chars.length) return node.isEnd;

        char ch = chars[pos];
        if (ch != '.') {
            return dfs(node.children[ch - 'a'], chars, pos + 1);
        } else {
            for (TrieNode child : node.children) {
                if (dfs(child, chars, pos + 1)) {
                    return true;
                }
            }
            return false;
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
```

## Python

```python
class WordDictionary(object):
    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['#'] = True  # end of word marker

    def search(self, word):
        def dfs(i, node):
            if i == len(word):
                return '#' in node
            ch = word[i]
            if ch == '.':
                for child in node:
                    if child != '#':
                        if dfs(i + 1, node[child]):
                            return True
                return False
            else:
                if ch not in node:
                    return False
                return dfs(i + 1, node[ch])
        return dfs(0, self.trie)
```

## Python3

```python
class WordDictionary:
    class TrieNode:
        __slots__ = ('children', 'is_word')
        def __init__(self):
            self.children = {}
            self.is_word = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = self.TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_word
            ch = word[i]
            if ch == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], i + 1)
        return dfs(self.root, 0)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct TrieNode {
    struct TrieNode *child[26];
    bool isEnd;
} TrieNode;

typedef struct {
    TrieNode *root;
} WordDictionary;

/* Create a new trie node */
static TrieNode* createNode() {
    TrieNode *node = (TrieNode *)malloc(sizeof(TrieNode));
    if (!node) return NULL;
    memset(node->child, 0, sizeof(node->child));
    node->isEnd = false;
    return node;
}

/* Recursive search helper */
static bool dfsSearch(TrieNode *node, const char *word, int pos) {
    if (!node) return false;
    if (word[pos] == '\0')
        return node->isEnd;

    char c = word[pos];
    if (c == '.') {
        for (int i = 0; i < 26; ++i) {
            if (node->child[i] && dfsSearch(node->child[i], word, pos + 1))
                return true;
        }
        return false;
    } else {
        int idx = c - 'a';
        return dfsSearch(node->child[idx], word, pos + 1);
    }
}

/* Free trie recursively */
static void freeTrie(TrieNode *node) {
    if (!node) return;
    for (int i = 0; i < 26; ++i)
        freeTrie(node->child[i]);
    free(node);
}

/* Public API implementations */

WordDictionary* wordDictionaryCreate() {
    WordDictionary *obj = (WordDictionary *)malloc(sizeof(WordDictionary));
    if (!obj) return NULL;
    obj->root = createNode();
    return obj;
}

void wordDictionaryAddWord(WordDictionary* obj, char* word) {
    TrieNode *curr = obj->root;
    for (int i = 0; word[i] != '\0'; ++i) {
        int idx = word[i] - 'a';
        if (!curr->child[idx])
            curr->child[idx] = createNode();
        curr = curr->child[idx];
    }
    curr->isEnd = true;
}

bool wordDictionarySearch(WordDictionary* obj, char* word) {
    return dfsSearch(obj->root, word, 0);
}

void wordDictionaryFree(WordDictionary* obj) {
    if (!obj) return;
    freeTrie(obj->root);
    free(obj);
}
```

## Csharp

```csharp
public class WordDictionary
{
    private class TrieNode
    {
        public TrieNode[] Children = new TrieNode[26];
        public bool IsWord;
    }

    private readonly TrieNode _root = new TrieNode();

    public WordDictionary()
    {
    }

    public void AddWord(string word)
    {
        var node = _root;
        foreach (char ch in word)
        {
            int idx = ch - 'a';
            if (node.Children[idx] == null)
                node.Children[idx] = new TrieNode();
            node = node.Children[idx];
        }
        node.IsWord = true;
    }

    public bool Search(string word)
    {
        return Dfs(word, 0, _root);
    }

    private bool Dfs(string word, int pos, TrieNode node)
    {
        if (pos == word.Length)
            return node.IsWord;

        char c = word[pos];
        if (c == '.')
        {
            foreach (var child in node.Children)
            {
                if (child != null && Dfs(word, pos + 1, child))
                    return true;
            }
            return false;
        }
        else
        {
            int idx = c - 'a';
            var child = node.Children[idx];
            if (child == null) return false;
            return Dfs(word, pos + 1, child);
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.AddWord(word);
 * bool param_2 = obj.Search(word);
 */
```

## Javascript

```javascript
var WordDictionary = function() {
    this.root = { children: {}, end: false };
};

WordDictionary.prototype.addWord = function(word) {
    let node = this.root;
    for (const ch of word) {
        if (!node.children[ch]) {
            node.children[ch] = { children: {}, end: false };
        }
        node = node.children[ch];
    }
    node.end = true;
};

WordDictionary.prototype.search = function(word) {
    const dfs = (node, i) => {
        if (!node) return false;
        if (i === word.length) return node.end;
        const ch = word[i];
        if (ch !== '.') {
            return dfs(node.children[ch], i + 1);
        } else {
            for (const key in node.children) {
                if (dfs(node.children[key], i + 1)) return true;
            }
            return false;
        }
    };
    return dfs(this.root, 0);
};
```

## Typescript

```typescript
class TrieNode {
    children: (TrieNode | null)[];
    isEnd: boolean;
    constructor() {
        this.children = new Array(26).fill(null);
        this.isEnd = false;
    }
}

class WordDictionary {
    private root: TrieNode;

    constructor() {
        this.root = new TrieNode();
    }

    addWord(word: string): void {
        let node = this.root;
        for (const ch of word) {
            const idx = ch.charCodeAt(0) - 97;
            if (!node.children[idx]) {
                node.children[idx] = new TrieNode();
            }
            node = node.children[idx]!;
        }
        node.isEnd = true;
    }

    search(word: string): boolean {
        const dfs = (node: TrieNode, i: number): boolean => {
            if (i === word.length) {
                return node.isEnd;
            }
            const ch = word[i];
            if (ch !== '.') {
                const idx = ch.charCodeAt(0) - 97;
                const child = node.children[idx];
                if (!child) return false;
                return dfs(child, i + 1);
            } else {
                for (let j = 0; j < 26; j++) {
                    const child = node.children[j];
                    if (child && dfs(child, i + 1)) {
                        return true;
                    }
                }
                return false;
            }
        };
        return dfs(this.root, 0);
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
```

## Php

```php
class WordDictionary {
    private array $root = [];

    public function __construct() {
        $this->root = [];
    }

    /**
     * @param String $word
     * @return NULL
     */
    public function addWord($word) {
        $node =& $this->root;
        $len = strlen($word);
        for ($i = 0; $i < $len; $i++) {
            $c = $word[$i];
            if (!isset($node[$c])) {
                $node[$c] = [];
            }
            $node =& $node[$c];
        }
        $node['#'] = true;
    }

    /**
     * @param String $word
     * @return Boolean
     */
    public function search($word) {
        return $this->dfs($this->root, $word, 0);
    }

    private function dfs(array &$node, string $word, int $pos): bool {
        $len = strlen($word);
        if ($pos == $len) {
            return isset($node['#']);
        }
        $c = $word[$pos];
        if ($c === '.') {
            foreach ($node as $k => &$child) {
                if ($k === '#') {
                    continue;
                }
                if ($this->dfs($child, $word, $pos + 1)) {
                    return true;
                }
            }
            return false;
        } else {
            if (!isset($node[$c])) {
                return false;
            }
            return $this->dfs($node[$c], $word, $pos + 1);
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * $obj = new WordDictionary();
 * $obj->addWord($word);
 * $ret_2 = $obj->search($word);
 */
```

## Swift

```swift
class WordDictionary {
    private class TrieNode {
        var children: [Character: TrieNode] = [:]
        var isWord: Bool = false
    }
    
    private let root = TrieNode()
    
    init() { }
    
    func addWord(_ word: String) {
        var node = root
        for ch in word {
            if node.children[ch] == nil {
                node.children[ch] = TrieNode()
            }
            node = node.children[ch]!
        }
        node.isWord = true
    }
    
    func search(_ word: String) -> Bool {
        let chars = Array(word)
        return dfs(chars, 0, root)
    }
    
    private func dfs(_ chars: [Character], _ index: Int, _ node: TrieNode) -> Bool {
        if index == chars.count {
            return node.isWord
        }
        let ch = chars[index]
        if ch == "." {
            for child in node.children.values {
                if dfs(chars, index + 1, child) {
                    return true
                }
            }
            return false
        } else {
            guard let nextNode = node.children[ch] else { return false }
            return dfs(chars, index + 1, nextNode)
        }
    }
}
```

## Kotlin

```kotlin
class WordDictionary() {

    private class Node {
        var isWord: Boolean = false
        val children: Array<Node?> = arrayOfNulls(26)
    }

    private val root = Node()

    fun addWord(word: String) {
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
        return dfs(root, word, 0)
    }

    private fun dfs(node: Node?, word: String, index: Int): Boolean {
        if (node == null) return false
        if (index == word.length) return node.isWord
        val ch = word[index]
        return if (ch == '.') {
            for (child in node.children) {
                if (dfs(child, word, index + 1)) return true
            }
            false
        } else {
            val child = node.children[ch - 'a'] ?: return false
            dfs(child, word, index + 1)
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
```

## Dart

```dart
class WordDictionary {
  final _Node _root = _Node();

  WordDictionary() {}

  void addWord(String word) {
    var node = _root;
    for (int i = 0; i < word.length; i++) {
      String ch = word[i];
      node = node.children.putIfAbsent(ch, () => _Node());
    }
    node.isWord = true;
  }

  bool search(String word) {
    return _dfs(_root, word, 0);
  }

  bool _dfs(_Node node, String word, int index) {
    if (index == word.length) {
      return node.isWord;
    }
    String ch = word[index];
    if (ch == '.') {
      for (var child in node.children.values) {
        if (_dfs(child, word, index + 1)) {
          return true;
        }
      }
      return false;
    } else {
      var next = node.children[ch];
      if (next == null) return false;
      return _dfs(next, word, index + 1);
    }
  }
}

class _Node {
  final Map<String, _Node> children = {};
  bool isWord = false;
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = WordDictionary();
 * obj.addWord(word);
 * bool param2 = obj.search(word);
 */
```

## Golang

```go
type TrieNode struct {
	children [26]*TrieNode
	isEnd    bool
}

type WordDictionary struct {
	root *TrieNode
}

/** Initialize your data structure here. */
func Constructor() WordDictionary {
	return WordDictionary{root: &TrieNode{}}
}

/** Adds a word into the data structure. */
func (this *WordDictionary) AddWord(word string) {
	node := this.root
	for i := 0; i < len(word); i++ {
		c := word[i] - 'a'
		if node.children[c] == nil {
			node.children[c] = &TrieNode{}
		}
		node = node.children[c]
	}
	node.isEnd = true
}

/** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
func (this *WordDictionary) Search(word string) bool {
	return dfs(this.root, word, 0)
}

func dfs(node *TrieNode, word string, idx int) bool {
	if node == nil {
		return false
	}
	if idx == len(word) {
		return node.isEnd
	}
	ch := word[idx]
	if ch != '.' {
		child := node.children[ch-'a']
		return dfs(child, word, idx+1)
	}
	// wildcard: try all possible children
	for i := 0; i < 26; i++ {
		if node.children[i] != nil && dfs(node.children[i], word, idx+1) {
			return true
		}
	}
	return false
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */
```

## Ruby

```ruby
class TrieNode
  attr_accessor :children, :is_end

  def initialize
    @children = {}
    @is_end = false
  end
end

class WordDictionary
  def initialize()
    @root = TrieNode.new
  end

=begin
    :type word: String
    :rtype: Void
=end
  def add_word(word)
    node = @root
    word.each_char do |ch|
      node.children[ch] ||= TrieNode.new
      node = node.children[ch]
    end
    node.is_end = true
  end

=begin
    :type word: String
    :rtype: Boolean
=end
  def search(word)
    dfs(@root, word, 0)
  end

  private

  def dfs(node, word, idx)
    return false unless node
    if idx == word.length
      return node.is_end
    end

    ch = word[idx]
    if ch == '.'
      node.children.each_value do |child|
        return true if dfs(child, word, idx + 1)
      end
      false
    else
      child = node.children[ch]
      return false unless child
      dfs(child, word, idx + 1)
    end
  end
end
```

## Scala

```scala
class WordDictionary() {

  private class Node {
    val child = new Array[Node](26)
    var isWord: Boolean = false
  }

  private val root = new Node

  def addWord(word: String): Unit = {
    var node = root
    for (c <- word) {
      val idx = c - 'a'
      if (node.child(idx) == null) node.child(idx) = new Node
      node = node.child(idx)
    }
    node.isWord = true
  }

  def search(word: String): Boolean = {
    def dfs(node: Node, i: Int): Boolean = {
      if (node == null) return false
      if (i == word.length) return node.isWord
      val ch = word.charAt(i)
      if (ch == '.') {
        var j = 0
        while (j < 26) {
          if (dfs(node.child(j), i + 1)) return true
          j += 1
        }
        false
      } else {
        dfs(node.child(ch - 'a'), i + 1)
      }
    }
    dfs(root, 0)
  }

}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * val obj = new WordDictionary()
 * obj.addWord(word)
 * val param_2 = obj.search(word)
 */
```

## Rust

```rust
use std::cell::RefCell;
use std::rc::Rc;
use std::collections::HashMap;

type NodePtr = Rc<RefCell<Node>>;

struct Node {
    children: HashMap<char, NodePtr>,
    is_end: bool,
}

impl Node {
    fn new() -> Self {
        Node {
            children: HashMap::new(),
            is_end: false,
        }
    }
}

struct WordDictionary {
    root: NodePtr,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl WordDictionary {

    fn new() -> Self {
        WordDictionary {
            root: Rc::new(RefCell::new(Node::new())),
        }
    }
    
    fn add_word(&self, word: String) {
        let mut node = self.root.clone();
        for ch in word.chars() {
            let next = {
                let mut n = node.borrow_mut();
                n.children
                    .entry(ch)
                    .or_insert_with(|| Rc::new(RefCell::new(Node::new())))
                    .clone()
            };
            node = next;
        }
        node.borrow_mut().is_end = true;
    }
    
    fn search(&self, word: String) -> bool {
        fn dfs(node: &NodePtr, chars: &[char], idx: usize) -> bool {
            if idx == chars.len() {
                return node.borrow().is_end;
            }
            let c = chars[idx];
            if c == '.' {
                // Collect children to avoid holding the borrow across recursion
                let children: Vec<NodePtr> = {
                    let n = node.borrow();
                    n.children.values().cloned().collect()
                };
                for child in children {
                    if dfs(&child, chars, idx + 1) {
                        return true;
                    }
                }
                false
            } else {
                match node.borrow().children.get(&c) {
                    Some(child) => dfs(child, chars, idx + 1),
                    None => false,
                }
            }
        }

        let chars: Vec<char> = word.chars().collect();
        dfs(&self.root, &chars, 0)
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * let obj = WordDictionary::new();
 * obj.add_word(word);
 * let ret_2: bool = obj.search(word);
 */
```

## Racket

```racket
(struct node ([children #:mutable] [end? #:mutable]) #:transparent)

(define word-dictionary%
  (class object%
    (super-new)
    
    (init-field) ; no init fields
    
    (define root (node (make-hash) #f))
    
    ;; add-word : string? -> void?
    (define/public (add-word word)
      (let ([cur root])
        (for ([i (in-range (string-length word))])
          (let* ([c (string-ref word i)]
                 [child (hash-ref (node-children cur) c #f)])
            (unless child
              (set! child (node (make-hash) #f))
              (hash-set! (node-children cur) c child))
            (set! cur child)))
        (set-node-end?! cur #t)))
    
    ;; search : string? -> boolean?
    (define/public (search word)
      (letrec ([dfs
                (lambda (cur idx)
                  (if (= idx (string-length word))
                      (node-end? cur)
                      (let ([c (string-ref word idx)])
                        (if (char=? c #\.)
                            (for/or ([pair (in-hash (node-children cur))])
                              (dfs (cdr pair) (+ idx 1)))
                            (let* ([child (hash-ref (node-children cur) c #f)])
                              (and child (dfs child (+ idx 1))))))))])
        (dfs root 0)))))
```

## Erlang

```erlang
-module(solution).
-export([word_dictionary_init_/0,
         word_dictionary_add_word/1,
         word_dictionary_search/1]).

-define(TABLE, word_dict_table).

word_dictionary_init_() ->
    case ets:info(?TABLE) of
        undefined -> ok;
        _ -> ets:delete(?TABLE)
    end,
    ets:new(?TABLE, [named_table, public, set]),
    ok.

word_dictionary_add_word(Word) when is_binary(Word) ->
    ets:insert(?TABLE, {Word}),
    ok.

word_dictionary_search(Pattern) when is_binary(Pattern) ->
    Fun = fun({W}, Acc) ->
        case Acc of
            true -> true;
            false ->
                case matches(Pattern, W) of
                    true -> true;
                    false -> false
                end
        end
    end,
    ets:foldl(Fun, false, ?TABLE).

matches(<<>>, <<>>) -> true;
matches(<<".", RestPat/binary>>, <<_, RestWord/binary>>) ->
    matches(RestPat, RestWord);
matches(<<C, RestPat/binary>>, <<C, RestWord/binary>>) ->
    matches(RestPat, RestWord);
matches(_, _) -> false.
```

## Elixir

```elixir
defmodule WordDictionary do
  @spec init_() :: any
  def init_() do
    root = %{children: %{}, end?: false}
    Process.put(:word_dict_root, root)
    :ok
  end

  @spec add_word(word :: String.t) :: any
  def add_word(word) do
    root = Process.get(:word_dict_root)
    new_root = add(root, String.graphemes(word))
    Process.put(:word_dict_root, new_root)
    :ok
  end

  @spec search(word :: String.t) :: boolean
  def search(word) do
    root = Process.get(:word_dict_root)
    dfs(root, String.graphemes(word))
  end

  defp add(node, []), do: %{node | end?: true}

  defp add(node, [c | rest]) do
    child = Map.get(node.children, c, %{children: %{}, end?: false})
    new_child = add(child, rest)
    %{node | children: Map.put(node.children, c, new_child)}
  end

  defp dfs(node, []), do: node.end?

  defp dfs(node, [c | rest]) when c != "." do
    case Map.get(node.children, c) do
      nil -> false
      child -> dfs(child, rest)
    end
  end

  defp dfs(node, [_dot | rest]) do
    Enum.any?(node.children, fn {_k, child} -> dfs(child, rest) end)
  end
end
```
