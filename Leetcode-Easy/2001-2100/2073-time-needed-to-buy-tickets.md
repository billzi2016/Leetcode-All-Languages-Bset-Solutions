# 2073. Time Needed to Buy Tickets

## Cpp

```cpp
class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int target = tickets[k];
        int time = 0;
        for (int i = 0; i < (int)tickets.size(); ++i) {
            if (i <= k)
                time += min(tickets[i], target);
            else
                time += min(tickets[i], target - 1);
        }
        return time;
    }
};
```

## Java

```java
class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        int target = tickets[k];
        int time = 0;
        for (int i = 0; i < tickets.length; i++) {
            if (i <= k) {
                time += Math.min(tickets[i], target);
            } else {
                time += Math.min(tickets[i], target - 1);
            }
        }
        return time;
    }
}
```

## Python

```python
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        target = tickets[k]
        time = 0
        for i, t in enumerate(tickets):
            if i <= k:
                time += min(t, target)
            else:
                time += min(t, target - 1)
        return time
```

## Python3

```python
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]
        time = 0
        for i, t in enumerate(tickets):
            if i <= k:
                time += min(target, t)
            else:
                time += min(target - 1, t)
        return time
```

## C

```c
int timeRequiredToBuy(int* tickets, int ticketsSize, int k) {
    int target = tickets[k];
    int time = 0;
    for (int i = 0; i < ticketsSize; ++i) {
        if (i <= k) {
            time += tickets[i] < target ? tickets[i] : target;
        } else {
            int limit = target - 1;
            time += tickets[i] < limit ? tickets[i] : limit;
        }
    }
    return time;
}
```

## Csharp

```csharp
public class Solution
{
    public int TimeRequiredToBuy(int[] tickets, int k)
    {
        int target = tickets[k];
        int time = 0;
        int beforeTarget = target - 1;
        if (beforeTarget < 0) beforeTarget = 0;

        for (int i = 0; i < tickets.Length; i++)
        {
            if (i <= k)
                time += Math.Min(tickets[i], target);
            else
                time += Math.Min(tickets[i], beforeTarget);
        }

        return time;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} tickets
 * @param {number} k
 * @return {number}
 */
var timeRequiredToBuy = function(tickets, k) {
    const need = tickets[k];
    let time = 0;
    for (let i = 0; i < tickets.length; i++) {
        if (i <= k) {
            time += Math.min(tickets[i], need);
        } else {
            time += Math.min(tickets[i], need - 1);
        }
    }
    return time;
};
```

## Typescript

```typescript
function timeRequiredToBuy(tickets: number[], k: number): number {
    const target = tickets[k];
    let time = 0;
    for (let i = 0; i < tickets.length; i++) {
        if (i <= k) {
            time += Math.min(tickets[i], target);
        } else {
            time += Math.min(tickets[i], target - 1);
        }
    }
    return time;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $tickets
     * @param Integer $k
     * @return Integer
     */
    function timeRequiredToBuy($tickets, $k) {
        $target = $tickets[$k];
        $time = 0;
        $n = count($tickets);
        for ($i = 0; $i < $n; $i++) {
            if ($i <= $k) {
                $time += min($target, $tickets[$i]);
            } else {
                $time += min($target - 1, $tickets[$i]);
            }
        }
        return $time;
    }
}
```

## Swift

```swift
class Solution {
    func timeRequiredToBuy(_ tickets: [Int], _ k: Int) -> Int {
        let need = tickets[k]
        var time = 0
        for i in 0..<tickets.count {
            if i <= k {
                time += min(tickets[i], need)
            } else {
                time += min(tickets[i], need - 1)
            }
        }
        return time
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun timeRequiredToBuy(tickets: IntArray, k: Int): Int {
        val target = tickets[k]
        var time = 0
        for (i in tickets.indices) {
            time += if (i <= k) {
                kotlin.math.min(tickets[i], target)
            } else {
                kotlin.math.min(tickets[i], target - 1)
            }
        }
        return time
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int timeRequiredToBuy(List<int> tickets, int k) {
    int target = tickets[k];
    int time = 0;
    for (int i = 0; i < tickets.length; i++) {
      if (i <= k) {
        time += min(tickets[i], target);
      } else {
        time += min(tickets[i], target - 1);
      }
    }
    return time;
  }
}
```

## Golang

```go
func timeRequiredToBuy(tickets []int, k int) int {
	target := tickets[k]
	total := 0
	limitAfterK := target - 1
	if limitAfterK < 0 {
		limitAfterK = 0
	}
	for i, t := range tickets {
		if i <= k {
			if t < target {
				total += t
			} else {
				total += target
			}
		} else {
			if t < limitAfterK {
				total += t
			} else {
				total += limitAfterK
			}
		}
	}
	return total
}
```

## Ruby

```ruby
def time_required_to_buy(tickets, k)
  target = tickets[k]
  time = 0
  tickets.each_with_index do |t, i|
    if i <= k
      time += [t, target].min
    else
      time += [t, target - 1].min
    end
  end
  time
end
```

## Scala

```scala
object Solution {
    def timeRequiredToBuy(tickets: Array[Int], k: Int): Int = {
        val target = tickets(k)
        var time = 0
        for (i <- tickets.indices) {
            if (i <= k) {
                time += math.min(target, tickets(i))
            } else {
                time += math.min(target - 1, tickets(i))
            }
        }
        time
    }
}
```

## Rust

```rust
impl Solution {
    pub fn time_required_to_buy(tickets: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let target = tickets[k];
        let mut time = 0;
        for (i, &t) in tickets.iter().enumerate() {
            if i <= k {
                time += std::cmp::min(t, target);
            } else {
                time += std::cmp::min(t, target - 1);
            }
        }
        time
    }
}
```

## Racket

```racket
(define/contract (time-required-to-buy tickets k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((tk (list-ref tickets k))
         (n  (length tickets)))
    (let loop ((i 0) (acc 0))
      (if (= i n)
          acc
          (let* ((ti   (list-ref tickets i))
                 (add  (if (<= i k)
                           (min tk ti)
                           (min (sub1 tk) ti))))
            (loop (+ i 1) (+ acc add)))))))
```

## Erlang

```erlang
-module(solution).
-export([time_required_to_buy/2]).

-spec time_required_to_buy(Tickets :: [integer()], K :: integer()) -> integer().
time_required_to_buy(Tickets, K) ->
    Target = lists:nth(K + 1, Tickets),
    time_required_to_buy(Tickets, K, 0, 0, Target).

time_required_to_buy([], _K, _Idx, Acc, _Target) ->
    Acc;
time_required_to_buy([H|T], K, Idx, Acc, Target) ->
    Add = if
        Idx =< K -> erlang:min(H, Target);
        true     -> erlang:min(H, Target - 1)
    end,
    time_required_to_buy(T, K, Idx + 1, Acc + Add, Target).
```

## Elixir

```elixir
defmodule Solution do
  @spec time_required_to_buy(tickets :: [integer], k :: integer) :: integer
  def time_required_to_buy(tickets, k) do
    target = Enum.at(tickets, k)

    Enum.reduce(Enum.with_index(tickets), 0, fn {cnt, i}, acc ->
      if i <= k do
        acc + min(cnt, target)
      else
        acc + min(cnt, target - 1)
      end
    end)
  end
end
```
