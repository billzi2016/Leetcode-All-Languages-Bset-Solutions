# 3577. Count the Number of Computer Unlocking Permutations

## Cpp

```cpp
class Solution {
public:
    int countPermutations(vector<int>& complexity) {
        const long long MOD = 1000000007LL;
        int n = complexity.size();
        for (int i = 1; i < n; ++i) {
            if (complexity[i] <= complexity[0]) return 0;
        }
        long long ans = 1;
        for (long long i = 2; i <= n - 1; ++i) {
            ans = ans * i % MOD;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int countPermutations(int[] complexity) {
        int n = complexity.length;
        int minVal = complexity[0];
        // verify uniqueness of minimum at index 0
        for (int i = 1; i < n; i++) {
            if (complexity[i] <= minVal) {
                return 0;
            }
        }
        long fact = 1L;
        for (int i = 2; i <= n - 1; i++) {
            fact = (fact * i) % MOD;
        }
        return (int) fact;
    }
}
```

## Python

```python
class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(complexity)
        root = complexity[0]
        for v in complexity[1:]:
            if v <= root:
                return 0
        res = 1
        for i in range(2, n):
            res = (res * i) % MOD
        return res
```

## Python3

```python
class Solution:
    def countPermutations(self, complexity):
        MOD = 10**9 + 7
        n = len(complexity)
        root = complexity[0]
        for v in complexity[1:]:
            if v <= root:
                return 0
        fact = 1
        for i in range(2, n):
            fact = (fact * i) % MOD
        return fact
```

## C

```c
#include <stddef.h>

int countPermutations(int* complexity, int complexitySize) {
    const long long MOD = 1000000007LL;
    if (complexitySize <= 1) return 0;
    
    int root = complexity[0];
    for (int i = 1; i < complexitySize; ++i) {
        if (complexity[i] <= root) {
            return 0;
        }
    }
    
    long long ans = 1;
    for (int i = 2; i <= complexitySize - 1; ++i) {
        ans = (ans * i) % MOD;
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int CountPermutations(int[] complexity) {
        const int MOD = 1000000007;
        int n = complexity.Length;
        for (int i = 1; i < n; i++) {
            if (complexity[i] <= complexity[0]) return 0;
        }
        long ans = 1;
        for (int i = 2; i <= n - 1; i++) {
            ans = (ans * i) % MOD;
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} complexity
 * @return {number}
 */
var countPermutations = function(complexity) {
    const n = complexity.length;
    const minVal = complexity[0];
    for (let i = 1; i < n; ++i) {
        if (complexity[i] <= minVal) return 0;
    }
    const MOD = 1000000007n;
    let fact = 1n;
    for (let i = 2; i <= n - 1; ++i) {
        fact = (fact * BigInt(i)) % MOD;
    }
    return Number(fact);
};
```

## Typescript

```typescript
function countPermutations(complexity: number[]): number {
    const MOD = 1000000007n;
    const n = complexity.length;
    const first = complexity[0];
    for (let i = 1; i < n; i++) {
        if (complexity[i] <= first) return 0;
    }
    let ans = 1n;
    for (let i = 2; i <= n - 1; i++) {
        ans = (ans * BigInt(i)) % MOD;
    }
    return Number(ans);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $complexity
     * @return Integer
     */
    function countPermutations($complexity) {
        $mod = 1000000007;
        $n = count($complexity);
        $first = $complexity[0];
        for ($i = 1; $i < $n; $i++) {
            if ($complexity[$i] <= $first) {
                return 0;
            }
        }
        $res = 1;
        for ($i = 2; $i <= $n - 1; $i++) {
            $res = ($res * $i) % $mod;
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func countPermutations(_ complexity: [Int]) -> Int {
        let MOD: Int64 = 1_000_000_007
        let n = complexity.count
        let first = complexity[0]
        for i in 1..<n {
            if complexity[i] <= first {
                return 0
            }
        }
        var result: Int64 = 1
        if n > 2 {
            for i in 2..<n { // multiply 2 * 3 * ... * (n-1)
                result = (result * Int64(i)) % MOD
            }
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val MOD = 1_000_000_007L
    fun countPermutations(complexity: IntArray): Int {
        val n = complexity.size
        var minVal = complexity[0]
        var cntMin = 1
        for (i in 1 until n) {
            val v = complexity[i]
            if (v < minVal) {
                minVal = v
                cntMin = 1
            } else if (v == minVal) {
                cntMin++
            }
        }
        // element at index 0 must be the unique minimum
        if (complexity[0] != minVal || cntMin > 1) return 0

        var fact = 1L
        for (i in 2..n - 1) {
            fact = (fact * i) % MOD
        }
        return fact.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int countPermutations(List<int> complexity) {
    int n = complexity.length;
    int first = complexity[0];
    for (int i = 1; i < n; ++i) {
      if (complexity[i] <= first) return 0;
    }
    int ans = 1;
    for (int i = 2; i <= n - 1; ++i) {
      ans = (ans * i) % _mod;
    }
    return ans;
  }
}
```

## Golang

```go
func countPermutations(complexity []int) int {
	const MOD = 1000000007
	n := len(complexity)
	if n == 0 {
		return 0
	}
	min0 := complexity[0]
	for i := 1; i < n; i++ {
		if complexity[i] <= min0 {
			return 0
		}
	}
	ans := 1
	for i := 2; i <= n-1; i++ {
		ans = int(int64(ans) * int64(i) % MOD)
	}
	return ans
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def count_permutations(complexity)
  n = complexity.length
  base = complexity[0]
  (1...n).each do |i|
    return 0 if complexity[i] <= base
  end
  res = 1
  i = 2
  while i <= n - 1
    res = (res * i) % MOD
    i += 1
  end
  res
end
```

## Scala

```scala
object Solution {
    private val MOD: Long = 1000000007L

    def countPermutations(complexity: Array[Int]): Int = {
        if (complexity.isEmpty) return 0
        val root = complexity(0)
        // If any other computer has complexity <= root, unlocking is impossible
        for (i <- 1 until complexity.length) {
            if (complexity(i) <= root) return 0
        }
        var ans: Long = 1L
        val nMinusOne = complexity.length - 1
        var i = 2
        while (i <= nMinusOne) {
            ans = (ans * i) % MOD
            i += 1
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_permutations(complexity: Vec<i32>) -> i32 {
        let n = complexity.len();
        if n == 0 {
            return 0;
        }
        // Find minimum value
        let mut min_val = complexity[0];
        for &v in &complexity[1..] {
            if v < min_val {
                min_val = v;
            }
        }
        // The root must be the unique minimum
        if min_val != complexity[0] {
            return 0;
        }
        let mut cnt_min = 0usize;
        for &v in &complexity {
            if v == min_val {
                cnt_min += 1;
            }
        }
        if cnt_min != 1 {
            return 0;
        }

        const MOD: i64 = 1_000_000_007;
        let mut ans: i64 = 1;
        // (n-1)! modulo MOD
        for i in 2..= (n as i64 - 1) {
            ans = ans * i % MOD;
        }
        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (count-permutations complexity)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length complexity))
         (first (car complexity)))
    (if (for/or ([c (in-list (cdr complexity))]) (<= c first))
        0
        (for/fold ([acc 1])
                  ([i (in-range 2 n)])
          (mod (* acc i) MOD)))))
```

## Erlang

```erlang
-module(solution).
-export([count_permutations/1]).

-define(MOD, 1000000007).

-spec count_permutations(Complexity :: [integer()]) -> integer().
count_permutations(Complexity) ->
    case is_valid(Complexity) of
        true ->
            N = length(Complexity) - 1,
            factorial(N);
        false ->
            0
    end.

is_valid([First|Rest]) ->
    lists:all(fun(X) -> X > First end, Rest).

factorial(N) when N >= 0 ->
    factorial(N, 1).

factorial(0, Acc) ->
    Acc;
factorial(N, Acc) ->
    NewAcc = (Acc * N) rem ?MOD,
    factorial(N - 1, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_permutations(complexity :: [integer]) :: integer
  def count_permutations(complexity) do
    mod = 1_000_000_007
    [root | rest] = complexity

    if Enum.any?(rest, fn x -> x <= root end) do
      0
    else
      n = length(complexity)

      Enum.reduce(1..(n - 1), 1, fn i, acc ->
        rem(acc * i, mod)
      end)
    end
  end
end
```
