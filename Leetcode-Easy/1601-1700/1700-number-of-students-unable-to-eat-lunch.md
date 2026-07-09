# 1700. Number of Students Unable to Eat Lunch

## Cpp

```cpp
class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int cnt[2] = {0, 0};
        for (int s : students) ++cnt[s];
        for (int sand : sandwiches) {
            if (cnt[sand] == 0) return cnt[1 - sand];
            --cnt[sand];
        }
        return 0;
    }
};
```

## Java

```java
class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int zeros = 0, ones = 0;
        for (int s : students) {
            if (s == 0) zeros++;
            else ones++;
        }
        for (int sand : sandwiches) {
            if (sand == 0) {
                if (zeros == 0) return ones;
                zeros--;
            } else {
                if (ones == 0) return zeros;
                ones--;
            }
        }
        return 0;
    }
}
```

## Python

```python
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        cnt0 = students.count(0)
        cnt1 = len(students) - cnt0
        for s in sandwiches:
            if s == 0:
                if cnt0 == 0:
                    return cnt1
                cnt0 -= 1
            else:
                if cnt1 == 0:
                    return cnt0
                cnt1 -= 1
        return 0
```

## Python3

```python
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = [0, 0]  # cnt[0]: circular, cnt[1]: square
        for s in students:
            cnt[s] += 1
        for sand in sandwiches:
            if cnt[sand] == 0:
                return cnt[1 - sand]
            cnt[sand] -= 1
        return 0
```

## C

```c
int countStudents(int* students, int studentsSize, int* sandwiches, int sandwichesSize) {
    int cnt[2] = {0, 0};
    for (int i = 0; i < studentsSize; ++i) {
        cnt[students[i]]++;
    }
    for (int i = 0; i < sandwichesSize; ++i) {
        int type = sandwiches[i];
        if (cnt[type] == 0) {
            return cnt[1 - type];
        }
        cnt[type]--;
    }
    return 0;
}
```

## Csharp

```csharp
public class Solution {
    public int CountStudents(int[] students, int[] sandwiches) {
        int countZero = 0, countOne = 0;
        foreach (int s in students) {
            if (s == 0) countZero++;
            else countOne++;
        }
        foreach (int sand in sandwiches) {
            if (sand == 0) {
                if (countZero == 0) return countOne;
                countZero--;
            } else {
                if (countOne == 0) return countZero;
                countOne--;
            }
        }
        return 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} students
 * @param {number[]} sandwiches
 * @return {number}
 */
var countStudents = function(students, sandwiches) {
    let cnt0 = 0, cnt1 = 0;
    for (const s of students) {
        if (s === 0) cnt0++;
        else cnt1++;
    }
    for (const sand of sandwiches) {
        if (sand === 0) {
            if (cnt0 === 0) return cnt1;
            cnt0--;
        } else {
            if (cnt1 === 0) return cnt0;
            cnt1--;
        }
    }
    return 0;
};
```

## Typescript

```typescript
function countStudents(students: number[], sandwiches: number[]): number {
    let circle = 0, square = 0;
    for (const s of students) {
        if (s === 0) circle++;
        else square++;
    }
    for (const sand of sandwiches) {
        if (sand === 0) {
            if (circle === 0) return square;
            circle--;
        } else {
            if (square === 0) return circle;
            square--;
        }
    }
    return 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $students
     * @param Integer[] $sandwiches
     * @return Integer
     */
    function countStudents($students, $sandwiches) {
        $cnt0 = 0; // students who prefer circular (0)
        $cnt1 = 0; // students who prefer square (1)

        foreach ($students as $s) {
            if ($s == 0) {
                $cnt0++;
            } else {
                $cnt1++;
            }
        }

        foreach ($sandwiches as $sand) {
            if ($sand == 0) {
                if ($cnt0 == 0) {
                    return $cnt1;
                }
                $cnt0--;
            } else { // sand == 1
                if ($cnt1 == 0) {
                    return $cnt0;
                }
                $cnt1--;
            }
        }

        return 0;
    }
}
```

## Swift

```swift
class Solution {
    func countStudents(_ students: [Int], _ sandwiches: [Int]) -> Int {
        var count = [0, 0] // count[0]: circular, count[1]: square
        for s in students {
            count[s] += 1
        }
        var i = 0
        while i < sandwiches.count {
            let sand = sandwiches[i]
            if count[sand] > 0 {
                count[sand] -= 1
                i += 1
            } else {
                // No student wants this sandwich type; remaining students cannot eat.
                return count[1 - sand]
            }
        }
        return 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countStudents(students: IntArray, sandwiches: IntArray): Int {
        var circle = 0
        var square = 0
        for (s in students) {
            if (s == 0) circle++ else square++
        }
        for (sand in sandwiches) {
            if (sand == 0) {
                if (circle == 0) return square
                circle--
            } else {
                if (square == 0) return circle
                square--
            }
        }
        return 0
    }
}
```

## Dart

```dart
class Solution {
  int countStudents(List<int> students, List<int> sandwiches) {
    int zeroCount = 0, oneCount = 0;
    for (var s in students) {
      if (s == 0) {
        zeroCount++;
      } else {
        oneCount++;
      }
    }
    for (var sand in sandwiches) {
      if (sand == 0) {
        if (zeroCount == 0) return oneCount;
        zeroCount--;
      } else {
        if (oneCount == 0) return zeroCount;
        oneCount--;
      }
    }
    return 0;
  }
}
```

## Golang

```go
func countStudents(students []int, sandwiches []int) int {
    cnt := [2]int{}
    for _, s := range students {
        cnt[s]++
    }
    for _, sand := range sandwiches {
        if cnt[sand] == 0 {
            return cnt[1-sand]
        }
        cnt[sand]--
    }
    return 0
}
```

## Ruby

```ruby
def count_students(students, sandwiches)
  cnt = [0, 0]
  students.each { |s| cnt[s] += 1 }
  sandwiches.each do |sand|
    return cnt[1 - sand] if cnt[sand] == 0
    cnt[sand] -= 1
  end
  0
end
```

## Scala

```scala
object Solution {
    def countStudents(students: Array[Int], sandwiches: Array[Int]): Int = {
        var cnt0 = 0
        var cnt1 = 0
        for (s <- students) {
            if (s == 0) cnt0 += 1 else cnt1 += 1
        }
        for (sand <- sandwiches) {
            if (sand == 0) {
                if (cnt0 == 0) return cnt1
                cnt0 -= 1
            } else {
                if (cnt1 == 0) return cnt0
                cnt1 -= 1
            }
        }
        0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_students(students: Vec<i32>, sandwiches: Vec<i32>) -> i32 {
        let mut cnt = [0i32; 2];
        for s in students {
            cnt[s as usize] += 1;
        }
        for sand in sandwiches {
            let idx = sand as usize;
            if cnt[idx] > 0 {
                cnt[idx] -= 1;
            } else {
                return cnt[1 - idx];
            }
        }
        0
    }
}
```

## Racket

```racket
(define/contract (count-students students sandwiches)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((circle-count
          (foldl (lambda (s acc) (if (= s 0) (+ acc 1) acc)) 0 students))
         (square-count
          (foldl (lambda (s acc) (if (= s 1) (+ acc 1) acc)) 0 students)))
    (let loop ((sandwiches sandwiches)
               (c circle-count)
               (sq square-count))
      (cond
        [(null? sandwiches) 0]
        [else
         (define sand (car sandwiches))
         (cond
           [(= sand 0)
            (if (> c 0)
                (loop (cdr sandwiches) (- c 1) sq)
                sq)]
           [(= sand 1)
            (if (> sq 0)
                (loop (cdr sandwiches) c (- sq 1))
                c)])]))))
```

## Erlang

```erlang
-spec count_students([integer()], [integer()]) -> integer().
count_students(Students, Sandwiches) ->
    {ZeroCount, OneCount} = lists:foldl(
        fun(S, {Z, O}) ->
            case S of
                0 -> {Z + 1, O};
                1 -> {Z, O + 1}
            end
        end,
        {0, 0},
        Students),
    serve(Sandwiches, ZeroCount, OneCount).

serve([], _Z, _O) ->
    0;
serve([S | Rest], Z, O) ->
    case S of
        0 ->
            if Z =:= 0 -> O;
               true -> serve(Rest, Z - 1, O)
            end;
        1 ->
            if O =:= 0 -> Z;
               true -> serve(Rest, Z, O - 1)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_students(students :: [integer], sandwiches :: [integer]) :: integer
  def count_students(students, sandwiches) do
    {cnt0, cnt1} = Enum.reduce(students, {0, 0}, fn s, {z, o} ->
      if s == 0, do: {z + 1, o}, else: {z, o + 1}
    end)

    serve(sandwiches, cnt0, cnt1)
  end

  defp serve([], _cnt0, _cnt1), do: 0

  defp serve([s | rest], cnt0, cnt1) do
    cond do
      s == 0 and cnt0 > 0 ->
        serve(rest, cnt0 - 1, cnt1)

      s == 1 and cnt1 > 0 ->
        serve(rest, cnt0, cnt1 - 1)

      s == 0 and cnt0 == 0 ->
        cnt1

      s == 1 and cnt1 == 0 ->
        cnt0
    end
  end
end
```
