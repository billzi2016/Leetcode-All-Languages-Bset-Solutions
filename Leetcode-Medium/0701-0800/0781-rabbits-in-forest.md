# 0781. Rabbits in Forest

## Cpp

```cpp
class Solution {
public:
    int numRabbits(vector<int>& answers) {
        unordered_map<int,int> freq;
        for (int a : answers) ++freq[a];
        int total = 0;
        for (auto& p : freq) {
            int v = p.first;
            int cnt = p.second;
            int groupSize = v + 1;
            int groups = (cnt + groupSize - 1) / groupSize; // ceil division
            total += groups * groupSize;
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public int numRabbits(int[] answers) {
        java.util.Map<Integer, Integer> freq = new java.util.HashMap<>();
        for (int a : answers) {
            freq.put(a, freq.getOrDefault(a, 0) + 1);
        }
        int total = 0;
        for (java.util.Map.Entry<Integer, Integer> e : freq.entrySet()) {
            int v = e.getKey();
            int cnt = e.getValue();
            int groupSize = v + 1;
            int groups = (cnt + groupSize - 1) / groupSize; // ceil division
            total += groups * groupSize;
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        from collections import Counter
        cnt = Counter(answers)
        total = 0
        for a, freq in cnt.items():
            group_size = a + 1
            groups = (freq + group_size - 1) // group_size
            total += groups * group_size
        return total
```

## Python3

```python
from typing import List
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = {}
        for a in answers:
            freq[a] = freq.get(a, 0) + 1

        total = 0
        for a, count in freq.items():
            group_size = a + 1
            groups_needed = (count + group_size - 1) // group_size
            total += groups_needed * group_size
        return total
```

## C

```c
int numRabbits(int* answers, int answersSize) {
    int cnt[1001] = {0};
    for (int i = 0; i < answersSize; ++i) {
        cnt[answers[i]]++;
    }
    int total = 0;
    for (int k = 0; k <= 1000; ++k) {
        if (cnt[k] == 0) continue;
        int groupSize = k + 1;
        int groups = (cnt[k] + groupSize - 1) / groupSize; // ceil division
        total += groups * groupSize;
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int NumRabbits(int[] answers) {
        var freq = new System.Collections.Generic.Dictionary<int, int>();
        foreach (var a in answers) {
            if (freq.ContainsKey(a))
                freq[a]++;
            else
                freq[a] = 1;
        }

        int total = 0;
        foreach (var kvp in freq) {
            int k = kvp.Key;          // answer value
            int count = kvp.Value;    // number of rabbits with this answer
            int groupSize = k + 1;    // rabbits per color group
            int groups = (count + groupSize - 1) / groupSize; // ceil division
            total += groups * groupSize;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} answers
 * @return {number}
 */
var numRabbits = function(answers) {
    const freq = new Map();
    for (const a of answers) {
        freq.set(a, (freq.get(a) || 0) + 1);
    }
    let total = 0;
    for (const [k, cnt] of freq.entries()) {
        const groupSize = k + 1;
        const groups = Math.ceil(cnt / groupSize);
        total += groups * groupSize;
    }
    return total;
};
```

## Typescript

```typescript
function numRabbits(answers: number[]): number {
    const freqMap = new Map<number, number>();
    for (const ans of answers) {
        freqMap.set(ans, (freqMap.get(ans) ?? 0) + 1);
    }
    let total = 0;
    for (const [ans, cnt] of freqMap.entries()) {
        const groupSize = ans + 1;
        const groups = Math.ceil(cnt / groupSize);
        total += groups * groupSize;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $answers
     * @return Integer
     */
    function numRabbits($answers) {
        $freq = [];
        foreach ($answers as $ans) {
            if (!isset($freq[$ans])) {
                $freq[$ans] = 0;
            }
            $freq[$ans]++;
        }

        $total = 0;
        foreach ($freq as $a => $cnt) {
            $groupSize = $a + 1;
            // ceil division to determine how many groups are needed
            $groups = intdiv($cnt + $groupSize - 1, $groupSize);
            $total += $groups * $groupSize;
        }

        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func numRabbits(_ answers: [Int]) -> Int {
        var freq = [Int:Int]()
        for a in answers {
            freq[a, default: 0] += 1
        }
        var total = 0
        for (a, cnt) in freq {
            let groupSize = a + 1
            let groups = (cnt + groupSize - 1) / groupSize
            total += groups * groupSize
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numRabbits(answers: IntArray): Int {
        val count = mutableMapOf<Int, Int>()
        for (a in answers) {
            count[a] = (count[a] ?: 0) + 1
        }
        var total = 0
        for ((answer, freq) in count) {
            val groupSize = answer + 1
            val groups = (freq + groupSize - 1) / groupSize
            total += groups * groupSize
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int numRabbits(List<int> answers) {
    final Map<int, int> freq = {};
    for (var a in answers) {
      freq[a] = (freq[a] ?? 0) + 1;
    }
    int total = 0;
    freq.forEach((a, count) {
      int groupSize = a + 1;
      int groups = (count + groupSize - 1) ~/ groupSize;
      total += groups * groupSize;
    });
    return total;
  }
}
```

## Golang

```go
func numRabbits(answers []int) int {
    freq := make(map[int]int)
    for _, a := range answers {
        freq[a]++
    }
    total := 0
    for k, cnt := range freq {
        groupSize := k + 1
        groups := (cnt + groupSize - 1) / groupSize
        total += groups * groupSize
    }
    return total
}
```

## Ruby

```ruby
def num_rabbits(answers)
  freq = Hash.new(0)
  answers.each { |a| freq[a] += 1 }
  total = 0
  freq.each do |k, cnt|
    group_size = k + 1
    groups = (cnt + group_size - 1) / group_size
    total += groups * group_size
  end
  total
end
```

## Scala

```scala
object Solution {
    def numRabbits(answers: Array[Int]): Int = {
        val freqMap = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
        for (a <- answers) {
            freqMap(a) += 1
        }
        var total = 0
        for ((a, cnt) <- freqMap) {
            val groupSize = a + 1
            val groups = (cnt + groupSize - 1) / groupSize // ceiling division
            total += groups * groupSize
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_rabbits(answers: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        let mut freq: HashMap<i32, usize> = HashMap::new();
        for a in answers {
            *freq.entry(a).or_insert(0) += 1;
        }
        let mut total = 0i32;
        for (a, &cnt) in freq.iter() {
            let group_size = (*a as usize) + 1;
            let groups = (cnt + group_size - 1) / group_size; // ceil division
            total += (groups * group_size) as i32;
        }
        total
    }
}
```

## Racket

```racket
(define/contract (num-rabbits answers)
  (-> (listof exact-integer?) exact-integer?)
  (let ([cnts (make-hash)])
    ;; count occurrences of each answer
    (for ([a answers])
      (hash-set! cnts a (+ 1 (hash-ref cnts a 0))))
    ;; compute minimal total rabbits
    (for/sum ([(ans cnt) (in-hash cnts)])
      (let* ((group-size (+ ans 1))
             (groups (quotient (+ cnt (- group-size 1)) group-size))) ; ceiling division
        (* groups group-size)))))
```

## Erlang

```erlang
-module(solution).
-export([num_rabbits/1]).

-spec num_rabbits(Answers :: [integer()]) -> integer().
num_rabbits(Answers) ->
    Freq = lists:foldl(
        fun(A, Acc) ->
            maps:update_with(A,
                             fun(C) -> C + 1 end,
                             1,
                             Acc)
        end,
        #{},
        Answers),
    maps:fold(
        fun(Ans, Count, Sum) ->
            GroupSize = Ans + 1,
            Groups = (Count + GroupSize - 1) div GroupSize,
            Sum + Groups * GroupSize
        end,
        0,
        Freq).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_rabbits(answers :: [integer]) :: integer
  def num_rabbits(answers) do
    answers
    |> Enum.frequencies()
    |> Enum.reduce(0, fn {a, cnt}, acc ->
      group_size = a + 1
      groups = div(cnt + a, group_size)
      acc + groups * group_size
    end)
  end
end
```
