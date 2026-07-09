# 1122. Relative Sort Array

## Cpp

```cpp
class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        const int MAX_VAL = 1000;
        vector<int> count(MAX_VAL + 1, 0);
        for (int num : arr1) ++count[num];
        
        vector<int> result;
        result.reserve(arr1.size());
        
        for (int num : arr2) {
            while (count[num]--) {
                result.push_back(num);
            }
        }
        for (int i = 0; i <= MAX_VAL; ++i) {
            while (count[i]--) {
                result.push_back(i);
            }
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int maxVal = 1000; // given constraints: 0 <= value <= 1000
        int[] count = new int[maxVal + 1];
        for (int num : arr1) {
            count[num]++;
        }
        int[] result = new int[arr1.length];
        int idx = 0;
        for (int num : arr2) {
            while (count[num] > 0) {
                result[idx++] = num;
                count[num]--;
            }
        }
        for (int i = 0; i <= maxVal; i++) {
            while (count[i] > 0) {
                result[idx++] = i;
                count[i]--;
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # Since values are in range 0..1000, use counting sort
        max_val = 1000
        count = [0] * (max_val + 1)
        for num in arr1:
            count[num] += 1

        result = []
        for num in arr2:
            if count[num]:
                result.extend([num] * count[num])
                count[num] = 0

        for num in range(max_val + 1):
            if count[num]:
                result.extend([num] * count[num])

        return result
```

## Python3

```python
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Since values are in the range 0..1000, use a fixed-size count array.
        max_val = 1000
        count = [0] * (max_val + 1)
        for num in arr1:
            count[num] += 1

        result: List[int] = []
        # Add elements that appear in arr2 preserving the order of arr2.
        for num in arr2:
            cnt = count[num]
            if cnt:
                result.extend([num] * cnt)
                count[num] = 0  # reset to avoid adding again later

        # Append remaining numbers in ascending order.
        for num in range(max_val + 1):
            cnt = count[num]
            if cnt:
                result.extend([num] * cnt)

        return result
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* relativeSortArray(int* arr1, int arr1Size, int* arr2, int arr2Size, int* returnSize) {
    // Since 0 <= value <= 1000
    const int MAX_VAL = 1000;
    int count[MAX_VAL + 1] = {0};

    for (int i = 0; i < arr1Size; ++i) {
        count[arr1[i]]++;
    }

    int* result = (int*)malloc(sizeof(int) * arr1Size);
    int idx = 0;

    // Place elements according to arr2 order
    for (int i = 0; i < arr2Size; ++i) {
        int val = arr2[i];
        while (count[val] > 0) {
            result[idx++] = val;
            count[val]--;
        }
    }

    // Place remaining elements in ascending order
    for (int val = 0; val <= MAX_VAL; ++val) {
        while (count[val] > 0) {
            result[idx++] = val;
            count[val]--;
        }
    }

    *returnSize = arr1Size;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[] RelativeSortArray(int[] arr1, int[] arr2) {
        const int MAX_VAL = 1000;
        int[] count = new int[MAX_VAL + 1];
        foreach (int num in arr1) {
            count[num]++;
        }

        List<int> result = new List<int>(arr1.Length);
        foreach (int num in arr2) {
            while (count[num] > 0) {
                result.Add(num);
                count[num]--;
            }
        }

        for (int i = 0; i <= MAX_VAL; i++) {
            while (count[i] > 0) {
                result.Add(i);
                count[i]--;
            }
        }

        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var relativeSortArray = function(arr1, arr2) {
    const MAX_VAL = 1000; // given constraint: 0 <= value <= 1000
    const count = new Array(MAX_VAL + 1).fill(0);
    
    for (const num of arr1) {
        count[num]++;
    }
    
    const result = [];
    
    // Add elements in the order defined by arr2
    for (const num of arr2) {
        while (count[num] > 0) {
            result.push(num);
            count[num]--;
        }
    }
    
    // Add remaining elements in ascending order
    for (let i = 0; i <= MAX_VAL; i++) {
        while (count[i] > 0) {
            result.push(i);
            count[i]--;
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function relativeSortArray(arr1: number[], arr2: number[]): number[] {
    const MAX = 1000;
    const count = new Array(MAX + 1).fill(0);
    for (const num of arr1) {
        count[num]++;
    }
    const result: number[] = [];
    for (const num of arr2) {
        while (count[num] > 0) {
            result.push(num);
            count[num]--;
        }
    }
    for (let i = 0; i <= MAX; i++) {
        while (count[i] > 0) {
            result.push(i);
            count[i]--;
        }
    }
    return result;
}
```

## Php

```php
<?php
class Solution {

    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer[]
     */
    function relativeSortArray($arr1, $arr2) {
        // Since values are in range 0..1000, use a fixed-size count array.
        $maxVal = 1000;
        $count = array_fill(0, $maxVal + 1, 0);
        
        foreach ($arr1 as $num) {
            $count[$num]++;
        }
        
        $result = [];
        
        // Add elements according to the order in arr2.
        foreach ($arr2 as $num) {
            while ($count[$num] > 0) {
                $result[] = $num;
                $count[$num]--;
            }
        }
        
        // Append remaining elements in ascending order.
        for ($i = 0; $i <= $maxVal; $i++) {
            while ($count[$i] > 0) {
                $result[] = $i;
                $count[$i]--;
            }
        }
        
        return $result;
    }
}
?>
```

## Swift

```swift
class Solution {
    func relativeSortArray(_ arr1: [Int], _ arr2: [Int]) -> [Int] {
        var count = [Int](repeating: 0, count: 1001)
        for num in arr1 {
            count[num] += 1
        }
        
        var result = [Int]()
        for num in arr2 {
            let c = count[num]
            if c > 0 {
                result.append(contentsOf: Array(repeating: num, count: c))
                count[num] = 0
            }
        }
        
        for i in 0..<count.count {
            let c = count[i]
            if c > 0 {
                result.append(contentsOf: Array(repeating: i, count: c))
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun relativeSortArray(arr1: IntArray, arr2: IntArray): IntArray {
        val maxVal = 1000
        val count = IntArray(maxVal + 1)
        for (num in arr1) {
            count[num]++
        }
        val result = IntArray(arr1.size)
        var idx = 0
        for (num in arr2) {
            while (count[num] > 0) {
                result[idx++] = num
                count[num]--
            }
        }
        for (i in 0..maxVal) {
            while (count[i] > 0) {
                result[idx++] = i
                count[i]--
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> relativeSortArray(List<int> arr1, List<int> arr2) {
    const int maxVal = 1000;
    List<int> cnt = List.filled(maxVal + 1, 0);
    for (int num in arr1) {
      cnt[num]++;
    }
    List<int> res = [];
    for (int num in arr2) {
      int c = cnt[num];
      for (int i = 0; i < c; i++) {
        res.add(num);
      }
      cnt[num] = 0;
    }
    for (int i = 0; i <= maxVal; i++) {
      int c = cnt[i];
      for (int j = 0; j < c; j++) {
        res.add(i);
      }
    }
    return res;
  }
}
```

## Golang

```go
func relativeSortArray(arr1 []int, arr2 []int) []int {
	const maxVal = 1000
	count := make([]int, maxVal+1)
	for _, v := range arr1 {
		count[v]++
	}
	result := make([]int, 0, len(arr1))
	for _, v := range arr2 {
		for count[v] > 0 {
			result = append(result, v)
			count[v]--
		}
	}
	for i := 0; i <= maxVal; i++ {
		for count[i] > 0 {
			result = append(result, i)
			count[i]--
		}
	}
	return result
}
```

## Ruby

```ruby
def relative_sort_array(arr1, arr2)
  max_val = 1000
  count = Array.new(max_val + 1, 0)
  arr1.each { |num| count[num] += 1 }

  result = []

  arr2.each do |num|
    cnt = count[num]
    result.concat([num] * cnt) if cnt > 0
    count[num] = 0
  end

  (0..max_val).each do |i|
    cnt = count[i]
    next if cnt == 0
    result.concat([i] * cnt)
  end

  result
end
```

## Scala

```scala
object Solution {
    def relativeSortArray(arr1: Array[Int], arr2: Array[Int]): Array[Int] = {
        val maxVal = 1000
        val count = new Array[Int](maxVal + 1)
        for (v <- arr1) count(v) += 1

        val result = scala.collection.mutable.ArrayBuffer[Int]()

        for (v <- arr2) {
            var c = count(v)
            while (c > 0) {
                result += v
                c -= 1
            }
            count(v) = 0
        }

        for (i <- 0 to maxVal) {
            var c = count(i)
            while (c > 0) {
                result += i
                c -= 1
            }
        }

        result.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn relative_sort_array(arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {
        let mut count = vec![0usize; 1001];
        for &num in &arr1 {
            count[num as usize] += 1;
        }
        let mut result = Vec::with_capacity(arr1.len());
        for &num in &arr2 {
            let idx = num as usize;
            while count[idx] > 0 {
                result.push(num);
                count[idx] -= 1;
            }
        }
        for i in 0..=1000 {
            while count[i] > 0 {
                result.push(i as i32);
                count[i] -= 1;
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (relative-sort-array arr1 arr2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((max-val (if (null? arr1) 0 (apply max arr1)))
         (count   (make-vector (+ max-val 1) 0))
         (builder '()))
    ;; Count frequencies in arr1
    (for-each (lambda (x)
                (vector-set! count x (+ 1 (vector-ref count x))))
              arr1)
    ;; Helper to prepend cnt copies of val onto builder
    (define (add-copies val cnt)
      (let loop ((i cnt) (lst builder))
        (if (= i 0)
            (set! builder lst)
            (loop (- i 1) (cons val lst)))))
    ;; Add elements following the order in arr2
    (for-each (lambda (x)
                (let ((c (vector-ref count x)))
                  (when (> c 0)
                    (add-copies x c))
                  (vector-set! count x 0)))
              arr2)
    ;; Add remaining elements in ascending order
    (for ([i (in-range (vector-length count))])
      (let ((c (vector-ref count i)))
        (when (> c 0)
          (add-copies i c))))
    (reverse builder)))
```

## Erlang

```erlang
relative_sort_array(Arr1, Arr2) ->
    CountMap = count_map(Arr1, #{}),
    {RemMap, List1} = build_from_arr2(Arr2, CountMap),
    List2 = build_rest(RemMap),
    lists:append([List1, List2]).

count_map([], M) -> M;
count_map([H|T], M) ->
    NewM = maps:update_with(H, fun(C) -> C + 1 end, 1, M),
    count_map(T, NewM).

build_from_arr2([], M) -> {M, []};
build_from_arr2([V|Rest], M) ->
    C = maps:get(V, M, 0),
    Dup = lists:duplicate(C, V),
    NewM = case C of
        0 -> M;
        _ -> maps:remove(V, M)
    end,
    {FinalMap, RestList} = build_from_arr2(Rest, NewM),
    {FinalMap, Dup ++ RestList}.

build_rest(M) ->
    Keys = maps:keys(M),
    Sorted = lists:sort(Keys),
    build_rest(Sorted, M, []).

build_rest([], _, Acc) -> lists:flatten(lists:reverse(Acc));
build_rest([K|Rest], M, Acc) ->
    C = maps:get(K, M),
    Dup = lists:duplicate(C, K),
    build_rest(Rest, M, [Dup | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec relative_sort_array(arr1 :: [integer], arr2 :: [integer]) :: [integer]
  def relative_sort_array(arr1, arr2) do
    order = Map.new(Enum.with_index(arr2), fn {v, i} -> {v, i} end)

    Enum.sort_by(arr1, fn x ->
      case Map.fetch(order, x) do
        {:ok, idx} -> {0, idx}
        :error -> {1, x}
      end
    end)
  end
end
```
