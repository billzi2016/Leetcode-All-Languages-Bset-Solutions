# 2028. Find Missing Observations

## Cpp

```cpp
class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        long long m = rolls.size();
        long long totalSum = 1LL * mean * (n + m);
        long long knownSum = 0;
        for (int v : rolls) knownSum += v;
        long long remaining = totalSum - knownSum;
        if (remaining < n || remaining > 6LL * n) return {};
        long long base = remaining / n;
        int extra = remaining % n;
        vector<int> ans(n, static_cast<int>(base));
        for (int i = 0; i < extra; ++i) {
            ++ans[i];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] missingRolls(int[] rolls, int mean, int n) {
        long totalObservations = (long) rolls.length + n;
        long requiredSum = totalObservations * mean;
        long knownSum = 0;
        for (int v : rolls) knownSum += v;
        long remaining = requiredSum - knownSum;
        if (remaining < n || remaining > 6L * n) {
            return new int[0];
        }
        int[] ans = new int[n];
        // start with all 1s
        for (int i = 0; i < n; i++) ans[i] = 1;
        long extra = remaining - n; // amount to distribute over the base 1s
        int idx = 0;
        while (extra > 0) {
            int add = (int) Math.min(5, extra);
            ans[idx++] += add;
            extra -= add;
            if (idx == n) idx = 0; // continue cycling if needed (though not necessary)
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)
        total_needed = mean * (n + m)
        current_sum = sum(rolls)
        remaining = total_needed - current_sum

        if remaining < n or remaining > 6 * n:
            return []

        base = remaining // n
        extra = remaining % n

        result = [base] * n
        for i in range(extra):
            result[i] += 1

        return result
```

## Python3

```python
from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_needed = mean * (n + m)
        current_sum = sum(rolls)
        remaining = total_needed - current_sum

        if remaining < n or remaining > 6 * n:
            return []

        base = remaining // n
        extra = remaining % n

        result = [base] * n
        for i in range(extra):
            result[i] += 1

        return result
```

## C

```c
#include <stdlib.h>

int* missingRolls(int* rolls, int rollsSize, int mean, int n, int* returnSize) {
    long long sum = 0;
    for (int i = 0; i < rollsSize; ++i) {
        sum += rolls[i];
    }
    
    long long total = (long long)mean * (n + rollsSize);
    long long remaining = total - sum;
    
    if (remaining < n || remaining > 6LL * n) {
        *returnSize = 0;
        return NULL;
    }
    
    int* ans = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i) {
        ans[i] = 1;
    }
    
    long long extra = remaining - n; // distribute this over the rolls
    for (int i = 0; i < n && extra > 0; ++i) {
        int add = (extra > 5) ? 5 : (int)extra;
        ans[i] += add;
        extra -= add;
    }
    
    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] MissingRolls(int[] rolls, int mean, int n) {
        long m = rolls.Length;
        long totalSum = (long)mean * (m + n);
        long knownSum = 0;
        foreach (int v in rolls) knownSum += v;
        long remaining = totalSum - knownSum;
        if (remaining < n || remaining > 6L * n) {
            return new int[0];
        }
        int[] result = new int[n];
        for (int i = 0; i < n; i++) result[i] = 1;
        long extra = remaining - n; // each element already has 1
        int idx = 0;
        while (extra > 0) {
            int add = (int)Math.Min(5, extra);
            result[idx++] += add;
            extra -= add;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} rolls
 * @param {number} mean
 * @param {number} n
 * @return {number[]}
 */
var missingRolls = function(rolls, mean, n) {
    const m = rolls.length;
    let sumKnown = 0;
    for (let i = 0; i < m; ++i) {
        sumKnown += rolls[i];
    }
    const totalNeeded = mean * (m + n);
    const remaining = totalNeeded - sumKnown;
    
    if (remaining < n || remaining > 6 * n) {
        return [];
    }
    
    const base = Math.floor(remaining / n);
    let extra = remaining % n;
    const result = new Array(n).fill(base);
    for (let i = 0; i < extra; ++i) {
        result[i] += 1;
    }
    return result;
};
```

## Typescript

```typescript
function missingRolls(rolls: number[], mean: number, n: number): number[] {
    const m = rolls.length;
    let sum = 0;
    for (const v of rolls) sum += v;
    const total = mean * (m + n);
    const remain = total - sum;
    if (remain < n || remain > 6 * n) return [];
    const base = Math.floor(remain / n);
    let extra = remain % n;
    const res = new Array(n).fill(base);
    for (let i = 0; i < extra; i++) {
        res[i] += 1;
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $rolls
     * @param Integer $mean
     * @param Integer $n
     * @return Integer[]
     */
    function missingRolls($rolls, $mean, $n) {
        $m = count($rolls);
        $sumKnown = 0;
        foreach ($rolls as $v) {
            $sumKnown += $v;
        }
        $totalSum = $mean * ($m + $n);
        $remaining = $totalSum - $sumKnown;

        if ($remaining < $n || $remaining > 6 * $n) {
            return [];
        }

        $base = intdiv($remaining, $n);
        $extra = $remaining % $n;

        $result = array_fill(0, $n, $base);
        for ($i = 0; $i < $extra; $i++) {
            $result[$i] += 1;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func missingRolls(_ rolls: [Int], _ mean: Int, _ n: Int) -> [Int] {
        let m = rolls.count
        var sum = 0
        for v in rolls { sum += v }
        let total = mean * (n + m)
        let remaining = total - sum
        if remaining < n || remaining > 6 * n {
            return []
        }
        let base = remaining / n
        let extra = remaining % n
        var result = Array(repeating: base, count: n)
        for i in 0..<extra {
            result[i] += 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun missingRolls(rolls: IntArray, mean: Int, n: Int): IntArray {
        val m = rolls.size
        var sum = 0L
        for (v in rolls) sum += v
        val total = mean.toLong() * (n + m)
        val remaining = total - sum
        if (remaining < n || remaining > 6L * n) return intArrayOf()
        val res = IntArray(n) { 1 }
        var extra = (remaining - n).toInt()
        var i = 0
        while (extra > 0 && i < n) {
            val add = if (extra >= 5) 5 else extra
            res[i] += add
            extra -= add
            i++
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> missingRolls(List<int> rolls, int mean, int n) {
    int m = rolls.length;
    int totalSum = mean * (m + n);
    int knownSum = 0;
    for (int v in rolls) {
      knownSum += v;
    }
    int remaining = totalSum - knownSum;
    if (remaining < n || remaining > 6 * n) {
      return [];
    }
    int base = remaining ~/ n;
    int extra = remaining % n;
    List<int> res = List.filled(n, base);
    for (int i = 0; i < extra; ++i) {
      res[i] += 1;
    }
    return res;
  }
}
```

## Golang

```go
func missingRolls(rolls []int, mean int, n int) []int {
    total := int64(mean) * int64(len(rolls)+n)
    var sum int64
    for _, v := range rolls {
        sum += int64(v)
    }
    remaining := total - sum
    if remaining < int64(n) || remaining > int64(6*n) {
        return []int{}
    }
    base := int(remaining / int64(n))
    extra := int(remaining % int64(n))
    res := make([]int, n)
    for i := 0; i < n; i++ {
        res[i] = base
        if i < extra {
            res[i]++
        }
    }
    return res
}
```

## Ruby

```ruby
# @param {Integer[]} rolls
# @param {Integer} mean
# @param {Integer} n
# @return {Integer[]}
def missing_rolls(rolls, mean, n)
  m = rolls.length
  total_needed = mean * (n + m)
  current_sum = rolls.sum
  remaining = total_needed - current_sum

  return [] if remaining < n || remaining > 6 * n

  base = remaining / n
  extra = remaining % n

  result = Array.new(n, base)
  extra.times { |i| result[i] += 1 }
  result
end
```

## Scala

```scala
object Solution {
    def missingRolls(rolls: Array[Int], mean: Int, n: Int): Array[Int] = {
        val m = rolls.length
        val totalSum = mean.toLong * (n + m)
        var knownSum = 0L
        var i = 0
        while (i < m) {
            knownSum += rolls(i).toLong
            i += 1
        }
        val remaining = totalSum - knownSum
        if (remaining < n || remaining > 6L * n) return Array.emptyIntArray

        val base = (remaining / n).toInt
        val extra = (remaining % n).toInt
        val res = Array.fill(n)(base)
        var j = 0
        while (j < extra) {
            res(j) += 1
            j += 1
        }
        res
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn missing_rolls(rolls: Vec<i32>, mean: i32, n: i32) -> Vec<i32> {
        let m = rolls.len() as i64;
        let n_i64 = n as i64;
        let total_len = m + n_i64;
        let target_sum = mean as i64 * total_len;
        let known_sum: i64 = rolls.iter().map(|&x| x as i64).sum();
        let remaining = target_sum - known_sum;

        if remaining < n_i64 || remaining > 6 * n_i64 {
            return Vec::new();
        }

        let base = (remaining / n_i64) as i32;
        let extra = (remaining % n_i64) as usize;
        let mut ans = vec![base; n as usize];
        for i in 0..extra {
            ans[i] += 1;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (missing-rolls rolls mean n)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  (let* ((m (length rolls))
         (total (* mean (+ n m)))
         (known (foldl + 0 rolls))
         (remaining (- total known)))
    (if (or (< remaining n) (> remaining (* 6 n)))
        '()
        (let* ((base (quotient remaining n))
               (extra (remainder remaining n)))
          (append (make-list extra (+ base 1))
                  (make-list (- n extra) base))))))
```

## Erlang

```erlang
-spec missing_rolls(Rolls :: [integer()], Mean :: integer(), N :: integer()) -> [integer()].
missing_rolls(Rolls, Mean, N) ->
    SumRolls = lists:sum(Rolls),
    M = length(Rolls),
    Total = Mean * (N + M),
    Remaining = Total - SumRolls,
    if
        Remaining >= N, Remaining =< 6 * N ->
            Base = Remaining div N,
            Extra = Remaining rem N,
            [Base + (if I =< Extra -> 1; true -> 0 end) || I <- lists:seq(1, N)];
        true ->
            []
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec missing_rolls(rolls :: [integer], mean :: integer, n :: integer) :: [integer]
  def missing_rolls(rolls, mean, n) do
    m = length(rolls)
    total_len = m + n
    required_total = mean * total_len
    sum_known = Enum.sum(rolls)
    missing_sum = required_total - sum_known

    if missing_sum < n or missing_sum > 6 * n do
      []
    else
      base = div(missing_sum, n)
      extra = rem(missing_sum, n)

      Enum.map(0..(n - 1), fn i ->
        base + if i < extra, do: 1, else: 0
      end)
    end
  end
end
```
