# 0838. Push Dominoes

## Cpp

```cpp
class Solution {
public:
    string pushDominoes(string dominoes) {
        int n = dominoes.size();
        vector<int> force(n, 0);
        int f = 0;
        for (int i = 0; i < n; ++i) {
            if (dominoes[i] == 'R') {
                f = n;
            } else if (dominoes[i] == 'L') {
                f = 0;
            } else {
                f = max(f - 1, 0);
            }
            force[i] = f;
        }
        f = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (dominoes[i] == 'L') {
                f = n;
            } else if (dominoes[i] == 'R') {
                f = 0;
            } else {
                f = max(f - 1, 0);
            }
            force[i] -= f;
        }
        string result;
        result.reserve(n);
        for (int i = 0; i < n; ++i) {
            if (force[i] > 0) result.push_back('R');
            else if (force[i] < 0) result.push_back('L');
            else result.push_back('.');
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public String pushDominoes(String dominoes) {
        int n = dominoes.length();
        int[] forces = new int[n];
        int force = 0;
        // Scan from left to right, calculate force exerted by 'R'
        for (int i = 0; i < n; i++) {
            char c = dominoes.charAt(i);
            if (c == 'R') {
                force = n;
            } else if (c == 'L') {
                force = 0;
            } else {
                force = Math.max(force - 1, 0);
            }
            forces[i] = force;
        }
        // Scan from right to left, calculate force exerted by 'L' (negative)
        force = 0;
        for (int i = n - 1; i >= 0; i--) {
            char c = dominoes.charAt(i);
            if (c == 'L') {
                force = n;
            } else if (c == 'R') {
                force = 0;
            } else {
                force = Math.max(force - 1, 0);
            }
            forces[i] -= force;
        }
        // Build result based on net forces
        char[] res = new char[n];
        for (int i = 0; i < n; i++) {
            if (forces[i] > 0) {
                res[i] = 'R';
            } else if (forces[i] < 0) {
                res[i] = 'L';
            } else {
                res[i] = '.';
            }
        }
        return new String(res);
    }
}
```

## Python

```python
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        n = len(dominoes)
        forces = [0] * n

        # Left to right pass for 'R' forces
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force

        # Right to left pass for 'L' forces (negative)
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        # Build result based on net force
        res = []
        for f in forces:
            if f > 0:
                res.append('R')
            elif f < 0:
                res.append('L')
            else:
                res.append('.')
        return ''.join(res)
```

## Python3

```python
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n
        force = 0
        for i, ch in enumerate(dominoes):
            if ch == 'R':
                force = n
            elif ch == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force
        force = 0
        for i in range(n - 1, -1, -1):
            ch = dominoes[i]
            if ch == 'L':
                force = n
            elif ch == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force
        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')
        return ''.join(result)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* pushDominoes(char* dominoes) {
    int n = strlen(dominoes);
    int *force = (int *)malloc(sizeof(int) * n);
    if (!force) return NULL;

    int f = 0;
    for (int i = 0; i < n; ++i) {
        if (dominoes[i] == 'R') {
            f = n;
        } else if (dominoes[i] == 'L') {
            f = 0;
        } else {
            if (f > 0) f--;
        }
        force[i] = f;
    }

    f = 0;
    for (int i = n - 1; i >= 0; --i) {
        if (dominoes[i] == 'L') {
            f = n;
        } else if (dominoes[i] == 'R') {
            f = 0;
        } else {
            if (f > 0) f--;
        }
        force[i] -= f; // subtract leftward force
    }

    char *res = (char *)malloc(sizeof(char) * (n + 1));
    if (!res) {
        free(force);
        return NULL;
    }

    for (int i = 0; i < n; ++i) {
        if (force[i] > 0)
            res[i] = 'R';
        else if (force[i] < 0)
            res[i] = 'L';
        else
            res[i] = '.';
    }
    res[n] = '\0';

    free(force);
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string PushDominoes(string dominoes)
    {
        int n = dominoes.Length;
        int[] force = new int[n];
        int f = 0;

        // Left to right pass for 'R' forces
        for (int i = 0; i < n; i++)
        {
            char c = dominoes[i];
            if (c == 'R')
                f = n;
            else if (c == 'L')
                f = 0;
            else
                f = Math.Max(f - 1, 0);
            force[i] = f;
        }

        // Right to left pass for 'L' forces (subtract)
        f = 0;
        for (int i = n - 1; i >= 0; i--)
        {
            char c = dominoes[i];
            if (c == 'L')
                f = n;
            else if (c == 'R')
                f = 0;
            else
                f = Math.Max(f - 1, 0);
            force[i] -= f;
        }

        char[] result = new char[n];
        for (int i = 0; i < n; i++)
        {
            if (force[i] > 0)
                result[i] = 'R';
            else if (force[i] < 0)
                result[i] = 'L';
            else
                result[i] = '.';
        }

        return new string(result);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} dominoes
 * @return {string}
 */
var pushDominoes = function(dominoes) {
    const n = dominoes.length;
    const forces = new Array(n).fill(0);
    let force = 0;
    
    // Left to right, calculate force from 'R'
    for (let i = 0; i < n; i++) {
        if (dominoes[i] === 'R') {
            force = n;
        } else if (dominoes[i] === 'L') {
            force = 0;
        } else {
            force = Math.max(force - 1, 0);
        }
        forces[i] += force;
    }
    
    // Right to left, calculate force from 'L' (negative)
    force = 0;
    for (let i = n - 1; i >= 0; i--) {
        if (dominoes[i] === 'L') {
            force = n;
        } else if (dominoes[i] === 'R') {
            force = 0;
        } else {
            force = Math.max(force - 1, 0);
        }
        forces[i] -= force;
    }
    
    // Build result based on net force
    const res = [];
    for (let i = 0; i < n; i++) {
        if (forces[i] > 0) {
            res.push('R');
        } else if (forces[i] < 0) {
            res.push('L');
        } else {
            res.push('.');
        }
    }
    
    return res.join('');
};
```

## Typescript

```typescript
function pushDominoes(dominoes: string): string {
    const n = dominoes.length;
    const forces = new Array<number>(n).fill(0);
    let force = 0;

    // Left to right pass for 'R' forces
    for (let i = 0; i < n; i++) {
        if (dominoes[i] === 'R') {
            force = n;
        } else if (dominoes[i] === 'L') {
            force = 0;
        } else {
            force = Math.max(force - 1, 0);
        }
        forces[i] = force;
    }

    // Right to left pass for 'L' forces
    force = 0;
    for (let i = n - 1; i >= 0; i--) {
        if (dominoes[i] === 'L') {
            force = n;
        } else if (dominoes[i] === 'R') {
            force = 0;
        } else {
            force = Math.max(force - 1, 0);
        }
        forces[i] -= force; // subtract because leftward force is negative
    }

    const result: string[] = [];
    for (let i = 0; i < n; i++) {
        if (forces[i] > 0) {
            result.push('R');
        } else if (forces[i] < 0) {
            result.push('L');
        } else {
            result.push('.');
        }
    }

    return result.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $dominoes
     * @return String
     */
    function pushDominoes($dominoes) {
        $n = strlen($dominoes);
        if ($n == 0) return "";
        $forces = array_fill(0, $n, 0);

        // Left to right pass (R forces)
        $force = 0;
        for ($i = 0; $i < $n; $i++) {
            $c = $dominoes[$i];
            if ($c === 'R') {
                $force = $n;
            } elseif ($c === 'L') {
                $force = 0;
            } else {
                $force = max($force - 1, 0);
            }
            $forces[$i] += $force;
        }

        // Right to left pass (L forces)
        $force = 0;
        for ($i = $n - 1; $i >= 0; $i--) {
            $c = $dominoes[$i];
            if ($c === 'L') {
                $force = $n;
            } elseif ($c === 'R') {
                $force = 0;
            } else {
                $force = max($force - 1, 0);
            }
            $forces[$i] -= $force;
        }

        // Build result
        $result = '';
        for ($i = 0; $i < $n; $i++) {
            if ($forces[$i] > 0) {
                $result .= 'R';
            } elseif ($forces[$i] < 0) {
                $result .= 'L';
            } else {
                $result .= '.';
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func pushDominoes(_ dominoes: String) -> String {
        let n = dominoes.count
        var chars = Array(dominoes)
        var forces = [Int](repeating: 0, count: n)

        var force = 0
        for i in 0..<n {
            if chars[i] == "R" {
                force = n
            } else if chars[i] == "L" {
                force = 0
            } else {
                force = max(force - 1, 0)
            }
            forces[i] += force
        }

        force = 0
        var i = n - 1
        while i >= 0 {
            if chars[i] == "L" {
                force = n
            } else if chars[i] == "R" {
                force = 0
            } else {
                force = max(force - 1, 0)
            }
            forces[i] -= force
            i -= 1
        }

        var result = [Character]()
        result.reserveCapacity(n)
        for i in 0..<n {
            if forces[i] > 0 {
                result.append("R")
            } else if forces[i] < 0 {
                result.append("L")
            } else {
                result.append(".")
            }
        }

        return String(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun pushDominoes(dominoes: String): String {
        val n = dominoes.length
        val forces = IntArray(n)
        var force = 0
        for (i in 0 until n) {
            when (dominoes[i]) {
                'R' -> force = n
                'L' -> force = 0
                else -> if (force > 0) force--
            }
            forces[i] = force
        }
        force = 0
        for (i in n - 1 downTo 0) {
            when (dominoes[i]) {
                'L' -> force = n
                'R' -> force = 0
                else -> if (force > 0) force--
            }
            forces[i] -= force
        }
        val sb = StringBuilder()
        for (i in 0 until n) {
            sb.append(
                when {
                    forces[i] > 0 -> 'R'
                    forces[i] < 0 -> 'L'
                    else -> '.'
                }
            )
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String pushDominoes(String dominoes) {
    int n = dominoes.length;
    List<int> forces = List.filled(n, 0);
    int force = 0;

    // Left to right pass (R forces)
    for (int i = 0; i < n; i++) {
      String c = dominoes[i];
      if (c == 'R') {
        force = n;
      } else if (c == 'L') {
        force = 0;
      } else {
        force = force > 0 ? force - 1 : 0;
      }
      forces[i] = force;
    }

    // Right to left pass (L forces) and build result
    StringBuffer sb = StringBuffer();
    force = 0;
    for (int i = n - 1; i >= 0; i--) {
      String c = dominoes[i];
      if (c == 'L') {
        force = n;
      } else if (c == 'R') {
        force = 0;
      } else {
        force = force > 0 ? force - 1 : 0;
      }
      int net = forces[i] - force; // positive => R, negative => L
      if (net > 0) {
        sb.write('R');
      } else if (net < 0) {
        sb.write('L');
      } else {
        sb.write('.');
      }
    }

    return sb.toString();
  }
}
```

## Golang

```go
import "strings"

func pushDominoes(dominoes string) string {
	n := len(dominoes)
	forces := make([]int, n)

	// Left to right pass: calculate force from 'R'
	force := 0
	for i := 0; i < n; i++ {
		switch dominoes[i] {
		case 'R':
			force = n
		case 'L':
			force = 0
		default:
			if force > 0 {
				force--
			}
		}
		forces[i] = force
	}

	// Right to left pass: calculate force from 'L' (negative)
	force = 0
	for i := n - 1; i >= 0; i-- {
		switch dominoes[i] {
		case 'L':
			force = n
		case 'R':
			force = 0
		default:
			if force > 0 {
				force--
			}
		}
		forces[i] -= force
	}

	var sb strings.Builder
	sb.Grow(n)
	for i := 0; i < n; i++ {
		if forces[i] > 0 {
			sb.WriteByte('R')
		} else if forces[i] < 0 {
			sb.WriteByte('L')
		} else {
			sb.WriteByte('.')
		}
	}
	return sb.String()
}
```

## Ruby

```ruby
def push_dominoes(dominoes)
  n = dominoes.length
  chars = dominoes.chars
  forces = Array.new(n, 0)

  force = 0
  (0...n).each do |i|
    case chars[i]
    when 'R'
      force = n
    when 'L'
      force = 0
    else
      force = [force - 1, 0].max
    end
    forces[i] = force
  end

  result = Array.new(n)
  force = 0
  (n - 1).downto(0) do |i|
    case chars[i]
    when 'L'
      force = n
    when 'R'
      force = 0
    else
      force = [force - 1, 0].max
    end
    net = forces[i] - force
    result[i] =
      if net > 0
        'R'
      elsif net < 0
        'L'
      else
        '.'
      end
  end

  result.join
end
```

## Scala

```scala
object Solution {
    def pushDominoes(dominoes: String): String = {
        val n = dominoes.length
        val force = new Array[Int](n)
        var f = 0
        for (i <- 0 until n) {
            dominoes.charAt(i) match {
                case 'R' => f = n
                case 'L' => f = 0
                case '.' => if (f > 0) f -= 1
            }
            force(i) = f
        }
        f = 0
        for (i <- (n - 1) to 0 by -1) {
            dominoes.charAt(i) match {
                case 'L' => f = n
                case 'R' => f = 0
                case '.' => if (f > 0) f -= 1
            }
            force(i) -= f
        }
        val sb = new StringBuilder(n)
        for (i <- 0 until n) {
            if (force(i) > 0) sb.append('R')
            else if (force(i) < 0) sb.append('L')
            else sb.append('.')
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn push_dominoes(dominoes: String) -> String {
        let chars = dominoes.as_bytes();
        let n = chars.len();
        let mut forces = vec![0i32; n];

        // Left to right pass, compute force from 'R'
        let mut force = 0i32;
        for i in 0..n {
            match chars[i] as char {
                'R' => force = n as i32,
                'L' => force = 0,
                _ => {
                    if force > 0 {
                        force -= 1;
                    }
                }
            }
            forces[i] = force;
        }

        // Right to left pass, compute force from 'L' (negative)
        let mut force = 0i32;
        for i in (0..n).rev() {
            match chars[i] as char {
                'L' => force = n as i32,
                'R' => force = 0,
                _ => {
                    if force > 0 {
                        force -= 1;
                    }
                }
            }
            forces[i] -= force; // subtract because leftward force is negative
        }

        // Build result string
        let mut res_bytes = Vec::with_capacity(n);
        for &f in &forces {
            let c = if f > 0 { b'R' } else if f < 0 { b'L' } else { b'.' };
            res_bytes.push(c);
        }
        String::from_utf8(res_bytes).unwrap()
    }
}
```

## Racket

```racket
(define/contract (push-dominoes dominoes)
  (-> string? string?)
  (let* ((n (string-length dominoes))
         (forces (make-vector n 0)))
    ;; left‑to‑right pass: influence of 'R'
    (let loop ((i 0) (f 0))
      (when (< i n)
        (define c (string-ref dominoes i))
        (cond [(char=? c #\R) (set! f n)]
              [(char=? c #\L) (set! f 0)])
        (unless (or (char=? c #\R) (char=? c #\L))
          (set! f (max 0 (- f 1))))
        (vector-set! forces i f)
        (loop (+ i 1) f)))
    ;; right‑to‑left pass: influence of 'L' and build result
    (let ((result (make-string n #\.)))
      (let loop ((i (- n 1)) (f 0))
        (when (>= i 0)
          (define c (string-ref dominoes i))
          (cond [(char=? c #\L) (set! f n)]
                [(char=? c #\R) (set! f 0)])
          (unless (or (char=? c #\L) (char=? c #\R))
            (set! f (max 0 (- f 1))))
          (define net (- (vector-ref forces i) f))
          (cond [(> net 0) (string-set! result i #\R)]
                [(< net 0) (string-set! result i #\L)]
                [else       (string-set! result i #\.)])
          (loop (- i 1) f)))
      result)))
```

## Erlang

```erlang
-spec push_dominoes(Dominoes :: unicode:unicode_binary()) -> unicode:unicode_binary().
push_dominoes(Dominoes) ->
    Chars = binary_to_list(Dominoes),
    N = length(Chars),

    LeftForces = left_pass(Chars, N, 0, []),
    RightForcesRev = right_pass(lists:reverse(Chars), N, 0, []),
    RightForces = lists:reverse(RightForcesRev),

    ResultChars = combine(LeftForces, RightForces, []),
    list_to_binary(ResultChars).

left_pass([], _N, _F, Acc) ->
    lists:reverse(Acc);
left_pass([C|Rest], N, F, Acc) ->
    NewF = case C of
        $R -> N;
        $L -> 0;
        _. -> erlang:max(F-1, 0)
    end,
    left_pass(Rest, N, NewF, [NewF|Acc]).

right_pass([], _N, _F, Acc) ->
    lists:reverse(Acc);
right_pass([C|Rest], N, F, Acc) ->
    NewF = case C of
        $L -> N;
        $R -> 0;
        _. -> erlang:max(F-1, 0)
    end,
    right_pass(Rest, N, NewF, [NewF|Acc]).

combine([], [], Acc) ->
    lists:reverse(Acc);
combine([L|Ls], [R|Rs], Acc) ->
    Char = if
        L > R -> $R;
        L < R -> $L;
        true  -> $.
    end,
    combine(Ls, Rs, [Char|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec push_dominoes(dominoes :: String.t) :: String.t
  def push_dominoes(dominoes) do
    chars = String.to_charlist(dominoes)
    n = length(chars)

    {left_forces, _} =
      Enum.map_reduce(chars, 0, fn ch, force ->
        new_force =
          cond do
            ch == ?R -> n
            ch == ?L -> 0
            true -> max(force - 1, 0)
          end

        {new_force, new_force}
      end)

    rev_chars = Enum.reverse(chars)
    rev_left = Enum.reverse(left_forces)

    {_final_right, result} =
      Enum.reduce(Enum.zip(rev_chars, rev_left), {0, []}, fn {ch, left_f},
                                                             {right_force, acc} ->
        new_right =
          cond do
            ch == ?L -> n
            ch == ?R -> 0
            true -> max(right_force - 1, 0)
          end

        net = left_f - new_right

        final_char =
          cond do
            net > 0 -> ?R
            net < 0 -> ?L
            true -> ?. 
          end

        {new_right, [final_char | acc]}
      end)

    List.to_string(result)
  end
end
```
