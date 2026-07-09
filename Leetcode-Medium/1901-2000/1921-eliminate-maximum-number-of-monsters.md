# 1921. Eliminate Maximum Number of Monsters

## Cpp

```cpp
class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        int n = dist.size();
        vector<long long> arrival;
        arrival.reserve(n);
        for (int i = 0; i < n; ++i) {
            long long t = (static_cast<long long>(dist[i]) + speed[i] - 1) / speed[i];
            arrival.push_back(t);
        }
        sort(arrival.begin(), arrival.end());
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (arrival[i] <= i) break;
            ++ans;
        }
        return ans;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int eliminateMaximum(int[] dist, int[] speed) {
        int n = dist.length;
        long[] deadline = new long[n];
        for (int i = 0; i < n; i++) {
            deadline[i] = (dist[i] - 1L) / speed[i]; // latest minute we can shoot this monster
        }
        Arrays.sort(deadline);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (deadline[i] < i) break;
            ans++;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        deadlines = [(d - 1) // s for d, s in zip(dist, speed)]
        deadlines.sort()
        ans = 0
        for i, t in enumerate(deadlines):
            if t < i:
                break
            ans += 1
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        deadlines = [(d - 1) // s for d, s in zip(dist, speed)]
        deadlines.sort()
        ans = 0
        for i, dl in enumerate(deadlines):
            if dl < i:
                break
            ans += 1
        return ans
```

## C

```c
#include <stdlib.h>

static int cmpInt(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int eliminateMaximum(int* dist, int distSize, int* speed, int speedSize){
    int n = distSize;
    int *deadline = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        // maximum whole minutes we can wait before this monster reaches the city
        deadline[i] = (dist[i] - 1) / speed[i];
    }
    qsort(deadline, n, sizeof(int), cmpInt);
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        if (deadline[i] < i) break;
        ++ans;
    }
    free(deadline);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int EliminateMaximum(int[] dist, int[] speed)
    {
        int n = dist.Length;
        double[] arrival = new double[n];
        for (int i = 0; i < n; i++)
        {
            arrival[i] = (double)dist[i] / speed[i];
        }
        Array.Sort(arrival);
        int eliminated = 0;
        for (int i = 0; i < n; i++)
        {
            if (arrival[i] <= i)
                break;
            eliminated++;
        }
        return eliminated;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} dist
 * @param {number[]} speed
 * @return {number}
 */
var eliminateMaximum = function(dist, speed) {
    const n = dist.length;
    const arrival = new Array(n);
    for (let i = 0; i < n; ++i) {
        // ceil(dist[i] / speed[i]) without floating point
        arrival[i] = Math.floor((dist[i] + speed[i] - 1) / speed[i]);
    }
    arrival.sort((a, b) => a - b);
    let eliminated = 0;
    for (let i = 0; i < n; ++i) {
        if (arrival[i] <= i) break;
        eliminated++;
    }
    return eliminated;
};
```

## Typescript

```typescript
function eliminateMaximum(dist: number[], speed: number[]): number {
    const n = dist.length;
    const deadlines: number[] = new Array(n);
    for (let i = 0; i < n; i++) {
        deadlines[i] = Math.floor((dist[i] - 1) / speed[i]);
    }
    deadlines.sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (deadlines[i] < i) break;
        ans++;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $dist
     * @param Integer[] $speed
     * @return Integer
     */
    function eliminateMaximum($dist, $speed) {
        $n = count($dist);
        $times = [];
        for ($i = 0; $i < $n; ++$i) {
            // ceil(dist / speed)
            $times[] = intdiv($dist[$i] + $speed[$i] - 1, $speed[$i]);
        }
        sort($times);
        $ans = 0;
        foreach ($times as $t) {
            if ($t <= $ans) {
                break;
            }
            ++$ans;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func eliminateMaximum(_ dist: [Int], _ speed: [Int]) -> Int {
        let n = dist.count
        var deadlines = [Int]()
        deadlines.reserveCapacity(n)
        for i in 0..<n {
            let time = (dist[i] + speed[i] - 1) / speed[i] // ceiling of dist/speed
            deadlines.append(time)
        }
        deadlines.sort()
        var eliminated = 0
        for (i, deadline) in deadlines.enumerated() {
            if deadline <= i { break }
            eliminated += 1
        }
        return eliminated
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun eliminateMaximum(dist: IntArray, speed: IntArray): Int {
        val n = dist.size
        val times = DoubleArray(n)
        for (i in 0 until n) {
            times[i] = dist[i].toDouble() / speed[i]
        }
        times.sort()
        var eliminated = 0
        while (eliminated < n && times[eliminated] > eliminated.toDouble()) {
            eliminated++
        }
        return eliminated
    }
}
```

## Dart

```dart
class Solution {
  int eliminateMaximum(List<int> dist, List<int> speed) {
    int n = dist.length;
    List<int> arrival = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      arrival[i] = ((dist[i] + speed[i] - 1) ~/ speed[i]);
    }
    arrival.sort();
    int ans = 0;
    for (int i = 0; i < n; i++) {
      if (arrival[i] <= i) break;
      ans++;
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func eliminateMaximum(dist []int, speed []int) int {
    n := len(dist)
    deadlines := make([]int, n)
    for i := 0; i < n; i++ {
        deadlines[i] = (dist[i] - 1) / speed[i]
    }
    sort.Ints(deadlines)

    ans := 0
    for i, d := range deadlines {
        if d < i {
            break
        }
        ans++
    }
    return ans
}
```

## Ruby

```ruby
def eliminate_maximum(dist, speed)
  times = dist.zip(speed).map { |d, s| (d + s - 1) / s }
  times.sort!
  ans = 0
  times.each_with_index do |t, i|
    break if t <= i
    ans += 1
  end
  ans
end
```

## Scala

```scala
object Solution {
  def eliminateMaximum(dist: Array[Int], speed: Array[Int]): Int = {
    val n = dist.length
    val times = new Array[Double](n)
    var i = 0
    while (i < n) {
      times(i) = dist(i).toDouble / speed(i)
      i += 1
    }
    java.util.Arrays.sort(times)
    var eliminated = 0
    while (eliminated < n && times(eliminated) > eliminated) {
      eliminated += 1
    }
    eliminated
  }
}
```

## Rust

```rust
impl Solution {
    pub fn eliminate_maximum(dist: Vec<i32>, speed: Vec<i32>) -> i32 {
        let n = dist.len();
        let mut times = Vec::with_capacity(n);
        for i in 0..n {
            // ceiling of dist[i] / speed[i]
            let t = (dist[i] + speed[i] - 1) / speed[i];
            times.push(t);
        }
        times.sort_unstable();

        let mut ans = 0;
        for (i, &t) in times.iter().enumerate() {
            if t <= i as i32 {
                break;
            }
            ans += 1;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (eliminate-maximum dist speed)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((arrival (map / dist speed))
         (sorted (sort arrival <)))
    (let loop ((lst sorted) (i 0))
      (cond
        [(null? lst) i]
        [(<= (car lst) i) i]
        [else (loop (cdr lst) (+ i 1))]))))
```

## Erlang

```erlang
-spec eliminate_maximum(Dist :: [integer()], Speed :: [integer()]) -> integer().
eliminate_maximum(Dist, Speed) ->
    Deadlines = lists:map(
        fun({D, S}) -> (D + S - 1) div S end,
        lists:zip(Dist, Speed)
    ),
    Sorted = lists:sort(Deadlines),
    count_kills(Sorted, 0).

-spec count_kills([integer()], integer()) -> integer().
count_kills([], _Idx) ->
    0;
count_kills([D | Rest], Idx) ->
    case D =< Idx of
        true -> 0;
        false -> 1 + count_kills(Rest, Idx + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec eliminate_maximum(dist :: [integer], speed :: [integer]) :: integer
  def eliminate_maximum(dist, speed) do
    arrivals =
      Enum.zip(dist, speed)
      |> Enum.map(fn {d, s} -> d / s end)
      |> Enum.sort()

    Enum.reduce_while(Enum.with_index(arrivals), 0, fn {time, idx}, cnt ->
      if time <= idx do
        {:halt, cnt}
      else
        {:cont, cnt + 1}
      end
    end)
  end
end
```
