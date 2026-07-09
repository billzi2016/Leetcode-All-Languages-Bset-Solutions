# 0466. Count The Repetitions

## Cpp

```cpp
class Solution {
public:
    int getMaxRepetitions(string s1, int n1, string s2, int n2) {
        if (n1 == 0) return 0;
        vector<int> recall(s2.size() + 1, -1);
        vector<int> s1cntRec(s2.size() + 1, 0), s2cntRec(s2.size() + 1, 0);
        int s1cnt = 0;          // number of processed s1 blocks
        int index = 0;          // current position in s2
        int s2cnt = 0;          // total completed s2 sequences

        while (true) {
            ++s1cnt;
            for (char c : s1) {
                if (c == s2[index]) {
                    ++index;
                    if (index == (int)s2.size()) {
                        index = 0;
                        ++s2cnt;
                    }
                }
            }
            if (s1cnt == n1) return s2cnt / n2;

            if (recall[index] != -1) {
                int preS1Cnt = recall[index];
                int preS2Cnt = s2cntRec[index];

                int periodS1 = s1cnt - preS1Cnt;
                int periodS2 = s2cnt - preS2Cnt;

                int remain = n1 - s1cnt;
                int loops = remain / periodS1;
                s1cnt += loops * periodS1;
                s2cnt += loops * periodS2;
            }

            recall[index] = s1cnt;
            s2cntRec[index] = s2cnt;
        }
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int getMaxRepetitions(String s1, int n1, String s2, int n2) {
        // Quick check: if any character in s2 does not appear in s1, answer is 0
        boolean[] present = new boolean[26];
        for (char c : s1.toCharArray()) {
            present[c - 'a'] = true;
        }
        for (char c : s2.toCharArray()) {
            if (!present[c - 'a']) return 0;
        }

        int s1Len = s1.length();
        int s2Len = s2.length();

        // recallIndex[pos] stores the number of processed s1 blocks when we first saw position pos in s2
        // recallCount[pos] stores the total completed s2 strings at that moment
        int[] recallIndex = new int[s2Len + 1];
        int[] recallCount = new int[s2Len + 1];
        Arrays.fill(recallIndex, -1);

        int s1Count = 0; // how many s1 blocks have been processed
        int s2Count = 0; // how many full s2 strings have been matched
        int pos = 0;     // current position in s2 (0 .. s2Len-1)

        while (s1Count < n1) {
            s1Count++;
            for (int i = 0; i < s1Len; i++) {
                if (s1.charAt(i) == s2.charAt(pos)) {
                    pos++;
                    if (pos == s2Len) {
                        s2Count++;
                        pos = 0;
                    }
                }
            }

            // Detect a previously seen state to form a loop
            if (recallIndex[pos] != -1) {
                int prevS1Count = recallIndex[pos];
                int prevS2Count = recallCount[pos];

                int loopS1 = s1Count - prevS1Count;
                int loopS2 = s2Count - prevS2Count;

                int remainingS1 = n1 - s1Count;
                if (loopS1 > 0) {
                    int loops = remainingS1 / loopS1;
                    s1Count += loops * loopS1;
                    s2Count += loops * loopS2;
                }
            } else {
                recallIndex[pos] = s1Count;
                recallCount[pos] = s2Count;
            }
        }

        return s2Count / n2;
    }
}
```

## Python

```python
class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if not s1 or not s2:
            return 0

        # quick check: if a character in s2 never appears in s1, answer is 0
        set_s1 = set(s1)
        for ch in set(s2):
            if ch not in set_s1:
                return 0

        j = 0               # position in s2
        count_s2 = 0        # how many full s2 have been matched
        index_record = {}   # maps j -> (i, count_s2) where i is number of processed s1 blocks

        i = 0
        while i < n1:
            i += 1
            for ch in s1:
                if ch == s2[j]:
                    j += 1
                    if j == len(s2):
                        j = 0
                        count_s2 += 1

            # after processing i-th block of s1
            if j in index_record:
                prev_i, prev_count = index_record[j]

                # pre-loop part length and count
                pre_loop_blocks = prev_i
                pre_loop_count = prev_count

                # loop part length and count
                loop_blocks = i - prev_i
                loop_count = count_s2 - prev_count

                # how many full loops can we still fit
                remaining_blocks = n1 - i
                loops = remaining_blocks // loop_blocks

                count_s2 += loops * loop_count
                i += loops * loop_blocks

                # process the rest blocks after loops
                while i < n1:
                    i += 1
                    for ch in s1:
                        if ch == s2[j]:
                            j += 1
                            if j == len(s2):
                                j = 0
                                count_s2 += 1
                break
            else:
                index_record[j] = (i, count_s2)

        return count_s2 // n2
```

## Python3

```python
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not set(s2).issubset(set(s1)):
            return 0

        len_s2 = len(s2)
        index_s2 = 0          # current position in s2
        count_s2 = 0          # how many times s2 has been fully matched
        recall = dict()       # key: index_s2, value: (i, count_s2)

        i = 0
        while i < n1:
            i += 1
            for ch in s1:
                if ch == s2[index_s2]:
                    index_s2 += 1
                    if index_s2 == len_s2:
                        index_s2 = 0
                        count_s2 += 1

            # after processing one block of s1
            if index_s2 in recall:
                prev_i, prev_count = recall[index_s2]
                # pre-cycle part
                pre_cycle_cnt = prev_count
                # cycle length and count increase
                cycle_len = i - prev_i
                cycle_cnt = count_s2 - prev_count

                # total repetitions using cycles
                remaining_blocks = n1 - prev_i
                full_cycles = remaining_blocks // cycle_len
                total_cnt = pre_cycle_cnt + full_cycles * cycle_cnt

                leftover = remaining_blocks % cycle_len
                # simulate leftover blocks
                for _ in range(leftover):
                    for ch in s1:
                        if ch == s2[index_s2]:
                            index_s2 += 1
                            if index_s2 == len_s2:
                                index_s2 = 0
                                total_cnt += 1

                return total_cnt // n2
            else:
                recall[index_s2] = (i, count_s2)

        # no cycle detected; processed all blocks
        return count_s2 // n2
```

## C

```c
#include <stdlib.h>
#include <string.h>

int getMaxRepetitions(char* s1, int n1, char* s2, int n2) {
    int l1 = (int)strlen(s1);
    int l2 = (int)strlen(s2);

    /* quick impossibility check */
    int present[26] = {0};
    for (int i = 0; i < l1; ++i) present[s1[i] - 'a'] = 1;
    for (int i = 0; i < l2; ++i)
        if (!present[s2[i] - 'a']) return 0;

    int *recall_i   = (int *)malloc(l2 * sizeof(int));
    int *recall_cnt = (int *)malloc(l2 * sizeof(int));
    for (int i = 0; i < l2; ++i) {
        recall_i[i] = -1;
        recall_cnt[i] = 0;
    }

    int s1cnt = 0;   // how many s1 blocks processed
    int s2cnt = 0;   // how many full s2 strings matched
    int idx   = 0;   // current position in s2

    while (1) {
        ++s1cnt;
        for (int i = 0; i < l1; ++i) {
            if (s1[i] == s2[idx]) {
                ++idx;
                if (idx == l2) {
                    ++s2cnt;
                    idx = 0;
                }
            }
        }

        if (s1cnt == n1) {
            free(recall_i);
            free(recall_cnt);
            return s2cnt / n2;
        }

        if (recall_i[idx] != -1) {
            int pre_s1cnt = recall_i[idx];
            int pre_s2cnt = recall_cnt[idx];

            int per_loop_s1cnt = s1cnt - pre_s1cnt;
            int per_loop_s2cnt = s2cnt - pre_s2cnt;

            if (per_loop_s1cnt > 0) {
                int loops = (n1 - s1cnt) / per_loop_s1cnt;
                s1cnt += loops * per_loop_s1cnt;
                s2cnt += loops * per_loop_s2cnt;
            }
        } else {
            recall_i[idx]   = s1cnt;
            recall_cnt[idx] = s2cnt;
        }
    }
}
```

## Csharp

```csharp
public class Solution {
    public int GetMaxRepetitions(string s1, int n1, string s2, int n2) {
        int l1 = s1.Length;
        int l2 = s2.Length;
        // record first occurrence of each position in s2
        int[] recI = new int[l2 + 1];
        int[] recCnt = new int[l2 + 1];
        for (int i = 0; i <= l2; i++) recI[i] = -1;

        int j = 0; // index in s2
        int cnt = 0; // how many times s2 fully matched

        for (int i = 1; i <= n1; i++) {
            for (int p = 0; p < l1; p++) {
                if (s1[p] == s2[j]) {
                    j++;
                    if (j == l2) {
                        j = 0;
                        cnt++;
                    }
                }
            }

            if (recI[j] != -1) {
                int preI = recI[j];
                int preCnt = recCnt[j];

                int cycleLen = i - preI;
                int cycleCnt = cnt - preCnt;

                int remainingBlocks = n1 - preI;
                int cycles = remainingBlocks / cycleLen;
                int totalCnt = preCnt + cycles * cycleCnt;

                int rest = remainingBlocks % cycleLen;
                for (int k = 0; k < rest; k++) {
                    for (int p = 0; p < l1; p++) {
                        if (s1[p] == s2[j]) {
                            j++;
                            if (j == l2) {
                                j = 0;
                                totalCnt++;
                            }
                        }
                    }
                }

                return totalCnt / n2;
            } else {
                recI[j] = i;
                recCnt[j] = cnt;
            }
        }

        return cnt / n2;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {number} n1
 * @param {string} s2
 * @param {number} n2
 * @return {number}
 */
var getMaxRepetitions = function(s1, n1, s2, n2) {
    const len1 = s1.length;
    const len2 = s2.length;

    // quick impossibility check
    const charsInS1 = new Set(s1);
    for (let ch of s2) {
        if (!charsInS1.has(ch)) return 0;
    }

    // recall[index] = [s1Count, s2Count] when this index first appears
    const recall = new Array(len2).fill(null);

    let s1Count = 0;   // how many s1 blocks have been processed
    let s2Count = 0;   // how many full s2 strings have been matched
    let idx = 0;       // current position in s2

    while (true) {
        s1Count++;
        for (let i = 0; i < len1; i++) {
            if (s1[i] === s2[idx]) {
                idx++;
                if (idx === len2) {
                    s2Count++;
                    idx = 0;
                }
            }
        }

        if (s1Count === n1) {
            return Math.floor(s2Count / n2);
        }

        // detect a previously seen state to form a cycle
        if (recall[idx] !== null) {
            const [prevS1, prevS2] = recall[idx];
            const cycleS1 = s1Count - prevS1;
            const cycleS2 = s2Count - prevS2;

            const remainingS1 = n1 - s1Count;
            const cycles = Math.floor(remainingS1 / cycleS1);
            if (cycles > 0) {
                s1Count += cycles * cycleS1;
                s2Count += cycles * cycleS2;
            }
        } else {
            recall[idx] = [s1Count, s2Count];
        }
    }
};
```

## Typescript

```typescript
function getMaxRepetitions(s1: string, n1: number, s2: string, n2: number): number {
    const s1Len = s1.length;
    const s2Len = s2.length;

    // countArr[i] = total completed s2 after processing i blocks of s1
    const countArr: number[] = new Array(n1 + 1).fill(0);
    // seen[pos] = first block index where we had this position in s2
    const seen: number[] = new Array(s2Len).fill(-1);

    let pos = 0; // current position in s2
    seen[0] = 0;

    for (let i = 1; i <= n1; i++) {
        for (let j = 0; j < s1Len; j++) {
            if (s1.charCodeAt(j) === s2.charCodeAt(pos)) {
                pos++;
                if (pos === s2Len) {
                    pos = 0;
                    countArr[i]++; // completed one s2 within this block
                }
            }
        }
        countArr[i] += countArr[i - 1]; // accumulate previous blocks

        if (seen[pos] !== -1) {
            const preBlock = seen[pos];
            const preCount = countArr[preBlock];

            const loopBlocks = i - preBlock;
            const loopCount = countArr[i] - preCount;

            const remainingBlocks = n1 - preBlock;
            const loops = Math.floor(remainingBlocks / loopBlocks);
            const rest = remainingBlocks % loopBlocks;

            let total = preCount + loops * loopCount;
            const endBlock = preBlock + rest;
            total += countArr[endBlock] - countArr[preBlock];

            return Math.floor(total / n2);
        } else {
            seen[pos] = i;
        }
    }

    return Math.floor(countArr[n1] / n2);
}
```

## Php

```php
class Solution {

    /**
     * @param String $s1
     * @param Integer $n1
     * @param String $s2
     * @param Integer $n2
     * @return Integer
     */
    function getMaxRepetitions($s1, $n1, $s2, $n2) {
        $len1 = strlen($s1);
        $len2 = strlen($s2);
        if ($len1 == 0 || $len2 == 0) return 0;

        $index = 0; // current position in s2
        $count = 0; // how many times we have completed s2

        $posMap = []; // key: index in s2, value: [block number, count]

        for ($i = 1; $i <= $n1; $i++) {
            for ($j = 0; $j < $len1; $j++) {
                if ($s1[$j] === $s2[$index]) {
                    $index++;
                    if ($index == $len2) {
                        $index = 0;
                        $count++;
                    }
                }
            }

            // check for a previously seen state
            if (!isset($posMap[$index])) {
                $posMap[$index] = [$i, $count];
            } else {
                list($prevI, $prevCount) = $posMap[$index];

                // blocks before loop starts
                $preLoopBlocks = $prevI;
                $cntPre = $prevCount;

                // blocks inside one loop
                $inLoopBlocks = $i - $prevI;
                $cntLoop = $count - $prevCount;

                // total remaining blocks after pre-loop part
                $remainingBlocks = $n1 - $preLoopBlocks;
                $loops = intdiv($remainingBlocks, $inLoopBlocks);
                $totalCnt = $cntPre + $loops * $cntLoop;
                $restBlocks = $remainingBlocks % $inLoopBlocks;

                // simulate the remaining blocks
                $idxRest = $index; // after each full loop we are at same index
                $cntRest = 0;
                for ($r = 0; $r < $restBlocks; $r++) {
                    for ($j = 0; $j < $len1; $j++) {
                        if ($s1[$j] === $s2[$idxRest]) {
                            $idxRest++;
                            if ($idxRest == $len2) {
                                $idxRest = 0;
                                $cntRest++;
                            }
                        }
                    }
                }

                $totalCnt += $cntRest;
                return intdiv($totalCnt, $n2);
            }
        }

        // no loop detected
        return intdiv($count, $n2);
    }
}
```

## Swift

```swift
class Solution {
    func getMaxRepetitions(_ s1: String, _ n1: Int, _ s2: String, _ n2: Int) -> Int {
        let a = Array(s1)
        let b = Array(s2)
        let l1 = a.count
        let l2 = b.count
        
        var recallIter = Array(repeating: -1, count: l2)
        var recallCount = Array(repeating: 0, count: l2)
        
        var indexS2 = 0          // current position in s2
        var countS2 = 0          // how many times s2 is fully matched
        
        var i = 0                // number of processed s1 blocks
        while i < n1 {
            for ch in a {
                if ch == b[indexS2] {
                    indexS2 += 1
                    if indexS2 == l2 {
                        indexS2 = 0
                        countS2 += 1
                    }
                }
            }
            i += 1
            
            // Check for previously seen state
            if recallIter[indexS2] != -1 {
                let preIter = recallIter[indexS2]
                let preCount = recallCount[indexS2]
                
                let loopSize = i - preIter               // number of s1 blocks in one loop
                let loopCount = countS2 - preCount       // how many s2 are matched per loop
                
                var total = preCount
                let remainingBlocks = n1 - preIter
                let loops = remainingBlocks / loopSize
                total += loops * loopCount
                
                let leftover = remainingBlocks % loopSize
                var curIdx = indexS2
                var extra = 0
                for _ in 0..<leftover {
                    for ch in a {
                        if ch == b[curIdx] {
                            curIdx += 1
                            if curIdx == l2 {
                                curIdx = 0
                                extra += 1
                            }
                        }
                    }
                }
                total += extra
                
                return total / n2
            } else {
                recallIter[indexS2] = i
                recallCount[indexS2] = countS2
            }
        }
        
        // No loop detected; processed all blocks directly
        return countS2 / n2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getMaxRepetitions(s1: String, n1: Int, s2: String, n2: Int): Int {
        val l1 = s1.length
        val l2 = s2.length
        var idx2 = 0               // current position in s2
        var cnt = 0                // how many times s2 is fully matched
        val recallI = IntArray(l2) { -1 }   // first occurrence of idx2 after some blocks of s1
        val recallCnt = IntArray(l2)        // corresponding cnt at that occurrence

        var i = 0
        while (i < n1) {
            i++
            for (ch in s1) {
                if (ch == s2[idx2]) {
                    idx2++
                    if (idx2 == l2) {
                        idx2 = 0
                        cnt++
                    }
                }
            }

            if (recallI[idx2] != -1) {
                // loop detected
                val preI = recallI[idx2]
                val preCnt = recallCnt[idx2]

                val loopLen = i - preI          // number of s1 blocks in one loop
                val loopCnt = cnt - preCnt      // how many s2 completed in one loop

                var total = preCnt + ((n1 - preI) / loopLen) * loopCnt
                var remain = (n1 - preI) % loopLen

                var curIdx = idx2
                var extra = 0
                while (remain > 0) {
                    for (ch in s1) {
                        if (ch == s2[curIdx]) {
                            curIdx++
                            if (curIdx == l2) {
                                curIdx = 0
                                extra++
                            }
                        }
                    }
                    remain--
                }
                total += extra
                return total / n2
            } else {
                recallI[idx2] = i
                recallCnt[idx2] = cnt
            }
        }
        // no loop found within n1 repetitions
        return cnt / n2
    }
}
```

## Dart

```dart
class Solution {
  int getMaxRepetitions(String s1, int n1, String s2, int n2) {
    if (n1 == 0) return 0;
    int s1Len = s1.length;
    int s2Len = s2.length;

    // recallIdx[pos] stores the iteration count of processed s1 blocks when we first saw this pos
    List<int> recallIdx = List.filled(s2Len, -1);
    List<int> recallCnt = List.filled(s2Len, 0);

    int s2Pos = 0; // current position in s2
    int cnt = 0;   // how many times we have completed s2
    int i = 0;     // number of processed s1 blocks

    while (i < n1) {
      i++;
      for (int j = 0; j < s1Len; j++) {
        if (s1.codeUnitAt(j) == s2.codeUnitAt(s2Pos)) {
          s2Pos++;
          if (s2Pos == s2Len) {
            s2Pos = 0;
            cnt++;
          }
        }
      }

      if (recallIdx[s2Pos] != -1) {
        // a loop is detected
        int preI = recallIdx[s2Pos];
        int preCnt = recallCnt[s2Pos];

        int loopBlock = i - preI;       // number of s1 blocks in one loop
        int loopCnt = cnt - preCnt;     // how many s2 completions in one loop

        int remain = n1 - i;
        if (loopBlock > 0) {
          int loops = remain ~/ loopBlock;
          cnt += loops * loopCnt;
          i += loops * loopBlock;
        }
      } else {
        recallIdx[s2Pos] = i;
        recallCnt[s2Pos] = cnt;
      }
    }

    return cnt ~/ n2;
  }
}
```

## Golang

```go
func getMaxRepetitions(s1 string, n1 int, s2 string, n2 int) int {
    l1, l2 := len(s1), len(s2)
    // record the first occurrence of each position in s2 after processing some blocks of s1
    indexRec := make([]int, l2)
    countRec := make([]int, l2)
    for i := 0; i < l2; i++ {
        indexRec[i] = -1
    }

    pos, cnt := 0, 0 // current position in s2 and total completed s2 strings

    for i := 0; i < n1; i++ {
        // process one block of s1
        for j := 0; j < l1; j++ {
            if s1[j] == s2[pos] {
                pos++
                if pos == l2 {
                    cnt++
                    pos = 0
                }
            }
        }

        if indexRec[pos] != -1 {
            // a previous state with the same position in s2 was seen -> cycle detected
            preI := indexRec[pos]
            preCnt := countRec[pos]

            loopLen := i - preI          // number of s1 blocks per cycle
            loopCnt := cnt - preCnt      // number of completed s2 strings per cycle

            remaining := n1 - i - 1      // blocks left after current one
            loops := remaining / loopLen // how many full cycles we can skip

            cnt += loops * loopCnt
            i += loops * loopLen
        } else {
            indexRec[pos] = i
            countRec[pos] = cnt
        }
    }

    return cnt / n2
}
```

## Ruby

```ruby
def get_max_repetitions(s1, n1, s2, n2)
  s1_chars = s1.chars
  s2_chars = s2.chars
  len_s2 = s2.length

  index_j = 0          # position in s2
  count_s2 = 0         # how many times s2 is fully matched
  recall = {}          # map: index_j => [i (blocks processed), count_s2]

  i = 0
  while i < n1
    i += 1
    s1_chars.each do |c|
      if c == s2_chars[index_j]
        index_j += 1
        if index_j == len_s2
          index_j = 0
          count_s2 += 1
        end
      end
    end

    if recall.key?(index_j)
      prev_i, prev_count = recall[index_j]

      # loop length in terms of s1 blocks and s2 completions
      loop_blocks = i - prev_i
      loop_count  = count_s2 - prev_count

      remaining = n1 - i
      loops = remaining / loop_blocks
      count_s2 += loops * loop_count
      i += loops * loop_blocks

      # process the leftover blocks after full loops
      while i < n1
        s1_chars.each do |c|
          if c == s2_chars[index_j]
            index_j += 1
            if index_j == len_s2
              index_j = 0
              count_s2 += 1
            end
          end
        end
        i += 1
      end

      return count_s2 / n2
    else
      recall[index_j] = [i, count_s2]
    end
  end

  count_s2 / n2
end
```

## Scala

```scala
object Solution {
    def getMaxRepetitions(s1: String, n1: Int, s2: String, n2: Int): Int = {
        val s1Arr = s1.toCharArray
        val s2Arr = s2.toCharArray
        val len2 = s2Arr.length

        // cnt[i]: number of completed s2 after i repetitions of s1
        val cnt = new Array[Int](n1 + 1)
        // pos[i]: current position in s2 after i repetitions of s1
        val pos = new Array[Int](n1 + 1)

        // firstIdx[p] stores the earliest i where pos[i] == p
        val firstIdx = new Array[Int](len2 + 1)
        java.util.Arrays.fill(firstIdx, -1)
        firstIdx(0) = 0

        var i = 1
        var preLoop = 0
        var inLoop = 0
        var found = false

        while (i <= n1 && !found) {
            var curPos = pos(i - 1)
            var curCnt = cnt(i - 1)

            var idx = 0
            while (idx < s1Arr.length) {
                if (s1Arr(idx) == s2Arr(curPos)) {
                    curPos += 1
                    if (curPos == len2) {
                        curCnt += 1
                        curPos = 0
                    }
                }
                idx += 1
            }

            pos(i) = curPos
            cnt(i) = curCnt

            if (firstIdx(curPos) != -1) {
                preLoop = firstIdx(curPos)
                inLoop = i - preLoop
                found = true
            } else {
                firstIdx(curPos) = i
            }

            i += 1
        }

        if (!found) {
            return cnt(n1) / n2
        }

        val countBefore = cnt(preLoop)
        val remaining = n1 - preLoop
        val loops = remaining / inLoop

        var totalCnt = countBefore + loops * (cnt(preLoop + inLoop) - cnt(preLoop))
        val rest = remaining % inLoop
        totalCnt += cnt(preLoop + rest) - cnt(preLoop)

        totalCnt / n2
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_max_repetitions(s1: String, n1: i32, s2: String, n2: i32) -> i32 {
        let s1_bytes = s1.as_bytes();
        let s2_bytes = s2.as_bytes();
        let s2_len = s2_bytes.len();

        if s2_len == 0 {
            return 0;
        }

        // recall_i[idx] = the block count (i) when we first saw index_s2 == idx
        // recall_cnt[idx] = total completed s2 sequences at that moment
        let mut recall_i = vec![-1i32; s2_len];
        let mut recall_cnt = vec![0i32; s2_len];

        let mut index_s2: usize = 0;
        let mut cnt_s2: i32 = 0;

        let mut i: i32 = 0;
        while i < n1 {
            i += 1;
            for &c in s1_bytes.iter() {
                if c == s2_bytes[index_s2] {
                    index_s2 += 1;
                    if index_s2 == s2_len {
                        cnt_s2 += 1;
                        index_s2 = 0;
                    }
                }
            }

            if recall_i[index_s2] != -1 {
                let pre_i = recall_i[index_s2];
                let pre_cnt = recall_cnt[index_s2];

                let loop_len = i - pre_i;          // number of s1 blocks in a loop
                let loop_cnt = cnt_s2 - pre_cnt;   // how many s2 completions per loop

                if loop_len > 0 {
                    let remaining = n1 - i;
                    let loops = remaining / loop_len;
                    cnt_s2 += loops * loop_cnt;
                    i += loops * loop_len;
                }
            } else {
                recall_i[index_s2] = i;
                recall_cnt[index_s2] = cnt_s2;
            }
        }

        cnt_s2 / n2
    }
}
```

## Racket

```racket
(define/contract (get-max-repetitions s1 n1 s2 n2)
  (-> string? exact-integer? string? exact-integer? exact-integer?)
  (let* ((len1 (string-length s1))
         (len2 (string-length s2))
         (pos 0)                     ; current index in s2
         (cnt 0)                     ; total completed s2 matches
         (visited (make-vector len2 #f))) ; store (block-index . cnt) for each pos
    ;; initial state before any block processed
    (vector-set! visited pos (cons 0 0))
    (let loop ((i 0))               ; i = number of blocks already processed
      (if (= i n1)
          (quotient cnt n2)
          (begin
            ;; process one whole s1 block
            (for ([j (in-range len1)])
              (when (char=? (string-ref s1 j) (string-ref s2 pos))
                (set! pos (+ pos 1))
                (when (= pos len2)
                  (set! pos 0)
                  (set! cnt (+ cnt 1)))))
            ;; after processing block i+1, check for cycle
            (let ((prev (vector-ref visited pos)))
              (if prev
                  (let* ((i-prev (car prev))          ; blocks processed at previous occurrence
                         (cnt-prev (cdr prev))
                         (cycle-len (- (+ i 1) i-prev))   ; length of one cycle in blocks
                         (cycle-cnt (- cnt cnt-prev))    ; s2 matches gained per cycle
                         (remaining (- n1 i-prev))       ; blocks left after the prefix before cycle
                         (cycles (quotient remaining cycle-len))
                         (total (+ cnt-prev (* cycles cycle-cnt))))
                    ;; simulate the leftover blocks that don't fit a full cycle
                    (let ((rest (remainder remaining cycle-len)))
                      (let loop-rest ((k 0) (p pos) (c total))
                        (if (= k rest)
                            (quotient c n2)
                            (begin
                              (for ([j (in-range len1)])
                                (when (char=? (string-ref s1 j) (string-ref s2 p))
                                  (set! p (+ p 1))
                                  (when (= p len2)
                                    (set! p 0)
                                    (set! c (+ c 1)))))
                              (loop-rest (+ k 1) p c))))))
                  ;; first time seeing this pos, record and continue
                  (begin
                    (vector-set! visited pos (cons (+ i 1) cnt))
                    (loop (+ i 1))))))))))
```

## Erlang

```erlang
-spec get_max_repetitions(S1 :: unicode:unicode_binary(), N1 :: integer(), S2 :: unicode:unicode_binary(), N2 :: integer()) -> integer().
get_max_repetitions(S1, N1, S2, N2) ->
    S1List = binary_to_list(S1),
    S2List = binary_to_list(S2),
    LenS2 = length(S2List),
    S2Tuple = list_to_tuple(S2List),
    TotalCount = process(N1, S1List, S2Tuple, LenS2, 0, 0, #{}, 0),
    TotalCount div N2.

process(_N1, _S1List, _S2Tuple, _LenS2, _Index, Count, _Map, _Total) ->
    Count;
process(N1, S1List, S2Tuple, LenS2, Index, Count, Map, Total) when Total < N1 ->
    {NewIndex, NewCount} = process_one_block(S1List, S2Tuple, LenS2, Index, Count),
    NewTotal = Total + 1,
    case maps:find(NewIndex, Map) of
        error ->
            NewMap = maps:put(NewIndex, {NewTotal, NewCount}, Map),
            process(N1, S1List, S2Tuple, LenS2, NewIndex, NewCount, NewMap, NewTotal);
        {ok, {PrevTotal, PrevCount}} ->
            LoopLen = NewTotal - PrevTotal,
            LoopCount = NewCount - PrevCount,
            Remaining = N1 - NewTotal,
            Loops = if LoopLen == 0 -> 0; true -> Remaining div LoopLen end,
            CountAfterLoops = NewCount + Loops * LoopCount,
            TotalAfterLoops = NewTotal + Loops * LoopLen,
            process(N1, S1List, S2Tuple, LenS2, NewIndex, CountAfterLoops, Map, TotalAfterLoops)
    end.

process_one_block([], _S2Tuple, _LenS2, Index, Count) ->
    {Index, Count};
process_one_block([C|Rest], S2Tuple, LenS2, Index, Count) ->
    Char = element(Index + 1, S2Tuple),
    if C == Char ->
            NewIdx = Index + 1,
            if NewIdx == LenS2 ->
                    process_one_block(Rest, S2Tuple, LenS2, 0, Count + 1);
               true ->
                    process_one_block(Rest, S2Tuple, LenS2, NewIdx, Count)
            end;
       true ->
            process_one_block(Rest, S2Tuple, LenS2, Index, Count)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_max_repetitions(String.t, integer, String.t, integer) :: integer
  def get_max_repetitions(s1, n1, s2, n2) do
    s1_chars = String.graphemes(s1)
    s2_chars = String.graphemes(s2)
    s2_len = length(s2_chars)

    total_cnt = loop(0, 0, 0, %{}, s1_chars, s2_chars, s2_len, n1)
    div(total_cnt, n2)
  end

  defp loop(i, cnt, j, visited, s1_chars, s2_chars, s2_len, n1) do
    if i == n1 do
      cnt
    else
      {new_j, new_cnt} = process_block(s1_chars, s2_chars, j, cnt, s2_len)
      i1 = i + 1

      case Map.get(visited, new_j) do
        nil ->
          visited1 = Map.put(visited, new_j, {i1, new_cnt})
          loop(i1, new_cnt, new_j, visited1, s1_chars, s2_chars, s2_len, n1)

        {prev_i, prev_cnt} ->
          in_loop_i = i1 - prev_i
          in_loop_cnt = new_cnt - prev_cnt

          remaining = n1 - i1
          loops = div(remaining, in_loop_i)
          cnt2 = new_cnt + loops * in_loop_cnt
          i2 = i1 + loops * in_loop_i

          loop(i2, cnt2, new_j, %{}, s1_chars, s2_chars, s2_len, n1)
      end
    end
  end

  defp process_block(s1_chars, s2_chars, j, cnt, s2_len) do
    Enum.reduce(s1_chars, {j, cnt}, fn c, {jj, cc} ->
      if c == Enum.at(s2_chars, jj) do
        jj = jj + 1

        if jj == s2_len do
          {0, cc + 1}
        else
          {jj, cc}
        end
      else
        {jj, cc}
      end
    end)
  end
end
```
