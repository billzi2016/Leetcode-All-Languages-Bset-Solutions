# 2562. Find the Array Concatenation Value

## Cpp

```cpp
class Solution {
public:
    long long findTheArrayConcVal(vector<int>& nums) {
        int i = 0, j = (int)nums.size() - 1;
        long long ans = 0;
        while (i <= j) {
            if (i == j) {
                ans += nums[i];
            } else {
                int b = nums[j];
                long long mult = 1;
                int temp = b;
                while (temp > 0) {
                    mult *= 10;
                    temp /= 10;
                }
                ans += (long long)nums[i] * mult + b;
            }
            ++i;
            --j;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long findTheArrayConcVal(int[] nums) {
        int n = nums.length;
        long total = 0L;
        int left = 0, right = n - 1;
        // precompute powers of 10 up to 5 digits (since nums[i] <= 10000)
        long[] pow10 = new long[6];
        pow10[0] = 1;
        for (int i = 1; i < pow10.length; i++) {
            pow10[i] = pow10[i - 1] * 10L;
        }
        while (left < right) {
            int a = nums[left];
            int b = nums[right];
            // compute number of digits in b
            int len = 0;
            int temp = b;
            do {
                len++;
                temp /= 10;
            } while (temp > 0);
            long concat = ((long) a) * pow10[len] + b;
            total += concat;
            left++;
            right--;
        }
        if (left == right) {
            total += nums[left];
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        total = 0
        while i < j:
            total += int(str(nums[i]) + str(nums[j]))
            i += 1
            j -= 1
        if i == j:
            total += nums[i]
        return total
```

## Python3

```python
class Solution:
    def findTheArrayConcVal(self, nums):
        i, j = 0, len(nums) - 1
        total = 0
        while i < j:
            total += int(str(nums[i]) + str(nums[j]))
            i += 1
            j -= 1
        if i == j:
            total += nums[i]
        return total
```

## C

```c
long long findTheArrayConcVal(int* nums, int numsSize) {
    long long result = 0;
    int left = 0, right = numsSize - 1;
    while (left < right) {
        int a = nums[left];
        int b = nums[right];
        int pow10 = 1;
        int temp = b;
        while (temp > 0) {
            pow10 *= 10;
            temp /= 10;
        }
        result += (long long)a * pow10 + b;
        left++;
        right--;
    }
    if (left == right) {
        result += nums[left];
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public long FindTheArrayConcVal(int[] nums) {
        long total = 0;
        int left = 0, right = nums.Length - 1;
        while (left < right) {
            int a = nums[left];
            int b = nums[right];
            long mult = 1;
            int temp = b;
            while (temp > 0) {
                mult *= 10;
                temp /= 10;
            }
            total += (long)a * mult + b;
            left++;
            right--;
        }
        if (left == right) {
            total += nums[left];
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findTheArrayConcVal = function(nums) {
    let left = 0, right = nums.length - 1;
    let result = 0;
    while (left < right) {
        const concat = Number(String(nums[left]) + String(nums[right]));
        result += concat;
        left++;
        right--;
    }
    if (left === right) {
        result += nums[left];
    }
    return result;
};
```

## Typescript

```typescript
function findTheArrayConcVal(nums: number[]): number {
    let i = 0;
    let j = nums.length - 1;
    let total = 0;
    while (i < j) {
        const concatNum = Number(String(nums[i]) + String(nums[j]));
        total += concatNum;
        i++;
        j--;
    }
    if (i === j) {
        total += nums[i];
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findTheArrayConcVal($nums) {
        $ans = 0;
        $i = 0;
        $j = count($nums) - 1;
        while ($i < $j) {
            $a = $nums[$i];
            $b = $nums[$j];
            $digits = strlen((string)$b);
            $concat = $a * (int)pow(10, $digits) + $b;
            $ans += $concat;
            $i++;
            $j--;
        }
        if ($i == $j) {
            $ans += $nums[$i];
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func findTheArrayConcVal(_ nums: [Int]) -> Int {
        var left = 0
        var right = nums.count - 1
        var result = 0
        while left <= right {
            if left == right {
                result += nums[left]
            } else {
                let a = nums[left]
                let b = nums[right]
                var mul = 1
                var temp = b
                while temp > 0 {
                    mul *= 10
                    temp /= 10
                }
                result += a * mul + b
            }
            left += 1
            right -= 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findTheArrayConcVal(nums: IntArray): Long {
        var i = 0
        var j = nums.size - 1
        var result = 0L
        while (i <= j) {
            if (i == j) {
                result += nums[i].toLong()
            } else {
                val last = nums[j]
                var mult = 10L
                while (mult <= last) {
                    mult *= 10
                }
                val concat = nums[i].toLong() * mult + last
                result += concat
            }
            i++
            j--
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int findTheArrayConcVal(List<int> nums) {
    int i = 0;
    int j = nums.length - 1;
    int ans = 0;
    while (i <= j) {
      if (i == j) {
        ans += nums[i];
      } else {
        int b = nums[j];
        int mul = 1;
        while (mul <= b) {
          mul *= 10;
        }
        ans += nums[i] * mul + b;
      }
      i++;
      j--;
    }
    return ans;
  }
}
```

## Golang

```go
func findTheArrayConcVal(nums []int) int64 {
	var total int64
	i, j := 0, len(nums)-1
	for i < j {
		b := nums[j]
		pow := 1
		for t := b; t > 0; t /= 10 {
			pow *= 10
		}
		total += int64(nums[i])*int64(pow) + int64(b)
		i++
		j--
	}
	if i == j {
		total += int64(nums[i])
	}
	return total
}
```

## Ruby

```ruby
def find_the_array_conc_val(nums)
  i = 0
  j = nums.length - 1
  total = 0
  while i <= j
    if i == j
      total += nums[i]
    else
      b = nums[j]
      mul = 1
      while mul <= b
        mul *= 10
      end
      total += nums[i] * mul + b
    end
    i += 1
    j -= 1
  end
  total
end
```

## Scala

```scala
object Solution {
    def findTheArrayConcVal(nums: Array[Int]): Long = {
        var left = 0
        var right = nums.length - 1
        var ans: Long = 0L

        while (left <= right) {
            if (left == right) {
                ans += nums(left)
            } else {
                val a = nums(left).toLong
                val b = nums(right)

                var d = 0
                var temp = b
                while (temp > 0) {
                    d += 1
                    temp /= 10
                }

                var pow: Long = 1L
                var i = 0
                while (i < d) {
                    pow *= 10
                    i += 1
                }

                ans += a * pow + b
            }
            left += 1
            right -= 1
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_the_array_conc_val(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut ans: i64 = 0;
        let mut left = 0usize;
        let mut right = n - 1;
        while left < right {
            let a = nums[left] as i64;
            let b = nums[right] as i64;

            // compute 10^{digits(b)}
            let mut temp = nums[right];
            let mut pow: i64 = 1;
            while temp > 0 {
                pow *= 10;
                temp /= 10;
            }

            ans += a * pow + b;
            left += 1;
            right -= 1;
        }
        if left == right {
            ans += nums[left] as i64;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (find-the-array-conc-val nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v)))
    (let loop ((i 0) (j (- n 1)) (sum 0))
      (cond
        [(> i j) sum]
        [(= i j) (+ sum (vector-ref v i))]
        [else
         (let* ((a (vector-ref v i))
                (b (vector-ref v j))
                (concat-val (+ (* a (expt 10 (string-length (number->string b)))) b)))
           (loop (+ i 1) (- j 1) (+ sum concat-val)))]))))
```

## Erlang

```erlang
-spec find_the_array_conc_val(Nums :: [integer()]) -> integer().
find_the_array_conc_val(Nums) ->
    process(Nums, 0).

process([], Acc) -> Acc;
process([X], Acc) -> Acc + X;
process(List, Acc) ->
    Len = length(List),
    First = hd(List),
    Last = lists:last(List),
    Concat = First * pow10(digits(Last)) + Last,
    NewList = if
        Len > 2 -> lists:sublist(List, 2, Len - 2);
        true -> []
    end,
    process(NewList, Acc + Concat).

digits(N) when N < 10 -> 1;
digits(N) -> 1 + digits(N div 10).

pow10(0) -> 1;
pow10(N) when N > 0 -> 10 * pow10(N - 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_the_array_conc_val(nums :: [integer]) :: integer
  def find_the_array_conc_val(nums) do
    len = length(nums)

    Enum.reduce(0..div(len - 1, 2), 0, fn k, acc ->
      i = k
      j = len - 1 - k

      if i == j do
        acc + Enum.at(nums, i)
      else
        a = Enum.at(nums, i)
        b = Enum.at(nums, j)

        concat =
          Integer.to_string(a) <> Integer.to_string(b)
          |> String.to_integer()

        acc + concat
      end
    end)
  end
end
```
