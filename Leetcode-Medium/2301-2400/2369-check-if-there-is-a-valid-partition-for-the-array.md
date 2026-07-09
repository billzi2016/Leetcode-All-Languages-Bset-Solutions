# 2369. Check if There is a Valid Partition For The Array

## Cpp

```cpp
class Solution {
public:
    bool validPartition(vector<int>& nums) {
        int n = nums.size();
        // dp[i] indicates whether first i elements (0..i-1) can be partitioned
        vector<char> dp(n + 1, 0);
        dp[0] = 1;
        for (int i = 2; i <= n; ++i) {
            // check pair of equal numbers
            if (nums[i - 1] == nums[i - 2] && dp[i - 2]) {
                dp[i] = 1;
                continue;
            }
            if (i >= 3) {
                // three equal numbers
                if (nums[i - 1] == nums[i - 2] && nums[i - 2] == nums[i - 3] && dp[i - 3]) {
                    dp[i] = 1;
                    continue;
                }
                // consecutive increasing sequence
                if (nums[i - 1] == nums[i - 2] + 1 && nums[i - 2] == nums[i - 3] + 1 && dp[i - 3]) {
                    dp[i] = 1;
                }
            }
        }
        return dp[n];
    }
};
```

## Java

```java
class Solution {
    public boolean validPartition(int[] nums) {
        int n = nums.length;
        boolean[] dp = new boolean[n + 1];
        dp[0] = true; // empty prefix is valid
        
        for (int i = 2; i <= n; i++) {
            // Check last two equal
            if (dp[i - 2] && nums[i - 1] == nums[i - 2]) {
                dp[i] = true;
            }
            // Check last three conditions
            if (!dp[i] && i >= 3) {
                boolean threeEqual = nums[i - 1] == nums[i - 2] && nums[i - 2] == nums[i - 3];
                boolean consecutive = nums[i - 1] == nums[i - 2] + 1 && nums[i - 2] == nums[i - 3] + 1;
                if (dp[i - 3] && (threeEqual || consecutive)) {
                    dp[i] = true;
                }
            }
        }
        return dp[n];
    }
}
```

## Python

```python
class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(2, n + 1):
            # pair of equal numbers
            if nums[i - 1] == nums[i - 2] and dp[i - 2]:
                dp[i] = True
            # three equal numbers
            if i >= 3 and nums[i - 1] == nums[i - 2] == nums[i - 3] and dp[i - 3]:
                dp[i] = True
            # three consecutive increasing numbers
            if i >= 3 and nums[i - 3] + 1 == nums[i - 2] and nums[i - 2] + 1 == nums[i - 1] and dp[i - 3]:
                dp[i] = True
        return dp[n]
```

## Python3

```python
from typing import List

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(2, n + 1):
            # check pair of equal numbers
            if nums[i - 2] == nums[i - 1] and dp[i - 2]:
                dp[i] = True
            # check triples
            if not dp[i] and i >= 3:
                a, b, c = nums[i - 3], nums[i - 2], nums[i - 1]
                if (a == b == c or (a + 1 == b and b + 1 == c)) and dp[i - 3]:
                    dp[i] = True
        return dp[n]
```

## C

```c
bool validPartition(int* nums, int numsSize) {
    if (numsSize < 2) return false;
    bool *dp = (bool *)malloc((numsSize + 1) * sizeof(bool));
    for (int i = 0; i <= numsSize; ++i) dp[i] = false;
    dp[0] = true;
    for (int i = 2; i <= numsSize; ++i) {
        if (dp[i - 2] && nums[i - 2] == nums[i - 1]) dp[i] = true;
        if (i >= 3) {
            if (dp[i - 3] && nums[i - 3] == nums[i - 2] && nums[i - 2] == nums[i - 1])
                dp[i] = true;
            if (dp[i - 3] && nums[i - 3] + 1 == nums[i - 2] && nums[i - 2] + 1 == nums[i - 1])
                dp[i] = true;
        }
    }
    bool ans = dp[numsSize];
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public bool ValidPartition(int[] nums)
    {
        int n = nums.Length;
        bool[] dp = new bool[n + 1];
        dp[0] = true;

        for (int i = 2; i <= n; i++)
        {
            // Check pair of equal numbers
            if (dp[i - 2] && nums[i - 1] == nums[i - 2])
            {
                dp[i] = true;
                continue;
            }

            if (i >= 3 && dp[i - 3])
            {
                // Three equal numbers
                if (nums[i - 1] == nums[i - 2] && nums[i - 2] == nums[i - 3])
                {
                    dp[i] = true;
                    continue;
                }
                // Consecutive increasing sequence
                if (nums[i - 1] == nums[i - 2] + 1 && nums[i - 2] == nums[i - 3] + 1)
                {
                    dp[i] = true;
                    continue;
                }
            }
        }

        return dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var validPartition = function(nums) {
    const n = nums.length;
    const dp = new Array(n + 1).fill(false);
    dp[0] = true;
    for (let i = 2; i <= n; i++) {
        // Check pair [a, a]
        if (dp[i - 2] && nums[i - 2] === nums[i - 1]) {
            dp[i] = true;
        }
        // Check triple [a, a, a] or [a, a+1, a+2]
        if (!dp[i] && i >= 3 && dp[i - 3]) {
            const a = nums[i - 3], b = nums[i - 2], c = nums[i - 1];
            if (a === b && b === c) {
                dp[i] = true;
            } else if (a + 1 === b && b + 1 === c) {
                dp[i] = true;
            }
        }
    }
    return dp[n];
};
```

## Typescript

```typescript
function validPartition(nums: number[]): boolean {
    const n = nums.length;
    const dp: boolean[] = new Array(n + 1).fill(false);
    dp[0] = true;

    for (let i = 2; i <= n; i++) {
        // Check last two elements are equal
        if (dp[i - 2] && nums[i - 2] === nums[i - 1]) {
            dp[i] = true;
        }

        // Check last three elements
        if (!dp[i] && i >= 3 && dp[i - 3]) {
            const a = nums[i - 3], b = nums[i - 2], c = nums[i - 1];
            if ((a === b && b === c) || (b === a + 1 && c === b + 1)) {
                dp[i] = true;
            }
        }
    }

    return dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function validPartition($nums) {
        $n = count($nums);
        $dp = array_fill(0, $n + 1, false);
        $dp[0] = true;

        for ($i = 2; $i <= $n; $i++) {
            // Pair of equal numbers
            if ($dp[$i - 2] && $nums[$i - 1] === $nums[$i - 2]) {
                $dp[$i] = true;
            }

            if (!$dp[$i] && $i >= 3) {
                // Triple of equal numbers
                if ($dp[$i - 3] && $nums[$i - 1] === $nums[$i - 2] && $nums[$i - 2] === $nums[$i - 3]) {
                    $dp[$i] = true;
                }
                // Consecutive increasing triple
                elseif ($dp[$i - 3] && $nums[$i - 3] + 1 === $nums[$i - 2] && $nums[$i - 2] + 1 === $nums[$i - 1]) {
                    $dp[$i] = true;
                }
            }
        }

        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func validPartition(_ nums: [Int]) -> Bool {
        let n = nums.count
        var dp = Array(repeating: false, count: n + 1)
        dp[0] = true
        
        for i in 2...n {
            // Check a pair of equal numbers
            if dp[i - 2] && nums[i - 2] == nums[i - 1] {
                dp[i] = true
            }
            // Check triples: all equal or consecutive increasing
            if i >= 3 && dp[i - 3] {
                if nums[i - 3] == nums[i - 2] && nums[i - 2] == nums[i - 1] {
                    dp[i] = true
                } else if nums[i - 3] + 1 == nums[i - 2] && nums[i - 2] + 1 == nums[i - 1] {
                    dp[i] = true
                }
            }
        }
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validPartition(nums: IntArray): Boolean {
        val n = nums.size
        val dp = BooleanArray(n + 1)
        dp[0] = true
        for (i in 2..n) {
            if (nums[i - 1] == nums[i - 2] && dp[i - 2]) {
                dp[i] = true
            }
            if (!dp[i] && i >= 3) {
                if (nums[i - 1] == nums[i - 2] && nums[i - 2] == nums[i - 3] && dp[i - 3]) {
                    dp[i] = true
                } else if (nums[i - 3] + 1 == nums[i - 2] && nums[i - 2] + 1 == nums[i - 1] && dp[i - 3]) {
                    dp[i] = true
                }
            }
        }
        return dp[n]
    }
}
```

## Dart

```dart
class Solution {
  bool validPartition(List<int> nums) {
    int n = nums.length;
    List<bool> dp = List.filled(n + 1, false);
    dp[0] = true;

    for (int i = 2; i <= n; ++i) {
      // Pair of equal numbers
      if (dp[i - 2] && nums[i - 2] == nums[i - 1]) {
        dp[i] = true;
      }
      // Triplet of equal numbers
      if (!dp[i] && i >= 3 && dp[i - 3] &&
          nums[i - 3] == nums[i - 2] && nums[i - 2] == nums[i - 1]) {
        dp[i] = true;
      }
      // Triplet of consecutive increasing numbers
      if (!dp[i] && i >= 3 && dp[i - 3] &&
          nums[i - 3] + 1 == nums[i - 2] && nums[i - 2] + 1 == nums[i - 1]) {
        dp[i] = true;
      }
    }

    return dp[n];
  }
}
```

## Golang

```go
func validPartition(nums []int) bool {
	n := len(nums)
	dp := make([]bool, n+1)
	dp[0] = true
	for i := 2; i <= n; i++ {
		if nums[i-2] == nums[i-1] && dp[i-2] {
			dp[i] = true
		}
		if !dp[i] && i >= 3 {
			if nums[i-3] == nums[i-2] && nums[i-2] == nums[i-1] && dp[i-3] {
				dp[i] = true
			} else if nums[i-3]+1 == nums[i-2] && nums[i-2]+1 == nums[i-1] && dp[i-3] {
				dp[i] = true
			}
		}
	}
	return dp[n]
}
```

## Ruby

```ruby
def valid_partition(nums)
  n = nums.length
  dp = Array.new(n + 1, false)
  dp[0] = true

  (2..n).each do |i|
    # Pair of equal numbers
    if dp[i - 2] && nums[i - 2] == nums[i - 1]
      dp[i] = true
    end

    # Triplet of equal numbers
    if i >= 3 && dp[i - 3] && nums[i - 3] == nums[i - 2] && nums[i - 2] == nums[i - 1]
      dp[i] = true
    end

    # Triplet of consecutive increasing numbers
    if i >= 3 && dp[i - 3] && nums[i - 3] + 1 == nums[i - 2] && nums[i - 2] + 1 == nums[i - 1]
      dp[i] = true
    end
  end

  dp[n]
end
```

## Scala

```scala
object Solution {
    def validPartition(nums: Array[Int]): Boolean = {
        val n = nums.length
        val dp = new Array[Boolean](n + 1)
        dp(0) = true
        var i = 2
        while (i <= n) {
            if (nums(i - 1) == nums(i - 2) && dp(i - 2)) {
                dp(i) = true
            }
            if (!dp(i) && i >= 3 && nums(i - 1) == nums(i - 2) && nums(i - 2) == nums(i - 3) && dp(i - 3)) {
                dp(i) = true
            }
            if (!dp(i) && i >= 3 && nums(i - 1) == nums(i - 2) + 1 && nums(i - 2) == nums(i - 3) + 1 && dp(i - 3)) {
                dp(i) = true
            }
            i += 1
        }
        dp(n)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn valid_partition(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut dp = vec![false; n + 1];
        dp[0] = true;
        for i in 2..=n {
            // Pair of equal numbers
            if dp[i - 2] && nums[i - 2] == nums[i - 1] {
                dp[i] = true;
            }
            // Triples
            if !dp[i] && i >= 3 {
                if dp[i - 3]
                    && (nums[i - 3] == nums[i - 2] && nums[i - 2] == nums[i - 1]
                        || nums[i - 3] + 1 == nums[i - 2] && nums[i - 2] + 1 == nums[i - 1])
                {
                    dp[i] = true;
                }
            }
        }
        dp[n]
    }
}
```

## Racket

```racket
(define/contract (valid-partition nums)
  (-> (listof exact-integer?) boolean?)
  (let* ([v (list->vector nums)]
         [n (vector-length v)])
    (let ([dp (make-vector (+ n 1) #f)])
      (vector-set! dp 0 #t)
      (for ([i (in-range 2 (add1 n))])
        (when (or
                (and (vector-ref dp (- i 2))
                     (= (vector-ref v (- i 2)) (vector-ref v (- i 1))))
                (and (>= i 3) (vector-ref dp (- i 3))
                     (let* ([a (vector-ref v (- i 3))]
                            [b (vector-ref v (- i 2))]
                            [c (vector-ref v (- i 1))])
                       (or (and (= a b) (= b c))
                           (and (= (+ a 1) b) (= (+ b 1) c))))))
          (vector-set! dp i #t)))
      (vector-ref dp n))))
```

## Erlang

```erlang
-spec valid_partition(Nums :: [integer()]) -> boolean().
valid_partition(Nums) ->
    N = length(Nums),
    Tuple = list_to_tuple([0|Nums]),
    DP0 = true,
    DP1 = false,
    DP2 = case N >= 2 of
              true -> (element(1, Tuple) =:= element(2, Tuple)) andalso DP0;
              false -> false
          end,
    case N of
        0 -> false;
        1 -> false;
        2 -> DP2;
        _ ->
            loop(3, N, Tuple, DP0, DP1, DP2)
    end.

loop(I, N, Tuple, Dp_i_3, Dp_i_2, Dp_i_1) when I > N ->
    Dp_i_1;
loop(I, N, Tuple, Dp_i_3, Dp_i_2, Dp_i_1) ->
    A = element(I, Tuple),
    B = element(I-1, Tuple),
    C = element(I-2, Tuple),
    Valid = (A =:= B andalso Dp_i_2) orelse
            ((A =:= B andalso B =:= C) andalso Dp_i_3) orelse
            ((A =:= B + 1 andalso B =:= C + 1) andalso Dp_i_3),
    New_dp_i_3 = Dp_i_2,
    New_dp_i_2 = Dp_i_1,
    New_dp_i_1 = Valid,
    loop(I+1, N, Tuple, New_dp_i_3, New_dp_i_2, New_dp_i_1).
```

## Elixir

```elixir
defmodule Solution do
  @spec valid_partition(nums :: [integer]) :: boolean
  def valid_partition(nums) do
    n = length(nums)
    arr = List.to_tuple(nums)

    dp0 = true

    {_, result} =
      Enum.reduce(2..n, {dp0, dp0}, fn i, {dp_im3, dp_im2} ->
        a_i_1 = elem(arr, i - 1)
        a_i_2 = elem(arr, i - 2)

        cur =
          if a_i_1 == a_i_2 and dp_im2 do
            true
          else
            if i >= 3 do
              a_i_3 = elem(arr, i - 3)

              (a_i_1 == a_i_2 && a_i_2 == a_i_3 && dp_im3) ||
                (a_i_3 + 1 == a_i_2 && a_i_2 + 1 == a_i_1 && dp_im3)
            else
              false
            end
          end

        {dp_im2, cur}
      end)

    result
  end
end
```
