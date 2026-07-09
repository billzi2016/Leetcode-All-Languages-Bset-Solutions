# 2952. Minimum Number of Coins to be Added

## Cpp

```cpp
class Solution {
public:
    int minimumAddedCoins(vector<int>& coins, int target) {
        sort(coins.begin(), coins.end());
        long long reach = 0; // we can form all values in [1, reach]
        int added = 0;
        for (int c : coins) {
            while (reach < target && c > reach + 1) {
                ++added;
                reach = 2 * reach + 1; // add coin of value reach+1
            }
            if (reach >= target) break;
            if (c <= reach + 1) {
                reach += c;
            }
        }
        while (reach < target) {
            ++added;
            reach = 2 * reach + 1;
        }
        return added;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int minimumAddedCoins(int[] coins, int target) {
        Arrays.sort(coins);
        long miss = 1;
        int added = 0;
        int i = 0;
        while (miss <= target) {
            if (i < coins.length && coins[i] <= miss) {
                miss += coins[i];
                i++;
            } else {
                // add a coin of value 'miss'
                miss += miss;
                added++;
            }
        }
        return added;
    }
}
```

## Python

```python
class Solution(object):
    def minimumAddedCoins(self, coins, target):
        """
        :type coins: List[int]
        :type target: int
        :rtype: int
        """
        coins.sort()
        miss = 1          # smallest sum that cannot be formed yet
        added = 0
        i = 0
        n = len(coins)
        while miss <= target:
            if i < n and coins[i] <= miss:
                miss += coins[i]
                i += 1
            else:
                # add a coin of value 'miss'
                added += 1
                miss <<= 1   # same as miss += miss
        return added
```

## Python3

```python
class Solution:
    def minimumAddedCoins(self, coins: list[int], target: int) -> int:
        coins.sort()
        added = 0
        reach = 0  # we can form all values in [1, reach]
        i = 0
        n = len(coins)
        while reach < target:
            if i < n and coins[i] <= reach + 1:
                reach += coins[i]
                i += 1
            else:
                added += 1
                # add a coin of value reach+1
                reach = 2 * reach + 1
        return added
```

## C

```c
#include <stdlib.h>

static int cmpInt(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int minimumAddedCoins(int* coins, int coinsSize, int target) {
    qsort(coins, (size_t)coinsSize, sizeof(int), cmpInt);
    long long miss = 1;          // smallest sum that cannot be formed yet
    int i = 0, added = 0;
    while (miss <= target) {
        if (i < coinsSize && coins[i] <= miss) {
            miss += coins[i];
            ++i;
        } else {
            // add a coin of value 'miss'
            miss += miss;
            ++added;
        }
    }
    return added;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumAddedCoins(int[] coins, int target)
    {
        Array.Sort(coins);
        long miss = 1;
        int added = 0;
        int i = 0;
        int n = coins.Length;

        while (i < n && miss <= target)
        {
            if (coins[i] <= miss)
            {
                miss += coins[i];
                i++;
            }
            else
            {
                added++;
                miss += miss;
            }
        }

        while (miss <= target)
        {
            added++;
            miss += miss;
        }

        return added;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} coins
 * @param {number} target
 * @return {number}
 */
var minimumAddedCoins = function(coins, target) {
    coins.sort((a, b) => a - b);
    let miss = 1; // smallest sum we cannot form yet
    let added = 0;
    let i = 0;
    const n = coins.length;
    
    while (miss <= target) {
        if (i < n && coins[i] <= miss) {
            miss += coins[i];
            i++;
        } else {
            // add a coin of value 'miss'
            added++;
            miss += miss; // now we can form up to 2*miss-1
        }
    }
    
    return added;
};
```

## Typescript

```typescript
function minimumAddedCoins(coins: number[], target: number): number {
    coins.sort((a, b) => a - b);
    let miss = 1;
    let added = 0;
    let i = 0;
    const n = coins.length;

    while (miss <= target) {
        if (i < n && coins[i] <= miss) {
            miss += coins[i];
            i++;
        } else {
            // add a coin of value 'miss'
            added++;
            miss += miss; // now we can reach up to 2*miss - 1
        }
    }

    return added;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $coins
     * @param Integer $target
     * @return Integer
     */
    function minimumAddedCoins($coins, $target) {
        sort($coins);
        $reach = 0;   // we can form all sums in [1, $reach]
        $added = 0;
        foreach ($coins as $c) {
            while ($c > $reach + 1 && $reach < $target) {
                // add a coin of value $reach+1
                $added++;
                $reach += $reach + 1; // now we can reach up to 2*$reach+1 (old $reach)
            }
            if ($c <= $reach + 1) {
                $reach += $c;
            }
        }
        while ($reach < $target) {
            $added++;
            $reach += $reach + 1;
        }
        return $added;
    }
}
```

## Swift

```swift
class Solution {
    func minimumAddedCoins(_ coins: [Int], _ target: Int) -> Int {
        let sorted = coins.sorted()
        var added = 0
        var reach = 0
        var i = 0
        while i < sorted.count && reach < target {
            if sorted[i] <= reach + 1 {
                reach += sorted[i]
                i += 1
            } else {
                added += 1
                reach = reach + (reach + 1)
            }
        }
        while reach < target {
            added += 1
            reach = reach + (reach + 1)
        }
        return added
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumAddedCoins(coins: IntArray, target: Int): Int {
        val sorted = coins.sorted()
        var miss: Long = 1L
        var added = 0
        var i = 0
        while (miss <= target) {
            if (i < sorted.size && sorted[i].toLong() <= miss) {
                miss += sorted[i]
                i++
            } else {
                // add a coin of value 'miss'
                miss *= 2L
                added++
            }
        }
        return added
    }
}
```

## Dart

```dart
class Solution {
  int minimumAddedCoins(List<int> coins, int target) {
    coins.sort();
    int i = 0;
    int added = 0;
    int miss = 1; // smallest unobtainable sum
    while (miss <= target) {
      if (i < coins.length && coins[i] <= miss) {
        miss += coins[i];
        i++;
      } else {
        added++;
        miss += miss; // add coin of value 'miss'
      }
    }
    return added;
  }
}
```

## Golang

```go
func minimumAddedCoins(coins []int, target int) int {
    sort.Ints(coins)
    ans, miss, i := 0, 1, 0
    for miss <= target {
        if i < len(coins) && coins[i] <= miss {
            miss += coins[i]
            i++
        } else {
            ans++
            miss <<= 1 // same as miss += miss
        }
    }
    return ans
}
```

## Ruby

```ruby
def minimum_added_coins(coins, target)
  coins.sort!
  miss = 1
  i = 0
  added = 0
  n = coins.length

  while miss <= target
    if i < n && coins[i] <= miss
      miss += coins[i]
      i += 1
    else
      # add a coin of value 'miss'
      miss <<= 1
      added += 1
    end
  end

  added
end
```

## Scala

```scala
object Solution {
    def minimumAddedCoins(coins: Array[Int], target: Int): Int = {
        val sorted = coins.sorted
        var miss: Long = 1L
        var i = 0
        var added = 0
        while (miss <= target) {
            if (i < sorted.length && sorted(i).toLong <= miss) {
                miss += sorted(i)
                i += 1
            } else {
                added += 1
                miss += miss
            }
        }
        added
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_added_coins(mut coins: Vec<i32>, target: i32) -> i32 {
        coins.sort_unstable();
        let mut miss: i64 = 1; // smallest unobtainable sum
        let mut added = 0i32;
        let mut idx = 0usize;
        let n = coins.len();

        while miss <= target as i64 {
            if idx < n && (coins[idx] as i64) <= miss {
                miss += coins[idx] as i64;
                idx += 1;
            } else {
                // add a coin of value 'miss'
                added += 1;
                miss += miss; // now we can reach up to 2*miss-1
            }
        }

        added
    }
}
```

## Racket

```racket
(define/contract (minimum-added-coins coins target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((sorted (sort coins <))
         (vec (list->vector sorted))
         (n (vector-length vec)))
    (let loop ((i 0) (miss 1) (added 0))
      (if (> miss target)
          added
          (if (and (< i n) (<= (vector-ref vec i) miss))
              (loop (+ i 1) (+ miss (vector-ref vec i)) added)
              (loop i (* 2 miss) (+ added 1)))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_added_coins/2]).

-spec minimum_added_coins(Coins :: [integer()], Target :: integer()) -> integer().
minimum_added_coins(Coins, Target) ->
    Sorted = lists:sort(Coins),
    go(Sorted, Target, 0, 1).

go(_, Target, Ans, Miss) when Miss > Target ->
    Ans;
go([], Target, Ans, Miss) ->
    go([], Target, Ans + 1, Miss * 2);
go([H|T], Target, Ans, Miss) when H =< Miss ->
    go(T, Target, Ans, Miss + H);
go(Coins, Target, Ans, Miss) ->
    go(Coins, Target, Ans + 1, Miss * 2).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_added_coins(coins :: [integer], target :: integer) :: integer
  def minimum_added_coins(coins, target) do
    sorted = Enum.sort(coins)
    go(sorted, 1, target, 0)
  end

  # When the smallest unobtainable sum exceeds target, we're done.
  defp go(_list, miss, target, added) when miss > target, do: added

  # No more original coins left; keep adding patches until coverage is enough.
  defp go([], miss, target, added) do
    go([], miss * 2, target, added + 1)
  end

  # Process the next coin.
  defp go([h | t] = list, miss, target, added) do
    if h <= miss do
      go(t, miss + h, target, added)
    else
      # Need to add a patch of value `miss`.
      go(list, miss * 2, target, added + 1)
    end
  end
end
```
