# 1390. Four Divisors

## Cpp

```cpp
class Solution {
public:
    int sumFourDivisors(vector<int>& nums) {
        long long total = 0;
        for (int x : nums) {
            int cnt = 0;
            int sum = 0;
            for (int i = 1; i * i <= x && cnt <= 4; ++i) {
                if (x % i == 0) {
                    int j = x / i;
                    if (i == j) {
                        ++cnt;
                        sum += i;
                    } else {
                        cnt += 2;
                        sum += i + j;
                    }
                }
            }
            if (cnt == 4) total += sum;
        }
        return static_cast<int>(total);
    }
};
```

## Java

```java
class Solution {
    public int sumFourDivisors(int[] nums) {
        int total = 0;
        for (int num : nums) {
            int cnt = 0;
            int sum = 0;
            for (int d = 1; d * d <= num; ++d) {
                if (num % d == 0) {
                    int other = num / d;
                    if (d == other) {
                        cnt++;
                        sum += d;
                    } else {
                        cnt += 2;
                        sum += d + other;
                    }
                    if (cnt > 4) break;
                }
            }
            if (cnt == 4) total += sum;
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for n in nums:
            # early skip if n is too small to have four divisors
            if n < 6:  # smallest number with 4 divisors is 6 (1,2,3,6)
                continue
            divs = [1]
            limit = int(n ** 0.5)
            for i in range(2, limit + 1):
                if n % i == 0:
                    j = n // i
                    divs.append(i)
                    if j != i:
                        divs.append(j)
                    if len(divs) > 4:
                        break
            if n != 1:
                divs.append(n)
            if len(divs) == 4:
                total += sum(divs)
        return total
```

## Python3

```python
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            if n <= 1:
                continue
            div_sum = 1 + n
            cnt = 2
            limit = int(n ** 0.5)
            for i in range(2, limit + 1):
                if n % i == 0:
                    j = n // i
                    if i == j:
                        cnt += 1
                        div_sum += i
                    else:
                        cnt += 2
                        div_sum += i + j
                    if cnt > 4:
                        break
            if cnt == 4:
                total += div_sum
        return total
```

## C

```c
int sumFourDivisors(int* nums, int numsSize) {
    long total = 0;
    for (int i = 0; i < numsSize; ++i) {
        int n = nums[i];
        int cnt = 0;
        int sum = 0;
        for (int d = 1; d * d <= n; ++d) {
            if (n % d == 0) {
                int other = n / d;
                if (d == other) {
                    cnt += 1;
                    sum += d;
                } else {
                    cnt += 2;
                    sum += d + other;
                }
                if (cnt > 4) break;
            }
        }
        if (cnt == 4) total += sum;
    }
    return (int)total;
}
```

## Csharp

```csharp
public class Solution {
    public int SumFourDivisors(int[] nums) {
        int total = 0;
        foreach (int num in nums) {
            int count = 0;
            int sum = 0;
            for (int i = 1; i * i <= num && count <= 4; ++i) {
                if (num % i == 0) {
                    int j = num / i;
                    if (i == j) {
                        count += 1;
                        sum += i;
                    } else {
                        count += 2;
                        sum += i + j;
                    }
                }
            }
            if (count == 4) total += sum;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumFourDivisors = function(nums) {
    let total = 0;
    for (const n of nums) {
        let cnt = 0, sum = 0;
        const limit = Math.floor(Math.sqrt(n));
        for (let i = 1; i <= limit; ++i) {
            if (n % i === 0) {
                const j = n / i;
                if (i === j) {
                    cnt += 1;
                    sum += i;
                } else {
                    cnt += 2;
                    sum += i + j;
                }
                if (cnt > 4) break;
            }
        }
        if (cnt === 4) total += sum;
    }
    return total;
};
```

## Typescript

```typescript
function sumFourDivisors(nums: number[]): number {
    let total = 0;
    for (const n of nums) {
        let cnt = 0;
        let sum = 0;
        const limit = Math.floor(Math.sqrt(n));
        for (let i = 1; i <= limit; ++i) {
            if (n % i === 0) {
                const j = n / i;
                if (i === j) {
                    cnt += 1;
                    sum += i;
                } else {
                    cnt += 2;
                    sum += i + j;
                }
                if (cnt > 4) break;
            }
        }
        if (cnt === 4) total += sum;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumFourDivisors($nums) {
        $total = 0;
        foreach ($nums as $n) {
            $cnt = 0;
            $sum = 0;
            $limit = (int)sqrt($n);
            for ($i = 1; $i <= $limit; $i++) {
                if ($n % $i === 0) {
                    $j = intdiv($n, $i);
                    if ($i == $j) {
                        $cnt += 1;
                        $sum += $i;
                    } else {
                        $cnt += 2;
                        $sum += $i + $j;
                    }
                    if ($cnt > 4) {
                        break;
                    }
                }
            }
            if ($cnt === 4) {
                $total += $sum;
            }
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func sumFourDivisors(_ nums: [Int]) -> Int {
        var total = 0
        for num in nums {
            var count = 0
            var sum = 0
            let limit = Int(Double(num).squareRoot())
            var i = 1
            while i <= limit {
                if num % i == 0 {
                    let j = num / i
                    if i == j {
                        count += 1
                        sum += i
                    } else {
                        count += 2
                        sum += i + j
                    }
                    if count > 4 { break }
                }
                i += 1
            }
            if count == 4 {
                total += sum
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumFourDivisors(nums: IntArray): Int {
        var total = 0L
        for (num in nums) {
            if (num <= 1) continue
            var count = 2               // 1 and num itself
            var sum = 1 + num
            val limit = Math.sqrt(num.toDouble()).toInt()
            var i = 2
            while (i <= limit && count <= 4) {
                if (num % i == 0) {
                    val other = num / i
                    if (i == other) {
                        count += 1
                        sum += i
                    } else {
                        count += 2
                        sum += i + other
                    }
                }
                i++
            }
            if (count == 4) total += sum
        }
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int sumFourDivisors(List<int> nums) {
    int total = 0;
    for (int n in nums) {
      int cnt = 0;
      int sum = 0;
      for (int i = 1; i * i <= n && cnt <= 4; i++) {
        if (n % i == 0) {
          int j = n ~/ i;
          if (i == j) {
            cnt += 1;
            sum += i;
          } else {
            cnt += 2;
            sum += i + j;
          }
          if (cnt > 4) break;
        }
      }
      if (cnt == 4) total += sum;
    }
    return total;
  }
}
```

## Golang

```go
import "math"

func sumFourDivisors(nums []int) int {
    total := 0
    for _, n := range nums {
        cnt, sum := 0, 0
        limit := int(math.Sqrt(float64(n)))
        for i := 1; i <= limit; i++ {
            if n%i == 0 {
                j := n / i
                if i == j {
                    cnt++
                    sum += i
                } else {
                    cnt += 2
                    sum += i + j
                }
                if cnt > 4 {
                    break
                }
            }
        }
        if cnt == 4 {
            total += sum
        }
    }
    return total
}
```

## Ruby

```ruby
def sum_four_divisors(nums)
  total = 0
  nums.each do |num|
    cnt = 0
    sum = 0
    limit = Math.sqrt(num).to_i
    i = 1
    while i <= limit && cnt <= 4
      if num % i == 0
        j = num / i
        if i == j
          cnt += 1
          sum += i
        else
          cnt += 2
          sum += i + j
        end
      end
      i += 1
    end
    total += sum if cnt == 4
  end
  total
end
```

## Scala

```scala
object Solution {
    def sumFourDivisors(nums: Array[Int]): Int = {
        var total = 0
        for (n <- nums) {
            var cnt = 0
            var sum = 0
            val limit = math.sqrt(n).toInt
            var i = 1
            while (i <= limit && cnt <= 4) {
                if (n % i == 0) {
                    val j = n / i
                    if (i == j) {
                        cnt += 1
                        sum += i
                    } else {
                        cnt += 2
                        sum += i + j
                    }
                }
                i += 1
            }
            if (cnt == 4) total += sum
        }
        total
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {
        let mut total: i64 = 0;
        for &num in nums.iter() {
            if num < 2 {
                continue;
            }
            let mut cnt = 0;
            let mut sum = 0i64;
            let limit = (num as f64).sqrt() as i32;
            for d in 1..=limit {
                if num % d == 0 {
                    let other = num / d;
                    if d == other {
                        cnt += 1;
                        sum += d as i64;
                    } else {
                        cnt += 2;
                        sum += d as i64 + other as i64;
                    }
                    if cnt > 4 {
                        break;
                    }
                }
            }
            if cnt == 4 {
                total += sum;
            }
        }
        total as i32
    }
}
```

## Racket

```racket
(require racket/math)

(define (divisor-sum-if-4 n)
  (let* ((limit (exact-floor (sqrt n)))
         (cnt 0)
         (sum 0))
    (for ([i (in-range 1 (+ limit 1))] #:break (> cnt 4))
      (when (= (remainder n i) 0)
        (set! cnt (+ cnt 1))
        (set! sum (+ sum i))
        (let ((j (/ n i)))
          (unless (= i j)
            (set! cnt (+ cnt 1))
            (set! sum (+ sum j))))))
    (if (= cnt 4) sum 0)))

(define/contract (sum-four-divisors nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (total 0))
    (if (null? lst)
        total
        (loop (cdr lst) (+ total (divisor-sum-if-4 (car lst)))))))
```

## Erlang

```erlang
-spec sum_four_divisors(Nums :: [integer()]) -> integer().
-export([sum_four_divisors/1]).
 
sum_four_divisors(Nums) ->
    lists:foldl(fun(N, Acc) -> Acc + four_sum(N) end, 0, Nums).
 
four_sum(N) ->
    Limit = trunc(math:sqrt(N)),
    {Count, Sum} = count_sum(N, 1, Limit, 0, 0),
    case Count of
        4 -> Sum;
        _ -> 0
    end.
 
count_sum(_N, I, Limit, Count, Sum) when I > Limit ->
    {Count, Sum};
count_sum(N, I, Limit, Count, Sum) ->
    case N rem I of
        0 ->
            D2 = N div I,
            NewCount = if I == D2 -> Count + 1; true -> Count + 2 end,
            NewSum = if I == D2 -> Sum + I; true -> Sum + I + D2 end,
            count_sum(N, I + 1, Limit, NewCount, NewSum);
        _ ->
            count_sum(N, I + 1, Limit, Count, Sum)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_four_divisors(nums :: [integer]) :: integer
  def sum_four_divisors(nums) do
    Enum.reduce(nums, 0, fn num, acc ->
      acc + four_div_sum(num)
    end)
  end

  defp four_div_sum(n) when n > 0 do
    limit = :math.sqrt(n) |> trunc()
    {cnt, sum} =
      1..limit
      |> Enum.reduce_while({0, 0}, fn i, {c, s} ->
        if rem(n, i) == 0 do
          d2 = div(n, i)
          new_c = c + (if i == d2, do: 1, else: 2)
          new_s = s + i + (if i == d2, do: 0, else: d2)

          if new_c > 4 do
            {:halt, {new_c, new_s}}
          else
            {:cont, {new_c, new_s}}
          end
        else
          {:cont, {c, s}}
        end
      end)

    if cnt == 4, do: sum, else: 0
  end

  defp four_div_sum(_), do: 0
end
```
