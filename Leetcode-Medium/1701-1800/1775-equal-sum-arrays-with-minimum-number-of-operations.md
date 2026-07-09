# 1775. Equal Sum Arrays With Minimum Number of Operations

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums1, vector<int>& nums2) {
        long long sum1 = 0, sum2 = 0;
        for (int v : nums1) sum1 += v;
        for (int v : nums2) sum2 += v;
        if (sum1 == sum2) return 0;
        // Ensure sum1 < sum2
        if (sum1 > sum2) {
            swap(nums1, nums2);
            swap(sum1, sum2);
        }
        int diff = static_cast<int>(sum2 - sum1); // diff > 0 and fits in int (max 5*1e5)
        vector<int> cnt(6, 0); // index is possible gain (1..5)
        for (int v : nums1) {
            int g = 6 - v;
            if (g > 0) cnt[g]++;
        }
        for (int v : nums2) {
            int g = v - 1;
            if (g > 0) cnt[g]++;
        }
        int ops = 0;
        for (int gain = 5; gain >= 1 && diff > 0; --gain) {
            while (cnt[gain] > 0 && diff > 0) {
                int need = (diff + gain - 1) / gain; // operations needed with this gain
                int use = min(cnt[gain], need);
                ops += use;
                diff -= use * gain;
                cnt[gain] -= use;
            }
        }
        return diff > 0 ? -1 : ops;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums1, int[] nums2) {
        long sum1 = 0, sum2 = 0;
        for (int v : nums1) sum1 += v;
        for (int v : nums2) sum2 += v;
        if (sum1 == sum2) return 0;

        // Ensure sum1 is the smaller sum
        if (sum1 > sum2) {
            int[] tmp = nums1; nums1 = nums2; nums2 = tmp;
            long t = sum1; sum1 = sum2; sum2 = t;
        }

        int diff = (int) (sum2 - sum1); // positive difference to eliminate
        int[] cnt = new int[6]; // cnt[gain] for gain 1..5

        for (int v : nums1) {
            int gain = 6 - v;          // possible increase
            if (gain > 0) cnt[gain]++;
        }
        for (int v : nums2) {
            int gain = v - 1;          // possible decrease
            if (gain > 0) cnt[gain]++;
        }

        int ops = 0;
        for (int gain = 5; gain >= 1 && diff > 0; gain--) {
            while (cnt[gain] > 0 && diff > 0) {
                diff -= gain;
                cnt[gain]--;
                ops++;
            }
        }
        return diff <= 0 ? ops : -1;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        # ensure s1 < s2
        if s1 > s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
        diff = s2 - s1  # positive
        
        # count possible gains from 1 to 5
        cnt = [0] * 6  # index is gain value
        for v in nums1:
            g = 6 - v
            if g > 0:
                cnt[g] += 1
        for v in nums2:
            g = v - 1
            if g > 0:
                cnt[g] += 1
        
        ops = 0
        # apply largest gains first
        for gain in range(5, 0, -1):
            if diff <= 0:
                break
            if cnt[gain] == 0:
                continue
            max_use = (diff + gain - 1) // gain  # minimal ops needed with this gain
            use = min(cnt[gain], max_use)
            diff -= use * gain
            ops += use
        
        return ops if diff <= 0 else -1
```

## Python3

```python
from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        # make s1 the smaller sum
        if s1 > s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
        diff = s2 - s1  # positive
        
        cnt = [0] * 6  # indices 0..5, we use 1..5
        for v in nums1:
            inc = 6 - v
            if inc > 0:
                cnt[inc] += 1
        for v in nums2:
            dec = v - 1
            if dec > 0:
                cnt[dec] += 1
        
        total_possible = sum(g * cnt[g] for g in range(1, 6))
        if total_possible < diff:
            return -1
        
        ops = 0
        for gain in range(5, 0, -1):
            if diff <= 0:
                break
            if cnt[gain] == 0:
                continue
            need = (diff + gain - 1) // gain  # minimal operations of this gain needed
            use = min(cnt[gain], need)
            diff -= use * gain
            ops += use
        
        return ops
```

## C

```c
int minOperations(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int sum1 = 0, sum2 = 0;
    for (int i = 0; i < nums1Size; ++i) sum1 += nums1[i];
    for (int i = 0; i < nums2Size; ++i) sum2 += nums2[i];
    
    if (sum1 == sum2) return 0;
    
    int diff;
    int cnt[6] = {0}; // indices 1..5 store frequencies of possible gain values
    
    if (sum1 < sum2) {
        diff = sum2 - sum1;
        for (int i = 0; i < nums1Size; ++i) {
            int g = 6 - nums1[i];
            if (g > 0) cnt[g]++;
        }
        for (int i = 0; i < nums2Size; ++i) {
            int g = nums2[i] - 1;
            if (g > 0) cnt[g]++;
        }
    } else { // sum2 < sum1
        diff = sum1 - sum2;
        for (int i = 0; i < nums2Size; ++i) {
            int g = 6 - nums2[i];
            if (g > 0) cnt[g]++;
        }
        for (int i = 0; i < nums1Size; ++i) {
            int g = nums1[i] - 1;
            if (g > 0) cnt[g]++;
        }
    }
    
    int ops = 0;
    for (int gain = 5; gain >= 1 && diff > 0; --gain) {
        while (cnt[gain] > 0 && diff > 0) {
            diff -= gain;
            cnt[gain]--;
            ++ops;
        }
    }
    
    return diff > 0 ? -1 : ops;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int[] nums1, int[] nums2) {
        long sum1 = 0, sum2 = 0;
        foreach (int v in nums1) sum1 += v;
        foreach (int v in nums2) sum2 += v;

        if (sum1 == sum2) return 0;

        // Ensure sum1 is the smaller one
        if (sum1 > sum2) {
            var tmpArr = nums1; nums1 = nums2; nums2 = tmpArr;
            var tmpSum = sum1; sum1 = sum2; sum2 = tmpSum;
        }

        int[] gainCount = new int[6]; // indices 0..5, we use 1..5

        foreach (int v in nums1) {
            int gain = 6 - v;          // possible increase
            if (gain > 0) gainCount[gain]++;
        }
        foreach (int v in nums2) {
            int gain = v - 1;          // possible decrease
            if (gain > 0) gainCount[gain]++;
        }

        long diff = sum2 - sum1;
        int operations = 0;

        for (int g = 5; g >= 1 && diff > 0; g--) {
            if (gainCount[g] == 0) continue;
            long needOps = (diff + g - 1) / g; // ceil(diff/g)
            long use = Math.Min(gainCount[g], needOps);
            diff -= use * g;
            operations += (int)use;
        }

        return diff > 0 ? -1 : operations;
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
var minOperations = function(nums1, nums2) {
    let sum1 = 0, sum2 = 0;
    for (const v of nums1) sum1 += v;
    for (const v of nums2) sum2 += v;
    if (sum1 === sum2) return 0;

    // Ensure sum1 < sum2
    if (sum1 > sum2) {
        [nums1, nums2] = [nums2, nums1];
        [sum1, sum2] = [sum2, sum1];
    }

    let diff = sum2 - sum1; // positive
    const cnt = new Array(6).fill(0); // indices 0..5, we use 1..5

    for (const v of nums1) {
        const gain = 6 - v;
        if (gain > 0) cnt[gain]++;
    }
    for (const v of nums2) {
        const gain = v - 1;
        if (gain > 0) cnt[gain]++;
    }

    let ops = 0;
    for (let g = 5; g >= 1 && diff > 0; g--) {
        if (cnt[g] === 0) continue;
        const need = Math.ceil(diff / g);
        const take = Math.min(cnt[g], need);
        ops += take;
        diff -= take * g;
    }

    return diff > 0 ? -1 : ops;
};
```

## Typescript

```typescript
function minOperations(nums1: number[], nums2: number[]): number {
    let sum1 = 0, sum2 = 0;
    for (const v of nums1) sum1 += v;
    for (const v of nums2) sum2 += v;
    if (sum1 === sum2) return 0;

    // Ensure sum1 < sum2
    if (sum1 > sum2) {
        [nums1, nums2] = [nums2, nums1];
        [sum1, sum2] = [sum2, sum1];
    }

    let diff = sum2 - sum1; // positive
    const cnt = new Array(6).fill(0); // indices 0..5, we use 1..5

    for (const v of nums1) {
        const inc = 6 - v;
        if (inc > 0) cnt[inc]++;
    }
    for (const v of nums2) {
        const dec = v - 1;
        if (dec > 0) cnt[dec]++;
    }

    let ops = 0;
    for (let gain = 5; gain >= 1 && diff > 0; gain--) {
        if (cnt[gain] === 0) continue;
        const need = Math.ceil(diff / gain);
        const use = Math.min(cnt[gain], need);
        diff -= use * gain;
        ops += use;
    }

    return diff <= 0 ? ops : -1;
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
    function minOperations($nums1, $nums2) {
        $sum1 = array_sum($nums1);
        $sum2 = array_sum($nums2);
        if ($sum1 == $sum2) {
            return 0;
        }
        // Ensure sum1 <= sum2
        if ($sum1 > $sum2) {
            $tmp = $nums1; $nums1 = $nums2; $nums2 = $tmp;
            $tmpSum = $sum1; $sum1 = $sum2; $sum2 = $tmpSum;
        }
        $diff = $sum2 - $sum1; // positive

        // Count possible gains (1..5)
        $cnt = array_fill(0, 6, 0); // index by gain
        foreach ($nums1 as $v) {
            $gain = 6 - $v;
            if ($gain > 0) {
                $cnt[$gain]++;
            }
        }
        foreach ($nums2 as $v) {
            $gain = $v - 1;
            if ($gain > 0) {
                $cnt[$gain]++;
            }
        }

        $ops = 0;
        for ($g = 5; $g >= 1 && $diff > 0; $g--) {
            if ($cnt[$g] == 0) continue;
            // Minimum operations needed with this gain
            $need = intdiv($diff + $g - 1, $g); // ceil(diff / g)
            $use = min($cnt[$g], $need);
            $diff -= $use * $g;
            $ops += $use;
        }

        return $diff > 0 ? -1 : $ops;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var sum1 = nums1.reduce(0, +)
        var sum2 = nums2.reduce(0, +)
        if sum1 == sum2 { return 0 }
        
        // Ensure sum1 is the smaller sum
        var a = nums1
        var b = nums2
        if sum1 > sum2 {
            swap(&sum1, &sum2)
            swap(&a, &b)
        }
        
        let diff = sum2 - sum1
        var counts = [Int](repeating: 0, count: 6) // indices 0..5, we use 1..5
        
        for v in a {               // can increase values up to 6
            let inc = 6 - v
            if inc > 0 {
                counts[inc] += 1
            }
        }
        for v in b {               // can decrease values down to 1
            let dec = v - 1
            if dec > 0 {
                counts[dec] += 1
            }
        }
        
        var totalPossible = 0
        for gain in 1...5 {
            totalPossible += gain * counts[gain]
        }
        if totalPossible < diff { return -1 }
        
        var remaining = diff
        var ops = 0
        var gain = 5
        while remaining > 0 && gain >= 1 {
            let cnt = counts[gain]
            if cnt > 0 {
                let need = (remaining + gain - 1) / gain   // ceil division
                if cnt >= need {
                    ops += need
                    remaining = 0
                    break
                } else {
                    ops += cnt
                    remaining -= cnt * gain
                }
            }
            gain -= 1
        }
        return ops
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(nums1: IntArray, nums2: IntArray): Int {
        var sum1 = nums1.sum()
        var sum2 = nums2.sum()
        if (sum1 == sum2) return 0

        // Ensure sum1 is the smaller sum
        var small = nums1
        var large = nums2
        var sSmall = sum1
        var sLarge = sum2
        if (sSmall > sLarge) {
            small = nums2
            large = nums1
            sSmall = sum2
            sLarge = sum1
        }

        var diff = sLarge - sSmall // positive

        val freq = IntArray(6) // index 0..5, we use 1..5
        for (v in small) {
            val inc = 6 - v
            if (inc > 0) freq[inc]++
        }
        for (v in large) {
            val dec = v - 1
            if (dec > 0) freq[dec]++
        }

        var totalGain = 0L
        for (g in 1..5) {
            totalGain += g.toLong() * freq[g]
        }
        if (totalGain < diff) return -1

        var ops = 0
        var gain = 5
        while (gain >= 1 && diff > 0) {
            val cnt = freq[gain]
            if (cnt > 0) {
                val need = (diff + gain - 1) / gain
                if (need <= cnt) {
                    ops += need
                    diff = 0
                    break
                } else {
                    ops += cnt
                    diff -= cnt * gain
                }
            }
            gain--
        }
        return ops
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums1, List<int> nums2) {
    int sum1 = 0;
    for (int v in nums1) sum1 += v;
    int sum2 = 0;
    for (int v in nums2) sum2 += v;

    if (sum1 == sum2) return 0;

    // Ensure sum1 is the smaller sum
    if (sum1 > sum2) {
      var tmpList = nums1;
      nums1 = nums2;
      nums2 = tmpList;
      int tmpSum = sum1;
      sum1 = sum2;
      sum2 = tmpSum;
    }

    int diff = sum2 - sum1; // positive
    List<int> cnt = List.filled(6, 0); // indices 0..5, we use 1..5

    for (int v in nums1) {
      int gain = 6 - v;
      if (gain > 0) cnt[gain] += 1;
    }
    for (int v in nums2) {
      int gain = v - 1;
      if (gain > 0) cnt[gain] += 1;
    }

    int ops = 0;
    for (int g = 5; g >= 1 && diff > 0; g--) {
      while (cnt[g] > 0 && diff > 0) {
        diff -= g;
        cnt[g]--;
        ops++;
      }
    }

    return diff <= 0 ? ops : -1;
  }
}
```

## Golang

```go
func minOperations(nums1 []int, nums2 []int) int {
	sum1, sum2 := 0, 0
	for _, v := range nums1 {
		sum1 += v
	}
	for _, v := range nums2 {
		sum2 += v
	}
	if sum1 == sum2 {
		return 0
	}

	cnt := make([]int, 6) // indices 0..5, we use 1..5
	diff := 0

	if sum1 < sum2 {
		// need to increase nums1 or decrease nums2
		for _, v := range nums1 {
			if inc := 6 - v; inc > 0 {
				cnt[inc]++
			}
		}
		for _, v := range nums2 {
			if dec := v - 1; dec > 0 {
				cnt[dec]++
			}
		}
		diff = sum2 - sum1
	} else {
		// need to increase nums2 or decrease nums1
		for _, v := range nums2 {
			if inc := 6 - v; inc > 0 {
				cnt[inc]++
			}
		}
		for _, v := range nums1 {
			if dec := v - 1; dec > 0 {
				cnt[dec]++
			}
		}
		diff = sum1 - sum2
	}

	totalGain := 0
	for g := 1; g <= 5; g++ {
		totalGain += g * cnt[g]
	}
	if totalGain < diff {
		return -1
	}

	ops := 0
	remaining := diff
	for gain := 5; gain >= 1 && remaining > 0; gain-- {
		if cnt[gain] == 0 {
			continue
		}
		need := (remaining + gain - 1) / gain // ceil division
		use := cnt[gain]
		if need < use {
			use = need
		}
		ops += use
		remaining -= use * gain
	}
	return ops
}
```

## Ruby

```ruby
def min_operations(nums1, nums2)
  sum1 = nums1.sum
  sum2 = nums2.sum
  return 0 if sum1 == sum2

  # Ensure sum1 <= sum2
  if sum1 > sum2
    nums1, nums2 = nums2, nums1
    sum1, sum2 = sum2, sum1
  end

  diff = sum2 - sum1
  cnt = Array.new(6, 0) # indices 0..5, we use only 1..5

  nums1.each do |v|
    inc = 6 - v
    cnt[inc] += 1 if inc > 0
  end

  nums2.each do |v|
    dec = v - 1
    cnt[dec] += 1 if dec > 0
  end

  total_gain = 0
  (1..5).each { |g| total_gain += cnt[g] * g }
  return -1 if total_gain < diff

  ops = 0
  g = 5
  while diff > 0 && g >= 1
    if cnt[g] > 0
      need = (diff + g - 1) / g
      use = [cnt[g], need].min
      ops += use
      diff -= use * g
    end
    g -= 1
  end

  ops
end
```

## Scala

```scala
object Solution {
    def minOperations(nums1: Array[Int], nums2: Array[Int]): Int = {
        var sum1 = nums1.sum
        var sum2 = nums2.sum
        if (sum1 == sum2) return 0

        // Ensure sum1 <= sum2, otherwise swap
        var a = nums1
        var b = nums2
        var sA = sum1
        var sB = sum2
        if (sA > sB) {
            a = nums2
            b = nums1
            sA = sum2
            sB = sum1
        }

        val diff = sB - sA // positive needed increase/decrease
        val freq = new Array[Int](6) // indices 0..5, we use 1..5
        var maxGain = 0

        for (v <- a) {
            val g = 6 - v
            if (g > 0) {
                freq(g) += 1
                maxGain += g
            }
        }

        for (v <- b) {
            val g = v - 1
            if (g > 0) {
                freq(g) += 1
                maxGain += g
            }
        }

        if (maxGain < diff) return -1

        var remaining = diff
        var ops = 0
        var gain = 5
        while (remaining > 0 && gain > 0) {
            val cnt = freq(gain)
            if (cnt > 0) {
                val need = (remaining + gain - 1) / gain // ceil division
                if (need <= cnt) {
                    ops += need
                    remaining = 0
                } else {
                    ops += cnt
                    remaining -= cnt * gain
                }
            }
            gain -= 1
        }

        ops
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut sum1: i32 = nums1.iter().sum();
        let mut sum2: i32 = nums2.iter().sum();

        if sum1 == sum2 {
            return 0;
        }

        // Ensure sum1 <= sum2, swapping vectors if needed
        let (mut a, mut b) = (nums1, nums2);
        if sum1 > sum2 {
            std::mem::swap(&mut a, &mut b);
            std::mem::swap(&mut sum1, &mut sum2);
        }

        let diff = sum2 - sum1; // positive difference to eliminate

        // freq[g] = number of operations that can change the total by exactly g (1..5)
        let mut freq = [0i32; 6];

        for &v in a.iter() {
            let inc = 6 - v;
            if inc > 0 {
                freq[inc as usize] += 1;
            }
        }

        for &v in b.iter() {
            let dec = v - 1;
            if dec > 0 {
                freq[dec as usize] += 1;
            }
        }

        // Check feasibility
        let mut total_gain: i32 = 0;
        for g in 1..=5 {
            total_gain += g as i32 * freq[g];
        }
        if total_gain < diff {
            return -1;
        }

        // Greedy use largest gains first
        let mut ops: i32 = 0;
        let mut remaining = diff;

        for g in (1..=5).rev() {
            let cnt = freq[g];
            if cnt == 0 {
                continue;
            }
            let max_change = g as i32 * cnt;
            if max_change >= remaining {
                ops += (remaining + g as i32 - 1) / g as i32;
                return ops;
            } else {
                ops += cnt;
                remaining -= max_change;
            }
        }

        -1
    }
}
```

## Racket

```racket
#lang racket

(provide min-operations)

(define/contract (min-operations nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((s1 (foldl + 0 nums1))
         (s2 (foldl + 0 nums2)))
    (cond
      [(= s1 s2) 0]
      [else
       (define diff (if (< s1 s2) (- s2 s1) (- s1 s2)))
       (define gains (make-vector 6 0)) ; indices 0..5, we use 1..5

       (define (add-gain v inc?)
         (let ((gain (if inc? (- 6 v) (- v 1))))
           (when (> gain 0)
             (vector-set! gains gain (+ (vector-ref gains gain) 1)))))

       (if (< s1 s2)
           (begin
             (for ([v nums1]) (add-gain v #t))
             (for ([v nums2]) (add-gain v #f)))
           (begin
             (for ([v nums2]) (add-gain v #t))
             (for ([v nums1]) (add-gain v #f))))

       ;; total possible gain
       (define total
         (let loop ((g 5) (acc 0))
           (if (< g 1)
               acc
               (loop (- g 1) (+ acc (* g (vector-ref gains g)))))))

       (if (< total diff)
           -1
           (let loop ((g 5) (rem diff) (ops 0))
             (cond [(<= rem 0) ops]
                   [(< g 1) -1] ; should not happen because of the check above
                   [else
                    (define cnt (vector-ref gains g))
                    (if (= cnt 0)
                        (loop (- g 1) rem ops)
                        (let* ((need (quotient (+ rem (- g 1)) g)) ; ceil(rem / g)
                               (use (if (< need cnt) need cnt)))
                          (loop (- g 1) (- rem (* use g)) (+ ops use))))])))])))
```

## Erlang

```erlang
-spec min_operations(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
min_operations(Nums1, Nums2) ->
    Sum1 = lists:foldl(fun(X, Acc) -> Acc + X end, 0, Nums1),
    Sum2 = lists:foldl(fun(X, Acc) -> Acc + X end, 0, Nums2),
    case Sum1 == Sum2 of
        true -> 0;
        false when Sum1 < Sum2 ->
            diff_counts(Sum1, Sum2, Nums1, Nums2);
        false ->
            min_operations(Nums2, Nums1)
    end.

diff_counts(SmallSum, LargeSum, SmallList, LargeList) ->
    Diff = LargeSum - SmallSum,
    Counts0 = {0, 0, 0, 0, 0},
    Counts1 = lists:foldl(fun(Val, Acc) -> inc_count(6 - Val, Acc) end, Counts0, SmallList),
    Counts = lists:foldl(fun(Val, Acc) -> inc_count(Val - 1, Acc) end, Counts1, LargeList),
    Gains = [{5, element(1, Counts)},
             {4, element(2, Counts)},
             {3, element(3, Counts)},
             {2, element(4, Counts)},
             {1, element(5, Counts)}],
    case greedy(Diff, Gains, 0) of
        {0, Ops} -> Ops;
        {_Rem, _Ops} -> -1
    end.

inc_count(Gain, {C5, C4, C3, C2, C1}) ->
    case Gain of
        5 -> {C5 + 1, C4, C3, C2, C1};
        4 -> {C5, C4 + 1, C3, C2, C1};
        3 -> {C5, C4, C3 + 1, C2, C1};
        2 -> {C5, C4, C3, C2 + 1, C1};
        1 -> {C5, C4, C3, C2, C1 + 1};
        _ -> {C5, C4, C3, C2, C1}
    end.

greedy(Diff, [], Ops) ->
    {Diff, Ops};
greedy(Diff, [{Gain, Count} | Rest], Ops) when Diff =< 0 ->
    {0, Ops};
greedy(Diff, [{Gain, Count} | Rest], Ops) ->
    case Count of
        0 -> greedy(Diff, Rest, Ops);
        _ ->
            MaxReduce = Gain * Count,
            if MaxReduce >= Diff ->
                    Needed = (Diff + Gain - 1) div Gain,
                    {0, Ops + Needed};
               true ->
                    NewDiff = Diff - MaxReduce,
                    greedy(NewDiff, Rest, Ops + Count)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums1 :: [integer], nums2 :: [integer]) :: integer
  def min_operations(nums1, nums2) do
    sum1 = Enum.sum(nums1)
    sum2 = Enum.sum(nums2)

    cond do
      sum1 == sum2 ->
        0

      sum1 > sum2 ->
        # ensure sum1 <= sum2 by swapping the arrays
        min_operations(nums2, nums1)

      true ->
        diff = sum2 - sum1

        gains =
          nums1
          |> Enum.map(fn v -> 6 - v end)
          |> Enum.filter(&(&1 > 0))
          ++
          nums2
          |> Enum.map(fn v -> v - 1 end)
          |> Enum.filter(&(&1 > 0))

        sorted = Enum.sort(gains, &>=/2)

        {ops, remaining} =
          Enum.reduce(sorted, {0, diff}, fn gain, {cnt, left} ->
            if left <= 0 do
              {cnt, left}
            else
              {cnt + 1, left - gain}
            end
          end)

        if remaining <= 0, do: ops, else: -1
    end
  end
end
```
