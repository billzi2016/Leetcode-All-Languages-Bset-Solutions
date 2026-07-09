# 3485. Longest Common Prefix of K Strings After Removal

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct Node{
        int child[26];
        int cnt;
        int depth;
        int parent;
        Node(int d=0,int p=-1):cnt(0),depth(d),parent(p){
            fill(begin(child), end(child), -1);
        }
    };
    
    vector<int> longestCommonPrefix(vector<string>& words, int k) {
        int n = words.size();
        if (n <= k) return vector<int>(n, 0);
        
        vector<Node> trie;
        trie.emplace_back(0,-1); // root id 0
        
        vector<int> termNode(n);
        for (int i=0;i<n;++i){
            int cur = 0;
            trie[cur].cnt++; // root passes through
            for(char ch: words[i]){
                int idx = ch - 'a';
                if(trie[cur].child[idx]==-1){
                    trie[cur].child[idx] = trie.size();
                    trie.emplace_back(trie[cur].depth+1, cur);
                }
                cur = trie[cur].child[idx];
                trie[cur].cnt++;
            }
            termNode[i]=cur;
        }
        
        int nodeCnt = trie.size();
        int bestBigDepth = -1;
        vector<int> listK; // nodes with cnt == k
        for(int id=0; id<nodeCnt; ++id){
            if(trie[id].cnt >= k+1) bestBigDepth = max(bestBigDepth, trie[id].depth);
            if(trie[id].cnt == k) listK.push_back(id);
        }
        sort(listK.begin(), listK.end(), [&](int a,int b){
            return trie[a].depth > trie[b].depth;
        });
        
        vector<int> mark(nodeCnt, 0);
        vector<int> ans(n,0);
        for(int i=0;i<n;++i){
            int cur = termNode[i];
            while(cur!=-1){
                mark[cur]=i+1;
                cur = trie[cur].parent;
            }
            int candDepth = -1;
            for(int nid: listK){
                if(mark[nid]!=i+1){
                    candDepth = trie[nid].depth;
                    break;
                }
            }
            int best = max(bestBigDepth, candDepth);
            ans[i] = max(0, best);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class Node {
        int[] child = new int[26];
        int cnt;
        int depth;
        Node(int depth) {
            Arrays.fill(child, -1);
            this.depth = depth;
        }
    }

    public int[] longestCommonPrefix(String[] words, int k) {
        int n = words.length;
        if (n - 1 < k) {
            return new int[n]; // all zeros
        }

        List<Node> nodes = new ArrayList<>();
        nodes.add(new Node(0)); // root at index 0

        // store path of node indices for each word
        int[][] paths = new int[n][];
        for (int i = 0; i < n; i++) {
            String w = words[i];
            int len = w.length();
            int[] path = new int[len];
            int cur = 0;
            for (int j = 0; j < len; j++) {
                int c = w.charAt(j) - 'a';
                if (nodes.get(cur).child[c] == -1) {
                    nodes.add(new Node(nodes.get(cur).depth + 1));
                    nodes.get(cur).child[c] = nodes.size() - 1;
                }
                cur = nodes.get(cur).child[c];
                nodes.get(cur).cnt++;
                path[j] = cur;
            }
            paths[i] = path;
        }

        TreeSet<Integer> goodDepths = new TreeSet<>();
        for (int idx = 1; idx < nodes.size(); idx++) {
            Node nd = nodes.get(idx);
            if (nd.cnt >= k) {
                goodDepths.add(nd.depth);
            }
        }

        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            // remove word i
            int[] path = paths[i];
            for (int nodeIdx : path) {
                Node nd = nodes.get(nodeIdx);
                if (nd.cnt >= k && nd.cnt - 1 < k) {
                    goodDepths.remove(nd.depth);
                }
                nd.cnt--;
            }

            answer[i] = goodDepths.isEmpty() ? 0 : goodDepths.last();

            // restore word i
            for (int nodeIdx : path) {
                Node nd = nodes.get(nodeIdx);
                if (nd.cnt < k && nd.cnt + 1 >= k) {
                    goodDepths.add(nd.depth);
                }
                nd.cnt++;
            }
        }

        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def longestCommonPrefix(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[int]
        """
        n = len(words)
        if n - 1 < k:
            return [0] * n

        # Trie structures
        children = []          # list of dicts
        cnt = []               # count of strings passing through node
        depth = []             # depth of node (root depth 0)

        # root
        children.append({})
        cnt.append(0)
        depth.append(0)

        paths = []   # per word, list of node ids along its path

        for w in words:
            cur = 0
            path = []
            for ch in w:
                nxt = children[cur].get(ch)
                if nxt is None:
                    nxt = len(children)
                    children[cur][ch] = nxt
                    children.append({})
                    cnt.append(0)
                    depth.append(depth[cur] + 1)
                cur = nxt
                cnt[cur] += 1
                path.append(cur)
            paths.append(path)

        max_depth = max(depth) if len(depth) > 1 else 0

        # per depth statistics
        max1_cnt = [0] * (max_depth + 1)
        max1_node = [-1] * (max_depth + 1)
        max1_freq = [0] * (max_depth + 1)
        max2_cnt = [0] * (max_depth + 1)

        for node_id in range(1, len(children)):
            d = depth[node_id]
            c = cnt[node_id]
            if c > max1_cnt[d]:
                max2_cnt[d] = max1_cnt[d]
                max1_cnt[d] = c
                max1_node[d] = node_id
                max1_freq[d] = 1
            elif c == max1_cnt[d]:
                max1_freq[d] += 1
            elif c > max2_cnt[d]:
                max2_cnt[d] = c

        # original deepest depth with count >= k
        orig_best = 0
        for d in range(1, max_depth + 1):
            if max1_cnt[d] >= k and d > orig_best:
                orig_best = d

        res = [0] * n
        for i, w in enumerate(words):
            L = len(w)
            if orig_best > L:
                res[i] = orig_best
                continue
            best = 0
            path = paths[i]
            # iterate depths up to L
            for idx, node_id in enumerate(path):
                d = idx + 1
                if max1_node[d] == node_id and max1_freq[d] == 1:
                    eff = max(max2_cnt[d], max1_cnt[d] - 1)
                else:
                    eff = max1_cnt[d]
                if eff >= k:
                    best = d
            res[i] = best
        return res
```

## Python3

```python
import sys
from typing import List

class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        n = len(words)
        if n <= k:
            return [0] * n

        # Build trie with counts of strings passing each node
        nodes = [{'cnt': 0, 'depth': 0, 'children': {}}]  # root at index 0

        for w in words:
            cur = 0
            for ch in w:
                nxt = nodes[cur]['children'].get(ch)
                if nxt is None:
                    nodes.append({'cnt': 0,
                                  'depth': nodes[cur]['depth'] + 1,
                                  'children': {}})
                    nxt = len(nodes) - 1
                    nodes[cur]['children'][ch] = nxt
                cur = nxt
                nodes[cur]['cnt'] += 1

        max_len = max(len(w) for w in words)
        qual_by_depth = [[] for _ in range(max_len + 1)]

        for nid, node in enumerate(nodes):
            if node['cnt'] >= k:
                d = node['depth']
                qual_by_depth[d].append(nid)

        base_max = 0
        for d in range(max_len, -1, -1):
            if qual_by_depth[d]:
                base_max = d
                break

        critical_node_at_depth = [-1] * (max_len + 1)
        for d in range(1, max_len + 1):
            lst = qual_by_depth[d]
            if len(lst) == 1:
                nid = lst[0]
                if nodes[nid]['cnt'] == k:   # only exact k becomes invalid after removal
                    critical_node_at_depth[d] = nid

        ans = [0] * n
        for i, w in enumerate(words):
            cur = 0
            critical_set = set()
            for ch in w:
                cur = nodes[cur]['children'][ch]
                d = nodes[cur]['depth']
                if critical_node_at_depth[d] == cur:
                    critical_set.add(d)
            cur_ans = base_max
            while cur_ans > 0 and cur_ans in critical_set:
                cur_ans -= 1
            ans[i] = cur_ans

        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int cnt;
    int depth;
    struct Node *child[26];
} Node;

int* longestCommonPrefix(char** words, int wordsSize, int k, int* returnSize) {
    *returnSize = wordsSize;
    int *ans = (int*)malloc(sizeof(int) * wordsSize);
    if (!ans) return NULL;

    if (wordsSize - 1 < k) {               // not enough strings after any removal
        for (int i = 0; i < wordsSize; ++i) ans[i] = 0;
        return ans;
    }

    /* compute total characters to allocate trie nodes */
    int totalLen = 0, maxDepthSeen = 0;
    for (int i = 0; i < wordsSize; ++i) totalLen += (int)strlen(words[i]);

    Node *pool = (Node*)malloc(sizeof(Node) * (totalLen + 5));
    int poolIdx = 0;

    /* initialize root */
    Node *root = &pool[poolIdx++];
    memset(root, 0, sizeof(Node));
    root->depth = 0;
    root->cnt = wordsSize;   // all strings pass through root

    /* build trie and count prefixes */
    for (int i = 0; i < wordsSize; ++i) {
        const char *s = words[i];
        Node *cur = root;
        while (*s) {
            int idx = *s - 'a';
            if (!cur->child[idx]) {
                Node *newNode = &pool[poolIdx++];
                memset(newNode, 0, sizeof(Node));
                newNode->depth = cur->depth + 1;
                cur->child[idx] = newNode;
                if (newNode->depth > maxDepthSeen) maxDepthSeen = newNode->depth;
            }
            cur = cur->child[idx];
            cur->cnt++;
            s++;
        }
    }

    /* frequency array for depths where cnt >= k */
    int *freq = (int*)calloc(maxDepthSeen + 2, sizeof(int));
    int curMax = -1;

    for (int i = 0; i < poolIdx; ++i) {
        Node *node = &pool[i];
        if (node->cnt >= k) {
            freq[node->depth]++;
            if (node->depth > curMax) curMax = node->depth;
        }
    }

    /* process each removal */
    for (int i = 0; i < wordsSize; ++i) {
        const char *s = words[i];
        Node *cur = root;

        /* handle root */
        if (root->cnt == k) {               // will drop below k
            freq[0]--;
        }
        root->cnt--;

        if (freq[curMax] == 0) {
            while (curMax >= 0 && freq[curMax] == 0) curMax--;
        }

        /* traverse word, decrement counts */
        while (*s) {
            int idx = *s - 'a';
            cur = cur->child[idx];
            if (cur->cnt == k) {            // will become k-1
                freq[cur->depth]--;
            }
            cur->cnt--;
            s++;
        }

        if (freq[curMax] == 0) {
            while (curMax >= 0 && freq[curMax] == 0) curMax--;
        }

        ans[i] = curMax;    // longest common prefix length after removal

        /* restore counts */
        s = words[i];
        cur = root;
        if (root->cnt == k - 1) {           // will become k again
            freq[0]++;
            if (0 > curMax) curMax = 0;
        }
        root->cnt++;

        while (*s) {
            int idx = *s - 'a';
            cur = cur->child[idx];
            if (cur->cnt == k - 1) {        // will become k
                freq[cur->depth]++;
                if (cur->depth > curMax) curMax = cur->depth;
            }
            cur->cnt++;
            s++;
        }
    }

    free(pool);
    free(freq);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private class Node {
        public int[] Next = new int[26];
        public int Count;
        public int Depth;
        public Node(int depth) {
            Depth = depth;
            for (int i = 0; i < 26; i++) Next[i] = -1;
        }
    }

    private class Fenwick {
        private readonly int[] bit;
        private readonly int n;
        public Fenwick(int size) {
            n = size;
            bit = new int[n + 2];
        }
        public void Add(int idx, int delta) {
            for (int i = idx; i <= n; i += i & -i) bit[i] += delta;
        }
        // returns the largest index with prefix sum > 0, or 0 if none
        public int MaxPositive() {
            int idx = 0;
            int mask = 1;
            while ((mask << 1) <= n) mask <<= 1;
            int sum = 0;
            for (int step = mask; step > 0; step >>= 1) {
                int next = idx + step;
                if (next <= n && bit[next] + sum > 0) {
                    idx = next;
                    sum += bit[next];
                }
            }
            return idx;
        }
    }

    public int[] LongestCommonPrefix(string[] words, int k) {
        int n = words.Length;
        int[] answer = new int[n];

        if (n - 1 < k) {
            // removing any word leaves fewer than k strings
            return answer; // all zeros
        }

        List<Node> nodes = new List<Node>();
        nodes.Add(new Node(0)); // root at index 0

        // Build trie and count prefixes
        foreach (var w in words) {
            int cur = 0;
            foreach (char ch in w) {
                int c = ch - 'a';
                if (nodes[cur].Next[c] == -1) {
                    nodes[cur].Next[c] = nodes.Count;
                    nodes.Add(new Node(nodes[cur].Depth + 1));
                }
                cur = nodes[cur].Next[c];
                nodes[cur].Count++;
            }
        }

        // Determine maximum depth to size BIT
        int maxDepth = 0;
        foreach (var node in nodes) if (node.Depth > maxDepth) maxDepth = node.Depth;

        Fenwick bit = new Fenwick(maxDepth);

        // Initialize BIT with nodes whose count >= k
        for (int i = 1; i < nodes.Count; i++) {
            if (nodes[i].Count >= k) {
                bit.Add(nodes[i].Depth, 1);
            }
        }

        // Process each removal
        for (int idx = 0; idx < n; idx++) {
            string w = words[idx];
            int cur = 0;
            // Decrement counts along the path, updating BIT when crossing k -> k-1
            foreach (char ch in w) {
                int c = ch - 'a';
                cur = nodes[cur].Next[c];
                if (nodes[cur].Count == k) {
                    bit.Add(nodes[cur].Depth, -1); // will drop below k
                }
                nodes[cur].Count--;
            }

            // Query current maximum depth with at least k strings sharing prefix
            answer[idx] = bit.MaxPositive();

            // Restore counts along the path, updating BIT when crossing k-1 -> k
            cur = 0;
            foreach (char ch in w) {
                int c = ch - 'a';
                cur = nodes[cur].Next[c];
                if (nodes[cur].Count == k - 1) {
                    // after increment becomes k
                    bit.Add(nodes[cur].Depth, +1);
                }
                nodes[cur].Count++;
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {number} k
 * @return {number[]}
 */
var longestCommonPrefix = function(words, k) {
    const n = words.length;
    if (n - 1 < k) return new Array(n).fill(0);

    // Trie node definition
    function newNode(depth) {
        return { cnt: 0, depth: depth, child: {} };
    }

    const root = newNode(0);
    let maxDepth = 0;

    // Build trie and count passes
    for (const w of words) {
        let node = root;
        for (let i = 0; i < w.length; ++i) {
            const idx = w.charCodeAt(i) - 97;
            if (!node.child[idx]) node.child[idx] = newNode(node.depth + 1);
            node = node.child[idx];
            node.cnt++;
            if (node.depth > maxDepth) maxDepth = node.depth;
        }
    }

    // depthGoodCount[depth] = number of nodes at this depth with cnt >= k
    const depthGoodCount = new Array(maxDepth + 1).fill(0);

    // Max-heap for depths that currently have good nodes (lazy deletion)
    const heap = [];
    function heapPush(val) {
        heap.push(val);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p] >= heap[i]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    }
    function heapPop() {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let l = i * 2 + 1, r = l + 1, largest = i;
                if (l < heap.length && heap[l] > heap[largest]) largest = l;
                if (r < heap.length && heap[r] > heap[largest]) largest = r;
                if (largest === i) break;
                [heap[i], heap[largest]] = [heap[largest], heap[i]];
                i = largest;
            }
        }
        return top;
    }
    function heapPeek() { return heap[0]; }

    // Initialize depthGoodCount and heap
    const stack = [root];
    while (stack.length) {
        const node = stack.pop();
        if (node.depth > 0 && node.cnt >= k) {
            depthGoodCount[node.depth]++;
            heapPush(node.depth);
        }
        for (const child of Object.values(node.child)) stack.push(child);
    }

    const ans = new Array(n);

    // Process each removal
    for (let i = 0; i < n; ++i) {
        const w = words[i];
        let node = root;
        // Decrement counts along the path
        for (let j = 0; j < w.length; ++j) {
            const idx = w.charCodeAt(j) - 97;
            node = node.child[idx];
            if (node.cnt === k) { // will drop below k
                depthGoodCount[node.depth]--;
            }
            node.cnt--;
        }

        // Clean heap top if stale
        while (heap.length && depthGoodCount[heapPeek()] === 0) {
            heapPop();
        }
        ans[i] = heap.length ? heapPeek() : 0;

        // Add the word back
        node = root;
        for (let j = 0; j < w.length; ++j) {
            const idx = w.charCodeAt(j) - 97;
            node = node.child[idx];
            node.cnt++;
            if (node.cnt === k) { // just reached threshold
                depthGoodCount[node.depth]++;
                heapPush(node.depth);
            }
        }
    }

    return ans;
};
```

## Typescript

```typescript
function longestCommonPrefix(words: string[], k: number): number[] {
    const n = words.length;

    // Trie structures
    const nodeDepth: number[] = [];
    const cntArr: number[] = [];
    const childrenArr: { [key: string]: number }[] = [];

    function newNode(depth: number): number {
        const idx = nodeDepth.length;
        nodeDepth.push(depth);
        cntArr.push(0);
        childrenArr.push(Object.create(null));
        return idx;
    }

    const root = newNode(0);

    // Build trie and count passes
    for (const w of words) {
        let cur = root;
        for (let i = 0; i < w.length; ++i) {
            const ch = w.charCodeAt(i);
            const key = String.fromCharCode(ch);
            let child = childrenArr[cur][key];
            if (child === undefined) {
                child = newNode(nodeDepth[cur] + 1);
                childrenArr[cur][key] = child;
            }
            cur = child;
            cntArr[cur]++;
        }
    }

    // Determine max depth
    let maxDepth = 0;
    for (const d of nodeDepth) if (d > maxDepth) maxDepth = d;

    const depthCnt = new Int32Array(maxDepth + 1);
    for (let i = 0; i < nodeDepth.length; ++i) {
        const d = nodeDepth[i];
        if (d === 0) continue;
        if (cntArr[i] >= k) depthCnt[d]++;
    }

    // Segment tree for max depth with positive count
    let size = 1;
    while (size < maxDepth + 1) size <<= 1;
    const seg = new Int32Array(2 * size);
    for (let d = 0; d <= maxDepth; ++d) {
        seg[size + d] = depthCnt[d] > 0 ? d : 0;
    }
    for (let i = size - 1; i > 0; --i) {
        const left = seg[i << 1];
        const right = seg[(i << 1) | 1];
        seg[i] = left > right ? left : right;
    }

    function segUpdate(pos: number, delta: number): void {
        depthCnt[pos] += delta;
        let idx = size + pos;
        seg[idx] = depthCnt[pos] > 0 ? pos : 0;
        idx >>= 1;
        while (idx) {
            const left = seg[idx << 1];
            const right = seg[(idx << 1) | 1];
            const val = left > right ? left : right;
            if (seg[idx] === val) break;
            seg[idx] = val;
            idx >>= 1;
        }
    }

    function getMax(): number {
        return seg[1];
    }

    // Modify counts along a word's path
    function modify(word: string, delta: number): void {
        let cur = root;
        for (let i = 0; i < word.length; ++i) {
            const ch = word.charCodeAt(i);
            const key = String.fromCharCode(ch);
            const child = childrenArr[cur][key];
            if (child === undefined) continue; // safety
            const before = cntArr[child];
            const after = before + delta;

            if (before >= k && after < k) {
                segUpdate(nodeDepth[child], -1);
            } else if (before < k && after >= k) {
                segUpdate(nodeDepth[child], 1);
            }

            cntArr[child] = after;
            cur = child;
        }
    }

    const ans: number[] = new Array(n);
    for (let i = 0; i < n; ++i) {
        modify(words[i], -1);      // remove
        ans[i] = getMax();         // query
        modify(words[i], 1);       // restore
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $words
     * @param Integer $k
     * @return Integer[]
     */
    function longestCommonPrefix($words, $k) {
        $n = count($words);
        if ($n - 1 < $k) {
            return array_fill(0, $n, 0);
        }

        // Trie structures
        $children = [];
        $cnt = [];
        $depth = [];

        // root node
        $children[0] = array_fill(0, 26, -1);
        $cnt[0] = 0;
        $depth[0] = 0;

        $paths = []; // store node ids for each word

        // Build trie and record paths
        for ($i = 0; $i < $n; $i++) {
            $word = $words[$i];
            $cur = 0;
            $len = strlen($word);
            $path = [];
            for ($j = 0; $j < $len; $j++) {
                $cIdx = ord($word[$j]) - 97;
                if ($children[$cur][$cIdx] == -1) {
                    $newId = count($children);
                    $children[$cur][$cIdx] = $newId;
                    $children[$newId] = array_fill(0, 26, -1);
                    $cnt[$newId] = 0;
                    $depth[$newId] = $depth[$cur] + 1;
                }
                $cur = $children[$cur][$cIdx];
                $cnt[$cur]++;               // increase prefix count
                $path[] = $cur;             // record node for this character
            }
            $paths[$i] = $path;
        }

        // Initialize qualified depths where cnt >= k
        $qualified = [];   // depth => number of nodes with cnt>=k
        $maxDepth = 0;
        $totalNodes = count($children);
        for ($id = 1; $id < $totalNodes; $id++) {
            if ($cnt[$id] >= $k) {
                $d = $depth[$id];
                $qualified[$d] = ($qualified[$d] ?? 0) + 1;
                if ($d > $maxDepth) $maxDepth = $d;
            }
        }

        $ans = array_fill(0, $n, 0);

        // Process each removal
        for ($i = 0; $i < $n; $i++) {
            // remove word i
            foreach ($paths[$i] as $nodeId) {
                $old = $cnt[$nodeId];
                $new = $old - 1;
                $cnt[$nodeId] = $new;
                $d = $depth[$nodeId];
                if ($old >= $k && $new < $k) {
                    $qualified[$d]--;
                    if ($d == $maxDepth && $qualified[$d] == 0) {
                        while ($maxDepth > 0 && (!isset($qualified[$maxDepth]) || $qualified[$maxDepth] == 0)) {
                            $maxDepth--;
                        }
                    }
                }
            }

            $ans[$i] = $maxDepth;

            // restore word i
            foreach ($paths[$i] as $nodeId) {
                $old = $cnt[$nodeId];
                $new = $old + 1;
                $cnt[$nodeId] = $new;
                $d = $depth[$nodeId];
                if ($old < $k && $new >= $k) {
                    $qualified[$d] = ($qualified[$d] ?? 0) + 1;
                    if ($d > $maxDepth) $maxDepth = $d;
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func longestCommonPrefix(_ words: [String], _ k: Int) -> [Int] {
        // Trie node definition
        final class Node {
            var child: [Int]
            var cnt: Int = 0
            let depth: Int
            init(depth: Int) {
                self.depth = depth
                self.child = Array(repeating: -1, count: 26)
            }
        }

        // Build trie and count passes
        var trie: [Node] = [Node(depth: 0)]   // root at index 0
        for (idx, word) in words.enumerated() {
            var cur = 0
            for byte in word.utf8 {
                let c = Int(byte - 97)
                if trie[cur].child[c] == -1 {
                    let newNode = Node(depth: trie[cur].depth + 1)
                    trie.append(newNode)
                    trie[cur].child[c] = trie.count - 1
                }
                cur = trie[cur].child[c]
                trie[cur].cnt += 1
            }
        }

        // Determine strong nodes and weak depth statistics
        var maxStrongDepth = -1
        var depthWeakCount: [Int:Int] = [:]   // depth -> number of weak nodes (cnt == k)
        var weakDepthsSet = Set<Int>()
        for node in trie where node.depth > 0 {
            if node.cnt >= k + 1 {
                if node.depth > maxStrongDepth { maxStrongDepth = node.depth }
            } else if node.cnt == k {
                depthWeakCount[node.depth, default: 0] += 1
                weakDepthsSet.insert(node.depth)
            }
        }

        // If any strong node exists, answer is its deepest depth for all indices
        if maxStrongDepth != -1 {
            return Array(repeating: maxStrongDepth, count: words.count)
        }

        // No strong nodes
        if weakDepthsSet.isEmpty {
            return Array(repeating: 0, count: words.count)
        }

        // Check if any depth has at least two weak nodes (always survives removal)
        var maxDepthMulti = -1
        for (d, cnt) in depthWeakCount where cnt >= 2 {
            if d > maxDepthMulti { maxDepthMulti = d }
        }
        if maxDepthMulti != -1 {
            return Array(repeating: maxDepthMulti, count: words.count)
        }

        // All weak depths have exactly one node
        let weakDepthsDesc = weakDepthsSet.sorted(by: >)   // descending
        var nextDepthMap: [Int:Int] = [:]
        for i in 0..<(weakDepthsDesc.count - 1) {
            nextDepthMap[weakDepthsDesc[i]] = weakDepthsDesc[i + 1]
        }
        nextDepthMap[weakDepthsDesc.last!] = -1
        let overallMaxWeakDepth = weakDepthsDesc.first!

        // Compute answer for each word
        var result = [Int](repeating: 0, count: words.count)
        for (idx, word) in words.enumerated() {
            var cur = 0
            var blocked = Set<Int>()
            for byte in word.utf8 {
                let c = Int(byte - 97)
                cur = trie[cur].child[c]
                if trie[cur].cnt == k {   // this node is a weak node
                    blocked.insert(trie[cur].depth)
                }
            }
            var d = overallMaxWeakDepth
            while d != -1 && blocked.contains(d) {
                d = nextDepthMap[d] ?? -1
            }
            result[idx] = (d == -1) ? 0 : d
        }
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.TreeSet

class Solution {
    private class Node(val depth: Int) {
        val child = IntArray(26) { -1 }
        var cnt: Int = 0
    }

    fun longestCommonPrefix(words: Array<String>, k: Int): IntArray {
        if (words.isEmpty()) return intArrayOf()
        // Build trie
        val nodes = mutableListOf<Node>()
        nodes.add(Node(0)) // root at index 0
        var maxDepth = 0
        for (w in words) {
            var cur = 0
            nodes[cur].cnt++
            for (ch in w) {
                val c = ch - 'a'
                var nxt = nodes[cur].child[c]
                if (nxt == -1) {
                    nxt = nodes.size
                    nodes.add(Node(nodes[cur].depth + 1))
                    nodes[cur].child[c] = nxt
                }
                cur = nxt
                nodes[cur].cnt++
            }
            if (nodes[cur].depth > maxDepth) maxDepth = nodes[cur].depth
        }

        // Frequency per depth for nodes with cnt >= k
        val freq = IntArray(maxDepth + 1)
        val depthsSet = TreeSet<Int>()
        for (node in nodes) {
            if (node.cnt >= k) {
                freq[node.depth]++
                depthsSet.add(node.depth)
            }
        }

        val n = words.size
        val answer = IntArray(n)

        for (i in 0 until n) {
            val w = words[i]
            // collect path indices including root
            val path = IntArray(w.length + 1)
            var pos = 0
            var cur = 0
            path[pos++] = cur
            for (ch in w) {
                val c = ch - 'a'
                cur = nodes[cur].child[c]
                path[pos++] = cur
            }

            // remove word i
            for (j in 0 until pos) {
                val nodeIdx = path[j]
                val node = nodes[nodeIdx]
                if (node.cnt == k) {
                    freq[node.depth]--
                    if (freq[node.depth] == 0) depthsSet.remove(node.depth)
                }
                node.cnt--
            }

            // compute answer after removal
            answer[i] = if (depthsSet.isEmpty()) 0 else depthsSet.last()

            // add word i back
            for (j in 0 until pos) {
                val nodeIdx = path[j]
                val node = nodes[nodeIdx]
                node.cnt++
                if (node.cnt == k) {
                    freq[node.depth]++
                    if (freq[node.depth] == 1) depthsSet.add(node.depth)
                }
            }
        }

        return answer
    }
}
```

## Dart

```dart
import 'dart:collection';

class Node {
  List<int> child = List.filled(26, -1);
  int cnt = 0;
  final int depth;
  Node(this.depth);
}

class Solution {
  List<int> longestCommonPrefix(List<String> words, int k) {
    // Build trie
    List<Node> nodes = [Node(0)];
    for (String w in words) {
      int cur = 0;
      nodes[cur].cnt++;
      for (int i = 0; i < w.length; i++) {
        int idx = w.codeUnitAt(i) - 97;
        if (nodes[cur].child[idx] == -1) {
          nodes.add(Node(nodes[cur].depth + 1));
          nodes[cur].child[idx] = nodes.length - 1;
        }
        cur = nodes[cur].child[idx];
        nodes[cur].cnt++;
      }
    }

    // Data structures to maintain depths with count >= k
    final Map<int, int> depthCount = {};
    final SplayTreeSet<int> eligibleDepths = SplayTreeSet<int>();

    void addDepth(int d) {
      depthCount[d] = (depthCount[d] ?? 0) + 1;
      eligibleDepths.add(d);
    }

    void removeDepth(int d) {
      int newVal = (depthCount[d] ?? 0) - 1;
      if (newVal == 0) {
        depthCount.remove(d);
        eligibleDepths.remove(d);
      } else {
        depthCount[d] = newVal;
      }
    }

    // Initialize eligible depths
    for (int i = 0; i < nodes.length; i++) {
      if (nodes[i].cnt >= k) addDepth(nodes[i].depth);
    }

    void adjust(int nodeIdx, int delta) {
      Node node = nodes[nodeIdx];
      bool wasEligible = node.cnt >= k;
      node.cnt += delta;
      bool nowEligible = node.cnt >= k;
      if (wasEligible != nowEligible) {
        if (nowEligible) {
          addDepth(node.depth);
        } else {
          removeDepth(node.depth);
        }
      }
    }

    int n = words.length;
    List<int> answer = List.filled(n, 0);

    for (int i = 0; i < n; i++) {
      // Remove word i
      adjust(0, -1);
      int cur = 0;
      String w = words[i];
      for (int j = 0; j < w.length; j++) {
        int idx = w.codeUnitAt(j) - 97;
        cur = nodes[cur].child[idx];
        adjust(cur, -1);
      }

      // Record answer
      answer[i] = eligibleDepths.isEmpty ? 0 : eligibleDepths.last;

      // Restore word i
      adjust(0, +1);
      cur = 0;
      for (int j = 0; j < w.length; j++) {
        int idx = w.codeUnitAt(j) - 97;
        cur = nodes[cur].child[idx];
        adjust(cur, +1);
      }
    }

    return answer;
  }
}
```

## Golang

```go
func longestCommonPrefix(words []string, k int) []int {
	type Node struct {
		child   [26]int
		cnt     int
		depth   int
	}
	n := len(words)
	if n == 0 {
		return []int{}
	}

	// Build trie and store path for each word
	nodes := make([]Node, 1) // root at index 0
	paths := make([][]int, n)

	maxDepth := 0
	for i, w := range words {
		cur := 0
		path := make([]int, len(w))
		for j, ch := range w {
			idx := int(ch - 'a')
			if nodes[cur].child[idx] == 0 {
				nodes = append(nodes, Node{depth: nodes[cur].depth + 1})
				nodes[cur].child[idx] = len(nodes) - 1
			}
			cur = nodes[cur].child[idx]
			nodes[cur].cnt++
			path[j] = cur
		}
		paths[i] = path
		if len(w) > maxDepth {
			maxDepth = len(w)
		}
	}

	// tot[depth] = number of nodes with cnt >= k at that depth
	tot := make([]int, maxDepth+1) // 0..maxDepth
	isCritical := make([]bool, len(nodes))

	for i := 1; i < len(nodes); i++ { // skip root
		if nodes[i].cnt >= k {
			d := nodes[i].depth
			tot[d]++
		}
		if nodes[i].cnt == k {
			isCritical[i] = true
		}
	}

	// global deepest depth with tot>0
	D0 := 0
	for d := maxDepth; d >= 1; d-- {
		if tot[d] > 0 {
			D0 = d
			break
		}
	}

	ans := make([]int, n)
	for i := 0; i < n; i++ {
		cur := D0
		path := paths[i]
		plen := len(path)
		for cur > 0 {
			if cur <= plen {
				nodeID := path[cur-1]
				if isCritical[nodeID] && tot[cur] == 1 {
					cur--
					continue
				}
			}
			// either depth not on this word or node not critical or multiple nodes at this depth
			break
		}
		ans[i] = cur
	}
	return ans
}
```

## Ruby

```ruby
def longest_common_prefix(words, k)
  n = words.length
  # Build trie
  nodes = [{cnt: 0, depth: 0, children: {}}] # root at index 0
  paths = Array.new(n) { [] }

  words.each_with_index do |word, idx|
    cur = 0
    nodes[cur][:cnt] += 1
    paths[idx] << cur
    word.each_char do |ch|
      child = nodes[cur][:children][ch]
      unless child
        child_id = nodes.length
        nodes << {cnt: 0, depth: nodes[cur][:depth] + 1, children: {}}
        nodes[cur][:children][ch] = child_id
        child = child_id
      end
      cur = child
      nodes[cur][:cnt] += 1
      paths[idx] << cur
    end
  end

  max_depth = nodes.map { |node| node[:depth] }.max
  good = Array.new(max_depth + 1, 0)
  nodes.each do |node|
    good[node[:depth]] += 1 if node[:cnt] >= k
  end

  # Build segment tree for maximum depth with good[depth] > 0
  size = 1
  while size < max_depth + 1
    size <<= 1
  end
  seg = Array.new(2 * size, -1)
  (0..max_depth).each do |d|
    seg[size + d] = good[d] > 0 ? d : -1
  end
  (size - 1).downto(1) { |i| seg[i] = [seg[i << 1], seg[(i << 1) + 1]].max }

  update = lambda do |depth|
    pos = size + depth
    seg[pos] = good[depth] > 0 ? depth : -1
    pos >>= 1
    while pos > 0
      new_val = [seg[pos << 1], seg[(pos << 1) + 1]].max
      break if seg[pos] == new_val
      seg[pos] = new_val
      pos >>= 1
    end
  end

  answer = Array.new(n, 0)

  n.times do |i|
    # apply removal effects
    paths[i].each do |node_id|
      d = nodes[node_id][:depth]
      if nodes[node_id][:cnt] == k
        good[d] -= 1
        update.call(d)
      end
    end

    max_d = seg[1]
    answer[i] = max_d < 0 ? 0 : max_d

    # revert removal effects
    paths[i].each do |node_id|
      d = nodes[node_id][:depth]
      if nodes[node_id][:cnt] == k
        good[d] += 1
        update.call(d)
      end
    end
  end

  answer
end
```

## Scala

```scala
object Solution {
    def longestCommonPrefix(words: Array[String], k: Int): Array[Int] = {
        val n = words.length
        if (n == 0) return Array.emptyIntArray
        // total characters to allocate trie nodes
        var totalChars = 0
        var i = 0
        while (i < n) {
            totalChars += words(i).length
            i += 1
        }
        val maxNodes = totalChars + 1 // include root
        val child = Array.ofDim[Int](maxNodes, 26)
        var nodeIdx = 0
        while (nodeIdx < maxNodes) {
            java.util.Arrays.fill(child(nodeIdx), -1)
            nodeIdx += 1
        }
        val cnt = new Array[Int](maxNodes)
        val depthArr = new Array[Int](maxNodes)

        // store path nodes for each word
        val paths = new Array[Array[Int]](n)

        var nextId = 1 // root is 0
        i = 0
        while (i < n) {
            val w = words(i)
            var cur = 0
            val buf = scala.collection.mutable.ArrayBuffer.empty[Int]
            var j = 0
            while (j < w.length) {
                val cIdx = w.charAt(j) - 'a'
                if (child(cur)(cIdx) == -1) {
                    child(cur)(cIdx) = nextId
                    depthArr(nextId) = depthArr(cur) + 1
                    nextId += 1
                }
                cur = child(cur)(cIdx)
                cnt(cur) += 1
                buf.append(cur)
                j += 1
            }
            paths(i) = buf.toArray
            i += 1
        }
        // root count is total number of strings
        cnt(0) = n

        // compute max depth where cnt >= k
        var maxDepth = 0
        var id = 0
        while (id < nextId) {
            if (cnt(id) >= k && depthArr(id) > maxDepth) maxDepth = depthArr(id)
            id += 1
        }

        val goodCountByDepth = new Array[Int](maxDepth + 1)
        val uniqueNodeAtDepth = new Array[Int](maxDepth + 1).map(_ => -1)

        id = 0
        while (id < nextId) {
            if (cnt(id) >= k) {
                val d = depthArr(id)
                goodCountByDepth(d) += 1
            }
            id += 1
        }

        id = 0
        while (id < nextId) {
            if (cnt(id) >= k) {
                val d = depthArr(id)
                if (goodCountByDepth(d) == 1) uniqueNodeAtDepth(d) = id
            }
            id += 1
        }

        // candidate depths descending where there is at least one good node
        val candBuf = scala.collection.mutable.ArrayBuffer.empty[Int]
        var d = maxDepth
        while (d >= 0) {
            if (goodCountByDepth(d) > 0) candBuf.append(d)
            d -= 1
        }
        val candidateDepths = candBuf.toArray

        val answer = new Array[Int](n)

        // if after removal we have fewer than k strings, all answers are 0
        if (n - 1 < k) {
            java.util.Arrays.fill(answer, 0)
            return answer
        }

        i = 0
        while (i < n) {
            val path = paths(i)
            var dOn = 0
            var idx = 0
            while (idx < path.length) {
                val nodeId = path(idx)
                if (cnt(nodeId) >= k + 1) {
                    val dep = depthArr(nodeId)
                    if (dep > dOn) dOn = dep
                }
                idx += 1
            }

            // build a hash set of nodes on this word's path for O(1) membership checks
            val nodeSet = new java.util.HashSet[Int]()
            idx = 0
            while (idx < path.length) {
                nodeSet.add(path(idx))
                idx += 1
            }

            var ans = dOn
            var found = false
            var cIdx = 0
            while (cIdx < candidateDepths.length && !found) {
                val curDepth = candidateDepths(cIdx)
                if (curDepth <= ans) {
                    // no deeper depth possible
                    cIdx = candidateDepths.length
                } else {
                    var ok = true
                    if (goodCountByDepth(curDepth) == 1) {
                        val nodeId = uniqueNodeAtDepth(curDepth)
                        if (cnt(nodeId) == k && nodeSet.contains(nodeId)) {
                            ok = false
                        }
                    }
                    if (ok) {
                        ans = curDepth
                        found = true
                    } else {
                        cIdx += 1
                    }
                }
            }

            answer(i) = ans
            i += 1
        }

        answer
    }
}
```

## Rust

```rust
use std::cmp::max;

struct Node {
    children: [i32; 26],
    cnt: i32,
    depth: i32,
}

impl Solution {
    pub fn longest_common_prefix(words: Vec<String>, k: i32) -> Vec<i32> {
        let n = words.len() as i32;
        if n - 1 < k {
            return vec![0; words.len()];
        }

        // Build trie
        let mut nodes: Vec<Node> = Vec::new();
        nodes.push(Node {
            children: [-1; 26],
            cnt: 0,
            depth: 0,
        });

        for w in &words {
            let bytes = w.as_bytes();
            let mut cur = 0usize;
            for &b in bytes {
                let idx = (b - b'a') as usize;
                if nodes[cur].children[idx] == -1 {
                    let new_id = nodes.len();
                    nodes.push(Node {
                        children: [-1; 26],
                        cnt: 0,
                        depth: nodes[cur].depth + 1,
                    });
                    nodes[cur].children[idx] = new_id as i32;
                }
                cur = nodes[cur].children[idx] as usize;
                nodes[cur].cnt += 1;
            }
        }

        // Global max depth with cnt > k and collect nodes with cnt == k
        let mut global_max_gt_k: i32 = 0;
        let mut eq_nodes: Vec<usize> = Vec::new();
        for (id, node) in nodes.iter().enumerate() {
            if id == 0 {
                continue;
            }
            if node.cnt > k {
                if node.depth > global_max_gt_k {
                    global_max_gt_k = node.depth;
                }
            } else if node.cnt == k {
                eq_nodes.push(id);
            }
        }

        // Sort eq nodes by depth descending
        eq_nodes.sort_by_key(|&id| -nodes[id].depth);

        let mut stamp: Vec<u32> = vec![0; nodes.len()];
        let mut cur_version: u32 = 1;
        let mut answer: Vec<i32> = Vec::with_capacity(words.len());

        for w in &words {
            // mark path of current word
            let bytes = w.as_bytes();
            let mut cur = 0usize;
            for &b in bytes {
                let idx = (b - b'a') as usize;
                cur = nodes[cur].children[idx] as usize;
                stamp[cur] = cur_version;
            }

            // find deepest node with cnt == k not on path
            let mut best_eq: i32 = 0;
            for &nid in &eq_nodes {
                if stamp[nid] != cur_version {
                    best_eq = nodes[nid].depth;
                    break;
                }
            }

            answer.push(max(global_max_gt_k, best_eq));
            cur_version += 1;
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (longest-common-prefix words k)
  (-> (listof string?) exact-integer? (listof exact-integer?))
  (let* ([n (length words)]
         [words-vec (list->vector words)])
    (if (< (- n 1) k)
        (make-list n 0)
        (let* ([total-len (apply + (map string-length words))]
               [max-nodes (+ total-len 1)]
               [nodes (make-vector max-nodes #f)]
               [next-id (box 1)])
          ;; node struct: children hash, cnt int, depth int, qualified? bool
          (struct node (children cnt depth qualified?) #:mutable)
          (vector-set! nodes 0 (node (make-hash) 0 0 #f))
          
          ;; helpers to modify counts and qualification
          (define (inc-cnt! nid heap)
            (let* ([nd (vector-ref nodes nid)]
                   [old (node-cnt nd)])
              (set-node-cnt! nd (+ old 1))
              (when (and (< old k) (>= (+ old 1) k))
                (set-node-qualified! nd #t)
                (heap-push! heap (list (node-depth nd) nid)))))
          (define (dec-cnt! nid)
            (let* ([nd (vector-ref nodes nid)]
                   [old (node-cnt nd)])
              (set-node-cnt! nd (- old 1))
              (when (and (>= old k) (< (- old 1) k))
                (set-node-qualified! nd #f))))
          
          ;; build trie and store paths
          (define paths (make-vector n))
          (for ([i (in-range n)])
            (let* ([word (vector-ref words-vec i)]
                   [len (string-length word)]
                   [path (list 0)]) ; start with root
              (inc-cnt! 0 #f) ; temporary, will adjust later after heap created
              (let loop ((pos 0) (cur 0))
                (if (= pos len)
                    (begin
                      (set! path (reverse path))
                      (vector-set! paths i path))
                    (let* ([c (string-ref word pos)]
                           [children (node-children (vector-ref nodes cur))]
                           [nid (if (hash-has-key? children c)
                                    (hash-ref children c)
                                    (let ([new-id (unbox next-id)])
                                      (set-box! next-id (+ new-id 1))
                                      (hash-set! children c new-id)
                                      (vector-set! nodes new-id
                                                   (node (make-hash) 0 (+ (node-depth (vector-ref nodes cur)) 1) #f))
                                      new-id))])
                      (inc-cnt! nid #f)
                      (loop (+ pos 1) nid)))))))
          
          ;; heap implementation (max-heap by depth)
          (struct heap (vec size) #:mutable)
          (define (make-heap cap)
            (heap (make-vector (+ cap 2) #f) 0))
          (define (heap-size h) (heap-size h))
          (define (set-heap-size! h v) (set-heap-size! h v))
          (define (heap-push! h item)
            (let* ([sz (+ (heap-size h) 1)])
              (vector-set! (heap-vec h) sz item)
              (set-heap-size! h sz)
              (let loop ((i sz))
                (when (> i 1)
                  (define p (quotient i 2))
                  (define cur (vector-ref (heap-vec h) i))
                  (define par (vector-ref (heap-vec h) p))
                  (if (> (first cur) (first par))
                      (begin
                        (vector-set! (heap-vec h) i par)
                        (vector-set! (heap-vec h) p cur)
                        (loop p))
                      (void))))))
          (define (heap-peek h)
            (if (> (heap-size h) 0)
                (vector-ref (heap-vec h) 1)
                #f))
          (define (heap-pop! h)
            (when (> (heap-size h) 0)
              (let* ([sz (heap-size h)]
                     [last (vector-ref (heap-vec h) sz)])
                (if (= sz 1)
                    (set-heap-size! h 0)
                    (begin
                      (vector-set! (heap-vec h) 1 last)
                      (set-heap-size! h (- sz 1))
                      ;; bubble down
                      (let loop ((i 1))
                        (define l (* i 2))
                        (define r (+ l 1))
                        (if (> l (heap-size h))
                            (void)
                            (let* ([largest i]
                                   [left-item (vector-ref (heap-vec h) l)]
                                   [right-item (if (<= r (heap-size h))
                                                   (vector-ref (heap-vec h) r)
                                                   #f)])
                              (when (> (first left-item) (first (vector-ref (heap-vec h) largest)))
                                (set! largest l))
                              (when (and right-item
                                         (> (first right-item) (first (vector-ref (heap-vec h) largest))))
                                (set! largest r))
                              (if (= largest i)
                                  (void)
                                  (begin
                                    (define tmp (vector-ref (heap-vec h) i))
                                    (vector-set! (heap-vec h) i (vector-ref (heap-vec h) largest))
                                    (vector-set! (heap-vec h) largest tmp)
                                    (loop largest)))))))))))
          
          ;; initialize heap with current counts
          (define h (make-heap max-nodes))
          (for ([id (in-range (unbox next-id))])
            (let ([nd (vector-ref nodes id)])
              (when (>= (node-cnt nd) k)
                (set-node-qualified! nd #t)
                (heap-push! h (list (node-depth nd) id)))))
          
          ;; answers vector
          (define ans (make-vector n 0))
          
          (for ([i (in-range n)])
            ;; remove word i
            (for ([nid (in-list (vector-ref paths i))])
              (dec-cnt! nid))
            ;; get current max depth
            (let loop ()
              (if (= (heap-size h) 0)
                  (vector-set! ans i 0)
                  (let* ([top (heap-peek h)]
                         [depth (first top)]
                         [nid (second top)])
                    (if (node-qualified? (vector-ref nodes nid))
                        (vector-set! ans i depth)
                        (begin (heap-pop! h) (loop))))))
            ;; add word i back
            (for ([nid (in-list (vector-ref paths i))])
              (inc-cnt! nid h)))
          
          (vector->list ans))))))
```

## Erlang

```erlang
-spec longest_common_prefix(Words :: [unicode:unicode_binary()], K :: integer()) -> [integer()].
longest_common_prefix(Words, K) ->
    N = length(Words),
    case N - 1 < K of
        true -> lists:duplicate(N, 0);
        false ->
            {PrefixCount0, WordPrefListsRev} = build_prefix_counts(Words, #{}),
            WordPrefLists = lists:reverse(WordPrefListsRev),
            DepthTree0 = init_depth_tree(PrefixCount0, K),
            process_all(WordPrefLists, PrefixCount0, DepthTree0, K, [])
    end.

%% Build prefix count map and store per‑word prefix lists
build_prefix_counts([], PC) -> {PC, []};
build_prefix_counts([W|Rest], PC) ->
    Prefs = gen_prefixes(W),
    PC1 = add_prefixes(Prefs, PC),
    {PC2, Lists} = build_prefix_counts(Rest, PC1),
    {PC2, [Prefs | Lists]}.

%% Increment counts for a list of prefixes
add_prefixes([], PC) -> PC;
add_prefixes([P|Ps], PC) ->
    Cnt = maps:get(P, PC, 0) + 1,
    add_prefixes(Ps, maps:put(P, Cnt, PC)).

%% Generate all non‑empty prefixes of a binary word
gen_prefixes(Word) when is_binary(Word) ->
    Len = byte_size(Word),
    gen_prefixes(Word, Len, 1, []).

gen_prefixes(_Word, _Len, Pos, Acc) when Pos > _Len -> lists:reverse(Acc);
gen_prefixes(Word, Len, Pos, Acc) ->
    Prefix = binary:part(Word, {0, Pos}),
    gen_prefixes(Word, Len, Pos + 1, [Prefix | Acc]).

%% Initialise depth tree with prefixes whose count >= K
init_depth_tree(PrefixCount, K) ->
    init_depth_tree(maps:to_list(PrefixCount), K, gb_trees.empty()).

init_depth_tree([], _K, Tree) -> Tree;
init_depth_tree([{Pref, Cnt} | Rest], K, Tree) ->
    case Cnt >= K of
        true ->
            Len = byte_size(Pref),
            NewTree = case gb_trees:lookup(Len, Tree) of
                {value, V} -> gb_trees:update(Len, V + 1, Tree);
                none       -> gb_trees:insert(Len, 1, Tree)
            end,
            init_depth_tree(Rest, K, NewTree);
        false ->
            init_depth_tree(Rest, K, Tree)
    end.

%% Process each word: remove, record answer, add back
process_all([], _PC, _DT, _K, Acc) -> lists:reverse(Acc);
process_all([PrefList | RestWords], PC, DT, K, Acc) ->
    {PC1, DT1} = update_counts(PrefList, PC, DT, K, -1),
    MaxDepth = case gb_trees:is_empty(DT1) of
        true -> 0;
        false -> {Len, _} = gb_trees:largest(DT1), Len
    end,
    {PC2, DT2} = update_counts(PrefList, PC1, DT1, K, +1),
    process_all(RestWords, PC2, DT2, K, [MaxDepth | Acc]).

%% Update counts for a list of prefixes; Delta is -1 (remove) or +1 (add)
update_counts([], PC, DT, _K, _Delta) -> {PC, DT};
update_counts([P|Ps], PC, DT, K, Delta) ->
    OldCnt = maps:get(P, PC),
    NewCnt = OldCnt + Delta,
    PC1 = case NewCnt of
        0 -> maps:remove(P, PC);
        _ -> maps:put(P, NewCnt, PC)
    end,
    Len = byte_size(P),
    DT1 = case {OldCnt >= K, NewCnt >= K} of
        {true, false} -> % crossed below K
            case gb_trees:lookup(Len, DT) of
                {value, V} when V =:= 1 -> gb_trees:delete(Len, DT);
                {value, V}              -> gb_trees:update(Len, V - 1, DT)
            end;
        {false, true} -> % crossed above K
            case gb_trees:lookup(Len, DT) of
                {value, V} -> gb_trees:update(Len, V + 1, DT);
                none       -> gb_trees:insert(Len, 1, DT)
            end;
        _ -> DT
    end,
    update_counts(Ps, PC1, DT1, K, Delta).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_common_prefix(words :: [String.t()], k :: integer) :: [integer]
  def longest_common_prefix(words, k) do
    n = length(words)

    if n - 1 < k do
      List.duplicate(0, n)
    else
      # Build trie and store path of node ids for each word
      {nodes, paths, _next_id} =
        Enum.reduce(Enum.with_index(words), {%{0 => %{cnt: 0, depth: 0, children: %{}}}, [], 1},
          fn {word, _idx}, {nds, pths, nid} ->
            chars = String.graphemes(word)

            {nds2, path_rev, nid2} =
              Enum.reduce(chars, {nds, [], nid}, fn ch, {nmap, acc_path, next_id} ->
                parent = nmap[0] # placeholder, will be overwritten below
                # find current node (starting from root)
                cur_node = if acc_path == [] do
                  0
                else
                  List.first(acc_path)
                end

                parent = nmap[cur_node]

                child_id =
                  case Map.get(parent.children, ch) do
                    nil ->
                      new_id = next_id
                      new_node = %{cnt: 0, depth: parent.depth + 1, children: %{}}
                      nmap = Map.put(nmap, new_id, new_node)
                      updated_parent = %{parent | children: Map.put(parent.children, ch, new_id)}
                      nmap = Map.put(nmap, cur_node, updated_parent)
                      {nmap, new_id, next_id + 1}

                    existing ->
                      {nmap, existing, next_id}
                  end

                {nmap3, child_id2, nid_next} = child_id

                node = nmap3[child_id2]
                nmap4 = Map.put(nmap3, child_id2, %{node | cnt: node.cnt + 1})

                {nmap4, [child_id2 | acc_path], nid_next}
              end)

            path = Enum.reverse(path_rev)
            {nds2, [path | pths], nid2}
          end)

      paths = Enum.reverse(paths)

      # Initialize depth tree with nodes having count >= k
      tree0 =
        Enum.reduce(nodes, :gb_trees.empty(), fn
          {0, _}, acc -> acc
          {_id, node}, acc ->
            if node.cnt >= k do
              inc_depth(acc, node.depth)
            else
              acc
            end
        end)

      # Process each word
      {answers_rev, _, _} =
        Enum.reduce(Enum.with_index(paths), {[], nodes, tree0},
          fn {path, _i}, {ans_acc, nds_cur, tr_cur} ->
            # remove current word
            {nds_after_rem, tr_after_rem} =
              Enum.reduce(path, {nds_cur, tr_cur}, fn node_id, {nm, tr} ->
                node = nm[node_id]
                old_cnt = node.cnt
                new_cnt = old_cnt - 1
                nm2 = Map.put(nm, node_id, %{node | cnt: new_cnt})

                tr2 =
                  if old_cnt >= k and new_cnt < k do
                    dec_depth(tr, node.depth)
                  else
                    tr
                  end

                {nm2, tr2}
              end)

            ans_i =
              if :gb_trees.is_empty(tr_after_rem) do
                0
              else
                elem(:gb_trees.largest(tr_after_rem), 0)
              end

            # restore the word
            {nds_restored, tr_restored} =
              Enum.reduce(path, {nds_after_rem, tr_after_rem}, fn node_id, {nm, tr} ->
                node = nm[node_id]
                old_cnt = node.cnt
                new_cnt = old_cnt + 1
                nm2 = Map.put(nm, node_id, %{node | cnt: new_cnt})

                tr2 =
                  if old_cnt < k and new_cnt >= k do
                    inc_depth(tr, node.depth)
                  else
                    tr
                  end

                {nm2, tr2}
              end)

            {[ans_i | ans_acc], nds_restored, tr_restored}
          end)

      Enum.reverse(answers_rev)
    end
  end

  defp inc_depth(tree, depth) do
    case :gb_trees.lookup(depth, tree) do
      {:value, v} -> :gb_trees.update(depth, v + 1, tree)
      :none -> :gb_trees.insert(depth, 1, tree)
    end
  end

  defp dec_depth(tree, depth) do
    case :gb_trees.lookup(depth, tree) do
      {:value, 1} -> :gb_trees.delete(depth, tree)
      {:value, v} -> :gb_trees.update(depth, v - 1, tree)
      :none -> tree
    end
  end
end
```
