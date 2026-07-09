# 1010. Pairs of Songs With Total Durations Divisible by 60

## Cpp

```cpp
class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        long long ans = 0;
        int cnt[60] = {0};
        for (int t : time) {
            int r = t % 60;
            int need = (60 - r) % 60;
            ans += cnt[need];
            ++cnt[r];
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        long pairs = 0;
        int[] freq = new int[60];
        for (int t : time) {
            int r = t % 60;
            int complement = (60 - r) % 60;
            pairs += freq[complement];
            freq[r]++;
        }
        return (int) pairs;
    }
}
```

## Python

```python
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        cnt = [0] * 60
        pairs = 0
        for t in time:
            r = t % 60
            complement = (60 - r) % 60
            pairs += cnt[complement]
            cnt[r] += 1
        return pairs
```

## Python3

```python
from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = [0] * 60
        pairs = 0
        for t in time:
            r = t % 60
            complement = (60 - r) % 60
            pairs += count[complement]
            count[r] += 1
        return pairs
```

## C

```c
int numPairsDivisibleBy60(int* time, int timeSize) {
    int freq[60] = {0};
    long long pairs = 0;
    for (int i = 0; i < timeSize; ++i) {
        int r = time[i] % 60;
        int complement = (60 - r) % 60;
        pairs += freq[complement];
        freq[r]++;
    }
    return (int)pairs;
}
```

## Csharp

```csharp
public class Solution {
    public int NumPairsDivisibleBy60(int[] time) {
        long result = 0;
        int[] count = new int[60];
        foreach (int t in time) {
            int mod = t % 60;
            int complement = (60 - mod) % 60;
            result += count[complement];
            count[mod]++;
        }
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} time
 * @return {number}
 */
var numPairsDivisibleBy60 = function(time) {
    const cnt = new Array(60).fill(0);
    let pairs = 0;
    for (let t of time) {
        const mod = t % 60;
        const need = (60 - mod) % 60;
        pairs += cnt[need];
        cnt[mod]++;
    }
    return pairs;
};
```

## Typescript

```typescript
function numPairsDivisibleBy60(time: number[]): number {
    const freq = new Array(60).fill(0);
    let ans = 0;
    for (const t of time) {
        const r = t % 60;
        const complement = (60 - r) % 60;
        ans += freq[complement];
        freq[r]++;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $time
     * @return Integer
     */
    function numPairsDivisibleBy60($time) {
        $cnt = array_fill(0, 60, 0);
        $ans = 0;
        foreach ($time as $t) {
            $r = $t % 60;
            $comp = (60 - $r) % 60;
            $ans += $cnt[$comp];
            $cnt[$r]++;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numPairsDivisibleBy60(_ time: [Int]) -> Int {
        var count = [Int](repeating: 0, count: 60)
        var result = 0
        for t in time {
            let remainder = t % 60
            let complement = (60 - remainder) % 60
            result += count[complement]
            count[remainder] += 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numPairsDivisibleBy60(time: IntArray): Int {
        val count = IntArray(60)
        var pairs = 0L
        for (t in time) {
            val r = t % 60
            val complement = if (r == 0) 0 else 60 - r
            pairs += count[complement]
            count[r]++
        }
        return pairs.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numPairsDivisibleBy60(List<int> time) {
    List<int> cnt = List.filled(60, 0);
    int res = 0;
    for (int t in time) {
      int r = t % 60;
      int complement = (60 - r) % 60;
      res += cnt[complement];
      cnt[r]++;
    }
    return res;
  }
}
```

## Golang

```go
func numPairsDivisibleBy60(time []int) int {
    var cnt [60]int
    ans := 0
    for _, t := range time {
        r := t % 60
        complement := (60 - r) % 60
        ans += cnt[complement]
        cnt[r]++
    }
    return ans
}
```

## Ruby

```ruby
def num_pairs_divisible_by60(time)
  counts = Array.new(60, 0)
  pairs = 0
  time.each do |t|
    r = t % 60
    complement = (60 - r) % 60
    pairs += counts[complement]
    counts[r] += 1
  end
  pairs
end
```

## Scala

```scala
object Solution {
    def numPairsDivisibleBy60(time: Array[Int]): Int = {
        val cnt = new Array[Long](60)
        var ans: Long = 0L
        for (t <- time) {
            val r = t % 60
            val complement = (60 - r) % 60
            ans += cnt(complement)
            cnt(r) += 1
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_pairs_divisible_by60(time: Vec<i32>) -> i32 {
        let mut cnt = [0i64; 60];
        let mut ans: i64 = 0;
        for t in time {
            let r = (t % 60) as usize;
            let complement = if r == 0 { 0 } else { 60 - r };
            ans += cnt[complement];
            cnt[r] += 1;
        }
        ans as i32
    }
}
```

## Racket

```racket
#lang racket
(require racket/contract)

(define/contract (num-pairs-divisible-by60 time)
  (-> (listof exact-integer?) exact-integer?)
  (let ([freq (make-vector 60 0)])
    (for ([t time])
      (define r (modulo t 60))
      (vector-set! freq r (+ 1 (vector-ref freq r))))
    (define (choose2 n) (/ (* n (- n 1)) 2))
    (let* ([base (+ (choose2 (vector-ref freq 0))
                    (choose2 (vector-ref freq 30)))])
      (for/fold ([total base]) ([r (in-range 1 30)])
        (+ total (* (vector-ref freq r) (vector-ref freq (- 60 r))))))))
```

## Erlang

```erlang
-spec num_pairs_divisible_by60(Time :: [integer()]) -> integer().
num_pairs_divisible_by60(Time) ->
    {Ans, _} = lists:foldl(
        fun(T, {Acc, Freq}) ->
            R = T rem 60,
            Comp = if R == 0 -> 0; true -> 60 - R end,
            CountComp = maps:get(Comp, Freq, 0),
            NewAcc = Acc + CountComp,
            NewFreq = maps:update_with(R, fun(C) -> C + 1 end, 1, Freq),
            {NewAcc, NewFreq}
        end,
        {0, #{ }},
        Time),
    Ans.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_pairs_divisible_by60(time :: [integer]) :: integer
  def num_pairs_divisible_by60(time) do
    {ans, _} =
      Enum.reduce(time, {0, :array.new(60, default: 0)}, fn t, {cnt, arr} ->
        r = rem(t, 60)
        comp = if r == 0, do: 0, else: 60 - r
        cnt = cnt + :array.get(comp, arr)
        new_arr = :array.set(r, (:array.get(r, arr) + 1), arr)
        {cnt, new_arr}
      end)

    ans
  end
end
```
