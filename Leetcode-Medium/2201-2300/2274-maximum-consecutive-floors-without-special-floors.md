# 2274. Maximum Consecutive Floors Without Special Floors

## Cpp

```cpp
class Solution {
public:
    int maxConsecutive(int bottom, int top, vector<int>& special) {
        sort(special.begin(), special.end());
        int ans = 0;
        // before first special
        ans = max(ans, special[0] - bottom);
        // between specials
        for (int i = 1; i < (int)special.size(); ++i) {
            ans = max(ans, special[i] - special[i-1] - 1);
        }
        // after last special
        ans = max(ans, top - special.back());
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxConsecutive(int bottom, int top, int[] special) {
        java.util.Arrays.sort(special);
        int ans = 0;
        // gap before the first special floor
        ans = Math.max(ans, special[0] - bottom);
        // gaps between consecutive special floors
        for (int i = 1; i < special.length; i++) {
            ans = Math.max(ans, special[i] - special[i - 1] - 1);
        }
        // gap after the last special floor
        ans = Math.max(ans, top - special[special.length - 1]);
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        special.sort()
        ans = 0
        # floors before the first special floor
        ans = max(ans, special[0] - bottom)
        # floors between consecutive special floors
        for i in range(1, len(special)):
            gap = special[i] - special[i - 1] - 1
            if gap > ans:
                ans = gap
        # floors after the last special floor
        ans = max(ans, top - special[-1])
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        ans = 0
        # before first special
        ans = max(ans, special[0] - bottom)
        # between specials
        for i in range(1, len(special)):
            gap = special[i] - special[i - 1] - 1
            if gap > ans:
                ans = gap
        # after last special
        ans = max(ans, top - special[-1])
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int ai = *(const int *)a;
    int bi = *(const int *)b;
    return (ai > bi) - (ai < bi);
}

int maxConsecutive(int bottom, int top, int* special, int specialSize) {
    if (specialSize == 0) {
        return top - bottom + 1;
    }
    qsort(special, specialSize, sizeof(int), cmp_int);
    int ans = 0;
    int gap = special[0] - bottom;
    if (gap > ans) ans = gap;
    for (int i = 1; i < specialSize; ++i) {
        gap = special[i] - special[i - 1] - 1;
        if (gap > ans) ans = gap;
    }
    gap = top - special[specialSize - 1];
    if (gap > ans) ans = gap;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxConsecutive(int bottom, int top, int[] special)
    {
        Array.Sort(special);
        int n = special.Length;
        int maxGap = Math.Max(special[0] - bottom, top - special[n - 1]);

        for (int i = 1; i < n; i++)
        {
            int gap = special[i] - special[i - 1] - 1;
            if (gap > maxGap)
                maxGap = gap;
        }

        return maxGap;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} bottom
 * @param {number} top
 * @param {number[]} special
 * @return {number}
 */
var maxConsecutive = function(bottom, top, special) {
    special.sort((a, b) => a - b);
    let ans = 0;
    // floors before the first special floor
    ans = Math.max(ans, special[0] - bottom);
    // floors between consecutive special floors
    for (let i = 1; i < special.length; ++i) {
        ans = Math.max(ans, special[i] - special[i - 1] - 1);
    }
    // floors after the last special floor
    ans = Math.max(ans, top - special[special.length - 1]);
    return ans;
};
```

## Typescript

```typescript
function maxConsecutive(bottom: number, top: number, special: number[]): number {
    special.sort((a, b) => a - b);
    let maxGap = 0;
    // Floors before the first special floor
    maxGap = Math.max(maxGap, special[0] - bottom);
    // Gaps between consecutive special floors
    for (let i = 1; i < special.length; i++) {
        const gap = special[i] - special[i - 1] - 1;
        if (gap > maxGap) maxGap = gap;
    }
    // Floors after the last special floor
    maxGap = Math.max(maxGap, top - special[special.length - 1]);
    return maxGap;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $bottom
     * @param Integer $top
     * @param Integer[] $special
     * @return Integer
     */
    function maxConsecutive($bottom, $top, $special) {
        sort($special);
        $max = 0;
        
        // Gap before the first special floor
        $firstGap = $special[0] - $bottom;
        if ($firstGap > $max) {
            $max = $firstGap;
        }
        
        // Gaps between consecutive special floors
        $n = count($special);
        for ($i = 1; $i < $n; $i++) {
            $gap = $special[$i] - $special[$i - 1] - 1;
            if ($gap > $max) {
                $max = $gap;
            }
        }
        
        // Gap after the last special floor
        $lastGap = $top - $special[$n - 1];
        if ($lastGap > $max) {
            $max = $lastGap;
        }
        
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maxConsecutive(_ bottom: Int, _ top: Int, _ special: [Int]) -> Int {
        let sorted = special.sorted()
        var ans = 0
        
        if let first = sorted.first {
            ans = max(ans, first - bottom)
        }
        
        for i in 1..<sorted.count {
            let gap = sorted[i] - sorted[i - 1] - 1
            if gap > ans { ans = gap }
        }
        
        if let last = sorted.last {
            ans = max(ans, top - last)
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxConsecutive(bottom: Int, top: Int, special: IntArray): Int {
        if (special.isEmpty()) return top - bottom + 1
        special.sort()
        var ans = 0
        ans = maxOf(ans, special[0] - bottom)
        for (i in 1 until special.size) {
            val gap = special[i] - special[i - 1] - 1
            if (gap > ans) ans = gap
        }
        ans = maxOf(ans, top - special.last())
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxConsecutive(int bottom, int top, List<int> special) {
    special.sort();
    int ans = special[0] - bottom;
    for (int i = 1; i < special.length; ++i) {
      int gap = special[i] - special[i - 1] - 1;
      if (gap > ans) ans = gap;
    }
    int lastGap = top - special.last;
    if (lastGap > ans) ans = lastGap;
    return ans;
  }
}
```

## Golang

```go
import "sort"

func maxConsecutive(bottom int, top int, special []int) int {
	if len(special) == 0 {
		return top - bottom + 1
	}
	sort.Ints(special)
	ans := special[0] - bottom
	for i := 1; i < len(special); i++ {
		gap := special[i] - special[i-1] - 1
		if gap > ans {
			ans = gap
		}
	}
	lastGap := top - special[len(special)-1]
	if lastGap > ans {
		ans = lastGap
	}
	return ans
}
```

## Ruby

```ruby
def max_consecutive(bottom, top, special)
  special.sort!
  max_gap = [special[0] - bottom, top - special[-1]].max
  (1...special.length).each do |i|
    gap = special[i] - special[i - 1] - 1
    max_gap = gap if gap > max_gap
  end
  max_gap
end
```

## Scala

```scala
object Solution {
    def maxConsecutive(bottom: Int, top: Int, special: Array[Int]): Int = {
        java.util.Arrays.sort(special)
        var ans = 0
        // Floors before the first special floor
        ans = math.max(ans, special(0) - bottom)
        // Gaps between consecutive special floors
        for (i <- 1 until special.length) {
            val gap = special(i) - special(i - 1) - 1
            if (gap > ans) ans = gap
        }
        // Floors after the last special floor
        ans = math.max(ans, top - special(special.length - 1))
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_consecutive(bottom: i32, top: i32, mut special: Vec<i32>) -> i32 {
        special.sort_unstable();
        let mut ans = 0;
        // Gap before the first special floor
        ans = ans.max(special[0] - bottom);
        // Gaps between consecutive special floors
        for i in 1..special.len() {
            let gap = special[i] - special[i - 1] - 1;
            if gap > ans {
                ans = gap;
            }
        }
        // Gap after the last special floor
        ans = ans.max(top - special[special.len() - 1]);
        ans
    }
}
```

## Racket

```racket
(define/contract (max-consecutive bottom top special)
  (-> exact-integer? exact-integer? (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort special <))
         (n (length sorted)))
    (if (= n 0)
        (+ (- top bottom) 1)
        (let* ((first-sp (list-ref sorted 0))
               (last-sp (list-ref sorted (- n 1)))
               (initial-ans (max (- first-sp bottom) (- top last-sp))))
          (let loop ((i 1) (prev first-sp) (ans initial-ans))
            (if (>= i n)
                ans
                (let* ((curr (list-ref sorted i))
                       (gap (- curr prev 1))
                       (new-ans (if (> gap ans) gap ans)))
                  (loop (+ i 1) curr new-ans))))))))
```

## Erlang

```erlang
-module(solution).
-export([max_consecutive/3]).

-spec max_consecutive(Bottom :: integer(), Top :: integer(), Special :: [integer()]) -> integer().
max_consecutive(Bottom, Top, Special) ->
    Sorted = lists:sort(Special),
    case Sorted of
        [] -> 0;
        [First|Rest] ->
            FirstGap = First - Bottom,
            LastGap = Top - lists:last(Sorted),
            InitMax = erlang:max(FirstGap, LastGap),
            {_, Max} = lists:foldl(
                fun(Next, {Prev, CurMax}) ->
                    Gap = Next - Prev - 1,
                    NewMax = if Gap > CurMax -> Gap; true -> CurMax end,
                    {Next, NewMax}
                end,
                {First, InitMax},
                Rest
            ),
            Max
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_consecutive(bottom :: integer, top :: integer, special :: [integer]) :: integer
  def max_consecutive(bottom, top, special) do
    sorted = Enum.sort(special)

    # Gaps at the edges
    edge_gap =
      max(
        List.first(sorted) - bottom,
        top - List.last(sorted)
      )

    # Gaps between consecutive special floors
    middle_gap =
      sorted
      |> Enum.chunk_every(2, 1, [])
      |> Enum.reduce(0, fn [a, b], acc ->
        gap = b - a - 1
        if gap > acc, do: gap, else: acc
      end)

    max(edge_gap, middle_gap)
  end
end
```
