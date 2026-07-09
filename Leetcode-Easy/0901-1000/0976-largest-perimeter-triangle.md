# 0976. Largest Perimeter Triangle

## Cpp

```cpp
class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = nums.size() - 1; i >= 2; --i) {
            long long a = nums[i - 2];
            long long b = nums[i - 1];
            long long c = nums[i];
            if (a + b > c) return static_cast<int>(a + b + c);
        }
        return 0;
    }
};
```

## Java

```java
class Solution {
    public int largestPerimeter(int[] nums) {
        java.util.Arrays.sort(nums);
        for (int i = nums.length - 3; i >= 0; i--) {
            if (nums[i] + nums[i + 1] > nums[i + 2]) {
                return nums[i] + nums[i + 1] + nums[i + 2];
            }
        }
        return 0;
    }
}
```

## Python

```python
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                return nums[i - 2] + nums[i - 1] + nums[i]
        return 0
```

## Python3

```python
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int largestPerimeter(int* nums, int numsSize) {
    if (numsSize < 3) return 0;
    qsort(nums, numsSize, sizeof(int), cmp_int);
    for (int i = numsSize - 1; i >= 2; --i) {
        long long a = nums[i - 2];
        long long b = nums[i - 1];
        long long c = nums[i];
        if (a + b > c) {
            return (int)(a + b + c);
        }
    }
    return 0;
}
```

## Csharp

```csharp
public class Solution {
    public int LargestPerimeter(int[] nums) {
        System.Array.Sort(nums);
        for (int i = nums.Length - 1; i >= 2; i--) {
            if ((long)nums[i - 2] + nums[i - 1] > nums[i]) {
                return nums[i - 2] + nums[i - 1] + nums[i];
            }
        }
        return 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var largestPerimeter = function(nums) {
    // Sort in descending order so the largest side is first
    nums.sort((a, b) => b - a);
    
    for (let i = 0; i < nums.length - 2; i++) {
        const c = nums[i];
        const b = nums[i + 1];
        const a = nums[i + 2];
        // Check triangle inequality: sum of two smaller sides > largest side
        if (a + b > c) {
            return a + b + c;
        }
    }
    
    return 0;
};
```

## Typescript

```typescript
function largestPerimeter(nums: number[]): number {
    nums.sort((a, b) => b - a);
    for (let i = 0; i < nums.length - 2; i++) {
        if (nums[i] < nums[i + 1] + nums[i + 2]) {
            return nums[i] + nums[i + 1] + nums[i + 2];
        }
    }
    return 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function largestPerimeter($nums) {
        rsort($nums);
        $n = count($nums);
        for ($i = 0; $i < $n - 2; $i++) {
            if ($nums[$i] < $nums[$i + 1] + $nums[$i + 2]) {
                return $nums[$i] + $nums[$i + 1] + $nums[$i + 2];
            }
        }
        return 0;
    }
}
```

## Swift

```swift
class Solution {
    func largestPerimeter(_ nums: [Int]) -> Int {
        let sorted = nums.sorted(by: >)
        for i in 0..<(sorted.count - 2) {
            if sorted[i + 1] + sorted[i + 2] > sorted[i] {
                return sorted[i] + sorted[i + 1] + sorted[i + 2]
            }
        }
        return 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestPerimeter(nums: IntArray): Int {
        nums.sort()
        for (i in nums.size - 1 downTo 2) {
            val a = nums[i - 2]
            val b = nums[i - 1]
            val c = nums[i]
            if (a + b > c) return a + b + c
        }
        return 0
    }
}
```

## Dart

```dart
class Solution {
  int largestPerimeter(List<int> nums) {
    nums.sort();
    for (int i = nums.length - 3; i >= 0; i--) {
      if (nums[i] + nums[i + 1] > nums[i + 2]) {
        return nums[i] + nums[i + 1] + nums[i + 2];
      }
    }
    return 0;
  }
}
```

## Golang

```go
func largestPerimeter(nums []int) int {
    sort.Ints(nums)
    for i := len(nums) - 1; i >= 2; i-- {
        if nums[i-2]+nums[i-1] > nums[i] {
            return nums[i-2] + nums[i-1] + nums[i]
        }
    }
    return 0
}
```

## Ruby

```ruby
def largest_perimeter(nums)
  nums.sort!
  (nums.length - 1).downto(2) do |i|
    a = nums[i - 2]
    b = nums[i - 1]
    c = nums[i]
    return a + b + c if a + b > c
  end
  0
end
```

## Scala

```scala
object Solution {
    def largestPerimeter(nums: Array[Int]): Int = {
        val sorted = nums.sorted(Ordering.Int.reverse)
        for (i <- 0 until sorted.length - 2) {
            if (sorted(i + 1) + sorted(i + 2) > sorted(i)) {
                return sorted(i) + sorted(i + 1) + sorted(i + 2)
            }
        }
        0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_perimeter(nums: Vec<i32>) -> i32 {
        let mut v = nums;
        v.sort_unstable();
        for i in (2..v.len()).rev() {
            if v[i - 2] + v[i - 1] > v[i] {
                return v[i - 2] + v[i - 1] + v[i];
            }
        }
        0
    }
}
```

## Racket

```racket
(define/contract (largest-perimeter nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort nums >))
         (n (length sorted)))
    (let loop ((i 0))
      (if (> i (- n 3))
          0
          (let ((a (list-ref sorted i))
                (b (list-ref sorted (+ i 1)))
                (c (list-ref sorted (+ i 2))))
            (if (> (+ b c) a)
                (+ a b c)
                (loop (+ i 1))))))))
```

## Erlang

```erlang
-module(solution).
-export([largest_perimeter/1]).
-spec largest_perimeter(Nums :: [integer()]) -> integer().
largest_perimeter(Nums) ->
    SortedDesc = lists:reverse(lists:sort(Nums)),
    find_perimeter(SortedDesc).

find_perimeter([C, B, A | _]) when B + A > C ->
    C + B + A;
find_perimeter([_, B, A | Rest]) ->
    find_perimeter([B, A | Rest]);
find_perimeter(_) ->
    0.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_perimeter(nums :: [integer]) :: integer
  def largest_perimeter(nums) do
    sorted = Enum.sort(nums, &>=/2)
    find_perimeter(sorted)
  end

  defp find_perimeter([a, b, c | rest]) do
    if b + c > a do
      a + b + c
    else
      find_perimeter([b, c | rest])
    end
  end

  defp find_perimeter(_), do: 0
end
```
