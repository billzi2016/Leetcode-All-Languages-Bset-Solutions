# 3159. Find Occurrences of an Element in an Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> occurrencesOfElement(vector<int>& nums, vector<int>& queries, int x) {
        vector<int> pos;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] == x) pos.push_back(i);
        }
        vector<int> ans;
        ans.reserve(queries.size());
        for (int q : queries) {
            if (q <= (int)pos.size()) ans.push_back(pos[q - 1]);
            else ans.push_back(-1);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] occurrencesOfElement(int[] nums, int[] queries, int x) {
        List<Integer> positions = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == x) {
                positions.add(i);
            }
        }
        int[] answer = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int k = queries[i];
            if (k <= positions.size()) {
                answer[i] = positions.get(k - 1);
            } else {
                answer[i] = -1;
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """
        positions = [i for i, val in enumerate(nums) if val == x]
        m = len(positions)
        ans = []
        for k in queries:
            if 1 <= k <= m:
                ans.append(positions[k - 1])
            else:
                ans.append(-1)
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        positions = [i for i, val in enumerate(nums) if val == x]
        res = []
        occ_len = len(positions)
        for k in queries:
            idx = k - 1
            if 0 <= idx < occ_len:
                res.append(positions[idx])
            else:
                res.append(-1)
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* occurrencesOfElement(int* nums, int numsSize, int* queries, int queriesSize, int x, int* returnSize) {
    // Store indices where nums[i] == x
    int *pos = (int *)malloc(numsSize * sizeof(int));
    int posCount = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == x) {
            pos[posCount++] = i;
        }
    }

    // Prepare answer array
    int *ans = (int *)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; ++i) {
        int k = queries[i];
        if (k > 0 && k <= posCount) {
            ans[i] = pos[k - 1];
        } else {
            ans[i] = -1;
        }
    }

    free(pos);
    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] OccurrencesOfElement(int[] nums, int[] queries, int x) {
        var positions = new System.Collections.Generic.List<int>();
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == x) positions.Add(i);
        }

        int[] answer = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int k = queries[i];
            answer[i] = (k > 0 && k <= positions.Count) ? positions[k - 1] : -1;
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} queries
 * @param {number} x
 * @return {number[]}
 */
var occurrencesOfElement = function(nums, queries, x) {
    const positions = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === x) positions.push(i);
    }
    const result = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const k = queries[i];
        result[i] = k <= positions.length ? positions[k - 1] : -1;
    }
    return result;
};
```

## Typescript

```typescript
function occurrencesOfElement(nums: number[], queries: number[], x: number): number[] {
    const positions: number[] = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === x) positions.push(i);
    }
    const result: number[] = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const k = queries[i];
        result[i] = (k > 0 && k <= positions.length) ? positions[k - 1] : -1;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $queries
     * @param Integer $x
     * @return Integer[]
     */
    function occurrencesOfElement($nums, $queries, $x) {
        $positions = [];
        foreach ($nums as $idx => $val) {
            if ($val == $x) {
                $positions[] = $idx;
            }
        }

        $cnt = count($positions);
        $answer = [];

        foreach ($queries as $k) {
            if ($k <= $cnt) {
                $answer[] = $positions[$k - 1];
            } else {
                $answer[] = -1;
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func occurrencesOfElement(_ nums: [Int], _ queries: [Int], _ x: Int) -> [Int] {
        var positions = [Int]()
        for (i, val) in nums.enumerated() {
            if val == x {
                positions.append(i)
            }
        }
        var result = [Int]()
        result.reserveCapacity(queries.count)
        for q in queries {
            if q > 0 && q <= positions.count {
                result.append(positions[q - 1])
            } else {
                result.append(-1)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun occurrencesOfElement(nums: IntArray, queries: IntArray, x: Int): IntArray {
        val positions = mutableListOf<Int>()
        for (i in nums.indices) {
            if (nums[i] == x) positions.add(i)
        }
        val result = IntArray(queries.size)
        for (i in queries.indices) {
            val k = queries[i]
            result[i] = if (k <= positions.size) positions[k - 1] else -1
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> occurrencesOfElement(List<int> nums, List<int> queries, int x) {
    List<int> positions = [];
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == x) positions.add(i);
    }
    List<int> answer = List.filled(queries.length, 0);
    for (int i = 0; i < queries.length; i++) {
      int k = queries[i];
      answer[i] = (k <= positions.length) ? positions[k - 1] : -1;
    }
    return answer;
  }
}
```

## Golang

```go
func occurrencesOfElement(nums []int, queries []int, x int) []int {
    // Collect indices where nums[i] == x
    positions := make([]int, 0)
    for i, v := range nums {
        if v == x {
            positions = append(positions, i)
        }
    }

    ans := make([]int, len(queries))
    total := len(positions)

    for i, q := range queries {
        // q is the occurrence count (1-indexed)
        if q <= 0 || q > total {
            ans[i] = -1
        } else {
            ans[i] = positions[q-1]
        }
    }

    return ans
}
```

## Ruby

```ruby
def occurrences_of_element(nums, queries, x)
  positions = []
  nums.each_with_index { |val, idx| positions << idx if val == x }
  answers = Array.new(queries.length)
  queries.each_with_index do |k, i|
    answers[i] = k <= positions.size ? positions[k - 1] : -1
  end
  answers
end
```

## Scala

```scala
object Solution {
    def occurrencesOfElement(nums: Array[Int], queries: Array[Int], x: Int): Array[Int] = {
        val positions = new scala.collection.mutable.ArrayBuffer[Int]()
        var i = 0
        while (i < nums.length) {
            if (nums(i) == x) positions += i
            i += 1
        }
        val ans = new Array[Int](queries.length)
        var j = 0
        while (j < queries.length) {
            val k = queries(j)
            if (k <= positions.size) ans(j) = positions(k - 1) else ans(j) = -1
            j += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn occurrences_of_element(nums: Vec<i32>, queries: Vec<i32>, x: i32) -> Vec<i32> {
        let mut positions = Vec::new();
        for (i, &v) in nums.iter().enumerate() {
            if v == x {
                positions.push(i as i32);
            }
        }

        let mut answer = Vec::with_capacity(queries.len());
        for q in queries {
            if (q as usize) <= positions.len() && q > 0 {
                answer.push(positions[(q - 1) as usize]);
            } else {
                answer.push(-1);
            }
        }
        answer
    }
}
```

## Racket

```racket
(define/contract (occurrences-of-element nums queries x)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ([positions
          (let loop ((lst nums) (idx 0) (acc '()))
            (if (null? lst)
                (list->vector (reverse acc))
                (loop (cdr lst) (+ idx 1)
                      (if (= (car lst) x)
                          (cons idx acc)
                          acc))))]
         [len (vector-length positions)])
    (let loop ((qs queries) (acc '()))
      (if (null? qs)
          (reverse acc)
          (let* ([k (car qs)]
                 [ans (if (and (positive? k) (<= k len))
                          (vector-ref positions (- k 1))
                          -1)])
            (loop (cdr qs) (cons ans acc)))))))
```

## Erlang

```erlang
-spec occurrences_of_element(Nums :: [integer()], Queries :: [integer()], X :: integer()) -> [integer()].
occurrences_of_element(Nums, Queries, X) ->
    Map = build_occurrence_map(Nums, X),
    lists:map(fun(Q) ->
        case maps:find(Q, Map) of
            {ok, Pos} -> Pos;
            error -> -1
        end
    end, Queries).

build_occurrence_map(Nums, X) ->
    build_occurrence_map(Nums, X, 0, 1, #{}).

build_occurrence_map([], _X, _Idx, _Occ, Map) ->
    Map;
build_occurrence_map([H|T], X, Idx, Occ, Map) ->
    if
        H =:= X ->
            NewMap = maps:put(Occ, Idx, Map),
            build_occurrence_map(T, X, Idx + 1, Occ + 1, NewMap);
        true ->
            build_occurrence_map(T, X, Idx + 1, Occ, Map)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec occurrences_of_element(nums :: [integer], queries :: [integer], x :: integer) :: [integer]
  def occurrences_of_element(nums, queries, x) do
    positions = for {v, i} <- Enum.with_index(nums), v == x, do: i
    pos_len = length(positions)
    pos_tuple = List.to_tuple(positions)

    Enum.map(queries, fn q ->
      if q <= pos_len do
        elem(pos_tuple, q - 1)
      else
        -1
      end
    end)
  end
end
```
