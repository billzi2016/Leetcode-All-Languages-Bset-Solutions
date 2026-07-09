# 2657. Find the Prefix Common Array of Two Arrays

## Cpp

```cpp
class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        int n = A.size();
        vector<int> freq(n + 1, 0);
        vector<int> ans(n);
        int common = 0;
        for (int i = 0; i < n; ++i) {
            if (++freq[A[i]] == 2) ++common;
            if (++freq[B[i]] == 2) ++common;
            ans[i] = common;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int n = A.length;
        int[] freq = new int[n + 1];
        int[] result = new int[n];
        int common = 0;
        for (int i = 0; i < n; i++) {
            if (++freq[A[i]] == 2) {
                common++;
            }
            if (++freq[B[i]] == 2) {
                common++;
            }
            result[i] = common;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        freq = [0] * (n + 1)
        common = 0
        res = []
        for i in range(n):
            a = A[i]
            freq[a] += 1
            if freq[a] == 2:
                common += 1
            b = B[i]
            freq[b] += 1
            if freq[b] == 2:
                common += 1
            res.append(common)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0] * (n + 1)
        common = 0
        result = []
        for i in range(n):
            a = A[i]
            freq[a] += 1
            if freq[a] == 2:
                common += 1
            b = B[i]
            freq[b] += 1
            if freq[b] == 2:
                common += 1
            result.append(common)
        return result
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findThePrefixCommonArray(int* A, int ASize, int* B, int BSize, int* returnSize) {
    int n = ASize;  // ASize == BSize
    int *freq = (int *)calloc(n + 1, sizeof(int));
    int *res = (int *)malloc(n * sizeof(int));
    int common = 0;
    
    for (int i = 0; i < n; ++i) {
        int a = A[i];
        if (++freq[a] == 2) {
            ++common;
        }
        int b = B[i];
        if (++freq[b] == 2) {
            ++common;
        }
        res[i] = common;
    }
    
    free(freq);
    *returnSize = n;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] FindThePrefixCommonArray(int[] A, int[] B)
    {
        int n = A.Length;
        int[] freq = new int[n + 1];
        int common = 0;
        int[] result = new int[n];

        for (int i = 0; i < n; i++)
        {
            if (++freq[A[i]] == 2) common++;
            if (++freq[B[i]] == 2) common++;
            result[i] = common;
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var findThePrefixCommonArray = function(A, B) {
    const n = A.length;
    const freq = new Array(n + 1).fill(0);
    const result = new Array(n);
    let common = 0;
    for (let i = 0; i < n; ++i) {
        const a = A[i];
        if (++freq[a] === 2) ++common;
        const b = B[i];
        if (++freq[b] === 2) ++common;
        result[i] = common;
    }
    return result;
};
```

## Typescript

```typescript
function findThePrefixCommonArray(A: number[], B: number[]): number[] {
    const n = A.length;
    const freq = new Array(n + 1).fill(0);
    const result: number[] = new Array(n);
    let common = 0;
    for (let i = 0; i < n; i++) {
        if (++freq[A[i]] === 2) common++;
        if (++freq[B[i]] === 2) common++;
        result[i] = common;
    }
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $A
     * @param Integer[] $B
     * @return Integer[]
     */
    function findThePrefixCommonArray($A, $B) {
        $n = count($A);
        $freq = array_fill(0, $n + 1, 0);
        $common = 0;
        $result = [];
        for ($i = 0; $i < $n; $i++) {
            $x = $A[$i];
            $freq[$x]++;
            if ($freq[$x] == 2) {
                $common++;
            }
            $y = $B[$i];
            $freq[$y]++;
            if ($freq[$y] == 2) {
                $common++;
            }
            $result[] = $common;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findThePrefixCommonArray(_ A: [Int], _ B: [Int]) -> [Int] {
        let n = A.count
        var freq = Array(repeating: 0, count: n + 1)
        var common = 0
        var result = [Int]()
        result.reserveCapacity(n)
        
        for i in 0..<n {
            let a = A[i]
            freq[a] += 1
            if freq[a] == 2 { common += 1 }
            
            let b = B[i]
            freq[b] += 1
            if freq[b] == 2 { common += 1 }
            
            result.append(common)
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findThePrefixCommonArray(A: IntArray, B: IntArray): IntArray {
        val n = A.size
        val freq = IntArray(n + 1)
        var common = 0
        val result = IntArray(n)
        for (i in 0 until n) {
            val a = A[i]
            if (++freq[a] == 2) common++
            val b = B[i]
            if (++freq[b] == 2) common++
            result[i] = common
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findThePrefixCommonArray(List<int> A, List<int> B) {
    int n = A.length;
    List<int> freq = List.filled(n + 1, 0);
    int common = 0;
    List<int> result = [];
    for (int i = 0; i < n; i++) {
      int a = A[i];
      freq[a] += 1;
      if (freq[a] == 2) common++;
      int b = B[i];
      freq[b] += 1;
      if (freq[b] == 2) common++;
      result.add(common);
    }
    return result;
  }
}
```

## Golang

```go
func findThePrefixCommonArray(A []int, B []int) []int {
    n := len(A)
    freq := make([]int, n+1)
    res := make([]int, n)
    common := 0
    for i := 0; i < n; i++ {
        x := A[i]
        freq[x]++
        if freq[x] == 2 {
            common++
        }
        y := B[i]
        freq[y]++
        if freq[y] == 2 {
            common++
        }
        res[i] = common
    }
    return res
}
```

## Ruby

```ruby
# @param {Integer[]} a
# @param {Integer[]} b
# @return {Integer[]}
def find_the_prefix_common_array(a, b)
  n = a.length
  freq = Array.new(n + 1, 0)
  common = 0
  result = []

  (0...n).each do |i|
    x = a[i]
    freq[x] += 1
    common += 1 if freq[x] == 2

    y = b[i]
    freq[y] += 1
    common += 1 if freq[y] == 2

    result << common
  end

  result
end
```

## Scala

```scala
object Solution {
    def findThePrefixCommonArray(A: Array[Int], B: Array[Int]): Array[Int] = {
        val n = A.length
        val freq = new Array[Int](n + 1)
        var common = 0
        val res = new Array[Int](n)
        for (i <- 0 until n) {
            val a = A(i)
            freq(a) += 1
            if (freq(a) == 2) common += 1
            val b = B(i)
            freq(b) += 1
            if (freq(b) == 2) common += 1
            res(i) = common
        }
        res
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn find_the_prefix_common_array(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
        let n = a.len();
        let mut freq = vec![0i32; n + 1];
        let mut common = 0;
        let mut result = Vec::with_capacity(n);
        for i in 0..n {
            let ai = a[i] as usize;
            freq[ai] += 1;
            if freq[ai] == 2 {
                common += 1;
            }
            let bi = b[i] as usize;
            freq[bi] += 1;
            if freq[bi] == 2 {
                common += 1;
            }
            result.push(common);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (find-the-prefix-common-array A B)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length A))
         (freq (make-vector (+ n 1) 0)))
    (let loop ((i 0) (common 0) (as A) (bs B) (acc '()))
      (if (= i n)
          (reverse acc)
          (let* ((a (car as))
                 (prev-a (vector-ref freq a)))
            (vector-set! freq a (+ prev-a 1))
            (let ((inc-a (if (= (vector-ref freq a) 2) 1 0))
                  (b (car bs))
                  (prev-b (vector-ref freq b)))
              (vector-set! freq b (+ prev-b 1))
              (let ((inc-b (if (= (vector-ref freq b) 2) 1 0))
                    (new-common (+ common inc-a inc-b)))
                (loop (+ i 1) new-common (cdr as) (cdr bs) (cons new-common acc)))))))))
```

## Erlang

```erlang
-spec find_the_prefix_common_array([integer()], [integer()]) -> [integer()].
find_the_prefix_common_array(A, B) ->
    find_prefix(A, B, #{}, 0, []).

find_prefix([], [], _Map, _Common, AccRev) ->
    lists:reverse(AccRev);
find_prefix([Ah|At], [Bh|Bt], Map, Common, AccRev) ->
    {Map1, Inc1} = inc_if_two(Ah, Map),
    {Map2, Inc2} = inc_if_two(Bh, Map1),
    NewCommon = Common + Inc1 + Inc2,
    find_prefix(At, Bt, Map2, NewCommon, [NewCommon|AccRev]).

inc_if_two(Value, Map) ->
    case maps:get(Value, Map, 0) of
        1 -> {maps:put(Value, 2, Map), 1};
        _ -> {maps:put(Value, maps:get(Value, Map, 0) + 1, Map), 0}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_the_prefix_common_array(a :: [integer], b :: [integer]) :: [integer]
  def find_the_prefix_common_array(a, b) do
    {rev_res, _freq, _} =
      Enum.reduce(Enum.zip(a, b), {[], %{}, 0}, fn {x, y},
                                                   {acc_rev, freq, common} ->
        {freq1, inc1} = incr(freq, x)
        {freq2, inc2} = incr(freq1, y)
        new_common = common + inc1 + inc2
        {[new_common | acc_rev], freq2, new_common}
      end)

    Enum.reverse(rev_res)
  end

  defp incr(freq, key) do
    cnt = Map.get(freq, key, 0) + 1
    inc = if cnt == 2, do: 1, else: 0
    {Map.put(freq, key, cnt), inc}
  end
end
```
