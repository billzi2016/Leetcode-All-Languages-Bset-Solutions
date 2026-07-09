# 2310. Sum of Numbers With Units Digit K

## Cpp

```cpp
class Solution {
public:
    int minimumNumbers(int num, int k) {
        if (num == 0) return 0;
        for (int cnt = 1; cnt <= num; ++cnt) {
            if (num >= cnt * k && (num - cnt * k) % 10 == 0) {
                return cnt;
            }
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int minimumNumbers(int num, int k) {
        if (num == 0) return 0;
        if (k == 0) {
            return (num % 10 == 0) ? 1 : -1;
        }
        for (int cnt = 1; cnt <= num / k + 1; cnt++) {
            int remaining = num - cnt * k;
            if (remaining >= 0 && remaining % 10 == 0) {
                return cnt;
            }
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def minimumNumbers(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        if num == 0:
            return 0
        if k == 0:
            return 1 if num % 10 == 0 else -1
        for i in range(1, 11):
            if i * k > num:
                break
            if (num - i * k) % 10 == 0:
                return i
        return -1
```

## Python3

```python
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        if k == 0:
            return 1 if num % 10 == 0 else -1
        max_m = num // k + 1
        for m in range(1, max_m + 1):
            if num >= m * k and (num - m * k) % 10 == 0:
                return m
        return -1
```

## C

```c
int minimumNumbers(int num, int k){
    if (num == 0) return 0;
    if (k == 0){
        if (num % 10 == 0) return num / 10;
        return -1;
    }
    for (int i = 1; i <= num / k; ++i){
        int base = i * k;
        if ((num - base) % 10 == 0) return i;
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumNumbers(int num, int k) {
        if (num == 0) return 0;
        if (k == 0) {
            return (num % 10 == 0) ? 1 : -1;
        }
        for (int cnt = 1; cnt * k <= num; cnt++) {
            if ((num - cnt * k) % 10 == 0) return cnt;
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @param {number} k
 * @return {number}
 */
var minimumNumbers = function(num, k) {
    if (num === 0) return 0;
    if (k === 0) {
        return num % 10 === 0 ? Math.floor(num / 10) : -1;
    }
    const maxCnt = Math.floor(num / k);
    for (let cnt = 1; cnt <= maxCnt; ++cnt) {
        if ((num - cnt * k) % 10 === 0) return cnt;
    }
    return -1;
};
```

## Typescript

```typescript
function minimumNumbers(num: number, k: number): number {
    if (num === 0) return 0;
    if (k === 0) {
        return num % 10 === 0 ? 1 : -1;
    }
    for (let cnt = 1; ; cnt++) {
        const remaining = num - cnt * k;
        if (remaining < 0) break;
        if (remaining % 10 === 0) return cnt;
    }
    return -1;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $num
     * @param Integer $k
     * @return Integer
     */
    function minimumNumbers($num, $k) {
        if ($num == 0) return 0;
        if ($k == 0) {
            return ($num % 10 == 0) ? 1 : -1;
        }
        for ($m = 1; $m * $k <= $num; $m++) {
            if ((($m * $k) % 10) == ($num % 10)) {
                return $m;
            }
        }
        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func minimumNumbers(_ num: Int, _ k: Int) -> Int {
        if num == 0 { return 0 }
        if k == 0 {
            return (num % 10 == 0) ? 1 : -1
        }
        var m = 1
        while m * k <= num {
            let remaining = num - m * k
            if remaining % 10 == 0 {
                return m
            }
            m += 1
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumNumbers(num: Int, k: Int): Int {
        if (num == 0) return 0
        if (k == 0) {
            return if (num % 10 == 0) 1 else -1
        }
        val maxCount = num / k
        for (c in 1..maxCount) {
            if ((c * k) % 10 == num % 10 && c * k <= num) {
                return c
            }
        }
        return -1
    }
}
```

## Dart

```dart
class Solution {
  int minimumNumbers(int num, int k) {
    if (num == 0) return 0;
    if (k == 0) {
      return (num % 10 == 0) ? (num ~/ 10) : -1;
    }
    for (int cnt = 1; cnt <= num; ++cnt) {
      if ((cnt * k) % 10 == num % 10 && cnt * k <= num) {
        return cnt;
      }
    }
    return -1;
  }
}
```

## Golang

```go
func minimumNumbers(num int, k int) int {
	if num == 0 {
		return 0
	}
	if k == 0 {
		if num%10 == 0 {
			return 1
		}
		return -1
	}
	for i := 1; i*k <= num; i++ {
		if (num-i*k)%10 == 0 {
			return i
		}
	}
	return -1
}
```

## Ruby

```ruby
def minimum_numbers(num, k)
  return 0 if num == 0
  if k == 0
    return (num % 10).zero? ? 1 : -1
  end
  max_n = num / k
  (1..max_n).each do |n|
    remainder = num - n * k
    return n if remainder % 10 == 0
  end
  -1
end
```

## Scala

```scala
object Solution {
    def minimumNumbers(num: Int, k: Int): Int = {
        if (num == 0) return 0
        for (c <- 1 to 1000) {
            val sumK = c * k
            if (sumK % 10 == num % 10 && sumK <= num) {
                return c
            }
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_numbers(num: i32, k: i32) -> i32 {
        if num == 0 {
            return 0;
        }
        for n in 1..=num {
            let used = n * k;
            if used > num {
                break;
            }
            let remaining = num - used;
            if remaining % 10 == 0 {
                return n;
            }
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (minimum-numbers num k)
  (-> exact-integer? exact-integer? exact-integer?)
  (cond
    [(zero? num) 0]
    [(zero? k)
     (if (= (modulo num 10) 0) 1 -1)]
    [else
     (let loop ((c 1)
                (max-c (quotient num k))) ; floor(num/k)
       (cond
         [(> c max-c) -1]
         [(and (= (modulo num 10) (modulo (* c k) 10))
               (>= num (* c k)))
          c]
         [else (loop (+ c 1) max-c)]))]))
```

## Erlang

```erlang
-spec minimum_numbers(Num :: integer(), K :: integer()) -> integer().
minimum_numbers(Num, K) ->
    case Num of
        0 -> 0;
        _ when K =:= 0 ->
            if Num rem 10 =:= 0 -> 1; true -> -1 end;
        _ ->
            MaxI = Num div K,
            find_min(1, MaxI, Num, K)
    end.

find_min(I, MaxI, _Num, _K) when I > MaxI -> -1;
find_min(I, MaxI, Num, K) ->
    Rem = Num - I * K,
    if Rem >= 0, Rem rem 10 =:= 0 -> I;
       true -> find_min(I + 1, MaxI, Num, K)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_numbers(num :: integer, k :: integer) :: integer
  def minimum_numbers(num, k) do
    cond do
      num == 0 ->
        0

      k == 0 ->
        if rem(num, 10) == 0, do: 1, else: -1

      true ->
        find_min(num, k, 1)
    end
  end

  defp find_min(num, k, m) when m * k > num, do: -1

  defp find_min(num, k, m) do
    if rem(num - m * k, 10) == 0 do
      m
    else
      find_min(num, k, m + 1)
    end
  end
end
```
