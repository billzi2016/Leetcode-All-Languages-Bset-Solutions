# 1638. Count Substrings That Differ by One Character

## Cpp

```cpp
class Solution {
public:
    int countSubstrings(string s, string t) {
        int n = s.size(), m = t.size();
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                int diff = 0;
                for (int k = 0; i + k < n && j + k < m; ++k) {
                    if (s[i + k] != t[j + k]) ++diff;
                    if (diff == 1) ++ans;
                    else if (diff > 1) break;
                }
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int countSubstrings(String s, String t) {
        int n = s.length();
        int m = t.length();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int diff = 0;
                for (int k = 0; i + k < n && j + k < m; k++) {
                    if (s.charAt(i + k) != t.charAt(j + k)) {
                        diff++;
                    }
                    if (diff == 1) {
                        ans++;
                    } else if (diff > 1) {
                        break;
                    }
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n, m = len(s), len(t)
        ans = 0
        for i in range(n):
            for j in range(m):
                diff = 0
                k = 0
                while i + k < n and j + k < m:
                    if s[i + k] != t[j + k]:
                        diff += 1
                    if diff == 1:
                        ans += 1
                    elif diff > 1:
                        break
                    k += 1
        return ans
```

## Python3

```python
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        ans = 0
        for i in range(n):
            for j in range(m):
                diff = 0
                k = 0
                while i + k < n and j + k < m:
                    if s[i + k] != t[j + k]:
                        diff += 1
                    if diff == 1:
                        ans += 1
                    elif diff > 1:
                        break
                    k += 1
        return ans
```

## C

```c
#include <string.h>

int countSubstrings(char* s, char* t) {
    int n = strlen(s);
    int m = strlen(t);
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            int diff = 0;
            for (int k = 0; i + k < n && j + k < m; ++k) {
                if (s[i + k] != t[j + k]) {
                    ++diff;
                }
                if (diff == 1) {
                    ++ans;
                } else if (diff > 1) {
                    break;
                }
            }
        }
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int CountSubstrings(string s, string t) {
        int n = s.Length, m = t.Length;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int diff = 0;
                for (int k = 0; i + k < n && j + k < m; k++) {
                    if (s[i + k] != t[j + k]) diff++;
                    if (diff == 1) ans++;
                    else if (diff > 1) break;
                }
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var countSubstrings = function(s, t) {
    let ans = 0;
    const n = s.length, m = t.length;
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < m; ++j) {
            let diff = 0;
            for (let k = 0; i + k < n && j + k < m; ++k) {
                if (s[i + k] !== t[j + k]) diff++;
                if (diff === 1) {
                    ans++;
                } else if (diff > 1) {
                    break;
                }
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function countSubstrings(s: string, t: string): number {
    let ans = 0;
    const n = s.length, m = t.length;
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < m; ++j) {
            let diff = 0;
            for (let k = 0; i + k < n && j + k < m; ++k) {
                if (s[i + k] !== t[j + k]) diff++;
                if (diff === 1) ans++;
                else if (diff > 1) break;
            }
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function countSubstrings($s, $t) {
        $n = strlen($s);
        $m = strlen($t);
        $ans = 0;
        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $m; ++$j) {
                $diff = 0;
                $k = 0;
                while ($i + $k < $n && $j + $k < $m) {
                    if ($s[$i + $k] !== $t[$j + $k]) {
                        $diff++;
                    }
                    if ($diff == 1) {
                        $ans++;
                    } elseif ($diff > 1) {
                        break;
                    }
                    ++$k;
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countSubstrings(_ s: String, _ t: String) -> Int {
        let sArr = Array(s)
        let tArr = Array(t)
        var result = 0
        for i in 0..<sArr.count {
            for j in 0..<tArr.count {
                var diff = 0
                var k = 0
                while i + k < sArr.count && j + k < tArr.count {
                    if sArr[i + k] != tArr[j + k] {
                        diff += 1
                    }
                    if diff == 1 {
                        result += 1
                    } else if diff > 1 {
                        break
                    }
                    k += 1
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countSubstrings(s: String, t: String): Int {
        val n = s.length
        val m = t.length
        var ans = 0
        for (i in 0 until n) {
            for (j in 0 until m) {
                var diff = 0
                var k = 0
                while (i + k < n && j + k < m) {
                    if (s[i + k] != t[j + k]) diff++
                    if (diff == 1) {
                        ans++
                    } else if (diff > 1) {
                        break
                    }
                    k++
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countSubstrings(String s, String t) {
    int n = s.length;
    int m = t.length;
    int ans = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        int diff = 0;
        for (int k = 0; i + k < n && j + k < m; k++) {
          if (s.codeUnitAt(i + k) != t.codeUnitAt(j + k)) diff++;
          if (diff == 1) {
            ans++;
          } else if (diff > 1) {
            break;
          }
        }
      }
    }
    return ans;
  }
}
```

## Golang

```go
func countSubstrings(s string, t string) int {
	n, m := len(s), len(t)
	ans := 0
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			diff := 0
			for k := 0; i+k < n && j+k < m; k++ {
				if s[i+k] != t[j+k] {
					diff++
				}
				if diff == 1 {
					ans++
				} else if diff > 1 {
					break
				}
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def count_substrings(s, t)
  n = s.length
  m = t.length
  ans = 0
  (0...n).each do |i|
    (0...m).each do |j|
      diff = 0
      k = 0
      while i + k < n && j + k < m
        diff += 1 if s.getbyte(i + k) != t.getbyte(j + k)
        break if diff > 1
        ans += 1 if diff == 1
        k += 1
      end
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def countSubstrings(s: String, t: String): Int = {
        val n = s.length
        val m = t.length
        var ans = 0
        for (i <- 0 until n) {
            for (j <- 0 until m) {
                var diff = 0
                var k = 0
                while (i + k < n && j + k < m && diff <= 1) {
                    if (s.charAt(i + k) != t.charAt(j + k)) diff += 1
                    if (diff == 1) ans += 1
                    k += 1
                }
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_substrings(s: String, t: String) -> i32 {
        let s_bytes = s.as_bytes();
        let t_bytes = t.as_bytes();
        let n = s_bytes.len();
        let m = t_bytes.len();

        // left[i][j] = length of common suffix ending at s[i-1], t[j-1]
        let mut left = vec![vec![0usize; m + 1]; n + 1];
        for i in 1..=n {
            for j in 1..=m {
                if s_bytes[i - 1] == t_bytes[j - 1] {
                    left[i][j] = left[i - 1][j - 1] + 1;
                }
            }
        }

        // right[i][j] = length of common prefix starting at s[i], t[j]
        let mut right = vec![vec![0usize; m + 2]; n + 2];
        for i in (0..n).rev() {
            for j in (0..m).rev() {
                if s_bytes[i] == t_bytes[j] {
                    right[i][j] = right[i + 1][j + 1] + 1;
                }
            }
        }

        let mut ans: i64 = 0;
        for i in 0..n {
            for j in 0..m {
                if s_bytes[i] != t_bytes[j] {
                    let left_len = left[i][j];
                    let right_len = right[i + 1][j + 1];
                    ans += (left_len as i64 + 1) * (right_len as i64 + 1);
                }
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (count-substrings s t)
  (-> string? string? exact-integer?)
  (let* ((n (string-length s))
         (m (string-length t)))
    (let outer-i ((i 0) (ans 0))
      (if (= i n)
          ans
          (let outer-j ((j 0) (ans2 ans))
            (if (= j m)
                (outer-i (+ i 1) ans2)
                (let inner ((k 0) (mismatch 0) (ans3 ans2))
                  (cond
                    [(or (>= (+ i k) n) (>= (+ j k) m))
                     (outer-j (+ j 1) ans3)]
                    [else
                     (define ch-s (string-ref s (+ i k)))
                     (define ch-t (string-ref t (+ j k)))
                     (define new-mismatch (if (char=? ch-s ch-t) mismatch (+ mismatch 1)))
                     (cond
                       [(> new-mismatch 1)
                        (outer-j (+ j 1) ans3)]
                       [else
                        (define inc (if (= new-mismatch 1) 1 0))
                        (inner (+ k 1) new-mismatch (+ ans3 inc))])])))))))))
```

## Erlang

```erlang
-spec count_substrings(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
count_substrings(S, T) ->
    SList = binary_to_list(S),
    TList = binary_to_list(T),
    STuple = list_to_tuple(SList),
    TTuple = list_to_tuple(TList),
    Ns = tuple_size(STuple),
    Nt = tuple_size(TTuple),
    loop_i(0, Ns, STuple, TTuple, Nt, 0).

loop_i(I, Ns, _ST, _TT, _Nt, Acc) when I >= Ns ->
    Acc;
loop_i(I, Ns, ST, TT, Nt, Acc) ->
    NewAcc = loop_j(0, Nt, I, ST, TT, Acc),
    loop_i(I + 1, Ns, ST, TT, Nt, NewAcc).

loop_j(J, Nt, _I, _ST, _TT, Acc) when J >= Nt ->
    Acc;
loop_j(J, Nt, I, ST, TT, Acc) ->
    CharS = element(I + 1, ST),
    CharT = element(J + 1, TT),
    NewAcc =
        if CharS =/= CharT ->
                L = left_match(I - 1, J - 1, ST, TT, 0),
                R = right_match(I + 1, J + 1, ST, TT, tuple_size(ST), tuple_size(TT), 0),
                Acc + (L + 1) * (R + 1);
           true ->
                Acc
        end,
    loop_j(J + 1, Nt, I, ST, TT, NewAcc).

left_match(I, J, _ST, _TT, Acc) when I < 0; J < 0 ->
    Acc;
left_match(I, J, ST, TT, Acc) ->
    case element(I + 1, ST) =:= element(J + 1, TT) of
        true -> left_match(I - 1, J - 1, ST, TT, Acc + 1);
        false -> Acc
    end.

right_match(I, _J, _ST, _TT, Ns, _Nt, Acc) when I >= Ns ->
    Acc;
right_match(_I, J, _ST, _TT, _Ns, Nt, Acc) when J >= Nt ->
    Acc;
right_match(I, J, ST, TT, Ns, Nt, Acc) ->
    case element(I + 1, ST) =:= element(J + 1, TT) of
        true -> right_match(I + 1, J + 1, ST, TT, Ns, Nt, Acc + 1);
        false -> Acc
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_substrings(s :: String.t(), t :: String.t()) :: integer()
  def count_substrings(s, t) do
    s_tuple = :binary.bin_to_list(s) |> List.to_tuple()
    t_tuple = :binary.bin_to_list(t) |> List.to_tuple()
    len_s = tuple_size(s_tuple)
    len_t = tuple_size(t_tuple)

    0..len_s - 1
    |> Enum.reduce(0, fn i, acc_i ->
      0..len_t - 1
      |> Enum.reduce(acc_i, fn j, acc_j ->
        acc_j + count_pairs(i, j, s_tuple, t_tuple, len_s, len_t)
      end)
    end)
  end

  defp count_pairs(i, j, s_tuple, t_tuple, len_s, len_t) do
    max_len = min(len_s - i, len_t - j)
    do_count(0, max_len, i, j, s_tuple, t_tuple, 0, 0)
  end

  defp do_count(k, max_len, i, j, s_tuple, t_tuple, mismatches, acc) when k < max_len do
    mis =
      if elem(s_tuple, i + k) != elem(t_tuple, j + k),
        do: mismatches + 1,
        else: mismatches

    cond do
      mis == 1 ->
        do_count(k + 1, max_len, i, j, s_tuple, t_tuple, mis, acc + 1)

      mis > 1 ->
        acc

      true ->
        do_count(k + 1, max_len, i, j, s_tuple, t_tuple, mis, acc)
    end
  end

  defp do_count(_k, _max_len, _i, _j, _s_tuple, _t_tuple, _mismatches, acc), do: acc
end
```
