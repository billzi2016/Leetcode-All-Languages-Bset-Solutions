# 1542. Find Longest Awesome Substring

## Cpp

```cpp
class Solution {
public:
    int longestAwesome(string s) {
        const int INF = 1e9;
        vector<int> first(1 << 10, INF);
        first[0] = -1; // empty prefix
        int mask = 0;
        int ans = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            int d = s[i] - '0';
            mask ^= (1 << d);
            if (first[mask] != INF) {
                ans = max(ans, i - first[mask]);
            } else {
                first[mask] = i;
            }
            for (int b = 0; b < 10; ++b) {
                int m2 = mask ^ (1 << b);
                if (first[m2] != INF) {
                    ans = max(ans, i - first[m2]);
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int longestAwesome(String s) {
        int[] first = new int[1 << 10];
        Arrays.fill(first, -1);
        int mask = 0;
        first[0] = 0; // empty prefix at index 0
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            int digit = s.charAt(i) - '0';
            mask ^= 1 << digit;

            if (first[mask] != -1) {
                ans = Math.max(ans, i + 1 - first[mask]);
            } else {
                first[mask] = i + 1; // store earliest occurrence
            }

            for (int b = 0; b < 10; b++) {
                int toggled = mask ^ (1 << b);
                if (first[toggled] != -1) {
                    ans = Math.max(ans, i + 1 - first[toggled]);
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
    def longestAwesome(self, s):
        """
        :type s: str
        :rtype: int
        """
        first = {0: -1}
        mask = 0
        res = 0
        for i, ch in enumerate(s):
            digit = ord(ch) - 48
            mask ^= 1 << digit

            if mask in first:
                res = max(res, i - first[mask])
            else:
                first[mask] = i

            # check masks that differ by exactly one bit
            for k in range(10):
                m2 = mask ^ (1 << k)
                if m2 in first:
                    res = max(res, i - first[m2])

        return res
```

## Python3

```python
class Solution:
    def longestAwesome(self, s: str) -> int:
        earliest = {0: -1}
        mask = 0
        ans = 0
        for i, ch in enumerate(s):
            mask ^= 1 << (ord(ch) - ord('0'))
            # same mask
            if mask in earliest:
                ans = max(ans, i - earliest[mask])
            else:
                earliest[mask] = i
            # masks differing by one bit
            for b in range(10):
                toggled = mask ^ (1 << b)
                if toggled in earliest:
                    ans = max(ans, i - earliest[toggled])
        return ans
```

## C

```c
#include <string.h>
#include <limits.h>

int longestAwesome(char* s) {
    int n = (int)strlen(s);
    const int INF = INT_MAX;
    int first[1 << 10];
    for (int i = 0; i < (1 << 10); ++i) first[i] = INF;
    first[0] = 0;

    int mask = 0;
    int ans = 0;

    for (int i = 0; i < n; ++i) {
        int d = s[i] - '0';
        mask ^= (1 << d);

        if (first[mask] != INF) {
            int len = i + 1 - first[mask];
            if (len > ans) ans = len;
        }

        for (int k = 0; k < 10; ++k) {
            int m2 = mask ^ (1 << k);
            if (first[m2] != INF) {
                int len = i + 1 - first[m2];
                if (len > ans) ans = len;
            }
        }

        if (first[mask] == INF) first[mask] = i + 1;
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int LongestAwesome(string s)
    {
        const int TOTAL_MASKS = 1 << 10; // digits 0-9
        int[] firstPos = new int[TOTAL_MASKS];
        for (int i = 0; i < TOTAL_MASKS; i++) firstPos[i] = int.MaxValue;

        int mask = 0;
        firstPos[0] = -1; // empty prefix
        int maxLen = 0;

        for (int i = 0; i < s.Length; i++)
        {
            int digit = s[i] - '0';
            mask ^= 1 << digit;

            if (firstPos[mask] != int.MaxValue)
                maxLen = Math.Max(maxLen, i - firstPos[mask]);
            else
                firstPos[mask] = i;

            for (int b = 0; b < 10; b++)
            {
                int toggled = mask ^ (1 << b);
                if (firstPos[toggled] != int.MaxValue)
                    maxLen = Math.Max(maxLen, i - firstPos[toggled]);
            }
        }

        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var longestAwesome = function(s) {
    const INF = -2;
    const earliest = new Array(1 << 10).fill(INF);
    earliest[0] = -1; // empty prefix
    let mask = 0;
    let ans = 0;
    for (let i = 0; i < s.length; ++i) {
        const d = s.charCodeAt(i) - 48; // digit value
        mask ^= (1 << d);
        if (earliest[mask] !== INF) {
            ans = Math.max(ans, i - earliest[mask]);
        }
        for (let b = 0; b < 10; ++b) {
            const m2 = mask ^ (1 << b);
            if (earliest[m2] !== INF) {
                ans = Math.max(ans, i - earliest[m2]);
            }
        }
        if (earliest[mask] === INF) {
            earliest[mask] = i;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function longestAwesome(s: string): number {
    const INF = Number.MAX_SAFE_INTEGER;
    const first = new Array(1024).fill(INF);
    let mask = 0;
    first[0] = -1; // empty prefix
    let ans = 0;

    for (let i = 0; i < s.length; i++) {
        const digit = s.charCodeAt(i) - 48; // '0' -> 48
        mask ^= (1 << digit);

        if (first[mask] !== INF) {
            ans = Math.max(ans, i - first[mask]);
        } else {
            first[mask] = i;
        }

        for (let b = 0; b < 10; b++) {
            const toggled = mask ^ (1 << b);
            if (first[toggled] !== INF) {
                ans = Math.max(ans, i - first[toggled]);
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
     * @return Integer
     */
    function longestAwesome($s) {
        $firstPos = [];
        $firstPos[0] = -1; // mask 0 before start
        $mask = 0;
        $maxLen = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; ++$i) {
            $digit = ord($s[$i]) - 48;
            $mask ^= (1 << $digit);

            // same mask
            if (isset($firstPos[$mask])) {
                $candidate = $i - $firstPos[$mask];
                if ($candidate > $maxLen) {
                    $maxLen = $candidate;
                }
            }

            // masks differing by one bit
            for ($b = 0; $b < 10; ++$b) {
                $temp = $mask ^ (1 << $b);
                if (isset($firstPos[$temp])) {
                    $candidate = $i - $firstPos[$temp];
                    if ($candidate > $maxLen) {
                        $maxLen = $candidate;
                    }
                }
            }

            // store earliest occurrence of this mask
            if (!isset($firstPos[$mask])) {
                $firstPos[$mask] = $i;
            }
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func longestAwesome(_ s: String) -> Int {
        var firstPos = [Int: Int]()
        firstPos[0] = -1  // mask 0 before any character
        var mask = 0
        var maxLen = 0
        
        for (i, ch) in s.enumerated() {
            let digit = Int(ch.unicodeScalars.first!.value - Unicode.Scalar("0").value)
            mask ^= (1 << digit)
            
            // Same mask -> all even counts
            if let first = firstPos[mask] {
                maxLen = max(maxLen, i - first)
            } else {
                firstPos[mask] = i
            }
            
            // Masks differing by one bit -> exactly one odd count
            for b in 0..<10 {
                let toggled = mask ^ (1 << b)
                if let first = firstPos[toggled] {
                    maxLen = max(maxLen, i - first)
                }
            }
        }
        
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestAwesome(s: String): Int {
        val first = IntArray(1 shl 10) { Int.MAX_VALUE }
        first[0] = -1
        var mask = 0
        var ans = 0
        for (i in s.indices) {
            val d = s[i] - '0'
            mask = mask xor (1 shl d)
            if (first[mask] != Int.MAX_VALUE) {
                ans = kotlin.math.max(ans, i - first[mask])
            } else {
                first[mask] = i
            }
            for (b in 0..9) {
                val toggled = mask xor (1 shl b)
                if (first[toggled] != Int.MAX_VALUE) {
                    ans = kotlin.math.max(ans, i - first[toggled])
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int longestAwesome(String s) {
    const int INF = 1 << 30;
    List<int> first = List.filled(1 << 10, INF);
    int mask = 0;
    first[0] = -1;
    int maxLen = 0;

    for (int i = 0; i < s.length; i++) {
      int digit = s.codeUnitAt(i) - 48;
      mask ^= (1 << digit);

      if (first[mask] != INF) {
        maxLen = max(maxLen, i - first[mask]);
      } else {
        first[mask] = i;
      }

      for (int k = 0; k < 10; k++) {
        int toggled = mask ^ (1 << k);
        if (first[toggled] != INF) {
          maxLen = max(maxLen, i - first[toggled]);
        }
      }
    }

    return maxLen;
  }
}
```

## Golang

```go
func longestAwesome(s string) int {
    const totalMasks = 1 << 10 // 1024
    first := make([]int, totalMasks)
    for i := range first {
        first[i] = -2 // sentinel for unseen masks
    }
    mask := 0
    first[0] = -1 // empty prefix
    maxLen := 0

    for i := 0; i < len(s); i++ {
        d := int(s[i] - '0')
        mask ^= 1 << d

        if first[mask] != -2 {
            if cur := i - first[mask]; cur > maxLen {
                maxLen = cur
            }
        } else {
            first[mask] = i
        }

        for k := 0; k < 10; k++ {
            m2 := mask ^ (1 << k)
            if first[m2] != -2 {
                if cur := i - first[m2]; cur > maxLen {
                    maxLen = cur
                }
            }
        }
    }

    return maxLen
}
```

## Ruby

```ruby
def longest_awesome(s)
  earliest = Array.new(1 << 10, nil)
  mask = 0
  earliest[0] = -1
  max_len = 0

  s.each_char.with_index do |ch, i|
    digit = ch.ord - 48
    mask ^= (1 << digit)

    if (idx = earliest[mask])
      len = i - idx
      max_len = len if len > max_len
    else
      earliest[mask] = i
    end

    10.times do |b|
      m2 = mask ^ (1 << b)
      next unless (idx2 = earliest[m2])

      len = i - idx2
      max_len = len if len > max_len
    end
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def longestAwesome(s: String): Int = {
        val first = Array.fill(1 << 10)(Int.MaxValue)
        first(0) = 0
        var mask = 0
        var ans = 0
        for (i <- s.indices) {
            val digit = s.charAt(i) - '0'
            mask ^= (1 << digit)

            // same parity mask
            if (first(mask) != Int.MaxValue) {
                ans = math.max(ans, i + 1 - first(mask))
            }

            // masks differing by one bit
            var d = 0
            while (d < 10) {
                val m2 = mask ^ (1 << d)
                if (first(m2) != Int.MaxValue) {
                    ans = math.max(ans, i + 1 - first(m2))
                }
                d += 1
            }

            // record earliest occurrence of this mask
            if (first(mask) == Int.MaxValue) {
                first(mask) = i + 1
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_awesome(s: String) -> i32 {
        let bytes = s.as_bytes();
        // first[mask] = earliest index where this mask appeared, -2 means unseen
        let mut first = vec![-2i32; 1024];
        first[0] = -1;
        let mut mask: usize = 0;
        let mut ans: i32 = 0;
        for (i, &b) in bytes.iter().enumerate() {
            let d = (b - b'0') as usize;
            mask ^= 1 << d;

            // same mask
            if first[mask] != -2 {
                ans = ans.max(i as i32 - first[mask]);
            } else {
                first[mask] = i as i32;
            }

            // masks differing by one bit
            for j in 0..10 {
                let m2 = mask ^ (1 << j);
                if first[m2] != -2 {
                    ans = ans.max(i as i32 - first[m2]);
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (longest-awesome s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (vec (make-vector 1024 -2))
         (ans 0)
         (mask 0))
    (vector-set! vec 0 -1)
    (for ([i (in-range n)])
      (let* ((ch (string-ref s i))
             (digit (- (char->integer ch) (char->integer #\0))))
        (set! mask (bitwise-xor mask (arithmetic-shift 1 digit)))
        ;; same mask
        (let ((first (vector-ref vec mask)))
          (when (not (= first -2))
            (set! ans (max ans (- i first)))))
        ;; one bit difference
        (for ([b (in-range 10)])
          (let* ((m2 (bitwise-xor mask (arithmetic-shift 1 b)))
                 (first2 (vector-ref vec m2)))
            (when (not (= first2 -2))
              (set! ans (max ans (- i first2))))))
        ;; store earliest occurrence
        (when (= (vector-ref vec mask) -2)
          (vector-set! vec mask i)))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([longest_awesome/1]).

-spec longest_awesome(S :: unicode:unicode_binary()) -> integer().
longest_awesome(S) ->
    longest_awesome_loop(S, 0, 0, #{0 => -1}, 0).

longest_awesome_loop(<<>>, _Idx, _Mask, _Map, Max) ->
    Max;
longest_awesome_loop(<<Char, Rest/binary>>, Idx, Mask, Map, Max) ->
    Digit = Char - $0,
    NewMask = Mask bxor (1 bsl Digit),
    Max1 = case maps:find(NewMask, Map) of
               {ok, Pos} -> erlang:max(Max, Idx - Pos);
               error -> Max
           end,
    Max2 = lists:foldl(fun(K, Acc) ->
                Tog = NewMask bxor (1 bsl K),
                case maps:find(Tog, Map) of
                    {ok, PosT} -> erlang:max(Acc, Idx - PosT);
                    error -> Acc
                end
            end, Max1, lists:seq(0, 9)),
    UpdatedMap = case maps:is_key(NewMask, Map) of
                     true -> Map;
                     false -> maps:put(NewMask, Idx, Map)
                 end,
    longest_awesome_loop(Rest, Idx + 1, NewMask, UpdatedMap, Max2).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_awesome(s :: String.t()) :: integer
  def longest_awesome(s) do
    import Bitwise

    bytes = :binary.bin_to_list(s)

    {max_len, _mask, _map} =
      Enum.reduce(Enum.with_index(bytes), {0, 0, %{0 => -1}}, fn {b, i},
                                                               {ans, mask, map} ->
        digit = b - ?0
        new_mask = bxor(mask, 1 <<< digit)

        ans1 =
          case Map.get(map, new_mask) do
            nil -> ans
            idx -> max(ans, i - idx)
          end

        ans2 =
          Enum.reduce(0..9, ans1, fn k, acc ->
            toggled = bxor(new_mask, 1 <<< k)

            case Map.get(map, toggled) do
              nil -> acc
              idx -> max(acc, i - idx)
            end
          end)

        new_map = Map.put_new(map, new_mask, i)
        {ans2, new_mask, new_map}
      end)

    max_len
  end
end
```
