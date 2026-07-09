# 1665. Minimum Initial Energy to Finish Tasks

## Cpp

```cpp
class Solution {
public:
    int minimumEffort(vector<vector<int>>& tasks) {
        sort(tasks.begin(), tasks.end(), [](const vector<int>& a, const vector<int>& b){
            return (a[1] - a[0]) > (b[1] - b[0]);
        });
        long long sum = 0;
        long long ans = 0;
        for (auto& t : tasks) {
            ans = max(ans, (long long)t[1] + sum);
            sum += t[0];
        }
        return (int)ans;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int minimumEffort(int[][] tasks) {
        Arrays.sort(tasks, (a, b) -> {
            int diffA = a[1] - a[0];
            int diffB = b[1] - b[0];
            return Integer.compare(diffB, diffA); // descending by (minimum - actual)
        });
        long need = 0;
        for (int i = tasks.length - 1; i >= 0; --i) {
            need = Math.max(tasks[i][1], need + tasks[i][0]);
        }
        return (int) need;
    }
}
```

## Python

```python
class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        # Sort by (minimum - actual) descending
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        total_actual = 0
        cur = 0
        for actual, minimum in tasks:
            total_actual += actual
            cur = max(cur, minimum)
            cur -= actual
        return cur + total_actual
```

## Python3

```python
from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort by (minimum - actual) descending
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        ans = 0
        prefix = 0  # sum of actual energies of already processed tasks
        for actual, minimum in tasks:
            ans = max(ans, minimum + prefix)
            prefix += actual
        return ans
```

## C

```c
#include <stdlib.h>

static int cmpTasks(const void *p1, const void *p2) {
    const int *a = *(const int **)p1;
    const int *b = *(const int **)p2;
    int diffA = a[1] - a[0];
    int diffB = b[1] - b[0];
    if (diffA != diffB) return diffB - diffA;          // descending by (minimum-actual)
    return b[1] - a[1];                                // tie‑breaker: larger minimum first
}

int minimumEffort(int** tasks, int tasksSize, int* tasksColSize) {
    if (tasksSize == 0) return 0;
    qsort(tasks, tasksSize, sizeof(int *), cmpTasks);
    
    long long ans = 0;
    long long cur = 0;
    for (int i = 0; i < tasksSize; ++i) {
        int actual = tasks[i][0];
        int minimum = tasks[i][1];
        if (cur < minimum) {
            ans += (minimum - cur);
            cur = minimum;
        }
        cur -= actual;
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumEffort(int[][] tasks) {
        System.Array.Sort(tasks, (x, y) => {
            int diffX = x[1] - x[0];
            int diffY = y[1] - y[0];
            // descending order
            return diffY.CompareTo(diffX);
        });

        long need = 0;
        for (int i = tasks.Length - 1; i >= 0; --i) {
            int actual = tasks[i][0];
            int minimum = tasks[i][1];
            need = System.Math.Max(minimum, need + actual);
        }
        return (int)need;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} tasks
 * @return {number}
 */
var minimumEffort = function(tasks) {
    tasks.sort((a, b) => {
        const diffA = a[1] - a[0];
        const diffB = b[1] - b[0];
        if (diffA !== diffB) return diffB - diffA;
        return b[1] - a[1];
    });
    let need = 0;
    for (let i = tasks.length - 1; i >= 0; --i) {
        const [actual, minimum] = tasks[i];
        need = Math.max(minimum, need + actual);
    }
    return need;
};
```

## Typescript

```typescript
function minimumEffort(tasks: number[][]): number {
    // Sort by (minimum - actual) descending
    tasks.sort((a, b) => {
        const diffA = a[1] - a[0];
        const diffB = b[1] - b[0];
        return diffB - diffA;
    });
    let cur = 0;
    for (let i = tasks.length - 1; i >= 0; --i) {
        const [actual, minimum] = tasks[i];
        cur = Math.max(minimum, cur + actual);
    }
    return cur;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $tasks
     * @return Integer
     */
    function minimumEffort($tasks) {
        usort($tasks, function($a, $b) {
            $diffA = $a[1] - $a[0];
            $diffB = $b[1] - $b[0];
            if ($diffA == $diffB) return 0;
            // sort by descending (minimum - actual)
            return ($diffA < $diffB) ? 1 : -1;
        });
        $required = 0;
        foreach ($tasks as $task) {
            $required = max($task[1], $required + $task[0]);
        }
        return $required;
    }
}
```

## Swift

```swift
class Solution {
    func minimumEffort(_ tasks: [[Int]]) -> Int {
        let sortedTasks = tasks.sorted { (a, b) -> Bool in
            let diffA = a[1] - a[0]
            let diffB = b[1] - b[0]
            if diffA == diffB {
                return a[1] > b[1]
            }
            return diffA > diffB
        }
        var required = 0
        var spent = 0
        for task in sortedTasks {
            let actual = task[0]
            let minimum = task[1]
            required = max(required, minimum + spent)
            spent += actual
        }
        return required
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumEffort(tasks: Array<IntArray>): Int {
        tasks.sortWith { a, b ->
            val diffA = a[1] - a[0]
            val diffB = b[1] - b[0]
            diffB.compareTo(diffA) // descending order
        }
        var sumActual = 0L
        var answer = 0L
        for (t in tasks) {
            answer = maxOf(answer, sumActual + t[1])
            sumActual += t[0]
        }
        return answer.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minimumEffort(List<List<int>> tasks) {
    // Sort by descending (minimum - actual), tie-breaker by larger minimum
    tasks.sort((a, b) {
      int diffA = a[1] - a[0];
      int diffB = b[1] - b[0];
      if (diffA != diffB) return diffB.compareTo(diffA);
      return b[1].compareTo(a[1]);
    });

    int need = 0;
    for (int i = tasks.length - 1; i >= 0; --i) {
      int actual = tasks[i][0];
      int minimum = tasks[i][1];
      int afterTask = need + actual;
      need = afterTask > minimum ? afterTask : minimum;
    }
    return need;
  }
}
```

## Golang

```go
import "sort"

func minimumEffort(tasks [][]int) int {
	sort.Slice(tasks, func(i, j int) bool {
		diffI := tasks[i][1] - tasks[i][0]
		diffJ := tasks[j][1] - tasks[j][0]
		if diffI == diffJ {
			return tasks[i][1] > tasks[j][1]
		}
		return diffI > diffJ
	})
	var prefix, ans int64
	for _, t := range tasks {
		actual := int64(t[0])
		minimum := int64(t[1])
		if minimum+prefix > ans {
			ans = minimum + prefix
		}
		prefix += actual
	}
	return int(ans)
}
```

## Ruby

```ruby
# @param {Integer[][]} tasks
# @return {Integer}
def minimum_effort(tasks)
  tasks.sort_by! { |a, m| m - a }
  need = 0
  tasks.each do |actual, minimum|
    need = [minimum, need + actual].max
  end
  need
end
```

## Scala

```scala
object Solution {
    def minimumEffort(tasks: Array[Array[Int]]): Int = {
        val sorted = tasks.sortWith { (a, b) =>
            val diffA = a(1) - a(0)
            val diffB = b(1) - b(0)
            if (diffA != diffB) diffA > diffB else a(1) > b(1)
        }
        var spent: Long = 0L
        var ans: Long = 0L
        for (t <- sorted) {
            val actual = t(0).toLong
            val minimum = t(1).toLong
            ans = math.max(ans, minimum + spent)
            spent += actual
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_effort(tasks: Vec<Vec<i32>>) -> i32 {
        let mut tasks = tasks;
        // Sort by descending (minimum - actual)
        tasks.sort_by(|a, b| {
            let diff_a = a[1] - a[0];
            let diff_b = b[1] - b[0];
            diff_b.cmp(&diff_a)
        });
        let mut need: i64 = 0;
        for task in tasks.iter().rev() {
            let actual = task[0] as i64;
            let minimum = task[1] as i64;
            need = std::cmp::max(minimum, need + actual);
        }
        need as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-effort tasks)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((sorted
          (sort tasks
                (lambda (a b)
                  (> (- (second a) (first a))
                     (- (second b) (first b))))))
         (rev-sorted (reverse sorted)))
    (let loop ((lst rev-sorted) (need 0))
      (if (null? lst)
          need
          (let* ((task (car lst))
                 (actual (first task))
                 (minimum (second task))
                 (new-need (max minimum (+ need actual))))
            (loop (cdr lst) new-need))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_effort/1]).

-spec minimum_effort(Tasks :: [[integer()]]) -> integer().
minimum_effort(Tasks) ->
    Sorted = lists:sort(fun compare/2, Tasks),
    compute(Sorted, 0).

compare(A, B) ->
    ActualA = hd(A), MinimumA = tl(A) |> hd(),
    ActualB = hd(B), MinimumB = tl(B) |> hd(),
    DiffA = MinimumA - ActualA,
    DiffB = MinimumB - ActualB,
    case DiffA <=> DiffB of
        less -> true;
        greater -> false;
        equal -> MinimumA > MinimumB
    end.

compute([], Acc) ->
    Acc;
compute([[Actual, Minimum] | Rest], Acc) ->
    NewAcc = erlang:max(Minimum, Acc + Actual),
    compute(Rest, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_effort(tasks :: [[integer]]) :: integer
  def minimum_effort(tasks) do
    sorted =
      Enum.sort_by(tasks, fn [actual, minimum] -> minimum - actual end, &>=/2)

    Enum.reduce(sorted, 0, fn [actual, minimum], acc ->
      if acc + actual < minimum, do: minimum, else: acc + actual
    end)
  end
end
```
