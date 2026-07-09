# 1744. Can You Eat Your Favorite Candy on Your Favorite Day?

## Cpp

```cpp
class Solution {
public:
    vector<bool> canEat(vector<int>& candiesCount, vector<vector<int>>& queries) {
        int n = candiesCount.size();
        vector<long long> pref(n);
        for (int i = 0; i < n; ++i) {
            pref[i] = candiesCount[i] + (i ? pref[i-1] : 0LL);
        }
        vector<bool> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            int type = q[0];
            long long day = q[1];
            long long cap = q[2];
            
            long long before = (type == 0 ? 0LL : pref[type-1]);
            long long earliestDay = (before + cap - 1) / cap; // ceil division
            long long latestDay = pref[type] - 1;
            
            ans.push_back(day >= earliestDay && day <= latestDay);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public boolean[] canEat(int[] candiesCount, int[][] queries) {
        int n = candiesCount.length;
        long[] pref = new long[n];
        long sum = 0L;
        for (int i = 0; i < n; i++) {
            sum += candiesCount[i];
            pref[i] = sum;
        }
        boolean[] ans = new boolean[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int favoriteType = queries[i][0];
            long favoriteDay = queries[i][1];
            long dailyCap = queries[i][2];

            long totalPrev = favoriteType == 0 ? 0L : pref[favoriteType - 1];
            long totalCurr = pref[favoriteType];

            long minEat = favoriteDay + 1; // at least one candy per day
            long maxEat = (favoriteDay + 1) * dailyCap;

            boolean can = !(maxEat <= totalPrev || minEat > totalCurr);
            ans[i] = can;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Build prefix sums where pref[i] = total candies before type i
        n = len(candiesCount)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + candiesCount[i]

        ans = []
        for favoriteType, favoriteDay, dailyCap in queries:
            # total candies before this type
            before = pref[favoriteType]
            # last candy index (0‑based) of this type
            last_of_type = pref[favoriteType + 1] - 1

            # minimum and maximum candies that could have been eaten by favoriteDay
            min_eaten = favoriteDay + 1               # at least one per day
            max_eaten = (favoriteDay + 1) * dailyCap   # up to dailyCap per day

            # Check overlap between [min_eaten, max_eaten] and (before, last_of_type]
            possible = (max_eaten > before) and (min_eaten <= last_of_type)
            ans.append(possible)

        return ans
```

## Python3

```python
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        # Prefix sums of candy counts
        n = len(candiesCount)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + candiesCount[i]

        ans = []
        for favoriteType, favoriteDay, dailyCap in queries:
            # total candies before this type
            before = pref[favoriteType]
            # first and last candy index (1‑based) of the favorite type
            start = before + 1
            end = pref[favoriteType + 1]

            # possible total candies eaten by day favoriteDay
            min_eaten = favoriteDay + 1          # eat at least one per day
            max_eaten = (favoriteDay + 1) * dailyCap

            # intervals intersect?
            ans.append(not (max_eaten < start or min_eaten > end))
        return ans
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

bool* canEat(int* candiesCount, int candiesCountSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    long long *pref = (long long *)malloc(sizeof(long long) * candiesCountSize);
    long long sum = 0;
    for (int i = 0; i < candiesCountSize; ++i) {
        sum += (long long)candiesCount[i];
        pref[i] = sum;
    }

    bool *ans = (bool *)malloc(sizeof(bool) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        int type = queries[i][0];
        long long day = (long long)queries[i][1];
        long long cap = (long long)queries[i][2];

        long long totalPrev = (type == 0) ? 0 : pref[type - 1];
        long long earliestDay = totalPrev / cap;
        long long latestDay = pref[type] - 1;

        ans[i] = (day >= earliestDay && day <= latestDay);
    }

    free(pref);
    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public bool[] CanEat(int[] candiesCount, int[][] queries) {
        int n = candiesCount.Length;
        long[] prefix = new long[n];
        long sum = 0;
        for (int i = 0; i < n; i++) {
            sum += candiesCount[i];
            prefix[i] = sum;
        }

        bool[] answer = new bool[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int type = queries[i][0];
            long day = queries[i][1];
            long cap = queries[i][2];

            long candiesBefore = type == 0 ? 0 : prefix[type - 1];
            long candiesOfType = candiesCount[type];

            long minEat = day + 1;                     // at least one candy per day
            long maxEat = (day + 1) * cap;             // up to dailyCap each day

            bool can = maxEat > candiesBefore && minEat <= candiesBefore + candiesOfType - 1;
            answer[i] = can;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} candiesCount
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var canEat = function(candiesCount, queries) {
    const n = candiesCount.length;
    const prefix = new Array(n);
    let sum = 0;
    for (let i = 0; i < n; ++i) {
        sum += candiesCount[i];
        prefix[i] = sum;
    }
    
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        const [type, day, cap] = queries[i];
        const prev = type === 0 ? 0 : prefix[type - 1];
        const totalUpToType = prefix[type];
        
        const earliestDay = Math.floor(prev / cap);
        const latestDay = totalUpToType - 1;
        
        ans[i] = day >= earliestDay && day <= latestDay;
    }
    return ans;
};
```

## Typescript

```typescript
function canEat(candiesCount: number[], queries: number[][]): boolean[] {
    const n = candiesCount.length;
    const pref: bigint[] = new Array(n);
    let sum = 0n;
    for (let i = 0; i < n; i++) {
        sum += BigInt(candiesCount[i]);
        pref[i] = sum;
    }
    const result: boolean[] = [];
    for (const q of queries) {
        const favoriteType = q[0];
        const favoriteDay = BigInt(q[1]);
        const dailyCap = BigInt(q[2]);

        const totalPrev = favoriteType === 0 ? 0n : pref[favoriteType - 1];
        const totalCurr = pref[favoriteType];

        const minCandies = favoriteDay + 1n; // at least one candy per day
        const maxCandies = (favoriteDay + 1n) * dailyCap;

        const canEat = minCandies <= totalCurr && maxCandies > totalPrev;
        result.push(canEat);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $candiesCount
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function canEat($candiesCount, $queries) {
        $n = count($candiesCount);
        $prefix = [];
        $sum = 0;
        foreach ($candiesCount as $c) {
            $sum += $c;               // use 64‑bit integer
            $prefix[] = $sum;
        }

        $result = [];
        foreach ($queries as $q) {
            [$type, $day, $cap] = $q;

            $totalPrev = $type > 0 ? $prefix[$type - 1] : 0;
            $earliest = $totalPrev + 1;                     // first candy of this type (1‑based index)
            $latest   = $totalPrev + $candiesCount[$type]; // last candy of this type

            $minEat = $day + 1;                 // at least one per day
            $maxEat = ($day + 1) * $cap;        // at most cap per day

            if ($latest < $minEat || $earliest > $maxEat) {
                $result[] = false;
            } else {
                $result[] = true;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func canEat(_ candiesCount: [Int], _ queries: [[Int]]) -> [Bool] {
        let n = candiesCount.count
        var prefix = [Int64](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + Int64(candiesCount[i])
        }
        
        var answer = [Bool]()
        answer.reserveCapacity(queries.count)
        
        for q in queries {
            let favoriteType = q[0]
            let favoriteDay = Int64(q[1])
            let dailyCap = Int64(q[2])
            
            let candiesBefore = prefix[favoriteType]               // total candies of types < favoriteType
            let candiesUpTo = prefix[favoriteType + 1]             // total candies up to favoriteType inclusive
            
            let earliestDay = candiesBefore / dailyCap            // minimum day index we could start eating this type
            let latestDay = candiesUpTo - 1                       // maximum day index if we eat 1 candy per day
            
            answer.append(favoriteDay >= earliestDay && favoriteDay <= latestDay)
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canEat(candiesCount: IntArray, queries: Array<IntArray>): BooleanArray {
        val n = candiesCount.size
        val prefix = LongArray(n)
        var sum = 0L
        for (i in 0 until n) {
            sum += candiesCount[i].toLong()
            prefix[i] = sum
        }
        val result = BooleanArray(queries.size)
        for (i in queries.indices) {
            val q = queries[i]
            val type = q[0]
            val day = q[1].toLong()
            val cap = q[2].toLong()
            val before = if (type == 0) 0L else prefix[type - 1]
            val upTo = prefix[type]
            val minEat = day + 1 // at least one candy per day
            val maxEat = (day + 1) * cap
            result[i] = maxEat > before && minEat <= upTo
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<bool> canEat(List<int> candiesCount, List<List<int>> queries) {
    int n = candiesCount.length;
    List<int> pref = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      pref[i + 1] = pref[i] + candiesCount[i];
    }
    List<bool> ans = List.filled(queries.length, false);
    for (int i = 0; i < queries.length; ++i) {
      int favoriteType = queries[i][0];
      int favoriteDay = queries[i][1];
      int dailyCap = queries[i][2];

      int totalPrev = pref[favoriteType];
      int totalCurr = candiesCount[favoriteType];

      int earliestDay = (totalPrev + dailyCap - 1) ~/ dailyCap;
      int latestDay = totalPrev + totalCurr - 1;

      ans[i] = earliestDay <= favoriteDay && favoriteDay <= latestDay;
    }
    return ans;
  }
}
```

## Golang

```go
func canEat(candiesCount []int, queries [][]int) []bool {
	prefix := make([]int64, len(candiesCount))
	var sum int64
	for i, v := range candiesCount {
		sum += int64(v)
		prefix[i] = sum
	}
	ans := make([]bool, len(queries))
	for i, q := range queries {
		t, day, cap := q[0], int64(q[1]), int64(q[2])
		var prev int64
		if t > 0 {
			prev = prefix[t-1]
		}
		first := prev + 1
		last := prev + int64(candiesCount[t])

		minEat := day + 1
		maxEat := (day + 1) * cap

		ans[i] = !(maxEat < first || minEat > last)
	}
	return ans
}
```

## Ruby

```ruby
def can_eat(candies_count, queries)
  n = candies_count.length
  prefix = Array.new(n + 1, 0)
  (0...n).each do |i|
    prefix[i + 1] = prefix[i] + candies_count[i]
  end

  result = []
  queries.each do |type, day, cap|
    total_before = prefix[type]
    total_up_to = prefix[type + 1]

    earliest_day = (total_before + cap - 1) / cap
    latest_day = total_up_to - 1

    result << (day >= earliest_day && day <= latest_day)
  end
  result
end
```

## Scala

```scala
object Solution {
    def canEat(candiesCount: Array[Int], queries: Array[Array[Int]]): Array[Boolean] = {
        val n = candiesCount.length
        val prefix = new Array[Long](n)
        var sum: Long = 0L
        for (i <- 0 until n) {
            sum += candiesCount(i).toLong
            prefix(i) = sum
        }

        val result = new Array[Boolean](queries.length)

        for (idx <- queries.indices) {
            val q = queries(idx)
            val favoriteType = q(0)
            val favoriteDay = q(1).toLong
            val dailyCap = q(2).toLong

            val before: Long = if (favoriteType == 0) 0L else prefix(favoriteType - 1)
            val after: Long = prefix(favoriteType)

            val earliest = before / dailyCap          // minimum possible day index
            val latest = after - 1                    // maximum possible day index

            result(idx) = favoriteDay >= earliest && favoriteDay <= latest
        }

        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_eat(candies_count: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let n = candies_count.len();
        let mut prefix: Vec<i64> = vec![0; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + candies_count[i] as i64;
        }

        let mut result = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let fav_type = q[0] as usize;
            let day = q[1] as i64;
            let cap = q[2] as i64;

            let before = prefix[fav_type];
            let up_to = prefix[fav_type + 1];

            // earliest possible day to start eating this type
            let earliest_day = before / cap; // floor division
            // latest possible day while still eating this type
            let latest_day = up_to - 1;

            result.push(day >= earliest_day && day <= latest_day);
        }
        result
    }
}
```

## Racket

```racket
#lang racket
(require racket/match)

(define/contract (can-eat candiesCount queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof boolean?))
  (let* ((n (length candiesCount))
         (candies-vec (list->vector candiesCount))
         (pref (make-vector (+ n 1) 0)))
    ;; prefix sums: pref[i] = total candies before type i
    (for ([i (in-range n)])
      (vector-set! pref (add1 i)
                   (+ (vector-ref pref i) (vector-ref candies-vec i))))
    (let loop ((qs queries) (acc '()))
      (if (null? qs)
          (reverse acc)
          (match (car qs)
            [(list type day cap)
             (define sumPrev (vector-ref pref type))
             (define totalT  (vector-ref candies-vec type))
             (define minCandies (+ day 1))                     ; eat at least 1 per day
             (define maxCandies (* (+ day 1) cap))            ; eat up to dailyCap each day
             (define ok (and (<= minCandies (+ sumPrev totalT))
                             (> maxCandies sumPrev)))
             (loop (cdr qs) (cons ok acc))])))))
```

## Erlang

```erlang
-spec can_eat(CandiesCount :: [integer()], Queries :: [[integer()]]) -> [boolean()].
can_eat(CandiesCount, Queries) ->
    PrefTuple = list_to_tuple(prefix_sums(CandiesCount)),
    [check_query(Q, PrefTuple) || Q <- Queries].

prefix_sums([]) -> [];
prefix_sums(List) -> prefix_sums(List, 0, []).

prefix_sums([], _Acc, AccRev) -> lists:reverse(AccRev);
prefix_sums([H|T], Acc, AccRev) ->
    New = Acc + H,
    prefix_sums(T, New, [New | AccRev]).

check_query([Type, Day, Cap], PrefTuple) ->
    MinEat = Day + 1,
    MaxEat = (Day + 1) * Cap,
    CurrSum = element(Type+1, PrefTuple),
    PrevSum = case Type of
        0 -> 0;
        _ -> element(Type, PrefTuple)
    end,
    (MaxEat > PrevSum) andalso (MinEat =< CurrSum).
```

## Elixir

```elixir
defmodule Solution do
  @spec can_eat(candies_count :: [integer], queries :: [[integer]]) :: [boolean]
  def can_eat(candies_count, queries) do
    prefix =
      Enum.reduce(candies_count, [], fn x, acc ->
        case acc do
          [] -> [x]
          [last | _] = rev -> [(last + x) | rev]
        end
      end)
      |> Enum.reverse()

    arr = :array.from_list(prefix)

    Enum.map(queries, fn [fav_type, fav_day, daily_cap] ->
      prev =
        if fav_type == 0 do
          0
        else
          :array.get(fav_type - 1, arr)
        end

      total_up_to = :array.get(fav_type, arr)

      earliest = div(prev, daily_cap)
      latest = total_up_to - 1

      fav_day >= earliest and fav_day <= latest
    end)
  end
end
```
