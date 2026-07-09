# 2449. Minimum Number of Operations to Make Arrays Similar

## Cpp

```cpp
class Solution {
public:
    long long makeSimilar(vector<int>& nums, vector<int>& target) {
        vector<int> evenNums, oddNums, evenTarget, oddTarget;
        for (int x : nums) {
            if (x % 2 == 0) evenNums.push_back(x);
            else oddNums.push_back(x);
        }
        for (int x : target) {
            if (x % 2 == 0) evenTarget.push_back(x);
            else oddTarget.push_back(x);
        }
        sort(evenNums.begin(), evenNums.end());
        sort(evenTarget.begin(), evenTarget.end());
        sort(oddNums.begin(), oddNums.end());
        sort(oddTarget.begin(), oddTarget.end());
        
        long long ops = 0;
        for (size_t i = 0; i < evenNums.size(); ++i) {
            if (evenNums[i] > evenTarget[i])
                ops += (long long)(evenNums[i] - evenTarget[i]);
        }
        for (size_t i = 0; i < oddNums.size(); ++i) {
            if (oddNums[i] > oddTarget[i])
                ops += (long long)(oddNums[i] - oddTarget[i]);
        }
        return ops / 2;
    }
};
```

## Java

```java
class Solution {
    public long makeSimilar(int[] nums, int[] target) {
        java.util.List<Integer> numsEven = new java.util.ArrayList<>();
        java.util.List<Integer> numsOdd = new java.util.ArrayList<>();
        java.util.List<Integer> targetEven = new java.util.ArrayList<>();
        java.util.List<Integer> targetOdd = new java.util.ArrayList<>();

        for (int v : nums) {
            if ((v & 1) == 0) numsEven.add(v);
            else numsOdd.add(v);
        }
        for (int v : target) {
            if ((v & 1) == 0) targetEven.add(v);
            else targetOdd.add(v);
        }

        java.util.Collections.sort(numsEven);
        java.util.Collections.sort(targetEven);
        java.util.Collections.sort(numsOdd);
        java.util.Collections.sort(targetOdd);

        long ops = 0;
        for (int i = 0; i < numsEven.size(); i++) {
            int a = numsEven.get(i);
            int b = targetEven.get(i);
            if (a > b) ops += (a - b) / 2L;
        }
        for (int i = 0; i < numsOdd.size(); i++) {
            int a = numsOdd.get(i);
            int b = targetOdd.get(i);
            if (a > b) ops += (a - b) / 2L;
        }
        return ops;
    }
}
```

## Python

```python
class Solution(object):
    def makeSimilar(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        ev_nums = []
        od_nums = []
        ev_tgt = []
        od_tgt = []

        for x in nums:
            (ev_nums if x % 2 == 0 else od_nums).append(x)
        for x in target:
            (ev_tgt if x % 2 == 0 else od_tgt).append(x)

        ev_nums.sort()
        ev_tgt.sort()
        od_nums.sort()
        od_tgt.sort()

        total_diff = 0
        for a, b in zip(ev_nums, ev_tgt):
            total_diff += abs(a - b)
        for a, b in zip(od_nums, od_tgt):
            total_diff += abs(a - b)

        return total_diff // 4
```

## Python3

```python
class Solution:
    def makeSimilar(self, nums, target):
        ev_nums = []
        od_nums = []
        ev_tgt = []
        od_tgt = []
        for x in nums:
            (ev_nums if x % 2 == 0 else od_nums).append(x)
        for x in target:
            (ev_tgt if x % 2 == 0 else od_tgt).append(x)
        ev_nums.sort()
        ev_tgt.sort()
        od_nums.sort()
        od_tgt.sort()
        diff = 0
        for a, b in zip(ev_nums, ev_tgt):
            diff += abs(a - b)
        for a, b in zip(od_nums, od_tgt):
            diff += abs(a - b)
        return diff // 4
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

long long makeSimilar(int* nums, int numsSize, int* target, int targetSize) {
    (void)targetSize; // unused, sizes are equal
    int *evenNums = (int *)malloc(numsSize * sizeof(int));
    int *oddNums  = (int *)malloc(numsSize * sizeof(int));
    int *evenTgt = (int *)malloc(numsSize * sizeof(int));
    int *oddTgt  = (int *)malloc(numsSize * sizeof(int));
    int eN = 0, oN = 0, eT = 0, oT = 0;

    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] % 2 == 0)
            evenNums[eN++] = nums[i];
        else
            oddNums[oN++] = nums[i];

        if (target[i] % 2 == 0)
            evenTgt[eT++] = target[i];
        else
            oddTgt[oT++] = target[i];
    }

    qsort(evenNums, eN, sizeof(int), cmp_int);
    qsort(oddNums, oN, sizeof(int), cmp_int);
    qsort(evenTgt, eT, sizeof(int), cmp_int);
    qsort(oddTgt, oT, sizeof(int), cmp_int);

    long long totalDiff = 0;
    for (int i = 0; i < eN; ++i)
        totalDiff += llabs((long long)evenNums[i] - (long long)evenTgt[i]);
    for (int i = 0; i < oN; ++i)
        totalDiff += llabs((long long)oddNums[i] - (long long)oddTgt[i]);

    free(evenNums);
    free(oddNums);
    free(evenTgt);
    free(oddTgt);

    return totalDiff / 4;
}
```

## Csharp

```csharp
public class Solution
{
    public long MakeSimilar(int[] nums, int[] target)
    {
        var evenNums = new List<int>();
        var oddNums = new List<int>();
        var evenTarget = new List<int>();
        var oddTarget = new List<int>();

        for (int i = 0; i < nums.Length; i++)
        {
            if ((nums[i] & 1) == 0) evenNums.Add(nums[i]); else oddNums.Add(nums[i]);
            if ((target[i] & 1) == 0) evenTarget.Add(target[i]); else oddTarget.Add(target[i]);
        }

        evenNums.Sort();
        evenTarget.Sort();
        oddNums.Sort();
        oddTarget.Sort();

        long totalDiff = 0;
        for (int i = 0; i < evenNums.Count; i++)
        {
            int diff = evenNums[i] - evenTarget[i];
            if (diff > 0) totalDiff += diff;
        }
        for (int i = 0; i < oddNums.Count; i++)
        {
            int diff = oddNums[i] - oddTarget[i];
            if (diff > 0) totalDiff += diff;
        }

        return totalDiff / 2;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} target
 * @return {number}
 */
var makeSimilar = function(nums, target) {
    const evNums = [], odNums = [];
    for (const x of nums) {
        if ((x & 1) === 0) evNums.push(x);
        else odNums.push(x);
    }
    const evTar = [], odTar = [];
    for (const x of target) {
        if ((x & 1) === 0) evTar.push(x);
        else odTar.push(x);
    }
    evNums.sort((a, b) => a - b);
    evTar.sort((a, b) => a - b);
    odNums.sort((a, b) => a - b);
    odTar.sort((a, b) => a - b);
    
    let diff = 0;
    for (let i = 0; i < evNums.length; ++i) {
        if (evTar[i] > evNums[i]) diff += evTar[i] - evNums[i];
    }
    for (let i = 0; i < odNums.length; ++i) {
        if (odTar[i] > odNums[i]) diff += odTar[i] - odNums[i];
    }
    return diff / 2;
};
```

## Typescript

```typescript
function makeSimilar(nums: number[], target: number[]): number {
    const numsEven: number[] = [];
    const numsOdd: number[] = [];
    const targetEven: number[] = [];
    const targetOdd: number[] = [];

    for (const x of nums) {
        if ((x & 1) === 0) numsEven.push(x);
        else numsOdd.push(x);
    }
    for (const x of target) {
        if ((x & 1) === 0) targetEven.push(x);
        else targetOdd.push(x);
    }

    numsEven.sort((a, b) => a - b);
    targetEven.sort((a, b) => a - b);
    numsOdd.sort((a, b) => a - b);
    targetOdd.sort((a, b) => a - b);

    let diff = 0;
    for (let i = 0; i < numsEven.length; ++i) {
        diff += Math.abs(numsEven[i] - targetEven[i]);
    }
    for (let i = 0; i < numsOdd.length; ++i) {
        diff += Math.abs(numsOdd[i] - targetOdd[i]);
    }

    return diff / 4;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $target
     * @return Integer
     */
    function makeSimilar($nums, $target) {
        $evenNums = [];
        $oddNums = [];
        $evenTarget = [];
        $oddTarget = [];

        foreach ($nums as $v) {
            if (($v & 1) == 0) {
                $evenNums[] = $v;
            } else {
                $oddNums[] = $v;
            }
        }

        foreach ($target as $v) {
            if (($v & 1) == 0) {
                $evenTarget[] = $v;
            } else {
                $oddTarget[] = $v;
            }
        }

        sort($evenNums);
        sort($evenTarget);
        sort($oddNums);
        sort($oddTarget);

        $ops = 0;

        $lenEven = count($evenNums);
        for ($i = 0; $i < $lenEven; $i++) {
            if ($evenNums[$i] > $evenTarget[$i]) {
                $ops += intdiv($evenNums[$i] - $evenTarget[$i], 2);
            }
        }

        $lenOdd = count($oddNums);
        for ($i = 0; $i < $lenOdd; $i++) {
            if ($oddNums[$i] > $oddTarget[$i]) {
                $ops += intdiv($oddNums[$i] - $oddTarget[$i], 2);
            }
        }

        return $ops;
    }
}
```

## Swift

```swift
class Solution {
    func makeSimilar(_ nums: [Int], _ target: [Int]) -> Int {
        var evenNums = [Int]()
        var oddNums = [Int]()
        var evenTarget = [Int]()
        var oddTarget = [Int]()
        
        for v in nums {
            if v % 2 == 0 {
                evenNums.append(v)
            } else {
                oddNums.append(v)
            }
        }
        for v in target {
            if v % 2 == 0 {
                evenTarget.append(v)
            } else {
                oddTarget.append(v)
            }
        }
        
        evenNums.sort()
        evenTarget.sort()
        oddNums.sort()
        oddTarget.sort()
        
        var excess = 0
        for i in 0..<evenNums.count {
            let diff = evenNums[i] - evenTarget[i]
            if diff > 0 { excess += diff }
        }
        for i in 0..<oddNums.count {
            let diff = oddNums[i] - oddTarget[i]
            if diff > 0 { excess += diff }
        }
        
        return excess / 2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun makeSimilar(nums: IntArray, target: IntArray): Long {
        val evenNums = mutableListOf<Int>()
        val evenTarget = mutableListOf<Int>()
        val oddNums = mutableListOf<Int>()
        val oddTarget = mutableListOf<Int>()

        for (v in nums) {
            if ((v and 1) == 0) evenNums.add(v) else oddNums.add(v)
        }
        for (v in target) {
            if ((v and 1) == 0) evenTarget.add(v) else oddTarget.add(v)
        }

        evenNums.sort()
        evenTarget.sort()
        oddNums.sort()
        oddTarget.sort()

        var diff = 0L
        for (i in evenNums.indices) {
            diff += kotlin.math.abs(evenNums[i] - evenTarget[i]).toLong()
        }
        for (i in oddNums.indices) {
            diff += kotlin.math.abs(oddNums[i] - oddTarget[i]).toLong()
        }

        return diff / 4
    }
}
```

## Dart

```dart
class Solution {
  int makeSimilar(List<int> nums, List<int> target) {
    List<int> evenNums = [];
    List<int> oddNums = [];
    List<int> evenTarget = [];
    List<int> oddTarget = [];

    for (int v in nums) {
      if ((v & 1) == 0) {
        evenNums.add(v);
      } else {
        oddNums.add(v);
      }
    }

    for (int v in target) {
      if ((v & 1) == 0) {
        evenTarget.add(v);
      } else {
        oddTarget.add(v);
      }
    }

    evenNums.sort();
    evenTarget.sort();
    oddNums.sort();
    oddTarget.sort();

    int totalDiff = 0;
    for (int i = 0; i < evenNums.length; ++i) {
      totalDiff += (evenNums[i] - evenTarget[i]).abs();
    }
    for (int i = 0; i < oddNums.length; ++i) {
      totalDiff += (oddNums[i] - oddTarget[i]).abs();
    }

    // Each operation can adjust two numbers by 2, reducing the total difference by 4.
    return totalDiff ~/ 4;
  }
}
```

## Golang

```go
func makeSimilar(nums []int, target []int) int64 {
    var evenNums, oddNums []int
    var evenTarget, oddTarget []int

    for _, v := range nums {
        if v%2 == 0 {
            evenNums = append(evenNums, v)
        } else {
            oddNums = append(oddNums, v)
        }
    }
    for _, v := range target {
        if v%2 == 0 {
            evenTarget = append(evenTarget, v)
        } else {
            oddTarget = append(oddTarget, v)
        }
    }

    sort.Ints(evenNums)
    sort.Ints(evenTarget)
    sort.Ints(oddNums)
    sort.Ints(oddTarget)

    var total int64
    for i := 0; i < len(evenNums); i++ {
        diff := evenNums[i] - evenTarget[i]
        if diff < 0 {
            diff = -diff
        }
        total += int64(diff)
    }
    for i := 0; i < len(oddNums); i++ {
        diff := oddNums[i] - oddTarget[i]
        if diff < 0 {
            diff = -diff
        }
        total += int64(diff)
    }

    return total / 4
}
```

## Ruby

```ruby
def make_similar(nums, target)
  ev_nums = []
  od_nums = []
  nums.each do |x|
    if x.even?
      ev_nums << x
    else
      od_nums << x
    end
  end

  ev_tgt = []
  od_tgt = []
  target.each do |x|
    if x.even?
      ev_tgt << x
    else
      od_tgt << x
    end
  end

  ev_nums.sort!
  ev_tgt.sort!
  od_nums.sort!
  od_tgt.sort!

  diff = 0
  ev_nums.each_index { |i| diff += (ev_nums[i] - ev_tgt[i]).abs }
  od_nums.each_index { |i| diff += (od_nums[i] - od_tgt[i]).abs }

  diff / 4
end
```

## Scala

```scala
object Solution {
  def makeSimilar(nums: Array[Int], target: Array[Int]): Long = {
    val evN = nums.filter(_ % 2 == 0).sorted
    val evT = target.filter(_ % 2 == 0).sorted
    val odN = nums.filter(_ % 2 != 0).sorted
    val odT = target.filter(_ % 2 != 0).sorted

    var surplus: Long = 0L

    for (i <- evN.indices) {
      if (evN(i) > evT(i)) surplus += (evN(i) - evT(i))
    }
    for (i <- odN.indices) {
      if (odN(i) > odT(i)) surplus += (odN(i) - odT(i))
    }

    surplus / 2
  }
}
```

## Rust

```rust
impl Solution {
    pub fn make_similar(nums: Vec<i32>, target: Vec<i32>) -> i64 {
        let mut even_nums = Vec::new();
        let mut odd_nums = Vec::new();
        for &x in nums.iter() {
            if x % 2 == 0 {
                even_nums.push(x);
            } else {
                odd_nums.push(x);
            }
        }

        let mut even_target = Vec::new();
        let mut odd_target = Vec::new();
        for &x in target.iter() {
            if x % 2 == 0 {
                even_target.push(x);
            } else {
                odd_target.push(x);
            }
        }

        even_nums.sort_unstable();
        even_target.sort_unstable();
        odd_nums.sort_unstable();
        odd_target.sort_unstable();

        let mut total: i64 = 0;
        for (a, b) in even_nums.iter().zip(even_target.iter()) {
            if a > b {
                total += (*a - *b) as i64;
            }
        }
        for (a, b) in odd_nums.iter().zip(odd_target.iter()) {
            if a > b {
                total += (*a - *b) as i64;
            }
        }

        total / 2
    }
}
```

## Racket

```racket
(define/contract (make-similar nums target)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (letrec ((factor-info
            (lambda (x)
              (let loop ((v x) (cnt 0))
                (if (even? v)
                    (loop (/ v 2) (+ cnt 1))
                    (values v cnt))))))
    (define hash-nums (make-hash))
    (define hash-target (make-hash))
    ;; collect exponents for nums
    (for ([x nums])
      (define-values (odd cnt) (factor-info x))
      (hash-update! hash-nums odd (lambda (lst) (cons cnt lst)) '()))
    ;; collect exponents for target
    (for ([x target])
      (define-values (odd cnt) (factor-info x))
      (hash-update! hash-target odd (lambda (lst) (cons cnt lst)) '()))
    ;; compute total difference
    (let ((total-diff 0))
      (for ([key (in-hash-keys hash-nums)])
        (define list1 (sort (hash-ref hash-nums key) <))
        (define list2 (sort (hash-ref hash-target key) <))
        (for ([a (in-list list1)] [b (in-list list2)])
          (set! total-diff (+ total-diff (abs (- a b))))))
      (quotient total-diff 2))))
```

## Erlang

```erlang
-spec make_similar(Nums :: [integer()], Target :: [integer()]) -> integer().
make_similar(Nums, Target) ->
    EvensNum = [X || X <- Nums, X rem 2 == 0],
    OddsNum  = [X || X <- Nums, X rem 2 =/= 0],
    EvensTar = [X || X <- Target, X rem 2 == 0],
    OddsTar  = [X || X <- Target, X rem 2 =/= 0],

    SortedEN = lists:sort(EvensNum),
    SortedET = lists:sort(EvensTar),
    SortedON = lists:sort(OddsNum),
    SortedOT = lists:sort(OddsTar),

    DiffEven = diff_sum(SortedEN, SortedET),
    DiffOdd  = diff_sum(SortedON, SortedOT),

    (DiffEven + DiffOdd) div 4.

diff_sum([], []) -> 0;
diff_sum([H|T], [H2|T2]) ->
    erlang:abs(H - H2) + diff_sum(T, T2).
```

## Elixir

```elixir
defmodule Solution do
  @spec make_similar(nums :: [integer], target :: [integer]) :: integer
  def make_similar(nums, target) do
    {nums_even, nums_odd} = Enum.split_with(nums, fn x -> rem(x, 2) == 0 end)
    {target_even, target_odd} = Enum.split_with(target, fn x -> rem(x, 2) == 0 end)

    surplus =
      compute_surplus(Enum.sort(nums_even), Enum.sort(target_even)) +
      compute_surplus(Enum.sort(nums_odd), Enum.sort(target_odd))

    div(surplus, 2)
  end

  defp compute_surplus(list_a, list_b) do
    Enum.zip(list_a, list_b)
    |> Enum.reduce(0, fn {a, b}, acc ->
      if a > b, do: acc + (a - b), else: acc
    end)
  end
end
```
