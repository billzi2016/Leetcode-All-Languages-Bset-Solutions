# 0395. Longest Substring with At Least K Repeating Characters

## Cpp

```cpp
class Solution {
public:
    int longestSubstring(string s, int k) {
        if (k == 1) return s.size();
        int n = s.size();
        int maxUnique = 0;
        int freqAll[26] = {0};
        for (char c : s) {
            if (freqAll[c - 'a']++ == 0) ++maxUnique;
        }
        int result = 0;
        for (int target = 1; target <= maxUnique; ++target) {
            int count[26] = {0};
            int start = 0, end = 0;
            int unique = 0, atLeastK = 0;
            while (end < n) {
                int idx = s[end] - 'a';
                if (count[idx] == 0) ++unique;
                ++count[idx];
                if (count[idx] == k) ++atLeastK;
                ++end;
                
                while (unique > target) {
                    int idx2 = s[start] - 'a';
                    if (count[idx2] == k) --atLeastK;
                    --count[idx2];
                    if (count[idx2] == 0) --unique;
                    ++start;
                }
                
                if (unique == target && unique == atLeastK) {
                    result = max(result, end - start);
                }
            }
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int longestSubstring(String s, int k) {
        if (k == 1) return s.length();
        int n = s.length();
        int maxUnique = 0;
        boolean[] seen = new boolean[26];
        for (int i = 0; i < n; i++) {
            int idx = s.charAt(i) - 'a';
            if (!seen[idx]) {
                seen[idx] = true;
                maxUnique++;
            }
        }

        int result = 0;
        for (int targetUnique = 1; targetUnique <= maxUnique; targetUnique++) {
            int[] count = new int[26];
            int start = 0, end = 0;
            int unique = 0;          // number of chars with count > 0 in window
            int atLeastK = 0;        // number of chars whose count >= k

            while (end < n) {
                int idxEnd = s.charAt(end) - 'a';
                if (count[idxEnd] == 0) unique++;
                count[idxEnd]++;
                if (count[idxEnd] == k) atLeastK++;
                end++;

                while (unique > targetUnique) {
                    int idxStart = s.charAt(start) - 'a';
                    if (count[idxStart] == k) atLeastK--;
                    count[idxStart]--;
                    if (count[idxStart] == 0) unique--;
                    start++;
                }

                if (unique == targetUnique && unique == atLeastK) {
                    result = Math.max(result, end - start);
                }
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        if k == 1:
            return n

        max_unique = len(set(s))
        result = 0

        for target_unique in range(1, max_unique + 1):
            count = [0] * 26
            start = 0
            end = 0
            unique = 0          # number of unique chars in current window
            at_least_k = 0      # number of chars meeting freq >= k

            while end < n:
                idx = ord(s[end]) - ord('a')
                if count[idx] == 0:
                    unique += 1
                count[idx] += 1
                if count[idx] == k:
                    at_least_k += 1
                end += 1

                # shrink window if we have more than target_unique unique chars
                while unique > target_unique:
                    idx_start = ord(s[start]) - ord('a')
                    if count[idx_start] == k:
                        at_least_k -= 1
                    count[idx_start] -= 1
                    if count[idx_start] == 0:
                        unique -= 1
                    start += 1

                # update result when all chars in window satisfy the condition
                if unique == target_unique and unique == at_least_k:
                    result = max(result, end - start)

        return result
```

## Python3

```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)
        n = len(s)
        # total distinct characters in the whole string
        max_unique = len(set(s))
        result = 0

        for target_unique in range(1, max_unique + 1):
            count = [0] * 26
            start = 0
            end = 0
            unique = 0          # number of chars with freq > 0 in window
            at_least_k = 0      # number of chars with freq >= k in window

            while end < n:
                idx = ord(s[end]) - 97
                if count[idx] == 0:
                    unique += 1
                count[idx] += 1
                if count[idx] == k:
                    at_least_k += 1
                end += 1

                # shrink window if we have more than target_unique distinct chars
                while unique > target_unique:
                    idx_start = ord(s[start]) - 97
                    if count[idx_start] == k:
                        at_least_k -= 1
                    count[idx_start] -= 1
                    if count[idx_start] == 0:
                        unique -= 1
                    start += 1

                # update result when all chars in window satisfy freq >= k
                if unique == target_unique and unique == at_least_k:
                    result = max(result, end - start)

        return result
```

## C

```c
int longestSubstring(char* s, int k) {
    if (k <= 1) {
        int len = 0;
        while (s[len]) ++len;
        return len;
    }
    // count total unique characters in the whole string
    int totalFreq[26] = {0};
    int maxUnique = 0;
    for (int i = 0; s[i]; ++i) {
        int idx = s[i] - 'a';
        if (totalFreq[idx] == 0) ++maxUnique;
        ++totalFreq[idx];
    }
    int ans = 0;
    // try each possible number of unique characters
    for (int targetUnique = 1; targetUnique <= maxUnique; ++targetUnique) {
        int freq[26] = {0};
        int start = 0, end = 0;
        int unique = 0, countAtLeastK = 0;
        while (s[end]) {
            if (unique <= targetUnique) {
                int idx = s[end] - 'a';
                if (freq[idx] == 0) ++unique;
                ++freq[idx];
                if (freq[idx] == k) ++countAtLeastK;
                ++end;
            } else {
                int idx = s[start] - 'a';
                if (freq[idx] == k) --countAtLeastK;
                --freq[idx];
                if (freq[idx] == 0) --unique;
                ++start;
            }
            if (unique == targetUnique && unique == countAtLeastK) {
                int len = end - start;
                if (len > ans) ans = len;
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int LongestSubstring(string s, int k)
    {
        if (k <= 1) return s.Length;

        int maxUnique = 0;
        bool[] seen = new bool[26];
        foreach (char c in s)
        {
            if (!seen[c - 'a'])
            {
                seen[c - 'a'] = true;
                maxUnique++;
            }
        }

        int result = 0;
        for (int targetUnique = 1; targetUnique <= maxUnique; targetUnique++)
        {
            int[] count = new int[26];
            int start = 0, end = 0;
            int unique = 0, atLeastK = 0;

            while (end < s.Length)
            {
                int idx = s[end] - 'a';
                if (count[idx] == 0) unique++;
                count[idx]++;
                if (count[idx] == k) atLeastK++;
                end++;

                while (unique > targetUnique)
                {
                    int leftIdx = s[start] - 'a';
                    if (count[leftIdx] == k) atLeastK--;
                    count[leftIdx]--;
                    if (count[leftIdx] == 0) unique--;
                    start++;
                }

                if (unique == targetUnique && unique == atLeastK)
                {
                    result = Math.Max(result, end - start);
                }
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
 * @param {number} k
 * @return {number}
 */
var longestSubstring = function(s, k) {
    const n = s.length;
    if (n === 0 || k > n) return 0;
    if (k <= 1) return n;

    // count total distinct characters in the whole string
    let maxUnique = 0;
    const globalFreq = new Array(26).fill(0);
    for (let i = 0; i < n; i++) {
        const idx = s.charCodeAt(i) - 97;
        if (globalFreq[idx] === 0) maxUnique++;
        globalFreq[idx]++;
    }

    let result = 0;

    // try each possible number of unique characters
    for (let target = 1; target <= maxUnique; target++) {
        const freq = new Array(26).fill(0);
        let start = 0, end = 0;
        let unique = 0;          // distinct chars in current window
        let countAtLeastK = 0;   // how many of those have freq >= k

        while (end < n) {
            if (unique <= target) {
                const idx = s.charCodeAt(end) - 97;
                if (freq[idx] === 0) unique++;
                freq[idx]++;
                if (freq[idx] === k) countAtLeastK++;
                end++;
            } else {
                const idx = s.charCodeAt(start) - 97;
                if (freq[idx] === k) countAtLeastK--;
                freq[idx]--;
                if (freq[idx] === 0) unique--;
                start++;
            }

            if (unique === target && unique === countAtLeastK) {
                result = Math.max(result, end - start);
            }
        }
    }

    return result;
};
```

## Typescript

```typescript
function longestSubstring(s: string, k: number): number {
    if (k === 1) return s.length;
    const n = s.length;
    // count distinct characters in the whole string
    const totalFreq = new Array(26).fill(0);
    for (let i = 0; i < n; ++i) {
        totalFreq[s.charCodeAt(i) - 97]++;
    }
    let maxUnique = 0;
    for (let cnt of totalFreq) if (cnt > 0) maxUnique++;

    let result = 0;

    for (let targetUnique = 1; targetUnique <= maxUnique; ++targetUnique) {
        const freq = new Array(26).fill(0);
        let start = 0, end = 0;
        let unique = 0;          // number of unique chars in current window
        let countAtLeastK = 0;   // number of chars meeting at least k occurrences

        while (end < n) {
            const idxEnd = s.charCodeAt(end) - 97;
            if (freq[idxEnd] === 0) unique++;
            freq[idxEnd]++;
            if (freq[idxEnd] === k) countAtLeastK++;

            // shrink window if we have more than targetUnique distinct chars
            while (unique > targetUnique) {
                const idxStart = s.charCodeAt(start) - 97;
                if (freq[idxStart] === k) countAtLeastK--;
                freq[idxStart]--;
                if (freq[idxStart] === 0) unique--;
                start++;
            }

            // update result when all chars in window satisfy the condition
            if (unique === targetUnique && unique === countAtLeastK) {
                result = Math.max(result, end - start + 1);
            }
            end++;
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
     * @param Integer $k
     * @return Integer
     */
    function longestSubstring($s, $k) {
        $len = strlen($s);
        if ($k == 1) return $len;

        // count distinct characters in the whole string
        $distinct = [];
        $maxUnique = 0;
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (!isset($distinct[$c])) {
                $distinct[$c] = true;
                $maxUnique++;
            }
        }

        $result = 0;

        // try each possible number of unique characters
        for ($targetUnique = 1; $targetUnique <= $maxUnique; $targetUnique++) {
            $freq = array_fill(0, 26, 0);
            $start = 0;
            $end = 0;
            $unique = 0;
            $countAtLeastK = 0;

            while ($end < $len) {
                $idx = ord($s[$end]) - ord('a');
                if ($freq[$idx] == 0) $unique++;
                $freq[$idx]++;
                if ($freq[$idx] == $k) $countAtLeastK++;

                // shrink window if unique exceeds target
                while ($unique > $targetUnique) {
                    $idxStart = ord($s[$start]) - ord('a');
                    if ($freq[$idxStart] == $k) $countAtLeastK--;
                    $freq[$idxStart]--;
                    if ($freq[$idxStart] == 0) $unique--;
                    $start++;
                }

                // update result if all characters meet the requirement
                if ($unique == $targetUnique && $unique == $countAtLeastK) {
                    $currLen = $end - $start + 1;
                    if ($currLen > $result) $result = $currLen;
                }
                $end++;
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func longestSubstring(_ s: String, _ k: Int) -> Int {
        let n = s.count
        if k > n { return 0 }
        if k <= 1 { return n }
        
        let chars = Array(s.utf8)
        var uniqueCharsSet = Set<UInt8>()
        for c in chars { uniqueCharsSet.insert(c) }
        let maxUnique = uniqueCharsSet.count
        
        var result = 0
        
        for targetUnique in 1...maxUnique {
            var count = [Int](repeating: 0, count: 26)
            var start = 0
            var end = 0
            var unique = 0
            var atLeastK = 0
            
            while end < n {
                let idxEnd = Int(chars[end] - 97)
                if count[idxEnd] == 0 { unique += 1 }
                count[idxEnd] += 1
                if count[idxEnd] == k { atLeastK += 1 }
                
                while unique > targetUnique {
                    let idxStart = Int(chars[start] - 97)
                    if count[idxStart] == k { atLeastK -= 1 }
                    count[idxStart] -= 1
                    if count[idxStart] == 0 { unique -= 1 }
                    start += 1
                }
                
                if unique == targetUnique && unique == atLeastK {
                    result = max(result, end - start + 1)
                }
                
                end += 1
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestSubstring(s: String, k: Int): Int {
        if (k <= 1) return s.length
        if (s.length < k) return 0

        var maxUnique = 0
        val seen = BooleanArray(26)
        for (ch in s) {
            val idx = ch - 'a'
            if (!seen[idx]) {
                seen[idx] = true
                maxUnique++
            }
        }

        var result = 0
        val n = s.length

        for (targetUnique in 1..maxUnique) {
            val freq = IntArray(26)
            var start = 0
            var end = 0
            var unique = 0
            var countAtLeastK = 0

            while (end < n) {
                val idxEnd = s[end] - 'a'
                if (freq[idxEnd] == 0) unique++
                freq[idxEnd]++
                if (freq[idxEnd] == k) countAtLeastK++
                end++

                while (unique > targetUnique) {
                    val idxStart = s[start] - 'a'
                    if (freq[idxStart] == k) countAtLeastK--
                    freq[idxStart]--
                    if (freq[idxStart] == 0) unique--
                    start++
                }

                if (unique == targetUnique && unique == countAtLeastK) {
                    result = maxOf(result, end - start)
                }
            }
        }

        return result
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int longestSubstring(String s, int k) {
    if (k <= 1) return s.length;
    int n = s.length;

    // total distinct characters in the whole string
    List<int> seen = List.filled(26, 0);
    int maxUnique = 0;
    for (int i = 0; i < n; i++) {
      int idx = s.codeUnitAt(i) - 97;
      if (seen[idx] == 0) {
        seen[idx] = 1;
        maxUnique++;
      }
    }

    int result = 0;

    // try every possible number of unique characters
    for (int target = 1; target <= maxUnique; target++) {
      List<int> cnt = List.filled(26, 0);
      int start = 0, end = 0;
      int unique = 0, atLeastK = 0;

      while (end < n) {
        int idx = s.codeUnitAt(end) - 97;
        if (cnt[idx] == 0) unique++;
        cnt[idx]++;
        if (cnt[idx] == k) atLeastK++;
        end++;

        // shrink window if we have too many unique chars
        while (unique > target) {
          int idx2 = s.codeUnitAt(start) - 97;
          if (cnt[idx2] == k) atLeastK--;
          cnt[idx2]--;
          if (cnt[idx2] == 0) unique--;
          start++;
        }

        // update answer when window is valid
        if (unique == target && unique == atLeastK) {
          result = max(result, end - start);
        }
      }
    }

    return result;
  }
}
```

## Golang

```go
func longestSubstring(s string, k int) int {
	if k <= 1 {
		return len(s)
	}
	// count distinct characters in s
	distinct := 0
	var seen [26]bool
	for i := 0; i < len(s); i++ {
		idx := int(s[i] - 'a')
		if !seen[idx] {
			seen[idx] = true
			distinct++
		}
	}

	maxLen := 0
	n := len(s)

	for targetUnique := 1; targetUnique <= distinct; targetUnique++ {
		var freq [26]int
		start, end := 0, 0
		uniqueCount, countAtLeastK := 0, 0

		for end < n {
			idx := int(s[end] - 'a')
			if freq[idx] == 0 {
				uniqueCount++
			}
			freq[idx]++
			if freq[idx] == k {
				countAtLeastK++
			}

			// shrink window if unique characters exceed target
			for uniqueCount > targetUnique {
				idx2 := int(s[start] - 'a')
				if freq[idx2] == k {
					countAtLeastK--
				}
				freq[idx2]--
				if freq[idx2] == 0 {
					uniqueCount--
				}
				start++
			}

			if uniqueCount == targetUnique && uniqueCount == countAtLeastK {
				if curLen := end - start + 1; curLen > maxLen {
					maxLen = curLen
				}
			}
			end++
		}
	}
	return maxLen
}
```

## Ruby

```ruby
def longest_substring(s, k)
  return s.length if k <= 1
  max_unique = s.each_char.to_a.uniq.size
  best = 0

  (1..max_unique).each do |target|
    counts = Array.new(26, 0)
    start_idx = 0
    unique = 0
    at_least_k = 0
    i = 0
    while i < s.length
      idx = s.getbyte(i) - 97
      if counts[idx] == 0
        unique += 1
      end
      counts[idx] += 1
      at_least_k += 1 if counts[idx] == k

      while unique > target
        left_idx = s.getbyte(start_idx) - 97
        at_least_k -= 1 if counts[left_idx] == k
        counts[left_idx] -= 1
        unique -= 1 if counts[left_idx] == 0
        start_idx += 1
      end

      if unique == target && unique == at_least_k
        len = i - start_idx + 1
        best = len if len > best
      end
      i += 1
    end
  end

  best
end
```

## Scala

```scala
object Solution {
    def longestSubstring(s: String, k: Int): Int = {
        if (k <= 1) return s.length
        val n = s.length
        // count distinct characters in the whole string
        val seen = new Array[Boolean](26)
        var maxUnique = 0
        var i = 0
        while (i < n) {
            val idx = s.charAt(i) - 'a'
            if (!seen(idx)) {
                seen(idx) = true
                maxUnique += 1
            }
            i += 1
        }

        var answer = 0

        var targetUnique = 1
        while (targetUnique <= maxUnique) {
            val freq = new Array[Int](26)
            var start = 0
            var end = 0
            var unique = 0
            var countAtLeastK = 0

            while (end < n) {
                // expand window
                val idxEnd = s.charAt(end) - 'a'
                if (freq(idxEnd) == 0) unique += 1
                freq(idxEnd) += 1
                if (freq(idxEnd) == k) countAtLeastK += 1

                // shrink window if too many unique chars
                while (unique > targetUnique) {
                    val idxStart = s.charAt(start) - 'a'
                    if (freq(idxStart) == k) countAtLeastK -= 1
                    freq(idxStart) -= 1
                    if (freq(idxStart) == 0) unique -= 1
                    start += 1
                }

                // update answer if valid
                if (unique == targetUnique && unique == countAtLeastK) {
                    val len = end - start + 1
                    if (len > answer) answer = len
                }
                end += 1
            }

            targetUnique += 1
        }

        answer
    }
}
```

## Rust

```rust
use std::cmp::max;

impl Solution {
    pub fn longest_substring(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return 0;
        }
        let k_usize = k as usize;

        // total distinct characters in the whole string
        let mut total_freq = [0usize; 26];
        for &b in bytes {
            total_freq[(b - b'a') as usize] += 1;
        }
        let max_unique = total_freq.iter().filter(|&&c| c > 0).count();

        let mut result = 0usize;

        for target_unique in 1..=max_unique {
            let mut freq = [0usize; 26];
            let (mut start, mut end) = (0usize, 0usize);
            let (mut unique, mut count_at_least_k) = (0usize, 0usize);

            while end < n {
                let idx = (bytes[end] - b'a') as usize;
                if freq[idx] == 0 {
                    unique += 1;
                }
                freq[idx] += 1;
                if freq[idx] == k_usize {
                    count_at_least_k += 1;
                }

                while unique > target_unique {
                    let idx2 = (bytes[start] - b'a') as usize;
                    if freq[idx2] == k_usize {
                        count_at_least_k -= 1;
                    }
                    freq[idx2] -= 1;
                    if freq[idx2] == 0 {
                        unique -= 1;
                    }
                    start += 1;
                }

                if unique == target_unique && unique == count_at_least_k {
                    result = max(result, end - start + 1);
                }

                end += 1;
            }
        }

        result as i32
    }
}
```

## Racket

```racket
(define/contract (longest-substring s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length s))
         ;; number of distinct characters in the whole string
         (max-unique
          (let ((seen (make-vector 26 #f)))
            (let loop ((i 0) (cnt 0))
              (if (= i n)
                  cnt
                  (let ((idx (- (char->integer (string-ref s i))
                                (char->integer #\a))))
                    (if (vector-ref seen idx)
                        (loop (+ i 1) cnt)
                        (begin
                          (vector-set! seen idx #t)
                          (loop (+ i 1) (+ cnt 1))))))))))
    ;; try each possible number of unique characters in the window
    (let outer ((target 1) (best 0))
      (if (> target max-unique)
          best
          (let* ((counts (make-vector 26 0))
                 (window-start 0)
                 (window-end 0)
                 (unique 0)
                 (at-least-k 0)
                 (best-local best))
            (let inner ()
              (when (< window-end n)
                (let ((idx (- (char->integer (string-ref s window-end))
                              (char->integer #\a))))
                  (when (= (vector-ref counts idx) 0)
                    (set! unique (+ unique 1)))
                  (vector-set! counts idx (+ (vector-ref counts idx) 1))
                  (when (= (vector-ref counts idx) k)
                    (set! at-least-k (+ at-least-k 1))))
                (set! window-end (+ window-end 1))
                ;; shrink the window if we have too many unique chars
                (let shrink ()
                  (when (> unique target)
                    (let ((idx2 (- (char->integer (string-ref s window-start))
                                   (char->integer #\a))))
                      (when (= (vector-ref counts idx2) k)
                        (set! at-least-k (- at-least-k 1)))
                      (vector-set! counts idx2 (- (vector-ref counts idx2) 1))
                      (when (= (vector-ref counts idx2) 0)
                        (set! unique (- unique 1))))
                    (set! window-start (+ window-start 1))
                    (shrink)))
                ;; update answer if current window is valid
                (when (and (= unique target) (= at-least-k target))
                  (set! best-local (max best-local (- window-end window-start))))
                (inner)))
            (outer (+ target 1) best-local))))))
```

## Erlang

```erlang
-spec longest_substring(S :: unicode:unicode_binary(), K :: integer()) -> integer().
longest_substring(S, K) ->
    Chars = binary_to_list(S),
    Tuple = list_to_tuple(Chars),
    N = tuple_size(Tuple),
    MaxUnique = length(lists:usort(Chars)),
    longest_substring_loop(1, MaxUnique, Tuple, N, K, 0).

%% iterate over possible numbers of unique characters
longest_substring_loop(Cur, MaxU, _Tuple, _N, _K, Ans) when Cur > MaxU ->
    Ans;
longest_substring_loop(Cur, MaxU, Tuple, N, K, Ans) ->
    Len = sliding_window(Tuple, N, K, Cur),
    NewAns = erlang:max(Ans, Len),
    longest_substring_loop(Cur + 1, MaxU, Tuple, N, K, NewAns).

%% sliding window for a fixed target number of unique characters
sliding_window(Tuple, N, K, TargetU) ->
    sliding_window(Tuple, N, K, TargetU, 0, 0, #{}, 0, 0, 0).

%% recursion over the right pointer
sliding_window(_Tuple, N, _K, _TargetU, _L, R, _Counts, _U, _AK, MaxLen) when R == N ->
    MaxLen;
sliding_window(Tuple, N, K, TargetU, L, R, Counts, U, AK, MaxLen) ->
    C = element(R + 1, Tuple),
    Idx = C - $a,
    PrevCnt = maps:get(Idx, Counts, 0),
    NewCnt = PrevCnt + 1,
    Counts1 = maps:put(Idx, NewCnt, Counts),
    U1 = case PrevCnt of
            0 -> U + 1;
            _ -> U
         end,
    AK1 = case NewCnt of
             K -> AK + 1;
             _ -> AK
          end,
    {L1, Counts2, U2, AK2} = shrink(L, R, TargetU, Counts1, U1, AK1, Tuple, K),
    MaxLen1 = case (U2 == TargetU) andalso (U2 == AK2) of
                  true -> erlang:max(MaxLen, R - L1 + 1);
                  false -> MaxLen
              end,
    sliding_window(Tuple, N, K, TargetU, L1, R + 1, Counts2, U2, AK2, MaxLen1).

%% shrink left side while unique count exceeds target
shrink(L, R, TargetU, Counts, U, AK, Tuple, K) when U =< TargetU ->
    {L, Counts, U, AK};
shrink(L, R, TargetU, Counts, U, AK, Tuple, K) ->
    Cleft = element(L + 1, Tuple),
    IdxL = Cleft - $a,
    PrevCntL = maps:get(IdxL, Counts),
    NewCntL = PrevCntL - 1,
    CountsTmp = case NewCntL of
                    0 -> maps:remove(IdxL, Counts);
                    _ -> maps:put(IdxL, NewCntL, Counts)
                end,
    U2 = case PrevCntL of
            1 -> U - 1;
            _ -> U
         end,
    AK2 = case PrevCntL of
             K -> AK - 1;
             _ -> AK
          end,
    shrink(L + 1, R, TargetU, CountsTmp, U2, AK2, Tuple, K).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_substring(s :: String.t(), k :: integer()) :: integer()
  def longest_substring(s, k) do
    len = byte_size(s)

    if k <= 1 do
      len
    else
      bytes = :binary.bin_to_list(s)
      max_unique = MapSet.size(Enum.into(bytes, MapSet.new()))
      tuple = List.to_tuple(bytes)

      Enum.reduce(1..max_unique, 0, fn target, acc ->
        best = longest_for_target(tuple, len, k, target)
        if best > acc, do: best, else: acc
      end)
    end
  end

  defp longest_for_target(tuple, len, k, target) do
    loop(0, 0, 0, 0, %{}, 0, tuple, len, k, target)
  end

  defp loop(_left, _right, _unique, _at_least_k, _counts, best, _tuple, len, _k, _target) when _right == len do
    best
  end

  defp loop(left, right, unique, at_least_k, counts, best, tuple, len, k, target) do
    ch = elem(tuple, right)
    {unique1, at_least_k1, counts1} = add_char(ch, unique, at_least_k, counts, k)

    {left2, unique2, at_least_k2, counts2} =
      shrink(left, unique1, at_least_k1, counts1, tuple, target, k)

    best2 =
      if unique2 == target && at_least_k2 == target do
        cur_len = right - left2 + 1
        if cur_len > best, do: cur_len, else: best
      else
        best
      end

    loop(left2, right + 1, unique2, at_least_k2, counts2, best2, tuple, len, k, target)
  end

  defp add_char(ch, unique, at_least_k, counts, k) do
    prev = Map.get(counts, ch, 0)
    new = prev + 1
    counts = Map.put(counts, ch, new)

    unique =
      if prev == 0 do
        unique + 1
      else
        unique
      end

    at_least_k =
      if new == k do
        at_least_k + 1
      else
        at_least_k
      end

    {unique, at_least_k, counts}
  end

  defp remove_char(ch, unique, at_least_k, counts, k) do
    prev = Map.get(counts, ch)
    new = prev - 1

    at_least_k =
      if prev == k do
        at_least_k - 1
      else
        at_least_k
      end

    {unique, at_least_k, counts} =
      if new == 0 do
        {unique - 1, at_least_k, Map.delete(counts, ch)}
      else
        {unique, at_least_k, Map.put(counts, ch, new)}
      end

    {unique, at_least_k, counts}
  end

  defp shrink(left, unique, at_least_k, counts, tuple, target, k) do
    if unique <= target do
      {left, unique, at_least_k, counts}
    else
      ch = elem(tuple, left)
      {unique1, at_least_k1, counts1} = remove_char(ch, unique, at_least_k, counts, k)
      shrink(left + 1, unique1, at_least_k1, counts1, tuple, target, k)
    end
  end
end
```
