# 3096. Minimum Levels to Gain More Points

## Cpp

```cpp
class Solution {
public:
    int minimumLevels(vector<int>& possible) {
        int n = possible.size();
        int total = 0;
        for (int v : possible) {
            total += (v == 1 ? 1 : -1);
        }
        int pref = 0;
        for (int i = 0; i < n - 1; ++i) { // Alice must leave at least one level for Bob
            pref += (possible[i] == 1 ? 1 : -1);
            if (pref * 2 > total) {
                return i + 1;
            }
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int minimumLevels(int[] possible) {
        int n = possible.length;
        int total = 0;
        for (int p : possible) {
            total += (p == 1 ? 1 : -1);
        }
        int prefix = 0;
        // Alice must leave at least one level for Bob
        for (int i = 0; i < n - 1; i++) {
            prefix += (possible[i] == 1 ? 1 : -1);
            if (2L * prefix > total) { // use long to avoid overflow, though not needed here
                return i + 1;
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def minimumLevels(self, possible):
        """
        :type possible: List[int]
        :rtype: int
        """
        n = len(possible)
        total = 0
        # compute total sum with 1 -> +1, 0 -> -1
        for v in possible:
            total += 1 if v == 1 else -1

        pref = 0
        for i in range(n - 1):  # Alice must leave at least one level for Bob
            pref += 1 if possible[i] == 1 else -1
            if 2 * pref > total:
                return i + 1
        return -1
```

## Python3

```python
class Solution:
    def minimumLevels(self, possible):
        n = len(possible)
        # Convert 0 to -1 and compute total sum
        total = 0
        for v in possible:
            total += 1 if v == 1 else -1

        pref = 0
        for i in range(n - 1):  # Alice must leave at least one level for Bob
            pref += 1 if possible[i] == 1 else -1
            if 2 * pref > total:
                return i + 1  # levels are counted from 1
        return -1
```

## C

```c
int minimumLevels(int* possible, int possibleSize) {
    int total = 0;
    for (int i = 0; i < possibleSize; ++i) {
        total += possible[i] ? 1 : -1;
    }
    int prefix = 0;
    for (int i = 0; i < possibleSize - 1; ++i) {
        prefix += possible[i] ? 1 : -1;
        if (prefix * 2 > total) {
            return i + 1;
        }
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumLevels(int[] possible)
    {
        int n = possible.Length;
        long total = 0;
        foreach (int v in possible)
            total += v == 1 ? 1 : -1;

        long prefix = 0;
        for (int i = 0; i < n - 1; i++)
        {
            prefix += possible[i] == 1 ? 1 : -1;
            if (2 * prefix > total)
                return i + 1;
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} possible
 * @return {number}
 */
var minimumLevels = function(possible) {
    const n = possible.length;
    let total = 0;
    for (let i = 0; i < n; ++i) {
        total += possible[i] === 1 ? 1 : -1;
    }
    let pref = 0;
    for (let i = 0; i < n - 1; ++i) {
        pref += possible[i] === 1 ? 1 : -1;
        if (2 * pref > total) return i + 1;
    }
    return -1;
};
```

## Typescript

```typescript
function minimumLevels(possible: number[]): number {
    const n = possible.length;
    let total = 0;
    for (let i = 0; i < n; ++i) {
        total += possible[i] === 1 ? 1 : -1;
    }
    let pref = 0;
    for (let k = 1; k <= n - 1; ++k) {
        pref += possible[k - 1] === 1 ? 1 : -1;
        if (2 * pref > total) return k;
    }
    return -1;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $possible
     * @return Integer
     */
    function minimumLevels($possible) {
        $n = count($possible);
        $total = 0;
        foreach ($possible as $v) {
            $total += ($v == 1) ? 1 : -1;
        }
        $pref = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            $pref += ($possible[$i] == 1) ? 1 : -1;
            if (2 * $pref > $total) {
                return $i + 1;
            }
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func minimumLevels(_ possible: [Int]) -> Int {
        let n = possible.count
        var total = 0
        for v in possible {
            total += (v == 1 ? 1 : -1)
        }
        var prefix = 0
        for i in 0..<(n - 1) {
            prefix += (possible[i] == 1 ? 1 : -1)
            if prefix * 2 > total {
                return i + 1
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumLevels(possible: IntArray): Int {
        var total = 0
        for (v in possible) {
            total += if (v == 1) 1 else -1
        }
        var pref = 0
        val n = possible.size
        for (i in 0 until n - 1) { // Alice must leave at least one level for Bob
            pref += if (possible[i] == 1) 1 else -1
            if (pref * 2 > total) {
                return i + 1
            }
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int minimumLevels(List<int> possible) {
    int n = possible.length;
    int total = 0;
    List<int> arr = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      int val = possible[i] == 1 ? 1 : -1;
      arr[i] = val;
      total += val;
    }
    int pref = 0;
    for (int l = 1; l <= n - 1; l++) {
      pref += arr[l - 1];
      if (2 * pref > total) return l;
    }
    return -1;
  }
}
```

## Golang

```go
func minimumLevels(possible []int) int {
    n := len(possible)
    total := 0
    vals := make([]int, n)
    for i, v := range possible {
        if v == 0 {
            vals[i] = -1
        } else {
            vals[i] = 1
        }
        total += vals[i]
    }

    pref := 0
    for i := 0; i < n-1; i++ { // ensure Bob gets at least one level
        pref += vals[i]
        if 2*pref > total {
            return i + 1
        }
    }
    return -1
}
```

## Ruby

```ruby
def minimum_levels(possible)
  vals = possible.map { |v| v == 1 ? 1 : -1 }
  total = vals.sum
  prefix = 0
  (0...possible.length - 1).each do |i|
    prefix += vals[i]
    return i + 1 if prefix * 2 > total
  end
  -1
end
```

## Scala

```scala
object Solution {
    def minimumLevels(possible: Array[Int]): Int = {
        val n = possible.length
        var total = 0
        for (v <- possible) {
            total += (if (v == 1) 1 else -1)
        }
        var pref = 0
        for (i <- 0 until n - 1) {
            pref += (if (possible(i) == 1) 1 else -1)
            if (pref * 2 > total) return i + 1
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_levels(possible: Vec<i32>) -> i32 {
        let n = possible.len();
        // Compute total sum where 0 becomes -1 and 1 stays 1
        let mut total: i64 = 0;
        for &p in &possible {
            total += if p == 1 { 1 } else { -1 };
        }
        let mut prefix: i64 = 0;
        // Alice must play at least one level and leave at least one for Bob
        for i in 0..n - 1 {
            prefix += if possible[i] == 1 { 1 } else { -1 };
            // Condition: prefix > (total - prefix)  <=> 2*prefix > total
            if prefix * 2 > total {
                return (i + 1) as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (minimum-levels possible)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length possible))
         (converted (map (lambda (x) (if (= x 0) -1 1)) possible))
         (total (apply + converted)))
    (let loop ((lst converted) (idx 0) (pref 0))
      (if (>= idx (- n 1))
          -1
          (let* ((new-pref (+ pref (car lst)))
                 (k (+ idx 1)))
            (if (> (* 2 new-pref) total)
                k
                (loop (cdr lst) k new-pref)))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_levels/1]).

minimum_levels(Possible) ->
    Total = lists:foldl(fun(X, Acc) -> (if X == 1 -> 1; true -> -1 end) + Acc end, 0, Possible),
    find_k(Possible, Total, 0, 0).

find_k([H|T], Total, Index, Prefix) ->
    NewPrefix = Prefix + (if H == 1 -> 1; true -> -1 end),
    case {2 * NewPrefix > Total, T} of
        {true, [_|_]} -> Index + 1;
        _ -> find_k(T, Total, Index + 1, NewPrefix)
    end;
find_k([], _, _, _) ->
    -1.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_levels(possible :: [integer]) :: integer
  def minimum_levels(possible) do
    n = length(possible)

    total =
      Enum.reduce(possible, 0, fn v, acc ->
        acc + if(v == 1, do: 1, else: -1)
      end)

    {found_k, _} =
      Enum.reduce_while(Enum.with_index(possible), {nil, 0}, fn {v, idx}, {_k, pref} ->
        # stop before the last level so Bob gets at least one level
        if idx == n - 1 do
          {:halt, {nil, pref}}
        else
          new_pref = pref + if(v == 1, do: 1, else: -1)
          k = idx + 1

          if new_pref * 2 > total do
            {:halt, {k, new_pref}}
          else
            {:cont, {nil, new_pref}}
          end
        end
      end)

    case found_k do
      nil -> -1
      k -> k
    end
  end
end
```
