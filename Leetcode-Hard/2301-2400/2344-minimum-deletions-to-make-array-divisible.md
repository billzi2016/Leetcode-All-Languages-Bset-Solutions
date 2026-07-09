# 2344. Minimum Deletions to Make Array Divisible

## Cpp

```cpp
class Solution {
public:
    int minOperations(std::vector<int>& nums, std::vector<int>& numsDivide) {
        long long g = 0;
        for (int x : numsDivide) {
            g = std::gcd(g, static_cast<long long>(x));
        }
        std::sort(nums.begin(), nums.end());
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (g % nums[i] == 0) return i;
        }
        return -1;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minOperations(int[] nums, int[] numsDivide) {
        int g = 0;
        for (int v : numsDivide) {
            g = gcd(g, v);
        }
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; ++i) {
            if (g % nums[i] == 0) {
                return i;
            }
        }
        return -1;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums, numsDivide):
        """
        :type nums: List[int]
        :type numsDivide: List[int]
        :rtype: int
        """
        import math
        # Compute GCD of all elements in numsDivide
        g = 0
        for v in numsDivide:
            g = math.gcd(g, v)
        # Sort nums to consider candidates from smallest to largest
        nums.sort()
        deletions = 0
        for i, val in enumerate(nums):
            if g % val == 0:
                return i  # number of elements before this index are deleted
        return -1
```

## Python3

```python
from typing import List
import math

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = 0
        for v in numsDivide:
            g = math.gcd(g, v)
        nums.sort()
        deletions = 0
        for val in nums:
            if g % val == 0:
                return deletions
            deletions += 1
        return -1
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

static long long gcd_ll(long long a, long long b) {
    while (b) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int minOperations(int* nums, int numsSize, int* numsDivide, int numsDivideSize) {
    if (numsSize == 0 || numsDivideSize == 0) return -1;

    long long g = numsDivide[0];
    for (int i = 1; i < numsDivideSize; ++i) {
        g = gcd_ll(g, numsDivide[i]);
    }

    qsort(nums, numsSize, sizeof(int), cmp_int);

    int i = 0;
    while (i < numsSize) {
        int val = nums[i];
        if (g % val == 0) {
            return i; // delete all elements before this distinct value
        }
        while (i < numsSize && nums[i] == val) ++i; // skip duplicates
    }

    return -1;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinOperations(int[] nums, int[] numsDivide)
    {
        long g = 0;
        foreach (int v in numsDivide)
        {
            if (g == 0) g = v;
            else g = Gcd(g, v);
        }

        Array.Sort(nums);
        for (int i = 0; i < nums.Length; i++)
        {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            if (g % nums[i] == 0) return i;
        }
        return -1;
    }

    private long Gcd(long a, long b)
    {
        while (b != 0)
        {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} numsDivide
 * @return {number}
 */
var minOperations = function(nums, numsDivide) {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    
    let g = numsDivide[0];
    for (let i = 1; i < numsDivide.length; ++i) {
        g = gcd(g, numsDivide[i]);
    }
    
    nums.sort((a, b) => a - b);
    
    for (let i = 0; i < nums.length; ++i) {
        if (g % nums[i] === 0) return i;
    }
    return -1;
};
```

## Typescript

```typescript
function minOperations(nums: number[], numsDivide: number[]): number {
    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    
    let g = numsDivide[0];
    for (let i = 1; i < numsDivide.length; ++i) {
        g = gcd(g, numsDivide[i]);
    }
    
    nums.sort((a, b) => a - b);
    for (let i = 0; i < nums.length; ++i) {
        if (g % nums[i] === 0) return i;
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $numsDivide
     * @return Integer
     */
    function minOperations($nums, $numsDivide) {
        // Compute GCD of all elements in numsDivide
        $g = $numsDivide[0];
        foreach ($numsDivide as $v) {
            $g = $this->gcd($g, $v);
        }

        sort($nums);
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($g % $nums[$i] === 0) {
                return $i;
            }
        }
        return -1;
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
    func minOperations(_ nums: [Int], _ numsDivide: [Int]) -> Int {
        var g = 0
        for v in numsDivide {
            g = gcd(g, v)
        }
        let sortedNums = nums.sorted()
        for (i, val) in sortedNums.enumerated() {
            if g % val == 0 {
                return i
            }
        }
        return -1
    }
    
    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a
        var y = b
        while y != 0 {
            let temp = x % y
            x = y
            y = temp
        }
        return x
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray, numsDivide: IntArray): Int {
        var g = 0
        for (v in numsDivide) {
            g = gcd(g, v)
        }
        val sorted = nums.sorted()
        for ((i, v) in sorted.withIndex()) {
            if (g % v == 0) return i
        }
        return -1
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = kotlin.math.abs(a)
        var y = kotlin.math.abs(b)
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return x
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums, List<int> numsDivide) {
    int g = numsDivide[0];
    for (int i = 1; i < numsDivide.length; ++i) {
      g = _gcd(g, numsDivide[i]);
    }
    nums.sort();
    for (int i = 0; i < nums.length; ++i) {
      if (g % nums[i] == 0) return i;
    }
    return -1;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int t = a % b;
      a = b;
      b = t;
    }
    return a.abs();
  }
}
```

## Golang

```go
func minOperations(nums []int, numsDivide []int) int {
    // compute GCD of all elements in numsDivide
    g := numsDivide[0]
    for _, x := range numsDivide[1:] {
        g = gcd(g, x)
    }

    sort.Ints(nums)

    deletions := 0
    prev := -1
    for _, v := range nums {
        if v != prev {
            if g%v == 0 {
                return deletions
            }
            prev = v
        }
        deletions++
    }
    return -1
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
def min_operations(nums, nums_divide)
  g = nums_divide.reduce(0) { |acc, x| acc.gcd(x) }
  nums.sort!
  nums.each_with_index do |v, i|
    return i if g % v == 0
  end
  -1
end
```

## Scala

```scala
object Solution {
  def minOperations(nums: Array[Int], numsDivide: Array[Int]): Int = {
    // Compute GCD of all elements in numsDivide
    var g = 0L
    for (v <- numsDivide) {
      g = if (g == 0) v.toLong else gcd(g, v.toLong)
    }

    val sorted = nums.sorted
    var i = 0
    while (i < sorted.length) {
      val value = sorted(i).toLong
      if (g % value == 0) return i

      // skip duplicates of the current value
      var j = i + 1
      while (j < sorted.length && sorted(j) == sorted(i)) {
        j += 1
      }
      i = j
    }
    -1
  }

  private def gcd(a: Long, b: Long): Long = {
    if (b == 0) a else gcd(b, a % b)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>, nums_divide: Vec<i32>) -> i32 {
        // Compute GCD of all elements in nums_divide
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let r = a % b;
                a = b;
                b = r;
            }
            a.abs()
        }

        let mut g = nums_divide[0];
        for &v in nums_divide.iter().skip(1) {
            g = gcd(g, v);
        }

        // Sort nums to consider candidates from smallest to largest
        let mut sorted = nums.clone();
        sorted.sort_unstable();

        let n = sorted.len();
        let mut i = 0usize;
        let mut deletions: i32 = 0;

        while i < n {
            let val = sorted[i];
            if g % val == 0 {
                return deletions;
            }
            // skip all occurrences of the current value and count them as deletions
            let mut j = i + 1;
            while j < n && sorted[j] == val {
                j += 1;
            }
            deletions += (j - i) as i32;
            i = j;
        }

        -1
    }
}
```

## Racket

```racket
(define/contract (min-operations nums numsDivide)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((g (apply gcd numsDivide))
         (sorted (sort nums <)))
    (let loop ((lst sorted) (idx 0))
      (cond
        [(null? lst) -1]
        [else (if (zero? (modulo g (car lst)))
                  idx
                  (loop (cdr lst) (+ idx 1)))]))))
```

## Erlang

```erlang
-module(solution).
-export([min_operations/2]).

-spec min_operations(Nums :: [integer()], NumsDivide :: [integer()]) -> integer().
min_operations(Nums, NumsDivide) ->
    G = gcd_list(NumsDivide),
    Sorted = lists:sort(Nums),
    find_deletions(Sorted, G, 0).

gcd(A, B) when B =:= 0 -> A;
gcd(A, B) -> gcd(B, A rem B).

gcd_list([H|T]) ->
    lists:foldl(fun(X, Acc) -> gcd(Acc, X) end, H, T);
gcd_list([]) -> 0.

find_deletions([], _G, _Idx) -> -1;
find_deletions([H|T], G, Idx) ->
    case G rem H of
        0 -> Idx;
        _ -> find_deletions(T, G, Idx + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer], nums_divide :: [integer]) :: integer
  def min_operations(nums, nums_divide) do
    target_gcd = Enum.reduce(nums_divide, 0, fn x, acc -> Integer.gcd(acc, x) end)
    sorted_nums = Enum.sort(nums)
    find_min_deletions(sorted_nums, target_gcd, 0)
  end

  defp find_min_deletions([], _gcd, _idx), do: -1

  defp find_min_deletions([h | t], gcd, idx) do
    if rem(gcd, h) == 0 do
      idx
    else
      find_min_deletions(t, gcd, idx + 1)
    end
  end
end
```
