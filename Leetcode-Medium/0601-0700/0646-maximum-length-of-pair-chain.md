# 0646. Maximum Length of Pair Chain

## Cpp

```cpp
class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        sort(pairs.begin(), pairs.end(),
             [](const vector<int>& a, const vector<int>& b) { return a[1] < b[1]; });
        int cnt = 0;
        int curEnd = INT_MIN;
        for (const auto& p : pairs) {
            if (p[0] > curEnd) {
                ++cnt;
                curEnd = p[1];
            }
        }
        return cnt;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a, b) -> Integer.compare(a[1], b[1]));
        int count = 0;
        int prevEnd = Integer.MIN_VALUE;
        for (int[] pair : pairs) {
            if (pair[0] > prevEnd) {
                count++;
                prevEnd = pair[1];
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # Greedy: sort by the right endpoint and pick non-overlapping intervals
        pairs.sort(key=lambda x: x[1])
        count = 0
        cur_end = -10**9  # smaller than any possible left value
        for left, right in pairs:
            if left > cur_end:
                count += 1
                cur_end = right
        return count
```

## Python3

```python
from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort pairs by their ending value to apply greedy selection
        pairs.sort(key=lambda x: x[1])
        cur_end = -10**9  # smaller than any possible left value
        chain_len = 0
        for left, right in pairs:
            if left > cur_end:
                chain_len += 1
                cur_end = right
        return chain_len
```

## C

```c
#include <limits.h>
#include <stdlib.h>

static int cmpPairs(const void *a, const void *b) {
    int *p1 = *(int **)a;
    int *p2 = *(int **)b;
    if (p1[1] != p2[1])
        return p1[1] - p2[1];
    return p1[0] - p2[0];
}

int findLongestChain(int** pairs, int pairsSize, int* pairsColSize) {
    if (pairsSize == 0) return 0;
    qsort(pairs, pairsSize, sizeof(int *), cmpPairs);
    int count = 0;
    int prev_end = INT_MIN;
    for (int i = 0; i < pairsSize; ++i) {
        if (pairs[i][0] > prev_end) {
            ++count;
            prev_end = pairs[i][1];
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int FindLongestChain(int[][] pairs) {
        if (pairs == null || pairs.Length == 0) return 0;
        System.Array.Sort(pairs, (a, b) => a[1].CompareTo(b[1]));
        int count = 0;
        int prevEnd = int.MinValue;
        foreach (var p in pairs) {
            if (p[0] > prevEnd) {
                count++;
                prevEnd = p[1];
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} pairs
 * @return {number}
 */
var findLongestChain = function(pairs) {
    // Sort pairs by their right endpoint (ascending)
    pairs.sort((a, b) => a[1] - b[1]);
    
    let count = 0;
    let prevEnd = -Infinity;
    
    for (const [left, right] of pairs) {
        if (left > prevEnd) {
            count++;
            prevEnd = right;
        }
    }
    
    return count;
};
```

## Typescript

```typescript
function findLongestChain(pairs: number[][]): number {
    pairs.sort((a, b) => a[1] - b[1]);
    let count = 0;
    let prevEnd = -Infinity;
    for (const [left, right] of pairs) {
        if (left > prevEnd) {
            count++;
            prevEnd = right;
        }
    }
    return count;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer[][] $pairs
     * @return Integer
     */
    function findLongestChain($pairs) {
        usort($pairs, function ($a, $b) {
            if ($a[1] == $b[1]) return 0;
            return ($a[1] < $b[1]) ? -1 : 1;
        });
        $count = 0;
        $prevEnd = PHP_INT_MIN;
        foreach ($pairs as $pair) {
            if ($pair[0] > $prevEnd) {
                $count++;
                $prevEnd = $pair[1];
            }
        }
        return $count;
    }
}
?>
```

## Swift

```swift
class Solution {
    func findLongestChain(_ pairs: [[Int]]) -> Int {
        let sortedPairs = pairs.sorted { $0[1] < $1[1] }
        var currentEnd = Int.min
        var chainLength = 0
        
        for pair in sortedPairs {
            if pair[0] > currentEnd {
                chainLength += 1
                currentEnd = pair[1]
            }
        }
        
        return chainLength
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findLongestChain(pairs: Array<IntArray>): Int {
        val sorted = pairs.sortedBy { it[1] }
        var count = 0
        var currentEnd = Int.MIN_VALUE
        for (pair in sorted) {
            if (pair[0] > currentEnd) {
                count++
                currentEnd = pair[1]
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int findLongestChain(List<List<int>> pairs) {
    // Sort the pairs based on their right endpoint
    pairs.sort((a, b) => a[1].compareTo(b[1]));
    
    int count = 0;
    int prevEnd = -1000000000; // sufficiently small sentinel
    
    for (var pair in pairs) {
      if (pair[0] > prevEnd) {
        count++;
        prevEnd = pair[1];
      }
    }
    
    return count;
  }
}
```

## Golang

```go
func findLongestChain(pairs [][]int) int {
    if len(pairs) == 0 {
        return 0
    }
    // Sort pairs by their second element (right endpoint)
    sort.Slice(pairs, func(i, j int) bool {
        return pairs[i][1] < pairs[j][1]
    })
    count := 1
    prevEnd := pairs[0][1]
    for i := 1; i < len(pairs); i++ {
        if pairs[i][0] > prevEnd {
            count++
            prevEnd = pairs[i][1]
        }
    }
    return count
}

import "sort"
```

## Ruby

```ruby
def find_longest_chain(pairs)
  sorted = pairs.sort_by { |pair| pair[1] }
  count = 0
  prev_end = -Float::INFINITY
  sorted.each do |left, right|
    if left > prev_end
      count += 1
      prev_end = right
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def findLongestChain(pairs: Array[Array[Int]]): Int = {
        val sorted = pairs.sortBy(_(1))
        var count = 0
        var prevEnd = Int.MinValue
        for (p <- sorted) {
            if (p(0) > prevEnd) {
                count += 1
                prevEnd = p(1)
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_longest_chain(mut pairs: Vec<Vec<i32>>) -> i32 {
        // Sort pairs by their right endpoint
        pairs.sort_by_key(|p| p[1]);
        let mut count: i32 = 0;
        let mut current_end = i32::MIN;
        for pair in pairs.iter() {
            if pair[0] > current_end {
                count += 1;
                current_end = pair[1];
            }
        }
        count
    }
}
```

## Racket

```racket
#lang racket

(define/contract (find-longest-chain pairs)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (if (null? pairs)
      0
      (let* ((sorted (sort pairs (lambda (a b) (< (second a) (second b)))))
             (first-pair (car sorted))
             (count 1)
             (current-end (second first-pair)))
        (for ([p (in-list (cdr sorted))])
          (when (> (first p) current-end)
            (set! count (+ count 1))
            (set! current-end (second p))))
        count)))
```

## Erlang

```erlang
-module(solution).
-export([find_longest_chain/1]).

-spec find_longest_chain(Pairs :: [[integer()]]) -> integer().
find_longest_chain(Pairs) ->
    PairsTuples = [ {L,R} || [L,R] <- Pairs ],
    Sorted = lists:keysort(2, PairsTuples),
    case Sorted of
        [] -> 0;
        [{_,R}|Rest] ->
            chain_len(Rest, R, 1)
    end.

-spec chain_len(list(), integer(), integer()) -> integer().
chain_len([], _End, Count) -> Count;
chain_len([{L,R}|Tail], End, Count) when L > End ->
    chain_len(Tail, R, Count + 1);
chain_len([_|Tail], End, Count) ->
    chain_len(Tail, End, Count).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_longest_chain(pairs :: [[integer]]) :: integer
  def find_longest_chain(pairs) do
    pairs
    |> Enum.sort_by(fn [_l, r] -> r end)
    |> Enum.reduce({-1_000_001, 0}, fn [l, r], {prev_end, cnt} ->
      if l > prev_end do
        {r, cnt + 1}
      else
        {prev_end, cnt}
      end
    end)
    |> elem(1)
  end
end
```
