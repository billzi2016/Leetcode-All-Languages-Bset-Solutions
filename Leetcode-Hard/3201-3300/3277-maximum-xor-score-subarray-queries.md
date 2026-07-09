# 3277. Maximum XOR Score Subarray Queries

## Cpp

```cpp
class Solution {
public:
    vector<int> maximumSubarrayXor(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n));
        vector<vector<int>> best(n, vector<int>(n));
        // base cases length 1
        for (int i = 0; i < n; ++i) {
            dp[i][i] = nums[i];
            best[i][i] = nums[i];
        }
        // build dp and best for increasing lengths
        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i + len - 1 < n; ++i) {
                int j = i + len - 1;
                dp[i][j] = dp[i][j-1] ^ dp[i+1][j];
                best[i][j] = max({dp[i][j], best[i+1][j], best[i][j-1]});
            }
        }
        vector<int> ans;
        ans.reserve(queries.size());
        for (auto &q : queries) {
            int l = q[0], r = q[1];
            ans.push_back(best[l][r]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] maximumSubarrayXor(int[] nums, int[][] queries) {
        int n = nums.length;
        int[][] dp = new int[n][n];
        int[][] best = new int[n][n];

        for (int len = 1; len <= n; ++len) {
            for (int l = 0; l + len - 1 < n; ++l) {
                int r = l + len - 1;
                if (len == 1) {
                    dp[l][r] = nums[l];
                    best[l][r] = dp[l][r];
                } else {
                    dp[l][r] = dp[l + 1][r] ^ dp[l][r - 1];
                    int m = dp[l][r];
                    if (best[l + 1][r] > m) m = best[l + 1][r];
                    if (best[l][r - 1] > m) m = best[l][r - 1];
                    best[l][r] = m;
                }
            }
        }

        int q = queries.length;
        int[] ans = new int[q];
        for (int i = 0; i < q; ++i) {
            int l = queries[i][0];
            int r = queries[i][1];
            ans[i] = best[l][r];
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumSubarrayXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        # dp[i][j] = XOR score of subarray nums[i..j]
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i][j - 1] ^ dp[i + 1][j]

        # f[i][j] = maximum XOR score of any subarray within nums[i..j]
        f = [[0] * n for _ in range(n)]
        for i in range(n):
            f[i][i] = dp[i][i]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # max of subarrays that end before j, start after i, or exactly [i,j]
                f[i][j] = dp[i][j]
                if f[i][j - 1] > f[i][j]:
                    f[i][j] = f[i][j - 1]
                if f[i + 1][j] > f[i][j]:
                    f[i][j] = f[i + 1][j]

        return [f[l][r] for l, r in queries]
```

## Python3

```python
class Solution:
    def maximumSubarrayXor(self, nums, queries):
        n = len(nums)
        # dp[l][r] = XOR score of subarray nums[l..r]
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for length in range(2, n + 1):
            for l in range(0, n - length + 1):
                r = l + length - 1
                dp[l][r] = dp[l][r - 1] ^ dp[l + 1][r]

        # ans[l][r] = maximum XOR score of any subarray within nums[l..r]
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            ans[i][i] = dp[i][i]
        for length in range(2, n + 1):
            for l in range(0, n - length + 1):
                r = l + length - 1
                a = ans[l][r - 1]
                b = ans[l + 1][r]
                best = a if a >= b else b
                c = dp[l][r]
                if c > best:
                    best = c
                ans[l][r] = best

        return [ans[l][r] for l, r in queries]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maximumSubarrayXor(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    *returnSize = queriesSize;
    int n = numsSize;
    int total = n * n;
    int *score = (int*)malloc(total * sizeof(int));
    int *best  = (int*)malloc(total * sizeof(int));

    // Base cases: subarrays of length 1
    for (int i = 0; i < n; ++i) {
        score[i * n + i] = nums[i];
        best[i * n + i]  = nums[i];
    }

    // Compute XOR scores using dp[l][r] = dp[l][r-1] ^ dp[l+1][r]
    for (int len = 2; len <= n; ++len) {
        for (int l = 0; l + len - 1 < n; ++l) {
            int r = l + len - 1;
            score[l * n + r] = score[l * n + (r - 1)] ^ score[(l + 1) * n + r];
        }
    }

    // Compute best[l][r] = max(best[l][r-1], best[l+1][r], score[l][r])
    for (int len = 2; len <= n; ++len) {
        for (int l = 0; l + len - 1 < n; ++l) {
            int r = l + len - 1;
            int mx = best[l * n + (r - 1)];
            int tmp = best[(l + 1) * n + r];
            if (tmp > mx) mx = tmp;
            int cur = score[l * n + r];
            if (cur > mx) mx = cur;
            best[l * n + r] = mx;
        }
    }

    int *answer = (int*)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; ++i) {
        int l = queries[i][0];
        int r = queries[i][1];
        answer[i] = best[l * n + r];
    }

    free(score);
    free(best);
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int[] MaximumSubarrayXor(int[] nums, int[][] queries) {
        int n = nums.Length;
        var score = new int[n, n];
        for (int i = 0; i < n; i++) {
            score[i, i] = nums[i];
        }
        for (int len = 2; len <= n; ++len) {
            for (int l = 0; l + len - 1 < n; ++l) {
                int r = l + len - 1;
                score[l, r] = score[l, r - 1] ^ score[l + 1, r];
            }
        }

        var best = new int[n, n];
        for (int i = 0; i < n; i++) {
            best[i, i] = score[i, i];
        }
        for (int len = 2; len <= n; ++len) {
            for (int l = 0; l + len - 1 < n; ++l) {
                int r = l + len - 1;
                int m = score[l, r];
                if (best[l, r - 1] > m) m = best[l, r - 1];
                if (best[l + 1, r] > m) m = best[l + 1, r];
                best[l, r] = m;
            }
        }

        int q = queries.Length;
        var answer = new int[q];
        for (int i = 0; i < q; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            answer[i] = best[l, r];
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var maximumSubarrayXor = function(nums, queries) {
    const n = nums.length;
    // dp[l][r] = XOR score of subarray nums[l..r]
    const dp = Array.from({length: n}, () => new Uint32Array(n));
    // best[l][r] = max XOR score among all subarrays within [l, r]
    const best = Array.from({length: n}, () => new Uint32Array(n));

    for (let i = 0; i < n; ++i) {
        const val = nums[i] >>> 0;
        dp[i][i] = val;
        best[i][i] = val;
    }

    for (let len = 2; len <= n; ++len) {
        for (let l = 0, r = len - 1; r < n; ++l, ++r) {
            // dp[l][r] = dp[l+1][r] XOR dp[l][r-1]
            const curDp = dp[l + 1][r] ^ dp[l][r - 1];
            dp[l][r] = curDp;

            let curBest = best[l + 1][r];
            if (best[l][r - 1] > curBest) curBest = best[l][r - 1];
            if (curDp > curBest) curBest = curDp;
            best[l][r] = curBest;
        }
    }

    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        const [l, r] = queries[i];
        ans[i] = best[l][r];
    }
    return ans;
};
```

## Typescript

```typescript
function maximumSubarrayXor(nums: number[], queries: number[][]): number[] {
    const n = nums.length;
    const size = n * n;
    const score = new Uint32Array(size);
    const maxScore = new Uint32Array(size);
    const idx = (i: number, j: number) => i * n + j;

    for (let i = 0; i < n; ++i) {
        const id = idx(i, i);
        const v = nums[i] >>> 0;
        score[id] = v;
        maxScore[id] = v;
    }

    for (let len = 2; len <= n; ++len) {
        for (let l = 0; l + len - 1 < n; ++l) {
            const r = l + len - 1;
            const s = (score[idx(l, r - 1)] ^ score[idx(l + 1, r)]) >>> 0;
            const id = idx(l, r);
            score[id] = s;

            let mx = maxScore[idx(l, r - 1)];
            const m2 = maxScore[idx(l + 1, r)];
            if (m2 > mx) mx = m2;
            if (s > mx) mx = s;
            maxScore[id] = mx;
        }
    }

    const ans: number[] = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        const [l, r] = queries[i];
        ans[i] = maxScore[idx(l, r)];
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function maximumSubarrayXor($nums, $queries) {
        $n = count($nums);
        // initialize dp and maxScore matrices
        $dp = array_fill(0, $n, array_fill(0, $n, 0));
        $maxScore = array_fill(0, $n, array_fill(0, $n, 0));

        // length 1 subarrays
        for ($i = 0; $i < $n; ++$i) {
            $dp[$i][$i] = $nums[$i];
            $maxScore[$i][$i] = $nums[$i];
        }

        // build for increasing lengths
        for ($len = 2; $len <= $n; ++$len) {
            $limit = $n - $len;
            for ($i = 0; $i <= $limit; ++$i) {
                $j = $i + $len - 1;
                // recurrence: score(i,j) = score(i,j-1) XOR score(i+1,j)
                $dp[$i][$j] = $dp[$i][$j - 1] ^ $dp[$i + 1][$j];

                // compute maximum within [i, j]
                $mx = $dp[$i][$j];
                if ($i + 1 <= $j) {
                    $mx = max($mx, $maxScore[$i + 1][$j]);
                }
                if ($i <= $j - 1) {
                    $mx = max($mx, $maxScore[$i][$j - 1]);
                }
                $maxScore[$i][$j] = $mx;
            }
        }

        // answer queries
        $ans = [];
        foreach ($queries as $q) {
            [$l, $r] = $q;
            $ans[] = $maxScore[$l][$r];
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumSubarrayXor(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        var pref = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            pref[i + 1] = pref[i] ^ nums[i]
        }
        var ans = Array(repeating: Array(repeating: 0, count: n + 1), repeatCount: n + 1)
        for l in 0...n {
            var nodes = [[Int]]()
            nodes.append([-1, -1]) // root
            func insert(_ x: Int) {
                var cur = 0
                for b in stride(from: 30, through: 0, by: -1) {
                    let bit = (x >> b) & 1
                    if nodes[cur][bit] == -1 {
                        nodes[cur][bit] = nodes.count
                        nodes.append([-1, -1])
                    }
                    cur = nodes[cur][bit]
                }
            }
            func query(_ x: Int) -> Int {
                var cur = 0
                var res = 0
                for b in stride(from: 30, through: 0, by: -1) {
                    let bit = (x >> b) & 1
                    let prefer = 1 - bit
                    if nodes[cur][prefer] != -1 {
                        res |= (1 << b)
                        cur = nodes[cur][prefer]
                    } else {
                        cur = nodes[cur][bit]
                    }
                }
                return res
            }
            var currentMax = 0
            for r in l...n {
                if r == l {
                    insert(pref[r])
                } else {
                    let best = query(pref[r])
                    if best > currentMax { currentMax = best }
                    insert(pref[r])
                }
                ans[l][r] = currentMax
            }
        }
        var result = [Int]()
        result.reserveCapacity(queries.count)
        for q in queries {
            let l = q[0]
            let r = q[1]
            result.append(ans[l][r + 1])
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumSubarrayXor(nums: IntArray, queries: Array<IntArray>): IntArray {
        val n = nums.size
        // dp[l][r] = XOR score of subarray nums[l..r]
        val dp = Array(n) { IntArray(n) }
        // ans[l][r] = maximum XOR score among all subarrays within [l, r]
        val ans = Array(n) { IntArray(n) }

        for (i in 0 until n) {
            dp[i][i] = nums[i]
            ans[i][i] = nums[i]
        }

        for (len in 2..n) {
            var l = 0
            while (l + len <= n) {
                val r = l + len - 1
                dp[l][r] = dp[l][r - 1] xor dp[l + 1][r]
                var best = dp[l][r]
                if (ans[l][r - 1] > best) best = ans[l][r - 1]
                if (ans[l + 1][r] > best) best = ans[l + 1][r]
                ans[l][r] = best
                l++
            }
        }

        val m = queries.size
        val res = IntArray(m)
        for (i in 0 until m) {
            val q = queries[i]
            val l = q[0]
            val r = q[1]
            res[i] = ans[l][r]
        }
        return res
    }
}
```

## Dart

```dart
import 'dart:typed_data';

class Solution {
  List<int> maximumSubarrayXor(List<int> nums, List<List<int>> queries) {
    int n = nums.length;
    // dp[i][j] = XOR score of subarray nums[i..j]
    List<Int32List> dp = List.generate(n, (_) => Int32List(n));
    for (int i = 0; i < n; ++i) {
      dp[i][i] = nums[i];
    }
    for (int len = 2; len <= n; ++len) {
      for (int i = 0; i + len - 1 < n; ++i) {
        int j = i + len - 1;
        dp[i][j] = dp[i + 1][j] ^ dp[i][j - 1];
      }
    }

    // best[i][j] = maximum XOR score of any subarray within nums[i..j]
    List<Int32List> best = List.generate(n, (_) => Int32List(n));
    for (int i = 0; i < n; ++i) {
      best[i][i] = dp[i][i];
    }
    for (int len = 2; len <= n; ++len) {
      for (int i = 0; i + len - 1 < n; ++i) {
        int j = i + len - 1;
        int m = dp[i][j];
        int b1 = best[i][j - 1];
        if (b1 > m) m = b1;
        int b2 = best[i + 1][j];
        if (b2 > m) m = b2;
        best[i][j] = m;
      }
    }

    List<int> answer = List.filled(queries.length, 0);
    for (int idx = 0; idx < queries.length; ++idx) {
      int l = queries[idx][0];
      int r = queries[idx][1];
      answer[idx] = best[l][r];
    }
    return answer;
  }
}
```

## Golang

```go
func maximumSubarrayXor(nums []int, queries [][]int) []int {
	n := len(nums)
	if n == 0 {
		return nil
	}
	dp := make([][]int, n)
	ans := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, n)
		ans[i] = make([]int, n)
		dp[i][i] = nums[i]
		ans[i][i] = nums[i]
	}
	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			dp[i][j] = dp[i][j-1] ^ dp[i+1][j]
			maxVal := dp[i][j]
			if ans[i][j-1] > maxVal {
				maxVal = ans[i][j-1]
			}
			if ans[i+1][j] > maxVal {
				maxVal = ans[i+1][j]
			}
			ans[i][j] = maxVal
		}
	}
	res := make([]int, len(queries))
	for idx, q := range queries {
		l, r := q[0], q[1]
		res[idx] = ans[l][r]
	}
	return res
}
```

## Ruby

```ruby
def maximum_subarray_xor(nums, queries)
  n = nums.length
  dp = Array.new(n) { Array.new(n, 0) }
  best = Array.new(n) { Array.new(n, 0) }

  i = 0
  while i < n
    dp[i][i] = nums[i]
    best[i][i] = nums[i]
    i += 1
  end

  len = 2
  while len <= n
    i = 0
    limit = n - len
    while i <= limit
      j = i + len - 1
      dp[i][j] = dp[i][j - 1] ^ dp[i + 1][j]
      b = dp[i][j]
      b = best[i + 1][j] if best[i + 1][j] > b
      b = best[i][j - 1] if best[i][j - 1] > b
      best[i][j] = b
      i += 1
    end
    len += 1
  end

  answers = []
  queries.each do |l, r|
    answers << best[l][r]
  end
  answers
end
```

## Scala

```scala
object Solution {
    def maximumSubarrayXor(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
        val n = nums.length
        val dp = Array.ofDim[Int](n, n)
        val best = Array.ofDim[Int](n, n)

        var i = 0
        while (i < n) {
            dp(i)(i) = nums(i)
            best(i)(i) = nums(i)
            i += 1
        }

        var len = 2
        while (len <= n) {
            var start = 0
            while (start + len - 1 < n) {
                val end = start + len - 1
                dp(start)(end) = dp(start + 1)(end) ^ dp(start)(end - 1)
                var mx = dp(start)(end)
                if (best(start + 1)(end) > mx) mx = best(start + 1)(end)
                if (best(start)(end - 1) > mx) mx = best(start)(end - 1)
                best(start)(end) = mx
                start += 1
            }
            len += 1
        }

        val q = queries.length
        val ans = new Array[Int](q)
        var idx = 0
        while (idx < q) {
            val l = queries(idx)(0)
            val r = queries(idx)(1)
            ans(idx) = best(l)(r)
            idx += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_subarray_xor(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        if n == 0 {
            return vec![];
        }
        // dp[l][r] = XOR score of subarray nums[l..=r]
        let mut dp = vec![vec![0i32; n]; n];
        for i in 0..n {
            dp[i][i] = nums[i];
        }
        for len in 2..=n {
            for l in 0..=n - len {
                let r = l + len - 1;
                dp[l][r] = dp[l][r - 1] ^ dp[l + 1][r];
            }
        }
        // best[l][r] = maximum XOR score among all subarrays inside nums[l..=r]
        let mut best = vec![vec![0i32; n]; n];
        for i in 0..n {
            best[i][i] = dp[i][i];
        }
        for len in 2..=n {
            for l in 0..=n - len {
                let r = l + len - 1;
                let mut m = dp[l][r];
                if best[l + 1][r] > m {
                    m = best[l + 1][r];
                }
                if best[l][r - 1] > m {
                    m = best[l][r - 1];
                }
                best[l][r] = m;
            }
        }
        let mut ans = Vec::with_capacity(queries.len());
        for q in queries {
            let l = q[0] as usize;
            let r = q[1] as usize;
            ans.push(best[l][r]);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-subarray-xor nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((n (length nums))
         (nums-vec (list->vector nums))
         (dp (make-vector n))
         (ans (make-vector n)))
    ;; initialize inner vectors
    (for ([i (in-range n)])
      (vector-set! dp i (make-vector n 0))
      (vector-set! ans i (make-vector n 0)))
    ;; base case length 1
    (for ([i (in-range n)])
      (let ((val (vector-ref nums-vec i)))
        (vector-set! (vector-ref dp i) i val)
        (vector-set! (vector-ref ans i) i val)))
    ;; compute dp for longer subarrays using dp[i][j] = dp[i][j-1] xor dp[i+1][j]
    (for ([len (in-range 2 (+ n 1))])
      (for ([i (in-range 0 (+ 1 (- n len)))])
        (let* ((j (+ i (- len 1)))
               (left (vector-ref (vector-ref dp i) (sub1 j)))
               (right (vector-ref (vector-ref dp (add1 i)) j))
               (val (bitwise-xor left right)))
          (vector-set! (vector-ref dp i) j val))))
    ;; compute ans[l][r] = max(dp[l][r], ans[l+1][r], ans[l][r-1])
    (for ([len (in-range 2 (+ n 1))])
      (for ([i (in-range 0 (+ 1 (- n len)))])
        (let* ((j (+ i (- len 1)))
               (a (vector-ref (vector-ref dp i) j))
               (b (vector-ref (vector-ref ans (add1 i)) j))
               (c (vector-ref (vector-ref ans i) (sub1 j)))
               (mx (max a b c)))
          (vector-set! (vector-ref ans i) j mx))))
    ;; answer queries
    (map (lambda (qr)
           (let ((l (list-ref qr 0))
                 (r (list-ref qr 1)))
             (vector-ref (vector-ref ans l) r)))
         queries)))
```

## Erlang

```erlang
-export([maximum_subarray_xor/2]).

-define(TABLE, answer_table).

maximum_subarray_xor(Nums, Queries) ->
    Table = ets:new(?TABLE, [named_table, public, {read_concurrency,true}]),
    N = length(Nums),

    %% insert intervals of length 1
    lists:foldl(
        fun({Val, Idx}, _) ->
            ets:insert(?TABLE, {{Idx, Idx}, Val})
        end,
        ok,
        lists:zip(Nums, lists:seq(0, N-1))
    ),

    %% iterative DP for lengths >= 2
    {_, _} = lists:foldl(
        fun(Len, {PrevDP, PrevAns}) ->
            build_next(PrevDP, PrevAns, Len, 0)
        end,
        {Nums, Nums},
        lists:seq(2, N)
    ),

    %% answer queries
    Answers = [
        begin
            [{_, Val}] = ets:lookup(?TABLE, {L, R}),
            Val
        end || [L, R] <- Queries
    ],

    ets:delete(?TABLE),
    Answers.

%% build_next/4 computes dp and ans for current length,
%% returns {CurDPList, CurAnsList}
build_next([D0, D1 | RestDP], [A0, A1 | RestAns], Len, I) ->
    CurDP = D0 bxor D1,
    MaxAB = if A0 > A1 -> A0; true -> A1 end,
    CurAns = if CurDP > MaxAB -> CurDP; true -> MaxAB end,
    ets:insert(?TABLE, {{I, I + Len - 1}, CurAns}),
    {NextCurDP, NextCurAns} = build_next([D1 | RestDP], [A1 | RestAns], Len, I + 1),
    {[CurDP | NextCurDP], [CurAns | NextCurAns]};
build_next(_, _, _, _) ->
    {[], []}.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec maximum_subarray_xor(nums :: [integer], queries :: [[integer]]) :: [integer]
  def maximum_subarray_xor(nums, queries) do
    n = length(nums)

    # prefix xor tuple
    {pref_rev, _} =
      Enum.reduce(nums, {[0], 0}, fn x, {list, acc} ->
        new_acc = bxor(acc, x)
        {[new_acc | list], new_acc}
      end)

    pref = pref_rev |> Enum.reverse() |> List.to_tuple()

    q = length(queries)

    queries_by_l =
      Enum.with_index(queries)
      |> Enum.reduce(%{}, fn {{l, r}, idx}, acc ->
        Map.update(acc, l, [{r, idx}], fn existing -> [{r, idx} | existing] end)
      end)

    answers = :array.from_list(List.duplicate(0, q))

    final_answers = process_left(0, n, pref, queries_by_l, answers)

    :array.to_list(final_answers)
  end

  defp process_left(l, n, _pref, _queries_by_l, answers) when l == n do
    answers
  end

  defp process_left(l, n, pref, queries_by_l, answers) do
    trie = %{}
    trie = trie_insert(trie, elem(pref, l), 30)
    cur_max = 0
    qs = Map.get(queries_by_l, l, []) |> Enum.sort_by(&elem(&1, 0))

    {answers2, _} = process_right(l, l, n - 1, pref, trie, cur_max, qs, answers)

    process_left(l + 1, n, pref, queries_by_l, answers2)
  end

  defp process_right(_l, r, max_r, _pref, _trie, _cur_max, qs, answers) when r > max_r do
    {answers, qs}
  end

  defp process_right(l, r, max_r, pref, trie, cur_max, qs, answers) do
    val = elem(pref, r + 1)
    best = trie_query(trie, val, 30)
    new_max = if best > cur_max, do: best, else: cur_max
    trie2 = trie_insert(trie, val, 30)

    {answers2, qs2} = handle_queries(r, qs, answers, new_max)

    process_right(l, r + 1, max_r, pref, trie2, new_max, qs2, answers2)
  end

  defp handle_queries(r, [{qr, idx} | rest], answers, cur_max) when qr == r do
    answers = :array.set(idx, cur_max, answers)
    handle_queries(r, rest, answers, cur_max)
  end

  defp handle_queries(_r, qs, answers, _cur_max), do: {answers, qs}

  defp trie_insert(trie, _val, bit) when bit < 0, do: trie

  defp trie_insert(trie, val, bit) do
    b = (val >>> bit) &&& 1
    key = if b == 0, do: :zero, else: :one
    child = Map.get(trie, key, %{})
    new_child = trie_insert(child, val, bit - 1)
    Map.put(trie, key, new_child)
  end

  defp trie_query(_trie, _val, bit) when bit < 0, do: 0

  defp trie_query(trie, val, bit) do
    b = (val >>> bit) &&& 1
    pref_key = if b == 0, do: :one, else: :zero
    alt_key = if b == 0, do: :zero, else: :one

    case Map.get(trie, pref_key) do
      nil ->
        child = Map.get(trie, alt_key)
        trie_query(child, val, bit - 1)

      child_pref ->
        (1 <<< bit) + trie_query(child_pref, val, bit - 1)
    end
  end
end
```
