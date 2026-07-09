# 0944. Delete Columns to Make Sorted

## Cpp

```cpp
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs.size();
        int m = strs[0].size();
        int deletions = 0;
        for (int col = 0; col < m; ++col) {
            bool sorted = true;
            for (int row = 1; row < n; ++row) {
                if (strs[row][col] < strs[row - 1][col]) {
                    sorted = false;
                    break;
                }
            }
            if (!sorted) ++deletions;
        }
        return deletions;
    }
};
```

## Java

```java
class Solution {
    public int minDeletionSize(String[] strs) {
        int rows = strs.length;
        int cols = strs[0].length();
        int deletions = 0;
        for (int c = 0; c < cols; c++) {
            for (int r = 1; r < rows; r++) {
                if (strs[r].charAt(c) < strs[r - 1].charAt(c)) {
                    deletions++;
                    break;
                }
            }
        }
        return deletions;
    }
}
```

## Python

```python
class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        if not strs:
            return 0
        rows = len(strs)
        cols = len(strs[0])
        deletions = 0
        for c in range(cols):
            for r in range(1, rows):
                if strs[r][c] < strs[r-1][c]:
                    deletions += 1
                    break
        return deletions
```

## Python3

```python
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs:
            return 0
        n = len(strs)
        m = len(strs[0])
        deletions = 0
        for col in range(m):
            for row in range(1, n):
                if strs[row][col] < strs[row - 1][col]:
                    deletions += 1
                    break
        return deletions
```

## C

```c
#include <string.h>

int minDeletionSize(char** strs, int strsSize) {
    if (strsSize == 0) return 0;
    int m = strlen(strs[0]);
    int deletions = 0;
    for (int col = 0; col < m; ++col) {
        for (int row = 0; row < strsSize - 1; ++row) {
            if (strs[row][col] > strs[row + 1][col]) {
                ++deletions;
                break;
            }
        }
    }
    return deletions;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinDeletionSize(string[] strs)
    {
        if (strs == null || strs.Length == 0) return 0;
        int rows = strs.Length;
        int cols = strs[0].Length;
        int deletions = 0;

        for (int c = 0; c < cols; c++)
        {
            bool needDelete = false;
            for (int r = 1; r < rows; r++)
            {
                if (strs[r][c] < strs[r - 1][c])
                {
                    needDelete = true;
                    break;
                }
            }
            if (needDelete) deletions++;
        }

        return deletions;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} strs
 * @return {number}
 */
var minDeletionSize = function(strs) {
    const n = strs.length;
    const m = strs[0].length;
    let deleteCount = 0;
    
    for (let col = 0; col < m; col++) {
        for (let row = 1; row < n; row++) {
            if (strs[row][col] < strs[row - 1][col]) {
                deleteCount++;
                break;
            }
        }
    }
    
    return deleteCount;
};
```

## Typescript

```typescript
function minDeletionSize(strs: string[]): number {
    const n = strs.length;
    const m = strs[0].length;
    let deletions = 0;
    for (let col = 0; col < m; col++) {
        for (let row = 1; row < n; row++) {
            if (strs[row][col] < strs[row - 1][col]) {
                deletions++;
                break;
            }
        }
    }
    return deletions;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $strs
     * @return Integer
     */
    function minDeletionSize($strs) {
        $n = count($strs);
        if ($n === 0) return 0;
        $m = strlen($strs[0]);
        $delete = 0;
        for ($col = 0; $col < $m; $col++) {
            for ($row = 1; $row < $n; $row++) {
                if ($strs[$row][$col] < $strs[$row - 1][$col]) {
                    $delete++;
                    break;
                }
            }
        }
        return $delete;
    }
}
```

## Swift

```swift
class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
        let n = strs.count
        guard n > 0 else { return 0 }
        let m = strs[0].count
        var rows = [[Character]]()
        rows.reserveCapacity(n)
        for s in strs {
            rows.append(Array(s))
        }
        var deletions = 0
        for col in 0..<m {
            var sorted = true
            for row in 1..<n {
                if rows[row][col] < rows[row - 1][col] {
                    sorted = false
                    break
                }
            }
            if !sorted { deletions += 1 }
        }
        return deletions
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDeletionSize(strs: Array<String>): Int {
        if (strs.isEmpty()) return 0
        val n = strs.size
        val m = strs[0].length
        var deletions = 0
        for (c in 0 until m) {
            var ok = true
            for (r in 1 until n) {
                if (strs[r][c] < strs[r - 1][c]) {
                    ok = false
                    break
                }
            }
            if (!ok) deletions++
        }
        return deletions
    }
}
```

## Dart

```dart
class Solution {
  int minDeletionSize(List<String> strs) {
    if (strs.isEmpty) return 0;
    int rows = strs.length;
    int cols = strs[0].length;
    int deleteCount = 0;

    for (int c = 0; c < cols; ++c) {
      bool sorted = true;
      for (int r = 1; r < rows; ++r) {
        if (strs[r].codeUnitAt(c) < strs[r - 1].codeUnitAt(c)) {
          sorted = false;
          break;
        }
      }
      if (!sorted) deleteCount++;
    }

    return deleteCount;
  }
}
```

## Golang

```go
func minDeletionSize(strs []string) int {
	if len(strs) == 0 {
		return 0
	}
	rows := len(strs)
	cols := len(strs[0])
	deletions := 0

	for c := 0; c < cols; c++ {
		for r := 1; r < rows; r++ {
			if strs[r][c] < strs[r-1][c] {
				deletions++
				break
			}
		}
	}
	return deletions
}
```

## Ruby

```ruby
def min_deletion_size(strs)
  return 0 if strs.empty?
  rows = strs.size
  cols = strs[0].size
  deletions = 0
  (0...cols).each do |c|
    (1...rows).each do |r|
      if strs[r][c] < strs[r - 1][c]
        deletions += 1
        break
      end
    end
  end
  deletions
end
```

## Scala

```scala
object Solution {
    def minDeletionSize(strs: Array[String]): Int = {
        val n = strs.length
        if (n == 0) return 0
        val m = strs(0).length
        var deletions = 0
        for (c <- 0 until m) {
            var sorted = true
            var i = 1
            while (i < n && sorted) {
                if (strs(i)(c) < strs(i - 1)(c)) sorted = false
                i += 1
            }
            if (!sorted) deletions += 1
        }
        deletions
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        if strs.is_empty() {
            return 0;
        }
        let n = strs.len();
        let m = strs[0].len();
        let rows: Vec<Vec<u8>> = strs.iter().map(|s| s.as_bytes().to_vec()).collect();

        let mut deletions = 0;
        for col in 0..m {
            let mut sorted = true;
            for row in 1..n {
                if rows[row][col] < rows[row - 1][col] {
                    sorted = false;
                    break;
                }
            }
            if !sorted {
                deletions += 1;
            }
        }
        deletions as i32
    }
}
```

## Racket

```racket
(define/contract (min-deletion-size strs)
  (-> (listof string?) exact-integer?)
  (let* ((vec (list->vector strs))
         (n (vector-length vec))
         (m (if (= n 0) 0 (string-length (vector-ref vec 0)))))
    (for/sum ([col (in-range m)])
      (let loop ((i 1))
        (cond
          [(= i n) 0]
          [else (if (< (char->integer (string-ref (vector-ref vec i) col))
                       (char->integer (string-ref (vector-ref vec (- i 1)) col)))
                    1
                    (loop (+ i 1))))])))))
```

## Erlang

```erlang
-spec min_deletion_size(Strs :: [unicode:unicode_binary()]) -> integer().
min_deletion_size(Strs) ->
    case Strs of
        [] -> 0;
        [First|_] ->
            L = byte_size(First),
            loop(0, L, Strs, 0)
    end.

loop(Index, Len, _Strs, Acc) when Index >= Len ->
    Acc;
loop(Index, Len, Strs, Acc) ->
    case column_unsorted(Index, Strs) of
        true -> loop(Index + 1, Len, Strs, Acc + 1);
        false -> loop(Index + 1, Len, Strs, Acc)
    end.

column_unsorted(Index, [First, Second | Rest]) ->
    Char1 = binary:at(First, Index),
    Char2 = binary:at(Second, Index),
    if
        Char1 =< Char2 -> column_unsorted(Index, [Second | Rest]);
        true -> true
    end;
column_unsorted(_, [_]) ->
    false.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_deletion_size(strs :: [String.t]) :: integer
  def min_deletion_size(strs) do
    m = String.length(List.first(strs))

    Enum.reduce(0..(m - 1), 0, fn col, del ->
      if column_unsorted?(strs, col) do
        del + 1
      else
        del
      end
    end)
  end

  defp column_unsorted?(strs, col) do
    Enum.reduce_while(1..(length(strs) - 1), false, fn i, _ ->
      prev = String.at(Enum.at(strs, i - 1), col)
      curr = String.at(Enum.at(strs, i), col)

      if prev <= curr do
        {:cont, false}
      else
        {:halt, true}
      end
    end)
  end
end
```
