# 0823. Binary Trees With Factors

## Cpp

```cpp
class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        const long long MOD = 1000000007LL;
        sort(arr.begin(), arr.end());
        int n = arr.size();
        unordered_map<int, int> index;
        for (int i = 0; i < n; ++i) index[arr[i]] = i;
        vector<long long> dp(n, 1); // each number alone forms a tree
        long long result = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (arr[i] % arr[j] == 0) {
                    int rightVal = arr[i] / arr[j];
                    auto it = index.find(rightVal);
                    if (it != index.end()) {
                        dp[i] = (dp[i] + dp[j] * dp[it->second]) % MOD;
                    }
                }
            }
            result = (result + dp[i]) % MOD;
        }
        return static_cast<int>(result);
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1_000_000_007L;
    public int numFactoredBinaryTrees(int[] arr) {
        int n = arr.length;
        java.util.Arrays.sort(arr);
        java.util.Map<Integer, Long> dp = new java.util.HashMap<>();
        for (int v : arr) dp.put(v, 1L); // each number alone
        
        for (int i = 0; i < n; i++) {
            long total = 1L; // the tree consisting of the node itself
            int cur = arr[i];
            for (int j = 0; j < i; j++) {
                int left = arr[j];
                if (cur % left != 0) continue;
                int right = cur / left;
                Long rightCount = dp.get(right);
                if (rightCount == null) continue;
                long add = (dp.get(left) * rightCount) % MOD;
                total = (total + add) % MOD;
            }
            dp.put(cur, total);
        }
        
        long ans = 0L;
        for (long v : dp.values()) {
            ans = (ans + v) % MOD;
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        for i, val in enumerate(arr):
            count = 1  # tree consisting of the node itself
            for j in range(i):
                left = arr[j]
                if val % left == 0:
                    right = val // left
                    if right in dp:
                        count += dp[left] * dp[right]
                        count %= MOD
            dp[val] = count
        return sum(dp.values()) % MOD
```

## Python3

```python
from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()
        dp = {}
        index = {x: i for i, x in enumerate(arr)}
        for i, val in enumerate(arr):
            count = 1  # tree consisting of the node itself
            for j in range(i):
                left = arr[j]
                if val % left == 0:
                    right = val // left
                    if right in dp:
                        add = dp[left] * dp[right]
                        if left != right:
                            add *= 2
                        count += add
            dp[val] = count % MOD
        return sum(dp.values()) % MOD
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007LL

static int cmp_int(const void *a, const void *b) {
    int av = *(const int *)a;
    int bv = *(const int *)b;
    return (av > bv) - (av < bv);
}

static int binarySearch(int *arr, int size, int target) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int mid = left + ((right - left) >> 1);
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

int numFactoredBinaryTrees(int* arr, int arrSize) {
    if (arrSize == 0) return 0;
    qsort(arr, (size_t)arrSize, sizeof(int), cmp_int);
    
    long long *dp = (long long *)malloc(sizeof(long long) * (size_t)arrSize);
    for (int i = 0; i < arrSize; ++i) dp[i] = 1LL;
    
    for (int i = 0; i < arrSize; ++i) {
        for (int j = 0; j < i; ++j) {
            if (arr[i] % arr[j] != 0) continue;
            int complement = arr[i] / arr[j];
            int k = binarySearch(arr, i, complement);
            if (k != -1) {
                dp[i] = (dp[i] + (dp[j] * dp[k]) % MOD) % MOD;
            }
        }
    }
    
    long long result = 0;
    for (int i = 0; i < arrSize; ++i) {
        result += dp[i];
        if (result >= MOD) result -= MOD;
    }
    
    free(dp);
    return (int)(result % MOD);
}
```

## Csharp

```csharp
public class Solution {
    private const int MOD = 1000000007;
    public int NumFactoredBinaryTrees(int[] arr) {
        Array.Sort(arr);
        int n = arr.Length;
        var dp = new long[n];
        var indexMap = new Dictionary<int, int>();
        for (int i = 0; i < n; i++) {
            dp[i] = 1; // single node tree
            indexMap[arr[i]] = i;
        }
        for (int i = 0; i < n; i++) {
            long total = 1; // start with the single-node tree
            for (int j = 0; j < i; j++) {
                if (arr[i] % arr[j] == 0) {
                    int right = arr[i] / arr[j];
                    if (indexMap.TryGetValue(right, out int k)) {
                        total = (total + dp[j] * dp[k]) % MOD;
                    }
                }
            }
            dp[i] = total;
        }
        long result = 0;
        foreach (var val in dp) {
            result = (result + val) % MOD;
        }
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var numFactoredBinaryTrees = function(arr) {
    const MOD = 1000000007n;
    arr.sort((a, b) => a - b);
    const dp = new Map(); // value -> BigInt count
    
    for (let i = 0; i < arr.length; i++) {
        const x = arr[i];
        let ways = 1n; // tree consisting of the node itself
        for (let j = 0; j < i; j++) {
            const y = arr[j];
            if (x % y === 0) {
                const z = x / y;
                if (dp.has(z)) {
                    ways = (ways + dp.get(y) * dp.get(z)) % MOD;
                }
            }
        }
        dp.set(x, ways);
    }
    
    let ans = 0n;
    for (const val of dp.values()) {
        ans = (ans + val) % MOD;
    }
    return Number(ans);
};
```

## Typescript

```typescript
function numFactoredBinaryTrees(arr: number[]): number {
    const MOD = 1000000007n;
    arr.sort((a, b) => a - b);
    const dp = new Map<number, bigint>();
    for (let i = 0; i < arr.length; i++) {
        const val = arr[i];
        let ways = 1n; // tree consisting of the node itself
        for (let j = 0; j < i; j++) {
            if (val % arr[j] === 0) {
                const complement = val / arr[j];
                if (dp.has(complement)) {
                    const left = dp.get(arr[j])!;
                    const right = dp.get(complement)!;
                    ways = (ways + (left * right) % MOD) % MOD;
                }
            }
        }
        dp.set(val, ways);
    }
    let result = 0n;
    for (const count of dp.values()) {
        result = (result + count) % MOD;
    }
    return Number(result);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function numFactoredBinaryTrees($arr) {
        sort($arr);
        $mod = 1000000007;
        $dp = [];
        foreach ($arr as $v) {
            $dp[$v] = 1; // single node tree
        }
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) {
            $val = $arr[$i];
            $cnt = 1;
            for ($j = 0; $j < $i; $j++) {
                $a = $arr[$j];
                if ($val % $a === 0) {
                    $b = intdiv($val, $a);
                    if (isset($dp[$b])) {
                        $add = ($dp[$a] * $dp[$b]) % $mod;
                        if ($a != $b) {
                            $add = ($add * 2) % $mod; // ordered pair
                        }
                        $cnt = ($cnt + $add) % $mod;
                    }
                }
            }
            $dp[$val] = $cnt;
        }
        $ans = 0;
        foreach ($dp as $c) {
            $ans = ($ans + $c) % $mod;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numFactoredBinaryTrees(_ arr: [Int]) -> Int {
        let MOD = 1_000_000_007
        let sortedArr = arr.sorted()
        var dp = [Int: Int64]()
        var result: Int64 = 0
        
        for i in 0..<sortedArr.count {
            let cur = sortedArr[i]
            var total: Int64 = 1   // tree consisting of the node itself
            
            for j in 0..<i {
                let left = sortedArr[j]
                if cur % left == 0 {
                    let right = cur / left
                    if let rightCount = dp[right] {
                        let leftCount = dp[left]!   // left is already processed
                        total += (leftCount * rightCount) % Int64(MOD)
                        if total >= Int64(MOD) { total %= Int64(MOD) }
                    }
                }
            }
            
            total %= Int64(MOD)
            dp[cur] = total
            result = (result + total) % Int64(MOD)
        }
        
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numFactoredBinaryTrees(arr: IntArray): Int {
        val MOD = 1_000_000_007L
        val sorted = arr.sorted()
        val dp = HashMap<Int, Long>()
        for (v in sorted) {
            var ways = 1L // tree consisting of the node itself
            for (left in sorted) {
                if (left > v) break
                if (v % left == 0) {
                    val right = v / left
                    val leftWays = dp[left]
                    val rightWays = dp[right]
                    if (leftWays != null && rightWays != null) {
                        ways = (ways + leftWays * rightWays) % MOD
                    }
                }
            }
            dp[v] = ways
        }
        var ans = 0L
        for (cnt in dp.values) {
            ans = (ans + cnt) % MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numFactoredBinaryTrees(List<int> arr) {
    const int MOD = 1000000007;
    arr.sort();
    int n = arr.length;
    Map<int, int> index = {};
    for (int i = 0; i < n; i++) {
      index[arr[i]] = i;
    }
    List<int> dp = List.filled(n, 1);
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < i; j++) {
        if (arr[i] % arr[j] == 0) {
          int right = arr[i] ~/ arr[j];
          if (index.containsKey(right)) {
            dp[i] = (dp[i] + (dp[j] * dp[index[right]] ) % MOD) % MOD;
          }
        }
      }
    }
    int ans = 0;
    for (int v in dp) {
      ans = (ans + v) % MOD;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

func numFactoredBinaryTrees(arr []int) int {
	const MOD int64 = 1000000007
	sort.Ints(arr)

	dp := make(map[int]int64, len(arr))
	for _, v := range arr {
		dp[v] = 1 // single node tree
	}

	for i := 0; i < len(arr); i++ {
		vi := arr[i]
		for j := 0; j < i; j++ {
			vj := arr[j]
			if vi%vj == 0 {
				complement := vi / vj
				if cnt, ok := dp[complement]; ok {
					product := (dp[vj] * cnt) % MOD
					dp[vi] = (dp[vi] + product) % MOD
				}
			}
		}
	}

	var ans int64
	for _, v := range dp {
		ans = (ans + v) % MOD
	}
	return int(ans)
}
```

## Ruby

```ruby
def num_factored_binary_trees(arr)
  mod = 1_000_000_007
  arr.sort!
  dp = {}
  arr.each { |v| dp[v] = 1 }

  n = arr.length
  (0...n).each do |i|
    vi = arr[i]
    (0...i).each do |j|
      vj = arr[j]
      next unless vi % vj == 0
      right = vi / vj
      if dp.key?(right)
        dp[vi] = (dp[vi] + dp[vj] * dp[right]) % mod
      end
    end
  end

  total = 0
  dp.each_value { |cnt| total = (total + cnt) % mod }
  total
end
```

## Scala

```scala
object Solution {
    def numFactoredBinaryTrees(arr: Array[Int]): Int = {
        val MOD = 1000000007L
        val sorted = arr.sorted
        val indexMap = scala.collection.mutable.Map[Long, Int]()
        for (i <- sorted.indices) {
            indexMap(sorted(i).toLong) = i
        }
        val dp = Array.fill[Long](sorted.length)(1L)
        for (i <- sorted.indices) {
            val cur = sorted(i).toLong
            var j = 0
            while (j < i) {
                val left = sorted(j).toLong
                if (cur % left == 0) {
                    val right = cur / left
                    indexMap.get(right).foreach { k =>
                        dp(i) = (dp(i) + dp(j) * dp(k)) % MOD
                    }
                }
                j += 1
            }
        }
        ((dp.foldLeft(0L)((acc, v) => (acc + v) % MOD)) % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_factored_binary_trees(arr: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut a: Vec<i64> = arr.iter().map(|&x| x as i64).collect();
        a.sort_unstable();
        let n = a.len();
        let mut dp = vec![0i64; n];
        for i in 0..n {
            let v = a[i];
            let mut cnt = 1i64;
            for j in 0..i {
                let left = a[j];
                if v % left == 0 {
                    let right = v / left;
                    if let Ok(k) = a.binary_search(&right) {
                        cnt = (cnt + dp[j] * dp[k] % MOD) % MOD;
                    }
                }
            }
            dp[i] = cnt;
        }
        let mut ans = 0i64;
        for &c in &dp {
            ans += c;
            if ans >= MOD { ans -= MOD; }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (num-factored-binary-trees arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted-list (sort arr <))
         (sorted (list->vector sorted-list))
         (n (vector-length sorted))
         (dp (make-hash)))
    ;; each value can form a single-node tree
    (for ([i (in-range n)])
      (hash-set! dp (vector-ref sorted i) 1))
    ;; compute counts for larger values
    (for ([i (in-range n)])
      (define vi (vector-ref sorted i))
      (define total 1) ; the single-node tree
      (for ([j (in-range i)])
        (define left (vector-ref sorted j))
        (when (= (remainder vi left) 0)
          (define right (quotient vi left))
          (when (hash-has-key? dp right)
            (set! total
                  (modulo (+ total (* (hash-ref dp left) (hash-ref dp right))) MOD)))))
      (hash-set! dp vi total))
    ;; sum all possibilities
    (let ((ans 0))
      (for ([i (in-range n)])
        (define v (vector-ref sorted i))
        (set! ans (modulo (+ ans (hash-ref dp v)) MOD)))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([num_factored_binary_trees/1]).

-define(MOD, 1000000007).

-spec num_factored_binary_trees(Arr :: [integer()]) -> integer().
num_factored_binary_trees(Arr) ->
    Sorted = lists:sort(Arr),
    Set = maps:from_list([{V, true} || V <- Sorted]),
    DP0 = #{},
    {DPMap,_}= lists:foldl(fun(V, {DPAcc, _}) ->
        Count = count_for(V, Sorted, Set, DPAcc),
        NewDP = maps:put(V, Count, DPAcc),
        {NewDP, ok}
    end, {DP0, ok}, Sorted),
    Total = lists:foldl(fun(V, Acc) ->
        (maps:get(V, DPMap) + Acc) rem ?MOD
    end, 0, Sorted),
    Total.

count_for(V, Sorted, Set, DPAcc) ->
    Count0 = 1,
    lists:foldl(fun(L, Acc) ->
        if L > V -> Acc;
           true ->
            case V rem L of
                0 ->
                    R = V div L,
                    case maps:is_key(R, Set) of
                        true ->
                            Cleft = maps:get(L, DPAcc),
                            Cright = maps:get(R, DPAcc),
                            (Acc + ((Cleft * Cright) rem ?MOD)) rem ?MOD;
                        false -> Acc
                    end;
                _ -> Acc
            end
        end
    end, Count0, Sorted).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_factored_binary_trees(arr :: [integer]) :: integer
  def num_factored_binary_trees(arr) do
    mod = 1_000_000_007
    sorted = Enum.sort(arr)

    {dp_map, _} =
      Enum.reduce(sorted, {%{}, []}, fn v, {map_acc, processed} ->
        total =
          Enum.reduce(processed, 1, fn a, acc ->
            if rem(v, a) == 0 do
              b = div(v, a)

              case Map.get(map_acc, b) do
                nil -> acc
                dp_b ->
                  dp_a = map_acc[a]
                  add = (dp_a * dp_b) |> rem(mod)
                  (acc + add) |> rem(mod)
              end
            else
              acc
            end
          end)

        {Map.put(map_acc, v, total), processed ++ [v]}
      end)

    Enum.reduce(dp_map, 0, fn {_k, val}, acc -> (acc + val) |> rem(mod) end)
  end
end
```
