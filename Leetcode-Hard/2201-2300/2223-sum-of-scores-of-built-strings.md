# 2223. Sum of Scores of Built Strings

## Cpp

```cpp
class Solution {
public:
    long long sumScores(string s) {
        int n = s.size();
        vector<int> z(n);
        z[0] = n;
        int l = 0, r = 0;
        for (int i = 1; i < n; ++i) {
            if (i <= r) z[i] = min(r - i + 1, z[i - l]);
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        long long ans = 0;
        for (int v : z) ans += v;
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long sumScores(String s) {
        int n = s.length();
        char[] ch = s.toCharArray();
        int[] z = new int[n];
        int l = 0, r = 0;
        for (int i = 1; i < n; i++) {
            if (i <= r) {
                z[i] = Math.min(r - i + 1, z[i - l]);
            }
            while (i + z[i] < n && ch[z[i]] == ch[i + z[i]]) {
                z[i]++;
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        long sum = n; // Z[0] equals the whole length
        for (int i = 1; i < n; i++) {
            sum += z[i];
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def sumScores(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        z = [0] * n
        l = r = 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return n + sum(z)
```

## Python3

```python
class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        z = [0] * n
        l = r = 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return n + sum(z)
```

## C

```c
#include <string.h>
#include <stdlib.h>

long long sumScores(char* s) {
    int n = strlen(s);
    if (n == 0) return 0;
    int *z = (int *)malloc(n * sizeof(int));
    z[0] = n;
    int l = 0, r = 0;
    for (int i = 1; i < n; ++i) {
        if (i <= r)
            z[i] = (r - i + 1 < z[i - l]) ? (r - i + 1) : z[i - l];
        else
            z[i] = 0;
        while (i + z[i] < n && s[z[i]] == s[i + z[i]])
            ++z[i];
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    long long ans = 0;
    for (int i = 0; i < n; ++i)
        ans += z[i];
    free(z);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public long SumScores(string s)
    {
        int n = s.Length;
        long total = n; // score of the whole string

        int[] z = new int[n];
        int l = 0, r = 0;

        for (int i = 1; i < n; i++)
        {
            if (i <= r)
                z[i] = Math.Min(r - i + 1, z[i - l]);

            while (i + z[i] < n && s[z[i]] == s[i + z[i]])
                z[i]++;

            if (i + z[i] - 1 > r)
            {
                l = i;
                r = i + z[i] - 1;
            }

            total += z[i];
        }

        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var sumScores = function(s) {
    const n = s.length;
    if (n === 0) return 0;
    const z = new Array(n).fill(0);
    let l = 0, r = 0;
    for (let i = 1; i < n; i++) {
        if (i <= r) {
            z[i] = Math.min(r - i + 1, z[i - l]);
        }
        while (i + z[i] < n && s.charAt(z[i]) === s.charAt(i + z[i])) {
            z[i]++;
        }
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    let sum = n; // Z[0] equals the length of the whole string
    for (let i = 1; i < n; i++) {
        sum += z[i];
    }
    return sum;
};
```

## Typescript

```typescript
function sumScores(s: string): number {
    const n = s.length;
    if (n === 0) return 0;
    const z = new Array<number>(n);
    let l = 0, r = 0;
    for (let i = 1; i < n; i++) {
        if (i <= r) {
            z[i] = Math.min(r - i + 1, z[i - l]);
        } else {
            z[i] = 0;
        }
        while (i + z[i] < n && s[z[i]] === s[i + z[i]]) {
            z[i]++;
        }
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    let sum = n; // score for the whole string
    for (let i = 1; i < n; i++) {
        sum += z[i];
    }
    return sum;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function sumScores($s) {
        $n = strlen($s);
        if ($n == 0) return 0;
        $z = array_fill(0, $n, 0);
        $l = 0;
        $r = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($i <= $r) {
                $z[$i] = min($r - $i + 1, $z[$i - $l]);
            }
            while ($i + $z[$i] < $n && $s[$z[$i]] === $s[$i + $z[$i]]) {
                $z[$i]++;
            }
            if ($i + $z[$i] - 1 > $r) {
                $l = $i;
                $r = $i + $z[$i] - 1;
            }
        }
        $sum = $n; // score for the whole string
        for ($i = 1; $i < $n; $i++) {
            $sum += $z[$i];
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func sumScores(_ s: String) -> Int {
        let chars = Array(s.utf8)
        let n = chars.count
        var z = [Int](repeating: 0, count: n)
        if n == 0 { return 0 }
        z[0] = n
        var l = 0
        var r = 0
        for i in 1..<n {
            if i <= r {
                z[i] = min(r - i + 1, z[i - l])
            }
            while i + z[i] < n && chars[z[i]] == chars[i + z[i]] {
                z[i] += 1
            }
            if i + z[i] - 1 > r {
                l = i
                r = i + z[i] - 1
            }
        }
        var total = 0
        for value in z {
            total += value
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumScores(s: String): Long {
        val n = s.length
        val z = IntArray(n)
        var l = 0
        var r = 0
        for (i in 1 until n) {
            if (i <= r) {
                z[i] = kotlin.math.min(r - i + 1, z[i - l])
            }
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
                z[i]++
            }
            if (i + z[i] - 1 > r) {
                l = i
                r = i + z[i] - 1
            }
        }
        var sum: Long = n.toLong()
        for (i in 1 until n) {
            sum += z[i].toLong()
        }
        return sum
    }
}
```

## Dart

```dart
class Solution {
  int sumScores(String s) {
    int n = s.length;
    List<int> z = List.filled(n, 0);
    int l = 0, r = 0;
    for (int i = 1; i < n; i++) {
      if (i <= r) {
        int k = i - l;
        int bound = r - i + 1;
        z[i] = z[k] < bound ? z[k] : bound;
      }
      while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
        z[i]++;
      }
      if (i + z[i] - 1 > r) {
        l = i;
        r = i + z[i] - 1;
      }
    }
    int sum = n; // score for the whole string
    for (int i = 1; i < n; i++) {
      sum += z[i];
    }
    return sum;
  }
}
```

## Golang

```go
func sumScores(s string) int64 {
	n := len(s)
	if n == 0 {
		return 0
	}
	z := make([]int, n)
	z[0] = n
	l, r := 0, 0
	for i := 1; i < n; i++ {
		if i <= r {
			if z[i-l] < r-i+1 {
				z[i] = z[i-l]
			} else {
				z[i] = r - i + 1
			}
		}
		for i+z[i] < n && s[z[i]] == s[i+z[i]] {
			z[i]++
		}
		if i+z[i]-1 > r {
			l = i
			r = i + z[i] - 1
		}
	}
	var ans int64
	for _, v := range z {
		ans += int64(v)
	}
	return ans
}
```

## Ruby

```ruby
def sum_scores(s)
  n = s.length
  return 0 if n == 0
  z = Array.new(n, 0)
  l = 0
  r = 0
  (1...n).each do |i|
    if i <= r
      z[i] = [r - i + 1, z[i - l]].min
    end
    while i + z[i] < n && s.getbyte(z[i]) == s.getbyte(i + z[i])
      z[i] += 1
    end
    if i + z[i] - 1 > r
      l = i
      r = i + z[i] - 1
    end
  end
  total = n + z.sum
  total
end
```

## Scala

```scala
object Solution {
    def sumScores(s: String): Long = {
        val n = s.length
        if (n == 0) return 0L
        val z = new Array[Int](n)
        var l = 0
        var r = 0
        for (i <- 1 until n) {
            if (i <= r) {
                z(i) = math.min(r - i + 1, z(i - l))
            }
            while (i + z(i) < n && s(z(i)) == s(i + z(i))) {
                z(i) += 1
            }
            if (i + z(i) - 1 > r) {
                l = i
                r = i + z(i) - 1
            }
        }
        var total: Long = n.toLong // score for the whole string
        var idx = 1
        while (idx < n) {
            total += z(idx).toLong
            idx += 1
        }
        total
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn sum_scores(s: String) -> i64 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return 0;
        }
        let mut z = vec![0usize; n];
        z[0] = n;
        let mut l = 0usize;
        let mut r = 0usize;
        for i in 1..n {
            if i <= r {
                let k = i - l;
                z[i] = std::cmp::min(r - i + 1, z[k]);
            }
            while i + z[i] < n && bytes[z[i]] == bytes[i + z[i]] {
                z[i] += 1;
            }
            if i + z[i] - 1 > r {
                l = i;
                r = i + z[i] - 1;
            }
        }
        z.iter().map(|&v| v as i64).sum()
    }
}
```

## Racket

```racket
(define/contract (sum-scores s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (z (make-vector n 0)))
    (let loop ((i 1) (l 0) (r 0) (total n)) ; total includes Z[0] = n
      (if (= i n)
          total
          (let* ((z_i (if (<= i r)
                          (min (- r i + 1) (vector-ref z (- i l)))
                          0))
                 (z_val (let rec ((k z_i))
                          (if (and (< (+ i k) n)
                                   (char=? (string-ref s k)
                                           (string-ref s (+ i k))))
                              (rec (+ k 1))
                              k))))
            (vector-set! z i z_val)
            (define-values (new-l new-r)
              (if (> (+ i z_val -1) r)
                  (values i (+ i z_val -1))
                  (values l r)))
            (loop (+ i 1) new-l new-r (+ total z_val)))))))
```

## Erlang

```erlang
-export([sum_scores/1]).

-spec sum_scores(S :: unicode:unicode_binary()) -> integer().
sum_scores(S) ->
    N = byte_size(S),
    Z0 = array:new(N, {default, 0}),
    ZArr = array:set(0, N, Z0),
    loop(1, 0, 0, N, S, N, ZArr).

loop(I, _L, _R, Sum, _S, N, _ZArr) when I >= N ->
    Sum;
loop(I, L, R, Sum, S, N, ZArr) ->
    ZI =
        if
            I > R ->
                match_len(S, N, I, 0);
            true ->
                K = I - L,
                ZK = array:get(K, ZArr),
                Rem = R - I + 1,
                if
                    ZK < Rem ->
                        ZK;
                    true ->
                        Extra = match_len(S, N, R + 1, Rem),
                        Rem + Extra
                end
        end,
    NewSum = Sum + ZI,
    {NewL, NewR} =
        case I + ZI - 1 > R of
            true -> {I, I + ZI - 1};
            false -> {L, R}
        end,
    ZArr2 = array:set(I, ZI, ZArr),
    loop(I + 1, NewL, NewR, NewSum, S, N, ZArr2).

match_len(S, N, Pos, Len) ->
    if
        Pos + Len >= N ->
            Len;
        binary:at(S, Len) =:= binary:at(S, Pos + Len) ->
            match_len(S, N, Pos, Len + 1);
        true ->
            Len
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_scores(String.t()) :: integer()
  def sum_scores(s) do
    bytes = :binary.bin_to_list(s)
    n = length(bytes)

    arr = :array.from_list(bytes, default: 0)
    z_arr = :array.new(n, default: 0)

    {z_final, _l, _r} =
      Enum.reduce(1..(n - 1), {z_arr, 0, 0}, fn i, {z_acc, l, r} ->
        zi =
          if i <= r do
            prev = :array.get(z_acc, i - l)
            min(r - i + 1, prev)
          else
            0
          end

        zi = extend(zi, i, arr, n)

        {z_new, l_new, r_new} =
          if i + zi - 1 > r do
            {z_acc, i, i + zi - 1}
          else
            {z_acc, l, r}
          end

        z_updated = :array.set(z_new, i, zi)
        {z_updated, l_new, r_new}
      end)

    total =
      Enum.reduce(0..(n - 1), 0, fn idx, acc ->
        val = if idx == 0, do: n, else: :array.get(z_final, idx)
        acc + val
      end)

    total
  end

  defp extend(k, i, arr, n) do
    if i + k < n and :array.get(arr, k) == :array.get(arr, i + k) do
      extend(k + 1, i, arr, n)
    else
      k
    end
  end
end
```
