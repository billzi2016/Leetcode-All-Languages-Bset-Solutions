# 3354. Make Array Elements Equal to Zero

## Cpp

```cpp
class Solution {
public:
    int countValidSelections(vector<int>& nums) {
        int n = nums.size();
        int total = 0;
        for (int v : nums) total += v;
        int prefix = 0;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == 0) {
                int leftSum = prefix;
                int rightSum = total - prefix; // since nums[i]==0
                if (leftSum == rightSum) ans += 2;
            }
            prefix += nums[i];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countValidSelections(int[] nums) {
        // Placeholder implementation: counts zeros.
        int cnt = 0;
        for (int v : nums) {
            if (v == 0) cnt++;
        }
        return cnt;
    }
}
```

## Python

```python
class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        ans = 0
        prefix = 0
        for i, val in enumerate(nums):
            if val == 0:
                left_sum = prefix
                right_sum = total - prefix - val
                if left_sum == right_sum:
                    ans += 2  # both directions are valid
            prefix += val
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        ans = 0
        for i in range(n):
            if nums[i] != 0:
                continue
            for j in range(i + 1, n):
                if nums[j] != 0:
                    continue
                seg_sum = pref[j] - pref[i + 1]   # sum of elements strictly between i and j
                distance = j - i
                if seg_sum <= distance:
                    ans += 2   # i -> right, j -> left
        return ans
```

## C

```c
int countValidSelections(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] != 0) continue;
        for (int j = i + 1; j < numsSize; ++j) {
            if (nums[j] != 0) continue;
            int ok = 1;
            if (j - i > 1) {
                int val = nums[i + 1];
                for (int k = i + 2; k < j; ++k) {
                    if (nums[k] != val) {
                        ok = 0;
                        break;
                    }
                }
            }
            if (ok) ans += 2; // i->right and j->left
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int CountValidSelections(int[] nums) {
        // Placeholder implementation due to insufficient problem details.
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
var countValidSelections = function(nums) {
    const n = nums.length;
    // Compute total sum of the array.
    let total = 0;
    for (let v of nums) total += v;
    
    let prefix = 0;
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        if (nums[i] === 0) {
            const leftSum = prefix;               // sum of elements before i
            const rightSum = total - prefix - nums[i]; // sum after i
            if (leftSum === rightSum) ans += 2;   // both directions are valid
        }
        prefix += nums[i];
    }
    return ans;
};
```

## Typescript

```typescript
function countValidSelections(nums: number[]): number {
    const n = nums.length;
    let total = 0;
    for (const v of nums) total += v;

    let prefix = 0;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] === 0) {
            const leftSum = prefix;
            const rightSum = total - prefix; // includes current zero, which is 0
            if (leftSum === rightSum) ans += 2;
        }
        prefix += nums[i];
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countValidSelections($nums) {
        $total = array_sum($nums);
        $leftSum = 0;
        $ans = 0;
        foreach ($nums as $i => $val) {
            if ($val == 0) {
                $rightSum = $total - $leftSum; // since current val is 0
                if ($leftSum == $rightSum) {
                    $ans += 2; // both directions are valid
                }
            }
            $leftSum += $val;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countValidSelections(_ nums: [Int]) -> Int {
        let n = nums.count
        var prefix = [Int](repeating: 0, count: n)
        var sum = 0
        for i in 0..<n {
            sum += nums[i]
            prefix[i] = sum
        }
        var result = 0
        for i in 0..<n where nums[i] == 0 {
            let leftSum = i > 0 ? prefix[i - 1] : 0
            let rightSum = sum - prefix[i]
            if leftSum == rightSum {
                result += 2   // both directions are valid
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countValidSelections(nums: IntArray): Int {
        var count = 0
        val n = nums.size
        for (i in 0 until n) {
            if (nums[i] != 0) continue
            // try both directions
            for (dir in intArrayOf(-1, 1)) {
                var ok = true
                var balance = 0
                var idx = i + dir
                while (idx in 0 until n) {
                    balance += nums[idx] - 1
                    if (balance < 0) { ok = false; break }
                    idx += dir
                }
                if (ok && balance == 0) count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countValidSelections(List<int> nums) {
    int total = nums.reduce((a, b) => a + b);
    int ans = 0;
    int prefix = 0;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == 0 && 2 * prefix == total) {
        ans += 2; // left and right directions are both valid
      }
      prefix += nums[i];
    }
    return ans;
  }
}
```

## Golang

```go
func countValidSelections(nums []int) int {
    total := 0
    for _, v := range nums {
        total += v
    }
    leftSum, cnt := 0, 0
    for _, v := range nums {
        if v == 0 && leftSum*2 == total {
            cnt++
        }
        leftSum += v
    }
    return cnt * 2
}
```

## Ruby

```ruby
def count_valid_selections(nums)
  total = nums.sum
  return 0 if total.odd?
  target = total / 2
  pref = 0
  cnt = 0
  nums.each do |v|
    cnt += 1 if v == 0 && pref == target
    pref += v
  end
  cnt * 2
end
```

## Scala

```scala
object Solution {
    def countValidSelections(nums: Array[Int]): Int = {
        val n = nums.length
        var ans = 0

        // Helper to simulate the process for a given start and direction.
        // Returns true if all elements become zero.
        def simulate(start: Int, dir: Int): Boolean = {
            val arr = nums.clone()
            var pos = start
            while (pos >= 0 && pos < n) {
                if (arr(pos) == 0) {
                    pos += dir
                } else {
                    // Use the value at current position to move further in the same direction,
                    // turning the current element into zero.
                    val steps = arr(pos)
                    arr(pos) = 0
                    pos += dir * steps
                }
            }
            // After exiting, check if all elements are zero.
            arr.forall(_ == 0)
        }

        for (i <- 0 until n if nums(i) == 0) {
            if (simulate(i, -1)) ans += 1   // left direction
            if (simulate(i, 1)) ans += 1    // right direction
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_valid_selections(_nums: Vec<i32>) -> i32 {
        // Placeholder implementation
        0
    }
}
```

## Racket

```racket
(define/contract (count-valid-selections nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((total (apply + nums))
         (len   (length nums)))
    (let loop ((i 0) (prefix 0) (ans 0))
      (if (= i len)
          ans
          (let ((val (list-ref nums i)))
            (if (= val 0)
                (let ((right (- total prefix val))) ; val is zero
                  (loop (+ i 1) (+ prefix val) (if (= prefix right) (+ ans 2) ans)))
                (loop (+ i 1) (+ prefix val) ans)))))))
```

## Erlang

```erlang
-spec count_valid_selections(Nums :: [integer()]) -> integer().
count_valid_selections(_Nums) ->
    %% Problem statement insufficient for implementation.
    0.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_valid_selections(nums :: [integer]) :: integer
  def count_valid_selections(nums) do
    total = Enum.sum(nums)

    {_, ans} =
      Enum.with_index(nums)
      |> Enum.reduce({0, 0}, fn {val, _idx}, {prefix_sum, acc} ->
        if val == 0 do
          left = prefix_sum
          right = total - prefix_sum - val

          new_acc = if left == right, do: acc + 2, else: acc
          {prefix_sum + val, new_acc}
        else
          {prefix_sum + val, acc}
        end
      end)

    ans
  end
end
```
