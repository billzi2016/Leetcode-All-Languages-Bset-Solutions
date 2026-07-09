# 0406. Queue Reconstruction by Height

## Cpp

```cpp
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(),
            [](const vector<int>& a, const vector<int>& b) {
                if (a[0] != b[0]) return a[0] > b[0];
                return a[1] < b[1];
            });
        vector<vector<int>> queue;
        for (auto& p : people) {
            queue.insert(queue.begin() + p[1], p);
        }
        return queue;
    }
};
```

## Java

```java
class Solution {
    public int[][] reconstructQueue(int[][] people) {
        // Sort by descending height and ascending k
        java.util.Arrays.sort(people, (a, b) -> {
            if (a[0] != b[0]) return b[0] - a[0];
            return a[1] - b[1];
        });
        java.util.List<int[]> queue = new java.util.ArrayList<>();
        for (int[] person : people) {
            queue.add(person[1], person);
        }
        int[][] result = new int[queue.size()][2];
        for (int i = 0; i < queue.size(); i++) {
            result[i] = queue.get(i);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sort by descending height and ascending k
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []
        for person in people:
            queue.insert(person[1], person)
        return queue
```

## Python3

```python
from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by descending height and ascending k
        people.sort(key=lambda x: (-x[0], x[1]))
        queue: List[List[int]] = []
        for person in people:
            queue.insert(person[1], person)
        return queue
```

## C

```c
#include <stdlib.h>

struct Person {
    int h;
    int k;
};

static int cmpPerson(const void *a, const void *b) {
    const struct Person *p1 = (const struct Person *)a;
    const struct Person *p2 = (const struct Person *)b;
    if (p1->h != p2->h)
        return p2->h - p1->h;          // higher height first
    return p1->k - p2->k;              // smaller k first
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** reconstructQueue(int** people, int peopleSize, int* peopleColSize,
                       int* returnSize, int*** returnColumnSizes) {
    (void)peopleColSize; // unused

    struct Person *arr = (struct Person *)malloc(peopleSize * sizeof(struct Person));
    for (int i = 0; i < peopleSize; ++i) {
        arr[i].h = people[i][0];
        arr[i].k = people[i][1];
    }

    qsort(arr, peopleSize, sizeof(struct Person), cmpPerson);

    int **queue = (int **)malloc(peopleSize * sizeof(int *));
    int curSize = 0;

    for (int i = 0; i < peopleSize; ++i) {
        int pos = arr[i].k;
        // shift right to make space at position pos
        for (int j = curSize; j > pos; --j) {
            queue[j] = queue[j - 1];
        }
        queue[pos] = (int *)malloc(2 * sizeof(int));
        queue[pos][0] = arr[i].h;
        queue[pos][1] = arr[i].k;
        ++curSize;
    }

    free(arr);

    *returnSize = peopleSize;
    *returnColumnSizes = (int **)malloc(sizeof(int *));
    **returnColumnSizes = (int *)malloc(peopleSize * sizeof(int));
    for (int i = 0; i < peopleSize; ++i) {
        (**returnColumnSizes)[i] = 2;
    }

    return queue;
}
```

## Csharp

```csharp
public class Solution {
    public int[][] ReconstructQueue(int[][] people) {
        // Sort by descending height, then ascending k
        Array.Sort(people, (a, b) => {
            if (a[0] != b[0]) return b[0].CompareTo(a[0]); // higher first
            return a[1].CompareTo(b[1]); // smaller k first
        });

        var result = new System.Collections.Generic.List<int[]>();
        foreach (var p in people) {
            result.Insert(p[1], p);
        }

        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function(people) {
    // Sort by descending height, then ascending k value
    people.sort((a, b) => {
        if (b[0] !== a[0]) return b[0] - a[0];
        return a[1] - b[1];
    });
    
    const queue = [];
    for (const person of people) {
        // Insert person at the index equal to their k value
        queue.splice(person[1], 0, person);
    }
    return queue;
};
```

## Typescript

```typescript
function reconstructQueue(people: number[][]): number[][] {
    // Sort by descending height; for equal heights, sort by ascending k
    people.sort((a, b) => {
        if (b[0] !== a[0]) return b[0] - a[0];
        return a[1] - b[1];
    });

    const queue: number[][] = [];
    for (const person of people) {
        // Insert person at the index equal to their k value
        queue.splice(person[1], 0, person);
    }
    return queue;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $people
     * @return Integer[][]
     */
    function reconstructQueue($people) {
        usort($people, function($a, $b) {
            if ($a[0] == $b[0]) {
                return $a[1] <=> $b[1];
            }
            // higher height first
            return $b[0] <=> $a[0];
        });

        $queue = [];
        foreach ($people as $person) {
            // insert person at index k
            array_splice($queue, $person[1], 0, [$person]);
        }

        return $queue;
    }
}
```

## Swift

```swift
class Solution {
    func reconstructQueue(_ people: [[Int]]) -> [[Int]] {
        let sorted = people.sorted { (a, b) -> Bool in
            if a[0] != b[0] {
                return a[0] > b[0]
            } else {
                return a[1] < b[1]
            }
        }
        var queue: [[Int]] = []
        for person in sorted {
            let index = person[1]
            queue.insert(person, at: index)
        }
        return queue
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reconstructQueue(people: Array<IntArray>): Array<IntArray> {
        val sorted = people.sortedWith(
            compareByDescending<IntArray> { it[0] }
                .thenBy { it[1] }
        )
        val result = mutableListOf<IntArray>()
        for (p in sorted) {
            result.add(p[1], p)
        }
        return result.toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<List<int>> reconstructQueue(List<List<int>> people) {
    // Sort by descending height and ascending k
    people.sort((a, b) {
      if (a[0] != b[0]) return b[0] - a[0];
      return a[1] - b[1];
    });
    List<List<int>> queue = [];
    for (var person in people) {
      queue.insert(person[1], person);
    }
    return queue;
  }
}
```

## Golang

```go
import "sort"

func reconstructQueue(people [][]int) [][]int {
	sort.Slice(people, func(i, j int) bool {
		if people[i][0] != people[j][0] {
			return people[i][0] > people[j][0]
		}
		return people[i][1] < people[j][1]
	})
	res := make([][]int, 0, len(people))
	for _, p := range people {
		k := p[1]
		if k >= len(res) {
			res = append(res, p)
		} else {
			res = append(res, nil)
			copy(res[k+1:], res[k:])
			res[k] = p
		}
	}
	return res
}
```

## Ruby

```ruby
def reconstruct_queue(people)
  people.sort_by { |h, k| [-h, k] }.each_with_object([]) do |person, queue|
    queue.insert(person[1], person)
  end
end
```

## Scala

```scala
object Solution {
  def reconstructQueue(people: Array[Array[Int]]): Array[Array[Int]] = {
    val sorted = people.sortWith { (a, b) =>
      if (a(0) != b(0)) a(0) > b(0) else a(1) < b(1)
    }
    val queue = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    for (p <- sorted) {
      queue.insert(p(1), p)
    }
    queue.toArray
  }
}
```

## Rust

```rust
impl Solution {
    pub fn reconstruct_queue(people: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut people = people;
        // Sort by descending height, then ascending k
        people.sort_by(|a, b| {
            if a[0] != b[0] {
                b[0].cmp(&a[0])
            } else {
                a[1].cmp(&b[1])
            }
        });
        let mut queue: Vec<Vec<i32>> = Vec::new();
        for person in people {
            let idx = person[1] as usize;
            queue.insert(idx, person);
        }
        queue
    }
}
```

## Racket

```racket
(require racket/list)

(define (insert-at lst idx elem)
  (cond [(zero? idx) (cons elem lst)]
        [else (cons (car lst) (insert-at (cdr lst) (- idx 1) elem))]))

(define/contract (reconstruct-queue people)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ((sorted (sort people
                       (lambda (a b)
                         (let ((ha (first a)) (hb (first b))
                               (ka (second a)) (kb (second b)))
                           (if (= ha hb)
                               (< ka kb)
                               (> ha hb))))))
         (result (foldl (lambda (person acc)
                          (insert-at acc (second person) person))
                        '()
                        sorted)))
    result))
```

## Erlang

```erlang
-module(solution).
-export([reconstruct_queue/1]).

-spec reconstruct_queue(People :: [[integer()]]) -> [[integer()]].
reconstruct_queue(People) ->
    Compare = fun({H1, K1}, {H2, K2}) ->
        if
            H1 > H2 -> true;
            H1 < H2 -> false;
            true -> K1 < K2
        end
    end,
    Sorted = lists:sort(Compare, People),
    lists:foldl(fun({H, K}, Acc) ->
        insert_at(K, [H, K], Acc)
    end, [], Sorted).

insert_at(Index, Elem, List) ->
    {Front, Back} = lists:split(Index, List),
    Front ++ [Elem] ++ Back.
```

## Elixir

```elixir
defmodule Solution do
  @spec reconstruct_queue(people :: [[integer]]) :: [[integer]]
  def reconstruct_queue(people) do
    sorted = Enum.sort_by(people, fn [h, k] -> {-h, k} end)

    Enum.reduce(sorted, [], fn person, acc ->
      [_h, k] = person
      List.insert_at(acc, k, person)
    end)
  end
end
```
