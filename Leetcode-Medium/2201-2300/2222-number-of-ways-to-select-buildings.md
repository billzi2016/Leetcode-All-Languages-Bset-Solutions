# 2222. Number of Ways to Select Buildings

## Cpp

```cpp
class Solution {
public:
    long long numberOfWays(string s) {
        int n = s.size();
        vector<long long> pref0(n), pref1(n);
        pref0[0] = (s[0] == '0');
        pref1[0] = (s[0] == '1');
        for (int i = 1; i < n; ++i) {
            pref0[i] = pref0[i - 1] + (s[i] == '0');
            pref1[i] = pref1[i - 1] + (s[i] == '1');
        }
        long long total0 = pref0.back();
        long long total1 = pref1.back();
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            if (s[i] == '1') {
                long long zeros_before = (i > 0 ? pref0[i - 1] : 0);
                long long zeros_after = total0 - pref0[i];
                ans += zeros_before * zeros_after;
            } else { // s[i] == '0'
                long long ones_before = (i > 0 ? pref1[i - 1] : 0);
                long long ones_after = total1 - pref1[i];
                ans += ones_before * ones_after;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long numberOfWays(String s) {
        int n = s.length();
        long[] suffixZero = new long[n];
        long[] suffixOne = new long[n];
        long cnt0 = 0, cnt1 = 0;
        for (int i = n - 1; i >= 0; --i) {
            char c = s.charAt(i);
            if (c == '0') {
                cnt0++;
            } else {
                cnt1++;
            }
            suffixZero[i] = cnt0;
            suffixOne[i] = cnt1;
        }

        long leftZero = 0, leftOne = 0, ans = 0;
        for (int i = 0; i < n; ++i) {
            char c = s.charAt(i);
            if (c == '1') { // middle of "010"
                long rightZeros = suffixZero[i];
                ans += leftZero * rightZeros;
            } else { // c == '0', middle of "101"
                long rightOnes = suffixOne[i];
                ans += leftOne * rightOnes;
            }
            if (c == '0') {
                leftZero++;
            } else {
                leftOne++;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        prefix0 = [0] * (n + 1)
        prefix1 = [0] * (n + 1)
        for i, ch in enumerate(s):
            prefix0[i + 1] = prefix0[i] + (ch == '0')
            prefix1[i + 1] = prefix1[i] + (ch == '1')
        total0 = prefix0[-1]
        total1 = prefix1[-1]
        ans = 0
        for i, ch in enumerate(s):
            if ch == '1':
                left0 = prefix0[i]
                right0 = total0 - prefix0[i + 1]
                ans += left0 * right0
            else:  # ch == '0'
                left1 = prefix1[i]
                right1 = total1 - prefix1[i + 1]
                ans += left1 * right1
        return ans
```

## Python3

```python
class Solution:
    def numberOfWays(self, s: str) -> int:
        total_zero = s.count('0')
        total_one = len(s) - total_zero

        left_zero = 0
        left_one = 0
        ans = 0

        for ch in s:
            if ch == '0':
                # middle is 0, need ones on both sides -> pattern 101
                right_one = total_one - left_one
                ans += left_one * right_one
                left_zero += 1
            else:  # ch == '1'
                # middle is 1, need zeros on both sides -> pattern 010
                right_zero = total_zero - left_zero
                ans += left_zero * right_zero
                left_one += 1

        return ans
```

## C

```c
#include <string.h>

long long numberOfWays(char* s) {
    int n = (int)strlen(s);
    long long totalZeros = 0, totalOnes = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == '0') totalZeros++;
        else totalOnes++;
    }
    
    long long prefixZero = 0, prefixOne = 0;
    long long ans = 0;
    
    for (int i = 0; i < n; ++i) {
        if (s[i] == '0') {
            // pattern "101" with this zero as middle
            long long afterOnes = totalOnes - prefixOne;
            ans += prefixOne * afterOnes;
            ++prefixZero;
        } else { // s[i] == '1'
            // pattern "010" with this one as middle
            long long afterZeros = totalZeros - prefixZero;
            ans += prefixZero * afterZeros;
            ++prefixOne;
        }
    }
    
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long NumberOfWays(string s) {
        int n = s.Length;
        long[] prefZero = new long[n];
        long[] prefOne = new long[n];
        long zero = 0, one = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '0') zero++;
            else one++;
            prefZero[i] = zero;
            prefOne[i] = one;
        }
        long totalZero = zero, totalOne = one;
        long ans = 0;
        for (int j = 0; j < n; j++) {
            if (s[j] == '1') {
                long leftZero = j > 0 ? prefZero[j - 1] : 0;
                long rightZero = totalZero - prefZero[j];
                ans += leftZero * rightZero;
            } else { // s[j] == '0'
                long leftOne = j > 0 ? prefOne[j - 1] : 0;
                long rightOne = totalOne - prefOne[j];
                ans += leftOne * rightOne;
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numberOfWays = function(s) {
    const n = s.length;
    let totalZero = 0, totalOne = 0;
    for (let i = 0; i < n; ++i) {
        if (s[i] === '0') totalZero++;
        else totalOne++;
    }
    
    let leftZero = 0, leftOne = 0;
    let ans = 0;
    
    for (let i = 0; i < n; ++i) {
        const ch = s[i];
        if (ch === '0') {
            // middle is 0 -> pattern "101"
            const rightOnes = totalOne - leftOne;
            ans += leftOne * rightOnes;
            leftZero++;
        } else { // ch === '1'
            // middle is 1 -> pattern "010"
            const rightZeros = totalZero - leftZero;
            ans += leftZero * rightZeros;
            leftOne++;
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function numberOfWays(s: string): number {
    const n = s.length;
    let totalZero = 0, totalOne = 0;
    for (let ch of s) {
        if (ch === '0') totalZero++;
        else totalOne++;
    }
    let leftZero = 0, leftOne = 0;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const ch = s[i];
        if (ch === '1') {
            // pattern 010 with middle at i
            const zerosAfter = totalZero - leftZero;
            ans += leftZero * zerosAfter;
        } else { // '0'
            // pattern 101 with middle at i
            const onesAfter = totalOne - leftOne;
            ans += leftOne * onesAfter;
        }
        if (ch === '0') leftZero++;
        else leftOne++;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numberOfWays($s) {
        $len = strlen($s);
        $totalZero = substr_count($s, '0');
        $totalOne = $len - $totalZero;

        $prefixZero = 0;
        $prefixOne = 0;
        $ans = 0;

        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if ($c === '1') {
                // zeros on the left * zeros on the right form "010"
                $rightZero = $totalZero - $prefixZero;
                $ans += $prefixZero * $rightZero;
                $prefixOne++;
            } else { // '0'
                // ones on the left * ones on the right form "101"
                $rightOne = $totalOne - $prefixOne;
                $ans += $prefixOne * $rightOne;
                $prefixZero++;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfWays(_ s: String) -> Int {
        var zeros = 0
        var ones = 0
        var count01 = 0   // subsequences "01"
        var count10 = 0   // subsequences "10"
        var result = 0
        
        for ch in s {
            if ch == "0" {
                result += count01          // complete "010"
                count10 += ones           // new "10" ending at this '0'
                zeros += 1
            } else { // ch == "1"
                result += count10          // complete "101"
                count01 += zeros           // new "01" ending at this '1'
                ones += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfWays(s: String): Long {
        var totalZero = 0L
        var totalOne = 0L
        for (ch in s) {
            if (ch == '0') totalZero++ else totalOne++
        }
        var leftZero = 0L
        var leftOne = 0L
        var ans = 0L
        for (ch in s) {
            if (ch == '1') {
                val rightZero = totalZero - leftZero
                ans += leftZero * rightZero
                leftOne++
            } else { // ch == '0'
                val rightOne = totalOne - leftOne
                ans += leftOne * rightOne
                leftZero++
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int numberOfWays(String s) {
    int n = s.length;
    int total0 = 0, total1 = 0;
    for (int i = 0; i < n; i++) {
      if (s.codeUnitAt(i) == 48) { // '0'
        total0++;
      } else {
        total1++;
      }
    }

    int prefix0 = 0, prefix1 = 0;
    int ans = 0;

    for (int i = 0; i < n; i++) {
      int ch = s.codeUnitAt(i);
      if (ch == 48) { // middle '0' -> pattern 101
        int leftOnes = prefix1;
        int rightOnes = total1 - prefix1;
        ans += leftOnes * rightOnes;
        prefix0++;
      } else { // middle '1' -> pattern 010
        int leftZeros = prefix0;
        int rightZeros = total0 - prefix0;
        ans += leftZeros * rightZeros;
        prefix1++;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func numberOfWays(s string) int64 {
    n := len(s)
    totalZero, totalOne := 0, 0
    for i := 0; i < n; i++ {
        if s[i] == '0' {
            totalZero++
        } else {
            totalOne++
        }
    }

    leftZero, leftOne := 0, 0
    var ans int64 = 0

    for i := 0; i < n; i++ {
        c := s[i]
        if c == '1' {
            rightZero := totalZero - leftZero
            ans += int64(leftZero) * int64(rightZero)
            leftOne++
        } else { // c == '0'
            rightOne := totalOne - leftOne
            ans += int64(leftOne) * int64(rightOne)
            leftZero++
        }
    }

    return ans
}
```

## Ruby

```ruby
def number_of_ways(s)
  n = s.length
  pref0 = Array.new(n, 0)
  pref1 = Array.new(n, 0)
  cnt0 = 0
  cnt1 = 0

  s.each_char.with_index do |ch, i|
    if ch == '0'
      cnt0 += 1
    else
      cnt1 += 1
    end
    pref0[i] = cnt0
    pref1[i] = cnt1
  end

  total0 = cnt0
  total1 = cnt1
  ans = 0

  s.each_char.with_index do |ch, i|
    if ch == '1'
      left0 = i.zero? ? 0 : pref0[i - 1]
      right0 = total0 - pref0[i]
      ans += left0 * right0
    else # ch == '0'
      left1 = i.zero? ? 0 : pref1[i - 1]
      right1 = total1 - pref1[i]
      ans += left1 * right1
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def numberOfWays(s: String): Long = {
        val n = s.length
        val prefZero = new Array[Long](n)
        val prefOne = new Array[Long](n)
        var zeros: Long = 0L
        var ones: Long = 0L
        for (i <- 0 until n) {
            if (s.charAt(i) == '0') zeros += 1 else ones += 1
            prefZero(i) = zeros
            prefOne(i) = ones
        }
        val totalZeros = zeros
        val totalOnes = ones
        var ans: Long = 0L
        for (j <- 0 until n) {
            if (s.charAt(j) == '1') {
                val leftZero = if (j > 0) prefZero(j - 1) else 0L
                val rightZero = totalZeros - prefZero(j)
                ans += leftZero * rightZero
            } else { // s[j] == '0'
                val leftOne = if (j > 0) prefOne(j - 1) else 0L
                val rightOne = totalOnes - prefOne(j)
                ans += leftOne * rightOne
            }
        }
        ans
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn number_of_ways(s: String) -> i64 {
        let bytes = s.as_bytes();
        let mut total_zero: i64 = 0;
        let mut total_one: i64 = 0;
        for &c in bytes {
            if c == b'0' {
                total_zero += 1;
            } else {
                total_one += 1;
            }
        }

        let mut left_zero: i64 = 0;
        let mut left_one: i64 = 0;
        let mut ans: i64 = 0;

        for &c in bytes {
            if c == b'1' {
                // middle is '1', need zeros before and after
                let right_zero = total_zero - left_zero;
                ans += left_zero * right_zero;
                left_one += 1;
            } else {
                // middle is '0', need ones before and after
                let right_one = total_one - left_one;
                ans += left_one * right_one;
                left_zero += 1;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (number-of-ways s)
  (-> string? exact-integer?)
  (let* ([n (string-length s)]
         [total0 (for/sum ([i (in-range n)])
                   (if (char=? (string-ref s i) #\0) 1 0))]
         [total1 (- n total0)])
    (let loop ([i 0] [pref0 0] [pref1 0] [ans 0])
      (if (= i n)
          ans
          (let* ([ch (string-ref s i)]
                 [add (if (char=? ch #\0)
                          (* pref1 (- total1 pref1))
                          (* pref0 (- total0 pref0)))]
                 [new-ans (+ ans add)])
            (loop (add1 i)
                  (if (char=? ch #\0) (add1 pref0) pref0)
                  (if (char=? ch #\1) (add1 pref1) pref1)
                  new-ans))))))
```

## Erlang

```erlang
-spec number_of_ways(S :: unicode:unicode_binary()) -> integer().
number_of_ways(S) ->
    {TotalZ, TotalO} = count_totals(S, 0, 0),
    calc(S, TotalZ, TotalO, 0, 0, 0).

count_totals(<<>>, Z, O) -> {Z, O};
count_totals(<<C, Rest/binary>>, Z, O) ->
    if C =:= $0 ->
            count_totals(Rest, Z + 1, O);
       true ->
            count_totals(Rest, Z, O + 1)
    end.

calc(<<>>, _TotalZ, _TotalO, _LZ, _LO, Acc) -> Acc;
calc(<<C, Rest/binary>>, TotalZ, TotalO, LZ, LO, Acc) ->
    if C =:= $0 ->
            RightOnes = TotalO - LO,
            NewAcc = Acc + LO * RightOnes,
            calc(Rest, TotalZ, TotalO, LZ + 1, LO, NewAcc);
       true -> % character '1'
            RightZeros = TotalZ - LZ,
            NewAcc = Acc + LZ * RightZeros,
            calc(Rest, TotalZ, TotalO, LZ, LO + 1, NewAcc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_ways(s :: String.t()) :: integer()
  def number_of_ways(s) do
    chars = :binary.bin_to_list(s)

    total0 = Enum.count(chars, fn c -> c == ?0 end)
    total1 = length(chars) - total0

    {ans, _pref0, _pref1} =
      Enum.reduce(Enum.with_index(chars), {0, 0, 0}, fn
        {?0, _idx}, {acc, pref0, pref1} ->
          left = pref1
          right = total1 - pref1
          {acc + left * right, pref0 + 1, pref1}

        {?1, _idx}, {acc, pref0, pref1} ->
          left = pref0
          right = total0 - pref0
          {acc + left * right, pref0, pref1 + 1}
      end)

    ans
  end
end
```
