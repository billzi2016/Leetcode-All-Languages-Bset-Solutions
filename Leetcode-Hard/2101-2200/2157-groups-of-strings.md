# 2157. Groups of Strings

## Cpp

```cpp
class Solution {
public:
    struct DSU {
        vector<int> parent;
        vector<int> sz;
        DSU(int n) : parent(n), sz(n, 1) {
            iota(parent.begin(), parent.end(), 0);
        }
        int find(int x) {
            return parent[x] == x ? x : parent[x] = find(parent[x]);
        }
        void unite(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return;
            if (sz[a] < sz[b]) swap(a, b);
            parent[b] = a;
            sz[a] += sz[b];
        }
    };
    
    vector<int> groupStrings(vector<string>& words) {
        int n = words.size();
        vector<int> masks(n);
        unordered_map<int,int> mp; // mask -> first index
        mp.reserve(n * 2);
        DSU dsu(n);
        
        for (int i = 0; i < n; ++i) {
            int m = 0;
            for (char c : words[i]) m |= 1 << (c - 'a');
            masks[i] = m;
            auto it = mp.find(m);
            if (it != mp.end()) {
                dsu.unite(i, it->second); // duplicate strings
            } else {
                mp[m] = i;
            }
        }
        
        const int ALL = 1 << 26;
        for (const auto& entry : mp) {
            int mask = entry.first;
            int idx = entry.second;
            
            // deletion (remove one existing letter)
            for (int b = 0; b < 26; ++b) {
                if (mask & (1 << b)) {
                    int nb = mask ^ (1 << b);
                    auto it = mp.find(nb);
                    if (it != mp.end()) dsu.unite(idx, it->second);
                }
            }
            
            // addition (add one missing letter)
            for (int b = 0; b < 26; ++b) {
                if (!(mask & (1 << b))) {
                    int nb = mask | (1 << b);
                    auto it = mp.find(nb);
                    if (it != mp.end()) dsu.unite(idx, it->second);
                }
            }
            
            // replacement (remove one existing and add a different missing)
            for (int del = 0; del < 26; ++del) {
                if (!(mask & (1 << del))) continue;
                int withoutDel = mask ^ (1 << del);
                for (int add = 0; add < 26; ++add) {
                    if (mask & (1 << add)) continue; // already present
                    int nb = withoutDel | (1 << add);
                    auto it = mp.find(nb);
                    if (it != mp.end()) dsu.unite(idx, it->second);
                }
            }
        }
        
        int groups = 0;
        int maxSize = 0;
        for (int i = 0; i < n; ++i) {
            if (dsu.find(i) == i) {
                ++groups;
                maxSize = max(maxSize, dsu.sz[i]);
            }
        }
        return {groups, maxSize};
    }
};
```

## Java

```java
class Solution {
    public int[] groupStrings(String[] words) {
        int n = words.length;
        int[] masks = new int[n];
        for (int i = 0; i < n; i++) {
            int m = 0;
            for (char c : words[i].toCharArray()) {
                m |= 1 << (c - 'a');
            }
            masks[i] = m;
        }

        DSU dsu = new DSU(n);
        java.util.HashMap<Integer, Integer> map = new java.util.HashMap<>();

        for (int i = 0; i < n; i++) {
            int m = masks[i];

            // duplicate mask
            Integer existing = map.get(m);
            if (existing != null) {
                dsu.union(i, existing);
            } else {
                map.put(m, i);
            }

            // toggle one bit (add or delete)
            for (int b = 0; b < 26; b++) {
                int m2 = m ^ (1 << b);
                Integer idx = map.get(m2);
                if (idx != null) dsu.union(i, idx);
            }

            // replace one existing letter with a new one
            for (int b1 = 0; b1 < 26; b1++) {
                if ((m & (1 << b1)) == 0) continue; // must be present to delete
                for (int b2 = 0; b2 < 26; b2++) {
                    if ((m & (1 << b2)) != 0) continue; // must be absent to add
                    int m3 = m ^ (1 << b1) ^ (1 << b2);
                    Integer idx = map.get(m3);
                    if (idx != null) dsu.union(i, idx);
                }
            }
        }

        int groups = 0;
        int maxSize = 0;
        for (int i = 0; i < n; i++) {
            if (dsu.parent[i] == i) {
                groups++;
                maxSize = Math.max(maxSize, dsu.size[i]);
            }
        }
        return new int[]{groups, maxSize};
    }

    class DSU {
        int[] parent;
        int[] size;

        DSU(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }

        void union(int a, int b) {
            int ra = find(a);
            int rb = find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb]) {
                int tmp = ra; ra = rb; rb = tmp;
            }
            parent[rb] = ra;
            size[ra] += size[rb];
        }
    }
}
```

## Python

```python
class Solution(object):
    def groupStrings(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(words)
        masks = []
        for w in words:
            m = 0
            for ch in w:
                m |= 1 << (ord(ch) - 97)
            masks.append(m)

        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        mask_to_idx = {}

        for i, m in enumerate(masks):
            # identical mask
            if m in mask_to_idx:
                union(i, mask_to_idx[m])
            else:
                mask_to_idx[m] = i

            # toggle one bit (add or delete)
            for b in range(26):
                nm = m ^ (1 << b)
                if nm in mask_to_idx:
                    union(i, mask_to_idx[nm])

            # replace: toggle two bits (remove one present, add another absent)
            # iterate over set bits
            for b1 in range(26):
                if not (m >> b1) & 1:
                    continue
                m_without = m ^ (1 << b1)
                for b2 in range(26):
                    if b2 == b1:
                        continue
                    nm = m_without ^ (1 << b2)
                    if nm in mask_to_idx:
                        union(i, mask_to_idx[nm])

        groups = set()
        max_sz = 0
        for i in range(n):
            r = find(i)
            groups.add(r)
            if size[r] > max_sz:
                max_sz = size[r]

        return [len(groups), max_sz]
```

## Python3

```python
from typing import List

class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        masks = [0] * n
        mask_to_idx = {}
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # compute masks and handle duplicates
        for i, w in enumerate(words):
            m = 0
            for ch in w:
                m |= 1 << (ord(ch) - ord('a'))
            masks[i] = m
            if m in mask_to_idx:
                union(i, mask_to_idx[m])
            else:
                mask_to_idx[m] = i

        # process connections: deletions and replacements
        for i, m in enumerate(masks):
            # deletion (also covers addition from other side)
            bits_set = [b for b in range(26) if (m >> b) & 1]
            for b in bits_set:
                del_mask = m ^ (1 << b)
                j = mask_to_idx.get(del_mask)
                if j is not None:
                    union(i, j)

            # replacement: remove one set bit and add one unset bit
            bits_unset = [b for b in range(26) if not ((m >> b) & 1)]
            for b1 in bits_set:
                base = m ^ (1 << b1)  # mask after removing b1
                for b2 in bits_unset:
                    rep_mask = base | (1 << b2)
                    j = mask_to_idx.get(rep_mask)
                    if j is not None:
                        union(i, j)

        # count groups and max size
        group_count = 0
        max_size = 0
        for i in range(n):
            if parent[i] == i:  # root
                group_count += 1
                if size[i] > max_size:
                    max_size = size[i]

        return [group_count, max_size]
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define HASH_SIZE (1 << 15)

typedef struct Node {
    int key;
    int idx;
    struct Node* next;
} Node;

static Node** table;

/* hash function */
static unsigned hash_key(int key) {
    return ((unsigned)key * 2654435761u) & (HASH_SIZE - 1);
}

/* get index for a mask, -1 if not present */
static int hashmap_get(int key) {
    unsigned h = hash_key(key);
    Node* p = table[h];
    while (p) {
        if (p->key == key) return p->idx;
        p = p->next;
    }
    return -1;
}

/* insert mask with its index */
static void hashmap_put(int key, int idx) {
    unsigned h = hash_key(key);
    Node* node = (Node*)malloc(sizeof(Node));
    node->key = key;
    node->idx = idx;
    node->next = table[h];
    table[h] = node;
}

/* Union-Find */
static int* parent_;
static int* sz_;

static int find_set(int x) {
    while (parent_[x] != x) {
        parent_[x] = parent_[parent_[x]];
        x = parent_[x];
    }
    return x;
}

static void union_sets(int a, int b) {
    int ra = find_set(a);
    int rb = find_set(b);
    if (ra == rb) return;
    if (sz_[ra] < sz_[rb]) {
        int tmp = ra; ra = rb; rb = tmp;
    }
    parent_[rb] = ra;
    sz_[ra] += sz_[rb];
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* groupStrings(char** words, int wordsSize, int* returnSize) {
    *returnSize = 2;
    int* answer = (int*)malloc(2 * sizeof(int));
    
    if (wordsSize == 0) {
        answer[0] = 0;
        answer[1] = 0;
        return answer;
    }
    
    /* allocate structures */
    parent_ = (int*)malloc(wordsSize * sizeof(int));
    sz_ = (int*)malloc(wordsSize * sizeof(int));
    int* masks = (int*)malloc(wordsSize * sizeof(int));
    
    for (int i = 0; i < wordsSize; ++i) {
        parent_[i] = i;
        sz_[i] = 1;
    }
    
    table = (Node**)calloc(HASH_SIZE, sizeof(Node*));
    
    /* first pass: store masks and union duplicates */
    for (int i = 0; i < wordsSize; ++i) {
        const char* w = words[i];
        int mask = 0;
        while (*w) {
            mask |= 1 << (*w - 'a');
            ++w;
        }
        masks[i] = mask;
        int existing = hashmap_get(mask);
        if (existing != -1) {
            union_sets(i, existing);
        } else {
            hashmap_put(mask, i);
        }
    }
    
    /* second pass: connect via add/delete/replace operations */
    for (int i = 0; i < wordsSize; ++i) {
        int m = masks[i];
        /* add or delete one letter */
        for (int b = 0; b < 26; ++b) {
            int newMask;
            if (m & (1 << b)) {               // delete
                newMask = m ^ (1 << b);
            } else {                           // add
                newMask = m | (1 << b);
            }
            int idx = hashmap_get(newMask);
            if (idx != -1) union_sets(i, idx);
        }
        /* replace one letter with another */
        for (int a = 0; a < 26; ++a) {
            if (!(m & (1 << a))) continue;
            for (int b = 0; b < 26; ++b) {
                if (m & (1 << b)) continue;
                int newMask = m ^ (1 << a) ^ (1 << b);
                int idx = hashmap_get(newMask);
                if (idx != -1) union_sets(i, idx);
            }
        }
    }
    
    /* count groups and max size */
    int groups = 0;
    int maxSize = 0;
    for (int i = 0; i < wordsSize; ++i) {
        if (parent_[i] == i) {
            ++groups;
            if (sz_[i] > maxSize) maxSize = sz_[i];
        }
    }
    
    answer[0] = groups;
    answer[1] = maxSize;
    
    /* free temporary allocations (optional for LeetCode) */
    free(parent_);
    free(sz_);
    free(masks);
    /* free hashmap */
    for (int i = 0; i < HASH_SIZE; ++i) {
        Node* p = table[i];
        while (p) {
            Node* nxt = p->next;
            free(p);
            p = nxt;
        }
    }
    free(table);
    
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] GroupStrings(string[] words) {
        int n = words.Length;
        int[] masks = new int[n];
        for (int i = 0; i < n; i++) {
            int mask = 0;
            foreach (char ch in words[i]) {
                mask |= 1 << (ch - 'a');
            }
            masks[i] = mask;
        }

        DSU dsu = new DSU(n);
        Dictionary<int, int> map = new Dictionary<int, int>();

        for (int i = 0; i < n; i++) {
            int m = masks[i];

            // duplicate masks
            if (map.TryGetValue(m, out int firstIdx)) {
                dsu.Union(i, firstIdx);
            } else {
                map[m] = i;
            }

            // toggle each bit (add or delete one letter)
            for (int b = 0; b < 26; b++) {
                int toggled = m ^ (1 << b);
                if (map.TryGetValue(toggled, out int idx2)) {
                    dsu.Union(i, idx2);
                }
            }

            // replace one letter with another
            for (int b = 0; b < 26; b++) {
                if ((m & (1 << b)) == 0) continue; // bit not set, cannot replace it
                for (int c = 0; c < 26; c++) {
                    if ((m & (1 << c)) != 0) continue; // target bit already present
                    int newMask = (m ^ (1 << b)) | (1 << c);
                    if (map.TryGetValue(newMask, out int idx3)) {
                        dsu.Union(i, idx3);
                    }
                }
            }
        }

        int groups = 0;
        int maxSize = 0;
        for (int i = 0; i < n; i++) {
            if (dsu.Parent[i] == i) {
                groups++;
                if (dsu.Size[i] > maxSize) maxSize = dsu.Size[i];
            }
        }

        return new int[] { groups, maxSize };
    }

    private class DSU {
        public int[] Parent;
        public int[] Size;

        public DSU(int n) {
            Parent = new int[n];
            Size = new int[n];
            for (int i = 0; i < n; i++) {
                Parent[i] = i;
                Size[i] = 1;
            }
        }

        public int Find(int x) {
            if (Parent[x] != x) Parent[x] = Find(Parent[x]);
            return Parent[x];
        }

        public void Union(int a, int b) {
            int ra = Find(a);
            int rb = Find(b);
            if (ra == rb) return;
            if (Size[ra] < Size[rb]) {
                int tmp = ra; ra = rb; rb = tmp;
            }
            Parent[rb] = ra;
            Size[ra] += Size[rb];
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number[]}
 */
var groupStrings = function(words) {
    const n = words.length;
    const masks = new Array(n);
    const maskToIdx = new Map();
    
    class UnionFind {
        constructor(size) {
            this.parent = new Array(size);
            this.rank = new Array(size).fill(0);
            for (let i = 0; i < size; i++) this.parent[i] = i;
        }
        find(x) {
            if (this.parent[x] !== x) {
                this.parent[x] = this.find(this.parent[x]);
            }
            return this.parent[x];
        }
        union(a, b) {
            let ra = this.find(a), rb = this.find(b);
            if (ra === rb) return;
            if (this.rank[ra] < this.rank[rb]) {
                this.parent[ra] = rb;
            } else if (this.rank[ra] > this.rank[rb]) {
                this.parent[rb] = ra;
            } else {
                this.parent[rb] = ra;
                this.rank[ra]++;
            }
        }
    }
    
    const uf = new UnionFind(n);
    
    // compute masks and union duplicates
    for (let i = 0; i < n; i++) {
        let mask = 0;
        for (const ch of words[i]) {
            mask |= 1 << (ch.charCodeAt(0) - 97);
        }
        masks[i] = mask;
        if (maskToIdx.has(mask)) {
            uf.union(i, maskToIdx.get(mask));
        } else {
            maskToIdx.set(mask, i);
        }
    }
    
    // helper to iterate set bits
    const getSetBits = (mask) => {
        const bits = [];
        for (let b = 0; b < 26; b++) {
            if ((mask >> b) & 1) bits.push(b);
        }
        return bits;
    };
    
    // connect via one-bit toggle (add/delete) and replace (two-bit change)
    for (let i = 0; i < n; i++) {
        const mask = masks[i];
        // add/delete
        for (let b = 0; b < 26; b++) {
            const newMask = mask ^ (1 << b);
            if (maskToIdx.has(newMask)) {
                uf.union(i, maskToIdx.get(newMask));
            }
        }
        // replace: remove one existing bit and add another missing bit
        const setBits = getSetBits(mask);
        for (const bRemove of setBits) {
            for (let bAdd = 0; bAdd < 26; bAdd++) {
                if ((mask >> bAdd) & 1) continue; // already present
                const newMask = mask ^ (1 << bRemove) ^ (1 << bAdd);
                if (maskToIdx.has(newMask)) {
                    uf.union(i, maskToIdx.get(newMask));
                }
            }
        }
    }
    
    const compSize = new Map();
    for (let i = 0; i < n; i++) {
        const root = uf.find(i);
        compSize.set(root, (compSize.get(root) || 0) + 1);
    }
    
    let groups = compSize.size;
    let maxSize = 0;
    for (const sz of compSize.values()) {
        if (sz > maxSize) maxSize = sz;
    }
    
    return [groups, maxSize];
};
```

## Typescript

```typescript
function groupStrings(words: string[]): number[] {
    const n = words.length;

    class DSU {
        parent: number[];
        size: number[];
        constructor(n: number) {
            this.parent = new Array(n);
            this.size = new Array(n);
            for (let i = 0; i < n; i++) {
                this.parent[i] = i;
                this.size[i] = 1;
            }
        }
        find(x: number): number {
            if (this.parent[x] !== x) {
                this.parent[x] = this.find(this.parent[x]);
            }
            return this.parent[x];
        }
        union(a: number, b: number): void {
            let ra = this.find(a);
            let rb = this.find(b);
            if (ra === rb) return;
            if (this.size[ra] < this.size[rb]) {
                [ra, rb] = [rb, ra];
            }
            this.parent[rb] = ra;
            this.size[ra] += this.size[rb];
        }
    }

    const dsu = new DSU(n);
    const maskToIdx = new Map<number, number>();
    const masks: number[] = new Array(n);

    // Compute masks and union duplicates
    for (let i = 0; i < n; i++) {
        let m = 0;
        for (const ch of words[i]) {
            m |= 1 << (ch.charCodeAt(0) - 97);
        }
        masks[i] = m;
        const existing = maskToIdx.get(m);
        if (existing !== undefined) {
            dsu.union(i, existing);
        } else {
            maskToIdx.set(m, i);
        }
    }

    // Connect via one-bit toggle (add/delete)
    for (let i = 0; i < n; i++) {
        const m = masks[i];
        for (let b = 0; b < 26; b++) {
            const neighbor = m ^ (1 << b);
            const idx = maskToIdx.get(neighbor);
            if (idx !== undefined) {
                dsu.union(i, idx);
            }
        }
    }

    // Connect via replace operation (toggle one set bit and one unset bit)
    for (let i = 0; i < n; i++) {
        const m = masks[i];
        for (let b = 0; b < 26; b++) {
            if ((m & (1 << b)) === 0) continue; // b must be set
            for (let c = 0; c < 26; c++) {
                if ((m & (1 << c)) !== 0) continue; // c must be unset
                const neighbor = m ^ (1 << b) ^ (1 << c);
                const idx = maskToIdx.get(neighbor);
                if (idx !== undefined) {
                    dsu.union(i, idx);
                }
            }
        }
    }

    let groups = 0;
    let maxSize = 0;
    for (let i = 0; i < n; i++) {
        if (dsu.find(i) === i) {
            groups++;
            if (dsu.size[i] > maxSize) maxSize = dsu.size[i];
        }
    }

    return [groups, maxSize];
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer[]
     */
    function groupStrings($words) {
        $n = count($words);
        $masks = [];
        $maskToIndices = [];

        for ($i = 0; $i < $n; $i++) {
            $word = $words[$i];
            $mask = 0;
            $len = strlen($word);
            for ($j = 0; $j < $len; $j++) {
                $c = ord($word[$j]) - 97;
                $mask |= (1 << $c);
            }
            $masks[$i] = $mask;
            if (!isset($maskToIndices[$mask])) {
                $maskToIndices[$mask] = [];
            }
            $maskToIndices[$mask][] = $i;
        }

        // DSU initialization
        $parent = range(0, $n - 1);
        $size   = array_fill(0, $n, 1);

        $find = function($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) {
                $parent[$x] = $find($parent[$x]);
            }
            return $parent[$x];
        };

        $union = function($a, $b) use (&$parent, &$size, &$find) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra === $rb) return;
            if ($size[$ra] < $size[$rb]) {
                $tmp = $ra; $ra = $rb; $rb = $tmp;
            }
            $parent[$rb] = $ra;
            $size[$ra] += $size[$rb];
        };

        // Union duplicates (same mask)
        foreach ($maskToIndices as $list) {
            $first = $list[0];
            $cnt = count($list);
            for ($k = 1; $k < $cnt; $k++) {
                $union($first, $list[$k]);
            }
        }

        // Process connections
        for ($i = 0; $i < $n; $i++) {
            $mask = $masks[$i];

            // Add/Delete (toggle one bit)
            for ($b = 0; $b < 26; $b++) {
                $neighbor = $mask ^ (1 << $b);
                if (isset($maskToIndices[$neighbor])) {
                    $union($i, $maskToIndices[$neighbor][0]);
                }
            }

            // Replace (toggle one set bit and one unset bit)
            $setBits = [];
            $unsetBits = [];
            for ($b = 0; $b < 26; $b++) {
                if ($mask & (1 << $b)) {
                    $setBits[] = $b;
                } else {
                    $unsetBits[] = $b;
                }
            }

            foreach ($setBits as $sb) {
                foreach ($unsetBits as $ub) {
                    $neighbor = $mask ^ (1 << $sb) ^ (1 << $ub);
                    if (isset($maskToIndices[$neighbor])) {
                        $union($i, $maskToIndices[$neighbor][0]);
                    }
                }
            }
        }

        // Count groups and max size
        $rootCount = [];
        for ($i = 0; $i < $n; $i++) {
            $r = $find($i);
            if (!isset($rootCount[$r])) $rootCount[$r] = 0;
            $rootCount[$r]++;
        }

        $groupCount = count($rootCount);
        $maxSize = 0;
        foreach ($rootCount as $cnt) {
            if ($cnt > $maxSize) $maxSize = $cnt;
        }

        return [$groupCount, $maxSize];
    }
}
```

## Swift

```swift
class Solution {
    func groupStrings(_ words: [String]) -> [Int] {
        let n = words.count
        var masks = [Int](repeating: 0, count: n)
        var indexByMask = [Int:Int]()
        var parent = [Int](repeating: 0, count: n)
        var compSize = [Int](repeating: 1, count: n)
        for i in 0..<n { parent[i] = i }
        
        func find(_ x: Int) -> Int {
            var v = x
            while parent[v] != v {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
        }
        func union(_ a: Int, _ b: Int) {
            var ra = find(a)
            var rb = find(b)
            if ra == rb { return }
            if compSize[ra] < compSize[rb] {
                swap(&ra, &rb)
            }
            parent[rb] = ra
            compSize[ra] += compSize[rb]
        }
        
        // compute masks and union duplicates
        for i in 0..<n {
            var mask = 0
            for ch in words[i].utf8 {
                let bit = Int(ch - 97)
                mask |= (1 << bit)
            }
            masks[i] = mask
            if let j = indexByMask[mask] {
                union(i, j)
            } else {
                indexByMask[mask] = i
            }
        }
        
        // connect via allowed operations
        for i in 0..<n {
            let m = masks[i]
            // add or delete one letter (toggle a bit)
            for b in 0..<26 {
                let toggled = m ^ (1 << b)
                if let j = indexByMask[toggled] {
                    union(i, j)
                }
            }
            // replace one letter: remove a set bit and add an unset bit
            var setBits = [Int]()
            for b in 0..<26 where (m & (1 << b)) != 0 {
                setBits.append(b)
            }
            for sb in setBits {
                let without = m ^ (1 << sb)
                for nb in 0..<26 where (without & (1 << nb)) == 0 {
                    let newMask = without | (1 << nb)
                    if let j = indexByMask[newMask] {
                        union(i, j)
                    }
                }
            }
        }
        
        var groups = 0
        var maxGroupSize = 0
        var seenRoots = Set<Int>()
        for i in 0..<n {
            let r = find(i)
            if !seenRoots.contains(r) {
                seenRoots.insert(r)
                groups += 1
                if compSize[r] > maxGroupSize { maxGroupSize = compSize[r] }
            }
        }
        return [groups, maxGroupSize]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun groupStrings(words: Array<String>): IntArray {
        val n = words.size
        val masks = IntArray(n)
        val dsu = DSU(n)
        val map = HashMap<Int, Int>() // mask -> representative index

        for (i in 0 until n) {
            var m = 0
            for (ch in words[i]) {
                m = m or (1 shl (ch - 'a'))
            }
            masks[i] = m
            val rep = map[m]
            if (rep != null) {
                dsu.union(i, rep)
            } else {
                map[m] = i
            }
        }

        for (i in 0 until n) {
            val m = masks[i]

            // add or delete one letter (toggle a single bit)
            for (b in 0 until 26) {
                val neighbor = m xor (1 shl b)
                map[neighbor]?.let { dsu.union(i, it) }
            }

            // replace one letter: remove an existing bit and add a missing bit
            val setBits = IntArray(26)
            var cntSet = 0
            for (b in 0 until 26) {
                if ((m shr b) and 1 == 1) {
                    setBits[cntSet++] = b
                }
            }
            for (idx in 0 until cntSet) {
                val bRemove = setBits[idx]
                val without = m xor (1 shl bRemove)
                for (bAdd in 0 until 26) {
                    if ((m shr bAdd) and 1 == 0) { // not present originally
                        val neighbor = without or (1 shl bAdd)
                        map[neighbor]?.let { dsu.union(i, it) }
                    }
                }
            }
        }

        var groups = 0
        var maxSize = 0
        for (i in 0 until n) {
            if (dsu.find(i) == i) {
                groups++
                if (dsu.size[i] > maxSize) maxSize = dsu.size[i]
            }
        }
        return intArrayOf(groups, maxSize)
    }

    private class DSU(n: Int) {
        val parent = IntArray(n) { it }
        val size = IntArray(n) { 1 }

        fun find(x: Int): Int {
            var v = x
            while (parent[v] != v) {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
        }

        fun union(a: Int, b: Int) {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (size[ra] < size[rb]) {
                val tmp = ra
                ra = rb
                rb = tmp
            }
            parent[rb] = ra
            size[ra] += size[rb]
        }
    }
}
```

## Dart

```dart
class Solution {
  List<int> groupStrings(List<String> words) {
    final Map<int, int> maskToId = {};
    final List<int> parent = [];
    final List<int> rankSize = []; // for union by size (number of ids)
    final List<int> wordCount = [];

    // Build unique masks and count occurrences
    for (final w in words) {
      int mask = 0;
      for (int i = 0; i < w.length; ++i) {
        int bit = w.codeUnitAt(i) - 97;
        mask |= 1 << bit;
      }
      if (!maskToId.containsKey(mask)) {
        int id = parent.length;
        maskToId[mask] = id;
        parent.add(id);
        rankSize.add(1);
        wordCount.add(1);
      } else {
        int id = maskToId[mask]!;
        wordCount[id]++;
      }
    }

    int find(int x) {
      while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
      }
      return x;
    }

    void union(int a, int b) {
      int ra = find(a);
      int rb = find(b);
      if (ra == rb) return;
      // attach smaller tree to larger
      if (rankSize[ra] < rankSize[rb]) {
        parent[ra] = rb;
        rankSize[rb] += rankSize[ra];
      } else {
        parent[rb] = ra;
        rankSize[ra] += rankSize[rb];
      }
    }

    // Generate connections
    for (final entry in maskToId.entries) {
      int mask = entry.key;
      int id = entry.value;

      // collect set bits
      final List<int> setBits = [];
      for (int b = 0; b < 26; ++b) {
        if ((mask >> b) & 1 == 1) setBits.add(b);
      }

      // Deletion: remove one existing bit
      for (final b in setBits) {
        int newMask = mask ^ (1 << b);
        final nid = maskToId[newMask];
        if (nid != null) union(id, nid);
      }

      // Replacement: remove a set bit and add an unset bit
      for (final iBit in setBits) {
        for (int j = 0; j < 26; ++j) {
          if ((mask >> j) & 1 == 1) continue;
          int newMask = (mask ^ (1 << iBit)) | (1 << j);
          final nid = maskToId[newMask];
          if (nid != null) union(id, nid);
        }
      }
    }

    // Compute groups and largest size
    final List<int> compSize = List.filled(parent.length, 0);
    for (int i = 0; i < parent.length; ++i) {
      int root = find(i);
      compSize[root] += wordCount[i];
    }

    int groups = 0;
    int maxSize = 0;
    for (final size in compSize) {
      if (size > 0) {
        groups++;
        if (size > maxSize) maxSize = size;
      }
    }

    return [groups, maxSize];
  }
}
```

## Golang

```go
func groupStrings(words []string) []int {
    n := len(words)
    parent := make([]int, n)
    size := make([]int, n)
    for i := 0; i < n; i++ {
        parent[i] = i
        size[i] = 1
    }

    var find func(int) int
    find = func(x int) int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    union := func(a, b int) {
        ra, rb := find(a), find(b)
        if ra == rb {
            return
        }
        if size[ra] < size[rb] {
            ra, rb = rb, ra
        }
        parent[rb] = ra
        size[ra] += size[rb]
    }

    maskToIdx := make(map[int]int)

    for i, w := range words {
        mask := 0
        for _, ch := range w {
            mask |= 1 << (ch - 'a')
        }

        // duplicate masks
        if idx, ok := maskToIdx[mask]; ok {
            union(i, idx)
        } else {
            maskToIdx[mask] = i
        }

        // add/delete one letter (toggle a bit)
        for b := 0; b < 26; b++ {
            toggled := mask ^ (1 << b)
            if idx, ok := maskToIdx[toggled]; ok {
                union(i, idx)
            }
        }

        // replace one letter with another
        for b := 0; b < 26; b++ {
            if (mask>>b)&1 == 0 {
                continue
            }
            for c := 0; c < 26; c++ {
                if (mask>>c)&1 == 1 {
                    continue
                }
                newMask := mask ^ (1 << b) ^ (1 << c)
                if idx, ok := maskToIdx[newMask]; ok {
                    union(i, idx)
                }
            }
        }
    }

    groupsCount := make(map[int]int)
    maxSize := 0
    for i := 0; i < n; i++ {
        root := find(i)
        groupsCount[root]++
        if groupsCount[root] > maxSize {
            maxSize = groupsCount[root]
        }
    }

    return []int{len(groupsCount), maxSize}
}
```

## Ruby

```ruby
def group_strings(words)
  n = words.length
  masks = Array.new(n, 0)
  mask_to_index = {}

  # Compute bitmask for each word and map first occurrence
  words.each_with_index do |w, i|
    m = 0
    w.each_byte { |c| m |= 1 << (c - 97) }
    masks[i] = m
    if mask_to_index.key?(m)
      # duplicate mask, union later
    else
      mask_to_index[m] = i
    end
  end

  class DSU
    def initialize(n)
      @parent = Array.new(n) { |i| i }
      @rank   = Array.new(n, 0)
    end

    def find(x)
      while @parent[x] != x
        @parent[x] = @parent[@parent[x]]
        x = @parent[x]
      end
      x
    end

    def union(x, y)
      xr = find(x)
      yr = find(y)
      return if xr == yr
      if @rank[xr] < @rank[yr]
        @parent[xr] = yr
      elsif @rank[xr] > @rank[yr]
        @parent[yr] = xr
      else
        @parent[yr] = xr
        @rank[xr] += 1
      end
    end
  end

  dsu = DSU.new(n)

  # Union duplicate masks (if any)
  mask_counts = Hash.new { |h, k| h[k] = [] }
  masks.each_with_index { |m, i| mask_counts[m] << i }
  mask_counts.each_value do |indices|
    first = indices[0]
    indices[1..-1].each { |idx| dsu.union(first, idx) } if indices.size > 1
  end

  (0...n).each do |i|
    m = masks[i]

    # Delete or Add one letter
    26.times do |b|
      bit = 1 << b
      if (m & bit) != 0
        new_mask = m ^ bit          # delete
        if (j = mask_to_index[new_mask])
          dsu.union(i, j)
        end
      else
        new_mask = m | bit          # add
        if (j = mask_to_index[new_mask])
          dsu.union(i, j)
        end
      end
    end

    # Replace one letter with another
    26.times do |i_bit|
      i_bitmask = 1 << i_bit
      next if (m & i_bitmask) == 0
      26.times do |j_bit|
        j_bitmask = 1 << j_bit
        next if (m & j_bitmask) != 0
        new_mask = (m ^ i_bitmask) | j_bitmask
        if (j = mask_to_index[new_mask])
          dsu.union(i, j)
        end
      end
    end
  end

  group_sizes = Hash.new(0)
  n.times do |i|
    root = dsu.find(i)
    group_sizes[root] += 1
  end

  [group_sizes.size, group_sizes.values.max]
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable

  class DSU(n: Int) {
    val parent: Array[Int] = (0 until n).toArray
    val size: Array[Int] = Array.fill(n)(1)

    def find(x: Int): Int = {
      var p = x
      while (parent(p) != p) p = parent(p)
      var root = p
      var cur = x
      while (parent(cur) != cur) {
        val nxt = parent(cur)
        parent(cur) = root
        cur = nxt
      }
      root
    }

    def union(a: Int, b: Int): Unit = {
      var ra = find(a)
      var rb = find(b)
      if (ra == rb) return
      if (size(ra) < size(rb)) {
        val tmp = ra; ra = rb; rb = tmp
      }
      parent(rb) = ra
      size(ra) += size(rb)
    }
  }

  def groupStrings(words: Array[String]): Array[Int] = {
    val n = words.length
    val masks = new Array[Int](n)
    for (i <- 0 until n) {
      var mask = 0
      for (ch <- words(i)) {
        mask |= 1 << (ch - 'a')
      }
      masks(i) = mask
    }

    val dsu = new DSU(n)
    val map = mutable.HashMap[Int, Int]()

    for (i <- 0 until n) {
      val m = masks(i)

      // same mask already seen
      map.get(m).foreach(dsu.union(i, _))

      // iterate over bits
      for (b <- 0 until 26) {
        val bitB = 1 << b
        if ((m & bitB) != 0) {
          // delete operation
          val delMask = m ^ bitB
          map.get(delMask).foreach(dsu.union(i, _))

          // replace operation: remove b, add c (c not set)
          for (c <- 0 until 26) {
            if ((m & (1 << c)) == 0) {
              val repMask = m ^ bitB ^ (1 << c)
              map.get(repMask).foreach(dsu.union(i, _))
            }
          }
        } else {
          // add operation
          val addMask = m | bitB
          map.get(addMask).foreach(dsu.union(i, _))
        }
      }

      if (!map.contains(m)) map.put(m, i)
    }

    var groups = 0
    var maxSize = 0
    for (i <- 0 until n) {
      if (dsu.find(i) == i) {
        groups += 1
        if (dsu.size(i) > maxSize) maxSize = dsu.size(i)
      }
    }

    Array(groups, maxSize)
  }
}
```

## Rust

```rust
use std::collections::HashMap;

struct DSU {
    parent: Vec<usize>,
    size: Vec<usize>,
}
impl DSU {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(i);
        }
        DSU { parent, size: vec![1; n] }
    }
    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            let root = self.find(self.parent[x]);
            self.parent[x] = root;
        }
        self.parent[x]
    }
    fn union(&mut self, a: usize, b: usize) {
        let mut ra = self.find(a);
        let mut rb = self.find(b);
        if ra == rb {
            return;
        }
        if self.size[ra] < self.size[rb] {
            std::mem::swap(&mut ra, &mut rb);
        }
        self.parent[rb] = ra;
        self.size[ra] += self.size[rb];
    }
}

impl Solution {
    pub fn group_strings(words: Vec<String>) -> Vec<i32> {
        let mut mask_to_id: HashMap<u32, usize> = HashMap::new();
        let mut cnt: Vec<i32> = Vec::new();

        for w in words.iter() {
            let mut mask: u32 = 0;
            for b in w.bytes() {
                mask |= 1 << (b - b'a');
            }
            if let Some(&id) = mask_to_id.get(&mask) {
                cnt[id] += 1;
            } else {
                let id = cnt.len();
                mask_to_id.insert(mask, id);
                cnt.push(1);
            }
        }

        let n = cnt.len();
        let mut dsu = DSU::new(n);
        let masks: Vec<u32> = mask_to_id.keys().cloned().collect();

        for &mask in masks.iter() {
            let id1 = mask_to_id[&mask];
            for i in 0..26 {
                let bit_i = 1u32 << i;
                if mask & bit_i != 0 {
                    // delete one letter
                    let m_del = mask ^ bit_i;
                    if let Some(&id2) = mask_to_id.get(&m_del) {
                        dsu.union(id1, id2);
                    }
                    // replace one letter with another
                    for j in 0..26 {
                        if i == j {
                            continue;
                        }
                        let bit_j = 1u32 << j;
                        if mask & bit_j == 0 {
                            let m_rep = (mask ^ bit_i) | bit_j;
                            if let Some(&id3) = mask_to_id.get(&m_rep) {
                                dsu.union(id1, id3);
                            }
                        }
                    }
                } else {
                    // add one letter
                    let m_add = mask | bit_i;
                    if let Some(&id2) = mask_to_id.get(&m_add) {
                        dsu.union(id1, id2);
                    }
                }
            }
        }

        let mut comp_cnt: HashMap<usize, i32> = HashMap::new();
        for id in 0..n {
            let root = dsu.find(id);
            *comp_cnt.entry(root).or_insert(0) += cnt[id];
        }

        let groups = comp_cnt.len() as i32;
        let mut largest = 0i32;
        for &v in comp_cnt.values() {
            if v > largest {
                largest = v;
            }
        }

        vec![groups, largest]
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(provide group-strings)

(define/contract (group-strings words)
  (-> (listof string?) (listof exact-integer?))
  (let* ([n (length words)]
         [masks (make-vector n)]
         ;; compute bitmask for each word
         [_ (for ([i (in-range n)] [w (in-list words)])
              (define mask
                (for/fold ([m 0]) ([c (in-string w)])
                  (bitwise-ior m (arithmetic-shift 1 (- (char->integer c) (char->integer #\a))))))
              (vector-set! masks i mask))]
         [parent (make-vector n)]
         [sz (make-vector n 1)]
         [_ (for ([i (in-range n)]) (vector-set! parent i i))]
         ;; union‑find helpers
         [find (letrec ([find
                         (lambda (x)
                           (let ([p (vector-ref parent x)])
                             (if (= p x)
                                 x
                                 (let ([r (find p)])
                                   (vector-set! parent x r)
                                   r))))])
                find)]
         [union (lambda (a b)
                  (let* ([ra (find a)] [rb (find b)])
                    (when (not (= ra rb))
                      (let ([sa (vector-ref sz ra)] [sb (vector-ref sz rb)])
                        (if (> sa sb)
                            (begin
                              (vector-set! parent rb ra)
                              (vector-set! sz ra (+ sa sb)))
                            (begin
                              (vector-set! parent ra rb)
                              (vector-set! sz rb (+ sa sb))))))))]
         [mp (make-hash)])
    ;; main loop: union with duplicates and neighbours
    (for ([i (in-range n)])
      (define m (vector-ref masks i))
      ;; duplicate mask
      (when (hash-has-key? mp m)
        (union i (hash-ref mp m)))
      (hash-set! mp m i)
      ;; toggle one bit (add or delete)
      (for ([b (in-range 26)])
        (define m1 (bitwise-xor m (arithmetic-shift 1 b)))
        (when (hash-has-key? mp m1)
          (union i (hash-ref mp m1))))
      ;; replace one letter with another (toggle two bits)
      (for* ([s (in-range 26)]
             #:when (not (= 0 (bitwise-and m (arithmetic-shift 1 s)))))
        [t (in-range 26)]
        #:when (= 0 (bitwise-and m (arithmetic-shift 1 t))))
        (define m2 (bitwise-xor (bitwise-xor m (arithmetic-shift 1 s))
                                (arithmetic-shift 1 t)))
        (when (hash-has-key? mp m2)
          (union i (hash-ref mp m2)))))
    ;; count components and max size
    (define groups 0)
    (define max-size 0)
    (for ([i (in-range n)])
      (when (= i (find i))
        (set! groups (+ groups 1))
        (let ([s (vector-ref sz i)])
          (when (> s max-size) (set! max-size s)))))
    (list groups max-size)))
```

## Erlang

```erlang
-module(solution).
-export([group_strings/1]).
-spec group_strings(Words :: [unicode:unicode_binary()]) -> [integer()].
group_strings(Words) ->
    Masks = [mask_from_word(W) || W <- Words],
    {FreqMap, Distinct} = build_freq_map(Masks),
    Table = ets:new(dsu_table, [set, private]),
    init_dsu(Table, Distinct, FreqMap),
    lists:foreach(fun(M) -> process_mask(Table, M, FreqMap) end, Distinct),
    {Groups, MaxSize} = compute_groups(Table, Distinct),
    ets:delete(Table),
    [Groups, MaxSize].

mask_from_word(Word) ->
    Bytes = binary:bin_to_list(Word),
    lists:foldl(fun(C, Acc) -> Acc bor (1 bsl (C - $a)) end, 0, Bytes).

build_freq_map(Masks) ->
    build_freq_map(Masks, maps:new(), []).

build_freq_map([], Map, List) ->
    {Map, List};
build_freq_map([M|Rest], Map, List) ->
    case maps:is_key(M, Map) of
        true ->
            NewMap = maps:update_with(M, fun(C) -> C + 1 end, 1, Map),
            build_freq_map(Rest, NewMap, List);
        false ->
            NewMap = maps:put(M, 1, Map),
            build_freq_map(Rest, NewMap, [M|List])
    end.

init_dsu(Table, Distinct, FreqMap) ->
    lists:foreach(fun(M) ->
        Count = maps:get(M, FreqMap),
        ets:insert(Table, {M, M, Count})
    end, Distinct).

process_mask(Table, M, FreqMap) ->
    process_bits(Table, M, FreqMap, 0).

process_bits(_Table, _M, _FreqMap, I) when I >= 26 -> ok;
process_bits(Table, M, FreqMap, I) ->
    Bit = 1 bsl I,
    case (M band Bit) of
        0 ->
            N = M bor Bit,
            maybe_union(Table, M, N, FreqMap);
        _ ->
            N = M bxor Bit,
            maybe_union(Table, M, N, FreqMap)
    end,
    replace_loop(Table, M, I, FreqMap),
    process_bits(Table, M, FreqMap, I + 1).

replace_loop(_Table, _M, I, _FreqMap) when I >= 26 -> ok;
replace_loop(Table, M, I, FreqMap) ->
    BitI = 1 bsl I,
    case (M band BitI) of
        0 -> ok; % cannot remove a bit that is not set
        _ ->
            replace_inner(Table, M, I, FreqMap, 0)
    end,
    replace_loop(Table, M, I + 1, FreqMap).

replace_inner(_Table, _M, _I, _FreqMap, J) when J >= 26 -> ok;
replace_inner(Table, M, I, FreqMap, J) ->
    BitJ = 1 bsl J,
    case (M band BitJ) of
        0 ->
            N = (M bxor (1 bsl I)) bor BitJ,
            maybe_union(Table, M, N, FreqMap);
        _ -> ok
    end,
    replace_inner(Table, M, I, FreqMap, J + 1).

maybe_union(_Table, _A, _B, FreqMap) when not maps:is_key(_B, FreqMap) -> ok;
maybe_union(Table, A, B, FreqMap) ->
    case maps:is_key(B, FreqMap) of
        true -> union(Table, A, B);
        false -> ok
    end.

find(Table, X) ->
    [{X, Parent, _}] = ets:lookup(Table, X),
    if Parent == X ->
            X;
       true ->
            Root = find(Table, Parent),
            ets:update_element(Table, X, {2, Root}),
            Root
    end.

union(Table, A, B) ->
    RA = find(Table, A),
    RB = find(Table, B),
    if RA == RB -> ok;
       true ->
            [{RA, _, SizeA}] = ets:lookup(Table, RA),
            [{RB, _, SizeB}] = ets:lookup(Table, RB),
            if SizeA < SizeB ->
                    NewSize = SizeA + SizeB,
                    ets:update_element(Table, RB, {3, NewSize}),
                    ets:update_element(Table, RA, {2, RB});
               true ->
                    NewSize = SizeA + SizeB,
                    ets:update_element(Table, RA, {3, NewSize}),
                    ets:update_element(Table, RB, {2, RA})
            end
    end.

compute_groups(Table, Distinct) ->
    compute_groups(Distinct, Table, 0, 0).

compute_groups([], _Table, G, Max) -> {G, Max};
compute_groups([M|Rest], Table, G, Max) ->
    case ets:lookup(Table, M) of
        [{M, Parent, Size}] when Parent == M ->
            NewMax = erlang:max(Max, Size),
            compute_groups(Rest, Table, G + 1, NewMax);
        _ -> compute_groups(Rest, Table, G, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  defp word_to_mask(word) do
    String.to_charlist(word)
    |> Enum.reduce(0, fn ch, acc ->
      bit = ch - ?a
      acc ||| (1 <<< bit)
    end)
  end

  defmodule DSU do
    def new(n) do
      parent =
        :array.new(n, default: -1)
        |> Enum.reduce(0..n-1, fn i, arr -> :array.set(i, i, arr) end)

      size = :array.new(n, default: 1)
      {parent, size}
    end

    def find(parent, x) do
      p = :array.get(x, parent)

      if p == x do
        {parent, x}
      else
        {parent2, root} = find(parent, p)
        parent3 = :array.set(x, root, parent2)
        {parent3, root}
      end
    end

    def union({parent, size}, a, b) do
      {parent1, ra} = find(parent, a)
      {parent2, rb} = find(parent1, b)

      if ra == rb do
        {{parent2, size}, false}
      else
        sa = :array.get(ra, size)
        sb = :array.get(rb, size)

        if sa < sb do
          parent3 = :array.set(ra, rb, parent2)
          size3 = :array.set(rb, sa + sb, size)
          {{parent3, size3}, true}
        else
          parent3 = :array.set(rb, ra, parent2)
          size3 = :array.set(ra, sa + sb, size)
          {{parent3, size3}, true}
        end
      end
    end
  end

  @spec group_strings(words :: [String.t()]) :: [integer]
  def group_strings(words) do
    n = length(words)

    masks =
      Enum.map(words, fn w -> word_to_mask(w) end)
      |> List.to_tuple()

    # initial DSU
    dsu = DSU.new(n)

    # map mask to first index
    {dsu, mask_index} =
      Enum.reduce(0..n - 1, {dsu, %{}}, fn i, {cur_dsu, mp} ->
        mask = elem(masks, i)

        case Map.fetch(mp, mask) do
          {:ok, idx} ->
            {new_dsu, _} = DSU.union(cur_dsu, i, idx)
            {new_dsu, mp}

          :error ->
            {cur_dsu, Map.put(mp, mask, i)}
        end
      end)

    # helper to get set bits and missing bits
    get_bits = fn mask ->
      set_bits =
        for b <- 0..25,
            (mask &&& (1 <<< b)) != 0,
            do: b

      missing_bits =
        for b <- 0..25,
            (mask &&& (1 <<< b)) == 0,
            do: b

      {set_bits, missing_bits}
    end

    # second pass: connect via one operation
    dsu_final =
      Enum.reduce(0..n - 1, dsu, fn i, cur_dsu ->
        mask = elem(masks, i)
        {set_bits, missing_bits} = get_bits.(mask)

        # deletions
        cur_dsu =
          Enum.reduce(set_bits, cur_dsu, fn b, acc_dsu ->
            new_mask = mask ^^^ (1 <<< b)

            case Map.fetch(mask_index, new_mask) do
              {:ok, idx} -> elem(DSU.union(acc_dsu, i, idx), 0)
              :error -> acc_dsu
            end
          end)

        # additions
        cur_dsu =
          Enum.reduce(missing_bits, cur_dsu, fn b, acc_dsu ->
            new_mask = mask ||| (1 <<< b)

            case Map.fetch(mask_index, new_mask) do
              {:ok, idx} -> elem(DSU.union(acc_dsu, i, idx), 0)
              :error -> acc_dsu
            end
          end)

        # replacements
        cur_dsu =
          Enum.reduce(set_bits, cur_dsu, fn del_b, acc1 ->
            Enum.reduce(missing_bits, acc1, fn add_b, acc2 ->
              new_mask = (mask ^^^ (1 <<< del_b)) ||| (1 <<< add_b)

              case Map.fetch(mask_index, new_mask) do
                {:ok, idx} -> elem(DSU.union(acc2, i, idx), 0)
                :error -> acc2
              end
            end)
          end)

        cur_dsu
      end)

    # count component sizes
    {final_parent, _size_arr} = dsu_final

    {_parent_after_counts, counts} =
      Enum.reduce(0..n - 1, {final_parent, %{}}, fn i, {par, cnts} ->
        {par2, root} = DSU.find(par, i)
        new_cnts = Map.update(cnts, root, 1, &(&1 + 1))
        {par2, new_cnts}
      end)

    num_groups = map_size(counts)
    max_group =
      if num_groups == 0 do
        0
      else
        counts |> Map.values() |> Enum.max()
      end

    [num_groups, max_group]
  end
end
```
