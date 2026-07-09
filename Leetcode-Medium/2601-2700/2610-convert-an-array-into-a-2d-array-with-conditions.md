# 2610. Convert an Array Into a 2D Array With Conditions

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        int n = nums.size();
        vector<int> freq(n + 1, 0);
        vector<vector<int>> ans;
        for (int x : nums) {
            if (freq[x] >= (int)ans.size()) {
                ans.emplace_back();
            }
            ans[freq[x]].push_back(x);
            ++freq[x];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<java.util.List<Integer>> findMatrix(int[] nums) {
        int n = nums.length;
        int[] freq = new int[n + 1];
        java.util.List<java.util.List<Integer>> ans = new java.util.ArrayList<>();
        for (int num : nums) {
            int f = freq[num];
            if (f == ans.size()) {
                ans.add(new java.util.ArrayList<>());
            }
            ans.get(f).add(num);
            freq[num]++;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        freq = [0] * (len(nums) + 1)
        ans = []
        for x in nums:
            row = freq[x]
            if row == len(ans):
                ans.append([])
            ans[row].append(x)
            freq[x] += 1
        return ans
```

## Python3

```python
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        freq = [0] * (n + 1)          # frequencies of values (values are <= n)
        ans: List[List[int]] = []     # resulting rows
        
        for x in nums:
            row_idx = freq[x]
            if row_idx == len(ans):   # need a new row
                ans.append([])
            ans[row_idx].append(x)
            freq[x] += 1
        
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findMatrix(int* nums, int numsSize, int* returnSize, int*** returnColumnSizes) {
    // Frequency count to determine maximum frequency (number of rows)
    int *freq = calloc(numsSize + 1, sizeof(int));
    int maxFreq = 0;
    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        freq[val]++;
        if (freq[val] > maxFreq) maxFreq = freq[val];
    }

    // Allocate result structures
    *returnSize = maxFreq;
    int **ans = malloc(maxFreq * sizeof(int*));
    int *colSizes = calloc(maxFreq, sizeof(int));

    for (int i = 0; i < maxFreq; ++i) {
        ans[i] = malloc(numsSize * sizeof(int)); // maximum possible length
    }

    // Reset counters to place elements row by row
    memset(freq, 0, (numsSize + 1) * sizeof(int));

    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        int row = freq[val];          // current occurrence index determines the row
        ans[row][colSizes[row]++] = val;
        freq[val]++;
    }

    free(freq);
    *returnColumnSizes = &colSizes;
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> FindMatrix(int[] nums) {
        int n = nums.Length;
        int[] freq = new int[n + 1];
        List<IList<int>> ans = new List<IList<int>>();
        foreach (int x in nums) {
            if (freq[x] == ans.Count) {
                ans.Add(new List<int>());
            }
            ans[freq[x]].Add(x);
            freq[x]++;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var findMatrix = function(nums) {
    const n = nums.length;
    const freq = new Array(n + 1).fill(0);
    const ans = [];
    
    for (const num of nums) {
        if (freq[num] >= ans.length) {
            ans.push([]);
        }
        ans[freq[num]].push(num);
        freq[num]++;
    }
    
    return ans;
};
```

## Typescript

```typescript
function findMatrix(nums: number[]): number[][] {
    const n = nums.length;
    const freq = new Array(n + 1).fill(0);
    const ans: number[][] = [];
    for (const num of nums) {
        const rowIdx = freq[num];
        if (rowIdx >= ans.length) {
            ans.push([]);
        }
        ans[rowIdx].push(num);
        freq[num] = rowIdx + 1;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function findMatrix($nums) {
        $n = count($nums);
        $freq = array_fill(0, $n + 1, 0);
        $ans = [];

        foreach ($nums as $c) {
            $rowIdx = $freq[$c];
            if ($rowIdx >= count($ans)) {
                $ans[] = [];
            }
            $ans[$rowIdx][] = $c;
            $freq[$c]++;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func findMatrix(_ nums: [Int]) -> [[Int]] {
        let n = nums.count
        var freq = Array(repeating: 0, count: n + 1)
        var ans: [[Int]] = []
        for num in nums {
            if freq[num] >= ans.count {
                ans.append([])
            }
            ans[freq[num]].append(num)
            freq[num] += 1
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMatrix(nums: IntArray): List<List<Int>> {
        val n = nums.size
        val freq = IntArray(n + 1)
        val ans = mutableListOf<MutableList<Int>>()
        for (c in nums) {
            val idx = freq[c]
            if (idx == ans.size) {
                ans.add(mutableListOf())
            }
            ans[idx].add(c)
            freq[c] = idx + 1
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> findMatrix(List<int> nums) {
    int n = nums.length;
    List<int> freq = List.filled(n + 1, 0);
    List<List<int>> ans = [];
    for (int c in nums) {
      if (freq[c] == ans.length) {
        ans.add([]);
      }
      ans[freq[c]].add(c);
      freq[c]++;
    }
    return ans;
  }
}
```

## Golang

```go
func findMatrix(nums []int) [][]int {
    n := len(nums)
    freq := make([]int, n+1)
    var ans [][]int
    for _, v := range nums {
        if freq[v] >= len(ans) {
            ans = append(ans, []int{})
        }
        ans[freq[v]] = append(ans[freq[v]], v)
        freq[v]++
    }
    return ans
}
```

## Ruby

```ruby
def find_matrix(nums)
  n = nums.length
  freq = Array.new(n + 1, 0)
  ans = []
  nums.each do |c|
    row = freq[c]
    if row >= ans.size
      ans << []
    end
    ans[row] << c
    freq[c] += 1
  end
  ans
end
```

## Scala

```scala
object Solution {
    def findMatrix(nums: Array[Int]): List[List[Int]] = {
        val n = nums.length
        val freq = new Array[Int](n + 1)
        val rows = scala.collection.mutable.ArrayBuffer[scala.collection.mutable.ArrayBuffer[Int]]()
        for (c <- nums) {
            if (freq(c) >= rows.size) {
                rows += scala.collection.mutable.ArrayBuffer[Int]()
            }
            rows(freq(c)) += c
            freq(c) += 1
        }
        rows.map(_.toList).toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_matrix(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let n = nums.len();
        let mut freq = vec![0usize; n + 1];
        let mut ans: Vec<Vec<i32>> = Vec::new();

        for &c in nums.iter() {
            let idx = c as usize;
            if freq[idx] >= ans.len() {
                ans.push(Vec::new());
            }
            let row = freq[idx];
            ans[row].push(c);
            freq[idx] += 1;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (find-matrix nums)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  (let* ((n (length nums))
         (size (+ n 1))
         (freq (make-vector size 0)))
    ;; count frequencies to determine needed rows
    (for ([c nums])
      (vector-set! freq c (+ 1 (vector-ref freq c))))
    (define max-freq
      (apply max (vector->list freq)))
    ;; reset frequency counters for placement
    (for ([i (in-range size)])
      (vector-set! freq i 0))
    ;; create rows container
    (define rows (make-vector max-freq '()))
    ;; distribute elements into rows
    (for ([c nums])
      (let ((idx (vector-ref freq c)))
        (vector-set! rows idx (cons c (vector-ref rows idx)))
        (vector-set! freq c (+ idx 1))))
    ;; build final list of rows, preserving original order within each row
    (let loop ((i (- max-freq 1)) (acc '()))
      (if (< i 0)
          (reverse acc)
          (loop (- i 1)
                (cons (reverse (vector-ref rows i)) acc))))))
```

## Erlang

```erlang
-spec find_matrix(Nums :: [integer()]) -> [[integer()]].
find_matrix(Nums) ->
    build(Nums, [], #{}).

build([], Ans, _Freq) -> 
    Ans;
build([C|Rest], Ans, Freq) ->
    Count = maps:get(C, Freq, 0),
    RowNum = length(Ans),
    NewAns =
        if
            Count >= RowNum ->
                Ans ++ [[C]];
            true ->
                {Prefix, [Row|Suffix]} = lists:split(Count, Ans),
                UpdatedRow = Row ++ [C],
                Prefix ++ [UpdatedRow] ++ Suffix
        end,
    NewFreq = maps:put(C, Count + 1, Freq),
    build(Rest, NewAns, NewFreq).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_matrix(nums :: [integer]) :: [[integer]]
  def find_matrix(nums) do
    {_, rows} =
      Enum.reduce(nums, {%{}, []}, fn num, {freq, rows} ->
        count = Map.get(freq, num, 0)

        rows =
          if count == length(rows) do
            rows ++ [[]]
          else
            rows
          end

        cur_row = Enum.at(rows, count)
        new_row = cur_row ++ [num]

        rows = List.replace_at(rows, count, new_row)
        freq = Map.put(freq, num, count + 1)

        {freq, rows}
      end)

    rows
  end
end
```
