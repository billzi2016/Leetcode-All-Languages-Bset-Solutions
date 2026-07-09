# 0556. Next Greater Element III

## Cpp

```cpp
class Solution {
public:
    int nextGreaterElement(int n) {
        string s = to_string(n);
        int i = (int)s.size() - 2;
        while (i >= 0 && s[i] >= s[i + 1]) --i;
        if (i < 0) return -1;
        int j = (int)s.size() - 1;
        while (j > i && s[j] <= s[i]) --j;
        swap(s[i], s[j]);
        reverse(s.begin() + i + 1, s.end());
        long long val = stoll(s);
        if (val > INT_MAX) return -1;
        return (int)val;
    }
};
```

## Java

```java
class Solution {
    public int nextGreaterElement(int n) {
        char[] digits = Integer.toString(n).toCharArray();
        int i = digits.length - 2;
        while (i >= 0 && digits[i] >= digits[i + 1]) {
            i--;
        }
        if (i < 0) return -1;
        int j = digits.length - 1;
        while (digits[j] <= digits[i]) {
            j--;
        }
        char tmp = digits[i];
        digits[i] = digits[j];
        digits[j] = tmp;
        int left = i + 1, right = digits.length - 1;
        while (left < right) {
            char t = digits[left];
            digits[left++] = digits[right];
            digits[right--] = t;
        }
        long result = Long.parseLong(new String(digits));
        return result > Integer.MAX_VALUE ? -1 : (int) result;
    }
}
```

## Python

```python
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = list(map(int, str(n)))
        i = len(digits) - 2
        # Find first digit that is smaller than the digit after it
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i < 0:
            return -1

        # Find the smallest digit greater than digits[i] to its right
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Swap and reverse the suffix
        digits[i], digits[j] = digits[j], digits[i]
        digits[i + 1:] = reversed(digits[i + 1:])

        result = int(''.join(map(str, digits)))
        return result if result <= 2**31 - 1 else -1
```

## Python3

```python
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i == -1:
            return -1
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
        digits[i], digits[j] = digits[j], digits[i]
        digits[i + 1:] = reversed(digits[i + 1:])
        res = int(''.join(digits))
        return res if res <= 2**31 - 1 else -1
```

## C

```c
#include <stdio.h>
#include <limits.h>

int nextGreaterElement(int n) {
    char s[12];
    int len = sprintf(s, "%d", n);
    
    int i = len - 2;
    while (i >= 0 && s[i] >= s[i + 1]) i--;
    if (i < 0) return -1;
    
    int j = len - 1;
    while (j > i && s[j] <= s[i]) j--;
    
    char tmp = s[i];
    s[i] = s[j];
    s[j] = tmp;
    
    int l = i + 1, r = len - 1;
    while (l < r) {
        tmp = s[l];
        s[l++] = s[r];
        s[r--] = tmp;
    }
    
    long long res = 0;
    for (int k = 0; k < len; ++k) {
        res = res * 10 + (s[k] - '0');
        if (res > INT_MAX) return -1;
    }
    return (int)res;
}
```

## Csharp

```csharp
public class Solution
{
    public int NextGreaterElement(int n)
    {
        char[] digits = n.ToString().ToCharArray();
        int i = digits.Length - 2;
        while (i >= 0 && digits[i] >= digits[i + 1])
            i--;
        if (i < 0) return -1;

        int j = digits.Length - 1;
        while (digits[j] <= digits[i])
            j--;

        char tmp = digits[i];
        digits[i] = digits[j];
        digits[j] = tmp;

        System.Array.Reverse(digits, i + 1, digits.Length - i - 1);

        long val = long.Parse(new string(digits));
        return val > int.MaxValue ? -1 : (int)val;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var nextGreaterElement = function(n) {
    const digits = String(n).split('').map(ch => Number(ch));
    let i = digits.length - 2;
    while (i >= 0 && digits[i] >= digits[i + 1]) {
        i--;
    }
    if (i < 0) return -1;

    let j = digits.length - 1;
    while (j > i && digits[j] <= digits[i]) {
        j--;
    }

    [digits[i], digits[j]] = [digits[j], digits[i]];

    // reverse the suffix starting at i+1
    for (let left = i + 1, right = digits.length - 1; left < right; left++, right--) {
        [digits[left], digits[right]] = [digits[right], digits[left]];
    }

    const result = Number(digits.join(''));
    return result > 0x7fffffff ? -1 : result;
};
```

## Typescript

```typescript
function nextGreaterElement(n: number): number {
    const digits = Array.from(String(n), ch => Number(ch));
    let i = digits.length - 2;
    while (i >= 0 && digits[i] >= digits[i + 1]) {
        i--;
    }
    if (i < 0) return -1;

    let j = digits.length - 1;
    while (j > i && digits[j] <= digits[i]) {
        j--;
    }

    [digits[i], digits[j]] = [digits[j], digits[i]];

    let left = i + 1, right = digits.length - 1;
    while (left < right) {
        [digits[left], digits[right]] = [digits[right], digits[left]];
        left++;
        right--;
    }

    const result = Number(digits.join(''));
    return result > 0x7fffffff ? -1 : result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function nextGreaterElement($n) {
        $digits = str_split((string)$n);
        $len = count($digits);

        // Find the first index from the right where digits[i] < digits[i+1]
        $i = $len - 2;
        while ($i >= 0 && $digits[$i] >= $digits[$i + 1]) {
            $i--;
        }
        if ($i < 0) {
            return -1; // No larger permutation
        }

        // Find the smallest digit on right side that is greater than digits[i]
        $j = $len - 1;
        while ($digits[$j] <= $digits[$i]) {
            $j--;
        }

        // Swap them
        $tmp = $digits[$i];
        $digits[$i] = $digits[$j];
        $digits[$j] = $tmp;

        // Sort the suffix to get the smallest possible number
        $suffix = array_slice($digits, $i + 1);
        sort($suffix, SORT_STRING); // single-digit strings sort correctly

        $newDigits = array_merge(array_slice($digits, 0, $i + 1), $suffix);
        $resultStr = implode('', $newDigits);

        // Check 32-bit signed integer overflow
        if (strlen($resultStr) > 10 || ($resultStr > '2147483647')) {
            return -1;
        }

        $result = (int)$resultStr;
        return $result <= 2147483647 ? $result : -1;
    }
}
```

## Swift

```swift
class Solution {
    func nextGreaterElement(_ n: Int) -> Int {
        var chars = Array(String(n))
        let len = chars.count
        var i = len - 2
        while i >= 0 && chars[i] >= chars[i + 1] {
            i -= 1
        }
        if i < 0 { return -1 }
        
        var j = len - 1
        while chars[j] <= chars[i] {
            j -= 1
        }
        chars.swapAt(i, j)
        
        var left = i + 1
        var right = len - 1
        while left < right {
            chars.swapAt(left, right)
            left += 1
            right -= 1
        }
        
        let resultStr = String(chars)
        if let val = Int64(resultStr), val <= Int64(Int32.max) {
            return Int(val)
        } else {
            return -1
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun nextGreaterElement(n: Int): Int {
        val chars = n.toString().toCharArray()
        var i = chars.size - 2
        while (i >= 0 && chars[i] >= chars[i + 1]) {
            i--
        }
        if (i < 0) return -1

        var j = chars.size - 1
        while (j > i && chars[j] <= chars[i]) {
            j--
        }

        // swap i and j
        val tmp = chars[i]
        chars[i] = chars[j]
        chars[j] = tmp

        // reverse the suffix starting at i+1
        var left = i + 1
        var right = chars.size - 1
        while (left < right) {
            val t = chars[left]
            chars[left] = chars[right]
            chars[right] = t
            left++
            right--
        }

        val result = String(chars).toLong()
        return if (result > Int.MAX_VALUE) -1 else result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int nextGreaterElement(int n) {
    const int INT_MAX = 2147483647;
    List<int> digits = n.toString().split('').map(int.parse).toList();

    int i = digits.length - 2;
    while (i >= 0 && digits[i] >= digits[i + 1]) {
      i--;
    }
    if (i < 0) return -1;

    int j = digits.length - 1;
    while (digits[j] <= digits[i]) {
      j--;
    }

    // swap
    int tmp = digits[i];
    digits[i] = digits[j];
    digits[j] = tmp;

    // reverse suffix
    int left = i + 1, right = digits.length - 1;
    while (left < right) {
      int t = digits[left];
      digits[left] = digits[right];
      digits[right] = t;
      left++;
      right--;
    }

    int result = 0;
    for (int d in digits) {
      result = result * 10 + d;
      if (result > INT_MAX) return -1;
    }
    return result;
  }
}
```

## Golang

```go
import "strconv"

func nextGreaterElement(n int) int {
	s := strconv.Itoa(n)
	b := []byte(s)

	i := len(b) - 2
	for i >= 0 && b[i] >= b[i+1] {
		i--
	}
	if i < 0 {
		return -1
	}

	j := len(b) - 1
	for j > i && b[j] <= b[i] {
		j--
	}

	b[i], b[j] = b[j], b[i]

	left, right := i+1, len(b)-1
	for left < right {
		b[left], b[right] = b[right], b[left]
		left++
		right--
	}

	var res int64
	const maxInt32 = 1<<31 - 1
	for _, ch := range b {
		res = res*10 + int64(ch-'0')
		if res > maxInt32 {
			return -1
		}
	}
	return int(res)
}
```

## Ruby

```ruby
def next_greater_element(n)
  digits = n.to_s.chars
  i = digits.length - 2
  while i >= 0 && digits[i] >= digits[i + 1]
    i -= 1
  end
  return -1 if i < 0

  j = digits.length - 1
  while digits[j] <= digits[i]
    j -= 1
  end

  digits[i], digits[j] = digits[j], digits[i]

  left = i + 1
  right = digits.length - 1
  while left < right
    digits[left], digits[right] = digits[right], digits[left]
    left += 1
    right -= 1
  end

  result = digits.join.to_i
  limit = 2**31 - 1
  result <= limit ? result : -1
end
```

## Scala

```scala
object Solution {
    def nextGreaterElement(n: Int): Int = {
        val chars = n.toString.toCharArray
        var i = chars.length - 2
        while (i >= 0 && chars(i) >= chars(i + 1)) {
            i -= 1
        }
        if (i < 0) return -1

        var j = chars.length - 1
        while (chars(j) <= chars(i)) {
            j -= 1
        }

        // swap chars(i) and chars(j)
        val tmp = chars(i)
        chars(i) = chars(j)
        chars(j) = tmp

        // reverse the suffix starting at i+1
        var left = i + 1
        var right = chars.length - 1
        while (left < right) {
            val t = chars(left)
            chars(left) = chars(right)
            chars(right) = t
            left += 1
            right -= 1
        }

        val resultLong = java.lang.Long.parseLong(new String(chars))
        if (resultLong > Int.MaxValue) -1 else resultLong.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn next_greater_element(n: i32) -> i32 {
        let mut digits = n.to_string().into_bytes();
        let len = digits.len();
        if len < 2 {
            return -1;
        }

        // Find the first index 'i' from the right where digits[i] < digits[i+1]
        let mut i: isize = (len as isize) - 2;
        while i >= 0 && digits[i as usize] >= digits[(i + 1) as usize] {
            i -= 1;
        }
        if i < 0 {
            return -1;
        }
        let i_usize = i as usize;

        // Find the smallest digit greater than digits[i] to its right
        let mut j = len - 1;
        while digits[j] <= digits[i_usize] {
            j -= 1;
        }

        // Swap and reverse the suffix
        digits.swap(i_usize, j);
        digits[(i_usize + 1)..].reverse();

        // Convert back to integer and check overflow
        let s = unsafe { String::from_utf8_unchecked(digits) };
        if let Ok(val) = s.parse::<i64>() {
            if val <= i32::MAX as i64 {
                return val as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (next-greater-element n)
  (-> exact-integer? exact-integer?)
  (let* ([s (number->string n)]
         [digits (list->vector
                  (map (lambda (c) (- (char->integer c) (char->integer #\0)))
                       (string->list s)))]
         [len (vector-length digits)])
    (define (find-i i)
      (if (< i 0)
          -1
          (if (< (vector-ref digits i) (vector-ref digits (+ i 1)))
              i
              (find-i (- i 1)))))
    (let ([i (find-i (- len 2))])
      (if (= i -1)
          -1
          (begin
            (define (find-j j)
              (if (> j i)
                  (if (> (vector-ref digits j) (vector-ref digits i))
                      j
                      (find-j (- j 1)))
                  #f))
            (let ([j (find-j (- len 1))])
              ;; swap i and j
              (let ([tmp (vector-ref digits i)])
                (vector-set! digits i (vector-ref digits j))
                (vector-set! digits j tmp))
              ;; reverse suffix i+1 .. len-1
              (let loop-rev ((l (+ i 1)) (r (- len 1)))
                (when (< l r)
                  (let ([tmp2 (vector-ref digits l)])
                    (vector-set! digits l (vector-ref digits r))
                    (vector-set! digits r tmp2))
                  (loop-rev (+ l 1) (- r 1))))
              ;; construct number
              (let loop-construct ((idx 0) (acc 0))
                (if (= idx len)
                    (if (> acc #x7fffffff) -1 acc)
                    (loop-construct (+ idx 1) (+ (* acc 10) (vector-ref digits idx)))))))))))
```

## Erlang

```erlang
-module(solution).
-export([next_greater_element/1]).

-spec next_greater_element(N :: integer()) -> integer().
next_greater_element(N) ->
    Digits = integer_to_list(N),
    case next_permutation(Digits) of
        false -> -1;
        NewDigits ->
            Val = list_to_integer(NewDigits),
            if Val =< 2147483647 -> Val; true -> -1 end
    end.

%% internal helpers

next_permutation(Digits) ->
    Tuple = list_to_tuple(Digits),
    Len = tuple_size(Tuple),
    case find_i(Tuple, Len - 2) of
        undefined -> false;
        I ->
            {Prefix, [Pivot|Rest]} = lists:split(I, Digits),
            J = find_j(Rest, Pivot),
            {RestPrefix, [Succ|RestSuffix]} = lists:split(J, Rest),
            NewPivot = Succ,
            NewSucc = Pivot,
            Suffix = RestPrefix ++ [NewSucc] ++ RestSuffix,
            SortedSuffix = lists:reverse(Suffix),
            Prefix ++ [NewPivot] ++ SortedSuffix
    end.

find_i(_Tuple, I) when I < 0 -> undefined;
find_i(Tuple, I) ->
    Elem = element(I + 1, Tuple),
    Next = element(I + 2, Tuple),
    if Elem < Next -> I; true -> find_i(Tuple, I - 1) end.

find_j(Rest, Pivot) ->
    Rev = lists:reverse(Rest),
    RevIdx = find_first_greater(Rev, Pivot, 0),
    LenRest = length(Rest),
    LenRest - RevIdx - 1.

find_first_greater([H|_], Pivot, Index) when H > Pivot -> Index;
find_first_greater([_|T], Pivot, Index) ->
    find_first_greater(T, Pivot, Index + 1);
find_first_greater([], _, _) -> undefined.
```

## Elixir

```elixir
defmodule Solution do
  @spec next_greater_element(n :: integer) :: integer
  def next_greater_element(n) do
    digits = Integer.digits(n)

    case next_permutation(digits) do
      nil -> -1
      perm ->
        result = Enum.reduce(perm, 0, fn d, acc -> acc * 10 + d end)
        if result <= 2_147_483_647, do: result, else: -1
    end
  end

  defp next_permutation(digits) do
    case find_i(digits) do
      nil -> nil
      i ->
        j = find_j(digits, i)
        val_i = Enum.at(digits, i)
        val_j = Enum.at(digits, j)

        swapped =
          digits
          |> List.replace_at(i, val_j)
          |> List.replace_at(j, val_i)

        prefix = Enum.take(swapped, i + 1)
        suffix = swapped |> Enum.drop(i + 1) |> Enum.reverse()
        prefix ++ suffix
    end
  end

  defp find_i(digits), do: find_i(digits, length(digits) - 2)

  defp find_i(_digits, -1), do: nil

  defp find_i(digits, i) do
    if Enum.at(digits, i) < Enum.at(digits, i + 1) do
      i
    else
      find_i(digits, i - 1)
    end
  end

  defp find_j(digits, i) do
    val_i = Enum.at(digits, i)
    find_j(digits, length(digits) - 1, val_i)
  end

  defp find_j(_digits, -1, _val_i), do: nil

  defp find_j(digits, j, val_i) do
    if Enum.at(digits, j) > val_i do
      j
    else
      find_j(digits, j - 1, val_i)
    end
  end
end
```
