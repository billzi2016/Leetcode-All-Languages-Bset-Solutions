# 2012. Sum of Beauty in the Array

## Cpp

```cpp
class Solution {
public:
    int sumOfBeauties(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefMax(n), prefMin(n);
        prefMax[0] = prefMin[0] = nums[0];
        for (int i = 1; i < n; ++i) {
            prefMax[i] = max(prefMax[i - 1], nums[i]);
            prefMin[i] = min(prefMin[i - 1], nums[i]);
        }
        vector<int> suffMax(n), suffMin(n);
        suffMax[n - 1] = suffMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            suffMax[i] = max(suffMax[i + 1], nums[i]);
            suffMin[i] = min(suffMin[i + 1], nums[i]);
        }
        int ans = 0;
        for (int i = 1; i <= n - 2; ++i) {
            if (nums[i] > prefMax[i - 1] && nums[i] < suffMin[i + 1]) {
                ans += 2;
            } else if (prefMin[i - 1] < nums[i] && suffMax[i + 1] > nums[i]) {
                ans += 1;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int sumOfBeauties(int[] nums) {
        int n = nums.length;
        int[] prefMax = new int[n];
        int[] prefMin = new int[n];
        int[] suffMax = new int[n];
        int[] suffMin = new int[n];

        prefMax[0] = nums[0];
        prefMin[0] = nums[0];
        for (int i = 1; i < n; i++) {
            prefMax[i] = Math.max(prefMax[i - 1], nums[i]);
            prefMin[i] = Math.min(prefMin[i - 1], nums[i]);
        }

        suffMax[n - 1] = nums[n - 1];
        suffMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffMax[i] = Math.max(suffMax[i + 1], nums[i]);
            suffMin[i] = Math.min(suffMin[i + 1], nums[i]);
        }

        int sum = 0;
        for (int i = 1; i <= n - 2; i++) {
            if (nums[i] > prefMax[i - 1] && nums[i] < suffMin[i + 1]) {
                sum += 2;
            } else if (prefMin[i - 1] < nums[i] && suffMax[i + 1] > nums[i]) {
                sum += 1;
            }
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return 0

        # prefix max and min up to i-1
        pref_max = [0] * n
        pref_min = [0] * n
        cur_max = nums[0]
        cur_min = nums[0]
        pref_max[0] = -float('inf')  # unused for i=0
        pref_min[0] = float('inf')
        for i in range(1, n):
            pref_max[i] = cur_max
            pref_min[i] = cur_min
            if nums[i] > cur_max:
                cur_max = nums[i]
            if nums[i] < cur_min:
                cur_min = nums[i]

        # suffix min and max from i+1 to end
        suff_min = [0] * n
        suff_max = [0] * n
        cur_min = nums[-1]
        cur_max = nums[-1]
        suff_min[-1] = float('inf')
        suff_max[-1] = -float('inf')
        for i in range(n - 2, -1, -1):
            suff_min[i] = cur_min
            suff_max[i] = cur_max
            if nums[i] < cur_min:
                cur_min = nums[i]
            if nums[i] > cur_max:
                cur_max = nums[i]

        total = 0
        for i in range(1, n - 1):
            if nums[i] > pref_max[i] and nums[i] < suff_min[i]:
                total += 2
            elif pref_min[i] < nums[i] and suff_max[i] > nums[i]:
                total += 1
        return total
```

## Python3

```python
from typing import List

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        prefix_max = [0] * n
        cur_max = nums[0]
        for i in range(1, n):
            prefix_max[i] = cur_max
            if nums[i] > cur_max:
                cur_max = nums[i]

        suffix_min = [0] * n
        cur_min = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = cur_min
            if nums[i] < cur_min:
                cur_min = nums[i]

        total = 0
        for i in range(1, n - 1):
            left = prefix_max[i]
            right = suffix_min[i]
            if nums[i] > left and nums[i] < right:
                total += 2
            elif nums[i] > left or nums[i] < right:
                total += 1

        return total
```

## C

```c
#include <limits.h>
#include <stdlib.h>

int sumOfBeauties(int* nums, int numsSize) {
    if (numsSize < 3) return 0;
    
    int *leftMin = (int*)malloc(numsSize * sizeof(int));
    int *leftMax = (int*)malloc(numsSize * sizeof(int));
    int *rightMin = (int*)malloc(numsSize * sizeof(int));
    int *rightMax = (int*)malloc(numsSize * sizeof(int));
    
    leftMin[0] = INT_MAX;
    leftMax[0] = INT_MIN;
    for (int i = 1; i < numsSize; ++i) {
        leftMin[i] = (nums[i - 1] < leftMin[i - 1]) ? nums[i - 1] : leftMin[i - 1];
        leftMax[i] = (nums[i - 1] > leftMax[i - 1]) ? nums[i - 1] : leftMax[i - 1];
    }
    
    rightMin[numsSize - 1] = INT_MAX;
    rightMax[numsSize - 1] = INT_MIN;
    for (int i = numsSize - 2; i >= 0; --i) {
        rightMin[i] = (nums[i + 1] < rightMin[i + 1]) ? nums[i + 1] : rightMin[i + 1];
        rightMax[i] = (nums[i + 1] > rightMax[i + 1]) ? nums[i + 1] : rightMax[i + 1];
    }
    
    int sum = 0;
    for (int i = 1; i <= numsSize - 2; ++i) {
        if (nums[i] > leftMax[i] && nums[i] < rightMin[i]) {
            sum += 2;
        } else if (leftMin[i] < nums[i] && rightMax[i] > nums[i]) {
            sum += 1;
        }
    }
    
    free(leftMin);
    free(leftMax);
    free(rightMin);
    free(rightMax);
    
    return sum;
}
```

## Csharp

```csharp
public class Solution {
    public int SumOfBeauties(int[] nums) {
        int n = nums.Length;
        int[] prefixMax = new int[n];
        int[] prefixMin = new int[n];
        int curMax = nums[0];
        int curMin = nums[0];
        for (int i = 1; i < n; i++) {
            prefixMax[i] = curMax;
            prefixMin[i] = curMin;
            if (nums[i] > curMax) curMax = nums[i];
            if (nums[i] < curMin) curMin = nums[i];
        }

        int[] suffixMin = new int[n];
        int[] suffixMax = new int[n];
        int curSMin = nums[n - 1];
        int curSMax = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffixMin[i] = curSMin;
            suffixMax[i] = curSMax;
            if (nums[i] < curSMin) curSMin = nums[i];
            if (nums[i] > curSMax) curSMax = nums[i];
        }

        int sum = 0;
        for (int i = 1; i <= n - 2; i++) {
            if (nums[i] > prefixMax[i] && nums[i] < suffixMin[i]) {
                sum += 2;
            } else if (prefixMin[i] < nums[i] && suffixMax[i] > nums[i]) {
                sum += 1;
            }
        }

        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfBeauties = function(nums) {
    const n = nums.length;
    const prefMax = new Array(n);
    const prefMin = new Array(n);
    const suffixMin = new Array(n);
    const suffixMax = new Array(n);
    
    // Prefix max/min (excluding current index)
    let curMax = nums[0];
    let curMin = nums[0];
    prefMax[0] = -Infinity;
    prefMin[0] = Infinity;
    for (let i = 1; i < n; ++i) {
        prefMax[i] = curMax;
        prefMin[i] = curMin;
        if (nums[i] > curMax) curMax = nums[i];
        if (nums[i] < curMin) curMin = nums[i];
    }
    
    // Suffix min/max (excluding current index)
    let curSufMin = nums[n - 1];
    let curSufMax = nums[n - 1];
    suffixMin[n - 1] = Infinity;
    suffixMax[n - 1] = -Infinity;
    for (let i = n - 2; i >= 0; --i) {
        suffixMin[i] = curSufMin;
        suffixMax[i] = curSufMax;
        if (nums[i] < curSufMin) curSufMin = nums[i];
        if (nums[i] > curSufMax) curSufMax = nums[i];
    }
    
    let sum = 0;
    for (let i = 1; i <= n - 2; ++i) {
        const val = nums[i];
        if (val > prefMax[i] && val < suffixMin[i]) {
            sum += 2;
        } else if (prefMin[i] < val && suffixMax[i] > val) {
            sum += 1;
        }
    }
    
    return sum;
};
```

## Typescript

```typescript
function sumOfBeauties(nums: number[]): number {
    const n = nums.length;
    const prefixMax = new Array<number>(n);
    const prefixMin = new Array<number>(n);
    const suffixMin = new Array<number>(n);
    const suffixMax = new Array<number>(n);

    for (let i = 0; i < n; i++) {
        if (i === 0) {
            prefixMax[i] = nums[i];
            prefixMin[i] = nums[i];
        } else {
            prefixMax[i] = Math.max(prefixMax[i - 1], nums[i]);
            prefixMin[i] = Math.min(prefixMin[i - 1], nums[i]);
        }
    }

    for (let i = n - 1; i >= 0; i--) {
        if (i === n - 1) {
            suffixMin[i] = nums[i];
            suffixMax[i] = nums[i];
        } else {
            suffixMin[i] = Math.min(suffixMin[i + 1], nums[i]);
            suffixMax[i] = Math.max(suffixMax[i + 1], nums[i]);
        }
    }

    let sum = 0;
    for (let i = 1; i <= n - 2; i++) {
        const leftMax = prefixMax[i - 1];
        const rightMin = suffixMin[i + 1];

        if (nums[i] > leftMax && nums[i] < rightMin) {
            sum += 2;
        } else {
            const leftMin = prefixMin[i - 1];
            const rightMax = suffixMax[i + 1];
            if (nums[i] > leftMin && nums[i] < rightMax) {
                sum += 1;
            }
        }
    }

    return sum;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumOfBeauties($nums) {
        $n = count($nums);
        if ($n < 3) return 0;

        $prefixMax = array_fill(0, $n, 0);
        $prefixMin = array_fill(0, $n, 0);
        $suffixMin = array_fill(0, $n, 0);
        $suffixMax = array_fill(0, $n, 0);

        $max = -1;                 // nums[i] >= 1
        $min = PHP_INT_MAX;
        for ($i = 0; $i < $n; $i++) {
            $prefixMax[$i] = $max;
            $prefixMin[$i] = $min;
            if ($nums[$i] > $max) $max = $nums[$i];
            if ($nums[$i] < $min) $min = $nums[$i];
        }

        $max = -1;
        $min = PHP_INT_MAX;
        for ($i = $n - 1; $i >= 0; $i--) {
            $suffixMin[$i] = $min;
            $suffixMax[$i] = $max;
            if ($nums[$i] > $max) $max = $nums[$i];
            if ($nums[$i] < $min) $min = $nums[$i];
        }

        $sum = 0;
        for ($i = 1; $i <= $n - 2; $i++) {
            $val = $nums[$i];
            if ($val > $prefixMax[$i] && $val < $suffixMin[$i]) {
                $sum += 2;
            } elseif ($val > $prefixMin[$i] && $val < $suffixMax[$i]) {
                $sum += 1;
            }
        }

        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func sumOfBeauties(_ nums: [Int]) -> Int {
        let n = nums.count
        if n < 3 { return 0 }
        
        var prefixMax = Array(repeating: 0, count: n)
        var prefixMin = Array(repeating: 0, count: n)
        var suffixMin = Array(repeating: 0, count: n)
        var suffixMax = Array(repeating: 0, count: n)
        
        var curMax = nums[0]
        var curMin = nums[0]
        for i in 1..<n {
            prefixMax[i] = curMax
            prefixMin[i] = curMin
            if nums[i] > curMax { curMax = nums[i] }
            if nums[i] < curMin { curMin = nums[i] }
        }
        
        var curSufMin = nums[n - 1]
        var curSufMax = nums[n - 1]
        for i in stride(from: n - 2, through: 0, by: -1) {
            suffixMin[i] = curSufMin
            suffixMax[i] = curSufMax
            if nums[i] < curSufMin { curSufMin = nums[i] }
            if nums[i] > curSufMax { curSufMax = nums[i] }
        }
        
        var result = 0
        for i in 1..<(n - 1) {
            let val = nums[i]
            if val > prefixMax[i] && val < suffixMin[i] {
                result += 2
            } else if prefixMin[i] < val && suffixMax[i] > val {
                result += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumOfBeauties(nums: IntArray): Int {
        val n = nums.size
        val prefixMax = IntArray(n)
        var curMax = nums[0]
        for (i in 0 until n) {
            if (nums[i] > curMax) curMax = nums[i]
            prefixMax[i] = curMax
        }
        val suffixMin = IntArray(n)
        var curMin = nums[n - 1]
        for (i in n - 1 downTo 0) {
            if (nums[i] < curMin) curMin = nums[i]
            suffixMin[i] = curMin
        }
        var ans = 0
        for (i in 1 until n - 1) {
            val leftMax = prefixMax[i - 1]
            val rightMin = suffixMin[i + 1]
            if (nums[i] > leftMax && nums[i] < rightMin) {
                ans += 2
            } else if (leftMax < nums[i] && rightMin > nums[i]) {
                ans += 1
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int sumOfBeauties(List<int> nums) {
    int n = nums.length;
    // prefix min up to i-1
    List<int> prefixMin = List.filled(n, 0);
    int curMin = nums[0];
    for (int i = 1; i < n; i++) {
      prefixMin[i] = curMin;
      if (nums[i] < curMin) curMin = nums[i];
    }

    // suffix max from i+1 to end
    List<int> suffixMax = List.filled(n, 0);
    int curMax = nums[n - 1];
    for (int i = n - 2; i >= 0; i--) {
      suffixMax[i] = curMax;
      if (nums[i] > curMax) curMax = nums[i];
    }

    // prefix max up to i-1
    List<int> prefixMax = List.filled(n, 0);
    int curPrefMax = nums[0];
    for (int i = 1; i < n; i++) {
      prefixMax[i] = curPrefMax;
      if (nums[i] > curPrefMax) curPrefMax = nums[i];
    }

    // suffix min from i+1 to end
    List<int> suffixMin = List.filled(n, 0);
    int curSufMin = nums[n - 1];
    for (int i = n - 2; i >= 0; i--) {
      suffixMin[i] = curSufMin;
      if (nums[i] < curSufMin) curSufMin = nums[i];
    }

    int ans = 0;
    for (int i = 1; i <= n - 2; i++) {
      if (prefixMax[i] < nums[i] && nums[i] < suffixMin[i]) {
        ans += 2;
      } else if (prefixMin[i] < nums[i] && suffixMax[i] > nums[i]) {
        ans += 1;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func sumOfBeauties(nums []int) int {
	n := len(nums)
	if n < 3 {
		return 0
	}
	prefMax := make([]int, n)
	prefMin := make([]int, n)
	suffMin := make([]int, n)
	suffMax := make([]int, n)

	prefMax[0], prefMin[0] = nums[0], nums[0]
	for i := 1; i < n; i++ {
		if nums[i] > prefMax[i-1] {
			prefMax[i] = nums[i]
		} else {
			prefMax[i] = prefMax[i-1]
		}
		if nums[i] < prefMin[i-1] {
			prefMin[i] = nums[i]
		} else {
			prefMin[i] = prefMin[i-1]
		}
	}

	suffMin[n-1], suffMax[n-1] = nums[n-1], nums[n-1]
	for i := n - 2; i >= 0; i-- {
		if nums[i] < suffMin[i+1] {
			suffMin[i] = nums[i]
		} else {
			suffMin[i] = suffMin[i+1]
		}
		if nums[i] > suffMax[i+1] {
			suffMax[i] = nums[i]
		} else {
			suffMax[i] = suffMax[i+1]
		}
	}

	ans := 0
	for i := 1; i <= n-2; i++ {
		if nums[i] > prefMax[i-1] && nums[i] < suffMin[i+1] {
			ans += 2
		} else if prefMin[i-1] < nums[i] && suffMax[i+1] > nums[i] {
			ans++
		}
	}
	return ans
}
```

## Ruby

```ruby
def sum_of_beauties(nums)
  n = nums.length
  prefix_max = Array.new(n, -Float::INFINITY)
  prefix_min = Array.new(n, Float::INFINITY)

  (1...n).each do |i|
    prefix_max[i] = [prefix_max[i - 1], nums[i - 1]].max
    prefix_min[i] = [prefix_min[i - 1], nums[i - 1]].min
  end

  suffix_max = Array.new(n, -Float::INFINITY)
  suffix_min = Array.new(n, Float::INFINITY)

  (n - 2).downto(0) do |i|
    suffix_max[i] = [suffix_max[i + 1], nums[i + 1]].max
    suffix_min[i] = [suffix_min[i + 1], nums[i + 1]].min
  end

  ans = 0
  (1..n - 2).each do |i|
    if nums[i] > prefix_max[i] && nums[i] < suffix_min[i]
      ans += 2
    elsif prefix_min[i] < nums[i] && suffix_max[i] > nums[i]
      ans += 1
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def sumOfBeauties(nums: Array[Int]): Int = {
        val n = nums.length
        val leftMax = new Array[Int](n)
        val leftMin = new Array[Int](n)

        var curMax = Int.MinValue
        var curMin = Int.MaxValue
        for (i <- 0 until n) {
            leftMax(i) = curMax
            leftMin(i) = curMin
            if (nums(i) > curMax) curMax = nums(i)
            if (nums(i) < curMin) curMin = nums(i)
        }

        val rightMin = new Array[Int](n)
        val rightMax = new Array[Int](n)

        var curRMin = Int.MaxValue
        var curRMax = Int.MinValue
        for (i <- (n - 1) to 0 by -1) {
            rightMin(i) = curRMin
            rightMax(i) = curRMax
            if (nums(i) < curRMin) curRMin = nums(i)
            if (nums(i) > curRMax) curRMax = nums(i)
        }

        var sum = 0
        for (i <- 1 until n - 1) {
            val v = nums(i)
            if (v > leftMax(i) && v < rightMin(i)) {
                sum += 2
            } else if (leftMin(i) < v && rightMax(i) > v) {
                sum += 1
            }
        }
        sum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_of_beauties(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n < 3 {
            return 0;
        }

        // Prefix max and min up to each index
        let mut prefix_max = vec![0i32; n];
        let mut prefix_min = vec![0i32; n];
        let mut cur_max = nums[0];
        let mut cur_min = nums[0];
        for i in 0..n {
            if nums[i] > cur_max { cur_max = nums[i]; }
            if nums[i] < cur_min { cur_min = nums[i]; }
            prefix_max[i] = cur_max;
            prefix_min[i] = cur_min;
        }

        // Suffix max and min from each index to end
        let mut suffix_max = vec![0i32; n];
        let mut suffix_min = vec![0i32; n];
        cur_max = nums[n - 1];
        cur_min = nums[n - 1];
        for i in (0..n).rev() {
            if nums[i] > cur_max { cur_max = nums[i]; }
            if nums[i] < cur_min { cur_min = nums[i]; }
            suffix_max[i] = cur_max;
            suffix_min[i] = cur_min;
        }

        let mut sum = 0i32;
        for i in 1..n - 1 {
            // left side: indices [0, i-1]
            // right side: indices [i+1, n-1]
            if nums[i] > prefix_max[i - 1] && nums[i] < suffix_min[i + 1] {
                sum += 2;
            } else if prefix_min[i - 1] < nums[i] && suffix_max[i + 1] > nums[i] {
                sum += 1;
            }
        }

        sum
    }
}
```

## Racket

```racket
(define/contract (sum-of-beauties nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums)))
    (if (< n 3)
        0
        (let* ((pref (make-vector n))
               (suff (make-vector n)))
          ;; prefix maximums
          (vector-set! pref 0 (vector-ref arr 0))
          (for ([i (in-range 1 n)])
            (vector-set! pref i (max (vector-ref pref (sub1 i)) (vector-ref arr i))))
          ;; suffix minimums
          (vector-set! suff (sub1 n) (vector-ref arr (sub1 n)))
          (for ([i (in-range (- n 2) -1 -1)])
            (vector-set! suff i (min (vector-ref suff (+ i 1)) (vector-ref arr i))))
          ;; compute sum of beauties
          (let loop ((i 1) (sum 0))
            (if (> i (- n 2))
                sum
                (let* ((left-max (vector-ref pref (sub1 i)))
                       (right-min (vector-ref suff (+ i 1)))
                       (val (vector-ref arr i)))
                  (cond [(and (> val left-max) (< val right-min))
                         (loop (add1 i) (+ sum 2))]
                        [(or (> val left-max) (< val right-min))
                         (loop (add1 i) (+ sum 1))]
                        [else
                         (loop (add1 i) sum)])))))))))
```

## Erlang

```erlang
-module(solution).
-export([sum_of_beauties/1]).

-spec sum_of_beauties(Nums :: [integer()]) -> integer().
sum_of_beauties(Nums) ->
    case Nums of
        [] -> 0;
        [_] -> 0;
        [_, _] -> 0;
        [First | Rest] ->
            {RightMinList, RightMaxList} = build_right(Nums),
            % skip the first element's right values (index 0)
            RightMinTail = tl(RightMinList),
            RightMaxTail = tl(RightMaxList),
            loop(Rest, RightMinTail, RightMaxTail, First, First, 0)
    end.

%% Build lists where RightMin[i] = min of elements after i,
%% RightMax[i] = max of elements after i.
-spec build_right([integer()]) -> {[integer()], [integer()]}.
build_right(Nums) ->
    Inf = 1000001,
    NegInf = -1,
    {RMinRev, RMaxRev, _CurMin, _CurMax} =
        lists:foldl(
            fun(X, {AccRMin, AccRMax, CurMin, CurMax}) ->
                NewAccRMin = [CurMin | AccRMin],
                NewAccRMax = [CurMax | AccRMax],
                {NewAccRMin,
                 NewAccRMax,
                 erlang:min(CurMin, X),
                 erlang:max(CurMax, X)}
            end,
            {[], [], Inf, NegInf},
            lists:reverse(Nums)
        ),
    RightMin = lists:reverse(RMinRev),
    RightMax = lists:reverse(RMaxRev),
    {RightMin, RightMax}.

%% Recursive loop over the array positions 1 .. N-2
-spec loop([integer()], [integer()], [integer()], integer(), integer(), integer()) -> integer().
loop(CurrList, RightMinTail, RightMaxTail, LeftMax, LeftMin, Sum) ->
    case {CurrList, RightMinTail, RightMaxTail} of
        {[Cur | RestCurr], [RightMin | RestRMin], [RightMax | RestRMax]} when RestCurr =/= [] ->
            Beauty =
                if Cur > LeftMax andalso Cur < RightMin ->
                        2;
                   (LeftMin < Cur) andalso (RightMax > Cur) ->
                        1;
                   true -> 0
                end,
            NewSum = Sum + Beauty,
            NewLeftMax = erlang:max(LeftMax, Cur),
            NewLeftMin = erlang:min(LeftMin, Cur),
            loop(RestCurr, RestRMin, RestRMax, NewLeftMax, NewLeftMin, NewSum);
        _ ->
            Sum
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_of_beauties(nums :: [integer]) :: integer
  def sum_of_beauties(nums) do
    n = length(nums)
    nums_t = List.to_tuple(nums)

    # Build suffix maximums: suffix_max[i] = max of nums[i..end]
    suffix_max_list =
      Enum.reduce(Enum.reverse(nums), [], fn x, acc ->
        new_max = if acc == [], do: x, else: max(x, hd(acc))
        [new_max | acc]
      end)

    suffix_max_t = List.to_tuple(suffix_max_list)

    {_, total} =
      Enum.reduce(1..(n - 2), {elem(nums_t, 0), 0}, fn idx, {min_left, sum} ->
        val = elem(nums_t, idx)
        cond1 = if val > min_left, do: 1, else: 0
        max_right = elem(suffix_max_t, idx + 1)
        cond2 = if val < max_right, do: 1, else: 0
        {min(min_left, val), sum + cond1 + cond2}
      end)

    total
  end
end
```
