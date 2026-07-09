# 1103. Distribute Candies to People

## Cpp

```cpp
class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        vector<int> ans(num_people, 0);
        long long i = 0;
        while (candies > 0) {
            int give = (int)min<long long>(candies, i + 1);
            ans[i % num_people] += give;
            candies -= give;
            ++i;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] distributeCandies(int candies, int num_people) {
        int[] ans = new int[num_people];
        int give = 1;
        int idx = 0;
        while (candies > 0) {
            int cur = Math.min(give, candies);
            ans[idx] += cur;
            candies -= cur;
            give++;
            idx = (idx + 1) % num_people;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        ans = [0] * num_people
        i = 0  # turn counter starting from 0, gives i+1 candies
        while candies > 0:
            give = i + 1
            idx = i % num_people
            if candies >= give:
                ans[idx] += give
                candies -= give
            else:
                ans[idx] += candies
                break
            i += 1
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        distribution = [0] * num_people
        give = 1
        idx = 0
        while candies > 0:
            take = give if candies >= give else candies
            distribution[idx] += take
            candies -= take
            give += 1
            idx = (idx + 1) % num_people
        return distribution
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* distributeCandies(int candies, int num_people, int* returnSize) {
    *returnSize = num_people;
    int* ans = (int*)calloc(num_people, sizeof(int));
    long long i = 0; // turn counter
    while (candies > 0) {
        int idx = i % num_people;
        long long give = i + 1;               // candies to give this turn
        int take = (candies >= give) ? (int)give : candies;
        ans[idx] += take;
        candies -= take;
        i++;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] DistributeCandies(int candies, int num_people) {
        int[] ans = new int[num_people];
        int give = 1;
        int idx = 0;
        while (candies > 0) {
            int take = Math.Min(give, candies);
            ans[idx] += take;
            candies -= take;
            give++;
            idx = (idx + 1) % num_people;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} candies
 * @param {number} num_people
 * @return {number[]}
 */
var distributeCandies = function(candies, num_people) {
    const res = new Array(num_people).fill(0);
    let i = 0;
    let give = 1;
    while (candies > 0) {
        const take = Math.min(give, candies);
        res[i] += take;
        candies -= take;
        i = (i + 1) % num_people;
        give++;
    }
    return res;
};
```

## Typescript

```typescript
function distributeCandies(candies: number, num_people: number): number[] {
    const result = new Array(num_people).fill(0);
    let give = 1;
    let idx = 0;
    while (candies > 0) {
        if (candies >= give) {
            result[idx] += give;
            candies -= give;
        } else {
            result[idx] += candies;
            break;
        }
        give++;
        idx = (idx + 1) % num_people;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $candies
     * @param Integer $num_people
     * @return Integer[]
     */
    function distributeCandies($candies, $num_people) {
        $distribution = array_fill(0, $num_people, 0);
        $give = 1;
        $i = 0;
        while ($candies > 0) {
            $idx = $i % $num_people;
            $take = min($candies, $give);
            $distribution[$idx] += $take;
            $candies -= $take;
            $give++;
            $i++;
        }
        return $distribution;
    }
}
```

## Swift

```swift
class Solution {
    func distributeCandies(_ candies: Int, _ num_people: Int) -> [Int] {
        var result = Array(repeating: 0, count: num_people)
        var remaining = candies
        var give = 1
        var index = 0
        
        while remaining > 0 {
            let amount = min(remaining, give)
            result[index] += amount
            remaining -= amount
            give += 1
            index = (index + 1) % num_people
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distributeCandies(candies: Int, num_people: Int): IntArray {
        val result = IntArray(num_people)
        var remaining = candies
        var give = 1
        var idx = 0
        while (remaining > 0) {
            if (remaining >= give) {
                result[idx] += give
                remaining -= give
            } else {
                result[idx] += remaining
                break
            }
            give++
            idx = (idx + 1) % num_people
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> distributeCandies(int candies, int num_people) {
    List<int> ans = List.filled(num_people, 0);
    int give = 1;
    int idx = 0;
    while (candies > 0) {
      if (candies >= give) {
        ans[idx] += give;
        candies -= give;
      } else {
        ans[idx] += candies;
        break;
      }
      give++;
      idx = (idx + 1) % num_people;
    }
    return ans;
  }
}
```

## Golang

```go
func distributeCandies(candies int, num_people int) []int {
    result := make([]int, num_people)
    give := 1
    idx := 0
    for candies > 0 {
        if candies >= give {
            result[idx] += give
            candies -= give
        } else {
            result[idx] += candies
            candies = 0
        }
        give++
        idx = (idx + 1) % num_people
    }
    return result
}
```

## Ruby

```ruby
def distribute_candies(candies, num_people)
  distribution = Array.new(num_people, 0)
  give = 1
  while candies > 0
    idx = (give - 1) % num_people
    take = [candies, give].min
    distribution[idx] += take
    candies -= take
    give += 1
  end
  distribution
end
```

## Scala

```scala
object Solution {
    def distributeCandies(candies: Int, num_people: Int): Array[Int] = {
        val res = new Array[Int](num_people)
        var remaining = candies
        var give = 1
        var idx = 0
        while (remaining > 0) {
            val cur = if (give <= remaining) give else remaining
            res(idx) += cur
            remaining -= cur
            give += 1
            idx = (idx + 1) % num_people
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn distribute_candies(candies: i32, num_people: i32) -> Vec<i32> {
        let n = num_people as usize;
        let mut ans = vec![0i64; n];
        let mut remaining = candies as i64;
        let mut give = 1i64;
        let mut idx = 0usize;
        while remaining > 0 {
            let take = if remaining >= give { give } else { remaining };
            ans[idx] += take;
            remaining -= take;
            give += 1;
            idx = (idx + 1) % n;
        }
        ans.into_iter().map(|x| x as i32).collect()
    }
}
```

## Racket

```racket
(define/contract (distribute-candies candies num_people)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  (let* ([arr (make-vector num_people 0)]
         [i   1])
    (let loop ()
      (when (> candies 0)
        (define give (if (< candies i) candies i))
        (define idx (modulo (- i 1) num_people))
        (vector-set! arr idx (+ (vector-ref arr idx) give))
        (set! candies (- candies give))
        (set! i (+ i 1))
        (loop)))
    (vector->list arr)))
```

## Erlang

```erlang
-module(solution).
-export([distribute_candies/2]).

-spec distribute_candies(Candies :: integer(), Num_people :: integer()) -> [integer()].
distribute_candies(Candies, Num_people) ->
    Tuple0 = list_to_tuple(lists:duplicate(Num_people, 0)),
    distribute_loop(Candies, 1, 0, Num_people, Tuple0).

-spec distribute_loop(integer(), integer(), integer(), integer(), tuple()) -> [integer()].
distribute_loop(0, _Give, _Idx, _N, Tuple) ->
    tuple_to_list(Tuple);
distribute_loop(CandiesLeft, Give, Idx, N, Tuple) ->
    ToGive = if CandiesLeft >= Give -> Give; true -> CandiesLeft end,
    Current = element(Idx + 1, Tuple),
    NewTuple = setelement(Idx + 1, Tuple, Current + ToGive),
    distribute_loop(CandiesLeft - ToGive, Give + 1, (Idx + 1) rem N, N, NewTuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec distribute_candies(candies :: integer, num_people :: integer) :: [integer]
  def distribute_candies(candies, num_people) do
    initial = for _ <- 1..num_people, do: 0
    distribute(candies, initial, 1, 0, num_people)
  end

  defp distribute(0, acc, _, _, _) do
    acc
  end

  defp distribute(candies, acc, give, idx, n) do
    amount = if candies < give, do: candies, else: give
    updated = List.update_at(acc, idx, &(&1 + amount))
    next_candies = candies - amount
    next_idx = rem(idx + 1, n)
    distribute(next_candies, updated, give + 1, next_idx, n)
  end
end
```
