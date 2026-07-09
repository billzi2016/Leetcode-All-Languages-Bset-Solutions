# 1916. Count Ways to Build Rooms in an Ant Colony

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1000000007;
    
    long long modPow(long long a, long long e) {
        long long r = 1;
        while (e) {
            if (e & 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
    
    int waysToBuildRooms(vector<int>& prevRoom) {
        int n = prevRoom.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; ++i) {
            children[prevRoom[i]].push_back(i);
        }
        
        // factorials
        vector<long long> fact(n + 1), invFact(n + 1);
        fact[0] = 1;
        for (int i = 1; i <= n; ++i) fact[i] = fact[i - 1] * i % MOD;
        invFact[n] = modPow(fact[n], MOD - 2);
        for (int i = n; i > 0; --i) invFact[i - 1] = invFact[i] * i % MOD;
        
        vector<int> sz(n, 0);
        vector<long long> dp(n, 0);
        
        // iterative post-order DFS
        vector<pair<int,int>> st;
        st.reserve(2*n);
        st.emplace_back(0, 0); // (node, state) 0=enter,1=exit
        while (!st.empty()) {
            auto [u, state] = st.back();
            st.pop_back();
            if (state == 0) {
                st.emplace_back(u, 1);
                for (int v : children[u]) st.emplace_back(v, 0);
            } else {
                long long ways = 1;
                int total = 0;
                for (int v : children[u]) {
                    ways = ways * dp[v] % MOD;
                    total += sz[v];
                }
                // multinomial coefficient
                long long comb = fact[total];
                for (int v : children[u]) {
                    comb = comb * invFact[sz[v]] % MOD;
                }
                ways = ways * comb % MOD;
                dp[u] = ways;
                sz[u] = total + 1; // include self
            }
        }
        return (int)dp[0];
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    
    public int waysToBuildRooms(int[] prevRoom) {
        int n = prevRoom.length;
        @SuppressWarnings("unchecked")
        List<Integer>[] children = new ArrayList[n];
        for (int i = 0; i < n; i++) children[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            int p = prevRoom[i];
            children[p].add(i);
        }
        
        long[] fact = new long[n + 1];
        long[] invFact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[n] = modPow(fact[n], MOD - 2);
        for (int i = n; i > 0; i--) {
            invFact[i - 1] = invFact[i] * i % MOD;
        }
        
        int[] order = new int[n];
        int idx = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        while (!stack.isEmpty()) {
            int u = stack.pop();
            order[idx++] = u;
            for (int v : children[u]) {
                stack.push(v);
            }
        }
        
        int[] size = new int[n];
        long[] ways = new long[n];
        for (int i = n - 1; i >= 0; --i) {
            int u = order[i];
            long curWays = 1;
            int total = 0;
            for (int v : children[u]) {
                curWays = curWays * ways[v] % MOD;
                total += size[v];
            }
            // multinomial coefficient: total! / (size[child1]! * ... )
            long comb = fact[total];
            for (int v : children[u]) {
                comb = comb * invFact[size[v]] % MOD;
            }
            curWays = curWays * comb % MOD;
            ways[u] = curWays;
            size[u] = total + 1; // include the node itself
        }
        return (int) ways[0];
    }
    
    private long modPow(long base, long exp) {
        long res = 1;
        long b = base % MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = res * b % MOD;
            }
            b = b * b % MOD;
            exp >>= 1;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def waysToBuildRooms(self, prevRoom):
        """
        :type prevRoom: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(prevRoom)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = prevRoom[i]
            children[p].append(i)

        # factorials and inverse factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        size = [0] * n
        dp = [0] * n

        # iterative post-order traversal
        stack = [(0, 0)]  # (node, visited_flag)
        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, 1))
                for child in children[node]:
                    stack.append((child, 0))
            else:
                total_sub = 0
                ways = 1
                for child in children[node]:
                    sz = size[child]
                    total_sub += sz
                    ways = ways * dp[child] % MOD
                # multinomial coefficient to interleave children's subtrees
                mult = fact[total_sub]
                for child in children[node]:
                    mult = mult * inv_fact[size[child]] % MOD
                ways = ways * mult % MOD
                size[node] = total_sub + 1  # include the node itself
                dp[node] = ways

        return dp[0]
```

## Python3

```python
import sys
from typing import List

class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(prevRoom)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = prevRoom[i]
            children[p].append(i)

        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(a: int, b: int) -> int:
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        sys.setrecursionlimit(200000)
        sz = [0] * n
        dp = [0] * n

        def dfs(u: int) -> None:
            total_sz = 1  # includes u itself
            ways = 1
            for v in children[u]:
                dfs(v)
                ways = ways * dp[v] % MOD
                ways = ways * comb(total_sz - 1 + sz[v], sz[v]) % MOD
                total_sz += sz[v]
            sz[u] = total_sz
            dp[u] = ways

        dfs(0)
        return dp[0]
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define MOD 1000000007LL

static long long mod_pow(long long a, long long e) {
    long long res = 1;
    while (e) {
        if (e & 1) res = res * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return res;
}

int waysToBuildRooms(int* prevRoom, int prevRoomSize){
    int n = prevRoomSize;
    // count children
    int *cnt = (int*)calloc(n, sizeof(int));
    for (int i = 1; i < n; ++i) {
        cnt[prevRoom[i]]++;
    }
    // prefix sums to get offsets
    int *offset = (int*)malloc(n * sizeof(int));
    offset[0] = 0;
    for (int i = 1; i < n; ++i) {
        offset[i] = offset[i-1] + cnt[i-1];
    }
    // allocate children array
    int totalEdges = n - 1;
    int *children = (int*)malloc(totalEdges * sizeof(int));
    // current fill positions
    int *cur = (int*)malloc(n * sizeof(int));
    memcpy(cur, offset, n * sizeof(int));
    for (int i = 1; i < n; ++i) {
        int p = prevRoom[i];
        children[cur[p]++] = i;
    }
    free(cur);
    // factorials
    long long *fact = (long long*)malloc((n+1) * sizeof(long long));
    long long *invFact = (long long*)malloc((n+1) * sizeof(long long));
    fact[0] = 1;
    for (int i = 1; i <= n; ++i) fact[i] = fact[i-1] * i % MOD;
    invFact[n] = mod_pow(fact[n], MOD-2);
    for (int i = n; i > 0; --i) invFact[i-1] = invFact[i] * i % MOD;

    // arrays for size and ways
    int *sz = (int*)malloc(n * sizeof(int));
    long long *ways = (long long*)malloc(n * sizeof(long long));

    // iterative post-order DFS
    int *stack = (int*)malloc(n * sizeof(int));
    char *state = (char*)malloc(n * sizeof(char));
    int top = 0;
    stack[0] = 0;
    state[0] = 0; // 0 = first visit, 1 = after children
    while (top >= 0) {
        int u = stack[top];
        char st = state[top];
        if (st == 0) {
            state[top] = 1;
            // push children
            int start = offset[u];
            int end = start + cnt[u];
            for (int i = start; i < end; ++i) {
                int v = children[i];
                ++top;
                stack[top] = v;
                state[top] = 0;
            }
        } else {
            // compute
            long long w = 1;
            int totalChildSize = 0;
            int start = offset[u];
            int end = start + cnt[u];
            for (int i = start; i < end; ++i) {
                int v = children[i];
                totalChildSize += sz[v];
                w = w * ways[v] % MOD;
            }
            long long mult = fact[totalChildSize];
            for (int i = start; i < end; ++i) {
                int v = children[i];
                mult = mult * invFact[sz[v]] % MOD;
            }
            w = w * mult % MOD;
            sz[u] = totalChildSize + 1;
            ways[u] = w;
            --top;
        }
    }

    int result = (int)(ways[0] % MOD);
    // free memory
    free(cnt);
    free(offset);
    free(children);
    free(fact);
    free(invFact);
    free(sz);
    free(ways);
    free(stack);
    free(state);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private const int MOD = 1000000007;
    
    public int WaysToBuildRooms(int[] prevRoom) {
        int n = prevRoom.Length;
        var children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        for (int i = 1; i < n; i++) {
            int p = prevRoom[i];
            children[p].Add(i);
        }
        
        long[] fact = new long[n + 1];
        long[] invFact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[n] = ModPow(fact[n], MOD - 2);
        for (int i = n; i >= 1; i--) invFact[i - 1] = invFact[i] * i % MOD;
        
        long[] size = new long[n];
        long[] dp = new long[n];
        
        var stack = new Stack<(int node, bool visited)>();
        stack.Push((0, false));
        while (stack.Count > 0) {
            var (u, visited) = stack.Pop();
            if (!visited) {
                stack.Push((u, true));
                foreach (var v in children[u]) {
                    stack.Push((v, false));
                }
            } else {
                long totalSize = 0;
                long waysProduct = 1;
                foreach (var v in children[u]) {
                    totalSize += size[v];
                    waysProduct = waysProduct * dp[v] % MOD;
                }
                
                long multinomial = fact[totalSize];
                foreach (var v in children[u]) {
                    multinomial = multinomial * invFact[size[v]] % MOD;
                }
                
                dp[u] = waysProduct * multinomial % MOD;
                size[u] = totalSize + 1; // include the node itself
            }
        }
        
        return (int)dp[0];
    }
    
    private long ModPow(long a, long e) {
        long res = 1;
        a %= MOD;
        while (e > 0) {
            if ((e & 1) == 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} prevRoom
 * @return {number}
 */
var waysToBuildRooms = function(prevRoom) {
    const MOD = 1000000007n;
    const n = prevRoom.length;
    const children = Array.from({length: n}, () => []);
    for (let i = 1; i < n; ++i) {
        const p = prevRoom[i];
        children[p].push(i);
    }

    // factorials and inverse factorials
    const fact = new Array(n + 1);
    const invFact = new Array(n + 1);
    fact[0] = 1n;
    for (let i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    function modPow(base, exp) {
        let result = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0n) {
            if (e & 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    }
    invFact[n] = modPow(fact[n], MOD - 2n);
    for (let i = n; i >= 1; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }

    // iterative post-order traversal
    const stack = [0];
    const order = [];
    while (stack.length) {
        const node = stack.pop();
        order.push(node);
        for (const child of children[node]) {
            stack.push(child);
        }
    }

    const sz = new Array(n).fill(0);
    const dp = new Array(n).fill(0n);

    for (let idx = order.length - 1; idx >= 0; --idx) {
        const node = order[idx];
        let totalSize = 0;
        for (const child of children[node]) {
            totalSize += sz[child];
        }

        // multinomial coefficient for interleaving children's subtrees
        let ways = fact[totalSize];
        for (const child of children[node]) {
            ways = (ways * invFact[sz[child]]) % MOD;
        }

        // multiply by each child's internal arrangements
        let prod = 1n;
        for (const child of children[node]) {
            prod = (prod * dp[child]) % MOD;
        }

        dp[node] = (ways * prod) % MOD;
        sz[node] = totalSize + 1; // include the node itself
    }

    return Number(dp[0]);
};
```

## Typescript

```typescript
function waysToBuildRooms(prevRoom: number[]): number {
    const MOD = 1000000007n;
    const n = prevRoom.length;

    // Build children adjacency list
    const children: number[][] = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; i++) {
        const p = prevRoom[i];
        children[p].push(i);
    }

    // Precompute factorials and inverse factorials
    const fact: bigint[] = new Array(n + 1);
    fact[0] = 1n;
    for (let i = 1; i <= n; i++) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }

    function modPow(base: bigint, exp: bigint): bigint {
        let result = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0) {
            if (e & 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    }

    function modInv(x: bigint): bigint {
        return modPow(x, MOD - 2n);
    }

    const size = new Array<bigint>(n);
    const ways = new Array<bigint>(n);

    // Iterative post-order DFS
    const stack: [number, boolean][] = [[0, false]];
    while (stack.length) {
        const [node, visited] = stack.pop()!;
        if (!visited) {
            stack.push([node, true]);
            for (const child of children[node]) {
                stack.push([child, false]);
            }
        } else {
            let totalSize = 1n; // include the node itself
            let prodWays = 1n;
            for (const child of children[node]) {
                totalSize += size[child];
                prodWays = (prodWays * ways[child]) % MOD;
            }

            const numerator = fact[Number(totalSize - 1n)];
            let denominator = 1n;
            for (const child of children[node]) {
                denominator = (denominator * fact[Number(size[child])]) % MOD;
            }
            const comb = (numerator * modInv(denominator)) % MOD;

            ways[node] = (comb * prodWays) % MOD;
            size[node] = totalSize;
        }
    }

    return Number(ways[0]);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $prevRoom
     * @return Integer
     */
    function waysToBuildRooms($prevRoom) {
        $MOD = 1000000007;
        $n = count($prevRoom);
        // build children list
        $children = array_fill(0, $n, []);
        for ($i = 1; $i < $n; ++$i) {
            $p = $prevRoom[$i];
            $children[$p][] = $i;
        }
        // factorials and inverse factorials
        $fact = array_fill(0, $n + 1, 1);
        for ($i = 1; $i <= $n; ++$i) {
            $fact[$i] = ($fact[$i - 1] * $i) % $MOD;
        }
        $invFact = array_fill(0, $n + 1, 1);
        $invFact[$n] = $this->modPow($fact[$n], $MOD - 2, $MOD);
        for ($i = $n; $i > 0; --$i) {
            $invFact[$i - 1] = ($invFact[$i] * $i) % $MOD;
        }
        // iterative post-order DFS
        $size = array_fill(0, $n, 0);
        $ways = array_fill(0, $n, 1);
        $stack = [[0, false]]; // [node, visitedFlag]
        while ($stack) {
            [$node, $visited] = array_pop($stack);
            if (!$visited) {
                $stack[] = [$node, true];
                foreach ($children[$node] as $ch) {
                    $stack[] = [$ch, false];
                }
            } else {
                $totalChildSize = 0;
                $res = 1;
                foreach ($children[$node] as $ch) {
                    $totalChildSize += $size[$ch];
                    // multiply ways of child
                    $res = ($res * $ways[$ch]) % $MOD;
                }
                // multinomial coefficient for interleaving children subtrees
                $res = ($res * $fact[$totalChildSize]) % $MOD;
                foreach ($children[$node] as $ch) {
                    $res = ($res * $invFact[$size[$ch]]) % $MOD;
                }
                $ways[$node] = $res;
                $size[$node] = $totalChildSize + 1; // include itself
            }
        }
        return $ways[0];
    }

    private function modPow($base, $exp, $mod) {
        $result = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $result;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    private let MOD = 1_000_000_007
    
    func waysToBuildRooms(_ prevRoom: [Int]) -> Int {
        let n = prevRoom.count
        var children = [[Int]](repeating: [], count: n)
        if n > 1 {
            for i in 1..<n {
                let p = prevRoom[i]
                children[p].append(i)
            }
        }
        
        // factorials and inverse factorials
        var fact = [Int](repeating: 1, count: n + 1)
        for i in 1...n {
            fact[i] = Int(Int64(fact[i - 1]) * Int64(i) % Int64(MOD))
        }
        var invFact = [Int](repeating: 1, count: n + 1)
        invFact[n] = modPow(fact[n], MOD - 2)
        if n > 0 {
            for i in stride(from: n, to: 0, by: -1) {
                invFact[i - 1] = Int(Int64(invFact[i]) * Int64(i) % Int64(MOD))
            }
        }
        
        var size = [Int](repeating: 0, count: n)
        var dp = [Int](repeating: 0, count: n)
        
        // iterative post-order DFS
        var stack: [(Int, Bool)] = [(0, false)]
        while let (node, visited) = stack.popLast() {
            if !visited {
                stack.append((node, true))
                for child in children[node] {
                    stack.append((child, false))
                }
            } else {
                var totalSize = 0
                var ways: Int64 = 1
                for child in children[node] {
                    totalSize += size[child]
                    ways = ways * Int64(dp[child]) % Int64(MOD)
                }
                
                // multinomial coefficient
                var comb = fact[totalSize]
                for child in children[node] {
                    comb = Int(Int64(comb) * Int64(invFact[size[child]]) % Int64(MOD))
                }
                
                ways = ways * Int64(comb) % Int64(MOD)
                dp[node] = Int(ways)
                size[node] = totalSize + 1
            }
        }
        
        return dp[0]
    }
    
    private func modPow(_ base: Int, _ exp: Int) -> Int {
        var result: Int64 = 1
        var b: Int64 = Int64(base % MOD)
        var e = exp
        let m = Int64(MOD)
        while e > 0 {
            if e & 1 == 1 {
                result = (result * b) % m
            }
            b = (b * b) % m
            e >>= 1
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    private val MOD = 1_000_000_007L

    fun waysToBuildRooms(prevRoom: IntArray): Int {
        val n = prevRoom.size
        val children = Array(n) { mutableListOf<Int>() }
        for (i in 1 until n) {
            val p = prevRoom[i]
            children[p].add(i)
        }

        // factorials and inverse factorials
        val fact = LongArray(n + 1)
        val invFact = LongArray(n + 1)
        fact[0] = 1L
        for (i in 1..n) {
            fact[i] = fact[i - 1] * i % MOD
        }
        invFact[n] = modPow(fact[n], MOD - 2)
        for (i in n - 1 downTo 0) {
            invFact[i] = invFact[i + 1] * (i + 1) % MOD
        }

        val size = IntArray(n)
        val dp = LongArray(n)

        // iterative post-order DFS
        val stack: ArrayDeque<Pair<Int, Boolean>> = ArrayDeque()
        stack.push(Pair(0, false))
        while (!stack.isEmpty()) {
            val (node, visited) = stack.pop()
            if (!visited) {
                stack.push(Pair(node, true))
                for (child in children[node]) {
                    stack.push(Pair(child, false))
                }
            } else {
                var totalChildrenSize = 0
                var ways = 1L
                for (child in children[node]) {
                    ways = ways * dp[child] % MOD
                    totalChildrenSize += size[child]
                }
                // multinomial coefficient
                ways = ways * fact[totalChildrenSize] % MOD
                for (child in children[node]) {
                    ways = ways * invFact[size[child]] % MOD
                }
                dp[node] = ways
                size[node] = totalChildrenSize + 1
            }
        }

        return dp[0].toInt()
    }

    private fun modPow(base: Long, exp: Long): Long {
        var b = base % MOD
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e and 1L) == 1L) {
                res = res * b % MOD
            }
            b = b * b % MOD
            e = e shr 1
        }
        return res
    }
}
```

## Golang

```go
package main

const MOD int64 = 1000000007

func waysToBuildRooms(prevRoom []int) int {
	n := len(prevRoom)
	children := make([][]int, n)
	for i := 1; i < n; i++ {
		p := prevRoom[i]
		children[p] = append(children[p], i)
	}

	fact := make([]int64, n+1)
	invFact := make([]int64, n+1)
	fact[0] = 1
	for i := 1; i <= n; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD
	}
	invFact[n] = modPow(fact[n], MOD-2)
	for i := n - 1; i >= 0; i-- {
		invFact[i] = invFact[i+1] * int64(i+1) % MOD
	}

	size := make([]int, n)
	dp := make([]int64, n)

	var dfs func(int)
	dfs = func(u int) {
		total := 0
		ways := int64(1)
		for _, v := range children[u] {
			dfs(v)
			total += size[v]
			ways = ways * dp[v] % MOD
		}
		ways = ways * fact[total] % MOD
		for _, v := range children[u] {
			ways = ways * invFact[size[v]] % MOD
		}
		size[u] = total + 1
		dp[u] = ways
	}

	dfs(0)
	return int(dp[0])
}

func modPow(a, e int64) int64 {
	res := int64(1)
	a %= MOD
	for e > 0 {
		if e&1 == 1 {
			res = res * a % MOD
		}
		a = a * a % MOD
		e >>= 1
	}
	return res
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(a, e)
  res = 1
  base = a % MOD
  while e > 0
    res = (res * base) % MOD if (e & 1) == 1
    base = (base * base) % MOD
    e >>= 1
  end
  res
end

def ways_to_build_rooms(prev_room)
  n = prev_room.length
  children = Array.new(n) { [] }
  (1...n).each do |i|
    p = prev_room[i]
    children[p] << i
  end

  fact = Array.new(n + 1, 0)
  inv_fact = Array.new(n + 1, 0)
  fact[0] = 1
  (1..n).each { |i| fact[i] = (fact[i - 1] * i) % MOD }
  inv_fact[n] = mod_pow(fact[n], MOD - 2)
  (n - 1).downto(0) { |i| inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD }

  size = Array.new(n, 1)
  dp = Array.new(n, 1)

  stack = [[0, false]]
  until stack.empty?
    node, visited = stack.pop
    if visited
      total = 0
      ways = 1
      children[node].each do |ch|
        total += size[ch]
        ways = (ways * dp[ch]) % MOD
      end
      multinomial = fact[total]
      children[node].each do |ch|
        multinomial = (multinomial * inv_fact[size[ch]]) % MOD
      end
      dp[node] = (ways * multinomial) % MOD
      size[node] = total + 1
    else
      stack << [node, true]
      children[node].reverse_each { |ch| stack << [ch, false] }
    end
  end

  dp[0] % MOD
end
```

## Scala

```scala
object Solution {
  def waysToBuildRooms(prevRoom: Array[Int]): Int = {
    val MOD = 1000000007L
    val n = prevRoom.length
    val children = Array.fill(n)(new scala.collection.mutable.ArrayBuffer[Int]())
    var i = 1
    while (i < n) {
      val p = prevRoom(i)
      children(p).append(i)
      i += 1
    }

    // factorials and inverse factorials
    val fact = new Array[Long](n + 1)
    val invFact = new Array[Long](n + 1)
    fact(0) = 1L
    var j = 1
    while (j <= n) {
      fact(j) = fact(j - 1) * j % MOD
      j += 1
    }
    def modPow(a: Long, e: Long): Long = {
      var base = a % MOD
      var exp = e
      var res = 1L
      while (exp > 0) {
        if ((exp & 1L) == 1L) res = res * base % MOD
        base = base * base % MOD
        exp >>= 1
      }
      res
    }
    invFact(n) = modPow(fact(n), MOD - 2)
    var k = n - 1
    while (k >= 0) {
      invFact(k) = invFact(k + 1) * (k + 1) % MOD
      k -= 1
    }

    val size = new Array[Int](n)
    val dp = new Array[Long](n)

    import java.util.ArrayDeque
    val stack = new ArrayDeque[(Int, Boolean)]()
    stack.push((0, false))
    while (!stack.isEmpty) {
      val (u, visited) = stack.pop()
      if (!visited) {
        stack.push((u, true))
        val ch = children(u)
        var idx = 0
        while (idx < ch.length) {
          stack.push((ch(idx), false))
          idx += 1
        }
      } else {
        var total = 0
        var ways = 1L
        val ch = children(u)
        var idx = 0
        while (idx < ch.length) {
          val v = ch(idx)
          total += size(v)
          ways = ways * dp(v) % MOD
          idx += 1
        }
        // multinomial coefficient for interleaving child subtrees
        var comb = fact(total)
        idx = 0
        while (idx < ch.length) {
          val v = ch(idx)
          comb = comb * invFact(size(v)) % MOD
          idx += 1
        }
        ways = ways * comb % MOD
        dp(u) = ways
        size(u) = total + 1
      }
    }

    dp(0).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn ways_to_build_rooms(prev_room: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = prev_room.len();
        // build children adjacency list
        let mut children: Vec<Vec<usize>> = vec![Vec::new(); n];
        for i in 1..n {
            let p = prev_room[i] as usize;
            children[p].push(i);
        }

        // precompute factorials and inverse factorials
        let mut fact: Vec<i64> = vec![1; n + 1];
        for i in 1..=n {
            fact[i] = fact[i - 1] * (i as i64) % MOD;
        }
        fn mod_pow(mut a: i64, mut e: i64, m: i64) -> i64 {
            let mut res = 1i64;
            while e > 0 {
                if e & 1 == 1 {
                    res = res * a % m;
                }
                a = a * a % m;
                e >>= 1;
            }
            res
        }
        let mut inv_fact: Vec<i64> = vec![1; n + 1];
        inv_fact[n] = mod_pow(fact[n], MOD - 2, MOD);
        for i in (0..n).rev() {
            inv_fact[i] = inv_fact[i + 1] * ((i + 1) as i64) % MOD;
        }
        let comb = |nn: usize, kk: usize, fact: &Vec<i64>, inv_fact: &Vec<i64>| -> i64 {
            if kk > nn {
                return 0;
            }
            fact[nn] * inv_fact[kk] % MOD * inv_fact[nn - kk] % MOD
        };

        // iterative post-order traversal
        let mut order: Vec<usize> = Vec::with_capacity(n);
        let mut stack: Vec<usize> = vec![0];
        while let Some(u) = stack.pop() {
            order.push(u);
            for &v in &children[u] {
                stack.push(v);
            }
        }

        let mut size: Vec<usize> = vec![0; n];
        let mut ways: Vec<i64> = vec![1; n];

        for &u in order.iter().rev() {
            let mut total = 0usize;
            let mut w = 1i64;
            for &v in &children[u] {
                // multiply by ways of child subtree
                w = w * ways[v] % MOD;
                // interleave this child's subtree with previously processed ones
                w = w * comb(total + size[v], size[v], &fact, &inv_fact) % MOD;
                total += size[v];
            }
            size[u] = 1 + total;
            ways[u] = w;
        }

        ways[0] as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

;; fast modular exponentiation
(define (pow-mod base exp)
  (let loop ((b (modulo base MOD)) (e exp) (res 1))
    (if (= e 0)
        res
        (loop (modulo (* b b) MOD)
              (arithmetic-shift e -1)
              (if (odd? e) (modulo (* res b) MOD) res)))))

(define/contract (ways-to-build-rooms prevRoom)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length prevRoom))
         (arr (list->vector prevRoom))
         
         ;; build children adjacency list
         (children (make-vector n '()))
         (_ (for ([i (in-range 1 n)])
              (let ((p (vector-ref arr i)))
                (vector-set! children p (cons i (vector-ref children p))))))
         
         ;; precompute factorials and inverse factorials
         (fact (make-vector (+ n 1) 0))
         (invFact (make-vector (+ n 1) 0))
         (_ (begin
              (vector-set! fact 0 1)
              (for ([i (in-range 1 (add1 n))])
                (vector-set! fact i (modulo (* (vector-ref fact (- i 1)) i) MOD)))
              (vector-set! invFact n (pow-mod (vector-ref fact n) (- MOD 2)))
              (for ([i (in-range n 0 -1)])
                (when (> i 0)
                  (vector-set! invFact (- i 1)
                               (modulo (* (vector-ref invFact i) i) MOD))))))

         ;; iterative DFS to obtain processing order (children before parent)
         (stack (list 0))
         (order '())
         (_ (let loop ()
              (when (not (null? stack))
                (define u (car stack))
                (set! stack (cdr stack))
                (set! order (cons u order))
                (for ([v (in-list (vector-ref children u))])
                  (set! stack (cons v stack)))
                (loop))))
         
         ;; vectors for subtree sizes and ways
         (sz (make-vector n 0))
         (ways (make-vector n 1)))

    ;; compute sizes and ways bottom‑up
    (for ([u (in-list order)])
      (let* ((child-list (vector-ref children u))
             (total-child-sz 0)
             (prod-ways 1)
             
             ;; accumulate size and ways from children
             (accumulate
              (lambda ()
                (for ([v (in-list child-list)])
                  (set! total-child-sz (+ total_child_sz (vector-ref sz v)))
                  (set! prod-ways (modulo (* prod-ways (vector-ref ways v)) MOD)))))
             
             ;; multinomial coefficient for interleaving children
             (mult
              (if (= total-child-sz 0)
                  1
                  (let loop ((lst child-list) (acc (vector-ref fact total_child_s z)))
                    (if (null? lst)
                        acc
                        (let* ((szv (vector-ref sz (car lst)))
                               (new-acc (modulo (* acc (vector-ref invFact szv)) MOD)))
                          (loop (cdr lst) new-acc))))))

        ;; compute ways for node u
        (define w (modulo (* prod-ways mult) MOD))
        (vector-set! sz u (+ 1 total-child-sz))
        (vector-set! ways u w)))

    (vector-ref ways 0)))
```
