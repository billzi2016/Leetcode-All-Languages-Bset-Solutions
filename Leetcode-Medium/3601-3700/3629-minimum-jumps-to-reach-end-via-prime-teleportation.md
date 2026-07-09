# 3629. Minimum Jumps to Reach End via Prime Teleportation

## Cpp

```cpp
class Solution {
public:
    int minJumps(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 0;
        int maxA = 1000000;
        vector<int> spf(maxA + 1);
        for (int i = 2; i <= maxA; ++i) {
            if (!spf[i]) {
                spf[i] = i;
                if ((long long)i * i <= maxA)
                    for (int j = i * i; j <= maxA; j += i)
                        if (!spf[j]) spf[j] = i;
            }
        }

        vector<vector<int>> primeFactors(n);
        vector<vector<int>> bucket(maxA + 1);
        for (int i = 0; i < n; ++i) {
            int x = nums[i];
            while (x > 1) {
                int p = spf[x];
                primeFactors[i].push_back(p);
                while (x % p == 0) x /= p;
            }
            for (int p : primeFactors[i]) bucket[p].push_back(i);
        }

        vector<int> dist(n, -1);
        queue<int> q;
        dist[0] = 0;
        q.push(0);

        while (!q.empty()) {
            int i = q.front(); q.pop();
            int d = dist[i];
            if (i == n - 1) return d;

            // adjacent moves
            if (i - 1 >= 0 && dist[i - 1] == -1) {
                dist[i - 1] = d + 1;
                q.push(i - 1);
            }
            if (i + 1 < n && dist[i + 1] == -1) {
                dist[i + 1] = d + 1;
                q.push(i + 1);
            }

            // prime teleportation
            for (int p : primeFactors[i]) {
                for (int idx : bucket[p]) {
                    if (dist[idx] == -1) {
                        dist[idx] = d + 1;
                        q.push(idx);
                    }
                }
                bucket[p].clear(); // avoid future processing
            }
        }
        return -1; // should never reach here
    }
};
```

## Java

```java
class Solution {
    public int minJumps(int[] nums) {
        int n = nums.length;
        if (n == 1) return 0;

        int maxVal = 0;
        for (int v : nums) if (v > maxVal) maxVal = v;

        // smallest prime factor sieve
        int[] spf = new int[maxVal + 1];
        for (int i = 2; i <= maxVal; i++) {
            if (spf[i] == 0) {
                spf[i] = i;
                if ((long) i * i <= maxVal) {
                    for (int j = i * i; j <= maxVal; j += i) {
                        if (spf[j] == 0) spf[j] = i;
                    }
                }
            }
        }

        // buckets for each prime
        @SuppressWarnings("unchecked")
        ArrayList<Integer>[] bucket = new ArrayList[maxVal + 1];
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (x > 1) {
                int p = spf[x];
                if (bucket[p] == null) bucket[p] = new ArrayList<>();
                bucket[p].add(i);
                while (x % p == 0) x /= p;
            }
        }

        int[] dist = new int[n];
        java.util.Arrays.fill(dist, -1);
        java.util.ArrayDeque<Integer> q = new java.util.ArrayDeque<>();
        dist[0] = 0;
        q.add(0);

        while (!q.isEmpty()) {
            int i = q.poll();
            if (i == n - 1) return dist[i];
            int nd = dist[i] + 1;

            // adjacent moves
            if (i - 1 >= 0 && dist[i - 1] == -1) {
                dist[i - 1] = nd;
                q.add(i - 1);
            }
            if (i + 1 < n && dist[i + 1] == -1) {
                dist[i + 1] = nd;
                q.add(i + 1);
            }

            // prime teleportation
            int x = nums[i];
            while (x > 1) {
                int p = spf[x];
                ArrayList<Integer> list = bucket[p];
                if (list != null) {
                    for (int idx : list) {
                        if (dist[idx] == -1) {
                            dist[idx] = nd;
                            q.add(idx);
                        }
                    }
                    list.clear(); // ensure each prime processed once
                }
                while (x % p == 0) x /= p;
            }
        }

        return -1; // should not reach here
    }
}
```

## Python

```python
import collections

class Solution(object):
    def minJumps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0

        max_val = max(nums)
        # smallest prime factor sieve
        spf = [0] * (max_val + 1)
        primes = []
        for i in range(2, max_val + 1):
            if spf[i] == 0:
                spf[i] = i
                primes.append(i)
            for p in primes:
                if p > spf[i] or i * p > max_val:
                    break
                spf[i * p] = p

        def get_factors(x):
            facs = []
            while x > 1:
                p = spf[x]
                facs.append(p)
                while x % p == 0:
                    x //= p
            # deduplicate (they are already distinct due to loop structure)
            return list(set(facs))

        # precompute prime factors for each index and build buckets
        idx_factors = [None] * n
        bucket = collections.defaultdict(list)
        for i, val in enumerate(nums):
            facs = get_factors(val)
            idx_factors[i] = facs
            for p in facs:
                bucket[p].append(i)

        visited = [False] * n
        q = collections.deque()
        q.append(0)
        visited[0] = True
        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()
                if i == n - 1:
                    return steps
                # adjacent moves
                for nb in (i - 1, i + 1):
                    if 0 <= nb < n and not visited[nb]:
                        visited[nb] = True
                        q.append(nb)
                # prime teleportation
                for p in idx_factors[i]:
                    lst = bucket[p]
                    for j in lst:
                        if not visited[j]:
                            visited[j] = True
                            q.append(j)
                    # clear to avoid future processing
                    bucket[p] = []
            steps += 1

        return -1
```

## Python3

```python
class Solution:
    def minJumps(self, nums):
        from collections import defaultdict, deque
        n = len(nums)
        if n == 1:
            return 0

        max_val = max(nums)

        # smallest prime factor sieve
        spf = [0] * (max_val + 1)
        for i in range(2, max_val + 1):
            if spf[i] == 0:
                spf[i] = i
                if i * i <= max_val:
                    step = i
                    start = i * i
                    for j in range(start, max_val + 1, step):
                        if spf[j] == 0:
                            spf[j] = i

        # factorization and bucket building
        factors = [None] * n
        bucket = defaultdict(list)
        for idx, val in enumerate(nums):
            primes = []
            x = val
            while x > 1:
                p = spf[x]
                if p == 0:  # when val is 1
                    break
                primes.append(p)
                while x % p == 0:
                    x //= p
            factors[idx] = primes
            for p in primes:
                bucket[p].append(idx)

        visited = [False] * n
        q = deque()
        visited[0] = True
        q.append((0, 0))

        while q:
            i, d = q.popleft()
            if i == n - 1:
                return d

            # adjacent moves
            for nxt in (i - 1, i + 1):
                if 0 <= nxt < n and not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, d + 1))

            # prime teleportation
            for p in factors[i]:
                lst = bucket.get(p)
                if lst:
                    for j in lst:
                        if not visited[j]:
                            visited[j] = True
                            q.append((j, d + 1))
                    bucket[p] = []  # clear to avoid revisiting

        return -1
```

## C

```c
#include <stdlib.h>
#include <string.h>

struct Bucket {
    int *data;
    int sz;
    int cap;
};

int minJumps(int* nums, int numsSize) {
    if (numsSize <= 1) return 0;

    int maxVal = 0;
    for (int i = 0; i < numsSize; ++i)
        if (nums[i] > maxVal) maxVal = nums[i];

    /* smallest prime factor sieve */
    int *spf = (int *)malloc((maxVal + 1) * sizeof(int));
    for (int i = 0; i <= maxVal; ++i) spf[i] = i;
    for (int i = 2; i * i <= maxVal; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= maxVal; j += i)
                if (spf[j] == j) spf[j] = i;
        }
    }

    /* bucket per prime */
    struct Bucket *bucket = (struct Bucket *)calloc(maxVal + 1, sizeof(struct Bucket));
    for (int idx = 0; idx < numsSize; ++idx) {
        int x = nums[idx];
        while (x > 1) {
            int p = spf[x];
            while (x % p == 0) x /= p;
            struct Bucket *b = &bucket[p];
            if (b->sz == b->cap) {
                int newCap = b->cap ? b->cap * 2 : 4;
                b->data = (int *)realloc(b->data, newCap * sizeof(int));
                b->cap = newCap;
            }
            b->data[b->sz++] = idx;
        }
    }

    /* BFS */
    int *queue = (int *)malloc(numsSize * sizeof(int));
    char *vis = (char *)calloc(numsSize, sizeof(char));
    int *dist = (int *)malloc(numsSize * sizeof(int));

    int head = 0, tail = 0;
    queue[tail++] = 0;
    vis[0] = 1;
    dist[0] = 0;

    while (head < tail) {
        int cur = queue[head++];
        if (cur == numsSize - 1) {
            int ans = dist[cur];
            /* cleanup (optional for LeetCode) */
            free(spf);
            for (int i = 0; i <= maxVal; ++i) free(bucket[i].data);
            free(bucket);
            free(queue);
            free(vis);
            free(dist);
            return ans;
        }
        int nd = dist[cur] + 1;

        if (cur + 1 < numsSize && !vis[cur + 1]) {
            vis[cur + 1] = 1;
            dist[cur + 1] = nd;
            queue[tail++] = cur + 1;
        }
        if (cur - 1 >= 0 && !vis[cur - 1]) {
            vis[cur - 1] = 1;
            dist[cur - 1] = nd;
            queue[tail++] = cur - 1;
        }

        int x = nums[cur];
        while (x > 1) {
            int p = spf[x];
            while (x % p == 0) x /= p;
            struct Bucket *b = &bucket[p];
            for (int i = 0; i < b->sz; ++i) {
                int idx = b->data[i];
                if (!vis[idx]) {
                    vis[idx] = 1;
                    dist[idx] = nd;
                    queue[tail++] = idx;
                }
            }
            b->sz = 0;  // clear to avoid future repeats
        }
    }

    /* cleanup (optional) */
    free(spf);
    for (int i = 0; i <= maxVal; ++i) free(bucket[i].data);
    free(bucket);
    free(queue);
    free(vis);
    free(dist);
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int MinJumps(int[] nums) {
        int n = nums.Length;
        if (n == 1) return 0;

        int maxVal = 0;
        foreach (int v in nums) if (v > maxVal) maxVal = v;

        // smallest prime factor sieve
        int[] spf = new int[maxVal + 1];
        for (int i = 2; i <= maxVal; i++) {
            if (spf[i] == 0) {
                spf[i] = i;
                if ((long)i * i <= maxVal) {
                    for (int j = i * i; j <= maxVal; j += i)
                        if (spf[j] == 0) spf[j] = i;
                }
            }
        }

        // bucket per prime
        List<int>[] bucket = new List<int>[maxVal + 1];
        for (int idx = 0; idx < n; idx++) {
            int x = nums[idx];
            while (x > 1) {
                int p = spf[x];
                if (bucket[p] == null) bucket[p] = new List<int>();
                bucket[p].Add(idx);
                while (x % p == 0) x /= p;
            }
        }

        int[] dist = new int[n];
        for (int i = 0; i < n; i++) dist[i] = -1;

        var q = new System.Collections.Generic.Queue<int>();
        dist[0] = 0;
        q.Enqueue(0);

        while (q.Count > 0) {
            int i = q.Dequeue();
            if (i == n - 1) return dist[i];
            int nd = dist[i] + 1;

            // adjacent moves
            if (i - 1 >= 0 && dist[i - 1] == -1) {
                dist[i - 1] = nd;
                q.Enqueue(i - 1);
            }
            if (i + 1 < n && dist[i + 1] == -1) {
                dist[i + 1] = nd;
                q.Enqueue(i + 1);
            }

            // prime teleportation
            int val = nums[i];
            while (val > 1) {
                int p = spf[val];
                var list = bucket[p];
                if (list != null) {
                    foreach (int j in list) {
                        if (dist[j] == -1) {
                            dist[j] = nd;
                            q.Enqueue(j);
                        }
                    }
                    bucket[p] = null; // clear to avoid revisiting
                }
                while (val % p == 0) val /= p;
            }
        }

        return -1; // should not happen with given constraints
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minJumps = function(nums) {
    const n = nums.length;
    if (n === 1) return 0;

    // find maximum value to size SPF array
    let maxA = 0;
    for (let v of nums) if (v > maxA) maxA = v;

    // smallest prime factor sieve
    const spf = new Uint32Array(maxA + 1);
    for (let i = 2; i <= maxA; i++) {
        if (spf[i] === 0) {
            spf[i] = i;
            if (i * i <= maxA) {
                for (let j = i * i; j <= maxA; j += i) {
                    if (spf[j] === 0) spf[j] = i;
                }
            }
        }
    }

    // buckets for each prime and store distinct factors per index
    const buckets = new Array(maxA + 1);
    const idxFactors = new Array(n);

    for (let i = 0; i < n; i++) {
        let x = nums[i];
        const factors = [];
        while (x > 1) {
            const p = spf[x];
            factors.push(p);
            while (x % p === 0) x = Math.trunc(x / p);
        }
        idxFactors[i] = factors;
        for (const p of factors) {
            if (!buckets[p]) buckets[p] = [];
            buckets[p].push(i);
        }
    }

    // BFS
    const visited = new Uint8Array(n);
    const dist = new Int32Array(n);
    const queue = new Array(n);
    let head = 0, tail = 0;
    queue[tail++] = 0;
    visited[0] = 1;

    while (head < tail) {
        const i = queue[head++];
        const d = dist[i];
        if (i === n - 1) return d;

        // move to i-1
        if (i - 1 >= 0 && !visited[i - 1]) {
            visited[i - 1] = 1;
            dist[i - 1] = d + 1;
            queue[tail++] = i - 1;
        }
        // move to i+1
        if (i + 1 < n && !visited[i + 1]) {
            visited[i + 1] = 1;
            dist[i + 1] = d + 1;
            queue[tail++] = i + 1;
        }

        // teleport via prime factors
        for (const p of idxFactors[i]) {
            const list = buckets[p];
            if (!list) continue;
            for (let k = 0; k < list.length; k++) {
                const j = list[k];
                if (!visited[j]) {
                    visited[j] = 1;
                    dist[j] = d + 1;
                    queue[tail++] = j;
                }
            }
            buckets[p] = null; // clear to avoid reprocessing
        }
    }

    return -1; // unreachable (should not happen)
};
```

## Typescript

```typescript
function minJumps(nums: number[]): number {
    const n = nums.length;
    if (n === 1) return 0;

    // build smallest prime factor array
    let maxVal = 0;
    for (const v of nums) if (v > maxVal) maxVal = v;
    const spf = new Uint32Array(maxVal + 1);
    for (let i = 2; i * i <= maxVal; ++i) {
        if (spf[i] === 0) {
            for (let j = i * i; j <= maxVal; j += i) {
                if (spf[j] === 0) spf[j] = i;
            }
        }
    }
    for (let i = 2; i <= maxVal; ++i) {
        if (spf[i] === 0) spf[i] = i;
    }

    const getPrimeFactors = (x: number): number[] => {
        const res: number[] = [];
        while (x > 1) {
            const p = spf[x];
            res.push(p);
            while (x % p === 0) x = Math.trunc(x / p);
        }
        return res;
    };

    // factors per index and bucket per prime
    const factors: number[][] = new Array(n);
    const bucket = new Map<number, number[]>();

    for (let i = 0; i < n; ++i) {
        const pf = getPrimeFactors(nums[i]);
        factors[i] = pf;
        for (const p of pf) {
            let arr = bucket.get(p);
            if (!arr) {
                arr = [];
                bucket.set(p, arr);
            }
            arr.push(i);
        }
    }

    // BFS
    const visited = new Array<boolean>(n).fill(false);
    const dist = new Array<number>(n).fill(0);
    const queue: number[] = [];
    let head = 0;

    visited[0] = true;
    queue.push(0);

    while (head < queue.length) {
        const i = queue[head++];
        if (i === n - 1) return dist[i];
        const nd = dist[i] + 1;

        // adjacent moves
        if (i - 1 >= 0 && !visited[i - 1]) {
            visited[i - 1] = true;
            dist[i - 1] = nd;
            queue.push(i - 1);
        }
        if (i + 1 < n && !visited[i + 1]) {
            visited[i + 1] = true;
            dist[i + 1] = nd;
            queue.push(i + 1);
        }

        // prime teleportation
        for (const p of factors[i]) {
            const list = bucket.get(p);
            if (!list) continue;
            for (const j of list) {
                if (!visited[j]) {
                    visited[j] = true;
                    dist[j] = nd;
                    queue.push(j);
                }
            }
            bucket.delete(p); // clear to avoid revisiting this prime
        }
    }

    return -1; // should not happen with given constraints
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minJumps($nums) {
        $n = count($nums);
        if ($n <= 1) return 0;
        $maxVal = max($nums);

        // smallest prime factor sieve
        $spf = array_fill(0, $maxVal + 1, 0);
        for ($i = 2; $i * $i <= $maxVal; $i++) {
            if ($spf[$i] == 0) {
                for ($j = $i * $i; $j <= $maxVal; $j += $i) {
                    if ($spf[$j] == 0) $spf[$j] = $i;
                }
            }
        }
        for ($i = 2; $i <= $maxVal; $i++) {
            if ($spf[$i] == 0) $spf[$i] = $i;
        }

        // bucket per prime and factor list per index
        $bucket = [];               // prime => list of indices
        $factorsList = array_fill(0, $n, []); // per index unique primes

        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            $primes = [];
            while ($x > 1) {
                $p = $spf[$x];
                $primes[] = $p;
                while ($x % $p == 0) {
                    $x = intdiv($x, $p);
                }
            }
            $factorsList[$i] = $primes;
            foreach ($primes as $p) {
                if (!isset($bucket[$p])) $bucket[$p] = [];
                $bucket[$p][] = $i;
            }
        }

        $visited = array_fill(0, $n, false);
        $queue = new SplQueue();
        $queue->enqueue(0);
        $visited[0] = true;
        $steps = 0;

        while (!$queue->isEmpty()) {
            $size = $queue->count();
            for ($s = 0; $s < $size; $s++) {
                $i = $queue->dequeue();
                if ($i == $n - 1) return $steps;

                // move to i+1
                $next = $i + 1;
                if ($next < $n && !$visited[$next]) {
                    $visited[$next] = true;
                    $queue->enqueue($next);
                }
                // move to i-1
                $prev = $i - 1;
                if ($prev >= 0 && !$visited[$prev]) {
                    $visited[$prev] = true;
                    $queue->enqueue($prev);
                }

                // teleport via prime factors
                foreach ($factorsList[$i] as $p) {
                    if (isset($bucket[$p])) {
                        foreach ($bucket[$p] as $idx) {
                            if (!$visited[$idx]) {
                                $visited[$idx] = true;
                                $queue->enqueue($idx);
                            }
                        }
                        unset($bucket[$p]); // clear to avoid reprocessing
                    }
                }
            }
            $steps++;
        }

        return -1; // unreachable (should not happen)
    }
}
```

## Swift

```swift
class Solution {
    func minJumps(_ nums: [Int]) -> Int {
        let n = nums.count
        if n == 1 { return 0 }
        guard let maxVal = nums.max() else { return -1 }
        
        // Smallest prime factor sieve
        var spf = [Int](repeating: 0, count: maxVal + 1)
        var i = 2
        while i * i <= maxVal {
            if spf[i] == 0 {
                var j = i * i
                while j <= maxVal {
                    if spf[j] == 0 { spf[j] = i }
                    j += i
                }
            }
            i += 1
        }
        for v in 2...maxVal where spf[v] == 0 {
            spf[v] = v
        }
        
        // Function to get distinct prime factors using spf
        func factor(_ x: Int) -> [Int] {
            var num = x
            var res = [Int]()
            while num > 1 {
                let p = spf[num]
                res.append(p)
                while num % p == 0 { num /= p }
            }
            return res
        }
        
        // Precompute factors for each index and fill buckets
        var idxFactors = [[Int]](repeating: [], count: n)
        var buckets = [Int:[Int]]()
        for (idx, val) in nums.enumerated() {
            let facs = factor(val)
            idxFactors[idx] = facs
            for p in facs {
                buckets[p, default: []].append(idx)
            }
        }
        
        // BFS
        var visited = [Bool](repeating: false, count: n)
        var dist = [Int](repeating: 0, count: n)
        var queue = [Int]()
        var head = 0
        
        visited[0] = true
        dist[0] = 0
        queue.append(0)
        
        while head < queue.count {
            let cur = queue[head]
            head += 1
            if cur == n - 1 { return dist[cur] }
            let nextDist = dist[cur] + 1
            
            // adjacent moves
            if cur + 1 < n && !visited[cur + 1] {
                visited[cur + 1] = true
                dist[cur + 1] = nextDist
                queue.append(cur + 1)
            }
            if cur - 1 >= 0 && !visited[cur - 1] {
                visited[cur - 1] = true
                dist[cur - 1] = nextDist
                queue.append(cur - 1)
            }
            
            // prime teleportation
            for p in idxFactors[cur] {
                if let list = buckets[p] {
                    for nxt in list where !visited[nxt] {
                        visited[nxt] = true
                        dist[nxt] = nextDist
                        queue.append(nxt)
                    }
                    buckets[p] = [] // clear to avoid reprocessing
                }
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minJumps(nums: IntArray): Int {
        val n = nums.size
        if (n == 1) return 0

        // maximum value for sieve
        var maxVal = 0
        for (v in nums) if (v > maxVal) maxVal = v

        // smallest prime factor sieve
        val spf = IntArray(maxVal + 1) { it }
        val limit = Math.sqrt(maxVal.toDouble()).toInt()
        for (i in 2..limit) {
            if (spf[i] == i) {
                var j = i * i
                while (j <= maxVal) {
                    if (spf[j] == j) spf[j] = i
                    j += i
                }
            }
        }

        // buckets for each prime factor
        val buckets = Array(maxVal + 1) { mutableListOf<Int>() }
        for (idx in nums.indices) {
            var x = nums[idx]
            while (x > 1) {
                val p = spf[x]
                buckets[p].add(idx)
                while (x % p == 0) x /= p
            }
        }

        val visited = BooleanArray(n)
        val dist = IntArray(n) { -1 }
        val deque: ArrayDeque<Int> = ArrayDeque()
        visited[0] = true
        dist[0] = 0
        deque.add(0)

        while (deque.isNotEmpty()) {
            val i = deque.removeFirst()
            if (i == n - 1) return dist[i]

            // move to i-1
            var nb = i - 1
            if (nb >= 0 && !visited[nb]) {
                visited[nb] = true
                dist[nb] = dist[i] + 1
                deque.add(nb)
            }
            // move to i+1
            nb = i + 1
            if (nb < n && !visited[nb]) {
                visited[nb] = true
                dist[nb] = dist[i] + 1
                deque.add(nb)
            }

            // teleport via prime factors
            var x = nums[i]
            while (x > 1) {
                val p = spf[x]
                val list = buckets[p]
                if (list.isNotEmpty()) {
                    for (j in list) {
                        if (!visited[j]) {
                            visited[j] = true
                            dist[j] = dist[i] + 1
                            deque.add(j)
                        }
                    }
                    list.clear() // avoid future processing of same prime
                }
                while (x % p == 0) x /= p
            }
        }

        return -1 // should never reach here per problem constraints
    }
}
```

## Dart

```dart
class Solution {
  int minJumps(List<int> nums) {
    int n = nums.length;
    if (n == 1) return 0;

    int maxVal = 0;
    for (int v in nums) {
      if (v > maxVal) maxVal = v;
    }

    // smallest prime factor sieve
    List<int> spf = List.filled(maxVal + 1, 0);
    List<int> primes = [];
    for (int i = 2; i <= maxVal; ++i) {
      if (spf[i] == 0) {
        spf[i] = i;
        primes.add(i);
      }
      for (int p in primes) {
        int v = i * p;
        if (v > maxVal) break;
        spf[v] = p;
        if (p == spf[i]) break;
      }
    }

    // factor each number, store its distinct prime factors and fill buckets
    List<List<int>> idxPrimes = List.generate(n, (_) => []);
    List<List<int>?> bucket = List.filled(maxVal + 1, null);
    for (int i = 0; i < n; ++i) {
      int x = nums[i];
      while (x > 1) {
        int p = spf[x];
        idxPrimes[i].add(p);
        if (bucket[p] == null) bucket[p] = [];
        bucket[p]!.add(i);
        while (x % p == 0) x ~/= p;
      }
    }

    // BFS
    List<int> dist = List.filled(n, -1);
    List<int> q = List.filled(n, 0);
    int head = 0, tail = 0;
    q[tail++] = 0;
    dist[0] = 0;

    while (head < tail) {
      int i = q[head++];
      int d = dist[i];
      if (i == n - 1) break;

      // adjacent moves
      if (i - 1 >= 0 && dist[i - 1] == -1) {
        dist[i - 1] = d + 1;
        q[tail++] = i - 1;
      }
      if (i + 1 < n && dist[i + 1] == -1) {
        dist[i + 1] = d + 1;
        q[tail++] = i + 1;
      }

      // prime teleportation
      for (int p in idxPrimes[i]) {
        List<int>? list = bucket[p];
        if (list != null) {
          for (int j in list) {
            if (dist[j] == -1) {
              dist[j] = d + 1;
              q[tail++] = j;
            }
          }
          bucket[p] = null; // clear to avoid revisiting
        }
      }
    }

    return dist[n - 1];
  }
}
```

## Golang

```go
func minJumps(nums []int) int {
    n := len(nums)
    if n <= 1 {
        return 0
    }

    // find maximum value to size SPF array
    maxVal := 0
    for _, v := range nums {
        if v > maxVal {
            maxVal = v
        }
    }

    // smallest prime factor sieve
    spf := make([]int, maxVal+1)
    for i := 2; i <= maxVal; i++ {
        if spf[i] == 0 {
            spf[i] = i
            if i*i <= maxVal {
                for j := i * i; j <= maxVal; j += i {
                    if spf[j] == 0 {
                        spf[j] = i
                    }
                }
            }
        }
    }

    // buckets per prime and factor list per index
    buckets := make([][]int, maxVal+1)
    primeFactors := make([][]int, n)

    for idx, val := range nums {
        x := val
        lastP := 0
        for x > 1 {
            p := spf[x]
            if p == 0 { // when x is prime larger than sqrt(maxVal)
                p = x
            }
            if p != lastP {
                primeFactors[idx] = append(primeFactors[idx], p)
                buckets[p] = append(buckets[p], idx)
                lastP = p
            }
            for x%p == 0 {
                x /= p
            }
        }
    }

    visited := make([]bool, n)
    dist := make([]int, n)
    queue := make([]int, 0, n)

    visited[0] = true
    queue = append(queue, 0)
    head := 0

    for head < len(queue) {
        i := queue[head]
        head++
        if i == n-1 {
            return dist[i]
        }
        nd := dist[i] + 1

        // move to i-1
        if i-1 >= 0 && !visited[i-1] {
            visited[i-1] = true
            dist[i-1] = nd
            queue = append(queue, i-1)
        }
        // move to i+1
        if i+1 < n && !visited[i+1] {
            visited[i+1] = true
            dist[i+1] = nd
            queue = append(queue, i+1)
        }

        // teleport via prime factors
        for _, p := range primeFactors[i] {
            for _, j := range buckets[p] {
                if !visited[j] {
                    visited[j] = true
                    dist[j] = nd
                    queue = append(queue, j)
                }
            }
            // clear to avoid revisiting this bucket
            buckets[p] = nil
        }
    }

    return -1
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def min_jumps(nums)
  n = nums.length
  return 0 if n == 1

  max_val = nums.max
  spf = Array.new(max_val + 1, 0)

  (2..max_val).each do |i|
    next unless spf[i] == 0
    spf[i] = i
    j = i * i
    while j <= max_val
      spf[j] = i if spf[j] == 0
      j += i
    end
  end

  factors = Array.new(n) { [] }
  buckets = Hash.new { |h, k| h[k] = [] }

  nums.each_with_index do |num, idx|
    x = num
    last_p = nil
    while x > 1
      p = spf[x]
      if p != last_p
        factors[idx] << p
        buckets[p] << idx
        last_p = p
      end
      x /= p while (x % p).zero?
    end
  end

  visited = Array.new(n, false)
  dist = Array.new(n, 0)
  queue = [0]
  visited[0] = true
  head = 0

  while head < queue.length
    i = queue[head]
    head += 1
    return dist[i] if i == n - 1

    ndist = dist[i] + 1

    nxt = i + 1
    if nxt < n && !visited[nxt]
      visited[nxt] = true
      dist[nxt] = ndist
      queue << nxt
    end

    prv = i - 1
    if prv >= 0 && !visited[prv]
      visited[prv] = true
      dist[prv] = ndist
      queue << prv
    end

    factors[i].each do |p|
      bucket = buckets[p]
      bucket.each do |j|
        next if visited[j]
        visited[j] = true
        dist[j] = ndist
        queue << j
      end
      buckets[p] = [] # clear to avoid revisiting
    end
  end

  -1
end
```

## Scala

```scala
import scala.collection.mutable.{ArrayBuffer, ArrayDeque}

object Solution {
  def minJumps(nums: Array[Int]): Int = {
    val n = nums.length
    if (n == 1) return 0

    // maximum value for sieve
    var maxVal = 0
    var i = 0
    while (i < n) {
      if (nums(i) > maxVal) maxVal = nums(i)
      i += 1
    }

    // smallest prime factor sieve
    val spf = new Array[Int](maxVal + 1)
    var p = 2
    while (p <= maxVal) {
      if (spf(p) == 0) {
        spf(p) = p
        if (p.toLong * p <= maxVal) {
          var mult = p * p
          while (mult <= maxVal) {
            if (spf(mult) == 0) spf(mult) = p
            mult += p
          }
        }
      }
      p += 1
    }

    // function to get distinct prime factors using spf
    def primeFactors(x: Int): Array[Int] = {
      var v = x
      val buf = ArrayBuffer[Int]()
      while (v > 1) {
        val prime = spf(v)
        buf += prime
        while (v % prime == 0) v /= prime
      }
      buf.toArray
    }

    // precompute factors for each index
    val factors = new Array[Array[Int]](n)
    i = 0
    while (i < n) {
      factors(i) = primeFactors(nums(i))
      i += 1
    }

    // bucket per prime -> list of indices having that prime factor
    val bucket = new Array[ArrayBuffer[Int]](maxVal + 1)
    i = 0
    while (i < n) {
      for (prime <- factors(i)) {
        var buf = bucket(prime)
        if (buf == null) {
          buf = ArrayBuffer[Int]()
          bucket(prime) = buf
        }
        buf += i
      }
      i += 1
    }

    // BFS
    val visited = new Array[Boolean](n)
    val dist = new Array[Int](n)
    val queue = ArrayDeque[Int]()

    visited(0) = true
    dist(0) = 0
    queue.append(0)

    while (queue.nonEmpty) {
      val cur = queue.removeHead()
      if (cur == n - 1) return dist(cur)
      val ndist = dist(cur) + 1

      // neighbor left
      val left = cur - 1
      if (left >= 0 && !visited(left)) {
        visited(left) = true
        dist(left) = ndist
        queue.append(left)
      }
      // neighbor right
      val right = cur + 1
      if (right < n && !visited(right)) {
        visited(right) = true
        dist(right) = ndist
        queue.append(right)
      }

      // teleport via primes
      for (prime <- factors(cur)) {
        var list = bucket(prime)
        if (list != null) {
          for (idx <- list) {
            if (!visited(idx)) {
              visited(idx) = true
              dist(idx) = ndist
              queue.append(idx)
            }
          }
          // clear to avoid revisiting this prime's bucket
          bucket(prime) = null
        }
      }
    }

    -1 // should not reach here
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_jumps(nums: Vec<i32>) -> i32 {
        use std::collections::VecDeque;
        let n = nums.len();
        if n <= 1 {
            return 0;
        }
        // maximum value in nums
        let max_val = *nums.iter().max().unwrap() as usize;

        // smallest prime factor sieve
        let mut spf = vec![0usize; max_val + 1];
        for i in 2..=max_val {
            if spf[i] == 0 {
                for j in (i..=max_val).step_by(i) {
                    if spf[j] == 0 {
                        spf[j] = i;
                    }
                }
            }
        }

        // bucket[p] -> indices whose nums[idx] divisible by prime p
        let mut bucket: Vec<Vec<usize>> = vec![Vec::new(); max_val + 1];
        for (idx, &val) in nums.iter().enumerate() {
            let mut x = val as usize;
            while x > 1 {
                let p = spf[x];
                bucket[p].push(idx);
                while x % p == 0 {
                    x /= p;
                }
            }
        }

        // BFS
        let mut visited = vec![false; n];
        let mut dist = vec![-1i32; n];
        let mut q = VecDeque::new();
        visited[0] = true;
        dist[0] = 0;
        q.push_back(0usize);

        while let Some(i) = q.pop_front() {
            let d = dist[i];
            if i == n - 1 {
                return d;
            }
            // move to i+1
            if i + 1 < n && !visited[i + 1] {
                visited[i + 1] = true;
                dist[i + 1] = d + 1;
                q.push_back(i + 1);
            }
            // move to i-1
            if i >= 1 && !visited[i - 1] {
                visited[i - 1] = true;
                dist[i - 1] = d + 1;
                q.push_back(i - 1);
            }

            // prime teleportation
            let mut x = nums[i] as usize;
            while x > 1 {
                let p = spf[x];
                // take all indices for this prime and clear the bucket
                let list = std::mem::take(&mut bucket[p]);
                for nxt in list {
                    if !visited[nxt] {
                        visited[nxt] = true;
                        dist[nxt] = d + 1;
                        q.push_back(nxt);
                    }
                }
                while x % p == 0 {
                    x /= p;
                }
            }
        }

        -1 // should never reach here
    }
}
```

## Racket

```racket
(define/contract (min-jumps nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (nums-vec (list->vector nums)))
    (if (= n 1)
        0
        (let* ((max-val (apply max nums))
               (spf (make-vector (+ max-val 1) 0)))
          ;; smallest prime factor sieve
          (for ([i (in-range 2 (add1 max-val))])
            (when (= (vector-ref spf i) 0)
              (vector-set! spf i i)
              (let ((start (* i i))
                    (step i))
                (when (<= start max-val)
                  (for ([j (in-range start (+ max-val 1) step)])
                    (when (= (vector-ref spf j) 0)
                      (vector-set! spf j i))))))

          ;; distinct prime factors of x using spf
          (define (prime-factors x)
            (let loop ((v x) (primes '()))
              (if (= v 1)
                  (reverse primes)
                  (let ((p (vector-ref spf v)))
                    (let inner ((t v))
                      (if (= (remainder t p) 0)
                          (inner (/ t p))
                          (loop t (cons p primes))))))))

          ;; bucket[p] = list of indices whose value divisible by prime p
          (define buckets (make-vector (+ max-val 1) '()))
          (for ([i (in-range n)])
            (let ((v (vector-ref nums-vec i)))
              (for ([p (in-list (prime-factors v))])
                (vector-set! buckets p (cons i (vector-ref buckets p))))))

          ;; BFS
          (define dist (make-vector n -1))
          (define queue (make-vector n))
          (define head 0)
          (define tail 0)

          (vector-set! dist 0 0)
          (vector-set! queue tail 0)
          (set! tail (+ tail 1))

          (let bfs ()
            (when (< head tail)
              (define i (vector-ref queue head))
              (set! head (+ head 1))
              (define cur (vector-ref dist i))

              ;; move to i+1
              (when (< (+ i 1) n)
                (when (= (vector-ref dist (+ i 1)) -1)
                  (vector-set! dist (+ i 1) (+ cur 1))
                  (vector-set! queue tail (+ i 1))
                  (set! tail (+ tail 1))))
              ;; move to i-1
              (when (> i 0)
                (when (= (vector-ref dist (- i 1)) -1)
                  (vector-set! dist (- i 1) (+ cur 1))
                  (vector-set! queue tail (- i 1))
                  (set! tail (+ tail 1))))

              ;; teleport via prime factors
              (let ((v (vector-ref nums-vec i)))
                (for ([p (in-list (prime-factors v))])
                  (let ((lst (vector-ref buckets p)))
                    (for ([idx (in-list lst)])
                      (when (= (vector-ref dist idx) -1)
                        (vector-set! dist idx (+ cur 1))
                        (vector-set! queue tail idx)
                        (set! tail (+ tail 1))))
                    (vector-set! buckets p '()))))

              (bfs)))
          (bfs)
          (vector-ref dist (- n 1))))))
```

## Erlang

```erlang
-module(solution).
-export([min_jumps/1]).

-include_lib("kernel/include/logger.hrl").

-spec min_jumps(Nums :: [integer()]) -> integer().
min_jumps(Nums) ->
    case Nums of
        [] -> 0;
        [_] -> 0;
        _ ->
            MaxVal = lists:max(Nums),
            PrimeList = sieve_trunc(math:sqrt(MaxVal)),
            N = length(Nums),
            FactArray = array:new(N, {default, []}),
            Buckets0 = #{},
            {FactArr, Buckets} = build_factors(0, Nums, PrimeList, FactArray, Buckets0),
            bfs(queue:in({0, 0}, queue:new()), #{0 => true}, FactArr, Buckets, N)
    end.

%% Build prime list up to Limit (integer floor of sqrt max)
sieve_trunc(Limit) when is_float(Limit) ->
    sieve_trunc(trunc(Limit));
sieve_trunc(Limit) ->
    sieve(2, lists:seq(2, Limit), []).

sieve(_, [], Acc) -> lists:reverse(Acc);
sieve(P, [P|Rest], Acc) ->
    Filtered = [X || X <- Rest, X rem P =/= 0],
    sieve(P + 1, Filtered, [P | Acc]);
sieve(P, [_|Rest] = List, Acc) when P * P =< hd(List) ->
    sieve(P + 1, List, Acc);
sieve(_, List, Acc) -> lists:reverse(Acc).

%% Build factor array and prime buckets
build_factors(_Idx, [], _PrimeList, FactArr, Buckets) ->
    {FactArr, Buckets};
build_factors(Idx, [Val | Rest], PrimeList, FactArr, Buckets) ->
    PF = distinct_prime_factors(Val, PrimeList),
    NewFactArr = array:set(Idx, PF, FactArr),
    NewBuckets = add_to_buckets(PF, Idx, Buckets),
    build_factors(Idx + 1, Rest, PrimeList, NewFactArr, NewBuckets).

add_to_buckets([], _Idx, Buckets) -> Buckets;
add_to_buckets([P | Ps], Idx, Buckets) ->
    Updated = maps:update_with(P,
        fun(L) -> [Idx | L] end,
        fun() -> [Idx] end,
        Buckets),
    add_to_buckets(Ps, Idx, Updated).

%% Distinct prime factors using trial division
distinct_prime_factors(N, PrimeList) ->
    distinct_prime_factors(N, PrimeList, []).

distinct_prime_factors(1, _Plist, Acc) -> lists:reverse(Acc);
distinct_prime_factors(N, [], Acc) when N > 1 ->
    lists:reverse([N | Acc]);
distinct_prime_factors(N, [P | Rest], Acc) when P * P =< N ->
    case N rem P of
        0 ->
            NewN = remove_all_factor(N, P),
            distinct_prime_factors(NewN, Rest, [P | Acc]);
        _ ->
            distinct_prime_factors(N, Rest, Acc)
    end;
distinct_prime_factors(N, [_ | _] = Plist, Acc) when N > 1 ->
    lists:reverse([N | Acc]).

remove_all_factor(N, P) when N rem P =:= 0 ->
    remove_all_factor(N div P, P);
remove_all_factor(N, _) -> N.

%% BFS
bfs(Queue, Visited, FactArr, Buckets, TargetIdx) ->
    case queue:out(Queue) of
        {empty, _} -> -1;
        {{value, {Idx, Dist}}, QRest} ->
            if Idx =:= TargetIdx ->
                    Dist;
               true ->
                    {QNext, VisNext, BuckNext} = process_neighbors(Idx, Dist, QRest, Visited, FactArr, Buckets),
                    bfs(QNext, VisNext, FactArr, BuckNext, TargetIdx)
            end
    end.

process_neighbors(Idx, Dist, Queue, Visited, FactArr, Buckets) ->
    N = array:size(FactArr),
    {Q1, V1} = maybe_enqueue(Idx - 1, Dist + 1, Queue, Visited, N),
    {Q2, V2} = maybe_enqueue(Idx + 1, Dist + 1, Q1, V1, N),
    PF = array:get(Idx, FactArr),
    lists:foldl(
        fun(P, {QAcc, VAcc, BAcc}) ->
            case maps:find(P, BAcc) of
                error -> {QAcc, VAcc, BAcc};
                {ok, IdxList} ->
                    {QNew, VNew} = enqueue_list(IdxList, Dist + 1, QAcc, VAcc),
                    {QNew, VNew, maps:remove(P, BAcc)}
            end
        end,
        {Q2, V2, Buckets},
        PF).

maybe_enqueue(Index, NewDist, Queue, Visited, Size) ->
    if Index >= 0, Index < Size, not maps:is_key(Index, Visited) ->
            {queue:in({Index, NewDist}, Queue), Visited#{Index => true}};
       true -> {Queue, Visited}
    end.

enqueue_list([], _Dist, Q, V) -> {Q, V};
enqueue_list([J | Rest], Dist, Q, V) ->
    if maps:is_key(J, V) ->
            enqueue_list(Rest, Dist, Q, V);
       true ->
            enqueue_list(Rest, Dist, queue:in({J, Dist}, Q), V#{J => true})
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_jumps(nums :: [integer]) :: integer
  def min_jumps(nums) do
    n = length(nums)

    # trivial case
    if n == 1, do: 0, else: bfs(nums, n)
  end

  defp bfs(nums, n) do
    max_val = Enum.max(nums)
    limit = :math.sqrt(max_val) |> floor()
    primes = sieve(limit)

    # distinct prime factors for each index
    factors_list =
      Enum.map(nums, fn num ->
        prime_factors(num, primes)
      end)

    # bucket: prime => list of indices having this prime factor
    buckets =
      Enum.with_index(factors_list)
      |> Enum.reduce(%{}, fn {faclist, idx}, acc ->
        Enum.reduce(faclist, acc, fn p, a ->
          Map.update(a, p, [idx], &[idx | &1])
        end)
      end)

    # BFS
    start_queue = :queue.in({0, 0}, :queue.new())
    visited = MapSet.new([0])

    bfs_loop(start_queue, visited, nums, factors_list, n, buckets)
  end

  defp bfs_loop(queue, visited, _nums, _factors_list, n, _buckets) do
    case :queue.out(queue) do
      {:empty, _} -> -1
      {{:value, {i, dist}}, q} ->
        if i == n - 1 do
          dist
        else
          bfs_loop(q, visited, [], [], n, %{})
        end
    end
  end

  defp bfs_loop(queue, visited, nums, factors_list, n, buckets) do
    case :queue.out(queue) do
      {:empty, _} -> -1
      {{:value, {i, dist}}, q} ->
        if i == n - 1 do
          dist
        else
          {visited1, q1, buckets1} = enqueue_neighbor(i - 1, dist + 1, visited, q, n)
          {visited2, q2, buckets2} = enqueue_neighbor(i + 1, dist + 1, visited1, q1, n)

          facs = Enum.at(factors_list, i)

          {visited3, q3, buckets3} =
            Enum.reduce(facs, {visited2, q2, buckets}, fn p, {vis, qu, buck} ->
              case Map.get(buck, p) do
                nil -> {vis, qu, buck}
                idxs ->
                  {vis2, qu2} =
                    Enum.reduce(idxxs = idxs, {vis, qu}, fn j, {vacc, qacc} ->
                      if MapSet.member?(vacc, j) do
                        {vacc, qacc}
                      else
                        {MapSet.put(vacc, j), :queue.in({j, dist + 1}, qacc)}
                      end
                    end)

                  {vis2, qu2, Map.delete(buck, p)}
              end
            end)

          bfs_loop(q3, visited3, nums, factors_list, n, buckets3)
        end
    end
  end

  defp enqueue_neighbor(idx, new_dist, visited, queue, n) do
    if idx >= 0 and idx < n and not MapSet.member?(visited, idx) do
      {MapSet.put(visited, idx), :queue.in({idx, new_dist}, queue), %{}}
    else
      {visited, queue, %{}}
    end
  end

  defp sieve(limit) when limit < 2, do: []

  defp sieve(limit) do
    2..limit
    |> Enum.filter(fn x -> is_prime(x) end)
  end

  defp is_prime(k) do
    max = :math.sqrt(k) |> floor()
    2..max |> Enum.all?(fn d -> rem(k, d) != 0 end)
  end

  defp prime_factors(num, primes), do: factorize(num, primes, [])

  defp factorize(1, _primes, acc), do: Enum.reverse(acc)

  defp factorize(n, [p | rest] = primes, acc) when p * p <= n do
    if rem(n, p) == 0 do
      new_n = divide_out(n, p)
      factorize(new_n, primes, [p | acc])
    else
      factorize(n, rest, acc)
    end
  end

  defp factorize(n, _primes, acc) when n > 1 do
    Enum.reverse([n | acc])
  end

  defp divide_out(n, p) do
    if rem(n, p) == 0 do
      divide_out(div(n, p), p)
    else
      n
    end
  end
end
```
