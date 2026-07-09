# 3152. Special Array II

## Cpp

```cpp
class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> pref(n, 0);
        for (int i = 1; i < n; ++i) {
            pref[i] = pref[i - 1] + ((nums[i] & 1) == (nums[i - 1] & 1));
        }
        vector<bool> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            int l = q[0], r = q[1];
            bool ok = (pref[r] - pref[l]) == 0;
            ans.push_back(ok);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        int n = nums.length;
        int[] prefix = new int[n];
        // prefix[i] stores number of parity violations up to index i
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] + ((nums[i] & 1) == (nums[i - 1] & 1) ? 1 : 0);
        }
        int q = queries.length;
        boolean[] ans = new boolean[q];
        for (int i = 0; i < q; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            ans[i] = prefix[r] - prefix[l] == 0;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(nums)
        pref = [0] * n
        for i in range(1, n):
            pref[i] = pref[i - 1] + (1 if (nums[i] & 1) == (nums[i - 1] & 1) else 0)
        ans = []
        for l, r in queries:
            ans.append(pref[r] == pref[l])
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        pref = [0] * n
        for i in range(1, n):
            pref[i] = pref[i - 1] + (1 if (nums[i] % 2) == (nums[i - 1] % 2) else 0)

        ans = []
        for l, r in queries:
            # No violating index between l+1 and r inclusive means pref[r] - pref[l] == 0
            ans.append(pref[r] - pref[l] == 0)
        return ans
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* isArraySpecial(int* nums, int numsSize, int** queries, int queriesSize,
                     int* queriesColSize, int* returnSize) {
    // Prefix sum of violating indices
    int *prefix = (int *)malloc(sizeof(int) * numsSize);
    if (!prefix) return NULL;
    prefix[0] = 0;
    for (int i = 1; i < numsSize; ++i) {
        if ((nums[i] & 1) == (nums[i - 1] & 1))
            prefix[i] = prefix[i - 1] + 1;
        else
            prefix[i] = prefix[i - 1];
    }

    bool *ans = (bool *)malloc(sizeof(bool) * queriesSize);
    if (!ans) {
        free(prefix);
        return NULL;
    }

    for (int i = 0; i < queriesSize; ++i) {
        int left = queries[i][0];
        int right = queries[i][1];
        ans[i] = (prefix[right] - prefix[left] == 0);
    }

    free(prefix);
    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public bool[] IsArraySpecial(int[] nums, int[][] queries)
    {
        int n = nums.Length;
        int[] prefix = new int[n];
        for (int i = 1; i < n; i++)
        {
            prefix[i] = prefix[i - 1] + ((nums[i] & 1) == (nums[i - 1] & 1) ? 1 : 0);
        }

        bool[] answer = new bool[queries.Length];
        for (int i = 0; i < queries.Length; i++)
        {
            int left = queries[i][0];
            int right = queries[i][1];
            answer[i] = prefix[right] - prefix[left] == 0;
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
 * @return {boolean[]}
 */
var isArraySpecial = function(nums, queries) {
    const n = nums.length;
    const pref = new Array(n).fill(0);
    for (let i = 1; i < n; i++) {
        pref[i] = pref[i - 1] + ((nums[i] & 1) === (nums[i - 1] & 1) ? 1 : 0);
    }
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const [l, r] = queries[i];
        ans[i] = pref[r] - pref[l] === 0;
    }
    return ans;
};
```

## Typescript

```typescript
function isArraySpecial(nums: number[], queries: number[][]): boolean[] {
    const n = nums.length;
    const prefix = new Array<number>(n);
    prefix[0] = 0;
    for (let i = 1; i < n; i++) {
        prefix[i] = prefix[i - 1] + ((nums[i] & 1) === (nums[i - 1] & 1) ? 1 : 0);
    }
    const ans: boolean[] = new Array<boolean>(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const [l, r] = queries[i];
        ans[i] = prefix[r] - prefix[l] === 0;
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
     * @return Boolean[]
     */
    function isArraySpecial($nums, $queries) {
        $n = count($nums);
        $prefix = array_fill(0, $n, 0);
        for ($i = 1; $i < $n; $i++) {
            $prefix[$i] = $prefix[$i - 1];
            if ( ($nums[$i] & 1) == ($nums[$i - 1] & 1) ) {
                $prefix[$i]++;
            }
        }

        $ans = [];
        foreach ($queries as $q) {
            $l = $q[0];
            $r = $q[1];
            $ans[] = ($prefix[$r] - $prefix[$l] == 0);
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func isArraySpecial(_ nums: [Int], _ queries: [[Int]]) -> [Bool] {
        let n = nums.count
        var prefix = Array(repeating: 0, count: n)
        if n > 1 {
            for i in 1..<n {
                let violation = (nums[i] % 2) == (nums[i - 1] % 2) ? 1 : 0
                prefix[i] = prefix[i - 1] + violation
            }
        }
        var answer = [Bool]()
        answer.reserveCapacity(queries.count)
        for q in queries {
            let l = q[0]
            let r = q[1]
            answer.append(prefix[r] - prefix[l] == 0)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isArraySpecial(nums: IntArray, queries: Array<IntArray>): BooleanArray {
        val n = nums.size
        if (n == 0) return BooleanArray(queries.size)
        val prefix = IntArray(n)
        // prefix[i] stores number of parity violations up to index i
        for (i in 1 until n) {
            prefix[i] = prefix[i - 1] + if ((nums[i] and 1) == (nums[i - 1] and 1)) 1 else 0
        }
        val ans = BooleanArray(queries.size)
        for (idx in queries.indices) {
            val q = queries[idx]
            val l = q[0]
            val r = q[1]
            ans[idx] = prefix[r] - prefix[l] == 0
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<bool> isArraySpecial(List<int> nums, List<List<int>> queries) {
    int n = nums.length;
    List<int> prefix = List.filled(n, 0);
    for (int i = 1; i < n; ++i) {
      prefix[i] = prefix[i - 1] + ((nums[i] % 2 == nums[i - 1] % 2) ? 1 : 0);
    }

    List<bool> result = [];
    for (var q in queries) {
      int start = q[0];
      int end = q[1];
      bool ok = (prefix[end] - prefix[start]) == 0;
      result.add(ok);
    }
    return result;
  }
}
```

## Golang

```go
func isArraySpecial(nums []int, queries [][]int) []bool {
	n := len(nums)
	if n == 0 {
		return make([]bool, len(queries))
	}
	prefix := make([]int, n)
	for i := 1; i < n; i++ {
		if (nums[i]&1) == (nums[i-1]&1) {
			prefix[i] = prefix[i-1] + 1
		} else {
			prefix[i] = prefix[i-1]
		}
	}
	ans := make([]bool, len(queries))
	for i, q := range queries {
		l, r := q[0], q[1]
		if prefix[r]-prefix[l] == 0 {
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
def is_array_special(nums, queries)
  n = nums.length
  prefix = Array.new(n, 0)
  (1...n).each do |i|
    prefix[i] = prefix[i - 1]
    if (nums[i] & 1) == (nums[i - 1] & 1)
      prefix[i] += 1
    end
  end

  result = []
  queries.each do |l, r|
    result << (prefix[r] - prefix[l] == 0)
  end
  result
end
```

## Scala

```scala
object Solution {
  def isArraySpecial(nums: Array[Int], queries: Array[Array[Int]]): Array[Boolean] = {
    val n = nums.length
    val prefix = new Array[Int](n)
    var i = 1
    while (i < n) {
      prefix(i) = prefix(i - 1) + (if ((nums(i) & 1) == (nums(i - 1) & 1)) 1 else 0)
      i += 1
    }
    val m = queries.length
    val ans = new Array[Boolean](m)
    var q = 0
    while (q < m) {
      val l = queries(q)(0)
      val r = queries(q)(1)
      ans(q) = prefix(r) - prefix(l) == 0
      q += 1
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn is_array_special(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let n = nums.len();
        if n == 0 {
            return vec![false; queries.len()];
        }
        let mut pref = vec![0usize; n];
        for i in 1..n {
            if (nums[i] & 1) == (nums[i - 1] & 1) {
                pref[i] = pref[i - 1] + 1;
            } else {
                pref[i] = pref[i - 1];
            }
        }

        let mut ans = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let l = q[0] as usize;
            let r = q[1] as usize;
            let is_special = pref[r] - pref[l] == 0;
            ans.push(is_special);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (is-array-special nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof boolean?))
  (let* ((n (length nums))
         (v (list->vector nums))
         (pref (make-vector n 0)))
    ;; build prefix sum of parity violations
    (for ([i (in-range 1 n)])
      (let ((prev (vector-ref v (- i 1)))
            (curr (vector-ref v i)))
        (if (= (modulo prev 2) (modulo curr 2))
            (vector-set! pref i (+ (vector-ref pref (- i 1)) 1))
            (vector-set! pref i (vector-ref pref (- i 1))))))
    ;; answer each query
    (map (lambda (qr)
           (let ((l (first qr))
                 (r (second qr)))
             (= (vector-ref pref r) (vector-ref pref l))))
         queries)))
```

## Erlang

```erlang
-spec is_array_special(Nums :: [integer()], Queries :: [[integer()]]) -> [boolean()].
is_array_special(Nums, Queries) ->
    PrefixVals = build_prefix_vals(Nums),
    PrefixArray = array:from_list(PrefixVals),
    lists:map(fun([L, R]) ->
        PR = array:get(R + 1, PrefixArray),
        PL = array:get(L + 1, PrefixArray),
        (PR - PL) == 0
    end, Queries).

build_prefix_vals([]) -> [];
build_prefix_vals([First | Rest]) ->
    build_prefix_vals(Rest, First, 0, [0]).

build_prefix_vals([], _Prev, _Count, Acc) ->
    lists:reverse(Acc);
build_prefix_vals([Curr | Tail], Prev, Count, Acc) ->
    NewCount = if (Curr band 1) == (Prev band 1) -> Count + 1; true -> Count end,
    build_prefix_vals(Tail, Curr, NewCount, [NewCount | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_array_special(nums :: [integer], queries :: [[integer]]) :: [boolean]
  def is_array_special(nums, queries) do
    # Build prefix tuple where prefix[i] = number of parity violations up to index i
    {_, _, rev_prefix} =
      nums
      |> Enum.with_index()
      |> Enum.reduce({nil, 0, []}, fn
        {val, 0}, {_prev, _cnt, acc} ->
          # first element: no violation yet
          {rem(val, 2), 0, [0 | acc]}

        {val, _idx}, {prev_parity, cnt, acc} ->
          parity = rem(val, 2)
          new_cnt = if parity == prev_parity, do: cnt + 1, else: cnt
          {parity, new_cnt, [new_cnt | acc]}
      end)

    prefix_tuple = rev_prefix |> Enum.reverse() |> List.to_tuple()

    Enum.map(queries, fn [l, r] ->
      diff = elem(prefix_tuple, r) - elem(prefix_tuple, l)
      diff == 0
    end)
  end
end
```
