# 1766. Tree of Coprimes

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> getCoprimes(vector<int>& nums, vector<vector<int>>& edges) {
        int n = nums.size();
        vector<vector<int>> g(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            g[u].push_back(v);
            g[v].push_back(u);
        }
        vector<int> ans(n, -1);
        vector<int> nodeDepth(n, 0);
        const int MAXV = 50;
        vector<int> lastNode(MAXV + 1, -1);
        vector<int> depthVal(MAXV + 1, -1);

        struct Item {
            int u, p;
            bool enter;
            int prevNode, prevDepth;
        };
        vector<Item> st;
        st.reserve(2 * n);
        st.push_back({0, -1, true, -1, -1});

        while (!st.empty()) {
            Item cur = st.back();
            st.pop_back();

            if (cur.enter) {
                int u = cur.u, p = cur.p;
                int depth = (p == -1 ? 0 : nodeDepth[p] + 1);
                nodeDepth[u] = depth;

                int v = nums[u];
                int bestNode = -1, bestDepth = -1;
                for (int val = 1; val <= MAXV; ++val) {
                    if (std::gcd(v, val) == 1 && lastNode[val] != -1) {
                        if (depthVal[val] > bestDepth) {
                            bestDepth = depthVal[val];
                            bestNode = lastNode[val];
                        }
                    }
                }
                ans[u] = bestNode;

                int prevNode = lastNode[v];
                int prevDepth = depthVal[v];

                lastNode[v] = u;
                depthVal[v] = depth;

                // exit marker
                st.push_back({u, p, false, prevNode, prevDepth});

                // push children
                for (int i = (int)g[u].size() - 1; i >= 0; --i) {
                    int nb = g[u][i];
                    if (nb == p) continue;
                    st.push_back({nb, u, true, -1, -1});
                }
            } else {
                // restore state
                int v = nums[cur.u];
                lastNode[v] = cur.prevNode;
                depthVal[v] = cur.prevDepth;
            }
        }

        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] getCoprimes(int[] nums, int[][] edges) {
        int n = nums.length;
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }

        // precompute coprime matrix for values 1..50
        boolean[][] coprime = new boolean[51][51];
        for (int i = 1; i <= 50; i++) {
            for (int j = 1; j <= 50; j++) {
                coprime[i][j] = gcd(i, j) == 1;
            }
        }

        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        int[] lastNode = new int[51];          // latest node with given value on current path
        Arrays.fill(lastNode, -1);
        int[] depth = new int[n];              // depth of each node

        Deque<int[]> stack = new ArrayDeque<>();   // {node, parent, stage}
        Deque<int[]> changes = new ArrayDeque<>(); // {value, previousNode}
        stack.push(new int[]{0, -1, 0});           // start with root entering

        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            int node = cur[0];
            int parent = cur[1];
            int stage = cur[2];

            if (stage == 0) { // entering
                // compute answer using ancestors only
                int bestNode = -1;
                int bestDepth = -1;
                int val = nums[node];
                for (int v = 1; v <= 50; v++) {
                    if (coprime[val][v] && lastNode[v] != -1) {
                        int anc = lastNode[v];
                        if (depth[anc] > bestDepth) {
                            bestDepth = depth[anc];
                            bestNode = anc;
                        }
                    }
                }
                ans[node] = bestNode;

                // schedule exit
                stack.push(new int[]{node, parent, 1});

                // record previous occurrence of this value and update
                int prev = lastNode[val];
                changes.push(new int[]{val, prev});
                lastNode[val] = node;
                depth[node] = (parent == -1) ? 0 : depth[parent] + 1;

                // push children
                for (int nei : graph[node]) {
                    if (nei != parent) {
                        stack.push(new int[]{nei, node, 0});
                    }
                }
            } else { // exiting
                int[] change = changes.pop();
                int val = change[0];
                int prev = change[1];
                lastNode[val] = prev;
            }
        }

        return ans;
    }

    private static int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def getCoprimes(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        import sys
        from math import gcd

        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # precompute coprime values for 1..50
        coprime = [[] for _ in range(51)]
        for i in range(1, 51):
            for j in range(1, 51):
                if gcd(i, j) == 1:
                    coprime[i].append(j)

        # stacks[value] holds (node_index, depth) of nodes with that value on current path
        stacks = [[] for _ in range(51)]
        ans = [-1] * n

        sys.setrecursionlimit(200000)

        def dfs(u, parent, depth):
            val = nums[u]
            best_node = -1
            best_depth = -1
            # find deepest ancestor with coprime value
            for w in coprime[val]:
                if stacks[w]:
                    node_idx, d = stacks[w][-1]
                    if d > best_depth:
                        best_depth = d
                        best_node = node_idx
            ans[u] = best_node

            # push current node onto its value stack
            stacks[val].append((u, depth))

            for v in adj[u]:
                if v == parent:
                    continue
                dfs(v, u, depth + 1)

            # pop after returning
            stacks[val].pop()

        dfs(0, -1, 0)
        return ans
```

## Python3

```python
import sys
from math import gcd
from typing import List

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        sys.setrecursionlimit(300000)
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # precompute coprime values for each possible value 1..50
        max_val = 50
        coprime = [[] for _ in range(max_val + 1)]
        for i in range(1, max_val + 1):
            for j in range(1, max_val + 1):
                if gcd(i, j) == 1:
                    coprime[i].append(j)

        # last occurrence depth and node index for each value on current path
        depth_last = [-1] * (max_val + 1)
        node_last = [-1] * (max_val + 1)

        ans = [-1] * n

        def dfs(u: int, parent: int, depth: int) -> None:
            val = nums[u]
            best_node = -1
            best_depth = -1
            for v in coprime[val]:
                if depth_last[v] > best_depth:
                    best_depth = depth_last[v]
                    best_node = node_last[v]
            ans[u] = best_node

            # store previous state to backtrack later
            prev_depth = depth_last[val]
            prev_node = node_last[val]

            depth_last[val] = depth
            node_last[val] = u

            for w in adj[u]:
                if w != parent:
                    dfs(w, u, depth + 1)

            # restore previous state
            depth_last[val] = prev_depth
            node_last[val] = prev_node

        dfs(0, -1, 0)
        return ans
```

## C

```c
#include <stdlib.h>

static inline int gcd_int(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

typedef struct {
    int node;
    int parent;
    int childIdx;
    int prevLast;
} Frame;

int* getCoprimes(int* nums, int numsSize, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    int n = numsSize;
    // Build adjacency list
    int *deg = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        deg[u]++; deg[v]++;
    }
    int **adj = (int**)malloc(n * sizeof(int*));
    int *cur = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; ++i) {
        adj[i] = (int*)malloc(deg[i] * sizeof(int));
    }
    for (int i = 0; i < edgesSize; ++i) {
        int u = edges[i][0];
        int v = edges[i][1];
        adj[u][cur[u]++] = v;
        adj[v][cur[v]++] = u;
    }

    // Prepare answer and helper arrays
    int *ans = (int*)malloc(n * sizeof(int));
    int *depth = (int*)malloc(n * sizeof(int));
    int lastPos[51];
    for (int i = 0; i <= 50; ++i) lastPos[i] = -1;

    // Stack for iterative DFS
    Frame *stack = (Frame*)malloc(n * sizeof(Frame));
    int top = -1;

    // Process root node (0)
    depth[0] = 0;
    ans[0] = -1; // no ancestors
    int prevRoot = lastPos[nums[0]];
    lastPos[nums[0]] = 0;
    stack[++top] = (Frame){0, -1, 0, prevRoot};

    while (top >= 0) {
        Frame *f = &stack[top];
        if (f->childIdx < deg[f->node]) {
            int child = adj[f->node][f->childIdx++];
            if (child == f->parent) continue;
            depth[child] = depth[f->node] + 1;

            // Find closest coprime ancestor
            int best = -1, bestDepth = -1;
            for (int v = 1; v <= 50; ++v) {
                if (lastPos[v] != -1 && gcd_int(nums[child], v) == 1) {
                    int cand = lastPos[v];
                    if (depth[cand] > bestDepth) {
                        bestDepth = depth[cand];
                        best = cand;
                    }
                }
            }
            ans[child] = best;

            // Update state for child
            int prev = lastPos[nums[child]];
            lastPos[nums[child]] = child;
            stack[++top] = (Frame){child, f->node, 0, prev};
        } else {
            // Exit node, restore previous occurrence
            int val = nums[f->node];
            lastPos[val] = f->prevLast;
            top--;
        }
    }

    // Clean up temporary allocations
    for (int i = 0; i < n; ++i) free(adj[i]);
    free(adj);
    free(deg);
    free(cur);
    free(stack);
    free(depth);

    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] GetCoprimes(int[] nums, int[][] edges)
    {
        int n = nums.Length;
        var adj = new List<int>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<int>();
        foreach (var e in edges)
        {
            int u = e[0], v = e[1];
            adj[u].Add(v);
            adj[v].Add(u);
        }

        var ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = -1;
        var depth = new int[n];
        var lastNode = new int[51];
        for (int i = 0; i <= 50; i++) lastNode[i] = -1;

        var stack = new Stack<Frame>();
        stack.Push(new Frame { node = 0, parent = -1, childIdx = 0, entered = false });

        while (stack.Count > 0)
        {
            var f = stack.Peek();

            if (!f.entered)
            {
                int u = f.node;
                int best = -1, bestDepth = -1;
                int valU = nums[u];
                for (int v = 1; v <= 50; v++)
                {
                    if (Gcd(valU, v) == 1 && lastNode[v] != -1)
                    {
                        int anc = lastNode[v];
                        if (depth[anc] > bestDepth)
                        {
                            bestDepth = depth[anc];
                            best = anc;
                        }
                    }
                }
                ans[u] = best;

                f.prev = lastNode[valU];
                lastNode[valU] = u;
                f.entered = true;
            }

            f = stack.Peek(); // refresh reference after possible modifications

            if (f.childIdx < adj[f.node].Count)
            {
                int v = adj[f.node][f.childIdx++];
                if (v == f.parent) continue;
                depth[v] = depth[f.node] + 1;
                stack.Push(new Frame { node = v, parent = f.node, childIdx = 0, entered = false });
            }
            else
            {
                int u = f.node;
                lastNode[nums[u]] = f.prev; // restore previous occurrence
                stack.Pop();
            }
        }

        return ans;
    }

    private int Gcd(int a, int b)
    {
        while (b != 0)
        {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    class Frame
    {
        public int node;
        public int parent;
        public int childIdx;
        public int prev;
        public bool entered;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} edges
 * @return {number[]}
 */
var getCoprimes = function(nums, edges) {
    const n = nums.length;
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    // precompute coprime pairs for values 1..50
    const MAXV = 50;
    const coprime = Array.from({ length: MAXV + 1 }, () => new Uint8Array(MAXV + 1));
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    for (let i = 1; i <= MAXV; ++i) {
        for (let j = 1; j <= MAXV; ++j) {
            if (gcd(i, j) === 1) coprime[i][j] = 1;
        }
    }

    const lastSeen = new Int32Array(MAXV + 1).fill(-1); // latest node index on current path for each value
    const depth = new Int32Array(n);
    const ans = new Int32Array(n).fill(-1);

    // iterative DFS with explicit stack (enter/exit states)
    const stack = [{ node: 0, parent: -1, state: 0 }]; // state 0 = enter, 1 = exit
    while (stack.length) {
        const cur = stack.pop();
        if (cur.state === 0) { // entering node
            const node = cur.node;
            const parent = cur.parent;
            depth[node] = parent === -1 ? 0 : depth[parent] + 1;

            // find closest coprime ancestor
            let bestNode = -1;
            let bestDepth = -1;
            const val = nums[node];
            for (let v = 1; v <= MAXV; ++v) {
                if (coprime[val][v]) {
                    const anc = lastSeen[v];
                    if (anc !== -1 && depth[anc] > bestDepth) {
                        bestDepth = depth[anc];
                        bestNode = anc;
                    }
                }
            }
            ans[node] = bestNode;

            // save previous occurrence to restore later
            const prev = lastSeen[val];

            // schedule exit action
            stack.push({ node, parent, state: 1, prev });

            // update current value as latest on path
            lastSeen[val] = node;

            // push children
            for (const nei of adj[node]) {
                if (nei !== parent) {
                    stack.push({ node: nei, parent: node, state: 0 });
                }
            }
        } else { // exiting node, restore previous state
            const val = nums[cur.node];
            lastSeen[val] = cur.prev;
        }
    }

    return Array.from(ans);
};
```

## Typescript

```typescript
function getCoprimes(nums: number[], edges: number[][]): number[] {
    const n = nums.length;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const MAXV = 50;
    const coprime: boolean[][] = Array.from({ length: MAXV + 1 }, () => Array(MAXV + 1).fill(false));
    function gcd(a: number, b: number): number {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
    for (let i = 1; i <= MAXV; i++) {
        for (let j = 1; j <= MAXV; j++) {
            coprime[i][j] = gcd(i, j) === 1;
        }
    }

    const ans: number[] = new Array(n).fill(-1);
    const lastNode = new Int32Array(MAXV + 1);
    const depthVal = new Int32Array(MAXV + 1);
    for (let i = 0; i <= MAXV; i++) {
        lastNode[i] = -1;
        depthVal[i] = -1;
    }

    type StackEntry = {
        node: number;
        parent: number;
        depth: number;
        stage: 0 | 1;
        prevLast?: number;
        prevDepth?: number;
    };
    const stack: StackEntry[] = [];
    stack.push({ node: 0, parent: -1, depth: 0, stage: 0 });

    while (stack.length) {
        const cur = stack.pop()!;
        if (cur.stage === 0) {
            const val = nums[cur.node];
            let bestNode = -1;
            let bestDepth = -1;
            for (let w = 1; w <= MAXV; w++) {
                if (coprime[val][w] && lastNode[w] !== -1) {
                    if (depthVal[w] > bestDepth) {
                        bestDepth = depthVal[w];
                        bestNode = lastNode[w];
                    }
                }
            }
            ans[cur.node] = bestNode;

            const prevLast = lastNode[val];
            const prevDepth = depthVal[val];
            lastNode[val] = cur.node;
            depthVal[val] = cur.depth;

            stack.push({ node: cur.node, parent: cur.parent, depth: cur.depth, stage: 1, prevLast, prevDepth });
            for (const nb of adj[cur.node]) {
                if (nb === cur.parent) continue;
                stack.push({ node: nb, parent: cur.node, depth: cur.depth + 1, stage: 0 });
            }
        } else {
            const val = nums[cur.node];
            lastNode[val] = cur.prevLast!;
            depthVal[val] = cur.prevDepth!;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {
    private function gcd(int $a, int $b): int {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }

    /**
     * @param Integer[] $nums
     * @param Integer[][] $edges
     * @return Integer[]
     */
    function getCoprimes($nums, $edges) {
        $n = count($nums);
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $u = $e[0];
            $v = $e[1];
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }

        // Precompute coprime lists for values 1..50
        $coprime = array_fill(0, 51, []);
        for ($i = 1; $i <= 50; $i++) {
            $list = [];
            for ($j = 1; $j <= 50; $j++) {
                if ($this->gcd($i, $j) == 1) {
                    $list[] = $j;
                }
            }
            $coprime[$i] = $list;
        }

        // Stacks for each possible value on the current path
        $valueStacks = array_fill(0, 51, []);
        $ans = array_fill(0, $n, -1);

        // Stack entries: [node, parent, state (0=enter,1=exit), depth]
        $stack = [];
        $stack[] = [0, -1, 0, 0]; // start from root

        while (!empty($stack)) {
            $item = array_pop($stack);
            [$node, $parent, $state, $depth] = $item;

            if ($state === 0) { // entering node
                $v = $nums[$node];
                $bestNode = -1;
                $bestDepth = -1;

                foreach ($coprime[$v] as $cval) {
                    $list = $valueStacks[$cval];
                    if (!empty($list)) {
                        $candidate = end($list);
                        $candNode = $candidate[0];
                        $candDepth = $candidate[1];
                        if ($candDepth > $bestDepth) {
                            $bestDepth = $candDepth;
                            $bestNode = $candNode;
                        }
                    }
                }

                $ans[$node] = $bestNode;

                // Schedule exit processing
                $stack[] = [$node, $parent, 1, $depth];
                // Add current node to its value stack
                $valueStacks[$v][] = [$node, $depth];

                foreach ($adj[$node] as $nei) {
                    if ($nei === $parent) continue;
                    $stack[] = [$nei, $node, 0, $depth + 1];
                }
            } else { // exiting node
                $v = $nums[$node];
                array_pop($valueStacks[$v]);
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func getCoprimes(_ nums: [Int], _ edges: [[Int]]) -> [Int] {
        let n = nums.count
        var graph = [[Int]](repeating: [], count: n)
        for e in edges {
            let u = e[0]
            let v = e[1]
            graph[u].append(v)
            graph[v].append(u)
        }
        
        // Precompute coprime lists for values 1..50
        var coprime = [[Int]](repeating: [], count: 51)
        func gcd(_ a: Int, _ b: Int) -> Int {
            var x = a, y = b
            while y != 0 {
                let t = x % y
                x = y
                y = t
            }
            return x
        }
        for i in 1...50 {
            for j in 1...50 {
                if gcd(i, j) == 1 {
                    coprime[i].append(j)
                }
            }
        }
        
        var lastNode = [Int](repeating: -1, count: 51)
        var lastDepth = [Int](repeating: -1, count: 51)
        var ans = [Int](repeating: -1, count: n)
        
        struct Item {
            var node: Int
            var parent: Int
            var depth: Int
            var stage: Int   // 0 = enter, 1 = exit
            var prevNode: Int
            var prevDepth: Int
        }
        
        var stack: [Item] = []
        stack.append(Item(node: 0, parent: -1, depth: 0, stage: 0, prevNode: -1, prevDepth: -1))
        
        while let item = stack.popLast() {
            if item.stage == 0 {
                // compute answer using current ancestors
                let curVal = nums[item.node]
                var bestNode = -1
                var bestDepth = -1
                for v in coprime[curVal] {
                    let ancNode = lastNode[v]
                    if ancNode != -1 && lastDepth[v] > bestDepth {
                        bestDepth = lastDepth[v]
                        bestNode = ancNode
                    }
                }
                ans[item.node] = bestNode
                
                // save previous state for this value
                let prevN = lastNode[curVal]
                let prevD = lastDepth[curVal]
                // update with current node as latest ancestor
                lastNode[curVal] = item.node
                lastDepth[curVal] = item.depth
                
                // push exit event to restore later
                stack.append(Item(node: item.node, parent: item.parent, depth: item.depth, stage: 1, prevNode: prevN, prevDepth: prevD))
                
                // push children enter events
                for child in graph[item.node] {
                    if child == item.parent { continue }
                    stack.append(Item(node: child, parent: item.node, depth: item.depth + 1, stage: 0, prevNode: -1, prevDepth: -1))
                }
            } else {
                // restore previous state
                let curVal = nums[item.node]
                lastNode[curVal] = item.prevNode
                lastDepth[curVal] = item.prevDepth
            }
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getCoprimes(nums: IntArray, edges: Array<IntArray>): IntArray {
        val n = nums.size
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            val u = e[0]
            val v = e[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        // precompute coprime matrix for values 1..50
        val coprime = Array(51) { BooleanArray(51) }
        fun gcd(a: Int, b: Int): Int {
            var x = a
            var y = b
            while (y != 0) {
                val t = x % y
                x = y
                y = t
            }
            return x
        }
        for (i in 1..50) {
            for (j in 1..50) {
                coprime[i][j] = gcd(i, j) == 1
            }
        }

        val ans = IntArray(n) { -1 }
        val lastNode = IntArray(51) { -1 }   // deepest node index with given value on current path
        val lastDepth = IntArray(51) { -1 }  // its depth
        val depth = IntArray(n)
        val prevNodeArr = IntArray(n)
        val prevDepthArr = IntArray(n)

        data class Frame(val node: Int, val parent: Int, val state: Int) // state 0=enter,1=exit

        val stack = ArrayDeque<Frame>()
        stack.addLast(Frame(0, -1, 0))

        while (stack.isNotEmpty()) {
            val f = stack.removeLast()
            val u = f.node
            val p = f.parent
            if (f.state == 0) { // entering node
                depth[u] = if (p == -1) 0 else depth[p] + 1

                var bestNode = -1
                var bestDepth = -1
                val curVal = nums[u]
                for (v in 1..50) {
                    if (coprime[curVal][v]) {
                        val anc = lastNode[v]
                        if (anc != -1 && lastDepth[v] > bestDepth) {
                            bestDepth = lastDepth[v]
                            bestNode = anc
                        }
                    }
                }
                ans[u] = bestNode

                // schedule exit after processing children
                stack.addLast(Frame(u, p, 1))

                // save previous state for this value
                prevNodeArr[u] = lastNode[curVal]
                prevDepthArr[u] = lastDepth[curVal]

                // update with current node as latest occurrence of its value
                lastNode[curVal] = u
                lastDepth[curVal] = depth[u]

                // push children
                for (v in adj[u]) {
                    if (v != p) {
                        stack.addLast(Frame(v, u, 0))
                    }
                }
            } else { // exiting node, restore previous state
                val curVal = nums[u]
                lastNode[curVal] = prevNodeArr[u]
                lastDepth[curVal] = prevDepthArr[u]
            }
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> getCoprimes(List<int> nums, List<List<int>> edges) {
    int n = nums.length;
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var e in edges) {
      int u = e[0];
      int v = e[1];
      adj[u].add(v);
      adj[v].add(u);
    }

    List<int> ans = List.filled(n, -1);
    List<int> depth = List.filled(n, 0);
    List<int> lastSeen = List.filled(51, -1);

    int _gcd(int a, int b) {
      while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
      }
      return a;
    }

    class _Item {
      int node;
      int parent;
      int state; // 0 = enter, 1 = exit
      int prev;
      _Item(this.node, this.parent, this.state, this.prev);
    }

    List<_Item> stack = [];
    stack.add(_Item(0, -1, 0, -2));

    while (stack.isNotEmpty) {
      var cur = stack.removeLast();
      int u = cur.node;
      if (cur.state == 0) {
        // entering node
        int val = nums[u];
        int bestNode = -1;
        int bestDepth = -1;
        for (int v = 1; v <= 50; v++) {
          if (_gcd(val, v) == 1 && lastSeen[v] != -1) {
            int anc = lastSeen[v];
            if (depth[anc] > bestDepth) {
              bestDepth = depth[anc];
              bestNode = anc;
            }
          }
        }
        ans[u] = bestNode;

        int prev = lastSeen[val];
        lastSeen[val] = u;

        // push exit state
        stack.add(_Item(u, cur.parent, 1, prev));

        // push children
        for (int v in adj[u]) {
          if (v == cur.parent) continue;
          depth[v] = depth[u] + 1;
          stack.add(_Item(v, u, 0, -2));
        }
      } else {
        // exiting node, restore previous state
        int val = nums[u];
        lastSeen[val] = cur.prev;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func getCoprimes(nums []int, edges [][]int) []int {
	type stackItem struct {
		node   int
		parent int
		state  int // 0 = enter, 1 = exit
	}
	n := len(nums)
	adj := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}

	// precompute coprime lists for values 1..50
	coprimeVals := make([][]int, 51)
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	for i := 1; i <= 50; i++ {
		for j := 1; j <= 50; j++ {
			if gcd(i, j) == 1 {
				coprimeVals[i] = append(coprimeVals[i], j)
			}
		}
	}

	ans := make([]int, n)
	depth := make([]int, n)
	lastSeen := make([]int, 51)
	prevSeen := make([]int, n) // store previous lastSeen for each node's value
	for i := range lastSeen {
		lastSeen[i] = -1
	}
	for i := range ans {
		ans[i] = -1
	}

	stack := []stackItem{{node: 0, parent: -1, state: 0}}
	for len(stack) > 0 {
		it := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if it.state == 0 { // entering node
			node := it.node

			bestDepth := -1
			bestNode := -1
			val := nums[node]
			for _, v := range coprimeVals[val] {
				anc := lastSeen[v]
				if anc != -1 && depth[anc] > bestDepth {
					bestDepth = depth[anc]
					bestNode = anc
				}
			}
			ans[node] = bestNode

			// save previous and update lastSeen for current value
			prevSeen[node] = lastSeen[val]
			lastSeen[val] = node

			// push exit state
			stack = append(stack, stackItem{node: node, parent: it.parent, state: 1})

			// push children
			for _, nb := range adj[node] {
				if nb == it.parent {
					continue
				}
				depth[nb] = depth[node] + 1
				stack = append(stack, stackItem{node: nb, parent: node, state: 0})
			}
		} else { // exiting node, restore lastSeen
			node := it.node
			val := nums[node]
			lastSeen[val] = prevSeen[node]
		}
	}

	return ans
}
```

## Ruby

```ruby
def get_coprimes(nums, edges)
  n = nums.length
  graph = Array.new(n) { [] }
  edges.each do |u, v|
    graph[u] << v
    graph[v] << u
  end

  # precompute coprime table for values 1..50
  cop = Array.new(51) { Array.new(51, false) }
  (1..50).each do |i|
    (1..50).each do |j|
      cop[i][j] = i.gcd(j) == 1
    end
  end

  depth = Array.new(n, 0)
  ans = Array.new(n, -1)

  last_node = Array.new(51, -1)   # latest node index for each value on current path
  prev_val = Array.new(n, -1)     # store previous last_node for restoration

  stack = [[0, -1, 0]]            # [node, parent, state] state: 0 -> pre, 1 -> post

  while !stack.empty?
    node, parent, state = stack.pop
    if state == 0
      depth[node] = (parent == -1 ? 0 : depth[parent] + 1)

      v = nums[node]
      best_node = -1
      best_depth = -1
      (1..50).each do |val|
        next unless cop[val][v]
        anc = last_node[val]
        if anc != -1 && depth[anc] > best_depth
          best_node = anc
          best_depth = depth[anc]
        end
      end
      ans[node] = best_node

      # push post-processing marker
      stack << [node, parent, 1]

      # update last occurrence for current value and remember previous
      prev_val[node] = last_node[v]
      last_node[v] = node

      graph[node].each do |nei|
        next if nei == parent
        stack << [nei, node, 0]
      end
    else
      v = nums[node]
      last_node[v] = prev_val[node]   # restore previous occurrence
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def getCoprimes(nums: Array[Int], edges: Array[Array[Int]]): Array[Int] = {
        val n = nums.length
        // Build adjacency list
        val adj = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
        for (e <- edges) {
            val u = e(0)
            val v = e(1)
            adj(u).append(v)
            adj(v).append(u)
        }

        // GCD function
        def gcd(a: Int, b: Int): Int = {
            var x = a
            var y = b
            while (y != 0) {
                val t = x % y
                x = y
                y = t
            }
            x
        }

        // Precompute coprime lists for values 1..50
        val coprime = Array.ofDim[Array[Int]](51)
        for (i <- 1 to 50) {
            val buf = new scala.collection.mutable.ArrayBuffer[Int]()
            for (j <- 1 to 50) {
                if (gcd(i, j) == 1) buf.append(j)
            }
            coprime(i) = buf.toArray
        }

        val ans = Array.fill(n)(-1)
        val depth = new Array[Int](n)
        val lastNode = Array.fill(51)(-1)          // latest node index for each value on current path
        val savedPrev = new Array[Int](n)          // to restore lastNode when backtracking

        import scala.collection.mutable.Stack
        // Stack entries: (node, parent, visitedFlag)
        val stack = Stack[(Int, Int, Boolean)]()
        stack.push((0, -1, false))

        while (stack.nonEmpty) {
            val (node, parent, visited) = stack.pop()
            if (!visited) {
                // entering node
                val value = nums(node)

                var bestAncestor = -1
                var bestDepth = -1
                for (v <- coprime(value)) {
                    val anc = lastNode(v)
                    if (anc != -1 && depth(anc) > bestDepth) {
                        bestDepth = depth(anc)
                        bestAncestor = anc
                    }
                }
                ans(node) = bestAncestor

                // save previous state for restoration later
                savedPrev(node) = lastNode(value)

                // update structures
                if (parent != -1) depth(node) = depth(parent) + 1 else depth(node) = 0
                lastNode(value) = node

                // push exit marker
                stack.push((node, parent, true))
                // push children
                for (child <- adj(node) if child != parent) {
                    stack.push((child, node, false))
                }
            } else {
                // exiting node, restore previous lastNode entry
                val value = nums(node)
                lastNode(value) = savedPrev(node)
            }
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_coprimes(nums: Vec<i32>, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        // build adjacency list
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in edges.iter() {
            let u = e[0] as usize;
            let v = e[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }

        // gcd function
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a.abs()
        }

        // precompute coprime lists for values 1..=50
        let max_val = 50usize;
        let mut coprime: Vec<Vec<usize>> = vec![Vec::new(); max_val + 1];
        for i in 1..=max_val {
            for j in 1..=max_val {
                if gcd(i as i32, j as i32) == 1 {
                    coprime[i].push(j);
                }
            }
        }

        // last occurrence of each value on current path (-1 means none)
        let mut last_node: Vec<i32> = vec![-1; max_val + 1];
        // store previous last_node for each node to restore later
        let mut prev_of_node: Vec<i32> = vec![-2; n];
        // depth of each node
        let mut depth: Vec<i32> = vec![0; n];
        // answer array
        let mut ans: Vec<i32> = vec![-1; n];

        // iterative DFS stack: (node, parent, depth, visited_flag)
        let mut stack: Vec<(usize, usize, i32, bool)> = Vec::new();
        stack.push((0, n, 0, false)); // use n as sentinel parent for root

        while let Some((u, p, d, visited)) = stack.pop() {
            if !visited {
                depth[u] = d;
                let val = nums[u] as usize;

                // find closest coprime ancestor
                let mut best_node = -1i32;
                let mut best_depth = -1i32;
                for &w in coprime[val].iter() {
                    let anc = last_node[w];
                    if anc != -1 {
                        let anc_depth = depth[anc as usize];
                        if anc_depth > best_depth {
                            best_depth = anc_depth;
                            best_node = anc;
                        }
                    }
                }
                ans[u] = best_node;

                // save previous occurrence and update
                prev_of_node[u] = last_node[val];
                last_node[val] = u as i32;

                // push exit marker
                stack.push((u, p, d, true));
                // push children
                for &v in adj[u].iter().rev() {
                    if v != p {
                        stack.push((v, u, d + 1, false));
                    }
                }
            } else {
                // restore previous occurrence when exiting node
                let val = nums[u] as usize;
                last_node[val] = prev_of_node[u];
            }
        }

        ans
    }
}
```

## Racket

```racket
(define (get-coprimes nums edges)
  (let* ((n (length nums))
         (nums-vec (list->vector nums))
         (adj (make-vector n '()))
         (add-edge
          (lambda (u v)
            (vector-set! adj u (cons v (vector-ref adj u)))
            (vector-set! adj v (cons u (vector-ref adj v)))))
         (last (make-vector 51 -1))
         (depth (make-vector n 0))
         (ans (make-vector n -1))
         (stack '()))
    ;; build adjacency
    (for-each (lambda (e)
                (let ((u (first e)) (v (second e)))
                  (add-edge u v)))
              edges)
    ;; initial frame: node, parent, stage(0=enter,1=exit), prev-last
    (set! stack (cons (list 0 -1 0 #f) stack))
    (let loop ()
      (when (not (null? stack))
        (define frame (car stack))
        (set! stack (cdr stack))
        (define node   (first frame))
        (define parent (second frame))
        (define stage  (third frame))
        (define prev   (fourth frame))
        (if (= stage 0)
            (begin
              ;; compute answer using current last[]
              (let* ((v (vector-ref nums-vec node))
                     (best -1)
                     (bestDepth -1))
                (for ([w (in-range 1 51)])
                  (when (= (gcd v w) 1)
                    (define anc (vector-ref last w))
                    (when (>= anc 0)
                      (define d (vector-ref depth anc))
                      (when (> d bestDepth)
                        (set! best anc)
                        (set! bestDepth d)))))
                (vector-set! ans node best))
              ;; set depth
              (if (= parent -1)
                  (vector-set! depth node 0)
                  (vector-set! depth node (+ 1 (vector-ref depth parent))))
              ;; record previous occurrence for this value and update
              (define v (vector-ref nums-vec node))
              (define prev-val (vector-ref last v))
              (vector-set! last v node)
              ;; push exit frame with stored previous value
              (set! stack (cons (list node parent 1 prev-val) stack))
              ;; push children frames
              (for ([child (in-list (vector-ref adj node))])
                (when (not (= child parent))
                  (set! stack (cons (list child node 0 #f) stack)))))
            (begin
              ;; exit stage: restore last[]
              (define v (vector-ref nums-vec node))
              (vector-set! last v prev)))
        (loop)))
    ;; convert answer vector to list
    (let build ((i 0) (res '()))
      (if (= i n)
          (reverse res)
          (build (+ i 1) (cons (vector-ref ans i) res)))))
```

## Erlang

```erlang
-spec get_coprimes(Nums :: [integer()], Edges :: [[integer()]]) -> [integer()].
get_coprimes(Nums, Edges) ->
    N = length(Nums),
    NumArr = array:from_list(Nums),

    Adj0 = maps:from_list(lists:map(fun(I) -> {I, []} end, lists:seq(0, N - 1))),
    Adj = add_edges(Edges, Adj0),

    CoprimeMap = build_coprime_map(),

    EmptyStacks = erlang:make_tuple(51, []),
    AnswerArr0 = array:new(N, [{default, -1}]),

    Stack0 = [{0, -1, 0, 0}], % {Node, Parent, Depth, Stage}
    FinalAnsArr = dfs(Stack0, Adj, NumArr, CoprimeMap, EmptyStacks, AnswerArr0),

    array:to_list(FinalAnsArr).

add_edges([], Adj) -> Adj;
add_edges([[U, V] | Rest], Adj) ->
    Adj1 = maps:update_with(U,
            fun(L) -> [V | L] end,
            [V],
            Adj),
    Adj2 = maps:update_with(V,
            fun(L) -> [U | L] end,
            [U],
            Adj1),
    add_edges(Rest, Adj2).

build_coprime_map() ->
    build_coprime_map(1, erlang:make_tuple(51, [])).

build_coprime_map(51, Tuple) -> Tuple;
build_coprime_map(X, Tuple) ->
    Coprimes = [Y || Y <- lists:seq(1, 50), gcd(X, Y) =:= 1],
    NewTuple = setelement(X, Tuple, Coprimes),
    build_coprime_map(X + 1, NewTuple).

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).

dfs([], _Adj, _NumArr, _CMap, _Stacks, Ans) -> Ans;
dfs([{Node, Parent, Depth, 0} | RestStack], Adj, NumArr, CMap, Stacks, Ans) ->
    Val = array:get(Node, NumArr),
    CoprimeVals = element(Val, CMap),
    {BestNode, _BestDepth} = find_best(CoprimeVals, Stacks, -1, -1),

    NewAns = array:set(Node, BestNode, Ans),

    StackAfterExit = [{Node, Parent, Depth, 1} | RestStack],

    CurList = element(Val, Stacks),
    UpdatedCurList = [{Node, Depth} | CurList],
    NewStacks = setelement(Val, Stacks, UpdatedCurList),

    Children = maps:get(Node, Adj),
    ChildFrames = [{Child, Node, Depth + 1, 0}
                   || Child <- Children,
                      Child =/= Parent],

    NewStack = lists:foldl(fun(F, Acc) -> [F | Acc] end, StackAfterExit, ChildFrames),

    dfs(NewStack, Adj, NumArr, CMap, NewStacks, NewAns);
dfs([{Node, _Parent, _Depth, 1} | RestStack], Adj, NumArr, CMap, Stacks, Ans) ->
    Val = array:get(Node, NumArr),
    CurList = element(Val, Stacks),
    [_ | RestList] = CurList,
    NewStacks = setelement(Val, Stacks, RestList),
    dfs(RestStack, Adj, NumArr, CMap, NewStacks, Ans).

find_best([], _Stacks, BestNode, _BestDepth) -> {BestNode, -1};
find_best([V | Rest], Stacks, CurBestNode, CurBestDepth) ->
    List = element(V, Stacks),
    case List of
        [] ->
            find_best(Rest, Stacks, CurBestNode, CurBestDepth);
        [{AncNode, AncDepth} | _] ->
            if AncDepth > CurBestDepth ->
                    find_best(Rest, Stacks, AncNode, AncDepth);
               true ->
                    find_best(Rest, Stacks, CurBestNode, CurBestDepth)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_coprimes(nums :: [integer], edges :: [[integer]]) :: [integer]
  def get_coprimes(nums, edges) do
    n = length(nums)
    nums_t = List.to_tuple(nums)

    adj =
      Enum.reduce(edges, %{}, fn [u, v], acc ->
        acc
        |> Map.update(u, [v], &[v | &1])
        |> Map.update(v, [u], &[u | &1])
      end)

    coprime_arr = :array.new(51, default: [])
    coprime_arr =
      Enum.reduce(1..50, coprime_arr, fn a, arr ->
        lst = for b <- 1..50, Integer.gcd(a, b) == 1, do: b
        :array.set(a, lst, arr)
      end)

    value_stacks = %{}
    ans_arr = :array.new(n, default: -1)
    stack = [{0, -1, 0, 0}] # {node, parent, state (0 enter / 1 exit), depth}

    dfs = fn
      [], _vs, ans -> ans

      [{node, parent, state, depth} | rest], vs, ans ->
        val = elem(nums_t, node)

        if state == 0 do
          coprime_vals = :array.get(val, coprime_arr)

          {best_node, best_depth} =
            Enum.reduce(coprime_vals, {-1, -1}, fn v, acc ->
              case Map.get(vs, v, []) do
                [] -> acc
                [{d, anc} | _] ->
                  if d > elem(acc, 1), do: {anc, d}, else: acc
              end
            end)

          ans = :array.set(node, best_node, ans)
          cur_stack = Map.get(vs, val, [])
          vs2 = Map.put(vs, val, [{depth, node} | cur_stack])

          new_stack = [{node, parent, 1, depth} | rest]

          child_entries =
            Enum.reduce(Map.get(adj, node, []), new_stack, fn child, acc ->
              if child != parent do
                [{child, node, 0, depth + 1} | acc]
              else
                acc
              end
            end)

          dfs.(child_entries, vs2, ans)
        else
          cur_stack = Map.get(vs, val, [])
          new_cur = tl(cur_stack)

          vs2 =
            if new_cur == [] do
              Map.delete(vs, val)
            else
              Map.put(vs, val, new_cur)
            end

          dfs.(rest, vs2, ans)
        end
    end

    final_ans_arr = dfs.(stack, value_stacks, ans_arr)
    :array.to_list(final_ans_arr)
  end
end
```
