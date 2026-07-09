# 2554. Maximum Number of Integers to Choose From a Range I

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxCount(vector<int>& banned, int n, int maxSum) {
        unordered_set<int> ban(banned.begin(), banned.end());
        long long remaining = maxSum;
        int cnt = 0;
        for (int i = 1; i <= n; ++i) {
            if (ban.count(i)) continue;
            if (remaining < i) break;
            remaining -= i;
            ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int maxCount(int[] banned, int n, int maxSum) {
        boolean[] isBanned = new boolean[n + 1];
        for (int b : banned) {
            if (b <= n) {
                isBanned[b] = true;
            }
        }
        int count = 0;
        for (int i = 1; i <= n && maxSum >= i; i++) {
            if (!isBanned[i]) {
                maxSum -= i;
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        banned_set = set(banned)
        count = 0
        for i in range(1, n + 1):
            if i in banned_set:
                continue
            if maxSum < i:
                break
            maxSum -= i
            count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        count = 0
        for i in range(1, n + 1):
            if i in banned_set:
                continue
            if i > maxSum:
                break
            maxSum -= i
            count += 1
        return count
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

int maxCount(int* banned, int bannedSize, int n, int maxSum) {
    bool *isBanned = (bool *)calloc(n + 1, sizeof(bool));
    for (int i = 0; i < bannedSize; ++i) {
        if (banned[i] <= n) {
            isBanned[banned[i]] = true;
        }
    }

    long long remaining = maxSum;
    int count = 0;
    for (int i = 1; i <= n; ++i) {
        if (!isBanned[i]) {
            if (remaining < i) break;
            remaining -= i;
            ++count;
        }
    }

    free(isBanned);
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxCount(int[] banned, int n, int maxSum)
    {
        var bannedSet = new HashSet<int>(banned);
        long remaining = maxSum;
        int count = 0;

        for (int i = 1; i <= n; i++)
        {
            if (bannedSet.Contains(i))
                continue;

            if (remaining < i)
                break;

            remaining -= i;
            count++;
        }

        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} banned
 * @param {number} n
 * @param {number} maxSum
 * @return {number}
 */
var maxCount = function(banned, n, maxSum) {
    const bannedSet = new Set(banned);
    let count = 0;
    for (let i = 1; i <= n && maxSum >= i; i++) {
        if (bannedSet.has(i)) continue;
        maxSum -= i;
        count++;
    }
    return count;
};
```

## Typescript

```typescript
function maxCount(banned: number[], n: number, maxSum: number): number {
    const bannedSet = new Set<number>(banned);
    let count = 0;
    for (let i = 1; i <= n; ++i) {
        if (bannedSet.has(i)) continue;
        if (maxSum < i) break;
        maxSum -= i;
        ++count;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $banned
     * @param Integer $n
     * @param Integer $maxSum
     * @return Integer
     */
    function maxCount($banned, $n, $maxSum) {
        // Build a hash set of banned numbers for O(1) lookups.
        $bannedSet = array_flip($banned);
        $count = 0;
        for ($i = 1; $i <= $n; $i++) {
            if (isset($bannedSet[$i])) {
                continue;
            }
            if ($maxSum < $i) {
                break;
            }
            $maxSum -= $i;
            $count++;
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func maxCount(_ banned: [Int], _ n: Int, _ maxSum: Int) -> Int {
        let bannedSet = Set(banned)
        var remaining = maxSum
        var count = 0
        for i in 1...n {
            if bannedSet.contains(i) { continue }
            if remaining < i { break }
            remaining -= i
            count += 1
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxCount(banned: IntArray, n: Int, maxSum: Int): Int {
        val bannedSet = HashSet<Int>()
        for (b in banned) {
            if (b <= n) bannedSet.add(b)
        }
        var remaining = maxSum
        var count = 0
        var i = 1
        while (i <= n && remaining >= i) {
            if (!bannedSet.contains(i)) {
                remaining -= i
                count++
            }
            i++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int maxCount(List<int> banned, int n, int maxSum) {
    final Set<int> bannedSet = {};
    for (int b in banned) {
      if (b <= n) bannedSet.add(b);
    }
    int count = 0;
    for (int i = 1; i <= n && maxSum >= i; ++i) {
      if (bannedSet.contains(i)) continue;
      maxSum -= i;
      count++;
    }
    return count;
  }
}
```

## Golang

```go
func maxCount(banned []int, n int, maxSum int) int {
	bannedSet := make(map[int]struct{}, len(banned))
	for _, v := range banned {
		if v <= n {
			bannedSet[v] = struct{}{}
		}
	}
	count := 0
	for i := 1; i <= n && maxSum >= i; i++ {
		if _, ok := bannedSet[i]; ok {
			continue
		}
		maxSum -= i
		count++
	}
	return count
}
```

## Ruby

```ruby
require 'set'

def max_count(banned, n, max_sum)
  banned_set = Set.new(banned)
  count = 0
  (1..n).each do |i|
    break if max_sum < i
    next if banned_set.include?(i)
    max_sum -= i
    count += 1
  end
  count
end
```

## Scala

```scala
object Solution {
    def maxCount(banned: Array[Int], n: Int, maxSum: Int): Int = {
        val bannedSet = banned.toSet
        var remaining = maxSum.toLong
        var count = 0
        var i = 1
        while (i <= n && remaining >= i) {
            if (!bannedSet.contains(i)) {
                remaining -= i
                count += 1
            }
            i += 1
        }
        count
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn max_count(banned: Vec<i32>, n: i32, max_sum: i32) -> i32 {
        let banned_set: HashSet<i32> = banned.into_iter().collect();
        let mut remaining = max_sum as i64;
        let mut count = 0i32;
        for i in 1..=n {
            if banned_set.contains(&i) {
                continue;
            }
            if remaining < i as i64 {
                break;
            }
            remaining -= i as i64;
            count += 1;
        }
        count
    }
}
```

## Racket

```racket
(require racket/set)

(define/contract (max-count banned n maxSum)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ((banned-set (list->set banned))
         (cnt 0)
         (remaining maxSum))
    (for ([i (in-range 1 (+ n 1))])
      (when (and (not (set-member? banned-set i))
                 (>= remaining i))
        (set! remaining (- remaining i))
        (set! cnt (+ cnt 1))))
    cnt))
```

## Erlang

```erlang
-module(solution).
-export([max_count/3]).

-spec max_count(Banned :: [integer()], N :: integer(), MaxSum :: integer()) -> integer().
max_count(Banned, N, MaxSum) ->
    BSet = maps:from_list([{X, true} || X <- Banned]),
    max_count_loop(1, N, MaxSum, BSet, 0).

max_count_loop(I, N, _Rem, _BSet, Count) when I > N ->
    Count;
max_count_loop(I, N, Rem, BSet, Count) ->
    case maps:is_key(I, BSet) of
        true ->
            max_count_loop(I + 1, N, Rem, BSet, Count);
        false ->
            if Rem >= I ->
                    max_count_loop(I + 1, N, Rem - I, BSet, Count + 1);
               true ->
                    Count
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_count(banned :: [integer], n :: integer, max_sum :: integer) :: integer
  def max_count(banned, n, max_sum) do
    banned_set = MapSet.new(banned)

    {count, _} =
      Enum.reduce_while(1..n, {0, max_sum}, fn i, {cnt, remaining} ->
        if MapSet.member?(banned_set, i) do
          {:cont, {cnt, remaining}}
        else
          if remaining >= i do
            {:cont, {cnt + 1, remaining - i}}
          else
            {:halt, {cnt, remaining}}
          end
        end
      end)

    count
  end
end
```
