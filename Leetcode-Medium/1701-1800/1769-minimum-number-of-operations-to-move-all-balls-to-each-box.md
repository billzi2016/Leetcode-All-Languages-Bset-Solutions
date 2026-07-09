# 1769. Minimum Number of Operations to Move All Balls to Each Box

## Cpp

```cpp
class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.size();
        vector<int> answer(n, 0);
        int balls = 0;
        int moves = 0;
        for (int i = 0; i < n; ++i) {
            answer[i] += moves;
            if (boxes[i] == '1') ++balls;
            moves += balls;
        }
        balls = 0;
        moves = 0;
        for (int i = n - 1; i >= 0; --i) {
            answer[i] += moves;
            if (boxes[i] == '1') ++balls;
            moves += balls;
        }
        return answer;
    }
};
```

## Java

```java
class Solution {
    public int[] minOperations(String boxes) {
        int n = boxes.length();
        int[] answer = new int[n];
        int balls = 0;
        int moves = 0;
        // left to right pass
        for (int i = 0; i < n; i++) {
            answer[i] += moves;
            if (boxes.charAt(i) == '1') {
                balls++;
            }
            moves += balls;
        }
        // right to left pass
        balls = 0;
        moves = 0;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] += moves;
            if (boxes.charAt(i) == '1') {
                balls++;
            }
            moves += balls;
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        ans = [0] * n

        balls = 0
        moves = 0
        for i in range(n):
            ans[i] += moves
            if boxes[i] == '1':
                balls += 1
            moves += balls

        balls = 0
        moves = 0
        for i in range(n - 1, -1, -1):
            ans[i] += moves
            if boxes[i] == '1':
                balls += 1
            moves += balls

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n

        balls_left = 0
        ops_left = 0
        for i in range(n):
            ans[i] += ops_left
            if boxes[i] == '1':
                balls_left += 1
            ops_left += balls_left

        balls_right = 0
        ops_right = 0
        for i in range(n - 1, -1, -1):
            ans[i] += ops_right
            if boxes[i] == '1':
                balls_right += 1
            ops_right += balls_right

        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minOperations(char* boxes, int* returnSize) {
    int n = (int)strlen(boxes);
    *returnSize = n;
    int *ans = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; ++i) ans[i] = 0;

    int balls = 0, moves = 0;
    for (int i = 0; i < n; ++i) {
        ans[i] += moves;
        if (boxes[i] == '1') balls++;
        moves += balls;
    }

    balls = 0;
    moves = 0;
    for (int i = n - 1; i >= 0; --i) {
        ans[i] += moves;
        if (boxes[i] == '1') balls++;
        moves += balls;
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] MinOperations(string boxes)
    {
        int n = boxes.Length;
        int[] answer = new int[n];
        int ballsToLeft = 0;
        int movesToLeft = 0;

        for (int i = 0; i < n; i++)
        {
            answer[i] = movesToLeft;
            if (boxes[i] == '1')
                ballsToLeft++;
            movesToLeft += ballsToLeft;
        }

        int ballsToRight = 0;
        int movesToRight = 0;

        for (int i = n - 1; i >= 0; i--)
        {
            answer[i] += movesToRight;
            if (boxes[i] == '1')
                ballsToRight++;
            movesToRight += ballsToRight;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} boxes
 * @return {number[]}
 */
var minOperations = function(boxes) {
    const n = boxes.length;
    const answer = new Array(n).fill(0);
    
    // Left to right pass
    let ballsToLeft = 0;
    let movesToLeft = 0;
    for (let i = 0; i < n; ++i) {
        answer[i] += movesToLeft;
        if (boxes[i] === '1') ballsToLeft++;
        movesToLeft += ballsToLeft;
    }
    
    // Right to left pass
    let ballsToRight = 0;
    let movesToRight = 0;
    for (let i = n - 1; i >= 0; --i) {
        answer[i] += movesToRight;
        if (boxes[i] === '1') ballsToRight++;
        movesToRight += ballsToRight;
    }
    
    return answer;
};
```

## Typescript

```typescript
function minOperations(boxes: string): number[] {
    const n = boxes.length;
    const ans = new Array<number>(n).fill(0);
    let balls = 0, moves = 0;

    // left to right pass
    for (let i = 0; i < n; i++) {
        ans[i] = moves;
        if (boxes.charAt(i) === '1') balls++;
        moves += balls;
    }

    // right to left pass
    balls = 0;
    moves = 0;
    for (let i = n - 1; i >= 0; i--) {
        ans[i] += moves;
        if (boxes.charAt(i) === '1') balls++;
        moves += balls;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $boxes
     * @return Integer[]
     */
    function minOperations($boxes) {
        $n = strlen($boxes);
        $answer = array_fill(0, $n, 0);

        // Left to right pass
        $balls = 0;
        $moves = 0;
        for ($i = 0; $i < $n; $i++) {
            $answer[$i] += $moves;
            if ($boxes[$i] === '1') {
                $balls++;
            }
            $moves += $balls;
        }

        // Right to left pass
        $balls = 0;
        $moves = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            $answer[$i] += $moves;
            if ($boxes[$i] === '1') {
                $balls++;
            }
            $moves += $balls;
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ boxes: String) -> [Int] {
        let n = boxes.count
        var ans = [Int](repeating: 0, count: n)
        let chars = Array(boxes)
        
        var balls = 0
        var moves = 0
        // left to right pass
        for i in 0..<n {
            ans[i] += moves
            if chars[i] == "1" {
                balls += 1
            }
            moves += balls
        }
        
        balls = 0
        moves = 0
        // right to left pass
        for i in stride(from: n - 1, through: 0, by: -1) {
            ans[i] += moves
            if chars[i] == "1" {
                balls += 1
            }
            moves += balls
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minOperations(boxes: String): IntArray {
        val n = boxes.length
        val ans = IntArray(n)
        var balls = 0
        var ops = 0
        // left to right pass
        for (i in 0 until n) {
            ans[i] += ops
            if (boxes[i] == '1') {
                balls++
            }
            ops += balls
        }
        // right to left pass
        balls = 0
        ops = 0
        for (i in n - 1 downTo 0) {
            ans[i] += ops
            if (boxes[i] == '1') {
                balls++
            }
            ops += balls
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> minOperations(String boxes) {
    int n = boxes.length;
    List<int> answer = List.filled(n, 0);
    int balls = 0;
    int moves = 0;

    // Left to right pass
    for (int i = 0; i < n; i++) {
      answer[i] += moves;
      if (boxes.codeUnitAt(i) == 49) { // '1'
        balls++;
      }
      moves += balls;
    }

    // Right to left pass
    balls = 0;
    moves = 0;
    for (int i = n - 1; i >= 0; i--) {
      answer[i] += moves;
      if (boxes.codeUnitAt(i) == 49) { // '1'
        balls++;
      }
      moves += balls;
    }

    return answer;
  }
}
```

## Golang

```go
package main

func minOperations(boxes string) []int {
	n := len(boxes)
	ans := make([]int, n)

	balls, ops := 0, 0
	for i := 0; i < n; i++ {
		ans[i] = ops
		if boxes[i] == '1' {
			balls++
		}
		ops += balls
	}

	balls, ops = 0, 0
	for i := n - 1; i >= 0; i-- {
		ans[i] += ops
		if boxes[i] == '1' {
			balls++
		}
		ops += balls
	}

	return ans
}
```

## Ruby

```ruby
# @param {String} boxes
# @return {Integer[]}
def min_operations(boxes)
  n = boxes.length
  answer = Array.new(n, 0)

  balls = 0
  moves = 0
  (0...n).each do |i|
    answer[i] += moves
    balls += 1 if boxes[i] == '1'
    moves += balls
  end

  balls = 0
  moves = 0
  (n - 1).downto(0) do |i|
    answer[i] += moves
    balls += 1 if boxes[i] == '1'
    moves += balls
  end

  answer
end
```

## Scala

```scala
object Solution {
    def minOperations(boxes: String): Array[Int] = {
        val n = boxes.length
        val ans = new Array[Int](n)
        var ballsLeft = 0
        var movesLeft = 0
        for (i <- 0 until n) {
            ans(i) += movesLeft
            if (boxes.charAt(i) == '1') ballsLeft += 1
            movesLeft += ballsLeft
        }
        var ballsRight = 0
        var movesRight = 0
        for (i <- (n - 1) to 0 by -1) {
            ans(i) += movesRight
            if (boxes.charAt(i) == '1') ballsRight += 1
            movesRight += ballsRight
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(boxes: String) -> Vec<i32> {
        let bytes = boxes.as_bytes();
        let n = bytes.len();
        let mut ans = vec![0i32; n];
        let mut balls = 0i32;
        let mut moves = 0i32;

        // left to right pass
        for i in 0..n {
            ans[i] += moves;
            if bytes[i] == b'1' {
                balls += 1;
            }
            moves += balls;
        }

        // right to left pass
        balls = 0;
        moves = 0;
        for i in (0..n).rev() {
            ans[i] += moves;
            if bytes[i] == b'1' {
                balls += 1;
            }
            moves += balls;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (min-operations boxes)
  (-> string? (listof exact-integer?))
  (let* ((n (string-length boxes))
         (ans (make-vector n 0)))
    ;; left to right pass
    (let loop ((i 0) (balls 0) (ops 0))
      (when (< i n)
        (vector-set! ans i (+ (vector-ref ans i) ops))
        (let* ((c (string-ref boxes i))
               (new-balls (if (char=? c #\1) (+ balls 1) balls))
               (new-ops (+ ops new-balls)))
          (loop (+ i 1) new-balls new-ops))))
    ;; right to left pass
    (let loop ((i (- n 1)) (balls 0) (ops 0))
      (when (>= i 0)
        (vector-set! ans i (+ (vector-ref ans i) ops))
        (let* ((c (string-ref boxes i))
               (new-balls (if (char=? c #\1) (+ balls 1) balls))
               (new-ops (+ ops new-balls)))
          (loop (- i 1) new-balls new-ops))))
    ;; convert vector to list
    (let loop ((i 0) (lst '()))
      (if (= i n)
          (reverse lst)
          (loop (+ i 1) (cons (vector-ref ans i) lst))))))
```

## Erlang

```erlang
-spec min_operations(Boxes :: unicode:unicode_binary()) -> [integer()].
min_operations(Boxes) ->
    Chars = binary_to_list(Boxes),
    LeftAns = left_pass(Chars, 0, 0, []),
    RevChars = lists:reverse(Chars),
    RightAns = right_pass(RevChars, 0, 0, []),
    lists:zipwith(fun(L, R) -> L + R end, LeftAns, RightAns).

left_pass([], _, _, Acc) ->
    lists:reverse(Acc);
left_pass([C | Cs], BallsLeft, MovesLeft, Acc) ->
    Ans = MovesLeft,
    NewBalls = case C of
        $1 -> BallsLeft + 1;
        _ -> BallsLeft
    end,
    NewMoves = MovesLeft + NewBalls,
    left_pass(Cs, NewBalls, NewMoves, [Ans | Acc]).

right_pass([], _, _, Acc) ->
    lists:reverse(Acc);
right_pass([C | Cs], BallsRight, MovesRight, Acc) ->
    Ans = MovesRight,
    NewBalls = case C of
        $1 -> BallsRight + 1;
        _ -> BallsRight
    end,
    NewMoves = MovesRight + NewBalls,
    right_pass(Cs, NewBalls, NewMoves, [Ans | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(boxes :: String.t) :: [integer]
  def min_operations(boxes) do
    chars = String.to_charlist(boxes)

    # Left to right pass
    {_balls_left, _ops_left, left_rev} =
      Enum.reduce(chars, {0, 0, []}, fn c, {balls, ops, acc} ->
        new_acc = [ops | acc]
        balls2 = if c == ?1, do: balls + 1, else: balls
        ops2 = ops + balls2
        {balls2, ops2, new_acc}
      end)

    left = Enum.reverse(left_rev)

    # Right to left pass (process reversed string)
    {_balls_right, _ops_right, right} =
      Enum.reduce(Enum.reverse(chars), {0, 0, []}, fn c, {balls, ops, acc} ->
        new_acc = [ops | acc]
        balls2 = if c == ?1, do: balls + 1, else: balls
        ops2 = ops + balls2
        {balls2, ops2, new_acc}
      end)

    Enum.zip(left, right) |> Enum.map(fn {l, r} -> l + r end)
  end
end
```
