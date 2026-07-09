# 0076. Minimum Window Substring

## Cpp

```cpp
class Solution {
public:
    string minWindow(string s, string t) {
        if (t.empty() || s.size() < t.size()) return "";
        vector<int> need(128, 0);
        for (char c : t) ++need[c];
        int missing = t.size();
        int left = 0, start = 0, minLen = INT_MAX;
        for (int right = 0; right < (int)s.size(); ++right) {
            char c = s[right];
            if (need[c] > 0) --missing;
            --need[c];
            while (missing == 0) {
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    start = left;
                }
                char cl = s[left];
                ++need[cl];
                if (need[cl] > 0) ++missing;
                ++left;
            }
        }
        return minLen == INT_MAX ? "" : s.substr(start, minLen);
    }
};
```

## Java

```java
class Solution {
    public String minWindow(String s, String t) {
        if (s == null || t == null || s.length() < t.length()) return "";
        int[] need = new int[256];
        for (int i = 0; i < t.length(); i++) {
            need[t.charAt(i)]++;
        }
        int missing = t.length();
        int left = 0, right = 0;
        int bestStart = 0, bestLen = Integer.MAX_VALUE;

        while (right < s.length()) {
            char c = s.charAt(right);
            if (need[c] > 0) {
                missing--;
            }
            need[c]--;
            right++;

            while (missing == 0) {
                if (right - left < bestLen) {
                    bestLen = right - left;
                    bestStart = left;
                }
                char cl = s.charAt(left);
                need[cl]++;
                if (need[cl] > 0) {
                    missing++;
                }
                left++;
            }
        }

        return bestLen == Integer.MAX_VALUE ? "" : s.substring(bestStart, bestStart + bestLen);
    }
}
```

## Python

```python
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        from collections import Counter, defaultdict
        
        dict_t = Counter(t)
        required = len(dict_t)
        
        # Filter s to characters that are actually in t to potentially speed up
        filtered_s = [(i, ch) for i, ch in enumerate(s) if ch in dict_t]
        
        l, r = 0, 0
        formed = 0
        window_counts = defaultdict(int)
        ans = float("inf"), None, None  # window length, left, right
        
        while r < len(filtered_s):
            char = filtered_s[r][1]
            window_counts[char] += 1
            
            if window_counts[char] == dict_t[char]:
                formed += 1
            
            # Try and contract the window till the point it ceases to be 'desirable'.
            while l <= r and formed == required:
                start = filtered_s[l][0]
                end = filtered_s[r][0]
                
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)
                
                left_char = filtered_s[l][1]
                window_counts[left_char] -= 1
                if window_counts[left_char] < dict_t[left_char]:
                    formed -= 1
                l += 1
            
            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2]+1]
```

## Python3

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if not s or not t:
            return ""
        need = Counter(t)
        required = len(need)

        left = 0
        formed = 0
        window_counts = {}
        ans_len = float('inf')
        ans_l = ans_r = 0

        for right, ch in enumerate(s):
            window_counts[ch] = window_counts.get(ch, 0) + 1
            if ch in need and window_counts[ch] == need[ch]:
                formed += 1

            while left <= right and formed == required:
                ch_left = s[left]
                if right - left + 1 < ans_len:
                    ans_len = right - left + 1
                    ans_l, ans_r = left, right

                window_counts[ch_left] -= 1
                if ch_left in need and window_counts[ch_left] < need[ch_left]:
                    formed -= 1
                left += 1

        return "" if ans_len == float('inf') else s[ans_l:ans_r+1]
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

char* minWindow(char* s, char* t) {
    if (!s || !t) {
        char *empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    
    int need[128] = {0};
    int required = 0;
    for (int i = 0; t[i]; ++i) {
        if (need[(unsigned char)t[i]] == 0)
            required++;
        need[(unsigned char)t[i]]++;
    }
    
    int window[128] = {0};
    int formed = 0;
    int left = 0, right = 0;
    int min_len = INT_MAX, start_idx = 0;
    int s_len = strlen(s);
    
    while (right < s_len) {
        unsigned char c = (unsigned char)s[right];
        window[c]++;
        if (need[c] > 0 && window[c] == need[c])
            formed++;
        
        while (left <= right && formed == required) {
            if (right - left + 1 < min_len) {
                min_len = right - left + 1;
                start_idx = left;
            }
            unsigned char d = (unsigned char)s[left];
            window[d]--;
            if (need[d] > 0 && window[d] < need[d])
                formed--;
            left++;
        }
        right++;
    }
    
    if (min_len == INT_MAX) {
        char *empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    
    char *result = (char*)malloc(min_len + 1);
    memcpy(result, s + start_idx, min_len);
    result[min_len] = '\0';
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string MinWindow(string s, string t)
    {
        if (string.IsNullOrEmpty(s) || string.IsNullOrEmpty(t) || s.Length < t.Length)
            return "";

        int[] need = new int[128];
        foreach (char c in t)
            need[c]++;

        int requiredUnique = 0;
        for (int i = 0; i < need.Length; i++)
            if (need[i] > 0) requiredUnique++;

        int[] window = new int[128];
        int formed = 0, left = 0, right = 0;
        int minLen = int.MaxValue, startIdx = 0;

        while (right < s.Length)
        {
            char c = s[right];
            window[c]++;

            if (need[c] > 0 && window[c] == need[c])
                formed++;

            while (left <= right && formed == requiredUnique)
            {
                int len = right - left + 1;
                if (len < minLen)
                {
                    minLen = len;
                    startIdx = left;
                }

                char chLeft = s[left];
                window[chLeft]--;
                if (need[chLeft] > 0 && window[chLeft] < need[chLeft])
                    formed--;

                left++;
            }

            right++;
        }

        return minLen == int.MaxValue ? "" : s.Substring(startIdx, minLen);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    if (t.length === 0 || s.length === 0) return "";
    
    const need = new Map();
    for (let i = 0; i < t.length; ++i) {
        const c = t[i];
        need.set(c, (need.get(c) || 0) + 1);
    }
    
    let missing = t.length;
    let left = 0;
    let minLen = Infinity;
    let start = 0;
    
    for (let right = 0; right < s.length; ++right) {
        const c = s[right];
        if (need.has(c)) {
            need.set(c, need.get(c) - 1);
            if (need.get(c) >= 0) missing--;
        }
        
        while (missing === 0) {
            // update answer
            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                start = left;
            }
            
            const cl = s[left];
            if (need.has(cl)) {
                need.set(cl, need.get(cl) + 1);
                if (need.get(cl) > 0) missing++;
            }
            left++;
        }
    }
    
    return minLen === Infinity ? "" : s.substring(start, start + minLen);
};
```

## Typescript

```typescript
function minWindow(s: string, t: string): string {
    const need = new Array(128).fill(0);
    for (let i = 0; i < t.length; i++) {
        need[t.charCodeAt(i)]++;
    }
    let missing = t.length;
    let left = 0;
    let start = 0;
    let minLen = Infinity;

    for (let right = 0; right < s.length; right++) {
        const rc = s.charCodeAt(right);
        if (need[rc] > 0) missing--;
        need[rc]--;

        while (missing === 0) {
            if (right - left + 1 < minLen) {
                start = left;
                minLen = right - left + 1;
            }
            const lc = s.charCodeAt(left);
            need[lc]++;
            if (need[lc] > 0) missing++;
            left++;
        }
    }

    return minLen === Infinity ? "" : s.substring(start, start + minLen);
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param String $t
     * @return String
     */
    function minWindow($s, $t) {
        $m = strlen($s);
        $n = strlen($t);
        if ($m == 0 || $n == 0 || $n > $m) {
            return "";
        }

        // frequency of characters needed from t
        $need = array_fill(0, 128, 0);
        for ($i = 0; $i < $n; $i++) {
            $need[ord($t[$i])]++;
        }

        // number of unique chars that must be satisfied
        $required = 0;
        for ($i = 0; $i < 128; $i++) {
            if ($need[$i] > 0) {
                $required++;
            }
        }

        $window = array_fill(0, 128, 0);
        $formed = 0;
        $l = 0;
        $ansLen = PHP_INT_MAX;
        $ansStart = 0;

        for ($r = 0; $r < $m; $r++) {
            $cIdx = ord($s[$r]);
            $window[$cIdx]++;

            if ($need[$cIdx] > 0 && $window[$cIdx] == $need[$cIdx]) {
                $formed++;
            }

            while ($l <= $r && $formed == $required) {
                $currLen = $r - $l + 1;
                if ($currLen < $ansLen) {
                    $ansLen = $currLen;
                    $ansStart = $l;
                }

                $cLeftIdx = ord($s[$l]);
                $window[$cLeftIdx]--;
                if ($need[$cLeftIdx] > 0 && $window[$cLeftIdx] < $need[$cLeftIdx]) {
                    $formed--;
                }
                $l++;
            }
        }

        return $ansLen == PHP_INT_MAX ? "" : substr($s, $ansStart, $ansLen);
    }
}
```

## Swift

```swift
class Solution {
    func minWindow(_ s: String, _ t: String) -> String {
        let sBytes = Array(s.utf8)
        let tBytes = Array(t.utf8)
        if tBytes.isEmpty || sBytes.isEmpty { return "" }
        
        var needCounts = [Int](repeating: 0, count: 256)
        for b in tBytes {
            needCounts[Int(b)] += 1
        }
        var windowCounts = [Int](repeating: 0, count: 256)
        
        var need = tBytes.count          // characters still required
        var left = 0
        var minLen = Int.max
        var minStart = 0
        
        for right in 0..<sBytes.count {
            let c = Int(sBytes[right])
            windowCounts[c] += 1
            if needCounts[c] > 0 && windowCounts[c] <= needCounts[c] {
                need -= 1
            }
            
            while need == 0 {
                let currentLen = right - left + 1
                if currentLen < minLen {
                    minLen = currentLen
                    minStart = left
                }
                
                let lc = Int(sBytes[left])
                if needCounts[lc] > 0 && windowCounts[lc] <= needCounts[lc] {
                    need += 1
                }
                windowCounts[lc] -= 1
                left += 1
            }
        }
        
        if minLen == Int.max { return "" }
        let startIdx = s.index(s.startIndex, offsetBy: minStart)
        let endIdx = s.index(startIdx, offsetBy: minLen)
        return String(s[startIdx..<endIdx])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minWindow(s: String, t: String): String {
        if (s.isEmpty() || t.isEmpty()) return ""
        val need = IntArray(128)
        for (ch in t) {
            need[ch.code]++
        }
        var required = 0
        for (cnt in need) {
            if (cnt > 0) required++
        }

        val windowCounts = IntArray(128)
        var formed = 0
        var left = 0
        var right = 0

        var ansLen = Int.MAX_VALUE
        var ansL = 0
        var ansR = 0

        while (right < s.length) {
            val c = s[right]
            val idx = c.code
            windowCounts[idx]++
            if (need[idx] > 0 && windowCounts[idx] == need[idx]) {
                formed++
            }

            while (left <= right && formed == required) {
                // Update answer
                if (right - left + 1 < ansLen) {
                    ansLen = right - left + 1
                    ansL = left
                    ansR = right
                }
                val chLeft = s[left]
                val idxL = chLeft.code
                windowCounts[idxL]--
                if (need[idxL] > 0 && windowCounts[idxL] < need[idxL]) {
                    formed--
                }
                left++
            }

            right++
        }

        return if (ansLen == Int.MAX_VALUE) "" else s.substring(ansL, ansR + 1)
    }
}
```

## Dart

```dart
class Solution {
  String minWindow(String s, String t) {
    if (s.isEmpty || t.isEmpty) return "";
    const int asciiSize = 128;
    List<int> need = List.filled(asciiSize, 0);
    for (int i = 0; i < t.length; i++) {
      need[t.codeUnitAt(i)]++;
    }
    int requiredUnique = 0;
    for (int cnt in need) {
      if (cnt > 0) requiredUnique++;
    }

    List<int> have = List.filled(asciiSize, 0);
    int formed = 0;
    int left = 0;
    int minLen = s.length + 1;
    int ansStart = 0;

    for (int right = 0; right < s.length; right++) {
      int c = s.codeUnitAt(right);
      have[c]++;
      if (need[c] > 0 && have[c] == need[c]) {
        formed++;
      }

      while (formed == requiredUnique) {
        int windowLen = right - left + 1;
        if (windowLen < minLen) {
          minLen = windowLen;
          ansStart = left;
        }
        int cl = s.codeUnitAt(left);
        have[cl]--;
        if (need[cl] > 0 && have[cl] < need[cl]) {
          formed--;
        }
        left++;
      }
    }

    return minLen == s.length + 1 ? "" : s.substring(ansStart, ansStart + minLen);
  }
}
```

## Golang

```go
func minWindow(s string, t string) string {
    if len(s) == 0 || len(t) == 0 {
        return ""
    }

    var need [128]int
    for i := 0; i < len(t); i++ {
        need[t[i]]++
    }
    required := 0
    for _, v := range need {
        if v > 0 {
            required++
        }
    }

    var window [128]int
    formed, left, right := 0, 0, 0
    minLen := len(s) + 1
    start := 0

    for right < len(s) {
        c := s[right]
        window[c]++
        if need[c] > 0 && window[c] == need[c] {
            formed++
        }

        for left <= right && formed == required {
            if (right-left+1) < minLen {
                minLen = right - left + 1
                start = left
            }
            lc := s[left]
            if need[lc] > 0 && window[lc] == need[lc] {
                formed--
            }
            window[lc]--
            left++
        }

        right++
    }

    if minLen == len(s)+1 {
        return ""
    }
    return s[start : start+minLen]
}
```

## Ruby

```ruby
def min_window(s, t)
  return "" if s.empty? || t.empty?
  need = Hash.new(0)
  t.each_char { |c| need[c] += 1 }
  required = need.size

  left = 0
  right = 0
  formed = 0
  window_counts = Hash.new(0)

  ans_len = Float::INFINITY
  ans_start = 0

  while right < s.length
    c = s[right]
    window_counts[c] += 1
    if need.key?(c) && window_counts[c] == need[c]
      formed += 1
    end

    while left <= right && formed == required
      if (right - left + 1) < ans_len
        ans_len = right - left + 1
        ans_start = left
      end

      d = s[left]
      window_counts[d] -= 1
      if need.key?(d) && window_counts[d] < need[d]
        formed -= 1
      end
      left += 1
    end

    right += 1
  end

  return "" if ans_len == Float::INFINITY
  s[ans_start, ans_len]
end
```

## Scala

```scala
object Solution {
    def minWindow(s: String, t: String): String = {
        if (t.isEmpty || s.length < t.length) return ""
        val need = new Array[Int](128)
        for (ch <- t) {
            need(ch.toInt) += 1
        }
        var required = 0
        for (cnt <- need) if (cnt > 0) required += 1

        val windowCounts = new Array[Int](128)
        var formed = 0
        var left = 0
        var ansLen = Int.MaxValue
        var ansLeft = 0

        for (right <- 0 until s.length) {
            val c = s.charAt(right).toInt
            windowCounts(c) += 1
            if (need(c) > 0 && windowCounts(c) == need(c)) {
                formed += 1
            }

            while (left <= right && formed == required) {
                val windowSize = right - left + 1
                if (windowSize < ansLen) {
                    ansLen = windowSize
                    ansLeft = left
                }
                val lc = s.charAt(left).toInt
                windowCounts(lc) -= 1
                if (need(lc) > 0 && windowCounts(lc) < need(lc)) {
                    formed -= 1
                }
                left += 1
            }
        }

        if (ansLen == Int.MaxValue) "" else s.substring(ansLeft, ansLeft + ansLen)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        if s.len() < t.len() {
            return "".to_string();
        }
        let s_bytes = s.as_bytes();
        let t_bytes = t.as_bytes();

        const SIZE: usize = 256;
        let mut need = [0i32; SIZE];
        for &c in t_bytes {
            need[c as usize] += 1;
        }

        let mut required = 0usize;
        for &cnt in need.iter() {
            if cnt > 0 {
                required += 1;
            }
        }

        let mut window_counts = [0i32; SIZE];
        let mut formed = 0usize;

        let (mut left, mut right) = (0usize, 0usize);
        let mut best_len = usize::MAX;
        let mut best_start = 0usize;

        while right < s_bytes.len() {
            let c_idx = s_bytes[right] as usize;
            window_counts[c_idx] += 1;
            if need[c_idx] > 0 && window_counts[c_idx] == need[c_idx] {
                formed += 1;
            }

            while left <= right && formed == required {
                let window_len = right - left + 1;
                if window_len < best_len {
                    best_len = window_len;
                    best_start = left;
                }
                let d_idx = s_bytes[left] as usize;
                window_counts[d_idx] -= 1;
                if need[d_idx] > 0 && window_counts[d_idx] < need[d_idx] {
                    formed -= 1;
                }
                left += 1;
            }

            right += 1;
        }

        if best_len == usize::MAX {
            "".to_string()
        } else {
            s[best_start..best_start + best_len].to_string()
        }
    }
}
```

## Racket

```racket
(define/contract (min-window s t)
  (-> string? string? string?)
  (let* ([m (string-length s)]
         [n (string-length t)])
    (if (> n m) ""
        (let* ([need (make-hash)])
          ;; build need counts
          (for ([i (in-range n)])
            (let ([c (string-ref t i)])
              (hash-set! need c (+ 1 (hash-ref need c 0)))))
          (define required (hash-count need))
          (define window (make-hash))
          (define left 0)
          (define formed 0)
          (define ans (list (+ m 1) 0 0)) ; length, start, end
          (for ([right (in-range m)])
            (let* ([c (string-ref s right)]
                   [cnt (+ 1 (hash-ref window c 0))])
              (hash-set! window c cnt)
              (when (and (hash-has-key? need c)
                         (= cnt (hash-ref need c)))
                (set! formed (+ formed 1))))
            ;; try to contract the window
            (let loop ()
              (when (and (<= left right) (= formed required))
                (let* ([start left]
                       [end (+ right 1)]
                       [len (- end start)])
                  (when (< len (first ans))
                    (set! ans (list len start end))))
                (let* ([d (string-ref s left)]
                       [cnt-d (- (hash-ref window d) 1)])
                  (hash-set! window d cnt-d)
                  (when (and (hash-has-key? need d)
                             (< cnt-d (hash-ref need d)))
                    (set! formed (- formed 1))))
                (set! left (+ left 1))
                (loop)))))
          (if (= (first ans) (+ m 1))
              ""
              (substring s (second ans) (third ans)))))))
```

## Erlang

```erlang
-spec min_window(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> unicode:unicode_binary().
min_window(S, T) ->
    NeedMap = build_need_map(T),
    Required = maps:size(NeedMap),
    CharListS = binary_to_list(S),
    LenS = length(CharListS),
    CharArray = array:from_list(CharListS),
    {AnsLen, AnsStart, _} = loop(CharArray, LenS, 0, 0, NeedMap, Required, #{}, 0, {-1, 0, 0}),
    case AnsLen of
        -1 -> <<>>;
        _ -> binary:part(S, AnsStart, AnsLen)
    end.

build_need_map(T) ->
    lists:foldl(
      fun(C, Acc) ->
              case maps:is_key(C, Acc) of
                  true -> maps:update(C, maps:get(C, Acc) + 1, Acc);
                  false -> maps:put(C, 1, Acc)
              end
      end,
      #{},
      binary_to_list(T)).

loop(_Array, _LenS, R, _L, _NeedMap, _Required, _WindowCounts, _Formed, Ans) when R == _LenS ->
    Ans;
loop(Array, LenS, R, L, NeedMap, Required, WindowCounts, Formed, Ans) ->
    C = array:get(R, Array),
    {WC1, F1} = add_char(C, WindowCounts, NeedMap, Formed),
    NewR = R + 1,
    {L2, WC2, F2, Ans2} = contract(L, NewR, Array, NeedMap, Required, WC1, F1, Ans),
    loop(Array, LenS, NewR, L2, NeedMap, Required, WC2, F2, Ans2).

add_char(C, Wc, NeedMap, Formed) ->
    case maps:is_key(C, NeedMap) of
        true ->
            Count = maps:get(C, Wc, 0) + 1,
            Wc1 = maps:put(C, Count, Wc),
            Needed = maps:get(C, NeedMap),
            Formed1 = if Count == Needed -> Formed + 1; true -> Formed end,
            {Wc1, Formed1};
        false ->
            Count = maps:get(C, Wc, 0) + 1,
            {maps:put(C, Count, Wc), Formed}
    end.

remove_char(C, Wc, NeedMap, Formed) ->
    case maps:is_key(C, NeedMap) of
        true ->
            Count = maps:get(C, Wc) - 1,
            Wc1 = if Count == 0 -> maps:remove(C, Wc); true -> maps:put(C, Count, Wc) end,
            Needed = maps:get(C, NeedMap),
            Formed1 = if Count < Needed -> Formed - 1; true -> Formed end,
            {Wc1, Formed1};
        false ->
            Count = maps:get(C, Wc) - 1,
            Wc1 = if Count == 0 -> maps:remove(C, Wc); true -> maps:put(C, Count, Wc) end,
            {Wc1, Formed}
    end.

contract(L, R, Array, NeedMap, Required, WindowCounts, Formed, Ans) when Formed == Required ->
    Len = R - L,
    {BestLen, BestStart, _} = Ans,
    NewAns = case BestLen of
                 -1 -> {Len, L, R};
                 _ when Len < BestLen -> {Len, L, R};
                 _ -> Ans
             end,
    Cleft = array:get(L, Array),
    {WC2, F2} = remove_char(Cleft, WindowCounts, NeedMap, Formed),
    contract(L + 1, R, Array, NeedMap, Required, WC2, F2, NewAns);
contract(L, _R, _Array, _NeedMap, _Required, WindowCounts, Formed, Ans) ->
    {L, WindowCounts, Formed, Ans}.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_window(s :: String.t(), t :: String.t()) :: String.t()
  def min_window(s, t) do
    if byte_size(t) > byte_size(s) do
      ""
    else
      need = build_need(t)
      required = map_size(need)

      {start, len} =
        slide(
          s,
          need,
          required,
          0,
          0,
          0,
          %{},
          0,
          :infinity
        )

      if len == :infinity do
        ""
      else
        String.slice(s, start, len)
      end
    end
  end

  defp build_need(t) do
    t
    |> String.to_charlist()
    |> Enum.reduce(%{}, fn c, acc ->
      Map.update(acc, c, 1, &(&1 + 1))
    end)
  end

  defp slide(s, need, required, left, right, formed, window_counts, ans_start, ans_len) do
    len = byte_size(s)

    if right == len do
      {ans_start, ans_len}
    else
      c = :binary.at(s, right)
      wc = Map.update(window_counts, c, 1, &(&1 + 1))

      formed2 =
        if need[c] && wc == need[c] do
          formed + 1
        else
          formed
        end

      {left2, formed3, wc2, ans_start2, ans_len2} =
        shrink(
          left,
          right,
          formed2,
          wc,
          need,
          required,
          s,
          ans_start,
          ans_len
        )

      slide(s, need, required, left2, right + 1, formed3, wc2, ans_start2, ans_len2)
    end
  end

  defp shrink(left, right, formed, window_counts, need, required, s, ans_start, ans_len) do
    if formed == required do
      cur_len = right - left + 1

      {ans_start2, ans_len2} =
        if ans_len == :infinity or cur_len < ans_len do
          {left, cur_len}
        else
          {ans_start, ans_len}
        end

      c_left = :binary.at(s, left)
      wc_new = Map.update!(window_counts, c_left, &(&1 - 1))

      formed2 =
        if need[c_left] && wc_new < need[c_left] do
          formed - 1
        else
          formed
        end

      shrink(left + 1, right, formed2, wc_new, need, required, s, ans_start2, ans_len2)
    else
      {left, formed, window_counts, ans_start, ans_len}
    end
  end
end
```
