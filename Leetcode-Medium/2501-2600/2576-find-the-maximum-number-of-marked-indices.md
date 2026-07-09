# 2576. Find the Maximum Number of Marked Indices

## Cpp

```cpp
class Solution {
public:
    int maxNumOfMarkedIndices(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int lo = 0, hi = n / 2;
        auto can = [&](int k)->bool{
            for (int i = 0; i < k; ++i) {
                if (2LL * nums[i] > nums[n - k + i]) return false;
            }
            return true;
        };
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (can(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo * 2;
    }
};
```

## Java

```java
class Solution {
    public int maxNumOfMarkedIndices(int[] nums) {
        java.util.Arrays.sort(nums);
        int n = nums.length;
        int low = 0, high = n / 2;
        while (low < high) {
            int mid = (low + high + 1) >>> 1; // upper middle
            if (canFormPairs(mid, nums)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low * 2;
    }

    private boolean canFormPairs(int k, int[] arr) {
        int n = arr.length;
        for (int i = 0; i < k; i++) {
            long small = arr[i];
            long large = arr[n - k + i];
            if (small * 2 > large) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        i, j = 0, n // 2
        cnt = 0
        while i < n // 2 and j < n:
            if 2 * nums[i] <= nums[j]:
                cnt += 1
                i += 1
                j += 1
            else:
                j += 1
        return cnt * 2
```

## Python3

```python
from typing import List

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        lo, hi = 0, n // 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            ok = True
            for i in range(mid):
                if 2 * nums[i] > nums[n - mid + i]:
                    ok = False
                    break
            if ok:
                lo = mid
            else:
                hi = mid - 1
        return lo * 2
```

## C

```c
#include <stdlib.h>

static int cmp(const void *a, const void *b) {
    int ai = *(const int *)a;
    int bi = *(const int *)b;
    return (ai > bi) - (ai < bi);
}

int maxNumOfMarkedIndices(int* nums, int numsSize) {
    if (numsSize < 2) return 0;
    qsort(nums, numsSize, sizeof(int), cmp);
    int i = 0, j = numsSize / 2, cnt = 0;
    while (i < numsSize / 2 && j < numsSize) {
        if ((long long)nums[i] * 2 <= (long long)nums[j]) {
            ++cnt;
            ++i;
            ++j;
        } else {
            ++j;
        }
    }
    return cnt * 2;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxNumOfMarkedIndices(int[] nums) {
        System.Array.Sort(nums);
        int n = nums.Length;
        int i = 0, j = n / 2;
        int pairs = 0;
        while (i < n / 2 && j < n) {
            if ((long)nums[i] * 2 <= nums[j]) {
                pairs++;
                i++;
                j++;
            } else {
                j++;
            }
        }
        return pairs * 2;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxNumOfMarkedIndices = function(nums) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const half = Math.floor(n / 2);
    let i = 0, j = half, cnt = 0;
    while (i < half && j < n) {
        if (2 * nums[i] <= nums[j]) {
            cnt++;
            i++;
            j++;
        } else {
            j++;
        }
    }
    return cnt * 2;
};
```

## Typescript

```typescript
function maxNumOfMarkedIndices(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const half = Math.floor(n / 2);
    let left = 0;
    let right = half;
    let pairs = 0;
    while (left < half && right < n) {
        if (nums[left] * 2 <= nums[right]) {
            pairs++;
            left++;
            right++;
        } else {
            right++;
        }
    }
    return pairs * 2;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxNumOfMarkedIndices($nums) {
        sort($nums);
        $n = count($nums);
        $low = 0;
        $high = intdiv($n, 2);
        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2);
            if ($this->canMark($nums, $n, $mid)) {
                $low = $mid;
            } else {
                $high = $mid - 1;
            }
        }
        return $low * 2;
    }

    private function canMark($arr, $n, $k) {
        for ($i = 0; $i < $k; $i++) {
            if (2 * $arr[$i] > $arr[$n - $k + $i]) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func maxNumOfMarkedIndices(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        let n = sorted.count
        var i = 0
        var j = n / 2
        var pairs = 0
        while i < n / 2 && j < n {
            if sorted[i] * 2 <= sorted[j] {
                pairs += 1
                i += 1
                j += 1
            } else {
                j += 1
            }
        }
        return pairs * 2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxNumOfMarkedIndices(nums: IntArray): Int {
        val sorted = nums.sorted()
        val n = sorted.size
        var left = 0
        var right = n / 2
        var pairs = 0
        while (left < n / 2 && right < n) {
            if (sorted[left].toLong() * 2L <= sorted[right]) {
                pairs++
                left++
                right++
            } else {
                right++
            }
        }
        return pairs * 2
    }
}
```

## Dart

```dart
class Solution {
  int maxNumOfMarkedIndices(List<int> nums) {
    nums.sort();
    int n = nums.length;
    int leftSize = n ~/ 2;
    int i = 0, j = leftSize, cnt = 0;
    while (i < leftSize && j < n) {
      if (nums[i] * 2 <= nums[j]) {
        cnt++;
        i++;
        j++;
      } else {
        j++;
      }
    }
    return cnt * 2;
  }
}
```

## Golang

```go
func maxNumOfMarkedIndices(nums []int) int {
    sort.Ints(nums)
    n := len(nums)
    lo, hi := 0, n/2
    for lo < hi {
        mid := (lo + hi + 1) / 2
        if can(mid, nums) {
            lo = mid
        } else {
            hi = mid - 1
        }
    }
    return lo * 2
}

func can(k int, a []int) bool {
    n := len(a)
    for i := 0; i < k; i++ {
        if int64(2)*int64(a[i]) > int64(a[n-k+i]) {
            return false
        }
    }
    return true
}

import "sort"
```

## Ruby

```ruby
def max_num_of_marked_indices(nums)
  a = nums.sort
  n = a.length
  low = 0
  high = n / 2
  while low < high
    mid = (low + high + 1) / 2
    ok = true
    i = 0
    while i < mid
      if 2 * a[i] > a[n - mid + i]
        ok = false
        break
      end
      i += 1
    end
    if ok
      low = mid
    else
      high = mid - 1
    end
  end
  low * 2
end
```

## Scala

```scala
object Solution {
    def maxNumOfMarkedIndices(nums: Array[Int]): Int = {
        val sorted = nums.sorted
        val n = sorted.length
        var left = 0
        var right = n / 2
        var marked = 0
        while (left < n / 2 && right < n) {
            if (sorted(left).toLong * 2 <= sorted(right).toLong) {
                marked += 2
                left += 1
                right += 1
            } else {
                right += 1
            }
        }
        marked
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_num_of_marked_indices(nums: Vec<i32>) -> i32 {
        let mut a = nums;
        a.sort_unstable();
        let n = a.len();
        let mut lo = 0usize;
        let mut hi = n / 2;
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if Self::can(&a, mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        (lo * 2) as i32
    }

    fn can(arr: &Vec<i32>, k: usize) -> bool {
        if k == 0 {
            return true;
        }
        let n = arr.len();
        let mut i = 0usize;          // index in the smallest k elements
        let mut j = n - k;           // start of the largest k elements
        let mut matched = 0usize;

        while i < k && j < n {
            if (arr[i] as i64) * 2 <= arr[j] as i64 {
                matched += 1;
                i += 1;
                j += 1;
            } else {
                i += 1;
            }
        }
        matched == k
    }
}
```

## Racket

```racket
(define/contract (max-num-of-marked-indices nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([sorted (sort nums <)]
         [v (list->vector sorted)]
         [n (vector-length v)]
         [mid (quotient n 2)])
    (let loop ([left 0] [right mid] [cnt 0])
      (if (or (>= left mid) (>= right n))
          (* cnt 2)
          (if (<= (* 2 (vector-ref v left)) (vector-ref v right))
              (loop (+ left 1) (+ right 1) (+ cnt 1))
              (loop left (+ right 1) cnt))))))
```

## Erlang

```erlang
-module(solution).
-export([max_num_of_marked_indices/1]).

-spec max_num_of_marked_indices(Nums :: [integer()]) -> integer().
max_num_of_marked_indices(Nums) ->
    Sorted = lists:sort(Nums),
    N = length(Sorted),
    MaxPairs = N div 2,
    binary_search(Sorted, N, 0, MaxPairs).

binary_search(_Sorted, _N, Low, High) when Low >= High ->
    Low * 2;
binary_search(Sorted, N, Low, High) ->
    Mid = (Low + High + 1) div 2,
    case can_pair(Sorted, N, Mid) of
        true -> binary_search(Sorted, N, Mid, High);
        false -> binary_search(Sorted, N, Low, Mid - 1)
    end.

can_pair(_Sorted, _N, 0) -> true;
can_pair(Sorted, N, K) ->
    Left = lists:sublist(Sorted, 1, K),
    RightStart = N - K + 1,
    Right = lists:sublist(Sorted, RightStart, K),
    check_pairs(Left, Right).

check_pairs([], []) -> true;
check_pairs([L|Ls], [R|Rs]) ->
    if
        2 * L =< R -> check_pairs(Ls, Rs);
        true -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_num_of_marked_indices(nums :: [integer]) :: integer
  def max_num_of_marked_indices(nums) do
    sorted = nums |> Enum.sort() |> List.to_tuple()
    n = tuple_size(sorted)
    limit = div(n, 2)

    count =
      pair_count(sorted, 0, limit, limit, n, 0)

    count * 2
  end

  defp pair_count(_arr, i, _j, limit_i, _n, acc) when i >= limit_i, do: acc
  defp pair_count(_arr, _i, j, _limit_i, n, acc) when j >= n, do: acc

  defp pair_count(arr, i, j, limit_i, n, acc) do
    if 2 * elem(arr, i) <= elem(arr, j) do
      pair_count(arr, i + 1, j + 1, limit_i, n, acc + 1)
    else
      pair_count(arr, i, j + 1, limit_i, n, acc)
    end
  end
end
```
