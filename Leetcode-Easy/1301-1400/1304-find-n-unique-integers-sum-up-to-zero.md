# 1304. Find N Unique Integers Sum up to Zero

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> sumZero(int n) {
        vector<int> ans;
        int half = n / 2;
        for (int i = 1; i <= half; ++i) {
            ans.push_back(i);
            ans.push_back(-i);
        }
        if (n % 2 == 1) ans.push_back(0);
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] sumZero(int n) {
        int[] result = new int[n];
        int idx = 0;
        if (n % 2 == 1) {
            result[idx++] = 0;
        }
        for (int i = 1; idx < n; i++) {
            result[idx++] = i;
            result[idx++] = -i;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        half = n // 2
        for i in range(1, half + 1):
            res.append(i)
            res.append(-i)
        if n % 2:
            res.append(0)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        if n % 2 == 1:
            res.append(0)
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumZero(int n, int* returnSize) {
    *returnSize = n;
    int* res = (int*)malloc(n * sizeof(int));
    int left = 0, right = n - 1;
    for (int i = 1; i <= n / 2; ++i) {
        res[left++] = i;
        res[right--] = -i;
    }
    if (n % 2 == 1) {
        res[n / 2] = 0;
    }
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] SumZero(int n) {
        int[] result = new int[n];
        int idx = 0;
        if (n % 2 == 1) {
            result[idx++] = 0;
        }
        for (int i = 1; idx < n; i++) {
            result[idx++] = i;
            result[idx++] = -i;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    const res = [];
    const half = Math.floor(n / 2);
    for (let i = 1; i <= half; i++) {
        res.push(i);
        res.push(-i);
    }
    if (n % 2 === 1) {
        res.push(0);
    }
    return res;
};
```

## Typescript

```typescript
function sumZero(n: number): number[] {
    const result: number[] = [];
    const half = Math.floor(n / 2);
    for (let i = 1; i <= half; i++) {
        result.push(i);
        result.push(-i);
    }
    if (n % 2 === 1) {
        result.push(0);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function sumZero($n) {
        $res = [];
        // If n is odd, include zero
        if ($n % 2 == 1) {
            $res[] = 0;
            $pairs = intdiv($n - 1, 2);
        } else {
            $pairs = intdiv($n, 2);
        }
        for ($i = 1; $i <= $pairs; $i++) {
            $res[] = $i;
            $res[] = -$i;
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func sumZero(_ n: Int) -> [Int] {
        var result = [Int]()
        var remaining = n
        if n % 2 == 1 {
            result.append(0)
            remaining -= 1
        }
        let half = remaining / 2
        if half > 0 {
            for i in 1...half {
                result.append(i)
                result.append(-i)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumZero(n: Int): IntArray {
        val result = IntArray(n)
        var idx = 0
        if (n % 2 == 1) {
            result[idx++] = 0
        }
        var i = 1
        while (idx < n) {
            result[idx++] = i
            result[idx++] = -i
            i++
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> sumZero(int n) {
    List<int> res = [];
    int half = n ~/ 2;
    for (int i = 1; i <= half; ++i) {
      res.add(i);
      res.add(-i);
    }
    if (n % 2 == 1) {
      res.add(0);
    }
    return res;
  }
}
```

## Golang

```go
func sumZero(n int) []int {
    res := make([]int, 0, n)
    for i := 1; i <= n/2; i++ {
        res = append(res, i, -i)
    }
    if n%2 == 1 {
        res = append(res, 0)
    }
    return res
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {Integer[]}
def sum_zero(n)
  result = []
  (1..n / 2).each do |i|
    result << i
    result << -i
  end
  result << 0 if n.odd?
  result
end
```

## Scala

```scala
object Solution {
    def sumZero(n: Int): Array[Int] = {
        val res = new Array[Int](n)
        var idx = 0
        for (i <- 1 to n / 2) {
            res(idx) = i
            res(idx + 1) = -i
            idx += 2
        }
        if (n % 2 == 1) {
            res(idx) = 0
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_zero(n: i32) -> Vec<i32> {
        let mut res = Vec::with_capacity(n as usize);
        for i in 1..=n / 2 {
            res.push(i);
            res.push(-i);
        }
        if n % 2 != 0 {
            res.push(0);
        }
        res
    }
}
```

## Racket

```racket
(define/contract (sum-zero n)
  (-> exact-integer? (listof exact-integer?))
  (let* ((half (quotient n 2))
         (pos (for/list ([i (in-range 1 (+ half 1))]) i))
         (neg (map - pos))
         (base (append neg pos)))
    (if (odd? n)
        (cons 0 base)
        base)))
```

## Erlang

```erlang
-module(solution).
-export([sum_zero/1]).

-spec sum_zero(N :: integer()) -> [integer()].
sum_zero(N) when N >= 0 ->
    case N rem 2 of
        0 ->
            Pos = lists:seq(1, N div 2),
            Neg = [-X || X <- Pos],
            Neg ++ Pos;
        _ ->
            M = N div 2,
            Pos = lists:seq(1, M),
            Neg = [-X || X <- Pos],
            [0 | (Neg ++ Pos)]
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_zero(n :: integer) :: [integer]
  def sum_zero(n) do
    half = div(n, 2)
    pos = Enum.to_list(1..half)
    neg = Enum.map(pos, & -&1)

    if rem(n, 2) == 1 do
      [0 | (pos ++ neg)]
    else
      pos ++ neg
    end
  end
end
```
