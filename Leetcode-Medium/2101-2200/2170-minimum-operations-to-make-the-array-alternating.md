# 2170. Minimum Operations to Make the Array Alternating

## Cpp

```cpp
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        
        unordered_map<int,int> evenCnt, oddCnt;
        for (int i = 0; i < n; ++i) {
            if ((i & 1) == 0)
                ++evenCnt[nums[i]];
            else
                ++oddCnt[nums[i]];
        }
        
        // top two in even positions
        int ev1Val = -1, ev1Cnt = 0, ev2Val = -1, ev2Cnt = 0;
        for (auto &p : evenCnt) {
            if (p.second > ev1Cnt) {
                ev2Cnt = ev1Cnt; ev2Val = ev1Val;
                ev1Cnt = p.second; ev1Val = p.first;
            } else if (p.second > ev2Cnt) {
                ev2Cnt = p.second; ev2Val = p.first;
            }
        }
        // top two in odd positions
        int od1Val = -1, od1Cnt = 0, od2Val = -1, od2Cnt = 0;
        for (auto &p : oddCnt) {
            if (p.second > od1Cnt) {
                od2Cnt = od1Cnt; od2Val = od1Val;
                od1Cnt = p.second; od1Val = p.first;
            } else if (p.second > od2Cnt) {
                od2Cnt = p.second; od2Val = p.first;
            }
        }
        
        if (ev1Val != od1Val) {
            return n - (ev1Cnt + od1Cnt);
        } else {
            int keepUsingOddSecond = ev1Cnt + od2Cnt;
            int keepUsingEvenSecond = ev2Cnt + od1Cnt;
            int maxKeep = max(keepUsingOddSecond, keepUsingEvenSecond);
            return n - maxKeep;
        }
    }
};
```

## Java

```java
class Solution {
    public int minimumOperations(int[] nums) {
        int n = nums.length;
        java.util.HashMap<Integer, Integer> evenCount = new java.util.HashMap<>();
        java.util.HashMap<Integer, Integer> oddCount = new java.util.HashMap<>();

        for (int i = 0; i < n; i++) {
            if ((i & 1) == 0) {
                evenCount.put(nums[i], evenCount.getOrDefault(nums[i], 0) + 1);
            } else {
                oddCount.put(nums[i], oddCount.getOrDefault(nums[i], 0) + 1);
            }
        }

        // Find top two frequencies for even indices
        int evenFirstVal = -1, evenFirstFreq = 0, evenSecondFreq = 0;
        for (java.util.Map.Entry<Integer, Integer> e : evenCount.entrySet()) {
            int val = e.getKey();
            int freq = e.getValue();
            if (freq > evenFirstFreq) {
                evenSecondFreq = evenFirstFreq;
                evenFirstVal = val;
                evenFirstFreq = freq;
            } else if (freq > evenSecondFreq) {
                evenSecondFreq = freq;
            }
        }

        // Find top two frequencies for odd indices
        int oddFirstVal = -1, oddFirstFreq = 0, oddSecondFreq = 0;
        for (java.util.Map.Entry<Integer, Integer> e : oddCount.entrySet()) {
            int val = e.getKey();
            int freq = e.getValue();
            if (freq > oddFirstFreq) {
                oddSecondFreq = oddFirstFreq;
                oddFirstVal = val;
                oddFirstFreq = freq;
            } else if (freq > oddSecondFreq) {
                oddSecondFreq = freq;
            }
        }

        // If the most frequent values are different, keep both
        if (evenFirstVal != oddFirstVal) {
            return n - (evenFirstFreq + oddFirstFreq);
        }

        // Otherwise choose the best alternative combination
        int keepUsingEvenFirstOddSecond = evenFirstFreq + oddSecondFreq;
        int keepUsingEvenSecondOddFirst = evenSecondFreq + oddFirstFreq;
        int maxKeep = Math.max(keepUsingEvenFirstOddSecond, keepUsingEvenSecondOddFirst);
        return n - maxKeep;
    }
}
```

## Python

```python
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        even_cnt = Counter()
        odd_cnt = Counter()
        for i, v in enumerate(nums):
            if i % 2 == 0:
                even_cnt[v] += 1
            else:
                odd_cnt[v] += 1

        # get top two (freq, value) for each parity
        def top_two(counter):
            most = counter.most_common(2)
            if not most:
                return [(0, None), (0, None)]
            if len(most) == 1:
                return [most[0], (0, None)]
            return most

        even_top = top_two(even_cnt)
        odd_top = top_two(odd_cnt)

        # unpack
        even_max_val, even_max_freq = even_top[0][0], even_top[0][1]
        even_sec_val, even_sec_freq = even_top[1][0], even_top[1][1]

        odd_max_val, odd_max_freq = odd_top[0][0], odd_top[0][1]
        odd_sec_val, odd_sec_freq = odd_top[1][0], odd_top[1][1]

        n = len(nums)
        if even_max_val != odd_max_val:
            # can keep both most frequent values
            return n - (even_max_val + odd_max_val)
        else:
            # need to choose alternative combination
            keep1 = even_max_val + odd_sec_val  # use even's best, odd's second
            keep2 = even_sec_val + odd_max_val  # use odd's best, even's second
            max_keep = max(keep1, keep2)
            return n - max_keep
```

## Python3

```python
from collections import Counter
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        even_counts = Counter()
        odd_counts = Counter()
        for i, v in enumerate(nums):
            if i % 2 == 0:
                even_counts[v] += 1
            else:
                odd_counts[v] += 1

        ev = even_counts.most_common(2)
        od = odd_counts.most_common(2)

        even_top_val, even_top_cnt = ev[0] if ev else (None, 0)
        even_second_cnt = ev[1][1] if len(ev) > 1 else 0

        odd_top_val, odd_top_cnt = od[0] if od else (None, 0)
        odd_second_cnt = od[1][1] if len(od) > 1 else 0

        if even_top_val != odd_top_val:
            return n - even_top_cnt - odd_top_cnt

        keep1 = even_top_cnt + odd_second_cnt
        keep2 = even_second_cnt + odd_top_cnt
        max_keep = max(keep1, keep2)
        return n - max_keep
```

## C

```c
#include <stdlib.h>

int minimumOperations(int* nums, int numsSize) {
    const int MAX_VAL = 100000;
    int *evenCnt = (int *)calloc(MAX_VAL + 1, sizeof(int));
    int *oddCnt  = (int *)calloc(MAX_VAL + 1, sizeof(int));

    for (int i = 0; i < numsSize; ++i) {
        if ((i & 1) == 0)
            evenCnt[nums[i]]++;
        else
            oddCnt[nums[i]]++;
    }

    int evenTop1Val = -1, evenTop2Val = -1;
    int evenTop1Cnt = 0, evenTop2Cnt = 0;
    int oddTop1Val = -1, oddTop2Val = -1;
    int oddTop1Cnt = 0, oddTop2Cnt = 0;

    for (int v = 1; v <= MAX_VAL; ++v) {
        if (evenCnt[v] > evenTop1Cnt) {
            evenTop2Cnt = evenTop1Cnt;
            evenTop2Val = evenTop1Val;
            evenTop1Cnt = evenCnt[v];
            evenTop1Val = v;
        } else if (evenCnt[v] > evenTop2Cnt) {
            evenTop2Cnt = evenCnt[v];
            evenTop2Val = v;
        }

        if (oddCnt[v] > oddTop1Cnt) {
            oddTop2Cnt = oddTop1Cnt;
            oddTop2Val = oddTop1Val;
            oddTop1Cnt = oddCnt[v];
            oddTop1Val = v;
        } else if (oddCnt[v] > oddTop2Cnt) {
            oddTop2Cnt = oddCnt[v];
            oddTop2Val = v;
        }
    }

    int keep;
    if (evenTop1Val != oddTop1Val) {
        keep = evenTop1Cnt + oddTop1Cnt;
    } else {
        int option1 = evenTop1Cnt + oddTop2Cnt; // use second best for odd positions
        int option2 = evenTop2Cnt + oddTop1Cnt; // use second best for even positions
        keep = (option1 > option2) ? option1 : option2;
    }

    free(evenCnt);
    free(oddCnt);

    return numsSize - keep;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumOperations(int[] nums)
    {
        var evenCounts = new Dictionary<int, int>();
        var oddCounts = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            if ((i & 1) == 0)
            {
                if (!evenCounts.ContainsKey(nums[i]))
                    evenCounts[nums[i]] = 0;
                evenCounts[nums[i]]++;
            }
            else
            {
                if (!oddCounts.ContainsKey(nums[i]))
                    oddCounts[nums[i]] = 0;
                oddCounts[nums[i]]++;
            }
        }

        // Find top two frequencies for even positions
        int topEvenVal = -1, topEvenFreq = 0, secondEvenFreq = 0;
        foreach (var kvp in evenCounts)
        {
            if (kvp.Value > topEvenFreq)
            {
                secondEvenFreq = topEvenFreq;
                topEvenFreq = kvp.Value;
                topEvenVal = kvp.Key;
            }
            else if (kvp.Value > secondEvenFreq)
            {
                secondEvenFreq = kvp.Value;
            }
        }

        // Find top two frequencies for odd positions
        int topOddVal = -1, topOddFreq = 0, secondOddFreq = 0;
        foreach (var kvp in oddCounts)
        {
            if (kvp.Value > topOddFreq)
            {
                secondOddFreq = topOddFreq;
                topOddFreq = kvp.Value;
                topOddVal = kvp.Key;
            }
            else if (kvp.Value > secondOddFreq)
            {
                secondOddFreq = kvp.Value;
            }
        }

        int keep;
        if (topEvenVal != topOddVal)
        {
            keep = topEvenFreq + topOddFreq;
        }
        else
        {
            keep = Math.Max(topEvenFreq + secondOddFreq, secondEvenFreq + topOddFreq);
        }

        return nums.Length - keep;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    const evenMap = new Map();
    const oddMap = new Map();

    for (let i = 0; i < nums.length; i++) {
        if ((i & 1) === 0) {
            evenMap.set(nums[i], (evenMap.get(nums[i]) || 0) + 1);
        } else {
            oddMap.set(nums[i], (oddMap.get(nums[i]) || 0) + 1);
        }
    }

    const getTopTwo = (map) => {
        let topVal = null, topFreq = 0, secondFreq = 0;
        for (const [val, freq] of map.entries()) {
            if (freq > topFreq) {
                secondFreq = topFreq;
                topFreq = freq;
                topVal = val;
            } else if (freq > secondFreq) {
                secondFreq = freq;
            }
        }
        return [topVal, topFreq, secondFreq];
    };

    const [evenTopVal, evenTopFreq, evenSecondFreq] = getTopTwo(evenMap);
    const [oddTopVal, oddTopFreq, oddSecondFreq] = getTopTwo(oddMap);

    let keep;
    if (evenTopVal !== oddTopVal) {
        keep = evenTopFreq + oddTopFreq;
    } else {
        keep = Math.max(evenTopFreq + oddSecondFreq, evenSecondFreq + oddTopFreq);
    }

    return nums.length - keep;
};
```

## Typescript

```typescript
function minimumOperations(nums: number[]): number {
    const evenMap = new Map<number, number>();
    const oddMap = new Map<number, number>();
    for (let i = 0; i < nums.length; i++) {
        if ((i & 1) === 0) {
            evenMap.set(nums[i], (evenMap.get(nums[i]) ?? 0) + 1);
        } else {
            oddMap.set(nums[i], (oddMap.get(nums[i]) ?? 0) + 1);
        }
    }

    const topTwo = (map: Map<number, number>): [number, number, number, number] => {
        let val1 = -1, cnt1 = 0, val2 = -1, cnt2 = 0;
        for (const [v, c] of map.entries()) {
            if (c > cnt1) {
                val2 = val1; cnt2 = cnt1;
                val1 = v; cnt1 = c;
            } else if (c > cnt2) {
                val2 = v; cnt2 = c;
            }
        }
        return [val1, cnt1, val2, cnt2];
    };

    const [evenVal1, evenCnt1, evenVal2, evenCnt2] = topTwo(evenMap);
    const [oddVal1, oddCnt1, oddVal2, oddCnt2] = topTwo(oddMap);

    if (evenVal1 !== oddVal1) {
        return nums.length - (evenCnt1 + oddCnt1);
    } else {
        const keep1 = evenCnt1 + oddCnt2;
        const keep2 = evenCnt2 + oddCnt1;
        const maxKeep = Math.max(keep1, keep2);
        return nums.length - maxKeep;
    }
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumOperations($nums) {
        $evenCount = [];
        $oddCount = [];

        foreach ($nums as $i => $num) {
            if (($i & 1) === 0) {
                $evenCount[$num] = ($evenCount[$num] ?? 0) + 1;
            } else {
                $oddCount[$num] = ($oddCount[$num] ?? 0) + 1;
            }
        }

        // Top two frequencies for even positions
        arsort($evenCount);
        $evenTop = [];
        foreach ($evenCount as $val => $cnt) {
            $evenTop[] = [$val, $cnt];
            if (count($evenTop) == 2) break;
        }
        while (count($evenTop) < 2) {
            $evenTop[] = [null, 0];
        }

        // Top two frequencies for odd positions
        arsort($oddCount);
        $oddTop = [];
        foreach ($oddCount as $val => $cnt) {
            $oddTop[] = [$val, $cnt];
            if (count($oddTop) == 2) break;
        }
        while (count($oddTop) < 2) {
            $oddTop[] = [null, 0];
        }

        [$valE1, $cntE1] = $evenTop[0];
        [$valE2, $cntE2] = $evenTop[1];
        [$valO1, $cntO1] = $oddTop[0];
        [$valO2, $cntO2] = $oddTop[1];

        $n = count($nums);
        if ($valE1 !== $valO1) {
            return $n - $cntE1 - $cntO1;
        } else {
            $keep1 = $cntE1 + $cntO2; // odd uses second best
            $keep2 = $cntE2 + $cntO1; // even uses second best
            $maxKeep = max($keep1, $keep2);
            return $n - $maxKeep;
        }
    }
}
```

## Swift

```swift
class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        var evenCounts = [Int:Int]()
        var oddCounts = [Int:Int]()
        
        for (i, num) in nums.enumerated() {
            if i % 2 == 0 {
                evenCounts[num, default: 0] += 1
            } else {
                oddCounts[num, default: 0] += 1
            }
        }
        
        func topTwo(_ dict: [Int:Int]) -> (value: Int, first: Int, second: Int) {
            var bestVal = -1
            var bestCnt = 0
            var secondCnt = 0
            for (v, c) in dict {
                if c > bestCnt {
                    secondCnt = bestCnt
                    bestCnt = c
                    bestVal = v
                } else if c > secondCnt {
                    secondCnt = c
                }
            }
            return (bestVal, bestCnt, secondCnt)
        }
        
        let (evenVal, evenFirst, evenSecond) = topTwo(evenCounts)
        let (oddVal, oddFirst, oddSecond) = topTwo(oddCounts)
        
        var keep: Int
        if evenVal != oddVal {
            keep = evenFirst + oddFirst
        } else {
            keep = max(evenFirst + oddSecond, evenSecond + oddFirst)
        }
        
        return nums.count - keep
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumOperations(nums: IntArray): Int {
        val evenCount = HashMap<Int, Int>()
        val oddCount = HashMap<Int, Int>()
        for (i in nums.indices) {
            if ((i and 1) == 0) {
                evenCount[nums[i]] = (evenCount[nums[i]] ?: 0) + 1
            } else {
                oddCount[nums[i]] = (oddCount[nums[i]] ?: 0) + 1
            }
        }

        fun topTwo(map: HashMap<Int, Int>): Triple<Int, Int, Int> {
            var firstVal = -1
            var firstCnt = 0
            var secondCnt = 0
            for ((k, c) in map) {
                if (c > firstCnt) {
                    secondCnt = firstCnt
                    firstCnt = c
                    firstVal = k
                } else if (c > secondCnt) {
                    secondCnt = c
                }
            }
            return Triple(firstVal, firstCnt, secondCnt)
        }

        val (evenFirstVal, evenFirstCnt, evenSecondCnt) = topTwo(evenCount)
        val (oddFirstVal, oddFirstCnt, oddSecondCnt) = topTwo(oddCount)

        val keep = if (evenFirstVal != oddFirstVal) {
            evenFirstCnt + oddFirstCnt
        } else {
            maxOf(evenSecondCnt + oddFirstCnt, evenFirstCnt + oddSecondCnt)
        }

        return nums.size - keep
    }
}
```

## Dart

```dart
class Solution {
  int minimumOperations(List<int> nums) {
    Map<int, int> evenCounts = {};
    Map<int, int> oddCounts = {};

    for (int i = 0; i < nums.length; i++) {
      if ((i & 1) == 0) {
        evenCounts[nums[i]] = (evenCounts[nums[i]] ?? 0) + 1;
      } else {
        oddCounts[nums[i]] = (oddCounts[nums[i]] ?? 0) + 1;
      }
    }

    int evenFirstVal = -1, evenFirstCnt = 0;
    int evenSecondVal = -1, evenSecondCnt = 0;
    evenCounts.forEach((val, cnt) {
      if (cnt > evenFirstCnt) {
        evenSecondCnt = evenFirstCnt;
        evenSecondVal = evenFirstVal;
        evenFirstCnt = cnt;
        evenFirstVal = val;
      } else if (cnt > evenSecondCnt) {
        evenSecondCnt = cnt;
        evenSecondVal = val;
      }
    });

    int oddFirstVal = -1, oddFirstCnt = 0;
    int oddSecondVal = -1, oddSecondCnt = 0;
    oddCounts.forEach((val, cnt) {
      if (cnt > oddFirstCnt) {
        oddSecondCnt = oddFirstCnt;
        oddSecondVal = oddFirstVal;
        oddFirstCnt = cnt;
        oddFirstVal = val;
      } else if (cnt > oddSecondCnt) {
        oddSecondCnt = cnt;
        oddSecondVal = val;
      }
    });

    int keep;
    if (evenFirstVal != oddFirstVal) {
      keep = evenFirstCnt + oddFirstCnt;
    } else {
      int option1 = evenFirstCnt + oddSecondCnt;
      int option2 = evenSecondCnt + oddFirstCnt;
      keep = option1 > option2 ? option1 : option2;
    }

    return nums.length - keep;
  }
}
```

## Golang

```go
func minimumOperations(nums []int) int {
    n := len(nums)
    evenFreq := make(map[int]int)
    oddFreq := make(map[int]int)

    for i, v := range nums {
        if i%2 == 0 {
            evenFreq[v]++
        } else {
            oddFreq[v]++
        }
    }

    type pair struct {
        val int
        cnt int
    }

    getTopTwo := func(freq map[int]int) (pair, pair) {
        var first, second pair
        for v, c := range freq {
            if c > first.cnt {
                second = first
                first = pair{v, c}
            } else if c > second.cnt {
                second = pair{v, c}
            }
        }
        return first, second
    }

    evenFirst, evenSecond := getTopTwo(evenFreq)
    oddFirst, oddSecond := getTopTwo(oddFreq)

    // If the most frequent values are different, keep both.
    if evenFirst.val != oddFirst.val {
        return n - evenFirst.cnt - oddFirst.cnt
    }

    // Otherwise choose the best alternative combination.
    keep1 := evenFirst.cnt + oddSecond.cnt
    keep2 := evenSecond.cnt + oddFirst.cnt
    maxKeep := keep1
    if keep2 > maxKeep {
        maxKeep = keep2
    }
    return n - maxKeep
}
```

## Ruby

```ruby
def minimum_operations(nums)
  even_counts = Hash.new(0)
  odd_counts = Hash.new(0)

  nums.each_with_index do |num, i|
    if i.even?
      even_counts[num] += 1
    else
      odd_counts[num] += 1
    end
  end

  def top_two(hash)
    first_val = nil
    first_cnt = 0
    second_cnt = 0
    hash.each do |val, cnt|
      if cnt > first_cnt
        second_cnt = first_cnt
        first_cnt = cnt
        first_val = val
      elsif cnt > second_cnt
        second_cnt = cnt
      end
    end
    [first_val, first_cnt, second_cnt]
  end

  even_val1, even_cnt1, even_cnt2 = top_two(even_counts)
  odd_val1, odd_cnt1, odd_cnt2 = top_two(odd_counts)

  kept =
    if even_val1 != odd_val1
      even_cnt1 + odd_cnt1
    else
      [even_cnt1 + odd_cnt2, even_cnt2 + odd_cnt1].max
    end

  nums.length - kept
end
```

## Scala

```scala
object Solution {
    def minimumOperations(nums: Array[Int]): Int = {
        val evenFreq = scala.collection.mutable.Map[Int, Int]()
        val oddFreq = scala.collection.mutable.Map[Int, Int]()

        for (i <- nums.indices) {
            if ((i & 1) == 0) {
                evenFreq(nums(i)) = evenFreq.getOrElse(nums(i), 0) + 1
            } else {
                oddFreq(nums(i)) = oddFreq.getOrElse(nums(i), 0) + 1
            }
        }

        def topTwo(freq: scala.collection.mutable.Map[Int, Int]): Array[(Int, Int)] = {
            var firstVal = -1
            var firstCnt = 0
            var secondVal = -1
            var secondCnt = 0
            for ((v, c) <- freq) {
                if (c > firstCnt) {
                    secondCnt = firstCnt
                    secondVal = firstVal
                    firstCnt = c
                    firstVal = v
                } else if (c > secondCnt) {
                    secondCnt = c
                    secondVal = v
                }
            }
            Array((firstVal, firstCnt), (secondVal, secondCnt))
        }

        val evenTop = topTwo(evenFreq)
        val oddTop = topTwo(oddFreq)

        val n = nums.length
        if (evenTop(0)._1 != oddTop(0)._1) {
            n - (evenTop(0)._2 + oddTop(0)._2)
        } else {
            val keep1 = evenTop(0)._2 + oddTop(1)._2 // use second best odd value
            val keep2 = evenTop(1)._2 + oddTop(0)._2 // use second best even value
            n - Math.max(keep1, keep2)
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        let n = nums.len();
        let mut even_map: HashMap<i32, usize> = HashMap::new();
        let mut odd_map: HashMap<i32, usize> = HashMap::new();

        for (i, &v) in nums.iter().enumerate() {
            if i % 2 == 0 {
                *even_map.entry(v).or_insert(0) += 1;
            } else {
                *odd_map.entry(v).or_insert(0) += 1;
            }
        }

        // Find top two frequencies for even positions
        let (mut ev_first_val, mut ev_first_cnt) = (0i32, 0usize);
        let (mut ev_second_val, mut ev_second_cnt) = (0i32, 0usize);
        for (&val, &cnt) in even_map.iter() {
            if cnt > ev_first_cnt {
                ev_second_val = ev_first_val;
                ev_second_cnt = ev_first_cnt;
                ev_first_val = val;
                ev_first_cnt = cnt;
            } else if cnt > ev_second_cnt {
                ev_second_val = val;
                ev_second_cnt = cnt;
            }
        }

        // Find top two frequencies for odd positions
        let (mut od_first_val, mut od_first_cnt) = (0i32, 0usize);
        let (mut od_second_val, mut od_second_cnt) = (0i32, 0usize);
        for (&val, &cnt) in odd_map.iter() {
            if cnt > od_first_cnt {
                od_second_val = od_first_val;
                od_second_cnt = od_first_cnt;
                od_first_val = val;
                od_first_cnt = cnt;
            } else if cnt > od_second_cnt {
                od_second_val = val;
                od_second_cnt = cnt;
            }
        }

        let total = n as i32;
        if ev_first_val != od_first_val {
            // we can keep both most frequent values
            total - ((ev_first_cnt + od_first_cnt) as i32)
        } else {
            // need to choose alternative for one side
            let keep_even_top_odd_second = ev_first_cnt + od_second_cnt;
            let keep_odd_top_even_second = ev_second_cnt + od_first_cnt;
            let max_keep = std::cmp::max(keep_even_top_odd_second, keep_odd_top_even_second);
            total - (max_keep as i32)
        }
    }
}
```

## Racket

```racket
(define/contract (minimum-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (even-hash (make-hash))
         (odd-hash (make-hash)))
    (for ([i (in-range n)]
          [v (in-list nums)])
      (if (even? i)
          (hash-update! even-hash v add1 0)
          (hash-update! odd-hash v add1 0)))
    (define (top-two h)
      (let ((pairs (hash->list h)))
        (if (null? pairs)
            (list (cons 0 0) (cons 0 0))
            (let* ((sorted (sort pairs > #:key cdr))
                   (first (car sorted))
                   (second (if (null? (cdr sorted)) (cons 0 0) (cadr sorted))))
              (list first second)))))
    (define evens (top-two even-hash))
    (define odds (top-two odd-hash))
    (define e1 (car evens))
    (define e2 (cadr evens))
    (define o1 (car odds))
    (define o2 (cadr odds))
    (define keep
      (if (not (= (car e1) (car o1)))
          (+ (cdr e1) (cdr o1))
          (max (+ (cdr e1) (cdr o2)) (+ (cdr e2) (cdr o1)))))
    (- n keep)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_operations/1]).

-spec minimum_operations(Nums :: [integer()]) -> integer().
minimum_operations(Nums) ->
    {EvenMap, OddMap} = build_maps(Nums, 0, #{}, #{}),
    {EV1, EC1, EV2, EC2} = top_two(EvenMap),
    {OV1, OC1, OV2, OC2} = top_two(OddMap),
    N = length(Nums),
    case EV1 =/= OV1 of
        true ->
            N - EC1 - OC1;
        false ->
            Ops1 = N - EC1 - OC2,
            Ops2 = N - EC2 - OC1,
            min(Ops1, Ops2)
    end.

build_maps([], _Idx, EvenMap, OddMap) -> {EvenMap, OddMap};
build_maps([H|T], Idx, EvenMap, OddMap) ->
    if
        (Idx rem 2) =:= 0 ->
            NewEven = maps:update_with(H, fun(C) -> C + 1 end, 1, EvenMap),
            build_maps(T, Idx + 1, NewEven, OddMap);
        true ->
            NewOdd = maps:update_with(H, fun(C) -> C + 1 end, 1, OddMap),
            build_maps(T, Idx + 1, EvenMap, NewOdd)
    end.

top_two(Map) ->
    top_two(maps:to_list(Map), undefined, 0, undefined, 0).

top_two([], V1, C1, V2, C2) -> {V1, C1, V2, C2};
top_two([{Key, Count}|Rest], V1, C1, V2, C2) ->
    if
        Count > C1 ->
            top_two(Rest, Key, Count, V1, C1);
        Count > C2 ->
            top_two(Rest, V1, C1, Key, Count);
        true ->
            top_two(Rest, V1, C1, V2, C2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(nums :: [integer]) :: integer
  def minimum_operations(nums) do
    {even_map, odd_map} =
      Enum.reduce(Enum.with_index(nums), {%{}, %{}}, fn {val, idx}, {e_acc, o_acc} ->
        if rem(idx, 2) == 0 do
          {Map.update(e_acc, val, 1, &(&1 + 1)), o_acc}
        else
          {e_acc, Map.update(o_acc, val, 1, &(&1 + 1))}
        end
      end)

    even_sorted = Enum.sort_by(even_map, fn {_k, v} -> -v end)
    odd_sorted = Enum.sort_by(odd_map, fn {_k, v} -> -v end)

    {even_top1_val, even_top1_cnt} =
      case even_sorted do
        [{val, cnt} | _] -> {val, cnt}
        [] -> {nil, 0}
      end

    {even_top2_val, even_top2_cnt} =
      case Enum.at(even_sorted, 1) do
        nil -> {nil, 0}
        {val, cnt} -> {val, cnt}
      end

    {odd_top1_val, odd_top1_cnt} =
      case odd_sorted do
        [{val, cnt} | _] -> {val, cnt}
        [] -> {nil, 0}
      end

    {odd_top2_val, odd_top2_cnt} =
      case Enum.at(odd_sorted, 1) do
        nil -> {nil, 0}
        {val, cnt} -> {val, cnt}
      end

    n = length(nums)

    if even_top1_val != odd_top1_val do
      n - (even_top1_cnt + odd_top1_cnt)
    else
      keep1 = even_top1_cnt + odd_top2_cnt
      keep2 = even_top2_cnt + odd_top1_cnt
      max_keep = max(keep1, keep2)
      n - max_keep
    end
  end
end
```
