# 3425. Longest Special Path

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        vector<vector<pair<int,int>>> adj(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v,w});
            adj[v].push_back({u,w});
        }

        unordered_map<int,int> lastPos;          // value -> depth index
        vector<long long> prefDist;              // distance from root to node at each depth
        long long bestLen = -1;
        int minNodes = INT_MAX;

        function<void(int,int,int,long long,int)> dfs = [&](int u, int parent, int depth,
                                                            long long curDist, int L) {
            int prevIdx = -1;
            auto it = lastPos.find(nums[u]);
            if (it != lastPos.end()) prevIdx = it->second;

            int newL = max(L, prevIdx + 1);

            prefDist.push_back(curDist); // index depth
            long long segLen = curDist - (newL > 0 ? prefDist[newL-1] : 0LL);
            int nodeCnt = depth - newL + 1;

            if (segLen > bestLen) {
                bestLen = segLen;
                minNodes = nodeCnt;
            } else if (segLen == bestLen && nodeCnt < minNodes) {
                minNodes = nodeCnt;
            }

            // update last occurrence
            int oldIdx = prevIdx;
            lastPos[nums[u]] = depth;

            for (auto &p : adj[u]) {
                int v = p.first, w = p.second;
                if (v == parent) continue;
                dfs(v, u, depth + 1, curDist + w, newL);
            }

            // restore
            if (oldIdx == -1) lastPos.erase(nums[u]);
            else lastPos[nums[u]] = oldIdx;

            prefDist.pop_back();
        };

        dfs(0, -1, 0, 0LL, 0);

        return {(int)bestLen, minNodes};
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] longestSpecialPath(int[][] edges, int[] nums) {
        int n = nums.length;
        List<int[]>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].add(new int[]{v, w});
            adj[v].add(new int[]{u, w});
        }

        int maxVal = 0;
        for (int v : nums) if (v > maxVal) maxVal = v;
        int[] lastPos = new int[maxVal + 1];
        Arrays.fill(lastPos, -1);

        long[] prefDist = new long[n]; // distance from root for each depth on current path
        int[] depth = new int[n];
        long[] dist = new long[n];

        Deque<Frame> stack = new ArrayDeque<>();
        Deque<Integer> savedPrevStack = new ArrayDeque<>();
        Deque<Integer> savedLeftStack = new ArrayDeque<>();

        // initial state for root (node 0)
        depth[0] = 0;
        dist[0] = 0L;
        int curLeft = 0; // earliest depth allowed for uniqueness
        long bestLen = 0L;
        int minNodes = Integer.MAX_VALUE;

        stack.push(new Frame(0, -1, false));

        while (!stack.isEmpty()) {
            Frame f = stack.pop();
            int u = f.u;
            int parent = f.parent;

            if (f.exit) {
                // restore state
                curLeft = savedLeftStack.pop();
                lastPos[nums[u]] = savedPrevStack.pop();
                continue;
            }

            // entry processing
            int d = depth[u];
            int savedPrev = lastPos[nums[u]];
            int savedLeft = curLeft;

            // update curLeft based on duplicate of current value
            if (savedPrev != -1) {
                curLeft = Math.max(curLeft, savedPrev + 1);
            }

            // set current position for this value
            lastPos[nums[u]] = d;
            prefDist[d] = dist[u];

            // evaluate path ending at u
            long pathLen = dist[u] - prefDist[curLeft];
            int nodesCnt = d - curLeft + 1;
            if (pathLen > bestLen) {
                bestLen = pathLen;
                minNodes = nodesCnt;
            } else if (pathLen == bestLen && nodesCnt < minNodes) {
                minNodes = nodesCnt;
            }

            // push exit marker to restore later
            stack.push(new Frame(u, parent, true));
            savedPrevStack.push(savedPrev);
            savedLeftStack.push(savedLeft);

            // push children
            for (int[] nb : adj[u]) {
                int v = nb[0];
                if (v == parent) continue;
                depth[v] = d + 1;
                dist[v] = dist[u] + nb[1];
                stack.push(new Frame(v, u, false));
            }
        }

        return new int[]{(int) bestLen, minNodes};
    }

    private static class Frame {
        int u;
        int parent;
        boolean exit;
        Frame(int u, int parent, boolean exit) {
            this.u = u;
            this.parent = parent;
            this.exit = exit;
        }
    }
}
```

## Python

```python
class Solution(object):
    def longestSpecialPath(self, edges, nums):
        """
        :type edges: List[List[int]]
        :type nums: List[int]
        :rtype: List[int]
        """
        import sys
        sys.setrecursionlimit(200000)

        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        last_pos = {}          # value -> depth index of its latest occurrence
        dist_at_depth = []     # distance from root at each depth index

        best_len = -1
        min_nodes = 10**9

        def dfs(u, parent, cur_dist, left_idx):
            nonlocal best_len, min_nodes
            idx = len(dist_at_depth)
            dist_at_depth.append(cur_dist)

            val = nums[u]
            prev = last_pos.get(val, -1)
            new_left = left_idx
            if prev != -1 and prev + 1 > new_left:
                new_left = prev + 1

            old_prev = prev
            last_pos[val] = idx

            start_dist = dist_at_depth[new_left]
            path_len = cur_dist - start_dist
            node_cnt = idx - new_left + 1

            if path_len > best_len:
                best_len = path_len
                min_nodes = node_cnt
            elif path_len == best_len and node_cnt < min_nodes:
                min_nodes = node_cnt

            for v, w in adj[u]:
                if v == parent:
                    continue
                dfs(v, u, cur_dist + w, new_left)

            dist_at_depth.pop()
            if old_prev == -1:
                del last_pos[val]
            else:
                last_pos[val] = old_prev

        dfs(0, -1, 0, 0)
        return [best_len, min_nodes]
```

## Python3

```python
import sys
from typing import List

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        sys.setrecursionlimit(200000)
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        prefDist = [0] * n
        path: List[int] = []
        lastSeen = {}
        bestLen = -1
        minNodes = 0

        def dfs(u: int, parent: int, curLeft: int):
            nonlocal bestLen, minNodes
            # add current node to path
            path.append(u)
            depth = len(path) - 1

            prevDepth = lastSeen.get(nums[u], -1)
            curLeft = max(curLeft, prevDepth + 1)

            startNode = path[curLeft]
            length = prefDist[u] - prefDist[startNode]
            nodesCnt = depth - curLeft + 1

            if length > bestLen:
                bestLen = length
                minNodes = nodesCnt
            elif length == bestLen and nodesCnt < minNodes:
                minNodes = nodesCnt

            # store previous occurrence to restore later
            old = lastSeen.get(nums[u], None)
            lastSeen[nums[u]] = depth

            for v, w in adj[u]:
                if v == parent:
                    continue
                prefDist[v] = prefDist[u] + w
                dfs(v, u, curLeft)

            # restore state
            if old is None:
                del lastSeen[nums[u]]
            else:
                lastSeen[nums[u]] = old
            path.pop()

        dfs(0, -1, 0)
        return [bestLen, minNodes]
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct Edge {
    int to;
    int w;
    int next;
} Edge;

static Edge *gEdges;
static int *gHead;
static int *gNums;
static int gN;

static int *gLastPos;      // value -> depth, -1 if not present
static int *gStackNode;    // node id at each depth
static int *gDistStack;    // distance from root to node at each depth

static int bestLen;
static int bestNodes;

/* add undirected edge */
static void addEdge(int u, int v, int w, int *edgeCnt) {
    gEdges[*edgeCnt].to = v;
    gEdges[*edgeCnt].w = w;
    gEdges[*edgeCnt].next = gHead[u];
    gHead[u] = (*edgeCnt)++;
}

/* depth‑first search */
static void dfs(int u, int parent, int depth, int low, int curDist) {
    /* push current node onto path stacks */
    gStackNode[depth] = u;
    gDistStack[depth] = curDist;

    int val = gNums[u];
    int prevDepth = gLastPos[val];
    int newLow = low;
    if (prevDepth != -1 && prevDepth + 1 > newLow) {
        newLow = prevDepth + 1;
    }

    /* evaluate longest special path ending at u */
    int startDepth = newLow;
    int nodesCnt = depth - startDepth + 1;
    int lenPath;
    if (startDepth == depth) {
        lenPath = 0;                     // single node
    } else {
        int parentIdx = startDepth - 1;
        int parentDist = (parentIdx >= 0) ? gDistStack[parentIdx] : 0;
        lenPath = curDist - parentDist;
    }

    if (lenPath > bestLen || (lenPath == bestLen && nodesCnt < bestNodes)) {
        bestLen = lenPath;
        bestNodes = nodesCnt;
    }

    /* record current value depth */
    int oldPrev = gLastPos[val];
    gLastPos[val] = depth;

    /* recurse to children */
    for (int e = gHead[u]; e != -1; e = gEdges[e].next) {
        int v = gEdges[e].to;
        if (v == parent) continue;
        dfs(v, u, depth + 1, newLow, curDist + gEdges[e].w);
    }

    /* restore previous occurrence */
    gLastPos[val] = oldPrev;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* longestSpecialPath(int** edges, int edgesSize, int* edgesColSize,
                        int* nums, int numsSize, int* returnSize) {
    gN = numsSize;
    gNums = nums;

    /* build adjacency list */
    gHead = (int*)calloc(gN, sizeof(int));
    for (int i = 0; i < gN; ++i) gHead[i] = -1;
    gEdges = (Edge*)malloc(sizeof(Edge) * 2 * (gN - 1));
    int edgeCnt = 0;
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int w = edges[i][2];
        addEdge(u, v, w, &edgeCnt);
        addEdge(v, u, w, &edgeCnt);
    }

    /* auxiliary structures */
    int maxVal = 50000;                     // per constraints
    gLastPos = (int*)malloc(sizeof(int) * (maxVal + 1));
    for (int i = 0; i <= maxVal; ++i) gLastPos[i] = -1;

    gStackNode = (int*)malloc(sizeof(int) * gN);
    gDistStack = (int*)malloc(sizeof(int) * gN);

    bestLen = 0;
    bestNodes = 1;                         // any single node

    dfs(0, -1, 0, 0, 0);                   // start from root

    int* ans = (int*)malloc(sizeof(int) * 2);
    ans[0] = bestLen;
    ans[1] = bestNodes;
    *returnSize = 2;

    /* clean up */
    free(gHead);
    free(gEdges);
    free(gLastPos);
    free(gStackNode);
    free(gDistStack);

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private List<(int neighbor, int len)>[] graph;
    private int[] nums;
    private long[] prefLen;
    private Dictionary<int, int> lastPos;
    private int[] depthNode;
    private long maxLen;
    private int minNodes;

    public int[] LongestSpecialPath(int[][] edges, int[] nums) {
        int n = nums.Length;
        this.nums = nums;
        graph = new List<(int neighbor, int len)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, int)>();
        foreach (var e in edges) {
            int u = e[0], v = e[1], w = e[2];
            graph[u].Add((v, w));
            graph[v].Add((u, w));
        }
        prefLen = new long[n];
        lastPos = new Dictionary<int, int>();
        depthNode = new int[n];
        maxLen = 0;
        minNodes = 1; // at least one node path length 0

        Dfs(0, -1, 0L, 0, 0);
        return new int[] { (int)maxLen, minNodes };
    }

    private void Dfs(int node, int parent, long curPref, int leftIdx, int depth) {
        prefLen[node] = curPref;
        int val = nums[node];
        int prevDepth = -1;
        if (lastPos.TryGetValue(val, out int pd)) prevDepth = pd;

        int newLeft = leftIdx;
        if (prevDepth != -1) newLeft = Math.Max(newLeft, prevDepth + 1);

        lastPos[val] = depth;
        depthNode[depth] = node;

        long segLen = curPref - prefLen[depthNode[newLeft]];
        int nodeCount = depth - newLeft + 1;

        if (segLen > maxLen) {
            maxLen = segLen;
            minNodes = nodeCount;
        } else if (segLen == maxLen && nodeCount < minNodes) {
            minNodes = nodeCount;
        }

        foreach (var (nbr, w) in graph[node]) {
            if (nbr == parent) continue;
            Dfs(nbr, node, curPref + w, newLeft, depth + 1);
        }

        // backtrack
        if (prevDepth == -1) lastPos.Remove(val);
        else lastPos[val] = prevDepth;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} edges
 * @param {number[]} nums
 * @return {number[]}
 */
var longestSpecialPath = function(edges, nums) {
    const n = nums.length;
    // build adjacency list
    const adj = Array.from({length: n}, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }

    const MAX_VAL = 50000; // per constraints
    const lastPos = new Int32Array(MAX_VAL + 1);
    for (let i = 0; i <= MAX_VAL; ++i) lastPos[i] = -1;

    const distStack = new Array(n);
    let bestLen = 0;
    let minNodes = 1; // single node path

    // iterative DFS stack
    const stack = [];
    // frame: {node, parent, depth, cumDist, windowStart, stage, prevDepth}
    stack.push({node:0, parent:-1, depth:0, cumDist:0, windowStart:0, stage:0});

    while (stack.length) {
        const f = stack.pop();
        if (f.stage === 0) { // entering node
            const val = nums[f.node];
            const prevDepth = lastPos[val]; // -1 if not present
            const newWindowStart = Math.max(f.windowStart, prevDepth + 1);

            // push exit frame to restore state later
            stack.push({
                node: f.node,
                parent: f.parent,
                depth: f.depth,
                cumDist: f.cumDist,
                windowStart: newWindowStart,
                stage: 1,
                prevDepth: prevDepth
            });

            // record current node info
            distStack[f.depth] = f.cumDist;
            lastPos[val] = f.depth;

            // evaluate path ending at this node
            const ancDist = distStack[newWindowStart];
            const length = f.cumDist - ancDist;
            const nodesCount = f.depth - newWindowStart + 1;
            if (length > bestLen) {
                bestLen = length;
                minNodes = nodesCount;
            } else if (length === bestLen && nodesCount < minNodes) {
                minNodes = nodesCount;
            }

            // push children
            for (const [to, w] of adj[f.node]) {
                if (to === f.parent) continue;
                stack.push({
                    node: to,
                    parent: f.node,
                    depth: f.depth + 1,
                    cumDist: f.cumDist + w,
                    windowStart: newWindowStart,
                    stage: 0
                });
            }
        } else { // exiting node, restore lastPos
            const val = nums[f.node];
            if (f.prevDepth === -1) {
                lastPos[val] = -1;
            } else {
                lastPos[val] = f.prevDepth;
            }
        }
    }

    return [bestLen, minNodes];
};
```

## Typescript

```typescript
function longestSpecialPath(edges: number[][], nums: number[]): number[] {
    const n = nums.length;
    const adj: [number, number][][] = Array.from({ length: n }, () => []);
    for (const e of edges) {
        const u = e[0], v = e[1], w = e[2];
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }

    const maxVal = Math.max(...nums);
    const lastPos = new Int32Array(maxVal + 1);
    for (let i = 0; i < lastPos.length; ++i) lastPos[i] = -1;

    const pathNodes: number[] = [];
    const pathDist: number[] = [];

    const dist = new Int32Array(n);
    let curLeft = 0;
    let bestLen = 0;
    let bestCnt = Number.MAX_SAFE_INTEGER;

    interface FrameEnter {
        u: number;
        parent: number;
        stage: 0;
    }
    interface FrameExit {
        u: number;
        parent: number;
        stage: 1;
        savedPrevPos: number;
        savedCurLeft: number;
    }
    type Frame = FrameEnter | FrameExit;

    const stack: Frame[] = [{ u: 0, parent: -1, stage: 0 }];

    while (stack.length) {
        const f = stack.pop() as Frame;
        if (f.stage === 0) { // enter node
            const u = f.u;
            const val = nums[u];
            const prevPos = lastPos[val];
            const savedPrevPos = prevPos;
            const savedCurLeft = curLeft;

            if (prevPos !== -1 && prevPos + 1 > curLeft) {
                curLeft = prevPos + 1;
            }

            // push exit frame
            stack.push({
                u,
                parent: f.parent,
                stage: 1,
                savedPrevPos,
                savedCurLeft,
            });

            const pos = pathNodes.length; // index of current node after push
            pathNodes.push(u);
            pathDist.push(dist[u]);

            const startIdx = curLeft;
            const len = dist[u] - pathDist[startIdx];
            const cnt = pos - startIdx + 1;

            if (len > bestLen) {
                bestLen = len;
                bestCnt = cnt;
            } else if (len === bestLen && cnt < bestCnt) {
                bestCnt = cnt;
            }

            lastPos[val] = pos;

            // push children
            const neighbors = adj[u];
            for (let i = neighbors.length - 1; i >= 0; --i) {
                const [v, w] = neighbors[i];
                if (v === f.parent) continue;
                dist[v] = dist[u] + w;
                stack.push({ u: v, parent: u, stage: 0 });
            }
        } else { // exit node
            const u = f.u;
            const val = nums[u];
            lastPos[val] = f.savedPrevPos;
            curLeft = f.savedCurLeft;
            pathNodes.pop();
            pathDist.pop();
        }
    }

    return [bestLen, bestCnt];
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $edges
     * @param Integer[] $nums
     * @return Integer[]
     */
    function longestSpecialPath($edges, $nums) {
        $n = count($nums);
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            [$u, $v, $len] = $e;
            $adj[$u][] = [$v, $len];
            $adj[$v][] = [$u, $len];
        }

        $lastPos = [];                 // value => depth on current path
        $stackNodes = array_fill(0, $n, 0); // node at each depth
        $distRoot = array_fill(0, $n, 0);

        $bestLen = 0;
        $minNodes = 1;   // single node path length 0

        $depth = 0;
        $leftBound = 0;  // earliest depth allowed for unique values ending at current node

        $dfs = function($u, $parent) use (&$adj, &$nums, &$lastPos, &$stackNodes, &$distRoot, &$bestLen, &$minNodes, &$depth, &$leftBound, &$dfs) {
            $stackNodes[$depth] = $u;
            $val = $nums[$u];
            $prevPos = $lastPos[$val] ?? -1;
            $oldLeft = $leftBound;

            if ($prevPos != -1) {
                $leftBound = max($leftBound, $prevPos + 1);
            }
            $lastPos[$val] = $depth;

            // candidate path from leftBound depth to current node
            $ancestorNode = $stackNodes[$leftBound];
            $candLen = $distRoot[$u] - $distRoot[$ancestorNode];
            $nodesCount = $depth - $leftBound + 1;
            if ($candLen > $bestLen) {
                $bestLen = $candLen;
                $minNodes = $nodesCount;
            } elseif ($candLen == $bestLen && $nodesCount < $minNodes) {
                $minNodes = $nodesCount;
            }

            foreach ($adj[$u] as $edge) {
                [$v, $w] = $edge;
                if ($v === $parent) continue;
                $distRoot[$v] = $distRoot[$u] + $w;
                $depth++;
                $dfs($v, $u);
                $depth--;
            }

            // restore state
            if ($prevPos === -1) {
                unset($lastPos[$val]);
            } else {
                $lastPos[$val] = $prevPos;
            }
            $leftBound = $oldLeft;
        };

        $dfs(0, -1);
        return [$bestLen, $minNodes];
    }
}
```

## Swift

```swift
class Solution {
    func longestSpecialPath(_ edges: [[Int]], _ nums: [Int]) -> [Int] {
        let n = nums.count
        var adj = Array(repeating: [(to: Int, w: Int)](), count: n)
        for e in edges {
            let u = e[0], v = e[1], w = e[2]
            adj[u].append((v, w))
            adj[v].append((u, w))
        }
        var dist = Array(repeating: Int64(0), count: n)
        let maxVal = 50000
        var lastPos = Array(repeating: -1, count: maxVal + 1)
        var pathDist = [Int64]()          // distance at each depth
        var curLStack = [Int]()           // previous curL values for backtrack
        var curL = 0                      // left boundary index of unique window
        var bestLen: Int64 = 0
        var minNodes = Int.max

        func dfs(_ u: Int, _ parent: Int) {
            let depth = pathDist.count          // depth before adding current node
            let val = nums[u]
            let prevLast = lastPos[val]

            let oldCurL = curL
            if prevLast != -1 && prevLast + 1 > curL {
                curL = prevLast + 1
            }
            curLStack.append(oldCurL)

            // add current node to path
            pathDist.append(dist[u])

            // compute length and node count for the longest unique suffix ending at u
            let ancDist = pathDist[curL]
            let length = dist[u] - ancDist
            let nodesCount = depth - curL + 1

            if length > bestLen {
                bestLen = length
                minNodes = nodesCount
            } else if length == bestLen && nodesCount < minNodes {
                minNodes = nodesCount
            }

            // update last occurrence of value
            lastPos[val] = depth

            for edge in adj[u] where edge.to != parent {
                let v = edge.to
                dist[v] = dist[u] + Int64(edge.w)
                dfs(v, u)
            }

            // backtrack
            lastPos[val] = prevLast
            pathDist.removeLast()
            curL = curLStack.removeLast()
        }

        dfs(0, -1)

        return [Int(bestLen), minNodes]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestSpecialPath(edges: Array<IntArray>, nums: IntArray): IntArray {
        val n = nums.size
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val w = e[2]
            adj[u].add(Pair(v, w))
            adj[v].add(Pair(u, w))
        }

        val lastPos = HashMap<Int, Int>()
        val prefixDist = LongArray(n)
        var maxLen = 0L
        var minNodes = Int.MAX_VALUE

        fun dfs(node: Int, parent: Int, dist: Long, depth: Int, startIdx: Int) {
            val value = nums[node]
            val prev = lastPos.getOrDefault(value, -1)
            var curStart = startIdx
            if (prev != -1) {
                curStart = kotlin.math.max(curStart, prev + 1)
            }
            lastPos[value] = depth
            prefixDist[depth] = dist

            val pathLen = dist - if (curStart == 0) 0L else prefixDist[curStart - 1]
            val nodeCnt = depth - curStart + 1
            if (pathLen > maxLen) {
                maxLen = pathLen
                minNodes = nodeCnt
            } else if (pathLen == maxLen && nodeCnt < minNodes) {
                minNodes = nodeCnt
            }

            for ((to, w) in adj[node]) {
                if (to == parent) continue
                dfs(to, node, dist + w.toLong(), depth + 1, curStart)
            }

            if (prev == -1) {
                lastPos.remove(value)
            } else {
                lastPos[value] = prev
            }
        }

        dfs(0, -1, 0L, 0, 0)

        return intArrayOf(maxLen.toInt(), minNodes)
    }
}
```

## Dart

```dart
class Solution {
  List<int> longestSpecialPath(List<List<int>> edges, List<int> nums) {
    int n = nums.length;
    // Build adjacency list
    List<List<List<int>>> graph = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0], v = e[1], w = e[2];
      graph[u].add([v, w]);
      graph[v].add([u, w]);
    }

    int maxLen = 0;
    int minNodes = n + 1;

    // value -> depth index of its last occurrence on current path
    Map<int, int> lastPos = {};

    // prefix cumulative lengths for each depth (excluding current node)
    List<int> prefix = [];

    void dfs(int u, int parent, int depth, int cumLen, int left) {
      int val = nums[u];
      int prevIdx = -1;
      if (lastPos.containsKey(val)) prevIdx = lastPos[val]!;

      int newLeft = left;
      if (prevIdx != -1 && prevIdx + 1 > newLeft) {
        newLeft = prevIdx + 1;
      }

      // record current occurrence
      lastPos[val] = depth;

      // compute length of longest unique suffix ending at u
      int startDepth = newLeft;
      int len = cumLen - (startDepth > 0 ? prefix[startDepth - 1] : 0);
      int nodesCount = depth - startDepth + 1;

      if (len > maxLen) {
        maxLen = len;
        minNodes = nodesCount;
      } else if (len == maxLen && nodesCount < minNodes) {
        minNodes = nodesCount;
      }

      // add current cumulative length to prefix for children
      prefix.add(cumLen);

      for (var edge in graph[u]) {
        int v = edge[0];
        int w = edge[1];
        if (v == parent) continue;
        dfs(v, u, depth + 1, cumLen + w, newLeft);
      }

      // backtrack
      prefix.removeLast();
      if (prevIdx == -1) {
        lastPos.remove(val);
      } else {
        lastPos[val] = prevIdx;
      }
    }

    dfs(0, -1, 0, 0, 0);
    return [maxLen, minNodes];
  }
}
```

## Golang

```go
func longestSpecialPath(edges [][]int, nums []int) []int {
	type edge struct {
		to int
		w  int
	}
	n := len(nums)
	adj := make([][]edge, n)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		adj[u] = append(adj[u], edge{v, w})
		adj[v] = append(adj[v], edge{u, w})
	}
	maxVal := 0
	for _, v := range nums {
		if v > maxVal {
			maxVal = v
		}
	}
	lastPos := make([]int, maxVal+1)
	for i := range lastPos {
		lastPos[i] = -1
	}

	var stack []int          // node indices along current path
	var pref []int64         // cumulative distance from root to each node in stack
	bestLen := int64(-1)    // longest length found
	minNodes := n + 1       // minimal nodes for that length

	var dfs func(u, parent, curLeft int)
	dfs = func(u, parent, curLeft int) {
		val := nums[u]
		prevIdx := lastPos[val]
		newLeft := curLeft
		if prevIdx != -1 && prevIdx+1 > newLeft {
			newLeft = prevIdx + 1
		}

		stack = append(stack, u)
		depth := len(stack) - 1

		var pathLen int64
		if newLeft == 0 {
			pathLen = pref[depth]
		} else {
			pathLen = pref[depth] - pref[newLeft-1]
		}
		nodesCnt := depth - newLeft + 1

		if pathLen > bestLen || (pathLen == bestLen && nodesCnt < minNodes) {
			bestLen = pathLen
			minNodes = nodesCnt
		}

		oldPos := lastPos[val]
		lastPos[val] = depth

		for _, e := range adj[u] {
			if e.to == parent {
				continue
			}
			pref = append(pref, pref[depth]+int64(e.w))
			dfs(e.to, u, newLeft)
			pref = pref[:len(pref)-1]
		}

		lastPos[val] = oldPos
		stack = stack[:len(stack)-1]
	}

	// start from root 0
	pref = []int64{0}
	dfs(0, -1, 0)

	return []int{int(bestLen), minNodes}
}
```

## Ruby

```ruby
def longest_special_path(edges, nums)
  n = nums.length
  adj = Array.new(n) { [] }
  edges.each do |u, v, l|
    adj[u] << [v, l]
    adj[v] << [u, l]
  end

  dist_at_depth = Array.new(n + 1, 0)
  last_occurrence = {}
  max_len = -1
  min_nodes = n + 1

  stack = []
  # [:enter, node, parent, depth, cum_dist, start_parent]
  # [:exit, node, prev_occ]
  stack << [:enter, 0, -1, 0, 0, 0]

  until stack.empty?
    frame = stack.pop
    if frame[0] == :enter
      _, node, parent, depth, cum_dist, start_parent = frame
      val = nums[node]
      prev_occ = last_occurrence[val]
      cur_start = start_parent
      cur_start = [cur_start, (prev_occ ? prev_occ + 1 : 0)].max

      stack << [:exit, node, prev_occ]

      last_occurrence[val] = depth
      dist_at_depth[depth] = cum_dist

      len = cum_dist - dist_at_depth[cur_start]
      nodes_cnt = depth - cur_start + 1
      if max_len < len || (max_len == len && nodes_cnt < min_nodes)
        max_len = len
        min_nodes = nodes_cnt
      end

      adj[node].each do |nbr, w|
        next if nbr == parent
        stack << [:enter, nbr, node, depth + 1, cum_dist + w, cur_start]
      end
    else
      _, node, prev_occ = frame
      val = nums[node]
      if prev_occ.nil?
        last_occurrence.delete(val)
      else
        last_occurrence[val] = prev_occ
      end
    end
  end

  [max_len, min_nodes]
end
```

## Scala

```scala
import scala.collection.mutable

object Solution {
  def longestSpecialPath(edges: Array[Array[Int]], nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val adj = Array.fill(n)(new mutable.ArrayBuffer[(Int, Int)]())
    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      val w = e(2)
      adj(u).append((v, w))
      adj(v).append((u, w))
    }

    case class Frame(node: Int,
                     parent: Int,
                     depth: Int,
                     cumDist: Long,
                     leftBoundParent: Int,
                     idx: Int,               // -1 = entering, >=0 processing children
                     curLeft: Int,           // valid after entry
                     oldPrev: Option[Int])   // previous position of nums[node]

    val lastPos = mutable.HashMap.empty[Int, Int]          // value -> depth index
    val distAtDepth = new Array[Long](n)                  // cumulative distance at each depth

    var bestLen: Long = -1L
    var minNodes: Int = Int.MaxValue

    val stack = new mutable.ArrayStack[Frame]()
    stack.push(Frame(0, -1, 0, 0L, 0, -1, 0, None))

    while (stack.nonEmpty) {
      val fr = stack.pop()
      if (fr.idx == -1) { // entering node
        val prevPos = lastPos.getOrElse(nums(fr.node), -1)
        val curLeft = math.max(fr.leftBoundParent, if (prevPos == -1) 0 else prevPos + 1)

        distAtDepth(fr.depth) = fr.cumDist

        val startDist = if (curLeft == 0) 0L else distAtDepth(curLeft - 1)
        val len = fr.cumDist - startDist
        val nodesCnt = fr.depth - curLeft + 1

        if (len > bestLen || (len == bestLen && nodesCnt < minNodes)) {
          bestLen = len
          minNodes = nodesCnt
        }

        val oldPrevOpt = lastPos.get(nums(fr.node))
        lastPos(nums(fr.node)) = fr.depth

        // push frame back for child processing, storing curLeft and oldPrev
        stack.push(fr.copy(idx = 0, curLeft = curLeft, oldPrev = oldPrevOpt))
      } else if (fr.idx < adj(fr.node).size) {
        val (v, w) = adj(fr.node)(fr.idx)
        // push current frame with next child index
        stack.push(fr.copy(idx = fr.idx + 1))

        if (v != fr.parent) {
          // child frame, pass curLeft as its leftBoundParent
          stack.push(Frame(v, fr.node, fr.depth + 1,
            fr.cumDist + w, fr.curLeft, -1, 0, None))
        }
      } else {
        // exiting node, restore lastPos
        fr.oldPrev match {
          case Some(prev) => lastPos(nums(fr.node)) = prev
          case None       => lastPos.remove(nums(fr.node))
        }
      }
    }

    Array(bestLen.toInt, minNodes)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_special_path(edges: Vec<Vec<i32>>, nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        // build adjacency list
        let mut adj: Vec<Vec<(usize, i32)>> = vec![Vec::new(); n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2];
            adj[u].push((v, w));
            adj[v].push((u, w));
        }

        // last occurrence depth for each value
        let max_val = *nums.iter().max().unwrap() as usize;
        let mut last: Vec<i32> = vec![-1; max_val + 1];

        // stack to simulate recursion
        #[derive(Clone)]
        struct Frame {
            node: usize,
            parent: usize,
            depth: usize,
            start: usize,
            cum: i64,
            child_idx: usize,
            prev_last: i32,
        }

        let mut stack: Vec<Frame> = Vec::with_capacity(n);
        let mut cum_stack: Vec<i64> = Vec::with_capacity(n);

        // root initialization
        cum_stack.push(0);
        let root_val = nums[0] as usize;
        let prev_root = last[root_val];
        last[root_val] = 0; // depth of root is 0
        stack.push(Frame {
            node: 0,
            parent: n, // sentinel
            depth: 0,
            start: 0,
            cum: 0,
            child_idx: 0,
            prev_last: prev_root,
        });

        let mut best_len: i64 = 0;
        let mut best_nodes: usize = 1; // single node path

        while let Some(frame) = stack.last_mut() {
            if frame.child_idx < adj[frame.node].len() {
                let (next, w) = {
                    let (nxt, wt) = adj[frame.node][frame.child_idx];
                    (nxt, wt)
                };
                frame.child_idx += 1;
                if next == frame.parent {
                    continue;
                }
                // entering child
                let depth = frame.depth + 1;
                let cum = frame.cum + w as i64;
                let val = nums[next] as usize;
                let prev_last = last[val];
                let mut start = frame.start;
                if prev_last != -1 && (prev_last as usize) >= start {
                    start = (prev_last as usize) + 1;
                }
                // update last occurrence
                last[val] = depth as i32;

                // compute path length and node count
                let prefix = if start == 0 { 0 } else { cum_stack[start - 1] };
                let length = cum - prefix;
                let nodes_cnt = depth - start + 1;

                if length > best_len {
                    best_len = length;
                    best_nodes = nodes_cnt;
                } else if length == best_len && nodes_cnt < best_nodes {
                    best_nodes = nodes_cnt;
                }

                // push child frame
                cum_stack.push(cum);
                stack.push(Frame {
                    node: next,
                    parent: frame.node,
                    depth,
                    start,
                    cum,
                    child_idx: 0,
                    prev_last,
                });
            } else {
                // exiting node, restore last occurrence
                let val = nums[frame.node] as usize;
                last[val] = frame.prev_last;
                cum_stack.pop();
                stack.pop();
            }
        }

        vec![best_len as i32, best_nodes as i32]
    }
}
```

## Racket

```racket
(define/contract (longest-special-path edges nums)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length nums))
         (adj (make-vector n '()))
         (ht (make-hash))
         (depthDist (make-vector n 0))
         (best-len (box -1))
         (best-nodes (box 0)))
    ;; build adjacency list
    (for-each
     (lambda (e)
       (let ((u (list-ref e 0))
             (v (list-ref e 1))
             (w (list-ref e 2)))
         (vector-set! adj u (cons (cons v w) (vector-ref adj u)))
         (vector-set! adj v (cons (cons u w) (vector-ref adj v)))))
     edges)
    ;; depth‑first search
    (letrec ((dfs
              (lambda (node parent depth cur-left dist)
                (vector-set! depthDist depth dist)
                (let* ((val (list-ref nums node))
                       (prev (hash-ref ht val #f))
                       (new-left (if prev
                                     (max cur-left (+ prev 1))
                                     cur-left)))
                  (hash-set! ht val depth)
                  (let* ((start-dist (vector-ref depthDist new-left))
                         (path-length (- dist start-dist))
                         (node-count (+ 1 (- depth new-left))))
                    (when (or (> path-length (unbox best-len))
                              (and (= path-length (unbox best-len))
                                   (< node-count (unbox best-nodes))))
                      (set-box! best-len path-length)
                      (set-box! best-nodes node-count)))
                  ;; recurse children
                  (for-each
                   (lambda (pair)
                     (let ((nbr (car pair))
                           (w   (cdr pair)))
                       (when (not (= nbr parent))
                         (dfs nbr node (+ depth 1) new-left (+ dist w)))))
                   (vector-ref adj node))
                  ;; restore hash table entry
                  (if prev
                      (hash-set! ht val prev)
                      (hash-remove! ht val))))))
      (dfs 0 -1 0 0 0))
    (list (unbox best-len) (unbox best-nodes))))
```

## Erlang

```erlang
-spec longest_special_path(Edges :: [[integer()]], Nums :: [integer()]) -> [integer()].
longest_special_path(Edges, Nums) ->
    % Build adjacency list as a map: Node => [{Neighbor, Length}, ...]
    Graph = lists:foldl(fun([U, V, L], G) ->
                G1 = maps:put(U, [{V, L} | maps:get(U, G, [])], G),
                maps:put(V, [{U, L} | maps:get(V, G1, [])], G1)
            end, #{}, Edges),

    N = length(Nums),
    NumsArr = array:from_list(Nums),
    DistArray0 = array:new(N, {default, 0}),
    % Start DFS from root (node 0)
    {BestLen, MinNodes} = dfs(0, -1, 0, 0, 0,
                              DistArray0, maps:new(),
                              Graph, NumsArr, -1, 0),
    [BestLen, MinNodes].

%% Depth‑first search.
dfs(Node, Parent, Depth, Dist, CurLeft,
    DistArr, LastPosMap,
    Graph, NumsArr, BestLen, MinNodes) ->

    % Record distance for current depth
    DistArr1 = array:set(Depth, Dist, DistArr),

    Value = array:get(Node, NumsArr),
    PrevDepth = maps:get(Value, LastPosMap, -1),
    NewLeft = case PrevDepth of
                  -1 -> CurLeft;
                  _  -> erlang:max(CurLeft, PrevDepth + 1)
              end,

    LeftDist = array:get(NewLeft, DistArr1),
    PathLen = Dist - LeftDist,
    NodesCnt = Depth - NewLeft + 1,

    {BestLen1, MinNodes1} =
        if
            PathLen > BestLen ->
                {PathLen, NodesCnt};
            PathLen == BestLen, NodesCnt < MinNodes ->
                {BestLen, NodesCnt};
            true ->
                {BestLen, MinNodes}
        end,

    UpdatedLastPos = maps:put(Value, Depth, LastPosMap),

    Children = maps:get(Node, Graph, []),
    lists:foldl(
      fun({Nb, L}, {BL, MN}) ->
          if Nb =:= Parent ->
                 {BL, MN};
             true ->
                 ChildDist = Dist + L,
                 dfs(Nb, Node, Depth + 1, ChildDist, NewLeft,
                     DistArr1, UpdatedLastPos,
                     Graph, NumsArr, BL, MN)
          end
      end,
      {BestLen1, MinNodes1},
      Children).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_special_path(edges :: [[integer]], nums :: [integer]) :: [integer]
  def longest_special_path(edges, nums) do
    n = length(nums)

    adj =
      Enum.reduce(edges, %{}, fn [u, v, l], acc ->
        acc
        |> Map.update(u, [{v, l}], fn lst -> [{v, l} | lst] end)
        |> Map.update(v, [{u, l}], fn lst -> [{u, l} | lst] end)
      end)

    dfs(
      [{:enter, 0, -1, 0}],
      -1,
      %{},
      [],
      %{},
      -1,
      n + 1,
      nums,
      adj
    )
  end

  defp dfs([], _depth, _dist_map, _valid_stack, _val_map, max_len, min_nodes, _nums, _adj) do
    [max_len, min_nodes]
  end

  # Enter a node
  defp dfs([{:enter, node, parent, edge_len} | rest], depth, dist_map, valid_stack, val_map,
           max_len, min_nodes, nums, adj) do
    cur_depth = depth + 1
    parent_dist = if depth < 0, do: 0, else: Map.get(dist_map, depth)
    cur_dist = parent_dist + edge_len

    node_val = Enum.at(nums, node)
    prev_occurrence = Map.get(val_map, node_val)

    # children entries (excluding parent)
    children =
      for {nbr, w} <- Map.get(adj, node, []), nbr != parent do
        {:enter, nbr, node, w}
      end

    new_stack = [{:exit, node, prev_occurrence} | Enum.reverse(children)] ++ rest

    dist_map2 = Map.put(dist_map, cur_depth, cur_dist)
    val_map2 = Map.put(val_map, node_val, cur_depth)

    parent_valid_start =
      case valid_stack do
        [] -> 0
        [v | _] -> v
      end

    cur_valid_start =
      if prev_occurrence == nil do
        parent_valid_start
      else
        max(parent_valid_start, prev_occurrence + 1)
      end

    valid_stack2 = [cur_valid_start | valid_stack]

    start_dist = Map.get(dist_map2, cur_valid_start)
    len = cur_dist - start_dist
    nodes_cnt = cur_depth - cur_valid_start + 1

    {new_max_len, new_min_nodes} =
      cond do
        len > max_len -> {len, nodes_cnt}
        len == max_len and nodes_cnt < min_nodes -> {max_len, nodes_cnt}
        true -> {max_len, min_nodes}
      end

    dfs(
      new_stack,
      cur_depth,
      dist_map2,
      valid_stack2,
      val_map2,
      new_max_len,
      new_min_nodes,
      nums,
      adj
    )
  end

  # Exit a node
  defp dfs([{:exit, node, prev_occurrence} | rest], depth, dist_map, valid_stack,
           val_map, max_len, min_nodes, nums, _adj) do
    # Remove current node's data
    dist_map2 = Map.delete(dist_map, depth)
    [_cur_valid_start | valid_rest] = valid_stack

    node_val = Enum.at(nums, node)

    val_map2 =
      if prev_occurrence == nil do
        Map.delete(val_map, node_val)
      else
        Map.put(val_map, node_val, prev_occurrence)
      end

    dfs(
      rest,
      depth - 1,
      dist_map2,
      valid_rest,
      val_map2,
      max_len,
      min_nodes,
      nums,
      %{}
    )
  end
end
```
