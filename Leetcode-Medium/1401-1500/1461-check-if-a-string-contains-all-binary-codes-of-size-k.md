# 1461. Check If a String Contains All Binary Codes of Size K

## Cpp

```cpp
class Solution {
public:
    bool hasAllCodes(string s, int k) {
        int n = s.size();
        if (n < k) return false;
        int total = 1 << k;
        vector<char> seen(total, 0);
        int mask = 0;
        for (int i = 0; i < k; ++i) {
            mask = (mask << 1) | (s[i] - '0');
        }
        seen[mask] = 1;
        int cnt = 1;
        int bitmask = total - 1;
        for (int i = k; i < n; ++i) {
            mask = ((mask << 1) & bitmask) | (s[i] - '0');
            if (!seen[mask]) {
                seen[mask] = 1;
                ++cnt;
                if (cnt == total) return true;
            }
        }
        return cnt == total;
    }
};
```

## Java

```java
class Solution {
    public boolean hasAllCodes(String s, int k) {
        int n = s.length();
        if (n < k) return false;
        int total = 1 << k;
        boolean[] seen = new boolean[total];
        int mask = total - 1;
        int cur = 0;
        int count = 0;
        for (int i = 0; i < n; i++) {
            cur = ((cur << 1) & mask) | (s.charAt(i) - '0');
            if (i >= k - 1) {
                if (!seen[cur]) {
                    seen[cur] = true;
                    count++;
                    if (count == total) return true;
                }
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        if n < k:
            return False

        total = 1 << k
        seen = [False] * total
        mask = total - 1

        cur = 0
        for i in range(k):
            cur = (cur << 1) | (s[i] == '1')
        seen[cur] = True
        count = 1

        for i in range(k, n):
            # shift left, add new bit, keep only k bits
            cur = ((cur << 1) & mask) | (s[i] == '1')
            if not seen[cur]:
                seen[cur] = True
                count += 1
                if count == total:
                    return True

        return count == total
```

## Python3

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        total = 1 << k
        seen = [False] * total
        mask = total - 1

        cur = 0
        for i in range(k):
            cur = (cur << 1) | (s[i] == '1')
        seen[cur] = True
        count = 1

        for i in range(k, n):
            cur = ((cur << 1) & mask) | (s[i] == '1')
            if not seen[cur]:
                seen[cur] = True
                count += 1
                if count == total:
                    return True
        return count == total
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool hasAllCodes(char* s, int k) {
    int n = strlen(s);
    if (n < k) return false;
    int total = 1 << k;
    bool *seen = calloc(total, sizeof(bool));
    int mask = total - 1;
    int val = 0;
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        val = ((val << 1) & mask) | (s[i] - '0');
        if (i >= k - 1) {
            if (!seen[val]) {
                seen[val] = true;
                if (++cnt == total) {
                    free(seen);
                    return true;
                }
            }
        }
    }
    free(seen);
    return false;
}
```

## Csharp

```csharp
public class Solution
{
    public bool HasAllCodes(string s, int k)
    {
        if (s.Length < k) return false;
        int total = 1 << k;
        var seen = new bool[total];
        int mask = total - 1;
        int cur = 0;
        int count = 0;

        for (int i = 0; i < s.Length; i++)
        {
            cur = ((cur << 1) & mask) | (s[i] - '0');
            if (i >= k - 1)
            {
                if (!seen[cur])
                {
                    seen[cur] = true;
                    count++;
                    if (count == total) return true;
                }
            }
        }

        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */
var hasAllCodes = function(s, k) {
    const n = s.length;
    if (n < k) return false;
    const total = 1 << k;               // number of possible codes
    const mask = total - 1;             // keep only last k bits
    const seen = new Uint8Array(total); // boolean array
    let count = 0;
    let cur = 0;

    // build first window
    for (let i = 0; i < k; ++i) {
        cur = (cur << 1) | (s.charCodeAt(i) - 48);
    }
    if (!seen[cur]) {
        seen[cur] = 1;
        ++count;
    }

    // slide window
    for (let i = k; i < n; ++i) {
        cur = ((cur << 1) & mask) | (s.charCodeAt(i) - 48);
        if (!seen[cur]) {
            seen[cur] = 1;
            ++count;
            if (count === total) return true; // early exit
        }
    }

    return count === total;
};
```

## Typescript

```typescript
function hasAllCodes(s: string, k: number): boolean {
    const n = s.length;
    if (n < k) return false;

    const total = 1 << k;
    const seen = new Uint8Array(total);
    const mask = total - 1;

    let val = 0;
    for (let i = 0; i < k; ++i) {
        val = (val << 1) | (s.charCodeAt(i) - 48);
    }
    seen[val] = 1;
    let count = 1;
    if (count === total) return true;

    for (let i = k; i < n; ++i) {
        val = ((val << 1) & mask) | (s.charCodeAt(i) - 48);
        if (!seen[val]) {
            seen[val] = 1;
            if (++count === total) return true;
        }
    }

    return count === total;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Boolean
     */
    function hasAllCodes($s, $k) {
        $n = strlen($s);
        if ($n < $k) return false;

        $need = 1 << $k;
        $mask = $need - 1; // keep only last k bits

        $val = 0;
        for ($i = 0; $i < $k; $i++) {
            $val = ($val << 1) | ($s[$i] === '1' ? 1 : 0);
        }

        $seen = [];
        $seen[$val] = true;
        $count = 1;

        for ($i = $k; $i < $n; $i++) {
            $val = (($val << 1) & $mask) | ($s[$i] === '1' ? 1 : 0);
            if (!isset($seen[$val])) {
                $seen[$val] = true;
                $count++;
                if ($count == $need) return true;
            }
        }

        return $count == $need;
    }
}
```

## Swift

```swift
class Solution {
    func hasAllCodes(_ s: String, _ k: Int) -> Bool {
        let n = s.count
        if n < k { return false }
        let totalNeeded = 1 << k
        var seen = [Bool](repeating: false, count: totalNeeded)
        var cur = 0
        var count = 0
        let mask = totalNeeded - 1
        let bytes = Array(s.utf8)
        for i in 0..<n {
            let bit = (bytes[i] == 49) ? 1 : 0   // ASCII '1' is 49
            cur = ((cur << 1) & mask) | bit
            if i >= k - 1 {
                if !seen[cur] {
                    seen[cur] = true
                    count += 1
                    if count == totalNeeded { return true }
                }
            }
        }
        return count == totalNeeded
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun hasAllCodes(s: String, k: Int): Boolean {
        val n = s.length
        if (n < k) return false
        val total = 1 shl k
        val seen = BooleanArray(total)
        var cur = 0
        val mask = total - 1
        var count = 0
        for (i in 0 until n) {
            cur = ((cur shl 1) and mask) or (s[i] - '0')
            if (i >= k - 1) {
                if (!seen[cur]) {
                    seen[cur] = true
                    count++
                    if (count == total) return true
                }
            }
        }
        return false
    }
}
```

## Dart

```dart
import 'dart:typed_data';

class Solution {
  bool hasAllCodes(String s, int k) {
    if (k > s.length) return false;
    final total = 1 << k;
    final seen = Uint8List(total);
    int cur = 0;
    int count = 0;
    final mask = total - 1;

    for (int i = 0; i < s.length; ++i) {
      cur = ((cur << 1) & mask) | (s.codeUnitAt(i) - 48);
      if (i >= k - 1) {
        if (seen[cur] == 0) {
          seen[cur] = 1;
          count++;
          if (count == total) return true;
        }
      }
    }
    return count == total;
  }
}
```

## Golang

```go
func hasAllCodes(s string, k int) bool {
    n := len(s)
    if n < k {
        return false
    }
    total := 1 << k
    seen := make([]bool, total)
    mask := total - 1
    cur := 0
    count := 0

    for i := 0; i < n; i++ {
        cur = ((cur << 1) & mask) | int(s[i]-'0')
        if i >= k-1 {
            if !seen[cur] {
                seen[cur] = true
                count++
                if count == total {
                    return true
                }
            }
        }
    }
    return false
}
```

## Ruby

```ruby
def has_all_codes(s, k)
  n = s.length
  return false if n < k
  total = 1 << k
  seen = Array.new(total, false)
  mask = total - 1
  cur = 0
  count = 0
  s.each_char.with_index do |ch, i|
    cur = ((cur << 1) & mask) | (ch == '1' ? 1 : 0)
    if i >= k - 1
      unless seen[cur]
        seen[cur] = true
        count += 1
        return true if count == total
      end
    end
  end
  false
end
```

## Scala

```scala
object Solution {
    def hasAllCodes(s: String, k: Int): Boolean = {
        val n = s.length
        if (n < k) return false
        val total = 1 << k
        val seen = new Array[Boolean](total)
        var count = 0
        var cur = 0
        val mask = total - 1
        var i = 0
        while (i < n) {
            cur = ((cur << 1) & mask) | (s.charAt(i) - '0')
            if (i >= k - 1) {
                if (!seen(cur)) {
                    seen(cur) = true
                    count += 1
                    if (count == total) return true
                }
            }
            i += 1
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn has_all_codes(s: String, k: i32) -> bool {
        let n = s.len();
        let kk = k as usize;
        if n < kk {
            return false;
        }
        let total = 1usize << kk;
        let mut seen = vec![false; total];
        let mask = total - 1;
        let bytes = s.as_bytes();
        let mut val: usize = 0;
        for i in 0..n {
            val = ((val << 1) & mask) | (bytes[i] - b'0') as usize;
            if i + 1 >= kk {
                seen[val] = true;
            }
        }
        seen.iter().all(|&b| b)
    }
}
```

## Racket

```racket
(define/contract (has-all-codes s k)
  (-> string? exact-integer? boolean?)
  (let* ((n (string-length s))
         (total (arithmetic-shift 1 k))          ; 2^k
         (mask (sub1 total))                     ; (1<<k)-1
         (seen (make-vector total #f)))
    (if (< n k)
        #f
        (let loop ((i 0) (cur 0) (cnt 0))
          (if (= i n)
              (= cnt total)
              (let* ((bit (if (char=? (string-ref s i) #\1) 1 0))
                     (new-cur (bitwise-and (+ (arithmetic-shift cur 1) bit) mask)))
                (if (>= i (- k 1))
                    (let ((already (vector-ref seen new-cur)))
                      (if already
                          (loop (+ i 1) new-cur cnt)
                          (begin
                            (vector-set! seen new-cur #t)
                            (loop (+ i 1) new-cur (+ cnt 1)))))
                    (loop (+ i 1) new-cur cnt)))))))))
```

## Erlang

```erlang
-spec has_all_codes(S :: unicode:unicode_binary(), K :: integer()) -> boolean().
has_all_codes(S, K) when is_binary(S), K >= 1 ->
    Len = byte_size(S),
    if
        Len < K -> false;
        true ->
            Needed = 1 bsl K,
            Mask = Needed - 1,
            go(S, K, Needed, Mask, 0, 0, #{}, 0)
    end.

go(<<>>, _K, _Needed, _Mask, _Idx, _Cur, _Set, _Count) ->
    false;
go(Bin, K, Needed, Mask, Idx, Cur, Set, Count) ->
    <<C, Rest/binary>> = Bin,
    Bit = C - $0,
    NewCurTmp = ((Cur bsl 1) bor Bit),
    NewCur = NewCurTmp band Mask,
    NewIdx = Idx + 1,
    case NewIdx >= K of
        true ->
            case maps:is_key(NewCur, Set) of
                true ->
                    go(Rest, K, Needed, Mask, NewIdx, NewCur, Set, Count);
                false ->
                    NewSet = maps:put(NewCur, true, Set),
                    NewCount = Count + 1,
                    if
                        NewCount == Needed -> true;
                        true -> go(Rest, K, Needed, Mask, NewIdx, NewCur, NewSet, NewCount)
                    end
            end;
        false ->
            go(Rest, K, Needed, Mask, NewIdx, NewCur, Set, Count)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec has_all_codes(s :: String.t(), k :: integer) :: boolean
  def has_all_codes(s, k) do
    total = 1 <<< k
    mask_limit = total - 1

    {_, codes_set, _} =
      s
      |> String.to_charlist()
      |> Enum.reduce({0, MapSet.new(), 0}, fn ch, {mask, set, cnt} ->
        bit = if ch == ?1, do: 1, else: 0
        mask = ((mask <<< 1) ||| bit) &&& mask_limit
        cnt = cnt + 1

        if cnt >= k do
          {mask, MapSet.put(set, mask), cnt}
        else
          {mask, set, cnt}
        end
      end)

    MapSet.size(codes_set) == total
  end
end
```
