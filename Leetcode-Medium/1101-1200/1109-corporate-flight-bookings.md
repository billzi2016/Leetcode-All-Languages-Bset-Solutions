# 1109. Corporate Flight Bookings

## Cpp

```cpp
class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<long long> diff(n + 1, 0);
        for (const auto& b : bookings) {
            int first = b[0] - 1; // zero based
            int last = b[1] - 1;
            int seats = b[2];
            diff[first] += seats;
            if (last + 1 < n) diff[last + 1] -= seats;
        }
        vector<int> ans(n);
        long long cur = 0;
        for (int i = 0; i < n; ++i) {
            cur += diff[i];
            ans[i] = static_cast<int>(cur);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] diff = new int[n + 1];
        for (int[] b : bookings) {
            int start = b[0] - 1;
            int end = b[1] - 1;
            int seats = b[2];
            diff[start] += seats;
            if (end + 1 < n) {
                diff[end + 1] -= seats;
            }
        }
        int[] ans = new int[n];
        int cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            ans[i] = cur;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        diff = [0] * (n + 1)  # extra slot for easier handling of the end boundary
        for first, last, seats in bookings:
            diff[first - 1] += seats
            if last < n:
                diff[last] -= seats
        res = []
        cur = 0
        for i in range(n):
            cur += diff[i]
            res.append(cur)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        for first, last, seats in bookings:
            diff[first - 1] += seats
            if last < n:
                diff[last] -= seats
        res = []
        cur = 0
        for i in range(n):
            cur += diff[i]
            res.append(cur)
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* corpFlightBookings(int** bookings, int bookingsSize, int* bookingsColSize, int n, int* returnSize) {
    (void)bookingsColSize; // unused
    int *diff = (int *)calloc(n + 1, sizeof(int));
    for (int i = 0; i < bookingsSize; ++i) {
        int first = bookings[i][0] - 1;   // zero‑based index
        int last  = bookings[i][1] - 1;
        int seats = bookings[i][2];
        diff[first] += seats;
        if (last + 1 < n)
            diff[last + 1] -= seats;
    }
    
    int *ans = (int *)malloc(n * sizeof(int));
    int cur = 0;
    for (int i = 0; i < n; ++i) {
        cur += diff[i];
        ans[i] = cur;
    }
    
    free(diff);
    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] CorpFlightBookings(int[][] bookings, int n)
    {
        int[] diff = new int[n + 1];
        foreach (var b in bookings)
        {
            int start = b[0] - 1;
            int end = b[1] - 1;
            int seats = b[2];
            diff[start] += seats;
            if (end + 1 < n) diff[end + 1] -= seats;
        }

        int[] result = new int[n];
        int cur = 0;
        for (int i = 0; i < n; i++)
        {
            cur += diff[i];
            result[i] = cur;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} bookings
 * @param {number} n
 * @return {number[]}
 */
var corpFlightBookings = function(bookings, n) {
    const diff = new Array(n + 1).fill(0);
    for (const [first, last, seats] of bookings) {
        diff[first - 1] += seats;
        diff[last] -= seats;
    }
    const result = new Array(n);
    let cur = 0;
    for (let i = 0; i < n; ++i) {
        cur += diff[i];
        result[i] = cur;
    }
    return result;
};
```

## Typescript

```typescript
function corpFlightBookings(bookings: number[][], n: number): number[] {
    const diff = new Array<number>(n + 1).fill(0);
    for (const [first, last, seats] of bookings) {
        diff[first - 1] += seats;
        diff[last] -= seats;
    }
    const answer = new Array<number>(n);
    let cur = 0;
    for (let i = 0; i < n; i++) {
        cur += diff[i];
        answer[i] = cur;
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $bookings
     * @param Integer $n
     * @return Integer[]
     */
    function corpFlightBookings($bookings, $n) {
        // Difference array of size n+1 (extra slot for easier handling)
        $diff = array_fill(0, $n + 1, 0);
        
        foreach ($bookings as $b) {
            $first = $b[0] - 1;   // convert to 0‑based index
            $last  = $b[1];       // keep as exclusive upper bound in diff array
            $seats = $b[2];
            
            $diff[$first] += $seats;
            if ($last < $n) {
                $diff[$last] -= $seats;
            }
        }
        
        $result = [];
        $curr = 0;
        for ($i = 0; $i < $n; $i++) {
            $curr += $diff[$i];
            $result[] = $curr;
        }
        
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func corpFlightBookings(_ bookings: [[Int]], _ n: Int) -> [Int] {
        var diff = Array(repeating: 0, count: n + 1)
        for booking in bookings {
            let start = booking[0] - 1
            let end = booking[1] - 1
            let seats = booking[2]
            diff[start] += seats
            if end + 1 < n {
                diff[end + 1] -= seats
            }
        }
        var result = Array(repeating: 0, count: n)
        var current = 0
        for i in 0..<n {
            current += diff[i]
            result[i] = current
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun corpFlightBookings(bookings: Array<IntArray>, n: Int): IntArray {
        val diff = IntArray(n + 1)
        for (b in bookings) {
            val start = b[0] - 1
            val end = b[1]
            val seats = b[2]
            diff[start] += seats
            diff[end] -= seats
        }
        val ans = IntArray(n)
        var cur = 0
        for (i in 0 until n) {
            cur += diff[i]
            ans[i] = cur
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> corpFlightBookings(List<List<int>> bookings, int n) {
    List<int> diff = List.filled(n + 1, 0);
    for (var b in bookings) {
      int first = b[0];
      int last = b[1];
      int seats = b[2];
      diff[first - 1] += seats;
      if (last < n) diff[last] -= seats;
    }
    List<int> ans = List.filled(n, 0);
    int cur = 0;
    for (int i = 0; i < n; ++i) {
      cur += diff[i];
      ans[i] = cur;
    }
    return ans;
  }
}
```

## Golang

```go
func corpFlightBookings(bookings [][]int, n int) []int {
	diff := make([]int, n+1)
	for _, b := range bookings {
		start := b[0] - 1
		end := b[1]
		seats := b[2]
		diff[start] += seats
		if end < n {
			diff[end] -= seats
		}
	}
	ans := make([]int, n)
	cur := 0
	for i := 0; i < n; i++ {
		cur += diff[i]
		ans[i] = cur
	}
	return ans
}
```

## Ruby

```ruby
def corp_flight_bookings(bookings, n)
  diff = Array.new(n + 1, 0)
  bookings.each do |first, last, seats|
    diff[first - 1] += seats
    diff[last] -= seats if last < n
  end
  result = []
  cur = 0
  (0...n).each do |i|
    cur += diff[i]
    result << cur
  end
  result
end
```

## Scala

```scala
object Solution {
    def corpFlightBookings(bookings: Array[Array[Int]], n: Int): Array[Int] = {
        val diff = new Array[Int](n + 1)
        for (b <- bookings) {
            val first = b(0) - 1
            val last = b(1) - 1
            val seats = b(2)
            diff(first) += seats
            if (last + 1 < n) diff(last + 1) -= seats
        }
        val res = new Array[Int](n)
        var cur = 0
        for (i <- 0 until n) {
            cur += diff(i)
            res(i) = cur
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn corp_flight_bookings(bookings: Vec<Vec<i32>>, n: i32) -> Vec<i32> {
        let n_usize = n as usize;
        let mut diff = vec![0i64; n_usize + 1];
        for b in bookings.iter() {
            let first = b[0] as usize;
            let last = b[1] as usize;
            let seats = b[2] as i64;
            diff[first - 1] += seats;
            if last < n_usize {
                diff[last] -= seats;
            }
        }
        let mut ans = Vec::with_capacity(n_usize);
        let mut cur: i64 = 0;
        for i in 0..n_usize {
            cur += diff[i];
            ans.push(cur as i32);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (corp-flight-bookings bookings n)
  (-> (listof (listof exact-integer?)) exact-integer? (listof exact-integer?))
  (let* ((diff (make-vector (+ n 1) 0)))
    (for ([b bookings])
      (match-define (list first last seats) b)
      (vector-set! diff (- first 1) (+ (vector-ref diff (- first 1)) seats))
      (when (< last n)
        (vector-set! diff last (- (vector-ref diff last) seats))))
    (let loop ((i 0) (curr 0) (res '()))
      (if (= i n)
          (reverse res)
          (let ((new (+ curr (vector-ref diff i))))
            (loop (add1 i) new (cons new res)))))))
```

## Erlang

```erlang
-module(solution).
-export([corp_flight_bookings/2]).

-spec corp_flight_bookings(Bookings :: [[integer()]], N :: integer()) -> [integer()].
corp_flight_bookings(Bookings, N) ->
    Diff0 = array:new(N + 2, {default, 0}),
    Diff = lists:foldl(
        fun([First, Last, Seats], Acc) ->
            Acc1 = array:set(First,
                             array:get(First, Acc) + Seats,
                             Acc),
            case Last + 1 =< N of
                true ->
                    array:set(Last + 1,
                              array:get(Last + 1, Acc1) - Seats,
                              Acc1);
                false -> Acc1
            end
        end,
        Diff0,
        Bookings),
    build_prefix(1, 0, Diff, N, []).

build_prefix(Index, PrevSum, _Diff, N, Acc) when Index > N ->
    lists:reverse(Acc);
build_prefix(Index, PrevSum, Diff, N, Acc) ->
    Val = array:get(Index, Diff),
    NewSum = PrevSum + Val,
    build_prefix(Index + 1, NewSum, Diff, N, [NewSum | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec corp_flight_bookings(bookings :: [[integer]], n :: integer) :: [integer]
  def corp_flight_bookings(bookings, n) do
    diff =
      Enum.reduce(bookings, %{}, fn [first, last, seats], acc ->
        start_idx = first - 1
        end_idx = last

        acc
        |> Map.update(start_idx, seats, &(&1 + seats))
        |> Map.update(end_idx, -seats, &(&1 - seats))
      end)

    {result, _} =
      Enum.reduce(0..(n - 1), {[], 0}, fn i, {list, cur} ->
        cur = cur + Map.get(diff, i, 0)
        {[cur | list], cur}
      end)

    Enum.reverse(result)
  end
end
```
