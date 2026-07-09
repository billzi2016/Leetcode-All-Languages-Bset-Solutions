# 0522. Longest Uncommon Subsequence II

## Cpp

```cpp
class Solution {
public:
    bool isSubsequence(const string& a, const string& b) {
        int i = 0, j = 0;
        while (i < (int)a.size() && j < (int)b.size()) {
            if (a[i] == b[j]) ++i;
            ++j;
        }
        return i == (int)a.size();
    }

    int findLUSlength(vector<string>& strs) {
        int n = strs.size();
        int ans = -1;
        for (int i = 0; i < n; ++i) {
            bool uncommon = true;
            for (int j = 0; j < n; ++j) {
                if (i == j) continue;
                if (isSubsequence(strs[i], strs[j])) {
                    uncommon = false;
                    break;
                }
            }
            if (uncommon) {
                ans = max(ans, (int)strs[i].size());
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int findLUSlength(String[] strs) {
        Arrays.sort(strs, (a, b) -> b.length() - a.length());
        for (int i = 0; i < strs.length; i++) {
            boolean uncommon = true;
            for (int j = 0; j < strs.length; j++) {
                if (i == j) continue;
                if (isSubsequence(strs[i], strs[j])) {
                    uncommon = false;
                    break;
                }
            }
            if (uncommon) return strs[i].length();
        }
        return -1;
    }

    private boolean isSubsequence(String a, String b) {
        int i = 0, j = 0;
        while (i < a.length() && j < b.length()) {
            if (a.charAt(i) == b.charAt(j)) i++;
            j++;
        }
        return i == a.length();
    }
}
```

## Python

```python
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        from collections import Counter

        freq = Counter(strs)

        def is_subseq(a, b):
            # check if a is a subsequence of b
            it = iter(b)
            return all(ch in it for ch in a)

        ans = -1
        n = len(strs)
        for i, s in enumerate(strs):
            if freq[s] > 1:
                continue
            uncommon = True
            for j, t in enumerate(strs):
                if i == j:
                    continue
                if len(t) < len(s):
                    continue
                if is_subseq(s, t):
                    uncommon = False
                    break
            if uncommon:
                ans = max(ans, len(s))
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(a: str, b: str) -> bool:
            # return True if a is subsequence of b
            i = 0
            for ch in b:
                if i < len(a) and a[i] == ch:
                    i += 1
                if i == len(a):
                    break
            return i == len(a)

        freq = {}
        for s in strs:
            freq[s] = freq.get(s, 0) + 1

        ans = -1
        n = len(strs)
        for i in range(n):
            s = strs[i]
            if freq[s] > 1:
                continue
            uncommon = True
            for j in range(n):
                if i == j:
                    continue
                if is_subseq(s, strs[j]):
                    uncommon = False
                    break
            if uncommon:
                ans = max(ans, len(s))
        return ans
```

## C

```c
#include <string.h>
#include <stdbool.h>

static bool isSubseq(const char *a, const char *b) {
    while (*a && *b) {
        if (*a == *b) a++;
        b++;
    }
    return *a == '\0';
}

int findLUSlength(char** strs, int strsSize) {
    int ans = -1;
    for (int i = 0; i < strsSize; ++i) {
        bool uncommon = true;
        for (int j = 0; j < strsSize; ++j) {
            if (i == j) continue;
            if (isSubseq(strs[i], strs[j])) {
                uncommon = false;
                break;
            }
        }
        if (uncommon) {
            int len = strlen(strs[i]);
            if (len > ans) ans = len;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int FindLUSlength(string[] strs) {
        int n = strs.Length;
        int best = -1;
        for (int i = 0; i < n; i++) {
            bool isUncommon = true;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (IsSubsequence(strs[i], strs[j])) {
                    isUncommon = false;
                    break;
                }
            }
            if (isUncommon) {
                best = Math.Max(best, strs[i].Length);
            }
        }
        return best;
    }

    private bool IsSubsequence(string a, string b) {
        int i = 0, j = 0;
        while (i < a.Length && j < b.Length) {
            if (a[i] == b[j]) i++;
            j++;
        }
        return i == a.Length;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} strs
 * @return {number}
 */
var findLUSlength = function(strs) {
    // Sort strings by descending length
    strs.sort((a, b) => b.length - a.length);
    
    const isSubseq = (sub, str) => {
        let i = 0, j = 0;
        while (i < sub.length && j < str.length) {
            if (sub[i] === str[j]) i++;
            j++;
        }
        return i === sub.length;
    };
    
    const n = strs.length;
    for (let i = 0; i < n; i++) {
        let candidate = strs[i];
        let uncommon = true;
        for (let j = 0; j < n; j++) {
            if (i === j) continue;
            if (isSubseq(candidate, strs[j])) {
                uncommon = false;
                break;
            }
        }
        if (uncommon) return candidate.length;
    }
    return -1;
};
```

## Typescript

```typescript
function findLUSlength(strs: string[]): number {
    const isSubseq = (a: string, b: string): boolean => {
        let i = 0, j = 0;
        while (i < a.length && j < b.length) {
            if (a[i] === b[j]) i++;
            j++;
        }
        return i === a.length;
    };

    let ans = -1;
    const n = strs.length;

    for (let i = 0; i < n; ++i) {
        let uncommon = true;
        for (let j = 0; j < n; ++j) {
            if (i === j) continue;
            if (isSubseq(strs[i], strs[j])) {
                uncommon = false;
                break;
            }
        }
        if (uncommon) {
            ans = Math.max(ans, strs[i].length);
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $strs
     * @return Integer
     */
    function findLUSlength($strs) {
        // Count occurrences of each string
        $cnt = [];
        foreach ($strs as $s) {
            if (!isset($cnt[$s])) $cnt[$s] = 0;
            $cnt[$s]++;
        }

        // Sort strings by length descending
        usort($strs, function($a, $b) {
            return strlen($b) - strlen($a);
        });

        $n = count($strs);
        for ($i = 0; $i < $n; $i++) {
            $s = $strs[$i];
            if ($cnt[$s] != 1) continue; // duplicates can't be uncommon

            $isUncommon = true;
            for ($j = 0; $j < $n; $j++) {
                if ($i == $j) continue;
                if ($this->isSubsequence($s, $strs[$j])) {
                    $isUncommon = false;
                    break;
                }
            }

            if ($isUncommon) {
                return strlen($s);
            }
        }

        return -1;
    }

    private function isSubsequence(string $a, string $b): bool {
        $i = 0; $j = 0;
        $lenA = strlen($a);
        $lenB = strlen($b);
        while ($i < $lenA && $j < $lenB) {
            if ($a[$i] === $b[$j]) {
                $i++;
            }
            $j++;
        }
        return $i === $lenA;
    }
}
```

## Swift

```swift
class Solution {
    func findLUSlength(_ strs: [String]) -> Int {
        var freq = [String:Int]()
        for s in strs {
            freq[s, default: 0] += 1
        }
        let sorted = strs.sorted { $0.count > $1.count }
        for s in sorted {
            var uncommon = true
            for t in strs {
                if s == t {
                    if freq[s]! > 1 {
                        uncommon = false
                        break
                    } else {
                        continue
                    }
                }
                if isSubsequence(s, t) {
                    uncommon = false
                    break
                }
            }
            if uncommon {
                return s.count
            }
        }
        return -1
    }

    private func isSubsequence(_ a: String, _ b: String) -> Bool {
        var i = a.startIndex
        var j = b.startIndex
        while i != a.endIndex && j != b.endIndex {
            if a[i] == b[j] {
                i = a.index(after: i)
            }
            j = b.index(after: j)
        }
        return i == a.endIndex
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findLUSlength(strs: Array<String>): Int {
        val count = mutableMapOf<String, Int>()
        for (s in strs) {
            count[s] = (count[s] ?: 0) + 1
        }
        var ans = -1
        outer@ for (i in strs.indices) {
            val s = strs[i]
            if (count[s]!! > 1) continue
            for (j in strs.indices) {
                if (i == j) continue
                if (isSubsequence(s, strs[j])) {
                    continue@outer
                }
            }
            ans = maxOf(ans, s.length)
        }
        return ans
    }

    private fun isSubsequence(a: String, b: String): Boolean {
        var idx = 0
        for (ch in b) {
            if (idx < a.length && ch == a[idx]) {
                idx++
            }
        }
        return idx == a.length
    }
}
```

## Dart

```dart
class Solution {
  int findLUSlength(List<String> strs) {
    int n = strs.length;
    int ans = -1;
    for (int i = 0; i < n; i++) {
      bool uncommon = true;
      for (int j = 0; j < n; j++) {
        if (i == j) continue;
        if (_isSubsequence(strs[i], strs[j])) {
          uncommon = false;
          break;
        }
      }
      if (uncommon && strs[i].length > ans) {
        ans = strs[i].length;
      }
    }
    return ans;
  }

  bool _isSubsequence(String a, String b) {
    int i = 0, j = 0;
    while (i < a.length && j < b.length) {
      if (a.codeUnitAt(i) == b.codeUnitAt(j)) i++;
      j++;
    }
    return i == a.length;
  }
}
```

## Golang

```go
import "sort"

func findLUSlength(strs []string) int {
    sort.Slice(strs, func(i, j int) bool {
        return len(strs[i]) > len(strs[j])
    })
    for i, s := range strs {
        uncommon := true
        for j, t := range strs {
            if i == j {
                continue
            }
            if isSubseq(s, t) {
                uncommon = false
                break
            }
        }
        if uncommon {
            return len(s)
        }
    }
    return -1
}

func isSubseq(a, b string) bool {
    i := 0
    for k := 0; k < len(b) && i < len(a); k++ {
        if a[i] == b[k] {
            i++
        }
    }
    return i == len(a)
}
```

## Ruby

```ruby
def subseq?(a, b)
  i = 0
  j = 0
  while i < a.length && j < b.length
    i += 1 if a[i] == b[j]
    j += 1
  end
  i == a.length
end

# @param {String[]} strs
# @return {Integer}
def find_lu_slength(strs)
  pairs = strs.each_with_index.map { |s, idx| [s, idx] }
  pairs.sort_by! { |pair| -pair[0].length }

  pairs.each do |s, i|
    uncommon = true
    strs.each_with_index do |t, j|
      next if i == j
      if subseq?(s, t)
        uncommon = false
        break
      end
    end
    return s.length if uncommon
  end
  -1
end
```

## Scala

```scala
object Solution {
    def findLUSlength(strs: Array[String]): Int = {
        def isSubseq(a: String, b: String): Boolean = {
            var i = 0
            var j = 0
            while (i < a.length && j < b.length) {
                if (a.charAt(i) == b.charAt(j)) i += 1
                j += 1
            }
            i == a.length
        }

        val freq = strs.groupBy(identity).view.mapValues(_.length).toMap
        var ans = -1

        for (i <- strs.indices) {
            val s = strs(i)
            if (freq(s) == 1) {
                var uncommon = true
                var j = 0
                while (j < strs.length && uncommon) {
                    if (j != i && isSubseq(s, strs(j))) {
                        uncommon = false
                    }
                    j += 1
                }
                if (uncommon) ans = math.max(ans, s.length)
            }
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_lu_slength(strs: Vec<String>) -> i32 {
        let n = strs.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by(|&i, &j| strs[j].len().cmp(&strs[i].len()));
        for &i in &idx {
            let s = &strs[i];
            let mut uncommon = true;
            for j in 0..n {
                if i == j {
                    continue;
                }
                if Self::is_subsequence(s, &strs[j]) {
                    uncommon = false;
                    break;
                }
            }
            if uncommon {
                return s.len() as i32;
            }
        }
        -1
    }

    fn is_subsequence(a: &String, b: &String) -> bool {
        let a_bytes = a.as_bytes();
        let mut pos = 0usize;
        for &c in b.as_bytes() {
            if pos < a_bytes.len() && a_bytes[pos] == c {
                pos += 1;
                if pos == a_bytes.len() {
                    return true;
                }
            }
        }
        pos == a_bytes.len()
    }
}
```

## Racket

```racket
(define/contract (find-lu-slength strs)
  (-> (listof string?) exact-integer?)
  (let* ((vec (list->vector strs))
         (n   (vector-length vec))
         (idxs
           (sort (for/list ([i (in-range n)]) i)
                 > #:key (lambda (i) (string-length (vector-ref vec i))))))
    (define (is-subseq? a b)
      (let loop ((ia 0) (ib 0)
                 (la (string-length a))
                 (lb (string-length b)))
        (cond
          [(= ia la) #t]
          [(= ib lb) #f]
          [else (if (char=? (string-ref a ia) (string-ref b ib))
                    (loop (+ ia 1) (+ ib 1) la lb)
                    (loop ia (+ ib 1) la lb))])))
    (let ((ans
            (for/first ([i idxs]
                        #:when (let* ((s (vector-ref vec i))
                                      (ok (for/and ([j (in-range n)])
                                            (or (= j i)
                                                (not (is-subseq? s (vector-ref vec j)))))))
                                 ok))
              (string-length (vector-ref vec i)))))
      (if (void? ans) -1 ans))))
```

## Erlang

```erlang
-spec find_lu_slength(Strs :: [unicode:unicode_binary()]) -> integer().
find_lu_slength(Strs) ->
    Indexed = lists:zip(lists:seq(1, length(Strs)), Strs),
    find_max(Indexed, -1, Indexed).

find_max([], CurMax, _All) -> CurMax;
find_max([{Idx, S} | Rest], CurMax, All) ->
    LenS = byte_size(S),
    NewCur =
        if is_uncommon(Idx, S, All), LenS > CurMax ->
                LenS;
           true -> CurMax
        end,
    find_max(Rest, NewCur, All).

is_uncommon(Idx, S, List) ->
    not lists:any(fun({J, T}) -> J =/= Idx andalso is_subseq(S, T) end, List).

is_subseq(Sub, Str) ->
    subseq_check(binary_to_list(Sub), binary_to_list(Str)).

subseq_check([], _) -> true;
subseq_check(_, []) -> false;
subseq_check([H | T1], [H | T2]) -> subseq_check(T1, T2);
subseq_check([H | T1], [_ | T2]) -> subseq_check([H | T1], T2).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_lu_slength(strs :: [String.t]) :: integer
  def find_lu_slength(strs) do
    sorted = Enum.sort_by(strs, &String.length/1, :desc)

    Enum.reduce_while(sorted, -1, fn s, _acc ->
      if uncommon?(s, strs) do
        {:halt, String.length(s)}
      else
        {:cont, -1}
      end
    end)
  end

  defp uncommon?(s, list) do
    occ = Enum.count(list, fn x -> x == s end)

    if occ > 1 do
      false
    else
      Enum.all?(list, fn t ->
        t == s or not subseq?(s, t)
      end)
    end
  end

  defp subseq?(a, b) do
    a_len = String.length(a)
    b_len = String.length(b)

    if a_len > b_len, do: false, else: subseq_loop(String.graphemes(a), String.graphemes(b))
  end

  defp subseq_loop([], _), do: true
  defp subseq_loop(_, []), do: false
  defp subseq_loop([ah | at], [bh | bt]) do
    if ah == bh do
      subseq_loop(at, bt)
    else
      subseq_loop([ah | at], bt)
    end
  end
end
```
