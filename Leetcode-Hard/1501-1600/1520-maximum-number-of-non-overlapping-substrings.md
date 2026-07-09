# 1520. Maximum Number of Non-Overlapping Substrings

## Cpp

```cpp
class Solution {
public:
    vector<string> maxNumOfSubstrings(string s) {
        const int n = s.size();
        const int INF = 1e9;
        vector<int> first(26, INF), last(26, -1);
        for (int i = 0; i < n; ++i) {
            int c = s[i] - 'a';
            first[c] = min(first[c], i);
            last[c] = max(last[c], i);
        }
        vector<pair<int,int>> intervals;
        for (int ch = 0; ch < 26; ++ch) {
            if (first[ch] == INF) continue;
            int l = first[ch];
            int r = last[ch];
            int curL = l, curR = r;
            bool expanded = true;
            while (expanded) {
                expanded = false;
                int newL = curL, newR = curR;
                for (int i = curL; i <= curR; ++i) {
                    int c = s[i] - 'a';
                    if (first[c] < newL) { newL = first[c]; }
                    if (last[c] > newR) { newR = last[c]; }
                }
                if (newL != curL || newR != curR) {
                    expanded = true;
                    curL = newL;
                    curR = newR;
                }
            }
            // ensure this interval is minimal for its starting character
            if (curL == first[ch]) {
                intervals.emplace_back(curL, curR);
            }
        }
        sort(intervals.begin(), intervals.end(),
             [](const pair<int,int>& a, const pair<int,int>& b) {
                 return a.second < b.second;
             });
        vector<string> ans;
        int prevEnd = -1;
        for (auto &p : intervals) {
            if (p.first > prevEnd) {
                ans.push_back(s.substr(p.first, p.second - p.first + 1));
                prevEnd = p.second;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public List<String> maxNumOfSubstrings(String s) {
        int n = s.length();
        int[] first = new int[26];
        int[] last = new int[26];
        Arrays.fill(first, n);
        Arrays.fill(last, -1);
        for (int i = 0; i < n; i++) {
            int idx = s.charAt(i) - 'a';
            if (first[idx] == n) first[idx] = i;
            last[idx] = i;
        }
        List<int[]> intervals = new ArrayList<>();
        for (int c = 0; c < 26; c++) {
            if (first[c] == n) continue;
            int l = first[c];
            int r = last[c];
            boolean valid = true;
            int i = l;
            while (i <= r) {
                int chIdx = s.charAt(i) - 'a';
                if (first[chIdx] < l) {
                    valid = false;
                    break;
                }
                r = Math.max(r, last[chIdx]);
                i++;
            }
            if (valid) intervals.add(new int[]{l, r});
        }
        intervals.sort((a, b) -> a[1] - b[1]); // sort by right endpoint
        List<String> result = new ArrayList<>();
        int prevEnd = -1;
        for (int[] seg : intervals) {
            if (seg[0] > prevEnd) {
                result.add(s.substring(seg[0], seg[1] + 1));
                prevEnd = seg[1];
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        first = [n] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            if i < first[idx]:
                first[idx] = i
            if i > last[idx]:
                last[idx] = i

        intervals = []
        for c in range(26):
            if first[c] == n:
                continue
            l, r = first[c], last[c]
            valid = True
            j = l
            while j <= r:
                idx = ord(s[j]) - 97
                if first[idx] < l:
                    valid = False
                    break
                if last[idx] > r:
                    r = last[idx]
                j += 1
            if valid:
                intervals.append((l, r))

        intervals.sort(key=lambda x: x[1])
        res = []
        prev_end = -1
        for l, r in intervals:
            if l > prev_end:
                res.append(s[l:r+1])
                prev_end = r
        return res
```

## Python3

```python
from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        first = [-1] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        intervals = []
        for c in range(26):
            if first[c] == -1:
                continue
            l, r = first[c], last[c]
            j = l
            while j <= r:
                idx = ord(s[j]) - 97
                if first[idx] < l or last[idx] > r:
                    l = min(l, first[idx])
                    r = max(r, last[idx])
                    j = l  # restart scanning from new left bound
                else:
                    j += 1
            if l == first[c]:  # minimal interval starting at its first occurrence
                intervals.append((l, r))

        intervals.sort(key=lambda x: x[1])  # sort by right endpoint

        res = []
        prev_end = -1
        for l, r in intervals:
            if l > prev_end:
                res.append(s[l:r+1])
                prev_end = r
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int l;
    int r;
} Interval;

/* Comparator for qsort: sort by right endpoint ascending, then left ascending */
static int cmpInterval(const void *a, const void *b) {
    const Interval *ia = (const Interval *)a;
    const Interval *ib = (const Interval *)b;
    if (ia->r != ib->r) return ia->r - ib->r;
    return ia->l - ib->l;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** maxNumOfSubstrings(char* s, int* returnSize) {
    int n = strlen(s);
    int first[26];
    int last[26];
    for (int i = 0; i < 26; ++i) {
        first[i] = -1;
        last[i] = -1;
    }
    for (int i = 0; i < n; ++i) {
        int c = s[i] - 'a';
        if (first[c] == -1) first[c] = i;
        last[c] = i;
    }

    Interval intervals[26];
    int cnt = 0;

    for (int ch = 0; ch < 26; ++ch) {
        if (first[ch] == -1) continue;          // character not present
        int l = first[ch];
        int r = last[ch];
        int i = l;
        int valid = 1;
        while (i <= r) {
            int cur = s[i] - 'a';
            if (first[cur] < l) {               // need to include earlier occurrence -> invalid
                valid = 0;
                break;
            }
            if (last[cur] > r) {
                r = last[cur];                  // expand right bound
            }
            ++i;
        }
        if (valid) {
            intervals[cnt].l = l;
            intervals[cnt].r = r;
            ++cnt;
        }
    }

    qsort(intervals, cnt, sizeof(Interval), cmpInterval);

    // Greedy selection of non‑overlapping intervals
    Interval selected[26];
    int selCnt = 0;
    int prevEnd = -1;
    for (int i = 0; i < cnt; ++i) {
        if (intervals[i].l > prevEnd) {
            selected[selCnt++] = intervals[i];
            prevEnd = intervals[i].r;
        }
    }

    char **res = (char **)malloc(sizeof(char *) * selCnt);
    for (int i = 0; i < selCnt; ++i) {
        int l = selected[i].l;
        int r = selected[i].r;
        int len = r - l + 1;
        char *sub = (char *)malloc(len + 1);
        memcpy(sub, s + l, len);
        sub[len] = '\0';
        res[i] = sub;
    }

    *returnSize = selCnt;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<string> MaxNumOfSubstrings(string s) {
        int n = s.Length;
        int[] first = new int[26];
        int[] last = new int[26];
        for (int i = 0; i < 26; i++) {
            first[i] = -1;
            last[i] = -1;
        }
        for (int i = 0; i < n; i++) {
            int idx = s[i] - 'a';
            if (first[idx] == -1) first[idx] = i;
            last[idx] = i;
        }

        var intervals = new List<(int left, int right)>();
        for (int c = 0; c < 26; c++) {
            if (first[c] == -1) continue;
            int left = first[c];
            int right = last[c];
            bool expanded = true;
            while (expanded) {
                expanded = false;
                for (int i = left; i <= right; i++) {
                    int ch = s[i] - 'a';
                    if (first[ch] < left) {
                        left = first[ch];
                        expanded = true;
                    }
                    if (last[ch] > right) {
                        right = last[ch];
                        expanded = true;
                    }
                }
            }
            // keep only minimal intervals that start at the character's first occurrence
            if (left == first[c]) {
                intervals.Add((left, right));
            }
        }

        intervals.Sort((a, b) => {
            int cmp = a.right.CompareTo(b.right);
            return cmp != 0 ? cmp : a.left.CompareTo(b.left);
        });

        var result = new List<string>();
        int prevEnd = -1;
        foreach (var seg in intervals) {
            if (seg.left > prevEnd) {
                result.Add(s.Substring(seg.left, seg.right - seg.left + 1));
                prevEnd = seg.right;
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var maxNumOfSubstrings = function(s) {
    const n = s.length;
    const first = new Array(26).fill(Infinity);
    const last = new Array(26).fill(-1);
    
    for (let i = 0; i < n; ++i) {
        const idx = s.charCodeAt(i) - 97;
        if (first[idx] === Infinity) first[idx] = i;
        last[idx] = i;
    }
    
    // expand interval [l, r] to include all characters that appear inside it
    function expand(l, r) {
        let changed = true;
        while (changed) {
            changed = false;
            for (let i = l; i <= r; ++i) {
                const idx = s.charCodeAt(i) - 97;
                if (first[idx] < l) {
                    l = first[idx];
                    changed = true;
                }
                if (last[idx] > r) {
                    r = last[idx];
                    changed = true;
                }
            }
        }
        return [l, r];
    }
    
    const intervals = [];
    for (let c = 0; c < 26; ++c) {
        if (first[c] === Infinity) continue;
        let [l, r] = expand(first[c], last[c]);
        // verify that the interval is self‑contained
        let ok = true;
        for (let i = l; i <= r && ok; ++i) {
            const idx = s.charCodeAt(i) - 97;
            if (first[idx] < l || last[idx] > r) ok = false;
        }
        if (ok) intervals.push({l, r});
    }
    
    intervals.sort((a, b) => a.r - b.r);
    
    const res = [];
    let prevEnd = -1;
    for (const inter of intervals) {
        if (inter.l > prevEnd) {
            res.push(s.substring(inter.l, inter.r + 1));
            prevEnd = inter.r;
        }
    }
    return res;
};
```

## Typescript

```typescript
function maxNumOfSubstrings(s: string): string[] {
    const n = s.length;
    const left = new Array(26).fill(Infinity);
    const right = new Array(26).fill(-1);
    for (let i = 0; i < n; i++) {
        const idx = s.charCodeAt(i) - 97;
        if (left[idx] === Infinity) left[idx] = i;
        right[idx] = i;
    }

    const getInterval = (start: number): [number, number] | null => {
        let l = start;
        let r = right[s.charCodeAt(start) - 97];
        let i = l;
        while (i <= r) {
            const idx = s.charCodeAt(i) - 97;
            if (left[idx] < l) return null; // need to expand left, invalid for this start
            if (right[idx] > r) r = right[idx];
            i++;
        }
        return [l, r];
    };

    const intervals: [number, number][] = [];
    for (let c = 0; c < 26; c++) {
        if (left[c] === Infinity) continue;
        const start = left[c];
        const interval = getInterval(start);
        if (interval) intervals.push(interval);
    }

    intervals.sort((a, b) => a[1] - b[1]); // sort by end index

    const result: string[] = [];
    let prevEnd = -1;
    for (const [l, r] of intervals) {
        if (l > prevEnd) {
            result.push(s.substring(l, r + 1));
            prevEnd = r;
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function maxNumOfSubstrings($s) {
        $n = strlen($s);
        $INF = $n + 1;
        $left = array_fill(0, 26, $INF);
        $right = array_fill(0, 26, -1);

        // record first and last positions for each character
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            if ($left[$idx] > $i) $left[$idx] = $i;
            if ($right[$idx] < $i) $right[$idx] = $i;
        }

        $intervals = [];

        // build minimal valid intervals for each character
        for ($c = 0; $c < 26; $c++) {
            if ($left[$c] == $INF) continue; // character not present

            $l = $left[$c];
            $r = $right[$c];
            $valid = true;
            for ($i = $l; $i <= $r; $i++) {
                $idx = ord($s[$i]) - 97;
                if ($left[$idx] < $l) { // cannot form a minimal substring
                    $valid = false;
                    break;
                }
                if ($right[$idx] > $r) {
                    $r = $right[$idx]; // expand right bound
                }
            }
            if ($valid) {
                $intervals[] = [$l, $r];
            }
        }

        // sort intervals by their ending index (and then start to stabilize)
        usort($intervals, function($a, $b) {
            if ($a[1] == $b[1]) return $a[0] <=> $b[0];
            return $a[1] <=> $b[1];
        });

        $result = [];
        $prevEnd = -1;
        foreach ($intervals as $int) {
            [$l, $r] = $int;
            if ($l > $prevEnd) {
                $result[] = substr($s, $l, $r - $l + 1);
                $prevEnd = $r;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func maxNumOfSubstrings(_ s: String) -> [String] {
        let chars = Array(s)
        let n = chars.count
        let aVal = Int(Character("a").asciiValue!)
        var firstPos = Array(repeating: -1, count: 26)
        var lastPos = Array(repeating: -1, count: 26)
        
        for i in 0..<n {
            let idx = Int(chars[i].asciiValue!) - aVal
            if firstPos[idx] == -1 { firstPos[idx] = i }
            lastPos[idx] = i
        }
        
        var intervals: [(Int, Int)] = []
        for i in 0..<n {
            let cIdx = Int(chars[i].asciiValue!) - aVal
            // start only at the first occurrence of its character
            if firstPos[cIdx] != i { continue }
            
            var l = firstPos[cIdx]
            var r = lastPos[cIdx]
            var j = l
            while j <= r {
                let idx = Int(chars[j].asciiValue!) - aVal
                if firstPos[idx] < l {
                    l = firstPos[idx]
                    j = l   // restart scanning from new left bound
                }
                if lastPos[idx] > r {
                    r = lastPos[idx]
                }
                j += 1
            }
            intervals.append((l, r))
        }
        
        intervals.sort { $0.1 < $1.1 }   // sort by right endpoint
        
        var result: [String] = []
        var prevEnd = -1
        for (l, r) in intervals {
            if l > prevEnd {
                let substr = String(chars[l...r])
                result.append(substr)
                prevEnd = r
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxNumOfSubstrings(s: String): List<String> {
        val n = s.length
        val first = IntArray(26) { -1 }
        val last = IntArray(26) { -1 }

        for (i in 0 until n) {
            val idx = s[i] - 'a'
            if (first[idx] == -1) first[idx] = i
            last[idx] = i
        }

        val intervals = mutableListOf<Pair<Int, Int>>()

        for (c in 0 until 26) {
            if (first[c] == -1) continue
            var l = first[c]
            var r = last[c]
            var changed = true
            while (changed) {
                changed = false
                var i = l
                while (i <= r) {
                    val chIdx = s[i] - 'a'
                    if (first[chIdx] < l) {
                        l = first[chIdx]
                        changed = true
                    }
                    if (last[chIdx] > r) {
                        r = last[chIdx]
                        changed = true
                    }
                    i++
                }
            }
            if (first[c] == l) {
                intervals.add(Pair(l, r))
            }
        }

        intervals.sortBy { it.second }

        val result = mutableListOf<String>()
        var prevEnd = -1
        for ((start, end) in intervals) {
            if (start > prevEnd) {
                result.add(s.substring(start, end + 1))
                prevEnd = end
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> maxNumOfSubstrings(String s) {
    int n = s.length;
    const int INF = 1 << 30;
    List<int> first = List.filled(26, INF);
    List<int> last = List.filled(26, -1);

    for (int i = 0; i < n; ++i) {
      int c = s.codeUnitAt(i) - 97;
      if (first[c] > i) first[c] = i;
      if (last[c] < i) last[c] = i;
    }

    List<List<int>> intervals = [];

    for (int ch = 0; ch < 26; ++ch) {
      if (last[ch] == -1) continue; // character not present
      int start = first[ch];
      int end = last[ch];
      bool expanded = true;
      while (expanded) {
        expanded = false;
        for (int i = start; i <= end; ++i) {
          int cur = s.codeUnitAt(i) - 97;
          if (first[cur] < start) {
            start = first[cur];
            expanded = true;
          }
          if (last[cur] > end) {
            end = last[cur];
            expanded = true;
          }
        }
      }
      // after expansion, interval is minimal valid for this character
      intervals.add([start, end]);
    }

    intervals.sort((a, b) {
      if (a[1] != b[1]) return a[1] - b[1];
      return a[0] - b[0];
    });

    List<String> result = [];
    int prevEnd = -1;
    for (var seg in intervals) {
      int l = seg[0], r = seg[1];
      if (l > prevEnd) {
        result.add(s.substring(l, r + 1));
        prevEnd = r;
      }
    }

    return result;
  }
}
```

## Golang

```go
import "sort"

type interval struct {
	l, r int
}

func maxNumOfSubstrings(s string) []string {
	first := make([]int, 26)
	last := make([]int, 26)
	for i := 0; i < 26; i++ {
		first[i] = -1
	}
	for i, ch := range s {
		idx := int(ch - 'a')
		if first[idx] == -1 {
			first[idx] = i
		}
		last[idx] = i
	}

	var intervals []interval
	for c := 0; c < 26; c++ {
		if first[c] == -1 {
			continue
		}
		l, r := first[c], last[c]
		i := l
		for i <= r {
			idx := int(s[i] - 'a')
			if first[idx] < l {
				l = first[idx]
				i = l - 1 // will become l after i++
			}
			if last[idx] > r {
				r = last[idx]
			}
			i++
		}
		intervals = append(intervals, interval{l, r})
	}

	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i].r == intervals[j].r {
			return intervals[i].l < intervals[j].l
		}
		return intervals[i].r < intervals[j].r
	})

	var res []string
	prevEnd := -1
	for _, iv := range intervals {
		if iv.l > prevEnd {
			res = append(res, s[iv.l:iv.r+1])
			prevEnd = iv.r
		}
	}
	return res
}
```

## Ruby

```ruby
def max_num_of_substrings(s)
  first = Array.new(26, -1)
  last = Array.new(26, -1)

  s.each_byte.with_index do |b, i|
    idx = b - 97
    first[idx] = i if first[idx] == -1
    last[idx] = i
  end

  intervals = []
  0.upto(25) do |c|
    next if first[c] == -1
    l = first[c]
    r = last[c]
    j = l
    while j <= r
      idx = s.getbyte(j) - 97
      if first[idx] < l
        l = first[idx]
        j = l
        next
      end
      r = last[idx] if last[idx] > r
      j += 1
    end
    intervals << [l, r]
  end

  intervals.sort_by! { |lr| lr[1] }
  res = []
  prev_end = -1
  intervals.each do |l, r|
    if l > prev_end
      res << s[l..r]
      prev_end = r
    end
  end
  res
end
```

## Scala

```scala
object Solution {
    def maxNumOfSubstrings(s: String): List[String] = {
        val n = s.length
        val first = Array.fill(26)(n)
        val last = Array.fill(26)(-1)

        for (i <- 0 until n) {
            val idx = s.charAt(i) - 'a'
            if (i < first(idx)) first(idx) = i
            if (i > last(idx)) last(idx) = i
        }

        val intervals = scala.collection.mutable.ArrayBuffer[(Int, Int)]()

        for (c <- 0 until 26) {
            if (last(c) != -1) {
                var l = first(c)
                var r = last(c)
                var k = l
                while (k <= r) {
                    val idx2 = s.charAt(k) - 'a'
                    if (first(idx2) < l) {
                        l = first(idx2)
                        k = l // restart scanning from new start
                    } else if (last(idx2) > r) {
                        r = last(idx2)
                        k += 1
                    } else {
                        k += 1
                    }
                }
                intervals.append((l, r))
            }
        }

        val sorted = intervals.sortBy(_._2)

        val result = scala.collection.mutable.ArrayBuffer[String]()
        var prevEnd = -1
        for ((l, r) <- sorted) {
            if (l > prevEnd) {
                result.append(s.substring(l, r + 1))
                prevEnd = r
            }
        }

        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_num_of_substrings(s: String) -> Vec<String> {
        let n = s.len();
        let bytes = s.as_bytes();

        // first and last occurrence for each character
        let mut first = vec![usize::MAX; 26];
        let mut last = vec![0usize; 26];
        for (i, &b) in bytes.iter().enumerate() {
            let idx = (b - b'a') as usize;
            if first[idx] == usize::MAX {
                first[idx] = i;
            }
            last[idx] = i;
        }

        // collect candidate intervals
        let mut intervals: Vec<(usize, usize)> = Vec::new();
        for c in 0..26 {
            if first[c] == usize::MAX {
                continue;
            }
            let mut l = first[c];
            let mut r = last[c];
            let mut changed = true;
            while changed {
                changed = false;
                for i in l..=r {
                    let ch = (bytes[i] - b'a') as usize;
                    if first[ch] < l {
                        l = first[ch];
                        changed = true;
                    }
                    if last[ch] > r {
                        r = last[ch];
                        changed = true;
                    }
                }
            }
            // after expansion, the interval is valid
            intervals.push((l, r));
        }

        // sort by right endpoint to apply greedy selection
        intervals.sort_by_key(|&(_, r)| r);

        let mut result_intervals: Vec<(usize, usize)> = Vec::new();
        let mut last_end: i32 = -1;
        for &(l, r) in &intervals {
            if (l as i32) > last_end {
                result_intervals.push((l, r));
                last_end = r as i32;
            }
        }

        // build the resulting substrings
        let mut ans: Vec<String> = Vec::new();
        for &(l, r) in &result_intervals {
            ans.push(s[l..r + 1].to_string());
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-num-of-substrings s)
  (-> string? (listof string?))
  (let* ((n (string-length s))
         (first (make-vector 26 -1))
         (last (make-vector 26 -1))
         (base (char->integer #\a)))
    ;; record first and last positions for each character
    (for ([i (in-range n)])
      (let* ((ch (string-ref s i))
             (idx (- (char->integer ch) base)))
        (when (= (vector-ref first idx) -1)
          (vector-set! first idx i))
        (vector-set! last idx i)))
    ;; build minimal valid intervals
    (define intervals '())
    (for ([c (in-range 26)])
      (let ((l (vector-ref first c)))
        (when (>= l 0)
          (let* ((r0 (vector-ref last c))
                 (start l)
                 (end r0)
                 (valid #t))
            (let loop ((i start))
              (when (and (< i (add1 end)) valid)
                (let* ((ch (string-ref s i))
                       (idx (- (char->integer ch) base)))
                  (if (< (vector-ref first idx) start)
                      (set! valid #f)
                      (begin
                        (when (> (vector-ref last idx) end)
                          (set! end (vector-ref last idx)))
                        (loop (+ i 1)))))))
            (when valid
              (set! intervals (cons (list start end) intervals)))))))
    ;; sort intervals by right endpoint
    (define sorted-intervals
      (sort intervals (lambda (a b) (< (cadr a) (cadr b)))))
    ;; greedy selection of non‑overlapping intervals
    (define result '())
    (define last-end -1)
    (for ([intv sorted-intervals])
      (let ((l (car intv))
            (r (cadr intv)))
        (when (> l last-end)
          (set! result (cons intv result))
          (set! last-end r))))
    ;; extract substrings
    (map (lambda (intv)
           (substring s (car intv) (+ (cadr intv) 1)))
         (reverse result))))
```

## Erlang

```erlang
-spec max_num_of_substrings(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
max_num_of_substrings(S) ->
    {FirstMap, LastMap} = build_maps(S, 0, #{}, #{}),
    CharList = maps:keys(FirstMap),
    Intervals = [expand_interval(C, FirstMap, LastMap, S) || C <- CharList],
    Sorted = lists:keysort(2, Intervals), % sort by end index
    select_intervals(Sorted, S, -1, []).

%% Build first and last occurrence maps for each character.
build_maps(_Bin, Index, FMap, LMap) when Index >= byte_size(_Bin) ->
    {FMap, LMap};
build_maps(Bin, Index, FMap, LMap) ->
    Char = binary:at(Bin, Index),
    NewFMap = case maps:is_key(Char, FMap) of
        true -> FMap;
        false -> maps:put(Char, Index, FMap)
    end,
    NewLMap = maps:put(Char, Index, LMap),
    build_maps(Bin, Index + 1, NewFMap, NewLMap).

%% Expand interval for a character to include all characters that appear inside it.
expand_interval(C, FirstMap, LastMap, Bin) ->
    Start0 = maps:get(C, FirstMap),
    End0   = maps:get(C, LastMap),
    expand_loop(Start0, End0, FirstMap, LastMap, Bin).

expand_loop(Start, End, FirstMap, LastMap, Bin) ->
    {NewStart, NewEnd, Changed} = scan_interval(Start, End, FirstMap, LastMap, Bin),
    case Changed of
        true -> expand_loop(NewStart, NewEnd, FirstMap, LastMap, Bin);
        false -> {Start, End}
    end.

%% Scan current interval and possibly extend it.
scan_interval(Start, End, FirstMap, LastMap, Bin) ->
    scan_interval_helper(Start, End, Start, End, false, FirstMap, LastMap, Bin).

scan_interval_helper(I, EndIdx, CurS, CurE, Changed, FMap, LMap, Bin)
        when I =< EndIdx ->
    Char = binary:at(Bin, I),
    CFirst = maps:get(Char, FMap),
    CLast  = maps:get(Char, LMap),
    NewS = if CFirst < CurS -> CFirst; true -> CurS end,
    NewE = if CLast > CurE -> CLast; true -> CurE end,
    NewChanged = Changed orelse (NewS =/= CurS) orelse (NewE =/= CurE),
    scan_interval_helper(I + 1, EndIdx, NewS, NewE, NewChanged, FMap, LMap, Bin);
scan_interval_helper(_I, _EndIdx, CurS, CurE, Changed, _FMap, _LMap, _Bin) ->
    {CurS, CurE, Changed}.

%% Greedy selection of non‑overlapping intervals.
select_intervals([], _Bin, _LastEnd, Acc) ->
    lists:reverse(Acc);
select_intervals([{S,E}|Rest], Bin, LastEnd, Acc) ->
    case S > LastEnd of
        true ->
            Len = E - S + 1,
            Sub = binary:part(Bin, S, Len),
            select_intervals(Rest, Bin, E, [Sub|Acc]);
        false ->
            select_intervals(Rest, Bin, LastEnd, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_num_of_substrings(s :: String.t) :: [String.t]
  def max_num_of_substrings(s) do
    len = byte_size(s)
    arr = :array.from_list(String.to_charlist(s))

    {left_map, right_map} =
      Enum.reduce(0..len - 1, {%{}, %{}}, fn i, {lmap, rmap} ->
        c = :array.get(i, arr)
        idx = c - ?a

        lmap = Map.update(lmap, idx, i, &min(&1, i))
        rmap = Map.update(rmap, idx, i, &max(&1, i))

        {lmap, rmap}
      end)

    intervals =
      Enum.reduce(0..len - 1, [], fn i, acc ->
        c = :array.get(i, arr)
        idx = c - ?a
        start = Map.get(left_map, idx)

        if i == start do
          {l_final, r_final} = expand_interval(arr, left_map, right_map, start, Map.get(right_map, idx))

          if l_final == start do
            [{l_final, r_final} | acc]
          else
            acc
          end
        else
          acc
        end
      end)

    sorted =
      intervals
      |> Enum.sort_by(fn {_l, r} -> r end)

    {selected_rev, _} =
      Enum.reduce(sorted, {[], -1}, fn {l, r}, {acc, last_end} ->
        if l > last_end do
          {[String.slice(s, l, r - l + 1) | acc], r}
        else
          {acc, last_end}
        end
      end)

    Enum.reverse(selected_rev)
  end

  defp expand_interval(arr, left_map, right_map, l, r) do
    {new_l, new_r} = scan_interval(arr, left_map, right_map, l, r, l)

    if new_l < l do
      expand_interval(arr, left_map, right_map, new_l, new_r)
    else
      {new_l, new_r}
    end
  end

  defp scan_interval(_arr, _left_map, _right_map, l, r, i) when i > r do
    {l, r}
  end

  defp scan_interval(arr, left_map, right_map, l, r, i) do
    ch = :array.get(i, arr)
    idx = ch - ?a

    cur_l = min(l, Map.get(left_map, idx))
    cur_r = max(r, Map.get(right_map, idx))

    if cur_l < l do
      {cur_l, cur_r}
    else
      scan_interval(arr, left_map, right_map, cur_l, cur_r, i + 1)
    end
  end
end
```
