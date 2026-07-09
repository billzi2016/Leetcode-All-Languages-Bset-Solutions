# 1310. XOR Queries of a Subarray

## Cpp

```cpp
class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int n = arr.size();
        vector<int> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] ^ arr[i];
        }
        vector<int> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            int left = q[0], right = q[1];
            ans.push_back(pref[right + 1] ^ pref[left]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        int n = arr.length;
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] ^ arr[i];
        }
        int m = queries.length;
        int[] ans = new int[m];
        for (int i = 0; i < m; i++) {
            int left = queries[i][0];
            int right = queries[i][1];
            ans[i] = pref[right + 1] ^ pref[left];
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]

        res = []
        for left, right in queries:
            res.append(prefix[right + 1] ^ prefix[left])
        return res
```

## Python3

```python
from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
        return [prefix[r + 1] ^ prefix[l] for l, r in queries]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* xorQueries(int* arr, int arrSize, int** queries, int queriesSize,
                int* queriesColSize, int* returnSize) {
    // Build prefix XOR array of size arrSize + 1
    int *prefix = (int *)malloc((arrSize + 1) * sizeof(int));
    if (!prefix) return NULL;
    prefix[0] = 0;
    for (int i = 0; i < arrSize; ++i) {
        prefix[i + 1] = prefix[i] ^ arr[i];
    }

    // Allocate result array
    int *result = (int *)malloc(queriesSize * sizeof(int));
    if (!result) {
        free(prefix);
        return NULL;
    }

    for (int i = 0; i < queriesSize; ++i) {
        int left = queries[i][0];
        int right = queries[i][1];
        result[i] = prefix[right + 1] ^ prefix[left];
    }

    free(prefix);
    *returnSize = queriesSize;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] XorQueries(int[] arr, int[][] queries)
    {
        int n = arr.Length;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++)
        {
            prefix[i + 1] = prefix[i] ^ arr[i];
        }

        int q = queries.Length;
        int[] result = new int[q];
        for (int i = 0; i < q; i++)
        {
            int left = queries[i][0];
            int right = queries[i][1];
            result[i] = prefix[right + 1] ^ prefix[left];
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number[][]} queries
 * @return {number[]}
 */
var xorQueries = function(arr, queries) {
    const n = arr.length;
    const prefix = new Array(n + 1);
    prefix[0] = 0;
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] ^ arr[i];
    }
    const res = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        const [l, r] = queries[i];
        res[i] = prefix[r + 1] ^ prefix[l];
    }
    return res;
};
```

## Typescript

```typescript
function xorQueries(arr: number[], queries: number[][]): number[] {
    const n = arr.length;
    const prefix = new Array<number>(n + 1);
    prefix[0] = 0;
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] ^ arr[i];
    }
    const ans: number[] = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const [l, r] = queries[i];
        ans[i] = prefix[r + 1] ^ prefix[l];
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function xorQueries($arr, $queries) {
        $n = count($arr);
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; ++$i) {
            $prefix[$i + 1] = $prefix[$i] ^ $arr[$i];
        }
        $result = [];
        foreach ($queries as $q) {
            $l = $q[0];
            $r = $q[1];
            $result[] = $prefix[$r + 1] ^ $prefix[$l];
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func xorQueries(_ arr: [Int], _ queries: [[Int]]) -> [Int] {
        let n = arr.count
        var prefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] ^ arr[i]
        }
        var result = [Int]()
        result.reserveCapacity(queries.count)
        for q in queries {
            let left = q[0]
            let right = q[1]
            result.append(prefix[right + 1] ^ prefix[left])
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun xorQueries(arr: IntArray, queries: Array<IntArray>): IntArray {
        val n = arr.size
        val prefix = IntArray(n + 1)
        for (i in 0 until n) {
            prefix[i + 1] = prefix[i] xor arr[i]
        }
        val res = IntArray(queries.size)
        for (i in queries.indices) {
            val left = queries[i][0]
            val right = queries[i][1]
            res[i] = prefix[right + 1] xor prefix[left]
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> xorQueries(List<int> arr, List<List<int>> queries) {
    final n = arr.length;
    final prefix = List<int>.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      prefix[i + 1] = prefix[i] ^ arr[i];
    }
    final result = List<int>.filled(queries.length, 0);
    for (int i = 0; i < queries.length; ++i) {
      final left = queries[i][0];
      final right = queries[i][1];
      result[i] = prefix[right + 1] ^ prefix[left];
    }
    return result;
  }
}
```

## Golang

```go
func xorQueries(arr []int, queries [][]int) []int {
	n := len(arr)
	prefix := make([]int, n+1)
	for i, v := range arr {
		prefix[i+1] = prefix[i] ^ v
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		l, r := q[0], q[1]
		ans[i] = prefix[r+1] ^ prefix[l]
	}
	return ans
}
```

## Ruby

```ruby
def xor_queries(arr, queries)
  n = arr.length
  prefix = Array.new(n + 1, 0)
  (0...n).each do |i|
    prefix[i + 1] = prefix[i] ^ arr[i]
  end

  result = []
  queries.each do |left, right|
    result << (prefix[right + 1] ^ prefix[left])
  end
  result
end
```

## Scala

```scala
object Solution {
    def xorQueries(arr: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
        val n = arr.length
        val prefix = new Array[Int](n + 1)
        var i = 0
        while (i < n) {
            prefix(i + 1) = prefix(i) ^ arr(i)
            i += 1
        }
        val m = queries.length
        val result = new Array[Int](m)
        var j = 0
        while (j < m) {
            val left = queries(j)(0)
            val right = queries(j)(1)
            result(j) = prefix(right + 1) ^ prefix(left)
            j += 1
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn xor_queries(arr: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = arr.len();
        let mut prefix = vec![0i32; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] ^ arr[i];
        }
        let mut result = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let left = q[0] as usize;
            let right = q[1] as usize;
            result.push(prefix[right + 1] ^ prefix[left]);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (xor-queries arr queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((n (length arr))
         (pref (make-vector (+ n 1) 0)))
    ;; build prefix XOR array
    (for ([i (in-range n)])
      (vector-set! pref (+ i 1)
                   (bitwise-xor (vector-ref pref i) (list-ref arr i))))
    ;; answer queries
    (let loop ((qs queries) (acc '()))
      (if (null? qs)
          (reverse acc)
          (let* ((q (car qs))
                 (left (first q))
                 (right (second q))
                 (res (bitwise-xor (vector-ref pref (+ right 1))
                                   (vector-ref pref left))))
            (loop (cdr qs) (cons res acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([xor_queries/2]).

-spec xor_queries(Arr :: [integer()], Queries :: [[integer()]]) -> [integer()].
xor_queries(Arr, Queries) ->
    {PrefixRev, _} = lists:foldl(
        fun(Elem, {ListRev, Prev}) ->
            NewXor = Prev bxor Elem,
            {[NewXor | ListRev], NewXor}
        end,
        {[], 0},
        Arr
    ),
    PrefixVals = [0 | lists:reverse(PrefixRev)],
    PrefixTuple = list_to_tuple(PrefixVals),
    lists:map(
        fun([L, R]) ->
            XorR = element(R + 2, PrefixTuple),
            XorL = element(L + 1, PrefixTuple),
            XorR bxor XorL
        end,
        Queries
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec xor_queries(arr :: [integer], queries :: [[integer]]) :: [integer]
  def xor_queries(arr, queries) do
    require Bitwise

    # Build prefix XOR list with an initial 0
    {_, rev_prefix} =
      Enum.reduce(arr, {0, []}, fn x, {prev, acc} ->
        cur = Bitwise.bxor(prev, x)
        {cur, [cur | acc]}
      end)

    prefix_list = [0 | Enum.reverse(rev_prefix)]
    pref_tuple = List.to_tuple(prefix_list)

    Enum.map(queries, fn [l, r] ->
      left_val = :erlang.element(l + 1, pref_tuple)
      right_val = :erlang.element(r + 2, pref_tuple)
      Bitwise.bxor(right_val, left_val)
    end)
  end
end
```
