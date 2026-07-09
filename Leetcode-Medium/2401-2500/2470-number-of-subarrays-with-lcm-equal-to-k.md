# 2470. Number of Subarrays With LCM Equal to K

## Cpp

```cpp
class Solution {
public:
    int subarrayLCM(vector<int>& nums, int k) {
        int n = nums.size();
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            long long cur = 1;
            for (int j = i; j < n; ++j) {
                long long g = std::gcd(cur, (long long)nums[j]);
                cur = cur / g * nums[j];
                if (cur > k) break;
                if (cur == k) ++ans;
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int subarrayLCM(int[] nums, int k) {
        int n = nums.length;
        int count = 0;
        for (int i = 0; i < n; i++) {
            long lcm = 1;
            for (int j = i; j < n; j++) {
                lcm = lcm(lcm, nums[j]);
                if (lcm > k) break;
                if (lcm == k) count++;
            }
        }
        return count;
    }

    private long lcm(long a, long b) {
        return a / gcd(a, b) * b;
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long tmp = a % b;
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
    def subarrayLCM(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import math
        n = len(nums)
        ans = 0
        for i in range(n):
            cur = 1
            for j in range(i, n):
                g = math.gcd(cur, nums[j])
                cur = cur // g * nums[j]
                if cur > k or k % cur != 0:
                    break
                if cur == k:
                    ans += 1
        return ans
```

## Python3

```python
from typing import List
from math import gcd

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            if k % nums[i] != 0:
                continue
            lcm_val = 1
            for j in range(i, n):
                if k % nums[j] != 0:
                    break
                # compute lcm(lcm_val, nums[j])
                g = gcd(lcm_val, nums[j])
                lcm_val = lcm_val // g * nums[j]
                if lcm_val > k:
                    break
                if lcm_val == k:
                    ans += 1
        return ans
```

## C

```c
int gcd_long(long long a, long long b) {
    while (b) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return (int)a;
}

int subarrayLCM(int* nums, int numsSize, int k) {
    int count = 0;
    for (int i = 0; i < numsSize; ++i) {
        long long lcm = 1;
        for (int j = i; j < numsSize; ++j) {
            long long g = gcd_long(lcm, (long long)nums[j]);
            lcm = lcm / g * nums[j];
            if (lcm > k) break;
            if (lcm == k) ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int SubarrayLCM(int[] nums, int k) {
        long count = 0;
        int n = nums.Length;
        for (int i = 0; i < n; i++) {
            long lcm = 1;
            for (int j = i; j < n; j++) {
                lcm = Lcm(lcm, nums[j]);
                if (lcm > k) break;
                if (lcm == k) count++;
            }
        }
        return (int)count;
    }

    private static long Gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    private static long Lcm(long a, long b) {
        if (a == 0 || b == 0) return 0;
        long g = Gcd(a, b);
        // To avoid overflow, divide before multiply
        return a / g * b;
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
var subarrayLCM = function(nums, k) {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const lcm = (a, b) => {
        if (a === 0 || b === 0) return 0;
        return (a / gcd(a, b)) * b;
    };

    let count = 0;
    const n = nums.length;

    for (let i = 0; i < n; ++i) {
        let cur = 1;
        for (let j = i; j < n; ++j) {
            cur = lcm(cur, nums[j]);
            if (cur > k) break;
            if (cur === k) ++count;
        }
    }

    return count;
};
```

## Typescript

```typescript
function subarrayLCM(nums: number[], k: number): number {
    const n = nums.length;
    let ans = 0;

    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    const lcm = (a: number, b: number): number => {
        if (a === 0 || b === 0) return 0;
        return (a / gcd(a, b)) * b;
    };

    for (let i = 0; i < n; i++) {
        let cur = 1;
        for (let j = i; j < n; j++) {
            cur = lcm(cur, nums[j]);
            if (cur > k) break;
            if (cur === k) ans++;
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
    function subarrayLCM($nums, $k) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $curr = 1;
            for ($j = $i; $j < $n; $j++) {
                $curr = $this->lcm($curr, $nums[$j]);
                if ($curr == $k) {
                    $ans++;
                }
                if ($curr > $k) {
                    break;
                }
            }
        }
        return $ans;
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }

    private function lcm($a, $b) {
        if ($a == 0 || $b == 0) return 0;
        $g = $this->gcd($a, $b);
        return (int)($a / $g) * $b;
    }
}
```

## Swift

```swift
class Solution {
    func subarrayLCM(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var result = 0
        for i in 0..<n {
            var currentLCM = 1
            for j in i..<n {
                let a = currentLCM
                let b = nums[j]
                let g = gcd(a, b)
                // compute lcm using Int64 to avoid overflow
                let newLCM = (Int64(a) / Int64(g)) * Int64(b)
                if newLCM > Int64(k) {
                    break
                }
                currentLCM = Int(newLCM)
                if currentLCM == k {
                    result += 1
                }
            }
        }
        return result
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
    fun subarrayLCM(nums: IntArray, k: Int): Int {
        var count = 0
        val target = k.toLong()
        for (i in nums.indices) {
            var cur = 1L
            for (j in i until nums.size) {
                cur = lcm(cur, nums[j].toLong())
                if (cur > target) break
                if (cur == target) count++
            }
        }
        return count
    }

    private fun gcd(a: Long, b: Long): Long {
        var x = a
        var y = b
        while (y != 0L) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return kotlin.math.abs(x)
    }

    private fun lcm(a: Long, b: Long): Long {
        if (a == 0L || b == 0L) return 0L
        val g = gcd(a, b)
        // Since values are small, overflow is not a concern for valid results.
        return a / g * b
    }
}
```

## Dart

```dart
class Solution {
  int subarrayLCM(List<int> nums, int k) {
    int n = nums.length;
    int ans = 0;

    int gcd(int a, int b) {
      while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
      }
      return a;
    }

    int lcm(int a, int b) {
      return a ~/ gcd(a, b) * b;
    }

    for (int i = 0; i < n; ++i) {
      if (k % nums[i] != 0) continue;
      int cur = 1;
      for (int j = i; j < n; ++j) {
        if (k % nums[j] != 0) break;
        cur = lcm(cur, nums[j]);
        if (cur > k) break;
        if (cur == k) ans++;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func subarrayLCM(nums []int, k int) int {
	n := len(nums)
	ans := 0
	for i := 0; i < n; i++ {
		cur := 1
		for j := i; j < n; j++ {
			g := gcd(cur, nums[j])
			l := int(int64(cur/g) * int64(nums[j]))
			if l > k {
				break
			}
			cur = l
			if cur == k {
				ans++
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def subarray_lcm(nums, k)
  n = nums.length
  count = 0
  (0...n).each do |i|
    cur = 1
    (i...n).each do |j|
      cur = cur.lcm(nums[j])
      break if cur > k
      count += 1 if cur == k
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def subarrayLCM(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        var count = 0
        for (i <- 0 until n) {
            var lcmVal: Long = 1L
            var j = i
            var keepGoing = true
            while (j < n && keepGoing) {
                val a = nums(j).toLong
                // gcd of lcmVal and a
                var x = lcmVal
                var y = a
                while (y != 0) {
                    val tmp = x % y
                    x = y
                    y = tmp
                }
                val g = x
                lcmVal = lcmVal / g * a
                if (lcmVal == k) {
                    count += 1
                } else if (lcmVal > k) {
                    keepGoing = false
                }
                j += 1
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn subarray_lcm(nums: Vec<i32>, k: i32) -> i32 {
        fn gcd(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                let r = a % b;
                a = b;
                b = r;
            }
            a
        }

        let n = nums.len();
        let target = k as i64;
        let mut ans: i32 = 0;

        for i in 0..n {
            let mut cur_lcm: i64 = 1;
            for j in i..n {
                let val = nums[j] as i64;
                let g = gcd(cur_lcm, val);
                // avoid overflow; if intermediate exceeds target we can break early
                cur_lcm = cur_lcm / g * val;
                if cur_lcm > target {
                    break;
                }
                if cur_lcm == target {
                    ans += 1;
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (subarray-lcm nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length nums)]
         [vec (list->vector nums)])
    (let loop-outer ((i 0) (total 0))
      (if (= i n)
          total
          (let inner-loop ((j i) (cur 1) (cnt total))
            (if (>= j n)
                (loop-outer (+ i 1) cnt)
                (let ([new-lcm (lcm cur (vector-ref vec j))])
                  (cond [(> new-lcm k)
                         (loop-outer (+ i 1) cnt)]
                        [(= new-lcm k)
                         (inner-loop (+ j 1) new-lcm (+ cnt 1))]
                        [else
                         (inner-loop (+ j 1) new-lcm cnt)])))))))))
```

## Erlang

```erlang
-module(solution).
-export([subarray_lcm/2]).

-spec subarray_lcm(Nums :: [integer()], K :: integer()) -> integer().
subarray_lcm(Nums, K) ->
    count_starts(Nums, K, 0).

count_starts([], _K, Acc) -> Acc;
count_starts([_|T]=Rest, K, Acc) ->
    FromHere = count_from(Rest, K, 1, 0),
    count_starts(T, K, Acc + FromHere).

count_from([], _K, _LCM, Count) -> Count;
count_from([X|Xs], K, PrevLCM, Count) ->
    G = gcd(PrevLCM, X),
    NewLCM = (PrevLCM div G) * X,
    NewCount = case NewLCM == K of
        true -> Count + 1;
        false -> Count
    end,
    if
        NewLCM > K; (K rem NewLCM) =/= 0 ->
            NewCount;
        true ->
            count_from(Xs, K, NewLCM, NewCount)
    end.

gcd(0, B) -> B;
gcd(A, 0) -> A;
gcd(A, B) -> gcd(B rem A, A).
```

## Elixir

```elixir
defmodule Solution do
  @spec subarray_lcm(nums :: [integer], k :: integer) :: integer
  def subarray_lcm(nums, k) do
    n = length(nums)

    Enum.reduce(0..(n - 1), 0, fn i, acc ->
      {_, new_acc} =
        Enum.reduce_while(i..(n - 1), {1, acc}, fn j, {cur_lcm, cnt} ->
          l = lcm(cur_lcm, Enum.at(nums, j))

          cond do
            l == k -> {:cont, {l, cnt + 1}}
            l > k -> {:halt, {l, cnt}}
            true -> {:cont, {l, cnt}}
          end
        end)

      new_acc
    end)
  end

  defp gcd(a, 0), do: a
  defp gcd(a, b), do: gcd(b, rem(a, b))

  defp lcm(a, b) do
    div(a * b, gcd(a, b))
  end
end
```
