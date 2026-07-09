# 2448. Minimum Cost to Make Array Equal

## Cpp

```cpp
class Solution {
public:
    long long minCost(vector<int>& nums, vector<int>& cost) {
        int n = nums.size();
        vector<pair<long long,long long>> v;
        v.reserve(n);
        for (int i = 0; i < n; ++i) {
            v.emplace_back((long long)nums[i], (long long)cost[i]);
        }
        sort(v.begin(), v.end(),
             [](const pair<long long,long long>& a, const pair<long long,long long>& b){
                 return a.first < b.first;
             });
        long long total = 0;
        for (auto &p : v) total += p.second;
        long long half = (total + 1) / 2; // weighted median position
        long long pref = 0;
        long long target = v.back().first;
        for (auto &p : v) {
            pref += p.second;
            if (pref >= half) {
                target = p.first;
                break;
            }
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            ans += llabs((long long)nums[i] - target) * (long long)cost[i];
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long minCost(int[] nums, int[] cost) {
        int n = nums.length;
        long[][] pairs = new long[n][2];
        for (int i = 0; i < n; i++) {
            pairs[i][0] = nums[i];
            pairs[i][1] = cost[i];
        }
        Arrays.sort(pairs, Comparator.comparingLong(a -> a[0]));
        long totalWeight = 0;
        for (long[] p : pairs) {
            totalWeight += p[1];
        }
        long cum = 0;
        long median = 0;
        for (int i = 0; i < n; i++) {
            cum += pairs[i][1];
            if (cum * 2 >= totalWeight) {
                median = pairs[i][0];
                break;
            }
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            ans += Math.abs(pairs[i][0] - median) * pairs[i][1];
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # Pair and sort by nums
        pairs = sorted(zip(nums, cost), key=lambda x: x[0])
        total_weight = sum(c for _, c in pairs)
        cum = 0
        median = None
        for val, w in pairs:
            cum += w
            if cum * 2 >= total_weight:
                median = val
                break
        # Compute total cost to make all elements equal to median
        ans = 0
        for val, w in pairs:
            ans += w * abs(val - median)
        return ans
```

## Python3

```python
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pairs = sorted(zip(nums, cost), key=lambda x: x[0])
        total_weight = sum(cost)
        cum = 0
        median = 0
        for val, w in pairs:
            cum += w
            if cum * 2 >= total_weight:
                median = val
                break
        return sum(w * abs(val - median) for val, w in pairs)
```

## C

```c
#include <stdlib.h>

typedef struct {
    long long num;
    long long cost;
} Pair;

static int cmpPair(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    if (pa->num < pb->num) return -1;
    if (pa->num > pb->num) return 1;
    return 0;
}

long long minCost(int* nums, int numsSize, int* cost, int costSize) {
    (void)costSize; // unused, same as numsSize
    Pair *arr = (Pair *)malloc(sizeof(Pair) * numsSize);
    if (!arr) return 0;
    for (int i = 0; i < numsSize; ++i) {
        arr[i].num = (long long)nums[i];
        arr[i].cost = (long long)cost[i];
    }
    qsort(arr, numsSize, sizeof(Pair), cmpPair);
    
    long long totalWeight = 0;
    for (int i = 0; i < numsSize; ++i)
        totalWeight += arr[i].cost;
    
    long long half = (totalWeight + 1) / 2; // ceil(total/2)
    long long pref = 0;
    long long target = arr[numsSize - 1].num;
    for (int i = 0; i < numsSize; ++i) {
        pref += arr[i].cost;
        if (pref >= half) {
            target = arr[i].num;
            break;
        }
    }
    
    long long ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        long long diff = arr[i].num - target;
        if (diff < 0) diff = -diff;
        ans += diff * arr[i].cost;
    }
    
    free(arr);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public long MinCost(int[] nums, int[] cost)
    {
        int n = nums.Length;
        var pairs = new (int num, int w)[n];
        for (int i = 0; i < n; i++)
            pairs[i] = (nums[i], cost[i]);

        Array.Sort(pairs, (a, b) => a.num.CompareTo(b.num));

        long totalWeight = 0;
        foreach (var p in pairs)
            totalWeight += p.w;

        long prefix = 0;
        int medianVal = 0;
        foreach (var p in pairs)
        {
            prefix += p.w;
            if (prefix * 2 >= totalWeight)
            {
                medianVal = p.num;
                break;
            }
        }

        long ans = 0;
        foreach (var p in pairs)
            ans += (long)Math.Abs(p.num - medianVal) * p.w;

        return ans;
    }
}
```

## Javascript

```javascript
var minCost = function(nums, cost) {
    const n = nums.length;
    const pairs = new Array(n);
    for (let i = 0; i < n; ++i) {
        pairs[i] = [nums[i], cost[i]];
    }
    pairs.sort((a, b) => a[0] - b[0]);

    let totalWeight = 0n;
    for (let i = 0; i < n; ++i) {
        totalWeight += BigInt(pairs[i][1]);
    }

    const half = (totalWeight + 1n) / 2n;
    let prefix = 0n;
    let target = pairs[0][0];
    for (let i = 0; i < n; ++i) {
        prefix += BigInt(pairs[i][1]);
        if (prefix >= half) {
            target = pairs[i][0];
            break;
        }
    }

    let ans = 0n;
    for (let i = 0; i < n; ++i) {
        const diff = BigInt(Math.abs(nums[i] - target));
        ans += diff * BigInt(cost[i]);
    }
    return Number(ans);
};
```

## Typescript

```typescript
function minCost(nums: number[], cost: number[]): number {
    const n = nums.length;
    const pairs: [number, number][] = new Array(n);
    let totalWeight = 0;
    for (let i = 0; i < n; i++) {
        pairs[i] = [nums[i], cost[i]];
        totalWeight += cost[i];
    }
    pairs.sort((a, b) => a[0] - b[0]);

    let prefix = 0;
    let target = pairs[n - 1][0];
    for (let i = 0; i < n; i++) {
        prefix += pairs[i][1];
        if (prefix * 2 >= totalWeight) {
            target = pairs[i][0];
            break;
        }
    }

    let ans = 0;
    for (let i = 0; i < n; i++) {
        ans += cost[i] * Math.abs(nums[i] - target);
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $cost
     * @return Integer
     */
    function minCost($nums, $cost) {
        $n = count($nums);
        $pairs = [];
        for ($i = 0; $i < $n; $i++) {
            $pairs[] = [$nums[$i], $cost[$i]];
        }
        usort($pairs, function($a, $b) {
            if ($a[0] == $b[0]) return 0;
            return ($a[0] < $b[0]) ? -1 : 1;
        });

        $totalWeight = 0;
        foreach ($cost as $c) {
            $totalWeight += $c;
        }

        $cum = 0;
        $target = $pairs[0][0];
        foreach ($pairs as $p) {
            $cum += $p[1];
            if ($cum * 2 >= $totalWeight) { // weighted median condition
                $target = $p[0];
                break;
            }
        }

        $ans = 0;
        foreach ($pairs as $p) {
            $ans += abs($p[0] - $target) * $p[1];
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minCost(_ nums: [Int], _ cost: [Int]) -> Int {
        let n = nums.count
        var pairs = [(num: Int, cost: Int)]()
        pairs.reserveCapacity(n)
        for i in 0..<n {
            pairs.append((nums[i], cost[i]))
        }
        pairs.sort { $0.num < $1.num }
        
        var totalWeight: Int64 = 0
        for p in pairs {
            totalWeight += Int64(p.cost)
        }
        let half = (totalWeight + 1) / 2   // ceil(totalWeight/2)
        var cum: Int64 = 0
        var target = 0
        for p in pairs {
            cum += Int64(p.cost)
            if cum >= half {
                target = p.num
                break
            }
        }
        
        var result: Int64 = 0
        let t = Int64(target)
        for p in pairs {
            let diff = abs(Int64(p.num) - t)
            result += diff * Int64(p.cost)
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCost(nums: IntArray, cost: IntArray): Long {
        val n = nums.size
        val arr = Array(n) { i -> longArrayOf(nums[i].toLong(), cost[i].toLong()) }
        java.util.Arrays.sort(arr) { a, b ->
            when {
                a[0] < b[0] -> -1
                a[0] > b[0] -> 1
                else -> 0
            }
        }
        var total = 0L
        for (i in 0 until n) {
            total += arr[i][1]
        }
        val half = (total + 1) / 2
        var prefix = 0L
        var target = arr[n - 1][0]
        for (i in 0 until n) {
            prefix += arr[i][1]
            if (prefix >= half) {
                target = arr[i][0]
                break
            }
        }
        var ans = 0L
        for (i in 0 until n) {
            ans += kotlin.math.abs(arr[i][0] - target) * arr[i][1]
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minCost(List<int> nums, List<int> cost) {
    int n = nums.length;
    // Pair each number with its corresponding cost
    List<MapEntry<int, int>> pairs = List.generate(
        n, (i) => MapEntry(nums[i], cost[i]));
    // Sort by the numbers
    pairs.sort((a, b) => a.key.compareTo(b.key));

    // Total weight (sum of costs)
    int totalWeight = 0;
    for (var p in pairs) {
      totalWeight += p.value;
    }

    // Find weighted median
    int half = (totalWeight + 1) >> 1; // ceil(totalWeight / 2)
    int prefix = 0;
    int target = 0;
    for (var p in pairs) {
      prefix += p.value;
      if (prefix >= half) {
        target = p.key;
        break;
      }
    }

    // Compute total cost to make all elements equal to the median
    int answer = 0;
    for (int i = 0; i < n; ++i) {
      answer += (nums[i] - target).abs() * cost[i];
    }
    return answer;
  }
}
```

## Golang

```go
func minCost(nums []int, cost []int) int64 {
	type pair struct {
		num  int
		cost int64
	}
	n := len(nums)
	pairs := make([]pair, n)
	var totalCost int64
	for i := 0; i < n; i++ {
		c := int64(cost[i])
		pairs[i] = pair{num: nums[i], cost: c}
		totalCost += c
	}
	// sort by num
	sort.Slice(pairs, func(i, j int) bool { return pairs[i].num < pairs[j].num })
	// find weighted median
	var cum int64
	target := 0
	for _, p := range pairs {
		cum += p.cost
		if cum*2 >= totalCost {
			target = p.num
			break
		}
	}
	// compute total cost to make all equal to target
	var ans int64
	for _, p := range pairs {
		diff := int64(p.num - target)
		if diff < 0 {
			diff = -diff
		}
		ans += diff * p.cost
	}
	return ans
}
```

## Ruby

```ruby
def min_cost(nums, cost)
  pairs = nums.zip(cost)
  pairs.sort_by! { |v, _| v }
  total_weight = cost.sum
  half = (total_weight + 1) / 2
  cum = 0
  target = nil
  pairs.each do |val, w|
    cum += w
    if cum >= half
      target = val
      break
    end
  end
  ans = 0
  pairs.each do |val, w|
    ans += (val - target).abs * w
  end
  ans
end
```

## Scala

```scala
object Solution {
    def minCost(nums: Array[Int], cost: Array[Int]): Long = {
        val n = nums.length
        // Pair each number with its corresponding cost (as Long)
        val pairs = new Array[(Int, Long)](n)
        var i = 0
        while (i < n) {
            pairs(i) = (nums(i), cost(i).toLong)
            i += 1
        }
        // Sort by the number values
        scala.util.Sorting.stableSort(pairs)(Ordering.by[(Int, Long), Int](_._1))

        // Total weight (sum of costs)
        var totalWeight: Long = 0L
        i = 0
        while (i < n) {
            totalWeight += pairs(i)._2
            i += 1
        }

        // Find weighted median as target value
        var cumWeight: Long = 0L
        var target = pairs(0)._1
        i = 0
        while (i < n) {
            cumWeight += pairs(i)._2
            if (cumWeight * 2 >= totalWeight) {
                target = pairs(i)._1
                // median found, exit loop
                i = n
            } else {
                i += 1
            }
        }

        // Compute total cost to make all elements equal to target
        var answer: Long = 0L
        i = 0
        while (i < n) {
            val diff = (nums(i) - target).toLong
            answer += cost(i).toLong * (if (diff < 0) -diff else diff)
            i += 1
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_cost(nums: Vec<i32>, cost: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut pairs: Vec<(i32, i64)> = (0..n)
            .map(|i| (nums[i], cost[i] as i64))
            .collect();
        pairs.sort_by_key(|&(v, _)| v);
        let total_weight: i64 = pairs.iter().map(|&(_, w)| w).sum();
        let need = (total_weight + 1) / 2;
        let mut prefix = 0i64;
        let mut target = pairs[0].0;
        for &(val, w) in &pairs {
            prefix += w;
            if prefix >= need {
                target = val;
                break;
            }
        }
        let mut ans: i64 = 0;
        for &(val, w) in &pairs {
            let diff = (val as i64 - target as i64).abs();
            ans += diff * w;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-cost nums cost)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((pairs (map cons nums cost))
         (sorted-pairs (sort pairs < #:key car))
         (total-weight (foldl + 0 cost))
         (half (quotient (+ total-weight 1) 2))) ; ceil(total/2)
    (define prefix 0)
    (define target 0)
    (for ([p sorted-pairs])
      (set! prefix (+ prefix (cdr p)))
      (when (and (= target 0) (>= prefix half))
        (set! target (car p))))
    (foldl + 0
           (map (lambda (n c)
                  (* c (abs (- n target))))
                nums cost))))
```

## Erlang

```erlang
-spec min_cost([integer()], [integer()]) -> integer().
min_cost(Nums, Cost) ->
    Pairs = lists:zip(Nums, Cost),
    Sorted = lists:keysort(1, Pairs),
    TotalWeight = lists:foldl(fun({_N,W}, Acc) -> Acc + W end, 0, Sorted),
    Half = (TotalWeight + 1) div 2,
    Median = find_median(Sorted, Half, 0),
    compute_cost(Sorted, Median).

find_median([], _Half, _Acc) ->
    0;
find_median([{Num,W}|Rest], Half, Acc) ->
    NewAcc = Acc + W,
    if
        NewAcc >= Half -> Num;
        true -> find_median(Rest, Half, NewAcc)
    end.

compute_cost(List, Target) ->
    lists:foldl(fun({Num,W}, Acc) ->
        Diff = erlang:abs(Num - Target),
        Acc + Diff * W
    end, 0, List).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_cost(nums :: [integer], cost :: [integer]) :: integer
  def min_cost(nums, cost) do
    pairs = Enum.zip(nums, cost)
    sorted = Enum.sort_by(pairs, fn {num, _} -> num end)

    total_weight = Enum.reduce(cost, 0, &+/2)
    half = div(total_weight + 1, 2)

    target =
      sorted
      |> Enum.reduce_while({0, 0}, fn {num, w}, {_curr_target, acc} ->
        new_acc = acc + w

        if new_acc >= half do
          {:halt, num}
        else
          {:cont, {0, new_acc}}
        end
      end)

    Enum.reduce(sorted, 0, fn {num, w}, sum ->
      sum + abs(num - target) * w
    end)
  end
end
```
