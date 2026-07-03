# 0066. Plus One

## Cpp

```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        for (int i = n - 1; i >= 0; --i) {
            if (digits[i] < 9) {
                ++digits[i];
                return digits;
            }
            digits[i] = 0;
        }
        // If we are here, all digits were 9
        vector<int> result(n + 1, 0);
        result[0] = 1;
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        int[] result = new int[n + 1];
        result[0] = 1;
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        # If we are here, all digits were 9
        return [1] + digits
```

## Python3

```python
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    int* res = (int*)malloc(digitsSize * sizeof(int));
    if (!res) return NULL;
    memcpy(res, digits, digitsSize * sizeof(int));

    int carry = 1;
    for (int i = digitsSize - 1; i >= 0 && carry; --i) {
        int sum = res[i] + carry;
        res[i] = sum % 10;
        carry = sum / 10;
    }

    if (carry) {
        int* final = (int*)malloc((digitsSize + 1) * sizeof(int));
        if (!final) {
            free(res);
            return NULL;
        }
        final[0] = carry; // will be 1
        memcpy(final + 1, res, digitsSize * sizeof(int));
        free(res);
        *returnSize = digitsSize + 1;
        return final;
    } else {
        *returnSize = digitsSize;
        return res;
    }
}
```

## Csharp

```csharp
public class Solution {
    public int[] PlusOne(int[] digits) {
        int n = digits.Length;
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        // If we are here, all digits were 9
        int[] result = new int[n + 1];
        result[0] = 1;
        // remaining elements are already 0 by default
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    for (let i = digits.length - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            return digits;
        }
        digits[i] = 0;
    }
    digits.unshift(1);
    return digits;
};
```

## Typescript

```typescript
function plusOne(digits: number[]): number[] {
    for (let i = digits.length - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            return digits;
        }
        digits[i] = 0;
    }
    digits.unshift(1);
    return digits;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $digits
     * @return Integer[]
     */
    function plusOne($digits) {
        $n = count($digits);
        $carry = 1;
        for ($i = $n - 1; $i >= 0 && $carry > 0; $i--) {
            $sum = $digits[$i] + $carry;
            $digits[$i] = $sum % 10;
            $carry = intdiv($sum, 10);
        }
        if ($carry > 0) {
            array_unshift($digits, $carry);
        }
        return $digits;
    }
}
```

## Swift

```swift
class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        var result = digits
        for i in stride(from: result.count - 1, through: 0, by: -1) {
            if result[i] < 9 {
                result[i] += 1
                return result
            }
            result[i] = 0
        }
        result.insert(1, at: 0)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun plusOne(digits: IntArray): IntArray {
        for (i in digits.indices.reversed()) {
            if (digits[i] < 9) {
                digits[i]++
                return digits
            }
            digits[i] = 0
        }
        val result = IntArray(digits.size + 1)
        result[0] = 1
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> plusOne(List<int> digits) {
    for (int i = digits.length - 1; i >= 0; i--) {
      if (digits[i] < 9) {
        digits[i]++;
        return digits;
      }
      digits[i] = 0;
    }
    digits.insert(0, 1);
    return digits;
  }
}
```

## Golang

```go
func plusOne(digits []int) []int {
	n := len(digits)
	for i := n - 1; i >= 0; i-- {
		if digits[i] < 9 {
			digits[i]++
			return digits
		}
		digits[i] = 0
	}
	res := make([]int, n+1)
	res[0] = 1
	return res
}
```

## Ruby

```ruby
def plus_one(digits)
  i = digits.length - 1
  carry = 1
  while i >= 0 && carry > 0
    sum = digits[i] + carry
    digits[i] = sum % 10
    carry = sum / 10
    i -= 1
  end
  digits.unshift(carry) if carry > 0
  digits
end
```

## Scala

```scala
object Solution {
    def plusOne(digits: Array[Int]): Array[Int] = {
        var i = digits.length - 1
        while (i >= 0 && digits(i) == 9) {
            digits(i) = 0
            i -= 1
        }
        if (i < 0) {
            val res = new Array[Int](digits.length + 1)
            res(0) = 1
            res
        } else {
            digits(i) += 1
            digits
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn plus_one(mut digits: Vec<i32>) -> Vec<i32> {
        let mut carry = 1;
        for i in (0..digits.len()).rev() {
            let sum = digits[i] + carry;
            digits[i] = sum % 10;
            carry = sum / 10;
            if carry == 0 {
                break;
            }
        }
        if carry > 0 {
            digits.insert(0, carry);
        }
        digits
    }
}
```

## Racket

```racket
(define/contract (plus-one digits)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let loop ((lst (reverse digits)) (carry 1) (acc '()))
    (if (null? lst)
        (if (= carry 0) acc (cons carry acc))
        (let* ((sum (+ (car lst) carry))
               (new-digit (modulo sum 10))
               (new-carry (quotient sum 10)))
          (loop (cdr lst) new-carry (cons new-digit acc))))))
```

## Erlang

```erlang
-spec plus_one(Digits :: [integer()]) -> [integer()].
plus_one(Digits) ->
    Rev = lists:reverse(Digits),
    NewRev = add_one(Rev, 1),
    lists:reverse(NewRev).

add_one([], 0) -> [];
add_one([], Carry) -> [Carry];
add_one([H|T], Carry) ->
    Sum = H + Carry,
    Digit = Sum rem 10,
    NewCarry = Sum div 10,
    [Digit | add_one(T, NewCarry)].
```

## Elixir

```elixir
defmodule Solution do
  @spec plus_one(digits :: [integer]) :: [integer]
  def plus_one(digits) do
    {rev_res, carry} =
      digits
      |> Enum.reverse()
      |> Enum.map_reduce(1, fn d, c ->
        sum = d + c
        {rem(sum, 10), div(sum, 10)}
      end)

    result = if carry == 1, do: [1 | rev_res], else: rev_res
    Enum.reverse(result)
  end
end
```
