# 1460. Make Two Arrays Equal by Reversing Subarrays

## Cpp

```cpp
class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        sort(target.begin(), target.end());
        sort(arr.begin(), arr.end());
        return target == arr;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        Arrays.sort(target);
        Arrays.sort(arr);
        return Arrays.equals(target, arr);
    }
}
```

## Python

```python
class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        return sorted(target) == sorted(arr)
```

## Python3

```python
from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static int cmpInt(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

bool canBeEqual(int* target, int targetSize, int* arr, int arrSize) {
    if (targetSize != arrSize) return false;

    int *t = (int *)malloc(sizeof(int) * targetSize);
    int *a = (int *)malloc(sizeof(int) * arrSize);
    if (!t || !a) {
        free(t);
        free(a);
        return false;
    }

    for (int i = 0; i < targetSize; ++i) t[i] = target[i];
    for (int i = 0; i < arrSize; ++i) a[i] = arr[i];

    qsort(t, targetSize, sizeof(int), cmpInt);
    qsort(a, arrSize,   sizeof(int), cmpInt);

    bool equal = true;
    for (int i = 0; i < targetSize; ++i) {
        if (t[i] != a[i]) {
            equal = false;
            break;
        }
    }

    free(t);
    free(a);
    return equal;
}
```

## Csharp

```csharp
public class Solution {
    public bool CanBeEqual(int[] target, int[] arr) {
        System.Array.Sort(target);
        System.Array.Sort(arr);
        for (int i = 0; i < target.Length; i++) {
            if (target[i] != arr[i]) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} target
 * @param {number[]} arr
 * @return {boolean}
 */
var canBeEqual = function(target, arr) {
    if (target.length !== arr.length) return false;
    target.sort((a, b) => a - b);
    arr.sort((a, b) => a - b);
    for (let i = 0; i < target.length; i++) {
        if (target[i] !== arr[i]) return false;
    }
    return true;
};
```

## Typescript

```typescript
function canBeEqual(target: number[], arr: number[]): boolean {
    if (target.length !== arr.length) return false;
    target.sort((a, b) => a - b);
    arr.sort((a, b) => a - b);
    for (let i = 0; i < target.length; i++) {
        if (target[i] !== arr[i]) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $target
     * @param Integer[] $arr
     * @return Boolean
     */
    function canBeEqual($target, $arr) {
        sort($target);
        sort($arr);
        return $target == $arr;
    }
}
```

## Swift

```swift
class Solution {
    func canBeEqual(_ target: [Int], _ arr: [Int]) -> Bool {
        return target.sorted() == arr.sorted()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canBeEqual(target: IntArray, arr: IntArray): Boolean {
        target.sort()
        arr.sort()
        return target.contentEquals(arr)
    }
}
```

## Dart

```dart
class Solution {
  bool canBeEqual(List<int> target, List<int> arr) {
    if (target.length != arr.length) return false;
    var t = List<int>.from(target);
    var a = List<int>.from(arr);
    t.sort();
    a.sort();
    for (int i = 0; i < t.length; i++) {
      if (t[i] != a[i]) return false;
    }
    return true;
  }
}
```

## Golang

```go
package main

import "sort"

func canBeEqual(target []int, arr []int) bool {
	if len(target) != len(arr) {
		return false
	}
	sort.Ints(target)
	sort.Ints(arr)
	for i := range target {
		if target[i] != arr[i] {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
# @param {Integer[]} target
# @param {Integer[]} arr
# @return {Boolean}
def can_be_equal(target, arr)
  target.sort == arr.sort
end
```

## Scala

```scala
object Solution {
  def canBeEqual(target: Array[Int], arr: Array[Int]): Boolean = {
    val t = target.clone()
    java.util.Arrays.sort(t)
    val a = arr.clone()
    java.util.Arrays.sort(a)
    java.util.Arrays.equals(t, a)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn can_be_equal(mut target: Vec<i32>, mut arr: Vec<i32>) -> bool {
        target.sort_unstable();
        arr.sort_unstable();
        target == arr
    }
}
```

## Racket

```racket
(define/contract (can-be-equal target arr)
  (-> (listof exact-integer?) (listof exact-integer?) boolean?)
  (let ([sorted-target (sort target <)]
        [sorted-arr    (sort arr <)])
    (equal? sorted-target sorted-arr)))
```

## Erlang

```erlang
-spec can_be_equal(Target :: [integer()], Arr :: [integer()]) -> boolean().
can_be_equal(Target, Arr) ->
    lists:sort(Target) =:= lists:sort(Arr).
```

## Elixir

```elixir
defmodule Solution do
  @spec can_be_equal(target :: [integer], arr :: [integer]) :: boolean
  def can_be_equal(target, arr) do
    Enum.sort(target) == Enum.sort(arr)
  end
end
```
