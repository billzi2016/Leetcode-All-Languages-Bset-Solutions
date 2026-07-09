# 2824. Count Pairs Whose Sum is Less than Target

## Cpp

```cpp
class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        int n = nums.size();
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] + nums[j] < target) ++cnt;
            }
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int countPairs(java.util.List<Integer> nums, int target) {
        int n = nums.size();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = nums.get(i);
        }
        java.util.Arrays.sort(arr);
        int left = 0, right = n - 1;
        int count = 0;
        while (left < right) {
            if (arr[left] + arr[right] < target) {
                count += right - left;
                left++;
            } else {
                right--;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        cnt = 0
        for i in range(n):
            ai = nums[i]
            for j in range(i + 1, n):
                if ai + nums[j] < target:
                    cnt += 1
        return cnt
```

## Python3

```python
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count
```

## C

```c
int countPairs(int* nums, int numsSize, int target) {
    int cnt = 0;
    for (int i = 0; i < numsSize; ++i) {
        for (int j = i + 1; j < numsSize; ++j) {
            if (nums[i] + nums[j] < target) {
                ++cnt;
            }
        }
    }
    return cnt;
}
```

## Csharp

```csharp
public class Solution {
    public int CountPairs(IList<int> nums, int target) {
        int n = nums.Count;
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] < target) {
                    count++;
                }
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var countPairs = function(nums, target) {
    let count = 0;
    const n = nums.length;
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            if (nums[i] + nums[j] < target) {
                ++count;
            }
        }
    }
    return count;
};
```

## Typescript

```typescript
function countPairs(nums: number[], target: number): number {
    let count = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (nums[i] + nums[j] < target) {
                count++;
            }
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function countPairs($nums, $target) {
        $cnt = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                if ($nums[$i] + $nums[$j] < $target) {
                    $cnt++;
                }
            }
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func countPairs(_ nums: [Int], _ target: Int) -> Int {
        var count = 0
        let n = nums.count
        for i in 0..<n {
            for j in (i + 1)..<n {
                if nums[i] + nums[j] < target {
                    count += 1
                }
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPairs(nums: List<Int>, target: Int): Int {
        var count = 0
        val n = nums.size
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (nums[i] + nums[j] < target) {
                    count++
                }
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countPairs(List<int> nums, int target) {
    int count = 0;
    for (int i = 0; i < nums.length; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        if (nums[i] + nums[j] < target) {
          count++;
        }
      }
    }
    return count;
  }
}
```

## Golang

```go
func countPairs(nums []int, target int) int {
    cnt := 0
    n := len(nums)
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            if nums[i]+nums[j] < target {
                cnt++
            }
        }
    }
    return cnt
}
```

## Ruby

```ruby
def count_pairs(nums, target)
  count = 0
  n = nums.length
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      count += 1 if nums[i] + nums[j] < target
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def countPairs(nums: List[int], target: int): Int = {
        var count = 0
        val n = nums.length
        for (i <- 0 until n) {
            for (j <- i + 1 until n) {
                if (nums(i) + nums(j) < target) count += 1
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_pairs(nums: Vec<i32>, target: i32) -> i32 {
        let mut a = nums;
        a.sort();
        let n = a.len();
        if n < 2 {
            return 0;
        }
        let mut left = 0usize;
        let mut right = n - 1;
        let mut cnt: i64 = 0;
        while left < right {
            if a[left] + a[right] < target {
                cnt += (right - left) as i64;
                left += 1;
            } else {
                right -= 1;
            }
        }
        cnt as i32
    }
}
```

## Racket

```racket
(define/contract (count-pairs nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length nums)])
    (for/sum ([i (in-range n)]
              [j (in-range (+ i 1) n)])
      (if (< (+ (list-ref nums i) (list-ref nums j)) target)
          1
          0))))
```

## Erlang

```erlang
-spec count_pairs(Nums :: [integer()], Target :: integer()) -> integer().
count_pairs(Nums, Target) ->
    count_pairs_recursive(Nums, Target).

count_pairs_recursive([], _Target) -> 0;
count_pairs_recursive([H|T], Target) ->
    CountWithH = length([1 || X <- T, H + X < Target]),
    CountWithH + count_pairs_recursive(T, Target).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_pairs(nums :: [integer], target :: integer) :: integer
  def count_pairs(nums, target) do
    len = length(nums)

    0..(len - 2)
    |> Enum.reduce(0, fn i, acc ->
      ai = Enum.at(nums, i)

      cnt =
        (i + 1)..(len - 1)
        |> Enum.count(fn j -> ai + Enum.at(nums, j) < target end)

      acc + cnt
    end)
  end
end
```
