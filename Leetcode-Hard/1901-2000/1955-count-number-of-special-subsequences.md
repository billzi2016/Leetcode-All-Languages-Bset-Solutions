# 1955. Count Number of Special Subsequences

## Cpp

```cpp
class Solution {
public:
    int countSpecialSubsequences(vector<int>& nums) {
        const long long MOD = 1000000007LL;
        long long dp0 = 0, dp01 = 0, dp012 = 0;
        for (int x : nums) {
            if (x == 0) {
                dp0 = (dp0 * 2 + 1) % MOD;
            } else if (x == 1) {
                dp01 = (dp01 * 2 + dp0) % MOD;
            } else { // x == 2
                dp012 = (dp012 * 2 + dp01) % MOD;
            }
        }
        return static_cast<int>(dp012);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int countSpecialSubsequences(int[] nums) {
        long dp0 = 0, dp1 = 0, dp2 = 0;
        for (int x : nums) {
            if (x == 0) {
                dp0 = (dp0 * 2 + 1) % MOD;
            } else if (x == 1) {
                dp1 = (dp1 * 2 + dp0) % MOD;
            } else { // x == 2
                dp2 = (dp2 * 2 + dp1) % MOD;
            }
        }
        return (int) dp2;
    }
}
```

## Python

```python
class Solution(object):
    def countSpecialSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        dp0 = dp1 = dp2 = 0
        for x in nums:
            if x == 0:
                dp0 = (dp0 * 2 + 1) % MOD
            elif x == 1:
                dp1 = (dp1 * 2 + dp0) % MOD
            else:  # x == 2
                dp2 = (dp2 * 2 + dp1) % MOD
        return dp2 % MOD
```

## Python3

```python
class Solution:
    def countSpecialSubsequences(self, nums):
        MOD = 10**9 + 7
        dp0 = dp1 = dp2 = 0
        for x in nums:
            if x == 0:
                dp0 = (dp0 * 2 + 1) % MOD
            elif x == 1:
                dp1 = (dp1 * 2 + dp0) % MOD
            else:  # x == 2
                dp2 = (dp2 * 2 + dp1) % MOD
        return dp2 % MOD
```

## C

```c
#include <stdint.h>

int countSpecialSubsequences(int* nums, int numsSize) {
    const int64_t MOD = 1000000007LL;
    int64_t dp0 = 0, dp1 = 0, dp2 = 0;
    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        if (x == 0) {
            dp0 = (dp0 * 2 + 1) % MOD;
        } else if (x == 1) {
            dp1 = (dp1 * 2 + dp0) % MOD;
        } else { // x == 2
            dp2 = (dp2 * 2 + dp1) % MOD;
        }
    }
    return (int)(dp2 % MOD);
}
```

## Csharp

```csharp
public class Solution {
    private const int MOD = 1000000007;
    public int CountSpecialSubsequences(int[] nums) {
        long dp0 = 0, dp1 = 0, dp2 = 0;
        foreach (int x in nums) {
            if (x == 0) {
                dp0 = (dp0 * 2 + 1) % MOD;
            } else if (x == 1) {
                dp1 = (dp1 * 2 + dp0) % MOD;
            } else { // x == 2
                dp2 = (dp2 * 2 + dp1) % MOD;
            }
        }
        return (int)(dp2 % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countSpecialSubsequences = function(nums) {
    const MOD = 1000000007;
    let dp0 = 0, dp1 = 0, dp2 = 0;
    for (const x of nums) {
        if (x === 0) {
            dp0 = (dp0 * 2 + 1) % MOD;
        } else if (x === 1) {
            dp1 = (dp1 * 2 + dp0) % MOD;
        } else { // x === 2
            dp2 = (dp2 * 2 + dp1) % MOD;
        }
    }
    return dp2;
};
```

## Typescript

```typescript
function countSpecialSubsequences(nums: number[]): number {
    const MOD = 1000000007;
    let dp0 = 0, dp1 = 0, dp2 = 0;
    for (const x of nums) {
        if (x === 0) {
            dp0 = (dp0 * 2 + 1) % MOD;
        } else if (x === 1) {
            dp1 = (dp1 * 2 + dp0) % MOD;
        } else { // x === 2
            dp2 = (dp2 * 2 + dp1) % MOD;
        }
    }
    return dp2;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countSpecialSubsequences($nums) {
        $mod = 1000000007;
        $dp0 = 0; // subsequences of only 0s (at least one)
        $dp1 = 0; // subsequences of 0s then 1s (both positive)
        $dp2 = 0; // subsequences of 0s then 1s then 2s (all positive)

        foreach ($nums as $v) {
            if ($v == 0) {
                $dp0 = ($dp0 * 2 + 1) % $mod;
            } elseif ($v == 1) {
                $dp1 = ($dp1 * 2 + $dp0) % $mod;
            } else { // $v == 2
                $dp2 = ($dp2 * 2 + $dp1) % $mod;
            }
        }

        return $dp2;
    }
}
```

## Swift

```swift
class Solution {
    func countSpecialSubsequences(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        var dp0 = 0
        var dp1 = 0
        var dp2 = 0
        for num in nums {
            if num == 0 {
                dp0 = (dp0 * 2 + 1) % MOD
            } else if num == 1 {
                dp1 = (dp1 * 2 + dp0) % MOD
            } else { // num == 2
                dp2 = (dp2 * 2 + dp1) % MOD
            }
        }
        return dp2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSpecialSubsequences(nums: IntArray): Int {
        val MOD = 1_000_000_007L
        var dp0 = 0L
        var dp1 = 0L
        var dp2 = 0L
        for (v in nums) {
            when (v) {
                0 -> dp0 = (dp0 * 2 + 1) % MOD
                1 -> dp1 = (dp1 * 2 + dp0) % MOD
                2 -> dp2 = (dp2 * 2 + dp1) % MOD
            }
        }
        return dp2.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;
  int countSpecialSubsequences(List<int> nums) {
    int dp0 = 0, dp1 = 0, dp2 = 0;
    for (int x in nums) {
      if (x == 0) {
        dp0 = ((dp0 * 2) % _mod + 1) % _mod;
      } else if (x == 1) {
        dp1 = ((dp1 * 2) % _mod + dp0) % _mod;
      } else { // x == 2
        dp2 = ((dp2 * 2) % _mod + dp1) % _mod;
      }
    }
    return dp2;
  }
}
```

## Golang

```go
func countSpecialSubsequences(nums []int) int {
	const MOD int64 = 1000000007
	var c0, c1, c2 int64
	for _, x := range nums {
		switch x {
		case 0:
			c0 = (c0*2 + 1) % MOD
		case 1:
			c1 = (c1*2 + c0) % MOD
		case 2:
			c2 = (c2*2 + c1) % MOD
		}
	}
	return int(c2)
}
```

## Ruby

```ruby
def count_special_subsequences(nums)
  mod = 1_000_000_007
  dp0 = dp1 = dp2 = 0
  nums.each do |x|
    case x
    when 0
      dp0 = (dp0 * 2 + 1) % mod
    when 1
      dp1 = (dp1 * 2 + dp0) % mod
    when 2
      dp2 = (dp2 * 2 + dp1) % mod
    end
  end
  dp2 % mod
end
```

## Scala

```scala
object Solution {
    def countSpecialSubsequences(nums: Array[Int]): Int = {
        val MOD = 1000000007L
        var dp0 = 0L
        var dp1 = 0L
        var dp2 = 0L
        for (x <- nums) {
            x match {
                case 0 => dp0 = (dp0 * 2 + 1) % MOD
                case 1 => dp1 = (dp1 * 2 + dp0) % MOD
                case 2 => dp2 = (dp2 * 2 + dp1) % MOD
                case _ => // ignore, not possible per constraints
            }
        }
        dp2.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_special_subsequences(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut dp0: i64 = 0;
        let mut dp1: i64 = 0;
        let mut dp2: i64 = 0;
        for &x in nums.iter() {
            match x {
                0 => {
                    dp0 = (dp0 * 2 + 1) % MOD;
                }
                1 => {
                    dp1 = (dp1 * 2 + dp0) % MOD;
                }
                2 => {
                    dp2 = (dp2 * 2 + dp1) % MOD;
                }
                _ => {}
            }
        }
        dp2 as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (count-special-subsequences nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (dp0 0) (dp1 0) (dp2 0))
    (if (null? lst)
        dp2
        (let* ((x (car lst))
               (new-dp0 (if (= x 0)
                           (modulo (+ (* 2 dp0) 1) MOD)
                           dp0))
               (new-dp1 (if (= x 1)
                           (modulo (+ (* 2 dp1) dp0) MOD)
                           dp1))
               (new-dp2 (if (= x 2)
                           (modulo (+ (* 2 dp2) dp1) MOD)
                           dp2)))
          (loop (cdr lst) new-dp0 new-dp1 new-dp2)))))
```

## Erlang

```erlang
-module(solution).
-export([count_special_subsequences/1]).

-define(MOD, 1000000007).

count_special_subsequences(Nums) ->
    {_, _, C} = lists:foldl(
        fun
            (0, {A, B, C}) ->
                NewA = (A * 2 + 1) rem ?MOD,
                {NewA, B, C};
            (1, {A, B, C}) ->
                NewB = (B * 2 + A) rem ?MOD,
                {A, NewB, C};
            (2, {A, B, C}) ->
                NewC = (C * 2 + B) rem ?MOD,
                {A, B, NewC}
        end,
        {0, 0, 0},
        Nums),
    C.
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec count_special_subsequences(nums :: [integer]) :: integer
  def count_special_subsequences(nums) do
    {_, _, dp2} =
      Enum.reduce(nums, {0, 0, 0}, fn x, {dp0, dp1, dp2} ->
        case x do
          0 ->
            new_dp0 = (dp0 * 2 + 1) |> rem(@mod)
            {new_dp0, dp1, dp2}
          1 ->
            new_dp1 = (dp1 * 2 + dp0) |> rem(@mod)
            {dp0, new_dp1, dp2}
          2 ->
            new_dp2 = (dp2 * 2 + dp1) |> rem(@mod)
            {dp0, dp1, new_dp2}
        end
      end)

    dp2
  end
end
```
