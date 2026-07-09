# 3115. Maximum Prime Difference

## Cpp

```cpp
class Solution {
public:
    int maximumPrimeDifference(vector<int>& nums) {
        auto isPrime = [](int x) -> bool {
            if (x < 2) return false;
            for (int d = 2; d * d <= x; ++d) {
                if (x % d == 0) return false;
            }
            return true;
        };
        
        int first = -1, last = -1;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (isPrime(nums[i])) {
                if (first == -1) first = i;
                last = i;
            }
        }
        // At least one prime guaranteed
        return last - first;
    }
};
```

## Java

```java
class Solution {
    private static final boolean[] IS_PRIME = new boolean[101];
    static {
        java.util.Arrays.fill(IS_PRIME, true);
        IS_PRIME[0] = false;
        IS_PRIME[1] = false;
        for (int p = 2; p * p <= 100; ++p) {
            if (IS_PRIME[p]) {
                for (int multiple = p * p; multiple <= 100; multiple += p) {
                    IS_PRIME[multiple] = false;
                }
            }
        }
    }

    public int maximumPrimeDifference(int[] nums) {
        int first = -1, last = -1;
        for (int i = 0; i < nums.length; ++i) {
            if (IS_PRIME[nums[i]]) {
                if (first == -1) first = i;
                last = i;
            }
        }
        // At least one prime exists per problem statement
        return last - first;
    }
}
```

## Python

```python
class Solution(object):
    def maximumPrimeDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Precompute primes up to 100
        is_prime = [False] * 101
        for i in range(2, 101):
            prime = True
            j = 2
            while j * j <= i:
                if i % j == 0:
                    prime = False
                    break
                j += 1
            is_prime[i] = prime

        first = -1
        last = -1
        for idx, val in enumerate(nums):
            if is_prime[val]:
                if first == -1:
                    first = idx
                last = idx
        # At least one prime exists per problem statement
        return last - first if first != -1 else 0

    # LeetCode expects the method name as given in the prompt
    def maximumPrimeDifference(self, nums):
        return self.maximumPrimeDistance(nums)
```

## Python3

```python
from typing import List

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        # Precomputed primes up to 100
        prime_set = {
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
            31, 37, 41, 43, 47, 53, 59, 61, 67,
            71, 73, 79, 83, 89, 97
        }
        first = -1
        last = -1
        for i, val in enumerate(nums):
            if val in prime_set:
                if first == -1:
                    first = i
                last = i
        return last - first
```

## C

```c
int maximumPrimeDifference(int* nums, int numsSize) {
    // Precompute primes up to 100
    static const char primeTable[101] = {
        0,0,1,1,0,1,0,1,0,0,
        0,1,0,1,0,0,0,1,0,1,
        0,0,0,1,0,0,0,0,0,1,
        0,1,0,0,0,1,0,1,0,0,
        0,1,0,0,0,0,0,1,0,1,
        0,0,0,1,0,0,0,0,0,1,
        0,1,0,0,0,1,0,1,0,0,
        0,1,0,0,0,0,0,1,0,1,
        0,0,0,1,0,0,0,0,0,1,
        0,1,0,0,0,1,0,1,0,0,
        0
    };
    
    int first = -1;
    int last = -1;
    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        if (val <= 100 && primeTable[val]) {
            if (first == -1) first = i;
            last = i;
        }
    }
    // At least one prime exists, so first != -1
    return last - first;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumPrimeDifference(int[] nums) {
        bool[] isPrime = new bool[101];
        for (int i = 2; i <= 100; i++) isPrime[i] = true;
        for (int p = 2; p * p <= 100; p++) {
            if (isPrime[p]) {
                for (int multiple = p * p; multiple <= 100; multiple += p) {
                    isPrime[multiple] = false;
                }
            }
        }

        int first = -1, last = -1;
        for (int i = 0; i < nums.Length; i++) {
            int val = nums[i];
            if (val >= 2 && isPrime[val]) {
                if (first == -1) first = i;
                last = i;
            }
        }

        return last - first;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumPrimeDistance = function(nums) {
    // Precompute primality up to 100
    const isPrime = new Array(101).fill(true);
    isPrime[0] = isPrime[1] = false;
    for (let i = 2; i * i <= 100; ++i) {
        if (isPrime[i]) {
            for (let j = i * i; j <= 100; j += i) {
                isPrime[j] = false;
            }
        }
    }

    let first = Infinity, last = -1;
    for (let i = 0; i < nums.length; ++i) {
        if (isPrime[nums[i]]) {
            if (i < first) first = i;
            if (i > last) last = i;
        }
    }
    return last - first;
};
```

## Typescript

```typescript
function maximumPrimeDifference(nums: number[]): number {
    const MAX_VAL = 100;
    const isPrime = new Array<boolean>(MAX_VAL + 1).fill(true);
    isPrime[0] = isPrime[1] = false;
    for (let p = 2; p * p <= MAX_VAL; ++p) {
        if (isPrime[p]) {
            for (let multiple = p * p; multiple <= MAX_VAL; multiple += p) {
                isPrime[multiple] = false;
            }
        }
    }

    let first = -1;
    let last = -1;

    for (let i = 0; i < nums.length; ++i) {
        if (isPrime[nums[i]]) {
            if (first === -1) first = i;
            last = i;
        }
    }

    // At least one prime guaranteed
    return last - first;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumPrimeDifference($nums) {
        // Precompute prime flags up to 100
        $prime = array_fill(0, 101, false);
        $primesList = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97];
        foreach ($primesList as $p) {
            $prime[$p] = true;
        }

        $first = -1;
        $last = -1;

        foreach ($nums as $idx => $val) {
            if ($val <= 100 && $prime[$val]) {
                if ($first === -1) {
                    $first = $idx;
                }
                $last = $idx;
            }
        }

        // At least one prime guaranteed
        return $last - $first;
    }
}
```

## Swift

```swift
class Solution {
    func maximumPrimeDifference(_ nums: [Int]) -> Int {
        var isPrime = [Bool](repeating: false, count: 101)
        if 2 <= 100 {
            for i in 2...100 {
                var primeFlag = true
                var d = 2
                while d * d <= i {
                    if i % d == 0 {
                        primeFlag = false
                        break
                    }
                    d += 1
                }
                isPrime[i] = primeFlag
            }
        }
        
        var first = -1
        var last = -1
        
        for (idx, val) in nums.enumerated() {
            if isPrime[val] {
                if first == -1 { first = idx }
                last = idx
            }
        }
        return last - first
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val isPrime = BooleanArray(101) { true }.apply {
        this[0] = false
        this[1] = false
        for (i in 2..10) {
            if (this[i]) {
                var j = i * i
                while (j <= 100) {
                    this[j] = false
                    j += i
                }
            }
        }
    }

    fun maximumPrimeDifference(nums: IntArray): Int {
        var first = -1
        var last = -1
        for (i in nums.indices) {
            if (isPrime[nums[i]]) {
                if (first == -1) first = i
                last = i
            }
        }
        return last - first
    }
}
```

## Dart

```dart
class Solution {
  int maximumPrimeDifference(List<int> nums) {
    // Precompute primes up to 100
    const int limit = 100;
    List<bool> isPrime = List.filled(limit + 1, true);
    if (limit >= 0) isPrime[0] = false;
    if (limit >= 1) isPrime[1] = false;
    for (int i = 2; i * i <= limit; ++i) {
      if (isPrime[i]) {
        for (int j = i * i; j <= limit; j += i) {
          isPrime[j] = false;
        }
      }
    }

    int first = -1;
    int last = -1;

    for (int i = 0; i < nums.length; ++i) {
      if (isPrime[nums[i]]) {
        if (first == -1) first = i;
        last = i;
      }
    }

    // At least one prime exists per problem statement
    return last - first;
  }
}
```

## Golang

```go
func maximumPrimeDifference(nums []int) int {
    // Precompute primes up to 100
    const limit = 100
    isPrime := make([]bool, limit+1)
    for i := 2; i <= limit; i++ {
        isPrime[i] = true
    }
    for p := 2; p*p <= limit; p++ {
        if isPrime[p] {
            for multiple := p * p; multiple <= limit; multiple += p {
                isPrime[multiple] = false
            }
        }
    }

    first, last := -1, -1
    for i, v := range nums {
        if v >= 0 && v <= limit && isPrime[v] {
            if first == -1 {
                first = i
            }
            last = i
        }
    }
    // At least one prime exists per problem statement
    return last - first
}
```

## Ruby

```ruby
def maximum_prime_difference(nums)
  max_val = 100
  is_prime = Array.new(max_val + 1, true)
  is_prime[0] = is_prime[1] = false
  limit = Math.sqrt(max_val).to_i
  (2..limit).each do |p|
    next unless is_prime[p]
    (p * p).step(max_val, p) { |multiple| is_prime[multiple] = false }
  end

  first = nil
  last = nil
  nums.each_with_index do |num, idx|
    if is_prime[num]
      first = idx if first.nil?
      last = idx
    end
  end
  last - first
end
```

## Scala

```scala
object Solution {
    def maximumPrimeDifference(nums: Array[Int]): Int = {
        val limit = 100
        val isPrime = Array.fill(limit + 1)(true)
        isPrime(0) = false
        isPrime(1) = false
        var p = 2
        while (p * p <= limit) {
            if (isPrime(p)) {
                var multiple = p * p
                while (multiple <= limit) {
                    isPrime(multiple) = false
                    multiple += p
                }
            }
            p += 1
        }

        var first = -1
        var last = -1
        var i = 0
        val n = nums.length
        while (i < n) {
            if (isPrime(nums(i))) {
                if (first == -1) first = i
                last = i
            }
            i += 1
        }
        last - first
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_prime_difference(nums: Vec<i32>) -> i32 {
        // Precompute primality for numbers up to 100
        let mut is_prime = [false; 101];
        for i in 2..=100 {
            is_prime[i] = true;
        }
        let mut p = 2;
        while p * p <= 100 {
            if is_prime[p] {
                let mut multiple = p * p;
                while multiple <= 100 {
                    is_prime[multiple] = false;
                    multiple += p;
                }
            }
            p += 1;
        }

        let mut first: Option<usize> = None;
        let mut last: usize = 0;

        for (i, &val) in nums.iter().enumerate() {
            if val as usize <= 100 && is_prime[val as usize] {
                if first.is_none() {
                    first = Some(i);
                }
                last = i;
            }
        }

        let start = first.unwrap();
        (last - start) as i32
    }
}
```

## Racket

```racket
(define (prime? n)
  (cond [(< n 2) #f]
        [(= n 2) #t]
        [(even? n) #f]
        [else
         (let loop ((i 3))
           (if (> (* i i) n)
               #t
               (if (= (remainder n i) 0)
                   #f
                   (loop (+ i 2)))))]))

(define/contract (maximum-prime-difference nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (idx 0) (first #f) (last #f))
    (if (null? lst)
        (if first
            (- last first)
            0)
        (let* ((val (car lst))
               (is-p (prime? val))
               (new-first (if (and is-p (not first)) idx first))
               (new-last (if is-p idx last)))
          (loop (cdr lst) (+ idx 1) new-first new-last)))))
```

## Erlang

```erlang
-spec maximum_prime_difference([integer()]) -> integer().
maximum_prime_difference(Nums) ->
    {First, Last} = find_first_last(Nums, 0, undefined, undefined),
    case First of
        undefined -> 0;
        _ -> Last - First
    end.

find_first_last([], _Idx, First, Last) ->
    {First, Last};
find_first_last([H|T], Idx, First, Last) ->
    if is_prime(H) ->
            case First of
                undefined -> find_first_last(T, Idx + 1, Idx, Idx);
                _ -> find_first_last(T, Idx + 1, First, Idx)
            end;
       true ->
            find_first_last(T, Idx + 1, First, Last)
    end.

is_prime(N) when N < 2 -> false;
is_prime(2) -> true;
is_prime(N) when N rem 2 =:= 0 -> false;
is_prime(N) -> is_prime(N, 3).

is_prime(N, D) when D * D > N -> true;
is_prime(N, D) ->
    case N rem D of
        0 -> false;
        _ -> is_prime(N, D + 2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_prime_difference(nums :: [integer]) :: integer
  def maximum_prime_difference(nums) do
    primes = MapSet.new([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97])

    {first_idx, last_idx} =
      Enum.reduce(Enum.with_index(nums), {nil, nil}, fn {val, idx}, {first, _last}=acc ->
        if MapSet.member?(primes, val) do
          first = if is_nil(first), do: idx, else: first
          {first, idx}
        else
          acc
        end
      end)

    last_idx - first_idx
  end
end
```
