# 1716. Calculate Money in Leetcode Bank

## Cpp

```cpp
class Solution {
public:
    int totalMoney(int n) {
        long long k = n / 7;
        long long r = n % 7;
        long long fullWeeks = k * 28 + 7 * k * (k - 1) / 2;
        long long remaining = r * (2 * k + r + 1) / 2;
        return static_cast<int>(fullWeeks + remaining);
    }
};
```

## Java

```java
class Solution {
    public int totalMoney(int n) {
        int weeks = n / 7;
        int rem = n % 7;

        // Sum of full weeks: (weeks * 7 * (weeks + 7)) / 2
        int fullWeeksSum = weeks * 7 * (weeks + 7) / 2;

        // Money deposited in the remaining days
        int startMonday = weeks + 1;
        int remainderSum = rem * startMonday + rem * (rem - 1) / 2;

        return fullWeeksSum + remainderSum;
    }
}
```

## Python

```python
class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        full_weeks = n // 7
        rem_days = n % 7

        # Sum of complete weeks (arithmetic series)
        sum_full = full_weeks * (28 + (28 + (full_weeks - 1) * 7)) // 2

        # Sum of the remaining days in the last partial week
        monday_amount = 1 + full_weeks
        sum_rem = rem_days * monday_amount + rem_days * (rem_days - 1) // 2

        return sum_full + sum_rem
```

## Python3

```python
class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        # Sum of complete weeks: each week adds 28 + 7*i dollars (i from 0)
        full_weeks_sum = 28 * weeks + 7 * weeks * (weeks - 1) // 2

        remaining_days = n % 7
        monday_amount = 1 + weeks
        # Sum of the remaining days: arithmetic series starting at monday_amount
        partial_week_sum = remaining_days * monday_amount + remaining_days * (remaining_days - 1) // 2

        return full_weeks_sum + partial_week_sum
```

## C

```c
int totalMoney(int n) {
    int k = n / 7;
    int r = n % 7;
    int fullWeeks = 28 * k + (7 * k * (k - 1)) / 2;
    int finalWeek = r * (r + 1 + 2 * k) / 2;
    return fullWeeks + finalWeek;
}
```

## Csharp

```csharp
public class Solution {
    public int TotalMoney(int n) {
        int weeks = n / 7;
        int rem = n % 7;
        long total = 0;
        // Sum for full weeks
        total += (long)weeks * 28 + 7L * weeks * (weeks - 1) / 2;
        // Sum for remaining days
        int monday = 1 + weeks;
        total += (long)rem * (2L * monday + rem - 1) / 2;
        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var totalMoney = function(n) {
    const weeks = Math.floor(n / 7);
    const rem = n % 7;
    
    // Sum for full weeks: arithmetic series starting at 28, difference 7
    let sumFull = 0;
    if (weeks > 0) {
        const firstWeekSum = 28;
        const lastWeekSum = 28 + (weeks - 1) * 7;
        sumFull = weeks * (firstWeekSum + lastWeekSum) / 2;
    }
    
    // Sum for remaining days
    const mondayAmount = 1 + weeks; // amount deposited on Monday of the partial week
    const sumRem = rem * (2 * mondayAmount + (rem - 1)) / 2;
    
    return sumFull + sumRem;
};
```

## Typescript

```typescript
function totalMoney(n: number): number {
    const weeks = Math.floor(n / 7);
    const rem = n % 7;

    // Sum for full weeks
    let fullWeeksSum = 0;
    if (weeks > 0) {
        const firstWeek = 28; // sum of week 1 (Monday=1)
        const lastWeek = firstWeek + (weeks - 1) * 7;
        fullWeeksSum = weeks * (firstWeek + lastWeek) / 2;
    }

    // Sum for remaining days in the incomplete week
    const mondayAmount = 1 + weeks;
    const remSum = rem * mondayAmount + (rem * (rem - 1)) / 2;

    return fullWeeksSum + remSum;
}
```

## Php

```php
<?php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function totalMoney($n) {
        $fullWeeks = intdiv($n, 7);
        $remDays   = $n % 7;

        // Sum for complete weeks
        if ($fullWeeks > 0) {
            $firstWeekSum = 28; // 1+2+3+4+5+6+7
            $lastWeekSum  = $firstWeekSum + ($fullWeeks - 1) * 7;
            $sumFullWeeks = intdiv($fullWeeks * ($firstWeekSum + $lastWeekSum), 2);
        } else {
            $sumFullWeeks = 0;
        }

        // Sum for the remaining days of the last (partial) week
        $mondayAmount = 1 + $fullWeeks;
        $sumRem = 0;
        for ($i = 0; $i < $remDays; $i++) {
            $sumRem += $mondayAmount + $i;
        }

        return $sumFullWeeks + $sumRem;
    }
}
?>
```

## Swift

```swift
class Solution {
    func totalMoney(_ n: Int) -> Int {
        let weeks = n / 7
        var ans = 0
        if weeks > 0 {
            // Sum of full weeks: arithmetic series with first term 28 and difference 7
            ans = weeks * (56 + (weeks - 1) * 7) / 2
        }
        let remaining = n % 7
        if remaining > 0 {
            let monday = 1 + weeks
            ans += remaining * monday + remaining * (remaining - 1) / 2
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun totalMoney(n: Int): Int {
        val weeks = n / 7
        val firstWeekSum = 28
        val lastWeekSum = 28 + (weeks - 1) * 7
        val fullWeeksSum = weeks * (firstWeekSum + lastWeekSum) / 2

        val remainingDays = n % 7
        val monday = 1 + weeks
        val partialSum = remainingDays * (2 * monday + (remainingDays - 1)) / 2

        return fullWeeksSum + partialSum
    }
}
```

## Dart

```dart
class Solution {
  int totalMoney(int n) {
    int fullWeeks = n ~/ 7;
    int remainingDays = n % 7;

    int firstWeekSum = 28;
    int lastWeekSum = 28 + (fullWeeks - 1) * 7;
    int sumFullWeeks = fullWeeks * (firstWeekSum + lastWeekSum) ~/ 2;

    int monday = fullWeeks + 1;
    int sumRemaining = 0;
    for (int i = 0; i < remainingDays; ++i) {
      sumRemaining += monday + i;
    }

    return sumFullWeeks + sumRemaining;
  }
}
```

## Golang

```go
func totalMoney(n int) int {
	weeks := n / 7
	days := n % 7

	// Sum for complete weeks: each week adds 28 + 7*i dollars, i = 0..weeks-1
	totalFull := weeks*28 + 7*weeks*(weeks-1)/2

	// Money deposited in the remaining days of the last (partial) week
	monday := 1 + weeks
	partial := days*monday + days*(days-1)/2

	return totalFull + partial
}
```

## Ruby

```ruby
def total_money(n)
  k = n / 7
  full = k * (56 + (k - 1) * 7) / 2
  r = n % 7
  monday = 1 + k
  partial = r * monday + r * (r - 1) / 2
  full + partial
end
```

## Scala

```scala
object Solution {
    def totalMoney(n: Int): Int = {
        val weeks = n / 7
        val fullWeeksSum = 7 * weeks * (weeks + 7) / 2
        val remainingDays = n % 7
        val extra = remainingDays * (2 * weeks + remainingDays + 1) / 2
        fullWeeksSum + extra
    }
}
```

## Rust

```rust
impl Solution {
    pub fn total_money(n: i32) -> i32 {
        let weeks = n / 7;
        let rem = n % 7;

        let sum_full = if weeks > 0 {
            let weeks_i64 = weeks as i64;
            let first = 28i64;
            let last = 28 + (weeks_i64 - 1) * 7;
            weeks_i64 * (first + last) / 2
        } else {
            0
        };

        let sum_rem = if rem > 0 {
            let rem_i64 = rem as i64;
            let start = (1 + weeks) as i64;
            rem_i64 * (2 * start + (rem_i64 - 1)) / 2
        } else {
            0
        };

        (sum_full + sum_rem) as i32
    }
}
```

## Racket

```racket
(define/contract (total-money n)
  (-> exact-integer? exact-integer?)
  (let* ((k (quotient n 7))                ; full weeks
         (r (remainder n 7))               ; remaining days
         (sum-full (if (= k 0)
                       0
                       (/ (* k (+ 56 (* (- k 1) 7))) 2)))
         (monday (+ 1 k))
         (sum-rem (if (= r 0)
                      0
                      (/ (* r (+ (* 2 monday) (- r 1))) 2))))
    (+ sum-full sum-rem)))
```

## Erlang

```erlang
-spec total_money(N :: integer()) -> integer().
total_money(N) ->
    K = N div 7,
    R = N rem 7,
    SumFull = K * (49 + 7*K) div 2,
    Monday = 1 + K,
    SumRem = lists:foldl(fun(I, Acc) -> Acc + Monday + I end, 0, lists:seq(0, R-1)),
    SumFull + SumRem.
```

## Elixir

```elixir
defmodule Solution do
  @spec total_money(n :: integer) :: integer
  def total_money(n) do
    k = div(n, 7)
    r = rem(n, 7)

    full_sum =
      k * (28 + (28 + (k - 1) * 7))
      |> div(2)

    extra_sum =
      r * (2 * (1 + k) + (r - 1))
      |> div(2)

    full_sum + extra_sum
  end
end
```
