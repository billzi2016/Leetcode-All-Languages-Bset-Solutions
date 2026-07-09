# 3502. Minimum Cost to Reach Every Position

## Cpp

```cpp
class Solution {
public:
    vector<int> minCosts(vector<int>& cost) {
        int n = cost.size();
        vector<int> answer(n);
        int curMin = INT_MAX;
        for (int i = 0; i < n; ++i) {
            curMin = min(curMin, cost[i]);
            answer[i] = curMin;
        }
        return answer;
    }
};
```

## Java

```java
class Solution {
    public int[] minCosts(int[] cost) {
        int n = cost.length;
        int[] answer = new int[n];
        int minSoFar = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (cost[i] < minSoFar) {
                minSoFar = cost[i];
            }
            answer[i] = minSoFar;
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def minCosts(self, cost):
        """
        :type cost: List[int]
        :rtype: List[int]
        """
        ans = []
        cur_min = float('inf')
        for c in cost:
            if c < cur_min:
                cur_min = c
            ans.append(cur_min)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = []
        cur_min = float('inf')
        for c in cost:
            if c < cur_min:
                cur_min = c
            ans.append(cur_min)
        return ans
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minCosts(int* cost, int costSize, int* returnSize) {
    int *ans = (int*)malloc(sizeof(int) * costSize);
    if (!ans) {
        *returnSize = 0;
        return NULL;
    }
    int curMin = 101; // since cost[i] <= 100
    for (int i = 0; i < costSize; ++i) {
        if (cost[i] < curMin) curMin = cost[i];
        ans[i] = curMin;
    }
    *returnSize = costSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] MinCosts(int[] cost) {
        int n = cost.Length;
        int[] answer = new int[n];
        int curMin = int.MaxValue;
        for (int i = 0; i < n; i++) {
            if (cost[i] < curMin) curMin = cost[i];
            answer[i] = curMin;
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} cost
 * @return {number[]}
 */
var minCosts = function(cost) {
    const n = cost.length;
    const answer = new Array(n);
    let curMin = Infinity;
    for (let i = 0; i < n; i++) {
        if (cost[i] < curMin) curMin = cost[i];
        answer[i] = curMin;
    }
    return answer;
};
```

## Typescript

```typescript
function minCosts(cost: number[]): number[] {
    const answer: number[] = [];
    let minSoFar = Infinity;
    for (const c of cost) {
        if (c < minSoFar) minSoFar = c;
        answer.push(minSoFar);
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $cost
     * @return Integer[]
     */
    function minCosts($cost) {
        $ans = [];
        $min = PHP_INT_MAX;
        foreach ($cost as $c) {
            if ($c < $min) {
                $min = $c;
            }
            $ans[] = $min;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minCosts(_ cost: [Int]) -> [Int] {
        var result = [Int]()
        var currentMin = Int.max
        for c in cost {
            if c < currentMin { currentMin = c }
            result.append(currentMin)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCosts(cost: IntArray): IntArray {
        val n = cost.size
        val answer = IntArray(n)
        var minSoFar = Int.MAX_VALUE
        for (i in 0 until n) {
            if (cost[i] < minSoFar) minSoFar = cost[i]
            answer[i] = minSoFar
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> minCosts(List<int> cost) {
    int n = cost.length;
    List<int> answer = List.filled(n, 0);
    int curMin = cost[0];
    answer[0] = curMin;
    for (int i = 1; i < n; i++) {
      if (cost[i] < curMin) curMin = cost[i];
      answer[i] = curMin;
    }
    return answer;
  }
}
```

## Golang

```go
func minCosts(cost []int) []int {
    n := len(cost)
    if n == 0 {
        return []int{}
    }
    ans := make([]int, n)
    cur := cost[0]
    ans[0] = cur
    for i := 1; i < n; i++ {
        if cost[i] < cur {
            cur = cost[i]
        }
        ans[i] = cur
    }
    return ans
}
```

## Ruby

```ruby
def min_costs(cost)
  result = []
  min_val = Float::INFINITY
  cost.each do |c|
    min_val = c if c < min_val
    result << min_val
  end
  result
end
```

## Scala

```scala
object Solution {
    def minCosts(cost: Array[Int]): Array[Int] = {
        val n = cost.length
        val answer = new Array[Int](n)
        var curMin = Int.MaxValue
        var i = 0
        while (i < n) {
            if (cost(i) < curMin) curMin = cost(i)
            answer(i) = curMin
            i += 1
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_costs(cost: Vec<i32>) -> Vec<i32> {
        let mut ans = Vec::with_capacity(cost.len());
        let mut cur_min = i32::MAX;
        for &c in cost.iter() {
            if c < cur_min {
                cur_min = c;
            }
            ans.push(cur_min);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-costs cost)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let loop ((lst cost) (cur-min #f) (acc '()))
    (if (null? lst)
        (reverse acc)
        (let* ((c (car lst))
               (new-min (if cur-min (min cur-min c) c)))
          (loop (cdr lst) new-min (cons new-min acc))))))
```

## Erlang

```erlang
-spec min_costs(Cost :: [integer()]) -> [integer()].
min_costs(Cost) ->
    min_costs(Cost, []).

min_costs([], Acc) ->
    lists:reverse(Acc);
min_costs([H|T], []) ->
    min_costs(T, [H]);
min_costs([H|T], [Prev|_]=Acc) ->
    Min = if H < Prev -> H; true -> Prev end,
    min_costs(T, [Min|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_costs(cost :: [integer]) :: [integer]
  def min_costs(cost) do
    {ans, _} = Enum.map_reduce(cost, :infinity, fn c, acc ->
      new_min = if acc == :infinity or c < acc, do: c, else: acc
      {new_min, new_min}
    end)

    ans
  end
end
```
