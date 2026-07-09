# 1806. Minimum Number of Operations to Reinitialize a Permutation

## Cpp

```cpp
class Solution {
public:
    int reinitializePermutation(int n) {
        int steps = 0;
        int i = 1;
        do {
            if (i % 2 == 0)
                i = i / 2;
            else
                i = n / 2 + (i - 1) / 2;
            ++steps;
        } while (i != 1);
        return steps;
    }
};
```

## Java

```java
class Solution {
    public int reinitializePermutation(int n) {
        if (n == 2) return 1;
        int mod = n - 1;
        int cnt = 0;
        int cur = 1;
        do {
            cur = (cur * 2) % mod;
            cnt++;
        } while (cur != 1);
        return cnt;
    }
}
```

## Python

```python
class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        original = list(range(n))
        perm = original[:]
        cnt = 0
        while True:
            arr = [0] * n
            half = n // 2
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[half + (i - 1) // 2]
            cnt += 1
            if arr == original:
                return cnt
            perm = arr
```

## Python3

```python
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        pos = 1
        cnt = 0
        while True:
            if pos % 2 == 0:
                pos //= 2
            else:
                pos = n // 2 + (pos - 1) // 2
            cnt += 1
            if pos == 1:
                return cnt
```

## C

```c
int reinitializePermutation(int n){
    if (n == 2) return 1;
    int pos = 1, steps = 0;
    do{
        pos = (pos * 2) % (n - 1);
        ++steps;
    }while(pos != 1);
    return steps;
}
```

## Csharp

```csharp
public class Solution {
    public int ReinitializePermutation(int n) {
        int pos = 1;
        int steps = 0;
        do {
            if (pos % 2 == 0)
                pos = pos / 2;
            else
                pos = n / 2 + (pos - 1) / 2;
            steps++;
        } while (pos != 1);
        return steps;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var reinitializePermutation = function(n) {
    let pos = 1;
    let steps = 0;
    do {
        if (pos % 2 === 0) {
            pos = pos / 2;
        } else {
            pos = n / 2 + Math.floor((pos - 1) / 2);
        }
        steps++;
    } while (pos !== 1);
    return steps;
};
```

## Typescript

```typescript
function reinitializePermutation(n: number): number {
    let pos = 1;
    let steps = 0;
    do {
        if (pos % 2 === 0) {
            pos = pos / 2;
        } else {
            pos = n / 2 + (pos - 1) / 2;
        }
        steps++;
    } while (pos !== 1);
    return steps;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function reinitializePermutation($n) {
        $cnt = 0;
        $pos = 1; // track the position of element 1
        $half = intdiv($n, 2);
        do {
            if ($pos % 2 == 0) {
                $pos = intdiv($pos, 2);
            } else {
                $pos = $half + intdiv($pos - 1, 2);
            }
            $cnt++;
        } while ($pos != 1);
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func reinitializePermutation(_ n: Int) -> Int {
        if n == 2 { return 1 }
        let mod = n - 1
        var cur = 2 % mod
        var steps = 1
        while cur != 1 {
            cur = (cur * 2) % mod
            steps += 1
        }
        return steps
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reinitializePermutation(n: Int): Int {
        var pos = 1
        var steps = 0
        do {
            pos = if (pos % 2 == 0) {
                pos / 2
            } else {
                n / 2 + (pos - 1) / 2
            }
            steps++
        } while (pos != 1)
        return steps
    }
}
```

## Dart

```dart
class Solution {
  int reinitializePermutation(int n) {
    int pos = 1;
    int steps = 0;
    do {
      if (pos % 2 == 0) {
        pos = pos ~/ 2;
      } else {
        pos = n ~/ 2 + (pos - 1) ~/ 2;
      }
      steps++;
    } while (pos != 1);
    return steps;
  }
}
```

## Golang

```go
func reinitializePermutation(n int) int {
	if n == 2 {
		return 1
	}
	mod := n - 1
	cur, steps := 1, 0
	for {
		cur = (cur * 2) % mod
		steps++
		if cur == 1 {
			break
		}
	}
	return steps
}
```

## Ruby

```ruby
def reinitialize_permutation(n)
  pos = 1
  count = 0
  loop do
    if pos.even?
      pos = pos / 2
    else
      pos = n / 2 + (pos - 1) / 2
    end
    count += 1
    break if pos == 1
  end
  count
end
```

## Scala

```scala
object Solution {
    def reinitializePermutation(n: Int): Int = {
        if (n == 2) return 1
        val mod = n - 1
        var pos = 1
        var cnt = 0
        do {
            pos = (pos * 2) % mod
            cnt += 1
        } while (pos != 1)
        cnt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reinitialize_permutation(n: i32) -> i32 {
        if n == 2 {
            return 1;
        }
        let mut cnt = 0i32;
        let mut pos: i64 = 1;
        let m: i64 = (n as i64) - 1; // modulus, odd
        loop {
            pos = (pos * 2) % m;
            cnt += 1;
            if pos == 1 {
                break;
            }
        }
        cnt
    }
}
```

## Racket

```racket
(define/contract (reinitialize-permutation n)
  (-> exact-integer? exact-integer?)
  (let* ((half (quotient n 2))
         (next-pos
          (lambda (i)
            (if (even? i)
                (quotient i 2)
                (+ half (quotient (- i 1) 2))))))
    (let loop ((pos 1) (cnt 0))
      (let* ((new-pos (next-pos pos))
             (new-cnt (+ cnt 1)))
        (if (= new-pos 1)
            new-cnt
            (loop new-pos new-cnt))))))
```

## Erlang

```erlang
-module(solution).
-export([reinitialize_permutation/1]).

-spec reinitialize_permutation(N :: integer()) -> integer().
reinitialize_permutation(2) ->
    1;
reinitialize_permutation(N) when N > 2, N rem 2 =:= 0 ->
    Mod = N - 1,
    find_order(2 rem Mod, Mod, 1).

-spec find_order(Cur :: integer(), Mod :: integer(), Steps :: integer()) -> integer().
find_order(1, _Mod, Steps) ->
    Steps;
find_order(Cur, Mod, Steps) ->
    Next = (Cur * 2) rem Mod,
    find_order(Next, Mod, Steps + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec reinitialize_permutation(n :: integer) :: integer
  def reinitialize_permutation(2), do: 1

  def reinitialize_permutation(n) do
    mod = n - 1
    find_k(mod, rem(2, mod), 1)
  end

  defp find_k(_mod, 1, k), do: k
  defp find_k(mod, cur, k) do
    find_k(mod, rem(cur * 2, mod), k + 1)
  end
end
```
