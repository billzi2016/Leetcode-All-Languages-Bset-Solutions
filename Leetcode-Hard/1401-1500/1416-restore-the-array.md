# 1416. Restore The Array

## Cpp

```cpp
class Solution {
public:
    int numberOfArrays(string s, int k) {
        const int MOD = 1000000007;
        int n = s.size();
        vector<int> dp(n + 1, 0);
        dp[n] = 1;
        int maxLen = 0;
        long long tmp = k;
        while (tmp > 0) {
            ++maxLen;
            tmp /= 10;
        }
        for (int i = n - 1; i >= 0; --i) {
            if (s[i] == '0') {
                dp[i] = 0;
                continue;
            }
            long long num = 0;
            for (int j = i; j < n && j - i + 1 <= maxLen; ++j) {
                num = num * 10 + (s[j] - '0');
                if (num > k) break;
                dp[i] += dp[j + 1];
                if (dp[i] >= MOD) dp[i] -= MOD;
            }
        }
        return dp[0];
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int numberOfArrays(String s, int k) {
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[n] = 1;
        int maxLen = Integer.toString(k).length();
        for (int i = n - 1; i >= 0; --i) {
            if (s.charAt(i) == '0') continue;
            long cur = 0;
            for (int j = i; j < n && j < i + maxLen; ++j) {
                cur = cur * 10 + (s.charAt(j) - '0');
                if (cur > k) break;
                dp[i] += dp[j + 1];
                if (dp[i] >= MOD) dp[i] -= MOD;
            }
        }
        return dp[0];
    }
}
```

## Python

```python
class Solution(object):
    def numberOfArrays(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        max_len = len(str(k))
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                continue
            val = 0
            limit = min(n, i + max_len)
            for j in range(i, limit):
                val = val * 10 + (ord(s[j]) - 48)
                if val > k:
                    break
                dp[i] = (dp[i] + dp[j + 1]) % MOD
        return dp[0]
```

## Python3

```python
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        max_len = len(str(k))
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                continue
            num = 0
            limit = min(n, i + max_len)
            for j in range(i, limit):
                num = num * 10 + (ord(s[j]) - 48)
                if num > k:
                    break
                dp[i] = (dp[i] + dp[j + 1]) % MOD
        return dp[0]
```

## C

```c
#include <string.h>
#include <stdlib.h>

int numberOfArrays(char* s, int k) {
    const int MOD = 1000000007;
    int n = strlen(s);
    
    // maximum possible length of a valid number (digits in k)
    int maxLen = 0;
    for (int tmp = k; tmp > 0; tmp /= 10) ++maxLen;
    
    long long *dp = (long long *)malloc((n + 1) * sizeof(long long));
    dp[n] = 1;
    
    for (int i = n - 1; i >= 0; --i) {
        if (s[i] == '0') {          // numbers cannot have leading zeros
            dp[i] = 0;
            continue;
        }
        long long val = 0;
        long long ways = 0;
        for (int j = i, len = 0; j < n && len < maxLen; ++j, ++len) {
            val = val * 10 + (s[j] - '0');
            if (val > k) break;
            ways += dp[j + 1];
            if (ways >= MOD) ways -= MOD;
        }
        dp[i] = ways;
    }
    
    int result = (int)(dp[0] % MOD);
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1_000_000_007;
    public int NumberOfArrays(string s, int k)
    {
        int n = s.Length;
        int maxLen = k.ToString().Length;
        long[] dp = new long[n + 1];
        dp[n] = 1;

        for (int i = n - 1; i >= 0; --i)
        {
            if (s[i] == '0') continue;

            long cur = 0;
            for (int j = i; j < n && j - i + 1 <= maxLen; ++j)
            {
                cur = cur * 10 + (s[j] - '0');
                if (cur > k) break;
                dp[i] += dp[j + 1];
                if (dp[i] >= MOD) dp[i] -= MOD;
            }
        }

        return (int)(dp[0] % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var numberOfArrays = function(s, k) {
    const MOD = 1000000007;
    const n = s.length;
    const maxLen = k.toString().length;
    const dp = new Array(n + 1).fill(0);
    dp[n] = 1;

    for (let i = n - 1; i >= 0; --i) {
        if (s[i] === '0') continue; // numbers cannot have leading zeros
        let num = 0;
        const limit = Math.min(n, i + maxLen);
        for (let j = i; j < limit; ++j) {
            num = num * 10 + (s.charCodeAt(j) - 48);
            if (num > k) break;
            dp[i] = (dp[i] + dp[j + 1]) % MOD;
        }
    }

    return dp[0];
};
```

## Typescript

```typescript
function numberOfArrays(s: string, k: number): number {
    const MOD = 1000000007;
    const n = s.length;
    const maxLen = k.toString().length;
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1;

    for (let i = 0; i < n; i++) {
        if (dp[i] === 0) continue;
        if (s.charAt(i) === '0') continue; // numbers cannot have leading zeros
        let num = 0;
        for (let j = i; j < n && j < i + maxLen; j++) {
            num = num * 10 + (s.charCodeAt(j) - 48);
            if (num > k) break;
            dp[j + 1] = (dp[j + 1] + dp[i]) % MOD;
        }
    }

    return dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function numberOfArrays($s, $k) {
        $mod = 1000000007;
        $n = strlen($s);
        $dp = array_fill(0, $n + 1, 0);
        $dp[$n] = 1; // empty suffix

        $maxLen = strlen((string)$k);

        for ($i = $n - 1; $i >= 0; --$i) {
            if ($s[$i] === '0') {
                continue; // numbers cannot have leading zeros
            }
            $num = 0;
            for ($j = $i; $j < $n && $j - $i + 1 <= $maxLen; ++$j) {
                $digit = ord($s[$j]) - 48;
                $num = $num * 10 + $digit;
                if ($num > $k) {
                    break;
                }
                $dp[$i] = ($dp[$i] + $dp[$j + 1]) % $mod;
            }
        }

        return $dp[0];
    }
}
```

## Swift

```swift
class Solution {
    func numberOfArrays(_ s: String, _ k: Int) -> Int {
        let MOD = 1_000_000_007
        let chars = Array(s.utf8)
        let n = chars.count
        
        // maximum length of a valid number (digits in k)
        var maxLen = 0
        var tempK = k
        repeat {
            maxLen += 1
            tempK /= 10
        } while tempK > 0
        
        var dp = [Int](repeating: 0, count: n + 1)
        dp[n] = 1
        
        for i in stride(from: n - 1, through: 0, by: -1) {
            if chars[i] == 48 { // '0'
                dp[i] = 0
                continue
            }
            var num = 0
            var j = i
            while j < n && (j - i + 1) <= maxLen {
                let digit = Int(chars[j] - 48)
                num = num * 10 + digit
                if num > k { break }
                dp[i] += dp[j + 1]
                if dp[i] >= MOD { dp[i] -= MOD }
                j += 1
            }
        }
        
        return dp[0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfArrays(s: String, k: Int): Int {
        val MOD = 1_000_000_007L
        val n = s.length
        val dp = LongArray(n + 1)
        dp[n] = 1L
        val maxLen = k.toString().length
        for (i in n - 1 downTo 0) {
            if (s[i] == '0') {
                dp[i] = 0L
                continue
            }
            var num = 0L
            var j = i
            while (j < n && j - i + 1 <= maxLen) {
                num = num * 10 + (s[j] - '0')
                if (num > k) break
                dp[i] += dp[j + 1]
                if (dp[i] >= MOD) dp[i] %= MOD
                j++
            }
        }
        return (dp[0] % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numberOfArrays(String s, int k) {
    const int MOD = 1000000007;
    int n = s.length;
    List<int> dp = List.filled(n + 1, 0);
    dp[n] = 1;
    int maxLen = k.toString().length;

    for (int i = n - 1; i >= 0; --i) {
      if (s.codeUnitAt(i) == 48) { // '0'
        dp[i] = 0;
        continue;
      }
      int num = 0;
      for (int j = i; j < n && j - i + 1 <= maxLen; ++j) {
        int digit = s.codeUnitAt(j) - 48;
        num = num * 10 + digit;
        if (num > k) break;
        dp[i] += dp[j + 1];
        if (dp[i] >= MOD) dp[i] -= MOD;
      }
    }

    return dp[0];
  }
}
```

## Golang

```go
func numberOfArrays(s string, k int) int {
	const MOD = 1000000007
	n := len(s)
	dp := make([]int, n+1)
	dp[n] = 1

	// maximum length of a valid number (digits in k)
	maxLen := 0
	tmp := k
	for tmp > 0 {
		maxLen++
		tmp /= 10
	}
	if maxLen == 0 { // when k == 0, though constraints guarantee k >= 1
		maxLen = 1
	}

	for i := n - 1; i >= 0; i-- {
		if s[i] == '0' {
			dp[i] = 0
			continue
		}
		var num int64 = 0
		for j := i; j < n && j-i+1 <= maxLen; j++ {
			num = num*10 + int64(s[j]-'0')
			if num > int64(k) {
				break
			}
			dp[i] += dp[j+1]
			if dp[i] >= MOD {
				dp[i] -= MOD
			}
		}
	}
	return dp[0]
}
```

## Ruby

```ruby
def number_of_arrays(s, k)
  mod = 1_000_000_007
  n = s.length
  dp = Array.new(n + 1, 0)
  dp[n] = 1
  max_len = k.to_s.length

  i = n - 1
  while i >= 0
    if s.getbyte(i) == 48 # '0'
      dp[i] = 0
    else
      val = 0
      j = i
      while j < n && (j - i + 1) <= max_len
        val = val * 10 + (s.getbyte(j) - 48)
        break if val > k
        dp[i] += dp[j + 1]
        dp[i] -= mod if dp[i] >= mod
        j += 1
      end
    end
    i -= 1
  end

  dp[0] % mod
end
```

## Scala

```scala
object Solution {
  private val MOD = 1000000007L

  def numberOfArrays(s: String, k: Int): Int = {
    val n = s.length
    val dp = new Array[Long](n + 1)
    dp(n) = 1L
    val maxDigits = k.toString.length

    var i = n - 1
    while (i >= 0) {
      if (s.charAt(i) == '0') {
        dp(i) = 0L
      } else {
        var num = 0L
        var j = i
        val limit = Math.min(n, i + maxDigits)
        var continueLoop = true
        while (j < limit && continueLoop) {
          num = num * 10 + (s.charAt(j) - '0')
          if (num > k) {
            continueLoop = false
          } else {
            dp(i) = (dp(i) + dp(j + 1)) % MOD
          }
          j += 1
        }
      }
      i -= 1
    }

    (dp(0) % MOD).toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_arrays(s: String, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut dp = vec![0i64; n + 1];
        dp[n] = 1;
        let k_val = k as i64;

        // maximum possible length of a number not exceeding k
        let max_len = {
            let mut len = 0usize;
            let mut tmp = k_val;
            while tmp > 0 {
                len += 1;
                tmp /= 10;
            }
            if len == 0 { 1 } else { len }
        };

        for i in (0..n).rev() {
            if bytes[i] == b'0' {
                dp[i] = 0;
                continue;
            }
            let mut num: i64 = 0;
            for j in i..std::cmp::min(n, i + max_len) {
                num = num * 10 + (bytes[j] - b'0') as i64;
                if num > k_val {
                    break;
                }
                dp[i] += dp[j + 1];
                if dp[i] >= MOD {
                    dp[i] %= MOD;
                }
            }
            dp[i] %= MOD;
        }

        dp[0] as i32
    }
}
```

## Racket

```racket
#lang racket

(define MOD 1000000007)

(define (digit-count x)
  (let loop ((cnt 0) (y x))
    (if (= y 0)
        cnt
        (loop (+ cnt 1) (quotient y 10)))))

(define/contract (number-of-arrays s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length s))
         (lenK (digit-count k))
         (dp (make-vector (+ n 1) 0)))
    (vector-set! dp n 1)
    (let loop-i ((i (- n 1)))
      (when (>= i 0)
        (if (char=? (string-ref s i) #\0)
            (vector-set! dp i 0)
            (let ((max-pos (min n (+ i lenK))))
              (let loop-j ((j i) (num 0) (sum 0))
                (if (= j max-pos)
                    (vector-set! dp i sum)
                    (let* ((digit (- (char->integer (string-ref s j))
                                     (char->integer #\0)))
                           (new-num (+ (* num 10) digit)))
                      (if (> new-num k)
                          (vector-set! dp i sum)
                          (loop-j (+ j 1) new-num
                                  (modulo (+ sum (vector-ref dp (+ j 1))) MOD))))))))
        (loop-i (- i 1))))
    (vector-ref dp 0)))
```

## Erlang

```erlang
-module(solution).
-export([number_of_arrays/2]).

-define(MOD, 1000000007).

-spec number_of_arrays(S :: unicode:unicode_binary(), K :: integer()) -> integer().
number_of_arrays(S, K) ->
    MaxLen = length(integer_to_list(K)),
    N = byte_size(S),
    BaseMap = maps:put(N, 1, #{}),
    FinalMap = dp_loop(N - 1, S, K, MaxLen, N, BaseMap),
    maps:get(0, FinalMap).

dp_loop(I, _S, _K, _MaxLen, _N, Map) when I < 0 ->
    Map;
dp_loop(I, S, K, MaxLen, N, Map) ->
    case binary:at(S, I) of
        $0 ->
            DP = 0,
            NewMap = maps:put(I, DP, Map),
            dp_loop(I - 1, S, K, MaxLen, N, NewMap);
        _ ->
            DP = compute_dp(I, S, K, MaxLen, N, Map, 0, 0),
            NewMap = maps:put(I, DP, Map),
            dp_loop(I - 1, S, K, MaxLen, N, NewMap)
    end.

compute_dp(_I, _S, _K, _MaxLen, _N, _Map, Len, Sum) when Len > _MaxLen ->
    Sum;
compute_dp(I, S, K, MaxLen, N, Map, Len, Sum) ->
    Pos = I + Len,
    case Pos =< N of
        false -> Sum;
        true ->
            Digit = binary:at(S, Pos - 1),
            Num = (case Len of
                       0 -> 0;
                       _ -> maps:get({num, I, Len}, Map, 0) % placeholder not used
                   end),
            NewNum = Num * 10 + (Digit - $0),
            if NewNum > K ->
                    Sum;
               true ->
                    DPj = maps:get(Pos, Map, 0),
                    NewSum = (Sum + DPj) rem ?MOD,
                    compute_dp(I, S, K, MaxLen, N, Map, Len + 1, NewSum)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @spec number_of_arrays(s :: String.t(), k :: integer) :: integer
  def number_of_arrays(s, k) do
    n = byte_size(s)
    len_k = Integer.digits(k) |> length()
    mod = 1_000_000_007

    dp = :array.new(n + 1, default: 0)
    dp = :array.set(0, 1, dp)

    dp =
      Enum.reduce(0..(n - 1), dp, fn i, acc_dp ->
        ways = :array.get(i, acc_dp)

        if ways == 0 do
          acc_dp
        else
          # check leading zero
          first_bin = :binary.part(s, i, 1)
          <<c>> = first_bin

          if c == ?0 do
            acc_dp
          else
            extend(i, ways, 0, i, acc_dp, s, k, len_k, mod)
          end
        end
      end)

    :array.get(n, dp)
  end

  defp extend(_i, _ways, _num, j, dp, _s, _k, _len_k, _mod) when j >= byte_size(dp) do
    dp
  end

  defp extend(i, ways, num, j, dp, s, k, len_k, mod) do
    if j - i + 1 > len_k or j >= byte_size(s) do
      dp
    else
      bin = :binary.part(s, j, 1)
      <<c>> = bin
      digit = c - ?0
      new_num = num * 10 + digit

      if new_num > k do
        dp
      else
        idx = j + 1
        cur = :array.get(idx, dp)
        new_val = rem(cur + ways, mod)
        dp2 = :array.set(idx, new_val, dp)

        extend(i, ways, new_num, j + 1, dp2, s, k, len_k, mod)
      end
    end
  end
end
```
