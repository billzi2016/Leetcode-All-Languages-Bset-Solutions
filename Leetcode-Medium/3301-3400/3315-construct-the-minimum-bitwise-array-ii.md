# 3315. Construct the Minimum Bitwise Array II

## Cpp

```cpp
class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        vector<int> ans;
        for (int num : nums) {
            if ((num & 1) == 0) { // even numbers cannot be represented
                ans.push_back(-1);
                continue;
            }
            int t = 0;
            while ((num >> t) & 1) ++t;   // count trailing ones, at least 1
            int p = t - 1;                 // position of the bit to clear
            int val = num ^ (1 << p);      // clear that bit
            ans.push_back(val);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] minBitwiseArray(java.util.List<Integer> nums) {
        int n = nums.size();
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            int val = nums.get(i);
            if ((val & 1) == 0) { // even numbers cannot be represented
                ans[i] = -1;
                continue;
            }
            int cnt = 0;
            while (((val >> cnt) & 1) == 1) {
                cnt++;
            }
            int pos = cnt - 1;               // highest bit among trailing ones
            ans[i] = val - (1 << pos);       // clear that bit to get minimal x
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for n in nums:
            if n % 2 == 0:
                res.append(-1)
                continue
            # count trailing ones
            s = 0
            temp = n
            while temp & 1:
                s += 1
                temp >>= 1
            # prefix bits above the zero bit
            prefix = n >> (s + 1)
            lower = ((1 << (s - 1)) - 1) if s > 1 else 0
            ans = (prefix << (s + 1)) | lower
            res.append(ans)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for y in nums:
            if y % 2 == 0:
                res.append(-1)
                continue
            # count trailing ones
            t = 0
            temp = y
            while temp & 1:
                t += 1
                temp >>= 1
            # turn off the most significant bit among the trailing ones
            x = y - (1 << (t - 1))
            res.append(x)
        return res
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {
    int *ans = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        int num = nums[i];
        if ((num & 1) == 0) {          // even numbers have no solution
            ans[i] = -1;
            continue;
        }
        int t = 0;
        while ((num >> t) & 1) {       // count trailing ones
            ++t;
        }
        // t >= 1 because num is odd
        int sub = 1 << (t - 1);        // clear the highest trailing one
        ans[i] = num - sub;
    }
    *returnSize = numsSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] MinBitwiseArray(IList<int> nums) {
        int n = nums.Count;
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            // Even numbers cannot be represented
            if ((num & 1) == 0) {
                res[i] = -1;
                continue;
            }
            int ans = -1;
            // Check bits from high to low (up to 30 because nums[i] <= 1e9)
            for (int k = 30; k >= 0; k--) {
                int maskLow = (k == 0) ? 0 : ((1 << k) - 1);
                if ((num & maskLow) == maskLow && ((num >> k) & 1) == 1) {
                    ans = num - (1 << k);
                    break; // largest k gives minimal answer
                }
            }
            res[i] = ans;
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var minBitwiseArray = function(nums) {
    const ans = [];
    for (const num of nums) {
        if ((num & 1) === 0) {
            ans.push(-1);
            continue;
        }
        let t = 0;
        while (((num >> t) & 1) === 1) {
            t++;
        }
        // t >= 1 for odd numbers
        const val = num - (1 << (t - 1));
        ans.push(val);
    }
    return ans;
};
```

## Typescript

```typescript
function minBitwiseArray(nums: number[]): number[] {
    const result: number[] = [];
    for (const num of nums) {
        if ((num & 1) === 0) { // even numbers cannot be represented
            result.push(-1);
            continue;
        }
        let t = 0; // count trailing ones
        while (((num >> t) & 1) === 1) {
            t++;
        }
        const higher = num >> t;
        const lowerMask = t > 1 ? ((1 << (t - 1)) - 1) : 0;
        const ans = (higher << t) | lowerMask;
        result.push(ans);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function minBitwiseArray($nums) {
        $result = [];
        foreach ($nums as $num) {
            // If the number is even, impossible to satisfy condition
            if (($num & 1) == 0) {
                $result[] = -1;
                continue;
            }
            // Count consecutive trailing ones
            $len = 0;
            $temp = $num;
            while (($temp & 1) == 1) {
                $len++;
                $temp >>= 1;
            }
            // Subtract the highest bit in that trailing block
            $ans = $num - (1 << ($len - 1));
            $result[] = $ans;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func minBitwiseArray(_ nums: [Int]) -> [Int] {
        var ans = [Int]()
        for num in nums {
            if num % 2 == 0 {
                ans.append(-1)
                continue
            }
            var t = 0
            var temp = num
            while (temp & 1) == 1 {
                t += 1
                temp >>= 1
            }
            // t >= 1 for odd numbers
            let prefix = num >> t
            let b = (prefix << t) | (1 << (t - 1))
            ans.append(b - 1)
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minBitwiseArray(nums: List<Int>): IntArray {
        val result = IntArray(nums.size)
        for (i in nums.indices) {
            val num = nums[i]
            if ((num and 1) == 0) {
                result[i] = -1
                continue
            }
            var cnt = 0
            var x = num
            while ((x and 1) == 1) {
                cnt++
                x = x ushr 1
            }
            val mask = 1 shl (cnt - 1)
            result[i] = num xor mask
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> minBitwiseArray(List<int> nums) {
    List<int> ans = [];
    for (int num in nums) {
      if ((num & 1) == 0) {
        ans.add(-1);
        continue;
      }
      int cnt = 0;
      int t = num;
      while ((t & 1) == 1) {
        cnt++;
        t >>= 1;
      }
      int d = 1 << (cnt - 1);
      ans.add(num - d);
    }
    return ans;
  }
}
```

## Golang

```go
func minBitwiseArray(nums []int) []int {
    res := make([]int, len(nums))
    for i, v := range nums {
        if v%2 == 0 {
            res[i] = -1
            continue
        }
        cnt := 0
        temp := v
        for temp&1 == 1 {
            cnt++
            temp >>= 1
        }
        // cnt >= 1 because v is odd
        ans := v - (1 << (cnt - 1))
        res[i] = ans
    }
    return res
}
```

## Ruby

```ruby
def min_bitwise_array(nums)
  result = []
  nums.each do |num|
    if num.even?
      result << -1
      next
    end
    t = 0
    while ((num >> t) & 1) == 1
      t += 1
    end
    k = t - 1
    result << (num - (1 << k))
  end
  result
end
```

## Scala

```scala
object Solution {
    def minBitwiseArray(nums: List[Int]): Array[Int] = {
        nums.map { num =>
            if ((num & 1) == 0) -1
            else {
                var t = 0
                var temp = num
                while ((temp & 1) == 1) {
                    t += 1
                    temp >>= 1
                }
                val pos = t - 1
                val higher = (num >> (pos + 1)) << (pos + 1)
                val lower = if (pos > 0) ((1 << pos) - 1) else 0
                higher | lower
            }
        }.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = Vec::with_capacity(nums.len());
        for &num in nums.iter() {
            if num % 2 == 0 {
                ans.push(-1);
                continue;
            }
            // count trailing ones
            let mut cnt = 0usize;
            let mut x = num as u32;
            while (x & 1) == 1 {
                cnt += 1;
                x >>= 1;
            }
            // cnt >= 1 because num is odd
            let sub = 1i32 << (cnt - 1);
            ans.push(num - sub);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-bitwise-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (map
   (lambda (num)
     (if (even? num)
         -1
         (let loop ((i 0))
           (if (= (bitwise-and num (arithmetic-shift 1 i)) 0)
               (let ((t (- i 1)))
                 (- num (arithmetic-shift 1 t)))
               (loop (+ i 1))))))
   nums))
```

## Erlang

```erlang
-spec min_bitwise_array(Nums :: [integer()]) -> [integer()].
min_bitwise_array(Nums) ->
    lists:map(
      fun(N) ->
          case N rem 2 of
              0 -> -1;
              _ ->
                  T = N + 1,
                  if (T band (T-1)) == 0 ->
                         (T div 2) - 1;
                     true ->
                         -1
                  end
          end
      end,
      Nums
    ).
```

## Elixir

```elixir
defmodule Solution do
  require Bitwise

  @spec min_bitwise_array(nums :: [integer]) :: [integer]
  def min_bitwise_array(nums) do
    Enum.map(nums, fn n ->
      if rem(n, 2) == 0 do
        -1
      else
        t = trailing_ones(n)
        n - (1 <<< (t - 1))
      end
    end)
  end

  defp trailing_ones(0), do: 0
  defp trailing_ones(n), do: trailing_ones_rec(n, 0)

  defp trailing_ones_rec(n, cnt) when Bitwise.band(n, 1) == 1 do
    trailing_ones_rec(Bitwise.bsr(n, 1), cnt + 1)
  end

  defp trailing_ones_rec(_, cnt), do: cnt
end
```
