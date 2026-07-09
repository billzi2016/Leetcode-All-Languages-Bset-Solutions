# 2856. Minimum Array Length After Pair Removals

## Cpp

```cpp
class Solution {
public:
    int minLengthAfterRemovals(vector<int>& nums) {
        int i = 0, j = (int)nums.size() - 1;
        while (i < j && nums[i] < nums[j]) {
            ++i;
            --j;
        }
        return max(0, j - i + 1);
    }
};
```

## Java

```java
class Solution {
    public int minLengthAfterRemovals(List<Integer> nums) {
        int n = nums.size();
        int low = 0, high = n / 2;
        while (low < high) {
            int mid = (low + high + 1) >>> 1; // upper middle
            if (isValid(nums, n, mid)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return n - 2 * low;
    }

    private boolean isValid(List<Integer> nums, int n, int k) {
        for (int i = 0; i < k; i++) {
            if (nums.get(i) >= nums.get(n - k + i)) {
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
    def minLengthAfterRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lo, hi = 0, n // 2

        # helper to check if k pairs can be removed
        def valid(k):
            for i in range(k):
                if nums[i] >= nums[n - k + i]:
                    return False
            return True

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if valid(mid):
                lo = mid
            else:
                hi = mid - 1

        return n - 2 * lo
```

## Python3

```python
from typing import List

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n // 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            ok = True
            for i in range(mid):
                if nums[i] >= nums[n - mid + i]:
                    ok = False
                    break
            if ok:
                lo = mid
            else:
                hi = mid - 1
        return n - 2 * lo
```

## C

```c
int minLengthAfterRemovals(int* nums, int numsSize) {
    int low = 0, high = numsSize / 2;
    while (low < high) {
        int mid = (low + high + 1) / 2;
        int ok = 1;
        for (int i = 0; i < mid; ++i) {
            if (nums[i] >= nums[numsSize - mid + i]) {
                ok = 0;
                break;
            }
        }
        if (ok)
            low = mid;
        else
            high = mid - 1;
    }
    return numsSize - 2 * low;
}
```

## Csharp

```csharp
public class Solution {
    public int MinLengthAfterRemovals(IList<int> nums) {
        int n = nums.Count;
        int left = 0, right = n - 1, pairs = 0;
        while (left < right && nums[left] < nums[right]) {
            pairs++;
            left++;
            right--;
        }
        return n - 2 * pairs;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minLengthAfterRemovals = function(nums) {
    let left = 0;
    let right = nums.length - 1;
    let pairs = 0;
    while (left < right && nums[left] < nums[right]) {
        pairs++;
        left++;
        right--;
    }
    return nums.length - 2 * pairs;
};
```

## Typescript

```typescript
function minLengthAfterRemovals(nums: number[]): number {
    const n = nums.length;
    let low = 0, high = Math.floor(n / 2);
    
    const isValid = (k: number): boolean => {
        for (let i = 0; i < k; ++i) {
            if (nums[i] >= nums[n - k + i]) return false;
        }
        return true;
    };
    
    while (low < high) {
        const mid = Math.floor((low + high + 1) / 2);
        if (isValid(mid)) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    
    return n - 2 * low;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minLengthAfterRemovals($nums) {
        $n = count($nums);
        $i = 0;
        $j = $n - 1;
        $pairs = 0;
        while ($i < $j && $nums[$i] < $nums[$j]) {
            $pairs++;
            $i++;
            $j--;
        }
        return $n - 2 * $pairs;
    }
}
```

## Swift

```swift
class Solution {
    func minLengthAfterRemovals(_ nums: [Int]) -> Int {
        var left = 0
        var right = nums.count - 1
        var pairs = 0
        while left < right && nums[left] < nums[right] {
            pairs += 1
            left += 1
            right -= 1
        }
        return nums.count - 2 * pairs
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minLengthAfterRemovals(nums: List<Int>): Int {
        val n = nums.size
        var lo = 0
        var hi = n / 2
        while (lo < hi) {
            val mid = (lo + hi + 1) / 2
            if (isValid(mid, nums)) {
                lo = mid
            } else {
                hi = mid - 1
            }
        }
        return n - 2 * lo
    }

    private fun isValid(k: Int, nums: List<Int>): Boolean {
        val n = nums.size
        for (i in 0 until k) {
            if (nums[i] >= nums[n - k + i]) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  int minLengthAfterRemovals(List<int> nums) {
    int n = nums.length;
    int lo = 0, hi = n ~/ 2;
    while (lo < hi) {
      int mid = (lo + hi + 1) >> 1;
      bool ok = true;
      for (int i = 0; i < mid; ++i) {
        if (nums[i] >= nums[n - mid + i]) {
          ok = false;
          break;
        }
      }
      if (ok) {
        lo = mid;
      } else {
        hi = mid - 1;
      }
    }
    return n - 2 * lo;
  }
}
```

## Golang

```go
func minLengthAfterRemovals(nums []int) int {
    n := len(nums)
    lo, hi := 0, n/2

    valid := func(k int) bool {
        for i := 0; i < k; i++ {
            if !(nums[i] < nums[n-k+i]) {
                return false
            }
        }
        return true
    }

    for lo < hi {
        mid := (lo + hi + 1) / 2
        if valid(mid) {
            lo = mid
        } else {
            hi = mid - 1
        }
    }
    return n - 2*lo
}
```

## Ruby

```ruby
def min_length_after_removals(nums)
  n = nums.length
  lo = 0
  hi = n / 2
  while lo < hi
    mid = (lo + hi + 1) / 2
    valid = true
    i = 0
    while i < mid
      if !(nums[i] < nums[n - mid + i])
        valid = false
        break
      end
      i += 1
    end
    if valid
      lo = mid
    else
      hi = mid - 1
    end
  end
  n - 2 * lo
end
```

## Scala

```scala
object Solution {
    def minLengthAfterRemovals(nums: List[Int]): Int = {
        val arr = nums.toArray
        var left = 0
        var right = arr.length - 1
        var pairs = 0
        while (left < right && arr(left) < arr(right)) {
            pairs += 1
            left += 1
            right -= 1
        }
        arr.length - 2 * pairs
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_length_after_removals(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut lo = 0usize;
        let mut hi = n / 2;
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if Self::valid(&nums, mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        (n - 2 * lo) as i32
    }

    fn valid(nums: &[i32], k: usize) -> bool {
        let n = nums.len();
        for i in 0..k {
            if nums[i] >= nums[n - k + i] {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (min-length-after-removals nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (v (list->vector nums))
         (maxk (quotient n 2)))
    (define (valid? k)
      (let loop ((i 0))
        (or (= i k)
            (and (< (vector-ref v i)
                    (vector-ref v (+ (- n k) i)))
                 (loop (+ i 1))))))
    (let rec ((low 0) (high maxk))
      (if (= low high)
          (- n (* 2 low))
          (let* ((mid (quotient (+ low high 1) 2)))
            (if (valid? mid)
                (rec mid high)
                (rec low (- mid 1))))))))
```

## Erlang

```erlang
-spec min_length_after_removals(Nums :: [integer()]) -> integer().
min_length_after_removals(Nums) ->
    Tuple = list_to_tuple(Nums),
    Len = tuple_size(Tuple),
    MaxK = binary_search(0, Len div 2, Tuple, Len),
    Len - 2 * MaxK.

binary_search(Low, High, Tuple, Len) when Low =< High ->
    Mid = (Low + High) bsr 1,
    case check(Mid, Tuple, Len) of
        true -> binary_search(Mid + 1, High, Tuple, Len);
        false -> binary_search(Low, Mid - 1, Tuple, Len)
    end;
binary_search(_, High, _, _) ->
    High.

check(0, _, _) -> true;
check(K, Tuple, Len) ->
    StartRight = Len - K,
    check_loop(0, K, Tuple, StartRight).

check_loop(I, K, _Tuple, _StartRight) when I >= K -> true;
check_loop(I, K, Tuple, StartRight) ->
    A = element(I + 1, Tuple),
    B = element(StartRight + I + 1, Tuple),
    if
        A < B -> check_loop(I + 1, K, Tuple, StartRight);
        true -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_length_after_removals(nums :: [integer]) :: integer
  def min_length_after_removals(nums) do
    n = length(nums)
    arr = List.to_tuple(nums)
    max_k = binary_search(arr, n, 0, div(n, 2))
    n - 2 * max_k
  end

  defp binary_search(_arr, _n, low, high) when low >= high, do: low

  defp binary_search(arr, n, low, high) do
    mid = div(low + high + 1, 2)

    if valid?(arr, n, mid) do
      binary_search(arr, n, mid, high)
    else
      binary_search(arr, n, low, mid - 1)
    end
  end

  defp valid?(_arr, _n, 0), do: true

  defp valid?(arr, n, k) do
    0..(k - 1)
    |> Enum.reduce_while(true, fn i, _acc ->
      if elem(arr, i) < elem(arr, n - k + i) do
        {:cont, true}
      else
        {:halt, false}
      end
    end)
  end
end
```
