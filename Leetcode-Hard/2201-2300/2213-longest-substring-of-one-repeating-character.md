# 2213. Longest Substring of One Repeating Character

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct Node {
        int len = 0;
        char lch = 0, rch = 0;
        int pref = 0, suff = 0, best = 0;
    };
    
    vector<Node> seg;
    string s;
    
    Node mergeNode(const Node& a, const Node& b) {
        if (a.len == 0) return b;
        if (b.len == 0) return a;
        Node res;
        res.len = a.len + b.len;
        res.lch = a.lch;
        res.rch = b.rch;
        
        // prefix
        res.pref = a.pref;
        if (a.pref == a.len && a.rch == b.lch) {
            res.pref = a.len + b.pref;
        }
        // suffix
        res.suff = b.suff;
        if (b.suff == b.len && a.rch == b.lch) {
            res.suff = b.len + a.suff;
        }
        // best
        res.best = max(a.best, b.best);
        if (a.rch == b.lch) {
            res.best = max(res.best, a.suff + b.pref);
        }
        return res;
    }
    
    void build(int idx, int l, int r) {
        if (l == r) {
            Node leaf;
            leaf.len = 1;
            leaf.lch = leaf.rch = s[l];
            leaf.pref = leaf.suff = leaf.best = 1;
            seg[idx] = leaf;
            return;
        }
        int mid = (l + r) >> 1;
        build(idx<<1, l, mid);
        build(idx<<1|1, mid+1, r);
        seg[idx] = mergeNode(seg[idx<<1], seg[idx<<1|1]);
    }
    
    void update(int idx, int l, int r, int pos, char c) {
        if (l == r) {
            Node leaf;
            leaf.len = 1;
            leaf.lch = leaf.rch = c;
            leaf.pref = leaf.suff = leaf.best = 1;
            seg[idx] = leaf;
            return;
        }
        int mid = (l + r) >> 1;
        if (pos <= mid) update(idx<<1, l, mid, pos, c);
        else update(idx<<1|1, mid+1, r, pos, c);
        seg[idx] = mergeNode(seg[idx<<1], seg[idx<<1|1]);
    }
    
    vector<int> longestRepeating(string s_, string queryCharacters, vector<int>& queryIndices) {
        s = move(s_);
        int n = s.size();
        seg.assign(4*n+5, Node());
        build(1, 0, n-1);
        int q = queryCharacters.size();
        vector<int> ans;
        ans.reserve(q);
        for (int i = 0; i < q; ++i) {
            int pos = queryIndices[i];
            char c = queryCharacters[i];
            if (s[pos] != c) {
                s[pos] = c;
                update(1, 0, n-1, pos, c);
            }
            ans.push_back(seg[1].best);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private static class Node {
        char leftChar;
        char rightChar;
        int pref;   // longest prefix of same character
        int suff;   // longest suffix of same character
        int best;   // longest homogeneous substring in this segment
        int len;    // length of the segment

        Node(char c) {
            this.leftChar = this.rightChar = c;
            this.pref = this.suff = this.best = this.len = 1;
        }

        Node() { }
    }

    private Node[] seg;
    private char[] arr;

    public int[] longestRepeating(String s, String queryCharacters, int[] queryIndices) {
        int n = s.length();
        arr = s.toCharArray();
        seg = new Node[4 * n];
        build(1, 0, n - 1);
        int q = queryCharacters.length();
        int[] ans = new int[q];
        for (int i = 0; i < q; ++i) {
            int idx = queryIndices[i];
            char c = queryCharacters.charAt(i);
            if (arr[idx] != c) {
                arr[idx] = c;
                update(1, 0, n - 1, idx, c);
            }
            ans[i] = seg[1].best;
        }
        return ans;
    }

    private void build(int node, int l, int r) {
        if (l == r) {
            seg[node] = new Node(arr[l]);
            return;
        }
        int mid = (l + r) >>> 1;
        build(node << 1, l, mid);
        build(node << 1 | 1, mid + 1, r);
        seg[node] = merge(seg[node << 1], seg[node << 1 | 1]);
    }

    private void update(int node, int l, int r, int idx, char c) {
        if (l == r) {
            seg[node] = new Node(c);
            return;
        }
        int mid = (l + r) >>> 1;
        if (idx <= mid) {
            update(node << 1, l, mid, idx, c);
        } else {
            update(node << 1 | 1, mid + 1, r, idx, c);
        }
        seg[node] = merge(seg[node << 1], seg[node << 1 | 1]);
    }

    private Node merge(Node left, Node right) {
        if (left == null) return right;
        if (right == null) return left;
        Node res = new Node();
        res.len = left.len + right.len;
        res.leftChar = left.leftChar;
        res.rightChar = right.rightChar;

        // prefix
        res.pref = left.pref;
        if (left.pref == left.len && left.rightChar == right.leftChar) {
            res.pref = left.len + right.pref;
        }

        // suffix
        res.suff = right.suff;
        if (right.suff == right.len && left.rightChar == right.leftChar) {
            res.suff = right.len + left.suff;
        }

        // best inside children
        res.best = Math.max(left.best, right.best);
        // crossing segment
        if (left.rightChar == right.leftChar) {
            int cross = left.suff + right.pref;
            if (cross > res.best) res.best = cross;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)
        size = 4 * n
        leftc = [''] * size
        rightc = [''] * size
        pref = [0] * size
        suff = [0] * size
        best = [0] * size
        seglen = [0] * size

        def pull(i):
            l = i << 1
            r = l | 1
            seglen[i] = seglen[l] + seglen[r]
            leftc[i] = leftc[l]
            rightc[i] = rightc[r]

            # prefix
            pref[i] = pref[l]
            if pref[l] == seglen[l] and rightc[l] == leftc[r]:
                pref[i] = seglen[l] + pref[r]

            # suffix
            suff[i] = suff[r]
            if suff[r] == seglen[r] and rightc[l] == leftc[r]:
                suff[i] = seglen[r] + suff[l]

            # best
            best[i] = best[l] if best[l] > best[r] else best[r]
            if rightc[l] == leftc[r]:
                cross = suff[l] + pref[r]
                if cross > best[i]:
                    best[i] = cross

        def build(i, l, r):
            if l == r:
                ch = s[l]
                leftc[i] = rightc[i] = ch
                pref[i] = suff[i] = best[i] = 1
                seglen[i] = 1
                return
            m = (l + r) >> 1
            build(i << 1, l, m)
            build(i << 1 | 1, m + 1, r)
            pull(i)

        def update(i, l, r, pos, ch):
            if l == r:
                leftc[i] = rightc[i] = ch
                pref[i] = suff[i] = best[i] = 1
                return
            m = (l + r) >> 1
            if pos <= m:
                update(i << 1, l, m, pos, ch)
            else:
                update(i << 1 | 1, m + 1, r, pos, ch)
            pull(i)

        build(1, 0, n - 1)
        arr = list(s)
        res = []
        for ch, idx in zip(queryCharacters, queryIndices):
            if arr[idx] != ch:
                arr[idx] = ch
                update(1, 0, n - 1, idx, ch)
            res.append(best[1])
        return res
```

## Python3

```python
class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        size = 4 * n
        seg = [None] * size

        def make_node(ch):
            return (ch, ch, 1, 1, 1, 1)  # left_char, right_char, pref, suff, best, length

        def merge(left, right):
            lch, lrc, lpref, lsuff, lbest, llen = left
            rch, rrc, rpref, rsuff, rbest, rlen = right
            # prefix
            if lpref == llen and lrc == rch:
                pref = llen + rpref
            else:
                pref = lpref
            # suffix
            if rsuff == rlen and lrc == rch:
                suff = rlen + lsuff
            else:
                suff = rsuff
            best = max(lbest, rbest)
            if lrc == rch:
                best = max(best, lsuff + rpref)
            return (lch, rrc, pref, suff, best, llen + rlen)

        def build(idx, l, r):
            if l == r:
                seg[idx] = make_node(s[l])
                return
            m = (l + r) // 2
            build(idx * 2, l, m)
            build(idx * 2 + 1, m + 1, r)
            seg[idx] = merge(seg[idx * 2], seg[idx * 2 + 1])

        def update(idx, l, r, pos, ch):
            if l == r:
                seg[idx] = make_node(ch)
                return
            m = (l + r) // 2
            if pos <= m:
                update(idx * 2, l, m, pos, ch)
            else:
                update(idx * 2 + 1, m + 1, r, pos, ch)
            seg[idx] = merge(seg[idx * 2], seg[idx * 2 + 1])

        build(1, 0, n - 1)
        res = []
        s_list = list(s)  # to keep current characters if needed
        for ch, pos in zip(queryCharacters, queryIndices):
            if s_list[pos] != ch:
                s_list[pos] = ch
                update(1, 0, n - 1, pos, ch)
            res.append(seg[1][3])  # best is at index 4, but we stored as (.., best, ..) -> index 4
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char lc;
    char rc;
    int pref;
    int suf;
    int best;
    int len;
} Node;

static Node *seg;

/* Combine left and right child into parent */
static void combine(Node *parent, const Node *left, const Node *right) {
    parent->lc = left->lc;
    parent->rc = right->rc;
    parent->len = left->len + right->len;

    /* prefix */
    parent->pref = left->pref;
    if (left->pref == left->len && left->rc == right->lc) {
        parent->pref = left->len + right->pref;
    }

    /* suffix */
    parent->suf = right->suf;
    if (right->suf == right->len && left->rc == right->lc) {
        parent->suf = right->len + left->suf;
    }

    /* best */
    int best = left->best > right->best ? left->best : right->best;
    if (left->rc == right->lc) {
        int cross = left->suf + right->pref;
        if (cross > best) best = cross;
    }
    parent->best = best;
}

/* Build segment tree */
static void build(int idx, int l, int r, const char *s) {
    if (l == r) {
        seg[idx].lc = seg[idx].rc = s[l];
        seg[idx].pref = seg[idx].suf = seg[idx].best = 1;
        seg[idx].len = 1;
        return;
    }
    int mid = (l + r) >> 1;
    build(idx << 1, l, mid, s);
    build(idx << 1 | 1, mid + 1, r, s);
    combine(&seg[idx], &seg[idx << 1], &seg[idx << 1 | 1]);
}

/* Point update */
static void update(int idx, int l, int r, int pos, char ch) {
    if (l == r) {
        seg[idx].lc = seg[idx].rc = ch;
        seg[idx].pref = seg[idx].suf = seg[idx].best = 1;
        return;
    }
    int mid = (l + r) >> 1;
    if (pos <= mid)
        update(idx << 1, l, mid, pos, ch);
    else
        update(idx << 1 | 1, mid + 1, r, pos, ch);
    combine(&seg[idx], &seg[idx << 1], &seg[idx << 1 | 1]);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* longestRepeating(char* s, char* queryCharacters, int* queryIndices, int queryIndicesSize, int* returnSize) {
    int n = (int)strlen(s);
    seg = (Node *)malloc(sizeof(Node) * 4 * n);
    build(1, 0, n - 1, s);

    int *ans = (int *)malloc(sizeof(int) * queryIndicesSize);
    for (int i = 0; i < queryIndicesSize; ++i) {
        int pos = queryIndices[i];
        char ch = queryCharacters[i];
        if (s[pos] != ch) {
            s[pos] = ch;
            update(1, 0, n - 1, pos, ch);
        }
        ans[i] = seg[1].best;
    }

    free(seg);
    *returnSize = queryIndicesSize;
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    private struct Node {
        public char left;
        public char right;
        public int pref;
        public int suff;
        public int best;
        public int len;
    }

    private Node[] seg;
    private int n;

    private Node Merge(Node a, Node b) {
        if (a.len == 0) return b;
        if (b.len == 0) return a;
        Node res = new Node();
        res.len = a.len + b.len;
        res.left = a.left;
        res.right = b.right;

        // prefix
        res.pref = a.pref;
        if (a.pref == a.len && a.right == b.left) {
            res.pref = a.len + b.pref;
        }

        // suffix
        res.suff = b.suff;
        if (b.suff == b.len && a.right == b.left) {
            res.suff = b.len + a.suff;
        }

        // best
        res.best = Math.Max(a.best, b.best);
        if (a.right == b.left) {
            int combined = a.suff + b.pref;
            if (combined > res.best) res.best = combined;
        }
        return res;
    }

    private void Build(int idx, int l, int r, char[] arr) {
        if (l == r) {
            char c = arr[l];
            seg[idx] = new Node { left = c, right = c, pref = 1, suff = 1, best = 1, len = 1 };
            return;
        }
        int mid = (l + r) >> 1;
        Build(idx << 1, l, mid, arr);
        Build(idx << 1 | 1, mid + 1, r, arr);
        seg[idx] = Merge(seg[idx << 1], seg[idx << 1 | 1]);
    }

    private void Update(int idx, int l, int r, int pos, char c) {
        if (l == r) {
            seg[idx] = new Node { left = c, right = c, pref = 1, suff = 1, best = 1, len = 1 };
            return;
        }
        int mid = (l + r) >> 1;
        if (pos <= mid) Update(idx << 1, l, mid, pos, c);
        else Update(idx << 1 | 1, mid + 1, r, pos, c);
        seg[idx] = Merge(seg[idx << 1], seg[idx << 1 | 1]);
    }

    public int[] LongestRepeating(string s, string queryCharacters, int[] queryIndices) {
        n = s.Length;
        seg = new Node[4 * n];
        char[] arr = s.ToCharArray();
        Build(1, 0, n - 1, arr);

        int k = queryCharacters.Length;
        int[] ans = new int[k];

        for (int i = 0; i < k; i++) {
            int pos = queryIndices[i];
            char c = queryCharacters[i];
            if (arr[pos] != c) {
                arr[pos] = c;
                Update(1, 0, n - 1, pos, c);
            }
            ans[i] = seg[1].best;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} queryCharacters
 * @param {number[]} queryIndices
 * @return {number[]}
 */
var longestRepeating = function(s, queryCharacters, queryIndices) {
    const n = s.length;
    const arr = s.split('');
    const tree = new Array(4 * n);

    function combine(left, right) {
        if (!left) return right;
        if (!right) return left;
        const node = {};
        node.len = left.len + right.len;
        node.leftChar = left.leftChar;
        node.rightChar = right.rightChar;

        // prefix
        node.pref = left.pref;
        if (left.pref === left.len && left.rightChar === right.leftChar) {
            node.pref = left.len + right.pref;
        }

        // suffix
        node.suff = right.suff;
        if (right.suff === right.len && left.rightChar === right.leftChar) {
            node.suff = right.len + left.suff;
        }

        // best
        node.best = Math.max(left.best, right.best);
        if (left.rightChar === right.leftChar) {
            node.best = Math.max(node.best, left.suff + right.pref);
        }
        return node;
    }

    function build(idx, l, r) {
        if (l === r) {
            const ch = arr[l];
            tree[idx] = { leftChar: ch, rightChar: ch, pref: 1, suff: 1, best: 1, len: 1 };
            return;
        }
        const mid = (l + r) >> 1;
        build(idx << 1, l, mid);
        build((idx << 1) | 1, mid + 1, r);
        tree[idx] = combine(tree[idx << 1], tree[(idx << 1) | 1]);
    }

    function update(idx, l, r, pos, ch) {
        if (l === r) {
            arr[pos] = ch;
            tree[idx] = { leftChar: ch, rightChar: ch, pref: 1, suff: 1, best: 1, len: 1 };
            return;
        }
        const mid = (l + r) >> 1;
        if (pos <= mid) update(idx << 1, l, mid, pos, ch);
        else update((idx << 1) | 1, mid + 1, r, pos, ch);
        tree[idx] = combine(tree[idx << 1], tree[(idx << 1) | 1]);
    }

    build(1, 0, n - 1);

    const m = queryCharacters.length;
    const result = new Array(m);
    for (let i = 0; i < m; ++i) {
        const pos = queryIndices[i];
        const ch = queryCharacters[i];
        if (arr[pos] !== ch) update(1, 0, n - 1, pos, ch);
        result[i] = tree[1].best;
    }
    return result;
};
```

## Typescript

```typescript
function longestRepeating(s: string, queryCharacters: string, queryIndices: number[]): number[] {
    const n = s.length;
    interface Node {
        leftChar: string;
        rightChar: string;
        pref: number;
        suff: number;
        best: number;
        len: number;
    }
    const tree: Node[] = new Array(4 * n);

    function makeNode(ch: string): Node {
        return { leftChar: ch, rightChar: ch, pref: 1, suff: 1, best: 1, len: 1 };
    }

    function merge(a: Node, b: Node): Node {
        const res: Node = {
            leftChar: a.leftChar,
            rightChar: b.rightChar,
            pref: a.pref,
            suff: b.suff,
            best: Math.max(a.best, b.best),
            len: a.len + b.len
        };
        // prefix
        if (a.pref === a.len && a.rightChar === b.leftChar) {
            res.pref = a.len + b.pref;
        } else {
            res.pref = a.pref;
        }
        // suffix
        if (b.suff === b.len && a.rightChar === b.leftChar) {
            res.suff = b.len + a.suff;
        } else {
            res.suff = b.suff;
        }
        // crossing segment
        if (a.rightChar === b.leftChar) {
            const cross = a.suff + b.pref;
            if (cross > res.best) res.best = cross;
        }
        return res;
    }

    function build(idx: number, l: number, r: number): void {
        if (l === r) {
            tree[idx] = makeNode(s.charAt(l));
            return;
        }
        const mid = (l + r) >> 1;
        build(idx << 1, l, mid);
        build(idx << 1 | 1, mid + 1, r);
        tree[idx] = merge(tree[idx << 1], tree[idx << 1 | 1]);
    }

    function update(idx: number, l: number, r: number, pos: number, ch: string): void {
        if (l === r) {
            tree[idx] = makeNode(ch);
            return;
        }
        const mid = (l + r) >> 1;
        if (pos <= mid) update(idx << 1, l, mid, pos, ch);
        else update(idx << 1 | 1, mid + 1, r, pos, ch);
        tree[idx] = merge(tree[idx << 1], tree[idx << 1 | 1]);
    }

    build(1, 0, n - 1);

    const res: number[] = [];
    for (let i = 0; i < queryIndices.length; ++i) {
        const pos = queryIndices[i];
        const ch = queryCharacters.charAt(i);
        update(1, 0, n - 1, pos, ch);
        res.push(tree[1].best);
    }
    return res;
}
```

## Php

```php
class Solution {
    private $tree = [];
    private $n;

    private function merge(array $a, array $b): array {
        $len = $a[5] + $b[5];
        $leftChar = $a[0];
        $rightChar = $b[1];

        // prefix
        $prefLen = $a[2];
        if ($a[2] == $a[5] && $a[1] === $b[0]) {
            $prefLen = $a[5] + $b[2];
        }

        // suffix
        $suffLen = $b[3];
        if ($b[3] == $b[5] && $a[1] === $b[0]) {
            $suffLen = $b[5] + $a[3];
        }

        // best
        $best = max($a[4], $b[4]);
        if ($a[1] === $b[0]) {
            $best = max($best, $a[3] + $b[2]);
        }

        return [$leftChar, $rightChar, $prefLen, $suffLen, $best, $len];
    }

    private function build(int $idx, int $l, int $r, string $s): void {
        if ($l === $r) {
            $c = ord($s[$l]) - 97;
            $this->tree[$idx] = [$c, $c, 1, 1, 1, 1];
            return;
        }
        $mid = intdiv($l + $r, 2);
        $this->build($idx * 2, $l, $mid, $s);
        $this->build($idx * 2 + 1, $mid + 1, $r, $s);
        $this->tree[$idx] = $this->merge($this->tree[$idx * 2], $this->tree[$idx * 2 + 1]);
    }

    private function update(int $idx, int $l, int $r, int $pos, int $charCode): void {
        if ($l === $r) {
            $c = $charCode;
            $this->tree[$idx] = [$c, $c, 1, 1, 1, 1];
            return;
        }
        $mid = intdiv($l + $r, 2);
        if ($pos <= $mid) {
            $this->update($idx * 2, $l, $mid, $pos, $charCode);
        } else {
            $this->update($idx * 2 + 1, $mid + 1, $r, $pos, $charCode);
        }
        $this->tree[$idx] = $this->merge($this->tree[$idx * 2], $this->tree[$idx * 2 + 1]);
    }

    /**
     * @param String $s
     * @param String $queryCharacters
     * @param Integer[] $queryIndices
     * @return Integer[]
     */
    function longestRepeating($s, $queryCharacters, $queryIndices) {
        $this->n = strlen($s);
        $this->tree = array_fill(0, 4 * $this->n, null);
        $this->build(1, 0, $this->n - 1, $s);

        $k = strlen($queryCharacters);
        $result = [];

        for ($i = 0; $i < $k; ++$i) {
            $pos = $queryIndices[$i];
            $charCode = ord($queryCharacters[$i]) - 97;
            $this->update(1, 0, $this->n - 1, $pos, $charCode);
            $result[] = $this->tree[1][4]; // best length at root
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    struct Node {
        var lChar: Int
        var rChar: Int
        var pref: Int
        var suff: Int
        var best: Int
        var len: Int
    }
    
    private var seg: [Node] = []
    
    private func merge(_ a: Node, _ b: Node) -> Node {
        var res = Node(lChar: a.lChar,
                       rChar: b.rChar,
                       pref: 0,
                       suff: 0,
                       best: 0,
                       len: a.len + b.len)
        
        // prefix
        if a.pref == a.len && a.rChar == b.lChar {
            res.pref = a.len + b.pref
        } else {
            res.pref = a.pref
        }
        // suffix
        if b.suff == b.len && a.rChar == b.lChar {
            res.suff = b.len + a.suff
        } else {
            res.suff = b.suff
        }
        // best
        var bestVal = max(a.best, b.best)
        if a.rChar == b.lChar {
            bestVal = max(bestVal, a.suff + b.pref)
        }
        res.best = bestVal
        return res
    }
    
    private func build(_ idx: Int, _ l: Int, _ r: Int, _ arr: [Int]) {
        if l == r {
            let c = arr[l]
            seg[idx] = Node(lChar: c, rChar: c, pref: 1, suff: 1, best: 1, len: 1)
            return
        }
        let mid = (l + r) >> 1
        build(idx << 1, l, mid, arr)
        build(idx << 1 | 1, mid + 1, r, arr)
        seg[idx] = merge(seg[idx << 1], seg[idx << 1 | 1])
    }
    
    private func update(_ idx: Int, _ l: Int, _ r: Int, _ pos: Int, _ val: Int) {
        if l == r {
            seg[idx] = Node(lChar: val, rChar: val, pref: 1, suff: 1, best: 1, len: 1)
            return
        }
        let mid = (l + r) >> 1
        if pos <= mid {
            update(idx << 1, l, mid, pos, val)
        } else {
            update(idx << 1 | 1, mid + 1, r, pos, val)
        }
        seg[idx] = merge(seg[idx << 1], seg[idx << 1 | 1])
    }
    
    func longestRepeating(_ s: String, _ queryCharacters: String, _ queryIndices: [Int]) -> [Int] {
        let n = s.count
        var arr = [Int]()
        arr.reserveCapacity(n)
        for ch in s.utf8 {
            arr.append(Int(ch - 97))
        }
        
        var qVals = [Int]()
        qVals.reserveCapacity(queryCharacters.count)
        for ch in queryCharacters.utf8 {
            qVals.append(Int(ch - 97))
        }
        
        seg = [Node](repeating: Node(lChar: 0, rChar: 0, pref: 0, suff: 0, best: 0, len: 0), count: 4 * n)
        build(1, 0, n - 1, arr)
        
        var ans = [Int]()
        ans.reserveCapacity(queryIndices.count)
        for i in 0..<queryIndices.count {
            let pos = queryIndices[i]
            let val = qVals[i]
            update(1, 0, n - 1, pos, val)
            ans.append(seg[1].best)
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestRepeating(s: String, queryCharacters: String, queryIndices: IntArray): IntArray {
        val n = s.length
        val tree = Array(4 * n) { Node() }

        fun build(node: Int, l: Int, r: Int) {
            if (l == r) {
                val c = s[l]
                val nd = tree[node]
                nd.leftChar = c
                nd.rightChar = c
                nd.prefLen = 1
                nd.suffLen = 1
                nd.best = 1
                nd.len = 1
                return
            }
            val mid = (l + r) / 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            merge(node, node * 2, node * 2 + 1)
        }

        fun merge(parent: Int, leftIdx: Int, rightIdx: Int) {
            val left = tree[leftIdx]
            val right = tree[rightIdx]
            val p = tree[parent]

            p.len = left.len + right.len
            p.leftChar = left.leftChar
            p.rightChar = right.rightChar

            // prefix length
            p.prefLen = if (left.prefLen == left.len && left.rightChar == right.leftChar) {
                left.len + right.prefLen
            } else {
                left.prefLen
            }

            // suffix length
            p.suffLen = if (right.suffLen == right.len && left.rightChar == right.leftChar) {
                right.len + left.suffLen
            } else {
                right.suffLen
            }

            var bestVal = maxOf(left.best, right.best)
            if (left.rightChar == right.leftChar) {
                bestVal = maxOf(bestVal, left.suffLen + right.prefLen)
            }
            p.best = bestVal
        }

        fun update(node: Int, l: Int, r: Int, pos: Int, ch: Char) {
            if (l == r) {
                val nd = tree[node]
                nd.leftChar = ch
                nd.rightChar = ch
                nd.prefLen = 1
                nd.suffLen = 1
                nd.best = 1
                nd.len = 1
                return
            }
            val mid = (l + r) / 2
            if (pos <= mid) update(node * 2, l, mid, pos, ch) else update(node * 2 + 1, mid + 1, r, pos, ch)
            merge(node, node * 2, node * 2 + 1)
        }

        build(1, 0, n - 1)

        val k = queryCharacters.length
        val ans = IntArray(k)
        for (i in 0 until k) {
            val idx = queryIndices[i]
            val ch = queryCharacters[i]
            update(1, 0, n - 1, idx, ch)
            ans[i] = tree[1].best
        }
        return ans
    }

    private class Node {
        var leftChar: Char = 0.toChar()
        var rightChar: Char = 0.toChar()
        var prefLen: Int = 0
        var suffLen: Int = 0
        var best: Int = 0
        var len: Int = 0
    }
}
```

## Dart

```dart
class Node {
  int leftChar;
  int rightChar;
  int pref;
  int suff;
  int best;
  int len;
  Node(this.leftChar, this.rightChar, this.pref, this.suff, this.best, this.len);
  Node.empty()
      : leftChar = -1,
        rightChar = -1,
        pref = 0,
        suff = 0,
        best = 0,
        len = 0;
}

class Solution {
  List<int> longestRepeating(String s, String queryCharacters, List<int> queryIndices) {
    int n = s.length;
    List<int> chars = s.codeUnits;
    List<Node> seg = List<Node>.filled(4 * n, Node.empty());

    Node leaf(int ch) => Node(ch, ch, 1, 1, 1, 1);

    Node merge(Node a, Node b) {
      if (a.len == 0) return b;
      if (b.len == 0) return a;
      int leftChar = a.leftChar;
      int rightChar = b.rightChar;

      int pref = a.pref;
      if (a.pref == a.len && a.rightChar == b.leftChar) {
        pref = a.len + b.pref;
      }

      int suff = b.suff;
      if (b.suff == b.len && a.rightChar == b.leftChar) {
        suff = b.len + a.suff;
      }

      int best = a.best > b.best ? a.best : b.best;
      if (a.rightChar == b.leftChar) {
        int cross = a.suff + b.pref;
        if (cross > best) best = cross;
      }

      return Node(leftChar, rightChar, pref, suff, best, a.len + b.len);
    }

    void build(int idx, int l, int r) {
      if (l == r) {
        seg[idx] = leaf(chars[l]);
        return;
      }
      int mid = (l + r) >> 1;
      build(idx << 1, l, mid);
      build((idx << 1) | 1, mid + 1, r);
      seg[idx] = merge(seg[idx << 1], seg[(idx << 1) | 1]);
    }

    void update(int idx, int l, int r, int pos, int ch) {
      if (l == r) {
        seg[idx] = leaf(ch);
        return;
      }
      int mid = (l + r) >> 1;
      if (pos <= mid) {
        update(idx << 1, l, mid, pos, ch);
      } else {
        update((idx << 1) | 1, mid + 1, r, pos, ch);
      }
      seg[idx] = merge(seg[idx << 1], seg[(idx << 1) | 1]);
    }

    build(1, 0, n - 1);

    int q = queryCharacters.length;
    List<int> result = List<int>.filled(q, 0);
    for (int i = 0; i < q; ++i) {
      int pos = queryIndices[i];
      int newChar = queryCharacters.codeUnitAt(i);
      update(1, 0, n - 1, pos, newChar);
      result[i] = seg[1].best;
    }
    return result;
  }
}
```

## Golang

```go
func longestRepeating(s string, queryCharacters string, queryIndices []int) []int {
	type Node struct {
		leftChar byte
		rightChar byte
		pref int
		suff int
		best int
		length int
	}
	n := len(s)
	tree := make([]Node, 4*n)

	var build func(idx, l, r int)
	build = func(idx, l, r int) {
		if l == r {
			c := s[l]
			tree[idx] = Node{
				leftChar: c,
				rightChar: c,
				pref: 1,
				suff: 1,
				best: 1,
				length: 1,
			}
			return
		}
		mid := (l + r) >> 1
		build(idx<<1, l, mid)
		build(idx<<1|1, mid+1, r)
		tree[idx] = merge(tree[idx<<1], tree[idx<<1|1])
	}

	merge := func(a, b Node) Node {
		if a.length == 0 {
			return b
		}
		if b.length == 0 {
			return a
		}
		res := Node{
			leftChar: a.leftChar,
			rightChar: b.rightChar,
			length: a.length + b.length,
		}
		// prefix
		res.pref = a.pref
		if a.pref == a.length && a.rightChar == b.leftChar {
			res.pref = a.length + b.pref
		}
		// suffix
		res.suff = b.suff
		if b.suff == b.length && a.rightChar == b.leftChar {
			res.suff = b.length + a.suff
		}
		// best
		res.best = a.best
		if b.best > res.best {
			res.best = b.best
		}
		if a.rightChar == b.leftChar {
			combined := a.suff + b.pref
			if combined > res.best {
				res.best = combined
			}
		}
		return res
	}

	var update func(idx, l, r, pos int, ch byte)
	update = func(idx, l, r, pos int, ch byte) {
		if l == r {
			tree[idx] = Node{
				leftChar: ch,
				rightChar: ch,
				pref: 1,
				suff: 1,
				best: 1,
				length: 1,
			}
			return
		}
		mid := (l + r) >> 1
		if pos <= mid {
			update(idx<<1, l, mid, pos, ch)
		} else {
			update(idx<<1|1, mid+1, r, pos, ch)
		}
		tree[idx] = merge(tree[idx<<1], tree[idx<<1|1])
	}

	build(1, 0, n-1)

	k := len(queryIndices)
	ans := make([]int, k)
	for i := 0; i < k; i++ {
		pos := queryIndices[i]
		ch := queryCharacters[i]
		update(1, 0, n-1, pos, ch)
		ans[i] = tree[1].best
	}
	return ans
}
```

## Ruby

```ruby
def longest_repeating(s, query_characters, query_indices)
  n = s.length
  size = 4 * n
  lc = Array.new(size)   # leftmost character (byte)
  rc = Array.new(size)   # rightmost character (byte)
  pref = Array.new(size) # longest prefix of same char
  suff = Array.new(size) # longest suffix of same char
  best = Array.new(size) # longest uniform substring in segment
  seg_len = Array.new(size)

  build = nil
  pull = nil
  update = nil

  pull = lambda do |node|
    left = node * 2
    right = node * 2 + 1

    lc[node] = lc[left]
    rc[node] = rc[right]
    seg_len[node] = seg_len[left] + seg_len[right]

    # prefix
    pref[node] = pref[left]
    if pref[left] == seg_len[left] && rc[left] == lc[right]
      pref[node] = seg_len[left] + pref[right]
    end

    # suffix
    suff[node] = suff[right]
    if suff[right] == seg_len[right] && rc[left] == lc[right]
      suff[node] = seg_len[right] + suff[left]
    end

    # best
    cur_best = best[left] > best[right] ? best[left] : best[right]
    if rc[left] == lc[right]
      combined = suff[left] + pref[right]
      cur_best = combined if combined > cur_best
    end
    best[node] = cur_best
  end

  build = lambda do |node, l, r|
    if l == r
      ch = s.getbyte(l)
      lc[node] = rc[node] = ch
      pref[node] = suff[node] = best[node] = 1
      seg_len[node] = 1
    else
      mid = (l + r) / 2
      build.call(node * 2, l, mid)
      build.call(node * 2 + 1, mid + 1, r)
      pull.call(node)
    end
  end

  update = lambda do |node, l, r, idx, ch|
    if l == r
      lc[node] = rc[node] = ch
      pref[node] = suff[node] = best[node] = 1
      seg_len[node] = 1
    else
      mid = (l + r) / 2
      if idx <= mid
        update.call(node * 2, l, mid, idx, ch)
      else
        update.call(node * 2 + 1, mid + 1, r, idx, ch)
      end
      pull.call(node)
    end
  end

  build.call(1, 0, n - 1)

  res = []
  k = query_indices.length
  (0...k).each do |i|
    idx = query_indices[i]
    ch_byte = query_characters[i].ord
    update.call(1, 0, n - 1, idx, ch_byte)
    res << best[1]
  end
  res
end
```

## Scala

```scala
object Solution {
  case class Node(len: Int, leftChar: Char, rightChar: Char, pref: Int, suff: Int, best: Int)

  def longestRepeating(s: String, queryCharacters: String, queryIndices: Array[Int]): Array[Int] = {
    val n = s.length
    val q = queryCharacters.length
    val res = new Array[Int](q)
    if (n == 0) return res

    val tree = new Array[Node](4 * n)

    def merge(a: Node, b: Node): Node = {
      if (a.len == 0) return b
      if (b.len == 0) return a
      val leftChar = a.leftChar
      val rightChar = b.rightChar
      val pref = if (a.pref == a.len && a.rightChar == b.leftChar) a.len + b.pref else a.pref
      val suff = if (b.suff == b.len && a.rightChar == b.leftChar) b.len + a.suff else b.suff
      var bestVal = math.max(a.best, b.best)
      if (a.rightChar == b.leftChar) {
        bestVal = math.max(bestVal, a.suff + b.pref)
      }
      Node(a.len + b.len, leftChar, rightChar, pref, suff, bestVal)
    }

    def build(idx: Int, l: Int, r: Int): Unit = {
      if (l == r) {
        val c = s.charAt(l)
        tree(idx) = Node(1, c, c, 1, 1, 1)
      } else {
        val mid = (l + r) >>> 1
        build(idx << 1, l, mid)
        build(idx << 1 | 1, mid + 1, r)
        tree(idx) = merge(tree(idx << 1), tree(idx << 1 | 1))
      }
    }

    def update(idx: Int, l: Int, r: Int, pos: Int, ch: Char): Unit = {
      if (l == r) {
        tree(idx) = Node(1, ch, ch, 1, 1, 1)
      } else {
        val mid = (l + r) >>> 1
        if (pos <= mid) update(idx << 1, l, mid, pos, ch)
        else update(idx << 1 | 1, mid + 1, r, pos, ch)
        tree(idx) = merge(tree(idx << 1), tree(idx << 1 | 1))
      }
    }

    build(1, 0, n - 1)

    var i = 0
    while (i < q) {
      val pos = queryIndices(i)
      val ch = queryCharacters.charAt(i)
      update(1, 0, n - 1, pos, ch)
      res(i) = tree(1).best
      i += 1
    }

    res
  }
}
```

## Rust

```rust
use std::cmp::max;

#[derive(Clone, Copy)]
struct Node {
    left: u8,
    right: u8,
    pref: usize,
    suff: usize,
    best: usize,
    len: usize,
}

impl Node {
    fn new(c: u8) -> Self {
        Node {
            left: c,
            right: c,
            pref: 1,
            suff: 1,
            best: 1,
            len: 1,
        }
    }

    fn empty() -> Self {
        Node {
            left: b' ',
            right: b' ',
            pref: 0,
            suff: 0,
            best: 0,
            len: 0,
        }
    }
}

struct SegTree {
    n: usize,
    tree: Vec<Node>,
}

impl SegTree {
    fn new(s: &String) -> Self {
        let n = s.len();
        let mut seg = SegTree {
            n,
            tree: vec![Node::empty(); 4 * n + 5],
        };
        let bytes = s.as_bytes();
        seg.build(1, 0, n - 1, bytes);
        seg
    }

    fn build(&mut self, idx: usize, l: usize, r: usize, arr: &[u8]) {
        if l == r {
            self.tree[idx] = Node::new(arr[l]);
            return;
        }
        let mid = (l + r) / 2;
        self.build(idx * 2, l, mid, arr);
        self.build(idx * 2 + 1, mid + 1, r, arr);
        self.pull(idx);
    }

    fn pull(&mut self, idx: usize) {
        let left = self.tree[idx * 2];
        let right = self.tree[idx * 2 + 1];

        if left.len == 0 {
            self.tree[idx] = right;
            return;
        }
        if right.len == 0 {
            self.tree[idx] = left;
            return;
        }

        let len = left.len + right.len;

        // prefix
        let pref = if left.pref == left.len && left.right == right.left {
            left.len + right.pref
        } else {
            left.pref
        };

        // suffix
        let suff = if right.suff == right.len && left.right == right.left {
            right.len + left.suff
        } else {
            right.suff
        };

        // best inside
        let mut best = max(left.best, right.best);
        if left.right == right.left {
            best = max(best, left.suff + right.pref);
        }

        self.tree[idx] = Node {
            left: left.left,
            right: right.right,
            pref,
            suff,
            best,
            len,
        };
    }

    fn update(&mut self, pos: usize, val: u8) {
        self.update_rec(1, 0, self.n - 1, pos, val);
    }

    fn update_rec(&mut self, idx: usize, l: usize, r: usize, pos: usize, val: u8) {
        if l == r {
            self.tree[idx] = Node::new(val);
            return;
        }
        let mid = (l + r) / 2;
        if pos <= mid {
            self.update_rec(idx * 2, l, mid, pos, val);
        } else {
            self.update_rec(idx * 2 + 1, mid + 1, r, pos, val);
        }
        self.pull(idx);
    }

    fn root_best(&self) -> usize {
        self.tree[1].best
    }
}

impl Solution {
    pub fn longest_repeating(s: String, query_characters: String, query_indices: Vec<i32>) -> Vec<i32> {
        let mut seg = SegTree::new(&s);
        let chars: Vec<char> = query_characters.chars().collect();
        let mut ans = Vec::with_capacity(query_indices.len());
        for (c, &idx_i) in chars.iter().zip(query_indices.iter()) {
            let idx = idx_i as usize;
            seg.update(idx, *c as u8);
            ans.push(seg.root_best() as i32);
        }
        ans
    }
}
```

## Racket

```racket
(define-struct node (len lch rch pref suff best) #:transparent)

;; create a leaf node for a single character
(define (make-leaf ch)
  (make-node 1 ch ch 1 1 1))

;; zero-length node used for padding
(define zero-node (make-node 0 #\a #\a 0 0 0))

;; merge two nodes
(define (merge-nodes left right)
  (cond [(= (node-len left) 0) right]
        [(= (node-len right) 0) left]
        [else
         (let* ((len (+ (node-len left) (node-len right)))
                (lch (node-lch left))
                (rch (node-rch right))
                (pref (if (and (= (node-pref left) (node-len left))
                               (char=? (node-rch left) (node-lch right)))
                          (+ (node-len left) (node-pref right))
                          (node-pref left)))
                (suff (if (and (= (node-suff right) (node-len right))
                               (char=? (node-rch left) (node-lch right)))
                          (+ (node-suff left) (node-len right))
                          (node-suff right)))
                (mid-best (if (char=? (node-rch left) (node-lch right))
                              (+ (node-suff left) (node-pref right))
                              0))
                (best (max (node-best left) (node-best right) mid-best)))
           (make-node len lch rch pref suff best))])))

;; compute next power of two >= x
(define (next-power-of-two x)
  (let loop ((p 1))
    (if (>= p x) p (loop (* p 2)))))

(define (longest-repeating s queryCharacters queryIndices)
  (let* ((n (string-length s))
         (base (next-power-of-two n))
         (cur-vec (list->vector
                    (for/list ([i (in-range n)]) (string-ref s i))))
         (tree (make-vector (* 2 base) zero-node)))
    ;; initialize leaves
    (for ([i (in-range n)])
      (vector-set! tree (+ base i) (make-leaf (vector-ref cur-vec i))))
    ;; build internal nodes
    (for ([i (in-range (sub1 base) 0 -1)])
      (vector-set! tree i
        (merge-nodes (vector-ref tree (* i 2))
                     (vector-ref tree (+ (* i 2) 1)))))
    ;; point update (iterative)
    (define (point-update pos new-ch)
      (let ((idx (+ base pos)))
        (vector-set! cur-vec pos new-ch)
        (vector-set! tree idx (make-leaf new-ch))
        (let loop ((i (quotient idx 2)))
          (when (> i 0)
            (vector-set! tree i
              (merge-nodes (vector-ref tree (* i 2))
                           (vector-ref tree (+ (* i 2) 1))))
            (loop (quotient i 2))))))
    ;; process queries
    (let* ((k (string-length queryCharacters))
           (q-idx-vec (list->vector queryIndices))
           (answers (make-vector k)))
      (for ([i (in-range k)])
        (let ((pos (vector-ref q-idx-vec i))
              (ch  (string-ref queryCharacters i)))
          (point-update pos ch)
          (vector-set! answers i (node-best (vector-ref tree 1)))))
      (vector->list answers))))
```

## Erlang

```erlang
-spec longest_repeating(S :: unicode:unicode_binary(), QueryCharacters :: unicode:unicode_binary(), QueryIndices :: [integer()]) -> [integer()].
longest_repeating(S, QueryCharacters, QueryIndices) ->
    Len = byte_size(S),
    Tree0 = build(S, 0, Len - 1),
    QCharsList = binary_to_list(QueryCharacters),
    process_queries(QCharsList, QueryIndices, Tree0, Len, []).

%% Build segment tree from string S in range [L,R]
build(_S, L, R) when L > R ->
    {undefined, undefined, undefined};
build(S, L, R) when L == R ->
    Char = binary:at(S, L),
    Node = #{len => 1,
             left => Char,
             right => Char,
             pref => 1,
             suff => 1,
             best => 1},
    {Node, undefined, undefined};
build(S, L, R) ->
    Mid = (L + R) div 2,
    LeftTree = build(S, L, Mid),
    RightTree = build(S, Mid + 1, R),
    Node = merge(node(LeftTree), node(RightTree)),
    {Node, LeftTree, RightTree}.

%% Process all queries recursively
process_queries([], [], _Tree, _Len, Acc) ->
    lists:reverse(Acc);
process_queries([Char|RestChars], [Idx|RestIdxs], Tree, Len, Acc) ->
    NewTree = update(Tree, 0, Len - 1, Idx, Char),
    Best = maps:get(best, node(NewTree)),
    process_queries(RestChars, RestIdxs, NewTree, Len, [Best | Acc]).

%% Update character at position Index to Char
update({Node, Left, Right}, L, R, Index, Char) when L == R ->
    NewNode = #{len => 1,
                left => Char,
                right => Char,
                pref => 1,
                suff => 1,
                best => 1},
    {NewNode, undefined, undefined};
update({Node, Left, Right}, L, R, Index, Char) ->
    Mid = (L + R) div 2,
    if
        Index =< Mid ->
            NewLeft = update(Left, L, Mid, Index, Char),
            NewRight = Right;
        true ->
            NewLeft = Left,
            NewRight = update(Right, Mid + 1, R, Index, Char)
    end,
    NewNode = merge(node(NewLeft), node(NewRight)),
    {NewNode, NewLeft, NewRight}.

%% Merge two nodes into a parent node
merge(N1, N2) ->
    Len = N1.len + N2.len,
    LeftChar = N1.left,
    RightChar = N2.right,
    Pref = case (N1.pref == N1.len) andalso (N1.right == N2.left) of
               true -> N1.len + N2.pref;
               false -> N1.pref
           end,
    Suff = case (N2.suff == N2.len) andalso (N1.right == N2.left) of
               true -> N2.len + N1.suff;
               false -> N2.suff
           end,
    Cross = if N1.right == N2.left -> N1.suff + N2.pref; true -> 0 end,
    Best = erlang:max(N1.best, erlang:max(N2.best, Cross)),
    #{len => Len,
      left => LeftChar,
      right => RightChar,
      pref => Pref,
      suff => Suff,
      best => Best}.

%% Helper to extract node map from tree tuple
node({Node, _Left, _Right}) -> Node.
```

## Elixir

```elixir
defmodule Solution do
  defmodule Node do
    defstruct [:l, :r, :left_c, :right_c, :pref, :suff, :best, :len, :left, :right]
  end

  @spec longest_repeating(String.t(), String.t(), [integer]) :: [integer]
  def longest_repeating(s, query_characters, query_indices) do
    arr = String.to_charlist(s)
    n = length(arr)

    root = build(arr, 0, n - 1)

    q_chars = String.to_charlist(query_characters)

    {answers_rev, _} =
      Enum.reduce(Enum.zip(q_chars, query_indices), {[], root}, fn {ch, idx},
                                                                   {acc, cur_root} ->
        new_root = update(cur_root, idx, ch)
        {[new_root.best | acc], new_root}
      end)

    Enum.reverse(answers_rev)
  end

  defp build(arr, l, r) do
    if l == r do
      c = Enum.at(arr, l)

      %Node{
        l: l,
        r: r,
        left_c: c,
        right_c: c,
        pref: 1,
        suff: 1,
        best: 1,
        len: 1,
        left: nil,
        right: nil
      }
    else
      mid = div(l + r, 2)
      left = build(arr, l, mid)
      right = build(arr, mid + 1, r)
      merge(left, right)
    end
  end

  defp merge(left, right) do
    len = left.len + right.len
    left_c = left.left_c
    right_c = right.right_c

    pref =
      if left.pref == left.len and left.right_c == right.left_c do
        left.len + right.pref
      else
        left.pref
      end

    suff =
      if right.suff == right.len and left.right_c == right.left_c do
        right.len + left.suff
      else
        right.suff
      end

    cross = if left.right_c == right.left_c, do: left.suff + right.pref, else: 0
    best = Enum.max([left.best, right.best, cross])

    %Node{
      l: left.l,
      r: right.r,
      left_c: left_c,
      right_c: right_c,
      pref: pref,
      suff: suff,
      best: best,
      len: len,
      left: left,
      right: right
    }
  end

  defp update(node, idx, new_c) do
    if node.l == node.r do
      %Node{node | left_c: new_c, right_c: new_c}
    else
      {new_left, new_right} =
        if idx <= node.left.r do
          {update(node.left, idx, new_c), node.right}
        else
          {node.left, update(node.right, idx, new_c)}
        end

      merge(new_left, new_right)
    end
  end
end
```
