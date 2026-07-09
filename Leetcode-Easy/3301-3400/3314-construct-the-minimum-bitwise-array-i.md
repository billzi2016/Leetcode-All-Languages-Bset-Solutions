# 3314. Construct the Minimum Bitwise Array I

## Cpp

```cpp
class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        vector<int> ans;
        ans.reserve(nums.size());
        for (int p : nums) {
            if ((p & 1) == 0) { // even number, cannot be represented
                ans.push_back(-1);
                continue;
            }
            int cnt = 0;
            while ((p >> cnt) & 1) ++cnt; // count trailing ones, at least 1
            int val = p - (1 << (cnt - 1));
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
            int p = nums.get(i);
            int res = -1;
            for (int x = 0; x <= p; x++) {
                if ((x | (x + 1)) == p) {
                    res = x;
                    break;
                }
            }
            ans[i] = res;
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
        for num in nums:
            if num % 2 == 0:
                res.append(-1)
                continue
            # count trailing ones
            t = 0
            temp = num
            while temp & 1:
                t += 1
                temp >>= 1
            # clear the (t-1)th bit and set lower bits to 1
            x = num & ~(1 << (t - 1))
            if t > 1:
                x |= (1 << (t - 1)) - 1
            res.append(x)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if x % 2 == 0:
                res.append(-1)
                continue
            ans = -1
            for a in range(x + 1):
                if (a | (a + 1)) == x:
                    ans = a
                    break
            res.append(ans)
        return res
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minBitwiseArray(int* nums, int numsSize, int* returnSize){
    int *ans = (int*)malloc(numsSize * sizeof(int));
    *returnSize = numsSize;
    for (int i = 0; i < numsSize; ++i) {
        int y = nums[i];
        if ((y & 1) == 0) {               // even numbers have no solution
            ans[i] = -1;
            continue;
        }
        int r = 0;
        while ( (y >> r) & 1 ) ++r;       // count trailing ones, r >= 1
        int t = r - 1;                    // use the longest suffix of ones
        int higher = y >> (t + 1);        // bits above the suffix
        int lowerMask = (t == 0) ? 0 : ((1 << t) - 1);
        int x = (higher << (t + 1)) | lowerMask;
        ans[i] = x;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] MinBitwiseArray(IList<int> nums) {
        int n = nums.Count;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            int p = nums[i];
            int best = int.MaxValue;
            for (int k = 0; ; k++) {
                int shift = k + 1;
                if (shift >= 31) break;
                int mask = (1 << shift) - 1;
                if (mask > p) break;
                if ((p & mask) == mask) {
                    int x = (p & ~mask) | ((1 << k) - 1);
                    if (x < best) best = x;
                }
            }
            ans[i] = best == int.MaxValue ? -1 : best;
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
var minBitwiseArray = function(nums) {
    const result = [];
    for (const p of nums) {
        let ans = -1;
        for (let x = 0; x < p; ++x) {
            if ((x | (x + 1)) === p) {
                ans = x;
                break;
            }
        }
        result.push(ans);
    }
    return result;
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
        let m = 0; // count trailing ones
        while (((num >> m) & 1) === 1) {
            m++;
        }
        const higher = num >> m;
        const lowerMask = (1 << (m - 1)) - 1; // when m=1 this becomes 0
        const ans = (higher << m) | lowerMask;
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
            $ans = -1;
            for ($a = 0; $a <= $num; $a++) {
                if ( ($a | ($a + 1)) == $num ) {
                    $ans = $a;
                    break;
                }
            }
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
        var result = [Int]()
        for num in nums {
            var ans = -1
            if num > 0 {
                for x in 0..<num {
                    if (x | (x + 1)) == num {
                        ans = x
                        break
                    }
                }
            }
            result.append(ans)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minBitwiseArray(nums: List<Int>): IntArray {
        val res = IntArray(nums.size)
        for ((idx, num) in nums.withIndex()) {
            if (num % 2 == 0) {
                res[idx] = -1
                continue
            }
            var t = 0
            var temp = num
            while ((temp and 1) == 1) {
                t++
                temp = temp shr 1
            }
            // t >= 1 because num is odd
            val high = num ushr t
            if ((high and 1) != 0) {
                res[idx] = -1
                continue
            }
            val lowerMask = if (t > 1) ((1 shl (t - 1)) - 1) else 0
            val ansVal = (high shl t) or lowerMask
            res[idx] = ansVal
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> minBitwiseArray(List<int> nums) {
    List<int> result = [];
    for (int num in nums) {
      if (num == 2) {
        result.add(-1);
        continue;
      }
      int t = 0;
      int temp = num;
      while ((temp & 1) == 1) {
        t++;
        temp >>= 1;
      }
      int k = t - 1; // t >= 1 for odd primes
      int ans = num - (1 << k);
      result.add(ans);
    }
    return result;
  }
}
```

## Golang

```go
func minBitwiseArray(nums []int) []int {
    res := make([]int, len(nums))
    for i, v := range nums {
        ans := -1
        for x := 0; x <= v; x++ {
            if (x | (x + 1)) == v {
                ans = x
                break
            }
        }
        res[i] = ans
    }
    return res
}
```

## Ruby

```ruby
def min_bitwise_array(nums)
  nums.map do |p|
    if p.even?
      -1
    else
      l = 0
      t = p
      while (t & 1) == 1
        l += 1
        t >>= 1
      end
      h = p >> l
      suffix = l > 1 ? ((1 << (l - 1)) - 1) : 0
      (h << l) | suffix
    end
  end
end
```

## Scala

```scala
object Solution {
    def minBitwiseArray(nums: List[Int]): Array[Int] = {
        val ans = new Array[Int](nums.length)
        for ((p, i) <- nums.zipWithIndex) {
            var found = -1
            var x = 0
            while (x < p && found == -1) {
                if ((x | (x + 1)) == p) found = x
                x += 1
            }
            ans(i) = found
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = Vec::with_capacity(nums.len());
        for n in nums {
            if n % 2 == 0 {
                ans.push(-1);
                continue;
            }
            // count trailing ones
            let mut t: usize = 0;
            let mut temp = n as u32;
            while (temp & 1) == 1 {
                t += 1;
                temp >>= 1;
            }
            // t >= 1 because n is odd
            let k = t - 1;               // position of the lowest zero in ans[i]
            let shift = k + 1;           // number of bits to keep as higher part
            let higher = (n as i64) >> shift;
            let lower_mask: i64 = if k == 0 { 0 } else { (1i64 << k) - 1 };
            let x = (higher << shift) + lower_mask;
            ans.push(x as i32);
        }
        ans
    }
}
```

## Racket

```racket
(define (trailing-ones n)
  (let loop ((cnt 0) (x n))
    (if (= (bitwise-and x 1) 1)
        (loop (+ cnt 1) (arithmetic-shift x -1))
        cnt)))

(define/contract (min-bitwise-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (map
   (lambda (n)
     (if (= (bitwise-and n 1) 0)
         -1
         (let* ((t (trailing-ones n))
                (high (arithmetic-shift (arithmetic-shift n (- t)) t))
                (low (if (= t 0)
                         0
                         (sub1 (arithmetic-shift 1 (- t 1))))))
           (+ high low))))
   nums))
```

## Erlang

```erlang
-module(solution).
-export([min_bitwise_array/1]).

-spec min_bitwise_array(Nums :: [integer()]) -> [integer()].
min_bitwise_array(Nums) ->
    lists:map(fun find_min/1, Nums).

find_min(Num) ->
    find_min_helper(0, Num).

find_min_helper(X, Num) when X =< Num ->
    case (X bor (X + 1)) of
        Num -> X;
        _   -> find_min_helper(X + 1, Num)
    end;
find_min_helper(_, _) ->
    -1.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec min_bitwise_array(nums :: [integer]) :: [integer]
  def min_bitwise_array(nums) do
    Enum.map(nums, fn p ->
      if (p &&& 1) == 0 do
        -1
      else
        t = trailing_ones(p)
        p - (1 <<< (t - 1))
      end
    end)
  end

  defp trailing_ones(n), do: trailing_ones(n, 0)

  defp trailing_ones(n, cnt) do
    if (n &&& (1 <<< cnt)) != 0 do
      trailing_ones(n, cnt + 1)
    else
      cnt
    end
  end
end
```
