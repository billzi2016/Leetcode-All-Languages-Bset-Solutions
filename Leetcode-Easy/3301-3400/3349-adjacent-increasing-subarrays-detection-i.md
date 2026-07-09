# 3349. Adjacent Increasing Subarrays Detection I

## Cpp

```cpp
class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> inc_end(n);
        inc_end[0] = 1;
        for (int i = 1; i < n; ++i) {
            if (nums[i] > nums[i - 1])
                inc_end[i] = inc_end[i - 1] + 1;
            else
                inc_end[i] = 1;
        }
        vector<char> good(n, 0); // good[start] indicates subarray [start, start+k-1] is strictly increasing
        for (int start = 0; start + k - 1 < n; ++start) {
            if (inc_end[start + k - 1] >= k)
                good[start] = 1;
        }
        for (int a = 0; a + 2 * k <= n; ++a) {
            if (good[a] && good[a + k])
                return true;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
        int n = nums.size();
        // Need two adjacent subarrays of length k: total length 2k
        for (int start = 0; start <= n - 2 * k; start++) {
            if (isStrictlyIncreasing(nums, start, start + k - 1) &&
                isStrictlyIncreasing(nums, start + k, start + 2 * k - 1)) {
                return true;
            }
        }
        return false;
    }

    private boolean isStrictlyIncreasing(List<Integer> nums, int l, int r) {
        for (int i = l + 1; i <= r; i++) {
            if (nums.get(i) <= nums.get(i - 1)) {
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
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        # precompute whether subarray of length k starting at i is strictly increasing
        good = [False] * (n - k + 1)
        for i in range(n - k + 1):
            inc = True
            for j in range(i, i + k - 1):
                if nums[j] >= nums[j + 1]:
                    inc = False
                    break
            good[i] = inc

        # check adjacent windows
        for a in range(0, n - 2 * k + 1):
            if good[a] and good[a + k]:
                return True
        return False
```

## Python3

```python
class Solution:
    def hasIncreasingSubarrays(self, nums, k):
        n = len(nums)
        # Helper to check if subarray nums[l:l+k] is strictly increasing
        def inc(l):
            for i in range(l, l + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True

        for start in range(n - 2 * k + 1):
            if inc(start) and inc(start + k):
                return True
        return False
```

## C

```c
#include <stdbool.h>

bool hasIncreasingSubarrays(int* nums, int numsSize, int k) {
    if (numsSize < 2 * k) return false;

    int inc[101]; // numsSize ≤ 100
    inc[numsSize - 1] = 1;
    for (int i = numsSize - 2; i >= 0; --i) {
        inc[i] = (nums[i] < nums[i + 1]) ? inc[i + 1] + 1 : 1;
    }

    for (int i = 0; i <= numsSize - 2 * k; ++i) {
        if (inc[i] >= k && inc[i + k] >= k) return true;
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool HasIncreasingSubarrays(IList<int> nums, int k) {
        int n = nums.Count;
        // Precompute whether a subarray of length k starting at i is strictly increasing
        bool[] incStart = new bool[n];
        for (int i = 0; i + k <= n; i++) {
            bool ok = true;
            for (int j = i + 1; j < i + k; j++) {
                if (nums[j] <= nums[j - 1]) {
                    ok = false;
                    break;
                }
            }
            incStart[i] = ok;
        }

        // Check for two adjacent increasing subarrays
        for (int i = 0; i + 2 * k <= n; i++) {
            if (incStart[i] && incStart[i + k]) {
                return true;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var hasIncreasingSubarrays = function(nums, k) {
    const n = nums.length;
    const inc = new Array(n).fill(1);
    for (let i = n - 2; i >= 0; --i) {
        if (nums[i] < nums[i + 1]) {
            inc[i] = inc[i + 1] + 1;
        }
    }
    for (let i = 0; i <= n - 2 * k; ++i) {
        if (inc[i] >= k && inc[i + k] >= k) return true;
    }
    return false;
};
```

## Typescript

```typescript
function hasIncreasingSubarrays(nums: number[], k: number): boolean {
    const n = nums.length;
    const inc: boolean[] = new Array(n).fill(false);
    
    // Determine if each subarray of length k is strictly increasing
    for (let i = 0; i <= n - k; i++) {
        let ok = true;
        for (let j = i + 1; j < i + k; j++) {
            if (nums[j] <= nums[j - 1]) {
                ok = false;
                break;
            }
        }
        inc[i] = ok;
    }
    
    // Check for two adjacent increasing subarrays
    for (let i = 0; i <= n - 2 * k; i++) {
        if (inc[i] && inc[i + k]) {
            return true;
        }
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function hasIncreasingSubarrays($nums, $k) {
        $n = count($nums);
        if ($n < 2 * $k) return false;

        // pair[i] = 1 if nums[i] < nums[i+1]
        $pair = array_fill(0, $n - 1, 0);
        for ($i = 0; $i < $n - 1; $i++) {
            $pair[$i] = ($nums[$i] < $nums[$i + 1]) ? 1 : 0;
        }

        // prefix sums of pair
        $prefix = array_fill(0, $n, 0); // prefix[0]=0
        for ($i = 0; $i < $n - 1; $i++) {
            $prefix[$i + 1] = $prefix[$i] + $pair[$i];
        }

        // good[i] true if subarray starting at i of length k is strictly increasing
        $good = array_fill(0, $n, false);
        for ($i = 0; $i <= $n - $k; $i++) {
            $sum = $prefix[$i + $k - 1] - $prefix[$i]; // sum of pair[i .. i+k-2]
            if ($sum == $k - 1) {
                $good[$i] = true;
            }
        }

        for ($i = 0; $i <= $n - 2 * $k; $i++) {
            if ($good[$i] && $good[$i + $k]) {
                return true;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func hasIncreasingSubarrays(_ nums: [Int], _ k: Int) -> Bool {
        let n = nums.count
        var inc = Array(repeating: 1, count: n)
        if n >= 2 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                if nums[i] < nums[i + 1] {
                    inc[i] = inc[i + 1] + 1
                }
            }
        }
        if n < 2 * k { return false }
        for i in 0...(n - 2 * k) {
            if inc[i] >= k && inc[i + k] >= k {
                return true
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun hasIncreasingSubarrays(nums: List<Int>, k: Int): Boolean {
        val n = nums.size
        if (2 * k > n) return false

        fun isInc(start: Int): Boolean {
            for (i in start until start + k - 1) {
                if (nums[i] >= nums[i + 1]) return false
            }
            return true
        }

        for (start in 0..n - 2 * k) {
            if (isInc(start) && isInc(start + k)) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool hasIncreasingSubarrays(List<int> nums, int k) {
    int n = nums.length;
    List<bool> good = List.filled(n, false);
    for (int i = 0; i <= n - k; ++i) {
      bool ok = true;
      for (int j = i + 1; j < i + k; ++j) {
        if (nums[j] <= nums[j - 1]) {
          ok = false;
          break;
        }
      }
      good[i] = ok;
    }
    for (int i = 0; i <= n - 2 * k; ++i) {
      if (good[i] && good[i + k]) return true;
    }
    return false;
  }
}
```

## Golang

```go
func hasIncreasingSubarrays(nums []int, k int) bool {
	n := len(nums)
	if n < 2*k {
		return false
	}
	inc := make([]bool, n)
	// Determine increasing windows of length k
	for i := 0; i+k <= n; i++ {
		ok := true
		for j := i + 1; j < i+k; j++ {
			if nums[j] <= nums[j-1] {
				ok = false
				break
			}
		}
		inc[i] = ok
	}
	// Check for two adjacent windows
	for i := 0; i+2*k <= n; i++ {
		if inc[i] && inc[i+k] {
			return true
		}
	}
	return false
}
```

## Ruby

```ruby
def has_increasing_subarrays(nums, k)
  n = nums.length
  good = Array.new(n, false)

  (0..n - k).each do |i|
    inc = true
    (i...(i + k - 1)).each do |j|
      unless nums[j] < nums[j + 1]
        inc = false
        break
      end
    end
    good[i] = inc
  end

  (0..n - 2 * k).each do |i|
    return true if good[i] && good[i + k]
  end
  false
end
```

## Scala

```scala
object Solution {
    def hasIncreasingSubarrays(nums: List[Int], k: Int): Boolean = {
        val n = nums.length
        for (i <- 0 to n - 2 * k) {
            var ok = true
            // first subarray [i, i+k)
            var j = i + 1
            while (j < i + k && ok) {
                if (nums(j) <= nums(j - 1)) ok = false
                j += 1
            }
            // second subarray [i+k, i+2k)
            j = i + k + 1
            while (j < i + 2 * k && ok) {
                if (nums(j) <= nums(j - 1)) ok = false
                j += 1
            }
            if (ok) return true
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn has_increasing_subarrays(nums: Vec<i32>, k: i32) -> bool {
        let n = nums.len();
        let k = k as usize;
        if 2 * k > n {
            return false;
        }
        for start in 0..=n - 2 * k {
            // check first subarray
            let mut ok = true;
            for j in start..start + k - 1 {
                if nums[j] >= nums[j + 1] {
                    ok = false;
                    break;
                }
            }
            if !ok {
                continue;
            }
            // check second subarray
            for j in start + k..start + 2 * k - 1 {
                if nums[j] >= nums[j + 1] {
                    ok = false;
                    break;
                }
            }
            if ok {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (has-increasing-subarrays nums k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (define (increasing? start)
      (let loop ((j start))
        (if (= j (+ start (- k 1))) ; reached last element of the subarray
            #t
            (and (< (vector-ref v j) (vector-ref v (+ j 1)))
                 (loop (+ j 1))))))
    (let loop ((i 0))
      (cond [(> i (- n (* 2 k))) #f]
            [(and (increasing? i) (increasing? (+ i k))) #t]
            [else (loop (+ i 1))]))))
```

## Erlang

```erlang
-module(solution).
-export([has_increasing_subarrays/2]).

-spec has_increasing_subarrays(Nums :: [integer()], K :: integer()) -> boolean().
has_increasing_subarrays(Nums, K) ->
    N = length(Nums),
    MaxStart = N - 2 * K,
    check_adjacent(Nums, K, 0, MaxStart).

check_adjacent(_Nums, _K, Index, Max) when Index > Max ->
    false;
check_adjacent(Nums, K, Index, Max) ->
    case inc_subarray(Nums, Index, K) andalso inc_subarray(Nums, Index + K, K) of
        true -> true;
        false -> check_adjacent(Nums, K, Index + 1, Max)
    end.

inc_subarray(_Nums, _Start, K) when K =< 1 ->
    true;
inc_subarray(Nums, Start, K) ->
    inc_check(Nums, Start, K - 1).

inc_check(_Nums, _Pos, 0) ->
    true;
inc_check(Nums, Pos, Rem) ->
    A = lists:nth(Pos + 1, Nums),
    B = lists:nth(Pos + 2, Nums),
    if
        A < B -> inc_check(Nums, Pos + 1, Rem - 1);
        true -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec has_increasing_subarrays(nums :: [integer], k :: integer) :: boolean
  def has_increasing_subarrays(nums, k) do
    n = length(nums)
    max_start = n - 2 * k

    Enum.any?(0..max_start, fn i ->
      increasing?(nums, i, k) and increasing?(nums, i + k, k)
    end)
  end

  defp increasing?(nums, start, k) do
    if k <= 1 do
      true
    else
      Enum.reduce_while(0..(k - 2), true, fn offset, _acc ->
        a = Enum.at(nums, start + offset)
        b = Enum.at(nums, start + offset + 1)

        if a < b do
          {:cont, true}
        else
          {:halt, false}
        end
      end)
    end
  end
end
```
