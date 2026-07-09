# 3377. Digit Operations to Make Two Integers Equal

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minOperations(int n, int m) {
        const int MAXV = 10000;
        // sieve for primes up to 9999
        vector<bool> isPrime(MAXV, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i < MAXV; ++i) {
            if (isPrime[i]) {
                for (int j = i * i; j < MAXV; j += i)
                    isPrime[j] = false;
            }
        }
        // if start or target is prime, impossible
        if (isPrime[n] || isPrime[m]) return -1;

        string sN = to_string(n);
        int len = sN.size();

        const long long INF = 1e18;
        vector<long long> dist(MAXV, INF);
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;

        dist[n] = n; // cost includes the starting value
        pq.push({dist[n], n});

        while (!pq.empty()) {
            auto [d, cur] = pq.top(); pq.pop();
            if (d != dist[cur]) continue;
            if (cur == m) return (int)d;

            string curStr = to_string(cur);
            // ensure leading zeros are not dropped
            if ((int)curStr.size() < len) curStr = string(len - curStr.size(), '0') + curStr;

            for (int i = 0; i < len; ++i) {
                char orig = curStr[i];
                int digit = orig - '0';
                // try decrement
                if (digit > 0) {
                    int ndig = digit - 1;
                    if (!(i == 0 && ndig == 0)) { // no leading zero
                        string nxtStr = curStr;
                        nxtStr[i] = char('0' + ndig);
                        int nxt = stoi(nxtStr);
                        if (!isPrime[nxt]) {
                            long long ndist = d + nxt;
                            if (ndist < dist[nxt]) {
                                dist[nxt] = ndist;
                                pq.push({ndist, nxt});
                            }
                        }
                    }
                }
                // try increment
                if (digit < 9) {
                    int ndig = digit + 1;
                    if (!(i == 0 && ndig == 0)) { // leading zero not possible here anyway
                        string nxtStr = curStr;
                        nxtStr[i] = char('0' + ndig);
                        int nxt = stoi(nxtStr);
                        if (!isPrime[nxt]) {
                            long long ndist = d + nxt;
                            if (ndist < dist[nxt]) {
                                dist[nxt] = ndist;
                                pq.push({ndist, nxt});
                            }
                        }
                    }
                }
            }
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    private static final int MAX = 10000;
    private boolean[] isPrime = new boolean[MAX];
    
    public int minOperations(int n, int m) {
        sieve();
        if (isPrime[n] || isPrime[m]) return -1; // cannot start or end on prime
        
        int len = String.valueOf(n).length(); // same as m
        int[] dist = new int[MAX];
        java.util.Arrays.fill(dist, Integer.MAX_VALUE);
        java.util.PriorityQueue<int[]> pq = new java.util.PriorityQueue<>(
            (a, b) -> Integer.compare(a[0], b[0])
        );
        
        dist[n] = n; // cost includes starting value
        pq.offer(new int[]{dist[n], n});
        
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int d = cur[0];
            int x = cur[1];
            if (d != dist[x]) continue;
            if (x == m) return d;
            
            char[] chars = Integer.toString(x).toCharArray();
            for (int i = 0; i < len; i++) {
                char original = chars[i];
                for (char nd = '0'; nd <= '9'; nd++) {
                    if (nd == original) continue;
                    if (i == 0 && nd == '0') continue; // leading zero not allowed
                    chars[i] = nd;
                    int y = Integer.parseInt(new String(chars));
                    if (!isPrime[y]) {
                        int newDist = d + y;
                        if (newDist < dist[y]) {
                            dist[y] = newDist;
                            pq.offer(new int[]{newDist, y});
                        }
                    }
                }
                chars[i] = original; // restore
            }
        }
        return -1;
    }
    
    private void sieve() {
        java.util.Arrays.fill(isPrime, true);
        isPrime[0] = false;
        if (MAX > 1) isPrime[1] = false;
        for (int i = 2; i * i < MAX; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < MAX; j += i) {
                    isPrime[j] = false;
                }
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # Helper to check primality up to 9999
        MAXV = 10000
        is_prime = [True] * MAXV
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(MAXV ** 0.5) + 1):
            if is_prime[i]:
                step = i
                start = i * i
                for j in range(start, MAXV, step):
                    is_prime[j] = False

        # If starting or target number is prime, impossible
        if is_prime[n] or is_prime[m]:
            return -1

        L = len(str(n))
        # Precompute neighbors on the fly during Dijkstra
        import heapq
        INF = 10 ** 18
        dist = [INF] * MAXV
        dist[n] = n  # cost includes starting value
        heap = [(n, n)]

        while heap:
            cur_cost, x = heapq.heappop(heap)
            if cur_cost != dist[x]:
                continue
            if x == m:
                return cur_cost
            s = list(str(x).zfill(L))
            for i in range(L):
                d = int(s[i])
                for nd in (d - 1, d + 1):
                    if nd < 0 or nd > 9:
                        continue
                    # avoid leading zero
                    if i == 0 and nd == 0:
                        continue
                    if nd == d:
                        continue
                    s[i] = str(nd)
                    y = int(''.join(s))
                    s[i] = str(d)  # restore
                    if is_prime[y]:
                        continue
                    new_cost = cur_cost + y
                    if new_cost < dist[y]:
                        dist[y] = new_cost
                        heapq.heappush(heap, (new_cost, y))

        return -1
```

## Python3

```python
import heapq

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        # primality sieve up to 10000
        limit = 10000
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if is_prime[i]:
                step = i * i
                while step <= limit:
                    is_prime[step] = False
                    step += i

        # both numbers must have same length
        L = len(str(n))
        if len(str(m)) != L:
            return -1

        # start or target cannot be prime
        if is_prime[n] or is_prime[m]:
            return -1

        lower = 10 ** (L - 1)
        upper = 10 ** L - 1

        dist = {n: n}
        heap = [(n, n)]  # (cost so far, node)

        while heap:
            cur_cost, u = heapq.heappop(heap)
            if cur_cost != dist.get(u, None):
                continue
            if u == m:
                return cur_cost
            for i in range(L):
                power = 10 ** i
                digit = (u // power) % 10

                # decrement digit
                if digit > 0:
                    new_digit = digit - 1
                    if not (i == L - 1 and new_digit == 0):  # avoid leading zero
                        v = u - power
                        if lower <= v <= upper and not is_prime[v]:
                            nd = cur_cost + v
                            if nd < dist.get(v, float('inf')):
                                dist[v] = nd
                                heapq.heappush(heap, (nd, v))

                # increment digit
                if digit < 9:
                    new_digit = digit + 1
                    v = u + power
                    if lower <= v <= upper and not is_prime[v]:
                        nd = cur_cost + v
                        if nd < dist.get(v, float('inf')):
                            dist[v] = nd
                            heapq.heappush(heap, (nd, v))

        return -1
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static bool primeTable[10000];
static bool initialized = false;

static void initPrimes() {
    fill(begin(primeTable), end(primeTable), true);
    primeTable[0] = primeTable[1] = false;
    for (int i = 2; i * i < 10000; ++i) if (primeTable[i])
        for (int j = i * i; j < 10000; j += i) primeTable[j] = false;
    initialized = true;
}

static int digitCount(int x) {
    int cnt = 0;
    do { ++cnt; x /= 10; } while (x);
    return cnt;
}

int minOperations(int n, int m) {
    if (!initialized) initPrimes();
    if (primeTable[n] || primeTable[m]) return -1;
    if (n == m) return n;

    int L = digitCount(n);
    const long long INF = 4e18;
    vector<long long> dist(10000, INF);
    using P = pair<long long,int>;
    priority_queue<P, vector<P>, greater<P>> pq;

    dist[n] = n;
    pq.emplace(dist[n], n);

    while (!pq.empty()) {
        auto [d,u] = pq.top(); pq.pop();
        if (d != dist[u]) continue;
        if (u == m) return (int)d;

        int pow10 = 1;
        for (int pos = 0; pos < L; ++pos) {
            int digit = (u / pow10) % 10;

            // decrement
            if (digit > 0) {
                int ndigit = digit - 1;
                if (!(L > 1 && pos == L-1 && ndigit == 0)) {
                    int v = u + (ndigit - digit) * pow10;
                    if (!primeTable[v]) {
                        long long nd = d + v;
                        if (nd < dist[v]) {
                            dist[v] = nd;
                            pq.emplace(nd, v);
                        }
                    }
                }
            }
            // increment
            if (digit < 9) {
                int ndigit = digit + 1;
                if (!(L > 1 && pos == L-1 && ndigit == 0)) {
                    int v = u + (ndigit - digit) * pow10;
                    if (!primeTable[v]) {
                        long long nd = d + v;
                        if (nd < dist[v]) {
                            dist[v] = nd;
                            pq.emplace(nd, v);
                        }
                    }
                }
            }

            pow10 *= 10;
        }
    }
    return -1;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinOperations(int n, int m) {
        // Determine number of digits (both have same length)
        int len = n.ToString().Length;
        int maxVal = (int)Math.Pow(10, len) - 1;

        // Sieve for primes up to maxVal
        bool[] isPrime = new bool[maxVal + 1];
        Array.Fill(isPrime, true);
        if (maxVal >= 0) isPrime[0] = false;
        if (maxVal >= 1) isPrime[1] = false;
        for (int i = 2; i * i <= maxVal; ++i) {
            if (isPrime[i]) {
                for (int j = i * i; j <= maxVal; j += i)
                    isPrime[j] = false;
            }
        }

        // If start or target is prime, impossible
        if (isPrime[n] || isPrime[m]) return -1;

        const int INF = int.MaxValue / 2;
        int[] dist = new int[maxVal + 1];
        for (int i = 0; i <= maxVal; ++i) dist[i] = INF;
        dist[n] = n; // cost includes starting value

        var pq = new PriorityQueue<int, int>();
        pq.Enqueue(n, dist[n]);

        while (pq.Count > 0) {
            int cur = pq.Dequeue();
            int curDist = dist[cur];
            if (cur == m) return curDist;
            // generate neighbors by changing one digit
            char[] digits = cur.ToString().PadLeft(len, '0').ToCharArray();
            for (int pos = 0; pos < len; ++pos) {
                char original = digits[pos];
                for (char d = '0'; d <= '9'; ++d) {
                    if (d == original) continue;
                    if (pos == 0 && d == '0') continue; // leading zero not allowed
                    digits[pos] = d;
                    int nxt = int.Parse(new string(digits));
                    if (!isPrime[nxt]) {
                        int newDist = curDist + nxt;
                        if (newDist < dist[nxt]) {
                            dist[nxt] = newDist;
                            pq.Enqueue(nxt, newDist);
                        }
                    }
                }
                digits[pos] = original; // restore
            }
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var minOperations = function(n, m) {
    // helper: sieve for primes up to 10000
    const MAX = 10000;
    const isPrime = new Array(MAX).fill(true);
    isPrime[0] = isPrime[1] = false;
    for (let i = 2; i * i < MAX; ++i) {
        if (isPrime[i]) {
            for (let j = i * i; j < MAX; j += i) isPrime[j] = false;
        }
    }

    // same digit length check
    const d = n.toString().length;
    if (m.toString().length !== d) return -1;

    // prime restriction on start and target
    if (isPrime[n] || isPrime[m]) return -1;

    const lower = Math.pow(10, d - 1);
    const upper = Math.pow(10, d) - 1;

    // distance array, Infinity for unreachable
    const dist = new Array(upper + 1).fill(Infinity);
    dist[n] = n;

    // min-heap implementation
    class MinHeap {
        constructor() { this.heap = []; }
        push(item) {
            this.heap.push(item);
            this._siftUp(this.heap.length - 1);
        }
        _siftUp(idx) {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.heap[parent][0] <= this.heap[idx][0]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        pop() {
            if (this.heap.length === 0) return null;
            const top = this.heap[0];
            const last = this.heap.pop();
            if (this.heap.length > 0) {
                this.heap[0] = last;
                this._siftDown(0);
            }
            return top;
        }
        _siftDown(idx) {
            const n = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = left + 1;
                let smallest = idx;
                if (left < n && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
                if (right < n && this.heap[right][0] < this.heap[smallest][0]) smallest = right;
                if (smallest === idx) break;
                [this.heap[smallest], this.heap[idx]] = [this.heap[idx], this.heap[smallest]];
                idx = smallest;
            }
        }
        isEmpty() { return this.heap.length === 0; }
    }

    const heap = new MinHeap();
    heap.push([dist[n], n]);

    while (!heap.isEmpty()) {
        const [curDist, cur] = heap.pop();
        if (curDist !== dist[cur]) continue;
        if (cur === m) return curDist;

        const s = cur.toString();
        for (let i = 0; i < d; ++i) {
            const digit = s.charCodeAt(i) - 48; // faster than parseInt
            for (const delta of [-1, 1]) {
                const nd = digit + delta;
                if (nd < 0 || nd > 9) continue;
                if (i === 0 && nd === 0) continue; // avoid leading zero
                const newNum = Number(s.slice(0, i) + nd.toString() + s.slice(i + 1));
                if (newNum < lower || newNum > upper) continue;
                if (isPrime[newNum]) continue;
                const newDist = curDist + newNum;
                if (newDist < dist[newNum]) {
                    dist[newNum] = newDist;
                    heap.push([newDist, newNum]);
                }
            }
        }
    }

    return -1;
};
```

## Typescript

```typescript
function minOperations(n: number, m: number): number {
    const maxVal = 10000;
    // Sieve for primality
    const isPrime = new Array(maxVal).fill(true);
    isPrime[0] = false;
    isPrime[1] = false;
    for (let i = 2; i * i < maxVal; ++i) {
        if (isPrime[i]) {
            for (let j = i * i; j < maxVal; j += i) isPrime[j] = false;
        }
    }

    // If start or target is prime, impossible
    if (isPrime[n] || isPrime[m]) return -1;

    const digitsCount = n.toString().length;
    const limit = Math.pow(10, digitsCount);

    // Dijkstra
    const dist = new Array(limit).fill(Infinity);
    const visited = new Array(limit).fill(false);
    const pq: [number, number][] = []; // [cost, node]

    function push(cost: number, node: number) {
        let i = pq.length;
        pq.push([cost, node]);
        while (i > 0) {
            const p = ((i - 1) >> 1);
            if (pq[p][0] <= cost) break;
            pq[i] = pq[p];
            i = p;
        }
        pq[i] = [cost, node];
    }

    function pop(): [number, number] | undefined {
        if (pq.length === 0) return undefined;
        const top = pq[0];
        const last = pq.pop()!;
        if (pq.length > 0) {
            let i = 0;
            while (true) {
                let left = i * 2 + 1;
                if (left >= pq.length) break;
                let right = left + 1;
                let smallest = left;
                if (right < pq.length && pq[right][0] < pq[left][0]) smallest = right;
                if (pq[smallest][0] >= last[0]) break;
                pq[i] = pq[smallest];
                i = smallest;
            }
            pq[i] = last;
        }
        return top;
    }

    dist[n] = n; // cost includes starting value
    push(n, n);

    while (true) {
        const cur = pop();
        if (!cur) break;
        const [costSoFar, u] = cur;
        if (visited[u]) continue;
        visited[u] = true;
        if (u === m) return costSoFar;

        const s = u.toString().padStart(digitsCount, '0');
        for (let pos = 0; pos < digitsCount; ++pos) {
            for (let d = 0; d <= 9; ++d) {
                if (s[pos] === String(d)) continue;
                // avoid leading zero
                if (pos === 0 && d === 0) continue;
                const newStr = s.slice(0, pos) + d.toString() + s.slice(pos + 1);
                const v = Number(newStr);
                if (isPrime[v]) continue; // cannot step onto a prime
                const newCost = costSoFar + v;
                if (newCost < dist[v]) {
                    dist[v] = newCost;
                    push(newCost, v);
                }
            }
        }
    }

    return -1;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $m
     * @return Integer
     */
    function minOperations($n, $m) {
        // If either start or target is prime, impossible
        $maxVal = 10000; // exclusive upper bound as per constraints
        $isPrime = array_fill(0, $maxVal, true);
        $isPrime[0] = $isPrime[1] = false;
        for ($i = 2; $i * $i < $maxVal; $i++) {
            if ($isPrime[$i]) {
                for ($j = $i * $i; $j < $maxVal; $j += $i) {
                    $isPrime[$j] = false;
                }
            }
        }
        if ($isPrime[$n] || $isPrime[$m]) {
            return -1;
        }

        // Dijkstra
        $INF = PHP_INT_MAX;
        $dist = array_fill(0, $maxVal, $INF);
        $dist[$n] = $n;

        $pq = new SplPriorityQueue();
        // SplPriorityQueue extracts highest priority, so use negative distance
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
        $pq->insert($n, -$n);

        while (!$pq->isEmpty()) {
            $current = $pq->extract();
            $u = $current['data'];
            $curDist = -$current['priority']; // because we stored negative

            if ($curDist != $dist[$u]) {
                continue; // outdated entry
            }
            if ($u == $m) {
                return $dist[$u];
            }

            $s = strval($u);
            $len = strlen($s);
            for ($i = 0; $i < $len; $i++) {
                $digit = intval($s[$i]);
                foreach ([-1, 1] as $delta) {
                    $newDigit = $digit + $delta;
                    if ($newDigit < 0 || $newDigit > 9) continue;
                    // avoid leading zero
                    if ($i == 0 && $newDigit == 0) continue;

                    $newStr = $s;
                    $newStr[$i] = strval($newDigit);
                    $v = intval($newStr);

                    if ($isPrime[$v]) continue; // cannot be prime

                    $newDist = $dist[$u] + $v;
                    if ($newDist < $dist[$v]) {
                        $dist[$v] = $newDist;
                        $pq->insert($v, -$newDist);
                    }
                }
            }
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    private let INF = Int.max / 4
    func minOperations(_ n: Int, _ m: Int) -> Int {
        // digit length (both have same length)
        let len = String(n).count
        let maxVal = Int(pow(10.0, Double(len))) - 1
        
        // sieve for primes up to max possible value (9999)
        var isPrime = [Bool](repeating: true, count: maxVal + 1)
        if maxVal >= 0 {
            isPrime[0] = false
        }
        if maxVal >= 1 {
            isPrime[1] = false
        }
        let limit = Int(Double(maxVal).squareRoot())
        if maxVal >= 2 {
            for i in 2...limit where isPrime[i] {
                var j = i * i
                while j <= maxVal {
                    isPrime[j] = false
                    j += i
                }
            }
        }
        
        // start or target being prime -> impossible
        if n < isPrime.count && isPrime[n] { return -1 }
        if m < isPrime.count && isPrime[m] { return -1 }
        
        var dist = [Int](repeating: INF, count: maxVal + 1)
        var heap = MinHeap()
        dist[n] = n
        heap.push(Node(cost: n, value: n))
        
        while let node = heap.pop() {
            let curCost = node.cost
            let curVal = node.value
            if curVal == m { return curCost }
            if curCost != dist[curVal] { continue }
            
            // generate neighbors by changing one digit +/-1
            var digits = Array(String(curVal).map { Int($0.unicodeScalars.first!.value - 48) })
            // pad with leading zeros if needed (should not happen because we keep length)
            while digits.count < len {
                digits.insert(0, at: 0)
            }
            
            for i in 0..<len {
                let original = digits[i]
                for delta in [-1, 1] {
                    let nd = original + delta
                    if nd < 0 || nd > 9 { continue }
                    if i == 0 && nd == 0 { continue } // no leading zero
                    var newDigits = digits
                    newDigits[i] = nd
                    // construct number
                    var newVal = 0
                    for d in newDigits {
                        newVal = newVal * 10 + d
                    }
                    if newVal > maxVal { continue }
                    if isPrime[newVal] { continue }
                    let newCost = curCost + newVal
                    if newCost < dist[newVal] {
                        dist[newVal] = newCost
                        heap.push(Node(cost: newCost, value: newVal))
                    }
                }
            }
        }
        return -1
    }
}

// Helper structures for priority queue (min-heap)
private struct Node {
    let cost: Int
    let value: Int
}

private struct MinHeap {
    private var data: [Node] = []
    
    mutating func push(_ node: Node) {
        data.append(node)
        siftUp(data.count - 1)
    }
    
    mutating func pop() -> Node? {
        guard !data.isEmpty else { return nil }
        if data.count == 1 {
            return data.removeLast()
        }
        let top = data[0]
        data[0] = data.removeLast()
        siftDown(0)
        return top
    }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        while child > 0 {
            let parent = (child - 1) >> 1
            if data[child].cost < data[parent].cost {
                data.swapAt(child, parent)
                child = parent
            } else { break }
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var smallest = parent
            if left < data.count && data[left].cost < data[smallest].cost {
                smallest = left
            }
            if right < data.count && data[right].cost < data[smallest].cost {
                smallest = right
            }
            if smallest == parent { break }
            data.swapAt(parent, smallest)
            parent = smallest
        }
    }
}
```

## Kotlin

```kotlin
import java.util.PriorityQueue
import kotlin.math.sqrt

class Solution {
    fun minOperations(n: Int, m: Int): Int {
        if (isPrimeNumber(n) || isPrimeNumber(m)) return -1
        if (n == m) return n

        val digits = n.toString().length
        var maxVal = 1
        repeat(digits) { maxVal *= 10 }
        maxVal -= 1
        val minVal = maxVal / 10 + 1

        // sieve for primes up to maxVal
        val isPrime = BooleanArray(maxVal + 1) { true }
        if (maxVal >= 0) isPrime[0] = false
        if (maxVal >= 1) isPrime[1] = false
        val limit = sqrt(maxVal.toDouble()).toInt()
        for (i in 2..limit) {
            if (isPrime[i]) {
                var j = i * i
                while (j <= maxVal) {
                    isPrime[j] = false
                    j += i
                }
            }
        }

        // precompute powers of 10
        val pow10 = IntArray(digits)
        var p = 1
        for (i in 0 until digits) {
            pow10[i] = p
            p *= 10
        }

        val dist = IntArray(maxVal + 1) { Int.MAX_VALUE }
        val pq = PriorityQueue(compareBy<Pair<Int, Int>> { it.first })
        dist[n] = n
        pq.add(Pair(n, n))

        while (pq.isNotEmpty()) {
            val (cost, cur) = pq.poll()
            if (cost != dist[cur]) continue
            if (cur == m) return cost

            for (pos in 0 until digits) {
                val factor = pow10[pos]
                val digit = (cur / factor) % 10

                // decrement digit
                if (digit > 0) {
                    val nd = digit - 1
                    if (!(pos == digits - 1 && nd == 0)) { // avoid leading zero
                        val nxt = cur + (nd - digit) * factor
                        if (!isPrime[nxt]) {
                            val newCost = cost + nxt
                            if (newCost < dist[nxt]) {
                                dist[nxt] = newCost
                                pq.add(Pair(newCost, nxt))
                            }
                        }
                    }
                }

                // increment digit
                if (digit < 9) {
                    val nd = digit + 1
                    val nxt = cur + (nd - digit) * factor
                    if (!isPrime[nxt]) {
                        val newCost = cost + nxt
                        if (newCost < dist[nxt]) {
                            dist[nxt] = newCost
                            pq.add(Pair(newCost, nxt))
                        }
                    }
                }
            }
        }

        return -1
    }

    private fun isPrimeNumber(x: Int): Boolean {
        if (x < 2) return false
        var i = 2
        while (i * i <= x) {
            if (x % i == 0) return false
            i++
        }
        return true
    }
}
```

## Dart

```dart
import 'dart:math';

class MinHeap {
  List<_Node> heap = [];

  bool get isEmpty => heap.isEmpty;

  void push(_Node item) {
    heap.add(item);
    _siftUp(heap.length - 1);
  }

  _Node pop() {
    final top = heap.first;
    final last = heap.removeLast();
    if (heap.isNotEmpty) {
      heap[0] = last;
      _siftDown(0);
    }
    return top;
  }

  void _siftUp(int idx) {
    while (idx > 0) {
      int parent = (idx - 1) >> 1;
      if (heap[parent].dist <= heap[idx].dist) break;
      final tmp = heap[parent];
      heap[parent] = heap[idx];
      heap[idx] = tmp;
      idx = parent;
    }
  }

  void _siftDown(int idx) {
    int n = heap.length;
    while (true) {
      int left = idx * 2 + 1;
      int right = left + 1;
      int smallest = idx;
      if (left < n && heap[left].dist < heap[smallest].dist) smallest = left;
      if (right < n && heap[right].dist < heap[smallest].dist) smallest = right;
      if (smallest == idx) break;
      final tmp = heap[smallest];
      heap[smallest] = heap[idx];
      heap[idx] = tmp;
      idx = smallest;
    }
  }
}

class _Node {
  int val;
  int dist;
  _Node(this.val, this.dist);
}

class Solution {
  static const int MAXV = 10000;
  final List<bool> isPrime = List.filled(MAXV, true);

  Solution() {
    _sieve();
  }

  void _sieve() {
    if (MAXV <= 2) return;
    isPrime[0] = false;
    isPrime[1] = false;
    for (int i = 2; i * i < MAXV; ++i) {
      if (isPrime[i]) {
        for (int j = i * i; j < MAXV; j += i) {
          isPrime[j] = false;
        }
      }
    }
  }

  int minOperations(int n, int m) {
    if (isPrime[n] || isPrime[m]) return -1;
    if (n == m) return n;

    int len = n.toString().length;
    int lower = pow(10, len - 1).toInt();
    int upper = pow(10, len).toInt() - 1;

    const int INF = 1 << 60;
    List<int> dist = List.filled(MAXV, INF);
    MinHeap pq = MinHeap();

    dist[n] = n; // include starting value
    pq.push(_Node(n, n));

    while (!pq.isEmpty) {
      _Node cur = pq.pop();
      int x = cur.val;
      int d = cur.dist;
      if (d != dist[x]) continue;
      if (x == m) return d;

      List<int> digits = _toDigits(x, len);
      for (int pos = 0; pos < len; ++pos) {
        int original = digits[pos];
        for (int nd = 0; nd <= 9; ++nd) {
          if (nd == original) continue;
          if (pos == 0 && nd == 0) continue; // leading zero not allowed
          digits[pos] = nd;
          int y = _fromDigits(digits);
          if (!isPrime[y]) {
            int ndist = d + y;
            if (ndist < dist[y]) {
              dist[y] = ndist;
              pq.push(_Node(y, ndist));
            }
          }
        }
        digits[pos] = original; // restore
      }
    }

    return -1;
  }

  List<int> _toDigits(int num, int len) {
    List<int> res = List.filled(len, 0);
    for (int i = len - 1; i >= 0; --i) {
      res[i] = num % 10;
      num ~/= 10;
    }
    return res;
  }

  int _fromDigits(List<int> digits) {
    int val = 0;
    for (int d in digits) {
      val = val * 10 + d;
    }
    return val;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
	"math"
)

func minOperations(n int, m int) int {
	if isPrime(n) || isPrime(m) {
		return -1
	}
	if n == m {
		return n
	}

	lenDigits := numDigits(n)
	maxVal := 0
	for i := 0; i < lenDigits; i++ {
		maxVal = maxVal*10 + 9
	}
	const INF = int(^uint(0) >> 1)

	dist := make([]int, maxVal+1)
	for i := range dist {
		dist[i] = INF
	}
	dist[n] = n

	pq := &PriorityQueue{}
	heap.Push(pq, &Item{node: n, dist: n})

	for pq.Len() > 0 {
		it := heap.Pop(pq).(*Item)
		u := it.node
		if it.dist != dist[u] {
			continue
		}
		if u == m {
			return dist[m]
		}
		neighbors := generateNeighbors(u, lenDigits)
		for _, v := range neighbors {
			if isPrime(v) {
				continue
			}
			newDist := dist[u] + v
			if newDist < dist[v] {
				dist[v] = newDist
				heap.Push(pq, &Item{node: v, dist: newDist})
			}
		}
	}
	return -1
}

func isPrime(x int) bool {
	if x <= 1 {
		return false
	}
	if x == 2 || x == 3 {
		return true
	}
	if x%2 == 0 || x%3 == 0 {
		return false
	}
	limit := int(math.Sqrt(float64(x)))
	for i := 5; i <= limit; i += 6 {
		if x%i == 0 || x%(i+2) == 0 {
			return false
		}
	}
	return true
}

func numDigits(x int) int {
	if x == 0 {
		return 1
	}
	cnt := 0
	for x > 0 {
		cnt++
		x /= 10
	}
	return cnt
}

// generate all numbers reachable by incrementing or decrementing a single digit by 1
func generateNeighbors(x, lenDigits int) []int {
	var res []int
	power := 1
	for pos := 0; pos < lenDigits; pos++ {
		curDigit := (x / power) % 10

		if curDigit > 0 {
			newVal := x - power
			// avoid leading zero
			if !(pos == lenDigits-1 && curDigit == 1) {
				res = append(res, newVal)
			}
		}
		if curDigit < 9 {
			newVal := x + power
			// avoid leading zero (cannot happen when incrementing)
			res = append(res, newVal)
		}
		power *= 10
	}
	return res
}

// Priority queue implementation

type Item struct {
	node int
	dist int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].dist < pq[j].dist
}
func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }

func (pq *PriorityQueue) Push(x interface{}) {
	*pq = append(*pq, x.(*Item))
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	it := old[n-1]
	*pq = old[0 : n-1]
	return it
}
```

## Ruby

```ruby
def prime?(num)
  return false if num < 2
  return true if num == 2
  return false if num.even?
  i = 3
  while i * i <= num
    return true if num % i == 0
    i += 2
  end
  false
end

def min_operations(n, m)
  return -1 if prime?(n) || prime?(m)

  len = n.to_s.length
  max_val = 10**len - 1
  min_val = 10**(len - 1)

  dist = Array.new(max_val + 1, Float::INFINITY)
  dist[n] = n

  # simple binary heap implementation
  heap = []
  heap << [n, n] # [cost, node]

  while !heap.empty?
    # pop min
    heap.sort_by! { |c, _| c }
    cost, cur = heap.shift
    next if cost != dist[cur]
    return cost if cur == m

    s = cur.to_s.rjust(len, '0')
    digits = s.chars.map(&:to_i)

    len.times do |i|
      (0..9).each do |d|
        next if d == digits[i]
        next if i == 0 && d == 0 # leading zero not allowed
        new_digits = digits.dup
        new_digits[i] = d
        nxt = new_digits.join.to_i
        next if prime?(nxt)
        new_cost = cost + nxt
        if new_cost < dist[nxt]
          dist[nxt] = new_cost
          heap << [new_cost, nxt]
        end
      end
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable

    def minOperations(n: Int, m: Int): Int = {
        // Helper to check primality up to 9999
        val MAX = 10000
        val isPrime = Array.fill[Boolean](MAX)(true)
        if (MAX > 0) isPrime(0) = false
        if (MAX > 1) isPrime(1) = false
        var i = 2
        while (i * i < MAX) {
            if (isPrime(i)) {
                var j = i * i
                while (j < MAX) {
                    isPrime(j) = false
                    j += i
                }
            }
            i += 1
        }

        // If start or target is prime, impossible
        if (isPrime(n) || isPrime(m)) return -1

        val len = n.toString.length   // same as m's length per constraints
        val lower = Math.pow(10, len - 1).toInt
        val upper = Math.pow(10, len).toInt - 1

        // Precompute powers of ten for each digit position (0 = units)
        val pow10 = Array.tabulate(len)(p => Math.pow(10, p).toInt)

        val INF: Long = Long.MaxValue / 4
        val dist = Array.fill[Long](MAX)(INF)
        val pq = mutable.PriorityQueue.empty[(Long, Int)](
            Ordering.by[(Long, Int), Long](_._1).reverse
        )

        dist(n) = n.toLong
        pq.enqueue((dist(n), n))

        while (pq.nonEmpty) {
            val (curDist, cur) = pq.dequeue()
            if (curDist != dist(cur)) {
                // stale entry
                continue
            }
            if (cur == m) return curDist.toInt

            // generate neighbors by changing one digit +/- 1
            for (pos <- 0 until len) {
                val digit = (cur / pow10(pos)) % 10
                // decrement
                if (digit > 0) {
                    // avoid leading zero
                    if (!(pos == len - 1 && digit == 1)) {
                        val nxt = cur - pow10(pos)
                        if (!isPrime(nxt) && nxt >= lower && nxt <= upper) {
                            val ndist = curDist + nxt
                            if (ndist < dist(nxt)) {
                                dist(nxt) = ndist
                                pq.enqueue((ndist, nxt))
                            }
                        }
                    }
                }
                // increment
                if (digit < 9) {
                    val nxt = cur + pow10(pos)
                    // leading digit cannot become zero (increment never does)
                    if (!isPrime(nxt) && nxt >= lower && nxt <= upper) {
                        val ndist = curDist + nxt
                        if (ndist < dist(nxt)) {
                            dist(nxt) = ndist
                            pq.enqueue((ndist, nxt))
                        }
                    }
                }
            }
        }

        -1
    }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

pub struct Solution;

impl Solution {
    pub fn min_operations(n: i32, m: i32) -> i32 {
        // If n or m is prime, impossible
        if Self::is_prime(n as usize) || Self::is_prime(m as usize) {
            return -1;
        }
        // Determine number of digits
        let len = ((n as f64).log10().floor() as usize) + 1;
        let lower = 10_i32.pow((len - 1) as u32);
        let upper = 10_i32.pow(len as u32) - 1;

        // Sieve up to 10000
        const MAX: usize = 10000;
        static mut IS_PRIME: [bool; MAX] = [false; MAX];
        unsafe {
            if IS_PRIME[2] == false {
                for i in 0..MAX {
                    IS_PRIME[i] = true;
                }
                IS_PRIME[0] = false;
                IS_PRIME[1] = false;
                let mut p = 2usize;
                while p * p < MAX {
                    if IS_PRIME[p] {
                        let mut multiple = p * p;
                        while multiple < MAX {
                            IS_PRIME[multiple] = false;
                            multiple += p;
                        }
                    }
                    p += 1;
                }
            }
        }

        // Map number to index
        let mut idx_of: Vec<Option<usize>> = vec![None; (upper + 1) as usize];
        let mut numbers: Vec<i32> = Vec::new();
        let mut masks: Vec<u16> = Vec::new(); // digit mask

        for num in lower..=upper {
            unsafe {
                if IS_PRIME[num as usize] {
                    continue;
                }
            }
            let index = numbers.len();
            idx_of[num as usize] = Some(index);
            numbers.push(num);
            masks.push(Self::digit_mask(num));
        }

        // Buckets per digit
        let mut buckets: Vec<Vec<usize>> = vec![Vec::new(); 10];
        for (i, &mask) in masks.iter().enumerate() {
            for d in 0..10 {
                if (mask >> d) & 1 == 1 {
                    buckets[d].push(i);
                }
            }
        }

        let start_idx = match idx_of[n as usize] {
            Some(v) => v,
            None => return -1,
        };
        let target_idx = match idx_of[m as usize] {
            Some(v) => v,
            None => return -1,
        };

        let inf: i64 = i64::MAX / 4;
        let mut dist: Vec<i64> = vec![inf; numbers.len()];
        dist[start_idx] = n as i64;

        let mut heap: BinaryHeap<(Reverse<i64>, usize)> = BinaryHeap::new();
        heap.push((Reverse(dist[start_idx]), start_idx));

        while let Some((Reverse(cur_dist), u)) = heap.pop() {
            if cur_dist != dist[u] {
                continue;
            }
            if u == target_idx {
                break;
            }
            let mask_u = masks[u];
            // To avoid processing same neighbor multiple times via different digits,
            // we can use a temporary visited set per node.
            let mut seen: [bool; 10000] = [false; 10000]; // size enough for indices
            for d in 0..10 {
                if (mask_u >> d) & 1 == 1 {
                    for &v in &buckets[d] {
                        if v == u || seen[v] {
                            continue;
                        }
                        seen[v] = true;
                        let ndist = cur_dist + numbers[v] as i64;
                        if ndist < dist[v] {
                            dist[v] = ndist;
                            heap.push((Reverse(ndist), v));
                        }
                    }
                }
            }
        }

        if dist[target_idx] == inf {
            -1
        } else {
            dist[target_idx] as i32
        }
    }

    fn digit_mask(mut x: i32) -> u16 {
        let mut mask: u16 = 0;
        while x > 0 {
            let d = (x % 10) as usize;
            mask |= 1 << d;
            x /= 10;
        }
        mask
    }

    fn is_prime(x: usize) -> bool {
        if x < 2 {
            return false;
        }
        // simple trial division up to sqrt, sufficient for <=10000
        let mut i = 2usize;
        while i * i <= x {
            if x % i == 0 {
                return false;
            }
            i += 1;
        }
        true
    }
}
```

## Racket

```racket
(require data/heap)

(define/contract (min-operations n m)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ((max-val 9999)
         ;; sieve for primes up to max-val
         (is-prime (let ([vec (make-vector (+ max-val 1) #t)])
                     (vector-set! vec 0 #f)
                     (vector-set! vec 1 #f)
                     (for ([i (in-range 2 (add1 (exact-floor (sqrt max-val))))])
                       (when (vector-ref vec i)
                         (for ([j (in-range (* i i) (+ max-val 1) i)])
                           (vector-set! vec j #f))))
                     vec))
         ;; check prime condition
         (prime? (lambda (x) (vector-ref is-prime x)))
         (len (string-length (number->string n))))
    (cond [(or (prime? n) (prime? m)) -1]
          [(= n m) n] ; already equal, cost is the initial value
          [else
           (let* ((dist (make-vector (+ max-val 1) +inf.0))
                  (compare (lambda (a b) (< (first a) (first b))))
                  (heap (make-heap compare)))
             (vector-set! dist n n)
             (heap-add! heap (list n n)) ; (distance node)

             (let loop ()
               (if (heap-empty? heap)
                   -1
                   (let* ((item (heap-min heap))
                          (cur-dist (first item))
                          (u (second item)))
                     (heap-remove-min! heap)
                     (when (> cur-dist (vector-ref dist u))
                       (loop)) ; stale entry, skip

                     (if (= u m)
                         cur-dist
                         (begin
                           ;; generate neighbors by changing one digit
                           (let* ((pow10 (let loop-pow ([i len] [acc '()])
                                           (if (zero? i)
                                               acc
                                               (loop-pow (- i 1) (cons (expt 10 (- i 1)) acc)))))
                                  (powers pow10))
                             (for ([pos (in-range len)])
                               (let* ((power (list-ref powers pos))
                                      (orig-digit (quotient (remainder u (* power 10)) power)))
                                 (for ([d (in-range 0 10)])
                                   (when (and (not (= d orig-digit))
                                              (or (> pos 0) (not (= d 0)))) ; no leading zero
                                     (let ((v (+ u (* (- d orig-digit) power))))
                                       (when (and (<= v max-val) (not (prime? v)))
                                         (let ((new-dist (+ cur-dist v)))
                                           (when (< new-dist (vector-ref dist v))
                                             (vector-set! dist v new-dist)
                                             (heap-add! heap (list new-dist v))))))))))
                           (loop))))))))])))))
```

## Erlang

```erlang
-export([min_operations/2]).

-spec min_operations(N :: integer(), M :: integer()) -> integer().
min_operations(N, M) ->
    case N =:= M of
        true ->
            if is_prime(N) -> -1; true -> N end;
        false ->
            L = length(integer_to_list(N)),
            Lower = trunc(math:pow(10, L-1)),
            Upper = trunc(math:pow(10, L)) - 1,
            case {is_prime(N), is_prime(M)} of
                {true, _} -> -1;
                {_, true} -> -1;
                _ ->
                    Dist0 = maps:put(N, N, #{}),
                    Visited0 = #{},
                    dijkstra_loop(Dist0, Visited0, M, L, Lower, Upper)
            end
    end.

%% Dijkstra main loop (O(V^2) acceptable for ≤ 9999 nodes)
dijkstra_loop(Dist, Visited, Target, Len, Low, High) ->
    case find_min_unvisited(Dist, Visited) of
        undefined -> -1;
        {CurDist, CurNode} ->
            if CurNode =:= Target ->
                    CurDist;
               true ->
                    Visited2 = maps:put(CurNode, true, Visited),
                    Neighs = neighbors(CurNode, Len, Low, High),
                    Dist2 = update_distances(Neighs, CurDist, Dist),
                    dijkstra_loop(Dist2, Visited2, Target, Len, Low, High)
            end
    end.

find_min_unvisited(Dist, Visited) ->
    maps:fold(
      fun(Node, D, Acc) ->
          case maps:is_key(Node, Visited) of
              true -> Acc;
              false ->
                  case Acc of
                      undefined -> {D, Node};
                      {MinD, _} when D < MinD -> {D, Node};
                      _ -> Acc
                  end
          end
      end,
      undefined,
      Dist).

neighbors(N, Len, Low, High) ->
    PowList = [ trunc(math:pow(10, Len-1-I)) || I <- lists:seq(0, Len-1) ],
    lists:foldl(
      fun(Pow, Acc) ->
          Digit = (N div Pow) rem 10,
          Acc1 = case Digit > 0 of
                     true ->
                         New = N - Pow,
                         if New >= Low, New =< High -> [New|Acc]; true -> Acc end;
                     false -> Acc
                 end,
          Acc2 = case Digit < 9 of
                     true ->
                         New = N + Pow,
                         if New >= Low, New =< High -> [New|Acc1]; true -> Acc1 end;
                     false -> Acc1
                 end,
          Acc2
      end,
      [],
      PowList).

update_distances([], _CurDist, Dist) -> Dist;
update_distances([Y|Rest], CurDist, Dist) ->
    case is_prime(Y) of
        true -> update_distances(Rest, CurDist, Dist);
        false ->
            NewDist = CurDist + Y,
            case maps:get(Y, Dist, undefined) of
                undefined ->
                    Dist1 = maps:put(Y, NewDist, Dist);
                Existing when NewDist < Existing ->
                    Dist1 = maps:put(Y, NewDist, Dist);
                _Existing ->
                    Dist1 = Dist
            end,
            update_distances(Rest, CurDist, Dist1)
    end.

-spec is_prime(integer()) -> boolean().
is_prime(N) when N < 2 -> false;
is_prime(2) -> true;
is_prime(N) when N rem 2 =:= 0 -> false;
is_prime(N) ->
    Limit = trunc(math:sqrt(N)),
    is_prime_check(N, 3, Limit).

is_prime_check(_N, I, Limit) when I > Limit -> true;
is_prime_check(N, I, Limit) ->
    case N rem I of
        0 -> false;
        _ -> is_prime_check(N, I + 2, Limit)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(n :: integer, m :: integer) :: integer
  def min_operations(n, m) do
    cond do
      prime?(n) or prime?(m) ->
        -1

      true ->
        d = Integer.digits(n) |> length()
        max = :math.pow(10, d) |> trunc() - 1

        prime_map =
          Enum.reduce(0..max, %{}, fn i, acc ->
            Map.put(acc, i, prime?(i))
          end)

        if Map.get(prime_map, m) do
          -1
        else
          dijkstra(n, m, d, prime_map)
        end
    end
  end

  # Dijkstra implementation where distance includes node values (cost = sum of visited numbers)
  defp dijkstra(start, target, digit_len, prime_map) do
    dist = %{start => start}
    visited = MapSet.new()
    do_dijkstra(dist, visited, target, digit_len, prime_map)
  end

  defp do_dijkstra(dist, visited, target, digit_len, prime_map) do
    candidates =
      Map.keys(dist)
      |> Enum.filter(fn k -> not MapSet.member?(visited, k) end)

    if candidates == [] do
      -1
    else
      u = Enum.min_by(candidates, fn k -> dist[k] end)

      if u == target do
        dist[u]
      else
        visited = MapSet.put(visited, u)
        neighbors = generate_neighbors(u, digit_len, prime_map)

        new_dist =
          Enum.reduce(neighbors, dist, fn v, dmap ->
            if MapSet.member?(visited, v) do
              dmap
            else
              nd = dist[u] + v
              old = Map.get(dmap, v, :infinity)

              cond do
                old == :infinity or nd < old -> Map.put(dmap, v, nd)
                true -> dmap
              end
            end
          end)

        do_dijkstra(new_dist, visited, target, digit_len, prime_map)
      end
    end
  end

  # Generate all valid neighbors differing by exactly one digit and non‑prime
  defp generate_neighbors(num, digit_len, prime_map) do
    digits = Integer.digits(num)

    for idx <- 0..(digit_len - 1),
        new_digit <- 0..9,
        new_digit != Enum.at(digits, idx),
        not (idx == 0 and new_digit == 0) do
      new_digits = List.replace_at(digits, idx, new_digit)
      v = Enum.reduce(new_digits, 0, fn d, acc -> acc * 10 + d end)

      if not Map.get(prime_map, v) do
        v
      else
        nil
      end
    end
    |> Enum.filter(& &1)
  end

  # Simple primality test (sufficient for numbers < 10000)
  defp prime?(x) when x < 2, do: false

  defp prime?(x) do
    limit = :math.sqrt(x) |> trunc()
    2..limit |> Enum.all?(fn i -> rem(x, i) != 0 end)
  end
end
```
