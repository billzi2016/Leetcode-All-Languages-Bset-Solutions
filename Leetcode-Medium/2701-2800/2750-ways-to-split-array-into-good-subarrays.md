# 2750. Ways to Split Array Into Good Subarrays

## Cpp

```cpp
class Solution {
public:
    int numberOfGoodSubarraySplits(vector<int>& nums) {
        const long long MOD = 1000000007LL;
        long long ans = 1;
        int prev = -1; // index of previous 1
        int ones = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] == 1) {
                ++ones;
                if (prev != -1) {
                    long long zerosBetween = i - prev - 1;
                    ans = (ans * (zerosBetween + 1)) % MOD;
                }
                prev = i;
            }
        }
        if (ones == 0) return 0;
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int numberOfGoodSubarraySplits(int[] nums) {
        long result = 1L;
        int prevOneIdx = -1;
        boolean hasOne = false;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                if (!hasOne) {
                    hasOne = true;
                } else {
                    long dist = i - prevOneIdx;
                    result = (result * dist) % MOD;
                }
                prevOneIdx = i;
            }
        }
        return hasOne ? (int) result : 0;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfGoodSubarraySplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        ones = [i for i, v in enumerate(nums) if v == 1]
        k = len(ones)
        if k == 0:
            return 0
        if k == 1:
            return 1
        ans = 1
        for i in range(1, k):
            ans = (ans * (ones[i] - ones[i-1])) % MOD
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        ones = [i for i, v in enumerate(nums) if v == 1]
        k = len(ones)
        if k == 0:
            return 0
        ans = 1
        for i in range(k - 1):
            gap = ones[i + 1] - ones[i] - 1
            ans = (ans * (gap + 1)) % MOD
        return ans
```

## C

```c
int numberOfGoodSubarraySplits(int* nums, int numsSize) {
    const int MOD = 1000000007;
    long long ans = 1;
    int prev = -1;
    int ones = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 1) {
            ++ones;
            if (prev != -1) {
                long long dist = i - prev;
                ans = (ans * dist) % MOD;
            }
            prev = i;
        }
    }
    if (ones == 0) return 0;
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    private const int MOD = 1000000007;
    public int NumberOfGoodSubarraySplits(int[] nums) {
        var ones = new System.Collections.Generic.List<int>();
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 1) ones.Add(i);
        }
        int k = ones.Count;
        if (k == 0) return 0;
        long result = 1;
        for (int i = 1; i < k; i++) {
            int gap = ones[i] - ones[i - 1] - 1;
            result = (result * (gap + 1)) % MOD;
        }
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfGoodSubarraySplits = function(nums) {
    const MOD = 1000000007;
    const positions = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) positions.push(i);
    }
    const k = positions.length;
    if (k === 0) return 0;
    let ans = 1;
    for (let i = 0; i < k - 1; i++) {
        const gap = positions[i + 1] - positions[i] - 1;
        ans = (ans * (gap + 1)) % MOD;
    }
    return ans;
};
```

## Typescript

```typescript
function numberOfGoodSubarraySplits(nums: number[]): number {
    const MOD = 1000000007n;
    const ones: number[] = [];
    for (let i = 0; i < nums.length; ++i) {
        if (nums[i] === 1) ones.push(i);
    }
    if (ones.length === 0) return 0;
    let ans = 1n;
    for (let i = 1; i < ones.length; ++i) {
        const gap = BigInt(ones[i] - ones[i - 1]);
        ans = (ans * gap) % MOD;
    }
    return Number(ans);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numberOfGoodSubarraySplits($nums) {
        $mod = 1000000007;
        $prev = -1;
        $ans = 1;
        $ones = 0;

        foreach ($nums as $i => $val) {
            if ($val == 1) {
                $ones++;
                if ($prev != -1) {
                    $gap = $i - $prev;
                    $ans = ($ans * $gap) % $mod;
                }
                $prev = $i;
            }
        }

        if ($ones == 0) {
            return 0;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfGoodSubarraySplits(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        var onesIndices = [Int]()
        for (i, v) in nums.enumerated() where v == 1 {
            onesIndices.append(i)
        }
        let countOnes = onesIndices.count
        if countOnes == 0 { return 0 }
        var ans: Int64 = 1
        for i in 0..<(countOnes - 1) {
            let zerosBetween = onesIndices[i + 1] - onesIndices[i] - 1
            ans = (ans * Int64(zerosBetween + 1)) % Int64(MOD)
        }
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfGoodSubarraySplits(nums: IntArray): Int {
        val MOD = 1000000007L
        var onesCount = 0
        for (v in nums) if (v == 1) onesCount++
        if (onesCount == 0) return 0
        var result = 1L
        var prevOneIdx = -1
        for (i in nums.indices) {
            if (nums[i] == 1) {
                if (prevOneIdx != -1) {
                    val zerosBetween = i - prevOneIdx - 1
                    result = (result * (zerosBetween + 1)) % MOD
                }
                prevOneIdx = i
            }
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numberOfGoodSubarraySplits(List<int> nums) {
    const int MOD = 1000000007;
    List<int> onesPos = [];
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == 1) onesPos.add(i);
    }
    if (onesPos.isEmpty) return 0;
    int ans = 1;
    for (int i = 0; i < onesPos.length - 1; i++) {
      int zeros = onesPos[i + 1] - onesPos[i] - 1;
      ans = (ans * (zeros + 1)) % MOD;
    }
    return ans;
  }
}
```

## Golang

```go
package main

import "fmt"

const MOD = 1000000007

func numberOfGoodSubarraySplits(nums []int) int {
	prev := -1
	ans := int64(1)
	for i, v := range nums {
		if v == 1 {
			if prev != -1 {
				dist := int64(i - prev)
				ans = (ans * dist) % MOD
			}
			prev = i
		}
	}
	if prev == -1 { // no ones
		return 0
	}
	return int(ans)
}

// The following is only for local testing and will be ignored by LeetCode.
func main() {
	fmt.Println(numberOfGoodSubarraySplits([]int{0, 1, 0, 0, 1})) // 3
	fmt.Println(numberOfGoodSubarraySplits([]int{0, 1, 0}))       // 1
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def number_of_good_subarray_splits(nums)
  ones = []
  nums.each_with_index { |v, i| ones << i if v == 1 }
  k = ones.length
  return 0 if k == 0
  ans = 1
  (0...k - 1).each do |i|
    gap = ones[i + 1] - ones[i] - 1
    ans = (ans * (gap + 1)) % MOD
  end
  ans
end
```

## Scala

```scala
object Solution {
    def numberOfGoodSubarraySplits(nums: Array[Int]): Int = {
        val MOD = 1000000007L
        var prev = -1
        var result = 1L
        var ones = 0
        for (i <- nums.indices) {
            if (nums(i) == 1) {
                ones += 1
                if (prev != -1) {
                    val diff = i - prev
                    result = (result * diff) % MOD
                }
                prev = i
            }
        }
        if (ones == 0) 0 else result.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_good_subarray_splits(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut ones: Vec<usize> = Vec::new();
        for (i, &v) in nums.iter().enumerate() {
            if v == 1 {
                ones.push(i);
            }
        }
        if ones.is_empty() {
            return 0;
        }
        let mut ans: i64 = 1;
        for w in ones.windows(2) {
            let diff = (w[1] - w[0]) as i64;
            ans = ans * diff % MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (number-of-good-subarray-splits nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (idx 0) (prev -1) (ans 1) (found? #f))
    (if (null? lst)
        (if found? ans 0)
        (let ((val (car lst)))
          (if (= val 1)
              (if (not found?)
                  (loop (cdr lst) (+ idx 1) idx ans #t)
                  (let* ((gap (- idx prev 1))
                         (new-ans (modulo (* ans (add1 gap)) MOD)))
                    (loop (cdr lst) (+ idx 1) idx new-ans #t)))
              (loop (cdr lst) (+ idx 1) prev ans found?))))))
```

## Erlang

```erlang
-module(solution).
-export([number_of_good_subarray_splits/1]).

-spec number_of_good_subarray_splits(Nums :: [integer()]) -> integer().
number_of_good_subarray_splits(Nums) ->
    Mod = 1000000007,
    compute(Nums, 0, -1, 1, Mod).

compute([], _Idx, PrevOne, Res, _Mod) ->
    case PrevOne of
        -1 -> 0;
        _  -> Res
    end;
compute([H|T], Idx, PrevOne, Res, Mod) ->
    case H of
        1 ->
            case PrevOne of
                -1 ->
                    compute(T, Idx + 1, Idx, Res, Mod);
                _ ->
                    Gap = Idx - PrevOne - 1,
                    NewRes = (Res * (Gap + 1)) rem Mod,
                    compute(T, Idx + 1, Idx, NewRes, Mod)
            end;
        _ -> % zero
            compute(T, Idx + 1, PrevOne, Res, Mod)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_good_subarray_splits(nums :: [integer]) :: integer
  def number_of_good_subarray_splits(nums) do
    mod = 1_000_000_007

    positions =
      nums
      |> Enum.with_index()
      |> Enum.filter(fn {v, _i} -> v == 1 end)
      |> Enum.map(fn {_v, i} -> i end)

    case positions do
      [] -> 0
      [_] -> 1
      _ ->
        {ans, _} =
          Enum.reduce(positions, {1, nil}, fn pos, {res, prev} ->
            if prev == nil do
              {res, pos}
            else
              diff = pos - prev
              {rem(res * diff, mod), pos}
            end
          end)

        ans
    end
  end
end
```
