# 1291. Sequential Digits

## Cpp

```cpp
class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        vector<int> result;
        for (int len = 2; len <= 9; ++len) {
            for (int start = 1; start + len - 1 <= 9; ++start) {
                int num = 0;
                for (int i = 0; i < len; ++i) {
                    num = num * 10 + (start + i);
                }
                if (num >= low && num <= high) {
                    result.push_back(num);
                }
            }
        }
        sort(result.begin(), result.end());
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        List<Integer> result = new ArrayList<>();
        for (int start = 1; start <= 9; start++) {
            int num = start;
            for (int next = start + 1; next <= 9; next++) {
                num = num * 10 + next;
                if (num > high) break;
                if (num >= low) result.add(num);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        res = []
        max_len = len(str(high))
        for length in range(2, max_len + 1):
            for start in range(1, 10 - length + 1):
                num = 0
                for i in range(length):
                    num = num * 10 + (start + i)
                if low <= num <= high:
                    res.append(num)
        return sorted(res)
```

## Python3

```python
from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for length in range(2, 10):
            for start in range(1, 11 - length):
                num = 0
                for i in range(length):
                    num = num * 10 + (start + i)
                if low <= num <= high:
                    res.append(num)
        res.sort()
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sequentialDigits(int low, int high, int* returnSize) {
    int temp[36];
    int cnt = 0;
    for (int len = 2; len <= 9; ++len) {
        for (int start = 1; start + len - 1 <= 9; ++start) {
            int num = 0;
            for (int i = 0; i < len; ++i) {
                num = num * 10 + (start + i);
            }
            if (num > high) break;
            if (num >= low) temp[cnt++] = num;
        }
    }
    *returnSize = cnt;
    if (cnt == 0) return NULL;
    int* ans = (int*)malloc(cnt * sizeof(int));
    for (int i = 0; i < cnt; ++i) {
        ans[i] = temp[i];
    }
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> SequentialDigits(int low, int high) {
        var result = new List<int>();
        for (int length = 2; length <= 9; length++) {
            for (int start = 1; start + length - 1 <= 9; start++) {
                int num = 0;
                for (int i = 0; i < length; i++) {
                    num = num * 10 + (start + i);
                }
                if (num > high) break;
                if (num >= low) result.Add(num);
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var sequentialDigits = function(low, high) {
    const result = [];
    for (let len = 2; len <= 9; len++) {
        for (let start = 1; start + len - 1 <= 9; start++) {
            let num = 0;
            for (let i = 0; i < len; i++) {
                num = num * 10 + (start + i);
            }
            if (num > high) break;
            if (num >= low) result.push(num);
        }
    }
    return result;
};
```

## Typescript

```typescript
function sequentialDigits(low: number, high: number): number[] {
    const res: number[] = [];
    for (let len = 2; len <= 9; len++) {
        for (let start = 1; start + len - 1 <= 9; start++) {
            let num = 0;
            for (let i = 0; i < len; i++) {
                num = num * 10 + (start + i);
            }
            if (num >= low && num <= high) {
                res.push(num);
            }
        }
    }
    res.sort((a, b) => a - b);
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $low
     * @param Integer $high
     * @return Integer[]
     */
    function sequentialDigits($low, $high) {
        $result = [];
        $digits = '123456789';
        $lenLow = strlen((string)$low);
        $lenHigh = strlen((string)$high);
        for ($len = $lenLow; $len <= $lenHigh; $len++) {
            for ($start = 0; $start + $len <= 9; $start++) {
                $numStr = substr($digits, $start, $len);
                $num = intval($numStr);
                if ($num >= $low && $num <= $high) {
                    $result[] = $num;
                }
            }
        }
        sort($result);
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func sequentialDigits(_ low: Int, _ high: Int) -> [Int] {
        var result = [Int]()
        for length in 2...9 {
            for start in 1...(10 - length) {
                var num = 0
                for i in 0..<length {
                    num = num * 10 + (start + i)
                }
                if num > high { break }
                if num >= low {
                    result.append(num)
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sequentialDigits(low: Int, high: Int): List<Int> {
        val result = mutableListOf<Int>()
        for (len in 2..9) {
            for (start in 1..(10 - len)) {
                var num = 0
                for (i in 0 until len) {
                    num = num * 10 + (start + i)
                }
                if (num > high) break
                if (num >= low) result.add(num)
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> sequentialDigits(int low, int high) {
    List<int> result = [];
    for (int length = 2; length <= 9; ++length) {
      for (int start = 1; start + length - 1 <= 9; ++start) {
        int num = 0;
        for (int i = 0; i < length; ++i) {
          num = num * 10 + (start + i);
        }
        if (num >= low && num <= high) {
          result.add(num);
        }
      }
    }
    result.sort();
    return result;
  }
}
```

## Golang

```go
import "sort"

func sequentialDigits(low int, high int) []int {
    res := []int{}
    for start := 1; start <= 9; start++ {
        num := 0
        for d := start; d <= 9; d++ {
            num = num*10 + d
            if num > high {
                break
            }
            if num >= low {
                res = append(res, num)
            }
        }
    }
    sort.Ints(res)
    return res
}
```

## Ruby

```ruby
def sequential_digits(low, high)
  result = []
  (1..9).each do |start|
    num = 0
    digit = start
    while digit <= 9
      num = num * 10 + digit
      break if num > high
      result << num if num >= low
      digit += 1
    end
  end
  result.sort
end
```

## Scala

```scala
object Solution {
    def sequentialDigits(low: Int, high: Int): List[Int] = {
        val res = scala.collection.mutable.ListBuffer[Int]()
        for (len <- 2 to 9) {
            for (start <- 1 to 10 - len) {
                var num = 0
                for (i <- 0 until len) {
                    num = num * 10 + (start + i)
                }
                if (num >= low && num <= high) res += num
            }
        }
        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        let mut res = Vec::new();
        for len in 2..=9 {
            for start in 1..=10 - len {
                let mut num = 0;
                for d in start..start + len {
                    num = num * 10 + d as i32;
                }
                if num >= low && num <= high {
                    res.push(num);
                }
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (sequential-digits low high)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  (let ((build-number
         (lambda (start len)
           (let loop ((i 0) (num 0))
             (if (= i len)
                 num
                 (loop (+ i 1) (+ (* num 10) (+ start i))))))))
    (let ((nums
            (for/fold ([acc '()])
                      ([len (in-range 2 10)]
                       [start (in-range 1 (+ 1 (- 10 len)))])
              (let ((num (build-number start len)))
                (if (and (>= num low) (<= num high))
                    (cons num acc)
                    acc)))))
      (reverse nums))))
```

## Erlang

```erlang
-module(solution).
-export([sequential_digits/2]).

-spec sequential_digits(Low :: integer(), High :: integer()) -> [integer()].
sequential_digits(Low, High) ->
    Seq = generate(),
    Filtered = [N || N <- Seq, N >= Low, N =< High],
    lists:sort(Filtered).

generate() ->
    lists:foldl(fun(S, Acc) ->
        build_seq(S, Acc)
    end, [], lists:seq(1, 9)).

build_seq(CurrNum, Acc) ->
    NewAcc = [CurrNum | Acc],
    LastDigit = CurrNum rem 10,
    NextDigit = LastDigit + 1,
    if
        NextDigit =< 9 ->
            build_seq(CurrNum * 10 + NextDigit, NewAcc);
        true ->
            NewAcc
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec sequential_digits(low :: integer, high :: integer) :: [integer]
  def sequential_digits(low, high) do
    seq_numbers =
      for len <- 2..9,
          start <- 1..(10 - len) do
        Enum.reduce(start..(start + len - 1), 0, fn d, acc -> acc * 10 + d end)
      end

    seq_numbers
    |> Enum.filter(fn n -> n >= low and n <= high end)
    |> Enum.sort()
  end
end
```
