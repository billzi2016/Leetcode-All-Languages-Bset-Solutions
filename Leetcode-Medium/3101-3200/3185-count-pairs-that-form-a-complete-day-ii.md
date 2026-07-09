# 3185. Count Pairs That Form a Complete Day II

## Cpp

```cpp
class Solution {
public:
    long long countCompleteDayPairs(vector<int>& hours) {
        long long ans = 0;
        long long cnt[24] = {0};
        for (int h : hours) {
            int mod = h % 24;
            int need = (24 - mod) % 24;
            ans += cnt[need];
            ++cnt[mod];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long countCompleteDayPairs(int[] hours) {
        long[] freq = new long[24];
        long pairs = 0;
        for (int h : hours) {
            int r = h % 24;
            int need = (24 - r) % 24;
            pairs += freq[need];
            freq[r]++;
        }
        return pairs;
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
        cnt = [0] * 24
        ans = 0
        for h in hours:
            mod = h % 24
            complement = (-mod) % 24  # same as (24 - mod) % 24
            ans += cnt[complement]
            cnt[mod] += 1
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = [0] * 24
        ans = 0
        for h in hours:
            mod = h % 24
            target = (24 - mod) % 24
            ans += cnt[target]
            cnt[mod] += 1
        return ans
```

## C

```c
long long countCompleteDayPairs(int* hours, int hoursSize) {
    long long freq[24] = {0};
    long long ans = 0;
    for (int i = 0; i < hoursSize; ++i) {
        int mod = hours[i] % 24;
        int complement = (24 - mod) % 24;
        ans += freq[complement];
        freq[mod]++;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long CountCompleteDayPairs(int[] hours) {
        int[] count = new int[24];
        long ans = 0;
        foreach (int h in hours) {
            int rem = h % 24;
            int need = (24 - rem) % 24;
            ans += count[need];
            count[rem]++;
        }
        return ans;
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
    const cnt = new Array(24).fill(0);
    let ans = 0;
    for (const h of hours) {
        const r = h % 24;
        const need = (24 - r) % 24;
        ans += cnt[need];
        cnt[r]++;
    }
    return ans;
};
```

## Typescript

```typescript
function countCompleteDayPairs(hours: number[]): number {
    const cnt = new Array(24).fill(0);
    let ans = 0;
    for (const h of hours) {
        const r = h % 24;
        const need = (24 - r) % 24;
        ans += cnt[need];
        cnt[r]++;
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
        // Frequency array for remainders modulo 24
        $freq = array_fill(0, 24, 0);
        $pairs = 0;
        foreach ($hours as $h) {
            $mod = $h % 24;
            $need = (24 - $mod) % 24;
            $pairs += $freq[$need];
            $freq[$mod]++;
        }
        return $pairs;
    }
}
```

## Swift

```swift
class Solution {
    func countCompleteDayPairs(_ hours: [Int]) -> Int {
        var freq = Array(repeating: 0, count: 24)
        var ans: Int64 = 0
        for h in hours {
            let r = h % 24
            let target = (24 - r) % 24
            ans += Int64(freq[target])
            freq[r] += 1
        }
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countCompleteDayPairs(hours: IntArray): Long {
        val cnt = LongArray(24)
        var ans = 0L
        for (h in hours) {
            val r = h % 24
            val need = (24 - r) % 24
            ans += cnt[need]
            cnt[r]++
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countCompleteDayPairs(List<int> hours) {
    List<int> cnt = List.filled(24, 0);
    int ans = 0;
    for (int h in hours) {
      int r = h % 24;
      int complement = (24 - r) % 24;
      ans += cnt[complement];
      cnt[r] += 1;
    }
    return ans;
  }
}
```

## Golang

```go
func countCompleteDayPairs(hours []int) int64 {
	var cnt [24]int64
	var ans int64
	for _, h := range hours {
		r := h % 24
		c := (24 - r) % 24
		ans += cnt[c]
		cnt[r]++
	}
	return ans
}
```

## Ruby

```ruby
def count_complete_day_pairs(hours)
  counts = Array.new(24, 0)
  ans = 0
  hours.each do |h|
    r = h % 24
    c = (24 - r) % 24
    ans += counts[c]
    counts[r] += 1
  end
  ans
end
```

## Scala

```scala
object Solution {
    def countCompleteDayPairs(hours: Array[Int]): Long = {
        val cnt = new Array[Long](24)
        var ans: Long = 0L
        for (h <- hours) {
            val r = h % 24
            val need = (24 - r) % 24
            ans += cnt(need)
            cnt(r) += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_complete_day_pairs(hours: Vec<i32>) -> i64 {
        let mut cnt = [0i64; 24];
        let mut ans: i64 = 0;
        for h in hours {
            let r = (h % 24) as usize;
            let need = (24 - r) % 24;
            ans += cnt[need];
            cnt[r] += 1;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (count-complete-day-pairs hours)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([cnt (make-vector 24 0)]
         [ans 0])
    (for ([h hours])
      (let* ([r (modulo h 24)]
             [c (if (= r 0) 0 (- 24 r))])
        (set! ans (+ ans (vector-ref cnt c)))
        (vector-set! cnt r (+ 1 (vector-ref cnt r)))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([count_complete_day_pairs/1]).

-spec count_complete_day_pairs(Hours :: [integer()]) -> integer().
count_complete_day_pairs(Hours) ->
    count_complete_day_pairs(Hours, #{}, 0).

count_complete_day_pairs([], _Map, Acc) ->
    Acc;
count_complete_day_pairs([H|T], Map, Acc) ->
    R = H rem 24,
    Complement = (24 - R) rem 24,
    CountComp = maps:get(Complement, Map, 0),
    NewAcc = Acc + CountComp,
    PrevCount = maps:get(R, Map, 0),
    NewMap = maps:put(R, PrevCount + 1, Map),
    count_complete_day_pairs(T, NewMap, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_complete_day_pairs(hours :: [integer]) :: integer
  def count_complete_day_pairs(hours) do
    {ans, _} =
      Enum.reduce(hours, {0, %{}}, fn hour, {cnt, freq} ->
        r = rem(hour, 24)
        complement = rem(24 - r, 24)
        add = Map.get(freq, complement, 0)
        new_cnt = cnt + add
        new_freq = Map.update(freq, r, 1, &(&1 + 1))
        {new_cnt, new_freq}
      end)

    ans
  end
end
```
