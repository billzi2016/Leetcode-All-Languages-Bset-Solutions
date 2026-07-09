# 2598. Smallest Missing Non-negative Integer After Operations

## Cpp

```cpp
class Solution {
public:
    int findSmallestInteger(vector<int>& nums, int value) {
        vector<int> freq(value, 0);
        for (int num : nums) {
            int r = ((num % value) + value) % value;
            ++freq[r];
        }
        for (int i = 0; ; ++i) {
            int r = i % value;
            if (freq[r] == 0) return i;
            --freq[r];
        }
    }
};
```

## Java

```java
class Solution {
    public int findSmallestInteger(int[] nums, int value) {
        int[] cnt = new int[value];
        for (int num : nums) {
            int r = ((num % value) + value) % value;
            cnt[r]++;
        }
        int mex = 0;
        while (true) {
            int r = mex % value;
            if (cnt[r] == 0) break;
            cnt[r]--;
            mex++;
        }
        return mex;
    }
}
```

## Python

```python
class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        cnt = [0] * value
        for x in nums:
            cnt[x % value] += 1

        i = 0
        while True:
            r = i % value
            if cnt[r]:
                cnt[r] -= 1
                i += 1
            else:
                return i
```

## Python3

```python
from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = [0] * value
        for x in nums:
            freq[x % value] += 1
        mex = 0
        while True:
            r = mex % value
            if freq[r] == 0:
                return mex
            freq[r] -= 1
            mex += 1
```

## C

```c
#include <stdlib.h>

int findSmallestInteger(int* nums, int numsSize, int value) {
    int *cnt = (int *)calloc(value, sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        int r = nums[i] % value;
        if (r < 0) r += value;
        cnt[r]++;
    }

    int low = 0, high = numsSize; // maximum possible MEX is numsSize
    while (low < high) {
        int mid = (low + high + 1) / 2; // try larger MEX
        int ok = 1;
        for (int r = 0; r < value && r < mid; ++r) {
            int needed = ((mid - 1 - r) / value) + 1;
            if (cnt[r] < needed) { ok = 0; break; }
        }
        if (ok) low = mid;
        else high = mid - 1;
    }

    free(cnt);
    return low;
}
```

## Csharp

```csharp
public class Solution {
    public int FindSmallestInteger(int[] nums, int value) {
        int[] cnt = new int[value];
        foreach (int num in nums) {
            int r = ((num % value) + value) % value;
            cnt[r]++;
        }
        int[] used = new int[value];
        int mex = 0;
        while (true) {
            int r = mex % value;
            if (used[r] < cnt[r]) {
                used[r]++;
                mex++;
            } else {
                break;
            }
        }
        return mex;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} value
 * @return {number}
 */
var findSmallestInteger = function(nums, value) {
    const freq = new Array(value).fill(0);
    for (let num of nums) {
        let r = ((num % value) + value) % value;
        freq[r]++;
    }
    let mex = 0;
    while (true) {
        const r = mex % value;
        if (freq[r] > 0) {
            freq[r]--;
            mex++;
        } else {
            break;
        }
    }
    return mex;
};
```

## Typescript

```typescript
function findSmallestInteger(nums: number[], value: number): number {
    const freq = new Array(value).fill(0);
    for (const num of nums) {
        const r = ((num % value) + value) % value;
        freq[r]++;
    }
    let i = 0;
    while (i < nums.length) {
        const r = i % value;
        if (freq[r] > 0) {
            freq[r]--;
            i++;
        } else {
            return i;
        }
    }
    return nums.length;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $value
     * @return Integer
     */
    function findSmallestInteger($nums, $value) {
        $freq = array_fill(0, $value, 0);
        foreach ($nums as $num) {
            $rem = ($num % $value + $value) % $value;
            $freq[$rem]++;
        }
        for ($i = 0; ; $i++) {
            $r = $i % $value;
            if ($freq[$r] > 0) {
                $freq[$r]--;
            } else {
                return $i;
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func findSmallestInteger(_ nums: [Int], _ value: Int) -> Int {
        var cnt = Array(repeating: 0, count: value)
        for num in nums {
            let mod = ((num % value) + value) % value
            cnt[mod] += 1
        }
        var mex = 0
        while true {
            let r = mex % value
            if cnt[r] == 0 { break }
            cnt[r] -= 1
            mex += 1
        }
        return mex
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findSmallestInteger(nums: IntArray, value: Int): Int {
        val cnt = IntArray(value)
        for (num in nums) {
            var r = num % value
            if (r < 0) r += value
            cnt[r]++
        }
        var i = 0
        while (true) {
            val r = i % value
            if (cnt[r] == 0) return i
            cnt[r]--
            i++
        }
    }
}
```

## Dart

```dart
class Solution {
  int findSmallestInteger(List<int> nums, int value) {
    List<int> cnt = List.filled(value, 0);
    for (int num in nums) {
      int r = ((num % value) + value) % value;
      cnt[r]++;
    }
    int i = 0;
    while (true) {
      int r = i % value;
      if (cnt[r] > 0) {
        cnt[r]--;
        i++;
      } else {
        return i;
      }
    }
  }
}
```

## Golang

```go
func findSmallestInteger(nums []int, value int) int {
	cnt := make([]int, value)
	for _, num := range nums {
		r := num % value
		if r < 0 {
			r += value
		}
		cnt[r]++
	}
	mex := 0
	for {
		r := mex % value
		if cnt[r] == 0 {
			break
		}
		cnt[r]--
		mex++
	}
	return mex
}
```

## Ruby

```ruby
def find_smallest_integer(nums, value)
  freq = Array.new(value, 0)
  nums.each do |num|
    r = num % value
    r += value if r < 0
    freq[r] += 1
  end

  mex = 0
  loop do
    r = mex % value
    break if freq[r].zero?
    freq[r] -= 1
    mex += 1
  end
  mex
end
```

## Scala

```scala
object Solution {
    def findSmallestInteger(nums: Array[Int], value: Int): Int = {
        val freq = new Array[Int](value)
        for (num <- nums) {
            var r = num % value
            if (r < 0) r += value
            freq(r) += 1
        }
        var i = 0
        while (true) {
            val r = i % value
            if (freq(r) > 0) {
                freq(r) -= 1
                i += 1
            } else {
                return i
            }
        }
        0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_smallest_integer(nums: Vec<i32>, value: i32) -> i32 {
        let v = value as usize;
        let mut cnt = vec![0i64; v];
        for num in nums.iter() {
            let mut r = *num % value;
            if r < 0 { r += value; }
            cnt[r as usize] += 1;
        }
        let mut mex: i32 = 0;
        loop {
            let idx = (mex % value) as usize;
            if cnt[idx] > 0 {
                cnt[idx] -= 1;
                mex += 1;
            } else {
                break;
            }
        }
        mex
    }
}
```

## Racket

```racket
(define/contract (find-smallest-integer nums value)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((cnt (make-vector value 0)))
    (for ([num nums])
      (let ((r (modulo num value)))
        (vector-set! cnt r (+ 1 (vector-ref cnt r)))))
    (let loop ((i 0))
      (let ((r (modulo i value)))
        (if (> (vector-ref cnt r) 0)
            (begin
              (vector-set! cnt r (- (vector-ref cnt r) 1))
              (loop (+ i 1)))
            i)))))
```

## Erlang

```erlang
-module(solution).
-export([find_smallest_integer/2]).

-spec find_smallest_integer(Nums :: [integer()], Value :: integer()) -> integer().
find_smallest_integer(Nums, Value) ->
    Counts = build_counts(Nums, Value, #{}),
    mex_loop(0, Value, Counts).

build_counts([], _Value, Acc) ->
    Acc;
build_counts([H|T], Value, Acc) ->
    R = ((H rem Value) + Value) rem Value,
    NewAcc = maps:update_with(R, fun(C) -> C + 1 end, 1, Acc),
    build_counts(T, Value, NewAcc).

mex_loop(Mex, Value, Counts) ->
    R = Mex rem Value,
    case maps:get(R, Counts, 0) of
        0 ->
            Mex;
        C when C > 0 ->
            UpdatedCounts = maps:put(R, C - 1, Counts),
            mex_loop(Mex + 1, Value, UpdatedCounts)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_smallest_integer(nums :: [integer], value :: integer) :: integer
  def find_smallest_integer(nums, value) do
    freq =
      Enum.reduce(nums, %{}, fn num, acc ->
        r = Integer.mod(num, value)
        Map.update(acc, r, 1, &(&1 + 1))
      end)

    mex(freq, value, 0)
  end

  defp mex(freq, value, t) do
    r = rem(t, value)

    case Map.get(freq, r, 0) do
      0 ->
        t

      cnt ->
        new_freq =
          if cnt == 1,
            do: Map.delete(freq, r),
            else: Map.put(freq, r, cnt - 1)

        mex(new_freq, value, t + 1)
    end
  end
end
```
