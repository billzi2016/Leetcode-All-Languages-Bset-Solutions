# 2607. Make K-Subarray Sums Equal

## Cpp

```cpp
class Solution {
public:
    long long makeSubKSumEqual(vector<int>& arr, int k) {
        int n = arr.size();
        int g = std::gcd(n, k);
        vector<vector<int>> groups(g);
        for (int i = 0; i < n; ++i) {
            groups[i % g].push_back(arr[i]);
        }
        long long ans = 0;
        for (auto& v : groups) {
            sort(v.begin(), v.end());
            int median = v[v.size() / 2];
            for (int x : v) {
                ans += llabs((long long)x - median);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long makeSubKSumEqual(int[] arr, int k) {
        int n = arr.length;
        int g = gcd(n, k);
        @SuppressWarnings("unchecked")
        java.util.ArrayList<Integer>[] groups = new java.util.ArrayList[g];
        for (int i = 0; i < g; i++) groups[i] = new java.util.ArrayList<>();
        for (int i = 0; i < n; i++) {
            groups[i % g].add(arr[i]);
        }
        long total = 0L;
        for (java.util.ArrayList<Integer> list : groups) {
            java.util.Collections.sort(list);
            int median = list.get(list.size() / 2);
            for (int val : list) {
                total += Math.abs((long) val - median);
            }
        }
        return total;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Python

```python
import math

class Solution(object):
    def makeSubKSumEqual(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        g = math.gcd(n, k)
        total_ops = 0
        for start in range(g):
            group = []
            i = start
            while i < n:
                group.append(arr[i])
                i += g
            group.sort()
            median = group[len(group) // 2]
            total_ops += sum(abs(x - median) for x in group)
        return total_ops
```

## Python3

```python
import math
from typing import List

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        g = math.gcd(n, k)
        total_ops = 0
        for start in range(g):
            group = []
            i = start
            while i < n:
                group.append(arr[i])
                i += g
            group.sort()
            median = group[len(group) // 2]
            total_ops += sum(abs(x - median) for x in group)
        return total_ops
```

## C

```c
#include <stdlib.h>
#include <stddef.h>

static int gcd_int(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

/* LeetCode entry point */
long long makeSubKSumEqual(int* arr, int arrSize, int k) {
    int n = arrSize;
    int g = gcd_int(n, k);
    
    /* count elements per group */
    int *cnt = (int *)calloc(g, sizeof(int));
    for (int i = 0; i < n; ++i) {
        cnt[i % g]++;
    }
    
    /* allocate storage for groups */
    int **group = (int **)malloc(g * sizeof(int *));
    for (int r = 0; r < g; ++r) {
        group[r] = (int *)malloc(cnt[r] * sizeof(int));
    }
    
    /* fill groups */
    int *pos = (int *)calloc(g, sizeof(int));
    for (int i = 0; i < n; ++i) {
        int r = i % g;
        group[r][pos[r]++] = arr[i];
    }
    
    long long ans = 0LL;
    for (int r = 0; r < g; ++r) {
        int sz = cnt[r];
        if (sz <= 1) continue;
        qsort(group[r], sz, sizeof(int), cmp_int);
        int median = group[r][sz / 2];
        for (int i = 0; i < sz; ++i) {
            long long diff = (long long)group[r][i] - (long long)median;
            if (diff < 0) diff = -diff;
            ans += diff;
        }
    }
    
    /* clean up */
    for (int r = 0; r < g; ++r) {
        free(group[r]);
    }
    free(group);
    free(cnt);
    free(pos);
    
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public long MakeSubKSumEqual(int[] arr, int k)
    {
        int n = arr.Length;
        int g = Gcd(n, k);
        long total = 0;

        for (int start = 0; start < g; ++start)
        {
            var group = new List<int>();
            int idx = start;
            do
            {
                group.Add(arr[idx]);
                idx = (idx + k) % n;
            } while (idx != start);

            group.Sort();
            int median = group[group.Count / 2];
            foreach (int val in group)
            {
                total += Math.Abs((long)val - median);
            }
        }

        return total;
    }

    private int Gcd(int a, int b)
    {
        while (b != 0)
        {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var makeSubKSumEqual = function(arr, k) {
    const n = arr.length;
    const g = gcd(n, k);
    let ans = 0;
    for (let start = 0; start < g; ++start) {
        const group = [];
        for (let i = start; i < n; i += g) {
            group.push(arr[i]);
        }
        group.sort((a, b) => a - b);
        const median = group[Math.floor(group.length / 2)];
        for (const v of group) {
            ans += Math.abs(v - median);
        }
    }
    return ans;
};

function gcd(a, b) {
    while (b !== 0) {
        const t = a % b;
        a = b;
        b = t;
    }
    return a;
}
```

## Typescript

```typescript
function makeSubKSumEqual(arr: number[], k: number): number {
    const n = arr.length;
    const g = gcd(n, k);
    let total = 0;

    for (let start = 0; start < g; ++start) {
        const group: number[] = [];
        let idx = start;
        while (true) {
            group.push(arr[idx]);
            idx = (idx + k) % n;
            if (idx === start) break;
        }
        group.sort((a, b) => a - b);
        const median = group[Math.floor(group.length / 2)];
        for (const v of group) {
            total += Math.abs(v - median);
        }
    }

    return total;
}

function gcd(a: number, b: number): number {
    while (b !== 0) {
        const t = a % b;
        a = b;
        b = t;
    }
    return a;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function makeSubKSumEqual($arr, $k) {
        $n = count($arr);
        $g = $this->gcd($n, $k);
        $total = 0;
        for ($start = 0; $start < $g; $start++) {
            $group = [];
            for ($i = $start; $i < $n; $i += $g) {
                $group[] = $arr[$i];
            }
            sort($group);
            $m = count($group);
            $median = $group[intval($m / 2)];
            foreach ($group as $v) {
                $total += abs($v - $median);
            }
        }
        return $total;
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }
}
```

## Swift

```swift
class Solution {
    func makeSubKSumEqual(_ arr: [Int], _ k: Int) -> Int {
        let n = arr.count
        let g = gcd(n, k)
        var total: Int64 = 0
        
        for r in 0..<g {
            var group = [Int]()
            var i = r
            while i < n {
                group.append(arr[i])
                i += g
            }
            group.sort()
            let median = group[group.count / 2]
            for v in group {
                total += Int64(abs(v - median))
            }
        }
        return Int(total)
    }
    
    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a
        var y = b
        while y != 0 {
            let temp = x % y
            x = y
            y = temp
        }
        return x
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun makeSubKSumEqual(arr: IntArray, k: Int): Long {
        val n = arr.size
        val g = gcd(n, k)
        var ans = 0L
        for (start in 0 until g) {
            val group = mutableListOf<Int>()
            var idx = start
            while (idx < n) {
                group.add(arr[idx])
                idx += g
            }
            group.sort()
            val median = group[group.size / 2]
            for (v in group) {
                ans += kotlin.math.abs(v - median).toLong()
            }
        }
        return ans
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return x
    }
}
```

## Dart

```dart
class Solution {
  int makeSubKSumEqual(List<int> arr, int k) {
    int n = arr.length;
    int g = _gcd(n, k);
    int ans = 0;
    for (int start = 0; start < g; ++start) {
      List<int> group = [];
      for (int i = start; i < n; i += g) {
        group.add(arr[i]);
      }
      group.sort();
      int median = group[group.length ~/ 2];
      for (int v in group) {
        ans += (v - median).abs();
      }
    }
    return ans;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int t = a % b;
      a = b;
      b = t;
    }
    return a;
  }
}
```

## Golang

```go
import "sort"

func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}

func makeSubKSumEqual(arr []int, k int) int64 {
    n := len(arr)
    d := gcd(n, k)

    var ans int64 = 0

    for r := 0; r < d; r++ {
        group := make([]int, 0, n/d+1)
        for i := r; i < n; i += d {
            group = append(group, arr[i])
        }
        sort.Ints(group)
        median := group[len(group)/2]
        for _, v := range group {
            diff := int64(v - median)
            if diff < 0 {
                diff = -diff
            }
            ans += diff
        }
    }

    return ans
}
```

## Ruby

```ruby
def make_sub_k_sum_equal(arr, k)
  n = arr.length
  g = n.gcd(k)
  group_len = n / g
  ans = 0

  (0...g).each do |start|
    vals = []
    idx = start
    group_len.times do
      vals << arr[idx]
      idx += g
    end
    vals.sort!
    median = vals[group_len / 2]
    vals.each { |v| ans += (v - median).abs }
  end

  ans
end
```

## Scala

```scala
object Solution {
  private def gcd(a: Int, b: Int): Int = {
    var x = a
    var y = b
    while (y != 0) {
      val t = x % y
      x = y
      y = t
    }
    x
  }

  def makeSubKSumEqual(arr: Array[Int], k: Int): Long = {
    val n = arr.length
    val d = gcd(n, k)
    var total: Long = 0L

    for (r <- 0 until d) {
      val buf = scala.collection.mutable.ArrayBuffer.empty[Int]
      var i = r
      while (i < n) {
        buf += arr(i)
        i += d
      }
      val sorted = buf.sorted
      val median = sorted(sorted.length / 2)
      var sum: Long = 0L
      for (v <- sorted) {
        sum += math.abs(v.toLong - median.toLong)
      }
      total += sum
    }

    total
  }
}
```

## Rust

```rust
impl Solution {
    pub fn make_sub_k_sum_equal(arr: Vec<i32>, k: i32) -> i64 {
        fn gcd(mut a: usize, mut b: usize) -> usize {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }

        let n = arr.len();
        let g = gcd(n, k as usize);
        let mut ans: i64 = 0;

        for r in 0..g {
            let mut group: Vec<i64> = Vec::new();
            let mut idx = r;
            while idx < n {
                group.push(arr[idx] as i64);
                idx += g;
            }
            group.sort_unstable();
            let median = group[group.len() / 2];
            for &v in &group {
                ans += (v - median).abs();
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (make-sub-k-sum-equal arr k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length arr))
         (g (gcd n k))
         (groups (make-vector g '())))
    ;; distribute elements into groups based on index modulo g
    (for ([i (in-range n)])
      (let* ((r (remainder i g))
             (old (vector-ref groups r)))
        (vector-set! groups r (cons (list-ref arr i) old))))
    ;; compute minimal operations for each group
    (let loop ((idx 0) (total 0))
      (if (= idx g)
          total
          (let* ((lst (vector-ref groups idx))
                 (sorted (sort lst <))
                 (len (length sorted))
                 (median (list-ref sorted (quotient len 2)))
                 (ops (apply + (map (lambda (x) (abs (- x median))) sorted))))
            (loop (+ idx 1) (+ total ops)))))))
```

## Erlang

```erlang
-module(solution).
-export([make_sub_k_sum_equal/2]).

-spec make_sub_k_sum_equal(Arr :: [integer()], K :: integer()) -> integer().
make_sub_k_sum_equal(Arr, K) ->
    N = length(Arr),
    G = gcd(N, K),
    GroupsMap = build_groups(Arr, G),
    maps:fold(fun(_Idx, List, Acc) -> Acc + group_cost(List) end,
              0,
              GroupsMap).

gcd(A, B) when B == 0 -> A;
gcd(A, B) -> gcd(B, A rem B).

build_groups(Arr, G) ->
    build_groups(Arr, G, 0, #{}).

build_groups([], _G, _Idx, Map) -> Map;
build_groups([V|Rest], G, Idx, Map) ->
    GroupIdx = Idx rem G,
    NewMap = maps:update_with(GroupIdx,
                              fun(L) -> [V|L] end,
                              [V],
                              Map),
    build_groups(Rest, G, Idx + 1, NewMap).

group_cost(Values) ->
    Sorted = lists:sort(Values),
    Len = length(Sorted),
    MedianIdx = Len div 2,
    Median = lists:nth(MedianIdx + 1, Sorted),
    diff_sum(Values, Median, 0).

diff_sum([], _M, Acc) -> Acc;
diff_sum([V|Rest], M, Acc) ->
    diff_sum(Rest, M, Acc + erlang:abs(V - M)).
```

## Elixir

```elixir
defmodule Solution do
  @spec make_sub_k_sum_equal(arr :: [integer], k :: integer) :: integer
  def make_sub_k_sum_equal(arr, k) do
    n = length(arr)
    g = Integer.gcd(n, k)

    groups = Enum.map(0..(g - 1), fn _ -> [] end)

    groups =
      Enum.reduce(Enum.with_index(arr), groups, fn {val, idx}, acc ->
        id = rem(idx, g)
        List.update_at(acc, id, fn list -> [val | list] end)
      end)

    Enum.reduce(groups, 0, fn group_vals, total ->
      sorted = Enum.sort(group_vals)
      len = length(sorted)
      median = Enum.at(sorted, div(len, 2))

      cost =
        Enum.reduce(sorted, 0, fn v, acc -> acc + abs(v - median) end)

      total + cost
    end)
  end
end
```
