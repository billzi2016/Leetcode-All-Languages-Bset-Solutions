# 1996. The Number of Weak Characters in the Game

## Cpp

```cpp
class Solution {
public:
    int numberOfWeakCharacters(vector<vector<int>>& properties) {
        sort(properties.begin(), properties.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 if (a[0] != b[0]) return a[0] > b[0];          // attack descending
                 return a[1] < b[1];                            // defense ascending for equal attack
             });
        int maxDef = 0;
        int weak = 0;
        for (const auto& p : properties) {
            if (p[1] < maxDef) ++weak;
            else maxDef = p[1];
        }
        return weak;
    }
};
```

## Java

```java
class Solution {
    public int numberOfWeakCharacters(int[][] properties) {
        java.util.Arrays.sort(properties, (a, b) -> {
            if (a[0] != b[0]) return b[0] - a[0]; // attack descending
            return a[1] - b[1]; // defense ascending for same attack
        });
        int maxDefense = 0;
        int weakCount = 0;
        for (int[] p : properties) {
            int defense = p[1];
            if (defense < maxDefense) {
                weakCount++;
            } else {
                maxDefense = defense;
            }
        }
        return weakCount;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        # Sort by descending attack; for same attack sort by ascending defense
        properties.sort(key=lambda x: (-x[0], x[1]))
        max_def = 0
        weak = 0
        for _, d in properties:
            if d < max_def:
                weak += 1
            else:
                max_def = d
        return weak
```

## Python3

```python
class Solution:
    def numberOfWeakCharacters(self, properties):
        # Sort by attack descending, and for same attack sort defense ascending
        properties.sort(key=lambda x: (-x[0], x[1]))
        max_def = 0
        weak = 0
        for _, d in properties:
            if d < max_def:
                weak += 1
            else:
                max_def = d
        return weak
```

## C

```c
#include <stdlib.h>

static int cmp(const void *p1, const void *p2) {
    int *a = *(int **)p1;
    int *b = *(int **)p2;
    if (a[0] != b[0])
        return a[0] - b[0];          // attack ascending
    return b[1] - a[1];              // defense descending for equal attack
}

int numberOfWeakCharacters(int** properties, int propertiesSize, int* propertiesColSize) {
    if (propertiesSize == 0) return 0;
    qsort(properties, propertiesSize, sizeof(int *), cmp);
    
    int maxDef = 0;
    int weak = 0;
    for (int i = propertiesSize - 1; i >= 0; --i) {
        int def = properties[i][1];
        if (def < maxDef)
            ++weak;
        else if (def > maxDef)
            maxDef = def;
    }
    return weak;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumberOfWeakCharacters(int[][] properties)
    {
        Array.Sort(properties, (a, b) =>
        {
            if (a[0] != b[0]) return b[0].CompareTo(a[0]); // descending attack
            return a[1].CompareTo(b[1]);                 // ascending defense for equal attack
        });

        int maxDef = 0;
        int weak = 0;

        foreach (var p in properties)
        {
            if (p[1] < maxDef)
                weak++;
            else
                maxDef = p[1];
        }

        return weak;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} properties
 * @return {number}
 */
var numberOfWeakCharacters = function(properties) {
    // Sort by descending attack; for equal attack sort ascending defense
    properties.sort((a, b) => {
        if (b[0] !== a[0]) return b[0] - a[0];
        return a[1] - b[1];
    });
    
    let maxDef = 0;
    let weakCount = 0;
    
    for (const [, def] of properties) {
        if (def < maxDef) {
            weakCount++;
        } else if (def > maxDef) {
            maxDef = def;
        }
    }
    
    return weakCount;
};
```

## Typescript

```typescript
function numberOfWeakCharacters(properties: number[][]): number {
    // Sort by attack descending, and for equal attack sort defense ascending
    properties.sort((a, b) => {
        if (a[0] !== b[0]) return b[0] - a[0];
        return a[1] - b[1];
    });

    let maxDefense = 0;
    let weakCount = 0;

    for (const [, defense] of properties) {
        if (defense < maxDefense) {
            weakCount++;
        } else {
            maxDefense = defense;
        }
    }

    return weakCount;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $properties
     * @return Integer
     */
    function numberOfWeakCharacters($properties) {
        usort($properties, function ($a, $b) {
            if ($a[0] === $b[0]) {
                // same attack: sort defense ascending
                return $a[1] <=> $b[1];
            }
            // different attack: sort attack descending
            return $b[0] <=> $a[0];
        });

        $maxDef = 0;
        $weak = 0;

        foreach ($properties as $p) {
            if ($p[1] < $maxDef) {
                $weak++;
            } else {
                $maxDef = $p[1];
            }
        }

        return $weak;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfWeakCharacters(_ properties: [[Int]]) -> Int {
        let sorted = properties.sorted { (p1, p2) -> Bool in
            if p1[0] != p2[0] {
                return p1[0] > p2[0]   // attack descending
            } else {
                return p1[1] < p2[1]   // defense ascending for same attack
            }
        }
        
        var maxDefense = 0
        var weakCount = 0
        var i = 0
        let n = sorted.count
        
        while i < n {
            let currentAttack = sorted[i][0]
            var j = i
            
            // Count weak characters in the current attack group
            while j < n && sorted[j][0] == currentAttack {
                if sorted[j][1] < maxDefense {
                    weakCount += 1
                }
                j += 1
            }
            
            // Update maxDefense with defenses from this group
            var k = i
            while k < j {
                if sorted[k][1] > maxDefense {
                    maxDefense = sorted[k][1]
                }
                k += 1
            }
            
            i = j
        }
        
        return weakCount
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfWeakCharacters(properties: Array<IntArray>): Int {
        // Sort by attack descending, and for same attack sort defense ascending
        properties.sortWith(compareByDescending<IntArray> { it[0] }.thenBy { it[1] })
        var maxDefense = 0
        var weakCount = 0
        var i = 0
        val n = properties.size
        while (i < n) {
            var j = i
            // Process all characters with the same attack value
            while (j < n && properties[j][0] == properties[i][0]) {
                if (properties[j][1] < maxDefense) {
                    weakCount++
                }
                j++
            }
            // Update maxDefense with the highest defense in this group
            var k = i
            while (k < j) {
                if (properties[k][1] > maxDefense) {
                    maxDefense = properties[k][1]
                }
                k++
            }
            i = j
        }
        return weakCount
    }
}
```

## Dart

```dart
class Solution {
  int numberOfWeakCharacters(List<List<int>> properties) {
    properties.sort((a, b) {
      if (a[0] != b[0]) return b[0] - a[0]; // attack descending
      return a[1] - b[1]; // defense ascending for equal attack
    });
    int maxDefense = 0;
    int weakCount = 0;
    for (var p in properties) {
      int defense = p[1];
      if (defense < maxDefense) {
        weakCount++;
      } else if (defense > maxDefense) {
        maxDefense = defense;
      }
    }
    return weakCount;
  }
}
```

## Golang

```go
import "sort"

func numberOfWeakCharacters(properties [][]int) int {
    sort.Slice(properties, func(i, j int) bool {
        if properties[i][0] != properties[j][0] {
            return properties[i][0] > properties[j][0]
        }
        return properties[i][1] < properties[j][1]
    })
    maxDef := 0
    weak := 0
    for _, p := range properties {
        if p[1] < maxDef {
            weak++
        } else if p[1] > maxDef {
            maxDef = p[1]
        }
    }
    return weak
}
```

## Ruby

```ruby
def number_of_weak_characters(properties)
  sorted = properties.sort_by { |atk, d| [-atk, d] }
  max_def = 0
  weak = 0
  sorted.each do |_, d|
    if d < max_def
      weak += 1
    else
      max_def = d
    end
  end
  weak
end
```

## Scala

```scala
object Solution {
    def numberOfWeakCharacters(properties: Array[Array[Int]]): Int = {
        val sorted = properties.sortWith { (a, b) =>
            if (a(0) != b(0)) a(0) > b(0)
            else a(1) < b(1)
        }
        var maxDef = 0
        var weak = 0
        for (p <- sorted) {
            val d = p(1)
            if (d < maxDef) weak += 1
            else if (d > maxDef) maxDef = d
        }
        weak
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_weak_characters(mut properties: Vec<Vec<i32>>) -> i32 {
        // Sort by attack descending, and for equal attack, defense ascending
        properties.sort_unstable_by(|a, b| {
            if a[0] != b[0] {
                b[0].cmp(&a[0])
            } else {
                a[1].cmp(&b[1])
            }
        });

        let mut max_defense = 0;
        let mut weak_count = 0;

        for prop in properties.iter() {
            let defense = prop[1];
            if defense < max_defense {
                weak_count += 1;
            } else if defense > max_defense {
                max_defense = defense;
            }
        }

        weak_count as i32
    }
}
```

## Racket

```racket
(define/contract (number-of-weak-characters properties)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([sorted
          (sort properties
                (lambda (a b)
                  (let ([ax (first a)] [dx (second a)]
                        [ay (first b)] [dy (second b)])
                    (cond [(> ax ay) #t]
                          [(< ax ay) #f]
                          [else (< dx dy)]))))])
    (let loop ((lst sorted) (max-def 0) (cnt 0))
      (if (null? lst)
          cnt
          (let* ([def (second (first lst))]
                 [new-cnt (if (< def max-def) (+ cnt 1) cnt)]
                 [new-max (if (> def max-def) def max-def)])
            (loop (rest lst) new-max new-cnt))))))
```

## Erlang

```erlang
-module(solution).
-export([number_of_weak_characters/1]).

-spec number_of_weak_characters(Properties :: [[integer()]]) -> integer().
number_of_weak_characters(Properties) ->
    Sorted = lists:sort(fun compare/2, Properties),
    count_weak(Sorted, 0, 0).

compare([A1, D1], [A2, D2]) ->
    case A1 > A2 of
        true -> true;
        false when A1 < A2 -> false;
        false -> % equal attack values
            D1 < D2
    end.

count_weak([], _MaxDef, Count) ->
    Count;
count_weak([[_, Def] | Rest], MaxDef, Count) when Def < MaxDef ->
    count_weak(Rest, MaxDef, Count + 1);
count_weak([[_, Def] | Rest], MaxDef, Count) ->
    NewMax = erlang:max(MaxDef, Def),
    count_weak(Rest, NewMax, Count).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_weak_characters(properties :: [[integer]]) :: integer
  def number_of_weak_characters(properties) do
    sorted = Enum.sort_by(properties, fn [atk, def] -> {-atk, def} end)

    {_max_def, weak_count} =
      Enum.reduce(sorted, {0, 0}, fn [_atk, defense], {max_def, cnt} ->
        if defense < max_def do
          {max_def, cnt + 1}
        else
          {defense, cnt}
        end
      end)

    weak_count
  end
end
```
