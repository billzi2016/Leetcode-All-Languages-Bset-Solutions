# 0119. Pascal's Triangle II

## Cpp

```cpp
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> row(rowIndex + 1, 0);
        row[0] = 1;
        for (int i = 1; i <= rowIndex; ++i) {
            row[i] = 1;
            for (int j = i - 1; j > 0; --j) {
                row[j] += row[j - 1];
            }
        }
        return row;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<Integer> getRow(int rowIndex) {
        int[] row = new int[rowIndex + 1];
        row[0] = 1;
        for (int i = 1; i <= rowIndex; i++) {
            for (int j = i; j >= 1; j--) {
                row[j] += row[j - 1];
            }
        }
        java.util.List<Integer> result = new java.util.ArrayList<>(rowIndex + 1);
        for (int val : row) {
            result.add(val);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(1, rowIndex + 1):
            row.append(0)
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        return row
```

## Python3

```python
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        c = 1
        for k in range(1, rowIndex + 1):
            c = c * (rowIndex - k + 1) // k
            result.append(c)
        return result
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getRow(int rowIndex, int* returnSize) {
    *returnSize = rowIndex + 1;
    int* row = (int*)malloc((*returnSize) * sizeof(int));
    long long val = 1;
    for (int i = 0; i <= rowIndex; ++i) {
        row[i] = (int)val;
        val = val * (rowIndex - i) / (i + 1);
    }
    return row;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> GetRow(int rowIndex) {
        var row = new List<int>(rowIndex + 1);
        for (int i = 0; i <= rowIndex; i++) row.Add(0);
        row[0] = 1;
        for (int i = 1; i <= rowIndex; i++) {
            for (int j = i; j > 0; j--) {
                row[j] = row[j] + row[j - 1];
            }
        }
        return row;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    const row = new Array(rowIndex + 1).fill(0);
    row[0] = 1;
    for (let i = 1; i <= rowIndex; i++) {
        for (let j = i; j > 0; j--) {
            row[j] += row[j - 1];
        }
    }
    return row;
};
```

## Typescript

```typescript
function getRow(rowIndex: number): number[] {
    const row: number[] = [1];
    for (let i = 1; i <= rowIndex; i++) {
        row.push(0);
        for (let j = i; j > 0; j--) {
            row[j] = (row[j] ?? 0) + row[j - 1];
        }
    }
    return row;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $rowIndex
     * @return Integer[]
     */
    function getRow($rowIndex) {
        $row = [1];
        for ($i = 1; $i <= $rowIndex; $i++) {
            $row[] = 0;
            for ($j = $i; $j > 0; $j--) {
                $row[$j] = $row[$j] + $row[$j - 1];
            }
        }
        return $row;
    }
}
```

## Swift

```swift
class Solution {
    func getRow(_ rowIndex: Int) -> [Int] {
        var row = Array(repeating: 0, count: rowIndex + 1)
        row[0] = 1
        if rowIndex == 0 { return row }
        for i in 1...rowIndex {
            var j = i
            while j > 0 {
                row[j] += row[j - 1]
                j -= 1
            }
        }
        return row
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getRow(rowIndex: Int): List<Int> {
        val row = MutableList(rowIndex + 1) { 0 }
        row[0] = 1
        for (i in 1..rowIndex) {
            for (j in i downTo 1) {
                row[j] = row[j] + row[j - 1]
            }
        }
        return row
    }
}
```

## Dart

```dart
class Solution {
  List<int> getRow(int rowIndex) {
    List<int> row = [1];
    for (int i = 1; i <= rowIndex; i++) {
      row.add(0);
      for (int j = i; j >= 1; j--) {
        row[j] = row[j] + row[j - 1];
      }
    }
    return row;
  }
}
```

## Golang

```go
func getRow(rowIndex int) []int {
    row := make([]int, rowIndex+1)
    row[0] = 1
    for i := 1; i <= rowIndex; i++ {
        for j := i; j > 0; j-- {
            row[j] += row[j-1]
        }
    }
    return row
}
```

## Ruby

```ruby
def get_row(row_index)
  row = [1]
  (1..row_index).each do |i|
    j = i - 1
    while j > 0
      row[j] = row[j] + row[j - 1]
      j -= 1
    end
    row << 1
  end
  row
end
```

## Scala

```scala
object Solution {
    def getRow(rowIndex: Int): List[Int] = {
        val row = new Array[Int](rowIndex + 1)
        row(0) = 1
        var i = 1
        while (i <= rowIndex) {
            var j = i
            while (j > 0) {
                row(j) += row(j - 1)
                j -= 1
            }
            i += 1
        }
        row.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_row(row_index: i32) -> Vec<i32> {
        let n = row_index as usize;
        let mut row = vec![1i32; n + 1];
        for i in 2..=n {
            for j in (1..i).rev() {
                row[j] = row[j] + row[j - 1];
            }
        }
        row
    }
}
```

## Racket

```racket
(define/contract (get-row rowIndex)
  (-> exact-integer? (listof exact-integer?))
  (let* ((n (+ rowIndex 1))
         (vec (make-vector n 1)))
    (for ([i (in-range 1 n)])
      (for ([j (in-range (- i 1) 0 -1)])
        (vector-set! vec j
                     (+ (vector-ref vec j)
                        (vector-ref vec (- j 1))))))
    (vector->list vec)))
```

## Erlang

```erlang
-module(solution).
-export([get_row/1]).

-spec get_row(RowIndex :: integer()) -> [integer()].
get_row(RowIndex) when RowIndex >= 0 ->
    build(RowIndex, 0, [], 1).

build(N, I, Acc, Curr) when I =< N ->
    NewAcc = [Curr | Acc],
    Next = if I == N -> Curr; true -> (Curr * (N - I)) div (I + 1) end,
    build(N, I + 1, NewAcc, Next);
build(_, _, Acc, _) ->
    lists:reverse(Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_row(row_index :: integer) :: [integer]
  def get_row(row_index) do
    0..row_index
    |> Enum.reduce([], fn k, acc ->
      if k == 0 do
        [1 | acc]
      else
        prev = hd(acc)
        val = div(prev * (row_index - k + 1), k)
        [val | acc]
      end
    end)
    |> Enum.reverse()
  end
end
```
