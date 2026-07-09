# 3327. Check if DFS Strings Are Palindromes

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<bool> findAnswer(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; ++i) {
            children[parent[i]].push_back(i);
        }

        // Euler tour with entry and exit
        vector<int> L(n), R(n);
        vector<int> euler;
        euler.reserve(2 * n);
        stack<pair<int,int>> st;
        st.emplace(0, 0);
        while (!st.empty()) {
            int v = st.top().first;
            int &idx = st.top().second;
            if (idx == 0) {               // entry
                L[v] = euler.size();
                euler.push_back(v);
            }
            if (idx < (int)children[v].size()) {
                int child = children[v][idx];
                ++idx;
                st.emplace(child, 0);
            } else {                      // exit
                R[v] = euler.size();
                euler.push_back(v);
                st.pop();
            }
        }

        int m = euler.size(); // 2*n
        vector<char> chars(m);
        for (int i = 0; i < m; ++i) chars[i] = s[euler[i]];

        // Manacher's algorithm for even length palindromes
        vector<int> d2(m, 0);
        int l = 0, r = -1;
        for (int i = 0; i < m; ++i) {
            int k = (i > r) ? 0 : min(d2[l + r - i + 1], r - i + 1);
            while (i - k - 1 >= 0 && i + k < m && chars[i - k - 1] == chars[i + k]) ++k;
            d2[i] = k;
            if (i + k - 1 > r) {
                l = i - k;
                r = i + k - 1;
            }
        }

        vector<bool> ans(n);
        for (int v = 0; v < n; ++v) {
            int len = R[v] - L[v] + 1;                 // even length
            int mid = (L[v] + R[v] + 1) / 2;           // center index for even palindrome
            ans[v] = (d2[mid] * 2 >= len);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public boolean[] findAnswer(int[] parent, String s) {
        int n = parent.length;
        List<Integer>[] children = new ArrayList[n];
        for (int i = 0; i < n; i++) children[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            children[parent[i]].add(i);
        }

        int[] tin = new int[n];
        int[] tout = new int[n];
        int[] order = new int[n];
        int pos = 0;

        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        while (!stack.isEmpty()) {
            int v = stack.pop();
            if (v >= 0) {
                tin[v] = pos;
                order[pos++] = v;
                stack.push(~v); // marker for exit
                List<Integer> childs = children[v];
                for (int i = childs.size() - 1; i >= 0; --i) {
                    stack.push(childs.get(i));
                }
            } else {
                int node = ~v;
                tout[node] = pos - 1;
            }
        }

        char[] seq = new char[n];
        for (int i = 0; i < n; i++) {
            seq[i] = s.charAt(order[i]);
        }

        // Manacher's algorithm
        int[] d1 = new int[n];
        int l = 0, r = -1;
        for (int i = 0; i < n; i++) {
            int k = (i > r) ? 1 : Math.min(d1[l + r - i], r - i + 1);
            while (i - k >= 0 && i + k < n && seq[i - k] == seq[i + k]) k++;
            d1[i] = k;
            if (i + k - 1 > r) {
                l = i - k + 1;
                r = i + k - 1;
            }
        }

        int[] d2 = new int[n];
        l = 0; r = -1;
        for (int i = 0; i < n; i++) {
            int k = (i > r) ? 0 : Math.min(d2[l + r - i + 1], r - i + 1);
            while (i - k - 1 >= 0 && i + k < n && seq[i - k - 1] == seq[i + k]) k++;
            d2[i] = k;
            if (i + k - 1 > r) {
                l = i - k;
                r = i + k - 1;
            }
        }

        boolean[] ans = new boolean[n];
        for (int i = 0; i < n; i++) {
            int left = tin[i];
            int right = tout[i];
            int len = right - left + 1;
            if ((len & 1) == 1) { // odd length
                int center = (left + right) >> 1;
                ans[i] = d1[center] >= (len + 1) / 2;
            } else { // even length
                int center = left + len / 2; // right side index for even center
                ans[i] = d2[center] >= len / 2;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findAnswer(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[bool]
        """
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            children[p].append(i)

        # postorder traversal (node added after its children)
        stack = [0]
        temp = []
        while stack:
            node = stack.pop()
            temp.append(node)
            for ch in children[node]:
                stack.append(ch)
        order = temp[::-1]  # postorder

        pos = [0] * n
        for idx, node in enumerate(order):
            pos[node] = idx

        # subtree sizes using reverse order accumulation
        sz = [1] * n
        for node in reversed(order):
            p = parent[node]
            if p != -1:
                sz[p] += sz[node]

        # build string according to postorder
        t = ''.join(s[node] for node in order)

        # Manacher's algorithm
        m = len(t)
        d1 = [0] * m  # odd length radii
        l = 0
        r = -1
        for i in range(m):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < m and t[i - k] == t[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1

        d2 = [0] * m  # even length radii
        l = 0
        r = -1
        for i in range(m):
            k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
            while i - k - 1 >= 0 and i + k < m and t[i - k - 1] == t[i + k]:
                k += 1
            d2[i] = k
            if i + k - 1 > r:
                l = i - k
                r = i + k - 1

        ans = [False] * n
        for node in range(n):
            length = sz[node]
            right = pos[node]
            left = right - length + 1
            if length & 1:
                c = (left + right) // 2
                ok = d1[c] >= (length + 1) // 2
            else:
                i_center = (left + right + 1) // 2
                ok = d2[i_center] >= length // 2
            ans[node] = ok

        return ans
```

## Python3

```python
import sys
sys.setrecursionlimit(300000)

class Solution:
    def findAnswer(self, parent, s):
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        for lst in children:
            lst.sort(reverse=True)  # visit larger indices first

        tin = [0] * n
        tout = [0] * n
        order = []

        def dfs(u):
            tin[u] = len(order)
            order.append(u)
            for v in children[u]:
                dfs(v)
            tout[u] = len(order) - 1

        dfs(0)

        dfsStr = ''.join(s[node] for node in order)

        # Manacher on transformed string with separators '#'
        m = 2 * n + 1
        t = ['#'] * m
        for i, ch in enumerate(dfsStr):
            t[2 * i + 1] = ch

        p = [0] * m
        center = right = 0
        for i in range(m):
            mirror = 2 * center - i
            if i < right:
                p[i] = min(right - i, p[mirror])
            # expand around i
            while i - 1 - p[i] >= 0 and i + 1 + p[i] < m and t[i - 1 - p[i]] == t[i + 1 + p[i]]:
                p[i] += 1
            if i + p[i] > right:
                center, right = i, i + p[i]

        ans = [False] * n
        for i in range(n):
            L, R = tin[i], tout[i]
            c = L + R + 1  # center index in transformed string
            if p[c] >= R - L:
                ans[i] = True

        return ans
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static int min_int(int a, int b) { return a < b ? a : b; }

bool* findAnswer(int* parent, int parentSize, char* s, int* returnSize) {
    int n = parentSize;
    /* Build children list in CSR format */
    int *deg = (int*)calloc(n, sizeof(int));
    for (int i = 1; i < n; ++i) deg[parent[i]]++;

    int *pos = (int*)malloc((n + 1) * sizeof(int));
    pos[0] = 0;
    for (int i = 0; i < n; ++i) pos[i + 1] = pos[i] + deg[i];

    int *children = (int*)malloc((n - 1) * sizeof(int));
    int *cur = (int*)malloc(n * sizeof(int));
    memcpy(cur, pos, n * sizeof(int));

    for (int i = 1; i < n; ++i) {
        int p = parent[i];
        children[cur[p]++] = i;          // stored in increasing order
    }

    free(deg);
    free(cur);

    /* DFS preorder with children visited in decreasing index */
    int *order = (int*)malloc(n * sizeof(int));
    int *tin   = (int*)malloc(n * sizeof(int));
    int *tout  = (int*)malloc(n * sizeof(int));

    int *stackNode = (int*)malloc(n * sizeof(int));
    int *stackIdx  = (int*)malloc(n * sizeof(int));
    int sp = 0;
    int timer = 0;

    stackNode[sp] = 0;
    stackIdx[sp]  = pos[1] - 1;               // last child of root
    tin[0] = timer;
    order[timer++] = 0;

    while (sp >= 0) {
        int node = stackNode[sp];
        int idx  = stackIdx[sp];

        if (idx >= pos[node]) {                // there is an unprocessed child
            int child = children[idx];
            stackIdx[sp]--;                    // move to next child for current node

            sp++;
            stackNode[sp] = child;
            stackIdx[sp]  = pos[child + 1] - 1; // start from its largest child
            tin[child] = timer;
            order[timer++] = child;
        } else {
            tout[node] = timer - 1;
            sp--;
        }
    }

    free(stackNode);
    free(stackIdx);
    free(children);
    free(pos);

    /* Build string according to preorder */
    char *t = (char*)malloc((n + 1) * sizeof(char));
    for (int i = 0; i < n; ++i) t[i] = s[order[i]];
    t[n] = '\0';
    free(order);

    /* Manacher's algorithm */
    int *d1 = (int*)malloc(n * sizeof(int));
    int l = 0, r = -1;
    for (int i = 0; i < n; ++i) {
        int k = (i > r) ? 1 : min_int(d1[l + r - i], r - i + 1);
        while (i - k >= 0 && i + k < n && t[i - k] == t[i + k]) ++k;
        d1[i] = k;
        if (i + k - 1 > r) {
            l = i - k + 1;
            r = i + k - 1;
        }
    }

    int *d2 = (int*)malloc(n * sizeof(int));
    l = 0; r = -1;
    for (int i = 0; i < n; ++i) {
        int k = (i > r) ? 0 : min_int(d2[l + r - i + 1], r - i + 1);
        while (i - k - 1 >= 0 && i + k < n && t[i - k - 1] == t[i + k]) ++k;
        d2[i] = k;
        if (i + k - 1 > r) {
            l = i - k;
            r = i + k - 1;
        }
    }

    free(t);
    free(d1);   // keep d2 for later use? we need both, so postpone free
    /* Compute answers */
    bool *ans = (bool*)malloc(n * sizeof(bool));
    for (int node = 0; node < n; ++node) {
        int L = tin[node];
        int R = tout[node];
        int len = R - L + 1;
        if (len & 1) { // odd
            int c = (L + R) >> 1;
            ans[node] = d1[c] >= (len + 1) / 2;
        } else {       // even
            int center = L + len / 2;   // as per definition of d2
            ans[node] = d2[center] >= len / 2;
        }
    }

    free(d2);
    free(tin);
    free(tout);

    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public bool[] FindAnswer(int[] parent, string s) {
        int n = parent.Length;
        var children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        for (int i = 1; i < n; i++) {
            children[parent[i]].Add(i);
        }

        int[] tin = new int[n];
        int[] sz = new int[n];
        var order = new List<int>(n);

        // iterative DFS to get preorder and subtree sizes
        var stack = new Stack<(int node, int state)>();
        stack.Push((0, 0));
        while (stack.Count > 0) {
            var (node, state) = stack.Pop();
            if (state == 0) {
                tin[node] = order.Count;
                order.Add(node);
                // marker for post-processing
                stack.Push((node, 1));
                // push children in reverse to maintain original order
                var childs = children[node];
                for (int i = childs.Count - 1; i >= 0; --i) {
                    stack.Push((childs[i], 0));
                }
            } else {
                sz[node] = order.Count - tin[node];
            }
        }

        // build preorder character array
        char[] arr = new char[n];
        for (int i = 0; i < n; i++) {
            arr[i] = s[order[i]];
        }

        const ulong B = 127UL;
        var pow = new ulong[n + 1];
        pow[0] = 1;
        for (int i = 1; i <= n; i++) pow[i] = pow[i - 1] * B;

        var pref = new ulong[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] * B + (ulong)(arr[i] - 'a' + 1);
        }

        // reverse string hashes
        var revPref = new ulong[n + 1];
        for (int i = 0; i < n; i++) {
            revPref[i + 1] = revPref[i] * B + (ulong)(arr[n - 1 - i] - 'a' + 1);
        }

        bool[] ans = new bool[n];
        for (int v = 0; v < n; v++) {
            int l = tin[v];
            int r = tin[v] + sz[v] - 1;
            int len = sz[v];

            ulong hashF = pref[r + 1] - pref[l] * pow[len];
            // corresponding segment in reversed array
            int rl = n - 1 - r;
            int rr = n - 1 - l;
            ulong hashR = revPref[rr + 1] - revPref[rl] * pow[len];

            ans[v] = hashF == hashR;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} parent
 * @param {string} s
 * @return {boolean[]}
 */
var findAnswer = function(parent, s) {
    const n = parent.length;
    const children = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; ++i) {
        children[parent[i]].push(i);
    }
    const mask = new Uint32Array(n); // parity mask for each subtree
    const ans = new Array(n);
    const stack = [[0, 0]]; // [node, state] state 0 = first visit, 1 = after children

    while (stack.length) {
        const [u, state] = stack.pop();
        if (state === 0) {
            stack.push([u, 1]);
            const ch = children[u];
            for (let i = ch.length - 1; i >= 0; --i) {
                stack.push([ch[i], 0]);
            }
        } else {
            let m = 1 << (s.charCodeAt(u) - 97);
            for (const v of children[u]) {
                m ^= mask[v];
            }
            mask[u] = m;
            // true if at most one bit is set in m
            ans[u] = (m & (m - 1)) === 0;
        }
    }

    return ans;
};
```

## Typescript

```typescript
function findAnswer(parent: number[], s: string): boolean[] {
    const n = parent.length;
    const children: number[][] = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; i++) {
        children[parent[i]].push(i);
    }

    const tin = new Int32Array(n);
    const sz = new Int32Array(n);
    const orderChars: string[] = [];

    type StackItem = { node: number; idx: number };
    const stack: StackItem[] = [{ node: 0, idx: -1 }];

    while (stack.length) {
        const top = stack[stack.length - 1];
        if (top.idx === -1) {
            // first time visiting this node
            tin[top.node] = orderChars.length;
            orderChars.push(s.charAt(top.node));
            top.idx = 0;
        } else if (top.idx < children[top.node].length) {
            const child = children[top.node][top.idx];
            top.idx++;
            stack.push({ node: child, idx: -1 });
        } else {
            // all children processed, compute subtree size
            let total = 1;
            for (const c of children[top.node]) total += sz[c];
            sz[top.node] = total;
            stack.pop();
        }
    }

    const dfsStr = orderChars.join('');
    const m = dfsStr.length;

    // Manacher's algorithm
    const d1 = new Array<number>(m).fill(0);
    let l = 0, r = -1;
    for (let i = 0; i < m; i++) {
        let k = 1;
        if (i <= r) k = Math.min(d1[l + r - i], r - i + 1);
        while (i - k >= 0 && i + k < m && dfsStr[i - k] === dfsStr[i + k]) k++;
        d1[i] = k;
        if (i + k - 1 > r) {
            l = i - k + 1;
            r = i + k - 1;
        }
    }

    const d2 = new Array<number>(m).fill(0);
    l = 0; r = -1;
    for (let i = 0; i < m; i++) {
        let k = 0;
        if (i <= r) k = Math.min(d2[l + r - i + 1], r - i + 1);
        while (i - k - 1 >= 0 && i + k < m && dfsStr[i - k - 1] === dfsStr[i + k]) k++;
        d2[i] = k;
        if (i + k - 1 > r) {
            l = i - k;
            r = i + k - 1;
        }
    }

    const answer: boolean[] = new Array<boolean>(n);
    for (let i = 0; i < n; i++) {
        const len = sz[i];
        const left = tin[i];
        const right = left + len - 1;
        if (len % 2 === 1) {
            const center = (left + right) >> 1;
            answer[i] = d1[center] >= ((len + 1) >> 1);
        } else {
            const center = (left + right + 1) >> 1;
            answer[i] = d2[center] >= (len >> 1);
        }
    }

    return answer;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $parent
     * @param String $s
     * @return Boolean[]
     */
    function findAnswer($parent, $s) {
        $n = count($parent);
        // build children list
        $children = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) {
            $p = $parent[$i];
            $children[$p][] = $i;
        }

        // iterative DFS to get preorder and subtree intervals
        $tin = array_fill(0, $n, -1);
        $tout = array_fill(0, $n, -1);
        $order = [];

        $stack = [];
        // each element: [node, visitedFlag]
        $stack[] = [0, false];
        while (!empty($stack)) {
            [$v, $exit] = array_pop($stack);
            if (!$exit) {
                $tin[$v] = count($order);
                $order[] = $v;
                // push exit marker
                $stack[] = [$v, true];
                // push children in reverse to keep original order
                $chs = $children[$v];
                for ($j = count($chs) - 1; $j >= 0; $j--) {
                    $stack[] = [$chs[$j], false];
                }
            } else {
                $tout[$v] = count($order) - 1;
            }
        }

        // build the DFS string as array of characters
        $tChars = [];
        foreach ($order as $idx) {
            $tChars[] = $s[$idx];
        }
        $m = $n; // length of tChars

        // Manacher odd-length radii (d1)
        $d1 = array_fill(0, $m, 0);
        $l = 0;
        $r = -1;
        for ($i = 0; $i < $m; $i++) {
            $k = ($i > $r) ? 1 : min($d1[$l + $r - $i], $r - $i + 1);
            while ($i - $k >= 0 && $i + $k < $m && $tChars[$i - $k] === $tChars[$i + $k]) {
                $k++;
            }
            $d1[$i] = $k;
            if ($i + $k - 1 > $r) {
                $l = $i - $k + 1;
                $r = $i + $k - 1;
            }
        }

        // Manacher even-length radii (d2)
        $d2 = array_fill(0, $m, 0);
        $l = 0;
        $r = -1;
        for ($i = 0; $i < $m; $i++) {
            $k = ($i > $r) ? 0 : min($d2[$l + $r - $i + 1], $r - $i + 1);
            while ($i - $k - 1 >= 0 && $i + $k < $m && $tChars[$i - $k - 1] === $tChars[$i + $k]) {
                $k++;
            }
            $d2[$i] = $k;
            if ($i + $k - 1 > $r) {
                $l = $i - $k;
                $r = $i + $k - 1;
            }
        }

        // compute answer for each node
        $answer = array_fill(0, $n, false);
        for ($node = 0; $node < $n; $node++) {
            $lIdx = $tin[$node];
            $rIdx = $tout[$node];
            $len = $rIdx - $lIdx + 1;
            if (($len & 1) == 1) { // odd length
                $center = intdiv($lIdx + $rIdx, 2);
                $need = intdiv($len, 2) + 1; // radius needed in d1
                $answer[$node] = ($d1[$center] >= $need);
            } else { // even length
                $half = intdiv($len, 2);
                $centerIdx = $lIdx + $half; // index for d2
                $answer[$node] = ($d2[$centerIdx] >= $half);
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func findAnswer(_ parent: [Int], _ s: String) -> [Bool] {
        let n = parent.count
        var children = [[Int]](repeating: [], count: n)
        if n > 1 {
            for i in 1..<n {
                children[parent[i]].append(i)
            }
        }

        // preorder traversal, compute tin and subtree sizes
        var order = [Int]()
        order.reserveCapacity(n)
        var tin = [Int](repeating: 0, count: n)
        var subSize = [Int](repeating: 0, count: n)

        var stack: [(Int, Int)] = [(0, 0)]   // (node, state) state 0 = enter, 1 = exit
        while let (v, state) = stack.popLast() {
            if state == 0 {
                tin[v] = order.count
                order.append(v)
                stack.append((v, 1))
                for child in children[v].reversed() {
                    stack.append((child, 0))
                }
            } else {
                var sz = 1
                for c in children[v] {
                    sz += subSize[c]
                }
                subSize[v] = sz
            }
        }

        var tout = [Int](repeating: 0, count: n)
        for i in 0..<n {
            tout[i] = tin[i] + subSize[i] - 1
        }

        // convert characters to numbers (a -> 1, b -> 2, ...)
        let charVals = Array(s.utf8).map { UInt64($0 - 96) }
        var seq = [UInt64](repeating: 0, count: n)
        for i in 0..<n {
            seq[i] = charVals[order[i]]
        }

        // rolling hash preparation
        let base: UInt64 = 91138233
        var powBase = [UInt64](repeating: 0, count: n + 1)
        powBase[0] = 1
        if n > 0 {
            for i in 1...n {
                powBase[i] = powBase[i - 1] &* base
            }
        }

        var pref = [UInt64](repeating: 0, count: n + 1)
        for i in 0..<n {
            pref[i + 1] = pref[i] &* base &+ seq[i]
        }

        // hash of reversed sequence
        var revSeq = [UInt64](repeating: 0, count: n)
        for i in 0..<n {
            revSeq[i] = seq[n - 1 - i]
        }
        var revPref = [UInt64](repeating: 0, count: n + 1)
        for i in 0..<n {
            revPref[i + 1] = revPref[i] &* base &+ revSeq[i]
        }

        func forwardHash(_ l: Int, _ r: Int) -> UInt64 {
            let len = r - l + 1
            return pref[r + 1] &- (pref[l] &* powBase[len])
        }

        func reverseHash(_ l: Int, _ r: Int) -> UInt64 {
            // map to reversed indices
            let rl = n - 1 - r
            let rr = n - 1 - l
            let len = r - l + 1
            return revPref[rr + 1] &- (revPref[rl] &* powBase[len])
        }

        var answer = [Bool](repeating: false, count: n)
        for i in 0..<n {
            let l = tin[i]
            let r = tout[i]
            if forwardHash(l, r) == reverseHash(l, r) {
                answer[i] = true
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun findAnswer(parent: IntArray, s: String): BooleanArray {
        val n = parent.size
        // build children lists
        val children = Array(n) { mutableListOf<Int>() }
        for (i in 1 until n) {
            children[parent[i]].add(i)
        }

        // preorder traversal to get tin, tout and order of nodes
        val tin = IntArray(n)
        val tout = IntArray(n)
        val order = IntArray(n)
        var idx = 0

        // iterative DFS using explicit stacks
        val nodeStack = IntArray(n)
        val childIdxStack = IntArray(n)
        var sp = 0
        nodeStack[sp] = 0
        childIdxStack[sp] = 0
        sp++

        while (sp > 0) {
            val top = sp - 1
            val node = nodeStack[top]
            var ci = childIdxStack[top]

            if (ci == 0) { // first time we see this node
                tin[node] = idx
                order[idx] = node
                idx++
            }

            if (ci < children[node].size) {
                // go deeper to next child
                val child = children[node][ci]
                childIdxStack[top] = ci + 1
                nodeStack[sp] = child
                childIdxStack[sp] = 0
                sp++
            } else {
                tout[node] = idx - 1
                sp--
            }
        }

        // build the string according to preorder order
        val t = CharArray(n)
        for (i in 0 until n) {
            t[i] = s[order[i]]
        }

        // Manacher's algorithm: odd length palindromes
        val d1 = IntArray(n)
        var l = 0
        var r = -1
        for (i in 0 until n) {
            var k = if (i > r) 1 else kotlin.math.min(d1[l + r - i], r - i + 1)
            while (i - k >= 0 && i + k < n && t[i - k] == t[i + k]) {
                k++
            }
            d1[i] = k
            if (i + k - 1 > r) {
                l = i - k + 1
                r = i + k - 1
            }
        }

        // Manacher's algorithm: even length palindromes
        val d2 = IntArray(n)
        l = 0
        r = -1
        for (i in 0 until n) {
            var k = if (i > r) 0 else kotlin.math.min(d2[l + r - i + 1], r - i + 1)
            while (i - k - 1 >= 0 && i + k < n && t[i - k - 1] == t[i + k]) {
                k++
            }
            d2[i] = k
            if (i + k - 1 > r) {
                l = i - k
                r = i + k - 1
            }
        }

        // answer for each node based on its subtree interval
        val ans = BooleanArray(n)
        for (i in 0 until n) {
            val left = tin[i]
            val right = tout[i]
            val len = right - left + 1
            if (len % 2 == 1) {
                val center = (left + right) / 2
                ans[i] = d1[center] >= (len + 1) / 2
            } else {
                // even length: center is between positions (c-1) and c, represented by index c in d2
                val c = (left + right + 1) / 2
                ans[i] = d2[c] >= len / 2
            }
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<bool> findAnswer(List<int> parent, String s) {
    int n = parent.length;
    // Build children lists in decreasing order of indices
    List<List<int>> children = List.generate(n, (_) => []);
    for (int i = n - 1; i >= 1; --i) {
      children[parent[i]].add(i);
    }

    // Preorder traversal to get order and subtree intervals
    List<int> tin = List.filled(n, 0);
    List<int> tout = List.filled(n, 0);
    List<int> order = [];
    // stack of pairs (node, next child index)
    List<List<int>> stack = [[0, 0]];
    while (stack.isNotEmpty) {
      var top = stack.last;
      int node = top[0];
      int idx = top[1];
      if (idx == 0) {
        tin[node] = order.length;
        order.add(node);
      }
      if (idx < children[node].length) {
        // visit next child
        int child = children[node][idx];
        top[1] = idx + 1; // increment child index for current node
        stack.add([child, 0]);
      } else {
        tout[node] = order.length - 1;
        stack.removeLast();
      }
    }

    int m = order.length;
    String dfsStr = StringBuffer()
        .writeAll(order.map((idx) => s[idx]))
        .toString();

    const int mod1 = 1000000007;
    const int mod2 = 1000000009;
    const int base = 91138233;

    List<int> pow1 = List.filled(m + 1, 0);
    List<int> pow2 = List.filled(m + 1, 0);
    pow1[0] = 1;
    pow2[0] = 1;
    for (int i = 1; i <= m; ++i) {
      pow1[i] = ((pow1[i - 1] * base) % mod1).toInt();
      pow2[i] = ((pow2[i - 1] * base) % mod2).toInt();
    }

    List<int> prefF1 = List.filled(m + 1, 0);
    List<int> prefF2 = List.filled(m + 1, 0);
    for (int i = 0; i < m; ++i) {
      int code = dfsStr.codeUnitAt(i) - 97 + 1;
      prefF1[i + 1] = ((prefF1[i] * base + code) % mod1).toInt();
      prefF2[i + 1] = ((prefF2[i] * base + code) % mod2).toInt();
    }

    String revStr = dfsStr.split('').reversed.join();
    List<int> prefR1 = List.filled(m + 1, 0);
    List<int> prefR2 = List.filled(m + 1, 0);
    for (int i = 0; i < m; ++i) {
      int code = revStr.codeUnitAt(i) - 97 + 1;
      prefR1[i + 1] = ((prefR1[i] * base + code) % mod1).toInt();
      prefR2[i + 1] = ((prefR2[i] * base + code) % mod2).toInt();
    }

    int getHash(List<int> pref, List<int> pow, int l, int r, int mod) {
      int res = (pref[r + 1] -
              (pref[l] * pow[r - l + 1]) % mod +
              mod) %
          mod;
      return res;
    }

    List<bool> ans = List.filled(n, false);
    for (int node = 0; node < n; ++node) {
      int l = tin[node];
      int r = tout[node];
      int h1F = getHash(prefF1, pow1, l, r, mod1);
      int h2F = getHash(prefF2, pow2, l, r, mod2);
      int revL = m - 1 - r;
      int revR = m - 1 - l;
      int h1R = getHash(prefR1, pow1, revL, revR, mod1);
      int h2R = getHash(prefR2, pow2, revL, revR, mod2);
      ans[node] = (h1F == h1R && h2F == h2R);
    }
    return ans;
  }
}
```

## Golang

```go
func findAnswer(parent []int, s string) []bool {
    n := len(parent)
    children := make([][]int, n)
    for i := 1; i < n; i++ {
        p := parent[i]
        children[p] = append(children[p], i)
    }

    order := make([]int, 0, n)
    tin := make([]int, n)
    tout := make([]int, n)

    var dfs func(int)
    time := 0
    dfs = func(u int) {
        tin[u] = time
        order = append(order, u)
        time++
        for _, v := range children[u] {
            dfs(v)
        }
        tout[u] = time - 1
    }
    dfs(0)

    pref := make([]int, n+1)
    for i, node := range order {
        c := s[node] - 'a'
        pref[i+1] = pref[i] ^ (1 << c)
    }

    ans := make([]bool, n)
    for i := 0; i < n; i++ {
        mask := pref[tout[i]+1] ^ pref[tin[i]]
        if mask&(mask-1) == 0 {
            ans[i] = true
        } else {
            ans[i] = false
        }
    }
    return ans
}
```

## Ruby

```ruby
def find_answer(parent, s)
  n = parent.length
  children = Array.new(n) { [] }
  (1...n).each do |i|
    p = parent[i]
    children[p] << i
  end

  order_chars = []
  order_nodes = []
  entry = Array.new(n)
  stack = [0]

  while !stack.empty?
    u = stack.pop
    entry[u] = order_chars.length
    order_chars << s[u]
    order_nodes << u
    # push children in ascending order so they are processed in descending order
    children[u].each { |v| stack << v }
  end

  subsize = Array.new(n, 1)
  (order_nodes.length - 1).downto(0) do |idx|
    u = order_nodes[idx]
    p = parent[u]
    subsize[p] += subsize[u] if p != -1
  end

  str = order_chars.join

  # Manacher's algorithm
  n_str = str.length
  d1 = Array.new(n_str, 0)
  l = 0
  r = -1
  (0...n_str).each do |i|
    k = i > r ? 1 : [d1[l + r - i], r - i + 1].min
    while i - k >= 0 && i + k < n_str && str[i - k] == str[i + k]
      k += 1
    end
    d1[i] = k
    k -= 1
    if i + k > r
      l = i - k
      r = i + k
    end
  end

  d2 = Array.new(n_str, 0)
  l = 0
  r = -1
  (0...n_str).each do |i|
    k = i > r ? 0 : [d2[l + r - i + 1], r - i + 1].min
    while i - k - 1 >= 0 && i + k < n_str && str[i - k - 1] == str[i + k]
      k += 1
    end
    d2[i] = k
    k -= 1
    if i + k > r
      l = i - k - 1
      r = i + k
    end
  end

  answer = Array.new(n, false)
  (0...n).each do |u|
    l_idx = entry[u]
    r_idx = l_idx + subsize[u] - 1
    len = r_idx - l_idx + 1
    if len.odd?
      center = (l_idx + r_idx) / 2
      need = (len + 1) / 2
      answer[u] = d1[center] >= need
    else
      center = (l_idx + r_idx + 1) / 2
      need = len / 2
      answer[u] = d2[center] >= need
    end
  end

  answer
end
```

## Scala

```scala
object Solution {
  def findAnswer(parent: Array[Int], s: String): Array[Boolean] = {
    val n = parent.length
    // build children adjacency list
    val children = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
    var i = 1
    while (i < n) {
      children(parent(i)).append(i)
      i += 1
    }

    // preorder traversal to get order and subtree ranges
    val order = new Array[Int](n)
    val tin = new Array[Int](n)
    val tout = new Array[Int](n)

    var idx = 0
    val stack = new scala.collection.mutable.Stack[(Int, Int)]()
    stack.push((0, 0)) // (node, next child index)

    while (stack.nonEmpty) {
      val (node, childIdx) = stack.pop()
      if (childIdx == 0) {
        tin(node) = idx
        order(idx) = node
        idx += 1
      }
      if (childIdx < children(node).size) {
        // push current node with next child index
        stack.push((node, childIdx + 1))
        val child = children(node)(childIdx)
        stack.push((child, 0))
      } else {
        tout(node) = idx
      }
    }

    // build character array in preorder order
    val seq = new Array[Char](n)
    i = 0
    while (i < n) {
      seq(i) = s.charAt(order(i))
      i += 1
    }

    // Manacher's algorithm
    def manacher(arr: Array[Char]): (Array[Int], Array[Int]) = {
      val m = arr.length
      val d1 = new Array[Int](m)
      var l = 0
      var r = -1
      var j = 0
      while (j < m) {
        var k = if (j > r) 1 else math.min(d1(l + r - j), r - j + 1)
        while (j - k >= 0 && j + k < m && arr(j - k) == arr(j + k)) k += 1
        d1(j) = k
        if (j + k - 1 > r) {
          l = j - k + 1
          r = j + k - 1
        }
        j += 1
      }

      val d2 = new Array[Int](m)
      l = 0
      r = -1
      j = 0
      while (j < m) {
        var k = if (j > r) 0 else math.min(d2(l + r - j + 1), r - j + 1)
        while (j - k - 1 >= 0 && j + k < m && arr(j - k - 1) == arr(j + k)) k += 1
        d2(j) = k
        if (j + k - 1 > r) {
          l = j - k
          r = j + k - 1
        }
        j += 1
      }
      (d1, d2)
    }

    val (d1, d2) = manacher(seq)

    // answer for each node
    val ans = new Array[Boolean](n)
    i = 0
    while (i < n) {
      val lIdx = tin(i)
      val rIdx = tout(i) - 1
      val len = rIdx - lIdx + 1
      if ((len & 1) == 1) { // odd length
        val c = (lIdx + rIdx) / 2
        ans(i) = d1(c) >= (len + 1) / 2
      } else { // even length
        val c = (lIdx + rIdx + 1) / 2
        ans(i) = d2(c) >= len / 2
      }
      i += 1
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_answer(parent: Vec<i32>, s: String) -> Vec<bool> {
        let n = parent.len();
        let mut children: Vec<Vec<usize>> = vec![Vec::new(); n];
        for i in 1..n {
            let p = parent[i] as usize;
            children[p].push(i);
        }

        // DFS to build the traversal string and record entry/exit positions
        let s_bytes = s.as_bytes();
        let mut lpos: Vec<usize> = vec![0; n];
        let mut rpos: Vec<usize> = vec![0; n];
        let mut dfs_str: Vec<u8> = Vec::with_capacity(2 * n);
        // stack of (node, next_child_index)
        let mut stack: Vec<(usize, usize)> = Vec::new();
        stack.push((0, 0));
        while let Some(&(v, idx)) = stack.last() {
            if idx == 0 {
                // first time we see this node
                lpos[v] = dfs_str.len();
                dfs_str.push(s_bytes[v]);
            }
            if idx < children[v].len() {
                let child = children[v][idx];
                // increment child index for current node
                *stack.last_mut().unwrap() = (v, idx + 1);
                stack.push((child, 0));
            } else {
                // all children processed, add exit character
                rpos[v] = dfs_str.len();
                dfs_str.push(s_bytes[v]);
                stack.pop();
            }
        }

        let m = dfs_str.len();

        // Manacher's algorithm for odd length palindromes (d1)
        let mut d1: Vec<usize> = vec![0; m];
        let mut l = 0usize;
        let mut r = 0usize;
        for i in 0..m {
            let mut k = if i > r { 1 } else { std::cmp::min(d1[l + r - i], r - i + 1) };
            while i + k < m && i >= k - 1 && dfs_str[i - (k - 1)] == dfs_str[i + k] {
                k += 1;
            }
            d1[i] = k;
            if i + k - 1 > r {
                l = i - (k - 1);
                r = i + k - 1;
            }
        }

        // Manacher's algorithm for even length palindromes (d2)
        let mut d2: Vec<usize> = vec![0; m];
        l = 0;
        r = 0;
        for i in 0..m {
            let mut k = if i > r { 0 } else { std::cmp::min(d2[l + r - i + 1], r - i + 1) };
            while i + k < m && i >= k && dfs_str[i - k] == dfs_str[i + k] {
                k += 1;
            }
            d2[i] = k;
            if i + k - 1 > r {
                l = i - k;
                r = i + k - 1;
            }
        }

        // Determine answer for each node
        let mut ans: Vec<bool> = vec![false; n];
        for v in 0..n {
            let len = rpos[v] - lpos[v] + 1;
            if len % 2 == 1 {
                let center = (lpos[v] + rpos[v]) / 2;
                let need = (len + 1) / 2;
                ans[v] = d1[center] >= need;
            } else {
                let center = (lpos[v] + rpos[v] + 1) / 2; // between positions
                let need = len / 2;
                ans[v] = d2[center] >= need;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (find-answer parent s)
  (-> (listof exact-integer?) string? (listof boolean?))
  (let* ((n (length parent))
         (parentV (list->vector parent))
         (children (make-vector n '()))
         ;; build children lists
         (build-children
          (let loop ((i 1))
            (when (< i n)
              (let ((p (vector-ref parentV i)))
                (vector-set! children p (cons i (vector-ref children p))))
              (loop (+ i 1)))))
         (_ (build-children))
         ;; preorder traversal
         (order (make-vector n 0))
         (tin (make-vector n -1))
         (stack (list 0))
         (traverse
          (let loop ((stk stack) (idx 0))
            (if (null? stk)
                idx
                (let* ((x (car stk))
                       (rest (cdr stk)))
                  (vector-set! tin x idx)
                  (vector-set! order idx x)
                  ;; push children onto stack
                  (let ((new-stack
                         (foldl (lambda (ch acc) (cons ch acc))
                                rest
                                (vector-ref children x))))
                    (loop new-stack (+ idx 1)))))))
         (_ (traverse)) ; fill tin and order
         ;; compute subtree sizes
         (size (make-vector n 1))
         (compute-sizes
          (let loop ((i (- n 1)))
            (when (>= i 0)
              (let ((node (vector-ref order i)))
                (for-each (lambda (ch)
                            (vector-set! size node
                                         (+ (vector-ref size node)
                                            (vector-ref size ch))))
                          (vector-ref children node)))
              (loop (- i 1)))))
         (_ (compute-sizes))
         ;; tout indices
         (tout (make-vector n 0))
         (set-tout
          (let loop ((i 0))
            (when (< i n)
              (let ((node i))
                (vector-set! tout node
                             (+ (vector-ref tin node)
                                (vector-ref size node) -1)))
              (loop (+ i 1)))))
         (_ (set-tout))
         ;; character codes in preorder order (1..26)
         (chars (make-vector n 0))
         (fill-chars
          (let loop ((pos 0))
            (when (< pos n)
              (let* ((node (vector-ref order pos))
                     (ch (string-ref s node))
                     (code (+ (- (char->integer ch) (char->integer #\a)) 1)))
                (vector-set! chars pos code))
              (loop (+ pos 1)))))
         (_ (fill-chars))
         ;; hashing preparation
         (MOD 1000000007)
         (BASE 91138233)
         (pow (make-vector (+ n 1) 0))
         (pref (make-vector (+ n 1) 0))
         (revPref (make-vector (+ n 1) 0))
         (_ (vector-set! pow 0 1))
         (_ (let loop ((i 1))
              (when (<= i n)
                (vector-set! pow i
                             (modulo (* (vector-ref pow (- i 1)) BASE) MOD))
                (loop (+ i 1)))))
         (_ (let loop ((i 0))
              (when (< i n)
                (let ((prev (vector-ref pref i))
                      (code (vector-ref chars i)))
                  (vector-set! pref (+ i 1)
                               (modulo (+ (* prev BASE) code) MOD)))
                (loop (+ i 1)))))
         (_ (let loop ((i 0))
              (when (< i n)
                (let* ((code (vector-ref chars (- n 1 i))) ; reverse order
                       (prev (vector-ref revPref i)))
                  (vector-set! revPref (+ i 1)
                               (modulo (+ (* prev BASE) code) MOD)))
                (loop (+ i 1)))))
         ;; helper to get hash of substring [l,r] inclusive
         (subhash
          (lambda (prefVec l r)
            (let* ((len (+ 1 (- r l)))
                   (raw (- (vector-ref prefVec (+ r 1))
                           (modulo (* (vector-ref prefVec l)
                                      (vector-ref pow len)) MOD))))
              (if (< raw 0) (+ raw MOD) raw)))))
         ;; palindrome check for a node's subtree
         (is-pal?
          (lambda (l r)
            (= (subhash pref l r)
               (subhash revPref (- n 1 r) (- n 1 l)))))
         ;; build answer list
         (ansVec (make-vector n #f))
         (_ (let loop ((i 0))
              (when (< i n)
                (let ((l (vector-ref tin i))
                      (r (vector-ref tout i)))
                  (vector-set! ansVec i (is-pal? l r)))
                (loop (+ i 1))))))
    (vector->list ansVec)))
```

## Erlang

```erlang
-spec find_answer(Parent :: [integer()], S :: unicode:unicode_binary()) -> [boolean()].
find_answer(Parent, S) ->
    N = length(Parent),

    %% Build children map
    Indices = lists:seq(0, N - 1),
    ChildrenMap = lists:foldl(
        fun(I, Acc) ->
            case I of
                0 -> Acc;
                _ ->
                    P = lists:nth(I + 1, Parent), % nth is 1‑based
                    maps:update_with(P,
                        fun(L) -> [I | L] end,
                        [I],
                        Acc)
            end
        end,
        #{},
        Indices),

    %% Iterative DFS to obtain preorder, tin and tout
    {PreorderRev, TinMap, ToutMap} = dfs_iter([{0, 0}], ChildrenMap, #{}, #{}, [], 0),
    Preorder = lists:reverse(PreorderRev),

    %% Character codes in preorder
    CharCodes = [binary:at(S, Node) || Node <- Preorder],
    RevCharCodes = lists:reverse(CharCodes),

    Base = 91138233,
    Mod1 = 1000000007,
    Mod2 = 1000000009,

    Pow1 = build_pow(N, Base, Mod1),
    Pow2 = build_pow(N, Base, Mod2),

    PrefF1 = build_prefix(CharCodes, Base, Mod1),
    PrefF2 = build_prefix(CharCodes, Base, Mod2),
    PrefR1 = build_prefix(RevCharCodes, Base, Mod1),
    PrefR2 = build_prefix(RevCharCodes, Base, Mod2),

    %% Compute answer for each node
    lists:map(
        fun(I) ->
            L = maps:get(I, TinMap),
            R = maps:get(I, ToutMap),
            Hf1 = get_hash(PrefF1, Pow1, L, R, Mod1),
            Hr1 = get_hash(PrefR1, Pow1, N - 1 - R, N - 1 - L, Mod1),
            Hf2 = get_hash(PrefF2, Pow2, L, R, Mod2),
            Hr2 = get_hash(PrefR2, Pow2, N - 1 - R, N - 1 - L, Mod2),
            (Hf1 == Hr1) andalso (Hf2 == Hr2)
        end,
        lists:seq(0, N - 1)).

%% ------------------------------------------------------------------
%% DFS iterative traversal
%% Returns {PreorderRev, TinMap, ToutMap}
%% PreorderRev is the preorder list built in reverse order for efficiency.
%% ------------------------------------------------------------------
dfs_iter([], _ChildrenMap, Tin, Tout, OrderAcc, _Idx) ->
    {OrderAcc, Tin, Tout};
dfs_iter([{Node, Flag} | Rest], ChildrenMap, Tin, Tout, OrderAcc, Idx) ->
    case Flag of
        0 -> % entering node
            NewTin = maps:put(Node, Idx, Tin),
            NewOrderAcc = [Node | OrderAcc],
            NewIdx = Idx + 1,
            Children = maps:get(Node, ChildrenMap, []),
            RevChildren = lists:reverse(Children),
            StackWithExit = [{Node, 1} | Rest],
            NewStack = lists:foldl(
                fun(C, Acc) -> [{C, 0} | Acc] end,
                StackWithExit,
                RevChildren),
            dfs_iter(NewStack, ChildrenMap, NewTin, Tout, NewOrderAcc, NewIdx);
        1 -> % exiting node
            NewTout = maps:put(Node, Idx - 1, Tout),
            dfs_iter(Rest, ChildrenMap, Tin, NewTout, OrderAcc, Idx)
    end.

%% ------------------------------------------------------------------
%% Build power array pow[i] = base^i mod Mod, for i = 0..N
%% Returned as tuple where element(Idx+1) = pow[Idx]
%% ------------------------------------------------------------------
build_pow(N, Base, Mod) ->
    PowList = lists:foldl(
        fun(_, Acc) ->
            [Prev | _] = Acc,
            New = (Prev * Base) rem Mod,
            [New | Acc]
        end,
        [1],
        lists:seq(1, N)),
    list_to_tuple(lists:reverse(PowList)).

%% ------------------------------------------------------------------
%% Build prefix hash array pref where pref[0]=0 and
%% pref[i+1] = (pref[i]*Base + Code_i) mod Mod
%% Returned as tuple where element(i+1)=pref[i]
%% ------------------------------------------------------------------
build_prefix(Codes, Base, Mod) ->
    {_, RevPref} = lists:foldl(
        fun(Code, {Prev, Acc}) ->
            New = (Prev * Base + Code) rem Mod,
            {New, [New | Acc]}
        end,
        {0, [0]},
        Codes),
    list_to_tuple(lists:reverse(RevPref)).

%% ------------------------------------------------------------------
%% Get hash of substring [L,R] inclusive using prefix and power arrays
%% ------------------------------------------------------------------
get_hash(PrefTuple, PowTuple, L, R, Mod) ->
    Len = R - L + 1,
    HashL = element(L + 1, PrefTuple),
    HashRplus = element(R + 2, PrefTuple), % pref at index R+1
    PowLen = element(Len + 1, PowTuple),
    ((HashRplus - (HashL * PowLen) rem Mod) + Mod) rem Mod.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_answer(parent :: [integer], s :: String.t) :: [boolean]
  def find_answer(parent, s) do
    n = length(parent)

    # convert parent to array for O(1) access
    parent_arr = :array.from_list(parent)

    # build children adjacency list
    children =
      Enum.reduce(1..(n - 1), List.duplicate([], n), fn i, acc ->
        p = :array.get(i, parent_arr)
        List.update_at(acc, p, fn lst -> [i | lst] end)
      end)

    # preorder traversal to get order and tin
    {order, tin_arr} = preorder(children, n)

    # compute subtree sizes using postorder (reverse of preorder)
    size_arr =
      Enum.reduce(Enum.reverse(order), :array.new(n, default: 0), fn node, arr ->
        child_sum =
          Enum.reduce(Enum.at(children, node), 0, fn child, acc ->
            acc + :array.get(child, arr)
          end)

        :array.set(node, 1 + child_sum, arr)
      end)

    # build dfs string as array of character codes
    charlist = String.to_charlist(s)

    dfs_codes =
      Enum.map(order, fn node -> Enum.at(charlist, node) end)

    code_arr = :array.from_list(dfs_codes)

    # Manacher algorithm
    {d1, d2} = manacher(code_arr)

    # answer for each node
    answers =
      for i <- 0..(n - 1) do
        l = :array.get(i, tin_arr)
        sz = :array.get(i, size_arr)
        r = l + sz - 1
        len = sz

        if rem(len, 2) == 1 do
          center = div(l + r, 2)
          need = div(len + 1, 2)

          rad = :array.get(center, d1)
          rad >= need
        else
          center = div(l + r + 1, 2)
          need = div(len, 2)

          rad = :array.get(center, d2)
          rad >= need
        end
      end

    answers
  end

  # preorder traversal returning order list and tin array
  defp preorder(children, n) do
    traverse = fn
      [], _idx, order_rev, tin_arr ->
        {Enum.reverse(order_rev), tin_arr}

      [node | rest], idx, order_rev, tin_arr ->
        tin_arr = :array.set(node, idx, tin_arr)
        child_list = Enum.at(children, node)

        # push children onto stack in reverse to process them in original order
        new_stack = Enum.reverse(child_list) ++ rest

        traverse.(new_stack, idx + 1, [node | order_rev], tin_arr)
    end

    traverse.([0], 0, [], :array.new(n, default: 0))
  end

  # Manacher algorithm returning arrays d1 (odd) and d2 (even)
  defp manacher(arr) do
    n = :array.size(arr)

    # odd length palindromes
    {d1, _l, _r} =
      Enum.reduce(0..(n - 1), {:array.new(n, default: 0), 0, -1}, fn i,
                                                                   {d1_acc, l, r} ->
        k =
          if i > r do
            1
          else
            min(:array.get(l + r - i, d1_acc), r - i + 1)
          end

        k = expand_odd(arr, i, k, n)

        d1_new = :array.set(i, k, d1_acc)

        if i + k - 1 > r do
          {d1_new, i - k + 1, i + k - 1}
        else
          {d1_new, l, r}
        end
      end)

    # even length palindromes
    {d2, _l2, _r2} =
      Enum.reduce(0..(n - 1), {:array.new(n, default: 0), 0, -1}, fn i,
                                                                   {d2_acc, l, r} ->
        k =
          if i > r do
            0
          else
            min(:array.get(l + r - i + 1, d2_acc), r - i + 1)
          end

        k = expand_even(arr, i, k, n)

        d2_new = :array.set(i, k, d2_acc)

        if i + k - 1 > r do
          {d2_new, i - k, i + k - 1}
        else
          {d2_new, l, r}
        end
      end)

    {d1, d2}
  end

  defp expand_odd(arr, i, k, n) do
    if i - k >= 0 and i + k < n and :array.get(i - k, arr) == :array.get(i + k, arr) do
      expand_odd(arr, i, k + 1, n)
    else
      k
    end
  end

  defp expand_even(arr, i, k, n) do
    if i - k - 1 >= 0 and i + k < n and :array.get(i - k - 1, arr) == :array.get(i + k, arr) do
      expand_even(arr, i, k + 1, n)
    else
      k
    end
  end
end
```
