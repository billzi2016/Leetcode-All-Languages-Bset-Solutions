# 2442. Count Number of Distinct Integers After Reverse Operations

## Cpp

```cpp
class Solution {
public:
    int countDistinctIntegers(vector<int>& nums) {
        unordered_set<int> s;
        s.reserve(nums.size() * 2);
        for (int x : nums) {
            s.insert(x);
            int rev = 0, t = x;
            while (t > 0) {
                rev = rev * 10 + t % 10;
                t /= 10;
            }
            s.insert(rev);
        }
        return static_cast<int>(s.size());
    }
};
```

## Java

```java
class Solution {
    public int countDistinctIntegers(int[] nums) {
        java.util.HashSet<Integer> set = new java.util.HashSet<>();
        for (int num : nums) {
            set.add(num);
            set.add(reverse(num));
        }
        return set.size();
    }

    private int reverse(int n) {
        int rev = 0;
        while (n > 0) {
            rev = rev * 10 + (n % 10);
            n /= 10;
        }
        return rev;
    }
}
```

## Python

```python
class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct = set()
        for num in nums:
            distinct.add(num)
            rev = int(str(num)[::-1])
            distinct.add(rev)
        return len(distinct)
```

## Python3

```python
from typing import List

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct = set()
        for num in nums:
            distinct.add(num)
            rev = 0
            x = num
            while x:
                rev = rev * 10 + x % 10
                x //= 10
            distinct.add(rev)
        return len(distinct)
```

## C

```c
int countDistinctIntegers(int* nums, int numsSize) {
    const int MAX_VAL = 1000000;
    char *seen = (char *)calloc(MAX_VAL + 1, sizeof(char));
    int distinct = 0;
    for (int i = 0; i < numsSize; ++i) {
        int v = nums[i];
        if (!seen[v]) {
            seen[v] = 1;
            ++distinct;
        }
        int x = v, rev = 0;
        while (x > 0) {
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        if (!seen[rev]) {
            seen[rev] = 1;
            ++distinct;
        }
    }
    free(seen);
    return distinct;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int CountDistinctIntegers(int[] nums) {
        HashSet<int> seen = new HashSet<int>();
        foreach (int num in nums) {
            seen.Add(num);
            seen.Add(Reverse(num));
        }
        return seen.Count;
    }

    private int Reverse(int x) {
        int rev = 0;
        while (x > 0) {
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        return rev;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countDistinctIntegers = function(nums) {
    const seen = new Set();
    
    const reverseNumber = (n) => {
        let rev = 0;
        while (n > 0) {
            rev = rev * 10 + (n % 10);
            n = Math.floor(n / 10);
        }
        return rev;
    };
    
    for (const num of nums) {
        seen.add(num);
        seen.add(reverseNumber(num));
    }
    
    return seen.size;
};
```

## Typescript

```typescript
function countDistinctIntegers(nums: number[]): number {
    const distinct = new Set<number>();
    for (const num of nums) {
        distinct.add(num);
        let rev = 0;
        let x = num;
        while (x > 0) {
            rev = rev * 10 + (x % 10);
            x = Math.floor(x / 10);
        }
        // handle the case when num is 0, though constraints say positive integers
        distinct.add(rev);
    }
    return distinct.size;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countDistinctIntegers($nums) {
        $unique = [];
        foreach ($nums as $num) {
            $unique[$num] = true;
            $rev = intval(strrev((string)$num));
            $unique[$rev] = true;
        }
        return count($unique);
    }
}
```

## Swift

```swift
class Solution {
    func countDistinctIntegers(_ nums: [Int]) -> Int {
        var distinct = Set<Int>()
        for num in nums {
            distinct.insert(num)
            var x = num
            var rev = 0
            while x > 0 {
                rev = rev * 10 + x % 10
                x /= 10
            }
            distinct.insert(rev)
        }
        return distinct.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countDistinctIntegers(nums: IntArray): Int {
        val distinct = HashSet<Int>()
        for (num in nums) {
            distinct.add(num)
            var x = num
            var rev = 0
            while (x > 0) {
                rev = rev * 10 + (x % 10)
                x /= 10
            }
            distinct.add(rev)
        }
        return distinct.size
    }
}
```

## Dart

```dart
class Solution {
  int countDistinctIntegers(List<int> nums) {
    final Set<int> distinct = {};
    for (var num in nums) {
      distinct.add(num);
      distinct.add(_reverse(num));
    }
    return distinct.length;
  }

  int _reverse(int x) {
    int rev = 0;
    while (x > 0) {
      rev = rev * 10 + x % 10;
      x ~/= 10;
    }
    return rev;
  }
}
```

## Golang

```go
func reverseNum(x int) int {
	rev := 0
	for x > 0 {
		rev = rev*10 + x%10
		x /= 10
	}
	return rev
}

func countDistinctIntegers(nums []int) int {
	set := make(map[int]struct{}, len(nums)*2)
	for _, v := range nums {
		set[v] = struct{}{}
		set[reverseNum(v)] = struct{}{}
	}
	return len(set)
}
```

## Ruby

```ruby
require 'set'

# @param {Integer[]} nums
# @return {Integer}
def count_distinct_integers(nums)
  distinct = Set.new
  nums.each do |num|
    distinct.add(num)
    reversed_num = num.to_s.reverse.to_i
    distinct.add(reversed_num)
  end
  distinct.size
end
```

## Scala

```scala
object Solution {
    def countDistinctIntegers(nums: Array[Int]): Int = {
        val seen = scala.collection.mutable.HashSet[Int]()
        def reverse(num: Int): Int = {
            var n = num
            var rev = 0
            while (n > 0) {
                rev = rev * 10 + n % 10
                n /= 10
            }
            rev
        }
        for (num <- nums) {
            seen += num
            seen += reverse(num)
        }
        seen.size
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_distinct_integers(nums: Vec<i32>) -> i32 {
        use std::collections::HashSet;
        let mut set = HashSet::with_capacity(nums.len() * 2);
        for &num in nums.iter() {
            set.insert(num);
            set.insert(Self::reverse(num));
        }
        set.len() as i32
    }

    fn reverse(mut n: i32) -> i32 {
        let mut rev = 0;
        while n > 0 {
            rev = rev * 10 + n % 10;
            n /= 10;
        }
        rev
    }
}
```

## Racket

```racket
#lang racket
(require racket/string)
(require racket/set)

(define (reverse-int n)
  (string->number
   (list->string (reverse (string->list (number->string n))))))

(define/contract (count-distinct-integers nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((lst nums) (s (set)))
    (if (null? lst)
        (set-count s)
        (let* ((x (car lst))
               (rev (reverse-int x))
               (new-s (set-add (set-add s x) rev)))
          (loop (cdr lst) new-s)))))
```

## Erlang

```erlang
-module(solution).
-export([count_distinct_integers/1]).

-spec count_distinct_integers(Nums :: [integer()]) -> integer().
count_distinct_integers(Nums) ->
    Set = lists:foldl(fun(N, Acc) ->
        Rev = reverse_int(N),
        maps:put(N, true, maps:put(Rev, true, Acc))
    end, #{}, Nums),
    map_size(Set).

reverse_int(N) -> rev(N, 0).
rev(0, Acc) -> Acc;
rev(N, Acc) ->
    Digit = N rem 10,
    rev(N div 10, Acc * 10 + Digit).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_distinct_integers(nums :: [integer]) :: integer
  def count_distinct_integers(nums) do
    set =
      Enum.reduce(nums, MapSet.new(), fn num, acc ->
        rev = reverse_int(num)
        acc |> MapSet.put(num) |> MapSet.put(rev)
      end)

    MapSet.size(set)
  end

  defp reverse_int(n) when n >= 0 do
    do_reverse(n, 0)
  end

  defp do_reverse(0, rev), do: rev
  defp do_reverse(num, rev) do
    do_reverse(div(num, 10), rev * 10 + rem(num, 10))
  end
end
```
