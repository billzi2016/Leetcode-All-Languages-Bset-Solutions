# 2956. Find Common Elements Between Two Arrays

## Cpp

```cpp
class Solution {
public:
    vector<int> findIntersectionValues(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1(nums1.begin(), nums1.end());
        unordered_set<int> set2(nums2.begin(), nums2.end());
        
        int answer1 = 0;
        for (int x : nums1) {
            if (set2.count(x)) ++answer1;
        }
        
        int answer2 = 0;
        for (int x : nums2) {
            if (set1.count(x)) ++answer2;
        }
        
        return {answer1, answer2};
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int[] findIntersectionValues(int[] nums1, int[] nums2) {
        boolean[] present = new boolean[101];
        for (int v : nums2) {
            present[v] = true;
        }
        int ans1 = 0;
        for (int v : nums1) {
            if (present[v]) ans1++;
        }

        Arrays.fill(present, false);
        for (int v : nums1) {
            present[v] = true;
        }
        int ans2 = 0;
        for (int v : nums2) {
            if (present[v]) ans2++;
        }

        return new int[]{ans1, ans2};
    }
}
```

## Python

```python
class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set2 = set(nums2)
        set1 = set(nums1)
        ans1 = sum(1 for x in nums1 if x in set2)
        ans2 = sum(1 for x in nums2 if x in set1)
        return [ans1, ans2]
```

## Python3

```python
from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set2 = set(nums2)
        cnt1 = sum(1 for x in nums1 if x in set2)

        set1 = set(nums1)
        cnt2 = sum(1 for x in nums2 if x in set1)

        return [cnt1, cnt2]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findIntersectionValues(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    *returnSize = 2;
    int *result = (int *)malloc(2 * sizeof(int));
    
    int present1[101] = {0};
    int present2[101] = {0};
    
    for (int i = 0; i < nums1Size; ++i) {
        present1[nums1[i]] = 1;
    }
    for (int i = 0; i < nums2Size; ++i) {
        present2[nums2[i]] = 1;
    }
    
    int ans1 = 0, ans2 = 0;
    for (int i = 0; i < nums1Size; ++i) {
        if (present2[nums1[i]]) ++ans1;
    }
    for (int i = 0; i < nums2Size; ++i) {
        if (present1[nums2[i]]) ++ans2;
    }
    
    result[0] = ans1;
    result[1] = ans2;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] FindIntersectionValues(int[] nums1, int[] nums2) {
        bool[] presentInNums2 = new bool[101];
        foreach (int num in nums2) {
            if (num >= 0 && num <= 100) presentInNums2[num] = true;
        }
        int answer1 = 0;
        foreach (int num in nums1) {
            if (num >= 0 && num <= 100 && presentInNums2[num]) answer1++;
        }

        bool[] presentInNums1 = new bool[101];
        foreach (int num in nums1) {
            if (num >= 0 && num <= 100) presentInNums1[num] = true;
        }
        int answer2 = 0;
        foreach (int num in nums2) {
            if (num >= 0 && num <= 100 && presentInNums1[num]) answer2++;
        }

        return new int[] { answer1, answer2 };
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var findIntersectionValues = function(nums1, nums2) {
    const set2 = new Set(nums2);
    const set1 = new Set(nums1);
    
    let answer1 = 0;
    for (const num of nums1) {
        if (set2.has(num)) answer1++;
    }
    
    let answer2 = 0;
    for (const num of nums2) {
        if (set1.has(num)) answer2++;
    }
    
    return [answer1, answer2];
};
```

## Typescript

```typescript
function findIntersectionValues(nums1: number[], nums2: number[]): number[] {
    const set2 = new Set(nums2);
    let answer1 = 0;
    for (const v of nums1) {
        if (set2.has(v)) answer1++;
    }
    const set1 = new Set(nums1);
    let answer2 = 0;
    for (const v of nums2) {
        if (set1.has(v)) answer2++;
    }
    return [answer1, answer2];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[]
     */
    function findIntersectionValues($nums1, $nums2) {
        // Build hash sets for quick existence checks
        $set1 = [];
        foreach ($nums1 as $v) {
            $set1[$v] = true;
        }
        $set2 = [];
        foreach ($nums2 as $v) {
            $set2[$v] = true;
        }

        // Count elements in nums1 that appear in nums2
        $answer1 = 0;
        foreach ($nums1 as $v) {
            if (isset($set2[$v])) {
                $answer1++;
            }
        }

        // Count elements in nums2 that appear in nums1
        $answer2 = 0;
        foreach ($nums2 as $v) {
            if (isset($set1[$v])) {
                $answer2++;
            }
        }

        return [$answer1, $answer2];
    }
}
```

## Swift

```swift
class Solution {
    func findIntersectionValues(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        let set2 = Set(nums2)
        var answer1 = 0
        for v in nums1 {
            if set2.contains(v) {
                answer1 += 1
            }
        }
        
        let set1 = Set(nums1)
        var answer2 = 0
        for v in nums2 {
            if set1.contains(v) {
                answer2 += 1
            }
        }
        
        return [answer1, answer2]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findIntersectionValues(nums1: IntArray, nums2: IntArray): IntArray {
        val set1 = nums1.toHashSet()
        val set2 = nums2.toHashSet()
        var answer1 = 0
        for (v in nums1) {
            if (set2.contains(v)) answer1++
        }
        var answer2 = 0
        for (v in nums2) {
            if (set1.contains(v)) answer2++
        }
        return intArrayOf(answer1, answer2)
    }
}
```

## Dart

```dart
class Solution {
  List<int> findIntersectionValues(List<int> nums1, List<int> nums2) {
    final set2 = nums2.toSet();
    int answer1 = 0;
    for (var v in nums1) {
      if (set2.contains(v)) answer1++;
    }

    final set1 = nums1.toSet();
    int answer2 = 0;
    for (var v in nums2) {
      if (set1.contains(v)) answer2++;
    }

    return [answer1, answer2];
  }
}
```

## Golang

```go
func findIntersectionValues(nums1 []int, nums2 []int) []int {
	set2 := make(map[int]struct{}, len(nums2))
	for _, v := range nums2 {
		set2[v] = struct{}{}
	}
	ans1 := 0
	for _, v := range nums1 {
		if _, ok := set2[v]; ok {
			ans1++
		}
	}

	set1 := make(map[int]struct{}, len(nums1))
	for _, v := range nums1 {
		set1[v] = struct{}{}
	}
	ans2 := 0
	for _, v := range nums2 {
		if _, ok := set1[v]; ok {
			ans2++
		}
	}

	return []int{ans1, ans2}
}
```

## Ruby

```ruby
require 'set'

def find_intersection_values(nums1, nums2)
  set1 = nums1.to_set
  set2 = nums2.to_set
  count1 = nums1.count { |v| set2.include?(v) }
  count2 = nums2.count { |v| set1.include?(v) }
  [count1, count2]
end
```

## Scala

```scala
object Solution {
    def findIntersectionValues(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
        val set2 = nums2.toSet
        val answer1 = nums1.count(set2.contains)
        val set1 = nums1.toSet
        val answer2 = nums2.count(set1.contains)
        Array(answer1, answer2)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_intersection_values(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut in_nums2 = [false; 101];
        for &v in &nums2 {
            in_nums2[v as usize] = true;
        }
        let answer1 = nums1.iter().filter(|&&x| in_nums2[x as usize]).count() as i32;

        let mut in_nums1 = [false; 101];
        for &v in &nums1 {
            in_nums1[v as usize] = true;
        }
        let answer2 = nums2.iter().filter(|&&x| in_nums1[x as usize]).count() as i32;

        vec![answer1, answer2]
    }
}
```

## Racket

```racket
(define/contract (find-intersection-values nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ((answer1 (for/sum ([x nums1]) (if (member x nums2) 1 0)))
         (answer2 (for/sum ([y nums2]) (if (member y nums1) 1 0))))
    (list answer1 answer2)))
```

## Erlang

```erlang
-module(solution).
-export([find_intersection_values/2]).

-spec find_intersection_values(Nums1 :: [integer()], Nums2 :: [integer()]) -> [integer()].
find_intersection_values(Nums1, Nums2) ->
    Set2 = maps:from_list([{X, true} || X <- Nums2]),
    Answer1 = count_common(Nums1, Set2),
    Set1 = maps:from_list([{X, true} || X <- Nums1]),
    Answer2 = count_common(Nums2, Set1),
    [Answer1, Answer2].

count_common([], _Set) -> 0;
count_common([H|T], Set) ->
    case maps:is_key(H, Set) of
        true -> 1 + count_common(T, Set);
        false -> count_common(T, Set)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_intersection_values(nums1 :: [integer], nums2 :: [integer]) :: [integer]
  def find_intersection_values(nums1, nums2) do
    set2 = MapSet.new(nums2)
    answer1 = Enum.count(nums1, fn x -> MapSet.member?(set2, x) end)

    set1 = MapSet.new(nums1)
    answer2 = Enum.count(nums2, fn x -> MapSet.member?(set1, x) end)

    [answer1, answer2]
  end
end
```
