# 1560. Most Visited Sector in  a Circular Track

## Cpp

```cpp
class Solution {
public:
    vector<int> mostVisited(int n, vector<int>& rounds) {
        int start = rounds.front();
        int end = rounds.back();
        vector<int> ans;
        if (start <= end) {
            for (int i = start; i <= end; ++i) ans.push_back(i);
        } else {
            for (int i = 1; i <= end; ++i) ans.push_back(i);
            for (int i = start; i <= n; ++i) ans.push_back(i);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public List<Integer> mostVisited(int n, int[] rounds) {
        int start = rounds[0];
        int end = rounds[rounds.length - 1];
        List<Integer> result = new ArrayList<>();
        if (start <= end) {
            for (int i = start; i <= end; i++) {
                result.add(i);
            }
        } else {
            for (int i = 1; i <= end; i++) {
                result.add(i);
            }
            for (int i = start; i <= n; i++) {
                result.add(i);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        start = rounds[0]
        end = rounds[-1]
        if start <= end:
            return list(range(start, end + 1))
        else:
            return list(range(1, end + 1)) + list(range(start, n + 1))
```

## Python3

```python
from typing import List

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start, end = rounds[0], rounds[-1]
        if start <= end:
            return list(range(start, end + 1))
        else:
            return list(range(1, end + 1)) + list(range(start, n + 1))
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* mostVisited(int n, int* rounds, int roundsSize, int* returnSize) {
    int start = rounds[0];
    int end = rounds[roundsSize - 1];
    int cnt;
    if (start <= end) {
        cnt = end - start + 1;
    } else {
        cnt = (n - start + 1) + end;
    }
    int *res = (int *)malloc(cnt * sizeof(int));
    int idx = 0;
    if (start <= end) {
        for (int i = start; i <= end; ++i) {
            res[idx++] = i;
        }
    } else {
        for (int i = start; i <= n; ++i) {
            res[idx++] = i;
        }
        for (int i = 1; i <= end; ++i) {
            res[idx++] = i;
        }
    }
    *returnSize = cnt;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> MostVisited(int n, int[] rounds) {
        int start = rounds[0];
        int end = rounds[rounds.Length - 1];
        var result = new List<int>();
        if (start <= end) {
            for (int i = start; i <= end; i++) {
                result.Add(i);
            }
        } else {
            for (int i = 1; i <= end; i++) {
                result.Add(i);
            }
            for (int i = start; i <= n; i++) {
                result.Add(i);
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
 * @param {number[]} rounds
 * @return {number[]}
 */
var mostVisited = function(n, rounds) {
    const start = rounds[0];
    const end = rounds[rounds.length - 1];
    const result = [];
    if (start <= end) {
        for (let i = start; i <= end; ++i) {
            result.push(i);
        }
    } else {
        for (let i = 1; i <= end; ++i) {
            result.push(i);
        }
        for (let i = start; i <= n; ++i) {
            result.push(i);
        }
    }
    return result;
};
```

## Typescript

```typescript
function mostVisited(n: number, rounds: number[]): number[] {
    const start = rounds[0];
    const end = rounds[rounds.length - 1];
    const result: number[] = [];
    if (start <= end) {
        for (let i = start; i <= end; i++) {
            result.push(i);
        }
    } else {
        for (let i = 1; i <= end; i++) {
            result.push(i);
        }
        for (let i = start; i <= n; i++) {
            result.push(i);
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
     * @param Integer[] $rounds
     * @return Integer[]
     */
    function mostVisited($n, $rounds) {
        $start = $rounds[0];
        $end = $rounds[count($rounds) - 1];

        if ($start <= $end) {
            return range($start, $end);
        } else {
            $result = array_merge(range(1, $end), range($start, $n));
            sort($result); // ensure ascending order
            return $result;
        }
    }
}
```

## Swift

```swift
class Solution {
    func mostVisited(_ n: Int, _ rounds: [Int]) -> [Int] {
        guard let start = rounds.first, let end = rounds.last else { return [] }
        var result = [Int]()
        if start <= end {
            for i in start...end {
                result.append(i)
            }
        } else {
            for i in start...n {
                result.append(i)
            }
            for i in 1...end {
                result.append(i)
            }
        }
        return result.sorted()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mostVisited(n: Int, rounds: IntArray): List<Int> {
        val start = rounds.first()
        val end = rounds.last()
        val res = mutableListOf<Int>()
        if (start <= end) {
            for (i in start..end) res.add(i)
        } else {
            for (i in start..n) res.add(i)
            for (i in 1..end) res.add(i)
        }
        res.sort()
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> mostVisited(int n, List<int> rounds) {
    int start = rounds.first;
    int end = rounds.last;
    List<int> result = [];
    if (start <= end) {
      for (int i = start; i <= end; ++i) {
        result.add(i);
      }
    } else {
      for (int i = 1; i <= end; ++i) {
        result.add(i);
      }
      for (int i = start; i <= n; ++i) {
        result.add(i);
      }
    }
    return result;
  }
}
```

## Golang

```go
func mostVisited(n int, rounds []int) []int {
    start := rounds[0]
    end := rounds[len(rounds)-1]
    res := make([]int, 0)
    if start <= end {
        for i := start; i <= end; i++ {
            res = append(res, i)
        }
    } else {
        for i := 1; i <= end; i++ {
            res = append(res, i)
        }
        for i := start; i <= n; i++ {
            res = append(res, i)
        }
    }
    return res
}
```

## Ruby

```ruby
def most_visited(n, rounds)
  start = rounds[0]
  finish = rounds[-1]
  if start <= finish
    (start..finish).to_a
  else
    (1..finish).to_a + (start..n).to_a
  end
end
```

## Scala

```scala
object Solution {
    def mostVisited(n: Int, rounds: Array[Int]): List[Int] = {
        val start = rounds.head
        val end = rounds.last
        if (start <= end) {
            (start to end).toList
        } else {
            ((1 to end) ++ (start to n)).toList
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn most_visited(n: i32, rounds: Vec<i32>) -> Vec<i32> {
        let start = rounds[0];
        let end = *rounds.last().unwrap();
        let mut res = Vec::new();
        if start <= end {
            for i in start..=end {
                res.push(i);
            }
        } else {
            for i in 1..=end {
                res.push(i);
            }
            for i in start..=n {
                res.push(i);
            }
        }
        res
    }
}
```

## Racket

```racket
(define/contract (most-visited n rounds)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?))
  (let* ((len (length rounds))
         (start (list-ref rounds 0))
         (end (list-ref rounds (- len 1)))
         (seq (if (<= start end)
                  (range start (+ end 1))
                  (append (range start (+ n 1)) (range 1 (+ end 1))))))
    (sort seq <)))
```

## Erlang

```erlang
-module(solution).
-export([most_visited/2]).

-spec most_visited(N :: integer(), Rounds :: [integer()]) -> [integer()].
most_visited(N, Rounds) ->
    Start = hd(Rounds),
    End = lists:last(Rounds),
    case Start =< End of
        true -> lists:seq(Start, End);
        false -> lists:seq(1, End) ++ lists:seq(Start, N)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec most_visited(n :: integer, rounds :: [integer]) :: [integer]
  def most_visited(_n, rounds) do
    start = hd(rounds)
    finish = List.last(rounds)

    if start <= finish do
      Enum.to_list(start..finish)
    else
      Enum.to_list(1..finish) ++ Enum.to_list(start.._n)
    end
  end
end
```
