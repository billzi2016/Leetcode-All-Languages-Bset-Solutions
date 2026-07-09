# 2567. Minimum Score by Changing Two Elements

## Cpp

```cpp
class Solution {
public:
    int minimizeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        // After changing two elements, we can effectively remove any two extremes.
        // Consider three scenarios: remove first two, last two, or one from each end.
        long long ans1 = (long long)nums[n - 1] - nums[2];      // remove two smallest
        long long ans2 = (long long)nums[n - 3] - nums[0];      // remove two largest
        long long ans3 = (long long)nums[n - 2] - nums[1];      // remove one from each side
        long long res = min({ans1, ans2, ans3});
        return (int)res;
    }
};
```

## Java

```java
class Solution {
    public int minimizeSum(int[] nums) {
        int n = nums.length;
        java.util.Arrays.sort(nums);
        int diff1 = nums[n - 1] - nums[2];      // change two smallest
        int diff2 = nums[n - 3] - nums[0];      // change two largest
        int diff3 = nums[n - 2] - nums[1];      // change one smallest and one largest
        return Math.min(diff1, Math.min(diff2, diff3));
    }
}
```

## Python

```python
class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        # discard i smallest and (2-i) largest, for i = 0,1,2
        ans = float('inf')
        # i = 0 -> remove two largest
        ans = min(ans, nums[n - 3] - nums[0])
        # i = 1 -> remove one from each side
        ans = min(ans, nums[n - 2] - nums[1])
        # i = 2 -> remove two smallest
        ans = min(ans, nums[n - 1] - nums[2])
        return ans
```

## Python3

```python
class Solution:
    def minimizeSum(self, nums):
        nums.sort()
        n = len(nums)
        # three possible scenarios after changing two elements
        ans1 = nums[-1] - nums[2]          # change two smallest
        ans2 = nums[-2] - nums[1]          # change one smallest and one largest
        ans3 = nums[-3] - nums[0]          # change two largest
        return min(ans1, ans2, ans3)
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

int minimizeSum(int* nums, int numsSize) {
    if (numsSize <= 2) return 0; // not needed per constraints
    qsort(nums, numsSize, sizeof(int), cmp_int);
    
    int n = numsSize;
    int diff1 = nums[n - 1] - nums[1];       // change min element
    int diff2 = nums[n - 2] - nums[0];       // change max element
    int diff3 = nums[n - 2] - nums[1];       // change both extremes
    
    int ans = diff1;
    if (diff2 < ans) ans = diff2;
    if (diff3 < ans) ans = diff3;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimizeSum(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        // Remove two largest
        int diff1 = nums[n - 3] - nums[0];
        // Remove one smallest and one largest
        int diff2 = nums[n - 2] - nums[1];
        // Remove two smallest
        int diff3 = nums[n - 1] - nums[2];
        return Math.Min(diff1, Math.Min(diff2, diff3));
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimizeSum = function(nums) {
    const n = nums.length;
    if (n <= 2) return 0; // not needed per constraints but safe
    
    const sorted = nums.slice().sort((a, b) => a - b);
    let ans = Infinity;
    
    for (let i = 0; i <= 2; ++i) {
        for (let j = 0; j <= 2 - i; ++j) {
            const leftIdx = i;
            const rightIdx = n - 1 - j;
            if (leftIdx > rightIdx) continue;
            const diff = sorted[rightIdx] - sorted[leftIdx];
            if (diff < ans) ans = diff;
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function minimizeSum(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const diff1 = nums[n - 2] - nums[0];
    const diff2 = nums[n - 1] - nums[1];
    const diff3 = nums[n - 2] - nums[1];
    return Math.min(diff1, diff2, diff3);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimizeSum($nums) {
        sort($nums);
        $n = count($nums);
        // Since n >= 3, the following indices are always valid.
        $ans = $nums[$n - 3] - $nums[0];
        $ans = min($ans, $nums[$n - 2] - $nums[1]);
        $ans = min($ans, $nums[$n - 1] - $nums[2]);
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimizeSum(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        let n = sorted.count
        var answer = Int.max
        
        for leftRemoved in 0...2 {
            let rightRemoved = 2 - leftRemoved
            let i = leftRemoved
            let j = n - 1 - rightRemoved
            if i <= j {
                let diff = sorted[j] - sorted[i]
                answer = min(answer, diff)
            }
        }
        
        return answer == Int.max ? 0 : answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimizeSum(nums: IntArray): Int {
        nums.sort()
        val n = nums.size
        var ans = Int.MAX_VALUE
        for (i in 0..2) {
            val left = i
            val right = n - 1 - (2 - i)
            val diff = nums[right] - nums[left]
            if (diff < ans) ans = diff
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minimizeSum(List<int> nums) {
    nums.sort();
    int n = nums.length;
    int minVal = nums[0];
    int secondMin = nums[1];
    int maxVal = nums[n - 1];
    int secondMax = nums[n - 2];

    int option1 = maxVal - secondMin;      // change the minimum
    int option2 = secondMax - minVal;      // change the maximum
    int option3 = secondMax - secondMin;   // change both extremes

    int result = option1;
    if (option2 < result) result = option2;
    if (option3 < result) result = option3;
    return result;
  }
}
```

## Golang

```go
package main

import (
	"math"
	"sort"
)

func minimizeSum(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	ans := math.MaxInt64
	for i := 0; i <= 2; i++ {
		left := i
		right := n - 1 - (2 - i)
		if diff := nums[right] - nums[left]; diff < ans {
			ans = diff
		}
	}
	return ans
}
```

## Ruby

```ruby
def minimize_sum(nums)
  nums.sort!
  n = nums.length
  ans = Float::INFINITY

  # No changes
  ans = [ans, nums[-1] - nums[0]].min

  # Change one element (either min or max)
  if n > 1
    ans = [ans, nums[-1] - nums[1]].min   # change the smallest
    ans = [ans, nums[-2] - nums[0]].min   # change the largest
  end

  # Change two elements (both from one side or one each)
  if n > 2
    ans = [ans, nums[-1] - nums[2]].min   # change two smallest
    ans = [ans, nums[-3] - nums[0]].min   # change two largest
    ans = [ans, nums[-2] - nums[1]].min   # change one smallest and one largest
  end

  ans.to_i
end
```

## Scala

```scala
object Solution {
    def minimizeSum(nums: Array[Int]): Int = {
        val n = nums.length
        java.util.Arrays.sort(nums)
        var ans = Int.MaxValue
        for (i <- 0 to 2) {
            val diff = nums(n - 3 + i) - nums(i)
            if (diff < ans) ans = diff
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimize_sum(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        let n = nums.len();
        // According to constraints, n >= 3
        let diff1 = nums[n - 1] - nums[2];   // remove two smallest
        let diff2 = nums[n - 3] - nums[0];   // remove two largest
        let diff3 = nums[n - 2] - nums[1];   // remove one smallest and one largest
        *[diff1, diff2, diff3].iter().min().unwrap()
    }
}
```

## Racket

```racket
(define/contract (minimize-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort nums <))
         (n (length sorted))
         (first (list-ref sorted 0))
         (second (list-ref sorted 1))
         (third (list-ref sorted 2))
         (last (list-ref sorted (- n 1)))
         (second-last (list-ref sorted (- n 2)))
         (third-last (list-ref sorted (- n 3))))
    (min (- last third)          ; change two smallest
         (- third-last first)    ; change two largest
         (- second-last second)))) ; change one smallest and one largest
```

## Erlang

```erlang
-module(solution).
-export([minimize_sum/1]).

-spec minimize_sum(Nums :: [integer()]) -> integer().
minimize_sum(Nums) ->
    Sorted = lists:sort(Nums),
    T = list_to_tuple(Sorted),
    N = tuple_size(T),
    D1 = element(N, T) - element(3, T),          % remove two smallest
    D2 = element(N-2, T) - element(1, T),        % remove two largest
    D3 = element(N-1, T) - element(2, T),        % remove one smallest and one largest
    min(min(D1, D2), D3).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimize_sum(nums :: [integer]) :: integer
  def minimize_sum(nums) do
    sorted = Enum.sort(nums)
    n = length(sorted)

    diffs =
      for i <- 0..2 do
        low = i
        high = n - 1 - (2 - i)
        Enum.at(sorted, high) - Enum.at(sorted, low)
      end

    Enum.min(diffs)
  end
end
```
