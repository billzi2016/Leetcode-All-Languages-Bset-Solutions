# 1561. Maximum Number of Coins You Can Get

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxCoins(vector<int>& piles) {
        sort(piles.begin(), piles.end());
        int n = piles.size() / 3;
        long long ans = 0;
        for (int i = n; i < (int)piles.size(); i += 2) {
            ans += piles[i];
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int maxCoins(int[] piles) {
        java.util.Arrays.sort(piles);
        int n = piles.length / 3;
        int ans = 0;
        for (int i = n; i < piles.length; i += 2) {
            ans += piles[i];
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n = len(piles) // 3
        ans = 0
        # sum every second element starting from index n
        for i in range(n, len(piles), 2):
            ans += piles[i]
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        ans = 0
        for i in range(n, len(piles), 2):
            ans += piles[i]
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int maxCoins(int* piles, int pilesSize) {
    qsort(piles, (size_t)pilesSize, sizeof(int), cmp);
    int n = pilesSize / 3;
    long long ans = 0;
    for (int i = n; i < pilesSize; i += 2) {
        ans += piles[i];
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxCoins(int[] piles)
    {
        Array.Sort(piles);
        int n = piles.Length / 3;
        long ans = 0;
        for (int i = n; i < piles.Length; i += 2)
        {
            ans += piles[i];
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} piles
 * @return {number}
 */
var maxCoins = function(piles) {
    const n = piles.length / 3;
    piles.sort((a, b) => a - b);
    let ans = 0;
    for (let i = n; i < piles.length; i += 2) {
        ans += piles[i];
    }
    return ans;
};
```

## Typescript

```typescript
function maxCoins(piles: number[]): number {
    piles.sort((a, b) => a - b);
    const n = piles.length / 3;
    let ans = 0;
    for (let i = n; i < piles.length; i += 2) {
        ans += piles[i];
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $piles
     * @return Integer
     */
    function maxCoins($piles) {
        sort($piles);
        $len = count($piles);
        $n = intdiv($len, 3);
        $ans = 0;
        for ($i = $n; $i < $len; $i += 2) {
            $ans += $piles[$i];
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxCoins(_ piles: [Int]) -> Int {
        let sorted = piles.sorted()
        let n = sorted.count / 3
        var ans = 0
        var i = n
        while i < sorted.count {
            ans += sorted[i]
            i += 2
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxCoins(piles: IntArray): Int {
        piles.sort()
        val n = piles.size / 3
        var ans = 0
        var i = n
        while (i < piles.size) {
            ans += piles[i]
            i += 2
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxCoins(List<int> piles) {
    piles.sort();
    int n = piles.length ~/ 3;
    int ans = 0;
    for (int i = n; i < piles.length; i += 2) {
      ans += piles[i];
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "sort"

func maxCoins(piles []int) int {
	sort.Ints(piles)
	n := len(piles) / 3
	ans := 0
	for i := n; i < len(piles); i += 2 {
		ans += piles[i]
	}
	return ans
}
```

## Ruby

```ruby
def max_coins(piles)
  piles.sort!
  n = piles.length / 3
  ans = 0
  i = n
  while i < piles.length
    ans += piles[i]
    i += 2
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maxCoins(piles: Array[Int]): Int = {
        java.util.Arrays.sort(piles)
        val n = piles.length / 3
        var sum: Long = 0L
        var i = n
        while (i < piles.length) {
            sum += piles(i)
            i += 2
        }
        sum.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_coins(mut piles: Vec<i32>) -> i32 {
        piles.sort();
        let n = piles.len() / 3;
        let mut ans: i64 = 0;
        for i in (n..piles.len()).step_by(2) {
            ans += piles[i] as i64;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (max-coins piles)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort piles <))
         (vec (list->vector sorted))
         (len (vector-length vec))
         (n (/ len 3)))
    (let loop ((i n) (acc 0))
      (if (>= i len)
          acc
          (loop (+ i 2) (+ acc (vector-ref vec i)))))))
```

## Erlang

```erlang
-module(solution).
-export([max_coins/1]).

-spec max_coins(Piles :: [integer()]) -> integer().
max_coins(Piles) ->
    Sorted = lists:sort(Piles),
    N = length(Piles) div 3,
    Rest = lists:nthtail(N, Sorted),
    sum_even(Rest).

sum_even([]) -> 0;
sum_even([H|T]) ->
    H + sum_skip(T).

sum_skip([]) -> 0;
sum_skip([_|T]) -> sum_even(T).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_coins(piles :: [integer]) :: integer
  def max_coins(piles) do
    sorted = Enum.sort(piles)
    n = div(length(piles), 3)

    sorted
    |> Enum.with_index()
    |> Enum.reduce(0, fn {val, idx}, acc ->
      if idx >= n and rem(idx - n, 2) == 0 do
        acc + val
      else
        acc
      end
    end)
  end
end
```
