# 1798. Maximum Number of Consecutive Values You Can Make

## Cpp

```cpp
class Solution {
public:
    int getMaximumConsecutive(vector<int>& coins) {
        sort(coins.begin(), coins.end());
        long long cur = 0; // use long long to avoid overflow
        for (int v : coins) {
            if ((long long)v > cur + 1) break;
            cur += v;
        }
        return (int)(cur + 1);
    }
};
```

## Java

```java
class Solution {
    public int getMaximumConsecutive(int[] coins) {
        java.util.Arrays.sort(coins);
        long reachable = 0; // use long to avoid overflow during addition
        for (int coin : coins) {
            if (coin > reachable + 1) {
                break;
            }
            reachable += coin;
        }
        return (int)(reachable + 1);
    }
}
```

## Python

```python
class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        reach = 0  # we can form all values in [0, reach]
        for v in coins:
            if v > reach + 1:
                break
            reach += v
        return reach + 1
```

## Python3

```python
from typing import List

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        reachable = 0
        for v in coins:
            if v > reachable + 1:
                break
            reachable += v
        return reachable + 1
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int getMaximumConsecutive(int* coins, int coinsSize) {
    if (coinsSize == 0) return 1; // only value 0
    qsort(coins, (size_t)coinsSize, sizeof(int), cmp_int);
    long long cur = 0;
    for (int i = 0; i < coinsSize; ++i) {
        if ((long long)coins[i] <= cur + 1) {
            cur += coins[i];
        } else {
            break;
        }
    }
    return (int)(cur + 1);
}
```

## Csharp

```csharp
public class Solution
{
    public int GetMaximumConsecutive(int[] coins)
    {
        Array.Sort(coins);
        long reach = 0;
        foreach (int coin in coins)
        {
            if (coin <= reach + 1)
                reach += coin;
            else
                break;
        }
        return (int)(reach + 1);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} coins
 * @return {number}
 */
var getMaximumConsecutive = function(coins) {
    coins.sort((a, b) => a - b);
    let reach = 0;
    for (const v of coins) {
        if (v <= reach + 1) {
            reach += v;
        } else {
            break;
        }
    }
    return reach + 1;
};
```

## Typescript

```typescript
function getMaximumConsecutive(coins: number[]): number {
    coins.sort((a, b) => a - b);
    let reachable = 0;
    for (const coin of coins) {
        if (coin <= reachable + 1) {
            reachable += coin;
        } else {
            break;
        }
    }
    return reachable + 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $coins
     * @return Integer
     */
    function getMaximumConsecutive($coins) {
        sort($coins);
        $reach = 0;
        foreach ($coins as $c) {
            if ($c <= $reach + 1) {
                $reach += $c;
            } else {
                break;
            }
        }
        return $reach + 1;
    }
}
```

## Swift

```swift
class Solution {
    func getMaximumConsecutive(_ coins: [Int]) -> Int {
        let sortedCoins = coins.sorted()
        var reachable = 0
        for coin in sortedCoins {
            if coin <= reachable + 1 {
                reachable += coin
            } else {
                break
            }
        }
        return reachable + 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getMaximumConsecutive(coins: IntArray): Int {
        val arr = coins.clone()
        arr.sort()
        var cur = 0L
        for (v in arr) {
            if (v.toLong() <= cur + 1) {
                cur += v
            } else {
                break
            }
        }
        return (cur + 1).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int getMaximumConsecutive(List<int> coins) {
    coins.sort();
    int reachable = 0;
    for (int v in coins) {
      if (v <= reachable + 1) {
        reachable += v;
      } else {
        break;
      }
    }
    return reachable + 1;
  }
}
```

## Golang

```go
package main

import "sort"

func getMaximumConsecutive(coins []int) int {
	sort.Ints(coins)
	cur := 0
	for _, v := range coins {
		if v <= cur+1 {
			cur += v
		} else {
			break
		}
	}
	return cur + 1
}
```

## Ruby

```ruby
def get_maximum_consecutive(coins)
  coins.sort!
  reach = 0
  coins.each do |v|
    break if v > reach + 1
    reach += v
  end
  reach + 1
end
```

## Scala

```scala
object Solution {
    def getMaximumConsecutive(coins: Array[Int]): Int = {
        java.util.Arrays.sort(coins)
        var reachable: Long = 0L
        for (c <- coins) {
            if (c.toLong <= reachable + 1) {
                reachable += c
            } else {
                return (reachable + 1).toInt
            }
        }
        (reachable + 1).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_maximum_consecutive(mut coins: Vec<i32>) -> i32 {
        coins.sort_unstable();
        let mut reach: i64 = 0;
        for &c in &coins {
            let v = c as i64;
            if v <= reach + 1 {
                reach += v;
            } else {
                break;
            }
        }
        (reach + 1) as i32
    }
}
```

## Racket

```racket
(define/contract (get-maximum-consecutive coins)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort coins <)))
    (let loop ((lst sorted) (reach 0))
      (if (null? lst)
          (+ reach 1)
          (let ((v (car lst)))
            (if (<= v (+ reach 1))
                (loop (cdr lst) (+ reach v))
                (+ reach 1)))))))
```

## Erlang

```erlang
-module(solution).
-export([get_maximum_consecutive/1]).

-spec get_maximum_consecutive(Coins :: [integer()]) -> integer().
get_maximum_consecutive(Coins) ->
    Sorted = lists:sort(Coins),
    MaxReach = max_reach(Sorted, 0),
    MaxReach + 1.

max_reach([], Cur) -> Cur;
max_reach([V|Rest], Cur) when V =< Cur + 1 ->
    max_reach(Rest, Cur + V);
max_reach(_, Cur) -> Cur.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_maximum_consecutive(coins :: [integer]) :: integer
  def get_maximum_consecutive(coins) do
    coins
    |> Enum.sort()
    |> Enum.reduce_while(0, fn coin, reachable ->
      if coin <= reachable + 1 do
        {:cont, reachable + coin}
      else
        {:halt, reachable}
      end
    end)
    |> Kernel.+(1)
  end
end
```
