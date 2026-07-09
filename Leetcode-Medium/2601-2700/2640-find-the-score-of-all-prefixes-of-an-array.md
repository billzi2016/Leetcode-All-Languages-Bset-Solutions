# 2640. Find the Score of All Prefixes of an Array

## Cpp

```cpp
class Solution {
public:
    vector<long long> findPrefixScore(vector<int>& nums) {
        int n = nums.size();
        vector<long long> ans(n);
        long long curMax = 0;
        long long curScore = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] > curMax) curMax = nums[i];
            curScore += nums[i] + curMax;
            ans[i] = curScore;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long[] findPrefixScore(int[] nums) {
        int n = nums.length;
        long[] ans = new long[n];
        long curMax = 0;
        long total = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] > curMax) {
                curMax = nums[i];
            }
            long conv = curMax + nums[i];
            total += conv;
            ans[i] = total;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findPrefixScore(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        cur_max = 0
        total = 0
        for x in nums:
            if x > cur_max:
                cur_max = x
            conv = x + cur_max
            total += conv
            res.append(total)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = []
        cur_max = 0
        total = 0
        for x in nums:
            if x > cur_max:
                cur_max = x
            conv = x + cur_max
            total += conv
            ans.append(total)
        return ans
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* findPrefixScore(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    long long* ans = (long long*)malloc(sizeof(long long) * numsSize);
    if (!ans) return NULL;  // allocation check
    
    long long maxSoFar = 0;
    long long curScore = 0;
    
    for (int i = 0; i < numsSize; ++i) {
        if ((long long)nums[i] > maxSoFar) {
            maxSoFar = nums[i];
        }
        curScore += (long long)nums[i] + maxSoFar;
        ans[i] = curScore;
    }
    
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long[] FindPrefixScore(int[] nums) {
        int n = nums.Length;
        long[] ans = new long[n];
        long max = 0;
        long sum = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] > max) max = nums[i];
            long conv = nums[i] + max;
            sum += conv;
            ans[i] = sum;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findPrefixScore = function(nums) {
    const n = nums.length;
    const ans = new Array(n);
    let prefMax = 0;
    let total = 0;
    for (let i = 0; i < n; ++i) {
        const x = nums[i];
        if (x > prefMax) prefMax = x;
        const conv = x + prefMax;
        total += conv;
        ans[i] = total;
    }
    return ans;
};
```

## Typescript

```typescript
function findPrefixScore(nums: number[]): number[] {
    const n = nums.length;
    const ans: number[] = new Array(n);
    let curMax = 0;
    let prefixSum = 0;
    for (let i = 0; i < n; i++) {
        const x = nums[i];
        let conv: number;
        if (x > curMax) {
            curMax = x;
            conv = 2 * x;
        } else {
            conv = curMax + x;
        }
        prefixSum += conv;
        ans[i] = prefixSum;
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function findPrefixScore($nums) {
        $ans = [];
        $curMax = 0;
        $score = 0;
        foreach ($nums as $num) {
            if ($num > $curMax) {
                $curMax = $num;
            }
            $score += $num + $curMax;
            $ans[] = $score;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func findPrefixScore(_ nums: [Int]) -> [Int] {
        var result = [Int]()
        var currentMax = 0
        var total = 0
        for num in nums {
            if num > currentMax { currentMax = num }
            let conversion = currentMax + num
            total += conversion
            result.append(total)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findPrefixScore(nums: IntArray): LongArray {
        val n = nums.size
        val ans = LongArray(n)
        var curMax = 0L
        var total = 0L
        for (i in 0 until n) {
            val v = nums[i].toLong()
            if (v > curMax) curMax = v
            val conv = curMax + v
            total += conv
            ans[i] = total
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> findPrefixScore(List<int> nums) {
    int n = nums.length;
    List<int> ans = List.filled(n, 0);
    int maxSoFar = 0;
    int curSum = 0;
    for (int i = 0; i < n; i++) {
      int num = nums[i];
      if (num > maxSoFar) maxSoFar = num;
      int conver = num + maxSoFar;
      curSum += conver;
      ans[i] = curSum;
    }
    return ans;
  }
}
```

## Golang

```go
func findPrefixScore(nums []int) []int64 {
    n := len(nums)
    ans := make([]int64, n)
    var curMax int
    var total int64
    for i, v := range nums {
        if v > curMax {
            curMax = v
        }
        conv := int64(curMax) + int64(v)
        total += conv
        ans[i] = total
    }
    return ans
}
```

## Ruby

```ruby
def find_prefix_score(nums)
  res = []
  cur_max = 0
  total = 0
  nums.each do |x|
    cur_max = x if x > cur_max
    conv = cur_max + x
    total += conv
    res << total
  end
  res
end
```

## Scala

```scala
object Solution {
    def findPrefixScore(nums: Array[Int]): Array[Long] = {
        val n = nums.length
        val ans = new Array[Long](n)
        var maxSoFar = 0L
        var total = 0L
        var i = 0
        while (i < n) {
            val v = nums(i).toLong
            if (v > maxSoFar) maxSoFar = v
            val conv = maxSoFar + v
            total += conv
            ans(i) = total
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_prefix_score(nums: Vec<i32>) -> Vec<i64> {
        let mut max_val: i64 = 0;
        let mut prefix_sum: i64 = 0;
        let mut ans = Vec::with_capacity(nums.len());
        for &num in nums.iter() {
            let v = num as i64;
            if v > max_val {
                max_val = v;
            }
            let conv = v + max_val;
            prefix_sum += conv;
            ans.push(prefix_sum);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (find-prefix-score nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let loop ((rest nums) (cur-max 0) (total 0) (acc '()))
    (if (null? rest)
        (reverse acc)
        (let* ((x (car rest))
               (new-max (max cur-max x))
               (conv (+ x new-max))
               (new-total (+ total conv)))
          (loop (cdr rest) new-max new-total (cons new-total acc))))))
```

## Erlang

```erlang
-spec find_prefix_score([integer()]) -> [integer()].
find_prefix_score(Nums) ->
    find_prefix_score(Nums, 0, 0, []).

find_prefix_score([], _Max, _Score, Acc) ->
    lists:reverse(Acc);
find_prefix_score([H|T], Max, Score, Acc) ->
    NewMax = erlang:max(H, Max),
    NewScore = Score + H + NewMax,
    find_prefix_score(T, NewMax, NewScore, [NewScore | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_prefix_score(nums :: [integer]) :: [integer]
  def find_prefix_score(nums) do
    {_, _, rev_ans} =
      Enum.reduce(nums, {0, 0, []}, fn x, {cur_max, cur_sum, acc} ->
        new_max = if x > cur_max, do: x, else: cur_max
        new_sum = cur_sum + x + new_max
        {new_max, new_sum, [new_sum | acc]}
      end)

    Enum.reverse(rev_ans)
  end
end
```
