# 2416. Sum of Prefix Scores of Strings

## Cpp

```cpp
class Solution {
public:
    struct TrieNode {
        int cnt = 0;
        TrieNode* child[26];
        TrieNode() { memset(child, 0, sizeof(child)); }
    };
    
    vector<int> sumPrefixScores(vector<string>& words) {
        TrieNode* root = new TrieNode();
        // Build trie and count prefixes
        for (const string& w : words) {
            TrieNode* node = root;
            for (char ch : w) {
                int idx = ch - 'a';
                if (!node->child[idx]) node->child[idx] = new TrieNode();
                node = node->child[idx];
                node->cnt += 1;
            }
        }
        // Compute answer for each word
        vector<int> ans;
        ans.reserve(words.size());
        for (const string& w : words) {
            int sum = 0;
            TrieNode* node = root;
            for (char ch : w) {
                int idx = ch - 'a';
                node = node->child[idx];
                sum += node->cnt;
            }
            ans.push_back(sum);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class TrieNode {
        TrieNode[] child = new TrieNode[26];
        int cnt;
    }

    public int[] sumPrefixScores(String[] words) {
        TrieNode root = new TrieNode();
        for (String w : words) {
            TrieNode node = root;
            for (int i = 0; i < w.length(); i++) {
                int idx = w.charAt(i) - 'a';
                if (node.child[idx] == null) {
                    node.child[idx] = new TrieNode();
                }
                node = node.child[idx];
                node.cnt++;
            }
        }

        int n = words.length;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            String w = words[i];
            TrieNode node = root;
            int sum = 0;
            for (int j = 0; j < w.length(); j++) {
                int idx = w.charAt(j) - 'a';
                node = node.child[idx];
                sum += node.cnt;
            }
            ans[i] = sum;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        class Node:
            __slots__ = ('cnt', 'next')
            def __init__(self):
                self.cnt = 0
                self.next = [None] * 26

        root = Node()
        # Build trie and count prefixes
        for w in words:
            node = root
            for ch in w:
                idx = ord(ch) - 97
                if node.next[idx] is None:
                    node.next[idx] = Node()
                node = node.next[idx]
                node.cnt += 1

        # Compute scores
        res = []
        for w in words:
            total = 0
            node = root
            for ch in w:
                idx = ord(ch) - 97
                node = node.next[idx]
                total += node.cnt
            res.append(total)
        return res
```

## Python3

```python
class Solution:
    def sumPrefixScores(self, words):
        # Trie represented by arrays
        nxt = [[-1] * 26]   # children indices
        cnt = [0]           # count of strings passing through node

        for w in words:
            node = 0
            for ch in w:
                idx = ord(ch) - 97
                if nxt[node][idx] == -1:
                    nxt[node][idx] = len(nxt)
                    nxt.append([-1] * 26)
                    cnt.append(0)
                node = nxt[node][idx]
                cnt[node] += 1

        ans = []
        for w in words:
            node = 0
            total = 0
            for ch in w:
                idx = ord(ch) - 97
                node = nxt[node][idx]
                total += cnt[node]
            ans.append(total)
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct TrieNode {
    int cnt;
    struct TrieNode *child[26];
} TrieNode;

static TrieNode* newNode(void) {
    TrieNode *node = (TrieNode *)calloc(1, sizeof(TrieNode));
    return node;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumPrefixScores(char** words, int wordsSize, int* returnSize){
    TrieNode *root = newNode();
    
    // Build trie with counts
    for (int i = 0; i < wordsSize; ++i) {
        const char *w = words[i];
        TrieNode *cur = root;
        while (*w) {
            int idx = *w - 'a';
            if (!cur->child[idx]) cur->child[idx] = newNode();
            cur = cur->child[idx];
            cur->cnt += 1;
            ++w;
        }
    }
    
    int *ans = (int *)malloc(sizeof(int) * wordsSize);
    for (int i = 0; i < wordsSize; ++i) {
        const char *w = words[i];
        TrieNode *cur = root;
        int sum = 0;
        while (*w) {
            int idx = *w - 'a';
            cur = cur->child[idx];
            sum += cur->cnt;
            ++w;
        }
        ans[i] = sum;
    }
    
    *returnSize = wordsSize;
    // Note: Not freeing trie nodes as LeetCode does not require it.
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    private class TrieNode
    {
        public TrieNode[] Children = new TrieNode[26];
        public int Count;
    }

    public int[] SumPrefixScores(string[] words)
    {
        var root = new TrieNode();

        // Build trie with counts
        foreach (var word in words)
        {
            var node = root;
            foreach (char ch in word)
            {
                int idx = ch - 'a';
                if (node.Children[idx] == null)
                    node.Children[idx] = new TrieNode();
                node = node.Children[idx];
                node.Count++;
            }
        }

        int n = words.Length;
        var result = new int[n];

        // Compute sum of prefix scores for each word
        for (int i = 0; i < n; i++)
        {
            var node = root;
            int sum = 0;
            foreach (char ch in words[i])
            {
                int idx = ch - 'a';
                node = node.Children[idx];
                sum += node.Count;
            }
            result[i] = sum;
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number[]}
 */
var sumPrefixScores = function(words) {
    // Trie node structure: { next: Int32Array(26) with -1 for null, cnt: number }
    const trie = [{ next: new Int32Array(26).fill(-1), cnt: 0 }];
    
    // Build the trie and count prefixes
    for (const w of words) {
        let node = 0;
        for (let i = 0; i < w.length; ++i) {
            const idx = w.charCodeAt(i) - 97;
            if (trie[node].next[idx] === -1) {
                trie[node].next[idx] = trie.length;
                trie.push({ next: new Int32Array(26).fill(-1), cnt: 0 });
            }
            node = trie[node].next[idx];
            trie[node].cnt += 1;
        }
    }
    
    // Compute answer for each word
    const ans = new Array(words.length);
    for (let i = 0; i < words.length; ++i) {
        let sum = 0;
        let node = 0;
        const w = words[i];
        for (let j = 0; j < w.length; ++j) {
            const idx = w.charCodeAt(j) - 97;
            node = trie[node].next[idx];
            sum += trie[node].cnt;
        }
        ans[i] = sum;
    }
    
    return ans;
};
```

## Typescript

```typescript
function sumPrefixScores(words: string[]): number[] {
    class TrieNode {
        children: (TrieNode | null)[] = new Array(26).fill(null);
        cnt: number = 0;
    }
    const root = new TrieNode();

    // Build trie and count prefixes
    for (const word of words) {
        let node = root;
        for (let i = 0; i < word.length; i++) {
            const idx = word.charCodeAt(i) - 97;
            if (!node.children[idx]) {
                node.children[idx] = new TrieNode();
            }
            node = node.children[idx]!;
            node.cnt += 1;
        }
    }

    // Compute scores for each word
    const result: number[] = [];
    for (const word of words) {
        let sum = 0;
        let node = root;
        for (let i = 0; i < word.length; i++) {
            const idx = word.charCodeAt(i) - 97;
            node = node.children[idx]!;
            sum += node.cnt;
        }
        result.push(sum);
    }

    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $words
     * @return Integer[]
     */
    function sumPrefixScores($words) {
        $root = ['next' => [], 'cnt' => 0];

        // Build trie and count prefixes
        foreach ($words as $word) {
            $node = &$root;
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $c = $word[$i];
                if (!isset($node['next'][$c])) {
                    $node['next'][$c] = ['next' => [], 'cnt' => 0];
                }
                $node = &$node['next'][$c];
                $node['cnt']++;
            }
        }

        // Compute answer for each word
        $result = [];
        foreach ($words as $word) {
            $sum = 0;
            $node = $root;
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $c = $word[$i];
                if (!isset($node['next'][$c])) {
                    break;
                }
                $node = $node['next'][$c];
                $sum += $node['cnt'];
            }
            $result[] = $sum;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func sumPrefixScores(_ words: [String]) -> [Int] {
        class TrieNode {
            var cnt = 0
            var next: [TrieNode?] = Array(repeating: nil, count: 26)
        }
        let root = TrieNode()
        
        // Build the trie and count prefixes
        for word in words {
            var node = root
            for byte in word.utf8 {
                let idx = Int(byte - 97) // 'a' ascii is 97
                if node.next[idx] == nil {
                    node.next[idx] = TrieNode()
                }
                node = node.next[idx]!
                node.cnt += 1
            }
        }
        
        var answer: [Int] = []
        // Compute sum of prefix scores for each word
        for word in words {
            var node = root
            var sum = 0
            for byte in word.utf8 {
                let idx = Int(byte - 97)
                if let child = node.next[idx] {
                    sum += child.cnt
                    node = child
                } else {
                    break
                }
            }
            answer.append(sum)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class Node {
        val next = IntArray(26) { -1 }
        var cnt = 0
    }

    fun sumPrefixScores(words: Array<String>): IntArray {
        // Build trie with counts
        val nodes = mutableListOf(Node()) // root at index 0

        for (word in words) {
            var cur = 0
            for (ch in word) {
                val idx = ch - 'a'
                var nxt = nodes[cur].next[idx]
                if (nxt == -1) {
                    nxt = nodes.size
                    nodes.add(Node())
                    nodes[cur].next[idx] = nxt
                }
                cur = nxt
                nodes[cur].cnt++
            }
        }

        val result = IntArray(words.size)
        for ((i, word) in words.withIndex()) {
            var sum = 0
            var cur = 0
            for (ch in word) {
                val idx = ch - 'a'
                cur = nodes[cur].next[idx]
                sum += nodes[cur].cnt
            }
            result[i] = sum
        }
        return result
    }
}
```

## Dart

```dart
class TrieNode {
  final List<TrieNode?> children = List.filled(26, null);
  int cnt = 0;
}

class Solution {
  List<int> sumPrefixScores(List<String> words) {
    final root = TrieNode();

    // Build trie and count prefixes
    for (final word in words) {
      var node = root;
      for (int i = 0; i < word.length; ++i) {
        int idx = word.codeUnitAt(i) - 97;
        if (node.children[idx] == null) {
          node.children[idx] = TrieNode();
        }
        node = node.children[idx]!;
        node.cnt += 1;
      }
    }

    // Compute answer for each word
    List<int> ans = List.filled(words.length, 0);
    for (int w = 0; w < words.length; ++w) {
      var node = root;
      int sum = 0;
      final word = words[w];
      for (int i = 0; i < word.length; ++i) {
        int idx = word.codeUnitAt(i) - 97;
        node = node.children[idx]!;
        sum += node.cnt;
      }
      ans[w] = sum;
    }

    return ans;
  }
}
```

## Golang

```go
type Node struct {
	next [26]*Node
	cnt  int
}

func (r *Node) insert(word string) {
	node := r
	for _, ch := range word {
		idx := int(ch - 'a')
		if node.next[idx] == nil {
			node.next[idx] = &Node{}
		}
		node = node.next[idx]
		node.cnt++
	}
}

func (r *Node) query(word string) int {
	sum, node := 0, r
	for _, ch := range word {
		idx := int(ch - 'a')
		node = node.next[idx]
		if node == nil {
			break
		}
		sum += node.cnt
	}
	return sum
}

func sumPrefixScores(words []string) []int {
	root := &Node{}
	for _, w := range words {
		root.insert(w)
	}
	ans := make([]int, len(words))
	for i, w := range words {
		ans[i] = root.query(w)
	}
	return ans
}
```

## Ruby

```ruby
def sum_prefix_scores(words)
  Node = Struct.new(:cnt, :next) do
    def initialize
      super(0, Array.new(26))
    end
  end

  root = Node.new

  words.each do |word|
    node = root
    word.each_byte do |b|
      idx = b - 97
      child = node.next[idx]
      unless child
        child = Node.new
        node.next[idx] = child
      end
      child.cnt += 1
      node = child
    end
  end

  result = []
  words.each do |word|
    node = root
    sum = 0
    word.each_byte do |b|
      idx = b - 97
      node = node.next[idx]
      sum += node.cnt
    end
    result << sum
  end

  result
end
```

## Scala

```scala
import scala.collection.mutable.ArrayBuffer

object Solution {
  def sumPrefixScores(words: Array[String]): Array[Int] = {
    class Node(var children: Array[Int], var cnt: Int)

    val nodes = ArrayBuffer[Node]()
    nodes += new Node(Array.fill(26)(-1), 0) // root at index 0

    // Build trie and count prefixes
    for (word <- words) {
      var cur = 0
      for (ch <- word) {
        val idx = ch - 'a'
        var nxt = nodes(cur).children(idx)
        if (nxt == -1) {
          nodes += new Node(Array.fill(26)(-1), 0)
          nxt = nodes.length - 1
          nodes(cur).children(idx) = nxt
        }
        cur = nxt
        nodes(cur).cnt += 1
      }
    }

    // Compute answer for each word
    val ans = new Array[Int](words.length)
    for (i <- words.indices) {
      var cur = 0
      var sum = 0
      for (ch <- words(i)) {
        val idx = ch - 'a'
        cur = nodes(cur).children(idx)
        sum += nodes(cur).cnt
      }
      ans(i) = sum
    }
    ans
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn sum_prefix_scores(words: Vec<String>) -> Vec<i32> {
        #[derive(Clone)]
        struct Node {
            next: [Option<usize>; 26],
            cnt: i32,
        }
        impl Node {
            fn new() -> Self {
                Node { next: [None; 26], cnt: 0 }
            }
        }

        let mut nodes: Vec<Node> = Vec::new();
        nodes.push(Node::new()); // root

        // Build trie and count prefixes
        for w in &words {
            let mut cur = 0usize;
            for &b in w.as_bytes() {
                let idx = (b - b'a') as usize;
                if nodes[cur].next[idx].is_none() {
                    nodes.push(Node::new());
                    let new_idx = nodes.len() - 1;
                    nodes[cur].next[idx] = Some(new_idx);
                }
                let nxt = nodes[cur].next[idx].unwrap();
                nodes[nxt].cnt += 1;
                cur = nxt;
            }
        }

        // Compute answer for each word
        let mut ans: Vec<i32> = Vec::with_capacity(words.len());
        for w in &words {
            let mut sum = 0i32;
            let mut cur = 0usize;
            for &b in w.as_bytes() {
                let idx = (b - b'a') as usize;
                let nxt = nodes[cur].next[idx].unwrap();
                sum += nodes[nxt].cnt;
                cur = nxt;
            }
            ans.push(sum);
        }

        ans
    }
}
```

## Racket

```racket
(struct node ([cnt #:mutable] [children #:mutable]) #:transparent)

(define (insert! root word)
  (let loop ((cur root) (i 0))
    (when (< i (string-length word))
      (let* ((c (string-ref word i))
             (idx (- (char->integer c) (char->integer #\a)))
             (child (vector-ref (node-children cur) idx)))
        (if child
            (begin
              (set-node-cnt! child (+ (node-cnt child) 1))
              (loop child (+ i 1)))
            (let ((new (node 1 (make-vector 26 #f))))
              (vector-set! (node-children cur) idx new)
              (loop new (+ i 1))))))))

(define (score root word)
  (let loop ((cur root) (i 0) (sum 0))
    (if (= i (string-length word))
        sum
        (let* ((c (string-ref word i))
               (idx (- (char->integer c) (char->integer #\a)))
               (child (vector-ref (node-children cur) idx)))
          (loop child (+ i 1) (+ sum (node-cnt child)))))))

(define/contract (sum-prefix-scores words)
  (-> (listof string?) (listof exact-integer?))
  (let ((root (node 0 (make-vector 26 #f))))
    (for-each (lambda (w) (insert! root w)) words)
    (map (lambda (w) (score root w)) words)))
```

## Erlang

```erlang
-module(solution).
-export([sum_prefix_scores/1]).

-spec sum_prefix_scores(Words :: [unicode:unicode_binary()]) -> [integer()].
sum_prefix_scores(Words) ->
    PrefixMap = build_counts(Words, maps:new()),
    calc_scores(Words, PrefixMap).

%% Build map of prefix -> count
build_counts([], Map) -> Map;
build_counts([Word | Rest], Map) ->
    NewMap = add_prefixes(Word, Map, 1, byte_size(Word)),
    build_counts(Rest, NewMap).

add_prefixes(_Word, Map, I, Len) when I > Len -> Map;
add_prefixes(Word, Map, I, Len) ->
    Prefix = binary:part(Word, 0, I),
    Count = maps:get(Prefix, Map, 0) + 1,
    UpdatedMap = maps:put(Prefix, Count, Map),
    add_prefixes(Word, UpdatedMap, I + 1, Len).

%% Calculate scores for each word
calc_scores(Words, PrefixMap) ->
    lists:reverse(calc_scores(Words, PrefixMap, [])).

calc_scores([], _Map, Acc) -> Acc;
calc_scores([Word | Rest], Map, Acc) ->
    Sum = sum_prefixes(Word, Map, 1, byte_size(Word), 0),
    calc_scores(Rest, Map, [Sum | Acc]).

sum_prefixes(_Word, _Map, I, Len, Acc) when I > Len -> Acc;
sum_prefixes(Word, Map, I, Len, Acc) ->
    Prefix = binary:part(Word, 0, I),
    Count = maps:get(Prefix, Map, 0),
    sum_prefixes(Word, Map, I + 1, Len, Acc + Count).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_prefix_scores(words :: [String.t()]) :: [integer()]
  def sum_prefix_scores(words) do
    root = Enum.reduce(words, %{cnt: 0, next: %{}}, fn word, acc ->
      insert(acc, String.graphemes(word))
    end)

    Enum.map(words, fn word ->
      count(root, String.graphemes(word))
    end)
  end

  defp insert(node, []), do: node

  defp insert(node, [ch | rest]) do
    child = Map.get(node.next, ch, %{cnt: 0, next: %{}})
    child = %{child | cnt: child.cnt + 1}
    updated_child = insert(child, rest)
    new_next = Map.put(node.next, ch, updated_child)
    %{node | next: new_next}
  end

  defp count(root, chars) do
    {_final_node, sum} =
      Enum.reduce(chars, {root, 0}, fn ch, {node, acc} ->
        case Map.get(node.next, ch) do
          nil -> {node, acc}
          child -> {child, acc + child.cnt}
        end
      end)

    sum
  end
end
```
