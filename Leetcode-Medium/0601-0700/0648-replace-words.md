# 0648. Replace Words

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    TrieNode* child[26];
    bool end;
    TrieNode() : end(false) {
        memset(child, 0, sizeof(child));
    }
};

class Trie {
public:
    TrieNode* root;
    Trie() { root = new TrieNode(); }
    
    void insert(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!node->child[idx]) node->child[idx] = new TrieNode();
            node = node->child[idx];
        }
        node->end = true;
    }
    
    string shortestRoot(const string& word) const {
        TrieNode* node = root;
        string prefix;
        for (char c : word) {
            int idx = c - 'a';
            if (!node->child[idx]) return word;
            node = node->child[idx];
            prefix.push_back(c);
            if (node->end) return prefix;
        }
        return word;
    }
};

class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        Trie trie;
        for (const string& root : dictionary) trie.insert(root);
        
        istringstream iss(sentence);
        string word, result;
        bool first = true;
        while (iss >> word) {
            string rep = trie.shortestRoot(word);
            if (!first) result.push_back(' ');
            result += rep;
            first = false;
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    private static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd;
    }

    private final TrieNode root = new TrieNode();

    private void insert(String word) {
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

    private String shortestRoot(String word) {
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++) {
            int idx = word.charAt(i) - 'a';
            if (node.children[idx] == null) {
                return word;
            }
            node = node.children[idx];
            if (node.isEnd) {
                return word.substring(0, i + 1);
            }
        }
        return word;
    }

    public String replaceWords(java.util.List<String> dictionary, String sentence) {
        for (String root : dictionary) {
            insert(root);
        }
        String[] words = sentence.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < words.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(shortestRoot(words[i]));
        }
        return sb.toString();
    }
}
```

## Python

```python
class TrieNode:
    __slots__ = ('children', 'is_end')
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        root = TrieNode()
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        result = []
        for w in sentence.split():
            node = root
            prefix = []
            replaced = False
            for ch in w:
                if ch not in node.children:
                    break
                node = node.children[ch]
                prefix.append(ch)
                if node.is_end:
                    result.append(''.join(prefix))
                    replaced = True
                    break
            if not replaced:
                result.append(w)

        return ' '.join(result)
```

## Python3

```python
from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        class TrieNode:
            __slots__ = ('children', 'is_end')
            def __init__(self):
                self.children = {}
                self.is_end = False

        root = TrieNode()
        # Build trie
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        def shortest_root(word: str) -> str:
            node = root
            prefix_chars = []
            for ch in word:
                if ch not in node.children:
                    break
                node = node.children[ch]
                prefix_chars.append(ch)
                if node.is_end:
                    return ''.join(prefix_chars)
            return word

        words = sentence.split()
        replaced = [shortest_root(w) for w in words]
        return ' '.join(replaced)
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

static TrieNode* newNode(void) {
    TrieNode *node = (TrieNode *)malloc(sizeof(TrieNode));
    if (!node) return NULL;
    node->isEnd = false;
    for (int i = 0; i < 26; ++i) node->child[i] = NULL;
    return node;
}

static void insertWord(TrieNode *root, const char *word) {
    TrieNode *cur = root;
    while (*word) {
        int idx = *word - 'a';
        if (idx < 0 || idx >= 26) { word++; continue; } // safety
        if (!cur->child[idx]) cur->child[idx] = newNode();
        cur = cur->child[idx];
        ++word;
    }
    cur->isEnd = true;
}

static int shortestRootLen(TrieNode *root, const char *s, int len) {
    TrieNode *cur = root;
    for (int i = 0; i < len; ++i) {
        int idx = s[i] - 'a';
        if (idx < 0 || idx >= 26) return 0;
        if (!cur->child[idx]) return 0;
        cur = cur->child[idx];
        if (cur->isEnd) return i + 1; // length of root
    }
    return 0;
}

static void freeTrie(TrieNode *node) {
    if (!node) return;
    for (int i = 0; i < 26; ++i) {
        if (node->child[i]) freeTrie(node->child[i]);
    }
    free(node);
}

/* LeetCode entry point */
char* replaceWords(char** dictionary, int dictionarySize, char* sentence) {
    TrieNode *root = newNode();
    for (int i = 0; i < dictionarySize; ++i) {
        insertWord(root, dictionary[i]);
    }

    size_t n = strlen(sentence);
    char *result = (char *)malloc(n + 1);
    int pos = 0;
    int i = 0;

    while (sentence[i]) {
        if (sentence[i] == ' ') {
            result[pos++] = ' ';
            ++i;
            continue;
        }
        int start = i;
        while (sentence[i] && sentence[i] != ' ') ++i;
        int wlen = i - start;
        int rlen = shortestRootLen(root, sentence + start, wlen);
        int copyLen = rlen ? rlen : wlen;
        memcpy(result + pos, sentence + start, copyLen);
        pos += copyLen;
    }
    result[pos] = '\0';

    freeTrie(root);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    private class TrieNode
    {
        public TrieNode[] Children = new TrieNode[26];
        public bool IsEnd;
    }

    private readonly TrieNode _root = new TrieNode();

    private void Insert(string word)
    {
        var node = _root;
        foreach (char ch in word)
        {
            int idx = ch - 'a';
            if (node.Children[idx] == null) node.Children[idx] = new TrieNode();
            node = node.Children[idx];
        }
        node.IsEnd = true;
    }

    private string FindRoot(string word)
    {
        var node = _root;
        for (int i = 0; i < word.Length; i++)
        {
            int idx = word[i] - 'a';
            if (node.Children[idx] == null) return word;
            node = node.Children[idx];
            if (node.IsEnd) return word.Substring(0, i + 1);
        }
        return word;
    }

    public string ReplaceWords(IList<string> dictionary, string sentence)
    {
        foreach (var w in dictionary) Insert(w);

        var words = sentence.Split(' ');
        var sb = new System.Text.StringBuilder();

        for (int i = 0; i < words.Length; i++)
        {
            if (i > 0) sb.Append(' ');
            sb.Append(FindRoot(words[i]));
        }

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} dictionary
 * @param {string} sentence
 * @return {string}
 */
var replaceWords = function(dictionary, sentence) {
    // Trie node constructor
    function Node() {
        this.children = Object.create(null);
        this.isEnd = false;
    }

    const root = new Node();

    // Build trie
    for (const word of dictionary) {
        let cur = root;
        for (let i = 0; i < word.length; ++i) {
            const ch = word[i];
            if (!cur.children[ch]) {
                cur.children[ch] = new Node();
            }
            cur = cur.children[ch];
        }
        cur.isEnd = true;
    }

    // Find shortest root for a given word
    function getRoot(word) {
        let cur = root;
        for (let i = 0; i < word.length; ++i) {
            const ch = word[i];
            if (!cur.children[ch]) break;
            cur = cur.children[ch];
            if (cur.isEnd) return word.slice(0, i + 1);
        }
        return word;
    }

    const words = sentence.split(' ');
    for (let i = 0; i < words.length; ++i) {
        words[i] = getRoot(words[i]);
    }
    return words.join(' ');
};
```

## Typescript

```typescript
function replaceWords(dictionary: string[], sentence: string): string {
    class TrieNode {
        children: (TrieNode | null)[];
        isEnd: boolean;
        constructor() {
            this.children = new Array(26).fill(null);
            this.isEnd = false;
        }
    }

    const root = new TrieNode();

    for (const word of dictionary) {
        let node = root;
        for (let i = 0; i < word.length; i++) {
            const idx = word.charCodeAt(i) - 97;
            if (!node.children[idx]) {
                node.children[idx] = new TrieNode();
            }
            node = node.children[idx] as TrieNode;
        }
        node.isEnd = true;
    }

    function shortestRoot(word: string): string {
        let node = root;
        for (let i = 0; i < word.length; i++) {
            const idx = word.charCodeAt(i) - 97;
            if (!node.children[idx]) return word;
            node = node.children[idx] as TrieNode;
            if (node.isEnd) return word.substring(0, i + 1);
        }
        return word;
    }

    const words = sentence.split(' ');
    for (let i = 0; i < words.length; i++) {
        words[i] = shortestRoot(words[i]);
    }
    return words.join(' ');
}
```

## Php

```php
<?php
class TrieNode {
    public array $children = [];
    public bool $isEnd = false;
}

class Solution {

    /**
     * @param String[] $dictionary
     * @param String $sentence
     * @return String
     */
    function replaceWords($dictionary, $sentence) {
        $root = new TrieNode();

        // Build the trie from dictionary roots
        foreach ($dictionary as $word) {
            $node = $root;
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $c = $word[$i];
                if (!isset($node->children[$c])) {
                    $node->children[$c] = new TrieNode();
                }
                $node = $node->children[$c];
            }
            $node->isEnd = true;
        }

        // Process each word in the sentence
        $words = explode(' ', $sentence);
        foreach ($words as &$w) {
            $node = $root;
            $prefix = '';
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) {
                $c = $w[$i];
                if (!isset($node->children[$c])) {
                    break;
                }
                $node = $node->children[$c];
                $prefix .= $c;
                if ($node->isEnd) {
                    $w = $prefix;
                    break;
                }
            }
        }

        return implode(' ', $words);
    }
}
?>
```

## Swift

```swift
class TrieNode {
    var children: [TrieNode?] = Array(repeating: nil, count: 26)
    var isEnd: Bool = false
}

class Solution {
    func replaceWords(_ dictionary: [String], _ sentence: String) -> String {
        let root = TrieNode()
        for word in dictionary {
            insert(word, into: root)
        }
        let words = sentence.split(separator: " ")
        var result = [String]()
        result.reserveCapacity(words.count)
        for wSub in words {
            let w = String(wSub)
            result.append(shortestRoot(w, from: root))
        }
        return result.joined(separator: " ")
    }

    private func insert(_ word: String, into root: TrieNode) {
        var node = root
        for ch in word {
            let idx = Int(ch.asciiValue! - 97)
            if node.children[idx] == nil {
                node.children[idx] = TrieNode()
            }
            node = node.children[idx]!
        }
        node.isEnd = true
    }

    private func shortestRoot(_ word: String, from root: TrieNode) -> String {
        var node = root
        var prefix = ""
        for ch in word {
            let idx = Int(ch.asciiValue! - 97)
            if node.children[idx] == nil {
                return word
            }
            node = node.children[idx]!
            prefix.append(ch)
            if node.isEnd {
                return prefix
            }
        }
        return word
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class TrieNode {
        val children = arrayOfNulls<TrieNode>(26)
        var isEnd: Boolean = false
    }

    private class Trie {
        private val root = TrieNode()

        fun insert(word: String) {
            var node = root
            for (ch in word) {
                val idx = ch - 'a'
                if (node.children[idx] == null) {
                    node.children[idx] = TrieNode()
                }
                node = node.children[idx]!!
            }
            node.isEnd = true
        }

        fun shortestRoot(word: String): String {
            var node = root
            for ((i, ch) in word.withIndex()) {
                val idx = ch - 'a'
                if (node.children[idx] == null) return word
                node = node.children[idx]!!
                if (node.isEnd) return word.substring(0, i + 1)
            }
            return word
        }
    }

    fun replaceWords(dictionary: List<String>, sentence: String): String {
        val trie = Trie()
        for (root in dictionary) {
            trie.insert(root)
        }
        val words = sentence.split(' ')
        val sb = StringBuilder()
        for (i in words.indices) {
            sb.append(trie.shortestRoot(words[i]))
            if (i + 1 < words.size) sb.append(' ')
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class TrieNode {
  List<TrieNode?> children = List.filled(26, null);
  bool isEnd = false;
}

class Trie {
  final TrieNode root = TrieNode();

  void insert(String word) {
    TrieNode node = root;
    for (int i = 0; i < word.length; i++) {
      int idx = word.codeUnitAt(i) - 97;
      if (node.children[idx] == null) {
        node.children[idx] = TrieNode();
      }
      node = node.children[idx]!;
    }
    node.isEnd = true;
  }

  String shortestRoot(String word) {
    TrieNode node = root;
    for (int i = 0; i < word.length; i++) {
      int idx = word.codeUnitAt(i) - 97;
      if (node.children[idx] == null) {
        return word;
      }
      node = node.children[idx]!;
      if (node.isEnd) {
        return word.substring(0, i + 1);
      }
    }
    return word;
  }
}

class Solution {
  String replaceWords(List<String> dictionary, String sentence) {
    Trie trie = Trie();
    for (var root in dictionary) {
      trie.insert(root);
    }

    List<String> words = sentence.split(' ');
    for (int i = 0; i < words.length; i++) {
      words[i] = trie.shortestRoot(words[i]);
    }
    return words.join(' ');
  }
}
```

## Golang

```go
package main

import (
	"strings"
)

type TrieNode struct {
	children [26]*TrieNode
	isEnd    bool
}

func (t *TrieNode) insert(word string) {
	node := t
	for i := 0; i < len(word); i++ {
		idx := word[i] - 'a'
		if node.children[idx] == nil {
			node.children[idx] = &TrieNode{}
		}
		node = node.children[idx]
	}
	node.isEnd = true
}

func (t *TrieNode) shortestRoot(word string) string {
	node := t
	for i := 0; i < len(word); i++ {
		idx := word[i] - 'a'
		if node.children[idx] == nil {
			return word
		}
		node = node.children[idx]
		if node.isEnd {
			return word[:i+1]
		}
	}
	return word
}

func replaceWords(dictionary []string, sentence string) string {
	root := &TrieNode{}
	for _, w := range dictionary {
		root.insert(w)
	}
	words := strings.Split(sentence, " ")
	for i, w := range words {
		words[i] = root.shortestRoot(w)
	}
	return strings.Join(words, " ")
}
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

def replace_words(dictionary, sentence)
  root = TrieNode.new
  dictionary.each do |word|
    node = root
    word.each_char do |ch|
      node.children[ch] ||= TrieNode.new
      node = node.children[ch]
    end
    node.is_end = true
  end

  words = sentence.split(' ')
  words.map! do |w|
    node = root
    prefix = ''
    replacement = nil
    w.each_char do |ch|
      break unless node.children.key?(ch)
      node = node.children[ch]
      prefix << ch
      if node.is_end
        replacement = prefix
        break
      end
    end
    replacement || w
  end

  words.join(' ')
end
```

## Scala

```scala
object Solution {
  class TrieNode {
    var children: Array[TrieNode] = new Array[TrieNode](26)
    var isEnd: Boolean = false
  }

  class Trie {
    private val root = new TrieNode

    def insert(word: String): Unit = {
      var node = root
      for (c <- word) {
        val idx = c - 'a'
        if (node.children(idx) == null) node.children(idx) = new TrieNode
        node = node.children(idx)
      }
      node.isEnd = true
    }

    def shortestRoot(word: String): String = {
      var node = root
      val sb = new StringBuilder
      for (i <- 0 until word.length) {
        val c = word.charAt(i)
        val idx = c - 'a'
        if (node.children(idx) == null) return word
        node = node.children(idx)
        sb.append(c)
        if (node.isEnd) return sb.toString()
      }
      word
    }
  }

  def replaceWords(dictionary: List[String], sentence: String): String = {
    val trie = new Trie
    for (root <- dictionary) trie.insert(root)

    val words = sentence.split(" ")
    val replaced = words.map(trie.shortestRoot)
    replaced.mkString(" ")
  }
}
```

## Rust

```rust
struct Node {
    next: [i32; 26],
    end: bool,
}

impl Solution {
    pub fn replace_words(dictionary: Vec<String>, sentence: String) -> String {
        // Build Trie
        let mut nodes = Vec::new();
        nodes.push(Node { next: [-1; 26], end: false }); // root

        for word in dictionary.iter() {
            let mut idx_node = 0usize;
            for b in word.bytes() {
                let c = (b - b'a') as usize;
                if nodes[idx_node].next[c] == -1 {
                    nodes.push(Node { next: [-1; 26], end: false });
                    let new_idx = (nodes.len() - 1) as i32;
                    nodes[idx_node].next[c] = new_idx;
                }
                idx_node = nodes[idx_node].next[c] as usize;
            }
            nodes[idx_node].end = true;
        }

        // Process sentence
        let mut result = Vec::new();
        for w in sentence.split_whitespace() {
            let mut idx_node = 0usize;
            let mut replace_len: Option<usize> = None;

            for (i, b) in w.bytes().enumerate() {
                let c = (b - b'a') as usize;
                let next = nodes[idx_node].next[c];
                if next == -1 {
                    break;
                }
                idx_node = next as usize;
                if nodes[idx_node].end {
                    replace_len = Some(i + 1);
                    break;
                }
            }

            let replaced = match replace_len {
                Some(len) => w[..len].to_string(),
                None => w.to_string(),
            };
            result.push(replaced);
        }

        result.join(" ")
    }
}
```

## Racket

```racket
(require racket/string)

;; Trie node is a mutable hash table.
;; Keys are characters (as strings of length 1) mapping to child nodes,
;; and the special key '#end' indicating end of a word.

(define (make-trie)
  (hash))

(define (trie-insert! trie word)
  (let loop ((i 0) (node trie))
    (if (= i (string-length word))
        (hash-set! node '#end #t)
        (let* ((c (string-ref word i))
               (child (hash-ref node c #f)))
          (unless child
            (set! child (make-hash))
            (hash-set! node c child))
          (loop (+ i 1) child)))))

(define (trie-shortest-root trie word)
  (let loop ((i 0) (node trie))
    (if (= i (string-length word))
        word
        (let* ((c (string-ref word i))
               (child (hash-ref node c #f)))
          (cond [(not child) word]
                [(hash-ref child '#end #f) (substring word 0 (+ i 1))]
                [else (loop (+ i 1) child)])))))

(define/contract (replace-words dictionary sentence)
  (-> (listof string?) string? string?)
  (let ((trie (make-trie)))
    (for ([w dictionary])
      (trie-insert! trie w))
    (define words (string-split sentence " "))
    (define replaced
      (map (lambda (w) (trie-shortest-root trie w)) words))
    (string-join replaced " ")))
```

## Erlang

```erlang
-module(solution).
-export([replace_words/2]).

-spec replace_words(Dictionary :: [binary()], Sentence :: binary()) -> binary().
replace_words(Dictionary, Sentence) ->
    DictSet = maps:from_list([{Root, true} || Root <- Dictionary]),
    Words = binary:split(Sentence, <<" ">>, [global]),
    Replaced = [shortest_root(W, DictSet) || W <- Words],
    binary:join(Replaced, <<" ">>).

shortest_root(Word, Set) ->
    Len = byte_size(Word),
    find_prefix(1, Len, Word, Set).

find_prefix(Cur, Max, Word, Set) when Cur =< Max ->
    Prefix = binary:part(Word, {0, Cur}),
    case maps:is_key(Prefix, Set) of
        true -> Prefix;
        false -> find_prefix(Cur + 1, Max, Word, Set)
    end;
find_prefix(_, _, Word, _) ->
    Word.
```

## Elixir

```elixir
defmodule Solution do
  defmodule TrieNode do
    defstruct end: false, children: %{}
  end

  @spec replace_words(dictionary :: [String.t()], sentence :: String.t()) :: String.t()
  def replace_words(dictionary, sentence) do
    trie = Enum.reduce(dictionary, %TrieNode{}, &insert(&2, &1))
    sentence
    |> String.split(" ")
    |> Enum.map(&shortest_root(trie, &1))
    |> Enum.join(" ")
  end

  # Insert a word into the trie
  defp insert(node, ""), do: %{node | end: true}

  defp insert(%TrieNode{children: children} = node, <<char, rest::binary>>) do
    child = Map.get(children, char, %TrieNode{})
    new_child = insert(child, rest)
    %{node | children: Map.put(children, char, new_child)}
  end

  # Find the shortest root for a given word; return original if none found
  defp shortest_root(trie, word) do
    case traverse(trie, word, <<>>) do
      nil -> word
      prefix -> prefix
    end
  end

  # Traverse the trie following the characters of the word,
  # building the current prefix. Return the prefix when a terminal node is hit.
  defp traverse(_node, "", _acc), do: nil

  defp traverse(node, <<char, rest::binary>>, acc) do
    case Map.get(node.children, char) do
      nil -> nil
      child ->
        new_acc = <<acc::binary, char>>
        if child.end do
          new_acc
        else
          traverse(child, rest, new_acc)
        end
    end
  end
end
```
