# 0217. Contains Duplicate

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int x : nums) {
            if (!seen.insert(x).second) return true;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        java.util.HashSet<Integer> seen = new java.util.HashSet<>(nums.length);
        for (int num : nums) {
            if (!seen.add(num)) {
                return true;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

## Python3

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
}

bool containsDuplicate(int* nums, int numsSize) {
    if (numsSize <= 1) return false;
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    for (int i = 1; i < numsSize; ++i) {
        if (nums[i] == nums[i - 1]) return true;
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        var seen = new HashSet<int>();
        foreach (int num in nums) {
            if (!seen.Add(num)) return true;
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const seen = new Set();
    for (const num of nums) {
        if (seen.has(num)) return true;
        seen.add(num);
    }
    return false;
};
```

## Typescript

```typescript
function containsDuplicate(nums: number[]): boolean {
    const seen = new Set<number>();
    for (const num of nums) {
        if (seen.has(num)) return true;
        seen.add(num);
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function containsDuplicate($nums) {
        $seen = [];
        foreach ($nums as $num) {
            if (isset($seen[$num])) {
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
    func containsDuplicate(_ nums: [Int]) -> Bool {
        var seen = Set<Int>()
        for num in nums {
            if seen.contains(num) {
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
    fun containsDuplicate(nums: IntArray): Boolean {
        val seen = HashSet<Int>()
        for (num in nums) {
            if (!seen.add(num)) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool containsDuplicate(List<int> nums) {
    final seen = <int>{};
    for (var num in nums) {
      if (seen.contains(num)) return true;
      seen.add(num);
    }
    return false;
  }
}
```

## Golang

```go
func containsDuplicate(nums []int) bool {
	seen := make(map[int]struct{}, len(nums))
	for _, v := range nums {
		if _, ok := seen[v]; ok {
			return true
		}
		seen[v] = struct{}{}
	}
	return false
}
```

## Ruby

```ruby
def contains_duplicate(nums)
  seen = {}
  nums.each do |num|
    return true if seen.key?(num)
    seen[num] = true
  end
  false
end
```

## Scala

```scala
object Solution {
    def containsDuplicate(nums: Array[Int]): Boolean = {
        val seen = scala.collection.mutable.HashSet[Int]()
        for (num <- nums) {
            if (!seen.add(num)) return true
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        use std::collections::HashSet;
        let mut seen = HashSet::with_capacity(nums.len());
        for v in nums {
            if !seen.insert(v) {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (contains-duplicate nums)
  (-> (listof exact-integer?) boolean?)
  (let loop ((lst nums) (seen (make-hash)))
    (cond
      [(null? lst) #f]
      [else
       (let ((x (car lst)))
         (if (hash-has-key? seen x)
             #t
             (begin
               (hash-set! seen x #t)
               (loop (cdr lst) seen))))])))
```

## Erlang

```erlang
-module(solution).
-export([contains_duplicate/1]).

-spec contains_duplicate(Nums :: [integer()]) -> boolean().
contains_duplicate(Nums) ->
    contains_duplicate(Nums, #{}).

contains_duplicate([], _) -> false;
contains_duplicate([H|T], Seen) ->
    case maps:is_key(H, Seen) of
        true -> true;
        false -> contains_duplicate(T, maps:put(H, true, Seen))
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec contains_duplicate(nums :: [integer]) :: boolean
  def contains_duplicate(nums) do
    Enum.uniq(nums) |> length() != length(nums)
  end
end
```
