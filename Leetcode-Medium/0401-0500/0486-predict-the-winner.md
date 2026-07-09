# 0486. Predict the Winner

## Cpp

```cpp
class Solution {
public:
    bool predictTheWinner(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = 0; i < n; ++i) dp[i][i] = nums[i];
        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i + len - 1 < n; ++i) {
                int j = i + len - 1;
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
            }
        }
        return dp[0][n - 1] >= 0;
    }
};
```

## Java

```java
class Solution {
    public boolean predictTheWinner(int[] nums) {
        int n = nums.length;
        Integer[][] memo = new Integer[n][n];
        return dfs(nums, 0, n - 1, memo) >= 0;
    }
    
    private int dfs(int[] nums, int i, int j, Integer[][] memo) {
        if (i == j) {
            return nums[i];
        }
        if (memo[i][j] != null) {
            return memo[i][j];
        }
        int pickLeft = nums[i] - dfs(nums, i + 1, j, memo);
        int pickRight = nums[j] - dfs(nums, i, j - 1, memo);
        int best = Math.max(pickLeft, pickRight);
        memo[i][j] = best;
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return nums[i]
            # choose left or right, subtract opponent's best response
            take_left = nums[i] - dp(i + 1, j)
            take_right = nums[j] - dp(i, j - 1)
            return max(take_left, take_right)

        return dp(0, len(nums) - 1) >= 0
```

## Python3

```python
from typing import List
from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            pick_left = nums[i] - dfs(i + 1, j)
            pick_right = nums[j] - dfs(i, j - 1)
            return max(pick_left, pick_right)

        return dfs(0, len(nums) - 1) >= 0
```

## C

```c
#include <stdbool.h>
#include <limits.h>

static int *g_nums;
static int g_n;
static int memo[20][20];

static int dfs(int i, int j) {
    if (i == j) return g_nums[i];
    if (memo[i][j] != INT_MIN) return memo[i][j];
    int pickLeft = g_nums[i] - dfs(i + 1, j);
    int pickRight = g_nums[j] - dfs(i, j - 1);
    int best = pickLeft > pickRight ? pickLeft : pickRight;
    memo[i][j] = best;
    return best;
}

bool predictTheWinner(int* nums, int numsSize) {
    g_nums = nums;
    g_n = numsSize;
    for (int i = 0; i < numsSize; ++i)
        for (int j = 0; j < numsSize; ++j)
            memo[i][j] = INT_MIN;
    int diff = dfs(0, numsSize - 1);
    return diff >= 0;
}
```

## Csharp

```csharp
public class Solution {
    public bool PredictTheWinner(int[] nums) {
        int n = nums.Length;
        int[,] dp = new int[n, n];
        for (int i = 0; i < n; i++) {
            dp[i, i] = nums[i];
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                dp[i, j] = Math.Max(nums[i] - dp[i + 1, j], nums[j] - dp[i, j - 1]);
            }
        }
        return dp[0, n - 1] >= 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var predictTheWinner = function(nums) {
    const n = nums.length;
    const dp = Array.from({ length: n }, () => Array(n).fill(0));
    
    for (let i = 0; i < n; i++) {
        dp[i][i] = nums[i];
    }
    
    for (let len = 2; len <= n; len++) {
        for (let i = 0; i + len - 1 < n; i++) {
            const j = i + len - 1;
            dp[i][j] = Math.max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
        }
    }
    
    return dp[0][n - 1] >= 0;
};
```

## Typescript

```typescript
function predictTheWinner(nums: number[]): boolean {
    const n = nums.length;
    const dp: number[][] = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < n; i++) {
        dp[i][i] = nums[i];
    }
    for (let len = 2; len <= n; len++) {
        for (let i = 0; i + len - 1 < n; i++) {
            const j = i + len - 1;
            dp[i][j] = Math.max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
        }
    }
    return dp[0][n - 1] >= 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function predictTheWinner($nums) {
        $n = count($nums);
        $memo = [];

        $dfs = function($i, $j) use (&$dfs, &$nums, &$memo) {
            if ($i == $j) {
                return $nums[$i];
            }
            $key = $i . ',' . $j;
            if (isset($memo[$key])) {
                return $memo[$key];
            }
            $pickLeft  = $nums[$i] - $dfs($i + 1, $j);
            $pickRight = $nums[$j] - $dfs($i, $j - 1);
            $res = max($pickLeft, $pickRight);
            $memo[$key] = $res;
            return $res;
        };

        $diff = $dfs(0, $n - 1);
        return $diff >= 0;
    }
}
```

## Swift

```swift
class Solution {
    func predictTheWinner(_ nums: [Int]) -> Bool {
        let n = nums.count
        var memo = Array(repeating: Array(repeating: Int.min, count: n), count: n)
        
        func dfs(_ i: Int, _ j: Int) -> Int {
            if i == j { return nums[i] }
            if memo[i][j] != Int.min { return memo[i][j] }
            let pickLeft = nums[i] - dfs(i + 1, j)
            let pickRight = nums[j] - dfs(i, j - 1)
            let best = max(pickLeft, pickRight)
            memo[i][j] = best
            return best
        }
        
        return dfs(0, n - 1) >= 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun predictTheWinner(nums: IntArray): Boolean {
        val n = nums.size
        val dp = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            dp[i][i] = nums[i]
        }
        for (len in 2..n) {
            var i = 0
            while (i + len - 1 < n) {
                val j = i + len - 1
                dp[i][j] = maxOf(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
                i++
            }
        }
        return dp[0][n - 1] >= 0
    }
}
```

## Dart

```dart
class Solution {
  bool predictTheWinner(List<int> nums) {
    int n = nums.length;
    List<List<int>> dp = List.generate(n, (_) => List.filled(n, 0));
    for (int i = 0; i < n; i++) {
      dp[i][i] = nums[i];
    }
    for (int len = 2; len <= n; len++) {
      for (int i = 0; i + len - 1 < n; i++) {
        int j = i + len - 1;
        int pickLeft = nums[i] - dp[i + 1][j];
        int pickRight = nums[j] - dp[i][j - 1];
        dp[i][j] = pickLeft > pickRight ? pickLeft : pickRight;
      }
    }
    return dp[0][n - 1] >= 0;
  }
}
```

## Golang

```go
func predictTheWinner(nums []int) bool {
    n := len(nums)
    memo := make([][]int, n)
    seen := make([][]bool, n)
    for i := 0; i < n; i++ {
        memo[i] = make([]int, n)
        seen[i] = make([]bool, n)
    }
    var dfs func(int, int) int
    dfs = func(i, j int) int {
        if i == j {
            return nums[i]
        }
        if seen[i][j] {
            return memo[i][j]
        }
        left := nums[i] - dfs(i+1, j)
        right := nums[j] - dfs(i, j-1)
        if left > right {
            memo[i][j] = left
        } else {
            memo[i][j] = right
        }
        seen[i][j] = true
        return memo[i][j]
    }
    return dfs(0, n-1) >= 0
}
```

## Ruby

```ruby
def predict_the_winner(nums)
  memo = {}
  dfs = nil
  dfs = ->(l, r) {
    return 0 if l > r
    key = [l, r]
    return memo[key] if memo.key?(key)
    left = nums[l] - dfs.call(l + 1, r)
    right = nums[r] - dfs.call(l, r - 1)
    memo[key] = left > right ? left : right
  }
  dfs.call(0, nums.length - 1) >= 0
end
```

## Scala

```scala
object Solution {
    def predictTheWinner(nums: Array[Int]): Boolean = {
        val n = nums.length
        if (n == 0) return true
        val dp = Array.ofDim[Int](n, n)
        for (i <- 0 until n) dp(i)(i) = nums(i)

        for (len <- 2 to n) {
            var i = 0
            while (i <= n - len) {
                val j = i + len - 1
                val pickLeft = nums(i) - dp(i + 1)(j)
                val pickRight = nums(j) - dp(i)(j - 1)
                dp(i)(j) = if (pickLeft > pickRight) pickLeft else pickRight
                i += 1
            }
        }

        dp(0)(n - 1) >= 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn predict_the_winner(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut dp = vec![vec![0i32; n]; n];
        for i in 0..n {
            dp[i][i] = nums[i];
        }
        for len in 2..=n {
            for i in 0..=n - len {
                let j = i + len - 1;
                dp[i][j] = std::cmp::max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
            }
        }
        dp[0][n - 1] >= 0
    }
}
```

## Racket

```racket
(define/contract (predict-the-winner nums)
  (-> (listof exact-integer?) boolean?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         (memo (make-vector n)))
    (for ([i n])
      (vector-set! memo i (make-vector n #f)))
    (define (dp i j)
      (if (= i j)
          (vector-ref arr i)
          (let ((cached (vector-ref (vector-ref memo i) j)))
            (if cached
                cached
                (let* ((left (- (vector-ref arr i) (dp (add1 i) j)))
                       (right (- (vector-ref arr j) (dp i (sub1 j))))
                       (best (max left right)))
                  (vector-set! (vector-ref memo i) j best)
                  best)))))
    (>= (dp 0 (sub1 n)) 0)))
```

## Erlang

```erlang
-module(solution).
-export([predict_the_winner/1]).

-spec predict_the_winner(Nums :: [integer()]) -> boolean().
predict_the_winner(Nums) ->
    Len = length(Nums),
    Arr = list_to_tuple(Nums),
    {Diff, _} = diff(0, Len - 1, Arr, #{}),
    Diff >= 0.

diff(I, J, _Arr, Memo) when I > J ->
    {0, Memo};
diff(I, J, Arr, Memo) ->
    case maps:get({I, J}, Memo, undefined) of
        Value when is_integer(Value) ->
            {Value, Memo};
        _ ->
            {LeftDiff, Memo1} = diff(I + 1, J, Arr, Memo),
            {RightDiff, Memo2} = diff(I, J - 1, Arr, Memo1),
            NumI = element(I + 1, Arr),
            NumJ = element(J + 1, Arr),
            TakeLeft = NumI - LeftDiff,
            TakeRight = NumJ - RightDiff,
            Best = erlang:max(TakeLeft, TakeRight),
            NewMemo = maps:put({I, J}, Best, Memo2),
            {Best, NewMemo}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec predict_the_winner(nums :: [integer]) :: boolean
  def predict_the_winner(nums) do
    {diff, _} = dfs(nums, 0, length(nums) - 1, %{})
    diff >= 0
  end

  defp dfs(_nums, i, j, memo) when i > j do
    {0, memo}
  end

  defp dfs(nums, i, j, memo) do
    case Map.fetch(memo, {i, j}) do
      {:ok, val} ->
        {val, memo}

      :error ->
        if i == j do
          val = Enum.at(nums, i)
          {val, Map.put(memo, {i, j}, val)}
        else
          {left_next, memo1} = dfs(nums, i + 1, j, memo)
          left_score = Enum.at(nums, i) - left_next

          {right_next, memo2} = dfs(nums, i, j - 1, memo1)
          right_score = Enum.at(nums, j) - right_next

          best = max(left_score, right_score)
          {best, Map.put(memo2, {i, j}, best)}
        end
    end
  end
end
```
