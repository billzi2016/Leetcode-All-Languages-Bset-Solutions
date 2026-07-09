# 0213. House Robber II

## Cpp

```cpp
class Solution {
public:
    int robLinear(const vector<int>& nums, int start, int end) {
        int prev = 0, curr = 0;
        for (int i = start; i <= end; ++i) {
            int temp = max(prev + nums[i], curr);
            prev = curr;
            curr = temp;
        }
        return curr;
    }
    
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];
        int money1 = robLinear(nums, 0, n - 2);
        int money2 = robLinear(nums, 1, n - 1);
        return max(money1, money2);
    }
};
```

## Java

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        return Math.max(robRange(nums, 0, n - 2), robRange(nums, 1, n - 1));
    }
    
    private int robRange(int[] nums, int start, int end) {
        int prev = 0, curr = 0;
        for (int i = start; i <= end; i++) {
            int temp = Math.max(curr, prev + nums[i]);
            prev = curr;
            curr = temp;
        }
        return curr;
    }
}
```

## Python

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def rob_linear(arr):
            prev, curr = 0, 0
            for x in arr:
                prev, curr = curr, max(curr, prev + x)
            return curr

        # Exclude last house or exclude first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
```

## Python3

```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def rob_linear(arr: List[int]) -> int:
            prev, curr = 0, 0
            for amount in arr:
                prev, curr = curr, max(curr, prev + amount)
            return curr

        # Exclude last house or exclude first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
```

## C

```c
#include <stddef.h>

static int robLinear(int* nums, int start, int end) {
    int prev2 = 0; // dp[i-2]
    int prev1 = 0; // dp[i-1]
    for (int i = start; i <= end; ++i) {
        int cur = (prev2 + nums[i] > prev1) ? prev2 + nums[i] : prev1;
        prev2 = prev1;
        prev1 = cur;
    }
    return prev1;
}

int rob(int* nums, int numsSize){
    if (numsSize == 0) return 0;
    if (numsSize == 1) return nums[0];
    int ans1 = robLinear(nums, 0, numsSize - 2);
    int ans2 = robLinear(nums, 1, numsSize - 1);
    return ans1 > ans2 ? ans1 : ans2;
}
```

## Csharp

```csharp
public class Solution
{
    public int Rob(int[] nums)
    {
        int n = nums.Length;
        if (n == 1) return nums[0];
        // Compute max for two scenarios: exclude last house, or exclude first house
        int moneyExcludeLast = RobLinear(nums, 0, n - 2);
        int moneyExcludeFirst = RobLinear(nums, 1, n - 1);
        return Math.Max(moneyExcludeLast, moneyExcludeFirst);
    }

    private int RobLinear(int[] nums, int start, int end)
    {
        int prevTwo = 0; // dp[i-2]
        int prevOne = 0; // dp[i-1]
        for (int i = start; i <= end; i++)
        {
            int cur = Math.Max(prevOne, prevTwo + nums[i]);
            prevTwo = prevOne;
            prevOne = cur;
        }
        return prevOne;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    const n = nums.length;
    if (n === 0) return 0;
    if (n === 1) return nums[0];
    
    const robLinear = (start, end) => {
        let prev = 0, curr = 0;
        for (let i = start; i <= end; i++) {
            const temp = Math.max(curr, prev + nums[i]);
            prev = curr;
            curr = temp;
        }
        return curr;
    };
    
    // Exclude last house or exclude first house
    return Math.max(robLinear(0, n - 2), robLinear(1, n - 1));
};
```

## Typescript

```typescript
function rob(nums: number[]): number {
    const n = nums.length;
    if (n === 0) return 0;
    if (n === 1) return nums[0];

    const robLinear = (start: number, end: number): number => {
        let prev2 = 0; // dp[i-2]
        let prev1 = 0; // dp[i-1]
        for (let i = start; i <= end; i++) {
            const cur = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    };

    const money1 = robLinear(0, n - 2);
    const money2 = robLinear(1, n - 1);
    return Math.max(money1, money2);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function rob($nums) {
        $n = count($nums);
        if ($n == 0) return 0;
        if ($n == 1) return $nums[0];
        $max1 = $this->robLinear($nums, 0, $n - 2);
        $max2 = $this->robLinear($nums, 1, $n - 1);
        return max($max1, $max2);
    }

    private function robLinear($nums, $start, $end) {
        $prev1 = 0;
        $prev2 = 0;
        for ($i = $start; $i <= $end; $i++) {
            $curr = max($prev1, $prev2 + $nums[$i]);
            $prev2 = $prev1;
            $prev1 = $curr;
        }
        return $prev1;
    }
}
```

## Swift

```swift
class Solution {
    func rob(_ nums: [Int]) -> Int {
        let n = nums.count
        if n == 0 { return 0 }
        if n == 1 { return nums[0] }
        
        func robLinear(_ arr: [Int]) -> Int {
            var prev = 0
            var curr = 0
            for v in arr {
                let newCurr = max(curr, prev + v)
                prev = curr
                curr = newCurr
            }
            return curr
        }
        
        let case1 = robLinear(Array(nums[0..<(n-1)]))
        let case2 = robLinear(Array(nums[1..<n]))
        return max(case1, case2)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rob(nums: IntArray): Int {
        val n = nums.size
        if (n == 1) return nums[0]
        // Helper lambda for linear robbery on subarray [start, end] inclusive
        fun robLinear(start: Int, end: Int): Int {
            var prev = 0
            var curr = 0
            for (i in start..end) {
                val temp = kotlin.math.max(curr, prev + nums[i])
                prev = curr
                curr = temp
            }
            return curr
        }
        // Exclude last house or first house
        val excludeLast = robLinear(0, n - 2)
        val excludeFirst = robLinear(1, n - 1)
        return kotlin.math.max(excludeLast, excludeFirst)
    }
}
```

## Dart

```dart
class Solution {
  int rob(List<int> nums) {
    int n = nums.length;
    if (n == 1) return nums[0];
    int _robLinear(int start, int end) {
      int prev = 0, curr = 0;
      for (int i = start; i <= end; ++i) {
        int temp = curr;
        int take = prev + nums[i];
        curr = take > curr ? take : curr;
        prev = temp;
      }
      return curr;
    }

    int ans1 = _robLinear(0, n - 2);
    int ans2 = _robLinear(1, n - 1);
    return ans1 > ans2 ? ans1 : ans2;
  }
}
```

## Golang

```go
func rob(nums []int) int {
    n := len(nums)
    if n == 0 {
        return 0
    }
    if n == 1 {
        return nums[0]
    }
    ans1 := robLinear(nums, 0, n-2)
    ans2 := robLinear(nums, 1, n-1)
    if ans1 > ans2 {
        return ans1
    }
    return ans2
}

func robLinear(nums []int, start, end int) int {
    prev2, prev1 := 0, 0
    for i := start; i <= end; i++ {
        cur := max(prev1, prev2+nums[i])
        prev2 = prev1
        prev1 = cur
    }
    return prev1
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

## Ruby

```ruby
def linear_rob(arr)
  prev = 0
  curr = 0
  arr.each do |v|
    temp = [curr, prev + v].max
    prev = curr
    curr = temp
  end
  curr
end

def rob(nums)
  n = nums.length
  return 0 if n == 0
  return nums[0] if n == 1
  [linear_rob(nums[0...-1]), linear_rob(nums[1..-1])].max
end
```

## Scala

```scala
object Solution {
    def rob(nums: Array[Int]): Int = {
        val n = nums.length
        if (n == 0) return 0
        if (n == 1) return nums(0)

        def robLinear(start: Int, end: Int): Int = {
            var prevInclude = 0 // dp[i-2] + current
            var prevExclude = 0 // dp[i-1]
            var i = start
            while (i <= end) {
                val cur = Math.max(prevInclude + nums(i), prevExclude)
                prevInclude = prevExclude
                prevExclude = cur
                i += 1
            }
            prevExclude
        }

        Math.max(robLinear(0, n - 2), robLinear(1, n - 1))
    }
}
```

## Rust

```rust
impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        if n == 1 {
            return nums[0];
        }
        let max1 = Self::rob_linear(&nums[..n - 1]);
        let max2 = Self::rob_linear(&nums[1..]);
        std::cmp::max(max1, max2)
    }

    fn rob_linear(nums: &[i32]) -> i32 {
        let mut prev = 0;
        let mut curr = 0;
        for &x in nums {
            let new_curr = std::cmp::max(curr, prev + x);
            prev = curr;
            curr = new_curr;
        }
        curr
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(define (rob-linear lst)
  (let loop ((lst lst) (prev1 0) (prev2 0))
    (if (null? lst)
        prev1
        (let* ((x (car lst))
               (new (max prev1 (+ prev2 x))))
          (loop (cdr lst) new prev1)))))

(define/contract (rob nums)
  (-> (listof exact-integer?) exact-integer?)
  (cond
    [(null? nums) 0]
    [(null? (cdr nums)) (car nums)]
    [else
     (let* ((n (length nums))
            (exclude-last (take nums (- n 1)))   ; houses 0..n-2
            (exclude-first (drop nums 1)))      ; houses 1..n-1
       (max (rob-linear exclude-last)
            (rob-linear exclude-first)))]))
```

## Erlang

```erlang
-module(solution).
-export([rob/1]).

-spec rob(Nums :: [integer()]) -> integer().
rob([]) ->
    0;
rob([X]) ->
    X;
rob([A, B]) ->
    erlang:max(A, B);
rob(Nums) ->
    N = length(Nums),
    % Case 1: houses 1..N-1 (exclude last)
    FirstCase = max_rob(lists:sublist(Nums, N - 1)),
    % Case 2: houses 2..N (exclude first)
    SecondCase = max_rob(tl(Nums)),
    erlang:max(FirstCase, SecondCase).

% Helper for linear house robber problem
-spec max_rob([integer()]) -> integer().
max_rob(List) ->
    {_, Max} = lists:foldl(
        fun(X, {Prev2, Prev1}) ->
            Cur = erlang:max(Prev1, Prev2 + X),
            {Prev1, Cur}
        end,
        {0, 0},
        List
    ),
    Max.
```

## Elixir

```elixir
defmodule Solution do
  @spec rob(nums :: [integer]) :: integer
  def rob(nums) do
    case nums do
      [] -> 0
      [x] -> x
      _ ->
        n = length(nums)
        list1 = Enum.slice(nums, 0, n - 1)
        list2 = Enum.slice(nums, 1, n - 1)
        max(rob_linear(list1), rob_linear(list2))
    end
  end

  defp rob_linear([]), do: 0
  defp rob_linear([x]), do: x

  defp rob_linear([first | rest]) do
    {prev2, prev1} = Enum.reduce(rest, {0, first}, fn cur, {a, b} ->
      new = max(b, a + cur)
      {b, new}
    end)

    prev1
  end
end
```
