# 3522. Calculate Score After Performing Instructions

## Cpp

```cpp
class Solution {
public:
    long long calculateScore(vector<string>& instructions, vector<int>& values) {
        int n = instructions.size();
        vector<char> visited(n, 0);
        long long score = 0;
        long long idx = 0; // use long long to avoid overflow in jumps
        while (idx >= 0 && idx < n && !visited[idx]) {
            visited[idx] = 1;
            if (instructions[idx] == "add") {
                score += values[idx];
                ++idx;
            } else { // "jump"
                idx += values[idx];
            }
        }
        return score;
    }
};
```

## Java

```java
class Solution {
    public long calculateScore(String[] instructions, int[] values) {
        int n = instructions.length;
        boolean[] visited = new boolean[n];
        long score = 0L;
        int idx = 0;
        while (idx >= 0 && idx < n && !visited[idx]) {
            visited[idx] = true;
            if ("add".equals(instructions[idx])) {
                score += values[idx];
                idx++;
            } else { // "jump"
                idx += values[idx];
            }
        }
        return score;
    }
}
```

## Python

```python
class Solution(object):
    def calculateScore(self, instructions, values):
        """
        :type instructions: List[str]
        :type values: List[int]
        :rtype: int
        """
        n = len(instructions)
        visited = [False] * n
        idx = 0
        score = 0
        while 0 <= idx < n and not visited[idx]:
            visited[idx] = True
            if instructions[idx] == "add":
                score += values[idx]
                idx += 1
            else:  # "jump"
                idx += values[idx]
        return score
```

## Python3

```python
from typing import List

class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)
        visited = [False] * n
        idx = 0
        score = 0
        while 0 <= idx < n and not visited[idx]:
            visited[idx] = True
            if instructions[idx] == "add":
                score += values[idx]
                idx += 1
            else:  # "jump"
                idx += values[idx]
        return score
```

## C

```c
#include <stdlib.h>
#include <string.h>

long long calculateScore(char** instructions, int instructionsSize, int* values, int valuesSize) {
    int n = instructionsSize;
    char *visited = (char *)calloc(n, sizeof(char));
    long long score = 0;
    int idx = 0;

    while (idx >= 0 && idx < n && !visited[idx]) {
        visited[idx] = 1;
        if (strcmp(instructions[idx], "add") == 0) {
            score += (long long)values[idx];
            idx += 1;
        } else { // "jump"
            idx += values[idx];
        }
    }

    free(visited);
    return score;
}
```

## Csharp

```csharp
public class Solution {
    public long CalculateScore(string[] instructions, int[] values) {
        int n = instructions.Length;
        bool[] visited = new bool[n];
        long score = 0;
        int i = 0;
        while (i >= 0 && i < n && !visited[i]) {
            visited[i] = true;
            if (instructions[i] == "add") {
                score += values[i];
                i++;
            } else { // "jump"
                i = i + values[i];
            }
        }
        return score;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} instructions
 * @param {number[]} values
 * @return {number}
 */
var calculateScore = function(instructions, values) {
    const n = instructions.length;
    const visited = new Array(n).fill(false);
    let i = 0;
    let score = 0;
    while (i >= 0 && i < n && !visited[i]) {
        visited[i] = true;
        if (instructions[i] === "add") {
            score += values[i];
            i += 1;
        } else { // "jump"
            i += values[i];
        }
    }
    return score;
};
```

## Typescript

```typescript
function calculateScore(instructions: string[], values: number[]): number {
    const n = instructions.length;
    const visited = new Uint8Array(n);
    let pos = 0;
    let score = 0;
    while (pos >= 0 && pos < n) {
        if (visited[pos]) break;
        visited[pos] = 1;
        if (instructions[pos] === "add") {
            score += values[pos];
            pos++;
        } else { // "jump"
            pos += values[pos];
        }
    }
    return score;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $instructions
     * @param Integer[] $values
     * @return Integer
     */
    function calculateScore($instructions, $values) {
        $n = count($instructions);
        $visited = array_fill(0, $n, false);
        $score = 0;
        $i = 0;
        while ($i >= 0 && $i < $n && !$visited[$i]) {
            $visited[$i] = true;
            if ($instructions[$i] === "add") {
                $score += $values[$i];
                $i++;
            } else { // "jump"
                $i += $values[$i];
            }
        }
        return $score;
    }
}
```

## Swift

```swift
class Solution {
    func calculateScore(_ instructions: [String], _ values: [Int]) -> Int {
        let n = instructions.count
        var visited = Array(repeating: false, count: n)
        var pos = 0
        var score = 0
        while pos >= 0 && pos < n && !visited[pos] {
            visited[pos] = true
            if instructions[pos] == "add" {
                score += values[pos]
                pos += 1
            } else { // "jump"
                pos += values[pos]
            }
        }
        return score
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun calculateScore(instructions: Array<String>, values: IntArray): Long {
        val n = instructions.size
        val visited = BooleanArray(n)
        var idx = 0
        var score = 0L
        while (idx in 0 until n && !visited[idx]) {
            visited[idx] = true
            if (instructions[idx] == "add") {
                score += values[idx].toLong()
                idx++
            } else { // "jump"
                idx += values[idx]
            }
        }
        return score
    }
}
```

## Dart

```dart
class Solution {
  int calculateScore(List<String> instructions, List<int> values) {
    int n = instructions.length;
    List<bool> visited = List.filled(n, false);
    int i = 0;
    int score = 0;
    while (i >= 0 && i < n && !visited[i]) {
      visited[i] = true;
      if (instructions[i] == "add") {
        score += values[i];
        i += 1;
      } else { // "jump"
        i += values[i];
      }
    }
    return score;
  }
}
```

## Golang

```go
func calculateScore(instructions []string, values []int) int64 {
	n := len(instructions)
	visited := make([]bool, n)
	idx := 0
	var score int64 = 0

	for {
		if idx < 0 || idx >= n {
			break
		}
		if visited[idx] {
			break
		}
		visited[idx] = true
		if instructions[idx] == "add" {
			score += int64(values[idx])
			idx++
		} else { // "jump"
			idx += values[idx]
		}
	}
	return score
}
```

## Ruby

```ruby
def calculate_score(instructions, values)
  n = instructions.length
  visited = Array.new(n, false)
  idx = 0
  score = 0

  while idx >= 0 && idx < n && !visited[idx]
    visited[idx] = true
    if instructions[idx] == "add"
      score += values[idx]
      idx += 1
    else # "jump"
      idx += values[idx]
    end
  end

  score
end
```

## Scala

```scala
object Solution {
    def calculateScore(instructions: Array[String], values: Array[Int]): Long = {
        val n = instructions.length
        val visited = new Array[Boolean](n)
        var idx = 0
        var score: Long = 0L
        while (idx >= 0 && idx < n && !visited(idx)) {
            visited(idx) = true
            if (instructions(idx) == "add") {
                score += values(idx).toLong
                idx += 1
            } else { // "jump"
                idx += values(idx)
            }
        }
        score
    }
}
```

## Rust

```rust
impl Solution {
    pub fn calculate_score(instructions: Vec<String>, values: Vec<i32>) -> i64 {
        let n = instructions.len();
        let mut visited = vec![false; n];
        let mut idx: i64 = 0;
        let mut score: i64 = 0;

        while idx >= 0 && (idx as usize) < n {
            let i = idx as usize;
            if visited[i] {
                break;
            }
            visited[i] = true;
            match instructions[i].as_str() {
                "add" => {
                    score += values[i] as i64;
                    idx += 1;
                }
                "jump" => {
                    idx += values[i] as i64;
                }
                _ => {}
            }
        }

        score
    }
}
```

## Racket

```racket
(define/contract (calculate-score instructions values)
  (-> (listof string?) (listof exact-integer?) exact-integer?)
  (let* ((n (length instructions))
         (instrV (list->vector instructions))
         (valV (list->vector values))
         (visited (make-vector n #f)))
    (let loop ((i 0) (score 0))
      (cond
        [(or (< i 0) (>= i n)) score]
        [(vector-ref visited i) score]
        [else
          (vector-set! visited i #t)
          (if (string=? (vector-ref instrV i) "add")
              (loop (+ i 1) (+ score (vector-ref valV i)))
              (loop (+ i (vector-ref valV i)) score))]))))
```

## Erlang

```erlang
-spec calculate_score([unicode:unicode_binary()], [integer()]) -> integer().
calculate_score(Instructions, Values) ->
    InstrT = list_to_tuple(Instructions),
    ValT = list_to_tuple(Values),
    loop(InstrT, ValT, #{}, 0, 0).

loop(_InstrT, _ValT, _Visited, Index, Score) when Index < 0; Index >= tuple_size(_InstrT) ->
    Score;
loop(InstrT, ValT, Visited, Index, Score) ->
    case maps:is_key(Index, Visited) of
        true -> Score;
        false ->
            Instr = element(Index + 1, InstrT),
            Value = element(Index + 1, ValT),
            NewVisited = maps:put(Index, true, Visited),
            case Instr of
                <<"add">> ->
                    loop(InstrT, ValT, NewVisited, Index + 1, Score + Value);
                <<"jump">> ->
                    loop(InstrT, ValT, NewVisited, Index + Value, Score)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec calculate_score(instructions :: [String.t()], values :: [integer]) :: integer
  def calculate_score(instructions, values) do
    n = length(instructions)
    instr_tuple = List.to_tuple(instructions)
    val_tuple = List.to_tuple(values)

    do_calc(0, 0, n, instr_tuple, val_tuple, %{})
  end

  defp do_calc(i, score, n, _instr, _vals, _visited) when i < 0 or i >= n, do: score

  defp do_calc(i, score, n, instr, vals, visited) do
    if Map.has_key?(visited, i) do
      score
    else
      visited = Map.put(visited, i, true)

      case elem(instr, i) do
        "add" ->
          new_score = score + elem(vals, i)
          do_calc(i + 1, new_score, n, instr, vals, visited)

        "jump" ->
          new_i = i + elem(vals, i)
          do_calc(new_i, score, n, instr, vals, visited)
      end
    end
  end
end
```
