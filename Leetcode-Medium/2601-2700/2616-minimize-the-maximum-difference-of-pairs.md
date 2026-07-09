# 2616. Minimize the Maximum Difference of Pairs

## Cpp

```cpp
class Solution {
public:
    int minimizeMax(vector<int>& nums, int p) {
        if (p == 0) return 0;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int left = 0;
        int right = nums.back() - nums.front(); // maximum possible difference
        
        auto can = [&](int limit) -> bool {
            int cnt = 0;
            for (int i = 0; i + 1 < n; ) {
                if (nums[i + 1] - nums[i] <= limit) {
                    ++cnt;
                    i += 2;
                } else {
                    ++i;
                }
                if (cnt >= p) return true;
            }
            return cnt >= p;
        };
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (can(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
```

## Java

```java
class Solution {
    public int minimizeMax(int[] nums, int p) {
        if (p == 0) return 0;
        java.util.Arrays.sort(nums);
        int n = nums.length;
        int left = 0;
        int right = nums[n - 1] - nums[0];
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (canFormPairs(nums, p, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private boolean canFormPairs(int[] nums, int p, int limit) {
        int count = 0;
        for (int i = 0; i < nums.length - 1 && count < p; ) {
            if (nums[i + 1] - nums[i] <= limit) {
                count++;
                i += 2;
            } else {
                i++;
            }
        }
        return count >= p;
    }
}
```

## Python

```python
class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        def can(limit):
            cnt = 0
            i = 0
            while i + 1 < n:
                if nums[i + 1] - nums[i] <= limit:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1
        return left
```

## Python3

```python
from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        n = len(nums)

        def can(threshold: int) -> int:
            cnt = 0
            i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= threshold:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if can(mid) >= p:
                right = mid
            else:
                left = mid + 1
        return left
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int minimizeMax(int* nums, int numsSize, int p) {
    if (p == 0) return 0;
    qsort(nums, numsSize, sizeof(int), cmp_int);
    
    int left = 0;
    int right = nums[numsSize - 1] - nums[0];
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        int cnt = 0;
        for (int i = 0; i + 1 < numsSize; ) {
            if (nums[i + 1] - nums[i] <= mid) {
                ++cnt;
                i += 2;
            } else {
                ++i;
            }
        }
        if (cnt >= p)
            right = mid;
        else
            left = mid + 1;
    }
    
    return left;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimizeMax(int[] nums, int p) {
        if (p == 0) return 0;
        Array.Sort(nums);
        int n = nums.Length;
        int left = 0;
        int right = nums[n - 1] - nums[0];
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (CanFormPairs(nums, p, mid))
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }

    private bool CanFormPairs(int[] sorted, int p, int maxDiff) {
        int cnt = 0;
        for (int i = 0; i < sorted.Length - 1 && cnt < p;) {
            if (sorted[i + 1] - sorted[i] <= maxDiff) {
                cnt++;
                i += 2;
            } else {
                i++;
            }
        }
        return cnt >= p;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} p
 * @return {number}
 */
var minimizeMax = function(nums, p) {
    if (p === 0) return 0;
    nums.sort((a, b) => a - b);
    const n = nums.length;
    let left = 0;
    let right = nums[n - 1] - nums[0];
    
    const canForm = (limit) => {
        let cnt = 0;
        for (let i = 0; i < n - 1;) {
            if (nums[i + 1] - nums[i] <= limit) {
                cnt++;
                i += 2;
                if (cnt >= p) return true;
            } else {
                i++;
            }
        }
        return cnt >= p;
    };
    
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (canForm(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
};
```

## Typescript

```typescript
function minimizeMax(nums: number[], p: number): number {
    if (p === 0) return 0;
    nums.sort((a, b) => a - b);
    const n = nums.length;

    const can = (limit: number): boolean => {
        let cnt = 0;
        for (let i = 0; i < n - 1;) {
            if (nums[i + 1] - nums[i] <= limit) {
                cnt++;
                i += 2;
                if (cnt >= p) return true;
            } else {
                i++;
            }
        }
        return cnt >= p;
    };

    let left = 0;
    let right = nums[n - 1] - nums[0];
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (can(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $p
     * @return Integer
     */
    function minimizeMax($nums, $p) {
        $n = count($nums);
        if ($p == 0) return 0;
        sort($nums);
        $left = 0;
        $right = $nums[$n - 1] - $nums[0];
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($this->canForm($nums, $p, $mid)) {
                $right = $mid;
            } else {
                $left = $mid + 1;
            }
        }
        return $left;
    }

    private function canForm($arr, $p, $limit) {
        $cnt = 0;
        $i = 0;
        $n = count($arr);
        while ($i < $n - 1) {
            if ($arr[$i + 1] - $arr[$i] <= $limit) {
                $cnt++;
                if ($cnt >= $p) return true;
                $i += 2;
            } else {
                $i++;
            }
        }
        return $cnt >= $p;
    }
}
```

## Swift

```swift
class Solution {
    func minimizeMax(_ nums: [Int], _ p: Int) -> Int {
        if p == 0 { return 0 }
        let sorted = nums.sorted()
        let n = sorted.count
        var left = 0
        var right = sorted[n - 1] - sorted[0]
        
        while left < right {
            let mid = (left + right) / 2
            var count = 0
            var i = 0
            while i + 1 < n {
                if sorted[i + 1] - sorted[i] <= mid {
                    count += 1
                    i += 2
                } else {
                    i += 1
                }
            }
            if count >= p {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimizeMax(nums: IntArray, p: Int): Int {
        if (p == 0) return 0
        nums.sort()
        val n = nums.size
        var left = 0
        var right = nums[n - 1] - nums[0]

        fun can(limit: Int): Boolean {
            var cnt = 0
            var i = 0
            while (i + 1 < n) {
                if (nums[i + 1] - nums[i] <= limit) {
                    cnt++
                    i += 2
                } else {
                    i++
                }
                if (cnt >= p) return true
            }
            return false
        }

        while (left < right) {
            val mid = left + (right - left) / 2
            if (can(mid)) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
}
```

## Dart

```dart
class Solution {
  int minimizeMax(List<int> nums, int p) {
    if (p == 0) return 0;
    nums.sort();
    int n = nums.length;

    bool can(int limit) {
      int cnt = 0;
      for (int i = 0; i + 1 < n;) {
        if (nums[i + 1] - nums[i] <= limit) {
          cnt++;
          i += 2;
        } else {
          i += 1;
        }
        if (cnt >= p) return true;
      }
      return cnt >= p;
    }

    int left = 0;
    int right = nums[n - 1] - nums[0];
    while (left < right) {
      int mid = left + ((right - left) >> 1);
      if (can(mid)) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return left;
  }
}
```

## Golang

```go
package main

import "sort"

func minimizeMax(nums []int, p int) int {
	if p == 0 {
		return 0
	}
	sort.Ints(nums)
	n := len(nums)

	can := func(limit int) bool {
		cnt, i := 0, 0
		for i < n-1 {
			if nums[i+1]-nums[i] <= limit {
				cnt++
				i += 2
				if cnt >= p {
					return true
				}
			} else {
				i++
			}
		}
		return cnt >= p
	}

	left, right := 0, nums[n-1]-nums[0]
	for left < right {
		mid := left + (right-left)/2
		if can(mid) {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
}
```

## Ruby

```ruby
def minimize_max(nums, p)
  return 0 if p == 0
  nums.sort!
  n = nums.length
  left = 0
  right = nums[-1] - nums[0]

  possible = lambda do |limit|
    cnt = 0
    i = 0
    while i < n - 1
      if nums[i + 1] - nums[i] <= limit
        cnt += 1
        i += 2
      else
        i += 1
      end
    end
    cnt >= p
  end

  while left < right
    mid = (left + right) / 2
    if possible.call(mid)
      right = mid
    else
      left = mid + 1
    end
  end
  left
end
```

## Scala

```scala
object Solution {
    def minimizeMax(nums: Array[Int], p: Int): Int = {
        val n = nums.length
        if (p == 0) return 0
        java.util.Arrays.sort(nums)
        var left = 0
        var right = nums(n - 1) - nums(0)

        def can(limit: Int): Boolean = {
            var cnt = 0
            var i = 0
            while (i < n - 1 && cnt < p) {
                if (nums(i + 1) - nums(i) <= limit) {
                    cnt += 1
                    i += 2
                } else {
                    i += 1
                }
            }
            cnt >= p
        }

        while (left < right) {
            val mid = left + (right - left) / 2
            if (can(mid)) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        left
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimize_max(nums: Vec<i32>, p: i32) -> i32 {
        let n = nums.len();
        if p == 0 || n < 2 {
            return 0;
        }
        let mut arr: Vec<i64> = nums.into_iter().map(|x| x as i64).collect();
        arr.sort_unstable();
        let need = p as usize;
        let mut lo = 0i64;
        let mut hi = arr[n - 1] - arr[0];
        while lo < hi {
            let mid = (lo + hi) / 2;
            if Self::can(&arr, need, mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }

    fn can(arr: &Vec<i64>, p: usize, limit: i64) -> bool {
        let mut cnt = 0usize;
        let n = arr.len();
        let mut i = 0usize;
        while i + 1 < n {
            if arr[i + 1] - arr[i] <= limit {
                cnt += 1;
                if cnt >= p {
                    return true;
                }
                i += 2;
            } else {
                i += 1;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (minimize-max nums p)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (if (= p 0)
      0
      (let* ((sorted (sort nums <))
             (vec (list->vector sorted))
             (n (vector-length vec))
             (left 0)
             (right (- (vector-ref vec (- n 1)) (vector-ref vec 0))))
        (define (count-pairs thresh)
          (let loop ((i 0) (cnt 0))
            (if (or (>= i (- n 1)) (= cnt p))
                cnt
                (if (<= (- (vector-ref vec (+ i 1)) (vector-ref vec i)) thresh)
                    (loop (+ i 2) (+ cnt 1))
                    (loop (+ i 1) cnt)))))
        (let rec ((l left) (r right))
          (if (= l r)
              l
              (let* ((mid (quotient (+ l r) 2))
                     (cnt (count-pairs mid)))
                (if (>= cnt p)
                    (rec l mid)
                    (rec (+ mid 1) r))))))))
```

## Erlang

```erlang
-module(solution).
-export([minimize_max/2]).

-spec minimize_max(Nums :: [integer()], P :: integer()) -> integer().
minimize_max(_Nums, 0) ->
    0;
minimize_max(Nums, P) ->
    Sorted = lists:sort(Nums),
    MinVal = hd(Sorted),
    MaxVal = lists:last(Sorted),
    Right = MaxVal - MinVal,
    binary_search(0, Right, Sorted, P).

binary_search(L, R, _Sorted, _P) when L >= R ->
    L;
binary_search(L, R, Sorted, P) ->
    Mid = (L + R) div 2,
    Count = count_pairs(Sorted, Mid),
    if
        Count >= P ->
            binary_search(L, Mid, Sorted, P);
        true ->
            binary_search(Mid + 1, R, Sorted, P)
    end.

count_pairs(List, Threshold) ->
    count_pairs(List, Threshold, 0).

count_pairs([], _Threshold, Acc) ->
    Acc;
count_pairs([_], _Threshold, Acc) ->
    Acc;
count_pairs([A, B | Rest], Threshold, Acc) ->
    if
        B - A =< Threshold ->
            count_pairs(Rest, Threshold, Acc + 1);
        true ->
            count_pairs([B | Rest], Threshold, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimize_max(nums :: [integer], p :: integer) :: integer
  def minimize_max(nums, p) do
    if p == 0 do
      0
    else
      sorted = Enum.sort(nums)
      left = 0
      right = List.last(sorted) - hd(sorted)
      binary_search(sorted, p, left, right)
    end
  end

  defp binary_search(_sorted, _p, left, right) when left == right do
    left
  end

  defp binary_search(sorted, p, left, right) do
    mid = div(left + right, 2)

    if can_form?(sorted, p, mid) do
      binary_search(sorted, p, left, mid)
    else
      binary_search(sorted, p, mid + 1, right)
    end
  end

  defp can_form?(sorted, p, limit) do
    greedy_count(sorted, limit, 0) >= p
  end

  defp greedy_count([], _limit, acc), do: acc
  defp greedy_count([_], _limit, acc), do: acc

  defp greedy_count([a, b | rest], limit, acc) do
    if b - a <= limit do
      greedy_count(rest, limit, acc + 1)
    else
      greedy_count([b | rest], limit, acc)
    end
  end
end
```
