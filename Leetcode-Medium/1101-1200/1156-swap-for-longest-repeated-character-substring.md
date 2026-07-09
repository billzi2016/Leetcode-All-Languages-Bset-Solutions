# 1156. Swap For Longest Repeated Character Substring

## Cpp

```cpp
class Solution {
public:
    int maxRepOpt1(string text) {
        int n = text.size();
        vector<int> total(26, 0);
        for (char ch : text) total[ch - 'a']++;
        
        // Run-length encoding
        vector<pair<char,int>> runs;
        for (int i = 0; i < n; ) {
            char c = text[i];
            int j = i;
            while (j < n && text[j] == c) ++j;
            runs.emplace_back(c, j - i);
            i = j;
        }
        
        int ans = 0;
        // Case 1: extend a single run by swapping in one more same character
        for (auto &run : runs) {
            int idx = run.first - 'a';
            int len = run.second;
            ans = max(ans, min(len + 1, total[idx]));
        }
        
        // Case 2: merge two runs separated by a single different character
        for (int i = 1; i + 1 < (int)runs.size(); ++i) {
            if (runs[i].second == 1 && runs[i-1].first == runs[i+1].first) {
                int idx = runs[i-1].first - 'a';
                int combined = runs[i-1].second + runs[i+1].second;
                ans = max(ans, min(combined + 1, total[idx]));
            }
        }
        
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxRepOpt1(String text) {
        int n = text.length();
        int[] totalCount = new int[26];
        for (int i = 0; i < n; i++) {
            totalCount[text.charAt(i) - 'a']++;
        }

        java.util.ArrayList<Integer> lens = new java.util.ArrayList<>();
        java.util.ArrayList<Character> chars = new java.util.ArrayList<>();

        int i = 0;
        while (i < n) {
            char c = text.charAt(i);
            int j = i;
            while (j < n && text.charAt(j) == c) {
                j++;
            }
            lens.add(j - i);
            chars.add(c);
            i = j;
        }

        int m = lens.size();
        int ans = 0;

        // Extend a single block by swapping in one more same character if possible
        for (int idx = 0; idx < m; idx++) {
            char c = chars.get(idx);
            int curLen = lens.get(idx);
            int possible = Math.min(curLen + 1, totalCount[c - 'a']);
            ans = Math.max(ans, possible);
        }

        // Merge two blocks separated by a single different character
        for (int idx = 0; idx + 2 < m; idx++) {
            if (chars.get(idx) == chars.get(idx + 2) && lens.get(idx + 1) == 1) {
                char c = chars.get(idx);
                int combined = lens.get(idx) + lens.get(idx + 2);
                if (totalCount[c - 'a'] > combined) {
                    combined += 1; // we can bring another same character from elsewhere
                }
                ans = Math.max(ans, combined);
            }
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        from collections import Counter
        cnt = Counter(text)

        # Run-length encoding
        runs = []
        i, n = 0, len(text)
        while i < n:
            j = i
            while j < n and text[j] == text[i]:
                j += 1
            runs.append((text[i], j - i))
            i = j

        ans = 0
        m = len(runs)

        for idx, (ch, length) in enumerate(runs):
            # Extend current block by swapping one more same character from elsewhere
            if cnt[ch] > length:
                ans = max(ans, length + 1)
            else:
                ans = max(ans, length)

            # Merge two blocks of the same character separated by a single different char
            if idx > 0 and idx < m - 1:
                prev_ch, prev_len = runs[idx - 1]
                next_ch, next_len = runs[idx + 1]
                if length == 1 and prev_ch == next_ch:
                    combined = prev_len + next_len
                    # If there is at least one more of this character elsewhere, we can add it
                    if cnt[prev_ch] > combined:
                        combined += 1
                    ans = max(ans, combined)

        return ans
```

## Python3

```python
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        from collections import Counter
        if not text:
            return 0

        total = Counter(text)

        # Run-length encoding
        runs = []
        prev = text[0]
        cnt = 1
        for ch in text[1:]:
            if ch == prev:
                cnt += 1
            else:
                runs.append((prev, cnt))
                prev = ch
                cnt = 1
        runs.append((prev, cnt))

        ans = 0

        # Extend a single run by swapping one same character from elsewhere
        for ch, c in runs:
            ans = max(ans, min(c + 1, total[ch]))

        # Merge two runs separated by a single different character
        for i in range(1, len(runs) - 1):
            if runs[i][1] == 1 and runs[i-1][0] == runs[i+1][0]:
                ch = runs[i-1][0]
                combined = runs[i-1][1] + runs[i+1][1]
                ans = max(ans, min(combined + 1, total[ch]))

        return ans
```

## C

```c
#include <string.h>

int max(int a, int b) { return a > b ? a : b; }

int maxRepOpt1(char* text) {
    int n = strlen(text);
    if (n == 0) return 0;

    int cnt[26] = {0};
    for (int i = 0; i < n; ++i) {
        cnt[text[i] - 'a']++;
    }

    // Run‑length encoding
    char chArr[n];
    int lenArr[n];
    int groups = 0;
    for (int i = 0; i < n;) {
        char c = text[i];
        int j = i;
        while (j < n && text[j] == c) ++j;
        chArr[groups] = c;
        lenArr[groups] = j - i;
        groups++;
        i = j;
    }

    int ans = 1; // at least one character

    // Case 1: extend a single block by swapping in another same character
    for (int g = 0; g < groups; ++g) {
        char c = chArr[g];
        int total = cnt[c - 'a'];
        int curLen = lenArr[g];
        if (curLen < total) {
            ans = max(ans, curLen + 1);
        } else {
            ans = max(ans, curLen);
        }
    }

    // Case 2: merge two blocks separated by a single different character
    for (int g = 1; g + 1 < groups; ++g) {
        if (lenArr[g] == 1 && chArr[g - 1] == chArr[g + 1]) {
            char c = chArr[g - 1];
            int merged = lenArr[g - 1] + lenArr[g + 1];
            int total = cnt[c - 'a'];
            if (merged < total) {
                ans = max(ans, merged + 1);
            } else {
                ans = max(ans, merged);
            }
        }
    }

    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxRepOpt1(string text) {
        int n = text.Length;
        if (n == 0) return 0;

        int[] total = new int[26];
        foreach (char ch in text) total[ch - 'a']++;

        List<char> chars = new List<char>();
        List<int> lens = new List<int>();

        for (int i = 0; i < n;) {
            char c = text[i];
            int j = i;
            while (j < n && text[j] == c) j++;
            chars.Add(c);
            lens.Add(j - i);
            i = j;
        }

        int m = chars.Count;
        int ans = 0;

        for (int i = 0; i < m; i++) {
            char c = chars[i];
            int len = lens[i];

            // Extend current block by swapping in one more same character if possible
            int best = len;
            if (total[c - 'a'] > len) best = len + 1;
            ans = Math.Max(ans, best);

            // Merge two blocks separated by a single different character
            if (i > 0 && i + 1 < m && lens[i] == 1 && chars[i - 1] == chars[i + 1]) {
                int combined = lens[i - 1] + lens[i + 1];
                if (total[chars[i - 1] - 'a'] > combined) combined += 1;
                ans = Math.Max(ans, combined);
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} text
 * @return {number}
 */
var maxRepOpt1 = function(text) {
    const n = text.length;
    const total = new Array(26).fill(0);
    for (let i = 0; i < n; ++i) {
        total[text.charCodeAt(i) - 97]++;
    }

    let ans = 0;

    for (let ci = 0; ci < 26; ++ci) {
        const ch = String.fromCharCode(97 + ci);
        let left = 0;
        let cntC = 0;   // count of target char in window
        let cntNon = 0; // count of non-target chars in window (should be <=1)

        for (let right = 0; right < n; ++right) {
            if (text[right] === ch) cntC++;
            else cntNon++;

            while (cntNon > 1) {
                if (text[left] === ch) cntC--;
                else cntNon--;
                left++;
            }

            const windowLen = right - left + 1;
            // we can extend by one more if there is at least one extra target char outside the window
            const possible = Math.min(total[ci], windowLen + (total[ci] > cntC ? 1 : 0));
            ans = Math.max(ans, possible);
        }
    }

    return ans;
};
```

## Typescript

```typescript
function maxRepOpt1(text: string): number {
    const n = text.length;
    const total = new Array(26).fill(0);
    for (let i = 0; i < n; i++) {
        total[text.charCodeAt(i) - 97]++;
    }

    const groupsChar: string[] = [];
    const groupsLen: number[] = [];

    let i = 0;
    while (i < n) {
        const ch = text[i];
        let j = i;
        while (j < n && text[j] === ch) j++;
        groupsChar.push(ch);
        groupsLen.push(j - i);
        i = j;
    }

    let ans = 0;
    const m = groupsChar.length;

    for (let idx = 0; idx < m; idx++) {
        const chIdx = groupsChar[idx].charCodeAt(0) - 97;
        const curLen = groupsLen[idx];
        // Extend current block by swapping one more same character from elsewhere
        ans = Math.max(ans, Math.min(curLen + 1, total[chIdx]));

        // Merge two blocks separated by a single different character
        if (
            idx > 0 &&
            idx + 1 < m &&
            groupsLen[idx] === 1 &&
            groupsChar[idx - 1] === groupsChar[idx + 1]
        ) {
            const leftChIdx = groupsChar[idx - 1].charCodeAt(0) - 97;
            const mergedLen = groupsLen[idx - 1] + groupsLen[idx + 1];
            ans = Math.max(ans, Math.min(mergedLen + 1, total[leftChIdx]));
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $text
     * @return Integer
     */
    function maxRepOpt1($text) {
        $n = strlen($text);
        if ($n == 0) return 0;

        // total count of each character
        $total = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($text[$i]) - ord('a');
            $total[$idx]++;
        }

        // run-length encoding
        $runsChar = [];
        $runsLen = [];
        $prev = $text[0];
        $len = 1;
        for ($i = 1; $i < $n; $i++) {
            if ($text[$i] === $prev) {
                $len++;
            } else {
                $runsChar[] = $prev;
                $runsLen[] = $len;
                $prev = $text[$i];
                $len = 1;
            }
        }
        $runsChar[] = $prev;
        $runsLen[] = $len;

        $m = count($runsChar);
        $ans = 0;

        // case: extend a single run by swapping in one more same character
        for ($i = 0; $i < $m; $i++) {
            $cIdx = ord($runsChar[$i]) - ord('a');
            $possible = min($runsLen[$i] + 1, $total[$cIdx]);
            if ($possible > $ans) $ans = $possible;
        }

        // case: merge two runs separated by a single different character
        for ($i = 1; $i < $m - 1; $i++) {
            if ($runsLen[$i] == 1 && $runsChar[$i-1] === $runsChar[$i+1]) {
                $cIdx = ord($runsChar[$i-1]) - ord('a');
                $combined = $runsLen[$i-1] + $runsLen[$i+1];
                if ($total[$cIdx] > $combined) {
                    $combined += 1;
                }
                if ($combined > $ans) $ans = $combined;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxRepOpt1(_ text: String) -> Int {
        let chars = Array(text)
        let n = chars.count
        if n == 0 { return 0 }
        
        // total count per character
        var total = [Int](repeating: 0, count: 26)
        for ch in chars {
            let idx = Int(ch.unicodeScalars.first!.value - UnicodeScalar("a").value)
            total[idx] += 1
        }
        
        // run-length encoding
        var groupsChar: [Character] = []
        var groupsCount: [Int] = []
        var i = 0
        while i < n {
            let cur = chars[i]
            var j = i
            while j < n && chars[j] == cur { j += 1 }
            groupsChar.append(cur)
            groupsCount.append(j - i)
            i = j
        }
        
        var answer = 0
        let m = groupsChar.count
        
        // case: single group extended by one extra same character elsewhere
        for idx in 0..<m {
            let chIdx = Int(groupsChar[idx].unicodeScalars.first!.value - UnicodeScalar("a").value)
            let possible = min(groupsCount[idx] + 1, total[chIdx])
            if possible > answer { answer = possible }
        }
        
        // case: two groups separated by a single different character
        if m >= 3 {
            for idx in 0..<(m - 2) {
                if groupsChar[idx] == groupsChar[idx + 2] && groupsCount[idx + 1] == 1 {
                    let chIdx = Int(groupsChar[idx].unicodeScalars.first!.value - UnicodeScalar("a").value)
                    let combined = groupsCount[idx] + groupsCount[idx + 2]
                    let possible = min(combined + 1, total[chIdx])
                    if possible > answer { answer = possible }
                }
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
import kotlin.math.max
import kotlin.math.min

class Solution {
    fun maxRepOpt1(text: String): Int {
        val n = text.length
        if (n == 0) return 0
        val total = IntArray(26)
        for (c in text) {
            total[c - 'a']++
        }

        // Run-length encoding
        val groups = mutableListOf<Pair<Char, Int>>()
        var i = 0
        while (i < n) {
            val ch = text[i]
            var j = i
            while (j < n && text[j] == ch) j++
            groups.add(Pair(ch, j - i))
            i = j
        }

        var ans = 0

        // Case 1: extend a single block by swapping one more same character
        for ((ch, len) in groups) {
            val idx = ch - 'a'
            ans = max(ans, min(len + 1, total[idx]))
        }

        // Case 2: merge two blocks separated by a single different character
        for (k in 1 until groups.size - 1) {
            if (groups[k].second == 1 && groups[k - 1].first == groups[k + 1].first) {
                val ch = groups[k - 1].first
                val idx = ch - 'a'
                var mergedLen = groups[k - 1].second + groups[k + 1].second
                if (total[idx] > mergedLen) mergedLen += 1
                ans = max(ans, mergedLen)
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
  int maxRepOpt1(String text) {
    List<int> total = List.filled(26, 0);
    for (int c in text.codeUnits) {
      total[c - 97]++;
    }

    List<int> runChars = [];
    List<int> runLens = [];

    int n = text.length;
    int i = 0;
    while (i < n) {
      int ch = text.codeUnitAt(i) - 97;
      int j = i;
      while (j < n && text.codeUnitAt(j) - 97 == ch) {
        j++;
      }
      runChars.add(ch);
      runLens.add(j - i);
      i = j;
    }

    int ans = 0;

    for (int idx = 0; idx < runLens.length; ++idx) {
      int ch = runChars[idx];
      int len = runLens[idx];
      ans = max(ans, min(len + 1, total[ch]));
    }

    for (int idx = 0; idx + 2 < runLens.length; ++idx) {
      if (runChars[idx] == runChars[idx + 2] && runLens[idx + 1] == 1) {
        int combined = runLens[idx] + runLens[idx + 2];
        int ch = runChars[idx];
        ans = max(ans, min(combined + 1, total[ch]));
      }
    }

    return ans;
  }
}
```

## Golang

```go
func maxRepOpt1(text string) int {
    n := len(text)
    if n == 0 {
        return 0
    }
    // total count of each character
    cnt := [26]int{}
    for i := 0; i < n; i++ {
        cnt[text[i]-'a']++
    }

    // run-length encoding
    var chars []byte
    var lens []int
    for i := 0; i < n; {
        j := i + 1
        for j < n && text[j] == text[i] {
            j++
        }
        chars = append(chars, text[i])
        lens = append(lens, j-i)
        i = j
    }

    ans := 1
    // case: extend a single block by swapping in one more same character
    for idx, c := range chars {
        l := lens[idx]
        total := cnt[c-'a']
        possible := l + 1
        if possible > total {
            possible = total
        }
        if possible > ans {
            ans = possible
        }
    }

    // case: merge two blocks separated by a single different character
    for i := 0; i+2 < len(chars); i++ {
        if chars[i] == chars[i+2] && lens[i+1] == 1 {
            combined := lens[i] + lens[i+2]
            total := cnt[chars[i]-'a']
            possible := combined
            if total > combined { // we can bring one more from elsewhere
                possible = combined + 1
            }
            if possible > ans {
                ans = possible
            }
        }
    }

    return ans
}
```

## Ruby

```ruby
def max_rep_opt1(text)
  # Count total occurrences of each character
  total = Hash.new(0)
  text.each_char { |ch| total[ch] += 1 }

  # Run-length encoding: chars and their consecutive lengths
  chars = []
  lens = []
  i = 0
  n = text.length
  while i < n
    j = i
    while j < n && text[j] == text[i]
      j += 1
    end
    chars << text[i]
    lens << (j - i)
    i = j
  end

  max_len = 0
  m = lens.size

  # Case 1: extend a single block by swapping in another same character if available
  (0...m).each do |idx|
    c = chars[idx]
    cur = lens[idx]
    possible = cur + (total[c] > cur ? 1 : 0)
    max_len = possible if possible > max_len
  end

  # Case 2: merge two blocks separated by a single different character
  (0...m - 2).each do |idx|
    next unless chars[idx] == chars[idx + 2] && lens[idx + 1] == 1
    c = chars[idx]
    combined = lens[idx] + lens[idx + 2]
    possible = combined + (total[c] > combined ? 1 : 0)
    max_len = possible if possible > max_len
  end

  max_len
end
```

## Scala

```scala
object Solution {
  def maxRepOpt1(text: String): Int = {
    val n = text.length
    if (n == 0) return 0

    // total count of each character
    val total = new Array[Int](26)
    for (ch <- text) {
      total(ch - 'a') += 1
    }

    // run-length encoding
    val chars = scala.collection.mutable.ArrayBuffer[Int]()
    val lens = scala.collection.mutable.ArrayBuffer[Int]()

    var i = 0
    while (i < n) {
      val start = i
      val idx = text.charAt(i) - 'a'
      while (i < n && text.charAt(i) == text.charAt(start)) i += 1
      chars += idx
      lens += (i - start)
    }

    var ans = 0
    val m = chars.length

    for (j <- 0 until m) {
      val c = chars(j)
      val len = lens(j)

      // Extend current block by swapping in one more same character if possible
      ans = math.max(ans, math.min(total(c), len + 1))

      // Merge two blocks separated by a single different character
      if (j > 0 && j < m - 1 && lens(j) == 1 && chars(j - 1) == chars(j + 1)) {
        val c2 = chars(j - 1)
        val combined = lens(j - 1) + lens(j + 1)
        ans = math.max(ans, math.min(total(c2), combined + 1))
      }
    }

    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_rep_opt1(text: String) -> i32 {
        let bytes = text.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return 0;
        }
        // frequency of each character
        let mut freq = [0usize; 26];
        for &b in bytes.iter() {
            freq[(b - b'a') as usize] += 1;
        }

        // run-length encoding: vector of (char_byte, length)
        let mut groups: Vec<(u8, usize)> = Vec::new();
        let mut i = 0;
        while i < n {
            let cur = bytes[i];
            let mut j = i + 1;
            while j < n && bytes[j] == cur {
                j += 1;
            }
            groups.push((cur, j - i));
            i = j;
        }

        let mut ans: usize = 0;

        // case 1: extend a single group by swapping in one more same character
        for &(c, len) in &groups {
            let total = freq[(c - b'a') as usize];
            let possible = std::cmp::min(len + 1, total);
            if possible > ans {
                ans = possible;
            }
        }

        // case 2: merge two groups separated by a single different character
        for i in 0..groups.len() {
            if i + 2 >= groups.len() {
                continue;
            }
            let (c1, len1) = groups[i];
            let (mid_c, mid_len) = groups[i + 1];
            let (c2, len2) = groups[i + 2];
            if c1 == c2 && mid_len == 1 {
                let combined = len1 + len2;
                let total = freq[(c1 - b'a') as usize];
                let possible = if total > combined { combined + 1 } else { combined };
                if possible > ans {
                    ans = possible;
                }
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (max-rep-opt1 text)
  (-> string? exact-integer?)
  (let* ((n (string-length text))
         (counts (make-vector 26 0)))
    ;; total count of each character
    (for ([i (in-range n)])
      (let* ((c (string-ref text i))
             (idx (- (char->integer c) (char->integer #\a))))
        (vector-set! counts idx (+ (vector-ref counts idx) 1))))
    (define ans 0)
    (for ([t (in-range 26)])
      (let ((total (vector-ref counts t)))
        (when (> total 0)
          (let ((left 0)
                (otherCount 0)
                (maxlen 0))
            (for ([right (in-range n)])
              (define c (string-ref text right))
              (define idx (- (char->integer c) (char->integer #\a)))
              (when (not (= idx t))
                (set! otherCount (+ otherCount 1)))
              ;; shrink window while more than one non‑target character
              (let loop ((l left) (oc otherCount))
                (if (<= oc 1)
                    (begin
                      (set! left l)
                      (set! otherCount oc))
                    (let* ((cl (string-ref text l))
                           (idxl (- (char->integer cl) (char->integer #\a))))
                      (loop (+ l 1) (if (= idxl t) oc (- oc 1))))))
              (define curSize (+ (- right left) 1))
              (when (> curSize total)
                (set! curSize total))
              (when (> curSize maxlen)
                (set! maxlen curSize)))
            (set! ans (max ans maxlen)))))
    ans)))
```

## Erlang

```erlang
-spec max_rep_opt1(Text :: unicode:unicode_binary()) -> integer().
max_rep_opt1(Text) ->
    CharList = binary_to_list(Text),
    Counts = lists:foldl(fun(Char, Acc) ->
        maps:update_with(Char, fun(V) -> V + 1 end, 1, Acc)
    end, #{}, CharList),

    Runs = case CharList of
        [] -> [];
        [H | T] -> build_runs(T, H, 1, [])
    end,

    MaxSingle = lists:foldl(fun({C, L}, MaxAcc) ->
        Total = maps:get(C, Counts),
        Cand = erlang:min(Total, L + 1),
        if Cand > MaxAcc -> Cand; true -> MaxAcc end
    end, 0, Runs),

    MaxMerge = merge_case(Runs, Counts, 0),

    erlang:max(MaxSingle, MaxMerge).

build_runs([], CurrChar, CurrLen, Acc) ->
    lists:reverse([{CurrChar, CurrLen} | Acc]);
build_runs([H | T], CurrChar, CurrLen, Acc) when H =:= CurrChar ->
    build_runs(T, CurrChar, CurrLen + 1, Acc);
build_runs([H | T], CurrChar, CurrLen, Acc) ->
    build_runs(T, H, 1, [{CurrChar, CurrLen} | Acc]).

merge_case([], _Counts, Max) -> Max;
merge_case([_], _Counts, Max) -> Max;
merge_case([_, _], _Counts, Max) -> Max;
merge_case([Run1, Run2, Run3 | Rest], Counts, Max) ->
    case {Run1, Run2, Run3} of
        {{C, L1}, {_MidChar, 1}, {C, L3}} ->
            Total = maps:get(C, Counts),
            Combined = L1 + L3,
            Cand = if Total > Combined -> Combined + 1; true -> Combined end,
            NewMax = erlang:max(Max, Cand),
            merge_case([Run2, Run3 | Rest], Counts, NewMax);
        _ ->
            merge_case([Run2, Run3 | Rest], Counts, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_rep_opt1(text :: String.t()) :: integer
  def max_rep_opt1(text) do
    chars = String.graphemes(text)

    # Total count of each character
    total_counts =
      Enum.reduce(chars, %{}, fn ch, acc ->
        Map.update(acc, ch, 1, &(&1 + 1))
      end)

    # Run-length encoding: list of {char, count}
    {runs_rev, prev, cnt} =
      Enum.reduce(chars, {[], nil, 0}, fn ch, {list, prev_char, cur_cnt} ->
        if ch == prev_char do
          {list, prev_char, cur_cnt + 1}
        else
          new_list = if prev_char != nil, do: [{prev_char, cur_cnt} | list], else: list
          {new_list, ch, 1}
        end
      end)

    runs =
      case prev do
        nil -> []
        _ -> Enum.reverse([{prev, cnt} | runs_rev])
      end

    # Initial answer considering extending a single block by one swap
    max_len =
      Enum.reduce(runs, 0, fn {ch, cnt}, acc ->
        total = Map.get(total_counts, ch)
        cand = min(cnt + 1, total)
        if cand > acc, do: cand, else: acc
      end)

    run_len = length(runs)

    # Consider merging two blocks separated by a single different character
    max_len =
      Enum.with_index(runs)
      |> Enum.reduce(max_len, fn {{ch, cnt}, i}, acc ->
        if i + 2 < run_len do
          {mid_ch, mid_cnt} = Enum.at(runs, i + 1)
          {next_ch, next_cnt} = Enum.at(runs, i + 2)

          if ch == next_ch and mid_cnt == 1 do
            total = Map.get(total_counts, ch)
            cand = min(cnt + next_cnt + 1, total)
            if cand > acc, do: cand, else: acc
          else
            acc
          end
        else
          acc
        end
      end)

    max_len
  end
end
```
