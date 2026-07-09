# 2358. Maximum Number of Groups Entering a Competition

## Cpp

```cpp
class Solution {
public:
    int maximumGroups(vector<int>& grades) {
        long long n = grades.size();
        long long k = (long long)((std::sqrt(1.0 + 8.0 * n) - 1) / 2);
        while ((k + 1) * (k + 2) / 2 <= n) ++k;
        while (k * (k + 1) / 2 > n) --k;
        return static_cast<int>(k);
    }
};
```

## Java

```java
class Solution {
    public int maximumGroups(int[] grades) {
        long n = grades.length;
        long k = (long)Math.floor((Math.sqrt(1 + 8 * n) - 1) / 2);
        return (int)k;
    }
}
```

## Python

```python
class Solution(object):
    def maximumGroups(self, grades):
        """
        :type grades: List[int]
        :rtype: int
        """
        grades.sort()
        prev_sum = 0
        cur_sum = 0
        groups = 0
        for g in grades:
            cur_sum += g
            if cur_sum > prev_sum:
                groups += 1
                prev_sum = cur_sum
                cur_sum = 0
        return groups
```

## Python3

```python
from typing import List

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort()
        prev_sum = 0
        cur_sum = 0
        groups = 0
        need = 1  # size of the next group to form
        i = 0
        n = len(grades)
        while i < n:
            cur_sum += grades[i]
            i += 1
            need -= 1
            if need == 0:
                if cur_sum > prev_sum:
                    groups += 1
                    prev_sum = cur_sum
                    cur_sum = 0
                    need = groups + 1  # next group size increases by 1 each time
                else:
                    break
        return groups
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int maximumGroups(int* grades, int gradesSize) {
    if (gradesSize == 0) return 0;
    qsort(grades, gradesSize, sizeof(int), cmp_int);
    
    long long prevSum = 0;
    long long curSum = 0;
    int groups = 0;
    
    for (int i = 0; i < gradesSize; ++i) {
        curSum += grades[i];
        if (curSum > prevSum) {
            ++groups;
            prevSum = curSum;
            curSum = 0;
        }
    }
    return groups;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximumGroups(int[] grades)
    {
        Array.Sort(grades);
        long prevSum = 0, curSum = 0;
        int groups = 0, cnt = 0;

        foreach (int g in grades)
        {
            curSum += g;
            cnt++;
            if (cnt > groups && curSum > prevSum)
            {
                groups++;
                prevSum = curSum;
                curSum = 0;
                cnt = 0;
            }
        }

        return groups;
    }
}
```

## Javascript

```javascript
var maximumGroups = function(grades) {
    grades.sort((a, b) => a - b);
    const n = grades.length;
    let i = 0;
    let groups = 0;
    let prevSum = 0;
    let needSize = 1;
    while (i < n) {
        let curSum = 0;
        let cnt = 0;
        // take at least the required number of students
        while (cnt < needSize && i < n) {
            curSum += grades[i++];
            cnt++;
        }
        // if sum is not larger than previous group's sum, keep adding students
        while (i < n && curSum <= prevSum) {
            curSum += grades[i++];
            cnt++;
        }
        if (curSum > prevSum) {
            groups++;
            prevSum = curSum;
            needSize = cnt + 1; // next group must be larger
        } else {
            break;
        }
    }
    return groups;
};
```

## Typescript

```typescript
function maximumGroups(grades: number[]): number {
    grades.sort((a, b) => a - b);
    let groups = 0;
    let idx = 0;
    const n = grades.length;
    while (true) {
        const need = groups + 1;
        if (idx + need > n) break;
        groups++;
        idx += need;
    }
    return groups;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $grades
     * @return Integer
     */
    function maximumGroups($grades) {
        sort($grades, SORT_NUMERIC);
        $prevSum = 0;
        $needSize = 1;
        $groups = 0;
        $curSum = 0;
        $curSize = 0;

        foreach ($grades as $g) {
            $curSum += $g;
            $curSize++;

            if ($curSize >= $needSize && $curSum > $prevSum) {
                $groups++;
                $prevSum = $curSum;
                $curSum = 0;
                $curSize = 0;
                $needSize++;
            }
        }

        return $groups;
    }
}
```

## Swift

```swift
class Solution {
    func maximumGroups(_ grades: [Int]) -> Int {
        let sortedGrades = grades.sorted()
        var groups = 0
        var currentSum = 0
        var countInGroup = 0
        var previousSum = 0
        
        for grade in sortedGrades {
            currentSum += grade
            countInGroup += 1
            if countInGroup == groups + 1 && currentSum > previousSum {
                groups += 1
                previousSum = currentSum
                currentSum = 0
                countInGroup = 0
            }
        }
        
        return groups
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumGroups(grades: IntArray): Int {
        val n = grades.size
        var groups = 0
        var used = 0
        while (used + groups + 1 <= n) {
            groups++
            used += groups
        }
        return groups
    }
}
```

## Dart

```dart
class Solution {
  int maximumGroups(List<int> grades) {
    grades.sort();
    int n = grades.length;
    int groups = 0;
    int i = 0;
    while (true) {
      int need = groups + 1;
      if (i + need > n) break;
      i += need;
      groups++;
    }
    return groups;
  }
}
```

## Golang

```go
import "sort"

func maximumGroups(grades []int) int {
	sort.Ints(grades)
	ans, curSize, need := 0, 0, 1
	for i := 0; i < len(grades); i++ {
		curSize++
		if curSize == need {
			ans++
			curSize = 0
			need++
		}
	}
	return ans
}
```

## Ruby

```ruby
def maximum_groups(grades)
  grades.sort!
  prev_sum = 0
  prev_cnt = 0
  cur_sum = 0
  cur_cnt = 0
  groups = 0

  grades.each do |g|
    cur_sum += g
    cur_cnt += 1
    if cur_sum > prev_sum && cur_cnt > prev_cnt
      groups += 1
      prev_sum = cur_sum
      prev_cnt = cur_cnt
      cur_sum = 0
      cur_cnt = 0
    end
  end

  groups
end
```

## Scala

```scala
object Solution {
    def maximumGroups(grades: Array[Int]): Int = {
        val n = grades.length.toLong
        var left = 0L
        var right = n + 1
        while (left + 1 < right) {
            val mid = (left + right) / 2
            if (mid * (mid + 1) / 2 <= n) left = mid else right = mid
        }
        left.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_groups(mut grades: Vec<i32>) -> i32 {
        grades.sort_unstable();
        let mut groups: usize = 0;
        let mut prev_sum: i64 = 0;
        let mut cur_sum: i64 = 0;
        let mut cur_cnt: usize = 0;
        for g in grades {
            cur_sum += g as i64;
            cur_cnt += 1;
            if cur_cnt > groups && cur_sum > prev_sum {
                groups += 1;
                prev_sum = cur_sum;
                cur_sum = 0;
                cur_cnt = 0;
            }
        }
        groups as i32
    }
}
```

## Racket

```racket
(require racket/match)

(define/contract (maximum-groups grades)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort grades <))
         (state
          (foldl
           (lambda (g acc)
             (match-define (list prev-sum target ans cur-sum cnt) acc)
             (let ((new-cur (+ cur-sum g))
                   (new-cnt (+ cnt 1)))
               (if (and (>= new-cnt target) (> new-cur prev-sum))
                   (list new-cur (+ target 1) (+ ans 1) 0 0)
                   (list prev-sum target ans new-cur new-cnt))))
           (list 0 1 0 0 0)
           sorted)))
    (match-define (list _ _ ans _ _) state)
    ans))
```

## Erlang

```erlang
-spec maximum_groups(Grades :: [integer()]) -> integer().
maximum_groups(Grades) ->
    Sorted = lists:sort(Grades),
    {_Prev, _Cur, Count} = lists:foldl(
        fun(G, {Prev, Cur, Cnt}) ->
            NewCur = Cur + G,
            if
                NewCur > Prev -> {NewCur, 0, Cnt + 1};
                true -> {Prev, NewCur, Cnt}
            end
        end,
        {0, 0, 0},
        Sorted),
    Count.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_groups(grades :: [integer]) :: integer
  def maximum_groups(grades) do
    n = length(grades)
    ((:math.sqrt(1 + 8 * n) - 1) / 2)
    |> Float.floor()
    |> trunc()
  end
end
```
