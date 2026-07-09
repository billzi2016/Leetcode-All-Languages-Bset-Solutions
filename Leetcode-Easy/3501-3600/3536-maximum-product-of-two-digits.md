# 3536. Maximum Product of Two Digits

## Cpp

```cpp
class Solution {
public:
    int maxProduct(int n) {
        std::vector<int> digits;
        while (n > 0) {
            digits.push_back(n % 10);
            n /= 10;
        }
        std::sort(digits.rbegin(), digits.rend());
        return digits[0] * digits[1];
    }
};
```

## Java

```java
class Solution {
    public int maxProduct(int n) {
        int max1 = 0, max2 = 0;
        while (n > 0) {
            int d = n % 10;
            if (d > max1) {
                max2 = max1;
                max1 = d;
            } else if (d > max2) {
                max2 = d;
            }
            n /= 10;
        }
        return max1 * max2;
    }
}
```

## Python

```python
class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = [int(c) for c in str(n)]
        digits.sort(reverse=True)
        return digits[0] * digits[1]
```

## Python3

```python
class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        ans = 0
        m = len(digits)
        for i in range(m):
            for j in range(i + 1, m):
                prod = digits[i] * digits[j]
                if prod > ans:
                    ans = prod
        return ans
```

## C

```c
int maxProduct(int n) {
    int cnt[10] = {0};
    while (n > 0) {
        cnt[n % 10]++;
        n /= 10;
    }
    int ans = 0;
    for (int i = 0; i <= 9; ++i) {
        for (int j = i; j <= 9; ++j) {
            if (i == j) {
                if (cnt[i] >= 2) {
                    int prod = i * j;
                    if (prod > ans) ans = prod;
                }
            } else {
                if (cnt[i] > 0 && cnt[j] > 0) {
                    int prod = i * j;
                    if (prod > ans) ans = prod;
                }
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxProduct(int n) {
        int[] cnt = new int[10];
        while (n > 0) {
            cnt[n % 10]++;
            n /= 10;
        }
        int maxProd = 0;
        for (int i = 0; i <= 9; i++) {
            for (int j = i; j <= 9; j++) {
                if (i == j) {
                    if (cnt[i] >= 2) {
                        maxProd = Math.Max(maxProd, i * j);
                    }
                } else {
                    if (cnt[i] > 0 && cnt[j] > 0) {
                        maxProd = Math.Max(maxProd, i * j);
                    }
                }
            }
        }
        return maxProd;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var maxProduct = function(n) {
    const digits = [];
    while (n > 0) {
        digits.push(n % 10);
        n = Math.floor(n / 10);
    }
    digits.sort((a, b) => b - a);
    return digits[0] * digits[1];
};
```

## Typescript

```typescript
function maxProduct(n: number): number {
    const digits: number[] = [];
    while (n > 0) {
        digits.push(n % 10);
        n = Math.floor(n / 10);
    }
    digits.sort((a, b) => b - a);
    return digits[0] * digits[1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function maxProduct($n) {
        $digits = array_map('intval', str_split((string)$n));
        rsort($digits);
        return $digits[0] * $digits[1];
    }
}
```

## Swift

```swift
class Solution {
    func maxProduct(_ n: Int) -> Int {
        var count = Array(repeating: 0, count: 10)
        var num = n
        while num > 0 {
            let digit = num % 10
            count[digit] += 1
            num /= 10
        }
        var ans = 0
        for i in 0...9 {
            for j in i...9 {
                if (i == j && count[i] >= 2) || (i != j && count[i] > 0 && count[j] > 0) {
                    let prod = i * j
                    if prod > ans { ans = prod }
                }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProduct(n: Int): Int {
        val cnt = IntArray(10)
        var x = n
        while (x > 0) {
            cnt[x % 10]++
            x /= 10
        }
        var first = -1
        var second = -1
        for (d in 9 downTo 0) {
            while (cnt[d] > 0) {
                if (first == -1) {
                    first = d
                } else {
                    second = d
                    break
                }
                cnt[d]--
            }
            if (second != -1) break
        }
        return first * second
    }
}
```

## Dart

```dart
class Solution {
  int maxProduct(int n) {
    List<int> digits = [];
    while (n > 0) {
      digits.add(n % 10);
      n ~/= 10;
    }
    digits.sort((a, b) => b - a);
    return digits[0] * digits[1];
  }
}
```

## Golang

```go
func maxProduct(n int) int {
    var digits []int
    for n > 0 {
        digits = append(digits, n%10)
        n /= 10
    }
    maxProd := 0
    for i := 0; i < len(digits); i++ {
        for j := i + 1; j < len(digits); j++ {
            prod := digits[i] * digits[j]
            if prod > maxProd {
                maxProd = prod
            }
        }
    }
    return maxProd
}
```

## Ruby

```ruby
def max_product(n)
  a, b = n.to_s.chars.map(&:to_i).max(2)
  a * b
end
```

## Scala

```scala
object Solution {
    def maxProduct(n: Int): Int = {
        var num = n
        val digits = scala.collection.mutable.ArrayBuffer[Int]()
        while (num > 0) {
            digits += (num % 10)
            num /= 10
        }
        val sorted = digits.sorted(Ordering.Int.reverse)
        sorted(0) * sorted(1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_product(n: i32) -> i32 {
        let mut cnt = [0i32; 10];
        let mut x = n;
        while x > 0 {
            let d = (x % 10) as usize;
            cnt[d] += 1;
            x /= 10;
        }
        let mut ans = 0;
        for i in 0..=9 {
            for j in i..=9 {
                if i == j {
                    if cnt[i] >= 2 {
                        ans = ans.max((i * j) as i32);
                    }
                } else if cnt[i] > 0 && cnt[j] > 0 {
                    ans = ans.max((i * j) as i32);
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-product n)
  (-> exact-integer? exact-integer?)
  (let loop ((x n) (digits '()))
    (if (= x 0)
        (let* ((sorted (sort digits >))
               (a (first sorted))
               (b (second sorted)))
          (* a b))
        (loop (quotient x 10) (cons (remainder x 10) digits)))))
```

## Erlang

```erlang
-module(solution).
-export([max_product/1]).

-spec max_product(N :: integer()) -> integer().
max_product(N) ->
    max_product(N, 0, 0).

max_product(0, Max1, Max2) ->
    Max1 * Max2;
max_product(N, Max1, Max2) ->
    Digit = N rem 10,
    {NewMax1, NewMax2} =
        if
            Digit > Max1 -> {Digit, Max1};
            Digit > Max2 -> {Max1, Digit};
            true -> {Max1, Max2}
        end,
    max_product(N div 10, NewMax1, NewMax2).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_product(n :: integer) :: integer
  def max_product(n) do
    digits = Integer.digits(n)
    [a, b | _] = Enum.sort(digits, &>=/2)
    a * b
  end
end
```
