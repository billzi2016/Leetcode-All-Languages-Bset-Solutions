# 2570. Merge Two 2D Arrays by Summing Values

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {
        vector<vector<int>> res;
        int i = 0, j = 0;
        while (i < (int)nums1.size() && j < (int)nums2.size()) {
            int id1 = nums1[i][0];
            int id2 = nums2[j][0];
            if (id1 == id2) {
                res.push_back({id1, nums1[i][1] + nums2[j][1]});
                ++i; ++j;
            } else if (id1 < id2) {
                res.push_back(nums1[i]);
                ++i;
            } else { // id2 < id1
                res.push_back(nums2[j]);
                ++j;
            }
        }
        while (i < (int)nums1.size()) {
            res.push_back(nums1[i++]);
        }
        while (j < (int)nums2.size()) {
            res.push_back(nums2[j++]);
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        int i = 0, j = 0;
        int n1 = nums1.length, n2 = nums2.length;
        java.util.List<int[]> merged = new java.util.ArrayList<>();
        while (i < n1 && j < n2) {
            int id1 = nums1[i][0];
            int id2 = nums2[j][0];
            if (id1 == id2) {
                merged.add(new int[]{id1, nums1[i][1] + nums2[j][1]});
                i++;
                j++;
            } else if (id1 < id2) {
                merged.add(nums1[i]);
                i++;
            } else {
                merged.add(nums2[j]);
                j++;
            }
        }
        while (i < n1) {
            merged.add(nums1[i++]);
        }
        while (j < n2) {
            merged.add(nums2[j++]);
        }
        int[][] result = new int[merged.size()][2];
        for (int k = 0; k < merged.size(); k++) {
            result[k] = merged.get(k);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        i = j = 0
        merged = []
        n1, n2 = len(nums1), len(nums2)
        while i < n1 and j < n2:
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            if id1 == id2:
                merged.append([id1, val1 + val2])
                i += 1
                j += 1
            elif id1 < id2:
                merged.append([id1, val1])
                i += 1
            else:
                merged.append([id2, val2])
                j += 1
        while i < n1:
            merged.append(nums1[i][:])
            i += 1
        while j < n2:
            merged.append(nums2[j][:])
            j += 1
        return merged
```

## Python3

```python
from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = j = 0
        merged: List[List[int]] = []
        while i < len(nums1) and j < len(nums2):
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            if id1 == id2:
                merged.append([id1, val1 + val2])
                i += 1
                j += 1
            elif id1 < id2:
                merged.append([id1, val1])
                i += 1
            else:
                merged.append([id2, val2])
                j += 1
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        return merged
```

## C

```c
#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** mergeArrays(int** nums1, int nums1Size, int* nums1ColSize,
                  int** nums2, int nums2Size, int* nums2ColSize,
                  int* returnSize, int** returnColumnSizes) {
    int maxSize = nums1Size + nums2Size;
    int **result = (int **)malloc(sizeof(int *) * maxSize);
    int *colSizes = (int *)malloc(sizeof(int) * maxSize);

    int i = 0, j = 0, idx = 0;

    while (i < nums1Size && j < nums2Size) {
        int id1 = nums1[i][0];
        int val1 = nums1[i][1];
        int id2 = nums2[j][0];
        int val2 = nums2[j][1];

        if (id1 == id2) {
            result[idx] = (int *)malloc(sizeof(int) * 2);
            result[idx][0] = id1;
            result[idx][1] = val1 + val2;
            colSizes[idx] = 2;
            idx++;
            i++;
            j++;
        } else if (id1 < id2) {
            result[idx] = (int *)malloc(sizeof(int) * 2);
            result[idx][0] = id1;
            result[idx][1] = val1;
            colSizes[idx] = 2;
            idx++;
            i++;
        } else { // id2 < id1
            result[idx] = (int *)malloc(sizeof(int) * 2);
            result[idx][0] = id2;
            result[idx][1] = val2;
            colSizes[idx] = 2;
            idx++;
            j++;
        }
    }

    while (i < nums1Size) {
        result[idx] = (int *)malloc(sizeof(int) * 2);
        result[idx][0] = nums1[i][0];
        result[idx][1] = nums1[i][1];
        colSizes[idx] = 2;
        idx++;
        i++;
    }

    while (j < nums2Size) {
        result[idx] = (int *)malloc(sizeof(int) * 2);
        result[idx][0] = nums2[j][0];
        result[idx][1] = nums2[j][1];
        colSizes[idx] = 2;
        idx++;
        j++;
    }

    *returnSize = idx;
    *returnColumnSizes = colSizes;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] MergeArrays(int[][] nums1, int[][] nums2) {
        int n1 = nums1.Length;
        int n2 = nums2.Length;
        var result = new List<int[]>();
        int i = 0, j = 0;
        while (i < n1 && j < n2) {
            if (nums1[i][0] == nums2[j][0]) {
                result.Add(new int[] { nums1[i][0], nums1[i][1] + nums2[j][1] });
                i++;
                j++;
            } else if (nums1[i][0] < nums2[j][0]) {
                result.Add(new int[] { nums1[i][0], nums1[i][1] });
                i++;
            } else {
                result.Add(new int[] { nums2[j][0], nums2[j][1] });
                j++;
            }
        }
        while (i < n1) {
            result.Add(new int[] { nums1[i][0], nums1[i][1] });
            i++;
        }
        while (j < n2) {
            result.Add(new int[] { nums2[j][0], nums2[j][1] });
            j++;
        }
        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} nums1
 * @param {number[][]} nums2
 * @return {number[][]}
 */
var mergeArrays = function(nums1, nums2) {
    let i = 0, j = 0;
    const merged = [];
    while (i < nums1.length && j < nums2.length) {
        const [id1, val1] = nums1[i];
        const [id2, val2] = nums2[j];
        if (id1 === id2) {
            merged.push([id1, val1 + val2]);
            i++;
            j++;
        } else if (id1 < id2) {
            merged.push([id1, val1]);
            i++;
        } else {
            merged.push([id2, val2]);
            j++;
        }
    }
    while (i < nums1.length) {
        merged.push(nums1[i++]);
    }
    while (j < nums2.length) {
        merged.push(nums2[j++]);
    }
    return merged;
};
```

## Typescript

```typescript
function mergeArrays(nums1: number[][], nums2: number[][]): number[][] {
    const result: number[][] = [];
    let i = 0, j = 0;
    while (i < nums1.length && j < nums2.length) {
        const [id1, val1] = nums1[i];
        const [id2, val2] = nums2[j];
        if (id1 === id2) {
            result.push([id1, val1 + val2]);
            i++;
            j++;
        } else if (id1 < id2) {
            result.push([id1, val1]);
            i++;
        } else {
            result.push([id2, val2]);
            j++;
        }
    }
    while (i < nums1.length) {
        result.push(nums1[i]);
        i++;
    }
    while (j < nums2.length) {
        result.push(nums2[j]);
        j++;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $nums1
     * @param Integer[][] $nums2
     * @return Integer[][]
     */
    function mergeArrays($nums1, $nums2) {
        $i = 0;
        $j = 0;
        $n1 = count($nums1);
        $n2 = count($nums2);
        $result = [];

        while ($i < $n1 && $j < $n2) {
            $id1 = $nums1[$i][0];
            $id2 = $nums2[$j][0];

            if ($id1 == $id2) {
                $result[] = [$id1, $nums1[$i][1] + $nums2[$j][1]];
                $i++;
                $j++;
            } elseif ($id1 < $id2) {
                $result[] = $nums1[$i];
                $i++;
            } else {
                $result[] = $nums2[$j];
                $j++;
            }
        }

        while ($i < $n1) {
            $result[] = $nums1[$i];
            $i++;
        }

        while ($j < $n2) {
            $result[] = $nums2[$j];
            $j++;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func mergeArrays(_ nums1: [[Int]], _ nums2: [[Int]]) -> [[Int]] {
        var i = 0
        var j = 0
        var merged: [[Int]] = []
        
        while i < nums1.count && j < nums2.count {
            let id1 = nums1[i][0]
            let id2 = nums2[j][0]
            
            if id1 == id2 {
                merged.append([id1, nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            } else if id1 < id2 {
                merged.append(nums1[i])
                i += 1
            } else {
                merged.append(nums2[j])
                j += 1
            }
        }
        
        while i < nums1.count {
            merged.append(nums1[i])
            i += 1
        }
        
        while j < nums2.count {
            merged.append(nums2[j])
            j += 1
        }
        
        return merged
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun mergeArrays(nums1: Array<IntArray>, nums2: Array<IntArray>): Array<IntArray> {
        val merged = mutableListOf<IntArray>()
        var i = 0
        var j = 0
        while (i < nums1.size && j < nums2.size) {
            val id1 = nums1[i][0]
            val id2 = nums2[j][0]
            when {
                id1 == id2 -> {
                    merged.add(intArrayOf(id1, nums1[i][1] + nums2[j][1]))
                    i++
                    j++
                }
                id1 < id2 -> {
                    merged.add(nums1[i])
                    i++
                }
                else -> {
                    merged.add(nums2[j])
                    j++
                }
            }
        }
        while (i < nums1.size) {
            merged.add(nums1[i])
            i++
        }
        while (j < nums2.size) {
            merged.add(nums2[j])
            j++
        }
        return merged.toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> mergeArrays(List<List<int>> nums1, List<List<int>> nums2) {
    int i = 0, j = 0;
    int n1 = nums1.length, n2 = nums2.length;
    List<List<int>> merged = [];

    while (i < n1 && j < n2) {
      int id1 = nums1[i][0];
      int val1 = nums1[i][1];
      int id2 = nums2[j][0];
      int val2 = nums2[j][1];

      if (id1 == id2) {
        merged.add([id1, val1 + val2]);
        i++;
        j++;
      } else if (id1 < id2) {
        merged.add([id1, val1]);
        i++;
      } else {
        merged.add([id2, val2]);
        j++;
      }
    }

    while (i < n1) {
      merged.add([nums1[i][0], nums1[i][1]]);
      i++;
    }

    while (j < n2) {
      merged.add([nums2[j][0], nums2[j][1]]);
      j++;
    }

    return merged;
  }
}
```

## Golang

```go
func mergeArrays(nums1 [][]int, nums2 [][]int) [][]int {
	i, j := 0, 0
	n1, n2 := len(nums1), len(nums2)
	res := make([][]int, 0, n1+n2)

	for i < n1 && j < n2 {
		id1, val1 := nums1[i][0], nums1[i][1]
		id2, val2 := nums2[j][0], nums2[j][1]

		if id1 == id2 {
			res = append(res, []int{id1, val1 + val2})
			i++
			j++
		} else if id1 < id2 {
			res = append(res, []int{id1, val1})
			i++
		} else {
			res = append(res, []int{id2, val2})
			j++
		}
	}

	for i < n1 {
		res = append(res, []int{nums1[i][0], nums1[i][1]})
		i++
	}
	for j < n2 {
		res = append(res, []int{nums2[j][0], nums2[j][1]})
		j++
	}

	return res
}
```

## Ruby

```ruby
def merge_arrays(nums1, nums2)
  i = 0
  j = 0
  result = []
  while i < nums1.length && j < nums2.length
    id1, val1 = nums1[i]
    id2, val2 = nums2[j]
    if id1 == id2
      result << [id1, val1 + val2]
      i += 1
      j += 1
    elsif id1 < id2
      result << [id1, val1]
      i += 1
    else
      result << [id2, val2]
      j += 1
    end
  end
  while i < nums1.length
    result << nums1[i]
    i += 1
  end
  while j < nums2.length
    result << nums2[j]
    j += 1
  end
  result
end
```

## Scala

```scala
object Solution {
    def mergeArrays(nums1: Array[Array[Int]], nums2: Array[Array[Int]]): Array[Array[Int]] = {
        val result = scala.collection.mutable.ArrayBuffer[Array[Int]]()
        var i = 0
        var j = 0
        while (i < nums1.length && j < nums2.length) {
            val id1 = nums1(i)(0)
            val id2 = nums2(j)(0)
            if (id1 == id2) {
                result += Array(id1, nums1(i)(1) + nums2(j)(1))
                i += 1
                j += 1
            } else if (id1 < id2) {
                result += nums1(i)
                i += 1
            } else {
                result += nums2(j)
                j += 1
            }
        }
        while (i < nums1.length) {
            result += nums1(i)
            i += 1
        }
        while (j < nums2.length) {
            result += nums2(j)
            j += 1
        }
        result.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn merge_arrays(nums1: Vec<Vec<i32>>, nums2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut i = 0;
        let mut j = 0;
        let n1 = nums1.len();
        let n2 = nums2.len();
        let mut res: Vec<Vec<i32>> = Vec::with_capacity(n1 + n2);
        while i < n1 && j < n2 {
            let id1 = nums1[i][0];
            let id2 = nums2[j][0];
            if id1 == id2 {
                let sum = nums1[i][1] + nums2[j][1];
                res.push(vec![id1, sum]);
                i += 1;
                j += 1;
            } else if id1 < id2 {
                res.push(nums1[i].clone());
                i += 1;
            } else {
                res.push(nums2[j].clone());
                j += 1;
            }
        }
        while i < n1 {
            res.push(nums1[i].clone());
            i += 1;
        }
        while j < n2 {
            res.push(nums2[j].clone());
            j += 1;
        }
        res
    }
}
```

## Racket

```racket
(define/contract (merge-arrays nums1 nums2)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof (listof exact-integer?)))
  (let loop ((l1 nums1) (l2 nums2) (acc '()))
    (cond
      [(and (null? l1) (null? l2)) (reverse acc)]
      [(null? l1) (loop '() (cdr l2) (cons (car l2) acc))]
      [(null? l2) (loop (cdr l1) '() (cons (car l1) acc))]
      [else
       (define id1 (caar l1))
       (define val1 (cadar l1))
       (define id2 (caar l2))
       (define val2 (cadar l2))
       (cond
         [(= id1 id2)
          (loop (cdr l1) (cdr l2) (cons (list id1 (+ val1 val2)) acc))]
         [(< id1 id2)
          (loop (cdr l1) l2 (cons (car l1) acc))]
         [else
          (loop l1 (cdr l2) (cons (car l2) acc))])])))
```

## Erlang

```erlang
-spec merge_arrays(Nums1 :: [[integer()]], Nums2 :: [[integer()]]) -> [[integer()]].
merge_arrays(Nums1, Nums2) ->
    merge(Nums1, Nums2, []).

merge([], [], Acc) ->
    lists:reverse(Acc);
merge([], [H|T], Acc) ->
    merge([], T, [H|Acc]);
merge([H|T], [], Acc) ->
    merge(T, [], [H|Acc]);
merge([[Id,V1]=P1|Rest1], [[Id,_]=P2|Rest2], Acc) when Id =:= Id ->
    %% This clause will never match because of guard redundancy; keep for completeness
    merge(Rest1, Rest2, [[Id, V1+element(2, P2)]|Acc]);
merge([[Id1,V1]=P1|Rest1], [[Id2,_]|_]=L2, Acc) when Id1 < Id2 ->
    merge(Rest1, L2, [P1|Acc]);
merge(L1, [[Id2,V2]=P2|Rest2], Acc) ->
    merge(L1, Rest2, [P2|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec merge_arrays(nums1 :: [[integer]], nums2 :: [[integer]]) :: [[integer]]
  def merge_arrays(nums1, nums2) do
    merge(nums1, nums2)
  end

  defp merge([], b), do: b
  defp merge(a, []), do: a

  defp merge([[id1, val1] | t1] = a, [[id2, val2] | t2] = b) do
    cond do
      id1 == id2 ->
        [[id1, val1 + val2] | merge(t1, t2)]

      id1 < id2 ->
        [[id1, val1] | merge(t1, b)]

      true ->
        [[id2, val2] | merge(a, t2)]
    end
  end
end
```
