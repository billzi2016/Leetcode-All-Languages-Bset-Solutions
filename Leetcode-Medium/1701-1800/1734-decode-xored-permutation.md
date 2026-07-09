# 1734. Decode XORed Permutation

## Cpp

```cpp
class Solution {
public:
    vector<int> decode(vector<int>& encoded) {
        int n = encoded.size() + 1;
        int totalXor = 0;
        for (int i = 1; i <= n; ++i) totalXor ^= i;

        int oddXor = 0;
        for (int i = 1; i < encoded.size(); i += 2) {
            oddXor ^= encoded[i];
        }

        vector<int> perm(n);
        perm[0] = totalXor ^ oddXor;
        for (int i = 1; i < n; ++i) {
            perm[i] = perm[i - 1] ^ encoded[i - 1];
        }
        return perm;
    }
};
```

## Java

```java
class Solution {
    public int[] decode(int[] encoded) {
        int n = encoded.length + 1;
        int totalXor = 0;
        for (int i = 1; i <= n; i++) {
            totalXor ^= i;
        }
        int oddXor = 0;
        for (int i = 1; i < encoded.length; i += 2) {
            oddXor ^= encoded[i];
        }
        int[] perm = new int[n];
        perm[0] = totalXor ^ oddXor;
        for (int i = 1; i < n; i++) {
            perm[i] = perm[i - 1] ^ encoded[i - 1];
        }
        return perm;
    }
}
```

## Python

```python
class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        n = len(encoded) + 1
        total_xor = 0
        for i in range(1, n + 1):
            total_xor ^= i

        odd_xor = 0
        # XOR encoded elements at odd indices (1-based indexing -> even positions in zero-index)
        for i in range(1, len(encoded), 2):
            odd_xor ^= encoded[i]

        perm = [total_xor ^ odd_xor]
        for e in encoded:
            perm.append(perm[-1] ^ e)

        return perm
```

## Python3

```python
class Solution:
    def decode(self, encoded):
        n = len(encoded) + 1
        total = 0
        for i in range(1, n + 1):
            total ^= i
        odd_xor = 0
        for i in range(1, len(encoded), 2):
            odd_xor ^= encoded[i]
        perm = [total ^ odd_xor]
        for e in encoded:
            perm.append(perm[-1] ^ e)
        return perm
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decode(int* encoded, int encodedSize, int* returnSize) {
    int n = encodedSize + 1;
    int totalXor = 0;
    for (int i = 1; i <= n; ++i) {
        totalXor ^= i;
    }
    
    int oddXor = 0;
    for (int i = 1; i < encodedSize; i += 2) {
        oddXor ^= encoded[i];
    }
    
    int *perm = (int *)malloc(n * sizeof(int));
    perm[0] = totalXor ^ oddXor;
    
    for (int i = 1; i < n; ++i) {
        perm[i] = perm[i - 1] ^ encoded[i - 1];
    }
    
    *returnSize = n;
    return perm;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] Decode(int[] encoded)
    {
        int n = encoded.Length + 1;
        int totalXor = 0;
        for (int i = 1; i <= n; i++)
            totalXor ^= i;

        int oddXor = 0;
        for (int i = 1; i < encoded.Length; i += 2)
            oddXor ^= encoded[i];

        int[] perm = new int[n];
        perm[0] = totalXor ^ oddXor;

        for (int i = 1; i < n; i++)
            perm[i] = perm[i - 1] ^ encoded[i - 1];

        return perm;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} encoded
 * @return {number[]}
 */
var decode = function(encoded) {
    const n = encoded.length + 1;
    let totalXor = 0;
    for (let i = 1; i <= n; i++) {
        totalXor ^= i;
    }
    let oddXor = 0;
    for (let i = 1; i < encoded.length; i += 2) {
        oddXor ^= encoded[i];
    }
    const perm = new Array(n);
    perm[0] = totalXor ^ oddXor;
    for (let i = 1; i < n; i++) {
        perm[i] = perm[i - 1] ^ encoded[i - 1];
    }
    return perm;
};
```

## Typescript

```typescript
function decode(encoded: number[]): number[] {
    const n = encoded.length + 1;
    let totalXor = 0;
    for (let i = 1; i <= n; i++) {
        totalXor ^= i;
    }
    let oddEncodedXor = 0;
    for (let i = 1; i < encoded.length; i += 2) {
        oddEncodedXor ^= encoded[i];
    }
    const perm: number[] = new Array(n);
    perm[0] = totalXor ^ oddEncodedXor;
    for (let i = 1; i < n; i++) {
        perm[i] = perm[i - 1] ^ encoded[i - 1];
    }
    return perm;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $encoded
     * @return Integer[]
     */
    function decode($encoded) {
        $n = count($encoded) + 1;
        // XOR of all numbers from 1 to n
        $totalXor = 0;
        for ($i = 1; $i <= $n; $i++) {
            $totalXor ^= $i;
        }
        // XOR of encoded elements at odd indices (1,3,5,...)
        $xorOddEncoded = 0;
        for ($i = 1; $i < $n - 1; $i += 2) {
            $xorOddEncoded ^= $encoded[$i];
        }
        $perm = array_fill(0, $n, 0);
        $perm[0] = $totalXor ^ $xorOddEncoded;
        for ($i = 1; $i < $n; $i++) {
            $perm[$i] = $perm[$i - 1] ^ $encoded[$i - 1];
        }
        return $perm;
    }
}
```

## Swift

```swift
class Solution {
    func decode(_ encoded: [Int]) -> [Int] {
        let n = encoded.count + 1
        var totalXor = 0
        for i in 1...n {
            totalXor ^= i
        }
        var xorOdd = 0
        var idx = 1
        while idx < encoded.count {
            xorOdd ^= encoded[idx]
            idx += 2
        }
        var perm = Array(repeating: 0, count: n)
        perm[0] = totalXor ^ xorOdd
        for i in 1..<n {
            perm[i] = perm[i - 1] ^ encoded[i - 1]
        }
        return perm
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun decode(encoded: IntArray): IntArray {
        val n = encoded.size + 1
        var totalXor = 0
        for (i in 1..n) {
            totalXor = totalXor xor i
        }
        var oddEncodedXor = 0
        var idx = 1
        while (idx < encoded.size) {
            oddEncodedXor = oddEncodedXor xor encoded[idx]
            idx += 2
        }
        val perm = IntArray(n)
        perm[0] = totalXor xor oddEncodedXor
        for (i in 1 until n) {
            perm[i] = perm[i - 1] xor encoded[i - 1]
        }
        return perm
    }
}
```

## Dart

```dart
class Solution {
  List<int> decode(List<int> encoded) {
    int n = encoded.length + 1;
    int totalXor = 0;
    for (int i = 1; i <= n; ++i) {
      totalXor ^= i;
    }

    int oddEncodedXor = 0;
    for (int i = 1; i < encoded.length; i += 2) {
      oddEncodedXor ^= encoded[i];
    }

    List<int> perm = List.filled(n, 0);
    perm[0] = totalXor ^ oddEncodedXor;

    for (int i = 1; i < n; ++i) {
      perm[i] = perm[i - 1] ^ encoded[i - 1];
    }

    return perm;
  }
}
```

## Golang

```go
func decode(encoded []int) []int {
	n := len(encoded) + 1
	// XOR of all numbers from 1 to n
	totalXor := 0
	for i := 1; i <= n; i++ {
		totalXor ^= i
	}
	// XOR of encoded elements at odd indices (1,3,5,...)
	oddXor := 0
	for i := 1; i < len(encoded); i += 2 {
		oddXor ^= encoded[i]
	}
	perm := make([]int, n)
	perm[0] = totalXor ^ oddXor
	for i := 1; i < n; i++ {
		perm[i] = perm[i-1] ^ encoded[i-1]
	}
	return perm
}
```

## Ruby

```ruby
def decode(encoded)
  n = encoded.length + 1
  total = 0
  (1..n).each { |i| total ^= i }
  odd_xor = 0
  i = 1
  while i < encoded.length
    odd_xor ^= encoded[i]
    i += 2
  end
  perm = Array.new(n)
  perm[0] = total ^ odd_xor
  (1...n).each do |idx|
    perm[idx] = perm[idx - 1] ^ encoded[idx - 1]
  end
  perm
end
```

## Scala

```scala
object Solution {
    def decode(encoded: Array[Int]): Array[Int] = {
        val n = encoded.length + 1
        var totalXor = 0
        for (i <- 1 to n) totalXor ^= i

        var oddXor = 0
        var idx = 1
        while (idx < encoded.length) {
            oddXor ^= encoded(idx)
            idx += 2
        }

        val perm = new Array[Int](n)
        perm(0) = totalXor ^ oddXor

        for (i <- 1 until n) {
            perm(i) = perm(i - 1) ^ encoded(i - 1)
        }
        perm
    }
}
```

## Rust

```rust
impl Solution {
    pub fn decode(encoded: Vec<i32>) -> Vec<i32> {
        let n = encoded.len() + 1;
        // XOR of all numbers from 1 to n
        let mut total = 0i32;
        for i in 1..=n as i32 {
            total ^= i;
        }
        // XOR of encoded elements at odd indices (0‑based)
        let mut odd_xor = 0i32;
        let mut idx = 1usize;
        while idx < encoded.len() {
            odd_xor ^= encoded[idx];
            idx += 2;
        }
        let first = total ^ odd_xor;
        let mut perm = Vec::with_capacity(n);
        perm.push(first);
        for &e in &encoded {
            let next = *perm.last().unwrap() ^ e;
            perm.push(next);
        }
        perm
    }
}
```

## Racket

```racket
(define/contract (decode encoded)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((n (+ 1 (length encoded)))
         ;; XOR of all numbers from 1 to n
         (totalXor
          (let loop ((i 1) (acc 0))
            (if (> i n)
                acc
                (loop (+ i 1) (bitwise-xor acc i)))))
         ;; XOR of encoded elements at odd indices (0‑based)
         (xorOddEncoded
          (let loop ((lst encoded) (idx 0) (acc 0))
            (if (null? lst)
                acc
                (loop (cdr lst)
                      (+ idx 1)
                      (if (= (modulo idx 2) 1)
                          (bitwise-xor acc (car lst))
                          acc)))))
         ;; First element of the permutation
         (first (bitwise-xor totalXor xorOddEncoded)))
    ;; Reconstruct the whole permutation
    (let loop ((lst encoded) (prev first) (acc (list first)))
      (if (null? lst)
          (reverse acc)
          (let ((next (bitwise-xor prev (car lst))))
            (loop (cdr lst) next (cons next acc)))))))
```

## Erlang

```erlang
-spec decode(Encoded :: [integer()]) -> [integer()].
decode(Encoded) ->
    N = length(Encoded) + 1,
    TotalXor = total_xor(N),
    XorOdd = xor_odd(Encoded, 0, 0),
    First = TotalXor bxor XorOdd,
    build_perm_helper(First, Encoded, [First]).

total_xor(N) ->
    lists:foldl(fun(I, Acc) -> Acc bxor I end, 0, lists:seq(1, N)).

xor_odd([], _Idx, Acc) -> Acc;
xor_odd([H|T], Idx, Acc) ->
    NewAcc = case (Idx rem 2) of
        1 -> Acc bxor H;
        _ -> Acc
    end,
    xor_odd(T, Idx + 1, NewAcc).

build_perm_helper(_Prev, [], Rev) ->
    lists:reverse(Rev);
build_perm_helper(Prev, [E|Es], Rev) ->
    Next = Prev bxor E,
    build_perm_helper(Next, Es, [Next | Rev]).
```

## Elixir

```elixir
defmodule Solution do
  @spec decode(encoded :: [integer]) :: [integer]
  def decode(encoded) do
    n = length(encoded) + 1

    all_xor =
      Enum.reduce(1..n, 0, fn x, acc -> Bitwise.bxor(acc, x) end)

    xor_odd =
      encoded
      |> Enum.with_index()
      |> Enum.reduce(0, fn {val, i}, acc ->
        if rem(i, 2) == 1 do
          Bitwise.bxor(acc, val)
        else
          acc
        end
      end)

    first = Bitwise.bxor(all_xor, xor_odd)

    len = length(encoded)
    build_perm(encoded, len, 0, first, [first])
  end

  defp build_perm(_encoded, len, idx, _current, acc) when idx == len do
    Enum.reverse(acc)
  end

  defp build_perm(encoded, len, idx, current, acc) do
    next = Bitwise.bxor(current, Enum.at(encoded, idx))
    build_perm(encoded, len, idx + 1, next, [next | acc])
  end
end
```
