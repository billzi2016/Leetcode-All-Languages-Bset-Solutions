# 3532. Path Existence Queries in a Graph I

## Cpp

```cpp
class Solution {
public:
    vector<bool> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        vector<int> comp(n);
        int cur = 0;
        comp[0] = cur;
        for (int i = 1; i < n; ++i) {
            if (nums[i] - nums[i - 1] > maxDiff) ++cur;
            comp[i] = cur;
        }
        vector<bool> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            int u = q[0], v = q[1];
            ans.push_back(comp[u] == comp[v]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public boolean[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        int[] comp = new int[n];
        int cur = 0;
        comp[0] = 0;
        for (int i = 1; i < n; i++) {
            if ((long) nums[i] - nums[i - 1] > maxDiff) {
                cur++;
            }
            comp[i] = cur;
        }
        boolean[] ans = new boolean[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0];
            int v = queries[i][1];
            ans[i] = comp[u] == comp[v];
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        if n == 0:
            return [False] * len(queries)
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid
        ans = []
        for u, v in queries:
            ans.append(comp[u] == comp[v])
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        comp = [0] * n
        cur = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                cur += 1
            comp[i] = cur
        return [comp[u] == comp[v] for u, v in queries]
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool* pathExistenceQueries(int n, int* nums, int numsSize, int maxDiff,
                           int** queries, int queriesSize, int* queriesColSize,
                           int* returnSize) {
    (void)numsSize; // unused
    (void)queriesColSize; // assumed to be 2 for each query

    int *comp = (int *)malloc(sizeof(int) * n);
    if (!comp) return NULL;

    int cur = 0;
    comp[0] = cur;
    for (int i = 1; i < n; ++i) {
        if ((long long)nums[i] - nums[i - 1] > maxDiff)
            ++cur;
        comp[i] = cur;
    }

    bool *ans = (bool *)malloc(sizeof(bool) * queriesSize);
    if (!ans) {
        free(comp);
        return NULL;
    }

    for (int i = 0; i < queriesSize; ++i) {
        int u = queries[i][0];
        int v = queries[i][1];
        ans[i] = (comp[u] == comp[v]);
    }

    *returnSize = queriesSize;
    free(comp);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public bool[] PathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        int[] component = new int[n];
        int curComp = 0;
        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i] - nums[i - 1] > maxDiff) {
                curComp++;
            }
            component[i] = curComp;
        }

        bool[] answer = new bool[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int u = queries[i][0];
            int v = queries[i][1];
            answer[i] = component[u] == component[v];
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} nums
 * @param {number} maxDiff
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var pathExistenceQueries = function(n, nums, maxDiff, queries) {
    const comp = new Array(n);
    let cur = 0;
    comp[0] = 0;
    for (let i = 1; i < n; i++) {
        if (nums[i] - nums[i - 1] > maxDiff) {
            cur++;
        }
        comp[i] = cur;
    }
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const [u, v] = queries[i];
        ans[i] = comp[u] === comp[v];
    }
    return ans;
};
```

## Typescript

```typescript
function pathExistenceQueries(n: number, nums: number[], maxDiff: number, queries: number[][]): boolean[] {
    const comp = new Uint32Array(n);
    let cur = 0;
    comp[0] = 0;
    for (let i = 1; i < n; i++) {
        if (nums[i] - nums[i - 1] <= maxDiff) {
            comp[i] = cur;
        } else {
            cur++;
            comp[i] = cur;
        }
    }
    const ans: boolean[] = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const [u, v] = queries[i];
        ans[i] = comp[u] === comp[v];
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $nums
     * @param Integer $maxDiff
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function pathExistenceQueries($n, $nums, $maxDiff, $queries) {
        $comp = array_fill(0, $n, 0);
        $curr = 0;
        $comp[0] = $curr;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] - $nums[$i - 1] > $maxDiff) {
                $curr++;
            }
            $comp[$i] = $curr;
        }

        $ans = [];
        foreach ($queries as $q) {
            [$u, $v] = $q;
            $ans[] = $comp[$u] === $comp[$v];
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func pathExistenceQueries(_ n: Int, _ nums: [Int], _ maxDiff: Int, _ queries: [[Int]]) -> [Bool] {
        var component = Array(repeating: 0, count: n)
        var current = 0
        for i in 0..<n {
            if i > 0 && nums[i] - nums[i - 1] > maxDiff {
                current += 1
            }
            component[i] = current
        }
        
        var answer = [Bool]()
        answer.reserveCapacity(queries.count)
        for q in queries {
            let u = q[0]
            let v = q[1]
            answer.append(component[u] == component[v])
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun pathExistenceQueries(n: Int, nums: IntArray, maxDiff: Int, queries: Array<IntArray>): BooleanArray {
        val component = IntArray(n)
        var cur = 0
        if (n > 0) component[0] = 0
        for (i in 1 until n) {
            if (nums[i] - nums[i - 1] > maxDiff) cur++
            component[i] = cur
        }
        val answer = BooleanArray(queries.size)
        for (idx in queries.indices) {
            val q = queries[idx]
            answer[idx] = component[q[0]] == component[q[1]]
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<bool> pathExistenceQueries(int n, List<int> nums, int maxDiff, List<List<int>> queries) {
    List<int> comp = List.filled(n, 0);
    int cur = 0;
    comp[0] = cur;
    for (int i = 1; i < n; i++) {
      if (nums[i] - nums[i - 1] > maxDiff) {
        cur++;
      }
      comp[i] = cur;
    }

    List<bool> ans = List.filled(queries.length, false);
    for (int i = 0; i < queries.length; i++) {
      int u = queries[i][0];
      int v = queries[i][1];
      ans[i] = comp[u] == comp[v];
    }
    return ans;
  }
}
```

## Golang

```go
func pathExistenceQueries(n int, nums []int, maxDiff int, queries [][]int) []bool {
	if n == 0 {
		return make([]bool, len(queries))
	}
	comp := make([]int, n)
	cid := 0
	comp[0] = cid
	for i := 1; i < n; i++ {
		if nums[i]-nums[i-1] <= maxDiff {
			comp[i] = cid
		} else {
			cid++
			comp[i] = cid
		}
	}
	ans := make([]bool, len(queries))
	for i, q := range queries {
		u, v := q[0], q[1]
		if comp[u] == comp[v] {
			ans[i] = true
		} else {
			ans[i] = false
		}
	}
	return ans
}
```

## Ruby

```ruby
def path_existence_queries(n, nums, max_diff, queries)
  comp = Array.new(n)
  cur = 0
  comp[0] = cur
  (1...n).each do |i|
    cur += 1 if nums[i] - nums[i - 1] > max_diff
    comp[i] = cur
  end

  queries.map { |u, v| comp[u] == comp[v] }
end
```

## Scala

```scala
object Solution {
    def pathExistenceQueries(n: Int, nums: Array[Int], maxDiff: Int, queries: Array[Array[Int]]): Array[Boolean] = {
        val comp = new Array[Int](n)
        var cur = 0
        if (n > 0) comp(0) = 0
        var i = 1
        while (i < n) {
            if (nums(i) - nums(i - 1) > maxDiff) cur += 1
            comp(i) = cur
            i += 1
        }
        val m = queries.length
        val ans = new Array[Boolean](m)
        var q = 0
        while (q < m) {
            val u = queries(q)(0)
            val v = queries(q)(1)
            ans(q) = comp(u) == comp(v)
            q += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn path_existence_queries(
        n: i32,
        nums: Vec<i32>,
        max_diff: i32,
        queries: Vec<Vec<i32>>,
    ) -> Vec<bool> {
        let n_usize = n as usize;
        let mut comp = vec![0usize; n_usize];
        let mut cur = 0usize;
        for i in 1..n_usize {
            if nums[i] - nums[i - 1] > max_diff {
                cur += 1;
            }
            comp[i] = cur;
        }

        let mut ans = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let u = q[0] as usize;
            let v = q[1] as usize;
            ans.push(comp[u] == comp[v]);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (path-existence-queries n nums maxDiff queries)
  (-> exact-integer? (listof exact-integer?) exact-integer? (listof (listof exact-integer?)) (listof boolean?))
  (let* ([nums-vec (list->vector nums)]
         [comp-vec (make-vector n 0)])
    ;; compute component ids
    (let loop ((i 1) (cur 0))
      (when (< i n)
        (let* ([diff (- (vector-ref nums-vec i) (vector-ref nums-vec (sub1 i)))]
               [abs-diff (if (< diff 0) (- diff) diff)])
          (if (<= abs-diff maxDiff)
              (begin
                (vector-set! comp-vec i cur)
                (loop (+ i 1) cur))
              (let ([newcur (+ cur 1)])
                (vector-set! comp-vec i newcur)
                (loop (+ i 1) newcur))))))
    ;; answer queries
    (map (lambda (q)
           (let* ([u (first q)]
                  [v (second q)])
             (= (vector-ref comp-vec u) (vector-ref comp-vec v))))
         queries)))
```

## Erlang

```erlang
-spec path_existence_queries(N :: integer(), Nums :: [integer()], MaxDiff :: integer(), Queries :: [[integer()]]) -> [boolean()].
path_existence_queries(_N, Nums, MaxDiff, Queries) ->
    CompList = build_comp(Nums, MaxDiff),
    CompTuple = list_to_tuple(CompList),
    lists:map(
        fun([U, V]) ->
            element(U + 1, CompTuple) =:= element(V + 1, CompTuple)
        end,
        Queries).

%% Build component id list for each index.
-spec build_comp([integer()], integer()) -> [integer()].
build_comp([], _MaxDiff) -> [];
build_comp([First | Rest], MaxDiff) ->
    build_comp(Rest, First, 0, [0]).

-spec build_comp([integer()], integer(), integer(), [integer()]) -> [integer()].
build_comp([], _Prev, _CompId, Acc) ->
    lists:reverse(Acc);
build_comp([Num | Rest], Prev, CompId, Acc) ->
    Diff = Num - Prev,
    NewCompId =
        if
            Diff =< MaxDiff -> CompId;
            true -> CompId + 1
        end,
    build_comp(Rest, Num, NewCompId, [NewCompId | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec path_existence_queries(n :: integer, nums :: [integer], max_diff :: integer, queries :: [[integer]]) :: [boolean]
  def path_existence_queries(_n, nums, max_diff, queries) do
    {ids_rev, _, _} =
      Enum.reduce(Enum.with_index(nums), {[], nil, 0}, fn {val, idx},
                                                          {ids_rev, prev, comp} ->
        if idx == 0 do
          {[comp | ids_rev], val, comp}
        else
          if val - prev > max_diff do
            new_comp = comp + 1
            {[new_comp | ids_rev], val, new_comp}
          else
            {[comp | ids_rev], val, comp}
          end
        end
      end)

    ids_tuple = List.to_tuple(Enum.reverse(ids_rev))

    Enum.map(queries, fn [u, v] ->
      elem(ids_tuple, u) == elem(ids_tuple, v)
    end)
  end
end
```
