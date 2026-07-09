# 0955. Delete Columns to Make Sorted II

## Cpp

```cpp
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs.size();
        if (n <= 1) return 0;
        int m = strs[0].size();
        vector<bool> resolved(n - 1, false);
        int deletions = 0;
        for (int col = 0; col < m; ++col) {
            bool deleteCol = false;
            for (int i = 0; i < n - 1; ++i) {
                if (!resolved[i] && strs[i][col] > strs[i + 1][col]) {
                    deleteCol = true;
                    break;
                }
            }
            if (deleteCol) {
                ++deletions;
                continue;
            }
            for (int i = 0; i < n - 1; ++i) {
                if (!resolved[i] && strs[i][col] < strs[i + 1][col]) {
                    resolved[i] = true;
                }
            }
        }
        return deletions;
    }
};
```

## Java

```java
class Solution {
    public int minDeletionSize(String[] strs) {
        int n = strs.length;
        if (n <= 1) return 0;
        int m = strs[0].length();
        boolean[] sorted = new boolean[n - 1];
        int deletions = 0;

        for (int col = 0; col < m; col++) {
            boolean delete = false;
            for (int i = 0; i < n - 1; i++) {
                if (!sorted[i] && strs[i].charAt(col) > strs[i + 1].charAt(col)) {
                    delete = true;
                    break;
                }
            }
            if (delete) {
                deletions++;
            } else {
                for (int i = 0; i < n - 1; i++) {
                    if (!sorted[i] && strs[i].charAt(col) < strs[i + 1].charAt(col)) {
                        sorted[i] = true;
                    }
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
        n = len(strs)
        if n <= 1:
            return 0
        m = len(strs[0])
        sorted_pair = [False] * (n - 1)  # whether row i < row i+1 is already determined
        deletions = 0

        for col in range(m):
            delete = False
            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] > strs[i + 1][col]:
                    delete = True
                    break
            if delete:
                deletions += 1
                continue
            # keep column, update resolved pairs
            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pair[i] = True
        return deletions
```

## Python3

```python
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        if n <= 1:
            return 0
        m = len(strs[0])
        sorted_pair = [False] * (n - 1)  # True if order already decided for this adjacent pair
        deletions = 0

        for col in range(m):
            # Check if keeping this column would break ordering
            need_delete = False
            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] > strs[i + 1][col]:
                    need_delete = True
                    break
            if need_delete:
                deletions += 1
                continue

            # Update sorted pairs where this column resolves order
            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pair[i] = True

            # If all pairs are resolved, we can stop early
            if all(sorted_pair):
                break

        return deletions
```

## C

```c
#include <string.h>
#include <stdlib.h>

int minDeletionSize(char** strs, int strsSize) {
    if (strsSize <= 1) return 0;
    int n = strsSize;
    int m = strlen(strs[0]);
    int *sorted = (int *)calloc(n - 1, sizeof(int));
    int deletions = 0;

    for (int col = 0; col < m; ++col) {
        int needDelete = 0;
        for (int i = 0; i < n - 1; ++i) {
            if (!sorted[i] && strs[i][col] > strs[i + 1][col]) {
                needDelete = 1;
                break;
            }
        }
        if (needDelete) {
            ++deletions;
            continue;
        }
        for (int i = 0; i < n - 1; ++i) {
            if (!sorted[i] && strs[i][col] < strs[i + 1][col]) {
                sorted[i] = 1;
            }
        }
    }

    free(sorted);
    return deletions;
}
```

## Csharp

```csharp
public class Solution {
    public int MinDeletionSize(string[] strs) {
        int n = strs.Length;
        if (n <= 1) return 0;
        int m = strs[0].Length;
        bool[] sorted = new bool[n - 1];
        int deletions = 0;

        for (int col = 0; col < m; col++) {
            bool needDelete = false;
            for (int i = 0; i < n - 1; i++) {
                if (!sorted[i] && strs[i][col] > strs[i + 1][col]) {
                    needDelete = true;
                    break;
                }
            }

            if (needDelete) {
                deletions++;
                continue;
            }

            for (int i = 0; i < n - 1; i++) {
                if (!sorted[i] && strs[i][col] < strs[i + 1][col]) {
                    sorted[i] = true;
                }
            }

            bool allSorted = true;
            for (int i = 0; i < n - 1; i++) {
                if (!sorted[i]) {
                    allSorted = false;
                    break;
                }
            }
            if (allSorted) break;
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
    if (n <= 1) return 0;
    const m = strs[0].length;
    const sorted = new Array(n - 1).fill(false);
    let deletions = 0;

    for (let col = 0; col < m; col++) {
        let needDelete = false;
        for (let i = 0; i < n - 1; i++) {
            if (!sorted[i] && strs[i][col] > strs[i + 1][col]) {
                needDelete = true;
                break;
            }
        }
        if (needDelete) {
            deletions++;
        } else {
            for (let i = 0; i < n - 1; i++) {
                if (!sorted[i] && strs[i][col] < strs[i + 1][col]) {
                    sorted[i] = true;
                }
            }
        }
    }

    return deletions;
};
```

## Typescript

```typescript
function minDeletionSize(strs: string[]): number {
    const n = strs.length;
    if (n <= 1) return 0;
    const m = strs[0].length;
    const sorted = new Array(n - 1).fill(false);
    let deletions = 0;

    for (let col = 0; col < m; col++) {
        let deleteCol = false;
        for (let i = 0; i < n - 1; i++) {
            if (!sorted[i] && strs[i][col] > strs[i + 1][col]) {
                deleteCol = true;
                break;
            }
        }
        if (deleteCol) {
            deletions++;
        } else {
            for (let i = 0; i < n - 1; i++) {
                if (!sorted[i] && strs[i][col] < strs[i + 1][col]) {
                    sorted[i] = true;
                }
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
        if ($n <= 1) return 0;
        $m = strlen($strs[0]);
        $sorted = array_fill(0, $n - 1, false);
        $ans = 0;

        for ($col = 0; $col < $m; $col++) {
            $needDelete = false;
            for ($i = 0; $i < $n - 1; $i++) {
                if (!$sorted[$i] && $strs[$i][$col] > $strs[$i + 1][$col]) {
                    $needDelete = true;
                    break;
                }
            }

            if ($needDelete) {
                $ans++;
                continue;
            }

            for ($i = 0; $i < $n - 1; $i++) {
                if (!$sorted[$i] && $strs[$i][$col] < $strs[$i + 1][$col]) {
                    $sorted[$i] = true;
                }
            }

            // optional early exit if all pairs are sorted
            $allSorted = true;
            foreach ($sorted as $flag) {
                if (!$flag) { $allSorted = false; break; }
            }
            if ($allSorted) break;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
        let n = strs.count
        if n <= 1 { return 0 }
        var rows = [[UInt8]]()
        rows.reserveCapacity(n)
        for s in strs {
            rows.append(Array(s.utf8))
        }
        let m = rows[0].count
        var resolved = Array(repeating: false, count: n - 1)
        var deletions = 0
        
        for col in 0..<m {
            var deleteCol = false
            for i in 0..<(n - 1) {
                if !resolved[i] && rows[i][col] > rows[i + 1][col] {
                    deleteCol = true
                    break
                }
            }
            if deleteCol {
                deletions += 1
                continue
            }
            for i in 0..<(n - 1) {
                if !resolved[i] && rows[i][col] < rows[i + 1][col] {
                    resolved[i] = true
                }
            }
        }
        return deletions
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDeletionSize(strs: Array<String>): Int {
        val n = strs.size
        if (n <= 1) return 0
        val m = strs[0].length
        val sorted = BooleanArray(n - 1)
        var deletions = 0
        for (c in 0 until m) {
            var needDelete = false
            for (i in 0 until n - 1) {
                if (!sorted[i] && strs[i][c] > strs[i + 1][c]) {
                    needDelete = true
                    break
                }
            }
            if (needDelete) {
                deletions++
            } else {
                for (i in 0 until n - 1) {
                    if (!sorted[i] && strs[i][c] < strs[i + 1][c]) {
                        sorted[i] = true
                    }
                }
            }
        }
        return deletions
    }
}
```

## Dart

```dart
class Solution {
  int minDeletionSize(List<String> strs) {
    int n = strs.length;
    if (n <= 1) return 0;
    int m = strs[0].length;
    List<bool> sorted = List.filled(n - 1, false);
    int deletions = 0;

    for (int col = 0; col < m; col++) {
      bool needDelete = false;
      for (int i = 0; i < n - 1; i++) {
        if (!sorted[i]) {
          int c1 = strs[i].codeUnitAt(col);
          int c2 = strs[i + 1].codeUnitAt(col);
          if (c1 > c2) {
            needDelete = true;
            break;
          }
        }
      }

      if (needDelete) {
        deletions++;
        continue;
      }

      for (int i = 0; i < n - 1; i++) {
        if (!sorted[i]) {
          int c1 = strs[i].codeUnitAt(col);
          int c2 = strs[i + 1].codeUnitAt(col);
          if (c1 < c2) {
            sorted[i] = true;
          }
        }
      }

      bool allSorted = true;
      for (bool s in sorted) {
        if (!s) {
          allSorted = false;
          break;
        }
      }
      if (allSorted) break;
    }

    return deletions;
  }
}
```

## Golang

```go
func minDeletionSize(strs []string) int {
	if len(strs) == 0 {
		return 0
	}
	n := len(strs)
	m := len(strs[0])
	sorted := make([]bool, n-1)
	deletions := 0

	for col := 0; col < m; col++ {
		needDelete := false
		for i := 0; i < n-1; i++ {
			if !sorted[i] && strs[i][col] > strs[i+1][col] {
				needDelete = true
				break
			}
		}
		if needDelete {
			deletions++
			continue
		}
		for i := 0; i < n-1; i++ {
			if !sorted[i] && strs[i][col] < strs[i+1][col] {
				sorted[i] = true
			}
		}
	}
	return deletions
}
```

## Ruby

```ruby
def min_deletion_size(strs)
  n = strs.length
  return 0 if n <= 1
  m = strs[0].length
  resolved = Array.new(n - 1, false)
  deletions = 0

  (0...m).each do |col|
    need_delete = false
    (0...(n - 1)).each do |i|
      next if resolved[i]
      if strs[i].getbyte(col) > strs[i + 1].getbyte(col)
        need_delete = true
        break
      end
    end

    if need_delete
      deletions += 1
    else
      (0...(n - 1)).each do |i|
        next if resolved[i]
        if strs[i].getbyte(col) < strs[i + 1].getbyte(col)
          resolved[i] = true
        end
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
        if (n <= 1) return 0
        val m = strs(0).length
        var deletions = 0
        val resolved = Array.fill(n - 1)(false)

        for (col <- 0 until m) {
            var needDelete = false
            var i = 0
            while (i < n - 1 && !needDelete) {
                if (!resolved(i)) {
                    val c1 = strs(i).charAt(col)
                    val c2 = strs(i + 1).charAt(col)
                    if (c1 > c2) needDelete = true
                }
                i += 1
            }

            if (needDelete) {
                deletions += 1
            } else {
                var j = 0
                while (j < n - 1) {
                    if (!resolved(j)) {
                        val c1 = strs(j).charAt(col)
                        val c2 = strs(j + 1).charAt(col)
                        if (c1 < c2) resolved(j) = true
                    }
                    j += 1
                }
            }
        }

        deletions
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let n = strs.len();
        if n <= 1 {
            return 0;
        }
        let m = strs[0].len();
        let rows: Vec<Vec<u8>> = strs.iter().map(|s| s.as_bytes().to_vec()).collect();

        let mut sorted = vec![false; n - 1];
        let mut deletions = 0;

        for col in 0..m {
            // Determine if this column must be deleted
            let mut delete = false;
            for i in 0..n - 1 {
                if !sorted[i] && rows[i][col] > rows[i + 1][col] {
                    delete = true;
                    break;
                }
            }
            if delete {
                deletions += 1;
                continue;
            }

            // Keep column and update ordering information
            for i in 0..n - 1 {
                if !sorted[i] && rows[i][col] < rows[i + 1][col] {
                    sorted[i] = true;
                }
            }

            // If all pairs are already ordered, we can stop early
            if sorted.iter().all(|&v| v) {
                break;
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
  (let* ((n (length strs))
         (v (list->vector strs)))
    (if (= n 1)
        0
        (let* ((m (string-length (vector-ref v 0)))
               (resolved (make-vector (- n 1) #f)))
          (let loop ((col 0) (deletions 0) (rcount 0))
            (cond
              [(or (= col m) (= rcount (- n 1))) deletions]
              [else
               (define need-delete #f)
               (for ([i (in-range (- n 1))]
                     #:when (not need-delete))
                 (unless (vector-ref resolved i)
                   (let* ((c1 (string-ref (vector-ref v i) col))
                          (c2 (string-ref (vector-ref v (+ i 1)) col)))
                     (when (char>? c1 c2)
                       (set! need-delete #t)))))
               (if need-delete
                   (loop (+ col 1) (+ deletions 1) rcount)
                   (let ((new-rcount rcount))
                     (for ([i (in-range (- n 1))])
                       (when (and (not (vector-ref resolved i))
                                  (char<? (string-ref (vector-ref v i) col)
                                          (string-ref (vector-ref v (+ i 1)) col)))
                         (vector-set! resolved i #t)
                         (set! new-rcount (+ new-rcount 1))))
                     (loop (+ col 1) deletions new-rcount))))])))))
```

## Erlang

```erlang
-module(solution).
-export([min_deletion_size/1]).

-spec min_deletion_size(Strs :: [unicode:unicode_binary()]) -> integer().
min_deletion_size(Strs) ->
    N = length(Strs),
    case N =< 1 of
        true -> 0;
        false ->
            M = byte_size(hd(Strs)),
            Unresolved = lists:seq(0, N - 2),
            process(0, Unresolved, 0, Strs, M)
    end.

process(_J, [], Del, _Strs, _M) -> Del;
process(J, Unresolved, Del, Strs, M) when J == M -> Del;
process(J, Unresolved, Del, Strs, M) ->
    case need_delete(J, Unresolved, Strs) of
        true ->
            process(J + 1, Unresolved, Del + 1, Strs, M);
        false ->
            NewUnresolved = filter_unresolved(J, Unresolved, Strs),
            process(J + 1, NewUnresolved, Del, Strs, M)
    end.

need_delete(_J, [], _Strs) -> false;
need_delete(J, Unresolved, Strs) ->
    lists:any(
        fun(I) ->
            CharI = binary:at(lists:nth(I + 1, Strs), J),
            CharNext = binary:at(lists:nth(I + 2, Strs), J),
            CharI > CharNext
        end,
        Unresolved).

filter_unresolved(J, Unresolved, Strs) ->
    [I ||
        I <- Unresolved,
        binary:at(lists:nth(I + 1, Strs), J) == binary:at(lists:nth(I + 2, Strs), J)
    ].
```

## Elixir

```elixir
defmodule Solution do
  @spec min_deletion_size(strs :: [String.t()]) :: integer()
  def min_deletion_size(strs) do
    n = length(strs)
    m = String.length(hd strs)
    sorted = List.duplicate(false, max(n - 1, 0))

    {ans, _} =
      Enum.reduce(0..(m - 1), {0, sorted}, fn col, {del, sorted_acc} ->
        need_delete =
          Enum.any?(0..(n - 2), fn i ->
            not Enum.at(sorted_acc, i) and
              :binary.at(Enum.at(strs, i), col) > :binary.at(Enum.at(strs, i + 1), col)
          end)

        if need_delete do
          {del + 1, sorted_acc}
        else
          new_sorted =
            Enum.map(0..(n - 2), fn i ->
              if not Enum.at(sorted_acc, i) and
                   :binary.at(Enum.at(strs, i), col) < :binary.at(Enum.at(strs, i + 1), col) do
                true
              else
                Enum.at(sorted_acc, i)
              end
            end)

          {del, new_sorted}
        end
      end)

    ans
  end
end
```
