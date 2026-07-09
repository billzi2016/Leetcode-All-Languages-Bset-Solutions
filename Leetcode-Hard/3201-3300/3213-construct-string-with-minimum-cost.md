# 3213. Construct String with Minimum Cost

## Cpp

```cpp
class Solution {
public:
    struct Node {
        int nxt[26];
        int link;
        vector<int> out;
        Node() {
            fill(begin(nxt), end(nxt), -1);
            link = 0;
        }
    };
    
    int minimumCost(string target, vector<string>& words, vector<int>& costs) {
        int m = words.size();
        vector<int> wlen(m);
        for (int i = 0; i < m; ++i) wlen[i] = words[i].size();
        
        // Build Aho-Corasick trie
        vector<Node> trie(1); // root at 0
        for (int id = 0; id < m; ++id) {
            int v = 0;
            for (char ch : words[id]) {
                int c = ch - 'a';
                if (trie[v].nxt[c] == -1) {
                    trie[v].nxt[c] = trie.size();
                    trie.emplace_back();
                }
                v = trie[v].nxt[c];
            }
            trie[v].out.push_back(id);
        }
        
        // Build failure links
        queue<int> q;
        for (int c = 0; c < 26; ++c) {
            int u = trie[0].nxt[c];
            if (u != -1) {
                trie[u].link = 0;
                q.push(u);
            } else {
                trie[0].nxt[c] = 0;
            }
        }
        while (!q.empty()) {
            int v = q.front(); q.pop();
            for (int c = 0; c < 26; ++c) {
                int u = trie[v].nxt[c];
                if (u != -1) {
                    trie[u].link = trie[trie[v].link].nxt[c];
                    // merge outputs
                    const vector<int>& linkOut = trie[trie[u].link].out;
                    trie[u].out.insert(trie[u].out.end(), linkOut.begin(), linkOut.end());
                    q.push(u);
                } else {
                    trie[v].nxt[c] = trie[trie[v].link].nxt[c];
                }
            }
        }
        
        const long long INF = (1LL<<60);
        int n = target.size();
        vector<long long> dp(n+1, INF);
        dp[0] = 0;
        int node = 0;
        for (int i = 0; i < n; ++i) {
            int c = target[i] - 'a';
            node = trie[node].nxt[c];
            // process all patterns ending at position i
            for (int pid : trie[node].out) {
                int len = wlen[pid];
                long long cost = costs[pid];
                int startIdx = i + 1 - len;
                if (startIdx >= 0 && dp[startIdx] != INF) {
                    dp[i+1] = min(dp[i+1], dp[startIdx] + cost);
                }
            }
        }
        return dp[n] == INF ? -1 : (int)dp[n];
    }
};
```

## Java

```java
class Solution {
    private static class Node {
        int[] next = new int[26];
        int link;
        java.util.List<Integer> out = new java.util.ArrayList<>();
        Node() {
            java.util.Arrays.fill(next, -1);
            link = 0;
        }
    }

    public int minimumCost(String target, String[] words, int[] costs) {
        int n = target.length();
        int m = words.length;

        // store word lengths
        int[] wlen = new int[m];
        for (int i = 0; i < m; i++) wlen[i] = words[i].length();

        // build trie
        java.util.List<Node> nodes = new java.util.ArrayList<>();
        nodes.add(new Node()); // root at index 0
        for (int id = 0; id < m; id++) {
            String w = words[id];
            int cur = 0;
            for (int j = 0; j < w.length(); j++) {
                int c = w.charAt(j) - 'a';
                if (nodes.get(cur).next[c] == -1) {
                    nodes.add(new Node());
                    nodes.get(cur).next[c] = nodes.size() - 1;
                }
                cur = nodes.get(cur).next[c];
            }
            nodes.get(cur).out.add(id);
        }

        // build failure links (Aho-Corasick)
        java.util.Queue<Integer> q = new java.util.ArrayDeque<>();
        for (int c = 0; c < 26; c++) {
            int child = nodes.get(0).next[c];
            if (child != -1) {
                nodes.get(child).link = 0;
                q.offer(child);
            } else {
                nodes.get(0).next[c] = 0;
            }
        }

        while (!q.isEmpty()) {
            int v = q.poll();
            Node nodeV = nodes.get(v);
            for (int c = 0; c < 26; c++) {
                int child = nodeV.next[c];
                if (child != -1) {
                    nodes.get(child).link = nodes.get(nodes.get(nodeV.link).next[c]);
                    // merge output lists
                    nodes.get(child).out.addAll(nodes.get(nodes.get(child).link).out);
                    q.offer(child);
                } else {
                    nodeV.next[c] = nodes.get(nodeV.link).next[c];
                }
            }
        }

        final int INF = Integer.MAX_VALUE / 2;
        int[] dp = new int[n + 1];
        java.util.Arrays.fill(dp, INF);
        dp[0] = 0;

        int state = 0;
        for (int i = 0; i < n; i++) {
            int c = target.charAt(i) - 'a';
            state = nodes.get(state).next[c];
            Node curNode = nodes.get(state);
            if (!curNode.out.isEmpty()) {
                for (int idx : curNode.out) {
                    int len = wlen[idx];
                    int start = i + 1 - len;
                    if (dp[start] != INF) {
                        int cand = dp[start] + costs[idx];
                        if (cand < dp[i + 1]) dp[i + 1] = cand;
                    }
                }
            }
        }

        return dp[n] >= INF ? -1 : dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def minimumCost(self, target, words, costs):
        """
        :type target: str
        :type words: List[str]
        :type costs: List[int]
        :rtype: int
        """
        # Build Aho-Corasick automaton
        n_words = len(words)
        word_len = [len(w) for w in words]

        children = [[-1] * 26]   # root node
        fail = [0]
        out = [[]]               # list of word ids ending at this node

        for idx, w in enumerate(words):
            node = 0
            for ch in w:
                c = ord(ch) - 97
                if children[node][c] == -1:
                    children[node][c] = len(children)
                    children.append([-1] * 26)
                    fail.append(0)
                    out.append([])
                node = children[node][c]
            out[node].append(idx)

        # Build failure links using BFS
        from collections import deque
        q = deque()
        for c in range(26):
            nxt = children[0][c]
            if nxt != -1:
                fail[nxt] = 0
                q.append(nxt)
            else:
                children[0][c] = 0  # set missing transitions to root

        while q:
            v = q.popleft()
            for c in range(26):
                nxt = children[v][c]
                if nxt != -1:
                    f = fail[v]
                    while children[f][c] == -1:
                        f = fail[f]
                    fail[nxt] = children[f][c]
                    out[nxt].extend(out[fail[nxt]])
                    q.append(nxt)
                else:
                    children[v][c] = children[fail[v]][c]

        INF = 10 ** 18
        m = len(target)
        dp = [INF] * (m + 1)
        dp[0] = 0

        node = 0
        for i, ch in enumerate(target):
            c = ord(ch) - 97
            node = children[node][c]
            # process all words ending here
            if out[node]:
                cur_pos = i + 1
                best = dp[cur_pos]  # current value
                for wid in out[node]:
                    L = word_len[wid]
                    prev = dp[cur_pos - L]
                    if prev + costs[wid] < best:
                        best = prev + costs[wid]
                dp[cur_pos] = best

        return -1 if dp[m] == INF else dp[m]
```

## Python3

```python
import sys
from collections import deque
from typing import List

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        # keep minimal cost for each distinct word
        best = {}
        for w, c in zip(words, costs):
            if w not in best or c < best[w]:
                best[w] = c

        # Aho-Corasick construction
        children = [[-1] * 26]   # root node
        fail = [0]
        out = [[]]               # list of (length, cost)

        for w, c in best.items():
            node = 0
            for ch in w:
                idx = ord(ch) - 97
                if children[node][idx] == -1:
                    children[node][idx] = len(children)
                    children.append([-1] * 26)
                    fail.append(0)
                    out.append([])
                node = children[node][idx]
            out[node].append((len(w), c))

        # build failure links
        q = deque()
        for ch in range(26):
            nxt = children[0][ch]
            if nxt != -1:
                q.append(nxt)
                fail[nxt] = 0
            else:
                children[0][ch] = 0

        while q:
            v = q.popleft()
            for ch in range(26):
                u = children[v][ch]
                if u != -1:
                    f = fail[v]
                    while children[f][ch] == -1:
                        f = fail[f]
                    fail[u] = children[f][ch]
                    out[u].extend(out[fail[u]])
                    q.append(u)
                else:
                    children[v][ch] = children[fail[v]][ch]

        n = len(target)
        INF = 10**18
        dp = [INF] * (n + 1)
        dp[0] = 0

        node = 0
        for i, ch in enumerate(target):
            idx = ord(ch) - 97
            node = children[node][idx]
            if out[node]:
                pos = i + 1
                for length, cost in out[node]:
                    prev = pos - length
                    val = dp[prev] + cost
                    if val < dp[pos]:
                        dp[pos] = val

        return -1 if dp[n] == INF else dp[n]
```

## C

```c
#include <string.h>
#include <limits.h>

#define MAXNODES 50010
#define MAXOUT   50010

static int nxt[MAXNODES][26];
static int fail_link[MAXNODES];
static int out_link[MAXNODES];
static int out_head[MAXNODES];

static int out_len[MAXOUT];
static int out_cost[MAXOUT];
static int out_next[MAXOUT];

int minimumCost(char* target, char** words, int wordsSize, int* costs, int costsSize) {
    // initialize trie
    int nodeCnt = 1; // root is 0
    memset(nxt, -1, sizeof(nxt));
    memset(out_head, -1, sizeof(out_head));
    int outCnt = 0;

    for (int i = 0; i < wordsSize; ++i) {
        char *w = words[i];
        int len = strlen(w);
        int cur = 0;
        for (int j = 0; j < len; ++j) {
            int c = w[j] - 'a';
            if (nxt[cur][c] == -1) {
                nxt[cur][c] = nodeCnt++;
            }
            cur = nxt[cur][c];
        }
        // add output entry
        out_len[outCnt] = len;
        out_cost[outCnt] = costs[i];
        out_next[outCnt] = out_head[cur];
        out_head[cur] = outCnt;
        ++outCnt;
    }

    // set missing transitions of root to itself
    for (int c = 0; c < 26; ++c) {
        if (nxt[0][c] == -1) nxt[0][c] = 0;
    }

    // build failure links using BFS
    int queue[MAXNODES];
    int qh = 0, qt = 0;

    for (int c = 0; c < 26; ++c) {
        int v = nxt[0][c];
        if (v != 0) {
            fail_link[v] = 0;
            out_link[v] = (out_head[0] != -1) ? 0 : -1;
            queue[qt++] = v;
        }
    }

    while (qh < qt) {
        int u = queue[qh++];
        for (int c = 0; c < 26; ++c) {
            int v = nxt[u][c];
            if (v != -1) {
                int f = fail_link[u];
                while (nxt[f][c] == -1) f = fail_link[f];
                fail_link[v] = nxt[f][c];

                if (out_head[fail_link[v]] != -1)
                    out_link[v] = fail_link[v];
                else
                    out_link[v] = out_link[fail_link[v]];
                queue[qt++] = v;
            } else {
                nxt[u][c] = nxt[fail_link[u]][c];
            }
        }
    }

    // DP over target
    int n = strlen(target);
    const long long INF = (1LL << 60);
    static long long dp[MAXNODES]; // size up to n+1 <= 50005
    for (int i = 0; i <= n; ++i) dp[i] = INF;
    dp[0] = 0;

    int cur = 0;
    for (int i = 0; i < n; ++i) {
        int c = target[i] - 'a';
        cur = nxt[cur][c];

        int temp = cur;
        while (temp != -1 && temp != 0) {
            for (int idx = out_head[temp]; idx != -1; idx = out_next[idx]) {
                int len = out_len[idx];
                int cost = out_cost[idx];
                int start = i + 1 - len;
                if (start >= 0 && dp[start] + cost < dp[i + 1])
                    dp[i + 1] = dp[start] + cost;
            }
            temp = out_link[temp];
        }
    }

    if (dp[n] == INF) return -1;
    return (int)dp[n];
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumCost(string target, string[] words, int[] costs) {
        int totalLen = 0;
        foreach (var w in words) totalLen += w.Length;
        int maxNodes = totalLen + 1;

        var next = new int[maxNodes][];
        for (int i = 0; i < maxNodes; i++) {
            next[i] = new int[26];
            for (int j = 0; j < 26; j++) next[i][j] = -1;
        }

        var fail = new int[maxNodes];
        var output = new List<int>[maxNodes];

        int nodeCount = 1; // root is 0

        for (int idx = 0; idx < words.Length; idx++) {
            string w = words[idx];
            int cur = 0;
            foreach (char ch in w) {
                int c = ch - 'a';
                if (next[cur][c] == -1) {
                    next[cur][c] = nodeCount++;
                }
                cur = next[cur][c];
            }
            if (output[cur] == null) output[cur] = new List<int>();
            output[cur].Add(idx);
        }

        var queue = new Queue<int>();
        for (int c = 0; c < 26; c++) {
            int child = next[0][c];
            if (child != -1) {
                fail[child] = 0;
                queue.Enqueue(child);
            } else {
                next[0][c] = 0;
            }
        }

        while (queue.Count > 0) {
            int v = queue.Dequeue();
            for (int c = 0; c < 26; c++) {
                int child = next[v][c];
                if (child != -1) {
                    fail[child] = next[fail[v]][c];
                    if (output[fail[child]] != null) {
                        if (output[child] == null) output[child] = new List<int>();
                        output[child].AddRange(output[fail[child]]);
                    }
                    queue.Enqueue(child);
                } else {
                    next[v][c] = next[fail[v]][c];
                }
            }
        }

        int n = target.Length;
        const long INF = (long)1e18;
        var dp = new long[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = INF;
        dp[0] = 0;

        int state = 0;
        for (int i = 0; i < n; i++) {
            int c = target[i] - 'a';
            state = next[state][c];
            if (output[state] != null) {
                foreach (int idx in output[state]) {
                    int len = words[idx].Length;
                    int prev = i + 1 - len;
                    if (prev >= 0 && dp[prev] != INF) {
                        long cand = dp[prev] + costs[idx];
                        if (cand < dp[i + 1]) dp[i + 1] = cand;
                    }
                }
            }
        }

        return dp[n] == INF ? -1 : (int)dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} target
 * @param {string[]} words
 * @param {number[]} costs
 * @return {number}
 */
var minimumCost = function(target, words, costs) {
    // Build Aho-Corasick automaton
    const nodes = [];
    const createNode = () => ({
        next: new Array(26).fill(-1),
        fail: 0,
        outputs: [] // each element {len, cost}
    });
    nodes.push(createNode()); // root at index 0

    for (let i = 0; i < words.length; ++i) {
        const w = words[i];
        const c = costs[i];
        let cur = 0;
        for (let j = 0; j < w.length; ++j) {
            const ch = w.charCodeAt(j) - 97;
            if (nodes[cur].next[ch] === -1) {
                nodes[cur].next[ch] = nodes.length;
                nodes.push(createNode());
            }
            cur = nodes[cur].next[ch];
        }
        // store minimal cost for this length at terminal node
        const len = w.length;
        let found = false;
        for (let o of nodes[cur].outputs) {
            if (o.len === len) {
                if (c < o.cost) o.cost = c;
                found = true;
                break;
            }
        }
        if (!found) nodes[cur].outputs.push({len, cost: c});
    }

    // Build failure links
    const queue = [];
    for (let ch = 0; ch < 26; ++ch) {
        const nxt = nodes[0].next[ch];
        if (nxt !== -1) {
            nodes[nxt].fail = 0;
            queue.push(nxt);
        } else {
            nodes[0].next[ch] = 0; // link missing edges to root for easier transition
        }
    }

    for (let qIdx = 0; qIdx < queue.length; ++qIdx) {
        const v = queue[qIdx];
        for (let ch = 0; ch < 26; ++ch) {
            let u = nodes[v].next[ch];
            if (u !== -1) {
                let f = nodes[v].fail;
                while (nodes[f].next[ch] === -1) f = nodes[f].fail;
                f = nodes[f].next[ch];
                nodes[u].fail = f;

                // merge outputs from fail node
                const outFail = nodes[f].outputs;
                if (outFail.length) {
                    for (let o of outFail) {
                        let exist = false;
                        for (let curOut of nodes[u].outputs) {
                            if (curOut.len === o.len) {
                                if (o.cost < curOut.cost) curOut.cost = o.cost;
                                exist = true;
                                break;
                            }
                        }
                        if (!exist) nodes[u].outputs.push({len: o.len, cost: o.cost});
                    }
                }

                queue.push(u);
            } else {
                nodes[v].next[ch] = nodes[nodes[v].fail].next[ch];
            }
        }
    }

    const n = target.length;
    const dp = new Array(n + 1).fill(Infinity);
    dp[0] = 0;

    let state = 0;
    for (let i = 0; i < n; ++i) {
        const chIdx = target.charCodeAt(i) - 97;
        while (nodes[state].next[chIdx] === -1) state = nodes[state].fail;
        state = nodes[state].next[chIdx];

        const outs = nodes[state].outputs;
        for (let o of outs) {
            const start = i - o.len + 1;
            if (start >= 0 && dp[start] !== Infinity) {
                const newCost = dp[start] + o.cost;
                if (newCost < dp[i + 1]) dp[i + 1] = newCost;
            }
        }
    }

    return dp[n] === Infinity ? -1 : dp[n];
};
```

## Typescript

```typescript
function minimumCost(target: string, words: string[], costs: number[]): number {
    const n = target.length;
    const INF = Number.MAX_SAFE_INTEGER;

    interface Node {
        next: Int32Array;
        fail: number;
        out: number[];
    }

    const nodes: Node[] = [];
    const newNode = (): Node => ({
        next: new Int32Array(26).fill(-1),
        fail: 0,
        out: []
    });
    nodes.push(newNode()); // root at index 0

    // Build trie
    for (let i = 0; i < words.length; i++) {
        const w = words[i];
        let cur = 0;
        for (let j = 0; j < w.length; j++) {
            const c = w.charCodeAt(j) - 97;
            if (nodes[cur].next[c] === -1) {
                nodes[cur].next[c] = nodes.length;
                nodes.push(newNode());
            }
            cur = nodes[cur].next[c];
        }
        nodes[cur].out.push(i);
    }

    // Build failure links using BFS
    const queue: number[] = [];
    for (let c = 0; c < 26; c++) {
        const child = nodes[0].next[c];
        if (child !== -1) {
            nodes[child].fail = 0;
            queue.push(child);
        } else {
            nodes[0].next[c] = 0; // set missing transitions to root for easier traversal
        }
    }

    while (queue.length) {
        const v = queue.shift()!;
        const outFail = nodes[nodes[v].fail].out;
        if (outFail.length) {
            nodes[v].out = nodes[v].out.concat(outFail);
        }
        for (let c = 0; c < 26; c++) {
            let child = nodes[v].next[c];
            if (child !== -1) {
                nodes[child].fail = nodes[nodes[v].fail].next[c];
                queue.push(child);
            } else {
                nodes[v].next[c] = nodes[nodes[v].fail].next[c];
            }
        }
    }

    const dp: number[] = new Array(n + 1).fill(INF);
    dp[0] = 0;

    let state = 0;
    for (let i = 0; i < n; i++) {
        const ch = target.charCodeAt(i) - 97;
        state = nodes[state].next[ch];

        const outs = nodes[state].out;
        for (const idx of outs) {
            const len = words[idx].length;
            const prevPos = i + 1 - len;
            if (prevPos >= 0 && dp[prevPos] !== INF) {
                const newCost = dp[prevPos] + costs[idx];
                if (newCost < dp[i + 1]) dp[i + 1] = newCost;
            }
        }
    }

    return dp[n] === INF ? -1 : dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param String $target
     * @param String[] $words
     * @param Integer[] $costs
     * @return Integer
     */
    function minimumCost($target, $words, $costs) {
        $nWords = count($words);
        $wordLen = [];
        for ($i = 0; $i < $nWords; $i++) {
            $wordLen[$i] = strlen($words[$i]);
        }

        // Build Aho-Corasick automaton
        $next = [];      // transitions
        $fail = [];      // failure links
        $out  = [];      // list of word indices ending at node
        $link = [];      // output link to next node with output

        // create root node 0
        $next[] = array_fill(0, 26, -1);
        $fail[] = 0;
        $out[]  = [];
        $link[] = 0;

        // insert words
        for ($idx = 0; $idx < $nWords; $idx++) {
            $node = 0;
            $w = $words[$idx];
            $lenW = $wordLen[$idx];
            for ($j = 0; $j < $lenW; $j++) {
                $cIdx = ord($w[$j]) - 97;
                if ($next[$node][$cIdx] === -1) {
                    // create new node
                    $next[] = array_fill(0, 26, -1);
                    $fail[] = 0;
                    $out[]  = [];
                    $link[] = 0;
                    $next[$node][$cIdx] = count($next) - 1;
                }
                $node = $next[$node][$cIdx];
            }
            $out[$node][] = $idx; // store word index at terminal node
        }

        // build failure links using BFS
        $queue = new SplQueue();

        // initialize root transitions
        for ($c = 0; $c < 26; $c++) {
            $child = $next[0][$c];
            if ($child !== -1) {
                $fail[$child] = 0;
                $link[$child] = 0;
                $queue->enqueue($child);
            } else {
                $next[0][$c] = 0; // point missing transitions to root
            }
        }

        while (!$queue->isEmpty()) {
            $r = $queue->dequeue();
            for ($c = 0; $c < 26; $c++) {
                $child = $next[$r][$c];
                if ($child !== -1) {
                    $f = $fail[$r];
                    while ($next[$f][$c] === -1) {
                        $f = $fail[$f];
                    }
                    $failChild = $next[$f][$c];
                    $fail[$child] = $failChild;

                    if (!empty($out[$failChild])) {
                        $link[$child] = $failChild;
                    } else {
                        $link[$child] = $link[$failChild];
                    }

                    $queue->enqueue($child);
                } else {
                    $next[$r][$c] = $next[$fail[$r]][$c];
                }
            }
        }

        // DP over target
        $n = strlen($target);
        $INF = PHP_INT_MAX;
        $dp = array_fill(0, $n + 1, $INF);
        $dp[0] = 0;

        $state = 0;
        for ($i = 0; $i < $n; $i++) {
            $cIdx = ord($target[$i]) - 97;
            $state = $next[$state][$cIdx];

            // process all outputs reachable from current state
            $temp = $state;
            while ($temp != 0) {
                if (!empty($out[$temp])) {
                    foreach ($out[$temp] as $wIdx) {
                        $lenW = $wordLen[$wIdx];
                        $start = $i - $lenW + 1; // start index of this word in target
                        if ($dp[$start] !== $INF) {
                            $newCost = $dp[$start] + $costs[$wIdx];
                            $endPos = $i + 1;
                            if ($newCost < $dp[$endPos]) {
                                $dp[$endPos] = $newCost;
                            }
                        }
                    }
                }
                $temp = $link[$temp];
            }
        }

        return $dp[$n] === $INF ? -1 : $dp[$n];
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func minimumCost(_ target: String, _ words: [String], _ costs: [Int]) -> Int {
        let INF = Int.max / 4
        // Trie structures
        var next = [[Int]]()
        var fail = [Int]()
        var outs = [[(len: Int, cost: Int)]]()
        
        func addNode() {
            next.append(Array(repeating: -1, count: 26))
            fail.append(0)
            outs.append([])
        }
        addNode() // root node index 0
        
        // Insert words into trie
        for (idx, word) in words.enumerated() {
            let cost = costs[idx]
            var cur = 0
            for ch in word.utf8 {
                let c = Int(ch - 97)
                if next[cur][c] == -1 {
                    addNode()
                    next[cur][c] = next.count - 1
                }
                cur = next[cur][c]
            }
            let wlen = word.count
            var found = false
            for i in 0..<outs[cur].count {
                if outs[cur][i].len == wlen {
                    if cost < outs[cur][i].cost {
                        outs[cur][i].cost = cost
                    }
                    found = true
                    break
                }
            }
            if !found {
                outs[cur].append((len: wlen, cost: cost))
            }
        }
        
        // Build failure links (Aho-Corasick)
        var queue = [Int]()
        var head = 0
        
        for c in 0..<26 {
            let child = next[0][c]
            if child != -1 {
                fail[child] = 0
                queue.append(child)
            } else {
                next[0][c] = 0
            }
        }
        
        while head < queue.count {
            let v = queue[head]
            head += 1
            for c in 0..<26 {
                var u = next[v][c]
                if u != -1 {
                    fail[u] = next[fail[v]][c]
                    // merge outputs from failure node
                    outs[u].append(contentsOf: outs[fail[u]])
                    queue.append(u)
                } else {
                    next[v][c] = next[fail[v]][c]
                }
            }
        }
        
        // DP over target string
        let bytes = Array(target.utf8)
        let n = bytes.count
        var dp = Array(repeating: INF, count: n + 1)
        dp[0] = 0
        var state = 0
        
        for i in 0..<n {
            let cIdx = Int(bytes[i] - 97)
            state = next[state][cIdx]
            if !outs[state].isEmpty {
                for out in outs[state] {
                    let start = i + 1 - out.len
                    if start >= 0 && dp[start] != INF {
                        let newCost = dp[start] + out.cost
                        if newCost < dp[i + 1] {
                            dp[i + 1] = newCost
                        }
                    }
                }
            }
        }
        
        return dp[n] == INF ? -1 : dp[n]
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun minimumCost(target: String, words: Array<String>, costs: IntArray): Int {
        val n = target.length
        val m = words.size
        val wordLen = IntArray(m) { words[it].length }

        // Aho-Corasick structures
        val next = mutableListOf<IntArray>()
        val fail = mutableListOf<Int>()
        val output = mutableListOf<MutableList<Int>>()

        fun newNode(): Int {
            next.add(IntArray(26) { -1 })
            fail.add(0)
            output.add(mutableListOf())
            return next.size - 1
        }

        newNode() // root at index 0

        // Build trie
        for (i in 0 until m) {
            var node = 0
            for (ch in words[i]) {
                val c = ch.code - 'a'.code
                if (next[node][c] == -1) {
                    val nxt = newNode()
                    next[node][c] = nxt
                }
                node = next[node][c]
            }
            output[node].add(i)
        }

        // Build failure links
        val q: ArrayDeque<Int> = ArrayDeque()
        for (c in 0 until 26) {
            val child = next[0][c]
            if (child != -1) {
                fail[child] = 0
                q.add(child)
            }
        }

        while (!q.isEmpty()) {
            val v = q.removeFirst()
            for (c in 0 until 26) {
                val child = next[v][c]
                if (child != -1) {
                    var f = fail[v]
                    while (f != 0 && next[f][c] == -1) {
                        f = fail[f]
                    }
                    if (next[f][c] != -1) f = next[f][c] else f = 0
                    fail[child] = f
                    if (output[f].isNotEmpty()) {
                        output[child].addAll(output[f])
                    }
                    q.add(child)
                }
            }
        }

        val INF = Long.MAX_VALUE / 4
        val dp = LongArray(n + 1) { INF }
        dp[0] = 0L

        var node = 0
        for (i in 0 until n) {
            val c = target[i].code - 'a'.code
            while (node != 0 && next[node][c] == -1) {
                node = fail[node]
            }
            if (next[node][c] != -1) node = next[node][c] else node = 0

            for (idx in output[node]) {
                val len = wordLen[idx]
                val start = i - len + 1
                if (start >= 0 && dp[start] != INF) {
                    val newCost = dp[start] + costs[idx].toLong()
                    if (newCost < dp[i + 1]) dp[i + 1] = newCost
                }
            }
        }

        return if (dp[n] == INF) -1 else dp[n].toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minimumCost(String target, List<String> words, List<int> costs) {
    const int ALPH = 26;
    const int INF = 1 << 60;

    // Node definition
    class Node {
      List<int> next = List.filled(ALPH, -1);
      int fail = 0;
      List<int> out = [];
    }

    // Build trie
    List<Node> nodes = [Node()];
    for (int idx = 0; idx < words.length; idx++) {
      String w = words[idx];
      int cur = 0;
      for (int i = 0; i < w.length; i++) {
        int c = w.codeUnitAt(i) - 97;
        if (nodes[cur].next[c] == -1) {
          nodes[cur].next[c] = nodes.length;
          nodes.add(Node());
        }
        cur = nodes[cur].next[c];
      }
      nodes[cur].out.add(idx);
    }

    // Build failure links using BFS
    List<int> queue = [];
    int head = 0;

    for (int c = 0; c < ALPH; c++) {
      int child = nodes[0].next[c];
      if (child != -1) {
        nodes[child].fail = 0;
        queue.add(child);
      } else {
        // optional: set missing transitions to root (handled in traversal)
        nodes[0].next[c] = -1;
      }
    }

    while (head < queue.length) {
      int u = queue[head++];
      for (int c = 0; c < ALPH; c++) {
        int v = nodes[u].next[c];
        if (v != -1) {
          int f = nodes[u].fail;
          while (f != 0 && nodes[f].next[c] == -1) {
            f = nodes[f].fail;
          }
          if (nodes[f].next[c] != -1) {
            f = nodes[f].next[c];
          } else {
            f = 0;
          }
          nodes[v].fail = f;
          // merge output lists
          if (nodes[f].out.isNotEmpty) {
            nodes[v].out.addAll(nodes[f].out);
          }
          queue.add(v);
        } else {
          // keep -1, will be handled during traversal
        }
      }
    }

    int n = target.length;
    List<int> dp = List.filled(n + 1, INF);
    dp[0] = 0;

    int state = 0;
    for (int i = 0; i < n; i++) {
      int c = target.codeUnitAt(i) - 97;
      while (state != 0 && nodes[state].next[c] == -1) {
        state = nodes[state].fail;
      }
      if (nodes[state].next[c] != -1) {
        state = nodes[state].next[c];
      } else {
        state = 0;
      }

      // process all words ending at position i
      for (int idx in nodes[state].out) {
        int len = words[idx].length;
        int prevPos = i + 1 - len;
        if (prevPos >= 0 && dp[prevPos] != INF) {
          int newCost = dp[prevPos] + costs[idx];
          if (newCost < dp[i + 1]) dp[i + 1] = newCost;
        }
      }

      // also propagate dp without using a word ending here
      // (dp[i+1] may already have value from previous matches)
    }

    return dp[n] == INF ? -1 : dp[n];
  }
}
```

## Golang

```go
type pair struct {
	length int
	cost   int
}

type node struct {
	next [26]int
	fail int
	outs []pair
}

func minimumCost(target string, words []string, costs []int) int {
	// Build Aho-Corasick automaton
	nodes := make([]node, 0, 50000+1)
	newNode := func() node {
		n := node{fail: 0}
		for i := 0; i < 26; i++ {
			n.next[i] = -1
		}
		return n
	}
	nodes = append(nodes, newNode()) // root at index 0

	for idx, w := range words {
		cur := 0
		for _, ch := range w {
			c := int(ch - 'a')
			if nodes[cur].next[c] == -1 {
				nodes = append(nodes, newNode())
				nodes[cur].next[c] = len(nodes) - 1
			}
			cur = nodes[cur].next[c]
		}
		nodes[cur].outs = append(nodes[cur].outs, pair{length: len(w), cost: costs[idx]})
	}

	// Build failure links
	queue := make([]int, 0)
	for c := 0; c < 26; c++ {
		nxt := nodes[0].next[c]
		if nxt != -1 {
			nodes[nxt].fail = 0
			queue = append(queue, nxt)
		} else {
			nodes[0].next[c] = 0
		}
	}
	for len(queue) > 0 {
		v := queue[0]
		queue = queue[1:]
		for c := 0; c < 26; c++ {
			nxt := nodes[v].next[c]
			if nxt != -1 {
				f := nodes[nodes[v].fail].next[c]
				nodes[nxt].fail = f
				if len(nodes[f].outs) > 0 {
					nodes[nxt].outs = append(nodes[nxt].outs, nodes[f].outs...)
				}
				queue = append(queue, nxt)
			} else {
				nodes[v].next[c] = nodes[nodes[v].fail].next[c]
			}
		}
	}

	n := len(target)
	const INF int64 = 1 << 60
	dp := make([]int64, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = INF
	}
	dp[0] = 0

	cur := 0
	for i := 0; i < n; i++ {
		c := int(target[i] - 'a')
		cur = nodes[cur].next[c]
		if len(nodes[cur].outs) == 0 {
			continue
		}
		for _, p := range nodes[cur].outs {
			l := p.length
			if i+1 >= l && dp[i+1-l] != INF {
				val := dp[i+1-l] + int64(p.cost)
				if val < dp[i+1] {
					dp[i+1] = val
				}
			}
		}
	}

	if dp[n] == INF {
		return -1
	}
	return int(dp[n])
}
```

## Ruby

```ruby
def minimum_cost(target, words, costs)
  # Keep minimal cost for each distinct word
  min_cost = {}
  words.each_with_index do |w, i|
    c = costs[i]
    if !min_cost.key?(w) || c < min_cost[w]
      min_cost[w] = c
    end
  end

  # Build Aho-Corasick automaton
  next_arr = [Array.new(26, -1)]
  fail = [0]
  output = [[]]

  min_cost.each do |word, cost|
    node = 0
    word.each_byte do |b|
      idx = b - 97
      if next_arr[node][idx] == -1
        next_arr[node][idx] = next_arr.size
        next_arr << Array.new(26, -1)
        fail << 0
        output << []
      end
      node = next_arr[node][idx]
    end
    output[node] << [word.length, cost]
  end

  # Build failure links and complete transitions
  queue = []
  26.times do |c|
    child = next_arr[0][c]
    if child != -1
      fail[child] = 0
      queue << child
    else
      next_arr[0][c] = 0
    end
  end

  until queue.empty?
    r = queue.shift
    26.times do |c|
      u = next_arr[r][c]
      if u != -1
        f = fail[r]
        while next_arr[f][c] == -1
          f = fail[f]
        end
        fail[u] = next_arr[f][c]
        output[u].concat(output[fail[u]])
        queue << u
      else
        next_arr[r][c] = next_arr[fail[r]][c]
      end
    end
  end

  n = target.length
  inf = 1 << 60
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  node = 0

  target.each_byte.with_index do |b, i|
    idx = b - 97
    node = next_arr[node][idx]
    output[node].each do |len, cost|
      start = i - len + 1
      if dp[start] != inf
        new_cost = dp[start] + cost
        dp[i + 1] = new_cost if new_cost < dp[i + 1]
      end
    end
  end

  ans = dp[n]
  ans >= inf ? -1 : ans
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{ArrayBuffer, Queue}

  class Node {
    val children: Array[Int] = Array.fill(26)(-1)
    var fail: Int = 0
    val outs: ArrayBuffer[(Int, Int)] = ArrayBuffer.empty // (length, cost)
  }

  def minimumCost(target: String, words: Array[String], costs: Array[Int]): Int = {
    val nodes = new ArrayBuffer[Node]()
    nodes += new Node() // root at index 0

    // Build trie
    var idx = 0
    while (idx < words.length) {
      val w = words(idx)
      val cost = costs(idx)
      var cur = 0
      var j = 0
      while (j < w.length) {
        val c = w.charAt(j) - 'a'
        if (nodes(cur).children(c) == -1) {
          nodes(cur).children(c) = nodes.size
          nodes += new Node()
        }
        cur = nodes(cur).children(c)
        j += 1
      }
      nodes(cur).outs.append((w.length, cost))
      idx += 1
    }

    // Build failure links (Aho-Corasick)
    val q: Queue[Int] = Queue()
    for (c <- 0 until 26) {
      val child = nodes(0).children(c)
      if (child != -1) {
        nodes(child).fail = 0
        q.enqueue(child)
      }
    }

    while (q.nonEmpty) {
      val v = q.dequeue()
      for (c <- 0 until 26) {
        val u = nodes(v).children(c)
        if (u != -1) {
          var f = nodes(v).fail
          while (f != 0 && nodes(f).children(c) == -1) {
            f = nodes(f).fail
          }
          if (nodes(f).children(c) != -1) {
            nodes(u).fail = nodes(f).children(c)
          } else {
            nodes(u).fail = 0
          }
          // merge outputs from fail link
          nodes(u).outs ++= nodes(nodes(u).fail).outs
          q.enqueue(u)
        }
      }
    }

    val n = target.length
    val INF: Long = Long.MaxValue / 4
    val dp = Array.fill[Long](n + 1)(INF)
    dp(0) = 0L

    var state = 0
    var i = 0
    while (i < n) {
      val ch = target.charAt(i) - 'a'
      while (state != 0 && nodes(state).children(ch) == -1) {
        state = nodes(state).fail
      }
      if (nodes(state).children(ch) != -1) {
        state = nodes(state).children(ch)
      }

      // process matches ending at i
      val outsIter = nodes(state).outs.iterator
      while (outsIter.hasNext) {
        val (len, cost) = outsIter.next()
        val start = i + 1 - len
        if (start >= 0 && dp(start) != INF) {
          val newCost = dp(start) + cost
          if (newCost < dp(i + 1)) dp(i + 1) = newCost
        }
      }

      i += 1
    }

    if (dp(n) == INF) -1 else dp(n).toInt
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

#[derive(Clone)]
struct Node {
    next: [i32; 26],
    link: usize,
    out: Vec<usize>,
}
impl Node {
    fn new() -> Self {
        Node {
            next: [-1; 26],
            link: 0,
            out: Vec::new(),
        }
    }
}

impl Solution {
    pub fn minimum_cost(target: String, words: Vec<String>, costs: Vec<i32>) -> i32 {
        let n = target.len();
        let m = words.len();

        // store lengths and costs
        let mut word_len: Vec<usize> = Vec::with_capacity(m);
        for w in &words {
            word_len.push(w.len());
        }

        // Build Aho-Corasick trie
        let mut nodes: Vec<Node> = Vec::new();
        nodes.push(Node::new()); // root at index 0

        for (idx, w) in words.iter().enumerate() {
            let mut v = 0usize;
            for &b in w.as_bytes() {
                let c = (b - b'a') as usize;
                if nodes[v].next[c] == -1 {
                    nodes[v].next[c] = nodes.len() as i32;
                    nodes.push(Node::new());
                }
                v = nodes[v].next[c] as usize;
            }
            nodes[v].out.push(idx);
        }

        // Build failure links
        let mut q: VecDeque<usize> = VecDeque::new();
        // initialize children of root
        for c in 0..26 {
            if nodes[0].next[c] != -1 {
                let child = nodes[0].next[c] as usize;
                nodes[child].link = 0;
                q.push_back(child);
            }
        }

        while let Some(v) = q.pop_front() {
            for c in 0..26 {
                let nxt = nodes[v].next[c];
                if nxt != -1 {
                    let u = nxt as usize;
                    // compute failure link for u
                    let mut f = nodes[v].link;
                    while f != 0 && nodes[f].next[c] == -1 {
                        f = nodes[f].link;
                    }
                    if nodes[f].next[c] != -1 {
                        nodes[u].link = nodes[f].next[c] as usize;
                    } else {
                        nodes[u].link = 0;
                    }
                    // merge output
                    let link_out = nodes[nodes[u].link].out.clone();
                    nodes[u].out.extend(link_out);
                    q.push_back(u);
                }
            }
        }

        const INF: i64 = i64::MAX / 4;
        let mut dp: Vec<i64> = vec![INF; n + 1];
        dp[0] = 0;

        let bytes = target.as_bytes();
        let mut state = 0usize;
        for (pos, &b) in bytes.iter().enumerate() {
            let c = (b - b'a') as usize;
            while state != 0 && nodes[state].next[c] == -1 {
                state = nodes[state].link;
            }
            if nodes[state].next[c] != -1 {
                state = nodes[state].next[c] as usize;
            } // else stay at root (state = 0)

            let cur_pos = pos + 1; // dp index
            for &idx in &nodes[state].out {
                let len = word_len[idx];
                if cur_pos >= len {
                    let start = cur_pos - len;
                    if dp[start] != INF {
                        let cand = dp[start] + costs[idx] as i64;
                        if cand < dp[cur_pos] {
                            dp[cur_pos] = cand;
                        }
                    }
                }
            }
        }

        if dp[n] == INF {
            -1
        } else {
            dp[n] as i32
        }
    }
}
```

## Racket

```racket
(define/contract (minimum-cost target words costs)
  (-> string? (listof string?) (listof exact-integer?) exact-integer?)
  (let* ([n (string-length target)]
         [m (length words)]
         [word-lens (list->vector (map string-length words))]
         [cost-vec (list->vector costs)]
         ;; total nodes upper bound
         [total-len (apply + (map string-length words))]
         [max-nodes (+ total-len 1)]
         [children (make-vector max-nodes #f)]   ; each entry will be a vector of 26 ints
         [outs (make-vector max-nodes '())]      ; list of word indices ending at node
         [fail (make-vector max-nodes -1)])
    ;; initialize root
    (vector-set! children 0 (make-vector 26 -1))
    (let ([node-count 1])
      ;; build trie
      (for ([w words] [idx (in-naturals)])
        (let ([len (string-length w)]
              [node 0])
          (for ([j (in-range len)])
            (define c (- (char->integer (string-ref w j))
                         (char->integer #\a)))
            (define child (vector-ref (vector-ref children node) c))
            (if (= child -1)
                (begin
                  (set! child node-count)
                  (vector-set! children node-count (make-vector 26 -1))
                  (vector-set! outs node-count '())
                  (vector-set! fail node-count -1)
                  (vector-set! (vector-ref children node) c child)
                  (set! node-count (+ node-count 1)))
                (void))
            (set! node child))
          ;; add word index to output list of terminal node
          (let ([lst (vector-ref outs node)])
            (vector-set! outs node (cons idx lst)))))
      ;; build failure links using BFS
      (define queue (make-vector max-nodes 0))
      (define head 0)
      (define tail 0)
      ;; enqueue root's immediate children
      (for ([c (in-range 26)])
        (define child (vector-ref (vector-ref children 0) c))
        (when (>= child 0)
          (vector-set! fail child 0)
          (vector-set! queue tail child)
          (set! tail (+ tail 1))))
      ;; BFS
      (let loop ()
        (when (< head tail)
          (define cur (vector-ref queue head))
          (set! head (+ head 1))
          (for ([c (in-range 26)])
            (define child (vector-ref (vector-ref children cur) c))
            (if (>= child 0)
                (begin
                  ;; compute fail for child
                  (let recur ((f (vector-ref fail cur)))
                    (define fchild (vector-ref (vector-ref children f) c))
                    (if (>= fchild 0)
                        (vector-set! fail child fchild)
                        (if (= f 0)
                            (vector-set! fail child 0)
                            (recur (vector-ref fail f)))))
                  ;; enqueue child
                  (vector-set! queue tail child)
                  (set! tail (+ tail 1)))
                (void))))
          (loop))
      ;; DP over target
      (define INF (expt 2 60))
      (define dp (make-vector (+ n 1) INF))
      (vector-set! dp 0 0)
      (let ([cur 0])
        (for ([i (in-range n)])
          (define ch (- (char->integer (string-ref target i))
                        (char->integer #\a)))
          ;; transition with fallback
          (let move ()
            (define nxt (vector-ref (vector-ref children cur) ch))
            (if (>= nxt 0)
                (set! cur nxt)
                (if (= cur 0)
                    (void)
                    (begin (set! cur (vector-ref fail cur)) (move)))))
          ;; process outputs along failure chain
          (let recur ((node cur))
            (when (>= node 0)
              (for ([idx (in-list (vector-ref outs node))])
                (define l (vector-ref word-lens idx))
                (define prev (- (+ i 1) l))
                (when (and (>= prev 0) (< (vector-ref dp prev) INF))
                  (define newc (+ (vector-ref dp prev) (vector-ref cost-vec idx)))
                  (when (< newc (vector-ref dp (+ i 1)))
                    (vector-set! dp (+ i 1) newc))))
              (if (= node 0)
                  (void)
                  (recur (vector-ref fail node)))))
          ))
      (let ([ans (vector-ref dp n)])
        (if (>= ans INF) -1 ans)))))
```

## Erlang

```erlang
-spec minimum_cost(Target :: unicode:unicode_binary(), Words :: [unicode:unicode_binary()], Costs :: [integer()]) -> integer().
minimum_cost(Target, Words, Costs) ->
    INF = 1 bsl 60,
    N = byte_size(Target),
    M = length(Words),

    %% Build maps for word lengths and costs (id starts from 1)
    {LenMap, CostMap} = build_word_maps(Words, Costs, 1, #{}, #{}),

    %% Build Aho-Corasick automaton
    {Nodes, _NextId} = build_trie(Words, 1, #{0 => #{children => #{},
                                                   fail => 0,
                                                   output => []}}),
    NodesWithFail = build_fail_links(Nodes),

    %% DP array initialization
    DP0 = array:new(0, [{size, N + 1}]),
    DP = array:set(0, 0, DP0),

    %% Scan target string
    TargetCodes = binary:bin_to_list(Target),
    FinalDP = scan_target(TargetCodes, NodesWithFail, LenMap, CostMap, DP, INF, 0, 1),

    Result = array:get(N, FinalDP),
    case Result >= INF of
        true -> -1;
        false -> Result
    end.

%% Build length and cost maps for words (id => value)
build_word_maps([], [], _Id, LenMap, CostMap) ->
    {LenMap, CostMap};
build_word_maps([W|Ws], [C|Cs], Id, LenMapAcc, CostMapAcc) ->
    Len = byte_size(W),
    NewLenMap = maps:put(Id, Len, LenMapAcc),
    NewCostMap = maps:put(Id, C, CostMapAcc),
    build_word_maps(Ws, Cs, Id + 1, NewLenMap, NewCostMap).

%% Insert all words into trie
build_trie([], _NextId, Nodes) ->
    {Nodes, _NextId};
build_trie([W|Ws], NextId, Nodes) ->
    Codes = binary:bin_to_list(W),
    {NewNodes, NewNextId} = insert_word(Codes, 0, Nodes, NextId, length(Ws)+1), % id will be assigned later
    build_trie(Ws, NewNextId, NewNodes).

%% Insert a single word (its characters) into the trie.
insert_word([], NodeId, Nodes, NextId, WordId) ->
    %% add output (word id) to node
    Node = maps:get(NodeId, Nodes),
    Output = maps:get(output, Node),
    UpdatedNode = Node#{output => [WordId | Output]},
    {maps:put(NodeId, UpdatedNode, Nodes), NextId};
insert_word([C|Rest], CurId, Nodes, NextId, WordId) ->
    CurNode = maps:get(CurId, Nodes),
    Children = maps:get(children, CurNode),
    case maps:find(C, Children) of
        {ok, ChildId} ->
            insert_word(Rest, ChildId, Nodes, NextId, WordId);
        error ->
            NewId = NextId,
            NewNode = #{children => #{}, fail => 0, output => []},
            UpdatedChildren = maps:put(C, NewId, Children),
            UpdatedCurNode = CurNode#{children => UpdatedChildren},
            Nodes1 = maps:put(CurId, UpdatedCurNode, Nodes),
            Nodes2 = maps:put(NewId, NewNode, Nodes1),
            insert_word(Rest, NewId, Nodes2, NextId + 1, WordId)
    end.

%% Build failure links using BFS
build_fail_links(Nodes) ->
    Queue0 = [],
    RootChildren = maps:get(children, maps:get(0, Nodes)),
    {Queue1, Nodes1} = maps:fold(
        fun(_Char, ChildId, {QAcc, NAcc}) ->
                Node = maps:get(ChildId, NAcc),
                UpdatedNode = Node#{fail => 0},
                {QAcc ++ [ChildId], maps:put(ChildId, UpdatedNode, NAcc)}
        end,
        {Queue0, Nodes},
        RootChildren),
    bfs_fail(Queue1, Nodes1).

bfs_fail([], Nodes) -> Nodes;
bfs_fail([Current|RestQueue], Nodes) ->
    CurNode = maps:get(Current, Nodes),
    Children = maps:get(children, CurNode),
    {NewQueue, UpdatedNodes} = maps:fold(
        fun(Char, ChildId, {QAcc, NAcc}) ->
                %% compute fail for child
                FailState = find_fail(maps:get(fail, CurNode), Char, NAcc),
                ChildNode = maps:get(ChildId, NAcc),
                ChildFail = FailState,
                OutputFromFail = maps:get(output, maps:get(FailState, NAcc)),
                NewOutput = lists:usort(lists:append(maps:get(output, ChildNode), OutputFromFail)),
                UpdatedChild = ChildNode#{fail => ChildFail, output => NewOutput},
                {QAcc ++ [ChildId], maps:put(ChildId, UpdatedChild, NAcc)}
        end,
        {RestQueue, Nodes},
        Children),
    bfs_fail(NewQueue, UpdatedNodes).

find_fail(State, Char, Nodes) when State =:= 0 ->
    RootChildren = maps:get(children, maps:get(0, Nodes)),
    case maps:find(Char, RootChildren) of
        {ok, Id} -> Id;
        error -> 0
    end;
find_fail(State, Char, Nodes) ->
    Children = maps:get(children, maps:get(State, Nodes)),
    case maps:find(Char, Children) of
        {ok, Id} -> Id;
        error -> find_fail(maps:get(fail, maps:get(State, Nodes)), Char, Nodes)
    end.

%% Scan target string and update DP
scan_target([], _Nodes, _LenMap, _CostMap, DP, _INF, _State, _Pos) ->
    DP;
scan_target([C|Rest], Nodes, LenMap, CostMap, DP0, INF, State0, Pos) ->
    %% transition in automaton
    NewState = transition(State0, C, Nodes),
    OutputIds = maps:get(output, maps:get(NewState, Nodes)),
    DP1 = lists:foldl(
        fun(Id, DPA) ->
                Len = maps:get(Id, LenMap),
                Cost = maps:get(Id, CostMap),
                PrevPos = Pos - Len,
                case array:get(PrevPos, DPA) of
                    PrevCost when PrevCost < INF ->
                        CurCost = array:get(Pos, DPA),
                        NewCost = PrevCost + Cost,
                        if NewCost < CurCost -> array:set(Pos, NewCost, DPA); true -> DPA end;
                    _ -> DPA
                end
        end,
        DP0,
        OutputIds),
    scan_target(Rest, Nodes, LenMap, CostMap, DP1, INF, NewState, Pos + 1).

transition(State, Char, Nodes) ->
    case maps:is_key(Char, maps:get(children, maps:get(State, Nodes))) of
        true -> maps:get(Char, maps:get(children, maps:get(State, Nodes)));
        false when State =:= 0 -> 0;
        false -> transition(maps:get(fail, maps:get(State, Nodes)), Char, Nodes)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(String.t(), [String.t()], [integer]) :: integer
  def minimum_cost(target, words, costs) do
    n = byte_size(target)
    inf = 1_000_000_000

    # ---------- Build Trie ----------
    {nodes, _next_id} =
      Enum.reduce(Enum.with_index(words), {%{0 => %{next: %{}, fail: 0, out: []}}, 1}, fn {{word, idx}, {trie, nid}},
                                                                                     do:
        cost = Enum.at(costs, idx)
        len = String.length(word)
        bytes = :binary.bin_to_list(word)

        {new_trie, new_nid, cur} =
          Enum.reduce(bytes, {trie, nid, 0}, fn b,
                                                {t, next_id, cur_node} ->
            case t[cur_node][:next][b] do
              nil ->
                child = next_id
                next_id = next_id + 1

                # update current node's next map
                cur_struct = t[cur_node]
                updated_cur = %{cur_struct | next: Map.put(cur_struct.next, b, child)}
                t = Map.put(t, cur_node, updated_cur)

                # add new child node
                t = Map.put(t, child, %{next: %{}, fail: 0, out: []})
                {t, next_id, child}

              child ->
                {t, next_id, child}
            end
          end)

        # add output to the terminal node
        term_struct = new_trie[cur]
        updated_term = %{term_struct | out: [{len, cost} | term_struct.out]}
        new_trie = Map.put(new_trie, cur, updated_term)
        {new_trie, new_nid}
      end)

    # ---------- Build Failure Links ----------
    go_fail = fn
      (state, ch, nodes) ->
        cond do
          Map.has_key?(nodes[state][:next], ch) -> nodes[state][:next][ch]
          state == 0 -> 0
          true -> go_fail.(nodes[state][:fail], ch, nodes)
        end
    end

    queue = :queue.from_list(Map.keys(nodes[0][:next]))
    nodes =
      Enum.reduce(Map.keys(nodes[0][:next]), nodes, fn child_id, acc ->
        Map.update!(acc, child_id, &%{&1 | fail: 0})
      end)

    {nodes, _} =
      :queue.fold(
        fn v, {trie, q} ->
          Enum.reduce(trie[v][:next], {trie, q}, fn {ch, child},
                                                  {t, qq} ->
            f = go_fail.(t[v][:fail], ch, t)
            child_struct = t[child]
            merged_out = child_struct.out ++ t[f].out
            t = Map.update!(t, child, fn _ -> %{child_struct | fail: f, out: merged_out} end)
            {t, :queue.in(child, qq)}
          end)
        end,
        {nodes, queue},
        fn {_v, acc}, _ -> acc end
      )

    # ---------- DP Scan ----------
    dp = :array.new(n + 1, default: inf) |> :array.set(0, 0)

    bytes = :binary.bin_to_list(target)

    {final_dp, _state} =
      Enum.reduce(Enum.with_index(bytes), {dp, 0}, fn {b, idx},
                                                    {dp_acc, state} ->
        i = idx + 1

        # transition
        new_state =
          cond do
            Map.has_key?(nodes[state][:next], b) -> nodes[state][:next][b]
            state == 0 -> 0
            true -> go_fail.(nodes[state][:fail], b, nodes)
          end

        dp_updated =
          Enum.reduce(nodes[new_state][:out], dp_acc, fn {len, cost}, dpar ->
            prev = :array.get(i - len, dpar)

            if prev < inf do
              cur = :array.get(i, dpar)
              newc = prev + cost

              if newc < cur, do: :array.set(i, newc, dpar), else: dpar
            else
              dpar
            end
          end)

        {dp_updated, new_state}
      end)

    ans = :array.get(n, final_dp)
    if ans >= inf, do: -1, else: ans
  end
end
```
