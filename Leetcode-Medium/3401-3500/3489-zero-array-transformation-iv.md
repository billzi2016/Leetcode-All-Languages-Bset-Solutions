# 3489. Zero Array Transformation IV

## Cpp

```cpp
class Solution {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        const int MAX_SUM = 1000; // as per constraints
        int n = nums.size();
        int m = queries.size();
        vector<int> earliest(n, -1);
        for (int i = 0; i < n; ++i) {
            if (nums[i] == 0) {
                earliest[i] = 0;
                continue;
            }
            bitset<MAX_SUM + 1> dp;
            dp[0] = 1;
            int found = -1;
            for (int q = 0; q < m; ++q) {
                int l = queries[q][0];
                int r = queries[q][1];
                int v = queries[q][2];
                if (l <= i && i <= r) {
                    dp |= (dp << v);
                }
                if (dp[nums[i]]) {
                    found = q + 1; // number of processed queries
                    break;
                }
            }
            earliest[i] = found;
        }
        int ans = 0;
        for (int step : earliest) {
            if (step == -1) return -1;
            ans = max(ans, step);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minZeroArray(int[] nums, int[][] queries) {
        int n = nums.length;
        // Check if already zero
        boolean allZero = true;
        for (int v : nums) {
            if (v != 0) { allZero = false; break; }
        }
        if (allZero) return 0;

        int[] acc = new int[n];
        for (int k = 0; k < queries.length; k++) {
            int l = queries[k][0];
            int r = queries[k][1];
            int v = queries[k][2];
            for (int i = l; i <= r; i++) {
                acc[i] += v;
            }
            boolean ok = true;
            for (int i = 0; i < n; i++) {
                if (acc[i] < nums[i]) { ok = false; break; }
            }
            if (ok) return k + 1;
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        cur = [0] * n
        if all(v == 0 for v in nums):
            return 0
        for k, (l, r, val) in enumerate(queries, 1):
            for i in range(l, r + 1):
                cur[i] += val
            ok = True
            for i in range(n):
                if cur[i] < nums[i]:
                    ok = False
                    break
            if ok:
                return k
        return -1
```

## Python3

```python
class Solution:
    def minZeroArray(self, nums, queries):
        arr = nums[:]
        if all(v == 0 for v in arr):
            return 0
        for idx, (l, r, val) in enumerate(queries, 1):
            for i in range(l, r + 1):
                if arr[i] > 0:
                    arr[i] = max(0, arr[i] - val)
            if all(v == 0 for v in arr):
                return idx
        return -1
```

## C

```c
int minZeroArray(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize) {
    int cur[11];
    for (int i = 0; i < numsSize; ++i) cur[i] = nums[i];
    
    // check initial zero array
    int allZero = 1;
    for (int i = 0; i < numsSize; ++i) if (cur[i] != 0) { allZero = 0; break; }
    if (allZero) return 0;
    
    for (int q = 0; q < queriesSize; ++q) {
        int l = queries[q][0];
        int r = queries[q][1];
        int v = queries[q][2];
        for (int i = l; i <= r; ++i) {
            if (cur[i] > v) cur[i] -= v;
            else cur[i] = 0;
        }
        allZero = 1;
        for (int i = 0; i < numsSize; ++i) {
            if (cur[i] != 0) { allZero = 0; break; }
        }
        if (allZero) return q + 1;
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int MinZeroArray(int[] nums, int[][] queries) {
        int n = nums.Length;
        int target = 0;
        foreach (int x in nums) if (x > target) target = x;

        // If already zero array
        bool allZero = true;
        foreach (int x in nums) {
            if (x != 0) { allZero = false; break; }
        }
        if (allZero) return 0;

        // dp[i][s] == can achieve sum s using some subset of processed queries affecting index i
        bool[][] dp = new bool[n][];
        for (int i = 0; i < n; i++) {
            dp[i] = new bool[target + 1];
            dp[i][0] = true;
        }

        for (int idx = 0; idx < queries.Length; idx++) {
            int l = queries[idx][0];
            int r = queries[idx][1];
            int v = queries[idx][2];

            for (int i = l; i <= r; i++) {
                bool[] cur = dp[i];
                // update in reverse to avoid using the same query multiple times
                for (int s = target - v; s >= 0; s--) {
                    if (cur[s]) cur[s + v] = true;
                }
            }

            bool ok = true;
            for (int i = 0; i < n; i++) {
                int need = nums[i];
                if (!dp[i][need]) { ok = false; break; }
            }
            if (ok) return idx + 1;
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number}
 */
var minZeroArray = function(nums, queries) {
    const n = nums.length;
    const targetKey = nums.join(',');
    // initial reachable sum: all zeros
    let reachable = new Set();
    reachable.add('0'.repeat(n).split('').map(() => 0).join(',')); // just "0,0,..."
    
    for (let k = 0; k < queries.length; ++k) {
        const [l, r, val] = queries[k];
        // contribution vector of this query
        const contrib = new Array(n).fill(0);
        for (let i = l; i <= r; ++i) contrib[i] = val;
        
        const nextReachable = new Set(reachable); // keep old states
        
        for (const key of reachable) {
            const cur = key.split(',').map(Number);
            let ok = true;
            for (let i = 0; i < n; ++i) {
                if (cur[i] + contrib[i] > nums[i]) { ok = false; break; }
            }
            if (!ok) continue;
            const newArr = cur.map((v, i) => v + contrib[i]);
            nextReachable.add(newArr.join(','));
        }
        
        reachable = nextReachable;
        if (reachable.has(targetKey)) return k + 1; // processed k+1 queries
    }
    
    return -1;
};
```

## Typescript

```typescript
function minZeroArray(nums: number[], queries: number[][]): number {
    const n = nums.length;
    // Check if already zero array
    let alreadyZero = true;
    for (let i = 0; i < n; i++) {
        if (nums[i] !== 0) { alreadyZero = false; break; }
    }
    if (alreadyZero) return 0;

    const cur = new Array(n).fill(0);
    for (let k = 0; k < queries.length; k++) {
        const [l, r, val] = queries[k];
        for (let i = l; i <= r; i++) {
            cur[i] += val;
        }
        let ok = true;
        for (let i = 0; i < n; i++) {
            if (cur[i] < nums[i]) { ok = false; break; }
        }
        if (ok) return k + 1;
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer
     */
    function minZeroArray($nums, $queries) {
        $n = count($nums);
        // current accumulated reductions for each position
        $cur = array_fill(0, $n, 0);

        // check if already zero array
        $allZero = true;
        foreach ($nums as $val) {
            if ($val != 0) {
                $allZero = false;
                break;
            }
        }
        if ($allZero) return 0;

        foreach ($queries as $idx => $q) {
            $l = $q[0];
            $r = $q[1];
            $v = $q[2];
            for ($i = $l; $i <= $r; $i++) {
                $cur[$i] += $v;
            }
            $ok = true;
            for ($i = 0; $i < $n; $i++) {
                if ($cur[$i] < $nums[$i]) {
                    $ok = false;
                    break;
                }
            }
            if ($ok) return $idx + 1; // k is number of processed queries
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func minZeroArray(_ nums: [Int], _ queries: [[Int]]) -> Int {
        let n = nums.count
        var cur = Array(repeating: 0, count: n)
        for (idx, q) in queries.enumerated() {
            let l = q[0]
            let r = q[1]
            let v = q[2]
            for i in l...r {
                cur[i] += v
            }
            var ok = true
            for i in 0..<n {
                if cur[i] != nums[i] {
                    ok = false
                    break
                }
            }
            if ok { return idx + 1 }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minZeroArray(nums: IntArray, queries: Array<IntArray>): Int {
        val n = nums.size
        var allZero = true
        for (v in nums) {
            if (v != 0) { allZero = false; break }
        }
        if (allZero) return 0
        val cur = IntArray(n)
        for (idx in queries.indices) {
            val q = queries[idx]
            val l = q[0]
            val r = q[1]
            val v = q[2]
            for (i in l..r) {
                cur[i] += v
            }
            var ok = true
            for (i in 0 until n) {
                if (cur[i] < nums[i]) { ok = false; break }
            }
            if (ok) return idx + 1
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int minZeroArray(List<int> nums, List<List<int>> queries) {
    List<int> arr = List.from(nums);
    bool allZero() => arr.every((x) => x == 0);
    if (allZero()) return 0;
    for (int i = 0; i < queries.length; i++) {
      int l = queries[i][0];
      int r = queries[i][1];
      int v = queries[i][2];
      for (int idx = l; idx <= r; idx++) {
        arr[idx] -= v;
        if (arr[idx] < 0) arr[idx] = 0;
      }
      if (allZero()) return i + 1;
    }
    return -1;
  }
}
```

## Golang

```go
func minZeroArray(nums []int, queries [][]int) int {
	n := len(nums)
	// Check if already zero
	allZero := true
	for _, v := range nums {
		if v != 0 {
			allZero = false
			break
		}
	}
	if allZero {
		return 0
	}

	cur := make([]int, n)

	for k, q := range queries {
		l, r, val := q[0], q[1], q[2]
		for i := l; i <= r; i++ {
			cur[i] += val
		}
		ok := true
		for i := 0; i < n; i++ {
			if cur[i] < nums[i] {
				ok = false
				break
			}
		}
		if ok {
			return k + 1 // queries are 0-indexed, need count
		}
	}
	return -1
}
```

## Ruby

```ruby
def min_zero_array(nums, queries)
  # Placeholder implementation
  -1
end
```

## Scala

```scala
object Solution {
    def minZeroArray(nums: Array[Int], queries: Array[Array[Int]]): Int = {
        val n = nums.length
        if (n == 0) return 0
        val maxTarget = nums.max
        val m = queries.length

        for (k <- 1 to m) {
            var allOk = true
            var i = 0
            while (i < n && allOk) {
                val target = nums(i)
                // DP for this position using first k queries
                val dp = new Array[Boolean](maxTarget + 1)
                dp(0) = true
                var q = 0
                while (q < k) {
                    val l = queries(q)(0)
                    val r = queries(q)(1)
                    val v = queries(q)(2)
                    if (i >= l && i <= r) {
                        var s = maxTarget - v
                        while (s >= 0) {
                            if (dp(s)) dp(s + v) = true
                            s -= 1
                        }
                    }
                    q += 1
                }
                if (!dp(target)) allOk = false
                i += 1
            }
            if (allOk) return k
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_zero_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        let mut arr = nums.clone();
        if arr.iter().all(|&x| x == 0) {
            return 0;
        }
        for (idx, q) in queries.iter().enumerate() {
            let l = q[0] as usize;
            let r = q[1] as usize;
            let v = q[2];
            for i in l..=r {
                arr[i] = (arr[i] - v).max(0);
            }
            if arr.iter().all(|&x| x == 0) {
                return (idx + 1) as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (min-zero-array nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length nums))
         (target (list->vector nums))
         (sums (make-vector n 0)))
    ;; check if already zero array
    (if (for/and ([i (in-range n)])
          (>= (vector-ref sums i) (vector-ref target i)))
        0
        (let loop ((qs queries) (k 0))
          (cond
            [(null? qs) -1]
            [else
             (define q (car qs))
             (define l (list-ref q 0))
             (define r (list-ref q 1))
             (define v (list-ref q 2))
             (for ([i (in-range l (+ r 1))])
               (vector-set! sums i (+ (vector-ref sums i) v)))
             (if (for/and ([i (in-range n)])
                   (>= (vector-ref sums i) (vector-ref target i)))
                 (+ k 1)
                 (loop (cdr qs) (+ k 1)))])])))
```

## Erlang

```erlang
-spec min_zero_array(Nums :: [integer()], Queries :: [[integer()]]) -> integer().
min_zero_array(Nums, Queries) ->
    case all_zero(Nums) of
        true -> 0;
        false -> loop(Queries, Nums, 0)
    end.

%% Check if all elements are zero
all_zero([]) -> true;
all_zero([H|T]) -> H =:= 0 andalso all_zero(T).

%% Process queries recursively
loop([], _Cur, _K) ->
    -1;
loop([[L,R,V]|Rest], Cur, K) ->
    NewCur = apply_query(Cur, L, R, V),
    NewK = K + 1,
    case all_zero(NewCur) of
        true -> NewK;
        false -> loop(Rest, NewCur, NewK)
    end.

%% Apply a single query to the current array
apply_query(List, L, R, V) ->
    apply_query(List, 0, L, R, V).

apply_query([], _Idx, _L, _R, _V) ->
    [];
apply_query([H|T], Idx, L, R, V) ->
    NewH = if
        Idx >= L, Idx =< R -> erlang:max(0, H - V);
        true -> H
    end,
    [NewH | apply_query(T, Idx + 1, L, R, V)].
```

## Elixir

```elixir
defmodule Solution do
  @spec min_zero_array(nums :: [integer], queries :: [[integer]]) :: integer
  def min_zero_array(nums, queries) do
    n = length(nums)

    # If already all zeros, answer is 0
    if Enum.all?(nums, &(&1 == 0)) do
      0
    else
      initial_sums = List.duplicate(0, n)

      {final_k, _} =
        Enum.reduce_while(Enum.with_index(queries), { -1, initial_sums }, fn {q, idx}, {_k, cur_sums} ->
          [l, r, v] = q
          new_sums = update_range(cur_sums, l, r, v)

          if enough?(new_sums, nums) do
            {:halt, {idx + 1, new_sums}}
          else
            {:cont, {-1, new_sums}}
          end
        end)

      final_k
    end
  end

  defp update_range(sums, l, r, v) do
    Enum.with_index(sums)
    |> Enum.map(fn {val, i} ->
      if i >= l and i <= r, do: val + v, else: val
    end)
  end

  defp enough?(sums, nums) do
    Enum.zip(sums, nums)
    |> Enum.all?(fn {s, n} -> s >= n end)
  end
end
```
