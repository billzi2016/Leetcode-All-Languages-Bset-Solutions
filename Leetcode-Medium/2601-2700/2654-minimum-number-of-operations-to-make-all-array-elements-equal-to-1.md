# 2654. Minimum Number of Operations to Make All Array Elements Equal to 1

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        int cnt1 = 0;
        for (int x : nums) if (x == 1) ++cnt1;
        if (cnt1 > 0) return n - cnt1;
        
        int best = INT_MAX;
        for (int i = 0; i < n; ++i) {
            int g = 0;
            for (int j = i; j < n; ++j) {
                g = std::gcd(g, nums[j]);
                if (g == 1) {
                    best = min(best, j - i + 1);
                    break;
                }
            }
        }
        if (best == INT_MAX) return -1;
        return (best - 1) + (n - 1);
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums) {
        int n = nums.length;
        int ones = 0;
        for (int v : nums) if (v == 1) ones++;
        if (ones > 0) return n - ones;

        int minLen = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int g = nums[i];
            for (int j = i + 1; j < n; j++) {
                g = gcd(g, nums[j]);
                if (g == 1) {
                    minLen = Math.min(minLen, j - i + 1);
                    break;
                }
            }
        }

        if (minLen == Integer.MAX_VALUE) return -1;
        return (minLen - 1) + (n - 1);
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
import math

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ones = sum(1 for x in nums if x == 1)
        if ones:
            return n - ones

        best = n + 1
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    best = min(best, j - i + 1)
                    break

        if best == n + 1:
            return -1
        # (best-1) ops to create a 1, then (n-1) ops to turn all others into 1
        return (best - 1) + (n - 1)
```

## Python3

```python
from typing import List
import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        cnt_one = nums.count(1)
        if cnt_one:
            return n - cnt_one

        min_len = float('inf')
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        if min_len == float('inf'):
            return -1

        # (min_len-1) to create a 1, then (n-1) to turn all others into 1
        return (min_len - 1) + (n - 1)
```

## C

```c
#include <limits.h>

static int gcd_int(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int minOperations(int* nums, int numsSize) {
    int countOnes = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 1) countOnes++;
    }
    if (countOnes > 0) {
        return numsSize - countOnes;
    }

    int minLen = INT_MAX;
    for (int i = 0; i < numsSize; ++i) {
        int curGcd = nums[i];
        for (int j = i; j < numsSize; ++j) {
            curGcd = gcd_int(curGcd, nums[j]);
            if (curGcd == 1) {
                int len = j - i + 1;
                if (len < minLen) minLen = len;
                break;
            }
        }
    }

    if (minLen == INT_MAX) return -1;
    return minLen + numsSize - 2;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinOperations(int[] nums)
    {
        int n = nums.Length;
        int ones = 0;
        foreach (int v in nums)
            if (v == 1) ones++;

        if (ones > 0)
            return n - ones;

        int minLen = int.MaxValue;
        for (int i = 0; i < n; i++)
        {
            int g = nums[i];
            for (int j = i; j < n; j++)
            {
                g = Gcd(g, nums[j]);
                if (g == 1)
                {
                    int len = j - i + 1;
                    if (len < minLen) minLen = len;
                    break;
                }
            }
        }

        if (minLen == int.MaxValue)
            return -1;

        // (minLen-1) to create a 1, then (n-1) to turn the rest into 1
        return (minLen - 1) + (n - 1);
    }

    private int Gcd(int a, int b)
    {
        while (b != 0)
        {
            int t = a % b;
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
 * @return {number}
 */
var minOperations = function(nums) {
    const n = nums.length;
    let ones = 0;
    for (const v of nums) if (v === 1) ++ones;
    if (ones > 0) return n - ones;

    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    let minLen = Infinity;
    for (let i = 0; i < n; ++i) {
        let g = 0;
        for (let j = i; j < n; ++j) {
            g = gcd(g, nums[j]);
            if (g === 1) {
                minLen = Math.min(minLen, j - i + 1);
                break;
            }
        }
    }

    if (minLen === Infinity) return -1;
    return minLen + n - 2;
};
```

## Typescript

```typescript
function minOperations(nums: number[]): number {
    const n = nums.length;
    let ones = 0;
    for (const v of nums) if (v === 1) ++ones;
    if (ones > 0) return n - ones;

    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    let minLen = Infinity;
    for (let i = 0; i < n; ++i) {
        let g = nums[i];
        if (g === 1) {
            minLen = 1;
            break;
        }
        for (let j = i + 1; j < n; ++j) {
            g = gcd(g, nums[j]);
            if (g === 1) {
                const len = j - i + 1;
                if (len < minLen) minLen = len;
                break;
            }
        }
    }

    if (!isFinite(minLen)) return -1;
    return (minLen - 1) + (n - 1);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minOperations($nums) {
        $n = count($nums);
        $cnt1 = 0;
        foreach ($nums as $v) {
            if ($v == 1) $cnt1++;
        }
        if ($cnt1 > 0) {
            return $n - $cnt1;
        }

        // helper gcd
        $gcd = function($a, $b) {
            while ($b != 0) {
                $tmp = $a % $b;
                $a = $b;
                $b = $tmp;
            }
            return $a;
        };

        $minLen = PHP_INT_MAX;
        for ($i = 0; $i < $n; $i++) {
            $currentGcd = $nums[$i];
            if ($currentGcd == 1) {
                $minLen = 1;
                break;
            }
            for ($j = $i + 1; $j < $n; $j++) {
                $currentGcd = $gcd($currentGcd, $nums[$j]);
                if ($currentGcd == 1) {
                    $len = $j - $i + 1;
                    if ($len < $minLen) $minLen = $len;
                    break; // no need to extend further for this i
                }
            }
        }

        if ($minLen == PHP_INT_MAX) return -1;

        // operations: (minLen-1) to create a 1, then (n-1) to spread it
        return $minLen + $n - 2;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        var onesCount = 0
        for v in nums where v == 1 { onesCount += 1 }
        if onesCount > 0 {
            return n - onesCount
        }
        var minLen = Int.max
        for i in 0..<n {
            var g = nums[i]
            if g == 1 {
                minLen = 1
                break
            }
            for j in (i + 1)..<n {
                g = gcd(g, nums[j])
                if g == 1 {
                    let len = j - i + 1
                    if len < minLen { minLen = len }
                    break
                }
            }
        }
        if minLen == Int.max {
            return -1
        }
        // (minLen - 1) ops to create a 1, then (n - 1) ops to turn the rest into 1s.
        return (minLen - 1) + (n - 1)
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
    fun minOperations(nums: IntArray): Int {
        val n = nums.size
        var countOnes = 0
        for (v in nums) if (v == 1) countOnes++
        if (countOnes > 0) return n - countOnes

        var best = Int.MAX_VALUE
        for (i in 0 until n) {
            var g = nums[i]
            for (j in i + 1 until n) {
                g = gcd(g, nums[j])
                if (g == 1) {
                    val len = j - i + 1
                    if (len < best) best = len
                    break
                }
            }
        }

        return if (best == Int.MAX_VALUE) -1 else n + best - 2
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return kotlin.math.abs(x)
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums) {
    int n = nums.length;
    int countOnes = 0;
    for (int v in nums) {
      if (v == 1) countOnes++;
    }
    if (countOnes > 0) {
      return n - countOnes;
    }

    int minLen = n + 1; // larger than any possible subarray
    for (int i = 0; i < n; i++) {
      int g = nums[i];
      for (int j = i; j < n; j++) {
        g = _gcd(g, nums[j]);
        if (g == 1) {
          minLen = (j - i + 1).clamp(0, minLen);
          break;
        }
      }
    }

    if (minLen == n + 1) return -1;
    // (minLen - 1) operations to create a 1, then (n - 1) more to spread it
    return minLen + n - 2;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int t = a % b;
      a = b;
      b = t;
    }
    return a;
  }
}
```

## Golang

```go
func minOperations(nums []int) int {
    n := len(nums)
    ones := 0
    for _, v := range nums {
        if v == 1 {
            ones++
        }
    }
    if ones > 0 {
        return n - ones
    }

    // overall gcd
    g := nums[0]
    for i := 1; i < n; i++ {
        g = gcd(g, nums[i])
    }
    if g != 1 {
        return -1
    }

    minLen := n + 1
    for i := 0; i < n; i++ {
        cur := nums[i]
        for j := i; j < n; j++ {
            if j > i {
                cur = gcd(cur, nums[j])
            }
            if cur == 1 {
                length := j - i + 1
                if length < minLen {
                    minLen = length
                }
                break
            }
        }
    }

    return minLen + n - 2
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
def min_operations(nums)
  n = nums.length
  cnt_one = nums.count(1)
  return n - cnt_one if cnt_one > 0

  inf = 1 << 60
  min_len = inf

  (0...n).each do |i|
    g = 0
    (i...n).each do |j|
      g = g.gcd(nums[j])
      if g == 1
        len = j - i + 1
        min_len = len if len < min_len
        break
      end
    end
  end

  return -1 if min_len == inf
  min_len + n - 2
end
```

## Scala

```scala
object Solution {
  private def gcd(a: Int, b: Int): Int = {
    var x = a
    var y = b
    while (y != 0) {
      val t = x % y
      x = y
      y = t
    }
    x
  }

  def minOperations(nums: Array[Int]): Int = {
    val n = nums.length
    val ones = nums.count(_ == 1)
    if (ones > 0) return n - ones

    var minLen = Int.MaxValue
    for (i <- 0 until n) {
      var cur = nums(i)
      for (j <- i until n) {
        cur = gcd(cur, nums(j))
        if (cur == 1) {
          val len = j - i + 1
          if (len < minLen) minLen = len
        }
      }
    }

    if (minLen == Int.MaxValue) -1 else minLen + n - 2
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a.abs()
        }

        // overall gcd check
        let overall_gcd = nums.iter().fold(0, |acc, &x| if acc == 0 { x } else { gcd(acc, x) });
        if overall_gcd != 1 {
            return -1;
        }

        // if there is already a 1
        let cnt_one = nums.iter().filter(|&&x| x == 1).count();
        if cnt_one > 0 {
            return (n - cnt_one) as i32;
        }

        // find shortest subarray with gcd 1
        let mut min_len = n + 1;
        for i in 0..n {
            let mut cur = nums[i];
            if cur == 1 {
                min_len = 1;
                break;
            }
            for j in (i + 1)..n {
                cur = gcd(cur, nums[j]);
                if cur == 1 {
                    let len = j - i + 1;
                    if len < min_len {
                        min_len = len;
                    }
                    break;
                }
            }
        }

        // total operations: (min_len-1) to create a 1, then (n-1) to spread it
        ((min_len + n) as i32) - 2
    }
}
```

## Racket

```racket
(define/contract (min-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (cnt1 (for/sum ([x nums]) (if (= x 1) 1 0))))
    (cond
      [(> cnt1 0) (- n cnt1)]
      [else
       (define best (expt 2 30)) ; large initial value
       (for ([i (in-range n)])
         (let ((g (list-ref nums i)))
           (for ([j (in-range (add1 i) n)])
             (set! g (gcd g (list-ref nums j)))
             (when (= g 1)
               (set! best (min best (+ (- j i) 1)))))))
       (if (> best (expt 2 29)) ; still large, no subarray with gcd 1
           -1
           (+ (- best 1) (- n 1)))])))
```

## Erlang

```erlang
-module(solution).
-export([min_operations/1]).

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).

count_ones([], Acc) -> Acc;
count_ones([H|T], Acc) ->
    NewAcc = case H of
        1 -> Acc + 1;
        _ -> Acc
    end,
    count_ones(T, NewAcc).

min_operations(Nums) ->
    N = length(Nums),
    CountOnes = count_ones(Nums, 0),
    case CountOnes > 0 of
        true -> N - CountOnes;
        false ->
            MinLen = find_min_subarray(Nums),
            case MinLen of
                undefined -> -1;
                L -> L + N - 2
            end
    end.

find_min_subarray(Nums) ->
    Tuple = list_to_tuple(Nums),
    N = tuple_size(Tuple),
    find_min_subarray(0, N, Tuple, undefined).

find_min_subarray(I, N, _Tuple, Min) when I >= N -> Min;
find_min_subarray(I, N, Tuple, Min) ->
    NewMin = inner_gcd(I, I, N, Tuple, 0, Min),
    find_min_subarray(I + 1, N, Tuple, NewMin).

inner_gcd(_Start, J, N, _Tuple, _CurrGcd, Min) when J >= N -> Min;
inner_gcd(Start, J, N, Tuple, CurrGcd, Min) ->
    Val = element(J + 1, Tuple),
    NewGcd = case CurrGcd of
        0 -> Val;
        _ -> gcd(CurrGcd, Val)
    end,
    case NewGcd of
        1 ->
            Len = J - Start + 1,
            UpdatedMin = case Min of
                undefined -> Len;
                _ when Len < Min -> Len;
                _ -> Min
            end,
            UpdatedMin; % stop inner loop after finding gcd 1
        _ ->
            inner_gcd(Start, J + 1, N, Tuple, NewGcd, Min)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer]) :: integer
  def min_operations(nums) do
    n = length(nums)
    cnt_one = Enum.count(nums, fn x -> x == 1 end)

    if cnt_one > 0 do
      n - cnt_one
    else
      max_len = n + 1

      min_len =
        Enum.reduce(0..(n - 1), max_len, fn i, best ->
          {_, len} =
            Enum.reduce_while(i..(n - 1), {0, nil}, fn j, {curr_gcd, _} ->
              new_gcd = Integer.gcd(curr_gcd, Enum.at(nums, j))

              if new_gcd == 1 do
                {:halt, {new_gcd, j - i + 1}}
              else
                {:cont, {new_gcd, nil}}
              end
            end)

          case len do
            nil -> best
            l when l < best -> l
            _ -> best
          end
        end)

      if min_len == max_len do
        -1
      else
        min_len + n - 2
      end
    end
  end
end
```
