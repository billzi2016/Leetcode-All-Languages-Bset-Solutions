# 2935. Maximum Strong Pair XOR II

## Cpp

```cpp
class Solution {
public:
    struct Node {
        int child[2];
        int cnt;
        Node() { child[0] = child[1] = -1; cnt = 0; }
    };
    
    const int MAXBIT = 20; // enough for numbers < 2^20
    
    void insert(vector<Node>& trie, int x) {
        int cur = 0;
        trie[cur].cnt++;
        for (int b = MAXBIT; b >= 0; --b) {
            int bit = (x >> b) & 1;
            if (trie[cur].child[bit] == -1) {
                trie[cur].child[bit] = trie.size();
                trie.emplace_back();
            }
            cur = trie[cur].child[bit];
            trie[cur].cnt++;
        }
    }
    
    void erase(vector<Node>& trie, int x) {
        int cur = 0;
        trie[cur].cnt--;
        for (int b = MAXBIT; b >= 0; --b) {
            int bit = (x >> b) & 1;
            int nxt = trie[cur].child[bit];
            cur = nxt;
            trie[cur].cnt--;
        }
    }
    
    int query(const vector<Node>& trie, int x) {
        int cur = 0;
        int res = 0;
        for (int b = MAXBIT; b >= 0; --b) {
            int bit = (x >> b) & 1;
            int want = bit ^ 1;
            if (trie[cur].child[want] != -1 && trie[trie[cur].child[want]].cnt > 0) {
                res |= (1 << b);
                cur = trie[cur].child[want];
            } else {
                cur = trie[cur].child[bit];
            }
        }
        return res;
    }
    
    int maximumStrongPairXor(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<Node> trie;
        trie.emplace_back(); // root
        
        long long ans = 0;
        int r = -1;
        for (int i = 0; i < n; ++i) {
            while (r + 1 < n && (long long)nums[r + 1] <= 2LL * nums[i]) {
                ++r;
                insert(trie, nums[r]);
            }
            // trie now contains indices [i, r]
            int curAns = query(trie, nums[i]);
            if (curAns > ans) ans = curAns;
            erase(trie, nums[i]); // remove current left for next iteration
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static class TrieNode {
        TrieNode[] child = new TrieNode[2];
        int cnt;
    }

    private static class Trie {
        private final TrieNode root = new TrieNode();
        int size = 0;

        void insert(int num) {
            TrieNode node = root;
            for (int i = 30; i >= 0; --i) {
                int bit = (num >>> i) & 1;
                if (node.child[bit] == null) node.child[bit] = new TrieNode();
                node = node.child[bit];
                node.cnt++;
            }
            size++;
        }

        void remove(int num) {
            TrieNode node = root;
            for (int i = 30; i >= 0; --i) {
                int bit = (num >>> i) & 1;
                TrieNode nxt = node.child[bit];
                nxt.cnt--;
                if (nxt.cnt == 0) {
                    node.child[bit] = null;
                    return;
                }
                node = nxt;
            }
            size--;
        }

        int maxXor(int num) {
            TrieNode node = root;
            int xor = 0;
            for (int i = 30; i >= 0; --i) {
                int bit = (num >>> i) & 1;
                int want = bit ^ 1;
                if (node.child[want] != null && node.child[want].cnt > 0) {
                    xor |= (1 << i);
                    node = node.child[want];
                } else {
                    node = node.child[bit];
                }
            }
            return xor;
        }
    }

    public int maximumStrongPairXor(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        Trie trie = new Trie();
        int ans = 0;
        int l = 0, r = 0;

        while (l < n) {
            while (r < n && (long) nums[r] <= 2L * nums[l]) {
                if (trie.size > 0) {
                    ans = Math.max(ans, trie.maxXor(nums[r]));
                }
                trie.insert(nums[r]);
                r++;
            }
            // remove current left element before moving l
            trie.remove(nums[l]);
            l++;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        class TrieNode:
            __slots__ = ('child', 'cnt')
            def __init__(self):
                self.child = [None, None]  # 0 and 1
                self.cnt = 0

        BIT = 20  # numbers are < 2^20

        root = TrieNode()

        def insert(x):
            node = root
            for i in range(BIT - 1, -1, -1):
                b = (x >> i) & 1
                if not node.child[b]:
                    node.child[b] = TrieNode()
                node = node.child[b]
                node.cnt += 1

        def delete(x):
            node = root
            stack = []
            for i in range(BIT - 1, -1, -1):
                b = (x >> i) & 1
                stack.append((node, b))
                node = node.child[b]
                node.cnt -= 1
            # clean up nodes with zero count
            while stack:
                parent, b = stack.pop()
                child = parent.child[b]
                if child.cnt == 0:
                    parent.child[b] = None

        def query(x):
            node = root
            if not node.child[0] and not node.child[1]:
                return 0
            res = 0
            for i in range(BIT - 1, -1, -1):
                b = (x >> i) & 1
                toggled = 1 - b
                if node.child[toggled] and node.child[toggled].cnt > 0:
                    res |= (1 << i)
                    node = node.child[toggled]
                else:
                    node = node.child[b]
            return res

        nums.sort()
        left = 0
        ans = 0
        n = len(nums)

        for right in range(n):
            # maintain window where nums[right] <= 2 * nums[left]
            while left < right and nums[left] * 2 < nums[right]:
                delete(nums[left])
                left += 1
            insert(nums[right])
            cur = query(nums[right])
            if cur > ans:
                ans = cur

        return ans
```

## Python3

```python
import sys
from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        # Trie node: [child0, child1, cnt]
        nodes = [[-1, -1, 0]]
        BIT = 20  # since nums[i] <= 2^20 - 1

        def insert(x: int) -> None:
            idx = 0
            for i in range(BIT - 1, -1, -1):
                b = (x >> i) & 1
                if nodes[idx][b] == -1:
                    nodes.append([-1, -1, 0])
                    nodes[idx][b] = len(nodes) - 1
                idx = nodes[idx][b]
                nodes[idx][2] += 1

        def delete(x: int) -> None:
            idx = 0
            for i in range(BIT - 1, -1, -1):
                b = (x >> i) & 1
                nxt = nodes[idx][b]
                idx = nxt
                nodes[idx][2] -= 1

        def query_max_xor(x: int) -> int:
            idx = 0
            res = 0
            for i in range(BIT - 1, -1, -1):
                b = (x >> i) & 1
                want = b ^ 1
                if nodes[idx][want] != -1 and nodes[nodes[idx][want]][2] > 0:
                    res |= (1 << i)
                    idx = nodes[idx][want]
                else:
                    idx = nodes[idx][b]
            return res

        l = 0
        ans = 0
        size = 0  # number of elements currently in trie
        for r, val in enumerate(nums):
            while l < r and nums[l] * 2 < val:
                delete(nums[l])
                size -= 1
                l += 1
            if size > 0:
                ans = max(ans, query_max_xor(val))
            insert(val)
            size += 1
        return ans
```

## C

```c
#include <stdlib.h>

#define MAXBIT 20
#define MAXN 50000
#define MAXNODE (MAXN * 22)

struct Node {
    int child[2];
    int cnt;
};

static struct Node trie[MAXNODE];
static int nodeCnt;

static void initTrie(void) {
    nodeCnt = 1;
    trie[0].child[0] = trie[0].child[1] = -1;
    trie[0].cnt = 0;
}

static int newNode(void) {
    trie[nodeCnt].child[0] = trie[nodeCnt].child[1] = -1;
    trie[nodeCnt].cnt = 0;
    return nodeCnt++;
}

static void insertNum(int x) {
    int cur = 0;
    trie[cur].cnt++;
    for (int b = MAXBIT; b >= 0; --b) {
        int bit = (x >> b) & 1;
        if (trie[cur].child[bit] == -1)
            trie[cur].child[bit] = newNode();
        cur = trie[cur].child[bit];
        trie[cur].cnt++;
    }
}

static void removeNum(int x) {
    int cur = 0;
    trie[cur].cnt--;
    for (int b = MAXBIT; b >= 0; --b) {
        int bit = (x >> b) & 1;
        cur = trie[cur].child[bit];
        trie[cur].cnt--;
    }
}

static int queryMaxXor(int x) {
    int cur = 0;
    int ans = 0;
    for (int b = MAXBIT; b >= 0; --b) {
        int bit = (x >> b) & 1;
        int want = bit ^ 1;
        if (trie[cur].child[want] != -1 && trie[trie[cur].child[want]].cnt > 0) {
            ans |= (1 << b);
            cur = trie[cur].child[want];
        } else {
            cur = trie[cur].child[bit];
        }
    }
    return ans;
}

static int cmpInt(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int maximumStrongPairXor(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpInt);
    initTrie();
    int left = 0;
    int best = 0;
    for (int right = 0; right < numsSize; ++right) {
        insertNum(nums[right]);
        while (left <= right && (long long)nums[right] > 2LL * nums[left]) {
            removeNum(nums[left]);
            ++left;
        }
        int curBest = queryMaxXor(nums[right]);
        if (curBest > best) best = curBest;
    }
    return best;
}
```

## Csharp

```csharp
public class Solution
{
    private const int MAXBIT = 20; // since nums[i] < 2^20

    private class TrieNode
    {
        public int[] Next = new int[2];
        public int Count;
        public TrieNode()
        {
            Next[0] = -1;
            Next[1] = -1;
        }
    }

    private readonly List<TrieNode> _nodes = new List<TrieNode>();

    private void Insert(int val)
    {
        int node = 0;
        for (int k = MAXBIT - 1; k >= 0; --k)
        {
            int b = (val >> k) & 1;
            if (_nodes[node].Next[b] == -1)
            {
                _nodes[node].Next[b] = _nodes.Count;
                _nodes.Add(new TrieNode());
            }
            node = _nodes[node].Next[b];
            _nodes[node].Count++;
        }
    }

    private void Delete(int val)
    {
        int node = 0;
        for (int k = MAXBIT - 1; k >= 0; --k)
        {
            int b = (val >> k) & 1;
            int nextNode = _nodes[node].Next[b];
            node = nextNode;
            _nodes[node].Count--;
        }
    }

    private int QueryMaxXor(int val)
    {
        int node = 0;
        int xor = 0;
        for (int k = MAXBIT - 1; k >= 0; --k)
        {
            int b = (val >> k) & 1;
            int want = 1 - b;
            int nextIdx = _nodes[node].Next[want];
            if (nextIdx != -1 && _nodes[nextIdx].Count > 0)
            {
                xor |= (1 << k);
                node = nextIdx;
            }
            else
            {
                node = _nodes[node].Next[b];
            }
        }
        return xor;
    }

    public int MaximumStrongPairXor(int[] nums)
    {
        Array.Sort(nums);
        _nodes.Clear();
        _nodes.Add(new TrieNode()); // root

        int n = nums.Length;
        int r = 0;
        int answer = 0;

        for (int l = 0; l < n; ++l)
        {
            while (r < n && (long)nums[r] <= 2L * nums[l])
            {
                Insert(nums[r]);
                r++;
            }

            // current window is [l, r-1]
            int cur = QueryMaxXor(nums[l]);
            if (cur > answer) answer = cur;

            Delete(nums[l]); // move left pointer
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumStrongPairXor = function(nums) {
    nums.sort((a, b) => a - b);
    const MAX_BIT = 20; // enough for numbers < 2^20

    function newNode() {
        return { cnt: 0, child: [null, null] };
    }
    const root = newNode();

    function insert(num) {
        let node = root;
        for (let i = MAX_BIT; i >= 0; --i) {
            const bit = (num >> i) & 1;
            if (!node.child[bit]) node.child[bit] = newNode();
            node = node.child[bit];
            node.cnt++;
        }
    }

    function remove(num) {
        let node = root;
        for (let i = MAX_BIT; i >= 0; --i) {
            const bit = (num >> i) & 1;
            node = node.child[bit];
            node.cnt--;
        }
    }

    function query(num) {
        // assume trie is non‑empty when called
        let node = root;
        let xor = 0;
        for (let i = MAX_BIT; i >= 0; --i) {
            const bit = (num >> i) & 1;
            const toggled = bit ^ 1;
            if (node.child[toggled] && node.child[toggled].cnt > 0) {
                xor |= (1 << i);
                node = node.child[toggled];
            } else {
                node = node.child[bit];
            }
        }
        return xor;
    }

    let ans = 0;
    let l = 0;
    for (let r = 0; r < nums.length; ++r) {
        while (l < r && nums[l] * 2 < nums[r]) {
            remove(nums[l]);
            l++;
        }
        if (root.child[0] !== null || root.child[1] !== null) {
            const cur = query(nums[r]);
            if (cur > ans) ans = cur;
        }
        insert(nums[r]);
    }
    return ans;
};
```

## Typescript

```typescript
function maximumStrongPairXor(nums: number[]): number {
    const n = nums.length;
    if (n === 0) return 0;
    nums.sort((a, b) => a - b);
    const MAX_BIT = 20; // numbers are < 2^20

    class TrieNode {
        child: [TrieNode | null, TrieNode | null];
        cnt: number;
        constructor() {
            this.child = [null, null];
            this.cnt = 0;
        }
    }

    const root = new TrieNode();

    function insert(x: number): void {
        let node = root;
        for (let i = MAX_BIT; i >= 0; --i) {
            const b = (x >> i) & 1;
            if (!node.child[b]) node.child[b] = new TrieNode();
            node = node.child[b]!;
            node.cnt++;
        }
    }

    function remove(x: number): void {
        let node = root;
        for (let i = MAX_BIT; i >= 0; --i) {
            const b = (x >> i) & 1;
            const child = node.child[b];
            if (!child) break;
            child.cnt--;
            // optional cleanup:
            // if (child.cnt === 0) node.child[b] = null;
            node = child;
        }
    }

    function query(x: number): number {
        let node = root;
        let ans = 0;
        for (let i = MAX_BIT; i >= 0; --i) {
            const b = (x >> i) & 1;
            const togg = b ^ 1;
            if (node.child[togg] && node.child[togg]!.cnt > 0) {
                ans |= (1 << i);
                node = node.child[togg]!;
            } else {
                node = node.child[b]!;
            }
        }
        return ans;
    }

    let best = 0;
    let r = 0;

    for (let l = 0; l < n; ++l) {
        while (r < n && nums[r] <= 2 * nums[l]) {
            insert(nums[r]);
            r++;
        }
        const cur = query(nums[l]);
        if (cur > best) best = cur;
        remove(nums[l]);
    }

    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumStrongPairXor($nums) {
        sort($nums);
        $bits = 20; // numbers are < 2^20
        $nodes = [];
        $nodes[] = ['child' => [-1, -1], 'cnt' => 0];

        $insert = function(int $num) use (&$nodes, $bits) {
            $node = 0;
            $nodes[$node]['cnt']++;
            for ($i = $bits - 1; $i >= 0; $i--) {
                $b = ($num >> $i) & 1;
                if ($nodes[$node]['child'][$b] === -1) {
                    $nodes[] = ['child' => [-1, -1], 'cnt' => 0];
                    $nodes[$node]['child'][$b] = count($nodes) - 1;
                }
                $node = $nodes[$node]['child'][$b];
                $nodes[$node]['cnt']++;
            }
        };

        $remove = function(int $num) use (&$nodes, $bits) {
            $node = 0;
            $nodes[$node]['cnt']--;
            for ($i = $bits - 1; $i >= 0; $i--) {
                $b = ($num >> $i) & 1;
                $next = $nodes[$node]['child'][$b];
                $node = $next;
                $nodes[$node]['cnt']--;
            }
        };

        $query = function(int $num) use (&$nodes, $bits) {
            if ($nodes[0]['cnt'] == 0) return null;
            $node = 0;
            $xor = 0;
            for ($i = $bits - 1; $i >= 0; $i--) {
                $b = ($num >> $i) & 1;
                $desired = 1 - $b; // opposite bit
                if ($nodes[$node]['child'][$desired] !== -1 &&
                    $nodes[ $nodes[$node]['child'][$desired] ]['cnt'] > 0) {
                    $xor |= (1 << $i);
                    $node = $nodes[$node]['child'][$desired];
                } else {
                    $node = $nodes[$node]['child'][$b];
                }
            }
            return $xor;
        };

        $ans = 0;
        $l = 0;
        $n = count($nums);

        for ($r = 0; $r < $n; $r++) {
            while ($l < $r && $nums[$l] * 2 < $nums[$r]) {
                $remove($nums[$l]);
                $l++;
            }
            $candidate = $query($nums[$r]);
            if ($candidate !== null && $candidate > $ans) {
                $ans = $candidate;
            }
            $insert($nums[$r]);
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumStrongPairXor(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        let n = sorted.count
        if n == 0 { return 0 }
        
        class TrieNode {
            var child: [Int] = [-1, -1]
            var cnt: Int = 0
        }
        
        class Trie {
            let MAX_BIT = 20   // enough for values up to 2^20-1
            var nodes: [TrieNode] = [TrieNode()]
            
            func insert(_ num: Int) {
                var idx = 0
                nodes[idx].cnt += 1
                for b in stride(from: MAX_BIT, through: 0, by: -1) {
                    let bit = (num >> b) & 1
                    if nodes[idx].child[bit] == -1 {
                        nodes.append(TrieNode())
                        nodes[idx].child[bit] = nodes.count - 1
                    }
                    idx = nodes[idx].child[bit]
                    nodes[idx].cnt += 1
                }
            }
            
            func remove(_ num: Int) {
                var idx = 0
                nodes[idx].cnt -= 1
                for b in stride(from: MAX_BIT, through: 0, by: -1) {
                    let bit = (num >> b) & 1
                    let childIdx = nodes[idx].child[bit]
                    idx = childIdx
                    nodes[idx].cnt -= 1
                }
            }
            
            func query(_ num: Int) -> Int {
                var idx = 0
                var ans = 0
                for b in stride(from: MAX_BIT, through: 0, by: -1) {
                    let bit = (num >> b) & 1
                    let prefer = 1 - bit
                    if nodes[idx].child[prefer] != -1 && nodes[nodes[idx].child[prefer]].cnt > 0 {
                        ans |= (1 << b)
                        idx = nodes[idx].child[prefer]
                    } else {
                        idx = nodes[idx].child[bit]
                    }
                }
                return ans
            }
        }
        
        let trie = Trie()
        var l = 0, r = 0
        var maxXor = 0
        
        while l < n {
            while r < n && sorted[r] <= 2 * sorted[l] {
                if r > l { // there is at least one element already in the window
                    let cur = trie.query(sorted[r])
                    if cur > maxXor { maxXor = cur }
                }
                trie.insert(sorted[r])
                r += 1
            }
            // remove leftmost element before moving l forward
            trie.remove(sorted[l])
            l += 1
        }
        
        return maxXor
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumStrongPairXor(nums: IntArray): Int {
        val sorted = nums.clone()
        java.util.Arrays.sort(sorted)
        val n = sorted.size
        val MAX_BIT = 20 // sufficient for values up to 2^20 - 1
        val maxNodes = (n + 5) * 22
        val child = Array(maxNodes) { IntArray(2) { -1 } }
        val cnt = IntArray(maxNodes)
        var nodes = 1 // root is 0

        fun insert(num: Int) {
            var node = 0
            for (k in MAX_BIT downTo 0) {
                val b = (num shr k) and 1
                var nxt = child[node][b]
                if (nxt == -1) {
                    nxt = nodes++
                    child[node][b] = nxt
                }
                node = nxt
                cnt[node]++
            }
        }

        fun delete(num: Int) {
            var node = 0
            for (k in MAX_BIT downTo 0) {
                val b = (num shr k) and 1
                val nxt = child[node][b]
                node = nxt
                cnt[node]--
            }
        }

        fun query(num: Int): Int {
            var node = 0
            var res = 0
            for (k in MAX_BIT downTo 0) {
                val b = (num shr k) and 1
                val prefer = b xor 1
                val nxtPrefer = child[node][prefer]
                if (nxtPrefer != -1 && cnt[nxtPrefer] > 0) {
                    res = res or (1 shl k)
                    node = nxtPrefer
                } else {
                    val nxtSame = child[node][b]
                    if (nxtSame == -1 || cnt[nxtSame] == 0) break
                    node = nxtSame
                }
            }
            return res
        }

        var maxXor = 0
        var j = 0
        for (i in 0 until n) {
            val limit = sorted[i].toLong() * 2L
            while (j < n && sorted[j].toLong() <= limit) {
                insert(sorted[j])
                j++
            }
            val cur = query(sorted[i])
            if (cur > maxXor) maxXor = cur
            delete(sorted[i])
        }
        return maxXor
    }
}
```

## Dart

```dart
class Solution {
  int maximumStrongPairXor(List<int> nums) {
    if (nums.isEmpty) return 0;
    nums.sort();
    const int MAX_BIT = 20;

    class TrieNode {
      List<TrieNode?> child = List.filled(2, null);
      int cnt = 0;
    }

    final TrieNode root = TrieNode();

    void insert(int num) {
      TrieNode node = root;
      for (int i = MAX_BIT; i >= 0; i--) {
        int b = (num >> i) & 1;
        if (node.child[b] == null) node.child[b] = TrieNode();
        node = node.child[b]!;
        node.cnt++;
      }
    }

    void remove(int num) {
      TrieNode node = root;
      for (int i = MAX_BIT; i >= 0; i--) {
        int b = (num >> i) & 1;
        TrieNode next = node.child[b]!;
        next.cnt--;
        if (next.cnt == 0) {
          node.child[b] = null;
          return;
        }
        node = next;
      }
    }

    int query(int num) {
      TrieNode node = root;
      int xor = 0;
      for (int i = MAX_BIT; i >= 0; i--) {
        int b = (num >> i) & 1;
        int toggled = b ^ 1;
        if (node.child[toggled] != null && node.child[toggled]!.cnt > 0) {
          xor |= (1 << i);
          node = node.child[toggled]!;
        } else {
          node = node.child[b]!;
        }
      }
      return xor;
    }

    int ans = 0;
    int left = 0;
    for (int right = 0; right < nums.length; right++) {
      while (left < right && nums[right] > 2 * nums[left]) {
        remove(nums[left]);
        left++;
      }
      if (root.child[0] != null || root.child[1] != null) {
        int cur = query(nums[right]);
        if (cur > ans) ans = cur;
      }
      insert(nums[right]);
    }
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

const maxBit = 19 // since nums[i] < 2^20

type trieNode struct {
	child [2]*trieNode
	cnt   int
}

func (t *trieNode) insert(val int) {
	node := t
	for b := maxBit; b >= 0; b-- {
		bit := (val >> b) & 1
		if node.child[bit] == nil {
			node.child[bit] = &trieNode{}
		}
		node = node.child[bit]
		node.cnt++
	}
}

func (t *trieNode) remove(val int) {
	node := t
	for b := maxBit; b >= 0; b-- {
		bit := (val >> b) & 1
		next := node.child[bit]
		if next == nil { // should not happen
			return
		}
		next.cnt--
		if next.cnt == 0 {
			node.child[bit] = nil
			return
		}
		node = next
	}
}

func (t *trieNode) maxXor(val int) int {
	node := t
	xorVal := 0
	for b := maxBit; b >= 0; b-- {
		bit := (val >> b) & 1
		want := 1 - bit
		if node.child[want] != nil && node.child[want].cnt > 0 {
			xorVal |= 1 << b
			node = node.child[want]
		} else {
			node = node.child[bit]
		}
	}
	return xorVal
}

func maximumStrongPairXor(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	sort.Ints(nums)
	n := len(nums)

	trie := &trieNode{}
	ans := 0
	r := -1

	for i := 0; i < n; i++ {
		// expand right bound while condition holds: nums[r] <= 2*nums[i]
		for r+1 < n && nums[r+1] <= 2*nums[i] {
			r++
			trie.insert(nums[r])
		}
		// now trie contains numbers in [i, r]
		if r >= i { // there is at least nums[i] itself
			cur := trie.maxXor(nums[i])
			if cur > ans {
				ans = cur
			}
		}
		// remove nums[i] before moving left pointer
		trie.remove(nums[i])
	}
	return ans
}
```

## Ruby

```ruby
def maximum_strong_pair_xor(nums)
  nums.sort!
  max_bit = 19
  # Trie node definition
  Node = Struct.new(:child, :cnt) do
    def initialize
      self.child = [nil, nil]
      self.cnt = 0
    end
  end

  root = Node.new

  insert = lambda do |val|
    node = root
    max_bit.downto(0) do |b|
      bit = (val >> b) & 1
      node.child[bit] ||= Node.new
      node = node.child[bit]
      node.cnt += 1
    end
  end

  delete = lambda do |val|
    node = root
    max_bit.downto(0) do |b|
      bit = (val >> b) & 1
      child = node.child[bit]
      return unless child # safety, should not happen
      child.cnt -= 1
      node = child
    end
  end

  query_max_xor = lambda do |val|
    node = root
    xor_val = 0
    max_bit.downto(0) do |b|
      bit = (val >> b) & 1
      toggled = bit ^ 1
      if node.child[toggled] && node.child[toggled].cnt > 0
        xor_val |= (1 << b)
        node = node.child[toggled]
      else
        node = node.child[bit]
      end
    end
    xor_val
  end

  l = 0
  ans = 0
  n = nums.length

  (0...n).each do |r|
    while l < r && nums[l] * 2 < nums[r]
      delete.call(nums[l])
      l += 1
    end
    if root.cnt > 0 # there is at least one number in trie
      cur = query_max_xor.call(nums[r])
      ans = cur if cur > ans
    end
    insert.call(nums[r])
  end

  ans
end
```

## Scala

```scala
object Solution {
  def maximumStrongPairXor(nums: Array[Int]): Int = {
    val sorted = nums.sorted
    val n = sorted.length
    val trie = new Trie()
    var r = 0
    var ans = 0
    for (i <- 0 until n) {
      while (r < n && sorted(r).toLong <= 2L * sorted(i).toLong) {
        trie.insert(sorted(r))
        r += 1
      }
      val cur = trie.maxXor(sorted(i))
      if (cur > ans) ans = cur
      trie.remove(sorted(i))
    }
    ans
  }

  private class Trie {
    private val MAX_BIT = 19 // since nums[i] < 2^20
    private class Node {
      var child: Array[Node] = new Array[Node](2)
      var cnt: Int = 0
    }
    private val root = new Node

    def insert(num: Int): Unit = {
      var node = root
      for (k <- MAX_BIT to 0 by -1) {
        val b = (num >> k) & 1
        if (node.child(b) == null) node.child(b) = new Node
        node = node.child(b)
        node.cnt += 1
      }
    }

    def remove(num: Int): Unit = {
      var node = root
      for (k <- MAX_BIT to 0 by -1) {
        val b = (num >> k) & 1
        node = node.child(b)
        node.cnt -= 1
      }
    }

    def maxXor(num: Int): Int = {
      var node = root
      var res = 0
      for (k <- MAX_BIT to 0 by -1) {
        val b = (num >> k) & 1
        val desired = b ^ 1
        if (node.child(desired) != null && node.child(desired).cnt > 0) {
          res |= (1 << k)
          node = node.child(desired)
        } else {
          node = node.child(b)
        }
      }
      res
    }
  }
}
```

## Rust

```rust
use std::cmp::max;

struct TrieNode {
    child: [i32; 2],
    cnt: i32,
}
impl TrieNode {
    fn new() -> Self {
        TrieNode { child: [-1, -1], cnt: 0 }
    }
}

struct Trie {
    nodes: Vec<TrieNode>,
    max_bit: i32,
}
impl Trie {
    fn new(max_bit: i32) -> Self {
        let mut t = Trie { nodes: Vec::new(), max_bit };
        t.nodes.push(TrieNode::new()); // root
        t
    }

    fn insert(&mut self, mut num: i32) {
        let mut idx = 0usize;
        for k in (0..=self.max_bit).rev() {
            let bit = ((num >> k) & 1) as usize;
            if self.nodes[idx].child[bit] == -1 {
                self.nodes.push(TrieNode::new());
                let new_idx = (self.nodes.len() - 1) as i32;
                self.nodes[idx].child[bit] = new_idx;
            }
            idx = self.nodes[idx].child[bit] as usize;
            self.nodes[idx].cnt += 1;
        }
    }

    fn remove(&mut self, mut num: i32) {
        let mut idx = 0usize;
        for k in (0..=self.max_bit).rev() {
            let bit = ((num >> k) & 1) as usize;
            let next = self.nodes[idx].child[bit] as usize;
            idx = next;
            self.nodes[idx].cnt -= 1;
        }
    }

    fn is_empty(&self) -> bool {
        // root has no count, check if any child exists with cnt>0
        for &c in &self.nodes[0].child {
            if c != -1 && self.nodes[c as usize].cnt > 0 {
                return false;
            }
        }
        true
    }

    fn max_xor(&self, mut num: i32) -> i32 {
        let mut idx = 0usize;
        let mut xor_val = 0i32;
        for k in (0..=self.max_bit).rev() {
            let bit = ((num >> k) & 1) as usize;
            let opp = 1 - bit;
            let child_opp = self.nodes[idx].child[opp];
            if child_opp != -1 && self.nodes[child_opp as usize].cnt > 0 {
                xor_val |= 1 << k;
                idx = child_opp as usize;
            } else {
                // must go to same bit branch (it exists because trie not empty)
                let child_same = self.nodes[idx].child[bit];
                idx = child_same as usize;
            }
        }
        xor_val
    }
}

impl Solution {
    pub fn maximum_strong_pair_xor(nums: Vec<i32>) -> i32 {
        if nums.is_empty() {
            return 0;
        }
        let mut a = nums.clone();
        a.sort_unstable();

        const MAX_BIT: i32 = 19; // since nums[i] <= 2^20 - 1
        let mut trie = Trie::new(MAX_BIT);
        let mut left = 0usize;
        let mut ans = 0i32;

        for right in 0..a.len() {
            while left < right && (a[right] as i64) > 2 * (a[left] as i64) {
                trie.remove(a[left]);
                left += 1;
            }
            if !trie.is_empty() {
                let cur = trie.max_xor(a[right]);
                ans = max(ans, cur);
            }
            trie.insert(a[right]);
        }

        ans
    }
}
```

## Racket

```racket
(struct node (children cnt) #:mutable)

(define (maximum-strong-pair-xor nums)
  (let* ((sorted (list->vector (sort (copy-list nums) <)))
         (n (vector-length sorted))
         (MAXBIT 20)
         (root (make-node (make-vector 2 #f) 0)))
    (define (bit-at n k)
      (bitwise-and (arithmetic-shift n (- k)) 1))
    (define (insert num)
      (let loop ((cur root) (bit (sub1 MAXBIT)))
        (set-node-cnt! cur (+ (node-cnt cur) 1))
        (when (>= bit 0)
          (let* ((b (bit-at num bit))
                 (child (vector-ref (node-children cur) b)))
            (unless child
              (set! child (make-node (make-vector 2 #f) 0))
              (vector-set! (node-children cur) b child))
            (loop child (sub1 bit))))))
    (define (delete num)
      (let loop ((cur root) (bit (sub1 MAXBIT)))
        (set-node-cnt! cur (- (node-cnt cur) 1))
        (when (>= bit 0)
          (let* ((b (bit-at num bit))
                 (child (vector-ref (node-children cur) b)))
            (loop child (sub1 bit))))))
    (define (query-max-xor num)
      (if (= (node-cnt root) 0)
          0
          (let loop ((cur root) (bit (sub1 MAXBIT)) (acc 0))
            (if (< bit 0)
                acc
                (let* ((b (bit-at num bit))
                       (desired (if (= b 0) 1 0))
                       (child-desired (vector-ref (node-children cur) desired)))
                  (if (and child-desired (> (node-cnt child-desired) 0))
                      (loop child-desired (sub1 bit)
                            (bitwise-ior acc (arithmetic-shift 1 bit)))
                      (let ((child-same (vector-ref (node-children cur) b)))
                        (loop child-same (sub1 bit) acc))))))))
    (define ans (box 0))
    (define l 0)
    (for ([r (in-range n)])
      (let ((val (vector-ref sorted r)))
        ;; shrink window while smallest element no longer satisfies condition
        (let loop ((lcur l))
          (if (and (< lcur n) (< (* 2 (vector-ref sorted lcur)) val))
              (begin
                (delete (vector-ref sorted lcur))
                (loop (add1 lcur)))
              (set! l lcur)))
        ;; query with existing numbers in window
        (when (> (node-cnt root) 0)
          (let ((cand (query-max-xor val)))
            (when (> cand (unbox ans))
              (set-box! ans cand))))
        (insert val)))
    (unbox ans)))
```

## Erlang

```erlang
-spec maximum_strong_pair_xor(Nums :: [integer()]) -> integer().
maximum_strong_pair_xor(Nums) ->
    Sorted = lists:sort(Nums),
    SortedT = list_to_tuple(Sorted),
    N = tuple_size(SortedT),
    Trie0 = #{0 => {undefined, undefined, 0}},
    State0 = {Trie0, 1},
    loop(0, 0, N, SortedT, State0, 0).

%% main loop over left pointer I
loop(I, R, N, SortedT, State, MaxAns) when I < N ->
    X = element(I + 1, SortedT),
    {State2, R2} = expand(R, N, X, SortedT, State),
    {TrieMap, _} = State2,
    Cand = trie_query(X, TrieMap),
    NewMax = erlang:max(MaxAns, Cand),
    State3 = trie_delete(X, State2),
    loop(I + 1, R2, N, SortedT, State3, NewMax);
loop(_, _, _, _, _, MaxAns) ->
    MaxAns.

%% expand right pointer while condition holds
expand(R, N, X, SortedT, State) when R < N ->
    Y = element(R + 1, SortedT),
    if Y =< 2 * X ->
            {NewTrie, NewNext} = trie_insert(Y, State),
            expand(R + 1, N, X, SortedT, {NewTrie, NewNext});
       true ->
            {State, R}
    end;
expand(R, _N, _X, _SortedT, State) ->
    {State, R}.

%% Insert number into trie
trie_insert(Num, {Nodes, Next}) ->
    {NewNodes, NewNext} = insert_bit(Num, 19, 0, Nodes, Next),
    {NewNodes, NewNext}.

insert_bit(_Num, -1, NodeId, Nodes, Next) ->
    Node = maps:get(NodeId, Nodes),
    Cnt = element(3, Node),
    Updated = setelement(3, Node, Cnt + 1),
    {maps:put(NodeId, Updated, Nodes), Next};
insert_bit(Num, Pos, NodeId, Nodes, Next) when Pos >= 0 ->
    Node = maps:get(NodeId, Nodes),
    Cnt = element(3, Node),
    UpdatedNode = setelement(3, Node, Cnt + 1),
    Nodes1 = maps:put(NodeId, UpdatedNode, Nodes),
    Bit = (Num bsr Pos) band 1,
    ChildId = case Bit of
                  0 -> element(1, UpdatedNode);
                  1 -> element(2, UpdatedNode)
              end,
    case ChildId of
        undefined ->
            NewChildId = Next,
            Next1 = Next + 1,
            ChildNode = {undefined, undefined, 0},
            Nodes2 = maps:put(NewChildId, ChildNode, Nodes1),
            UpdatedParent = set_child(UpdatedNode, Bit, NewChildId),
            Nodes3 = maps:put(NodeId, UpdatedParent, Nodes2),
            insert_bit(Num, Pos - 1, NewChildId, Nodes3, Next1);
        _ ->
            insert_bit(Num, Pos - 1, ChildId, Nodes1, Next)
    end.

%% Delete number from trie
trie_delete(Num, {Nodes, Next}) ->
    NewNodes = delete_bit(Num, 19, 0, Nodes),
    {NewNodes, Next}.

delete_bit(_Num, -1, NodeId, Nodes) ->
    Node = maps:get(NodeId, Nodes),
    Cnt = element(3, Node),
    Updated = setelement(3, Node, Cnt - 1),
    maps:put(NodeId, Updated, Nodes);
delete_bit(Num, Pos, NodeId, Nodes) when Pos >= 0 ->
    Node = maps:get(NodeId, Nodes),
    Cnt = element(3, Node),
    UpdatedNode = setelement(3, Node, Cnt - 1),
    Nodes1 = maps:put(NodeId, UpdatedNode, Nodes),
    Bit = (Num bsr Pos) band 1,
    ChildId = case Bit of
                  0 -> element(1, UpdatedNode);
                  1 -> element(2, UpdatedNode)
              end,
    delete_bit(Num, Pos - 1, ChildId, Nodes1).

%% Query maximum xor with Num in current trie
trie_query(Num, Nodes) ->
    query_bit(Num, 19, 0, 0, Nodes).

query_bit(_Num, -1, _NodeId, Acc, _Nodes) ->
    Acc;
query_bit(Num, Pos, NodeId, Acc, Nodes) when Pos >= 0 ->
    Node = maps:get(NodeId, Nodes),
    Bit = (Num bsr Pos) band 1,
    PrefBit = 1 - Bit,
    ChildPref = case PrefBit of
                    0 -> element(1, Node);
                    1 -> element(2, Node)
                end,
    case ChildPref of
        undefined ->
            ChildSame = case Bit of
                            0 -> element(1, Node);
                            1 -> element(2, Node)
                        end,
            query_bit(Num, Pos - 1, ChildSame, Acc, Nodes);
        CId ->
            {_, _, Cnt} = maps:get(CId, Nodes),
            if Cnt > 0 ->
                    NewAcc = Acc bor (1 bsl Pos),
                    query_bit(Num, Pos - 1, CId, NewAcc, Nodes);
               true ->
                    ChildSame = case Bit of
                                    0 -> element(1, Node);
                                    1 -> element(2, Node)
                                end,
                    query_bit(Num, Pos - 1, ChildSame, Acc, Nodes)
            end
    end.

%% Helper to set child pointer in a node tuple
set_child(Node, 0, ChildId) ->
    setelement(1, Node, ChildId);
set_child(Node, 1, ChildId) ->
    setelement(2, Node, ChildId).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_strong_pair_xor(nums :: [integer]) :: integer
  def maximum_strong_pair_xor(nums) do
    sorted = nums |> Enum.sort() |> List.to_tuple()
    n = tuple_size(sorted)
    max_val = Enum.max(nums)
    bits = if max_val == 0, do: 1, else: :math.floor(:math.log2(max_val)) + 1 |> trunc()

    root = %{}
    {_, _, ans} = process(sorted, n, bits, 0, 0, root, 0)
    ans
  end

  defp process(_sorted, n, _bits, idx, l, root, ans) when idx == n do
    {idx, l, ans}
  end

  defp process(sorted, n, bits, idx, l, root, ans) do
    y = :erlang.element(idx + 1, sorted)

    {new_l, new_root} = slide_left(sorted, n, bits, l, root, y)

    cur_max =
      if map_size(new_root) == 0 do
        0
      else
        query(new_root, y, bits - 1)
      end

    ans2 = if cur_max > ans, do: cur_max, else: ans
    root2 = insert(new_root, y, bits - 1)

    process(sorted, n, bits, idx + 1, new_l, root2, ans2)
  end

  defp slide_left(_sorted, _n, _bits, l, root, _y) when l < 0 do
    {l, root}
  end

  defp slide_left(sorted, n, bits, l, root, y) do
    if l < n and :erlang.element(l + 1, sorted) * 2 < y do
      x = :erlang.element(l + 1, sorted)
      new_root = delete(root, x, bits - 1)
      slide_left(sorted, n, bits, l + 1, new_root, y)
    else
      {l, root}
    end
  end

  defp insert(node, _num, bit) when bit < 0 do
    cnt = Map.get(node, :cnt, 0) + 1
    Map.put(node, :cnt, cnt)
  end

  defp insert(node, num, bit) do
    cnt = Map.get(node, :cnt, 0) + 1
    b = (num >>> bit) &&& 1
    key = if b == 0, do: :zero, else: :one
    child = Map.get(node, key, %{})
    new_child = insert(child, num, bit - 1)
    node
    |> Map.put(:cnt, cnt)
    |> Map.put(key, new_child)
  end

  defp delete(node, _num, bit) when bit < 0 do
    cnt = Map.get(node, :cnt, 0) - 1
    if cnt == 0, do: %{}, else: Map.put(node, :cnt, cnt)
  end

  defp delete(node, num, bit) do
    cnt = Map.get(node, :cnt, 0) - 1
    b = (num >>> bit) &&& 1
    key = if b == 0, do: :zero, else: :one
    child = Map.get(node, key, %{})
    new_child = delete(child, num, bit - 1)
    node = Map.put(node, :cnt, cnt)

    cond do
      map_size(new_child) == 0 ->
        Map.delete(node, key)

      true ->
        Map.put(node, key, new_child)
    end
  end

  defp query(_node, _num, bit) when bit < 0, do: 0

  defp query(node, num, bit) do
    desired = 1 - ((num >>> bit) &&& 1)
    pref_key = if desired == 0, do: :zero, else: :one
    alt_key = if desired == 0, do: :one, else: :zero

    cond do
      Map.has_key?(node, pref_key) ->
        (1 <<< bit) + query(Map.get(node, pref_key), num, bit - 1)

      Map.has_key?(node, alt_key) ->
        query(Map.get(node, alt_key), num, bit - 1)

      true ->
        0
    end
  end
end
```
