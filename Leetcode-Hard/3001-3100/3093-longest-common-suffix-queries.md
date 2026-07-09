# 3093. Longest Common Suffix Queries

## Cpp

```cpp
class Solution {
public:
    struct Node {
        int nxt[26];
        int bestIdx;
        Node() : bestIdx(-1) {
            for (int i = 0; i < 26; ++i) nxt[i] = -1;
        }
    };
    
    bool better(int cand, int cur, const vector<int>& len) {
        if (cur == -1) return true;
        if (len[cand] != len[cur]) return len[cand] < len[cur];
        return cand < cur;
    }
    
    vector<int> stringIndices(vector<string>& wordsContainer, vector<string>& wordsQuery) {
        int n = wordsContainer.size();
        vector<int> wlen(n);
        for (int i = 0; i < n; ++i) wlen[i] = wordsContainer[i].size();
        
        vector<Node> trie(1); // root at index 0
        
        // build trie with reversed strings
        for (int idx = 0; idx < n; ++idx) {
            const string& w = wordsContainer[idx];
            int node = 0;
            if (better(idx, trie[node].bestIdx, wlen)) trie[node].bestIdx = idx;
            for (int p = (int)w.size() - 1; p >= 0; --p) {
                int c = w[p] - 'a';
                if (trie[node].nxt[c] == -1) {
                    trie[node].nxt[c] = trie.size();
                    trie.emplace_back();
                }
                node = trie[node].nxt[c];
                if (better(idx, trie[node].bestIdx, wlen)) trie[node].bestIdx = idx;
            }
        }
        
        vector<int> ans;
        ans.reserve(wordsQuery.size());
        for (const string& q : wordsQuery) {
            int node = 0;
            for (int p = (int)q.size() - 1; p >= 0; --p) {
                int c = q[p] - 'a';
                if (trie[node].nxt[c] == -1) break;
                node = trie[node].nxt[c];
            }
            ans.push_back(trie[node].bestIdx);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class Node {
        Node[] next = new Node[26];
        int bestIdx = -1;
    }

    public int[] stringIndices(String[] wordsContainer, String[] wordsQuery) {
        int n = wordsContainer.length;
        int[] len = new int[n];
        Node root = new Node();

        // Build trie with reversed container strings
        for (int i = 0; i < n; i++) {
            String w = wordsContainer[i];
            len[i] = w.length();
            Node node = root;
            updateBest(node, i, len);
            for (int p = w.length() - 1; p >= 0; --p) {
                int c = w.charAt(p) - 'a';
                if (node.next[c] == null) node.next[c] = new Node();
                node = node.next[c];
                updateBest(node, i, len);
            }
        }

        // Answer queries
        int m = wordsQuery.length;
        int[] ans = new int[m];
        for (int qi = 0; qi < m; qi++) {
            String q = wordsQuery[qi];
            Node node = root;
            int bestIdx = node.bestIdx; // empty suffix case
            for (int p = q.length() - 1; p >= 0; --p) {
                int c = q.charAt(p) - 'a';
                if (node.next[c] == null) break;
                node = node.next[c];
                bestIdx = node.bestIdx;
            }
            ans[qi] = bestIdx;
        }
        return ans;
    }

    private void updateBest(Node node, int idx, int[] len) {
        if (node.bestIdx == -1) {
            node.bestIdx = idx;
        } else {
            int cur = node.bestIdx;
            if (len[idx] < len[cur] || (len[idx] == len[cur] && idx < cur)) {
                node.bestIdx = idx;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        # Trie node structure: {'next':{}, 'best_idx':int, 'best_len':int}
        nodes = [{'next': {}, 'best_idx': -1, 'best_len': 0}]
        
        def update(node_id, idx, length):
            node = nodes[node_id]
            if node['best_idx'] == -1 or length < node['best_len'] or (length == node['best_len'] and idx < node['best_idx']):
                node['best_idx'] = idx
                node['best_len'] = length
        
        # Build trie with reversed container words
        for idx, word in enumerate(wordsContainer):
            rev = word[::-1]
            cur = 0
            update(cur, idx, len(word))
            for ch in rev:
                nxt = nodes[cur]['next'].get(ch)
                if nxt is None:
                    nxt = len(nodes)
                    nodes.append({'next': {}, 'best_idx': -1, 'best_len': 0})
                    nodes[cur]['next'][ch] = nxt
                cur = nxt
                update(cur, idx, len(word))
        
        # Answer queries
        ans = []
        for q in wordsQuery:
            rev_q = q[::-1]
            cur = 0
            candidate = nodes[cur]['best_idx']
            for ch in rev_q:
                if ch not in nodes[cur]['next']:
                    break
                cur = nodes[cur]['next'][ch]
                candidate = nodes[cur]['best_idx']
            ans.append(candidate)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        n = len(wordsContainer)
        lengths = [len(w) for w in wordsContainer]

        def better(i: int, j: int) -> bool:
            # return True if i is better than j
            li, lj = lengths[i], lengths[j]
            if li != lj:
                return li < lj
            return i < j

        # Trie node structure: {'best': int or None, 'children': dict}
        root = {'best': None, 'children': {}}

        for idx, word in enumerate(wordsContainer):
            rev = word[::-1]
            node = root
            if node['best'] is None or better(idx, node['best']):
                node['best'] = idx
            for ch in rev:
                children = node['children']
                if ch not in children:
                    children[ch] = {'best': None, 'children': {}}
                node = children[ch]
                if node['best'] is None or better(idx, node['best']):
                    node['best'] = idx

        ans: List[int] = []
        for q in wordsQuery:
            rev = q[::-1]
            node = root
            best_idx = node['best']
            for ch in rev:
                if ch not in node['children']:
                    break
                node = node['children'][ch]
                best_idx = node['best']
            ans.append(best_idx)

        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct TrieNode {
    int child[26];
    int bestIdx;
} TrieNode;

static int *contLen;   // lengths of wordsContainer
static TrieNode *nodes;
static int nodeCnt;

/* Return true if idxA is better than idxB according to criteria */
static int isBetter(int idxA, int idxB) {
    if (idxB == -1) return 1;
    if (contLen[idxA] < contLen[idxB]) return 1;
    if (contLen[idxA] > contLen[idxB]) return 0;
    return idxA < idxB;
}

/* Update the best index stored at node */
static void updateBest(int nodeIdx, int candIdx) {
    if (isBetter(candIdx, nodes[nodeIdx].bestIdx))
        nodes[nodeIdx].bestIdx = candIdx;
}

/* Create a new trie node and return its index */
static int newNode() {
    int idx = nodeCnt++;
    for (int i = 0; i < 26; ++i) nodes[idx].child[i] = -1;
    nodes[idx].bestIdx = -1;
    return idx;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* stringIndices(char** wordsContainer, int wordsContainerSize,
                   char** wordsQuery, int wordsQuerySize,
                   int* returnSize) {
    /* Preprocess lengths and total characters */
    contLen = (int*)malloc(wordsContainerSize * sizeof(int));
    long long totalChars = 0;
    for (int i = 0; i < wordsContainerSize; ++i) {
        contLen[i] = (int)strlen(wordsContainer[i]);
        totalChars += contLen[i];
    }

    /* Allocate trie nodes */
    nodes = (TrieNode*)malloc((totalChars + 1) * sizeof(TrieNode));
    nodeCnt = 0;
    newNode();                     // root at index 0

    /* Insert each container word reversed into the trie */
    for (int idx = 0; idx < wordsContainerSize; ++idx) {
        const char *s = wordsContainer[idx];
        int len = contLen[idx];
        int cur = 0;
        updateBest(cur, idx);      // root
        for (int p = len - 1; p >= 0; --p) {
            int c = s[p] - 'a';
            if (nodes[cur].child[c] == -1) {
                nodes[cur].child[c] = newNode();
            }
            cur = nodes[cur].child[c];
            updateBest(cur, idx);
        }
    }

    /* Answer queries */
    int *ans = (int*)malloc(wordsQuerySize * sizeof(int));
    for (int q = 0; q < wordsQuerySize; ++q) {
        const char *s = wordsQuery[q];
        int len = (int)strlen(s);
        int cur = 0;
        int best = nodes[cur].bestIdx;   // root's best (suffix length 0)
        for (int p = len - 1; p >= 0; --p) {
            int c = s[p] - 'a';
            if (nodes[cur].child[c] == -1) break;
            cur = nodes[cur].child[c];
            best = nodes[cur].bestIdx;
        }
        ans[q] = best;
    }

    *returnSize = wordsQuerySize;

    free(contLen);
    free(nodes);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    private string[] container;
    private TrieNode root;

    private class TrieNode {
        public int bestIdx = -1;
        public TrieNode[] child = new TrieNode[26];
    }

    private bool IsBetter(int i, int j) {
        if (container[i].Length != container[j].Length)
            return container[i].Length < container[j].Length;
        return i < j;
    }

    private void UpdateBest(TrieNode node, int idx) {
        if (node.bestIdx == -1 || IsBetter(idx, node.bestIdx))
            node.bestIdx = idx;
    }

    public int[] StringIndices(string[] wordsContainer, string[] wordsQuery) {
        container = wordsContainer;
        root = new TrieNode();

        for (int i = 0; i < wordsContainer.Length; i++) {
            string w = wordsContainer[i];
            TrieNode node = root;
            UpdateBest(node, i);
            for (int p = w.Length - 1; p >= 0; p--) {
                int c = w[p] - 'a';
                if (node.child[c] == null) node.child[c] = new TrieNode();
                node = node.child[c];
                UpdateBest(node, i);
            }
        }

        int[] ans = new int[wordsQuery.Length];
        for (int qi = 0; qi < wordsQuery.Length; qi++) {
            string q = wordsQuery[qi];
            TrieNode node = root;
            for (int p = q.Length - 1; p >= 0; p--) {
                int c = q[p] - 'a';
                if (node.child[c] == null) break;
                node = node.child[c];
            }
            ans[qi] = node.bestIdx;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} wordsContainer
 * @param {string[]} wordsQuery
 * @return {number[]}
 */
var stringIndices = function(wordsContainer, wordsQuery) {
    const n = wordsContainer.length;
    const lengths = new Array(n);
    for (let i = 0; i < n; ++i) lengths[i] = wordsContainer[i].length;

    // Trie structures
    const next = [];   // array of Int32Array(26)
    const best = [];   // best index at each node

    function addNode() {
        next.push(new Int32Array(26).fill(-1));
        best.push(-1);
        return next.length - 1;
    }

    function better(a, b) { // returns true if a is better than b
        if (b === -1) return true;
        if (lengths[a] < lengths[b]) return true;
        if (lengths[a] === lengths[b] && a < b) return true;
        return false;
    }

    function update(node, idx) {
        if (better(idx, best[node])) best[node] = idx;
    }

    // initialize root
    addNode(); // node 0

    // Build trie with reversed words
    for (let i = 0; i < n; ++i) {
        const s = wordsContainer[i];
        let node = 0;
        update(node, i);
        for (let j = s.length - 1; j >= 0; --j) {
            const ch = s.charCodeAt(j) - 97;
            if (next[node][ch] === -1) {
                next[node][ch] = addNode();
            }
            node = next[node][ch];
            update(node, i);
        }
    }

    // Answer queries
    const m = wordsQuery.length;
    const ans = new Array(m);
    for (let i = 0; i < m; ++i) {
        const q = wordsQuery[i];
        let node = 0;
        for (let j = q.length - 1; j >= 0; --j) {
            const ch = q.charCodeAt(j) - 97;
            if (next[node][ch] === -1) break;
            node = next[node][ch];
        }
        ans[i] = best[node];
    }

    return ans;
};
```

## Typescript

```typescript
function stringIndices(wordsContainer: string[], wordsQuery: string[]): number[] {
    const n = wordsContainer.length;
    const lengths = new Int32Array(n);
    for (let i = 0; i < n; ++i) lengths[i] = wordsContainer[i].length;

    const next: number[][] = [];
    const best: number[] = [];

    function newNode(): number {
        next.push(new Array(26).fill(-1));
        best.push(-1);
        return next.length - 1;
    }
    newNode(); // root at index 0

    function isBetter(i: number, j: number): boolean {
        if (j === -1) return true;
        const li = lengths[i];
        const lj = lengths[j];
        if (li !== lj) return li < lj;
        return i < j;
    }

    function update(nodeIdx: number, wordIdx: number): void {
        if (isBetter(wordIdx, best[nodeIdx])) best[nodeIdx] = wordIdx;
    }

    // Build trie with reversed words
    for (let idx = 0; idx < n; ++idx) {
        const w = wordsContainer[idx];
        let node = 0;
        update(node, idx);
        for (let p = w.length - 1; p >= 0; --p) {
            const c = w.charCodeAt(p) - 97;
            if (next[node][c] === -1) next[node][c] = newNode();
            node = next[node][c];
            update(node, idx);
        }
    }

    const ans: number[] = new Array(wordsQuery.length);
    for (let qi = 0; qi < wordsQuery.length; ++qi) {
        const q = wordsQuery[qi];
        let node = 0;
        for (let p = q.length - 1; p >= 0; --p) {
            const c = q.charCodeAt(p) - 97;
            const nxt = next[node][c];
            if (nxt === -1) break;
            node = nxt;
        }
        ans[qi] = best[node];
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $wordsContainer
     * @param String[] $wordsQuery
     * @return Integer[]
     */
    function stringIndices($wordsContainer, $wordsQuery) {
        $n = count($wordsContainer);
        $lenArr = [];
        foreach ($wordsContainer as $i => $w) {
            $lenArr[$i] = strlen($w);
        }

        // Trie: each node has 'next' (char=>nodeIdx) and 'best' (index of best word)
        $trie = [];
        $trie[] = ['next' => [], 'best' => -1]; // root at index 0

        // Build trie with reversed words, updating best at each node
        for ($idx = 0; $idx < $n; ++$idx) {
            $word = $wordsContainer[$idx];
            $node = 0;

            // update root best
            $curBest = $trie[$node]['best'];
            if ($curBest == -1 ||
                $lenArr[$idx] < $lenArr[$curBest] ||
                ($lenArr[$idx] == $lenArr[$curBest] && $idx < $curBest)) {
                $trie[$node]['best'] = $idx;
            }

            for ($i = strlen($word) - 1; $i >= 0; --$i) {
                $c = $word[$i];
                if (!isset($trie[$node]['next'][$c])) {
                    $trie[] = ['next' => [], 'best' => -1];
                    $trie[$node]['next'][$c] = count($trie) - 1;
                }
                $node = $trie[$node]['next'][$c];

                // update best at this node
                $curBest = $trie[$node]['best'];
                if ($curBest == -1 ||
                    $lenArr[$idx] < $lenArr[$curBest] ||
                    ($lenArr[$idx] == $lenArr[$curBest] && $idx < $curBest)) {
                    $trie[$node]['best'] = $idx;
                }
            }
        }

        // Answer queries
        $ans = [];
        foreach ($wordsQuery as $q) {
            $node = 0;
            $deepNode = 0; // deepest node reached (including root)
            for ($i = strlen($q) - 1; $i >= 0; --$i) {
                $c = $q[$i];
                if (isset($trie[$node]['next'][$c])) {
                    $node = $trie[$node]['next'][$c];
                    $deepNode = $node;
                } else {
                    break;
                }
            }
            $ans[] = $trie[$deepNode]['best'];
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    class Node {
        var children: [Int:Int] = [:]
        var bestIdx: Int = -1
    }
    
    func stringIndices(_ wordsContainer: [String], _ wordsQuery: [String]) -> [Int] {
        let n = wordsContainer.count
        var lengths = [Int](repeating: 0, count: n)
        for i in 0..<n { lengths[i] = wordsContainer[i].count }
        
        func isBetter(_ cand: Int, _ cur: Int) -> Bool {
            if cur == -1 { return true }
            let lenCand = lengths[cand]
            let lenCur = lengths[cur]
            if lenCand != lenCur {
                return lenCand < lenCur
            } else {
                return cand < cur
            }
        }
        
        var nodes: [Node] = [Node()]   // root at index 0
        
        for idx in 0..<n {
            let bytes = Array(wordsContainer[idx].utf8)
            var nodeIdx = 0
            if isBetter(idx, nodes[nodeIdx].bestIdx) {
                nodes[nodeIdx].bestIdx = idx
            }
            for b in bytes.reversed() {
                let c = Int(b - 97)   // 'a' ascii = 97
                if let next = nodes[nodeIdx].children[c] {
                    nodeIdx = next
                } else {
                    let newNode = Node()
                    nodes.append(newNode)
                    let newIndex = nodes.count - 1
                    nodes[nodeIdx].children[c] = newIndex
                    nodeIdx = newIndex
                }
                if isBetter(idx, nodes[nodeIdx].bestIdx) {
                    nodes[nodeIdx].bestIdx = idx
                }
            }
        }
        
        var result: [Int] = []
        for query in wordsQuery {
            let bytes = Array(query.utf8)
            var nodeIdx = 0
            var answer = nodes[0].bestIdx   // root best (suffix length 0)
            for b in bytes.reversed() {
                let c = Int(b - 97)
                guard let next = nodes[nodeIdx].children[c] else { break }
                nodeIdx = next
                answer = nodes[nodeIdx].bestIdx
            }
            result.append(answer)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun stringIndices(wordsContainer: Array<String>, wordsQuery: Array<String>): IntArray {
        val n = wordsContainer.size
        val lengths = IntArray(n) { wordsContainer[it].length }

        // Trie structures
        val children = mutableListOf<IntArray>()
        val bestIdx = mutableListOf<Int>()

        fun newNode(): Int {
            children.add(IntArray(26) { -1 })
            bestIdx.add(-1)
            return children.size - 1
        }

        fun isBetter(newIdx: Int, curIdx: Int): Boolean {
            if (curIdx == -1) return true
            val lenNew = lengths[newIdx]
            val lenCur = lengths[curIdx]
            if (lenNew != lenCur) return lenNew < lenCur
            return newIdx < curIdx
        }

        val root = newNode()

        // Insert reversed container words into the trie
        for (idx in 0 until n) {
            var node = root
            if (isBetter(idx, bestIdx[node])) bestIdx[node] = idx
            val word = wordsContainer[idx]
            for (i in word.length - 1 downTo 0) {
                val c = word[i] - 'a'
                var child = children[node][c]
                if (child == -1) {
                    child = newNode()
                    children[node][c] = child
                }
                node = child
                if (isBetter(idx, bestIdx[node])) bestIdx[node] = idx
            }
        }

        val m = wordsQuery.size
        val ans = IntArray(m)
        for (i in 0 until m) {
            var node = root
            var answer = bestIdx[node]
            val q = wordsQuery[i]
            for (j in q.length - 1 downTo 0) {
                val c = q[j] - 'a'
                val child = children[node][c]
                if (child == -1) break
                node = child
                answer = bestIdx[node] // deeper suffix overrides previous
            }
            ans[i] = answer
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> stringIndices(List<String> wordsContainer, List<String> wordsQuery) {
    // Store lengths for comparison
    final int n = wordsContainer.length;
    final List<int> lengths = List.filled(n, 0);
    for (int i = 0; i < n; ++i) lengths[i] = wordsContainer[i].length;

    // Trie node definition
    class Node {
      List<int> next = List.filled(26, -1);
      int best = -1;
    }

    bool isBetter(int cand, int cur) {
      if (cur == -1) return true;
      if (lengths[cand] < lengths[cur]) return true;
      if (lengths[cand] == lengths[cur] && cand < cur) return true;
      return false;
    }

    // Build trie with reversed words
    final List<Node> trie = [Node()];
    for (int idx = 0; idx < n; ++idx) {
      String w = wordsContainer[idx];
      int node = 0;
      if (isBetter(idx, trie[node].best)) trie[node].best = idx;
      for (int j = w.length - 1; j >= 0; --j) {
        int ch = w.codeUnitAt(j) - 97;
        if (trie[node].next[ch] == -1) {
          trie[node].next[ch] = trie.length;
          trie.add(Node());
        }
        node = trie[node].next[ch];
        if (isBetter(idx, trie[node].best)) trie[node].best = idx;
      }
    }

    // Answer queries
    final List<int> ans = List.filled(wordsQuery.length, 0);
    for (int qi = 0; qi < wordsQuery.length; ++qi) {
      String q = wordsQuery[qi];
      int node = 0;
      int bestIdx = trie[node].best; // root best (empty suffix)
      for (int j = q.length - 1; j >= 0; --j) {
        int ch = q.codeUnitAt(j) - 97;
        int nxt = trie[node].next[ch];
        if (nxt == -1) break;
        node = nxt;
        bestIdx = trie[node].best;
      }
      ans[qi] = bestIdx;
    }

    return ans;
  }
}
```

## Golang

```go
func stringIndices(wordsContainer []string, wordsQuery []string) []int {
	type Node struct {
		child [26]int
		best  int
	}
	newNode := func() Node {
		n := Node{best: -1}
		for i := 0; i < 26; i++ {
			n.child[i] = -1
		}
		return n
	}
	better := func(newIdx, curIdx int, lens []int) bool {
		if curIdx == -1 {
			return true
		}
		if lens[newIdx] < lens[curIdx] {
			return true
		}
		if lens[newIdx] == lens[curIdx] && newIdx < curIdx {
			return true
		}
		return false
	}

	m := len(wordsContainer)
	lens := make([]int, m)
	for i, w := range wordsContainer {
		lens[i] = len(w)
	}

	nodes := []Node{newNode()}

	// Build trie with reversed strings
	for idx, w := range wordsContainer {
		node := 0
		if better(idx, nodes[node].best, lens) {
			nodes[node].best = idx
		}
		for i := len(w) - 1; i >= 0; i-- {
			c := w[i] - 'a'
			next := nodes[node].child[c]
			if next == -1 {
				nodes = append(nodes, newNode())
				next = len(nodes) - 1
				nodes[node].child[c] = next
			}
			node = next
			if better(idx, nodes[node].best, lens) {
				nodes[node].best = idx
			}
		}
	}

	// Answer queries
	ans := make([]int, len(wordsQuery))
	for qi, q := range wordsQuery {
		bestIdx := nodes[0].best
		node := 0
		for i := len(q) - 1; i >= 0; i-- {
			c := q[i] - 'a'
			next := nodes[node].child[c]
			if next == -1 {
				break
			}
			node = next
			bestIdx = nodes[node].best
		}
		ans[qi] = bestIdx
	}
	return ans
}
```

## Ruby

```ruby
class Node
  attr_accessor :children, :best_idx

  def initialize
    @children = Array.new(26)
    @best_idx = -1
  end
end

def better?(idx_a, idx_b, lengths)
  return true if idx_b == -1
  len_a = lengths[idx_a]
  len_b = lengths[idx_b]
  if len_a < len_b
    true
  elsif len_a > len_b
    false
  else
    idx_a < idx_b
  end
end

def string_indices(words_container, words_query)
  n = words_container.size
  lengths = Array.new(n) { |i| words_container[i].length }

  root = Node.new

  # Insert reversed container words into trie
  words_container.each_with_index do |word, idx|
    node = root
    if better?(idx, node.best_idx, lengths)
      node.best_idx = idx
    end
    word.reverse.each_byte do |b|
      c = b - 97
      child = node.children[c]
      unless child
        child = Node.new
        node.children[c] = child
      end
      node = child
      if better?(idx, node.best_idx, lengths)
        node.best_idx = idx
      end
    end
  end

  result = []

  words_query.each do |q|
    node = root
    ans = node.best_idx
    q.reverse.each_byte do |b|
      c = b - 97
      child = node.children[c]
      break unless child
      node = child
      ans = node.best_idx
    end
    result << ans
  end

  result
end
```

## Scala

```scala
object Solution {
    def stringIndices(wordsContainer: Array[String], wordsQuery: Array[String]): Array[Int] = {
        val n = wordsContainer.length
        val lens = new Array[Int](n)
        var i = 0
        while (i < n) {
            lens(i) = wordsContainer(i).length
            i += 1
        }

        case class Node(children: Array[Int], var best: Int)

        val nodes = scala.collection.mutable.ArrayBuffer[Node]()
        def newNode(): Int = {
            nodes += Node(Array.fill(26)(-1), -1)
            nodes.length - 1
        }
        newNode() // root at index 0

        def better(a: Int, b: Int): Boolean = {
            if (lens(a) != lens(b)) lens(a) < lens(b) else a < b
        }

        def updateBest(nodeIdx: Int, idx: Int): Unit = {
            val node = nodes(nodeIdx)
            if (node.best == -1 || better(idx, node.best)) node.best = idx
        }

        // Build trie with reversed container strings
        var idx = 0
        while (idx < n) {
            var cur = 0
            updateBest(cur, idx)
            val s = wordsContainer(idx)
            var pos = s.length - 1
            while (pos >= 0) {
                val c = s.charAt(pos) - 'a'
                var child = nodes(cur).children(c)
                if (child == -1) {
                    child = newNode()
                    nodes(cur).children(c) = child
                }
                cur = child
                updateBest(cur, idx)
                pos -= 1
            }
            idx += 1
        }

        val m = wordsQuery.length
        val ans = new Array[Int](m)

        var qIdx = 0
        while (qIdx < m) {
            var cur = 0
            var bestIdx = nodes(cur).best // root's best (global)
            val q = wordsQuery(qIdx)
            var pos = q.length - 1
            var continue = true
            while (pos >= 0 && continue) {
                val c = q.charAt(pos) - 'a'
                val child = nodes(cur).children(c)
                if (child == -1) {
                    continue = false
                } else {
                    cur = child
                    bestIdx = nodes(cur).best
                    pos -= 1
                }
            }
            ans(qIdx) = bestIdx
            qIdx += 1
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn string_indices(words_container: Vec<String>, words_query: Vec<String>) -> Vec<i32> {
        let n = words_container.len();
        let mut lens = vec![0usize; n];
        for (i, w) in words_container.iter().enumerate() {
            lens[i] = w.len();
        }

        #[derive(Clone)]
        struct Node {
            next: [i32; 26],
            best: i32,
        }
        impl Node {
            fn new() -> Self {
                Node { next: [-1; 26], best: -1 }
            }
        }

        fn is_better(a_idx: usize, b_idx: i32, lens: &Vec<usize>) -> bool {
            if b_idx == -1 {
                return true;
            }
            let b = b_idx as usize;
            if lens[a_idx] < lens[b] {
                true
            } else if lens[a_idx] == lens[b] && a_idx < b {
                true
            } else {
                false
            }
        }

        let mut trie: Vec<Node> = Vec::new();
        trie.push(Node::new()); // root

        for (idx, word) in words_container.iter().enumerate() {
            if is_better(idx, trie[0].best, &lens) {
                trie[0].best = idx as i32;
            }
            let mut node = 0usize;
            for &b in word.as_bytes().iter().rev() {
                let c = (b - b'a') as usize;
                let next_idx = trie[node].next[c];
                if next_idx == -1 {
                    trie.push(Node::new());
                    let new_index = (trie.len() - 1) as i32;
                    trie[node].next[c] = new_index;
                    node = new_index as usize;
                } else {
                    node = next_idx as usize;
                }
                if is_better(idx, trie[node].best, &lens) {
                    trie[node].best = idx as i32;
                }
            }
        }

        let mut result: Vec<i32> = Vec::with_capacity(words_query.len());
        for q in words_query.iter() {
            let mut node = 0usize;
            let mut ans = trie[0].best; // empty suffix case
            for &b in q.as_bytes().iter().rev() {
                let c = (b - b'a') as usize;
                let next_idx = trie[node].next[c];
                if next_idx == -1 {
                    break;
                }
                node = next_idx as usize;
                ans = trie[node].best;
            }
            result.push(ans);
        }

        result
    }
}
```

## Racket

```racket
(define/contract (string-indices wordsContainer wordsQuery)
  (-> (listof string?) (listof string?) (listof exact-integer?))
  (let* ((n (length wordsContainer))
         (root (node (make-hash) -1)))
    ;; struct definition
    (struct node (children best) #:mutable)

    ;; comparison according to problem criteria
    (define (better? i1 i2)
      (cond [(= i2 -1) #t]
            [else
             (let* ((len1 (string-length (list-ref wordsContainer i1)))
                    (len2 (string-length (list-ref wordsContainer i2))))
               (or (< len1 len2)
                   (and (= len1 len2) (< i1 i2))))]))

    ;; insert each word into the reversed trie
    (for ([idx (in-range n)])
      (let* ((word (list-ref wordsContainer idx))
             (rev  (list->string (reverse (string->list word)))))
        (define cur root)
        (when (better? idx (node-best cur))
          (set-node-best! cur idx))
        (for ([ch (in-string rev)])
          (let ((child (hash-ref (node-children cur) ch #f)))
            (unless child
              (set! child (node (make-hash) -1))
              (hash-set! (node-children cur) ch child))
            (set! cur child)
            (when (better? idx (node-best cur))
              (set-node-best! cur idx))))))

    ;; query helper: find best index for a single query string
    (define (query q)
      (let* ((rev (list->string (reverse (string->list q)))))
        (let loop ((i 0) (cur root) (best (node-best root)) (len (string-length rev)))
          (if (= i len)
              best
              (let* ((ch (string-ref rev i))
                     (child (hash-ref (node-children cur) ch #f)))
                (if child
                    (loop (+ i 1) child (node-best child) len)
                    best))))))

    ;; process all queries
    (map query wordsQuery)))
```

## Erlang

```erlang
-module(solution).
-export([string_indices/2]).

-spec string_indices(WordsContainer :: [unicode:unicode_binary()], WordsQuery :: [unicode:unicode_binary()]) -> [integer()].
string_indices(WordsContainer, WordsQuery) ->
    Trie = build_trie(WordsContainer),
    [query_answer(Q, Trie) || Q <- WordsQuery].

build_trie(Words) ->
    EmptyNode = #{best => none, childs => #{}},
    lists:foldl(fun({Word, Idx}, AccTrie) ->
        Rev = lists:reverse(binary_to_list(Word)),
        Len = byte_size(Word),
        insert_word(Rev, Idx, Len, AccTrie)
    end,
    EmptyNode,
    indexed(Words, 0)).

indexed([], _Idx) -> [];
indexed([W|Rest], I) -> [{W, I} | indexed(Rest, I+1)].

insert_word([], Idx, Len, Node) ->
    update_best(Node, Idx, Len);
insert_word([C|Cs], Idx, Len, Node0) ->
    Node1 = update_best(Node0, Idx, Len),
    Children = maps:get(childs, Node1),
    ChildNode0 = maps:get(C, Children, #{best => none, childs => #{}}),
    UpdatedChild = insert_word(Cs, Idx, Len, ChildNode0),
    NewChildren = maps:put(C, UpdatedChild, Children),
    Node1#{childs := NewChildren}.

update_best(Node, Idx, Len) ->
    case maps:get(best, Node) of
        none -> Node#{best => {Idx, Len}};
        {CurIdx, CurLen} ->
            if Len < CurLen orelse (Len == CurLen andalso Idx < CurIdx) ->
                    Node#{best => {Idx, Len}};
               true -> Node
            end
    end.

query_answer(Query, Trie) ->
    Rev = lists:reverse(binary_to_list(Query)),
    query_traverse(Rev, Trie).

query_traverse([], Node) ->
    {Idx,_} = maps:get(best, Node),
    Idx;
query_traverse([C|Cs], Node) ->
    Children = maps:get(childs, Node),
    case maps:find(C, Children) of
        {ok, Child} -> query_traverse(Cs, Child);
        error ->
            {Idx,_} = maps:get(best, Node),
            Idx
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec string_indices(words_container :: [String.t()], words_query :: [String.t()]) :: [integer()]
  def string_indices(words_container, words_query) do
    lengths = for {w, i} <- Enum.with_index(words_container), into: %{}, do: {i, String.length(w)}

    trie =
      Enum.reduce(Enum.with_index(words_container), %{}, fn {word, idx}, acc ->
        rev = String.reverse(word)
        len = Map.fetch!(lengths, idx)
        insert_word(acc, String.graphemes(rev), idx, len, lengths)
      end)

    for query <- words_query do
      rev_q = String.reverse(query)
      node = traverse(trie, String.graphemes(rev_q))
      Map.fetch!(node, :best)
    end
  end

  defp insert_word(node, [], idx, _len, _lengths) do
    maybe_update_best(node, idx, _len)
  end

  defp insert_word(node, [ch | rest], idx, len, lengths) do
    child = Map.get(node, ch, %{})
    updated_child = insert_word(child, rest, idx, len, lengths)

    node
    |> maybe_update_best(idx, len)
    |> Map.put(ch, updated_child)
  end

  defp maybe_update_best(node, idx, len) do
    case Map.fetch(node, :best) do
      :error ->
        Map.put(node, :best, idx)

      {:ok, cur_idx} ->
        cur_len = String.length(Enum.at([], 0)) # placeholder, will be replaced below
        # Since we don't have lengths here, compare using external map via closure.
        # We'll compute comparison outside this function.
        node
    end
  end

  # Revised approach: store best based on length and index directly in node as {len, idx}
  defp insert_word(node, [], idx, len, _lengths) do
    update_best(node, idx, len)
  end

  defp insert_word(node, [ch | rest], idx, len, lengths) do
    child = Map.get(node, ch, %{})
    updated_child = insert_word(child, rest, idx, len, lengths)

    node
    |> update_best(idx, len)
    |> Map.put(ch, updated_child)
  end

  defp update_best(node, idx, len) do
    case Map.fetch(node, :best) do
      :error ->
        Map.put(node, :best, {len, idx})

      {:ok, {cur_len, cur_idx}} ->
        if better?(len, idx, cur_len, cur_idx) do
          Map.put(node, :best, {len, idx})
        else
          node
        end
    end
  end

  defp better?(len1, idx1, len2, idx2) do
    cond do
      len1 < len2 -> true
      len1 > len2 -> false
      true -> idx1 < idx2
    end
  end

  defp traverse(node, []), do: node

  defp traverse(node, [ch | rest]) do
    case Map.get(node, ch) do
      nil -> node
      child -> traverse(child, rest)
    end
  end

  # After traversal we need to extract index from stored {len, idx}
  defp fetch_best_index(node) do
    {_len, idx} = Map.fetch!(node, :best)
    idx
  end

  # Adjust query processing to use fetch_best_index
  defp string_indices(words_container, words_query) do
    lengths = for {w, i} <- Enum.with_index(words_container), into: %{}, do: {i, String.length(w)}

    trie =
      Enum.reduce(Enum.with_index(words_container), %{}, fn {word, idx}, acc ->
        rev = String.reverse(word)
        len = Map.fetch!(lengths, idx)
        insert_word(acc, String.graphemes(rev), idx, len, lengths)
      end)

    for query <- words_query do
      rev_q = String.reverse(query)
      node = traverse(trie, String.graphemes(rev_q))
      fetch_best_index(node)
    end
  end
end
```
