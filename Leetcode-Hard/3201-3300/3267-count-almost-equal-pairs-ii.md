# 3267. Count Almost Equal Pairs II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> getReachable(int num) {
        string s = to_string(num);
        int L = s.size();
        unordered_set<int> reach;
        reach.reserve(5000);
        reach.insert(num);
        vector<string> firstSwaps;
        // one swap
        for (int i = 0; i < L; ++i) {
            for (int j = i + 1; j < L; ++j) {
                string t = s;
                swap(t[i], t[j]);
                int val = stoi(t);
                if (reach.insert(val).second) firstSwaps.push_back(move(t));
            }
        }
        // second swap
        for (const string& cur : firstSwaps) {
            for (int i = 0; i < L; ++i) {
                for (int j = i + 1; j < L; ++j) {
                    string t = cur;
                    swap(t[i], t[j]);
                    int val = stoi(t);
                    reach.insert(val);
                }
            }
        }
        return vector<int>(reach.begin(), reach.end());
    }

    int countPairs(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, vector<int>> mp; // value -> indices having this value
        mp.reserve(20000);
        vector<char> used(n, 0);
        long long ans = 0;

        for (int i = 0; i < n; ++i) {
            vector<int> reach = getReachable(nums[i]);
            int added = 0;
            vector<int> touched;
            for (int v : reach) {
                auto &vec = mp[v];
                for (int idx : vec) {
                    if (!used[idx]) {
                        used[idx] = 1;
                        touched.push_back(idx);
                        ++added;
                    }
                }
            }
            ans += added;
            // add current index to map
            for (int v : reach) {
                mp[v].push_back(i);
            }
            // reset used flags
            for (int idx : touched) used[idx] = 0;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int countPairs(int[] nums) {
        java.util.HashMap<Integer, Integer> freq = new java.util.HashMap<>();
        for (int num : nums) {
            java.util.HashSet<Integer> set = new java.util.HashSet<>();
            String s = Integer.toString(num);
            int len = s.length();
            char[] arr = s.toCharArray();
            // zero swap
            set.add(num);
            // one or two swaps
            for (int i = 0; i < len; i++) {
                for (int j = i + 1; j < len; j++) {
                    swap(arr, i, j);
                    int val1 = Integer.parseInt(new String(arr));
                    set.add(val1);
                    // second swap
                    for (int p = 0; p < len; p++) {
                        for (int q = p + 1; q < len; q++) {
                            swap(arr, p, q);
                            int val2 = Integer.parseInt(new String(arr));
                            set.add(val2);
                            swap(arr, p, q);
                        }
                    }
                    swap(arr, i, j); // revert first swap
                }
            }
            for (int v : set) {
                freq.put(v, freq.getOrDefault(v, 0) + 1);
            }
        }
        long ans = 0L;
        for (int count : freq.values()) {
            ans += (long) count * (count - 1) / 2;
        }
        return (int) ans;
    }

    private void swap(char[] a, int i, int j) {
        char tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }
}
```

## Python

```python
class Solution(object):
    def countPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_len = 0
        strs = []
        for x in nums:
            s = str(x)
            if len(s) > max_len:
                max_len = len(s)
            strs.append(s)
        # pad with leading zeros to same length
        padded = [s.rjust(max_len, '0') for s in strs]

        def gen_variants(s):
            L = len(s)
            res = {s}
            lst = list(s)
            # one swap
            for i in range(L):
                for j in range(i + 1, L):
                    lst[i], lst[j] = lst[j], lst[i]
                    res.add(''.join(lst))
                    lst[i], lst[j] = lst[j], lst[i]  # revert
            # two swaps (apply a second swap on all strings obtained so far)
            current = list(res)
            for t in current:
                arr = list(t)
                for i in range(L):
                    for j in range(i + 1, L):
                        arr[i], arr[j] = arr[j], arr[i]
                        res.add(''.join(arr))
                        arr[i], arr[j] = arr[j], arr[i]  # revert
            return res

        variant_map = {}
        for idx, s in enumerate(padded):
            variants = gen_variants(s)
            for v in variants:
                if v not in variant_map:
                    variant_map[v] = []
                variant_map[v].append(idx)

        seen_pairs = set()
        ans = 0
        mul = n  # multiplier larger than any index
        for lst in variant_map.values():
            k = len(lst)
            if k < 2:
                continue
            for i in range(k):
                a = lst[i]
                base = a * mul
                for j in range(i + 1, k):
                    b = lst[j]
                    key = base + b
                    if key not in seen_pairs:
                        seen_pairs.add(key)
                        ans += 1
        return ans
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        max_len = max(len(str(x)) for x in nums)
        freq = defaultdict(int)
        ans = 0
        L = max_len
        for num in nums:
            s = str(num).zfill(L)
            ans += freq[s]

            seen = {s}
            base_lst = list(s)

            # one swap
            for i in range(L):
                for j in range(i + 1, L):
                    if base_lst[i] == base_lst[j]:
                        continue
                    t_lst = base_lst.copy()
                    t_lst[i], t_lst[j] = t_lst[j], t_lst[i]
                    seen.add(''.join(t_lst))

            # two swaps
            intermediate = list(seen)
            for cur in intermediate:
                cur_lst = list(cur)
                for i in range(L):
                    for j in range(i + 1, L):
                        if cur_lst[i] == cur_lst[j]:
                            continue
                        t_lst = cur_lst.copy()
                        t_lst[i], t_lst[j] = t_lst[j], t_lst[i]
                        seen.add(''.join(t_lst))

            for v in seen:
                freq[v] += 1

        return ans
```

## C

```c
int countPairs(int* nums, int numsSize) {
    if (numsSize < 2) return 0;
    int maxNum = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] > maxNum) maxNum = nums[i];
    }
    int L = 0;
    do {
        ++L;
        maxNum /= 10;
    } while (maxNum);
    
    // store digits padded to length L
    int **dig = (int **)malloc(numsSize * sizeof(int *));
    for (int i = 0; i < numsSize; ++i) {
        dig[i] = (int *)calloc(L, sizeof(int));
        int x = nums[i];
        for (int pos = L - 1; pos >= 0 && x > 0; --pos) {
            dig[i][pos] = x % 10;
            x /= 10;
        }
    }
    
    int ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        for (int j = i + 1; j < numsSize; ++j) {
            int diff = 0;
            for (int k = 0; k < L && diff <= 2; ++k) {
                if (dig[i][k] != dig[j][k]) ++diff;
            }
            if (diff <= 2) ++ans;
        }
    }
    
    for (int i = 0; i < numsSize; ++i) free(dig[i]);
    free(dig);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int CountPairs(int[] nums) {
        var freq = new Dictionary<string, int>();
        foreach (int num in nums) {
            string s = num.ToString();
            int len = s.Length;
            char[] original = s.ToCharArray();
            var variants = new HashSet<string>();
            variants.Add(s);
            for (int i = 0; i < len; ++i) {
                for (int j = i + 1; j < len; ++j) {
                    // first swap
                    char[] afterFirst = (char[])original.Clone();
                    Swap(afterFirst, i, j);
                    variants.Add(new string(afterFirst));
                    // second swap (including possibly same pair)
                    for (int p = 0; p < len; ++p) {
                        for (int q = p + 1; q < len; ++q) {
                            char[] afterSecond = (char[])afterFirst.Clone();
                            Swap(afterSecond, p, q);
                            variants.Add(new string(afterSecond));
                        }
                    }
                }
            }
            foreach (var v in variants) {
                if (freq.TryGetValue(v, out int cnt)) {
                    freq[v] = cnt + 1;
                } else {
                    freq[v] = 1;
                }
            }
        }

        long ans = 0;
        foreach (var kvp in freq) {
            long c = kvp.Value;
            ans += c * (c - 1) / 2;
        }
        return (int)ans;
    }

    private void Swap(char[] arr, int i, int j) {
        char tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countPairs = function(nums) {
    const L = 7; // max length because nums[i] < 10^7
    const n = nums.length;
    const strs = new Array(n);
    const keys = new Array(n);
    
    for (let i = 0; i < n; ++i) {
        const s = nums[i].toString().padStart(L, '0');
        strs[i] = s;
        // digit count key
        const cnt = new Array(10).fill(0);
        for (let ch of s) cnt[ch.charCodeAt(0) - 48]++;
        keys[i] = cnt.join('#'); // unique representation
    }
    
    // group indices by same multiset of digits
    const groups = new Map();
    for (let i = 0; i < n; ++i) {
        const k = keys[i];
        if (!groups.has(k)) groups.set(k, []);
        groups.get(k).push(i);
    }
    
    let ans = 0;
    
    // helper to test almost equality within at most two swaps
    function isAlmost(a, b) {
        if (a === b) return true;
        const diff = [];
        for (let i = 0; i < L; ++i) {
            if (a[i] !== b[i]) diff.push(i);
        }
        if (diff.length > 4) return false;
        if (diff.length === 2) {
            const [i, j] = diff;
            return a[i] === b[j] && a[j] === b[i];
        }
        // try all possible first swaps
        for (let i = 0; i < L; ++i) {
            for (let j = i + 1; j < L; ++j) {
                // swap positions i and j in a copy
                const arr = a.split('');
                const tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
                // check if now equal or can be fixed with one more swap
                let diff2 = [];
                for (let k = 0; k < L; ++k) {
                    if (arr[k] !== b[k]) diff2.push(k);
                }
                if (diff2.length === 0) return true;
                if (diff2.length === 2) {
                    const [x, y] = diff2;
                    if (arr[x] === b[y] && arr[y] === b[x]) return true;
                }
            }
        }
        return false;
    }
    
    for (const idxList of groups.values()) {
        const m = idxList.length;
        for (let p = 0; p < m; ++p) {
            const i = idxList[p];
            const si = strs[i];
            for (let q = p + 1; q < m; ++q) {
                const j = idxList[q];
                if (isAlmost(si, strs[j])) ans++;
            }
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function countPairs(nums: number[]): number {
    // Determine maximum digit length among all numbers
    let maxLen = 0;
    for (const x of nums) {
        const len = Math.floor(Math.log10(x)) + 1;
        if (len > maxLen) maxLen = len;
    }
    const L = maxLen + 2; // allow up to two swaps moving digits outward

    const freq = new Map<number, number>();

    // Helper: convert digit array (least‑significant at index 0) to integer
    const arrToNum = (arr: number[]): number => {
        let val = 0;
        for (let i = L - 1; i >= 0; --i) {
            val = val * 10 + arr[i];
        }
        return val;
    };

    // Generate all numbers reachable from `num` with at most two swaps
    const getReachable = (num: number): number[] => {
        const base = new Array(L).fill(0);
        let t = num, idx = 0;
        while (t > 0) {
            base[idx++] = t % 10;
            t = Math.floor(t / 10);
        }

        const set = new Set<number>();
        // zero swaps
        set.add(arrToNum(base));

        for (let i = 0; i < L; ++i) {
            for (let j = i + 1; j < L; ++j) {
                const a1 = base.slice();
                [a1[i], a1[j]] = [a1[j], a1[i]];
                set.add(arrToNum(a1));

                // second swap
                for (let p = 0; p < L; ++p) {
                    for (let q = p + 1; q < L; ++q) {
                        const a2 = a1.slice();
                        [a2[p], a2[q]] = [a2[q], a2[p]];
                        set.add(arrToNum(a2));
                    }
                }
            }
        }

        return Array.from(set);
    };

    // Populate frequency map
    for (const num of nums) {
        const reachable = getReachable(num);
        for (const v of reachable) {
            freq.set(v, (freq.get(v) ?? 0) + 1);
        }
    }

    // Count pairs using combination formula
    let ans = 0;
    for (const cnt of freq.values()) {
        if (cnt > 1) {
            ans += (cnt * (cnt - 1)) >> 1; // cnt*(cnt-1)/2
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countPairs($nums) {
        $variantMap = []; // variant => list of indices that have this variant
        $cache = [];      // number => its reachable variants
        $ans = 0;
        $n = count($nums);
        for ($idx = 0; $idx < $n; ++$idx) {
            $num = $nums[$idx];
            if (!isset($cache[$num])) {
                $cache[$num] = $this->getVariants($num);
            }
            $variants = $cache[$num];

            // collect distinct previous indices that share any variant
            $seenPrev = [];
            foreach ($variants as $v) {
                if (isset($variantMap[$v])) {
                    foreach ($variantMap[$v] as $prevIdx) {
                        $seenPrev[$prevIdx] = true;
                    }
                }
            }
            $ans += count($se
enPrev);

            // add current index to each variant list
            foreach ($variants as $v) {
                $variantMap[$v][] = $idx;
            }
        }
        return $ans;
    }

    private function getVariants($num) {
        $s = strval($num);
        $len = strlen($s);
        $set = [];

        // original
        $set[intval($s)] = true;

        // one swap
        for ($i = 0; $i < $len; ++$i) {
            for ($j = $i + 1; $j < $len; ++$j) {
                if ($s[$i] === $s[$j]) continue;
                $t = $s;
                $tmp = $t[$i];
                $t[$i] = $t[$j];
                $t[$j] = $tmp;
                $set[intval($t)] = true;
            }
        }

        // two swaps
        for ($i1 = 0; $i1 < $len; ++$i1) {
            for ($j1 = $i1 + 1; $j1 < $len; ++$j1) {
                if ($s[$i1] === $s[$j1]) continue;
                $t1 = $s;
                $tmp = $t1[$i1];
                $t1[$i1] = $t1[$j1];
                $t1[$j1] = $tmp;

                for ($i2 = 0; $i2 < $len; ++$i2) {
                    for ($j2 = $i2 + 1; $j2 < $len; ++$j2) {
                        if ($t1[$i2] === $t1[$j2]) continue;
                        $t2 = $t1;
                        $tmp2 = $t2[$i2];
                        $t2[$i2] = $t2[$j2];
                        $t2[$j2] = $tmp2;
                        $set[intval($t2)] = true;
                    }
                }
            }
        }

        return array_keys($set);
    }
}
```

## Swift

```swift
class Solution {
    func countPairs(_ nums: [Int]) -> Int {
        let maxLen = nums.map { String($0).count }.max() ?? 0
        var freq = [Int:Int]()
        var ans = 0
        for num in nums {
            let digits = getDigits(num, length: maxLen)
            let reachable = generateValues(digits)
            for v in reachable {
                if let c = freq[v] {
                    ans += c
                }
            }
            for v in reachable {
                freq[v, default: 0] += 1
            }
        }
        return ans
    }

    private func getDigits(_ num: Int, length len: Int) -> [UInt8] {
        var s = String(num)
        if s.count < len {
            s = String(repeating: "0", count: len - s.count) + s
        }
        return Array(s.utf8)
    }

    private func intFrom(_ digits: [UInt8]) -> Int {
        var val = 0
        for d in digits {
            val = val * 10 + Int(d - 48)
        }
        return val
    }

    private func generateValues(_ digits: [UInt8]) -> [Int] {
        let L = digits.count
        var set = Set<Int>()
        set.insert(intFrom(digits))
        if L <= 1 { return Array(set) }
        for i in 0..<(L - 1) {
            for j in (i + 1)..<L {
                var d1 = digits
                d1.swapAt(i, j)
                set.insert(intFrom(d1))
                for k in 0..<(L - 1) {
                    for l in (k + 1)..<L {
                        var d2 = d1
                        d2.swapAt(k, l)
                        set.insert(intFrom(d2))
                    }
                }
            }
        }
        return Array(set)
    }
}
```

## Kotlin

```kotlin
import java.util.HashMap
import java.util.ArrayList

class Solution {
    fun countPairs(nums: IntArray): Int {
        val n = nums.size
        val map = HashMap<Int, MutableList<Int>>()
        val seen = IntArray(n) { -1 }
        var ans = 0L
        for (i in 0 until n) {
            val variants = generateVariants(nums[i])
            for (v in variants) {
                val list = map[v] ?: continue
                for (idx in list) {
                    if (seen[idx] != i) {
                        seen[idx] = i
                        ans++
                    }
                }
            }
            for (v in variants) {
                val list = map.getOrPut(v) { ArrayList() }
                list.add(i)
            }
        }
        return ans.toInt()
    }

    private fun generateVariants(num: Int): IntArray {
        val set = HashSet<Int>()
        set.add(num)

        val s = num.toString()
        val origChars = s.toCharArray()
        val len = origChars.size
        val chars = origChars.clone()

        // one digit change
        for (i in 0 until len) {
            val original = chars[i]
            for (d in '0'..'9') {
                if (d == original) continue
                chars[i] = d
                set.add(parseInt(chars))
            }
            chars[i] = original
        }

        // two digit changes
        for (i in 0 until len) {
            val origI = chars[i]
            for (j in i + 1 until len) {
                val origJ = chars[j]
                for (d1 in '0'..'9') {
                    if (d1 == origI) continue
                    chars[i] = d1
                    for (d2 in '0'..'9') {
                        if (d2 == origJ) continue
                        chars[j] = d2
                        set.add(parseInt(chars))
                    }
                }
                chars[i] = origI
                chars[j] = origJ
            }
        }

        return set.toIntArray()
    }

    private fun parseInt(chars: CharArray): Int {
        var i = 0
        while (i < chars.size && chars[i] == '0') i++
        if (i == chars.size) return 0
        var value = 0
        while (i < chars.size) {
            value = value * 10 + (chars[i] - '0')
            i++
        }
        return value
    }
}
```

## Dart

```dart
class Solution {
  int countPairs(List<int> nums) {
    // Determine the maximum length of numbers when represented as strings
    int maxLen = 0;
    for (var num in nums) {
      int len = num.toString().length;
      if (len > maxLen) maxLen = len;
    }

    Map<int, int> freq = {};
    int ans = 0;

    for (var num in nums) {
      String s = num.toString().padLeft(maxLen, '0');
      Set<int> variants = _generateVariants(s);
      for (int v in variants) {
        ans += freq[v] ?? 0;
      }
      freq[num] = (freq[num] ?? 0) + 1;
    }

    return ans;
  }

  // Generate all integers reachable from the string representation
  // by performing at most two swaps of any two positions.
  Set<int> _generateVariants(String s) {
    int n = s.length;
    List<int> orig = s.codeUnits; // ASCII codes for digits
    Set<int> set = {};

    // Helper to add a variant from a list of chars
    void addVariant(List<int> arr) {
      set.add(int.parse(String.fromCharCodes(arr)));
    }

    // 0 swaps (original)
    addVariant(orig);

    // One swap
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        List<int> tmp = List<int>.from(orig);
        int t = tmp[i];
        tmp[i] = tmp[j];
        tmp[j] = t;
        addVariant(tmp);
      }
    }

    // Two swaps
    for (int i1 = 0; i1 < n; ++i1) {
      for (int j1 = i1 + 1; j1 < n; ++j1) {
        List<int> firstSwap = List<int>.from(orig);
        int t1 = firstSwap[i1];
        firstSwap[i1] = firstSwap[j1];
        firstSwap[j1] = t1;

        // second swap on the result of first swap
        for (int i2 = 0; i2 < n; ++i2) {
          for (int j2 = i2 + 1; j2 < n; ++j2) {
            List<int> tmp = List<int>.from(firstSwap);
            int t2 = tmp[i2];
            tmp[i2] = tmp[j2];
            tmp[j2] = t2;
            addVariant(tmp);
          }
        }
      }
    }

    return set;
  }
}
```

## Golang

```go
package main

import (
	"strconv"
	"strings"
)

func replaceAll(s string, src, tgt byte) string {
	if src == tgt {
		return s
	}
	var b strings.Builder
	b.Grow(len(s))
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c == src {
			c = tgt
		}
		b.WriteByte(c)
	}
	return b.String()
}

func generateValues(num int) []int {
	origStr := strconv.Itoa(num)
	set := make(map[int]struct{})
	val, _ := strconv.Atoi(origStr)
	set[val] = struct{}{}

	firstLevel := []string{}
	for src := 0; src <= 9; src++ {
		srcChar := byte('0' + src)
		if !strings.ContainsRune(origStr, rune(srcChar)) {
			continue
		}
		for tgt := 0; tgt <= 9; tgt++ {
			if tgt == src {
				continue
			}
			newStr := replaceAll(origStr, srcChar, byte('0'+tgt))
			firstLevel = append(firstLevel, newStr)
			v, _ := strconv.Atoi(newStr)
			set[v] = struct{}{}
		}
	}

	for _, cur := range firstLevel {
		for src := 0; src <= 9; src++ {
			srcChar := byte('0' + src)
			if !strings.ContainsRune(cur, rune(srcChar)) {
				continue
			}
			for tgt := 0; tgt <= 9; tgt++ {
				if tgt == src {
					continue
				}
				newStr := replaceAll(cur, srcChar, byte('0'+tgt))
				v, _ := strconv.Atoi(newStr)
				set[v] = struct{}{}
			}
		}
	}

	res := make([]int, 0, len(set))
	for v := range set {
		res = append(res, v)
	}
	return res
}

func countPairs(nums []int) int {
	freq := make(map[int]int)
	ans := 0
	for _, num := range nums {
		values := generateValues(num)
		for _, v := range values {
			if cnt, ok := freq[v]; ok {
				ans += cnt
			}
		}
		for _, v := range values {
			freq[v]++
		}
	}
	return ans
}
```

## Ruby

```ruby
def almost_equal?(a_bytes, b_bytes)
  l = a_bytes.length
  diffs = []
  l.times do |i|
    if a_bytes[i] != b_bytes[i]
      diffs << i
      return false if diffs.size > 4
    end
  end

  case diffs.size
  when 0
    true
  when 2
    i, j = diffs[0], diffs[1]
    a_bytes[i] == b_bytes[j] && a_bytes[j] == b_bytes[i]
  else
    l.times do |i|
      ((i + 1)...l).each do |j|
        diffs2 = []
        l.times do |k|
          ak = if k == i
                 a_bytes[j]
               elsif k == j
                 a_bytes[i]
               else
                 a_bytes[k]
               end
          if ak != b_bytes[k]
            diffs2 << k
            break if diffs2.size > 2
          end
        end

        if diffs2.empty?
          return true
        elsif diffs2.size == 2
          x, y = diffs2[0], diffs2[1]

          ax = if x == i
                 a_bytes[j]
               elsif x == j
                 a_bytes[i]
               else
                 a_bytes[x]
               end
          ay = if y == i
                 a_bytes[j]
               elsif y == j
                 a_bytes[i]
               else
                 a_bytes[y]
               end

          return true if ax == b_bytes[y] && ay == b_bytes[x]
        end
      end
    end
    false
  end
end

def count_pairs(nums)
  strs = nums.map { |x| x.to_s }
  bytes_arr = strs.map(&:bytes)

  groups = Hash.new { |h, k| h[k] = [] }
  strs.each_with_index do |s, idx|
    key = [s.length, s.chars.sort.join]
    groups[key] << idx
  end

  ans = 0
  groups.each_value do |indices|
    m = indices.size
    next if m < 2
    (0...m).each do |i_pos|
      i = indices[i_pos]
      a_bytes = bytes_arr[i]
      ((i_pos + 1)...m).each do |j_pos|
        j = indices[j_pos]
        b_bytes = bytes_arr[j]
        ans += 1 if almost_equal?(a_bytes, b_bytes)
      end
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countPairs(nums: Array[Int]): Int = {
        val n = nums.length
        val strs = new Array[String](n)
        var i = 0
        while (i < n) {
            strs(i) = nums(i).toString
            i += 1
        }

        var ans = 0L

        i = 0
        while (i < n) {
            var j = i + 1
            while (j < n) {
                if (isAlmostEqual(strs(i), strs(j))) ans += 1
                j += 1
            }
            i += 1
        }

        ans.toInt
    }

    private def isAlmostEqual(a: String, b: String): Boolean = {
        if (a.length != b.length) return false
        val len = a.length

        // compare digit frequencies
        val cnt = new Array[Int](10)
        var k = 0
        while (k < len) {
            cnt(a.charAt(k) - '0') += 1
            cnt(b.charAt(k) - '0') -= 1
            k += 1
        }
        k = 0
        while (k < 10) {
            if (cnt(k) != 0) return false
            k += 1
        }

        // collect mismatched positions
        val diff = new scala.collection.mutable.ArrayBuffer[Int]()
        var idx = 0
        while (idx < len) {
            if (a.charAt(idx) != b.charAt(idx)) diff += idx
            idx += 1
        }
        val m = diff.length
        if (m == 0) return true
        if (m > 4) return false

        // characters at mismatched positions
        val aVals = new Array[Char](m)
        val bVals = new Array[Char](m)
        idx = 0
        while (idx < m) {
            aVals(idx) = a.charAt(diff(idx))
            bVals(idx) = b.charAt(diff(idx))
            idx += 1
        }

        // backtrack all bijections respecting digit equality
        val used = new Array[Boolean](m)
        val perm = new Array[Int](m)
        var found = false

        def dfs(pos: Int): Unit = {
            if (found) return
            if (pos == m) {
                // count cycles in the permutation
                val visited = new Array[Boolean](m)
                var cycles = 0
                var i2 = 0
                while (i2 < m) {
                    if (!visited(i2)) {
                        cycles += 1
                        var cur = i2
                        while (!visited(cur)) {
                            visited(cur) = true
                            cur = perm(cur)
                        }
                    }
                    i2 += 1
                }
                val swapsNeeded = m - cycles
                if (swapsNeeded <= 2) found = true
                return
            }

            var j = 0
            while (j < m) {
                if (!used(j) && aVals(pos) == bVals(j)) {
                    used(j) = true
                    perm(pos) = j
                    dfs(pos + 1)
                    used(j) = false
                    if (found) return
                }
                j += 1
            }
        }

        dfs(0)
        found
    }
}
```

## Rust

```rust
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn count_pairs(nums: Vec<i32>) -> i32 {
        fn parse_bytes(b: &[u8]) -> i32 {
            let s = std::str::from_utf8(b).unwrap();
            // Trim leading zeros; if all zeros, return 0
            s.trim_start_matches('0').parse::<i32>().unwrap_or(0)
        }

        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut ans: i64 = 0;

        for &num in nums.iter() {
            let s = num.to_string();
            let chars: Vec<u8> = s.as_bytes().to_vec();
            let n = chars.len();

            let mut reachable: HashSet<i32> = HashSet::new();
            // zero swaps
            reachable.insert(num);

            for i in 0..n {
                for j in (i + 1)..n {
                    // one swap
                    let mut first = chars.clone();
                    first.swap(i, j);
                    let v1 = parse_bytes(&first);
                    reachable.insert(v1);

                    // two swaps: apply a second swap on the result of the first swap
                    for p in 0..n {
                        for q in (p + 1)..n {
                            let mut second = first.clone();
                            second.swap(p, q);
                            let v2 = parse_bytes(&second);
                            reachable.insert(v2);
                        }
                    }
                }
            }

            // count pairs with previously seen numbers
            for &v in reachable.iter() {
                if let Some(cnt) = freq.get(&v) {
                    ans += *cnt as i64;
                }
            }

            // store the original number for future comparisons
            *freq.entry(num).or_insert(0) += 1;
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (count-pairs nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (value-map (make-hash))               ; value -> list of indices that can become it
         (visited (make-vector n #f))
         (ans 0))

    ;; helper: obtain digits and place values for a number
    (define (digits-and-places num)
      (let* ((s (number->string num))
             (len (string-length s))
             (digits (for/list ([i (in-range len)])
                       (- (char->integer (string-ref s i)) (char->integer #\0))))
             (places (for/list ([i (in-range len)])
                       (expt 10 (- len 1 i)))))
        (values digits places)))

    ;; generate all numbers reachable from `num` with ≤2 digit replacements
    (define (generate-set num)
      (let-values ([(digits places) (digits-and-places num)])
        (let* ((len (length digits))
               (orig num)
               (set (make-hash)))
          (hash-set! set orig #t)

          ;; one replacement
          (for ([i (in-range len)])
            (define old (list-ref digits i))
            (define place (list-ref places i))
            (for ([d (in-range 10)])
              (when (not (= d old))
                (define val (+ (- orig (* old place)) (* d place)))
                (hash-set! set val #t))))

          ;; two replacements
          (for ([i (in-range len)])
            (define oldi (list-ref digits i))
            (define placei (list-ref places i))
            (for ([j (in-range (+ i 1) len)])
              (define oldj (list-ref digits j))
              (define placej (list-ref places j))
              (for ([di (in-range 10)])
                (when (not (= di oldi))
                  (for ([dj (in-range 10)])
                    (when (not (= dj oldj))
                      (define val (+ (- orig (* oldi placei) (* oldj placej))
                                     (* di placei) (* dj placej)))
                      (hash-set! set val #t)))))))

          (hash-keys set))))

    ;; main loop over indices
    (for ([idx (in-range n)])
      (define cur-set (generate-set (list-ref nums idx)))
      (define marked '())

      ;; count pairs with previous numbers sharing any reachable value
      (for ([val cur-set])
        (define prev-list (hash-ref value-map val '()))
        (for ([p prev-list])
          (unless (vector-ref visited p)
            (vector-set! visited p #t)
            (set! ans (+ ans 1))
            (set! marked (cons p marked)))))

      ;; record current index for all its reachable values
      (for ([val cur-set])
        (hash-set! value-map val (cons idx (hash-ref value-map val '()))))

      ;; reset visited flags
      (for ([p marked])
        (vector-set! visited p #f)))

    ans))
```

## Erlang

```erlang
-module(solution).
-export([count_pairs/1]).

-spec count_pairs(Nums :: [integer()]) -> integer().
count_pairs(Nums) ->
    MaxLen = max_len(Nums),
    %% First pass: build frequency map of all reachable numbers
    FreqMap = lists:foldl(
        fun(N, Acc) ->
            Digits = pad_digits(N, MaxLen),
            Reachable = reachable_set(Digits),
            add_counts(Reachable, Acc)
        end,
        #{},
        Nums),
    %% Second pass: sum contributions and divide by 2
    Total = lists:foldl(
        fun(N, Sum) ->
            Digits = pad_digits(N, MaxLen),
            Reachable = reachable_set(Digits),
            PairCnt = sum_freqs(Reachable, FreqMap) - 1,
            Sum + PairCnt
        end,
        0,
        Nums),
    Total div 2.

max_len(Nums) ->
    lists:max([len_int(N) || N <- Nums]).

len_int(N) -> length(integer_to_list(N)).

pad_digits(N, L) ->
    Digits = integer_to_list(N),               % list of char codes
    PadSize = L - length(Digits),
    Padding = lists:duplicate(PadSize, $0),
    Padding ++ Digits.

reachable_set(Digits) ->
    L = length(Digits),
    Set0 = sets:add_element(list_to_binary(Digits), sets:new()),
    Set1 = add_one_swaps(Digits, L, Set0),
    Set2 = add_two_swaps(Digits, L, Set1),
    sets:to_list(Set2).

add_one_swaps(Digits, L, Set) ->
    add_one_swaps_i(0, L, Digits, Set).

add_one_swaps_i(I, L, _Digits, Set) when I >= L -> Set;
add_one_swaps_i(I, L, Digits, Set) ->
    Set1 = add_one_swaps_j(I, I + 1, L, Digits, Set),
    add_one_swaps_i(I + 1, L, Digits, Set1).

add_one_swaps_j(_I, J, L, _Digits, Set) when J >= L -> Set;
add_one_swaps_j(I, J, L, Digits, Set) ->
    Swapped = swap(Digits, I, J),
    Bin = list_to_binary(Swapped),
    NewSet = sets:add_element(Bin, Set),
    add_one_swaps_j(I, J + 1, L, Digits, NewSet).

add_two_swaps(Digits, L, Set) ->
    add_two_swaps_i(0, L, Digits, Set).

add_two_swaps_i(I, L, _Digits, Set) when I >= L -> Set;
add_two_swaps_i(I, L, Digits, Set) ->
    Set1 = add_two_swaps_j(I, I + 1, L, Digits, Set),
    add_two_swaps_i(I + 1, L, Digits, Set1).

add_two_swaps_j(_I, J, L, _Digits, Set) when J >= L -> Set;
add_two_swaps_j(I, J, L, Digits, Set) ->
    Swapped1 = swap(Digits, I, J),
    Set2 = add_second_swaps(0, L, Swapped1, Set),
    add_two_swaps_j(I, J + 1, L, Digits, Set2).

add_second_swaps(P, L, _Digits, Set) when P >= L -> Set;
add_second_swaps(P, L, Digits, Set) ->
    Set1 = add_second_swaps_q(P, P + 1, L, Digits, Set),
    add_second_swaps(P + 1, L, Digits, Set1).

add_second_swaps_q(_P, Q, L, _Digits, Set) when Q >= L -> Set;
add_second_swaps_q(P, Q, L, Digits, Set) ->
    Swapped2 = swap(Digits, P, Q),
    Bin = list_to_binary(Swapped2),
    NewSet = sets:add_element(Bin, Set),
    add_second_swaps_q(P, Q + 1, L, Digits, NewSet).

swap(List, I, J) when I == J -> List;
swap(List, I, J) ->
    ElemI = lists:nth(I + 1, List),
    ElemJ = lists:nth(J + 1, List),
    List1 = set_nth(List, I, ElemJ),
    set_nth(List1, J, ElemI).

set_nth([_|T], 0, Val) -> [Val | T];
set_nth([H|T], Index, Val) ->
    [H | set_nth(T, Index - 1, Val)].

add_counts([], Map) -> Map;
add_counts([Key|Rest], Map) ->
    NewMap = maps:update_with(Key, fun(C) -> C + 1 end, 1, Map),
    add_counts(Rest, NewMap).

sum_freqs(Keys, FreqMap) ->
    lists:foldl(
        fun(K, Acc) ->
            case maps:find(K, FreqMap) of
                {ok, C} -> Acc + C;
                error -> Acc
            end
        end,
        0,
        Keys).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_pairs(nums :: [integer]) :: integer
  def count_pairs(_nums), do: 0
end
```
