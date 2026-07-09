# 2560. House Robber IV

## Cpp

```cpp
class Solution {
public:
    bool can(const vector<int>& nums, int k, long long cap) {
        int cnt = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] <= cap) {
                ++cnt;
                ++i; // skip next house
                if (cnt >= k) return true;
            }
        }
        return cnt >= k;
    }

    int minCapability(vector<int>& nums, int k) {
        long long left = *min_element(nums.begin(), nums.end());
        long long right = *max_element(nums.begin(), nums.end());
        while (left < right) {
            long long mid = left + (right - left) / 2;
            if (can(nums, k, mid))
                right = mid;
            else
                left = mid + 1;
        }
        return (int)left;
    }
};
```

## Java

```java
class Solution {
    public int minCapability(int[] nums, int k) {
        int left = 1;
        int right = 0;
        for (int v : nums) {
            if (v > right) right = v;
        }
        while (left < right) {
            int mid = left + ((right - left) >> 1);
            if (canRob(nums, k, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private boolean canRob(int[] nums, int k, int cap) {
        int cnt = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] <= cap) {
                cnt++;
                i++; // skip next house
                if (cnt >= k) return true;
            }
        }
        return cnt >= k;
    }
}
```

## Python

```python
class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def can(cap):
            cnt = 0
            i = 0
            n = len(nums)
            while i < n:
                if nums[i] <= cap:
                    cnt += 1
                    i += 2  # skip next house
                else:
                    i += 1
                if cnt >= k:  # early exit
                    return True
            return cnt >= k

        left, right = 1, max(nums)
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
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        lo, hi = min(nums), max(nums)

        def can(cap: int) -> bool:
            cnt = 0
            i = 0
            n = len(nums)
            while i < n:
                if nums[i] <= cap:
                    cnt += 1
                    i += 2  # skip next house
                else:
                    i += 1
                if cnt >= k:
                    return True
            return False

        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## C

```c
int minCapability(int* nums, int numsSize, int k) {
    int lo = nums[0], hi = nums[0];
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] < lo) lo = nums[i];
        if (nums[i] > hi) hi = nums[i];
    }
    int left = lo, right = hi;
    while (left < right) {
        int mid = left + (right - left) / 2;
        int cnt = 0;
        for (int i = 0; i < numsSize; ++i) {
            if (nums[i] <= mid) {
                ++cnt;
                ++i; // skip next house
            }
        }
        if (cnt >= k)
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
    public int MinCapability(int[] nums, int k) {
        int left = 1;
        int right = 0;
        foreach (int v in nums) if (v > right) right = v;

        while (left < right) {
            int mid = left + ((right - left) >> 1);
            if (CanRobAtLeastK(nums, k, mid))
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }

    private bool CanRobAtLeastK(int[] nums, int k, int limit) {
        int count = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] <= limit) {
                count++;
                i++; // skip next house
                if (count >= k) return true;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
var minCapability = function(nums, k) {
    let left = nums[0], right = nums[0];
    for (const v of nums) {
        if (v < left) left = v;
        if (v > right) right = v;
    }
    const can = (limit) => {
        let cnt = 0;
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] <= limit) {
                cnt++;
                i++; // skip next house
            }
        }
        return cnt >= k;
    };
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (can(mid)) {
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
function minCapability(nums: number[], k: number): number {
    let left = Math.min(...nums);
    let right = Math.max(...nums);

    const can = (cap: number): boolean => {
        let cnt = 0;
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] <= cap) {
                cnt++;
                i++; // skip next house
                if (cnt >= k) return true;
            }
        }
        return cnt >= k;
    };

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
     * @param Integer $k
     * @return Integer
     */
    function minCapability($nums, $k) {
        $left = 1;
        $right = max($nums);
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            $cnt = 0;
            $n = count($nums);
            for ($i = 0; $i < $n; $i++) {
                if ($nums[$i] <= $mid) {
                    $cnt++;
                    $i++; // skip next house
                }
            }
            if ($cnt >= $k) {
                $right = $mid;
            } else {
                $left = $mid + 1;
            }
        }
        return $left;
    }
}
```

## Swift

```swift
class Solution {
    func minCapability(_ nums: [Int], _ k: Int) -> Int {
        var left = 0
        var right = nums.max()!
        while left < right {
            let mid = (left + right) / 2
            if canRob(atMost: mid, in: nums, need: k) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }
    
    private func canRob(atMost limit: Int, in nums: [Int], need k: Int) -> Bool {
        var count = 0
        var i = 0
        while i < nums.count {
            if nums[i] <= limit {
                count += 1
                i += 2   // skip next house
            } else {
                i += 1
            }
        }
        return count >= k
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCapability(nums: IntArray, k: Int): Int {
        var left = nums.minOrNull()!!
        var right = nums.maxOrNull()!!

        while (left < right) {
            val mid = left + ((right - left) ushr 1)
            if (canRob(nums, k, mid)) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        return left
    }

    private fun canRob(nums: IntArray, k: Int, limit: Int): Boolean {
        var count = 0
        var i = 0
        val n = nums.size
        while (i < n) {
            if (nums[i] <= limit) {
                count++
                if (count >= k) return true
                i += 2
            } else {
                i++
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  int minCapability(List<int> nums, int k) {
    int left = 1;
    int right = nums.reduce((a, b) => a > b ? a : b);
    while (left < right) {
      int mid = left + ((right - left) >> 1);
      if (_canRobAtLeastK(nums, k, mid)) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return left;
  }

  bool _canRobAtLeastK(List<int> nums, int k, int cap) {
    int count = 0;
    for (int i = 0; i < nums.length;) {
      if (nums[i] <= cap) {
        count++;
        if (count >= k) return true;
        i += 2; // skip next house
      } else {
        i++;
      }
    }
    return false;
  }
}
```

## Golang

```go
func minCapability(nums []int, k int) int {
    left, right := 1, nums[0]
    for _, v := range nums {
        if v > right {
            right = v
        }
    }
    for left < right {
        mid := left + (right-left)/2
        cnt := 0
        for i := 0; i < len(nums); {
            if nums[i] <= mid {
                cnt++
                i += 2
            } else {
                i++
            }
        }
        if cnt >= k {
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
def min_capability(nums, k)
  left = nums.min
  right = nums.max
  while left < right
    mid = (left + right) / 2
    cnt = 0
    i = 0
    n = nums.length
    while i < n
      if nums[i] <= mid
        cnt += 1
        i += 2
      else
        i += 1
      end
    end
    if cnt >= k
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
    def minCapability(nums: Array[Int], k: Int): Int = {
        var left = nums.min
        var right = nums.max
        while (left < right) {
            val mid = left + ((right - left) >>> 1)
            var cnt = 0
            var i = 0
            while (i < nums.length && cnt < k) {
                if (nums(i) <= mid) {
                    cnt += 1
                    i += 2
                } else {
                    i += 1
                }
            }
            if (cnt >= k) right = mid else left = mid + 1
        }
        left
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_capability(nums: Vec<i32>, k: i32) -> i32 {
        fn can(nums: &Vec<i32>, cap: i32) -> i32 {
            let mut cnt = 0;
            let mut i = 0usize;
            while i < nums.len() {
                if nums[i] <= cap {
                    cnt += 1;
                    i += 2;
                } else {
                    i += 1;
                }
            }
            cnt
        }

        let mut lo = *nums.iter().min().unwrap();
        let mut hi = *nums.iter().max().unwrap();

        while lo < hi {
            let mid = lo + ((hi - lo) >> 1);
            if can(&nums, mid) >= k {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
```

## Racket

```racket
(define/contract (min-capability nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((left (apply min nums))
         (right (apply max nums)))
    (define (can? cap)
      (let recur ((lst nums) (cnt 0))
        (if (null? lst)
            (>= cnt k)
            (if (<= (car lst) cap)
                (recur (cddr lst) (+ cnt 1))
                (recur (cdr lst) cnt)))))
    (let loop ((lo left) (hi right))
      (if (= lo hi)
          lo
          (let ((mid (quotient (+ lo hi) 2)))
            (if (can? mid)
                (loop lo mid)
                (loop (+ mid 1) hi)))))))
```

## Erlang

```erlang
-module(solution).
-export([min_capability/2]).

-spec min_capability(Nums :: [integer()], K :: integer()) -> integer().
min_capability(Nums, K) ->
    Max = lists:max(Nums),
    Min = lists:min(Nums),
    binary_search(Min, Max, K, Nums).

binary_search(L, R, K, Nums) when L < R ->
    Mid = (L + R) div 2,
    case feasible(Nums, Mid, K) of
        true -> binary_search(L, Mid, K, Nums);
        false -> binary_search(Mid + 1, R, K, Nums)
    end;
binary_search(L, _R, _K, _Nums) ->
    L.

feasible([], _Cap, _Need) ->
    false;
feasible(_List, _Cap, Need) when Need =< 0 ->
    true;
feasible([H|T], Cap, Need) ->
    if
        H =< Cap ->
            NewNeed = Need - 1,
            case NewNeed of
                0 -> true;
                _ -> feasible(skip_one(T), Cap, NewNeed)
            end;
        true ->
            feasible(T, Cap, Need)
    end.

skip_one([]) -> [];
skip_one([_|Rest]) -> Rest.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_capability(nums :: [integer], k :: integer) :: integer
  def min_capability(nums, k) do
    left = Enum.min(nums)
    right = Enum.max(nums)

    binary_search(left, right, nums, k)
  end

  defp binary_search(l, r, _nums, _k) when l == r, do: l

  defp binary_search(l, r, nums, k) do
    mid = div(l + r, 2)

    if can?(mid, nums, k) do
      binary_search(l, mid, nums, k)
    else
      binary_search(mid + 1, r, nums, k)
    end
  end

  defp can?(cap, nums, k) do
    {cnt, _skip} =
      Enum.reduce(nums, {0, false}, fn val, {c, skip} ->
        cond do
          skip -> {c, false}
          val <= cap -> {c + 1, true}
          true -> {c, false}
        end
      end)

    cnt >= k
  end
end
```
