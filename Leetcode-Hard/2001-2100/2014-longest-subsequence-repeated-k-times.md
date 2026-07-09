# 2014. Longest Subsequence Repeated k Times

## Cpp

```cpp
class Solution {
public:
    string longestSubsequenceRepeatedK(string s, int k) {
        int n = s.size();
        vector<int> freq(26, 0);
        for (char ch : s) freq[ch - 'a']++;
        // characters that can appear at least once in the answer
        vector<char> cand;
        for (int c = 25; c >= 0; --c) {
            if (freq[c] >= k) cand.push_back('a' + c);
        }
        int maxLen = n / k;
        string best = "";
        // helper to check if t repeated k times is a subsequence of s
        auto can = [&](const string& t)->bool{
            if (t.empty()) return true;
            int i = 0, j = 0, cnt = 0;
            while (i < n && cnt < k) {
                if (s[i] == t[j]) {
                    ++j;
                    if (j == (int)t.size()) {
                        ++cnt;
                        j = 0;
                    }
                }
                ++i;
            }
            return cnt == k;
        };
        function<void(const string&)> dfs = [&](const string& cur) {
            if ((int)cur.size() > (int)best.size() ||
               ((int)cur.size() == (int)best.size() && cur > best)) {
                best = cur;
            }
            if ((int)cur.size() == maxLen) return;
            for (char c : cand) {
                string nxt = cur;
                nxt.push_back(c);
                if (can(nxt)) dfs(nxt);
            }
        };
        dfs("");
        return best;
    }
};
```

## Java

```java
class Solution {
    private String s;
    private int k;
    private String best;

    public String longestSubsequenceRepeatedK(String s, int k) {
        this.s = s;
        this.k = k;
        int[] freq = new int[26];
        for (char ch : s.toCharArray()) freq[ch - 'a']++;
        int[] rem = new int[26];
        boolean possible = false;
        for (int i = 0; i < 26; i++) {
            rem[i] = freq[i] / k;
            if (rem[i] > 0) possible = true;
        }
        if (!possible) return "";
        best = "";
        dfs(new StringBuilder(), rem);
        return best;
    }

    private void dfs(StringBuilder cur, int[] rem) {
        // prune if even using all remaining chars cannot beat current best
        int remainingTotal = 0;
        for (int v : rem) remainingTotal += v;
        if (cur.length() + remainingTotal < best.length()) return;

        for (int c = 25; c >= 0; --c) {
            if (rem[c] == 0) continue;
            cur.append((char) ('a' + c));
            rem[c]--;
            if (isValid(cur)) {
                String cand = cur.toString();
                if (cand.length() > best.length() ||
                    (cand.length() == best.length() && cand.compareTo(best) > 0)) {
                    best = cand;
                }
                dfs(cur, rem);
            }
            // backtrack
            rem[c]++;
            cur.deleteCharAt(cur.length() - 1);
        }
    }

    private boolean isValid(StringBuilder sb) {
        String t = sb.toString();
        int pos = 0, cnt = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == t.charAt(pos)) {
                pos++;
                if (pos == t.length()) {
                    cnt++;
                    if (cnt == k) return true;
                    pos = 0;
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
    def longestSubsequenceRepeatedK(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)

        def can(t):
            # check if t repeated k times is a subsequence of s
            need = len(t) * k
            j = 0
            for ch in s:
                if j < need and ch == t[j % len(t)]:
                    j += 1
                    if j == need:
                        return True
            return j == need

        ans = ""
        while True:
            added = False
            # try characters from 'z' down to 'a'
            for c in reversed("abcdefghijklmnopqrstuvwxyz"):
                cand = ans + c
                if can(cand):
                    ans = cand
                    added = True
                    break
            if not added:
                break
        return ans
```

## Python3

```python
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        from collections import Counter

        n = len(s)
        max_len_possible = n // k
        freq = Counter(s)

        # characters that appear at least k times, in descending order
        chars = [c for c in map(chr, range(ord('z'), ord('a') - 1, -1)) if freq[c] >= k]

        best = ""

        def ok(t: str) -> bool:
            need = len(t) * k
            idx = 0
            lt = len(t)
            for ch in s:
                if ch == t[idx % lt]:
                    idx += 1
                    if idx == need:
                        return True
            return False

        def dfs(cur: str):
            nonlocal best
            # prune by maximum possible length
            if len(cur) > max_len_possible:
                return
            # update answer
            if len(cur) > len(best) or (len(cur) == len(best) and cur > best):
                best = cur
            # try to extend
            for c in chars:
                nxt = cur + c
                if len(nxt) > max_len_possible:
                    continue
                if ok(nxt):
                    dfs(nxt)

        dfs("")
        return best
```

## C

```c
#include <stdlib.h>
#include <string.h>

static const char *S;
static int K;
static int MAXLEN;

static bool canRepeat(const char *t, int len) {
    int i = 0, cnt = 0;
    for (int p = 0; S[p]; ++p) {
        if (S[p] == t[i]) {
            ++i;
            if (i == len) {
                ++cnt;
                if (cnt == K) return true;
                i = 0;
            }
        }
    }
    return false;
}

static char cur[8];
static char bestAns[8];
static int bestLen;
static int limit[26];

static void dfs(int curLen) {
    if (curLen > bestLen || (curLen == bestLen && strcmp(cur, bestAns) > 0)) {
        memcpy(bestAns, cur, curLen);
        bestAns[curLen] = '\0';
        bestLen = curLen;
    }
    if (curLen == MAXLEN) return;

    for (int c = 25; c >= 0; --c) {
        if (!limit[c]) continue;
        cur[curLen] = 'a' + c;
        cur[curLen + 1] = '\0';
        limit[c]--;
        if (canRepeat(cur, curLen + 1)) dfs(curLen + 1);
        limit[c]++;
    }
}

char* longestSubsequenceRepeatedK(char* s, int k) {
    S = s;
    K = k;
    int n = strlen(s);
    MAXLEN = n / k;

    int freq[26] = {0};
    for (int i = 0; s[i]; ++i) freq[s[i] - 'a']++;

    for (int i = 0; i < 26; ++i) limit[i] = freq[i] / k;

    bestLen = 0;
    bestAns[0] = '\0';
    cur[0] = '\0';

    dfs(0);

    char *res = (char*)malloc(bestLen + 1);
    memcpy(res, bestAns, bestLen + 1);
    return res;
}
```

## Csharp

```csharp
using System;
using System.Text;

public class Solution {
    public string LongestSubsequenceRepeatedK(string s, int k) {
        int n = s.Length;
        int maxLen = n / k;
        if (maxLen == 0) return "";
        
        int[] freq = new int[26];
        foreach (char ch in s) freq[ch - 'a']++;
        
        // Collect characters that appear at least k times
        var allowedList = new System.Collections.Generic.List<char>();
        for (int i = 25; i >= 0; i--) {
            if (freq[i] >= k) allowedList.Add((char)('a' + i));
        }
        char[] allowed = allowedList.ToArray();
        if (allowed.Length == 0) return "";
        
        int[] cntInT = new int[26];
        string best = "";
        StringBuilder sb = new StringBuilder();
        
        bool IsValid(string t) {
            if (t.Length == 0) return true;
            int pos = 0, reps = 0;
            foreach (char ch in s) {
                if (ch == t[pos]) {
                    pos++;
                    if (pos == t.Length) {
                        reps++;
                        if (reps == k) return true;
                        pos = 0;
                    }
                }
            }
            return false;
        }
        
        void Dfs() {
            // Evaluate current candidate
            string cur = sb.ToString();
            if (cur.Length > 0 && IsValid(cur)) {
                if (cur.Length > best.Length ||
                    (cur.Length == best.Length && String.CompareOrdinal(cur, best) > 0)) {
                    best = cur;
                }
            }
            // Stop if reached maximum possible length
            if (sb.Length == maxLen) return;
            
            foreach (char c in allowed) {
                int idx = c - 'a';
                // Ensure total usage after k repetitions does not exceed frequency
                if ((cntInT[idx] + 1) * k <= freq[idx]) {
                    cntInT[idx]++;
                    sb.Append(c);
                    Dfs();
                    sb.Length--;
                    cntInT[idx]--;
                }
            }
        }
        
        Dfs();
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var longestSubsequenceRepeatedK = function(s, k) {
    const n = s.length;
    const maxLen = Math.floor(n / k);
    // frequency of each character
    const freq = new Array(26).fill(0);
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    // characters that appear at least k times, sorted descending
    const chars = [];
    for (let i = 25; i >= 0; --i) {
        if (freq[i] >= k) chars.push(String.fromCharCode(97 + i));
    }

    let best = "";

    // check whether t repeated k times is a subsequence of s
    const canRepeat = (t) => {
        const need = t.length * k;
        let idx = 0;
        for (const ch of s) {
            if (ch === t[idx % t.length]) {
                idx++;
                if (idx === need) break;
            }
        }
        return idx === need;
    };

    const dfs = (cur) => {
        // update best answer
        if (
            cur.length > best.length ||
            (cur.length === best.length && cur > best)
        ) {
            best = cur;
        }
        if (cur.length === maxLen) return; // cannot get longer

        for (const c of chars) {
            const nxt = cur + c;
            if (nxt.length > maxLen) continue;
            if (canRepeat(nxt)) {
                dfs(nxt);
            }
        }
    };

    dfs("");
    return best;
};
```

## Typescript

```typescript
function longestSubsequenceRepeatedK(s: string, k: number): string {
    const n = s.length;
    const freq = new Array(26).fill(0);
    for (const ch of s) freq[ch.charCodeAt(0) - 97]++;

    // maximum times a character can appear in one copy of the answer
    const limit = freq.map(cnt => Math.floor(cnt / k));
    const candidates: number[] = [];
    for (let i = 25; i >= 0; --i) {
        if (limit[i] > 0) candidates.push(i);
    }

    const maxLen = Math.floor(n / k);
    let best = "";

    // check whether t repeated k times is a subsequence of s
    function canForm(t: string): boolean {
        if (t.length === 0) return true;
        let idx = 0, reps = 0;
        for (let i = 0; i < n; ++i) {
            if (s[i] === t[idx]) {
                idx++;
                if (idx === t.length) {
                    reps++;
                    if (reps === k) return true;
                    idx = 0;
                }
            }
        }
        return false;
    }

    const used = new Array(26).fill(0);
    function dfs(cur: string): void {
        if (!canForm(cur)) return; // prune
        if (
            cur.length > best.length ||
            (cur.length === best.length && cur > best)
        ) {
            best = cur;
        }
        if (cur.length === maxLen) return;

        for (const idx of candidates) {
            if (used[idx] < limit[idx]) {
                used[idx]++;
                dfs(cur + String.fromCharCode(97 + idx));
                used[idx]--;
            }
        }
    }

    dfs("");
    return best;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function longestSubsequenceRepeatedK($s, $k) {
        $n = strlen($s);
        $maxLen = intdiv($n, $k);
        if ($maxLen == 0) return "";
        
        // frequency of each character
        $freq = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            $freq[$idx]++;
        }
        
        // how many times each character can appear in the answer
        $cntArr = [];
        $totalPossible = 0;
        for ($i = 0; $i < 26; $i++) {
            $ch = chr(97 + $i);
            if ($freq[$i] >= $k) {
                $cnt = intdiv($freq[$i], $k);
                $cntArr[$ch] = $cnt;
                $totalPossible += $cnt;
            } else {
                $cntArr[$ch] = 0;
            }
        }
        if ($totalPossible == 0) return "";
        
        // try lengths from longest to shortest
        for ($len = $maxLen; $len >= 1; $len--) {
            if ($totalPossible < $len) continue;
            $curr = "";
            $answer = null;
            $this->backtrack($len, 0, $curr, $cntArr, $s, $k, $answer);
            if ($answer !== null) return $answer;
        }
        return "";
    }
    
    private function backtrack($targetLen, $depth, &$curr, &$cntArr, $s, $k, &$ans) {
        if ($ans !== null) return true; // already found
        if ($depth == $targetLen) {
            if ($this->isValid($curr, $s, $k)) {
                $ans = $curr;
                return true;
            }
            return false;
        }
        for ($c = ord('z'); $c >= ord('a'); $c--) {
            $ch = chr($c);
            if ($cntArr[$ch] > 0) {
                $cntArr[$ch]--;
                $curr .= $ch;
                if ($this->backtrack($targetLen, $depth + 1, $curr, $cntArr, $s, $k, $ans)) return true;
                // backtrack
                $curr = substr($curr, 0, -1);
                $cntArr[$ch]++;
            }
        }
        return false;
    }
    
    private function isValid($t, $s, $k) {
        $lenT = strlen($t);
        if ($lenT == 0) return false;
        $i = 0; $j = 0; $cnt = 0;
        $n = strlen($s);
        while ($i < $n && $cnt < $k) {
            if ($s[$i] === $t[$j]) {
                $j++;
                if ($j == $lenT) {
                    $cnt++;
                    $j = 0;
                }
            }
            $i++;
        }
        return $cnt == $k;
    }
}
```

## Swift

```swift
class Solution {
    func longestSubsequenceRepeatedK(_ s: String, _ k: Int) -> String {
        let n = s.count
        let maxLen = n / k
        if maxLen == 0 { return "" }
        let sArr = Array(s)
        var freq = [Int](repeating: 0, count: 26)
        for ch in sArr {
            let idx = Int(ch.unicodeScalars.first!.value - 97)
            freq[idx] += 1
        }
        var maxUse = [Int](repeating: 0, count: 26)
        var allowedIndices: [Int] = []
        for i in 0..<26 {
            let use = freq[i] / k
            if use > 0 {
                maxUse[i] = use
                allowedIndices.append(i)
            }
        }
        if allowedIndices.isEmpty { return "" }
        allowedIndices.sort(by: >)   // descending for lexicographic order
        
        var best = ""
        var curCounts = [Int](repeating: 0, count: 26)
        
        func can(_ cand: String) -> Bool {
            if cand.isEmpty { return true }
            let cArr = Array(cand)
            var i = 0
            var reps = 0
            for ch in sArr {
                if ch == cArr[i] {
                    i += 1
                    if i == cArr.count {
                        i = 0
                        reps += 1
                        if reps == k { return true }
                    }
                }
            }
            return false
        }
        
        func dfs(_ current: String) {
            for idx in allowedIndices {
                if curCounts[idx] < maxUse[idx] {
                    let ch = Character(UnicodeScalar(idx + 97)!)
                    curCounts[idx] += 1
                    let next = current + String(ch)
                    if can(next) {
                        if next.count > best.count || (next.count == best.count && next > best) {
                            best = next
                        }
                        if next.count < maxLen {
                            dfs(next)
                        }
                    }
                    curCounts[idx] -= 1
                }
            }
        }
        
        dfs("")
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestSubsequenceRepeatedK(s: String, k: Int): String {
        val n = s.length
        val maxLen = n / k
        if (maxLen == 0) return ""
        // frequency count
        val freq = IntArray(26)
        for (ch in s) {
            freq[ch - 'a']++
        }
        // characters that appear at least k times, in descending order
        val allowed = mutableListOf<Char>()
        for (i in 25 downTo 0) {
            if (freq[i] >= k) allowed.add(('a' + i))
        }
        if (allowed.isEmpty()) return ""

        // check whether seq repeated k times is a subsequence of s
        fun canRepeat(seq: String): Boolean {
            var pos = 0
            var cnt = 0
            val m = seq.length
            for (c in s) {
                if (c == seq[pos]) {
                    pos++
                    if (pos == m) {
                        cnt++
                        if (cnt >= k) return true
                        pos = 0
                    }
                }
            }
            return false
        }

        // depth‑first search building strings of a given length in lexicographically descending order
        fun dfs(targetLen: Int, sb: StringBuilder): String? {
            if (sb.length == targetLen) {
                val cand = sb.toString()
                return if (canRepeat(cand)) cand else null
            }
            for (ch in allowed) {
                sb.append(ch)
                val res = dfs(targetLen, sb)
                if (res != null) return res
                sb.setLength(sb.length - 1)
            }
            return null
        }

        for (len in maxLen downTo 1) {
            val ans = dfs(len, StringBuilder())
            if (ans != null) return ans
        }
        return ""
    }
}
```

## Dart

```dart
class Solution {
  String _s = "";
  int _k = 0;
  List<int> _freq = [];
  String _best = "";

  String longestSubsequenceRepeatedK(String s, int k) {
    _s = s;
    _k = k;
    _freq = List.filled(26, 0);
    for (int i = 0; i < s.length; ++i) {
      _freq[s.codeUnitAt(i) - 97]++;
    }
    _best = "";
    _dfs("");
    return _best;
  }

  bool _can(String cand) {
    if (cand.isEmpty) return true;
    int need = cand.length * _k;
    int i = 0;
    for (int idx = 0; idx < _s.length && i < need; ++idx) {
      if (_s.codeUnitAt(idx) == cand.codeUnitAt(i % cand.length)) {
        i++;
      }
    }
    return i == need;
  }

  void _dfs(String cur) {
    for (int ci = 25; ci >= 0; --ci) {
      if (_freq[ci] < _k) continue;
      String next = cur + String.fromCharCode(97 + ci);
      if (_can(next)) {
        _dfs(next);
      }
    }
    if (cur.length > _best.length ||
        (cur.length == _best.length && cur.compareTo(_best) > 0)) {
      _best = cur;
    }
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

func longestSubsequenceRepeatedK(s string, k int) string {
	n := len(s)
	if k == 0 || n == 0 {
		return ""
	}
	// frequency of each character
	freq := [26]int{}
	for i := 0; i < n; i++ {
		freq[s[i]-'a']++
	}

	// characters that can appear at least once in the answer
	maxUse := [26]int{}
	allowed := []byte{}
	for i := 0; i < 26; i++ {
		if freq[i] >= k {
			maxUse[i] = freq[i] / k
			allowed = append(allowed, byte('a'+i))
		}
	}
	if len(allowed) == 0 {
		return ""
	}
	// iterate allowed characters in descending order for lexicographic priority
	sort.Slice(allowed, func(i, j int) bool { return allowed[i] > allowed[j] })

	maxLen := n / k // upper bound of answer length

	best := ""

	// helper to test if t repeated k times is a subsequence of s
	canRepeat := func(t string) bool {
		if len(t) == 0 {
			return true
		}
		idx, cnt := 0, 0
		for i := 0; i < n && cnt < k; i++ {
			if s[i] == t[idx] {
				idx++
				if idx == len(t) {
					cnt++
					idx = 0
				}
			}
		}
		return cnt >= k
	}

	type node struct {
		str []byte
		cnt [26]int
	}
	stack := []node{{str: []byte{}, cnt: [26]int{}}}

	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if len(cur.str) > 0 {
			strVal := string(cur.str)
			if canRepeat(strVal) {
				if len(strVal) > len(best) || (len(strVal) == len(best) && strVal > best) {
					best = strVal
				}
			} else {
				// if current string cannot be repeated k times, no need to extend it
				continue
			}
		}

		if len(cur.str) == maxLen {
			continue
		}

		for _, ch := range allowed {
			idx := int(ch - 'a')
			if cur.cnt[idx]+1 > maxUse[idx] {
				continue
			}
			newCnt := cur.cnt
			newCnt[idx]++
			newStr := append(append([]byte{}, cur.str...), ch)
			if canRepeat(string(newStr)) {
				stack = append(stack, node{str: newStr, cnt: newCnt})
			}
		}
	}

	return best
}
```

## Ruby

```ruby
def longest_subsequence_repeated_k(s, k)
  n = s.length
  max_len = n / k
  freq = Array.new(26, 0)
  s.each_byte { |b| freq[b - 97] += 1 }

  chars = []
  (0...26).each do |i|
    use = freq[i] / k
    chars << [(i + 97).chr, use] if use > 0
  end
  return "" if chars.empty?

  chars.sort_by! { |c, _| -c.ord }

  valid = lambda do |t|
    i = 0
    cnt = 0
    tlen = t.length
    s.each_byte do |b|
      if b == t.getbyte(i)
        i += 1
        if i == tlen
          cnt += 1
          return true if cnt >= k
          i = 0
        end
      end
    end
    false
  end

  dfs = nil
  dfs = lambda do |pos, target_len, cur_str, rem_counts|
    if pos == target_len
      return cur_str if valid.call(cur_str)
      return nil
    end
    chars.each_with_index do |(ch, _), idx|
      next if rem_counts[idx] == 0
      rem_counts[idx] -= 1
      res = dfs.call(pos + 1, target_len, cur_str + ch, rem_counts)
      return res if res
      rem_counts[idx] += 1
    end
    nil
  end

  max_len.downto(1) do |len|
    rem = chars.map { |_, cnt| cnt }
    ans = dfs.call(0, len, "", rem)
    return ans if ans
  end
  ""
end
```

## Scala

```scala
object Solution {
    def longestSubsequenceRepeatedK(s: String, k: Int): String = {
        val n = s.length
        val maxLen = n / k
        if (maxLen == 0) return ""

        // frequency count
        val freq = Array.fill(26)(0)
        for (ch <- s) {
            freq(ch - 'a') += 1
        }

        // candidates: characters that appear at least k times, in descending order
        val candidates = (0 until 26).filter(i => freq(i) >= k).map(i => ('a' + i).toChar).reverse

        // helper to check if t repeated k times is a subsequence of s
        def canRepeat(t: String): Boolean = {
            var idx = 0
            val m = n
            var repeat = 0
            while (repeat < k) {
                var ti = 0
                while (ti < t.length) {
                    val target = t.charAt(ti)
                    while (idx < m && s.charAt(idx) != target) idx += 1
                    if (idx == m) return false
                    idx += 1
                    ti += 1
                }
                repeat += 1
            }
            true
        }

        var best = ""

        def dfs(cur: String): Unit = {
            // update best
            if (cur.length > best.length || (cur.length == best.length && cur > best)) {
                best = cur
            }
            if (cur.length == maxLen) return

            for (c <- candidates) {
                val next = cur + c
                if (canRepeat(next)) {
                    dfs(next)
                }
            }
        }

        dfs("")
        best
    }
}
```

## Rust

```rust
use std::vec::Vec;

fn is_valid(seq: &Vec<u8>, s_bytes: &[u8], k: i32) -> bool {
    if seq.is_empty() {
        return false;
    }
    let len_seq = seq.len();
    let total = len_seq * k as usize;
    let mut p = 0usize;
    for &ch in s_bytes.iter() {
        if ch == seq[p % len_seq] {
            p += 1;
            if p == total {
                break;
            }
        }
    }
    p == total
}

fn dfs(
    seq: &mut Vec<u8>,
    used: &mut [i32; 26],
    best: &mut String,
    allowed: &[u8],
    limit: &[i32; 26],
    s_bytes: &[u8],
    k: i32,
    max_len: usize,
) {
    if !seq.is_empty() && is_valid(seq, s_bytes, k) {
        let cand = unsafe { String::from_utf8_unchecked(seq.clone()) };
        if cand.len() > best.len() || (cand.len() == best.len() && cand > *best) {
            *best = cand;
        }
    }
    if seq.len() == max_len {
        return;
    }

    for &c in allowed.iter() {
        let idx = (c - b'a') as usize;
        if used[idx] < limit[idx] {
            seq.push(c);
            used[idx] += 1;
            if is_valid(seq, s_bytes, k) {
                dfs(seq, used, best, allowed, limit, s_bytes, k, max_len);
            }
            seq.pop();
            used[idx] -= 1;
        }
    }
}

impl Solution {
    pub fn longest_subsequence_repeated_k(s: String, k: i32) -> String {
        let n = s.len();
        let max_len = n / k as usize;
        if max_len == 0 {
            return "".to_string();
        }
        let bytes = s.as_bytes();

        // frequency count
        let mut freq = [0i32; 26];
        for &b in bytes.iter() {
            freq[(b - b'a') as usize] += 1;
        }

        // characters that appear at least k times, sorted descending
        let mut allowed: Vec<u8> = Vec::new();
        let mut limit = [0i32; 26];
        for i in (0..26).rev() {
            if freq[i] >= k {
                allowed.push(b'a' + i as u8);
                limit[i] = freq[i] / k;
            }
        }

        if allowed.is_empty() {
            return "".to_string();
        }

        let mut best = String::new();
        let mut seq: Vec<u8> = Vec::new();
        let mut used = [0i32; 26];

        dfs(
            &mut seq,
            &mut used,
            &mut best,
            &allowed,
            &limit,
            bytes,
            k,
            max_len,
        );

        best
    }
}
```

## Racket

```racket
(define/contract (longest-subsequence-repeated-k s k)
  (-> string? exact-integer? string?)
  (let* ((n (string-length s))
         (maxLen (quotient n k))
         (freq (make-vector 26 0)))
    ;; count frequencies
    (for ([i (in-range n)])
      (let* ((ch (string-ref s i))
             (idx (- (char->integer ch) (char->integer #\a))))
        (vector-set! freq idx (+ 1 (vector-ref freq idx)))))
    ;; allowed uses per character (each use consumes k occurrences)
    (define rem0 (make-vector 26 0))
    (for ([i (in-range 26)])
      (let ((cnt (vector-ref freq i)))
        (vector-set! rem0 i (quotient cnt k))))
    (define best "")
    ;; check if t repeated k times is a subsequence of s
    (define (can-repeat? t)
      (let* ((m (string-length t))
             (len-s n))
        (if (= m 0) #t
            (let loop ((i 0) (j 0) (cnt 0))
              (cond [(= cnt k) #t]
                    [(>= i len-s) #f]
                    [else (if (char=? (string-ref s i) (string-ref t j))
                              (let ((nj (+ j 1)))
                                (if (= nj m)
                                    (loop (+ i 1) 0 (+ cnt 1))
                                    (loop (+ i 1) nj cnt)))
                              (loop (+ i 1) j cnt))])))))
    ;; depth‑first search building candidates in reverse lexicographic order
    (define (dfs cur rem)
      (when (and (> (string-length cur) (string-length best))
                 (can-repeat? cur))
        (set! best cur))
      (when (< (string-length cur) maxLen)
        (for ([ci (in-range 25 -1 -1)])
          (let ((cnt (vector-ref rem ci)))
            (when (> cnt 0)
              (let* ((ch (integer->char (+ ci (char->integer #\a))))
                     (newcur (string-append cur (string ch)))
                     (newrem (vector-copy rem)))
                (vector-set! newrem ci (- cnt 1))
                (when (can-repeat? newcur)
                  (dfs newcur newrem))))))))
    (dfs "" rem0)
    best))
```

## Erlang

```erlang
-spec longest_subsequence_repeated_k(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
longest_subsequence_repeated_k(S, K) ->
    Slist = binary_to_list(S),
    N = length(Slist),
    MaxLen = N div K,
    Counts = lists:foldl(fun(C, Acc) ->
                CharIdx = C - $a,
                maps:update_with(CharIdx, fun(V) -> V + 1 end, 1, Acc)
            end, #{}, Slist),
    Limits0 = maps:fold(fun(CharIdx, Count, Acc) ->
                if Count >= K ->
                        Limit = Count div K,
                        maps:put(CharIdx, Limit, Acc);
                   true -> Acc
                end
            end, #{}, Counts),
    AllowedDesc = lists:sort(fun({A,_},{B,_}) -> A > B end, maps:to_list(Limits0)),
    Candidates = collect([], Limits0, Slist, K, MaxLen, AllowedDesc),
    Best = best_candidate(Candidates),
    list_to_binary(Best).

collect(Cur, LimitsMap, Slist, K, MaxLen, AllowedDesc) ->
    CurLen = length(Cur),
    Init = case Cur of [] -> []; _ -> [Cur] end,
    if CurLen >= MaxLen ->
            Init;
       true ->
            lists:foldl(fun({CharIdx,_}, Acc) ->
                Limit = maps:get(CharIdx, LimitsMap),
                if Limit > 0 ->
                        NewChar = CharIdx + $a,
                        NewCur = Cur ++ [NewChar],
                        case can_repeat_k(NewCur, Slist, K) of
                            true ->
                                UpdatedLimits = maps:update(CharIdx, fun(V) -> V - 1 end, LimitsMap),
                                Acc ++ collect(NewCur, UpdatedLimits, Slist, K, MaxLen, AllowedDesc);
                            false -> Acc
                        end;
                   true -> Acc
                end
            end, Init, AllowedDesc)
    end.

can_repeat_k(Str, Slist, K) ->
    Len = length(Str),
    go(Slist, Str, 0, 0, K, Len).

go([], _Str, _Pos, RepCnt, K, _Len) ->
    RepCnt >= K;
go([C|Rest], Str, Pos, RepCnt, K, Len) ->
    Target = lists:nth(Pos + 1, Str),
    if C == Target ->
            NewPos = Pos + 1,
            if NewPos == Len ->
                    go(Rest, Str, 0, RepCnt + 1, K, Len);
               true ->
                    go(Rest, Str, NewPos, RepCnt, K, Len)
            end;
       true -> go(Rest, Str, Pos, RepCnt, K, Len)
    end.

best_candidate(Candidates) ->
    lists:foldl(fun(Str, Acc) ->
        case better(Str, Acc) of
            true -> Str;
            false -> Acc
        end
    end, [], Candidates).

better([], []) -> false;
better([], _) -> false;
better(_, []) -> true;
better(A, B) ->
    LenA = length(A),
    LenB = length(B),
    if LenA > LenB -> true;
       LenA < LenB -> false;
       true -> lex_greater(A, B)
    end.

lex_greater([], []) -> false;
lex_greater([H|T], [H|T2]) -> lex_greater(T, T2);
lex_greater([H|_], [L|_]) when H > L -> true;
lex_greater(_, _) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_subsequence_repeated_k(s :: String.t(), k :: integer) :: String.t()
  def longest_subsequence_repeated_k(s, k) do
    n = String.length(s)
    max_len = div(n, k)

    freq =
      s
      |> String.graphemes()
      |> Enum.reduce(%{}, fn ch, acc ->
        Map.update(acc, ch, 1, &(&1 + 1))
      end)

    candidates =
      freq
      |> Enum.filter(fn {_ch, cnt} -> cnt >= k end)
      |> Enum.map(fn {ch, _cnt} -> ch end)
      |> Enum.sort(&(String.compare(&1, &2) == :gt))

    if max_len == 0 or candidates == [] do
      ""
    else
      dfs(s, candidates, max_len, k, "", "")
    end
  end

  defp dfs(_s, _candidates, _max_len, _k, cur, best) when String.length(cur) == 0 and best == "" do
    best
  end

  defp dfs(s, candidates, max_len, k, cur, best) do
    best =
      cond do
        String.length(cur) > String.length(best) -> cur
        String.length(cur) == String.length(best) and cur > best -> cur
        true -> best
      end

    if String.length(cur) == max_len do
      best
    else
      Enum.reduce(candidates, best, fn ch, acc_best ->
        new_cur = cur <> ch

        if can_repeat?(s, new_cur, k) do
          dfs(s, candidates, max_len, k, new_cur, acc_best)
        else
          acc_best
        end
      end)
    end
  end

  defp can_repeat?(s, pat, k) do
    len = String.length(pat)

    if len == 0 do
      true
    else
      p = String.graphemes(pat)

      {cnt, _idx} =
        s
        |> String.graphemes()
        |> Enum.reduce_while({0, 0}, fn ch, {c, i} ->
          if ch == Enum.at(p, i) do
            i = i + 1

            if i == len do
              c = c + 1

              if c == k do
                {:halt, {c, i}}
              else
                {:cont, {c, 0}}
              end
            else
              {:cont, {c, i}}
            end
          else
            {:cont, {c, i}}
          end
        end)

      cnt >= k
    end
  end
end
```
