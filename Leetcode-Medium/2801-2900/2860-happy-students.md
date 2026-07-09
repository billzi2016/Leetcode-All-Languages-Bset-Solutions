# 2860. Happy Students

## Cpp

```cpp
class Solution {
public:
    int countWays(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int ans = 0;
        for (int k = 0; k <= n; ++k) {
            int cnt = lower_bound(nums.begin(), nums.end(), k) - nums.begin();
            if (cnt == k) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countWays(java.util.List<Integer> nums) {
        int n = nums.size();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = nums.get(i);
        }
        java.util.Arrays.sort(arr);
        long ways = 1; // count the empty selection
        for (int i = 0; i < n; i++) {
            if (arr[i] <= i) {
                ways++;
            }
        }
        return (int) ways;
    }
}
```

## Python

```python
class Solution(object):
    def countWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sorted(nums)
        n = len(a)
        ans = 1  # empty selection is always valid
        for i in range(n):
            if a[i] == i and (i == n - 1 or a[i + 1] > a[i]):
                ans += 1
        return ans
```

## Python3

```python
import bisect
from typing import List

class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for k in range(0, n + 1):
            cnt = bisect.bisect_left(nums, k)  # number of elements < k
            if cnt == k:
                if cnt < n and nums[cnt] == k:
                    continue
                ans += 1
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return *(const int *)a - *(const int *)b;
}

int countWays(int* nums, int numsSize) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    int ans = 0;
    int idx = 0; // number of elements less than current i
    for (int i = 0; i <= numsSize; ++i) {
        while (idx < numsSize && nums[idx] < i) {
            ++idx;
        }
        if (idx == i) {
            if (i < numsSize && nums[idx] == i) {
                continue; // invalid because some element equals i
            }
            ++ans;
        }
    }
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int CountWays(IList<int> nums) {
        List<int> arr = new List<int>(nums);
        arr.Sort();
        int n = arr.Count;
        long ways = 1; // empty group
        for (int i = 0; i < n; i++) {
            if (arr[i] <= i && (i == n - 1 || arr[i + 1] > i)) {
                ways++;
            }
        }
        return (int)ways;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countWays = function(nums) {
    const n = nums.length;
    nums.sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        if (nums[i] <= i) {
            if (i === n - 1 || nums[i + 1] > i + 1) {
                ans++;
            }
        }
    }
    // empty set is valid only when there is no student with requirement 0
    if (n === 0 || nums[0] !== 0) ans += 1;
    return ans;
};
```

## Typescript

```typescript
function countWays(nums: number[]): number {
    const n = nums.length;
    nums.sort((a, b) => a - b);
    let ans = 0;
    for (let k = 0; k <= n; k++) {
        if (k > 0 && !(nums[k - 1] < k)) continue;
        if (k < n && !(nums[k] >= k)) continue;
        ans++;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countWays($nums) {
        $n = count($nums);
        sort($nums, SORT_NUMERIC);
        $ans = 0;
        // k = 0 case: valid only if no student has value 0
        if ($n > 0 && $nums[0] != 0) {
            $ans++;
        }
        // check gaps between consecutive values for k = i+1
        for ($i = 0; $i < $n - 1; $i++) {
            $k = $i + 1;
            if ($nums[$i] < $k && $nums[$i + 1] > $k) {
                $ans++;
            }
        }
        // k = n case is always valid because nums[i] < n for all i
        $ans++;
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countWays(_ nums: [Int]) -> Int {
        let n = nums.count
        var a = nums.sorted()
        var ans = 0
        
        // k = 0
        if a[0] > 0 { ans += 1 }
        
        // 1 <= k < n
        if n >= 2 {
            for k in 1..<n {
                if a[k - 1] < k && a[k] > k {
                    ans += 1
                }
            }
        }
        
        // k = n
        if a[n - 1] < n { ans += 1 }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countWays(nums: List<Int>): Int {
        val sorted = nums.sorted()
        val n = sorted.size
        var ans = 0

        // k = 0 (select no student)
        if (sorted[0] > 0) ans++

        // 1 <= k < n
        for (k in 1 until n) {
            if (sorted[k - 1] < k && sorted[k] > k) {
                ans++
            }
        }

        // k = n (select all students)
        if (sorted[n - 1] < n) ans++

        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countWays(List<int> nums) {
    int n = nums.length;
    nums.sort();
    int i = 0;
    int ans = 0;
    for (int k = 0; k <= n; ++k) {
      while (i < n && nums[i] < k) {
        i++;
      }
      if (i == k) {
        if (i == n || nums[i] != k) {
          ans++;
        }
      }
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "sort"

func countWays(nums []int) int {
	n := len(nums)
	sort.Ints(nums)
	ans := 0
	i := 0
	for k := 0; k <= n; k++ {
		for i < n && nums[i] < k {
			i++
		}
		if i == k && !(i < n && nums[i] == k) {
			ans++
		}
	}
	return ans
}
```

## Ruby

```ruby
def count_ways(nums)
  n = nums.length
  a = nums.sort
  ans = 0
  i = 0
  (0..n).each do |k|
    while i < n && a[i] < k
      i += 1
    end
    next if i < n && a[i] == k
    ans += 1 if i == k
  end
  ans
end
```

## Scala

```scala
object Solution {
  def countWays(nums: List[Int]): Int = {
    val n = nums.length
    val arr = nums.sorted
    var ans = 1 // select all students is always valid

    // empty selection is valid only if no student has value 0
    if (n == 0 || arr.head > 0) ans += 1

    for (i <- 0 until n - 1) {
      val k = i + 1
      if (arr(i) <= i && arr(i + 1) > k) {
        ans += 1
      }
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_ways(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        let n = nums.len();
        let mut ans = 0i32;
        for k in 0..=n {
            if k == 0 {
                if nums[0] > 0 {
                    ans += 1;
                }
            } else if k == n {
                // all selected, always valid because nums[i] <= n-1 < n
                ans += 1;
            } else {
                let left = nums[k - 1];
                let right = nums[k];
                if left < k as i32 && right > k as i32 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (count-ways nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (sorted (sort nums <))
         ;; build a hash set of all values in nums
         (val-set (let ((h (make-hash)))
                    (for ([v nums]) (hash-set! h v #t))
                    h))
         ;; empty selection corresponds to k = 0
         (ans0 (if (hash-has-key? val-set 0) 0 1)))
    (let loop ((i 0) (ans ans0))
      (if (= i n)
          ans
          (let* ((v (list-ref sorted i))
                 (last-of-block (or (= (+ i 1) n)
                                    (not (= v (list-ref sorted (+ i 1))))))
                 (new-ans (if last-of-block
                              (if (hash-has-key? val-set (+ i 1)) ans (+ ans 1))
                              ans)))
            (loop (+ i 1) new-ans))))))
```

## Erlang

```erlang
-spec count_ways(Nums :: [integer()]) -> integer().
count_ways(Nums) ->
    N = length(Nums),
    FreqMap = build_freq_map(Nums, #{}),
    loop(0, 0, 0, N, FreqMap).

build_freq_map([], Map) -> Map;
build_freq_map([H|T], Map) ->
    NewMap = maps:update_with(H, fun(C) -> C + 1 end, 1, Map),
    build_freq_map(T, NewMap).

loop(S, Processed, Ans, N, FreqMap) when S =< N ->
    CountLess = Processed,
    FreqS = maps:get(S, FreqMap, 0),
    NewAns = case (CountLess == S) andalso (FreqS == 0) of
                true -> Ans + 1;
                false -> Ans
            end,
    loop(S + 1, Processed + FreqS, NewAns, N, FreqMap);
loop(_, _, Ans, _, _) -> Ans.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_ways(nums :: [integer]) :: integer
  def count_ways(nums) do
    sorted = Enum.sort(nums)
    n = length(sorted)
    arr = List.to_tuple(sorted)

    Enum.reduce(0..n, 0, fn k, acc ->
      left_ok =
        if k == 0 do
          true
        else
          elem(arr, k - 1) < k
        end

      right_ok =
        if k == n do
          true
        else
          elem(arr, k) > k
        end

      if left_ok and right_ok, do: acc + 1, else: acc
    end)
  end
end
```
