# 2545. Sort the Students by Their Kth Score

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> sortTheStudents(vector<vector<int>>& score, int k) {
        sort(score.begin(), score.end(),
             [&](const vector<int>& a, const vector<int>& b) {
                 return a[k] > b[k];
             });
        return score;
    }
};
```

## Java

```java
class Solution {
    public int[][] sortTheStudents(int[][] score, int k) {
        java.util.Arrays.sort(score, (a, b) -> Integer.compare(b[k], a[k]));
        return score;
    }
}
```

## Python

```python
class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        return sorted(score, key=lambda row: row[k], reverse=True)
```

## Python3

```python
from typing import List

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, key=lambda row: row[k], reverse=True)
```

## C

```c
#include <stdlib.h>

static int gk;

/* Comparator for qsort: sort rows by the k-th column in descending order */
static int cmp_rows(const void *a, const void *b) {
    const int *rowA = *(const int **)a;
    const int *rowB = *(const int **)b;
    if (rowB[gk] > rowA[gk]) return 1;
    if (rowB[gk] < rowA[gk]) return -1;
    return 0;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** sortTheStudents(int** score, int scoreSize, int* scoreColSize, int k,
                      int* returnSize, int** returnColumnSizes) {
    int m = scoreSize;
    int n = scoreColSize[0];

    *returnSize = m;
    *returnColumnSizes = (int *)malloc(m * sizeof(int));
    for (int i = 0; i < m; ++i) {
        (*returnColumnSizes)[i] = n;
    }

    /* Allocate result matrix */
    int **result = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; ++i) {
        result[i] = (int *)malloc(n * sizeof(int));
    }

    /* Create an array of pointers to rows and sort it */
    int **rows = (int **)malloc(m * sizeof(int *));
    for (int i = 0; i < m; ++i) {
        rows[i] = score[i];
    }
    gk = k;
    qsort(rows, m, sizeof(int *), cmp_rows);

    /* Copy sorted rows into result */
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            result[i][j] = rows[i][j];
        }
    }

    free(rows);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[][] SortTheStudents(int[][] score, int k)
    {
        System.Array.Sort(score, (a, b) => b[k].CompareTo(a[k]));
        return score;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} score
 * @param {number} k
 * @return {number[][]}
 */
var sortTheStudents = function(score, k) {
    score.sort((a, b) => b[k] - a[k]);
    return score;
};
```

## Typescript

```typescript
function sortTheStudents(score: number[][], k: number): number[][] {
    return score.sort((a, b) => b[k] - a[k]);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $score
     * @param Integer $k
     * @return Integer[][]
     */
    function sortTheStudents($score, $k) {
        usort($score, function ($a, $b) use ($k) {
            return $b[$k] <=> $a[$k];
        });
        return $score;
    }
}
```

## Swift

```swift
class Solution {
    func sortTheStudents(_ score: [[Int]], _ k: Int) -> [[Int]] {
        return score.sorted { $0[k] > $1[k] }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sortTheStudents(score: Array<IntArray>, k: Int): Array<IntArray> {
        return score.sortedWith(compareByDescending<IntArray> { it[k] }).toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> sortTheStudents(List<List<int>> score, int k) {
    score.sort((a, b) => b[k].compareTo(a[k]));
    return score;
  }
}
```

## Golang

```go
import "sort"

func sortTheStudents(score [][]int, k int) [][]int {
	sort.Slice(score, func(i, j int) bool {
		return score[i][k] > score[j][k]
	})
	return score
}
```

## Ruby

```ruby
def sort_the_students(score, k)
  score.sort_by { |row| -row[k] }
end
```

## Scala

```scala
object Solution {
    def sortTheStudents(score: Array[Array[Int]], k: Int): Array[Array[Int]] = {
        score.sortWith(_(k) > _(k))
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sort_the_students(mut score: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let idx = k as usize;
        score.sort_by(|a, b| b[idx].cmp(&a[idx]));
        score
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (sort-the-students score k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof (listof exact-integer?)))
  (let ((cmp (lambda (a b) (> (list-ref a k) (list-ref b k)))))
    (sort score cmp)))
```

## Erlang

```erlang
-spec sort_the_students(Score :: [[integer()]], K :: integer()) -> [[integer()]].
sort_the_students(Score, K) ->
    Comparator = fun(A, B) ->
        lists:nth(K + 1, A) > lists:nth(K + 1, B)
    end,
    lists:sort(Comparator, Score).
```

## Elixir

```elixir
defmodule Solution do
  @spec sort_the_students(score :: [[integer]], k :: integer) :: [[integer]]
  def sort_the_students(score, k) do
    Enum.sort_by(score, fn row -> Enum.at(row, k) end, :desc)
  end
end
```
