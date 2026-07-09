# 1578. Minimum Time to Make Rope Colorful

## Cpp

```cpp
class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        long long total = 0;
        int n = colors.size();
        int i = 0;
        while (i < n) {
            char cur = colors[i];
            int maxTime = neededTime[i];
            long long sum = neededTime[i];
            ++i;
            while (i < n && colors[i] == cur) {
                maxTime = max(maxTime, neededTime[i]);
                sum += neededTime[i];
                ++i;
            }
            total += sum - maxTime;
        }
        return (int)total;
    }
};
```

## Java

```java
class Solution {
    public int minCost(String colors, int[] neededTime) {
        long total = 0;
        int n = colors.length();
        int i = 0;
        while (i < n) {
            char cur = colors.charAt(i);
            int sum = neededTime[i];
            int max = neededTime[i];
            i++;
            while (i < n && colors.charAt(i) == cur) {
                sum += neededTime[i];
                if (neededTime[i] > max) {
                    max = neededTime[i];
                }
                i++;
            }
            total += sum - max;
        }
        return (int) total;
    }
}
```

## Python

```python
class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        total = 0
        cur_max = 0
        cur_sum = 0
        prev = ''
        for c, t in zip(colors, neededTime):
            if c != prev:
                # finish previous group
                total += cur_sum - cur_max
                # start new group
                cur_sum = t
                cur_max = t
                prev = c
            else:
                cur_sum += t
                if t > cur_max:
                    cur_max = t
        # add last group contribution
        total += cur_sum - cur_max
        return total
```

## Python3

```python
from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        i = 0
        n = len(colors)
        while i < n:
            cur_char = colors[i]
            group_sum = 0
            group_max = 0
            # process contiguous segment of same color
            while i < n and colors[i] == cur_char:
                t = neededTime[i]
                group_sum += t
                if t > group_max:
                    group_max = t
                i += 1
            total += group_sum - group_max
        return total
```

## C

```c
int minCost(char* colors, int* neededTime, int neededTimeSize) {
    long long total = 0;
    int i = 0;
    while (i < neededTimeSize) {
        char cur = colors[i];
        long long sum = neededTime[i];
        int mx = neededTime[i];
        int j = i + 1;
        while (j < neededTimeSize && colors[j] == cur) {
            sum += neededTime[j];
            if (neededTime[j] > mx) mx = neededTime[j];
            ++j;
        }
        total += sum - mx;
        i = j;
    }
    return (int)total;
}
```

## Csharp

```csharp
public class Solution {
    public int MinCost(string colors, int[] neededTime) {
        int n = colors.Length;
        int total = 0;
        int sumInGroup = neededTime[0];
        int maxInGroup = neededTime[0];

        for (int i = 1; i < n; i++) {
            if (colors[i] == colors[i - 1]) {
                sumInGroup += neededTime[i];
                if (neededTime[i] > maxInGroup) {
                    maxInGroup = neededTime[i];
                }
            } else {
                total += sumInGroup - maxInGroup;
                sumInGroup = neededTime[i];
                maxInGroup = neededTime[i];
            }
        }

        total += sumInGroup - maxInGroup;
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} colors
 * @param {number[]} neededTime
 * @return {number}
 */
var minCost = function(colors, neededTime) {
    let total = 0;
    const n = colors.length;
    let i = 0;
    while (i < n) {
        let sum = 0;
        let maxTime = 0;
        const curColor = colors[i];
        while (i < n && colors[i] === curColor) {
            const t = neededTime[i];
            sum += t;
            if (t > maxTime) maxTime = t;
            i++;
        }
        total += sum - maxTime; // keep the most expensive balloon, remove others
    }
    return total;
};
```

## Typescript

```typescript
function minCost(colors: string, neededTime: number[]): number {
    let n = colors.length;
    let result = 0;
    let i = 0;
    while (i < n) {
        let sum = 0;
        let maxTime = 0;
        const currentColor = colors[i];
        while (i < n && colors[i] === currentColor) {
            sum += neededTime[i];
            if (neededTime[i] > maxTime) maxTime = neededTime[i];
            i++;
        }
        result += sum - maxTime;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $colors
     * @param Integer[] $neededTime
     * @return Integer
     */
    function minCost($colors, $neededTime) {
        $n = strlen($colors);
        $total = 0;
        $i = 0;
        while ($i < $n) {
            $maxTime = $neededTime[$i];
            $sum = $neededTime[$i];
            $j = $i + 1;
            while ($j < $n && $colors[$j] === $colors[$i]) {
                $sum += $neededTime[$j];
                if ($neededTime[$j] > $maxTime) {
                    $maxTime = $neededTime[$j];
                }
                $j++;
            }
            $total += $sum - $maxTime;
            $i = $j;
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func minCost(_ colors: String, _ neededTime: [Int]) -> Int {
        let chars = Array(colors)
        var total = 0
        var i = 0
        let n = chars.count
        while i < n {
            var groupMax = neededTime[i]
            var groupSum = neededTime[i]
            var j = i + 1
            while j < n && chars[j] == chars[i] {
                groupSum += neededTime[j]
                if neededTime[j] > groupMax {
                    groupMax = neededTime[j]
                }
                j += 1
            }
            total += groupSum - groupMax
            i = j
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCost(colors: String, neededTime: IntArray): Int {
        var total = 0
        var i = 0
        val n = colors.length
        while (i < n) {
            var sum = neededTime[i]
            var max = neededTime[i]
            var j = i + 1
            while (j < n && colors[j] == colors[i]) {
                sum += neededTime[j]
                if (neededTime[j] > max) max = neededTime[j]
                j++
            }
            total += sum - max
            i = j
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int minCost(String colors, List<int> neededTime) {
    int n = colors.length;
    int total = 0;
    int i = 0;
    while (i < n) {
      int maxTime = neededTime[i];
      int sum = neededTime[i];
      int j = i;
      while (j + 1 < n && colors.codeUnitAt(j + 1) == colors.codeUnitAt(i)) {
        j++;
        sum += neededTime[j];
        if (neededTime[j] > maxTime) {
          maxTime = neededTime[j];
        }
      }
      total += sum - maxTime;
      i = j + 1;
    }
    return total;
  }
}
```

## Golang

```go
func minCost(colors string, neededTime []int) int {
    total := 0
    n := len(colors)
    if n == 0 {
        return 0
    }
    groupSum := neededTime[0]
    groupMax := neededTime[0]

    for i := 1; i < n; i++ {
        if colors[i] == colors[i-1] {
            // same group, accumulate
            groupSum += neededTime[i]
            if neededTime[i] > groupMax {
                groupMax = neededTime[i]
            }
        } else {
            // end of current group
            total += groupSum - groupMax
            // start new group
            groupSum = neededTime[i]
            groupMax = neededTime[i]
        }
    }
    // add last group's cost
    total += groupSum - groupMax
    return total
}
```

## Ruby

```ruby
def min_cost(colors, needed_time)
  total = 0
  i = 0
  n = colors.length
  while i < n
    cur_char = colors[i]
    sum = needed_time[i]
    max_t = needed_time[i]
    j = i + 1
    while j < n && colors[j] == cur_char
      sum += needed_time[j]
      max_t = [max_t, needed_time[j]].max
      j += 1
    end
    total += sum - max_t
    i = j
  end
  total
end
```

## Scala

```scala
object Solution {
    def minCost(colors: String, neededTime: Array[Int]): Int = {
        var total = 0
        val n = colors.length
        var i = 0
        while (i < n) {
            var sum = 0
            var max = 0
            val cur = colors.charAt(i)
            var j = i
            while (j < n && colors.charAt(j) == cur) {
                val t = neededTime(j)
                sum += t
                if (t > max) max = t
                j += 1
            }
            total += sum - max
            i = j
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
        let bytes = colors.as_bytes();
        let n = bytes.len();
        let mut total = 0i32;
        let mut i = 0usize;
        while i < n {
            let mut sum = needed_time[i];
            let mut max_t = needed_time[i];
            let mut j = i + 1;
            while j < n && bytes[j] == bytes[i] {
                sum += needed_time[j];
                if needed_time[j] > max_t {
                    max_t = needed_time[j];
                }
                j += 1;
            }
            total += sum - max_t;
            i = j;
        }
        total
    }
}
```

## Racket

```racket
(define/contract (min-cost colors neededTime)
  (-> string? (listof exact-integer?) exact-integer?)
  (let* ((n (string-length colors))
         (times (list->vector neededTime)))
    (if (= n 0)
        0
        (let loop ((i 1)
                   (prev-char (string-ref colors 0))
                   (group-sum (vector-ref times 0))
                   (group-max (vector-ref times 0))
                   (total 0))
          (if (= i n)
              (+ total (- group-sum group-max))
              (let ((c (string-ref colors i))
                    (t (vector-ref times i)))
                (if (char=? c prev-char)
                    (loop (add1 i) c (+ group-sum t) (max group-max t) total)
                    (let ((new-total (+ total (- group-sum group-max))))
                      (loop (add1 i) c t t new-total)))))))))
```

## Erlang

```erlang
-module(solution).
-export([min_cost/2]).

-spec min_cost(unicode:unicode_binary(), [integer()]) -> integer().
min_cost(Colors, NeededTime) ->
    CharList = unicode:characters_to_list(Colors),
    process(CharList, NeededTime, undefined, 0, 0, 0).

process([], [], _PrevChar, GroupSum, GroupMax, Acc) ->
    Acc + (GroupSum - GroupMax);
process([C|Cs], [T|Ts], PrevChar, GroupSum, GroupMax, Acc) ->
    case C == PrevChar of
        true ->
            NewSum = GroupSum + T,
            NewMax = if T > GroupMax -> T; true -> GroupMax end,
            process(Cs, Ts, PrevChar, NewSum, NewMax, Acc);
        false ->
            NewAcc = Acc + (GroupSum - GroupMax),
            process(Cs, Ts, C, T, T, NewAcc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost(colors :: String.t(), needed_time :: [integer]) :: integer
  def min_cost(colors, needed_time) do
    chars = String.graphemes(colors)

    {total, _prev_c, {group_sum, group_max}} =
      Enum.reduce(Enum.zip(chars, needed_time), {0, nil, {0, 0}}, fn {c, t},
                                                                   {acc, prev_c,
                                                                    {g_sum, g_max}} ->
        if c == prev_c do
          {acc, prev_c, {g_sum + t, max(g_max, t)}}
        else
          added = g_sum - g_max
          {acc + added, c, {t, t}}
        end
      end)

    total + (group_sum - group_max)
  end
end
```
