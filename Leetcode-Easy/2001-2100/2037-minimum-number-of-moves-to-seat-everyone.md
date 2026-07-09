# 2037. Minimum Number of Moves to Seat Everyone

## Cpp

```cpp
class Solution {
public:
    int minMovesToSeat(vector<int>& seats, vector<int>& students) {
        sort(seats.begin(), seats.end());
        sort(students.begin(), students.end());
        int moves = 0;
        for (size_t i = 0; i < seats.size(); ++i) {
            moves += abs(seats[i] - students[i]);
        }
        return moves;
    }
};
```

## Java

```java
class Solution {
    public int minMovesToSeat(int[] seats, int[] students) {
        java.util.Arrays.sort(seats);
        java.util.Arrays.sort(students);
        int moves = 0;
        for (int i = 0; i < seats.length; i++) {
            moves += Math.abs(seats[i] - students[i]);
        }
        return moves;
    }
}
```

## Python

```python
class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        return sum(abs(s - t) for s, t in zip(seats, students))
```

## Python3

```python
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(s - t) for s, t in zip(seats, students))
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int minMovesToSeat(int* seats, int seatsSize, int* students, int studentsSize) {
    qsort(seats, (size_t)seatsSize, sizeof(int), cmp_int);
    qsort(students, (size_t)studentsSize, sizeof(int), cmp_int);
    
    int moves = 0;
    for (int i = 0; i < seatsSize; ++i) {
        int diff = seats[i] - students[i];
        if (diff < 0) diff = -diff;
        moves += diff;
    }
    return moves;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinMovesToSeat(int[] seats, int[] students)
    {
        Array.Sort(seats);
        Array.Sort(students);
        int moves = 0;
        for (int i = 0; i < seats.Length; i++)
        {
            moves += Math.Abs(seats[i] - students[i]);
        }
        return moves;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} seats
 * @param {number[]} students
 * @return {number}
 */
var minMovesToSeat = function(seats, students) {
    seats.sort((a, b) => a - b);
    students.sort((a, b) => a - b);
    let moves = 0;
    for (let i = 0; i < seats.length; ++i) {
        moves += Math.abs(seats[i] - students[i]);
    }
    return moves;
};
```

## Typescript

```typescript
function minMovesToSeat(seats: number[], students: number[]): number {
    seats.sort((a, b) => a - b);
    students.sort((a, b) => a - b);
    let moves = 0;
    for (let i = 0; i < seats.length; i++) {
        moves += Math.abs(seats[i] - students[i]);
    }
    return moves;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $seats
     * @param Integer[] $students
     * @return Integer
     */
    function minMovesToSeat($seats, $students) {
        sort($seats);
        sort($students);
        $moves = 0;
        $n = count($seats);
        for ($i = 0; $i < $n; $i++) {
            $moves += abs($seats[$i] - $students[$i]);
        }
        return $moves;
    }
}
```

## Swift

```swift
class Solution {
    func minMovesToSeat(_ seats: [Int], _ students: [Int]) -> Int {
        let sortedSeats = seats.sorted()
        let sortedStudents = students.sorted()
        var moves = 0
        for i in 0..<sortedSeats.count {
            moves += abs(sortedSeats[i] - sortedStudents[i])
        }
        return moves
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMovesToSeat(seats: IntArray, students: IntArray): Int {
        seats.sort()
        students.sort()
        var moves = 0
        for (i in seats.indices) {
            moves += kotlin.math.abs(seats[i] - students[i])
        }
        return moves
    }
}
```

## Dart

```dart
class Solution {
  int minMovesToSeat(List<int> seats, List<int> students) {
    seats.sort();
    students.sort();
    int moves = 0;
    for (int i = 0; i < seats.length; i++) {
      moves += (seats[i] - students[i]).abs();
    }
    return moves;
  }
}
```

## Golang

```go
package main

import "sort"

func minMovesToSeat(seats []int, students []int) int {
	sort.Ints(seats)
	sort.Ints(students)

	moves := 0
	for i := 0; i < len(seats); i++ {
		diff := seats[i] - students[i]
		if diff < 0 {
			diff = -diff
		}
		moves += diff
	}
	return moves
}
```

## Ruby

```ruby
def min_moves_to_seat(seats, students)
  seats.sort!
  students.sort!
  moves = 0
  seats.each_with_index do |seat, i|
    moves += (seat - students[i]).abs
  end
  moves
end
```

## Scala

```scala
object Solution {
    def minMovesToSeat(seats: Array[Int], students: Array[Int]): Int = {
        val sortedSeats = seats.sorted
        val sortedStudents = students.sorted
        var moves = 0
        for (i <- sortedSeats.indices) {
            moves += math.abs(sortedSeats(i) - sortedStudents(i))
        }
        moves
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_moves_to_seat(mut seats: Vec<i32>, mut students: Vec<i32>) -> i32 {
        seats.sort_unstable();
        students.sort_unstable();
        seats.iter()
            .zip(students.iter())
            .map(|(s, st)| (s - st).abs())
            .sum()
    }
}
```

## Racket

```racket
(define/contract (min-moves-to-seat seats students)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let ((sorted-seats (sort seats <))
        (sorted-students (sort students <)))
    (apply + (map (lambda (seat student) (abs (- seat student))) 
                  sorted-seats 
                  sorted-students))))
```

## Erlang

```erlang
-spec min_moves_to_seat(Seats :: [integer()], Students :: [integer()]) -> integer().
min_moves_to_seat(Seats, Students) ->
    SortedSeats = lists:sort(Seats),
    SortedStudents = lists:sort(Students),
    min_moves_to_seat(SortedSeats, SortedStudents, 0).

min_moves_to_seat([], [], Acc) -> Acc;
min_moves_to_seat([S|Ss], [St|Sts], Acc) ->
    min_moves_to_seat(Ss, Sts, Acc + abs(S - St)).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_moves_to_seat(seats :: [integer], students :: [integer]) :: integer
  def min_moves_to_seat(seats, students) do
    seats_sorted = Enum.sort(seats)
    students_sorted = Enum.sort(students)

    Enum.zip(seats_sorted, students_sorted)
    |> Enum.reduce(0, fn {seat, student}, acc -> acc + abs(seat - student) end)
  end
end
```
