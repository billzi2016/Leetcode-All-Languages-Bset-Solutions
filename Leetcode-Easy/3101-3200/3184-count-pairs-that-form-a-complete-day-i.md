# 3184. Count Pairs That Form a Complete Day I

## Cpp

```cpp
class Solution {
public:
    int countCompleteDayPairs(vector<int>& hours) {
        vector<int> cnt(24, 0);
        int ans = 0;
        for (int h : hours) {
            int r = h % 24;
            int need = (24 - r) % 24;
            ans += cnt[need];
            ++cnt[r];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countCompleteDayPairs(int[] hours) {
        int[] freq = new int[24];
        int count = 0;
        for (int h : hours) {
            int rem = h % 24;
            int need = (24 - rem) % 24;
            count += freq[need];
            freq[rem]++;
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        from collections import defaultdict
        cnt = defaultdict(int)
        pairs = 0
        for h in hours:
            r = h % 24
            need = (-r) % 24  # equivalent to (24 - r) % 24
            pairs += cnt[need]
            cnt[r] += 1
        return pairs
```

## Python3

```python
from typing import List
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = [0] * 24
        pairs = 0
        for h in hours:
            r = h % 24
            complement = (24 - r) % 24
            pairs += cnt[complement]
            cnt[r] += 1
        return pairs
```

## C

```c
int countCompleteDayPairs(int* hours, int hoursSize) {
    int cnt[24] = {0};
    int ans = 0;
    for (int i = 0; i < hoursSize; ++i) {
        int r = hours[i] % 24;
        int need = (24 - r) % 24;
        ans += cnt[need];
        cnt[r]++;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountCompleteDayPairs(int[] hours)
    {
        long result = 0;
        int[] remainderCount = new int[24];
        foreach (int h in hours)
        {
            int r = h % 24;
            int need = (24 - r) % 24;
            result += remainderCount[need];
            remainderCount[r]++;
        }
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} hours
 * @return {number}
 */
var countCompleteDayPairs = function(hours) {
    const MOD = 24;
    const freq = new Array(MOD).fill(0);
    let pairs = 0;
    for (const h of hours) {
        const r = ((h % MOD) + MOD) % MOD; // ensure non‑negative
        const need = (MOD - r) % MOD;
        pairs += freq[need];
        freq[r]++;
    }
    return pairs;
};
```

## Typescript

```typescript
function countCompleteDayPairs(hours: number[]): number {
    const freq = new Array(24).fill(0);
    let ans = 0;
    for (const h of hours) {
        const rem = ((h % 24) + 24) % 24; // ensure non-negative
        const need = (24 - rem) % 24;
        ans += freq[need];
        freq[rem]++;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $hours
     * @return Integer
     */
    function countCompleteDayPairs($hours) {
        $cnt = array_fill(0, 24, 0);
        $ans = 0;
        foreach ($hours as $h) {
            $r = $h % 24;
            $need = (24 - $r) % 24;
            $ans += $cnt[$need];
            $cnt[$r]++;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countCompleteDayPairs(_ hours: [Int]) -> Int {
        var remainderCount = Array(repeating: 0, count: 24)
        var pairs = 0
        for hour in hours {
            let r = hour % 24
            let need = (24 - r) % 24
            pairs += remainderCount[need]
            remainderCount[r] += 1
        }
        return pairs
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countCompleteDayPairs(hours: IntArray): Int {
        val count = IntArray(24)
        var pairs = 0
        for (h in hours) {
            val r = h % 24
            val need = (24 - r) % 24
            pairs += count[need]
            count[r]++
        }
        return pairs
    }
}
```

## Dart

```dart
class Solution {
  int countCompleteDayPairs(List<int> hours) {
    List<int> freq = List.filled(24, 0);
    int ans = 0;
    for (int h in hours) {
      int r = h % 24;
      int need = (24 - r) % 24;
      ans += freq[need];
      freq[r]++;
    }
    return ans;
  }
}
```

## Golang

```go
func countCompleteDayPairs(hours []int) int {
    var freq [24]int
    pairs := 0
    for _, h := range hours {
        r := h % 24
        need := (24 - r) % 24
        pairs += freq[need]
        freq[r]++
    }
    return pairs
}
```

## Ruby

```ruby
def count_complete_day_pairs(hours)
  freq = Array.new(24, 0)
  count = 0
  hours.each do |h|
    r = h % 24
    comp = (24 - r) % 24
    count += freq[comp]
    freq[r] += 1
  end
  count
end
```

## Scala

```scala
object Solution {
    def countCompleteDayPairs(hours: Array[Int]): Int = {
        import scala.collection.mutable
        val freq = mutable.Map.empty[Int, Int].withDefaultValue(0)
        var ans = 0L
        for (h <- hours) {
            val rem = ((h % 24) + 24) % 24
            val need = (24 - rem) % 24
            ans += freq(need)
            freq(rem) += 1
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_complete_day_pairs(hours: Vec<i32>) -> i32 {
        let mut cnt = [0i32; 24];
        let mut ans = 0i32;
        for h in hours {
            let rem = ((h % 24) + 24) % 24;
            let need = (24 - rem) % 24;
            ans += cnt[need as usize];
            cnt[rem as usize] += 1;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (count-complete-day-pairs hours)
  (-> (listof exact-integer?) exact-integer?)
  (let ([freq (make-hash)]
        [cnt 0])
    (for ([h hours])
      (let* ([rem (modulo h 24)]
             [need (modulo (- rem) 24)]
             [prev (hash-ref freq need 0)])
        (set! cnt (+ cnt prev))
        (hash-set! freq rem (+ 1 (hash-ref freq rem 0)))))
    cnt))
```

## Erlang

```erlang
-spec count_complete_day_pairs(Hours :: [integer()]) -> integer().
count_complete_day_pairs(Hours) ->
    Map = build_counts(Hours, #{}),
    C0 = maps:get(0, Map, 0),
    C12 = maps:get(12, Map, 0),
    Res0 = C0 * (C0 - 1) div 2,
    Res12 = C12 * (C12 - 1) div 2,
    PairSum = lists:foldl(
        fun(R, Acc) ->
            CountR = maps:get(R, Map, 0),
            CountComp = maps:get(24 - R, Map, 0),
            Acc + CountR * CountComp
        end,
        0,
        lists:seq(1, 11)
    ),
    Res0 + Res12 + PairSum.

build_counts([], Map) -> Map;
build_counts([H | T], Map) ->
    R = H rem 24,
    C = maps:get(R, Map, 0),
    NewMap = maps:put(R, C + 1, Map),
    build_counts(T, NewMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_complete_day_pairs(hours :: [integer]) :: integer
  def count_complete_day_pairs(hours) do
    {count, _} =
      Enum.reduce(hours, {0, %{}}, fn h, {acc, freq_map} ->
        r = rem(h, 24)
        complement = if r == 0, do: 0, else: 24 - r
        add = Map.get(freq_map, complement, 0)

        updated_map =
          Map.update(freq_map, r, 1, fn existing -> existing + 1 end)

        {acc + add, updated_map}
      end)

    count
  end
end
```
