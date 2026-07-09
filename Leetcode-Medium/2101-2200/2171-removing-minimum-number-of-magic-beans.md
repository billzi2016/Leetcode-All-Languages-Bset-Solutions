# 2171. Removing Minimum Number of Magic Beans

## Cpp

```cpp
class Solution {
public:
    long long minimumRemoval(vector<int>& beans) {
        int n = beans.size();
        sort(beans.begin(), beans.end());
        long long total = 0;
        for (int v : beans) total += v;
        long long maxKeep = 0;
        for (int i = 0; i < n; ++i) {
            long long keep = 1LL * beans[i] * (n - i);
            if (keep > maxKeep) maxKeep = keep;
        }
        return total - maxKeep;
    }
};
```

## Java

```java
class Solution {
    public long minimumRemoval(int[] beans) {
        int n = beans.length;
        java.util.Arrays.sort(beans);
        long total = 0L;
        for (int b : beans) total += b;
        long minRemoval = total; // case of removing all
        for (int i = 0; i < n; i++) {
            long keepCount = n - i;
            long removal = total - keepCount * (long) beans[i];
            if (removal < minRemoval) minRemoval = removal;
        }
        return minRemoval;
    }
}
```

## Python

```python
class Solution(object):
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        beans.sort()
        n = len(beans)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + beans[i]
        total = prefix[n]
        ans = total  # worst case: remove all
        for i in range(n):
            # make first i bags empty, reduce remaining to beans[i]
            removed = prefix[i] + (total - prefix[i] - beans[i] * (n - i))
            if removed < ans:
                ans = removed
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total = sum(beans)
        n = len(beans)
        max_keep = 0
        for i, v in enumerate(beans):
            keep = v * (n - i)
            if keep > max_keep:
                max_keep = keep
        return total - max_keep
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

long long minimumRemoval(int* beans, int beansSize) {
    if (beansSize == 0) return 0;
    qsort(beans, beansSize, sizeof(int), cmp_int);
    long long total = 0;
    for (int i = 0; i < beansSize; ++i) total += beans[i];
    long long best = 0;
    for (int i = 0; i < beansSize; ++i) {
        long long keep = (long long)(beansSize - i) * beans[i];
        if (keep > best) best = keep;
    }
    return total - best;
}
```

## Csharp

```csharp
public class Solution {
    public long MinimumRemoval(int[] beans) {
        Array.Sort(beans);
        long total = 0;
        foreach (int b in beans) total += b;
        long maxKept = 0;
        int n = beans.Length;
        for (int i = 0; i < n; i++) {
            long kept = (long)beans[i] * (n - i);
            if (kept > maxKept) maxKept = kept;
        }
        return total - maxKept;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} beans
 * @return {number}
 */
var minimumRemoval = function(beans) {
    const n = beans.length;
    beans.sort((a, b) => a - b);
    let total = 0;
    for (let v of beans) total += v;
    let ans = total; // worst case: remove all
    for (let i = 0; i < n; ++i) {
        const keep = (n - i) * beans[i];
        const removed = total - keep;
        if (removed < ans) ans = removed;
    }
    return ans;
};
```

## Typescript

```typescript
function minimumRemoval(beans: number[]): number {
    const n = beans.length;
    beans.sort((a, b) => a - b);
    let total = 0;
    for (const v of beans) total += v;
    let maxKept = 0;
    for (let i = 0; i < n; ++i) {
        const kept = (n - i) * beans[i];
        if (kept > maxKept) maxKept = kept;
    }
    return total - maxKept;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $beans
     * @return Integer
     */
    function minimumRemoval($beans) {
        sort($beans);
        $n = count($beans);
        $total = array_sum($beans);
        $ans = $total; // remove all beans
        
        for ($i = 0; $i < $n; ++$i) {
            $keep = ($n - $i) * $beans[$i];
            $removal = $total - $keep;
            if ($removal < $ans) {
                $ans = $removal;
            }
        }
        
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumRemoval(_ beans: [Int]) -> Int {
        let sorted = beans.sorted()
        var total: Int64 = 0
        for b in sorted { total += Int64(b) }
        var minRemoval = total
        let n = sorted.count
        for i in 0..<n {
            let target = Int64(sorted[i])
            let cnt = Int64(n - i)
            let kept = target * cnt
            let removal = total - kept
            if removal < minRemoval { minRemoval = removal }
        }
        return Int(minRemoval)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumRemoval(beans: IntArray): Long {
        val n = beans.size
        beans.sort()
        var total = 0L
        for (v in beans) total += v.toLong()
        var ans = total
        for (i in 0 until n) {
            val kept = (n - i).toLong()
            val candidate = total - kept * beans[i].toLong()
            if (candidate < ans) ans = candidate
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minimumRemoval(List<int> beans) {
    beans.sort();
    int n = beans.length;
    int total = 0;
    for (int b in beans) {
      total += b;
    }
    int minRemoval = total; // case: make all bags empty
    for (int i = 0; i < n; i++) {
      int keep = n - i;
      int removal = total - keep * beans[i];
      if (removal < minRemoval) {
        minRemoval = removal;
      }
    }
    return minRemoval;
  }
}
```

## Golang

```go
import "sort"

func minimumRemoval(beans []int) int64 {
	n := len(beans)
	sort.Ints(beans)

	prefix := make([]int64, n)
	var total int64
	for i, v := range beans {
		total += int64(v)
		if i == 0 {
			prefix[i] = int64(v)
		} else {
			prefix[i] = prefix[i-1] + int64(v)
		}
	}

	var maxKeep int64
	for i, v := range beans {
		t := int64(v)
		keep := prefix[i] + t*int64(n-i-1)
		if keep > maxKeep {
			maxKeep = keep
		}
	}
	return total - maxKeep
}
```

## Ruby

```ruby
def minimum_removal(beans)
  beans.sort!
  n = beans.size
  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = prefix[i] + beans[i] }
  total = prefix[n]
  ans = total
  (0...n).each do |i|
    suffix_len = n - i
    suffix_sum = total - prefix[i]
    removal = prefix[i] + (suffix_sum - beans[i] * suffix_len)
    ans = removal if removal < ans
  end
  ans
end
```

## Scala

```scala
object Solution {
    def minimumRemoval(beans: Array[Int]): Long = {
        val sorted = beans.sorted
        val n = sorted.length
        var total: Long = 0L
        for (b <- sorted) total += b.toLong
        var ans: Long = total
        for (i <- 0 until n) {
            val keep = (n - i).toLong * sorted(i).toLong
            val removed = total - keep
            if (removed < ans) ans = removed
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_removal(beans: Vec<i32>) -> i64 {
        let mut b = beans;
        b.sort_unstable();
        let n = b.len();
        let total: i64 = b.iter().map(|&x| x as i64).sum();
        let mut ans = total; // case where all bags become empty
        for (i, &val) in b.iter().enumerate() {
            let cnt = (n - i) as i64;
            let removed = total - cnt * val as i64;
            if removed < ans {
                ans = removed;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (minimum-removal beans)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort beans <))
         (n (length sorted))
         (total (foldl + 0 sorted)))
    (let loop ((lst sorted) (i 0) (best total))
      (if (null? lst)
          best
          (let* ((val (car lst))
                 (removed (- total (* (- n i) val))))
            (loop (cdr lst) (+ i 1) (min best removed)))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_removal/1]).

-spec minimum_removal(Beans :: [integer()]) -> integer().
minimum_removal(Beans) ->
    Sorted = lists:sort(Beans),
    Total = lists:foldl(fun(X, Acc) -> X + Acc end, 0, Sorted),
    Len = length(Sorted),
    compute_min(Sorted, Total, Len, 0, Total).

compute_min([], _Total, _Len, _Idx, Min) ->
    Min;
compute_min([V|Rest], Total, Len, Idx, Min) ->
    Count = Len - Idx,
    Removal = Total - Count * V,
    NewMin = if Removal < Min -> Removal; true -> Min end,
    compute_min(Rest, Total, Len, Idx + 1, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_removal(beans :: [integer]) :: integer
  def minimum_removal(beans) do
    sorted = Enum.sort(beans)
    total = Enum.sum(sorted)
    n = length(sorted)

    {ans, _} =
      Enum.with_index(sorted)
      |> Enum.reduce({total, nil}, fn {val, idx}, {best, _} ->
        keep = n - idx
        removal = total - keep * val

        if removal < best do
          {removal, nil}
        else
          {best, nil}
        end
      end)

    ans
  end
end
```
