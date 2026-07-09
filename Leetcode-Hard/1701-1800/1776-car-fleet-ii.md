# 1776. Car Fleet II

## Cpp

```cpp
class Solution {
public:
    vector<double> getCollisionTimes(vector<vector<int>>& cars) {
        int n = cars.size();
        vector<double> ans(n, -1.0);
        vector<int> st; // stack of indices
        for (int i = n - 1; i >= 0; --i) {
            while (!st.empty()) {
                int j = st.back();
                if (cars[i][1] <= cars[j][1]) {
                    // cannot catch up
                    st.pop_back();
                    continue;
                }
                double t = (double)(cars[j][0] - cars[i][0]) / (cars[i][1] - cars[j][1]);
                if (ans[j] > 0 && t >= ans[j]) {
                    // j collides before i reaches it
                    st.pop_back();
                } else {
                    break;
                }
            }
            if (!st.empty()) {
                int j = st.back();
                ans[i] = (double)(cars[j][0] - cars[i][0]) / (cars[i][1] - cars[j][1]);
            }
            st.push_back(i);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public double[] getCollisionTimes(int[][] cars) {
        int n = cars.length;
        double[] ans = new double[n];
        java.util.Deque<Integer> stack = new java.util.ArrayDeque<>();
        for (int i = n - 1; i >= 0; --i) {
            int posI = cars[i][0];
            int speedI = cars[i][1];
            while (!stack.isEmpty()) {
                int j = stack.peek();
                int posJ = cars[j][0];
                int speedJ = cars[j][1];
                if (speedI <= speedJ) {
                    stack.pop(); // cannot catch up
                    continue;
                }
                double t = (double) (posJ - posI) / (speedI - speedJ);
                if (ans[j] < 0 || t <= ans[j]) {
                    ans[i] = t;
                    break;
                } else {
                    stack.pop(); // j collides earlier, try next
                }
            }
            stack.push(i);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        n = len(cars)
        ans = [-1.0] * n
        stack = []  # indices of cars to the right that are potential collision targets
        
        for i in range(n - 1, -1, -1):
            pos_i, speed_i = cars[i]
            while stack:
                j = stack[-1]
                pos_j, speed_j = cars[j]
                
                if speed_i <= speed_j:
                    # cannot catch up to a faster or equal-speed car
                    stack.pop()
                    continue
                
                time = (pos_j - pos_i) / float(speed_i - speed_j)
                
                # If car j never collides, or i catches before j's own collision,
                # then this is the answer for i.
                if ans[j] < 0 or time <= ans[j]:
                    ans[i] = time
                    break
                else:
                    # j would have changed speed before i could catch it
                    stack.pop()
            stack.append(i)
        
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        pos = [c[0] for c in cars]
        speed = [c[1] for c in cars]
        ans = [-1.0] * n
        stack: List[int] = []  # indices of candidate cars to the right

        for i in range(n - 1, -1, -1):
            # Remove cars that cannot be collided with or will collide earlier than we can catch up
            while stack:
                j = stack[-1]
                if speed[i] <= speed[j]:
                    stack.pop()
                    continue
                t = (pos[j] - pos[i]) / (speed[i] - speed[j])
                # If car j collides later than its own collision time, it's not a valid target
                if ans[j] != -1.0 and t >= ans[j]:
                    stack.pop()
                else:
                    break
            if stack:
                j = stack[-1]
                ans[i] = (pos[j] - pos[i]) / (speed[i] - speed[j])
            # push current car as a potential target for cars on the left
            stack.append(i)

        return ans
```

## C

```c
#include <stdlib.h>

double* getCollisionTimes(int** cars, int carsSize, int* carsColSize, int* returnSize) {
    int n = carsSize;
    double *ans = (double *)malloc(sizeof(double) * n);
    for (int i = 0; i < n; ++i) ans[i] = -1.0;

    int *stack = (int *)malloc(sizeof(int) * n);
    int top = -1; // empty stack

    for (int i = n - 1; i >= 0; --i) {
        while (top >= 0) {
            int j = stack[top];
            if (cars[i][1] <= cars[j][1]) { // cannot catch up
                top--;
                continue;
            }
            double t = ((double)(cars[j][0] - cars[i][0])) / (cars[i][1] - cars[j][1]);
            if (ans[j] < 0 || t <= ans[j]) {
                break; // this j is the first collision candidate
            } else {
                top--; // j will collide earlier, discard it
            }
        }
        if (top >= 0) {
            int j = stack[top];
            double t = ((double)(cars[j][0] - cars[i][0])) / (cars[i][1] - cars[j][1]);
            ans[i] = t;
        }
        stack[++top] = i; // push current car as candidate for left cars
    }

    free(stack);
    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public double[] GetCollisionTimes(int[][] cars) {
        int n = cars.Length;
        double[] res = new double[n];
        for (int i = 0; i < n; i++) res[i] = -1.0;
        Stack<int> stack = new Stack<int>(); // indices of candidate cars to the right

        for (int i = n - 1; i >= 0; --i) {
            long posI = cars[i][0];
            long speedI = cars[i][1];

            while (stack.Count > 0) {
                int j = stack.Peek();
                long posJ = cars[j][0];
                long speedJ = cars[j][1];

                if (speedI <= speedJ) {
                    // cannot catch up
                    stack.Pop();
                    continue;
                }

                double t = (double)(posJ - posI) / (speedI - speedJ);

                // If car j never collides, or i catches up before j's own collision,
                // then this is the answer for i.
                if (res[j] < 0 || t <= res[j]) {
                    res[i] = t;
                    break;
                }

                // Otherwise, j would have collided earlier and changed speed,
                // so i cannot collide with j as considered; discard j.
                stack.Pop();
            }

            stack.Push(i);
        }

        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} cars
 * @return {number[]}
 */
var getCollisionTimes = function(cars) {
    const n = cars.length;
    const ans = new Array(n).fill(-1);
    const stack = []; // indices of candidate cars to the right
    
    for (let i = n - 1; i >= 0; i--) {
        const [posI, speedI] = cars[i];
        while (stack.length) {
            const j = stack[stack.length - 1];
            const [posJ, speedJ] = cars[j];
            
            // If current car is slower or equal, it will never catch up
            if (speedI <= speedJ) {
                stack.pop();
                continue;
            }
            
            const t = (posJ - posI) / (speedI - speedJ);
            
            // If j never collides or i catches before j's collision, it's valid
            if (ans[j] === -1 || t <= ans[j]) {
                ans[i] = t;
                break;
            }
            // Otherwise, j will have collided and changed speed before i reaches it
            stack.pop();
        }
        stack.push(i);
    }
    
    return ans;
};
```

## Typescript

```typescript
function getCollisionTimes(cars: number[][]): number[] {
    const n = cars.length;
    const answer = new Array<number>(n).fill(-1);
    const stack: number[] = []; // indices of candidate cars to the right

    for (let i = n - 1; i >= 0; --i) {
        const [posI, speedI] = cars[i];

        while (stack.length) {
            const j = stack[stack.length - 1];
            const [posJ, speedJ] = cars[j];

            // If current car is slower or equal, it will never catch up
            if (speedI <= speedJ) {
                stack.pop();
                continue;
            }

            const t = (posJ - posI) / (speedI - speedJ);

            // If car j never collides or i catches up before j's collision,
            // then this is the answer for i.
            if (answer[j] === -1 || t <= answer[j]) {
                answer[i] = t;
                break;
            }

            // Otherwise, j will collide earlier; discard it and try next candidate
            stack.pop();
        }

        stack.push(i);
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $cars
     * @return Float[]
     */
    function getCollisionTimes($cars) {
        $n = count($cars);
        $pos = [];
        $spd = [];
        for ($i = 0; $i < $n; $i++) {
            $pos[$i] = $cars[$i][0];
            $spd[$i] = $cars[$i][1];
        }

        $ans = array_fill(0, $n, -1.0);
        $stack = []; // indices of candidate cars

        for ($i = $n - 1; $i >= 0; $i--) {
            while (!empty($stack)) {
                $j = end($stack);
                if ($spd[$i] <= $spd[$j]) {
                    array_pop($stack);
                    continue;
                }
                // time to catch up car j
                $t = (float)($pos[$j] - $pos[$i]) / ($spd[$i] - $spd[$j]);
                // if car j never collides or i catches before j's collision
                if ($ans[$j] < 0 || $t <= $ans[$j]) {
                    $ans[$i] = $t;
                    break;
                } else {
                    array_pop($stack);
                }
            }
            $stack[] = $i;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func getCollisionTimes(_ cars: [[Int]]) -> [Double] {
        let n = cars.count
        var answer = Array(repeating: -1.0, count: n)
        var stack = [Int]()  // indices of candidate cars to the right
        
        for i in stride(from: n - 1, through: 0, by: -1) {
            let posI = Double(cars[i][0])
            let speedI = Double(cars[i][1])
            
            while let j = stack.last {
                let posJ = Double(cars[j][0])
                let speedJ = Double(cars[j][1])
                
                // If current car is slower or equal, it will never catch up
                if speedI <= speedJ {
                    stack.removeLast()
                    continue
                }
                
                // Time to collide with car j
                let t = (posJ - posI) / (speedI - speedJ)
                
                // If car j never collides or collision happens before j's own collision,
                // then this is the valid collision time for i.
                if answer[j] < 0 || t <= answer[j] {
                    answer[i] = t
                    break
                } else {
                    // Car j would have collided earlier, so its speed changes;
                    // current car cannot catch it before that, discard j.
                    stack.removeLast()
                }
            }
            
            stack.append(i)
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun getCollisionTimes(cars: Array<IntArray>): DoubleArray {
        val n = cars.size
        val ans = DoubleArray(n) { -1.0 }
        val stack = ArrayDeque<Int>()
        for (i in n - 1 downTo 0) {
            val posI = cars[i][0]
            val speedI = cars[i][1]
            while (!stack.isEmpty()) {
                val j = stack.peekLast()
                val speedJ = cars[j][1]
                if (speedI <= speedJ) {
                    stack.removeLast()
                    continue
                }
                val t = (cars[j][0] - posI).toDouble() / (speedI - speedJ)
                if (ans[j] < 0 || t <= ans[j]) {
                    ans[i] = t
                    break
                } else {
                    stack.removeLast()
                }
            }
            stack.addLast(i)
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<double> getCollisionTimes(List<List<int>> cars) {
    int n = cars.length;
    List<double> ans = List.filled(n, -1.0);
    List<int> stack = [];
    for (int i = n - 1; i >= 0; --i) {
      int posI = cars[i][0];
      int speedI = cars[i][1];
      while (stack.isNotEmpty) {
        int j = stack.last;
        int posJ = cars[j][0];
        int speedJ = cars[j][1];
        if (speedI <= speedJ) {
          stack.removeLast();
          continue;
        }
        double t = (posJ - posI).toDouble() / (speedI - speedJ);
        if (ans[j] < 0 || t <= ans[j]) {
          ans[i] = t;
          break;
        } else {
          stack.removeLast();
        }
      }
      stack.add(i);
    }
    return ans;
  }
}
```

## Golang

```go
func getCollisionTimes(cars [][]int) []float64 {
	n := len(cars)
	ans := make([]float64, n)
	for i := 0; i < n; i++ {
		ans[i] = -1.0
	}
	stack := make([]int, 0)

	for i := n - 1; i >= 0; i-- {
		posI := float64(cars[i][0])
		speedI := float64(cars[i][1])

		// Remove cars that i cannot collide with before they themselves collide
		for len(stack) > 0 {
			j := stack[len(stack)-1]
			posJ := float64(cars[j][0])
			speedJ := float64(cars[j][1])

			if speedI <= speedJ {
				// i is not faster; it will never catch j before j possibly slows down.
				stack = stack[:len(stack)-1]
				continue
			}
			t := (posJ - posI) / (speedI - speedJ)
			if ans[j] > 0 && t >= ans[j] {
				// j would have collided earlier, changing its speed; i cannot meet j first.
				stack = stack[:len(stack)-1]
			} else {
				break
			}
		}

		if len(stack) > 0 {
			j := stack[len(stack)-1]
			ans[i] = (float64(cars[j][0]) - posI) / (speedI - float64(cars[j][1]))
		}
		stack = append(stack, i)
	}
	return ans
}
```

## Ruby

```ruby
def get_collision_times(cars)
  n = cars.length
  ans = Array.new(n, -1.0)
  stack = [] # indices of candidate cars ahead

  (n - 1).downto(0) do |i|
    pos_i, speed_i = cars[i]

    while !stack.empty?
      j = stack[-1]
      pos_j, speed_j = cars[j]

      if speed_i <= speed_j
        stack.pop
        next
      end

      t = (pos_j - pos_i).to_f / (speed_i - speed_j)

      # If car j never collides or i catches up before j's collision, it's valid
      if ans[j] < 0 || t <= ans[j]
        break
      else
        stack.pop
      end
    end

    unless stack.empty?
      j = stack[-1]
      ans[i] = (cars[j][0] - pos_i).to_f / (speed_i - cars[j][1])
    end

    stack << i
  end

  ans
end
```

## Scala

```scala
import scala.collection.mutable
import scala.util.control.Breaks.{break, breakable}

object Solution {
  def getCollisionTimes(cars: Array[Array[Int]]): Array[Double] = {
    val n = cars.length
    val ans = Array.fill[Double](n)(-1.0)
    val stack = mutable.Stack[Int]() // indices of candidate cars

    for (i <- (n - 1) to 0 by -1) {
      var time = -1.0
      breakable {
        while (stack.nonEmpty) {
          val j = stack.top
          if (cars(i)(1) <= cars(j)(1)) {
            // cannot catch up
            stack.pop()
          } else {
            val t = (cars(j)(0).toDouble - cars(i)(0).toDouble) /
                    (cars(i)(1).toDouble - cars(j)(1).toDouble)
            if (ans(j) < 0 || t <= ans(j)) {
              time = t
              break
            } else {
              // j will collide earlier, so its speed changes; discard it
              stack.pop()
            }
          }
        }
      }
      ans(i) = time
      stack.push(i)
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn get_collision_times(cars: Vec<Vec<i32>>) -> Vec<f64> {
        let n = cars.len();
        let mut ans = vec![-1_f64; n];
        let mut stack: Vec<usize> = Vec::new(); // candidate indices to the right

        for i in (0..n).rev() {
            while let Some(&j) = stack.last() {
                // If current car cannot catch up because it's slower or equal speed, discard j
                if cars[i][1] <= cars[j][1] {
                    stack.pop();
                    continue;
                }
                // Time to collide with car j
                let t = (cars[j][0] - cars[i][0]) as f64 / (cars[i][1] - cars[j][1]) as f64;

                // If car j collides earlier than time t, its speed changes before i can catch it
                if ans[j] > 0.0 && t >= ans[j] {
                    stack.pop();
                    continue;
                }

                ans[i] = t;
                break;
            }
            stack.push(i);
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (get-collision-times cars)
  (-> (listof (listof exact-integer?)) (listof flonum?))
  (let* ((n (length cars))
         (pos (make-vector n))
         (spd (make-vector n)))
    ;; fill position and speed vectors
    (for ([i (in-range n)])
      (define pair (list-ref cars i))
      (vector-set! pos i (first pair))
      (vector-set! spd i (second pair)))
    (define ans (make-vector n -1.0))   ; default -1.0
    (define stack '())                  ; monotonic stack of candidate indices

    ;; process cars from right to left
    (for ([i (in-range (sub1 n) -1 -1)])  ; n-1 down to 0 inclusive
      (let ((p-i (vector-ref pos i))
            (s-i (vector-ref spd i)))
        (let loop ()
          (if (null? stack)
              (void)                     ; no candidate, answer stays -1.0
              (let* ((j (car stack))
                     (p-j (vector-ref pos j))
                     (s-j (vector-ref spd j)))
                (cond
                  [(<= s-i s-j)               ; cannot catch up, discard j
                   (set! stack (cdr stack))
                   (loop)]
                  [else
                   (define t (exact->inexact (/ (- p-j p-i) (- s-i s-j))))
                   (if (or (= (vector-ref ans j) -1.0)
                           (<= t (vector-ref ans j)))
                       (begin
                         (vector-set! ans i t))
                       (begin
                         (set! stack (cdr stack))
                         (loop)))])))))
        ;; push current car onto the stack
        (set! stack (cons i stack))))
    ;; convert answer vector to list
    (let loop ((idx 0) (res '()))
      (if (= idx n)
          (reverse res)
          (loop (add1 idx) (cons (vector-ref ans idx) res)))))
```

## Erlang

```erlang
-spec get_collision_times(Cars :: [[integer()]]) -> [float()].
get_collision_times(Cars) ->
    CarsTuple = list_to_tuple(Cars),
    N = tuple_size(CarsTuple),
    AnsArray0 = array:new(N, {default, -1.0}),
    FinalAnsArray = process(N, [], AnsArray0, CarsTuple),
    array:to_list(FinalAnsArray).

process(0, _Stack, AnswerArray, _CarsTuple) ->
    AnswerArray;
process(I, Stack, AnswerArray, CarsTuple) ->
    {PosI, SpeedI} = element(I, CarsTuple),
    case find_collision(PosI, SpeedI, I, Stack, AnswerArray, CarsTuple) of
        {NewStack, undefined} ->
            NewAnsArray = AnswerArray,
            process(I - 1, [I | NewStack], NewAnsArray, CarsTuple);
        {NewStack, Time} ->
            NewAnsArray = array:set(I, Time, AnswerArray),
            process(I - 1, [I | NewStack], NewAnsArray, CarsTuple)
    end.

find_collision(_PosI, _SpeedI, _I, [], _AnsArr, _CarsTuple) ->
    {[], undefined};
find_collision(PosI, SpeedI, I, [J | Rest], AnsArr, CarsTuple) ->
    {PosJ, SpeedJ} = element(J, CarsTuple),
    if
        SpeedI =< SpeedJ ->
            find_collision(PosI, SpeedI, I, Rest, AnsArr, CarsTuple);
        true ->
            Time = (PosJ - PosI) / (SpeedI - SpeedJ),
            CollisionJ = array:get(J, AnsArr),
            if
                CollisionJ < 0 orelse Time =< CollisionJ ->
                    {[J | Rest], Time};
                true ->
                    find_collision(PosI, SpeedI, I, Rest, AnsArr, CarsTuple)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_collision_times(cars :: [[integer]]) :: [float]
  def get_collision_times(cars) do
    n = length(cars)

    positions = :array.from_list(Enum.map(cars, fn [p, _] -> p end))
    speeds = :array.from_list(Enum.map(cars, fn [_ , s] -> s end))

    ans_arr = :array.new(n, default: -1.0)

    {_, final_ans} =
      Enum.reduce((n - 1)..0, {[], ans_arr}, fn i, {stack, ans_acc} ->
        {new_stack, t_opt} = find_collision(i, stack, positions, speeds, ans_acc)

        ans_val = case t_opt do
          nil -> -1.0
          _ -> t_opt
        end

        updated_ans = :array.set(i, ans_val, ans_acc)
        {[i | new_stack], updated_ans}
      end)

    Enum.map(0..(n - 1), fn i -> :array.get(i, final_ans) end)
  end

  defp find_collision(_i, [], _positions, _speeds, _ans_arr), do: {[], nil}

  defp find_collision(i, [j | rest] = stack, positions, speeds, ans_arr) do
    si = :array.get(i, speeds)
    sj = :array.get(j, speeds)

    if si <= sj do
      # cannot catch up, discard j
      find_collision(i, rest, positions, speeds, ans_arr)
    else
      pi = :array.get(i, positions)
      pj = :array.get(j, positions)
      t = (pj - pi) / (si - sj) * 1.0
      ans_j = :array.get(j, ans_arr)

      if ans_j != -1.0 && t >= ans_j do
        # j collides earlier, discard it
        find_collision(i, rest, positions, speeds, ans_arr)
      else
        {stack, t}
      end
    end
  end
end
```
