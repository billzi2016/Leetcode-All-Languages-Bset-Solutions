# 3147. Taking Maximum Energy From the Mystic Dungeon

## Cpp

```cpp
class Solution {
public:
    int maximumEnergy(vector<int>& energy, int k) {
        int n = energy.size();
        vector<int> dp(n);
        int ans = INT_MIN;
        for (int i = n - 1; i >= 0; --i) {
            if (i + k < n) dp[i] = energy[i] + dp[i + k];
            else dp[i] = energy[i];
            ans = max(ans, dp[i]);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumEnergy(int[] energy, int k) {
        int n = energy.length;
        int[] dp = new int[n];
        int max = Integer.MIN_VALUE;
        for (int i = n - 1; i >= 0; --i) {
            if (i + k < n) {
                dp[i] = energy[i] + dp[i + k];
            } else {
                dp[i] = energy[i];
            }
            if (dp[i] > max) {
                max = dp[i];
            }
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(energy)
        dp = [0] * n
        max_energy = -10**9  # sufficiently small
        
        for i in range(n - 1, -1, -1):
            if i + k < n:
                dp[i] = energy[i] + dp[i + k]
            else:
                dp[i] = energy[i]
            if dp[i] > max_energy:
                max_energy = dp[i]
                
        return max_energy
```

## Python3

```python
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        max_energy = -10**9  # sufficiently small
        
        for i in range(n - 1, -1, -1):
            nxt = i + k
            if nxt < n:
                dp[i] = energy[i] + dp[nxt]
            else:
                dp[i] = energy[i]
            if dp[i] > max_energy:
                max_energy = dp[i]
                
        return max_energy
```

## C

```c
#include <limits.h>

int maximumEnergy(int* energy, int energySize, int k) {
    int maxEnergy = INT_MIN;
    for (int i = energySize - 1; i >= 0; --i) {
        long long sum = energy[i];
        if (i + k < energySize) {
            sum += energy[i + k]; // energy[i+k] already holds dp value
        }
        energy[i] = (int)sum;
        if (energy[i] > maxEnergy) {
            maxEnergy = energy[i];
        }
    }
    return maxEnergy;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumEnergy(int[] energy, int k) {
        int n = energy.Length;
        int max = int.MinValue;
        for (int i = n - 1; i >= 0; --i) {
            if (i + k < n) {
                energy[i] += energy[i + k];
            }
            if (energy[i] > max) max = energy[i];
        }
        return max;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} energy
 * @param {number} k
 * @return {number}
 */
var maximumEnergy = function(energy, k) {
    const n = energy.length;
    const dp = new Array(n);
    let maxVal = -Infinity;
    for (let i = n - 1; i >= 0; --i) {
        if (i + k < n) {
            dp[i] = energy[i] + dp[i + k];
        } else {
            dp[i] = energy[i];
        }
        if (dp[i] > maxVal) maxVal = dp[i];
    }
    return maxVal;
};
```

## Typescript

```typescript
function maximumEnergy(energy: number[], k: number): number {
    const n = energy.length;
    const dp = new Array<number>(n);
    let maxEnergy = -Infinity;
    for (let i = n - 1; i >= 0; --i) {
        const nextIdx = i + k;
        const sum = energy[i] + (nextIdx < n ? dp[nextIdx] : 0);
        dp[i] = sum;
        if (sum > maxEnergy) maxEnergy = sum;
    }
    return maxEnergy;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $energy
     * @param Integer $k
     * @return Integer
     */
    function maximumEnergy($energy, $k) {
        $n = count($energy);
        $dp = $energy;
        $max = PHP_INT_MIN;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($i + $k < $n) {
                $dp[$i] += $dp[$i + $k];
            }
            if ($dp[$i] > $max) {
                $max = $dp[$i];
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maximumEnergy(_ energy: [Int], _ k: Int) -> Int {
        let n = energy.count
        var dp = energy
        var maxVal = Int.min
        for i in stride(from: n - 1, through: 0, by: -1) {
            if i + k < n {
                dp[i] += dp[i + k]
            }
            if dp[i] > maxVal {
                maxVal = dp[i]
            }
        }
        return maxVal
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumEnergy(energy: IntArray, k: Int): Int {
        val n = energy.size
        val dp = IntArray(n)
        var maxSum = Int.MIN_VALUE
        for (i in n - 1 downTo 0) {
            val next = i + k
            dp[i] = if (next < n) energy[i] + dp[next] else energy[i]
            if (dp[i] > maxSum) maxSum = dp[i]
        }
        return maxSum
    }
}
```

## Dart

```dart
class Solution {
  int maximumEnergy(List<int> energy, int k) {
    int n = energy.length;
    List<int> dp = List.filled(n, 0);
    int ans = -(1 << 60);
    for (int i = n - 1; i >= 0; --i) {
      int next = (i + k < n) ? dp[i + k] : 0;
      dp[i] = energy[i] + next;
      if (dp[i] > ans) ans = dp[i];
    }
    return ans;
  }
}
```

## Golang

```go
func maximumEnergy(energy []int, k int) int {
    n := len(energy)
    dp := make([]int, n)
    const negInf = -1 << 60
    maxVal := negInf
    for i := n - 1; i >= 0; i-- {
        if i+k < n {
            dp[i] = energy[i] + dp[i+k]
        } else {
            dp[i] = energy[i]
        }
        if dp[i] > maxVal {
            maxVal = dp[i]
        }
    }
    return maxVal
}
```

## Ruby

```ruby
def maximum_energy(energy, k)
  n = energy.length
  dp = Array.new(n, 0)
  max_sum = -1 << 60
  (n - 1).downto(0) do |i|
    if i + k < n
      dp[i] = energy[i] + dp[i + k]
    else
      dp[i] = energy[i]
    end
    max_sum = dp[i] if dp[i] > max_sum
  end
  max_sum
end
```

## Scala

```scala
object Solution {
    def maximumEnergy(energy: Array[Int], k: Int): Int = {
        val n = energy.length
        val dp = new Array[Int](n)
        var maxVal = Int.MinValue
        for (i <- (n - 1) to 0 by -1) {
            var sum = energy(i)
            if (i + k < n) sum += dp(i + k)
            dp(i) = sum
            if (sum > maxVal) maxVal = sum
        }
        maxVal
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_energy(mut energy: Vec<i32>, k: i32) -> i32 {
        let n = energy.len();
        let step = k as usize;
        let mut best = i32::MIN;
        for i in (0..n).rev() {
            if i + step < n {
                energy[i] += energy[i + step];
            }
            if energy[i] > best {
                best = energy[i];
            }
        }
        best
    }
}
```

## Racket

```racket
(define/contract (maximum-energy energy k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([v (list->vector energy)]
         [n (vector-length v)])
    (let ([dp (make-vector n)])
      (define max-sum #f)
      (for ([i (in-range (- n 1) -1 -1)])
        (let* ([next (+ i k)]
               [sum (if (< next n)
                        (+ (vector-ref v i) (vector-ref dp next))
                        (vector-ref v i))])
          (vector-set! dp i sum)
          (when (or (not max-sum) (> sum max-sum))
            (set! max-sum sum))))
      max-sum)))
```

## Erlang

```erlang
-spec maximum_energy(Energy :: [integer()], K :: integer()) -> integer().
maximum_energy(Energy, K) ->
    N = length(Energy),
    EnerTuple = list_to_tuple(Energy),
    Max0 = -1000000000,
    max_over_remainders(K, 0, N, EnerTuple, Max0).

max_over_remainders(K, Rem, N, EnerTuple, Max) when Rem < K ->
    if
        Rem >= N ->
            max_over_remainders(K, Rem + 1, N, EnerTuple, Max);
        true ->
            Last = last_index(Rem, N, K),
            {NewMax, _} = process_chain(Last, Rem, K, EnerTuple, Max, 0),
            max_over_remainders(K, Rem + 1, N, EnerTuple, NewMax)
    end;
max_over_remainders(_K, _Rem, _N, _EnerTuple, Max) ->
    Max.

process_chain(Idx, Rem, K, EnerTuple, MaxSoFar, SumSoFar) when Idx >= Rem ->
    Val = element(Idx + 1, EnerTuple),
    NewSum = Val + SumSoFar,
    NewMax = if NewSum > MaxSoFar -> NewSum; true -> MaxSoFar end,
    process_chain(Idx - K, Rem, K, EnerTuple, NewMax, NewSum);
process_chain(_Idx, _Rem, _K, _EnerTuple, Max, _Sum) ->
    {Max, ok}.

last_index(Rem, N, K) ->
    R = (N - 1 - Rem) rem K,
    N - 1 - R.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_energy(energy :: [integer], k :: integer) :: integer
  def maximum_energy(energy, k) do
    n = length(energy)
    arr = List.to_tuple(energy)
    dp = :array.new(n, default: 0)
    init_max = -1_000_000_000

    {_final_dp, max_sum} =
      Enum.reduce(:lists.seq(n - 1, 0, -1), {dp, init_max}, fn i, {dp_acc, cur_max} ->
        val = elem(arr, i)

        sum =
          if i + k < n do
            val + :array.get(i + k, dp_acc)
          else
            val
          end

        new_dp = :array.set(i, sum, dp_acc)
        new_max = if sum > cur_max, do: sum, else: cur_max
        {new_dp, new_max}
      end)

    max_sum
  end
end
```
