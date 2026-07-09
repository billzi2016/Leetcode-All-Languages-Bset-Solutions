# 3331. Find Subtree Sizes After Changes

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();
        // build original tree adjacency
        vector<vector<int>> children(n);
        for (int i = 1; i < n; ++i) {
            children[parent[i]].push_back(i);
        }

        // compute new parents after simultaneous changes
        vector<int> newParent = parent;
        vector<int> last(26, -1);               // latest node with each character on current path

        struct Frame {
            int u;
            int idx;       // next child index to process, -1 means not entered yet
            int prevLast;  // previous value of last[char] for this node
        };
        vector<Frame> stack;
        stack.reserve(n);
        stack.push_back({0, -1, -1});   // start with root

        while (!stack.empty()) {
            Frame &fr = stack.back();
            if (fr.idx == -1) {                 // entering node
                int c = s[fr.u] - 'a';
                fr.prevLast = last[c];
                last[c] = fr.u;
                fr.idx = 0;
            }
            if (fr.idx < (int)children[fr.u].size()) {
                int v = children[fr.u][fr.idx++];
                int c = s[v] - 'a';
                if (last[c] != -1) newParent[v] = last[c];
                stack.push_back({v, -1, -1});
            } else {                            // exiting node
                int c = s[fr.u] - 'a';
                last[c] = fr.prevLast;
                stack.pop_back();
            }
        }

        // build final tree using newParent
        vector<vector<int>> newChildren(n);
        for (int i = 1; i < n; ++i) {
            newChildren[newParent[i]].push_back(i);
        }

        // compute subtree sizes via post-order traversal
        vector<int> sz(n, 1);
        vector<pair<int,int>> st2;
        st2.reserve(2*n);
        st2.emplace_back(0, 0); // (node, state) state 0 = pre, 1 = post
        while (!st2.empty()) {
            auto [u, state] = st2.back();
            st2.pop_back();
            if (state == 0) {
                st2.emplace_back(u, 1);
                for (int v : newChildren[u]) st2.emplace_back(v, 0);
            } else {
                for (int v : newChildren[u]) sz[u] += sz[v];
            }
        }

        return sz;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class State {
        int node;
        int childIdx; // -1 = entering, 0 = exiting
        int prevLast;
        State(int node, int childIdx) {
            this.node = node;
            this.childIdx = childIdx;
        }
    }

    public int[] findSubtreeSizes(int[] parent, String s) {
        int n = parent.length;
        List<Integer>[] origChildren = new ArrayList[n];
        for (int i = 0; i < n; i++) origChildren[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            origChildren[parent[i]].add(i);
        }

        int[] newParent = new int[n];
        Arrays.fill(newParent, -1);
        char[] chs = s.toCharArray();

        int[] lastSeen = new int[26];
        Arrays.fill(lastSeen, -1);
        int[] prevLast = new int[n]; // store previous lastSeen for each node's character

        Deque<State> stack = new ArrayDeque<>();
        stack.push(new State(0, -1)); // start with root entering

        while (!stack.isEmpty()) {
            State cur = stack.pop();
            if (cur.childIdx == -1) { // entering node
                int idx = chs[cur.node] - 'a';
                prevLast[cur.node] = lastSeen[idx];

                if (cur.node != 0) {
                    if (lastSeen[idx] != -1) {
                        newParent[cur.node] = lastSeen[idx];
                    } else {
                        newParent[cur.node] = parent[cur.node];
                    }
                }

                // update lastSeen to current node
                lastSeen[idx] = cur.node;

                // push exiting marker
                cur.childIdx = 0;
                stack.push(cur);

                // push children (entering) in reverse order for correct processing order
                List<Integer> childs = origChildren[cur.node];
                for (int i = childs.size() - 1; i >= 0; --i) {
                    stack.push(new State(childs.get(i), -1));
                }
            } else { // exiting node, restore lastSeen
                int idx = chs[cur.node] - 'a';
                lastSeen[idx] = prevLast[cur.node];
            }
        }

        // Build final tree using newParent relationships
        List<Integer>[] finalChildren = new ArrayList[n];
        for (int i = 0; i < n; i++) finalChildren[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            int p = newParent[i];
            finalChildren[p].add(i);
        }

        // Compute subtree sizes with iterative post-order DFS
        int[] size = new int[n];
        Deque<int[]> dfsStack = new ArrayDeque<>();
        dfsStack.push(new int[]{0, 0}); // node, state (0=enter,1=exit)

        while (!dfsStack.isEmpty()) {
            int[] top = dfsStack.pop();
            int node = top[0];
            int state = top[1];
            if (state == 0) {
                dfsStack.push(new int[]{node, 1});
                for (int child : finalChildren[node]) {
                    dfsStack.push(new int[]{child, 0});
                }
            } else {
                int sz = 1;
                for (int child : finalChildren[node]) {
                    sz += size[child];
                }
                size[node] = sz;
            }
        }

        return size;
    }
}
```

## Python

```python
import sys

class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        sys.setrecursionlimit(200000)
        n = len(parent)

        # build original children adjacency
        orig_children = [[] for _ in range(n)]
        for i in range(1, n):
            orig_children[parent[i]].append(i)

        new_parent = parent[:]  # will be updated

        last = [-1] * 26  # last seen node with each character on current path

        def dfs(u):
            ci = ord(s[u]) - 97
            prev = last[ci]
            last[ci] = u
            for v in orig_children[u]:
                cvi = ord(s[v]) - 97
                anc = last[cvi]
                if anc != -1:
                    new_parent[v] = anc
                # else keep original parent (already set)
                dfs(v)
            last[ci] = prev

        dfs(0)

        # build new children adjacency based on updated parents
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            p = new_parent[i]
            new_children[p].append(i)

        ans = [0] * n

        def compute(u):
            total = 1
            for v in new_children[u]:
                total += compute(v)
            ans[u] = total
            return total

        compute(0)
        return ans
```

## Python3

```python
class Solution:
    def findSubtreeSizes(self, parent, s):
        import sys
        sys.setrecursionlimit(10**6)
        n = len(parent)
        # build original children list
        orig_children = [[] for _ in range(n)]
        for i in range(1, n):
            orig_children[parent[i]].append(i)

        new_parent = [-1] * n
        last = [-1] * 26

        def dfs(u):
            if u != 0:
                c = ord(s[u]) - 97
                anc = last[c]
                if anc != -1:
                    new_parent[u] = anc
                else:
                    new_parent[u] = parent[u]
            # update last occurrence for this node's character
            cur_c = ord(s[u]) - 97
            prev = last[cur_c]
            last[cur_c] = u
            for v in orig_children[u]:
                dfs(v)
            last[cur_c] = prev

        dfs(0)

        # build new tree children list
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            p = new_parent[i]
            new_children[p].append(i)

        ans = [0] * n

        def compute(u):
            sz = 1
            for v in new_children[u]:
                sz += compute(v)
            ans[u] = sz
            return sz

        compute(0)
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct Edge {
    int to;
    int next;
} Edge;

typedef struct Frame {
    int node;
    int state;   // 0 = enter, 1 = exit
    int prev;    // previous last occurrence for the node's character
} Frame;

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findSubtreeSizes(int* parent, int parentSize, char* s, int* returnSize) {
    int n = parentSize;
    // Build adjacency list of original tree
    Edge *origEdges = (Edge*)malloc((n - 1) * sizeof(Edge));
    int *headOrig = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) headOrig[i] = -1;
    int eidx = 0;
    for (int i = 1; i < n; ++i) {
        origEdges[eidx].to = i;
        origEdges[eidx].next = headOrig[parent[i]];
        headOrig[parent[i]] = eidx++;
    }

    // Compute new parents using DFS with last occurrence tracking
    int *newParent = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) newParent[i] = parent[i];

    int last[26];
    for (int i = 0; i < 26; ++i) last[i] = -1;

    Frame *stack = (Frame*)malloc(2 * n * sizeof(Frame));
    int top = 0;
    stack[top++] = (Frame){0, 0, -1}; // start with root entry

    while (top) {
        Frame cur = stack[--top];
        int node = cur.node;
        if (cur.state == 0) { // enter
            int ch = s[node] - 'a';
            int prev = last[ch];

            if (node != 0) {
                if (prev != -1)
                    newParent[node] = prev;
                else
                    newParent[node] = parent[node];
            }

            // push exit frame first
            stack[top++] = (Frame){node, 1, prev};

            // update last occurrence
            last[ch] = node;

            // push children entries
            for (int e = headOrig[node]; e != -1; e = origEdges[e].next) {
                int child = origEdges[e].to;
                stack[top++] = (Frame){child, 0, -1};
            }
        } else { // exit
            int ch = s[node] - 'a';
            last[ch] = cur.prev; // restore previous occurrence
        }
    }

    free(origEdges);
    free(headOrig);

    // Build adjacency list of final tree using newParent
    Edge *newEdges = (Edge*)malloc((n - 1) * sizeof(Edge));
    int *headNew = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) headNew[i] = -1;
    eidx = 0;
    for (int i = 1; i < n; ++i) {
        int p = newParent[i];
        newEdges[eidx].to = i;
        newEdges[eidx].next = headNew[p];
        headNew[p] = eidx++;
    }

    // Compute subtree sizes in final tree
    int *sz = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) sz[i] = 1;

    top = 0;
    stack[top++] = (Frame){0, 0, -1};

    while (top) {
        Frame cur = stack[--top];
        int node = cur.node;
        if (cur.state == 0) { // enter
            // push exit frame first
            stack[top++] = (Frame){node, 1, -1};
            // push children entries
            for (int e = headNew[node]; e != -1; e = newEdges[e].next) {
                int child = newEdges[e].to;
                stack[top++] = (Frame){child, 0, -1};
            }
        } else { // exit: accumulate children's sizes
            for (int e = headNew[node]; e != -1; e = newEdges[e].next) {
                int child = newEdges[e].to;
                sz[node] += sz[child];
            }
        }
    }

    free(newEdges);
    free(headNew);
    free(newParent);
    free(stack);

    *returnSize = n;
    return sz;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] FindSubtreeSizes(int[] parent, string s) {
        int n = parent.Length;
        var children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        for (int i = 1; i < n; i++) {
            children[parent[i]].Add(i);
        }

        int[] newParent = new int[n];
        newParent[0] = -1;
        int[] lastSeen = new int[26];
        for (int i = 0; i < 26; i++) lastSeen[i] = -1;

        var stack = new Stack<(int node, int stage)>();
        var restoreStack = new Stack<(int ch, int prev)>();
        stack.Push((0, 0));

        while (stack.Count > 0) {
            var (v, stage) = stack.Pop();
            if (stage == 0) {
                if (v != 0) {
                    int c = s[v] - 'a';
                    int anc = lastSeen[c];
                    newParent[v] = anc != -1 ? anc : parent[v];
                }
                stack.Push((v, 1));
                int ch = s[v] - 'a';
                restoreStack.Push((ch, lastSeen[ch]));
                lastSeen[ch] = v;
                var childs = children[v];
                for (int i = childs.Count - 1; i >= 0; i--) {
                    stack.Push((childs[i], 0));
                }
            } else {
                var rec = restoreStack.Pop();
                lastSeen[rec.ch] = rec.prev;
            }
        }

        var newChildren = new List<int>[n];
        for (int i = 0; i < n; i++) newChildren[i] = new List<int>();
        for (int i = 1; i < n; i++) {
            int p = newParent[i];
            newChildren[p].Add(i);
        }

        int[] size = new int[n];
        var stack2 = new Stack<(int node, bool visited)>();
        stack2.Push((0, false));
        while (stack2.Count > 0) {
            var (v, visited) = stack2.Pop();
            if (!visited) {
                stack2.Push((v, true));
                foreach (var child in newChildren[v]) {
                    stack2.Push((child, false));
                }
            } else {
                int sz = 1;
                foreach (var child in newChildren[v]) {
                    sz += size[child];
                }
                size[v] = sz;
            }
        }

        return size;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} parent
 * @param {string} s
 * @return {number[]}
 */
var findSubtreeSizes = function(parent, s) {
    const n = parent.length;
    // build original tree adjacency
    const origChildren = Array.from({length: n}, () => []);
    for (let i = 1; i < n; ++i) {
        origChildren[parent[i]].push(i);
    }

    const newParent = parent.slice();          // will hold final parents
    const lastSeen = new Array(26).fill(-1);   // latest node with each char on current path
    const prevSeen = new Array(n);             // store previous lastSeen for backtrack

    // DFS on original tree to compute newParent using nearest same-char ancestor
    const stack = [[0, 0]]; // [node, state] state 0=enter,1=exit
    while (stack.length) {
        const [node, state] = stack.pop();
        if (state === 0) {
            // determine new parent for non-root nodes
            if (node !== 0) {
                const cIdx = s.charCodeAt(node) - 97;
                if (lastSeen[cIdx] !== -1) {
                    newParent[node] = lastSeen[cIdx];
                }
            }

            // record previous and update lastSeen for this node's character
            const cNode = s.charCodeAt(node) - 97;
            prevSeen[node] = lastSeen[cNode];
            lastSeen[cNode] = node;

            // push exit marker
            stack.push([node, 1]);

            // traverse children
            const childs = origChildren[node];
            for (let i = childs.length - 1; i >= 0; --i) {
                stack.push([childs[i], 0]);
            }
        } else {
            // backtrack: restore previous lastSeen
            const cNode = s.charCodeAt(node) - 97;
            lastSeen[cNode] = prevSeen[node];
        }
    }

    // build final tree adjacency using newParent
    const finalChildren = Array.from({length: n}, () => []);
    for (let i = 1; i < n; ++i) {
        finalChildren[newParent[i]].push(i);
    }

    // compute subtree sizes on final tree
    const size = new Array(n).fill(1);
    const stack2 = [[0, 0]];
    while (stack2.length) {
        const [node, state] = stack2.pop();
        if (state === 0) {
            stack2.push([node, 1]);
            const childs = finalChildren[node];
            for (let i = childs.length - 1; i >= 0; --i) {
                stack2.push([childs[i], 0]);
            }
        } else {
            let sum = 1;
            const childs = finalChildren[node];
            for (const ch of childs) sum += size[ch];
            size[node] = sum;
        }
    }

    return size;
};
```

## Typescript

```typescript
function findSubtreeSizes(parent: number[], s: string): number[] {
    const n = parent.length;
    const origAdj: number[][] = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; ++i) {
        origAdj[parent[i]].push(i);
    }

    const newAdj: number[][] = Array.from({ length: n }, () => []);

    // stack that keeps the latest node index for each character on current path
    const charStack = new Int32Array(26).fill(-1);
    const rootCharIdx = s.charCodeAt(0) - 97;
    charStack[rootCharIdx] = 0;

    interface Entry {
        node: number;
        idx: number;   // next child index to process
        prev: number;  // previous value of charStack for this node's character
    }

    const stack: Entry[] = [{ node: 0, idx: 0, prev: -1 }];

    while (stack.length) {
        const top = stack[stack.length - 1];
        if (top.idx < origAdj[top.node].length) {
            const child = origAdj[top.node][top.idx++];
            const cIdx = s.charCodeAt(child) - 97;
            const anc = charStack[cIdx];
            const newParent = anc !== -1 ? anc : parent[child];
            newAdj[newParent].push(child);

            const prev = charStack[cIdx];
            charStack[cIdx] = child;
            stack.push({ node: child, idx: 0, prev });
        } else {
            // backtrack: restore previous character occurrence
            const cIdx = s.charCodeAt(top.node) - 97;
            charStack[cIdx] = top.prev;
            stack.pop();
        }
    }

    // compute subtree sizes on the new tree
    const size = new Int32Array(n);
    const order: number[] = [];
    const dfsStack: number[] = [0];
    while (dfsStack.length) {
        const node = dfsStack.pop()!;
        order.push(node);
        for (const ch of newAdj[node]) dfsStack.push(ch);
    }
    for (let i = order.length - 1; i >= 0; --i) {
        const node = order[i];
        let sz = 1;
        for (const ch of newAdj[node]) sz += size[ch];
        size[node] = sz;
    }

    return Array.from(size);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $parent
     * @param String $s
     * @return Integer[]
     */
    function findSubtreeSizes($parent, $s) {
        $n = count($parent);
        // build original children list
        $children = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) {
            $p = $parent[$i];
            $children[$p][] = $i;
        }

        // arrays for processing
        $newParent = $parent;
        $lastPos = array_fill(0, 26, -1);
        $savedPrev = array_fill(0, $n, -1);

        // iterative DFS to determine new parents
        $stack = [];
        $stack[] = [0, 0]; // node, state (0=enter,1=exit)

        while (!empty($stack)) {
            [$u, $state] = array_pop($stack);
            if ($state === 0) {
                $cIdx = ord($s[$u]) - 97;
                if ($lastPos[$cIdx] != -1) {
                    $newParent[$u] = $lastPos[$cIdx];
                }
                $savedPrev[$u] = $lastPos[$cIdx];
                $lastPos[$cIdx] = $u;

                // push exit state
                $stack[] = [$u, 1];
                // push children for entry
                foreach ($children[$u] as $v) {
                    $stack[] = [$v, 0];
                }
            } else {
                $cIdx = ord($s[$u]) - 97;
                $lastPos[$cIdx] = $savedPrev[$u];
            }
        }

        // build new children list based on newParent
        $newChildren = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) {
            $p = $newParent[$i];
            if ($p != -1) {
                $newChildren[$p][] = $i;
            }
        }

        // compute subtree sizes with post-order traversal
        $size = array_fill(0, $n, 1);
        $stack = [];
        $stack[] = [0, 0]; // node, visited flag (0=first time)

        while (!empty($stack)) {
            [$u, $visited] = array_pop($stack);
            if ($visited === 0) {
                $stack[] = [$u, 1];
                foreach ($newChildren[$u] as $v) {
                    $stack[] = [$v, 0];
                }
            } else {
                foreach ($newChildren[$u] as $v) {
                    $size[$u] += $size[$v];
                }
            }
        }

        return $size;
    }
}
```

## Swift

```swift
class Solution {
    func findSubtreeSizes(_ parent: [Int], _ s: String) -> [Int] {
        let n = parent.count
        // Convert characters to indices 0..25
        let charIndices = s.unicodeScalars.map { Int($0.value - 97) }
        
        // Build original children adjacency list
        var children = [[Int]](repeating: [], count: n)
        if n > 1 {
            for i in 1..<n {
                let p = parent[i]
                children[p].append(i)
            }
        }
        
        // Compute new parents after simultaneous changes
        var newParent = parent
        var lastSeen = [Int?](repeating: nil, count: 26)
        
        struct Frame {
            var node: Int
            var childIdx: Int
            var prevAnc: Int?
        }
        
        // Initialize with root
        let rootChar = charIndices[0]
        let rootPrev = lastSeen[rootChar]   // always nil
        lastSeen[rootChar] = 0
        var stack = [Frame]()
        stack.append(Frame(node: 0, childIdx: 0, prevAnc: rootPrev))
        
        while !stack.isEmpty {
            var top = stack[stack.count - 1]
            if top.childIdx < children[top.node].count {
                let child = children[top.node][top.childIdx]
                // advance iterator
                stack[stack.count - 1].childIdx += 1
                
                // Determine new parent for child
                let cChar = charIndices[child]
                if let anc = lastSeen[cChar] {
                    newParent[child] = anc!
                }
                
                // Push child frame with saved previous ancestor
                let prev = lastSeen[cChar]
                lastSeen[cChar] = child
                stack.append(Frame(node: child, childIdx: 0, prevAnc: prev))
            } else {
                // Exiting node, restore lastSeen for its character
                let cChar = charIndices[top.node]
                if let prev = top.prevAnc {
                    lastSeen[cChar] = prev
                } else {
                    lastSeen[cChar] = nil
                }
                stack.removeLast()
            }
        }
        
        // Build final tree adjacency list using newParent
        var finalChildren = [[Int]](repeating: [], count: n)
        if n > 1 {
            for i in 1..<n {
                let p = newParent[i]
                finalChildren[p].append(i)
            }
        }
        
        // Compute subtree sizes with post-order traversal (iterative)
        var order = [Int]()
        var dfsStack = [0]
        while !dfsStack.isEmpty {
            let node = dfsStack.removeLast()
            order.append(node)
            for child in finalChildren[node] {
                dfsStack.append(child)
            }
        }
        
        var size = [Int](repeating: 1, count: n) // each node counts itself
        for node in order.reversed() {
            for child in finalChildren[node] {
                size[node] += size[child]
            }
        }
        return size
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun findSubtreeSizes(parent: IntArray, s: String): IntArray {
        val n = parent.size
        // Build original children adjacency list
        val origChildren = Array(n) { mutableListOf<Int>() }
        for (i in 1 until n) {
            origChildren[parent[i]].add(i)
        }

        // Arrays to store new parents and previous lastSeen per node
        val newParent = parent.clone()
        val prevSame = IntArray(n)

        // last seen node index for each character, -1 if none
        val lastSeen = IntArray(26) { -1 }

        // Iterative DFS on original tree to determine new parents
        val stack = ArrayDeque<Int>()
        // encode (node << 1) | state where state 0=enter,1=exit
        stack.push(0 shl 1) // enter root

        while (stack.isNotEmpty()) {
            val encoded = stack.pop()
            val node = encoded ushr 1
            val exit = (encoded and 1) == 1
            if (!exit) {
                // entering node
                val cIdx = s[node] - 'a'
                prevSame[node] = lastSeen[cIdx]
                if (node != 0 && lastSeen[cIdx] != -1) {
                    newParent[node] = lastSeen[cIdx]
                }
                // update last seen to current node
                lastSeen[cIdx] = node

                // push exit state
                stack.push((node shl 1) or 1)
                // push children (enter states)
                for (child in origChildren[node]) {
                    stack.push(child shl 1)
                }
            } else {
                // exiting node, restore lastSeen
                val cIdx = s[node] - 'a'
                lastSeen[cIdx] = prevSame[node]
            }
        }

        // Build new children adjacency list after reattachment
        val newChildren = Array(n) { mutableListOf<Int>() }
        for (i in 1 until n) {
            val p = newParent[i]
            newChildren[p].add(i)
        }

        // Compute subtree sizes with post-order traversal
        val size = IntArray(n) { 1 }
        stack.clear()
        stack.push(0 shl 1) // enter root again

        while (stack.isNotEmpty()) {
            val encoded = stack.pop()
            val node = encoded ushr 1
            val exit = (encoded and 1) == 1
            if (!exit) {
                // entering
                stack.push((node shl 1) or 1)
                for (child in newChildren[node]) {
                    stack.push(child shl 1)
                }
            } else {
                var sum = 1
                for (child in newChildren[node]) {
                    sum += size[child]
                }
                size[node] = sum
            }
        }

        return size
    }
}
```

## Dart

```dart
class Solution {
  List<int> findSubtreeSizes(List<int> parent, String s) {
    int n = parent.length;
    // Build original children adjacency list
    List<List<int>> children = List.generate(n, (_) => []);
    for (int i = 1; i < n; i++) {
      children[parent[i]].add(i);
    }

    // First DFS to compute new parents after changes
    List<int> newParent = List.filled(n, -1);
    List<int> lastSeen = List.filled(26, -1);
    List<int> savedPrev = List.filled(n, -1);

    List<List<dynamic>> stack = [];
    stack.add([0, false]); // node, visited flag

    while (stack.isNotEmpty) {
      var cur = stack.removeLast();
      int node = cur[0] as int;
      bool visited = cur[1] as bool;

      if (!visited) {
        int charIdx = s.codeUnitAt(node) - 97;
        int prev = lastSeen[charIdx];
        savedPrev[node] = prev;
        if (node != 0) {
          newParent[node] = (prev == -1) ? parent[node] : prev;
        } else {
          newParent[node] = -1;
        }
        lastSeen[charIdx] = node;

        // push exit marker
        stack.add([node, true]);
        // push children for entering
        List<int> childs = children[node];
        for (int i = childs.length - 1; i >= 0; i--) {
          stack.add([childs[i], false]);
        }
      } else {
        int charIdx = s.codeUnitAt(node) - 97;
        lastSeen[charIdx] = savedPrev[node];
      }
    }

    // Build new children adjacency list based on newParent
    List<List<int>> newChildren = List.generate(n, (_) => []);
    for (int i = 1; i < n; i++) {
      int p = newParent[i];
      newChildren[p].add(i);
    }

    // Second DFS to compute subtree sizes in the final tree
    List<int> size = List.filled(n, 0);
    stack.clear();
    stack.add([0, false]);

    while (stack.isNotEmpty) {
      var cur = stack.removeLast();
      int node = cur[0] as int;
      bool visited = cur[1] as bool;

      if (!visited) {
        // post-order: first push exit marker then children
        stack.add([node, true]);
        List<int> childs = newChildren[node];
        for (int i = childs.length - 1; i >= 0; i--) {
          stack.add([childs[i], false]);
        }
      } else {
        int total = 1;
        for (int child in newChildren[node]) {
          total += size[child];
        }
        size[node] = total;
      }
    }

    return size;
  }
}
```

## Golang

```go
func findSubtreeSizes(parent []int, s string) []int {
    n := len(parent)
    // original tree children
    origChildren := make([][]int, n)
    for i := 1; i < n; i++ {
        p := parent[i]
        origChildren[p] = append(origChildren[p], i)
    }

    newParent := make([]int, n)
    copy(newParent, parent)

    lastSeen := make([]int, 26)
    for i := 0; i < 26; i++ {
        lastSeen[i] = -1
    }

    var dfs func(int)
    dfs = func(u int) {
        cIdx := s[u] - 'a'
        saved := lastSeen[cIdx]
        lastSeen[cIdx] = u

        // determine new parent for each child based on current ancestors
        for _, v := range origChildren[u] {
            cc := s[v] - 'a'
            if lastSeen[cc] != -1 {
                newParent[v] = lastSeen[cc]
            } else {
                newParent[v] = parent[v]
            }
        }

        // recurse to children in original tree
        for _, v := range origChildren[u] {
            dfs(v)
        }

        lastSeen[cIdx] = saved
    }

    dfs(0)

    // build final tree adjacency
    finalChildren := make([][]int, n)
    for i := 1; i < n; i++ {
        p := newParent[i]
        finalChildren[p] = append(finalChildren[p], i)
    }

    ans := make([]int, n)
    var compute func(int) int
    compute = func(u int) int {
        sz := 1
        for _, v := range finalChildren[u] {
            sz += compute(v)
        }
        ans[u] = sz
        return sz
    }
    compute(0)

    return ans
}
```

## Ruby

```ruby
def find_subtree_sizes(parent, s)
  n = parent.length
  children = Array.new(n) { [] }
  (1...n).each do |i|
    p = parent[i]
    children[p] << i
  end

  new_parent = Array.new(n, -1)
  new_parent[0] = -1

  last = Array.new(26, nil)

  stack = []
  stack << [0, true, nil] # node, entering?, previous_last_for_node_char

  while !stack.empty?
    node, entering, prev = stack.pop
    if entering
      char_idx = s.getbyte(node) - 97
      prev_last = last[char_idx]
      # schedule exit to restore
      stack << [node, false, prev_last]

      # update current last
      last[char_idx] = node

      # process children
      children[node].reverse_each do |child|
        cidx = s.getbyte(child) - 97
        new_parent[child] = last[cidx] ? last[cidx] : node
        stack << [child, true, nil]
      end
    else
      char_idx = s.getbyte(node) - 97
      last[char_idx] = prev
    end
  end

  final_children = Array.new(n) { [] }
  (1...n).each do |i|
    p = new_parent[i]
    final_children[p] << i
  end

  ans = Array.new(n, 0)
  stack = [[0, false]]
  while !stack.empty?
    node, visited = stack.pop
    if visited
      size = 1
      final_children[node].each { |ch| size += ans[ch] }
      ans[node] = size
    else
      stack << [node, true]
      final_children[node].reverse_each { |ch| stack << [ch, false] }
    end
  end

  ans
end
```

## Scala

```scala
import scala.collection.mutable.{ArrayBuffer, ArrayDeque}

object Solution {
  def findSubtreeSizes(parent: Array[Int], s: String): Array[Int] = {
    val n = parent.length
    // build original children adjacency list
    val origChildren = Array.fill(n)(new ArrayBuffer[Int]())
    for (i <- 1 until n) {
      origChildren(parent(i)).append(i)
    }

    val newParent = parent.clone()
    val lastSeen = Array.fill(26)(-1)
    val prevChar = Array.fill(n)(-1)

    // iterative DFS to compute new parents
    val stack = new ArrayDeque[(Int, Int)]() // (node, state) 0=enter,1=exit
    stack.push((0, 0))
    while (stack.nonEmpty) {
      val (u, state) = stack.pop()
      if (state == 0) {
        // entering node u
        val cIdx = s.charAt(u) - 'a'
        prevChar(u) = lastSeen(cIdx)
        lastSeen(cIdx) = u

        // push exit marker
        stack.push((u, 1))

        // process children in reverse order for correct DFS order
        val childs = origChildren(u)
        var i = childs.length - 1
        while (i >= 0) {
          val v = childs(i)
          val cvIdx = s.charAt(v) - 'a'
          val anc = lastSeen(cvIdx)
          if (anc != -1) newParent(v) = anc else newParent(v) = parent(v)
          stack.push((v, 0))
          i -= 1
        }
      } else {
        // exiting node u, restore lastSeen
        val cIdx = s.charAt(u) - 'a'
        lastSeen(cIdx) = prevChar(u)
      }
    }

    // build final children adjacency list using newParent
    val finalChildren = Array.fill(n)(new ArrayBuffer[Int]())
    for (i <- 1 until n) {
      val p = newParent(i)
      if (p != -1) finalChildren(p).append(i)
    }

    // compute subtree sizes with post-order traversal
    val ans = Array.fill(n)(0)
    val stack2 = new ArrayDeque[(Int, Boolean)]()
    stack2.push((0, false))
    while (stack2.nonEmpty) {
      val (u, visited) = stack2.pop()
      if (!visited) {
        stack2.push((u, true))
        for (v <- finalChildren(u)) {
          stack2.push((v, false))
        }
      } else {
        var sz = 1
        for (v <- finalChildren(u)) {
          sz += ans(v)
        }
        ans(u) = sz
      }
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_subtree_sizes(parent: Vec<i32>, s: String) -> Vec<i32> {
        let n = parent.len();
        let bytes = s.as_bytes();

        // Build original adjacency list
        let mut orig_adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for i in 1..n {
            let p = parent[i] as usize;
            orig_adj[p].push(i);
        }

        // Arrays to store new parents and previous same-char ancestor
        let mut new_parent: Vec<usize> = vec![0; n];
        let mut prev_same: Vec<Option<usize>> = vec![None; n];

        // last occurrence of each character on current path
        let mut last: [Option<usize>; 26] = [None; 26];

        // Stack for DFS on original tree: (node, state) where state 0=enter,1=exit
        let mut stack: Vec<(usize, u8)> = Vec::with_capacity(2 * n);
        stack.push((0, 0));

        while let Some((node, state)) = stack.pop() {
            if state == 0 {
                // entering node
                let ci = (bytes[node] - b'a') as usize;
                prev_same[node] = last[ci];

                if node != 0 {
                    if let Some(prev) = last[ci] {
                        new_parent[node] = prev;
                    } else {
                        new_parent[node] = parent[node] as usize;
                    }
                }

                // update last occurrence
                last[ci] = Some(node);

                // push exit state
                stack.push((node, 1));
                // push children for entry
                for &child in orig_adj[node].iter().rev() {
                    stack.push((child, 0));
                }
            } else {
                // exiting node, restore last occurrence
                let ci = (bytes[node] - b'a') as usize;
                last[ci] = prev_same[node];
            }
        }

        // Build final adjacency list using new_parent
        let mut final_adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for i in 1..n {
            let p = new_parent[i];
            final_adj[p].push(i);
        }

        // Compute subtree sizes with post-order traversal
        let mut ans: Vec<i32> = vec![0; n];
        let mut stack2: Vec<(usize, bool)> = Vec::with_capacity(2 * n);
        stack2.push((0, false));

        while let Some((node, visited)) = stack2.pop() {
            if !visited {
                // first time: push after children
                stack2.push((node, true));
                for &child in final_adj[node].iter().rev() {
                    stack2.push((child, false));
                }
            } else {
                let mut size = 1i32;
                for &child in final_adj[node].iter() {
                    size += ans[child];
                }
                ans[node] = size;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (find-subtree-sizes parent s)
  (-> (listof exact-integer?) string? (listof exact-integer?))
  (let* ((n (length parent))
         (parent-vec (list->vector parent))
         ;; original children adjacency
         (orig-children (make-vector n '()))
         (new-parent (make-vector n -1))
         (last-occurrence (make-vector 26 -1)))
    ;; build original adjacency list
    (for ([i (in-range 1 n)])
      (let ((p (vector-ref parent-vec i)))
        (vector-set! orig-children p (cons i (vector-ref orig-children p)))))
    ;; helper to get char index 0..25
    (define (char-index ch)
      (- (char->integer ch) (char->integer #\a)))
    ;; first DFS: compute new parents using last-occurrence stack simulation
    (let ((stack (list (list 0 #f)))) ; each frame: (node visited? [prev])
      (let loop ()
        (when (not (null? stack))
          (define frame (car stack))
          (set! stack (cdr stack))
          (define node (first frame))
          (define visited? (second frame))
          (if (not visited?)
              (begin
                ;; compute new parent for non‑root nodes
                (when (> node 0)
                  (let* ((cidx (char-index (string-ref s node)))
                         (anc (vector-ref last-occurrence cidx))
                         (orig-p (vector-ref parent-vec node)))
                    (if (= anc -1)
                        (vector-set! new-parent node orig-p)
                        (vector-set! new-parent node anc))))
                ;; push exit marker with previous occurrence to restore later
                (let* ((cidx (char-index (string-ref s node)))
                       (prev (vector-ref last-occurrence cidx))
                       (exit-frame (list node #t prev)))
                  (set! stack (cons exit-frame stack))
                  ;; update last occurrence for this character
                  (vector-set! last-occurrence cidx node)
                  ;; push children entries
                  (for ([child (in-list (vector-ref orig-children node))])
                    (set! stack (cons (list child #f) stack)))))
              ;; exit: restore previous occurrence
              (let ((prev (third frame))
                    (cidx (char-index (string-ref s node))))
                (vector-set! last-occurrence cidx prev)))
          (loop))))
    ;; build new adjacency list from new-parent
    (define new-children (make-vector n '()))
    (for ([i (in-range 1 n)])
      (let ((p (vector-ref new-parent i)))
        (vector-set! new-children p (cons i (vector-ref new-children p)))))
    ;; second DFS: compute subtree sizes
    (define sizes (make-vector n 0))
    (let ((stack (list (list 0 #f)))) ; visited flag only
      (let loop ()
        (when (not (null? stack))
          (define frame (car stack))
          (set! stack (cdr stack))
          (define node (first frame))
          (define visited? (second frame))
          (if (not visited?)
              (begin
                ;; push exit marker then children
                (set! stack (cons (list node #t) stack))
                (for ([child (in-list (vector-ref new-children node))])
                  (set! stack (cons (list child #f) stack))))
              (let ((total 1))
                (for ([child (in-list (vector-ref new-children node))])
                  (set! total (+ total (vector-ref sizes child))))
                (vector-set! sizes node total)))
          (loop))))
    ;; convert vector to list
    (let loop ((i 0) (acc '()))
      (if (= i n)
          (reverse acc)
          (loop (+ i 1) (cons (vector-ref sizes i) acc)))))
```

## Erlang

```erlang
-module(solution).
-export([find_subtree_sizes/2]).

-spec find_subtree_sizes(Parent :: [integer()], S :: unicode:unicode_binary()) -> [integer()].
find_subtree_sizes(Parent, S) ->
    N = length(Parent),
    ParentTuple = list_to_tuple(Parent),

    % build original children map
    ChildrenMap = build_children_map(ParentTuple, 1, N-1, #{}),

    % initial last occurrence tuple (-1 for each letter)
    Last0 = init_last(),

    % compute new parent for every node (except root)
    NewParentsMap = dfs_new_parent(0, ParentTuple, ChildrenMap, S, Last0, #{}),

    % build children map of the final tree
    NewChildrenMap = build_children_from_parents(NewParentsMap, 1, N-1, #{}),

    % compute subtree sizes on the final tree
    {_, SizesMap} = compute_sizes(0, NewChildrenMap, #{}),

    % produce result list in order 0..N-1
    lists:map(fun(I) -> maps:get(I, SizesMap) end,
              lists:seq(0, N-1)).

%% ------------------------------------------------------------------
%% Helpers
%% ------------------------------------------------------------------

init_last() ->
    list_to_tuple(lists:duplicate(26, -1)).

build_children_map(_ParentTuple, I, Max, Map) when I > Max -> Map;
build_children_map(ParentTuple, I, Max, Map) ->
    P = element(I+1, ParentTuple),
    UpdatedMap = maps:update_with(P,
                                 fun(L) -> [I|L] end,
                                 [I],
                                 Map),
    build_children_map(ParentTuple, I+1, Max, UpdatedMap).

build_children_from_parents(_ParentsMap, I, Max, Map) when I > Max -> Map;
build_children_from_parents(ParentsMap, I, Max, Map) ->
    P = maps:get(I, ParentsMap),
    UpdatedMap = maps:update_with(P,
                                 fun(L) -> [I|L] end,
                                 [I],
                                 Map),
    build_children_from_parents(ParentsMap, I+1, Max, UpdatedMap).

dfs_new_parent(Node, ParentTuple, ChildrenMap, S, Last, AccMap) ->
    ChildList = maps:get(Node, ChildrenMap, []),
    process_children(ChildList, ParentTuple, ChildrenMap, S, Last, AccMap).

process_children([], _ParentTuple, _ChildrenMap, _S, _Last, AccMap) -> AccMap;
process_children([C|Rest], ParentTuple, ChildrenMap, S, Last, AccMap0) ->
    CharCode = binary:at(S, C),
    Idx = CharCode - $a,
    PrevAnc = element(Idx+1, Last),
    NewParent = case PrevAnc of
                    -1 -> element(C+1, ParentTuple);
                    _  -> PrevAnc
                end,
    AccMap1 = maps:put(C, NewParent, AccMap0),

    % update last occurrence for this character while recursing into its subtree
    LastChild = setelement(Idx+1, Last, C),
    AccMap2 = dfs_new_parent(C, ParentTuple, ChildrenMap, S, LastChild, AccMap1),

    process_children(Rest, ParentTuple, ChildrenMap, S, Last, AccMap2).

compute_sizes(Node, ChildrenMap, Acc) ->
    ChildList = maps:get(Node, ChildrenMap, []),
    {Sum, Acc1} = lists:foldl(fun(Ch,{Tot,M}) ->
                                   {SizeCh, M2} = compute_sizes(Ch, ChildrenMap, M),
                                   {Tot + SizeCh, M2}
                               end,
                               {0, Acc},
                               ChildList),
    Size = Sum + 1,
    {Size, maps:put(Node, Size, Acc1)}.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_subtree_sizes(parent :: [integer], s :: String.t) :: [integer]
  def find_subtree_sizes(parent, s) do
    n = length(parent)

    # original children map
    orig_children = build_children_map(parent)

    # character array
    s_arr = :array.from_list(String.to_charlist(s))

    # compute new parents after changes
    {new_parent_arr, _} =
      compute_new_parents(
        [{0, :enter, nil}],
        orig_children,
        s_arr,
        :array.from_list(parent),
        %{}
      )

    # build final children map from new_parent_arr
    final_children = build_final_children(new_parent_arr, n)

    # compute subtree sizes on final tree
    sizes_arr = compute_subtree_sizes(final_children, n)
    :array.to_list(sizes_arr)
  end

  defp build_children_map(parent) do
    Enum.reduce(Enum.with_index(parent), %{}, fn {p, i}, acc ->
      if p != -1 do
        Map.update(acc, p, [i], &[i | &1])
      else
        acc
      end
    end)
  end

  defp compute_new_parents(stack, children_map, s_arr, new_parent_arr, last_map) do
    case stack do
      [] ->
        {new_parent_arr, last_map}

      [{node, :exit, prev} | rest] ->
        c = :array.get(node, s_arr) - ?a

        last_map2 =
          if prev == -1 do
            Map.delete(last_map, c)
          else
            Map.put(last_map, c, prev)
          end

        compute_new_parents(rest, children_map, s_arr, new_parent_arr, last_map2)

      [{node, :enter, _} | rest] ->
        c = :array.get(node, s_arr) - ?a
        prev = Map.get(last_map, c, -1)
        last_map2 = Map.put(last_map, c, node)

        # push exit marker first
        stack2 = [{node, :exit, prev} | rest]

        children = Map.get(children_map, node, [])

        {new_parent_arr2, stack3} =
          Enum.reduce(Enum.reverse(children), {new_parent_arr, stack2}, fn child,
                                                                          {np_arr, stk} ->
            child_c = :array.get(child, s_arr) - ?a
            anc = Map.get(last_map2, child_c, -1)

            np_arr2 =
              if anc != -1 do
                :array.set(child, anc, np_arr)
              else
                np_arr
              end

            {np_arr2, [{child, :enter, nil} | stk]}
          end)

        compute_new_parents(stack3, children_map, s_arr, new_parent_arr2, last_map2)
    end
  end

  defp build_final_children(new_parent_arr, n) do
    Enum.reduce(0..(n - 1), %{}, fn i, acc ->
      p = :array.get(i, new_parent_arr)

      if p != -1 do
        Map.update(acc, p, [i], &[i | &1])
      else
        acc
      end
    end)
  end

  defp compute_subtree_sizes(children_map, n) do
    sizes = :array.new(n, default: 0)
    process_stack([{0, false}], children_map, sizes)
  end

  defp process_stack([], _children_map, sizes), do: sizes

  # first time we see the node: push visited marker and its children
  defp process_stack([{node, false} | rest], children_map, sizes) do
    child_list = Map.get(children_map, node, [])

    stack2 =
      Enum.reduce(Enum.reverse(child_list), [{node, true} | rest], fn c, acc ->
        [{c, false} | acc]
      end)

    process_stack(stack2, children_map, sizes)
  end

  # visited marker: compute size from children's sizes
  defp process_stack([{node, true} | rest}, children_map, sizes) do
    child_list = Map.get(children_map, node, [])

    total =
      Enum.reduce(child_list, 1, fn c, acc ->
        acc + :array.get(c, sizes)
      end)

    sizes2 = :array.set(node, total, sizes)
    process_stack(rest, children_map, sizes2)
  end
end
```
