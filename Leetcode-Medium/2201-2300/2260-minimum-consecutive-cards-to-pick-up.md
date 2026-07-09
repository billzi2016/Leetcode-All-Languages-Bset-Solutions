# 2260. Minimum Consecutive Cards to Pick Up

## Cpp

```cpp
class Solution {
public:
    int minimumCardPickup(std::vector<int>& cards) {
        std::unordered_map<int, int> lastPos;
        int best = INT_MAX;
        for (int i = 0; i < (int)cards.size(); ++i) {
            auto it = lastPos.find(cards[i]);
            if (it != lastPos.end()) {
                best = std::min(best, i - it->second + 1);
            }
            lastPos[cards[i]] = i;
        }
        return best == INT_MAX ? -1 : best;
    }
};
```

## Java

```java
class Solution {
    public int minimumCardPickup(int[] cards) {
        java.util.HashMap<Integer, Integer> lastPos = new java.util.HashMap<>();
        int minLen = Integer.MAX_VALUE;
        for (int i = 0; i < cards.length; i++) {
            int val = cards[i];
            if (lastPos.containsKey(val)) {
                int prevIdx = lastPos.get(val);
                int len = i - prevIdx + 1;
                if (len < minLen) {
                    minLen = len;
                }
            }
            lastPos.put(val, i);
        }
        return minLen == Integer.MAX_VALUE ? -1 : minLen;
    }
}
```

## Python

```python
class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        last_pos = {}
        min_len = float('inf')
        for i, val in enumerate(cards):
            if val in last_pos:
                cur_len = i - last_pos[val] + 1
                if cur_len < min_len:
                    min_len = cur_len
            last_pos[val] = i
        return -1 if min_len == float('inf') else min_len
```

## Python3

```python
from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_pos = {}
        ans = float('inf')
        for i, v in enumerate(cards):
            if v in last_pos:
                ans = min(ans, i - last_pos[v] + 1)
            last_pos[v] = i
        return -1 if ans == float('inf') else ans
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

int minimumCardPickup(int* cards, int cardsSize) {
    const int MAX_VAL = 1000000;
    int *last = (int *)malloc((MAX_VAL + 1) * sizeof(int));
    if (!last) return -1; // allocation failure fallback
    memset(last, -1, (MAX_VAL + 1) * sizeof(int));

    int ans = INT_MAX;
    for (int i = 0; i < cardsSize; ++i) {
        int v = cards[i];
        if (last[v] != -1) {
            int len = i - last[v] + 1;
            if (len < ans) ans = len;
        }
        last[v] = i;
    }

    free(last);
    return (ans == INT_MAX) ? -1 : ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumCardPickup(int[] cards)
    {
        var lastIndex = new Dictionary<int, int>();
        int minLength = int.MaxValue;

        for (int i = 0; i < cards.Length; i++)
        {
            int val = cards[i];
            if (lastIndex.TryGetValue(val, out int prev))
            {
                int length = i - prev + 1;
                if (length < minLength)
                    minLength = length;
            }
            lastIndex[val] = i;
        }

        return minLength == int.MaxValue ? -1 : minLength;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} cards
 * @return {number}
 */
var minimumCardPickup = function(cards) {
    const lastPos = new Map();
    let minLen = Infinity;
    
    for (let i = 0; i < cards.length; i++) {
        const val = cards[i];
        if (lastPos.has(val)) {
            const prevIdx = lastPos.get(val);
            const curLen = i - prevIdx + 1;
            if (curLen < minLen) minLen = curLen;
        }
        lastPos.set(val, i);
    }
    
    return minLen === Infinity ? -1 : minLen;
};
```

## Typescript

```typescript
function minimumCardPickup(cards: number[]): number {
    const lastPos = new Map<number, number>();
    let minLen = Infinity;
    for (let i = 0; i < cards.length; i++) {
        const val = cards[i];
        if (lastPos.has(val)) {
            const prevIdx = lastPos.get(val)!;
            const len = i - prevIdx + 1;
            if (len < minLen) minLen = len;
        }
        lastPos.set(val, i);
    }
    return minLen === Infinity ? -1 : minLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $cards
     * @return Integer
     */
    function minimumCardPickup($cards) {
        $lastPos = [];
        $ans = PHP_INT_MAX;
        foreach ($cards as $i => $v) {
            if (isset($lastPos[$v])) {
                $len = $i - $lastPos[$v] + 1;
                if ($len < $ans) {
                    $ans = $len;
                }
            }
            $lastPos[$v] = $i;
        }
        return $ans === PHP_INT_MAX ? -1 : $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumCardPickup(_ cards: [Int]) -> Int {
        var lastIndex = [Int: Int]()
        var minLength = Int.max
        
        for (i, card) in cards.enumerated() {
            if let prev = lastIndex[card] {
                let length = i - prev + 1
                if length < minLength {
                    minLength = length
                }
            }
            lastIndex[card] = i
        }
        
        return minLength == Int.max ? -1 : minLength
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumCardPickup(cards: IntArray): Int {
        val lastIndex = HashMap<Int, Int>()
        var minLen = Int.MAX_VALUE
        for (i in cards.indices) {
            val value = cards[i]
            if (lastIndex.containsKey(value)) {
                val len = i - lastIndex[value]!! + 1
                if (len < minLen) minLen = len
            }
            lastIndex[value] = i
        }
        return if (minLen == Int.MAX_VALUE) -1 else minLen
    }
}
```

## Dart

```dart
class Solution {
  int minimumCardPickup(List<int> cards) {
    final Map<int, int> lastIndex = {};
    int minLen = cards.length + 1;
    for (int i = 0; i < cards.length; i++) {
      int val = cards[i];
      if (lastIndex.containsKey(val)) {
        int len = i - lastIndex[val]! + 1;
        if (len < minLen) minLen = len;
      }
      lastIndex[val] = i;
    }
    return minLen == cards.length + 1 ? -1 : minLen;
  }
}
```

## Golang

```go
func minimumCardPickup(cards []int) int {
	last := make(map[int]int)
	minLen := len(cards) + 1
	for i, v := range cards {
		if prev, ok := last[v]; ok {
			if length := i - prev + 1; length < minLen {
				minLen = length
			}
		}
		last[v] = i
	}
	if minLen == len(cards)+1 {
		return -1
	}
	return minLen
}
```

## Ruby

```ruby
def minimum_card_pickup(cards)
  last_index = {}
  min_len = Float::INFINITY

  cards.each_with_index do |card, i|
    if last_index.key?(card)
      length = i - last_index[card] + 1
      min_len = length if length < min_len
    end
    last_index[card] = i
  end

  min_len == Float::INFINITY ? -1 : min_len
end
```

## Scala

```scala
object Solution {
  def minimumCardPickup(cards: Array[Int]): Int = {
    import scala.collection.mutable
    val lastPos = mutable.Map[Int, Int]()
    var best = Int.MaxValue

    for (i <- cards.indices) {
      val v = cards(i)
      lastPos.get(v) match {
        case Some(prev) =>
          val len = i - prev + 1
          if (len < best) best = len
        case None => // do nothing
      }
      lastPos(v) = i
    }

    if (best == Int.MaxValue) -1 else best
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_card_pickup(cards: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        let mut last: HashMap<i32, usize> = HashMap::new();
        let mut ans = usize::MAX;
        for (i, &c) in cards.iter().enumerate() {
            if let Some(&prev) = last.get(&c) {
                let len = i - prev + 1;
                if len < ans {
                    ans = len;
                }
            }
            last.insert(c, i);
        }
        if ans == usize::MAX { -1 } else { ans as i32 }
    }
}
```

## Racket

```racket
(define/contract (minimum-card-pickup cards)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length cards))
         (vec (list->vector cards))
         (last-pos (make-hash))
         (best (+ n 1))) ; initialize with a value larger than any possible answer
    (for ([i (in-range n)])
      (let* ((val (vector-ref vec i))
             (prev (hash-ref last-pos val #f)))
        (when prev
          (let ((len (+ 1 (- i prev))))
            (when (< len best)
              (set! best len))))
        (hash-set! last-pos val i)))
    (if (= best (+ n 1))
        -1
        best)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_card_pickup/1]).

-spec minimum_card_pickup(Cards :: [integer()]) -> integer().
minimum_card_pickup(Cards) ->
    Len = length(Cards),
    Best = helper(Cards, 0, #{}, Len + 1),
    if
        Best =< Len -> Best;
        true -> -1
    end.

helper([], _, _, Best) ->
    Best;
helper([H|T], Index, Map, Best) ->
    case maps:find(H, Map) of
        {ok, PrevIdx} ->
            NewBest = min(Best, Index - PrevIdx + 1),
            NewMap = maps:put(H, Index, Map),
            helper(T, Index + 1, NewMap, NewBest);
        error ->
            NewMap = maps:put(H, Index, Map),
            helper(T, Index + 1, NewMap, Best)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_card_pickup(cards :: [integer]) :: integer
  def minimum_card_pickup(cards) do
    {min_len, _} =
      Enum.reduce(Enum.with_index(cards), {nil, %{}}, fn {value, idx},
                                                       {current_min, last_pos} ->
        case Map.get(last_pos, value) do
          nil ->
            {current_min, Map.put(last_pos, value, idx)}

          prev_idx ->
            len = idx - prev_idx + 1

            new_min =
              if current_min == nil or len < current_min do
                len
              else
                current_min
              end

            {new_min, Map.put(last_pos, value, idx)}
        end
      end)

    case min_len do
      nil -> -1
      _ -> min_len
    end
  end
end
```
