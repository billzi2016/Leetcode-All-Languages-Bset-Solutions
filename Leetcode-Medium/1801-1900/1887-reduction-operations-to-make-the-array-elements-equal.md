# 1887. Reduction Operations to Make the Array Elements Equal

## Cpp

```cpp
class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        long long ans = 0;
        int up = 0;
        for (int i = 1; i < (int)nums.size(); ++i) {
            if (nums[i] != nums[i - 1]) ++up;
            ans += up;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int reductionOperations(int[] nums) {
        java.util.Arrays.sort(nums);
        int up = 0;
        int ans = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                up++;
            }
            ans += up;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        up = 0
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                up += 1
            ans += up
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        up = 0
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                up += 1
            ans += up
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int reductionOperations(int* nums, int numsSize) {
    if (numsSize <= 1) return 0;
    qsort(nums, numsSize, sizeof(int), cmp_int);
    
    int ans = 0;
    int up = 0;
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] != nums[i - 1]) {
            ++up;
        }
        ans += up;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int ReductionOperations(int[] nums)
    {
        if (nums == null || nums.Length == 0) return 0;
        Array.Sort(nums);
        long ans = 0;
        int up = 0;
        for (int i = 1; i < nums.Length; i++)
        {
            if (nums[i] != nums[i - 1]) up++;
            ans += up;
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var reductionOperations = function(nums) {
    nums.sort((a, b) => a - b);
    let up = 0;
    let ans = 0;
    for (let i = 1; i < nums.length; ++i) {
        if (nums[i] !== nums[i - 1]) up++;
        ans += up;
    }
    return ans;
};
```

## Typescript

```typescript
function reductionOperations(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let ans = 0;
    let up = 0;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[i - 1]) up++;
        ans += up;
    }
    return ans;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function reductionOperations($nums) {
        sort($nums);
        $up = 0;
        $ans = 0;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] != $nums[$i - 1]) {
                $up++;
            }
            $ans += $up;
        }
        return $ans;
    }
}
?>
```

## Swift

```swift
class Solution {
    func reductionOperations(_ nums: [Int]) -> Int {
        let sortedNums = nums.sorted()
        var ans = 0
        var up = 0
        for i in 1..<sortedNums.count {
            if sortedNums[i] != sortedNums[i - 1] {
                up += 1
            }
            ans += up
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reductionOperations(nums: IntArray): Int {
        nums.sort()
        var up = 0
        var ans = 0L
        for (i in 1 until nums.size) {
            if (nums[i] != nums[i - 1]) up++
            ans += up
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int reductionOperations(List<int> nums) {
    nums.sort();
    int up = 0;
    int ans = 0;
    for (int i = 1; i < nums.length; ++i) {
      if (nums[i] != nums[i - 1]) {
        up++;
      }
      ans += up;
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func reductionOperations(nums []int) int {
    sort.Ints(nums)
    ans, up := 0, 0
    for i := 1; i < len(nums); i++ {
        if nums[i] != nums[i-1] {
            up++
        }
        ans += up
    }
    return ans
}
```

## Ruby

```ruby
def reduction_operations(nums)
  nums.sort!
  up = 0
  ans = 0
  (1...nums.length).each do |i|
    up += 1 if nums[i] != nums[i - 1]
    ans += up
  end
  ans
end
```

## Scala

```scala
object Solution {
    def reductionOperations(nums: Array[Int]): Int = {
        val sorted = nums.sorted
        var up = 0
        var ans: Long = 0L
        for (i <- 1 until sorted.length) {
            if (sorted(i) != sorted(i - 1)) up += 1
            ans += up
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reduction_operations(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        let mut up = 0i32;
        let mut ans = 0i32;
        for i in 1..nums.len() {
            if nums[i] != nums[i - 1] {
                up += 1;
            }
            ans += up;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (reduction-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((sorted (sort nums <)))
    (if (null? sorted)
        0
        (let loop ((prev (car sorted))
                   (rest (cdr sorted))
                   (up 0)
                   (ans 0))
          (if (null? rest)
              ans
              (let* ((curr (car rest))
                     (new-up (if (= curr prev) up (+ up 1))))
                (loop curr (cdr rest) new-up (+ ans new-up))))))))
```

## Erlang

```erlang
-spec reduction_operations(Nums :: [integer()]) -> integer().
reduction_operations([]) -> 0;
reduction_operations([_]) -> 0;
reduction_operations(Nums) ->
    Sorted = lists:sort(Nums),
    [First | Rest] = Sorted,
    {Ans, _, _} = lists:foldl(
        fun(X, {Acc, Prev, Up}) ->
            case X == Prev of
                true ->
                    {Acc + Up, X, Up};
                false ->
                    NewUp = Up + 1,
                    {Acc + NewUp, X, NewUp}
            end
        end,
        {0, First, 0},
        Rest),
    Ans.
```

## Elixir

```elixir
defmodule Solution do
  @spec reduction_operations(nums :: [integer]) :: integer
  def reduction_operations(nums) do
    sorted = Enum.sort(nums)

    {ans, _prev, _up} =
      Enum.reduce(sorted, {0, nil, 0}, fn val, {ans, prev, up} ->
        case prev do
          nil -> {ans, val, up}
          _ ->
            new_up = if val != prev, do: up + 1, else: up
            {ans + new_up, val, new_up}
        end
      end)

    ans
  end
end
```
