# 1431. Kids With the Greatest Number of Candies

## Cpp

```cpp
class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int mx = 0;
        for (int c : candies) {
            if (c > mx) mx = c;
        }
        vector<bool> res;
        res.reserve(candies.size());
        for (int c : candies) {
            res.push_back(c + extraCandies >= mx);
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = 0;
        for (int c : candies) {
            if (c > max) max = c;
        }
        List<Boolean> result = new ArrayList<>(candies.length);
        for (int c : candies) {
            result.add(c + extraCandies >= max);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        return [c + extraCandies >= max_candies for c in candies]
```

## Python3

```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return [c + extraCandies >= max_candy for c in candies]
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) {
    if (candiesSize == 0) {
        *returnSize = 0;
        return NULL;
    }
    
    int maxCandies = 0;
    for (int i = 0; i < candiesSize; ++i) {
        if (candies[i] > maxCandies) {
            maxCandies = candies[i];
        }
    }
    
    bool* result = (bool*)malloc(sizeof(bool) * candiesSize);
    for (int i = 0; i < candiesSize; ++i) {
        result[i] = (candies[i] + extraCandies >= maxCandies);
    }
    
    *returnSize = candiesSize;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<bool> KidsWithCandies(int[] candies, int extraCandies)
    {
        int max = 0;
        foreach (int c in candies)
        {
            if (c > max) max = c;
        }

        List<bool> result = new List<bool>(candies.Length);
        foreach (int c in candies)
        {
            result.Add(c + extraCandies >= max);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    let max = 0;
    for (let c of candies) {
        if (c > max) max = c;
    }
    return candies.map(c => c + extraCandies >= max);
};
```

## Typescript

```typescript
function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
    const max = Math.max(...candies);
    return candies.map(c => c + extraCandies >= max);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $candies
     * @param Integer $extraCandies
     * @return Boolean[]
     */
    function kidsWithCandies($candies, $extraCandies) {
        $max = 0;
        foreach ($candies as $c) {
            if ($c > $max) {
                $max = $c;
            }
        }
        $result = [];
        foreach ($candies as $c) {
            $result[] = ($c + $extraCandies >= $max);
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func kidsWithCandies(_ candies: [Int], _ extraCandies: Int) -> [Bool] {
        guard let maxCandy = candies.max() else { return [] }
        return candies.map { $0 + extraCandies >= maxCandy }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kidsWithCandies(candies: IntArray, extraCandies: Int): List<Boolean> {
        var max = 0
        for (c in candies) {
            if (c > max) max = c
        }
        val result = ArrayList<Boolean>(candies.size)
        for (c in candies) {
            result.add(c + extraCandies >= max)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<bool> kidsWithCandies(List<int> candies, int extraCandies) {
    int maxCandies = 0;
    for (int c in candies) {
      if (c > maxCandies) maxCandies = c;
    }
    List<bool> result = [];
    for (int c in candies) {
      result.add(c + extraCandies >= maxCandies);
    }
    return result;
  }
}
```

## Golang

```go
func kidsWithCandies(candies []int, extraCandies int) []bool {
    max := 0
    for _, c := range candies {
        if c > max {
            max = c
        }
    }
    result := make([]bool, len(candies))
    for i, c := range candies {
        result[i] = c+extraCandies >= max
    }
    return result
}
```

## Ruby

```ruby
def kids_with_candies(candies, extra_candies)
  max = candies.max
  candies.map { |c| c + extra_candies >= max }
end
```

## Scala

```scala
object Solution {
    def kidsWithCandies(candies: Array[Int], extraCandies: Int): List[Boolean] = {
        val maxCandy = candies.max
        candies.map(_ + extraCandies >= maxCandy).toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        let max = *candies.iter().max().unwrap();
        candies.iter().map(|&c| c + extra_candies >= max).collect()
    }
}
```

## Racket

```racket
(define/contract (kids-with-candies candies extraCandies)
  (-> (listof exact-integer?) exact-integer? (listof boolean?))
  (let* ((maxc (apply max candies))
         (result (map (lambda (c) (>= (+ c extraCandies) maxc)) candies)))
    result))
```

## Erlang

```erlang
-module(solution).
-export([kids_with_candies/2]).

-spec kids_with_candies(Candies :: [integer()], ExtraCandies :: integer()) -> [boolean()].
kids_with_candies(Candies, ExtraCandies) ->
    Max = lists:max(Candies),
    [Candy + ExtraCandies >= Max || Candy <- Candies].
```

## Elixir

```elixir
defmodule Solution do
  @spec kids_with_candies(candies :: [integer], extra_candies :: integer) :: [boolean]
  def kids_with_candies(candies, extra_candies) do
    max = Enum.max(candies)
    Enum.map(candies, fn c -> c + extra_candies >= max end)
  end
end
```
