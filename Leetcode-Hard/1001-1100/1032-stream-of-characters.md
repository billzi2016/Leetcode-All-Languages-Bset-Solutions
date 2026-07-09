# 1032. Stream of Characters

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class StreamChecker {
    struct Node {
        bool end = false;
        Node* nxt[26];
        Node() { memset(nxt, 0, sizeof(nxt)); }
    };
    Node* root;
    int maxLen;
    deque<char> recent;
public:
    StreamChecker(vector<string>& words) {
        root = new Node();
        maxLen = 0;
        for (const string& w : words) {
            maxLen = max(maxLen, (int)w.size());
            Node* cur = root;
            for (int i = (int)w.size() - 1; i >= 0; --i) {
                int c = w[i] - 'a';
                if (!cur->nxt[c]) cur->nxt[c] = new Node();
                cur = cur->nxt[c];
            }
            cur->end = true;
        }
    }

    bool query(char letter) {
        recent.push_back(letter);
        if ((int)recent.size() > maxLen) recent.pop_front();

        Node* cur = root;
        for (auto it = recent.rbegin(); it != recent.rend(); ++it) {
            int c = *it - 'a';
            if (!cur->nxt[c]) return false;
            cur = cur->nxt[c];
            if (cur->end) return true;
        }
        return false;
    }
};

/**
 * Your StreamChecker object will be instantiated and called as such:
 * StreamChecker* obj = new StreamChecker(words);
 * bool param_1 = obj->query(letter);
 */
```

## Java

```java
class StreamChecker {
    private static class Node {
        Node[] child = new Node[26];
        boolean isWord;
    }

    private final Node root = new Node();
    private final StringBuilder stream = new StringBuilder();
    private final int maxLen;

    public StreamChecker(String[] words) {
        int ml = 0;
        for (String w : words) {
            ml = Math.max(ml, w.length());
            Node node = root;
            // insert reversed word
            for (int i = w.length() - 1; i >= 0; --i) {
                int idx = w.charAt(i) - 'a';
                if (node.child[idx] == null) node.child[idx] = new Node();
                node = node.child[idx];
            }
            node.isWord = true;
        }
        maxLen = ml;
    }

    public boolean query(char letter) {
        stream.append(letter);
        // keep only the last maxLen characters
        if (stream.length() > maxLen) {
            stream.deleteCharAt(0);
        }
        Node node = root;
        for (int i = stream.length() - 1; i >= 0; --i) {
            int idx = stream.charAt(i) - 'a';
            node = node.child[idx];
            if (node == null) return false;
            if (node.isWord) return true;
        }
        return false;
    }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * StreamChecker obj = new StreamChecker(words);
 * boolean param_1 = obj.query(letter);
 */
```

## Python

```python
from collections import deque

class StreamChecker(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = {}
        self.max_len = 0
        for w in words:
            self.max_len = max(self.max_len, len(w))
            node = self.trie
            for ch in reversed(w):
                node = node.setdefault(ch, {})
            node['_end'] = True
        self.buffer = deque(maxlen=self.max_len)

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.buffer.append(letter)
        node = self.trie
        for ch in reversed(self.buffer):
            if ch not in node:
                return False
            node = node[ch]
            if '_end' in node:
                return True
        return False
```

## Python3

```python
class StreamChecker:
    class Node:
        __slots__ = ("children", "is_word")
        def __init__(self):
            self.children = {}
            self.is_word = False

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = self.Node()
        self.max_len = 0
        for w in words:
            self.max_len = max(self.max_len, len(w))
            node = self.root
            # insert reversed word
            for ch in reversed(w):
                if ch not in node.children:
                    node.children[ch] = self.Node()
                node = node.children[ch]
            node.is_word = True

        from collections import deque
        self.buffer = deque([], maxlen=self.max_len)

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.buffer.append(letter)
        node = self.root
        for ch in reversed(self.buffer):
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.is_word:
                return True
        return False
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct TrieNode {
    int child[26];
    bool isEnd;
} TrieNode;

typedef struct {
    TrieNode *nodes;
    int nodeCount;
    int maxLen;
    char *buf;
    int len;
} StreamChecker;

/* Create a new trie node and return its index */
static int createNode(StreamChecker *obj) {
    ++obj->nodeCount;
    TrieNode *n = &obj->nodes[obj->nodeCount];
    n->isEnd = false;
    for (int i = 0; i < 26; ++i) n->child[i] = -1;
    return obj->nodeCount;
}

/* Insert a word reversed into the trie */
static void insertReversed(StreamChecker *obj, const char *word) {
    int idx = 0; // root
    int wlen = (int)strlen(word);
    for (int i = wlen - 1; i >= 0; --i) {
        int c = word[i] - 'a';
        if (obj->nodes[idx].child[c] == -1) {
            obj->nodes[idx].child[c] = createNode(obj);
        }
        idx = obj->nodes[idx].child[c];
    }
    obj->nodes[idx].isEnd = true;
}

/** Initialize your data structure here. */
StreamChecker* streamCheckerCreate(char** words, int wordsSize) {
    StreamChecker *obj = (StreamChecker *)malloc(sizeof(StreamChecker));
    if (!obj) return NULL;

    // Determine total characters and max word length
    int totalChars = 0;
    int maxLen = 0;
    for (int i = 0; i < wordsSize; ++i) {
        int l = (int)strlen(words[i]);
        totalChars += l;
        if (l > maxLen) maxLen = l;
    }

    obj->maxLen = maxLen;
    obj->len = 0;
    obj->buf = (char *)malloc(sizeof(char) * maxLen);
    obj->nodes = (TrieNode *)malloc(sizeof(TrieNode) * (totalChars + 1));
    obj->nodeCount = 0;

    // Initialize root node
    obj->nodes[0].isEnd = false;
    for (int i = 0; i < 26; ++i) obj->nodes[0].child[i] = -1;

    // Insert all words reversed
    for (int i = 0; i < wordsSize; ++i) {
        insertReversed(obj, words[i]);
    }

    return obj;
}

/** Query the next letter in the stream. */
bool streamCheckerQuery(StreamChecker* obj, char letter) {
    if (obj->len < obj->maxLen) {
        obj->buf[obj->len++] = letter;
    } else {
        memmove(obj->buf, obj->buf + 1, obj->maxLen - 1);
        obj->buf[obj->maxLen - 1] = letter;
    }

    int nodeIdx = 0;
    for (int i = obj->len - 1; i >= 0; --i) {
        int c = obj->buf[i] - 'a';
        int child = obj->nodes[nodeIdx].child[c];
        if (child == -1) break;
        nodeIdx = child;
        if (obj->nodes[nodeIdx].isEnd) return true;
    }
    return false;
}

void streamCheckerFree(StreamChecker* obj) {
    if (!obj) return;
    free(obj->buf);
    free(obj->nodes);
    free(obj);
}

/**
 * Your StreamChecker struct will be instantiated and called as such:
 * StreamChecker* obj = streamCheckerCreate(words, wordsSize);
 * bool param_1 = streamCheckerQuery(obj, letter);
 * streamCheckerFree(obj);
 */
```

## Csharp

```csharp
public class StreamChecker {
    private class TrieNode {
        public TrieNode[] Children = new TrieNode[26];
        public bool IsEnd;
    }

    private readonly TrieNode _root = new TrieNode();
    private readonly int _maxLen;
    private readonly System.Collections.Generic.List<char> _stream = new System.Collections.Generic.List<char>();

    public StreamChecker(string[] words) {
        int max = 0;
        foreach (var w in words) {
            if (w.Length > max) max = w.Length;
            TrieNode node = _root;
            // insert reversed word
            for (int i = w.Length - 1; i >= 0; i--) {
                int idx = w[i] - 'a';
                if (node.Children[idx] == null) node.Children[idx] = new TrieNode();
                node = node.Children[idx];
            }
            node.IsEnd = true;
        }
        _maxLen = max;
    }

    public bool Query(char letter) {
        _stream.Add(letter);
        if (_stream.Count > _maxLen) {
            _stream.RemoveAt(0); // keep only recent characters up to max length
        }

        TrieNode node = _root;
        for (int i = _stream.Count - 1; i >= 0; i--) {
            int idx = _stream[i] - 'a';
            if (node.Children[idx] == null) return false;
            node = node.Children[idx];
            if (node.IsEnd) return true;
        }
        return false;
    }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * StreamChecker obj = new StreamChecker(words);
 * bool param_1 = obj.Query(letter);
 */
```

## Javascript

```javascript
/**
 * @param {string[]} words
 */
var StreamChecker = function(words) {
    this.trie = {};
    this.maxLen = 0;
    for (const w of words) {
        let node = this.trie;
        const rev = w.split('').reverse();
        for (const ch of rev) {
            if (!node[ch]) node[ch] = {};
            node = node[ch];
        }
        node.isEnd = true;
        this.maxLen = Math.max(this.maxLen, w.length);
    }
    this.stream = [];
};

/** 
 * @param {character} letter
 * @return {boolean}
 */
StreamChecker.prototype.query = function(letter) {
    this.stream.push(letter);
    let node = this.trie;
    for (let i = this.stream.length - 1, steps = 0; i >= 0 && steps < this.maxLen; i--, steps++) {
        const ch = this.stream[i];
        if (!node[ch]) return false;
        node = node[ch];
        if (node.isEnd) return true;
    }
    return false;
};
```

## Typescript

```typescript
class TrieNode {
    children: { [key: string]: TrieNode } = {};
    isWord: boolean = false;
}
 
class StreamChecker {
    private root: TrieNode = new TrieNode();
    private stream: string[] = [];
    private maxLen: number = 0;
 
    constructor(words: string[]) {
        for (const w of words) {
            this.maxLen = Math.max(this.maxLen, w.length);
            let node = this.root;
            // insert reversed word
            for (let i = w.length - 1; i >= 0; --i) {
                const ch = w[i];
                if (!node.children[ch]) node.children[ch] = new TrieNode();
                node = node.children[ch];
            }
            node.isWord = true;
        }
    }
 
    query(letter: string): boolean {
        this.stream.push(letter);
        let node = this.root;
        // traverse from newest character backwards, up to maxLen
        for (let i = this.stream.length - 1, steps = 0; i >= 0 && steps < this.maxLen; --i, ++steps) {
            const ch = this.stream[i];
            if (!node.children[ch]) return false;
            node = node.children[ch];
            if (node.isWord) return true;
        }
        return false;
    }
}
 
/**
 * Your StreamChecker object will be instantiated and called as such:
 * var obj = new StreamChecker(words)
 * var param_1 = obj.query(letter)
 */
```

## Php

```php
class StreamChecker {
    private array $trie;
    private string $stream = '';
    private int $maxLen = 0;

    /**
     * @param String[] $words
     */
    public function __construct($words) {
        $this->trie = ['next' => [], 'end' => false];
        foreach ($words as $word) {
            $len = strlen($word);
            if ($len > $this->maxLen) {
                $this->maxLen = $len;
            }
            $node =& $this->trie;
            for ($i = $len - 1; $i >= 0; --$i) {
                $c = $word[$i];
                if (!isset($node['next'][$c])) {
                    $node['next'][$c] = ['next' => [], 'end' => false];
                }
                $node =& $node['next'][$c];
            }
            $node['end'] = true;
        }
    }

    /**
     * @param String $letter
     * @return Boolean
     */
    public function query($letter) {
        $this->stream = $letter . $this->stream;
        if (strlen($this->stream) > $this->maxLen) {
            $this->stream = substr($this->stream, 0, $this->maxLen);
        }

        $node = $this->trie;
        $len = strlen($this->stream);
        for ($i = 0; $i < $len; ++$i) {
            $c = $this->stream[$i];
            if (!isset($node['next'][$c])) {
                return false;
            }
            $node = $node['next'][$c];
            if ($node['end']) {
                return true;
            }
        }
        return false;
    }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * $obj = new StreamChecker($words);
 * $ret_1 = $obj->query($letter);
 */
```

## Swift

```swift
class StreamChecker {
    private class TrieNode {
        var children: [TrieNode?]
        var isWord: Bool
        init() {
            self.children = Array(repeating: nil, count: 26)
            self.isWord = false
        }
    }

    private let root = TrieNode()
    private var stream: [UInt8] = []
    private let maxLen: Int

    init(_ words: [String]) {
        var m = 0
        for w in words {
            m = max(m, w.count)
            var node = root
            for ch in w.reversed() {
                let idx = Int(ch.asciiValue! - 97)
                if node.children[idx] == nil {
                    node.children[idx] = TrieNode()
                }
                node = node.children[idx]!
            }
            node.isWord = true
        }
        self.maxLen = m
    }

    func query(_ letter: Character) -> Bool {
        let idx = UInt8(letter.asciiValue! - 97)
        stream.append(idx)
        if stream.count > maxLen {
            stream.removeFirst(stream.count - maxLen)
        }
        var node = root
        for i in stride(from: stream.count - 1, through: 0, by: -1) {
            let childIdx = Int(stream[i])
            guard let next = node.children[childIdx] else { break }
            node = next
            if node.isWord { return true }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class StreamChecker(words: Array<String>) {
    private class Node {
        val children = arrayOfNulls<Node>(26)
        var isWord: Boolean = false
    }

    private val root = Node()
    private val maxLen: Int
    private val stream = StringBuilder()

    init {
        var ml = 0
        for (w in words) {
            ml = kotlin.math.max(ml, w.length)
            var node = root
            for (i in w.length - 1 downTo 0) {
                val idx = w[i] - 'a'
                if (node.children[idx] == null) {
                    node.children[idx] = Node()
                }
                node = node.children[idx]!!
            }
            node.isWord = true
        }
        maxLen = ml
    }

    fun query(letter: Char): Boolean {
        stream.append(letter)
        if (stream.length > maxLen) {
            stream.delete(0, stream.length - maxLen)
        }
        var node = root
        for (i in stream.length - 1 downTo 0) {
            val idx = stream[i] - 'a'
            node = node.children[idx] ?: return false
            if (node.isWord) return true
        }
        return false
    }
}
```

## Dart

```dart
class TrieNode {
  final List<TrieNode?> children = List.filled(26, null);
  bool isWord = false;
}

class StreamChecker {
  final TrieNode _root = TrieNode();
  final List<int> _stream = [];
  int _maxLen = 0;

  StreamChecker(List<String> words) {
    for (var w in words) {
      if (w.length > _maxLen) _maxLen = w.length;
      var node = _root;
      for (int i = w.length - 1; i >= 0; --i) {
        int idx = w.codeUnitAt(i) - 97;
        node.children[idx] ??= TrieNode();
        node = node.children[idx]!;
      }
      node.isWord = true;
    }
  }

  bool query(String letter) {
    int idx = letter.codeUnitAt(0) - 97;
    _stream.add(idx);
    var node = _root;
    int steps = 0;
    for (int i = _stream.length - 1; i >= 0 && steps < _maxLen; --i, ++steps) {
      int c = _stream[i];
      if (node.children[c] == null) return false;
      node = node.children[c]!;
      if (node.isWord) return true;
    }
    return false;
  }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * StreamChecker obj = StreamChecker(words);
 * bool param1 = obj.query(letter);
 */
```

## Golang

```go
type Node struct {
	child  [26]*Node
	isWord bool
}

type StreamChecker struct {
	root   *Node
	stream []byte
	maxLen int
}

/** Initialize your data structure here. */
func Constructor(words []string) StreamChecker {
	root := &Node{}
	maxL := 0
	for _, w := range words {
		if len(w) > maxL {
			maxL = len(w)
		}
		node := root
		// insert reversed word
		for i := len(w) - 1; i >= 0; i-- {
			c := w[i] - 'a'
			if node.child[c] == nil {
				node.child[c] = &Node{}
			}
			node = node.child[c]
		}
		node.isWord = true
	}
	return StreamChecker{
		root:   root,
		maxLen: maxL,
	}
}

func (this *StreamChecker) Query(letter byte) bool {
	this.stream = append(this.stream, letter)
	node := this.root
	// traverse from newest character backwards, up to maxLen
	for i := len(this.stream) - 1; i >= 0 && (len(this.stream)-i) <= this.maxLen; i-- {
		c := this.stream[i] - 'a'
		if node.child[c] == nil {
			return false
		}
		node = node.child[c]
		if node.isWord {
			return true
		}
	}
	return false
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * obj := Constructor(words);
 * param_1 := obj.Query(letter);
 */
```

## Ruby

```ruby
class Node
  attr_accessor :children, :is_word
  def initialize
    @children = Array.new(26)
    @is_word = false
  end
end

class StreamChecker
  # :type words: String[]
  def initialize(words)
    @root = Node.new
    @max_len = 0
    words.each do |w|
      @max_len = [@max_len, w.length].max
      node = @root
      w.reverse.each_char do |ch|
        idx = ch.ord - 97
        node.children[idx] ||= Node.new
        node = node.children[idx]
      end
      node.is_word = true
    end
    @stream = []
  end

  # :type letter: Character
  # :rtype: Boolean
  def query(letter)
    @stream << letter
    if @stream.size > @max_len
      @stream.shift
    end
    node = @root
    @stream.reverse_each do |ch|
      idx = ch.ord - 97
      node = node.children[idx]
      return false unless node
      return true if node.is_word
    end
    false
  end
end
```

## Scala

```scala
import scala.collection.mutable.ArrayDeque

class StreamChecker(_words: Array[String]) {

  private class Node {
    val child: Array[Node] = new Array[Node](26)
    var end: Boolean = false
  }

  private val root = new Node
  private val maxLen: Int = if (_words.isEmpty) 0 else _words.map(_.length).max
  private val buffer = ArrayDeque.empty[Char]

  // Build reversed trie
  for (w <- _words) {
    var node = root
    for (c <- w.reverse) {
      val idx = c - 'a'
      if (node.child(idx) == null) node.child(idx) = new Node
      node = node.child(idx)
    }
    node.end = true
  }

  def query(letter: Char): Boolean = {
    buffer.prepend(letter)
    if (buffer.length > maxLen) buffer.removeLast()

    var node = root
    for (c <- buffer) {
      val idx = c - 'a'
      node = node.child(idx)
      if (node == null) return false
      if (node.end) return true
    }
    false
  }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * val obj = new StreamChecker(words)
 * val param_1 = obj.query(letter)
 */
```

## Rust

```rust
use std::cell::RefCell;
use std::collections::VecDeque;

#[derive(Clone)]
struct Node {
    next: [i32; 26],
    is_word: bool,
}

impl Node {
    fn new() -> Self {
        Node {
            next: [-1; 26],
            is_word: false,
        }
    }
}

struct StreamChecker {
    nodes: Vec<Node>,
    buffer: RefCell<VecDeque<char>>,
    max_len: usize,
}

impl StreamChecker {
    fn new(words: Vec<String>) -> Self {
        let mut nodes = Vec::new();
        nodes.push(Node::new()); // root
        let mut max_len = 0usize;

        for w in words.iter() {
            if w.len() > max_len {
                max_len = w.len();
            }
            let mut idx = 0usize;
            for ch in w.chars().rev() {
                let c_idx = (ch as u8 - b'a') as usize;
                let next = nodes[idx].next[c_idx];
                if next == -1 {
                    nodes.push(Node::new());
                    let new_idx = (nodes.len() - 1) as i32;
                    nodes[idx].next[c_idx] = new_idx;
                }
                idx = nodes[idx].next[c_idx] as usize;
            }
            nodes[idx].is_word = true;
        }

        StreamChecker {
            nodes,
            buffer: RefCell::new(VecDeque::new()),
            max_len,
        }
    }

    fn query(&self, letter: char) -> bool {
        {
            let mut buf = self.buffer.borrow_mut();
            buf.push_back(letter);
            if buf.len() > self.max_len {
                buf.pop_front();
            }
        }

        let buf = self.buffer.borrow();
        let mut node_idx = 0usize;
        for &ch in buf.iter().rev() {
            let c_idx = (ch as u8 - b'a') as usize;
            let next = self.nodes[node_idx].next[c_idx];
            if next == -1 {
                return false;
            }
            node_idx = next as usize;
            if self.nodes[node_idx].is_word {
                return true;
            }
        }
        false
    }
}

/**
 * Your StreamChecker object will be instantiated and called as such:
 * let obj = StreamChecker::new(words);
 * let ret_1: bool = obj.query(letter);
 */
```

## Racket

```racket
(require racket/list)

(define stream-checker%
  (class object%
    (super-new)
    
    ; words : (listof string?)
    (init-field
      words)
    
    ; internal fields
    (define maxlen 0)
    (define root (make-hash))
    (define buffer '())
    
    ;; build reversed trie and compute maximum word length
    (for ([w words])
      (set! maxlen (max maxlen (string-length w)))
      (let ([node root])
        (for ([c (in-list (reverse (string->list w)))])
          (unless (hash-has-key? node c)
            (hash-set! node c (make-hash)))
          (set! node (hash-ref node c)))
        (hash-set! node '*end* #t)))
    
    ;; query : char? -> boolean?
    (define/public (query letter)
      (set! buffer (cons letter buffer))
      (when (> (length buffer) maxlen)
        (set! buffer (take buffer maxlen))) ; keep only recent maxlen chars
      (let loop ([node root] [chars buffer])
        (cond
          [(null? chars) #f]
          [else
           (define c (car chars))
           (if (hash-has-key? node c)
               (let ([next (hash-ref node c)])
                 (if (hash-has-key? next '*end*)
                     #t
                     (loop next (cdr chars))))
               #f)])))
    ))
```

## Erlang

```erlang
-module(stream_of_characters).
-export([stream_checker_init_/1, stream_checker_query/1]).

%% Initialize the StreamChecker with a list of words.
-spec stream_checker_init_(Words :: [unicode:unicode_binary()]) -> any().
stream_checker_init_(Words) ->
    Root = build_trie(Words, #{}),
    MaxLen = max_word_len(Words, 0),
    put(trie, Root),
    put(max_len, MaxLen),
    put(stream, []).

%% Query a single character and return true if any suffix matches a word.
-spec stream_checker_query(Letter :: char()) -> boolean().
stream_checker_query(Letter) ->
    Stream0 = get(stream, []),
    MaxLen = get(max_len),
    NewStream = [Letter | Stream0],
    TruncStream = case length(NewStream) > MaxLen of
        true -> lists:sublist(NewStream, MaxLen);
        false -> NewStream
    end,
    put(stream, TruncStream),
    Trie = get(trie),
    check_suffix(TruncStream, Trie).

%% Build a reversed trie from the list of words.
build_trie([], Trie) ->
    Trie;
build_trie([WordBin | Rest], Trie) ->
    Chars = binary_to_list(WordBin),
    RevChars = lists:reverse(Chars),
    NewTrie = insert_word(RevChars, Trie),
    build_trie(Rest, NewTrie).

%% Insert a reversed word into the trie.
insert_word([], Node) ->
    maps:put('$', true, Node);
insert_word([C | Rest], Node) ->
    Child = maps:get(C, Node, #{}),
    UpdatedChild = insert_word(Rest, Child),
    maps:put(C, UpdatedChild, Node).

%% Compute maximum word length.
max_word_len([], Max) -> Max;
max_word_len([WordBin | Rest], CurrentMax) ->
    Len = byte_size(WordBin),
    NewMax = case Len > CurrentMax of
        true -> Len;
        false -> CurrentMax
    end,
    max_word_len(Rest, NewMax).

%% Check if any prefix of the reversed stream matches a word in the trie.
check_suffix([], _) -> false;
check_suffix([C | Rest], Node) ->
    case maps:find(C, Node) of
        error -> false;
        {ok, Child} ->
            case maps:is_key('$', Child) of
                true -> true;
                false -> check_suffix(Rest, Child)
            end
    end.
```

## Elixir

```elixir
defmodule StreamChecker do
  @spec init_(words :: [String.t()]) :: :ok
  def init_(words) do
    rev_set = MapSet.new(Enum.map(words, &String.reverse/1))
    max_len = words |> Enum.map(&String.length/1) |> Enum.max()
    state = %{set: rev_set, max_len: max_len, buffer: []}
    Process.put({__MODULE__, :state}, state)
    :ok
  end

  @spec query(letter :: String.t()) :: boolean
  def query(letter) do
    state = Process.get({__MODULE__, :state})
    buffer = [letter | state.buffer]

    buffer =
      if length(buffer) > state.max_len do
        Enum.take(buffer, state.max_len)
      else
        buffer
      end

    found =
      Enum.any?(1..state.max_len, fn len ->
        candidate = buffer |> Enum.take(len) |> List.to_string()
        MapSet.member?(state.set, candidate)
      end)

    Process.put({__MODULE__, :state}, %{state | buffer: buffer})
    found
  end
end
```
