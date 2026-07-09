# 0996. Number of Squareful Arrays

## Cpp

```cpp
class Solution {
public:
    bool isSquare(long long x) {
        long long r = sqrt((double)x);
        while (r*r < x) ++r;
        while (r*r > x) --r;
        return r*r == x;
    }
    
    int numSquarefulPerms(vector<int>& nums) {
        int n = nums.size();
        vector<vector<bool>> adj(n, vector<bool>(n,false));
        for(int i=0;i<n;++i){
            for(int j=0;j<n;++j){
                if(i!=j && isSquare((long long)nums[i]+nums[j]))
                    adj[i][j]=true;
            }
        }
        int N = 1<<n;
        vector<vector<long long>> dp(N, vector<long long>(n,0));
        for(int i=0;i<n;++i){
            dp[1<<i][i]=1;
        }
        for(int mask=1;mask<N;++mask){
            for(int last=0;last<n;++last){
                long long cur = dp[mask][last];
                if(!cur) continue;
                for(int nxt=0;nxt<n;++nxt){
                    if(!(mask>>nxt & 1) && adj[last][nxt]){
                        dp[mask| (1<<nxt)][nxt] += cur;
                    }
                }
            }
        }
        long long total = 0;
        int full = N-1;
        for(int i=0;i<n;++i) total += dp[full][i];
        
        // divide by factorials of duplicate counts
        unordered_map<int,int> cnt;
        for(int v: nums) ++cnt[v];
        vector<long long> fact(n+1,1);
        for(int i=1;i<=n;++i) fact[i]=fact[i-1]*i;
        long long divisor = 1;
        for(auto &p: cnt){
            divisor *= fact[p.second];
        }
        return (int)(total / divisor);
    }
};
```

## Java

```java
class Solution {
    private int[] nums;
    private boolean[] used;
    private int n;
    private int count = 0;

    public int numSquarefulPerms(int[] nums) {
        this.nums = nums.clone();
        Arrays.sort(this.nums);
        n = this.nums.length;
        used = new boolean[n];
        backtrack(0, -1);
        return count;
    }

    private void backtrack(int depth, int prevIdx) {
        if (depth == n) {
            count++;
            return;
        }
        for (int i = 0; i < n; i++) {
            if (used[i]) continue;
            // skip duplicates
            if (i > 0 && !used[i - 1] && nums[i] == nums[i - 1]) continue;
            if (depth == 0 || isPerfectSquare(nums[prevIdx] + nums[i])) {
                used[i] = true;
                backtrack(depth + 1, i);
                used[i] = false;
            }
        }
    }

    private boolean isPerfectSquare(int sum) {
        int r = (int) Math.sqrt(sum);
        return r * r == sum;
    }
}
```

## Python

```python
class Solution(object):
    def numSquarefulPerms(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        n = len(nums)
        nums.sort()
        # adjacency list where sum is perfect square
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                s = nums[i] + nums[j]
                r = int(math.isqrt(s))
                if r * r == s:
                    adj[i].append(j)
                    adj[j].append(i)

        from functools import lru_cache

        @lru_cache(None)
        def dfs(mask, last):
            if mask == (1 << n) - 1:
                return 1
            total = 0
            for nxt in adj[last]:
                if not (mask >> nxt) & 1:
                    # skip duplicates: ensure we use the first unused occurrence among equal numbers
                    if nxt > 0 and nums[nxt] == nums[nxt - 1] and not ((mask >> (nxt - 1)) & 1):
                        continue
                    total += dfs(mask | (1 << nxt), nxt)
            return total

        ans = 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ans += dfs(1 << i, i)
        return ans
```

## Python3

```python
import math
from typing import List

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        # precompute perfect square adjacency
        adj = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                s = nums[i] + nums[j]
                r = math.isqrt(s)
                if r * r == s:
                    adj[i][j] = True

        used = [False] * n
        self.ans = 0

        def dfs(pos: int, last: int) -> None:
            if pos == n:
                self.ans += 1
                return
            for i in range(n):
                if used[i]:
                    continue
                # skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                if pos > 0 and not adj[last][i]:
                    continue
                used[i] = True
                dfs(pos + 1, i)
                used[i] = False

        dfs(0, -1)
        return self.ans
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

static int n;
static int nums[12];
static char adjMat[12][12];
static long long dp[1 << 12][13];

int cmpInt(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

int isPerfectSquare(long long x) {
    long long r = (long long)sqrt((double)x);
    while ((r + 1) * (r + 1) <= x) ++r;
    while (r * r > x) --r;
    return r * r == x;
}

static long long dfs(int mask, int last) {
    if (mask == (1 << n) - 1)
        return 1;
    long long *memo = dp[mask] + (last + 1);
    if (*memo != -1)
        return *memo;
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        if (mask & (1 << i))
            continue;
        if (i > 0 && nums[i] == nums[i - 1] && !(mask & (1 << (i - 1))))
            continue; // skip duplicate
        if (last == -1 || adjMat[last][i]) {
            ans += dfs(mask | (1 << i), i);
        }
    }
    *memo = ans;
    return ans;
}

int numSquarefulPerms(int* inputNums, int numsSize) {
    n = numsSize;
    for (int i = 0; i < n; ++i)
        nums[i] = inputNums[i];
    qsort(nums, n, sizeof(int), cmpInt);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            adjMat[i][j] = isPerfectSquare((long long)nums[i] + nums[j]);
        }
    }
    memset(dp, -1, sizeof(dp));
    return (int)dfs(0, -1);
}
```

## Csharp

```csharp
public class Solution {
    public int NumSquarefulPerms(int[] nums) {
        int n = nums.Length;
        Array.Sort(nums);
        bool[,] adj = new bool[n, n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                long sum = (long)nums[i] + nums[j];
                long r = (long)Math.Sqrt(sum);
                adj[i, j] = r * r == sum;
            }
        }

        bool[] used = new bool[n];
        long count = 0;

        void Dfs(int pos, int prevIdx) {
            if (pos == n) {
                count++;
                return;
            }
            for (int i = 0; i < n; i++) {
                if (used[i]) continue;
                // skip duplicates
                if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue;
                if (pos == 0 || adj[prevIdx, i]) {
                    used[i] = true;
                    Dfs(pos + 1, i);
                    used[i] = false;
                }
            }
        }

        Dfs(0, -1);
        return (int)count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numSquarefulPerms = function(nums) {
    const n = nums.length;
    nums.sort((a, b) => a - b);
    
    // precompute adjacency: whether sum of i and j is a perfect square
    const adj = Array.from({ length: n }, () => Array(n).fill(false));
    const isSquare = (x) => {
        const r = Math.floor(Math.sqrt(x));
        return r * r === x;
    };
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            if (i !== j && isSquare(nums[i] + nums[j])) adj[i][j] = true;
        }
    }
    
    const fullMask = (1 << n) - 1;
    // dp[mask][last+1], last = -1..n-1, offset by 1
    const dp = Array.from({ length: 1 << n }, () => new Array(n + 1));
    
    function dfs(mask, lastIdx) {
        if (mask === fullMask) return 1;
        const memoIdx = lastIdx + 1; // shift -1 to 0
        if (dp[mask][memoIdx] !== undefined) return dp[mask][memoIdx];
        let total = 0;
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) continue; // already used
            // skip duplicates: ensure we only take the first unused among equal numbers
            if (i > 0 && nums[i] === nums[i - 1] && ((mask >> (i - 1)) & 1) === 0) continue;
            if (lastIdx === -1 || adj[lastIdx][i]) {
                total += dfs(mask | (1 << i), i);
            }
        }
        dp[mask][memoIdx] = total;
        return total;
    }
    
    return dfs(0, -1);
};
```

## Typescript

```typescript
function numSquarefulPerms(nums: number[]): number {
    const n = nums.length;
    nums.sort((a, b) => a - b);
    const adj: boolean[][] = Array.from({ length: n }, () => Array(n).fill(false));
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (i === j) continue;
            const s = nums[i] + nums[j];
            const r = Math.floor(Math.sqrt(s));
            if (r * r === s) adj[i][j] = true;
        }
    }
    const fullMask = (1 << n) - 1;
    const memo = new Map<string, number>();
    function dfs(mask: number, lastIdx: number): number {
        if (mask === fullMask) return 1;
        const key = mask + ',' + lastIdx;
        if (memo.has(key)) return memo.get(key)!;
        let total = 0;
        for (let i = 0; i < n; i++) {
            if ((mask >> i) & 1) continue;
            if (i > 0 && nums[i] === nums[i - 1] && ((mask >> (i - 1)) & 1) === 0) continue;
            if (lastIdx === -1 || adj[lastIdx][i]) {
                total += dfs(mask | (1 << i), i);
            }
        }
        memo.set(key, total);
        return total;
    }
    return dfs(0, -1);
}
```

## Php

```php
class Solution {
    private $n;
    private $nums;
    private $adj;
    private $memo;

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numSquarefulPerms($nums) {
        sort($nums);
        $this->nums = $nums;
        $this->n = count($nums);

        // adjacency matrix: whether sum of two numbers is a perfect square
        $this->adj = array_fill(0, $this->n, array_fill(0, $this->n, false));
        for ($i = 0; $i < $this->n; $i++) {
            for ($j = 0; $j < $this->n; $j++) {
                if ($i == $j) continue;
                $sum = $nums[$i] + $nums[$j];
                $root = (int)sqrt($sum);
                if ($root * $root == $sum) {
                    $this->adj[$i][$j] = true;
                }
            }
        }

        $size = 1 << $this->n;
        $this->memo = array_fill(0, $size, []);

        $total = 0;
        for ($i = 0; $i < $this->n; $i++) {
            // avoid duplicate starting positions
            if ($i > 0 && $this->nums[$i] == $this->nums[$i - 1]) continue;
            $mask = 1 << $i;
            $total += $this->dfs($mask, $i);
        }
        return $total;
    }

    private function dfs($mask, $last) {
        if ($mask == (1 << $this->n) - 1) {
            return 1;
        }
        if (isset($this->memo[$mask][$last])) {
            return $this->memo[$mask][$last];
        }

        $total = 0;
        for ($next = 0; $next < $this->n; $next++) {
            if ($mask & (1 << $next)) continue; // already used

            // skip duplicates: ensure we only use the first unused occurrence of a value
            if ($next > 0 && $this->nums[$next] == $this->nums[$next - 1] && !($mask & (1 << ($next - 1)))) {
                continue;
            }

            if (!$this->adj[$last][$next]) continue;

            $total += $this->dfs($mask | (1 << $next), $next);
        }

        $this->memo[$mask][$last] = $total;
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func numSquarefulPerms(_ nums: [Int]) -> Int {
        let n = nums.count
        var sortedNums = nums.sorted()
        var adj = Array(repeating: Array(repeating: false, count: n), count: n)
        for i in 0..<n {
            for j in 0..<n where i != j {
                let sum = sortedNums[i] + sortedNums[j]
                let r = Int(Double(sum).squareRoot())
                if r * r == sum {
                    adj[i][j] = true
                }
            }
        }
        let fullMask = (1 << n) - 1
        var dp = Array(repeating: Array(repeating: -1, count: n), count: 1 << n)
        func dfs(_ mask: Int, _ last: Int) -> Int {
            if mask == fullMask { return 1 }
            if dp[mask][last] != -1 { return dp[mask][last] }
            var total = 0
            for next in 0..<n {
                if (mask & (1 << next)) != 0 { continue }
                if next > 0 && sortedNums[next] == sortedNums[next - 1] && (mask & (1 << (next - 1))) == 0 {
                    continue
                }
                if adj[last][next] {
                    total += dfs(mask | (1 << next), next)
                }
            }
            dp[mask][last] = total
            return total
        }
        var result = 0
        for i in 0..<n {
            if i > 0 && sortedNums[i] == sortedNums[i - 1] { continue }
            result += dfs(1 << i, i)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numSquarefulPerms(nums: IntArray): Int {
        val n = nums.size
        nums.sort()
        val adj = Array(n) { BooleanArray(n) }
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (i != j && isSquare(nums[i] + nums[j])) {
                    adj[i][j] = true
                }
            }
        }
        val used = BooleanArray(n)
        var count = 0L

        fun dfs(depth: Int, lastIdx: Int) {
            if (depth == n) {
                count++
                return
            }
            for (next in 0 until n) {
                if (used[next]) continue
                if (next > 0 && nums[next] == nums[next - 1] && !used[next - 1]) continue
                if (depth == 0 || adj[lastIdx][next]) {
                    used[next] = true
                    dfs(depth + 1, next)
                    used[next] = false
                }
            }
        }

        dfs(0, -1)
        return count.toInt()
    }

    private fun isSquare(x: Int): Boolean {
        val r = kotlin.math.sqrt(x.toDouble()).toLong()
        return r * r == x.toLong()
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int numSquarefulPerms(List<int> nums) {
    int n = nums.length;
    nums.sort();
    List<List<bool>> adj = List.generate(n, (_) => List.filled(n, false));

    bool isPerfectSquare(int x) {
      int r = sqrt(x).toInt();
      return r * r == x;
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (i != j && isPerfectSquare(nums[i] + nums[j])) {
          adj[i][j] = true;
        }
      }
    }

    List<bool> visited = List.filled(n, false);
    int result = 0;

    void dfs(int depth, int prevIdx) {
      if (depth == n) {
        result++;
        return;
      }
      for (int i = 0; i < n; i++) {
        if (visited[i]) continue;
        // skip duplicates
        if (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1]) continue;
        if (depth > 0 && !adj[prevIdx][i]) continue;

        visited[i] = true;
        dfs(depth + 1, i);
        visited[i] = false;
      }
    }

    dfs(0, -1);
    return result;
  }
}
```

## Golang

```go
package main

import (
	"math"
	"sort"
)

func numSquarefulPerms(nums []int) int {
	n := len(nums)
	sort.Ints(nums)

	adj := make([][]bool, n)
	for i := 0; i < n; i++ {
		adj[i] = make([]bool, n)
		for j := 0; j < n; j++ {
			if i == j {
				continue
			}
			s := nums[i] + nums[j]
			r := int(math.Sqrt(float64(s)))
			if r*r == s {
				adj[i][j] = true
			}
		}
	}

	used := make([]bool, n)

	var dfs func(prevIdx, depth int) int
	dfs = func(prevIdx, depth int) int {
		if depth == n {
			return 1
		}
		total := 0
		for i := 0; i < n; i++ {
			if used[i] {
				continue
			}
			if i > 0 && nums[i] == nums[i-1] && !used[i-1] {
				continue
			}
			if prevIdx != -1 && !adj[prevIdx][i] {
				continue
			}
			used[i] = true
			total += dfs(i, depth+1)
			used[i] = false
		}
		return total
	}

	return dfs(-1, 0)
}
```

## Ruby

```ruby
def num_squareful_perms(nums)
  n = nums.length
  nums.sort!
  full_mask = (1 << n) - 1

  # Build adjacency list where sum of pair is a perfect square
  adj = Array.new(n) { [] }
  n.times do |i|
    ((i + 1)...n).each do |j|
      s = nums[i] + nums[j]
      r = Math.sqrt(s).to_i
      if r * r == s
        adj[i] << j
        adj[j] << i
      end
    end
  end

  memo = {}
  dfs = nil
  dfs = lambda do |mask, last|
    return 1 if mask == full_mask
    key = [mask, last]
    return memo[key] if memo.key?(key)

    total = 0
    n.times do |i|
      next if (mask >> i) & 1 == 1
      # skip duplicates: ensure we pick the first unused identical element
      if i > 0 && nums[i] == nums[i - 1] && ((mask >> (i - 1)) & 1) == 0
        next
      end
      if last == -1 || adj[last].include?(i)
        total += dfs.call(mask | (1 << i), i)
      end
    end

    memo[key] = total
  end

  dfs.call(0, -1)
end
```

## Scala

```scala
object Solution {
    def numSquarefulPerms(nums: Array[Int]): Int = {
        val n = nums.length
        val sorted = nums.sorted
        // Precompute whether sum of two numbers is a perfect square
        val adj = Array.ofDim[Boolean](n, n)
        for (i <- 0 until n) {
            for (j <- 0 until n if i != j) {
                val s = sorted(i).toLong + sorted(j).toLong
                val r = math.sqrt(s.toDouble).toLong
                adj(i)(j) = r * r == s
            }
        }

        val used = new Array[Boolean](n)
        var total: Long = 0L

        def dfs(prevIdx: Int, depth: Int): Unit = {
            if (depth == n) {
                total += 1
                return
            }
            for (i <- 0 until n) {
                if (!used(i)) {
                    if (prevIdx != -1 && !adj(prevIdx)(i)) {
                        // not a square sum with previous element
                    } else if (i > 0 && sorted(i) == sorted(i - 1) && !used(i - 1)) {
                        // skip duplicates to avoid overcounting
                    } else {
                        used(i) = true
                        dfs(i, depth + 1)
                        used(i) = false
                    }
                }
            }
        }

        dfs(-1, 0)
        total.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_squareful_perms(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        // adjacency matrix
        let mut adj = vec![vec![false; n]; n];
        for i in 0..n {
            for j in 0..n {
                if i == j { continue; }
                let sum = nums[i] as i64 + nums[j] as i64;
                let r = (sum as f64).sqrt() as i64;
                if r * r == sum {
                    adj[i][j] = true;
                }
            }
        }

        let size = 1usize << n;
        // dp[mask][last]
        let mut dp = vec![vec![0i32; n]; size];
        for i in 0..n {
            dp[1 << i][i] = 1;
        }

        for mask in 0..size {
            for last in 0..n {
                let cur = dp[mask][last];
                if cur == 0 { continue; }
                for nxt in 0..n {
                    if (mask >> nxt) & 1 == 0 && adj[last][nxt] {
                        let new_mask = mask | (1 << nxt);
                        dp[new_mask][nxt] += cur;
                    }
                }
            }
        }

        let full_mask = size - 1;
        let mut total: i64 = 0;
        for last in 0..n {
            total += dp[full_mask][last] as i64;
        }

        // divide by factorials of duplicate counts
        use std::collections::HashMap;
        let mut cnt: HashMap<i32, usize> = HashMap::new();
        for &v in &nums {
            *cnt.entry(v).or_insert(0) += 1;
        }
        let mut denom: i64 = 1;
        let mut fact = vec![1i64; n + 1];
        for i in 1..=n {
            fact[i] = fact[i - 1] * (i as i64);
        }
        for &c in cnt.values() {
            denom *= fact[c];
        }

        (total / denom) as i32
    }
}
```

## Racket

```racket
(require racket/math)

(define/contract (num-squareful-perms nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [full-mask (- (arithmetic-shift 1 n) 1)]
         [num-vec (list->vector nums)]

         ;; check perfect square
         (define (square? x)
           (let-values ([(s r) (integer-sqrt x)])
             (= r 0)))

         ;; adjacency matrix
         (define adj
           (let ([a (make-vector n)])
             (for ([i (in-range n)])
               (let ([row (make-vector n #f)])
                 (vector-set! a i row)
                 (for ([j (in-range n)])
                   (when (and (not (= i j))
                              (square? (+ (vector-ref num-vec i)
                                          (vector-ref num-vec j))))
                     (vector-set! row j #t)))))
             a))

         ;; memoization hash: key = (cons mask last)
         (define memo (make-hash))

         (define (dp mask last)
           (if (= mask full-mask)
               1
               (let ([key (cons mask last)])
                 (cond [(hash-has-key? memo key) (hash-ref memo key)]
                       [else
                        (define sum 0)
                        (for ([next (in-range n)])
                          (when (and (zero? (bitwise-and mask (arithmetic-shift 1 next)))
                                     (vector-ref (vector-ref adj last) next))
                            (set! sum (+ sum (dp (bitwise-ior mask (arithmetic-shift 1 next)) next)))))
                        (hash-set! memo key sum)
                        sum]))))

         ;; total permutations treating equal elements as distinct
         (define total
           (let ([acc 0])
             (for ([i (in-range n)])
               (set! acc (+ acc (dp (arithmetic-shift 1 i) i))))
             acc))

         ;; factorial
         (define (fact k)
           (let loop ([i k] [res 1])
             (if (zero? i) res (loop (- i 1) (* res i)))))

         ;; frequency of each value
         (define freq (make-hash))
         (for ([v nums])
           (hash-update! freq v add1 0))

         ;; divisor = product of factorials of frequencies
         (define divisor
           (let ([d 1])
             (for ([cnt (in-hash-values freq)])
               (set! d (* d (fact cnt))))
             d)))
    (/ total divisor)))
```

## Erlang

```erlang
-module(solution).
-export([num_squareful_perms/1]).

-spec num_squareful_perms(Nums :: [integer()]) -> integer().
num_squareful_perms(Nums) ->
    Sorted = lists:sort(Nums),
    N = length(Sorted),
    NumTuple = list_to_tuple(Sorted),
    AdjMasks = build_adj_masks(N, NumTuple),
    AllMask = (1 bsl N) - 1,
    dfs(none, 0, N, NumTuple, AdjMasks, AllMask).

%% Build adjacency bitmask for each index
build_adj_masks(N, NumTuple) ->
    lists:map(
      fun(I) ->
          lists:foldl(
            fun(J, Acc) ->
                Sum = element(I + 1, NumTuple) + element(J + 1, NumTuple),
                case is_square(Sum) of
                    true -> Acc bor (1 bsl J);
                    false -> Acc
                end
            end,
            0,
            lists:seq(0, N - 1))
      end,
      lists:seq(0, N - 1)).

%% Check if a number is a perfect square
is_square(S) ->
    T = trunc(math:sqrt(S)),
    T * T == S.

%% Depth‑first search with memoization (process dictionary)
dfs(none, UsedMask, N, NumTuple, AdjMasks, AllMask) ->
    case get({none, UsedMask}) of
        undefined ->
            Count =
                if UsedMask =:= AllMask -> 1;
                   true -> try_start(N, UsedMask, NumTuple, AdjMasks, AllMask)
                end,
            put({none, UsedMask}, Count),
            Count;
        Val -> Val
    end;
dfs(LastIdx, UsedMask, N, NumTuple, AdjMasks, AllMask) ->
    case get({LastIdx, UsedMask}) of
        undefined ->
            Count =
                if UsedMask =:= AllMask -> 1;
                   true -> try_extend(LastIdx, UsedMask, N, NumTuple, AdjMasks, AllMask)
                end,
            put({LastIdx, UsedMask}, Count),
            Count;
        Val -> Val
    end.

%% Try all possible starting positions respecting duplicates
try_start(N, UsedMask, NumTuple, _AdjMasks, AllMask) ->
    lists:foldl(
      fun(I, Acc) ->
          Bit = 1 bsl I,
          case (UsedMask band Bit) of
              0 ->
                  if should_skip(I, UsedMask, NumTuple) -> Acc;
                     true ->
                         dfs(I, UsedMask bor Bit, N, NumTuple, [], AllMask) + Acc
                  end;
              _ -> Acc
          end
      end,
      0,
      lists:seq(0, N - 1)).

%% Try to extend the current permutation
try_extend(LastIdx, UsedMask, N, NumTuple, AdjMasks, AllMask) ->
    AdjMask = lists:nth(LastIdx + 1, AdjMasks),
    lists:foldl(
      fun(I, Acc) ->
          Bit = 1 bsl I,
          case (UsedMask band Bit) of
              0 ->
                  if (AdjMask band Bit) =:= 0 -> Acc;
                     should_skip(I, UsedMask, NumTuple) -> Acc;
                     true ->
                         dfs(I, UsedMask bor Bit, N, NumTuple, AdjMasks, AllMask) + Acc
                  end;
              _ -> Acc
          end
      end,
      0,
      lists:seq(0, N - 1)).

%% Duplicate‑skipping rule
should_skip(I, UsedMask, NumTuple) ->
    if I =:= 0 -> false;
       true ->
           PrevBit = 1 bsl (I - 1),
           NumI = element(I + 1, NumTuple),
           NumPrev = element(I, NumTuple),
           (NumI =:= NumPrev) andalso ((UsedMask band PrevBit) =:= 0)
    end.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec num_squareful_perms(nums :: [integer]) :: integer
  def num_squareful_perms(nums) do
    n = length(nums)
    max_mask = 1 <<< n

    # adjacency list: for each index i, list of indices j where sum is a perfect square
    adj =
      for i <- 0..(n - 1), into: %{} do
        list =
          for j <- 0..(n - 1),
              j != i,
              sum = Enum.at(nums, i) + Enum.at(nums, j),
              is_square(sum),
              do: j

        {i, list}
      end

    # initial DP states: each single element permutation
    dp_initial =
      for i <- 0..(n - 1), into: %{} do
        {{1 <<< i, i}, 1}
      end

    dp =
      Enum.reduce(0..(max_mask - 1), dp_initial, fn mask, acc ->
        Enum.reduce(0..(n - 1), acc, fn i, acc2 ->
          if (mask &&& (1 <<< i)) != 0 do
            cnt = Map.get(acc2, {mask, i}, 0)

            if cnt > 0 do
              Enum.reduce(adj[i], acc2, fn j, acc3 ->
                if (mask &&& (1 <<< j)) == 0 do
                  new_mask = mask ||| (1 <<< j)
                  key = {new_mask, j}
                  Map.update(acc3, key, cnt, &(&1 + cnt))
                else
                  acc3
                end
              end)
            else
              acc2
            end
          else
            acc2
          end
        end)
      end)

    full_mask = max_mask - 1

    total =
      Enum.reduce(0..(n - 1), 0, fn i, sum ->
        sum + Map.get(dp, {full_mask, i}, 0)
      end)

    # divide by factorials of duplicate counts
    freq = Enum.frequencies(nums)

    denom =
      Enum.reduce(freq, 1, fn {_val, c}, acc ->
        acc * fact(c)
      end)

    div(total, denom)
  end

  defp is_square(x) when x >= 0 do
    r = :math.sqrt(x) |> trunc()
    r * r == x
  end

  defp fact(k) when k <= 1, do: 1
  defp fact(k), do: Enum.reduce(2..k, 1, &*/2)
end
```
