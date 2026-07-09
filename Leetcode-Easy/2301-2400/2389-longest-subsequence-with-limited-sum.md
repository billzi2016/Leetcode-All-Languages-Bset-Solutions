# 2389. Longest Subsequence With Limited Sum

## Cpp

```cpp
class Solution {
public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + nums[i];
        }
        vector<int> ans;
        ans.reserve(queries.size());
        for (int q : queries) {
            int cnt = upper_bound(pref.begin(), pref.end(), (long long)q) - pref.begin() - 1;
            ans.push_back(cnt);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] answerQueries(int[] nums, int[] queries) {
        int n = nums.length;
        int[] sorted = nums.clone();
        java.util.Arrays.sort(sorted);
        long[] prefix = new long[n];
        for (int i = 0; i < n; i++) {
            prefix[i] = sorted[i] + (i > 0 ? prefix[i - 1] : 0L);
        }
        int m = queries.length;
        int[] answer = new int[m];
        for (int i = 0; i < m; i++) {
            long q = queries[i];
            int low = 0, high = n; // number of elements we can take
            while (low < high) {
                int mid = (low + high + 1) >>> 1;
                if (mid == 0) {
                    low = mid;
                } else if (prefix[mid - 1] <= q) {
                    low = mid;
                } else {
                    high = mid - 1;
                }
            }
            answer[i] = low;
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)
        import bisect
        result = []
        for q in queries:
            # number of elements with cumulative sum <= q
            cnt = bisect.bisect_right(prefix, q)
            result.append(cnt)
        return result
```

## Python3

```python
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)
        import bisect
        res = []
        for q in queries:
            # find largest index i where prefix[i] <= q
            i = bisect.bisect_right(prefix, q) - 1
            res.append(i)
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* answerQueries(int* nums, int numsSize, int* queries, int queriesSize, int* returnSize) {
    // Copy and sort nums
    int *sorted = (int *)malloc(numsSize * sizeof(int));
    memcpy(sorted, nums, numsSize * sizeof(int));
    qsort(sorted, numsSize, sizeof(int), cmp_int);
    
    // Prefix sums (use long long to avoid overflow)
    long long *pref = (long long *)malloc(numsSize * sizeof(long long));
    for (int i = 0; i < numsSize; ++i) {
        pref[i] = sorted[i];
        if (i > 0) pref[i] += pref[i - 1];
    }
    
    int *ans = (int *)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; ++i) {
        long long q = queries[i];
        // binary search first index where pref[idx] > q
        int lo = 0, hi = numsSize;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (pref[mid] <= q)
                lo = mid + 1;
            else
                hi = mid;
        }
        ans[i] = lo; // number of elements we can take
    }
    
    free(sorted);
    free(pref);
    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] AnswerQueries(int[] nums, int[] queries) {
        System.Array.Sort(nums);
        int n = nums.Length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        int m = queries.Length;
        int[] answer = new int[m];

        for (int i = 0; i < m; i++) {
            long q = queries[i];
            int left = 0, right = n;
            while (left < right) {
                int mid = (left + right + 1) >> 1;
                if (prefix[mid] <= q) {
                    left = mid;
                } else {
                    right = mid - 1;
                }
            }
            answer[i] = left;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} queries
 * @return {number[]}
 */
var answerQueries = function(nums, queries) {
    const sorted = nums.slice().sort((a, b) => a - b);
    const n = sorted.length;
    const prefix = new Array(n + 1);
    prefix[0] = 0;
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + sorted[i];
    }
    
    const result = [];
    for (const q of queries) {
        let left = 0, right = n;
        while (left < right) {
            const mid = Math.floor((left + right + 1) / 2);
            if (prefix[mid] <= q) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        result.push(left);
    }
    return result;
};
```

## Typescript

```typescript
function answerQueries(nums: number[], queries: number[]): number[] {
    nums.sort((a, b) => a - b);
    const prefix = new Array(nums.length + 1).fill(0);
    for (let i = 0; i < nums.length; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    const result: number[] = [];
    for (const q of queries) {
        let left = 0, right = nums.length;
        while (left < right) {
            const mid = Math.floor((left + right + 1) / 2);
            if (prefix[mid] <= q) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        result.push(left);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $queries
     * @return Integer[]
     */
    function answerQueries($nums, $queries) {
        sort($nums);
        $prefix = [];
        $sum = 0;
        foreach ($nums as $v) {
            $sum += $v;
            $prefix[] = $sum;
        }
        $n = count($prefix);
        $ans = [];
        foreach ($queries as $q) {
            $low = 0;
            $high = $n;
            while ($low < $high) {
                $mid = intdiv($low + $high + 1, 2);
                if ($mid == 0) {
                    $low = $mid;
                    continue;
                }
                if ($prefix[$mid - 1] <= $q) {
                    $low = $mid;
                } else {
                    $high = $mid - 1;
                }
            }
            $ans[] = $low;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func answerQueries(_ nums: [Int], _ queries: [Int]) -> [Int] {
        let sorted = nums.sorted()
        var prefix = [Int]()
        var sum = 0
        for v in sorted {
            sum += v
            prefix.append(sum)
        }
        var result = [Int]()
        for q in queries {
            var left = 0
            var right = prefix.count
            while left < right {
                let mid = (left + right) / 2
                if prefix[mid] <= q {
                    left = mid + 1
                } else {
                    right = mid
                }
            }
            result.append(left)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun answerQueries(nums: IntArray, queries: IntArray): IntArray {
        val sorted = nums.sorted()
        val n = sorted.size
        val prefix = LongArray(n)
        var sum = 0L
        for (i in 0 until n) {
            sum += sorted[i].toLong()
            prefix[i] = sum
        }
        val result = IntArray(queries.size)
        for (idx in queries.indices) {
            val q = queries[idx].toLong()
            var left = 0
            var right = n - 1
            var ans = -1
            while (left <= right) {
                val mid = (left + right) ushr 1
                if (prefix[mid] <= q) {
                    ans = mid
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            }
            result[idx] = ans + 1
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> answerQueries(List<int> nums, List<int> queries) {
    // Sort the numbers to pick smallest elements first
    var sorted = List<int>.from(nums)..sort();
    int n = sorted.length;

    // Prefix sums: pref[i] is sum of first i elements (i from 0..n)
    List<int> pref = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      pref[i + 1] = pref[i] + sorted[i];
    }

    List<int> result = [];
    for (int q in queries) {
      // Binary search for the largest k such that pref[k] <= q
      int left = 0, right = n;
      while (left < right) {
        int mid = (left + right + 1) >> 1;
        if (pref[mid] <= q) {
          left = mid;
        } else {
          right = mid - 1;
        }
      }
      result.add(left);
    }

    return result;
  }
}
```

## Golang

```go
import "sort"

func answerQueries(nums []int, queries []int) []int {
    sort.Ints(nums)
    n := len(nums)
    pref := make([]int64, n+1)
    for i := 0; i < n; i++ {
        pref[i+1] = pref[i] + int64(nums[i])
    }

    res := make([]int, len(queries))
    for i, q := range queries {
        target := int64(q)
        lo, hi := 0, n+1
        for lo < hi {
            mid := (lo + hi) / 2
            if pref[mid] <= target {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        res[i] = lo - 1
    }
    return res
}
```

## Ruby

```ruby
def answer_queries(nums, queries)
  sorted = nums.sort
  prefix = [0]
  sorted.each { |v| prefix << prefix[-1] + v }

  n = sorted.length
  results = []

  queries.each do |q|
    lo = 0
    hi = n
    while lo < hi
      mid = (lo + hi + 1) / 2
      if prefix[mid] <= q
        lo = mid
      else
        hi = mid - 1
      end
    end
    results << lo
  end

  results
end
```

## Scala

```scala
object Solution {
    def answerQueries(nums: Array[Int], queries: Array[Int]): Array[Int] = {
        val sorted = nums.sorted
        val prefix = new Array[Long](sorted.length)
        var sum = 0L
        for (i <- sorted.indices) {
            sum += sorted(i).toLong
            prefix(i) = sum
        }
        import scala.collection.Searching._
        queries.map { q =>
            prefix.search(q.toLong) match {
                case Found(idx) => idx + 1
                case InsertionPoint(idx) => idx
            }
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn answer_queries(nums: Vec<i32>, queries: Vec<i32>) -> Vec<i32> {
        let mut sorted = nums;
        sorted.sort_unstable();
        let n = sorted.len();
        let mut pref: Vec<i64> = Vec::with_capacity(n);
        let mut sum: i64 = 0;
        for &v in &sorted {
            sum += v as i64;
            pref.push(sum);
        }
        let mut ans: Vec<i32> = Vec::with_capacity(queries.len());
        for q in queries {
            let target = q as i64;
            match pref.binary_search_by(|&x| x.cmp(&target)) {
                Ok(idx) => ans.push((idx + 1) as i32),
                Err(idx) => ans.push(idx as i32),
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (answer-queries nums queries)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((sorted-list (sort nums <))
         (sorted (list->vector sorted-list))
         (n (vector-length sorted))
         (prefix (make-vector n)))
    ;; build prefix sums of the sorted array
    (let loop ((i 0) (sum 0))
      (when (< i n)
        (let ((new-sum (+ sum (vector-ref sorted i))))
          (vector-set! prefix i new-sum)
          (loop (+ i 1) new-sum))))
    ;; binary search: largest k such that prefix[k-1] <= q
    (define (max-count q)
      (let loop2 ((lo 0) (hi n))
        (if (= lo hi)
            lo
            (let ((mid (quotient (+ lo hi) 2)))
              (if (<= (vector-ref prefix mid) q)
                  (loop2 (+ mid 1) hi)
                  (loop2 lo mid))))))
    (map max-count queries)))
```

## Erlang

```erlang
-spec answer_queries([integer()], [integer()]) -> [integer()].
answer_queries(Nums, Queries) ->
    Sorted = lists:sort(Nums),
    [max_len(Sorted, Q) || Q <- Queries].

max_len(Sorted, Q) -> max_len(Sorted, Q, 0, 0).

max_len([], _, Count, _) -> Count;
max_len([H|T], Q, Count, Sum) when Sum + H =< Q ->
    max_len(T, Q, Count + 1, Sum + H);
max_len(_, _, Count, _) -> Count.
```

## Elixir

```elixir
defmodule Solution do
  @spec answer_queries(nums :: [integer], queries :: [integer]) :: [integer]
  def answer_queries(nums, queries) do
    sorted = Enum.sort(nums)

    prefix_sums =
      Enum.reduce(sorted, [], fn x, acc ->
        sum = case acc do
          [] -> x
          [prev | _] -> prev + x
        end
        [sum | acc]
      end)
      |> Enum.reverse()

    Enum.map(queries, fn q ->
      prefix_sums
      |> Enum.take_while(&(&1 <= q))
      |> length()
    end)
  end
end
```
