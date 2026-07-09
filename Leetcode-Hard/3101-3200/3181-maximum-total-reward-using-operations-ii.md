# 3181. Maximum Total Reward Using Operations II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxTotalReward(vector<int>& rewardValues) {
        if (rewardValues.empty()) return 0;
        sort(rewardValues.begin(), rewardValues.end());
        int maxV = *max_element(rewardValues.begin(), rewardValues.end());
        int limit = 2 * maxV;                     // maximum possible total reward
        int WORDS = (limit + 64) / 64;            // number of 64‑bit words
        
        vector<unsigned long long> bits(WORDS, 0);
        bits[0] = 1ULL;                           // dp[0] = true
        
        for (int v : rewardValues) {
            // copy current reachable sums
            vector<unsigned long long> src(bits);
            
            // mask out positions >= v (they cannot be used to add v)
            int fullWords = v / 64;
            int remBits   = v % 64;
            for (int i = fullWords + 1; i < WORDS; ++i) src[i] = 0;
            if (remBits) {
                unsigned long long mask = (1ULL << remBits) - 1;
                src[fullWords] &= mask;
            } else {
                if (fullWords < WORDS) src[fullWords] = 0;
            }
            
            // shift left by v bits
            int wordShift = v / 64;
            int bitShift  = v % 64;
            vector<unsigned long long> shifted(WORDS, 0);
            for (int i = 0; i < WORDS; ++i) {
                unsigned long long val = src[i];
                if (!val) continue;
                int j = i + wordShift;
                if (j < WORDS) {
                    shifted[j] |= val << bitShift;
                }
                if (bitShift && j + 1 < WORDS) {
                    shifted[j + 1] |= val >> (64 - bitShift);
                }
            }
            
            // merge new reachable sums
            for (int i = 0; i < WORDS; ++i) bits[i] |= shifted[i];
        }
        
        // find the maximum achievable total reward
        for (int idx = limit; idx >= 0; --idx) {
            int w = idx / 64;
            int b = idx % 64;
            if (bits[w] & (1ULL << b)) return idx;
        }
        return 0;
    }
};
```

## Java

```java
class Solution {
    public int maxTotalReward(int[] rewardValues) {
        java.util.Arrays.sort(rewardValues);
        int n = rewardValues.length;
        int maxVal = rewardValues[n - 1];
        int limit = maxVal * 2 + 1; // maximum possible total reward
        int words = (limit + 63) >>> 6;
        long[] bits = new long[words];
        bits[0] = 1L; // sum 0 is reachable

        for (int v : rewardValues) {
            // copy current bits but keep only sums < v
            long[] src = bits.clone();
            int maxIdx = v - 1;
            if (maxIdx >= 0) {
                int clearWordStart = (maxIdx >>> 6) + 1;
                for (int i = clearWordStart; i < words; ++i) {
                    src[i] = 0L;
                }
                // also mask the word containing maxIdx to keep bits <= maxIdx
                int maskBits = (maxIdx & 63);
                if (maskBits != 63) {
                    long mask = (1L << (maskBits + 1)) - 1;
                    src[maxIdx >>> 6] &= mask;
                }
            } else {
                // v == 0, nothing can be added
                continue;
            }

            int wordShift = v >>> 6;
            int bitShift = v & 63;

            long[] shifted = new long[words];
            if (bitShift == 0) {
                for (int i = 0; i + wordShift < words; ++i) {
                    shifted[i + wordShift] |= src[i];
                }
            } else {
                for (int i = 0; i + wordShift < words; ++i) {
                    long cur = src[i];
                    shifted[i + wordShift] |= cur << bitShift;
                    if (i + wordShift + 1 < words) {
                        shifted[i + wordShift + 1] |= cur >>> (64 - bitShift);
                    }
                }
            }

            // merge shifted into bits
            for (int i = 0; i < words; ++i) {
                bits[i] |= shifted[i];
            }
        }

        // find the maximum reachable sum
        int ans = 0;
        for (int i = words - 1; i >= 0; --i) {
            long w = bits[i];
            if (w != 0) {
                int msb = 63 - Long.numberOfLeadingZeros(w);
                ans = (i << 6) + msb;
                break;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxTotalReward(self, rewardValues):
        """
        :type rewardValues: List[int]
        :rtype: int
        """
        vals = sorted(rewardValues)
        max_v = vals[-1]
        limit = 2 * max_v  # maximum possible total reward
        bits = 1  # bit i is set if sum i is achievable
        mask_limit = (1 << (limit + 1)) - 1
        for v in vals:
            # only sums strictly less than v can be extended by v
            eligible = bits & ((1 << v) - 1)
            bits |= (eligible << v)
            bits &= mask_limit  # keep within bound
        return bits.bit_length() - 1
```

## Python3

```python
class Solution:
    def maxTotalReward(self, rewardValues):
        from typing import List
        rewardValues.sort()
        maxv = rewardValues[-1]
        limit = 2 * maxv
        dp = 1  # bit 0 is set
        mask_limit = (1 << (limit + 1)) - 1
        for a in rewardValues:
            low = dp & ((1 << a) - 1)   # sums less than a
            dp |= low << a
            if dp.bit_length() > limit + 1:
                dp &= mask_limit
        return dp.bit_length() - 1
```

## C

```c
#include <stdlib.h>
#include <string.h>

int maxTotalReward(int* rewardValues, int rewardValuesSize) {
    if (rewardValuesSize == 0) return 0;
    // sort the array
    qsort(rewardValues, rewardValuesSize, sizeof(int), (__compar_fn_t) (int (*)(const void *, const void *)) 
        [](const void *a, const void *b){return *(int*)a - *(int*)b;});
    
    int maxVal = 0;
    for (int i = 0; i < rewardValuesSize; ++i)
        if (rewardValues[i] > maxVal) maxVal = rewardValues[i];
    
    int limit = maxVal * 2;               // maximum possible total reward
    int words = (limit >> 6) + 2;         // number of 64‑bit blocks
    
    unsigned long long *bits = (unsigned long long*)calloc(words, sizeof(unsigned long long));
    if (!bits) return 0;
    bits[0] = 1ULL;                       // sum 0 is reachable
    
    for (int idx = 0; idx < rewardValuesSize; ++idx) {
        int v = rewardValues[idx];
        // make a masked copy of current bits (only sums < v)
        unsigned long long *tmp = (unsigned long long*)malloc(words * sizeof(unsigned long long));
        if (!tmp) { free(bits); return 0; }
        memcpy(tmp, bits, words * sizeof(unsigned long long));
        
        int fullWords = v >> 6;           // number of whole words completely before v
        int remBits   = v & 63;           // remaining bits in the word containing index v-1
        
        // clear bits >= v
        if (remBits) {
            unsigned long long mask = (1ULL << remBits) - 1;
            tmp[fullWords] &= mask;
            for (int i = fullWords + 1; i < words; ++i) tmp[i] = 0ULL;
        } else {
            for (int i = fullWords; i < words; ++i) tmp[i] = 0ULL;
        }
        
        // shift left by v and OR into bits
        int wordShift = v >> 6;
        int bitShift  = v & 63;
        if (bitShift == 0) {
            for (int i = words - 1; i >= wordShift; --i)
                bits[i] |= tmp[i - wordShift];
        } else {
            for (int i = words - 1; i >= 0; --i) {
                unsigned long long val = 0ULL;
                if (i - wordShift >= 0) {
                    val = tmp[i - wordShift] << bitShift;
                    if (i - wordShift - 1 >= 0)
                        val |= tmp[i - wordShift - 1] >> (64 - bitShift);
                }
                bits[i] |= val;
            }
        }
        free(tmp);
    }
    
    // find maximum reachable sum
    for (int s = limit; s >= 0; --s) {
        int w = s >> 6;
        int b = s & 63;
        if ((bits[w] >> b) & 1ULL) {
            free(bits);
            return s;
        }
    }
    free(bits);
    return 0;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxTotalReward(int[] rewardValues) {
        Array.Sort(rewardValues);
        int maxV = 0;
        foreach (int v in rewardValues) if (v > maxV) maxV = v;
        int limit = maxV * 2; // maximum possible total reward
        int totalBits = limit + 1;
        int wordCount = (totalBits + 63) >> 6;
        ulong[] bits = new ulong[wordCount];
        bits[0] = 1UL; // sum 0 is reachable

        foreach (int v in rewardValues) {
            // copy current reachable sums
            ulong[] orig = new ulong[wordCount];
            Array.Copy(bits, orig, wordCount);

            // mask out sums >= v (they cannot be used to add v)
            int startWord = v >> 6;
            int startBit = v & 63;
            if (startBit == 0) {
                for (int i = startWord; i < wordCount; ++i) orig[i] = 0UL;
            } else {
                ulong mask = (1UL << startBit) - 1;
                orig[startWord] &= mask;
                for (int i = startWord + 1; i < wordCount; ++i) orig[i] = 0UL;
            }

            // shift left by v and OR into bits
            int ws = v >> 6;
            int bs = v & 63;
            if (bs == 0) {
                for (int i = wordCount - 1; i >= ws; --i) {
                    bits[i] |= orig[i - ws];
                }
            } else {
                for (int i = wordCount - 1; i > ws; --i) {
                    ulong low = orig[i - ws] << bs;
                    ulong high = orig[i - ws - 1] >> (64 - bs);
                    bits[i] |= low | high;
                }
                // handle the lowest affected word
                bits[ws] |= orig[0] << bs;
            }
        }

        for (int i = limit; i >= 0; --i) {
            int w = i >> 6;
            int b = i & 63;
            if ((bits[w] & (1UL << b)) != 0) return i;
        }
        return 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} rewardValues
 * @return {number}
 */
var maxTotalReward = function(rewardValues) {
    if (!rewardValues || rewardValues.length === 0) return 0;
    rewardValues.sort((a, b) => a - b);
    const maxV = rewardValues[rewardValues.length - 1];
    const limit = maxV * 2 + 1;                 // maximum possible sum we need to track
    const words = (limit + 31) >> 5;            // number of 32‑bit blocks
    const bits = new Uint32Array(words);
    bits[0] = 1;                                // sum 0 is reachable

    for (let idx = 0; idx < rewardValues.length; ++idx) {
        const v = rewardValues[idx];
        const wordShift = v >>> 5;              // shift in whole words
        const offset = v & 31;                  // remaining bit shift
        const maxBitIdx = v - 1;
        if (maxBitIdx < 0) continue;
        const maxWordIdx = maxBitIdx >>> 5;

        for (let s = 0; s <= maxWordIdx; ++s) {
            let src = bits[s];
            if (src === 0) continue;

            // mask out bits that correspond to sums >= v in the highest word
            if (s === maxWordIdx) {
                const excessBits = ((maxWordIdx + 1) << 5) - v; // bits beyond v-1
                if (excessBits > 0) {
                    src &= (0xFFFFFFFF >>> excessBits);
                    if (src === 0) continue;
                }
            }

            const dst = s + wordShift;
            if (dst < words) {
                bits[dst] |= (src << offset) >>> 0;
            }
            if (offset !== 0 && dst + 1 < words) {
                bits[dst + 1] |= src >>> (32 - offset);
            }
        }
    }

    // find the largest reachable sum
    for (let i = words - 1; i >= 0; --i) {
        let w = bits[i];
        if (w !== 0) {
            for (let b = 31; b >= 0; --b) {
                if ((w >>> b) & 1) {
                    return i * 32 + b;
                }
            }
        }
    }
    return 0;
};
```

## Typescript

```typescript
function maxTotalReward(rewardValues: number[]): number {
    if (rewardValues.length === 0) return 0;
    rewardValues.sort((a, b) => a - b);
    const maxVal = rewardValues[rewardValues.length - 1];
    const limit = maxVal * 2; // maximum possible total reward
    const bits = limit + 1;
    const WORD_SIZE = 32;
    const words = (bits + WORD_SIZE - 1) >> 5; // ceil(bits/32)

    let dp = new Uint32Array(words);
    dp[0] = 1; // sum 0 is reachable

    for (const a of rewardValues) {
        const wordShift = a >>> 5; // divide by 32
        const bitShift = a & 31;   // modulo 32

        // shifted version based on previous state
        const shifted = new Uint32Array(words);
        for (let i = words - 1; i >= 0; --i) {
            const srcIdx = i - wordShift;
            if (srcIdx < 0) continue;
            let val = dp[srcIdx] << bitShift;
            if (bitShift !== 0 && srcIdx > 0) {
                val |= dp[srcIdx - 1] >>> (WORD_SIZE - bitShift);
            }
            shifted[i] = val >>> 0; // ensure unsigned
        }

        // apply condition sum < 2*a
        const maxSumAllowed = Math.min(limit, a * 2 - 1);
        const maxWordIdx = maxSumAllowed >>> 5;
        for (let i = maxWordIdx + 1; i < words; ++i) {
            shifted[i] = 0;
        }
        if (maxWordIdx < words) {
            const bitsInLast = (maxSumAllowed & 31) + 1; // inclusive
            if (bitsInLast !== WORD_SIZE) {
                const mask = (1 << bitsInLast) - 1;
                shifted[maxWordIdx] &= mask;
            }
        }

        // merge into dp
        for (let i = 0; i < words; ++i) {
            dp[i] |= shifted[i];
        }
    }

    // find maximum reachable sum
    for (let sum = limit; sum >= 0; --sum) {
        const wordIdx = sum >>> 5;
        const bitIdx = sum & 31;
        if ((dp[wordIdx] >>> bitIdx) & 1) return sum;
    }
    return 0;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $rewardValues
     * @return Integer
     */
    function maxTotalReward($rewardValues) {
        if (empty($rewardValues)) return 0;
        sort($rewardValues);
        $maxVal = max($rewardValues);
        $maxSum = $maxVal * 2; // upper bound of achievable sum

        $wordSize = 64;
        $numWords = intdiv($maxSum + $wordSize, $wordSize); // enough words to hold bits up to maxSum
        $dp = array_fill(0, $numWords, 0);
        $dp[0] = 1; // sum 0 is reachable

        foreach ($rewardValues as $v) {
            $wordShift = intdiv($v, $wordSize);
            $offset = $v % $wordSize;

            // number of bits we are allowed to use from previous dp (s < v)
            $limitBits = $v;
            if ($limitBits == 0) continue; // nothing can be added
            $limitWords = intdiv($limitBits + $wordSize - 1, $wordSize); // ceil

            for ($i = 0; $i < $limitWords; ++$i) {
                $word = $dp[$i];
                // mask out bits beyond limit in the highest considered word
                if ($i == $limitWords - 1) {
                    $bitsInWord = $limitBits % $wordSize;
                    if ($bitsInWord != 0) {
                        $mask = (1 << $bitsInWord) - 1;
                        $word &= $mask;
                    }
                }
                if ($word == 0) continue;

                $targetIdx = $i + $wordShift;
                if ($offset == 0) {
                    $dp[$targetIdx] |= $word;
                } else {
                    // left part within the target word
                    $dp[$targetIdx] |= ($word << $offset);
                    // carry to next word if exists
                    if ($targetIdx + 1 < $numWords) {
                        $dp[$targetIdx + 1] |= ($word >> (64 - $offset));
                    }
                }
            }
        }

        // find maximum reachable sum
        for ($pos = $maxSum; $pos >= 0; --$pos) {
            $wi = intdiv($pos, 64);
            $bi = $pos % 64;
            if ((($dp[$wi] >> $bi) & 1) == 1) {
                return $pos;
            }
        }
        return 0;
    }
}
```

## Swift

```swift
class Solution {
    func maxTotalReward(_ rewardValues: [Int]) -> Int {
        let sorted = rewardValues.sorted()
        guard let maxV = sorted.max() else { return 0 }
        let limit = maxV * 2
        let size = limit + 1
        let wordCount = (size + 63) >> 6
        
        var dp = [UInt64](repeating: 0, count: wordCount)
        dp[0] = 1   // sum 0 is reachable
        
        var masked = [UInt64](repeating: 0, count: wordCount)
        var shifted = [UInt64](repeating: 0, count: wordCount)
        
        for v in sorted {
            let shiftWords = v >> 6          // v / 64
            let offset = v & 63              // v % 64
            
            // mask bits that are < v
            for i in 0..<wordCount {
                let startBit = i << 6        // i * 64
                if startBit + 63 < v {       // whole word is within range
                    masked[i] = dp[i]
                } else if startBit > v - 1 { // completely out of range
                    masked[i] = 0
                } else {
                    let bits = v - startBit   // 1..63
                    let mask: UInt64 = (UInt64(1) << bits) - 1
                    masked[i] = dp[i] & mask
                }
            }
            
            // shift left by v bits
            for i in 0..<wordCount { shifted[i] = 0 }   // clear
            if offset == 0 {
                for i in stride(from: wordCount - 1, through: 0, by: -1) {
                    let src = i - shiftWords
                    if src >= 0 {
                        shifted[i] = masked[src]
                    }
                }
            } else {
                for i in stride(from: wordCount - 1, through: 0, by: -1) {
                    let src = i - shiftWords
                    if src < 0 { continue }
                    var val = masked[src] << offset
                    if src > 0 {
                        val |= masked[src - 1] >> (64 - offset)
                    }
                    shifted[i] = val
                }
            }
            
            // dp |= shifted
            for i in 0..<wordCount {
                dp[i] |= shifted[i]
            }
        }
        
        // find maximum reachable sum
        var answer = 0
        for s in stride(from: limit, through: 0, by: -1) {
            let wordIdx = s >> 6
            let bitIdx = s & 63
            if ((dp[wordIdx] >> bitIdx) & 1) == 1 {
                answer = s
                break
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    fun maxTotalReward(rewardValues: IntArray): Int {
        if (rewardValues.isEmpty()) return 0
        val sorted = rewardValues.sorted()
        val maxV = sorted.last()
        val limitSum = 2 * maxV
        val wordCount = (limitSum + 64) / 64
        val bits = LongArray(wordCount)
        bits[0] = 1L // sum 0 is reachable

        val src = LongArray(wordCount)

        for (v in sorted) {
            // copy bits that correspond to sums < v into src
            val limit = v
            if (limit == 0) continue
            val lastWordIdx = (limit - 1) / 64
            // clear src first up to needed range
            for (i in 0..lastWordIdx) {
                src[i] = bits[i]
            }
            // mask out bits >= v in the last word
            val rem = limit % 64
            if (rem != 0) {
                val mask = (1L shl rem) - 1
                src[lastWordIdx] = src[lastWordIdx] and mask
            }

            // shift left by v and OR into bits
            val shiftWords = v / 64
            val shiftBits = v % 64
            for (i in wordCount - 1 downTo 0) {
                var shifted = 0L
                val srcIdx = i - shiftWords
                if (srcIdx >= 0) {
                    shifted = src[srcIdx] shl shiftBits
                    if (shiftBits != 0 && srcIdx - 1 >= 0) {
                        shifted = shifted or (src[srcIdx - 1] ushr (64 - shiftBits))
                    }
                }
                bits[i] = bits[i] or shifted
            }
        }

        // find maximum reachable sum
        for (sum in limitSum downTo 0) {
            val wordIdx = sum / 64
            val bitPos = sum % 64
            if (((bits[wordIdx] ushr bitPos) and 1L) == 1L) return sum
        }
        return 0
    }
}
```

## Dart

```dart
class Solution {
  int maxTotalReward(List<int> rewardValues) {
    if (rewardValues.isEmpty) return 0;
    rewardValues.sort();
    int maxV = rewardValues.last;
    int limit = maxV * 2; // maximum possible total reward
    BigInt dp = BigInt.one; // bit 0 is set

    for (int v in rewardValues) {
      // keep only sums that are less than v
      BigInt lowMask = (BigInt.one << v) - BigInt.one;
      BigInt low = dp & lowMask;
      if (low != BigInt.zero) {
        dp |= (low << v);
      }
    }

    for (int i = limit; i >= 0; --i) {
      if (((dp >> i) & BigInt.one) == BigInt.one) return i;
    }
    return 0;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

func maxTotalReward(rewardValues []int) int {
	if len(rewardValues) == 0 {
		return 0
	}
	sort.Ints(rewardValues)
	maxVal := rewardValues[len(rewardValues)-1]
	limit := maxVal * 2 // maximum possible sum we need to track

	size := (limit >> 6) + 1 // number of uint64 words
	dp := make([]uint64, size)
	dp[0] = 1 // sum 0 is reachable

	for _, v := range rewardValues {
		shiftWords := v >> 6
		shiftBits := uint(v & 63)

		shifted := make([]uint64, size)

		// shift left by v bits
		for i := size - 1; i >= 0; i-- {
			var cur uint64
			if i-shiftWords >= 0 {
				cur = dp[i-shiftWords] << shiftBits
				if shiftBits != 0 && i-shiftWords-1 >= 0 {
					cur |= dp[i-shiftWords-1] >> (64 - shiftBits)
				}
			}
			shifted[i] = cur
		}

		// mask bits where j < 2*v
		maxIdx := 2*v - 1
		if maxIdx > limit {
			maxIdx = limit
		}
		maskWord := maxIdx >> 6
		maskBit := uint(maxIdx & 63)

		for i := maskWord + 1; i < size; i++ {
			shifted[i] = 0
		}
		if maskWord < size {
			shifted[maskWord] &= (uint64(1) << (maskBit + 1)) - 1
		}

		// dp |= shifted
		for i := 0; i < size; i++ {
			dp[i] |= shifted[i]
		}
	}

	// find maximum reachable sum
	for s := limit; s >= 0; s-- {
		word := s >> 6
		bit := uint(s & 63)
		if (dp[word]>>bit)&1 == 1 {
			return s
		}
	}
	return 0
}
```

## Ruby

```ruby
def max_total_reward(reward_values)
  reward_values.sort!
  max_v = reward_values.max
  limit = max_v * 2
  mask = (1 << (limit + 1)) - 1
  bits = 1
  reward_values.each do |v|
    low = bits & ((1 << v) - 1)
    bits |= (low << v)
    bits &= mask
  end
  bits.bit_length - 1
end
```

## Scala

```scala
object Solution {
    def maxTotalReward(rewardValues: Array[Int]): Int = {
        java.util.Arrays.sort(rewardValues)
        val maxV = rewardValues.max
        val limit = maxV * 2                     // maximum possible total reward
        val words = (limit >>> 6) + 1            // number of 64‑bit blocks needed
        var bits = new Array[Long](words)
        bits(0) = 1L                             // sum 0 is achievable

        for (v <- rewardValues) {
            val src = bits.clone()
            val shiftWords = v >>> 6
            val shiftBits = v & 63
            val maxSrcIdx = (v - 1) >>> 6        // last word that may contain allowed sums

            var srcIdx = 0
            while (srcIdx <= maxSrcIdx && srcIdx < src.length) {
                var w = src(srcIdx)
                if (srcIdx == maxSrcIdx) {
                    val bitsToKeep = v - (srcIdx << 6) // number of valid bits in this word (1..64)
                    val mask =
                        if (bitsToKeep == 64) -1L
                        else (1L << bitsToKeep) - 1
                    w &= mask
                }
                if (w != 0L) {
                    val tgtIdx = srcIdx + shiftWords
                    if (tgtIdx < bits.length) {
                        if (shiftBits == 0) {
                            bits(tgtIdx) |= w
                        } else {
                            bits(tgtIdx) |= w << shiftBits
                            if (tgtIdx + 1 < bits.length) {
                                bits(tgtIdx + 1) |= w >>> (64 - shiftBits)
                            }
                        }
                    }
                }
                srcIdx += 1
            }
        }

        var idx = limit
        while (idx >= 0) {
            val wordIdx = idx >>> 6
            val bitPos = idx & 63
            if ((bits(wordIdx) & (1L << bitPos)) != 0L) return idx
            idx -= 1
        }
        0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_total_reward(mut reward_values: Vec<i32>) -> i32 {
        if reward_values.is_empty() {
            return 0;
        }
        reward_values.sort_unstable();
        let max_val = *reward_values.iter().max().unwrap() as usize;
        let limit = 2 * max_val + 1; // maximum possible sum
        let word_len = (limit + 63) / 64;
        let mut dp = vec![0u64; word_len];
        dp[0] = 1; // sum 0 is reachable

        for &val in reward_values.iter() {
            let v = val as usize;

            // shift left by v bits
            let shifted = Self::shift_left(&dp, v, limit);
            let mut add_bits = shifted;

            // keep only sums < 2*v (since we can only use previous sums < v)
            let upper = 2 * v;
            if upper < limit {
                let start_word = upper / 64;
                let bit_offset = upper % 64;
                if bit_offset == 0 {
                    for w in start_word..word_len {
                        add_bits[w] = 0;
                    }
                } else {
                    add_bits[start_word] &= (1u64 << bit_offset) - 1;
                    for w in start_word + 1..word_len {
                        add_bits[w] = 0;
                    }
                }
            }

            // merge new reachable sums
            for i in 0..word_len {
                dp[i] |= add_bits[i];
            }
        }

        // find the maximum reachable sum
        for s in (0..limit).rev() {
            let word = s / 64;
            let bit = s % 64;
            if ((dp[word] >> bit) & 1) == 1 {
                return s as i32;
            }
        }
        0
    }

    fn shift_left(bits: &[u64], shift: usize, limit: usize) -> Vec<u64> {
        let word_len = bits.len();
        if shift == 0 {
            return bits.to_vec();
        }
        let mut res = vec![0u64; word_len];
        let word_shift = shift / 64;
        let bit_shift = shift % 64;

        for i in (0..word_len).rev() {
            if i < word_shift {
                continue;
            }
            let src = i - word_shift;
            let mut val = bits[src] << bit_shift;
            if bit_shift != 0 && src > 0 {
                val |= bits[src - 1] >> (64 - bit_shift);
            }
            res[i] = val;
        }

        // clear bits beyond the limit
        let excess_bits = word_len * 64 - limit;
        if excess_bits > 0 {
            let mask = (!0u64) >> excess_bits;
            if let Some(last) = res.last_mut() {
                *last &= mask;
            }
        }
        res
    }
}
```

## Racket

```racket
#lang racket
(require racket/contract)

(define/contract (max-total-reward rewardValues)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((vals (sort rewardValues <))
         (dp 1)) ; bit 0 set
    (for ([v vals])
      (let* ((mask (sub1 (arithmetic-shift 1 v)))   ; bits < v
             (low (bitwise-and dp mask))
             (new (arithmetic-shift low v)))
        (set! dp (bitwise-ior dp new))))
    (sub1 (integer-length dp))))
```

## Erlang

```erlang
-spec max_total_reward(RewardValues :: [integer()]) -> integer().
max_total_reward(RewardValues) ->
    Sorted = lists:sort(RewardValues),
    MaxV = case Sorted of
        [] -> 0;
        _ -> hd(lists:reverse(Sorted))
    end,
    Bits = lists:foldl(
        fun(R, Acc) ->
            Shifted = Acc bsl R,
            MaskLimit = 2 * R,
            Mask = (1 bsl MaskLimit) - 1,
            Candidate = Shifted band Mask,
            Acc bor Candidate
        end,
        1,
        Sorted),
    find_max(Bits, 2 * MaxV).

find_max(_Bits, -1) -> 0;
find_max(Bits, Pos) ->
    case Bits band (1 bsl Pos) of
        0 -> find_max(Bits, Pos - 1);
        _ -> Pos
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_total_reward(reward_values :: [integer]) :: integer
  def max_total_reward(reward_values) do
    sorted = Enum.sort(reward_values)

    dp =
      Enum.reduce(sorted, 1, fn v, acc ->
        mask = (1 <<< v) - 1
        candidates = Bitwise.band(acc, mask)
        candidates = Bitwise.shift_left(candidates, v)
        Bitwise.bor(acc, candidates)
      end)

    trunc(:math.log2(dp))
  end
end
```
