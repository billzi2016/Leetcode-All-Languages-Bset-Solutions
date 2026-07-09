# 3458. Select K Disjoint Special Substrings

## Cpp

```cpp
class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        if (k == 0) return true;
        int n = s.size();
        const int ALPH = 26;
        vector<int> first(ALPH, -1), last(ALPH, -1);
        for (int i = 0; i < n; ++i) {
            int c = s[i] - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }
        vector<pair<int,int>> intervals;
        for (int ch = 0; ch < ALPH; ++ch) {
            if (first[ch] == -1) continue;
            int left = first[ch];
            int right = last[ch];
            bool changed = true;
            while (changed) {
                changed = false;
                for (int i = left; i <= right; ++i) {
                    int c = s[i] - 'a';
                    if (first[c] < left) {
                        left = first[c];
                        changed = true;
                    }
                    if (last[c] > right) {
                        right = last[c];
                        changed = true;
                    }
                }
            }
            // ensure the interval starts at the original first occurrence of this character
            if (left == first[ch]) {
                intervals.emplace_back(left, right);
            }
        }
        sort(intervals.begin(), intervals.end(),
             [](const pair<int,int>& a, const pair<int,int>& b){
                 return a.second < b.second;
             });
        int cnt = 0;
        int lastEnd = -1;
        for (auto &p : intervals) {
            if (p.first > lastEnd) {
                ++cnt;
                lastEnd = p.second;
                if (cnt >= k) return true;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean maxSubstringLength(String s, int k) {
        if (k == 0) return true;
        int n = s.length();
        int[] first = new int[26];
        int[] last = new int[26];
        for (int i = 0; i < 26; ++i) {
            first[i] = n;
            last[i] = -1;
        }
        for (int i = 0; i < n; ++i) {
            int idx = s.charAt(i) - 'a';
            if (first[idx] == n) first[idx] = i;
            last[idx] = i;
        }

        java.util.List<int[]> intervals = new java.util.ArrayList<>();
        for (int c = 0; c < 26; ++c) {
            if (last[c] == -1) continue; // character not present
            int l = first[c];
            int r = last[c];
            boolean changed = true;
            while (changed) {
                changed = false;
                for (int i = l; i <= r; ++i) {
                    int idx = s.charAt(i) - 'a';
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
            // keep only minimal intervals that start at the character's first occurrence
            if (l == first[c]) {
                intervals.add(new int[]{l, r});
            }
        }

        intervals.sort((a, b) -> Integer.compare(a[1], b[1])); // sort by end

        int count = 0;
        int prevEnd = -1;
        for (int[] iv : intervals) {
            if (iv[0] > prevEnd) {
                count++;
                prevEnd = iv[1];
                if (count >= k) return true;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def maxSubstringLength(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return True

        n = len(s)
        first = [n] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            if first[idx] == n:
                first[idx] = i
            last[idx] = i

        intervals = []
        i = 0
        while i < n:
            idx = ord(s[i]) - 97
            if i != first[idx]:
                i += 1
                continue
            end = last[idx]
            j = i
            while j <= end:
                cur_idx = ord(s[j]) - 97
                if last[cur_idx] > end:
                    end = last[cur_idx]
                j += 1
            intervals.append((i, end))
            i += 1

        intervals.sort(key=lambda x: x[1])
        cnt = 0
        cur_end = -1
        for l, r in intervals:
            if l > cur_end:
                cnt += 1
                cur_end = r
                if cnt >= k:
                    return True
        return cnt >= k
```

## Python3

```python
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0:
            return True
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
        intervals = [(first[ch], last[ch]) for ch in first]
        intervals.sort(key=lambda x: x[1])
        cnt = 0
        prev_end = -1
        for l, r in intervals:
            if l > prev_end:
                cnt += 1
                prev_end = r
        return cnt >= k
```

## C

```c
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    int l;
    int r;
} Interval;

static int cmpInterval(const void *a, const void *b) {
    const Interval *ia = (const Interval *)a;
    const Interval *ib = (const Interval *)b;
    if (ia->r != ib->r) return ia->r - ib->r;
    return ia->l - ib->l;
}

bool maxSubstringLength(char* s, int k) {
    if (k == 0) return true;
    int n = strlen(s);
    int first[26], last[26];
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
        if (first[ch] == -1) continue;
        int l = first[ch];
        int r = last[ch];
        int j = l;
        bool ok = true;
        while (j <= r) {
            int cur = s[j] - 'a';
            if (first[cur] < l) { ok = false; break; }
            if (last[cur] > r) r = last[cur];
            ++j;
        }
        if (ok) {
            intervals[cnt].l = l;
            intervals[cnt].r = r;
            ++cnt;
        }
    }

    qsort(intervals, cnt, sizeof(Interval), cmpInterval);

    int selected = 0;
    int prevEnd = -1;
    for (int i = 0; i < cnt; ++i) {
        if (intervals[i].l > prevEnd) {
            ++selected;
            prevEnd = intervals[i].r;
            if (selected >= k) return true;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool MaxSubstringLength(string s, int k) {
        if (k == 0) return true;
        int n = s.Length;
        char[] arr = s.ToCharArray();
        int[] left = new int[26];
        int[] right = new int[26];
        for (int i = 0; i < 26; i++) {
            left[i] = n;
            right[i] = -1;
        }
        for (int i = 0; i < n; i++) {
            int c = arr[i] - 'a';
            if (i < left[c]) left[c] = i;
            if (i > right[c]) right[c] = i;
        }

        var intervals = new List<int[]>();
        for (int ch = 0; ch < 26; ch++) {
            if (right[ch] == -1) continue; // character not present
            int start = left[ch];
            int end = right[ch];
            bool expanded = true;
            while (expanded) {
                expanded = false;
                for (int i = start; i <= end; i++) {
                    int cur = arr[i] - 'a';
                    if (left[cur] < start) { start = left[cur]; expanded = true; }
                    if (right[cur] > end) { end = right[cur]; expanded = true; }
                }
            }
            // keep only intervals that start at the first occurrence of this character
            if (start == left[ch]) {
                intervals.Add(new int[] { start, end });
            }
        }

        intervals.Sort((a, b) => {
            if (a[1] != b[1]) return a[1].CompareTo(b[1]);
            return a[0].CompareTo(b[0]);
        });

        int cnt = 0;
        int lastEnd = -1;
        foreach (var iv in intervals) {
            if (iv[0] > lastEnd) {
                cnt++;
                lastEnd = iv[1];
                if (cnt >= k) return true; // early exit
            }
        }
        return cnt >= k;
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
var maxSubstringLength = function(s, k) {
    if (k === 0) return true;
    const n = s.length;
    const first = new Array(26).fill(-1);
    const last = new Array(26).fill(-1);
    for (let i = 0; i < n; ++i) {
        const idx = s.charCodeAt(i) - 97;
        if (first[idx] === -1) first[idx] = i;
        last[idx] = i;
    }
    const intervals = [];
    for (let c = 0; c < 26; ++c) {
        if (first[c] === -1) continue;
        let start = first[c];
        let end = last[c];
        let valid = true;
        for (let i = start; i <= end; ++i) {
            const idx = s.charCodeAt(i) - 97;
            if (first[idx] < start) { // earlier occurrence outside interval
                valid = false;
                break;
            }
            if (last[idx] > end) {
                end = last[idx]; // expand right bound
            }
        }
        if (valid) intervals.push([start, end]);
    }
    intervals.sort((a, b) => a[1] - b[1] || a[0] - b[0]);
    let cnt = 0;
    let prevEnd = -1;
    for (const [l, r] of intervals) {
        if (l > prevEnd) {
            ++cnt;
            prevEnd = r;
            if (cnt >= k) return true;
        }
    }
    return false;
};
```

## Typescript

```typescript
function maxSubstringLength(s: string, k: number): boolean {
    if (k === 0) return true;
    const n = s.length;
    const first = new Array(26).fill(-1);
    const last = new Array(26).fill(-1);
    for (let i = 0; i < n; ++i) {
        const idx = s.charCodeAt(i) - 97;
        if (first[idx] === -1) first[idx] = i;
        last[idx] = i;
    }
    const intervals: { l: number; r: number }[] = [];
    for (let i = 0; i < 26; ++i) {
        if (first[i] !== -1) intervals.push({ l: first[i], r: last[i] });
    }
    intervals.sort((a, b) => a.r - b.r || a.l - b.l);
    let cnt = 0;
    let prevEnd = -1;
    for (const seg of intervals) {
        if (seg.l > prevEnd) {
            ++cnt;
            prevEnd = seg.r;
            if (cnt >= k) return true;
        }
    }
    return false;
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
    function maxSubstringLength($s, $k) {
        if ($k == 0) {
            return true;
        }
        $n = strlen($s);
        // there are only lowercase letters
        $first = array_fill(0, 26, $n);   // init with large value
        $last  = array_fill(0, 26, -1);
        
        for ($i = 0; $i < $n; $i++) {
            $cIdx = ord($s[$i]) - ord('a');
            if ($i < $first[$cIdx]) $first[$cIdx] = $i;
            if ($i > $last[$cIdx]) $last[$cIdx] = $i;
        }
        
        $intervals = [];
        for ($i = 0; $i < 26; $i++) {
            if ($last[$i] != -1) { // character appears
                $intervals[] = [$first[$i], $last[$i]];
            }
        }
        
        // sort by end, then start
        usort($intervals, function($a, $b) {
            if ($a[1] == $b[1]) return $a[0] <=> $b[0];
            return $a[1] <=> $b[1];
        });
        
        $cnt = 0;
        $prevEnd = -1;
        foreach ($intervals as $int) {
            if ($int[0] > $prevEnd) {
                $cnt++;
                $prevEnd = $int[1];
                if ($cnt >= $k) return true;
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func maxSubstringLength(_ s: String, _ k: Int) -> Bool {
        if k == 0 { return true }
        let n = s.count
        let chars = Array(s)
        var first = [Int](repeating: n, count: 26)
        var last = [Int](repeating: -1, count: 26)
        
        for i in 0..<n {
            let idx = Int(chars[i].asciiValue! - Character("a").asciiValue!)
            if first[idx] == n { first[idx] = i }
            last[idx] = i
        }
        
        var intervals: [(Int, Int)] = []
        
        for c in 0..<26 {
            let start = first[c]
            if start == n { continue } // character not present
            var end = last[c]
            var j = start
            var valid = true
            while j <= end {
                let curIdx = Int(chars[j].asciiValue! - Character("a").asciiValue!)
                if first[curIdx] < start {
                    valid = false
                    break
                }
                if last[curIdx] > end {
                    end = last[curIdx]
                }
                j += 1
            }
            if valid {
                intervals.append((start, end))
            }
        }
        
        intervals.sort { $0.1 < $1.1 } // sort by ending index
        
        var count = 0
        var prevEnd = -1
        for interval in intervals {
            if interval.0 > prevEnd {
                count += 1
                prevEnd = interval.1
                if count >= k { return true }
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    fun maxSubstringLength(s: String, k: Int): Boolean {
        if (k == 0) return true
        val n = s.length
        val first = IntArray(26) { -1 }
        val last = IntArray(26) { -1 }
        for (i in 0 until n) {
            val idx = s[i] - 'a'
            if (first[idx] == -1) first[idx] = i
            last[idx] = i
        }

        data class Interval(val l: Int, val r: Int)

        val intervals = mutableListOf<Interval>()
        // individual letter intervals
        for (c in 0 until 26) {
            if (first[c] != -1) {
                intervals.add(Interval(first[c], last[c]))
            }
        }

        // build partition blocks (merged overlapping intervals)
        data class Letter(val l: Int, val r: Int)
        val letters = mutableListOf<Letter>()
        for (c in 0 until 26) {
            if (first[c] != -1) {
                letters.add(Letter(first[c], last[c]))
            }
        }
        letters.sortBy { it.l }

        var i = 0
        while (i < letters.size) {
            var start = letters[i].l
            var end = letters[i].r
            var j = i + 1
            while (j < letters.size && letters[j].l <= end) {
                end = maxOf(end, letters[j].r)
                j++
            }
            intervals.add(Interval(start, end))
            i = j
        }

        // deduplicate
        val seen = HashSet<Long>()
        val uniq = mutableListOf<Interval>()
        for (itv in intervals) {
            val key = (itv.l.toLong() shl 32) or (itv.r.toLong() and 0xffffffffL)
            if (seen.add(key)) {
                uniq.add(itv)
            }
        }

        // sort by end, then start
        uniq.sortWith(compareBy<Interval> { it.r }.thenBy { it.l })

        var count = 0
        var lastEnd = -1
        for (itv in uniq) {
            if (itv.l > lastEnd) {
                count++
                lastEnd = itv.r
                if (count >= k) return true
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool maxSubstringLength(String s, int k) {
    if (k == 0) return true;
    int n = s.length;
    const int INF = 1 << 30;
    List<int> left = List.filled(26, INF);
    List<int> right = List.filled(26, -1);

    for (int i = 0; i < n; i++) {
      int ch = s.codeUnitAt(i) - 97;
      if (i < left[ch]) left[ch] = i;
      if (i > right[ch]) right[ch] = i;
    }

    List<_Interval> intervals = [];

    for (int c = 0; c < 26; c++) {
      if (right[c] == -1) continue; // character not present
      int l = left[c];
      int r = right[c];
      bool expanded = true;
      while (expanded) {
        expanded = false;
        for (int i = l; i <= r; i++) {
          int ch = s.codeUnitAt(i) - 97;
          if (left[ch] < l) {
            l = left[ch];
            expanded = true;
          }
          if (right[ch] > r) {
            r = right[ch];
            expanded = true;
          }
        }
      }
      intervals.add(_Interval(l, r));
    }

    // sort by right endpoint, then by left
    intervals.sort((a, b) {
      if (a.r != b.r) return a.r - b.r;
      return a.l - b.l;
    });

    int count = 0;
    int lastEnd = -1;
    for (var inter in intervals) {
      if (inter.l > lastEnd) {
        count++;
        lastEnd = inter.r;
        if (count >= k) return true;
      }
    }
    return false;
  }
}

class _Interval {
  int l, r;
  _Interval(this.l, this.r);
}
```

## Golang

```go
func maxSubstringLength(s string, k int) bool {
	if k == 0 {
		return true
	}
	n := len(s)
	const alphabet = 26
	first := make([]int, alphabet)
	last := make([]int, alphabet)
	for i := 0; i < alphabet; i++ {
		first[i] = -1
	}
	for i := 0; i < n; i++ {
		c := int(s[i] - 'a')
		if first[c] == -1 {
			first[c] = i
		}
		last[c] = i
	}

	type interval struct{ l, r int }
	var intervals []interval

	for c := 0; c < alphabet; c++ {
		if first[c] == -1 {
			continue
		}
		l := first[c]
		r := last[c]
		j := l
		for j <= r {
			cur := int(s[j] - 'a')
			if last[cur] > r {
				r = last[cur]
			}
			j++
		}
		intervals = append(intervals, interval{l: l, r: r})
	}

	// sort intervals by right endpoint
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i].r == intervals[j].r {
			return intervals[i].l < intervals[j].l
		}
		return intervals[i].r < intervals[j].r
	})

	count := 0
	prevEnd := -1
	for _, iv := range intervals {
		if iv.l > prevEnd {
			count++
			prevEnd = iv.r
			if count >= k {
				return true
			}
		}
	}
	return false
}
```

## Ruby

```ruby
def max_substring_length(s, k)
  return true if k == 0
  n = s.length
  first = Array.new(26, -1)
  last = Array.new(26, -1)
  bytes = s.bytes

  bytes.each_with_index do |b, i|
    idx = b - 97
    first[idx] = i if first[idx] == -1
    last[idx] = i
  end

  intervals = []

  0.upto(25) do |c|
    next if first[c] == -1
    l = first[c]
    r = last[c]

    loop do
      changed = false
      (l..r).each do |j|
        idx = bytes[j] - 97
        if first[idx] < l || last[idx] > r
          l = [l, first[idx]].min
          r = [r, last[idx]].max
          changed = true
        end
      end
      break unless changed
    end

    intervals << [l, r] if l == first[c]
  end

  intervals.sort_by! { |int| int[1] }

  cnt = 0
  prev_end = -1
  intervals.each do |l, r|
    if l > prev_end
      cnt += 1
      prev_end = r
    end
  end

  cnt >= k
end
```

## Scala

```scala
object Solution {
  def maxSubstringLength(s: String, k: Int): Boolean = {
    if (k == 0) return true
    val n = s.length
    val first = Array.fill(26)(-1)
    val last = Array.fill(26)(-1)

    for (i <- 0 until n) {
      val idx = s.charAt(i) - 'a'
      if (first(idx) == -1) first(idx) = i
      last(idx) = i
    }

    import scala.collection.mutable.ArrayBuffer
    val intervals = ArrayBuffer.empty[(Int, Int)]

    for (c <- 0 until 26) {
      if (first(c) != -1) {
        var l = first(c)
        var r = last(c)
        var expanded = true
        while (expanded) {
          expanded = false
          var i = l
          while (i <= r) {
            val idx = s.charAt(i) - 'a'
            if (first(idx) < l) { l = first(idx); expanded = true }
            if (last(idx) > r)  { r = last(idx); expanded = true }
            i += 1
          }
        }
        // keep only minimal intervals that start at the character's first occurrence
        if (l == first(c)) {
          intervals.append((l, r))
        }
      }
    }

    val sorted = intervals.sortBy(_._2)
    var count = 0
    var prevEnd = -1
    for ((l, r) <- sorted) {
      if (l > prevEnd) {
        count += 1
        prevEnd = r
      }
    }
    count >= k
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_substring_length(s: String, k: i32) -> bool {
        if k <= 0 {
            return true;
        }
        let n = s.len();
        let bytes = s.as_bytes();
        const INF: usize = usize::MAX;
        let mut first = [INF; 26];
        let mut last = [0usize; 26];
        for i in 0..n {
            let idx = (bytes[i] - b'a') as usize;
            if first[idx] == INF {
                first[idx] = i;
            }
            last[idx] = i;
        }

        let mut intervals: Vec<(usize, usize)> = Vec::new();

        for c in 0..26 {
            if first[c] == INF {
                continue;
            }
            let mut l = first[c];
            let mut r = last[c];
            let mut changed = true;
            while changed {
                changed = false;
                for j in 0..26 {
                    if first[j] == INF {
                        continue;
                    }
                    if (first[j] >= l && first[j] <= r) || (last[j] >= l && last[j] <= r) {
                        if first[j] < l {
                            l = first[j];
                            changed = true;
                        }
                        if last[j] > r {
                            r = last[j];
                            changed = true;
                        }
                    }
                }
            }

            // verify that all characters inside have their whole range inside
            let mut ok = true;
            for j in 0..26 {
                if first[j] == INF {
                    continue;
                }
                if first[j] >= l && first[j] <= r && last[j] > r {
                    ok = false;
                    break;
                }
            }
            if ok {
                intervals.push((l, r));
            }
        }

        intervals.sort_by(|a, b| {
            if a.1 == b.1 {
                a.0.cmp(&b.0)
            } else {
                a.1.cmp(&b.1)
            }
        });

        let mut cnt = 0usize;
        let mut last_end: i32 = -1;
        for (l, r) in intervals {
            if (l as i32) > last_end {
                cnt += 1;
                last_end = r as i32;
                if cnt >= k as usize {
                    return true;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (max-substring-length s k)
  (-> string? exact-integer? boolean?)
  (if (= k 0)
      #t
      (let* ((n (string-length s))
             (first (make-vector 26 -1))
             (last  (make-vector 26 -1)))
        ;; record first and last positions of each character
        (for ([i (in-range n)])
          (let* ((c   (string-ref s i))
                 (idx (- (char->integer c) (char->integer #\a))))
            (when (= (vector-ref first idx) -1)
              (vector-set! first idx i))
            (vector-set! last idx i)))
        ;; collect minimal special intervals
        (define intervals '())
        (for ([ch (in-range 26)])
          (let ((start (vector-ref first ch)))
            (when (not (= start -1))
              (let loop ((l start) (r (vector-ref last ch)) (changed #t))
                (if (not changed)
                    (when (= l start)               ; minimal interval
                      (set! intervals (cons (list l r) intervals)))
                    (let ((new-l l) (new-r r) (any-changed #f))
                      (for ([i (in-range l (+ r 1))])
                        (let* ((c2   (string-ref s i))
                               (idx2 (- (char->integer c2) (char->integer #\a)))
                               (fl   (vector-ref first idx2))
                               (lr   (vector-ref last idx2)))
                          (when (< fl new-l)
                            (set! new-l fl)
                            (set! any-changed #t))
                          (when (> lr new-r)
                            (set! new-r lr)
                            (set! any-changed #t))))
                      (loop new-l new-r any-changed)))))))
        ;; greedy selection of disjoint intervals
        (let ((sorted (sort intervals (lambda (a b) (< (cadr a) (cadr b))))))
          (let loop ((lst sorted) (prev -1) (cnt 0))
            (cond
              [(>= cnt k) #t]
              [(null? lst) #f]
              [else
               (define l (car (car lst)))
               (define r (cadr (car lst)))
               (if (> l prev)
                   (loop (cdr lst) r (+ cnt 1))
                   (loop (cdr lst) prev cnt))]))))))
```

## Erlang

```erlang
-module(solution).
-export([max_substring_length/2]).

-spec max_substring_length(S :: unicode:unicode_binary(), K :: integer()) -> boolean().
max_substring_length(S, K) ->
    case K of
        0 -> true;
        _ ->
            StrList = binary_to_list(S),
            N = length(StrList),
            {First, Last} = build_first_last(StrList, make_tuple(26, -1), make_tuple(26, -1), 0),
            StrT = list_to_tuple(StrList),
            Intervals = collect_intervals(N, StrT, First, Last),
            Sorted = lists:keysort(2, Intervals),
            Count = count_greedy(Sorted, -1, 0),
            Count >= K
    end.

build_first_last([], First, Last, _) -> {First, Last};
build_first_last([C|Rest], First, Last, Index) ->
    Idx = C - $a + 1,
    F = element(Idx, First),
    NewFirst = if F == -1 -> put_elem(Idx, First, Index); true -> First end,
    NewLast = put_elem(Idx, Last, Index),
    build_first_last(Rest, NewFirst, NewLast, Index + 1).

collect_intervals(N, StrT, First, Last) ->
    collect_idx(0, N, StrT, First, Last, []).

collect_idx(I, N, _, _, _, Acc) when I >= N -> lists:reverse(Acc);
collect_idx(I, N, StrT, First, Last, Acc) ->
    Char = element(I + 1, StrT),
    Idx = Char - $a + 1,
    F = element(Idx, First),
    case F == I of
        true ->
            L0 = I,
            R0 = element(Idx, Last),
            {L, R} = expand_interval(L0, R0, StrT, First, Last),
            collect_idx(I + 1, N, StrT, First, Last, [{L, R} | Acc]);
        false ->
            collect_idx(I + 1, N, StrT, First, Last, Acc)
    end.

expand_interval(L, R, StrT, First, Last) ->
    case scan_and_update(L, R, StrT, First, Last) of
        {L1, R1, true} -> expand_interval(L1, R1, StrT, First, Last);
        {_L, _R, false} -> {L, R}
    end.

scan_and_update(L, R, StrT, First, Last) ->
    scan(L, R, StrT, First, Last, L, R, false).

scan(Pos, R, _, _, _, CurL, CurR, Changed) when Pos > R ->
    {CurL, CurR, Changed};
scan(Pos, R, StrT, First, Last, CurL, CurR, Changed) ->
    Char = element(Pos + 1, StrT),
    Idx = Char - $a + 1,
    F = element(Idx, First),
    L2 = if F < CurL -> F; true -> CurL end,
    LastPos = element(Idx, Last),
    R2 = if LastPos > CurR -> LastPos; true -> CurR end,
    NewChanged = Changed orelse (F < CurL) orelse (LastPos > CurR),
    scan(Pos + 1, R, StrT, First, Last, L2, R2, NewChanged).

count_greedy([], _, C) -> C;
count_greedy([{L, R} | Rest], PrevEnd, C) ->
    if
        L > PrevEnd -> count_greedy(Rest, R, C + 1);
        true -> count_greedy(Rest, PrevEnd, C)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_substring_length(s :: String.t(), k :: integer) :: boolean
  def max_substring_length(s, k) do
    if k == 0 do
      true
    else
      n = byte_size(s)

      {first_pos, last_pos} =
        :binary.bin_to_list(s)
        |> Enum.with_index()
        |> Enum.reduce({%{}, %{}}, fn {c, i}, {f, l} ->
          idx = c - ?a

          f =
            if Map.has_key?(f, idx) do
              f
            else
              Map.put(f, idx, i)
            end

          l = Map.put(l, idx, i)
          {f, l}
        end)

      count = loop(0, n, s, first_pos, last_pos, 0)
      count >= k
    end
  end

  defp loop(i, n, _s, _first, _last, cnt) when i >= n, do: cnt

  defp loop(i, n, s, first, last, cnt) do
    c = :binary.at(s, i)
    idx = c - ?a

    if Map.get(first, idx) != i do
      loop(i + 1, n, s, first, last, cnt)
    else
      end_pos = expand(i, Map.get(last, idx), i, s, last)
      loop(end_pos + 1, n, s, first, last, cnt + 1)
    end
  end

  defp expand(_start, cur_end, j, _s, _last) when j > cur_end, do: cur_end

  defp expand(start, cur_end, j, s, last) do
    c = :binary.at(s, j)
    idx = c - ?a
    new_end = max(cur_end, Map.get(last, idx))
    expand(start, new_end, j + 1, s, last)
  end
end
```
