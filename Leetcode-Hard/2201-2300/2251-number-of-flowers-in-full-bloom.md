# 2251. Number of Flowers in Full Bloom

## Cpp

```cpp
class Solution {
public:
    vector<int> fullBloomFlowers(vector<vector<int>>& flowers, vector<int>& people) {
        int n = flowers.size();
        vector<int> starts;
        vector<int> ends;
        starts.reserve(n);
        ends.reserve(n);
        for (auto &f : flowers) {
            starts.push_back(f[0]);
            // store end+1 to simplify counting
            ends.push_back(f[1] + 1);
        }
        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());
        
        vector<int> ans;
        ans.reserve(people.size());
        for (int t : people) {
            int started = upper_bound(starts.begin(), starts.end(), t) - starts.begin();
            int ended   = upper_bound(ends.begin(), ends.end(), t) - ends.begin();
            ans.push_back(started - ended);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] fullBloomFlowers(int[][] flowers, int[] people) {
        int n = flowers.length;
        long[] starts = new long[n];
        long[] ends = new long[n];
        for (int i = 0; i < n; i++) {
            starts[i] = flowers[i][0];
            ends[i] = (long) flowers[i][1] + 1L;
        }
        java.util.Arrays.sort(starts);
        java.util.Arrays.sort(ends);
        int m = people.length;
        int[] ans = new int[m];
        for (int i = 0; i < m; i++) {
            long t = people[i];
            int started = upperBound(starts, t);
            int ended = upperBound(ends, t);
            ans[i] = started - ended;
        }
        return ans;
    }

    private int upperBound(long[] arr, long target) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
```

## Python

```python
class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """
        starts = []
        ends = []
        for s, e in flowers:
            starts.append(s)
            ends.append(e + 1)  # flower stops being visible after end
        starts.sort()
        ends.sort()
        import bisect
        result = []
        for p in people:
            started = bisect.bisect_right(starts, p)
            ended = bisect.bisect_right(ends, p)
            result.append(started - ended)
        return result
```

## Python3

```python
from typing import List
import bisect

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = []
        ends = []
        for s, e in flowers:
            starts.append(s)
            ends.append(e + 1)
        starts.sort()
        ends.sort()
        result = []
        for p in people:
            started = bisect.bisect_right(starts, p)
            finished = bisect.bisect_right(ends, p)
            result.append(started - finished)
        return result
```

## C

```c
#include <stdlib.h>

/* Comparator for qsort (ascending order) */
static int cmp_int(const void *a, const void *b) {
    int av = *(const int *)a;
    int bv = *(const int *)b;
    return (av > bv) - (av < bv);
}

/* Upper bound: first index where arr[idx] > target */
static int upperBound(int *arr, int n, int target) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (arr[m] <= target)
            l = m + 1;
        else
            r = m;
    }
    return l;   // number of elements <= target
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* fullBloomFlowers(int** flowers, int flowersSize, int* flowersColSize,
                      int* people, int peopleSize, int* returnSize) {
    int n = flowersSize;
    int *starts = (int *)malloc(n * sizeof(int));
    int *ends   = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; ++i) {
        starts[i] = flowers[i][0];
        ends[i]   = flowers[i][1] + 1;   // end+1 to simplify counting
    }

    qsort(starts, n, sizeof(int), cmp_int);
    qsort(ends,   n, sizeof(int), cmp_int);

    int *ans = (int *)malloc(peopleSize * sizeof(int));
    for (int i = 0; i < peopleSize; ++i) {
        int t = people[i];
        int started = upperBound(starts, n, t); // flowers with start <= t
        int finished = upperBound(ends,   n, t); // flowers with end+1 <= t
        ans[i] = started - finished;
    }

    free(starts);
    free(ends);

    *returnSize = peopleSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] FullBloomFlowers(int[][] flowers, int[] people)
    {
        int n = flowers.Length;
        int[] starts = new int[n];
        int[] ends = new int[n];
        for (int i = 0; i < n; i++)
        {
            starts[i] = flowers[i][0];
            // store end + 1 to simplify counting finished blooms
            long ep1 = (long)flowers[i][1] + 1;
            ends[i] = (int)ep1;
        }

        Array.Sort(starts);
        Array.Sort(ends);

        int m = people.Length;
        int[] ans = new int[m];
        for (int i = 0; i < m; i++)
        {
            int t = people[i];
            int started = UpperBound(starts, t); // flowers with start <= t
            int ended = UpperBound(ends, t);     // flowers with end < t
            ans[i] = started - ended;
        }

        return ans;
    }

    private int UpperBound(int[] arr, int target)
    {
        int lo = 0, hi = arr.Length;
        while (lo < hi)
        {
            int mid = lo + ((hi - lo) >> 1);
            if (arr[mid] <= target)
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} flowers
 * @param {number[]} people
 * @return {number[]}
 */
var fullBloomFlowers = function(flowers, people) {
    const n = flowers.length;
    const starts = new Array(n);
    const ends = new Array(n);
    for (let i = 0; i < n; ++i) {
        starts[i] = flowers[i][0];
        ends[i] = flowers[i][1] + 1; // use end+1 to simplify counting
    }
    starts.sort((a, b) => a - b);
    ends.sort((a, b) => a - b);

    const upperBound = (arr, target) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] <= target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };

    const ans = new Array(people.length);
    for (let i = 0; i < people.length; ++i) {
        const t = people[i];
        const started = upperBound(starts, t); // flowers with start <= t
        const ended   = upperBound(ends, t);   // flowers with end+1 <= t => already finished
        ans[i] = started - ended;
    }
    return ans;
};
```

## Typescript

```typescript
function fullBloomFlowers(flowers: number[][], people: number[]): number[] {
    const n = flowers.length;
    const starts: number[] = new Array(n);
    const ends: number[] = new Array(n);
    for (let i = 0; i < n; i++) {
        starts[i] = flowers[i][0];
        ends[i] = flowers[i][1] + 1;
    }
    starts.sort((a, b) => a - b);
    ends.sort((a, b) => a - b);

    const upperBound = (arr: number[], target: number): number => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >>> 1;
            if (arr[mid] <= target) lo = mid + 1;
            else hi = mid;
        }
        return lo; // count of elements <= target
    };

    const ans: number[] = new Array(people.length);
    for (let i = 0; i < people.length; i++) {
        const t = people[i];
        const started = upperBound(starts, t);
        const ended = upperBound(ends, t);
        ans[i] = started - ended;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $flowers
     * @param Integer[] $people
     * @return Integer[]
     */
    function fullBloomFlowers($flowers, $people) {
        $starts = [];
        $ends = [];

        foreach ($flowers as $f) {
            $s = $f[0];
            $e = $f[1];
            $starts[] = $s;
            // store end+1 to simplify inclusive range handling
            $ends[] = $e + 1;
        }

        sort($starts);
        sort($ends);

        $nStarts = count($starts);
        $nEnds   = count($ends);

        $result = [];

        foreach ($people as $t) {
            $started = $this->upperBound($starts, $t, $nStarts);
            $ended   = $this->upperBound($ends, $t, $nEnds);
            $result[] = $started - $ended;
        }

        return $result;
    }

    /**
     * Returns the count of elements <= target in a sorted array.
     *
     * @param int[] $arr
     * @param int   $target
     * @param int   $len
     * @return int
     */
    private function upperBound($arr, $target, $len) {
        $low = 0;
        $high = $len; // exclusive

        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($arr[$mid] <= $target) {
                $low = $mid + 1;
            } else {
                $high = $mid;
            }
        }

        return $low; // number of elements <= target
    }
}
```

## Swift

```swift
class Solution {
    func fullBloomFlowers(_ flowers: [[Int]], _ people: [Int]) -> [Int] {
        var starts = [Int]()
        var ends = [Int]()
        starts.reserveCapacity(flowers.count)
        ends.reserveCapacity(flowers.count)
        for f in flowers {
            starts.append(f[0])
            ends.append(f[1] + 1)
        }
        starts.sort()
        ends.sort()
        
        func upperBound(_ arr: [Int], _ target: Int) -> Int {
            var left = 0
            var right = arr.count
            while left < right {
                let mid = (left + right) >> 1
                if arr[mid] <= target {
                    left = mid + 1
                } else {
                    right = mid
                }
            }
            return left
        }
        
        var result = [Int]()
        result.reserveCapacity(people.count)
        for p in people {
            let started = upperBound(starts, p)
            let ended = upperBound(ends, p)
            result.append(started - ended)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun fullBloomFlowers(flowers: Array<IntArray>, people: IntArray): IntArray {
        val n = flowers.size
        val starts = IntArray(n)
        val ends = IntArray(n)
        for (i in 0 until n) {
            starts[i] = flowers[i][0]
            ends[i] = flowers[i][1] + 1
        }
        java.util.Arrays.sort(starts)
        java.util.Arrays.sort(ends)

        fun upperBound(arr: IntArray, target: Int): Int {
            var l = 0
            var r = arr.size
            while (l < r) {
                val m = (l + r) ushr 1
                if (arr[m] <= target) {
                    l = m + 1
                } else {
                    r = m
                }
            }
            return l
        }

        val ans = IntArray(people.size)
        for (i in people.indices) {
            val t = people[i]
            val started = upperBound(starts, t)
            val ended = upperBound(ends, t)
            ans[i] = started - ended
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> fullBloomFlowers(List<List<int>> flowers, List<int> people) {
    int n = flowers.length;
    List<int> starts = List.filled(n, 0);
    List<int> ends = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      starts[i] = flowers[i][0];
      ends[i] = flowers[i][1] + 1;
    }
    starts.sort();
    ends.sort();

    int upperBound(List<int> arr, int target) {
      int lo = 0, hi = arr.length;
      while (lo < hi) {
        int mid = (lo + hi) >> 1;
        if (arr[mid] <= target) {
          lo = mid + 1;
        } else {
          hi = mid;
        }
      }
      return lo;
    }

    List<int> ans = [];
    for (int p in people) {
      int started = upperBound(starts, p);
      int ended = upperBound(ends, p);
      ans.add(started - ended);
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func fullBloomFlowers(flowers [][]int, people []int) []int {
    n := len(flowers)
    starts := make([]int, n)
    ends := make([]int, n)
    for i, f := range flowers {
        starts[i] = f[0]
        ends[i] = f[1] + 1
    }
    sort.Ints(starts)
    sort.Ints(ends)

    ans := make([]int, len(people))
    for i, p := range people {
        started := sort.Search(len(starts), func(j int) bool { return starts[j] > p })
        ended := sort.Search(len(ends), func(j int) bool { return ends[j] > p })
        ans[i] = started - ended
    }
    return ans
}
```

## Ruby

```ruby
def upper_bound(arr, target)
  l = 0
  r = arr.length
  while l < r
    m = (l + r) / 2
    if arr[m] <= target
      l = m + 1
    else
      r = m
    end
  end
  l
end

def full_bloom_flowers(flowers, people)
  n = flowers.length
  starts = Array.new(n)
  ends = Array.new(n)
  flowers.each_with_index do |f, i|
    starts[i] = f[0]
    ends[i] = f[1] + 1
  end
  starts.sort!
  ends.sort!
  ans = []
  people.each do |p|
    ans << upper_bound(starts, p) - upper_bound(ends, p)
  end
  ans
end
```

## Scala

```scala
object Solution {
  def fullBloomFlowers(flowers: Array[Array[Int]], people: Array[Int]): Array[Int] = {
    val n = flowers.length
    val starts = new Array[Int](n)
    val ends = new Array[Int](n)
    var i = 0
    while (i < n) {
      starts(i) = flowers(i)(0)
      ends(i) = flowers(i)(1) + 1
      i += 1
    }
    java.util.Arrays.sort(starts)
    java.util.Arrays.sort(ends)

    def upperBound(arr: Array[Int], target: Int): Int = {
      var l = 0
      var r = arr.length
      while (l < r) {
        val mid = (l + r) >>> 1
        if (arr(mid) <= target) l = mid + 1 else r = mid
      }
      l
    }

    val m = people.length
    val ans = new Array[Int](m)
    var idx = 0
    while (idx < m) {
      val t = people(idx)
      val started = upperBound(starts, t)
      val ended = upperBound(ends, t)
      ans(idx) = started - ended
      idx += 1
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn full_bloom_flowers(flowers: Vec<Vec<i32>>, people: Vec<i32>) -> Vec<i32> {
        let n = flowers.len();
        let mut starts = Vec::with_capacity(n);
        let mut ends = Vec::with_capacity(n);
        for f in &flowers {
            starts.push(f[0]);
            // end is inclusive, store end+1 to simplify counting
            ends.push(f[1] + 1);
        }
        starts.sort_unstable();
        ends.sort_unstable();

        let mut ans = Vec::with_capacity(people.len());
        for &p in &people {
            let started = starts.partition_point(|&x| x <= p) as i32;
            let ended = ends.partition_point(|&x| x <= p) as i32;
            ans.push(started - ended);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (full-bloom-flowers flowers people)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?))
  (let* ((starts (map first flowers))
         (ends   (map (lambda (fl) (+ (second fl) 1)) flowers))
         (sorted-starts (sort starts <))
         (sorted-ends   (sort ends <))
         (vec-starts (list->vector sorted-starts))
         (vec-ends   (list->vector sorted-ends)))
    (define (upper-bound vec x)
      (let loop ((lo 0) (hi (vector-length vec)))
        (if (= lo hi)
            lo
            (let* ((mid (quotient (+ lo hi) 2))
                   (mid-val (vector-ref vec mid)))
              (if (<= mid-val x)
                  (loop (+ mid 1) hi)
                  (loop lo mid))))))
    (map (lambda (t)
           (- (upper-bound vec-starts t)
              (upper-bound vec-ends   t)))
         people)))
```

## Erlang

```erlang
-spec full_bloom_flowers(Flowers :: [[integer()]], People :: [integer()]) -> [integer()].
full_bloom_flowers(Flowers, People) ->
    Starts0 = [Start || [Start,_] <- Flowers],
    Ends0   = [End+1  || [_ , End] <- Flowers],
    SortedStarts = lists:sort(Starts0),
    SortedEnds   = lists:sort(Ends0),
    StartsTuple = list_to_tuple(SortedStarts),
    EndsTuple   = list_to_tuple(SortedEnds),
    LenS = tuple_size(StartsTuple),
    LenE = tuple_size(EndsTuple),
    [calc(Person, StartsTuple, LenS, EndsTuple, LenE) || Person <- People].

calc(Person, StartsT, LenS, EndsT, LenE) ->
    I = upper_bound(StartsT, LenS, Person),
    J = upper_bound(EndsT, LenE, Person),
    I - J.

upper_bound(Tuple, Len, Target) ->
    upper_bound_loop(0, Len, Tuple, Target).

upper_bound_loop(Low, High, _Tuple, _Target) when Low >= High ->
    Low;
upper_bound_loop(Low, High, Tuple, Target) ->
    Mid = (Low + High) div 2,
    Elem = element(Mid+1, Tuple),
    if Elem =< Target ->
            upper_bound_loop(Mid+1, High, Tuple, Target);
       true ->
            upper_bound_loop(Low, Mid, Tuple, Target)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec full_bloom_flowers(flowers :: [[integer]], people :: [integer]) :: [integer]
  def full_bloom_flowers(flowers, people) do
    starts = for [s, _] <- flowers, do: s
    ends = for [_ , e] <- flowers, do: e + 1

    starts = Enum.sort(starts)
    ends = Enum.sort(ends)

    indexed_people =
      people
      |> Enum.with_index()
      |> Enum.map(fn {p, i} -> {p, i} end)

    sorted_people = Enum.sort_by(indexed_people, fn {p, _} -> p end)

    ans_array = :array.new(length(people), default: 0)

    final_ans =
      process(sorted_people, starts, ends, 0, 0, ans_array)

    len = length(people)

    Enum.map(0..len - 1, fn i -> :array.get(i, final_ans) end)
  end

  defp process([], _starts, _ends, _i_cnt, _j_cnt, ans), do: ans

  defp process([{time, idx} | rest], starts, ends, i_cnt, j_cnt, ans) do
    {new_starts, new_i_cnt} = pop_while(starts, time, i_cnt)
    {new_ends, new_j_cnt} = pop_while(ends, time, j_cnt)

    updated_ans = :array.set(idx, new_i_cnt - new_j_cnt, ans)

    process(rest, new_starts, new_ends, new_i_cnt, new_j_cnt, updated_ans)
  end

  defp pop_while([h | t] = list, time, cnt) when h <= time do
    pop_while(t, time, cnt + 1)
  end

  defp pop_while(list, _time, cnt), do: {list, cnt}
end
```
