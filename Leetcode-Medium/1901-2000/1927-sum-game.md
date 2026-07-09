# 1927. Sum Game

## Cpp

```cpp
class Solution {
public:
    bool sumGame(string num) {
        int n = num.size();
        int half = n / 2;
        long long leftSum = 0, rightSum = 0;
        long long ql = 0, qr = 0;
        for (int i = 0; i < half; ++i) {
            if (num[i] == '?') ++ql;
            else leftSum += num[i] - '0';
        }
        for (int i = half; i < n; ++i) {
            if (num[i] == '?') ++qr;
            else rightSum += num[i] - '0';
        }
        long long diff = leftSum - rightSum;          // left - right
        long long d = qr - ql;                        // extra '?' on right minus left
        return diff * 2 != d * 9;                     // Alice wins if not equal
    }
};
```

## Java

```java
class Solution {
    public boolean sumGame(String num) {
        int n = num.length();
        int half = n / 2;
        long sumLeft = 0, sumRight = 0;
        int leftQ = 0, rightQ = 0;
        for (int i = 0; i < n; i++) {
            char c = num.charAt(i);
            if (i < half) {
                if (c == '?') {
                    leftQ++;
                } else {
                    sumLeft += c - '0';
                }
            } else {
                if (c == '?') {
                    rightQ++;
                } else {
                    sumRight += c - '0';
                }
            }
        }
        long diff = sumLeft - sumRight; // left sum minus right sum
        if (leftQ == rightQ) {
            return diff != 0;
        }
        int qDiff = leftQ - rightQ;               // positive if more '?' on left
        long needed = (long) qDiff * 9;           // total influence possible
        if (needed % 2 != 0) {                    // cannot balance exactly
            return true;                          // Alice wins
        }
        long target = -needed / 2;                // required diff for Bob to win
        return diff != target;                    // Alice wins unless exact match
    }
}
```

## Python

```python
class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        half = n // 2
        left_sum = right_sum = 0
        left_q = right_q = 0

        for i, ch in enumerate(num):
            if ch == '?':
                if i < half:
                    left_q += 1
                else:
                    right_q += 1
            else:
                d = ord(ch) - 48
                if i < half:
                    left_sum += d
                else:
                    right_sum += d

        diff = left_sum - right_sum

        if left_q == right_q:
            return diff != 0
        elif left_q > right_q:
            # extra '?' on the left side gives Alice an automatic win when odd count
            if (left_q - right_q) % 2 == 1:
                return True
            diff += ((left_q - right_q) // 2) * 9
            return diff != 0
        else:  # right_q > left_q
            diff -= ((right_q - left_q) // 2) * 9
            return diff != 0
```

## Python3

```python
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        left = num[:half]
        right = num[half:]

        left_sum = sum(int(c) for c in left if c != '?')
        right_sum = sum(int(c) for c in right if c != '?')

        left_q = left.count('?')
        right_q = right.count('?')

        total_q = left_q + right_q
        if total_q % 2 == 1:
            return True

        diff = left_sum - right_sum
        # Bob can force equality iff diff*2 == (right_q - left_q) * 9
        return diff * 2 != (right_q - left_q) * 9
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool sumGame(char* num) {
    int n = strlen(num);
    int half = n / 2;
    int leftSum = 0, rightSum = 0;
    int leftQ = 0, rightQ = 0;

    for (int i = 0; i < half; ++i) {
        if (num[i] == '?')
            ++leftQ;
        else
            leftSum += num[i] - '0';
    }
    for (int i = half; i < n; ++i) {
        if (num[i] == '?')
            ++rightQ;
        else
            rightSum += num[i] - '0';
    }

    int totalQ = leftQ + rightQ;
    if (totalQ % 2 == 1)
        return true;

    int diff = leftSum - rightSum;
    int need = (rightQ - leftQ) * 9 / 2;
    return diff != need;
}
```

## Csharp

```csharp
public class Solution {
    public bool SumGame(string num) {
        int n = num.Length;
        int half = n / 2;
        long leftSum = 0, rightSum = 0;
        int leftQ = 0, rightQ = 0;

        for (int i = 0; i < half; i++) {
            char c = num[i];
            if (c == '?') leftQ++;
            else leftSum += c - '0';
        }
        for (int i = half; i < n; i++) {
            char c = num[i];
            if (c == '?') rightQ++;
            else rightSum += c - '0';
        }

        if (leftQ == rightQ) return leftSum != rightSum;

        int diff = (int)(leftSum - rightSum);
        int qDiff = leftQ - rightQ;

        if ((qDiff & 1) != 0) return true; // odd difference gives Alice advantage

        int target = -(qDiff / 2) * 9;
        return diff != target;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @return {boolean}
 */
var sumGame = function(num) {
    const n = num.length;
    const half = n >> 1;
    let leftSum = 0, rightSum = 0;
    let leftQ = 0, rightQ = 0;
    
    for (let i = 0; i < half; ++i) {
        const ch = num[i];
        if (ch === '?') leftQ++;
        else leftSum += ch.charCodeAt(0) - 48; // digit to int
    }
    for (let i = half; i < n; ++i) {
        const ch = num[i];
        if (ch === '?') rightQ++;
        else rightSum += ch.charCodeAt(0) - 48;
    }
    
    if (leftQ === rightQ) {
        return leftSum !== rightSum;
    }
    // Compare diff*2 with 9*(leftQ-rightQ)
    const diff = leftSum - rightSum;
    return diff * 2 !== 9 * (leftQ - rightQ);
};
```

## Typescript

```typescript
function sumGame(num: string): boolean {
    const n = num.length;
    let leftSum = 0, rightSum = 0;
    let leftQ = 0, rightQ = 0;

    for (let i = 0; i < n / 2; i++) {
        const ch = num[i];
        if (ch === '?') {
            leftQ++;
        } else {
            leftSum += ch.charCodeAt(0) - 48;
        }
    }

    for (let i = n / 2; i < n; i++) {
        const ch = num[i];
        if (ch === '?') {
            rightQ++;
        } else {
            rightSum += ch.charCodeAt(0) - 48;
        }
    }

    if (leftQ === rightQ) {
        return leftSum !== rightSum;
    }

    const diff = leftSum - rightSum;          // left sum minus right sum
    const qDiff = leftQ - rightQ;              // number of extra '?' on left side

    // Bob can force equality only when diff * 2 == -qDiff * 9
    return diff * 2 !== -qDiff * 9;
}
```

## Php

```php
class Solution {

    /**
     * @param String $num
     * @return Boolean
     */
    function sumGame($num) {
        $n = strlen($num);
        $half = intdiv($n, 2);
        $leftSum = 0;
        $rightSum = 0;
        $leftQ = 0;
        $rightQ = 0;

        for ($i = 0; $i < $half; ++$i) {
            $c = $num[$i];
            if ($c === '?') {
                $leftQ++;
            } else {
                $leftSum += intval($c);
            }
        }

        for ($i = $half; $i < $n; ++$i) {
            $c = $num[$i];
            if ($c === '?') {
                $rightQ++;
            } else {
                $rightSum += intval($c);
            }
        }

        $diff = $leftSum - $rightSum;               // left sum minus right sum
        $delta = $rightQ - $leftQ;                  // extra '?' on the right side

        return (2 * $diff) != ($delta * 9);
    }
}
```

## Swift

```swift
class Solution {
    func sumGame(_ num: String) -> Bool {
        let chars = Array(num)
        let n = chars.count
        let half = n / 2
        var leftSum = 0
        var rightSum = 0
        var leftQ = 0
        var rightQ = 0
        
        for i in 0..<n {
            let c = chars[i]
            if c == "?" {
                if i < half {
                    leftQ += 1
                } else {
                    rightQ += 1
                }
            } else {
                let digit = Int(String(c))!
                if i < half {
                    leftSum += digit
                } else {
                    rightSum += digit
                }
            }
        }
        
        let diff = leftSum - rightSum
        if leftQ == rightQ {
            return diff != 0
        } else {
            let needed = (rightQ - leftQ) * 9
            return diff * 2 != needed
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumGame(num: String): Boolean {
        val n = num.length
        val half = n / 2
        var sumLeft = 0
        var sumRight = 0
        var qLeft = 0
        var qRight = 0

        for (i in 0 until half) {
            val c = num[i]
            if (c == '?') {
                qLeft++
            } else {
                sumLeft += c - '0'
            }
        }
        for (i in half until n) {
            val c = num[i]
            if (c == '?') {
                qRight++
            } else {
                sumRight += c - '0'
            }
        }

        // Different parity of question marks guarantees Alice's win
        if ((qLeft % 2) != (qRight % 2)) return true

        val diff = sumLeft - sumRight
        val needed = (qRight - qLeft) * 9 / 2
        return diff != needed
    }
}
```

## Dart

```dart
class Solution {
  bool sumGame(String num) {
    int n = num.length;
    int half = n ~/ 2;
    int leftSum = 0, rightSum = 0;
    int leftQ = 0, rightQ = 0;

    for (int i = 0; i < half; i++) {
      String c = num[i];
      if (c == '?') {
        leftQ++;
      } else {
        leftSum += c.codeUnitAt(0) - 48;
      }
    }

    for (int i = half; i < n; i++) {
      String c = num[i];
      if (c == '?') {
        rightQ++;
      } else {
        rightSum += c.codeUnitAt(0) - 48;
      }
    }

    int diff = leftSum - rightSum;

    if (leftQ == rightQ) {
      return diff != 0;
    }

    // Bob can win only when diff * 2 == 9 * (rightQ - leftQ)
    return diff * 2 != 9 * (rightQ - leftQ);
  }
}
```

## Golang

```go
func sumGame(num string) bool {
    n := len(num)
    half := n / 2
    var sumL, sumR int
    var cntL, cntR int

    for i := 0; i < half; i++ {
        c := num[i]
        if c == '?' {
            cntL++
        } else {
            sumL += int(c - '0')
        }
    }
    for i := half; i < n; i++ {
        c := num[i]
        if c == '?' {
            cntR++
        } else {
            sumR += int(c - '0')
        }
    }

    diff := sumL - sumR
    if cntL == cntR {
        return diff != 0
    }
    k := cntL - cntR
    if k < 0 {
        k = -k
    }
    return diff*2 != 9*k
}
```

## Ruby

```ruby
def sum_game(num)
  n = num.length / 2
  left_sum = 0
  right_sum = 0
  left_q = 0
  right_q = 0

  (0...n).each do |i|
    ch = num[i]
    if ch == '?'
      left_q += 1
    else
      left_sum += ch.ord - 48
    end
  end

  (n...num.length).each do |i|
    ch = num[i]
    if ch == '?'
      right_q += 1
    else
      right_sum += ch.ord - 48
    end
  end

  diff = left_sum - right_sum
  d = left_q - right_q

  return diff != 0 if d == 0
  return true if d.abs.odd?

  target = -(d / 2) * 9
  diff != target
end
```

## Scala

```scala
object Solution {
    def sumGame(num: String): Boolean = {
        val n = num.length
        val half = n / 2
        var sumL = 0
        var sumR = 0
        var cntL = 0
        var cntR = 0

        for (i <- 0 until half) {
            val c = num.charAt(i)
            if (c == '?') cntL += 1 else sumL += c - '0'
        }
        for (i <- half until n) {
            val c = num.charAt(i)
            if (c == '?') cntR += 1 else sumR += c - '0'
        }

        val diff = sumL - sumR
        val deltaQ = cntR - cntL

        if ((deltaQ & 1) != 0) true
        else {
            val target = deltaQ * 9 / 2
            diff != target
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_game(num: String) -> bool {
        let bytes = num.as_bytes();
        let n = bytes.len();
        let half = n / 2;
        let mut sum_left: i32 = 0;
        let mut sum_right: i32 = 0;
        let mut q_left: i32 = 0;
        let mut q_right: i32 = 0;

        for i in 0..half {
            match bytes[i] {
                b'?' => q_left += 1,
                d => sum_left += (d - b'0') as i32,
            }
        }
        for i in half..n {
            match bytes[i] {
                b'?' => q_right += 1,
                d => sum_right += (d - b'0') as i32,
            }
        }

        let diff = sum_left - sum_right;
        let cnt = q_left - q_right;

        if cnt == 0 {
            return diff != 0;
        }

        let diff_abs = diff.abs();
        let cnt_abs = cnt.abs();

        diff_abs != (cnt_abs * 9) / 2
    }
}
```

## Racket

```racket
(define/contract (sum-game num)
  (-> string? boolean?)
  (let* ((len (string-length num))
         (half (/ len 2)))
    (let-values ([(left-sum right-sum left-q right-q)
                  (for/fold ([ls 0] [rs 0] [lq 0] [rq 0]) ((i (in-range half)))
                    (let* ((cl (string-ref num i))
                           (cr (string-ref num (+ i half))))
                      (values
                        (+ ls (if (char=? cl #\?) 0 (- (char->integer cl) (char->integer #\0))))
                        (+ rs (if (char=? cr #\?) 0 (- (char->integer cr) (char->integer #\0))))
                        (+ lq (if (char=? cl #\?) 1 0))
                        (+ rq (if (char=? cr #\?) 1 0))))))])
      (if (= left-q right-q)
          (not (= left-sum right-sum))
          (let* ((diff (- left-sum right-sum))
                 (qdiff (- left-q right-q)))
            (if (odd? (abs qdiff))
                #t
                (let ((target (* -9 (/ qdiff 2))))
                  (not (= diff target)))))))))
```

## Erlang

```erlang
-module(solution).
-export([sum_game/1]).

-spec sum_game(Num :: unicode:unicode_binary()) -> boolean().
sum_game(Num) ->
    Len = byte_size(Num),
    Half = Len div 2,
    <<LeftBin:Half/binary, RightBin/binary>> = Num,
    {SumL, QL} = process_bin(LeftBin, 0, 0),
    {SumR, QR} = process_bin(RightBin, 0, 0),
    Diff = SumL - SumR,
    case QL == QR of
        true ->
            Diff =/= 0;
        false ->
            if QL > QR ->
                    Extra = QL - QR,
                    case Extra rem 2 of
                        1 -> true;
                        0 ->
                            Adjust = (Extra div 2) * 9,
                            Diff + Adjust =/= 0
                    end;
               QR > QL ->
                    Extra = QR - QL,
                    case Extra rem 2 of
                        1 -> true;
                        0 ->
                            Adjust = (Extra div 2) * 9,
                            Diff - Adjust =/= 0
                    end
            end
    end.

process_bin(<<>>, Sum, Q) -> {Sum, Q};
process_bin(<<C, Rest/binary>>, Sum, Q) when C =:= $? ->
    process_bin(Rest, Sum, Q + 1);
process_bin(<<C, Rest/binary>>, Sum, Q) ->
    Digit = C - $0,
    process_bin(Rest, Sum + Digit, Q).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_game(num :: String.t) :: boolean
  def sum_game(num) do
    len = String.length(num)
    half = div(len, 2)

    {lsum, lq, rsum, rq} =
      num
      |> String.to_charlist()
      |> Enum.with_index()
      |> Enum.reduce({0, 0, 0, 0}, fn {c, i},
            {lsum, lq, rsum, rq} ->
        cond do
          c == ?? ->
            if i < half do
              {lsum, lq + 1, rsum, rq}
            else
              {lsum, lq, rsum, rq + 1}
            end

          c >= ?0 and c <= ?9 ->
            digit = c - ?0
            if i < half do
              {lsum + digit, lq, rsum, rq}
            else
              {lsum, lq, rsum + digit, rq}
            end

          true ->
            {lsum, lq, rsum, rq}
        end
      end)

    diff = lsum - rsum

    if lq == rq do
      diff != 0
    else
      diff * 2 != 9 * (rq - lq)
    end
  end
end
```
