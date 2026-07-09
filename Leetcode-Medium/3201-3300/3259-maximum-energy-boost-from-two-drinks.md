# 3259. Maximum Energy Boost From Two Drinks

## Cpp

```cpp
class Solution {
public:
    long long maxEnergyBoost(vector<int>& energyDrinkA, vector<int>& energyDrinkB) {
        int n = energyDrinkA.size();
        vector<long long> dpA(n), dpB(n);
        dpA[0] = energyDrinkA[0];
        dpB[0] = energyDrinkB[0];
        if (n == 1) return max(dpA[0], dpB[0]);
        dpA[1] = dpA[0] + energyDrinkA[1];
        dpB[1] = dpB[0] + energyDrinkB[1];
        for (int i = 2; i < n; ++i) {
            long long fromA = dpA[i-1];
            long long fromB = dpB[i-2];
            dpA[i] = max(fromA, fromB) + energyDrinkA[i];
            
            long long fromB2 = dpB[i-1];
            long long fromA2 = dpA[i-2];
            dpB[i] = max(fromB2, fromA2) + energyDrinkB[i];
        }
        return max(dpA[n-1], dpB[n-1]);
    }
};
```

## Java

```java
class Solution {
    public long maxEnergyBoost(int[] energyDrinkA, int[] energyDrinkB) {
        int n = energyDrinkA.length;
        if (n == 0) return 0L;
        long aPrev2 = 0, bPrev2 = 0;
        long aPrev1 = energyDrinkA[0];
        long bPrev1 = energyDrinkB[0];
        long ans = Math.max(aPrev1, bPrev1);
        if (n == 1) return ans;

        // i = 1
        long aCurr = Math.max(aPrev1, 0L) + energyDrinkA[1];
        long bCurr = Math.max(bPrev1, 0L) + energyDrinkB[1];
        ans = Math.max(ans, Math.max(aCurr, bCurr));

        // shift for next iteration
        aPrev2 = aPrev1;
        aPrev1 = aCurr;
        bPrev2 = bPrev1;
        bPrev1 = bCurr;

        for (int i = 2; i < n; i++) {
            aCurr = Math.max(aPrev1, bPrev2) + energyDrinkA[i];
            bCurr = Math.max(bPrev1, aPrev2) + energyDrinkB[i];
            ans = Math.max(ans, Math.max(aCurr, bCurr));

            // shift
            aPrev2 = aPrev1;
            aPrev1 = aCurr;
            bPrev2 = bPrev1;
            bPrev1 = bCurr;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxEnergyBoost(self, energyDrinkA, energyDrinkB):
        """
        :type energyDrinkA: List[int]
        :type energyDrinkB: List[int]
        :rtype: int
        """
        n = len(energyDrinkA)
        if n == 0:
            return 0
        dpA = [0] * n
        dpB = [0] * n
        for i in range(n):
            a = energyDrinkA[i]
            b = energyDrinkB[i]
            if i == 0:
                dpA[0] = a
                dpB[0] = b
            else:
                prevA = dpA[i - 1]
                prevB = dpB[i - 1]
                twoBackA = dpA[i - 2] if i >= 2 else 0
                twoBackB = dpB[i - 2] if i >= 2 else 0
                dpA[i] = max(prevA, twoBackB) + a
                dpB[i] = max(prevB, twoBackA) + b
        return max(dpA[-1], dpB[-1])
```

## Python3

```python
class Solution:
    def maxEnergyBoost(self, energyDrinkA, energyDrinkB):
        n = len(energyDrinkA)
        if n == 0:
            return 0
        dpA = [0] * n
        dpB = [0] * n

        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]

        if n >= 2:
            dpA[1] = max(dpA[0], 0) + energyDrinkA[1]
            dpB[1] = max(dpB[0], 0) + energyDrinkB[1]

        for i in range(2, n):
            dpA[i] = max(dpA[i - 1], dpB[i - 2]) + energyDrinkA[i]
            dpB[i] = max(dpB[i - 1], dpA[i - 2]) + energyDrinkB[i]

        return max(dpA[-1], dpB[-1])
```

## C

```c
long long maxEnergyBoost(int* energyDrinkA, int energyDrinkASize, int* energyDrinkB, int energyDrinkBSize) {
    int n = energyDrinkASize;
    if (n == 0) return 0LL;

    long long *dpA = (long long *)malloc(sizeof(long long) * n);
    long long *dpB = (long long *)malloc(sizeof(long long) * n);

    dpA[0] = (long long)energyDrinkA[0];
    dpB[0] = (long long)energyDrinkB[0];

    if (n > 1) {
        dpA[1] = dpA[0] + (long long)energyDrinkA[1];
        dpB[1] = dpB[0] + (long long)energyDrinkB[1];
    }

    for (int i = 2; i < n; ++i) {
        long long bestPrevA = dpA[i - 1] > dpB[i - 2] ? dpA[i - 1] : dpB[i - 2];
        long long bestPrevB = dpB[i - 1] > dpA[i - 2] ? dpB[i - 1] : dpA[i - 2];
        dpA[i] = bestPrevA + (long long)energyDrinkA[i];
        dpB[i] = bestPrevB + (long long)energyDrinkB[i];
    }

    long long result = dpA[n - 1] > dpB[n - 1] ? dpA[n - 1] : dpB[n - 1];

    free(dpA);
    free(dpB);
    return result;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public long MaxEnergyBoost(int[] energyDrinkA, int[] energyDrinkB) {
        int n = energyDrinkA.Length;
        if (n == 0) return 0L;

        long dpAPrev = energyDrinkA[0];
        long dpBPrev = energyDrinkB[0];
        long dpAPrev2 = 0L;
        long dpBPrev2 = 0L;

        for (int i = 1; i < n; i++) {
            long curA = Math.Max(dpAPrev, dpBPrev2) + energyDrinkA[i];
            long curB = Math.Max(dpBPrev, dpAPrev2) + energyDrinkB[i];

            dpAPrev2 = dpAPrev;
            dpBPrev2 = dpBPrev;
            dpAPrev = curA;
            dpBPrev = curB;
        }

        return Math.Max(dpAPrev, dpBPrev);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} energyDrinkA
 * @param {number[]} energyDrinkB
 * @return {number}
 */
var maxEnergyBoost = function(energyDrinkA, energyDrinkB) {
    const n = energyDrinkA.length;
    if (n === 0) return 0;

    const dpA = new Array(n);
    const dpB = new Array(n);

    dpA[0] = energyDrinkA[0];
    dpB[0] = energyDrinkB[0];
    let ans = Math.max(dpA[0], dpB[0]);

    if (n > 1) {
        dpA[1] = Math.max(dpA[0], 0) + energyDrinkA[1];
        dpB[1] = Math.max(dpB[0], 0) + energyDrinkB[1];
        ans = Math.max(ans, dpA[1], dpB[1]);
    }

    for (let i = 2; i < n; ++i) {
        dpA[i] = Math.max(dpA[i - 1], dpB[i - 2]) + energyDrinkA[i];
        dpB[i] = Math.max(dpB[i - 1], dpA[i - 2]) + energyDrinkB[i];
        ans = Math.max(ans, dpA[i], dpB[i]);
    }

    return ans;
};
```

## Typescript

```typescript
function maxEnergyBoost(energyDrinkA: number[], energyDrinkB: number[]): number {
    const n = energyDrinkA.length;
    if (n === 0) return 0;

    // dp for hour 0
    let prevA = energyDrinkA[0];
    let prevB = energyDrinkB[0];

    if (n === 1) return Math.max(prevA, prevB);

    // dp for hour 1
    let curA = Math.max(prevA, 0) + energyDrinkA[1];
    let curB = Math.max(prevB, 0) + energyDrinkB[1];

    if (n === 2) return Math.max(curA, curB);

    // keep dp values for i-2
    let prevPrevA = prevA;
    let prevPrevB = prevB;

    // iterate from hour 2 onward
    for (let i = 2; i < n; i++) {
        const nextA = Math.max(curA, prevPrevB) + energyDrinkA[i];
        const nextB = Math.max(curB, prevPrevA) + energyDrinkB[i];

        // shift windows
        prevPrevA = curA;
        prevPrevB = curB;
        curA = nextA;
        curB = nextB;
    }

    return Math.max(curA, curB);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $energyDrinkA
     * @param Integer[] $energyDrinkB
     * @return Integer
     */
    function maxEnergyBoost($energyDrinkA, $energyDrinkB) {
        $n = count($energyDrinkA);
        if ($n == 0) return 0;

        $dpA = array_fill(0, $n, 0);
        $dpB = array_fill(0, $n, 0);

        $dpA[0] = $energyDrinkA[0];
        $dpB[0] = $energyDrinkB[0];

        if ($n > 1) {
            $dpA[1] = max($dpA[0], 0) + $energyDrinkA[1];
            $dpB[1] = max($dpB[0], 0) + $energyDrinkB[1];
        }

        for ($i = 2; $i < $n; $i++) {
            $dpA[$i] = max($dpA[$i - 1], $dpB[$i - 2]) + $energyDrinkA[$i];
            $dpB[$i] = max($dpB[$i - 1], $dpA[$i - 2]) + $energyDrinkB[$i];
        }

        return max($dpA[$n - 1], $dpB[$n - 1]);
    }
}
```

## Swift

```swift
class Solution {
    func maxEnergyBoost(_ energyDrinkA: [Int], _ energyDrinkB: [Int]) -> Int {
        let n = energyDrinkA.count
        if n == 0 { return 0 }
        var dpA = Array(repeating: 0, count: n)
        var dpB = Array(repeating: 0, count: n)
        
        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]
        
        if n > 1 {
            dpA[1] = max(dpA[0], 0) + energyDrinkA[1]
            dpB[1] = max(dpB[0], 0) + energyDrinkB[1]
        }
        
        if n > 2 {
            for i in 2..<n {
                dpA[i] = max(dpA[i - 1], dpB[i - 2]) + energyDrinkA[i]
                dpB[i] = max(dpB[i - 1], dpA[i - 2]) + energyDrinkB[i]
            }
        }
        
        return max(dpA[n - 1], dpB[n - 1])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxEnergyBoost(energyDrinkA: IntArray, energyDrinkB: IntArray): Long {
        val n = energyDrinkA.size
        if (n == 0) return 0L
        var dpAPrev2 = 0L          // dpA[i-2]
        var dpBPrev2 = 0L          // dpB[i-2]
        var dpAPrev1 = energyDrinkA[0].toLong()   // dpA[i-1] for i=0
        var dpBPrev1 = energyDrinkB[0].toLong()   // dpB[i-1] for i=0

        for (i in 1 until n) {
            val curA = maxOf(dpAPrev1, dpBPrev2) + energyDrinkA[i].toLong()
            val curB = maxOf(dpBPrev1, dpAPrev2) + energyDrinkB[i].toLong()

            dpAPrev2 = dpAPrev1
            dpBPrev2 = dpBPrev1
            dpAPrev1 = curA
            dpBPrev1 = curB
        }
        return maxOf(dpAPrev1, dpBPrev1)
    }
}
```

## Dart

```dart
class Solution {
  int maxEnergyBoost(List<int> energyDrinkA, List<int> energyDrinkB) {
    int n = energyDrinkA.length;
    if (n == 0) return 0;
    int dpA_i_2 = 0;
    int dpB_i_2 = 0;
    int dpA_i_1 = energyDrinkA[0];
    int dpB_i_1 = energyDrinkB[0];

    for (int i = 1; i < n; ++i) {
      int curA = ((dpA_i_1 > dpB_i_2) ? dpA_i_1 : dpB_i_2) + energyDrinkA[i];
      int curB = ((dpB_i_1 > dpA_i_2) ? dpB_i_1 : dpA_i_2) + energyDrinkB[i];

      dpA_i_2 = dpA_i_1;
      dpB_i_2 = dpB_i_1;
      dpA_i_1 = curA;
      dpB_i_1 = curB;
    }

    return (dpA_i_1 > dpB_i_1) ? dpA_i_1 : dpB_i_1;
  }
}
```

## Golang

```go
func maxEnergyBoost(energyDrinkA []int, energyDrinkB []int) int64 {
    n := len(energyDrinkA)
    if n == 0 {
        return 0
    }
    dpA := make([]int64, n)
    dpB := make([]int64, n)

    dpA[0] = int64(energyDrinkA[0])
    dpB[0] = int64(energyDrinkB[0])

    for i := 1; i < n; i++ {
        // Compute dpA[i]
        bestPrevA := dpA[i-1]
        if i >= 2 && dpB[i-2] > bestPrevA {
            bestPrevA = dpB[i-2]
        }
        dpA[i] = bestPrevA + int64(energyDrinkA[i])

        // Compute dpB[i]
        bestPrevB := dpB[i-1]
        if i >= 2 && dpA[i-2] > bestPrevB {
            bestPrevB = dpA[i-2]
        }
        dpB[i] = bestPrevB + int64(energyDrinkB[i])
    }

    if dpA[n-1] > dpB[n-1] {
        return dpA[n-1]
    }
    return dpB[n-1]
}
```

## Ruby

```ruby
def max_energy_boost(energy_drink_a, energy_drink_b)
  n = energy_drink_a.length
  return 0 if n == 0

  dp_a = Array.new(n, 0)
  dp_b = Array.new(n, 0)

  dp_a[0] = energy_drink_a[0]
  dp_b[0] = energy_drink_b[0]

  (1...n).each do |i|
    best_prev_a = dp_a[i - 1]
    best_gap_from_b = i >= 2 ? dp_b[i - 2] : 0
    dp_a[i] = [best_prev_a, best_gap_from_b].max + energy_drink_a[i]

    best_prev_b = dp_b[i - 1]
    best_gap_from_a = i >= 2 ? dp_a[i - 2] : 0
    dp_b[i] = [best_prev_b, best_gap_from_a].max + energy_drink_b[i]
  end

  [dp_a[n - 1], dp_b[n - 1]].max
end
```

## Scala

```scala
object Solution {
    def maxEnergyBoost(energyDrinkA: Array[Int], energyDrinkB: Array[Int]): Long = {
        val n = energyDrinkA.length
        if (n == 0) return 0L

        val dpA = new Array[Long](n)
        val dpB = new Array[Long](n)

        dpA(0) = energyDrinkA(0).toLong
        dpB(0) = energyDrinkB(0).toLong

        if (n > 1) {
            dpA(1) = Math.max(dpA(0), 0L) + energyDrinkA(1)
            dpB(1) = Math.max(dpB(0), 0L) + energyDrinkB(1)
        }

        var i = 2
        while (i < n) {
            val bestPrevA = Math.max(dpA(i - 1), dpB(i - 2))
            dpA(i) = bestPrevA + energyDrinkA(i)

            val bestPrevB = Math.max(dpB(i - 1), dpA(i - 2))
            dpB(i) = bestPrevB + energyDrinkB(i)

            i += 1
        }

        Math.max(dpA(n - 1), dpB(n - 1))
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_energy_boost(energy_drink_a: Vec<i32>, energy_drink_b: Vec<i32>) -> i64 {
        let n = energy_drink_a.len();
        if n == 0 {
            return 0;
        }
        // dp values for i-2 and i-1
        let mut a_prev2: i64 = 0;
        let mut b_prev2: i64 = 0;
        let mut a_prev: i64 = 0;
        let mut b_prev: i64 = 0;

        for i in 0..n {
            let a = energy_drink_a[i] as i64;
            let b = energy_drink_b[i] as i64;

            let cur_a = if i == 0 {
                a
            } else if i == 1 {
                (a_prev + a).max(a)
            } else {
                (a_prev + a).max(b_prev2 + a).max(a)
            };

            let cur_b = if i == 0 {
                b
            } else if i == 1 {
                (b_prev + b).max(b)
            } else {
                (b_prev + b).max(a_prev2 + b).max(b)
            };

            // shift for next iteration
            a_prev2 = a_prev;
            b_prev2 = b_prev;
            a_prev = cur_a;
            b_prev = cur_b;
        }

        a_prev.max(b_prev)
    }
}
```

## Racket

```racket
(define/contract (max-energy-boost energyDrinkA energyDrinkB)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length energyDrinkA))
         (vecA (list->vector energyDrinkA))
         (vecB (list->vector energyDrinkB)))
    (if (= n 0)
        0
        (let loop ((i 1)
                   (a-prev (vector-ref vecA 0))
                   (b-prev (vector-ref vecB 0))
                   (a-prev2 0)
                   (b-prev2 0))
          (if (= i n)
              (max a-prev b-prev)
              (let* ((a-curr (+ (max a-prev b-prev2) (vector-ref vecA i)))
                     (b-curr (+ (max b-prev a-prev2) (vector-ref vecB i))))
                (loop (+ i 1) a-curr b-curr a-prev b-prev)))))))
```

## Erlang

```erlang
-module(solution).
-export([max_energy_boost/2]).

-spec max_energy_boost(EnergyDrinkA :: [integer()], EnergyDrinkB :: [integer()]) -> integer().
max_energy_boost(EnergyDrinkA, EnergyDrinkB) ->
    case {EnergyDrinkA, EnergyDrinkB} of
        {[HA|TA], [HB|TB]} ->
            DP_A0 = HA,
            DP_B0 = HB,
            loop(TA, TB, 1, DP_A0, DP_B0, 0, 0);
        _ -> 0
    end.

loop([], [], _Idx, PrevA, PrevB, _Prev2A, _Prev2B) ->
    erlang:max(PrevA, PrevB);
loop([HA|TA], [HB|TB], Idx, PrevA, PrevB, Prev2A, Prev2B) ->
    case Idx of
        1 ->
            DP_A = erlang:max(PrevA, 0) + HA,
            DP_B = erlang:max(PrevB, 0) + HB;
        _ ->
            DP_A = erlang:max(PrevA, Prev2B) + HA,
            DP_B = erlang:max(PrevB, Prev2A) + HB
    end,
    loop(TA, TB, Idx + 1, DP_A, DP_B, PrevA, PrevB).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_energy_boost(energy_drink_a :: [integer], energy_drink_b :: [integer]) :: integer
  def max_energy_boost(energy_drink_a, energy_drink_b) do
    {last_a, last_b, _prev2_a, _prev2_b} =
      Enum.with_index(Enum.zip(energy_drink_a, energy_drink_b))
      |> Enum.reduce({0, 0, 0, 0}, fn
        {{a_val, b_val}, 0}, _acc ->
          {a_val, b_val, 0, 0}

        {{a_val, b_val}, 1}, {prev_a, prev_b, _prev2_a, _prev2_b} ->
          dp_a = max(prev_a, 0) + a_val
          dp_b = max(prev_b, 0) + b_val
          {dp_a, dp_b, prev_a, prev_b}

        {{a_val, b_val}, _i}, {prev_a, prev_b, prev2_a, prev2_b} ->
          dp_a = max(prev_a, prev2_b) + a_val
          dp_b = max(prev_b, prev2_a) + b_val
          {dp_a, dp_b, prev_a, prev_b}
      end)

    max(last_a, last_b)
  end
end
```
