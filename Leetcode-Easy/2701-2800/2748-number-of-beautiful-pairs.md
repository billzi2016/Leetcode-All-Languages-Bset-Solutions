# 2748. Number of Beautiful Pairs

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countBeautifulPairs(vector<int>& nums) {
        auto firstDigit = [](int x) {
            while (x >= 10) x /= 10;
            return x;
        };
        int n = nums.size();
        vector<int> first(n), last(n);
        for (int i = 0; i < n; ++i) {
            first[i] = firstDigit(nums[i]);
            last[i] = nums[i] % 10;
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (std::gcd(first[i], last[j]) == 1) ++ans;
            }
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int countBeautifulPairs(int[] nums) {
        int n = nums.length;
        int count = 0;
        for (int i = 0; i < n; i++) {
            int first = firstDigit(nums[i]);
            for (int j = i + 1; j < n; j++) {
                int last = nums[j] % 10;
                if (gcd(first, last) == 1) {
                    count++;
                }
            }
        }
        return count;
    }

    private int firstDigit(int num) {
        while (num >= 10) {
            num /= 10;
        }
        return num;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int tmp = a % b;
            a = b;
            b = tmp;
        }
        return a;
    }
}
```

## Python

```python
import math

class Solution(object):
    def countBeautifulPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Precompute first and last digits
        first_digits = []
        last_digits = []
        for num in nums:
            last = num % 10
            first = num
            while first >= 10:
                first //= 10
            first_digits.append(first)
            last_digits.append(last)

        count = 0
        for i in range(n):
            fi = first_digits[i]
            for j in range(i + 1, n):
                lj = last_digits[j]
                if math.gcd(fi, lj) == 1:
                    count += 1
        return count
```

## Python3

```python
from typing import List
import math

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        first_digits = []
        last_digits = []
        for num in nums:
            # last digit (non-zero per constraints)
            last_digits.append(num % 10)
            # first digit
            x = num
            while x >= 10:
                x //= 10
            first_digits.append(x)

        count = 0
        for i in range(n):
            fi = first_digits[i]
            for j in range(i + 1, n):
                lj = last_digits[j]
                if math.gcd(fi, lj) == 1:
                    count += 1
        return count
```

## C

```c
int gcd(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int firstDigit(int x) {
    while (x >= 10) x /= 10;
    return x;
}

int countBeautifulPairs(int* nums, int numsSize) {
    int first[100];
    int last[100];
    for (int i = 0; i < numsSize; ++i) {
        first[i] = firstDigit(nums[i]);
        last[i] = nums[i] % 10;
    }
    int ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        for (int j = i + 1; j < numsSize; ++j) {
            if (gcd(first[i], last[j]) == 1) ++ans;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int CountBeautifulPairs(int[] nums) {
        int n = nums.Length;
        int count = 0;
        for (int i = 0; i < n; i++) {
            int first = GetFirstDigit(nums[i]);
            for (int j = i + 1; j < n; j++) {
                int last = nums[j] % 10;
                if (Gcd(first, last) == 1) count++;
            }
        }
        return count;
    }

    private int GetFirstDigit(int num) {
        while (num >= 10) num /= 10;
        return num;
    }

    private int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countBeautifulPairs = function(nums) {
    const firstDigits = nums.map(n => {
        while (n >= 10) n = Math.floor(n / 10);
        return n;
    });
    
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    
    let count = 0;
    const n = nums.length;
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            const lastDigit = nums[j] % 10;
            if (gcd(firstDigits[i], lastDigit) === 1) {
                count++;
            }
        }
    }
    return count;
};
```

## Typescript

```typescript
function countBeautifulPairs(nums: number[]): number {
    const firstDigits = nums.map(num => {
        while (num >= 10) num = Math.floor(num / 10);
        return num;
    });
    const lastDigits = nums.map(num => num % 10);
    let ans = 0;
    const n = nums.length;
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            if (gcd(firstDigits[i], lastDigits[j]) === 1) ans++;
        }
    }
    return ans;

    function gcd(a: number, b: number): number {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
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
    function countBeautifulPairs($nums) {
        $n = count($nums);
        $count = 0;
        for ($i = 0; $i < $n - 1; ++$i) {
            // get first digit of nums[i]
            $first = $nums[$i];
            while ($first >= 10) {
                $first = intdiv($first, 10);
            }
            for ($j = $i + 1; $j < $n; ++$j) {
                $last = $nums[$j] % 10;
                if ($this->gcd($first, $last) == 1) {
                    ++$count;
                }
            }
        }
        return $count;
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }
}
```

## Swift

```swift
class Solution {
    func countBeautifulPairs(_ nums: [Int]) -> Int {
        let n = nums.count
        var first = [Int](repeating: 0, count: n)
        var last = [Int](repeating: 0, count: n)
        for i in 0..<n {
            var x = nums[i]
            while x >= 10 { x /= 10 }
            first[i] = x
            last[i] = nums[i] % 10
        }
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 {
                let t = a % b
                a = b
                b = t
            }
            return a
        }
        var ans = 0
        for i in 0..<n {
            for j in (i + 1)..<n {
                if gcd(first[i], last[j]) == 1 {
                    ans += 1
                }
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countBeautifulPairs(nums: IntArray): Int {
        val n = nums.size
        val first = IntArray(n)
        val last = IntArray(n)
        for (i in 0 until n) {
            var x = nums[i]
            while (x >= 10) {
                x /= 10
            }
            first[i] = x
            last[i] = nums[i] % 10
        }
        var ans = 0
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (gcd(first[i], last[j]) == 1) ans++
            }
        }
        return ans
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return kotlin.math.abs(x)
    }
}
```

## Dart

```dart
class Solution {
  int countBeautifulPairs(List<int> nums) {
    int n = nums.length;
    List<int> firstDigits = List.filled(n, 0);
    List<int> lastDigits = List.filled(n, 0);

    for (int i = 0; i < n; i++) {
      int x = nums[i];
      lastDigits[i] = x % 10;
      while (x >= 10) {
        x ~/= 10;
      }
      firstDigits[i] = x;
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        if (_gcd(firstDigits[i], lastDigits[j]) == 1) {
          count++;
        }
      }
    }
    return count;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int temp = a % b;
      a = b;
      b = temp;
    }
    return a;
  }
}
```

## Golang

```go
func countBeautifulPairs(nums []int) int {
	first := make([]int, len(nums))
	last := make([]int, len(nums))
	for i, v := range nums {
		x := v
		for x >= 10 {
			x /= 10
		}
		first[i] = x
		last[i] = v % 10
	}
	ans := 0
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if gcd(first[i], last[j]) == 1 {
				ans++
			}
		}
	}
	return ans
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	if a < 0 {
		return -a
	}
	return a
}
```

## Ruby

```ruby
def count_beautiful_pairs(nums)
  n = nums.length
  first_digits = nums.map { |num| num.to_s[0].ord - 48 } # '0'.ord = 48
  last_digits = nums.map { |num| num % 10 }

  count = 0
  (0...n).each do |i|
    (i + 1...n).each do |j|
      count += 1 if first_digits[i].gcd(last_digits[j]) == 1
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def countBeautifulPairs(nums: Array[Int]): Int = {
        def gcd(a: Int, b: Int): Int = {
            var x = a
            var y = b
            while (y != 0) {
                val tmp = x % y
                x = y
                y = tmp
            }
            x
        }

        def firstDigit(x: Int): Int = {
            var n = x
            while (n >= 10) n /= 10
            n
        }

        val n = nums.length
        val first = new Array[Int](n)
        val last = new Array[Int](n)

        for (i <- 0 until n) {
            first(i) = firstDigit(nums(i))
            last(i) = nums(i) % 10
        }

        var count = 0
        for (i <- 0 until n) {
            for (j <- i + 1 until n) {
                if (gcd(first(i), last(j)) == 1) count += 1
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_beautiful_pairs(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut first = vec![0i32; n];
        let mut last = vec![0i32; n];
        for (idx, &num) in nums.iter().enumerate() {
            let mut x = num;
            while x >= 10 {
                x /= 10;
            }
            first[idx] = x;
            last[idx] = num % 10;
        }

        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a.abs()
        }

        let mut count = 0i32;
        for i in 0..n {
            for j in (i + 1)..n {
                if gcd(first[i], last[j]) == 1 {
                    count += 1;
                }
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (count-beautiful-pairs nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((vec (list->vector nums))
         (n   (vector-length vec)))
    (define (first-digit x)
      (let loop ((y x))
        (if (< y 10) y
            (loop (quotient y 10)))))
    (for/sum ([i (in-range n)]
              [j (in-range (add1 i) n)])
      (let* ((fd (first-digit (vector-ref vec i)))
             (ld (modulo (vector-ref vec j) 10)))
        (if (= (gcd fd ld) 1) 1 0)))))
```

## Erlang

```erlang
-spec count_beautiful_pairs(Nums :: [integer()]) -> integer().
count_beautiful_pairs(Nums) ->
    N = length(Nums),
    count_beautiful_pairs(Nums, 0, N).

%% outer loop over i
-spec count_beautiful_pairs([integer()], non_neg_integer(), pos_integer()) -> integer().
count_beautiful_pairs(_Nums, I, N) when I >= N - 1 ->
    0;
count_beautiful_pairs(Nums, I, N) ->
    Ai = lists:nth(I + 1, Nums),
    Fi = first_digit(Ai),
    CountJ = count_j(Nums, I + 1, N - 1, Fi, 0),
    CountRest = count_beautiful_pairs(Nums, I + 1, N),
    CountJ + CountRest.

%% inner loop over j
-spec count_j([integer()], non_neg_integer(), non_neg_integer(), integer(), integer()) -> integer().
count_j(_Nums, J, MaxJ, _Fi, Acc) when J > MaxJ ->
    Acc;
count_j(Nums, J, MaxJ, Fi, Acc) ->
    Aj = lists:nth(J + 1, Nums),
    Lj = Aj rem 10,
    NewAcc = case gcd(Fi, Lj) of
                 1 -> Acc + 1;
                 _ -> Acc
             end,
    count_j(Nums, J + 1, MaxJ, Fi, NewAcc).

%% first digit of a positive integer
-spec first_digit(pos_integer()) -> integer().
first_digit(N) when N < 10 ->
    N;
first_digit(N) ->
    first_digit(N div 10).

%% Euclidean algorithm for gcd
-spec gcd(integer(), integer()) -> integer().
gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_beautiful_pairs(nums :: [integer]) :: integer
  def count_beautiful_pairs(nums) do
    firsts = Enum.map(nums, &first_digit/1)
    lasts = Enum.map(nums, fn x -> rem(x, 10) end)

    len = length(nums)

    0..(len - 2)
    |> Enum.reduce(0, fn i, acc ->
      (i + 1)..(len - 1)
      |> Enum.reduce(acc, fn j, inner_acc ->
        if Integer.gcd(Enum.at(firsts, i), Enum.at(lasts, j)) == 1 do
          inner_acc + 1
        else
          inner_acc
        end
      end)
    end)
  end

  defp first_digit(num) when num < 10, do: num
  defp first_digit(num), do: first_digit(div(num, 10))
end
```
