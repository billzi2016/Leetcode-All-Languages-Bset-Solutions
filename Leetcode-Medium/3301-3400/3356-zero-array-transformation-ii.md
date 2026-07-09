# 3356. Zero Array Transformation II

## Cpp

```cpp
class Solution {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        int m = queries.size();
        
        // quick check for k=0
        bool allZero = true;
        for (int v : nums) if (v != 0) { allZero = false; break; }
        if (allZero) return 0;
        
        auto canForm = [&](int k)->bool{
            vector<long long> diff(n + 1, 0);
            for (int i = 0; i < k; ++i) {
                int l = queries[i][0];
                int r = queries[i][1];
                int v = queries[i][2];
                diff[l] += v;
                if (r + 1 < n) diff[r + 1] -= v;
            }
            long long cur = 0;
            for (int i = 0; i < n; ++i) {
                cur += diff[i];
                if (cur < nums[i]) return false;
            }
            return true;
        };
        
        if (!canForm(m)) return -1;
        
        int lo = 0, hi = m;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (canForm(mid))
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }
};
```

## Java

```java
class Solution {
    public int minZeroArray(int[] nums, int[][] queries) {
        int n = nums.length;
        int m = queries.length;

        // If already zero array
        boolean alreadyZero = true;
        for (int v : nums) {
            if (v != 0) {
                alreadyZero = false;
                break;
            }
        }
        if (alreadyZero) return 0;

        // If even all queries cannot make it zero, return -1
        if (!canTransform(nums, queries, m)) {
            return -1;
        }

        int lo = 0, hi = m; // search in [0, m]
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (canTransform(nums, queries, mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    private boolean canTransform(int[] nums, int[][] queries, int k) {
        int n = nums.length;
        long[] diff = new long[n + 1];
        for (int i = 0; i < k; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            int v = queries[i][2];
            diff[l] += v;
            if (r + 1 < n) diff[r + 1] -= v;
        }
        long cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            if (cur < nums[i]) return false;
        }
        return true;
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
        m = len(queries)

        def can(k):
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, v = queries[i]
                diff[l] += v
                if r + 1 < n:
                    diff[r + 1] -= v
            cur = 0
            for i in range(n):
                cur += diff[i]
                if cur < nums[i]:
                    return False
            return True

        # If even all queries cannot zero the array, return -1
        if not can(m):
            return -1

        lo, hi = 0, m
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Python3

```python
from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)

        # Helper to check if first k queries can zero the array
        def can(k: int) -> bool:
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, v = queries[i]
                diff[l] += v
                if r + 1 < n:
                    diff[r + 1] -= v
            cur = 0
            for i in range(n):
                cur += diff[i]
                if cur < nums[i]:
                    return False
            return True

        # Quick check for zero queries
        if all(x == 0 for x in nums):
            return 0

        left, right = 1, m
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static bool canFormZero(int *nums, int n, int **queries, int k) {
    long long *diff = (long long *)calloc(n + 1, sizeof(long long));
    if (!diff) return false; // allocation failure, treat as impossible

    for (int i = 0; i < k; ++i) {
        int l = queries[i][0];
        int r = queries[i][1];
        int v = queries[i][2];
        diff[l] += v;
        if (r + 1 < n) diff[r + 1] -= v;
    }

    long long cur = 0;
    for (int i = 0; i < n; ++i) {
        cur += diff[i];
        if (cur < nums[i]) {
            free(diff);
            return false;
        }
    }
    free(diff);
    return true;
}

int minZeroArray(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize){
    // Check if already zero
    bool allZero = true;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] != 0) { allZero = false; break; }
    }
    if (allZero) return 0;

    // If impossible even after all queries
    if (!canFormZero(nums, numsSize, queries, queriesSize))
        return -1;

    int left = 0, right = queriesSize;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (canFormZero(nums, numsSize, queries, mid))
            right = mid;
        else
            left = mid + 1;
    }
    return left;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MinZeroArray(int[] nums, int[][] queries) {
        int n = nums.Length;
        int m = queries.Length;

        // Quick check for k = 0
        bool allZero = true;
        foreach (int v in nums) {
            if (v != 0) { allZero = false; break; }
        }
        if (allZero) return 0;

        // Helper to test if first k queries are enough
        bool Can(int k) {
            long[] diff = new long[n + 1];
            for (int i = 0; i < k; i++) {
                int l = queries[i][0];
                int r = queries[i][1];
                int v = queries[i][2];
                diff[l] += v;
                if (r + 1 < n) diff[r + 1] -= v;
            }
            long cur = 0;
            for (int i = 0; i < n; i++) {
                cur += diff[i];
                if (cur < nums[i]) return false;
            }
            return true;
        }

        // If even all queries are insufficient
        if (!Can(m)) return -1;

        int left = 0, right = m;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (Can(mid))
                right = mid;
            else
                left = mid + 1;
        }
        return left;
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
    const m = queries.length;

    // helper to check if first k queries are enough
    const canForm = (k) => {
        const diff = new Array(n + 1).fill(0);
        for (let i = 0; i < k; i++) {
            const [l, r, v] = queries[i];
            diff[l] += v;
            if (r + 1 < n) diff[r + 1] -= v;
        }
        let cur = 0;
        for (let i = 0; i < n; i++) {
            cur += diff[i];
            if (cur < nums[i]) return false;
        }
        return true;
    };

    // If even all queries cannot zero the array, answer is -1
    if (!canForm(m)) return -1;

    let left = 0, right = m; // search range [left, right]
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (canForm(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
};
```

## Typescript

```typescript
function minZeroArray(nums: number[], queries: number[][]): number {
    const n = nums.length;
    const m = queries.length;

    const canForm = (k: number): boolean => {
        const diff = new Array(n + 1).fill(0);
        for (let i = 0; i < k; ++i) {
            const [l, r, v] = queries[i];
            diff[l] += v;
            if (r + 1 <= n) diff[r + 1] -= v;
        }
        let cur = 0;
        for (let i = 0; i < n; ++i) {
            cur += diff[i];
            if (cur < nums[i]) return false;
        }
        return true;
    };

    if (!canForm(m)) return -1;

    let left = 0, right = m;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (canForm(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
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
    public function minZeroArray($nums, $queries) {
        // If nums already all zeros, answer is 0
        $allZero = true;
        foreach ($nums as $v) {
            if ($v != 0) {
                $allZero = false;
                break;
            }
        }
        if ($allZero) {
            return 0;
        }

        $m = count($queries);
        $low = 1;               // we already know 0 is insufficient
        $high = $m;
        $ans = -1;

        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            if ($this->canFormZeroArray($nums, $queries, $mid)) {
                $ans = $mid;
                $high = $mid - 1;
            } else {
                $low = $mid + 1;
            }
        }

        return $ans;
    }

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @param int $k number of queries to consider (prefix length)
     * @return bool
     */
    private function canFormZeroArray($nums, $queries, $k) {
        $n = count($nums);
        // difference array for range additions
        $diff = array_fill(0, $n + 1, 0);

        for ($i = 0; $i < $k; $i++) {
            [$l, $r, $v] = $queries[$i];
            $diff[$l] += $v;
            if ($r + 1 < $n) {
                $diff[$r + 1] -= $v;
            }
        }

        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur += $diff[$i];
            if ($cur < $nums[$i]) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func minZeroArray(_ nums: [Int], _ queries: [[Int]]) -> Int {
        let n = nums.count
        let m = queries.count
        
        // If already zero array
        var allZero = true
        for v in nums {
            if v != 0 { allZero = false; break }
        }
        if allZero { return 0 }
        
        func canForm(_ k: Int) -> Bool {
            var diff = [Int](repeating: 0, count: n + 1)
            if k > 0 {
                for i in 0..<k {
                    let q = queries[i]
                    let l = q[0]
                    let r = q[1]
                    let v = q[2]
                    diff[l] += v
                    if r + 1 < n { diff[r + 1] -= v }
                }
            }
            var cur = 0
            for i in 0..<n {
                cur += diff[i]
                if cur < nums[i] {
                    return false
                }
            }
            return true
        }
        
        // If even all queries can't make it zero
        if !canForm(m) { return -1 }
        
        var left = 1
        var right = m
        while left < right {
            let mid = (left + right) / 2
            if canForm(mid) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minZeroArray(nums: IntArray, queries: Array<IntArray>): Int {
        val n = nums.size
        val m = queries.size

        fun canForm(k: Int): Boolean {
            val diff = LongArray(n + 1)
            for (i in 0 until k) {
                val q = queries[i]
                val l = q[0]
                val r = q[1]
                val v = q[2].toLong()
                diff[l] += v
                if (r + 1 < n) diff[r + 1] -= v
            }
            var sum = 0L
            for (i in 0 until n) {
                sum += diff[i]
                if (sum < nums[i]) return false
            }
            return true
        }

        var left = 0
        var right = m
        var answer = -1
        while (left <= right) {
            val mid = (left + right) ushr 1
            if (canForm(mid)) {
                answer = mid
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minZeroArray(List<int> nums, List<List<int>> queries) {
    int n = nums.length;
    bool alreadyZero = true;
    for (int v in nums) {
      if (v != 0) {
        alreadyZero = false;
        break;
      }
    }
    if (alreadyZero) return 0;

    int m = queries.length;

    bool canForm(int k) {
      List<int> diff = List.filled(n + 1, 0);
      for (int i = 0; i < k; ++i) {
        var q = queries[i];
        int l = q[0];
        int r = q[1];
        int v = q[2];
        diff[l] += v;
        if (r + 1 < diff.length) diff[r + 1] -= v;
      }
      int sum = 0;
      for (int i = 0; i < n; ++i) {
        sum += diff[i];
        if (sum < nums[i]) return false;
      }
      return true;
    }

    if (!canForm(m)) return -1;

    int low = 0, high = m;
    while (low < high) {
      int mid = (low + high) >> 1;
      if (canForm(mid)) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
func minZeroArray(nums []int, queries [][]int) int {
    n := len(nums)
    m := len(queries)

    // check if first k queries can zero the array
    can := func(k int) bool {
        diff := make([]int64, n+1)
        for i := 0; i < k; i++ {
            q := queries[i]
            l, r, v := q[0], q[1], q[2]
            diff[l] += int64(v)
            if r+1 < n {
                diff[r+1] -= int64(v)
            }
        }
        var cur int64
        for i := 0; i < n; i++ {
            cur += diff[i]
            if cur < int64(nums[i]) {
                return false
            }
        }
        return true
    }

    if can(0) {
        return 0
    }
    if !can(m) {
        return -1
    }

    left, right := 1, m
    ans := m
    for left <= right {
        mid := (left + right) / 2
        if can(mid) {
            ans = mid
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return ans
}
```

## Ruby

```ruby
def min_zero_array(nums, queries)
  n = nums.length
  m = queries.length
  diff = Array.new(n + 1, 0)
  cur = 0
  q = 0

  (0...n).each do |i|
    cur += diff[i]
    while cur < nums[i] && q < m
      l, r, v = queries[q]
      if r >= i
        start_idx = [l, i].max
        diff[start_idx] += v
        diff[r + 1] -= v if r + 1 <= n - 1
        cur += v if start_idx == i
      end
      q += 1
    end
    return -1 if cur < nums[i]
  end

  q
end
```

## Scala

```scala
object Solution {
    def minZeroArray(nums: Array[Int], queries: Array[Array[Int]]): Int = {
        val n = nums.length
        val m = queries.length

        def can(k: Int): Boolean = {
            val diff = new Array[Long](n + 1)
            var i = 0
            while (i < k) {
                val q = queries(i)
                val l = q(0)
                val r = q(1)
                val v = q(2).toLong
                diff(l) += v
                if (r + 1 < n) diff(r + 1) -= v
                i += 1
            }
            var cur: Long = 0L
            var idx = 0
            while (idx < n) {
                cur += diff(idx)
                if (cur < nums(idx).toLong) return false
                idx += 1
            }
            true
        }

        if (!can(m)) -1
        else {
            var lo = 0
            var hi = m
            while (lo < hi) {
                val mid = (lo + hi) >>> 1
                if (can(mid)) hi = mid
                else lo = mid + 1
            }
            lo
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_zero_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        if nums.iter().all(|&x| x == 0) {
            return 0;
        }
        let m = queries.len();

        fn can(k: usize, nums: &[i32], queries: &Vec<Vec<i32>>, n: usize) -> bool {
            let mut diff = vec![0i64; n + 1];
            for i in 0..k {
                let q = &queries[i];
                let l = q[0] as usize;
                let r = q[1] as usize;
                let v = q[2] as i64;
                diff[l] += v;
                if r + 1 < n {
                    diff[r + 1] -= v;
                }
            }
            let mut cur: i64 = 0;
            for i in 0..n {
                cur += diff[i];
                if cur < nums[i] as i64 {
                    return false;
                }
            }
            true
        }

        let mut left = 0usize;
        let mut right = m; // inclusive upper bound

        while left < right {
            let mid = (left + right) / 2;
            if can(mid, &nums, &queries, n) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        if left <= m && can(left, &nums, &queries, n) {
            left as i32
        } else {
            -1
        }
    }
}
```

## Racket

```racket
(define/contract (min-zero-array nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length nums))
         (m (length queries))
         (numsV (list->vector nums))
         (L (make-vector m))
         (R (make-vector m))
         (V (make-vector m)))
    ;; store queries in vectors for O(1) access
    (let loop ((i 0) (qs queries))
      (when (< i m)
        (let* ((q (car qs))
               (l (first q))
               (r (second q))
               (v (third q)))
          (vector-set! L i l)
          (vector-set! R i r)
          (vector-set! V i v))
        (loop (+ i 1) (cdr qs))))
    ;; check if first k queries can zero the array
    (define (can? k)
      (let ((diff (make-vector (+ n 1) 0)))
        (let add-loop ((i 0))
          (when (< i k)
            (let* ((l (vector-ref L i))
                   (r (vector-ref R i))
                   (val (vector-ref V i)))
              (vector-set! diff l (+ (vector-ref diff l) val))
              (let ((rp1 (+ r 1)))
                (when (< rp1 (+ n 1))
                  (vector-set! diff rp1 (- (vector-ref diff rp1) val))))
              (add-loop (+ i 1)))))
        (let ((sum 0)
              (ok #t))
          (let check-loop ((i 0))
            (when (and ok (< i n))
              (set! sum (+ sum (vector-ref diff i)))
              (when (< sum (vector-ref numsV i))
                (set! ok #f))
              (check-loop (+ i 1))))
          ok)))
    (if (not (can? m))
        -1
        (let search ((lo 0) (hi m) (ans m))
          (if (> lo hi)
              ans
              (let ((mid (quotient (+ lo hi) 2)))
                (if (can? mid)
                    (search lo (- mid 1) mid)
                    (search (+ mid 1) hi ans))))))))
```

## Erlang

```erlang
-spec min_zero_array(Nums :: [integer()], Queries :: [[integer()]]) -> integer().
min_zero_array(Nums, Queries) ->
    case lists:any(fun(X) -> X =/= 0 end, Nums) of
        false -> 0;
        true ->
            M = length(Queries),
            N = length(Nums),
            case can(M, Nums, Queries, N) of
                false -> -1;
                true -> binary_search(1, M, Nums, Queries, N)
            end
    end.

%% Binary search for minimal k (1..M) such that can(k) is true.
binary_search(L, R, Nums, Queries, N) when L =< R ->
    Mid = (L + R) div 2,
    case can(Mid, Nums, Queries, N) of
        true -> binary_search(L, Mid - 1, Nums, Queries, N);
        false -> binary_search(Mid + 1, R, Nums, Queries, N)
    end;
binary_search(L, _R, _Nums, _Queries, _N) ->
    L.

%% Check if first K queries can zero the array.
can(K, Nums, Queries, N) ->
    Diff0 = array:new(N + 1, {default, 0}),
    Diff = apply_queries(K, Queries, Diff0),
    check_nums(Nums, Diff, 0, 0).

%% Apply first K queries using a difference array.
apply_queries(K, Queries, Diff0) ->
    Sub = lists:sublist(Queries, K),
    lists:foldl(
        fun([L, R, V], DiffAcc) ->
            Diff1 = array:set(L, array:get(L, DiffAcc) + V, DiffAcc),
            Diff2 = array:set(R + 1, array:get(R + 1, Diff1) - V, Diff1),
            Diff2
        end,
        Diff0,
        Sub).

%% Verify that cumulative reductions meet or exceed each element.
check_nums([], _Diff, _Idx, _Sum) ->
    true;
check_nums([Num | Rest], Diff, Idx, Sum) ->
    D = array:get(Idx, Diff),
    NewSum = Sum + D,
    if
        NewSum < Num -> false;
        true -> check_nums(Rest, Diff, Idx + 1, NewSum)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_zero_array(nums :: [integer], queries :: [[integer]]) :: integer
  def min_zero_array(nums, queries) do
    n = length(nums)
    m = length(queries)

    qlist = Enum.map(queries, fn [l, r, v] -> {l, r, v} end)

    # If even all queries cannot zero the array, return -1 early.
    if not can?(m, nums, qlist, n) do
      -1
    else
      binary_search(0, m, -1, nums, qlist, n)
    end
  end

  defp binary_search(left, right, ans, nums, queries, n) do
    if left > right do
      ans
    else
      mid = div(left + right, 2)

      if can?(mid, nums, queries, n) do
        binary_search(left, mid - 1, mid, nums, queries, n)
      else
        binary_search(mid + 1, right, ans, nums, queries, n)
      end
    end
  end

  defp can?(k, nums, queries, n) do
    diff = :array.new(n + 1, default: 0)

    diff =
      Enum.reduce(0..(k - 1), diff, fn idx, acc ->
        {l, r, v} = Enum.at(queries, idx)
        acc = :array.set(l, (:array.get(l, acc) + v))

        if r + 1 <= n do
          :array.set(r + 1, (:array.get(r + 1, acc) - v))
        else
          acc
        end
      end)

    Enum.reduce_while(Enum.with_index(nums), 0, fn {num, i}, sum ->
      sum = sum + :array.get(i, diff)

      if sum < num do
        {:halt, false}
      else
        {:cont, sum}
      end
    end) != false
  end
end
```
