# 0873. Length of Longest Fibonacci Subsequence

## Cpp

```cpp
class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        int n = arr.size();
        unordered_map<int, int> valToIdx;
        vector<vector<int>> dp(n, vector<int>(n, 2));
        int maxLen = 0;
        for (int j = 0; j < n; ++j) {
            valToIdx[arr[j]] = j;
            for (int i = 0; i < j; ++i) {
                int need = arr[j] - arr[i];
                if (need < arr[i]) {
                    auto it = valToIdx.find(need);
                    if (it != valToIdx.end()) {
                        int k = it->second;
                        dp[i][j] = dp[k][i] + 1;
                        maxLen = max(maxLen, dp[i][j]);
                    }
                }
            }
        }
        return maxLen > 2 ? maxLen : 0;
    }
};
```

## Java

```java
class Solution {
    public int lenLongestFibSubseq(int[] arr) {
        int n = arr.length;
        java.util.Map<Integer, Integer> indexMap = new java.util.HashMap<>();
        for (int i = 0; i < n; i++) {
            indexMap.put(arr[i], i);
        }
        int[][] dp = new int[n][n];
        int maxLen = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < j; i++) {
                int need = arr[j] - arr[i];
                Integer k = indexMap.get(need);
                if (k != null && k < i) {
                    dp[i][j] = dp[k][i] + 1;
                } else {
                    dp[i][j] = 2; // start of a potential sequence
                }
                maxLen = Math.max(maxLen, dp[i][j]);
            }
        }
        return maxLen > 2 ? maxLen : 0;
    }
}
```

## Python

```python
class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n < 3:
            return 0
        index = {x: i for i, x in enumerate(arr)}
        dp = [[0] * n for _ in range(n)]
        max_len = 0

        for j in range(n):
            for i in range(j):
                need = arr[j] - arr[i]
                k = index.get(need)
                if k is not None and k < i:
                    # extend existing sequence or start a new one of length 3
                    dp[i][j] = dp[k][i] + 1 if dp[k][i] else 3
                    max_len = max(max_len, dp[i][j])
        return max_len if max_len >= 3 else 0
```

## Python3

```python
class Solution:
    def lenLongestFibSubseq(self, arr):
        n = len(arr)
        idx = {v: i for i, v in enumerate(arr)}
        dp = [[2] * n for _ in range(n)]
        best = 0
        for j in range(n):
            for i in range(j):
                need = arr[j] - arr[i]
                if need < arr[i] and need in idx:
                    k = idx[need]
                    dp[i][j] = dp[k][i] + 1
                    best = max(best, dp[i][j])
        return best if best >= 3 else 0
```

## C

```c
#include <stdlib.h>

int lenLongestFibSubseq(int* arr, int arrSize) {
    if (arrSize < 3) return 0;

    int **dp = (int **)malloc(arrSize * sizeof(int *));
    for (int i = 0; i < arrSize; ++i) {
        dp[i] = (int *)calloc(arrSize, sizeof(int));
    }

    int maxLen = 0;
    for (int j = 0; j < arrSize; ++j) {
        for (int i = 0; i < j; ++i) {
            long long diff = (long long)arr[j] - arr[i];
            if (diff <= 0) {
                dp[i][j] = 2;
                continue;
            }
            int l = 0, r = i - 1, k = -1;
            while (l <= r) {
                int m = (l + r) >> 1;
                if (arr[m] == diff) {
                    k = m;
                    break;
                } else if (arr[m] < diff) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
            if (k != -1) {
                dp[i][j] = dp[k][i] + 1;
                if (dp[i][j] > maxLen) maxLen = dp[i][j];
            } else {
                dp[i][j] = 2;
            }
        }
    }

    for (int i = 0; i < arrSize; ++i) free(dp[i]);
    free(dp);

    return maxLen >= 3 ? maxLen : 0;
}
```

## Csharp

```csharp
public class Solution {
    public int LenLongestFibSubseq(int[] arr) {
        int n = arr.Length;
        var index = new Dictionary<int, int>();
        for (int i = 0; i < n; i++) {
            index[arr[i]] = i;
        }

        int[,] dp = new int[n, n];
        int maxLen = 0;

        for (int j = 0; j < n; j++) {
            for (int i = 0; i < j; i++) {
                int need = arr[j] - arr[i];
                if (need < arr[i] && index.TryGetValue(need, out int k)) {
                    dp[i, j] = dp[k, i] + 1;
                } else {
                    dp[i, j] = 2;
                }
                if (dp[i, j] > maxLen) {
                    maxLen = dp[i, j];
                }
            }
        }

        return maxLen > 2 ? maxLen : 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var lenLongestFibSubseq = function(arr) {
    const n = arr.length;
    const idx = new Map();
    for (let i = 0; i < n; ++i) idx.set(arr[i], i);
    
    const dp = Array.from({ length: n }, () => Array(n).fill(0));
    let maxLen = 0;
    
    for (let j = 0; j < n; ++j) {
        for (let i = 0; i < j; ++i) {
            const need = arr[j] - arr[i];
            if (need < arr[i] && idx.has(need)) {
                const k = idx.get(need);
                dp[i][j] = dp[k][i] > 0 ? dp[k][i] + 1 : 2;
                maxLen = Math.max(maxLen, dp[i][j]);
            }
        }
    }
    
    return maxLen >= 3 ? maxLen : 0;
};
```

## Typescript

```typescript
function lenLongestFibSubseq(arr: number[]): number {
    const n = arr.length;
    const idxMap = new Map<number, number>();
    for (let i = 0; i < n; i++) {
        idxMap.set(arr[i], i);
    }

    // dp[i][j] = length of longest fib-like subsequence ending with arr[i], arr[j]
    const dp: number[][] = Array.from({ length: n }, () => Array(n).fill(2));
    let maxLen = 0;

    for (let j = 0; j < n; j++) {
        for (let i = 0; i < j; i++) {
            const need = arr[j] - arr[i];
            // need must be smaller than arr[i] to keep indices increasing
            if (need < arr[i] && idxMap.has(need)) {
                const k = idxMap.get(need)!;
                dp[i][j] = dp[k][i] + 1;
                maxLen = Math.max(maxLen, dp[i][j]);
            }
        }
    }

    return maxLen >= 3 ? maxLen : 0;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function lenLongestFibSubseq($arr) {
        $n = count($arr);
        if ($n < 3) return 0;
        
        // map value to its index for O(1) lookups
        $index = [];
        for ($i = 0; $i < $n; $i++) {
            $index[$arr[$i]] = $i;
        }
        
        // dp[i][j] = length of longest fib-like subseq ending with arr[i], arr[j]
        $dp = array_fill(0, $n, array_fill(0, $n, 2));
        $maxLen = 0;
        
        for ($j = 0; $j < $n; $j++) {
            for ($i = 0; $i < $j; $i++) {
                $prevVal = $arr[$j] - $arr[$i];
                if (isset($index[$prevVal])) {
                    $k = $index[$prevVal];
                    if ($k < $i) { // ensure increasing order
                        $dp[$i][$j] = $dp[$k][$i] + 1;
                        if ($dp[$i][$j] > $maxLen) {
                            $maxLen = $dp[$i][$j];
                        }
                    }
                }
            }
        }
        
        return $maxLen >= 3 ? $maxLen : 0;
    }
}
```

## Swift

```swift
class Solution {
    func lenLongestFibSubseq(_ arr: [Int]) -> Int {
        let n = arr.count
        if n < 3 { return 0 }
        var indexMap = [Int:Int]()
        for (i, v) in arr.enumerated() {
            indexMap[v] = i
        }
        var dp = Array(repeating: Array(repeating: 0, count: n), count: n)
        var maxLen = 0
        for j in 0..<n {
            for i in 0..<j {
                let need = arr[j] - arr[i]
                if let k = indexMap[need], k < i {
                    dp[i][j] = dp[k][i] + 1
                } else {
                    dp[i][j] = 2
                }
                maxLen = max(maxLen, dp[i][j])
            }
        }
        return maxLen > 2 ? maxLen : 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lenLongestFibSubseq(arr: IntArray): Int {
        val n = arr.size
        if (n < 3) return 0
        val indexMap = HashMap<Int, Int>(n * 2)
        for (i in 0 until n) {
            indexMap[arr[i]] = i
        }
        val dp = Array(n) { IntArray(n) { 2 } }
        var maxLen = 0
        for (j in 0 until n) {
            for (i in 0 until j) {
                val need = arr[j] - arr[i]
                val k = indexMap[need] ?: -1
                if (k >= 0 && k < i) {
                    dp[i][j] = dp[k][i] + 1
                }
                maxLen = kotlin.math.max(maxLen, dp[i][j])
            }
        }
        return if (maxLen > 2) maxLen else 0
    }
}
```

## Dart

```dart
class Solution {
  int lenLongestFibSubseq(List<int> arr) {
    int n = arr.length;
    Map<int, int> idx = {};
    for (int i = 0; i < n; i++) {
      idx[arr[i]] = i;
    }

    List<List<int>> dp = List.generate(n, (_) => List.filled(n, 0));
    int maxLen = 0;

    for (int j = 0; j < n; j++) {
      for (int i = 0; i < j; i++) {
        int need = arr[j] - arr[i];
        if (need < arr[i] && idx.containsKey(need)) {
          int k = idx[need]!;
          dp[i][j] = dp[k][i] + 1;
          if (dp[i][j] > maxLen) maxLen = dp[i][j];
        } else {
          dp[i][j] = 2;
        }
      }
    }

    return maxLen > 2 ? maxLen : 0;
  }
}
```

## Golang

```go
func lenLongestFibSubseq(arr []int) int {
    n := len(arr)
    if n < 3 {
        return 0
    }
    // Map each value to its index for O(1) lookups.
    idx := make(map[int]int, n)
    for i, v := range arr {
        idx[v] = i
    }

    dp := make([][]int, n)
    for i := 0; i < n; i++ {
        dp[i] = make([]int, n)
    }

    maxLen := 0
    for j := 0; j < n; j++ {
        for i := 0; i < j; i++ {
            diff := arr[j] - arr[i]
            k, ok := idx[diff]
            if ok && k < i {
                dp[i][j] = dp[k][i] + 1
            } else {
                dp[i][j] = 2 // start of a potential sequence
            }
            if dp[i][j] > maxLen {
                maxLen = dp[i][j]
            }
        }
    }

    if maxLen >= 3 {
        return maxLen
    }
    return 0
}
```

## Ruby

```ruby
def len_longest_fib_subseq(arr)
  n = arr.length
  idx = {}
  arr.each_with_index { |v, i| idx[v] = i }

  dp = Array.new(n) { Array.new(n, 2) }
  max_len = 0

  (0...n).each do |j|
    (0...j).each do |i|
      prev_val = arr[j] - arr[i]
      k = idx[prev_val]
      if k && k < i
        dp[i][j] = dp[k][i] + 1
        max_len = dp[i][j] if dp[i][j] > max_len
      end
    end
  end

  max_len >= 3 ? max_len : 0
end
```

## Scala

```scala
object Solution {
    def lenLongestFibSubseq(arr: Array[Int]): Int = {
        val n = arr.length
        val indexMap = scala.collection.mutable.Map[Int, Int]()
        for (i <- 0 until n) indexMap(arr(i)) = i

        val dp = Array.ofDim[Int](n, n)
        var maxLen = 0

        for (j <- 0 until n) {
            for (i <- 0 until j) {
                val needed = arr(j) - arr(i)
                indexMap.get(needed) match {
                    case Some(k) if k < i =>
                        dp(i)(j) = dp(k)(i) + 1
                    case _ =>
                        dp(i)(j) = 2
                }
                if (dp(i)(j) > maxLen) maxLen = dp(i)(j)
            }
        }

        if (maxLen >= 3) maxLen else 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn len_longest_fib_subseq(arr: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        let n = arr.len();
        if n < 3 {
            return 0;
        }
        let mut idx: HashMap<i32, usize> = HashMap::new();
        for (i, &v) in arr.iter().enumerate() {
            idx.insert(v, i);
        }
        let mut dp = vec![vec![2usize; n]; n];
        let mut ans = 0usize;
        for j in 0..n {
            for i in 0..j {
                let need = arr[j] - arr[i];
                if let Some(&k) = idx.get(&need) {
                    if k < i {
                        dp[i][j] = dp[k][i] + 1;
                        ans = ans.max(dp[i][j]);
                    }
                }
            }
        }
        if ans >= 3 { ans as i32 } else { 0 }
    }
}
```

## Racket

```racket
(define/contract (len-longest-fib-subseq arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector arr))
         (n (vector-length v)))
    (if (< n 3)
        0
        (begin
          ;; map value -> index
          (define idx (make-hash))
          (for ([i (in-range n)])
            (hash-set! idx (vector-ref v i) i))
          ;; dp[i][j] = length of fib-like seq ending with arr[i],arr[j]
          (define dp (make-vector n))
          (for ([i (in-range n)])
            (vector-set! dp i (make-vector n 2)))
          (define maxlen 0)
          (for ([j (in-range n)])
            (for ([i (in-range j)])
              (let* ((diff (- (vector-ref v j) (vector-ref v i))))
                (if (hash-has-key? idx diff)
                    (let ((k (hash-ref idx diff)))
                      (if (< k i)
                          (let* ((prev-inner (vector-ref dp k))
                                 (len (+ 1 (vector-ref prev-inner i))))
                            (let ((inner (vector-ref dp i)))
                              (vector-set! inner j len))
                            (when (> len maxlen) (set! maxlen len)))
                          (let ((inner (vector-ref dp i)))
                            (vector-set! inner j 2))))
                    (let ((inner (vector-ref dp i)))
                      (vector-set! inner j 2))))))
          (if (>= maxlen 3) maxlen 0))))))
```

## Erlang

```erlang
-module(solution).
-export([len_longest_fib_subseq/1]).

-spec len_longest_fib_subseq(Arr :: [integer()]) -> integer().
len_longest_fib_subseq(Arr) ->
    N = length(Arr),
    case N < 3 of
        true -> 0;
        false ->
            ArrT = list_to_tuple(Arr),
            ValIdx = build_val_idx_map(Arr),
            {_, MaxLen} = loop_j(0, N, ArrT, ValIdx, #{}, 0),
            if MaxLen > 2 -> MaxLen; true -> 0 end
    end.

build_val_idx_map(Arr) ->
    lists:foldl(
        fun({Val, Idx}, Acc) -> maps:put(Val, Idx, Acc) end,
        #{},
        lists:zip(Arr, lists:seq(0, length(Arr) - 1))
    ).

loop_j(J, N, _ArrT, _ValIdx, DPMap, MaxLen) when J >= N ->
    {DPMap, MaxLen};
loop_j(J, N, ArrT, ValIdx, DPMap, MaxLen) ->
    {NewDPMap, NewMax} = loop_i(0, J, ArrT, ValIdx, DPMap, MaxLen),
    loop_j(J + 1, N, ArrT, ValIdx, NewDPMap, NewMax).

loop_i(I, J, _ArrT, _ValIdx, DPMap, MaxLen) when I >= J ->
    {DPMap, MaxLen};
loop_i(I, J, ArrT, ValIdx, DPMap, MaxLen) ->
    Ai = erlang:element(I + 1, ArrT),
    Aj = erlang:element(J + 1, ArrT),
    Diff = Aj - Ai,
    case maps:find(Diff, ValIdx) of
        {ok, K} when K < I ->
            PrevLen = maps:get({K, I}, DPMap, 2),
            Len = PrevLen + 1,
            UpdatedDP = maps:put({I, J}, Len, DPMap),
            UpdatedMax = if Len > MaxLen -> Len; true -> MaxLen end,
            loop_i(I + 1, J, ArrT, ValIdx, UpdatedDP, UpdatedMax);
        _ ->
            UpdatedDP = maps:put({I, J}, 2, DPMap),
            loop_i(I + 1, J, ArrT, ValIdx, UpdatedDP, MaxLen)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec len_longest_fib_subseq(arr :: [integer]) :: integer
  def len_longest_fib_subseq(arr) do
    n = length(arr)

    if n < 3 do
      0
    else
      arr_t = List.to_tuple(arr)

      val_to_idx =
        Enum.with_index(arr)
        |> Map.new(fn {v, i} -> {v, i} end)

      {_, max_len} =
        Enum.reduce(0..(n - 1), {%{}, 0}, fn j, {dp_acc, max_acc} ->
          {dp_new, max_new} =
            Enum.reduce(0..(j - 1), {dp_acc, max_acc}, fn i, {dp_inner, max_inner} ->
              a_i = elem(arr_t, i)
              a_j = elem(arr_t, j)
              diff = a_j - a_i

              len =
                case Map.get(val_to_idx, diff) do
                  nil ->
                    2

                  k when k < i ->
                    prev_len = Map.get(dp_inner, {k, i}, 2)
                    prev_len + 1

                  _ ->
                    2
                end

              dp_updated = Map.put(dp_inner, {i, j}, len)
              max_updated = if len > max_inner, do: len, else: max_inner
              {dp_updated, max_updated}
            end)

          {dp_new, max_new}
        end)

      if max_len >= 3, do: max_len, else: 0
    end
  end
end
```
