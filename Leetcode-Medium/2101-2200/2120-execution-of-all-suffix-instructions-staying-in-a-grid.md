# 2120. Execution of All Suffix Instructions Staying in a Grid

## Cpp

```cpp
class Solution {
public:
    vector<int> executeInstructions(int n, vector<int>& startPos, string s) {
        int m = s.size();
        vector<int> ans(m);
        for (int i = 0; i < m; ++i) {
            int r = startPos[0];
            int c = startPos[1];
            int cnt = 0;
            for (int j = i; j < m; ++j) {
                char ch = s[j];
                if (ch == 'L') --c;
                else if (ch == 'R') ++c;
                else if (ch == 'U') --r;
                else if (ch == 'D') ++r;
                
                if (r < 0 || r >= n || c < 0 || c >= n) break;
                ++cnt;
            }
            ans[i] = cnt;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] executeInstructions(int n, int[] startPos, String s) {
        int m = s.length();
        int[] answer = new int[m];
        for (int i = 0; i < m; i++) {
            int r = startPos[0];
            int c = startPos[1];
            int cnt = 0;
            for (int j = i; j < m; j++) {
                char ch = s.charAt(j);
                if (ch == 'L') {
                    c--;
                } else if (ch == 'R') {
                    c++;
                } else if (ch == 'U') {
                    r--;
                } else { // 'D'
                    r++;
                }
                if (r < 0 || r >= n || c < 0 || c >= n) {
                    break;
                }
                cnt++;
            }
            answer[i] = cnt;
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        m = len(s)
        ans = [0] * m
        for i in range(m):
            r, c = startPos[0], startPos[1]
            cnt = 0
            for j in range(i, m):
                ch = s[j]
                if ch == 'L':
                    c -= 1
                elif ch == 'R':
                    c += 1
                elif ch == 'U':
                    r -= 1
                else:  # 'D'
                    r += 1
                if 0 <= r < n and 0 <= c < n:
                    cnt += 1
                else:
                    break
            ans[i] = cnt
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        ans = []
        for i in range(m):
            r, c = startPos
            cnt = 0
            for ch in s[i:]:
                if ch == 'L':
                    c -= 1
                elif ch == 'R':
                    c += 1
                elif ch == 'U':
                    r -= 1
                else:  # 'D'
                    r += 1
                if 0 <= r < n and 0 <= c < n:
                    cnt += 1
                else:
                    break
            ans.append(cnt)
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* executeInstructions(int n, int* startPos, int startPosSize, char* s, int* returnSize) {
    int m = strlen(s);
    *returnSize = m;
    int* ans = (int*)malloc(sizeof(int) * m);
    for (int i = 0; i < m; ++i) {
        int r = startPos[0];
        int c = startPos[1];
        int cnt = 0;
        for (int j = i; j < m; ++j) {
            char ch = s[j];
            if (ch == 'L') c--;
            else if (ch == 'R') c++;
            else if (ch == 'U') r--;
            else if (ch == 'D') r++;
            if (r < 0 || r >= n || c < 0 || c >= n) break;
            ++cnt;
        }
        ans[i] = cnt;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] ExecuteInstructions(int n, int[] startPos, string s) {
        int m = s.Length;
        int[] ans = new int[m];
        for (int i = 0; i < m; ++i) {
            int r = startPos[0];
            int c = startPos[1];
            int cnt = 0;
            for (int j = i; j < m; ++j) {
                char ch = s[j];
                if (ch == 'L') c--;
                else if (ch == 'R') c++;
                else if (ch == 'U') r--;
                else if (ch == 'D') r++;
                
                if (r < 0 || r >= n || c < 0 || c >= n) break;
                cnt++;
            }
            ans[i] = cnt;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} startPos
 * @param {string} s
 * @return {number[]}
 */
var executeInstructions = function(n, startPos, s) {
    const m = s.length;
    const ans = new Array(m).fill(0);
    const dirMap = {
        'L': [0, -1],
        'R': [0, 1],
        'U': [-1, 0],
        'D': [1, 0]
    };
    for (let i = 0; i < m; ++i) {
        let r = startPos[0];
        let c = startPos[1];
        let cnt = 0;
        for (let j = i; j < m; ++j) {
            const [dr, dc] = dirMap[s[j]];
            r += dr;
            c += dc;
            if (r < 0 || r >= n || c < 0 || c >= n) break;
            ++cnt;
        }
        ans[i] = cnt;
    }
    return ans;
};
```

## Typescript

```typescript
function executeInstructions(n: number, startPos: number[], s: string): number[] {
    const m = s.length;
    const ans = new Array<number>(m);
    const dirMap: { [key: string]: [number, number] } = {
        'L': [0, -1],
        'R': [0, 1],
        'U': [-1, 0],
        'D': [1, 0]
    };
    for (let i = 0; i < m; i++) {
        let r = startPos[0];
        let c = startPos[1];
        let cnt = 0;
        for (let j = i; j < m; j++) {
            const ch = s[j];
            const [dr, dc] = dirMap[ch];
            r += dr;
            c += dc;
            if (r < 0 || r >= n || c < 0 || c >= n) break;
            cnt++;
        }
        ans[i] = cnt;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $startPos
     * @param String $s
     * @return Integer[]
     */
    function executeInstructions($n, $startPos, $s) {
        $len = strlen($s);
        $result = array_fill(0, $len, 0);
        for ($i = 0; $i < $len; $i++) {
            $r = $startPos[0];
            $c = $startPos[1];
            $cnt = 0;
            for ($j = $i; $j < $len; $j++) {
                $ch = $s[$j];
                switch ($ch) {
                    case 'L':
                        $c--;
                        break;
                    case 'R':
                        $c++;
                        break;
                    case 'U':
                        $r--;
                        break;
                    case 'D':
                        $r++;
                        break;
                }
                if ($r < 0 || $r >= $n || $c < 0 || $c >= $n) {
                    break;
                }
                $cnt++;
            }
            $result[$i] = $cnt;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func executeInstructions(_ n: Int, _ startPos: [Int], _ s: String) -> [Int] {
        let moves = Array(s)
        let m = moves.count
        var result = Array(repeating: 0, count: m)
        for i in 0..<m {
            var r = startPos[0]
            var c = startPos[1]
            var cnt = 0
            for j in i..<m {
                switch moves[j] {
                case "L":
                    c -= 1
                case "R":
                    c += 1
                case "U":
                    r -= 1
                case "D":
                    r += 1
                default:
                    break
                }
                if r < 0 || r >= n || c < 0 || c >= n {
                    break
                }
                cnt += 1
            }
            result[i] = cnt
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun executeInstructions(n: Int, startPos: IntArray, s: String): IntArray {
        val m = s.length
        val ans = IntArray(m)
        for (i in 0 until m) {
            var r = startPos[0]
            var c = startPos[1]
            var cnt = 0
            for (j in i until m) {
                when (s[j]) {
                    'L' -> c--
                    'R' -> c++
                    'U' -> r--
                    'D' -> r++
                }
                if (r < 0 || r >= n || c < 0 || c >= n) break
                cnt++
            }
            ans[i] = cnt
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> executeInstructions(int n, List<int> startPos, String s) {
    int m = s.length;
    List<int> answer = List.filled(m, 0);
    for (int i = 0; i < m; i++) {
      int r = startPos[0];
      int c = startPos[1];
      int cnt = 0;
      for (int j = i; j < m; j++) {
        switch (s[j]) {
          case 'L':
            c--;
            break;
          case 'R':
            c++;
            break;
          case 'U':
            r--;
            break;
          case 'D':
            r++;
            break;
        }
        if (r < 0 || r >= n || c < 0 || c >= n) {
          break;
        }
        cnt++;
      }
      answer[i] = cnt;
    }
    return answer;
  }
}
```

## Golang

```go
func executeInstructions(n int, startPos []int, s string) []int {
	m := len(s)
	ans := make([]int, m)
	for i := 0; i < m; i++ {
		row, col := startPos[0], startPos[1]
		cnt := 0
		for j := i; j < m; j++ {
			switch s[j] {
			case 'L':
				col--
			case 'R':
				col++
			case 'U':
				row--
			case 'D':
				row++
			}
			if row < 0 || row >= n || col < 0 || col >= n {
				break
			}
			cnt++
		}
		ans[i] = cnt
	}
	return ans
}
```

## Ruby

```ruby
def execute_instructions(n, start_pos, s)
  m = s.length
  ans = Array.new(m, 0)
  dirs = { 'L' => [0, -1], 'R' => [0, 1], 'U' => [-1, 0], 'D' => [1, 0] }

  (0...m).each do |i|
    r, c = start_pos
    cnt = 0
    j = i
    while j < m
      dr, dc = dirs[s[j]]
      nr = r + dr
      nc = c + dc
      break unless nr.between?(0, n - 1) && nc.between?(0, n - 1)
      r = nr
      c = nc
      cnt += 1
      j += 1
    end
    ans[i] = cnt
  end

  ans
end
```

## Scala

```scala
object Solution {
    def executeInstructions(n: Int, startPos: Array[Int], s: String): Array[Int] = {
        val m = s.length
        val ans = new Array[Int](m)
        for (i <- 0 until m) {
            var r = startPos(0)
            var c = startPos(1)
            var cnt = 0
            var j = i
            while (j < m) {
                val ch = s.charAt(j)
                var nr = r
                var nc = c
                ch match {
                    case 'L' => nc -= 1
                    case 'R' => nc += 1
                    case 'U' => nr -= 1
                    case 'D' => nr += 1
                }
                if (nr < 0 || nr >= n || nc < 0 || nc >= n) {
                    // out of bounds, stop processing this start index
                    j = m // break loop
                } else {
                    r = nr
                    c = nc
                    cnt += 1
                    j += 1
                }
            }
            ans(i) = cnt
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn execute_instructions(n: i32, start_pos: Vec<i32>, s: String) -> Vec<i32> {
        let bytes = s.as_bytes();
        let m = bytes.len();
        let mut ans = Vec::with_capacity(m);
        for i in 0..m {
            let (mut r, mut c) = (start_pos[0], start_pos[1]);
            let mut cnt = 0;
            for j in i..m {
                match bytes[j] {
                    b'L' => c -= 1,
                    b'R' => c += 1,
                    b'U' => r -= 1,
                    b'D' => r += 1,
                    _ => {}
                }
                if r < 0 || r >= n || c < 0 || c >= n {
                    break;
                } else {
                    cnt += 1;
                }
            }
            ans.push(cnt);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (execute-instructions n startPos s)
  (-> exact-integer? (listof exact-integer?) string? (listof exact-integer?))
  (let* ((len (string-length s))
         (start-row (first startPos))
         (start-col (second startPos)))
    (let loop-i ((i 0) (acc '()))
      (if (= i len)
          (reverse acc)
          (let ((cnt
                 (let inner-loop ((j i) (r start-row) (c start-col) (count 0))
                   (if (= j len)
                       count
                       (let* ((ch (string-ref s j))
                              (dr (cond [(char=? ch #\U) -1]
                                        [(char=? ch #\D) 1]
                                        [else 0]))
                              (dc (cond [(char=? ch #\L) -1]
                                        [(char=? ch #\R) 1]
                                        [else 0]))
                              (nr (+ r dr))
                              (nc (+ c dc)))
                         (if (or (< nr 0) (>= nr n) (< nc 0) (>= nc n))
                             count
                             (inner-loop (+ j 1) nr nc (+ count 1))))))))
            (loop-i (+ i 1) (cons cnt acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([execute_instructions/3]).
-spec execute_instructions(N :: integer(), StartPos :: [integer()], S :: unicode:unicode_binary()) -> [integer()].
execute_instructions(N, StartPos, S) ->
    Chars = binary_to_list(S),
    M = length(Chars),
    StartRow = hd(StartPos),
    StartCol = hd(tl(StartPos)),
    lists:reverse(exec_loop(0, M, Chars, N, StartRow, StartCol, [])).

exec_loop(I, M, _Chars, _N, _SR, _SC, Acc) when I >= M ->
    Acc;
exec_loop(I, M, Chars, N, SR, SC, Acc) ->
    Suffix = lists:sublist(Chars, I + 1),
    Count = simulate(Suffix, N, SR, SC, 0),
    exec_loop(I + 1, M, Chars, N, SR, SC, [Count | Acc]).

simulate([], _N, _Row, _Col, Count) ->
    Count;
simulate([C|Rest], N, Row, Col, Count) ->
    {NewRow, NewCol} =
        case C of
            $L -> {Row, Col - 1};
            $R -> {Row, Col + 1};
            $U -> {Row - 1, Col};
            $D -> {Row + 1, Col}
        end,
    if
        NewRow < 0 orelse NewRow >= N orelse NewCol < 0 orelse NewCol >= N ->
            Count;
        true ->
            simulate(Rest, N, NewRow, NewCol, Count + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec execute_instructions(integer, [integer], String.t()) :: [integer]
  def execute_instructions(n, [sr, sc], s) do
    moves = String.graphemes(s)
    m = length(moves)

    Enum.map(0..m - 1, fn i ->
      simulate(i, moves, n, sr, sc)
    end)
  end

  defp simulate(idx, moves, n, row, col) do
    len = length(moves)
    do_simulate(idx, moves, n, row, col, len, 0)
  end

  defp do_simulate(i, _moves, _n, _r, _c, len, cnt) when i >= len, do: cnt

  defp do_simulate(i, moves, n, r, c, len, cnt) do
    {nr, nc} =
      case Enum.at(moves, i) do
        "L" -> {r, c - 1}
        "R" -> {r, c + 1}
        "U" -> {r - 1, c}
        "D" -> {r + 1, c}
      end

    if nr < 0 or nr >= n or nc < 0 or nc >= n do
      cnt
    else
      do_simulate(i + 1, moves, n, nr, nc, len, cnt + 1)
    end
  end
end
```
