# 3234. Count the Number of Substrings With Dominant Ones

## Cpp

```cpp
class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.size();
        vector<int> prefOnes(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefOnes[i + 1] = prefOnes[i] + (s[i] == '1');
        }
        vector<int> zeroPos;
        for (int i = 0; i < n; ++i) if (s[i] == '0') zeroPos.push_back(i);
        int m = zeroPos.size();
        int limit = (int)sqrt(n) + 2; // maximum zeros to consider
        long long ans = 0;
        for (int l = 0; l < n; ++l) {
            int idx = lower_bound(zeroPos.begin(), zeroPos.end(), l) - zeroPos.begin();
            int firstZero = (idx < m ? zeroPos[idx] : n);
            // substrings with no zeros
            ans += firstZero - l;
            for (int t = 0; t < limit && idx + t < m; ++t) {
                int zpos = zeroPos[idx + t];
                int k = t + 1; // number of zeros
                long long onesBefore = prefOnes[zpos + 1] - prefOnes[l];
                long long need = 1LL * k * k - onesBefore;
                int nextZero = (idx + t + 1 < m ? zeroPos[idx + t + 1] : n);
                if (need <= 0) {
                    ans += nextZero - zpos;
                } else {
                    long long maxOnesAfter = nextZero - zpos - 1; // consecutive ones after current zero
                    if (need <= maxOnesAfter) {
                        ans += nextZero - (zpos + (int)need);
                    }
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
    public int numberOfSubstrings(String s) {
        int n = s.length();
        // positions of zeros
        java.util.ArrayList<Integer> zeroPos = new java.util.ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '0') zeroPos.add(i);
        }
        int zeroCount = zeroPos.size();

        // prefix sum of ones
        int[] prefOnes = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefOnes[i + 1] = prefOnes[i] + (s.charAt(i) == '1' ? 1 : 0);
        }

        int B = (int) Math.sqrt(n) + 2; // safe upper bound for zeros in a valid substring
        long ans = 0;
        int idxZero = 0; // first zero index >= l

        for (int l = 0; l < n; l++) {
            while (idxZero < zeroCount && zeroPos.get(idxZero) < l) idxZero++;

            // substrings with zero zeros (only ones)
            int nextZero = (idxZero < zeroCount) ? zeroPos.get(idxZero) : n;
            ans += nextZero - l; // all lengths from 1 to that many are valid

            // consider substrings containing up to B zeros
            for (int z = 1; z <= B && idxZero + z - 1 < zeroCount; z++) {
                int rightZero = zeroPos.get(idxZero + z - 1);
                int limit;
                if (idxZero + z < zeroCount) {
                    limit = zeroPos.get(idxZero + z) - 1;
                } else {
                    limit = n - 1;
                }

                int needOnes = z * z;
                // check if already satisfied at rightZero
                int onesTillRight = prefOnes[rightZero + 1] - prefOnes[l];
                int minR;
                if (onesTillRight >= needOnes) {
                    minR = rightZero;
                } else {
                    // binary search for minimal r in [rightZero+1, limit]
                    int low = rightZero + 1, high = limit, pos = -1;
                    while (low <= high) {
                        int mid = (low + high) >>> 1;
                        int ones = prefOnes[mid + 1] - prefOnes[l];
                        if (ones >= needOnes) {
                            pos = mid;
                            high = mid - 1;
                        } else {
                            low = mid + 1;
                        }
                    }
                    if (pos == -1) continue; // not enough ones before next zero
                    minR = pos;
                }
                ans += limit - minR + 1;
            }
        }

        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        zero_pos = [i for i, ch in enumerate(s) if ch == '0']
        B = int(n ** 0.5) + 2

        # substrings consisting only of ones
        ans = 0
        cnt = 0
        for ch in s:
            if ch == '1':
                cnt += 1
            else:
                ans += cnt * (cnt + 1) // 2
                cnt = 0
        ans += cnt * (cnt + 1) // 2

        import bisect
        for l in range(n):
            idx = bisect.bisect_left(zero_pos, l)
            for t in range(B):
                if idx + t >= len(zero_pos):
                    break
                r_zero = zero_pos[idx + t]
                zeros = t + 1
                nextZero = zero_pos[idx + t + 1] if idx + t + 1 < len(zero_pos) else n
                maxR = nextZero - 1

                ones0 = (r_zero - l + 1) - zeros
                need = zeros * zeros
                if ones0 >= need:
                    add = maxR - r_zero + 1
                else:
                    delta = need - ones0
                    if r_zero + delta <= maxR:
                        add = maxR - (r_zero + delta) + 1
                    else:
                        add = 0
                ans += add

        return ans
```

## Python3

```python
import math
from bisect import bisect_left

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zeros = [i for i, ch in enumerate(s) if ch == '0']
        m = len(zeros)
        # sentinel not needed because we handle bounds explicitly
        limit = math.isqrt(n) + 1  # maximum zeros to consider

        ans = 0
        idx = 0  # first zero index >= current left
        for l in range(n):
            while idx < m and zeros[idx] < l:
                idx += 1

            # k = 0 : substrings with no zeros (all ones)
            next_zero = zeros[idx] if idx < m else n
            ans += next_zero - l

            # k >= 1
            for k in range(1, limit + 1):
                zero_idx = idx + k - 1
                if zero_idx >= m:
                    break
                pos_k = zeros[zero_idx]
                min_len = k * k + k
                r_needed = l + min_len - 1
                r_start = max(r_needed, pos_k)

                # rightmost position before the next zero (or end of string)
                if zero_idx + 1 < m:
                    r_end = zeros[zero_idx + 1] - 1
                else:
                    r_end = n - 1

                if r_start <= r_end:
                    ans += r_end - r_start + 1

        return ans
```

## C

```c
#include <string.h>
#include <stdlib.h>
#include <math.h>

int numberOfSubstrings(char* s) {
    int n = (int)strlen(s);
    int *zeros = (int*)malloc(n * sizeof(int));
    int zcnt = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == '0') zeros[zcnt++] = i;
    }

    long long ans = 0;

    // substrings with zero count = 0 (all ones)
    int i = 0;
    while (i < n) {
        if (s[i] == '1') {
            int j = i;
            while (j < n && s[j] == '1') ++j;
            long long len = j - i;
            ans += len * (len + 1) / 2;
            i = j;
        } else {
            ++i;
        }
    }

    int B = (int)sqrt((double)n) + 1; // bound for number of zeros to enumerate

    for (int l = 0; l < n; ++l) {
        // lower_bound to find first zero >= l
        int lo = 0, hi = zcnt;
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (zeros[mid] < l) lo = mid + 1;
            else hi = mid;
        }
        int idx = lo;

        for (int k = 0; k < B && idx + k < zcnt; ++k) {
            int zPos = zeros[idx + k];
            int z = k + 1;                     // number of zeros in substring
            long long minLen = (long long)z * z + z;
            long long r_needed = (long long)l + minLen - 1;
            if (r_needed >= n) break;          // further zeros will need even longer substrings

            int r_min = (int)(zPos > r_needed ? zPos : r_needed);
            int nextZero = (idx + k + 1 < zcnt) ? zeros[idx + k + 1] : n;
            int r_max = nextZero - 1;

            if (r_min <= r_max) {
                ans += (long long)(r_max - r_min + 1);
            }
        }
    }

    free(zeros);
    return (int)ans;   // answer fits in 32-bit signed integer for given constraints
}
```

## Csharp

```csharp
public class Solution {
    public int NumberOfSubstrings(string s) {
        int n = s.Length;
        var zeroList = new System.Collections.Generic.List<int>();
        for (int i = 0; i < n; i++) {
            if (s[i] == '0') zeroList.Add(i);
        }
        int[] zeros = zeroList.ToArray();
        int zc = zeros.Length;
        long ans = 0;

        for (int l = 0; l < n; l++) {
            // index of first zero >= l
            int idx = System.Array.BinarySearch(zeros, l);
            if (idx < 0) idx = ~idx;

            // substrings with 0 zeros (all ones)
            int maxR0 = (idx < zc) ? zeros[idx] - 1 : n - 1;
            if (maxR0 >= l) ans += (long)(maxR0 - l + 1);

            // substrings with z > 0 zeros, where z is limited by sqrt(n)
            for (int z = 1; ; z++) {
                long neededLen = (long)z * z + z; // minimal length to satisfy condition
                if (neededLen > n) break;

                int zeroIdxPos = idx + z - 1;
                if (zeroIdxPos >= zc) break; // not enough zeros after l

                int rightZeroIdx = zeros[zeroIdxPos]; // position of the z-th zero
                int maxR = (zeroIdxPos + 1 < zc) ? zeros[zeroIdxPos + 1] - 1 : n - 1;

                long neededR = l + neededLen - 1; // minimal right endpoint index
                if (neededR > maxR) continue; // cannot satisfy length requirement

                int startR = (int)Math.Max(rightZeroIdx, neededR);
                ans += (long)(maxR - startR + 1);
            }
        }

        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    const n = s.length;
    const prefOnes = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        prefOnes[i + 1] = prefOnes[i] + (s[i] === '1' ? 1 : 0);
    }
    const zeroPos = [];
    for (let i = 0; i < n; ++i) {
        if (s[i] === '0') zeroPos.push(i);
    }
    const m = zeroPos.length;
    const maxK = Math.floor(Math.sqrt(n));
    let ans = 0;
    let idxZero = 0; // first zero index >= current left
    for (let l = 0; l < n; ++l) {
        while (idxZero < m && zeroPos[idxZero] < l) idxZero++;
        const nextZero = idxZero < m ? zeroPos[idxZero] : n;
        // substrings with zero zeros are always valid
        ans += nextZero - l;
        for (let k = 1; k <= maxK; ++k) {
            if (idxZero + k - 1 >= m) break;
            const rightZero = zeroPos[idxZero + k - 1];
            const limit = (idxZero + k < m) ? zeroPos[idxZero + k] : n;
            // binary search for minimal r in [rightZero, limit-1] with enough ones
            let low = rightZero, high = limit;
            while (low < high) {
                const mid = (low + high) >> 1;
                const ones = prefOnes[mid + 1] - prefOnes[l];
                if (ones >= k * k) {
                    high = mid;
                } else {
                    low = mid + 1;
                }
            }
            if (low < limit) {
                ans += limit - low;
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function numberOfSubstrings(s: string): number {
    const n = s.length;
    const preOnes = new Int32Array(n + 1);
    for (let i = 0; i < n; ++i) {
        preOnes[i + 1] = preOnes[i] + (s.charAt(i) === '1' ? 1 : 0);
    }

    const zeroPos: number[] = [];
    for (let i = 0; i < n; ++i) if (s.charAt(i) === '0') zeroPos.push(i);

    let ans = 0;

    // substrings with no zeros (all ones)
    let cntOnes = 0;
    for (let i = 0; i < n; ++i) {
        if (s.charAt(i) === '1') {
            ++cntOnes;
        } else {
            ans += cntOnes * (cntOnes + 1) / 2;
            cntOnes = 0;
        }
    }
    ans += cntOnes * (cntOnes + 1) / 2;

    const B = Math.floor(Math.sqrt(n)) + 1;

    function lowerBound(arr: number[], target: number): number {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (arr[m] >= target) r = m; else l = m + 1;
        }
        return l;
    }

    for (let l = 0; l < n; ++l) {
        const startIdx = lowerBound(zeroPos, l);
        for (let z = 1; z <= B; ++z) {
            const idxZ = startIdx + z - 1;
            if (idxZ >= zeroPos.length) break;
            const rZero = zeroPos[idxZ];
            const neededOnes = z * z;
            const limit = (idxZ + 1 < zeroPos.length) ? zeroPos[idxZ + 1] : n;

            // binary search minimal r in [rZero, limit) with enough ones
            let low = rZero, high = limit;
            while (low < high) {
                const mid = (low + high) >> 1;
                if (preOnes[mid + 1] - preOnes[l] >= neededOnes) high = mid;
                else low = mid + 1;
            }
            if (low === limit) continue;
            ans += limit - low;
        }
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numberOfSubstrings($s) {
        $n = strlen($s);
        $prefixOnes = array_fill(0, $n + 1, 0);
        $zeroPos = [];
        for ($i = 0; $i < $n; ++$i) {
            $prefixOnes[$i + 1] = $prefixOnes[$i] + ($s[$i] === '1' ? 1 : 0);
            if ($s[$i] === '0') {
                $zeroPos[] = $i;
            }
        }

        // substrings consisting only of ones
        $ans = 0;
        $lenOnes = 0;
        for ($i = 0; $i < $n; ++$i) {
            if ($s[$i] === '1') {
                ++$lenOnes;
            } else {
                $ans += intdiv($lenOnes * ($lenOnes + 1), 2);
                $lenOnes = 0;
            }
        }
        $ans += intdiv($lenOnes * ($lenOnes + 1), 2);

        $cntZero = count($zeroPos);
        if ($cntZero == 0) {
            return $ans; // all substrings already counted
        }

        $B = (int)floor(sqrt($n));

        // helper lower_bound
        $lowerBound = function($arr, $target) {
            $low = 0;
            $high = count($arr);
            while ($low < $high) {
                $mid = intdiv($low + $high, 2);
                if ($arr[$mid] < $target) {
                    $low = $mid + 1;
                } else {
                    $high = $mid;
                }
            }
            return $low;
        };

        for ($l = 0; $l < $n; ++$l) {
            // find first zero index >= l
            $idx = $lowerBound($zeroPos, $l);
            if ($idx == $cntZero) continue; // no zeros to the right

            for ($k = 1; $k <= $B && $idx + $k - 1 < $cntZero; ++$k) {
                $zPos = $zeroPos[$idx + $k - 1]; // position of k-th zero in this substring
                $needOnes = $k * $k + $prefixOnes[$l];

                // binary search minimal r >= zPos with enough ones
                $low = $zPos;
                $high = $n - 1;
                $pos = -1;
                while ($low <= $high) {
                    $mid = intdiv($low + $high, 2);
                    if ($prefixOnes[$mid + 1] >= $needOnes) {
                        $pos = $mid;
                        $high = $mid - 1;
                    } else {
                        $low = $mid + 1;
                    }
                }
                if ($pos == -1) continue; // not enough ones even till end

                // limit before next zero appears
                $limit = ($idx + $k < $cntZero) ? $zeroPos[$idx + $k] - 1 : $n - 1;

                if ($pos > $limit) {
                    continue; // condition cannot be met before another zero appears
                }

                $firstValid = max($zPos, $pos);
                $ans += ($limit - $firstValid + 1);
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func numberOfSubstrings(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var pref = [Int](repeating: 0, count: n + 1)
        var zeroPos = [Int]()
        for i in 0..<n {
            pref[i + 1] = pref[i] + (chars[i] == "1" ? 1 : 0)
            if chars[i] == "0" { zeroPos.append(i) }
        }
        
        let B = Int(sqrt(Double(n)))
        var ans: Int64 = 0
        
        // substrings consisting only of ones
        var run = 0
        for i in 0..<n {
            if chars[i] == "1" {
                run += 1
            } else {
                ans += Int64(run * (run + 1) / 2)
                run = 0
            }
        }
        ans += Int64(run * (run + 1) / 2)
        
        // helper lower bound
        func lowerBound(_ arr: [Int], _ target: Int) -> Int {
            var l = 0, r = arr.count
            while l < r {
                let m = (l + r) >> 1
                if arr[m] < target { l = m + 1 } else { r = m }
            }
            return l
        }
        
        // substrings with at least one zero
        for l in 0..<n {
            var idx = lowerBound(zeroPos, l)
            if idx == zeroPos.count { continue }
            var zeros = 0
            while idx + zeros < zeroPos.count && zeros < B {
                let zPos = zeroPos[idx + zeros]
                zeros += 1
                let limit: Int
                if idx + zeros < zeroPos.count {
                    limit = zeroPos[idx + zeros] - 1
                } else {
                    limit = n - 1
                }
                
                var lo = zPos, hi = limit, found = -1
                while lo <= hi {
                    let mid = (lo + hi) >> 1
                    let ones = pref[mid + 1] - pref[l]
                    if ones >= zeros * zeros {
                        found = mid
                        hi = mid - 1
                    } else {
                        lo = mid + 1
                    }
                }
                if found != -1 {
                    ans += Int64(limit - found + 1)
                }
            }
        }
        
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfSubstrings(s: String): Int {
        val n = s.length
        val pref = IntArray(n + 1)
        for (i in 0 until n) {
            pref[i + 1] = pref[i] + if (s[i] == '1') 1 else 0
        }
        val zeroPos = mutableListOf<Int>()
        for (i in 0 until n) {
            if (s[i] == '0') zeroPos.add(i)
        }

        var ans = 0L

        // substrings consisting only of ones
        var i = 0
        while (i < n) {
            if (s[i] == '1') {
                var j = i
                while (j < n && s[j] == '1') j++
                val len = j - i
                ans += (len.toLong() * (len + 1)) / 2
                i = j
            } else {
                i++
            }
        }

        val limit = kotlin.math.sqrt(n.toDouble()).toInt() + 1

        fun lowerBound(arr: List<Int>, target: Int): Int {
            var l = 0
            var r = arr.size
            while (l < r) {
                val m = (l + r) ushr 1
                if (arr[m] < target) l = m + 1 else r = m
            }
            return l
        }

        for (l in 0 until n) {
            var idx = lowerBound(zeroPos, l)
            if (idx == zeroPos.size) continue
            val maxIdx = kotlin.math.min(idx + limit - 1, zeroPos.size - 1)
            for (kIdx in idx..maxIdx) {
                val k = kIdx - idx + 1
                val zPos = zeroPos[kIdx]
                val nextZero = if (kIdx + 1 < zeroPos.size) zeroPos[kIdx + 1] else n
                val maxR = nextZero - 1
                val needOnes = k * k

                var lo = zPos
                var hi = maxR
                var pos = -1
                while (lo <= hi) {
                    val mid = (lo + hi) ushr 1
                    val ones = pref[mid + 1] - pref[l]
                    if (ones >= needOnes) {
                        pos = mid
                        hi = mid - 1
                    } else {
                        lo = mid + 1
                    }
                }
                if (pos != -1) {
                    ans += (maxR - pos + 1).toLong()
                }
            }
        }

        return ans.toInt()
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int numberOfSubstrings(String s) {
    int n = s.length;
    List<int> pref = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      pref[i + 1] = pref[i] + (s.codeUnitAt(i) == 49 ? 1 : 0);
    }
    int limit = sqrt(n).toInt();
    int ans = 0;
    for (int l = 0; l < n; ++l) {
      int zeros = 0;
      for (int r = l; r < n && zeros <= limit; ++r) {
        if (s.codeUnitAt(r) == 48) zeros++;
        int ones = pref[r + 1] - pref[l];
        if (ones >= zeros * zeros) ans++;
      }
    }
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"math"
	"sort"
)

func numberOfSubstrings(s string) int {
	n := len(s)
	preOnes := make([]int, n+1)
	zerosPos := []int{}
	for i := 0; i < n; i++ {
		preOnes[i+1] = preOnes[i]
		if s[i] == '1' {
			preOnes[i+1]++
		} else {
			zerosPos = append(zerosPos, i)
		}
	}

	B := int(math.Sqrt(float64(n))) + 1
	ans := 0

	for l := 0; l < n; l++ {
		idx := sort.Search(len(zerosPos), func(i int) bool { return zerosPos[i] >= l })
		nextZero := n
		if idx < len(zerosPos) {
			nextZero = zerosPos[idx]
		}
		ans += nextZero - l // substrings with zero zeros (all ones)

		for k := 1; k <= B && idx+k-1 < len(zerosPos); k++ {
			z := zerosPos[idx+k-1]
			limit := n - 1
			if idx+k < len(zerosPos) {
				limit = zerosPos[idx+k] - 1
			}
			needOnes := k * k

			lo, hi := z, limit
			pos := -1
			for lo <= hi {
				mid := (lo + hi) / 2
				ones := preOnes[mid+1] - preOnes[l]
				if ones >= needOnes {
					pos = mid
					hi = mid - 1
				} else {
					lo = mid + 1
				}
			}
			if pos != -1 {
				ans += limit - pos + 1
			}
		}
	}

	return ans
}
```

## Ruby

```ruby
def number_of_substrings(s)
  n = s.length
  max_zero = Math.sqrt(n).to_i

  # prefix sum of ones
  pref_one = Array.new(n + 1, 0)
  (0...n).each do |i|
    pref_one[i + 1] = pref_one[i] + (s.getbyte(i) == 49 ? 1 : 0) # '1'.ord == 49
  end

  zero_pos = []
  (0...n).each { |i| zero_pos << i if s.getbyte(i) == 48 } # '0'.ord == 48

  def lower_bound(arr, val)
    l = 0
    r = arr.length
    while l < r
      m = (l + r) / 2
      if arr[m] < val
        l = m + 1
      else
        r = m
      end
    end
    l
  end

  ans = 0

  (0...n).each do |l|
    idx = lower_bound(zero_pos, l) # first zero >= l
    # k = number of zeros in substring
    (0..max_zero).each do |k|
      if k == 0
        next_zero = (idx < zero_pos.length) ? zero_pos[idx] : n
        ans += next_zero - l
        next
      end

      target_idx = idx + k - 1
      break if target_idx >= zero_pos.length

      pos_k = zero_pos[target_idx]
      next_zero = (target_idx + 1 < zero_pos.length) ? zero_pos[target_idx + 1] : n

      needed = k * k
      ones_at_posk = pref_one[pos_k + 1] - pref_one[l]

      if ones_at_posk >= needed
        ans += next_zero - pos_k
      else
        deficit = needed - ones_at_posk
        min_r = pos_k + deficit
        if min_r < next_zero
          ans += next_zero - min_r
        end
      end
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def numberOfSubstrings(s: String): Int = {
        val n = s.length
        val zeros = new scala.collection.mutable.ArrayBuffer[Int]()
        var i = 0
        while (i < n) {
            if (s.charAt(i) == '0') zeros += i
            i += 1
        }
        val m = zeros.length
        val B = Math.sqrt(n).toInt + 1

        var ans: Long = 0L
        var zeroPtr = 0 // first zero index >= l

        var l = 0
        while (l < n) {
            while (zeroPtr < m && zeros(zeroPtr) < l) zeroPtr += 1

            // substrings with no zeros
            val limitZero = if (zeroPtr < m) zeros(zeroPtr) else n
            ans += (limitZero - l).toLong

            var k = 1
            while (k <= B && zeroPtr + k - 1 < m) {
                val zeroIdx = zeroPtr + k - 1
                val rZero = zeros(zeroIdx)
                val limit = if (zeroIdx + 1 < m) zeros(zeroIdx + 1) else n + 1
                val lenMin = k * k + k
                var start = l + lenMin
                if (start < rZero + 1) start = rZero + 1
                if (start < limit) {
                    ans += (limit - start).toLong
                }
                k += 1
            }

            l += 1
        }

        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        // positions of zeros
        let mut zeros = Vec::new();
        for (i, &c) in bytes.iter().enumerate() {
            if c == b'0' {
                zeros.push(i);
            }
        }
        let m = zeros.len();

        // substrings consisting only of ones
        let mut ans: i64 = 0;
        let mut cur = 0usize;
        for &c in bytes.iter() {
            if c == b'1' {
                cur += 1;
            } else {
                ans += (cur * (cur + 1) / 2) as i64;
                cur = 0;
            }
        }
        ans += (cur * (cur + 1) / 2) as i64;

        // next zero index for each start position
        let mut next_idx = vec![m; n + 1];
        let mut j = m;
        for i in (0..n).rev() {
            if j > 0 && zeros[j - 1] == i {
                j -= 1;
            }
            next_idx[i] = j;
        }

        // bound on number of zeros to consider
        let b = ((n as f64).sqrt() as usize) + 1;

        for l in 0..n {
            let idx_start = next_idx[l];
            for t in 1..=b {
                if idx_start + t - 1 >= m {
                    break;
                }
                let zpos = zeros[idx_start + t - 1];
                // minimal length needed: t^2 + t
                let len_needed = t * (t + 1);
                let mut min_r = l + len_needed - 1;
                if min_r < zpos {
                    min_r = zpos;
                }
                let max_r = if idx_start + t < m {
                    zeros[idx_start + t] - 1
                } else {
                    n - 1
                };
                if min_r <= max_r {
                    ans += (max_r - min_r + 1) as i64;
                }
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define (lower-bound vec target)
  (let loop ((lo 0) (hi (vector-length vec)))
    (if (= lo hi)
        lo
        (let* ((mid (quotient (+ lo hi) 2))
               (val (vector-ref vec mid)))
          (if (< val target)
              (loop (+ mid 1) hi)
              (loop lo mid))))))

(define (find-first-pos low high l need pref)
  (let loop ((lo low) (hi high) (ans #f))
    (if (> lo hi)
        ans
        (let* ((mid (quotient (+ lo hi) 2))
               (ones (- (vector-ref pref (+ mid 1)) (vector-ref pref l))))
          (if (>= ones need)
              (loop lo (- mid 1) mid)
              (loop (+ mid 1) hi ans))))))

(define/contract (number-of-substrings s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (pref (make-vector (+ n 1) 0))
         (zero-list '()))
    ;; build prefix sum of ones and collect zero positions
    (for ([i (in-range n)])
      (let ((ch (string-ref s i)))
        (vector-set! pref (+ i 1)
                     (+ (vector-ref pref i) (if (char=? ch #\1) 1 0)))
        (when (char=? ch #\0)
          (set! zero-list (cons i zero-list)))))
    (define zero-pos (list->vector (reverse zero-list))) ; sorted vector of zero indices
    (define m (vector-length zero-pos))
    (define sqrtN (inexact->exact (floor (sqrt n))))
    (define ans 0)
    ;; iterate over each left endpoint
    (for ([l (in-range n)])
      (define idx (lower-bound zero-pos l))
      (define next-zero (if (< idx m) (vector-ref zero-pos idx) n))
      ;; substrings with no zeros
      (set! ans (+ ans (- next-zero l)))
      ;; consider substrings whose rightmost zero is among the next sqrtN zeros
      (let loop ((zcnt 0) (posIdx idx) (zeros 0))
        (when (and (< posIdx m) (< zcnt sqrtN))
          (define zpos (vector-ref zero-pos posIdx))
          (set! zeros (+ zeros 1))
          (define need (* zeros zeros))
          (define following-zero (if (< (+ posIdx 1) m)
                                    (vector-ref zero-pos (+ posIdx 1))
                                    n))
          (define low zpos)
          (define high (- following-zero 1))
          (define ones-at-low
            (- (vector-ref pref (+ low 1)) (vector-ref pref l)))
          (if (>= ones-at-low need)
              (set! ans (+ ans (- following-zero zpos))) ; all endings work
              (let ((rfound (find-first-pos low high l need pref)))
                (when rfound
                  (set! ans (+ ans (- following-zero rfound))))))
          (loop (+ zcnt 1) (+ posIdx 1) zeros)))))
    ans))
```

## Erlang

```erlang
-spec number_of_substrings(S :: unicode:unicode_binary()) -> integer().
number_of_substrings(S) ->
    N = byte_size(S),
    Bytes = binary_to_list(S),

    %% Build prefix sums and zero positions
    {PrefListRev, ZeroPosRev, _Ones} = build_lists(Bytes, 0, [0], []),
    PrefList = lists:reverse(PrefListRev),          % length N+1, pref[0]=0 ... pref[N]
    ZeroPosList = lists:reverse(ZeroPosRev),

    PrefTuple = list_to_tuple(PrefList),            % tuple for O(1) access
    ZeroTuple = list_to_tuple(ZeroPosList),
    Zlen = tuple_size(ZeroTuple),

    K = trunc(math:sqrt(N)),
    count_from_left(0, N, ZeroTuple, Zlen, PrefTuple, K, 0).

%% build_lists(Bytes, Index, PrefAcc, ZeroAcc) -> {PrefAccRev, ZeroAccRev, Ones}
build_lists([], _Idx, PrefAcc, ZeroAcc) ->
    {PrefAcc, ZeroAcc, undefined};
build_lists([C|Rest], Idx, PrefAcc, ZeroAcc) ->
    PrevOnes = hd(PrefAcc),
    NewOnes = case C of
        $49 -> PrevOnes + 1;   % '1'
        _   -> PrevOnes
    end,
    NewPrefAcc = [NewOnes | PrefAcc],
    NewZeroAcc = case C of
        $48 -> [Idx | ZeroAcc]; % '0'
        _   -> ZeroAcc
    end,
    build_lists(Rest, Idx + 1, NewPrefAcc, NewZeroAcc).

%% count_from_left(L, N, ZeroTuple, Zlen, PrefTuple, K, Acc) -> total answer
count_from_left(N, N, _, _, _, _, Acc) ->
    Acc;
count_from_left(L, N, ZeroTuple, Zlen, PrefTuple, K, Acc) ->
    Idx = lower_bound(ZeroTuple, Zlen, L),
    NextZeroPos = if
        Idx < Zlen -> element(Idx + 1, ZeroTuple);
        true       -> N
    end,
    Count0 = NextZeroPos - L,
    NewAcc0 = Acc + Count0,
    MaxK = K,
    NewAcc = count_k(1, MaxK, Idx, L, N, ZeroTuple, Zlen, PrefTuple, NewAcc0),
    count_from_left(L + 1, N, ZeroTuple, Zlen, PrefTuple, K, NewAcc).

%% iterate over k zeros (k from Cur to MaxK)
count_k(CurK, MaxK, IdxStart, L, N, ZeroTuple, Zlen, PrefTuple, Acc) when CurK =< MaxK,
    (IdxStart + CurK - 1) < Zlen ->
    ZkPos = element(IdxStart + CurK, ZeroTuple), % kth zero position
    Limit = if
        (IdxStart + CurK) < Zlen -> element(IdxStart + CurK + 1, ZeroTuple) - 1;
        true                     -> N - 1
    end,
    TargetOnes = element(L + 1, PrefTuple) + CurK * CurK,
    LowPrefIdx = ZkPos + 1,
    FirstPrefIdx = pref_lower_bound(PrefTuple, N, LowPrefIdx, TargetOnes),
    Add =
        if
            FirstPrefIdx =< N ->
                R0 = max(ZkPos, FirstPrefIdx - 1),
                if R0 =< Limit -> Limit - R0 + 1;
                   true       -> 0
                end;
            true -> 0
        end,
    count_k(CurK + 1, MaxK, IdxStart, L, N, ZeroTuple, Zlen, PrefTuple, Acc + Add);
count_k(_, _, _, _, _, _, _, _, Acc) ->
    Acc.

%% lower_bound on zero positions tuple: first index >= Value
lower_bound(ZeroTuple, Zlen, Value) ->
    lower_bound_loop(0, Zlen, Value, ZeroTuple).

lower_bound_loop(L, R, Value, ZeroTuple) when L < R ->
    M = (L + R) div 2,
    Elem = element(M + 1, ZeroTuple),
    if
        Elem >= Value -> lower_bound_loop(L, M, Value, ZeroTuple);
        true          -> lower_bound_loop(M + 1, R, Value, ZeroTuple)
    end;
lower_bound_loop(L, _R, _Value, _ZeroTuple) ->
    L.

%% pref_lower_bound: first index in [LowIdx..N] where pref >= Target
pref_lower_bound(PrefTuple, N, LowIdx, Target) ->
    pref_lower_bound_loop(LowIdx, N, Target, PrefTuple).

pref_lower_bound_loop(L, R, Target, PrefTuple) when L < R ->
    M = (L + R) div 2,
    Val = element(M + 1, PrefTuple),
    if
        Val >= Target -> pref_lower_bound_loop(L, M, Target, PrefTuple);
        true          -> pref_lower_bound_loop(M + 1, R, Target, PrefTuple)
    end;
pref_lower_bound_loop(L, _R, Target, PrefTuple) ->
    case element(L + 1, PrefTuple) >= Target of
        true -> L;
        false -> N + 1   % not found; will be handled by caller
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_substrings(s :: String.t()) :: integer
  def number_of_substrings(s) do
    n = String.length(s)
    chars = String.to_charlist(s)

    # prefix sums of ones (tuple for O(1) access)
    {pref_rev, zero_list_rev} =
      Enum.reduce(Enum.with_index(chars), {[], []}, fn {c, idx}, {pref_acc, zeros_acc} ->
        prev = case pref_acc do
          [] -> 0
          [last | _] -> last
        end

        new_sum = prev + if c == ?1, do: 1, else: 0
        pref_new = [new_sum | pref_acc]
        zeros_new = if c == ?0, do: [idx | zeros_acc], else: zeros_acc
        {pref_new, zeros_new}
      end)

    pref_list = Enum.reverse([0 | pref_rev])
    pref = List.to_tuple(pref_list)

    zero_pos = Enum.reverse(zero_list_rev)
    zero_tuple = List.to_tuple(zero_pos)
    m = tuple_size(zero_tuple)

    # count substrings consisting only of ones
    {ans_one, run} =
      Enum.reduce(chars, {0, 0}, fn c, {acc, cur_run} ->
        if c == ?1 do
          {acc, cur_run + 1}
        else
          {acc + div(cur_run * (cur_run + 1), 2), 0}
        end
      end)

    ans_one = ans_one + div(run * (run + 1), 2)

    b = :math.sqrt(n) |> trunc

    # helper binary searches
    lower_bound = fn(arr, size, target) ->
      lb = fn lo, hi, f ->
        if lo < hi do
          mid = div(lo + hi, 2)
          if elem(arr, mid) < target do
            f.(mid + 1, hi, f)
          else
            f.(lo, mid, f)
          end
        else
          lo
        end
      end

      lb.(0, size, lb)
    end

    binary_search_min_r = fn l, needed, lo, hi, pref_tuple ->
      bs = fn lo2, hi2, f ->
        if lo2 == hi2 do
          lo2
        else
          mid = div(lo2 + hi2, 2)
          cur = elem(pref_tuple, mid + 1) - elem(pref_tuple, l)

          if cur >= needed do
            f.(lo2, mid, f)
          else
            f.(mid + 1, hi2, f)
          end
        end
      end

      bs.(lo, hi, bs)
    end

    total =
      Enum.reduce(0..(n - 1), ans_one, fn l, acc ->
        idx = lower_bound.(zero_tuple, m, l)

        max_iter = min(b, m - idx)

        Enum.reduce(0..(max_iter - 1), acc, fn t, inner_acc ->
          r_zero = elem(zero_tuple, idx + t)
          zeros = t + 1
          needed = zeros * zeros

          max_r =
            if idx + t + 1 < m do
              elem(zero_tuple, idx + t + 1) - 1
            else
              n - 1
            end

          total_ones_max = elem(pref, max_r + 1) - elem(pref, l)

          if total_ones_max < needed do
            inner_acc
          else
            min_r = binary_search_min_r.(l, needed, r_zero, max_r, pref)
            inner_acc + (max_r - min_r + 1)
          end
        end)
      end)

    total
  end
end
```
