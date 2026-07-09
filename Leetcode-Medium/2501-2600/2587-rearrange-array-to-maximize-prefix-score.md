# 2587. Rearrange Array to Maximize Prefix Score

## Cpp

```cpp
class Solution {
public:
    int maxScore(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());
        long long sum = 0;
        int score = 0;
        for (int x : nums) {
            sum += x;
            if (sum > 0) ++score;
            else break; // further sums will not become positive as remaining numbers are <= current
        }
        return score;
    }
};
```

## Java

```java
class Solution {
    public int maxScore(int[] nums) {
        java.util.Arrays.sort(nums);
        long sum = 0;
        int score = 0;
        for (int i = nums.length - 1; i >= 0; --i) {
            sum += nums[i];
            if (sum > 0) {
                ++score;
            } else {
                break;
            }
        }
        return score;
    }
}
```

## Python

```python
class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        prefix = 0
        score = 0
        for v in nums:
            prefix += v
            if prefix > 0:
                score += 1
            else:
                # once prefix becomes non‑positive, further additions (which are <= current element)
                # cannot make it positive again because we are adding numbers that are
                # less than or equal to the current one (sorted descending).
                # However, there might be zeros later; they won't increase prefix.
                # So we can break early for efficiency.
                break
        return score
```

## Python3

```python
class Solution:
    def maxScore(self, nums):
        nums.sort(reverse=True)
        total = 0
        score = 0
        for x in nums:
            total += x
            if total > 0:
                score += 1
        return score
```

## C

```c
#include <stdlib.h>

static int cmp_desc(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return vb - va;  // descending order
}

int maxScore(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    qsort(nums, numsSize, sizeof(int), cmp_desc);
    long long sum = 0;
    int score = 0;
    for (int i = 0; i < numsSize; ++i) {
        sum += nums[i];
        if (sum > 0)
            ++score;
        else
            break;
    }
    return score;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxScore(int[] nums) {
        System.Array.Sort(nums);
        long sum = 0;
        int score = 0;
        for (int i = nums.Length - 1; i >= 0; i--) {
            sum += nums[i];
            if (sum > 0) {
                score++;
            } else {
                break;
            }
        }
        return score;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxScore = function(nums) {
    nums.sort((a, b) => b - a);
    let sum = 0;
    let score = 0;
    for (const v of nums) {
        sum += v;
        if (sum > 0) {
            ++score;
        } else {
            break;
        }
    }
    return score;
};
```

## Typescript

```typescript
function maxScore(nums: number[]): number {
    nums.sort((a, b) => b - a);
    let sum = 0;
    let score = 0;
    for (const v of nums) {
        sum += v;
        if (sum > 0) score++;
    }
    return score;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxScore($nums) {
        rsort($nums);
        $sum = 0;
        $cnt = 0;
        foreach ($nums as $v) {
            $sum += $v;
            if ($sum > 0) {
                $cnt++;
            } else {
                break;
            }
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func maxScore(_ nums: [Int]) -> Int {
        let sorted = nums.sorted(by: >)
        var sum = 0
        var count = 0
        for value in sorted {
            sum += value
            if sum > 0 {
                count += 1
            } else {
                break
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxScore(nums: IntArray): Int {
        val sorted = nums.sortedArrayDescending()
        var sum = 0L
        var count = 0
        for (v in sorted) {
            sum += v.toLong()
            if (sum > 0) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int maxScore(List<int> nums) {
    nums.sort((a, b) => b - a);
    int sum = 0;
    int score = 0;
    for (int v in nums) {
      sum += v;
      if (sum > 0) {
        score++;
      } else {
        break;
      }
    }
    return score;
  }
}
```

## Golang

```go
func maxScore(nums []int) int {
    // Sort nums in decreasing order
    sort.Slice(nums, func(i, j int) bool {
        return nums[i] > nums[j]
    })
    var sum int64
    count := 0
    for _, v := range nums {
        sum += int64(v)
        if sum > 0 {
            count++
        }
    }
    return count
}
```

## Ruby

```ruby
def max_score(nums)
  nums.sort!.reverse!
  sum = 0
  score = 0
  nums.each do |v|
    sum += v
    break if sum <= 0
    score += 1
  end
  score
end
```

## Scala

```scala
object Solution {
  def maxScore(nums: Array[Int]): Int = {
    val sorted = nums.sorted(Ordering[Int].reverse)
    var sum: Long = 0L
    var count = 0
    for (v <- sorted) {
      sum += v
      if (sum > 0) count += 1
    }
    count
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_score(mut nums: Vec<i32>) -> i32 {
        nums.sort_by(|a, b| b.cmp(a));
        let mut sum: i64 = 0;
        let mut count: i32 = 0;
        for v in nums {
            sum += v as i64;
            if sum > 0 {
                count += 1;
            } else {
                break;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (max-score nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((sorted (sort nums >)))
    (let loop ((lst sorted) (sum 0) (cnt 0))
      (if (null? lst)
          cnt
          (let* ((new-sum (+ sum (car lst)))
                 (new-cnt (if (> new-sum 0) (add1 cnt) cnt)))
            (loop (cdr lst) new-sum new-cnt))))))
```

## Erlang

```erlang
-spec max_score(Nums :: [integer()]) -> integer().
max_score(Nums) ->
    Sorted = lists:reverse(lists:sort(Nums)),
    max_score_sorted(Sorted, 0, 0).

max_score_sorted([], _Sum, Count) ->
    Count;
max_score_sorted([H|T], Sum, Count) ->
    NewSum = Sum + H,
    if
        NewSum > 0 -> max_score_sorted(T, NewSum, Count + 1);
        true       -> Count
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_score(nums :: [integer]) :: integer
  def max_score(nums) do
    nums
    |> Enum.sort(&>=/2)
    |> Enum.reduce_while({0, 0}, fn x, {sum, cnt} ->
      new_sum = sum + x

      if new_sum > 0 do
        {:cont, {new_sum, cnt + 1}}
      else
        {:halt, {new_sum, cnt}}
      end
    end)
    |> elem(1)
  end
end
```
