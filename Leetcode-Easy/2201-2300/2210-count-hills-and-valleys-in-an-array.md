# 2210. Count Hills and Valleys in an Array

## Cpp

```cpp
class Solution {
public:
    int countHillValley(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        for (int i = 1; i < n - 1; ++i) {
            if (nums[i] == nums[i - 1]) continue; // skip duplicates, only first of a plateau
            int left = nums[i - 1];
            int j = i + 1;
            while (j < n && nums[j] == nums[i]) ++j;
            if (j == n) break; // no right non‑equal neighbor
            int right = nums[j];
            if ((nums[i] > left && nums[i] > right) ||
                (nums[i] < left && nums[i] < right)) {
                ++ans;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countHillValley(int[] nums) {
        // Compress consecutive equal elements
        int n = nums.length;
        int[] compressed = new int[n];
        int m = 0;
        for (int num : nums) {
            if (m == 0 || compressed[m - 1] != num) {
                compressed[m++] = num;
            }
        }
        int count = 0;
        for (int i = 1; i < m - 1; i++) {
            if ((compressed[i] > compressed[i - 1] && compressed[i] > compressed[i + 1]) ||
                (compressed[i] < compressed[i - 1] && compressed[i] < compressed[i + 1])) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Remove consecutive duplicates
        filtered = []
        for x in nums:
            if not filtered or filtered[-1] != x:
                filtered.append(x)
        n = len(filtered)
        if n < 3:
            return 0
        count = 0
        for i in range(1, n - 1):
            if (filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]) or \
               (filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]):
                count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Remove consecutive duplicates to treat equal adjacent indices as one.
        compressed = []
        for x in nums:
            if not compressed or compressed[-1] != x:
                compressed.append(x)
        res = 0
        for i in range(1, len(compressed) - 1):
            if (compressed[i] > compressed[i - 1] and compressed[i] > compressed[i + 1]) or \
               (compressed[i] < compressed[i - 1] and compressed[i] < compressed[i + 1]):
                res += 1
        return res
```

## C

```c
int countHillValley(int* nums, int numsSize) {
    int res = 0;
    for (int i = 1; i < numsSize - 1; ++i) {
        if (nums[i] == nums[i - 1]) continue; // skip duplicates within a plateau
        int left = i - 1;
        while (left >= 0 && nums[left] == nums[i]) --left;
        int right = i + 1;
        while (right < numsSize && nums[right] == nums[i]) ++right;
        if (left < 0 || right >= numsSize) continue; // missing non‑equal neighbor
        if ((nums[i] > nums[left] && nums[i] > nums[right]) ||
            (nums[i] < nums[left] && nums[i] < nums[right])) {
            ++res;
        }
    }
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountHillValley(int[] nums)
    {
        if (nums == null || nums.Length < 3) return 0;

        var compressed = new System.Collections.Generic.List<int>();
        foreach (var num in nums)
        {
            if (compressed.Count == 0 || compressed[compressed.Count - 1] != num)
                compressed.Add(num);
        }

        int count = 0;
        for (int i = 1; i < compressed.Count - 1; i++)
        {
            if ((compressed[i] > compressed[i - 1] && compressed[i] > compressed[i + 1]) ||
                (compressed[i] < compressed[i - 1] && compressed[i] < compressed[i + 1]))
            {
                count++;
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
var countHillValley = function(nums) {
    const comp = [];
    for (const v of nums) {
        if (comp.length === 0 || comp[comp.length - 1] !== v) {
            comp.push(v);
        }
    }
    let ans = 0;
    for (let i = 1; i < comp.length - 1; ++i) {
        if ((comp[i] > comp[i - 1] && comp[i] > comp[i + 1]) ||
            (comp[i] < comp[i - 1] && comp[i] < comp[i + 1])) {
            ans++;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function countHillValley(nums: number[]): number {
    const comp: number[] = [];
    for (let i = 0; i < nums.length; i++) {
        if (i === 0 || nums[i] !== nums[i - 1]) comp.push(nums[i]);
    }
    let ans = 0;
    for (let i = 1; i + 1 < comp.length; i++) {
        const left = comp[i - 1];
        const mid = comp[i];
        const right = comp[i + 1];
        if ((mid > left && mid > right) || (mid < left && mid < right)) ans++;
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
    function countHillValley($nums) {
        $n = count($nums);
        $cnt = 0;
        for ($i = 1; $i < $n - 1; $i++) {
            if ($nums[$i] == $nums[$i - 1]) {
                continue;
            }
            // find left non-equal neighbor
            $j = $i - 1;
            while ($j >= 0 && $nums[$j] == $nums[$i]) {
                $j--;
            }
            if ($j < 0) {
                continue;
            }
            $left = $nums[$j];
            // find right non-equal neighbor
            $k = $i + 1;
            while ($k < $n && $nums[$k] == $nums[$i]) {
                $k++;
            }
            if ($k >= $n) {
                continue;
            }
            $right = $nums[$k];
            if (($nums[$i] > $left && $nums[$i] > $right) ||
                ($nums[$i] < $left && $nums[$i] < $right)) {
                $cnt++;
            }
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func countHillValley(_ nums: [Int]) -> Int {
        let n = nums.count
        var result = 0
        for i in 0..<n {
            if i > 0 && nums[i] == nums[i - 1] { continue }
            var left = i - 1
            while left >= 0 && nums[left] == nums[i] {
                left -= 1
            }
            var right = i + 1
            while right < n && nums[right] == nums[i] {
                right += 1
            }
            if left >= 0 && right < n {
                let lVal = nums[left]
                let rVal = nums[right]
                if (nums[i] > lVal && nums[i] > rVal) ||
                   (nums[i] < lVal && nums[i] < rVal) {
                    result += 1
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countHillValley(nums: IntArray): Int {
        val compressed = mutableListOf<Int>()
        for (num in nums) {
            if (compressed.isEmpty() || compressed.last() != num) {
                compressed.add(num)
            }
        }
        var count = 0
        for (i in 1 until compressed.size - 1) {
            val left = compressed[i - 1]
            val mid = compressed[i]
            val right = compressed[i + 1]
            if ((mid > left && mid > right) || (mid < left && mid < right)) {
                count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countHillValley(List<int> nums) {
    // Remove consecutive duplicates
    List<int> compressed = [];
    for (int num in nums) {
      if (compressed.isEmpty || compressed.last != num) {
        compressed.add(num);
      }
    }

    int count = 0;
    for (int i = 1; i + 1 < compressed.length; ++i) {
      if ((compressed[i] > compressed[i - 1] && compressed[i] > compressed[i + 1]) ||
          (compressed[i] < compressed[i - 1] && compressed[i] < compressed[i + 1])) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func countHillValley(nums []int) int {
    // Remove consecutive duplicates
    compressed := make([]int, 0, len(nums))
    for _, v := range nums {
        if len(compressed) == 0 || v != compressed[len(compressed)-1] {
            compressed = append(compressed, v)
        }
    }

    count := 0
    // Count peaks and valleys in the compressed array
    for i := 1; i+1 < len(compressed); i++ {
        if (compressed[i] > compressed[i-1] && compressed[i] > compressed[i+1]) ||
            (compressed[i] < compressed[i-1] && compressed[i] < compressed[i+1]) {
            count++
        }
    }
    return count
}
```

## Ruby

```ruby
def count_hill_valley(nums)
  # Remove consecutive duplicates
  compressed = []
  nums.each do |num|
    compressed << num if compressed.empty? || compressed[-1] != num
  end

  count = 0
  (1...compressed.length - 1).each do |i|
    if (compressed[i] > compressed[i - 1] && compressed[i] > compressed[i + 1]) ||
       (compressed[i] < compressed[i - 1] && compressed[i] < compressed[i + 1])
      count += 1
    end
  end

  count
end
```

## Scala

```scala
object Solution {
    def countHillValley(nums: Array[Int]): Int = {
        val compressed = scala.collection.mutable.ArrayBuffer[Int]()
        for (x <- nums) {
            if (compressed.isEmpty || compressed.last != x) compressed += x
        }
        var cnt = 0
        for (i <- 1 until compressed.length - 1) {
            if ((compressed(i) > compressed(i - 1) && compressed(i) > compressed(i + 1)) ||
                (compressed(i) < compressed(i - 1) && compressed(i) < compressed(i + 1))) {
                cnt += 1
            }
        }
        cnt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_hill_valley(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 3 {
            return 0;
        }
        let mut cnt = 0usize;
        let mut i = 1usize;
        while i + 1 < n {
            // skip indices that are equal to the previous one (same hill/valley)
            if nums[i] == nums[i - 1] {
                i += 1;
                continue;
            }

            // find closest left neighbor different from nums[i]
            let mut l = i as isize - 1;
            while l >= 0 && nums[l as usize] == nums[i] {
                l -= 1;
            }
            if l < 0 {
                i += 1;
                continue;
            }

            // find closest right neighbor different from nums[i]
            let mut r = i + 1;
            while r < n && nums[r] == nums[i] {
                r += 1;
            }
            if r >= n {
                i += 1;
                continue;
            }

            let left_val = nums[l as usize];
            let right_val = nums[r];
            let cur = nums[i];

            if (left_val < cur && right_val < cur) || (left_val > cur && right_val > cur) {
                cnt += 1;
            }
            i += 1;
        }
        cnt as i32
    }
}
```

## Racket

```racket
(define/contract (count-hill-valley nums)
  (-> (listof exact-integer?) exact-integer?)
  (letrec ((compress
            (lambda (lst)
              (reverse
               (foldl (lambda (x acc)
                        (if (null? acc)
                            (list x)
                            (if (= x (car acc))
                                acc
                                (cons x acc))))
                      '()
                      lst)))))
    (let ((comp (compress nums)))
      (let loop ((i 1) (cnt 0) (len (length comp)))
        (if (or (< len 3) (>= i (- len 1)))
            cnt
            (let* ((prev (list-ref comp (- i 1)))
                   (curr (list-ref comp i))
                   (next (list-ref comp (+ i 1))))
              (loop (+ i 1)
                    (if (or (and (> curr prev) (> curr next))
                            (and (< curr prev) (< curr next)))
                        (+ cnt 1)
                        cnt)
                    len)))))))
```

## Erlang

```erlang
-spec count_hill_valley(Nums :: [integer()]) -> integer().
count_hill_valley(Nums) ->
    Len = length(Nums),
    count_hv(Nums, Len, 0, 0).

count_hv(_Nums, Len, Index, Acc) when Index >= Len ->
    Acc;
count_hv(Nums, Len, Index, Acc) ->
    Val = lists:nth(Index + 1, Nums),
    case (Index > 0 andalso lists:nth(Index, Nums) == Val) of
        true ->
            count_hv(Nums, Len, Index + 1, Acc);
        false ->
            Left = find_left(Nums, Index - 1, Val),
            Right = find_right(Nums, Index + 1, Val, Len),
            NewAcc = if Left =/= 0, Left == Right -> Acc + 1; true -> Acc end,
            count_hv(Nums, Len, Index + 1, NewAcc)
    end.

find_left(_Nums, I, _Val) when I < 0 ->
    0;
find_left(Nums, I, Val) ->
    N = lists:nth(I + 1, Nums),
    case N == Val of
        true -> find_left(Nums, I - 1, Val);
        false ->
            if N > Val -> 1; true -> -1 end
    end.

find_right(_Nums, I, _Val, Len) when I >= Len ->
    0;
find_right(Nums, I, Val, Len) ->
    N = lists:nth(I + 1, Nums),
    case N == Val of
        true -> find_right(Nums, I + 1, Val, Len);
        false ->
            if N > Val -> 1; true -> -1 end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_hill_valley(nums :: [integer]) :: integer
  def count_hill_valley(nums) do
    len = length(nums)
    loop(1, len, nums, 0)
  end

  defp loop(i, len, _nums, cnt) when i >= len - 1, do: cnt

  defp loop(i, len, nums, cnt) do
    cur = Enum.at(nums, i)
    prev = Enum.at(nums, i - 1)

    if cur == prev do
      loop(i + 1, len, nums, cnt)
    else
      left = find_left(i - 1, cur, nums)
      right = find_right(i + 1, cur, nums, len)

      new_cnt = if left != 0 and left == right, do: cnt + 1, else: cnt
      loop(i + 1, len, nums, new_cnt)
    end
  end

  defp find_left(j, _cur, _nums) when j < 0, do: 0

  defp find_left(j, cur, nums) do
    val = Enum.at(nums, j)

    cond do
      val == cur -> find_left(j - 1, cur, nums)
      val > cur -> 1
      true -> -1
    end
  end

  defp find_right(k, _cur, _nums, len) when k >= len, do: 0

  defp find_right(k, cur, nums, len) do
    val = Enum.at(nums, k)

    cond do
      val == cur -> find_right(k + 1, cur, nums, len)
      val > cur -> 1
      true -> -1
    end
  end
end
```
