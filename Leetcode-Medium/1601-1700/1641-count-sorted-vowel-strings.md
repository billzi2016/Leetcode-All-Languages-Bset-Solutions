# 1641. Count Sorted Vowel Strings

## Cpp

```cpp
class Solution {
public:
    int countVowelStrings(int n) {
        std::vector<int> dp(5, 1); // strings of length 1 ending with each vowel
        for (int len = 2; len <= n; ++len) {
            for (int i = 1; i < 5; ++i) {
                dp[i] += dp[i - 1];
            }
        }
        int ans = 0;
        for (int v : dp) ans += v;
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countVowelStrings(int n) {
        long res = 1;
        for (int i = 1; i <= 4; i++) {
            res = res * (n + i) / i;
        }
        return (int) res;
    }
}
```

## Python

```python
class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Number of non‑decreasing strings of length n from 5 vowels = C(n+4, 4)
        res = 1
        for i in range(1, 5):  # i = 1..4
            res = res * (n + 5 - i) // i
        return res
```

## Python3

```python
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        for _ in range(n - 1):
            for i in range(1, 5):
                dp[i] += dp[i - 1]
        return sum(dp)
```

## C

```c
int countVowelStrings(int n) {
    long long res = 1;
    int N = n + 4; // compute C(N,4)
    for (int i = 1; i <= 4; ++i) {
        res = res * (N - 4 + i) / i;
    }
    return (int)res;
}
```

## Csharp

```csharp
public class Solution {
    public int CountVowelStrings(int n) {
        long result = 1;
        int N = n + 4; // total items for combination
        int k = 4;     // choose 4 positions
        for (int i = 1; i <= k; i++) {
            result = result * (N - k + i) / i;
        }
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countVowelStrings = function(n) {
    let res = 1;
    for (let i = 1; i <= 4; ++i) {
        res = res * (n + i) / i;
    }
    return Math.round(res);
};
```

## Typescript

```typescript
function countVowelStrings(n: number): number {
    let result = 1;
    for (let i = 1; i <= 4; i++) {
        result = result * (n + i) / i;
    }
    return Math.round(result);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countVowelStrings($n) {
        $result = 1;
        for ($i = 1; $i <= 4; $i++) {
            $result = intdiv($result * ($n + $i), $i);
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func countVowelStrings(_ n: Int) -> Int {
        var result: Int64 = 1
        for i in 1...4 {
            result = result * Int64(n + i) / Int64(i)
        }
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countVowelStrings(n: Int): Int {
        var res = 1L
        val N = n + 4
        for (i in 1..4) {
            res = res * (N - 4 + i) / i
        }
        return res.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int countVowelStrings(int n) {
    int result = 1;
    for (int i = 1; i <= 4; ++i) {
      result = result * (n + i) ~/ i;
    }
    return result;
  }
}
```

## Golang

```go
func countVowelStrings(n int) int {
    N := n + 4
    k := 4
    var res int64 = 1
    for i := 1; i <= k; i++ {
        res = res * int64(N-k+i) / int64(i)
    }
    return int(res)
}
```

## Ruby

```ruby
def count_vowel_strings(n)
  res = 1
  (1..4).each do |i|
    res = res * (n + 5 - i) / i
  end
  res
end
```

## Scala

```scala
object Solution {
    def countVowelStrings(n: Int): Int = {
        val N = n + 4
        var result: Long = 1L
        for (i <- 1 to 4) {
            result = result * (N - i + 1) / i
        }
        result.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_vowel_strings(n: i32) -> i32 {
        let n = n as i64;
        let mut res = 1i64;
        for i in 1..=4 {
            res = res * (n + i) / i;
        }
        res as i32
    }
}
```

## Racket

```racket
(define (choose n k)
  (let loop ([i 1] [res 1])
    (if (> i k)
        res
        (loop (+ i 1) (/ (* res (+ (- n k) i)) i)))))

(define/contract (count-vowel-strings n)
  (-> exact-integer? exact-integer?)
  (choose (+ n 4) 4))
```

## Erlang

```erlang
-module(solution).
-export([count_vowel_strings/1]).

-spec count_vowel_strings(N :: integer()) -> integer().
count_vowel_strings(N) ->
    comb(N + 4, 4).

comb(N, K) ->
    K1 = min(K, N - K),
    comb_iter(1, K1, N, 1).

comb_iter(I, K, _N, Acc) when I > K -> Acc;
comb_iter(I, K, N, Acc) ->
    NewAcc = (Acc * (N - K + I)) div I,
    comb_iter(I + 1, K, N, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_vowel_strings(integer) :: integer
  def count_vowel_strings(n) when is_integer(n) and n >= 0 do
    binom(n + 4, 4)
  end

  defp binom(n, k) do
    k = min(k, n - k)

    Enum.reduce(1..k, 1, fn i, acc ->
      div(acc * (n - k + i), i)
    end)
  end
end
```
