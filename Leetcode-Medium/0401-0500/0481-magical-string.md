# 0481. Magical String

## Cpp

```cpp
class Solution {
public:
    int magicalString(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        std::vector<int> s;
        s.reserve(n + 2);
        s.push_back(1);
        s.push_back(2);
        s.push_back(2);
        int countOnes = 1; // only the first element is '1'
        int i = 2; // read pointer
        while ((int)s.size() < n) {
            int nextVal = 3 - s.back(); // alternates between 1 and 2
            int repeat = s[i];
            for (int k = 0; k < repeat && (int)s.size() < n; ++k) {
                s.push_back(nextVal);
                if (nextVal == 1) ++countOnes;
            }
            ++i;
        }
        return countOnes;
    }
};
```

## Java

```java
class Solution {
    public int magicalString(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1; // "1"
        // first three characters are "122"
        if (n <= 3) return 1;
        
        int size = Math.max(3, n) + 2;
        int[] s = new int[size];
        s[0] = 1;
        s[1] = 2;
        s[2] = 2;
        
        int head = 3; // next position to write
        int i = 2;    // read pointer
        int countOnes = 1; // first element is '1'
        
        while (head < n) {
            int times = s[i];
            int val = (s[head - 1] == 1) ? 2 : 1;
            for (int k = 0; k < times && head < n; k++) {
                s[head++] = val;
                if (val == 1) countOnes++;
            }
            i++;
        }
        return countOnes;
    }
}
```

## Python

```python
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        # initial magical string "122"
        s = [1, 2, 2]
        i = 2          # pointer to the count element
        cur = 1        # next number to append (alternates between 1 and 2)
        while len(s) < n:
            repeat = s[i]
            s.extend([cur] * repeat)
            cur ^= 3   # toggle: 1->2, 2->1
            i += 1
        return sum(1 for x in s[:n] if x == 1)
```

## Python3

```python
class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        # Precomputed for small n
        if n <= 3:
            return [0, 1, 1, 2][n]

        s = [1, 2, 2]          # initial magical string
        ones = 1               # count of '1's in first n characters (the first element)
        i = 2                  # pointer to the element that tells how many times to repeat
        cur = 1                # next number to append

        while len(s) < n:
            repeat = s[i]
            for _ in range(repeat):
                s.append(cur)
                if cur == 1 and len(s) <= n:
                    ones += 1
            cur ^= 3           # toggle between 1 and 2 (1^3=2, 2^3=1)
            i += 1

        return ones
```

## C

```c
#include <stdlib.h>

int magicalString(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;

    int *s = (int *)malloc((n + 3) * sizeof(int));
    s[0] = 1;
    s[1] = 2;
    s[2] = 2;

    int countOnes = 1;          // first element is '1'
    int head = 2;               // reading position
    int tail = 3;               // next write position

    while (tail < n) {
        int cnt = s[head];
        int last = s[tail - 1];
        int nextVal = (last == 1) ? 2 : 1;

        for (int i = 0; i < cnt && tail < n; ++i) {
            s[tail++] = nextVal;
            if (nextVal == 1) ++countOnes;
        }
        ++head;
    }

    free(s);
    return countOnes;
}
```

## Csharp

```csharp
public class Solution {
    public int MagicalString(int n) {
        if (n == 0) return 0;
        if (n <= 3) {
            int[] baseArr = { 1, 2, 2 };
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                if (baseArr[i] == 1) cnt++;
            }
            return cnt;
        }

        int[] s = new int[n + 2];
        s[0] = 1;
        s[1] = 2;
        s[2] = 2;

        int head = 2;   // points to the element that tells how many times to repeat
        int num = 1;    // next number to append
        int tail = 3;   // next position to fill

        while (tail < n) {
            int count = s[head];
            for (int i = 0; i < count && tail < n; i++) {
                s[tail++] = num;
            }
            num = 3 - num; // toggle between 1 and 2
            head++;
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == 1) ans++;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var magicalString = function(n) {
    if (n <= 0) return 0;
    // The initial magical string "122"
    const s = [1, 2, 2];
    let head = 2;          // points to the element that tells how many times to repeat
    let cur = 1;           // next number to append (alternates between 1 and 2)
    let onesCount = 1;     // s[0] is 1

    while (s.length < n) {
        const cnt = s[head];
        for (let i = 0; i < cnt && s.length < n; i++) {
            s.push(cur);
            if (cur === 1) onesCount++;
        }
        cur = cur === 1 ? 2 : 1;
        head++;
    }

    return onesCount;
};
```

## Typescript

```typescript
function magicalString(n: number): number {
    if (n <= 0) return 0;
    if (n <= 3) return 1; // "122" has only one '1' in first three positions

    const s: number[] = [1, 2, 2];
    let readIdx = 2;          // index that tells how many times to repeat
    let nextVal = 1;          // value to be appended next
    let onesCount = 1;        // first element is '1'

    while (s.length < n) {
        const repeat = s[readIdx];
        for (let i = 0; i < repeat && s.length < n; i++) {
            s.push(nextVal);
            if (nextVal === 1) onesCount++;
        }
        nextVal = nextVal === 1 ? 2 : 1;
        readIdx++;
    }

    return onesCount;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function magicalString($n) {
        if ($n <= 0) return 0;
        if ($n <= 3) return 1;

        $s = [1, 2, 2];
        $head = 2; // read pointer
        $tail = 3; // next write position (size of array)
        $countOnes = 1; // first element is '1'

        while ($tail < $n) {
            $repeat = $s[$head];
            $nextVal = $s[$tail - 1] == 1 ? 2 : 1;
            for ($i = 0; $i < $repeat && $tail < $n; $i++) {
                $s[] = $nextVal;
                if ($nextVal == 1) {
                    $countOnes++;
                }
                $tail++;
            }
            $head++;
        }

        return $countOnes;
    }
}
```

## Swift

```swift
class Solution {
    func magicalString(_ n: Int) -> Int {
        if n <= 0 { return 0 }
        if n == 1 { return 1 }
        
        var s = [Int]()
        s.reserveCapacity(n + 2)
        s.append(1)
        s.append(2)
        s.append(2)
        
        var countOnes = 1
        var i = 2               // index that tells how many times to repeat next value
        var nextVal = 1         // the value to be appended next
        
        while s.count < n {
            let repeatTimes = s[i]
            for _ in 0..<repeatTimes {
                if s.count >= n { break }
                s.append(nextVal)
                if nextVal == 1 {
                    countOnes += 1
                }
            }
            nextVal = (nextVal == 1) ? 2 : 1
            i += 1
        }
        
        return countOnes
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun magicalString(n: Int): Int {
        if (n == 0) return 0
        if (n <= 3) return 1  // "122" contains exactly one '1' in first up to 3 chars

        val arr = IntArray(n + 2)
        arr[0] = 1
        arr[1] = 2
        arr[2] = 2
        var size = 3          // current length of the magical string built
        var head = 2          // index to read the count from
        var next = 1          // next number to append
        var onesCount = 1     // first element is '1'

        while (size < n) {
            val cnt = arr[head]
            for (i in 0 until cnt) {
                if (size >= n) break
                arr[size] = next
                if (next == 1) onesCount++
                size++
            }
            next = if (next == 1) 2 else 1
            head++
        }
        return onesCount
    }
}
```

## Dart

```dart
class Solution {
  int magicalString(int n) {
    if (n <= 0) return 0;
    List<int> s = [1, 2, 2];
    int head = 2; // points to the element that tells how many times to repeat next number
    int num = 1; // next number to append (either 1 or 2)
    while (s.length < n) {
      int cnt = s[head];
      for (int i = 0; i < cnt && s.length < n; ++i) {
        s.add(num);
      }
      num = 3 - num; // toggle between 1 and 2
      head++;
    }
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      if (s[i] == 1) ans++;
    }
    return ans;
  }
}
```

## Golang

```go
func magicalString(n int) int {
	if n == 0 {
		return 0
	}
	s := []int{1, 2, 2}
	if n <= 3 {
		cnt := 0
		for i := 0; i < n; i++ {
			if s[i] == 1 {
				cnt++
			}
		}
		return cnt
	}
	countOnes := 1 // first element is 1
	i, cur := 2, 1
	for len(s) < n {
		repeat := s[i]
		for j := 0; j < repeat && len(s) < n; j++ {
			s = append(s, cur)
			if cur == 1 {
				countOnes++
			}
		}
		cur = 3 - cur
		i++
	}
	return countOnes
}
```

## Ruby

```ruby
def magical_string(n)
  return 0 if n == 0
  s = [1, 2, 2]
  ones = 1
  head = 2
  num = 1
  while s.length < n
    cnt = s[head]
    cnt.times do
      break if s.length >= n
      s << num
      ones += 1 if num == 1
    end
    num = 3 - num
    head += 1
  end
  ones
end
```

## Scala

```scala
object Solution {
    def magicalString(n: Int): Int = {
        if (n <= 0) return 0
        val s = new Array[Int](n + 3)
        s(0) = 1
        s(1) = 2
        s(2) = 2

        var countOnes = 1 // first element is '1'
        var i = 2          // read pointer
        var j = 3          // write pointer
        var cur = 1        // next number to write (alternates between 1 and 2)

        while (j < n) {
            val repeat = s(i)
            var k = 0
            while (k < repeat && j < n) {
                s(j) = cur
                if (cur == 1) countOnes += 1
                j += 1
                k += 1
            }
            cur = 3 - cur // toggle between 1 and 2
            i += 1
        }

        countOnes
    }
}
```

## Rust

```rust
impl Solution {
    pub fn magical_string(n: i32) -> i32 {
        let n = n as usize;
        if n == 0 {
            return 0;
        }
        // Initial magical string: "122"
        let mut s: Vec<u8> = vec![1, 2, 2];
        let mut head: usize = 2; // position to read the count
        let mut cur: u8 = 1;     // next number to append

        while s.len() < n {
            let repeat = s[head] as usize;
            for _ in 0..repeat {
                if s.len() == n {
                    break;
                }
                s.push(cur);
            }
            cur = if cur == 1 { 2 } else { 1 };
            head += 1;
        }

        let mut count = 0;
        for i in 0..n {
            if s[i] == 1 {
                count += 1;
            }
        }
        count as i32
    }
}
```

## Racket

```racket
(define/contract (magical-string n)
  (-> exact-integer? exact-integer?)
  (if (= n 0)
      0
      (let* ((vec (make-vector (+ n 5) 0))
             (size 3)
             (i 2)
             (countOnes (if (> n 0) 1 0))) ; first element is '1'
        (vector-set! vec 0 1)
        (vector-set! vec 1 2)
        (vector-set! vec 2 2)
        (let loop ()
          (when (< size n)
            (let* ((val (vector-ref vec i))
                   (last (vector-ref vec (- size 1)))
                   (nextDigit (if (= last 1) 2 1)))
              (let inner ((k 0))
                (when (and (< k val) (< size n))
                  (vector-set! vec size nextDigit)
                  (when (= nextDigit 1)
                    (set! countOnes (+ countOnes 1)))
                  (set! size (+ size 1))
                  (inner (+ k 1))))
              (set! i (+ i 1))
              (loop))))
        countOnes)))
```

## Erlang

```erlang
-module(solution).
-export([magical_string/1]).

-spec magical_string(N :: integer()) -> integer().
magical_string(N) when N =< 0 ->
    0;
magical_string(N) when N =< 3 ->
    case N of
        0 -> 0;
        _ -> 1
    end;
magical_string(N) ->
    Seq0 = array:new(0, [{default,0}]),
    Seq1 = array:set(1, 1, Seq0),
    Seq2 = array:set(2, 2, Seq1),
    Seq3 = array:set(3, 2, Seq2),
    generate(Seq3, 3, 3, 1, 1, N).

generate(_Seq, Len, _I, _NextNum, OnesCount, N) when Len >= N ->
    OnesCount;
generate(Seq, Len, I, NextNum, OnesCount, N) ->
    Count = array:get(I, Seq),
    {Seq1, Len1, NextNum1, OnesCount1} = add_counts(Count, Seq, Len, NextNum, OnesCount, N),
    generate(Seq1, Len1, I + 1, NextNum1, OnesCount1, N).

add_counts(0, Seq, Len, NextNum, OnesCount, _N) ->
    {Seq, Len, NextNum, OnesCount};
add_counts(C, Seq, Len, NextNum, OnesCount, N) when C > 0 ->
    NewLen = Len + 1,
    Seq2 = array:set(NewLen, NextNum, Seq),
    NewOnes = case NextNum of
        1 -> if NewLen =< N -> OnesCount + 1; true -> OnesCount end;
        _ -> OnesCount
    end,
    NewNext = case NextNum of
        1 -> 2;
        2 -> 1
    end,
    add_counts(C - 1, Seq2, NewLen, NewNext, NewOnes, N).
```

## Elixir

```elixir
defmodule Solution do
  @spec magical_string(integer) :: integer
  def magical_string(n) when n <= 0, do: 0

  def magical_string(n) do
    cond do
      n == 1 -> 1
      n == 2 -> 1
      n == 3 -> 1
      true ->
        arr = :array.from_list([1, 2, 2])
        build(arr, 3, 1, 2, 1, n)
    end
  end

  defp build(_arr, len, ones, _i, _next_num, n) when len >= n, do: ones

  defp build(arr, len, ones, i, next_num, n) do
    count = :array.get(i, arr)
    {arr2, len2, ones2} = add(arr, len, ones, next_num, count, n)
    build(arr2, len2, ones2, i + 1, 3 - next_num, n)
  end

  defp add(arr, len, ones, _num, _cnt, n) when len >= n, do: {arr, len, ones}
  defp add(arr, len, ones, _num, 0, _n), do: {arr, len, ones}

  defp add(arr, len, ones, num, cnt, n) do
    arr = :array.set(len, num, arr)
    ones = if num == 1, do: ones + 1, else: ones
    add(arr, len + 1, ones, num, cnt - 1, n)
  end
end
```
