# 0126. Word Ladder II

## Cpp

```cpp
class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(), wordList.end());
        if (!dict.count(endWord)) return {};
        dict.insert(beginWord);
        
        unordered_map<string, vector<string>> parents;
        unordered_set<string> visited;          // words visited in previous levels
        queue<string> q;
        q.push(beginWord);
        bool found = false;
        
        while (!q.empty() && !found) {
            int sz = q.size();
            unordered_set<string> visited_this_level;
            for (int i = 0; i < sz; ++i) {
                string word = q.front(); q.pop();
                string cur = word;
                for (size_t pos = 0; pos < cur.size(); ++pos) {
                    char original = cur[pos];
                    for (char c = 'a'; c <= 'z'; ++c) {
                        if (c == original) continue;
                        cur[pos] = c;
                        if (!dict.count(cur)) continue;
                        
                        // record parent relationship
                        parents[cur].push_back(word);
                        
                        if (!visited.count(cur)) {
                            visited_this_level.insert(cur);
                            q.push(cur);
                        }
                        if (cur == endWord) found = true;
                    }
                    cur[pos] = original;
                }
            }
            for (const string& w : visited_this_level) visited.insert(w);
        }
        
        if (!found) return {};
        
        vector<vector<string>> results;
        vector<string> path;
        function<void(const string&)> dfs = [&](const string& word) {
            if (word == beginWord) {
                path.push_back(beginWord);
                results.emplace_back(path.rbegin(), path.rend());
                path.pop_back();
                return;
            }
            path.push_back(word);
            for (const string& prev : parents[word]) {
                dfs(prev);
            }
            path.pop_back();
        };
        
        dfs(endWord);
        return results;
    }
};
```

## Java

```java
class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        Set<String> dict = new HashSet<>(wordList);
        if (!dict.contains(endWord)) return Collections.emptyList();

        Map<String, List<String>> parents = new HashMap<>();
        Queue<String> queue = new ArrayDeque<>();
        queue.add(beginWord);

        Set<String> visited = new HashSet<>();
        visited.add(beginWord);

        boolean found = false;
        int wordLen = beginWord.length();

        while (!queue.isEmpty() && !found) {
            int size = queue.size();
            Set<String> levelVisited = new HashSet<>();

            for (int i = 0; i < size; i++) {
                String cur = queue.poll();
                char[] chars = cur.toCharArray();

                for (int pos = 0; pos < wordLen; pos++) {
                    char original = chars[pos];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == original) continue;
                        chars[pos] = c;
                        String nxt = new String(chars);
                        if (!dict.contains(nxt)) continue;

                        if (nxt.equals(endWord)) found = true;

                        if (!visited.contains(nxt)) {
                            if (levelVisited.add(nxt)) {
                                queue.add(nxt);
                            }
                            parents.computeIfAbsent(nxt, k -> new ArrayList<>()).add(cur);
                        } else if (levelVisited.contains(nxt)) {
                            // same level reached via another path
                            parents.get(nxt).add(cur);
                        }
                    }
                    chars[pos] = original;
                }
            }
            visited.addAll(levelVisited);
        }

        if (!found) return Collections.emptyList();

        List<List<String>> results = new ArrayList<>();
        LinkedList<String> path = new LinkedList<>();
        path.add(endWord);
        dfs(endWord, beginWord, parents, path, results);
        return results;
    }

    private void dfs(String word, String begin,
                     Map<String, List<String>> parents,
                     LinkedList<String> path,
                     List<List<String>> results) {
        if (word.equals(begin)) {
            List<String> list = new ArrayList<>(path);
            Collections.reverse(list);
            results.add(list);
            return;
        }
        List<String> preds = parents.get(word);
        if (preds == null) return;
        for (String p : preds) {
            path.addFirst(p);
            dfs(p, begin, parents, path, results);
            path.removeFirst();
        }
    }
}
```

## Python

```python
import collections

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # adjacency from child to its possible parents on shortest paths
        parents = collections.defaultdict(list)
        level = {beginWord}
        found = False
        L = len(beginWord)
        while level and not found:
            next_level = set()
            visited_this_round = set()
            for word in level:
                # generate all possible one-letter transformations
                word_chars = list(word)
                for i in range(L):
                    original_char = word_chars[i]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == original_char:
                            continue
                        word_chars[i] = c
                        new_word = ''.join(word_chars)
                        if new_word in wordSet:
                            if new_word not in visited_this_round:
                                visited_this_round.add(new_word)
                                next_level.add(new_word)
                            parents[new_word].append(word)
                            if new_word == endWord:
                                found = True
                    word_chars[i] = original_char
            # remove words visited this round to prevent cycles and ensure shortest paths
            wordSet -= visited_this_round
            level = next_level
        
        res = []
        if not found:
            return res
        
        path = [endWord]
        def dfs(word):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                path.append(p)
                dfs(p)
                path.pop()
        
        dfs(endWord)
        return res
```

## Python3

```python
from collections import defaultdict
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        L = len(beginWord)
        parents = defaultdict(list)          # child -> list of parents
        level = {beginWord}
        visited = set([beginWord])
        found = False

        while level and not found:
            next_level = set()
            for word in level:
                for i in range(L):
                    prefix, suffix = word[:i], word[i+1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                        nxt = prefix + c + suffix
                        if nxt not in word_set:
                            continue
                        if nxt not in visited:
                            if nxt == endWord:
                                found = True
                            next_level.add(nxt)
                            parents[nxt].append(word)
                        elif nxt in next_level:   # already discovered this level via another path
                            parents[nxt].append(word)
            visited.update(next_level)
            level = next_level

        if not found:
            return []

        res: List[List[str]] = []
        def backtrack(word: str, path: List[str]) -> None:
            if word == beginWord:
                res.append([beginWord] + path[::-1])
                return
            for p in parents[word]:
                backtrack(p, path + [word])

        backtrack(endWord, [])
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int *arr;
    int size;
    int cap;
} IntList;

static void initList(IntList *list) {
    list->size = 0;
    list->cap = 2;
    list->arr = (int *)malloc(list->cap * sizeof(int));
}

static void pushList(IntList *list, int val) {
    if (list->size == list->cap) {
        list->cap <<= 1;
        list->arr = (int *)realloc(list->arr, list->cap * sizeof(int));
    }
    list->arr[list->size++] = val;
}

/* check if two words differ by exactly one character */
static int isOneDiff(const char *a, const char *b) {
    int diff = 0;
    while (*a) {
        if (*a != *b) {
            if (++diff > 1) return 0;
        }
        ++a; ++b;
    }
    return diff == 1;
}

/* context for DFS backtracking */
typedef struct {
    char **words;          /* array of all words (including beginWord) */
    IntList *parents;      /* parents list per node */
    int *path;             /* current path indices */
    int depth;             /* current depth in path */
    int maxDepth;          /* length of shortest path */
    char ***seqs;          /* result sequences */
    int *colSizes;         /* sizes of each sequence */
    int resSize;           /* number of sequences found */
    int resCap;            /* capacity of seqs/colSizes arrays */
} Ctx;

/* depth‑first search from node to beginWord (index 0) */
static void dfs(int node, Ctx *ctx) {
    ctx->path[ctx->depth++] = node;
    if (node == 0) {   /* reached beginWord, output a sequence */
        int len = ctx->depth;
        char **seq = (char **)malloc(len * sizeof(char *));
        for (int i = 0; i < len; ++i) {
            int idx = ctx->path[len - 1 - i];
            seq[i] = strdup(ctx->words[idx]);
        }
        if (ctx->resSize == ctx->resCap) {
            ctx->resCap <<= 1;
            ctx->seqs = (char ***)realloc(ctx->seqs, ctx->resCap * sizeof(char **));
            ctx->colSizes = (int *)realloc(ctx->colSizes, ctx->resCap * sizeof(int));
        }
        ctx->seqs[ctx->resSize] = seq;
        ctx->colSizes[ctx->resSize] = len;
        ++ctx->resSize;
    } else {
        IntList *pl = &ctx->parents[node];
        for (int i = 0; i < pl->size; ++i) {
            dfs(pl->arr[i], ctx);
        }
    }
    --ctx->depth;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** findLadders(char* beginWord, char* endWord, char** wordList, int wordListSize,
                    int* returnSize, int** returnColumnSizes) {
    /* total number of distinct words (beginWord + list) */
    int N = wordListSize + 1;
    char **words = (char **)malloc(N * sizeof(char *));
    words[0] = strdup(beginWord);
    for (int i = 0; i < wordListSize; ++i)
        words[i + 1] = strdup(wordList[i]);

    /* locate endWord */
    int endIdx = -1;
    for (int i = 1; i < N; ++i) {
        if (strcmp(words[i], endWord) == 0) { endIdx = i; break; }
    }
    if (endIdx == -1) {   /* no possible transformation */
        *returnSize = 0;
        *returnColumnSizes = NULL;
        for (int i = 0; i < N; ++i) free(words[i]);
        free(words);
        return NULL;
    }

    /* BFS to compute shortest distances and parent relations */
    int *dist = (int *)malloc(N * sizeof(int));
    for (int i = 0; i < N; ++i) dist[i] = -1;

    IntList *parents = (IntList *)malloc(N * sizeof(IntList));
    for (int i = 0; i < N; ++i) initList(&parents[i]);

    int *queue = (int *)malloc(N * sizeof(int));
    int qh = 0, qt = 0;
    dist[0] = 0;
    queue[qt++] = 0;

    while (qh < qt) {
        int u = queue[qh++];
        for (int v = 1; v < N; ++v) {   /* all other words */
            if (dist[v] != -1 && dist[v] < dist[u] + 1) continue; /* already reached with shorter path */
            if (!isOneDiff(words[u], words[v])) continue;
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                queue[qt++] = v;
                pushList(&parents[v], u);
            } else if (dist[v] == dist[u] + 1) {
                pushList(&parents[v], u);
            }
        }
    }

    if (dist[endIdx] == -1) {   /* unreachable */
        *returnSize = 0;
        *returnColumnSizes = NULL;
        for (int i = 0; i < N; ++i) free(words[i]);
        free(words);
        free(dist);
        free(queue);
        for (int i = 0; i < N; ++i) free(parents[i].arr);
        free(parents);
        return NULL;
    }

    /* prepare context for DFS */
    Ctx ctx;
    ctx.words = words;
    ctx.parents = parents;
    ctx.maxDepth = dist[endIdx] + 1;
    ctx.path = (int *)malloc(ctx.maxDepth * sizeof(int));
    ctx.depth = 0;
    ctx.resCap = 16;
    ctx.seqs = (char ***)malloc(ctx.resCap * sizeof(char **));
    ctx.colSizes = (int *)malloc(ctx.resCap * sizeof(int));
    ctx.resSize = 0;

    dfs(endIdx, &ctx);

    /* clean up temporary structures */
    for (int i = 0; i < N; ++i) free(parents[i].arr);
    free(parents);
    free(dist);
    free(queue);
    free(ctx.path);
    for (int i = 0; i < N; ++i) free(words[i]);
    free(words);

    *returnSize = ctx.resSize;
    *returnColumnSizes = (int *)malloc(ctx.resSize * sizeof(int));
    memcpy(*returnColumnSizes, ctx.colSizes, ctx.resSize * sizeof(int));
    char ***ans = ctx.seqs;

    free(ctx.colSizes);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public IList<IList<string>> FindLadders(string beginWord, string endWord, IList<string> wordList) {
        var dict = new HashSet<string>(wordList);
        if (!dict.Contains(endWord)) return new List<IList<string>>();

        var parents = new Dictionary<string, List<string>>();
        var queue = new Queue<string>();
        queue.Enqueue(beginWord);
        var visited = new HashSet<string> { beginWord };
        bool found = false;
        int wordLen = beginWord.Length;

        while (queue.Count > 0 && !found) {
            int size = queue.Count;
            var levelVisited = new HashSet<string>();
            for (int i = 0; i < size; i++) {
                string cur = queue.Dequeue();
                char[] arr = cur.ToCharArray();
                for (int pos = 0; pos < wordLen; pos++) {
                    char original = arr[pos];
                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == original) continue;
                        arr[pos] = c;
                        string nxt = new string(arr);
                        if (!dict.Contains(nxt)) continue;

                        if (!parents.ContainsKey(nxt))
                            parents[nxt] = new List<string>();

                        if (!visited.Contains(nxt)) {
                            parents[nxt].Add(cur);
                            if (!levelVisited.Contains(nxt)) {
                                queue.Enqueue(nxt);
                                levelVisited.Add(nxt);
                            }
                        } else if (levelVisited.Contains(nxt)) {
                            parents[nxt].Add(cur);
                        }

                        if (nxt == endWord) found = true;
                    }
                    arr[pos] = original;
                }
            }
            foreach (var w in levelVisited) visited.Add(w);
        }

        var results = new List<IList<string>>();
        if (!found) return results;

        var path = new List<string>();
        void Dfs(string word) {
            path.Add(word);
            if (word == beginWord) {
                var rev = new List<string>(path);
                rev.Reverse();
                results.Add(rev);
            } else if (parents.ContainsKey(word)) {
                foreach (var p in parents[word]) {
                    Dfs(p);
                }
            }
            path.RemoveAt(path.Count - 1);
        }

        Dfs(endWord);
        return results;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {string[][]}
 */
var findLadders = function(beginWord, endWord, wordList) {
    const wordSet = new Set(wordList);
    if (!wordSet.has(endWord)) return [];

    const distance = new Map();               // word -> steps from begin
    const parents = new Map();                // word -> array of previous words on shortest paths

    const queue = [];
    queue.push(beginWord);
    distance.set(beginWord, 0);
    parents.set(beginWord, []);

    const L = beginWord.length;
    let foundLevel = Infinity;

    while (queue.length) {
        const cur = queue.shift();
        const curDist = distance.get(cur);
        if (curDist + 1 > foundLevel) break; // no need to explore deeper levels

        for (let i = 0; i < L; i++) {
            const arr = cur.split('');
            const originalChar = arr[i];
            for (let c = 97; c <= 122; c++) { // 'a' to 'z'
                const ch = String.fromCharCode(c);
                if (ch === originalChar) continue;
                arr[i] = ch;
                const neighbor = arr.join('');
                if (!wordSet.has(neighbor)) continue;

                if (!distance.has(neighbor)) {
                    distance.set(neighbor, curDist + 1);
                    queue.push(neighbor);
                    parents.set(neighbor, [cur]);
                } else if (distance.get(neighbor) === curDist + 1) {
                    parents.get(neighbor).push(cur);
                }

                if (neighbor === endWord) {
                    foundLevel = curDist + 1;
                }
            }
            arr[i] = originalChar; // restore not necessary due to new split each loop
        }
    }

    if (!distance.has(endWord)) return [];

    const results = [];
    const path = [];

    function backtrack(word) {
        if (word === beginWord) {
            path.push(beginWord);
            results.push([...path].reverse());
            path.pop();
            return;
        }
        path.push(word);
        const preds = parents.get(word) || [];
        for (const p of preds) {
            backtrack(p);
        }
        path.pop();
    }

    backtrack(endWord);
    return results;
};
```

## Typescript

```typescript
function findLadders(beginWord: string, endWord: string, wordList: string[]): string[][] {
    const wordSet = new Set<string>(wordList);
    if (!wordSet.has(endWord)) return [];
    wordSet.add(beginWord);

    const level = new Map<string, number>();
    const parents = new Map<string, string[]>();

    let queue: string[] = [beginWord];
    level.set(beginWord, 0);
    let found = false;
    let curLevel = 0;

    while (queue.length && !found) {
        curLevel++;
        const nextQueue: string[] = [];
        for (const word of queue) {
            const neighbors = getNeighbors(word);
            for (const nb of neighbors) {
                if (!level.has(nb)) {
                    level.set(nb, curLevel);
                    parents.set(nb, [word]);
                    if (nb === endWord) {
                        found = true;
                    } else {
                        nextQueue.push(nb);
                    }
                } else if (level.get(nb)! === curLevel) {
                    parents.get(nb)!.push(word);
                }
            }
        }
        queue = nextQueue;
    }

    const results: string[][] = [];
    if (!parents.has(endWord)) return results;

    const path: string[] = [endWord];
    function dfs(curr: string): void {
        if (curr === beginWord) {
            results.push([...path].reverse());
            return;
        }
        const preds = parents.get(curr)!;
        for (const p of preds) {
            path.push(p);
            dfs(p);
            path.pop();
        }
    }

    dfs(endWord);
    return results;

    function getNeighbors(word: string): string[] {
        const res: string[] = [];
        const arr = word.split('');
        for (let i = 0; i < arr.length; i++) {
            const original = arr[i];
            for (let c = 97; c <= 122; c++) {
                const ch = String.fromCharCode(c);
                if (ch === original) continue;
                arr[i] = ch;
                const newWord = arr.join('');
                if (wordSet.has(newWord)) res.push(newWord);
            }
            arr[i] = original;
        }
        return res;
    }
}
```

## Php

```php
class Solution {

    /**
     * @param String $beginWord
     * @param String $endWord
     * @param String[] $wordList
     * @return String[][]
     */
    function findLadders($beginWord, $endWord, $wordList) {
        $wordSet = array_flip($wordList);
        if (!isset($wordSet[$endWord])) {
            return [];
        }

        $len = strlen($beginWord);
        $queue = new SplQueue();
        $queue->enqueue($beginWord);
        $levels = [$beginWord => 0];
        $parents = [];

        $found = false;
        $endLevel = PHP_INT_MAX;

        while (!$queue->isEmpty()) {
            $word = $queue->dequeue();
            $currLevel = $levels[$word];
            if ($currLevel > $endLevel) {
                break;
            }

            for ($i = 0; $i < $len; $i++) {
                $originalChar = $word[$i];
                for ($cOrd = 97; $cOrd <= 122; $cOrd++) { // 'a' to 'z'
                    $c = chr($cOrd);
                    if ($c === $originalChar) {
                        continue;
                    }
                    $newWord = substr_replace($word, $c, $i, 1);
                    if (!isset($wordSet[$newWord])) {
                        continue;
                    }

                    if (!isset($levels[$newWord])) {
                        $levels[$newWord] = $currLevel + 1;
                        $queue->enqueue($newWord);
                        $parents[$word][] = $newWord;
                        if ($newWord === $endWord) {
                            $found = true;
                            $endLevel = $currLevel + 1;
                        }
                    } elseif ($levels[$newWord] == $currLevel + 1) {
                        $parents[$word][] = $newWord;
                    }
                }
            }
        }

        if (!$found) {
            return [];
        }

        $result = [];
        $path = [$beginWord];
        $this->dfs($beginWord, $endWord, $parents, $path, $result);
        return $result;
    }

    private function dfs($curr, $end, &$parents, &$path, &$result) {
        if ($curr === $end) {
            $result[] = $path;
            return;
        }
        if (!isset($parents[$curr])) {
            return;
        }
        foreach ($parents[$curr] as $next) {
            $path[] = $next;
            $this->dfs($next, $end, $parents, $path, $result);
            array_pop($path);
        }
    }
}
```

## Swift

```swift
class Solution {
    func findLadders(_ beginWord: String, _ endWord: String, _ wordList: [String]) -> [[String]] {
        var dict = Set(wordList)
        if !dict.contains(endWord) { return [] }
        let L = beginWord.count
        let letters: [Character] = Array("abcdefghijklmnopqrstuvwxyz")
        
        var level = [String:Int]()
        var parents = [String:[String]]()
        var queue = [String]()
        var head = 0
        
        level[beginWord] = 0
        queue.append(beginWord)
        var foundEnd = false
        
        while head < queue.count && !foundEnd {
            let currentLevelSize = queue.count - head
            for _ in 0..<currentLevelSize {
                let word = queue[head]
                head += 1
                let curDist = level[word]!
                var chars = Array(word)
                for i in 0..<L {
                    let originalChar = chars[i]
                    for ch in letters {
                        if ch == originalChar { continue }
                        chars[i] = ch
                        let newWord = String(chars)
                        if dict.contains(newWord) {
                            if level[newWord] == nil {
                                level[newWord] = curDist + 1
                                queue.append(newWord)
                                parents[newWord] = [word]
                            } else if level[newWord]! == curDist + 1 {
                                parents[newWord, default: []].append(word)
                            }
                            if newWord == endWord {
                                foundEnd = true
                            }
                        }
                    }
                    chars[i] = originalChar
                }
            }
        }
        
        guard level[endWord] != nil else { return [] }
        
        var results = [[String]]()
        var path = [String]()
        path.append(endWord)
        let start = beginWord
        
        func backtrack(_ word: String) {
            if word == start {
                results.append(path.reversed())
                return
            }
            guard let preds = parents[word] else { return }
            for pred in preds {
                path.append(pred)
                backtrack(pred)
                path.removeLast()
            }
        }
        
        backtrack(endWord)
        return results
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findLadders(beginWord: String, endWord: String, wordList: List<String>): List<List<String>> {
        val wordSet = HashSet(wordList)
        if (!wordSet.contains(endWord)) return emptyList()
        wordSet.add(beginWord)

        val distance = mutableMapOf<String, Int>()
        distance[beginWord] = 0

        val children = mutableMapOf<String, MutableList<String>>()

        var found = false
        var level = 0
        val queue: ArrayDeque<String> = ArrayDeque()
        queue.add(beginWord)

        while (queue.isNotEmpty() && !found) {
            val size = queue.size
            level++
            repeat(size) {
                val word = queue.removeFirst()
                val chars = word.toCharArray()
                for (i in chars.indices) {
                    val original = chars[i]
                    for (c in 'a'..'z') {
                        if (c == original) continue
                        chars[i] = c
                        val nb = String(chars)
                        if (!wordSet.contains(nb)) continue

                        if (!distance.containsKey(nb)) {
                            distance[nb] = level
                            queue.addLast(nb)
                            children.getOrPut(word) { mutableListOf() }.add(nb)
                        } else if (distance[nb] == level) {
                            children.getOrPut(word) { mutableListOf() }.add(nb)
                        }
                        if (nb == endWord) found = true
                    }
                    chars[i] = original
                }
            }
        }

        val results = mutableListOf<List<String>>()
        if (!distance.containsKey(endWord)) return results

        fun dfs(current: String, path: MutableList<String>) {
            if (current == endWord) {
                results.add(ArrayList(path))
                return
            }
            val nexts = children[current] ?: return
            for (next in nexts) {
                path.add(next)
                dfs(next, path)
                path.removeAt(path.size - 1)
            }
        }

        val path = mutableListOf<String>()
        path.add(beginWord)
        dfs(beginWord, path)

        return results
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
    Set<String> dict = Set.from(wordList);
    if (!dict.contains(endWord)) return [];

    // Ensure beginWord is in the dictionary for neighbor generation
    dict.add(beginWord);

    Map<String, int> distance = {};
    Map<String, List<String>> parents = {};

    Queue<String> queue = Queue();
    queue.add(beginWord);
    distance[beginWord] = 0;

    int foundLevel = -1;
    while (queue.isNotEmpty) {
      String word = queue.removeFirst();
      int level = distance[word]!;

      if (foundLevel != -1 && level > foundLevel) break; // processed all shortest paths

      for (int i = 0; i < word.length; i++) {
        List<int> chars = word.codeUnits;
        int originalChar = chars[i];
        for (int c = 97; c <= 122; c++) { // 'a' to 'z'
          if (c == originalChar) continue;
          chars[i] = c;
          String neighbor = String.fromCharCodes(chars);
          if (!dict.contains(neighbor)) continue;

          if (!distance.containsKey(neighbor)) {
            distance[neighbor] = level + 1;
            queue.add(neighbor);
            parents[neighbor] = [word];
          } else if (distance[neighbor] == level + 1) {
            parents[neighbor]!.add(word);
          }

          if (neighbor == endWord) {
            foundLevel = level + 1;
          }
        }
        chars[i] = originalChar; // restore
      }
    }

    if (!distance.containsKey(endWord)) return [];

    List<List<String>> results = [];
    List<String> path = [endWord];

    void dfs(String word) {
      if (word == beginWord) {
        results.add(List.from(path.reversed));
        return;
      }
      for (String parent in parents[word] ?? []) {
        path.add(parent);
        dfs(parent);
        path.removeLast();
      }
    }

    dfs(endWord);
    return results;
  }
}
```

## Golang

```go
func findLadders(beginWord string, endWord string, wordList []string) [][]string {
    wordSet := make(map[string]bool)
    for _, w := range wordList {
        wordSet[w] = true
    }
    if !wordSet[endWord] {
        return [][]string{}
    }

    dist := make(map[string]int)
    parents := make(map[string][]string)

    queue := []string{beginWord}
    dist[beginWord] = 0

    foundDist := -1
    wordLen := len(beginWord)

    for len(queue) > 0 {
        cur := queue[0]
        queue = queue[1:]
        d := dist[cur]

        if foundDist != -1 && d > foundDist {
            break
        }

        b := []byte(cur)
        for i := 0; i < wordLen; i++ {
            orig := b[i]
            for c := byte('a'); c <= 'z'; c++ {
                if c == orig {
                    continue
                }
                b[i] = c
                nb := string(b)
                if !wordSet[nb] {
                    continue
                }
                if _, ok := dist[nb]; !ok {
                    dist[nb] = d + 1
                    parents[nb] = []string{cur}
                    queue = append(queue, nb)
                } else if dist[nb] == d+1 {
                    parents[nb] = append(parents[nb], cur)
                }
                if nb == endWord && foundDist == -1 {
                    foundDist = d + 1
                }
            }
            b[i] = orig
        }
    }

    if _, ok := dist[endWord]; !ok {
        return [][]string{}
    }

    var res [][]string
    var dfs func(string, []string)
    dfs = func(word string, path []string) {
        if word == beginWord {
            tmp := make([]string, len(path)+1)
            tmp[0] = beginWord
            for i := 0; i < len(path); i++ {
                tmp[i+1] = path[len(path)-1-i]
            }
            res = append(res, tmp)
            return
        }
        for _, p := range parents[word] {
            dfs(p, append(path, word))
        }
    }

    dfs(endWord, []string{})
    return res
}
```

## Ruby

```ruby
require 'set'

def find_ladders(begin_word, end_word, word_list)
  word_set = Set.new(word_list)
  return [] unless word_set.include?(end_word)

  word_set.add(begin_word)

  adjacency = Hash.new { |h, k| h[k] = [] }
  distances = {}
  distances[begin_word] = 0

  queue = [begin_word]
  found_end = false
  level = 0

  while !queue.empty? && !found_end
    next_queue = []
    level += 1
    queue.each do |word|
      chars = word.chars
      (0...chars.size).each do |i|
        original_char = chars[i]
        ('a'..'z').each do |c|
          next if c == original_char
          chars[i] = c
          new_word = chars.join
          if word_set.include?(new_word)
            if !distances.key?(new_word)
              distances[new_word] = level
              adjacency[new_word] << word
              next_queue << new_word
            elsif distances[new_word] == level
              adjacency[new_word] << word
            end
            found_end = true if new_word == end_word
          end
        end
        chars[i] = original_char
      end
    end
    queue = next_queue
  end

  return [] unless distances.key?(end_word)

  results = []
  path = [end_word]

  dfs = lambda do |word|
    if word == begin_word
      results << path.reverse.clone
      return
    end
    adjacency[word].each do |prev|
      path << prev
      dfs.call(prev)
      path.pop
    end
  end

  dfs.call(end_word)
  results
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{Queue, Set => MSet, Map => MMap, ListBuffer}
  
  def findLadders(beginWord: String, endWord: String, wordList: List[String]): List[List[String]] = {
    val wordSet: MSet[String] = MSet(wordList: _*)
    if (!wordSet.contains(endWord)) return Nil
    wordSet += beginWord

    val adjacency: MMap[String, ListBuffer[String]] = MMap()
    val distance: MMap[String, Int] = MMap(beginWord -> 0)
    val q: Queue[String] = Queue(beginWord)

    var minLevel = Int.MaxValue
    val L = beginWord.length

    while (q.nonEmpty) {
      val cur = q.dequeue()
      val curDist = distance(cur)
      if (curDist >= minLevel) {
        // do not expand deeper levels
      } else {
        val chars = cur.toCharArray
        for (i <- 0 until L) {
          val original = chars(i)
          var c = 'a'
          while (c <= 'z') {
            if (c != original) {
              chars(i) = c
              val nxt = new String(chars)
              if (wordSet.contains(nxt)) {
                if (!distance.contains(nxt)) {
                  distance(nxt) = curDist + 1
                  if (nxt == endWord) minLevel = curDist + 1
                  q.enqueue(nxt)
                  adjacency.getOrElseUpdate(cur, ListBuffer()) += nxt
                } else if (distance(nxt) == curDist + 1) {
                  adjacency.getOrElseUpdate(cur, ListBuffer()) += nxt
                }
              }
            }
            c = (c + 1).toChar
          }
          chars(i) = original
        }
      }
    }

    if (!distance.contains(endWord)) return Nil

    val results = ListBuffer[List[String]]()
    val path = ListBuffer(beginWord)

    def dfs(word: String): Unit = {
      if (word == endWord) {
        results += path.toList
        return
      }
      for (next <- adjacency.getOrElse(word, Nil)) {
        path.append(next)
        dfs(next)
        path.remove(path.size - 1)
      }
    }

    dfs(beginWord)
    results.toList
  }
}
```

## Rust

```rust
use std::collections::{HashSet, HashMap, VecDeque};

impl Solution {
    pub fn find_ladders(begin_word: String, end_word: String, word_list: Vec<String>) -> Vec<Vec<String>> {
        let mut word_set: HashSet<String> = word_list.into_iter().collect();
        if !word_set.contains(&end_word) {
            return vec![];
        }

        let mut preds: HashMap<String, Vec<String>> = HashMap::new();
        let mut dist: HashMap<String, usize> = HashMap::new();

        let mut queue = VecDeque::new();
        queue.push_back(begin_word.clone());
        dist.insert(begin_word.clone(), 0);

        let mut min_len = usize::MAX;

        while let Some(word) = queue.pop_front() {
            let cur_dist = *dist.get(&word).unwrap();
            if cur_dist + 1 > min_len {
                continue;
            }
            for neighbor in Self::neighbors(&word, &word_set) {
                if cur_dist + 1 > min_len {
                    continue;
                }
                if !dist.contains_key(&neighbor) {
                    dist.insert(neighbor.clone(), cur_dist + 1);
                    queue.push_back(neighbor.clone());
                    preds.entry(neighbor.clone()).or_default().push(word.clone());
                } else if *dist.get(&neighbor).unwrap() == cur_dist + 1 {
                    preds.entry(neighbor.clone()).or_default().push(word.clone());
                }
                if neighbor == end_word {
                    min_len = cur_dist + 1;
                }
            }
        }

        if !dist.contains_key(&end_word) {
            return vec![];
        }

        let mut results: Vec<Vec<String>> = Vec::new();
        let mut path: Vec<String> = vec![end_word.clone()];
        Self::dfs(&end_word, &begin_word, &preds, &mut path, &mut results);
        results
    }

    fn neighbors(word: &String, word_set: &HashSet<String>) -> Vec<String> {
        let mut res = Vec::new();
        let bytes = word.as_bytes();
        let len = bytes.len();
        let mut chars = bytes.to_vec();

        for i in 0..len {
            let original = chars[i];
            for c in b'a'..=b'z' {
                if c == original {
                    continue;
                }
                chars[i] = c;
                let candidate = String::from_utf8(chars.clone()).unwrap();
                if word_set.contains(&candidate) {
                    res.push(candidate);
                }
            }
            chars[i] = original;
        }

        res
    }

    fn dfs(
        word: &String,
        begin: &String,
        preds: &HashMap<String, Vec<String>>,
        path: &mut Vec<String>,
        results: &mut Vec<Vec<String>>,
    ) {
        if word == begin {
            let mut seq = path.clone();
            seq.reverse();
            results.push(seq);
            return;
        }
        if let Some(parents) = preds.get(word) {
            for p in parents {
                path.push(p.clone());
                Self::dfs(p, begin, preds, path, results);
                path.pop();
            }
        }
    }
}
```

## Racket

```racket
(define/contract (find-ladders beginWord endWord wordList)
  (-> string? string? (listof string?) (listof (listof string?)))
  (let ((word-set (make-hash)))
    (for ([w wordList]) (hash-set! word-set w #t))
    (if (not (hash-has-key? word-set endWord))
        '()
        (let* ((len (string-length beginWord))
               (distance (make-hash))
               (parents (make-hash)))
          (hash-set! distance beginWord 0)
          (define current-level (list beginWord))
          (define found? #f)

          (define (gen-neighbors w)
            (let loop ((i 0) (result '()))
              (if (= i len)
                  result
                  (let* ((orig (string-ref w i)))
                    (let inner ((c 97) (res result))
                      (if (> c 122)
                          (loop (+ i 1) res)
                          (let ((new-char (integer->char c)))
                            (if (char=? new-char orig)
                                (inner (+ c 1) res)
                                (let ((new-word
                                       (string-append
                                        (substring w 0 i)
                                        (string new-char)
                                        (substring w (+ i 1)))))
                                  (if (hash-has-key? word-set new-word)
                                      (inner (+ c 1) (cons new-word res))
                                      (inner (+ c 1) res)))))))))))

          (let bfs-loop ()
            (when (and (not (null? current-level)) (not found?))
              (define next-level '())
              (for ([word current-level])
                (for ([nei (gen-neighbors word)])
                  (cond
                    [(not (hash-has-key? distance nei))
                     (hash-set! distance nei (+ (hash-ref distance word) 1))
                     (hash-set! parents nei (list word))
                     (set! next-level (cons nei next-level))]
                    [(= (hash-ref distance nei) (+ (hash-ref distance word) 1))
                     (hash-set! parents nei (cons word (hash-ref parents nei)))])))
              (when (hash-has-key? distance endWord)
                (set! found? #t))
              (set! current-level next-level)
              (bfs-loop)))

          (if (not (hash-has-key? distance endWord))
              '()
              (let ((results '()))
                (define (backtrack word path)
                  (if (string=? word beginWord)
                      (set! results (cons (reverse (cons beginWord path)) results))
                      (for ([parent (hash-ref parents word)])
                        (backtrack parent (cons word path)))))
                (backtrack endWord '())
                (reverse results)))))))
```

## Erlang

```erlang
-export([find_ladders/3]).

-spec find_ladders(BeginWord :: unicode:unicode_binary(),
                   EndWord   :: unicode:unicode_binary(),
                   WordList  :: [unicode:unicode_binary()]) ->
          [[unicode:unicode_binary()]].
find_ladders(BeginWord, EndWord, WordList) ->
    WordSet0 = maps:from_keys(WordList, true),
    case maps:is_key(EndWord, WordSet0) of
        false -> [];
        true  ->
            WordSet1 = maps:remove(BeginWord, WordSet0),
            Visited0 = #{BeginWord => 0},
            Preds0   = #{},
            Queue0   = [BeginWord],
            {PredsMap, Found} = bfs(1, Queue0, Visited0, Preds0, WordSet1, EndWord),
            case Found of
                false -> [];
                true  -> build_paths(EndWord, BeginWord, PredsMap)
            end
    end.

bfs(_Level, [], _Visited, Preds, _WordSet, _End) ->
    {Preds, false};
bfs(Level, Queue, Visited, Preds, WordSet, EndWord) ->
    {NextQueue, NewVisited, NewPreds} =
        lists:foldl(fun(Word, {NQ,NV,NP}) ->
            Neighs = neighbors(Word, WordSet),
            lists:foldl(fun(N, {AccQ, AccV, AccP}) ->
                case maps:get(N, AccV, undefined) of
                    undefined ->
                        V1 = maps:put(N, Level, AccV),
                        P1 = maps:update_with(N,
                                fun(L) -> [Word|L] end,
                                [Word],
                                AccP),
                        {AccQ ++ [N], V1, P1};
                    L when L == Level ->
                        P1 = maps:update_with(N,
                                fun(L) -> [Word|L] end,
                                [Word],
                                AccP),
                        {AccQ, AccV, P1};
                    _Other ->
                        {AccQ, AccV, AccP}
                end
            end, {NQ,NV,NP}, Neighs)
        end, {[], Visited, Preds}, Queue),

    NewWordSet = lists:foldl(fun(W, WS) -> maps:remove(W, WS) end,
                             WordSet, NextQueue),
    case maps:is_key(EndWord, NewVisited) of
        true  -> {NewPreds, true};
        false -> bfs(Level + 1, NextQueue, NewVisited, NewPreds, NewWordSet, EndWord)
    end.

neighbors(Word, WordSet) ->
    CharList = binary_to_list(Word),
    Len = length(CharList),
    lists:foldl(fun(I, Acc) ->
        Orig = lists:nth(I, CharList),
        lists:foldl(fun(C, Acc2) ->
            if C =/= Orig ->
                NewList = replace_nth(CharList, I, C),
                NewBin  = list_to_binary(NewList),
                case maps:is_key(NewBin, WordSet) of
                    true -> [NewBin|Acc2];
                    false -> Acc2
                end;
               true -> Acc2
            end
        end, Acc, lists:seq($a,$z))
    end, [], lists:seq(1, Len)).

replace_nth(List, Index, New) ->
    Prefix = lists:sublist(List, Index - 1),
    Suffix = lists:nthtail(Index, List),
    Prefix ++ [New] ++ Suffix.

build_paths(Word, BeginWord, Preds) ->
    if Word == BeginWord ->
            [[BeginWord]];
       true ->
            Parents = maps:get(Word, Preds),
            lists:foldl(fun(P, Acc) ->
                Sub = build_paths(P, BeginWord, Preds),
                Paths = [Path ++ [Word] || Path <- Sub],
                Acc ++ Paths
            end, [], Parents)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_ladders(begin_word :: String.t(), end_word :: String.t(), word_list :: [String.t()]) :: [[String.t()]]
  def find_ladders(begin_word, end_word, word_list) do
    if not Enum.member?(word_list, end_word) do
      []
    else
      word_set = MapSet.new(word_list)
      {adjacency, _dist} = bfs(begin_word, end_word, word_set)

      backtrack(begin_word, end_word, adjacency)
    end
  end

  # Breadth‑first search building forward edges that belong to shortest paths
  defp bfs(begin_word, end_word, word_set) do
    queue = :queue.from_list([begin_word])
    dist = %{begin_word => 0}
    adj = %{}
    bfs_level(queue, dist, adj, end_word, false, word_set)
  end

  defp bfs_level(queue, dist, adj, _end_word, true, _word_set) do
    {adj, dist}
  end

  defp bfs_level(queue, dist, adj, end_word, _found, word_set) do
    if :queue.is_empty(queue) do
      {adj, dist}
    else
      level_size = :queue.len(queue)

      {new_queue, new_dist, new_adj, found_in_level} =
        Enum.reduce(1..level_size, {queue, dist, adj, false}, fn _,
          {q_acc, d_acc, a_acc, f_acc} ->
          {{:value, word}, q_rest} = :queue.out(q_acc)
          cur_dist = Map.get(d_acc, word)

          neighbors = gen_neighbors(word)

          {q_next, d_next, a_next, f_next} =
            Enum.reduce(neighbors, {q_rest, d_acc, a_acc, f_acc}, fn nb,
              {qq, dd, aa, ff} ->
              if MapSet.member?(word_set, nb) do
                cond do
                  not Map.has_key?(dd, nb) ->
                    # first discovery of nb
                    dd2 = Map.put(dd, nb, cur_dist + 1)
                    qq2 = :queue.in(nb, qq)
                    aa2 = Map.update(aa, word, [nb], fn lst -> [nb | lst] end)
                    ff2 = if nb == end_word, do: true, else: ff
                    {qq2, dd2, aa2, ff2}

                  Map.get(dd, nb) == cur_dist + 1 ->
                    # already discovered at same level
                    aa2 = Map.update(aa, word, [nb], fn lst -> [nb | lst] end)
                    ff2 = if nb == end_word, do: true, else: ff
                    {qq, dd, aa2, ff2}

                  true ->
                    {qq, dd, aa, ff}
                end
              else
                {qq, dd, aa, ff}
              end
            end)

          {q_next, d_next, a_next, f_next}
        end)

      if found_in_level do
        {new_adj, new_dist}
      else
        bfs_level(new_queue, new_dist, new_adj, end_word, false, word_set)
      end
    end
  end

  # Generate all one‑letter transformations of a word
  defp gen_neighbors(word) do
    chars = String.to_charlist(word)
    len = length(chars)

    for i <- 0..(len - 1),
        c <- ?a..?z,
        c != Enum.at(chars, i) do
      List.replace_at(chars, i, c) |> to_string()
    end
  end

  # Backtrack using the adjacency map to collect all shortest paths
  defp backtrack(start, target, adj) do
    dfs(start, target, adj)
  end

  defp dfs(current, target, adj) when current == target do
    [[target]]
  end

  defp dfs(current, target, adj) do
    Enum.flat_map(Map.get(adj, current, []), fn nxt ->
      for path <- dfs(nxt, target, adj) do
        [current | path]
      end
    end)
  end
end
```
