# 0989. Add to Array-Form of Integer

## Cpp

```cpp
class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        vector<int> res;
        int i = (int)num.size() - 1;
        int carry = 0;
        while (i >= 0 || k > 0) {
            int digit = (i >= 0 ? num[i] : 0);
            int sum = digit + (k % 10) + carry;
            res.push_back(sum % 10);
            carry = sum / 10;
            if (i >= 0) --i;
            k /= 10;
        }
        while (carry > 0) {
            res.push_back(carry % 10);
            carry /= 10;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        List<Integer> result = new ArrayList<>();
        int i = num.length - 1;
        int carry = 0;
        while (i >= 0 || k > 0) {
            int n = (i >= 0) ? num[i] : 0;
            int sum = n + (k % 10) + carry;
            result.add(sum % 10);
            carry = sum / 10;
            k /= 10;
            i--;
        }
        if (carry > 0) {
            result.add(carry);
        }
        Collections.reverse(result);
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        i = len(num) - 1
        res = []
        while i >= 0 or k:
            if i >= 0:
                k += num[i]
                i -= 1
            res.append(k % 10)
            k //= 10
        return res[::-1]
```

## Python3

```python
from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        carry = 0
        res = []
        while i >= 0 or k > 0:
            digit_k = k % 10
            if i >= 0:
                total = num[i] + digit_k + carry
                i -= 1
            else:
                total = digit_k + carry
            res.append(total % 10)
            carry = total // 10
            k //= 10
        if carry:
            res.append(carry)
        return res[::-1]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* addToArrayForm(int* num, int numSize, int k, int* returnSize) {
    // Determine maximum possible length of the result
    int tempK = k;
    int kDigits = 0;
    if (tempK == 0) {
        kDigits = 1;
    } else {
        while (tempK > 0) {
            kDigits++;
            tempK /= 10;
        }
    }
    int capacity = (numSize > kDigits ? numSize : kDigits) + 2; // extra for possible carry

    int *tmp = (int *)malloc(sizeof(int) * capacity);
    int idx = 0;
    int i = numSize - 1;
    int carry = 0;

    while (i >= 0 || k > 0 || carry) {
        int sum = carry;
        if (i >= 0) {
            sum += num[i];
            i--;
        }
        if (k > 0) {
            sum += k % 10;
            k /= 10;
        }
        tmp[idx++] = sum % 10;
        carry = sum / 10;
    }

    *returnSize = idx;
    int *res = (int *)malloc(sizeof(int) * idx);
    for (int j = 0; j < idx; ++j) {
        res[j] = tmp[idx - 1 - j];
    }
    free(tmp);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> AddToArrayForm(int[] num, int k) {
        var result = new List<int>();
        int i = num.Length - 1;
        while (i >= 0 || k > 0) {
            if (i >= 0) {
                k += num[i];
                i--;
            }
            result.Add(k % 10);
            k /= 10;
        }
        result.Reverse();
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function(num, k) {
    let i = num.length - 1;
    let carry = 0;
    const res = [];
    while (i >= 0 || k > 0 || carry) {
        const n = i >= 0 ? num[i] : 0;
        const sum = n + (k % 10) + carry;
        res.push(sum % 10);
        carry = Math.floor(sum / 10);
        k = Math.floor(k / 10);
        i--;
    }
    return res.reverse();
};
```

## Typescript

```typescript
function addToArrayForm(num: number[], k: number): number[] {
    const res: number[] = [];
    let i = num.length - 1;
    let carry = 0;
    while (i >= 0 || k > 0) {
        const digitNum = i >= 0 ? num[i] : 0;
        const digitK = k % 10;
        const sum = digitNum + digitK + carry;
        res.push(sum % 10);
        carry = Math.floor(sum / 10);
        i--;
        k = Math.floor(k / 10);
    }
    if (carry) {
        res.push(carry);
    }
    return res.reverse();
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $num
     * @param Integer $k
     * @return Integer[]
     */
    function addToArrayForm($num, $k) {
        $i = count($num) - 1;
        $carry = $k;
        $res = [];

        while ($i >= 0 || $carry > 0) {
            if ($i >= 0) {
                $carry += $num[$i];
                $i--;
            }
            $res[] = $carry % 10;
            $carry = intdiv($carry, 10);
        }

        return array_reverse($res);
    }
}
```

## Swift

```swift
class Solution {
    func addToArrayForm(_ num: [Int], _ k: Int) -> [Int] {
        var i = num.count - 1
        var carry = k
        var result = [Int]()
        while i >= 0 || carry > 0 {
            let digit = i >= 0 ? num[i] : 0
            let sum = digit + carry
            result.append(sum % 10)
            carry = sum / 10
            i -= 1
        }
        return Array(result.reversed())
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun addToArrayForm(num: IntArray, k: Int): List<Int> {
        var carry = k
        val result = ArrayList<Int>()
        var i = num.size - 1
        while (i >= 0 || carry > 0) {
            if (i >= 0) {
                carry += num[i]
            }
            result.add(carry % 10)
            carry /= 10
            i--
        }
        result.reverse()
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> addToArrayForm(List<int> num, int k) {
    List<int> result = [];
    int i = num.length - 1;
    int carry = 0;

    while (i >= 0 || k > 0) {
      int n = i >= 0 ? num[i] : 0;
      int sum = n + (k % 10) + carry;
      result.add(sum % 10);
      carry = sum ~/ 10;
      k ~/= 10;
      i--;
    }

    while (carry > 0) {
      result.add(carry % 10);
      carry ~/= 10;
    }

    return result.reversed.toList();
  }
}
```

## Golang

```go
func addToArrayForm(num []int, k int) []int {
	i := len(num) - 1
	res := []int{}
	for i >= 0 || k > 0 {
		if i >= 0 {
			k += num[i]
			i--
		}
		res = append(res, k%10)
		k /= 10
	}
	// reverse the result slice
	for l, r := 0, len(res)-1; l < r; l, r = l+1, r-1 {
		res[l], res[r] = res[r], res[l]
	}
	return res
}
```

## Ruby

```ruby
def add_to_array_form(num, k)
  i = num.length - 1
  carry = 0
  res = []
  while i >= 0 || k > 0 || carry > 0
    digit_k = k % 10
    sum = (i >= 0 ? num[i] : 0) + digit_k + carry
    res << sum % 10
    carry = sum / 10
    i -= 1
    k /= 10
  end
  res.reverse!
end
```

## Scala

```scala
object Solution {
    def addToArrayForm(num: Array[Int], k: Int): List[Int] = {
        var i = num.length - 1
        var carry = k
        val digits = scala.collection.mutable.ListBuffer[Int]()
        while (i >= 0 || carry > 0) {
            if (i >= 0) {
                carry += num(i)
                i -= 1
            }
            digits.append(carry % 10)
            carry /= 10
        }
        digits.reverse.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn add_to_array_form(num: Vec<i32>, k: i32) -> Vec<i32> {
        let mut i = num.len() as i64;
        let mut carry: i64 = k as i64;
        let mut res: Vec<i32> = Vec::new();
        while i > 0 || carry > 0 {
            if i > 0 {
                i -= 1;
                carry += num[i as usize] as i64;
            }
            res.push((carry % 10) as i32);
            carry /= 10;
        }
        res.reverse();
        res
    }
}
```

## Racket

```racket
(define/contract (add-to-array-form num k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let ((rev-num (reverse num)))
    (let loop ((digits rev-num) (k k) (carry 0) (acc '()))
      (if (and (null? digits) (= k 0) (= carry 0))
          (reverse acc)
          (let* ((d (if (null? digits) 0 (car digits)))
                 (rest (if (null? digits) '() (cdr digits)))
                 (sum (+ d (modulo k 10) carry))
                 (new-digit (modulo sum 10))
                 (new-carry (quotient sum 10)))
            (loop rest (quotient k 10) new-carry (cons new-digit acc)))))))
```

## Erlang

```erlang
-spec add_to_array_form(Num :: [integer()], K :: integer()) -> [integer()].
add_to_array_form(Num, K) ->
    Rev = lists:reverse(Num),
    ResultRev = add_rev(Rev, K, 0, []),
    lists:reverse(ResultRev).

add_rev([], 0, 0, Acc) -> Acc;
add_rev([], K, Carry, Acc) ->
    DigitK = K rem 10,
    Sum = DigitK + Carry,
    NewDigit = Sum rem 10,
    NewCarry = Sum div 10,
    add_rev([], K div 10, NewCarry, [NewDigit|Acc]);
add_rev([D|Rest], K, Carry, Acc) ->
    DigitK = K rem 10,
    Sum = D + DigitK + Carry,
    NewDigit = Sum rem 10,
    NewCarry = Sum div 10,
    add_rev(Rest, K div 10, NewCarry, [NewDigit|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec add_to_array_form(num :: [integer], k :: integer) :: [integer]
  def add_to_array_form(num, k) do
    {result, carry} =
      Enum.reduce(Enum.reverse(num), {[], k}, fn digit, {acc, c} ->
        sum = digit + c
        {[rem(sum, 10) | acc], div(sum, 10)}
      end)

    if carry == 0 do
      result
    else
      Integer.digits(carry) ++ result
    end
  end
end
```
