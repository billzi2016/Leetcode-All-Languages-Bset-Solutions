# 1502. Can Make Arithmetic Progression From Sequence

## Cpp

```cpp
class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        if (arr.size() < 2) return true;
        sort(arr.begin(), arr.end());
        long long diff = static_cast<long long>(arr[1]) - arr[0];
        for (size_t i = 2; i < arr.size(); ++i) {
            if (static_cast<long long>(arr[i]) - arr[i-1] != diff)
                return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        java.util.Arrays.sort(arr);
        int diff = arr[1] - arr[0];
        for (int i = 2; i < arr.length; i++) {
            if (arr[i] - arr[i - 1] != diff) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) <= 2:
            return True
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return True
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

static int cmpInt(const void *a, const void *b) {
    int ai = *(const int *)a;
    int bi = *(const int *)b;
    return (ai > bi) - (ai < bi);
}

bool canMakeArithmeticProgression(int* arr, int arrSize) {
    if (arrSize <= 2) return true;
    qsort(arr, (size_t)arrSize, sizeof(int), cmpInt);
    int diff = arr[1] - arr[0];
    for (int i = 2; i < arrSize; ++i) {
        if (arr[i] - arr[i - 1] != diff) return false;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CanMakeArithmeticProgression(int[] arr) {
        System.Array.Sort(arr);
        int diff = arr[1] - arr[0];
        for (int i = 2; i < arr.Length; i++) {
            if (arr[i] - arr[i - 1] != diff) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var canMakeArithmeticProgression = function(arr) {
    if (arr.length <= 2) return true;
    arr.sort((a, b) => a - b);
    const diff = arr[1] - arr[0];
    for (let i = 2; i < arr.length; i++) {
        if (arr[i] - arr[i - 1] !== diff) return false;
    }
    return true;
};
```

## Typescript

```typescript
function canMakeArithmeticProgression(arr: number[]): boolean {
    if (arr.length <= 2) return true;
    arr.sort((a, b) => a - b);
    const diff = arr[1] - arr[0];
    for (let i = 2; i < arr.length; i++) {
        if (arr[i] - arr[i - 1] !== diff) {
            return false;
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function canMakeArithmeticProgression($arr) {
        sort($arr);
        $n = count($arr);
        if ($n < 2) {
            return true;
        }
        $diff = $arr[1] - $arr[0];
        for ($i = 2; $i < $n; $i++) {
            if ($arr[$i] - $arr[$i - 1] !== $diff) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func canMakeArithmeticProgression(_ arr: [Int]) -> Bool {
        let sortedArr = arr.sorted()
        guard sortedArr.count > 1 else { return true }
        let diff = sortedArr[1] - sortedArr[0]
        for i in 2..<sortedArr.count {
            if sortedArr[i] - sortedArr[i - 1] != diff {
                return false
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canMakeArithmeticProgression(arr: IntArray): Boolean {
        if (arr.size <= 2) return true
        arr.sort()
        val diff = arr[1] - arr[0]
        for (i in 2 until arr.size) {
            if (arr[i] - arr[i - 1] != diff) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool canMakeArithmeticProgression(List<int> arr) {
    if (arr.length <= 2) return true;
    arr.sort();
    int diff = arr[1] - arr[0];
    for (int i = 2; i < arr.length; i++) {
      if (arr[i] - arr[i - 1] != diff) return false;
    }
    return true;
  }
}
```

## Golang

```go
import "sort"

func canMakeArithmeticProgression(arr []int) bool {
	if len(arr) < 2 {
		return true
	}
	sort.Ints(arr)
	diff := arr[1] - arr[0]
	for i := 2; i < len(arr); i++ {
		if arr[i]-arr[i-1] != diff {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
# @param {Integer[]} arr
# @return {Boolean}
def can_make_arithmetic_progression(arr)
  return true if arr.length <= 2
  arr.sort!
  diff = arr[1] - arr[0]
  (2...arr.length).each do |i|
    return false unless arr[i] - arr[i - 1] == diff
  end
  true
end
```

## Scala

```scala
object Solution {
    def canMakeArithmeticProgression(arr: Array[Int]): Boolean = {
        if (arr.length <= 2) return true
        val sorted = arr.sorted
        val diff = sorted(1) - sorted(0)
        var i = 2
        while (i < sorted.length) {
            if (sorted(i) - sorted(i - 1) != diff) return false
            i += 1
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_make_arithmetic_progression(mut arr: Vec<i32>) -> bool {
        if arr.len() <= 2 {
            return true;
        }
        arr.sort_unstable();
        let diff = arr[1] - arr[0];
        for i in 2..arr.len() {
            if arr[i] - arr[i - 1] != diff {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (can-make-arithmetic-progression arr)
  (-> (listof exact-integer?) boolean?)
  (let* ((sorted (sort arr <))
         (n (length sorted)))
    (if (< n 2)
        #t
        (let ((diff (- (list-ref sorted 1) (list-ref sorted 0))))
          (let loop ((i 2))
            (if (= i n)
                #t
                (and (= (- (list-ref sorted i) (list-ref sorted (- i 1))) diff)
                     (loop (+ i 1)))))))))
```

## Erlang

```erlang
-module(solution).
-export([can_make_arithmetic_progression/1]).

-spec can_make_arithmetic_progression(Arr :: [integer()]) -> boolean().
can_make_arithmetic_progression(Arr) ->
    Sorted = lists:sort(Arr),
    case Sorted of
        [_] -> true;
        [_, _] -> true;
        [First, Second | Rest] ->
            Diff = Second - First,
            check(Rest, Second, Diff)
    end.

check([], _, _) -> true;
check([H|T], Prev, Diff) ->
    if
        H - Prev =:= Diff -> check(T, H, Diff);
        true -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_make_arithmetic_progression(arr :: [integer]) :: boolean
  def can_make_arithmetic_progression(arr) do
    sorted = Enum.sort(arr)
    diff = Enum.at(sorted, 1) - Enum.at(sorted, 0)
    len = length(sorted)

    Enum.reduce_while(2..len - 1, true, fn i, _acc ->
      if Enum.at(sorted, i) - Enum.at(sorted, i - 1) == diff do
        {:cont, true}
      else
        {:halt, false}
      end
    end)
  end
end
```
