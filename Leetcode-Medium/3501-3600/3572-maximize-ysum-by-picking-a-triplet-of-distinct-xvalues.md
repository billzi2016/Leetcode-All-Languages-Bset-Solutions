# 3572. Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values

## Cpp

```cpp
class Solution {
public:
    int maxSumDistinctTriplet(vector<int>& x, vector<int>& y) {
        unordered_map<int,int> best;
        best.reserve(x.size()*2);
        for (size_t i = 0; i < x.size(); ++i) {
            auto it = best.find(x[i]);
            if (it == best.end()) {
                best.emplace(x[i], y[i]);
            } else if (y[i] > it->second) {
                it->second = y[i];
            }
        }
        if (best.size() < 3) return -1;
        vector<int> vals;
        vals.reserve(best.size());
        for (auto &p : best) vals.push_back(p.second);
        sort(vals.begin(), vals.end(), greater<int>());
        return vals[0] + vals[1] + vals[2];
    }
};
```

## Java

```java
class Solution {
    public int maxSumDistinctTriplet(int[] x, int[] y) {
        int n = x.length;
        java.util.HashMap<Integer, Integer> map = new java.util.HashMap<>(n * 2);
        for (int i = 0; i < n; i++) {
            int key = x[i];
            int val = y[i];
            map.merge(key, val, Math::max);
        }
        if (map.size() < 3) return -1;
        int first = 0, second = 0, third = 0;
        for (int v : map.values()) {
            if (v > first) {
                third = second;
                second = first;
                first = v;
            } else if (v > second) {
                third = second;
                second = v;
            } else if (v > third) {
                third = v;
            }
        }
        return first + second + third;
    }
}
```

## Python

```python
class Solution(object):
    def maxSumDistinctTriplet(self, x, y):
        """
        :type x: List[int]
        :type y: List[int]
        :rtype: int
        """
        best = {}
        for xi, yi in zip(x, y):
            if xi not in best or yi > best[xi]:
                best[xi] = yi
        if len(best) < 3:
            return -1
        # get three largest values
        top_three = sorted(best.values(), reverse=True)[:3]
        return sum(top_three)
```

## Python3

```python
class Solution:
    def maxSumDistinctTriplet(self, x, y):
        """
        :type x: List[int]
        :type y: List[int]
        :rtype: int
        """
        best = {}
        for xi, yi in zip(x, y):
            if yi > best.get(xi, -1):
                best[xi] = yi

        if len(best) < 3:
            return -1

        # Get three largest values
        top_vals = sorted(best.values(), reverse=True)[:3]
        return sum(top_vals)
```

## C

```c
int maxSumDistinctTriplet(int* x, int xSize, int* y, int ySize) {
    if (xSize < 3) return -1;
    int maxX = 0;
    for (int i = 0; i < xSize; ++i) {
        if (x[i] > maxX) maxX = x[i];
    }
    int *best = (int *)malloc((maxX + 1) * sizeof(int));
    if (!best) return -1;
    for (int i = 0; i <= maxX; ++i) best[i] = -1;
    for (int i = 0; i < xSize; ++i) {
        int xi = x[i];
        int yi = y[i];
        if (yi > best[xi]) best[xi] = yi;
    }
    int top1 = -1, top2 = -1, top3 = -1;
    for (int v = 0; v <= maxX; ++v) {
        int val = best[v];
        if (val == -1) continue;
        if (val > top1) {
            top3 = top2;
            top2 = top1;
            top1 = val;
        } else if (val > top2) {
            top3 = top2;
            top2 = val;
        } else if (val > top3) {
            top3 = val;
        }
    }
    free(best);
    if (top3 == -1) return -1;
    return top1 + top2 + top3;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSumDistinctTriplet(int[] x, int[] y) {
        var best = new Dictionary<int, int>();
        for (int i = 0; i < x.Length; i++) {
            int key = x[i];
            int val = y[i];
            if (!best.TryGetValue(key, out int cur) || val > cur) {
                best[key] = val;
            }
        }
        if (best.Count < 3) return -1;
        var vals = new List<int>(best.Values);
        vals.Sort((a, b) => b.CompareTo(a));
        return vals[0] + vals[1] + vals[2];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} x
 * @param {number[]} y
 * @return {number}
 */
var maxSumDistinctTriplet = function(x, y) {
    const best = new Map();
    for (let i = 0; i < x.length; ++i) {
        const key = x[i];
        const val = y[i];
        if (!best.has(key) || val > best.get(key)) {
            best.set(key, val);
        }
    }
    const vals = Array.from(best.values());
    if (vals.length < 3) return -1;
    let first = 0, second = 0, third = 0;
    for (const v of vals) {
        if (v > first) {
            third = second;
            second = first;
            first = v;
        } else if (v > second) {
            third = second;
            second = v;
        } else if (v > third) {
            third = v;
        }
    }
    return first + second + third;
};
```

## Typescript

```typescript
function maxSumDistinctTriplet(x: number[], y: number[]): number {
    const best = new Map<number, number>();
    for (let i = 0; i < x.length; i++) {
        const xi = x[i];
        const yi = y[i];
        const cur = best.get(xi);
        if (cur === undefined || yi > cur) best.set(xi, yi);
    }
    const vals = Array.from(best.values());
    if (vals.length < 3) return -1;
    let m1 = 0, m2 = 0, m3 = 0;
    for (const v of vals) {
        if (v > m1) {
            m3 = m2;
            m2 = m1;
            m1 = v;
        } else if (v > m2) {
            m3 = m2;
            m2 = v;
        } else if (v > m3) {
            m3 = v;
        }
    }
    return m1 + m2 + m3;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $x
     * @param Integer[] $y
     * @return Integer
     */
    function maxSumDistinctTriplet($x, $y) {
        $maxByX = [];
        $n = count($x);
        for ($i = 0; $i < $n; ++$i) {
            $xi = $x[$i];
            $yi = $y[$i];
            if (!isset($maxByX[$xi]) || $yi > $maxByX[$xi]) {
                $maxByX[$xi] = $yi;
            }
        }

        if (count($maxByX) < 3) {
            return -1;
        }

        $values = array_values($maxByX);
        rsort($values); // descending order

        return $values[0] + $values[1] + $values[2];
    }
}
```

## Swift

```swift
class Solution {
    func maxSumDistinctTriplet(_ x: [Int], _ y: [Int]) -> Int {
        var bestYForX = [Int:Int]()
        for i in 0..<x.count {
            let key = x[i]
            let value = y[i]
            if let existing = bestYForX[key] {
                if value > existing {
                    bestYForX[key] = value
                }
            } else {
                bestYForX[key] = value
            }
        }
        
        var first = -1, second = -1, third = -1
        for v in bestYForX.values {
            if v > first {
                third = second
                second = first
                first = v
            } else if v > second {
                third = second
                second = v
            } else if v > third {
                third = v
            }
        }
        
        return third == -1 ? -1 : first + second + third
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSumDistinctTriplet(x: IntArray, y: IntArray): Int {
        val bestYForX = HashMap<Int, Int>()
        for (i in x.indices) {
            val xi = x[i]
            val yi = y[i]
            val cur = bestYForX[xi]
            if (cur == null || yi > cur) {
                bestYForX[xi] = yi
            }
        }
        if (bestYForX.size < 3) return -1

        var first = Int.MIN_VALUE
        var second = Int.MIN_VALUE
        var third = Int.MIN_VALUE

        for (value in bestYForX.values) {
            when {
                value > first -> {
                    third = second
                    second = first
                    first = value
                }
                value > second -> {
                    third = second
                    second = value
                }
                value > third -> {
                    third = value
                }
            }
        }
        return first + second + third
    }
}
```

## Dart

```dart
class Solution {
  int maxSumDistinctTriplet(List<int> x, List<int> y) {
    final Map<int, int> best = {};
    for (int i = 0; i < x.length; i++) {
      int xi = x[i];
      int yi = y[i];
      if (!best.containsKey(xi) || yi > best[xi]!) {
        best[xi] = yi;
      }
    }
    if (best.length < 3) return -1;
    List<int> vals = best.values.toList();
    vals.sort((a, b) => b.compareTo(a));
    return vals[0] + vals[1] + vals[2];
  }
}
```

## Golang

```go
func maxSumDistinctTriplet(x []int, y []int) int {
    if len(x) != len(y) || len(x) < 3 {
        return -1
    }
    // map each distinct x to its maximum y
    maxMap := make(map[int]int)
    for i, xv := range x {
        if cur, ok := maxMap[xv]; !ok || y[i] > cur {
            maxMap[xv] = y[i]
        }
    }
    // collect the maximal y values
    vals := make([]int, 0, len(maxMap))
    for _, v := range maxMap {
        vals = append(vals, v)
    }
    if len(vals) < 3 {
        return -1
    }
    // sort descending
    sort.Slice(vals, func(i, j int) bool { return vals[i] > vals[j] })
    return vals[0] + vals[1] + vals[2]
}
```

## Ruby

```ruby
def max_sum_distinct_triplet(x, y)
  best = {}
  x.each_with_index do |val, i|
    cur = y[i]
    if !best.key?(val) || cur > best[val]
      best[val] = cur
    end
  end
  return -1 if best.size < 3
  best.values.max(3).sum
end
```

## Scala

```scala
object Solution {
    def maxSumDistinctTriplet(x: Array[Int], y: Array[Int]): Int = {
        import scala.collection.mutable

        val best = mutable.HashMap[Int, Int]()
        var i = 0
        while (i < x.length) {
            val key = x(i)
            val value = y(i)
            best.get(key) match {
                case Some(prev) => if (value > prev) best.update(key, value)
                case None => best.put(key, value)
            }
            i += 1
        }

        if (best.size < 3) return -1

        var first = Int.MinValue
        var second = Int.MinValue
        var third = Int.MinValue

        for (v <- best.values) {
            if (v > first) {
                third = second
                second = first
                first = v
            } else if (v > second) {
                third = second
                second = v
            } else if (v > third) {
                third = v
            }
        }

        first + second + third
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn max_sum_distinct_triplet(x: Vec<i32>, y: Vec<i32>) -> i32 {
        let mut best: HashMap<i32, i32> = HashMap::new();
        for (xi, yi) in x.into_iter().zip(y.into_iter()) {
            match best.get_mut(&xi) {
                Some(v) => {
                    if yi > *v {
                        *v = yi;
                    }
                }
                None => {
                    best.insert(xi, yi);
                }
            }
        }

        let mut vals: Vec<i32> = best.into_values().collect();
        if vals.len() < 3 {
            return -1;
        }
        vals.sort_unstable_by(|a, b| b.cmp(a));
        vals[0] + vals[1] + vals[2]
    }
}
```

## Racket

```racket
(define/contract (max-sum-distinct-triplet x y)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let ((h (make-hash)))
    (for ([xi (in-list x)] [yi (in-list y)])
      (let ((prev (hash-ref h xi #f)))
        (when (or (not prev) (> yi prev))
          (hash-set! h xi yi))))
    (define vals (hash-values h))
    (if (< (length vals) 3)
        -1
        (let* ((sorted (sort vals >))
               (top3 (take sorted 3)))
          (+ (first top3) (second top3) (third top3))))))
```

## Erlang

```erlang
-spec max_sum_distinct_triplet(X :: [integer()], Y :: [integer()]) -> integer().
max_sum_distinct_triplet(X, Y) ->
    Map = build_map(X, Y, #{}),
    Values = maps:values(Map),
    case length(Values) >= 3 of
        true ->
            Sorted = lists:sort(fun(A, B) -> A > B end, Values),
            [A, B, C | _] = Sorted,
            A + B + C;
        false ->
            -1
    end.

build_map([], [], Map) ->
    Map;
build_map([Xh | Xt], [Yh | Yt], Map) ->
    NewMap =
        case maps:find(Xh, Map) of
            {ok, Prev} when Yh > Prev -> maps:put(Xh, Yh, Map);
            {ok, _Prev} -> Map;
            error -> maps:put(Xh, Yh, Map)
        end,
    build_map(Xt, Yt, NewMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sum_distinct_triplet(x :: [integer], y :: [integer]) :: integer
  def max_sum_distinct_triplet(x, y) do
    # Keep the maximum y for each distinct x
    max_map =
      Enum.zip(x, y)
      |> Enum.reduce(%{}, fn {xi, yi}, acc ->
        Map.update(acc, xi, yi, fn existing -> if yi > existing, do: yi, else: existing end)
      end)

    values = Map.values(max_map)

    if length(values) < 3 do
      -1
    else
      values
      |> Enum.sort(:desc)
      |> Enum.take(3)
      |> Enum.sum()
    end
  end
end
```
