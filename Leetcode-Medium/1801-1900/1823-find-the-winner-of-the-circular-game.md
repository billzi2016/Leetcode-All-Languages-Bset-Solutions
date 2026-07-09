# 1823. Find the Winner of the Circular Game

## Cpp

```cpp
class Solution {
public:
    int findTheWinner(int n, int k) {
        int ans = 0; // zero-based index for n = 1
        for (int i = 2; i <= n; ++i) {
            ans = (ans + k) % i;
        }
        return ans + 1; // convert to one-based indexing
    }
};
```

## Java

```java
class Solution {
    public int findTheWinner(int n, int k) {
        int winner = 0; // zero-based index for n = 1
        for (int i = 2; i <= n; i++) {
            winner = (winner + k) % i;
        }
        return winner + 1; // convert to one-based indexing
    }
}
```

## Python

```python
class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + k) % i
        return ans + 1
```

## Python3

```python
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + k) % i
        return ans + 1
```

## C

```c
int findTheWinner(int n, int k) {
    int ans = 0;
    for (int i = 2; i <= n; ++i) {
        ans = (ans + k) % i;
    }
    return ans + 1;
}
```

## Csharp

```csharp
public class Solution {
    public int FindTheWinner(int n, int k) {
        int winner = 0; // zero-based index for n = 1
        for (int i = 2; i <= n; i++) {
            winner = (winner + k) % i;
        }
        return winner + 1; // convert to one-based indexing
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findTheWinner = function(n, k) {
    let winner = 0; // zero-based index for n = 1
    for (let i = 2; i <= n; i++) {
        winner = (winner + k) % i;
    }
    return winner + 1; // convert to one-based indexing
};
```

## Typescript

```typescript
function findTheWinner(n: number, k: number): number {
    let ans = 0;
    for (let i = 2; i <= n; i++) {
        ans = (ans + k) % i;
    }
    return ans + 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function findTheWinner($n, $k) {
        $ans = 0;
        for ($i = 2; $i <= $n; $i++) {
            $ans = ($ans + $k) % $i;
        }
        return $ans + 1;
    }
}
```

## Swift

```swift
class Solution {
    func findTheWinner(_ n: Int, _ k: Int) -> Int {
        var ans = 0
        if n == 0 { return 0 }
        for i in 2...n {
            ans = (ans + k) % i
        }
        return ans + 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findTheWinner(n: Int, k: Int): Int {
        var ans = 0
        for (i in 2..n) {
            ans = (ans + k) % i
        }
        return ans + 1
    }
}
```

## Dart

```dart
class Solution {
  int findTheWinner(int n, int k) {
    int ans = 0;
    for (int i = 2; i <= n; i++) {
      ans = (ans + k) % i;
    }
    return ans + 1;
  }
}
```

## Golang

```go
func findTheWinner(n int, k int) int {
    ans := 0
    for i := 2; i <= n; i++ {
        ans = (ans + k) % i
    }
    return ans + 1
}
```

## Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def find_the_winner(n, k)
  ans = 0
  (2..n).each do |i|
    ans = (ans + k) % i
  end
  ans + 1
end
```

## Scala

```scala
object Solution {
    def findTheWinner(n: Int, k: Int): Int = {
        var ans = 0
        for (i <- 2 to n) {
            ans = (ans + k) % i
        }
        ans + 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_the_winner(n: i32, k: i32) -> i32 {
        let mut ans = 0usize;
        let k_usize = k as usize;
        for i in 2..=n as usize {
            ans = (ans + k_usize) % i;
        }
        (ans + 1) as i32
    }
}
```

## Racket

```racket
(define/contract (find-the-winner n k)
  (-> exact-integer? exact-integer? exact-integer?)
  (let loop ((i 2) (ans 0))
    (if (> i n)
        (+ ans 1)
        (loop (add1 i) (modulo (+ ans k) i)))))
```

## Erlang

```erlang
-module(solution).
-export([find_the_winner/2]).
-spec find_the_winner(N :: integer(), K :: integer()) -> integer().
find_the_winner(N, K) ->
    find_the_winner(2, N, K, 0).

find_the_winner(I, N, _K, Ans) when I > N ->
    Ans + 1;
find_the_winner(I, N, K, Ans) ->
    NewAns = (Ans + K) rem I,
    find_the_winner(I + 1, N, K, NewAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_the_winner(n :: integer, k :: integer) :: integer
  def find_the_winner(n, k) do
    ans = Enum.reduce(2..n, 0, fn i, acc -> rem(acc + k, i) end)
    ans + 1
  end
end
```
