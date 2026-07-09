# 3162. Find the Number of Good Pairs I

## Cpp

```cpp
class Solution {
public:
    int numberOfPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        int cnt = 0;
        for (int a : nums1) {
            for (int b : nums2) {
                long long divisor = 1LL * b * k;
                if (divisor != 0 && a % divisor == 0) ++cnt;
            }
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int numberOfPairs(int[] nums1, int[] nums2, int k) {
        int count = 0;
        for (int a : nums1) {
            for (int b : nums2) {
                long divisor = (long) b * k;
                if (divisor != 0 && a % divisor == 0) {
                    count++;
                }
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for a in nums1:
            for b in nums2:
                if a % (b * k) == 0:
                    count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0
        for a in nums1:
            for b in nums2:
                if a % (b * k) == 0:
                    count += 1
        return count
```

## C

```c
int numberOfPairs(int* nums1, int nums1Size, int* nums2, int nums2Size, int k) {
    int count = 0;
    for (int i = 0; i < nums1Size; ++i) {
        for (int j = 0; j < nums2Size; ++j) {
            long long divisor = (long long)nums2[j] * k;
            if (divisor != 0 && nums1[i] % divisor == 0) {
                ++count;
            }
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfPairs(int[] nums1, int[] nums2, int k) {
        int count = 0;
        foreach (int a in nums1) {
            foreach (int b in nums2) {
                int divisor = b * k;
                if (divisor != 0 && a % divisor == 0) {
                    count++;
                }
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
var numberOfPairs = function(nums1, nums2, k) {
    let count = 0;
    for (let i = 0; i < nums1.length; i++) {
        for (let j = 0; j < nums2.length; j++) {
            const divisor = nums2[j] * k;
            if (divisor !== 0 && nums1[i] % divisor === 0) {
                count++;
            }
        }
    }
    return count;
};
```

## Typescript

```typescript
function numberOfPairs(nums1: number[], nums2: number[], k: number): number {
    let count = 0;
    for (let i = 0; i < nums1.length; i++) {
        const a = nums1[i];
        for (let j = 0; j < nums2.length; j++) {
            const divisor = nums2[j] * k;
            if (a % divisor === 0) {
                count++;
            }
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer
     */
    function numberOfPairs($nums1, $nums2, $k) {
        $count = 0;
        foreach ($nums1 as $a) {
            foreach ($nums2 as $b) {
                $divisor = $b * $k;
                if ($divisor != 0 && $a % $divisor == 0) {
                    $count++;
                }
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfPairs(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        var count = 0
        for a in nums1 {
            for b in nums2 {
                let divisor = b * k
                if a % divisor == 0 {
                    count += 1
                }
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfPairs(nums1: IntArray, nums2: IntArray, k: Int): Int {
        var count = 0
        for (a in nums1) {
            for (b in nums2) {
                val divisor = b * k
                if (a % divisor == 0) {
                    count++
                }
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int numberOfPairs(List<int> nums1, List<int> nums2, int k) {
    int count = 0;
    for (int a in nums1) {
      for (int b in nums2) {
        if (a % (b * k) == 0) {
          count++;
        }
      }
    }
    return count;
  }
}
```

## Golang

```go
func numberOfPairs(nums1 []int, nums2 []int, k int) int {
    count := 0
    for _, a := range nums1 {
        for _, b := range nums2 {
            divisor := b * k
            if a%divisor == 0 {
                count++
            }
        }
    }
    return count
}
```

## Ruby

```ruby
def number_of_pairs(nums1, nums2, k)
  count = 0
  nums1.each do |a|
    nums2.each do |b|
      count += 1 if a % (b * k) == 0
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def numberOfPairs(nums1: Array[Int], nums2: Array[Int], k: Int): Int = {
        var count = 0
        for (a <- nums1) {
            for (b <- nums2) {
                if (a % (b * k) == 0) count += 1
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i32 {
        let mut count = 0;
        for &a in &nums1 {
            for &b in &nums2 {
                let divisor = b * k;
                if a % divisor == 0 {
                    count += 1;
                }
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (number-of-pairs nums1 nums2 k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (for/sum ([a nums1] [b nums2])
    (if (= (modulo a (* b k)) 0) 1 0)))
```

## Erlang

```erlang
-spec number_of_pairs(Nums1 :: [integer()], Nums2 :: [integer()], K :: integer()) -> integer().
number_of_pairs(Nums1, Nums2, K) ->
    length([1 || A <- Nums1, B <- Nums2, (A rem (B * K)) =:= 0]).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_pairs(nums1 :: [integer], nums2 :: [integer], k :: integer) :: integer
  def number_of_pairs(nums1, nums2, k) do
    Enum.reduce(nums1, 0, fn a, acc ->
      cnt = Enum.count(nums2, fn b -> rem(a, b * k) == 0 end)
      acc + cnt
    end)
  end
end
```
