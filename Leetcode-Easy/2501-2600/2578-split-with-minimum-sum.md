# 2578. Split With Minimum Sum

## Cpp

```cpp
class Solution {
public:
    int splitNum(int num) {
        string digits;
        while (num > 0) {
            digits.push_back('0' + (num % 10));
            num /= 10;
        }
        sort(digits.begin(), digits.end());
        string a, b;
        for (int i = 0; i < (int)digits.size(); ++i) {
            if (i % 2 == 0)
                a.push_back(digits[i]);
            else
                b.push_back(digits[i]);
        }
        int n1 = a.empty() ? 0 : stoi(a);
        int n2 = b.empty() ? 0 : stoi(b);
        return n1 + n2;
    }
};
```

## Java

```java
class Solution {
    public int splitNum(int num) {
        char[] digits = Integer.toString(num).toCharArray();
        java.util.Arrays.sort(digits);
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        for (int i = 0; i < digits.length; i++) {
            if ((i & 1) == 0) {
                sb1.append(digits[i]);
            } else {
                sb2.append(digits[i]);
            }
        }
        int n1 = sb1.length() == 0 ? 0 : Integer.parseInt(sb1.toString());
        int n2 = sb2.length() == 0 ? 0 : Integer.parseInt(sb2.toString());
        return n1 + n2;
    }
}
```

## Python

```python
class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = sorted(str(num))
        a = []
        b = []
        for i, d in enumerate(digits):
            if i % 2 == 0:
                a.append(d)
            else:
                b.append(d)
        num1 = int(''.join(a)) if a else 0
        num2 = int(''.join(b)) if b else 0
        return num1 + num2
```

## Python3

```python
class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(str(num))
        a, b = [], []
        for i, d in enumerate(digits):
            if i % 2 == 0:
                a.append(d)
            else:
                b.append(d)
        n1 = int(''.join(a)) if a else 0
        n2 = int(''.join(b)) if b else 0
        return n1 + n2
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int splitNum(int num) {
    int digits[10];
    int n = 0;
    while (num > 0) {
        digits[n++] = num % 10;
        num /= 10;
    }
    qsort(digits, n, sizeof(int), cmp_int);
    
    long long a = 0, b = 0;
    for (int i = 0; i < n; ++i) {
        if ((i & 1) == 0)
            a = a * 10 + digits[i];
        else
            b = b * 10 + digits[i];
    }
    return (int)(a + b);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int SplitNum(int num) {
        List<int> digits = new List<int>();
        while (num > 0) {
            digits.Add(num % 10);
            num /= 10;
        }
        digits.Sort();
        int n1 = 0, n2 = 0;
        bool turn = true;
        foreach (int d in digits) {
            if (turn) {
                n1 = n1 * 10 + d;
            } else {
                n2 = n2 * 10 + d;
            }
            turn = !turn;
        }
        return n1 + n2;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var splitNum = function(num) {
    const digits = String(num).split('').map(Number).sort((a, b) => a - b);
    let s1 = '', s2 = '';
    for (let i = 0; i < digits.length; i++) {
        if (i % 2 === 0) {
            s1 += digits[i];
        } else {
            s2 += digits[i];
        }
    }
    return Number(s1) + Number(s2);
};
```

## Typescript

```typescript
function splitNum(num: number): number {
    const digits = String(num)
        .split('')
        .map(ch => Number(ch))
        .sort((a, b) => a - b);
    
    let s1 = '';
    let s2 = '';
    for (let i = 0; i < digits.length; i++) {
        if (i % 2 === 0) {
            s1 += digits[i];
        } else {
            s2 += digits[i];
        }
    }
    
    const n1 = Number(s1 || '0');
    const n2 = Number(s2 || '0');
    return n1 + n2;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function splitNum($num) {
        // Convert number to array of its digits
        $digits = str_split((string)$num);
        // Sort digits in non-decreasing order
        sort($digits, SORT_NUMERIC);
        
        $a = '';
        $b = '';
        foreach ($digits as $idx => $d) {
            if ($idx % 2 == 0) {
                $a .= $d;
            } else {
                $b .= $d;
            }
        }
        // Convert to integers (leading zeros are ignored)
        $num1 = intval($a);
        $num2 = intval($b);
        return $num1 + $num2;
    }
}
```

## Swift

```swift
class Solution {
    func splitNum(_ num: Int) -> Int {
        var digits = [Int]()
        var n = num
        while n > 0 {
            digits.append(n % 10)
            n /= 10
        }
        digits.sort()
        var num1 = 0
        var num2 = 0
        for (i, d) in digits.enumerated() {
            if i % 2 == 0 {
                num1 = num1 * 10 + d
            } else {
                num2 = num2 * 10 + d
            }
        }
        return num1 + num2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun splitNum(num: Int): Int {
        val digits = num.toString().toCharArray()
        digits.sort()
        val sb1 = StringBuilder()
        val sb2 = StringBuilder()
        for (i in digits.indices) {
            if (i % 2 == 0) sb1.append(digits[i]) else sb2.append(digits[i])
        }
        val n1 = if (sb1.isEmpty()) 0 else sb1.toString().toInt()
        val n2 = if (sb2.isEmpty()) 0 else sb2.toString().toInt()
        return n1 + n2
    }
}
```

## Dart

```dart
class Solution {
  int splitNum(int num) {
    List<int> digits = num.toString().split('').map(int.parse).toList();
    digits.sort();
    StringBuffer sb1 = StringBuffer();
    StringBuffer sb2 = StringBuffer();
    for (int i = 0; i < digits.length; i++) {
      if (i % 2 == 0) {
        sb1.write(digits[i]);
      } else {
        sb2.write(digits[i]);
      }
    }
    int n1 = sb1.isEmpty ? 0 : int.parse(sb1.toString());
    int n2 = sb2.isEmpty ? 0 : int.parse(sb2.toString());
    return n1 + n2;
  }
}
```

## Golang

```go
import (
	"sort"
	"strconv"
	"strings"
)

func splitNum(num int) int {
	if num == 0 {
		return 0
	}
	var digits []int
	for n := num; n > 0; n /= 10 {
		digits = append(digits, n%10)
	}
	sort.Ints(digits)
	var sb1, sb2 strings.Builder
	for i, d := range digits {
		if i%2 == 0 {
			sb1.WriteByte(byte('0' + d))
		} else {
			sb2.WriteByte(byte('0' + d))
		}
	}
	n1, _ := strconv.Atoi(sb1.String())
	n2, _ := strconv.Atoi(sb2.String())
	return n1 + n2
}
```

## Ruby

```ruby
def split_num(num)
  digits = num.to_s.chars.map(&:to_i).sort
  a = ''
  b = ''
  digits.each_with_index do |d, i|
    if i.even?
      a << d.to_s
    else
      b << d.to_s
    end
  end
  a.to_i + b.to_i
end
```

## Scala

```scala
object Solution {
    def splitNum(num: Int): Int = {
        val digits = num.toString.map(_.asDigit).sorted
        var n1 = 0
        var n2 = 0
        for (i <- digits.indices) {
            if (i % 2 == 0) n1 = n1 * 10 + digits(i)
            else n2 = n2 * 10 + digits(i)
        }
        n1 + n2
    }
}
```

## Rust

```rust
impl Solution {
    pub fn split_num(num: i32) -> i32 {
        let mut digits: Vec<char> = num.to_string().chars().collect();
        digits.sort_unstable();
        let mut s1 = String::new();
        let mut s2 = String::new();
        for (i, d) in digits.iter().enumerate() {
            if i % 2 == 0 {
                s1.push(*d);
            } else {
                s2.push(*d);
            }
        }
        let n1: i32 = if s1.is_empty() { 0 } else { s1.parse().unwrap() };
        let n2: i32 = if s2.is_empty() { 0 } else { s2.parse().unwrap() };
        n1 + n2
    }
}
```

## Racket

```racket
(define/contract (split-num num)
  (-> exact-integer? exact-integer?)
  (let* ((digits
          (map (lambda (c)
                 (- (char->integer c) (char->integer #\0)))
               (string->list (number->string num))))
         (sorted (sort digits <)))
    (let loop ((ds sorted) (i 0) (s1 "") (s2 ""))
      (if (null? ds)
          (+ (string->number s1) (string->number s2))
          (let ((d (car ds))
                (rest (cdr ds)))
            (if (even? i)
                (loop rest (add1 i) (string-append s1 (number->string d)) s2)
                (loop rest (add1 i) s1 (string-append s2 (number->string d)))))))))
```

## Erlang

```erlang
-module(solution).
-export([split_num/1]).

-spec split_num(Num :: integer()) -> integer().
split_num(Num) ->
    Digits = [C - $0 || C <- integer_to_list(Num)],
    Sorted = lists:sort(Digits),
    {N1Rev, N2Rev} = assign(Sorted, [], [], true),
    Num1 = case N1Rev of
               [] -> 0;
               _ -> list_to_integer(lists:reverse(N1Rev))
           end,
    Num2 = case N2Rev of
               [] -> 0;
               _ -> list_to_integer(lists:reverse(N2Rev))
           end,
    Num1 + Num2.

assign([], N1, N2, _) ->
    {N1, N2};
assign([D|Rest], N1, N2, true) ->
    assign(Rest, [($0 + D)|N1], N2, false);
assign([D|Rest], N1, N2, false) ->
    assign(Rest, N1, [($0 + D)|N2], true).
```

## Elixir

```elixir
defmodule Solution do
  @spec split_num(num :: integer) :: integer
  def split_num(num) do
    digits = Integer.digits(num) |> Enum.sort()

    {num1_digits, num2_digits} =
      Enum.with_index(digits)
      |> Enum.reduce({[], []}, fn {d, idx}, {a, b} ->
        if rem(idx, 2) == 0 do
          {[d | a], b}
        else
          {a, [d | b]}
        end
      end)

    num1 = Enum.reverse(num1_digits) |> Enum.reduce(0, fn d, acc -> acc * 10 + d end)
    num2 = Enum.reverse(num2_digits) |> Enum.reduce(0, fn d, acc -> acc * 10 + d end)

    num1 + num2
  end
end
```
