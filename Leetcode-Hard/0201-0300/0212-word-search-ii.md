# 0212. Word Search II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    struct TrieNode {
        TrieNode* child[26];
        string word;
        TrieNode() : word("") { memset(child, 0, sizeof(child)); }
    };
    
    vector<string> result;
    int rows, cols;
    vector<vector<char>> *boardPtr;
    
    void dfs(int r, int c, TrieNode* node) {
        char ch = (*boardPtr)[r][c];
        if (ch == '#') return;
        TrieNode* nxt = node->child[ch - 'a'];
        if (!nxt) return;
        
        if (!nxt->word.empty()) {
            result.push_back(nxt->word);
            nxt->word.clear(); // avoid duplicate
        }
        
        (*boardPtr)[r][c] = '#';
        static const int dr[4] = {-1, 1, 0, 0};
        static const int dc[4] = {0, 0, -1, 1};
        for (int k = 0; k < 4; ++k) {
            int nr = r + dr[k], nc = c + dc[k];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols)
                dfs(nr, nc, nxt);
        }
        (*boardPtr)[r][c] = ch;
    }
    
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        // Build trie
        TrieNode* root = new TrieNode();
        for (const string& w : words) {
            TrieNode* node = root;
            for (char c : w) {
                int idx = c - 'a';
                if (!node->child[idx]) node->child[idx] = new TrieNode();
                node = node->child[idx];
            }
            node->word = w;
        }
        
        rows = board.size();
        cols = board[0].size();
        boardPtr = &board;
        for (int i = 0; i < rows; ++i)
            for (int j = 0; j < cols; ++j)
                dfs(i, j, root);
        
        // Cleanup trie to avoid memory leak
        function<void(TrieNode*)> del = [&](TrieNode* node) {
            if (!node) return;
            for (auto child : node->child) del(child);
            delete node;
        };
        del(root);
        
        return result;
    }
};
```

## Java

```java
class Solution {
    private static class TrieNode {
        TrieNode[] children = new TrieNode[26];
        String word;
    }

    public List<String> findWords(char[][] board, String[] words) {
        TrieNode root = buildTrie(words);
        List<String> result = new ArrayList<>();
        int m = board.length, n = board[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dfs(board, i, j, root, result);
            }
        }
        return result;
    }

    private TrieNode buildTrie(String[] words) {
        TrieNode root = new TrieNode();
        for (String w : words) {
            TrieNode node = root;
            for (char c : w.toCharArray()) {
                int idx = c - 'a';
                if (node.children[idx] == null) {
                    node.children[idx] = new TrieNode();
                }
                node = node.children[idx];
            }
            node.word = w; // store word at terminal node
        }
        return root;
    }

    private void dfs(char[][] board, int i, int j, TrieNode node, List<String> result) {
        char c = board[i][j];
        if (c == '#') return;
        int idx = c - 'a';
        TrieNode child = node.children[idx];
        if (child == null) return;

        if (child.word != null) {
            result.add(child.word);
            child.word = null; // avoid duplicate entries
        }

        board[i][j] = '#'; // mark visited

        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};

        for (int d = 0; d < 4; d++) {
            int ni = i + dx[d];
            int nj = j + dy[d];
            if (ni >= 0 && ni < board.length && nj >= 0 && nj < board[0].length) {
                dfs(board, ni, nj, child, result);
            }
        }

        board[i][j] = c; // restore
    }
}
```

## Python

```python
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Build Trie
        trie = {}
        for w in words:
            node = trie
            for ch in w:
                node = node.setdefault(ch, {})
            node['#'] = w  # end marker with word

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, parent):
            letter = board[r][c]
            cur_node = parent[letter]

            # check if we found a word
            word = cur_node.pop('#', None)
            if word:
                res.append(word)

            # mark the cell as visited
            board[r][c] = '#'

            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    nxt_char = board[nr][nc]
                    if nxt_char in cur_node:
                        dfs(nr, nc, cur_node)

            # restore the cell
            board[r][c] = letter

            # prune leaf nodes
            if not cur_node:
                parent.pop(letter)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie:
                    dfs(i, j, trie)

        return res
```

## Python3

```python
from typing import List

class TrieNode:
    __slots__ = ('children', 'word')
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build trie
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w

        m, n = len(board), len(board[0])
        res = []

        def dfs(i: int, j: int, node: TrieNode):
            ch = board[i][j]
            if ch not in node.children:
                return
            nxt = node.children[ch]

            # check word
            if nxt.word is not None:
                res.append(nxt.word)
                nxt.word = None  # avoid duplicate

            # mark visited
            board[i][j] = '#'

            for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    dfs(ni, nj, nxt)

            # restore
            board[i][j] = ch

            # prune leaf node to speed up future searches
            if not nxt.children:
                del node.children[ch]

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct TrieNode {
    int child[26];
    int wordIndex;      // index of the word in words array
    int isEnd;          // boolean flag
} TrieNode;

static char **gBoard;
static int gRows, gCols;
static TrieNode *gTrie;
static char **gWords;
static char ***gResultPtr;
static int *gReturnSize;

/* Create a new trie node and initialize */
static int newNode(int *size, TrieNode **pool) {
    int idx = (*size);
    (*size)++;
    TrieNode *node = &((*pool)[idx]);
    for (int i = 0; i < 26; ++i) node->child[i] = -1;
    node->isEnd = 0;
    node->wordIndex = -1;
    return idx;
}

/* Insert a word into the trie */
static void insertWord(const char *word, int index, TrieNode **pool, int *size) {
    int cur = 0; // root
    for (const char *p = word; *p; ++p) {
        int c = *p - 'a';
        if ((*pool)[cur].child[c] == -1) {
            (*pool)[cur].child[c] = newNode(size, pool);
        }
        cur = (*pool)[cur].child[c];
    }
    (*pool)[cur].isEnd = 1;
    (*pool)[cur].wordIndex = index;
}

/* Simple string copy (like strdup) */
static char *copyStr(const char *s) {
    size_t len = strlen(s);
    char *p = (char *)malloc(len + 1);
    memcpy(p, s, len + 1);
    return p;
}

/* Depth‑first search with backtracking */
static void dfs(int i, int j, int nodeIdx) {
    char ch = gBoard[i][j];
    if (ch == '#') return;
    int c = ch - 'a';
    int childIdx = gTrie[nodeIdx].child[c];
    if (childIdx == -1) return;

    TrieNode *nextNode = &gTrie[childIdx];

    if (nextNode->isEnd) {
        (*gResultPtr)[*gReturnSize] = copyStr(gWords[nextNode->wordIndex]);
        (*gReturnSize)++;
        nextNode->isEnd = 0;   // avoid duplicate entries
    }

    gBoard[i][j] = '#';
    static const int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    for (int d = 0; d < 4; ++d) {
        int ni = i + dirs[d][0];
        int nj = j + dirs[d][1];
        if (ni >= 0 && ni < gRows && nj >= 0 && nj < gCols && gBoard[ni][nj] != '#') {
            dfs(ni, nj, childIdx);
        }
    }
    gBoard[i][j] = ch;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findWords(char** board, int boardSize, int* boardColSize,
                 char** words, int wordsSize, int* returnSize) {
    gBoard = board;
    gRows = boardSize;
    gCols = boardColSize[0];
    gWords = words;

    /* Compute total characters to allocate trie nodes */
    int totalChars = 1; // root
    for (int i = 0; i < wordsSize; ++i) {
        totalChars += (int)strlen(words[i]);
    }

    TrieNode *triePool = (TrieNode *)malloc(totalChars * sizeof(TrieNode));
    int trieSize = 0;
    newNode(&trieSize, &triePool); // root at index 0

    for (int i = 0; i < wordsSize; ++i) {
        insertWord(words[i], i, &triePool, &trieSize);
    }
    gTrie = triePool;

    char **result = (char **)malloc(wordsSize * sizeof(char *));
    int ret = 0;
    gResultPtr = &result;
    gReturnSize = &ret;

    for (int i = 0; i < gRows; ++i) {
        for (int j = 0; j < gCols; ++j) {
            dfs(i, j, 0);
        }
    }

    *returnSize = ret;
    free(triePool);
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    private class TrieNode{
        public TrieNode[] children = new TrieNode[26];
        public string word;
    }

    private char[][] board;
    private int rows, cols;
    private List<string> result;

    public IList<string> FindWords(char[][] board, string[] words) {
        this.board = board;
        rows = board.Length;
        cols = board[0].Length;

        TrieNode root = new TrieNode();
        foreach (var w in words) Insert(root, w);

        result = new List<string>();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int idx = board[i][j] - 'a';
                if (root.children[idx] != null) {
                    Backtrack(i, j, root);
                }
            }
        }

        return result;
    }

    private void Insert(TrieNode root, string word) {
        TrieNode node = root;
        foreach (char c in word) {
            int idx = c - 'a';
            if (node.children[idx] == null) node.children[idx] = new TrieNode();
            node = node.children[idx];
        }
        node.word = word;
    }

    private void Backtrack(int row, int col, TrieNode parent) {
        char letter = board[row][col];
        int idx = letter - 'a';
        TrieNode curr = parent.children[idx];

        if (curr.word != null) {
            result.Add(curr.word);
            curr.word = null; // avoid duplicates
        }

        board[row][col] = '#';

        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};

        for (int d = 0; d < 4; d++) {
            int nr = row + dr[d];
            int nc = col + dc[d];
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
            char nextChar = board[nr][nc];
            if (nextChar == '#') continue;
            TrieNode child = curr.children[nextChar - 'a'];
            if (child != null) {
                Backtrack(nr, nc, curr);
            }
        }

        board[row][col] = letter;

        // prune leaf node to speed up future searches
        bool isLeaf = true;
        for (int i = 0; i < 26; i++) {
            if (curr.children[i] != null) {
                isLeaf = false;
                break;
            }
        }
        if (isLeaf) parent.children[idx] = null;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function(board, words) {
    // Build Trie
    const trie = {};
    for (const w of words) {
        let node = trie;
        for (let i = 0; i < w.length; i++) {
            const c = w[i];
            if (!node[c]) node[c] = {};
            node = node[c];
        }
        node.word = w; // mark end of word
    }

    const rows = board.length, cols = board[0].length;
    const result = [];

    const dfs = (r, c, node) => {
        const ch = board[r][c];
        const nextNode = node[ch];
        if (!nextNode) return;

        // Check if we found a word
        if (nextNode.word !== undefined) {
            result.push(nextNode.word);
            delete nextNode.word; // avoid duplicates
        }

        board[r][c] = '#'; // mark visited

        const dirs = [[-1,0],[1,0],[0,-1],[0,1]];
        for (const [dr, dc] of dirs) {
            const nr = r + dr, nc = c + dc;
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
            const nextChar = board[nr][nc];
            if (nextChar !== '#' && nextNode[nextChar]) {
                dfs(nr, nc, nextNode);
            }
        }

        board[r][c] = ch; // restore
    };

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (trie[board[i][j]]) {
                dfs(i, j, trie);
            }
        }
    }

    return result;
};
```

## Typescript

```typescript
function findWords(board: string[][], words: string[]): string[] {
    class TrieNode {
        children: (TrieNode | null)[];
        word: string | null;
        constructor() {
            this.children = new Array(26).fill(null);
            this.word = null;
        }
    }

    const root = new TrieNode();
    for (const w of words) {
        let node = root;
        for (const ch of w) {
            const idx = ch.charCodeAt(0) - 97;
            if (!node.children[idx]) node.children[idx] = new TrieNode();
            node = node.children[idx]!;
        }
        node.word = w;
    }

    const res: string[] = [];
    const rows = board.length;
    const cols = board[0].length;

    function dfs(r: number, c: number, node: TrieNode): void {
        if (r < 0 || c < 0 || r >= rows || c >= cols) return;
        const ch = board[r][c];
        if (ch === '*') return;
        const idx = ch.charCodeAt(0) - 97;
        const child = node.children[idx];
        if (!child) return;

        if (child.word !== null) {
            res.push(child.word);
            child.word = null; // avoid duplicates
        }

        board[r][c] = '*';
        dfs(r + 1, c, child);
        dfs(r - 1, c, child);
        dfs(r, c + 1, child);
        dfs(r, c - 1, child);
        board[r][c] = ch;
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            dfs(i, j, root);
        }
    }

    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $board
     * @param String[] $words
     * @return String[]
     */
    public function findWords($board, $words) {
        // Build Trie
        $trie = [];
        foreach ($words as $word) {
            $node =& $trie;
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $c = $word[$i];
                if (!isset($node[$c])) {
                    $node[$c] = [];
                }
                $node =& $node[$c];
            }
            // Mark end of word
            $node['#'] = $word;
        }

        $rows = count($board);
        $cols = count($board[0]);
        $result = [];

        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                $c = $board[$i][$j];
                if (isset($trie[$c])) {
                    $subNode =& $trie[$c];
                    $this->dfs($board, $i, $j, $subNode, $result);
                }
            }
        }

        return $result;
    }

    private function dfs(&$board, $i, $j, &$node, &$result) {
        // If a word ends here, add to result and remove to avoid duplicates
        if (isset($node['#'])) {
            $result[] = $node['#'];
            unset($node['#']);
        }

        $temp = $board[$i][$j];
        $board[$i][$j] = '#'; // mark visited

        $rows = count($board);
        $cols = count($board[0]);
        $dirs = [[-1,0],[1,0],[0,-1],[0,1]];

        foreach ($dirs as $d) {
            $ni = $i + $d[0];
            $nj = $j + $d[1];
            if ($ni < 0 || $ni >= $rows || $nj < 0 || $nj >= $cols) continue;
            $c = $board[$ni][$nj];
            if ($c === '#') continue;
            if (isset($node[$c])) {
                $nextNode =& $node[$c];
                $this->dfs($board, $ni, $nj, $nextNode, $result);
            }
        }

        $board[$i][$j] = $temp; // restore
    }
}
```

## Swift

```swift
class Solution {
    func findWords(_ board: [[Character]], _ words: [String]) -> [String] {
        guard !board.isEmpty && !board[0].isEmpty else { return [] }
        var board = board
        let rows = board.count, cols = board[0].count
        let aAscii = Character("a").asciiValue!
        
        class TrieNode {
            var children: [TrieNode?] = Array(repeating: nil, count: 26)
            var word: String?
        }
        
        // Build trie
        let root = TrieNode()
        for w in words {
            var node = root
            for ch in w {
                let idx = Int(ch.asciiValue! - aAscii)
                if node.children[idx] == nil {
                    node.children[idx] = TrieNode()
                }
                node = node.children[idx]!
            }
            node.word = w
        }
        
        var result: [String] = []
        let directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        func dfs(_ r: Int, _ c: Int, _ parent: TrieNode) {
            let ch = board[r][c]
            let idx = Int(ch.asciiValue! - aAscii)
            guard let node = parent.children[idx] else { return }
            
            if let foundWord = node.word {
                result.append(foundWord)
                node.word = nil   // avoid duplicate entries
            }
            
            board[r][c] = "#"   // mark visited
            
            for (dr, dc) in directions {
                let nr = r + dr, nc = c + dc
                if nr >= 0 && nr < rows && nc >= 0 && nc < cols {
                    let nextChar = board[nr][nc]
                    if nextChar != "#" {
                        dfs(nr, nc, node)
                    }
                }
            }
            
            board[r][c] = ch    // restore
        }
        
        for r in 0..<rows {
            for c in 0..<cols {
                let ch = board[r][c]
                if let idx = ch.asciiValue.map({ Int($0 - aAscii) }), root.children[idx] != nil {
                    dfs(r, c, root)
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class TrieNode {
        val children = arrayOfNulls<TrieNode>(26)
        var word: String? = null
    }

    fun findWords(board: Array<CharArray>, words: Array<String>): List<String> {
        val root = TrieNode()
        // Build trie
        for (w in words) {
            var node = root
            for (ch in w) {
                val idx = ch - 'a'
                if (node.children[idx] == null) node.children[idx] = TrieNode()
                node = node.children[idx]!!
            }
            node.word = w
        }

        val m = board.size
        val n = board[0].size
        val result = mutableListOf<String>()
        val dirs = intArrayOf(0, 1, 0, -1, 0)

        fun dfs(i: Int, j: Int, node: TrieNode) {
            if (i !in 0 until m || j !in 0 until n) return
            val ch = board[i][j]
            if (ch == '#') return
            val child = node.children[ch - 'a'] ?: return

            // Check word
            child.word?.let {
                result.add(it)
                child.word = null // avoid duplicate
            }

            // Mark visited
            board[i][j] = '#'

            for (d in 0 until 4) {
                val ni = i + dirs[d]
                val nj = j + dirs[d + 1]
                dfs(ni, nj, child)
            }

            // Restore
            board[i][j] = ch
        }

        for (i in 0 until m) {
            for (j in 0 until n) {
                dfs(i, j, root)
            }
        }

        return result
    }
}
```

## Dart

```dart
class TrieNode {
  Map<String, TrieNode> children = {};
  String? word;
}

class Solution {
  List<String> findWords(List<List<String>> board, List<String> words) {
    // Build trie
    final root = TrieNode();
    for (final w in words) {
      var node = root;
      for (int i = 0; i < w.length; i++) {
        String ch = w[i];
        node = node.children.putIfAbsent(ch, () => TrieNode());
      }
      node.word = w;
    }

    final result = <String>[];
    int m = board.length;
    if (m == 0) return result;
    int n = board[0].length;

    void dfs(int i, int j, TrieNode node) {
      String letter = board[i][j];
      if (letter == '#') return;
      final child = node.children[letter];
      if (child == null) return;

      if (child.word != null) {
        result.add(child.word!);
        child.word = null; // avoid duplicate entries
      }

      board[i][j] = '#';
      const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
      ];
      for (var d in dirs) {
        int ni = i + d[0];
        int nj = j + d[1];
        if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
          dfs(ni, nj, child);
        }
      }
      board[i][j] = letter;
    }

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        dfs(i, j, root);
      }
    }

    return result;
  }
}
```

## Golang

```go
package main

func findWords(board [][]byte, words []string) []string {
	type TrieNode struct {
		children [26]*TrieNode
		word     string
	}
	root := &TrieNode{}
	for _, w := range words {
		node := root
		for i := 0; i < len(w); i++ {
			idx := w[i] - 'a'
			if node.children[idx] == nil {
				node.children[idx] = &TrieNode{}
			}
			node = node.children[idx]
		}
		node.word = w
	}

	var res []string
	rows, cols := len(board), len(board[0])

	var dfs func(i, j int, node *TrieNode)
	dfs = func(i, j int, node *TrieNode) {
		c := board[i][j]
		child := node.children[c-'a']
		if child == nil {
			return
		}
		if child.word != "" {
			res = append(res, child.word)
			child.word = ""
		}

		board[i][j] = '#'
		if i > 0 && board[i-1][j] != '#' {
			dfs(i-1, j, child)
		}
		if i+1 < rows && board[i+1][j] != '#' {
			dfs(i+1, j, child)
		}
		if j > 0 && board[i][j-1] != '#' {
			dfs(i, j-1, child)
		}
		if j+1 < cols && board[i][j+1] != '#' {
			dfs(i, j+1, child)
		}
		board[i][j] = c
	}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			dfs(i, j, root)
		}
	}
	return res
}
```

## Ruby

```ruby
def find_words(board, words)
  class TrieNode
    attr_accessor :children, :word
    def initialize
      @children = {}
      @word = nil
    end
  end

  root = TrieNode.new
  words.each do |w|
    node = root
    w.each_char do |ch|
      node.children[ch] ||= TrieNode.new
      node = node.children[ch]
    end
    node.word = w
  end

  rows = board.size
  cols = board[0].size
  result = []
  dirs = [[-1,0],[1,0],[0,-1],[0,1]]

  dfs = nil
  dfs = lambda do |r, c, parent|
    ch = board[r][c]
    node = parent.children[ch]
    return unless node

    if node.word
      result << node.word
      node.word = nil
    end

    board[r][c] = '#'
    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next if nr < 0 || nr >= rows || nc < 0 || nc >= cols
      next if board[nr][nc] == '#'
      dfs.call(nr, nc, node) if node.children.key?(board[nr][nc])
    end
    board[r][c] = ch

    parent.children.delete(ch) if node.children.empty?
  end

  rows.times do |i|
    cols.times do |j|
      next unless root.children.key?(board[i][j])
      dfs.call(i, j, root)
    end
  end

  result
end
```

## Scala

```scala
object Solution {
  def findWords(board: Array[Array[Char]], words: Array[String]): List[String] = {
    class TrieNode {
      val children: Array[TrieNode] = new Array[TrieNode](26)
      var word: String = null
    }

    val root = new TrieNode()
    for (w <- words) {
      var node = root
      for (c <- w) {
        val idx = c - 'a'
        if (node.children(idx) == null) node.children(idx) = new TrieNode()
        node = node.children(idx)
      }
      node.word = w
    }

    val m = board.length
    val n = board(0).length
    val result = scala.collection.mutable.ListBuffer[String]()

    def dfs(i: Int, j: Int, node: TrieNode): Unit = {
      if (i < 0 || i >= m || j < 0 || j >= n) return
      val ch = board(i)(j)
      if (ch == '#') return
      val childIdx = ch - 'a'
      val child = node.children(childIdx)
      if (child == null) return

      if (child.word != null) {
        result += child.word
        child.word = null
      }

      board(i)(j) = '#'
      dfs(i + 1, j, child)
      dfs(i - 1, j, child)
      dfs(i, j + 1, child)
      dfs(i, j - 1, child)
      board(i)(j) = ch

      var empty = true
      var k = 0
      while (k < 26 && empty) {
        if (child.children(k) != null) empty = false
        k += 1
      }
      if (empty) node.children(childIdx) = null
    }

    for (i <- 0 until m; j <- 0 until n) dfs(i, j, root)

    result.toList
  }
}
```

## Rust

```rust
use std::vec::Vec;

struct Node {
    children: [Option<usize>; 26],
    word_idx: Option<usize>,
}

impl Node {
    fn new() -> Self {
        Self {
            children: [None; 26],
            word_idx: None,
        }
    }
}

fn dfs(
    board: &mut Vec<Vec<char>>,
    i: usize,
    j: usize,
    node_idx: usize,
    nodes: &mut Vec<Node>,
    words: &Vec<String>,
    result: &mut Vec<String>,
) {
    if let Some(wi) = nodes[node_idx].word_idx.take() {
        result.push(words[wi].clone());
    }

    let saved = board[i][j];
    board[i][j] = '#';

    const DIRS: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];
    for &(dx, dy) in &DIRS {
        let ni = i as i32 + dx;
        let nj = j as i32 + dy;
        if ni >= 0
            && nj >= 0
            && (ni as usize) < board.len()
            && (nj as usize) < board[0].len()
        {
            let ch = board[ni as usize][nj as usize];
            if ch != '#' {
                let idx = (ch as u8 - b'a') as usize;
                if let Some(next_idx) = nodes[node_idx].children[idx] {
                    dfs(
                        board,
                        ni as usize,
                        nj as usize,
                        next_idx,
                        nodes,
                        words,
                        result,
                    );
                }
            }
        }
    }

    board[i][j] = saved;
}

impl Solution {
    pub fn find_words(board: Vec<Vec<char>>, words: Vec<String>) -> Vec<String> {
        let mut nodes = vec![Node::new()];
        for (wi, w) in words.iter().enumerate() {
            let mut cur = 0usize;
            for ch in w.chars() {
                let idx = (ch as u8 - b'a') as usize;
                if nodes[cur].children[idx].is_none() {
                    nodes.push(Node::new());
                    let new_idx = nodes.len() - 1;
                    nodes[cur].children[idx] = Some(new_idx);
                }
                cur = nodes[cur].children[idx].unwrap();
            }
            nodes[cur].word_idx = Some(wi);
        }

        if board.is_empty() || board[0].is_empty() {
            return Vec::new();
        }

        let mut board_mut = board.clone();
        let rows = board_mut.len();
        let cols = board_mut[0].len();
        let mut result: Vec<String> = Vec::new();

        for i in 0..rows {
            for j in 0..cols {
                let ch = board_mut[i][j];
                let idx = (ch as u8 - b'a') as usize;
                if let Some(child_idx) = nodes[0].children[idx] {
                    dfs(
                        &mut board_mut,
                        i,
                        j,
                        child_idx,
                        &mut nodes,
                        &words,
                        &mut result,
                    );
                }
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (find-words board words)
  (-> (listof (listof char?)) (listof string?) (listof string?))
  (let* ([m (length board)]
         [n (if (> m 0) (length (first board)) 0)]
         [bvec (list->vector (map list->vector board))]
         [root (make-hash)])
    ;; build trie
    (for ([w words])
      (define node root)
      (for ([ch (in-string w)])
        (let* ([next (hash-ref node ch #f)])
          (unless next
            (set! next (make-hash))
            (hash-set! node ch next))
          (set! node next)))
      (hash-set! node '#:word w))
    ;; result set
    (define results (make-hash))
    (define dirs '((-1 0) (1 0) (0 -1) (0 1)))
    (define (dfs i j node)
      (let* ([c (vector-ref (vector-ref bvec i) j)])
        (when (not (char=? c #\0))
          (let ([child (hash-ref node c #f)])
            (when child
              ;; word found at this node
              (when (hash-has-key? child '#:word)
                (define w (hash-ref child '#:word))
                (hash-set! results w #t)
                (hash-remove! child '#:word))
              ;; mark visited
              (vector-set! (vector-ref bvec i) j #\0)
              ;; explore neighbours
              (for ([d dirs])
                (define di (first d))
                (define dj (second d))
                (let ([ni (+ i di)] [nj (+ j dj)])
                  (when (and (>= ni 0) (< ni m) (>= nj 0) (< nj n))
                    (dfs ni nj child))))
              ;; restore
              (vector-set! (vector-ref bvec i) j c))))))
    ;; start DFS from each cell
    (for ([i (in-range m)])
      (for ([j (in-range n)])
        (dfs i j root)))
    (hash-keys results)))
```

## Erlang

```erlang
-spec find_words(Board :: [[char()]], Words :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
find_words(Board, Words) ->
    Root = build_trie(Words),
    BoardTuples = [list_to_tuple(Row) || Row <- Board],
    Rows = length(BoardTuples),
    Cols = case BoardTuples of [] -> 0; [First|_] -> tuple_size(First) end,
    AllFound = find_all(Rows, Cols, BoardTuples, Root),
    maps:keys(maps:from_list([{W,true} || W <- AllFound])).

%% Build a trie from the list of words
build_trie(Words) ->
    Empty = #{children => #{}},
    lists:foldl(fun(Word, Acc) ->
        Chars = binary_to_list(Word),
        insert_word(Chars, Word, Acc)
    end, Empty, Words).

insert_word([], WordBin, Node) ->
    Node#{word => WordBin};
insert_word([C|Rest], WordBin, Node) ->
    Children = maps:get(children, Node, #{}),
    ChildNode0 = case maps:find(C, Children) of
        {ok, CN} -> CN;
        error -> #{children => #{}}
    end,
    UpdatedChild = insert_word(Rest, WordBin, ChildNode0),
    NewChildren = maps:put(C, UpdatedChild, Children),
    Node#{children => NewChildren}.

%% Retrieve character at (I,J) from board represented as list of tuples
get_char(BoardTuples, I, J) ->
    RowTuple = lists:nth(I + 1, BoardTuples),
    element(J + 1, RowTuple).

%% Depth‑first search starting from cell (I,J)
dfs(I, J, Board, TrieNode, Visited, Rows, Cols) ->
    Char = get_char(Board, I, J),
    Children = maps:get(children, TrieNode, #{}),
    case maps:find(Char, Children) of
        error -> [];
        {ok, ChildNode} ->
            WordsHere = case maps:get(word, ChildNode, undefined) of
                undefined -> [];
                WordBin -> [WordBin]
            end,
            Visited1 = maps:put({I, J}, true, Visited),
            NeighborDirs = [{-1,0},{1,0},{0,-1},{0,1}],
            WordsFromNeighbors = lists:foldl(fun({DI,DJ}, Acc) ->
                NI = I + DI,
                NJ = J + DJ,
                if NI >= 0, NI < Rows, NJ >= 0, NJ < Cols,
                   not maps:is_key({NI,NJ}, Visited1) ->
                       Acc ++ dfs(NI, NJ, Board, ChildNode, Visited1, Rows, Cols);
                   true -> Acc
                end
            end, [], NeighborDirs),
            WordsHere ++ WordsFromNeighbors
    end.

%% Run DFS from every cell and collect found words
find_all(Rows, Cols, Board, Root) ->
    lists:foldl(fun(I, AccI) ->
        RowAcc = lists:foldl(fun(J, AccJ) ->
            AccJ ++ dfs(I, J, Board, Root, #{}, Rows, Cols)
        end, [], lists:seq(0, Cols - 1)),
        AccI ++ RowAcc
    end, [], lists:seq(0, Rows - 1)).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_words(board :: [[char]], words :: [String.t()]) :: [String.t()]
  def find_words(board, words) do
    trie = Enum.reduce(words, %{}, fn w, acc -> insert(acc, w, w) end)

    rows = length(board)
    cols = board |> List.first() |> length()

    result_set =
      for i <- 0..(rows - 1), j <- 0..(cols - 1), reduce: MapSet.new() do
        acc -> dfs(board, i, j, trie, MapSet.new(), acc)
      end

    MapSet.to_list(result_set)
  end

  # Insert a word into the trie.
  defp insert(trie, <<>>, word) do
    Map.put(trie, :word, word)
  end

  defp insert(trie, <<c::utf8, rest::binary>>, word) do
    children = Map.get(trie, :children, %{})
    child = Map.get(children, <<c>>)
    new_child = insert(child || %{}, rest, word)
    new_children = Map.put(children, <<c>>, new_child)
    trie |> Map.put(:children, new_children)
  end

  # Depth‑first search from (i, j) using the current trie node.
  defp dfs(board, i, j, node, visited, acc) do
    rows = length(board)
    cols = board |> List.first() |> length()

    row = Enum.at(board, i)
    char = Enum.at(row, j)

    children = Map.get(node, :children, %{})
    child_node = Map.get(children, char)

    if child_node == nil do
      acc
    else
      acc =
        case Map.get(child_node, :word) do
          nil -> acc
          word -> MapSet.put(acc, word)
        end

      visited = MapSet.put(visited, {i, j})

      dirs = [{-1, 0}, {1, 0}, {0, -1}, {0, 1}]

      Enum.reduce(dirs, acc, fn {di, dj}, a ->
        ni = i + di
        nj = j + dj

        if ni >= 0 and ni < rows and nj >= 0 and nj < cols and not MapSet.member?(visited, {ni, nj}) do
          dfs(board, ni, nj, child_node, visited, a)
        else
          a
        end
      end)
    end
  end
end
```
