# 2815. Max Pair Sum in an Array

## Cpp

```cpp
class Solution {
public:
    int maxSum(vector<int>& nums) {
        // best[d] = {largest, second_largest} for numbers whose max digit is d
        vector<pair<int,int>> best(10, {-1, -1});
        for (int num : nums) {
            int x = num;
            int mx = 0;
            while (x > 0) {
                mx = max(mx, x % 10);
                x /= 10;
            }
            // update top two for digit mx
            if (num > best[mx].first) {
                best[mx].second = best[mx].first;
                best[mx].first = num;
            } else if (num > best[mx].second) {
                best[mx].second = num;
            }
        }
        int ans = -1;
        for (int d = 0; d <= 9; ++d) {
            if (best[d].second != -1) {
                ans = max(ans, best[d].first + best[d].second);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxSum(int[] nums) {
        int[] first = new int[10];
        int[] second = new int[10];
        for (int i = 0; i < 10; i++) {
            first[i] = -1;
            second[i] = -1;
        }
        for (int num : nums) {
            int d = maxDigit(num);
            if (num > first[d]) {
                second[d] = first[d];
                first[d] = num;
            } else if (num > second[d]) {
                second[d] = num;
            }
        }
        int ans = -1;
        for (int d = 0; d < 10; d++) {
            if (second[d] != -1) {
                ans = Math.max(ans, first[d] + second[d]);
            }
        }
        return ans;
    }

    private int maxDigit(int n) {
        int mx = 0;
        while (n > 0) {
            int digit = n % 10;
            if (digit > mx) mx = digit;
            n /= 10;
        }
        return mx;
    }
}
```

## Python

```python
class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def largest_digit(x):
            m = 0
            while x:
                d = x % 10
                if d > m:
                    m = d
                x //= 10
            return m

        top = {}  # digit -> [max1, max2]
        for num in nums:
            d = largest_digit(num)
            if d not in top:
                top[d] = [num, -1]
            else:
                if num > top[d][0]:
                    top[d][1] = top[d][0]
                    top[d][0] = num
                elif num > top[d][1]:
                    top[d][1] = num

        ans = -1
        for max1, max2 in top.values():
            if max2 != -1:
                s = max1 + max2
                if s > ans:
                    ans = s
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        first = [-1] * 10
        second = [-1] * 10
        for num in nums:
            # compute largest digit of num
            m = 0
            x = num
            while x:
                d = x % 10
                if d > m:
                    m = d
                x //= 10
            # update top two values for this digit
            if num > first[m]:
                second[m] = first[m]
                first[m] = num
            elif num > second[m]:
                second[m] = num
        ans = -1
        for d in range(10):
            if second[d] != -1:
                ans = max(ans, first[d] + second[d])
        return ans
```

## C

```c
int maxSum(int* nums, int numsSize) {
    int first[10];
    int second[10];
    for (int i = 0; i < 10; ++i) {
        first[i] = -1;
        second[i] = -1;
    }
    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        int maxDigit = 0;
        while (x > 0) {
            int d = x % 10;
            if (d > maxDigit) maxDigit = d;
            x /= 10;
        }
        if (nums[i] > first[maxDigit]) {
            second[maxDigit] = first[maxDigit];
            first[maxDigit] = nums[i];
        } else if (nums[i] > second[maxDigit]) {
            second[maxDigit] = nums[i];
        }
    }
    int ans = -1;
    for (int d = 0; d < 10; ++d) {
        if (second[d] != -1) {
            int sum = first[d] + second[d];
            if (sum > ans) ans = sum;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSum(int[] nums) {
        int[] first = new int[10];
        int[] second = new int[10];
        for (int i = 0; i < 10; i++) {
            first[i] = -1;
            second[i] = -1;
        }

        foreach (int num in nums) {
            int maxDigit = GetMaxDigit(num);
            if (num > first[maxDigit]) {
                second[maxDigit] = first[maxDigit];
                first[maxDigit] = num;
            } else if (num > second[maxDigit]) {
                second[maxDigit] = num;
            }
        }

        int ans = -1;
        for (int d = 0; d < 10; d++) {
            if (second[d] != -1) {
                ans = Math.Max(ans, first[d] + second[d]);
            }
        }
        return ans;
    }

    private int GetMaxDigit(int n) {
        int max = 0;
        while (n > 0) {
            int digit = n % 10;
            if (digit > max) max = digit;
            n /= 10;
        }
        return max;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSum = function(nums) {
    const top1 = Array(10).fill(-1);
    const top2 = Array(10).fill(-1);
    
    const maxDigit = (num) => {
        let m = 0;
        while (num > 0) {
            const d = num % 10;
            if (d > m) m = d;
            num = Math.floor(num / 10);
        }
        return m;
    };
    
    for (const n of nums) {
        const d = maxDigit(n);
        if (n > top1[d]) {
            top2[d] = top1[d];
            top1[d] = n;
        } else if (n > top2[d]) {
            top2[d] = n;
        }
    }
    
    let ans = -1;
    for (let d = 0; d <= 9; ++d) {
        if (top2[d] !== -1) {
            const sum = top1[d] + top2[d];
            if (sum > ans) ans = sum;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function maxSum(nums: number[]): number {
    const first = new Array(10).fill(-1);
    const second = new Array(10).fill(-1);

    for (const num of nums) {
        let n = num;
        let maxDigit = 0;
        while (n > 0) {
            const d = n % 10;
            if (d > maxDigit) maxDigit = d;
            n = Math.floor(n / 10);
        }

        if (num > first[maxDigit]) {
            second[maxDigit] = first[maxDigit];
            first[maxDigit] = num;
        } else if (num > second[maxDigit]) {
            second[maxDigit] = num;
        }
    }

    let ans = -1;
    for (let d = 0; d <= 9; ++d) {
        if (second[d] !== -1) {
            const sum = first[d] + second[d];
            if (sum > ans) ans = sum;
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
    function maxSum($nums) {
        $top1 = array_fill(0, 10, -1);
        $top2 = array_fill(0, 10, -1);
        foreach ($nums as $num) {
            $d = $this->largestDigit($num);
            if ($num > $top1[$d]) {
                $top2[$d] = $top1[$d];
                $top1[$d] = $num;
            } elseif ($num > $top2[$d]) {
                $top2[$d] = $num;
            }
        }
        $ans = -1;
        for ($i = 0; $i <= 9; $i++) {
            if ($top2[$i] != -1) {
                $sum = $top1[$i] + $top2[$i];
                if ($sum > $ans) {
                    $ans = $sum;
                }
            }
        }
        return $ans;
    }

    private function largestDigit($num) {
        $max = 0;
        while ($num > 0) {
            $digit = $num % 10;
            if ($digit > $max) {
                $max = $digit;
            }
            $num = intdiv($num, 10);
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maxSum(_ nums: [Int]) -> Int {
        var first = Array(repeating: -1, count: 10)
        var second = Array(repeating: -1, count: 10)
        
        for num in nums {
            let d = maxDigit(num)
            if num > first[d] {
                second[d] = first[d]
                first[d] = num
            } else if num > second[d] {
                second[d] = num
            }
        }
        
        var ans = -1
        for i in 0..<10 {
            if second[i] != -1 {
                let sum = first[i] + second[i]
                if sum > ans { ans = sum }
            }
        }
        return ans
    }
    
    private func maxDigit(_ n: Int) -> Int {
        var num = n
        var mx = 0
        while num > 0 {
            let d = num % 10
            if d > mx { mx = d }
            num /= 10
        }
        return mx
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSum(nums: IntArray): Int {
        val first = IntArray(10) { -1 }
        val second = IntArray(10) { -1 }

        for (num in nums) {
            var x = num
            var maxDigit = 0
            while (x > 0) {
                val d = x % 10
                if (d > maxDigit) maxDigit = d
                x /= 10
            }
            if (num > first[maxDigit]) {
                second[maxDigit] = first[maxDigit]
                first[maxDigit] = num
            } else if (num > second[maxDigit]) {
                second[maxDigit] = num
            }
        }

        var ans = -1
        for (d in 0..9) {
            if (second[d] != -1) {
                val sum = first[d] + second[d]
                if (sum > ans) ans = sum
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxSum(List<int> nums) {
    // Arrays to store the largest and second largest numbers for each possible max digit (0-9)
    List<int> first = List.filled(10, -1);
    List<int> second = List.filled(10, -1);

    for (int num in nums) {
      int d = _maxDigit(num);
      if (num > first[d]) {
        second[d] = first[d];
        first[d] = num;
      } else if (num > second[d]) {
        second[d] = num;
      }
    }

    int answer = -1;
    for (int d = 0; d <= 9; ++d) {
      if (second[d] != -1) {
        int sum = first[d] + second[d];
        if (sum > answer) answer = sum;
      }
    }
    return answer;
  }

  int _maxDigit(int num) {
    int maxD = 0;
    while (num > 0) {
      int digit = num % 10;
      if (digit > maxD) maxD = digit;
      num ~/= 10;
    }
    return maxD;
  }
}
```

## Golang

```go
func maxSum(nums []int) int {
	max1 := make([]int, 10)
	max2 := make([]int, 10)
	for i := 0; i < 10; i++ {
		max1[i] = -1
		max2[i] = -1
	}
	for _, num := range nums {
		d := largestDigit(num)
		if num > max1[d] {
			max2[d] = max1[d]
			max1[d] = num
		} else if num > max2[d] {
			max2[d] = num
		}
	}
	ans := -1
	for d := 0; d < 10; d++ {
		if max2[d] != -1 {
			sum := max1[d] + max2[d]
			if sum > ans {
				ans = sum
			}
		}
	}
	return ans
}

func largestDigit(num int) int {
	maxd := 0
	for num > 0 {
		d := num % 10
		if d > maxd {
			maxd = d
		}
		num /= 10
	}
	return maxd
}
```

## Ruby

```ruby
def max_sum(nums)
  buckets = Hash.new { |h, k| h[k] = [] }

  nums.each do |num|
    n = num
    max_digit = 0
    while n > 0
      d = n % 10
      max_digit = d if d > max_digit
      n /= 10
    end

    arr = buckets[max_digit]
    if arr.length < 2
      arr << num
      arr.sort!.reverse!
    else
      if num > arr[1]
        arr[1] = num
        arr.sort!.reverse!
      end
    end
  end

  ans = -1
  buckets.each_value do |arr|
    if arr.length == 2
      sum = arr[0] + arr[1]
      ans = sum if sum > ans
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maxSum(nums: Array[Int]): Int = {
        val first = Array.fill(10)(-1)
        val second = Array.fill(10)(-1)

        def largestDigit(n: Int): Int = {
            var x = n
            var mx = 0
            while (x > 0) {
                val d = x % 10
                if (d > mx) mx = d
                x /= 10
            }
            mx
        }

        for (num <- nums) {
            val d = largestDigit(num)
            if (num > first(d)) {
                second(d) = first(d)
                first(d) = num
            } else if (num > second(d)) {
                second(d) = num
            }
        }

        var ans = -1
        for (d <- 0 to 9) {
            if (second(d) != -1) {
                val sum = first(d) + second(d)
                if (sum > ans) ans = sum
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sum(nums: Vec<i32>) -> i32 {
        fn largest_digit(mut n: i32) -> usize {
            let mut mx = 0;
            while n > 0 {
                let d = n % 10;
                if d > mx {
                    mx = d;
                }
                n /= 10;
            }
            mx as usize
        }

        let mut buckets: Vec<Vec<i32>> = vec![Vec::new(); 10];
        for &num in nums.iter() {
            let d = largest_digit(num);
            buckets[d].push(num);
        }

        let mut ans = -1;
        for bucket in buckets.iter_mut() {
            if bucket.len() >= 2 {
                bucket.sort_unstable_by(|a, b| b.cmp(a));
                let sum = bucket[0] + bucket[1];
                if sum > ans {
                    ans = sum;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(require racket/list)

(define (max-digit n)
  (let loop ((x n) (mx 0))
    (if (= x 0)
        mx
        (let* ((d (remainder x 10))
               (new-mx (if (> d mx) d mx)))
          (loop (quotient x 10) new-mx)))))

(define (update-list lst val)
  (let* ((newlst (cons val lst))
         (sorted (sort newlst >)))
    (if (> (length sorted) 2)
        (take sorted 2)
        sorted)))

(define/contract (max-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ((v (make-vector 10 '())))
    (for-each
     (lambda (num)
       (let* ((d (max-digit num))
              (lst (vector-ref v d))
              (newlst (update-list lst num)))
         (vector-set! v d newlst)))
     nums)
    (let loop ((i 0) (best -1))
      (if (= i 10)
          best
          (let ((lst (vector-ref v i)))
            (if (>= (length lst) 2)
                (let ((sum (+ (first lst) (second lst))))
                  (loop (+ i 1) (max best sum)))
                (loop (+ i 1) best)))))))
```

## Erlang

```erlang
-spec max_sum(Nums :: [integer()]) -> integer().
max_sum(Nums) ->
    Groups = lists:foldl(fun(N, Acc) ->
        D = largest_digit(N),
        Prev = maps:get(D, Acc, []),
        maps:put(D, [N|Prev], Acc)
    end, #{}, Nums),
    Max = maps:fold(fun(_Key, List, CurMax) ->
        case length(List) >= 2 of
            true ->
                SortedDesc = lists:reverse(lists:sort(List)),
                [A,B|_] = SortedDesc,
                Sum = A + B,
                if Sum > CurMax -> Sum; true -> CurMax end;
            false -> CurMax
        end
    end, -1, Groups),
    Max.

largest_digit(N) ->
    Digits = integer_to_list(N),
    lists:max([D - $0 || D <- Digits]).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_sum(nums :: [integer]) :: integer
  def max_sum(nums) do
    groups =
      Enum.reduce(nums, %{}, fn num, acc ->
        d = largest_digit(num)
        Map.update(acc, d, [num], &[num | &1])
      end)

    max_pair_sum =
      groups
      |> Enum.reduce(-1, fn {_digit, list}, best ->
        if length(list) >= 2 do
          sorted = Enum.sort(list, :desc)
          sum = hd(sorted) + Enum.at(sorted, 1)
          if sum > best, do: sum, else: best
        else
          best
        end
      end)

    max_pair_sum
  end

  defp largest_digit(n) do
    n
    |> Integer.digits()
    |> Enum.max()
  end
end
```
