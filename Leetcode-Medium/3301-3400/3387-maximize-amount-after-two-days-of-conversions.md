# 3387. Maximize Amount After Two Days of Conversions

## Cpp

```cpp
class Solution {
public:
    double maxAmount(string initialCurrency, vector<vector<string>>& pairs1, vector<double>& rates1,
                     vector<vector<string>>& pairs2, vector<double>& rates2) {
        // Build adjacency lists with bidirectional edges
        unordered_map<string, vector<pair<string,double>>> adj1, adj2;
        auto addEdge = [&](unordered_map<string, vector<pair<string,double>>>& adj,
                           const string& a, const string& b, double r){
            adj[a].push_back({b, r});
            adj[b].push_back({a, 1.0 / r});
        };
        for (int i = 0; i < (int)pairs1.size(); ++i) {
            addEdge(adj1, pairs1[i][0], pairs1[i][1], rates1[i]);
        }
        for (int i = 0; i < (int)pairs2.size(); ++i) {
            addEdge(adj2, pairs2[i][0], pairs2[i][1], rates2[i]);
        }

        // BFS/DFS to compute conversion factors from initialCurrency on day 1
        unordered_map<string,double> f1;
        queue<string> q;
        f1[initialCurrency] = 1.0;
        q.push(initialCurrency);
        while (!q.empty()) {
            string cur = q.front(); q.pop();
            double curRate = f1[cur];
            if (adj1.find(cur) == adj1.end()) continue;
            for (auto &pr : adj1[cur]) {
                const string& nxt = pr.first;
                double w = pr.second;
                if (!f1.count(nxt)) {
                    f1[nxt] = curRate * w;
                    q.push(nxt);
                }
            }
        }

        // Compute conversion factors from initialCurrency on day 2 (initial -> node)
        unordered_map<string,double> g; // initial -> node
        g[initialCurrency] = 1.0;
        q.push(initialCurrency);
        while (!q.empty()) {
            string cur = q.front(); q.pop();
            double curRate = g[cur];
            if (adj2.find(cur) == adj2.end()) continue;
            for (auto &pr : adj2[cur]) {
                const string& nxt = pr.first;
                double w = pr.second;
                if (!g.count(nxt)) {
                    g[nxt] = curRate * w;
                    q.push(nxt);
                }
            }
        }

        // For each currency reachable on both days, compute product
        double ans = 1.0; // staying with no conversion
        for (const auto& kv : f1) {
            const string& cur = kv.first;
            double rateDay1 = kv.second;
            if (!g.count(cur)) continue; // cannot convert back on day2
            double rateDay2Back = 1.0 / g[cur]; // node -> initial on day2
            ans = max(ans, rateDay1 * rateDay2Back);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class Edge {
        String to;
        double weight;
        Edge(String t, double w) { to = t; weight = w; }
    }

    private Map<String, Double> computeRates(String start, List<List<String>> pairs, double[] rates) {
        Map<String, List<Edge>> graph = new HashMap<>();
        for (int i = 0; i < pairs.size(); i++) {
            List<String> p = pairs.get(i);
            String a = p.get(0);
            String b = p.get(1);
            double r = rates[i];
            graph.computeIfAbsent(a, k -> new ArrayList<>()).add(new Edge(b, r));
            graph.computeIfAbsent(b, k -> new ArrayList<>()).add(new Edge(a, 1.0 / r));
        }

        Map<String, Double> rateMap = new HashMap<>();
        Deque<String> stack = new ArrayDeque<>();
        rateMap.put(start, 1.0);
        stack.push(start);

        while (!stack.isEmpty()) {
            String cur = stack.pop();
            double curRate = rateMap.get(cur);
            List<Edge> edges = graph.getOrDefault(cur, Collections.emptyList());
            for (Edge e : edges) {
                if (!rateMap.containsKey(e.to)) {
                    rateMap.put(e.to, curRate * e.weight);
                    stack.push(e.to);
                }
            }
        }
        return rateMap;
    }

    public double maxAmount(String initialCurrency, List<List<String>> pairs1, double[] rates1,
                            List<List<String>> pairs2, double[] rates2) {
        Map<String, Double> day1 = computeRates(initialCurrency, pairs1, rates1);
        Map<String, Double> day2FromInit = computeRates(initialCurrency, pairs2, rates2);

        double best = 1.0; // staying in initial currency
        for (Map.Entry<String, Double> entry : day1.entrySet()) {
            String cur = entry.getKey();
            if (!day2FromInit.containsKey(cur)) continue;
            double rateDay1 = entry.getValue();               // init -> cur on day 1
            double rateDay2Back = 1.0 / day2FromInit.get(cur); // cur -> init on day 2
            double total = rateDay1 * rateDay2Back;
            if (total > best) best = total;
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def maxAmount(self, initialCurrency, pairs1, rates1, pairs2, rates2):
        """
        :type initialCurrency: str
        :type pairs1: List[List[str]]
        :type rates1: List[float]
        :type pairs2: List[List[str]]
        :type rates2: List[float]
        :rtype: float
        """
        from collections import defaultdict

        def build_adj(pairs, rates):
            adj = defaultdict(list)
            for (a, b), r in zip(pairs, rates):
                adj[a].append((b, r))
                adj[b].append((a, 1.0 / r))
            return adj

        def dfs(start, adj):
            res = {}
            stack = [(start, 1.0)]
            while stack:
                node, cur = stack.pop()
                if node in res:
                    continue
                res[node] = cur
                for nb, w in adj.get(node, []):
                    if nb not in res:
                        stack.append((nb, cur * w))
            return res

        adj1 = build_adj(pairs1, rates1)
        adj2 = build_adj(pairs2, rates2)

        conv1 = dfs(initialCurrency, adj1)  # init -> currency factor on day1
        conv2 = dfs(initialCurrency, adj2)  # init -> currency factor on day2

        best = 1.0
        for cur in conv1:
            if cur in conv2 and conv2[cur] != 0:
                amount = conv1[cur] / conv2[cur]
                if amount > best:
                    best = amount
        return best
```

## Python3

```python
from typing import List, Dict
class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float],
                  pairs2: List[List[str]], rates2: List[float]) -> float:
        def build_graph(pairs: List[List[str]], rates: List[float]) -> Dict[str, List]:
            g: Dict[str, List] = {}
            for (a, b), r in zip(pairs, rates):
                if a not in g:
                    g[a] = []
                if b not in g:
                    g[b] = []
                g[a].append((b, r))
                g[b].append((a, 1.0 / r))
            return g

        def compute_rates(g: Dict[str, List], start: str) -> Dict[str, float]:
            rates: Dict[str, float] = {start: 1.0}
            stack = [start]
            while stack:
                cur = stack.pop()
                for nxt, w in g.get(cur, []):
                    if nxt not in rates:
                        rates[nxt] = rates[cur] * w
                        stack.append(nxt)
            return rates

        g1 = build_graph(pairs1, rates1)
        g2 = build_graph(pairs2, rates2)

        rate1 = compute_rates(g1, initialCurrency)
        rate2 = compute_rates(g2, initialCurrency)

        best = 1.0
        for cur in rate1:
            if cur in rate2 and rate2[cur] > 0:
                val = rate1[cur] / rate2[cur]
                if val > best:
                    best = val
        return best
```

## C

```c
#include <stdio.h>
#include <string.h>

double maxAmount(char* initialCurrency, char*** pairs1, int pairs1Size, int* pairs1ColSize,
                 double* rates1, int rates1Size,
                 char*** pairs2, int pairs2Size, int* pairs2ColSize,
                 double* rates2, int rates2Size) {
    /* maximum distinct currencies: each pair adds up to 2, plus initial */
    const int MAXN = 50;
    const int MAXE = 200;

    char names[MAXN][4];
    int ncnt = 0;

    auto getIdx = [&](const char* s)->int{
        for (int i = 0; i < ncnt; ++i) {
            if (strcmp(names[i], s) == 0) return i;
        }
        strcpy(names[ncnt], s);
        return ncnt++;
    };

    int initIdx = getIdx(initialCurrency);

    /* adjacency for day1 */
    int head1[MAXN];
    int to1[MAXE];
    double w1[MAXE];
    int nxt1[MAXE];
    int ecnt1 = 0;
    for (int i = 0; i < MAXN; ++i) head1[i] = -1;

    /* adjacency for day2 */
    int head2[MAXN];
    int to2[MAXE];
    double w2[MAXE];
    int nxt2[MAXE];
    int ecnt2 = 0;
    for (int i = 0; i < MAXN; ++i) head2[i] = -1;

    auto addEdge = [&](int *head, int *to, double *w, int *nxt, int *ecnt,
                       int u, int v, double weight){
        to[*ecnt] = v;
        w[*ecnt] = weight;
        nxt[*ecnt] = head[u];
        head[u] = (*ecnt)++;
    };

    /* build day1 graph */
    for (int i = 0; i < pairs1Size; ++i) {
        int a = getIdx(pairs1[i][0]);
        int b = getIdx(pairs1[i][1]);
        double r = rates1[i];
        addEdge(head1, to1, w1, nxt1, &ecnt1, a, b, r);
        addEdge(head1, to1, w1, nxt1, &ecnt1, b, a, 1.0 / r);
    }

    /* build day2 graph */
    for (int i = 0; i < pairs2Size; ++i) {
        int a = getIdx(pairs2[i][0]);
        int b = getIdx(pairs2[i][1]);
        double r = rates2[i];
        addEdge(head2, to2, w2, nxt2, &ecnt2, a, b, r);
        addEdge(head2, to2, w2, nxt2, &ecnt2, b, a, 1.0 / r);
    }

    int N = ncnt;
    double factor1[MAXN];
    double factor2[MAXN];
    for (int i = 0; i < N; ++i) {
        factor1[i] = -1.0;
        factor2[i] = -1.0;
    }

    /* DFS for day1 */
    void dfs1(int u, double cur) {
        factor1[u] = cur;
        for (int e = head1[u]; e != -1; e = nxt1[e]) {
            int v = to1[e];
            if (factor1[v] < 0) {
                dfs1(v, cur * w1[e]);
            }
        }
    }

    /* DFS for day2 */
    void dfs2(int u, double cur) {
        factor2[u] = cur;
        for (int e = head2[u]; e != -1; e = nxt2[e]) {
            int v = to2[e];
            if (factor2[v] < 0) {
                dfs2(v, cur * w2[e]);
            }
        }
    }

    dfs1(initIdx, 1.0);
    dfs2(initIdx, 1.0);

    double best = 1.0; /* staying with no conversion */
    for (int i = 0; i < N; ++i) {
        if (factor1[i] >= 0 && factor2[i] > 0) {
            double amount = factor1[i] / factor2[i];
            if (amount > best) best = amount;
        }
    }
    return best;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    public double MaxAmount(string initialCurrency, IList<IList<string>> pairs1, double[] rates1, IList<IList<string>> pairs2, double[] rates2)
    {
        var adj1 = BuildAdj(pairs1, rates1);
        var adj2 = BuildAdj(pairs2, rates2);

        var factorDay1 = ComputeFactors(initialCurrency, adj1);          // initial -> X using day 1
        var forwardDay2 = ComputeFactors(initialCurrency, adj2);       // initial -> X using day 2

        double best = 1.0; // doing nothing
        foreach (var kv in factorDay1)
        {
            string cur = kv.Key;
            if (!forwardDay2.ContainsKey(cur)) continue;

            double f1 = kv.Value;                     // initial -> cur on day 1
            double fInitToCurDay2 = forwardDay2[cur]; // initial -> cur on day 2
            double f2 = 1.0 / fInitToCurDay2;          // cur -> initial on day 2

            best = Math.Max(best, f1 * f2);
        }
        return best;
    }

    private Dictionary<string, List<(string neighbor, double rate)>> BuildAdj(IList<IList<string>> pairs, double[] rates)
    {
        var adj = new Dictionary<string, List<(string, double)>>();
        for (int i = 0; i < pairs.Count; i++)
        {
            string a = pairs[i][0];
            string b = pairs[i][1];
            double r = rates[i];

            if (!adj.ContainsKey(a)) adj[a] = new List<(string, double)>();
            if (!adj.ContainsKey(b)) adj[b] = new List<(string, double)>();

            adj[a].Add((b, r));
            adj[b].Add((a, 1.0 / r));
        }
        return adj;
    }

    private Dictionary<string, double> ComputeFactors(string start, Dictionary<string, List<(string neighbor, double rate)>> adj)
    {
        var factors = new Dictionary<string, double>();
        var stack = new Stack<string>();
        factors[start] = 1.0;
        stack.Push(start);

        while (stack.Count > 0)
        {
            string cur = stack.Pop();
            double curFactor = factors[cur];

            if (!adj.ContainsKey(cur)) continue;

            foreach (var edge in adj[cur])
            {
                string nxt = edge.neighbor;
                double rate = edge.rate;
                if (!factors.ContainsKey(nxt))
                {
                    factors[nxt] = curFactor * rate;
                    stack.Push(nxt);
                }
            }
        }

        return factors;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} initialCurrency
 * @param {string[][]} pairs1
 * @param {number[]} rates1
 * @param {string[][]} pairs2
 * @param {number[]} rates2
 * @return {number}
 */
var maxAmount = function(initialCurrency, pairs1, rates1, pairs2, rates2) {
    const buildAdj = (pairs, rates) => {
        const adj = new Map();
        const addEdge = (a, b, w) => {
            if (!adj.has(a)) adj.set(a, []);
            adj.get(a).push([b, w]);
        };
        for (let i = 0; i < pairs.length; ++i) {
            const [u, v] = pairs[i];
            const w = rates[i];
            addEdge(u, v, w);
            addEdge(v, u, 1 / w);
        }
        return adj;
    };
    
    const dfsRates = (start, adj) => {
        const map = new Map();
        const stack = [[start, 1]];
        map.set(start, 1);
        while (stack.length) {
            const [cur, curRate] = stack.pop();
            const neighbors = adj.get(cur) || [];
            for (const [next, w] of neighbors) {
                if (!map.has(next)) {
                    const nextRate = curRate * w;
                    map.set(next, nextRate);
                    stack.push([next, nextRate]);
                }
            }
        }
        return map;
    };
    
    const adj1 = buildAdj(pairs1, rates1);
    const adj2 = buildAdj(pairs2, rates2);
    
    const rateFromStartDay1 = dfsRates(initialCurrency, adj1);
    const rateFromStartDay2 = dfsRates(initialCurrency, adj2);
    
    let best = 1.0; // staying with no conversion
    for (const [currency, r1] of rateFromStartDay1.entries()) {
        if (rateFromStartDay2.has(currency)) {
            const r2Forward = rateFromStartDay2.get(currency); // initial -> currency on day2
            const amount = r1 / r2Forward; // convert back using inverse of day2 path
            if (amount > best) best = amount;
        }
    }
    return best;
};
```

## Typescript

```typescript
function maxAmount(initialCurrency: string, pairs1: string[][], rates1: number[], pairs2: string[][], rates2: number[]): number {
    const buildGraph = (pairs: string[][], rates: number[]) => {
        const adj = new Map<string, [string, number][]>();
        for (let i = 0; i < pairs.length; ++i) {
            const [a, b] = pairs[i];
            const r = rates[i];
            if (!adj.has(a)) adj.set(a, []);
            if (!adj.has(b)) adj.set(b, []);
            adj.get(a)!.push([b, r]);
            adj.get(b)!.push([a, 1 / r]);
        }
        return adj;
    };

    const dfs = (graph: Map<string, [string, number][]>, start: string): Map<string, number> => {
        const res = new Map<string, number>();
        const stack: [string, number][] = [[start, 1]];
        while (stack.length) {
            const [node, val] = stack.pop()!;
            if (res.has(node)) continue;
            res.set(node, val);
            const neigh = graph.get(node) || [];
            for (const [nbr, w] of neigh) {
                if (!res.has(nbr)) stack.push([nbr, val * w]);
            }
        }
        return res;
    };

    const g1 = dfs(buildGraph(pairs1, rates1), initialCurrency);
    const g2 = dfs(buildGraph(pairs2, rates2), initialCurrency);

    let ans = 1.0;
    for (const [cur, f1] of g1) {
        if (g2.has(cur)) {
            const f2 = g2.get(cur)!; // factor from initial to cur on day 2
            const amount = f1 / f2;   // convert back using inverse rate
            if (amount > ans) ans = amount;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $initialCurrency
     * @param String[][] $pairs1
     * @param Float[] $rates1
     * @param String[][] $pairs2
     * @param Float[] $rates2
     * @return Float
     */
    function maxAmount($initialCurrency, $pairs1, $rates1, $pairs2, $rates2) {
        $map = [];
        $idx = 0;
        $add = function($c) use (&$map, &$idx) {
            if (!isset($map[$c])) {
                $map[$c] = $idx++;
            }
        };
        $add($initialCurrency);
        foreach ($pairs1 as $p) { $add($p[0]); $add($p[1]); }
        foreach ($pairs2 as $p) { $add($p[0]); $add($p[1]); }

        $n = $idx;
        $mat1 = array_fill(0, $n, array_fill(0, $n, 0.0));
        $mat2 = array_fill(0, $n, array_fill(0, $n, 0.0));
        for ($i = 0; $i < $n; $i++) {
            $mat1[$i][$i] = 1.0;
            $mat2[$i][$i] = 1.0;
        }

        $len1 = count($pairs1);
        for ($i = 0; $i < $len1; $i++) {
            $a = $pairs1[$i][0];
            $b = $pairs1[$i][1];
            $rate = $rates1[$i];
            $ia = $map[$a];
            $ib = $map[$b];
            if ($rate > $mat1[$ia][$ib]) $mat1[$ia][$ib] = $rate;
            $inv = 1.0 / $rate;
            if ($inv > $mat1[$ib][$ia]) $mat1[$ib][$ia] = $inv;
        }

        $len2 = count($pairs2);
        for ($i = 0; $i < $len2; $i++) {
            $a = $pairs2[$i][0];
            $b = $pairs2[$i][1];
            $rate = $rates2[$i];
            $ia = $map[$a];
            $ib = $map[$b];
            if ($rate > $mat2[$ia][$ib]) $mat2[$ia][$ib] = $rate;
            $inv = 1.0 / $rate;
            if ($inv > $mat2[$ib][$ia]) $mat2[$ib][$ia] = $inv;
        }

        for ($k = 0; $k < $n; $k++) {
            for ($i = 0; $i < $n; $i++) {
                if ($mat1[$i][$k] == 0) continue;
                for ($j = 0; $j < $n; $j++) {
                    $cand = $mat1[$i][$k] * $mat1[$k][$j];
                    if ($cand > $mat1[$i][$j]) {
                        $mat1[$i][$j] = $cand;
                    }
                }
            }
        }

        for ($k = 0; $k < $n; $k++) {
            for ($i = 0; $i < $n; $i++) {
                if ($mat2[$i][$k] == 0) continue;
                for ($j = 0; $j < $n; $j++) {
                    $cand = $mat2[$i][$k] * $mat2[$k][$j];
                    if ($cand > $mat2[$i][$j]) {
                        $mat2[$i][$j] = $cand;
                    }
                }
            }
        }

        $initIdx = $map[$initialCurrency];
        $best = 1.0;
        for ($c = 0; $c < $n; $c++) {
            $rate1 = $mat1[$initIdx][$c];
            $rate2 = $mat2[$c][$initIdx];
            if ($rate1 > 0 && $rate2 > 0) {
                $val = $rate1 * $rate2;
                if ($val > $best) $best = $val;
            }
        }

        return $best;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func maxAmount(_ initialCurrency: String, _ pairs1: [[String]], _ rates1: [Double], _ pairs2: [[String]], _ rates2: [Double]) -> Double {
        // Collect all unique currencies
        var currencySet = Set<String>()
        currencySet.insert(initialCurrency)
        for p in pairs1 { currencySet.insert(p[0]); currencySet.insert(p[1]) }
        for p in pairs2 { currencySet.insert(p[0]); currencySet.insert(p[1]) }
        let currencies = Array(currencySet)
        var idx: [String:Int] = [:]
        for (i, cur) in currencies.enumerated() {
            idx[cur] = i
        }
        let n = currencies.count
        func buildDist(_ pairs: [[String]], _ rates: [Double]) -> [[Double]] {
            var dist = Array(repeating: Array(repeating: -Double.infinity, count: n), count: n)
            for i in 0..<n { dist[i][i] = 0.0 }
            for (k, pair) in pairs.enumerated() {
                let a = idx[pair[0]]!
                let b = idx[pair[1]]!
                let r = rates[k]
                let logR = log(r)
                if logR > dist[a][b] { dist[a][b] = logR }
                if -logR > dist[b][a] { dist[b][a] = -logR }
            }
            // Floyd-Warshall for maximum sum of logs
            for m in 0..<n {
                for i in 0..<n where dist[i][m] > -Double.infinity {
                    for j in 0..<n where dist[m][j] > -Double.infinity {
                        let cand = dist[i][m] + dist[m][j]
                        if cand > dist[i][j] {
                            dist[i][j] = cand
                        }
                    }
                }
            }
            return dist
        }
        
        let dist1 = buildDist(pairs1, rates1)
        let dist2 = buildDist(pairs2, rates2)
        guard let startIdx = idx[initialCurrency] else { return 1.0 }
        var best: Double = 1.0
        for i in 0..<n {
            let log12 = dist1[startIdx][i]
            let log21 = dist2[i][startIdx]
            if log12 > -Double.infinity && log21 > -Double.infinity {
                let amount = exp(log12) * exp(log21)
                if amount > best { best = amount }
            }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxAmount(
        initialCurrency: String,
        pairs1: List<List<String>>,
        rates1: DoubleArray,
        pairs2: List<List<String>>,
        rates2: DoubleArray
    ): Double {
        // Build graph for day 1
        val g1 = mutableMapOf<String, MutableList<Pair<String, Double>>>()
        for (i in pairs1.indices) {
            val a = pairs1[i][0]
            val b = pairs1[i][1]
            val r = rates1[i]
            g1.computeIfAbsent(a) { mutableListOf() }.add(Pair(b, r))
            g1.computeIfAbsent(b) { mutableListOf() }.add(Pair(a, 1.0 / r))
        }
        // Build graph for day 2
        val g2 = mutableMapOf<String, MutableList<Pair<String, Double>>>()
        for (i in pairs2.indices) {
            val a = pairs2[i][0]
            val b = pairs2[i][1]
            val r = rates2[i]
            g2.computeIfAbsent(a) { mutableListOf() }.add(Pair(b, r))
            g2.computeIfAbsent(b) { mutableListOf() }.add(Pair(a, 1.0 / r))
        }

        // DFS to compute conversion ratios from initialCurrency
        fun dfs(
            graph: Map<String, List<Pair<String, Double>>>,
            cur: String,
            curRate: Double,
            map: MutableMap<String, Double>
        ) {
            if (map.containsKey(cur)) return
            map[cur] = curRate
            for ((next, w) in graph[cur] ?: emptyList()) {
                if (!map.containsKey(next)) {
                    dfs(graph, next, curRate * w, map)
                }
            }
        }

        val rateFromInitDay1 = mutableMapOf<String, Double>()
        dfs(g1, initialCurrency, 1.0, rateFromInitDay1)

        val rateFromInitDay2 = mutableMapOf<String, Double>()
        dfs(g2, initialCurrency, 1.0, rateFromInitDay2)

        var best = 1.0 // doing nothing
        for ((currency, r1) in rateFromInitDay1) {
            val r2 = rateFromInitDay2[currency] ?: continue
            val amount = r1 * (1.0 / r2)
            if (amount > best) best = amount
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  double maxAmount(String initialCurrency, List<List<String>> pairs1,
      List<double> rates1, List<List<String>> pairs2, List<double> rates2) {
    // Build adjacency list for day 1
    final Map<String, List<_Edge>> adj1 = {};
    for (int i = 0; i < pairs1.length; ++i) {
      String a = pairs1[i][0];
      String b = pairs1[i][1];
      double r = rates1[i];
      adj1.putIfAbsent(a, () => []).add(_Edge(b, r));
      adj1.putIfAbsent(b, () => []).add(_Edge(a, 1.0 / r));
    }

    // Build adjacency list for day 2
    final Map<String, List<_Edge>> adj2 = {};
    for (int i = 0; i < pairs2.length; ++i) {
      String a = pairs2[i][0];
      String b = pairs2[i][1];
      double r = rates2[i];
      adj2.putIfAbsent(a, () => []).add(_Edge(b, r));
      adj2.putIfAbsent(b, () => []).add(_Edge(a, 1.0 / r));
    }

    // Compute conversion factors from initialCurrency to every reachable currency
    final Map<String, double> factor1 = _computeFactors(initialCurrency, adj1);
    final Map<String, double> factor2 = _computeFactors(initialCurrency, adj2);

    double best = 1.0; // doing nothing yields amount 1
    for (final entry in factor1.entries) {
      String cur = entry.key;
      if (!factor2.containsKey(cur)) continue;
      double amount = entry.value * (1.0 / factor2[cur]!);
      if (amount > best) best = amount;
    }
    return best;
  }

  Map<String, double> _computeFactors(
      String start, Map<String, List<_Edge>> adj) {
    final Map<String, double> factors = {};
    final List<String> queue = [];
    factors[start] = 1.0;
    queue.add(start);
    int idx = 0;
    while (idx < queue.length) {
      String cur = queue[idx++];
      double curFactor = factors[cur]!;
      for (final edge in adj[cur] ?? const []) {
        if (!factors.containsKey(edge.to)) {
          factors[edge.to] = curFactor * edge.rate;
          queue.add(edge.to);
        }
      }
    }
    return factors;
  }
}

class _Edge {
  final String to;
  final double rate;
  const _Edge(this.to, this.rate);
}
```

## Golang

```go
func maxAmount(initialCurrency string, pairs1 [][]string, rates1 []float64, pairs2 [][]string, rates2 []float64) float64 {
	type Edge struct {
		to   string
		rate float64
	}
	buildGraph := func(pairs [][]string, rates []float64) map[string][]Edge {
		g := make(map[string][]Edge)
		for i, p := range pairs {
			a, b := p[0], p[1]
			r := rates[i]
			g[a] = append(g[a], Edge{b, r})
			g[b] = append(g[b], Edge{a, 1.0 / r})
		}
		return g
	}
	dfs := func(g map[string][]Edge, start string) map[string]float64 {
		res := make(map[string]float64)
		stack := []string{start}
		res[start] = 1.0
		for len(stack) > 0 {
			v := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			curRate := res[v]
			for _, e := range g[v] {
				if _, ok := res[e.to]; !ok {
					res[e.to] = curRate * e.rate
					stack = append(stack, e.to)
				}
			}
		}
		return res
	}

	g1 := buildGraph(pairs1, rates1)
	g2 := buildGraph(pairs2, rates2)

	f1 := dfs(g1, initialCurrency) // initial -> currency using day 1 rates
	f2 := dfs(g2, initialCurrency) // initial -> currency using day 2 rates

	ans := 1.0
	for cur, rate1 := range f1 {
		if rate2InitToCur, ok := f2[cur]; ok && rate2InitToCur != 0 {
			total := rate1 * (1.0 / rate2InitToCur)
			if total > ans {
				ans = total
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_amount(initial_currency, pairs1, rates1, pairs2, rates2)
  build_ratios = lambda do |pairs, rates|
    adj = Hash.new { |h, k| h[k] = [] }
    pairs.each_with_index do |(a, b), i|
      r = rates[i]
      adj[a] << [b, r]
      adj[b] << [a, 1.0 / r]
    end
    ratios = {}
    stack = [[initial_currency, 1.0]]
    until stack.empty?
      cur, val = stack.pop
      next if ratios.key?(cur)
      ratios[cur] = val
      adj[cur].each do |nbr, w|
        stack << [nbr, val * w] unless ratios.key?(nbr)
      end
    end
    ratios
  end

  ratios1 = build_ratios.call(pairs1, rates1)
  ratios2 = build_ratios.call(pairs2, rates2)

  max_val = 1.0
  ratios1.each_key do |c|
    if ratios2.key?(c)
      amount = ratios1[c] / ratios2[c]
      max_val = amount if amount > max_val
    end
  end
  max_val
end
```

## Scala

```scala
object Solution {
    def maxAmount(initialCurrency: String,
                  pairs1: List[List[String]],
                  rates1: Array[Double],
                  pairs2: List[List[String]],
                  rates2: Array[Double]): Double = {

        def computeFactors(pairs: List[List[String]], rates: Array[Double]): Map[String, Double] = {
            val adj = scala.collection.mutable.Map.empty[String, scala.collection.mutable.ListBuffer[(String, Double)]]
            for (i <- pairs.indices) {
                val a = pairs(i)(0)
                val b = pairs(i)(1)
                val r = rates(i)
                adj.getOrElseUpdate(a, scala.collection.mutable.ListBuffer()).append((b, r))
                adj.getOrElseUpdate(b, scala.collection.mutable.ListBuffer()).append((a, 1.0 / r))
            }
            val factor = scala.collection.mutable.Map[String, Double]()
            val stack = new scala.collection.mutable.Stack[String]()
            factor(initialCurrency) = 1.0
            stack.push(initialCurrency)
            while (stack.nonEmpty) {
                val cur = stack.pop()
                for ((nbr, rate) <- adj.getOrElse(cur, Nil)) {
                    if (!factor.contains(nbr)) {
                        factor(nbr) = factor(cur) * rate
                        stack.push(nbr)
                    }
                }
            }
            factor.toMap
        }

        val f1 = computeFactors(pairs1, rates1)
        val f2 = computeFactors(pairs2, rates2)

        var best = 1.0
        for (c <- f1.keySet.intersect(f2.keySet)) {
            val value = f1(c) / f2(c)
            if (value > best) best = value
        }
        best
    }
}
```

## Rust

```rust
use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn max_amount(
        initial_currency: String,
        pairs1: Vec<Vec<String>>,
        rates1: Vec<f64>,
        pairs2: Vec<Vec<String>>,
        rates2: Vec<f64>,
    ) -> f64 {
        // helper to compute conversion factor from start to every reachable currency
        fn build_map(start: &str, pairs: &[Vec<String>], rates: &[f64]) -> HashMap<String, f64> {
            let mut adj: HashMap<String, Vec<(String, f64)>> = HashMap::new();
            for (i, pair) in pairs.iter().enumerate() {
                let a = &pair[0];
                let b = &pair[1];
                let rate = rates[i];
                adj.entry(a.clone()).or_default().push((b.clone(), rate));
                adj.entry(b.clone())
                    .or_default()
                    .push((a.clone(), 1.0 / rate));
            }
            let mut map: HashMap<String, f64> = HashMap::new();
            let mut q: VecDeque<String> = VecDeque::new();
            map.insert(start.to_string(), 1.0);
            q.push_back(start.to_string());
            while let Some(cur) = q.pop_front() {
                let cur_val = *map.get(&cur).unwrap();
                if let Some(neis) = adj.get(&cur) {
                    for (next, w) in neis {
                        if !map.contains_key(next) {
                            map.insert(next.clone(), cur_val * (*w));
                            q.push_back(next.clone());
                        }
                    }
                }
            }
            map
        }

        let map1 = build_map(&initial_currency, &pairs1, &rates1);
        let map2 = build_map(&initial_currency, &pairs2, &rates2);

        let mut best = 1.0_f64;
        for (cur, val1) in map1.iter() {
            if let Some(val2) = map2.get(cur) {
                let amount = val1 * val2;
                if amount > best {
                    best = amount;
                }
            }
        }
        best
    }
}
```

## Racket

```racket
#lang racket
(provide max-amount)

(define/contract (max-amount initialCurrency pairs1 rates1 pairs2 rates2)
  (-> string? (listof (listof string?)) (listof flonum?) (listof (listof string?)) (listof flonum?) flonum?)
  (let* ((graph1 (make-hash))
         (graph2 (make-hash)))
    ;; build graph for day 1
    (for ([pair pairs1] [rate rates1])
      (define a (first pair))
      (define b (second pair))
      (hash-update! graph1 a (lambda (lst) (cons (cons b rate) lst)) '())
      (hash-update! graph1 b (lambda (lst) (cons (cons a (/ 1.0 rate)) lst)) '()))
    ;; build graph for day 2
    (for ([pair pairs2] [rate rates2])
      (define a (first pair))
      (define b (second pair))
      (hash-update! graph2 a (lambda (lst) (cons (cons b rate) lst)) '())
      (hash-update! graph2 b (lambda (lst) (cons (cons a (/ 1.0 rate)) lst)) '()))
    ;; compute conversion factors from initialCurrency to every reachable currency
    (define (compute-factors graph start)
      (let ((res (make-hash)))
        (hash-set! res start 1.0)
        (let loop ((stack (list start)))
          (when (not (null? stack))
            (define cur (car stack))
            (define cur-factor (hash-ref res cur))
            (for ([edge (hash-ref graph cur '())])
              (define nb (car edge))
              (define rate (cdr edge))
              (unless (hash-has-key? res nb)
                (hash-set! res nb (* cur-factor rate))
                (set! stack (cons nb (cdr stack)))))
            (loop (cdr stack))))
        res))
    (define map1 (compute-factors graph1 initialCurrency))
    (define map2 (compute-factors graph2 initialCurrency))
    ;; evaluate best intermediate currency
    (define max-amt 1.0)
    (for ([c (hash-keys map1)])
      (when (hash-has-key? map2 c)
        (define f1 (hash-ref map1 c))
        (define back (/ 1.0 (hash-ref map2 c))) ; C -> initial on day 2
        (define total (* f1 back))
        (when (> total max-amt) (set! max-amt total))))
    max-amt))
```

## Erlang

```erlang
-spec max_amount(InitialCurrency :: unicode:unicode_binary(),
                  Pairs1 :: [[unicode:unicode_binary()]],
                  Rates1 :: [float()],
                  Pairs2 :: [[unicode:unicode_binary()]],
                  Rates2 :: [float()]) -> float().
max_amount(InitialCurrency, Pairs1, Rates1, Pairs2, Rates2) ->
    NegInf = -1.0e100,

    %% collect all currencies
    AllMap = lists:foldl(fun([A,B], Acc) ->
                                 maps:put(A,true,maps:put(B,true,Acc))
                         end, #{}, Pairs1 ++ Pairs2),
    CurrencyList = maps:keys(AllMap),

    %% assign integer ids
    IdMap = assign_ids(CurrencyList, #{}, 0),

    %% build adjacency lists with log weights
    Adj1 = build_adj(Pairs1, Rates1, IdMap),
    Adj2 = build_adj(Pairs2, Rates2, IdMap),

    InitId = maps:get(InitialCurrency, IdMap),

    Dist1 = dijkstra(Adj1, InitId, NegInf),

    IDs = lists:seq(0, length(CurrencyList) - 1),

    MaxLog = lists:foldl(fun(Id, Acc) ->
                                 Log1 = maps:get(Id, Dist1, NegInf),
                                 if Log1 =:= NegInf -> Acc;
                                    true ->
                                        DistFromId = dijkstra(Adj2, Id, NegInf),
                                        Log2 = maps:get(InitId, DistFromId, NegInf),
                                        if Log2 =:= NegInf -> Acc;
                                           true ->
                                               Total = Log1 + Log2,
                                               if Total > Acc -> Total else Acc end
                                        end
                                 end
                         end, 0.0, IDs),

    math:exp(MaxLog).

%% assign sequential ids to currencies
assign_ids([], Map, _) -> Map;
assign_ids([C|Rest], Map, N) ->
    assign_ids(Rest, maps:put(C, N, Map), N + 1).

%% build adjacency list with log weights (both directions)
build_adj(Pairs, Rates, IdMap) ->
    build_adj(lists:zip(Pairs, Rates), #{}, IdMap).

build_adj([], Adj, _) -> Adj;
build_adj([{Pair, Rate}|Rest], Adj, IdMap) ->
    [FromStr, ToStr] = Pair,
    FromId = maps:get(FromStr, IdMap),
    ToId   = maps:get(ToStr, IdMap),
    Log = math:log(Rate),
    Adj1 = add_edge(Adj, FromId, {ToId, Log}),
    Adj2 = add_edge(Adj1, ToId, {FromId, -Log}),
    build_adj(Rest, Adj2, IdMap).

add_edge(Adj, From, {To, Weight}) ->
    Old = maps:get(From, Adj, []),
    maps:put(From, [{To, Weight} | Old], Adj).

%% Dijkstra-like max-sum of logs
dijkstra(Adj, Start, NegInf) ->
    Dist0 = #{Start => 0.0},
    Queue0 = [{0.0, Start}],
    dijkstra_loop(Adj, Dist0, Queue0, NegInf).

dijkstra_loop(_Adj, Dist, [], _) -> Dist;
dijkstra_loop(Adj, Dist, Queue, NegInf) ->
    {Log, Node, RestQueue} = pop_max(Queue),
    case maps:get(Node, Dist) of
        Cur when Log < Cur - 1.0e-12 ->
            dijkstra_loop(Adj, Dist, RestQueue, NegInf);
        _ ->
            Neighs = maps:get(Node, Adj, []),
            {NewDist, NewQueue} =
                lists:foldl(fun({Nb, EdgeLog}, {DAcc, QAcc}) ->
                                    NewLog = Log + EdgeLog,
                                    OldLog = maps:get(Nb, DAcc, NegInf),
                                    if NewLog > OldLog ->
                                            {maps:put(Nb, NewLog, DAcc), [{NewLog, Nb} | QAcc]};
                                       true -> {DAcc, QAcc}
                                    end
                            end, {Dist, RestQueue}, Neighs),
            dijkstra_loop(Adj, NewDist, NewQueue, NegInf)
    end.

%% pop element with maximum log value
pop_max([H|T]) -> pop_max(T, H, []).

pop_max([], Max, Acc) ->
    {element(1, Max), element(2, Max), lists:reverse(Acc)};
pop_max([{L,N}|Rest], {ML,MN}=Max, Acc) ->
    if L > ML ->
            pop_max(Rest, {L,N}, [{ML,MN} | Acc]);
       true ->
            pop_max(Rest, Max, [{L,N} | Acc])
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_amount(String.t(), [[String.t()]], [float()], [[String.t()]], [float()]) :: float()
  def max_amount(initial_currency, pairs1, rates1, pairs2, rates2) do
    g1 = build_graph(pairs1, rates1)
    g2 = build_graph(pairs2, rates2)

    f1 = compute_rates(initial_currency, g1)
    f2 = compute_rates(initial_currency, g2)

    Enum.reduce(Map.keys(f1), 0.0, fn cur, acc ->
      case Map.fetch(f2, cur) do
        {:ok, rate2} ->
          amount = Map.get(f1, cur) * (1.0 / rate2)
          if amount > acc, do: amount, else: acc

        :error ->
          acc
      end
    end)
  end

  defp build_graph(pairs, rates) do
    Enum.reduce(Enum.with_index(pairs), %{}, fn {{[a, b]}, idx}, acc ->
      r = Enum.at(rates, idx)

      acc
      |> Map.update(a, [{b, r}], fn list -> [{b, r} | list] end)
      |> Map.update(b, [{a, 1.0 / r}], fn list -> [{a, 1.0 / r} | list] end)
    end)
  end

  defp compute_rates(start, graph) do
    bfs([start], %{start => 1.0}, graph)
  end

  defp bfs([], visited, _graph), do: visited

  defp bfs([curr | rest], visited, graph) do
    curr_factor = Map.fetch!(visited, curr)

    {new_visited, new_queue} =
      Enum.reduce(Map.get(graph, curr, []), {visited, []}, fn {nbr, rate},
                                                             {vis, q} ->
        if Map.has_key?(vis, nbr) do
          {vis, q}
        else
          factor = curr_factor * rate
          {Map.put(vis, nbr, factor), [nbr | q]}
        end
      end)

    bfs(rest ++ new_queue, new_visited, graph)
  end
end
```
