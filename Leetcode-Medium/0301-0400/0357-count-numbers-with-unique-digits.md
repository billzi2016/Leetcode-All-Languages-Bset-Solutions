# 0357. Count Numbers with Unique Digits

## Cpp

```cpp
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if (n == 0) return 1;
        int result = 10; // all numbers with length 1 (0-9)
        int cur = 9;     // choices for the first digit when length >=2
        int available = 9; // remaining digits to choose from
        for (int len = 2; len <= n && available > 0; ++len) {
            cur *= available;
            result += cur;
            --available;
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int countNumbersWithUniqueDigits(int n) {
        if (n == 0) return 1;
        int total = 1; // count for number 0
        int mul = 9;   // numbers with length 1 (first digit cannot be zero)
        total += mul;
        for (int i = 2; i <= n && i < 10; i++) {
            mul *= (11 - i); // multiply by remaining available digits
            total += mul;
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        total = 1  # count for number 0
        cur = 9   # numbers with length 1 (1-9)
        total += cur
        available = 9  # remaining digits after choosing first non-zero digit
        for i in range(2, n + 1):
            cur *= available
            total += cur
            available -= 1
        return total
```

## Python3

```python
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        total = 1  # count for number 0
        cur = 9   # numbers with length 1 (1-9)
        total += cur
        for i in range(2, n + 1):
            cur *= (10 - (i - 1))
            total += cur
        return total
```

## C

```c
int countNumbersWithUniqueDigits(int n) {
    if (n == 0) return 1;
    int res = 10;               // all numbers with length 1 (0-9)
    int cur = 9;                // choices for the first non‑zero digit
    for (int i = 2; i <= n && i < 10; ++i) {
        cur *= (11 - i);        // multiply by remaining available digits
        res += cur;
    }
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int CountNumbersWithUniqueDigits(int n) {
        if (n == 0) return 1;
        int total = 1; // count the number 0
        int limit = Math.Min(n, 10);
        int cur = 9; // numbers with length 1 (excluding leading zero)
        total += cur;
        for (int k = 2; k <= limit; k++) {
            cur *= (11 - k); // multiply by decreasing available digits
            total += cur;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    if (n === 0) return 1;
    let total = 10; // numbers with length 1 (0-9)
    let cur = 9;    // count for current length starting from 2
    for (let i = 2; i <= n && i < 11; i++) {
        cur *= (11 - i); // multiply by remaining available digits
        total += cur;
    }
    return total;
};
```

## Typescript

```typescript
function countNumbersWithUniqueDigits(n: number): number {
    if (n === 0) return 1;
    let total = 10; // all one-digit numbers (0-9)
    let unique = 9; // choices for the first digit when length >=2
    for (let i = 2; i <= n && unique > 0; i++) {
        unique *= (11 - i); // multiply by remaining available digits
        total += unique;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countNumbersWithUniqueDigits($n) {
        if ($n == 0) {
            return 1;
        }
        $ans = 10; // numbers with length 1 (including zero)
        $cur = 0;
        for ($i = 2; $i <= $n; $i++) {
            if ($i == 2) {
                $cur = 9 * 9; // first digit non-zero (9 choices), second digit any except used (9 choices)
            } else {
                $cur *= (11 - $i); // multiply by decreasing available digits
            }
            $ans += $cur;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countNumbersWithUniqueDigits(_ n: Int) -> Int {
        if n == 0 { return 1 }
        var total = 10
        var uniqueCount = 9
        var available = 9
        var length = 2
        while length <= n && available > 0 {
            uniqueCount *= available
            total += uniqueCount
            available -= 1
            length += 1
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countNumbersWithUniqueDigits(n: Int): Int {
        if (n == 0) return 1
        var total = 1 // counting the number 0
        var cur = 1
        for (i in 1..n) {
            val factor = if (i == 1) 9 else 10 - i + 1
            cur *= factor
            total += cur
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int countNumbersWithUniqueDigits(int n) {
    if (n == 0) return 1;
    int total = 10; // numbers with length 1
    int cur = 9; // choices for first digit when length >=2
    int available = 9; // remaining digits to choose from
    for (int len = 2; len <= n && available > 0; ++len) {
      cur *= available;
      total += cur;
      available--;
    }
    return total;
  }
}
```

## Golang

```go
func countNumbersWithUniqueDigits(n int) int {
	if n == 0 {
		return 1
	}
	ans := 1 // counting the number 0
	mul := 9
	ans += mul // numbers with length 1 (1-9)
	for i := 2; i <= n && i < 10; i++ {
		mul *= 11 - i // multiply by decreasing available digits: 9,8,7,...
		ans += mul
	}
	return ans
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def count_numbers_with_unique_digits(n)
  return 1 if n == 0
  total = 1 # account for zero
  (1..n).each do |len|
    cur = 9
    available = 9
    (len - 1).times do
      cur *= available
      available -= 1
    end
    total += cur
  end
  total
end
```

## Scala

```scala
object Solution {
    def countNumbersWithUniqueDigits(n: Int): Int = {
        if (n == 0) return 1
        var total = 1          // counting the number 0
        var cur = 9            // numbers with length 1 (excluding leading zero)
        var available = 9      // digits left for subsequent positions
        val limit = math.min(n, 10)
        for (i <- 1 to limit) {
            if (i == 1) {
                total += cur    // add all one‑digit numbers (1..9)
            } else {
                cur *= available
                total += cur
                available -= 1
            }
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_numbers_with_unique_digits(n: i32) -> i32 {
        if n == 0 {
            return 1;
        }
        let mut total: i64 = 1; // include zero
        let limit = std::cmp::min(n, 10);
        for k in 1..=limit {
            let mut count: i64 = 9;
            let mut available: i64 = 9;
            for _ in 0..(k - 1) {
                count *= available;
                available -= 1;
            }
            total += count;
        }
        total as i32
    }
}
```

## Racket

```racket
(define/contract (count-numbers-with-unique-digits n)
  (-> exact-integer? exact-integer?)
  (if (= n 0)
      1
      (let loop ((k 1)          ; current length
                 (available 9) ; numbers left for next position (excluding leading zero)
                 (prod 1)      ; product of previous choices (P(9, k-1))
                 (sum 1))      ; start with counting the number 0
        (if (> k n)
            sum
            (let ((count-k (* 9 prod)))          ; numbers of length k with unique digits
              (loop (+ k 1)
                    (- available 1)
                    (* prod available)           ; update product for next length
                    (+ sum count-k)))))))
```

## Erlang

```erlang
-spec count_numbers_with_unique_digits(N :: integer()) -> integer().
count_numbers_with_unique_digits(N) when N >= 0, N =< 8 ->
    case N of
        0 -> 1;
        _ ->
            Total0 = 10,
            LenLoop = fun
                (Len, Prod, Tot) when Len > N ->
                    Tot;
                (Len, Prod, Tot) ->
                    NewProd = Prod * (11 - Len),
                    NewTot = Tot + NewProd,
                    LenLoop(Len + 1, NewProd, NewTot)
            end,
            LenLoop(2, 9, Total0)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_numbers_with_unique_digits(n :: integer) :: integer
  def count_numbers_with_unique_digits(n) do
    if n == 0 do
      1
    else
      max_len = min(n, 10)

      # sum includes the number 0 and all 1‑digit numbers (0..9)
      {initial_sum, initial_cur} = {1 + 9, 9}

      {total, _} =
        Enum.reduce(2..max_len, {initial_sum, initial_cur}, fn len, {sum, cur} ->
          new_cur = cur * (11 - len)   # multiply by remaining available digits
          {sum + new_cur, new_cur}
        end)

      total
    end
  end
end
```
