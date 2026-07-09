# 1346. Check If N and Its Double Exist

## Cpp

```cpp
class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_set<int> seen;
        for (int num : arr) {
            if (seen.count(num * 2) || (num % 2 == 0 && seen.count(num / 2))) {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean checkIfExist(int[] arr) {
        java.util.HashSet<Integer> seen = new java.util.HashSet<>();
        for (int num : arr) {
            if (seen.contains(num * 2) || (num % 2 == 0 && seen.contains(num / 2))) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
        for num in arr:
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False
```

## Python3

```python
from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False
```

## C

```c
#include <stdbool.h>

bool checkIfExist(int* arr, int arrSize) {
    const int OFFSET = 1000;
    char seen[2001] = {0};
    
    for (int i = 0; i < arrSize; ++i) {
        int num = arr[i];
        
        int doubleVal = num * 2;
        if (doubleVal >= -1000 && doubleVal <= 1000) {
            if (seen[doubleVal + OFFSET]) return true;
        }
        
        if ((num & 1) == 0) { // even number
            int half = num / 2;
            if (half >= -1000 && half <= 1000) {
                if (seen[half + OFFSET]) return true;
            }
        }
        
        seen[num + OFFSET] = 1;
    }
    
    return false;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CheckIfExist(int[] arr)
    {
        var seen = new HashSet<int>();
        foreach (int num in arr)
        {
            if (seen.Contains(2 * num) || (num % 2 == 0 && seen.Contains(num / 2)))
                return true;
            seen.Add(num);
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var checkIfExist = function(arr) {
    const seen = new Set();
    for (const num of arr) {
        if (seen.has(2 * num) || (num % 2 === 0 && seen.has(num / 2))) {
            return true;
        }
        seen.add(num);
    }
    return false;
};
```

## Typescript

```typescript
function checkIfExist(arr: number[]): boolean {
    const seen = new Set<number>();
    for (const num of arr) {
        if (seen.has(num * 2) || (num % 2 === 0 && seen.has(num / 2))) {
            return true;
        }
        seen.add(num);
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function checkIfExist($arr) {
        $seen = [];
        foreach ($arr as $num) {
            // Check if double of current number has been seen before
            if (isset($seen[$num * 2])) {
                return true;
            }
            // If current number is even, check if its half has been seen before
            if ($num % 2 === 0 && isset($seen[intdiv($num, 2)])) {
                return true;
            }
            $seen[$num] = true;
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func checkIfExist(_ arr: [Int]) -> Bool {
        var seen = Set<Int>()
        for num in arr {
            if seen.contains(num * 2) || (num % 2 == 0 && seen.contains(num / 2)) {
                return true
            }
            seen.insert(num)
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkIfExist(arr: IntArray): Boolean {
        val seen = HashSet<Int>()
        for (num in arr) {
            if (seen.contains(num * 2) || (num % 2 == 0 && seen.contains(num / 2))) {
                return true
            }
            seen.add(num)
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool checkIfExist(List<int> arr) {
    final Set<int> seen = {};
    for (final int num in arr) {
      if (seen.contains(2 * num)) return true;
      if (num % 2 == 0 && seen.contains(num ~/ 2)) return true;
      seen.add(num);
    }
    return false;
  }
}
```

## Golang

```go
func checkIfExist(arr []int) bool {
	seen := make(map[int]struct{})
	for _, v := range arr {
		if _, ok := seen[2*v]; ok {
			return true
		}
		if v%2 == 0 {
			if _, ok := seen[v/2]; ok {
				return true
			}
		}
		seen[v] = struct{}{}
	}
	return false
}
```

## Ruby

```ruby
def check_if_exist(arr)
  seen = {}
  arr.each do |num|
    return true if seen[2 * num]
    return true if num.even? && seen[num / 2]
    seen[num] = true
  end
  false
end
```

## Scala

```scala
object Solution {
    def checkIfExist(arr: Array[Int]): Boolean = {
        val seen = scala.collection.mutable.HashSet[Int]()
        for (num <- arr) {
            if (seen.contains(num * 2) || (num % 2 == 0 && seen.contains(num / 2))) return true
            seen.add(num)
        }
        false
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn check_if_exist(arr: Vec<i32>) -> bool {
        let mut seen = HashSet::new();
        for &num in arr.iter() {
            if seen.contains(&(2 * num)) {
                return true;
            }
            if num % 2 == 0 && seen.contains(&(num / 2)) {
                return true;
            }
            seen.insert(num);
        }
        false
    }
}
```

## Racket

```racket
(define/contract (check-if-exist arr)
  (-> (listof exact-integer?) boolean?)
  (let ((seen (make-hash)))
    (let loop ((lst arr))
      (cond
        [(null? lst) #false]
        [else
         (let ((num (car lst)))
           (if (or (hash-has-key? seen (* 2 num))
                   (and (even? num) (hash-has-key? seen (/ num 2))))
               #true
               (begin
                 (hash-set! seen num #t)
                 (loop (cdr lst)))))]))))
```

## Erlang

```erlang
-module(solution).
-export([check_if_exist/1]).

-spec check_if_exist(Arr :: [integer()]) -> boolean().
check_if_exist(Arr) ->
    check_if_exist(Arr, #{}).

check_if_exist([], _Seen) ->
    false;
check_if_exist([H|T], Seen) ->
    Double = H * 2,
    HalfCond = (H rem 2 =:= 0),
    case maps:is_key(Double, Seen) orelse (HalfCond andalso maps:is_key(H div 2, Seen)) of
        true -> true;
        false -> check_if_exist(T, Seen#{H => true})
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_if_exist(arr :: [integer]) :: boolean
  def check_if_exist(arr) do
    result =
      Enum.reduce_while(arr, MapSet.new(), fn num, seen ->
        cond do
          MapSet.member?(seen, num * 2) ->
            {:halt, true}

          rem(num, 2) == 0 and MapSet.member?(seen, div(num, 2)) ->
            {:halt, true}

          true ->
            {:cont, MapSet.put(seen, num)}
        end
      end)

    case result do
      true -> true
      _ -> false
    end
  end
end
```
