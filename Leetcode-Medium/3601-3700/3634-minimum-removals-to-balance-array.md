# 3634. Minimum Removals to Balance Array

## Cpp

```cpp
class Solution {
public:
    int minRemoval(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int maxLen = 0;
        int r = 0;
        for (int l = 0; l < n; ++l) {
            while (r < n && (long long)nums[r] <= (long long)k * nums[l]) {
                ++r;
            }
            maxLen = max(maxLen, r - l);
        }
        return n - maxLen;
    }
};
```

## Java

```java
class Solution {
    public int minRemoval(int[] nums, int k) {
        int n = nums.length;
        java.util.Arrays.sort(nums);
        int left = 0;
        int maxLen = 0;
        for (int right = 0; right < n; ++right) {
            while ((long) nums[right] > (long) k * nums[left]) {
                left++;
            }
            int len = right - left + 1;
            if (len > maxLen) {
                maxLen = len;
            }
        }
        return n - maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        max_len = 0
        j = 0
        for i in range(n):
            # Ensure j is at least i
            if j < i:
                j = i
            while j + 1 < n and nums[j + 1] <= k * nums[i]:
                j += 1
            # Current window [i, j]
            max_len = max(max_len, j - i + 1)
        return n - max_len
```

## Python3

```python
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_len = 0
        j = 0
        for i in range(n):
            while j < n and nums[j] <= k * nums[i]:
                j += 1
            # window is [i, j-1]
            cur_len = j - i
            if cur_len > max_len:
                max_len = cur_len
        return n - max_len
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

int minRemoval(int* nums, int numsSize, int k) {
    qsort(nums, numsSize, sizeof(int), cmp_int);
    int maxLen = 0;
    int j = 0;
    for (int i = 0; i < numsSize; ++i) {
        while (j < numsSize && (long long)nums[j] <= (long long)k * nums[i]) {
            ++j;
        }
        int len = j - i;
        if (len > maxLen) maxLen = len;
    }
    return numsSize - maxLen;
}
```

## Csharp

```csharp
public class Solution {
    public int MinRemoval(int[] nums, int k) {
        int n = nums.Length;
        System.Array.Sort(nums);
        int left = 0;
        int maxLen = 0;
        for (int right = 0; right < n; ++right) {
            while ((long)nums[right] > (long)k * nums[left]) {
                left++;
            }
            int len = right - left + 1;
            if (len > maxLen) maxLen = len;
        }
        return n - maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minRemoval = function(nums, k) {
    const sorted = nums.slice().sort((a, b) => a - b);
    const n = sorted.length;
    let maxLen = 0;
    let j = 0;
    for (let i = 0; i < n; ++i) {
        if (j < i) j = i;
        while (j < n && sorted[j] <= k * sorted[i]) {
            ++j;
        }
        const len = j - i;
        if (len > maxLen) maxLen = len;
    }
    return n - maxLen;
};
```

## Typescript

```typescript
function minRemoval(nums: number[], k: number): number {
    const n = nums.length;
    nums.sort((a, b) => a - b);
    let maxLen = 0;
    let j = 0;
    for (let i = 0; i < n; i++) {
        while (j < n && nums[j] <= k * nums[i]) {
            j++;
        }
        const len = j - i;
        if (len > maxLen) maxLen = len;
    }
    return n - maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minRemoval($nums, $k) {
        sort($nums);
        $n = count($nums);
        $i = 0;
        $maxLen = 0;
        for ($j = 0; $j < $n; $j++) {
            while ($i <= $j && $nums[$j] > $k * $nums[$i]) {
                $i++;
            }
            $len = $j - $i + 1;
            if ($len > $maxLen) {
                $maxLen = $len;
            }
        }
        return $n - $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func minRemoval(_ nums: [Int], _ k: Int) -> Int {
        let sorted = nums.sorted()
        let n = sorted.count
        var maxLen = 0
        var j = 0
        for i in 0..<n {
            if j < i { j = i }
            while j < n && Int64(sorted[j]) <= Int64(k) * Int64(sorted[i]) {
                j += 1
            }
            let len = j - i
            if len > maxLen {
                maxLen = len
            }
        }
        return n - maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minRemoval(nums: IntArray, k: Int): Int {
        nums.sort()
        val n = nums.size
        var maxLen = 0
        var j = 0
        val kk = k.toLong()
        for (i in 0 until n) {
            if (j < i) j = i
            while (j < n && nums[j].toLong() <= kk * nums[i].toLong()) {
                j++
            }
            val len = j - i
            if (len > maxLen) maxLen = len
        }
        return n - maxLen
    }
}
```

## Dart

```dart
class Solution {
  int minRemoval(List<int> nums, int k) {
    nums.sort();
    int n = nums.length;
    int i = 0;
    int maxLen = 0;
    for (int j = 0; j < n; ++j) {
      while (i <= j && nums[j] > k * nums[i]) {
        i++;
      }
      int curLen = j - i + 1;
      if (curLen > maxLen) maxLen = curLen;
    }
    return n - maxLen;
  }
}
```

## Golang

```go
package main

import "sort"

func minRemoval(nums []int, k int) int {
	sort.Ints(nums)
	n := len(nums)
	maxLen := 0
	j := 0
	for i := 0; i < n; i++ {
		if j < i {
			j = i
		}
		for j+1 < n && int64(nums[j+1]) <= int64(k)*int64(nums[i]) {
			j++
		}
		if cur := j - i + 1; cur > maxLen {
			maxLen = cur
		}
	}
	return n - maxLen
}
```

## Ruby

```ruby
def min_removal(nums, k)
  nums.sort!
  n = nums.length
  max_len = 0
  j = 0
  (0...n).each do |i|
    j = i if j < i
    while j < n && nums[j] <= k * nums[i]
      j += 1
    end
    len = j - i
    max_len = len if len > max_len
  end
  n - max_len
end
```

## Scala

```scala
object Solution {
    def minRemoval(nums: Array[Int], k: Int): Int = {
        val sorted = nums.sorted
        val n = sorted.length
        var maxWindow = 0
        var j = 0
        val kk = k.toLong
        for (i <- 0 until n) {
            if (j < i) j = i
            while (j < n && sorted(j).toLong <= kk * sorted(i).toLong) {
                j += 1
            }
            val size = j - i
            if (size > maxWindow) maxWindow = size
        }
        n - maxWindow
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn min_removal(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut sorted = nums;
        sorted.sort_unstable();

        let mut best = 0usize;
        let mut j = 0usize;

        for i in 0..n {
            while j < n && (sorted[j] as i64) <= (k as i64) * (sorted[i] as i64) {
                j += 1;
            }
            let len = j - i;
            if len > best {
                best = len;
            }
        }

        (n - best) as i32
    }
}
```

## Racket

```racket
(define/contract (min-removal nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([sorted (sort nums <)]
         [v (list->vector sorted)]
         [n (vector-length v)])
    (let loop ((i 0) (j 0) (maxlen 0))
      (if (= i n)
          (- n maxlen)
          (let* ([j (if (< j i) i j)]
                 [new-j
                  (let recur ((jj j))
                    (if (and (< jj n)
                             (<= (vector-ref v jj) (* k (vector-ref v i))))
                        (recur (+ jj 1))
                        jj))])
            (loop (+ i 1) new-j (max maxlen (- new-j i))))))))
```

## Erlang

```erlang
-spec min_removal([integer()], integer()) -> integer().
min_removal(Nums, K) ->
    Sorted = lists:sort(Nums),
    Tuple = list_to_tuple(Sorted),
    N = tuple_size(Tuple),
    MaxLen = slide(0, 0, N, K, Tuple, 0),
    N - MaxLen.

slide(I, J, N, _K, _Tuple, Max) when I >= N ->
    Max;
slide(I, J, N, K, Tuple, Max) ->
    J1 = if J < I -> I; true -> J end,
    NewJ = advance(J1, I, N, K, Tuple),
    Len = NewJ - I + 1,
    NewMax = if Len > Max -> Len; true -> Max end,
    slide(I + 1, NewJ, N, K, Tuple, NewMax).

advance(J, I, N, K, Tuple) ->
    case J + 1 < N of
        true ->
            NextVal = element(J + 2, Tuple),
            MinVal = element(I + 1, Tuple),
            if NextVal =< K * MinVal -> advance(J + 1, I, N, K, Tuple);
               true -> J
            end;
        false -> J
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_removal(nums :: [integer], k :: integer) :: integer
  def min_removal(nums, k) do
    sorted = Enum.sort(nums)
    arr = List.to_tuple(sorted)
    n = tuple_size(arr)

    max_len = slide(arr, n, k, 0, 0, 0)
    n - max_len
  end

  defp slide(_arr, n, _k, i, _j, max_len) when i >= n do
    max_len
  end

  defp slide(arr, n, k, i, j, max_len) do
    j = advance_j(arr, n, k, i, j)
    cur_len = j - i
    new_max = if cur_len > max_len, do: cur_len, else: max_len
    slide(arr, n, k, i + 1, j, new_max)
  end

  defp advance_j(_arr, n, _k, _i, j) when j >= n, do: j

  defp advance_j(arr, n, k, i, j) do
    min_val = elem(arr, i)
    max_val = elem(arr, j)

    if max_val <= k * min_val do
      advance_j(arr, n, k, i, j + 1)
    else
      j
    end
  end
end
```
