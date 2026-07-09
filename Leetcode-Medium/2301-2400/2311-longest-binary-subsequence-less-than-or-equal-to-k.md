# 2311. Longest Binary Subsequence Less Than or Equal to K

## Cpp

```cpp
class Solution {
public:
    int longestSubsequence(string s, int k) {
        long long cur = 0;
        long long pw = 1;               // weight of the current bit (LSB first)
        int onesIncluded = 0;
        for (int i = (int)s.size() - 1; i >= 0; --i) {
            if (s[i] == '1') {
                if (cur + pw <= k) {
                    cur += pw;
                    ++onesIncluded;
                } else {
                    break;               // more significant bits will only be larger
                }
            }
            pw <<= 1;
            if (pw > (1LL << 60)) pw = (1LL << 60); // prevent overflow
        }
        int zeroCnt = 0;
        for (char c : s) if (c == '0') ++zeroCnt;
        return zeroCnt + onesIncluded;
    }
};
```

## Java

```java
class Solution {
    public int longestSubsequence(String s, int k) {
        long cur = 0;
        int ans = 0;
        int power = 0; // number of selected bits to the right
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            if (c == '0') {
                ans++;
                power++;
            } else { // c == '1'
                if (power >= 31) continue; // any addition would exceed k
                long added = 1L << power;
                if (cur + added <= k) {
                    cur += added;
                    ans++;
                    power++;
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
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cur_len = 0
        cur_val = 0
        for ch in reversed(s):
            if ch == '0':
                cur_len += 1
            else:  # ch == '1'
                add = 1 << cur_len
                if cur_val + add <= k:
                    cur_val += add
                    cur_len += 1
        return cur_len
```

## Python3

```python
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = 0
        zeros_seen = 0
        remaining = k
        # Process from least significant side (right to left)
        for ch in reversed(s):
            if ch == '0':
                ans += 1
                zeros_seen += 1
            else:  # ch == '1'
                # If zeros_seen is large, value exceeds any possible k (k <= 1e9 < 2^30)
                if zeros_seen >= 31:
                    continue
                val = 1 << zeros_seen
                if val <= remaining:
                    ans += 1
                    remaining -= val
        return ans
```

## C

```c
#include <string.h>

int longestSubsequence(char* s, int k) {
    int n = strlen(s);
    long long power = 1;
    int onesIncluded = 0;
    int zeroCount = 0;
    for (int i = n - 1; i >= 0; --i) {
        if (s[i] == '0') {
            ++zeroCount;
        } else { // '1'
            if (power <= k) {
                ++onesIncluded;
                k -= (int)power;
            }
        }
        power <<= 1;
    }
    return zeroCount + onesIncluded;
}
```

## Csharp

```csharp
public class Solution {
    public int LongestSubsequence(string s, int k) {
        int zeroCount = 0;
        foreach (char c in s) {
            if (c == '0') zeroCount++;
        }

        long cur = 0;
        long power = 1;
        int oneCount = 0;

        for (int i = s.Length - 1; i >= 0 && power <= k; i--) {
            if (s[i] == '1') {
                if (cur + power <= k) {
                    cur += power;
                    oneCount++;
                }
            }
            power <<= 1;
        }

        return zeroCount + oneCount;
    }
}
```

## Javascript

```javascript
var longestSubsequence = function(s, k) {
    let ans = 0;
    let cur = 0;
    let len = 0; // selected bits count
    for (let i = s.length - 1; i >= 0; --i) {
        const ch = s[i];
        if (ch === '0') {
            ans++;
            len++;
        } else { // '1'
            if (len >= 31) continue; // weight exceeds possible k
            const w = 1 << len;
            if (cur + w <= k) {
                cur += w;
                ans++;
                len++;
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function longestSubsequence(s: string, k: number): number {
    let cur = 0;
    let cnt = 0;
    for (let i = s.length - 1; i >= 0; --i) {
        if (s[i] === '0') {
            cnt++;
        } else { // '1'
            if (cnt >= 31) continue; // any further 1 would exceed k (k < 2^30)
            const add = 1 << cnt;
            if (cur + add <= k) {
                cur += add;
                cnt++;
            }
        }
    }
    return cnt;
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
    function longestSubsequence($s, $k) {
        $n = strlen($s);
        $zeroCount = substr_count($s, '0');
        $ans = $zeroCount;
        $cur = 0;
        $pow = 1;
        for ($i = $n - 1; $i >= 0; --$i) {
            if ($s[$i] === '1') {
                if ($cur + $pow <= $k) {
                    $cur += $pow;
                    $ans++;
                }
            }
            // shift for next more significant position
            $pow <<= 1;
            // further bits will be too large to ever fit, we can stop early
            if ($pow > $k * 2) {
                break;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func longestSubsequence(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        var answer = 0
        var currentValue: Int64 = 0
        var power: Int64 = 1
        let limit = Int64(k)
        
        for i in stride(from: chars.count - 1, through: 0, by: -1) {
            if chars[i] == "0" {
                answer += 1
            } else { // '1'
                if currentValue + power <= limit {
                    answer += 1
                    currentValue += power
                }
            }
            power <<= 1
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestSubsequence(s: String, k: Int): Int {
        var selected = 0          // number of bits already taken to the right
        var value = 0L
        val limit = k.toLong()
        var answer = 0

        for (i in s.length - 1 downTo 0) {
            if (s[i] == '0') {
                selected++
                answer++
            } else { // '1'
                if (selected >= 63) continue   // contribution would overflow and exceed k
                val contrib = 1L shl selected
                if (value + contrib <= limit) {
                    value += contrib
                    selected++
                    answer++
                }
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int longestSubsequence(String s, int k) {
    int ans = 0;
    int cur = 1;
    for (int i = s.length - 1; i >= 0; --i) {
      if (s[i] == '0') {
        ans++;
      } else {
        if (cur <= k) {
          ans++;
          k -= cur;
        }
      }
      cur <<= 1;
    }
    return ans;
  }
}
```

## Golang

```go
func longestSubsequence(s string, k int) int {
	zeroCount := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '0' {
			zeroCount++
		}
	}

	onesCount := 0
	power := 1
	for i := len(s) - 1; i >= 0 && power <= k; i-- {
		if s[i] == '1' {
			onesCount++
		}
		power <<= 1
	}
	return zeroCount + onesCount
}
```

## Ruby

```ruby
def longest_subsequence(s, k)
  zero_cnt = s.count('0')
  ans = zero_cnt
  power = 1
  (s.length - 1).downto(0) do |i|
    if s[i] == '1'
      if power <= k
        ans += 1
        k -= power
      else
        break
      end
    end
    power <<= 1
  end
  ans
end
```

## Scala

```scala
object Solution {
    def longestSubsequence(s: String, k: Int): Int = {
        var ans = 0
        var remaining = k.toLong
        var weight = 1L
        var i = s.length - 1
        while (i >= 0) {
            if (s.charAt(i) == '0') {
                ans += 1
            } else {
                if (weight <= remaining) {
                    ans += 1
                    remaining -= weight
                }
            }
            // update weight for the next more significant position
            if (weight <= k) {
                weight <<= 1
            } else {
                weight = k.toLong + 1 // keep it larger than k
            }
            i -= 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_subsequence(s: String, k: i32) -> i32 {
        let mut sum: i64 = 0;
        let mut power: i64 = 1; // weight of the next selected bit (LSB)
        let limit = k as i64;
        let mut ans: i32 = 0;

        for ch in s.chars().rev() {
            if ch == '0' {
                // always take a zero
                ans += 1;
                power <<= 1; // shift for the next position
            } else {
                // try to take a one if it doesn't exceed k
                if sum + power <= limit {
                    sum += power;
                    ans += 1;
                    power <<= 1; // shift after taking this bit
                }
                // otherwise skip this '1' (do not shift)
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (longest-subsequence s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length s))
         (zero-count
          (let loop ((i 0) (cnt 0))
            (if (= i n)
                cnt
                (loop (+ i 1)
                      (if (char=? (string-ref s i) #\0)
                          (+ cnt 1)
                          cnt))))))
    (let loop ((i (- n 1)) (cur 0) (power 1) (ans zero-count))
      (if (< i 0)
          ans
          (let ((ch (string-ref s i)))
            (cond
              [(char=? ch #\1)
               (if (<= (+ cur power) k)
                   (loop (- i 1) (+ cur power) (* power 2) (+ ans 1))
                   ans)]
              [else
               (loop (- i 1) cur (* power 2) ans)]))))))
```

## Erlang

```erlang
-spec longest_subsequence(S :: unicode:unicode_binary(), K :: integer()) -> integer().
longest_subsequence(S, K) ->
    List = binary:bin_to_list(S),
    process(lists:reverse(List), K, 0, 0).

process([], _K, LenAcc, _Val) ->
    LenAcc;
process([C|Rest], K, LenAcc, Val) when C == $0 ->
    process(Rest, K, LenAcc + 1, Val);
process([C|Rest], K, LenAcc, Val) when C == $1 ->
    Weight = 1 bsl LenAcc,
    if
        Val + Weight =< K ->
            process(Rest, K, LenAcc + 1, Val + Weight);
        true ->
            process(Rest, K, LenAcc, Val)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_subsequence(s :: String.t(), k :: integer) :: integer
  def longest_subsequence(s, k) do
    chars = :binary.bin_to_list(s)

    {len, _cur} =
      Enum.reduce(Enum.reverse(chars), {0, 0}, fn byte, {len, cur} ->
        if byte == ?0 do
          {len + 1, cur}
        else
          # byte == ?1
          if len >= 31 do
            {len, cur}
          else
            weight = 1 <<< len

            if cur + weight <= k do
              {len + 1, cur + weight}
            else
              {len, cur}
            end
          end
        end
      end)

    len
  end
end
```
