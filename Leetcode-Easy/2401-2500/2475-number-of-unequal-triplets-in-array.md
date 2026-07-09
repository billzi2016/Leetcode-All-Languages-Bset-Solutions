# 2475. Number of Unequal Triplets in Array

## Cpp

```cpp
class Solution {
public:
    int unequalTriplets(vector<int>& nums) {
        int n = nums.size();
        int cnt = 0;
        for (int i = 0; i < n - 2; ++i) {
            for (int j = i + 1; j < n - 1; ++j) {
                if (nums[i] == nums[j]) continue;
                for (int k = j + 1; k < n; ++k) {
                    if (nums[i] != nums[k] && nums[j] != nums[k]) {
                        ++cnt;
                    }
                }
            }
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int unequalTriplets(int[] nums) {
        int n = nums.length;
        int cnt = 0;
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                if (nums[i] == nums[j]) continue;
                for (int k = j + 1; k < n; k++) {
                    if (nums[i] != nums[k] && nums[j] != nums[k]) {
                        cnt++;
                    }
                }
            }
        }
        return cnt;
    }
}
```

## Python

```python
class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[i] != nums[k] and nums[j] != nums[k]:
                        count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n - 2):
            a = nums[i]
            for j in range(i + 1, n - 1):
                b = nums[j]
                if a == b:
                    continue
                for k in range(j + 1, n):
                    c = nums[k]
                    if a != c and b != c:
                        count += 1
        return count
```

## C

```c
int unequalTriplets(int* nums, int numsSize) {
    int count = 0;
    for (int i = 0; i < numsSize - 2; ++i) {
        for (int j = i + 1; j < numsSize - 1; ++j) {
            if (nums[i] == nums[j]) continue;
            for (int k = j + 1; k < numsSize; ++k) {
                if (nums[i] != nums[k] && nums[j] != nums[k]) {
                    ++count;
                }
            }
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int UnequalTriplets(int[] nums) {
        int n = nums.Length;
        int count = 0;
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                if (nums[i] == nums[j]) continue;
                for (int k = j + 1; k < n; k++) {
                    if (nums[i] != nums[k] && nums[j] != nums[k]) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var unequalTriplets = function(nums) {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n - 2; ++i) {
        for (let j = i + 1; j < n - 1; ++j) {
            if (nums[i] === nums[j]) continue;
            for (let k = j + 1; k < n; ++k) {
                if (nums[i] !== nums[k] && nums[j] !== nums[k]) {
                    ++ans;
                }
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function unequalTriplets(nums: number[]): number {
    const n = nums.length;
    let count = 0;
    for (let i = 0; i < n - 2; i++) {
        for (let j = i + 1; j < n - 1; j++) {
            if (nums[i] === nums[j]) continue;
            for (let k = j + 1; k < n; k++) {
                if (nums[i] !== nums[k] && nums[j] !== nums[k]) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function unequalTriplets($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n - 2; $i++) {
            for ($j = $i + 1; $j < $n - 1; $j++) {
                if ($nums[$i] == $nums[$j]) continue;
                for ($k = $j + 1; $k < $n; $k++) {
                    if ($nums[$i] != $nums[$k] && $nums[$j] != $nums[$k]) {
                        $ans++;
                    }
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func unequalTriplets(_ nums: [Int]) -> Int {
        let n = nums.count
        var count = 0
        if n < 3 { return 0 }
        for i in 0..<(n - 2) {
            for j in (i + 1)..<(n - 1) {
                for k in (j + 1)..<n {
                    if nums[i] != nums[j] && nums[j] != nums[k] && nums[i] != nums[k] {
                        count += 1
                    }
                }
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun unequalTriplets(nums: IntArray): Int {
        val freq = HashMap<Int, Int>()
        for (v in nums) {
            freq[v] = (freq[v] ?: 0) + 1
        }
        val counts = freq.values.toIntArray()
        var ans = 0L
        val m = counts.size
        for (i in 0 until m) {
            for (j in i + 1 until m) {
                for (k in j + 1 until m) {
                    ans += counts[i].toLong() * counts[j] * counts[k]
                }
            }
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int unequalTriplets(List<int> nums) {
    int n = nums.length;
    int count = 0;
    for (int i = 0; i < n - 2; i++) {
      for (int j = i + 1; j < n - 1; j++) {
        if (nums[i] == nums[j]) continue;
        for (int k = j + 1; k < n; k++) {
          if (nums[i] != nums[k] && nums[j] != nums[k]) {
            count++;
          }
        }
      }
    }
    return count;
  }
}
```

## Golang

```go
func unequalTriplets(nums []int) int {
	n := len(nums)
	count := 0
	for i := 0; i < n-2; i++ {
		for j := i + 1; j < n-1; j++ {
			if nums[i] == nums[j] {
				continue
			}
			for k := j + 1; k < n; k++ {
				if nums[i] != nums[k] && nums[j] != nums[k] {
					count++
				}
			}
		}
	}
	return count
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def unequal_triplets(nums)
  n = nums.length
  count = 0
  (0...n-2).each do |i|
    ((i+1)...n-1).each do |j|
      ((j+1)...n).each do |k|
        if nums[i] != nums[j] && nums[i] != nums[k] && nums[j] != nums[k]
          count += 1
        end
      end
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def unequalTriplets(nums: Array[Int]): Int = {
        var count = 0
        val n = nums.length
        for (i <- 0 until n - 2) {
            for (j <- i + 1 until n - 1) {
                if (nums(i) != nums(j)) {
                    for (k <- j + 1 until n) {
                        if (nums(k) != nums(i) && nums(k) != nums(j)) {
                            count += 1
                        }
                    }
                }
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn unequal_triplets(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut count = 0i32;
        for i in 0..n {
            for j in (i + 1)..n {
                if nums[i] == nums[j] {
                    continue;
                }
                for k in (j + 1)..n {
                    if nums[i] != nums[k] && nums[j] != nums[k] {
                        count += 1;
                    }
                }
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (unequal-triplets nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)])
    (for*/fold ([cnt 0])
               ([i (in-range 0 (- n 2))]
                [j (in-range (+ i 1) (- n 1))]
                [k (in-range (+ j 1) n)])
      (if (and (not (= (list-ref nums i) (list-ref nums j)))
               (not (= (list-ref nums i) (list-ref nums k)))
               (not (= (list-ref nums j) (list-ref nums k))))
          (+ cnt 1)
          cnt))))
```

## Erlang

```erlang
-module(solution).
-export([unequal_triplets/1]).

-spec unequal_triplets([integer()]) -> integer().
unequal_triplets(Nums) ->
    N = length(Nums),
    count_i(Nums, N, 0, 0).

count_i(_Nums, N, I, Acc) when I > N - 3 ->
    Acc;
count_i(Nums, N, I, Acc) ->
    JStart = I + 1,
    Acc1 = count_j(Nums, N, I, JStart, Acc),
    count_i(Nums, N, I + 1, Acc1).

count_j(_Nums, N, _I, J, Acc) when J > N - 2 ->
    Acc;
count_j(Nums, N, I, J, Acc) ->
    KStart = J + 1,
    Acc1 = count_k(Nums, N, I, J, KStart, Acc),
    count_j(Nums, N, I, J + 1, Acc1).

count_k(_Nums, N, _I, _J, K, Acc) when K > N - 1 ->
    Acc;
count_k(Nums, N, I, J, K, Acc) ->
    Vi = lists:nth(I + 1, Nums),
    Vj = lists:nth(J + 1, Nums),
    Vk = lists:nth(K + 1, Nums),
    NewAcc = if
        Vi =/= Vj, Vi =/= Vk, Vj =/= Vk -> Acc + 1;
        true -> Acc
    end,
    count_k(Nums, N, I, J, K + 1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec unequal_triplets(nums :: [integer]) :: integer
  def unequal_triplets(nums) do
    n = length(nums)
    tup = List.to_tuple(nums)

    Enum.reduce(0..(n - 3), 0, fn i, acc_i ->
      Enum.reduce((i + 1)..(n - 2), acc_i, fn j, acc_j ->
        Enum.reduce((j + 1)..(n - 1), acc_j, fn k, acc_k ->
          if elem(tup, i) != elem(tup, j) and
             elem(tup, i) != elem(tup, k) and
             elem(tup, j) != elem(tup, k) do
            acc_k + 1
          else
            acc_k
          end
        end)
      end)
    end)
  end
end
```
