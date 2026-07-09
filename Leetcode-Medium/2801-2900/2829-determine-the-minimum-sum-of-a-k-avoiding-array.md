# 2829. Determine the Minimum Sum of a k-avoiding Array

## Cpp

```cpp
class Solution {
public:
    int minimumSum(int n, int k) {
        std::unordered_set<int> used;
        int cnt = 0;
        int sum = 0;
        for (int i = 1; cnt < n; ++i) {
            if (used.find(k - i) != used.end()) continue;
            used.insert(i);
            sum += i;
            ++cnt;
        }
        return sum;
    }
};
```

## Java

```java
class Solution {
    public int minimumSum(int n, int k) {
        int[] blocked = new int[300]; // enough for given constraints
        int count = 0;
        int sum = 0;
        for (int i = 1; count < n; i++) {
            if (blocked[i] == 0) {
                sum += i;
                count++;
                int complement = k - i;
                if (complement > 0 && complement < blocked.length) {
                    blocked[complement] = 1;
                }
            }
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def minimumSum(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        chosen = set()
        forbidden = set()
        i = 1
        while len(chosen) < n:
            if i not in chosen and i not in forbidden:
                chosen.add(i)
                comp = k - i
                if comp > 0:
                    forbidden.add(comp)
            i += 1
        return sum(chosen)
```

## Python3

```python
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        chosen = set()
        total = 0
        i = 1
        while len(chosen) < n:
            if (k - i) in chosen:
                i += 1
                continue
            chosen.add(i)
            total += i
            i += 1
        return total
```

## C

```c
int minimumSum(int n, int k) {
    // Since n,k ≤ 50, an array of size 200 is more than enough.
    bool used[200] = {false};
    int cnt = 0;
    int sum = 0;
    for (int i = 1; cnt < n; ++i) {
        if (k - i > 0 && used[k - i]) continue; // conflict with a previously chosen number
        used[i] = true;
        sum += i;
        ++cnt;
    }
    return sum;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumSum(int n, int k)
    {
        var taken = new HashSet<int>();
        int sum = 0, cnt = 0;
        for (int i = 1; cnt < n; i++)
        {
            if (i * 2 == k)
            {
                taken.Add(i);
                sum += i;
                cnt++;
            }
            else if (!taken.Contains(k - i))
            {
                taken.Add(i);
                sum += i;
                cnt++;
            }
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var minimumSum = function(n, k) {
    const chosen = new Set();
    let sum = 0;
    let i = 1;
    while (chosen.size < n) {
        if (!chosen.has(k - i)) {
            chosen.add(i);
            sum += i;
        }
        i++;
    }
    return sum;
};
```

## Typescript

```typescript
function minimumSum(n: number, k: number): number {
    const selected = new Set<number>();
    let sum = 0;
    let i = 1;
    while (selected.size < n) {
        if (!selected.has(k - i)) {
            selected.add(i);
            sum += i;
        }
        i++;
    }
    return sum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function minimumSum($n, $k) {
        $forbidden = [];
        $sum = 0;
        $cnt = 0;
        $i = 1;
        while ($cnt < $n) {
            if (!isset($forbidden[$i])) {
                $sum += $i;
                $cnt++;
                $f = $k - $i;
                if ($f > 0) {
                    $forbidden[$f] = true;
                }
            }
            $i++;
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func minimumSum(_ n: Int, _ k: Int) -> Int {
        var chosen = Set<Int>()
        var sum = 0
        var count = 0
        var i = 1
        while count < n {
            if !chosen.contains(k - i) {
                chosen.insert(i)
                sum += i
                count += 1
            }
            i += 1
        }
        return sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumSum(n: Int, k: Int): Int {
        val selected = HashSet<Int>()
        var sum = 0
        var count = 0
        var i = 1
        while (count < n) {
            if (!selected.contains(k - i)) {
                selected.add(i)
                sum += i
                count++
            }
            i++
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int minimumSum(int n, int k) {
    final Set<int> chosen = {};
    int sum = 0;
    int i = 1;
    while (chosen.length < n) {
      if (!chosen.contains(k - i)) {
        chosen.add(i);
        sum += i;
      }
      i++;
    }
    return sum;
  }
}
```

## Golang

```go
func minimumSum(n int, k int) int {
    selected := make(map[int]bool)
    sum := 0
    for i := 1; len(selected) < n; i++ {
        if _, exists := selected[k-i]; !exists {
            selected[i] = true
            sum += i
        }
    }
    return sum
}
```

## Ruby

```ruby
def minimum_sum(n, k)
  selected = {}
  sum = 0
  i = 1
  while selected.size < n
    unless selected.key?(k - i)
      selected[i] = true
      sum += i
    end
    i += 1
  end
  sum
end
```

## Scala

```scala
object Solution {
    def minimumSum(n: Int, k: Int): Int = {
        val blocked = scala.collection.mutable.Set[Int]()
        var sum = 0
        var count = 0
        var i = 1
        while (count < n) {
            if (!blocked.contains(i)) {
                sum += i
                count += 1
                val partner = k - i
                if (partner > 0 && partner != i) blocked += partner
            }
            i += 1
        }
        sum
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn minimum_sum(n: i32, k: i32) -> i32 {
        let mut selected: HashSet<i32> = HashSet::new();
        let mut sum = 0;
        let mut cur = 1;
        while (selected.len() as i32) < n {
            if !selected.contains(&(k - cur)) {
                selected.insert(cur);
                sum += cur;
            }
            cur += 1;
        }
        sum
    }
}
```

## Racket

```racket
(require racket/sequence)

(define/contract (minimum-sum n k)
  (-> exact-integer? exact-integer? exact-integer?)
  (let ([selected (make-hash)]
        [forbidden (make-hash)]
        [sum 0]
        [count 0])
    (for ([i (in-naturals 1)] #:break (= count n))
      (when (and (not (hash-has-key? selected i))
                 (not (hash-has-key? forbidden i)))
        (hash-set! selected i #t)
        (set! sum (+ sum i))
        (set! count (+ count 1))
        (let ([c (- k i)])
          (when (> c 0)
            (hash-set! forbidden c #t)))))
    sum))
```

## Erlang

```erlang
-spec minimum_sum(N :: integer(), K :: integer()) -> integer().
minimum_sum(N, K) ->
    go(1, N, K, #{}, 0).

go(_I, 0, _K, _Set, Sum) ->
    Sum;
go(I, Rem, K, Set, Sum) ->
    case maps:is_key(K - I, Set) of
        true ->
            go(I + 1, Rem, K, Set, Sum);
        false ->
            NewSet = maps:put(I, true, Set),
            go(I + 1, Rem - 1, K, NewSet, Sum + I)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_sum(n :: integer, k :: integer) :: integer
  def minimum_sum(n, k), do: go(1, 0, 0, MapSet.new(), n, k)

  defp go(_i, sum, count, _set, n, _k) when count == n,
    do: sum

  defp go(i, sum, count, set, n, k) do
    if MapSet.member?(set, k - i) do
      go(i + 1, sum, count, set, n, k)
    else
      go(i + 1, sum + i, count + 1, MapSet.put(set, i), n, k)
    end
  end
end
```
