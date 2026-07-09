# 3207. Maximum Points After Enemy Battles

## Cpp

```cpp
class Solution {
public:
    long long maximumPoints(vector<int>& enemyEnergies, int currentEnergy) {
        long long sum = 0;
        for (int e : enemyEnergies) sum += e;
        long long total = sum + currentEnergy;
        long long ans = 0;
        for (int e : enemyEnergies) {
            if (e == 0) continue; // avoid division by zero, though constraints guarantee >=1
            long long points = (total - e) / e;
            if (points > ans) ans = points;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maximumPoints(int[] enemyEnergies, int currentEnergy) {
        long min = Long.MAX_VALUE;
        long sum = 0;
        for (int e : enemyEnergies) {
            sum += e;
            if (e < min) min = e;
        }
        if (currentEnergy < min) return 0L;
        long totalEnergy = currentEnergy + (sum - min);
        return totalEnergy / min;
    }
}
```

## Python

```python
class Solution(object):
    def maximumPoints(self, enemyEnergies, currentEnergy):
        """
        :type enemyEnergies: List[int]
        :type currentEnergy: int
        :rtype: int
        """
        if not enemyEnergies:
            return 0
        min_energy = min(enemyEnergies)
        if currentEnergy < min_energy:
            return 0
        total_energy = currentEnergy + sum(enemyEnergies) - min_energy
        return total_energy // min_energy
```

## Python3

```python
from typing import List

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        if not enemyEnergies:
            return 0
        mn = min(enemyEnergies)
        if currentEnergy < mn:
            return 0
        n = len(enemyEnergies)
        return (currentEnergy // mn) + n - 1
```

## C

```c
long long maximumPoints(int* enemyEnergies, int enemyEnergiesSize, int currentEnergy) {
    if (enemyEnergiesSize == 0) return 0;
    int minVal = enemyEnergies[0];
    for (int i = 1; i < enemyEnergiesSize; ++i) {
        if (enemyEnergies[i] < minVal) minVal = enemyEnergies[i];
    }
    if (currentEnergy < minVal) return 0;
    long long extra = (long long)(currentEnergy - minVal) / minVal;
    return (long long)enemyEnergiesSize + extra;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MaximumPoints(int[] enemyEnergies, int currentEnergy) {
        Array.Sort(enemyEnergies);
        var minHeap = new PriorityQueue<long, long>();
        long cur = currentEnergy;
        long points = 0;
        int i = 0;
        while (true) {
            while (i < enemyEnergies.Length && cur >= enemyEnergies[i]) {
                minHeap.Enqueue(enemyEnergies[i], enemyEnergies[i]);
                points++;
                i++;
            }
            if (i == enemyEnergies.Length) break;
            if (minHeap.Count == 0) break;
            long smallest = minHeap.Dequeue();
            cur += smallest;
        }
        return points;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} enemyEnergies
 * @param {number} currentEnergy
 * @return {number}
 */
var maximumPoints = function(enemyEnergies, currentEnergy) {
    let min = Infinity;
    let sum = 0;
    for (let e of enemyEnergies) {
        sum += e;
        if (e < min) min = e;
    }
    // Energy after marking all enemies except the smallest one
    const totalEnergy = currentEnergy + sum - min;
    return Math.floor(totalEnergy / min);
};
```

## Typescript

```typescript
function maximumPoints(enemyEnergies: number[], currentEnergy: number): number {
    enemyEnergies.sort((a, b) => a - b);
    const min = enemyEnergies[0];
    if (currentEnergy < min) return 0;

    let cnt = 0;
    for (const e of enemyEnergies) {
        if (e <= currentEnergy) cnt++;
        else break;
    }

    const extra = Math.floor(currentEnergy / min);
    if (cnt === 1) return extra;
    return extra + cnt;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $enemyEnergies
     * @param Integer $currentEnergy
     * @return Integer
     */
    function maximumPoints($enemyEnergies, $currentEnergy) {
        $minVal = PHP_INT_MAX;
        $sumAll = 0;
        foreach ($enemyEnergies as $e) {
            $sumAll += $e;
            if ($e < $minVal) {
                $minVal = $e;
            }
        }
        // Add energies of all enemies except one smallest (used for battles)
        $totalEnergy = $currentEnergy + ($sumAll - $minVal);
        // Maximum number of battles with the smallest enemy
        return intdiv($totalEnergy, $minVal);
    }
}
```

## Swift

```swift
class Solution {
    func maximumPoints(_ enemyEnergies: [Int], _ currentEnergy: Int) -> Int {
        guard let minVal = enemyEnergies.min() else { return 0 }
        if currentEnergy < minVal { return 0 }
        var sumAll: Int64 = 0
        for v in enemyEnergies {
            sumAll += Int64(v)
        }
        let total = Int64(currentEnergy) + (sumAll - Int64(minVal))
        let result = total / Int64(minVal)
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumPoints(enemyEnergies: IntArray, currentEnergy: Int): Long {
        if (enemyEnergies.isEmpty()) return 0L
        var minEnergy = Int.MAX_VALUE
        for (e in enemyEnergies) {
            if (e < minEnergy) minEnergy = e
        }
        if (currentEnergy < minEnergy) return 0L
        val n = enemyEnergies.size.toLong()
        val extra = ((currentEnergy - minEnergy).toLong()) / minEnergy.toLong()
        return n + extra
    }
}
```

## Dart

```dart
class Solution {
  int maximumPoints(List<int> enemyEnergies, int currentEnergy) {
    enemyEnergies.sort();
    List<int> maxHeap = [];
    int points = 0;
    int i = 0;
    while (true) {
      while (i < enemyEnergies.length && enemyEnergies[i] <= currentEnergy) {
        points++;
        _heapPush(maxHeap, enemyEnergies[i]);
        i++;
      }
      if (i == enemyEnergies.length) break;
      if (maxHeap.isEmpty) break;
      int largest = _heapPop(maxHeap);
      currentEnergy += largest;
      points--;
    }
    return points;
  }

  void _heapPush(List<int> heap, int val) {
    heap.add(val);
    int idx = heap.length - 1;
    while (idx > 0) {
      int parent = (idx - 1) >> 1;
      if (heap[parent] >= heap[idx]) break;
      int tmp = heap[parent];
      heap[parent] = heap[idx];
      heap[idx] = tmp;
      idx = parent;
    }
  }

  int _heapPop(List<int> heap) {
    int top = heap[0];
    int last = heap.removeLast();
    if (heap.isNotEmpty) {
      heap[0] = last;
      int idx = 0;
      while (true) {
        int left = idx * 2 + 1;
        int right = left + 1;
        if (left >= heap.length) break;
        int largerChild = left;
        if (right < heap.length && heap[right] > heap[left]) {
          largerChild = right;
        }
        if (heap[idx] >= heap[largerChild]) break;
        int tmp = heap[idx];
        heap[idx] = heap[largerChild];
        heap[largerChild] = tmp;
        idx = largerChild;
      }
    }
    return top;
  }
}
```

## Golang

```go
func maximumPoints(enemyEnergies []int, currentEnergy int) int64 {
    var sum int64
    const inf = int64(^uint64(0) >> 1)
    minVal := inf
    for _, v := range enemyEnergies {
        val := int64(v)
        sum += val
        if val < minVal {
            minVal = val
        }
    }
    total := int64(currentEnergy) + sum - minVal
    return total / minVal
}
```

## Ruby

```ruby
def maximum_points(enemy_energies, current_energy)
  return 0 if enemy_energies.empty?
  min_energy = enemy_energies.min
  return 0 if current_energy < min_energy
  (enemy_energies.length - 1) + current_energy / min_energy
end
```

## Scala

```scala
object Solution {
    def maximumPoints(enemyEnergies: Array[Int], currentEnergy: Int): Long = {
        if (enemyEnergies.isEmpty) return 0L
        val minEnergy = enemyEnergies.min
        val n = enemyEnergies.length
        val extraPoints = currentEnergy / minEnergy
        (n - 1).toLong + extraPoints.toLong
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_points(enemy_energies: Vec<i32>, current_energy: i32) -> i64 {
        if enemy_energies.is_empty() {
            return 0;
        }
        let mut min_val = enemy_energies[0] as i64;
        let mut sum: i64 = 0;
        for &e in &enemy_energies {
            let v = e as i64;
            sum += v;
            if v < min_val {
                min_val = v;
            }
        }
        if (current_energy as i64) < min_val {
            return 0;
        }
        let total_energy = current_energy as i64 + (sum - min_val);
        total_energy / min_val
    }
}
```

## Racket

```racket
(define/contract (maximum-points enemyEnergies currentEnergy)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((min-energy (apply min enemyEnergies))
         (total-sum  (apply + enemyEnergies)))
    (if (< currentEnergy min-energy)
        0
        (quotient (+ currentEnergy (- total-sum min-energy)) min-energy))))
```

## Erlang

```erlang
-spec maximum_points(EnemyEnergies :: [integer()], CurrentEnergy :: integer()) -> integer().
maximum_points(EnemyEnergies, CurrentEnergy) ->
    Min = lists:min(EnemyEnergies),
    Sum = lists:foldl(fun(X, Acc) -> X + Acc end, 0, EnemyEnergies),
    Total = CurrentEnergy + (Sum - Min),
    Total div Min.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_points(enemy_energies :: [integer], current_energy :: integer) :: integer
  def maximum_points(enemy_energies, current_energy) do
    min_val = Enum.min(enemy_energies)
    total_sum = Enum.reduce(enemy_energies, 0, &+/2)
    div(current_energy + total_sum - min_val, min_val)
  end
end
```
