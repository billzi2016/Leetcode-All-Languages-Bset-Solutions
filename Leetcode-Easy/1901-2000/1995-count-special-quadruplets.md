# 1995. Count Special Quadruplets

## Cpp

```cpp
class Solution {
public:
    int countQuadruplets(vector<int>& nums) {
        int n = nums.size();
        long long ans = 0;
        unordered_map<int,int> sumCount;
        // prepopulate with the first possible pair (0,1)
        if (n >= 3) {
            sumCount[nums[0] + nums[1]] = 1;
        }
        for (int c = 2; c < n - 1; ++c) {
            // count valid quadruplets with current c as third index
            for (int d = c + 1; d < n; ++d) {
                int need = nums[d] - nums[c];
                auto it = sumCount.find(need);
                if (it != sumCount.end()) ans += it->second;
            }
            // add pairs where the second index is current c for future iterations
            for (int i = 0; i < c; ++i) {
                ++sumCount[nums[i] + nums[c]];
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int countQuadruplets(int[] nums) {
        int n = nums.length;
        int ans = 0;
        for (int d = 3; d < n; ++d) {
            java.util.HashMap<Integer, Integer> cnt = new java.util.HashMap<>();
            for (int c = 2; c < d; ++c) {
                int target = nums[d] - nums[c];
                ans += cnt.getOrDefault(target, 0);
                for (int a = 0; a < c; ++a) {
                    int sum = nums[a] + nums[c];
                    cnt.put(sum, cnt.getOrDefault(sum, 0) + 1);
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for a in range(n - 3):
            for b in range(a + 1, n - 2):
                for c in range(b + 1, n - 1):
                    s = nums[a] + nums[b] + nums[c]
                    for d in range(c + 1, n):
                        if s == nums[d]:
                            ans += 1
        return ans
```

## Python3

```python
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    target = nums[a] + nums[b] + nums[c]
                    for d in range(c + 1, n):
                        if nums[d] == target:
                            ans += 1
        return ans
```

## C

```c
#include <string.h>

int countQuadruplets(int* nums, int numsSize) {
    int ans = 0;
    int cnt[201];
    for (int d = 3; d < numsSize; ++d) {
        memset(cnt, 0, sizeof(cnt));
        for (int c = d - 1; c >= 2; --c) {
            int b = c - 1;
            for (int a = 0; a < b; ++a) {
                int sum = nums[a] + nums[b];
                cnt[sum]++;
            }
            int target = nums[d] - nums[c];
            if (target >= 0 && target <= 200) {
                ans += cnt[target];
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int CountQuadruplets(int[] nums) {
        int n = nums.Length;
        var sumCount = new Dictionary<int, int>();
        int result = 0;

        for (int d = 3; d < n; d++) {
            // iterate c from d-1 down to 2
            for (int c = d - 1; c >= 2; c--) {
                int need = nums[d] - nums[c];
                if (sumCount.TryGetValue(need, out int cnt)) {
                    result += cnt;
                }
                // after checking this c, add sums with current c for future smaller c
                for (int a = 0; a < c; a++) {
                    int s = nums[a] + nums[c];
                    if (sumCount.ContainsKey(s))
                        sumCount[s]++;
                    else
                        sumCount[s] = 1;
                }
            }
            // clear map for next d iteration
            sumCount.Clear();
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countQuadruplets = function(nums) {
    const n = nums.length;
    const maxSum = 200; // since nums[i] <= 100
    const cnt = new Array(maxSum + 1).fill(0);
    let ans = 0;

    for (let c = 2; c <= n - 2; ++c) {
        // count valid (a,b,c,d) with current c as the third index
        for (let d = c + 1; d < n; ++d) {
            const need = nums[d] - nums[c];
            if (need >= 0 && need <= maxSum) {
                ans += cnt[need];
            }
        }
        // add pairs (a,c) to the hashmap for future larger c
        for (let a = 0; a < c; ++a) {
            const sum = nums[a] + nums[c];
            if (sum <= maxSum) {
                cnt[sum]++;
            }
        }
    }

    return ans;
};
```

## Typescript

```typescript
function countQuadruplets(nums: number[]): number {
    const n = nums.length;
    let ans = 0;
    for (let a = 0; a < n - 3; ++a) {
        for (let b = a + 1; b < n - 2; ++b) {
            for (let c = b + 1; c < n - 1; ++c) {
                const sum = nums[a] + nums[b] + nums[c];
                for (let d = c + 1; d < n; ++d) {
                    if (sum === nums[d]) ++ans;
                }
            }
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countQuadruplets($nums) {
        $n = count($nums);
        $sumCount = [];
        $ans = 0;
        for ($c = 2; $c <= $n - 2; $c++) {
            // add all pairs (a, b) where b == $c-1 and a < b
            $b = $c - 1;
            for ($a = 0; $a < $b; $a++) {
                $s = $nums[$a] + $nums[$b];
                if (!isset($sumCount[$s])) {
                    $sumCount[$s] = 0;
                }
                $sumCount[$s]++;
            }
            // check all possible d > c
            for ($d = $c + 1; $d < $n; $d++) {
                $target = $nums[$d] - $nums[$c];
                if (isset($sumCount[$target])) {
                    $ans += $sumCount[$target];
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countQuadruplets(_ nums: [Int]) -> Int {
        let n = nums.count
        var answer = 0
        for d in 3..<n {
            var sumCount = [Int: Int]()
            // c ranges from 2 to d-1 inclusive
            for c in 2...d-1 {
                let j = c - 1
                if j >= 1 {
                    for i in 0..<j {
                        let s = nums[i] + nums[j]
                        sumCount[s, default: 0] += 1
                    }
                }
                let target = nums[d] - nums[c]
                if let cnt = sumCount[target] {
                    answer += cnt
                }
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countQuadruplets(nums: IntArray): Int {
        var ans = 0
        val n = nums.size
        for (d in 3 until n) {
            val sumCount = HashMap<Int, Int>()
            // initialize with the only possible pair before c starts (indices 0 and 1)
            val firstSum = nums[0] + nums[1]
            sumCount[firstSum] = (sumCount[firstSum] ?: 0) + 1
            for (c in 2 until d) {
                val need = nums[d] - nums[c]
                ans += sumCount[need] ?: 0
                // add pairs where the second index is c for future iterations
                for (a in 0 until c) {
                    val s = nums[a] + nums[c]
                    sumCount[s] = (sumCount[s] ?: 0) + 1
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countQuadruplets(List<int> nums) {
    int n = nums.length;
    int ans = 0;
    for (int a = 0; a < n - 3; ++a) {
      for (int b = a + 1; b < n - 2; ++b) {
        for (int c = b + 1; c < n - 1; ++c) {
          int sum = nums[a] + nums[b] + nums[c];
          for (int d = c + 1; d < n; ++d) {
            if (sum == nums[d]) ans++;
          }
        }
      }
    }
    return ans;
  }
}
```

## Golang

```go
func countQuadruplets(nums []int) int {
    n := len(nums)
    if n < 4 {
        return 0
    }
    sumCount := make(map[int]int)
    sumCount[nums[0]+nums[1]] = 1
    ans := 0
    for c := 2; c < n-1; c++ {
        for d := c + 1; d < n; d++ {
            need := nums[d] - nums[c]
            if cnt, ok := sumCount[need]; ok {
                ans += cnt
            }
        }
        for a := 0; a < c; a++ {
            s := nums[a] + nums[c]
            sumCount[s]++
        }
    }
    return ans
}
```

## Ruby

```ruby
def count_quadruplets(nums)
  n = nums.length
  freq = Array.new(101, 0)
  ans = 0

  (n - 2).downto(2) do |k|
    freq[nums[k + 1]] += 1
    i = 0
    while i < k - 1
      j = i + 1
      while j < k
        sum = nums[i] + nums[j] + nums[k]
        ans += freq[sum] if sum <= 100
        j += 1
      end
      i += 1
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countQuadruplets(nums: Array[Int]): Int = {
        import scala.collection.mutable
        val n = nums.length
        var ans = 0
        for (d <- 3 until n) {
            val cnt = mutable.Map[Int, Int]().withDefaultValue(0)
            for (c <- 2 until d) {
                val b = c - 1
                for (a <- 0 until b) {
                    val sum = nums(a) + nums(b)
                    cnt(sum) = cnt(sum) + 1
                }
                val target = nums(d) - nums(c)
                ans += cnt.getOrElse(target, 0)
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_quadruplets(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0i32;
        for a in 0..n - 3 {
            for b in a + 1..n - 2 {
                for c in b + 1..n - 1 {
                    let sum = nums[a] + nums[b] + nums[c];
                    for d in c + 1..n {
                        if sum == nums[d] {
                            ans += 1;
                        }
                    }
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (count-quadruplets nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (arr (list->vector nums)))
    (let loop-d ((d 3) (ans 0))
      (if (>= d n)
          ans
          (let ((sumCount (make-hash)))
            (let inner-c ((c (- d 1)) (cur ans))
              (if (< c 2)
                  (loop-d (+ d 1) cur)
                  (let* ((target (- (vector-ref arr d) (vector-ref arr c)))
                         (cnt (hash-ref sumCount target 0))
                         (new-ans (+ cur cnt)))
                    ;; add pairs (a, c) for future smaller c
                    (for ([a (in-range 0 c)])
                      (let ((s (+ (vector-ref arr a) (vector-ref arr c))))
                        (hash-set! sumCount s (+ 1 (hash-ref sumCount s 0)))))
                    (inner-c (- c 1) new-ans)))))))))
```

## Erlang

```erlang
-module(solution).
-export([count_quadruplets/1]).
-spec count_quadruplets(Nums :: [integer()]) -> integer().
count_quadruplets(Nums) ->
    Tuple = list_to_tuple(Nums),
    N = tuple_size(Tuple),
    length([true ||
        A <- lists:seq(1, N-3),
        B <- lists:seq(A+1, N-2),
        C <- lists:seq(B+1, N-1),
        D <- lists:seq(C+1, N),
        element(A, Tuple) + element(B, Tuple) + element(C, Tuple) =:= element(D, Tuple)
    ]).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_quadruplets(nums :: [integer]) :: integer
  def count_quadruplets(nums) do
    t = List.to_tuple(nums)
    n = tuple_size(t)

    0..(n - 4)
    |> Enum.reduce(0, fn a, acc_a ->
      (a + 1)..(n - 3)
      |> Enum.reduce(acc_a, fn b, acc_b ->
        (b + 1)..(n - 2)
        |> Enum.reduce(acc_b, fn c, acc_c ->
          sum = elem(t, a) + elem(t, b) + elem(t, c)

          cnt =
            ((c + 1)..(n - 1))
            |> Enum.count(fn d -> elem(t, d) == sum end)

          acc_c + cnt
        end)
      end)
    end)
  end
end
```
