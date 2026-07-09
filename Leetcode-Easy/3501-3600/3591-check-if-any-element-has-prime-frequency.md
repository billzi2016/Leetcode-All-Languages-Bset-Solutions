# 3591. Check if Any Element Has Prime Frequency

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool checkPrimeFrequency(vector<int>& nums) {
        vector<int> freq(101, 0);
        for (int x : nums) ++freq[x];
        
        auto isPrime = [](int n) -> bool {
            if (n < 2) return false;
            for (int i = 2; i * i <= n; ++i)
                if (n % i == 0) return false;
            return true;
        };
        
        for (int cnt : freq) {
            if (isPrime(cnt)) return true;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean checkPrimeFrequency(int[] nums) {
        int[] freq = new int[101];
        for (int num : nums) {
            if (num >= 0 && num <= 100) {
                freq[num]++;
            }
        }
        for (int count : freq) {
            if (isPrime(count)) {
                return true;
            }
        }
        return false;
    }

    private boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        freq = Counter(nums)

        def is_prime(n):
            if n <= 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            i = 3
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 2
            return True

        for count in freq.values():
            if is_prime(count):
                return True
        return False
```

## Python3

```python
from typing import List
import math
from collections import Counter

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            limit = int(math.isqrt(n))
            for i in range(3, limit + 1, 2):
                if n % i == 0:
                    return False
            return True

        freq = Counter(nums)
        for count in freq.values():
            if is_prime(count):
                return True
        return False
```

## C

```c
#include <stdbool.h>

bool checkPrimeFrequency(int* nums, int numsSize) {
    int freq[101] = {0};
    for (int i = 0; i < numsSize; ++i) {
        int v = nums[i];
        if (v >= 0 && v <= 100) {
            ++freq[v];
        }
    }
    for (int i = 0; i <= 100; ++i) {
        int f = freq[i];
        if (f > 1) {
            bool prime = true;
            for (int d = 2; d * d <= f; ++d) {
                if (f % d == 0) {
                    prime = false;
                    break;
                }
            }
            if (prime) return true;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CheckPrimeFrequency(int[] nums)
    {
        var freq = new System.Collections.Generic.Dictionary<int, int>();
        foreach (var num in nums)
        {
            if (freq.ContainsKey(num))
                freq[num]++;
            else
                freq[num] = 1;
        }

        foreach (var count in freq.Values)
        {
            if (IsPrime(count))
                return true;
        }
        return false;
    }

    private bool IsPrime(int n)
    {
        if (n <= 1) return false;
        if (n == 2) return true;
        if ((n & 1) == 0) return false; // even numbers greater than 2
        for (int i = 3; i * i <= n; i += 2)
        {
            if (n % i == 0) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPrimeFrequency = function(nums) {
    const freqMap = new Map();
    for (const num of nums) {
        freqMap.set(num, (freqMap.get(num) || 0) + 1);
    }
    
    const isPrime = (n) => {
        if (n <= 1) return false;
        if (n === 2) return true;
        if (n % 2 === 0) return false;
        for (let i = 3; i * i <= n; i += 2) {
            if (n % i === 0) return false;
        }
        return true;
    };
    
    for (const count of freqMap.values()) {
        if (isPrime(count)) return true;
    }
    return false;
};
```

## Typescript

```typescript
function checkPrimeFrequency(nums: number[]): boolean {
    const freq = new Map<number, number>();
    for (const num of nums) {
        freq.set(num, (freq.get(num) ?? 0) + 1);
    }

    const isPrime = (n: number): boolean => {
        if (n <= 1) return false;
        if (n === 2) return true;
        if (n % 2 === 0) return false;
        for (let i = 3; i * i <= n; i += 2) {
            if (n % i === 0) return false;
        }
        return true;
    };

    for (const count of freq.values()) {
        if (isPrime(count)) return true;
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function checkPrimeFrequency($nums) {
        $freq = [];
        foreach ($nums as $num) {
            if (!isset($freq[$num])) {
                $freq[$num] = 0;
            }
            $freq[$num]++;
        }
        foreach ($freq as $count) {
            if ($this->isPrime($count)) {
                return true;
            }
        }
        return false;
    }

    private function isPrime($n) {
        if ($n <= 1) {
            return false;
        }
        if ($n == 2) {
            return true;
        }
        if ($n % 2 == 0) {
            return false;
        }
        $limit = (int)sqrt($n);
        for ($i = 3; $i <= $limit; $i += 2) {
            if ($n % $i == 0) {
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
    func checkPrimeFrequency(_ nums: [Int]) -> Bool {
        var freq = [Int: Int]()
        for num in nums {
            freq[num, default: 0] += 1
        }
        for count in freq.values {
            if isPrime(count) { return true }
        }
        return false
    }
    
    private func isPrime(_ n: Int) -> Bool {
        if n <= 1 { return false }
        if n <= 3 { return true } // 2 and 3 are prime
        if n % 2 == 0 || n % 3 == 0 { return false }
        var i = 5
        while i * i <= n {
            if n % i == 0 || n % (i + 2) == 0 { return false }
            i += 6
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkPrimeFrequency(nums: IntArray): Boolean {
        val freq = IntArray(101)
        for (num in nums) {
            if (num in 0..100) freq[num]++
        }
        for (count in freq) {
            if (isPrime(count)) return true
        }
        return false
    }

    private fun isPrime(n: Int): Boolean {
        if (n < 2) return false
        if (n == 2 || n == 3) return true
        if (n % 2 == 0 || n % 3 == 0) return false
        var i = 5
        while (i * i <= n) {
            if (n % i == 0 || n % (i + 2) == 0) return false
            i += 6
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool checkPrimeFrequency(List<int> nums) {
    final Map<int, int> freq = {};
    for (var num in nums) {
      freq[num] = (freq[num] ?? 0) + 1;
    }
    for (var count in freq.values) {
      if (_isPrime(count)) return true;
    }
    return false;
  }

  bool _isPrime(int n) {
    if (n < 2) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; i * i <= n; i += 2) {
      if (n % i == 0) return false;
    }
    return true;
  }
}
```

## Golang

```go
func checkPrimeFrequency(nums []int) bool {
	freq := make(map[int]int)
	for _, v := range nums {
		freq[v]++
	}
	for _, cnt := range freq {
		if isPrime(cnt) {
			return true
		}
	}
	return false
}

func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	for i := 3; i*i <= n; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def prime?(n)
  return false if n <= 1
  return true if n == 2
  return false if n.even?
  i = 3
  while i * i <= n
    return false if n % i == 0
    i += 2
  end
  true
end

# @param {Integer[]} nums
# @return {Boolean}
def check_prime_frequency(nums)
  freq = Hash.new(0)
  nums.each { |num| freq[num] += 1 }
  freq.values.any? { |count| prime?(count) }
end
```

## Scala

```scala
object Solution {
    def checkPrimeFrequency(nums: Array[Int]): Boolean = {
        val freq = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
        for (num <- nums) {
            freq(num) = freq(num) + 1
        }

        def isPrime(n: Int): Boolean = {
            if (n <= 1) return false
            var i = 2
            while (i * i <= n) {
                if (n % i == 0) return false
                i += 1
            }
            true
        }

        freq.values.exists(isPrime)
    }
}
```

## Rust

```rust
use std::collections::HashMap;

fn is_prime(n: i32) -> bool {
    if n < 2 {
        return false;
    }
    let limit = (n as f64).sqrt() as i32;
    for i in 2..=limit {
        if n % i == 0 {
            return false;
        }
    }
    true
}

impl Solution {
    pub fn check_prime_frequency(nums: Vec<i32>) -> bool {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for num in nums {
            *freq.entry(num).or_insert(0) += 1;
        }
        for &count in freq.values() {
            if is_prime(count) {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(define (prime? n)
  (if (<= n 1)
      #f
      (let loop ((i 2))
        (cond [(> (* i i) n) #t]
              [(zero? (modulo n i)) #f]
              [else (loop (+ i 1))]))))

(define/contract (check-prime-frequency nums)
  (-> (listof exact-integer?) boolean?)
  (let ((freq (make-hash)))
    (for ([x nums])
      (hash-set! freq x (+ 1 (hash-ref freq x 0))))
    (for/or ([cnt (in-hash-values freq)])
      (prime? cnt))))
```

## Erlang

```erlang
-spec check_prime_frequency([integer()]) -> boolean().
check_prime_frequency(Nums) ->
    FreqMap = lists:foldl(
        fun(X, Acc) ->
            maps:update_with(X, fun(C) -> C + 1 end, 1, Acc)
        end,
        #{},
        Nums
    ),
    Values = maps:values(FreqMap),
    lists:any(fun is_prime/1, Values).

-spec is_prime(integer()) -> boolean().
is_prime(N) when N =< 1 -> false;
is_prime(2) -> true;
is_prime(N) when N rem 2 =:= 0 -> false;
is_prime(N) ->
    Max = trunc(math:sqrt(N)),
    is_prime_check(N, 3, Max).

-spec is_prime_check(integer(), integer(), integer()) -> boolean().
is_prime_check(_N, I, Max) when I > Max -> true;
is_prime_check(N, I, Max) ->
    case N rem I of
        0 -> false;
        _ -> is_prime_check(N, I + 2, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_prime_frequency(nums :: [integer]) :: boolean
  def check_prime_frequency(nums) do
    freq =
      Enum.reduce(nums, %{}, fn x, acc ->
        Map.update(acc, x, 1, &(&1 + 1))
      end)

    Enum.any?(freq, fn {_k, v} -> prime?(v) end)
  end

  defp prime?(n) when n <= 1, do: false
  defp prime?(2), do: true
  defp prime?(n) do
    max = :math.sqrt(n) |> trunc()
    3..max
    |> Enum.reduce_while(true, fn i, _acc ->
      if rem(n, i) == 0, do: {:halt, false}, else: {:cont, true}
    end)
  end
end
```
