# 1356. Sort Integers by The Number of 1 Bits

## Cpp

```cpp
class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        sort(arr.begin(), arr.end(), [](int a, int b) {
            int ca = __builtin_popcount(a);
            int cb = __builtin_popcount(b);
            if (ca == cb) return a < b;
            return ca < cb;
        });
        return arr;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] sortByBits(int[] arr) {
        Integer[] boxed = new Integer[arr.length];
        for (int i = 0; i < arr.length; i++) {
            boxed[i] = arr[i];
        }
        Arrays.sort(boxed, (a, b) -> {
            int ca = Integer.bitCount(a);
            int cb = Integer.bitCount(b);
            if (ca != cb) return ca - cb;
            return a - b;
        });
        for (int i = 0; i < arr.length; i++) {
            arr[i] = boxed[i];
        }
        return arr;
    }
}
```

## Python

```python
class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
```

## Python3

```python
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (x.bit_count(), x))
```

## C

```c
#include <stdlib.h>

/* Comparator for sorting by number of 1 bits, then by value */
static int compare(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    int bx = __builtin_popcount(x);
    int by = __builtin_popcount(y);
    if (bx != by) return bx - by;
    return x - y;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortByBits(int* arr, int arrSize, int* returnSize) {
    int *res = (int *)malloc(arrSize * sizeof(int));
    for (int i = 0; i < arrSize; ++i) res[i] = arr[i];
    qsort(res, arrSize, sizeof(int), compare);
    *returnSize = arrSize;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] SortByBits(int[] arr)
    {
        Array.Sort(arr, (a, b) =>
        {
            int ca = CountBits(a);
            int cb = CountBits(b);
            if (ca != cb) return ca - cb;
            return a - b;
        });
        return arr;
    }

    private static int CountBits(int x)
    {
        int cnt = 0;
        while (x != 0)
        {
            x &= (x - 1);
            cnt++;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function(arr) {
    const bitCount = (num) => {
        let cnt = 0;
        while (num) {
            num &= (num - 1);
            cnt++;
        }
        return cnt;
    };
    
    arr.sort((a, b) => {
        const ca = bitCount(a);
        const cb = bitCount(b);
        if (ca !== cb) return ca - cb;
        return a - b;
    });
    return arr;
};
```

## Typescript

```typescript
function sortByBits(arr: number[]): number[] {
    const bitCount = (n: number): number => {
        let cnt = 0;
        while (n) {
            n &= n - 1;
            cnt++;
        }
        return cnt;
    };
    arr.sort((a, b) => {
        const ca = bitCount(a);
        const cb = bitCount(b);
        if (ca === cb) return a - b;
        return ca - cb;
    });
    return arr;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function sortByBits($arr) {
        // Precompute bit counts for each value to avoid repeated calculations.
        $bitCountMap = [];
        foreach ($arr as $val) {
            $bitCountMap[$val] = $this->countBits($val);
        }

        usort($arr, function ($a, $b) use ($bitCountMap) {
            if ($bitCountMap[$a] === $bitCountMap[$b]) {
                return $a <=> $b; // tie‑break by numeric value
            }
            return $bitCountMap[$a] <=> $bitCountMap[$b];
        });

        return $arr;
    }

    /**
     * Count the number of set bits (1s) in an integer using Brian Kernighan's algorithm.
     *
     * @param int $num
     * @return int
     */
    private function countBits($num) {
        $cnt = 0;
        while ($num > 0) {
            $num &= ($num - 1);
            $cnt++;
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func sortByBits(_ arr: [Int]) -> [Int] {
        return arr.sorted { (a, b) -> Bool in
            let countA = a.nonzeroBitCount
            let countB = b.nonzeroBitCount
            if countA == countB {
                return a < b
            } else {
                return countA < countB
            }
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sortByBits(arr: IntArray): IntArray {
        return arr.sortedWith(compareBy<Int>({ Integer.bitCount(it) }, { it })).toIntArray()
    }
}
```

## Dart

```dart
class Solution {
  List<int> sortByBits(List<int> arr) {
    final Map<int, int> bitCache = {};
    int countBits(int x) {
      int cnt = 0;
      while (x > 0) {
        cnt++;
        x &= x - 1;
      }
      return cnt;
    }

    List<int> result = List.from(arr);
    result.sort((a, b) {
      int bitsA = bitCache.putIfAbsent(a, () => countBits(a));
      int bitsB = bitCache.putIfAbsent(b, () => countBits(b));
      if (bitsA != bitsB) return bitsA - bitsB;
      return a - b;
    });
    return result;
  }
}
```

## Golang

```go
package main

import (
	"math/bits"
	"sort"
)

func sortByBits(arr []int) []int {
	sort.Slice(arr, func(i, j int) bool {
		ci := bits.OnesCount(uint(arr[i]))
		cj := bits.OnesCount(uint(arr[j]))
		if ci == cj {
			return arr[i] < arr[j]
		}
		return ci < cj
	})
	return arr
}
```

## Ruby

```ruby
def sort_by_bits(arr)
  arr.sort_by { |x| [x.to_s(2).count('1'), x] }
end
```

## Scala

```scala
object Solution {
    def sortByBits(arr: Array[Int]): Array[Int] = {
        arr.sortBy(num => (Integer.bitCount(num), num))
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sort_by_bits(mut arr: Vec<i32>) -> Vec<i32> {
        arr.sort_by_key(|&x| (x.count_ones(), x));
        arr
    }
}
```

## Racket

```racket
#lang racket
(require racket/list
         racket/bitwise)

(define/contract (sort-by-bits arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  (letrec ((bit-count
            (lambda (n)
              (if (= n 0)
                  0
                  (+ 1 (bit-count (bitwise-and n (- n 1))))))))
    (sort arr
          (lambda (a b)
            (let ((ca (bit-count a))
                  (cb (bit-count b)))
              (if (= ca cb)
                  (< a b)
                  (< ca cb)))))))
```

## Erlang

```erlang
-module(solution).
-export([sort_by_bits/1]).

-spec sort_by_bits(Arr :: [integer()]) -> [integer()].
sort_by_bits(Arr) ->
    Comparator = fun(A, B) ->
        CA = popcnt(A),
        CB = popcnt(B),
        case CA < CB of
            true -> true;
            false ->
                case CA > CB of
                    true -> false;
                    false -> A =< B
                end
        end
    end,
    lists:sort(Comparator, Arr).

popcnt(N) when N >= 0 -> popcnt(N, 0).
popcnt(0, Acc) -> Acc;
popcnt(N, Acc) ->
    popcnt(N band (N - 1), Acc + 1).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec sort_by_bits(arr :: [integer]) :: [integer]
  def sort_by_bits(arr) do
    Enum.sort_by(arr, fn x -> {bit_count(x), x} end)
  end

  defp bit_count(0), do: 0
  defp bit_count(n) when n > 0 do
    1 + bit_count(band(n, n - 1))
  end
end
```
