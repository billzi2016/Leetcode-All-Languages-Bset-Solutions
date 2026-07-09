# 2614. Prime In Diagonal

## Cpp

```cpp
class Solution {
public:
    bool isPrime(int x) {
        if (x < 2) return false;
        if (x == 2) return true;
        if (x % 2 == 0) return false;
        for (int i = 3; 1LL * i * i <= x; i += 2) {
            if (x % i == 0) return false;
        }
        return true;
    }
    
    int diagonalPrime(vector<vector<int>>& nums) {
        int n = nums.size();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int a = nums[i][i];
            if (isPrime(a)) ans = max(ans, a);
            int b = nums[i][n - 1 - i];
            if (isPrime(b)) ans = max(ans, b);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int diagonalPrime(int[][] nums) {
        int n = nums.length;
        int maxPrime = 0;
        for (int i = 0; i < n; i++) {
            // main diagonal
            int val1 = nums[i][i];
            if (isPrime(val1) && val1 > maxPrime) {
                maxPrime = val1;
            }
            // anti-diagonal
            int val2 = nums[i][n - 1 - i];
            if (isPrime(val2) && val2 > maxPrime) {
                maxPrime = val2;
            }
        }
        return maxPrime;
    }

    private boolean isPrime(int x) {
        if (x <= 1) return false;
        if (x == 2) return true;
        if ((x & 1) == 0) return false;
        int limit = (int) Math.sqrt(x);
        for (int i = 3; i <= limit; i += 2) {
            if (x % i == 0) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        def is_prime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            i = 3
            limit = int(x ** 0.5) + 1
            while i <= limit:
                if x % i == 0:
                    return False
                i += 2
            return True

        n = len(nums)
        max_prime = 0
        for i in range(n):
            a = nums[i][i]
            b = nums[i][n - 1 - i]
            if is_prime(a) and a > max_prime:
                max_prime = a
            if is_prime(b) and b > max_prime:
                max_prime = b
        return max_prime
```

## Python3

```python
from math import isqrt
from typing import List

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        max_prime = 0

        def is_prime(x: int) -> bool:
            if x <= 1:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            r = isqrt(x)
            i = 3
            while i <= r:
                if x % i == 0:
                    return False
                i += 2
            return True

        for i in range(n):
            a = nums[i][i]
            b = nums[i][n - 1 - i]

            if is_prime(a) and a > max_prime:
                max_prime = a
            if b != a and is_prime(b) and b > max_prime:
                max_prime = b

        return max_prime
```

## C

```c
int isPrime(int x) {
    if (x < 2) return 0;
    if (x == 2) return 1;
    if (x % 2 == 0) return 0;
    for (int i = 3; i * i <= x; i += 2) {
        if (x % i == 0) return 0;
    }
    return 1;
}

int diagonalPrime(int** nums, int numsSize, int* numsColSize) {
    int maxPrime = 0;
    for (int i = 0; i < numsSize; ++i) {
        int val1 = nums[i][i];
        if (isPrime(val1) && val1 > maxPrime) maxPrime = val1;
        int j = numsSize - 1 - i;
        int val2 = nums[i][j];
        if (isPrime(val2) && val2 > maxPrime) maxPrime = val2;
    }
    return maxPrime;
}
```

## Csharp

```csharp
public class Solution
{
    public int DiagonalPrime(int[][] nums)
    {
        int n = nums.Length;
        int maxPrime = 0;
        for (int i = 0; i < n; i++)
        {
            int mainVal = nums[i][i];
            if (IsPrime(mainVal) && mainVal > maxPrime)
                maxPrime = mainVal;

            int antiVal = nums[i][n - 1 - i];
            if (antiVal != mainVal && IsPrime(antiVal) && antiVal > maxPrime)
                maxPrime = antiVal;
        }
        return maxPrime;
    }

    private bool IsPrime(int x)
    {
        if (x <= 1) return false;
        if (x == 2) return true;
        if ((x & 1) == 0) return false;
        int limit = (int)Math.Sqrt(x);
        for (int i = 3; i <= limit; i += 2)
            if (x % i == 0) return false;
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} nums
 * @return {number}
 */
var diagonalPrime = function(nums) {
    const n = nums.length;
    let maxPrime = 0;
    
    const isPrime = (num) => {
        if (num < 2) return false;
        if (num === 2) return true;
        if (num % 2 === 0) return false;
        const limit = Math.sqrt(num);
        for (let i = 3; i <= limit; i += 2) {
            if (num % i === 0) return false;
        }
        return true;
    };
    
    for (let i = 0; i < n; ++i) {
        const mainDiag = nums[i][i];
        if (mainDiag > maxPrime && isPrime(mainDiag)) {
            maxPrime = mainDiag;
        }
        const antiDiag = nums[i][n - 1 - i];
        if (antiDiag > maxPrime && isPrime(antiDiag)) {
            maxPrime = antiDiag;
        }
    }
    
    return maxPrime;
};
```

## Typescript

```typescript
function diagonalPrime(nums: number[][]): number {
    const n = nums.length;
    let maxPrime = 0;

    const isPrime = (x: number): boolean => {
        if (x < 2) return false;
        if (x === 2) return true;
        if (x % 2 === 0) return false;
        const limit = Math.sqrt(x);
        for (let i = 3; i <= limit; i += 2) {
            if (x % i === 0) return false;
        }
        return true;
    };

    for (let i = 0; i < n; ++i) {
        const mainVal = nums[i][i];
        if (isPrime(mainVal) && mainVal > maxPrime) maxPrime = mainVal;

        const antiVal = nums[i][n - 1 - i];
        if (isPrime(antiVal) && antiVal > maxPrime) maxPrime = antiVal;
    }

    return maxPrime;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $nums
     * @return Integer
     */
    function diagonalPrime($nums) {
        $n = count($nums);
        $maxPrime = 0;
        for ($i = 0; $i < $n; $i++) {
            $val1 = $nums[$i][$i];
            if ($this->isPrime($val1) && $val1 > $maxPrime) {
                $maxPrime = $val1;
            }
            $j = $n - 1 - $i;
            if ($j != $i) {
                $val2 = $nums[$i][$j];
                if ($this->isPrime($val2) && $val2 > $maxPrime) {
                    $maxPrime = $val2;
                }
            }
        }
        return $maxPrime;
    }

    private function isPrime($num) {
        if ($num < 2) {
            return false;
        }
        if ($num == 2) {
            return true;
        }
        if ($num % 2 == 0) {
            return false;
        }
        $limit = (int)sqrt($num);
        for ($i = 3; $i <= $limit; $i += 2) {
            if ($num % $i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func diagonalPrime(_ nums: [[Int]]) -> Int {
        let n = nums.count
        var maxPrime = 0
        for i in 0..<n {
            let valMain = nums[i][i]
            if isPrime(valMain) && valMain > maxPrime {
                maxPrime = valMain
            }
            let j = n - 1 - i
            if j != i {
                let valAnti = nums[i][j]
                if isPrime(valAnti) && valAnti > maxPrime {
                    maxPrime = valAnti
                }
            }
        }
        return maxPrime
    }
    
    private func isPrime(_ num: Int) -> Bool {
        if num < 2 { return false }
        if num == 2 { return true }
        if num % 2 == 0 { return false }
        var i = 3
        while i * i <= num {
            if num % i == 0 { return false }
            i += 2
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun diagonalPrime(nums: Array<IntArray>): Int {
        val n = nums.size
        var maxPrime = 0
        for (i in 0 until n) {
            val main = nums[i][i]
            if (isPrime(main) && main > maxPrime) maxPrime = main
            val anti = nums[i][n - 1 - i]
            if (anti != main && isPrime(anti) && anti > maxPrime) maxPrime = anti
        }
        return maxPrime
    }

    private fun isPrime(x: Int): Boolean {
        if (x < 2) return false
        if (x == 2 || x == 3) return true
        if (x % 2 == 0 || x % 3 == 0) return false
        var i = 5
        while (i * i <= x) {
            if (x % i == 0 || x % (i + 2) == 0) return false
            i += 6
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  int diagonalPrime(List<List<int>> nums) {
    int n = nums.length;
    int maxPrime = 0;

    bool isPrime(int x) {
      if (x < 2) return false;
      if (x == 2) return true;
      if (x % 2 == 0) return false;
      for (int d = 3; d * d <= x; d += 2) {
        if (x % d == 0) return false;
      }
      return true;
    }

    for (int i = 0; i < n; ++i) {
      int a = nums[i][i];
      if (a > maxPrime && isPrime(a)) {
        maxPrime = a;
      }
      int b = nums[i][n - 1 - i];
      if (b != a && b > maxPrime && isPrime(b)) {
        maxPrime = b;
      }
    }

    return maxPrime;
  }
}
```

## Golang

```go
func diagonalPrime(nums [][]int) int {
	isPrime := func(num int) bool {
		if num <= 1 {
			return false
		}
		if num == 2 {
			return true
		}
		if num%2 == 0 {
			return false
		}
		for i := 3; i*i <= num; i += 2 {
			if num%i == 0 {
				return false
			}
		}
		return true
	}

	n := len(nums)
	maxPrime := 0
	for i := 0; i < n; i++ {
		a := nums[i][i]
		if a > maxPrime && isPrime(a) {
			maxPrime = a
		}
		b := nums[i][n-1-i]
		if b > maxPrime && isPrime(b) {
			maxPrime = b
		}
	}
	return maxPrime
}
```

## Ruby

```ruby
def diagonal_prime(nums)
  n = nums.length
  max_prime = 0

  prime_check = lambda do |x|
    return false if x < 2
    return true if x == 2
    return false if x.even?
    i = 3
    while i * i <= x
      return false if x % i == 0
      i += 2
    end
    true
  end

  (0...n).each do |i|
    [nums[i][i], nums[i][n - 1 - i]].each do |val|
      if val > max_prime && prime_check.call(val)
        max_prime = val
      end
    end
  end

  max_prime
end
```

## Scala

```scala
object Solution {
    def diagonalPrime(nums: Array[Array[Int]]): Int = {
        def isPrime(x: Int): Boolean = {
            if (x < 2) false
            else if (x == 2) true
            else if ((x & 1) == 0) false
            else {
                var i = 3
                while (i * i <= x) {
                    if (x % i == 0) return false
                    i += 2
                }
                true
            }
        }

        val n = nums.length
        var maxPrime = 0
        for (i <- 0 until n) {
            val v1 = nums(i)(i)
            if (v1 > maxPrime && isPrime(v1)) maxPrime = v1

            val j = n - 1 - i
            if (j != i) {
                val v2 = nums(i)(j)
                if (v2 > maxPrime && isPrime(v2)) maxPrime = v2
            }
        }
        maxPrime
    }
}
```

## Rust

```rust
fn is_prime(num: i32) -> bool {
    if num < 2 {
        return false;
    }
    if num == 2 || num == 3 {
        return true;
    }
    if num % 2 == 0 || num % 3 == 0 {
        return false;
    }
    let mut i = 5;
    while (i as i64) * (i as i64) <= num as i64 {
        if num % i == 0 || num % (i + 2) == 0 {
            return false;
        }
        i += 6;
    }
    true
}

impl Solution {
    pub fn diagonal_prime(nums: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        let mut max_prime = 0;
        for i in 0..n {
            // main diagonal
            let val_main = nums[i][i];
            if is_prime(val_main) && val_main > max_prime {
                max_prime = val_main;
            }
            // anti-diagonal
            let j = n - 1 - i;
            if j != i {
                let val_anti = nums[i][j];
                if is_prime(val_anti) && val_anti > max_prime {
                    max_prime = val_anti;
                }
            }
        }
        max_prime
    }
}
```

## Racket

```racket
#lang racket

(define (prime? n)
  (cond [(<= n 1) #f]
        [(= n 2) #t]
        [(even? n) #f]
        [else
         (let loop ((i 3) (limit (exact-floor (sqrt n))))
           (if (> i limit)
               #t
               (if (= (remainder n i) 0)
                   #f
                   (loop (+ i 2) limit))))]))

(define/contract (diagonal-prime nums)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length nums))
         (maxp 0))
    (for ([i (in-range n)])
      (let* ((row (list-ref nums i))
             (a (list-ref row i))
             (b (list-ref row (- n 1 i))))
        (when (prime? a)
          (set! maxp (max maxp a)))
        (when (prime? b)
          (set! maxp (max maxp b)))))
    maxp))
```

## Erlang

```erlang
-module(solution).
-export([diagonal_prime/1]).

-spec diagonal_prime(Nums :: [[integer()]]) -> integer().
diagonal_prime(Nums) ->
    N = length(Nums),
    find_max(Nums, N, 0, 0).

find_max(_Nums, Size, Index, Max) when Index >= Size ->
    Max;
find_max(Nums, Size, Index, Max) ->
    Row = lists:nth(Index + 1, Nums),
    Main = lists:nth(Index + 1, Row),
    AntiIdx = Size - Index,
    Anti = lists:nth(AntiIdx, Row),

    Max1 = case is_prime(Main) of
               true -> max(Main, Max);
               false -> Max
           end,

    Max2 = case is_prime(Anti) of
               true -> max(Anti, Max1);
               false -> Max1
           end,

    find_max(Nums, Size, Index + 1, Max2).

-spec is_prime(integer()) -> boolean().
is_prime(N) when N < 2 -> false;
is_prime(2) -> true;
is_prime(N) when N rem 2 =:= 0 -> false;
is_prime(N) ->
    is_prime(N, 3).

-spec is_prime(integer(), integer()) -> boolean().
is_prime(N, I) when I * I > N -> true;
is_prime(N, I) ->
    case N rem I of
        0 -> false;
        _ -> is_prime(N, I + 2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec diagonal_prime(nums :: [[integer]]) :: integer
  def diagonal_prime(nums) do
    n = length(nums)

    0..(n - 1)
    |> Enum.reduce(0, fn i, acc ->
      row = Enum.at(nums, i)
      main_val = Enum.at(row, i)
      anti_val = Enum.at(row, n - 1 - i)

      acc
      |> maybe_update_max(main_val)
      |> maybe_update_max(anti_val)
    end)
  end

  defp maybe_update_max(current_max, val) do
    if prime?(val) and val > current_max do
      val
    else
      current_max
    end
  end

  defp prime?(n) when n < 2, do: false
  defp prime?(2), do: true
  defp prime?(n) when rem(n, 2) == 0, do: false
  defp prime?(n) do
    limit = :math.sqrt(n) |> trunc()
    Enum.reduce_while(3..limit, true, fn i, _ ->
      if rem(n, i) == 0 do
        {:halt, false}
      else
        {:cont, true}
      end
    end)
  end
end
```
