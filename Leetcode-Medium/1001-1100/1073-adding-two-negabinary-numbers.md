# 1073. Adding Two Negabinary Numbers

## Cpp

```cpp
class Solution {
public:
    vector<int> addNegabinary(vector<int>& arr1, vector<int>& arr2) {
        int i = (int)arr1.size() - 1;
        int j = (int)arr2.size() - 1;
        int carry = 0;
        vector<int> revRes; // least significant bit first
        while (i >= 0 || j >= 0 || carry != 0) {
            int a = (i >= 0) ? arr1[i] : 0;
            int b = (j >= 0) ? arr2[j] : 0;
            int sum = a + b + carry;
            int digit = sum & 1; // remainder modulo 2 (0 or 1)
            revRes.push_back(digit);
            carry = (sum - digit) / -2;
            --i;
            --j;
        }
        // remove leading zeros after reversing
        while (revRes.size() > 1 && revRes.back() == 0) {
            revRes.pop_back();
        }
        reverse(revRes.begin(), revRes.end());
        return revRes;
    }
};
```

## Java

```java
class Solution {
    public int[] addNegabinary(int[] arr1, int[] arr2) {
        int i = arr1.length - 1;
        int j = arr2.length - 1;
        int carry = 0;
        java.util.ArrayList<Integer> list = new java.util.ArrayList<>();
        while (i >= 0 || j >= 0 || carry != 0) {
            int a = i >= 0 ? arr1[i] : 0;
            int b = j >= 0 ? arr2[j] : 0;
            int sum = a + b + carry;
            int bit = sum & 1; // parity (0 or 1)
            list.add(bit);
            carry = (sum - bit) / -2;
            i--;
            j--;
        }
        while (list.size() > 1 && list.get(list.size() - 1) == 0) {
            list.remove(list.size() - 1);
        }
        int n = list.size();
        int[] res = new int[n];
        for (int k = 0; k < n; k++) {
            res[k] = list.get(n - 1 - k);
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry != 0:
            s = carry
            if i >= 0:
                s += arr1[i]
                i -= 1
            if j >= 0:
                s += arr2[j]
                j -= 1
            digit = s & 1
            res.append(digit)
            carry = -(s - digit) // 2
        # reverse and strip leading zeros
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]
```

## Python3

```python
from typing import List

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += arr1[i]
                i -= 1
            if j >= 0:
                total += arr2[j]
                j -= 1
            res.append(total & 1)
            carry = -(total >> 1)
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* addNegabinary(int* arr1, int arr1Size, int* arr2, int arr2Size, int* returnSize) {
    int maxLen = arr1Size > arr2Size ? arr1Size : arr2Size;
    int capacity = maxLen + 10; // enough space for possible carry overflow
    int *temp = (int*)malloc(sizeof(int) * capacity);
    int idx = 0;

    int i = arr1Size - 1;
    int j = arr2Size - 1;
    int carry = 0;

    while (i >= 0 || j >= 0 || carry != 0) {
        int sum = carry;
        if (i >= 0) sum += arr1[i--];
        if (j >= 0) sum += arr2[j--];

        int digit = sum & 1;          // parity gives the current bit (0 or 1)
        temp[idx++] = digit;

        carry = (sum - digit) / -2;   // new carry for base -2
    }

    // Remove leading zeros from most‑significant side (which is at idx-1)
    int msb = idx - 1;
    while (msb > 0 && temp[msb] == 0) {
        msb--;
    }
    int len = msb + 1;

    int *result = (int*)malloc(sizeof(int) * len);
    for (int k = 0; k < len; ++k) {
        result[k] = temp[len - 1 - k]; // reverse to most‑significant first
    }

    *returnSize = len;
    free(temp);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] AddNegabinary(int[] arr1, int[] arr2) {
        var result = new System.Collections.Generic.List<int>();
        int i = arr1.Length - 1;
        int j = arr2.Length - 1;
        int carry = 0;
        while (i >= 0 || j >= 0 || carry != 0) {
            int a = i >= 0 ? arr1[i] : 0;
            int b = j >= 0 ? arr2[j] : 0;
            int sum = a + b + carry;
            int digit = sum & 1; // remainder modulo 2 (non‑negative)
            result.Add(digit);
            carry = -(sum - digit) / 2;
            i--;
            j--;
        }
        while (result.Count > 1 && result[result.Count - 1] == 0) {
            result.RemoveAt(result.Count - 1);
        }
        result.Reverse();
        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var addNegabinary = function(arr1, arr2) {
    let i = arr1.length - 1;
    let j = arr2.length - 1;
    let carry = 0;
    const res = [];
    
    while (i >= 0 || j >= 0 || carry !== 0) {
        let sum = carry;
        if (i >= 0) sum += arr1[i--];
        if (j >= 0) sum += arr2[j--];
        
        // digit is sum modulo 2 (non‑negative)
        const digit = sum & 1;   // works for negative sums as well
        res.push(digit);
        // new carry for base -2
        carry = (sum - digit) / -2;
    }
    
    // reverse and remove leading zeros
    while (res.length > 1 && res[res.length - 1] === 0) {
        res.pop();
    }
    return res.reverse();
};
```

## Typescript

```typescript
function addNegabinary(arr1: number[], arr2: number[]): number[] {
    let i = arr1.length - 1;
    let j = arr2.length - 1;
    let carry = 0;
    const res: number[] = [];
    while (i >= 0 || j >= 0 || carry !== 0) {
        let sum = carry;
        if (i >= 0) sum += arr1[i--];
        if (j >= 0) sum += arr2[j--];
        const digit = sum & 1; // parity gives 0 or 1
        res.push(digit);
        carry = (sum - digit) / -2;
    }
    while (res.length > 1 && res[res.length - 1] === 0) {
        res.pop();
    }
    return res.reverse();
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer[]
     */
    function addNegabinary($arr1, $arr2) {
        $i = count($arr1) - 1;
        $j = count($arr2) - 1;
        $carry = 0;
        $res = [];

        while ($i >= 0 || $j >= 0 || $carry != 0) {
            $total = $carry;
            if ($i >= 0) {
                $total += $arr1[$i];
                $i--;
            }
            if ($j >= 0) {
                $total += $arr2[$j];
                $j--;
            }

            // digit is parity of total (0 or 1)
            $digit = $total & 1;
            $res[] = $digit;

            // new carry
            $carry = intdiv($total - $digit, -2);
        }

        $res = array_reverse($res);

        // remove leading zeros, keep at least one digit
        $idx = 0;
        $len = count($res);
        while ($idx < $len - 1 && $res[$idx] == 0) {
            $idx++;
        }
        return array_slice($res, $idx);
    }
}
```

## Swift

```swift
class Solution {
    func addNegabinary(_ arr1: [Int], _ arr2: [Int]) -> [Int] {
        var a = Array(arr1.reversed())
        var b = Array(arr2.reversed())
        let maxLen = max(a.count, b.count)
        var carry = 0
        var res = [Int]()
        
        for i in 0..<maxLen {
            var sum = carry
            if i < a.count { sum += a[i] }
            if i < b.count { sum += b[i] }
            let bit = ((sum % 2) + 2) % 2          // ensure 0 or 1
            let k = (sum - bit) / 2                // integer division
            carry = -k
            res.append(bit)
        }
        
        while carry != 0 {
            var sum = carry
            let bit = ((sum % 2) + 2) % 2
            let k = (sum - bit) / 2
            carry = -k
            res.append(bit)
        }
        
        // Remove leading zeros (which are at the end of the reversed array)
        while res.count > 1 && res.last == 0 {
            res.removeLast()
        }
        
        return res.reversed()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun addNegabinary(arr1: IntArray, arr2: IntArray): IntArray {
        var i = arr1.size - 1
        var j = arr2.size - 1
        var carry = 0
        val digits = mutableListOf<Int>() // LSB first

        while (i >= 0 || j >= 0 || carry != 0) {
            val a = if (i >= 0) arr1[i] else 0
            val b = if (j >= 0) arr2[j] else 0
            var sum = a + b + carry

            val digit = sum and 1          // remainder modulo 2 (0 or 1)
            digits.add(digit)

            sum -= digit                    // make it even
            carry = sum / -2                // new carry for base -2

            i--
            j--
        }

        // Remove leading zeros (most significant side)
        while (digits.size > 1 && digits.last() == 0) {
            digits.removeAt(digits.size - 1)
        }

        // Reverse to get MSB -> LSB order
        val result = IntArray(digits.size)
        for (k in digits.indices) {
            result[k] = digits[digits.size - 1 - k]
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> addNegabinary(List<int> arr1, List<int> arr2) {
    int i = arr1.length - 1;
    int j = arr2.length - 1;
    int carry = 0;
    List<int> rev = [];

    while (i >= 0 || j >= 0 || carry != 0) {
      int sum = carry;
      if (i >= 0) {
        sum += arr1[i];
        i--;
      }
      if (j >= 0) {
        sum += arr2[j];
        j--;
      }
      int digit = sum & 1; // equivalent to sum % 2 but always non‑negative
      rev.add(digit);
      carry = -(sum - digit) ~/ 2;
    }

    while (rev.length > 1 && rev.last == 0) {
      rev.removeLast();
    }
    return rev.reversed.toList();
  }
}
```

## Golang

```go
func addNegabinary(arr1 []int, arr2 []int) []int {
    i, j := len(arr1)-1, len(arr2)-1
    carry := 0
    res := make([]int, 0)
    for i >= 0 || j >= 0 || carry != 0 {
        sum := carry
        if i >= 0 {
            sum += arr1[i]
            i--
        }
        if j >= 0 {
            sum += arr2[j]
            j--
        }
        digit := sum & 1
        res = append(res, digit)
        carry = (sum - digit) / -2
    }
    // reverse the result
    for l, r := 0, len(res)-1; l < r; l, r = l+1, r-1 {
        res[l], res[r] = res[r], res[l]
    }
    // trim leading zeros, keep at least one digit
    idx := 0
    for idx < len(res)-1 && res[idx] == 0 {
        idx++
    }
    return res[idx:]
}
```

## Ruby

```ruby
def add_negabinary(arr1, arr2)
  a = arr1.reverse
  b = arr2.reverse
  max_len = [a.length, b.length].max + 5
  sum = Array.new(max_len, 0)

  a.each_with_index { |v, i| sum[i] += v }
  b.each_with_index { |v, i| sum[i] += v }

  (0...sum.length - 1).each do |i|
    while sum[i] < 0 || sum[i] > 1
      if sum[i] < 0
        sum[i] += 2
        sum[i + 1] += 1
      else # sum[i] > 1
        sum[i] -= 2
        sum[i + 1] -= 1
      end
    end
  end

  last = sum.rindex { |v| v != 0 }
  return [0] if last.nil?
  sum[0..last].reverse
end
```

## Scala

```scala
object Solution {
    def addNegabinary(arr1: Array[Int], arr2: Array[Int]): Array[Int] = {
        val aRev = arr1.reverse
        val bRev = arr2.reverse
        val maxLen = math.max(aRev.length, bRev.length)
        var carry = 0
        val buf = scala.collection.mutable.ArrayBuffer[Int]()
        var i = 0
        while (i < maxLen || carry != 0) {
            val a = if (i < aRev.length) aRev(i) else 0
            val b = if (i < bRev.length) bRev(i) else 0
            val sum = a + b + carry
            val digit = ((sum % 2) + 2) % 2
            buf.append(digit)
            carry = (sum - digit) / -2
            i += 1
        }
        var res = buf.toArray.reverse
        var idx = 0
        while (idx < res.length - 1 && res(idx) == 0) {
            idx += 1
        }
        if (idx > 0) res = res.drop(idx)
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn add_negabinary(arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {
        let n1 = arr1.len();
        let n2 = arr2.len();
        let mut i = 0usize;
        let mut carry: i64 = 0;
        let mut res: Vec<i32> = Vec::new();

        while i < n1 || i < n2 || carry != 0 {
            let mut sum = carry;
            if i < n1 {
                sum += arr1[n1 - 1 - i] as i64;
            }
            if i < n2 {
                sum += arr2[n2 - 1 - i] as i64;
            }

            // digit must be 0 or 1; take least significant bit
            let digit = (sum & 1) as i32;
            res.push(digit);
            // update carry for base -2
            carry = (sum - digit as i64) / -2;
            i += 1;
        }

        // remove leading zeros
        while res.len() > 1 && *res.last().unwrap() == 0 {
            res.pop();
        }
        res.reverse();
        res
    }
}
```

## Racket

```racket
(define/contract (add-negabinary arr1 arr2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((v1 (list->vector arr1))
         (v2 (list->vector arr2))
         (len1 (vector-length v1))
         (len2 (vector-length v2)))
    (let loop ((i (sub1 len1)) (j (sub1 len2)) (carry 0) (res '()))
      (if (and (< i 0) (< j 0) (= carry 0))
          (let ((ans (reverse res)))
            (let strip ((lst ans))
              (cond [(null? lst) '(0)]
                    [(and (= (car lst) 0) (not (null? (cdr lst)))) (strip (cdr lst))]
                    [else lst])))
          (let* ((sum carry)
                 (sum (if (>= i 0) (+ sum (vector-ref v1 i)) sum))
                 (sum (if (>= j 0) (+ sum (vector-ref v2 j)) sum))
                 (bit (bitwise-and sum 1))
                 (new-carry (- (arithmetic-shift sum -1)))
                 (next-i (if (>= i 0) (sub1 i) i))
                 (next-j (if (>= j 0) (sub1 j) j)))
            (loop next-i next-j new-carry (cons bit res)))))))
```

## Erlang

```erlang
-spec add_negabinary([integer()], [integer()]) -> [integer()].
add_negabinary(Arr1, Arr2) ->
    Rev1 = lists:reverse(Arr1),
    Rev2 = lists:reverse(Arr2),
    Res = add_rev(Rev1, Rev2, 0, []),
    Trimmed = trim_leading_zeros(Res),
    case Trimmed of
        [] -> [0];
        _  -> Trimmed
    end.

add_rev([], [], 0, Acc) ->
    Acc;
add_rev(L1, L2, Carry, Acc) ->
    {A, Rest1} = case L1 of
                     []      -> {0, []};
                     [H|T]   -> {H, T}
                 end,
    {B, Rest2} = case L2 of
                     []      -> {0, []};
                     [H|T]   -> {H, T}
                 end,
    Sum = A + B + Carry,
    Digit = Sum band 1,
    NewCarry = -(Sum - Digit) div 2,
    add_rev(Rest1, Rest2, NewCarry, [Digit | Acc]).

trim_leading_zeros([0|T]) ->
    trim_leading_zeros(T);
trim_leading_zeros(L) ->
    L.
```

## Elixir

```elixir
defmodule Solution do
  @spec add_negabinary(arr1 :: [integer], arr2 :: [integer]) :: [integer]
  def add_negabinary(arr1, arr2) do
    rev1 = :lists.reverse(arr1)
    rev2 = :lists.reverse(arr2)
    max_len = max(length(rev1), length(rev2))
    result_rev = loop(0, 0, [], rev1, rev2, max_len)
    result = Enum.reverse(result_rev)
    trim_leading_zeros(result)
  end

  defp loop(i, carry, acc, rev1, rev2, max_len) when i < max_len or carry != 0 do
    a = if i < length(rev1), do: Enum.at(rev1, i), else: 0
    b = if i < length(rev2), do: Enum.at(rev2, i), else: 0
    total = a + b + carry
    digit = Integer.mod(total, 2)
    new_carry = div(total - digit, -2)
    loop(i + 1, new_carry, [digit | acc], rev1, rev2, max_len)
  end

  defp loop(_i, _carry, acc, _rev1, _rev2, _max_len), do: acc

  defp trim_leading_zeros(list) do
    trimmed = Enum.drop_while(list, fn x -> x == 0 end)
    if trimmed == [], do: [0], else: trimmed
  end
end
```
