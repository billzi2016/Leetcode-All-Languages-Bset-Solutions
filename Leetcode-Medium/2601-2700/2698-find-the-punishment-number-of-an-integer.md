# 2698. Find the Punishment Number of an Integer

## Cpp

```cpp
class Solution {
public:
    bool dfs(const std::string& s, int target, int pos, int cur) {
        if (pos == (int)s.size()) return cur == target;
        if (cur > target) return false;
        long val = 0;
        for (int i = pos; i < (int)s.size(); ++i) {
            val = val * 10 + (s[i] - '0');
            int nxt = cur + (int)val;
            if (nxt > target) break;
            if (dfs(s, target, i + 1, nxt)) return true;
        }
        return false;
    }

    int punishmentNumber(int n) {
        long long ans = 0;
        for (int i = 1; i <= n; ++i) {
            std::string sq = std::to_string(i * i);
            if (dfs(sq, i, 0, 0)) ans += 1LL * i * i;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int punishmentNumber(int n) {
        int total = 0;
        for (int i = 1; i <= n; i++) {
            long sq = (long) i * i;
            String s = Long.toString(sq);
            if (canPartition(s, 0, 0, i)) {
                total += (int) sq;
            }
        }
        return total;
    }

    private boolean canPartition(String s, int idx, int curSum, int target) {
        if (idx == s.length()) {
            return curSum == target;
        }
        for (int end = idx + 1; end <= s.length(); end++) {
            int val = Integer.parseInt(s.substring(idx, end));
            int newSum = curSum + val;
            if (newSum > target) continue;
            if (canPartition(s, end, newSum, target)) return true;
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        from functools import lru_cache

        def can_partition(s, target):
            @lru_cache(None)
            def dfs(idx, cur):
                if idx == len(s):
                    return cur == target
                for end in range(idx + 1, len(s) + 1):
                    part = int(s[idx:end])
                    new_sum = cur + part
                    if new_sum > target:
                        break
                    if dfs(end, new_sum):
                        return True
                return False
            return dfs(0, 0)

        total = 0
        for i in range(1, n + 1):
            sq = i * i
            if can_partition(str(sq), i):
                total += sq
        return total
```

## Python3

```python
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(s: str, target: int) -> bool:
            length = len(s)
            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos: int, cur_sum: int) -> bool:
                if pos == length:
                    return cur_sum == target
                if cur_sum > target:
                    return False
                val = 0
                for i in range(pos, length):
                    val = val * 10 + (ord(s[i]) - 48)
                    new_sum = cur_sum + val
                    if new_sum > target:
                        break
                    if dfs(i + 1, new_sum):
                        return True
                return False

            return dfs(0, 0)

        total = 0
        for i in range(1, n + 1):
            sq = i * i
            if can_partition(str(sq), i):
                total += sq
        return total
```

## C

```c
#include <stdio.h>
#include <stdbool.h>

static bool dfs(const char *s, int pos, int target) {
    if (s[pos] == '\0')
        return target == 0;
    int val = 0;
    for (int i = pos; s[i] != '\0'; ++i) {
        val = val * 10 + (s[i] - '0');
        if (val > target)
            break;
        if (dfs(s, i + 1, target - val))
            return true;
    }
    return false;
}

int punishmentNumber(int n) {
    long long total = 0;
    char buf[20];
    for (int i = 1; i <= n; ++i) {
        int sq = i * i;
        sprintf(buf, "%d", sq);
        if (dfs(buf, 0, i))
            total += sq;
    }
    return (int)total;
}
```

## Csharp

```csharp
public class Solution
{
    public int PunishmentNumber(int n)
    {
        int total = 0;
        for (int i = 1; i <= n; i++)
        {
            long sq = (long)i * i;
            string s = sq.ToString();
            if (CanPartition(s, i))
                total += (int)sq;
        }
        return total;
    }

    private bool CanPartition(string s, int target)
    {
        int len = s.Length;
        bool Dfs(int idx, int sum)
        {
            if (idx == len) return sum == target;
            if (sum > target) return false;

            for (int end = idx + 1; end <= len; end++)
            {
                int val = int.Parse(s.Substring(idx, end - idx));
                if (sum + val > target) continue;
                if (Dfs(end, sum + val)) return true;
            }
            return false;
        }

        return Dfs(0, 0);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var punishmentNumber = function(n) {
    const canPartition = (s, target) => {
        const len = s.length;
        const dfs = (idx, sum) => {
            if (sum > target) return false;
            if (idx === len) return sum === target;
            for (let end = idx + 1; end <= len; ++end) {
                const part = Number(s.slice(idx, end));
                if (dfs(end, sum + part)) return true;
            }
            return false;
        };
        return dfs(0, 0);
    };

    let total = 0;
    for (let i = 1; i <= n; ++i) {
        const sq = i * i;
        if (canPartition(String(sq), i)) {
            total += sq;
        }
    }
    return total;
};
```

## Typescript

```typescript
function punishmentNumber(n: number): number {
    let total = 0;

    const canPartition = (s: string, target: number): boolean => {
        const len = s.length;
        const dfs = (pos: number, sum: number): boolean => {
            if (sum > target) return false;
            if (pos === len) return sum === target;
            for (let end = pos + 1; end <= len; ++end) {
                const part = Number(s.slice(pos, end));
                if (dfs(end, sum + part)) return true;
            }
            return false;
        };
        return dfs(0, 0);
    };

    for (let i = 1; i <= n; ++i) {
        const sq = i * i;
        if (canPartition(sq.toString(), i)) {
            total += sq;
        }
    }

    return total;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function punishmentNumber($n) {
        $total = 0;
        for ($i = 1; $i <= $n; $i++) {
            $sq = $i * $i;
            $s = strval($sq);
            if ($this->canPartition($s, $i)) {
                $total += $sq;
            }
        }
        return $total;
    }

    private function canPartition(string $s, int $target): bool {
        $len = strlen($s);
        return $this->dfs($s, 0, 0, $target, $len);
    }

    private function dfs(string $s, int $idx, int $sum, int $target, int $len): bool {
        if ($idx == $len) {
            return $sum == $target;
        }
        if ($sum > $target) {
            return false;
        }
        $num = 0;
        for ($i = $idx; $i < $len; $i++) {
            $digit = intval($s[$i]);
            $num = $num * 10 + $digit;
            if ($this->dfs($s, $i + 1, $sum + $num, $target, $len)) {
                return true;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func punishmentNumber(_ n: Int) -> Int {
        var total = 0
        for i in 1...n {
            let square = i * i
            let digits = Array(String(square))
            if canPartition(digits, 0, 0, i) {
                total += square
            }
        }
        return total
    }
    
    private func canPartition(_ s: [Character], _ idx: Int, _ currentSum: Int, _ target: Int) -> Bool {
        if idx == s.count {
            return currentSum == target
        }
        if currentSum > target { return false }
        var value = 0
        for i in idx..<s.count {
            let digit = Int(String(s[i]))!
            value = value * 10 + digit
            if canPartition(s, i + 1, currentSum + value, target) {
                return true
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun punishmentNumber(n: Int): Int {
        var total = 0L
        for (i in 1..n) {
            val sq = i * i
            if (canPartition(sq.toString(), i)) {
                total += sq
            }
        }
        return total.toInt()
    }

    private fun canPartition(numStr: String, target: Int): Boolean {
        return dfs(numStr, 0, 0, target)
    }

    private fun dfs(s: String, pos: Int, current: Int, target: Int): Boolean {
        if (pos == s.length) {
            return current == target
        }
        var value = 0
        for (i in pos until s.length) {
            value = value * 10 + (s[i] - '0')
            val newSum = current + value
            if (newSum > target) break
            if (dfs(s, i + 1, newSum, target)) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  int punishmentNumber(int n) {
    int total = 0;
    for (int i = 1; i <= n; i++) {
      int sq = i * i;
      String s = sq.toString();
      if (_canPartition(s, 0, 0, i)) {
        total += sq;
      }
    }
    return total;
  }

  bool _canPartition(String s, int idx, int curSum, int target) {
    if (idx == s.length) {
      return curSum == target;
    }
    if (curSum > target) return false;

    int val = 0;
    for (int end = idx; end < s.length; end++) {
      val = val * 10 + (s.codeUnitAt(end) - 48);
      int newSum = curSum + val;
      if (newSum > target) break;
      if (_canPartition(s, end + 1, newSum, target)) return true;
    }
    return false;
  }
}
```

## Golang

```go
package main

import "strconv"

func punishmentNumber(n int) int {
	var total int
	var dfs func(s string, idx, sum, target int) bool
	dfs = func(s string, idx, sum, target int) bool {
		if idx == len(s) {
			return sum == target
		}
		if sum > target {
			return false
		}
		val := 0
		for j := idx; j < len(s); j++ {
			val = val*10 + int(s[j]-'0')
			if dfs(s, j+1, sum+val, target) {
				return true
			}
		}
		return false
	}

	for i := 1; i <= n; i++ {
		sq := i * i
		if dfs(strconv.Itoa(sq), 0, 0, i) {
			total += sq
		}
	}
	return total
}
```

## Ruby

```ruby
def can_partition(s, target, idx = 0, sum = 0)
  return sum == target if idx == s.length
  return false if sum > target
  (idx + 1).upto(s.length) do |j|
    part = s[idx...j].to_i
    return true if can_partition(s, target, j, sum + part)
  end
  false
end

def punishment_number(n)
  total = 0
  (1..n).each do |i|
    sq = i * i
    total += sq if can_partition(sq.to_s, i)
  end
  total
end
```

## Scala

```scala
object Solution {
  def punishmentNumber(n: Int): Int = {
    var total = 0
    for (i <- 1 to n) {
      val sq = i * i
      if (canPartition(sq.toString, 0, 0, i)) {
        total += sq
      }
    }
    total
  }

  private def canPartition(s: String, idx: Int, curSum: Int, target: Int): Boolean = {
    if (idx == s.length) return curSum == target
    if (curSum > target) return false
    var end = idx + 1
    while (end <= s.length) {
      val part = s.substring(idx, end).toInt
      if (canPartition(s, end, curSum + part, target)) return true
      end += 1
    }
    false
  }
}
```

## Rust

```rust
impl Solution {
    pub fn punishment_number(n: i32) -> i32 {
        let mut total = 0i32;
        for i in 1..=n {
            let sq = i * i;
            let s = sq.to_string();
            if Self::can_partition(&s, i, 0, 0) {
                total += sq;
            }
        }
        total
    }

    fn can_partition(s: &str, target: i32, pos: usize, cur_sum: i32) -> bool {
        if pos == s.len() {
            return cur_sum == target;
        }
        if cur_sum > target {
            return false;
        }
        let bytes = s.as_bytes();
        let mut val = 0i32;
        for end in pos..s.len() {
            val = val * 10 + (bytes[end] - b'0') as i32;
            if cur_sum + val > target {
                break;
            }
            if Self::can_partition(s, target, end + 1, cur_sum + val) {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (punishment-number n)
  (-> exact-integer? exact-integer?)
  (let ((total 0))
    (for ([i (in-range 1 (add1 n))])
      (let* ((sq (* i i))
             (s (number->string sq)))
        (define (can-partition? str target)
          (letrec ((len (string-length str))
                   (dfs
                    (lambda (pos sum)
                      (cond [(> sum target) #f]
                            [(= pos len) (= sum target)]
                            [else
                             (let loop ((end (+ pos 1)))
                               (if (> end len)
                                   #f
                                   (let* ((sub (substring str pos end))
                                          (val (string->number sub))
                                          (new-sum (+ sum val)))
                                     (if (dfs end new-sum)
                                         #t
                                         (loop (+ end 1))))))])))
            (dfs 0 0)))
        (when (can-partition? s i)
          (set! total (+ total sq)))))
    total))
```

## Erlang

```erlang
-module(solution).
-export([punishment_number/1]).

-spec punishment_number(integer()) -> integer().
punishment_number(N) ->
    lists:foldl(fun(I, Acc) ->
        Square = I * I,
        case can_partition(Square, I) of
            true -> Acc + Square;
            false -> Acc
        end
    end, 0, lists:seq(1, N)).

can_partition(Square, Target) ->
    DigitsStr = integer_to_list(Square),
    Digits = [C - $0 || C <- DigitsStr],
    case Digits of
        [] -> false;
        [First|Rest] ->
            dfs(Rest, First, 0, Target)
    end.

dfs([], CurrNum, Sum, Target) ->
    (Sum + CurrNum) == Target;
dfs([D|Rest], CurrNum, Sum, Target) ->
    Continue = dfs(Rest, CurrNum * 10 + D, Sum, Target),
    Split = dfs(Rest, D, Sum + CurrNum, Target),
    Continue orelse Split.
```

## Elixir

```elixir
defmodule Solution do
  @spec punishment_number(n :: integer) :: integer
  def punishment_number(n) do
    1..n
    |> Enum.reduce(0, fn i, acc ->
      sq = i * i
      s = Integer.to_string(sq)

      if can_partition?(s, i) do
        acc + sq
      else
        acc
      end
    end)
  end

  defp can_partition?(s, target) do
    len = byte_size(s)
    dfs(0, 0, s, len, target)
  end

  defp dfs(pos, sum, _s, _len, target) when pos == _len do
    sum == target
  end

  defp dfs(pos, sum, s, len, target) do
    Enum.reduce_while((pos + 1)..len, false, fn e, _ ->
      part = String.slice(s, pos, e - pos)
      val = String.to_integer(part)
      new_sum = sum + val

      cond do
        new_sum > target ->
          {:halt, false}

        dfs(e, new_sum, s, len, target) ->
          {:halt, true}

        true ->
          {:cont, false}
      end
    end)
  end
end
```
