# 1450. Number of Students Doing Homework at a Given Time

## Cpp

```cpp
class Solution {
public:
    int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
        int cnt = 0;
        for (size_t i = 0; i < startTime.size(); ++i) {
            if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
                ++cnt;
            }
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int busyStudent(int[] startTime, int[] endTime, int queryTime) {
        int count = 0;
        for (int i = 0; i < startTime.length; i++) {
            if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        count = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                count += 1
        return count
```

## C

```c
int busyStudent(int* startTime, int startTimeSize, int* endTime, int endTimeSize, int queryTime) {
    int count = 0;
    for (int i = 0; i < startTimeSize; ++i) {
        if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int BusyStudent(int[] startTime, int[] endTime, int queryTime) {
        int count = 0;
        for (int i = 0; i < startTime.Length; i++) {
            if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
                count++;
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @param {number} queryTime
 * @return {number}
 */
var busyStudent = function(startTime, endTime, queryTime) {
    let cnt = 0;
    for (let i = 0; i < startTime.length; ++i) {
        if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
            ++cnt;
        }
    }
    return cnt;
};
```

## Typescript

```typescript
function busyStudent(startTime: number[], endTime: number[], queryTime: number): number {
    let count = 0;
    for (let i = 0; i < startTime.length; i++) {
        if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
            count++;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $startTime
     * @param Integer[] $endTime
     * @param Integer $queryTime
     * @return Integer
     */
    function busyStudent($startTime, $endTime, $queryTime) {
        $count = 0;
        $n = count($startTime);
        for ($i = 0; $i < $n; $i++) {
            if ($startTime[$i] <= $queryTime && $queryTime <= $endTime[$i]) {
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func busyStudent(_ startTime: [Int], _ endTime: [Int], _ queryTime: Int) -> Int {
        var count = 0
        for (s, e) in zip(startTime, endTime) {
            if s <= queryTime && queryTime <= e {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun busyStudent(startTime: IntArray, endTime: IntArray, queryTime: Int): Int {
        var count = 0
        for (i in startTime.indices) {
            if (queryTime >= startTime[i] && queryTime <= endTime[i]) {
                count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int busyStudent(List<int> startTime, List<int> endTime, int queryTime) {
    int count = 0;
    for (int i = 0; i < startTime.length; i++) {
      if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func busyStudent(startTime []int, endTime []int, queryTime int) int {
    count := 0
    for i := range startTime {
        if startTime[i] <= queryTime && queryTime <= endTime[i] {
            count++
        }
    }
    return count
}
```

## Ruby

```ruby
def busy_student(start_time, end_time, query_time)
  count = 0
  start_time.each_with_index do |s, i|
    count += 1 if s <= query_time && query_time <= end_time[i]
  end
  count
end
```

## Scala

```scala
object Solution {
    def busyStudent(startTime: Array[Int], endTime: Array[Int], queryTime: Int): Int = {
        var count = 0
        for (i <- startTime.indices) {
            if (startTime(i) <= queryTime && queryTime <= endTime(i)) {
                count += 1
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn busy_student(start_time: Vec<i32>, end_time: Vec<i32>, query_time: i32) -> i32 {
        let mut count = 0;
        for (s, e) in start_time.iter().zip(end_time.iter()) {
            if *s <= query_time && query_time <= *e {
                count += 1;
            }
        }
        count
    }
}
```

## Racket

```racket
(define/contract (busy-student startTime endTime queryTime)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (for/sum ([s startTime] [e endTime])
    (if (and (<= s queryTime) (>= e queryTime)) 1 0)))
```

## Erlang

```erlang
-module(solution).
-export([busy_student/3]).

-spec busy_student(StartTime :: [integer()], EndTime :: [integer()], QueryTime :: integer()) -> integer().
busy_student(StartTime, EndTime, QueryTime) ->
    busy_student(StartTime, EndTime, QueryTime, 0).

busy_student([], [], _QueryTime, Acc) ->
    Acc;
busy_student([S|Ss], [E|Es], Q, Acc) ->
    NewAcc = if Q >= S, Q =< E -> Acc + 1; true -> Acc end,
    busy_student(Ss, Es, Q, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec busy_student(start_time :: [integer], end_time :: [integer], query_time :: integer) :: integer
  def busy_student(start_time, end_time, query_time) do
    Enum.zip(start_time, end_time)
    |> Enum.count(fn {s, e} -> s <= query_time and query_time <= e end)
  end
end
```
