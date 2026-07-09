# 0822. Card Flipping Game

## Cpp

```cpp
class Solution {
public:
    int flipgame(vector<int>& fronts, vector<int>& backs) {
        unordered_set<int> same;
        int n = fronts.size();
        for (int i = 0; i < n; ++i) {
            if (fronts[i] == backs[i]) {
                same.insert(fronts[i]);
            }
        }
        int ans = INT_MAX;
        for (int x : fronts) {
            if (!same.count(x)) ans = min(ans, x);
        }
        for (int x : backs) {
            if (!same.count(x)) ans = min(ans, x);
        }
        return ans == INT_MAX ? 0 : ans;
    }
};
```

## Java

```java
class Solution {
    public int flipgame(int[] fronts, int[] backs) {
        java.util.HashSet<Integer> bad = new java.util.HashSet<>();
        int n = fronts.length;
        for (int i = 0; i < n; i++) {
            if (fronts[i] == backs[i]) {
                bad.add(fronts[i]);
            }
        }
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (!bad.contains(fronts[i])) {
                ans = Math.min(ans, fronts[i]);
            }
            if (!bad.contains(backs[i])) {
                ans = Math.min(ans, backs[i]);
            }
        }
        return ans == Integer.MAX_VALUE ? 0 : ans;
    }
}
```

## Python

```python
class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        bad = set()
        for f, b in zip(fronts, backs):
            if f == b:
                bad.add(f)
        ans = float('inf')
        for num in fronts + backs:
            if num not in bad and num < ans:
                ans = num
        return 0 if ans == float('inf') else ans
```

## Python3

```python
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        bad = set()
        for f, b in zip(fronts, backs):
            if f == b:
                bad.add(f)
        candidates = set(fronts) | set(backs)
        ans = float('inf')
        for x in candidates:
            if x not in bad:
                ans = min(ans, x)
        return 0 if ans == float('inf') else ans
```

## C

```c
#include <limits.h>
#include <stdbool.h>

int flipgame(int* fronts, int frontsSize, int* backs, int backsSize) {
    const int MAX_VAL = 2000;
    bool bad[MAX_VAL + 1] = {false};

    for (int i = 0; i < frontsSize; ++i) {
        if (fronts[i] == backs[i]) {
            bad[fronts[i]] = true;
        }
    }

    int ans = INT_MAX;
    for (int i = 0; i < frontsSize; ++i) {
        if (!bad[fronts[i]] && fronts[i] < ans) ans = fronts[i];
        if (!bad[backs[i]] && backs[i] < ans) ans = backs[i];
    }

    return (ans == INT_MAX) ? 0 : ans;
}
```

## Csharp

```csharp
public class Solution {
    public int Flipgame(int[] fronts, int[] backs) {
        var bad = new HashSet<int>();
        for (int i = 0; i < fronts.Length; i++) {
            if (fronts[i] == backs[i]) {
                bad.Add(fronts[i]);
            }
        }
        int ans = int.MaxValue;
        foreach (var x in fronts) {
            if (!bad.Contains(x)) {
                ans = Math.Min(ans, x);
            }
        }
        foreach (var x in backs) {
            if (!bad.Contains(x)) {
                ans = Math.Min(ans, x);
            }
        }
        return ans == int.MaxValue ? 0 : ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} fronts
 * @param {number[]} backs
 * @return {number}
 */
var flipgame = function(fronts, backs) {
    const bad = new Set();
    for (let i = 0; i < fronts.length; ++i) {
        if (fronts[i] === backs[i]) {
            bad.add(fronts[i]);
        }
    }
    let ans = Infinity;
    for (const x of fronts) {
        if (!bad.has(x) && x < ans) ans = x;
    }
    for (const x of backs) {
        if (!bad.has(x) && x < ans) ans = x;
    }
    return ans === Infinity ? 0 : ans;
};
```

## Typescript

```typescript
function flipgame(fronts: number[], backs: number[]): number {
    const n = fronts.length;
    const bad = new Set<number>();
    for (let i = 0; i < n; i++) {
        if (fronts[i] === backs[i]) {
            bad.add(fronts[i]);
        }
    }

    let ans = Infinity;
    for (let i = 0; i < n; i++) {
        const f = fronts[i];
        const b = backs[i];
        if (!bad.has(f) && f < ans) ans = f;
        if (!bad.has(b) && b < ans) ans = b;
    }

    return ans === Infinity ? 0 : ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $fronts
     * @param Integer[] $backs
     * @return Integer
     */
    function flipgame($fronts, $backs) {
        $bad = [];
        $n = count($fronts);
        for ($i = 0; $i < $n; $i++) {
            if ($fronts[$i] == $backs[$i]) {
                $bad[$fronts[$i]] = true;
            }
        }
        $ans = PHP_INT_MAX;
        for ($i = 0; $i < $n; $i++) {
            $f = $fronts[$i];
            $b = $backs[$i];
            if (!isset($bad[$f]) && $f < $ans) {
                $ans = $f;
            }
            if (!isset($bad[$b]) && $b < $ans) {
                $ans = $b;
            }
        }
        return $ans === PHP_INT_MAX ? 0 : $ans;
    }
}
```

## Swift

```swift
class Solution {
    func flipgame(_ fronts: [Int], _ backs: [Int]) -> Int {
        var bad = Set<Int>()
        let n = fronts.count
        for i in 0..<n {
            if fronts[i] == backs[i] {
                bad.insert(fronts[i])
            }
        }
        var answer = Int.max
        for v in fronts where !bad.contains(v) && v < answer {
            answer = v
        }
        for v in backs where !bad.contains(v) && v < answer {
            answer = v
        }
        return answer == Int.max ? 0 : answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun flipgame(fronts: IntArray, backs: IntArray): Int {
        val n = fronts.size
        val bad = HashSet<Int>()
        for (i in 0 until n) {
            if (fronts[i] == backs[i]) {
                bad.add(fronts[i])
            }
        }
        var ans = Int.MAX_VALUE
        for (i in 0 until n) {
            val f = fronts[i]
            val b = backs[i]
            if (!bad.contains(f)) ans = kotlin.math.min(ans, f)
            if (!bad.contains(b)) ans = kotlin.math.min(ans, b)
        }
        return if (ans == Int.MAX_VALUE) 0 else ans
    }
}
```

## Dart

```dart
class Solution {
  int flipgame(List<int> fronts, List<int> backs) {
    final Set<int> bad = {};
    for (int i = 0; i < fronts.length; i++) {
      if (fronts[i] == backs[i]) {
        bad.add(fronts[i]);
      }
    }

    int ans = 2001; // greater than any possible value
    for (final v in fronts) {
      if (!bad.contains(v) && v < ans) {
        ans = v;
      }
    }
    for (final v in backs) {
      if (!bad.contains(v) && v < ans) {
        ans = v;
      }
    }

    return ans == 2001 ? 0 : ans;
  }
}
```

## Golang

```go
func flipgame(fronts []int, backs []int) int {
    bad := make(map[int]bool)
    for i := 0; i < len(fronts); i++ {
        if fronts[i] == backs[i] {
            bad[fronts[i]] = true
        }
    }
    const maxInt = int(^uint(0) >> 1)
    ans := maxInt
    for i := 0; i < len(fronts); i++ {
        if !bad[fronts[i]] && fronts[i] < ans {
            ans = fronts[i]
        }
        if !bad[backs[i]] && backs[i] < ans {
            ans = backs[i]
        }
    }
    if ans == maxInt {
        return 0
    }
    return ans
}
```

## Ruby

```ruby
def flipgame(fronts, backs)
  bad = {}
  fronts.each_with_index do |f, i|
    b = backs[i]
    bad[f] = true if f == b
  end

  min_good = nil
  (fronts + backs).each do |num|
    next if bad.key?(num)
    min_good = num if min_good.nil? || num < min_good
  end

  min_good ? min_good : 0
end
```

## Scala

```scala
object Solution {
    def flipgame(fronts: Array[Int], backs: Array[Int]): Int = {
        val n = fronts.length
        val bad = scala.collection.mutable.HashSet[Int]()
        for (i <- 0 until n) {
            if (fronts(i) == backs(i)) bad += fronts(i)
        }
        var ans = Int.MaxValue
        for (i <- 0 until n) {
            if (!bad.contains(fronts(i))) ans = math.min(ans, fronts(i))
            if (!bad.contains(backs(i))) ans = math.min(ans, backs(i))
        }
        if (ans == Int.MaxValue) 0 else ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn flipgame(fronts: Vec<i32>, backs: Vec<i32>) -> i32 {
        use std::collections::HashSet;
        let mut bad = HashSet::new();
        for (f, b) in fronts.iter().zip(backs.iter()) {
            if f == b {
                bad.insert(*f);
            }
        }
        let mut ans = i32::MAX;
        for &x in fronts.iter() {
            if !bad.contains(&x) && x < ans {
                ans = x;
            }
        }
        for &x in backs.iter() {
            if !bad.contains(&x) && x < ans {
                ans = x;
            }
        }
        if ans == i32::MAX { 0 } else { ans }
    }
}
```

## Racket

```racket
(define/contract (flipgame fronts backs)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length fronts))
         (bad (make-hash)))
    ;; numbers that appear on both sides of the same card cannot be good
    (for ([i (in-range n)])
      (when (= (list-ref fronts i) (list-ref backs i))
        (hash-set! bad (list-ref fronts i) #t)))
    (define ans #f)
    (for ([i (in-range n)])
      (let ((f (list-ref fronts i))
            (b (list-ref backs i)))
        (unless (hash-has-key? bad f)
          (set! ans (if ans (min ans f) f)))
        (unless (hash-has-key? bad b)
          (set! ans (if ans (min ans b) b)))))
    (if ans ans 0)))
```

## Erlang

```erlang
-spec flipgame(Fronts :: [integer()], Backs :: [integer()]) -> integer().
flipgame(Fronts, Backs) ->
    BadSet = build_bad_set(Fronts, Backs, #{}),
    All = Fronts ++ Backs,
    find_min(All, BadSet, undefined).

build_bad_set([], [], Bad) -> Bad;
build_bad_set([F|Fs], [B|Bs], Bad) ->
    NewBad = if F == B -> maps:put(F, true, Bad); true -> Bad end,
    build_bad_set(Fs, Bs, NewBad).

find_min([], _Bad, undefined) -> 0;
find_min([], _Bad, Min) -> Min;
find_min([X|Xs], Bad, Min) ->
    case maps:is_key(X, Bad) of
        true ->
            find_min(Xs, Bad, Min);
        false ->
            NewMin = case Min of
                undefined -> X;
                _ when X < Min -> X;
                _ -> Min
            end,
            find_min(Xs, Bad, NewMin)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec flipgame(fronts :: [integer], backs :: [integer]) :: integer
  def flipgame(fronts, backs) do
    bad =
      Enum.zip(fronts, backs)
      |> Enum.reduce(MapSet.new(), fn {f, b}, acc ->
        if f == b, do: MapSet.put(acc, f), else: acc
      end)

    candidates = Enum.filter(backs, fn x -> not MapSet.member?(bad, x) end)

    case candidates do
      [] -> 0
      _ -> Enum.min(candidates)
    end
  end
end
```
