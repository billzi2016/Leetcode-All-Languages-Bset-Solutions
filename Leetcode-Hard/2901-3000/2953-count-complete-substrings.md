# 2953. Count Complete Substrings

## Cpp

```cpp
class Solution {
public:
    int countCompleteSubstrings(string word, int k) {
        int n = word.size();
        vector<int> a(n);
        for (int i = 0; i < n; ++i) a[i] = word[i] - 'a';
        if (n == 0) return 0;
        vector<int> diff(max(0, n - 1));
        for (int i = 0; i + 1 < n; ++i) diff[i] = abs(a[i] - a[i + 1]);

        long long ans = 0;
        int cnt[26];
        for (int m = 1; m <= 26; ++m) {
            long long Lll = 1LL * m * k;
            if (Lll > n) break;
            int L = (int)Lll;

            memset(cnt, 0, sizeof(cnt));
            int good = 0;      // letters with count == k
            int invalid = 0;   // letters with count >0 && count != k

            auto addChar = [&](int ch) {
                int old = cnt[ch];
                int nw = old + 1;
                cnt[ch] = nw;
                if (old == 0) {
                    if (nw == k) ++good;
                    else ++invalid;
                } else {
                    if (old == k) { --good; ++invalid; }
                    else {
                        if (nw == k) { --invalid; ++good; }
                    }
                }
            };
            auto removeChar = [&](int ch) {
                int old = cnt[ch];
                int nw = old - 1;
                cnt[ch] = nw;
                if (old == k) {
                    --good;
                    if (nw != 0) ++invalid;
                } else { // old != k, and old > 0
                    if (nw == 0) {
                        --invalid;
                    } else {
                        if (nw == k) { --invalid; ++good; }
                    }
                }
            };

            deque<int> dq; // indices of diff with decreasing values

            for (int i = 0; i < L; ++i) addChar(a[i]);
            for (int i = 0; i + 1 < L; ++i) {
                while (!dq.empty() && diff[dq.back()] <= diff[i]) dq.pop_back();
                dq.push_back(i);
            }

            int l = 0;
            while (true) {
                if (good == m && invalid == 0) {
                    int maxDiff = dq.empty() ? 0 : diff[dq.front()];
                    if (maxDiff <= 2) ++ans;
                }
                if (l + L >= n) break; // no further window
                // slide window by one
                removeChar(a[l]);
                ++l;
                int newR = l + L - 1;
                addChar(a[newR]);

                while (!dq.empty() && dq.front() < l) dq.pop_front();
                int idx = newR - 1; // new diff index entering window
                if (idx >= 0) {
                    while (!dq.empty() && diff[dq.back()] <= diff[idx]) dq.pop_back();
                    dq.push_back(idx);
                }
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int countCompleteSubstrings(String word, int k) {
        int n = word.length();
        char[] w = word.toCharArray();
        int[] diff = new int[n];
        for (int i = 1; i < n; i++) {
            diff[i] = Math.abs(w[i] - w[i - 1]);
        }
        long ans = 0;
        for (int m = 1; m <= 26; m++) {
            int len = k * m;
            if (len > n) break;

            int[] cnt = new int[26];
            int distinct = 0, exactK = 0;
            java.util.Deque<Integer> dq = new java.util.ArrayDeque<>();

            // initial window counts
            for (int i = 0; i < len; i++) {
                int idx = w[i] - 'a';
                int prev = cnt[idx];
                cnt[idx]++;
                if (prev == 0) distinct++;
                if (cnt[idx] == k) exactK++;
                if (prev == k) exactK--;
            }

            // initial diffs
            if (len > 1) {
                for (int i = 1; i < len; i++) {
                    while (!dq.isEmpty() && diff[dq.peekLast()] <= diff[i]) dq.pollLast();
                    dq.addLast(i);
                }
            }

            // check first window
            if (distinct == m && exactK == m) {
                int maxDiff = (len > 1 && !dq.isEmpty()) ? diff[dq.peekFirst()] : 0;
                if (maxDiff <= 2) ans++;
            }

            for (int start = 1; start + len - 1 < n; start++) {
                // remove left char
                int outIdx = w[start - 1] - 'a';
                int prevOut = cnt[outIdx];
                cnt[outIdx]--;
                if (cnt[outIdx] == 0) distinct--;
                if (prevOut == k) exactK--;
                if (cnt[outIdx] == k) exactK++;

                // add right char
                int inIdx = w[start + len - 1] - 'a';
                int prevIn = cnt[inIdx];
                cnt[inIdx]++;
                if (prevIn == 0) distinct++;
                if (cnt[inIdx] == k) exactK++;
                if (prevIn == k) exactK--;

                // update diffs
                if (len > 1) {
                    // remove diff at index start (old start+1)
                    while (!dq.isEmpty() && dq.peekFirst() <= start) dq.pollFirst();
                    int newDiffIdx = start + len - 1;
                    if (newDiffIdx < n) {
                        while (!dq.isEmpty() && diff[dq.peekLast()] <= diff[newDiffIdx]) dq.pollLast();
                        dq.addLast(newDiffIdx);
                    }
                }

                // check current window
                if (distinct == m && exactK == m) {
                    int maxDiff = (len > 1 && !dq.isEmpty()) ? diff[dq.peekFirst()] : 0;
                    if (maxDiff <= 2) ans++;
                }
            }
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def countCompleteSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        n = len(word)
        # precompute absolute differences between consecutive characters
        diff = [0] * n
        for i in range(1, n):
            diff[i] = abs(ord(word[i]) - ord(word[i - 1]))

        ans = 0

        for distinct in range(1, 27):          # number of different letters in the substring
            L = distinct * k                   # required length
            if L > n:
                break

            freq = [0] * 26
            bad = 0                             # count of letters whose frequency is NOT 0 nor k

            def update(idx, delta):
                nonlocal bad
                before = freq[idx]
                after = before + delta
                before_good = (before == 0 or before == k)
                after_good = (after == 0 or after == k)
                if before_good and not after_good:
                    bad += 1
                elif not before_good and after_good:
                    bad -= 1
                freq[idx] = after

            # initialise first window [0, L-1]
            for i in range(L):
                update(ord(word[i]) - 97, 1)

            from collections import deque
            dq = deque()
            if L > 1:
                for i in range(1, L):
                    while dq and diff[i] >= diff[dq[-1]]:
                        dq.pop()
                    dq.append(i)

            # check first window
            max_diff = diff[dq[0]] if dq else 0
            if max_diff <= 2 and bad == 0:
                ans += 1

            # slide the window
            for start in range(1, n - L + 1):
                # remove left character
                update(ord(word[start - 1]) - 97, -1)
                # add right character
                update(ord(word[start + L - 1]) - 97, 1)

                if L > 1:
                    out_idx = start          # diff that leaves the window
                    if dq and dq[0] == out_idx:
                        dq.popleft()
                    in_idx = start + L - 1   # new diff entering the window
                    while dq and diff[in_idx] >= diff[dq[-1]]:
                        dq.pop()
                    dq.append(in_idx)

                max_diff = diff[dq[0]] if dq else 0
                if max_diff <= 2 and bad == 0:
                    ans += 1

        return ans
```

## Python3

```python
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        a = [ord(c) - 97 for c in word]
        ans = 0

        # helper to verify window condition
        def window_is_complete(cnt, distinct_needed):
            full = 0
            for v in cnt:
                if v == k:
                    full += 1
                elif v != 0:
                    return False
            return full == distinct_needed

        for distinct in range(1, 27):
            length = distinct * k
            if length > n:
                break

            cnt = [0] * 26
            # initial window
            for i in range(length):
                cnt[a[i]] += 1

            if window_is_complete(cnt, distinct):
                ans += 1

            # slide the window
            for right in range(length, n):
                left_idx = a[right - length]
                cnt[left_idx] -= 1
                cnt[a[right]] += 1
                if window_is_complete(cnt, distinct):
                    ans += 1

        return ans
```

## C

```c
#include <string.h>
#include <stdlib.h>

int countCompleteSubstrings(char* word, int k) {
    int n = strlen(word);
    if (k > n) return 0;

    int *diff = NULL;
    if (n >= 2) {
        diff = (int *)malloc(sizeof(int) * (n - 1));
        for (int i = 0; i < n - 1; ++i)
            diff[i] = abs(word[i] - word[i + 1]);
    }

    long long ans = 0;
    static int dq[200005];   // enough for all possible n

    for (int m = 1; m <= 26; ++m) {
        long long lenLL = (long long)m * k;
        if (lenLL > n) break;
        int L = (int)lenLL;

        int cnt[26] = {0};
        int bad = 0;

        // initial window counts
        for (int i = 0; i < L; ++i) {
            int idx = word[i] - 'a';
            int before = cnt[idx];
            if (before != 0 && before != k) --bad;
            ++cnt[idx];
            int after = cnt[idx];
            if (after != 0 && after != k) ++bad;
        }

        // deque for maximum diff in window
        int head = 0, tail = 0;
        if (L >= 2) {
            for (int i = 0; i < L - 1; ++i) {   // diff indices [0, L-2]
                while (head < tail && diff[dq[tail - 1]] <= diff[i]) --tail;
                dq[tail++] = i;
            }
        }

        int maxDiff = (head < tail) ? diff[dq[head]] : 0;
        if (bad == 0 && (L < 2 || maxDiff <= 2)) ++ans;

        // slide the window
        for (int start = 1; start + L - 1 < n; ++start) {
            // remove left character
            int idx = word[start - 1] - 'a';
            int before = cnt[idx];
            if (before != 0 && before != k) --bad;
            --cnt[idx];
            int after = cnt[idx];
            if (after != 0 && after != k) ++bad;

            // add right character
            idx = word[start + L - 1] - 'a';
            before = cnt[idx];
            if (before != 0 && before != k) --bad;
            ++cnt[idx];
            after = cnt[idx];
            if (after != 0 && after != k) ++bad;

            // update deque for diffs
            if (L >= 2) {
                int outIdx = start - 1;               // leaving diff index
                if (head < tail && dq[head] == outIdx) ++head;
                int newIdx = start + L - 2;           // entering diff index
                while (head < tail && diff[dq[tail - 1]] <= diff[newIdx]) --tail;
                dq[tail++] = newIdx;
                maxDiff = diff[dq[head]];
            } else {
                maxDiff = 0;
            }

            if (bad == 0 && maxDiff <= 2) ++ans;
        }
    }

    free(diff);
    return (int)ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int CountCompleteSubstrings(string word, int k) {
        int n = word.Length;
        if (k > n) return 0;
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = word[i] - 'a';
        
        // adjacency bad array and prefix sums
        int[] adjBad = new int[n];
        for (int i = 1; i < n; i++) {
            adjBad[i] = Math.Abs(a[i] - a[i - 1]) > 2 ? 1 : 0;
        }
        int[] pref = new int[n];
        pref[0] = 0;
        for (int i = 1; i < n; i++) {
            pref[i] = pref[i - 1] + adjBad[i];
        }

        long ans = 0;
        int[] cnt = new int[26];

        for (int distinct = 1; distinct <= 26; distinct++) {
            long lenLong = (long)k * distinct;
            if (lenLong > n) break;
            int len = (int)lenLong;

            Array.Clear(cnt, 0, 26);
            int bad = 0;

            // helper to adjust bad count when a character's frequency changes
            void Adjust(int idx, int delta) {
                int prev = cnt[idx];
                int now = prev + delta;
                bool prevBad = (prev != 0 && prev != k);
                bool nowBad = (now != 0 && now != k);
                if (prevBad && !nowBad) bad--;
                else if (!prevBad && nowBad) bad++;
                cnt[idx] = now;
            }

            // initialize first window
            for (int i = 0; i < len; i++) {
                Adjust(a[i], 1);
            }
            int diffBad = pref[len - 1]; // sum of adjBad from 1 to len-1
            if (bad == 0 && diffBad == 0) ans++;

            // slide window
            for (int start = 1; start + len - 1 < n; start++) {
                Adjust(a[start - 1], -1);               // remove left char
                Adjust(a[start + len - 1], 1);          // add right char
                diffBad = pref[start + len - 1] - pref[start];
                if (bad == 0 && diffBad == 0) ans++;
            }
        }

        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var countCompleteSubstrings = function(word, k) {
    const n = word.length;
    const codes = new Array(n);
    for (let i = 0; i < n; ++i) codes[i] = word.charCodeAt(i) - 97;

    // goodAdj[i] == true if pair (i-1,i) satisfies condition, for i >= 1
    const goodAdj = new Array(n).fill(true);
    for (let i = 1; i < n; ++i) {
        goodAdj[i] = Math.abs(codes[i] - codes[i - 1]) <= 2;
    }

    let answer = 0;

    // try each possible number of distinct letters d (1..26)
    for (let d = 1; d <= 26; ++d) {
        const L = d * k;
        if (L > n) break;

        const cnt = new Array(26).fill(0);
        let badCount = 0; // number of letters with count !=0 && count !=k
        let badAdj = 0;   // number of adjacent pairs violating the diff condition

        const upd = (idx, delta) => {
            const prev = cnt[idx];
            if (prev !== 0 && prev !== k) badCount--;
            const now = prev + delta;
            if (now !== 0 && now !== k) badCount++;
            cnt[idx] = now;
        };

        // initial window [0, L-1]
        for (let i = 0; i < L; ++i) upd(codes[i], 1);
        for (let i = 1; i < L; ++i) if (!goodAdj[i]) badAdj++;

        if (badCount === 0 && badAdj === 0) answer++;

        // slide the window
        for (let start = 1; start + L <= n; ++start) {
            // remove leftmost character at position start-1
            upd(codes[start - 1], -1);
            // add new rightmost character at position start+L-1
            const newPos = start + L - 1;
            upd(codes[newPos], 1);

            // adjust badAdj: pair leaving is (start-1, start) -> index start
            if (!goodAdj[start]) badAdj--;
            // pair entering is (newPos-1, newPos) -> index newPos
            if (!goodAdj[newPos]) badAdj++;

            if (badCount === 0 && badAdj === 0) answer++;
        }
    }

    return answer;
};
```

## Typescript

```typescript
function countCompleteSubstrings(word: string, k: number): number {
    const n = word.length;
    const chars = new Array(n);
    for (let i = 0; i < n; i++) chars[i] = word.charCodeAt(i) - 97;

    const diff = new Array(n).fill(0);
    for (let i = 1; i < n; i++) diff[i] = Math.abs(chars[i] - chars[i - 1]);

    let ans = 0;

    for (let d = 1; d <= 26; d++) {
        const len = d * k;
        if (len > n) break;

        const freq = new Array(26).fill(0);
        let good = 0; // letters with count exactly k
        let over = 0; // letters with count > k

        // initial window frequencies
        for (let i = 0; i < len; i++) {
            const c = chars[i];
            const prev = freq[c];
            freq[c]++;
            if (prev === k - 1) good++;
            else if (prev === k) { good--; over++; }
        }

        // monotonic deque for max diff in window
        let deque: number[] = [];
        let head = 0;
        for (let i = 1; i < len; i++) {
            while (deque.length > head && diff[deque[deque.length - 1]] <= diff[i]) deque.pop();
            deque.push(i);
        }
        const maxDiff = () => (deque.length > head ? diff[deque[head]] : 0);

        if (over === 0 && good === d && maxDiff() <= 2) ans++;

        for (let l = 0; l + len < n; l++) {
            // remove left character
            const outC = chars[l];
            const prevOut = freq[outC];
            freq[outC]--;
            if (prevOut === k) {
                good--;
            } else if (prevOut === k + 1) {
                over--;
                good++;
            }

            // add right character
            const inC = chars[l + len];
            const prevIn = freq[inC];
            freq[inC]++;
            if (prevIn === k - 1) {
                good++;
            } else if (prevIn === k) {
                good--;
                over++;
            }

            // update deque: remove diff index l+1
            const remIdx = l + 1;
            if (deque.length > head && deque[head] === remIdx) head++;

            // add new diff index l+len (if within bounds)
            const addIdx = l + len;
            if (addIdx < n) {
                while (deque.length > head && diff[deque[deque.length - 1]] <= diff[addIdx]) deque.pop();
                deque.push(addIdx);
            }

            if (over === 0 && good === d && maxDiff() <= 2) ans++;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param String $word
     * @param Integer $k
     * @return Integer
     */
    function countCompleteSubstrings($word, $k) {
        $n = strlen($word);
        // convert characters to 0-25 indices
        $codes = [];
        for ($i = 0; $i < $n; $i++) {
            $codes[$i] = ord($word[$i]) - 97;
        }
        // precompute where adjacent difference > 2
        $diffBad = array_fill(0, max(0, $n - 1), 0);
        for ($i = 0; $i < $n - 1; $i++) {
            $diffBad[$i] = (abs($codes[$i + 1] - $codes[$i]) > 2) ? 1 : 0;
        }

        $ans = 0;
        for ($m = 1; $m <= 26; $m++) {
            $L = $k * $m;
            if ($L > $n) break;

            // frequency array and bad count
            $cnt = array_fill(0, 26, 0);
            $badCount = 0; // number of letters whose count is neither 0 nor k

            // initialize first window
            for ($i = 0; $i < $L; $i++) {
                $idx = $codes[$i];
                $prev = $cnt[$idx];
                if ($prev == 0) {
                    if ($k != 1) $badCount++;
                } elseif ($prev == $k - 1) {
                    $badCount--;
                } elseif ($prev == $k) {
                    $badCount++;
                }
                $cnt[$idx] = $prev + 1;
            }

            // initialize badDiff (adjacent violations)
            $badDiff = 0;
            if ($L > 1) {
                for ($i = 0; $i < $L - 1; $i++) {
                    $badDiff += $diffBad[$i];
                }
            }

            $maxStart = $n - $L;
            for ($start = 0; $start <= $maxStart; $start++) {
                if ($badCount == 0 && $badDiff == 0) {
                    $ans++;
                }
                if ($start == $maxStart) break;

                // remove left character
                $idx = $codes[$start];
                $prev = $cnt[$idx];
                if ($prev == 1) {
                    if ($k != 1) $badCount--;
                } elseif ($prev == $k) {
                    $badCount++;
                } elseif ($prev == $k + 1) {
                    $badCount--;
                }
                $cnt[$idx] = $prev - 1;

                // add right character
                $newPos = $start + $L;
                $idx = $codes[$newPos];
                $prev = $cnt[$idx];
                if ($prev == 0) {
                    if ($k != 1) $badCount++;
                } elseif ($prev == $k - 1) {
                    $badCount--;
                } elseif ($prev == $k) {
                    $badCount++;
                }
                $cnt[$idx] = $prev + 1;

                // update adjacency violations
                if ($L > 1) {
                    $badDiff -= $diffBad[$start];
                    $badDiff += $diffBad[$start + $L - 1];
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countCompleteSubstrings(_ word: String, _ k: Int) -> Int {
        let chars = Array(word.utf8)
        let n = chars.count
        var answer = 0
        
        for d in 1...26 {
            let length = k * d
            if length > n { break }
            
            var cnt = [Int](repeating: 0, count: 26)
            var good = 0               // letters whose count == k
            var distinct = 0           // letters with count > 0
            
            // initialize first window
            for i in 0..<length {
                let idx = Int(chars[i] - 97)
                let prev = cnt[idx]
                if prev == k { good -= 1 }
                cnt[idx] = prev + 1
                if cnt[idx] == k { good += 1 }
                if prev == 0 { distinct += 1 }
            }
            
            // compute min and max letter indices in current window
            var curMin = 26, curMax = -1
            for j in 0..<26 where cnt[j] > 0 {
                if j < curMin { curMin = j }
                if j > curMax { curMax = j }
            }
            
            if good == distinct && (curMax - curMin + 1) == distinct {
                answer += 1
            }
            
            // slide the window
            if n > length {
                for start in 1...(n - length) {
                    let outIdx = Int(chars[start - 1] - 97)
                    var prev = cnt[outIdx]
                    if prev == k { good -= 1 }
                    cnt[outIdx] = prev - 1
                    if cnt[outIdx] == k { good += 1 }
                    if prev == 1 { distinct -= 1 } // became zero
                    
                    let inIdx = Int(chars[start + length - 1] - 97)
                    prev = cnt[inIdx]
                    if prev == k { good -= 1 }
                    cnt[inIdx] = prev + 1
                    if cnt[inIdx] == k { good += 1 }
                    if prev == 0 && cnt[inIdx] > 0 { distinct += 1 }
                    
                    // recompute min and max
                    curMin = 26
                    curMax = -1
                    for j in 0..<26 where cnt[j] > 0 {
                        if j < curMin { curMin = j }
                        if j > curMax { curMax = j }
                    }
                    
                    if good == distinct && (curMax - curMin + 1) == distinct {
                        answer += 1
                    }
                }
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countCompleteSubstrings(word: String, k: Int): Int {
        val n = word.length
        val chars = IntArray(n) { word[it] - 'a' }
        var answer = 0

        for (m in 1..26) {
            val len = m * k
            if (len > n) break

            val cnt = IntArray(26)
            var bad = 0

            // initialize counts for first window
            for (i in 0 until len) {
                val idx = chars[i]
                val before = cnt[idx]
                if (before != 0 && before != k) bad--
                cnt[idx] = before + 1
                val after = cnt[idx]
                if (after != 0 && after != k) bad++
            }

            // diff handling
            val diffCnt = IntArray(26)
            var maxDiff = 0
            if (len > 1) {
                for (i in 1 until len) {
                    val d = kotlin.math.abs(chars[i] - chars[i - 1])
                    diffCnt[d]++
                    if (d > maxDiff) maxDiff = d
                }
            }

            fun isGood(): Boolean = bad == 0 && maxDiff <= 2

            if (isGood()) answer++

            var left = 0
            for (right in len until n) {
                // remove left character
                val idxRem = chars[left]
                var beforeRem = cnt[idxRem]
                if (beforeRem != 0 && beforeRem != k) bad--
                cnt[idxRem] = beforeRem - 1
                val afterRem = cnt[idxRem]
                if (afterRem != 0 && afterRem != k) bad++

                // remove diff at left boundary
                if (len > 1) {
                    val dRem = kotlin.math.abs(chars[left + 1] - chars[left])
                    diffCnt[dRem]--
                    if (diffCnt[dRem] == 0 && dRem == maxDiff) {
                        while (maxDiff > 0 && diffCnt[maxDiff] == 0) maxDiff--
                    }
                }

                // add right character
                val idxAdd = chars[right]
                var beforeAdd = cnt[idxAdd]
                if (beforeAdd != 0 && beforeAdd != k) bad--
                cnt[idxAdd] = beforeAdd + 1
                val afterAdd = cnt[idxAdd]
                if (afterAdd != 0 && afterAdd != k) bad++

                // add diff at right boundary
                if (len > 1) {
                    val dAdd = kotlin.math.abs(chars[right] - chars[right - 1])
                    diffCnt[dAdd]++
                    if (dAdd > maxDiff) maxDiff = dAdd
                }

                left++

                if (isGood()) answer++
            }
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  int countCompleteSubstrings(String word, int k) {
    int n = word.length;
    List<int> chars = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      chars[i] = word.codeUnitAt(i) - 97;
    }
    // precompute diffs between adjacent characters
    List<int> diffs = [];
    if (n > 1) {
      diffs = List.filled(n - 1, 0);
      for (int i = 0; i < n - 1; ++i) {
        diffs[i] = (chars[i + 1] - chars[i]).abs();
      }
    }

    int ans = 0;

    // try each possible number of distinct letters d (1..26)
    for (int d = 1; d <= 26; ++d) {
      int len = d * k;
      if (len > n) break;

      List<int> cnt = List.filled(26, 0);
      int good = 0; // letters with count exactly k
      int over = 0; // letters with count > k

      // monotonic deque for max diff in current window
      List<int> dq = [];

      // initialize first window [0, len)
      for (int i = 0; i < len; ++i) {
        int idx = chars[i];
        cnt[idx]++;
        if (cnt[idx] == k) {
          good++;
        } else if (cnt[idx] == k + 1) {
          good--;
          over++;
        }
      }

      if (len > 1) {
        for (int i = 0; i < len - 1; ++i) {
          int val = diffs[i];
          while (dq.isNotEmpty && diffs[dq.last] <= val) dq.removeLast();
          dq.add(i);
        }
      }

      int maxDiff = dq.isEmpty ? 0 : diffs[dq.first];
      if (maxDiff <= 2 && over == 0 && good == d) ans++;

      // slide the window
      for (int start = 1; start + len - 1 < n; ++start) {
        int leftIdx = start - 1;
        int rightIdx = start + len - 1;

        // remove left character
        int remIdx = chars[leftIdx];
        int prevRem = cnt[remIdx];
        cnt[remIdx]--;
        if (prevRem == k) {
          good--;
        } else if (prevRem == k + 1) {
          over--;
          good++;
        }

        // add right character
        int addIdx = chars[rightIdx];
        cnt[addIdx]++;
        if (cnt[addIdx] == k) {
          good++;
        } else if (cnt[addIdx] == k + 1) {
          good--;
          over++;
        }

        // update diffs deque if window size > 1
        if (len > 1) {
          // remove diff that left the window (index = leftIdx)
          if (dq.isNotEmpty && dq.first == leftIdx) dq.removeAt(0);
          // add new diff at index rightIdx - 1
          int newDiffIdx = rightIdx - 1;
          int val = diffs[newDiffIdx];
          while (dq.isNotEmpty && diffs[dq.last] <= val) dq.removeLast();
          dq.add(newDiffIdx);
          maxDiff = diffs[dq.first];
        } else {
          maxDiff = 0;
        }

        if (maxDiff <= 2 && over == 0 && good == d) ans++;
      }
    }

    return ans;
  }
}
```

## Golang

```go
func countCompleteSubstrings(word string, k int) int {
    n := len(word)
    if n == 0 {
        return 0
    }
    // pre‑compute absolute differences between consecutive characters
    diff := make([]int, n-1)
    for i := 1; i < n; i++ {
        d := int(word[i]) - int(word[i-1])
        if d < 0 {
            d = -d
        }
        diff[i-1] = d
    }

    ans := 0

    // possible number of distinct letters in a complete substring: 1 … 26
    for distinct := 1; distinct <= 26; distinct++ {
        L := distinct * k // required length of the window
        if L > n {
            break
        }

        var freq [26]int
        good := 0 // number of letters whose count equals k

        // initialise first window
        for i := 0; i < L; i++ {
            idx := word[i] - 'a'
            before := freq[idx]
            after := before + 1
            if before == k {
                good--
            }
            if after == k {
                good++
            }
            freq[idx] = after
        }

        type pair struct{ idx, val int }
        dq := []pair{} // monotonic queue for maximum diff in current window

        if L > 1 {
            for i := 0; i <= L-2; i++ { // diff indices covered by the first window
                v := diff[i]
                for len(dq) > 0 && dq[len(dq)-1].val <= v {
                    dq = dq[:len(dq)-1]
                }
                dq = append(dq, pair{i, v})
            }
        }

        // slide the window across the string
        for start := 0; start+L <= n; start++ {
            maxDiff := 0
            if L > 1 && len(dq) > 0 {
                maxDiff = dq[0].val
            }
            if good == distinct && maxDiff <= 2 {
                ans++
            }

            // reached the last window
            if start+L == n {
                break
            }

            // remove character leaving the window
            outIdx := word[start] - 'a'
            before := freq[outIdx]
            after := before - 1
            if before == k {
                good--
            }
            if after == k {
                good++
            }
            freq[outIdx] = after

            // add new character entering the window
            inIdx := word[start+L] - 'a'
            before = freq[inIdx]
            after = before + 1
            if before == k {
                good--
            }
            if after == k {
                good++
            }
            freq[inIdx] = after

            // update monotonic queue for diffs
            if L > 1 {
                outDiffIdx := start
                if len(dq) > 0 && dq[0].idx == outDiffIdx {
                    dq = dq[1:]
                }
                newDiffIdx := start + L - 1
                v := diff[newDiffIdx]
                for len(dq) > 0 && dq[len(dq)-1].val <= v {
                    dq = dq[:len(dq)-1]
                }
                dq = append(dq, pair{newDiffIdx, v})
            }
        }
    }

    return ans
}
```

## Ruby

```ruby
def count_complete_substrings(word, k)
  n = word.length
  chars = word.bytes.map { |b| b - 97 } # 0..25

  diffs = Array.new(n, 0)
  (1...n).each do |i|
    diffs[i] = (chars[i] - chars[i - 1]).abs
  end

  ans = 0
  max_d = [26, n / k].min

  (1..max_d).each do |d|
    len = k * d
    next if len > n

    cnt = Array.new(26, 0)
    bad = 0 # number of letters whose count is neither 0 nor k

    # initialize first window
    (0...len).each do |i|
      c = chars[i]
      prev = cnt[c]
      bad -= 1 if prev != 0 && prev != k
      cnt[c] = prev + 1
      newc = cnt[c]
      bad += 1 if newc != 0 && newc != k
    end

    # deque for max diff in current window (indices s+1 .. e)
    deque = [] # each element [value, index]
    s = 0
    e = len - 1
    ((s + 1)..e).each do |idx|
      val = diffs[idx]
      while !deque.empty? && deque[-1][0] <= val
        deque.pop
      end
      deque << [val, idx]
    end

    ans += 1 if bad == 0 && (deque.empty? || deque[0][0] <= 2)

    while s + len < n
      # remove left char
      c_out = chars[s]
      prev = cnt[c_out]
      bad -= 1 if prev != 0 && prev != k
      cnt[c_out] = prev - 1
      newc = cnt[c_out]
      bad += 1 if newc != 0 && newc != k

      # add right char
      c_in = chars[s + len]
      prev = cnt[c_in]
      bad -= 1 if prev != 0 && prev != k
      cnt[c_in] = prev + 1
      newc = cnt[c_in]
      bad += 1 if newc != 0 && newc != k

      # slide diffs deque
      left_diff_idx = s + 1
      deque.shift while !deque.empty? && deque[0][1] == left_diff_idx

      new_diff_idx = s + len
      if new_diff_idx < n
        val = diffs[new_diff_idx]
        while !deque.empty? && deque[-1][0] <= val
          deque.pop
        end
        deque << [val, new_diff_idx]
      end

      s += 1
      ans += 1 if bad == 0 && (deque.empty? || deque[0][0] <= 2)
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  def countCompleteSubstrings(word: String, k: Int): Int = {
    val n = word.length
    if (n == 0) return 0
    val chars = word.toCharArray
    val diffs = new Array[Int](n)
    var i = 1
    while (i < n) {
      diffs(i) = Math.abs(chars(i) - chars(i - 1))
      i += 1
    }

    var ans: Long = 0L
    import scala.collection.mutable.ArrayDeque

    var d = 1
    while (d <= 26) {
      val len = k * d
      if (len > n) {
        // no more possible lengths for larger d
      } else {
        val freq = new Array[Int](26)
        var j = 0
        while (j < len) {
          freq(chars(j) - 'a') += 1
          j += 1
        }

        var distinct = 0
        var bad = 0
        var c = 0
        while (c < 26) {
          if (freq(c) == k) distinct += 1
          else if (freq(c) != 0) bad += 1
          c += 1
        }

        val dq = new ArrayDeque[(Int, Int)]()
        if (len > 1) {
          var idx = 1
          while (idx < len) {
            val v = diffs(idx)
            while (dq.nonEmpty && dq.last._2 <= v) dq.removeLast()
            dq.append((idx, v))
            idx += 1
          }
        }

        def maxDiff: Int = if (dq.isEmpty) 0 else dq.head._2

        if (bad == 0 && distinct == d && maxDiff <= 2) ans += 1

        var l = 0
        while (l + len < n) {
          // remove left character
          val outIdx = chars(l) - 'a'
          val prevOut = freq(outIdx)
          if (prevOut == k) distinct -= 1
          else if (prevOut != 0 && prevOut != k) {} // nothing extra
          if (prevOut != 0 && prevOut != k) bad -= 1
          freq(outIdx) = prevOut - 1
          val nowOut = freq(outIdx)
          if (nowOut == k) distinct += 1
          else if (nowOut != 0 && nowOut != k) bad += 1

          // add right character
          val inIdx = chars(l + len) - 'a'
          val prevIn = freq(inIdx)
          if (prevIn == k) distinct -= 1
          if (prevIn != 0 && prevIn != k) bad -= 1
          freq(inIdx) = prevIn + 1
          val nowIn = freq(inIdx)
          if (nowIn == k) distinct += 1
          else if (nowIn != 0 && nowIn != k) bad += 1

          // update diff deque
          if (len > 1) {
            while (dq.nonEmpty && dq.head._1 <= l + 1) dq.removeHead()
            val newIdx = l + len
            val v = diffs(newIdx)
            while (dq.nonEmpty && dq.last._2 <= v) dq.removeLast()
            dq.append((newIdx, v))
          }

          if (bad == 0 && distinct == d && maxDiff <= 2) ans += 1

          l += 1
        }
      }
      d += 1
    }

    ans.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_complete_substrings(word: String, k: i32) -> i32 {
        let bytes = word.as_bytes();
        let n = bytes.len();
        if n == 0 { return 0; }
        // precompute absolute differences between consecutive characters
        let mut diff = vec![0usize; n];
        for i in 1..n {
            diff[i] = (bytes[i] as i32 - bytes[i - 1] as i32).abs() as usize;
        }

        let mut answer: i64 = 0;

        // helper closures to update frequency and bad count
        let mut add_char = |freq: &mut [i32; 26], idx: usize, k: i32, bad: &mut i32| {
            let before = freq[idx];
            if before != 0 && before != k {
                *bad -= 1;
            }
            let after = before + 1;
            if after != 0 && after != k {
                *bad += 1;
            }
            freq[idx] = after;
        };
        let mut remove_char = |freq: &mut [i32; 26], idx: usize, k: i32, bad: &mut i32| {
            let before = freq[idx];
            if before != 0 && before != k {
                *bad -= 1;
            }
            let after = before - 1;
            if after != 0 && after != k {
                *bad += 1;
            }
            freq[idx] = after;
        };

        for distinct in 1..=26 {
            let len = k as usize * distinct;
            if len > n {
                break;
            }

            // frequency array and bad counter
            let mut freq = [0i32; 26];
            let mut bad: i32 = 0;

            // initialize first window frequencies
            for i in 0..len {
                let idx = (bytes[i] - b'a') as usize;
                add_char(&mut freq, idx, k, &mut bad);
            }

            // diff multiset (counts) and current max diff
            let mut diff_cnt = [0i32; 27]; // diffs are at most 25
            let mut max_diff: usize = 0;

            if len > 1 {
                for i in 1..len {
                    let d = diff[i];
                    diff_cnt[d] += 1;
                    if d > max_diff {
                        max_diff = d;
                    }
                }
            }

            let mut left: usize = 0;
            while left + len <= n {
                if bad == 0 && max_diff <= 2 {
                    answer += 1;
                }

                // slide window
                if left + len == n {
                    break;
                }

                // remove left character
                let idx_remove = (bytes[left] - b'a') as usize;
                remove_char(&mut freq, idx_remove, k, &mut bad);

                // handle diff leaving the window
                if len > 1 {
                    let out_diff = diff[left + 1];
                    diff_cnt[out_diff] -= 1;
                    if diff_cnt[out_diff] == 0 && max_diff == out_diff {
                        while max_diff > 0 && diff_cnt[max_diff] == 0 {
                            max_diff -= 1;
                        }
                    }

                    // add new right character
                    let idx_add = (bytes[left + len] - b'a') as usize;
                    add_char(&mut freq, idx_add, k, &mut bad);

                    // handle diff entering the window
                    let in_diff = diff[left + len];
                    diff_cnt[in_diff] += 1;
                    if in_diff > max_diff {
                        max_diff = in_diff;
                    }
                } else {
                    // len == 1: only character updates needed, diffs stay empty
                    let idx_add = (bytes[left + len] - b'a') as usize;
                    add_char(&mut freq, idx_add, k, &mut bad);
                }

                left += 1;
            }
        }

        answer as i32
    }
}
```

## Racket

```racket
(define/contract (count-complete-substrings word k)
  (-> string? exact-integer? exact-integer?)
  (let* ([n (string-length word)]
         [codes (make-vector n)]
         [diffs (if (> n 1) (make-vector (- n 1)) #f)])
    ;; fill character codes 0..25
    (for ([i (in-range n)])
      (vector-set! codes i
        (- (char->integer (string-ref word i))
           (char->integer #\a))))
    ;; precompute absolute differences between adjacent characters
    (when (> n 1)
      (for ([i (in-range (- n 1))])
        (let* ([c1 (vector-ref codes i)]
               [c2 (vector-ref codes (+ i 1))]
               [d (abs (- c1 c2))])
          (vector-set! diffs i d))))
    (define ans 0)
    ;; iterate possible number of distinct letters d (1..26)
    (for ([d (in-range 1 27)])
      (let ([len (* k d)])
        (when (<= len n)
          (define counts (make-vector 26 0))
          (define bad 0) ; number of letters whose count is neither 0 nor k
          ;; initialize first window [0, len-1]
          (for ([i (in-range len)])
            (let* ([c (vector-ref codes i)]
                   [old (vector-ref counts c)])
              (when (and (not (= old 0)) (not (= old k))) (set! bad (- bad 1)))
              (vector-set! counts c (+ old 1))
              (let ([new (vector-ref counts c)])
                (when (and (not (= new 0)) (not (= new k))) (set! bad (+ bad 1))))))
          ;; monotonic deque for maximum diff in current window
          (define deq (make-vector n -1))
          (define head 0)
          (define tail 0)
          (when (> len 1)
            (for ([i (in-range (- len 1))])
              (let ([val (vector-ref diffs i)])
                (let loop ()
                  (when (< head tail)
                    (define back-idx (vector-ref deq (- tail 1)))
                    (when (<= (vector-ref diffs back-idx) val)
                      (set! tail (- tail 1))
                      (loop)))))
                (vector-set! deq tail i)
                (set! tail (+ tail 1))))
          ;; check first window
          (let ([maxdiff (if (> len 1) (vector-ref diffs (vector-ref deq head)) 0)])
            (when (and (= bad 0) (<= maxdiff 2))
              (set! ans (+ ans 1))))
          ;; slide the window
          (for ([start (in-range 1 (add1 (- n len)))])
            (let* ([out-idx (- start 1)]
                   [in-idx (+ start len -1)])
              ;; remove outgoing character
              (let* ([c-out (vector-ref codes out-idx)]
                     [old-out (vector-ref counts c-out)])
                (when (and (not (= old-out 0)) (not (= old-out k))) (set! bad (- bad 1)))
                (vector-set! counts c-out (- old-out 1))
                (let ([new-out (vector-ref counts c-out)])
                  (when (and (not (= new-out 0)) (not (= new-out k))) (set! bad (+ bad 1)))))
              ;; add incoming character
              (let* ([c-in (vector-ref codes in-idx)]
                     [old-in (vector-ref counts c-in)])
                (when (and (not (= old-in 0)) (not (= old-in k))) (set! bad (- bad 1)))
                (vector-set! counts c-in (+ old-in 1))
                (let ([new-in (vector-ref counts c-in)])
                  (when (and (not (= new-in 0)) (not (= new-in k))) (set! bad (+ bad 1)))))
              ;; update deque for diffs
              (when (> len 1)
                ;; remove diff at start-1
                (let ([old-diff-idx (- start 1)])
                  (when (and (< head tail) (= (vector-ref deq head) old-diff-idx))
                    (set! head (+ head 1))))
                ;; add new diff at start+len-2
                (let ([new-diff-idx (+ start len -2)])
                  (let ([val (vector-ref diffs new-diff-idx)])
                    (let loop ()
                      (when (< head tail)
                        (define back-idx (vector-ref deq (- tail 1)))
                        (when (<= (vector-ref diffs back-idx) val)
                          (set! tail (- tail 1))
                          (loop))))
                    (vector-set! deq tail new-diff-idx)
                    (set! tail (+ tail 1)))))
              ;; evaluate current window
              (let ([maxdiff (if (> len 1) (vector-ref diffs (vector-ref deq head)) 0)])
                (when (and (= bad 0) (<= maxdiff 2))
                  (set! ans (+ ans 1))))))))
    ans)))
```

## Erlang

```erlang
-spec count_complete_substrings(Word :: unicode:unicode_binary(), K :: integer()) -> integer().
count_complete_substrings(Word, K) ->
    CharList = binary:bin_to_list(Word),
    N = length(CharList),
    % convert characters to 0..25 and store in a tuple for O(1) access
    CharCodes = list_to_tuple([C - $a || C <- CharList]),
    DiffTuple = build_diff_tuple(N, CharCodes),          % index 0 is dummy, 1..N-1 are diffs
    NextBadTuple = build_next_bad_tuple(N, DiffTuple),   % first bad diff index after each position
    MaxM = min(26, N div K),
    count_by_m(1, MaxM, N, K, CharCodes, NextBadTuple).

%% Build tuple of diffs, element 0 is dummy (value 0)
build_diff_tuple(N, CharCodes) ->
    DiffList = build_diff_list(1, N - 1, CharCodes, [0]),
    list_to_tuple(lists:reverse(DiffList)).

build_diff_list(I, MaxI, CharCodes, Acc) when I =< MaxI ->
    CPrev = element(I, CharCodes),
    CCur  = element(I + 1, CharCodes),
    D = abs(CCur - CPrev),
    build_diff_list(I + 1, MaxI, CharCodes, [D | Acc]);
build_diff_list(_, _, _, Acc) -> Acc.

%% Build tuple NextBad where NextBad[i] (0‑based) is the smallest index j>i
%% such that diff[j] > 2; if none, value = N.
build_next_bad_tuple(N, DiffTuple) ->
    build_next_bad(N - 1, DiffTuple, N, [], N).

build_next_bad(-1, _, _, Acc, _) -> list_to_tuple(lists:reverse(Acc));
build_next_bad(I, DiffTuple, Next, Acc, N) ->
    Bad = if
        I + 1 < N andalso element(I + 1, DiffTuple) > 2 -> I + 1;
        true -> Next
    end,
    build_next_bad(I - 1, DiffTuple, Bad, [Bad | Acc], N).

%% Iterate over possible numbers of distinct letters (m)
count_by_m(M, MaxM, N, K, CharCodes, NextBad) when M =< MaxM ->
    L = M * K,
    Added = count_windows(N, L, K, CharCodes, NextBad),
    count_by_m(M + 1, MaxM, N, K, CharCodes, NextBad) + Added;
count_by_m(_, _, _, _, _, _) -> 0.

%% Count valid windows of fixed length L
count_windows(N, L, _K, _CharCodes, _NextBad) when L > N ->
    0;
count_windows(_N, 1, K, _CharCodes, _NextBad) ->
    % every single character forms a complete substring when K = 1
    case K of
        1 -> erlang:system_info(wordsize); % placeholder to avoid unused var warning
        _ -> 0
    end;
count_windows(N, L, K, CharCodes, NextBad) ->
    {Map0, Inv0} = init_counts(0, L - 1, #{}, 0, K, CharCodes),
    loop_windows(0, N - L, L, K, CharCodes, NextBad, Map0, Inv0, 0).

init_counts(I, End, Map, Invalid, _K, _CharCodes) when I > End ->
    {Map, Invalid};
init_counts(I, End, Map, Invalid, K, CharCodes) ->
    C = element(I + 1, CharCodes),
    {Map1, Inv1} = update_count(Map, C, 1, K, Invalid),
    init_counts(I + 1, End, Map1, Inv1, K, CharCodes).

loop_windows(S, MaxS, L, K, CharCodes, NextBad, Map, Invalid, Acc) when S =< MaxS ->
    EndIdx = S + L - 1,
    CondFreq = (Invalid == 0),
    NextBadPos = element(S + 1, NextBad),   % tuple is 1‑based
    CondDiff = EndIdx < NextBadPos,
    NewAcc = if CondFreq andalso CondDiff -> Acc + 1; true -> Acc end,
    case S < MaxS of
        true ->
            CharOut = element(S + 1, CharCodes),
            CharIn  = element(EndIdx + 2, CharCodes), % (EndIdx+1) in 0‑based => +2 for tuple index
            {Map1, Inv1} = update_count(Map, CharOut, -1, K, Invalid),
            {Map2, Inv2} = update_count(Map1, CharIn, 1, K, Inv1),
            loop_windows(S + 1, MaxS, L, K, CharCodes, NextBad, Map2, Inv2, NewAcc);
        false ->
            NewAcc
    end;
loop_windows(_, _, _, _, _, _, _, _, Acc) -> Acc.

%% Update count map and maintain number of invalid letters
update_count(Map, Char, Delta, K, Invalid) ->
    Prev = maps:get(Char, Map, 0),
    New = Prev + Delta,
    WasInvalid = (Prev > 0 andalso Prev /= K),
    NowInvalid = (New > 0 andalso New /= K),
    Inv1 = Invalid - (if WasInvalid -> 1; true -> 0 end) +
                     (if NowInvalid -> 1; true -> 0 end),
    Map1 = case New of
        0 -> maps:remove(Char, Map);
        _ -> maps:put(Char, New, Map)
    end,
    {Map1, Inv1}.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_complete_substrings(word :: String.t(), k :: integer) :: integer
  def count_complete_substrings(word, k) do
    chars = :binary.bin_to_list(word) |> List.to_tuple()
    n = tuple_size(chars)

    # precompute adjacency violations: diff[i] = 1 if |s[i]-s[i-1]| > 2 else 0 (i>=1)
    diffs =
      0..(n - 1)
      |> Enum.map(fn i ->
        if i == 0 do
          0
        else
          a = :erlang.element(i + 1, chars)
          b = :erlang.element(i, chars)
          if abs(a - b) > 2, do: 1, else: 0
        end
      end)
      |> List.to_tuple()

    total =
      Enum.reduce(1..26, 0, fn t, acc_total ->
        l = k * t
        if l > n do
          acc_total
        else
          # initialize frequency tuple and good/bad counters
          {freq, good, badc} = init_window(chars, l, k)

          # initial adjacency violations count in window [0, l-1]
          bad_adj =
            1..(l - 1)
            |> Enum.reduce(0, fn i, sum -> sum + :erlang.element(i + 1, diffs) end)

          acc_total = if badc == 0 and bad_adj == 0, do: acc_total + 1, else: acc_total

          max_start = n - l

          {_, _, _, _, final_total} =
            Enum.reduce(1..max_start, {freq, good, badc, bad_adj, acc_total}, fn s,
                                                                                 {f, g, b, ba,
                                                                                  tot} ->
              out_idx = :erlang.element(s, chars) - ?a
              {f, g, b} = dec_update(f, out_idx, g, b, k)

              in_idx = :erlang.element(s + l, chars) - ?a
              {f, g, b} = inc_update(f, in_idx, g, b, k)

              ba = ba - :erlang.element(s + 1, diffs) + :erlang.element(s + l + 1, diffs)
              tot = if b == 0 and ba == 0, do: tot + 1, else: tot
              {f, g, b, ba, tot}
            end)

          final_total
        end
      end)

    total
  end

  # Initialize frequency tuple for the first window of length l
  defp init_window(chars, l, k) do
    freq = :erlang.make_tuple(26, 0)
    good = 0
    badc = 0

    Enum.reduce(0..(l - 1), {freq, good, badc}, fn i, {f, g, b} ->
      idx = :erlang.element(i + 1, chars) - ?a
      inc_update(f, idx, g, b, k)
    end)
  end

  # Increment count of character at idx
  defp inc_update(freq, idx, good, bad, k) do
    old = :erlang.element(idx + 1, freq)
    new = old + 1
    freq = :erlang.setelement(idx + 1, freq, new)
    {good, bad} = adjust_counts(old, new, k, good, bad)
    {freq, good, bad}
  end

  # Decrement count of character at idx
  defp dec_update(freq, idx, good, bad, k) do
    old = :erlang.element(idx + 1, freq)
    new = old - 1
    freq = :erlang.setelement(idx + 1, freq, new)
    {good, bad} = adjust_counts(old, new, k, good, bad)
    {freq, good, bad}
  end

  # Update good/bad counters based on transition from old count to new count
  defp adjust_counts(old, new, k, good, bad) do
    cond do
      old == 0 ->
        if new == k, do: {good + 1, bad}, else: {good, bad + 1}

      old == k ->
        # was a good count
        if new == 0, do: {good - 1, bad}, else: {good - 1, bad + 1}

      true ->
        # old was neither 0 nor k (bad)
        if new == 0 or new == k do
          bad = bad - 1
          good = if new == k, do: good + 1, else: good
          {good, bad}
        else
          {good, bad}
        end
    end
  end
end
```
