# 2784. Check if Array is Good

## Cpp

```cpp
class Solution {
public:
    bool isGood(std::vector<int>& nums) {
        int n = *std::max_element(nums.begin(), nums.end());
        if ((int)nums.size() != n + 1) return false;
        std::vector<int> cnt(n + 1, 0);
        for (int x : nums) {
            if (x < 1 || x > n) return false;
            ++cnt[x];
        }
        for (int i = 1; i < n; ++i) {
            if (cnt[i] != 1) return false;
        }
        return cnt[n] == 2;
    }
};
```

## Java

```java
class Solution {
    public boolean isGood(int[] nums) {
        int max = 0;
        for (int v : nums) {
            if (v > max) max = v;
        }
        if (nums.length != max + 1) return false;
        int[] cnt = new int[max + 1];
        for (int v : nums) {
            if (v < 1 || v > max) return false;
            cnt[v]++;
        }
        if (cnt[max] != 2) return false;
        for (int i = 1; i < max; i++) {
            if (cnt[i] != 1) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        n = max(nums)
        # length must be n + 1
        if len(nums) != n + 1:
            return False
        from collections import Counter
        cnt = Counter(nums)
        # check frequencies
        for i in range(1, n):
            if cnt.get(i, 0) != 1:
                return False
        if cnt.get(n, 0) != 2:
            return False
        # ensure no extra numbers beyond n
        if any(k > n for k in cnt):
            return False
        return True
```

## Python3

```python
from collections import Counter
from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums) != n + 1:
            return False
        cnt = Counter(nums)
        for num in range(1, n):
            if cnt.get(num, 0) != 1:
                return False
        if cnt.get(n, 0) != 2:
            return False
        # No other numbers should be present
        if len(cnt) != n:
            return False
        return True
```

## C

```c
#include <stdbool.h>

bool isGood(int* nums, int numsSize) {
    int max = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > max) max = nums[i];
    }
    if (numsSize != max + 1) return false;

    int freq[201] = {0};
    for (int i = 0; i < numsSize; ++i) {
        int v = nums[i];
        if (v < 1 || v > 200) return false;
        ++freq[v];
    }

    for (int i = 1; i < max; ++i) {
        if (freq[i] != 1) return false;
    }
    if (freq[max] != 2) return false;

    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsGood(int[] nums) {
        int max = 0;
        foreach (int x in nums) {
            if (x > max) max = x;
        }
        // base[n] has length n+1
        if (nums.Length != max + 1) return false;

        int[] cnt = new int[max + 1];
        foreach (int x in nums) {
            if (x <= max) cnt[x]++;
            else return false; // should not happen, but safety
        }

        for (int i = 1; i < max; i++) {
            if (cnt[i] != 1) return false;
        }
        if (cnt[max] != 2) return false;

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isGood = function(nums) {
    // Find maximum element, which must be n
    let n = 0;
    for (const v of nums) {
        if (v > n) n = v;
    }
    // Length must be exactly n + 1
    if (nums.length !== n + 1) return false;
    
    const freq = new Array(n + 1).fill(0);
    for (const v of nums) {
        if (v < 1 || v > n) return false; // out of expected range
        freq[v]++;
    }
    
    // Check frequencies: numbers 1..n-1 appear once, n appears twice
    for (let i = 1; i <= n; i++) {
        const expected = (i === n) ? 2 : 1;
        if (freq[i] !== expected) return false;
    }
    
    return true;
};
```

## Typescript

```typescript
function isGood(nums: number[]): boolean {
    const n = Math.max(...nums);
    if (nums.length !== n + 1) return false;
    const cnt = new Array(n + 1).fill(0);
    for (const x of nums) {
        if (x > n) return false;
        cnt[x]++;
    }
    if (cnt[n] !== 2) return false;
    for (let i = 1; i < n; ++i) {
        if (cnt[i] !== 1) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function isGood($nums) {
        $n = max($nums);
        if (count($nums) != $n + 1) {
            return false;
        }
        // frequency array for values 0..$n
        $freq = array_fill(0, $n + 1, 0);
        foreach ($nums as $v) {
            if ($v > $n) {
                return false;
            }
            $freq[$v]++;
        }
        // check numbers 1 .. n-1 appear exactly once
        for ($i = 1; $i < $n; $i++) {
            if ($freq[$i] !== 1) {
                return false;
            }
        }
        // check n appears twice
        if ($freq[$n] !== 2) {
            return false;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isGood(_ nums: [Int]) -> Bool {
        guard let n = nums.max() else { return false }
        if nums.count != n + 1 { return false }
        
        var freq = [Int:Int]()
        for v in nums {
            if v > n { return false }
            freq[v, default: 0] += 1
        }
        
        // Check counts for numbers 1 to n-1
        if n > 1 {
            for i in 1..<n {
                if freq[i] != 1 {
                    return false
                }
            }
        }
        // Check count for n
        return freq[n] == 2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isGood(nums: IntArray): Boolean {
        var max = 0
        for (v in nums) if (v > max) max = v
        if (nums.size != max + 1) return false
        val freq = IntArray(max + 1)
        for (v in nums) {
            if (v <= max) {
                freq[v]++
            } else {
                return false
            }
        }
        for (i in 1 until max) {
            if (freq[i] != 1) return false
        }
        return freq[max] == 2
    }
}
```

## Dart

```dart
class Solution {
  bool isGood(List<int> nums) {
    int n = nums.reduce((a, b) => a > b ? a : b);
    if (nums.length != n + 1) return false;
    List<int> cnt = List.filled(n + 1, 0);
    for (int x in nums) {
      if (x < 1 || x > n) return false;
      cnt[x]++;
    }
    for (int i = 1; i < n; i++) {
      if (cnt[i] != 1) return false;
    }
    return cnt[n] == 2;
  }
}
```

## Golang

```go
func isGood(nums []int) bool {
	if len(nums) == 0 {
		return false
	}
	maxVal := nums[0]
	for _, v := range nums {
		if v > maxVal {
			maxVal = v
		}
	}
	if len(nums) != maxVal+1 {
		return false
	}
	counts := make([]int, maxVal+1)
	for _, v := range nums {
		if v <= 0 || v > maxVal {
			return false
		}
		counts[v]++
	}
	for i := 1; i < maxVal; i++ {
		if counts[i] != 1 {
			return false
		}
	}
	if counts[maxVal] != 2 {
		return false
	}
	return true
}
```

## Ruby

```ruby
def is_good(nums)
  n = nums.max
  return false unless nums.length == n + 1

  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }

  (1...n).each do |i|
    return false unless freq[i] == 1
  end

  freq[n] == 2
end
```

## Scala

```scala
object Solution {
    def isGood(nums: Array[Int]): Boolean = {
        if (nums.isEmpty) return false
        val n = nums.max
        if (nums.length != n + 1) return false
        val cnt = new Array[Int](n + 1)
        for (x <- nums) {
            if (x < 1 || x > n) return false
            cnt(x) += 1
        }
        for (i <- 1 until n) {
            if (cnt(i) != 1) return false
        }
        cnt(n) == 2
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_good(nums: Vec<i32>) -> bool {
        if nums.is_empty() {
            return false;
        }
        let &max_val = nums.iter().max().unwrap();
        let n = max_val as usize;
        if nums.len() != n + 1 {
            return false;
        }
        let mut cnt = vec![0usize; n + 2];
        for &v in &nums {
            let vi = v as usize;
            if vi > n {
                return false;
            }
            cnt[vi] += 1;
        }
        for i in 1..n {
            if cnt[i] != 1 {
                return false;
            }
        }
        cnt[n] == 2
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(define/contract (is-good nums)
  (-> (listof exact-integer?) boolean?)
  (let* ((max-val (apply max nums))
         (len (length nums)))
    (if (not (= len (+ max-val 1)))
        #false
        (let* ((sorted-nums (sort nums <))
               (prefix (if (> max-val 1)
                           (build-list (- max-val 1) (lambda (i) (+ i 1)))
                           '()))
               (expected (append prefix (list max-val max-val))))
          (equal? sorted-nums expected)))))
```

## Erlang

```erlang
-spec is_good([integer()]) -> boolean().
is_good(Nums) ->
    N = lists:max(Nums),
    case length(Nums) == N + 1 of
        false -> false;
        true ->
            Sorted = lists:sort(Nums),
            Expected = (lists:seq(1, N - 1)) ++ [N, N],
            Sorted =:= Expected
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_good(nums :: [integer]) :: boolean
  def is_good(nums) do
    n = Enum.max(nums)

    if length(nums) != n + 1 do
      false
    else
      freq =
        Enum.reduce(nums, %{}, fn x, acc ->
          Map.update(acc, x, 1, &(&1 + 1))
        end)

      cond do
        Map.get(freq, n, 0) != 2 -> false
        Enum.any?(1..(n - 1), fn i -> Map.get(freq, i, 0) != 1 end) -> false
        true -> true
      end
    end
  end
end
```
