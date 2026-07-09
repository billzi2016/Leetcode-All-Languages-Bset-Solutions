# 2287. Rearrange Characters to Make Target String

## Cpp

```cpp
class Solution {
public:
    int rearrangeCharacters(string s, string target) {
        vector<int> cntS(26, 0), cntT(26, 0);
        for (char c : s) cntS[c - 'a']++;
        for (char c : target) cntT[c - 'a']++;
        int ans = INT_MAX;
        for (int i = 0; i < 26; ++i) {
            if (cntT[i] > 0) {
                ans = min(ans, cntS[i] / cntT[i]);
            }
        }
        return ans == INT_MAX ? 0 : ans;
    }
};
```

## Java

```java
class Solution {
    public int rearrangeCharacters(String s, String target) {
        int[] cntS = new int[26];
        int[] cntT = new int[26];
        for (int i = 0; i < s.length(); i++) {
            cntS[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < target.length(); i++) {
            cntT[target.charAt(i) - 'a']++;
        }
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < 26; i++) {
            if (cntT[i] > 0) {
                ans = Math.min(ans, cntS[i] / cntT[i]);
            }
        }
        return ans == Integer.MAX_VALUE ? 0 : ans;
    }
}
```

## Python

```python
class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        from collections import Counter
        cnt_s = Counter(s)
        cnt_t = Counter(target)
        # Initialize answer with a large number
        ans = float('inf')
        for ch, need in cnt_t.items():
            have = cnt_s.get(ch, 0)
            ans = min(ans, have // need)
            if ans == 0:
                break
        return 0 if ans == float('inf') else ans
```

## Python3

```python
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        from collections import Counter
        cnt_s = Counter(s)
        cnt_t = Counter(target)
        ans = float('inf')
        for ch, need in cnt_t.items():
            if ch not in cnt_s:
                return 0
            ans = min(ans, cnt_s[ch] // need)
        return ans if ans != float('inf') else 0
```

## C

```c
#include <limits.h>

int rearrangeCharacters(char* s, char* target) {
    int cntS[26] = {0};
    int cntT[26] = {0};

    for (char *p = s; *p != '\0'; ++p) {
        cntS[*p - 'a']++;
    }
    for (char *p = target; *p != '\0'; ++p) {
        cntT[*p - 'a']++;
    }

    int result = INT_MAX;
    for (int i = 0; i < 26; ++i) {
        if (cntT[i] > 0) {
            int copies = cntS[i] / cntT[i];
            if (copies < result) result = copies;
        }
    }

    // If target has no characters (should not happen per constraints), return 0
    if (result == INT_MAX) result = 0;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int RearrangeCharacters(string s, string target) {
        int[] countS = new int[26];
        int[] countT = new int[26];
        
        foreach (char c in s) {
            countS[c - 'a']++;
        }
        foreach (char c in target) {
            countT[c - 'a']++;
        }
        
        int result = int.MaxValue;
        for (int i = 0; i < 26; i++) {
            if (countT[i] > 0) {
                result = Math.Min(result, countS[i] / countT[i]);
            }
        }
        return result == int.MaxValue ? 0 : result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} target
 * @return {number}
 */
var rearrangeCharacters = function(s, target) {
    const countS = new Array(26).fill(0);
    const countT = new Array(26).fill(0);
    
    for (let i = 0; i < s.length; ++i) {
        countS[s.charCodeAt(i) - 97]++;
    }
    for (let i = 0; i < target.length; ++i) {
        countT[target.charCodeAt(i) - 97]++;
    }
    
    let ans = Infinity;
    for (let i = 0; i < 26; ++i) {
        if (countT[i] > 0) {
            ans = Math.min(ans, Math.floor(countS[i] / countT[i]));
        }
    }
    return ans === Infinity ? 0 : ans;
};
```

## Typescript

```typescript
function rearrangeCharacters(s: string, target: string): number {
    const sCount = new Array(26).fill(0);
    for (const ch of s) {
        sCount[ch.charCodeAt(0) - 97]++;
    }
    const tCount = new Array(26).fill(0);
    for (const ch of target) {
        tCount[ch.charCodeAt(0) - 97]++;
    }

    let ans = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < 26; i++) {
        if (tCount[i] > 0) {
            ans = Math.min(ans, Math.floor(sCount[i] / tCount[i]));
        }
    }
    return ans === Number.MAX_SAFE_INTEGER ? 0 : ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $target
     * @return Integer
     */
    function rearrangeCharacters($s, $target) {
        $cntS = array_fill(0, 26, 0);
        $cntT = array_fill(0, 26, 0);

        $lenS = strlen($s);
        for ($i = 0; $i < $lenS; $i++) {
            $idx = ord($s[$i]) - 97;
            $cntS[$idx]++;
        }

        $lenT = strlen($target);
        for ($i = 0; $i < $lenT; $i++) {
            $idx = ord($target[$i]) - 97;
            $cntT[$idx]++;
        }

        $ans = PHP_INT_MAX;
        for ($i = 0; $i < 26; $i++) {
            if ($cntT[$i] > 0) {
                $possible = intdiv($cntS[$i], $cntT[$i]);
                if ($possible < $ans) {
                    $ans = $possible;
                }
            }
        }

        return $ans === PHP_INT_MAX ? 0 : $ans;
    }
}
```

## Swift

```swift
class Solution {
    func rearrangeCharacters(_ s: String, _ target: String) -> Int {
        var freqS = [Int](repeating: 0, count: 26)
        var freqT = [Int](repeating: 0, count: 26)
        
        for byte in s.utf8 {
            let idx = Int(byte - 97)
            if idx >= 0 && idx < 26 {
                freqS[idx] += 1
            }
        }
        
        for byte in target.utf8 {
            let idx = Int(byte - 97)
            if idx >= 0 && idx < 26 {
                freqT[idx] += 1
            }
        }
        
        var answer = Int.max
        for i in 0..<26 where freqT[i] > 0 {
            answer = min(answer, freqS[i] / freqT[i])
        }
        return answer == Int.max ? 0 : answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rearrangeCharacters(s: String, target: String): Int {
        val sCount = IntArray(26)
        val tCount = IntArray(26)
        for (ch in s) {
            sCount[ch - 'a']++
        }
        for (ch in target) {
            tCount[ch - 'a']++
        }
        var result = Int.MAX_VALUE
        for (i in 0 until 26) {
            if (tCount[i] > 0) {
                val copies = sCount[i] / tCount[i]
                if (copies < result) result = copies
            }
        }
        return if (result == Int.MAX_VALUE) 0 else result
    }
}
```

## Dart

```dart
class Solution {
  int rearrangeCharacters(String s, String target) {
    List<int> cntS = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      cntS[s.codeUnitAt(i) - 97]++;
    }

    List<int> cntT = List.filled(26, 0);
    for (int i = 0; i < target.length; i++) {
      cntT[target.codeUnitAt(i) - 97]++;
    }

    int ans = s.length;
    for (int i = 0; i < 26; i++) {
      if (cntT[i] > 0) {
        int copies = cntS[i] ~/ cntT[i];
        if (copies < ans) ans = copies;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func rearrangeCharacters(s string, target string) int {
    var cntS [26]int
    var cntT [26]int
    for _, ch := range s {
        cntS[ch-'a']++
    }
    for _, ch := range target {
        cntT[ch-'a']++
    }
    ans := len(s)
    for i := 0; i < 26; i++ {
        if cntT[i] > 0 {
            copies := cntS[i] / cntT[i]
            if copies < ans {
                ans = copies
            }
        }
    }
    return ans
}
```

## Ruby

```ruby
def rearrange_characters(s, target)
  s_cnt = Hash.new(0)
  s.each_char { |c| s_cnt[c] += 1 }

  t_cnt = Hash.new(0)
  target.each_char { |c| t_cnt[c] += 1 }

  min_copies = Float::INFINITY
  t_cnt.each do |ch, need|
    copies = s_cnt[ch] / need
    min_copies = [min_copies, copies].min
  end

  min_copies
end
```

## Scala

```scala
object Solution {
    def rearrangeCharacters(s: String, target: String): Int = {
        val freqS = Array.fill(26)(0)
        for (c <- s) freqS(c - 'a') += 1
        val freqT = Array.fill(26)(0)
        for (c <- target) freqT(c - 'a') += 1

        var ans = Int.MaxValue
        for (i <- 0 until 26) {
            if (freqT(i) > 0) {
                ans = math.min(ans, freqS(i) / freqT(i))
            }
        }
        if (ans == Int.MaxValue) 0 else ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn rearrange_characters(s: String, target: String) -> i32 {
        let mut cnt_s = [0i32; 26];
        for b in s.bytes() {
            cnt_s[(b - b'a') as usize] += 1;
        }
        let mut cnt_t = [0i32; 26];
        for b in target.bytes() {
            cnt_t[(b - b'a') as usize] += 1;
        }
        let mut ans = i32::MAX;
        for i in 0..26 {
            if cnt_t[i] > 0 {
                let copies = cnt_s[i] / cnt_t[i];
                if copies < ans {
                    ans = copies;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (rearrange-characters s target)
  (-> string? string? exact-integer?)
  (let* ([len-s (string-length s)]
         [len-t (string-length target)]
         [freq-s (make-vector 26 0)]
         [freq-t (make-vector 26 0)])
    ;; count characters in s
    (for ([i (in-range len-s)])
      (let* ([c (string-ref s i)]
             [idx (- (char->integer c) (char->integer #\a))])
        (vector-set! freq-s idx (+ 1 (vector-ref freq-s idx)))))
    ;; count characters in target
    (for ([i (in-range len-t)])
      (let* ([c (string-ref target i)]
             [idx (- (char->integer c) (char->integer #\a))])
        (vector-set! freq-t idx (+ 1 (vector-ref freq-t idx)))))
    ;; compute minimal copies possible
    (let loop ((i 0) (ans (expt 2 30))) ; start with a large number
      (if (= i 26)
          ans
          (let ([need (vector-ref freq-t i)])
            (if (> need 0)
                (let* ([have (vector-ref freq-s i)]
                       [copies (quotient have need)])
                  (loop (+ i 1) (min ans copies)))
                (loop (+ i 1) ans)))))))
```

## Erlang

```erlang
-module(solution).
-export([rearrange_characters/2]).

-spec rearrange_characters(S :: unicode:unicode_binary(), Target :: unicode:unicode_binary()) -> integer().
rearrange_characters(S, Target) ->
    SCounts = count_chars(S),
    TCounts = count_chars(Target),
    compute_min(TCounts, SCounts, 101).

count_chars(Bin) ->
    count_chars(Bin, #{}).

count_chars(<<>>, Acc) ->
    Acc;
count_chars(<<C, Rest/binary>>, Acc) ->
    NewAcc = maps:update_with(C,
        fun(V) -> V + 1 end,
        1,
        Acc),
    count_chars(Rest, NewAcc).

compute_min(TMap, _SMap, 0) ->
    0;
compute_min(TMap, SMap, Min) ->
    case maps:next(TMap) of
        none ->
            Min;
        {Char, Need, Rest} ->
            Have = maps:get(Char, SMap, 0),
            if Have == 0 ->
                    0;
               true ->
                    Copies = Have div Need,
                    NewMin = case Min of
                                 101 -> Copies;
                                 _   -> erlang:min(Min, Copies)
                             end,
                    compute_min(Rest, SMap, NewMin)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec rearrange_characters(s :: String.t(), target :: String.t()) :: integer()
  def rearrange_characters(s, target) do
    freq_s = String.graphemes(s) |> Enum.frequencies()
    freq_t = String.graphemes(target) |> Enum.frequencies()

    freq_t
    |> Enum.map(fn {ch, cnt_t} -> div(Map.get(freq_s, ch, 0), cnt_t) end)
    |> Enum.min()
  end
end
```
