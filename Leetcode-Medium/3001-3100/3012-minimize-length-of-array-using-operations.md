# 3012. Minimize Length of Array Using Operations

## Cpp

```cpp
class Solution {
public:
    int minimumArrayLength(vector<int>& nums) {
        int n = nums.size();
        int mn = *min_element(nums.begin(), nums.end());
        int cnt = 0;
        for (int v : nums) if (v == mn) ++cnt;
        if (cnt == 1) return 1;
        for (int v : nums) {
            if (v % mn != 0) return 1;
        }
        return (cnt + 1) / 2; // ceil(cnt/2)
    }
};
```

## Java

```java
class Solution {
    public int minimumArrayLength(int[] nums) {
        int min = Integer.MAX_VALUE;
        for (int v : nums) {
            if (v < min) min = v;
        }
        int cnt = 0;
        for (int v : nums) {
            if (v == min) cnt++;
        }
        if (cnt == 1) return 1;
        for (int v : nums) {
            if (v % min != 0) return 1;
        }
        return (cnt + 1) / 2;
    }
}
```

## Python

```python
class Solution(object):
    def minimumArrayLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = min(nums)
        cnt_min = 0
        has_non_multiple = False
        for v in nums:
            if v == mn:
                cnt_min += 1
            elif v % mn != 0:
                has_non_multiple = True
        if cnt_min == 1 or has_non_multiple:
            return 1
        return (cnt_min + 1) // 2
```

## Python3

```python
class Solution:
    def minimumArrayLength(self, nums):
        mn = min(nums)
        cnt = nums.count(mn)
        if cnt == 1:
            return 1
        for v in nums:
            if v % mn != 0:
                return 1
        return cnt // 2
```

## C

```c
int minimumArrayLength(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int minVal = INT_MAX;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] < minVal) minVal = nums[i];
    }
    int cnt = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == minVal) ++cnt;
    }
    if (cnt == 1) return 1;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] % minVal != 0) return 1;
    }
    return (cnt + 1) / 2;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumArrayLength(int[] nums)
    {
        int min = int.MaxValue;
        foreach (int v in nums)
            if (v < min) min = v;

        int cnt = 0;
        foreach (int v in nums)
            if (v == min) cnt++;

        if (cnt == 1) return 1;

        foreach (int v in nums)
            if (v % min != 0) return 1;

        return cnt / 2;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumArrayLength = function(nums) {
    let minVal = Infinity;
    for (const v of nums) {
        if (v < minVal) minVal = v;
    }
    let cntMin = 0;
    for (const v of nums) {
        if (v === minVal) cntMin++;
    }
    if (cntMin === 1) return 1;
    for (const v of nums) {
        if (v % minVal !== 0) return 1;
    }
    return Math.ceil(cntMin / 2);
};
```

## Typescript

```typescript
function minimumArrayLength(nums: number[]): number {
    let minVal = Infinity;
    for (const v of nums) {
        if (v < minVal) minVal = v;
    }
    let cnt = 0;
    for (const v of nums) {
        if (v === minVal) cnt++;
    }
    if (cnt === 1) return 1;
    for (const v of nums) {
        if (v % minVal !== 0) return 1;
    }
    return Math.ceil(cnt / 2);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumArrayLength($nums) {
        $min = PHP_INT_MAX;
        foreach ($nums as $v) {
            if ($v < $min) {
                $min = $v;
            }
        }

        $cntMin = 0;
        $hasNonDivisible = false;
        foreach ($nums as $v) {
            if ($v == $min) {
                $cntMin++;
            } else {
                if ($v % $min !== 0) {
                    $hasNonDivisible = true;
                }
            }
        }

        if ($cntMin == 1) {
            return 1;
        }
        if ($hasNonDivisible) {
            return 1;
        }
        // all numbers are multiples of min and min appears cntMin times
        return intdiv($cntMin + 1, 2); // ceil(cntMin / 2)
    }
}
```

## Swift

```swift
class Solution {
    func minimumArrayLength(_ nums: [Int]) -> Int {
        guard let minVal = nums.min() else { return 0 }
        var countMin = 0
        var hasNonDivisible = false
        
        for v in nums {
            if v == minVal {
                countMin += 1
            } else if v % minVal != 0 {
                hasNonDivisible = true
            }
        }
        
        if countMin == 1 || hasNonDivisible {
            return 1
        } else {
            return (countMin + 1) / 2
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumArrayLength(nums: IntArray): Int {
        var minVal = Int.MAX_VALUE
        for (v in nums) {
            if (v < minVal) minVal = v
        }
        var cnt = 0
        for (v in nums) {
            if (v == minVal) cnt++
        }
        if (cnt == 1) return 1
        for (v in nums) {
            if (v != minVal && v % minVal != 0) return 1
        }
        return (cnt + 1) / 2
    }
}
```

## Dart

```dart
class Solution {
  int minimumArrayLength(List<int> nums) {
    int minVal = nums[0];
    for (int v in nums) {
      if (v < minVal) minVal = v;
    }
    int cnt = 0;
    bool hasNonDivisible = false;
    for (int v in nums) {
      if (v == minVal) {
        cnt++;
      } else if (v % minVal != 0) {
        hasNonDivisible = true;
      }
    }
    if (cnt == 1) return 1;
    if (hasNonDivisible) return 1;
    int ans = cnt ~/ 2;
    return ans > 0 ? ans : 1;
  }
}
```

## Golang

```go
func minimumArrayLength(nums []int) int {
	minVal := nums[0]
	for _, v := range nums {
		if v < minVal {
			minVal = v
		}
	}
	cnt := 0
	for _, v := range nums {
		if v == minVal {
			cnt++
		}
	}
	if cnt == 1 {
		return 1
	}
	for _, v := range nums {
		if v%minVal != 0 {
			return 1
		}
	}
	return (cnt + 1) / 2
}
```

## Ruby

```ruby
def minimum_array_length(nums)
  min_val = nums.min
  cnt = 0
  has_non_multiple = false

  nums.each do |v|
    if v == min_val
      cnt += 1
    else
      has_non_multiple ||= (v % min_val != 0)
    end
  end

  return 1 if cnt == 1 || has_non_multiple
  (cnt + 1) / 2
end
```

## Scala

```scala
object Solution {
    def minimumArrayLength(nums: Array[Int]): Int = {
        val minVal = nums.min
        var cntMin = 0
        var hasNonMultiple = false
        for (v <- nums) {
            if (v == minVal) cntMin += 1
            else if (v % minVal != 0) hasNonMultiple = true
        }
        if (cntMin == 1) 1
        else if (hasNonMultiple) 1
        else (cntMin + 1) / 2
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_array_length(nums: Vec<i32>) -> i32 {
        let mut min_val = i32::MAX;
        for &v in &nums {
            if v < min_val {
                min_val = v;
            }
        }
        let mut cnt = 0;
        for &v in &nums {
            if v == min_val {
                cnt += 1;
            }
        }
        if cnt == 1 {
            return 1;
        }
        for &v in &nums {
            if v % min_val != 0 {
                return 1;
            }
        }
        ((cnt + 1) / 2) as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-array-length nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((x (apply min nums))
         (cnt (length (filter (lambda (v) (= v x)) nums)))
         (has-non-multiple? (ormap (lambda (y) (not (= (remainder y x) 0))) nums)))
    (cond
      [(= cnt 1) 1]
      [has-non-multiple? 1]
      [else (quotient (+ cnt 1) 2)])))
```

## Erlang

```erlang
-spec minimum_array_length(Nums :: [integer()]) -> integer().
minimum_array_length(Nums) ->
    Min = lists:min(Nums),
    Cnt = count_min(Min, Nums, 0),
    case has_non_multiple(Nums, Min) of
        true -> 1;
        false -> (Cnt + 1) div 2
    end.

count_min(_, [], Acc) -> Acc;
count_min(Min, [H|T], Acc) ->
    NewAcc = if H == Min -> Acc + 1; true -> Acc end,
    count_min(Min, T, NewAcc).

has_non_multiple([], _) -> false;
has_non_multiple([H|T], Min) ->
    if (H rem Min) =/= 0 -> true;
       true -> has_non_multiple(T, Min)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_array_length(nums :: [integer]) :: integer
  def minimum_array_length(nums) do
    min_val = Enum.min(nums)
    cnt_min = Enum.count(nums, fn v -> v == min_val end)

    cond do
      cnt_min == 1 ->
        1

      Enum.any?(nums, fn v -> rem(v, min_val) != 0 end) ->
        1

      true ->
        div(cnt_min + 1, 2)
    end
  end
end
```
