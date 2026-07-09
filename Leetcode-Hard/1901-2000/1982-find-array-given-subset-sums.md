# 1982. Find Array Given Subset Sums

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    optional<vector<int>> solve(const vector<int>& sums) {
        if (sums.size() == 1) return vector<int>();
        int diff = sums[1] - sums[0];
        for (int sign = 1; sign >= -1; sign -= 2) {
            int x = diff * sign;
            unordered_map<long long,int> cnt;
            cnt.reserve(sums.size()*2);
            for (int v : sums) ++cnt[v];
            vector<int> without;
            bool ok = true;
            for (int v : sums) {
                if (cnt[v] == 0) continue;
                without.push_back(v);
                --cnt[v];
                long long t = (long long)v + x;
                auto it = cnt.find(t);
                if (it == cnt.end() || it->second == 0) { ok = false; break; }
                --(it->second);
            }
            if (!ok) continue;
            auto subOpt = solve(without);
            if (subOpt.has_value()) {
                vector<int> ans = *subOpt;
                ans.push_back(x);
                return ans;
            }
        }
        return {};
    }

    vector<int> recoverArray(int n, vector<int>& sums) {
        sort(sums.begin(), sums.end());
        auto resOpt = solve(sums);
        vector<int> res = resOpt.value_or(vector<int>());
        // The order does not matter; any permutation is acceptable.
        return res;
    }
};
```

## Java

```java
class Solution {
    public int[] recoverArray(int n, int[] sums) {
        java.util.List<Integer> list = new java.util.ArrayList<>(sums.length);
        for (int v : sums) list.add(v);
        java.util.Collections.sort(list);
        java.util.List<Integer> ansList = solve(n, list);
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = ansList.get(i);
        return ans;
    }

    private java.util.List<Integer> solve(int n, java.util.List<Integer> sums) {
        if (n == 0) return new java.util.ArrayList<>();
        int diff = sums.get(1) - sums.get(0); // candidate absolute value
        java.util.Map<Integer, Integer> cnt = new java.util.HashMap<>();
        for (int v : sums) cnt.put(v, cnt.getOrDefault(v, 0) + 1);

        java.util.List<Integer> without = new java.util.ArrayList<>(sums.size() / 2);
        boolean hasZero = false;
        for (int v : sums) {
            int c = cnt.getOrDefault(v, 0);
            if (c == 0) continue;
            without.add(v);
            if (v == 0) hasZero = true;
            cnt.put(v, c - 1);
            int target = v + diff;
            cnt.put(target, cnt.get(target) - 1);
        }

        if (hasZero) {
            java.util.List<Integer> rest = solve(n - 1, without);
            rest.add(diff);
            return rest;
        } else {
            // element is -diff, rebuild groups using -diff
            cnt.clear();
            for (int v : sums) cnt.put(v, cnt.getOrDefault(v, 0) + 1);
            without.clear();
            for (int v : sums) {
                int c = cnt.getOrDefault(v, 0);
                if (c == 0) continue;
                without.add(v);
                if (v == 0) hasZero = true; // not needed further
                cnt.put(v, c - 1);
                int target = v - diff;
                cnt.put(target, cnt.get(target) - 1);
            }
            java.util.List<Integer> rest = solve(n - 1, without);
            rest.add(-diff);
            return rest;
        }
    }
}
```

## Python

```python
class Solution(object):
    def recoverArray(self, n, sums):
        """
        :type n: int
        :type sums: List[int]
        :rtype: List[int]
        """
        from collections import Counter

        def helper(cur_sums):
            if len(cur_sums) == 1:
                return []
            cur_sums.sort()
            diff = cur_sums[1] - cur_sums[0]

            for sign in (1, -1):
                x = diff * sign
                cnt = Counter(cur_sums)
                without = []
                valid = True
                for s in cur_sums:
                    if cnt[s] == 0:
                        continue
                    cnt[s] -= 1
                    counterpart = s + x
                    if cnt[counterpart] == 0:
                        valid = False
                        break
                    cnt[counterpart] -= 1
                    without.append(s)
                if valid and 0 in without:
                    rest = helper(without)
                    return [x] + rest
            # Should never reach here due to problem guarantee
            return []

        result = helper(sums)
        return result
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        def helper(arr: List[int]) -> List[int]:
            if len(arr) == 1:
                return []
            arr.sort()
            diff = arr[1] - arr[0]

            # try assuming element is +diff
            cnt = Counter(arr)
            without = []
            for x in arr:
                if cnt[x] == 0:
                    continue
                cnt[x] -= 1
                y = x + diff
                cnt[y] -= 1
                without.append(x)

            if 0 in without:  # element is positive diff
                rest = helper(without)
                return rest + [diff]

            # otherwise element must be -diff
            cnt = Counter(arr)
            without = []
            for x in arr:
                if cnt[x] == 0:
                    continue
                cnt[x] -= 1
                y = x - diff   # since element is -diff
                cnt[y] -= 1
                without.append(x)

            rest = helper(without)
            return rest + [-diff]

        return helper(sums)
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int key;
    int val;
    char used;
} Entry;

static unsigned int hash_int(int x) {
    return (unsigned int)(x * 2654435761u);
}

static void hashmap_add(Entry *tbl, int cap, int key, int delta) {
    unsigned int idx = hash_int(key) % cap;
    while (tbl[idx].used && tbl[idx].key != key) {
        idx = (idx + 1) % cap;
    }
    if (!tbl[idx].used) {
        tbl[idx].key = key;
        tbl[idx].val = 0;
        tbl[idx].used = 1;
    }
    tbl[idx].val += delta;
}

static int hashmap_dec_if_positive(Entry *tbl, int cap, int key) {
    unsigned int idx = hash_int(key) % cap;
    while (tbl[idx].used) {
        if (tbl[idx].key == key) {
            if (tbl[idx].val > 0) {
                tbl[idx].val--;
                return 1;
            }
            return 0;
        }
        idx = (idx + 1) % cap;
    }
    return 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* recoverArray(int n, int* sums, int sumsSize, int* returnSize) {
    qsort(sums, sumsSize, sizeof(int), (int (*)(const void *, const void *))strcmp);
    int m = sumsSize;
    int *cur = malloc(m * sizeof(int));
    memcpy(cur, sums, m * sizeof(int));

    int *ans = malloc(n * sizeof(int));
    int ansIdx = 0;

    while (m > 1) {
        int cand = cur[1] - cur[0];

        // try positive candidate
        int cap = 4 * m + 10;
        Entry *tbl = calloc(cap, sizeof(Entry));
        int *without = malloc((m / 2 + 1) * sizeof(int));
        int wsize = 0;

        for (int i = 0; i < m; ++i) {
            if (hashmap_dec_if_positive(tbl, cap, cur[i]))
                continue;
            without[wsize++] = cur[i];
            hashmap_add(tbl, cap, cur[i] + cand, 1);
        }

        int hasZero = 0;
        for (int i = 0; i < wsize; ++i) {
            if (without[i] == 0) { hasZero = 1; break; }
        }
        free(tbl);

        if (hasZero) {
            ans[ansIdx++] = cand;
            free(cur);
            cur = malloc(wsize * sizeof(int));
            memcpy(cur, without, wsize * sizeof(int));
            m = wsize;
            free(without);
            continue;
        }

        // negative candidate
        free(without);
        int negcand = -cand;
        cap = 4 * m + 10;
        tbl = calloc(cap, sizeof(Entry));
        int *without2 = malloc((m / 2 + 1) * sizeof(int));
        wsize = 0;

        for (int i = 0; i < m; ++i) {
            if (hashmap_dec_if_positive(tbl, cap, cur[i]))
                continue;
            without2[wsize++] = cur[i];
            hashmap_add(tbl, cap, cur[i] + negcand, 1);
        }
        free(tbl);

        ans[ansIdx++] = negcand;
        free(cur);
        cur = malloc(wsize * sizeof(int));
        memcpy(cur, without2, wsize * sizeof(int));
        m = wsize;
        free(without2);
    }

    free(cur);
    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] RecoverArray(int n, int[] sums) {
        var list = new List<int>(sums);
        var result = Recover(list);
        return result.ToArray();
    }

    private List<int> Recover(List<int> sums) {
        if (sums.Count == 1) {
            // only the empty subset sum remains
            return new List<int>();
        }

        sums.Sort();
        int diff = sums[1] - sums[0];

        var count = new Dictionary<int, int>();
        foreach (int v in sums) {
            if (count.ContainsKey(v)) count[v]++;
            else count[v] = 1;
        }

        var without = new List<int>();
        var with = new List<int>();

        foreach (int x in sums) {
            if (!count.TryGetValue(x, out int c) || c == 0) continue;

            // remove x
            count[x]--;
            // remove its pair x + diff
            int y = x + diff;
            count[y]--;

            without.Add(x);
            with.Add(y);
        }

        List<int> nextSums;
        int element;
        if (without.Contains(0)) {
            element = diff;
            nextSums = without;
        } else {
            element = -diff;
            nextSums = with;
        }

        var res = Recover(nextSums);
        res.Add(element);
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} sums
 * @return {number[]}
 */
var recoverArray = function(n, sums) {
    const helper = (arr) => {
        if (arr.length === 1) return [];
        arr.sort((a, b) => a - b);
        const max = arr[arr.length - 1];
        const secondMax = arr[arr.length - 2];
        const diff = max - secondMax;

        const cnt = new Map();
        const groupA = [];

        for (const s of arr) {
            const c = cnt.get(s) || 0;
            if (c > 0) {
                cnt.set(s, c - 1);
            } else {
                groupA.push(s);
                cnt.set(s + diff, (cnt.get(s + diff) || 0) + 1);
            }
        }

        if (groupA.includes(0)) {
            const rest = helper(groupA);
            rest.push(diff);
            return rest;
        } else {
            const groupB = groupA.map(v => v + diff);
            const rest = helper(groupB);
            rest.push(-diff);
            return rest;
        }
    };
    return helper(sums);
};
```

## Typescript

```typescript
function recoverArray(n: number, sums: number[]): number[] {
    sums.sort((a, b) => a - b);
    const res = dfs(sums, n);
    return res ?? [];
}

function dfs(sums: number[], k: number): number[] | null {
    if (k === 0) return [];
    // smallest sum is always 0
    const x = sums[1] - sums[0];

    // try assuming element is +x
    let part = partition(sums, x);
    if (part && part.withoutX.includes(0)) {
        const sub = dfs(part.withoutX, k - 1);
        if (sub) return [...sub, x];
    }

    // try assuming element is -x
    part = partition(sums, -x);
    if (part && part.withoutX.includes(0)) {
        const sub = dfs(part.withoutX, k - 1);
        if (sub) return [...sub, -x];
    }
    return null;
}

function partition(arr: number[], x: number): { withoutX: number[]; withX: number[] } | null {
    const freq = new Map<number, number>();
    for (const v of arr) {
        freq.set(v, (freq.get(v) ?? 0) + 1);
    }

    const without: number[] = [];
    const withArr: number[] = [];

    for (const v of arr) {
        const cnt = freq.get(v) ?? 0;
        if (cnt === 0) continue;

        // take v as a sum that does NOT include x
        without.push(v);
        freq.set(v, cnt - 1);

        const target = v + x;
        const cntT = freq.get(target) ?? 0;
        if (cntT === 0) return null; // invalid partition

        withArr.push(target);
        freq.set(target, cntT - 1);
    }

    return { withoutX: without, withX: withArr };
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $sums
     * @return Integer[]
     */
    function recoverArray($n, $sums) {
        sort($sums);
        return $this->solve($sums, $n);
    }

    private function solve(array $sums, int $n): ?array {
        if ($n == 0) {
            return [];
        }
        if ($n == 1) {
            foreach ($sums as $v) {
                if ($v != 0) {
                    return [$v];
                }
            }
            return [0];
        }

        $max = $sums[count($sums) - 1];
        $secondMax = $sums[count($sums) - 2];
        $x = $max - $secondMax;

        $res = $this->tryCandidate($sums, $n, $x);
        if ($res !== null) {
            return $res;
        }
        // try the opposite sign
        return $this->tryCandidate($sums, $n, -$x);
    }

    private function tryCandidate(array $sums, int $n, int $x): ?array {
        $cnt = [];
        foreach ($sums as $v) {
            $key = (string)$v;
            if (!isset($cnt[$key])) {
                $cnt[$key] = 0;
            }
            $cnt[$key]++;
        }

        $group0 = [];
        foreach ($sums as $v) {
            $key = (string)$v;
            if ($cnt[$key] > 0) {
                $group0[] = $v;
                $cnt[$key]--;
                $with = $v + $x;
                $k2 = (string)$with;
                if (!isset($cnt[$k2]) || $cnt[$k2] == 0) {
                    return null;
                }
                $cnt[$k2]--;
            }
        }

        // ensure the empty subset sum (0) is in group0
        $hasZero = false;
        foreach ($group0 as $v) {
            if ($v === 0) {
                $hasZero = true;
                break;
            }
        }
        if (!$hasZero) {
            return null;
        }

        $rest = $this->solve($group0, $n - 1);
        if ($rest === null) {
            return null;
        }
        $rest[] = $x;
        return $rest;
    }
}
```

## Swift

```swift
class Solution {
    func recoverArray(_ n: Int, _ sums: [Int]) -> [Int] {
        func partition(_ arr: [Int], _ x: Int) -> [Int]? {
            var cnt = [Int:Int]()
            for v in arr {
                cnt[v, default: 0] += 1
            }
            var without = [Int]()
            for v in arr {
                if let c = cnt[v], c > 0 {
                    cnt[v]! = c - 1
                    let w = v + x
                    guard let cw = cnt[w], cw > 0 else { return nil }
                    cnt[w]! = cw - 1
                    without.append(v)
                }
            }
            return without
        }

        func dfs(_ arr: [Int]) -> [Int] {
            if arr.count == 1 { return [] }
            let sortedArr = arr.sorted()
            let x = sortedArr[1] - sortedArr[0]
            if let without = partition(sortedArr, x), without.contains(0) {
                var res = dfs(without)
                res.append(x)
                return res
            } else {
                let negX = -x
                let withoutNeg = partition(sortedArr, negX)!
                var res = dfs(withoutNeg)
                res.append(negX)
                return res
            }
        }

        return dfs(sums)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun recoverArray(n: Int, sums: IntArray): IntArray {
        val result = solve(sums.toList(), n)
        return result.toIntArray()
    }

    private fun solve(currentSums: List<Int>, k: Int): MutableList<Int> {
        if (k == 0) return mutableListOf()
        val sorted = currentSums.sorted()
        val diff = sorted[1] - sorted[0]

        fun tryCandidate(x: Int): MutableList<Int>? {
            val cnt = HashMap<Int, Int>()
            for (v in sorted) {
                cnt[v] = (cnt[v] ?: 0) + 1
            }
            val without = mutableListOf<Int>()
            for (v in sorted) {
                val c = cnt[v] ?: 0
                if (c == 0) continue
                // v belongs to the group without x
                without.add(v)
                cnt[v] = c - 1
                val nx = v + x
                val cx = cnt[nx] ?: 0
                if (cx == 0) return null   // cannot pair, invalid candidate
                cnt[nx] = cx - 1
            }
            // recurse on the half-size list
            val rest = solve(without, k - 1)
            rest.add(x)
            return rest
        }

        var ans = tryCandidate(diff)
        if (ans != null) return ans
        ans = tryCandidate(-diff)
        return ans!!   // guaranteed to exist by problem statement
    }
}
```

## Dart

```dart
class Solution {
  List<int> recoverArray(int n, List<int> sums) {
    List<int> sorted = List.from(sums)..sort();
    List<int>? ans = _solve(sorted);
    return ans ?? [];
  }

  List<int>? _solve(List<int> sums) {
    if (sums.length == 1) {
      // only [0]
      return <int>[];
    }
    int total = sums.last;
    int second = sums[sums.length - 2];
    int diff = total - second;

    // try diff as the element
    List<int>? without = _tryCandidate(sums, diff);
    if (without != null) {
      List<int>? rec = _solve(without);
      if (rec != null) {
        rec.add(diff);
        return rec;
      }
    }

    // try -diff as the element
    without = _tryCandidate(sums, -diff);
    if (without != null) {
      List<int>? rec = _solve(without);
      if (rec != null) {
        rec.add(-diff);
        return rec;
      }
    }
    return null; // should not happen per problem guarantee
  }

  List<int>? _tryCandidate(List<int> sums, int x) {
    Map<int, int> cnt = {};
    for (int v in sums) {
      cnt[v] = (cnt[v] ?? 0) + 1;
    }
    List<int> without = [];
    for (int v in sums) {
      int curCnt = cnt[v] ?? 0;
      if (curCnt == 0) continue;
      // use v as a sum that does NOT contain x
      cnt[v] = curCnt - 1;
      without.add(v);
      int withVal = v + x;
      int withCnt = cnt[withVal] ?? 0;
      if (withCnt == 0) {
        return null; // pairing fails
      }
      cnt[withVal] = withCnt - 1;
    }
    return without;
  }
}
```

## Golang

```go
func recoverArray(n int, sums []int) []int {
    sort.Ints(sums)
    ans, _ := helper(sums, n)
    return ans
}

func helper(sums []int, k int) ([]int, bool) {
    if k == 0 {
        return []int{}, true
    }
    // candidate absolute value of an element
    cand := sums[1] - sums[0]

    freq := make(map[int]int, len(sums))
    for _, v := range sums {
        freq[v]++
    }

    without := make([]int, 0, len(sums)/2)
    with := make([]int, 0, len(sums)/2)

    valid := true
    for _, v := range sums {
        if freq[v] == 0 {
            continue
        }
        partner := v + cand
        if freq[partner] == 0 {
            valid = false
            break
        }
        without = append(without, v)
        with = append(with, partner)
        freq[v]--
        freq[partner]--
    }

    if !valid {
        return nil, false
    }

    // check where the empty subset (sum 0) resides
    hasZero := false
    for _, v := range without {
        if v == 0 {
            hasZero = true
            break
        }
    }

    if hasZero {
        // element is +cand
        res, ok := helper(without, k-1)
        if ok {
            return append(res, cand), true
        }
    } else {
        // element is -cand, empty subset is in 'with'
        res, ok := helper(with, k-1)
        if ok {
            return append(res, -cand), true
        }
    }

    return nil, false
}
```

## Ruby

```ruby
def try_partition(sums, x)
  cnt = Hash.new(0)
  sums.each { |v| cnt[v] += 1 }
  without = []
  sums.each do |s|
    next if cnt[s] == 0
    cnt[s] -= 1
    t = s + x
    return nil unless cnt[t] && cnt[t] > 0
    cnt[t] -= 1
    without << s
  end
  [without]
end

def recover(sums, k)
  return [] if k == 0
  sums.sort!
  diff = sums[1] - sums[0]

  part = try_partition(sums, diff)
  if part
    without = part[0]
    res = recover(without, k - 1)
    return res + [diff] if res
  end

  part = try_partition(sums, -diff)
  if part
    without = part[0]
    res = recover(without, k - 1)
    return res + [-diff] if res
  end

  nil
end

def recover_array(n, sums)
  recover(sums, n)
end
```

## Scala

```scala
object Solution {
    def recoverArray(n: Int, sums: Array[Int]): Array[Int] = {
        import scala.collection.mutable.{ArrayBuffer, Map => MutableMap}
        var curSums = sums.sorted
        val ans = ArrayBuffer[Int]()

        // helper to split sums with assumed element x
        def trySplit(arr: Array[Int], x: Int): Option[Array[Int]] = {
            val cnt = MutableMap[Int, Int]()
            for (v <- arr) cnt(v) = cnt.getOrElse(v, 0) + 1
            val without = ArrayBuffer[Int]()

            for (v <- arr) {
                if (cnt.getOrElse(v, 0) > 0) {
                    // take v into without set
                    cnt(v) = cnt(v) - 1
                    without += v
                    val t = v + x
                    val ct = cnt.getOrElse(t, 0)
                    if (ct == 0) return None
                    cnt(t) = ct - 1
                }
            }
            Some(without.toArray)
        }

        for (_ <- 0 until n) {
            val diff = curSums(1) - curSums(0) // candidate absolute value
            trySplit(curSums, diff) match {
                case Some(w) if w.contains(0) =>
                    ans += diff
                    curSums = w.sorted
                case _ =>
                    // must be the negative version
                    val wNeg = trySplit(curSums, -diff).get
                    ans += -diff
                    curSums = wNeg.sorted
            }
        }
        ans.toArray
    }
}
```

## Rust

```rust
impl Solution {
    pub fn recover_array(n: i32, sums: Vec<i32>) -> Vec<i32> {
        let mut sorted = sums;
        sorted.sort_unstable();
        Self::helper(sorted, n as usize).unwrap()
    }

    fn helper(sums: Vec<i32>, n: usize) -> Option<Vec<i32>> {
        if n == 0 {
            return Some(vec![]);
        }
        // smallest sum is always 0 after sorting
        let diff = sums[1] - sums[0];
        if let Some(mut ans) = Self::try_candidate(&sums, diff, n) {
            return Some(ans);
        }
        if let Some(mut ans) = Self::try_candidate(&sums, -diff, n) {
            return Some(ans);
        }
        None
    }

    fn try_candidate(sums: &Vec<i32>, x: i32, n: usize) -> Option<Vec<i32>> {
        use std::collections::HashMap;
        let mut cnt: HashMap<i32, usize> = HashMap::new();
        for &v in sums.iter() {
            *cnt.entry(v).or_insert(0) += 1;
        }
        let mut without = Vec::with_capacity(sums.len() / 2);
        for &v in sums.iter() {
            if let Some(c) = cnt.get_mut(&v) {
                if *c == 0 {
                    continue;
                }
                *c -= 1;
            } else {
                continue;
            }
            let target = v + x;
            match cnt.get_mut(&target) {
                Some(c2) => {
                    if *c2 == 0 {
                        return None;
                    }
                    *c2 -= 1;
                }
                None => return None,
            }
            without.push(v);
        }
        let mut rec = Self::helper(without, n - 1)?;
        rec.push(x);
        Some(rec)
    }
}
```

## Racket

```racket
(define (recover n sums)
  (if (= n 0)
      '()
      (let* ((sorted (sort sums <))
             (diff (- (list-ref sorted 1) (list-ref sorted 0))))
        (define counts (make-hash))
        (for ([v sorted])
          (hash-update! counts v (lambda (c) (+ (or c 0) 1)) 0))
        (define groupA '())
        (define groupB '())
        (for ([x sorted])
          (when (> (hash-ref counts x 0) 0)
            (hash-set! counts x (- (hash-ref counts x) 1))
            (define y (+ x diff))
            (hash-set! counts y (- (hash-ref counts y) 1))
            (set! groupA (cons x groupA))
            (set! groupB (cons y groupB))))
        (set! groupA (reverse groupA))
        (set! groupB (reverse groupB))
        (if (member 0 groupA)
            (cons diff (recover (- n 1) groupA))
            (cons (- diff) (recover (- n 1) groupB))))))

(define/contract (recover-array n sums)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?))
  (recover n sums))
```

## Erlang

```erlang
-module(solution).
-export([recover_array/2]).

-spec recover_array(N :: integer(), Sums :: [integer()]) -> [integer()].
recover_array(N, Sums) ->
    Sorted = lists:sort(Sums),
    helper(N, Sorted).

helper(0, _Sums) -> [];
helper(N, SumsSorted) ->
    Smallest = hd(SumsSorted),
    SecondSmallest = lists:nth(2, SumsSorted),
    Diff = SecondSmallest - Smallest,
    Counts0 = build_counts(SumsSorted),
    case try_candidate(Diff, Counts0, SumsSorted) of
        {ok, Without} ->
            if lists:member(0, Without) ->
                    Rest = helper(N-1, Without),
                    [Diff | Rest];
               true -> try_neg(Diff, Counts0, SumsSorted, N)
            end;
        error ->
            try_neg(Diff, Counts0, SumsSorted, N)
    end.

try_neg(_Diff, _Counts0, _SumsSorted, _N) when _Diff =:= 0 ->
    []; % should not happen for valid inputs
try_neg(Diff, Counts0, SumsSorted, N) ->
    NegDiff = -Diff,
    case try_candidate(NegDiff, Counts0, SumsSorted) of
        {ok, Without} ->
            if lists:member(0, Without) ->
                    Rest = helper(N-1, Without),
                    [NegDiff | Rest];
               true -> [] % unreachable per problem guarantee
            end;
        error -> [] % unreachable per problem guarantee
    end.

build_counts(List) -> build_counts(List, #{}).

build_counts([], Map) -> Map;
build_counts([H|T], Map) ->
    NewMap = case maps:get(H, Map, 0) of
                0 -> maps:put(H,1,Map);
                C -> maps:put(H,C+1,Map)
             end,
    build_counts(T, NewMap).

try_candidate(_X, _Counts, []) -> {ok, []};
try_candidate(X, Counts0, SumsSorted) ->
    try_candidate_loop(SumsSorted, Counts0, [], X).

try_candidate_loop([], _Counts, AccWithout, _X) ->
    {ok, lists:reverse(AccWithout)};
try_candidate_loop([S|Rest], Counts, AccWithout, X) ->
    case maps:get(S, Counts, 0) of
        0 ->
            try_candidate_loop(Rest, Counts, AccWithout, X);
        C when C > 0 ->
            Counts1 = decrement(Counts, S),
            Counter = S + X,
            case maps:get(Counter, Counts1, 0) of
                0 -> error;
                _C2 ->
                    Counts2 = decrement(Counts1, Counter),
                    try_candidate_loop(Rest, Counts2, [S|AccWithout], X)
            end
    end.

decrement(Map, Key) ->
    case maps:get(Key, Map) of
        1 -> maps:remove(Key, Map);
        N when N > 1 -> maps:put(Key, N-1, Map)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec recover_array(n :: integer, sums :: [integer]) :: [integer]
  def recover_array(_n, sums) do
    sorted = Enum.sort(sums)
    recover_helper(sorted)
  end

  defp recover_helper([_single]), do: []

  defp recover_helper(sums) do
    len = length(sums)
    x = List.last(sums) - Enum.at(sums, len - 2)

    case try_candidate(sums, x) do
      {:ok, rest} ->
        rest ++ [x]

      :error ->
        {:ok, rest} = try_candidate(sums, -x)
        rest ++ [-x]
    end
  end

  defp try_candidate(sums, x) do
    cnt =
      Enum.reduce(sums, %{}, fn v, m ->
        Map.update(m, v, 1, &(&1 + 1))
      end)

    {status, result} =
      Enum.reduce_while(sums, {cnt, []}, fn s, {cmap, acc} ->
        case Map.get(cmap, s, 0) do
          0 ->
            {:cont, {cmap, acc}}

          _ ->
            if Map.get(cmap, s + x, 0) == 0 do
              {:halt, :error}
            else
              cmap1 = Map.update!(cmap, s, &(&1 - 1))
              cmap2 = Map.update!(cmap1, s + x, &(&1 - 1))
              {:cont, {cmap2, [s | acc]}}
            end
        end
      end)

    case status do
      :error ->
        :error

      _ ->
        without = Enum.reverse(result)

        if Enum.member?(without, 0) do
          {:ok, without}
        else
          :error
        end
    end
  end
end
```
