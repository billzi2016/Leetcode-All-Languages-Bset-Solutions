# 1979. Find Greatest Common Divisor of Array

## Cpp

```cpp
class Solution {
public:
    int findGCD(vector<int>& nums) {
        int mn = nums[0], mx = nums[0];
        for (int v : nums) {
            if (v < mn) mn = v;
            if (v > mx) mx = v;
        }
        while (mx) {
            int r = mn % mx;
            mn = mx;
            mx = r;
        }
        return mn;
    }
};
```

## Java

```java
class Solution {
    public int findGCD(int[] nums) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int num : nums) {
            if (num < min) min = num;
            if (num > max) max = num;
        }
        return gcd(min, max);
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int tmp = a % b;
            a = b;
            b = tmp;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = min(nums)
        mx = max(nums)
        # Euclidean algorithm
        while mn:
            mn, mx = mx % mn, mn
        return mx
```

## Python3

```python
from typing import List
import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        return math.gcd(mn, mx)
```

## C

```c
int findGCD(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int mn = nums[0];
    int mx = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] < mn) mn = nums[i];
        if (nums[i] > mx) mx = nums[i];
    }
    while (mn != 0) {
        int temp = mx % mn;
        mx = mn;
        mn = temp;
    }
    return mx;
}
```

## Csharp

```csharp
public class Solution {
    public int FindGCD(int[] nums) {
        int mn = nums[0];
        int mx = nums[0];
        foreach (int v in nums) {
            if (v < mn) mn = v;
            if (v > mx) mx = v;
        }
        return Gcd(mn, mx);
    }

    private int Gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findGCD = function(nums) {
    let mn = nums[0], mx = nums[0];
    for (let i = 1; i < nums.length; i++) {
        const v = nums[i];
        if (v < mn) mn = v;
        else if (v > mx) mx = v;
    }
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    return gcd(mn, mx);
};
```

## Typescript

```typescript
function findGCD(nums: number[]): number {
    let mn = nums[0], mx = nums[0];
    for (const v of nums) {
        if (v < mn) mn = v;
        if (v > mx) mx = v;
    }
    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    return gcd(mn, mx);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findGCD($nums) {
        $mn = PHP_INT_MAX;
        $mx = 0;
        foreach ($nums as $num) {
            if ($num < $mn) $mn = $num;
            if ($num > $mx) $mx = $num;
        }
        return $this->gcd($mn, $mx);
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }
}
```

## Swift

```swift
class Solution {
    func findGCD(_ nums: [Int]) -> Int {
        var minVal = nums[0]
        var maxVal = nums[0]
        for num in nums {
            if num < minVal { minVal = num }
            if num > maxVal { maxVal = num }
        }
        func gcd(_ a: Int, _ b: Int) -> Int {
            var x = a
            var y = b
            while y != 0 {
                let temp = x % y
                x = y
                y = temp
            }
            return x
        }
        return gcd(minVal, maxVal)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findGCD(nums: IntArray): Int {
        var minVal = Int.MAX_VALUE
        var maxVal = Int.MIN_VALUE
        for (num in nums) {
            if (num < minVal) minVal = num
            if (num > maxVal) maxVal = num
        }
        return gcd(minVal, maxVal)
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val temp = x % y
            x = y
            y = temp
        }
        return kotlin.math.abs(x)
    }
}
```

## Dart

```dart
class Solution {
  int findGCD(List<int> nums) {
    int mn = nums[0];
    int mx = nums[0];
    for (int v in nums) {
      if (v < mn) mn = v;
      if (v > mx) mx = v;
    }
    int a = mn, b = mx;
    while (b != 0) {
      int temp = a % b;
      a = b;
      b = temp;
    }
    return a;
  }
}
```

## Golang

```go
func findGCD(nums []int) int {
	min, max := nums[0], nums[0]
	for _, v := range nums[1:] {
		if v < min {
			min = v
		}
		if v > max {
			max = v
		}
	}
	return gcd(min, max)
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
```

## Ruby

```ruby
def find_gcd(nums)
  mn = nums.min
  mx = nums.max
  a = mn
  b = mx
  while b != 0
    a, b = b, a % b
  end
  a
end
```

## Scala

```scala
object Solution {
    def findGCD(nums: Array[Int]): Int = {
        var mn = nums(0)
        var mx = nums(0)
        for (v <- nums) {
            if (v < mn) mn = v
            if (v > mx) mx = v
        }
        def gcd(a: Int, b: Int): Int = {
            if (b == 0) a else gcd(b, a % b)
        }
        gcd(mn, mx)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_gcd(nums: Vec<i32>) -> i32 {
        let mut min_val = nums[0];
        let mut max_val = nums[0];
        for &num in nums.iter().skip(1) {
            if num < min_val { min_val = num; }
            if num > max_val { max_val = num; }
        }
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let r = a % b;
                a = b;
                b = r;
            }
            a.abs()
        }
        gcd(min_val, max_val)
    }
}
```

## Racket

```racket
(define/contract (find-gcd nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([mn (apply min nums)]
         [mx (apply max nums)])
    (gcd mn mx)))
```

## Erlang

```erlang
-module(solution).
-export([find_gcd/1]).

-spec find_gcd(Nums :: [integer()]) -> integer().
find_gcd(Nums) ->
    Min = lists:min(Nums),
    Max = lists:max(Nums),
    gcd(Min, Max).

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_gcd(nums :: [integer]) :: integer
  def find_gcd([head | tail]) do
    {min_val, max_val} =
      Enum.reduce(tail, {head, head}, fn x, {cur_min, cur_max} ->
        {
          if x < cur_min, do: x, else: cur_min,
          if x > cur_max, do: x, else: cur_max
        }
      end)

    gcd(min_val, max_val)
  end

  defp gcd(a, 0), do: a
  defp gcd(a, b), do: gcd(b, rem(a, b))
end
```
