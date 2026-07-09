# 0330. Patching Array

## Cpp

```cpp
class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        long long miss = 1;
        int i = 0, patches = 0;
        const int sz = nums.size();
        while (miss <= n) {
            if (i < sz && nums[i] <= miss) {
                miss += nums[i];
                ++i;
            } else {
                ++patches;
                miss <<= 1; // same as miss *= 2
            }
        }
        return patches;
    }
};
```

## Java

```java
class Solution {
    public int minPatches(int[] nums, int n) {
        long miss = 1;
        long target = n;
        int i = 0, patches = 0;
        while (miss <= target) {
            if (i < nums.length && nums[i] <= miss) {
                miss += nums[i];
                i++;
            } else {
                miss <<= 1; // add patch equal to current miss
                patches++;
            }
        }
        return patches;
    }
}
```

## Python

```python
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss = 1
        i = 0
        patches = 0
        length = len(nums)
        while miss <= n:
            if i < length and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                # patch with miss
                miss <<= 1  # equivalent to miss *= 2
                patches += 1
        return patches
```

## Python3

```python
from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        i = 0
        patches = 0
        length = len(nums)
        while miss <= n:
            if i < length and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                # patch with miss
                miss <<= 1  # equivalent to miss *= 2
                patches += 1
        return patches
```

## C

```c
int minPatches(int* nums, int numsSize, int n) {
    long long miss = 1;
    long long target = (long long)n;
    int patches = 0;
    int i = 0;
    while (miss <= target) {
        if (i < numsSize && (long long)nums[i] <= miss) {
            miss += nums[i];
            i++;
        } else {
            miss <<= 1; // add patch equal to miss
            patches++;
        }
    }
    return patches;
}
```

## Csharp

```csharp
public class Solution {
    public int MinPatches(int[] nums, int n) {
        long miss = 1;
        int i = 0;
        int patches = 0;
        long target = n;
        
        while (miss <= target) {
            if (i < nums.Length && nums[i] <= miss) {
                miss += nums[i];
                i++;
            } else {
                miss <<= 1; // equivalent to miss *= 2
                patches++;
            }
        }
        
        return patches;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number}
 */
var minPatches = function(nums, n) {
    let miss = 1; // smallest sum we cannot form yet
    let patches = 0;
    let i = 0;
    const len = nums.length;
    
    while (miss <= n) {
        if (i < len && nums[i] <= miss) {
            miss += nums[i];
            i++;
        } else {
            // patch with miss
            miss <<= 1; // equivalent to miss *= 2, but faster
            patches++;
        }
    }
    
    return patches;
};
```

## Typescript

```typescript
function minPatches(nums: number[], n: number): number {
    let miss = 1;
    let i = 0;
    let patches = 0;
    const len = nums.length;
    while (miss <= n) {
        if (i < len && nums[i] <= miss) {
            miss += nums[i];
            i++;
        } else {
            miss += miss;
            patches++;
        }
    }
    return patches;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $n
     * @return Integer
     */
    function minPatches($nums, $n) {
        $miss = 1;          // smallest value that cannot be formed yet
        $i = 0;
        $patches = 0;
        $len = count($nums);
        while ($miss <= $n) {
            if ($i < $len && $nums[$i] <= $miss) {
                $miss += $nums[$i];
                $i++;
            } else {
                // add a patch equal to miss
                $miss += $miss;
                $patches++;
            }
        }
        return $patches;
    }
}
```

## Swift

```swift
class Solution {
    func minPatches(_ nums: [Int], _ n: Int) -> Int {
        var miss: Int64 = 1
        let target = Int64(n)
        var i = 0
        var patches = 0
        
        while miss <= target {
            if i < nums.count && Int64(nums[i]) <= miss {
                miss += Int64(nums[i])
                i += 1
            } else {
                // Patch with miss
                miss <<= 1
                patches += 1
            }
        }
        
        return patches
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minPatches(nums: IntArray, n: Int): Int {
        var patches = 0
        var miss: Long = 1L
        val target = n.toLong()
        var i = 0
        while (miss <= target) {
            if (i < nums.size && nums[i].toLong() <= miss) {
                miss += nums[i]
                i++
            } else {
                miss += miss
                patches++
            }
        }
        return patches
    }
}
```

## Dart

```dart
class Solution {
  int minPatches(List<int> nums, int n) {
    int patches = 0;
    int i = 0;
    // miss is the smallest value that cannot be formed yet
    int miss = 1;
    while (miss <= n) {
      if (i < nums.length && nums[i] <= miss) {
        miss += nums[i];
        i++;
      } else {
        // add a patch equal to miss
        miss <<= 1; // same as miss *= 2, but faster
        patches++;
      }
    }
    return patches;
  }
}
```

## Golang

```go
func minPatches(nums []int, n int) int {
	miss := int64(1)
	target := int64(n)
	patches := 0
	i := 0
	for miss <= target {
		if i < len(nums) && int64(nums[i]) <= miss {
			miss += int64(nums[i])
			i++
		} else {
			miss <<= 1
			patches++
		}
	}
	return patches
}
```

## Ruby

```ruby
def min_patches(nums, n)
  miss = 1
  i = 0
  patches = 0
  while miss <= n
    if i < nums.length && nums[i] <= miss
      miss += nums[i]
      i += 1
    else
      miss <<= 1
      patches += 1
    end
  end
  patches
end
```

## Scala

```scala
object Solution {
    def minPatches(nums: Array[Int], n: Int): Int = {
        var patches = 0
        var miss: Long = 1L
        val target: Long = n.toLong
        var i = 0
        while (miss <= target) {
            if (i < nums.length && nums(i).toLong <= miss) {
                miss += nums(i).toLong
                i += 1
            } else {
                // patch with miss
                miss <<= 1 // equivalent to miss *= 2
                patches += 1
            }
        }
        patches
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_patches(nums: Vec<i32>, n: i32) -> i32 {
        let mut miss: u64 = 1;
        let target: u64 = n as u64;
        let mut patches = 0i32;
        let mut i = 0usize;

        while miss <= target {
            if i < nums.len() && (nums[i] as u64) <= miss {
                miss += nums[i] as u64;
                i += 1;
            } else {
                // add a patch of value 'miss'
                miss <<= 1; // equivalent to miss *= 2
                patches += 1;
            }
        }

        patches
    }
}
```

## Racket

```racket
(define/contract (min-patches nums n)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let loop ((lst nums) (miss 1) (patches 0))
    (if (> miss n)
        patches
        (cond
          [(and (pair? lst) (<= (car lst) miss))
           (loop (cdr lst) (+ miss (car lst)) patches)]
          [else
           (loop lst (* 2 miss) (+ patches 1))]))))
```

## Erlang

```erlang
-spec min_patches(Nums :: [integer()], N :: integer()) -> integer().
min_patches(Nums, N) ->
    go(lists:sort(Nums), N, 1, 0).

go(_Nums, _N, Miss, Count) when Miss > _N ->
    Count;
go([], N, Miss, Count) ->
    go([], N, Miss * 2, Count + 1);
go([H|T]=Rest, N, Miss, Count) when H =< Miss ->
    go(T, N, Miss + H, Count);
go(Rest, N, Miss, Count) ->
    %% Here the head of Rest is greater than Miss
    go(Rest, N, Miss * 2, Count + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_patches(nums :: [integer], n :: integer) :: integer
  def min_patches(nums, n) do
    helper(nums, 1, n, 0)
  end

  defp helper(_nums, miss, n, patches) when miss > n,
    do: patches

  defp helper([], miss, n, patches) do
    helper([], miss * 2, n, patches + 1)
  end

  defp helper([h | t] = list, miss, n, patches) do
    if h <= miss do
      helper(t, miss + h, n, patches)
    else
      helper(list, miss * 2, n, patches + 1)
    end
  end
end
```
