# 3592. Inverse Coin Change

## Cpp

```cpp
class Solution {
public:
    vector<int> findCoins(vector<int>& numWays) {
        int n = (int)numWays.size();
        vector<long long> ways(n + 1);
        ways[0] = 1; // one way to make amount 0
        for (int i = 1; i <= n; ++i) ways[i] = numWays[i - 1];
        vector<int> ans;
        while (true) {
            int c = -1;
            for (int i = 1; i <= n; ++i) {
                if (ways[i] == 1) { c = i; break; }
            }
            if (c == -1) break;
            ans.push_back(c);
            for (int s = n; s >= c; --s) {
                ways[s] -= ways[s - c];
                if (ways[s] < 0) return {};
            }
        }
        for (int i = 1; i <= n; ++i) {
            if (ways[i] != 0) return {};
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> findCoins(int[] numWays) {
        int n = numWays.length - 1;
        long[] ways = new long[numWays.length];
        for (int i = 0; i < numWays.length; i++) {
            ways[i] = numWays[i];
        }
        List<Integer> ans = new ArrayList<>();
        while (true) {
            int c = -1;
            for (int i = 1; i <= n; i++) {
                if (ways[i] == 1) {
                    c = i;
                    break;
                }
            }
            if (c == -1) {
                break;
            }
            ans.add(c);
            for (int s = c; s <= n; s++) {
                ways[s] -= ways[s - c];
                if (ways[s] < 0) {
                    return new ArrayList<>();
                }
            }
        }
        for (int i = 1; i <= n; i++) {
            if (ways[i] != 0) {
                return new ArrayList<>();
            }
        }
        Collections.sort(ans);
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findCoins(self, numWays):
        """
        :type numWays: List[int]
        :rtype: List[int]
        """
        n = len(numWays)
        # ways[0] is the base case for amount 0
        ways = [1] + list(numWays)  # 1-indexed DP array
        ans = []
        while True:
            c = None
            for i in range(1, n + 1):
                if ways[i] == 1:
                    c = i
                    break
            if c is None:
                break
            ans.append(c)
            old = ways[:]  # snapshot before subtraction
            for s in range(c, n + 1):
                ways[s] -= old[s - c]
                if ways[s] < 0:
                    return []
        # after processing all possible coins, remaining counts must be zero
        if any(ways[i] != 0 for i in range(1, n + 1)):
            return []
        ans.sort()
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays) - 1
        if n < 0:
            return []
        ways = numWays[:]
        # base case for DP subtraction
        ways[0] = 1
        ans: List[int] = []

        while True:
            coin = None
            for i in range(1, n + 1):
                if ways[i] == 1:
                    coin = i
                    break
            if coin is None:
                break
            ans.append(coin)
            for s in range(coin, n + 1):
                ways[s] -= ways[s - coin]
                if ways[s] < 0:
                    return []
        # verify all remaining counts are zero
        for i in range(1, n + 1):
            if ways[i] != 0:
                return []
        return ans
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findCoins(int* numWays, int numWaysSize, int* returnSize) {
    if (numWaysSize <= 1) { // no amounts to represent
        *returnSize = 0;
        return NULL;
    }
    int n = numWaysSize - 1;                 // highest amount index (1‑based)
    long long ways[101];                     // constraints: length ≤ 100
    for (int i = 0; i < numWaysSize; ++i) {
        ways[i] = numWays[i];
    }

    int ans[101];
    int ansCnt = 0;

    while (1) {
        int c = -1;
        for (int i = 1; i <= n; ++i) {
            if (ways[i] == 1) {   // smallest remaining denomination
                c = i;
                break;
            }
        }
        if (c == -1) break;       // no more denominations with count 1

        ans[ansCnt++] = c;

        for (int s = c; s <= n; ++s) {
            ways[s] -= ways[s - c];
            if (ways[s] < 0) {    // impossible configuration
                *returnSize = 0;
                return NULL;
            }
        }
    }

    // verify that all counts are reduced to zero
    for (int i = 1; i <= n; ++i) {
        if (ways[i] != 0) {
            *returnSize = 0;
            return NULL;
        }
    }

    int* res = (int*)malloc(ansCnt * sizeof(int));
    for (int i = 0; i < ansCnt; ++i) res[i] = ans[i];
    *returnSize = ansCnt;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> FindCoins(int[] numWays) {
        int m = numWays.Length;
        // cur[amount], amount from 0..m
        long[] cur = new long[m + 1];
        cur[0] = 0;
        for (int i = 1; i <= m; i++) {
            cur[i] = numWays[i - 1];
        }

        List<int> ans = new List<int>();

        while (true) {
            int c = -1;
            for (int i = 1; i < cur.Length; i++) {
                if (cur[i] == 1) {
                    c = i;
                    break;
                }
            }
            if (c == -1) break;

            ans.Add(c);
            for (int s = c; s < cur.Length; s++) {
                cur[s] -= cur[s - c];
                if (cur[s] < 0) return new List<int>();
            }
        }

        for (int i = 1; i < cur.Length; i++) {
            if (cur[i] != 0) return new List<int>();
        }

        return ans;
    }
}
```

## Javascript

```javascript
/ **
 * @param {number[]} numWays
 * @return {number[]}
 */
var findCoins = function(numWays) {
    const n = numWays.length;
    // make a mutable copy
    const ways = numWays.slice();
    const ans = [];

    while (true) {
        let idx = -1;
        for (let i = 0; i < n; ++i) {
            if (ways[i] === 1) { idx = i; break; }
        }
        if (idx === -1) break;               // no more coins
        const c = idx + 1;                    // denomination value
        ans.push(c);

        // remove contribution of coin c
        for (let s = c; s <= n; ++s) {
            const curIdx = s - 1;
            const sub = (s - c === 0) ? 1 : ways[(s - c) - 1];
            ways[curIdx] -= sub;
            if (ways[curIdx] < 0) return [];
        }
    }

    // verify all zeros
    for (let i = 0; i < n; ++i) {
        if (ways[i] !== 0) return [];
    }
    return ans;
};
```

## Typescript

```typescript
function findCoins(numWays: number[]): number[] {
    const n = numWays.length - 1;
    const ways = numWays.slice(); // mutable copy
    const ans: number[] = [];

    while (true) {
        let c = -1;
        for (let i = 1; i <= n; ++i) {
            if (ways[i] === 1) {
                c = i;
                break;
            }
        }
        if (c === -1) break;

        ans.push(c);
        for (let s = c; s <= n; ++s) {
            ways[s] -= ways[s - c];
            if (ways[s] < 0) return [];
        }
    }

    for (let i = 1; i <= n; ++i) {
        if (ways[i] !== 0) return [];
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $numWays
     * @return Integer[]
     */
    function findCoins($numWays) {
        $n = count($numWays);
        // ways[0] is the empty way, always 1
        $ways = array_fill(0, $n + 1, 0);
        $ways[0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            $ways[$i] = $numWays[$i - 1];
        }

        $ans = [];

        while (true) {
            $c = -1;
            for ($i = 1; $i <= $n; $i++) {
                if ($ways[$i] == 1) {
                    $c = $i;
                    break;
                }
            }
            if ($c == -1) {
                break;
            }

            $ans[] = $c;

            // remove contribution of coin c (process descending to avoid using already updated values)
            for ($s = $n; $s >= $c; $s--) {
                $ways[$s] -= $ways[$s - $c];
                if ($ways[$s] < 0) {
                    return [];
                }
            }
        }

        // verify all remaining ways are zero
        for ($i = 1; $i <= $n; $i++) {
            if ($ways[$i] != 0) {
                return [];
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func findCoins(_ numWays: [Int]) -> [Int] {
        var ways = numWays
        let n = ways.count - 1
        if n <= 0 { return [] }
        var ans = [Int]()
        
        while true {
            var c = -1
            for i in 1...n {
                if ways[i] == 1 {
                    c = i
                    break
                }
            }
            if c == -1 { break }
            ans.append(c)
            for s in c...n {
                ways[s] -= ways[s - c]
                if ways[s] < 0 {
                    return []
                }
            }
        }
        
        for i in 1...n {
            if ways[i] != 0 {
                return []
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findCoins(numWays: IntArray): List<Int> {
        val n = numWays.size
        val a = LongArray(n + 1)
        a[0] = 1L
        for (i in 1..n) {
            a[i] = numWays[i - 1].toLong()
        }
        val ans = mutableListOf<Int>()
        while (true) {
            var c = -1
            for (i in 1..n) {
                if (a[i] == 1L) {
                    c = i
                    break
                }
            }
            if (c == -1) break
            ans.add(c)
            for (s in n downTo c) {
                a[s] -= a[s - c]
                if (a[s] < 0) return emptyList()
            }
        }
        for (i in 1..n) {
            if (a[i] != 0L) return emptyList()
        }
        ans.sort()
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> findCoins(List<int> numWays) {
    int n = numWays.length;
    // dp[0] is the number of ways to make amount 0, which is always 1.
    List<int> dp = List.filled(n + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
      dp[i] = numWays[i - 1];
    }

    List<int> ans = [];

    while (true) {
      int coin = -1;
      for (int i = 1; i <= n; i++) {
        if (dp[i] == 1) {
          coin = i;
          break;
        }
      }
      if (coin == -1) break;

      ans.add(coin);
      for (int s = coin; s <= n; s++) {
        dp[s] -= dp[s - coin];
        if (dp[s] < 0) return [];
      }
    }

    for (int i = 1; i <= n; i++) {
      if (dp[i] != 0) return [];
    }

    return ans;
  }
}
```

## Golang

```go
func findCoins(numWays []int) []int {
    n := len(numWays)
    ways := make([]int, n)
    copy(ways, numWays)

    ans := []int{}
    for {
        cIdx := -1
        for i := 0; i < n; i++ {
            if ways[i] == 1 {
                cIdx = i
                break
            }
        }
        if cIdx == -1 {
            break
        }
        coin := cIdx + 1
        ans = append(ans, coin)

        for s := coin; s <= n; s++ {
            var sub int
            if s == coin {
                sub = 1 // ways to make amount 0 is implicitly 1
            } else {
                sub = ways[s-coin-1]
            }
            ways[s-1] -= sub
            if ways[s-1] < 0 {
                return []int{}
            }
        }
    }

    for i := 0; i < n; i++ {
        if ways[i] != 0 {
            return []int{}
        }
    }
    return ans
}
```

## Ruby

```ruby
def find_coins(num_ways)
  n = num_ways.length
  w = Array.new(n + 1, 0)
  w[0] = 1
  (1..n).each { |i| w[i] = num_ways[i - 1] }

  ans = []
  loop do
    c = nil
    (1..n).each do |i|
      if w[i] == 1
        c = i
        break
      end
    end
    break unless c

    ans << c
    old = w.dup
    (c..n).each do |s|
      w[s] = old[s] - old[s - c]
      return [] if w[s] < 0
    end
  end

  return [] unless w[1..n].all? { |v| v == 0 }
  ans.sort
end
```

## Scala

```scala
object Solution {
    def findCoins(numWays: Array[Int]): List[Int] = {
        val n = numWays.length - 1
        if (n <= 0) return List.empty[Int]

        // ways[0] should be 1 for the empty combination
        val ways = new Array[Long](n + 1)
        ways(0) = 1L
        var i = 1
        while (i <= n) {
            ways(i) = numWays(i).toLong
            i += 1
        }

        val ans = scala.collection.mutable.ListBuffer[Int]()

        var continue = true
        while (continue) {
            // find smallest amount with exactly one way
            var c = -1
            var idx = 1
            while (idx <= n && c == -1) {
                if (ways(idx) == 1L) c = idx
                idx += 1
            }
            if (c == -1) {
                continue = false
            } else {
                ans += c
                var s = c
                while (s <= n) {
                    ways(s) -= ways(s - c)
                    if (ways(s) < 0) return List.empty[Int]
                    s += 1
                }
            }
        }

        // verify all remaining counts are zero
        var j = 1
        while (j <= n) {
            if (ways(j) != 0L) return List.empty[Int]
            j += 1
        }

        ans.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_coins(num_ways: Vec<i32>) -> Vec<i32> {
        let n = num_ways.len();
        if n == 0 {
            return Vec::new();
        }
        // ways[0] is the empty set, always 1
        let mut ways: Vec<i64> = vec![0; n + 1];
        ways[0] = 1;
        for i in 1..=n {
            ways[i] = num_ways[i - 1] as i64;
        }

        let mut ans: Vec<i32> = Vec::new();

        loop {
            // find smallest amount with exactly one way
            let mut coin_opt: Option<usize> = None;
            for i in 1..=n {
                if ways[i] == 1 {
                    coin_opt = Some(i);
                    break;
                }
            }
            match coin_opt {
                Some(c) => {
                    ans.push(c as i32);
                    // remove contributions of this coin (process descending)
                    for s in (c..=n).rev() {
                        ways[s] -= ways[s - c];
                        if ways[s] < 0 {
                            return Vec::new();
                        }
                    }
                }
                None => break,
            }
        }

        // verify all remaining counts are zero
        for i in 1..=n {
            if ways[i] != 0 {
                return Vec::new();
            }
        }

        ans.sort_unstable();
        ans
    }
}
```

## Racket

```racket
(define/contract (find-coins numWays)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((n (sub1 (length numWays)))               ; maximum amount index
         (vec (list->vector numWays))              ; mutable copy
         (valid #t))                               ; flag for negative values

    ;; helper: find smallest index >0 with value exactly 1
    (define (find-one)
      (let loop ((i 1))
        (cond [(> i n) #f]
              [(= (vector-ref vec i) 1) i]
              [else (loop (add1 i))])))

    ;; helper: check that all entries for amounts >=1 are zero
    (define (all-zero?)
      (let loop ((i 1))
        (cond [(> i n) #t]
              [(zero? (vector-ref vec i)) (loop (add1 i))]
              [else #f])))

    ;; main recursive extraction
    (let recur ((ans '()))
      (if (not valid)
          '()
          (let ((c (find-one)))
            (if (not c)                                   ; no more denominations
                (if (and (all-zero?) (not (null? ans)))   ; ensure we actually extracted something
                    (reverse ans)
                    (if (all-zero?) (reverse ans) '()))  ; empty answer is allowed if all zero
                (begin
                  ;; subtract contribution of coin c
                  (for ([s (in-range c (add1 n))])
                    (let* ((old (vector-ref vec s))
                           (sub (vector-ref vec (- s c)))
                           (new (- old sub)))
                      (when (< new 0) (set! valid #f))
                      (vector-set! vec s new)))
                  (if valid
                      (recur (cons c ans))
                      '()))))))))
```

## Erlang

```erlang
-spec find_coins(NumWays :: [integer()]) -> [integer()].
find_coins(NumWays) ->
    Tuple = list_to_tuple(NumWays),
    N = length(NumWays) - 1,
    process(Tuple, N, []).

%% --------------------------------------------------------------------
%% Main processing loop
process(Tuple, N, Ans) ->
    case find_coin(1, N, Tuple) of
        none ->
            if all_zero(Tuple, N) -> lists:reverse(Ans);
               true -> []
            end;
        {ok, C} ->
            case update(C, C, N, Tuple) of
                {error, _} -> [];
                {ok, NewTuple} -> process(NewTuple, N, [C | Ans])
            end
    end.

%% --------------------------------------------------------------------
%% Find smallest index >0 with value 1
find_coin(I, N, Tuple) when I =< N ->
    case element(I + 1, Tuple) of
        1 -> {ok, I};
        _ -> find_coin(I + 1, N, Tuple)
    end;
find_coin(_, _, _) -> none.

%% --------------------------------------------------------------------
%% Remove contribution of coin C
update(S, C, N, Tuple) when S =< N ->
    OldS   = element(S + 1, Tuple),
    OldPrev = element(S - C + 1, Tuple),
    NewVal = OldS - OldPrev,
    if NewVal < 0 ->
            {error, invalid};
       true ->
            NewTuple = setelement(S + 1, Tuple, NewVal),
            update(S + 1, C, N, NewTuple)
    end;
update(_, _, _, Tuple) -> {ok, Tuple}.

%% --------------------------------------------------------------------
%% Check all entries (except index 0) are zero
all_zero(I, N, Tuple) when I =< N ->
    case element(I + 1, Tuple) of
        0 -> all_zero(I + 1, N, Tuple);
        _ -> false
    end;
all_zero(_, _, _) -> true.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_coins(num_ways :: [integer]) :: [integer]
  def find_coins(num_ways) do
    max = length(num_ways)
    # prepend dummy zero for 1-indexed handling
    ways = List.to_tuple([0 | num_ways])

    case process(ways, max, []) do
      {:ok, ans, final_ways} ->
        if all_zero?(final_ways, max), do: Enum.reverse(ans), else: []

      :error ->
        []
    end
  end

  defp process(tuple, max, acc) do
    case find_smallest_one(tuple, max) do
      nil ->
        {:ok, acc, tuple}

      c ->
        case remove_coin(tuple, max, c) do
          {:error} -> :error
          new_tuple -> process(new_tuple, max, [c | acc])
        end
    end
  end

  defp find_smallest_one(t, max) do
    Enum.find(1..max, fn i -> elem(t, i) == 1 end)
  end

  defp remove_coin(t, max, c) do
    Enum.reduce_while(c..max, t, fn s, acc ->
      val = elem(acc, s) - elem(acc, s - c)

      if val < 0 do
        {:halt, {:error}}
      else
        {:cont, put_elem(acc, s, val)}
      end
    end)
  end

  defp all_zero?(t, max) do
    Enum.all?(1..max, fn i -> elem(t, i) == 0 end)
  end
end
```
