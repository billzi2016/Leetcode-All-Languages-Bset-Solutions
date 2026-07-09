# 2244. Minimum Rounds to Complete All Tasks

## Cpp

```cpp
class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        unordered_map<int, int> cnt;
        for (int t : tasks) ++cnt[t];
        long long rounds = 0;
        for (auto& p : cnt) {
            int f = p.second;
            if (f == 1) return -1;
            rounds += f / 3 + (f % 3 ? 1 : 0);
        }
        return (int)rounds;
    }
};
```

## Java

```java
class Solution {
    public int minimumRounds(int[] tasks) {
        java.util.Map<Integer, Integer> freq = new java.util.HashMap<>();
        for (int t : tasks) {
            freq.put(t, freq.getOrDefault(t, 0) + 1);
        }
        int rounds = 0;
        for (int count : freq.values()) {
            if (count == 1) return -1;
            int mod = count % 3;
            if (mod == 0) {
                rounds += count / 3;
            } else if (mod == 1) {
                // use two groups of 2 and the rest as groups of 3
                rounds += (count - 4) / 3 + 2;
            } else { // mod == 2
                rounds += count / 3 + 1;
            }
        }
        return rounds;
    }
}
```

## Python

```python
class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        from collections import Counter
        freq = Counter(tasks)
        rounds = 0
        for cnt in freq.values():
            if cnt == 1:
                return -1
            # Minimum number of rounds using groups of 2 or 3.
            rounds += (cnt + 2) // 3
        return rounds
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = Counter(tasks)
        total_rounds = 0
        for cnt in freq.values():
            if cnt == 1:
                return -1
            # Use as many groups of 3 as possible, adjust for remainder 1
            rounds = cnt // 3
            rem = cnt % 3
            if rem == 0:
                total_rounds += rounds
            elif rem == 1:
                # need to replace one group of 3 with two groups of 2
                total_rounds += (rounds - 1) + 2
            else:  # rem == 2
                total_rounds += rounds + 1
        return total_rounds
```

## C

```c
#include <stdlib.h>

static int int_cmp(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int minimumRounds(int* tasks, int tasksSize) {
    if (tasksSize == 0) return 0;
    qsort(tasks, tasksSize, sizeof(int), int_cmp);
    
    int totalRounds = 0;
    int i = 0;
    while (i < tasksSize) {
        int cnt = 1;
        while (i + cnt < tasksSize && tasks[i + cnt] == tasks[i]) {
            cnt++;
        }
        if (cnt == 1) return -1;
        totalRounds += cnt / 3 + (cnt % 3 ? 1 : 0);
        i += cnt;
    }
    return totalRounds;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumRounds(int[] tasks) {
        var freq = new Dictionary<int, int>();
        foreach (var t in tasks) {
            if (freq.ContainsKey(t)) freq[t]++;
            else freq[t] = 1;
        }
        long totalRounds = 0;
        foreach (var kvp in freq) {
            int cnt = kvp.Value;
            if (cnt == 1) return -1;
            int rounds = cnt / 3;
            int rem = cnt % 3;
            if (rem == 0) {
                // nothing to add
            } else if (rem == 1) {
                // replace one group of 3 with two groups of 2
                rounds -= 1;
                rounds += 2;
            } else { // rem == 2
                rounds += 1;
            }
            totalRounds += rounds;
        }
        return (int)totalRounds;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} tasks
 * @return {number}
 */
var minimumRounds = function(tasks) {
    const freqMap = new Map();
    for (const t of tasks) {
        freqMap.set(t, (freqMap.get(t) || 0) + 1);
    }
    let totalRounds = 0;
    for (const cnt of freqMap.values()) {
        if (cnt === 1) return -1;
        const groupsOfThree = Math.floor(cnt / 3);
        const remainder = cnt % 3;
        if (remainder === 0) {
            totalRounds += groupsOfThree;
        } else if (remainder === 1) {
            // need to replace one group of three with two groups of two
            if (groupsOfThree >= 1) {
                totalRounds += (groupsOfThree - 1) + 2;
            } else {
                // cnt == 4 case
                totalRounds += 2;
            }
        } else { // remainder === 2
            totalRounds += groupsOfThree + 1;
        }
    }
    return totalRounds;
};
```

## Typescript

```typescript
function minimumRounds(tasks: number[]): number {
    const freq = new Map<number, number>();
    for (const t of tasks) {
        freq.set(t, (freq.get(t) ?? 0) + 1);
    }
    let rounds = 0;
    for (const count of freq.values()) {
        if (count === 1) return -1;
        const mod = count % 3;
        if (mod === 0) {
            rounds += count / 3;
        } else if (mod === 1) {
            // use two groups of 2 and the rest as groups of 3
            rounds += Math.floor((count - 4) / 3) + 2;
        } else { // mod === 2
            rounds += Math.floor(count / 3) + 1;
        }
    }
    return rounds;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $tasks
     * @return Integer
     */
    function minimumRounds($tasks) {
        $freq = [];
        foreach ($tasks as $t) {
            if (!isset($freq[$t])) {
                $freq[$t] = 0;
            }
            $freq[$t]++;
        }

        $rounds = 0;
        foreach ($freq as $cnt) {
            if ($cnt == 1) {
                return -1;
            }
            $rem = $cnt % 3;
            if ($rem == 0) {
                $rounds += intdiv($cnt, 3);
            } elseif ($rem == 1) {
                // need to replace one group of 3 with two groups of 2
                $rounds += intdiv($cnt - 4, 3) + 2;
            } else { // $rem == 2
                $rounds += intdiv($cnt, 3) + 1;
            }
        }

        return $rounds;
    }
}
```

## Swift

```swift
class Solution {
    func minimumRounds(_ tasks: [Int]) -> Int {
        var freq = [Int:Int]()
        for t in tasks {
            freq[t, default: 0] += 1
        }
        var total = 0
        for count in freq.values {
            if count == 1 { return -1 }
            let rem = count % 3
            var rounds = 0
            if rem == 0 {
                rounds = count / 3
            } else if rem == 1 {
                // count >= 4 because count != 1
                rounds = (count - 4) / 3 + 2
            } else { // rem == 2
                rounds = count / 3 + 1
            }
            total += rounds
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumRounds(tasks: IntArray): Int {
        val freq = HashMap<Int, Int>()
        for (t in tasks) {
            freq[t] = (freq[t] ?: 0) + 1
        }
        var rounds = 0
        for (cnt in freq.values) {
            if (cnt == 1) return -1
            rounds += cnt / 3
            if (cnt % 3 != 0) rounds += 1
        }
        return rounds
    }
}
```

## Dart

```dart
class Solution {
  int minimumRounds(List<int> tasks) {
    final Map<int, int> count = {};
    for (var t in tasks) {
      count[t] = (count[t] ?? 0) + 1;
    }
    int rounds = 0;
    for (var freq in count.values) {
      if (freq == 1) return -1;
      final rem = freq % 3;
      if (rem == 0) {
        rounds += freq ~/ 3;
      } else if (rem == 1) {
        // need to replace one group of 3 with two groups of 2
        rounds += ((freq - 4) ~/ 3) + 2;
      } else { // rem == 2
        rounds += (freq ~/ 3) + 1;
      }
    }
    return rounds;
  }
}
```

## Golang

```go
func minimumRounds(tasks []int) int {
    freq := make(map[int]int)
    for _, t := range tasks {
        freq[t]++
    }
    rounds := 0
    for _, cnt := range freq {
        if cnt == 1 {
            return -1
        }
        switch cnt % 3 {
        case 0:
            rounds += cnt / 3
        case 1:
            // cnt >= 4 because cnt==1 handled above
            rounds += (cnt-4)/3 + 2
        case 2:
            rounds += (cnt-2)/3 + 1
        }
    }
    return rounds
}
```

## Ruby

```ruby
def minimum_rounds(tasks)
  freq = Hash.new(0)
  tasks.each { |t| freq[t] += 1 }
  rounds = 0
  freq.each_value do |cnt|
    return -1 if cnt == 1
    case cnt % 3
    when 0
      rounds += cnt / 3
    when 1
      rounds += (cnt - 4) / 3 + 2
    else # remainder 2
      rounds += cnt / 3 + 1
    end
  end
  rounds
end
```

## Scala

```scala
object Solution {
    def minimumRounds(tasks: Array[Int]): Int = {
        val freq = scala.collection.mutable.Map[Int, Int]()
        for (t <- tasks) {
            freq(t) = freq.getOrElse(t, 0) + 1
        }
        var total = 0
        for ((_, cnt) <- freq) {
            if (cnt == 1) return -1
            val mod = cnt % 3
            total += mod match {
                case 0 => cnt / 3
                case 1 => (cnt - 4) / 3 + 2
                case 2 => cnt / 3 + 1
            }
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_rounds(tasks: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for t in tasks {
            *freq.entry(t).or_insert(0) += 1;
        }
        let mut rounds = 0i32;
        for &cnt in freq.values() {
            if cnt == 1 {
                return -1;
            }
            rounds += cnt / 3 + if cnt % 3 == 0 { 0 } else { 1 };
        }
        rounds
    }
}
```

## Racket

```racket
(define/contract (minimum-rounds tasks)
  (-> (listof exact-integer?) exact-integer?)
  (let ([freq (make-hash)])
    ;; count frequencies
    (for-each (lambda (t) (hash-update! freq t add1 0)) tasks)
    (let ([total 0] [impossible #f])
      (for ([cnt (in-hash-values freq)])
        (cond [(= cnt 1) (set! impossible #t)]
              [else
               (let* ([rem (remainder cnt 3)]
                      [add (cond [(= rem 0) (/ cnt 3)]
                                 [(= rem 2) (+ (quotient cnt 3) 1)]
                                 [else ; rem = 1
                                  (if (= cnt 4)
                                      2
                                      (+ (quotient (- cnt 4) 3) 2))])])
                 (set! total (+ total add)))]))
      (if impossible -1 total))))
```

## Erlang

```erlang
-spec minimum_rounds(Tasks :: [integer()]) -> integer().
minimum_rounds(Tasks) ->
    FreqMap = build_freq_map(Tasks, #{}),
    case compute_total(FreqMap) of
        {ok, Total} -> Total;
        error -> -1
    end.

build_freq_map([], Map) -> Map;
build_freq_map([H|T], Map) ->
    Count = maps:get(H, Map, 0),
    build_freq_map(T, maps:put(H, Count + 1, Map)).

compute_total(Map) ->
    compute_total(maps:values(Map), 0).

compute_total([], Sum) -> {ok, Sum};
compute_total([C|Rest], Acc) ->
    case rounds_for(C) of
        -1 -> error;
        R -> compute_total(Rest, Acc + R)
    end.

rounds_for(1) -> -1;
rounds_for(C) ->
    case C rem 3 of
        0 -> C div 3;
        _ -> (C div 3) + 1
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_rounds(tasks :: [integer]) :: integer
  def minimum_rounds(tasks) do
    freqs =
      Enum.reduce(tasks, %{}, fn t, acc ->
        Map.update(acc, t, 1, &(&1 + 1))
      end)

    Enum.reduce_while(freqs, 0, fn {_k, cnt}, total ->
      if cnt == 1 do
        {:halt, -1}
      else
        rem = rem(cnt, 3)
        rounds = div(cnt, 3) + (if rem == 0, do: 0, else: 1)
        {:cont, total + rounds}
      end
    end)
  end
end
```
