# 2751. Robot Collisions

## Cpp

```cpp
class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        int n = positions.size();
        vector<int> order(n);
        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(),
             [&](int a, int b) { return positions[a] < positions[b]; });
        
        // use long long for intermediate health modifications
        vector<long long> h(healths.begin(), healths.end());
        vector<int> stack; // indices of robots moving right that are still alive
        
        for (int idx : order) {
            if (directions[idx] == 'R') {
                stack.push_back(idx);
            } else { // direction L
                while (!stack.empty() && h[idx] > 0) {
                    int j = stack.back(); // top robot moving right
                    if (h[j] > h[idx]) {
                        // right robot survives, loses 1 health
                        --h[j];
                        h[idx] = 0; // left robot destroyed
                        break;
                    } else if (h[j] < h[idx]) {
                        // left robot survives, loses 1 health
                        --h[idx];
                        stack.pop_back(); // right robot destroyed
                        // continue checking next right-moving robot
                    } else { // equal health, both destroyed
                        h[j] = 0;
                        h[idx] = 0;
                        stack.pop_back();
                        break;
                    }
                }
            }
        }
        
        vector<int> result;
        for (int i = 0; i < n; ++i) {
            if (h[i] > 0) result.push_back(static_cast<int>(h[i]));
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        int n = positions.length;
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        Arrays.sort(order, Comparator.comparingInt(i -> positions[i]));

        Deque<Integer> stack = new ArrayDeque<>();
        char[] dir = directions.toCharArray();

        for (int idx : order) {
            if (dir[idx] == 'R') {
                stack.push(idx);
            } else { // direction 'L'
                while (!stack.isEmpty() && healths[idx] > 0) {
                    int topIdx = stack.pop();
                    if (healths[topIdx] > healths[idx]) {
                        healths[topIdx]--;
                        healths[idx] = 0;
                        stack.push(topIdx);
                        break;
                    } else if (healths[topIdx] < healths[idx]) {
                        healths[idx]--;
                        healths[topIdx] = 0;
                        // continue to possibly collide with next right-moving robot
                    } else { // equal health
                        healths[topIdx] = 0;
                        healths[idx] = 0;
                        break;
                    }
                }
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (healths[i] > 0) {
                result.add(healths[i]);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        n = len(positions)
        # sort indices by position
        order = sorted(range(n), key=lambda i: positions[i])
        stack = []  # will store indices of robots moving right that are alive
        
        for idx in order:
            if directions[idx] == 'R':
                stack.append(idx)
            else:  # direction L, may collide with robots on stack
                while stack and healths[idx] > 0:
                    j = stack[-1]
                    if healths[j] == healths[idx]:
                        # both destroyed
                        healths[idx] = 0
                        healths[j] = 0
                        stack.pop()
                        break
                    elif healths[j] > healths[idx]:
                        # right robot survives, loses 1 health
                        healths[j] -= 1
                        healths[idx] = 0
                        break
                    else:  # healths[idx] > healths[j]
                        # left robot survives, loses 1 health
                        healths[idx] -= 1
                        stack.pop()
                        if healths[idx] == 0:
                            break
                # if stack empty or left robot dead, nothing to do
        
        # collect survivors in original order
        result = [healths[i] for i in range(n) if healths[i] > 0]
        return result
```

## Python3

```python
from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        # sort indices by position
        order = sorted(range(n), key=lambda i: positions[i])
        stack = []  # indices of right-moving robots that are alive
        
        for idx in order:
            if directions[idx] == 'R':
                stack.append(idx)
            else:  # moving left
                while stack and healths[idx] > 0:
                    top = stack[-1]
                    if healths[top] > healths[idx]:
                        # right robot survives, loses 1 health
                        healths[top] -= 1
                        healths[idx] = 0
                        break
                    elif healths[top] < healths[idx]:
                        # left robot survives this collision, loses 1 health
                        healths[idx] -= 1
                        stack.pop()
                        # continue checking next right-moving robot
                    else:  # equal health, both destroyed
                        healths[top] = 0
                        healths[idx] = 0
                        stack.pop()
                        break
        # collect survivors in original order
        return [healths[i] for i in range(n) if healths[i] > 0]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int pos;
    int idx;
} Robot;

static int cmpRobot(const void *a, const void *b) {
    const Robot *ra = (const Robot *)a;
    const Robot *rb = (const Robot *)b;
    if (ra->pos < rb->pos) return -1;
    if (ra->pos > rb->pos) return 1;
    return 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* survivedRobotsHealths(int* positions, int positionsSize, int* healths, int healthsSize,
                           char* directions, int* returnSize) {
    int n = positionsSize;
    Robot *robots = (Robot *)malloc(n * sizeof(Robot));
    for (int i = 0; i < n; ++i) {
        robots[i].pos = positions[i];
        robots[i].idx = i;
    }
    qsort(robots, n, sizeof(Robot), cmpRobot);

    int *stack = (int *)malloc(n * sizeof(int));
    int top = -1;  // empty stack

    for (int k = 0; k < n; ++k) {
        int idx = robots[k].idx;
        if (directions[idx] == 'R') {
            stack[++top] = idx;
        } else { // direction 'L'
            while (top >= 0 && healths[idx] > 0) {
                int rIdx = stack[top];
                if (healths[rIdx] == healths[idx]) {
                    healths[rIdx] = 0;
                    healths[idx] = 0;
                    top--; // both destroyed
                    break;
                } else if (healths[rIdx] > healths[idx]) {
                    healths[rIdx]--;
                    healths[idx] = 0; // left robot destroyed
                    break;
                } else { // left robot stronger
                    healths[idx]--;
                    top--; // right robot destroyed, continue checking
                }
            }
        }
    }

    int *result = (int *)malloc(n * sizeof(int));
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        if (healths[i] > 0) {
            result[cnt++] = healths[i];
        }
    }

    free(robots);
    free(stack);

    *returnSize = cnt;
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> SurvivedRobotsHealths(int[] positions, int[] healths, string directions) {
        int n = positions.Length;
        int[] order = new int[n];
        for (int i = 0; i < n; i++) order[i] = i;
        Array.Sort(order, (a, b) => positions[a].CompareTo(positions[b]));

        var stack = new Stack<int>(); // indices of robots moving right

        foreach (int idx in order) {
            if (directions[idx] == 'R') {
                stack.Push(idx);
            } else { // direction is 'L'
                while (stack.Count > 0 && healths[idx] > 0) {
                    int top = stack.Peek();
                    if (healths[top] == healths[idx]) {
                        healths[top] = 0;
                        healths[idx] = 0;
                        stack.Pop();
                        break; // left robot destroyed
                    } else if (healths[top] > healths[idx]) {
                        healths[top]--;
                        healths[idx] = 0;
                        break; // left robot destroyed
                    } else { // healths[top] < healths[idx]
                        healths[idx]--;
                        stack.Pop(); // right robot destroyed, continue checking
                    }
                }
            }
        }

        var result = new List<int>();
        for (int i = 0; i < n; i++) {
            if (healths[i] > 0) result.Add(healths[i]);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} positions
 * @param {number[]} healths
 * @param {string} directions
 * @return {number[]}
 */
var survivedRobotsHealths = function(positions, healths, directions) {
    const n = positions.length;
    const idx = Array.from({length: n}, (_, i) => i);
    idx.sort((a, b) => positions[a] - positions[b]); // left to right

    const stack = []; // indices of right-moving robots that are alive

    for (const i of idx) {
        if (directions[i] === 'R') {
            // push right-moving robot
            stack.push(i);
        } else { // 'L'
            while (stack.length > 0 && healths[i] > 0) {
                const j = stack[stack.length - 1]; // top right-moving robot

                if (healths[i] > healths[j]) {
                    // left robot survives this collision
                    healths[i]--;
                    // right robot dies
                    stack.pop();
                    // continue to possibly collide with next right robot
                } else if (healths[i] < healths[j]) {
                    // right robot survives
                    healths[j]--;
                    // left robot dies
                    healths[i] = 0;
                    if (healths[j] === 0) {
                        stack.pop(); // right robot also died after decrement
                    }
                    break; // left robot dead, stop collisions
                } else { // equal health
                    healths[i] = 0;
                    healths[j] = 0;
                    stack.pop();
                    break;
                }
            }
            // if healths[i] > 0 after loop, it survives moving left (no further action needed)
        }
    }

    const result = [];
    for (let i = 0; i < n; ++i) {
        if (healths[i] > 0) result.push(healths[i]);
    }
    return result;
};
```

## Typescript

```typescript
function survivedRobotsHealths(positions: number[], healths: number[], directions: string): number[] {
    const n = positions.length;
    const order = Array.from({ length: n }, (_, i) => i);
    order.sort((a, b) => positions[a] - positions[b]);

    const stack: number[] = []; // indices of right-moving robots that are still alive

    for (const idx of order) {
        if (directions[idx] === 'R') {
            stack.push(idx);
        } else { // direction is 'L'
            while (stack.length > 0 && healths[idx] > 0) {
                const topIdx = stack[stack.length - 1];
                if (healths[topIdx] === healths[idx]) {
                    // both destroyed
                    healths[topIdx] = 0;
                    healths[idx] = 0;
                    stack.pop();
                    break; // current robot is dead
                } else if (healths[topIdx] > healths[idx]) {
                    // right-moving robot survives, loses one health
                    healths[topIdx]--;
                    healths[idx] = 0; // left-moving robot destroyed
                    break;
                } else { // healths[topIdx] < healths[idx]
                    // left-moving robot survives this collision, loses one health
                    healths[idx]--;
                    // right-moving robot destroyed
                    healths[topIdx] = 0;
                    stack.pop();
                    // continue checking with previous right-moving robots
                }
            }
        }
    }

    const result: number[] = [];
    for (let i = 0; i < n; ++i) {
        if (healths[i] > 0) result.push(healths[i]);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $positions
     * @param Integer[] $healths
     * @param String $directions
     * @return Integer[]
     */
    function survivedRobotsHealths($positions, $healths, $directions) {
        $n = count($positions);
        // indices sorted by position
        $indices = range(0, $n - 1);
        usort($indices, function($a, $b) use ($positions) {
            return $positions[$a] <=> $positions[$b];
        });

        $stack = []; // stack of indices moving right

        foreach ($indices as $i) {
            if ($directions[$i] === 'R') {
                $stack[] = $i;
            } else { // direction L
                while (!empty($stack) && $healths[$i] > 0) {
                    $j = array_pop($stack); // right-moving robot

                    if ($healths[$i] > $healths[$j]) {
                        // left robot destroys right robot
                        $healths[$i]--;
                        // right robot is gone, continue with possible next collision
                        if ($healths[$i] == 0) {
                            break; // left robot died after decrement
                        }
                    } elseif ($healths[$i] < $healths[$j]) {
                        // right robot destroys left robot
                        $healths[$j]--;
                        $healths[$i] = 0;
                        if ($healths[$j] > 0) {
                            $stack[] = $j; // survivor stays on stack
                        }
                        break; // left robot dead
                    } else { // equal health, both destroyed
                        $healths[$i] = 0;
                        $healths[$j] = 0;
                        break; // left robot dead
                    }
                }
            }
        }

        $result = [];
        for ($i = 0; $i < $n; $i++) {
            if ($healths[$i] > 0) {
                $result[] = $healths[$i];
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func survivedRobotsHealths(_ positions: [Int], _ healths: [Int], _ directions: String) -> [Int] {
        let n = positions.count
        var idxs = Array(0..<n)
        idxs.sort { positions[$0] < positions[$1] }
        
        var health = healths
        let dirs = Array(directions)
        var stack = [Int]()   // indices of right‑moving robots that are still alive
        
        for i in idxs {
            if dirs[i] == "R" {
                stack.append(i)
            } else { // 'L'
                while !stack.isEmpty && health[i] > 0 {
                    let topIdx = stack[stack.count - 1]
                    if health[topIdx] < health[i] {
                        // right robot destroyed
                        health[topIdx] = 0
                        health[i] -= 1
                        stack.removeLast()
                    } else if health[topIdx] > health[i] {
                        // left robot destroyed
                        health[topIdx] -= 1
                        health[i] = 0
                        break
                    } else { // equal health
                        health[topIdx] = 0
                        health[i] = 0
                        stack.removeLast()
                        break
                    }
                }
            }
        }
        
        var result = [Int]()
        for i in 0..<n {
            if health[i] > 0 {
                result.append(health[i])
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun survivedRobotsHealths(positions: IntArray, healths: IntArray, directions: String): List<Int> {
        val n = positions.size
        // indices sorted by position
        val idx = (0 until n).toMutableList()
        idx.sortWith(compareBy { positions[it] })
        val stack = java.util.ArrayDeque<Int>()
        for (i in idx) {
            if (directions[i] == 'R') {
                stack.addLast(i)
            } else {
                var curIdx = i
                while (stack.isNotEmpty() && healths[curIdx] > 0) {
                    val topIdx = stack.removeLast()
                    when {
                        healths[topIdx] < healths[curIdx] -> {
                            // right-moving robot destroyed, left robot loses 1 health
                            healths[curIdx]--
                            // continue checking next right-moving robot
                        }
                        healths[topIdx] > healths[curIdx] -> {
                            // left-moving robot destroyed, right robot loses 1 health
                            healths[topIdx]--
                            healths[curIdx] = 0
                            // push back the surviving right robot with updated health
                            stack.addLast(topIdx)
                            break
                        }
                        else -> { // equal health, both destroyed
                            healths[topIdx] = 0
                            healths[curIdx] = 0
                            // no need to push back topIdx
                            break
                        }
                    }
                }
            }
        }
        val result = mutableListOf<Int>()
        for (i in 0 until n) {
            if (healths[i] > 0) result.add(healths[i])
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> survivedRobotsHealths(List<int> positions, List<int> healths, String directions) {
    int n = positions.length;
    List<int> idx = List.generate(n, (i) => i);
    idx.sort((a, b) => positions[a].compareTo(positions[b]));

    List<int> stack = [];

    for (int i in idx) {
      if (directions[i] == 'R') {
        stack.add(i);
      } else { // direction L
        while (stack.isNotEmpty && healths[i] > 0) {
          int j = stack.last;
          if (healths[j] < healths[i]) {
            // Right-moving robot dies
            healths[j] = 0;
            healths[i] -= 1;
            stack.removeLast();
            // continue checking next right-moving robot
          } else if (healths[j] > healths[i]) {
            // Left-moving robot dies
            healths[i] = 0;
            healths[j] -= 1;
            if (healths[j] == 0) {
              stack.removeLast();
            }
            break; // left robot destroyed, stop collisions for it
          } else {
            // Equal health, both die
            healths[j] = 0;
            healths[i] = 0;
            stack.removeLast();
            break;
          }
        }
      }
    }

    List<int> result = [];
    for (int i = 0; i < n; i++) {
      if (healths[i] > 0) {
        result.add(healths[i]);
      }
    }
    return result;
  }
}
```

## Golang

```go
import "sort"

func survivedRobotsHealths(positions []int, healths []int, directions string) []int {
	n := len(positions)
	type robot struct{ pos, idx int }
	ordered := make([]robot, n)
	for i := 0; i < n; i++ {
		ordered[i] = robot{positions[i], i}
	}
	sort.Slice(ordered, func(i, j int) bool { return ordered[i].pos < ordered[j].pos })

	h := make([]int, n)
	copy(h, healths)

	stack := []int{} // indices of right‑moving robots
	for _, r := range ordered {
		i := r.idx
		if directions[i] == 'R' {
			stack = append(stack, i)
		} else { // 'L'
			for len(stack) > 0 && h[i] > 0 {
				topIdx := stack[len(stack)-1]
				stack = stack[:len(stack)-1] // pop

				if h[topIdx] < h[i] {
					h[topIdx] = 0
					h[i]--
				} else if h[topIdx] > h[i] {
					h[topIdx]--
					h[i] = 0
					stack = append(stack, topIdx) // surviving right robot stays on stack
					break
				} else { // equal health
					h[topIdx] = 0
					h[i] = 0
					break
				}
			}
		}
	}

	res := []int{}
	for i := 0; i < n; i++ {
		if h[i] > 0 {
			res = append(res, h[i])
		}
	}
	return res
}
```

## Ruby

```ruby
def survived_robots_healths(positions, healths, directions)
  n = positions.size
  order = (0...n).to_a.sort_by { |i| positions[i] }
  stack = []

  order.each do |i|
    if directions[i] == 'R'
      stack << i
    else
      while !stack.empty? && healths[i] > 0
        j = stack.pop
        if healths[j] > healths[i]
          healths[j] -= 1
          healths[i] = 0
          stack << j
          break
        elsif healths[j] < healths[i]
          healths[i] -= 1
          # right robot destroyed, continue checking next right robot
        else
          healths[j] = 0
          healths[i] = 0
          break
        end
      end
    end
  end

  result = []
  (0...n).each { |i| result << healths[i] if healths[i] > 0 }
  result
end
```

## Scala

```scala
object Solution {
  def survivedRobotsHealths(positions: Array[Int], healths: Array[Int], directions: String): List[Int] = {
    val n = positions.length
    // indices sorted by position
    val order = (0 until n).toArray.sortBy(positions(_))
    // mutable copy of healths
    val h = healths.clone()
    import java.util.ArrayDeque
    val stack = new ArrayDeque[Int]() // stores indices of right-moving robots

    for (i <- order) {
      if (directions.charAt(i) == 'R') {
        stack.addLast(i)
      } else { // moving left
        var cur = i
        while (!stack.isEmpty && h(cur) > 0) {
          val top = stack.peekLast()
          if (h(top) == 0) {
            stack.removeLast()
          } else if (h(cur) == h(top)) {
            h(cur) = 0
            h(top) = 0
            stack.removeLast()
          } else if (h(cur) > h(top)) {
            // right robot dies
            h(top) = 0
            stack.removeLast()
            h(cur) -= 1
          } else { // left robot has less health
            h(cur) = 0
            h(top) -= 1
            if (h(top) == 0) {
              stack.removeLast()
            }
          }
        }
      }
    }

    val result = scala.collection.mutable.ListBuffer[Int]()
    for (i <- 0 until n) {
      if (h(i) > 0) result += h(i)
    }
    result.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn survived_robots_healths(
        positions: Vec<i32>,
        mut healths: Vec<i32>,
        directions: String,
    ) -> Vec<i32> {
        let n = positions.len();
        let dirs = directions.as_bytes();

        // indices sorted by position
        let mut order: Vec<usize> = (0..n).collect();
        order.sort_by_key(|&i| positions[i]);

        let mut stack: Vec<usize> = Vec::new(); // stores indices of right-moving robots

        for &idx in order.iter() {
            if dirs[idx] == b'R' {
                stack.push(idx);
            } else {
                while let Some(&top_idx) = stack.last() {
                    if healths[idx] <= 0 {
                        break;
                    }
                    // pop the right-moving robot to resolve collision
                    let j = stack.pop().unwrap();
                    if healths[j] > healths[idx] {
                        // left robot dies, right loses 1 and stays on stack
                        healths[j] -= 1;
                        healths[idx] = 0;
                        stack.push(j);
                        break;
                    } else if healths[j] < healths[idx] {
                        // right robot dies, left loses 1 and may continue colliding
                        healths[idx] -= 1;
                        healths[j] = 0;
                        // continue with next right-moving robot (if any)
                    } else {
                        // equal health, both die
                        healths[j] = 0;
                        healths[idx] = 0;
                        break;
                    }
                }
            }
        }

        let mut result = Vec::new();
        for h in healths.iter() {
            if *h > 0 {
                result.push(*h);
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (survived-robots-healths positions healths directions)
  (-> (listof exact-integer?) (listof exact-integer?) string? (listof exact-integer?))
  (let* ((n (length positions))
         (pos-vec (list->vector positions))
         (health-vec (list->vector healths))
         (indices (for/list ([i (in-range n)]) i))
         (sorted-indices
          (sort indices < #:key (lambda (i) (vector-ref pos-vec i))))
         (stack '()))
    (define (process-left cur-idx)
      (let loop ()
        (if (or (= (vector-ref health-vec cur-idx) 0) (null? stack))
            (void)
            (let* ((top-idx (car stack))
                   (h-top (vector-ref health-vec top-idx))
                   (h-cur (vector-ref health-vec cur-idx)))
              (cond
                [(> h-top h-cur)
                 (vector-set! health-vec top-idx (- h-top 1))
                 (vector-set! health-vec cur-idx 0)]
                [(< h-top h-cur)
                 (vector-set! health-vec cur-idx (- h-cur 1))
                 (vector-set! health-vec top-idx 0)
                 (set! stack (cdr stack))
                 (loop)]
                [else
                 (vector-set! health-vec cur-idx 0)
                 (vector-set! health-vec top-idx 0)
                 (set! stack (cdr stack))])))))
    (for ([i sorted-indices])
      (if (char=? (string-ref directions i) #\R)
          (set! stack (cons i stack))
          (process-left i)))
    (let loop ((idx 0) (acc '()))
      (if (= idx n)
          (reverse acc)
          (let ((h (vector-ref health-vec idx)))
            (if (> h 0)
                (loop (+ idx 1) (cons h acc))
                (loop (+ idx 1) acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([survived_robots_healths/3]).

-spec survived_robots_healths(Positions :: [integer()], Healths :: [integer()], Directions :: unicode:unicode_binary()) -> [integer()].
survived_robots_healths(Positions, Healths, Directions) ->
    N = length(Positions),
    Indices = lists:seq(0, N - 1),

    % pair positions with original indices and sort by position
    PosIdxPairs = lists:zip(Positions, Indices),
    Sorted = lists:keysort(1, PosIdxPairs),

    DirList = binary_to_list(Directions),
    DirMap = maps:from_list(lists:zip(Indices, DirList)),
    HealthMap0 = maps:from_list(lists:zip(Indices, Healths)),

    FinalHealthMap = process_sorted(Sorted, DirMap, HealthMap0, []),

    collect_survivors(Indices, FinalHealthMap).

% --------------------------------------------------------------------
% Process robots in order of increasing position
process_sorted([], _DirMap, HMap, _Stack) ->
    HMap;
process_sorted([{_Pos, Idx} | Rest], DirMap, HMap, Stack) ->
    Dir = maps:get(Idx, DirMap),
    case Dir of
        $R ->
            process_sorted(Rest, DirMap, HMap, [Idx | Stack]);
        $L ->
            CurHealth = maps:get(Idx, HMap),
            {NewHMap, NewStack} = process_left(CurHealth, Idx, Stack, HMap),
            process_sorted(Rest, DirMap, NewHMap, NewStack)
    end.

% --------------------------------------------------------------------
% Resolve collisions for a left‑moving robot against the stack of right robots
process_left(CurHealth, LIdx, [], HMap) ->
    % No more right robots to collide with
    UpdatedMap = maps:put(LIdx, CurHealth, HMap),
    {UpdatedMap, []};
process_left(CurHealth, LIdx, [RIdx | RestStack], HMap) when CurHealth > 0 ->
    RHealth = maps:get(RIdx, HMap),
    cond
        (RHealth > CurHealth) ->
            NewRHealth = RHealth - 1,
            HMap1 = maps:put(RIdx, NewRHealth, HMap),
            HMap2 = maps:put(LIdx, 0, HMap1),
            {HMap2, [RIdx | RestStack]};
        (RHealth < CurHealth) ->
            NewLHealth = CurHealth - 1,
            HMap1 = maps:put(RIdx, 0, HMap),
            process_left(NewLHealth, LIdx, RestStack, HMap1);
        true -> % equal health
            HMap1 = maps:put(RIdx, 0, HMap),
            HMap2 = maps:put(LIdx, 0, HMap1),
            {HMap2, RestStack}
    end;
process_left(_CurHealth, LIdx, Stack, HMap) ->
    % Left robot already dead
    UpdatedMap = maps:put(LIdx, 0, HMap),
    {UpdatedMap, Stack}.

% --------------------------------------------------------------------
% Gather surviving robots' healths in original order
collect_survivors([], _HMap) ->
    [];
collect_survivors([Idx | Rest], HMap) ->
    Health = maps:get(Idx, HMap),
    case Health > 0 of
        true -> [Health | collect_survivors(Rest, HMap)];
        false -> collect_survivors(Rest, HMap)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec survived_robots_healths(positions :: [integer], healths :: [integer], directions :: String.t) :: [integer]
  def survived_robots_healths(positions, healths, directions) do
    n = length(positions)

    # indices paired with positions for sorting
    indexed =
      Enum.with_index(positions)
      |> Enum.map(fn {pos, idx} -> {pos, idx} end)
      |> Enum.sort_by(fn {pos, _idx} -> pos end)

    # functional array for healths (allows O(log n) updates)
    health_arr = :array.from_list(healths)

    final_arr = process(indexed, [], health_arr, directions)

    # collect survivors in original order
    result_rev =
      Enum.reduce(0..(n - 1), [], fn i, acc ->
        h = :array.get(i, final_arr)
        if h > 0, do: [h | acc], else: acc
      end)

    Enum.reverse(result_rev)
  end

  defp process([], _stack, health_arr, _dir), do: health_arr

  defp process([{_pos, idx} | rest], stack, health_arr, dir) do
    case :binary.at(dir, idx) do
      ?R ->
        process(rest, [idx | stack], health_arr, dir)

      ?L ->
        {new_stack, new_health_arr} = collide_left(idx, stack, health_arr)
        process(rest, new_stack, new_health_arr, dir)
    end
  end

  defp collide_left(_cur_idx, [], health_arr), do: {[], health_arr}

  defp collide_left(cur_idx, stack, health_arr) do
    cur_health = :array.get(cur_idx, health_arr)

    if cur_health <= 0 do
      {stack, health_arr}
    else
      [top_idx | rest_stack] = stack
      top_health = :array.get(top_idx, health_arr)

      cond do
        top_health > cur_health ->
          # top survives with decreased health; current destroyed
          new_top_h = top_health - 1
          ha1 = :array.set(top_idx, new_top_h, health_arr)
          ha2 = :array.set(cur_idx, 0, ha1)
          {[top_idx | rest_stack], ha2}

        top_health < cur_health ->
          # current survives with decreased health; top destroyed
          new_cur_h = cur_health - 1
          ha1 = :array.set(cur_idx, new_cur_h, health_arr)
          ha2 = :array.set(top_idx, 0, ha1)
          collide_left(cur_idx, rest_stack, ha2)

        true ->
          # equal health, both destroyed
          ha1 = :array.set(cur_idx, 0, health_arr)
          ha2 = :array.set(top_idx, 0, ha1)
          {rest_stack, ha2}
      end
    end
  end
end
```
