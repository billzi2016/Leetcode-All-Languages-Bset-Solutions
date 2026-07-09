# 1608. Special Array With X Elements Greater Than or Equal X

## Cpp

```cpp
class Solution {
public:
    int specialArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> freq(n + 1, 0);
        for (int v : nums) {
            if (v > n) ++freq[n];
            else ++freq[v];
        }
        int cnt = 0;
        for (int i = n; i >= 0; --i) {
            cnt += freq[i];
            if (cnt == i) return i;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int specialArray(int[] nums) {
        int n = nums.length;
        int[] freq = new int[n + 1];
        for (int v : nums) {
            if (v > n) {
                freq[n]++;
            } else {
                freq[v]++;
            }
        }
        int count = 0;
        for (int i = n; i >= 0; i--) {
            count += freq[i];
            if (count == i) {
                return i;
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        freq = [0] * (n + 1)
        for v in nums:
            if v > n:
                freq[n] += 1
            else:
                freq[v] += 1

        greater_or_equal = 0
        for i in range(n, 0, -1):
            greater_or_equal += freq[i]
            if greater_or_equal == i:
                return i
        return -1
```

## Python3

```python
from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0] * (n + 1)
        for v in nums:
            if v > n:
                freq[n] += 1
            else:
                freq[v] += 1

        cnt = 0
        for i in range(n, 0, -1):
            cnt += freq[i]
            if cnt == i:
                return i
        return -1
```

## C

```c
int specialArray(int* nums, int numsSize) {
    int N = numsSize;
    int freq[101] = {0};  // N <= 100
    for (int i = 0; i < N; ++i) {
        if (nums[i] > N)
            freq[N]++;
        else
            freq[nums[i]]++;
    }
    int cnt = 0;
    for (int x = N; x >= 0; --x) {
        cnt += freq[x];
        if (cnt == x)
            return x;
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution
{
    public int SpecialArray(int[] nums)
    {
        int n = nums.Length;
        int[] freq = new int[n + 1];
        foreach (int v in nums)
        {
            if (v > n) freq[n]++; else freq[v]++;
        }

        int count = 0;
        for (int i = n; i >= 0; i--)
        {
            count += freq[i];
            if (count == i) return i;
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var specialArray = function(nums) {
    nums.sort((a, b) => b - a);
    const n = nums.length;
    for (let i = 1; i <= n; i++) {
        if (nums[i - 1] >= i && (i === n || nums[i] < i)) {
            return i;
        }
    }
    return -1;
};
```

## Typescript

```typescript
function specialArray(nums: number[]): number {
    const n = nums.length;
    const freq = new Array(n + 1).fill(0);
    for (const v of nums) {
        if (v > n) {
            freq[n]++;
        } else {
            freq[v]++;
        }
    }
    let count = 0;
    for (let i = n; i >= 1; i--) {
        count += freq[i];
        if (count === i) return i;
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function specialArray($nums) {
        $n = count($nums);
        // frequency array for values 0..n (values > n are grouped at index n)
        $freq = array_fill(0, $n + 1, 0);
        foreach ($nums as $v) {
            if ($v > $n) {
                $freq[$n]++;
            } else {
                $freq[$v]++;
            }
        }

        $greaterOrEqual = 0;
        for ($i = $n; $i >= 1; $i--) {
            $greaterOrEqual += $freq[$i];
            if ($greaterOrEqual == $i) {
                return $i;
            }
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func specialArray(_ nums: [Int]) -> Int {
        let n = nums.count
        var freq = Array(repeating: 0, count: n + 1)
        for v in nums {
            if v > n {
                freq[n] += 1
            } else {
                freq[v] += 1
            }
        }
        var greaterOrEqual = 0
        for i in stride(from: n, through: 0, by: -1) {
            greaterOrEqual += freq[i]
            if i == greaterOrEqual {
                return i
            }
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun specialArray(nums: IntArray): Int {
        val n = nums.size
        val freq = IntArray(n + 1)
        for (v in nums) {
            if (v >= n) {
                freq[n]++
            } else {
                freq[v]++
            }
        }
        var count = 0
        for (i in n downTo 0) {
            count += freq[i]
            if (i == count) return i
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int specialArray(List<int> nums) {
    int n = nums.length;
    List<int> freq = List.filled(n + 1, 0);
    for (int v in nums) {
      if (v > n) {
        freq[n]++;
      } else {
        freq[v]++;
      }
    }
    int greaterOrEqual = 0;
    for (int i = n; i >= 0; --i) {
      greaterOrEqual += freq[i];
      if (greaterOrEqual == i) return i;
    }
    return -1;
  }
}
```

## Golang

```go
import "sort"

func specialArray(nums []int) int {
	sort.Slice(nums, func(i, j int) bool { return nums[i] > nums[j] })
	n := len(nums)
	for i := 1; i <= n; i++ {
		if nums[i-1] >= i && (i == n || nums[i] < i) {
			return i
		}
	}
	return -1
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def special_array(nums)
  n = nums.length
  freq = Array.new(n + 1, 0)

  nums.each do |v|
    idx = v > n ? n : v
    freq[idx] += 1
  end

  greater_eq = 0
  n.downto(1) do |i|
    greater_eq += freq[i]
    return i if greater_eq == i
  end

  -1
end
```

## Scala

```scala
object Solution {
    def specialArray(nums: Array[Int]): Int = {
        val sorted = nums.sorted
        val n = sorted.length
        for (i <- 0 until n) {
            val x = n - i
            if ((i == 0 || sorted(i - 1) < x) && sorted(i) >= x) return x
        }
        -1
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn special_array(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut freq = vec![0usize; n + 1];
        for &v in &nums {
            if (v as usize) > n {
                freq[n] += 1;
            } else {
                freq[v as usize] += 1;
            }
        }
        let mut cnt = 0usize;
        for i in (1..=n).rev() {
            cnt += freq[i];
            if cnt == i {
                return i as i32;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (special-array nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort nums <))
         (n (length sorted)))
    (let loop ((x 0))
      (if (> x n)
          -1
          (let ((cnt (foldl (lambda (v acc) (if (>= v x) (+ acc 1) acc)) 0 sorted)))
            (if (= cnt x)
                x
                (loop (+ x 1)))))))
```

## Erlang

```erlang
-module(solution).
-export([special_array/1]).

-spec special_array(Nums :: [integer()]) -> integer().
special_array(Nums) ->
    N = length(Nums),
    find_x(N, Nums).

find_x(-1, _Nums) ->
    -1;
find_x(X, Nums) ->
    Count = count_ge(Nums, X),
    if
        Count == X -> X;
        true -> find_x(X - 1, Nums)
    end.

count_ge([], _X) -> 0;
count_ge([H|T], X) when H >= X ->
    1 + count_ge(T, X);
count_ge([_|T], X) ->
    count_ge(T, X).
```

## Elixir

```elixir
defmodule Solution do
  @spec special_array(nums :: [integer]) :: integer
  def special_array(nums) do
    n = length(nums)

    freq =
      Enum.reduce(nums, %{}, fn v, acc ->
        idx = if v > n, do: n, else: v
        Map.update(acc, idx, 1, &(&1 + 1))
      end)

    find_special(n, 0, freq)
  end

  defp find_special(i, sum, _freq) when i < 0, do: -1

  defp find_special(i, sum, freq) do
    new_sum = sum + Map.get(freq, i, 0)

    if new_sum == i do
      i
    else
      find_special(i - 1, new_sum, freq)
    end
  end
end
```
