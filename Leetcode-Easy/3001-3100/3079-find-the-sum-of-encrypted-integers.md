# 3079. Find the Sum of Encrypted Integers

## Cpp

```cpp
class Solution {
public:
    int sumOfEncryptedInt(vector<int>& nums) {
        int total = 0;
        for (int x : nums) {
            int n = x, maxDigit = 0, len = 0;
            while (n > 0) {
                int d = n % 10;
                if (d > maxDigit) maxDigit = d;
                n /= 10;
                ++len;
            }
            int encrypted = 0;
            for (int i = 0; i < len; ++i) {
                encrypted = encrypted * 10 + maxDigit;
            }
            total += encrypted;
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public int sumOfEncryptedInt(int[] nums) {
        int total = 0;
        for (int n : nums) {
            int maxDigit = 0;
            int temp = n;
            int digits = 0;
            while (temp > 0) {
                int d = temp % 10;
                if (d > maxDigit) maxDigit = d;
                temp /= 10;
                digits++;
            }
            int encrypted = 0;
            for (int i = 0; i < digits; i++) {
                encrypted = encrypted * 10 + maxDigit;
            }
            total += encrypted;
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for x in nums:
            s = str(x)
            max_digit = max(s)
            encrypted = int(max_digit * len(s))
            total += encrypted
        return total
```

## Python3

```python
from typing import List

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            s = str(num)
            max_digit = max(s)
            encrypted = int(max_digit * len(s))
            total += encrypted
        return total
```

## C

```c
int sumOfEncryptedInt(int* nums, int numsSize) {
    int total = 0;
    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        int maxDigit = 0;
        int temp = x;
        while (temp > 0) {
            int d = temp % 10;
            if (d > maxDigit) maxDigit = d;
            temp /= 10;
        }
        int digits = 0;
        temp = x;
        while (temp > 0) {
            ++digits;
            temp /= 10;
        }
        int encrypted = 0;
        for (int j = 0; j < digits; ++j) {
            encrypted = encrypted * 10 + maxDigit;
        }
        total += encrypted;
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int SumOfEncryptedInt(int[] nums) {
        int total = 0;
        foreach (int num in nums) {
            int n = num;
            int maxDigit = 0;
            int length = 0;
            while (n > 0) {
                int d = n % 10;
                if (d > maxDigit) maxDigit = d;
                n /= 10;
                length++;
            }
            int encrypted = 0;
            for (int i = 0; i < length; i++) {
                encrypted = encrypted * 10 + maxDigit;
            }
            total += encrypted;
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
var sumOfEncryptedInt = function(nums) {
    let total = 0;
    for (let num of nums) {
        const s = String(num);
        let maxDigit = '0';
        for (let ch of s) {
            if (ch > maxDigit) maxDigit = ch;
        }
        const encryptedStr = maxDigit.repeat(s.length);
        total += Number(encryptedStr);
    }
    return total;
};
```

## Typescript

```typescript
function sumOfEncryptedInt(nums: number[]): number {
    let total = 0;
    for (const num of nums) {
        let n = num;
        let maxDigit = 0;
        let digits = 0;
        while (n > 0) {
            const d = n % 10;
            if (d > maxDigit) maxDigit = d;
            n = Math.floor(n / 10);
            digits++;
        }
        let encrypted = 0;
        for (let i = 0; i < digits; i++) {
            encrypted = encrypted * 10 + maxDigit;
        }
        total += encrypted;
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
    function sumOfEncryptedInt($nums) {
        $total = 0;
        foreach ($nums as $num) {
            $str = (string)$num;
            $len = strlen($str);
            $maxDigit = 0;
            for ($i = 0; $i < $len; $i++) {
                $digit = intval($str[$i]);
                if ($digit > $maxDigit) {
                    $maxDigit = $digit;
                }
            }
            $encrypted = str_repeat((string)$maxDigit, $len);
            $total += intval($encrypted);
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func sumOfEncryptedInt(_ nums: [Int]) -> Int {
        var total = 0
        for num in nums {
            var x = num
            var maxDigit = 0
            var digitCount = 0
            while x > 0 {
                let d = x % 10
                if d > maxDigit { maxDigit = d }
                x /= 10
                digitCount += 1
            }
            var encrypted = 0
            for _ in 0..<digitCount {
                encrypted = encrypted * 10 + maxDigit
            }
            total += encrypted
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumOfEncryptedInt(nums: IntArray): Int {
        var total = 0
        for (num in nums) {
            var n = num
            var maxDigit = 0
            var len = 0
            while (n > 0) {
                val d = n % 10
                if (d > maxDigit) maxDigit = d
                n /= 10
                len++
            }
            var encrypted = 0
            repeat(len) { encrypted = encrypted * 10 + maxDigit }
            total += encrypted
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int sumOfEncryptedInt(List<int> nums) {
    int total = 0;
    for (int num in nums) {
      String s = num.toString();
      int maxDigit = 0;
      for (int i = 0; i < s.length; i++) {
        int d = s.codeUnitAt(i) - 48; // '0' ascii is 48
        if (d > maxDigit) maxDigit = d;
      }
      int encrypted = 0;
      for (int i = 0; i < s.length; i++) {
        encrypted = encrypted * 10 + maxDigit;
      }
      total += encrypted;
    }
    return total;
  }
}
```

## Golang

```go
func sumOfEncryptedInt(nums []int) int {
    total := 0
    for _, num := range nums {
        maxDigit := 0
        factor := 0
        n := num
        if n == 0 {
            // Though constraints guarantee positive numbers, handle zero just in case.
            maxDigit = 0
            factor = 1
        } else {
            for n > 0 {
                d := n % 10
                if d > maxDigit {
                    maxDigit = d
                }
                factor = factor*10 + 1
                n /= 10
            }
        }
        total += maxDigit * factor
    }
    return total
}
```

## Ruby

```ruby
def sum_of_encrypted_int(nums)
  total = 0
  nums.each do |num|
    s = num.to_s
    max_digit = s.chars.map(&:to_i).max
    encrypted = (max_digit.to_s * s.length).to_i
    total += encrypted
  end
  total
end
```

## Scala

```scala
object Solution {
    def sumOfEncryptedInt(nums: Array[Int]): Int = {
        var total = 0
        for (num <- nums) {
            var n = num
            var maxDigit = 0
            while (n > 0) {
                val d = n % 10
                if (d > maxDigit) maxDigit = d
                n /= 10
            }
            var enc = 0
            var temp = num
            while (temp > 0) {
                enc = enc * 10 + maxDigit
                temp /= 10
            }
            total += enc
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_of_encrypted_int(nums: Vec<i32>) -> i32 {
        let mut total = 0i32;
        for num in nums {
            // Find the maximum digit
            let mut n = num;
            let mut max_digit = 0i32;
            while n > 0 {
                let d = n % 10;
                if d > max_digit {
                    max_digit = d;
                }
                n /= 10;
            }

            // Build the encrypted number by repeating max_digit
            let mut encrypted = 0i32;
            let mut t = num;
            while t > 0 {
                encrypted = encrypted * 10 + max_digit;
                t /= 10;
            }

            total += encrypted;
        }
        total
    }
}
```

## Racket

```racket
(define (encrypt n)
  (let loop ((x n) (max 0) (len 0))
    (if (= x 0)
        (let ((repunit (quotient (- (expt 10 len) 1) 9)))
          (* max repunit))
        (let* ((digit (remainder x 10))
               (new-max (if (> digit max) digit max)))
          (loop (quotient x 10) new-max (+ len 1))))))

(define/contract (sum-of-encrypted-int nums)
  (-> (listof exact-integer?) exact-integer?)
  (apply + (map encrypt nums)))
```

## Erlang

```erlang
-spec sum_of_encrypted_int([integer()]) -> integer().
sum_of_encrypted_int(Nums) ->
    lists:foldl(fun(N, Acc) -> encrypt(N) + Acc end, 0, Nums).

encrypt(N) ->
    Digits = integer_to_list(N),
    MaxDigitChar = lists:max(Digits),
    EncryptedDigits = lists:duplicate(length(Digits), MaxDigitChar),
    list_to_integer(EncryptedDigits).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_of_encrypted_int(nums :: [integer]) :: integer
  def sum_of_encrypted_int(nums) do
    nums
    |> Enum.map(&encrypt/1)
    |> Enum.sum()
  end

  defp encrypt(num) do
    s = Integer.to_string(num)
    max_digit = Enum.max(String.graphemes(s))
    String.duplicate(max_digit, String.length(s))
    |> String.to_integer()
  end
end
```
