# 2468. Split Message Based on Limit

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> splitMessage(string message, int limit) {
        int n = (int)message.size();
        const int INF = 1e9;
        int bestB = INF;
        int pow10[7];
        pow10[0] = 1;
        for (int i = 1; i <= 6; ++i) pow10[i] = pow10[i-1]*10;

        for (int lenB = 1; lenB <= 5; ++lenB) {
            // each part must be able to contain the suffix with max digits
            if (limit < 2*lenB + 3) continue; // cannot fit "<a/b>"
            int low = max(1, pow10[lenB-1]);
            int high = min(pow10[lenB]-1, n); // never need more parts than characters
            if (low > high) continue;

            auto capacity = [&](int b)->long long {
                long long sumDigits = 0;
                for (int d = 1; d <= lenB; ++d) {
                    int l = max(pow10[d-1], 1);
                    int r = min(b, pow10[d]-1);
                    if (l > r) continue;
                    sumDigits += 1LL * (r - l + 1) * d;
                }
                long long cap = 1LL * b * (limit - lenB - 3) - sumDigits;
                return cap;
            };

            int lo = low, hi = high, ans = -1;
            while (lo <= hi) {
                int mid = (lo + hi) / 2;
                if (capacity(mid) >= n) {
                    ans = mid;
                    hi = mid - 1;
                } else {
                    lo = mid + 1;
                }
            }
            if (ans != -1 && ans < bestB) bestB = ans;
        }

        if (bestB == INF) return {};

        vector<string> res;
        int idx = 0;
        for (int i = 1; i <= bestB; ++i) {
            string suffix = "<" + to_string(i) + "/" + to_string(bestB) + ">";
            int allowed = limit - (int)suffix.size();
            int take = min(allowed, n - idx);
            string part = message.substr(idx, take) + suffix;
            res.push_back(part);
            idx += take;
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String[] splitMessage(String message, int limit) {
        int n = message.length();
        // Upper bound on parts is n (at least one character per part)
        for (int b = 1; b <= n; b++) {
            int digitsB = digitCount(b);
            int[] caps = new int[b];
            boolean ok = true;
            for (int i = 1; i <= b; i++) {
                int suffixLen = 3 + digitCount(i) + digitsB; // "<a/b>"
                int cap = limit - suffixLen;
                if (cap < 0) { // cannot fit even the suffix
                    ok = false;
                    break;
                }
                caps[i - 1] = cap;
            }
            if (!ok) continue;

            long sumPrev = 0;
            for (int i = 0; i < b - 1; i++) sumPrev += caps[i];
            long total = sumPrev + caps[b - 1];

            if (sumPrev <= n && n <= total) {
                // construct result
                String[] res = new String[b];
                int pos = 0;
                for (int i = 1; i <= b; i++) {
                    int take;
                    if (i == b) {
                        take = Math.min(caps[i - 1], n - pos);
                    } else {
                        take = caps[i - 1];
                    }
                    String part = message.substring(pos, pos + take) + "<" + i + "/" + b + ">";
                    res[i - 1] = part;
                    pos += take;
                }
                return res;
            }
        }
        return new String[0];
    }

    private int digitCount(int x) {
        if (x >= 100000) return 6;
        if (x >= 10000) return 5;
        if (x >= 1000) return 4;
        if (x >= 100) return 3;
        if (x >= 10) return 2;
        return 1;
    }
}
```

## Python

```python
class Solution(object):
    def splitMessage(self, message, limit):
        """
        :type message: str
        :type limit: int
        :rtype: List[str]
        """
        n = len(message)

        # Helper to compute total capacity for a given b
        def total_capacity(b):
            db = len(str(b))
            cap_sum = 0
            start = 1
            while start <= b:
                da = len(str(start))
                end = min(b, 10 ** da - 1)
                cnt = end - start + 1
                cap = limit - (2 + da + db)  # max chars for each part in this group
                if cap < 0:
                    return -1
                cap_sum += cnt * cap
                start = end + 1
            return cap_sum

        best_b = -1
        for b in range(1, n + 1):
            if limit < 2 + 1 + len(str(b)):  # smallest possible suffix already exceeds limit
                continue
            if total_capacity(b) >= n:
                best_b = b
                break

        if best_b == -1:
            return []

        b = best_b
        db = len(str(b))
        res = []
        pos = 0
        for i in range(1, b + 1):
            da = len(str(i))
            cap = limit - (2 + da + db)
            take = min(cap, n - pos)
            part = message[pos:pos + take] + "<{}/{}>".format(i, b)
            res.append(part)
            pos += take

        return res
```

## Python3

```python
from typing import List

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        n = len(message)
        # try total parts from 1 to n (worst case one char per part)
        for b in range(1, n + 1):
            db = len(str(b))
            # each suffix length at most 2*db+3, need limit >= that
            if limit < 2 * db + 3:
                continue

            # sum of digit lengths from 1 to b
            sum_digits = 0
            start = 1
            for d in range(1, db + 1):
                end = min(b, 10 ** d - 1)
                cnt = end - start + 1
                if cnt > 0:
                    sum_digits += cnt * d
                start = 10 ** d

            capacity = b * limit - sum_digits - b * (db + 3)
            if capacity < n:
                continue

            # construct the parts
            res = []
            idx = 0
            for i in range(1, b + 1):
                suffix = f"<{i}/{b}>"
                cap = limit - len(suffix)
                take = min(cap, n - idx) if idx < n else 0
                part = message[idx:idx + take] + suffix
                res.append(part)
                idx += take
            return res

        return []
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

static long long totalDigits(int n) {
    if (n <= 0) return 0;
    long long res = 0;
    long long start = 1;
    int len = 1;
    while (start * 10LL <= n) {
        long long end = start * 10LL - 1;
        res += (end - start + 1) * len;
        start *= 10LL;
        ++len;
    }
    res += ((long long)n - start + 1) * len;
    return res;
}

static int pow10_int(int e) {
    int r = 1;
    while (e--) r *= 10;
    return r;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** splitMessage(char* message, int limit, int* returnSize) {
    int msgLen = strlen(message);
    *returnSize = 0;

    if (limit < 5) { // smallest possible suffix "<1/1>" length is 5
        return NULL;
    }

    int maxD = (limit - 3) / 2; // maximum digits of total parts allowed
    if (maxD <= 0) {
        return NULL;
    }

    int bestB = -1;

    for (int d = 1; d <= maxD && bestB == -1; ++d) {
        int low = (d == 1) ? 1 : pow10_int(d - 1);
        int high = pow10_int(d) - 1;
        // Upper bound on parts: cannot exceed msgLen + some slack
        int maxPossibleB = msgLen * 2; // safe upper bound
        if (high > maxPossibleB) high = maxPossibleB;

        for (int b = low; b <= high; ++b) {
            if (limit < 2 * d + 3) continue; // suffix longer than limit

            long long S = totalDigits(b - 1); // sum of digits from 1 to b-1
            long long usedPrev = (long long)(b - 1) * (limit - d - 3) - S;
            if (usedPrev > msgLen) continue; // already exceeded message length

            long long remaining = (long long)msgLen - usedPrev;
            long long capLast = limit - (2 * d + 3);
            if (remaining >= 0 && remaining <= capLast) {
                bestB = b;
                break;
            }
        }
    }

    if (bestB == -1) {
        return NULL;
    }

    int b = bestB;
    char **result = (char **)malloc(sizeof(char *) * b);
    int pos = 0;
    for (int i = 1; i <= b; ++i) {
        // build suffix
        char suffix[32];
        int sufLen = sprintf(suffix, "<%d/%d>", i, b);

        int cap = limit - sufLen;
        int take;
        if (i == b) {
            take = msgLen - pos; // remaining characters (could be <= cap)
        } else {
            take = cap;
        }
        if (take < 0) take = 0;

        char *part = (char *)malloc(sizeof(char) * (take + sufLen + 1));
        memcpy(part, message + pos, take);
        memcpy(part + take, suffix, sufLen);
        part[take + sufLen] = '\0';

        result[i - 1] = part;
        pos += take;
    }

    *returnSize = b;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string[] SplitMessage(string message, int limit)
    {
        int n = message.Length;
        for (int b = 1; b <= n; b++)
        {
            int dTotal = Digits(b);
            if (limit < 3 + 2 * dTotal) continue; // suffix too large

            long sumDigits = SumDigits(b - 1);
            long pre = (long)(b - 1) * (limit - 3 - dTotal) - sumDigits;
            if (pre > n) continue; // already exceed message length before last part

            long remaining = n - pre;
            int capLast = limit - (3 + 2 * dTotal);
            if (remaining <= capLast)
            {
                var res = new List<string>(b);
                int pos = 0;
                for (int i = 1; i <= b; i++)
                {
                    string suffix = $"<{i}/{b}>";
                    int contentLen = (i == b) ? n - pos : limit - suffix.Length;
                    string part = message.Substring(pos, contentLen) + suffix;
                    res.Add(part);
                    pos += contentLen;
                }
                return res.ToArray();
            }
        }
        return new string[0];
    }

    private int Digits(int x)
    {
        if (x == 0) return 1;
        int cnt = 0;
        while (x > 0)
        {
            cnt++;
            x /= 10;
        }
        return cnt;
    }

    private long SumDigits(int n)
    {
        long sum = 0;
        long start = 1; // first number with current digit length
        int digit = 1;
        while (start <= n)
        {
            long end = Math.Min(n, start * 10 - 1);
            long count = end - start + 1;
            sum += count * digit;
            digit++;
            start *= 10;
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} message
 * @param {number} limit
 * @return {string[]}
 */
var splitMessage = function(message, limit) {
    const n = message.length;
    
    // helper: number of digits in x (x >= 1)
    const digitCount = (x) => x.toString().length;
    
    // sum of digits(i) for i = 1..b
    const sumDigitsUpTo = (b) => {
        let d = Math.floor(Math.log10(b)) + 1;
        let sum = 0;
        for (let k = 1; k < d; ++k) {
            sum += k * 9 * Math.pow(10, k - 1);
        }
        const start = Math.pow(10, d - 1);
        sum += d * (b - start + 1);
        return sum;
    };
    
    for (let b = 1; b <= n; ++b) {
        const d = digitCount(b);                 // digits of total parts
        const suffixLenLast = 2 * d + 3;          // "<b/b>"
        if (limit < suffixLenLast) continue;     // suffix itself doesn't fit
        
        const sumDigits = sumDigitsUpTo(b);
        const totalSuffix = b * (d + 3) + sumDigits;   // Σ (digits(i)+digits(b)+3)
        const capacity = b * limit - totalSuffix;      // max chars we can take from message
        
        if (capacity >= n) {
            const parts = [];
            let idx = 0;
            for (let i = 1; i <= b; ++i) {
                const suffix = `<${i}/${b}>`;
                const maxTake = limit - suffix.length;
                const take = (i === b) ? (n - idx) : maxTake;
                parts.push(message.slice(idx, idx + take) + suffix);
                idx += take;
            }
            return parts;
        }
    }
    
    return [];
};
```

## Typescript

```typescript
function splitMessage(message: string, limit: number): string[] {
    const n = message.length;
    const maxDigits = 5; // since limit and length are up to 1e4
    let bestB = Infinity;

    const digitCount = (x: number): number => x.toString().length;

    const sumDigitsUpTo = (b: number, D: number): number => {
        let sum = 0;
        for (let k = 1; k < D; ++k) {
            sum += k * 9 * Math.pow(10, k - 1);
        }
        const start = Math.pow(10, D - 1);
        sum += D * (b - start + 1);
        return sum;
    };

    const totalCapacity = (b: number, limitVal: number): number => {
        const D = digitCount(b);
        if (limitVal < 3 + 2 * D) return -1; // suffix too long for any part
        const sumDigits = sumDigitsUpTo(b, D);
        return b * (limitVal - 3 - D) - sumDigits;
    };

    for (let D = 1; D <= maxDigits; ++D) {
        if (limit < 3 + 2 * D) continue; // suffix would exceed limit
        const lowBound = D === 1 ? 1 : Math.pow(10, D - 1);
        const highBound = Math.pow(10, D) - 1;
        if (lowBound > highBound) continue;

        let lo = lowBound, hi = highBound;
        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);
            if (totalCapacity(mid, limit) >= n) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        if (totalCapacity(lo, limit) >= n && lo < bestB) {
            bestB = lo;
        }
    }

    if (!isFinite(bestB)) return [];

    const b = bestB;
    const result: string[] = [];
    let pos = 0;
    for (let i = 1; i <= b; ++i) {
        const suffix = `<${i}/${b}>`;
        const take = Math.min(limit - suffix.length, n - pos);
        const part = message.substring(pos, pos + take) + suffix;
        result.push(part);
        pos += take;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $message
     * @param Integer $limit
     * @return String[]
     */
    function splitMessage($message, $limit) {
        $n = strlen($message);
        // Minimum suffix length is "<1/1>" => 5 characters
        if ($limit < 5) return [];

        // Precompute digit counts and prefix sums up to n (max needed parts)
        $pref = array_fill(0, $n + 1, 0); // pref[0]=0
        for ($i = 1; $i <= $n; $i++) {
            $digits = strlen((string)$i);
            $pref[$i] = $pref[$i - 1] + $digits;
        }

        $foundB = -1;

        // Try number of parts from 1 to n (cannot need more than n parts)
        for ($b = 1; $b <= $n; $b++) {
            $dB = strlen((string)$b);
            // suffix length minimal when a has same digit count as b
            if ($limit < 3 + $dB + $dB) continue; // not enough space for suffix

            $contentBase = $limit - 3 - $dB; // may be zero or positive
            // total capacity (sum of content lengths over all parts)
            $totalCap = $b * $contentBase - $pref[$b];
            if ($totalCap < $n) continue; // cannot fit whole message

            // minimal required characters to fill first b-1 parts completely
            $minNeeded = ($b - 1) * $contentBase - $pref[$b - 1];
            if ($minNeeded > $n) continue; // would need more chars than we have

            // feasible solution found
            $foundB = $b;
            break;
        }

        if ($foundB == -1) return [];

        $b = $foundB;
        $parts = [];
        $pos = 0;

        for ($i = 1; $i <= $b; $i++) {
            $suffix = "<{$i}/{$b}>";
            $contentLen = $limit - strlen($suffix);
            if ($i < $b) {
                // non-last part must have exact length 'limit'
                $partStr = substr($message, $pos, $contentLen);
                $parts[] = $partStr . $suffix;
                $pos += $contentLen;
            } else {
                // last part: take remaining characters (could be <= contentLen)
                $remaining = $n - $pos;
                if ($remaining > $contentLen) {
                    // should not happen with the feasibility checks
                    return [];
                }
                $partStr = substr($message, $pos);
                $parts[] = $partStr . $suffix;
            }
        }

        return $parts;
    }
}
```

## Swift

```swift
class Solution {
    func splitMessage(_ message: String, _ limit: Int) -> [String] {
        let chars = Array(message)
        let m = chars.count
        var bestN = Int.max
        
        // precompute powers of 10
        var pow10 = [Int](repeating: 1, count: 7)
        for i in 1..<pow10.count { pow10[i] = pow10[i-1] * 10 }
        
        func digits(_ x: Int) -> Int {
            return String(x).count
        }
        
        func canSplit(_ n: Int) -> Bool {
            let lenB = digits(n)
            var total = 0
            for i in 1...n {
                let lenA = digits(i)
                let suffixLen = lenA + lenB + 3   // "<a/b>"
                if suffixLen > limit { return false }
                total += limit - suffixLen
                if total >= m { return true }
            }
            return total >= m
        }
        
        for d in 1...5 {
            let low = (d == 1) ? 1 : pow10[d-1]
            var high = min(pow10[d] - 1, 100000)
            // also cannot exceed reasonable upper bound based on message length
            high = min(high, m + 1000)   // extra buffer
            
            var l = low
            var r = high
            var candidate: Int? = nil
            while l <= r {
                let mid = (l + r) / 2
                if canSplit(mid) {
                    candidate = mid
                    r = mid - 1
                } else {
                    l = mid + 1
                }
            }
            if let cand = candidate, cand < bestN {
                bestN = cand
            }
        }
        
        if bestN == Int.max { return [] }
        
        // construct result
        var res: [String] = []
        var idx = 0
        for i in 1...bestN {
            let suffix = "<\(i)/\(bestN)>"
            let cap = limit - suffix.count
            var take = 0
            if idx < m && cap > 0 {
                take = min(cap, m - idx)
            }
            let partContent = String(chars[idx..<idx+take])
            res.append(partContent + suffix)
            idx += take
        }
        // sanity check
        if idx != m { return [] }
        return res
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun splitMessage(message: String, limit: Int): Array<String> {
        val n = message.length
        // helper to count digits of a positive integer
        fun digitCount(x: Int): Int {
            var v = x
            var cnt = 0
            do {
                cnt++
                v /= 10
            } while (v > 0)
            return cnt
        }
        // sum of digit counts from 1 to k
        fun sumDigits(k: Int): Long {
            if (k <= 0) return 0L
            var total = 0L
            var len = 1
            var start = 1
            while (start <= k) {
                val end = kotlin.math.min(k, start * 10 - 1)
                val count = end - start + 1
                total += count.toLong() * len
                len++
                start *= 10
            }
            return total
        }

        for (b in 1..n) {
            val dB = digitCount(b)

            // ensure non-last parts can fit at least the suffix
            if (b > 1) {
                val maxDigitsPrev = digitCount(b - 1)
                if (limit < 3 + dB + maxDigitsPrev) continue
            }

            // total characters taken by first b-1 parts
            val sumDigitsPrev = sumDigits(b - 1)
            val contentFirst = (b - 1).toLong() * (limit - dB - 3) - sumDigitsPrev
            if (contentFirst < 0) continue

            // last part capacity
            val suffixLastLen = 3 + dB + dB
            val maxContentLast = limit - suffixLastLen
            if (maxContentLast < 0) continue

            val remaining = n.toLong() - contentFirst
            if (remaining < 0 || remaining > maxContentLast) continue

            // feasible, construct result
            val res = ArrayList<String>(b)
            var pos = 0
            for (i in 1..b) {
                val suffix = "<$i/$b>"
                val take = if (i < b) limit - suffix.length else remaining.toInt()
                val partContent = message.substring(pos, pos + take)
                res.add(partContent + suffix)
                pos += take
            }
            return res.toTypedArray()
        }
        return emptyArray()
    }
}
```

## Dart

```dart
class Solution {
  List<String> splitMessage(String message, int limit) {
    if (limit < 5) return [];
    int n = message.length;

    // Helper to count digits
    int digitCount(int x) {
      int cnt = 0;
      while (x > 0) {
        cnt++;
        x ~/= 10;
      }
      return cnt;
    }

    List<int> pow10 = [1, 10, 100, 1000, 10000, 100000];

    for (int dB = 1; dB <= 5; dB++) {
      int baseConst = 3 + dB; // '<' '/' '>' plus digits of a and b
      int start = dB == 1 ? 1 : pow10[dB - 1];
      int end = pow10[dB] - 1;

      // Build prefix sums for content lengths where each part (except possibly last) must be exactly limit long.
      List<int> prefix = [0]; // prefix[0] = 0
      int sum = 0;
      int maxI = 0;
      for (int i = 1; ; i++) {
        int lenA = digitCount(i);
        int content = limit - (baseConst + lenA);
        if (content < 0) break;
        sum += content;
        prefix.add(sum); // prefix[i] = sum_{k=1..i} content_k
        maxI = i;
        // No need to go beyond possible total parts bound
        if (i > n * 2) break; // safety guard
      }

      int maxB = maxI + 1; // because first B-1 parts must be within computed range
      int candidateStart = start;
      int candidateEnd = end;
      if (candidateStart > maxB) continue;
      if (candidateEnd > maxB) candidateEnd = maxB;

      for (int B = candidateStart; B <= candidateEnd; B++) {
        int sumNeeded = prefix[B - 1];
        int remaining = n - sumNeeded;
        int lastContentMax = limit - (baseConst + digitCount(B));
        if (lastContentMax < 0) continue;
        if (remaining >= 0 && remaining <= lastContentMax) {
          // construct result
          List<String> res = [];
          int idx = 0;
          for (int i = 1; i < B; i++) {
            int lenA = digitCount(i);
            int contentLen = limit - (baseConst + lenA);
            String partContent = message.substring(idx, idx + contentLen);
            res.add(partContent + "<$i/$B>");
            idx += contentLen;
          }
          // last part
          String lastPart = message.substring(idx);
          res.add(lastPart + "<$B/$B>");
          return res;
        }
      }
    }
    return [];
  }
}
```

## Golang

```go
func splitMessage(message string, limit int) []string {
	n := len(message)
	if n == 0 {
		return []string{}
	}
	// maximum possible parts is n (each part at least one character)
	maxB := n
	// precompute digits and prefix sums of digits up to maxB+1
	digitsArr := make([]int, maxB+2)
	prefixDigits := make([]int, maxB+2)
	for i := 1; i <= maxB+1; i++ {
		x := i
		cnt := 0
		for x > 0 {
			cnt++
			x /= 10
		}
		digitsArr[i] = cnt
		prefixDigits[i] = prefixDigits[i-1] + cnt
	}

	for b := 1; b <= maxB; b++ {
		d := digitsArr[b]
		// minimal suffix length for any part when total parts have d digits:
		// "<a/b>" where a also has at most d digits, worst case both d digits.
		if limit < 2+2*d { // 2 for '<' and '>', plus '/' and two digit counts
			continue
		}
		// total characters that can be taken by first b-1 parts
		sumCap := (b-1)*(limit-(2+d)) - prefixDigits[b-1]
		if sumCap < 0 {
			continue
		}
		remaining := n - sumCap
		if remaining < 0 {
			continue
		}
		capLast := limit - (2 + d + d)
		if remaining > capLast {
			continue
		}
		// feasible, construct result
		res := make([]string, b)
		pos := 0
		for i := 1; i <= b; i++ {
			suffix := "<" + itoa(i) + "/" + itoa(b) + ">"
			contentLen := limit - len(suffix)
			if i == b {
				contentLen = remaining
			}
			part := message[pos:pos+contentLen] + suffix
			res[i-1] = part
			pos += contentLen
		}
		return res
	}
	return []string{}
}

// simple integer to string conversion without fmt for speed
func itoa(x int) string {
	if x == 0 {
		return "0"
	}
	buf := [20]byte{}
	i := len(buf)
	for x > 0 {
		i--
		buf[i] = byte('0' + x%10)
		x /= 10
	}
	return string(buf[i:])
}
```

## Ruby

```ruby
def split_message(message, limit)
  n = message.length
  max_n = n
  digits = Array.new(max_n + 1, 0)
  (1..max_n).each { |i| digits[i] = i.to_s.length }

  prefix = Array.new(max_n + 1, 0)
  (1..max_n).each { |i| prefix[i] = prefix[i - 1] + digits[i] }

  b_found = nil
  (1..max_n).each do |b|
    d = digits[b]
    next if limit < 2 * d + 3
    total_capacity = b * (limit - d - 3) - prefix[b]
    if total_capacity >= n
      b_found = b
      break
    end
  end

  return [] unless b_found

  b = b_found
  d_total = digits[b]
  result = []
  idx = 0

  (1..b).each do |i|
    suffix_len = i.to_s.length + d_total + 3
    cap = limit - suffix_len
    if i == b
      part_content = message[idx..-1] || ""
    else
      part_content = message[idx, cap]
      idx += cap
    end
    result << part_content + "<#{i}/#{b}>"
  end

  result
end
```

## Scala

```scala
object Solution {
    def splitMessage(message: String, limit: Int): Array[String] = {
        val n = message.length
        // helper to compute sum of digit counts from 1 to x
        def sumDigits(x: Int): Long = {
            var total: Long = 0
            var start = 1
            var digits = 1
            while (start <= x) {
                val end = Math.min(x, Math.pow(10, digits).toInt - 1)
                val cnt = end - start + 1
                total += cnt.toLong * digits
                digits += 1
                start *= 10
            }
            total
        }

        var bestB = Int.MaxValue

        // maximum possible digits for b given constraints (n <= 10000)
        for (d <- 1 to 5) {
            if (limit < 3 + 2 * d) {
                // suffix would be longer than limit even for the largest a with d digits
                // skip this digit length
            } else {
                var b = Math.max(1, Math.pow(10, d - 1).toInt)
                // upper bound: enough to definitely cover message (worst case each part contributes at most limit- (4+d))
                val maxContentPerPart = limit - (4 + d) // when a has 1 digit
                if (maxContentPerPart <= 0) {
                    // cannot place any character, impossible for this d
                } else {
                    // safe upper bound: when each part contributes only 1 char
                    val upper = Math.max(b, n * 2 + 100)
                    while (b <= upper) {
                        val cap = b.toLong * (limit - 3 - d) - sumDigits(b)
                        if (cap >= n) {
                            if (b < bestB) bestB = b
                            // found minimal for this digit length, break
                            b = upper + 1
                        } else {
                            b += 1
                        }
                    }
                }
            }
        }

        if (bestB == Int.MaxValue) return Array.empty[String]

        val res = new Array[String](bestB)
        var idx = 0
        for (i <- 1 to bestB) {
            val suffix = s"<$i/$bestB>"
            val maxContent = limit - suffix.length
            val take = if (i == bestB) n - idx else Math.min(maxContent, n - idx)
            val part = message.substring(idx, idx + take) + suffix
            res(i - 1) = part
            idx += take
        }
        // sanity check; if not all characters used, return empty (shouldn't happen)
        if (idx != n) Array.empty[String] else res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn split_message(message: String, limit: i32) -> Vec<String> {
        let msg = message.as_str();
        let n = msg.len();
        if n == 0 {
            return vec![];
        }
        // helper to count digits
        fn digits(mut x: usize) -> usize {
            let mut d = 0;
            while x > 0 {
                d += 1;
                x /= 10;
            }
            d
        }

        // try increasing total parts b
        for b in 1..=n + 10000 { // safe upper bound
            let len_b = digits(b);
            // minimal suffix length when a has 1 digit
            if limit < (3 + len_b + 1) as i32 {
                break; // further b will only increase suffix size
            }

            let mut used: usize = 0;
            let mut impossible = false;

            for i in 1..b {
                let cap = limit - (3 + digits(i) + len_b) as i32;
                if cap < 0 {
                    impossible = true;
                    break;
                }
                used += cap as usize;
                if used > n { // consumed more than message length
                    impossible = true;
                    break;
                }
            }
            if impossible {
                continue;
            }

            let last_cap = limit - (3 + digits(b) + len_b) as i32;
            if last_cap < 0 {
                continue;
            }
            if used > n {
                continue;
            }
            let remaining = n - used;
            if remaining > last_cap as usize {
                continue; // not enough space in last part
            }

            // feasible, construct result
            let mut res: Vec<String> = Vec::with_capacity(b);
            let mut pos: usize = 0;
            for i in 1..=b {
                let suffix = format!("<{}/{}>", i, b);
                let cap = limit as usize - suffix.len();
                if i == b {
                    // take whatever remains (could be less than cap)
                    let part_content = &msg[pos..];
                    res.push(format!("{}{}", part_content, suffix));
                } else {
                    let part_content = &msg[pos..pos + cap];
                    res.push(format!("{}{}", part_content, suffix));
                    pos += cap;
                }
            }
            return res;
        }

        Vec::new()
    }
}
```

## Racket

```racket
(define/contract (split-message message limit)
  (-> string? exact-integer? (listof string?))
  (let* ((msg-len (string-length message)))
    (define (digits n) (string-length (number->string n)))
    (define (sum-digits n)
      (if (= n 0) 0
          (let loop ((d 1) (total 0))
            (let* ((low (expt 10 (- d 1)))
                   (high (min n (- (expt 10 d) 1))))
              (if (> low high)
                  total
                  (loop (+ d 1) (+ total (* (+ 1 (- high low)) d))))))))
    (define (try-b b)
      (let* ((db (digits b))
             (min-suffix (+ (* 2 db) 3))) ; length of "<b/b>"
        (if (< limit min-suffix)
            #f
            (let* ((sumdig (sum-digits (- b 1)))
                   (total-fixed (- (* (- b 1) (- limit db 3)) sumdig))
                   (max-extra (- limit min-suffix))
                   (remaining (- msg-len total-fixed)))
              (if (and (>= remaining 0) (<= remaining max-extra))
                  (let build ((i 1) (pos 0) (parts '()))
                    (if (> i b)
                        (reverse parts)
                        (let* ((suffix (format "<~a/~a>" i b))
                               (suflen (string-length suffix))
                               (content-len (if (< i b)
                                                (- limit suflen)
                                                (- msg-len pos)))
                               (part (string-append (substring message pos (+ pos content-len)) suffix)))
                          (build (+ i 1) (+ pos content-len) (cons part parts)))))
                  #f))))
    (let loop ((b 1))
      (cond [(> b (+ msg-len 2000)) '()] ; give up
            [else (let ((res (try-b b)))
                    (if res res (loop (+ b 1))))]))))
```

## Erlang

```erlang
-spec split_message(Message :: unicode:unicode_binary(), Limit :: integer()) -> [unicode:unicode_binary()].
split_message(Message, Limit) ->
    LenMsg = byte_size(Message),
    case Limit < 5 of
        true -> [];
        false -> find_parts(Message, LenMsg, Limit)
    end.

find_parts(Message, LenMsg, Limit) ->
    loop(1, 0, Message, LenMsg, Limit).

loop(B, SumDigits, Message, LenMsg, Limit) ->
    D = digit_len(B),
    CapB = Limit - (2 * D + 3),
    if
        CapB < 0 -> [];
        true ->
            TotalFirst = (B - 1) * Limit - (SumDigits + (B - 1) * (D + 3)),
            Remaining = LenMsg - TotalFirst,
            case (Remaining >= 0) andalso (Remaining =< CapB) of
                true -> build_parts(Message, LenMsg, Limit, B);
                false ->
                    NewSum = SumDigits + D,
                    loop(B + 1, NewSum, Message, LenMsg, Limit)
            end
    end.

build_parts(Message, LenMsg, Limit, B) ->
    DB = digit_len(B),
    PartsRev = build_rev(1, 0, [], Message, LenMsg, Limit, B, DB),
    lists:reverse(PartsRev).

build_rev(I, Pos, Acc, _Message, _LenMsg, _Limit, B, _DB) when I > B ->
    Acc;
build_rev(I, Pos, Acc, Message, LenMsg, Limit, B, DB) ->
    if
        I == B ->
            ContentLen = LenMsg - Pos,
            Content = binary:part(Message, Pos, ContentLen),
            Suffix = suffix_bin(I, B),
            Part = <<Content/binary, Suffix/binary>>,
            [Part | Acc];
        true ->
            DI = digit_len(I),
            CapI = Limit - (DI + DB + 3),
            Content = binary:part(Message, Pos, CapI),
            Suffix = suffix_bin(I, B),
            Part = <<Content/binary, Suffix/binary>>,
            NewPos = Pos + CapI,
            build_rev(I + 1, NewPos, [Part | Acc], Message, LenMsg, Limit, B, DB)
    end.

suffix_bin(A, B) ->
    list_to_binary("<" ++ integer_to_list(A) ++ "/" ++ integer_to_list(B) ++ ">").

digit_len(N) -> length(integer_to_list(N)).
```

## Elixir

```elixir
defmodule Solution do
  @spec split_message(message :: String.t(), limit :: integer) :: [String.t()]
  def split_message(message, limit) do
    n = String.length(message)

    {_, b_opt} =
      Enum.reduce_while(1..n, {0, nil}, fn b, {cum, _found} ->
        d = digits_len(b)

        # suffix must fit even for the last part
        if limit - 3 - d < d do
          {:cont, {cum + d, nil}}
        else
          total_capacity = b * (limit - 3 - d) - (cum + d)

          if total_capacity >= n do
            {:halt, {cum + d, b}}
          else
            {:cont, {cum + d, nil}}
          end
        end
      end)

    case b_opt do
      nil -> []
      b -> build_parts(message, limit, b)
    end
  end

  defp digits_len(x) when x > 0, do: Integer.digits(x) |> length

  defp build_parts(message, limit, b) do
    total_len = String.length(message)

    do_build(1, 0, [], message, limit, b, total_len)
  end

  defp do_build(idx, pos, acc, _message, _limit, b, total_len) when idx > b do
    Enum.reverse(acc)
  end

  defp do_build(idx, pos, acc, message, limit, b, total_len) do
    suffix = "<#{idx}/#{b}>"
    content_len = limit - byte_size(suffix)

    take =
      if idx == b do
        total_len - pos
      else
        content_len
      end

    part_content = String.slice(message, pos, take)
    new_part = part_content <> suffix

    do_build(idx + 1, pos + take, [new_part | acc], message, limit, b, total_len)
  end
end
```
