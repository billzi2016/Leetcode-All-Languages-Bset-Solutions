# 3194. Minimum Average of Smallest and Largest Elements

## Cpp

```cpp
class Solution {
public:
    double minimumAverage(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        double ans = 1e9;
        for (int i = 0; i < n / 2; ++i) {
            double avg = (nums[i] + nums[n - 1 - i]) / 2.0;
            if (avg < ans) ans = avg;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public double minimumAverage(int[] nums) {
        java.util.Arrays.sort(nums);
        int n = nums.length;
        double minAvg = Double.MAX_VALUE;
        for (int i = 0; i < n / 2; i++) {
            double avg = (nums[i] + nums[n - 1 - i]) / 2.0;
            if (avg < minAvg) {
                minAvg = avg;
            }
        }
        return minAvg;
    }
}
```

## Python

```python
class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()
        n = len(nums)
        min_avg = float('inf')
        for i in range(n // 2):
            avg = (nums[i] + nums[n - i - 1]) / 2.0
            if avg < min_avg:
                min_avg = avg
        return min_avg
```

## Python3

```python
from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        min_avg = float('inf')
        for i in range(n // 2):
            avg = (nums[i] + nums[n - i - 1]) / 2.0
            if avg < min_avg:
                min_avg = avg
        return min_avg
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

double minimumAverage(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    double minAvg = 1e9;
    for (int i = 0; i < numsSize / 2; ++i) {
        double avg = ((double)nums[i] + (double)nums[numsSize - 1 - i]) / 2.0;
        if (avg < minAvg) {
            minAvg = avg;
        }
    }
    return minAvg;
}
```

## Csharp

```csharp
public class Solution
{
    public double MinimumAverage(int[] nums)
    {
        Array.Sort(nums);
        int n = nums.Length;
        double minAvg = double.MaxValue;
        for (int i = 0; i < n / 2; i++)
        {
            double avg = (nums[i] + nums[n - 1 - i]) / 2.0;
            if (avg < minAvg) minAvg = avg;
        }
        return minAvg;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumAverage = function(nums) {
    nums.sort((a, b) => a - b);
    let minAvg = Infinity;
    const n = nums.length;
    for (let i = 0; i < n / 2; ++i) {
        const avg = (nums[i] + nums[n - 1 - i]) / 2;
        if (avg < minAvg) minAvg = avg;
    }
    return minAvg;
};
```

## Typescript

```typescript
function minimumAverage(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let minAvg = Infinity;
    const n = nums.length;
    for (let i = 0; i < n / 2; ++i) {
        const avg = (nums[i] + nums[n - 1 - i]) / 2;
        if (avg < minAvg) minAvg = avg;
    }
    return minAvg;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Float
     */
    function minimumAverage($nums) {
        sort($nums);
        $n = count($nums);
        $minAvg = INF;
        for ($i = 0; $i < $n / 2; $i++) {
            $avg = ($nums[$i] + $nums[$n - $i - 1]) / 2.0;
            if ($avg < $minAvg) {
                $minAvg = $avg;
            }
        }
        return $minAvg;
    }
}
```

## Swift

```swift
class Solution {
    func minimumAverage(_ nums: [Int]) -> Double {
        let sorted = nums.sorted()
        var minAvg = Double.greatestFiniteMagnitude
        let n = sorted.count
        for i in 0..<(n / 2) {
            let avg = Double(sorted[i] + sorted[n - i - 1]) / 2.0
            if avg < minAvg {
                minAvg = avg
            }
        }
        return minAvg
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumAverage(nums: IntArray): Double {
        nums.sort()
        var minAvg = Double.MAX_VALUE
        val n = nums.size
        for (i in 0 until n / 2) {
            val avg = (nums[i] + nums[n - i - 1]) / 2.0
            if (avg < minAvg) minAvg = avg
        }
        return minAvg
    }
}
```

## Dart

```dart
class Solution {
  double minimumAverage(List<int> nums) {
    nums.sort();
    int n = nums.length;
    double minAvg = double.infinity;
    for (int i = 0; i < n ~/ 2; ++i) {
      double avg = (nums[i] + nums[n - 1 - i]) / 2.0;
      if (avg < minAvg) {
        minAvg = avg;
      }
    }
    return minAvg;
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

func minimumAverage(nums []int) float64 {
	sort.Ints(nums)
	n := len(nums)
	minAvg := math.MaxFloat64
	for i := 0; i < n/2; i++ {
		avg := float64(nums[i]+nums[n-1-i]) / 2.0
		if avg < minAvg {
			minAvg = avg
		}
	}
	return minAvg
}
```

## Ruby

```ruby
def minimum_average(nums)
  nums.sort!
  n = nums.length
  min_avg = Float::INFINITY
  (0...(n / 2)).each do |i|
    avg = (nums[i] + nums[n - 1 - i]) / 2.0
    min_avg = avg if avg < min_avg
  end
  min_avg
end
```

## Scala

```scala
object Solution {
    def minimumAverage(nums: Array[Int]): Double = {
        val sorted = nums.sorted
        var minAvg = Double.MaxValue
        val n = sorted.length
        for (i <- 0 until n / 2) {
            val avg = (sorted(i) + sorted(n - 1 - i)).toDouble / 2.0
            if (avg < minAvg) minAvg = avg
        }
        minAvg
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_average(nums: Vec<i32>) -> f64 {
        let mut v = nums;
        v.sort_unstable();
        let n = v.len();
        let mut min_avg = std::f64::MAX;
        for i in 0..n / 2 {
            let avg = (v[i] as f64 + v[n - 1 - i] as f64) / 2.0;
            if avg < min_avg {
                min_avg = avg;
            }
        }
        min_avg
    }
}
```

## Racket

```racket
(define/contract (minimum-average nums)
  (-> (listof exact-integer?) flonum?)
  (let* ([sorted (sort nums <)]
         [n (length sorted)])
    (let loop ((i 0) (min-avg +inf.0))
      (if (= i (/ n 2))
          min-avg
          (let* ([sum (+ (list-ref sorted i)
                         (list-ref sorted (- n i 1)))]
                 [avg (/ sum 2.0)])
            (loop (add1 i) (min avg min-avg)))))))
```

## Erlang

```erlang
-spec minimum_average(Nums :: [integer()]) -> float().
minimum_average(Nums) ->
    Sorted = lists:sort(Nums),
    N = length(Sorted),
    Half = N div 2,
    Averages = [ (lists:nth(I, Sorted) + lists:nth(N - I + 1, Sorted)) / 2.0
                 || I <- lists:seq(1, Half) ],
    lists:min(Averages).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_average(nums :: [integer]) :: float
  def minimum_average(nums) do
    sorted = Enum.sort(nums)
    n = length(sorted)
    half = div(n, 2)

    0..(half - 1)
    |> Enum.map(fn i ->
      (Enum.at(sorted, i) + Enum.at(sorted, n - 1 - i)) / 2.0
    end)
    |> Enum.min()
  end
end
```
