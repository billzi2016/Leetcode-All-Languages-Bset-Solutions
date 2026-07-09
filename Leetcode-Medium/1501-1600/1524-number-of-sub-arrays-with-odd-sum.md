# 1524. Number of Sub-arrays With Odd Sum

## Cpp

```cpp
class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        const int MOD = 1'000'000'007;
        long long even = 1, odd = 0; // counts of prefix sums with even/odd parity seen so far
        long long ans = 0;
        long long pref = 0;
        for (int x : arr) {
            pref += x;
            if ((pref & 1) == 0) {          // current prefix sum is even
                ans = (ans + odd) % MOD;    // pair with previous odd prefixes
                ++even;
            } else {                         // current prefix sum is odd
                ans = (ans + even) % MOD;   // pair with previous even prefixes
                ++odd;
            }
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int numOfSubarrays(int[] arr) {
        final int MOD = 1_000_000_007;
        long evenCount = 1; // empty prefix sum is even
        long oddCount = 0;
        long ans = 0;
        int parity = 0; // current prefix sum parity: 0 even, 1 odd

        for (int num : arr) {
            parity ^= (num & 1);
            if (parity == 0) { // prefix sum is even
                ans += oddCount;
                evenCount++;
            } else { // prefix sum is odd
                ans += evenCount;
                oddCount++;
            }
            ans %= MOD;
        }

        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        even_cnt = 1  # empty prefix sum is even
        odd_cnt = 0
        parity = 0   # current prefix sum parity (0 for even, 1 for odd)
        ans = 0
        for num in arr:
            parity ^= (num & 1)  # update parity with current number
            if parity == 0:
                ans += odd_cnt
                even_cnt += 1
            else:
                ans += even_cnt
                odd_cnt += 1
            ans %= MOD
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even_cnt = 1  # empty prefix sum is even
        odd_cnt = 0
        ans = 0
        parity = 0  # current prefix sum parity (0 for even, 1 for odd)
        for num in arr:
            parity ^= (num & 1)  # update parity of prefix sum
            if parity == 0:
                ans += odd_cnt
                even_cnt += 1
            else:
                ans += even_cnt
                odd_cnt += 1
            ans %= MOD
        return ans
```

## C

```c
#include <stdint.h>

int numOfSubarrays(int* arr, int arrSize) {
    const int MOD = 1000000007;
    long long evenCount = 1; // empty prefix has even sum
    long long oddCount = 0;
    long long ans = 0;
    int parity = 0; // current prefix sum parity: 0 even, 1 odd

    for (int i = 0; i < arrSize; ++i) {
        parity ^= (arr[i] & 1);
        if (parity == 0) {
            ans += oddCount;
            if (ans >= MOD) ans %= MOD;
            ++evenCount;
        } else {
            ans += evenCount;
            if (ans >= MOD) ans %= MOD;
            ++oddCount;
        }
    }

    return (int)(ans % MOD);
}
```

## Csharp

```csharp
public class Solution
{
    public int NumOfSubarrays(int[] arr)
    {
        const int MOD = 1000000007;
        long evenCount = 1; // empty prefix sum is even
        long oddCount = 0;
        long ans = 0;
        long prefix = 0;

        foreach (int num in arr)
        {
            prefix += num;
            if ((prefix & 1) == 0) // even prefix sum
            {
                ans = (ans + oddCount) % MOD;
                evenCount++;
            }
            else // odd prefix sum
            {
                ans = (ans + evenCount) % MOD;
                oddCount++;
            }
        }

        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var numOfSubarrays = function(arr) {
    const MOD = 1000000007;
    let evenCount = 1; // empty prefix sum is even
    let oddCount = 0;
    let parity = 0; // current prefix sum parity: 0 even, 1 odd
    let result = 0;

    for (let num of arr) {
        parity ^= (num & 1);
        if (parity === 0) {
            result += oddCount;
            evenCount++;
        } else {
            result += evenCount;
            oddCount++;
        }
        if (result >= MOD) result %= MOD;
    }

    return result % MOD;
};
```

## Typescript

```typescript
function numOfSubarrays(arr: number[]): number {
    const MOD = 1_000_000_007;
    let evenCount = 1; // empty prefix has even sum
    let oddCount = 0;
    let parity = 0; // current prefix sum parity: 0 even, 1 odd
    let result = 0;

    for (const num of arr) {
        parity ^= (num & 1);
        if (parity === 0) {
            result = (result + oddCount) % MOD;
            evenCount++;
        } else {
            result = (result + evenCount) % MOD;
            oddCount++;
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function numOfSubarrays($arr) {
        $MOD = 1000000007;
        $evenCount = 1; // empty prefix sum is even
        $oddCount = 0;
        $prefixSum = 0;
        $ans = 0;

        foreach ($arr as $num) {
            $prefixSum += $num;
            if (($prefixSum & 1) == 0) { // even prefix sum
                $ans = ($ans + $oddCount) % $MOD;
                $evenCount++;
            } else { // odd prefix sum
                $ans = ($ans + $evenCount) % $MOD;
                $oddCount++;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numOfSubarrays(_ arr: [Int]) -> Int {
        let MOD = 1_000_000_007
        var evenCount: Int64 = 1   // empty prefix sum is even
        var oddCount: Int64 = 0
        var prefixParity = 0       // 0 for even, 1 for odd
        var result: Int64 = 0
        
        for num in arr {
            let p = num & 1
            prefixParity ^= p
            if prefixParity == 0 {
                result += oddCount
                evenCount += 1
            } else {
                result += evenCount
                oddCount += 1
            }
            if result >= Int64(MOD) {
                result %= Int64(MOD)
            }
        }
        return Int(result % Int64(MOD))
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numOfSubarrays(arr: IntArray): Int {
        val MOD = 1_000_000_007L
        var evenCount = 1L   // empty prefix sum is even
        var oddCount = 0L
        var parity = 0       // current prefix sum parity: 0 for even, 1 for odd
        var result = 0L

        for (num in arr) {
            parity = (parity + (num and 1)) and 1
            if (parity == 0) {
                result += oddCount
                evenCount++
            } else {
                result += evenCount
                oddCount++
            }
            if (result >= MOD) result %= MOD
        }

        return (result % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int numOfSubarrays(List<int> arr) {
    int evenCount = 1; // empty prefix sum is even
    int oddCount = 0;
    int count = 0;
    int parity = 0; // current prefix sum parity (0 for even, 1 for odd)

    for (int num in arr) {
      parity ^= (num & 1);
      if (parity == 0) {
        count += oddCount;
        evenCount++;
      } else {
        count += evenCount;
        oddCount++;
      }
      if (count >= _MOD) count %= _MOD;
    }

    return count % _MOD;
  }
}
```

## Golang

```go
func numOfSubarrays(arr []int) int {
	const mod int64 = 1000000007
	var evenCount, oddCount int64 = 1, 0
	var ans int64
	parity := 0 // cumulative sum parity: 0 = even, 1 = odd

	for _, v := range arr {
		if v&1 == 1 {
			parity ^= 1
		}
		if parity == 0 {
			ans = (ans + oddCount) % mod
			evenCount++
		} else {
			ans = (ans + evenCount) % mod
			oddCount++
		}
	}
	return int(ans)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def num_of_subarrays(arr)
  even_cnt = 1   # empty prefix sum is even
  odd_cnt = 0
  parity = 0     # current prefix sum parity: 0 even, 1 odd
  ans = 0

  arr.each do |v|
    parity ^= (v & 1)          # update parity with current element
    if parity == 0
      ans += odd_cnt
      even_cnt += 1
    else
      ans += even_cnt
      odd_cnt += 1
    end
    ans %= MOD
  end

  ans % MOD
end
```

## Scala

```scala
object Solution {
  def numOfSubarrays(arr: Array[Int]): Int = {
    val MOD = 1000000007L
    var evenCount = 1L   // empty prefix sum is even
    var oddCount = 0L
    var ans = 0L
    var parity = 0       // current prefix sum parity: 0 even, 1 odd

    for (num <- arr) {
      parity ^= (num & 1)
      if (parity == 0) {
        ans += oddCount
        evenCount += 1
      } else {
        ans += evenCount
        oddCount += 1
      }
      if (ans >= MOD) ans %= MOD
    }

    (ans % MOD).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn num_of_subarrays(arr: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut even: i64 = 1; // empty prefix sum is even
        let mut odd: i64 = 0;
        let mut pref: i64 = 0;
        let mut ans: i64 = 0;

        for &v in arr.iter() {
            pref += v as i64;
            if pref % 2 == 0 {
                ans = (ans + odd) % MOD;
                even = (even + 1) % MOD;
            } else {
                ans = (ans + even) % MOD;
                odd = (odd + 1) % MOD;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (num-of-subarrays arr)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst arr) (prefix 0) (even-count 1) (odd-count 0) (ans 0))
    (if (null? lst)
        ans
        (let* ((new-prefix (+ prefix (car lst)))
               (parity (modulo new-prefix 2))
               (add (if (= parity 0) odd-count even-count))
               (new-ans (modulo (+ ans add) MOD))
               (new-even (if (= parity 0) (+ even-count 1) even-count))
               (new-odd (if (= parity 1) (+ odd-count 1) odd-count)))
          (loop (cdr lst) new-prefix new-even new-odd new-ans)))))
```

## Erlang

```erlang
-module(solution).
-export([num_of_subarrays/1]).
-define(MOD, 1000000007).

-spec num_of_subarrays(Arr :: [integer()]) -> integer().
num_of_subarrays(Arr) ->
    {_, _, Count, _} = lists:foldl(
        fun(N, {Even, Odd, Cnt, Par}) ->
            NewPar = (Par + N) band 1,
            case NewPar of
                0 ->
                    NewCnt = (Cnt + Odd) rem ?MOD,
                    {Even + 1, Odd, NewCnt, NewPar};
                1 ->
                    NewCnt = (Cnt + Even) rem ?MOD,
                    {Even, Odd + 1, NewCnt, NewPar}
            end
        end,
        {1, 0, 0, 0},
        Arr),
    Count.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec num_of_subarrays(arr :: [integer]) :: integer
  def num_of_subarrays(arr) do
    mod = 1_000_000_007

    {cnt, _even, _odd, _parity} =
      Enum.reduce(arr, {0, 1, 0, 0}, fn x, {cnt, even, odd, parity} ->
        p = (parity + rem(x, 2)) &&& 1

        if p == 0 do
          new_cnt = (cnt + odd) |> rem(mod)
          {new_cnt, even + 1, odd, p}
        else
          new_cnt = (cnt + even) |> rem(mod)
          {new_cnt, even, odd + 1, p}
        end
      end)

    cnt
  end
end
```
