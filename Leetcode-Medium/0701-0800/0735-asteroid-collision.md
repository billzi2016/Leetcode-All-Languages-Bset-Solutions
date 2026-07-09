# 0735. Asteroid Collision

## Cpp

```cpp
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> st;
        for (int a : asteroids) {
            bool alive = true;
            while (alive && a < 0 && !st.empty() && st.back() > 0) {
                if (abs(st.back()) < abs(a)) {
                    st.pop_back(); // previous asteroid destroyed, continue checking
                } else if (abs(st.back()) == abs(a)) {
                    st.pop_back();
                    alive = false; // both destroy each other
                } else { // previous asteroid larger
                    alive = false; // current asteroid destroyed
                }
            }
            if (alive) st.push_back(a);
        }
        return st;
    }
};
```

## Java

```java
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        int n = asteroids.length;
        int[] stack = new int[n];
        int top = -1;
        for (int a : asteroids) {
            boolean alive = true;
            while (alive && top >= 0 && a < 0 && stack[top] > 0) {
                if (Math.abs(a) > Math.abs(stack[top])) {
                    // current asteroid destroys the one on stack
                    top--;
                } else if (Math.abs(a) == Math.abs(stack[top])) {
                    // both destroy each other
                    top--;
                    alive = false;
                } else {
                    // stack top destroys current asteroid
                    alive = false;
                }
            }
            if (alive) {
                stack[++top] = a;
            }
        }
        int[] result = new int[top + 1];
        System.arraycopy(stack, 0, result, 0, top + 1);
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                top = stack[-1]
                if abs(a) > top:
                    stack.pop()
                    continue
                elif abs(a) == top:
                    stack.pop()
                # In both equal or smaller case, current asteroid is destroyed
                break
            else:
                # No collision occurred
                stack.append(a)
        return stack
```

## Python3

```python
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack: List[int] = []
        for a in asteroids:
            alive = True
            while alive and stack and stack[-1] > 0 and a < 0:
                top = stack[-1]
                if top < -a:
                    stack.pop()
                    continue
                elif top == -a:
                    stack.pop()
                    alive = False
                    break
                else:  # top > -a
                    alive = False
                    break
            if alive:
                stack.append(a)
        return stack
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* asteroidCollision(int* asteroids, int asteroidsSize, int* returnSize) {
    int *stack = (int *)malloc(sizeof(int) * asteroidsSize);
    int top = 0;
    
    for (int i = 0; i < asteroidsSize; ++i) {
        int cur = asteroids[i];
        int alive = 1;
        
        while (top > 0 && cur < 0 && stack[top - 1] > 0) {
            if (abs(stack[top - 1]) < abs(cur)) {
                // left asteroid explodes
                top--;
                continue; // keep checking with next left-moving asteroid
            } else if (abs(stack[top - 1]) == abs(cur)) {
                // both explode
                top--;
                alive = 0;
                break;
            } else {
                // right asteroid larger, current explodes
                alive = 0;
                break;
            }
        }
        
        if (alive) {
            stack[top++] = cur;
        }
    }
    
    int *result = (int *)malloc(sizeof(int) * top);
    for (int i = 0; i < top; ++i) {
        result[i] = stack[i];
    }
    free(stack);
    
    *returnSize = top;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] AsteroidCollision(int[] asteroids) {
        var stack = new System.Collections.Generic.List<int>();
        foreach (int a in asteroids) {
            bool alive = true;
            while (alive && a < 0 && stack.Count > 0 && stack[stack.Count - 1] > 0) {
                int top = stack[stack.Count - 1];
                if (Math.Abs(top) < Math.Abs(a)) {
                    // top asteroid explodes
                    stack.RemoveAt(stack.Count - 1);
                    // continue checking with next top
                } else if (Math.Abs(top) == Math.Abs(a)) {
                    // both explode
                    stack.RemoveAt(stack.Count - 1);
                    alive = false;
                } else {
                    // current asteroid explodes
                    alive = false;
                }
            }
            if (alive) {
                stack.Add(a);
            }
        }
        return stack.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision = function(asteroids) {
    const stack = [];
    for (const a of asteroids) {
        let alive = true;
        while (
            alive &&
            a < 0 && // current moving left
            stack.length > 0 &&
            stack[stack.length - 1] > 0 // top moving right
        ) {
            const top = stack[stack.length - 1];
            if (Math.abs(top) < Math.abs(a)) {
                // top asteroid explodes
                stack.pop();
                // continue checking with next top
            } else if (Math.abs(top) === Math.abs(a)) {
                // both explode
                stack.pop();
                alive = false;
            } else {
                // current asteroid explodes
                alive = false;
            }
        }
        if (alive) {
            stack.push(a);
        }
    }
    return stack;
};
```

## Typescript

```typescript
function asteroidCollision(asteroids: number[]): number[] {
    const stack: number[] = [];
    for (const a of asteroids) {
        let alive = true;
        while (
            alive &&
            a < 0 &&
            stack.length > 0 &&
            stack[stack.length - 1] > 0
        ) {
            const top = stack[stack.length - 1];
            if (Math.abs(top) < Math.abs(a)) {
                stack.pop();
                continue;
            } else if (Math.abs(top) === Math.abs(a)) {
                stack.pop();
                alive = false;
                break;
            } else {
                alive = false;
                break;
            }
        }
        if (alive) stack.push(a);
    }
    return stack;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $asteroids
     * @return Integer[]
     */
    function asteroidCollision($asteroids) {
        $stack = [];
        foreach ($asteroids as $a) {
            $alive = true;
            while ($alive && $a < 0 && !empty($stack)) {
                $top = end($stack);
                if ($top > 0) {
                    if (abs($top) == abs($a)) {
                        array_pop($stack);
                        $alive = false; // both explode
                    } elseif (abs($top) > abs($a)) {
                        $alive = false; // current asteroid explodes
                    } else {
                        array_pop($stack); // top asteroid explodes, continue checking
                    }
                } else {
                    break; // no collision possible
                }
            }
            if ($alive) {
                $stack[] = $a;
            }
        }
        return $stack;
    }
}
```

## Swift

```swift
class Solution {
    func asteroidCollision(_ asteroids: [Int]) -> [Int] {
        var stack = [Int]()
        for a in asteroids {
            var alive = true
            while alive && a < 0 && !stack.isEmpty && stack.last! > 0 {
                let top = stack.last!
                if abs(top) < abs(a) {
                    stack.removeLast()
                    // continue checking with next asteroid in stack
                } else if abs(top) == abs(a) {
                    stack.removeLast()
                    alive = false
                } else { // top larger
                    alive = false
                }
            }
            if alive {
                stack.append(a)
            }
        }
        return stack
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun asteroidCollision(asteroids: IntArray): IntArray {
        val stack = java.util.ArrayDeque<Int>()
        for (a in asteroids) {
            var cur = a
            var destroyed = false
            while (!stack.isEmpty() && cur < 0 && stack.peekLast() > 0) {
                val top = stack.peekLast()
                if (kotlin.math.abs(top) == kotlin.math.abs(cur)) {
                    stack.pollLast()
                    destroyed = true
                    break
                } else if (kotlin.math.abs(top) > kotlin.math.abs(cur)) {
                    destroyed = true
                    break
                } else {
                    stack.pollLast()
                }
            }
            if (!destroyed) {
                stack.addLast(cur)
            }
        }
        val result = IntArray(stack.size)
        var i = 0
        for (v in stack) {
            result[i++] = v
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> asteroidCollision(List<int> asteroids) {
    List<int> stack = [];
    for (int a in asteroids) {
      bool alive = true;
      while (alive && a < 0 && stack.isNotEmpty && stack.last > 0) {
        int top = stack.last;
        if (top < -a) {
          stack.removeLast();
        } else if (top == -a) {
          stack.removeLast();
          alive = false;
        } else {
          alive = false;
        }
      }
      if (alive) {
        stack.add(a);
      }
    }
    return stack;
  }
}
```

## Golang

```go
func asteroidCollision(asteroids []int) []int {
    var stack []int
    for _, a := range asteroids {
        alive := true
        for alive && len(stack) > 0 && a < 0 && stack[len(stack)-1] > 0 {
            top := stack[len(stack)-1]
            if abs(top) < abs(a) {
                // top asteroid explodes
                stack = stack[:len(stack)-1]
                continue
            } else if abs(top) == abs(a) {
                // both explode
                stack = stack[:len(stack)-1]
                alive = false
                break
            } else {
                // current asteroid explodes
                alive = false
                break
            }
        }
        if alive {
            stack = append(stack, a)
        }
    }
    return stack
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```

## Ruby

```ruby
# @param {Integer[]} asteroids
# @return {Integer[]}
def asteroid_collision(asteroids)
  stack = []
  asteroids.each do |a|
    if a > 0
      stack << a
    else
      alive = true
      while alive && !stack.empty? && stack[-1] > 0
        top = stack[-1]
        if top < -a
          stack.pop
        elsif top == -a
          stack.pop
          alive = false
        else
          alive = false
        end
      end
      stack << a if alive && (stack.empty? || stack[-1] < 0)
    end
  end
  stack
end
```

## Scala

```scala
object Solution {
    def asteroidCollision(asteroids: Array[Int]): Array[Int] = {
        val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
        for (a <- asteroids) {
            var alive = true
            while (alive && a < 0 && stack.nonEmpty && stack.last > 0) {
                val top = stack.last
                if (math.abs(a) > top) {
                    stack.remove(stack.size - 1)
                } else if (math.abs(a) == top) {
                    stack.remove(stack.size - 1)
                    alive = false
                } else {
                    alive = false
                }
            }
            if (alive) stack.append(a)
        }
        stack.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
        let mut stack: Vec<i32> = Vec::new();
        for &a in asteroids.iter() {
            let mut cur = a;
            while let Some(&top) = stack.last() {
                if top > 0 && cur < 0 {
                    if top < -cur {
                        // current asteroid destroys the top one
                        stack.pop();
                        continue;
                    } else if top == -cur {
                        // both destroy each other
                        stack.pop();
                        cur = 0;
                        break;
                    } else {
                        // top asteroid survives, current destroyed
                        cur = 0;
                        break;
                    }
                } else {
                    break;
                }
            }
            if cur != 0 {
                stack.push(cur);
            }
        }
        stack
    }
}
```

## Racket

```racket
(define/contract (asteroid-collision asteroids)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let loop ((rest asteroids) (stack '()))
    (if (null? rest)
        (reverse stack)
        (let ((curr (car rest)))
          (let recur ((a curr) (stk stack))
            (cond
              [(or (null? stk) (not (and (> (car stk) 0) (< a 0))))
               (if (= a 0)
                   (loop (cdr rest) stk)
                   (loop (cdr rest) (cons a stk)))]
              [else
               (define top (car stk))
               (cond
                 [(< (abs top) (abs a))
                  (recur a (cdr stk))]
                 [(= (abs top) (abs a))
                  (loop (cdr rest) (cdr stk))]
                 [else
                  (loop (cdr rest) stk))]))))))))
```

## Erlang

```erlang
-spec asteroid_collision(Asteroids :: [integer()]) -> [integer()].
asteroid_collision(Asteroids) ->
    process(Asteroids, []).

process([], Stack) ->
    lists:reverse(Stack);
process([A|Rest], Stack) when A > 0 ->
    process(Rest, [A|Stack]);
process([A|Rest], Stack) ->
    NewStack = handle_negative(A, Stack),
    process(Rest, NewStack).

handle_negative(A, []) ->
    [A];
handle_negative(A, [Top|Rest]) when Top > 0 ->
    case erlang:abs(Top) of
        TAbs when TAbs < erlang:abs(A) ->
            handle_negative(A, Rest);
        TAbs when TAbs == erlang:abs(A) ->
            Rest;
        _ ->
            [Top|Rest]
    end;
handle_negative(A, Stack) ->
    [A|Stack].
```

## Elixir

```elixir
defmodule Solution do
  @spec asteroid_collision(asteroids :: [integer]) :: [integer]
  def asteroid_collision(asteroids) do
    asteroids
    |> Enum.reduce([], fn cur, stack -> resolve(cur, stack) end)
    |> Enum.reverse()
  end

  # Positive asteroid always moves right, just push onto the stack.
  defp resolve(cur, stack) when cur > 0, do: [cur | stack]

  # No asteroids to collide with.
  defp resolve(_cur, []), do: [_cur]

  # Current asteroid is moving left; handle possible collisions.
  defp resolve(cur, [top | rest] = stack) when cur < 0 do
    if top > 0 do
      cond do
        top < -cur ->
          # Top asteroid explodes; continue checking with the same current asteroid.
          resolve(cur, rest)

        top == -cur ->
          # Both explode.
          rest

        top > -cur ->
          # Current asteroid explodes; keep the stack as is.
          stack
      end
    else
      # Top asteroid also moving left; no collision.
      [cur | stack]
    end
  end
end
```
