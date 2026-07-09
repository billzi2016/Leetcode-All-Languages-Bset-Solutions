# 0386. Lexicographical Numbers

## Cpp

```cpp
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> res;
        res.reserve(n);
        int cur = 1;
        for (int i = 0; i < n; ++i) {
            res.push_back(cur);
            if (cur * 10 <= n) {
                cur *= 10;
            } else {
                while (cur % 10 == 9 || cur + 1 > n) {
                    cur /= 10;
                }
                ++cur;
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<Integer> lexicalOrder(int n) {
        java.util.ArrayList<Integer> result = new java.util.ArrayList<>(n);
        int current = 1;
        for (int i = 0; i < n; i++) {
            result.add(current);
            if (current * 10 <= n) {
                current *= 10;
            } else {
                while (current % 10 == 9 || current + 1 > n) {
                    current /= 10;
                }
                current++;
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        cur = 1
        for _ in range(n):
            result.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                while cur % 10 == 9 or cur + 1 > n:
                    cur //= 10
                cur += 1
        return result
```

## Python3

```python
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        cur = 1
        for _ in range(n):
            result.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                while cur % 10 == 9 or cur + 1 > n:
                    cur //= 10
                cur += 1
        return result
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* lexicalOrder(int n, int* returnSize) {
    int *res = (int*)malloc(sizeof(int) * n);
    int cur = 1;
    for (int i = 0; i < n; ++i) {
        res[i] = cur;
        if (cur * 10 <= n) {
            cur *= 10;
        } else {
            while (cur % 10 == 9 || cur + 1 > n) {
                cur /= 10;
            }
            cur += 1;
        }
    }
    *returnSize = n;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<int> LexicalOrder(int n)
    {
        var result = new List<int>(n);
        int current = 1;
        for (int i = 0; i < n; i++)
        {
            result.Add(current);
            if (current * 10 <= n)
            {
                current *= 10;
            }
            else
            {
                while (current % 10 == 9 || current + 1 > n)
                {
                    current /= 10;
                }
                current++;
            }
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
var lexicalOrder = function(n) {
    const result = new Array(n);
    let cur = 1;
    for (let i = 0; i < n; i++) {
        result[i] = cur;
        if (cur * 10 <= n) {
            cur *= 10;
        } else {
            while (cur % 10 === 9 || cur + 1 > n) {
                cur = Math.floor(cur / 10);
            }
            cur++;
        }
    }
    return result;
};
```

## Typescript

```typescript
function lexicalOrder(n: number): number[] {
    const result: number[] = [];
    let current = 1;
    for (let i = 0; i < n; i++) {
        result.push(current);
        if (current * 10 <= n) {
            current *= 10;
        } else {
            while (current % 10 === 9 || current + 1 > n) {
                current = Math.floor(current / 10);
            }
            current += 1;
        }
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
    function lexicalOrder($n) {
        $result = [];
        $curr = 1;
        for ($i = 0; $i < $n; $i++) {
            $result[] = $curr;
            if ($curr * 10 <= $n) {
                $curr *= 10;
            } else {
                while ($curr % 10 == 9 || $curr + 1 > $n) {
                    $curr = intdiv($curr, 10);
                }
                $curr++;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func lexicalOrder(_ n: Int) -> [Int] {
        var result = [Int]()
        var current = 1
        for _ in 0..<n {
            result.append(current)
            if current * 10 <= n {
                current *= 10
            } else {
                while current % 10 == 9 || current + 1 > n {
                    current /= 10
                }
                current += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lexicalOrder(n: Int): List<Int> {
        val result = ArrayList<Int>(n)
        var cur = 1
        repeat(n) {
            result.add(cur)
            if (cur * 10 <= n) {
                cur *= 10
            } else {
                while (cur % 10 == 9 || cur + 1 > n) {
                    cur /= 10
                }
                cur += 1
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> lexicalOrder(int n) {
    List<int> result = [];
    int cur = 1;
    for (int i = 0; i < n; i++) {
      result.add(cur);
      if (cur * 10 <= n) {
        cur *= 10;
      } else {
        while (cur % 10 == 9 || cur + 1 > n) {
          cur ~/= 10;
        }
        cur += 1;
      }
    }
    return result;
  }
}
```

## Golang

```go
func lexicalOrder(n int) []int {
    res := make([]int, 0, n)
    cur := 1
    for i := 0; i < n; i++ {
        res = append(res, cur)
        if cur*10 <= n {
            cur *= 10
        } else {
            for cur%10 == 9 || cur+1 > n {
                cur /= 10
            }
            cur++
        }
    }
    return res
}
```

## Ruby

```ruby
def lexical_order(n)
  result = []
  cur = 1
  while result.size < n
    result << cur
    if cur * 10 <= n
      cur *= 10
    else
      while (cur % 10 == 9) || (cur + 1 > n)
        cur /= 10
      end
      cur += 1
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def lexicalOrder(n: Int): List[Int] = {
        val result = scala.collection.mutable.ListBuffer[Int]()
        var cur = 1
        for (_ <- 0 until n) {
            result += cur
            if (cur * 10 <= n) {
                cur *= 10
            } else {
                while (cur % 10 == 9 || cur + 1 > n) {
                    cur /= 10
                }
                cur += 1
            }
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn lexical_order(n: i32) -> Vec<i32> {
        let mut result = Vec::with_capacity(n as usize);
        let mut cur = 1;
        for _ in 0..n {
            result.push(cur);
            if cur * 10 <= n {
                cur *= 10;
            } else {
                while cur % 10 == 9 || cur + 1 > n {
                    cur /= 10;
                }
                cur += 1;
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (lexical-order n)
  (-> exact-integer? (listof exact-integer?))
  (define (next-number cur limit)
    (if (<= (* cur 10) limit)
        (* cur 10)
        (let loop ((c cur))
          (if (or (= (remainder c 10) 9) (> (+ c 1) limit))
              (loop (quotient c 10))
              (+ c 1)))))
  (let loop ((i 0) (cur 1) (acc '()))
    (if (= i n)
        (reverse acc)
        (loop (+ i 1) (next-number cur n) (cons cur acc)))))
```

## Erlang

```erlang
-spec lexical_order(N :: integer()) -> [integer()].
lexical_order(N) when N >= 1 ->
    lexical_order(N, 1, 0, []).

lexical_order(_N, _Curr, Count, Acc) when Count =:= length(Acc) + Count ->
    lists:reverse(Acc);
lexical_order(N, Curr, Count, Acc) when Count =:= N ->
    lists:reverse(Acc);
lexical_order(N, Curr, Count, Acc) ->
    NewAcc = [Curr | Acc],
    Next = next(Curr, N),
    lexical_order(N, Next, Count + 1, NewAcc).

next(Cur, N) ->
    case Cur * 10 =< N of
        true -> Cur * 10;
        false ->
            Inc = Cur + 1,
            if Inc =< N, Inc rem 10 =/= 0 ->
                    Inc;
               true ->
                    backtrack(Cur, N)
            end
    end.

backtrack(Cur, N) ->
    C1 = Cur div 10,
    case (C1 rem 10 == 9) orelse (C1 + 1 > N) of
        true -> backtrack(C1, N);
        false -> C1 + 1
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec lexical_order(n :: integer) :: [integer]
  def lexical_order(n) when n >= 1 do
    generate(1, n, [], 0)
  end

  defp generate(_cur, limit, acc, cnt) when cnt == limit do
    Enum.reverse(acc)
  end

  defp generate(cur, limit, acc, cnt) do
    new_acc = [cur | acc]

    next_cur =
      if cur * 10 <= limit do
        cur * 10
      else
        base = move_up(cur, limit)
        base + 1
      end

    generate(next_cur, limit, new_acc, cnt + 1)
  end

  defp move_up(cur, limit) do
    if rem(cur, 10) == 9 or cur + 1 > limit do
      move_up(div(cur, 10), limit)
    else
      cur
    end
  end
end
```
