# 3355. Zero Array Transformation I

## Cpp

```cpp
class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<long long> diff(n + 1, 0);
        for (const auto& q : queries) {
            int l = q[0];
            int r = q[1];
            diff[l] += 1;
            if (r + 1 < n) diff[r + 1] -= 1;
        }
        long long cur = 0;
        for (int i = 0; i < n; ++i) {
            cur += diff[i];
            if (cur < nums[i]) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isZeroArray(int[] nums, int[][] queries) {
        int n = nums.length;
        long[] diff = new long[n + 1];
        for (int[] q : queries) {
            int l = q[0];
            int r = q[1];
            diff[l] += 1;
            if (r + 1 < n) {
                diff[r + 1] -= 1;
            }
        }
        long cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            if (nums[i] > cur) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1
        cnt = 0
        for i in range(n):
            cnt += diff[i]
            if cnt < nums[i]:
                return False
        return True
```

## Python3

```python
class Solution:
    def isZeroArray(self, nums, queries):
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1
        cur = 0
        for i in range(n):
            cur += diff[i]
            if cur < nums[i]:
                return False
        return True
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool isZeroArray(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize) {
    int *diff = (int*)calloc(numsSize + 1, sizeof(int));
    for (int i = 0; i < queriesSize; ++i) {
        int l = queries[i][0];
        int r = queries[i][1];
        diff[l] += 1;
        if (r + 1 < numsSize) diff[r + 1] -= 1;
    }
    long long cur = 0;
    for (int i = 0; i < numsSize; ++i) {
        cur += diff[i];
        if ((long long)nums[i] > cur) {
            free(diff);
            return false;
        }
    }
    free(diff);
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsZeroArray(int[] nums, int[][] queries) {
        int n = nums.Length;
        int[] diff = new int[n + 1];
        foreach (var q in queries) {
            int l = q[0];
            int r = q[1];
            diff[l] += 1;
            diff[r + 1] -= 1; // r+1 is within bounds because diff length is n+1
        }
        int cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            if (nums[i] > cur) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {boolean}
 */
var isZeroArray = function(nums, queries) {
    const n = nums.length;
    const diff = new Array(n + 1).fill(0);
    
    for (const q of queries) {
        const l = q[0];
        const r = q[1];
        diff[l] += 1;
        if (r + 1 < diff.length) diff[r + 1] -= 1;
    }
    
    let cur = 0;
    for (let i = 0; i < n; ++i) {
        cur += diff[i];
        if (cur < nums[i]) return false;
    }
    return true;
};
```

## Typescript

```typescript
function isZeroArray(nums: number[], queries: number[][]): boolean {
    const n = nums.length;
    const diff = new Array(n + 1).fill(0);
    for (const [l, r] of queries) {
        diff[l] += 1;
        if (r + 1 < n) diff[r + 1] -= 1;
    }
    let cur = 0;
    for (let i = 0; i < n; i++) {
        cur += diff[i];
        if (cur < nums[i]) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Boolean
     */
    function isZeroArray($nums, $queries) {
        $n = count($nums);
        // difference array of size n+1 initialized to 0
        $diff = array_fill(0, $n + 1, 0);

        foreach ($queries as $q) {
            $l = $q[0];
            $r = $q[1];
            $diff[$l] += 1;
            if ($r + 1 < $n) {
                $diff[$r + 1] -= 1;
            }
        }

        $curr = 0;
        for ($i = 0; $i < $n; ++$i) {
            $curr += $diff[$i];
            if ($curr < $nums[$i]) {
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
    func isZeroArray(_ nums: [Int], _ queries: [[Int]]) -> Bool {
        let n = nums.count
        var diff = Array(repeating: 0, count: n + 1)
        for q in queries {
            let l = q[0]
            let r = q[1]
            diff[l] += 1
            if r + 1 < diff.count {
                diff[r + 1] -= 1
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
}
```

## Kotlin

```kotlin
class Solution {
    fun isZeroArray(nums: IntArray, queries: Array<IntArray>): Boolean {
        val n = nums.size
        val diff = IntArray(n + 1)
        for (q in queries) {
            val l = q[0]
            val r = q[1]
            diff[l] += 1
            if (r + 1 < n) diff[r + 1] -= 1
        }
        var cur = 0
        for (i in 0 until n) {
            cur += diff[i]
            if (cur < nums[i]) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isZeroArray(List<int> nums, List<List<int>> queries) {
    int n = nums.length;
    List<int> diff = List.filled(n + 1, 0);
    for (var q in queries) {
      int l = q[0];
      int r = q[1];
      diff[l] += 1;
      if (r + 1 < diff.length) diff[r + 1] -= 1;
    }
    int cur = 0;
    for (int i = 0; i < n; ++i) {
      cur += diff[i];
      if (cur < nums[i]) return false;
    }
    return true;
  }
}
```

## Golang

```go
func isZeroArray(nums []int, queries [][]int) bool {
	n := len(nums)
	diff := make([]int, n+1)
	for _, q := range queries {
		l, r := q[0], q[1]
		diff[l]++
		if r+1 < n {
			diff[r+1]--
		}
	}
	cur := 0
	for i := 0; i < n; i++ {
		cur += diff[i]
		if cur < nums[i] {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def is_zero_array(nums, queries)
  n = nums.length
  diff = Array.new(n + 1, 0)

  queries.each do |l, r|
    diff[l] += 1
    diff[r + 1] -= 1 if r + 1 < diff.size
  end

  cur = 0
  (0...n).each do |i|
    cur += diff[i]
    return false if nums[i] > cur
  end
  true
end
```

## Scala

```scala
object Solution {
    def isZeroArray(nums: Array[Int], queries: Array[Array[Int]]): Boolean = {
        val n = nums.length
        val diff = new Array[Long](n + 1)
        var i = 0
        while (i < queries.length) {
            val l = queries(i)(0)
            val r = queries(i)(1)
            diff(l) += 1L
            if (r + 1 < n) diff(r + 1) -= 1L
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
}
```

## Rust

```rust
impl Solution {
    pub fn is_zero_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> bool {
        let n = nums.len();
        let mut diff = vec![0i64; n + 1];
        for q in queries.iter() {
            let l = q[0] as usize;
            let r = q[1] as usize;
            diff[l] += 1;
            diff[r + 1] -= 1;
        }
        let mut cur = 0i64;
        for i in 0..n {
            cur += diff[i];
            if cur < nums[i] as i64 {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (is-zero-array nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) boolean?)
  (let* ((n (length nums))
         (diff (make-vector (+ n 1) 0)))
    ;; apply difference updates for each query
    (for ([q queries])
      (define l (first q))
      (define r (second q))
      (vector-set! diff l (+ 1 (vector-ref diff l)))
      (when (< (+ r 1) (+ n 1))
        (vector-set! diff (+ r 1) (- (vector-ref diff (+ r 1)) 1))))
    ;; compute prefix sums and verify feasibility
    (let loop ((i 0) (cur 0))
      (if (= i n)
          #t
          (let* ((cur (+ cur (vector-ref diff i)))
                 (need (list-ref nums i)))
            (if (< cur need)
                #f
                (loop (+ i 1) cur)))))))
```

## Erlang

```erlang
-spec is_zero_array(Nums :: [integer()], Queries :: [[integer()]]) -> boolean().
is_zero_array(Nums, Queries) ->
    N = length(Nums),
    DiffMap = build_diff_map(Queries, N, #{}),
    check_nums(Nums, DiffMap, 0, 0).

build_diff_map([], _N, Map) -> Map;
build_diff_map([[L,R]|Rest], N, Map) ->
    Map1 = maps:update_with(L,
            fun(V) -> V + 1 end,
            1,
            Map),
    End = R + 1,
    Map2 = if End < N ->
                maps:update_with(End,
                    fun(V) -> V - 1 end,
                    -1,
                    Map1);
           true -> Map1
        end,
    build_diff_map(Rest, N, Map2).

check_nums([], _Map, _Idx, _Cur) -> true;
check_nums([Num|Rest], Map, Idx, Cur) ->
    Delta = maps:get(Idx, Map, 0),
    NewCur = Cur + Delta,
    if NewCur < Num ->
            false;
       true ->
            check_nums(Rest, Map, Idx + 1, NewCur)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_zero_array(nums :: [integer], queries :: [[integer]]) :: boolean
  def is_zero_array(nums, queries) do
    n = length(nums)

    diff =
      Enum.reduce(queries, %{}, fn query, acc ->
        [l, r] = query
        acc = Map.update(acc, l, 1, &(&1 + 1))

        if r + 1 < n do
          Map.update(acc, r + 1, -1, &(&1 - 1))
        else
          acc
        end
      end)

    {_, result} =
      Enum.reduce_while(Enum.with_index(nums), {0, true}, fn {val, idx}, {curr, _} ->
        curr = curr + Map.get(diff, idx, 0)

        if val <= curr do
          {:cont, {curr, true}}
        else
          {:halt, {curr, false}}
        end
      end)

    result
  end
end
```
