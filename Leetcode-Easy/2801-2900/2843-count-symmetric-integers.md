# 2843. Count Symmetric Integers

## Cpp

```cpp
class Solution {
public:
    bool isSymmetric(int x) {
        std::string s = std::to_string(x);
        int len = s.size();
        if (len % 2 != 0) return false;
        int half = len / 2;
        int sum1 = 0, sum2 = 0;
        for (int i = 0; i < half; ++i) sum1 += s[i] - '0';
        for (int i = half; i < len; ++i) sum2 += s[i] - '0';
        return sum1 == sum2;
    }
    
    int countSymmetricIntegers(int low, int high) {
        int cnt = 0;
        for (int x = low; x <= high; ++x) {
            if (isSymmetric(x)) ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int countSymmetricIntegers(int low, int high) {
        int cnt = 0;
        for (int i = low; i <= high; i++) {
            String s = Integer.toString(i);
            int len = s.length();
            if ((len & 1) == 1) continue; // odd length cannot be symmetric
            int half = len / 2;
            int sumFirst = 0, sumSecond = 0;
            for (int j = 0; j < half; j++) {
                sumFirst += s.charAt(j) - '0';
                sumSecond += s.charAt(j + half) - '0';
            }
            if (sumFirst == sumSecond) cnt++;
        }
        return cnt;
    }
}
```

## Python

```python
class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        cnt = 0
        for x in range(low, high + 1):
            s = str(x)
            if len(s) % 2 != 0:
                continue
            mid = len(s) // 2
            if sum(map(int, s[:mid])) == sum(map(int, s[mid:])):
                cnt += 1
        return cnt
```

## Python3

```python
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for x in range(low, high + 1):
            s = str(x)
            if len(s) % 2 != 0:
                continue
            m = len(s) // 2
            if sum(map(int, s[:m])) == sum(map(int, s[m:])):
                cnt += 1
        return cnt
```

## C

```c
int countSymmetricIntegers(int low, int high) {
    int cnt = 0;
    for (int x = low; x <= high; ++x) {
        if (x < 10) continue;               // 1 digit, not symmetric
        else if (x < 100) {                  // 2 digits
            int d1 = x / 10;
            int d2 = x % 10;
            if (d1 == d2) ++cnt;
        } else if (x < 1000) {
            continue;                        // 3 digits, never symmetric
        } else if (x < 10000) {               // 4 digits
            int a = x / 1000;
            int b = (x / 100) % 10;
            int c = (x / 10) % 10;
            int d = x % 10;
            if (a + b == c + d) ++cnt;
        } else {
            // x == 10000 (5 digits), never symmetric
        }
    }
    return cnt;
}
```

## Csharp

```csharp
public class Solution {
    public int CountSymmetricIntegers(int low, int high) {
        int count = 0;
        for (int i = low; i <= high; i++) {
            string s = i.ToString();
            if ((s.Length & 1) == 0) { // even number of digits
                int half = s.Length / 2;
                int sumFirst = 0, sumSecond = 0;
                for (int j = 0; j < half; j++) {
                    sumFirst += s[j] - '0';
                }
                for (int j = half; j < s.Length; j++) {
                    sumSecond += s[j] - '0';
                }
                if (sumFirst == sumSecond) {
                    count++;
                }
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countSymmetricIntegers = function(low, high) {
    let ans = 0;
    for (let x = low; x <= high; ++x) {
        const s = String(x);
        if ((s.length & 1) !== 0) continue; // odd length can't be symmetric
        const half = s.length >> 1;
        let sum1 = 0, sum2 = 0;
        for (let i = 0; i < half; ++i) sum1 += s.charCodeAt(i) - 48;
        for (let i = half; i < s.length; ++i) sum2 += s.charCodeAt(i) - 48;
        if (sum1 === sum2) ++ans;
    }
    return ans;
};
```

## Typescript

```typescript
function countSymmetricIntegers(low: number, high: number): number {
    let count = 0;
    for (let x = low; x <= high; x++) {
        const s = String(x);
        if (s.length % 2 !== 0) continue;
        const half = s.length >> 1;
        let sumFirst = 0, sumSecond = 0;
        for (let i = 0; i < half; i++) sumFirst += s.charCodeAt(i) - 48;
        for (let i = half; i < s.length; i++) sumSecond += s.charCodeAt(i) - 48;
        if (sumFirst === sumSecond) count++;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $low
     * @param Integer $high
     * @return Integer
     */
    function countSymmetricIntegers($low, $high) {
        $count = 0;
        for ($i = $low; $i <= $high; $i++) {
            $s = (string)$i;
            $len = strlen($s);
            if ($len % 2 !== 0) {
                continue;
            }
            $half = $len / 2;
            $sum1 = 0;
            $sum2 = 0;
            for ($j = 0; $j < $half; $j++) {
                $sum1 += intval($s[$j]);
            }
            for ($j = $half; $j < $len; $j++) {
                $sum2 += intval($s[$j]);
            }
            if ($sum1 === $sum2) {
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countSymmetricIntegers(_ low: Int, _ high: Int) -> Int {
        var result = 0
        for num in low...high {
            let s = String(num)
            let len = s.count
            if len % 2 != 0 { continue }
            let half = len / 2
            var sumFirst = 0
            var sumSecond = 0
            var index = 0
            for ch in s {
                let digit = Int(String(ch))!
                if index < half {
                    sumFirst += digit
                } else {
                    sumSecond += digit
                }
                index += 1
            }
            if sumFirst == sumSecond {
                result += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSymmetricIntegers(low: Int, high: Int): Int {
        var count = 0
        for (num in low..high) {
            val s = num.toString()
            if (s.length % 2 != 0) continue
            val half = s.length / 2
            var sumFirst = 0
            var sumSecond = 0
            for (i in 0 until half) {
                sumFirst += s[i] - '0'
                sumSecond += s[i + half] - '0'
            }
            if (sumFirst == sumSecond) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countSymmetricIntegers(int low, int high) {
    int cnt = 0;
    for (int num = low; num <= high; ++num) {
      String s = num.toString();
      if (s.length.isOdd) continue;
      int half = s.length ~/ 2;
      int sumFirst = 0, sumSecond = 0;
      for (int i = 0; i < half; ++i) {
        sumFirst += s.codeUnitAt(i) - 48;
        sumSecond += s.codeUnitAt(i + half) - 48;
      }
      if (sumFirst == sumSecond) cnt++;
    }
    return cnt;
  }
}
```

## Golang

```go
package main

import "strconv"

func countSymmetricIntegers(low int, high int) int {
	cnt := 0
	for i := low; i <= high; i++ {
		s := strconv.Itoa(i)
		if len(s)%2 != 0 {
			continue
		}
		half := len(s) / 2
		sum1, sum2 := 0, 0
		for j := 0; j < half; j++ {
			sum1 += int(s[j] - '0')
			sum2 += int(s[half+j] - '0')
		}
		if sum1 == sum2 {
			cnt++
		}
	}
	return cnt
}
```

## Ruby

```ruby
# @param {Integer} low
# @param {Integer} high
# @return {Integer}
def count_symmetric_integers(low, high)
  count = 0
  (low..high).each do |num|
    s = num.to_s
    next if s.length.odd?
    mid = s.length / 2
    sum1 = 0
    sum2 = 0
    i = 0
    while i < mid
      sum1 += s[i].ord - 48
      sum2 += s[mid + i].ord - 48
      i += 1
    end
    count += 1 if sum1 == sum2
  end
  count
end
```

## Scala

```scala
object Solution {
    def countSymmetricIntegers(low: Int, high: Int): Int = {
        var cnt = 0
        for (num <- low to high) {
            val s = num.toString
            if ((s.length & 1) == 0) {
                val half = s.length / 2
                var sumFirst = 0
                var sumSecond = 0
                var i = 0
                while (i < half) {
                    sumFirst += s.charAt(i) - '0'
                    sumSecond += s.charAt(i + half) - '0'
                    i += 1
                }
                if (sumFirst == sumSecond) cnt += 1
            }
        }
        cnt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_symmetric_integers(low: i32, high: i32) -> i32 {
        let mut cnt = 0;
        for x in low..=high {
            let s = x.to_string();
            if s.len() % 2 != 0 {
                continue;
            }
            let half = s.len() / 2;
            let bytes = s.as_bytes();
            let mut sum1 = 0i32;
            let mut sum2 = 0i32;
            for i in 0..half {
                sum1 += (bytes[i] - b'0') as i32;
                sum2 += (bytes[half + i] - b'0') as i32;
            }
            if sum1 == sum2 {
                cnt += 1;
            }
        }
        cnt
    }
}
```

## Racket

```racket
(define/contract (count-symmetric-integers low high)
  (-> exact-integer? exact-integer? exact-integer?)
  (letrec
      ((sum-digits
        (lambda (str)
          (for/sum ([c (in-string str)])
            (- (char->integer c) (char->integer #\0)))))
       (loop
        (lambda (i cnt)
          (if (> i high)
              cnt
              (let* ((s (number->string i))
                     (len (string-length s)))
                (if (odd? len)
                    (loop (+ i 1) cnt)
                    (let* ((half (quotient len 2))
                           (first (substring s 0 half))
                           (second (substring s half len)))
                      (if (= (sum-digits first) (sum-digits second))
                          (loop (+ i 1) (+ cnt 1))
                          (loop (+ i 1) cnt)))))))))
    (loop low 0)))
```

## Erlang

```erlang
-module(solution).
-export([count_symmetric_integers/2]).

-spec count_symmetric_integers(Low :: integer(), High :: integer()) -> integer().
count_symmetric_integers(Low, High) ->
    count_symmetric_integers(Low, High, 0).

count_symmetric_integers(Current, High, Acc) when Current > High ->
    Acc;
count_symmetric_integers(Current, High, Acc) ->
    NewAcc = case is_symmetric(Current) of
                true -> Acc + 1;
                false -> Acc
            end,
    count_symmetric_integers(Current + 1, High, NewAcc).

is_symmetric(N) ->
    Str = integer_to_list(N),
    Len = length(Str),
    case Len rem 2 of
        1 -> false;
        0 ->
            Half = Len div 2,
            {First, Second} = lists:split(Half, Str),
            sum_digits(First) == sum_digits(Second)
    end.

sum_digits(List) ->
    lists:foldl(fun(C, Acc) -> (C - $0) + Acc end, 0, List).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_symmetric_integers(low :: integer, high :: integer) :: integer
  def count_symmetric_integers(low, high) do
    low..high
    |> Enum.reduce(0, fn num, acc ->
      if symmetric?(num), do: acc + 1, else: acc
    end)
  end

  defp symmetric?(num) do
    digits = Integer.digits(num)
    len = length(digits)

    if rem(len, 2) != 0 do
      false
    else
      n = div(len, 2)
      {first, second} = Enum.split(digits, n)
      Enum.sum(first) == Enum.sum(second)
    end
  end
end
```
