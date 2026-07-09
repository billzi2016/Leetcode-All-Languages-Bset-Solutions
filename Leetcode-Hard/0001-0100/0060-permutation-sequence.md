# 0060. Permutation Sequence

## Cpp

```cpp
class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> numbers;
        vector<int> fact(n + 1, 1);
        for (int i = 1; i <= n; ++i) {
            numbers.push_back(i);
            fact[i] = fact[i - 1] * i;
        }
        --k; // convert to zero-based index
        string result;
        for (int i = n; i >= 1; --i) {
            int idx = k / fact[i - 1];
            k %= fact[i - 1];
            result.push_back('0' + numbers[idx]);
            numbers.erase(numbers.begin() + idx);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public String getPermutation(int n, int k) {
        int[] fact = new int[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = fact[i - 1] * i;
        }
        List<Integer> numbers = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            numbers.add(i);
        }
        k--; // convert to zero-based index
        StringBuilder sb = new StringBuilder();
        for (int i = n; i >= 1; i--) {
            int idx = k / fact[i - 1];
            sb.append(numbers.get(idx));
            numbers.remove(idx);
            k %= fact[i - 1];
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Precompute factorials
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i

        # Convert k to zero-based index
        k -= 1

        numbers = list(range(1, n + 1))
        result = []

        for i in range(n, 0, -1):
            idx = k // fact[i - 1]
            result.append(str(numbers.pop(idx)))
            k %= fact[i - 1]

        return ''.join(result)
```

## Python3

```python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Precompute factorials
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i

        # Adjust k to be zero-indexed
        k -= 1

        numbers = [str(i) for i in range(1, n + 1)]
        result = []

        for i in range(n, 0, -1):
            idx, k = divmod(k, fact[i - 1])
            result.append(numbers.pop(idx))

        return ''.join(result)
```

## C

```c
#include <stdlib.h>

char* getPermutation(int n, int k) {
    int factorial[10];
    factorial[0] = 1;
    for (int i = 1; i <= n; ++i) {
        factorial[i] = factorial[i - 1] * i;
    }

    int numbers[9];
    for (int i = 0; i < n; ++i) {
        numbers[i] = i + 1;
    }

    char* res = (char*)malloc(n + 1);
    if (!res) return NULL;
    res[n] = '\0';

    k--; // convert to zero-based index
    int pos = 0;
    for (int i = n; i >= 1; --i) {
        int idx = k / factorial[i - 1];
        k %= factorial[i - 1];

        res[pos++] = '0' + numbers[idx];

        // remove used number
        for (int j = idx; j < i - 1; ++j) {
            numbers[j] = numbers[j + 1];
        }
    }

    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string GetPermutation(int n, int k)
    {
        var numbers = new List<int>();
        for (int i = 1; i <= n; i++) numbers.Add(i);

        var factorial = new int[n + 1];
        factorial[0] = 1;
        for (int i = 1; i <= n; i++) factorial[i] = factorial[i - 1] * i;

        k--; // convert to zero-based index
        var sb = new System.Text.StringBuilder();

        for (int i = n; i >= 1; i--)
        {
            int idx = k / factorial[i - 1];
            sb.Append(numbers[idx]);
            numbers.RemoveAt(idx);
            k %= factorial[i - 1];
        }

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getPermutation = function(n, k) {
    // Precompute factorials up to n
    const fact = new Array(n + 1);
    fact[0] = 1;
    for (let i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * i;
    }
    
    // Adjust k to be zero-indexed
    let remaining = k - 1;
    
    // Initialize list of numbers to pick from
    const nums = [];
    for (let i = 1; i <= n; i++) {
        nums.push(i);
    }
    
    let result = '';
    for (let i = n; i >= 1; i--) {
        const idx = Math.floor(remaining / fact[i - 1]);
        result += nums[idx];
        nums.splice(idx, 1);
        remaining %= fact[i - 1];
    }
    
    return result;
};
```

## Typescript

```typescript
function getPermutation(n: number, k: number): string {
    const numbers: number[] = [];
    for (let i = 1; i <= n; i++) numbers.push(i);
    
    const fact: number[] = new Array(n + 1).fill(1);
    for (let i = 2; i <= n; i++) fact[i] = fact[i - 1] * i;
    
    k--; // convert to zero-based index
    let result = '';
    
    for (let i = n; i >= 1; i--) {
        const idx = Math.floor(k / fact[i - 1]);
        result += numbers[idx];
        numbers.splice(idx, 1);
        k %= fact[i - 1];
    }
    
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return String
     */
    function getPermutation($n, $k) {
        // Initialize list of numbers to get indices from
        $numbers = range(1, $n);
        
        // Convert k to zero-based index
        $k -= 1;
        
        // Pre-compute factorials up to n
        $factorial = array_fill(0, $n + 1, 1);
        for ($i = 1; $i <= $n; $i++) {
            $factorial[$i] = $factorial[$i - 1] * $i;
        }
        
        $result = '';
        // Build permutation
        for ($i = $n; $i > 0; $i--) {
            $idx = intdiv($k, $factorial[$i - 1]);
            $result .= $numbers[$idx];
            array_splice($numbers, $idx, 1);
            $k %= $factorial[$i - 1];
        }
        
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func getPermutation(_ n: Int, _ k: Int) -> String {
        var numbers = [Int]()
        for i in 1...n { numbers.append(i) }
        
        var factorial = [Int](repeating: 1, count: n + 1)
        if n > 0 {
            for i in 1...n {
                factorial[i] = factorial[i - 1] * i
            }
        }
        
        var kVar = k - 1
        var result = ""
        
        for i in stride(from: n, through: 1, by: -1) {
            let f = factorial[i - 1]
            let index = kVar / f
            result += String(numbers[index])
            numbers.remove(at: index)
            kVar %= f
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getPermutation(n: Int, k: Int): String {
        val fact = IntArray(n + 1)
        fact[0] = 1
        for (i in 1..n) fact[i] = fact[i - 1] * i

        val numbers = mutableListOf<Int>()
        for (i in 1..n) numbers.add(i)

        var kVar = k - 1
        val sb = StringBuilder()
        for (i in n downTo 1) {
            val idx = kVar / fact[i - 1]
            sb.append(numbers[idx])
            numbers.removeAt(idx)
            kVar %= fact[i - 1]
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String getPermutation(int n, int k) {
    List<int> numbers = List.generate(n, (i) => i + 1);
    List<int> factorial = List.filled(n + 1, 1);
    for (int i = 2; i <= n; i++) {
      factorial[i] = factorial[i - 1] * i;
    }

    int kAdj = k - 1;
    StringBuffer sb = StringBuffer();

    for (int i = n; i >= 1; i--) {
      int fact = factorial[i - 1];
      int index = kAdj ~/ fact;
      sb.write(numbers[index]);
      numbers.removeAt(index);
      kAdj %= fact;
    }

    return sb.toString();
  }
}
```

## Golang

```go
func getPermutation(n int, k int) string {
    // Precompute factorials up to n
    fact := make([]int, n+1)
    fact[0] = 1
    for i := 1; i <= n; i++ {
        fact[i] = fact[i-1] * i
    }

    // Create a list of numbers to get indices from
    nums := make([]int, n)
    for i := 0; i < n; i++ {
        nums[i] = i + 1
    }

    // Convert k to zero-based index
    k--

    var sb []byte
    for i := n; i >= 1; i-- {
        idx := k / fact[i-1]
        sb = append(sb, byte('0'+nums[idx]))
        // remove used number
        nums = append(nums[:idx], nums[idx+1:]...)
        k %= fact[i-1]
    }
    return string(sb)
}
```

## Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {String}
def get_permutation(n, k)
  numbers = (1..n).to_a
  k -= 1
  fact = Array.new(n + 1, 1)
  (1..n).each { |i| fact[i] = fact[i - 1] * i }
  result = +''
  n.downto(1) do |i|
    idx = k / fact[i - 1]
    result << numbers[idx].to_s
    numbers.delete_at(idx)
    k %= fact[i - 1]
  end
  result
end
```

## Scala

```scala
object Solution {
    def getPermutation(n: Int, k: Int): String = {
        val factorial = new Array[Int](n + 1)
        factorial(0) = 1
        for (i <- 1 to n) factorial(i) = factorial(i - 1) * i

        import scala.collection.mutable.ArrayBuffer
        val numbers = ArrayBuffer[Int]()
        for (i <- 1 to n) numbers += i

        var kk = k - 1 // zero‑based index
        val sb = new StringBuilder

        for (i <- n to 1 by -1) {
            val f = factorial(i - 1)
            val idx = kk / f
            sb.append(numbers(idx))
            numbers.remove(idx)
            kk %= f
        }

        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_permutation(n: i32, k: i32) -> String {
        let n = n as usize;
        let mut k = (k - 1) as usize; // zero‑based index

        // Initialize the list of available numbers as characters.
        let mut numbers: Vec<char> = (1..=n)
            .map(|x| std::char::from_digit(x as u32, 10).unwrap())
            .collect();

        // Precompute factorials up to n.
        let mut fact = vec![1usize; n + 1];
        for i in 1..=n {
            fact[i] = fact[i - 1] * i;
        }

        let mut result = String::new();
        // Build the permutation using the factorial number system.
        for i in (1..=n).rev() {
            let f = fact[i - 1];
            let idx = k / f;
            result.push(numbers.remove(idx));
            k %= f;
        }

        result
    }
}
```

## Racket

```racket
#lang racket

(require racket/list)

(define/contract (get-permutation n k)
  (-> exact-integer? exact-integer? string?)
  (let* ((digits (build-list n (lambda (i) (number->string (+ i 1)))))
         (k0 (- k 1))
         (fact (make-vector (+ n 1) 1)))
    (for ([i (in-range 2 (+ n 1))])
      (vector-set! fact i (* (vector-ref fact (- i 1)) (- i 1))))
    (let loop ((remaining k0)
               (len n)
               (available digits)
               (acc '()))
      (if (= len 0)
          (apply string-append (reverse acc))
          (let* ((f (vector-ref fact (- len 1))) ; (len‑1)!
                 (index (quotient remaining f))
                 (new-remaining (remainder remaining f))
                 (chosen (list-ref available index))
                 (new-available (append (take available index)
                                        (drop available (+ index 1)))))
            (loop new-remaining (- len 1) new-available (cons chosen acc)))))))
```

## Erlang

```erlang
-spec get_permutation(N :: integer(), K :: integer()) -> unicode:unicode_binary().
get_permutation(N, K) ->
    Numbers = lists:seq(1, N),
    FactList = [factorial(I) || I <- lists:seq(N-1, 0, -1)],
    Digits = build_perm(Numbers, FactList, K - 1),
    list_to_binary([ $0 + D || D <- Digits]).

factorial(0) -> 1;
factorial(N) when N > 0 ->
    N * factorial(N-1).

build_perm([], [], _) -> [];
build_perm(Numbers, [Fact|RestFacts], K) ->
    Index = K div Fact,
    {Elem, RestNumbers} = pick(Index, Numbers),
    NewK = K rem Fact,
    [Elem | build_perm(RestNumbers, RestFacts, NewK)].

pick(0, [H|T]) -> {H, T};
pick(N, [H|T]) when N > 0 ->
    {Elem, Rest} = pick(N-1, T),
    {Elem, [H|Rest]}.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_permutation(n :: integer, k :: integer) :: String.t()
  def get_permutation(n, k) do
    nums = Enum.to_list(1..n)
    build(nums, k - 1, [])
  end

  defp build([], _k, acc), do: Enum.join(Enum.reverse(acc))

  defp build(nums, k, acc) do
    len = length(nums)
    f = fact(len - 1)
    idx = div(k, f)

    {head, [picked | tail]} = Enum.split_at(nums, idx)
    new_nums = head ++ tail

    build(new_nums, rem(k, f), [Integer.to_string(picked) | acc])
  end

  defp fact(0), do: 1
  defp fact(m) when m > 0 do
    Enum.reduce(1..m, 1, &*/2)
  end
end
```
