# 2094. Finding 3-Digit Even Numbers

## Cpp

```cpp
class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        const int MAX_NUM = 1000;
        vector<bool> seen(MAX_NUM, false);
        int n = digits.size();
        for (int i = 0; i < n; ++i) {
            if (digits[i] == 0) continue; // leading zero not allowed
            for (int j = 0; j < n; ++j) {
                if (j == i) continue;
                for (int k = 0; k < n; ++k) {
                    if (k == i || k == j) continue;
                    int num = digits[i] * 100 + digits[j] * 10 + digits[k];
                    if ((num % 2) == 0) {
                        seen[num] = true;
                    }
                }
            }
        }
        vector<int> result;
        for (int num = 100; num < MAX_NUM; ++num) {
            if (seen[num]) result.push_back(num);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] findEvenNumbers(int[] digits) {
        int[] freq = new int[10];
        for (int d : digits) {
            freq[d]++;
        }
        java.util.List<Integer> list = new java.util.ArrayList<>();
        for (int num = 100; num <= 999; num += 2) { // only even numbers
            int a = num / 100;
            int b = (num / 10) % 10;
            int c = num % 10;
            int[] need = new int[10];
            need[a]++;
            need[b]++;
            need[c]++;
            boolean ok = true;
            for (int d = 0; d < 10; d++) {
                if (need[d] > freq[d]) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                list.add(num);
            }
        }
        int[] result = new int[list.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = list.get(i);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        freq = [0] * 10
        for d in digits:
            freq[d] += 1

        result = []
        for num in range(100, 1000, 2):  # only even numbers
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            need = [0] * 10
            need[a] += 1
            need[b] += 1
            need[c] += 1

            for d in range(10):
                if need[d] > freq[d]:
                    break
            else:
                result.append(num)

        return result
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        res = []
        for num in range(100, 1000, 2):
            a = num // 100
            b = (num // 10) % 10
            c = num % 10
            need = Counter((a, b, c))
            if all(need[d] <= freq.get(d, 0) for d in need):
                res.append(num)
        return res
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findEvenNumbers(int* digits, int digitsSize, int* returnSize) {
    int freq[10] = {0};
    for (int i = 0; i < digitsSize; ++i) {
        freq[digits[i]]++;
    }
    
    int temp[500];
    int cnt = 0;
    
    for (int h = 1; h <= 9; ++h) {               // hundreds digit cannot be zero
        if (freq[h] == 0) continue;
        for (int t = 0; t <= 9; ++t) {           // tens digit
            if (freq[t] == 0 && t != h) continue; // quick prune, but will verify later
            for (int u = 0; u <= 8; u += 2) {    // units digit must be even
                int need[10] = {0};
                need[h]++;
                need[t]++;
                need[u]++;
                
                int ok = 1;
                for (int d = 0; d < 10; ++d) {
                    if (need[d] > freq[d]) {
                        ok = 0;
                        break;
                    }
                }
                if (ok) {
                    temp[cnt++] = h * 100 + t * 10 + u;
                }
            }
        }
    }
    
    // The generation order is already increasing, but ensure sorting just in case
    for (int i = 0; i < cnt - 1; ++i) {
        for (int j = i + 1; j < cnt; ++j) {
            if (temp[i] > temp[j]) {
                int tmp = temp[i];
                temp[i] = temp[j];
                temp[j] = tmp;
            }
        }
    }
    
    int* result = (int*)malloc(cnt * sizeof(int));
    for (int i = 0; i < cnt; ++i) {
        result[i] = temp[i];
    }
    *returnSize = cnt;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] FindEvenNumbers(int[] digits)
    {
        var n = digits.Length;
        var seen = new HashSet<int>();
        for (int i = 0; i < n; i++)
        {
            if (digits[i] == 0) continue; // leading zero not allowed
            for (int j = 0; j < n; j++)
            {
                if (j == i) continue;
                for (int k = 0; k < n; k++)
                {
                    if (k == i || k == j) continue;
                    if ((digits[k] & 1) != 0) continue; // must be even
                    int num = digits[i] * 100 + digits[j] * 10 + digits[k];
                    seen.Add(num);
                }
            }
        }

        var result = new int[seen.Count];
        seen.CopyTo(result);
        Array.Sort(result);
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var findEvenNumbers = function(digits) {
    const freq = new Array(10).fill(0);
    for (const d of digits) freq[d]++;

    const result = [];
    for (let num = 100; num <= 999; num += 2) { // only even numbers
        const d1 = Math.floor(num / 100);
        const d2 = Math.floor((num % 100) / 10);
        const d3 = num % 10;

        const cnt = freq.slice();
        cnt[d1]--;
        cnt[d2]--;
        cnt[d3]--;

        if (cnt[d1] >= 0 && cnt[d2] >= 0 && cnt[d3] >= 0) {
            result.push(num);
        }
    }
    return result;
};
```

## Typescript

```typescript
function findEvenNumbers(digits: number[]): number[] {
    const n = digits.length;
    const seen = new Set<number>();
    for (let i = 0; i < n; i++) {
        if (digits[i] === 0) continue; // leading zero not allowed
        for (let j = 0; j < n; j++) {
            if (j === i) continue;
            for (let k = 0; k < n; k++) {
                if (k === i || k === j) continue;
                const d3 = digits[k];
                if ((d3 & 1) === 1) continue; // must be even
                const num = digits[i] * 100 + digits[j] * 10 + d3;
                seen.add(num);
            }
        }
    }
    const result = Array.from(seen);
    result.sort((a, b) => a - b);
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $digits
     * @return Integer[]
     */
    function findEvenNumbers($digits) {
        $n = count($digits);
        $unique = [];
        for ($i = 0; $i < $n; $i++) {
            if ($digits[$i] == 0) continue; // leading zero not allowed
            for ($j = 0; $j < $n; $j++) {
                if ($j == $i) continue;
                for ($k = 0; $k < $n; $k++) {
                    if ($k == $i || $k == $j) continue;
                    $num = $digits[$i] * 100 + $digits[$j] * 10 + $digits[$k];
                    if (($num & 1) === 0) { // even check
                        $unique[$num] = true;
                    }
                }
            }
        }
        $result = array_keys($unique);
        sort($result, SORT_NUMERIC);
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findEvenNumbers(_ digits: [Int]) -> [Int] {
        var set = Set<Int>()
        let n = digits.count
        for i in 0..<n where digits[i] != 0 {
            for j in 0..<n where j != i {
                for k in 0..<n where k != i && k != j {
                    let num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num % 2 == 0 {
                        set.insert(num)
                    }
                }
            }
        }
        var result = Array(set)
        result.sort()
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findEvenNumbers(digits: IntArray): IntArray {
        val freq = IntArray(10)
        for (d in digits) freq[d]++

        val result = mutableListOf<Int>()
        for (num in 100..999 step 2) { // only even numbers
            var x = num
            val c = x % 10; x /= 10
            val b = x % 10; x /= 10
            val a = x

            if (freq[a] == 0 || freq[b] == 0 || freq[c] == 0) continue

            var ok = true
            val need = IntArray(10)
            need[a]++
            need[b]++
            need[c]++

            for (d in 0..9) {
                if (need[d] > freq[d]) {
                    ok = false
                    break
                }
            }

            if (ok) result.add(num)
        }
        return result.toIntArray()
    }
}
```

## Dart

```dart
class Solution {
  List<int> findEvenNumbers(List<int> digits) {
    final Set<int> result = {};
    int n = digits.length;
    for (int i = 0; i < n; i++) {
      if (digits[i] == 0) continue; // leading zero not allowed
      for (int j = 0; j < n; j++) {
        if (j == i) continue;
        for (int k = 0; k < n; k++) {
          if (k == i || k == j) continue;
          int d3 = digits[k];
          if (d3 % 2 != 0) continue; // must be even
          int num = digits[i] * 100 + digits[j] * 10 + d3;
          result.add(num);
        }
      }
    }
    List<int> ans = result.toList();
    ans.sort();
    return ans;
  }
}
```

## Golang

```go
package main

import "sort"

func findEvenNumbers(digits []int) []int {
	n := len(digits)
	seen := make(map[int]struct{})
	for i := 0; i < n; i++ {
		if digits[i] == 0 { // leading zero not allowed
			continue
		}
		for j := 0; j < n; j++ {
			if j == i {
				continue
			}
			for k := 0; k < n; k++ {
				if k == i || k == j {
					continue
				}
				num := digits[i]*100 + digits[j]*10 + digits[k]
				if num%2 == 0 {
					seen[num] = struct{}{}
				}
			}
		}
	}
	res := make([]int, 0, len(seen))
	for v := range seen {
		res = append(res, v)
	}
	sort.Ints(res)
	return res
}
```

## Ruby

```ruby
def find_even_numbers(digits)
  n = digits.length
  seen = {}
  result = []

  (0...n).each do |i|
    d1 = digits[i]
    next if d1 == 0
    (0...n).each do |j|
      next if j == i
      d2 = digits[j]
      (0...n).each do |k|
        next if k == i || k == j
        d3 = digits[k]
        num = d1 * 100 + d2 * 10 + d3
        next unless num.even?
        unless seen.key?(num)
          seen[num] = true
          result << num
        end
      end
    end
  end

  result.sort
end
```

## Scala

```scala
object Solution {
    def findEvenNumbers(digits: Array[Int]): Array[Int] = {
        val freq = new Array[Int](10)
        for (d <- digits) freq(d) += 1

        val result = scala.collection.mutable.ArrayBuffer[Int]()
        var num = 100
        while (num <= 999) {
            if ((num & 1) == 0) { // even check
                val d0 = num / 100
                val d1 = (num / 10) % 10
                val d2 = num % 10

                val need = new Array[Int](10)
                need(d0) += 1
                need(d1) += 1
                need(d2) += 1

                var ok = true
                var i = 0
                while (i < 10 && ok) {
                    if (need(i) > freq(i)) ok = false
                    i += 1
                }
                if (ok) result += num
            }
            num += 2 // next even number
        }
        result.toArray
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn find_even_numbers(digits: Vec<i32>) -> Vec<i32> {
        let n = digits.len();
        let mut set: HashSet<i32> = HashSet::new();

        for i in 0..n {
            if digits[i] == 0 {
                continue; // leading zero not allowed
            }
            for j in 0..n {
                if j == i {
                    continue;
                }
                for k in 0..n {
                    if k == i || k == j {
                        continue;
                    }
                    let d3 = digits[k];
                    if d3 % 2 != 0 {
                        continue; // must be even
                    }
                    let num = digits[i] * 100 + digits[j] * 10 + d3;
                    set.insert(num);
                }
            }
        }

        let mut result: Vec<i32> = set.into_iter().collect();
        result.sort_unstable();
        result
    }
}
```

## Racket

```racket
#lang racket

(define/contract (find-even-numbers digits)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let ((freq (make-vector 10 0)))
    (for ([d digits])
      (vector-set! freq d (+ 1 (vector-ref freq d))))
    (define (can-form? n)
      (let* ((d1 (quotient n 100))
             (rem (remainder n 100))
             (d2 (quotient rem 10))
             (d3 (remainder rem 10)))
        (if (= d1 0) #f
            (let ((need (make-vector 10 0)))
              (vector-set! need d1 (+ 1 (vector-ref need d1)))
              (vector-set! need d2 (+ 1 (vector-ref need d2)))
              (vector-set! need d3 (+ 1 (vector-ref need d3)))
              (let loop ((i 0))
                (cond [(= i 10) #t]
                      [(> (vector-ref need i) (vector-ref freq i)) #f]
                      [else (loop (+ i 1))]))))))
    (for/list ([n (in-range 100 1000 2)]
               #:when (can-form? n))
      n)))
```

## Erlang

```erlang
-module(solution).
-export([find_even_numbers/1]).

-spec find_even_numbers([integer()]) -> [integer()].
find_even_numbers(Digits) ->
    Freq = build_freq(Digits),
    [N || N <- lists:seq(100, 998, 2), can_form(N, Freq)].

build_freq(Digits) ->
    lists:foldl(
        fun(D, Acc) ->
            maps:update_with(
                D,
                fun(C) -> C + 1 end,
                1,
                Acc)
        end,
        #{},
        Digits).

can_form(Number, Freq) ->
    D1 = Number div 100,
    D2 = (Number div 10) rem 10,
    D3 = Number rem 10,
    case maps:get(D1, Freq, 0) of
        C1 when C1 > 0 ->
            F1 = maps:update_with(
                    D1,
                    fun(C) -> C - 1 end,
                    Freq),
            case maps:get(D2, F1, 0) of
                C2 when C2 > 0 ->
                    F2 = maps:update_with(
                            D2,
                            fun(C) -> C - 1 end,
                            F1),
                    case maps:get(D3, F2, 0) of
                        C3 when C3 > 0 -> true;
                        _ -> false
                    end;
                _ -> false
            end;
        _ -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_even_numbers(digits :: [integer]) :: [integer]
  def find_even_numbers(digits) do
    arr = List.to_tuple(digits)
    n = tuple_size(arr)

    numbers =
      for i <- 0..(n - 1),
          j <- 0..(n - 1),
          k <- 0..(n - 1),
          i != j,
          i != k,
          j != k do
        d1 = elem(arr, i)

        if d1 == 0 do
          nil
        else
          d2 = elem(arr, j)
          d3 = elem(arr, k)
          num = d1 * 100 + d2 * 10 + d3

          if rem(num, 2) == 0, do: num, else: nil
        end
      end
      |> Enum.filter(& &1)
      |> MapSet.new()
      |> MapSet.to_list()
      |> Enum.sort()

    numbers
  end
end
```
