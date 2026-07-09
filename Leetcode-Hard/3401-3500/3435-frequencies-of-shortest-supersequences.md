# 3435. Frequencies of Shortest Supersequences

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> supersequences(vector<string>& words) {
        // collect distinct letters
        unordered_map<char,int> idx;
        vector<char> chars;
        for (auto &w: words) {
            for (char c: w) {
                if (!idx.count(c)) {
                    idx[c] = chars.size();
                    chars.push_back(c);
                }
            }
        }
        int m = chars.size(); // <=16
        vector<pair<int,int>> pairs;
        pairs.reserve(words.size());
        for (auto &w: words) {
            int x = idx[w[0]];
            int y = idx[w[1]];
            pairs.emplace_back(x,y);
        }

        int bestLen = INT_MAX;
        vector<int> bestMasks;

        int totalLetters = m; // each at least once

        for (int mask = 0; mask < (1<<m); ++mask) {
            bool ok = true;
            // self-word requirement
            for (auto &p: pairs) {
                if (p.first == p.second) {
                    if ((mask>>p.first & 1)==0) { ok=false; break; }
                }
            }
            if (!ok) continue;

            // assign node ids
            vector<int> firstNode(m), secondNode(m, -1);
            int cur = 0;
            for (int i=0;i<m;++i){
                if (mask>>i & 1){
                    firstNode[i]=cur;
                    secondNode[i]=cur+1;
                    cur+=2;
                }else{
                    firstNode[i]=cur;
                    cur+=1;
                }
            }
            int N = cur;
            vector<vector<int>> adj(N);
            vector<int> indeg(N,0);

            // internal edges for duplicated letters
            for (int i=0;i<m;++i){
                if (mask>>i & 1){
                    int u = firstNode[i];
                    int v = secondNode[i];
                    adj[u].push_back(v);
                    ++indeg[v];
                }
            }

            // constraints from words
            for (auto &p: pairs) {
                int x=p.first, y=p.second;
                if (x==y) continue; // already handled
                int u = firstNode[x]; // earliest copy of x
                int v = (mask>>y & 1) ? secondNode[y] : firstNode[y]; // latest copy of y
                adj[u].push_back(v);
                ++indeg[v];
            }

            // topological check
            queue<int> q;
            for (int i=0;i<N;++i) if (indeg[i]==0) q.push(i);
            int visited = 0;
            while(!q.empty()){
                int u=q.front();q.pop();
                ++visited;
                for(int v:adj[u]){
                    if(--indeg[v]==0) q.push(v);
                }
            }
            if (visited!=N) continue; // cycle

            int len = totalLetters + __builtin_popcount(mask);
            if (len < bestLen){
                bestLen = len;
                bestMasks.clear();
                bestMasks.push_back(mask);
            }else if (len == bestLen){
                bestMasks.push_back(mask);
            }
        }

        vector<vector<int>> res;
        for (int mask: bestMasks){
            vector<int> freq(26,0);
            for (int i=0;i<m;++i){
                int cnt = ((mask>>i)&1) ? 2 : 1;
                freq[chars[i]-'a'] = cnt;
            }
            res.push_back(freq);
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> supersequences(String[] words) {
        // Collect distinct letters
        Set<Character> set = new HashSet<>();
        for (String w : words) {
            set.add(w.charAt(0));
            set.add(w.charAt(1));
        }
        int L = set.size();
        char[] letters = new char[L];
        int idx = 0;
        List<Character> sorted = new ArrayList<>(set);
        Collections.sort(sorted);
        for (char c : sorted) {
            letters[idx++] = c;
        }
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < L; i++) map.put(letters[i], i);

        int m = words.length;
        int[] wFirst = new int[m];
        int[] wSecond = new int[m];
        for (int i = 0; i < m; i++) {
            wFirst[i] = map.get(words[i].charAt(0));
            wSecond[i] = map.get(words[i].charAt(1));
        }

        List<Integer> feasibleMasks = new ArrayList<>();
        int minDup = Integer.MAX_VALUE;
        int totalMask = 1 << L;

        for (int mask = 0; mask < totalMask; mask++) {
            boolean ok = true;
            // quick check for words like "aa" needing duplication
            for (int i = 0; i < m && ok; i++) {
                if (wFirst[i] == wSecond[i]) {
                    int li = wFirst[i];
                    if ((mask & (1 << li)) == 0) {
                        ok = false;
                    }
                }
            }
            if (!ok) continue;

            // assign node ids
            int[] firstId = new int[L];
            int[] secondId = new int[L]; // -1 if not duplicated
            int nodeCnt = 0;
            for (int i = 0; i < L; i++) {
                firstId[i] = nodeCnt++;
                if ((mask & (1 << i)) != 0) {
                    secondId[i] = nodeCnt++;
                } else {
                    secondId[i] = -1;
                }
            }

            List<Integer>[] adj = new ArrayList[nodeCnt];
            for (int i = 0; i < nodeCnt; i++) adj[i] = new ArrayList<>();
            int[] indeg = new int[nodeCnt];

            // intra-letter edges
            for (int i = 0; i < L; i++) {
                if (secondId[i] != -1) {
                    adj[firstId[i]].add(secondId[i]);
                    indeg[secondId[i]]++;
                }
            }

            // word constraints: earliest of first -> latest of second
            for (int i = 0; i < m && ok; i++) {
                int a = wFirst[i];
                int b = wSecond[i];
                int from = firstId[a]; // earliest copy of a
                int to = (secondId[b] != -1) ? secondId[b] : firstId[b]; // latest copy of b
                if (from == to) {
                    ok = false;
                    break;
                }
                adj[from].add(to);
                indeg[to]++;
            }
            if (!ok) continue;

            // topological sort check
            int visited = 0;
            ArrayDeque<Integer> q = new ArrayDeque<>();
            for (int i = 0; i < nodeCnt; i++) {
                if (indeg[i] == 0) q.add(i);
            }
            while (!q.isEmpty()) {
                int u = q.poll();
                visited++;
                for (int v : adj[u]) {
                    indeg[v]--;
                    if (indeg[v] == 0) q.add(v);
                }
            }
            if (visited != nodeCnt) continue; // cycle

            int dupCount = Integer.bitCount(mask);
            if (dupCount < minDup) {
                minDup = dupCount;
                feasibleMasks.clear();
                feasibleMasks.add(mask);
            } else if (dupCount == minDup) {
                feasibleMasks.add(mask);
            }
        }

        List<List<Integer>> result = new ArrayList<>();
        for (int mask : feasibleMasks) {
            int[] freq = new int[26];
            for (int i = 0; i < L; i++) {
                int cnt = 1 + ((mask >> i) & 1);
                freq[letters[i] - 'a'] = cnt;
            }
            List<Integer> list = new ArrayList<>(26);
            for (int v : freq) list.add(v);
            result.add(list);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def supersequences(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # collect unique letters
        letters = set()
        edges = []
        for w in words:
            a, b = w[0], w[1]
            letters.add(a)
            letters.add(b)
            edges.append((a, b))
        letters = list(letters)
        m = len(letters)
        idx = {c: i for i, c in enumerate(letters)}
        # convert edges to indices
        e_idx = [(idx[a], idx[b]) for a, b in edges]

        best = m + 1
        good_masks = []

        # precompute adjacency list for indegree updates
        adj = [[] for _ in range(m)]
        for u, v in e_idx:
            adj[u].append(v)

        from collections import deque

        for mask in range(1 << m):
            sz = mask.bit_count()
            if sz > best:
                continue
            # compute indegrees for nodes not in mask
            indeg = [0] * m
            for u, v in e_idx:
                if (mask >> u) & 1 or (mask >> v) & 1:
                    continue
                indeg[v] += 1
            q = deque()
            remaining = m - sz
            for i in range(m):
                if ((mask >> i) & 1) == 0 and indeg[i] == 0:
                    q.append(i)
            cnt = 0
            while q:
                node = q.popleft()
                cnt += 1
                for nb in adj[node]:
                    if (mask >> nb) & 1:
                        continue
                    indeg[nb] -= 1
                    if indeg[nb] == 0:
                        q.append(nb)
            if cnt == remaining:  # acyclic
                if sz < best:
                    best = sz
                    good_masks = [mask]
                elif sz == best:
                    good_masks.append(mask)

        ans = []
        for mask in good_masks:
            freq = [0] * 26
            for c, i in idx.items():
                cnt = 2 if (mask >> i) & 1 else 1
                freq[ord(c) - 97] = cnt
            ans.append(freq)
        return ans
```

## Python3

```python
import sys
from typing import List

class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        # map characters to indices
        chars = {}
        for w in words:
            for ch in w:
                if ch not in chars:
                    chars[ch] = len(chars)
        m = len(chars)
        idx_to_char = [''] * m
        for ch, i in chars.items():
            idx_to_char[i] = ch

        # store edges list
        edges = []
        for w in words:
            u = chars[w[0]]
            v = chars[w[1]]
            edges.append((u, v))

        full_mask = (1 << m) - 1
        min_dup = m + 1
        feasible_masks = []

        # helper to test feasibility of a mask (duplicated letters)
        def is_feasible(mask: int) -> bool:
            Vmask = full_mask ^ mask  # vertices not duplicated
            indeg = [0] * m
            for u, v in edges:
                if ((Vmask >> u) & 1) and ((Vmask >> v) & 1):
                    indeg[v] += 1
            # Kahn's algorithm
            stack = [i for i in range(m) if (Vmask >> i) & 1 and indeg[i] == 0]
            removed = 0
            while stack:
                u = stack.pop()
                removed += 1
                for uu, vv in edges:
                    if uu == u and ((Vmask >> vv) & 1):
                        indeg[vv] -= 1
                        if indeg[vv] == 0:
                            stack.append(vv)
            total_vertices = bin(Vmask).count("1")
            return removed == total_vertices

        # enumerate all subsets
        for mask in range(1 << m):
            dup_cnt = bin(mask).count("1")
            if dup_cnt > min_dup:
                continue
            if is_feasible(mask):
                if dup_cnt < min_dup:
                    min_dup = dup_cnt
                    feasible_masks = [mask]
                elif dup_cnt == min_dup:
                    feasible_masks.append(mask)

        # build frequency arrays for each minimal mask
        res = []
        for mask in feasible_masks:
            freq = [0] * 26
            for i in range(m):
                cnt = 2 if (mask >> i) & 1 else 1
                ch_idx = ord(idx_to_char[i]) - 97
                freq[ch_idx] = cnt
            res.append(freq)
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

int** supersequences(char** words, int wordsSize, int* returnSize, int** returnColumnSizes) {
    // map letters to indices
    int idx[26];
    for (int i = 0; i < 26; ++i) idx[i] = -1;
    int L = 0;
    for (int i = 0; i < wordsSize; ++i) {
        for (int j = 0; j < 2; ++j) {
            int c = words[i][j] - 'a';
            if (idx[c] == -1) idx[c] = L++;
        }
    }

    // adjacency matrix
    char adj[16][16] = {{0}};
    int forcedMask = 0;
    for (int i = 0; i < wordsSize; ++i) {
        int a = words[i][0] - 'a';
        int b = words[i][1] - 'a';
        int ia = idx[a];
        int ib = idx[b];
        if (ia == ib) {
            forcedMask |= (1 << ia);
        } else {
            adj[ia][ib] = 1;
        }
    }

    int allMask = (L == 0) ? 0 : ((1 << L) - 1);
    int remMask = allMask & (~forcedMask);
    // collect indices of remaining letters
    int remIdx[16];
    int remCount = 0;
    for (int i = 0; i < L; ++i) {
        if (remMask & (1 << i)) remIdx[remCount++] = i;
    }

    int minSize = 1000;
    int resultMasksCap = 64, resultCount = 0;
    int *resultMasks = (int *)malloc(sizeof(int) * resultMasksCap);

    int totalSub = 1 << remCount;
    for (int sub = 0; sub < totalSub; ++sub) {
        int dupMask = forcedMask;
        for (int j = 0; j < remCount; ++j) {
            if (sub & (1 << j)) dupMask |= (1 << remIdx[j]);
        }
        int undupMask = allMask ^ dupMask;

        // Kahn's algorithm to test acyclicity on undupMask
        int indeg[16] = {0};
        int vertices = 0;
        for (int u = 0; u < L; ++u) {
            if (!(undupMask & (1 << u))) continue;
            vertices++;
            for (int v = 0; v < L; ++v) {
                if ((undupMask & (1 << v)) && adj[u][v]) indeg[v]++;
            }
        }

        int removed = 0;
        int processed[16] = {0};
        while (1) {
            int found = -1;
            for (int u = 0; u < L; ++u) {
                if ((undupMask & (1 << u)) && !processed[u] && indeg[u] == 0) {
                    found = u;
                    break;
                }
            }
            if (found == -1) break;
            processed[found] = 1;
            removed++;
            for (int v = 0; v < L; ++v) {
                if ((undupMask & (1 << v)) && adj[found][v]) indeg[v]--;
            }
        }

        if (removed == vertices) { // acyclic
            int size = __builtin_popcount((unsigned)dupMask);
            if (size < minSize) {
                minSize = size;
                resultCount = 0;
                if (resultCount >= resultMasksCap) {
                    resultMasksCap *= 2;
                    resultMasks = (int *)realloc(resultMasks, sizeof(int) * resultMasksCap);
                }
                resultMasks[resultCount++] = dupMask;
            } else if (size == minSize) {
                if (resultCount >= resultMasksCap) {
                    resultMasksCap *= 2;
                    resultMasks = (int *)realloc(resultMasks, sizeof(int) * resultMasksCap);
                }
                resultMasks[resultCount++] = dupMask;
            }
        }
    }

    // Build answer
    int **ans = (int **)malloc(sizeof(int *) * resultCount);
    *returnColumnSizes = (int *)malloc(sizeof(int) * resultCount);
    for (int i = 0; i < resultCount; ++i) {
        ans[i] = (int *)calloc(26, sizeof(int));
        (*returnColumnSizes)[i] = 26;
        int mask = resultMasks[i];
        // set frequencies
        for (int c = 0; c < 26; ++c) {
            if (idx[c] != -1) {
                ans[i][c] = (mask & (1 << idx[c])) ? 2 : 1;
            }
        }
    }

    free(resultMasks);
    *returnSize = resultCount;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Numerics;

public class Solution {
    public IList<IList<int>> Supersequences(string[] words) {
        // collect distinct letters
        var letterSet = new HashSet<char>();
        foreach (var w in words) {
            letterSet.Add(w[0]);
            letterSet.Add(w[1]);
        }
        char[] letters = new char[letterSet.Count];
        letterSet.CopyTo(letters);
        int k = letters.Length;
        var idx = new Dictionary<char, int>();
        for (int i = 0; i < k; i++) idx[letters[i]] = i;

        // adjacency matrix
        bool[,] adj = new bool[k, k];
        foreach (var w in words) {
            int u = idx[w[0]];
            int v = idx[w[1]];
            adj[u, v] = true;
        }

        int minSize = k + 1;
        var goodMasks = new List<int>();
        int totalMask = 1 << k;

        for (int mask = 0; mask < totalMask; mask++) {
            if (IsAcyclic(k, adj, mask)) {
                int sz = BitCount(mask);
                if (sz < minSize) {
                    minSize = sz;
                    goodMasks.Clear();
                    goodMasks.Add(mask);
                } else if (sz == minSize) {
                    goodMasks.Add(mask);
                }
            }
        }

        var result = new List<IList<int>>();
        foreach (int mask in goodMasks) {
            int[] freq = new int[26];
            for (int i = 0; i < k; i++) {
                char c = letters[i];
                int cnt = ((mask >> i) & 1) == 1 ? 2 : 1;
                freq[c - 'a'] = cnt;
            }
            var list = new List<int>(freq);
            result.Add(list);
        }

        return result;
    }

    private bool IsAcyclic(int n, bool[,] adj, int mask) {
        // vertices not in mask are active (cnt = 1)
        int[] indeg = new int[n];
        for (int u = 0; u < n; u++) if ((mask >> u & 1) == 0) {
            for (int v = 0; v < n; v++) if ((mask >> v & 1) == 0 && adj[u, v]) {
                indeg[v]++;
            }
        }

        var q = new Queue<int>();
        int remaining = 0;
        for (int i = 0; i < n; i++) if ((mask >> i & 1) == 0) {
            remaining++;
            if (indeg[i] == 0) q.Enqueue(i);
        }

        int processed = 0;
        while (q.Count > 0) {
            int u = q.Dequeue();
            processed++;
            for (int v = 0; v < n; v++) if ((mask >> v & 1) == 0 && adj[u, v]) {
                indeg[v]--;
                if (indeg[v] == 0) q.Enqueue(v);
            }
        }

        return processed == remaining;
    }

    private int BitCount(int x) => BitOperations.PopCount((uint)x);
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number[][]}
 */
var supersequences = function(words) {
    // map each unique letter to an index 0..k-1
    const idxMap = {};
    let k = 0;
    for (const w of words) {
        for (let i = 0; i < 2; ++i) {
            const ch = w.charCodeAt(i) - 97;
            if (!(ch in idxMap)) {
                idxMap[ch] = k++;
            }
        }
    }
    // convert words to pairs of indices
    const pairs = [];
    for (const w of words) {
        const a = idxMap[w.charCodeAt(0) - 97];
        const b = idxMap[w.charCodeAt(1) - 97];
        pairs.push([a, b]);
    }

    const maxMask = 1 << k;
    let bestLen = Infinity;
    const results = [];

    // helper popcount
    const popcnt = (x) => {
        let c = 0;
        while (x) { x &= x - 1; ++c; }
        return c;
    };

    for (let mask = 0; mask < maxMask; ++mask) {
        const cnt = new Array(k);
        let totalLen = 0;
        for (let i = 0; i < k; ++i) {
            cnt[i] = ((mask >> i) & 1) ? 2 : 1;
            totalLen += cnt[i];
        }
        if (totalLen > bestLen) continue; // cannot improve

        const nodeCount = totalLen; // each occurrence is a node
        const maxNodes = k * 2;
        const adj = Array.from({ length: maxNodes }, () => []);
        const indeg = new Int32Array(maxNodes);
        const present = new Uint8Array(maxNodes);

        // mark present nodes
        for (let i = 0; i < k; ++i) {
            const base = i * 2;
            present[base] = 1; // first copy always exists
            if (cnt[i] === 2) present[base + 1] = 1;
        }

        // intra-character edges (first -> second when count==2)
        for (let i = 0; i < k; ++i) {
            if (cnt[i] === 2) {
                const u = i * 2;
                const v = i * 2 + 1;
                adj[u].push(v);
                indeg[v]++;
            }
        }

        // edges for each word: first copy of source -> last copy of target
        let ok = true;
        for (const [a, b] of pairs) {
            const u = a * 2; // first copy of source always exists
            const v = (cnt[b] === 2) ? (b * 2 + 1) : (b * 2);
            // add edge u -> v
            adj[u].push(v);
            indeg[v]++;
        }

        // Kahn's algorithm to detect cycle
        const queue = [];
        for (let node = 0; node < maxNodes; ++node) {
            if (present[node] && indeg[node] === 0) queue.push(node);
        }
        let processed = 0;
        while (queue.length) {
            const u = queue.shift();
            processed++;
            for (const v of adj[u]) {
                indeg[v]--;
                if (indeg[v] === 0) queue.push(v);
            }
        }

        if (processed !== nodeCount) ok = false; // cycle detected

        if (!ok) continue;

        if (totalLen < bestLen) {
            bestLen = totalLen;
            results.length = 0;
        }
        if (totalLen === bestLen) {
            const freq = new Array(26).fill(0);
            for (let i = 0; i < k; ++i) {
                const chCode = Object.keys(idxMap).find(key => idxMap[key] === i);
                // keys are string numbers, convert back to int
                const letterIdx = parseInt(chCode, 10);
                freq[letterIdx] = cnt[i];
            }
            results.push(freq);
        }
    }

    return results;
};
```

## Typescript

```typescript
function supersequences(words: string[]): number[][] {
    // Collect distinct characters
    const charSet = new Set<string>();
    for (const w of words) {
        charSet.add(w[0]);
        charSet.add(w[1]);
    }
    const chars = Array.from(charSet);
    const m = chars.length;
    const idxMap = new Map<string, number>();
    chars.forEach((c, i) => idxMap.set(c, i));

    // Store edges (uIdx -> vIdx)
    const edgeList: [number, number][] = [];
    for (const w of words) {
        const u = idxMap.get(w[0])!;
        const v = idxMap.get(w[1])!;
        edgeList.push([u, v]);
    }

    const feasibleMasks: number[] = [];
    const lengths: number[] = [];

    const totalMasks = 1 << m;
    for (let mask = 0; mask < totalMasks; ++mask) {
        // assign extra node ids for duplicated characters
        const extraId = new Array<number>(m).fill(-1);
        let dupCount = 0;
        for (let i = 0; i < m; ++i) {
            if ((mask >> i) & 1) {
                extraId[i] = m + dupCount;
                dupCount++;
            }
        }
        const nodeCnt = m + dupCount;
        const adj: number[][] = Array.from({ length: nodeCnt }, () => []);
        const indeg = new Int32Array(nodeCnt);

        // edges for duplicated characters (first -> last)
        for (let i = 0; i < m; ++i) {
            if ((mask >> i) & 1) {
                const from = i;
                const to = extraId[i];
                adj[from].push(to);
                indeg[to]++;
            }
        }

        // edges from words: first(u) -> last(v)
        let hasSelfLoop = false;
        for (const [u, v] of edgeList) {
            const from = u; // always first occurrence node
            const to = ((mask >> v) & 1) ? extraId[v] : v;
            if (from === to) { // self-loop -> impossible
                hasSelfLoop = true;
                break;
            }
            adj[from].push(to);
            indeg[to]++;
        }
        if (hasSelfLoop) continue;

        // Kahn's algorithm for cycle detection
        const queue: number[] = [];
        for (let i = 0; i < nodeCnt; ++i) {
            if (indeg[i] === 0) queue.push(i);
        }
        let processed = 0;
        for (let qIdx = 0; qIdx < queue.length; ++qIdx) {
            const u = queue[qIdx];
            processed++;
            for (const v of adj[u]) {
                indeg[v]--;
                if (indeg[v] === 0) queue.push(v);
            }
        }
        if (processed === nodeCnt) {
            feasibleMasks.push(mask);
            lengths.push(m + dupCount);
        }
    }

    // Find minimal length
    let minLen = Infinity;
    for (const len of lengths) {
        if (len < minLen) minLen = len;
    }

    const result: number[][] = [];
    for (let i = 0; i < feasibleMasks.length; ++i) {
        if (lengths[i] !== minLen) continue;
        const mask = feasibleMasks[i];
        const freq = new Array<number>(26).fill(0);
        for (let j = 0; j < m; ++j) {
            const cnt = 1 + ((mask >> j) & 1);
            const chCode = chars[j].charCodeAt(0) - 97;
            freq[chCode] = cnt;
        }
        result.push(freq);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer[][]
     */
    function supersequences($words) {
        // map letters to indices
        $letterIdx = [];
        $idxLetter = [];
        $hasDouble = []; // whether a letter appears in a word like "aa"
        $edges = []; // adjacency list, temporary using chars

        foreach ($words as $w) {
            $a = $w[0];
            $b = $w[1];

            if (!isset($letterIdx[$a])) {
                $letterIdx[$a] = count($letterIdx);
                $idxLetter[] = $a;
                $hasDouble[$a] = false;
            }
            if (!isset($letterIdx[$b])) {
                $letterIdx[$b] = count($letterIdx);
                $idxLetter[] = $b;
                $hasDouble[$b] = false;
            }

            if ($a === $b) {
                $hasDouble[$a] = true; // need two copies of this letter
            } else {
                if (!isset($edges[$a])) $edges[$a] = [];
                $edges[$a][$b] = true; // directed edge a -> b
            }
        }

        $L = count($letterIdx);
        $required = array_fill(0, $L, 0);
        for ($i = 0; $i < $L; ++$i) {
            $ch = $idxLetter[$i];
            $required[$i] = $hasDouble[$ch] ? 2 : 1;
        }

        // build adjacency list with indices
        $adj = array_fill(0, $L, []);
        foreach ($edges as $from => $tos) {
            $u = $letterIdx[$from];
            foreach ($tos as $to => $_) {
                $v = $letterIdx[$to];
                $adj[$u][] = $v;
            }
        }

        // optional letters (those with count 1 initially)
        $optionalIdx = [];
        for ($i = 0; $i < $L; ++$i) {
            if ($required[$i] == 1) $optionalIdx[] = $i;
        }
        $optK = count($optionalIdx);
        $baseSum = array_sum($required);

        $minLen = PHP_INT_MAX;
        $bestCounts = [];

        // helper: cycle detection on induced subgraph of singles
        $hasCycle = function($singles, $adj) {
            $set = array_flip($singles);
            $color = [];
            foreach ($singles as $v) $color[$v] = 0;
            $dfs = null;
            $dfs = function($u) use (&$dfs, &$color, $adj, $set) {
                $color[$u] = 1;
                foreach ($adj[$u] as $v) {
                    if (!isset($set[$v])) continue; // ignore non‑single vertices
                    if ($color[$v] === 0) {
                        if ($dfs($v)) return true;
                    } elseif ($color[$v] === 1) {
                        return true; // back edge -> cycle
                    }
                }
                $color[$u] = 2;
                return false;
            };
            foreach ($singles as $v) {
                if ($color[$v] === 0) {
                    if ($dfs($v)) return true;
                }
            }
            return false;
        };

        $totalMasks = 1 << $optK;
        for ($mask = 0; $mask < $totalMasks; ++$mask) {
            // compute counts for this mask
            $counts = $required;
            for ($j = 0; $j < $optK; ++$j) {
                if (($mask >> $j) & 1) {
                    $idx = $optionalIdx[$j];
                    $counts[$idx] = 2;
                }
            }

            // collect vertices with count == 1 (singles)
            $singles = [];
            for ($i = 0; $i < $L; ++$i) {
                if ($counts[$i] === 1) $singles[] = $i;
            }

            // check feasibility: induced subgraph of singles must be acyclic
            if ($hasCycle($singles, $adj)) continue;

            $len = array_sum($counts);
            if ($len < $minLen) {
                $minLen = $len;
                $bestCounts = [$counts];
            } elseif ($len === $minLen) {
                $bestCounts[] = $counts;
            }
        }

        // build result frequency vectors
        $result = [];
        foreach ($bestCounts as $cntArr) {
            $freq = array_fill(0, 26, 0);
            for ($i = 0; $i < $L; ++$i) {
                $ch = $idxLetter[$i];
                $freq[ord($ch) - 97] = $cntArr[$i];
            }
            $result[] = $freq;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func supersequences(_ words: [String]) -> [[Int]] {
        var charToIdx = [Character:Int]()
        var idx = 0
        var presentMask = 0
        var forcedMask = 0
        var edges = [(Int, Int)]()
        
        for w in words {
            let chars = Array(w)
            guard chars.count == 2 else { continue }
            let a = chars[0]
            let b = chars[1]
            if charToIdx[a] == nil {
                charToIdx[a] = idx
                idx += 1
            }
            if charToIdx[b] == nil {
                charToIdx[b] = idx
                idx += 1
            }
            let ia = charToIdx[a]!
            let ib = charToIdx[b]!
            presentMask |= (1 << ia)
            presentMask |= (1 << ib)
            if a == b {
                forcedMask |= (1 << ia)
            } else {
                edges.append((ia, ib))
            }
        }
        
        let m = idx
        var adj = [[Int]](repeating: [], count: m)
        for (u, v) in edges {
            adj[u].append(v)
        }
        
        func isAcyclic(_ mask: Int) -> Bool {
            var state = [Int](repeating: 0, count: m) // 0 unvisited,1 visiting,2 done
            func dfs(_ u: Int) -> Bool {
                state[u] = 1
                for v in adj[u] where (mask >> v) & 1 == 1 {
                    if state[v] == 1 { return false }
                    if state[v] == 0 && !dfs(v) { return false }
                }
                state[u] = 2
                return true
            }
            for i in 0..<m where ((mask >> i) & 1) == 1 {
                if state[i] == 0 {
                    if !dfs(i) { return false }
                }
            }
            return true
        }
        
        let optionalMask = presentMask & ~forcedMask
        var optIndices = [Int]()
        for i in 0..<m where ((optionalMask >> i) & 1) == 1 {
            optIndices.append(i)
        }
        let k = optIndices.count
        var minSize = Int.max
        var resultMasks = [Int]()
        
        let totalSubsets = 1 << k
        for sub in 0..<totalSubsets {
            var extraMask = 0
            var bit = sub
            var idxBit = 0
            while bit > 0 {
                if (bit & 1) == 1 {
                    extraMask |= (1 << optIndices[idxBit])
                }
                idxBit += 1
                bit >>= 1
            }
            let dupMask = forcedMask | extraMask
            let remainingMask = presentMask ^ dupMask
            if isAcyclic(remainingMask) {
                let size = dupMask.nonzeroBitCount
                if size < minSize {
                    minSize = size
                    resultMasks = [dupMask]
                } else if size == minSize {
                    resultMasks.append(dupMask)
                }
            }
        }
        
        var answer = [[Int]]()
        for mask in resultMasks {
            var freq = Array(repeating: 0, count: 26)
            for (ch, i) in charToIdx {
                if ((presentMask >> i) & 1) == 1 {
                    var cnt = 1
                    if ((mask >> i) & 1) == 1 { cnt += 1 }
                    let idxAlpha = Int(ch.unicodeScalars.first!.value - UnicodeScalar("a").value)
                    freq[idxAlpha] = cnt
                }
            }
            answer.append(freq)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun supersequences(words: Array<String>): List<List<Int>> {
        // Collect unique letters
        val letterSet = mutableSetOf<Char>()
        for (w in words) {
            letterSet.add(w[0])
            letterSet.add(w[1])
        }
        val letters = letterSet.toList()
        val k = letters.size
        val idxMap = IntArray(26) { -1 }
        for ((i, ch) in letters.withIndex()) {
            idxMap[ch - 'a'] = i
        }

        // Store edges as indices
        val edgeA = IntArray(words.size)
        val edgeB = IntArray(words.size)
        for (i in words.indices) {
            val a = idxMap[words[i][0] - 'a']
            val b = idxMap[words[i][1] - 'a']
            edgeA[i] = a
            edgeB[i] = b
        }

        var minLen = Int.MAX_VALUE
        val bestMasks = mutableListOf<Int>()
        val totalMasks = 1 shl k

        for (mask in 0 until totalMasks) {
            // indegree for vertices that are single (bit not set)
            val indeg = IntArray(k)
            for (e in words.indices) {
                val a = edgeA[e]
                val b = edgeB[e]
                val dupA = (mask ushr a) and 1 == 1
                val dupB = (mask ushr b) and 1 == 1
                if (!dupA && !dupB) {
                    indeg[b]++
                }
            }

            // Kahn's algorithm on single vertices
            val q: ArrayDeque<Int> = ArrayDeque()
            var visited = 0
            for (i in 0 until k) {
                if ((mask ushr i and 1) == 0 && indeg[i] == 0) {
                    q.add(i)
                }
            }

            while (!q.isEmpty()) {
                val v = q.poll()
                visited++
                // process outgoing edges where both ends are single
                for (e in words.indices) {
                    if (edgeA[e] == v) {
                        val a = edgeA[e]
                        val b = edgeB[e]
                        val dupA = (mask ushr a) and 1 == 1
                        val dupB = (mask ushr b) and 1 == 1
                        if (!dupA && !dupB) {
                            indeg[b]--
                            if (indeg[b] == 0) q.add(b)
                        }
                    }
                }
            }

            var singles = 0
            for (i in 0 until k) if ((mask ushr i and 1) == 0) singles++

            if (visited != singles) continue // cycle among single vertices

            val len = k + Integer.bitCount(mask) // each duplicated letter adds one extra copy
            when {
                len < minLen -> {
                    minLen = len
                    bestMasks.clear()
                    bestMasks.add(mask)
                }
                len == minLen -> bestMasks.add(mask)
            }
        }

        val result = mutableListOf<List<Int>>()
        for (mask in bestMasks) {
            val freq = IntArray(26) { 0 }
            for ((i, ch) in letters.withIndex()) {
                val cnt = if ((mask ushr i and 1) == 1) 2 else 1
                freq[ch - 'a'] = cnt
            }
            result.add(freq.toList())
        }
        return result
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  List<List<int>> supersequences(List<String> words) {
    // Map each unique letter to an index
    Map<String, int> idx = {};
    List<String> letters = [];
    for (var w in words) {
      for (int i = 0; i < 2; i++) {
        String ch = w[i];
        if (!idx.containsKey(ch)) {
          idx[ch] = letters.length;
          letters.add(ch);
        }
      }
    }
    int n = letters.length;

    // Build edge list
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var w in words) {
      int u = idx[w[0]]!;
      int v = idx[w[1]]!;
      adj[u].add(v);
    }

    // Helper: popcount
    int popCount(int x) {
      int cnt = 0;
      while (x != 0) {
        cnt += x & 1;
        x >>= 1;
      }
      return cnt;
    }

    // Check if subset mask of duplicated letters yields acyclic constrained graph
    bool isAcyclic(int dupMask) {
      List<int> state = List.filled(n, 0); // 0=unvisited,1=visiting,2=done

      bool dfs(int u) {
        if (state[u] == 1) return false; // cycle
        if (state[u] == 2) return true;
        state[u] = 1;
        for (int v in adj[u]) {
          // consider edge only if target not duplicated
          if ((dupMask >> v & 1) == 0) {
            if (!dfs(v)) return false;
          }
        }
        state[u] = 2;
        return true;
      }

      for (int i = 0; i < n; i++) {
        if (state[i] == 0) {
          if (!dfs(i)) return false;
        }
      }
      return true;
    }

    int minLen = 1 << 30;
    List<int> bestMasks = [];

    int totalMasks = 1 << n;
    for (int mask = 0; mask < totalMasks; mask++) {
      if (!isAcyclic(mask)) continue;
      int len = n + popCount(mask);
      if (len < minLen) {
        minLen = len;
        bestMasks.clear();
        bestMasks.add(mask);
      } else if (len == minLen) {
        bestMasks.add(mask);
      }
    }

    List<List<int>> result = [];
    for (int mask in bestMasks) {
      List<int> freq = List.filled(26, 0);
      for (int i = 0; i < n; i++) {
        int count = ((mask >> i) & 1) == 1 ? 2 : 1;
        int charCode = letters[i].codeUnitAt(0) - 97;
        freq[charCode] = count;
      }
      result.add(freq);
    }

    return result;
  }
}
```

## Golang

```go
package main

import (
	"math/bits"
)

func supersequences(words []string) [][]int {
	// collect unique letters
	letterIdx := make(map[byte]int)
	var letters []byte
	for _, w := range words {
		for i := 0; i < 2; i++ {
			c := w[i]
			if _, ok := letterIdx[c]; !ok {
				letterIdx[c] = len(letters)
				letters = append(letters, c)
			}
		}
	}
	m := len(letters)
	adj := make([][]bool, m)
	for i := 0; i < m; i++ {
		adj[i] = make([]bool, m)
	}
	// build adjacency matrix
	for _, w := range words {
		u := letterIdx[w[0]]
		v := letterIdx[w[1]]
		adj[u][v] = true
	}

	isAcyclic := func(mask int) bool {
		indeg := make([]int, m)
		for u := 0; u < m; u++ {
			if mask&(1<<u) != 0 {
				continue
			}
			for v := 0; v < m; v++ {
				if mask&(1<<v) != 0 {
					continue
				}
				if adj[u][v] {
					indeg[v]++
				}
			}
		}
		queue := make([]int, 0)
		for i := 0; i < m; i++ {
			if mask&(1<<i) == 0 && indeg[i] == 0 {
				queue = append(queue, i)
			}
		}
		processed := 0
		for len(queue) > 0 {
			u := queue[0]
			queue = queue[1:]
			processed++
			for v := 0; v < m; v++ {
				if mask&(1<<v) != 0 {
					continue
				}
				if adj[u][v] {
					indeg[v]--
					if indeg[v] == 0 {
						queue = append(queue, v)
					}
				}
			}
		}
		total := 0
		for i := 0; i < m; i++ {
			if mask&(1<<i) == 0 {
				total++
			}
		}
		return processed == total
	}

	minDup := m + 1
	var feasibleMasks []int
	fullMask := (1 << m) - 1
	for mask := 0; mask <= fullMask; mask++ {
		if !isAcyclic(mask) {
			continue
		}
		cnt := bits.OnesCount(uint(mask))
		if cnt < minDup {
			minDup = cnt
			feasibleMasks = []int{mask}
		} else if cnt == minDup {
			feasibleMasks = append(feasibleMasks, mask)
		}
	}

	results := make([][]int, 0, len(feasibleMasks))
	for _, mask := range feasibleMasks {
		freq := make([]int, 26)
		for i, ch := range letters {
			cnt := 1
			if mask&(1<<i) != 0 {
				cnt = 2
			}
			freq[ch-'a'] = cnt
		}
		results = append(results, freq)
	}
	return results
}
```

## Ruby

```ruby
def supersequences(words)
  # collect distinct letters
  letter_set = {}
  words.each { |w| w.each_char { |ch| letter_set[ch] = true } }
  letters = letter_set.keys
  m = letters.size
  idx = {}
  letters.each_with_index { |ch, i| idx[ch] = i }

  # build graph edges (directed)
  out = Array.new(m) { [] }
  forced_mask = 0

  words.each do |w|
    x = w[0]
    y = w[1]
    if x == y
      forced_mask |= (1 << idx[x])
    else
      u = idx[x]
      v = idx[y]
      out[u] << v
    end
  end

  total_masks = 1 << m
  min_size = nil
  good_masks = []

  (0...total_masks).each do |mask|
    next if (mask & forced_mask) != forced_mask
    size = mask.to_s(2).count('1')
    next if !min_size.nil? && size > min_size

    # check acyclicity of remaining vertices
    indeg = Array.new(m, 0)
    remain = []
    m.times do |i|
      unless (mask >> i) & 1 == 1
        remain << i
      end
    end

    remain.each do |u|
      out[u].each do |v|
        next if ((mask >> v) & 1) == 1
        indeg[v] += 1
      end
    end

    queue = []
    remain.each { |i| queue << i if indeg[i] == 0 }
    visited = 0
    until queue.empty?
      u = queue.shift
      visited += 1
      out[u].each do |v|
        next if ((mask >> v) & 1) == 1
        indeg[v] -= 1
        queue << v if indeg[v] == 0
      end
    end

    next unless visited == remain.size # not acyclic

    if min_size.nil? || size < min_size
      min_size = size
      good_masks = [mask]
    elsif size == min_size
      good_masks << mask
    end
  end

  result = []
  good_masks.each do |mask|
    freq = Array.new(26, 0)
    letters.each do |ch|
      i = idx[ch]
      cnt = ((mask >> i) & 1) == 1 ? 2 : 1
      freq[ch.ord - 97] = cnt
    end
    result << freq
  end
  result
end
```

## Scala

```scala
object Solution {
    def supersequences(words: Array[String]): List[List[Int]] = {
        // collect distinct letters
        val letterSet = scala.collection.mutable.Set[Char]()
        for (w <- words) {
            letterSet += w.charAt(0)
            letterSet += w.charAt(1)
        }
        val letters = letterSet.toArray.sorted
        val k = letters.length

        // map char to index 0..k-1
        val idx = new Array[Int](26)
        java.util.Arrays.fill(idx, -1)
        for (i <- 0 until k) {
            idx(letters(i) - 'a') = i
        }

        // mask of letters that must be duplicated because of "xx"
        var requiredDupMask = 0
        for (w <- words if w.charAt(0) == w.charAt(1)) {
            val i = idx(w.charAt(0) - 'a')
            requiredDupMask |= (1 << i)
        }

        // store edges where characters differ
        val diffEdges = new scala.collection.mutable.ArrayBuffer[(Int, Int)]()
        for (w <- words if w.charAt(0) != w.charAt(1)) {
            val u = idx(w.charAt(0) - 'a')
            val v = idx(w.charAt(1) - 'a')
            diffEdges += ((u, v))
        }

        var minLen = Int.MaxValue
        val bestMasks = scala.collection.mutable.ArrayBuffer[Int]()

        val limit = 1 << k
        for (mask <- 0 until limit) {
            // must contain all required duplicated letters
            if ((mask & requiredDupMask) != requiredDupMask) {
                // skip invalid mask
            } else {
                // build graph with edges where both endpoints are not duplicated
                val indeg = new Array[Int](k)
                val adj = Array.fill(k)(new scala.collection.mutable.ArrayBuffer[Int]())
                for ((u, v) <- diffEdges) {
                    val dupU = (mask >> u) & 1
                    val dupV = (mask >> v) & 1
                    if (dupU == 0 && dupV == 0) {
                        adj(u).append(v)
                        indeg(v) += 1
                    }
                }

                // topological sort to detect cycle
                val q = new scala.collection.mutable.Queue[Int]()
                for (i <- 0 until k) if (indeg(i) == 0) q.enqueue(i)

                var visited = 0
                while (q.nonEmpty) {
                    val cur = q.dequeue()
                    visited += 1
                    for (nb <- adj(cur)) {
                        indeg(nb) -= 1
                        if (indeg(nb) == 0) q.enqueue(nb)
                    }
                }

                if (visited == k) { // acyclic, valid supersequence length
                    val len = k + Integer.bitCount(mask)
                    if (len < minLen) {
                        minLen = len
                        bestMasks.clear()
                        bestMasks += mask
                    } else if (len == minLen) {
                        bestMasks += mask
                    }
                }
            }
        }

        // construct frequency arrays for each optimal mask
        val result = scala.collection.mutable.ArrayBuffer[List[Int]]()
        for (mask <- bestMasks) {
            val freq = Array.fill(26)(0)
            for (i <- 0 until k) {
                val chIdx = letters(i) - 'a'
                var cnt = 1
                if (((mask >> i) & 1) == 1) cnt += 1
                freq(chIdx) = cnt
            }
            result += freq.toList
        }

        result.toList
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn supersequences(words: Vec<String>) -> Vec<Vec<i32>> {
        // Map each distinct letter to an index
        let mut idx_map: HashMap<char, usize> = HashMap::new();
        for w in &words {
            for ch in w.chars() {
                idx_map.entry(ch).or_insert_with(|| idx_map.len());
            }
        }
        let k = idx_map.len();
        let mut letters: Vec<char> = vec![' '; k];
        for (ch, &i) in &idx_map {
            letters[i] = *ch;
        }

        // adjacency matrix and forced duplicate mask
        let mut edges = vec![vec![false; k]; k];
        let mut forced_mask: u32 = 0;

        for w in words {
            let mut chars = w.chars();
            let c1 = chars.next().unwrap();
            let c2 = chars.next().unwrap();
            let i1 = idx_map[&c1];
            let i2 = idx_map[&c2];
            if i1 == i2 {
                forced_mask |= 1 << i1;
            } else {
                edges[i1][i2] = true;
            }
        }

        let total_masks = 1u32 << k;
        let mut best_len: usize = usize::MAX;
        let mut best_masks: Vec<u32> = Vec::new();

        for mask in 0..total_masks {
            if (mask & forced_mask) != forced_mask {
                continue; // must include all forced duplicates
            }

            // check acyclicity on subgraph of singleton nodes
            let mut state = vec![0u8; k]; // 0=unvisited,1=visiting,2=done
            let mut ok = true;

            fn dfs(u: usize, edges: &Vec<Vec<bool>>, mask: u32, state: &mut Vec<u8>, ok: &mut bool) {
                if !*ok { return; }
                state[u] = 1;
                for v in 0..edges.len() {
                    if !(edges[u][v]) { continue; }
                    // ignore edge if either endpoint is duplicated
                    if (mask >> u) & 1 == 1 || (mask >> v) & 1 == 1 {
                        continue;
                    }
                    if state[v] == 0 {
                        dfs(v, edges, mask, state, ok);
                        if !*ok { return; }
                    } else if state[v] == 1 {
                        *ok = false;
                        return;
                    }
                }
                state[u] = 2;
            }

            for i in 0..k {
                if (mask >> i) & 1 == 1 { continue; } // duplicated node, skip
                if state[i] == 0 {
                    dfs(i, &edges, mask, &mut state, &mut ok);
                    if !ok { break; }
                }
            }

            if !ok { continue; }

            let len = k + mask.count_ones() as usize;
            if len < best_len {
                best_len = len;
                best_masks.clear();
                best_masks.push(mask);
            } else if len == best_len {
                best_masks.push(mask);
            }
        }

        // Build result frequencies
        let mut result: Vec<Vec<i32>> = Vec::new();
        for mask in best_masks {
            let mut freq = vec![0i32; 26];
            for i in 0..k {
                let ch = letters[i];
                let cnt = 1 + ((mask >> i) & 1) as i32;
                freq[(ch as u8 - b'a') as usize] = cnt;
            }
            result.push(freq);
        }
        result
    }
}
```

## Racket

```racket
#lang racket
(require racket/contract)

(define/contract (supersequences words)
  (-> (listof string?) (listof (listof exact-integer?)))
  (let* ((char-index (make-hash))
         (next 0)
         (edges '()))
    ;; map characters to indices and collect edges
    (for ([w words])
      (define a (string-ref w 0))
      (define b (string-ref w 1))
      (unless (hash-has-key? char-index a)
        (hash-set! char-index a next)
        (set! next (+ next 1)))
      (unless (hash-has-key? char-index b)
        (hash-set! char-index b next)
        (set! next (+ next 1)))
      (define u (hash-ref char-index a))
      (define v (hash-ref char-index b))
      (set! edges (cons (list u v) edges)))
    (define n next)
    ;; adjacency list for all vertices
    (define out (make-vector n '()))
    (for ([e edges])
      (define u (first e))
      (define v (second e))
      (vector-set! out u (cons v (vector-ref out u))))
    (define all-mask (sub1 (arithmetic-shift 1 n))) ; bits 0..n-1 set

    ;; test if induced subgraph on vertices not in mask is acyclic
    (define (acyclic? mask)
      (let* ((indeg (make-vector n 0))
             (queue '())
             (cnt 0))
        ;; compute indegrees for remaining vertices
        (for ([u (in-range n)])
          (when (= (bitwise-and mask (arithmetic-shift 1 u)) 0)
            (for ([v (vector-ref out u)])
              (when (= (bitwise-and mask (arithmetic-shift 1 v)) 0)
                (vector-set! indeg v (+ (vector-ref indeg v) 1))))))
        ;; initial queue
        (for ([i (in-range n)])
          (when (and (= (bitwise-and mask (arithmetic-shift 1 i)) 0)
                     (= (vector-ref indeg i) 0))
            (set! queue (cons i queue))))
        ;; Kahn's algorithm
        (let loop ((queue queue) (cnt cnt))
          (if (null? queue)
              (= cnt (- n (bitwise-bit-count mask))) ; visited all remaining
              (let* ((v (car queue))
                     (new-queue (cdr queue))
                     (new-cnt (+ cnt 1)))
                (for ([w (vector-ref out v)])
                  (when (= (bitwise-and mask (arithmetic-shift 1 w)) 0)
                    (let ((d (- (vector-ref indeg w) 1)))
                      (vector-set! indeg w d)
                      (when (= d 0)
                        (set! new-queue (cons w new-queue))))))
                (loop new-queue new-cnt))))))

    ;; find minimal feedback vertex set size and collect all masks achieving it
    (let ((min-size n)
          (valid-masks '()))
      (for ([mask (in-range 0 (arithmetic-shift 1 n))])
        (define sz (bitwise-bit-count mask))
        (when (<= sz min-size)
          (when (acyclic? mask)
            (cond [(< sz min-size)
                   (set! min-size sz)
                   (set! valid-masks (list mask))]
                  [else
                   (set! valid-masks (cons mask valid-masks))]))))
      ;; build result frequency vectors
      (let ((result '()))
        (for ([mask valid-masks])
          (define freq-vec (make-vector 26 0))
          (hash-for-each char-index
                         (lambda (ch idx)
                           (define cnt (if (= (bitwise-and mask (arithmetic-shift 1 idx)) 0) 1 2))
                           (define pos (- (char->integer ch) (char->integer #\a)))
                           (vector-set! freq-vec pos (+ (vector-ref freq-vec pos) cnt))))
          (set! result (cons (vector->list freq-vec) result)))
        result))))
```

## Erlang

```erlang
-spec supersequences(Words :: [unicode:unicode_binary()]) -> [[integer()]].
supersequences(Words) ->
    % Collect unique letters and map to indices
    Letters = lists:usort(lists:flatten([binary_to_list(W) || W <- Words])),
    LetterIdxMap = maps:from_list([{L, I} || {L, I} <- lists:zip(Letters, lists:seq(0, length(Letters)-1))]),
    K = length(Letters),

    % Determine forced duplicates (words like "aa")
    ForcedDupMask = lists:foldl(fun(W, Acc) ->
        [C1, C2] = binary_to_list(W),
        if C1 == C2 ->
                Idx = maps:get(C1, LetterIdxMap),
                Acc bor (1 bsl Idx);
           true -> Acc
        end
    end, 0, Words),

    % Build adjacency list for distinct-letter edges
    AdjList = lists:foldl(fun(W, Acc) ->
        [C1, C2] = binary_to_list(W),
        if C1 == C2 -> Acc;
           true ->
                From = maps:get(C1, LetterIdxMap),
                To   = maps:get(C2, LetterIdxMap),
                maps:update_with(From,
                                 fun(L) -> [To|L] end,
                                 [To],
                                 Acc)
        end
    end, #{}, Words),

    % Precompute list of all masks that include forced duplicates
    AllMasks = lists:filter(fun(M) -> (M band ForcedDupMask) == ForcedDupMask end,
                            lists:seq(0, (1 bsl K) - 1)),

    % Find minimal total length among feasible masks
    {MinLen, FeasibleMasks} = find_min_masks(AllMasks, AdjList, K),

    % Build frequency vectors for each feasible mask
    [mask_to_freq(Mask, Letters, LetterIdxMap) || Mask <- FeasibleMasks].

% Find minimal length and collect masks achieving it
find_min_masks(Masks, AdjList, K) ->
    find_min_masks(Masks, AdjList, K, undefined, []).

find_min_masks([], _AdjList, _K, MinLen, Acc) ->
    {MinLen, lists:reverse(Acc)};
find_min_masks([Mask|Rest], AdjList, K, CurMin, Acc) ->
    case is_acyclic(Mask, AdjList, K) of
        true ->
            DupCount = popcount(Mask),
            TotalLen = K + DupCount,
            case CurMin of
                undefined -> find_min_masks(Rest, AdjList, K, TotalLen, [Mask]);
                _ when TotalLen < CurMin -> find_min_masks(Rest, AdjList, K, TotalLen, [Mask]);
                _ when TotalLen == CurMin -> find_min_masks(Rest, AdjList, K, CurMin, [Mask|Acc]);
                _ -> find_min_masks(Rest, AdjList, K, CurMin, Acc)
            end;
        false ->
            find_min_masks(Rest, AdjList, K, CurMin, Acc)
    end.

% Check if subgraph induced by vertices NOT in Mask is acyclic
is_acyclic(Mask, AdjList, K) ->
    RemainingMask = bnot(Mask) band ((1 bsl K) - 1),
    Vertices = bits_to_list(RemainingMask, K),
    % compute indegrees
    Indeg0 = maps:from_list([{V,0} || V <- Vertices]),
    Indeg = lists:foldl(fun(V, Acc) ->
                case maps:get(V, AdjList, []) of
                    [] -> Acc;
                    Nbs -> lists:foldl(fun(Nb, A) ->
                                if (RemainingMask band (1 bsl Nb)) =/= 0 ->
                                        maps:update_with(Nb,
                                                         fun(C) -> C+1 end,
                                                         1,
                                                         A);
                                   true -> A
                                end
                            end, Acc, Nbs)
                end
            end, Indeg0, Vertices),
    % Kahn's algorithm
    Queue = [V || V <- Vertices, maps:get(V, Indeg) == 0],
    process_queue(Queue, Indeg, AdjList, RemainingMask, 0, length(Vertices)).

process_queue(_Q, _Indeg, _AdjList, _RemMask, Processed, Total) when Processed == Total ->
    true;
process_queue([], _Indeg, _AdjList, _RemMask, Processed, Total) ->
    false; % cycle exists
process_queue([V|RestQueue], Indeg, AdjList, RemMask, Processed, Total) ->
    Nbs = maps:get(V, AdjList, []),
    {NewIndeg, NewQueue} = lists:foldl(fun(Nb, {IAcc,QAcc}) ->
                if (RemMask band (1 bsl Nb)) =/= 0 ->
                        Cur = maps:get(Nb, IAcc),
                        Updated = Cur - 1,
                        I2 = maps:put(Nb, Updated, IAcc),
                        Q2 = if Updated == 0 -> [Nb|QAcc]; true -> QAcc end,
                        {I2, Q2};
                   true -> {IAcc, QAcc}
                end
            end, {Indeg, RestQueue}, Nbs),
    process_queue(NewQueue, NewIndeg, AdjList, RemMask, Processed+1, Total).

% Convert mask to frequency vector of length 26
mask_to_freq(Mask, Letters, LetterIdxMap) ->
    Freq0 = lists:duplicate(26, 0),
    Freq = lists:foldl(fun({Letter, Idx}, Acc) ->
                Count = if (Mask band (1 bsl Idx)) =/= 0 -> 2; true -> 1 end,
                Pos = Letter - $a,
                lists:update_at(Pos, fun(_)->Count end, Acc)
            end, Freq0, maps:to_list(LetterIdxMap)),
    Freq.

% Helper: list of set bit positions
bits_to_list(0, _K) -> [];
bits_to_list(Mask, K) ->
    bits_to_list(Mask, 0, K, []).

bits_to_list(_Mask, I, K, Acc) when I >= K -> lists:reverse(Acc);
bits_to_list(Mask, I, K, Acc) ->
    Bit = (Mask band (1 bsl I)),
    NewAcc = if Bit =/= 0 -> [I|Acc]; true -> Acc end,
    bits_to_list(Mask, I+1, K, NewAcc).

% Popcount of integer
popcount(N) -> popcount(N, 0).
popcount(0, Acc) -> Acc;
popcount(N, Acc) -> popcount(N band (N-1), Acc+1).
```

## Elixir

```elixir
defmodule Solution do
  @spec supersequences(words :: [String.t]) :: [[integer]]
  def supersequences(words) do
    import Bitwise

    # Unique characters and indexing
    chars =
      words
      |> Enum.flat_map(&String.graphemes/1)
      |> Enum.uniq()

    k = length(chars)

    char_to_idx =
      chars
      |> Enum.with_index()
      |> Map.new(fn {c, i} -> {c, i} end)

    # Precompute word edges as indices
    word_edges =
      words
      |> Enum.map(fn w ->
        [a, b] = String.graphemes(w)
        {char_to_idx[a], char_to_idx[b]}
      end)

    total_masks = 1 <<< k

    popcnt = fn mask -> Integer.bit_count(mask) end

    # Feasibility check for a given mask
    feasible = fn mask ->
      # Build list of existing node ids
      nodes =
        Enum.reduce(0..(k - 1), [], fn i, acc ->
          base = i * 2

          if (mask &&& (1 <<< i)) != 0 do
            [base + 1, base | acc]
          else
            [base | acc]
          end
        end)

      # Build adjacency map and indegree map
      {adj, indeg} =
        Enum.reduce([], {%{}, %{}}, fn _, {a_acc, i_acc} -> {a_acc, i_acc} end)
        |> then(fn {a0, i0} ->
          # start with empty maps for all nodes
          a1 = Map.new(nodes, fn n -> {n, []} end)
          i1 = Map.new(nodes, fn n -> {n, 0} end)

          # duplicate internal edges
          dup_edges =
            Enum.filter(0..(k - 1), fn i -> (mask &&& (1 <<< i)) != 0 end)
            |> Enum.map(fn i -> {i * 2, i * 2 + 1} end)

          # word constraint edges
          word_constr =
            Enum.map(word_edges, fn {ia, ib} ->
              src = ia * 2

              tgt =
                if (mask &&& (1 <<< ib)) != 0 do
                  ib * 2 + 1
                else
                  ib * 2
                end

              {src, tgt}
            end)

          all_edges = dup_edges ++ word_constr

          # populate adjacency and indegree
          {adj_final, indeg_final} =
            Enum.reduce(all_edges, {a1, i1}, fn {u, v}, {adj_map, indeg_map} ->
              adj_map = Map.update!(adj_map, u, &[v | &1])
              indeg_map = Map.update!(indeg_map, v, &(&1 + 1))
              {adj_map, indeg_map}
            end)

          {adj_final, indeg_final}
        end)

      # Kahn's algorithm
      queue =
        nodes
        |> Enum.filter(fn n -> Map.get(indeg, n) == 0 end)
        |> :queue.from_list()

      process = fn rec, q, indeg_map, processed ->
        case :queue.out(q) do
          {:empty, _} ->
            {processed, indeg_map}

          {{:value, node}, q_next} ->
            {indeg_new, q_new} =
              Enum.reduce(Map.get(adj, node, []), {indeg_map, q_next}, fn v,
                                                                        {ind, qq} ->
                new_deg = Map.get(ind, v) - 1
                ind2 = Map.put(ind, v, new_deg)

                if new_deg == 0 do
                  {:ok, qq2} = :queue.in(v, qq) |> then(&{:ok, &1})
                  {ind2, qq2}
                else
                  {ind2, qq}
                end
              end)

            rec.(rec, q_new, indeg_new, processed + 1)
        end
      end

      {cnt, _} = process.(process, queue, indeg, 0)
      cnt == length(nodes)
    end

    # Find minimal masks that are feasible
    {min_dup, result_masks} =
      Enum.reduce(0..(total_masks - 1), {nil, []}, fn mask,
                                                    {cur_min, cur_res} ->
        if feasible.(mask) do
          d = popcnt.(mask)

          cond do
            cur_min == nil or d < cur_min -> {d, [mask]}
            d == cur_min -> {cur_min, [mask | cur_res]}
            true -> {cur_min, cur_res}
          end
        else
          {cur_min, cur_res}
        end
      end)

    # Build frequency vectors for each resulting mask
    Enum.map(result_masks, fn mask ->
      freq = List.duplicate(0, 26)

      Enum.each(chars, fn c ->
        idx = char_to_idx[c]
        count = if (mask &&& (1 <<< idx)) != 0, do: 2, else: 1
        pos = :binary.first(c) - ?a
        List.replace_at(freq, pos, count)
      end)
    end)
  end
end
```
