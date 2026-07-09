# 0745. Prefix and Suffix Search

## Cpp

```cpp
class WordFilter {
public:
    struct Node {
        int nxt[27];
        int w;
        Node() : w(-1) { for (int i = 0; i < 27; ++i) nxt[i] = -1; }
    };
    std::vector<Node> trie;
    
    WordFilter(std::vector<std::string>& words) {
        trie.emplace_back(); // root
        for (int weight = 0; weight < (int)words.size(); ++weight) {
            const std::string& w = words[weight];
            int L = w.size();
            for (int i = 0; i <= L; ++i) { // each suffix start
                int node = 0;
                // insert suffix part
                for (int j = i; j < L; ++j) {
                    int c = w[j] - 'a';
                    if (trie[node].nxt[c] == -1) {
                        trie[node].nxt[c] = trie.size();
                        trie.emplace_back();
                    }
                    node = trie[node].nxt[c];
                    trie[node].w = weight;
                }
                // separator '{' -> index 26
                const int sep = 26;
                if (trie[node].nxt[sep] == -1) {
                    trie[node].nxt[sep] = trie.size();
                    trie.emplace_back();
                }
                node = trie[node].nxt[sep];
                trie[node].w = weight;
                // insert whole word
                for (int j = 0; j < L; ++j) {
                    int c = w[j] - 'a';
                    if (trie[node].nxt[c] == -1) {
                        trie[node].nxt[c] = trie.size();
                        trie.emplace_back();
                    }
                    node = trie[node].nxt[c];
                    trie[node].w = weight;
                }
            }
        }
    }
    
    int f(std::string pref, std::string suff) {
        int node = 0;
        for (char ch : suff) {
            int c = ch - 'a';
            if (trie[node].nxt[c] == -1) return -1;
            node = trie[node].nxt[c];
        }
        const int sep = 26;
        if (trie[node].nxt[sep] == -1) return -1;
        node = trie[node].nxt[sep];
        for (char ch : pref) {
            int c = ch - 'a';
            if (trie[node].nxt[c] == -1) return -1;
            node = trie[node].nxt[c];
        }
        return trie[node].w;
    }
};

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter* obj = new WordFilter(words);
 * int param_1 = obj->f(pref,suff);
 */
```

## Java

```java
class WordFilter {
    private static class TrieNode {
        TrieNode[] child = new TrieNode[27];
        int weight = -1;
    }

    private final TrieNode root = new TrieNode();

    public WordFilter(String[] words) {
        for (int w = 0; w < words.length; ++w) {
            String word = words[w];
            int n = word.length();
            // insert all suffixes combined with the whole word
            for (int i = 0; i <= n; ++i) {
                String key = word.substring(i) + "{" + word;
                insert(key, w);
            }
        }
    }

    private void insert(String s, int weight) {
        TrieNode node = root;
        for (char ch : s.toCharArray()) {
            int idx = ch == '{' ? 26 : ch - 'a';
            if (node.child[idx] == null) node.child[idx] = new TrieNode();
            node = node.child[idx];
            node.weight = weight; // keep latest (largest index)
        }
    }

    public int f(String pref, String suff) {
        String key = suff + "{" + pref;
        TrieNode node = root;
        for (char ch : key.toCharArray()) {
            int idx = ch == '{' ? 26 : ch - 'a';
            if (node.child[idx] == null) return -1;
            node = node.child[idx];
        }
        return node.weight;
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter obj = new WordFilter(words);
 * int param_1 = obj.f(pref,suff);
 */
```

## Python

```python
class WordFilter(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = {}
        for weight, word in enumerate(words):
            L = len(word)
            # insert all suffixes combined with the whole word
            for i in range(L + 1):
                combo = word[i:] + '{' + word
                node = self.trie
                for ch in combo:
                    if ch not in node:
                        node[ch] = {}
                    node = node[ch]
                    node['#'] = weight  # store latest (largest) index

    def f(self, pref, suff):
        """
        :type pref: str
        :type suff: str
        :rtype: int
        """
        key = suff + '{' + pref
        node = self.trie
        for ch in key:
            if ch not in node:
                return -1
            node = node[ch]
        return node.get('#', -1)
```

## Python3

```python
from typing import List

class TrieNode:
    __slots__ = ('children', 'weight')
    def __init__(self):
        self.children = {}
        self.weight = -1

class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for weight, word in enumerate(words):
            L = len(word)
            # insert all suffixes combined with the whole word
            for i in range(L + 1):
                combined = word[i:] + '{' + word
                node = self.root
                for ch in combined:
                    if ch not in node.children:
                        node.children[ch] = TrieNode()
                    node = node.children[ch]
                    node.weight = weight

    def f(self, pref: str, suff: str) -> int:
        node = self.root
        query = suff + '{' + pref
        for ch in query:
            if ch not in node.children:
                return -1
            node = node.children[ch]
        return node.weight
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct TrieNode {
    int weight;
    struct TrieNode *child[27];
} TrieNode;

static TrieNode* newNode() {
    TrieNode *node = (TrieNode *)malloc(sizeof(TrieNode));
    node->weight = -1;
    memset(node->child, 0, sizeof(node->child));
    return node;
}

typedef struct {
    TrieNode *root;
} WordFilter;

/** Initialize your data structure here. */
WordFilter* wordFilterCreate(char** words, int wordsSize) {
    WordFilter *obj = (WordFilter *)malloc(sizeof(WordFilter));
    obj->root = newNode();
    for (int idx = 0; idx < wordsSize; ++idx) {
        char *w = words[idx];
        int L = strlen(w);
        // insert all suffixes combined with '{' and the whole word
        for (int i = 0; i <= L; ++i) { // i is start of suffix
            TrieNode *node = obj->root;
            // suffix part
            for (int k = i; k < L; ++k) {
                int c = w[k] - 'a';
                if (!node->child[c]) node->child[c] = newNode();
                node = node->child[c];
                node->weight = idx;
            }
            // separator '{' -> index 26
            if (!node->child[26]) node->child[26] = newNode();
            node = node->child[26];
            node->weight = idx;
            // whole word part (acts as prefix)
            for (int k = 0; k < L; ++k) {
                int c = w[k] - 'a';
                if (!node->child[c]) node->child[c] = newNode();
                node = node->child[c];
                node->weight = idx;
            }
        }
    }
    return obj;
}

/** Return the index of word with given prefix and suffix. */
int wordFilterF(WordFilter* obj, char* pref, char* suff) {
    TrieNode *node = obj->root;
    // traverse suffix
    for (int i = 0; suff[i]; ++i) {
        int c = suff[i] - 'a';
        if (!node->child[c]) return -1;
        node = node->child[c];
    }
    // separator '{'
    if (!node->child[26]) return -1;
    node = node->child[26];
    // traverse prefix
    for (int i = 0; pref[i]; ++i) {
        int c = pref[i] - 'a';
        if (!node->child[c]) return -1;
        node = node->child[c];
    }
    return node ? node->weight : -1;
}

/* Helper to free trie recursively */
static void freeTrie(TrieNode *node) {
    if (!node) return;
    for (int i = 0; i < 27; ++i) {
        if (node->child[i]) freeTrie(node->child[i]);
    }
    free(node);
}

/** Deallocate memory. */
void wordFilterFree(WordFilter* obj) {
    if (!obj) return;
    freeTrie(obj->root);
    free(obj);
}

/**
 * Your WordFilter struct will be instantiated and called as such:
 * WordFilter* obj = wordFilterCreate(words, wordsSize);
 * int param_1 = wordFilterF(obj, pref, suff);
 * wordFilterFree(obj);
 */
```

## Csharp

```csharp
public class WordFilter {
    private class TrieNode {
        public TrieNode[] Children = new TrieNode[27];
        public int Weight = -1;
    }

    private readonly TrieNode _root = new TrieNode();

    public WordFilter(string[] words) {
        for (int index = 0; index < words.Length; index++) {
            string word = words[index];
            int len = word.Length;
            // Insert all suffixes combined with the whole word
            for (int i = 0; i <= len; i++) {
                string key = word.Substring(i) + "{" + word;
                Insert(key, index);
            }
        }
    }

    private void Insert(string key, int weight) {
        TrieNode node = _root;
        foreach (char ch in key) {
            int idx = ch == '{' ? 26 : ch - 'a';
            if (node.Children[idx] == null) {
                node.Children[idx] = new TrieNode();
            }
            node = node.Children[idx];
            node.Weight = weight; // store latest (max index)
        }
    }

    public int F(string pref, string suff) {
        string key = suff + "{" + pref;
        TrieNode node = _root;
        foreach (char ch in key) {
            int idx = ch == '{' ? 26 : ch - 'a';
            if (node.Children[idx] == null) return -1;
            node = node.Children[idx];
        }
        return node.Weight;
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter obj = new WordFilter(words);
 * int param_1 = obj.F(pref,suff);
 */
```

## Javascript

```javascript
/**
 * @param {string[]} words
 */
var WordFilter = function(words) {
    const SEP = '{';
    const CHAR_COUNT = 27; // 26 letters + separator

    function charIdx(ch) {
        return ch === SEP ? 26 : ch.charCodeAt(0) - 97;
    }

    function Node() {
        this.children = new Array(CHAR_COUNT).fill(null);
        this.weight = -1;
    }

    this.root = new Node();

    for (let i = 0; i < words.length; ++i) {
        const w = words[i];
        const L = w.length;
        // insert all suffixes combined with separator and the whole word
        for (let j = 0; j <= L; ++j) {
            const suffix = w.slice(j); // may be empty when j==L
            const combo = suffix + SEP + w;
            let node = this.root;
            for (let k = 0; k < combo.length; ++k) {
                const idx = charIdx(combo.charAt(k));
                if (!node.children[idx]) node.children[idx] = new Node();
                node = node.children[idx];
                node.weight = i; // store latest index (max)
            }
        }
    }
};

/** 
 * @param {string} pref 
 * @param {string} suff
 * @return {number}
 */
WordFilter.prototype.f = function(pref, suff) {
    const SEP = '{';
    let node = this.root;
    const key = suff + SEP + pref;
    for (let i = 0; i < key.length; ++i) {
        const idx = key.charCodeAt(i) === 123 ? 26 : key.charCodeAt(i) - 97;
        if (!node.children[idx]) return -1;
        node = node.children[idx];
    }
    return node.weight;
};
```

## Typescript

```typescript
class TrieNode {
    children: (TrieNode | null)[];
    weight: number;
    constructor() {
        this.children = new Array(27).fill(null);
        this.weight = -1;
    }
}

function charIdx(ch: string): number {
    return ch === '#' ? 26 : ch.charCodeAt(0) - 97;
}

class WordFilter {
    private root: TrieNode;

    constructor(words: string[]) {
        this.root = new TrieNode();
        for (let i = 0; i < words.length; ++i) {
            const w = words[i];
            const len = w.length;
            for (let j = 0; j <= len; ++j) { // all suffixes including empty
                const suffix = w.substring(j);
                const combined = suffix + '#' + w;
                let node = this.root;
                for (let k = 0; k < combined.length; ++k) {
                    const id = charIdx(combined.charAt(k));
                    if (!node.children[id]) node.children[id] = new TrieNode();
                    node = node.children[id]!;
                    node.weight = i; // store latest index (max)
                }
            }
        }
    }

    f(pref: string, suff: string): number {
        const key = suff + '#' + pref;
        let node = this.root;
        for (let i = 0; i < key.length; ++i) {
            const id = charIdx(key.charAt(i));
            if (!node.children[id]) return -1;
            node = node.children[id]!;
        }
        return node.weight;
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * var obj = new WordFilter(words)
 * var param_1 = obj.f(pref,suff)
 */
```

## Php

```php
<?php
class WordFilter {
    private $trie = [];

    public function __construct($words) {
        // Initialize root node
        $this->trie[] = ['next' => [], 'weight' => -1];
        foreach ($words as $index => $word) {
            $len = strlen($word);
            // Insert all suffixes combined with '{' and the whole word
            for ($j = 0; $j <= $len; $j++) {
                $suffix = substr($word, $j);
                $combined = $suffix . '{' . $word;
                $this->insert($combined, $index);
            }
        }
    }

    private function insert(string $s, int $weight): void {
        $node = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (!isset($this->trie[$node]['next'][$c])) {
                $this->trie[] = ['next' => [], 'weight' => -1];
                $newIdx = count($this->trie) - 1;
                $this->trie[$node]['next'][$c] = $newIdx;
            }
            $node = $this->trie[$node]['next'][$c];
            // Store the latest (largest) index at each node
            $this->trie[$node]['weight'] = $weight;
        }
    }

    private function search(string $s): int {
        $node = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (!isset($this->trie[$node]['next'][$c])) {
                return -1;
            }
            $node = $this->trie[$node]['next'][$c];
        }
        return $this->trie[$node]['weight'];
    }

    public function f($pref, $suff) {
        $query = $suff . '{' . $pref;
        return $this->search($query);
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * $obj = new WordFilter($words);
 * $ret_1 = $obj->f($pref, $suff);
 */
?>
```

## Swift

```swift
class TrieNode {
    var child: [TrieNode?] = Array(repeating: nil, count: 27)
    var weight: Int = -1
}

class WordFilter {
    private let root = TrieNode()
    
    init(_ words: [String]) {
        for (idx, word) in words.enumerated() {
            let len = word.count
            for i in 0...len {
                let start = word.index(word.startIndex, offsetBy: i)
                let suffix = String(word[start...])
                let key = suffix + "{" + word
                insert(key, weight: idx)
            }
        }
    }
    
    private func charIdx(_ c: Character) -> Int {
        if c == "{" { return 26 }
        return Int(c.unicodeScalars.first!.value - 97)
    }
    
    private func insert(_ s: String, weight: Int) {
        var node = root
        for ch in s {
            let id = charIdx(ch)
            if node.child[id] == nil {
                node.child[id] = TrieNode()
            }
            node = node.child[id]!
            node.weight = weight
        }
    }
    
    func f(_ pref: String, _ suff: String) -> Int {
        let key = suff + "{" + pref
        var node = root
        for ch in key {
            let id = charIdx(ch)
            guard let next = node.child[id] else { return -1 }
            node = next
        }
        return node.weight
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * let obj = WordFilter(words)
 * let ret_1: Int = obj.f(pref, suff)
 */
```

## Kotlin

```kotlin
class WordFilter(words: Array<String>) {
    private val nodes = mutableListOf<TrieNode>()

    init {
        nodes.add(TrieNode())
        for ((idx, w) in words.withIndex()) {
            val len = w.length
            for (i in 0..len) {
                var cur = 0
                // suffix part
                for (j in i until len) {
                    cur = getOrCreate(cur, w[j])
                    nodes[cur].weight = idx
                }
                // separator '{'
                cur = getOrCreate(cur, '{')
                nodes[cur].weight = idx
                // whole word as prefix
                for (j in 0 until len) {
                    cur = getOrCreate(cur, w[j])
                    nodes[cur].weight = idx
                }
            }
        }
    }

    fun f(pref: String, suff: String): Int {
        var cur = 0
        // traverse suffix
        for (c in suff) {
            cur = getChild(cur, c) ?: return -1
        }
        // separator
        cur = getChild(cur, '{') ?: return -1
        // traverse prefix
        for (c in pref) {
            cur = getChild(cur, c) ?: return -1
        }
        return nodes[cur].weight
    }

    private fun charToIdx(c: Char): Int = if (c == '{') 26 else c - 'a'

    private fun getOrCreate(nodeIdx: Int, c: Char): Int {
        val ci = charToIdx(c)
        var next = nodes[nodeIdx].children[ci]
        if (next == -1) {
            next = nodes.size
            nodes.add(TrieNode())
            nodes[nodeIdx].children[ci] = next
        }
        return next
    }

    private fun getChild(nodeIdx: Int, c: Char): Int? {
        val ci = charToIdx(c)
        val nxt = nodes[nodeIdx].children[ci]
        return if (nxt == -1) null else nxt
    }

    private class TrieNode(var weight: Int = -1) {
        val children = IntArray(27) { -1 }
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * var obj = WordFilter(words)
 * var param_1 = obj.f(pref,suff)
 */
```

## Dart

```dart
class WordFilter {
  static const int _alphabetSize = 27; // 26 letters + '{'
  final TrieNode _root = TrieNode();

  WordFilter(List<String> words) {
    for (int weight = 0; weight < words.length; ++weight) {
      String word = words[weight];
      int len = word.length;
      // Insert all suffixes combined with the whole word
      for (int i = 0; i <= len; ++i) {
        String suffix = word.substring(i);
        String combined = suffix + '{' + word;
        _insert(combined, weight);
      }
    }
  }

  int f(String pref, String suff) {
    String key = suff + '{' + pref;
    TrieNode? node = _root;
    for (int i = 0; i < key.length; ++i) {
      int idx = _charToIndex(key.codeUnitAt(i));
      node = node!.children[idx];
      if (node == null) return -1;
    }
    return node.weight;
  }

  void _insert(String s, int weight) {
    TrieNode node = _root;
    for (int i = 0; i < s.length; ++i) {
      int idx = _charToIndex(s.codeUnitAt(i));
      node.children[idx] ??= TrieNode();
      node = node.children[idx]!;
      node.weight = weight; // always keep the latest (largest index)
    }
  }

  int _charToIndex(int codeUnit) {
    // '{' has ASCII code 123, which is just after 'z' (122)
    return codeUnit == 123 ? 26 : codeUnit - 97;
  }
}

class TrieNode {
  final List<TrieNode?> children = List.filled(WordFilter._alphabetSize, null);
  int weight = -1;
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter obj = WordFilter(words);
 * int param_1 = obj.f(pref,suff);
 */
```

## Golang

```go
type node struct {
	child  [27]int
	weight int
}

func newNode() node {
	n := node{weight: -1}
	for i := 0; i < 27; i++ {
		n.child[i] = -1
	}
	return n
}

type WordFilter struct {
	trie []node
}

func Constructor(words []string) WordFilter {
	wf := WordFilter{}
	wf.trie = make([]node, 1)
	wf.trie[0] = newNode()

	for idxWord, w := range words {
		L := len(w)
		for j := 0; j <= L; j++ { // each suffix start
			cur := 0 // root
			// insert suffix part w[j:]
			for k := j; k < L; k++ {
				c := int(w[k] - 'a')
				if wf.trie[cur].child[c] == -1 {
					wf.trie = append(wf.trie, newNode())
					wf.trie[cur].child[c] = len(wf.trie) - 1
				}
				cur = wf.trie[cur].child[c]
				if wf.trie[cur].weight < idxWord {
					wf.trie[cur].weight = idxWord
				}
			}
			// separator '{' -> index 26
			if wf.trie[cur].child[26] == -1 {
				wf.trie = append(wf.trie, newNode())
				wf.trie[cur].child[26] = len(wf.trie) - 1
			}
			cur = wf.trie[cur].child[26]
			if wf.trie[cur].weight < idxWord {
				wf.trie[cur].weight = idxWord
			}
			// insert whole word
			for k := 0; k < L; k++ {
				c := int(w[k] - 'a')
				if wf.trie[cur].child[c] == -1 {
					wf.trie = append(wf.trie, newNode())
					wf.trie[cur].child[c] = len(wf.trie) - 1
				}
				cur = wf.trie[cur].child[c]
				if wf.trie[cur].weight < idxWord {
					wf.trie[cur].weight = idxWord
				}
			}
		}
	}
	return wf
}

func (this *WordFilter) F(pref string, suff string) int {
	cur := 0
	// traverse suffix
	for i := 0; i < len(suff); i++ {
		c := int(suff[i] - 'a')
		if this.trie[cur].child[c] == -1 {
			return -1
		}
		cur = this.trie[cur].child[c]
	}
	// separator '{'
	if this.trie[cur].child[26] == -1 {
		return -1
	}
	cur = this.trie[cur].child[26]

	// traverse prefix
	for i := 0; i < len(pref); i++ {
		c := int(pref[i] - 'a')
		if this.trie[cur].child[c] == -1 {
			return -1
		}
		cur = this.trie[cur].child[c]
	}
	return this.trie[cur].weight
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * obj := Constructor(words);
 * param_1 := obj.F(pref,suff);
 */
```

## Ruby

```ruby
class TrieNode
  attr_accessor :children, :weight
  def initialize
    @children = Array.new(27)
    @weight = -1
  end
end

class WordFilter
  # :type words: String[]
  def initialize(words)
    @root = TrieNode.new
    words.each_with_index do |word, idx|
      l = word.length
      (0..l).each do |i|
        suffix = i == l ? "" : word[i..-1]
        combined = suffix + '{' + word
        node = @root
        combined.each_char do |ch|
          ci = ch == '{' ? 26 : (ch.ord - 97)
          child = node.children[ci]
          unless child
            child = TrieNode.new
            node.children[ci] = child
          end
          node = child
          node.weight = idx
        end
      end
    end
  end

  # :type pref: String
  # :type suff: String
  # :rtype: Integer
  def f(pref, suff)
    key = suff + '{' + pref
    node = @root
    key.each_char do |ch|
      ci = ch == '{' ? 26 : (ch.ord - 97)
      node = node.children[ci]
      return -1 unless node
    end
    node.weight
  end
end
```

## Scala

```scala
import scala.collection.mutable.ArrayBuffer

class WordFilter(_words: Array[String]) {

  private class Node {
    val children: Array[Int] = Array.fill(27)(-1)
    var weight: Int = -1
  }

  private val nodes: ArrayBuffer[Node] = ArrayBuffer(new Node())

  private def charIdx(c: Char): Int =
    if (c == '#') 26 else c - 'a'

  private def insert(s: String, w: Int): Unit = {
    var node = 0
    for (ch <- s) {
      val idx = charIdx(ch)
      var next = nodes(node).children(idx)
      if (next == -1) {
        nodes.append(new Node())
        next = nodes.length - 1
        nodes(node).children(idx) = next
      }
      node = next
      nodes(node).weight = w
    }
  }

  // Build trie with all suffix#word combinations
  for (i <- _words.indices) {
    val word = _words(i)
    val len = word.length
    for (j <- 0 to len) { // include empty suffix
      val combined = word.substring(j) + "#" + word
      insert(combined, i)
    }
  }

  def f(pref: String, suff: String): Int = {
    var node = 0
    val query = suff + "#" + pref
    for (ch <- query) {
      val idx = charIdx(ch)
      val next = nodes(node).children(idx)
      if (next == -1) return -1
      node = next
    }
    nodes(node).weight
  }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * val obj = new WordFilter(words)
 * val param_1 = obj.f(pref,suff)
 */
```

## Rust

```rust
use std::collections::HashMap;

struct WordFilter {
    map: HashMap<String, i32>,
}

impl WordFilter {
    fn new(words: Vec<String>) -> Self {
        let mut map: HashMap<String, i32> = HashMap::new();
        for (idx, w) in words.iter().enumerate() {
            let len = w.len();
            for p_len in 0..=len {
                let pref = &w[0..p_len];
                for s_len in 0..=len {
                    let suff = &w[len - s_len..];
                    let key = format!("{}#{}", pref, suff);
                    map.insert(key, idx as i32); // later indices overwrite earlier ones
                }
            }
        }
        WordFilter { map }
    }

    fn f(&self, pref: String, suff: String) -> i32 {
        let key = format!("{}#{}", pref, suff);
        *self.map.get(&key).unwrap_or(&-1)
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * let obj = WordFilter::new(words);
 * let ret_1: i32 = obj.f(pref, suff);
 */
```

## Racket

```racket
#lang racket

(struct trie-node (children weight) #:mutable)

(define word-filter%
  (class object%
    (super-new)
    
    ; words : (listof string?)
    (init-field
      words)
    
    ; root of the combined suffix+prefix trie
    (define root (trie-node (make-hash) -1))
    
    ;; insert a string into the trie, recording its index as weight
    (define (insert! s idx)
      (let loop ((node root) (pos 0))
        (set-trie-node-weight! node idx)
        (when (< pos (string-length s))
          (let* ([ch (string-ref s pos)]
                 [children (trie-node-children node)]
                 [child (hash-ref children ch #f)])
            (unless child
              (set! child (trie-node (make-hash) -1))
              (hash-set! children ch child))
            (loop child (+ pos 1))))))
    
    ;; build the trie using all words and their suffixes
    (begin
      (for ([w (in-list words)] [idx (in-naturals)])
        (let* ([len (string-length w)])
          (for ([i (in-range (+ len 1))]) ; include empty suffix
            (define suffix (substring w i len))
            (define combined (string-append suffix "{" w))
            (insert! combined idx)))))
    
    ;; f : string? string? -> exact-integer?
    (define/public (f pref suff)
      (let ([search (string-append suff "{" pref)])
        (let loop ((node root) (pos 0))
          (if (= pos (string-length search))
              (trie-node-weight node)
              (let* ([ch (string-ref search pos)]
                     [child (hash-ref (trie-node-children node) ch #f)])
                (if child
                    (loop child (+ pos 1))
                    -1))))))
    
    root)) ; dummy expression to end class body
```

## Erlang

```erlang
-module(wordfilter).
-export([word_filter_init_/1, word_filter_f/2]).

%% Initialize the WordFilter with a list of words.
-spec word_filter_init_(Words :: [unicode:unicode_binary()]) -> ok.
word_filter_init_(Words) ->
    Root = build_trie(Words),
    erlang:put(word_filter_trie, Root),
    ok.

%% Query for the maximum index of a word with given prefix and suffix.
-spec word_filter_f(Pref :: unicode:unicode_binary(), Suff :: unicode:unicode_binary()) -> integer().
word_filter_f(Pref, Suff) ->
    Trie = erlang:get(word_filter_trie),
    Sep = ${},
    PrefList = binary_to_list(Pref),
    SuffList = binary_to_list(Suff),
    Key = SuffList ++ [Sep] ++ PrefList,
    Weight = search(Key, Trie),
    case Weight of
        -1 -> -1;
        _  -> Weight
    end.

%% Build the combined trie from all words.
build_trie(Words) ->
    EmptyNode = #{children => #{}, weight => -1},
    build_trie(Words, 0, EmptyNode).

build_trie([], _Idx, Trie) ->
    Trie;
build_trie([WordBin | Rest], Idx, Trie) ->
    WordList = binary_to_list(WordBin),
    Sep = ${},
    UpdatedTrie = insert_all_suffixes(WordList, Sep, WordList, Idx, Trie),
    build_trie(Rest, Idx + 1, UpdatedTrie).

%% Insert all suffix+separator+word combinations for a single word.
insert_all_suffixes(_Word, _Sep, _FullWord, _Weight, Trie) when length(_Word) =:= 0 ->
    Trie;
insert_all_suffixes(WordList, Sep, FullWord, Weight, Trie) ->
    Len = length(WordList),
    Positions = lists:seq(0, Len),
    lists:foldl(fun(Pos, AccTrie) ->
        Suffix = lists:nthtail(Pos, WordList), % empty when Pos == Len
        Combined = Suffix ++ [Sep] ++ FullWord,
        insert(Combined, Weight, AccTrie)
    end, Trie, Positions).

%% Insert a character list into the trie, updating weight.
insert([], Weight, Node) ->
    CurWeight = maps:get(weight, Node, -1),
    NewWeight = if Weight > CurWeight -> Weight; true -> CurWeight end,
    maps:put(weight, NewWeight, Node);
insert([C | Rest], Weight, Node) ->
    CurWeight = maps:get(weight, Node, -1),
    NewWeight = if Weight > CurWeight -> Weight; true -> CurWeight end,
    Node1 = maps:put(weight, NewWeight, Node),
    Children = maps:get(children, Node1, #{}),
    ChildNode0 = maps:get(C, Children, #{children => #{}, weight => -1}),
    UpdatedChild = insert(Rest, Weight, ChildNode0),
    NewChildren = maps:put(C, UpdatedChild, Children),
    maps:put(children, NewChildren, Node1).

%% Search for a key in the trie and return stored weight or -1.
search([], Node) ->
    maps:get(weight, Node, -1);
search([C | Rest], Node) ->
    Children = maps:get(children, Node, #{}),
    case maps:find(C, Children) of
        error -> -1;
        {ok, ChildNode} -> search(Rest, ChildNode)
    end.
```

## Elixir

```elixir
defmodule WordFilter do
  @spec init_(words :: [String.t()]) :: any()
  def init_(words) do
    root = new_node()

    Enum.with_index(words)
    |> Enum.reduce(root, fn {word, idx}, acc_root ->
      len = String.length(word)

      0..len
      |> Enum.reduce(acc_root, fn j, cur_root ->
        suffix = String.slice(word, j, len - j)
        combined = suffix <> "{" <> word
        insert(cur_root, combined, idx)
      end)
    end)
    |> then(&Process.put(:trie_root, &1))
  end

  @spec f(pref :: String.t(), suff :: String.t()) :: integer()
  def f(pref, suff) do
    root = Process.get(:trie_root)

    case traverse(root, suff <> "{" <> pref) do
      nil -> -1
      node -> node.weight
    end
  end

  # Private helpers

  defp new_node do
    %{children: %{}, weight: -1}
  end

  defp insert(node, "", weight) do
    %{node | weight: weight}
  end

  defp insert(node, <<char::utf8, rest::binary>>, weight) do
    child = Map.get(node.children, char, new_node())
    updated_child = insert(child, rest, weight)

    %{
      node
      | children: Map.put(node.children, char, updated_child),
        weight: weight
    }
  end

  defp traverse(nil, _), do: nil
  defp traverse(node, ""), do: node

  defp traverse(node, <<char::utf8, rest::binary>>) do
    child = Map.get(node.children, char)
    traverse(child, rest)
  end
end
```
