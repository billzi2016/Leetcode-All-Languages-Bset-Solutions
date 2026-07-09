# 2605. Form Smallest Number From Two Digit Arrays

## Cpp

```cpp
class Solution {
public:
    int minNumber(vector<int>& nums1, vector<int>& nums2) {
        bool present[10] = {false};
        for (int x : nums1) present[x] = true;
        int common = 10;
        for (int y : nums2) {
            if (present[y]) common = min(common, y);
        }
        if (common != 10) return common;
        int a = *min_element(nums1.begin(), nums1.end());
        int b = *min_element(nums2.begin(), nums2.end());
        return min(10 * a + b, 10 * b + a);
    }
};
```

## Java

```java
class Solution {
    public int minNumber(int[] nums1, int[] nums2) {
        boolean[] in1 = new boolean[10];
        boolean[] in2 = new boolean[10];
        for (int x : nums1) in1[x] = true;
        for (int x : nums2) in2[x] = true;
        for (int d = 1; d <= 9; ++d) {
            if (in1[d] && in2[d]) return d;
        }
        int minA = 10, minB = 10;
        for (int x : nums1) if (x < minA) minA = x;
        for (int x : nums2) if (x < minB) minB = x;
        int cand1 = minA * 10 + minB;
        int cand2 = minB * 10 + minA;
        return Math.min(cand1, cand2);
    }
}
```

## Python

```python
class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        set1 = set(nums1)
        set2 = set(nums2)
        common = set1 & set2
        if common:
            return min(common)
        a = min(nums1)
        b = min(nums2)
        return min(10 * a + b, 10 * b + a)
```

## Python3

```python
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        common = set1 & set2
        if common:
            return min(common)
        a = min(set1)
        b = min(set2)
        return min(10 * a + b, 10 * b + a)
```

## C

```c
int minNumber(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int present[10] = {0};
    for (int i = 0; i < nums1Size; ++i) {
        present[nums1[i]] = 1;
    }
    // Check for common digit
    for (int i = 0; i < nums2Size; ++i) {
        if (present[nums2[i]]) {
            return nums2[i];
        }
    }
    int min1 = 10, min2 = 10;
    for (int i = 0; i < nums1Size; ++i) {
        if (nums1[i] < min1) min1 = nums1[i];
    }
    for (int i = 0; i < nums2Size; ++i) {
        if (nums2[i] < min2) min2 = nums2[i];
    }
    int a = min1 < min2 ? min1 : min2;
    int b = min1 < min2 ? min2 : min1;
    return a * 10 + b;
}
```

## Csharp

```csharp
public class Solution {
    public int MinNumber(int[] nums1, int[] nums2) {
        var set = new HashSet<int>(nums1);
        int commonMin = 10;
        foreach (int x in nums2) {
            if (set.Contains(x) && x < commonMin) {
                commonMin = x;
            }
        }
        if (commonMin != 10) return commonMin;

        int min1 = 10, min2 = 10;
        foreach (int x in nums1) if (x < min1) min1 = x;
        foreach (int x in nums2) if (x < min2) min2 = x;

        int candidate1 = min1 * 10 + min2;
        int candidate2 = min2 * 10 + min1;
        return Math.Min(candidate1, candidate2);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minNumber = function(nums1, nums2) {
    const set1 = new Set(nums1);
    let commonMin = 10;
    for (const v of nums2) {
        if (set1.has(v) && v < commonMin) {
            commonMin = v;
        }
    }
    if (commonMin !== 10) return commonMin;

    let ans = Infinity;
    for (const a of nums1) {
        for (const b of nums2) {
            const cand1 = a * 10 + b;
            const cand2 = b * 10 + a;
            if (cand1 < ans) ans = cand1;
            if (cand2 < ans) ans = cand2;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minNumber(nums1: number[], nums2: number[]): number {
    const set1 = new Set(nums1);
    let commonMin = 10;
    for (const x of nums2) {
        if (set1.has(x)) {
            commonMin = Math.min(commonMin, x);
        }
    }
    if (commonMin < 10) return commonMin;

    let ans = 100;
    for (const a of nums1) {
        for (const b of nums2) {
            const n1 = a * 10 + b;
            const n2 = b * 10 + a;
            if (n1 < ans) ans = n1;
            if (n2 < ans) ans = n2;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function minNumber($nums1, $nums2) {
        $set1 = array_flip($nums1);
        $common = [];
        foreach ($nums2 as $v) {
            if (isset($set1[$v])) {
                $common[] = $v;
            }
        }
        if (!empty($common)) {
            return min($common);
        }

        $ans = PHP_INT_MAX;
        foreach ($nums1 as $a) {
            foreach ($nums2 as $b) {
                $num1 = $a * 10 + $b;
                $num2 = $b * 10 + $a;
                if ($num1 < $ans) $ans = $num1;
                if ($num2 < $ans) $ans = $num2;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minNumber(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let set1 = Set(nums1)
        for v in nums2 {
            if set1.contains(v) {
                return v
            }
        }
        let min1 = nums1.min()!
        let min2 = nums2.min()!
        let smaller = min(min1, min2)
        let larger = max(min1, min2)
        return smaller * 10 + larger
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minNumber(nums1: IntArray, nums2: IntArray): Int {
        val present = BooleanArray(10)
        for (v in nums1) present[v] = true
        var common = -1
        for (v in nums2) {
            if (present[v]) {
                common = v
                break
            }
        }
        if (common != -1) return common
        var min1 = 9
        for (v in nums1) if (v < min1) min1 = v
        var min2 = 9
        for (v in nums2) if (v < min2) min2 = v
        val cand1 = min1 * 10 + min2
        val cand2 = min2 * 10 + min1
        return if (cand1 < cand2) cand1 else cand2
    }
}
```

## Dart

```dart
class Solution {
  int minNumber(List<int> nums1, List<int> nums2) {
    final set2 = nums2.toSet();
    int commonMin = 10;
    for (var x in nums1) {
      if (set2.contains(x) && x < commonMin) {
        commonMin = x;
      }
    }
    if (commonMin != 10) return commonMin;

    int min1 = nums1.reduce((a, b) => a < b ? a : b);
    int min2 = nums2.reduce((a, b) => a < b ? a : b);

    int candidate1 = min1 * 10 + min2;
    int candidate2 = min2 * 10 + min1;
    return candidate1 < candidate2 ? candidate1 : candidate2;
  }
}
```

## Golang

```go
func minNumber(nums1 []int, nums2 []int) int {
	// Record digits from the first array.
	var present [10]bool
	for _, v := range nums1 {
		present[v] = true
	}
	// Check for common digit and keep the smallest one.
	commonMin := 10
	for _, v := range nums2 {
		if present[v] && v < commonMin {
			commonMin = v
		}
	}
	if commonMin != 10 {
		return commonMin
	}
	// No common digit: find minimal digits in each array.
	min1, min2 := 10, 10
	for _, v := range nums1 {
		if v < min1 {
			min1 = v
		}
	}
	for _, v := range nums2 {
		if v < min2 {
			min2 = v
		}
	}
	// Form the two possible two‑digit numbers and return the smaller.
	a := min1*10 + min2
	b := min2*10 + min1
	if a < b {
		return a
	}
	return b
}
```

## Ruby

```ruby
def min_number(nums1, nums2)
  common = nums1 & nums2
  return common.min unless common.empty?
  a_min = nums1.min
  b_min = nums2.min
  [10 * a_min + b_min, 10 * b_min + a_min].min
end
```

## Scala

```scala
object Solution {
    def minNumber(nums1: Array[Int], nums2: Array[Int]): Int = {
        val set1 = nums1.toSet
        var commonMin = 10
        for (x <- nums2) {
            if (set1.contains(x) && x < commonMin) commonMin = x
        }
        if (commonMin != 10) return commonMin
        val a = nums1.min
        val b = nums2.min
        Math.min(a * 10 + b, b * 10 + a)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_number(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        use std::collections::HashSet;
        let set: HashSet<_> = nums1.iter().cloned().collect();
        let mut common_min = 10; // greater than any possible digit
        for &v in &nums2 {
            if set.contains(&v) && v < common_min {
                common_min = v;
            }
        }
        if common_min != 10 {
            return common_min;
        }
        let min1 = *nums1.iter().min().unwrap();
        let min2 = *nums2.iter().min().unwrap();
        let tens = std::cmp::min(min1, min2);
        let ones = std::cmp::max(min1, min2);
        tens * 10 + ones
    }
}
```

## Racket

```racket
(define/contract (min-number nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((common (filter (lambda (x) (member x nums2)) nums1)))
    (if (pair? common)
        (apply min common)
        (let* ((min1 (apply min nums1))
               (min2 (apply min nums2)))
          (if (< min1 min2)
              (+ (* 10 min1) min2)
              (+ (* 10 min2) min1))))))
```

## Erlang

```erlang
-module(solution).
-export([min_number/2]).

-spec min_number(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
min_number(Nums1, Nums2) ->
    Common = [X || X <- Nums1, lists:member(X, Nums2)],
    case Common of
        [] ->
            Min1 = lists:min(Nums1),
            Min2 = lists:min(Nums2),
            if Min1 < Min2 -> 10 * Min1 + Min2;
               true       -> 10 * Min2 + Min1
            end;
        _ ->
            lists:min(Common)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_number(nums1 :: [integer], nums2 :: [integer]) :: integer
  def min_number(nums1, nums2) do
    set1 = MapSet.new(nums1)
    set2 = MapSet.new(nums2)

    common = MapSet.intersection(set1, set2)

    if MapSet.size(common) > 0 do
      Enum.min(common)
    else
      min1 = Enum.min(nums1)
      min2 = Enum.min(nums2)
      a = 10 * min1 + min2
      b = 10 * min2 + min1
      min(a, b)
    end
  end
end
```
