# 3486. Longest Special Path II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        vector<vector<pair<int,int>>> g(n);
        for (auto &e : edges) {
            int u=e[0], v=e[1], w=e[2];
            g[u].push_back({v,w});
            g[v].push_back({u,w});
        }

        unordered_map<int, vector<int>> occ; // positions on current root->node path
        multiset<int> forced;   // fronts of values with count >=3 (must be excluded)
        multiset<int> optional; // fronts of values with count ==2 (may keep one)

        vector<int> path;               // node indices along current path
        vector<long long> prefDist;     // cumulative distance from root

        long long bestLen = -1;
        int minNodes = INT_MAX;

        function<void(int,int,long long)> dfs = [&](int u, int parent, long long wFromParent){
            int depth = (int)path.size(); // index of this node after push
            path.push_back(u);
            if (depth==0) prefDist.push_back(0);
            else prefDist.push_back(prefDist.back() + wFromParent);

            int val = nums[u];
            auto &vec = occ[val];
            vec.push_back(depth);
            int sz = (int)vec.size();
            if (sz == 2) {
                optional.insert(vec[0]);
            } else if (sz == 3) {
                auto it = optional.find(vec[0]);
                if (it != optional.end()) optional.erase(it);
                forced.insert(vec[0]);
            }

            // compute minimal start index L
            int maxForced = forced.empty() ? -1 : *forced.rbegin();
            int secondOpt = -1;
            if (optional.size() >= 2) {
                auto it = optional.end(); --it; // largest
                //int largest = *it;
                --it; // second largest
                secondOpt = *it;
            }
            int required = max(maxForced, secondOpt);
            int L = (required == -1) ? 0 : required + 1;

            long long length = prefDist.back() - (L==0?0:prefDist[L-1]);
            int nodesCnt = depth - L + 1;
            if (length > bestLen) {
                bestLen = length;
                minNodes = nodesCnt;
            } else if (length == bestLen && nodesCnt < minNodes) {
                minNodes = nodesCnt;
            }

            for (auto &p : g[u]) {
                int v = p.first, w = p.second;
                if (v == parent) continue;
                dfs(v, u, w);
            }

            // backtrack removal of current node
            sz = (int)vec.size();
            if (sz == 2) { // currently count==2, front in optional
                auto it = optional.find(vec[0]);
                if (it != optional.end()) optional.erase(it);
            } else if (sz == 3) { // currently count==3, front in forced
                auto it = forced.find(vec[0]);
                if (it != forced.end()) forced.erase(it);
                optional.insert(vec[0]); // after removal becomes count==2
            }
            vec.pop_back();
            if (vec.empty()) occ.erase(val); // optional cleanup

            path.pop_back();
            prefDist.pop_back();
        };

        dfs(0, -1, 0);

        return {(int)bestLen, minNodes};
    }
};
```

## Java

```java
class Solution {
    public int[] longestSpecialPath(int[][] edges, int[] nums) {
        int n = nums.length;
        List<int[]>[] adj = new ArrayList[n];
        for (int i = 0; i < n; ++i) adj[i] = new ArrayList<>();
        for (int[] e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].add(new int[]{v, w});
            adj[v].add(new int[]{u, w});
        }

        int maxVal = 0;
        for (int x : nums) if (x > maxVal) maxVal = x;
        int[] last1 = new int[maxVal + 1];
        int[] last2 = new int[maxVal + 1];
        Arrays.fill(last1, -1);
        Arrays.fill(last2, -1);

        TreeMap<Integer, Integer> dupPosCount = new TreeMap<>();

        // stacks for iterative DFS
        Deque<int[]> stack = new ArrayDeque<>(); // {node,parent,edgeLen,state}
        stack.push(new int[]{0, -1, 0, 0}); // state 0 = entry, 1 = exit

        int[] depthArr = new int[n];
        long[] distAtDepth = new long[n]; // distance from root at each depth
        Deque<RevertInfo> revertStack = new ArrayDeque<>();

        long bestLen = -1;
        int minNodes = Integer.MAX_VALUE;

        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            int node = cur[0];
            int parent = cur[1];
            int edgeLen = cur[2];
            int state = cur[3];

            if (state == 0) { // entry
                int depth = (parent == -1) ? 0 : depthArr[parent] + 1;
                depthArr[node] = depth;
                long dist = (parent == -1) ? 0L : distAtDepth[depth - 1] + edgeLen;
                distAtDepth[depth] = dist;

                int val = nums[node];
                int oldLast1 = last1[val];
                int oldLast2 = last2[val];

                // update multiset
                if (oldLast1 != -1) addPos(dupPosCount, oldLast1);
                if (oldLast2 != -1) removePos(dupPosCount, oldLast2);

                last2[val] = oldLast1;
                last1[val] = depth;

                // compute earliest allowed ancestor index
                int aIdx = 0;
                if (!dupPosCount.isEmpty()) {
                    Integer firstKey = dupPosCount.lastKey();
                    int cntFirst = dupPosCount.get(firstKey);
                    int secondPos;
                    if (cntFirst >= 2) {
                        secondPos = firstKey;
                    } else {
                        Integer lower = dupPosCount.lowerKey(firstKey);
                        secondPos = (lower == null) ? -1 : lower;
                    }
                    aIdx = (secondPos == -1) ? 0 : secondPos + 1;
                }

                long length = distAtDepth[depth] - distAtDepth[aIdx];
                int nodesCnt = depth - aIdx + 1;

                if (length > bestLen) {
                    bestLen = length;
                    minNodes = nodesCnt;
                } else if (length == bestLen && nodesCnt < minNodes) {
                    minNodes = nodesCnt;
                }

                // push exit frame
                stack.push(new int[]{node, parent, edgeLen, 1});
                // push children frames
                for (int[] e : adj[node]) {
                    int nb = e[0];
                    if (nb == parent) continue;
                    stack.push(new int[]{nb, node, e[1], 0});
                }

                revertStack.push(new RevertInfo(val, oldLast1, oldLast2));
            } else { // exit
                RevertInfo rev = revertStack.pop();
                int val = rev.val;
                int oldLast1 = rev.prevLast1;
                int oldLast2 = rev.prevLast2;

                // reverse multiset changes
                if (oldLast1 != -1) removePos(dupPosCount, oldLast1);
                if (oldLast2 != -1) addPos(dupPosCount, oldLast2);

                last1[val] = oldLast1;
                last2[val] = oldLast2;
            }
        }

        return new int[]{(int) bestLen, minNodes};
    }

    private void addPos(TreeMap<Integer, Integer> map, int pos) {
        map.merge(pos, 1, Integer::sum);
    }

    private void removePos(TreeMap<Integer, Integer> map, int pos) {
        int cnt = map.get(pos);
        if (cnt == 1) map.remove(pos);
        else map.put(pos, cnt - 1);
    }

    private static class RevertInfo {
        int val;
        int prevLast1;
        int prevLast2;
        RevertInfo(int v, int l1, int l2) {
            this.val = v;
            this.prevLast1 = l1;
            this.prevLast2 = l2;
        }
    }
}
```

## Python

```python
import sys
from collections import defaultdict, deque

class Solution(object):
    def longestSpecialPath(self, edges, nums):
        """
        :type edges: List[List[int]]
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        parent = [-1] * n
        depth = [0] * n
        dist = [0] * n
        stack = [0]
        parent[0] = -2
        while stack:
            u = stack.pop()
            for v, w in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                dist[v] = dist[u] + w
                stack.append(v)

        freq = defaultdict(int)
        dupCount = 0          # number of values with frequency == 2
        threeCount = 0        # number of values with frequency >= 3 (should be 0 for valid window)
        window = deque()      # nodes in current valid window, leftmost is start

        best_len = -1
        best_nodes = 10 ** 9

        sys.setrecursionlimit(200000)

        def dfs(u):
            nonlocal dupCount, threeCount, best_len, best_nodes

            val = nums[u]
            freq[val] += 1
            if freq[val] == 2:
                dupCount += 1
            elif freq[val] == 3:
                threeCount += 1

            window.append(u)
            removed = []

            while threeCount > 0 or dupCount > 1:
                left_node = window.popleft()
                removed.append(left_node)
                vval = nums[left_node]
                if freq[vval] == 3:
                    threeCount -= 1
                if freq[vval] == 2:
                    dupCount -= 1
                freq[vval] -= 1

            start_node = window[0]
            cur_len = dist[u] - dist[start_node]
            node_cnt = depth[u] - depth[start_node] + 1
            if cur_len > best_len or (cur_len == best_len and node_cnt < best_nodes):
                best_len = cur_len
                best_nodes = node_cnt

            for v, _ in adj[u]:
                if v == parent[u]:
                    continue
                dfs(v)

            # backtrack: remove current node from right side
            val = nums[u]
            if freq[val] == 2:
                dupCount -= 1
            elif freq[val] == 3:
                threeCount -= 1
            freq[val] -= 1
            window.pop()

            # restore nodes removed from left during this call
            for rn in reversed(removed):
                vval = nums[rn]
                freq[vval] += 1
                if freq[vval] == 2:
                    dupCount += 1
                elif freq[vval] == 3:
                    threeCount += 1
                window.appendleft(rn)

        dfs(0)
        return [best_len, best_nodes]
```

## Python3

```python
import sys, collections, heapq
from typing import List

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        sys.setrecursionlimit(200000)

        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        occ = collections.defaultdict(list)          # value -> list of depths (stack)
        dup_second_heap = []                         # (second_latest_depth, value)
        third_heap = []                              # (-third_latest_depth, value)
        cnt_dup_vals = 0                             # number of values with at least two occurrences
        dist = []                                    # distance from root for each depth

        best_len = -1
        best_nodes = 10**9

        def dfs(u: int, parent: int, curDist: int):
            nonlocal cnt_dup_vals, best_len, best_nodes

            depth = len(dist)          # current depth index
            dist.append(curDist)

            val = nums[u]
            lst = occ[val]
            prev_len = len(lst)
            lst.append(depth)

            if prev_len == 1:                     # becomes duplicated (2 occurrences)
                cnt_dup_vals += 1
                heapq.heappush(dup_second_heap, (lst[-2], val))
            elif prev_len >= 2:                   # already duplicated, update second latest depth
                heapq.heappush(dup_second_heap, (lst[-2], val))

            if len(lst) >= 3:
                heapq.heappush(third_heap, (-lst[-3], val))

            L = 0

            while third_heap:
                nd, v = third_heap[0]
                dth = -nd
                llist = occ[v]
                if len(llist) >= 3 and llist[-3] == dth:
                    break
                heapq.heappop(third_heap)
            if third_heap:
                L = max(L, dth + 1)

            while dup_second_heap:
                sd, v = dup_second_heap[0]
                llist = occ[v]
                if len(llist) >= 2 and llist[-2] == sd:
                    break
                heapq.heappop(dup_second_heap)
            if cnt_dup_vals >= 2 and dup_second_heap:
                L = max(L, dup_second_heap[0][0] + 1)

            path_len = curDist - dist[L]
            node_cnt = depth - L + 1

            if path_len > best_len or (path_len == best_len and node_cnt < best_nodes):
                best_len = path_len
                best_nodes = node_cnt

            for v, w in adj[u]:
                if v == parent:
                    continue
                dfs(v, u, curDist + w)

            # backtrack
            lst.pop()
            if prev_len == 2:          # was duplicated, now becomes single
                cnt_dup_vals -= 1
            # no need to adjust heaps; stale entries will be ignored later

            dist.pop()

        dfs(0, -1, 0)
        return [best_len, best_nodes]
```

## C

```c
#include <stdlib.h>
#include <limits.h>

struct Op {
    int val;
};

static int N;
static int *headArr;
static int *toArr;
static int *weightArr;
static int *nextArr;
static int edgePtr;

static int maxValGlobal;
static int *cntVals;
static int *pathVals;
static long long *prefDist;
static struct Op *opStack;

static int leftIdx, opSize, dupVals, overVals, depthIdx;
static long long bestLen;
static int minNodes;
static int *numsGlobal;

/* add undirected edge */
static void addEdge(int u, int v, int w) {
    toArr[edgePtr] = v;
    weightArr[edgePtr] = w;
    nextArr[edgePtr] = headArr[u];
    headArr[u] = edgePtr++;
}

/* depth‑first search */
static void dfs(int u, int parent, int wParent) {
    int savedLeft = leftIdx;
    int savedOpSize = opSize;

    /* push current node */
    pathVals[depthIdx] = numsGlobal[u];
    if (depthIdx == 0)
        prefDist[depthIdx] = 0;
    else
        prefDist[depthIdx] = prefDist[depthIdx - 1] + wParent;

    int val = numsGlobal[u];
    cntVals[val]++;
    if (cntVals[val] == 2) dupVals++;
    else if (cntVals[val] == 3) overVals++;

    /* shrink window while invalid */
    while (dupVals > 1 || overVals > 0) {
        int v = pathVals[leftIdx];
        if (cntVals[v] == 2) dupVals--;
        else if (cntVals[v] == 3) overVals--;
        cntVals[v]--;
        opStack[opSize].val = v;
        opSize++;
        leftIdx++;
    }

    /* evaluate current window */
    long long curLen = prefDist[depthIdx] - (leftIdx > 0 ? prefDist[leftIdx - 1] : 0);
    int nodesCnt = depthIdx - leftIdx + 1;
    if (curLen > bestLen || (curLen == bestLen && nodesCnt < minNodes)) {
        bestLen = curLen;
        minNodes = nodesCnt;
    }

    depthIdx++;

    for (int e = headArr[u]; e != -1; e = nextArr[e]) {
        int v = toArr[e];
        if (v == parent) continue;
        dfs(v, u, weightArr[e]);
    }

    /* backtrack: undo left moves */
    while (opSize > savedOpSize) {
        opSize--;
        leftIdx--;
        int v = opStack[opSize].val;
        cntVals[v]++;
        if (cntVals[v] == 2) dupVals++;
        else if (cntVals[v] == 3) overVals++;
    }
    leftIdx = savedLeft;

    /* remove current node's contribution */
    val = numsGlobal[u];
    if (cntVals[val] == 2) dupVals--;
    else if (cntVals[val] == 3) overVals--;
    cntVals[val]--;

    depthIdx--;
}

int* longestSpecialPath(int** edges, int edgesSize, int* edgesColSize, int* nums, int numsSize, int* returnSize){
    N = numsSize;
    numsGlobal = nums;

    /* adjacency list allocation */
    headArr = (int*)malloc(N * sizeof(int));
    for (int i = 0; i < N; ++i) headArr[i] = -1;
    edgePtr = 0;
    toArr = (int*)malloc(2 * edgesSize * sizeof(int));
    weightArr = (int*)malloc(2 * edgesSize * sizeof(int));
    nextArr = (int*)malloc(2 * edgesSize * sizeof(int));

    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        int w = edges[i][2];
        addEdge(u, v, w);
        addEdge(v, u, w);
    }

    /* value range */
    maxValGlobal = 0;
    for (int i = 0; i < N; ++i)
        if (nums[i] > maxValGlobal) maxValGlobal = nums[i];
    cntVals = (int*)calloc(maxValGlobal + 1, sizeof(int));

    pathVals = (int*)malloc(N * sizeof(int));
    prefDist = (long long*)malloc(N * sizeof(long long));
    opStack = (struct Op*)malloc(N * sizeof(struct Op));

    leftIdx = 0;
    opSize = 0;
    dupVals = 0;
    overVals = 0;
    depthIdx = 0;
    bestLen = -1;
    minNodes = INT_MAX;

    dfs(0, -1, 0);

    int *res = (int*)malloc(2 * sizeof(int));
    res[0] = (int)bestLen;
    res[1] = minNodes;
    *returnSize = 2;

    /* free allocated memory */
    free(headArr);
    free(toArr);
    free(weightArr);
    free(nextArr);
    free(cntVals);
    free(pathVals);
    free(prefDist);
    free(opStack);

    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private Dictionary<int, List<int>> occ = new Dictionary<int, List<int>>();
    private SortedDictionary<int, int> dupSecondCounts = new SortedDictionary<int, int>();
    private SortedDictionary<int, int> tripleIdxCounts = new SortedDictionary<int, int>();
    private int dupValsCount = 0;
    private List<int> path = new List<int>();
    private List<long> prefDist = new List<long>();
    private long bestLen = -1;
    private int minNodes = int.MaxValue;

    private void AddToMap(SortedDictionary<int, int> dict, int key) {
        if (dict.ContainsKey(key)) dict[key]++; else dict[key] = 1;
    }
    private void RemoveFromMap(SortedDictionary<int, int> dict, int key) {
        if (!dict.ContainsKey(key)) return;
        if (dict[key] == 1) dict.Remove(key);
        else dict[key]--;
    }

    private void AddNode(int node, int[] nums, long dist) {
        int val = nums[node];
        if (!occ.TryGetValue(val, out var list)) {
            list = new List<int>();
            occ[val] = list;
        }
        int occCount = list.Count; // before adding

        // handle duplicate structures before push
        if (occCount == 1) {
            AddToMap(dupSecondCounts, list[0]);
            dupValsCount++;
        } else if (occCount >= 2) {
            // replace old second-last entry
            RemoveFromMap(dupSecondCounts, list[occCount - 2]);
        }

        // handle triple insertion when count becomes 3
        if (occCount == 2) {
            AddToMap(tripleIdxCounts, list[0]);
        }

        int curIdx = path.Count;
        list.Add(curIdx);
        path.Add(node);
        prefDist.Add(dist);

        // after push, add new second-last entry if needed
        if (occCount >= 2) {
            AddToMap(dupSecondCounts, list[occCount - 1]); // new second-last
        }

        // compute best using current window
        int left = 0;
        if (dupValsCount > 1 && dupSecondCounts.Count > 0) {
            left = Math.Max(left, dupSecondCounts.First().Key + 1);
        }
        if (tripleIdxCounts.Count > 0) {
            left = Math.Max(left, tripleIdxCounts.Last().Key + 1);
        }

        long curLen = prefDist[curIdx] - (left > 0 ? prefDist[left - 1] : 0L);
        int nodesCnt = curIdx - left + 1;

        if (curLen > bestLen) {
            bestLen = curLen;
            minNodes = nodesCnt;
        } else if (curLen == bestLen && nodesCnt < minNodes) {
            minNodes = nodesCnt;
        }
    }

    private void RemoveNode(int node, int[] nums) {
        int val = nums[node];
        var list = occ[val];
        int cnt = list.Count; // includes current node

        if (cnt == 1) {
            // nothing to remove from structures
        } else if (cnt == 2) {
            RemoveFromMap(dupSecondCounts, list[0]);
            dupValsCount--;
        } else { // cnt >=3
            // remove current duplicate entry
            RemoveFromMap(dupSecondCounts, list[cnt - 2]);

            // after removal, if new count >=2 add new duplicate entry
            if (cnt - 1 >= 2) {
                AddToMap(dupSecondCounts, list[cnt - 3]);
            } else {
                // becomes single occurrence, decrement dupValsCount
                dupValsCount--;
            }
        }

        // handle triple removal when count drops from 3 to 2
        if (cnt == 3) {
            RemoveFromMap(tripleIdxCounts, list[0]);
        }

        // pop structures
        list.RemoveAt(cnt - 1);
        path.RemoveAt(path.Count - 1);
        prefDist.RemoveAt(prefDist.Count - 1);
    }

    public int[] LongestSpecialPath(int[][] edges, int[] nums) {
        int n = nums.Length;
        var graph = new List<(int to, int len)>[n];
        for (int i = 0; i < n; i++) graph[i] = new List<(int, int)>();
        foreach (var e in edges) {
            int u = e[0], v = e[1], w = e[2];
            graph[u].Add((v, w));
            graph[v].Add((u, w));
        }

        var stack = new Stack<(int node, int parent, long dist, int state)>();
        stack.Push((0, -1, 0L, 0));

        while (stack.Count > 0) {
            var cur = stack.Pop();
            if (cur.state == 0) { // pre
                AddNode(cur.node, nums, cur.dist);
                stack.Push((cur.node, cur.parent, cur.dist, 1)); // post frame
                // push children
                var neighbors = graph[cur.node];
                for (int i = neighbors.Count - 1; i >= 0; i--) {
                    var nb = neighbors[i];
                    if (nb.to == cur.parent) continue;
                    stack.Push((nb.to, cur.node, cur.dist + nb.len, 0));
                }
            } else { // post
                RemoveNode(cur.node, nums);
            }
        }

        return new int[] { (int)bestLen, minNodes };
    }
}
```

## Javascript

```javascript
/****
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

    // MaxHeap with lazy deletions
    class MaxHeap {
        constructor() {
            this.heap = [];
            this.del = new Map(); // value -> count to delete lazily
        }
        _siftUp(i) {
            const h = this.heap;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (h[p] >= h[i]) break;
                [h[p], h[i]] = [h[i], h[p]];
                i = p;
            }
        }
        _siftDown(i) {
            const h = this.heap;
            const n = h.length;
            while (true) {
                let l = i * 2 + 1, r = l + 1, largest = i;
                if (l < n && h[l] > h[largest]) largest = l;
                if (r < n && h[r] > h[largest]) largest = r;
                if (largest === i) break;
                [h[i], h[largest]] = [h[largest], h[i]];
                i = largest;
            }
        }
        _cleanTop() {
            const h = this.heap, d = this.del;
            while (h.length) {
                const top = h[0];
                if (!d.has(top)) break;
                // remove one pending deletion
                const cnt = d.get(top);
                if (cnt === 1) d.delete(top);
                else d.set(top, cnt - 1);
                // pop the top element
                const last = h.pop();
                if (h.length) {
                    h[0] = last;
                    this._siftDown(0);
                }
            }
        }
        push(val) {
            this.heap.push(val);
            this._siftUp(this.heap.length - 1);
        }
        remove(val) { // lazy delete
            const d = this.del;
            d.set(val, (d.get(val) || 0) + 1);
            this._cleanTop();
        }
        peek() {
            this._cleanTop();
            return this.heap.length ? this.heap[0] : -1;
        }
        popTop() { // remove and return top
            this._cleanTop();
            if (!this.heap.length) return -1;
            const top = this.heap[0];
            const last = this.heap.pop();
            if (this.heap.length) {
                this.heap[0] = last;
                this._siftDown(0);
            }
            return top;
        }
        secondMax() {
            const first = this.peek();
            if (first === -1) return -1;
            // temporarily remove the max
            this.popTop();
            const second = this.peek();
            // restore the removed max
            this.push(first);
            return second;
        }
    }

    const occMap = new Map(); // value -> array of depths
    const path = [];          // node ids along current root->node path
    const distArr = [];       // distance from root for each depth index

    const heap = new MaxHeap();   // stores second-last positions
    let maxThirdPos = -1;         // maximum third-last position among all values
    const maxThirdStack = [];

    let bestLen = -1;
    let minNodes = Infinity;

    // iterative DFS with explicit stack for entry/exit handling
    const stack = [{node: 0, parent: -1, depth: 0, dist: 0, stage: 0}];

    while (stack.length) {
        const frame = stack.pop();
        if (frame.stage === 0) { // entering node
            const {node, parent, depth, dist} = frame;
            const val = nums[node];
            let occ = occMap.get(val);
            if (!occ) {
                occ = [];
                occMap.set(val, occ);
            }
            const oldSecond = occ.length >= 2 ? occ[occ.length - 2] : -1;
            const oldThird = occ.length >= 3 ? occ[occ.length - 3] : -1;

            // add current depth
            occ.push(depth);
            const newSecond = occ.length >= 2 ? occ[occ.length - 2] : -1;
            const newThird = occ.length >= 3 ? occ[occ.length - 3] : -1;

            if (oldSecond !== -1) heap.remove(oldSecond);
            if (newSecond !== -1) heap.push(newSecond);

            maxThirdStack.push(maxThirdPos);
            if (newThird !== -1 && newThird > maxThirdPos) {
                maxThirdPos = newThird;
            }

            // push onto path structures
            path.push(node);
            distArr.push(dist);

            // compute left bound L
            const lb1 = maxThirdPos === -1 ? 0 : maxThirdPos + 1;
            const secondMax = heap.secondMax();
            const lb2 = secondMax === -1 ? 0 : secondMax + 1;
            let L = Math.max(lb1, lb2);
            if (L < 0) L = 0; // safety

            const length = dist - distArr[L];
            const nodesCount = depth - L + 1;

            if (length > bestLen) {
                bestLen = length;
                minNodes = nodesCount;
            } else if (length === bestLen && nodesCount < minNodes) {
                minNodes = nodesCount;
            }

            // schedule exit processing
            stack.push({
                node,
                parent,
                depth,
                dist,
                stage: 1,
                val,
                oldSecond,
                newSecond
            });

            // push children (enter stage)
            for (const [nei, w] of adj[node]) {
                if (nei === parent) continue;
                stack.push({node: nei, parent: node, depth: depth + 1, dist: dist + w, stage: 0});
            }
        } else { // exiting node, revert changes
            const {val, oldSecond, newSecond} = frame;

            if (newSecond !== -1) heap.remove(newSecond);
            if (oldSecond !== -1) heap.push(oldSecond);

            maxThirdPos = maxThirdStack.pop();

            path.pop();
            distArr.pop();

            const occ = occMap.get(val);
            occ.pop(); // remove current depth
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
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }

    const maxVal = Math.max(...nums);
    const occ: number[][] = new Array(maxVal + 1);
    const dupFirstDepth = new Int32Array(maxVal + 1).fill(-1);
    const constrDepth = new Int32Array(maxVal + 1).fill(-1);

    class Heap<T> {
        data: T[] = [];
        cmp: (a: T, b: T) => boolean;
        constructor(cmp: (a: T, b: T) => boolean) { this.cmp = cmp; }
        size(): number { return this.data.length; }
        peek(): T | undefined { return this.data[0]; }
        push(item: T): void {
            const a = this.data;
            a.push(item);
            let i = a.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (!this.cmp(a[i], a[p])) break;
                [a[i], a[p]] = [a[p], a[i]];
                i = p;
            }
        }
        pop(): T | undefined {
            const a = this.data;
            if (a.length === 0) return undefined;
            const top = a[0];
            const last = a.pop()!;
            if (a.length > 0) {
                a[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1, r = l + 1, smallest = i;
                    if (l < a.length && this.cmp(a[l], a[smallest])) smallest = l;
                    if (r < a.length && this.cmp(a[r], a[smallest])) smallest = r;
                    if (smallest === i) break;
                    [a[i], a[smallest]] = [a[smallest], a[i]];
                    i = smallest;
                }
            }
            return top;
        }
    }

    const minDupHeap = new Heap<{ depth: number; val: number }>((a, b) => a.depth < b.depth);
    const maxConstrHeap = new Heap<{ depth: number; val: number }>((a, b) => a.depth > b.depth);

    let dupCount = 0;
    const pref: number[] = []; // cumulative length from root to node at each depth
    let bestLen = -1;
    let bestNodes = Number.MAX_SAFE_INTEGER;

    interface Frame {
        node: number;
        parent: number;
        edgeLen: number;
        state: 0 | 1; // 0 enter, 1 exit
    }

    const stack: Frame[] = [{ node: 0, parent: -1, edgeLen: 0, state: 0 }];

    while (stack.length) {
        const fr = stack.pop()!;
        if (fr.state === 0) {
            // enter node
            const curDepth = pref.length;
            const newPref = (pref.length ? pref[pref.length - 1] : 0) + fr.edgeLen;
            pref.push(newPref);

            const val = nums[fr.node];
            let arr = occ[val];
            if (!arr) {
                arr = [];
                occ[val] = arr;
            }
            const prevSize = arr.length;
            arr.push(curDepth);
            const newSize = prevSize + 1;

            if (newSize === 2) {
                dupCount++;
                dupFirstDepth[val] = arr[0];
                minDupHeap.push({ depth: dupFirstDepth[val], val });
            } else if (newSize === 3) {
                dupCount--;
                dupFirstDepth[val] = -1;
                constrDepth[val] = arr[0];
                maxConstrHeap.push({ depth: constrDepth[val], val });
            } else if (newSize > 3) {
                constrDepth[val] = arr[newSize - 3];
                maxConstrHeap.push({ depth: constrDepth[val], val });
            }

            // compute lower bound
            let lower = 0;
            while (maxConstrHeap.size()) {
                const top = maxConstrHeap.peek()!;
                if (constrDepth[top.val] === top.depth) break;
                maxConstrHeap.pop();
            }
            if (maxConstrHeap.size()) {
                lower = Math.max(lower, maxConstrHeap.peek()!.depth + 1);
            }
            if (dupCount >= 2) {
                while (minDupHeap.size()) {
                    const top = minDupHeap.peek()!;
                    if (dupFirstDepth[top.val] === top.depth) break;
                    minDupHeap.pop();
                }
                if (minDupHeap.size()) {
                    lower = Math.max(lower, minDupHeap.peek()!.depth + 1);
                }
            }

            const startDepth = lower;
            const length = pref[pref.length - 1] - (startDepth === 0 ? 0 : pref[startDepth]);
            const nodesCnt = pref.length - startDepth;

            if (length > bestLen || (length === bestLen && nodesCnt < bestNodes)) {
                bestLen = length;
                bestNodes = nodesCnt;
            }

            // schedule exit
            stack.push({ node: fr.node, parent: fr.parent, edgeLen: fr.edgeLen, state: 1 });
            // push children
            for (let i = adj[fr.node].length - 1; i >= 0; --i) {
                const [nei, w] = adj[fr.node][i];
                if (nei === fr.parent) continue;
                stack.push({ node: nei, parent: fr.node, edgeLen: w, state: 0 });
            }
        } else {
            // exit node
            const val = nums[fr.node];
            const arr = occ[val]!;
            const size = arr.length; // before pop

            if (size === 2) {
                dupCount--;
                dupFirstDepth[val] = -1;
            } else if (size === 3) {
                // was constraint, becomes duplicate
                constrDepth[val] = -1;
                dupCount++;
                dupFirstDepth[val] = arr[0];
                minDupHeap.push({ depth: dupFirstDepth[val], val });
            } else if (size > 3) {
                // still constraint after removal
                const newSize = size - 1;
                constrDepth[val] = arr[newSize - 3];
                maxConstrHeap.push({ depth: constrDepth[val], val });
            }
            arr.pop();
            pref.pop();
        }
    }

    return [bestLen, bestNodes];
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
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            [$u, $v, $len] = $e;
            $graph[$u][] = [$v, $len];
            $graph[$v][] = [$u, $len];
        }

        // state variables
        $this->graph = $graph;
        $this->nums = $nums;
        $this->cnt = [];          // value => count in current window
        $this->ops = [];          // stack of [value, previousCount] for undo
        $this->L = 0;             // left bound depth index
        $this->dupCount = 0;      // number of values appearing exactly twice in window
        $this->bestLen = -1;
        $this->bestNodes = PHP_INT_MAX;
        $this->pathVals = [];     // depth => node value
        $this->prefLen = [];      // depth => cumulative length from root

        $this->dfs(0, -1, 0, 0);

        return [$this->bestLen, $this->bestNodes];
    }

    private function dfs($node, $parent, $depth, $cumLen) {
        $this->pathVals[$depth] = $this->nums[$node];
        $this->prefLen[$depth] = $cumLen;

        // save state before processing this node
        $opsSizeBefore = count($this->ops);
        $L_before = $this->L;
        $dup_before = $this->dupCount;

        $this->addNode($depth);

        foreach ($this->graph[$node] as $edge) {
            [$next, $len] = $edge;
            if ($next == $parent) continue;
            $this->dfs($next, $node, $depth + 1, $cumLen + $len);
        }

        // rollback to previous state
        while (count($this->ops) > $opsSizeBefore) {
            $entry = array_pop($this->ops);
            $val = $entry[0];
            $prev = $entry[1];
            $this->cnt[$val] = $prev;
        }
        $this->L = $L_before;
        $this->dupCount = $dup_before;
    }

    private function addNode($depth) {
        $val = $this->pathVals[$depth];

        // increment count for this value
        $prev = $this->cnt[$val] ?? 0;
        $new = $prev + 1;
        $this->ops[] = [$val, $prev];
        $this->cnt[$val] = $new;

        if ($new == 2) {
            $this->dupCount++;
        } elseif ($new == 3) { // was duplicate, now triple
            $this->dupCount--;
        }

        // adjust left bound while constraints violated
        while ($this->dupCount > 1 || $this->cnt[$val] > 2) {
            $remVal = $this->pathVals[$this->L];
            $prevRem = $this->cnt[$remVal];
            $newRem = $prevRem - 1;
            $this->ops[] = [$remVal, $prevRem];
            $this->cnt[$remVal] = $newRem;

            if ($prevRem == 2) {
                $this->dupCount--;
            } elseif ($prevRem == 3) { // from triple to double creates a duplicate
                $this->dupCount++;
            }
            $this->L++;
        }

        // compute current path length and node count
        $curLen = $this->prefLen[$depth] - ($this->L > 0 ? $this->prefLen[$this->L - 1] : 0);
        $nodeCnt = $depth - $this->L + 1;

        if ($curLen > $this->bestLen) {
            $this->bestLen = $curLen;
            $this->bestNodes = $nodeCnt;
        } elseif ($curLen == $this->bestLen && $nodeCnt < $this->bestNodes) {
            $this->bestNodes = $nodeCnt;
        }
    }
}
```

## Swift

```swift
import Foundation

class BIT {
    private var n: Int
    private var tree: [Int]
    init(_ size: Int) {
        self.n = size
        self.tree = Array(repeating: 0, count: size + 2)
    }
    func add(_ index: Int, _ delta: Int) {
        var i = index
        while i <= n {
            tree[i] += delta
            i += i & -i
        }
    }
    func sum(_ index: Int) -> Int {
        var res = 0
        var i = index
        while i > 0 {
            res += tree[i]
            i -= i & -i
        }
        return res
    }
    func total() -> Int {
        return sum(n)
    }
    // returns smallest idx such that prefix sum >= k (1-indexed). assumes 1 <= k <= total()
    func kth(_ k: Int) -> Int {
        var idx = 0
        var bitMask = 1
        while bitMask <= n { bitMask <<= 1 }
        var mask = bitMask
        var kk = k
        while mask > 0 {
            let next = idx + mask
            if next <= n && tree[next] < kk {
                kk -= tree[next]
                idx = next
            }
            mask >>= 1
        }
        return idx + 1
    }
}

class Solution {
    private var adj: [[(to: Int, w: Int)]] = []
    private var nums: [Int] = []
    private var occDict: [Int: [Int]] = [:]
    private var bitSecond = BIT(0)
    private var bitThird = BIT(0)
    private var prefLengths: [Int] = []   // cumulative length from root to node at each depth
    private var bestLen: Int = 0
    private var minNodes: Int = Int.max
    
    func longestSpecialPath(_ edges: [[Int]], _ nums: [Int]) -> [Int] {
        let n = nums.count
        self.nums = nums
        adj = Array(repeating: [], count: n)
        for e in edges {
            let u = e[0], v = e[1], w = e[2]
            adj[u].append((v, w))
            adj[v].append((u, w))
        }
        bitSecond = BIT(n + 5)
        bitThird = BIT(n + 5)
        prefLengths = []
        occDict = [:]
        bestLen = 0
        minNodes = Int.max
        dfs(0, -1, 0)
        return [bestLen, minNodes]
    }
    
    private func dfs(_ node: Int, _ parent: Int, _ curLen: Int) {
        let depth = prefLengths.count
        prefLengths.append(curLen)
        
        // process current node value
        var actions: [(isSecond: Bool, pos: Int, revDelta: Int)] = []
        let val = nums[node]
        let prevArr = occDict[val] ?? []
        var arr = prevArr
        
        switch arr.count {
        case 0:
            arr.append(depth)
        case 1:
            let p0 = arr[0]
            arr.append(depth)
            bitSecond.add(p0 + 1, 1)
            actions.append((true, p0 + 1, -1))
        case 2:
            let p0 = arr[0], p1 = arr[1]
            arr.append(depth)
            bitSecond.add(p1 + 1, 1)
            actions.append((true, p1 + 1, -1))
            bitThird.add(p0 + 1, 1)
            actions.append((false, p0 + 1, -1))
        default: // count == 3
            let a = arr[0], b = arr[1], c = arr[2]
            // remove old second (b) and third (a)
            bitSecond.add(b + 1, -1)
            actions.append((true, b + 1, 1))
            bitThird.add(a + 1, -1)
            actions.append((false, a + 1, 1))
            // shift
            arr.removeFirst()
            arr.append(depth)   // now [b,c,depth]
            // new second = c (arr[1]), third = b (arr[0])
            bitSecond.add(arr[1] + 1, 1)
            actions.append((true, arr[1] + 1, -1))
            bitThird.add(arr[0] + 1, 1)
            actions.append((false, arr[0] + 1, -1))
        }
        occDict[val] = arr
        
        // compute answer for this node
        let totalSecond = bitSecond.total()
        var secondLargestPos = -1
        if totalSecond >= 2 {
            let posIdx = bitSecond.kth(totalSecond - 1)   // 1-indexed
            secondLargestPos = posIdx - 1
        }
        var maxThirdPos = -1
        if bitThird.total() > 0 {
            let posIdx = bitThird.kth(bitThird.total())
            maxThirdPos = posIdx - 1
        }
        let L = max(maxThirdPos + 1, secondLargestPos + 1)
        let pathLen = curLen - (L > 0 ? prefLengths[L - 1] : 0)
        let nodeCount = depth - L + 1
        if pathLen > bestLen {
            bestLen = pathLen
            minNodes = nodeCount
        } else if pathLen == bestLen && nodeCount < minNodes {
            minNodes = nodeCount
        }
        
        // recurse children
        for edge in adj[node] {
            let nxt = edge.to
            if nxt == parent { continue }
            dfs(nxt, node, curLen + edge.w)
        }
        
        // revert actions
        for act in actions.reversed() {
            if act.isSecond {
                bitSecond.add(act.pos, act.revDelta)
            } else {
                bitThird.add(act.pos, act.revDelta)
            }
        }
        occDict[val] = prevArr
        prefLengths.removeLast()
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun longestSpecialPath(edges: Array<IntArray>, nums: IntArray): IntArray {
        val n = nums.size
        // build adjacency list
        val adj = Array(n) { mutableListOf<Pair<Int, Int>>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            val w = e[2]
            adj[u].add(Pair(v, w))
            adj[v].add(Pair(u, w))
        }

        // occurrences per value
        var maxVal = 0
        for (v in nums) if (v > maxVal) maxVal = v
        val occ = Array(maxVal + 1) { java.util.ArrayDeque<Int>() }

        var left = 0               // left index of current valid window
        var dupCount = 0           // number of values appearing exactly twice in window
        var overTwoCount = 0       // number of values appearing three times (invalid)

        val pref = LongArray(n)    // prefix length from root to each depth index

        var bestLen = -1L
        var bestNodes = Int.MAX_VALUE

        // iterative DFS stacks
        val nodeStack = IntArray(n)
        val parentStack = IntArray(n)
        val edgeStack = IntArray(n)
        val childIdx = IntArray(n)

        var sp = 0
        nodeStack[sp] = 0
        parentStack[sp] = -1
        edgeStack[sp] = 0
        childIdx[sp] = 0
        sp++

        while (sp > 0) {
            val depth = sp - 1
            val node = nodeStack[depth]

            // first time we see this node
            if (childIdx[depth] == 0) {
                pref[depth] = if (depth == 0) 0L else pref[depth - 1] + edgeStack[depth].toLong()
                if (left > depth) left = depth

                // add current node occurrence
                val v = nums[node]
                val dq = occ[v]
                dq.addLast(depth)
                when (dq.size) {
                    2 -> dupCount++
                    3 -> overTwoCount++
                }

                // shrink window until valid
                while (dupCount > 1 || overTwoCount > 0) {
                    val leftNode = nodeStack[left]
                    val vL = nums[leftNode]
                    val dqL = occ[vL]
                    when (dqL.size) {
                        2 -> dupCount--
                        3 -> overTwoCount--
                    }
                    dqL.removeFirst()
                    left++
                }

                // evaluate current path
                val curLen = pref[depth] - if (left > 0) pref[left - 1] else 0L
                val nodesCnt = depth - left + 1
                if (curLen > bestLen || (curLen == bestLen && nodesCnt < bestNodes)) {
                    bestLen = curLen
                    bestNodes = nodesCnt
                }
            }

            // explore next child
            if (childIdx[depth] < adj[node].size) {
                val (next, w) = adj[node][childIdx[depth]]
                childIdx[depth]++
                if (next == parentStack[depth]) continue
                nodeStack[sp] = next
                parentStack[sp] = node
                edgeStack[sp] = w
                childIdx[sp] = 0
                sp++
            } else {
                // exiting node, remove its occurrence from right side if still present
                val idx = depth
                val v = nums[node]
                val dq = occ[v]
                if (!dq.isEmpty() && dq.peekLast() == idx) {
                    when (dq.size) {
                        2 -> dupCount--
                        3 -> overTwoCount--
                    }
                    dq.removeLast()
                }
                sp--
            }
        }

        return intArrayOf(bestLen.toInt(), bestNodes)
    }
}
```

## Dart

```dart
class Solution {
  List<int> longestSpecialPath(List<List<int>> edges, List<int> nums) {
    int n = nums.length;
    // Build adjacency list
    List<List<List<int>>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0], v = e[1], w = e[2];
      adj[u].add([v, w]);
      adj[v].add([u, w]);
    }

    // Determine max value to size arrays
    int maxVal = 0;
    for (int x in nums) if (x > maxVal) maxVal = x;

    List<int> lastDepth = List.filled(maxVal + 1, -1);
    List<int> prevDepth = List.filled(maxVal + 1, -1);
    List<int> thirdDepth = List.filled(maxVal + 1, -1);

    // Fenwick tree implementation
    class Fenwick {
      final List<int> bit;
      final int n;
      final int maxMask;
      Fenwick(this.n)
          : bit = List.filled(n + 2, 0),
            maxMask = (() {
              int m = 1;
              while ((m << 1) <= n) m <<= 1;
              return m;
            })();
      void add(int idx, int delta) {
        for (int i = idx + 1; i <= n; i += i & -i) {
          bit[i] += delta;
        }
      }

      int sumPrefix(int idx) {
        int res = 0;
        for (int i = idx + 1; i > 0; i -= i & -i) {
          res += bit[i];
        }
        return res;
      }

      int total() => sumPrefix(n - 1);

      // smallest index such that prefix sum >= k (k >= 1)
      int findKth(int k) {
        int idx = 0;
        for (int mask = maxMask; mask > 0; mask >>= 1) {
          int next = idx + mask;
          if (next <= n && bit[next] < k) {
            k -= bit[next];
            idx = next;
          }
        }
        return idx; // 0‑based index
      }
    }

    Fenwick fenwickPrev = Fenwick(n);
    Fenwick fenwickThird = Fenwick(n);

    List<int> pathNodes = [];
    List<int> dist = List.filled(n, 0);

    int maxLen = -1;
    int minCnt = n + 1;

    void dfs(int node, int parent, int depth, int cumDist) {
      // push current node
      pathNodes.add(node);
      dist[node] = cumDist;

      int val = nums[node];
      int oldLast = lastDepth[val];
      int oldPrev = prevDepth[val];
      int oldThird = thirdDepth[val];

      if (oldPrev != -1) fenwickPrev.add(oldPrev, -1);
      if (oldThird != -1) fenwickThird.add(oldThird, -1);

      int newThird = oldPrev;
      int newPrev = oldLast;
      int newLast = depth;

      lastDepth[val] = newLast;
      prevDepth[val] = newPrev;
      thirdDepth[val] = newThird;

      if (newPrev != -1) fenwickPrev.add(newPrev, 1);
      if (newThird != -1) fenwickThird.add(newThird, 1);

      // compute constraint depth
      int constraint = -1;
      int totalThird = fenwickThird.total();
      if (totalThird > 0) {
        int maxThird = fenwickThird.findKth(totalThird);
        if (maxThird > constraint) constraint = maxThird;
      }
      int totalPrev = fenwickPrev.total();
      if (totalPrev >= 2) {
        int secondMaxPrev = fenwickPrev.findKth(totalPrev - 1);
        if (secondMaxPrev > constraint) constraint = secondMaxPrev;
      }

      int startDepth = constraint + 1;
      int ancNode = pathNodes[startDepth];
      int length = cumDist - dist[ancNode];
      int nodeCount = depth - startDepth + 1;

      if (length > maxLen) {
        maxLen = length;
        minCnt = nodeCount;
      } else if (length == maxLen && nodeCount < minCnt) {
        minCnt = nodeCount;
      }

      for (var edge in adj[node]) {
        int nxt = edge[0];
        int w = edge[1];
        if (nxt == parent) continue;
        dfs(nxt, node, depth + 1, cumDist + w);
      }

      // backtrack
      if (newPrev != -1) fenwickPrev.add(newPrev, -1);
      if (newThird != -1) fenwickThird.add(newThird, -1);

      lastDepth[val] = oldLast;
      prevDepth[val] = oldPrev;
      thirdDepth[val] = oldThird;

      if (oldPrev != -1) fenwickPrev.add(oldPrev, 1);
      if (oldThird != -1) fenwickThird.add(oldThird, 1);

      pathNodes.removeLast();
    }

    dfs(0, -1, 0, 0);
    return [maxLen, minCnt];
  }
}
```

## Golang

```go
package main

func longestSpecialPath(edges [][]int, nums []int) []int {
	n := len(nums)

	// build adjacency list
	type edge struct{ to, w int }
	graph := make([][]edge, n)
	maxVal := 0
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		graph[u] = append(graph[u], edge{v, w})
		graph[v] = append(graph[v], edge{u, w})
		if nums[u] > maxVal {
			maxVal = nums[u]
		}
		if nums[v] > maxVal {
			maxVal = nums[v]
		}
	}

	cnt := make([]int, maxVal+1) // count of each value in current window
	inWin := []bool{}            // whether node at depth i is currently inside the window
	path := []int{}              // nodes along current root->node path
	pref := []int64{}            // prefix sum of edge lengths from root

	L := 0          // left index of current valid window (inclusive)
	dupCnt := 0     // number of values that appear exactly twice in the window
	bestLen := int64(-1)
	bestNodes := 0

	var dfs func(u, parent, wFromParent int)
	dfs = func(u, parent, wFromParent int) {
		// push current node
		if len(path) == 0 {
			pref = append(pref, 0)
		} else {
			newPref := pref[len(pref)-1] + int64(wFromParent)
			pref = append(pref, newPref)
		}
		path = append(path, u)
		inWin = append(inWin, true)

		val := nums[u]
		cnt[val]++
		if cnt[val] == 2 {
			dupCnt++
		}

		// maintain window validity
		for dupCnt > 1 || cnt[val] == 3 {
			leftNode := path[L]
			leftVal := nums[leftNode]
			cnt[leftVal]--
			if cnt[leftVal] == 1 { // was 2, now 1
				dupCnt--
			}
			inWin[L] = false
			L++
		}

		// evaluate current window
		curLen := pref[len(pref)-1] - pref[L]
		nodesCnt := len(path) - L
		if curLen > bestLen || (curLen == bestLen && nodesCnt < bestNodes) {
			bestLen = curLen
			bestNodes = nodesCnt
		}

		// recurse to children
		for _, e := range graph[u] {
			if e.to == parent {
				continue
			}
			dfs(e.to, u, e.w)
		}

		// backtrack: remove current node
		idx := len(path) - 1
		if inWin[idx] {
			valBack := nums[path[idx]]
			cnt[valBack]--
			if cnt[valBack] == 1 { // was duplicate, now single
				dupCnt--
			}
		}
		path = path[:idx]
		pref = pref[:idx]
		inWin = inWin[:idx]

		if L > len(path) {
			L = len(path)
		}
	}

	dfs(0, -1, 0)

	return []int{int(bestLen), bestNodes}
}
```

## Ruby

```ruby
def longest_special_path(edges, nums)
  n = nums.length
  adj = Array.new(n) { [] }
  edges.each do |u, v, w|
    adj[u] << [v, w]
    adj[v] << [u, w]
  end

  cnt = Hash.new(0)
  ops = []
  l = 0
  dup_cnt = 0
  triple_cnt = 0
  path_vals = []
  cumlen = []

  l_stack = []
  dup_stack = []
  triple_stack = []
  ops_size_stack = []

  best_len = 0
  best_nodes = Float::INFINITY

  inc = lambda do |val|
    c = cnt[val]
    case c
    when 1
      dup_cnt += 1
    when 2
      triple_cnt += 1
    end
    cnt[val] = c + 1
    ops << [:inc, val]
  end

  dec = lambda do |val|
    c = cnt[val]
    case c
    when 2
      dup_cnt -= 1
    when 3
      triple_cnt -= 1
    end
    newc = c - 1
    if newc == 0
      cnt.delete(val)
    else
      cnt[val] = newc
    end
    ops << [:dec, val]
  end

  inc_noop = lambda do |val|
    c = cnt[val] || 0
    case c
    when 1
      dup_cnt += 1
    when 2
      triple_cnt += 1
    end
    cnt[val] = c + 1
  end

  dec_noop = lambda do |val|
    c = cnt[val]
    case c
    when 2
      dup_cnt -= 1
    when 3
      triple_cnt -= 1
    end
    newc = c - 1
    if newc == 0
      cnt.delete(val)
    else
      cnt[val] = newc
    end
  end

  stack = [[0, -1, 0, 0]] # node, parent, edge_len, state (0 enter, 1 exit)

  until stack.empty?
    node, parent, edge_len, state = stack.pop
    if state == 0
      depth = path_vals.length
      cum = (depth.zero? ? 0 : cumlen[-1]) + edge_len
      path_vals << nums[node]
      cumlen << cum

      l_stack << l
      dup_stack << dup_cnt
      triple_stack << triple_cnt
      ops_size_stack << ops.length

      inc.call(nums[node])

      while dup_cnt > 1 || triple_cnt > 0
        left_val = path_vals[l]
        dec.call(left_val)
        l += 1
      end

      cur_len = cum - (l.positive? ? cumlen[l - 1] : 0)
      cur_nodes = depth - l + 1
      if cur_len > best_len || (cur_len == best_len && cur_nodes < best_nodes)
        best_len = cur_len
        best_nodes = cur_nodes
      end

      stack << [node, parent, edge_len, 1]
      adj[node].each do |nbr, w|
        next if nbr == parent
        stack << [nbr, node, w, 0]
      end
    else
      target_ops_size = ops_size_stack.pop
      while ops.length > target_ops_size
        op_type, val = ops.pop
        if op_type == :inc
          dec_noop.call(val)
        else
          inc_noop.call(val)
        end
      end

      l = l_stack.pop
      dup_cnt = dup_stack.pop
      triple_cnt = triple_stack.pop

      path_vals.pop
      cumlen.pop
    end
  end

  [best_len, best_nodes]
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable.{ArrayBuffer, HashMap, TreeMap}

    def longestSpecialPath(edges: Array[Array[Int]], nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val adj = Array.fill(n)(new ArrayBuffer[(Int, Int)]())
        for (e <- edges) {
            val u = e(0); val v = e(1); val w = e(2)
            adj(u).append((v, w))
            adj(v).append((u, w))
        }

        // occurrence stacks per value
        val occMap = new HashMap[Int, ArrayBuffer[Int]]()
        // multiset for third-last depths (key -> count)
        val thirdLastCounts = new TreeMap[Int, Int]()
        // multiset for first occurrence depth of values that appear exactly twice
        val dupFirstCounts = new TreeMap[Int, Int]()

        var duplicateVals = 0          // number of values with exactly two occurrences

        def inc(map: TreeMap[Int, Int], key: Int): Unit = {
            map.put(key, map.getOrElse(key, 0) + 1)
        }
        def dec(map: TreeMap[Int, Int], key: Int): Unit = {
            val cnt = map(key) - 1
            if (cnt == 0) map.remove(key) else map.update(key, cnt)
        }

        // path cumulative lengths
        val cumLenStack = new ArrayBuffer[Long]()
        var bestLen: Long = -1L
        var minNodes: Int = Int.MaxValue

        def dfs(node: Int, parent: Int, depth: Int, curCum: Long): Unit = {
            // push current node info
            cumLenStack.append(curCum)

            val value = nums(node)
            val list = occMap.getOrElseUpdate(value, new ArrayBuffer[Int]())
            val prevSize = list.size
            list.append(depth)

            // handle transitions before adding new occurrence
            if (prevSize == 2) {
                // was duplicate, now becomes triple
                duplicateVals -= 1
                dec(dupFirstCounts, list(0))
            }
            if (prevSize >= 3) {
                // remove old third-last contribution
                val oldThird = list(prevSize - 3)
                dec(thirdLastCounts, oldThird)
            }

            // after addition handle new states
            if (list.size == 2) {
                duplicateVals += 1
                inc(dupFirstCounts, list(0))
            }
            if (list.size >= 3) {
                val newThird = list(list.size - 3)
                inc(thirdLastCounts, newThird)
            }

            // compute left bound for current depth
            var left = 0
            if (thirdLastCounts.nonEmpty) {
                left = math.max(left, thirdLastCounts.lastKey + 1)
            }
            if (duplicateVals >= 2 && dupFirstCounts.nonEmpty) {
                left = math.max(left, dupFirstCounts.firstKey + 1)
            }

            // evaluate current path
            val length = curCum - cumLenStack(left)
            val nodesCnt = depth - left + 1
            if (length > bestLen || (length == bestLen && nodesCnt < minNodes)) {
                bestLen = length
                minNodes = nodesCnt
            }

            // recurse children
            for ((nei, w) <- adj(node) if nei != parent) {
                dfs(nei, node, depth + 1, curCum + w)
            }

            // pop current node info (backtrack)
            // before removal handle states
            val curSize = list.size
            if (curSize >= 3) {
                val oldThird = list(curSize - 3)
                dec(thirdLastCounts, oldThird)
            }
            if (curSize == 2) {
                duplicateVals -= 1
                dec(dupFirstCounts, list(0))
            } else if (curSize == 3) {
                // becomes duplicate after removal
                duplicateVals += 1
                inc(dupFirstCounts, list(0))
            }
            // remove the occurrence
            list.remove(curSize - 1)
            // after removal, if size still >=3, add new third-last
            if (list.size >= 3) {
                val newThird = list(list.size - 3)
                inc(thirdLastCounts, newThird)
            }
            if (list.isEmpty) occMap.remove(value)

            cumLenStack.remove(cumLenStack.size - 1)
        }

        // start DFS from root (0), depth 0, cumulative length 0
        dfs(0, -1, 0, 0L)

        Array(bestLen.toInt, minNodes)
    }
}
```

## Rust

```rust
use std::collections::{HashMap, BTreeMap, VecDeque};

fn insert_multiset(map: &mut BTreeMap<usize, i32>, key: usize) {
    *map.entry(key).or_insert(0) += 1;
}
fn remove_multiset(map: &mut BTreeMap<usize, i32>, key: usize) {
    if let Some(cnt) = map.get_mut(&key) {
        *cnt -= 1;
        if *cnt == 0 {
            map.remove(&key);
        }
    }
}

fn push_node(
    val: i32,
    idx: usize,
    occ: &mut HashMap<i32, VecDeque<usize>>,
    dup_set: &mut BTreeMap<usize, i32>,
    third_set: &mut BTreeMap<usize, i32>,
) {
    let entry = occ.entry(val).or_insert(VecDeque::new());

    match entry.len() {
        2 => {
            if let Some(&second) = entry.get(1) {
                remove_multiset(dup_set, second);
            }
        }
        3 => {
            if let Some(&third) = entry.get(0) {
                remove_multiset(third_set, third);
            }
        }
        _ => {}
    }

    entry.push_back(idx);
    if entry.len() > 3 {
        entry.pop_front();
    }

    match entry.len() {
        2 => {
            let second = *entry.get(1).unwrap();
            insert_multiset(dup_set, second);
        }
        3 => {
            let third = *entry.get(0).unwrap();
            insert_multiset(third_set, third);
        }
        _ => {}
    }
}

fn pop_node(
    val: i32,
    occ: &mut HashMap<i32, VecDeque<usize>>,
    dup_set: &mut BTreeMap<usize, i32>,
    third_set: &mut BTreeMap<usize, i32>,
) {
    let entry = occ.get_mut(&val).unwrap();

    match entry.len() {
        2 => {
            if let Some(&second) = entry.get(1) {
                remove_multiset(dup_set, second);
            }
        }
        3 => {
            if let Some(&third) = entry.get(0) {
                remove_multiset(third_set, third);
            }
        }
        _ => {}
    }

    entry.pop_back();

    match entry.len() {
        2 => {
            let second = *entry.get(1).unwrap();
            insert_multiset(dup_set, second);
        }
        3 => {
            let third = *entry.get(0).unwrap();
            insert_multiset(third_set, third);
        }
        _ => {}
    }

    if entry.is_empty() {
        occ.remove(&val);
    }
}

impl Solution {
    pub fn longest_special_path(edges: Vec<Vec<i32>>, nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut adj: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2] as i64;
            adj[u].push((v, w));
            adj[v].push((u, w));
        }

        // data structures
        let mut occ: HashMap<i32, VecDeque<usize>> = HashMap::new();
        let mut dup_set: BTreeMap<usize, i32> = BTreeMap::new();   // second occurrence positions
        let mut third_set: BTreeMap<usize, i32> = BTreeMap::new(); // oldest of three occurrences

        let mut pref: Vec<i64> = Vec::with_capacity(n);
        let mut best_len: i64 = -1;
        let mut best_nodes: usize = 0;

        // iterative DFS stack: (node, parent, edge_len_from_parent, visited_flag)
        let mut stack: Vec<(usize, usize, i64, bool)> = Vec::new();
        stack.push((0, n, 0, false)); // root, no parent

        while let Some((node, parent, w_from_par, visited)) = stack.pop() {
            if !visited {
                // pre-order
                let cur_pref = if parent == n { 0 } else { pref.last().unwrap() + w_from_par };
                pref.push(cur_pref);
                let idx = pref.len() - 1;
                push_node(nums[node], idx, &mut occ, &mut dup_set, &mut third_set);

                // compute lower bound
                let mut lb: i64 = -1;
                if let Some((&max_third, _)) = third_set.iter().next_back() {
                    lb = lb.max(max_third as i64);
                }
                if dup_set.len() >= 2 {
                    let mut iter = dup_set.iter().rev();
                    let _first = *iter.next().unwrap().0;
                    let second = *iter.next().unwrap().0;
                    lb = lb.max(second as i64);
                }
                let start_idx = (lb + 1) as usize;
                let length = pref[idx] - pref[start_idx];
                let nodes_cnt = idx - start_idx + 1;

                if length > best_len || (length == best_len && nodes_cnt < best_nodes) {
                    best_len = length;
                    best_nodes = nodes_cnt;
                }

                // push post-order marker
                stack.push((node, parent, w_from_par, true));

                // push children
                for &(nei, w) in adj[node].iter().rev() {
                    if nei != parent {
                        stack.push((nei, node, w, false));
                    }
                }
            } else {
                // post-order: clean up
                let idx = pref.len() - 1;
                pop_node(nums[node], &mut occ, &mut dup_set, &mut third_set);
                pref.pop();
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
  (let* ((n (vector-length (list->vector (map car edges)))) ; placeholder, will be overwritten
         (adj (make-vector n '()))
         (max-node -1))
    ;; build adjacency list
    (for-each
     (lambda (e)
       (define u (list-ref e 0))
       (define v (list-ref e 1))
       (define w (list-ref e 2))
       (set! max-node (max max-node u v))
       (vector-set! adj u (cons (list v w) (vector-ref adj u)))
       (vector-set! adj v (cons (list u w) (vector-ref adj v))))
     edges)
    (define n-nodes (+ max-node 1))
    ;; mutable structures
    (define counts (make-hash))               ; value -> count in current window
    (define dup-count 0)                      ; number of values appearing exactly twice
    (define has-triple #f)                    ; any value appears three times
    (define log-actions (make-vector (* n-nodes 4) '())) ; preallocate enough
    (define log-size 0)
    (define (log-push act)
      (vector-set! log-actions log-size act)
      (set! log-size (+ log-size 1)))
    (define (log-pop)
      (when (> log-size 0)
        (set! log-size (- log-size 1))
        (vector-ref log-actions log-size)))
    ;; inc/dec with logging
    (define (inc-val v)
      (let ((c (hash-ref counts v 0)))
        (hash-set! counts v (+ c 1))
        (when (= (+ c 1) 2) (set! dup-count (+ dup-count 1)))
        (when (= (+ c 1) 3) (set! has-triple #t))
        (log-push (list 'inc v))))
    (define (dec-val v)
      (let ((c (hash-ref counts v)))
        (hash-set! counts v (- c 1))
        (when (= c 2) (set! dup-count (- dup-count 1)))
        (when (= c 3) (set! has-triple #f))
        (log-push (list 'dec v))))
    ;; inc/dec without logging (used during undo)
    (define (inc-val-no-log v)
      (let ((c (hash-ref counts v 0)))
        (hash-set! counts v (+ c 1))
        (when (= (+ c 1) 2) (set! dup-count (+ dup-count 1)))
        (when (= (+ c 1) 3) (set! has-triple #t))))
    (define (dec-val-no-log v)
      (let ((c (hash-ref counts v)))
        (hash-set! counts v (- c 1))
        (when (= c 2) (set! dup-count (- dup-count 1)))
        (when (= c 3) (set! has-triple #f))))
    ;; undo actions to a given checkpoint
    (define (undo-to checkpoint)
      (let loop ()
        (when (> log-size checkpoint)
          (let ((act (log-pop)))
            (match act
              [(list 'inc v) (dec-val-no-log v)]
              [(list 'dec v) (inc-val-no-log v)]))
          (loop))))
    ;; path storage
    (define path-nodes (make-vector n-nodes 0))
    (define path-dist  (make-vector n-nodes 0))
    (define left-index 0)
    (define best-length -1)
    (define best-nodes   +inf.0) ; use large number
    ;; DFS recursion
    (define (dfs node parent depth cumdist)
      (vector-set! path-nodes depth node)
      (vector-set! path-dist depth cumdist)
      (inc-val (list-ref nums node))
      (let ((checkpoint log-size)
            (saved-left left-index))
        ;; shrink window while invalid
        (let loop ()
          (when (or (> dup-count 1) has-triple)
            (define left-node (vector-ref path-nodes left-index))
            (dec-val (list-ref nums left-node))
            (set! left-index (+ left-index 1))
            (loop)))
        ;; evaluate current window
        (let* ((start left-index)
               (len (- cumdist (if (= start 0) 0 (vector-ref path-dist (- start 1)))))
               (nodes-count (+ (- depth start) 1)))
          (cond [(> len best-length)
                 (set! best-length len)
                 (set! best-nodes nodes-count)]
                [(and (= len best-length) (< nodes-count best-nodes))
                 (set! best-nodes nodes-count)]))
        ;; recurse children
        (for-each
         (lambda (nbr-info)
           (define nbr (list-ref nbr-info 0))
           (define w   (list-ref nbr-info 1))
           (when (not (= nbr parent))
             (dfs nbr node (+ depth 1) (+ cumdist w))))
         (vector-ref adj node))
        ;; undo to state before this call
        (undo-to checkpoint)
        (set! left-index saved-left)))
    ;; start DFS from root 0
    (dfs 0 -1 0 0)
    (list best-length best-nodes)))
```

## Erlang

```erlang
-export([longest_special_path/2]).

-spec longest_special_path(Edges :: [[integer()]], Nums :: [integer()]) -> [integer()].
longest_special_path(Edges, Nums) ->
    Adj = build_adj(Edges),
    ValTab = ets:new(val_tab, [set, private]),
    DistTab = ets:new(dist_tab, [set, private]),
    % start DFS from root 0
    {BestLen, BestCnt} = dfs(
        0,                     % Node
        -1,                    % Parent
        0,                     % Depth
        0,                     % Cumulative distance
        #{},                   % Counts map
        0,                     % Left index
        0,                     % Duplicate count (values with count==2)
        0,                     % Over count (values with count==3)
        -1,                    % Current best length
        size(Nums) + 1,        % Current best node count (large init)
        Adj,
        ValTab,
        DistTab,
        Nums),
    [BestLen, BestCnt].

build_adj(Edges) ->
    lists:foldl(fun([U,V,L], Acc) ->
        Acc1 = maps:update_with(U,
                fun(Lst) -> [{V,L}|Lst] end,
                [{V,L}], Acc),
        maps:update_with(V,
            fun(Lst) -> [{U,L}|Lst] end,
            [{U,L}], Acc1)
    end, #{}, Edges).

dfs(Node, Parent, Depth, CumDist,
    Counts, Left, DupCnt, OverCnt,
    MaxLen, MinNodes,
    Adj, ValTab, DistTab, Nums) ->

    Val = element(Node + 1, Nums),
    ets:insert(ValTab, {Depth, Val}),
    ets:insert(DistTab, {Depth, CumDist}),

    {Counts1, Dup1, Over1} = add_val(Counts, Val, DupCnt, OverCnt),

    {Left2, Counts2, Dup2, Over2} =
        shrink_loop(Left, Counts1, Dup1, Over1, ValTab),

    StartDist = case Left2 of
        0 -> 0;
        L ->
            [{_, D}] = ets:lookup(DistTab, L - 1),
            D
    end,
    CurrLen = CumDist - StartDist,
    NodeCnt = Depth - Left2 + 1,

    {NewMax, NewMin} =
        if CurrLen > MaxLen ->
                {CurrLen, NodeCnt};
           CurrLen == MaxLen ->
                {MaxLen, min(MinNodes, NodeCnt)};
           true ->
                {MaxLen, MinNodes}
        end,

    Children = maps:get(Node, Adj, []),
    lists:foldl(fun({Child, Len}, Acc) ->
        case Child of
            Parent -> Acc;
            _ ->
                {AccMax, AccMin} = Acc,
                dfs(Child, Node, Depth + 1, CumDist + Len,
                    Counts2, Left2, Dup2, Over2,
                    AccMax, AccMin,
                    Adj, ValTab, DistTab, Nums)
        end
    end, {NewMax, NewMin}, Children).

add_val(Counts, Val, DupCnt, OverCnt) ->
    case maps:get(Val, Counts, 0) of
        0 -> {maps:put(Val,1,Counts), DupCnt, OverCnt};
        1 -> {maps:put(Val,2,Counts), DupCnt + 1, OverCnt};
        2 -> {maps:put(Val,3,Counts), DupCnt, OverCnt + 1}
    end.

remove_val(Counts, Val, DupCnt, OverCnt) ->
    case maps:get(Val, Counts) of
        1 -> {maps:remove(Val,Counts), DupCnt, OverCnt};
        2 -> {maps:put(Val,1,Counts), DupCnt - 1, OverCnt};
        3 -> {maps:put(Val,2,Counts), DupCnt + 1, OverCnt - 1}
    end.

shrink_loop(Left, Counts, DupCnt, OverCnt, ValTab) ->
    case (DupCnt =< 1) andalso (OverCnt == 0) of
        true -> {Left, Counts, DupCnt, OverCnt};
        false ->
            [{_, V}] = ets:lookup(ValTab, Left),
            {Counts1, Dup1, Over1} = remove_val(Counts, V, DupCnt, OverCnt),
            shrink_loop(Left + 1, Counts1, Dup1, Over1, ValTab)
    end.
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

    occ_map = %{}
    second_tree = :gb_trees.empty()
    third_tree = :gb_trees.empty()
    second_cnt = 0
    dist_array = :array.new(n, default: 0)

    {best_len, best_nodes} =
      dfs(
        0,
        -1,
        0,
        0,
        adj,
        nums,
        occ_map,
        second_tree,
        third_tree,
        second_cnt,
        0,
        0,
        dist_array
      )

    [best_len, best_nodes]
  end

  defp dfs(
         u,
         parent,
         depth,
         dist,
         adj,
         nums,
         occ_map,
         second_tree,
         third_tree,
         second_cnt,
         best_len,
         best_nodes,
         dist_arr
       ) do
    # store distance for this depth
    dist_arr = :array.set(depth, dist, dist_arr)

    val = Enum.at(nums, u)

    {occ_map1, second_tree1, third_tree1, second_cnt1} =
      push(val, depth, occ_map, second_tree, third_tree, second_cnt)

    req = compute_req(third_tree1, second_tree1, second_cnt1)
    anc_dist = :array.get(req, dist_arr)
    path_len = dist - anc_dist
    node_cnt = depth - req + 1

    {best_len, best_nodes} =
      cond do
        path_len > best_len ->
          {path_len, node_cnt}

        path_len == best_len and node_cnt < best_nodes ->
          {best_len, node_cnt}

        true ->
          {best_len, best_nodes}
      end

    Enum.each(Map.get(adj, u, []), fn {v, w} ->
      if v != parent do
        {bl, bn} =
          dfs(
            v,
            u,
            depth + 1,
            dist + w,
            adj,
            nums,
            occ_map1,
            second_tree1,
            third_tree1,
            second_cnt1,
            best_len,
            best_nodes,
            dist_arr
          )

        # propagate best values upwards
        {best_len, best_nodes} = {bl, bn}
      end
    end)

    {best_len, best_nodes}
  end

  defp push(val, depth, occ_map, second_tree, third_tree, second_cnt) do
    occ = Map.get(occ_map, val, [])
    size_before = length(occ)
    new_occ = [depth | occ]
    occ_map = Map.put(occ_map, val, new_occ)

    cond do
      size_before == 0 ->
        {occ_map, second_tree, third_tree, second_cnt}

      size_before == 1 ->
        old = hd(occ)                     # previous depth
        second_tree = inc(second_tree, old)
        {occ_map, second_tree, third_tree, second_cnt + 1}

      size_before == 2 ->
        # replace old second entry and add third occurrence
        old_second = Enum.at(occ, -1)     # older depth (first occurrence)
        second_tree = dec(second_tree, old_second)

        new_second = hd(occ)              # previous newest depth
        second_tree = inc(second_tree, new_second)

        third_last = Enum.at(new_occ, 2)   # oldest among three
        third_tree = inc(third_tree, third_last)
        {occ_map, second_tree, third_tree, second_cnt}

      true ->
        # size_before >=3
        old_second = Enum.at(occ, 1)
        new_second = hd(occ)

        second_tree = dec(second_tree, old_second)
        second_tree = inc(second_tree, new_second)

        if size_before == 3 do
          {occ_map, second_tree, third_tree, second_cnt}
        else
          # size_before >=4
          old_third = Enum.at(occ, 2)
          new_third = Enum.at(new_occ, 3)

          third_tree = dec(third_tree, old_third)
          third_tree = inc(third_tree, new_third)
          {occ_map, second_tree, third_tree, second_cnt}
        end
    end
  end

  defp compute_req(third_tree, second_tree, second_cnt) do
    req = 0

    if not :gb_trees.is_empty(third_tree) do
      {max_key, _} = :gb_trees.largest(third_tree)
      req = max(req, max_key + 1)
    end

    if second_cnt >= 2 do
      {min_key, _} = :gb_trees.smallest(second_tree)
      req = max(req, min_key + 1)
    end

    req
  end

  defp inc(tree, key) do
    case :gb_trees.lookup(key, tree) do
      :none -> :gb_trees.insert(key, 1, tree)
      {_, cnt} -> :gb_trees.update(key, cnt + 1, tree)
    end
  end

  defp dec(tree, key) do
    case :gb_trees.lookup(key, tree) do
      :none ->
        tree

      {_, 1} ->
        :gb_trees.delete(key, tree)

      {_, cnt} ->
        :gb_trees.update(key, cnt - 1, tree)
    end
  end
end
```
