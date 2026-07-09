# 2275. Largest Combination With Bitwise AND Greater Than Zero

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        const int BITS = 24; // sufficient for values up to 1e7
        int cnt[BITS] = {0};
        for (int x : candidates) {
            for (int b = 0; b < BITS; ++b) {
                if (x & (1 << b)) ++cnt[b];
            }
        }
        int ans = 0;
        for (int i = 0; i < BITS; ++i) ans = max(ans, cnt[i]);
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int largestCombination(int[] candidates) {
        int[] bitCount = new int[31]; // enough for values up to 2^30
        for (int num : candidates) {
            for (int i = 0; i < 31; i++) {
                if (((num >> i) & 1) == 1) {
                    bitCount[i]++;
                }
            }
        }
        int max = 0;
        for (int cnt : bitCount) {
            if (cnt > max) {
                max = cnt;
            }
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        # Since candidates[i] <= 10^7 < 2^24, we only need to consider bits 0..23.
        bit_counts = [0] * 24
        for num in candidates:
            # Count set bits for this number.
            i = 0
            while num:
                if num & 1:
                    bit_counts[i] += 1
                num >>= 1
                i += 1
        return max(bit_counts)
```

## Python3

```python
from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # Since candidates[i] <= 10^7 < 2^24, we need at most 24 bits.
        bit_counts = [0] * 24
        for num in candidates:
            # Count set bits for each position
            i = 0
            while num:
                if num & 1:
                    bit_counts[i] += 1
                num >>= 1
                i += 1
        return max(bit_counts)
```

## C

```c
int largestCombination(int* candidates, int candidatesSize) {
    int maxCount = 0;
    for (int bit = 0; bit < 24; ++bit) {
        int cnt = 0;
        for (int i = 0; i < candidatesSize; ++i) {
            if ((candidates[i] >> bit) & 1)
                ++cnt;
        }
        if (cnt > maxCount)
            maxCount = cnt;
    }
    return maxCount;
}
```

## Csharp

```csharp
public class Solution
{
    public int LargestCombination(int[] candidates)
    {
        // Since candidates[i] ≤ 10^7 < 2^24, checking bits 0..23 is sufficient.
        const int MAX_BITS = 24;
        int[] bitCount = new int[MAX_BITS];

        foreach (int num in candidates)
        {
            for (int b = 0; b < MAX_BITS; ++b)
            {
                if ((num & (1 << b)) != 0)
                    bitCount[b]++;
            }
        }

        int max = 0;
        for (int i = 0; i < MAX_BITS; ++i)
        {
            if (bitCount[i] > max) max = bitCount[i];
        }
        return max;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} candidates
 * @return {number}
 */
var largestCombination = function(candidates) {
    const BIT_LIMIT = 24; // numbers ≤ 10^7 fit in 24 bits
    let maxCount = 0;
    for (let b = 0; b < BIT_LIMIT; ++b) {
        const mask = 1 << b;
        let cnt = 0;
        for (const num of candidates) {
            if (num & mask) ++cnt;
        }
        if (cnt > maxCount) maxCount = cnt;
    }
    return maxCount;
};
```

## Typescript

```typescript
function largestCombination(candidates: number[]): number {
    const BIT_LIMIT = 24; // numbers ≤ 10^7 fit in 24 bits
    const counts = new Array(BIT_LIMIT).fill(0);
    
    for (const num of candidates) {
        for (let i = 0; i < BIT_LIMIT; ++i) {
            if ((num & (1 << i)) !== 0) {
                counts[i]++;
            }
        }
    }
    
    let maxCount = 0;
    for (let i = 0; i < BIT_LIMIT; ++i) {
        if (counts[i] > maxCount) maxCount = counts[i];
    }
    return maxCount;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $candidates
     * @return Integer
     */
    function largestCombination($candidates) {
        $max = 0;
        // Since candidates[i] <= 10^7 (< 2^24), checking up to bit 30 is safe.
        for ($bit = 0; $bit < 31; $bit++) {
            $cnt = 0;
            foreach ($candidates as $num) {
                if (($num >> $bit) & 1) {
                    $cnt++;
                }
            }
            if ($cnt > $max) {
                $max = $cnt;
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func largestCombination(_ candidates: [Int]) -> Int {
        var bitCounts = [Int](repeating: 0, count: 24)
        for num in candidates {
            var value = num
            var idx = 0
            while value > 0 && idx < 24 {
                if (value & 1) == 1 {
                    bitCounts[idx] += 1
                }
                value >>= 1
                idx += 1
            }
        }
        return bitCounts.max()!
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestCombination(candidates: IntArray): Int {
        var maxCount = 0
        for (bit in 0 until 24) {
            val mask = 1 shl bit
            var count = 0
            for (num in candidates) {
                if ((num and mask) != 0) {
                    count++
                }
            }
            if (count > maxCount) {
                maxCount = count
            }
        }
        return maxCount
    }
}
```

## Dart

```dart
class Solution {
  int largestCombination(List<int> candidates) {
    const int BITS = 24;
    List<int> bitCount = List.filled(BITS, 0);
    for (int num in candidates) {
      for (int i = 0; i < BITS; ++i) {
        if ((num & (1 << i)) != 0) {
          bitCount[i]++;
        }
      }
    }
    int maxCnt = 0;
    for (int cnt in bitCount) {
      if (cnt > maxCnt) maxCnt = cnt;
    }
    return maxCnt;
  }
}
```

## Golang

```go
func largestCombination(candidates []int) int {
    maxCount := 0
    for i := 0; i < 24; i++ {
        mask := 1 << i
        count := 0
        for _, v := range candidates {
            if v&mask != 0 {
                count++
            }
        }
        if count > maxCount {
            maxCount = count
        }
    }
    return maxCount
}
```

## Ruby

```ruby
def largest_combination(candidates)
  # Since candidates[i] <= 10^7, we need at most 24 bits.
  bit_counts = Array.new(32, 0)

  candidates.each do |num|
    i = 0
    while num > 0
      if (num & 1) == 1
        bit_counts[i] += 1
      end
      num >>= 1
      i += 1
    end
  end

  bit_counts.max || 0
end
```

## Scala

```scala
object Solution {
    def largestCombination(candidates: Array[Int]): Int = {
        var maxCount = 0
        // Since candidates[i] <= 10^7, we need at most 24 bits (0 to 23)
        for (bit <- 0 until 24) {
            var count = 0
            var i = 0
            while (i < candidates.length) {
                if (((candidates(i) >> bit) & 1) == 1) count += 1
                i += 1
            }
            if (count > maxCount) maxCount = count
        }
        maxCount
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_combination(candidates: Vec<i32>) -> i32 {
        let mut max_cnt = 0;
        for bit in 0..24 {
            let mask = 1 << bit;
            let mut cnt = 0;
            for &num in candidates.iter() {
                if num & mask != 0 {
                    cnt += 1;
                }
            }
            if cnt > max_cnt {
                max_cnt = cnt;
            }
        }
        max_cnt as i32
    }
}
```

## Racket

```racket
(require racket/contract
         racket/bitwise)

(define/contract (largest-combination candidates)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((bit 0) (best 0))
    (if (> bit 23)
        best
        (let ((cnt (foldl (lambda (num acc)
                           (if (zero? (bitwise-and num (arithmetic-shift 1 bit)))
                               acc
                               (+ acc 1)))
                         0 candidates)))
          (loop (+ bit 1) (max best cnt))))))
```

## Erlang

```erlang
-module(solution).
-export([largest_combination/1]).

-spec largest_combination(Candidates :: [integer()]) -> integer().
largest_combination(Candidates) ->
    MaxBits = 24,
    lists:max([count_bit(Candidates, Bit) || Bit <- lists:seq(0, MaxBits - 1)]).

count_bit(Candidates, Bit) ->
    Mask = 1 bsl Bit,
    lists:foldl(fun(N, Acc) ->
        if (N band Mask) =/= 0 -> Acc + 1;
           true -> Acc
        end
    end, 0, Candidates).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec largest_combination(candidates :: [integer]) :: integer
  def largest_combination(candidates) do
    0..23
    |> Enum.reduce(0, fn bit, best ->
      mask = 1 <<< bit
      count = Enum.count(candidates, fn x -> (x &&& mask) != 0 end)
      if count > best, do: count, else: best
    end)
  end
end
```
