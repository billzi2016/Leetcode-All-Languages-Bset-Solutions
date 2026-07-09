# 0881. Boats to Save People

## Cpp

```cpp
class Solution {
public:
    int numRescueBoats(std::vector<int>& people, int limit) {
        std::sort(people.begin(), people.end());
        int i = 0;
        int j = people.size() - 1;
        int boats = 0;
        while (i <= j) {
            if (people[i] + people[j] <= limit) {
                ++i;
            }
            --j;
            ++boats;
        }
        return boats;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int i = 0, j = people.length - 1;
        int boats = 0;
        while (i <= j) {
            if (i == j) {
                boats++;
                break;
            }
            if (people[i] + people[j] <= limit) {
                i++;
            }
            j--;
            boats++;
        }
        return boats;
    }
}
```

## Python

```python
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i, j = 0, len(people) - 1
        boats = 0
        while i <= j:
            if i == j:
                boats += 1
                break
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            boats += 1
        return boats
```

## Python3

```python
from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        boats = 0
        while i <= j:
            if i == j:
                boats += 1
                break
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            boats += 1
        return boats
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int numRescueBoats(int* people, int peopleSize, int limit) {
    if (peopleSize == 0) return 0;
    qsort(people, peopleSize, sizeof(int), cmp_int);
    
    int left = 0;
    int right = peopleSize - 1;
    int boats = 0;
    
    while (left <= right) {
        if (left == right) {
            boats++;
            break;
        }
        if (people[left] + people[right] <= limit) {
            left++;
            right--;
        } else {
            right--;
        }
        boats++;
    }
    
    return boats;
}
```

## Csharp

```csharp
public class Solution {
    public int NumRescueBoats(int[] people, int limit) {
        if (people == null || people.Length == 0) return 0;
        Array.Sort(people);
        int i = 0;
        int j = people.Length - 1;
        int boats = 0;
        while (i <= j) {
            if (people[i] + people[j] <= limit) {
                i++;
            }
            j--;
            boats++;
        }
        return boats;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function(people, limit) {
    people.sort((a, b) => a - b);
    let i = 0;
    let j = people.length - 1;
    let boats = 0;
    while (i <= j) {
        if (people[i] + people[j] <= limit) i++;
        j--;
        boats++;
    }
    return boats;
};
```

## Typescript

```typescript
function numRescueBoats(people: number[], limit: number): number {
    people.sort((a, b) => a - b);
    let i = 0;
    let j = people.length - 1;
    let boats = 0;
    while (i <= j) {
        if (i === j) {
            boats++;
            break;
        }
        if (people[i] + people[j] <= limit) {
            i++;
        }
        j--;
        boats++;
    }
    return boats;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $people
     * @param Integer $limit
     * @return Integer
     */
    function numRescueBoats($people, $limit) {
        sort($people);
        $i = 0;
        $j = count($people) - 1;
        $boats = 0;
        while ($i <= $j) {
            if ($people[$i] + $people[$j] <= $limit) {
                $i++;
            }
            $j--;
            $boats++;
        }
        return $boats;
    }
}
```

## Swift

```swift
class Solution {
    func numRescueBoats(_ people: [Int], _ limit: Int) -> Int {
        let sorted = people.sorted()
        var i = 0
        var j = sorted.count - 1
        var boats = 0
        
        while i <= j {
            if i == j {
                boats += 1
                break
            }
            if sorted[i] + sorted[j] <= limit {
                i += 1
            }
            j -= 1
            boats += 1
        }
        
        return boats
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numRescueBoats(people: IntArray, limit: Int): Int {
        people.sort()
        var i = 0
        var j = people.size - 1
        var boats = 0
        while (i <= j) {
            if (people[i] + people[j] <= limit) {
                i++
            }
            j--
            boats++
        }
        return boats
    }
}
```

## Dart

```dart
class Solution {
  int numRescueBoats(List<int> people, int limit) {
    people.sort();
    int i = 0;
    int j = people.length - 1;
    int boats = 0;
    while (i <= j) {
      if (people[i] + people[j] <= limit) {
        i++;
      }
      j--;
      boats++;
    }
    return boats;
  }
}
```

## Golang

```go
import "sort"

func numRescueBoats(people []int, limit int) int {
    sort.Ints(people)
    i, j := 0, len(people)-1
    boats := 0
    for i <= j {
        if people[i]+people[j] <= limit {
            i++
        }
        j--
        boats++
    }
    return boats
}
```

## Ruby

```ruby
def num_rescue_boats(people, limit)
  people.sort!
  i = 0
  j = people.length - 1
  boats = 0
  while i <= j
    if people[i] + people[j] <= limit
      i += 1
    end
    j -= 1
    boats += 1
  end
  boats
end
```

## Scala

```scala
object Solution {
    def numRescueBoats(people: Array[Int], limit: Int): Int = {
        java.util.Arrays.sort(people)
        var i = 0
        var j = people.length - 1
        var boats = 0
        while (i <= j) {
            if (people(i) + people(j) <= limit) i += 1
            j -= 1
            boats += 1
        }
        boats
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_rescue_boats(mut people: Vec<i32>, limit: i32) -> i32 {
        people.sort_unstable();
        let mut left = 0usize;
        let mut right = people.len().saturating_sub(1);
        let mut boats = 0i32;

        while left < right {
            if people[left] + people[right] <= limit {
                left += 1;
            }
            // always place the heaviest person
            right -= 1;
            boats += 1;
        }

        // If one person remains unpaired
        if left == right {
            boats += 1;
        }

        boats
    }
}
```

## Racket

```racket
(define/contract (num-rescue-boats people limit)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([sorted (sort people <)]
         [v (list->vector sorted)]
         [n (vector-length v)])
    (let loop ((i 0) (j (- n 1)) (boats 0))
      (if (> i j)
          boats
          (let ((sum (+ (vector-ref v i) (vector-ref v j))))
            (if (<= sum limit)
                (loop (+ i 1) (- j 1) (+ boats 1))
                (loop i (- j 1) (+ boats 1))))))))
```

## Erlang

```erlang
-module(solution).
-export([num_rescue_boats/2]).

-spec num_rescue_boats(People :: [integer()], Limit :: integer()) -> integer().
num_rescue_boats(People, Limit) ->
    Sorted = lists:sort(People),
    Len = length(Sorted),
    Arr = array:from_list(Sorted),
    count_boats(Arr, 0, Len - 1, Limit, 0).

count_boats(_Arr, L, R, _Limit, Acc) when L > R ->
    Acc;
count_boats(_Arr, L, R, _Limit, Acc) when L == R ->
    Acc + 1;
count_boats(Arr, L, R, Limit, Acc) ->
    Left = array:get(L, Arr),
    Right = array:get(R, Arr),
    if
        Left + Right =< Limit ->
            count_boats(Arr, L + 1, R - 1, Limit, Acc + 1);
        true ->
            count_boats(Arr, L, R - 1, Limit, Acc + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec num_rescue_boats(people :: [integer], limit :: integer) :: integer
  def num_rescue_boats(people, limit) do
    sorted = Enum.sort(people)
    arr = List.to_tuple(sorted)
    count(arr, limit, 0, tuple_size(arr) - 1, 0)
  end

  defp count(_, _, i, j, boats) when i > j, do: boats

  defp count(arr, limit, i, j, boats) do
    if i == j do
      boats + 1
    else
      if elem(arr, i) + elem(arr, j) <= limit do
        count(arr, limit, i + 1, j - 1, boats + 1)
      else
        count(arr, limit, i, j - 1, boats + 1)
      end
    end
  end
end
```
