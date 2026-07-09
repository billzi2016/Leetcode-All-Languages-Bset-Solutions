# 1652. Defuse the Bomb

## Cpp

```cpp
class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        vector<int> result(n, 0);
        if (k == 0) return result;
        int steps = abs(k);
        for (int i = 0; i < n; ++i) {
            int sum = 0;
            for (int j = 1; j <= steps; ++j) {
                int idx;
                if (k > 0) {
                    idx = (i + j) % n;
                } else { // k < 0
                    idx = (i - j) % n;
                    if (idx < 0) idx += n;
                }
                sum += code[idx];
            }
            result[i] = sum;
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] decrypt(int[] code, int k) {
        int n = code.length;
        int[] result = new int[n];
        if (k == 0) return result;

        if (k > 0) {
            int sum = 0;
            for (int i = 1; i <= k; i++) {
                sum += code[i % n];
            }
            for (int i = 0; i < n; i++) {
                result[i] = sum;
                int startIdx = (i + 1) % n;
                int endIdx = (i + k + 1) % n;
                sum = sum - code[startIdx] + code[endIdx];
            }
        } else { // k < 0
            int kk = -k;
            int sum = 0;
            for (int i = n - kk; i < n; i++) {
                sum += code[i];
            }
            for (int i = 0; i < n; i++) {
                result[i] = sum;
                int removeIdx = (i - kk + n) % n;
                int addIdx = i;
                sum = sum - code[removeIdx] + code[addIdx];
            }
        }

        return result;
    }
}
```

## Python

```python
class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        res = [0] * n
        if k == 0:
            return res

        if k > 0:
            # sum of next k elements for index 0
            total = sum(code[i % n] for i in range(1, k + 1))
            for i in range(n):
                res[i] = total
                # slide window: remove element at i+1, add element at i+k+1
                total += -code[(i + 1) % n] + code[(i + k + 1) % n]
        else:
            kk = -k
            # sum of previous kk elements for index 0 (indices n-kk .. n-1)
            total = sum(code[i % n] for i in range(n - kk, n))
            for i in range(n):
                res[i] = total
                # slide window: remove element at i-kk, add element at i
                total += -code[(i - kk) % n] + code[i % n]

        return res
```

## Python3

```python
from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res

        if k > 0:
            # initial sum of next k elements for index 0
            total = sum(code[i % n] for i in range(1, k + 1))
            for i in range(n):
                res[i] = total
                # slide window: remove element at i+1, add element at i+1+k
                total -= code[(i + 1) % n]
                total += code[(i + 1 + k) % n]
        else:
            kk = -k
            # initial sum of previous kk elements for index 0 (indices n-kk .. n-1)
            total = sum(code[i] for i in range(n - kk, n))
            for i in range(n):
                res[i] = total
                # slide window: remove element at i-kk, add element at i
                total -= code[(i - kk) % n]
                total += code[i % n]

        return res
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decrypt(int* code, int codeSize, int k, int* returnSize) {
    *returnSize = codeSize;
    int* res = (int*)malloc(sizeof(int) * codeSize);
    if (!res) return NULL;  // safety
    
    if (k == 0) {
        for (int i = 0; i < codeSize; ++i) res[i] = 0;
        return res;
    }
    
    int n = codeSize;
    if (k > 0) {
        long sum = 0;
        for (int j = 1; j <= k; ++j)
            sum += code[j % n];
        for (int i = 0; i < n; ++i) {
            res[i] = (int)sum;
            int outIdx = (i + 1) % n;
            int inIdx  = (i + 1 + k) % n;
            sum = sum - code[outIdx] + code[inIdx];
        }
    } else { // k < 0
        int kk = -k;               // number of previous elements to sum
        long sum = 0;
        for (int j = n - kk; j < n; ++j)
            sum += code[j];
        for (int i = 0; i < n; ++i) {
            res[i] = (int)sum;
            int outIdx = (i - kk + n) % n; // element leaving the window
            int inIdx  = i % n;            // new element entering the window
            sum = sum - code[outIdx] + code[inIdx];
        }
    }
    
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] Decrypt(int[] code, int k) {
        int n = code.Length;
        int[] res = new int[n];
        if (k == 0) return res;

        if (k > 0) {
            long sum = 0;
            for (int i = 1; i <= k; i++) {
                sum += code[i % n];
            }
            for (int i = 0; i < n; i++) {
                res[i] = (int)sum;
                int outIdx = (i + 1) % n;
                int inIdx = (i + k + 1) % n;
                sum = sum - code[outIdx] + code[inIdx];
            }
        } else {
            int kk = -k;
            long sum = 0;
            for (int i = n - kk; i < n; i++) {
                sum += code[i];
            }
            for (int i = 0; i < n; i++) {
                res[i] = (int)sum;
                int outIdx = (i - kk + n) % n;
                int inIdx = i;
                sum = sum - code[outIdx] + code[inIdx];
            }
        }

        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} code
 * @param {number} k
 * @return {number[]}
 */
var decrypt = function(code, k) {
    const n = code.length;
    const res = new Array(n).fill(0);
    if (k === 0) return res;

    if (k > 0) {
        let sum = 0;
        for (let j = 1; j <= k; ++j) {
            sum += code[j % n];
        }
        for (let i = 0; i < n; ++i) {
            res[i] = sum;
            // slide window: remove the element that just left, add the new entering element
            const outIdx = (i + 1) % n;
            const inIdx = (i + k + 1) % n;
            sum = sum - code[outIdx] + code[inIdx];
        }
    } else {
        const kk = -k; // number of previous elements to sum
        let sum = 0;
        for (let j = n - kk; j < n; ++j) {
            sum += code[j % n];
        }
        for (let i = 0; i < n; ++i) {
            res[i] = sum;
            const outIdx = (i - kk + n) % n; // element leaving the window
            const inIdx = i;                 // new element entering the window
            sum = sum - code[outIdx] + code[inIdx];
        }
    }

    return res;
};
```

## Typescript

```typescript
function decrypt(code: number[], k: number): number[] {
    const n = code.length;
    const result = new Array<number>(n);
    if (k === 0) {
        result.fill(0);
        return result;
    }
    if (k > 0) {
        let sum = 0;
        for (let j = 1; j <= k; ++j) {
            sum += code[j % n];
        }
        for (let i = 0; i < n; ++i) {
            result[i] = sum;
            const outIdx = (i + 1) % n;
            const inIdx = (i + k + 1) % n;
            sum = sum - code[outIdx] + code[inIdx];
        }
    } else { // k < 0
        const kk = -k; // number of previous elements to sum
        let sum = 0;
        for (let j = n - kk; j < n; ++j) {
            sum += code[j];
        }
        for (let i = 0; i < n; ++i) {
            result[i] = sum;
            const outIdx = (i - kk + n) % n;
            const inIdx = i;
            sum = sum - code[outIdx] + code[inIdx];
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $code
     * @param Integer $k
     * @return Integer[]
     */
    function decrypt($code, $k) {
        $n = count($code);
        $result = array_fill(0, $n, 0);
        if ($k == 0) {
            return $result;
        }

        $absK = abs($k);
        $sum = 0;

        if ($k > 0) {
            // initial sum of next k elements for index 0
            for ($i = 1; $i <= $k; $i++) {
                $sum += $code[$i % $n];
            }
            for ($i = 0; $i < $n; $i++) {
                $result[$i] = $sum;
                // slide window: remove element at i+1, add element at i+k+1
                $removeIdx = ($i + 1) % $n;
                $addIdx    = ($i + $k + 1) % $n;
                $sum = $sum - $code[$removeIdx] + $code[$addIdx];
            }
        } else { // k < 0
            // initial sum of previous |k| elements for index 0
            for ($i = $n - $absK; $i < $n; $i++) {
                $sum += $code[$i];
            }
            for ($i = 0; $i < $n; $i++) {
                $result[$i] = $sum;
                // slide window: remove element at i-|k|, add element at i
                $removeIdx = ($i - $absK + $n) % $n;
                $addIdx    = $i % $n;
                $sum = $sum - $code[$removeIdx] + $code[$addIdx];
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func decrypt(_ code: [Int], _ k: Int) -> [Int] {
        let n = code.count
        var result = Array(repeating: 0, count: n)
        if k == 0 { return result }
        
        if k > 0 {
            var sum = 0
            for i in 1...k {
                sum += code[i % n]
            }
            for i in 0..<n {
                result[i] = sum
                let outIdx = (i + 1) % n
                let inIdx = (i + 1 + k) % n
                sum = sum - code[outIdx] + code[inIdx]
            }
        } else {
            let kk = -k
            var sum = 0
            for i in 0..<kk {
                sum += code[(n - kk + i) % n]
            }
            for i in 0..<n {
                result[i] = sum
                let outIdx = (i - kk + n) % n
                let inIdx = i % n
                sum = sum - code[outIdx] + code[inIdx]
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun decrypt(code: IntArray, k: Int): IntArray {
        val n = code.size
        val result = IntArray(n)
        if (k == 0) return result
        val steps = kotlin.math.abs(k)
        for (i in 0 until n) {
            var sum = 0
            if (k > 0) {
                for (j in 1..steps) {
                    val idx = (i + j) % n
                    sum += code[idx]
                }
            } else { // k < 0
                for (j in 1..steps) {
                    var idx = i - j
                    if (idx < 0) idx += n
                    sum += code[idx]
                }
            }
            result[i] = sum
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> decrypt(List<int> code, int k) {
    int n = code.length;
    List<int> res = List.filled(n, 0);
    if (k == 0) return res;

    if (k > 0) {
      int sum = 0;
      for (int j = 1; j <= k; ++j) {
        sum += code[j % n];
      }
      for (int i = 0; i < n; ++i) {
        res[i] = sum;
        int outIdx = (i + 1) % n;
        int inIdx = (i + k + 1) % n;
        sum = sum - code[outIdx] + code[inIdx];
      }
    } else {
      int kk = -k;
      int sum = 0;
      for (int j = n - kk; j < n; ++j) {
        sum += code[j];
      }
      for (int i = 0; i < n; ++i) {
        res[i] = sum;
        int outIdx = (i - kk + n) % n;
        int inIdx = i % n;
        sum = sum - code[outIdx] + code[inIdx];
      }
    }

    return res;
  }
}
```

## Golang

```go
func decrypt(code []int, k int) []int {
    n := len(code)
    res := make([]int, n)
    if k == 0 {
        return res
    }
    if k > 0 {
        sum := 0
        for j := 1; j <= k; j++ {
            sum += code[j%n]
        }
        for i := 0; i < n; i++ {
            res[i] = sum
            outIdx := (i + 1) % n
            inIdx := (i + k + 1) % n
            sum = sum - code[outIdx] + code[inIdx]
        }
    } else {
        kk := -k
        sum := 0
        for j := n - kk; j < n; j++ {
            sum += code[j%n]
        }
        for i := 0; i < n; i++ {
            res[i] = sum
            outIdx := (i - kk + n) % n
            inIdx := i % n
            sum = sum - code[outIdx] + code[inIdx]
        }
    }
    return res
}
```

## Ruby

```ruby
def decrypt(code, k)
  n = code.length
  return Array.new(n, 0) if k == 0

  result = Array.new(n, 0)

  if k > 0
    sum = 0
    (1..k).each { |i| sum += code[i % n] }
    start = 1 % n
    end_idx = k % n

    n.times do |i|
      result[i] = sum
      sum -= code[start]
      end_idx = (end_idx + 1) % n
      sum += code[end_idx]
      start = (start + 1) % n
    end
  else
    kk = -k
    sum = 0
    ((n - kk)...n).each { |i| sum += code[i] }
    start = (n - kk) % n
    end_idx = (n - 1) % n

    n.times do |i|
      result[i] = sum
      sum -= code[start]
      sum += code[i % n]
      start = (start + 1) % n
      end_idx = (end_idx + 1) % n
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def decrypt(code: Array[Int], k: Int): Array[Int] = {
        val n = code.length
        if (k == 0) return Array.fill(n)(0)

        val res = new Array[Int](n)
        var sum = 0

        if (k > 0) {
            // initial window: next k elements for index 0 -> indices 1 .. k
            for (i <- 1 to k) {
                sum += code(i % n)
            }
            var start = 1 % n
            var end = k % n
            for (i <- 0 until n) {
                res(i) = sum
                // slide window
                sum -= code(start)
                val nextIdx = (end + 1) % n
                sum += code(nextIdx)
                start = (start + 1) % n
                end = (end + 1) % n
            }
        } else {
            val kk = -k
            // initial window: previous kk elements for index 0 -> indices n-kk .. n-1
            for (i <- n - kk until n) {
                sum += code(i % n)
            }
            var start = (n - kk) % n
            var end = (n - 1) % n
            for (i <- 0 until n) {
                res(i) = sum
                // slide window
                sum -= code(start)
                val nextIdx = (end + 1) % n
                sum += code(nextIdx)
                start = (start + 1) % n
                end = (end + 1) % n
            }
        }

        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn decrypt(code: Vec<i32>, k: i32) -> Vec<i32> {
        let n = code.len();
        if k == 0 {
            return vec![0; n];
        }
        let mut res = vec![0; n];
        if k > 0 {
            let kk = k as usize;
            let mut sum: i32 = 0;
            for idx in 1..=kk {
                sum += code[idx % n];
            }
            for i in 0..n {
                res[i] = sum;
                let out_idx = (i + 1) % n;
                let in_idx = (i + kk + 1) % n;
                sum = sum - code[out_idx] + code[in_idx];
            }
        } else {
            let kk = (-k) as usize;
            let mut sum: i32 = 0;
            for idx in n - kk..n {
                sum += code[idx];
            }
            for i in 0..n {
                res[i] = sum;
                let out_idx = (i + n - kk) % n;
                let in_idx = i % n;
                sum = sum - code[out_idx] + code[in_idx];
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (decrypt code k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((n (length code))
         (v (list->vector code))
         (step (if (> k 0) 1 -1))
         (m (abs k)))
    (cond
      [(zero? k) (make-list n 0)]
      [else
       (build-list n
         (lambda (i)
           (let loop ((cnt 1) (s 0))
             (if (> cnt m)
                 s
                 (let* ((idx (+ i (* step cnt)))
                        (mod-idx (modulo idx n))
                        (val (vector-ref v mod-idx)))
                   (loop (+ cnt 1) (+ s val))))))])))
```

## Erlang

```erlang
-spec decrypt(Code :: [integer()], K :: integer()) -> [integer()].
decrypt(Code, K) ->
    N = length(Code),
    case K of
        0 -> lists:duplicate(N, 0);
        _ when K > 0 ->
            [sum_next(Code, N, K, I) || I <- lists:seq(0, N - 1)];
        _ ->
            AbsK = -K,
            [sum_prev(Code, N, AbsK, I) || I <- lists:seq(0, N - 1)]
    end.

sum_next(Code, N, K, I) ->
    lists:foldl(
        fun(J, Acc) ->
            Index = (I + J) rem N,
            Acc + element_at(Code, Index)
        end,
        0,
        lists:seq(1, K)
    ).

sum_prev(Code, N, AbsK, I) ->
    lists:foldl(
        fun(J, Acc) ->
            Index = (I - J + N) rem N,
            Acc + element_at(Code, Index)
        end,
        0,
        lists:seq(1, AbsK)
    ).

element_at(Code, Index) -> % zero‑based index
    lists:nth(Index + 1, Code).
```

## Elixir

```elixir
defmodule Solution do
  @spec decrypt(code :: [integer], k :: integer) :: [integer]
  def decrypt(code, k) do
    n = length(code)

    cond do
      k == 0 ->
        List.duplicate(0, n)

      k > 0 ->
        Enum.map(0..n - 1, fn i ->
          Enum.reduce(1..k, 0, fn offset, acc ->
            idx = rem(i + offset, n)
            acc + Enum.at(code, idx)
          end)
        end)

      true -> # k < 0
        m = -k

        Enum.map(0..n - 1, fn i ->
          Enum.reduce(1..m, 0, fn offset, acc ->
            raw_idx = rem(i - offset, n)
            idx = if raw_idx < 0, do: raw_idx + n, else: raw_idx
            acc + Enum.at(code, idx)
          end)
        end)
    end
  end
end
```
