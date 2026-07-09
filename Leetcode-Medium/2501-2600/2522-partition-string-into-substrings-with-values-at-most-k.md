# 2522. Partition String Into Substrings With Values at Most K

## Cpp

```cpp
class Solution {
public:
    int minimumPartition(string s, int k) {
        long long cur = 0;
        int parts = 0;
        for (char ch : s) {
            int d = ch - '0';
            if (d > k) return -1; // single digit exceeds k
            long long nxt = cur * 10 + d;
            if (nxt > k) {
                ++parts;
                cur = d;
            } else {
                cur = nxt;
            }
        }
        if (cur > 0) ++parts;
        return parts;
    }
};
```

## Java

```java
class Solution {
    public int minimumPartition(String s, int k) {
        int n = s.length();
        int partitions = 0;
        int i = 0;
        while (i < n) {
            long cur = 0;
            int j = i;
            while (j < n) {
                int digit = s.charAt(j) - '0';
                if (cur * 10 + digit > k) break;
                cur = cur * 10 + digit;
                j++;
            }
            if (j == i) return -1; // single digit exceeds k
            partitions++;
            i = j;
        }
        return partitions;
    }
}
```

## Python

```python
class Solution(object):
    def minimumPartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0
        cur = 0
        for ch in s:
            digit = ord(ch) - 48
            if digit > k:
                return -1
            cur = cur * 10 + digit
            if cur > k:
                ans += 1
                cur = digit
        return ans + 1
```

## Python3

```python
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        count = 1
        cur = 0
        for ch in s:
            d = ord(ch) - 48  # faster than int()
            if d > k:
                return -1
            nxt = cur * 10 + d
            if nxt <= k:
                cur = nxt
            else:
                count += 1
                cur = d
        return count
```

## C

```c
int minimumPartition(char* s, int k) {
    long long K = k;
    long long cur = 0;
    int partitions = 0;
    for (int i = 0; s[i]; ++i) {
        int d = s[i] - '0';
        if (cur * 10 + d > K) {
            ++partitions;
            cur = d;
            if (cur > K) return -1;
        } else {
            cur = cur * 10 + d;
        }
    }
    return partitions + (cur > 0 ? 1 : 0);
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumPartition(string s, int k) {
        long K = k;
        int n = s.Length;
        int partitions = 0;
        int i = 0;
        while (i < n) {
            long cur = 0;
            int j = i;
            while (j < n) {
                int digit = s[j] - '0';
                if (cur * 10 + digit > K) break;
                cur = cur * 10 + digit;
                j++;
            }
            if (j == i) return -1; // single digit exceeds k
            partitions++;
            i = j;
        }
        return partitions;
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
var minimumPartition = function(s, k) {
    const n = s.length;
    let i = 0;
    let parts = 0;
    while (i < n) {
        let cur = 0;
        const start = i;
        while (i < n) {
            const d = s.charCodeAt(i) - 48; // digit value
            if (cur * 10 + d > k) break;
            cur = cur * 10 + d;
            i++;
        }
        if (i === start) return -1; // single digit exceeds k
        parts++;
    }
    return parts;
};
```

## Typescript

```typescript
function minimumPartition(s: string, k: number): number {
    let partitions = 1;
    let current = 0;

    for (let i = 0; i < s.length; i++) {
        const digit = s.charCodeAt(i) - 48; // '0' -> 48
        if (digit > k) return -1;

        const nextVal = current * 10 + digit;
        if (nextVal <= k) {
            current = nextVal;
        } else {
            partitions++;
            current = digit;
        }
    }

    return partitions;
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
    function minimumPartition($s, $k) {
        $n = strlen($s);
        $cnt = 0;
        $i = 0;
        while ($i < $n) {
            $num = 0;
            $start = $i;
            while ($i < $n) {
                $digit = ord($s[$i]) - 48; // convert char to int
                $num = $num * 10 + $digit;
                if ($num > $k) {
                    break;
                }
                $i++;
            }
            if ($i == $start) { // cannot take even one digit
                return -1;
            }
            $cnt++;
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func minimumPartition(_ s: String, _ k: Int) -> Int {
        let limit = Int64(k)
        var ans = 0
        var cur: Int64 = 0
        
        for ch in s {
            guard let digitVal = ch.wholeNumberValue else { continue }
            let d = Int64(digitVal)
            
            if cur == 0 {
                if d > limit { return -1 }
                cur = d
            } else {
                if cur * 10 + d <= limit {
                    cur = cur * 10 + d
                } else {
                    ans += 1
                    if d > limit { return -1 }
                    cur = d
                }
            }
        }
        
        if cur > 0 {
            ans += 1
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumPartition(s: String, k: Int): Int {
        var partitions = 0
        var current = 0L
        val limit = k.toLong()
        for (ch in s) {
            val digit = ch - '0'
            if (digit > k) return -1
            current = current * 10 + digit
            if (current > limit) {
                partitions++
                current = digit.toLong()
            }
        }
        // At least one substring exists because s is non‑empty.
        return partitions + 1
    }
}
```

## Dart

```dart
class Solution {
  int minimumPartition(String s, int k) {
    int n = s.length;
    int ans = 0;
    int i = 0;
    while (i < n) {
      int cur = 0;
      while (i < n) {
        int d = s.codeUnitAt(i) - 48; // digit value
        if (d > k) return -1;
        // If adding this digit exceeds k, stop current substring.
        if (cur > k ~/ 10 || (cur == k ~/ 10 && d > k % 10)) {
          break;
        }
        cur = cur * 10 + d;
        i++;
      }
      ans++;
    }
    return ans;
  }
}
```

## Golang

```go
func minimumPartition(s string, k int) int {
	kk := int64(k)
	count := 1
	var cur int64 = 0
	for i := 0; i < len(s); i++ {
		d := int64(s[i] - '0')
		if d > kk {
			return -1
		}
		cur = cur*10 + d
		if cur > kk {
			count++
			cur = d
		}
	}
	return count
}
```

## Ruby

```ruby
def minimum_partition(s, k)
  n = s.length
  i = 0
  count = 0
  while i < n
    cur = 0
    j = i
    while j < n
      cur = cur * 10 + (s.getbyte(j) - 48)
      break if cur > k
      j += 1
    end
    return -1 if j == i
    count += 1
    i = j
  end
  count
end
```

## Scala

```scala
object Solution {
    def minimumPartition(s: String, k: Int): Int = {
        var count = 0
        var cur: Long = 0L
        val K = k.toLong
        for (ch <- s) {
            val d = ch - '0'
            if (d > k) return -1
            cur = cur * 10 + d
            if (cur > K) {
                count += 1
                cur = d.toLong
            }
        }
        count + 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_partition(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut i = 0usize;
        let mut parts = 0i32;
        let k64 = k as i64;

        while i < n {
            let mut cur: i64 = 0;
            let mut next_i: Option<usize> = None;
            // Digits are 1..9, so a valid substring cannot be longer than 9 digits for k <= 1e9
            for j in i..std::cmp::min(n, i + 10) {
                cur = cur * 10 + (bytes[j] - b'0') as i64;
                if cur > k64 {
                    break;
                }
                next_i = Some(j + 1);
            }
            match next_i {
                Some(pos) => {
                    parts += 1;
                    i = pos;
                }
                None => return -1,
            }
        }

        parts
    }
}
```

## Racket

```racket
(define/contract (minimum-partition s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length s)))
    (letrec
        ((process
           (lambda (pos cnt)
             (if (= pos n)
                 cnt
                 (let loop ((j pos) (val 0) (taken? #f))
                   (if (>= j n)
                       (if taken?
                           (process j (+ cnt 1))
                           -1)
                       (let* ((digit (- (char->integer (string-ref s j))
                                        (char->integer #\0)))
                              (newval (+ (* val 10) digit)))
                         (if (> newval k)
                             (if taken?
                                 (process j (+ cnt 1))
                                 -1)
                             (loop (+ j 1) newval #t)))))))))
      (process 0 0))))
```

## Erlang

```erlang
-spec minimum_partition(S :: unicode:unicode_binary(), K :: integer()) -> integer().
minimum_partition(S, K) ->
    case process(S, K, 0, 0, false) of
        -1 -> -1;
        Count -> Count
    end.

process(<<>>, _K, _Cur, Count, true) ->
    Count + 1;
process(<<>>, _K, _Cur, _Count, false) ->
    0;
process(<<DigitChar, Rest/binary>>, K, Cur, Count, Started) ->
    Digit = DigitChar - $0,
    case Started of
        false ->
            if Digit > K -> -1;
               true -> process(Rest, K, Digit, Count, true)
            end;
        true ->
            NewVal = Cur * 10 + Digit,
            if NewVal =< K ->
                    process(Rest, K, NewVal, Count, true);
               true ->
                    if Digit > K -> -1;
                       true -> process(Rest, K, Digit, Count + 1, true)
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_partition(s :: String.t(), k :: integer) :: integer
  def minimum_partition(s, k) do
    {cnt, cur, impossible} =
      :binary.bin_to_list(s)
      |> Enum.reduce({0, 0, false}, fn byte, {cnt, cur_val, imp} ->
        if imp do
          {cnt, cur_val, true}
        else
          d = byte - ?0

          cond do
            d > k ->
              {cnt, cur_val, true}

            cur_val == 0 ->
              # start a new substring with this digit
              {cnt, d, false}

            true ->
              new_cur = cur_val * 10 + d

              if new_cur <= k do
                {cnt, new_cur, false}
              else
                # cut before this digit, start new substring
                {cnt + 1, d, false}
              end
          end
        end
      end)

    if impossible do
      -1
    else
      if cur == 0, do: cnt, else: cnt + 1
    end
  end
end
```
