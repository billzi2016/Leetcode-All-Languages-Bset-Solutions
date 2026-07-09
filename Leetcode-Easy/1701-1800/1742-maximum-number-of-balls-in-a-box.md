# 1742. Maximum Number of Balls in a Box

## Cpp

```cpp
class Solution {
public:
    int countBalls(int lowLimit, int highLimit) {
        // Maximum possible digit sum for numbers up to 100000 is 45 (9*5)
        const int MAX_SUM = 45;
        int cnt[MAX_SUM + 1] = {0};
        int ans = 0;
        for (int num = lowLimit; num <= highLimit; ++num) {
            int s = 0, x = num;
            while (x > 0) {
                s += x % 10;
                x /= 10;
            }
            ++cnt[s];
            if (cnt[s] > ans) ans = cnt[s];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countBalls(int lowLimit, int highLimit) {
        // Maximum possible digit sum for numbers up to 100000 is 45 (9+9+9+9+9)
        int[] cnt = new int[46];
        int max = 0;
        for (int i = lowLimit; i <= highLimit; i++) {
            int sum = digitSum(i);
            cnt[sum]++;
            if (cnt[sum] > max) {
                max = cnt[sum];
            }
        }
        return max;
    }

    private int digitSum(int num) {
        int s = 0;
        while (num > 0) {
            s += num % 10;
            num /= 10;
        }
        return s;
    }
}
```

## Python

```python
class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        # Maximum possible digit sum for 10^5 is 9*5 = 45
        counts = [0] * 46
        max_balls = 0
        for num in range(lowLimit, highLimit + 1):
            s = 0
            x = num
            while x:
                s += x % 10
                x //= 10
            # handle case when num is 0 (not possible per constraints)
            counts[s] += 1
            if counts[s] > max_balls:
                max_balls = counts[s]
        return max_balls
```

## Python3

```python
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        counts = [0] * 46  # maximum digit sum for numbers up to 10^5 is 45
        max_balls = 0
        for num in range(lowLimit, highLimit + 1):
            s = 0
            x = num
            while x:
                s += x % 10
                x //= 10
            counts[s] += 1
            if counts[s] > max_balls:
                max_balls = counts[s]
        return max_balls
```

## C

```c
int countBalls(int lowLimit, int highLimit) {
    int freq[200] = {0};
    int maxcnt = 0;
    for (int i = lowLimit; i <= highLimit; ++i) {
        int x = i, sum = 0;
        while (x > 0) {
            sum += x % 10;
            x /= 10;
        }
        ++freq[sum];
        if (freq[sum] > maxcnt) {
            maxcnt = freq[sum];
        }
    }
    return maxcnt;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountBalls(int lowLimit, int highLimit)
    {
        int[] counts = new int[46]; // maximum digit sum for numbers up to 100000 is 45
        int max = 0;
        for (int i = lowLimit; i <= highLimit; i++)
        {
            int sum = DigitSum(i);
            counts[sum]++;
            if (counts[sum] > max) max = counts[sum];
        }
        return max;
    }

    private int DigitSum(int num)
    {
        int sum = 0;
        while (num > 0)
        {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} lowLimit
 * @param {number} highLimit
 * @return {number}
 */
var countBalls = function(lowLimit, highLimit) {
    const counts = new Array(46).fill(0); // max digit sum for 100000 is 45
    let max = 0;
    
    const digitSum = (num) => {
        let sum = 0;
        while (num > 0) {
            sum += num % 10;
            num = Math.floor(num / 10);
        }
        return sum;
    };
    
    for (let i = lowLimit; i <= highLimit; ++i) {
        const s = digitSum(i);
        counts[s] += 1;
        if (counts[s] > max) max = counts[s];
    }
    
    return max;
};
```

## Typescript

```typescript
function countBalls(lowLimit: number, highLimit: number): number {
    const maxPossibleSum = 45; // for numbers up to 99999
    const counts = new Uint32Array(maxPossibleSum + 1);
    let maxCount = 0;

    for (let num = lowLimit; num <= highLimit; ++num) {
        let n = num;
        let sum = 0;
        while (n > 0) {
            sum += n % 10;
            n = Math.floor(n / 10);
        }
        const c = ++counts[sum];
        if (c > maxCount) maxCount = c;
    }

    return maxCount;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $lowLimit
     * @param Integer $highLimit
     * @return Integer
     */
    function countBalls($lowLimit, $highLimit) {
        $counts = [];
        $max = 0;
        for ($i = $lowLimit; $i <= $highLimit; $i++) {
            $sum = 0;
            $x = $i;
            while ($x > 0) {
                $sum += $x % 10;
                $x = intdiv($x, 10);
            }
            if (isset($counts[$sum])) {
                $counts[$sum]++;
            } else {
                $counts[$sum] = 1;
            }
            if ($counts[$sum] > $max) {
                $max = $counts[$sum];
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func countBalls(_ lowLimit: Int, _ highLimit: Int) -> Int {
        var counts = [Int](repeating: 0, count: 55)
        var maxCount = 0
        for num in lowLimit...highLimit {
            var n = num
            var sum = 0
            while n > 0 {
                sum += n % 10
                n /= 10
            }
            counts[sum] += 1
            if counts[sum] > maxCount {
                maxCount = counts[sum]
            }
        }
        return maxCount
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countBalls(lowLimit: Int, highLimit: Int): Int {
        val freq = IntArray(46) // maximum digit sum for numbers <= 100000 is 45
        var maxCount = 0
        for (num in lowLimit..highLimit) {
            var x = num
            var sum = 0
            while (x > 0) {
                sum += x % 10
                x /= 10
            }
            freq[sum]++
            if (freq[sum] > maxCount) {
                maxCount = freq[sum]
            }
        }
        return maxCount
    }
}
```

## Dart

```dart
class Solution {
  int countBalls(int lowLimit, int highLimit) {
    List<int> cnt = List.filled(46, 0);
    int maxCnt = 0;
    for (int i = lowLimit; i <= highLimit; ++i) {
      int sum = 0;
      int x = i;
      while (x > 0) {
        sum += x % 10;
        x ~/= 10;
      }
      cnt[sum]++;
      if (cnt[sum] > maxCnt) maxCnt = cnt[sum];
    }
    return maxCnt;
  }
}
```

## Golang

```go
func countBalls(lowLimit int, highLimit int) int {
    // Maximum possible digit sum for numbers up to 100000 is 45 (9+9+9+9+9)
    const maxSum = 46
    counts := make([]int, maxSum)

    maxCount := 0
    for num := lowLimit; num <= highLimit; num++ {
        s := 0
        x := num
        for x > 0 {
            s += x % 10
            x /= 10
        }
        counts[s]++
        if counts[s] > maxCount {
            maxCount = counts[s]
        }
    }
    return maxCount
}
```

## Ruby

```ruby
def count_balls(low_limit, high_limit)
  counts = Hash.new(0)
  max_cnt = 0

  (low_limit..high_limit).each do |num|
    sum = 0
    n = num
    while n > 0
      sum += n % 10
      n /= 10
    end
    cnt = counts[sum] + 1
    counts[sum] = cnt
    max_cnt = cnt if cnt > max_cnt
  end

  max_cnt
end
```

## Scala

```scala
object Solution {
    def countBalls(lowLimit: Int, highLimit: Int): Int = {
        val maxSum = 9 * 6
        val counts = new Array[Int](maxSum + 1)
        var i = lowLimit
        while (i <= highLimit) {
            var n = i
            var sum = 0
            while (n > 0) {
                sum += n % 10
                n /= 10
            }
            counts(sum) += 1
            i += 1
        }
        var max = 0
        var idx = 0
        while (idx < counts.length) {
            if (counts(idx) > max) max = counts(idx)
            idx += 1
        }
        max
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_balls(low_limit: i32, high_limit: i32) -> i32 {
        // Maximum possible digit sum for numbers up to 100000 is 45 (9*5)
        let mut counts = vec![0usize; 46];
        let mut max_cnt = 0usize;
        for num in low_limit..=high_limit {
            let mut n = num;
            let mut sum = 0i32;
            while n > 0 {
                sum += n % 10;
                n /= 10;
            }
            let idx = sum as usize;
            counts[idx] += 1;
            if counts[idx] > max_cnt {
                max_cnt = counts[idx];
            }
        }
        max_cnt as i32
    }
}
```

## Racket

```racket
(define/contract (count-balls lowLimit highLimit)
  (-> exact-integer? exact-integer? exact-integer?)
  (let* ((max-sum 200)                     ; sufficient for given constraints
         (counts (make-vector max-sum 0))
         (max-count 0))
    (for ([i (in-range lowLimit (+ highLimit 1))])
      (let ((sum (let loop ((x i) (s 0))
                   (if (= x 0)
                       s
                       (loop (quotient x 10) (+ s (remainder x 10)))))))
        (vector-set! counts sum (+ 1 (vector-ref counts sum)))
        (when (> (vector-ref counts sum) max-count)
          (set! max-count (vector-ref counts sum)))))
    max-count))
```

## Erlang

```erlang
-spec count_balls(LowLimit :: integer(), HighLimit :: integer()) -> integer().
count_balls(LowLimit, HighLimit) ->
    count_balls(LowLimit, HighLimit, #{}, 0).

%% Recursive loop over the range
count_balls(Current, High, _Map, Max) when Current > High ->
    Max;
count_balls(Current, High, Map, Max) ->
    Sum = digit_sum(Current),
    NewCount = maps:get(Sum, Map, 0) + 1,
    NewMap = maps:put(Sum, NewCount, Map),
    NewMax = if NewCount > Max -> NewCount; true -> Max end,
    count_balls(Current + 1, High, NewMap, NewMax).

%% Compute sum of digits
digit_sum(0) ->
    0;
digit_sum(N) when N > 0 ->
    digit_sum(N, 0).

digit_sum(0, Acc) ->
    Acc;
digit_sum(N, Acc) ->
    digit_sum(N div 10, Acc + N rem 10).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_balls(low_limit :: integer, high_limit :: integer) :: integer
  def count_balls(low_limit, high_limit) do
    freq =
      Enum.reduce(low_limit..high_limit, %{}, fn n, acc ->
        s = digit_sum(n)
        Map.update(acc, s, 1, &(&1 + 1))
      end)

    freq
    |> Map.values()
    |> Enum.max(fn -> 0 end)
  end

  defp digit_sum(0), do: 0

  defp digit_sum(n) when n < 10, do: n

  defp digit_sum(n) do
    rem = rem(n, 10)
    div = div(n, 10)
    rem + digit_sum(div)
  end
end
```
