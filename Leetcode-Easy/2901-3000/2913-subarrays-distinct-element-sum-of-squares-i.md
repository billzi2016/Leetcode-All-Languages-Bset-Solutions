# 2913. Subarrays Distinct Element Sum of Squares I

## Cpp

```cpp
class Solution {
public:
    int sumCounts(vector<int>& nums) {
        int n = nums.size();
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            bool seen[101] = {false};
            int distinct = 0;
            for (int j = i; j < n; ++j) {
                if (!seen[nums[j]]) {
                    seen[nums[j]] = true;
                    ++distinct;
                }
                ans += 1LL * distinct * distinct;
            }
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int sumCounts(List<Integer> nums) {
        int n = nums.size();
        long total = 0;
        for (int i = 0; i < n; i++) {
            boolean[] seen = new boolean[101];
            int distinct = 0;
            for (int j = i; j < n; j++) {
                int val = nums.get(j);
                if (!seen[val]) {
                    seen[val] = true;
                    distinct++;
                }
                total += (long) distinct * distinct;
            }
        }
        return (int) total;
    }
}
```

## Python

```python
class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        for i in range(n):
            seen = set()
            distinct = 0
            for j in range(i, n):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    distinct += 1
                total += distinct * distinct
        return total
```

## Python3

```python
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            seen = set()
            distinct = 0
            for j in range(i, n):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    distinct += 1
                total += distinct * distinct
        return total
```

## C

```c
int sumCounts(int* nums, int numsSize) {
    int total = 0;
    for (int i = 0; i < numsSize; ++i) {
        int seen[101] = {0};
        int distinct = 0;
        for (int j = i; j < numsSize; ++j) {
            int v = nums[j];
            if (!seen[v]) {
                seen[v] = 1;
                ++distinct;
            }
            total += distinct * distinct;
        }
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int SumCounts(IList<int> nums) {
        int n = nums.Count;
        long total = 0;
        for (int i = 0; i < n; i++) {
            bool[] seen = new bool[101];
            int distinct = 0;
            for (int j = i; j < n; j++) {
                int val = nums[j];
                if (!seen[val]) {
                    seen[val] = true;
                    distinct++;
                }
                total += (long)distinct * distinct;
            }
        }
        return (int)total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumCounts = function(nums) {
    const n = nums.length;
    let total = 0;
    for (let i = 0; i < n; ++i) {
        const seen = new Set();
        for (let j = i; j < n; ++j) {
            seen.add(nums[j]);
            const d = seen.size;
            total += d * d;
        }
    }
    return total;
};
```

## Typescript

```typescript
function sumCounts(nums: number[]): number {
    const n = nums.length;
    let total = 0;
    for (let i = 0; i < n; i++) {
        const seen = new Set<number>();
        for (let j = i; j < n; j++) {
            seen.add(nums[j]);
            const d = seen.size;
            total += d * d;
        }
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumCounts($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $seen = [];
            $distinct = 0;
            for ($j = $i; $j < $n; $j++) {
                $val = $nums[$j];
                if (!isset($seen[$val])) {
                    $seen[$val] = true;
                    $distinct++;
                }
                $ans += $distinct * $distinct;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func sumCounts(_ nums: [Int]) -> Int {
        let n = nums.count
        var total = 0
        for i in 0..<n {
            var seen = Set<Int>()
            for j in i..<n {
                seen.insert(nums[j])
                let d = seen.count
                total += d * d
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumCounts(nums: List<Int>): Int {
        val n = nums.size
        var total = 0L
        for (i in 0 until n) {
            val seen = BooleanArray(101)
            var distinct = 0
            for (j in i until n) {
                val v = nums[j]
                if (!seen[v]) {
                    seen[v] = true
                    distinct++
                }
                total += distinct * distinct
            }
        }
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int sumCounts(List<int> nums) {
    int n = nums.length;
    int total = 0;
    for (int i = 0; i < n; i++) {
      Set<int> seen = {};
      for (int j = i; j < n; j++) {
        seen.add(nums[j]);
        int d = seen.length;
        total += d * d;
      }
    }
    return total;
  }
}
```

## Golang

```go
func sumCounts(nums []int) int {
	n := len(nums)
	total := 0
	for i := 0; i < n; i++ {
		seen := make([]bool, 101)
		distinct := 0
		for j := i; j < n; j++ {
			v := nums[j]
			if !seen[v] {
				seen[v] = true
				distinct++
			}
			total += distinct * distinct
		}
	}
	return total
}
```

## Ruby

```ruby
require 'set'

def sum_counts(nums)
  n = nums.length
  total = 0
  (0...n).each do |i|
    seen = Set.new
    distinct = 0
    (i...n).each do |j|
      unless seen.include?(nums[j])
        seen.add(nums[j])
        distinct += 1
      end
      total += distinct * distinct
    end
  end
  total
end
```

## Scala

```scala
object Solution {
    def sumCounts(nums: List[Int]): Int = {
        val arr = nums.toArray
        var total: Long = 0L
        for (i <- arr.indices) {
            val seen = new java.util.HashSet[Int]()
            var distinct = 0
            var j = i
            while (j < arr.length) {
                if (!seen.contains(arr(j))) {
                    seen.add(arr(j))
                    distinct += 1
                }
                total += distinct.toLong * distinct
                j += 1
            }
        }
        total.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_counts(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut total: i64 = 0;
        for i in 0..n {
            let mut seen = [false; 101];
            let mut distinct = 0i32;
            for j in i..n {
                let v = nums[j] as usize;
                if !seen[v] {
                    seen[v] = true;
                    distinct += 1;
                }
                total += (distinct * distinct) as i64;
            }
        }
        total as i32
    }
}
```

## Racket

```racket
(define/contract (sum-counts nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums)))
    (let loop-i ((i 0) (total 0))
      (if (= i n)
          total
          (let ((seen (make-hash)))
            (let loop-j ((j i) (distinct 0) (cur-total total))
              (if (= j n)
                  (loop-i (+ i 1) cur-total)
                  (let* ((val (vector-ref arr j))
                         (already (hash-has-key? seen val))
                         (new-distinct (if already distinct (+ distinct 1))))
                    (unless already
                      (hash-set! seen val #t))
                    (loop-j (+ j 1) new-distinct (+ cur-total (* new-distinct new-distinct)))))))))))
```

## Erlang

```erlang
-spec sum_counts(Nums :: [integer()]) -> integer().
sum_counts(Nums) ->
    N = length(Nums),
    sum_counts_i(Nums, 1, N, 0).

%% iterate over start index
-spec sum_counts_i([integer()], integer(), integer(), integer()) -> integer().
sum_counts_i(_Nums, I, N, Acc) when I > N ->
    Acc;
sum_counts_i(Nums, I, N, Acc) ->
    {NewAcc, _} = process_j(Nums, I, N, #{}, 0, Acc),
    sum_counts_i(Nums, I + 1, N, NewAcc).

%% extend subarray from start J to end, maintaining distinct count
-spec process_j([integer()], integer(), integer(), map(), integer(), integer()) -> {integer(), any()}.
process_j(_Nums, J, End, _Map, _Cnt, Acc) when J > End ->
    {Acc, undefined};
process_j(Nums, J, End, Map, Cnt, Acc) ->
    Val = lists:nth(J, Nums),
    case maps:is_key(Val, Map) of
        true ->
            NewCnt = Cnt,
            NewMap = Map;
        false ->
            NewCnt = Cnt + 1,
            NewMap = maps:put(Val, true, Map)
    end,
    NewAcc = Acc + NewCnt * NewCnt,
    process_j(Nums, J + 1, End, NewMap, NewCnt, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_counts(nums :: [integer]) :: integer
  def sum_counts(nums) do
    n = length(nums)
    compute(nums, 0, 0, n)
  end

  defp compute(_nums, i, acc, n) when i >= n, do: acc

  defp compute(nums, i, acc, n) do
    {new_acc, _} =
      Enum.reduce(Enum.slice(nums, i, n - i), {acc, MapSet.new()}, fn x, {a, set} ->
        new_set = MapSet.put(set, x)
        cnt = MapSet.size(new_set)
        {a + cnt * cnt, new_set}
      end)

    compute(nums, i + 1, new_acc, n)
  end
end
```
