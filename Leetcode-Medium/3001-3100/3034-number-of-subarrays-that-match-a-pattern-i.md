# 3034. Number of Subarrays That Match a Pattern I

## Cpp

```cpp
class Solution {
public:
    int countMatchingSubarrays(vector<int>& nums, vector<int>& pattern) {
        int n = nums.size();
        int m = pattern.size(); // subarray length will be m+1
        int ans = 0;
        for (int i = 0; i + m < n; ++i) {
            bool ok = true;
            for (int k = 0; k < m; ++k) {
                long long diff = (long long)nums[i + k + 1] - nums[i + k];
                int sign = (diff > 0) - (diff < 0); // yields 1, 0, or -1
                if (sign != pattern[k]) {
                    ok = false;
                    break;
                }
            }
            if (ok) ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countMatchingSubarrays(int[] nums, int[] pattern) {
        int n = nums.length;
        int m = pattern.length;
        int count = 0;
        for (int i = 0; i + m < n; i++) { // subarray of length m+1
            boolean matches = true;
            for (int k = 0; k < m; k++) {
                int a = nums[i + k];
                int b = nums[i + k + 1];
                int rel;
                if (a < b) {
                    rel = 1;
                } else if (a == b) {
                    rel = 0;
                } else {
                    rel = -1;
                }
                if (rel != pattern[k]) {
                    matches = false;
                    break;
                }
            }
            if (matches) {
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
    def countMatchingSubarrays(self, nums, pattern):
        """
        :type nums: List[int]
        :type pattern: List[int]
        :rtype: int
        """
        n = len(nums)
        m = len(pattern)
        count = 0
        for i in range(n - m):
            match = True
            for k in range(m):
                if pattern[k] == 1:
                    if not (nums[i + k] < nums[i + k + 1]):
                        match = False
                        break
                elif pattern[k] == 0:
                    if not (nums[i + k] == nums[i + k + 1]):
                        match = False
                        break
                else:  # pattern[k] == -1
                    if not (nums[i + k] > nums[i + k + 1]):
                        match = False
                        break
            if match:
                count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        count = 0
        for i in range(n - m):
            match = True
            for k in range(m):
                diff = nums[i + k + 1] - nums[i + k]
                sign = 0
                if diff > 0:
                    sign = 1
                elif diff < 0:
                    sign = -1
                if sign != pattern[k]:
                    match = False
                    break
            if match:
                count += 1
        return count
```

## C

```c
int countMatchingSubarrays(int* nums, int numsSize, int* pattern, int patternSize) {
    int count = 0;
    int subLen = patternSize + 1;
    for (int i = 0; i + subLen <= numsSize; ++i) {
        int ok = 1;
        for (int k = 0; k < patternSize; ++k) {
            if (pattern[k] == 1) {
                if (!(nums[i + k] < nums[i + k + 1])) { ok = 0; break; }
            } else if (pattern[k] == -1) {
                if (!(nums[i + k] > nums[i + k + 1])) { ok = 0; break; }
            } else { // pattern[k] == 0
                if (nums[i + k] != nums[i + k + 1]) { ok = 0; break; }
            }
        }
        if (ok) ++count;
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int CountMatchingSubarrays(int[] nums, int[] pattern) {
        int n = nums.Length;
        int m = pattern.Length;
        int count = 0;
        for (int i = 0; i + m < n; i++) {
            bool ok = true;
            for (int k = 0; k < m; k++) {
                int a = nums[i + k];
                int b = nums[i + k + 1];
                if (pattern[k] == 1) {
                    if (!(a < b)) { ok = false; break; }
                } else if (pattern[k] == 0) {
                    if (a != b) { ok = false; break; }
                } else { // -1
                    if (!(a > b)) { ok = false; break; }
                }
            }
            if (ok) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} pattern
 * @return {number}
 */
var countMatchingSubarrays = function(nums, pattern) {
    const n = nums.length;
    const m = pattern.length; // subarray length will be m+1
    let count = 0;

    for (let i = 0; i <= n - m - 1; i++) {
        let ok = true;
        for (let k = 0; k < m; k++) {
            const a = nums[i + k];
            const b = nums[i + k + 1];
            let sign = 0;
            if (a < b) sign = -1;
            else if (a > b) sign = 1;
            // else sign stays 0
            if (sign !== pattern[k]) {
                ok = false;
                break;
            }
        }
        if (ok) count++;
    }

    return count;
};
```

## Typescript

```typescript
function countMatchingSubarrays(nums: number[], pattern: number[]): number {
    const n = nums.length;
    const m = pattern.length;
    let count = 0;

    for (let i = 0; i <= n - m - 1; i++) {
        let ok = true;
        for (let k = 0; k < m; k++) {
            const a = nums[i + k];
            const b = nums[i + k + 1];
            if (pattern[k] === 1) {
                if (!(a < b)) { ok = false; break; }
            } else if (pattern[k] === -1) {
                if (!(a > b)) { ok = false; break; }
            } else { // pattern[k] === 0
                if (a !== b) { ok = false; break; }
            }
        }
        if (ok) count++;
    }

    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $pattern
     * @return Integer
     */
    function countMatchingSubarrays($nums, $pattern) {
        $n = count($nums);
        $m = count($pattern);
        $len = $m + 1;
        $ans = 0;

        for ($i = 0; $i <= $n - $len; $i++) {
            $ok = true;
            for ($k = 0; $k < $m; $k++) {
                $a = $nums[$i + $k];
                $b = $nums[$i + $k + 1];

                if ($a < $b) {
                    $sign = 1;
                } elseif ($a == $b) {
                    $sign = 0;
                } else {
                    $sign = -1;
                }

                if ($sign !== $pattern[$k]) {
                    $ok = false;
                    break;
                }
            }
            if ($ok) {
                $ans++;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countMatchingSubarrays(_ nums: [Int], _ pattern: [Int]) -> Int {
        let n = nums.count
        let m = pattern.count
        if n < m + 1 { return 0 }
        var result = 0
        for i in 0...(n - m - 1) {
            var matches = true
            for k in 0..<m {
                let a = nums[i + k]
                let b = nums[i + k + 1]
                var sign = 0
                if a < b { sign = 1 }
                else if a > b { sign = -1 }
                if sign != pattern[k] {
                    matches = false
                    break
                }
            }
            if matches { result += 1 }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countMatchingSubarrays(nums: IntArray, pattern: IntArray): Int {
        val n = nums.size
        val m = pattern.size
        var count = 0
        for (i in 0 until n - m) {
            var ok = true
            for (k in 0 until m) {
                when (pattern[k]) {
                    1 -> if (nums[i + k] >= nums[i + k + 1]) { ok = false; break }
                    -1 -> if (nums[i + k] <= nums[i + k + 1]) { ok = false; break }
                    0 -> if (nums[i + k] != nums[i + k + 1]) { ok = false; break }
                }
            }
            if (ok) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countMatchingSubarrays(List<int> nums, List<int> pattern) {
    int n = nums.length;
    int m = pattern.length;
    int count = 0;

    for (int i = 0; i <= n - m - 1; ++i) {
      bool matches = true;
      for (int k = 0; k < m; ++k) {
        int diff = nums[i + k + 1] - nums[i + k];
        if (pattern[k] == 1 && diff <= 0) {
          matches = false;
          break;
        }
        if (pattern[k] == -1 && diff >= 0) {
          matches = false;
          break;
        }
        if (pattern[k] == 0 && diff != 0) {
          matches = false;
          break;
        }
      }
      if (matches) count++;
    }

    return count;
  }
}
```

## Golang

```go
func countMatchingSubarrays(nums []int, pattern []int) int {
    n := len(nums)
    m := len(pattern)
    cnt := 0
    for i := 0; i+m < n; i++ {
        match := true
        for k := 0; k < m; k++ {
            a, b := nums[i+k], nums[i+k+1]
            switch pattern[k] {
            case 1:
                if !(a < b) {
                    match = false
                }
            case -1:
                if !(a > b) {
                    match = false
                }
            case 0:
                if a != b {
                    match = false
                }
            }
            if !match {
                break
            }
        }
        if match {
            cnt++
        }
    }
    return cnt
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} pattern
# @return {Integer}
def count_matching_subarrays(nums, pattern)
  n = nums.length
  m = pattern.length
  target_len = m + 1
  count = 0

  (0..n - target_len).each do |i|
    match = true
    (0...m).each do |k|
      case pattern[k]
      when 1
        unless nums[i + k] < nums[i + k + 1]
          match = false
          break
        end
      when -1
        unless nums[i + k] > nums[i + k + 1]
          match = false
          break
        end
      else # 0
        unless nums[i + k] == nums[i + k + 1]
          match = false
          break
        end
      end
    end
    count += 1 if match
  end

  count
end
```

## Scala

```scala
object Solution {
    def countMatchingSubarrays(nums: Array[Int], pattern: Array[Int]): Int = {
        val n = nums.length
        val m = pattern.length
        var count = 0
        for (i <- 0 to n - m - 1) {
            var ok = true
            var k = 0
            while (k < m && ok) {
                val cmp = Integer.compare(nums(i + k), nums(i + k + 1))
                // cmp: -1 if first<second, 0 if equal, 1 if first>second
                // pattern expects 1 for '<', 0 for '=', -1 for '>'
                val expected = pattern(k)
                // Convert cmp to pattern value:
                // If nums[i] < nums[i+1], cmp = -1 -> pattern should be 1
                // If equal, cmp=0 -> pattern 0
                // If greater, cmp=1 -> pattern -1
                val actualPattern = if (cmp == -1) 1 else if (cmp == 0) 0 else -1
                if (actualPattern != expected) ok = false
                k += 1
            }
            if (ok) count += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_matching_subarrays(nums: Vec<i32>, pattern: Vec<i32>) -> i32 {
        let n = nums.len();
        let m = pattern.len(); // pattern length
        let mut count = 0;
        // subarray size is m + 1, start indices from 0 to n - (m+1)
        for i in 0..=n - m - 1 {
            let mut ok = true;
            for k in 0..m {
                let a = nums[i + k];
                let b = nums[i + k + 1];
                match pattern[k] {
                    1 => {
                        if !(a < b) {
                            ok = false;
                            break;
                        }
                    }
                    0 => {
                        if a != b {
                            ok = false;
                            break;
                        }
                    }
                    -1 => {
                        if !(a > b) {
                            ok = false;
                            break;
                        }
                    }
                    _ => {}
                }
            }
            if ok {
                count += 1;
            }
        }
        count as i32
    }
}
```

## Racket

```racket
(define/contract (count-matching-subarrays nums pattern)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (m (length pattern))
         (vnums (list->vector nums))
         (vpat (list->vector pattern)))
    (for/sum ([i (in-range (- n m))])
      (if (for/and ([k (in-range m)])
            (let ((a (vector-ref vnums (+ i k)))
                  (b (vector-ref vnums (+ i k 1)))
                  (p (vector-ref vpat k)))
              (cond [(= p 1) (< a b)]
                    [(= p 0) (= a b)]
                    [else (> a b)])))
          1
          0))))
```

## Erlang

```erlang
-spec count_matching_subarrays(Nums :: [integer()], Pattern :: [integer()]) -> integer().
count_matching_subarrays(Nums, Pattern) ->
    N = length(Nums),
    M = length(Pattern),
    Tuple = list_to_tuple(Nums),
    MaxStart = N - M - 1,
    count_matches(0, MaxStart, Tuple, Pattern, 0).

-spec count_matches(integer(), integer(), tuple(), [integer()], integer()) -> integer().
count_matches(Index, Max, _Tuple, _Pattern, Acc) when Index > Max ->
    Acc;
count_matches(Index, Max, Tuple, Pattern, Acc) ->
    case matches(Index, Tuple, Pattern) of
        true -> count_matches(Index + 1, Max, Tuple, Pattern, Acc + 1);
        false -> count_matches(Index + 1, Max, Tuple, Pattern, Acc)
    end.

-spec matches(integer(), tuple(), [integer()]) -> boolean().
matches(_Pos, _Tuple, []) ->
    true;
matches(Pos, Tuple, [P|Rest]) ->
    X = element(Pos + 1, Tuple),
    Y = element(Pos + 2, Tuple),
    case {P, X < Y, X == Y, X > Y} of
        {1, true, _, _} -> matches(Pos + 1, Tuple, Rest);
        {0, _, true, _} -> matches(Pos + 1, Tuple, Rest);
        {-1, _, _, true} -> matches(Pos + 1, Tuple, Rest);
        _ -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_matching_subarrays(nums :: [integer], pattern :: [integer]) :: integer
  def count_matching_subarrays(nums, pattern) do
    n = length(nums)
    m = length(pattern)
    max_start = n - m - 1

    Enum.reduce(0..max_start, 0, fn i, acc ->
      if matches?(nums, pattern, i), do: acc + 1, else: acc
    end)
  end

  defp matches?(nums, pattern, start) do
    Enum.with_index(pattern)
    |> Enum.all?(fn {p, k} ->
      a = Enum.at(nums, start + k)
      b = Enum.at(nums, start + k + 1)

      case p do
        -1 -> a < b
        0 -> a == b
        1 -> a > b
      end
    end)
  end
end
```
