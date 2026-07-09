# 2447. Number of Subarrays With GCD Equal to K

## Cpp

```cpp
class Solution {
public:
    int subarrayGCD(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int g = 0;
            for (int j = i; j < n; ++j) {
                g = std::gcd(g, nums[j]);
                if (g == k) ++ans;
                if (g < k || g % k != 0) break;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int subarrayGCD(int[] nums, int k) {
        int n = nums.length;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] % k != 0) continue;
            int cur = nums[i];
            if (cur == k) ans++;
            for (int j = i + 1; j < n; j++) {
                if (nums[j] % k != 0) break;
                cur = gcd(cur, nums[j]);
                if (cur == k) {
                    ans++;
                } else if (cur < k) {
                    break;
                }
            }
        }
        return ans;
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
    def subarrayGCD(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import math
        n = len(nums)
        ans = 0
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur = math.gcd(cur, nums[j])
                if cur == k:
                    ans += 1
                # If current gcd is not a multiple of k, it can never become k later.
                if cur % k != 0:
                    break
        return ans
```

## Python3

```python
import math
from typing import List

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] % k != 0:
                continue
            cur_gcd = 0
            for j in range(i, n):
                if nums[j] % k != 0:
                    break
                cur_gcd = math.gcd(cur_gcd, nums[j])
                if cur_gcd == k:
                    ans += 1
                elif cur_gcd < k:
                    break
        return ans
```

## C

```c
int gcd_int(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int subarrayGCD(int* nums, int numsSize, int k) {
    int ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        int cur = 0;
        for (int j = i; j < numsSize; ++j) {
            cur = gcd_int(cur, nums[j]);
            if (cur == k) {
                ++ans;
            }
            if (cur < k || cur % k != 0) {
                break;
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int SubarrayGCD(int[] nums, int k)
    {
        int n = nums.Length;
        int result = 0;

        for (int i = 0; i < n; i++)
        {
            int currentGcd = 0;
            for (int j = i; j < n; j++)
            {
                currentGcd = Gcd(currentGcd, nums[j]);

                if (currentGcd == k)
                    result++;
                else if (currentGcd < k)
                    break;
            }
        }

        return result;
    }

    private int Gcd(int a, int b)
    {
        while (b != 0)
        {
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
 * @param {number} k
 * @return {number}
 */
var subarrayGCD = function(nums, k) {
    const n = nums.length;
    let count = 0;

    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    for (let i = 0; i < n; ++i) {
        let g = 0;
        for (let j = i; j < n; ++j) {
            g = gcd(g, nums[j]);
            if (g === k) {
                ++count;
            }
            // If further extension cannot reach k, break early
            if (g < k || g % k !== 0) {
                break;
            }
        }
    }

    return count;
};
```

## Typescript

```typescript
function gcd(a: number, b: number): number {
    while (b !== 0) {
        const t = a % b;
        a = b;
        b = t;
    }
    return Math.abs(a);
}

function subarrayGCD(nums: number[], k: number): number {
    let ans = 0;
    const n = nums.length;
    for (let i = 0; i < n; ++i) {
        let g = 0;
        for (let j = i; j < n; ++j) {
            g = g === 0 ? nums[j] : gcd(g, nums[j]);
            if (g === k) {
                ans++;
            } else if (g < k) {
                break;
            }
        }
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function subarrayGCD($nums, $k) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $g = 0;
            for ($j = $i; $j < $n; $j++) {
                $g = self::gcd($g, $nums[$j]);
                if ($g == $k) {
                    $ans++;
                }
                if ($g < $k) {
                    break;
                }
            }
        }
        return $ans;
    }

    private static function gcd($a, $b) {
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
    func subarrayGCD(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var result = 0
        
        func gcd(_ a: Int, _ b: Int) -> Int {
            var x = a
            var y = b
            while y != 0 {
                let temp = x % y
                x = y
                y = temp
            }
            return abs(x)
        }
        
        for i in 0..<n {
            var currentGCD = 0
            for j in i..<n {
                currentGCD = gcd(currentGCD, nums[j])
                if currentGCD == k {
                    result += 1
                }
                if currentGCD < k || (currentGCD % k != 0) {
                    break
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun subarrayGCD(nums: IntArray, k: Int): Int {
        var count = 0
        val n = nums.size
        for (i in 0 until n) {
            var g = 0
            for (j in i until n) {
                g = gcd(g, nums[j])
                if (g == k) {
                    count++
                }
                if (g < k) break
            }
        }
        return count
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
  int subarrayGCD(List<int> nums, int k) {
    int n = nums.length;
    int count = 0;

    int _gcd(int a, int b) {
      while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
      }
      return a;
    }

    for (int i = 0; i < n; ++i) {
      if (nums[i] % k != 0) continue;
      int cur = nums[i];
      for (int j = i; j < n; ++j) {
        if (nums[j] % k != 0) break;
        cur = _gcd(cur, nums[j]);
        if (cur == k) {
          count++;
        } else if (cur < k) {
          break;
        }
      }
    }

    return count;
  }
}
```

## Golang

```go
func subarrayGCD(nums []int, k int) int {
    gcd := func(a, b int) int {
        for b != 0 {
            a, b = b, a%b
        }
        if a < 0 {
            return -a
        }
        return a
    }

    count := 0
    n := len(nums)
    for i := 0; i < n; i++ {
        cur := 0
        for j := i; j < n; j++ {
            cur = gcd(cur, nums[j])
            if cur == k {
                count++
            }
            if cur < k || cur%k != 0 {
                break
            }
        }
    }
    return count
}
```

## Ruby

```ruby
def subarray_gcd(nums, k)
  n = nums.length
  count = 0
  (0...n).each do |i|
    g = 0
    (i...n).each do |j|
      g = g.gcd(nums[j])
      count += 1 if g == k
      break if g < k
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def subarrayGCD(nums: Array[Int], k: Int): Int = {
        var count = 0
        val n = nums.length
        for (i <- 0 until n) {
            var g = 0
            var j = i
            var keepGoing = true
            while (j < n && keepGoing) {
                g = gcd(g, nums(j))
                if (g == k) {
                    count += 1
                } else if (g < k) {
                    keepGoing = false
                }
                j += 1
            }
        }
        count
    }

    private def gcd(a: Int, b: Int): Int = {
        var x = math.abs(a)
        var y = math.abs(b)
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        x
    }
}
```

## Rust

```rust
impl Solution {
    pub fn subarray_gcd(nums: Vec<i32>, k: i32) -> i32 {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a.abs()
        }

        let n = nums.len();
        let mut ans: i32 = 0;
        for i in 0..n {
            let mut g = 0i32;
            for j in i..n {
                g = gcd(g, nums[j]);
                if g == k {
                    ans += 1;
                }
                if g < k || (g % k != 0) {
                    break;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (subarray-gcd nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums)))
    (let loop-i ((i 0) (total 0))
      (if (= i n)
          total
          (let loop-j ((j i) (cur 0) (cnt total))
            (if (= j n)
                (loop-i (+ i 1) cnt)
                (let ((new-gcd (gcd cur (vector-ref vec j))))
                  (cond
                    [(= new-gcd k)
                     (loop-j (+ j 1) new-gcd (+ cnt 1))]
                    [(or (< new-gcd k) (not (zero? (remainder new-gcd k))))
                     (loop-i (+ i 1) cnt)]
                    [else
                     (loop-j (+ j 1) new-gcd cnt)])))))))))
```

## Erlang

```erlang
-module(solution).
-export([subarray_gcd/2]).

-spec subarray_gcd(Nums :: [integer()], K :: integer()) -> integer().
subarray_gcd(Nums, K) ->
    subarray_gcd_start(Nums, K, 0).

subarray_gcd_start([], _K, Acc) -> Acc;
subarray_gcd_start([_|Rest]=List, K, Acc) ->
    Count = subarray_gcd_extend(List, K, 0),
    subarray_gcd_start(Rest, K, Acc + Count).

subarray_gcd_extend([], _K, _CurrentGcd) -> 0;
subarray_gcd_extend([X|Xs], K, CurrentGcd) ->
    NewGcd = case CurrentGcd of
        0 -> X;
        _ -> erlang:gcd(CurrentGcd, X)
    end,
    Add = if NewGcd == K -> 1; true -> 0 end,
    Add + subarray_gcd_extend(Xs, K, NewGcd).
```

## Elixir

```elixir
defmodule Solution do
  @spec subarray_gcd(nums :: [integer], k :: integer) :: integer
  def subarray_gcd(nums, k) do
    len = length(nums)

    0..(len - 1)
    |> Enum.reduce(0, fn i, total ->
      {cnt, _} =
        Enum.reduce_while(i..(len - 1), {0, 0}, fn j, {c, cur_gcd} ->
          new_gcd = Integer.gcd(cur_gcd, Enum.at(nums, j))

          cond do
            new_gcd == k -> {:cont, {c + 1, new_gcd}}
            new_gcd < k -> {:halt, {c, new_gcd}}
            true -> {:cont, {c, new_gcd}}
          end
        end)

      total + cnt
    end)
  end
end
```
