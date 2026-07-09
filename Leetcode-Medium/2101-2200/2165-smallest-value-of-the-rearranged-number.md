# 2165. Smallest Value of the Rearranged Number

## Cpp

```cpp
class Solution {
public:
    long long smallestNumber(long long num) {
        if (num == 0) return 0;
        bool negative = num < 0;
        long long x = std::llabs(num);
        std::string s = std::to_string(x);
        if (!negative) {
            std::sort(s.begin(), s.end());
            // place smallest non-zero at front
            size_t i = 0;
            while (i < s.size() && s[i] == '0') ++i;
            if (i < s.size()) {
                std::swap(s[0], s[i]);
            }
        } else {
            std::sort(s.begin(), s.end(), std::greater<char>());
        }
        long long res = 0;
        for (char c : s) {
            res = res * 10 + (c - '0');
        }
        return negative ? -res : res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long smallestNumber(long num) {
        if (num == 0) return 0;
        boolean negative = num < 0;
        char[] digits = Long.toString(Math.abs(num)).toCharArray();
        Arrays.sort(digits);
        if (!negative) {
            int i = 0;
            while (i < digits.length && digits[i] == '0') i++;
            if (i > 0 && i < digits.length) {
                char temp = digits[0];
                digits[0] = digits[i];
                digits[i] = temp;
            }
            return Long.parseLong(new String(digits));
        } else {
            int n = digits.length;
            for (int i = 0; i < n / 2; i++) {
                char tmp = digits[i];
                digits[i] = digits[n - 1 - i];
                digits[n - 1 - i] = tmp;
            }
            return -Long.parseLong(new String(digits));
        }
    }
}
```

## Python

```python
class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        if num > 0:
            digits = sorted(str(num))
            # place the smallest non-zero digit at front to avoid leading zeros
            if digits[0] == '0':
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            return int(''.join(digits))
        else:
            # negative: maximize the absolute value by sorting descending
            digits = sorted(str(-num), reverse=True)
            return -int(''.join(digits))
```

## Python3

```python
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num > 0:
            digits = sorted(str(num))
            # place first non-zero digit at front
            for i, d in enumerate(digits):
                if d != '0':
                    # swap with first position
                    digits[0], digits[i] = digits[i], digits[0]
                    break
            return int(''.join(digits))
        else:
            digits = sorted(str(-num), reverse=True)
            return -int(''.join(digits))
```

## C

```c
#include <stdlib.h>

static int cmp_asc(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

static int cmp_desc(const void *a, const void *b) {
    return (*(const int *)b) - (*(const int *)a);
}

long long smallestNumber(long long num) {
    if (num == 0) return 0;
    int neg = num < 0;
    long long x = llabs(num);
    int digits[20];
    int n = 0;
    while (x > 0) {
        digits[n++] = (int)(x % 10);
        x /= 10;
    }
    if (!neg) {
        qsort(digits, n, sizeof(int), cmp_asc);
        if (digits[0] == 0) {
            int i = 1;
            while (i < n && digits[i] == 0) ++i;
            if (i < n) {
                int tmp = digits[0];
                digits[0] = digits[i];
                digits[i] = tmp;
            }
        }
    } else {
        qsort(digits, n, sizeof(int), cmp_desc);
    }
    long long res = 0;
    for (int i = 0; i < n; ++i) {
        res = res * 10 + digits[i];
    }
    return neg ? -res : res;
}
```

## Csharp

```csharp
public class Solution
{
    public long SmallestNumber(long num)
    {
        if (num == 0) return 0;
        bool negative = num < 0;
        string s = Math.Abs(num).ToString();
        char[] digits = s.ToCharArray();
        System.Array.Sort(digits); // ascending

        if (!negative)
        {
            int i = 0;
            while (i < digits.Length && digits[i] == '0') i++;
            if (i > 0 && i < digits.Length)
            {
                char temp = digits[0];
                digits[0] = digits[i];
                digits[i] = temp;
            }
            return long.Parse(new string(digits));
        }
        else
        {
            System.Array.Reverse(digits); // descending
            return -long.Parse(new string(digits));
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var smallestNumber = function(num) {
    if (num === 0) return 0;
    if (num > 0) {
        const digits = String(num).split('').sort();
        if (digits[0] === '0') {
            let i = 0;
            while (i < digits.length && digits[i] === '0') i++;
            // swap first non-zero with the leading zero
            [digits[0], digits[i]] = [digits[i], digits[0]];
        }
        return Number(digits.join(''));
    } else {
        const digits = String(-num).split('').sort((a, b) => b - a);
        return -Number(digits.join(''));
    }
};
```

## Typescript

```typescript
function smallestNumber(num: number): number {
    if (num === 0) return 0;
    const sign = Math.sign(num);
    let digits = Math.abs(num).toString().split('');
    if (sign > 0) {
        digits.sort(); // ascending
        if (digits[0] === '0') {
            let i = 1;
            while (i < digits.length && digits[i] === '0') i++;
            if (i < digits.length) {
                [digits[0], digits[i]] = [digits[i], digits[0]];
            }
        }
        return Number(digits.join(''));
    } else {
        digits.sort((a, b) => b.localeCompare(a)); // descending
        return Number('-' + digits.join(''));
    }
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function smallestNumber($num) {
        if ($num == 0) {
            return 0;
        }
        $sign = $num > 0 ? 1 : -1;
        $digits = str_split(strval(abs($num)));
        sort($digits); // ascending
        
        if ($sign > 0) {
            // place the smallest non-zero digit at the front
            foreach ($digits as $i => $d) {
                if ($d !== '0') {
                    if ($i != 0) {
                        $tmp = $digits[0];
                        $digits[0] = $digits[$i];
                        $digits[$i] = $tmp;
                    }
                    break;
                }
            }
            $resultStr = implode('', $digits);
            return intval($resultStr);
        } else {
            // for negative numbers, arrange digits in descending order
            rsort($digits); // descending
            $resultStr = implode('', $digits);
            return -intval($resultStr);
        }
    }
}
```

## Swift

```swift
class Solution {
    func smallestNumber(_ num: Int) -> Int {
        if num == 0 { return 0 }
        let sign = num >= 0 ? 1 : -1
        var digits = Array(String(abs(num)))
        if sign > 0 {
            digits.sort()
            if let idx = digits.firstIndex(where: { $0 != "0" }) {
                if idx != 0 {
                    digits.swapAt(0, idx)
                }
            }
        } else {
            digits.sort(by: >)
        }
        let rearranged = Int(String(digits))!
        return rearranged * sign
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestNumber(num: Long): Long {
        if (num == 0L) return 0L
        val isNeg = num < 0
        val chars = kotlin.math.abs(num).toString().toCharArray()
        if (!isNeg) {
            chars.sort()
            var i = 0
            while (i < chars.size && chars[i] == '0') i++
            if (i < chars.size) {
                val tmp = chars[0]
                chars[0] = chars[i]
                chars[i] = tmp
            }
            return String(chars).toLong()
        } else {
            chars.sort()
            var l = 0
            var r = chars.lastIndex
            while (l < r) {
                val tmp = chars[l]
                chars[l] = chars[r]
                chars[r] = tmp
                l++
                r--
            }
            return -String(chars).toLong()
        }
    }
}
```

## Dart

```dart
class Solution {
  int smallestNumber(int num) {
    if (num == 0) return 0;
    bool negative = num < 0;
    int absNum = num.abs();
    List<int> digits = absNum.toString().split('').map(int.parse).toList();

    if (!negative) {
      digits.sort(); // ascending
      if (digits[0] == 0) {
        for (int i = 1; i < digits.length; ++i) {
          if (digits[i] != 0) {
            int temp = digits[0];
            digits[0] = digits[i];
            digits[i] = temp;
            break;
          }
        }
      }
    } else {
      // descending for negative numbers
      digits.sort((a, b) => b.compareTo(a));
    }

    int result = 0;
    for (int d in digits) {
      result = result * 10 + d;
    }
    return negative ? -result : result;
  }
}
```

## Golang

```go
import "sort"

func smallestNumber(num int64) int64 {
	if num == 0 {
		return 0
	}
	sign := 1
	if num < 0 {
		sign = -1
	}
	n := num
	if n < 0 {
		n = -n
	}

	var digits []int
	for n > 0 {
		digits = append(digits, int(n%10))
		n /= 10
	}

	if sign == 1 {
		sort.Ints(digits)
		// place the smallest non-zero digit at the front
		idx := 0
		for idx < len(digits) && digits[idx] == 0 {
			idx++
		}
		if idx > 0 && idx < len(digits) {
			digits[0], digits[idx] = digits[idx], digits[0]
		}
	} else {
		sort.Sort(sort.Reverse(sort.IntSlice(digits)))
	}

	var res int64
	for _, d := range digits {
		res = res*10 + int64(d)
	}
	if sign == -1 {
		res = -res
	}
	return res
}
```

## Ruby

```ruby
def smallest_number(num)
  if num >= 0
    digits = num.to_s.chars.sort
    if digits[0] == '0' && digits.size > 1
      i = digits.find_index { |d| d != '0' }
      digits[0], digits[i] = digits[i], digits[0] if i
    end
    digits.join.to_i
  else
    digits = num.abs.to_s.chars.sort.reverse
    -digits.join.to_i
  end
end
```

## Scala

```scala
object Solution {
    def smallestNumber(num: Long): Long = {
        if (num == 0) return 0L
        val isNeg = num < 0
        val chars = math.abs(num).toString.toCharArray
        if (!isNeg) {
            java.util.Arrays.sort(chars)
            var i = 0
            while (i < chars.length && chars(i) == '0') i += 1
            if (i > 0 && i < chars.length) {
                val tmp = chars(0)
                chars(0) = chars(i)
                chars(i) = tmp
            }
            new String(chars).toLong
        } else {
            java.util.Arrays.sort(chars) // ascending
            var l = 0
            var r = chars.length - 1
            while (l < r) {
                val tmp = chars(l)
                chars(l) = chars(r)
                chars(r) = tmp
                l += 1
                r -= 1
            }
            -new String(chars).toLong
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_number(num: i64) -> i64 {
        if num == 0 {
            return 0;
        }
        let sign = if num < 0 { -1 } else { 1 };
        let mut n = num.abs() as u64;
        let mut digits: Vec<u8> = Vec::new();
        while n > 0 {
            digits.push((n % 10) as u8);
            n /= 10;
        }
        if sign == 1 {
            digits.sort(); // ascending
            if digits[0] == 0 {
                let mut idx = 0usize;
                while idx < digits.len() && digits[idx] == 0 {
                    idx += 1;
                }
                digits.swap(0, idx);
            }
        } else {
            digits.sort_by(|a, b| b.cmp(a)); // descending
        }

        let mut result: i64 = 0;
        for d in digits {
            result = result * 10 + d as i64;
        }
        if sign == -1 { -result } else { result }
    }
}
```

## Racket

```racket
(define/contract (smallest-number num)
  (-> exact-integer? exact-integer?)
  (if (= num 0)
      0
      (let* ([abs-num (abs num)]
             [s (number->string abs-num)])
        (if (> num 0)
            ;; positive number: smallest non‑zero digit first, then ascending order
            (let* ([sorted (sort (string->list s) char<?)]
                   [zeros   (filter (lambda (c) (char=? c #\0)) sorted)]
                   [nonz    (filter (lambda (c) (not (char=? c #\0))) sorted)])
              (if (null? nonz)
                  0
                  (let* ([first-nz (car nonz)]
                         [rest-nz  (cdr nonz)]
                         [result-list (cons first-nz (append zeros rest-nz))]
                         [result-str (list->string result-list)])
                    (string->number result-str))))
            ;; negative number: arrange digits descending, then apply sign
            (let* ([sorted (sort (string->list s) char>?)]
                   [result-str (list->string sorted)]
                   [pos-num (string->number result-str)])
              (- pos-num))))))
```

## Erlang

```erlang
-module(solution).
-export([smallest_number/1]).

-spec smallest_number(integer()) -> integer().
smallest_number(Num) when Num >= 0 ->
    Digits = integer_to_list(Num),
    Sorted = lists:sort(Digits),
    NonZeros = [D || D <- Sorted, D =/= $0],
    case NonZeros of
        [] ->
            0;
        [_|_] ->
            First = hd(NonZeros),
            RestNonZeros = tl(NonZeros),
            Zeros = [D || D <- Sorted, D == $0],
            NewDigits = [First] ++ Zeros ++ RestNonZeros,
            list_to_integer(NewDigits)
    end;
smallest_number(Num) ->
    Abs = abs(Num),
    Digits = integer_to_list(Abs),
    SortedDesc = lists:reverse(lists:sort(Digits)),
    -list_to_integer(SortedDesc).
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_number(num :: integer) :: integer
  def smallest_number(num) do
    if num >= 0 do
      digits = Integer.digits(num)
      sorted = Enum.sort(digits)

      case sorted do
        [0 | _] ->
          {zeros, rest} = Enum.split_while(sorted, fn d -> d == 0 end)

          case rest do
            [] -> 0
            [first_nonzero | tail] ->
              new_digits = [first_nonzero] ++ zeros ++ tail
              Integer.undigits(new_digits)
          end

        _ ->
          Integer.undigits(sorted)
      end
    else
      abs = -num
      digits = Integer.digits(abs)
      sorted_desc = Enum.sort(digits, &>=/2)
      val = Integer.undigits(sorted_desc)
      -val
    end
  end
end
```
