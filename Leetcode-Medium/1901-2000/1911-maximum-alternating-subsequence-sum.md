# 1911. Maximum Alternating Subsequence Sum

## Cpp

```cpp
class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        const long long INF_NEG = LLONG_MIN / 4;
        long long even = 0;          // max sum ending at an even position (plus sign)
        long long odd = INF_NEG;     // max sum ending at an odd position (minus sign)

        for (int x : nums) {
            long long newEven = max({even, odd + x, (long long)x});
            long long newOdd  = max(odd, even - x);
            even = newEven;
            odd = newOdd;
        }
        return even;
    }
};
```

## Java

```java
class Solution {
    public long maxAlternatingSum(int[] nums) {
        long even = 0;
        long odd = Long.MIN_VALUE / 4;
        for (int x : nums) {
            long newEven = Math.max(even, odd + x);
            long newOdd = Math.max(odd, even - x);
            even = newEven;
            odd = newOdd;
        }
        return even;
    }
}
```

## Python

```python
class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0  # max sum where next element will be added (even position)
        odd = 0   # max sum where next element will be subtracted (odd position)
        for x in nums:
            new_even = max(even, odd + x)
            new_odd = max(odd, even - x)
            even, odd = new_even, new_odd
        return even
```

## Python3

```python
from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even = 0
        odd = -10**15
        for x in nums:
            new_even = max(even, odd + x, x)
            new_odd = max(odd, even - x)
            even, odd = new_even, new_odd
        return even
```

## C

```c
long long maxAlternatingSum(int* nums, int numsSize){
    if (numsSize == 0) return 0;
    long long even = nums[0]; // subsequence ending with a positive sign
    long long odd = 0;        // subsequence ending with a negative sign (or empty)
    for (int i = 1; i < numsSize; ++i){
        long long x = nums[i];
        long long newEven = even > odd + x ? even : odd + x;
        long long newOdd  = odd  > even - x ? odd  : even - x;
        even = newEven;
        odd = newOdd;
    }
    return even;
}
```

## Csharp

```csharp
public class Solution {
    public long MaxAlternatingSum(int[] nums) {
        long even = 0; // max sum when we have taken an even number of elements
        long odd = long.MinValue / 2; // max sum when we have taken an odd number of elements
        foreach (int x in nums) {
            long newEven = Math.Max(even, odd - x);
            long newOdd = Math.Max(odd, even + x);
            even = newEven;
            odd = newOdd;
        }
        return Math.Max(even, odd);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAlternatingSum = function(nums) {
    let even = 0; // max sum ending at an even index in the subsequence
    let odd = Number.NEGATIVE_INFINITY; // max sum ending at an odd index
    
    for (const x of nums) {
        const newEven = Math.max(even, odd + x);
        const newOdd = Math.max(odd, even - x);
        even = newEven;
        odd = newOdd;
    }
    
    return even;
};
```

## Typescript

```typescript
function maxAlternatingSum(nums: number[]): number {
    let even = 0;
    let odd = Number.NEGATIVE_INFINITY;

    for (const x of nums) {
        const newEven = Math.max(even, odd + x, x);
        const newOdd = Math.max(odd, even - x);
        even = newEven;
        odd = newOdd;
    }

    return even;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxAlternatingSum($nums) {
        $even = 0;
        $odd = PHP_INT_MIN;
        foreach ($nums as $num) {
            $newEven = max($even, $odd + $num);
            $newOdd = max($odd, $even - $num);
            $even = $newEven;
            $odd = $newOdd;
        }
        return $even;
    }
}
```

## Swift

```swift
class Solution {
    func maxAlternatingSum(_ nums: [Int]) -> Int {
        var even = 0
        let negInf = Int.min / 2
        var odd = negInf
        
        for x in nums {
            let prevEven = even
            let prevOdd = odd
            
            // Update even (subsequence ending with a positive contribution)
            let candidateEven = max(max(prevEven, prevOdd + x), x)
            even = candidateEven
            
            // Update odd (subsequence ending with a negative contribution)
            odd = max(prevOdd, prevEven - x)
        }
        
        return even
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxAlternatingSum(nums: IntArray): Long {
        var even = nums[0].toLong()
        var odd = Long.MIN_VALUE / 2
        for (i in 1 until nums.size) {
            val x = nums[i].toLong()
            val newEven = kotlin.math.max(even, odd + x)
            val newOdd = kotlin.math.max(odd, even - x)
            even = newEven
            odd = newOdd
        }
        return even
    }
}
```

## Golang

```go
func maxAlternatingSum(nums []int) int64 {
	var bestEven int64 // max sum where the last taken element is added
	var bestOdd int64  // max sum where the last taken element is subtracted

	for _, v := range nums {
		x := int64(v)
		newBestEven := bestEven
		if cand := bestOdd + x; cand > newBestEven {
			newBestEven = cand
		}
		newBestOdd := bestOdd
		if cand := bestEven - x; cand > newBestOdd {
			newBestOdd = cand
		}
		bestEven, bestOdd = newBestEven, newBestOdd
	}
	return bestEven
}
```

## Ruby

```ruby
def max_alternating_sum(nums)
  even = 0
  odd = -(1 << 60)
  nums.each do |x|
    new_odd = [odd, even + x].max
    new_even = [even, odd - x].max
    odd = new_odd
    even = new_even
  end
  odd
end
```

## Scala

```scala
object Solution {
    def maxAlternatingSum(nums: Array[Int]): Long = {
        var even: Long = 0L
        var odd: Long = Long.MinValue / 4
        for (xInt <- nums) {
            val x = xInt.toLong
            val newEven = math.max(even, odd + x)
            val newOdd = math.max(odd, even - x)
            even = newEven
            odd = newOdd
        }
        even
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_alternating_sum(nums: Vec<i32>) -> i64 {
        let mut even: i64 = 0;
        let mut odd: i64 = i64::MIN / 2; // effectively -infinity
        for &v in nums.iter() {
            let x = v as i64;
            let new_odd = std::cmp::max(odd, even + x);
            let new_even = std::cmp::max(even, odd - x);
            odd = new_odd;
            even = new_even;
        }
        odd
    }
}
```

## Racket

```racket
(define/contract (max-alternating-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (even 0) (odd -1000000000000))
    (if (null? lst)
        odd
        (let* ((x (car lst))
               (new-odd (max odd (+ even x)))
               (new-even (max even (- odd x))))
          (loop (cdr lst) new-even new-odd)))))
```
