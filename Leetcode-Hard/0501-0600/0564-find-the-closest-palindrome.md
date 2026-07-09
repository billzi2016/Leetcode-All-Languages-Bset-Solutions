# 0564. Find the Closest Palindrome

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string nearestPalindromic(string n) {
        int len = n.size();
        long long original = stoll(n);
        vector<string> candidates;
        
        // Edge cases: 10...01 and 9...9
        string edgeHigh = "1" + string(len - 1, '0') + "1";
        candidates.push_back(edgeHigh);
        if (len > 1) {
            string edgeLow(len - 1, '9');
            candidates.push_back(edgeLow);
        }
        
        int halfLen = (len + 1) / 2;
        bool isOdd = (len % 2 == 1);
        long long prefixNum = stoll(n.substr(0, halfLen));
        
        auto makePal = [&](const string& left)->string{
            string res = left;
            int i = isOdd ? (int)left.size() - 2 : (int)left.size() - 1;
            for (; i >= 0; --i) res.push_back(left[i]);
            return res;
        };
        
        for (long long delta = -1; delta <= 1; ++delta) {
            long long cur = prefixNum + delta;
            if (cur < 0) continue;
            string left = to_string(cur);
            if ((int)left.size() != halfLen) continue; // length changed, handled by edge cases
            string pal = makePal(left);
            long long val = stoll(pal);          // normalize (remove leading zeros)
            candidates.push_back(to_string(val));
        }
        
        string best;
        unsigned long long bestDiff = ULLONG_MAX;
        for (const string& cand : candidates) {
            if (cand == n) continue;
            long long val = stoll(cand);
            unsigned long long diff = (val > original) ? (unsigned long long)(val - original)
                                                       : (unsigned long long)(original - val);
            if (diff < bestDiff || (diff == bestDiff && stoll(cand) < stoll(best))) {
                bestDiff = diff;
                best = cand;
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public String nearestPalindromic(String n) {
        int len = n.length();
        long original = Long.parseLong(n);
        java.util.Set<String> candidates = new java.util.HashSet<>();

        // Edge case: 9...9 (len-1 digits)
        if (len > 1) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < len - 1; i++) sb.append('9');
            candidates.add(sb.toString());
        }

        // Edge case: 100...001 (len+1 digits)
        StringBuilder sb2 = new StringBuilder();
        sb2.append('1');
        for (int i = 0; i < len - 1; i++) sb2.append('0');
        sb2.append('1');
        candidates.add(sb2.toString());

        // Prefix based candidates
        int prefixLen = (len + 1) / 2;
        long prefixNum = Long.parseLong(n.substring(0, prefixLen));
        for (int delta = -1; delta <= 1; delta++) {
            long newPrefix = prefixNum + delta;
            if (newPrefix <= 0) continue;
            String left = Long.toString(newPrefix);
            StringBuilder pal = new StringBuilder(left);
            int startIdx = (len % 2 == 0) ? left.length() - 1 : left.length() - 2;
            for (int i = startIdx; i >= 0; i--) {
                pal.append(left.charAt(i));
            }
            candidates.add(pal.toString());
        }

        String answer = "";
        long minDiff = Long.MAX_VALUE;

        for (String cand : candidates) {
            if (cand.equals(n) || cand.isEmpty()) continue;
            long val = Long.parseLong(cand);
            long diff = Math.abs(val - original);
            if (diff < minDiff || (diff == minDiff && val < Long.parseLong(answer))) {
                minDiff = diff;
                answer = cand;
            }
        }

        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        length = len(n)
        original = int(n)

        def make_pal(left_str, total_len):
            if total_len % 2 == 0:
                return left_str + left_str[::-1]
            else:
                return left_str + left_str[-2::-1]

        candidates = set()

        # edge candidates: 10...01 and 9...9
        candidates.add('1' + ('0' * (length - 1)) + '1')
        if length > 1:
            candidates.add('9' * (length - 1))

        prefix_len = (length + 1) // 2
        prefix_num = int(n[:prefix_len])

        for delta in (-1, 0, 1):
            new_prefix = str(prefix_num + delta)
            cand = make_pal(new_prefix, length)
            candidates.add(cand)

        # remove the original number itself if present
        candidates.discard(n)

        best_candidate = None
        min_diff = float('inf')

        for cand in candidates:
            if not cand:  # skip empty strings
                continue
            cand_int = int(cand)
            diff = abs(cand_int - original)
            if diff < min_diff or (diff == min_diff and cand_int < int(best_candidate)):
                min_diff = diff
                best_candidate = cand

        return best_candidate
```

## Python3

```python
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return str(int(n) - 1)

        length = len(n)
        prefix_len = (length + 1) // 2
        prefix = int(n[:prefix_len])

        candidates = set()
        # edge cases: 99..9 and 100...001
        candidates.add('9' * (length - 1))
        candidates.add('1' + '0' * (length - 1) + '1')

        for delta in (-1, 0, 1):
            left = prefix + delta
            if left < 0:
                continue
            s = str(left)
            if length % 2 == 0:
                pal = s + s[::-1]
            else:
                pal = s + s[-2::-1]   # mirror without the middle character
            candidates.add(pal)

        candidates.discard(n)  # exclude the original number

        orig = int(n)
        best_val = None
        best_diff = float('inf')
        for cand in candidates:
            if not cand:  # skip empty strings, shouldn't happen
                continue
            val = int(cand)
            diff = abs(val - orig)
            if diff < best_diff or (diff == best_diff and val < best_val):
                best_diff = diff
                best_val = val

        return str(best_val)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int numDigits(unsigned long long x) {
    int cnt = 0;
    do {
        cnt++;
        x /= 10ULL;
    } while (x);
    return cnt;
}

static char* makePalindrome(const char* prefix, int totalLen) {
    int prefLen = strlen(prefix); // should be (totalLen+1)/2
    char* res = (char*)malloc(totalLen + 1);
    for (int i = 0; i < prefLen; ++i) res[i] = prefix[i];
    for (int i = 0; i < totalLen / 2; ++i) {
        res[totalLen - 1 - i] = res[i];
    }
    res[totalLen] = '\0';
    return res;
}

char* nearestPalindromic(char* n) {
    int len = strlen(n);
    int prefLen = (len + 1) / 2;

    char prefixStr[20];
    strncpy(prefixStr, n, prefLen);
    prefixStr[prefLen] = '\0';
    unsigned long long left = strtoull(prefixStr, NULL, 10);

    char* cand[6];
    int cnt = 0;

    // same prefix
    cand[cnt++] = makePalindrome(prefixStr, len);

    // incremented prefix
    unsigned long long inc = left + 1;
    if (numDigits(inc) == prefLen) {
        char incStr[20];
        sprintf(incStr, "%llu", inc);
        cand[cnt++] = makePalindrome(incStr, len);
    }

    // decremented prefix
    unsigned long long dec = (left == 0) ? 0 : left - 1;
    if (numDigits(dec) == prefLen) {
        char decStr[20];
        sprintf(decStr, "%llu", dec);
        cand[cnt++] = makePalindrome(decStr, len);
    }

    // all 9's of length len-1
    if (len > 1) {
        char* s = (char*)malloc(len);
        for (int i = 0; i < len - 1; ++i) s[i] = '9';
        s[len - 1] = '\0';
        cand[cnt++] = s;
    }

    // 1 followed by zeros and ending with 1 (length len+1)
    {
        char* s = (char*)malloc(len + 2);
        s[0] = '1';
        for (int i = 1; i < len; ++i) s[i] = '0';
        s[len] = '1';
        s[len + 1] = '\0';
        cand[cnt++] = s;
    }

    unsigned long long orig = strtoull(n, NULL, 10);
    unsigned long long bestDiff = ULLONG_MAX;
    unsigned long long bestVal = 0;
    char* bestStr = NULL;

    for (int i = 0; i < cnt; ++i) {
        char* c = cand[i];
        if (strcmp(c, n) == 0) continue;
        unsigned long long val = strtoull(c, NULL, 10);
        unsigned long long diff = (orig > val) ? (orig - val) : (val - orig);
        if (diff < bestDiff || (diff == bestDiff && val < bestVal)) {
            bestDiff = diff;
            bestVal = val;
            bestStr = c;
        }
    }

    char* ans = (char*)malloc(strlen(bestStr) + 1);
    strcpy(ans, bestStr);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Numerics;
using System.Linq;

public class Solution {
    public string NearestPalindromic(string n) {
        int len = n.Length;
        var candidates = new HashSet<string>();

        // Edge case: 100...001
        string edge1 = "1" + new string('0', len - 1) + "1";
        candidates.Add(edge1);

        // Edge case: 99...9 (len-1 digits)
        if (len > 1) {
            candidates.Add(new string('9', len - 1));
        } else {
            candidates.Add("0");
        }

        int k = (len + 1) / 2;
        string leftStr = n.Substring(0, k);
        long leftNum = long.Parse(leftStr);

        for (int delta = -1; delta <= 1; delta++) {
            long newLeftNum = leftNum + delta;
            if (newLeftNum < 0) continue;
            string newLeftStr = newLeftNum.ToString();
            string pal = MakePalindrome(newLeftStr, len % 2 == 0);
            candidates.Add(pal);
        }

        candidates.Remove(n);

        BigInteger original = BigInteger.Parse(n);
        string best = "";
        BigInteger bestDiff = BigInteger.Zero;
        bool first = true;

        foreach (var cand in candidates) {
            if (cand.Length == 0) continue;
            BigInteger val = BigInteger.Parse(cand);
            BigInteger diff = BigInteger.Abs(val - original);
            if (first || diff < bestDiff || (diff == bestDiff && val < BigInteger.Parse(best))) {
                best = cand;
                bestDiff = diff;
                first = false;
            }
        }

        return best;
    }

    private string MakePalindrome(string left, bool evenLength) {
        char[] revArr = left.ToCharArray();
        Array.Reverse(revArr);
        string rev = new string(revArr);
        if (!evenLength) {
            rev = rev.Substring(1);
        }
        return left + rev;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} n
 * @return {string}
 */
var nearestPalindromic = function(n) {
    const len = n.length;
    const original = BigInt(n);
    const candidates = new Set();

    // Edge candidates: 10...01 and 9...9 (one less digit)
    candidates.add('1' + '0'.repeat(len - 1) + '1');
    if (len > 1) {
        candidates.add('9'.repeat(len - 1));
    }

    const k = Math.floor((len + 1) / 2);
    const prefixNum = BigInt(n.slice(0, k));

    for (const delta of [-1n, 0n, 1n]) {
        const newPrefix = (prefixNum + delta).toString();
        let pal;
        if (len % 2 === 0) {
            const rev = newPrefix.split('').reverse().join('');
            pal = newPrefix + rev;
        } else {
            const left = newPrefix.slice(0, -1);
            const rev = left.split('').reverse().join('');
            pal = newPrefix + rev;
        }
        candidates.add(pal);
    }

    let best = '';
    let bestDiff = null;

    for (const cand of candidates) {
        if (cand === n) continue; // exclude the original number
        const candVal = BigInt(cand);
        const diff = original > candVal ? original - candVal : candVal - original;
        if (
            bestDiff === null ||
            diff < bestDiff ||
            (diff === bestDiff && candVal < BigInt(best))
        ) {
            bestDiff = diff;
            best = cand;
        }
    }

    return best;
};
```

## Typescript

```typescript
function nearestPalindromic(n: string): string {
    const len = n.length;
    const halfLen = Math.floor((len + 1) / 2);
    const prefix = n.slice(0, halfLen);
    const candidates = new Set<string>();

    function makePalindrome(leftPart: string, totalLen: number): string {
        const rev = leftPart.split('').reverse().join('');
        if (totalLen % 2 === 0) {
            return leftPart + rev;
        } else {
            return leftPart + rev.slice(1);
        }
    }

    const prefNum = BigInt(prefix);
    for (const delta of [-1n, 0n, 1n]) {
        const p = (prefNum + delta).toString();
        candidates.add(makePalindrome(p, len));
    }

    // 10...01
    candidates.add('1' + '0'.repeat(len - 1) + '1');

    // 9...9 (len-1 digits)
    if (len > 1) {
        candidates.add('9'.repeat(len - 1));
    } else {
        candidates.add('0');
    }

    const original = BigInt(n);
    let best: string | null = null;
    let bestDiff: bigint | null = null;

    for (const cand of candidates) {
        if (cand === n) continue;
        const candVal = BigInt(cand);
        const diff = candVal > original ? candVal - original : original - candVal;
        if (
            bestDiff === null ||
            diff < bestDiff ||
            (diff === bestDiff && candVal < BigInt(best!))
        ) {
            best = cand;
            bestDiff = diff;
        }
    }

    // normalize leading zeros
    let result = (best ?? '').replace(/^0+/, '');
    if (result === '') result = '0';
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $n
     * @return String
     */
    function nearestPalindromic($n) {
        $len = strlen($n);
        if ($len == 1) {
            // single digit case: closest palindrome is either n-1 or n+1, choose smaller diff then smaller number
            $num = intval($n);
            $cand1 = strval($num - 1);
            $cand2 = strval($num + 1);
            if (abs($num - $cand1) <= abs($cand2 - $num)) {
                return $cand1;
            }
            return $cand2;
        }

        // helper to build palindrome from left part
        $makePal = function(string $left, int $totalLen): string {
            $rev = strrev($left);
            if ($totalLen % 2 == 1) {
                $rev = substr($rev, 1); // drop middle character
            }
            return $left . $rev;
        };

        $k = intdiv($len + 1, 2);               // length of left part (includes middle for odd)
        $prefix = substr($n, 0, $k);
        $candidates = [];

        // same prefix
        $candidates[] = $makePal($prefix, $len);

        // incremented prefix
        $incPrefix = strval(intval($prefix) + 1);
        $candidates[] = $makePal($incPrefix, $len);

        // decremented prefix
        $decPrefixInt = intval($prefix) - 1;
        $decPrefix = strval($decPrefixInt);
        $candidates[] = $makePal($decPrefix, $len);

        // edge case: 99...9 (len-1 digits)
        $candidates[] = str_repeat('9', $len - 1);

        // edge case: 100...001 (len+1 digits)
        $candidates[] = '1' . str_repeat('0', $len - 1) . '1';

        $originalNum = intval($n);
        $bestDiff = PHP_INT_MAX;
        $answer = '';

        foreach ($candidates as $cand) {
            // normalize candidate (remove leading zeros)
            $candNum = intval($cand);
            $candStr = strval($candNum);

            if ($candNum == $originalNum) {
                continue; // skip the number itself
            }

            $diff = abs($candNum - $originalNum);
            if ($diff < $bestDiff || ($diff == $bestDiff && $candNum < intval($answer))) {
                $bestDiff = $diff;
                $answer = $candStr;
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func nearestPalindromic(_ n: String) -> String {
        let length = n.count
        var candidates = Set<String>()
        
        // Special candidates: 10...01 and all 9's of length-1 (or "0" for single digit)
        let oneZeroOne = "1" + String(repeating: "0", count: max(0, length - 1)) + "1"
        candidates.insert(oneZeroOne)
        if length > 1 {
            candidates.insert(String(repeating: "9", count: length - 1))
        } else {
            candidates.insert("0")
        }
        
        // Helper to build palindrome from left part
        func makePal(_ left: String, _ even: Bool) -> String {
            var res = left
            let revPart: String
            if even {
                revPart = String(left.reversed())
            } else {
                revPart = String(left.dropLast().reversed())
            }
            res += revPart
            return res
        }
        
        // Increment string number by one
        func addOne(_ s: String) -> String {
            var arr = Array(s)
            var i = arr.count - 1
            var carry = 1
            while i >= 0 && carry > 0 {
                let digit = Int(String(arr[i]))!
                let sum = digit + carry
                arr[i] = Character("\(sum % 10)")
                carry = sum / 10
                i -= 1
            }
            if carry > 0 { arr.insert("1", at: 0) }
            return String(arr)
        }
        
        // Decrement string number by one (assumes s != "0")
        func subtractOne(_ s: String) -> String {
            var arr = Array(s)
            var i = arr.count - 1
            var borrow = 1
            while i >= 0 && borrow > 0 {
                let digit = Int(String(arr[i]))!
                if digit >= borrow {
                    arr[i] = Character("\(digit - borrow)")
                    borrow = 0
                } else {
                    arr[i] = Character("\(10 + digit - borrow)")
                    borrow = 1
                }
                i -= 1
            }
            var result = String(arr)
            while result.first == "0" && result.count > 1 {
                result.removeFirst()
            }
            return result
        }
        
        let k = (length + 1) / 2
        let prefix = String(n.prefix(k))
        let even = length % 2 == 0
        
        // Same prefix palindrome
        candidates.insert(makePal(prefix, even))
        // Incremented prefix palindrome
        candidates.insert(makePal(addOne(prefix), even))
        // Decremented prefix palindrome
        candidates.insert(makePal(subtractOne(prefix), even))
        
        // Remove the original number itself
        candidates.remove(n)
        
        let originalVal = Int64(n)!
        var bestStr = ""
        var bestVal: Int64 = 0
        var minDiff = Int64.max
        
        for cand in candidates {
            guard let val = Int64(cand) else { continue }
            let diff = abs(val - originalVal)
            if bestStr.isEmpty || diff < minDiff || (diff == minDiff && val < bestVal) {
                minDiff = diff
                bestVal = val
                bestStr = cand
            }
        }
        return bestStr
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun nearestPalindromic(n: String): String {
        val len = n.length
        val original = n.toLong()
        val candidates = mutableSetOf<String>()

        // Special high candidate: 100...001
        val high = "1" + "0".repeat(len - 1) + "1"
        candidates.add(high)

        // Special low candidate: 99...9 (len-1 digits)
        if (len > 1) {
            val low = "9".repeat(len - 1)
            candidates.add(low)
        }

        val halfLen = (len + 1) / 2
        val prefixStr = n.substring(0, halfLen)
        val prefixNum = prefixStr.toLong()

        for (delta in intArrayOf(-1, 0, 1)) {
            val newPrefix = prefixNum + delta
            if (newPrefix < 0) continue
            val left = newPrefix.toString()
            val palindrome = buildPalindrome(left, len % 2 == 0)
            candidates.add(palindrome)
        }

        // Exclude the original number itself
        candidates.remove(n)

        var best = ""
        var minDiff = Long.MAX_VALUE

        for (cand in candidates) {
            if (cand.isEmpty()) continue
            val candVal = cand.toLong()
            val diff = kotlin.math.abs(candVal - original)
            if (diff < minDiff ||
                (diff == minDiff && (best.isEmpty() || candVal < best.toLong()))
            ) {
                minDiff = diff
                best = cand
            }
        }

        return best
    }

    private fun buildPalindrome(left: String, even: Boolean): String {
        val sb = StringBuilder()
        sb.append(left)
        val rev = if (even) left.reversed() else left.dropLast(1).reversed()
        sb.append(rev)
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String nearestPalindromic(String n) {
    int len = n.length;
    BigInt original = BigInt.parse(n);
    Set<String> candidates = {};

    // special cases: 10...01 and 9...9
    String allNines = List.filled(len - 1, '9').join();
    if (allNines.isNotEmpty) candidates.add(allNines);
    String oneZeroOne = '1' + List.filled(len - 1, '0').join() + '1';
    candidates.add(oneZeroOne);

    int k = (len + 1) >> 1; // ceil(len/2)
    String prefix = n.substring(0, k);
    BigInt prefixNum = BigInt.parse(prefix);

    for (int delta = -1; delta <= 1; ++delta) {
      BigInt newPrefixNum = prefixNum + BigInt.from(delta);
      if (newPrefixNum < BigInt.zero) continue;
      String newPrefix = newPrefixNum.toString();
      candidates.add(_makePalindrome(newPrefix, len));
    }

    String best = '';
    BigInt minDiff = BigInt.parse('9223372036854775807'); // large initial value

    for (String cand in candidates) {
      if (cand == n) continue;
      if (cand.length > 1 && cand[0] == '0') continue; // ignore leading zeros
      BigInt candNum = BigInt.parse(cand);
      BigInt diff = (candNum - original).abs();
      if (diff < minDiff ||
          (diff == minDiff && (best.isEmpty || candNum < BigInt.parse(best)))) {
        minDiff = diff;
        best = cand;
      }
    }

    return best;
  }

  String _makePalindrome(String left, int originalLen) {
    if (originalLen % 2 == 0) {
      String rev = left.split('').reversed.join();
      return left + rev;
    } else {
      // odd length: left includes the middle character
      String withoutMid = left.substring(0, left.length - 1);
      String rev = withoutMid.split('').reversed.join();
      return left + rev;
    }
  }
}
```

## Golang

```go
package main

import (
	"math"
	"strconv"
	"strings"
)

func nearestPalindromic(n string) string {
	l := len(n)
	if l == 0 {
		return ""
	}
	candidates := []string{}

	// candidate: all 9's with length l-1
	if l > 1 {
		candidates = append(candidates, strings.Repeat("9", l-1))
	}
	// candidate: 10...01 with length l+1
	candidates = append(candidates, "1"+strings.Repeat("0", l-1)+"1")

	prefixLen := (l + 1) / 2
	prefixStr := n[:prefixLen]
	prefixInt, _ := strconv.ParseInt(prefixStr, 10, 64)

	for _, delta := range []int64{-1, 0, 1} {
		newInt := prefixInt + delta
		if newInt < 0 {
			continue
		}
		newStr := strconv.FormatInt(newInt, 10)
		if len(newStr) != prefixLen {
			// overflow/underflow cases are covered by the special candidates above
			continue
		}
		pal := buildPalindrome(newStr, l%2 == 0)
		candidates = append(candidates, pal)
	}

	nVal, _ := strconv.ParseInt(n, 10, 64)
	best := ""
	bestDiff := int64(math.MaxInt64)
	var bestVal int64

	for _, cand := range candidates {
		if cand == n {
			continue
		}
		if len(cand) > 1 && cand[0] == '0' {
			continue // leading zeros not allowed except for "0"
		}
		val, err := strconv.ParseInt(cand, 10, 64)
		if err != nil {
			continue
		}
		diff := abs(val - nVal)
		if diff < bestDiff || (diff == bestDiff && val < bestVal) {
			bestDiff = diff
			best = cand
			bestVal = val
		}
	}
	return best
}

func buildPalindrome(left string, even bool) string {
	var sb strings.Builder
	sb.WriteString(left)
	mirror := left
	if !even {
		mirror = mirror[:len(mirror)-1]
	}
	for i := len(mirror) - 1; i >= 0; i-- {
		sb.WriteByte(mirror[i])
	}
	return sb.String()
}

func abs(a int64) int64 {
	if a < 0 {
		return -a
	}
	return a
}
```

## Ruby

```ruby
def make_pal(left_str, len)
  if len.even?
    left_str + left_str.reverse
  else
    left_str + left_str[0...-1].reverse
  end
end

# @param {String} n
# @return {String}
def nearest_palindromic(n)
  len = n.length
  prefix_len = (len + 1) / 2
  left = n[0, prefix_len].to_i

  candidates = []
  candidates << make_pal(left.to_s, len)
  candidates << make_pal((left + 1).to_s, len)
  candidates << make_pal((left - 1).to_s, len) if left > 0
  candidates << ("9" * (len - 1)) unless len == 1
  candidates << ("1" + ("0" * (len - 1)) + "1")

  orig = n.to_i
  best_val = nil
  best_diff = nil

  candidates.each do |c|
    next if c == n || c.empty?
    val = c.to_i
    diff = (val - orig).abs
    if best_val.nil? || diff < best_diff || (diff == best_diff && val < best_val)
      best_val = val
      best_diff = diff
    end
  end

  best_val.to_s
end
```

## Scala

```scala
object Solution {
  import scala.math.BigInt

  def nearestPalindromic(n: String): String = {
    val len = n.length
    val even = len % 2 == 0
    val prefixLen = (len + 1) / 2
    val prefix = n.substring(0, prefixLen)

    def makePalindrome(left: String, even: Boolean): String = {
      val sb = new StringBuilder(left)
      val rev = if (even) left.reverse else left.dropRight(1).reverse
      sb.append(rev)
      sb.toString()
    }

    var candidates = Set[String]()

    // same prefix
    candidates += makePalindrome(prefix, even)

    // decrement prefix
    val dec = (BigInt(prefix) - 1).toString
    candidates += makePalindrome(dec, even)

    // increment prefix
    val inc = (BigInt(prefix) + 1).toString
    candidates += makePalindrome(inc, even)

    // 99...9 (len-1 digits)
    if (len > 1) {
      candidates += "9" * (len - 1)
    }

    // 100...001 (len+1 digits)
    val high = "1" + ("0" * (len - 1)) + "1"
    candidates += high

    // remove the original number itself
    candidates -= n

    var best: String = ""
    var bestDiff: BigInt = null

    val original = BigInt(n)

    for (cand <- candidates) {
      // skip empty strings that may arise from decrementing "1" to "0" with odd length handling
      if (cand.nonEmpty && cand != n) {
        val candVal = BigInt(cand)
        val diff = (candVal - original).abs
        if (bestDiff == null || diff < bestDiff ||
            (diff == bestDiff && candVal < BigInt(best))) {
          bestDiff = diff
          best = cand
        }
      }
    }

    best
  }
}
```

## Rust

```rust
use std::cmp::{min, Ordering};

impl Solution {
    pub fn nearest_palindromic(n: String) -> String {
        let len = n.len();
        let original: i128 = n.parse().unwrap();

        // helper to build palindrome from left part
        fn build_pal(left: &str, even: bool) -> String {
            let mut res = left.to_string();
            if even {
                let rev: String = left.chars().rev().collect();
                res.push_str(&rev);
            } else {
                if left.len() > 1 {
                    let without_last = &left[..left.len() - 1];
                    let rev: String = without_last.chars().rev().collect();
                    res.push_str(&rev);
                }
                // when left.len()==1, dropping last gives empty string -> nothing to append
            }
            res
        }

        let mut candidates: Vec<String> = Vec::new();

        // edge case: 10...01 (len+1 digits)
        {
            let mut s = String::from("1");
            for _ in 0..(len - 1) {
                s.push('0');
            }
            s.push('1');
            candidates.push(s);
        }

        // edge case: 9...9 (len-1 digits)
        if len > 1 {
            let s = "9".repeat(len - 1);
            candidates.push(s);
        }

        // main candidates based on prefix
        let k = (len + 1) / 2; // length of left part
        let left_str = &n[0..k];
        let left_num: i128 = left_str.parse().unwrap();

        for delta in -1i128..=1 {
            let cur = left_num + delta;
            if cur < 0 {
                continue;
            }
            let cur_str = cur.to_string();
            let pal = build_pal(&cur_str, len % 2 == 0);
            candidates.push(pal);
        }

        // select the best candidate
        let mut best_candidate = String::new();
        let mut best_diff: i128 = i128::MAX;
        let mut best_val: i128 = 0;

        for cand in candidates {
            if cand == n {
                continue;
            }
            // skip empty strings (should not happen)
            if cand.is_empty() {
                continue;
            }
            let val: i128 = cand.parse().unwrap();
            let diff = (val - original).abs();

            match diff.cmp(&best_diff) {
                Ordering::Less => {
                    best_diff = diff;
                    best_candidate = cand.clone();
                    best_val = val;
                }
                Ordering::Equal => {
                    if val < best_val {
                        best_candidate = cand.clone();
                        best_val = val;
                    }
                }
                Ordering::Greater => {}
            }
        }

        best_candidate
    }
}
```

## Racket

```racket
(define/contract (nearest-palindromic n)
  (-> string? string?)
  (let* ((len (string-length n))
         (orig (string->number n))
         (even? (= (modulo len 2) 0))
         (left-len (if even?
                       (quotient len 2)
                       (+ (quotient len 2) 1)))
         (left (substring n 0 left-len))
         (make-pal
          (lambda (prefix)
            (let* ((rev (list->string (reverse (string->list prefix))))
                   (pal (if even?
                            (string-append prefix rev)
                            (string-append prefix (substring rev 1)))))
              pal)))
         (candidates
          (let ((cand '()))
            ;; same prefix
            (set! cand (cons (make-pal left) cand))
            ;; incremented prefix
            (let* ((inc-num (+ 1 (string->number left)))
                   (inc-str (number->string inc-num)))
              (set! cand (cons (make-pal inc-str) cand)))
            ;; decremented prefix
            (let* ((dec-num (- (string->number left) 1))
                   (dec-str (if (< dec-num 0)
                                "0"
                                (number->string dec-num))))
              (set! cand (cons (make-pal dec-str) cand)))
            ;; all 9's of length len-1
            (when (> len 1)
              (let ((nine (make-string (- len 1) #\9)))
                (set! cand (cons nine cand))))
            ;; 10^len + 1 => "1" followed by len zeros and another "1"
            (let ((one-zero-one
                   (string-append "1"
                                  (make-string len #\0)
                                  "1")))
              (set! cand (cons one-zero-one cand)))
            cand))
         (filtered (filter (lambda (s) (not (equal? s n))) candidates))
         (best
          (let loop ((lst filtered) (best-cand #f) (best-diff 0))
            (if (null? lst)
                best-cand
                (let* ((cand (car lst))
                       (val (string->number cand))
                       (diff (abs (- val orig))))
                  (cond
                    [(or (not best-cand)
                         (< diff best-diff)
                         (and (= diff best-diff) (< val (string->number best-cand))))
                     (loop (cdr lst) cand diff)]
                    [else (loop (cdr lst) best-cand best-diff)]))))))
    best))
```

## Erlang

```erlang
-module(solution).
-export([nearest_palindromic/1]).

-spec nearest_palindromic(N :: unicode:unicode_binary()) -> unicode:unicode_binary().
nearest_palindromic(N) ->
    NStr = binary_to_list(N),
    Orig = list_to_integer(NStr),
    L = length(NStr),
    PrefixLen = (L + 1) div 2,
    PrefixStr0 = lists:sublist(NStr, PrefixLen),
    PrefixNum = list_to_integer(PrefixStr0),

    % candidates from prefix +/- 1 and unchanged
    CandidatesFromPrefix = lists:foldl(
        fun(Delta, Acc) ->
            NewNum = PrefixNum + Delta,
            if NewNum < 0 -> Acc;
               true ->
                   NewPrefixStr = integer_to_list(NewNum),
                   PalInt = make_pal_from_prefix(NewPrefixStr, L),
                   [PalInt | Acc]
            end
        end,
        [],
        [-1, 0, 1]),

    % special candidates: 99..9 and 100...001
    LowAll9 = case L of
                 1 -> 0;
                 _ -> ten_pow(L - 1) - 1
             end,
    High10001 = ten_pow(L) + 1,

    AllCandidates = lists:usort(
        [C || C <- CandidatesFromPrefix ++ [LowAll9, High10001],
              C =/= Orig]),

    {Best, _} = lists:foldl(
        fun(Cand, {BestCand, BestDiff}) ->
            Diff = abs(Cand - Orig),
            case Diff < BestDiff orelse (Diff == BestDiff andalso Cand < BestCand) of
                true -> {Cand, Diff};
                false -> {BestCand, BestDiff}
            end
        end,
        {0, 1 bsl 63},
        AllCandidates),

    list_to_binary(integer_to_list(Best)).

make_pal_from_prefix(PrefixStr, OrigLen) ->
    case OrigLen rem 2 of
        0 ->
            PalStr = PrefixStr ++ lists:reverse(PrefixStr);
        1 ->
            RevPart = lists:reverse(lists:sublist(PrefixStr, length(PrefixStr) - 1)),
            PalStr = PrefixStr ++ RevPart
    end,
    list_to_integer(PalStr).

ten_pow(N) -> ten_pow(N, 1).
ten_pow(0, Acc) -> Acc;
ten_pow(N, Acc) -> ten_pow(N - 1, Acc * 10).
```

## Elixir

```elixir
defmodule Solution do
  @spec nearest_palindromic(n :: String.t) :: String.t
  def nearest_palindromic(n) do
    len = String.length(n)
    k = div(len + 1, 2)
    prefix = String.slice(n, 0, k)

    # initial candidate from the same prefix
    candidates =
      Enum.reduce([-1, 1], MapSet.new([make_pal(prefix, len)]), fn delta, acc ->
        new_pref = Integer.to_string(String.to_integer(prefix) + delta)

        if String.length(new_pref) == k do
          MapSet.put(acc, make_pal(new_pref, len))
        else
          acc
        end
      end)

    # edge candidates: 100...001 and 99...9
    candidates = MapSet.put(candidates, "1" <> String.duplicate("0", len - 1) <> "1")
    candidates =
      if len > 1 do
        MapSet.put(candidates, String.duplicate("9", len - 1))
      else
        candidates
      end

    # exclude the original number itself
    candidates = MapSet.delete(candidates, n)

    orig_int = String.to_integer(n)

    {best_cand, _} =
      Enum.reduce(candidates, nil, fn cand, acc ->
        cand_int = String.to_integer(cand)
        diff = abs(cand_int - orig_int)

        cond do
          acc == nil ->
            {cand, diff}

          diff < elem(acc, 1) ->
            {cand, diff}

          diff == elem(acc, 1) and cand_int < String.to_integer(elem(acc, 0)) ->
            {cand, diff}

          true ->
            acc
        end
      end)

    best_cand
  end

  defp make_pal(prefix, len) do
    if rem(len, 2) == 0 do
      prefix <> String.reverse(prefix)
    else
      rev = prefix |> String.slice(0, String.length(prefix) - 1) |> String.reverse()
      prefix <> rev
    end
  end
end
```
