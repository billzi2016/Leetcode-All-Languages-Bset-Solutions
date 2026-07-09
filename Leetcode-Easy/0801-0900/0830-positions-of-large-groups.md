# 0830. Positions of Large Groups

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> largeGroupPositions(string s) {
        vector<vector<int>> res;
        int n = s.size();
        for (int i = 0; i < n; ) {
            int j = i;
            while (j + 1 < n && s[j] == s[j + 1]) ++j;
            if (j - i + 1 >= 3) res.push_back({i, j});
            i = j + 1;
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public List<List<Integer>> largeGroupPositions(String s) {
        List<List<Integer>> res = new ArrayList<>();
        int n = s.length();
        int i = 0;
        while (i < n) {
            int j = i;
            while (j + 1 < n && s.charAt(j + 1) == s.charAt(i)) {
                j++;
            }
            if (j - i + 1 >= 3) {
                List<Integer> group = new ArrayList<>(2);
                group.add(i);
                group.add(j);
                res.add(group);
            }
            i = j + 1;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        n = len(s)
        res = []
        i = 0
        while i < n:
            j = i
            while j + 1 < n and s[j] == s[j + 1]:
                j += 1
            if j - i + 1 >= 3:
                res.append([i, j])
            i = j + 1
        return res
```

## Python3

```python
from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j + 1 < n and s[j] == s[j + 1]:
                j += 1
            if j - i + 1 >= 3:
                res.append([i, j])
            i = j + 1
        return res
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
int** largeGroupPositions(char* s, int* returnSize, int** returnColumnSizes) {
    int n = strlen(s);
    int maxGroups = n;  // upper bound
    int **res = (int **)malloc(sizeof(int *) * maxGroups);
    int *colSizes = (int *)malloc(sizeof(int) * maxGroups);
    int cnt = 0;
    
    for (int i = 0; i < n; ) {
        int j = i;
        while (j < n && s[j] == s[i]) {
            ++j;
        }
        if (j - i >= 3) {
            res[cnt] = (int *)malloc(2 * sizeof(int));
            res[cnt][0] = i;
            res[cnt][1] = j - 1;
            colSizes[cnt] = 2;
            ++cnt;
        }
        i = j;
    }
    
    *returnSize = cnt;
    *returnColumnSizes = colSizes;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<IList<int>> LargeGroupPositions(string s) {
        var result = new List<IList<int>>();
        int n = s.Length;
        int start = 0;
        for (int i = 1; i <= n; i++) {
            if (i == n || s[i] != s[i - 1]) {
                int length = i - start;
                if (length >= 3) {
                    result.Add(new List<int> { start, i - 1 });
                }
                start = i;
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number[][]}
 */
var largeGroupPositions = function(s) {
    const res = [];
    let n = s.length;
    let i = 0; // start of current group
    for (let j = 0; j < n; ++j) {
        if (j === n - 1 || s[j] !== s[j + 1]) {
            if (j - i + 1 >= 3) {
                res.push([i, j]);
            }
            i = j + 1;
        }
    }
    return res;
};
```

## Typescript

```typescript
function largeGroupPositions(s: string): number[][] {
    const result: number[][] = [];
    let i = 0;
    const n = s.length;
    while (i < n) {
        let j = i;
        while (j + 1 < n && s[j + 1] === s[i]) {
            j++;
        }
        if (j - i + 1 >= 3) {
            result.push([i, j]);
        }
        i = j + 1;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer[][]
     */
    function largeGroupPositions($s) {
        $n = strlen($s);
        $res = [];
        $i = 0;
        while ($i < $n) {
            $j = $i;
            while ($j + 1 < $n && $s[$j] === $s[$j + 1]) {
                $j++;
            }
            if ($j - $i + 1 >= 3) {
                $res[] = [$i, $j];
            }
            $i = $j + 1;
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func largeGroupPositions(_ s: String) -> [[Int]] {
        let chars = Array(s)
        var result: [[Int]] = []
        var i = 0
        let n = chars.count
        
        while i < n {
            var j = i
            while j + 1 < n && chars[j] == chars[j + 1] {
                j += 1
            }
            if j - i + 1 >= 3 {
                result.append([i, j])
            }
            i = j + 1
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largeGroupPositions(s: String): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        var i = 0
        val n = s.length
        while (i < n) {
            var j = i
            while (j + 1 < n && s[j] == s[j + 1]) {
                j++
            }
            if (j - i + 1 >= 3) {
                result.add(listOf(i, j))
            }
            i = j + 1
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> largeGroupPositions(String s) {
    List<List<int>> res = [];
    int n = s.length;
    int i = 0;
    while (i < n) {
      int j = i;
      while (j + 1 < n && s[j] == s[j + 1]) {
        j++;
      }
      if (j - i + 1 >= 3) {
        res.add([i, j]);
      }
      i = j + 1;
    }
    return res;
  }
}
```

## Golang

```go
func largeGroupPositions(s string) [][]int {
	n := len(s)
	var res [][]int
	start := 0
	for i := 0; i < n; i++ {
		if i == n-1 || s[i] != s[i+1] {
			if i-start+1 >= 3 {
				res = append(res, []int{start, i})
			}
			start = i + 1
		}
	}
	return res
}
```

## Ruby

```ruby
# @param {String} s
# @return {Integer[][]}
def large_group_positions(s)
  res = []
  i = 0
  n = s.length
  while i < n
    j = i
    while j + 1 < n && s[j] == s[j + 1]
      j += 1
    end
    if j - i + 1 >= 3
      res << [i, j]
    end
    i = j + 1
  end
  res
end
```

## Scala

```scala
object Solution {
    def largeGroupPositions(s: String): List[List[Int]] = {
        val result = scala.collection.mutable.ListBuffer[List[Int]]()
        var i = 0
        while (i < s.length) {
            var j = i
            while (j + 1 < s.length && s.charAt(j) == s.charAt(j + 1)) {
                j += 1
            }
            if (j - i + 1 >= 3) {
                result += List(i, j)
            }
            i = j + 1
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn large_group_positions(s: String) -> Vec<Vec<i32>> {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut i = 0;
        while i < n {
            let mut j = i;
            while j + 1 < n && bytes[j] == bytes[j + 1] {
                j += 1;
            }
            if j - i + 1 >= 3 {
                res.push(vec![i as i32, j as i32]);
            }
            i = j + 1;
        }
        res
    }
}
```

## Racket

```racket
(define/contract (large-group-positions s)
  (-> string? (listof (listof exact-integer?)))
  (let* ((n (string-length s))
         (ans
          (let loop ((i 0) (res '()))
            (if (>= i n)
                (reverse res)
                (let inner ((j i))
                  (if (or (= (+ j 1) n)
                          (not (char=? (string-ref s j) (string-ref s (+ j 1)))))
                      (if (>= (- j i) 2)
                          (loop (+ j 1) (cons (list i j) res))
                          (loop (+ j 1) res))
                      (inner (+ j 1))))))))
    ans))
```

## Erlang

```erlang
-spec large_group_positions(S :: unicode:unicode_binary()) -> [[integer()]].
large_group_positions(S) ->
    case S of
        <<>> -> [];
        <<First, Rest/binary>> ->
            helper(Rest, 1, First, 0, 1, [])
    end.

helper(<<>>, Index, _PrevChar, CurStart, CurLen, Acc) ->
    if CurLen >= 3 ->
            lists:reverse([[CurStart, Index - 1] | Acc]);
       true ->
            lists:reverse(Acc)
    end;
helper(<<Char, Rest/binary>>, Index, PrevChar, CurStart, CurLen, Acc) ->
    if Char =:= PrevChar ->
            helper(Rest, Index + 1, Char, CurStart, CurLen + 1, Acc);
       true ->
            NewAcc = case CurLen >= 3 of
                        true -> [[CurStart, Index - 1] | Acc];
                        false -> Acc
                     end,
            helper(Rest, Index + 1, Char, Index, 1, NewAcc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec large_group_positions(s :: String.t) :: [[integer]]
  def large_group_positions(s) do
    chars = String.graphemes(s)

    {acc_rev, state} =
      Enum.reduce(Enum.with_index(chars), {[], nil}, fn {c, idx}, {acc, st_state} ->
        case st_state do
          nil ->
            {acc, %{char: c, start: idx, count: 1}}

          %{char: prev_c, start: st, count: cnt} ->
            if c == prev_c do
              {acc, %{char: prev_c, start: st, count: cnt + 1}}
            else
              new_acc = if cnt >= 3, do: [[st, idx - 1] | acc], else: acc
              {new_acc, %{char: c, start: idx, count: 1}}
            end
        end
      end)

    final_acc_rev =
      case state do
        %{char: _, start: st, count: cnt} when cnt >= 3 ->
          [[st, length(chars) - 1] | acc_rev]

        _ ->
          acc_rev
      end

    Enum.reverse(final_acc_rev)
  end
end
```
