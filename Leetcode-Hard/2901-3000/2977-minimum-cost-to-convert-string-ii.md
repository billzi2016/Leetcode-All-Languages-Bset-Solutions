# 2977. Minimum Cost to Convert String II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct Match {int len; int id;};
    struct Node{
        int nxt[26];
        int id;
        Node(){fill(begin(nxt), end(nxt), -1); id=-1;}
    };
    
    long long minimumCost(string source, string target, vector<string>& original, vector<string>& changed, vector<int>& cost) {
        int n = source.size();
        // collect unique strings
        unordered_map<string,int> mp;
        vector<string> uniq;
        auto addStr=[&](const string& s){
            if(mp.find(s)==mp.end()){
                int id=uniq.size();
                mp[s]=id;
                uniq.push_back(s);
            }
        };
        for(const string& s: original) addStr(s);
        for(const string& s: changed) addStr(s);
        int m = uniq.size();
        const long long INF = (1LL<<60);
        vector<vector<long long>> dist(m, vector<long long>(m, INF));
        for(int i=0;i<m;i++) dist[i][i]=0;
        for(size_t i=0;i<original.size();++i){
            int u=mp[original[i]];
            int v=mp[changed[i]];
            dist[u][v]=min(dist[u][v], (long long)cost[i]);
        }
        // Floyd-Warshall
        for(int k=0;k<m;++k)
            for(int i=0;i<m;++i) if(dist[i][k]!=INF)
                for(int j=0;j<m;++j) if(dist[k][j]!=INF)
                    dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j]);
        // build trie
        vector<Node> trie(1);
        auto insertTrie=[&](const string& s, int id){
            int node=0;
            for(char ch: s){
                int c=ch-'a';
                if(trie[node].nxt[c]==-1){
                    trie[node].nxt[c]=trie.size();
                    trie.emplace_back();
                }
                node=trie[node].nxt[c];
            }
            trie[node].id=id;
        };
        for(int i=0;i<m;++i) insertTrie(uniq[i], i);
        // matches
        vector<vector<Match>> srcMatches(n), tgtMatches(n);
        for(int i=0;i<n;++i){
            int node=0;
            for(int j=i;j<n;++j){
                int c=source[j]-'a';
                if(trie[node].nxt[c]==-1) break;
                node=trie[node].nxt[c];
                if(trie[node].id!=-1){
                    srcMatches[i].push_back({j-i+1, trie[node].id});
                }
            }
        }
        for(int i=0;i<n;++i){
            int node=0;
            for(int j=i;j<n;++j){
                int c=target[j]-'a';
                if(trie[node].nxt[c]==-1) break;
                node=trie[node].nxt[c];
                if(trie[node].id!=-1){
                    tgtMatches[i].push_back({j-i+1, trie[node].id});
                }
            }
        }
        // DP
        vector<long long> dp(n+1, INF);
        dp[0]=0;
        for(int i=0;i<n;++i){
            if(dp[i]==INF) continue;
            // keep character unchanged
            if(source[i]==target[i]){
                dp[i+1]=min(dp[i+1], dp[i]);
            }
            // intervals starting at i
            for(const Match& sm: srcMatches[i]){
                int len=sm.len;
                int j=i+len;
                if(j>n) continue;
                for(const Match& tm: tgtMatches[i]){
                    if(tm.len!=len) continue;
                    long long c = dist[sm.id][tm.id];
                    if(c==INF) continue;
                    dp[j]=min(dp[j], dp[i]+c);
                }
            }
        }
        return dp[n]==INF ? -1 : dp[n];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long minimumCost(String source, String target, String[] original, String[] changed, int[] cost) {
        int n = source.length();
        // Map each unique string to an id
        HashMap<String, Integer> idMap = new HashMap<>();
        for (String s : original) {
            if (!idMap.containsKey(s)) idMap.put(s, idMap.size());
        }
        for (String s : changed) {
            if (!idMap.containsKey(s)) idMap.put(s, idMap.size());
        }
        int m = idMap.size();
        long INF = Long.MAX_VALUE / 4;
        long[][] dist = new long[m][m];
        for (int i = 0; i < m; i++) Arrays.fill(dist[i], INF);
        for (int i = 0; i < m; i++) dist[i][i] = 0;
        // edges
        for (int i = 0; i < original.length; i++) {
            int u = idMap.get(original[i]);
            int v = idMap.get(changed[i]);
            long c = cost[i];
            if (c < dist[u][v]) dist[u][v] = c;
        }
        // Floyd-Warshall
        for (int k = 0; k < m; k++) {
            for (int i = 0; i < m; i++) {
                if (dist[i][k] == INF) continue;
                for (int j = 0; j < m; j++) {
                    long nd = dist[i][k] + dist[k][j];
                    if (nd < dist[i][j]) dist[i][j] = nd;
                }
            }
        }

        // Precompute ids of substrings in source and target
        int[][] srcId = new int[n][n];
        int[][] tgtId = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(srcId[i], -1);
            Arrays.fill(tgtId[i], -1);
        }
        for (Map.Entry<String, Integer> e : idMap.entrySet()) {
            String s = e.getKey();
            int len = s.length();
            if (len > n) continue;
            int sid = e.getValue();
            // source occurrences
            for (int start = 0; start + len <= n; start++) {
                if (source.regionMatches(start, s, 0, len)) {
                    srcId[start][start + len - 1] = sid;
                }
            }
            // target occurrences
            for (int start = 0; start + len <= n; start++) {
                if (target.regionMatches(start, s, 0, len)) {
                    tgtId[start][start + len - 1] = sid;
                }
            }
        }

        long[] dp = new long[n + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            // keep last character unchanged if possible
            if (source.charAt(i - 1) == target.charAt(i - 1) && dp[i - 1] != INF) {
                dp[i] = Math.min(dp[i], dp[i - 1]);
            }
            for (int j = 0; j < i; j++) {
                int sid = srcId[j][i - 1];
                if (sid == -1) continue;
                int tid = tgtId[j][i - 1];
                if (tid == -1) continue;
                long d = dist[sid][tid];
                if (d >= INF / 2) continue;
                if (dp[j] != INF) {
                    dp[i] = Math.min(dp[i], dp[j] + d);
                }
            }
        }
        return dp[n] >= INF / 2 ? -1 : dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        INF = 10**18

        # collect unique strings from original and changed
        uniq = {}
        idx = 0
        for s in original + changed:
            if s not in uniq:
                uniq[s] = idx
                idx += 1
        m = len(uniq)

        # distance matrix
        dist = [[INF] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0

        # direct edges
        for o, c, w in zip(original, changed, cost):
            u = uniq[o]
            v = uniq[c]
            if w < dist[u][v]:
                dist[u][v] = w

        # Floyd-Warshall
        for k in range(m):
            dk = dist[k]
            for i in range(m):
                di = dist[i]
                ik = di[k]
                if ik == INF:
                    continue
                for j in range(m):
                    nd = ik + dk[j]
                    if nd < di[j]:
                        di[j] = nd

        n = len(source)
        dp = [INF] * (n + 1)
        dp[0] = 0

        # precompute list of strings and their lengths for iteration
        str_list = list(uniq.items())  # (string, id)

        for i in range(1, n + 1):
            # keep character if already equal
            if source[i - 1] == target[i - 1]:
                dp[i] = min(dp[i], dp[i - 1])

            # try all possible substrings ending at i
            for s_str, sid in str_list:
                L = len(s_str)
                j = i - L
                if j < 0:
                    continue
                if source[j:i] != s_str:
                    continue
                t_str = target[j:i]
                tid = uniq.get(t_str)
                if tid is None:
                    continue
                cst = dist[sid][tid]
                if cst >= INF:
                    continue
                if dp[j] + cst < dp[i]:
                    dp[i] = dp[j] + cst

        return -1 if dp[n] >= INF else dp[n]
```

## Python3

```python
class Solution:
    def minimumCost(self, source: str, target: str, original, changed, cost):
        from math import inf
        n = len(source)
        # map unique strings to ids
        uniq = {}
        idx = 0
        for s in original + changed:
            if s not in uniq:
                uniq[s] = idx
                idx += 1
        k = idx
        # distance matrix
        INF = 10**18
        dist = [[INF] * k for _ in range(k)]
        for i in range(k):
            dist[i][i] = 0
        # set direct edges (keep minimal cost if multiple)
        for o, c, w in zip(original, changed, cost):
            u = uniq[o]
            v = uniq[c]
            if w < dist[u][v]:
                dist[u][v] = w
        # Floyd-Warshall
        for m in range(k):
            dm = dist[m]
            for i in range(k):
                di = dist[i]
                im = di[m]
                if im == INF:
                    continue
                for j in range(k):
                    nd = im + dm[j]
                    if nd < di[j]:
                        di[j] = nd
        # group lengths of unique strings
        length_set = set()
        for s in uniq.keys():
            length_set.add(len(s))
        lengths = list(length_set)
        # dp
        dp = [INF] * (n + 1)
        dp[0] = 0
        str_to_idx = uniq  # alias
        for i in range(1, n + 1):
            # keep last character if already equal
            if source[i - 1] == target[i - 1]:
                dp[i] = dp[i - 1]
            # try all segment lengths
            for L in lengths:
                j = i - L
                if j < 0:
                    continue
                s_sub = source[j:i]
                t_sub = target[j:i]
                u = str_to_idx.get(s_sub)
                v = str_to_idx.get(t_sub)
                if u is None or v is None:
                    continue
                d = dist[u][v]
                if d >= INF:
                    continue
                cand = dp[j] + d
                if cand < dp[i]:
                    dp[i] = cand
        return -1 if dp[n] >= INF else dp[n]
```

## C

```c
#include <stdio.h>
#include <string.h>
#include <limits.h>

#define MAXM 200          // max unique strings (original + changed)
#define MAXN 1005         // max length of source/target
#define INF_LL ((long long)4e18)

typedef struct {
    int next[26];
    int strId;
} TrieNode;

static TrieNode trie[MAXM * 1000 + 5];
static int trieSize;

int getTrieNode() {
    int id = trieSize++;
    for (int i = 0; i < 26; ++i) trie[id].next[i] = -1;
    trie[id].strId = -1;
    return id;
}

void insertTrie(const char *s, int id) {
    int node = 0;
    for (int i = 0; s[i]; ++i) {
        int c = s[i] - 'a';
        if (trie[node].next[c] == -1) {
            trie[node].next[c] = getTrieNode();
        }
        node = trie[node].next[c];
    }
    trie[node].strId = id;
}

int getStringId(const char *s, const char **list, int *cnt) {
    for (int i = 0; i < *cnt; ++i) {
        if (strcmp(list[i], s) == 0) return i;
    }
    list[*cnt] = s;
    (*cnt)++;
    return *cnt - 1;
}

long long minimumCost(char* source, char* target, char** original, int originalSize,
                      char** changed, int changedSize, int* cost, int costSize) {
    const char *uniqueStr[MAXM];
    int uniqCnt = 0;

    // assign ids to all unique strings
    for (int i = 0; i < originalSize; ++i) {
        getStringId(original[i], uniqueStr, &uniqCnt);
        getStringId(changed[i], uniqueStr, &uniqCnt);
    }

    int K = uniqCnt;
    static long long dist[MAXM][MAXM];
    for (int i = 0; i < K; ++i) {
        for (int j = 0; j < K; ++j) {
            dist[i][j] = (i == j) ? 0 : INF_LL;
        }
    }

    // edges
    for (int i = 0; i < originalSize; ++i) {
        int u = -1, v = -1;
        for (int id = 0; id < K; ++id) if (strcmp(uniqueStr[id], original[i]) == 0) { u = id; break; }
        for (int id = 0; id < K; ++id) if (strcmp(uniqueStr[id], changed[i]) == 0) { v = id; break; }
        if (dist[u][v] > cost[i]) dist[u][v] = cost[i];
    }

    // Floyd-Warshall
    for (int m = 0; m < K; ++m)
        for (int i = 0; i < K; ++i) if (dist[i][m] < INF_LL)
            for (int j = 0; j < K; ++j)
                if (dist[m][j] < INF_LL && dist[i][j] > dist[i][m] + dist[m][j])
                    dist[i][j] = dist[i][m] + dist[m][j];

    // build trie with all unique strings
    trieSize = 0;
    getTrieNode(); // root at index 0
    for (int id = 0; id < K; ++id) {
        insertTrie(uniqueStr[id], id);
    }

    int n = strlen(source);
    static long long dp[MAXN];
    for (int i = 0; i <= n; ++i) dp[i] = INF_LL;
    dp[0] = 0;

    // base case of keeping equal characters
    for (int i = 1; i <= n; ++i) {
        if (source[i-1] == target[i-1]) dp[i] = dp[i-1];
    }

    // DP over intervals
    for (int start = 0; start < n; ++start) {
        int nodeS = 0, nodeT = 0;
        for (int end = start; end < n; ++end) {
            int cS = source[end] - 'a';
            if (trie[nodeS].next[cS] == -1) break;
            nodeS = trie[nodeS].next[cS];

            int cT = target[end] - 'a';
            if (trie[nodeT].next[cT] == -1) break;
            nodeT = trie[nodeT].next[cT];

            int idS = trie[nodeS].strId;
            int idT = trie[nodeT].strId;
            if (idS != -1 && idT != -1) {
                long long trans = dist[idS][idT];
                if (trans < INF_LL && dp[start] < INF_LL) {
                    long long cand = dp[start] + trans;
                    if (cand < dp[end+1]) dp[end+1] = cand;
                }
            }
        }
    }

    return (dp[n] >= INF_LL) ? -1 : dp[n];
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MinimumCost(string source, string target, string[] original, string[] changed, int[] cost) {
        int n = source.Length;
        const long INF = (long)4e18;

        // Map each unique string to an id
        var idMap = new Dictionary<string, int>();
        List<string> nodes = new List<string>();

        int GetId(string s) {
            if (!idMap.TryGetValue(s, out int id)) {
                id = nodes.Count;
                idMap[s] = id;
                nodes.Add(s);
            }
            return id;
        }

        // Build graph edges
        foreach (var s in original) GetId(s);
        foreach (var s in changed) GetId(s);
        int K = nodes.Count;

        long[,] dist = new long[K, K];
        for (int i = 0; i < K; i++) {
            for (int j = 0; j < K; j++) {
                dist[i, j] = (i == j) ? 0 : INF;
            }
        }

        for (int i = 0; i < original.Length; i++) {
            int u = idMap[original[i]];
            int v = idMap[changed[i]];
            long w = cost[i];
            if (w < dist[u, v]) dist[u, v] = w;
        }

        // Floyd-Warshall
        for (int k = 0; k < K; k++) {
            for (int i = 0; i < K; i++) {
                if (dist[i, k] == INF) continue;
                for (int j = 0; j < K; j++) {
                    if (dist[k, j] == INF) continue;
                    long nd = dist[i, k] + dist[k, j];
                    if (nd < dist[i, j]) dist[i, j] = nd;
                }
            }
        }

        // Precompute substring ids for source and target
        int[][] srcId = new int[n][];
        int[][] tgtId = new int[n][];
        for (int i = 0; i < n; i++) {
            srcId[i] = new int[n + 1];
            tgtId[i] = new int[n + 1];
            for (int j = 0; j <= n; j++) {
                srcId[i][j] = -1;
                tgtId[i][j] = -1;
            }
        }

        ReadOnlySpan<char> srcSpan = source.AsSpan();
        ReadOnlySpan<char> tgtSpan = target.AsSpan();

        for (int id = 0; id < K; id++) {
            string str = nodes[id];
            int len = str.Length;
            if (len > n) continue;
            var sSpan = str.AsSpan();

            // source
            for (int start = 0; start + len <= n; start++) {
                if (srcSpan.Slice(start, len).SequenceEqual(sSpan)) {
                    srcId[start][start + len] = id;
                }
            }

            // target
            for (int start = 0; start + len <= n; start++) {
                if (tgtSpan.Slice(start, len).SequenceEqual(sSpan)) {
                    tgtId[start][start + len] = id;
                }
            }
        }

        // DP over prefixes
        long[] dp = new long[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = INF;
        dp[0] = 0;

        for (int i = 1; i <= n; i++) {
            // keep character if already equal
            if (source[i - 1] == target[i - 1] && dp[i - 1] != INF) {
                dp[i] = Math.Min(dp[i], dp[i - 1]);
            }

            for (int j = 0; j < i; j++) {
                int sid = srcId[j][i];
                if (sid == -1) continue;
                int tid = tgtId[j][i];
                if (tid == -1) continue;
                long segCost = dist[sid, tid];
                if (segCost == INF || dp[j] == INF) continue;
                long cand = dp[j] + segCost;
                if (cand < dp[i]) dp[i] = cand;
            }
        }

        return dp[n] == INF ? -1 : dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} source
 * @param {string} target
 * @param {string[]} original
 * @param {string[]} changed
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function(source, target, original, changed, cost) {
    const n = source.length;
    // map each unique string to an id
    const idMap = new Map();
    let idx = 0;
    const addString = (s) => {
        if (!idMap.has(s)) {
            idMap.set(s, idx++);
        }
    };
    for (let s of original) addString(s);
    for (let s of changed) addString(s);
    const m = idx; // number of nodes

    const INF = 1e18;
    const dist = Array.from({ length: m }, () => Array(m).fill(INF));
    for (let i = 0; i < m; ++i) dist[i][i] = 0;

    for (let i = 0; i < original.length; ++i) {
        const u = idMap.get(original[i]);
        const v = idMap.get(changed[i]);
        if (cost[i] < dist[u][v]) dist[u][v] = cost[i];
    }

    // Floyd-Warshall
    for (let k = 0; k < m; ++k) {
        for (let i = 0; i < m; ++i) {
            if (dist[i][k] === INF) continue;
            const dik = dist[i][k];
            for (let j = 0; j < m; ++j) {
                const nd = dik + dist[k][j];
                if (nd < dist[i][j]) dist[i][j] = nd;
            }
        }
    }

    // collect distinct lengths of strings in the map
    const lengthSet = new Set();
    for (let s of idMap.keys()) {
        lengthSet.add(s.length);
    }
    const lengths = Array.from(lengthSet);

    const dp = new Array(n + 1).fill(INF);
    dp[0] = 0;

    for (let i = 1; i <= n; ++i) {
        // option: keep last character unchanged
        if (source[i - 1] === target[i - 1] && dp[i - 1] < INF) {
            dp[i] = Math.min(dp[i], dp[i - 1]);
        }
        // try all possible segment lengths ending at i-1
        for (let len of lengths) {
            const j = i - len;
            if (j < 0) continue;
            const subS = source.slice(j, i);
            const subT = target.slice(j, i);
            const idS = idMap.get(subS);
            const idT = idMap.get(subT);
            if (idS === undefined || idT === undefined) continue;
            const d = dist[idS][idT];
            if (d === INF) continue;
            if (dp[j] + d < dp[i]) {
                dp[i] = dp[j] + d;
            }
        }
    }

    return dp[n] >= INF ? -1 : dp[n];
};
```

## Typescript

```typescript
function minimumCost(source: string, target: string, original: string[], changed: string[], cost: number[]): number {
    const n = source.length;
    // Assign unique IDs to all strings appearing in original or changed
    const strToId = new Map<string, number>();
    const idToStr: string[] = [];
    function getId(s: string): number {
        let id = strToId.get(s);
        if (id === undefined) {
            id = idToStr.length;
            strToId.set(s, id);
            idToStr.push(s);
        }
        return id;
    }
    const m = original.length;
    for (let i = 0; i < m; ++i) {
        getId(original[i]);
        getId(changed[i]);
    }
    const k = idToStr.length;
    const INF = 1e18;

    // distance matrix
    const dist: number[][] = Array.from({ length: k }, () => Array(k).fill(INF));
    for (let i = 0; i < k; ++i) dist[i][i] = 0;
    for (let i = 0; i < m; ++i) {
        const u = strToId.get(original[i])!;
        const v = strToId.get(changed[i])!;
        if (cost[i] < dist[u][v]) dist[u][v] = cost[i];
    }

    // Floyd-Warshall to get minimal conversion costs between any two strings
    for (let mid = 0; mid < k; ++mid) {
        for (let i = 0; i < k; ++i) {
            if (dist[i][mid] === INF) continue;
            const via = dist[i][mid];
            for (let j = 0; j < k; ++j) {
                const nd = via + dist[mid][j];
                if (nd < dist[i][j]) dist[i][j] = nd;
            }
        }
    }

    // collect distinct lengths of strings we care about
    const lengthSet = new Set<number>();
    for (const s of idToStr) lengthSet.add(s.length);
    const lengths = Array.from(lengthSet);

    const dp: number[] = new Array(n + 1).fill(INF);
    dp[0] = 0;

    for (let i = 1; i <= n; ++i) {
        // option: keep current character if already equal
        if (source[i - 1] === target[i - 1]) {
            dp[i] = Math.min(dp[i], dp[i - 1]);
        }
        // try all possible segment lengths ending at i
        for (const len of lengths) {
            if (len > i) continue;
            const j = i - len;
            const sSub = source.substring(j, i);
            const tSub = target.substring(j, i);
            const sid = strToId.get(sSub);
            const tid = strToId.get(tSub);
            if (sid !== undefined && tid !== undefined) {
                const convCost = dist[sid][tid];
                if (convCost < INF && dp[j] < INF) {
                    const cand = dp[j] + convCost;
                    if (cand < dp[i]) dp[i] = cand;
                }
            }
        }
    }

    return dp[n] >= INF ? -1 : dp[n];
}
```

## Php

```php
class Solution {
    /**
     * @param String $source
     * @param String $target
     * @param String[] $original
     * @param String[] $changed
     * @param Integer[] $cost
     * @return Integer
     */
    function minimumCost($source, $target, $original, $changed, $cost) {
        $n = strlen($source);
        // assign ids to all unique strings in original and changed
        $idMap = [];
        $cnt = 0;
        $m = count($original);
        for ($i = 0; $i < $m; ++$i) {
            if (!isset($idMap[$original[$i]])) {
                $idMap[$original[$i]] = $cnt++;
            }
            if (!isset($idMap[$changed[$i]])) {
                $idMap[$changed[$i]] = $cnt++;
            }
        }
        $k = $cnt;
        $INF = 10**15;
        // distance matrix
        $dist = array_fill(0, $k, array_fill(0, $k, $INF));
        for ($i = 0; $i < $k; ++$i) {
            $dist[$i][$i] = 0;
        }
        for ($i = 0; $i < $m; ++$i) {
            $u = $idMap[$original[$i]];
            $v = $idMap[$changed[$i]];
            if ($cost[$i] < $dist[$u][$v]) {
                $dist[$u][$v] = $cost[$i];
            }
        }
        // Floyd‑Warshall
        for ($mid = 0; $mid < $k; ++$mid) {
            for ($i = 0; $i < $k; ++$i) {
                if ($dist[$i][$mid] == $INF) continue;
                $ik = $dist[$i][$mid];
                for ($j = 0; $j < $k; ++$j) {
                    $new = $ik + $dist[$mid][$j];
                    if ($new < $dist[$i][$j]) {
                        $dist[$i][$j] = $new;
                    }
                }
            }
        }

        // build trie for all strings (both original and changed)
        $root = ['next' => [], 'id' => -1];
        foreach ($idMap as $str => $sid) {
            $node =& $root;
            $len = strlen($str);
            for ($p = 0; $p < $len; ++$p) {
                $c = $str[$p];
                if (!isset($node['next'][$c])) {
                    $node['next'][$c] = ['next' => [], 'id' => -1];
                }
                $node =& $node['next'][$c];
            }
            $node['id'] = $sid;
            unset($node);
        }

        // DP over prefixes
        $dp = array_fill(0, $n + 1, $INF);
        $dp[0] = 0;

        for ($j = 0; $j < $n; ++$j) {
            if ($dp[$j] == $INF) continue;
            // single character equality
            if ($source[$j] === $target[$j]) {
                if ($dp[$j] < $dp[$j + 1]) $dp[$j + 1] = $dp[$j];
            }
            $nodeS =& $root;
            $nodeT =& $root;
            for ($i = $j; $i < $n; ++$i) {
                $cS = $source[$i];
                $cT = $target[$i];
                if (!isset($nodeS['next'][$cS]) || !isset($nodeT['next'][$cT])) break;
                $nodeS =& $nodeS['next'][$cS];
                $nodeT =& $nodeT['next'][$cT];
                $srcId = $nodeS['id'];
                $tgtId = $nodeT['id'];
                if ($srcId != -1 && $tgtId != -1) {
                    $costPath = $dist[$srcId][$tgtId];
                    if ($costPath < $INF) {
                        $newCost = $dp[$j] + $costPath;
                        if ($newCost < $dp[$i + 1]) {
                            $dp[$i + 1] = $newCost;
                        }
                    }
                }
            }
            unset($nodeS);
            unset($nodeT);
        }

        return $dp[$n] == $INF ? -1 : (int)$dp[$n];
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    struct TrieNode {
        var next: [Int] = Array(repeating: -1, count: 26)
        var id: Int = -1
    }
    
    func minimumCost(_ source: String, _ target: String, _ original: [String], _ changed: [String], _ cost: [Int]) -> Int {
        let n = source.count
        if n != target.count { return -1 }
        // Map each unique string to an id
        var strToId = [String:Int]()
        var strings = [String]()
        func getId(_ s: String) -> Int {
            if let v = strToId[s] { return v }
            let id = strings.count
            strToId[s] = id
            strings.append(s)
            return id
        }
        let m = original.count
        for i in 0..<m {
            _ = getId(original[i])
            _ = getId(changed[i])
        }
        let k = strings.count
        let INF: Int64 = 1_000_000_000_000_000 // large enough
        
        var dist = Array(repeating: Array(repeating: INF, count: k), count: k)
        for i in 0..<k { dist[i][i] = 0 }
        for i in 0..<m {
            let u = strToId[original[i]]!
            let v = strToId[changed[i]]!
            let c = Int64(cost[i])
            if c < dist[u][v] {
                dist[u][v] = c
            }
        }
        // Floyd-Warshall
        for p in 0..<k {
            for i in 0..<k where dist[i][p] < INF {
                let via = dist[i][p]
                for j in 0..<k where dist[p][j] < INF {
                    let nd = via + dist[p][j]
                    if nd < dist[i][j] {
                        dist[i][j] = nd
                    }
                }
            }
        }
        
        // Build Trie of all known strings
        var trie = [TrieNode()]
        func insert(_ s: String, _ id: Int) {
            var nodeIdx = 0
            for ch in s.utf8 {
                let idx = Int(ch - 97)
                if trie[nodeIdx].next[idx] == -1 {
                    trie.append(TrieNode())
                    trie[nodeIdx].next[idx] = trie.count - 1
                }
                nodeIdx = trie[nodeIdx].next[idx]
            }
            trie[nodeIdx].id = id
        }
        for (idx, s) in strings.enumerated() {
            insert(s, idx)
        }
        
        // Convert source and target to byte arrays
        let srcBytes = Array(source.utf8)
        let tgtBytes = Array(target.utf8)
        
        // Precompute matches: for each start position, list of (len, id)
        var srcMatches = [[(Int, Int)]](repeating: [], count: n)
        var tgtMatches = [[(Int, Int)]](repeating: [], count: n)
        func computeMatches(_ bytes: [UInt8], _ matches: inout [[(Int, Int)]]) {
            for start in 0..<n {
                var nodeIdx = 0
                var pos = start
                while pos < n {
                    let idx = Int(bytes[pos] - 97)
                    let nextIdx = trie[nodeIdx].next[idx]
                    if nextIdx == -1 { break }
                    nodeIdx = nextIdx
                    if trie[nodeIdx].id != -1 {
                        matches[start].append((pos - start + 1, trie[nodeIdx].id))
                    }
                    pos += 1
                }
            }
        }
        computeMatches(srcBytes, &srcMatches)
        computeMatches(tgtBytes, &tgtMatches)
        
        // DP over prefixes
        var dp = [Int64](repeating: INF, count: n + 1)
        dp[0] = 0
        for i in 1...n {
            // single character keep if equal
            if srcBytes[i-1] == tgtBytes[i-1] && dp[i-1] < dp[i] {
                dp[i] = dp[i-1]
            }
            // consider intervals ending at i
            for j in 0..<i {
                let len = i - j
                var sId: Int? = nil
                for (l, id) in srcMatches[j] where l == len {
                    sId = id
                    break
                }
                if sId == nil { continue }
                var tId: Int? = nil
                for (l, id) in tgtMatches[j] where l == len {
                    tId = id
                    break
                }
                if tId == nil { continue }
                let costConv = dist[sId!][tId!]
                if costConv >= INF/2 { continue }
                let cand = dp[j] + costConv
                if cand < dp[i] {
                    dp[i] = cand
                }
            }
        }
        return dp[n] >= INF/2 ? -1 : Int(dp[n])
    }
}
```

## Kotlin

```kotlin
import java.util.HashMap
import kotlin.math.min

class Solution {
    fun minimumCost(
        source: String,
        target: String,
        original: Array<String>,
        changed: Array<String>,
        cost: IntArray
    ): Long {
        val n = source.length
        // map each unique string to an id
        val idMap = HashMap<String, Int>()
        val nodes = mutableListOf<String>()
        fun getId(s: String): Int {
            return idMap.getOrPut(s) {
                nodes.add(s)
                nodes.size - 1
            }
        }

        val m = original.size
        for (i in 0 until m) {
            getId(original[i])
            getId(changed[i])
        }
        val v = nodes.size
        val INF = Long.MAX_VALUE / 4

        // distance matrix
        val dist = Array(v) { LongArray(v) { INF } }
        for (i in 0 until v) dist[i][i] = 0L
        for (i in 0 until m) {
            val u = idMap[original[i]]!!
            val w = idMap[changed[i]]!!
            val c = cost[i].toLong()
            if (c < dist[u][w]) dist[u][w] = c
        }

        // Floyd-Warshall
        for (k in 0 until v) {
            for (i in 0 until v) {
                val dik = dist[i][k]
                if (dik == INF) continue
                for (j in 0 until v) {
                    val dkj = dist[k][j]
                    if (dkj == INF) continue
                    val nd = dik + dkj
                    if (nd < dist[i][j]) dist[i][j] = nd
                }
            }
        }

        // precompute matches of each node string in source and target at every start position
        val srcMatches = Array(n) { mutableListOf<Int>() }
        val tgtMatches = Array(n) { mutableListOf<Int>() }

        for (id in 0 until v) {
            val str = nodes[id]
            val len = str.length
            if (len > n) continue
            var pos = 0
            while (pos + len <= n) {
                if (source.regionMatches(pos, str, 0, len)) srcMatches[pos].add(id)
                if (target.regionMatches(pos, str, 0, len)) tgtMatches[pos].add(id)
                pos++
            }
        }

        // DP over prefixes
        val dp = LongArray(n + 1) { INF }
        dp[0] = 0L
        for (i in 1..n) {
            // keep character unchanged
            if (source[i - 1] == target[i - 1] && dp[i - 1] != INF) {
                dp[i] = min(dp[i], dp[i - 1])
            }
            // consider intervals ending at i
            for (j in 0 until i) {
                val len = i - j
                if (dp[j] == INF) continue
                for (sId in srcMatches[j]) {
                    if (nodes[sId].length != len) continue
                    val row = dist[sId]
                    for (tId in tgtMatches[j]) {
                        if (nodes[tId].length != len) continue
                        val segCost = row[tId]
                        if (segCost == INF) continue
                        val newCost = dp[j] + segCost
                        if (newCost < dp[i]) dp[i] = newCost
                    }
                }
            }
        }

        return if (dp[n] == INF) -1L else dp[n]
    }
}
```

## Dart

```dart
class Solution {
  int minimumCost(String source, String target, List<String> original,
      List<String> changed, List<int> cost) {
    const int INF = 1 << 60;

    // Assign unique ids to all strings appearing in original or changed
    final Map<String, int> idMap = {};
    final List<String> idToStr = [];

    void addString(String s) {
      if (!idMap.containsKey(s)) {
        idMap[s] = idToStr.length;
        idToStr.add(s);
      }
    }

    for (int i = 0; i < original.length; ++i) {
      addString(original[i]);
      addString(changed[i]);
    }

    final int sz = idToStr.length;
    // Initialize distance matrix
    List<List<int>> dist =
        List.generate(sz, (_) => List.filled(sz, INF), growable: false);
    for (int i = 0; i < sz; ++i) {
      dist[i][i] = 0;
    }
    for (int i = 0; i < original.length; ++i) {
      int u = idMap[original[i]]!;
      int v = idMap[changed[i]]!;
      if (cost[i] < dist[u][v]) dist[u][v] = cost[i];
    }

    // Floyd-Warshall
    for (int k = 0; k < sz; ++k) {
      for (int i = 0; i < sz; ++i) {
        if (dist[i][k] == INF) continue;
        int ik = dist[i][k];
        for (int j = 0; j < sz; ++j) {
          int kj = dist[k][j];
          if (kj == INF) continue;
          int nd = ik + kj;
          if (nd < dist[i][j]) dist[i][j] = nd;
        }
      }
    }

    int n = source.length;

    // Precompute ids for all substrings of source and target
    List<List<int>> srcId =
        List.generate(n, (_) => List.filled(n + 1, -1), growable: false);
    List<List<int>> tgtId =
        List.generate(n, (_) => List.filled(n + 1, -1), growable: false);

    for (int start = 0; start < n; ++start) {
      for (int end = start + 1; end <= n; ++end) {
        String subS = source.substring(start, end);
        srcId[start][end] = idMap[subS] ?? -1;
        String subT = target.substring(start, end);
        tgtId[start][end] = idMap[subT] ?? -1;
      }
    }

    // DP over prefix
    List<int> dp = List.filled(n + 1, INF, growable: false);
    dp[0] = 0;

    for (int i = 1; i <= n; ++i) {
      // Keep character if already equal
      if (source[i - 1] == target[i - 1] && dp[i - 1] != INF) {
        dp[i] = dp[i - 1];
      }
      // Try converting a segment [j, i)
      for (int j = 0; j < i; ++j) {
        int sid = srcId[j][i];
        int tid = tgtId[j][i];
        if (sid == -1 || tid == -1) continue;
        int segCost = dist[sid][tid];
        if (segCost == INF) continue;
        if (dp[j] == INF) continue;
        int cand = dp[j] + segCost;
        if (cand < dp[i]) dp[i] = cand;
      }
    }

    return dp[n] == INF ? -1 : dp[n];
  }
}
```

## Golang

```go
package main

import (
	"math"
)

func minimumCost(source string, target string, original []string, changed []string, cost []int) int64 {
	const INF int64 = 1 << 60
	n := len(source)

	// assign ids to unique strings from original and changed
	str2id := make(map[string]int)
	idCnt := 0
	addStr := func(s string) {
		if _, ok := str2id[s]; !ok {
			str2id[s] = idCnt
			idCnt++
		}
	}
	for _, s := range original {
		addStr(s)
	}
	for _, s := range changed {
		addStr(s)
	}

	K := idCnt
	// distance matrix
	dist := make([][]int64, K)
	for i := 0; i < K; i++ {
		row := make([]int64, K)
		for j := 0; j < K; j++ {
			if i == j {
				row[j] = 0
			} else {
				row[j] = INF
			}
		}
		dist[i] = row
	}

	m := len(original)
	for i := 0; i < m; i++ {
		u := str2id[original[i]]
		v := str2id[changed[i]]
		w := int64(cost[i])
		if w < dist[u][v] {
			dist[u][v] = w
		}
	}

	// Floyd-Warshall
	for k := 0; k < K; k++ {
		for i := 0; i < K; i++ {
			if dist[i][k] == INF {
				continue
			}
			ik := dist[i][k]
			for j := 0; j < K; j++ {
				if dist[k][j] == INF {
					continue
				}
				if ik+dist[k][j] < dist[i][j] {
					dist[i][j] = ik + dist[k][j]
				}
			}
		}
	}

	// precompute ids for all substrings of source and target that exist in map
	srcId := make([][]int, n)
	tgtId := make([][]int, n)
	for i := 0; i < n; i++ {
		srcRow := make([]int, n+1)
		tgtRow := make([]int, n+1)
		for j := i + 1; j <= n; j++ {
			if id, ok := str2id[source[i:j]]; ok {
				srcRow[j] = id
			} else {
				srcRow[j] = -1
			}
			if id, ok := str2id[target[i:j]]; ok {
				tgtRow[j] = id
			} else {
				tgtRow[j] = -1
			}
		}
		srcId[i] = srcRow
		tgtId[i] = tgtRow
	}

	dp := make([]int64, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = INF
	}
	dp[0] = 0

	for i := 1; i <= n; i++ {
		// case: keep character if already equal
		if source[i-1] == target[i-1] && dp[i-1] < dp[i] {
			dp[i] = dp[i-1]
		}
		// try all possible previous split points
		for j := 0; j < i; j++ {
			sid := srcId[j][i]
			tid := tgtId[j][i]
			if sid == -1 || tid == -1 {
				continue
			}
			costVal := dist[sid][tid]
			if costVal == INF {
				continue
			}
			if dp[j]+costVal < dp[i] {
				dp[i] = dp[j] + costVal
			}
		}
	}

	if dp[n] >= INF/2 {
		return -1
	}
	return dp[n]
}
```

## Ruby

```ruby
def minimum_cost(source, target, original, changed, cost)
  n = source.length
  src_bytes = source.bytes
  tgt_bytes = target.bytes

  # Assign unique ids to all strings appearing in original or changed
  id_map = {}
  strings = []
  original.each_with_index do |s, idx|
    unless id_map.key?(s)
      id_map[s] = strings.size
      strings << s
    end
    c = changed[idx]
    unless id_map.key?(c)
      id_map[c] = strings.size
      strings << c
    end
  end

  m = strings.size
  inf = (1 << 60)

  # distance matrix
  dist = Array.new(m) { Array.new(m, inf) }
  m.times { |i| dist[i][i] = 0 }

  original.each_with_index do |s, idx|
    o_id = id_map[s]
    c_id = id_map[changed[idx]]
    w = cost[idx]
    dist[o_id][c_id] = w if w < dist[o_id][c_id]
  end

  # Floyd-Warshall
  m.times do |k|
    m.times do |i|
      next if dist[i][k] == inf
      ik = dist[i][k]
      m.times do |j|
        nk = ik + dist[k][j]
        dist[i][j] = nk if nk < dist[i][j]
      end
    end
  end

  # Build trie of all known strings (by bytes)
  root = { children: {}, id: nil }
  strings.each_with_index do |str, idx|
    node = root
    str.bytes.each do |b|
      node[:children][b] ||= { children: {}, id: nil }
      node = node[:children][b]
    end
    node[:id] = idx
  end

  # Precompute matches ending at each position (1..n)
  src_matches = Array.new(n + 1) { [] }   # each element: [start, id]
  tgt_matches = Array.new(n + 1) { [] }

  n.times do |start|
    node = root
    pos = start
    while pos < n && (child = node[:children][src_bytes[pos]])
      node = child
      if node[:id]
        src_matches[pos + 1] << [start, node[:id]]
      end
      pos += 1
    end
  end

  n.times do |start|
    node = root
    pos = start
    while pos < n && (child = node[:children][tgt_bytes[pos]])
      node = child
      if node[:id]
        tgt_matches[pos + 1] << [start, node[:id]]
      end
      pos += 1
    end
  end

  dp = Array.new(n + 1, inf)
  dp[0] = 0

  (1..n).each do |i|
    # keep character if already equal
    if src_bytes[i - 1] == tgt_bytes[i - 1]
      dp[i] = dp[i - 1] if dp[i - 1] < dp[i]
    end

    s_list = src_matches[i]
    t_list = tgt_matches[i]
    next if s_list.empty? || t_list.empty?

    # compare each pair with same start
    s_list.each do |s_start, s_id|
      t_list.each do |t_start, t_id|
        next unless s_start == t_start
        conv = dist[s_id][t_id]
        next if conv >= inf
        cand = dp[s_start] + conv
        dp[i] = cand if cand < dp[i]
      end
    end
  end

  ans = dp[n]
  ans >= inf ? -1 : ans
end
```

## Scala

```scala
import scala.collection.mutable

object Solution {
  def minimumCost(source: String, target: String,
                  original: Array[String], changed: Array[String],
                  cost: Array[Int]): Long = {

    val n = source.length
    // assign unique ids to all strings appearing in original or changed
    val idMap = mutable.HashMap[String, Int]()
    var curId = 0
    for (s <- original ++ changed) {
      if (!idMap.contains(s)) {
        idMap(s) = curId
        curId += 1
      }
    }
    val k = curId
    val INF: Long = Long.MaxValue / 4

    // distance matrix
    val dist = Array.ofDim[Long](k, k)
    for (i <- 0 until k) {
      java.util.Arrays.fill(dist(i), INF)
      dist(i)(i) = 0L
    }
    for (i <- original.indices) {
      val u = idMap(original(i))
      val v = idMap(changed(i))
      val c = cost(i).toLong
      if (c < dist(u)(v)) dist(u)(v) = c
    }

    // Floyd-Warshall
    for (m <- 0 until k) {
      for (i <- 0 until k) {
        val dik = dist(i)(m)
        if (dik < INF) {
          var j = 0
          while (j < k) {
            val dkj = dist(m)(j)
            if (dkj < INF) {
              val nd = dik + dkj
              if (nd < dist(i)(j)) dist(i)(j) = nd
            }
            j += 1
          }
        }
      }
    }

    // maximum length of any string in the map
    var maxLen = 0
    for ((s, _) <- idMap) {
      if (s.length > maxLen) maxLen = s.length
    }

    // Trie node definition
    class Node {
      val next: Array[Node] = new Array[Node](26)
      var id: Int = -1
    }
    val root = new Node

    // insert all strings into trie
    for ((s, idx) <- idMap) {
      var cur = root
      for (ch <- s) {
        val c = ch - 'a'
        if (cur.next(c) == null) cur.next(c) = new Node
        cur = cur.next(c)
      }
      cur.id = idx
    }

    // matrices storing matching ids for substrings starting at each position
    val srcMat = Array.ofDim[Int](n, maxLen + 1)
    val tgtMat = Array.ofDim[Int](n, maxLen + 1)
    for (i <- 0 until n) {
      java.util.Arrays.fill(srcMat(i), -1)
      java.util.Arrays.fill(tgtMat(i), -1)
    }

    // fill source matrix
    for (start <- 0 until n) {
      var node: Node = root
      var pos = start
      while (pos < n) {
        val c = source.charAt(pos) - 'a'
        if (node.next(c) == null) {
          // no further match possible
          break()
        }
        node = node.next(c)
        if (node.id != -1) {
          val len = pos - start + 1
          srcMat(start)(len) = node.id
        }
        pos += 1
      }
    }

    // fill target matrix
    for (start <- 0 until n) {
      var node: Node = root
      var pos = start
      while (pos < n) {
        val c = target.charAt(pos) - 'a'
        if (node.next(c) == null) {
          break()
        }
        node = node.next(c)
        if (node.id != -1) {
          val len = pos - start + 1
          tgtMat(start)(len) = node.id
        }
        pos += 1
      }
    }

    // DP over prefixes
    val dp = Array.fill[Long](n + 1)(INF)
    dp(0) = 0L

    for (i <- 1 to n) {
      // keep character if already equal
      if (source.charAt(i - 1) == target.charAt(i - 1) && dp(i - 1) < INF) {
        dp(i) = dp(i - 1)
      }
      var j = 0
      while (j < i) {
        val len = i - j
        if (len <= maxLen) {
          val sid = srcMat(j)(len)
          if (sid != -1) {
            val tid = tgtMat(j)(len)
            if (tid != -1) {
              val d = dist(sid)(tid)
              if (d < INF && dp(j) < INF) {
                val cand = dp(j) + d
                if (cand < dp(i)) dp(i) = cand
              }
            }
          }
        }
        j += 1
      }
    }

    if (dp(n) >= INF) -1L else dp(n)
  }

  // utility to break out of while loops (since Scala lacks built-in break)
  private def break(): Unit = throw new scala.util.control.ControlThrowable {}
}
```

## Rust

```rust
use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn minimum_cost(
        source: String,
        target: String,
        original: Vec<String>,
        changed: Vec<String>,
        cost: Vec<i32>,
    ) -> i64 {
        let n = source.len();
        if n != target.len() {
            return -1;
        }
        // map each unique string to an id
        let mut id_map: HashMap<String, usize> = HashMap::new();
        for s in original.iter().chain(changed.iter()) {
            id_map.entry(s.clone()).or_insert_with(|| id_map.len());
        }
        let k = id_map.len();
        const INF_DIST: i64 = 1_i64 << 60;

        // distance matrix
        let mut dist = vec![vec![INF_DIST; k]; k];
        for i in 0..k {
            dist[i][i] = 0;
        }
        for (o, c, &co) in itertools::izip!(&original, &changed, &cost) {
            let u = id_map[o];
            let v = id_map[c];
            let w = co as i64;
            if w < dist[u][v] {
                dist[u][v] = w;
            }
        }

        // Floyd-Warshall
        for m in 0..k {
            for i in 0..k {
                if dist[i][m] == INF_DIST {
                    continue;
                }
                let via = dist[i][m];
                for j in 0..k {
                    if dist[m][j] == INF_DIST {
                        continue;
                    }
                    let nd = via + dist[m][j];
                    if nd < dist[i][j] {
                        dist[i][j] = nd;
                    }
                }
            }
        }

        // Build trie of all known strings
        #[derive(Clone)]
        struct Node {
            next: [i32; 26],
            id: i32,
        }
        impl Node {
            fn new() -> Self {
                Node {
                    next: [-1; 26],
                    id: -1,
                }
            }
        }

        let mut trie: Vec<Node> = vec![Node::new()];
        for (s, &idx) in id_map.iter() {
            let mut node = 0usize;
            for &b in s.as_bytes() {
                let c = (b - b'a') as usize;
                if trie[node].next[c] == -1 {
                    trie[node].next[c] = trie.len() as i32;
                    trie.push(Node::new());
                }
                node = trie[node].next[c] as usize;
            }
            trie[node].id = idx as i32;
        }

        // maximum length of known strings
        let max_len = id_map.keys().map(|s| s.len()).max().unwrap_or(0);

        // src_id[start][end] = id or -1, end is exclusive
        let mut src_id = vec![vec![-1i32; n + 1]; n];
        let mut tgt_id = vec![vec![-1i32; n + 1]; n];

        let src_bytes = source.as_bytes();
        let tgt_bytes = target.as_bytes();

        for start in 0..n {
            let mut node = 0usize;
            for end in start..std::cmp::min(n, start + max_len) {
                let c = (src_bytes[end] - b'a') as usize;
                let nxt = trie[node].next[c];
                if nxt == -1 {
                    break;
                }
                node = nxt as usize;
                let id = trie[node].id;
                if id != -1 {
                    src_id[start][end + 1] = id;
                }
            }
        }

        for start in 0..n {
            let mut node = 0usize;
            for end in start..std::cmp::min(n, start + max_len) {
                let c = (tgt_bytes[end] - b'a') as usize;
                let nxt = trie[node].next[c];
                if nxt == -1 {
                    break;
                }
                node = nxt as usize;
                let id = trie[node].id;
                if id != -1 {
                    tgt_id[start][end + 1] = id;
                }
            }
        }

        // DP over prefixes
        const INF: i64 = 1_i64 << 60;
        let mut dp = vec![INF; n + 1];
        dp[0] = 0;

        for i in 1..=n {
            // keep last character unchanged if possible
            if src_bytes[i - 1] == tgt_bytes[i - 1] && dp[i - 1] != INF {
                dp[i] = dp[i - 1];
            }
            // consider intervals ending at i
            for j in 0..i {
                let sid = src_id[j][i];
                if sid == -1 {
                    continue;
                }
                let tid = tgt_id[j][i];
                if tid == -1 {
                    continue;
                }
                let d = dist[sid as usize][tid as usize];
                if d == INF_DIST {
                    continue;
                }
                if dp[j] != INF && dp[j] + d < dp[i] {
                    dp[i] = dp[j] + d;
                }
            }
        }

        if dp[n] >= INF {
            -1
        } else {
            dp[n]
        }
    }
}

// itertools::izip! macro used; add dependency for compilation
// In LeetCode environment, we can replace with manual loops to avoid external crate.
// Below is a replacement without itertools:

#[allow(dead_code)]
mod itertools {
    pub fn izip<A, B, C>(a: A, b: B, c: C) -> Izip3<A::IntoIter, B::IntoIter, C::IntoIter>
    where
        A: IntoIterator,
        B: IntoIterator,
        C: IntoIterator,
    {
        Izip3 {
            a: a.into_iter(),
            b: b.into_iter(),
            c: c.into_iter(),
        }
    }

    pub struct Izip3<A, B, C> {
        a: A,
        b: B,
        c: C,
    }

    impl<A, B, C> Iterator for Izip3<A, B, C>
    where
        A: Iterator,
        B: Iterator,
        C: Iterator,
    {
        type Item = (A::Item, B::Item, C::Item);
        fn next(&mut self) -> Option<Self::Item> {
            match (self.a.next(), self.b.next(), self.c.next()) {
                (Some(x), Some(y), Some(z)) => Some((x, y, z)),
                _ => None,
            }
        }
    }
}
```

## Racket

```racket
(define (minimum-cost source target original changed cost)
  (define INF 1000000000000000)

  ;; assign ids to all unique strings in original and changed
  (define str->id (make-hash))
  (define (add-string s)
    (unless (hash-has-key? str->id s)
      (hash-set! str->id s (hash-count str->id))))
  (for ([s original]) (add-string s))
  (for ([s changed]) (add-string s))

  (define k (hash-count str->id))
  ;; distance matrix
  (define dist (make-vector k #f))
  (for ([i k])
    (define row (make-vector k INF))
    (vector-set! row i 0)
    (vector-set! dist i row))

  ;; set direct edges
  (let loop ((idx 0) (len (length original)))
    (when (< idx len)
      (define u (hash-ref str->id (list-ref original idx)))
      (define v (hash-ref str->id (list-ref changed idx)))
      (define c (list-ref cost idx))
      (define cur (vector-ref (vector-ref dist u) v))
      (when (< c cur)
        (vector-set! (vector-ref dist u) v c))
      (loop (+ idx 1) len)))

  ;; Floyd-Warshall
  (for ([m k])
    (for ([i k])
      (define d-im (vector-ref (vector-ref dist i) m))
      (when (< d-im INF)
        (for ([j k])
          (define d-mj (vector-ref (vector-ref dist m) j))
          (define new (+ d-im d-mj))
          (when (< new (vector-ref (vector-ref dist i) j))
            (vector-set! (vector-ref dist i) j new))))))

  ;; DP over positions
  (define n (string-length source))
  (define dp (make-vector (+ n 1) INF))
  (vector-set! dp 0 0)

  (for ([i (in-range 1 (add1 n))])
    ;; single character match
    (when (= (string-ref source (- i 1)) (string-ref target (- i 1)))
      (define prev (vector-ref dp (- i 1)))
      (when (< prev (vector-ref dp i))
        (vector-set! dp i prev)))
    ;; consider all possible segments ending at i
    (for ([j (in-range 0 i)])
      (define src-sub (substring source j i))
      (define tgt-sub (substring target j i))
      (define id-s (hash-ref str->id src-sub #f))
      (define id-t (hash-ref str->id tgt-sub #f))
      (when (and id-s id-t)
        (define cst (vector-ref (vector-ref dist id-s) id-t))
        (when (< cst INF)
          (define cand (+ (vector-ref dp j) cst))
          (when (< cand (vector-ref dp i))
            (vector-set! dp i cand)))))))

  (define ans (vector-ref dp n))
  (if (>= ans INF) -1 ans))
```

## Erlang

```erlang
-spec minimum_cost(Source :: unicode:unicode_binary(), Target :: unicode:unicode_binary(),
                     Original :: [unicode:unicode_binary()], Changed :: [unicode:unicode_binary()],
                     Cost :: [integer()]) -> integer().
minimum_cost(Source, Target, Original, Changed, Cost) ->
    INF = 1 bsl 60,
    %% Build unique string list and map to ids (1-based)
    AllStrings0 = lists:foldl(fun(S, Acc) -> maps:put(S, true, Acc) end, #{}, Original ++ Changed),
    UniqueList = maps:keys(AllStrings0),
    {StrIdMap, _} =
        lists:foldl(
          fun(Str, {M, Id}) ->
                  {maps:put(Str, Id, M), Id + 1}
          end,
          {#{}, 1},
          UniqueList),
    Ids = lists:seq(1, maps:size(StrIdMap)),
    %% Initialize distance map
    Dist0 = maps:from_list([{ {I,I}, 0 } || I <- Ids]),
    %% Add direct edges with minimal cost
    EdgeDist =
        fun(DistMap, OStr, CStr, C) ->
                OId = maps:get(OStr, StrIdMap),
                CId = maps:get(CStr, StrIdMap),
                Key = {OId, CId},
                Prev = maps:get(Key, DistMap, INF),
                if C < Prev -> maps:put(Key, C, DistMap) else DistMap end
        end,
    Dist1 = lists:foldl(
               fun({O, C, Co}, DAcc) ->
                       EdgeDist(DAcc, O, C, Co)
               end,
               Dist0,
               lists:zip3(Original, Changed, Cost)),
    %% Floyd‑Warshall on small graph
    DistMap = 
        lists:foldl(
          fun(Kid, Dk) ->
                  lists:foldl(
                    fun(Iid, Di) ->
                            Dik = maps:get({Iid, Kid}, Di, INF),
                            if Dik < INF ->
                                    lists:foldl(
                                      fun(Jid, Dj) ->
                                              Dkj = maps:get({Kid, Jid}, Dj, INF),
                                              New = Dik + Dkj,
                                              Old = maps:get({Iid, Jid}, Dj, INF),
                                              if New < Old -> maps:put({Iid, Jid}, New, Dj) else Dj end
                                      end,
                                      Di,
                                      Ids)
                            else Di end
                    end,
                    Dk,
                    Ids)
          end,
          Dist1,
          Ids),
    %% DP over prefixes
    N = byte_size(Source),
    Dp0 = erlang:make_tuple(N + 1, INF),
    Dp1 = setelement(1, Dp0, 0),   % dp[0] = 0
    FinalDp =
        lists:foldl(
          fun(I, DpAcc) ->
                  %% I is 1‑based length of prefix
                  MinStart = 
                      case binary:part(Source, {I-1,1}) ==:= binary:part(Target, {I-1,1}) of
                          true -> element(I, DpAcc);   % dp[i-1]
                          false -> INF
                      end,
                  MinCost =
                      lists:foldl(
                        fun(J, CurMin) ->
                                Len = I - J,
                                SrcSub = binary:part(Source, {J, Len}),
                                TgtSub = binary:part(Target, {J, Len}),
                                case maps:find(SrcSub, StrIdMap) of
                                    {ok, Sid} ->
                                        case maps:find(TgtSub, StrIdMap) of
                                            {ok, Tid} ->
                                                DistST = maps:get({Sid, Tid}, DistMap, INF),
                                                if DistST < INF ->
                                                        PrevJ = element(J+1, DpAcc), % dp[j]
                                                        Cand = PrevJ + DistST,
                                                        if Cand < CurMin -> Cand else CurMin end
                                                   ; true -> CurMin
                                                end;
                                            error -> CurMin
                                        end;
                                    error -> CurMin
                                end
                        end,
                        MinStart,
                        lists:seq(0, I-1)),
                  setelement(I+1, DpAcc, MinCost)
          end,
          Dp1,
          lists:seq(1, N)),
    Result = element(N+1, FinalDp),
    if Result >= INF div 2 -> -1; true -> Result end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(String.t(), String.t(), [String.t()], [String.t()], [integer]) :: integer
  def minimum_cost(source, target, original, changed, cost) do
    inf = 1_000_000_000_000

    # assign ids to unique strings from original and changed
    uniq_strings =
      (original ++ changed)
      |> Enum.uniq()

    {id_map, _} =
      Enum.reduce(uniq_strings, {%{}, 0}, fn str, {m, idx} ->
        {Map.put(m, str, idx), idx + 1}
      end)

    m = map_size(id_map)

    # initialize distance map
    dist =
      Enum.reduce(0..(m - 1), %{}, fn i, acc ->
        Map.put(acc, {i, i}, 0)
      end)

    # set direct edges (keep minimal cost for duplicate edges)
    dist =
      Enum.zip([original, changed, cost])
      |> Enum.reduce(dist, fn {[orig, chg, c]}, dacc ->
        u = id_map[orig]
        v = id_map[chg]
        cur = Map.get(dacc, {u, v}, inf)
        if c < cur, do: Map.put(dacc, {u, v}, c), else: dacc
      end)

    # Floyd-Warshall on map representation (m <= 200)
    dist =
      Enum.reduce(0..(m - 1), dist, fn k, dk ->
        Enum.reduce(0..(m - 1), dk, fn i, di ->
          dik = Map.get(di, {i, k}, inf)

          if dik == inf do
            di
          else
            Enum.reduce(0..(m - 1), di, fn j, dj ->
              dkj = Map.get(dj, {k, j}, inf)
              nd = dik + dkj

              cur = Map.get(dj, {i, j}, inf)

              if nd < cur do
                Map.put(dj, {i, j}, nd)
              else
                dj
              end
            end)
          end
        end)
      end)

    # Build trie of all strings with ids
    root = %{children: %{}, id: nil}

    insert = fn
      (node, <<>>, sid) ->
        %{node | id: sid}
      (node, <<c, rest::binary>>, sid) ->
        child = Map.get(node.children, c, %{children: %{}, id: nil})
        new_child = insert.(child, rest, sid)
        %{node | children: Map.put(node.children, c, new_child)}
    end

    root =
      Enum.with_index(uniq_strings, fn str, idx ->
        {str, idx}
      end)
      |> Enum.reduce(root, fn {str, sid}, acc_root ->
        insert.(acc_root, str, sid)
      end)

    n = byte_size(source)

    # arrays of maps: start index -> %{end_index => id}
    src_maps = :array.new(n, default: %{})
    tgt_maps = :array.new(n, default: %{})

    # helper to fill matches for a given string and map array
    fill_matches = fn bin, arr ->
      Enum.each(0..(n - 1), fn start_idx ->
        node = root
        idx = start_idx

        while idx < n do
          c = :binary.at(bin, idx)
          child = Map.get(node.children, c)

          if child == nil do
            break
          end

          node = child

          if node.id != nil do
            end_idx = idx + 1
            cur_map = :array.get(arr, start_idx)
            new_map = Map.put(cur_map, end_idx, node.id)
            arr = :array.set(arr, start_idx, new_map)
          end

          idx = idx + 1
        end
      end)

      arr
    end

    src_maps = fill_matches.(source, src_maps)
    tgt_maps = fill_matches.(target, tgt_maps)

    # DP over prefixes
    dp = :array.new(n + 1, default: inf)
    dp = :array.set(dp, 0, 0)

    Enum.each(1..n, fn i ->
      best = inf

      # option: keep character if equal
      if :binary.at(source, i - 1) == :binary.at(target, i - 1) do
        prev = :array.get(dp, i - 1)
        if prev < best, do: best = prev
      end

      # consider intervals ending at i
      Enum.each(0..(i - 1), fn j ->
        src_map = :array.get(src_maps, j)
        case Map.fetch(src_map, i) do
          {:ok, sid} ->
            tgt_map = :array.get(tgt_maps, j)

            case Map.fetch(tgt_map, i) do
              {:ok, tid} ->
                trans_cost = Map.get(dist, {sid, tid}, inf)
                if trans_cost < inf do
                  prev = :array.get(dp, j)
                  if prev < inf do
                    cand = prev + trans_cost
                    if cand < best, do: best = cand
                  end
                end

              :error -> :ok
            end

          :error -> :ok
        end
      end)

      dp = :array.set(dp, i, best)
    end)

    ans = :array.get(dp, n)
    if ans >= inf, do: -1, else: ans
  end
end
```
