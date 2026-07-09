# 0904. Fruit Into Baskets

## Cpp

```cpp
class Solution {
public:
    int totalFruit(std::vector<int>& fruits) {
        std::unordered_map<int, int> cnt;
        int left = 0, maxLen = 0;
        for (int right = 0; right < (int)fruits.size(); ++right) {
            ++cnt[fruits[right]];
            while (cnt.size() > 2) {
                if (--cnt[fruits[left]] == 0) {
                    cnt.erase(fruits[left]);
                }
                ++left;
            }
            maxLen = std::max(maxLen, right - left + 1);
        }
        return maxLen;
    }
};
```

## Java

```java
class Solution {
    public int totalFruit(int[] fruits) {
        if (fruits == null || fruits.length == 0) return 0;
        java.util.Map<Integer, Integer> countMap = new java.util.HashMap<>();
        int left = 0, max = 0;
        for (int right = 0; right < fruits.length; right++) {
            countMap.put(fruits[right], countMap.getOrDefault(fruits[right], 0) + 1);
            while (countMap.size() > 2) {
                int leftFruit = fruits[left];
                int cnt = countMap.get(leftFruit) - 1;
                if (cnt == 0) {
                    countMap.remove(leftFruit);
                } else {
                    countMap.put(leftFruit, cnt);
                }
                left++;
            }
            max = Math.max(max, right - left + 1);
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0
        counts = {}
        max_len = 0

        for right, fruit in enumerate(fruits):
            counts[fruit] = counts.get(fruit, 0) + 1

            while len(counts) > 2:
                left_fruit = fruits[left]
                counts[left_fruit] -= 1
                if counts[left_fruit] == 0:
                    del counts[left_fruit]
                left += 1

            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len

        return max_len
```

## Python3

```python
class Solution:
    def totalFruit(self, fruits):
        from collections import defaultdict
        count = defaultdict(int)
        left = 0
        max_len = 0

        for right, fruit in enumerate(fruits):
            count[fruit] += 1
            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1
                if count[left_fruit] == 0:
                    del count[left_fruit]
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len
```

## C

```c
int totalFruit(int* fruits, int fruitsSize) {
    if (fruitsSize == 0) return 0;
    int *cnt = (int *)calloc(fruitsSize, sizeof(int));
    int left = 0, distinct = 0, maxlen = 0;
    for (int right = 0; right < fruitsSize; ++right) {
        if (cnt[fruits[right]] == 0) distinct++;
        cnt[fruits[right]]++;
        while (distinct > 2) {
            cnt[fruits[left]]--;
            if (cnt[fruits[left]] == 0) distinct--;
            left++;
        }
        int len = right - left + 1;
        if (len > maxlen) maxlen = len;
    }
    free(cnt);
    return maxlen;
}
```

## Csharp

```csharp
public class Solution {
    public int TotalFruit(int[] fruits) {
        if (fruits == null || fruits.Length == 0) return 0;
        var count = new Dictionary<int, int>();
        int left = 0, maxLen = 0;
        for (int right = 0; right < fruits.Length; right++) {
            int fruit = fruits[right];
            if (!count.ContainsKey(fruit))
                count[fruit] = 0;
            count[fruit]++;
            
            while (count.Count > 2) {
                int leftFruit = fruits[left];
                count[leftFruit]--;
                if (count[leftFruit] == 0)
                    count.Remove(leftFruit);
                left++;
            }
            maxLen = Math.Max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} fruits
 * @return {number}
 */
var totalFruit = function(fruits) {
    let left = 0;
    const count = new Map();
    let maxLen = 0;

    for (let right = 0; right < fruits.length; right++) {
        const fruit = fruits[right];
        count.set(fruit, (count.get(fruit) || 0) + 1);

        while (count.size > 2) {
            const leftFruit = fruits[left];
            const newCnt = count.get(leftFruit) - 1;
            if (newCnt === 0) {
                count.delete(leftFruit);
            } else {
                count.set(leftFruit, newCnt);
            }
            left++;
        }

        maxLen = Math.max(maxLen, right - left + 1);
    }

    return maxLen;
};
```

## Typescript

```typescript
function totalFruit(fruits: number[]): number {
    const cnt = new Map<number, number>();
    let left = 0;
    let maxLen = 0;

    for (let right = 0; right < fruits.length; right++) {
        const fruit = fruits[right];
        cnt.set(fruit, (cnt.get(fruit) ?? 0) + 1);

        while (cnt.size > 2) {
            const leftFruit = fruits[left];
            const cur = cnt.get(leftFruit)! - 1;
            if (cur === 0) {
                cnt.delete(leftFruit);
            } else {
                cnt.set(leftFruit, cur);
            }
            left++;
        }

        maxLen = Math.max(maxLen, right - left + 1);
    }

    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $fruits
     * @return Integer
     */
    function totalFruit($fruits) {
        $counts = [];
        $left = 0;
        $maxLen = 0;
        $n = count($fruits);
        for ($right = 0; $right < $n; $right++) {
            $fruit = $fruits[$right];
            if (!isset($counts[$fruit])) {
                $counts[$fruit] = 0;
            }
            $counts[$fruit]++;
            
            while (count($counts) > 2) {
                $leftFruit = $fruits[$left];
                $counts[$leftFruit]--;
                if ($counts[$leftFruit] == 0) {
                    unset($counts[$leftFruit]);
                }
                $left++;
            }
            
            $currentLen = $right - $left + 1;
            if ($currentLen > $maxLen) {
                $maxLen = $currentLen;
            }
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func totalFruit(_ fruits: [Int]) -> Int {
        var left = 0
        var maxLen = 0
        var count = [Int:Int]()
        
        for right in 0..<fruits.count {
            let fruit = fruits[right]
            count[fruit, default: 0] += 1
            
            while count.keys.count > 2 {
                let leftFruit = fruits[left]
                if let c = count[leftFruit] {
                    if c == 1 {
                        count.removeValue(forKey: leftFruit)
                    } else {
                        count[leftFruit] = c - 1
                    }
                }
                left += 1
            }
            
            maxLen = max(maxLen, right - left + 1)
        }
        
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun totalFruit(fruits: IntArray): Int {
        var left = 0
        val count = HashMap<Int, Int>()
        var maxLen = 0
        for (right in fruits.indices) {
            val fruit = fruits[right]
            count[fruit] = count.getOrDefault(fruit, 0) + 1
            while (count.size > 2) {
                val leftFruit = fruits[left]
                count[leftFruit] = count[leftFruit]!! - 1
                if (count[leftFruit] == 0) {
                    count.remove(leftFruit)
                }
                left++
            }
            maxLen = kotlin.math.max(maxLen, right - left + 1)
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int totalFruit(List<int> fruits) {
    Map<int, int> count = {};
    int left = 0;
    int maxLen = 0;

    for (int right = 0; right < fruits.length; right++) {
      int fruit = fruits[right];
      count[fruit] = (count[fruit] ?? 0) + 1;

      while (count.length > 2) {
        int leftFruit = fruits[left];
        count[leftFruit] = count[leftFruit]! - 1;
        if (count[leftFruit] == 0) {
          count.remove(leftFruit);
        }
        left++;
      }

      int currentLen = right - left + 1;
      if (currentLen > maxLen) {
        maxLen = currentLen;
      }
    }

    return maxLen;
  }
}
```

## Golang

```go
func totalFruit(fruits []int) int {
    counts := make(map[int]int)
    left, maxLen := 0, 0
    for right, f := range fruits {
        counts[f]++
        for len(counts) > 2 {
            lf := fruits[left]
            counts[lf]--
            if counts[lf] == 0 {
                delete(counts, lf)
            }
            left++
        }
        if cur := right - left + 1; cur > maxLen {
            maxLen = cur
        }
    }
    return maxLen
}
```

## Ruby

```ruby
def total_fruit(fruits)
  count = {}
  left = 0
  max_len = 0

  fruits.each_with_index do |fruit, right|
    count[fruit] = (count[fruit] || 0) + 1

    while count.size > 2
      left_fruit = fruits[left]
      count[left_fruit] -= 1
      count.delete(left_fruit) if count[left_fruit] == 0
      left += 1
    end

    current_len = right - left + 1
    max_len = current_len if current_len > max_len
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def totalFruit(fruits: Array[Int]): Int = {
        import scala.collection.mutable
        val count = mutable.Map[Int, Int]()
        var left = 0
        var maxLen = 0
        for (right <- fruits.indices) {
            val fruit = fruits(right)
            count.put(fruit, count.getOrElse(fruit, 0) + 1)
            while (count.size > 2) {
                val leftFruit = fruits(left)
                count.update(leftFruit, count(leftFruit) - 1)
                if (count(leftFruit) == 0) count.remove(leftFruit)
                left += 1
            }
            maxLen = math.max(maxLen, right - left + 1)
        }
        maxLen
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn total_fruit(fruits: Vec<i32>) -> i32 {
        let mut count: HashMap<i32, usize> = HashMap::new();
        let mut left = 0usize;
        let mut max_len = 0usize;

        for (right, &fruit) in fruits.iter().enumerate() {
            *count.entry(fruit).or_insert(0) += 1;

            while count.len() > 2 {
                let left_fruit = fruits[left];
                if let Some(c) = count.get_mut(&left_fruit) {
                    *c -= 1;
                    if *c == 0 {
                        count.remove(&left_fruit);
                    }
                }
                left += 1;
            }

            max_len = max_len.max(right - left + 1);
        }

        max_len as i32
    }
}
```

## Racket

```racket
(define/contract (total-fruit fruits)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([v (list->vector fruits)]
         [n (vector-length v)])
    (let outer ((right 0) (left 0) (cnt (make-hash)) (maxlen 0))
      (if (= right n)
          maxlen
          (begin
            (define val (vector-ref v right))
            (hash-set! cnt val (+ (hash-ref cnt val 0) 1))
            (call-with-values
                (lambda ()
                  (let loop-shrink ((l left) (c cnt))
                    (if (> (hash-count c) 2)
                        (let* ([lval (vector-ref v l)]
                               [newc (- (hash-ref c lval) 1)])
                          (if (= newc 0)
                              (hash-remove! c lval)
                              (hash-set! c lval newc))
                          (loop-shrink (+ l 1) c))
                        (values l c))))
              (lambda (new-left new-cnt)
                (define new-maxlen (max maxlen (+ (- right new-left) 1)))
                (outer (+ right 1) new-left new-cnt new-maxlen)))))))))
```

## Erlang

```erlang
-module(solution).
-export([total_fruit/1]).

-spec total_fruit(Fruits :: [integer()]) -> integer().
total_fruit(Fruits) ->
    case Fruits of
        [] -> 0;
        _ ->
            Tuple = list_to_tuple(Fruits),
            Len = tuple_size(Tuple),
            loop(0, 0, #{}, 0, 0, Tuple, Len)
    end.

loop(Right, Left, Map, Distinct, Max, Tuple, Len) when Right == Len ->
    Max;
loop(Right, Left, Map, Distinct, Max, Tuple, Len) ->
    Fruit = element(Right + 1, Tuple),
    Count0 = maps:get(Fruit, Map, 0),
    Count1 = Count0 + 1,
    Map1 = maps:put(Fruit, Count1, Map),
    Distinct1 = if Count0 == 0 -> Distinct + 1; true -> Distinct end,
    {Left2, Map2, Distinct2} = adjust_window(Left, Map1, Distinct1, Tuple),
    WindowSize = Right - Left2 + 1,
    Max1 = if WindowSize > Max -> WindowSize; true -> Max end,
    loop(Right + 1, Left2, Map2, Distinct2, Max1, Tuple, Len).

adjust_window(Left, Map, Distinct, _Tuple) when Distinct =< 2 ->
    {Left, Map, Distinct};
adjust_window(Left, Map, Distinct, Tuple) ->
    FruitL = element(Left + 1, Tuple),
    C0 = maps:get(FruitL, Map),
    C1 = C0 - 1,
    case C1 of
        0 ->
            Map1 = maps:remove(FruitL, Map),
            Distinct1 = Distinct - 1;
        _ ->
            Map1 = maps:put(FruitL, C1, Map),
            Distinct1 = Distinct
    end,
    adjust_window(Left + 1, Map1, Distinct1, Tuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec total_fruit(fruits :: [integer]) :: integer
  def total_fruit(fruits) do
    fruit_tuple = List.to_tuple(fruits)
    n = tuple_size(fruit_tuple)

    {state, _} =
      Enum.reduce(0..(n - 1), {%{left: 0, cnts: %{}, max: 0}, nil}, fn right, {st, _} ->
        fruit = elem(fruit_tuple, right)
        cnts = Map.update(st.cnts, fruit, 1, &(&1 + 1))
        left = st.left

        {left, cnts} =
          if map_size(cnts) <= 2 do
            {left, cnts}
          else
            shrink_left(left, cnts, fruit_tuple)
          end

        max_len = max(st.max, right - left + 1)

        {%{left: left, cnts: cnts, max: max_len}, nil}
      end)

    state.max
  end

  defp shrink_left(left, cnts, tuple) do
    if map_size(cnts) <= 2 do
      {left, cnts}
    else
      fruit = elem(tuple, left)
      count = Map.get(cnts, fruit) - 1

      cnts =
        if count == 0 do
          Map.delete(cnts, fruit)
        else
          Map.put(cnts, fruit, count)
        end

      shrink_left(left + 1, cnts, tuple)
    end
  end
end
```
