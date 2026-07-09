# 3291. Minimum Number of Valid Strings to Form Target I

## Cpp

```cpp
class Solution {
public:
    int minValidStrings(vector<string>& words, string target) {
        struct Node {
            int nxt[26];
            Node() { fill(begin(nxt), end(nxt), -1); }
        };
        vector<Node> trie(1);
        // Build Trie with all prefixes
        for (const string& w : words) {
            int node = 0;
            for (char ch : w) {
                int c = ch - 'a';
                if (trie[node].nxt[c] == -1) {
                    trie[node].nxt[c] = trie.size();
                    trie.emplace_back();
                }
                node = trie[node].nxt[c];
            }
        }
        const int n = target.size();
        const int INF = 1e9;
        vector<int> dp(n + 1, INF);
        dp[0] = 0;
        for (int i = 0; i < n; ++i) {
            if (dp[i] == INF) continue;
            int node = 0;
            for (int j = i; j < n; ++j) {
                int c = target[j] - 'a';
                if (trie[node].nxt[c] == -1) break;
                node = trie[node].nxt[c];
                dp[j + 1] = min(dp[j + 1], dp[i] + 1);
            }
        }
        return dp[n] == INF ? -1 : dp[n];
    }
};
```

## Java

```java
class Solution {
    static class Node {
        Node[] child = new Node[26];
    }

    public int minValidStrings(String[] words, String target) {
        Node root = new Node();
        // Build trie with all prefixes of words
        for (String w : words) {
            Node cur = root;
            for (int i = 0; i < w.length(); i++) {
                int idx = w.charAt(i) - 'a';
                if (cur.child[idx] == null) cur.child[idx] = new Node();
                cur = cur.child[idx];
            }
        }

        int n = target.length();
        final int INF = Integer.MAX_VALUE / 2;
        int[] dp = new int[n + 1];
        java.util.Arrays.fill(dp, INF);
        dp[0] = 0;

        char[] t = target.toCharArray();
        for (int i = 0; i < n; i++) {
            if (dp[i] == INF) continue;
            Node node = root;
            for (int j = i; j < n; j++) {
                int idx = t[j] - 'a';
                node = node.child[idx];
                if (node == null) break;
                if (dp[j + 1] > dp[i] + 1) dp[j + 1] = dp[i] + 1;
            }
        }

        return dp[n] == INF ? -1 : dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def minValidStrings(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        # Build trie of all prefixes (any node is a valid prefix)
        nodes = [{}]  # list of dicts for children
        for w in words:
            cur = 0
            for ch in w:
                nxt = nodes[cur].get(ch)
                if nxt is None:
                    nodes.append({})
                    nxt = len(nodes) - 1
                    nodes[cur][ch] = nxt
                cur = nxt

        n = len(target)
        INF = n + 5
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue
            cur = 0
            for j in range(i, n):
                ch = target[j]
                nxt = nodes[cur].get(ch)
                if nxt is None:
                    break
                cur = nxt
                # prefix of length (j-i+1) is valid
                if dp[i] + 1 < dp[j + 1]:
                    dp[j + 1] = dp[i] + 1

        return -1 if dp[n] == INF else dp[n]
```

## Python3

```python
from typing import List

class TrieNode:
    __slots__ = ('children',)
    def __init__(self):
        self.children = {}

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]

        n = len(target)
        INF = 10**9
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue
            node = root
            j = i
            while j < n and target[j] in node.children:
                node = node.children[target[j]]
                j += 1
                if dp[j] > dp[i] + 1:
                    dp[j] = dp[i] + 1

        return -1 if dp[n] == INF else dp[n]
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int child[26];
} Node;

int minValidStrings(char** words, int wordsSize, char* target) {
    // Calculate total length to allocate trie nodes
    int totalLen = 0;
    for (int i = 0; i < wordsSize; ++i) {
        totalLen += strlen(words[i]);
    }
    int maxNodes = totalLen + 1; // include root
    Node *trie = (Node *)malloc(sizeof(Node) * maxNodes);
    if (!trie) return -1;
    
    // Initialize root
    for (int k = 0; k < 26; ++k) trie[0].child[k] = -1;
    int nodeCnt = 1; // next free index
    
    // Build trie with all words
    for (int i = 0; i < wordsSize; ++i) {
        const char *w = words[i];
        int cur = 0;
        while (*w) {
            int idx = *w - 'a';
            if (trie[cur].child[idx] == -1) {
                trie[cur].child[idx] = nodeCnt;
                for (int k = 0; k < 26; ++k) trie[nodeCnt].child[k] = -1;
                ++nodeCnt;
            }
            cur = trie[cur].child[idx];
            ++w;
        }
    }
    
    int n = strlen(target);
    const int INF = n + 5;
    int *dp = (int *)malloc(sizeof(int) * (n + 1));
    for (int i = 0; i <= n; ++i) dp[i] = INF;
    dp[0] = 0;
    
    for (int i = 0; i < n; ++i) {
        if (dp[i] == INF) continue;
        int cur = 0;
        for (int j = i; j < n; ++j) {
            int idx = target[j] - 'a';
            if (trie[cur].child[idx] == -1) break;
            cur = trie[cur].child[idx];
            if (dp[j + 1] > dp[i] + 1)
                dp[j + 1] = dp[i] + 1;
        }
    }
    
    int ans = (dp[n] == INF) ? -1 : dp[n];
    free(dp);
    free(trie);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinValidStrings(string[] words, string target) {
        TrieNode root = new TrieNode();
        foreach (var w in words) {
            var node = root;
            foreach (char ch in w) {
                int idx = ch - 'a';
                if (node.children[idx] == null) node.children[idx] = new TrieNode();
                node = node.children[idx];
            }
        }

        int n = target.Length;
        const int INF = 1_000_000;
        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = INF;
        dp[0] = 0;

        for (int i = 0; i < n; i++) {
            if (dp[i] == INF) continue;
            var node = root;
            for (int j = i; j < n; j++) {
                int idx = target[j] - 'a';
                if (node.children[idx] == null) break;
                node = node.children[idx];
                if (dp[j + 1] > dp[i] + 1) dp[j + 1] = dp[i] + 1;
            }
        }

        return dp[n] == INF ? -1 : dp[n];
    }

    private class TrieNode {
        public TrieNode[] children = new TrieNode[26];
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {string} target
 * @return {number}
 */
var minValidStrings = function(words, target) {
    // Build Trie where every node (except root) represents a valid prefix
    const nodes = [{ next: new Int32Array(26).fill(-1) }];
    for (const w of words) {
        let cur = 0;
        for (let i = 0; i < w.length; ++i) {
            const c = w.charCodeAt(i) - 97;
            if (nodes[cur].next[c] === -1) {
                nodes[cur].next[c] = nodes.length;
                nodes.push({ next: new Int32Array(26).fill(-1) });
            }
            cur = nodes[cur].next[c];
        }
    }

    const n = target.length;
    const INF = 1e9;
    const dp = new Array(n + 1).fill(INF);
    dp[0] = 0;

    for (let i = 0; i < n; ++i) {
        if (dp[i] === INF) continue;
        let node = 0;
        for (let j = i; j < n; ++j) {
            const c = target.charCodeAt(j) - 97;
            node = nodes[node].next[c];
            if (node === -1) break; // no further match
            // substring target[i..j] is a valid prefix
            if (dp[j + 1] > dp[i] + 1) dp[j + 1] = dp[i] + 1;
        }
    }

    return dp[n] === INF ? -1 : dp[n];
};
```

## Typescript

```typescript
function minValidStrings(words: string[], target: string): number {
    const nodesNext: number[][] = [];
    const createNode = () => {
        nodesNext.push(new Array(26).fill(-1));
        return nodesNext.length - 1;
    };
    createNode(); // root at index 0

    for (const w of words) {
        let idx = 0;
        for (let i = 0; i < w.length; i++) {
            const c = w.charCodeAt(i) - 97;
            if (nodesNext[idx][c] === -1) {
                const newIdx = createNode();
                nodesNext[idx][c] = newIdx;
            }
            idx = nodesNext[idx][c];
        }
    }

    const n = target.length;
    const INF = 1e9;
    const dp = new Array(n + 1).fill(INF);
    dp[0] = 0;

    for (let i = 0; i < n; i++) {
        if (dp[i] === INF) continue;
        let nodeIdx = 0;
        for (let j = i; j < n; j++) {
            const c = target.charCodeAt(j) - 97;
            const nextIdx = nodesNext[nodeIdx][c];
            if (nextIdx === -1) break;
            nodeIdx = nextIdx;
            dp[j + 1] = Math.min(dp[j + 1], dp[i] + 1);
        }
    }

    return dp[n] === INF ? -1 : dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $target
     * @return Integer
     */
    function minValidStrings($words, $target) {
        // Build Trie where every node (except root) represents a valid prefix
        $root = new stdClass();
        $root->children = [];

        foreach ($words as $word) {
            $node = $root;
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $c = $word[$i];
                if (!isset($node->children[$c])) {
                    $newNode = new stdClass();
                    $newNode->children = [];
                    $node->children[$c] = $newNode;
                }
                $node = $node->children[$c];
            }
        }

        $n = strlen($target);
        $INF = 1 << 30;
        $dp = array_fill(0, $n + 1, $INF);
        $dp[0] = 0;

        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] == $INF) continue;
            $node = $root;
            for ($j = $i; $j < $n; $j++) {
                $c = $target[$j];
                if (!isset($node->children[$c])) break;
                $node = $node->children[$c];
                // any node reached corresponds to a valid string covering target[i..j]
                if ($dp[$j + 1] > $dp[$i] + 1) {
                    $dp[$j + 1] = $dp[$i] + 1;
                }
            }
        }

        return $dp[$n] == $INF ? -1 : $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func minValidStrings(_ words: [String], _ target: String) -> Int {
        // Build Trie
        class TrieNode {
            var next: [Int]
            init() {
                self.next = Array(repeating: -1, count: 26)
            }
        }
        var trie: [TrieNode] = [TrieNode()] // root at index 0
        
        func addWord(_ word: String) {
            var nodeIdx = 0
            for byte in word.utf8 {
                let c = Int(byte - 97) // 'a' ascii is 97
                if trie[nodeIdx].next[c] == -1 {
                    trie.append(TrieNode())
                    trie[nodeIdx].next[c] = trie.count - 1
                }
                nodeIdx = trie[nodeIdx].next[c]
            }
        }
        
        for w in words {
            addWord(w)
        }
        
        let tBytes = Array(target.utf8)
        let n = tBytes.count
        let INF = Int.max / 2
        var dp = Array(repeating: INF, count: n + 1)
        dp[0] = 0
        
        for i in 0..<n {
            if dp[i] == INF { continue }
            var nodeIdx = 0
            var j = i
            while j < n {
                let c = Int(tBytes[j] - 97)
                let child = trie[nodeIdx].next[c]
                if child == -1 { break }
                nodeIdx = child
                // substring target[i...j] is a valid prefix
                if dp[j + 1] > dp[i] + 1 {
                    dp[j + 1] = dp[i] + 1
                }
                j += 1
            }
        }
        
        return dp[n] == INF ? -1 : dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minValidStrings(words: Array<String>, target: String): Int {
        // Trie node definition
        data class Node(val next: IntArray = IntArray(26) { -1 })
        val nodes = mutableListOf(Node())

        // Insert each word into the trie (all prefixes are automatically represented)
        for (word in words) {
            var cur = 0
            for (ch in word) {
                val idx = ch - 'a'
                if (nodes[cur].next[idx] == -1) {
                    nodes.add(Node())
                    nodes[cur].next[idx] = nodes.size - 1
                }
                cur = nodes[cur].next[idx]
            }
        }

        val n = target.length
        val INF = Int.MAX_VALUE / 2
        val dp = IntArray(n + 1) { INF }
        dp[0] = 0

        for (i in 0 until n) {
            if (dp[i] == INF) continue
            var nodeIdx = 0
            var j = i
            while (j < n) {
                val cIdx = target[j] - 'a'
                val nextIdx = nodes[nodeIdx].next[cIdx]
                if (nextIdx == -1) break
                nodeIdx = nextIdx
                // any visited node corresponds to a valid prefix
                if (dp[j + 1] > dp[i] + 1) {
                    dp[j + 1] = dp[i] + 1
                }
                j++
            }
        }

        return if (dp[n] == INF) -1 else dp[n]
    }
}
```

## Dart

```dart
class Solution {
  int minValidStrings(List<String> words, String target) {
    // Build a trie containing all prefixes of the given words.
    final List<_TrieNode> trie = [_TrieNode()];
    for (final w in words) {
      int node = 0;
      for (int i = 0; i < w.length; ++i) {
        int c = w.codeUnitAt(i) - 97;
        int nxt = trie[node].next[c];
        if (nxt == -1) {
          nxt = trie.length;
          trie[node].next[c] = nxt;
          trie.add(_TrieNode());
        }
        node = nxt;
      }
    }

    final int n = target.length;
    const int INF = 1 << 30;
    List<int> dp = List.filled(n + 1, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
      if (dp[i] == INF) continue;
      int node = 0;
      for (int j = i; j < n; ++j) {
        int c = target.codeUnitAt(j) - 97;
        int nxt = trie[node].next[c];
        if (nxt == -1) break;
        node = nxt;
        if (dp[j + 1] > dp[i] + 1) {
          dp[j + 1] = dp[i] + 1;
        }
      }
    }

    return dp[n] == INF ? -1 : dp[n];
  }
}

class _TrieNode {
  final List<int> next;
  _TrieNode() : next = List.filled(26, -1);
}
```

## Golang

```go
func minValidStrings(words []string, target string) int {
	type node struct {
		next map[byte]int
	}
	// Build trie of all prefixes (all nodes are valid)
	trie := []node{{next: make(map[byte]int)}}
	for _, w := range words {
		cur := 0
		for i := 0; i < len(w); i++ {
			c := w[i]
			if nxt, ok := trie[cur].next[c]; ok {
				cur = nxt
			} else {
				trie = append(trie, node{next: make(map[byte]int)})
				newIdx := len(trie) - 1
				trie[cur].next[c] = newIdx
				cur = newIdx
			}
		}
	}

	n := len(target)
	const INF = int(1e9)
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = INF
	}
	dp[0] = 0

	for i := 0; i < n; i++ {
		if dp[i] == INF {
			continue
		}
		cur := 0
		for j := i; j < n; j++ {
			c := target[j]
			nextIdx, ok := trie[cur].next[c]
			if !ok {
				break
			}
			cur = nextIdx
			if dp[i]+1 < dp[j+1] {
				dp[j+1] = dp[i] + 1
			}
		}
	}

	if dp[n] == INF {
		return -1
	}
	return dp[n]
}
```

## Ruby

```ruby
def min_valid_strings(words, target)
  root = { children: {} }
  words.each do |w|
    node = root
    w.each_char do |ch|
      node[:children][ch] ||= { children: {} }
      node = node[:children][ch]
    end
  end

  n = target.length
  dp = Array.new(n + 1, Float::INFINITY)
  dp[0] = 0

  (0...n).each do |i|
    next if dp[i] == Float::INFINITY
    node = root
    j = i
    while j < n && node[:children].key?(target[j])
      node = node[:children][target[j]]
      new_val = dp[i] + 1
      dp[j + 1] = new_val if new_val < dp[j + 1]
      j += 1
    end
  end

  dp[n] == Float::INFINITY ? -1 : dp[n].to_i
end
```

## Scala

```scala
object Solution {
  def minValidStrings(words: Array[String], target: String): Int = {
    class Node {
      val next: Array[Node] = new Array[Node](26)
    }
    val root = new Node
    // Build trie with all words (prefixes are automatically represented)
    for (w <- words) {
      var node = root
      for (ch <- w) {
        val idx = ch - 'a'
        if (node.next(idx) == null) node.next(idx) = new Node
        node = node.next(idx)
      }
    }

    val n = target.length
    val INF = Int.MaxValue / 2
    val dp = Array.fill(n + 1)(INF)
    dp(0) = 0

    for (i <- 0 until n) {
      if (dp(i) != INF) {
        var node: Node = root
        var j = i
        while (j < n && node != null) {
          val idx = target.charAt(j) - 'a'
          node = node.next(idx)
          if (node != null) {
            dp(j + 1) = math.min(dp(j + 1), dp(i) + 1)
            j += 1
          }
        }
      }
    }

    val ans = dp(n)
    if (ans >= INF) -1 else ans
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn min_valid_strings(words: Vec<String>, target: String) -> i32 {
        #[derive(Clone)]
        struct Node {
            child: [Option<usize>; 26],
        }

        let mut nodes = Vec::new();
        nodes.push(Node { child: [None; 26] });

        for w in words.iter() {
            let mut cur = 0usize;
            for &b in w.as_bytes() {
                let idx = (b - b'a') as usize;
                if nodes[cur].child[idx].is_none() {
                    nodes.push(Node { child: [None; 26] });
                    let new_idx = nodes.len() - 1;
                    nodes[cur].child[idx] = Some(new_idx);
                }
                cur = nodes[cur].child[idx].unwrap();
            }
        }

        let n = target.len();
        let t_bytes = target.as_bytes();
        const INF: i32 = 1_000_000_0;
        let mut dp = vec![INF; n + 1];
        dp[0] = 0;

        for i in 0..n {
            if dp[i] == INF {
                continue;
            }
            let mut node_idx = 0usize;
            for j in i..n {
                let idx = (t_bytes[j] - b'a') as usize;
                match nodes[node_idx].child[idx] {
                    Some(next) => {
                        node_idx = next;
                        let cand = dp[i] + 1;
                        if cand < dp[j + 1] {
                            dp[j + 1] = cand;
                        }
                    }
                    None => break,
                }
            }
        }

        if dp[n] == INF { -1 } else { dp[n] }
    }
}
```

## Racket

```racket
(define-struct node (children) #:mutable)

(define (make-trie)
  (make-node (make-hash)))

(define (insert-word! root word)
  (let ((len (string-length word)))
    (let loop ((i 0) (cur root))
      (when (< i len)
        (let* ((c (string-ref word i))
               (children (node-children cur))
               (next (hash-ref children c #f)))
          (unless next
            (set! next (make-node (make-hash)))
            (hash-set! children c next))
          (loop (+ i 1) next))))))

(define/contract (min-valid-strings words target)
  (-> (listof string?) string? exact-integer?)
  (let* ((root (make-trie))
         (_ (for-each (lambda (w) (insert-word! root w)) words))
         (n (string-length target))
         (INF 1000000000)
         (dp (make-vector (+ n 1) INF)))
    (vector-set! dp 0 0)
    (let loop-i ((i 0))
      (when (< i n)
        (let ((cur-cost (vector-ref dp i)))
          (when (< cur-cost INF)
            (let inner-loop ((j i) (node root))
              (when (< j n)
                (let* ((c (string-ref target j))
                       (next (hash-ref (node-children node) c #f)))
                  (if next
                      (begin
                        (define new-cost (+ cur-cost 1))
                        (let ((old (vector-ref dp (+ j 1))))
                          (when (< new-cost old)
                            (vector-set! dp (+ j 1) new-cost)))
                        (inner-loop (+ j 1) next))
                      #f))))))
        (loop-i (+ i 1))))
    (let ((ans (vector-ref dp n)))
      (if (>= ans INF) -1 ans))))
```

## Erlang

```erlang
-module(solution).
-export([min_valid_strings/2]).

-define(INF, 1 bsl 30).

%% Public API
-spec min_valid_strings(Words :: [unicode:unicode_binary()], Target :: unicode:unicode_binary()) -> integer().
min_valid_strings(Words, Target) ->
    Trie = build_trie(Words),
    TargetList = binary_to_list(Target),
    LenT = length(TargetList),
    DP0 = array:new([{size, LenT + 1}, {default, ?INF}]),
    DP1 = array:set(0, 0, DP0),
    FinalDP = dp_loop(0, LenT, TargetList, Trie, DP1),
    Result = array:get(LenT, FinalDP),
    case Result of
        ?INF -> -1;
        _ -> Result
    end.

%% Build trie from list of words.
build_trie(Words) ->
    {Trie, _Next} = lists:foldl(fun(Word, {AccTrie, NextId}) ->
        Chars = binary_to_list(Word),
        add_word(Chars, 0, AccTrie, NextId)
    end, {#{0 => #{}}, 1}, Words),
    Trie.

add_word([], _NodeId, Trie, Next) ->
    {Trie, Next};
add_word([C|Rest], NodeId, Trie, Next) ->
    Children = maps:get(NodeId, Trie),
    case maps:find(C, Children) of
        {ok, ChildId} ->
            add_word(Rest, ChildId, Trie, Next);
        error ->
            ChildId = Next,
            NewChildren = maps:put(C, ChildId, Children),
            Trie1 = maps:put(NodeId, NewChildren, Trie),
            Trie2 = maps:put(ChildId, #{}, Trie1),
            add_word(Rest, ChildId, Trie2, Next + 1)
    end.

%% DP loop over positions.
dp_loop(I, LenT, _TargetList, _Trie, DP) when I > LenT ->
    DP;
dp_loop(I, LenT, TargetList, Trie, DP) ->
    Cur = array:get(I, DP),
    DP2 =
        if
            Cur == ?INF -> DP;
            true -> explore(I, I, 0, Cur, TargetList, Trie, DP)
        end,
    dp_loop(I + 1, LenT, TargetList, Trie, DP2).

%% Explore all prefixes starting at StartIdx.
explore(StartIdx, Pos, NodeId, CurCost, TargetList, Trie, DP) ->
    case Pos < length(TargetList) of
        false -> DP;
        true ->
            Char = lists:nth(Pos + 1, TargetList),
            Children = maps:get(NodeId, Trie),
            case maps:find(Char, Children) of
                {ok, ChildId} ->
                    NewPos = Pos + 1,
                    OldVal = array:get(NewPos, DP),
                    UpdatedDP =
                        if CurCost + 1 < OldVal ->
                                array:set(NewPos, CurCost + 1, DP);
                           true -> DP
                        end,
                    explore(StartIdx, NewPos, ChildId, CurCost, TargetList, Trie, UpdatedDP);
                error ->
                    DP
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_valid_strings(words :: [String.t()], target :: String.t()) :: integer()
  def min_valid_strings(words, target) do
    trie = build_trie(words)
    n = byte_size(target)

    inf = 1_000_000
    dp0 = :array.from_list(List.duplicate(inf, n + 1))
    dp0 = :array.set(0, 0, dp0)

    dp_final =
      Enum.reduce(0..(n - 1), dp0, fn i, dp_acc ->
        cur = :array.get(i, dp_acc)

        if cur < inf do
          update_from(i, cur, trie, i, target, n, dp_acc)
        else
          dp_acc
        end
      end)

    res = :array.get(n, dp_final)
    if res >= inf, do: -1, else: res
  end

  # Build a trie where every node represents a valid prefix.
  defp build_trie(words) do
    Enum.reduce(words, %{}, fn word, acc -> insert(acc, word) end)
  end

  defp insert(trie, <<c::utf8, rest::binary>>) do
    child = Map.get(trie, c, %{})
    updated_child = insert(child, rest)
    Map.put(trie, c, updated_child)
  end

  defp insert(trie, <<>>), do: trie

  # Walk the trie starting at position `pos` and update dp.
  defp update_from(start_i, cur_cost, node, pos, target, n, dp) when pos < n do
    c = :binary.at(target, pos)

    case Map.fetch(node, c) do
      {:ok, child} ->
        j = start_i + (pos - start_i + 1)
        old = :array.get(j, dp)

        dp2 =
          if cur_cost + 1 < old do
            :array.set(j, cur_cost + 1, dp)
          else
            dp
          end

        update_from(start_i, cur_cost, child, pos + 1, target, n, dp2)

      :error ->
        dp
    end
  end

  defp update_from(_start_i, _cur_cost, _node, _pos, _target, _n, dp), do: dp
end
```
