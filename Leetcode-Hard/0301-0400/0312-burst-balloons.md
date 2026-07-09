# 0312. Burst Balloons

## Cpp

```cpp
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<int> a(n + 2, 1);
        for (int i = 0; i < n; ++i) a[i + 1] = nums[i];
        int m = n + 2;
        vector<vector<int>> dp(m, vector<int>(m, 0));
        // len is the distance between i and j
        for (int len = 2; len < m; ++len) {
            for (int i = 0; i + len < m; ++i) {
                int j = i + len;
                int best = 0;
                for (int k = i + 1; k < j; ++k) {
                    int cur = dp[i][k] + dp[k][j] + a[i] * a[k] * a[j];
                    if (cur > best) best = cur;
                }
                dp[i][j] = best;
            }
        }
        return dp[0][m - 1];
    }
};
```

## Java

```java
class Solution {
    public int maxCoins(int[] nums) {
        int n = nums.length;
        int m = n + 2;
        int[] arr = new int[m];
        arr[0] = 1;
        arr[m - 1] = 1;
        System.arraycopy(nums, 0, arr, 1, n);
        
        int[][] dp = new int[m][m];
        
        for (int len = 2; len < m; ++len) { // length of interval [i, j]
            for (int i = 0; i + len < m; ++i) {
                int j = i + len;
                int best = 0;
                for (int k = i + 1; k < j; ++k) {
                    int coins = dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j];
                    if (coins > best) {
                        best = coins;
                    }
                }
                dp[i][j] = best;
            }
        }
        
        return dp[0][m - 1];
    }
}
```

## Python

```python
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Pad the original list with 1 on both sides
        n = len(nums)
        extended = [1] + nums + [1]
        m = n + 2

        # dp[i][j] will hold the max coins obtainable from interval (i, j)
        dp = [[0] * m for _ in range(m)]

        # length is the distance between i and j
        for length in range(2, m):  # minimum gap is 2 (i,i+1) which means no balloon inside
            for left in range(0, m - length):
                right = left + length
                # iterate over possible last burst balloon k in (left, right)
                max_val = 0
                for k in range(left + 1, right):
                    val = dp[left][k] + dp[k][right] + extended[left] * extended[k] * extended[right]
                    if val > max_val:
                        max_val = val
                dp[left][right] = max_val

        return dp[0][m - 1]
```

## Python3

```python
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad the list with 1 on both sides
        n = len(nums)
        arr = [1] + nums + [1]
        m = n + 2
        dp = [[0] * m for _ in range(m)]

        # length is the distance between i and j
        for length in range(2, m):
            for left in range(0, m - length):
                right = left + length
                best = 0
                # k is the last balloon to burst in (left, right)
                for k in range(left + 1, right):
                    coins = dp[left][k] + dp[k][right] + arr[left] * arr[k] * arr[right]
                    if coins > best:
                        best = coins
                dp[left][right] = best

        return dp[0][m - 1]
```

## C

```c
#include <stdlib.h>

int maxCoins(int* nums, int numsSize) {
    int m = numsSize + 2;
    int *arr = (int*)malloc(m * sizeof(int));
    if (!arr) return 0;
    arr[0] = 1;
    arr[m - 1] = 1;
    for (int i = 0; i < numsSize; ++i) {
        arr[i + 1] = nums[i];
    }

    int **dp = (int**)malloc(m * sizeof(int*));
    if (!dp) {
        free(arr);
        return 0;
    }
    for (int i = 0; i < m; ++i) {
        dp[i] = (int*)calloc(m, sizeof(int));
        if (!dp[i]) {
            for (int k = 0; k < i; ++k) free(dp[k]);
            free(dp);
            free(arr);
            return 0;
        }
    }

    for (int len = 2; len < m; ++len) {          // distance between i and j
        for (int i = 0; i + len < m; ++i) {
            int j = i + len;
            int best = 0;
            for (int k = i + 1; k < j; ++k) {
                int val = dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j];
                if (val > best) best = val;
            }
            dp[i][j] = best;
        }
    }

    int result = dp[0][m - 1];

    for (int i = 0; i < m; ++i) free(dp[i]);
    free(dp);
    free(arr);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxCoins(int[] nums)
    {
        int n = nums.Length;
        int m = n + 2;
        int[] extended = new int[m];
        extended[0] = 1;
        extended[m - 1] = 1;
        for (int i = 0; i < n; i++)
            extended[i + 1] = nums[i];

        int[,] dp = new int[m, m];

        // length is the distance between i and j
        for (int len = 2; len < m; len++) // at least one balloon inside
        {
            for (int i = 0; i + len < m; i++)
            {
                int j = i + len;
                int best = 0;
                for (int k = i + 1; k < j; k++)
                {
                    int coins = dp[i, k] + dp[k, j] + extended[i] * extended[k] * extended[j];
                    if (coins > best) best = coins;
                }
                dp[i, j] = best;
            }
        }

        return dp[0, m - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxCoins = function(nums) {
    const n = nums.length;
    // Pad with 1 on both sides
    const arr = new Array(n + 2);
    arr[0] = 1;
    for (let i = 0; i < n; ++i) arr[i + 1] = nums[i];
    arr[n + 1] = 1;
    const m = n + 2;

    // dp[i][j]: max coins from bursting balloons in (i, j)
    const dp = Array.from({ length: m }, () => new Array(m).fill(0));

    // len is the distance between i and j
    for (let len = 2; len < m; ++len) {
        for (let left = 0; left + len < m; ++left) {
            const right = left + len;
            let best = 0;
            for (let k = left + 1; k < right; ++k) {
                const coins = dp[left][k] + dp[k][right] + arr[left] * arr[k] * arr[right];
                if (coins > best) best = coins;
            }
            dp[left][right] = best;
        }
    }

    return dp[0][m - 1];
};
```

## Typescript

```typescript
function maxCoins(nums: number[]): number {
    const n = nums.length;
    const arr = new Array<number>(n + 2);
    arr[0] = 1;
    for (let i = 0; i < n; i++) {
        arr[i + 1] = nums[i];
    }
    arr[n + 1] = 1;

    const m = n + 2;
    const dp: number[][] = Array.from({ length: m }, () => new Array<number>(m).fill(0));

    for (let len = 2; len < m; len++) {
        for (let i = 0; i + len < m; i++) {
            const j = i + len;
            let best = 0;
            for (let k = i + 1; k < j; k++) {
                const coins = dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j];
                if (coins > best) best = coins;
            }
            dp[i][j] = best;
        }
    }

    return dp[0][m - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxCoins($nums) {
        // Add virtual balloons with value 1 at both ends
        array_unshift($nums, 1);
        $nums[] = 1;
        $n = count($nums);
        
        // dp[i][j] will hold the maximum coins obtainable from (i, j)
        $dp = array_fill(0, $n, array_fill(0, $n, 0));
        
        // length is the distance between i and j
        for ($len = 2; $len < $n; $len++) {
            for ($left = 0; $left + $len < $n; $left++) {
                $right = $left + $len;
                $best = 0;
                // try bursting each balloon k between left and right last
                for ($k = $left + 1; $k < $right; $k++) {
                    $coins = $dp[$left][$k] + $dp[$k][$right] + $nums[$left] * $nums[$k] * $nums[$right];
                    if ($coins > $best) {
                        $best = $coins;
                    }
                }
                $dp[$left][$right] = $best;
            }
        }
        
        return $dp[0][$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func maxCoins(_ nums: [Int]) -> Int {
        let n = nums.count
        var padded = [Int](repeating: 1, count: n + 2)
        for i in 0..<n {
            padded[i + 1] = nums[i]
        }
        let m = n + 2
        var dp = Array(repeating: Array(repeating: 0, count: m), count: m)
        
        if n == 0 { return 0 }
        
        // length is the distance between left and right indices
        for length in 2...(m - 1) {
            for left in 0..<(m - length) {
                let right = left + length
                var best = 0
                for k in (left + 1)..<right {
                    let coins = dp[left][k] + dp[k][right] + padded[left] * padded[k] * padded[right]
                    if coins > best {
                        best = coins
                    }
                }
                dp[left][right] = best
            }
        }
        
        return dp[0][m - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxCoins(nums: IntArray): Int {
        val n = nums.size
        val arr = IntArray(n + 2)
        arr[0] = 1
        arr[n + 1] = 1
        for (i in 0 until n) {
            arr[i + 1] = nums[i]
        }
        val m = n + 2
        val dp = Array(m) { IntArray(m) }
        for (len in 2..m) {
            var left = 0
            while (left + len < m + 1) {
                val right = left + len
                if (right >= m) break
                var best = 0
                var k = left + 1
                while (k < right) {
                    val coins = arr[left] * arr[k] * arr[right] + dp[left][k] + dp[k][right]
                    if (coins > best) best = coins
                    k++
                }
                dp[left][right] = best
                left++
            }
        }
        return dp[0][m - 1]
    }
}
```

## Dart

```dart
class Solution {
  int maxCoins(List<int> nums) {
    int n = nums.length;
    // Create new array with virtual balloons of value 1 at both ends
    List<int> arr = List.filled(n + 2, 1);
    for (int i = 0; i < n; ++i) {
      arr[i + 1] = nums[i];
    }
    int m = n + 2;
    // dp[left][right] stores max coins obtainable by bursting balloons exclusively between left and right
    List<List<int>> dp = List.generate(m, (_) => List.filled(m, 0));

    // length is the distance between left and right indices
    for (int len = 2; len < m; ++len) {
      for (int left = 0; left + len < m; ++left) {
        int right = left + len;
        int best = 0;
        for (int k = left + 1; k < right; ++k) {
          int coins = arr[left] * arr[k] * arr[right] + dp[left][k] + dp[k][right];
          if (coins > best) best = coins;
        }
        dp[left][right] = best;
      }
    }

    return dp[0][m - 1];
  }
}
```

## Golang

```go
func maxCoins(nums []int) int {
	n := len(nums)
	// Pad the array with 1 on both sides.
	arr := make([]int, n+2)
	arr[0] = 1
	arr[n+1] = 1
	copy(arr[1:], nums)

	m := n + 2
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, m)
	}

	// length is the distance between left and right indices.
	for length := 2; length < m; length++ {
		for left := 0; left+length < m; left++ {
			right := left + length
			best := 0
			for k := left + 1; k < right; k++ {
				val := dp[left][k] + dp[k][right] + arr[left]*arr[k]*arr[right]
				if val > best {
					best = val
				}
			}
			dp[left][right] = best
		}
	}

	return dp[0][m-1]
}
```

## Ruby

```ruby
def max_coins(nums)
  n = nums.length
  a = [1] + nums + [1]
  m = n + 2
  dp = Array.new(m) { Array.new(m, 0) }

  len = 2
  while len < m
    left = 0
    while left + len < m
      right = left + len
      max_val = 0
      k = left + 1
      while k < right
        val = dp[left][k] + a[left] * a[k] * a[right] + dp[k][right]
        max_val = val if val > max_val
        k += 1
      end
      dp[left][right] = max_val
      left += 1
    end
    len += 1
  end

  dp[0][m - 1]
end
```

## Scala

```scala
object Solution {
    def maxCoins(nums: Array[Int]): Int = {
        val n = nums.length
        val arr = new Array[Int](n + 2)
        arr(0) = 1
        arr(n + 1) = 1
        var i = 0
        while (i < n) {
            arr(i + 1) = nums(i)
            i += 1
        }
        val dp = Array.ofDim[Int](n + 2, n + 2)

        var length = 2
        while (length <= n + 2) {
            var left = 0
            while (left + length <= n + 2) {
                val right = left + length
                var maxVal = 0
                var k = left + 1
                while (k < right) {
                    val coins = arr(left) * arr(k) * arr(right) + dp(left)(k) + dp(k)(right)
                    if (coins > maxVal) maxVal = coins
                    k += 1
                }
                dp(left)(right) = maxVal
                left += 1
            }
            length += 1
        }

        dp(0)(n + 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_coins(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut arr: Vec<i64> = Vec::with_capacity(n + 2);
        arr.push(1);
        for &x in &nums {
            arr.push(x as i64);
        }
        arr.push(1);
        let m = arr.len();
        let mut dp = vec![vec![0i64; m]; m];
        for len in 2..m {
            for i in 0..=m - len - 1 {
                let j = i + len;
                let mut best = 0i64;
                for k in i + 1..j {
                    let val = dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j];
                    if val > best {
                        best = val;
                    }
                }
                dp[i][j] = best;
            }
        }
        dp[0][m - 1] as i32
    }
}
```

## Racket

```racket
(define/contract (max-coins nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [arr (list->vector (append (list 1) nums (list 1)))]
         [m (+ n 2)])
    (define dp (make-vector m))
    (for ([i (in-range m)]) (vector-set! dp i (make-vector m 0)))
    (for ([len (in-range 2 (add1 m))])               ; interval length
      (for ([i (in-range (- m len))])
        (let* ([j (+ i len)]
               [inner-i (vector-ref dp i)])
          (let ([best 0])
            (for ([k (in-range (+ i 1) j)])
              (let* ([left (vector-ref (vector-ref dp i) k)]
                     [right (vector-ref (vector-ref dp k) j)]
                     [gain (* (vector-ref arr i)
                              (vector-ref arr k)
                              (vector-ref arr j))]
                     [total (+ left gain right)])
                (when (> total best) (set! best total))))
            (vector-set! inner-i j best)))))
    (vector-ref (vector-ref dp 0) (- m 1))))
```

## Erlang

```erlang
-module(solution).
-export([max_coins/1]).

-spec max_coins(Nums :: [integer()]) -> integer().
max_coins(Nums) ->
    ExtList = [1] ++ Nums ++ [1],
    ExtT = list_to_tuple(ExtList),
    LastIdx = length(ExtList) - 1,
    {Result, _} = max_interval(0, LastIdx, ExtT, #{}),
    Result.

max_interval(L, R, _ExtT, Memo) when L + 1 >= R ->
    {0, Memo};
max_interval(L, R, ExtT, Memo) ->
    case maps:get({L, R}, Memo, undefined) of
        Value when is_integer(Value) -> {Value, Memo};
        _ ->
            {MaxVal, NewMemo} = max_k(L, R, ExtT, L + 1, 0, Memo),
            UpdatedMemo = maps:put({L, R}, MaxVal, NewMemo),
            {MaxVal, UpdatedMemo}
    end.

max_k(_L, _R, _ExtT, K, CurrentMax, Memo) when K >= _R ->
    {CurrentMax, Memo};
max_k(L, R, ExtT, K, CurrentMax, Memo) ->
    {LeftVal, Memo1} = max_interval(L, K, ExtT, Memo),
    {RightVal, Memo2} = max_interval(K, R, ExtT, Memo1),
    Coin = LeftVal + RightVal +
        element(L + 1, ExtT) * element(K + 1, ExtT) * element(R + 1, ExtT),
    NewMax = if Coin > CurrentMax -> Coin; true -> CurrentMax end,
    max_k(L, R, ExtT, K + 1, NewMax, Memo2).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_coins(nums :: [integer]) :: integer
  def max_coins(nums) do
    arr = :array.from_list([1] ++ nums ++ [1])
    n = :array.size(arr)

    table = :ets.new(:dp, [:set, :private])

    for len <- 2..(n - 1) do
      for i <- 0..(n - len - 1) do
        j = i + len

        max =
          Enum.reduce((i + 1)..(j - 1), 0, fn k, acc ->
            left =
              case :ets.lookup(table, {i, k}) do
                [{_, v}] -> v
                [] -> 0
              end

            right =
              case :ets.lookup(table, {k, j}) do
                [{_, v}] -> v
                [] -> 0
              end

            total = left + right + :array.get(i, arr) * :array.get(k, arr) * :array.get(j, arr)
            if total > acc, do: total, else: acc
          end)

        :ets.insert(table, {{i, j}, max})
      end
    end

    result =
      case :ets.lookup(table, {0, n - 1}) do
        [{_, v}] -> v
        [] -> 0
      end

    :ets.delete(table)
    result
  end
end
```
