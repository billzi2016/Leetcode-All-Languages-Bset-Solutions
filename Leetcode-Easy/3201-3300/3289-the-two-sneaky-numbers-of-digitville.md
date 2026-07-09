# 3289. The Two Sneaky Numbers of Digitville

## Cpp

```cpp
class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        int n = nums.size() - 2;
        vector<int> cnt(n, 0);
        vector<int> res;
        for (int x : nums) {
            if (++cnt[x] == 2) {
                res.push_back(x);
                if (res.size() == 2) break;
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        int n = nums.length - 2; // original range size
        boolean[] seen = new boolean[n];
        int[] result = new int[2];
        int idx = 0;
        for (int num : nums) {
            if (seen[num]) {
                result[idx++] = num;
                if (idx == 2) break;
            } else {
                seen[num] = true;
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) - 2
        total_expected = n * (n - 1) // 2
        sq_expected = (n - 1) * n * (2 * n - 1) // 6

        total_actual = sum(nums)
        sq_actual = sum(x * x for x in nums)

        s = total_actual - total_expected          # a + b
        sq_diff = sq_actual - sq_expected           # a^2 + b^2

        ab = (s * s - sq_diff) // 2                # a * b

        # discriminant = (a - b)^2
        disc = s * s - 4 * ab
        import math
        sqrt_disc = int(math.isqrt(disc))

        a = (s + sqrt_disc) // 2
        b = s - a
        return [a, b]
```

## Python3

```python
from typing import List
import math

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2
        expected_sum = n * (n - 1) // 2
        expected_sq = n * (n - 1) * (2 * n - 1) // 6

        actual_sum = sum(nums)
        actual_sq = sum(x * x for x in nums)

        diff = actual_sum - expected_sum          # a + b
        diff_sq = actual_sq - expected_sq         # a^2 + b^2

        prod = (diff * diff - diff_sq) // 2       # a * b

        disc = diff * diff - 4 * prod
        sqrt_disc = int(math.isqrt(disc))

        a = (diff + sqrt_disc) // 2
        b = diff - a
        return [a, b]
```

## C

```c
#include <stdlib.h>
#include <math.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getSneakyNumbers(int* nums, int numsSize, int* returnSize) {
    int n = numsSize - 2; // original range size
    long long expectedSum = (long long)n * (n - 1) / 2;
    long long expectedSq = (long long)n * (n - 1) * (2LL * n - 1) / 6;

    long long actualSum = 0, actualSq = 0;
    for (int i = 0; i < numsSize; ++i) {
        actualSum += nums[i];
        actualSq += (long long)nums[i] * nums[i];
    }

    long long sumDup = actualSum - expectedSum;          // x + y
    long long sqDiff = actualSq - expectedSq;            // x^2 + y^2

    long long prod = ((sumDup * sumDup) - sqDiff) / 2;   // xy

    long long disc = sumDup * sumDup - 4LL * prod;       // (x - y)^2
    long long sqrtDisc = (long long)(sqrt((double)disc) + 0.5);
    while (sqrtDisc * sqrtDisc > disc) --sqrtDisc;
    while ((sqrtDisc + 1) * (sqrtDisc + 1) <= disc) ++sqrtDisc;

    int x = (int)((sumDup + sqrtDisc) / 2);
    int y = (int)(sumDup - x);

    int* res = (int*)malloc(2 * sizeof(int));
    res[0] = x;
    res[1] = y;
    *returnSize = 2;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] GetSneakyNumbers(int[] nums) {
        int N = nums.Length;
        int n = N - 2; // original range size
        
        long sum = 0;
        long sumSq = 0;
        foreach (int x in nums) {
            sum += x;
            sumSq += (long)x * x;
        }
        
        long expectedSum = (long)n * (n - 1) / 2;
        long expectedSq = (long)n * (n - 1) * (2L * n - 1) / 6;
        
        long diffSum = sum - expectedSum;          // a + b
        long diffSq = sumSq - expectedSq;          // a^2 + b^2
        
        long prod = ((diffSum * diffSum) - diffSq) / 2; // a * b
        
        long discriminant = diffSum * diffSum - 4 * prod;
        long sqrtD = (long)Math.Round(Math.Sqrt(discriminant));
        
        int a = (int)((diffSum + sqrtD) / 2);
        int b = (int)(diffSum - a);
        
        return new int[] { a, b };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getSneakyNumbers = function(nums) {
    const n = nums.length - 2;
    const seen = new Array(n).fill(false);
    const result = [];
    for (const num of nums) {
        if (seen[num]) {
            result.push(num);
            if (result.length === 2) break;
        } else {
            seen[num] = true;
        }
    }
    return result;
};
```

## Typescript

```typescript
function getSneakyNumbers(nums: number[]): number[] {
    const n = nums.length - 2;
    let actualSum = 0;
    let actualSq = 0;
    for (const x of nums) {
        actualSum += x;
        actualSq += x * x;
    }
    const expectedSum = n * (n - 1) / 2;
    const expectedSq = (n - 1) * n * (2 * n - 1) / 6;

    const S = actualSum - expectedSum; // a + b
    const P = actualSq - expectedSq;   // a^2 + b^2

    const ab = (S * S - P) / 2;
    const D = S * S - 4 * ab;
    const sqrtD = Math.round(Math.sqrt(D));

    const a = (S + sqrtD) / 2;
    const b = S - a;

    return [a, b];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function getSneakyNumbers($nums) {
        $len = count($nums);
        $n = $len - 2; // original range size

        $actualSum = 0;
        $actualSqSum = 0;
        foreach ($nums as $v) {
            $actualSum += $v;
            $actualSqSum += $v * $v;
        }

        // Expected sums for numbers 0 .. n-1
        $expectedSum = intdiv($n * ($n - 1), 2);
        $expectedSqSum = intdiv(($n - 1) * $n * (2 * $n - 1), 6);

        $diff1 = $actualSum - $expectedSum;          // a + b
        $diff2 = $actualSqSum - $expectedSqSum;      // a^2 + b^2

        // Compute product ab using (a+b)^2 = a^2 + 2ab + b^2
        $ab = ($diff1 * $diff1 - $diff2) / 2;

        // Discriminant of x^2 - (a+b)x + ab = 0
        $D = $diff1 * $diff1 - 4 * $ab;
        $sqrtD = (int)sqrt($D);

        $a = intdiv($diff1 + $sqrtD, 2);
        $b = $diff1 - $a;

        return [$a, $b];
    }
}
```

## Swift

```swift
class Solution {
    func getSneakyNumbers(_ nums: [Int]) -> [Int] {
        let n = nums.count - 2
        var sum: Int64 = 0
        var sumSq: Int64 = 0
        for v in nums {
            let val = Int64(v)
            sum += val
            sumSq += val * val
        }
        let nn = Int64(n)
        let expectedSum = nn * (nn - 1) / 2               // sum 0..n-1
        let expectedSq = (nn - 1) * nn * (2 * nn - 1) / 6 // sum of squares 0..n-1
        
        let S = sum - expectedSum          // a + b
        let P = sumSq - expectedSq         // a^2 + b^2
        let ab = (S * S - P) / 2           // a * b
        
        var discriminant = S * S - 4 * ab   // (a - b)^2
        var sqrtD = Int64(Double(discriminant).squareRoot())
        while sqrtD * sqrtD < discriminant { sqrtD += 1 }
        while sqrtD * sqrtD > discriminant { sqrtD -= 1 }
        
        let a = (S + sqrtD) / 2
        let b = (S - sqrtD) / 2
        
        return [Int(a), Int(b)]
    }
}
```

## Kotlin

```kotlin
import kotlin.math.sqrt
import kotlin.math.roundToLong

class Solution {
    fun getSneakyNumbers(nums: IntArray): IntArray {
        val n = nums.size - 2
        var sum = 0L
        var sumSq = 0L
        for (v in nums) {
            sum += v.toLong()
            sumSq += v.toLong() * v
        }
        val expectedSum = n.toLong() * (n - 1) / 2
        val expectedSq = n.toLong() * (n - 1) * (2L * n - 1) / 6
        val diff = sum - expectedSum          // a + b
        val diffSq = sumSq - expectedSq        // a^2 + b^2
        val product = (diff * diff - diffSq) / 2   // a * b
        val discriminant = diff * diff - 4 * product
        val sqrtD = sqrt(discriminant.toDouble()).roundToLong()
        val a = ((diff + sqrtD) / 2).toInt()
        val b = (diff - a).toInt()
        return intArrayOf(a, b)
    }
}
```

## Dart

```dart
import 'dart:math' as math;

class Solution {
  List<int> getSneakyNumbers(List<int> nums) {
    int n = nums.length - 2;
    int expectedSum = n * (n - 1) ~/ 2;
    int expectedSq = n * (n - 1) * (2 * n - 1) ~/ 6;

    int actualSum = 0;
    int actualSq = 0;
    for (int x in nums) {
      actualSum += x;
      actualSq += x * x;
    }

    int sumDup = actualSum - expectedSum;          // a + b
    int sqDup = actualSq - expectedSq;             // a^2 + b^2

    int prodDup = ((sumDup * sumDup - sqDup) ~/ 2); // a * b
    int discriminant = sumDup * sumDup - 4 * prodDup;
    int sqrtD = math.sqrt(discriminant).toInt();

    int a = (sumDup + sqrtD) ~/ 2;
    int b = (sumDup - sqrtD) ~/ 2;

    return [a, b];
  }
}
```

## Golang

```go
func getSneakyNumbers(nums []int) []int {
    n := len(nums) - 2
    count := make([]int, n)
    for _, v := range nums {
        count[v]++
    }
    res := make([]int, 0, 2)
    for i, c := range count {
        if c == 2 {
            res = append(res, i)
        }
    }
    return res
}
```

## Ruby

```ruby
def get_sneaky_numbers(nums)
  n = nums.length - 2
  counts = Array.new(n, 0)
  result = []
  nums.each do |num|
    counts[num] += 1
    result << num if counts[num] == 2
  end
  result
end
```

## Scala

```scala
object Solution {
    def getSneakyNumbers(nums: Array[Int]): Array[Int] = {
        val n = nums.length - 2
        var actualSum: Long = 0L
        var actualSq: Long = 0L
        for (v <- nums) {
            actualSum += v
            actualSq += v.toLong * v
        }
        val expectedSum: Long = n.toLong * (n - 1) / 2
        val expectedSq: Long = (n - 1).toLong * n * (2L * n - 1) / 6

        val s = actualSum - expectedSum          // a + b
        val diff2 = actualSq - expectedSq        // a^2 + b^2

        val product = (s * s - diff2) / 2       // a * b

        val discriminant = s * s - 4 * product
        val sqrtD = math.sqrt(discriminant.toDouble).toLong

        val a = ((s - sqrtD) / 2).toInt
        val b = ((s + sqrtD) / 2).toInt
        Array(a, b)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_sneaky_numbers(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len() - 2;
        let mut seen = vec![false; n];
        let mut res = Vec::new();
        for &x in nums.iter() {
            let idx = x as usize;
            if seen[idx] {
                res.push(x);
                if res.len() == 2 {
                    break;
                }
            } else {
                seen[idx] = true;
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (get-sneaky-numbers nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ([len (length nums)]
         [n (- len 2)]
         [counts (make-vector n 0)]
         [result '()])
    (for ([x nums])
      (define cnt (vector-ref counts x))
      (when (= cnt 1)
        (set! result (cons x result)))
      (vector-set! counts x (+ cnt 1)))
    (reverse result)))
```

## Erlang

```erlang
-spec get_sneaky_numbers(Nums :: [integer()]) -> [integer()].
get_sneaky_numbers(Nums) ->
    Counts = lists:foldl(
        fun(N, Acc) ->
            maps:update_with(N, fun(C) -> C + 1 end, 1, Acc)
        end,
        #{},
        Nums
    ),
    [K || {K, V} <- maps:to_list(Counts), V == 2].
```

## Elixir

```elixir
defmodule Solution do
  @spec get_sneaky_numbers(nums :: [integer]) :: [integer]
  def get_sneaky_numbers(nums) do
    nums
    |> Enum.reduce(%{}, fn x, acc -> Map.update(acc, x, 1, &(&1 + 1)) end)
    |> Enum.filter(fn {_k, v} -> v == 2 end)
    |> Enum.map(fn {k, _v} -> k end)
  end
end
```
