# 0354. Russian Doll Envelopes

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        if (envelopes.empty()) return 0;
        sort(envelopes.begin(), envelopes.end(),
            [](const vector<int>& a, const vector<int>& b) {
                if (a[0] != b[0]) return a[0] < b[0];
                return a[1] > b[1]; // descending height for equal widths
            });
        vector<int> dp;
        dp.reserve(envelopes.size());
        for (const auto& env : envelopes) {
            int h = env[1];
            auto it = lower_bound(dp.begin(), dp.end(), h);
            if (it == dp.end())
                dp.push_back(h);
            else
                *it = h;
        }
        return static_cast<int>(dp.size());
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        if (envelopes == null || envelopes.length == 0) return 0;
        Arrays.sort(envelopes, (a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            return b[1] - a[1];
        });
        int n = envelopes.length;
        int[] tails = new int[n];
        int size = 0;
        for (int[] env : envelopes) {
            int h = env[1];
            int i = Arrays.binarySearch(tails, 0, size, h);
            if (i < 0) i = -i - 1;
            tails[i] = h;
            if (i == size) size++;
        }
        return size;
    }
}
```

## Python

```python
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        # Sort by width asc, height desc for equal widths
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        import bisect
        dp = []
        for _, h in envelopes:
            i = bisect.bisect_left(dp, h)
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h
        return len(dp)
```

## Python3

```python
from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        # Sort by width asc, height desc for equal widths
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis = []
        for _, h in envelopes:
            idx = bisect.bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h
        return len(lis)
```

## C

```c
#include <stdlib.h>

static int cmp(const void *a, const void *b) {
    const int *ea = *(const int **)a;
    const int *eb = *(const int **)b;
    if (ea[0] != eb[0]) return ea[0] - eb[0];
    return eb[1] - ea[1];  // descending height when widths are equal
}

int maxEnvelopes(int** envelopes, int envelopesSize, int* envelopesColSize) {
    if (envelopesSize == 0) return 0;
    
    qsort(envelopes, envelopesSize, sizeof(int *), cmp);
    
    int *tails = (int *)malloc(envelopesSize * sizeof(int));
    int len = 0;
    
    for (int i = 0; i < envelopesSize; ++i) {
        int h = envelopes[i][1];
        int l = 0, r = len;
        while (l < r) {
            int m = (l + r) / 2;
            if (tails[m] < h)
                l = m + 1;
            else
                r = m;
        }
        tails[l] = h;
        if (l == len) ++len;
    }
    
    free(tails);
    return len;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxEnvelopes(int[][] envelopes) {
        if (envelopes == null || envelopes.Length == 0) return 0;
        Array.Sort(envelopes, (a, b) => {
            if (a[0] != b[0]) return a[0].CompareTo(b[0]);
            // widths equal -> sort heights descending
            return b[1].CompareTo(a[1]);
        });

        List<int> lis = new List<int>();
        foreach (var env in envelopes) {
            int h = env[1];
            int idx = lis.BinarySearch(h);
            if (idx < 0) idx = ~idx;
            if (idx == lis.Count)
                lis.Add(h);
            else
                lis[idx] = h;
        }
        return lis.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} envelopes
 * @return {number}
 */
var maxEnvelopes = function(envelopes) {
    if (!envelopes || envelopes.length === 0) return 0;
    
    // Sort by width asc, height desc when widths are equal
    envelopes.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        return b[1] - a[1];
    });
    
    const dp = []; // tails of increasing subsequences on heights
    
    for (const [, h] of envelopes) {
        let left = 0, right = dp.length;
        while (left < right) {
            const mid = (left + right) >> 1;
            if (dp[mid] < h) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        if (left === dp.length) {
            dp.push(h);
        } else {
            dp[left] = h;
        }
    }
    
    return dp.length;
};
```

## Typescript

```typescript
function maxEnvelopes(envelopes: number[][]): number {
    if (envelopes.length === 0) return 0;
    envelopes.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        return b[1] - a[1]; // descending height for equal widths
    });
    const dp: number[] = [];
    for (const [, h] of envelopes) {
        let l = 0, r = dp.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (dp[m] < h) l = m + 1;
            else r = m;
        }
        if (l === dp.length) dp.push(h);
        else dp[l] = h;
    }
    return dp.length;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $envelopes
     * @return Integer
     */
    function maxEnvelopes($envelopes) {
        if (empty($envelopes)) {
            return 0;
        }

        usort($envelopes, function ($a, $b) {
            if ($a[0] == $b[0]) {
                // For equal widths, sort heights in descending order
                return $b[1] <=> $a[1];
            }
            return $a[0] <=> $b[0];
        });

        $tails = [];
        foreach ($envelopes as $env) {
            $h = $env[1];
            $left = 0;
            $right = count($tails);
            while ($left < $right) {
                $mid = intdiv($left + $right, 2);
                if ($tails[$mid] < $h) {
                    $left = $mid + 1;
                } else {
                    $right = $mid;
                }
            }
            if ($left == count($tails)) {
                $tails[] = $h;
            } else {
                $tails[$left] = $h;
            }
        }

        return count($tails);
    }
}
```

## Swift

```swift
class Solution {
    func maxEnvelopes(_ envelopes: [[Int]]) -> Int {
        if envelopes.isEmpty { return 0 }
        let sorted = envelopes.sorted {
            if $0[0] == $1[0] {
                return $0[1] > $1[1]
            } else {
                return $0[0] < $1[0]
            }
        }
        var dp = [Int]()
        for env in sorted {
            let h = env[1]
            var left = 0
            var right = dp.count
            while left < right {
                let mid = (left + right) / 2
                if dp[mid] < h {
                    left = mid + 1
                } else {
                    right = mid
                }
            }
            if left == dp.count {
                dp.append(h)
            } else {
                dp[left] = h
            }
        }
        return dp.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxEnvelopes(envelopes: Array<IntArray>): Int {
        if (envelopes.isEmpty()) return 0
        envelopes.sortWith(compareBy<IntArray> { it[0] }.thenByDescending { it[1] })
        val n = envelopes.size
        val tails = IntArray(n)
        var len = 0
        for (env in envelopes) {
            val h = env[1]
            var l = 0
            var r = len
            while (l < r) {
                val m = (l + r) ushr 1
                if (tails[m] < h) {
                    l = m + 1
                } else {
                    r = m
                }
            }
            tails[l] = h
            if (l == len) len++
        }
        return len
    }
}
```

## Dart

```dart
class Solution {
  int maxEnvelopes(List<List<int>> envelopes) {
    if (envelopes.isEmpty) return 0;
    envelopes.sort((a, b) {
      if (a[0] != b[0]) return a[0] - b[0];
      return b[1] - a[1];
    });
    List<int> dp = [];
    for (var env in envelopes) {
      int h = env[1];
      int l = 0, r = dp.length;
      while (l < r) {
        int m = (l + r) >> 1;
        if (dp[m] < h) {
          l = m + 1;
        } else {
          r = m;
        }
      }
      if (l == dp.length) {
        dp.add(h);
      } else {
        dp[l] = h;
      }
    }
    return dp.length;
  }
}
```

## Golang

```go
package main

import "sort"

func maxEnvelopes(envelopes [][]int) int {
	if len(envelopes) == 0 {
		return 0
	}
	sort.Slice(envelopes, func(i, j int) bool {
		if envelopes[i][0] == envelopes[j][0] {
			return envelopes[i][1] > envelopes[j][1]
		}
		return envelopes[i][0] < envelopes[j][0]
	})
	dp := make([]int, 0)
	for _, e := range envelopes {
		h := e[1]
		idx := sort.Search(len(dp), func(i int) bool { return dp[i] >= h })
		if idx == len(dp) {
			dp = append(dp, h)
		} else {
			dp[idx] = h
		}
	}
	return len(dp)
}
```

## Ruby

```ruby
def max_envelopes(envelopes)
  return 0 if envelopes.empty?
  envelopes.sort_by! { |w, h| [w, -h] }
  lis = []
  envelopes.each do |_, h|
    idx = lis.bsearch_index { |x| x >= h } || lis.length
    if idx == lis.length
      lis << h
    else
      lis[idx] = h
    end
  end
  lis.size
end
```

## Scala

```scala
object Solution {
  def maxEnvelopes(envelopes: Array[Array[Int]]): Int = {
    if (envelopes == null || envelopes.isEmpty) return 0

    val sorted = envelopes.sortWith { case (a, b) =>
      if (a(0) != b(0)) a(0) < b(0)
      else a(1) > b(1)
    }

    import scala.collection.mutable.ArrayBuffer
    val dp = ArrayBuffer.empty[Int]

    for (h <- sorted.map(_(1))) {
      var l = 0
      var r = dp.length
      while (l < r) {
        val m = (l + r) >>> 1
        if (dp(m) < h) l = m + 1 else r = m
      }
      if (l == dp.length) dp += h
      else dp(l) = h
    }

    dp.length
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_envelopes(envelopes: Vec<Vec<i32>>) -> i32 {
        let mut env = envelopes;
        if env.is_empty() {
            return 0;
        }
        env.sort_by(|a, b| {
            if a[0] != b[0] {
                a[0].cmp(&b[0])
            } else {
                b[1].cmp(&a[1]) // descending height when widths are equal
            }
        });
        let mut dp: Vec<i32> = Vec::new();
        for e in env.iter() {
            let h = e[1];
            match dp.binary_search(&h) {
                Ok(idx) => dp[idx] = h,
                Err(idx) => {
                    if idx == dp.len() {
                        dp.push(h);
                    } else {
                        dp[idx] = h;
                    }
                }
            }
        }
        dp.len() as i32
    }
}
```

## Racket

```racket
(define/contract (max-envelopes envelopes)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([sorted
          (sort envelopes
                (lambda (a b)
                  (let ([w1 (first a)] [h1 (second a)]
                        [w2 (first b)] [h2 (second b)])
                    (if (< w1 w2) #t
                        (if (> w1 w2) #f
                            (> h1 h2))))))]
         [heights (map second sorted)])
    (let ([n (length heights)]
          [tails (make-vector (length heights) 0)]
          [size 0])
      (for ([h heights])
        (let loop ([l 0] [r size])
          (if (= l r)
              (begin
                (vector-set! tails l h)
                (when (= l size) (set! size (+ size 1))))
              (let* ([mid (quotient (+ l r) 2)]
                     [midval (vector-ref tails mid)])
                (if (< midval h)
                    (loop (+ mid 1) r)
                    (loop l mid))))))
      size)))
```

## Erlang

```erlang
-spec max_envelopes(Envelopes :: [[integer()]]) -> integer().
max_envelopes(Envelopes) ->
    Sorted = lists:sort(fun compare/2, Envelopes),
    Heights = [H || [_W, H] <- Sorted],
    lis_length(Heights).

compare([W1, H1], [W2, H2]) ->
    case W1 =:= W2 of
        true -> H1 > H2;      % descending height when widths equal
        false -> W1 < W2
    end.

lis_length(Heights) ->
    {Len, _} = lists:foldl(
        fun(H, {CurLen, Tail}) ->
            case CurLen of
                0 ->
                    {1, array:set(0, H, Tail)};
                _ ->
                    Pos = binary_search(0, CurLen - 1, Tail, H),
                    if Pos == CurLen ->
                            NewTail = array:set(CurLen, H, Tail),
                            {CurLen + 1, NewTail};
                       true ->
                            NewTail = array:set(Pos, H, Tail),
                            {CurLen, NewTail}
                    end
            end
        end,
        {0, array:new()},
        Heights),
    Len.

binary_search(Low, High, Array, Target) when Low =< High ->
    Mid = (Low + High) bsr 1,
    Val = array:get(Mid, Array),
    if
        Val < Target ->
            binary_search(Mid + 1, High, Array, Target);
        true ->
            binary_search(Low, Mid - 1, Array, Target)
    end;
binary_search(Low, _High, _Array, _Target) -> Low.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_envelopes(envelopes :: [[integer]]) :: integer
  def max_envelopes(envelopes) do
    sorted = Enum.sort_by(envelopes, fn [w, h] -> {w, -h} end)
    heights = Enum.map(sorted, fn [_w, h] -> h end)

    {len, _arr} =
      Enum.reduce(heights, {0, :array.new()}, fn h, {len, arr} ->
        pos = lower_bound(arr, len, h)
        arr = :array.set(pos, h, arr)
        new_len = if pos == len, do: len + 1, else: len
        {new_len, arr}
      end)

    len
  end

  defp lower_bound(_arr, 0, _target), do: 0

  defp lower_bound(arr, len, target) do
    binary_search(arr, 0, len - 1, target)
  end

  defp binary_search(_arr, low, high, _target) when low > high, do: low

  defp binary_search(arr, low, high, target) do
    mid = div(low + high, 2)
    val = :array.get(mid, arr)

    if val < target do
      binary_search(arr, mid + 1, high, target)
    else
      binary_search(arr, low, mid - 1, target)
    end
  end
end
```
