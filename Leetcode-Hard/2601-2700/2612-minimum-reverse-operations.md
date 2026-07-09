# 2612. Minimum Reverse Operations

## Cpp

```cpp
class Solution {
public:
    vector<int> minReverseOperations(int n, int p, vector<int>& banned, int k) {
        unordered_set<int> ban(banned.begin(), banned.end());
        vector<int> ans(n, -1);
        set<int> evenSet, oddSet;
        for (int i = 0; i < n; ++i) {
            if (i == p || ban.count(i)) continue;
            if (i % 2 == 0) evenSet.insert(i);
            else oddSet.insert(i);
        }
        queue<int> q;
        ans[p] = 0;
        q.push(p);
        while (!q.empty()) {
            int pos = q.front(); q.pop();
            int d = ans[pos];
            int low = max(0, pos - k + 1);
            int high = min(pos, n - k);
            if (low > high) continue;
            int left = 2 * low + k - 1 - pos;
            int right = 2 * high + k - 1 - pos;
            // parity of reachable positions
            int parity = left & 1;
            set<int>& s = (parity == 0 ? evenSet : oddSet);
            auto it = s.lower_bound(left);
            while (it != s.end() && *it <= right) {
                int nxt = *it;
                ans[nxt] = d + 1;
                q.push(nxt);
                it = s.erase(it);
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
    public int[] minReverseOperations(int n, int p, int[] banned, int k) {
        boolean[] isBanned = new boolean[n];
        for (int b : banned) isBanned[b] = true;

        TreeSet<Integer> even = new TreeSet<>();
        TreeSet<Integer> odd = new TreeSet<>();

        for (int i = 0; i < n; i++) {
            if (i == p || isBanned[i]) continue;
            if ((i & 1) == 0) even.add(i);
            else odd.add(i);
        }

        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        ans[p] = 0;

        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.add(p);

        while (!q.isEmpty()) {
            int pos = q.poll();

            int left = Math.max(0, pos - k + 1);
            int right = Math.min(pos, n - k);
            if (left > right) continue;

            int low = 2 * left + k - 1 - pos;
            int high = 2 * right + k - 1 - pos;
            low = Math.max(low, 0);
            high = Math.min(high, n - 1);

            TreeSet<Integer> set = (((k - 1 - pos) & 1) == 0) ? even : odd;

            Integer nxt = set.ceiling(low);
            while (nxt != null && nxt <= high) {
                ans[nxt] = ans[pos] + 1;
                q.add(nxt);
                set.remove(nxt);
                nxt = set.ceiling(low);
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minReverseOperations(self, n, p, banned, k):
        """
        :type n: int
        :type p: int
        :type banned: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        import bisect

        ans = [-1] * n
        ans[p] = 0

        banned_set = set(banned)

        even = []
        odd = []
        for i in range(n):
            if i == p or i in banned_set:
                continue
            if i & 1:
                odd.append(i)
            else:
                even.append(i)

        q = deque([p])
        k_minus_1 = k - 1
        parity_target_mod = k_minus_1 & 1

        while q:
            cur = q.popleft()
            L = max(0, cur - k_minus_1)
            R = min(n - 1, cur + k_minus_1)

            # required parity for reachable positions
            target_parity = (parity_target_mod - (cur & 1)) & 1

            lst = even if target_parity == 0 else odd
            lo = bisect.bisect_left(lst, L)
            hi = lo
            while hi < len(lst) and lst[hi] <= R:
                nxt = lst[hi]
                ans[nxt] = ans[cur] + 1
                q.append(nxt)
                hi += 1
            # remove visited positions
            if hi > lo:
                del lst[lo:hi]

        return ans
```

## Python3

```python
import sys
from collections import deque
from typing import List

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ans = [-1] * n
        banned_set = set(banned)

        # DSU-like "next" array to skip visited/banned positions (step of 2)
        parent = list(range(n + 2))

        def find(x: int) -> int:
            if x >= n:
                return n
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        # mark banned positions as removed
        for b in banned_set:
            if b < n:
                parent[b] = b + 2

        # start position
        ans[p] = 0
        parent[p] = p + 2
        q = deque([p])

        while q:
            pos = q.popleft()
            step = ans[pos] + 1

            low = max(0, pos - k + 1)
            high = min(pos, n - k)
            if low > high:
                continue

            L = 2 * low + k - 1 - pos
            R = 2 * high + k - 1 - pos

            # clamp to array bounds
            L = max(L, 0)
            R = min(R, n - 1)

            needed_parity = (k - 1 - pos) & 1
            if (L & 1) != needed_parity:
                L += 1
            if (R & 1) != needed_parity:
                R -= 1
            if L > R:
                continue

            cur = find(L)
            while cur <= R:
                ans[cur] = step
                q.append(cur)
                # remove cur from future consideration
                parent[cur] = find(cur + 2)
                cur = find(cur)

        return ans
```

## C

```c
#include <stdlib.h>

static int n_global;
static int *nxt;

/* Find the smallest unvisited index >= x of the same parity */
static int find_next(int x) {
    if (x >= n_global) return n_global;
    if (nxt[x] == x) return x;
    return nxt[x] = find_next(nxt[x]);
}

/* Remove index i from future consideration */
static void remove_idx(int i) {
    nxt[i] = find_next(i + 2);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minReverseOperations(int n, int p, int* banned, int bannedSize, int k, int* returnSize) {
    n_global = n;
    nxt = (int *)malloc((n + 2) * sizeof(int));
    for (int i = 0; i <= n; ++i) nxt[i] = i;

    int *ans = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) ans[i] = -1;

    /* mark banned positions as removed */
    for (int i = 0; i < bannedSize; ++i) {
        int b = banned[i];
        if (b >= 0 && b < n) remove_idx(b);
    }

    /* BFS initialization */
    int *queue = (int *)malloc(n * sizeof(int));
    int front = 0, back = 0;

    ans[p] = 0;
    queue[back++] = p;
    remove_idx(p);   // mark visited

    while (front < back) {
        int cur = queue[front++];
        int left = cur - k + 1;
        if (left < 0) left = 0;
        int right = cur + k - 1;
        if (right >= n) right = n - 1;

        int parity = (cur + k - 1) & 1;          // required parity of next positions
        int start = left;
        if ((start & 1) != parity) ++start;     // first index with correct parity

        if (start > right) continue;

        for (int idx = find_next(start); idx <= right; idx = find_next(idx)) {
            ans[idx] = ans[cur] + 1;
            queue[back++] = idx;
            remove_idx(idx);
        }
    }

    free(queue);
    free(nxt);
    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] MinReverseOperations(int n, int p, int[] banned, int k) {
        var ans = new int[n];
        Array.Fill(ans, -1);
        bool[] isBanned = new bool[n];
        foreach (var b in banned) isBanned[b] = true;

        // sets for even and odd positions that are not visited yet
        SortedSet<int>[] sets = new SortedSet<int>[2];
        sets[0] = new SortedSet<int>();
        sets[1] = new SortedSet<int>();

        for (int i = 0; i < n; i++) {
            if (!isBanned[i] && i != p) {
                sets[i & 1].Add(i);
            }
        }

        var q = new Queue<int>();
        ans[p] = 0;
        q.Enqueue(p);

        int maxDist = k - 1;

        while (q.Count > 0) {
            int cur = q.Dequeue();
            int wantedParity = ((k - 1) - cur) & 1; // j % 2 == (k-1 - cur) mod 2
            int low = Math.Max(0, cur - maxDist);
            int high = Math.Min(n - 1, cur + maxDist);

            var view = sets[wantedParity].GetViewBetween(low, high);
            while (view.Count > 0) {
                int nxt = view.First(); // smallest element in the view
                ans[nxt] = ans[cur] + 1;
                q.Enqueue(nxt);
                view.Remove(nxt); // removes from underlying set as well
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} p
 * @param {number[]} banned
 * @param {number} k
 * @return {number[]}
 */
var minReverseOperations = function(n, p, banned, k) {
    const ans = new Array(n).fill(-1);
    // DSU parent array for skipping visited positions of same parity
    const parent = new Int32Array(n + 2);
    for (let i = 0; i < n + 2; ++i) parent[i] = i;
    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    // remove a position from future consideration
    const erase = (idx) => {
        if (idx < n) parent[idx] = find(idx + 2);
    };
    // mark banned positions as erased
    for (const b of banned) {
        erase(b);
    }
    const queue = [];
    let qh = 0;
    ans[p] = 0;
    queue.push(p);
    erase(p); // visited
    
    while (qh < queue.length) {
        const pos = queue[qh++];
        const dist = ans[pos];
        const left = Math.max(0, pos - k + 1);
        const right = Math.min(n - 1, pos + k - 1);
        const needParity = ((k - 1 - pos) & 1); // required parity for reachable indices
        let startIdx = left;
        if ((startIdx & 1) !== needParity) startIdx++;
        let idx = find(startIdx);
        while (idx <= right) {
            ans[idx] = dist + 1;
            queue.push(idx);
            erase(idx);
            idx = find(idx); // next candidate after erasing current
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minReverseOperations(n: number, p: number, banned: number[], k: number): number[] {
    const ans = new Array<number>(n).fill(-1);
    const parent = new Array<number>(n + 2);
    for (let i = 0; i < n + 2; i++) parent[i] = i;

    const find = (x: number): number => {
        if (x >= n) return n;
        let root = x;
        while (parent[root] !== root) root = parent[root];
        // path compression
        while (parent[x] !== x) {
            const nxt = parent[x];
            parent[x] = root;
            x = nxt;
        }
        return root;
    };

    const remove = (idx: number): void => {
        if (idx < n) parent[idx] = find(idx + 2);
    };

    for (const b of banned) remove(b);
    remove(p);

    ans[p] = 0;
    const queue: number[] = [p];
    let head = 0;

    while (head < queue.length) {
        const cur = queue[head++];
        const d = ans[cur];

        const left = Math.max(0, cur - k + 1);
        const right = Math.min(cur, n - k);
        if (left > right) continue;

        let minPos = 2 * left + k - 1 - cur;
        let maxPos = 2 * right + k - 1 - cur;
        if (minPos < 0) minPos = 0;
        if (maxPos >= n) maxPos = n - 1;

        const parity = ((k - 1 - cur) & 1);
        if ((minPos & 1) !== parity) minPos++;

        for (let x = find(minPos); x <= maxPos && x < n; x = find(x)) {
            ans[x] = d + 1;
            queue.push(x);
            parent[x] = find(x + 2);
        }
    }

    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $p
     * @param Integer[] $banned
     * @param Integer $k
     * @return Integer[]
     */
    function minReverseOperations($n, $p, $banned, $k) {
        $ans = array_fill(0, $n, -1);
        $visited = array_fill(0, $n, false);

        // DSU parents for each parity (size n+2 to avoid overflow)
        $size = $n + 2;
        $parent0 = array_fill(0, $size, 0);
        $parent1 = array_fill(0, $size, 0);
        for ($i = 0; $i < $size; $i++) {
            $parent0[$i] = $i;
            $parent1[$i] = $i;
        }

        // recursive find with path compression
        $find = function (&$parent, $x) use (&$find, $size) {
            if ($x >= $size) return $size - 1;
            if ($parent[$x] != $x) {
                $parent[$x] = $find($parent, $parent[$x]);
            }
            return $parent[$x];
        };

        // helper to remove an index from its parity set
        $remove = function (&$parent, $idx) use ($find, $size) {
            if ($idx + 2 < $size) {
                $parent[$idx] = $find($parent, $idx + 2);
            } else {
                $parent[$idx] = $size - 1;
            }
        };

        // mark banned positions as visited and remove them from DSU
        foreach ($banned as $b) {
            $visited[$b] = true;
            if (($b & 1) == 0) {
                $remove($parent0, $b);
            } else {
                $remove($parent1, $b);
            }
        }

        // start BFS from position p
        $queue = new SplQueue();
        $ans[$p] = 0;
        $visited[$p] = true;
        $queue->enqueue($p);
        if (($p & 1) == 0) {
            $remove($parent0, $p);
        } else {
            $remove($parent1, $p);
        }

        while (!$queue->isEmpty()) {
            $i = $queue->dequeue();

            // possible subarray start indices that include i
            $L = max(0, $i - $k + 1);
            $R = min($i, $n - $k);
            if ($L > $R) continue;

            $parityWanted = ($i + $k - 1) & 1; // parity of reachable positions

            // corresponding range of new positions after reversal
            $jLow  = 2 * $L + $k - 1 - $i;
            $jHigh = 2 * $R + $k - 1 - $i;

            if ($jLow < 0) $jLow = 0;
            if ($jHigh >= $n) $jHigh = $n - 1;

            // align jLow to correct parity
            if (($jLow & 1) != $parityWanted) $jLow++;

            if ($parityWanted == 0) {
                $cur = $find($parent0, $jLow);
                while ($cur <= $jHigh) {
                    $ans[$cur] = $ans[$i] + 1;
                    $queue->enqueue($cur);
                    // remove cur from set
                    $remove($parent0, $cur);
                    $cur = $find($parent0, $cur);
                }
            } else {
                $cur = $find($parent1, $jLow);
                while ($cur <= $jHigh) {
                    $ans[$cur] = $ans[$i] + 1;
                    $queue->enqueue($cur);
                    // remove cur from set
                    $remove($parent1, $cur);
                    $cur = $find($parent1, $cur);
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    class DSU {
        var parent: [Int]
        init(_ size: Int) {
            // creates array from 0 to size inclusive
            self.parent = Array(0...size)
        }
        func find(_ x: Int) -> Int {
            if parent[x] != x {
                parent[x] = find(parent[x])
            }
            return parent[x]
        }
        func union(_ x: Int, _ y: Int) {
            let fx = find(x)
            let fy = find(y)
            if fx != fy {
                parent[fx] = fy
            }
        }
    }

    func minReverseOperations(_ n: Int, _ p: Int, _ banned: [Int], _ k: Int) -> [Int] {
        var answer = Array(repeating: -1, count: n)
        let dsu = DSU(n + 1) // indices 0...n+1, n+1 is sentinel beyond last valid index

        // mark banned positions as visited (removed from future consideration)
        for b in banned {
            dsu.union(b, min(b + 2, n + 1))
        }
        // start position also considered visited
        dsu.union(p, min(p + 2, n + 1))

        var queue = [Int]()
        var head = 0
        answer[p] = 0
        queue.append(p)

        while head < queue.count {
            let cur = queue[head]
            head += 1
            let dist = answer[cur]

            // reachable range in one operation
            let L = max(0, cur - k + 1)
            let R = min(n - 1, cur + k - 1)

            // required parity for target positions
            let wantedParity = (cur + k - 1) & 1

            var start = L
            if (start & 1) != wantedParity {
                start += 1
            }

            var idx = dsu.find(start)
            while idx <= R {
                answer[idx] = dist + 1
                queue.append(idx)
                // remove idx from future consideration
                dsu.union(idx, min(idx + 2, n + 1))
                idx = dsu.find(idx) // next unvisited index with same parity
            }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque
import java.util.TreeSet

class Solution {
    fun minReverseOperations(n: Int, p: Int, banned: IntArray, k: Int): IntArray {
        val isBanned = BooleanArray(n)
        for (b in banned) isBanned[b] = true

        // TreeSets for positions of each parity that are not visited and not banned
        val sets = arrayOf(TreeSet<Int>(), TreeSet<Int>())
        for (i in 0 until n) {
            if (!isBanned[i] && i != p) {
                sets[i and 1].add(i)
            }
        }

        val ans = IntArray(n) { -1 }
        ans[p] = 0
        val q: ArrayDeque<Int> = ArrayDeque()
        q.add(p)

        while (q.isNotEmpty()) {
            val cur = q.removeFirst()

            // possible left boundaries of the subarray that includes cur
            val left = kotlin.math.max(0, cur - k + 1)
            val right = kotlin.math.min(cur, n - k)
            if (left > right) continue

            var a = 2 * left + k - 1 - cur
            var b = 2 * right + k - 1 - cur
            var lo = kotlin.math.min(a, b)
            var hi = kotlin.math.max(a, b)

            // clamp to array bounds
            lo = kotlin.math.max(lo, 0)
            hi = kotlin.math.min(hi, n - 1)

            // all reachable positions have the same parity
            val parity = (k - 1 - cur) and 1

            var nxt = sets[parity].ceiling(lo)
            while (nxt != null && nxt <= hi) {
                ans[nxt] = ans[cur] + 1
                q.add(nxt)
                // remove and fetch next candidate
                sets[parity].remove(nxt)
                nxt = sets[parity].ceiling(lo)
            }
        }

        return ans
    }
}
```

## Dart

```dart
import 'dart:collection';
import 'dart:math';

class Solution {
  List<int> minReverseOperations(int n, int p, List<int> banned, int k) {
    List<int> ans = List.filled(n, -1);
    // DSU parent array for skipping visited indices (step of 2)
    List<int> parent = List.filled(n + 2, 0);
    for (int i = 0; i < n + 2; ++i) parent[i] = i;

    int find(int x) {
      while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
      }
      return x;
    }

    void unite(int x, int y) {
      int fx = find(x);
      int fy = find(y);
      if (fx != fy) parent[fx] = fy;
    }

    // remove banned positions from DSU
    for (int b in banned) {
      if (b >= 0 && b < n) unite(b, b + 2);
    }

    // BFS initialization
    List<int> queue = [];
    int qIdx = 0;
    ans[p] = 0;
    queue.add(p);
    unite(p, p + 2); // mark start as visited

    while (qIdx < queue.length) {
      int cur = queue[qIdx++];
      // compute feasible window left/right for subarray start
      int left = max(0, cur - k + 1);
      int right = min(cur, n - k);
      if (left > right) continue;

      int low = 2 * left + k - 1 - cur;
      int high = 2 * right + k - 1 - cur;
      low = max(low, 0);
      high = min(high, n - 1);

      int parity = ((k - 1 - cur) & 1);
      if ((low & 1) != parity) low++;
      if ((high & 1) != parity) high--;

      if (low > high) continue;

      int x = find(low);
      while (x <= high) {
        ans[x] = ans[cur] + 1;
        queue.add(x);
        unite(x, x + 2);
        x = find(x);
      }
    }

    return ans;
  }
}
```

## Golang

```go
func minReverseOperations(n int, p int, banned []int, k int) []int {
    ans := make([]int, n)
    for i := range ans {
        ans[i] = -1
    }
    parent := make([]int, n+2)
    for i := 0; i < n+2; i++ {
        parent[i] = i
    }

    var find func(int) int
    find = func(x int) int {
        if x >= n {
            return n
        }
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    erase := func(x int) {
        if x < n {
            parent[x] = find(x + 2)
        }
    }

    // remove banned positions
    for _, b := range banned {
        erase(b)
    }
    // start position is visited
    erase(p)

    q := make([]int, n)
    head, tail := 0, 0
    ans[p] = 0
    q[tail] = p
    tail++

    parityMask := (k - 1) & 1

    for head < tail {
        cur := q[head]
        head++
        d := ans[cur]

        low := cur - (k - 1)
        if low < 0 {
            low = 0
        }
        high := cur + (k - 1)
        if high >= n {
            high = n - 1
        }

        // required parity for next positions: y%2 == (k-1-cur)%2
        needParity := ((k - 1) - cur) & 1
        start := low
        if (start&1) != needParity {
            start++
        }
        for {
            idx := find(start)
            if idx > high {
                break
            }
            ans[idx] = d + 1
            q[tail] = idx
            tail++
            erase(idx)
            start = idx + 2
        }

        // also need to consider the opposite parity when k is even?
        // The condition (cur + y) % 2 == (k-1)%2 already handled by needParity.
        // No further processing required.
        _ = parityMask // silence unused variable warning if any
    }
    return ans
}
```

## Ruby

```ruby
def min_reverse_operations(n, p, banned, k)
  dist = Array.new(n, -1)
  parent = Array.new(n + 2) { |i| i }
  find = lambda do |x|
    while x < parent.length && parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  banned.each do |b|
    parent[b] = find.call(b + 2)
  end

  queue = []
  head = 0
  dist[p] = 0
  queue << p
  parent[p] = find.call(p + 2)

  while head < queue.length
    cur = queue[head]
    head += 1
    left = cur - (k - 1)
    left = 0 if left < 0
    right = cur + (k - 1)
    right = n - 1 if right >= n
    target_parity = (cur + k - 1) & 1
    start = left
    start += 1 if (start & 1) != target_parity
    idx = find.call(start)
    while idx <= right
      dist[idx] = dist[cur] + 1
      queue << idx
      parent[idx] = find.call(idx + 2)
      idx = find.call(idx)
    end
  end

  dist
end
```

## Scala

```scala
import java.util.{ArrayDeque, TreeSet}

object Solution {
  def minReverseOperations(n: Int, p: Int, banned: Array[Int], k: Int): Array[Int] = {
    val blocked = new Array[Boolean](n)
    for (b <- banned) blocked(b) = true

    val ans = Array.fill[Int](n)(-1)
    ans(p) = 0

    val evenSet = new TreeSet[Int]()
    val oddSet = new TreeSet[Int]()

    var i = 0
    while (i < n) {
      if (!blocked(i) && i != p) {
        if ((i & 1) == 0) evenSet.add(i) else oddSet.add(i)
      }
      i += 1
    }

    val queue = new ArrayDeque[Int]()
    queue.add(p)

    while (!queue.isEmpty) {
      val cur = queue.poll()
      val dist = ans(cur)

      // parity of target positions reachable from cur
      val needParity = ((k - 1) + cur) & 1
      val set = if (needParity == 0) evenSet else oddSet

      var left = Math.max(0, cur - k + 1)
      left = Math.max(left, k - 1 - cur)

      var right = Math.min(n - 1, cur + k - 1)
      right = Math.min(right, 2 * n - k - 1 - cur)

      var cand = set.ceiling(left)
      while (cand != null && cand <= right) {
        ans(cand) = dist + 1
        queue.add(cand)
        set.remove(cand)
        cand = set.ceiling(left)
      }
    }

    ans
  }
}
```

## Rust

```rust
use std::collections::{BTreeSet, VecDeque};

impl Solution {
    pub fn min_reverse_operations(n: i32, p: i32, banned: Vec<i32>, k: i32) -> Vec<i32> {
        let n_usize = n as usize;
        let mut is_banned = vec![false; n_usize];
        for b in banned {
            is_banned[b as usize] = true;
        }

        let mut ans = vec![-1i32; n_usize];
        let start = p as usize;
        ans[start] = 0;

        let mut even_set: BTreeSet<usize> = BTreeSet::new();
        let mut odd_set: BTreeSet<usize> = BTreeSet::new();

        for i in 0..n_usize {
            if is_banned[i] || i == start {
                continue;
            }
            if i % 2 == 0 {
                even_set.insert(i);
            } else {
                odd_set.insert(i);
            }
        }

        let mut dq: VecDeque<usize> = VecDeque::new();
        dq.push_back(start);
        let k_minus1 = (k - 1) as usize;

        while let Some(cur) = dq.pop_front() {
            let cur_dist = ans[cur];
            let left = if cur >= k_minus1 { cur - k_minus1 } else { 0 };
            let right = std::cmp::min(n_usize - 1, cur + k_minus1);
            // parity condition: (cur + nxt) % 2 == (k-1) % 2
            let target_parity = ((cur as i32 + (k - 1)) & 1) as usize;
            let set_ref = if target_parity == 0 { &mut even_set } else { &mut odd_set };

            // collect positions in range [left, right]
            let mut to_visit = Vec::new();
            for &pos in set_ref.range(left..=right) {
                to_visit.push(pos);
            }
            for pos in to_visit {
                ans[pos] = cur_dist + 1;
                dq.push_back(pos);
                set_ref.remove(&pos);
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (min-reverse-operations n p banned k)
  (-> exact-integer? exact-integer? (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((banned-set (let ((h (make-hash)))
                       (for ([b banned]) (hash-set! h b #t))
                       h))
         (ans (make-vector n -1))
         (visited (make-vector n #f))
         ;; parent array for DSU, size n+2 to have a sentinel at index n
         (parent (let ((v (make-vector (+ n 2) 0)))
                   (for ([i (in-range (+ n 2))])
                     (vector-set! v i i))
                   v)))

    ;; find with path compression
    (define (find x)
      (let loop ((x x))
        (if (>= x (vector-length parent))
            x
            (let ((p (vector-ref parent x)))
              (if (= p x)
                  x
                  (let ((root (loop p)))
                    (vector-set! parent x root)
                    root))))))

    ;; remove an index from the set of unvisited positions (union with next same‑parity)
    (define (remove-index idx)
      (let ((next (+ idx 2)))
        (if (>= next (vector-length parent))
            (vector-set! parent idx (vector-length parent))
            (vector-set! parent idx (find next)))))

    ;; mark banned positions as visited and remove them from DSU
    (for ([b banned])
      (when (< b n)
        (vector-set! visited b #t)
        (remove-index b)))

    ;; BFS queue implementation
    (define queue (make-vector n 0))
    (define head 0)
    (define tail 0)

    ;; initialize with start position p
    (vector-set! ans p 0)
    (vector-set! visited p #t)
    (remove-index p)
    (vector-set! queue tail p)
    (set! tail (+ tail 1))

    ;; BFS loop
    (let bfs ()
      (when (< head tail)
        (define i (vector-ref queue head))
        (set! head (+ head 1))
        (define dist (vector-ref ans i))

        (define low (max 0 (+ (- i k) 1)))          ; i - k + 1
        (define high (min i (- n k)))               ; min(i, n-k)

        (when (<= low high)
          (define L (- (+ (* 2 low) (- k 1)) i))
          (define R (- (+ (* 2 high) (- k 1)) i))
          (define L (max 0 L))
          (define R (min (- n 1) R))

          ;; required parity for reachable positions: j % 2 == (k-1 - i) % 2
          (define target-parity
            (modulo (- (modulo (- k 1) 2) (modulo i 2)) 2))

          ;; first candidate respecting parity
          (define start
            (if (= (modulo L 2) target-parity)
                L
                (+ L 1)))

          (let loop ((cur start))
            (when (and (< cur n) (<= cur R))
              (define nxt (find cur))
              (if (or (>= nxt n) (> nxt R))
                  (void)
                  (begin
                    (vector-set! ans nxt (+ dist 1))
                    (remove-index nxt)
                    (vector-set! queue tail nxt)
                    (set! tail (+ tail 1))
                    (loop (+ nxt 2))))))))

        (bfs)))

    (vector->list ans)))
```

## Erlang

```erlang
-spec min_reverse_operations(N :: integer(), P :: integer(), Banned :: [integer()], K :: integer()) -> [integer()].
min_reverse_operations(N, P, Banned, K) ->
    BannedSet = sets:from_list(Banned),
    %% Initialize parent map for DSU (skip banned positions)
    Parent0 = init_parent(0, N, BannedSet, #{}),
    %% Remove starting position from DSU (mark visited)
    Parent1 = remove(P, N, Parent0),
    DistMap0 = maps:put(P, 0, #{}),
    Q0 = queue:new(),
    Q1 = queue:in(P, Q0),
    {DistMapFinal, _ParentFinal} = bfs(N, K, BannedSet, Q1, DistMap0, Parent1),
    %% Build answer list
    lists:map(fun(I) -> maps:get(I, DistMapFinal, -1) end, lists:seq(0, N-1)).

%% Initialize parent map: each index points to itself if not banned, else to sentinel N
init_parent(I, N, _BannedSet, Parent) when I >= N ->
    Parent;
init_parent(I, N, BannedSet, Parent) ->
    NewParent = case sets:is_element(I, BannedSet) of
        true -> maps:put(I, N, Parent);
        false -> maps:put(I, I, Parent)
    end,
    init_parent(I + 1, N, BannedSet, NewParent).

%% Find with path compression; returns {Root, UpdatedMap}
find(N, Map, X) when X >= N ->
    {N, Map};
find(N, Map, X) ->
    case maps:get(X, Map) of
        X -> {X, Map};
        Y ->
            {Root, M1} = find(N, Map, Y),
            Updated = maps:put(X, Root, M1),
            {Root, Updated}
    end.

%% Remove index from DSU (mark visited)
remove(Index, N, Map) ->
    Next = Index + 2,
    if
        Next >= N ->
            maps:put(Index, N, Map);
        true ->
            {RootNext, M1} = find(N, Map, Next),
            maps:put(Index, RootNext, M1)
    end.

%% BFS main loop
bfs(N, K, BannedSet, Queue, DistMap, Parent) ->
    case queue:out(Queue) of
        {empty, _} -> {DistMap, Parent};
        {{value, Pos}, QRest} ->
            CurDist = maps:get(Pos, DistMap),
            Left0 = max(0, Pos - (K - 1)),
            Right0 = min(N - 1, Pos + (K - 1)),
            ParityNeeded = ((Pos band 1) bxor ((K - 1) band 1)),
            Start0 = if
                (Left0 band 1) =:= ParityNeeded -> Left0;
                true -> Left0 + 1
            end,
            {QNew, DMapNew, PNew} = process_range(N, K, Pos, CurDist + 1, Start0, Right0, Queue, DistMap, Parent),
            bfs(N, K, BannedSet, QNew, DMapNew, PNew)
    end.

%% Process all reachable nodes in [Start,Right] of required parity
process_range(_N, _K, _Pos, _NewDist, Start, Right, Queue, DistMap, Parent) when Start > Right ->
    {Queue, DistMap, Parent};
process_range(N, K, Pos, NewDist, Start, Right, Queue, DistMap, Parent) ->
    {Idx, P1} = find(N, Parent, Start),
    case Idx =< Right of
        false -> {Queue, DistMap, P1};
        true ->
            Q1 = queue:in(Idx, Queue),
            DMap1 = maps:put(Idx, NewDist, DistMap),
            P2 = remove(Idx, N, P1),
            NextStart = Idx + 2,
            process_range(N, K, Pos, NewDist, NextStart, Right, Q1, DMap1, P2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_reverse_operations(n :: integer, p :: integer, banned :: [integer], k :: integer) :: [integer]
  def min_reverse_operations(n, p, banned, k) do
    # Initialize parent map for DSU (each index points to itself)
    parent = Enum.reduce(0..(n - 1), %{}, fn i, acc -> Map.put(acc, i, i) end)

    # Remove banned positions and the starting position from the set of unvisited nodes
    parent =
      Enum.reduce(banned ++ [p], parent, fn idx, acc ->
        union(acc, idx, idx + 2)
      end)

    dist_map = %{p => 0}
    queue = :queue.new() |> :queue.in(p)

    {_, final_dist} = bfs(queue, parent, dist_map, n, k)

    Enum.map(0..(n - 1), fn i -> Map.get(final_dist, i, -1) end)
  end

  # Breadth‑first search
  defp bfs(queue, parent, dist_map, n, k) do
    case :queue.out(queue) do
      {:empty, _} ->
        {parent, dist_map}

      {{:value, cur}, q2} ->
        d = Map.get(dist_map, cur)
        {new_parent, new_dist_map, new_queue} = process(cur, d, parent, dist_map, q2, n, k)
        bfs(new_queue, new_parent, new_dist_map, n, k)
    end
  end

  # Process all reachable neighbours of `cur`
  defp process(cur, d, parent, dist_map, queue, n, k) do
    d_min = max(0, cur - (n - k))
    d_max = min(k - 1, cur)

    low = cur + (k - 1) - 2 * d_max
    high = cur + (k - 1) - 2 * d_min

    low = max(low, 0)
    high = min(high, n - 1)

    if low > high do
      {parent, dist_map, queue}
    else
      parity_needed = rem(cur + k - 1, 2)
      start = if rem(low, 2) != parity_needed, do: low + 1, else: low

      {root, parent} = find(parent, start)

      process_loop(root, high, cur, d, parent, dist_map, queue, n)
    end
  end

  # Iterate over all unvisited positions in the interval [root, high] with correct parity
  defp process_loop(root, high, _cur, _d, parent, dist_map, queue, n) when root > high or root >= n do
    {parent, dist_map, queue}
  end

  defp process_loop(root, high, cur, d, parent, dist_map, queue, n) do
    nd = d + 1
    dist_map = Map.put(dist_map, root, nd)
    queue = :queue.in(root, queue)

    # Mark `root` as visited by linking it to the next candidate of same parity
    parent = union(parent, root, root + 2)

    {next_root, parent} = find(parent, root)
    process_loop(next_root, high, cur, d, parent, dist_map, queue, n)
  end

  # Disjoint Set Union: find with path compression
  defp find(parent, x) do
    case Map.get(parent, x) do
      nil ->
        {x, parent}

      ^x ->
        {x, parent}

      nxt ->
        {root, parent2} = find(parent, nxt)
        {root, Map.put(parent2, x, root)}
    end
  end

  # Union: attach root of x to root of y
  defp union(parent, x, y) do
    {rx, parent1} = find(parent, x)
    {ry, parent2} = find(parent1, y)

    if rx == ry do
      parent2
    else
      Map.put(parent2, rx, ry)
    end
  end
end
```
