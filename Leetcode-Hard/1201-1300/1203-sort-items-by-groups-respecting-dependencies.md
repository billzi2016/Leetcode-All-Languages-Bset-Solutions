# 1203. Sort Items by Groups Respecting Dependencies

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> sortItems(int n, int m, vector<int>& group, vector<vector<int>>& beforeItems) {
        // Assign unique groups to items with no group
        int newGroupId = m;
        for (int i = 0; i < n; ++i) {
            if (group[i] == -1) group[i] = newGroupId++;
        }
        
        // Build graphs
        vector<vector<int>> itemAdj(n);
        vector<int> indegItem(n, 0);
        vector<vector<int>> groupAdj(newGroupId);
        vector<int> indegGroup(newGroupId, 0);
        
        for (int i = 0; i < n; ++i) {
            for (int pre : beforeItems[i]) {
                if (group[pre] == group[i]) {
                    // intra-group dependency
                    itemAdj[pre].push_back(i);
                    ++indegItem[i];
                } else {
                    // inter-group dependency
                    groupAdj[group[pre]].push_back(group[i]);
                    ++indegGroup[group[i]];
                }
            }
        }
        
        // Topological sort groups
        queue<int> qg;
        for (int g = 0; g < newGroupId; ++g) {
            if (indegGroup[g] == 0) qg.push(g);
        }
        vector<int> groupOrder;
        while (!qg.empty()) {
            int cur = qg.front(); qg.pop();
            groupOrder.push_back(cur);
            for (int nb : groupAdj[cur]) {
                if (--indegGroup[nb] == 0) qg.push(nb);
            }
        }
        if ((int)groupOrder.size() != newGroupId) return {}; // cycle among groups
        
        // Collect items per group
        vector<vector<int>> itemsInGroup(newGroupId);
        for (int i = 0; i < n; ++i) {
            itemsInGroup[group[i]].push_back(i);
        }
        
        // Result ordering
        vector<int> result;
        for (int g : groupOrder) {
            queue<int> qi;
            int cnt = 0;
            for (int item : itemsInGroup[g]) {
                if (indegItem[item] == 0) qi.push(item);
            }
            while (!qi.empty()) {
                int u = qi.front(); qi.pop();
                result.push_back(u);
                ++cnt;
                for (int v : itemAdj[u]) {
                    if (--indegItem[v] == 0) qi.push(v);
                }
            }
            if (cnt != (int)itemsInGroup[g].size()) return {}; // cycle within group
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] sortItems(int n, int m, int[] group, List<List<Integer>> beforeItems) {
        // Assign unique groups to items with no group
        int newGroupId = m;
        for (int i = 0; i < n; i++) {
            if (group[i] == -1) {
                group[i] = newGroupId++;
            }
        }
        int totalGroups = newGroupId;

        // Build item graph
        List<Integer>[] itemAdj = new ArrayList[n];
        int[] indegItem = new int[n];
        for (int i = 0; i < n; i++) {
            itemAdj[i] = new ArrayList<>();
        }

        // Build group graph with deduplication
        List<Integer>[] groupAdj = new ArrayList[totalGroups];
        int[] indegGroup = new int[totalGroups];
        Set<Long> addedGroupEdges = new HashSet<>(); // encode (u,v) as ((long)u<<32)|v
        for (int i = 0; i < totalGroups; i++) {
            groupAdj[i] = new ArrayList<>();
        }

        for (int i = 0; i < n; i++) {
            int curGroup = group[i];
            for (int pre : beforeItems.get(i)) {
                // item edge
                itemAdj[pre].add(i);
                indegItem[i]++;

                int preGroup = group[pre];
                if (preGroup != curGroup) {
                    long code = ((long) preGroup << 32) | (curGroup & 0xffffffffL);
                    if (!addedGroupEdges.contains(code)) {
                        addedGroupEdges.add(code);
                        groupAdj[preGroup].add(curGroup);
                        indegGroup[curGroup]++;
                    }
                }
            }
        }

        // Topological sort groups
        List<Integer> groupOrder = topoSort(totalGroups, groupAdj, indegGroup);
        if (groupOrder == null) return new int[0];

        // Topological sort items
        List<Integer> itemOrder = topoSort(n, itemAdj, indegItem);
        if (itemOrder == null) return new int[0];

        // Collect items per group preserving item topological order
        Map<Integer, List<Integer>> itemsInGroup = new HashMap<>();
        for (int item : itemOrder) {
            itemsInGroup.computeIfAbsent(group[item], k -> new ArrayList<>()).add(item);
        }

        // Build final result following group order
        int[] result = new int[n];
        int idx = 0;
        for (int g : groupOrder) {
            List<Integer> list = itemsInGroup.getOrDefault(g, Collections.emptyList());
            for (int item : list) {
                result[idx++] = item;
            }
        }

        return result;
    }

    private List<Integer> topoSort(int nodeCount, List<Integer>[] adj, int[] indeg) {
        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < nodeCount; i++) {
            if (indeg[i] == 0) queue.add(i);
        }
        List<Integer> order = new ArrayList<>(nodeCount);
        while (!queue.isEmpty()) {
            int u = queue.poll();
            order.add(u);
            for (int v : adj[u]) {
                indeg[v]--;
                if (indeg[v] == 0) queue.add(v);
            }
        }
        return order.size() == nodeCount ? order : null;
    }
}
```

## Python

```python
class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque

        # Assign unique groups to items with no group
        new_group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = new_group_id
                new_group_id += 1
        total_groups = new_group_id

        # Build item graph and group graph
        item_adj = [[] for _ in range(n)]
        indeg_item = [0] * n

        group_adj = [[] for _ in range(total_groups)]
        indeg_group = [0] * total_groups
        added_group_edges = set()

        for i in range(n):
            cur_g = group[i]
            for pre in beforeItems[i]:
                pre_g = group[pre]
                # item edge pre -> i
                item_adj[pre].append(i)
                indeg_item[i] += 1
                # if groups differ, add group edge
                if pre_g != cur_g:
                    edge = (pre_g, cur_g)
                    if edge not in added_group_edges:
                        added_group_edges.add(edge)
                        group_adj[pre_g].append(cur_g)
                        indeg_group[cur_g] += 1

        # Topological sort for items
        q = deque([i for i in range(n) if indeg_item[i] == 0])
        item_order = []
        while q:
            u = q.popleft()
            item_order.append(u)
            for v in item_adj[u]:
                indeg_item[v] -= 1
                if indeg_item[v] == 0:
                    q.append(v)

        if len(item_order) != n:
            return []

        # Topological sort for groups
        q = deque([g for g in range(total_groups) if indeg_group[g] == 0])
        group_order = []
        while q:
            g = q.popleft()
            group_order.append(g)
            for nb in group_adj[g]:
                indeg_group[nb] -= 1
                if indeg_group[nb] == 0:
                    q.append(nb)

        if len(group_order) != total_groups:
            return []

        # Bucket items by group preserving item order
        buckets = [[] for _ in range(total_groups)]
        for item in item_order:
            buckets[group[item]].append(item)

        # Concatenate according to group order
        result = []
        for g in group_order:
            result.extend(buckets[g])

        return result
```

## Python3

```python
from typing import List
from collections import defaultdict, deque

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Assign unique groups to items with no group
        new_group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = new_group_id
                new_group_id += 1
        total_groups = new_group_id

        # Build item graph
        item_adj = [[] for _ in range(n)]
        indeg_item = [0] * n

        # Build group graph
        group_adj = [[] for _ in range(total_groups)]
        indeg_group = [0] * total_groups
        seen_group_edges = set()

        for i in range(n):
            for pre in beforeItems[i]:
                # item edge pre -> i
                item_adj[pre].append(i)
                indeg_item[i] += 1

                g_pre, g_cur = group[pre], group[i]
                if g_pre != g_cur:
                    if (g_pre, g_cur) not in seen_group_edges:
                        seen_group_edges.add((g_pre, g_cur))
                        group_adj[g_pre].append(g_cur)
                        indeg_group[g_cur] += 1

        # Topological sort for items
        q = deque([i for i in range(n) if indeg_item[i] == 0])
        item_order = []
        while q:
            u = q.popleft()
            item_order.append(u)
            for v in item_adj[u]:
                indeg_item[v] -= 1
                if indeg_item[v] == 0:
                    q.append(v)

        if len(item_order) != n:
            return []  # cycle among items

        # Collect items per group preserving item order
        group_to_items = defaultdict(list)
        for itm in item_order:
            group_to_items[group[itm]].append(itm)

        # Topological sort for groups
        qg = deque([g for g in range(total_groups) if indeg_group[g] == 0])
        group_order = []
        while qg:
            g = qg.popleft()
            group_order.append(g)
            for ng in group_adj[g]:
                indeg_group[ng] -= 1
                if indeg_group[ng] == 0:
                    qg.append(ng)

        if len(group_order) != total_groups:
            return []  # cycle among groups

        # Build final result
        res = []
        for g in group_order:
            res.extend(group_to_items.get(g, []))
        return res
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortItems(int n, int m, int* group, int groupSize, int** beforeItems,
               int beforeItemsSize, int* beforeItemsColSize, int* returnSize) {
    // Assign new groups for items with no group
    int totalGroups = m;
    int *newGroup = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        if (group[i] == -1) {
            newGroup[i] = totalGroups++;
        } else {
            newGroup[i] = group[i];
        }
    }

    // Allocate indegree arrays
    int *itemIndeg = (int *)calloc(n, sizeof(int));
    int *groupIndeg = (int *)calloc(totalGroups, sizeof(int));

    // Count outgoing edges for items and raw group edges (with duplicates)
    int *outCntItem = (int *)calloc(n, sizeof(int));
    int *outCntGroupRaw = (int *)calloc(totalGroups, sizeof(int));

    for (int i = 0; i < n; ++i) {
        int sz = beforeItemsColSize[i];
        for (int j = 0; j < sz; ++j) {
            int pre = beforeItems[i][j]; // edge: pre -> i
            outCntItem[pre]++;          // item graph
            itemIndeg[i]++;

            if (newGroup[pre] != newGroup[i]) {
                outCntGroupRaw[newGroup[pre]]++;
            }
        }
    }

    // Allocate adjacency lists for items
    int **itemAdj = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        if (outCntItem[i] > 0) {
            itemAdj[i] = (int *)malloc(outCntItem[i] * sizeof(int));
        } else {
            itemAdj[i] = NULL;
        }
    }

    // Allocate raw adjacency lists for groups
    int **groupAdjRaw = (int **)malloc(totalGroups * sizeof(int *));
    for (int g = 0; g < totalGroups; ++g) {
        if (outCntGroupRaw[g] > 0) {
            groupAdjRaw[g] = (int *)malloc(outCntGroupRaw[g] * sizeof(int));
        } else {
            groupAdjRaw[g] = NULL;
        }
    }

    // Fill adjacency lists
    int *curItemPos = (int *)calloc(n, sizeof(int));
    int *curGroupPos = (int *)calloc(totalGroups, sizeof(int));

    for (int i = 0; i < n; ++i) {
        int sz = beforeItemsColSize[i];
        for (int j = 0; j < sz; ++j) {
            int pre = beforeItems[i][j]; // edge: pre -> i
            itemAdj[pre][curItemPos[pre]++] = i;

            if (newGroup[pre] != newGroup[i]) {
                int gu = newGroup[pre];
                int gv = newGroup[i];
                groupAdjRaw[gu][curGroupPos[gu]++] = gv;
            }
        }
    }

    // Deduplicate group edges and compute indegrees
    int **groupAdj = (int **)malloc(totalGroups * sizeof(int *));
    int *groupAdjSize = (int *)calloc(totalGroups, sizeof(int));

    for (int g = 0; g < totalGroups; ++g) {
        int cnt = outCntGroupRaw[g];
        if (cnt == 0) {
            groupAdj[g] = NULL;
            continue;
        }
        int *arr = groupAdjRaw[g];
        qsort(arr, cnt, sizeof(int), cmp_int);
        int write = 0;
        for (int i = 0; i < cnt; ++i) {
            if (i == 0 || arr[i] != arr[i - 1]) {
                arr[write++] = arr[i];
                groupIndeg[arr[i]]++;
            }
        }
        groupAdj[g] = arr;
        groupAdjSize[g] = write;
    }

    // Topological sort groups
    int *queueG = (int *)malloc(totalGroups * sizeof(int));
    int headG = 0, tailG = 0;
    for (int g = 0; g < totalGroups; ++g) {
        if (groupIndeg[g] == 0) queueG[tailG++] = g;
    }
    int *groupOrder = (int *)malloc(totalGroups * sizeof(int));
    int idxG = 0;
    while (headG < tailG) {
        int cur = queueG[headG++];
        groupOrder[idxG++] = cur;
        for (int i = 0; i < groupAdjSize[cur]; ++i) {
            int nb = groupAdj[cur][i];
            if (--groupIndeg[nb] == 0) queueG[tailG++] = nb;
        }
    }
    if (idxG != totalGroups) { // cycle in groups
        *returnSize = 0;
        free(newGroup);
        free(itemIndeg);
        free(groupIndeg);
        free(outCntItem);
        free(outCntGroupRaw);
        for (int i = 0; i < n; ++i) if (itemAdj[i]) free(itemAdj[i]);
        free(itemAdj);
        for (int g = 0; g < totalGroups; ++g) if (groupAdjRaw[g]) free(groupAdjRaw[g]);
        free(groupAdjRaw);
        free(curItemPos);
        free(curGroupPos);
        free(queueG);
        free(groupOrder);
        return NULL;
    }

    // Topological sort items
    int *queueI = (int *)malloc(n * sizeof(int));
    int headI = 0, tailI = 0;
    for (int i = 0; i < n; ++i) {
        if (itemIndeg[i] == 0) queueI[tailI++] = i;
    }
    int *itemOrder = (int *)malloc(n * sizeof(int));
    int idxI = 0;
    while (headI < tailI) {
        int cur = queueI[headI++];
        itemOrder[idxI++] = cur;
        for (int k = 0; k < outCntItem[cur]; ++k) {
            int nb = itemAdj[cur][k];
            if (--itemIndeg[nb] == 0) queueI[tailI++] = nb;
        }
    }
    if (idxI != n) { // cycle in items
        *returnSize = 0;
        free(newGroup);
        free(itemIndeg);
        free(groupIndeg);
        free(outCntItem);
        free(outCntGroupRaw);
        for (int i = 0; i < n; ++i) if (itemAdj[i]) free(itemAdj[i]);
        free(itemAdj);
        for (int g = 0; g < totalGroups; ++g) if (groupAdjRaw[g]) free(groupAdjRaw[g]);
        free(groupAdjRaw);
        free(curItemPos);
        free(curGroupPos);
        free(queueG);
        free(groupOrder);
        free(queueI);
        free(itemOrder);
        return NULL;
    }

    // Collect items per group preserving item order
    int *groupCap = (int *)calloc(totalGroups, sizeof(int));
    int **groupItems = (int **)malloc(totalGroups * sizeof(int *));
    int *groupCnt = (int *)calloc(totalGroups, sizeof(int));

    for (int i = 0; i < n; ++i) {
        int itm = itemOrder[i];
        int g = newGroup[itm];
        if (groupCnt[g] == groupCap[g]) {
            int newCap = groupCap[g] ? groupCap[g] * 2 : 4;
            groupItems[g] = (int *)realloc(groupItems[g], newCap * sizeof(int));
            groupCap[g] = newCap;
        }
        groupItems[g][groupCnt[g]++] = itm;
    }

    // Build final result according to group order
    int *result = (int *)malloc(n * sizeof(int));
    int pos = 0;
    for (int i = 0; i < totalGroups; ++i) {
        int g = groupOrder[i];
        for (int j = 0; j < groupCnt[g]; ++j) {
            result[pos++] = groupItems[g][j];
        }
    }

    *returnSize = n;

    // Free temporary allocations
    free(newGroup);
    free(itemIndeg);
    free(groupIndeg);
    free(outCntItem);
    free(outCntGroupRaw);
    for (int i = 0; i < n; ++i) if (itemAdj[i]) free(itemAdj[i]);
    free(itemAdj);
    for (int g = 0; g < totalGroups; ++g) if (groupAdjRaw[g]) free(groupAdjRaw[g]);
    free(groupAdjRaw);
    free(curItemPos);
    free(curGroupPos);
    free(queueG);
    free(groupOrder);
    free(queueI);
    free(itemOrder);
    for (int g = 0; g < totalGroups; ++g) if (groupItems[g]) free(groupItems[g]);
    free(groupItems);
    free(groupCap);
    free(groupCnt);
    free(groupAdj);
    free(groupAdjSize);

    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] SortItems(int n, int m, int[] group, IList<IList<int>> beforeItems) {
        // Assign unique groups to items with no group
        int newGroupId = m;
        for (int i = 0; i < n; i++) {
            if (group[i] == -1) {
                group[i] = newGroupId++;
            }
        }
        int totalGroups = newGroupId;

        // Build item graph
        var itemAdj = new List<int>[n];
        var indegItem = new int[n];
        for (int i = 0; i < n; i++) itemAdj[i] = new List<int>();

        // Build group graph
        var groupAdj = new List<int>[totalGroups];
        var indegGroup = new int[totalGroups];
        for (int i = 0; i < totalGroups; i++) groupAdj[i] = new List<int>();

        // Collect items per group (optional)
        // var itemsInGroup = new List<int>[totalGroups];
        // for (int i = 0; i < totalGroups; i++) itemsInGroup[i] = new List<int>();
        // for (int i = 0; i < n; i++) itemsInGroup[group[i]].Add(i);

        // Build edges
        for (int i = 0; i < n; i++) {
            foreach (int pre in beforeItems[i]) {
                itemAdj[pre].Add(i);
                indegItem[i]++;

                int gPre = group[pre];
                int gCur = group[i];
                if (gPre != gCur) {
                    groupAdj[gPre].Add(gCur);
                    indegGroup[gCur]++;
                }
            }
        }

        // Topological sort groups
        var qGroup = new Queue<int>();
        for (int i = 0; i < totalGroups; i++) {
            if (indegGroup[i] == 0) qGroup.Enqueue(i);
        }
        var groupOrder = new List<int>();
        while (qGroup.Count > 0) {
            int g = qGroup.Dequeue();
            groupOrder.Add(g);
            foreach (int nb in groupAdj[g]) {
                indegGroup[nb]--;
                if (indegGroup[nb] == 0) qGroup.Enqueue(nb);
            }
        }
        if (groupOrder.Count != totalGroups) return new int[0]; // cycle in groups

        // Prepare queues for ready items per group
        var readyQueues = new Queue<int>[totalGroups];
        for (int i = 0; i < totalGroups; i++) readyQueues[i] = new Queue<int>();

        for (int i = 0; i < n; i++) {
            if (indegItem[i] == 0) {
                readyQueues[group[i]].Enqueue(i);
            }
        }

        var result = new List<int>(n);
        foreach (int g in groupOrder) {
            var q = readyQueues[g];
            while (q.Count > 0) {
                int item = q.Dequeue();
                result.Add(item);
                foreach (int nb in itemAdj[item]) {
                    indegItem[nb]--;
                    if (indegItem[nb] == 0) {
                        readyQueues[group[nb]].Enqueue(nb);
                    }
                }
            }
        }

        return result.Count == n ? result.ToArray() : new int[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} m
 * @param {number[]} group
 * @param {number[][]} beforeItems
 * @return {number[]}
 */
var sortItems = function(n, m, group, beforeItems) {
    // assign unique groups to items with no group
    let newGroupId = m;
    for (let i = 0; i < n; ++i) {
        if (group[i] === -1) {
            group[i] = newGroupId++;
        }
    }
    const totalGroups = newGroupId;

    // build item graph
    const itemAdj = Array.from({ length: n }, () => []);
    const itemIndeg = new Array(n).fill(0);

    // build group graph (use Set to avoid duplicate edges)
    const groupAdjSet = Array.from({ length: totalGroups }, () => new Set());
    const groupIndeg = new Array(totalGroups).fill(0);

    for (let i = 0; i < n; ++i) {
        for (const pre of beforeItems[i]) {
            // item edge pre -> i
            itemAdj[pre].push(i);
            itemIndeg[i]++;

            const gPre = group[pre];
            const gCur = group[i];
            if (gPre !== gCur && !groupAdjSet[gPre].has(gCur)) {
                groupAdjSet[gPre].add(gCur);
                groupIndeg[gCur]++;
            }
        }
    }

    // convert group adjacency sets to arrays for processing
    const groupAdj = groupAdjSet.map(s => Array.from(s));

    // topological sort helper (Kahn's algorithm)
    const kahn = (adj, indeg) => {
        const q = [];
        const res = [];
        const indegCopy = indeg.slice();
        for (let i = 0; i < indegCopy.length; ++i) {
            if (indegCopy[i] === 0) q.push(i);
        }
        let idx = 0;
        while (idx < q.length) {
            const u = q[idx++];
            res.push(u);
            for (const v of adj[u]) {
                indegCopy[v]--;
                if (indegCopy[v] === 0) q.push(v);
            }
        }
        return res.length === indegCopy.length ? res : [];
    };

    // topological order for groups and items
    const groupOrder = kahn(groupAdj, groupIndeg);
    if (groupOrder.length === 0) return [];

    const itemOrder = kahn(itemAdj, itemIndeg);
    if (itemOrder.length === 0) return [];

    // bucket items by their group preserving item order
    const buckets = Array.from({ length: totalGroups }, () => []);
    for (const item of itemOrder) {
        buckets[group[item]].push(item);
    }

    // concatenate groups according to group order
    const result = [];
    for (const g of groupOrder) {
        result.push(...buckets[g]);
    }
    return result;
};
```

## Typescript

```typescript
function sortItems(n: number, m: number, group: number[], beforeItems: number[][]): number[] {
    // Assign unique groups to items with no group
    const newGroup = group.slice();
    let curGroupId = m;
    for (let i = 0; i < n; i++) {
        if (newGroup[i] === -1) {
            newGroup[i] = curGroupId++;
        }
    }
    const totalGroups = curGroupId;

    // Build item graph
    const itemAdj: number[][] = Array.from({ length: n }, () => []);
    const itemIndeg = new Array(n).fill(0);
    for (let v = 0; v < n; v++) {
        for (const u of beforeItems[v]) {
            itemAdj[u].push(v);
            itemIndeg[v]++;
        }
    }

    // Build group graph
    const groupAdj: number[][] = Array.from({ length: totalGroups }, () => []);
    const groupIndeg = new Array(totalGroups).fill(0);
    for (let v = 0; v < n; v++) {
        const gv = newGroup[v];
        for (const u of beforeItems[v]) {
            const gu = newGroup[u];
            if (gu !== gv) {
                groupAdj[gu].push(gv);
                groupIndeg[gv]++;
            }
        }
    }

    // Topological sort helper
    function kahn(adj: number[][], indeg: number[]): number[] {
        const res: number[] = [];
        const queue: number[] = [];
        for (let i = 0; i < indeg.length; i++) {
            if (indeg[i] === 0) queue.push(i);
        }
        let qIdx = 0;
        while (qIdx < queue.length) {
            const node = queue[qIdx++];
            res.push(node);
            for (const nb of adj[node]) {
                indeg[nb]--;
                if (indeg[nb] === 0) queue.push(nb);
            }
        }
        return res.length === indeg.length ? res : [];
    }

    // Sort groups
    const groupOrder = kahn(groupAdj, groupIndeg.slice());
    if (groupOrder.length !== totalGroups) return [];

    // Sort items
    const itemOrder = kahn(itemAdj, itemIndeg.slice());
    if (itemOrder.length !== n) return [];

    // Collect items per group preserving intra-group order from itemOrder
    const itemsInGroup: number[][] = Array.from({ length: totalGroups }, () => []);
    for (const item of itemOrder) {
        itemsInGroup[newGroup[item]].push(item);
    }

    // Concatenate according to group order
    const result: number[] = [];
    for (const g of groupOrder) {
        result.push(...itemsInGroup[g]);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $m
     * @param Integer[] $group
     * @param Integer[][] $beforeItems
     * @return Integer[]
     */
    function sortItems($n, $m, $group, $beforeItems) {
        // Assign unique groups to items with no group
        $newGroupId = $m;
        for ($i = 0; $i < $n; $i++) {
            if ($group[$i] == -1) {
                $group[$i] = $newGroupId++;
            }
        }
        $totalGroups = $newGroupId;

        // Build graphs
        $itemAdj   = array_fill(0, $n, []);
        $indegItem = array_fill(0, $n, 0);
        $groupAdj   = array_fill(0, $totalGroups, []);
        $indegGroup = array_fill(0, $totalGroups, 0);
        $groupEdgeSet = [];

        for ($i = 0; $i < $n; $i++) {
            foreach ($beforeItems[$i] as $pre) {
                // item graph
                $itemAdj[$pre][] = $i;
                $indegItem[$i]++;

                // group graph if different groups
                $gFrom = $group[$pre];
                $gTo   = $group[$i];
                if ($gFrom != $gTo) {
                    $key = $gFrom . '-' . $gTo;
                    if (!isset($groupEdgeSet[$key])) {
                        $groupAdj[$gFrom][] = $gTo;
                        $indegGroup[$gTo]++;
                        $groupEdgeSet[$key] = true;
                    }
                }
            }
        }

        // Topological sort for groups
        $groupOrder = $this->topoSort($groupAdj, $indegGroup);
        if (empty($groupOrder) && $totalGroups > 0) {
            return [];
        }

        // Topological sort for items
        $itemOrder = $this->topoSort($itemAdj, $indegItem);
        if (empty($itemOrder) && $n > 0) {
            return [];
        }

        // Collect items per group preserving item topological order
        $itemsInGroup = [];
        foreach ($itemOrder as $it) {
            $g = $group[$it];
            $itemsInGroup[$g][] = $it;
        }

        // Build final result following group order
        $result = [];
        foreach ($groupOrder as $g) {
            if (isset($itemsInGroup[$g])) {
                foreach ($itemsInGroup[$g] as $it) {
                    $result[] = $it;
                }
            }
        }

        return $result;
    }

    /**
     * Kahn's algorithm for topological sorting.
     *
     * @param array $adj   adjacency list
     * @param array $indeg indegree array (will be modified)
     * @return array       ordered vertices, empty if cycle exists
     */
    private function topoSort($adj, &$indeg) {
        $queue = new SplQueue();
        $n = count($indeg);
        for ($i = 0; $i < $n; $i++) {
            if ($indeg[$i] == 0) {
                $queue->enqueue($i);
            }
        }

        $order = [];
        while (!$queue->isEmpty()) {
            $u = $queue->dequeue();
            $order[] = $u;
            foreach ($adj[$u] as $v) {
                $indeg[$v]--;
                if ($indeg[$v] == 0) {
                    $queue->enqueue($v);
                }
            }
        }

        return count($order) === $n ? $order : [];
    }
}
```

## Swift

```swift
class Solution {
    func sortItems(_ n: Int, _ m: Int, _ group: [Int], _ beforeItems: [[Int]]) -> [Int] {
        var newGroup = group
        var curGroup = m
        for i in 0..<n {
            if newGroup[i] == -1 {
                newGroup[i] = curGroup
                curGroup += 1
            }
        }
        let totalGroups = curGroup
        
        var itemAdj = [[Int]](repeating: [], count: n)
        var indegreeItem = [Int](repeating: 0, count: n)
        
        var groupAdj = [[Int]](repeating: [], count: totalGroups)
        var indegreeGroup = [Int](repeating: 0, count: totalGroups)
        
        for i in 0..<n {
            for pre in beforeItems[i] {
                itemAdj[pre].append(i)
                indegreeItem[i] += 1
                let gPre = newGroup[pre]
                let gCur = newGroup[i]
                if gPre != gCur {
                    groupAdj[gPre].append(gCur)
                    indegreeGroup[gCur] += 1
                }
            }
        }
        
        guard let itemOrder = topologicalSort(itemAdj, indegreeItem) else { return [] }
        guard let groupOrder = topologicalSort(groupAdj, indegreeGroup) else { return [] }
        
        var itemsInGroup = [[Int]](repeating: [], count: totalGroups)
        for item in itemOrder {
            let g = newGroup[item]
            itemsInGroup[g].append(item)
        }
        
        var result = [Int]()
        for g in groupOrder {
            result.append(contentsOf: itemsInGroup[g])
        }
        return result
    }
    
    private func topologicalSort(_ graph: [[Int]], _ indegreeOrig: [Int]) -> [Int]? {
        var indegree = indegreeOrig
        var queue = [Int]()
        for i in 0..<indegree.count where indegree[i] == 0 {
            queue.append(i)
        }
        var idx = 0
        var order = [Int]()
        while idx < queue.count {
            let node = queue[idx]
            idx += 1
            order.append(node)
            for nb in graph[node] {
                indegree[nb] -= 1
                if indegree[nb] == 0 {
                    queue.append(nb)
                }
            }
        }
        return order.count == graph.count ? order : nil
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sortItems(n: Int, m: Int, group: IntArray, beforeItems: List<List<Int>>): IntArray {
        // Assign unique groups to items with no group
        val newGroup = group.clone()
        var curGroup = m
        for (i in 0 until n) {
            if (newGroup[i] == -1) {
                newGroup[i] = curGroup++
            }
        }
        val totalGroups = curGroup

        // Build item graph
        val itemAdj = Array(n) { mutableListOf<Int>() }
        val indegreeItem = IntArray(n)

        // Build group graph (avoid duplicate edges)
        val groupAdj = Array(totalGroups) { mutableListOf<Int>() }
        val indegreeGroup = IntArray(totalGroups)
        val seenEdges = HashSet<Long>()

        for (i in 0 until n) {
            for (pre in beforeItems[i]) {
                // edge pre -> i
                itemAdj[pre].add(i)
                indegreeItem[i]++

                val gFrom = newGroup[pre]
                val gTo = newGroup[i]
                if (gFrom != gTo) {
                    val key = (gFrom.toLong() shl 32) or gTo.toLong()
                    if (!seenEdges.contains(key)) {
                        seenEdges.add(key)
                        groupAdj[gFrom].add(gTo)
                        indegreeGroup[gTo]++
                    }
                }
            }
        }

        // Topological sort helper
        fun topoSort(adj: Array<MutableList<Int>>, indegOrig: IntArray): IntArray? {
            val indeg = indegOrig.clone()
            val q: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
            for (i in indeg.indices) if (indeg[i] == 0) q.add(i)
            val order = IntArray(indeg.size)
            var idx = 0
            while (!q.isEmpty()) {
                val v = q.poll()
                order[idx++] = v
                for (nei in adj[v]) {
                    indeg[nei]--
                    if (indeg[nei] == 0) q.add(nei)
                }
            }
            return if (idx == adj.size) order else null
        }

        val groupOrder = topoSort(groupAdj, indegreeGroup) ?: return intArrayOf()
        val itemOrder = topoSort(itemAdj, indegreeItem) ?: return intArrayOf()

        // Collect items per group in the order given by itemOrder
        val itemsInGroup = Array(totalGroups) { mutableListOf<Int>() }
        for (item in itemOrder) {
            itemsInGroup[newGroup[item]].add(item)
        }

        // Build final result following groupOrder
        val result = IntArray(n)
        var pos = 0
        for (g in groupOrder) {
            for (it in itemsInGroup[g]) {
                result[pos++] = it
            }
        }
        return result
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  List<int> sortItems(int n, int m, List<int> group, List<List<int>> beforeItems) {
    // Assign unique groups to items with no group.
    int newGroupId = m;
    for (int i = 0; i < n; i++) {
      if (group[i] == -1) {
        group[i] = newGroupId;
        newGroupId++;
      }
    }
    int totalGroups = newGroupId;

    // Build item graph.
    List<List<int>> itemGraph = List.generate(n, (_) => []);
    List<int> indegItem = List.filled(n, 0);

    // Build group graph.
    List<List<int>> groupGraph = List.generate(totalGroups, (_) => []);
    List<int> indegGroup = List.filled(totalGroups, 0);
    List<Set<int>> groupEdgeSet = List.generate(totalGroups, (_) => <int>{});

    for (int i = 0; i < n; i++) {
      for (int pre in beforeItems[i]) {
        // Edge: pre -> i
        itemGraph[pre].add(i);
        indegItem[i]++;

        int gPre = group[pre];
        int gCur = group[i];
        if (gPre != gCur) {
          if (!groupEdgeSet[gPre].contains(gCur)) {
            groupEdgeSet[gPre].add(gCur);
            groupGraph[gPre].add(gCur);
            indegGroup[gCur]++;
          }
        }
      }
    }

    List<int> itemOrder = _topoSort(itemGraph, indegItem);
    if (itemOrder.isEmpty) return [];

    List<int> groupOrder = _topoSort(groupGraph, indegGroup);
    if (groupOrder.isEmpty) return [];

    // Map each group to its items in topological order.
    Map<int, List<int>> grpToItems = {};
    for (int item in itemOrder) {
      int g = group[item];
      grpToItems.putIfAbsent(g, () => []).add(item);
    }

    // Assemble final result respecting group order.
    List<int> result = [];
    for (int g in groupOrder) {
      if (grpToItems.containsKey(g)) {
        result.addAll(grpToItems[g]!);
      }
    }
    return result;
  }

  List<int> _topoSort(List<List<int>> graph, List<int> indegree) {
    int n = graph.length;
    List<int> indeg = List.from(indegree);
    Queue<int> q = ListQueue();
    for (int i = 0; i < n; i++) {
      if (indeg[i] == 0) q.add(i);
    }
    List<int> order = [];
    while (q.isNotEmpty) {
      int u = q.removeFirst();
      order.add(u);
      for (int v in graph[u]) {
        indeg[v]--;
        if (indeg[v] == 0) q.add(v);
      }
    }
    return order.length == n ? order : [];
  }
}
```

## Golang

```go
func sortItems(n int, m int, group []int, beforeItems [][]int) []int {
	// Assign unique groups to items with no group
	newGroupID := m
	for i := 0; i < n; i++ {
		if group[i] == -1 {
			group[i] = newGroupID
			newGroupID++
		}
	}
	totalGroups := newGroupID

	// Build item graph
	itemAdj := make([][]int, n)
	indegItem := make([]int, n)

	// Build group graph
	groupAdj := make([][]int, totalGroups)
	indegGroup := make([]int, totalGroups)

	for v := 0; v < n; v++ {
		for _, u := range beforeItems[v] {
			// edge u -> v for items
			itemAdj[u] = append(itemAdj[u], v)
			indegItem[v]++

			gu, gv := group[u], group[v]
			if gu != gv {
				groupAdj[gu] = append(groupAdj[gu], gv)
				indegGroup[gv]++
			}
		}
	}

	// Topological sort for items
	itemOrder := topologicalSort(itemAdj, indegItem)
	if itemOrder == nil {
		return []int{}
	}

	// Collect items per group preserving item order
	groupItems := make([][]int, totalGroups)
	for _, itm := range itemOrder {
		g := group[itm]
		groupItems[g] = append(groupItems[g], itm)
	}

	// Topological sort for groups
	groupOrder := topologicalSort(groupAdj, indegGroup)
	if groupOrder == nil {
		return []int{}
	}

	// Concatenate items according to group order
	result := make([]int, 0, n)
	for _, g := range groupOrder {
		result = append(result, groupItems[g]...)
	}
	return result
}

// Kahn's algorithm for topological sorting.
// Returns nil if a cycle exists.
func topologicalSort(adj [][]int, indeg []int) []int {
	n := len(indeg)
	q := make([]int, 0, n)
	for i := 0; i < n; i++ {
		if indeg[i] == 0 {
			q = append(q, i)
		}
	}
	order := make([]int, 0, n)
	for len(q) > 0 {
		v := q[0]
		q = q[1:]
		order = append(order, v)
		for _, nb := range adj[v] {
			indeg[nb]--
			if indeg[nb] == 0 {
				q = append(q, nb)
			}
		}
	}
	if len(order) != n {
		return nil
	}
	return order
}
```

## Ruby

```ruby
def sort_items(n, m, group, before_items)
  require 'set'
  # Assign unique groups to items with no group
  new_group_id = m
  (0...n).each do |i|
    if group[i] == -1
      group[i] = new_group_id
      new_group_id += 1
    end
  end
  total_groups = new_group_id

  adj_items = Array.new(n) { [] }
  indeg_items = Array.new(n, 0)

  adj_groups = Array.new(total_groups) { [] }
  indeg_groups = Array.new(total_groups, 0)
  edge_set = Set.new

  (0...n).each do |i|
    before_items[i].each do |pre|
      # item graph
      adj_items[pre] << i
      indeg_items[i] += 1

      g_from = group[pre]
      g_to   = group[i]
      if g_from != g_to
        pair = [g_from, g_to]
        unless edge_set.include?(pair)
          adj_groups[g_from] << g_to
          indeg_groups[g_to] += 1
          edge_set.add(pair)
        end
      end
    end
  end

  topo_sort = lambda do |node_cnt, adj, indeg|
    queue = []
    node_cnt.times { |i| queue << i if indeg[i] == 0 }
    order = []
    until queue.empty?
      u = queue.shift
      order << u
      adj[u].each do |v|
        indeg[v] -= 1
        queue << v if indeg[v] == 0
      end
    end
    order.size == node_cnt ? order : []
  end

  item_order = topo_sort.call(n, adj_items, indeg_items.dup)
  return [] if item_order.empty?

  group_order = topo_sort.call(total_groups, adj_groups, indeg_groups.dup)
  return [] if group_order.empty?

  items_by_group = Hash.new { |h, k| h[k] = [] }
  item_order.each do |i|
    items_by_group[group[i]] << i
  end

  result = []
  group_order.each do |g|
    result.concat(items_by_group[g]) if items_by_group.key?(g)
  end
  result
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.{ArrayBuffer, ArrayDeque}

  def sortItems(n: Int, m: Int, group: Array[Int], beforeItems: List[List[Int]]): Array[Int] = {
    // Assign unique groups to items with no group
    var newGroupId = m
    for (i <- 0 until n) {
      if (group(i) == -1) {
        group(i) = newGroupId
        newGroupId += 1
      }
    }
    val totalGroups = newGroupId

    // Build item graph
    val adjItem = Array.fill(n)(ArrayBuffer[Int]())
    val indegItem = Array.ofDim[Int](n)

    // Build group graph
    val adjGroup = Array.fill(totalGroups)(ArrayBuffer[Int]())
    val indegGroup = Array.ofDim[Int](totalGroups)

    for (i <- 0 until n) {
      for (pre <- beforeItems(i)) {
        // edge pre -> i
        adjItem(pre).append(i)
        indegItem(i) += 1

        if (group(pre) != group(i)) {
          adjGroup(group(pre)).append(group(i))
          indegGroup(group(i)) += 1
        }
      }
    }

    def topoSort(nodes: Int, adj: Array[ArrayBuffer[Int]], indegOrig: Array[Int]): Option[Array[Int]] = {
      val indeg = indegOrig.clone()
      val q = new ArrayDeque[Int]()
      for (i <- 0 until nodes if indeg(i) == 0) q.addLast(i)
      val res = new Array[Int](nodes)
      var idx = 0
      while (!q.isEmpty) {
        val u = q.removeFirst()
        res(idx) = u
        idx += 1
        for (v <- adj(u)) {
          indeg(v) -= 1
          if (indeg(v) == 0) q.addLast(v)
        }
      }
      if (idx == nodes) Some(res) else None
    }

    val itemOrderOpt = topoSort(n, adjItem, indegItem)
    if (itemOrderOpt.isEmpty) return Array.empty[Int]

    val groupOrderOpt = topoSort(totalGroups, adjGroup, indegGroup)
    if (groupOrderOpt.isEmpty) return Array.empty[Int]

    val itemOrder = itemOrderOpt.get
    val groupOrder = groupOrderOpt.get

    // Collect items per group preserving item order
    val itemsInGroup = Array.fill(totalGroups)(ArrayBuffer[Int]())
    for (item <- itemOrder) {
      itemsInGroup(group(item)).append(item)
    }

    // Build final result following group order
    val result = new ArrayBuffer[Int]()
    for (g <- groupOrder) {
      result ++= itemsInGroup(g)
    }
    result.toArray
  }
}
```

## Rust

```rust
use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn sort_items(
        n: i32,
        m: i32,
        mut group: Vec<i32>,
        before_items: Vec<Vec<i32>>,
    ) -> Vec<i32> {
        let n = n as usize;
        let mut m = m as usize;

        // Assign unique groups to items with no group
        for i in 0..n {
            if group[i] == -1 {
                group[i] = m as i32;
                m += 1;
            }
        }

        // Build item graph
        let mut item_adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        let mut item_indeg: Vec<usize> = vec![0; n];

        // Build group graph
        let mut group_adj: Vec<Vec<usize>> = vec![Vec::new(); m];
        let mut group_indeg: Vec<usize> = vec![0; m];
        let mut edge_set: HashSet<(usize, usize)> = HashSet::new();

        for i in 0..n {
            for &pre_i32 in &before_items[i] {
                let pre = pre_i32 as usize;
                // item edge
                item_adj[pre].push(i);
                item_indeg[i] += 1;

                let g_pre = group[pre] as usize;
                let g_cur = group[i] as usize;
                if g_pre != g_cur {
                    if edge_set.insert((g_pre, g_cur)) {
                        group_adj[g_pre].push(g_cur);
                        group_indeg[g_cur] += 1;
                    }
                }
            }
        }

        // Topological sort for items
        let mut indeg_items = item_indeg.clone();
        let items_order = match topological_sort(&item_adj, &mut indeg_items) {
            Some(ord) => ord,
            None => return Vec::new(),
        };

        // Topological sort for groups
        let mut indeg_groups = group_indeg.clone();
        let groups_order = match topological_sort(&group_adj, &mut indeg_groups) {
            Some(ord) => ord,
            None => return Vec::new(),
        };

        // Collect items per group preserving item order
        let mut items_by_group: Vec<Vec<usize>> = vec![Vec::new(); m];
        for &item in &items_order {
            let g = group[item] as usize;
            items_by_group[g].push(item);
        }

        // Build final result following groups order
        let mut result: Vec<i32> = Vec::with_capacity(n);
        for &g in &groups_order {
            for &item in &items_by_group[g] {
                result.push(item as i32);
            }
        }
        result
    }
}

fn topological_sort(adj: &[Vec<usize>], indeg: &mut [usize]) -> Option<Vec<usize>> {
    let mut queue = VecDeque::new();
    for (i, &d) in indeg.iter().enumerate() {
        if d == 0 {
            queue.push_back(i);
        }
    }
    let mut order = Vec::with_capacity(indeg.len());
    while let Some(u) = queue.pop_front() {
        order.push(u);
        for &v in &adj[u] {
            indeg[v] -= 1;
            if indeg[v] == 0 {
                queue.push_back(v);
            }
        }
    }
    if order.len() == indeg.len() {
        Some(order)
    } else {
        None
    }
}
```

## Racket

```racket
(define/contract (sort-items n m group beforeItems)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((group-vec (list->vector group))
         (before-vec (list->vector beforeItems))
         ;; assign new groups to items with -1
         (new-group-id m)
         (assign-groups
          (for ([i (in-range n)])
            (when (= (vector-ref group-vec i) -1)
              (vector-set! group-vec i new-group-id)
              (set! new-group-id (+ new-group-id 1))))))
         (total-groups new-group-id)
         ;; adjacency lists and indegrees
         (item-adj (make-vector n '()))
         (item-indeg (make-vector n 0))
         (group-adj (make-vector total-groups '()))
         (group-indeg (make-vector total-groups 0))
         (edge-hash (make-hash)))
    ;; build graphs
    (for ([i (in-range n)])
      (let* ((gi (vector-ref group-vec i))
             (pre-list (vector-ref before-vec i)))
        (for ([pre pre-list])
          ;; item edge pre -> i
          (vector-set! item-adj pre (cons i (vector-ref item-adj pre)))
          (vector-set! item-indeg i (+ 1 (vector-ref item-indeg i)))
          ;; possible group edge
          (let ((gj (vector-ref group-vec pre)))
            (when (not (= gi gj))
              (define key (cons gi gj))
              (unless (hash-has-key? edge-hash key)
                (hash-set! edge-hash key #t)
                (vector-set! group-adj gi (cons gj (vector-ref group-adj gi)))
                (vector-set! group-indeg gj (+ 1 (vector-ref group-indeg gj))))))))))
    ;; topological sort helper
    (define (topo-sort adj indeg)
      (let* ((size (vector-length indeg))
             (queue (make-vector size 0))
             (head 0) (tail 0)
             (order '()))
        (for ([i (in-range size)])
          (when (= (vector-ref indeg i) 0)
            (vector-set! queue tail i)
            (set! tail (+ tail 1))))
        (let loop ()
          (if (< head tail)
              (let* ((u (vector-ref queue head))
                     (new-head (+ head 1)))
                (set! head new-head)
                (set! order (cons u order))
                (for ([v (in-list (vector-ref adj u))])
                  (let ([deg (- (vector-ref indeg v) 1)])
                    (vector-set! indeg v deg)
                    (when (= deg 0)
                      (vector-set! queue tail v)
                      (set! tail (+ tail 1)))))
                (loop))
              (if (= (length order) size)
                  (reverse order)
                  #f))))))
    ;; sort groups
    (let ((group-order (topo-sort group-adj (vector-copy group-indeg))))
      (if (not group-order)
          '()
          (let ((item-order (topo-sort item-adj (vector-copy item-indeg))))
            (if (not item-order)
                '()
                (let* ((groups-items (make-vector total-groups '()))
                       ;; collect items per group preserving topological order
                       )
                  (for ([it (in-list item-order)])
                    (let ((g (vector-ref group-vec it)))
                      (vector-set! groups-items g (cons it (vector-ref groups-items g)))))
                  (define result-vec (make-vector n))
                  (define pos 0)
                  (for ([grp (in-list group-order)])
                    (let ((lst (reverse (vector-ref groups-items grp))))
                      (for ([it (in-list lst)])
                        (vector-set! result-vec pos it)
                        (set! pos (+ pos 1)))))
                  (vector->list result-vec)))))))
```

## Erlang

```erlang
-export([sort_items/4]).

-spec sort_items(N :: integer(), M :: integer(), Group :: [integer()], BeforeItems :: [[integer()]]) -> [integer()].
sort_items(N, M, Group, BeforeItems) ->
    {NewGroupList, TotalGroups} = assign_groups(Group, M),
    GroupMap = maps:from_list(lists:zip(lists:seq(0, N-1), NewGroupList)),
    ItemIndeg0 = maps:from_list([{I, 0} || I <- lists:seq(0, N-1)]),
    GroupIndeg0 = maps:from_list([{G, 0} || G <- lists:seq(0, TotalGroups-1)]),

    {ItemAdj, ItemIndeg, GroupAdj, GroupIndeg} =
        build_graphs(N, NewGroupList, BeforeItems, ItemAdj0 = #{}, ItemIndeg0,
                     GroupAdj0 = #{}, GroupIndeg0),

    case topo_sort(N, ItemAdj, ItemIndeg) of
        {ok, ItemOrder} ->
            case topo_sort(TotalGroups, GroupAdj, GroupIndeg) of
                {ok, GroupOrder} ->
                    BucketMap = bucket_items(ItemOrder, GroupMap),
                    ListsPerGroup = [lists:reverse(maps:get(G, BucketMap, [])) || G <- GroupOrder],
                    lists:flatten(ListsPerGroup);
                error -> []
            end;
        error -> []
    end.

assign_groups(GroupList, M) ->
    assign_groups(GroupList, 0, M, [], M).

assign_groups([], _Idx, CurGroup, AccRev, Total) ->
    {lists:reverse(AccRev), Total};
assign_groups([G|Rest], Idx, CurGroup, AccRev, _) when G =:= -1 ->
    assign_groups(Rest, Idx+1, CurGroup+1, [CurGroup|AccRev], CurGroup+1);
assign_groups([G|Rest], Idx, CurGroup, AccRev, Total) ->
    assign_groups(Rest, Idx+1, CurGroup, [G|AccRev], Total).

build_graphs(N, GroupList, BeforeItems,
             ItemAdj0, ItemIndeg0, GroupAdj0, GroupIndeg0) ->
    build_graphs(0, N, GroupList, BeforeItems,
                 ItemAdj0, ItemIndeg0, GroupAdj0, GroupIndeg0).

build_graphs(I, N, _GroupList, _BeforeItems,
             ItemAdj, ItemIndeg, GroupAdj, GroupIndeg) when I >= N ->
    {ItemAdj, ItemIndeg, GroupAdj, GroupIndeg};
build_graphs(I, N, GroupList, BeforeItems,
             ItemAdj, ItemIndeg, GroupAdj, GroupIndeg) ->
    Deps = lists:nth(I+1, BeforeItems), % lists are 1-indexed
    {ItemAdj2, ItemIndeg2, GroupAdj2, GroupIndeg2} =
        process_deps(Deps, I, GroupList,
                     ItemAdj, ItemIndeg, GroupAdj, GroupIndeg),
    build_graphs(I+1, N, GroupList, BeforeItems,
                 ItemAdj2, ItemIndeg2, GroupAdj2, GroupIndeg2).

process_deps([], _Item, _GroupList,
             ItemAdj, ItemIndeg, GroupAdj, GroupIndeg) ->
    {ItemAdj, ItemIndeg, GroupAdj, GroupIndeg};
process_deps([Pre|Rest], Item, GroupList,
             ItemAdj, ItemIndeg, GroupAdj, GroupIndeg) ->
    % item graph edge Pre -> Item
    NewItemAdj = add_edge(ItemAdj, Pre, Item),
    NewItemIndeg = inc_indeg(ItemIndeg, Item),

    GPre = lists:nth(Pre+1, GroupList),
    GItem = lists:nth(Item+1, GroupList),
    {NewGroupAdj, NewGroupIndeg} =
        if GPre =/= GItem ->
                GA = add_edge(GroupAdj, GPre, GItem),
                GI = inc_indeg(GroupIndeg, GItem),
                {GA, GI};
           true -> {GroupAdj, GroupIndeg}
        end,
    process_deps(Rest, Item, GroupList,
                 NewItemAdj, NewItemIndeg, NewGroupAdj, NewGroupIndeg).

add_edge(Adj, From, To) ->
    maps:update_with(From,
                     fun(L) -> [To|L] end,
                     [To],
                     Adj).

inc_indeg(IndegMap, Node) ->
    Old = maps:get(Node, IndegMap),
    maps:put(Node, Old + 1, IndegMap).

topo_sort(NodeCount, AdjMap, IndegMap) ->
    ZeroQueue = [Node || Node <- lists:seq(0, NodeCount-1), maps:get(Node, IndegMap) =:= 0],
    topo_process(ZeroQueue, AdjMap, IndegMap, [], NodeCount).

topo_process([], _AdjMap, _IndegMap, OrderRev, Total) ->
    if length(OrderRev) =:= Total -> {ok, lists:reverse(OrderRev)}; true -> error end;
topo_process([Node|RestQueue], AdjMap, IndegMap, OrderRev, Total) ->
    Neighs = maps:get(Node, AdjMap, []),
    {NewIndegMap, NewZeros} = reduce_neighbours(Neighs, IndegMap, []),
    Queue1 = RestQueue ++ lists:reverse(NewZeros),
    topo_process(Queue1, AdjMap, NewIndegMap, [Node|OrderRev], Total).

reduce_neighbours([], IndegMap, Zeros) ->
    {IndegMap, Zeros};
reduce_neighbours([N|Rest], IndegMap, Zeros) ->
    Deg = maps:get(N, IndegMap),
    NewDeg = Deg - 1,
    UpdatedIndeg = maps:put(N, NewDeg, IndegMap),
    NewZeros = if NewDeg =:= 0 -> [N|Zeros]; true -> Zeros end,
    reduce_neighbours(Rest, UpdatedIndeg, NewZeros).

bucket_items(ItemOrder, GroupMap) ->
    bucket_items(ItemOrder, GroupMap, #{}).

bucket_items([], _GroupMap, Acc) -> Acc;
bucket_items([I|Rest], GroupMap, Acc) ->
    G = maps:get(I, GroupMap),
    NewAcc = maps:update_with(G,
                              fun(L) -> [I|L] end,
                              [I],
                              Acc),
    bucket_items(Rest, GroupMap, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec sort_items(n :: integer, m :: integer, group :: [integer], before_items :: [[integer]]) :: [integer]
  def sort_items(n, m, group, before_items) do
    # Assign unique groups to items with no group
    {group_list_rev, total_groups} =
      Enum.reduce(0..(n - 1), {[], m}, fn i, {acc, gid} ->
        g = Enum.at(group, i)

        if g == -1 do
          {[gid | acc], gid + 1}
        else
          {[g | acc], gid}
        end
      end)

    group_list = Enum.reverse(group_list_rev)
    groups_arr = :array.from_list(group_list)

    # Initialize adjacency lists and indegree arrays
    item_adj = :array.new(n, [])
    item_indeg = :array.new(n, 0)
    group_adj = :array.new(total_groups, [])
    group_indeg = :array.new(total_groups, 0)

    {item_adj, item_indeg, group_adj, group_indeg} =
      Enum.reduce(Enum.with_index(before_items), {item_adj, item_indeg, group_adj, group_indeg},
        fn {pres, i}, {ia, indeg_i_arr, ga, gindeg_arr} ->
          g_i = :array.get(i, groups_arr)

          Enum.reduce(pres, {ia, indeg_i_arr, ga, gindeg_arr},
            fn b, {ia2, indeg2, ga2, gindeg2} ->
              # update item indegree
              indeg_val = :array.get(i, indeg2) + 1
              indeg2 = :array.set(i, indeg_val, indeg2)

              # add edge b -> i
              nb_list = :array.get(b, ia2)
              ia2 = :array.set(b, [i | nb_list], ia2)

              g_b = :array.get(b, groups_arr)

              if g_i != g_b do
                # update group indegree
                gindeg_val = :array.get(g_i, gindeg2) + 1
                gindeg2 = :array.set(g_i, gindeg_val, gindeg2)

                # add edge g_b -> g_i
                gb_list = :array.get(g_b, ga2)
                ga2 = :array.set(g_b, [g_i | gb_list], ga2)
              end

              {ia2, indeg2, ga2, gindeg2}
            end)
        end)

    # Topological sort for items
    item_order = kahn(item_adj, item_indeg, n)
    if item_order == [] do
      []
    else
      # Topological sort for groups
      group_order = kahn(group_adj, group_indeg, total_groups)

      if group_order == [] do
        []
      else
        # Map items to their groups preserving item order
        group_items_arr =
          Enum.reduce(item_order, :array.new(total_groups, []), fn item, arr ->
            g = :array.get(item, groups_arr)
            lst = :array.get(g, arr)
            :array.set(g, [item | lst], arr)
          end)

        # Build final result following group order
        Enum.reduce(group_order, [], fn g, acc ->
          lst_rev = :array.get(g, group_items_arr)
          lst = Enum.reverse(lst_rev)
          acc ++ lst
        end)
      end
    end
  end

  defp kahn(adj, indeg, n) do
    initial_queue =
      for i <- 0..(n - 1), :array.get(i, indeg) == 0, do: i
      |> :queue.from_list()

    {order, _} = kahn_loop(initial_queue, adj, indeg, [])
    if length(order) == n, do: order, else: []
  end

  defp kahn_loop(queue, adj, indeg, acc) do
    case :queue.out(queue) do
      {:empty, _} ->
        {Enum.reverse(acc), indeg}

      {{:value, node}, q2} ->
        neighbors = :array.get(node, adj)

        {indeg2, q3} =
          Enum.reduce(neighbors, {inde g, q2}, fn nb, {ind_cur, q_cur} ->
            deg = :array.get(nb, ind_cur) - 1
            ind_cur = :array.set(nb, deg, ind_cur)

            if deg == 0 do
              {:queue.in(nb, q_cur), ind_cur}
            else
              {ind_cur, q_cur}
            end
          end)

        kahn_loop(q3, adj, indeg2, [node | acc])
    end
  end
end
```
