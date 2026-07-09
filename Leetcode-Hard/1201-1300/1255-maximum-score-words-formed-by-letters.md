# 1255. Maximum Score Words Formed by Letters

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
        int n = words.size();
        array<int,26> letterFreq{};
        for (char c : letters) letterFreq[c - 'a']++;

        vector<array<int,26>> cnts(n);
        vector<int> wScore(n);
        for (int i = 0; i < n; ++i) {
            cnts[i].fill(0);
            int s = 0;
            for (char ch : words[i]) {
                int idx = ch - 'a';
                cnts[i][idx]++;
                s += score[idx];
            }
            wScore[i] = s;
        }

        int ans = 0;
        int totalMasks = 1 << n;
        array<int,26> cur{};
        for (int mask = 0; mask < totalMasks; ++mask) {
            cur.fill(0);
            int sum = 0;
            bool ok = true;
            for (int i = 0; i < n && ok; ++i) {
                if (mask & (1 << i)) {
                    sum += wScore[i];
                    for (int c = 0; c < 26; ++c) {
                        cur[c] += cnts[i][c];
                        if (cur[c] > letterFreq[c]) {
                            ok = false;
                            break;
                        }
                    }
                }
            }
            if (ok) ans = max(ans, sum);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxScoreWords(String[] words, char[] letters, int[] score) {
        int[] letterFreq = new int[26];
        for (char c : letters) {
            letterFreq[c - 'a']++;
        }

        int n = words.length;
        int[][] wordCounts = new int[n][26];
        int[] wordScores = new int[n];

        for (int i = 0; i < n; i++) {
            String w = words[i];
            int[] cnt = new int[26];
            int s = 0;
            for (int k = 0; k < w.length(); k++) {
                char c = w.charAt(k);
                int idx = c - 'a';
                cnt[idx]++;
                s += score[idx];
            }
            wordCounts[i] = cnt;
            wordScores[i] = s;
        }

        int maxScore = 0;
        int totalMasks = 1 << n;

        for (int mask = 0; mask < totalMasks; mask++) {
            int[] used = new int[26];
            int curScore = 0;
            boolean valid = true;

            for (int i = 0; i < n && valid; i++) {
                if ((mask & (1 << i)) != 0) {
                    curScore += wordScores[i];
                    int[] wc = wordCounts[i];
                    for (int c = 0; c < 26; c++) {
                        used[c] += wc[c];
                        if (used[c] > letterFreq[c]) {
                            valid = false;
                            break;
                        }
                    }
                }
            }

            if (valid && curScore > maxScore) {
                maxScore = curScore;
            }
        }

        return maxScore;
    }
}
```

## Python

```python
class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        # frequency of available letters
        avail = [0] * 26
        for ch in letters:
            avail[ord(ch) - 97] += 1

        n = len(words)
        word_cnt = []
        word_score = []

        # precompute each word's letter count and its total score
        for w in words:
            cnt = [0] * 26
            s = 0
            for ch in w:
                idx = ord(ch) - 97
                cnt[idx] += 1
                s += score[idx]
            word_cnt.append(cnt)
            word_score.append(s)

        max_res = 0
        remain = avail[:]  # mutable remaining letters during backtracking

        def backtrack(i, cur):
            nonlocal max_res
            if i == n:
                if cur > max_res:
                    max_res = cur
                return

            # option 1: skip current word
            backtrack(i + 1, cur)

            # option 2: try to take current word if possible
            cnt = word_cnt[i]
            for c in range(26):
                if cnt[c] > remain[c]:
                    break
            else:
                # feasible, consume letters
                for c in range(26):
                    remain[c] -= cnt[c]
                backtrack(i + 1, cur + word_score[i])
                # restore letters
                for c in range(26):
                    remain[c] += cnt[c]

        backtrack(0, 0)
        return max_res
```

## Python3

```python
from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        # frequency of available letters
        avail = [0] * 26
        for ch in letters:
            avail[ord(ch) - 97] += 1

        # precompute each word's letter counts and its total score
        word_counts = []
        word_scores = []
        for w in words:
            cnt = [0] * 26
            s = 0
            for ch in w:
                idx = ord(ch) - 97
                cnt[idx] += 1
                s += score[idx]
            word_counts.append(cnt)
            word_scores.append(s)

        max_score = 0
        # enumerate all subsets of words
        for mask in range(1 << n):
            cur_cnt = [0] * 26
            cur_score = 0
            valid = True
            for i in range(n):
                if (mask >> i) & 1:
                    wc = word_counts[i]
                    # add this word's letters and check feasibility
                    for c in range(26):
                        cur_cnt[c] += wc[c]
                        if cur_cnt[c] > avail[c]:
                            valid = False
                            break
                    if not valid:
                        break
                    cur_score += word_scores[i]
            if valid and cur_score > max_score:
                max_score = cur_score

        return max_score
```

## C

```c
#include <stdbool.h>
#include <string.h>

int maxScoreWords(char** words, int wordsSize, char* letters, int lettersSize, int* score, int scoreSize) {
    int freq[26] = {0};
    for (int i = 0; i < lettersSize; ++i) {
        freq[letters[i] - 'a']++;
    }

    int cnt[14][26];
    int wscore[14];
    memset(cnt, 0, sizeof(cnt));

    for (int i = 0; i < wordsSize; ++i) {
        const char *w = words[i];
        int s = 0;
        while (*w) {
            int idx = *w - 'a';
            cnt[i][idx]++;
            s += score[idx];
            w++;
        }
        wscore[i] = s;
    }

    int maxScore = 0;
    int totalCnt[26];
    int limit = 1 << wordsSize;

    for (int mask = 0; mask < limit; ++mask) {
        memset(totalCnt, 0, sizeof(totalCnt));
        int curScore = 0;
        bool valid = true;

        for (int i = 0; i < wordsSize && valid; ++i) {
            if (mask & (1 << i)) {
                curScore += wscore[i];
                for (int c = 0; c < 26; ++c) {
                    totalCnt[c] += cnt[i][c];
                    if (totalCnt[c] > freq[c]) {
                        valid = false;
                        break;
                    }
                }
            }
        }

        if (valid && curScore > maxScore) {
            maxScore = curScore;
        }
    }

    return maxScore;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MaxScoreWords(string[] words, char[] letters, int[] score) {
        int n = words.Length;
        int[][] wordCounts = new int[n][];
        int[] wordScores = new int[n];

        for (int i = 0; i < n; i++) {
            int[] cnt = new int[26];
            int wScore = 0;
            foreach (char c in words[i]) {
                int idx = c - 'a';
                cnt[idx]++;
                wScore += score[idx];
            }
            wordCounts[i] = cnt;
            wordScores[i] = wScore;
        }

        int[] lettersCount = new int[26];
        foreach (char c in letters) {
            lettersCount[c - 'a']++;
        }

        int maxScore = 0;
        int totalMasks = 1 << n;

        for (int mask = 0; mask < totalMasks; mask++) {
            int[] need = new int[26];
            int curScore = 0;
            bool ok = true;

            for (int i = 0; i < n && ok; i++) {
                if ((mask & (1 << i)) != 0) {
                    curScore += wordScores[i];
                    int[] wc = wordCounts[i];
                    for (int k = 0; k < 26; k++) {
                        need[k] += wc[k];
                        if (need[k] > lettersCount[k]) {
                            ok = false;
                            break;
                        }
                    }
                }
            }

            if (ok && curScore > maxScore) {
                maxScore = curScore;
            }
        }

        return maxScore;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {character[]} letters
 * @param {number[]} score
 * @return {number}
 */
var maxScoreWords = function(words, letters, score) {
    const n = words.length;
    // frequency of available letters
    const avail = new Array(26).fill(0);
    for (const ch of letters) {
        avail[ch.charCodeAt(0) - 97]++;
    }
    // precompute each word's letter frequencies and its score
    const wordFreq = new Array(n);
    const wordScore = new Array(n);
    for (let i = 0; i < n; i++) {
        const freq = new Array(26).fill(0);
        let sc = 0;
        for (const ch of words[i]) {
            const idx = ch.charCodeAt(0) - 97;
            freq[idx]++;
            sc += score[idx];
        }
        wordFreq[i] = freq;
        wordScore[i] = sc;
    }

    let maxScore = 0;
    const totalMasks = 1 << n;
    for (let mask = 0; mask < totalMasks; mask++) {
        const cur = new Array(26).fill(0);
        let curScore = 0;
        let valid = true;
        for (let i = 0; i < n && valid; i++) {
            if ((mask >> i) & 1) {
                // add word i
                const wf = wordFreq[i];
                for (let c = 0; c < 26; c++) {
                    cur[c] += wf[c];
                    if (cur[c] > avail[c]) { // early prune
                        valid = false;
                        break;
                    }
                }
                curScore += wordScore[i];
            }
        }
        if (valid && curScore > maxScore) {
            maxScore = curScore;
        }
    }
    return maxScore;
};
```

## Typescript

```typescript
function maxScoreWords(words: string[], letters: string[], score: number[]): number {
    const n = words.length;
    const letterFreq = new Array(26).fill(0);
    for (const ch of letters) {
        letterFreq[ch.charCodeAt(0) - 97]++;
    }

    const wordCounts: number[][] = [];
    const wordScores: number[] = [];

    for (const w of words) {
        const cnt = new Array(26).fill(0);
        let s = 0;
        for (const ch of w) {
            const idx = ch.charCodeAt(0) - 97;
            cnt[idx]++;
            s += score[idx];
        }
        wordCounts.push(cnt);
        wordScores.push(s);
    }

    let maxScore = 0;
    const totalMasks = 1 << n;

    for (let mask = 0; mask < totalMasks; ++mask) {
        const cur = new Array(26).fill(0);
        let total = 0;
        let ok = true;

        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) {
                const cnt = wordCounts[i];
                for (let c = 0; c < 26; ++c) {
                    cur[c] += cnt[c];
                    if (cur[c] > letterFreq[c]) {
                        ok = false;
                        break;
                    }
                }
                total += wordScores[i];
                if (!ok) break;
            }
        }

        if (ok && total > maxScore) {
            maxScore = total;
        }
    }

    return maxScore;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @param String[] $letters
     * @param Integer[] $score
     * @return Integer
     */
    function maxScoreWords($words, $letters, $score) {
        // frequency of available letters
        $freq = array_fill(0, 26, 0);
        foreach ($letters as $ch) {
            $idx = ord($ch) - 97;
            if ($idx >= 0 && $idx < 26) {
                $freq[$idx]++;
            }
        }

        $n = count($words);
        // precompute each word's letter counts and its score
        $wordCounts = [];
        $wordScores = [];

        for ($i = 0; $i < $n; $i++) {
            $cnt = array_fill(0, 26, 0);
            $s = 0;
            $len = strlen($words[$i]);
            for ($j = 0; $j < $len; $j++) {
                $cIdx = ord($words[$i][$j]) - 97;
                if ($cIdx >= 0 && $cIdx < 26) {
                    $cnt[$cIdx]++;
                    $s += $score[$cIdx];
                }
            }
            $wordCounts[$i] = $cnt;
            $wordScores[$i] = $s;
        }

        $maxScore = 0;
        $totalMasks = 1 << $n;

        for ($mask = 0; $mask < $totalMasks; $mask++) {
            $need = array_fill(0, 26, 0);
            $curScore = 0;
            $valid = true;

            for ($i = 0; $i < $n; $i++) {
                if ((($mask >> $i) & 1) === 1) {
                    $curScore += $wordScores[$i];
                    $cntWord = $wordCounts[$i];
                    for ($c = 0; $c < 26; $c++) {
                        $need[$c] += $cntWord[$c];
                        if ($need[$c] > $freq[$c]) {
                            $valid = false;
                            break 2; // exit both loops early
                        }
                    }
                }
            }

            if ($valid && $curScore > $maxScore) {
                $maxScore = $curScore;
            }
        }

        return $maxScore;
    }
}
```

## Swift

```swift
class Solution {
    func maxScoreWords(_ words: [String], _ letters: [Character], _ score: [Int]) -> Int {
        var available = Array(repeating: 0, count: 26)
        for ch in letters {
            if let v = ch.asciiValue {
                let idx = Int(v - 97) // 'a' ascii is 97
                available[idx] += 1
            }
        }

        let n = words.count
        var wordCounts = [[Int]]()
        var wordScores = [Int]()
        for w in words {
            var cnt = Array(repeating: 0, count: 26)
            var sc = 0
            for ch in w {
                if let v = ch.asciiValue {
                    let idx = Int(v - 97)
                    cnt[idx] += 1
                    sc += score[idx]
                }
            }
            wordCounts.append(cnt)
            wordScores.append(sc)
        }

        var maxScore = 0

        func dfs(_ index: Int, _ currentScore: Int) {
            if index == n {
                if currentScore > maxScore { maxScore = currentScore }
                return
            }
            // Skip current word
            dfs(index + 1, currentScore)

            // Try to include current word
            var canUse = true
            for i in 0..<26 {
                if wordCounts[index][i] > available[i] {
                    canUse = false
                    break
                }
            }
            if canUse {
                for i in 0..<26 {
                    available[i] -= wordCounts[index][i]
                }
                dfs(index + 1, currentScore + wordScores[index])
                for i in 0..<26 {
                    available[i] += wordCounts[index][i]
                }
            }
        }

        dfs(0, 0)
        return maxScore
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxScoreWords(words: Array<String>, letters: CharArray, score: IntArray): Int {
        val n = words.size
        val wordCounts = Array(n) { IntArray(26) }
        val wordScores = IntArray(n)
        for (i in 0 until n) {
            var s = 0
            for (ch in words[i]) {
                val idx = ch - 'a'
                wordCounts[i][idx]++
                s += score[idx]
            }
            wordScores[i] = s
        }
        val freq = IntArray(26)
        for (ch in letters) {
            freq[ch - 'a']++
        }
        var maxScore = 0
        val totalCount = IntArray(26)
        val limitMask = 1 shl n
        for (mask in 1 until limitMask) {
            java.util.Arrays.fill(totalCount, 0)
            var curScore = 0
            var m = mask
            var idxWord = 0
            while (m != 0) {
                if ((m and 1) == 1) {
                    curScore += wordScores[idxWord]
                    val wc = wordCounts[idxWord]
                    for (c in 0 until 26) {
                        totalCount[c] += wc[c]
                    }
                }
                idxWord++
                m = m shr 1
            }
            var valid = true
            for (c in 0 until 26) {
                if (totalCount[c] > freq[c]) {
                    valid = false
                    break
                }
            }
            if (valid && curScore > maxScore) {
                maxScore = curScore
            }
        }
        return maxScore
    }
}
```

## Dart

```dart
class Solution {
  int maxScoreWords(List<String> words, List<String> letters, List<int> score) {
    const int alphabet = 26;
    // Frequency of available letters
    List<int> letterFreq = List.filled(alphabet, 0);
    for (var ch in letters) {
      int idx = ch.codeUnitAt(0) - 97;
      if (idx >= 0 && idx < alphabet) letterFreq[idx]++;
    }

    int n = words.length;
    // Precompute each word's frequency and its score
    List<List<int>> wordFreqs = List.generate(n, (_) => List.filled(alphabet, 0));
    List<int> wordScores = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      String w = words[i];
      int wScore = 0;
      for (int j = 0; j < w.length; j++) {
        int idx = w.codeUnitAt(j) - 97;
        if (idx >= 0 && idx < alphabet) {
          wordFreqs[i][idx]++;
          wScore += score[idx];
        }
      }
      wordScores[i] = wScore;
    }

    int maxScore = 0;
    int totalMasks = 1 << n;

    for (int mask = 0; mask < totalMasks; mask++) {
      List<int> need = List.filled(alphabet, 0);
      int curScore = 0;
      bool valid = true;

      for (int i = 0; i < n && valid; i++) {
        if ((mask >> i) & 1 == 1) {
          // add word i
          List<int> wf = wordFreqs[i];
          for (int c = 0; c < alphabet; c++) {
            need[c] += wf[c];
            if (need[c] > letterFreq[c]) {
              valid = false;
              break;
            }
          }
          curScore += wordScores[i];
        }
      }

      if (valid && curScore > maxScore) {
        maxScore = curScore;
      }
    }

    return maxScore;
  }
}
```

## Golang

```go
func maxScoreWords(words []string, letters []byte, score []int) int {
    var freq [26]int
    for _, b := range letters {
        freq[b-'a']++
    }

    n := len(words)
    wordCnt := make([][26]int, n)
    wordScore := make([]int, n)

    for i, w := range words {
        var cnt [26]int
        s := 0
        for _, ch := range w {
            idx := ch - 'a'
            cnt[idx]++
            s += score[idx]
        }
        wordCnt[i] = cnt
        wordScore[i] = s
    }

    maxAns := 0
    totalMasks := 1 << n

    for mask := 0; mask < totalMasks; mask++ {
        var cur [26]int
        sum := 0
        ok := true
        for i := 0; i < n && ok; i++ {
            if (mask>>i)&1 == 1 {
                wc := wordCnt[i]
                for c := 0; c < 26; c++ {
                    cur[c] += wc[c]
                    if cur[c] > freq[c] {
                        ok = false
                        break
                    }
                }
                sum += wordScore[i]
            }
        }
        if ok && sum > maxAns {
            maxAns = sum
        }
    }

    return maxAns
}
```

## Ruby

```ruby
def max_score_words(words, letters, score)
  # Frequency of available letters
  avail = Array.new(26, 0)
  letters.each { |ch| avail[ch.ord - 97] += 1 }

  n = words.length
  word_counts = Array.new(n) { Array.new(26, 0) }
  word_scores = Array.new(n, 0)

  # Precompute each word's letter counts and its score
  words.each_with_index do |w, idx|
    cnt = word_counts[idx]
    sc = 0
    w.each_char do |c|
      i = c.ord - 97
      cnt[i] += 1
      sc += score[i]
    end
    word_scores[idx] = sc
  end

  max_score = 0
  total_masks = 1 << n

  (0...total_masks).each do |mask|
    cur_counts = Array.new(26, 0)
    cur_score = 0
    valid = true

    i = 0
    while i < n
      if (mask & (1 << i)) != 0
        wc = word_counts[i]
        26.times do |k|
          cur_counts[k] += wc[k]
          if cur_counts[k] > avail[k]
            valid = false
            break
          end
        end
        break unless valid
        cur_score += word_scores[i]
      end
      i += 1
    end

    max_score = cur_score if valid && cur_score > max_score
  end

  max_score
end
```

## Scala

```scala
object Solution {
    def maxScoreWords(words: Array[String], letters: Array[Char], score: Array[Int]): Int = {
        val n = words.length
        // Precompute letter counts and word scores
        val wordCounts = Array.ofDim[Int](n, 26)
        val wordScores = new Array[Int](n)

        for (i <- 0 until n) {
            var s = 0
            for (ch <- words(i)) {
                val idx = ch - 'a'
                wordCounts(i)(idx) += 1
                s += score(idx)
            }
            wordScores(i) = s
        }

        // Frequency of available letters
        val freq = new Array[Int](26)
        for (c <- letters) {
            freq(c - 'a') += 1
        }

        var maxScore = 0
        val totalMasks = 1 << n

        for (mask <- 0 until totalMasks) {
            val curCounts = new Array[Int](26)
            var curScore = 0
            var valid = true
            var i = 0
            while (i < n && valid) {
                if ((mask & (1 << i)) != 0) {
                    curScore += wordScores(i)
                    val wc = wordCounts(i)
                    var j = 0
                    while (j < 26) {
                        curCounts(j) += wc(j)
                        if (curCounts(j) > freq(j)) {
                            valid = false
                        }
                        j += 1
                    }
                }
                i += 1
            }
            if (valid && curScore > maxScore) {
                maxScore = curScore
            }
        }

        maxScore
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_score_words(words: Vec<String>, letters: Vec<char>, score: Vec<i32>) -> i32 {
        fn dfs(
            idx: usize,
            cnts: &Vec<[i32; 26]>,
            scores: &Vec<i32>,
            freq: &[i32; 26],
            used: &mut [i32; 26],
            cur_score: i32,
            best: &mut i32,
        ) {
            if idx == cnts.len() {
                if cur_score > *best {
                    *best = cur_score;
                }
                return;
            }

            // skip current word
            dfs(idx + 1, cnts, scores, freq, used, cur_score, best);

            // try to include current word
            let mut can_take = true;
            for c in 0..26 {
                if used[c] + cnts[idx][c] > freq[c] {
                    can_take = false;
                    break;
                }
            }
            if can_take {
                for c in 0..26 {
                    used[c] += cnts[idx][c];
                }
                dfs(
                    idx + 1,
                    cnts,
                    scores,
                    freq,
                    used,
                    cur_score + scores[idx],
                    best,
                );
                for c in 0..26 {
                    used[c] -= cnts[idx][c];
                }
            }
        }

        // frequency of available letters
        let mut freq = [0i32; 26];
        for ch in letters {
            let idx = (ch as u8 - b'a') as usize;
            freq[idx] += 1;
        }

        // preprocess words: count letters and compute word scores
        let mut raw_cnts = Vec::with_capacity(words.len());
        let mut raw_scores = Vec::with_capacity(words.len());

        for w in &words {
            let mut cnt = [0i32; 26];
            let mut sc = 0i32;
            for ch in w.chars() {
                let idx = (ch as u8 - b'a') as usize;
                cnt[idx] += 1;
                sc += score[idx];
            }
            raw_cnts.push(cnt);
            raw_scores.push(sc);
        }

        // filter out words that cannot be formed at all
        let mut cnts = Vec::new();
        let mut scores = Vec::new();
        for i in 0..raw_cnts.len() {
            let mut ok = true;
            for c in 0..26 {
                if raw_cnts[i][c] > freq[c] {
                    ok = false;
                    break;
                }
            }
            if ok {
                cnts.push(raw_cnts[i]);
                scores.push(raw_scores[i]);
            }
        }

        let mut best = 0i32;
        let mut used = [0i32; 26];
        dfs(0, &cnts, &scores, &freq, &mut used, 0, &mut best);
        best
    }
}
```

## Racket

```racket
(define/contract (max-score-words words letters score)
  (-> (listof string?) (listof char?) (listof exact-integer?) exact-integer?)
  (let* ([n (length words)]
         [freq (make-vector 26 0)])
    ;; frequency of available letters
    (for ([c letters])
      (define idx (- (char->integer c) (char->integer #\a)))
      (vector-set! freq idx (+ (vector-ref freq idx) 1)))
    ;; score vector for O(1) access
    (define score-vec (list->vector score))
    ;; pre‑compute each word's letter counts and its own score
    (define word-counts
      (for/vector ([w words])
        (let ([cnt (make-vector 26 0)])
          (for ([c (in-string w)])
            (define idx (- (char->integer c) (char->integer #\a)))
            (vector-set! cnt idx (+ (vector-ref cnt idx) 1)))
          cnt)))
    (define word-scores
      (for/vector ([w words])
        (let ([s 0])
          (for ([c (in-string w)])
            (define idx (- (char->integer c) (char->integer #\a)))
            (set! s (+ s (vector-ref score-vec idx))))
          s)))
    (define max-score 0)
    (define total-masks (arithmetic-shift 1 n)) ; 2^n
    (for ([mask (in-range total-masks)])
      (let ([counts (make-vector 26 0)]
            [total 0]
            [valid #t])
        ;; add words whose bits are set in mask
        (for ([i (in-range n)])
          (when (not (zero? (bitwise-and mask (arithmetic-shift 1 i))))
            (define wc (vector-ref word-counts i))
            (define ws (vector-ref word-scores i))
            (set! total (+ total ws))
            (for ([j (in-range 26)])
              (vector-set! counts j
                           (+ (vector-ref counts j) (vector-ref wc j))))))
        ;; validate against available letters
        (for ([j (in-range 26)])
          (when (> (vector-ref counts j) (vector-ref freq j))
            (set! valid #f)))
        (when (and valid (> total max-score))
          (set! max-score total)))))
    max-score))
```

## Erlang

```erlang
-spec max_score_words(Words :: [unicode:unicode_binary()], Letters :: [char()], Score :: [integer()]) -> integer().
max_score_words(Words, Letters, Score) ->
    Available = build_freq(Letters),
    WordData = [build_word_data(W, Score) || W <- Words],
    N = length(WordData),
    MaxMask = (1 bsl N) - 1,
    max_score_loop(0, MaxMask, WordData, Available, 0).

%% Build frequency list for given letters
build_freq(Letters) ->
    lists:foldl(fun(C, Acc) -> inc_char(C, Acc) end,
                lists:duplicate(26, 0),
                Letters).

inc_char(Char, List) ->
    Index = Char - $a,
    update_at(Index, List, fun(V) -> V + 1 end).

%% Build word frequency list and its total score
build_word_data(WordBin, ScoreList) ->
    Chars = binary_to_list(WordBin),
    {Freq, WordScore} =
        lists:foldl(fun(C, {FAcc, SAcc}) ->
                        Index = C - $a,
                        NewF = update_at(Index, FAcc, fun(V) -> V + 1 end),
                        CharScore = lists:nth(Index + 1, ScoreList),
                        {NewF, SAcc + CharScore}
                    end,
                    {lists:duplicate(26, 0), 0},
                    Chars),
    {Freq, WordScore}.

%% Update element at Index (0‑based) using Fun
update_at(Idx, List, Fun) ->
    update_at(Idx, List, Fun, []).

update_at(0, [H|T], Fun, Rev) ->
    lists:reverse(Rev) ++ [Fun(H) | T];
update_at(N, [H|T], Fun, Rev) when N > 0 ->
    update_at(N - 1, T, Fun, [H|Rev]).

%% Loop over all masks
max_score_loop(Mask, MaxMask, _WordData, _Available, CurrentMax) when Mask > MaxMask ->
    CurrentMax;
max_score_loop(Mask, MaxMask, WordData, Available, CurrentMax) ->
    {NeedFreq, TotalScore} = compute_mask(WordData, Mask),
    NewMax =
        case leq(NeedFreq, Available) of
            true -> max(CurrentMax, TotalScore);
            false -> CurrentMax
        end,
    max_score_loop(Mask + 1, MaxMask, WordData, Available, NewMax).

%% Compute needed frequencies and total score for a mask
compute_mask(WordData, Mask) ->
    compute_mask(WordData, Mask, 0, lists:duplicate(26, 0), 0).

compute_mask([], _Mask, _Idx, NeedAcc, ScoreAcc) ->
    {NeedAcc, ScoreAcc};
compute_mask([{Freq,Score}|Rest], Mask, Idx, NeedAcc, ScoreAcc) ->
    case (Mask band (1 bsl Idx)) =/= 0 of
        true ->
            NewNeed = add_freq(NeedAcc, Freq),
            compute_mask(Rest, Mask, Idx + 1, NewNeed, ScoreAcc + Score);
        false ->
            compute_mask(Rest, Mask, Idx + 1, NeedAcc, ScoreAcc)
    end.

add_freq(A, B) ->
    lists:zipwith(fun(X,Y) -> X + Y end, A, B).

leq(Needed, Available) ->
    lists:all(fun({N,A}) -> N =< A end,
              lists:zip(Needed, Available)).

max(A,B) when A >= B -> A;
max(_,B) -> B.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_score_words(words :: [String.t()], letters :: [char], score :: [integer]) :: integer
  def max_score_words(words, letters, score) do
    letters_freq = freq_array(letters)

    {word_freqs, word_scores} =
      Enum.map(words, fn w ->
        wf = freq_string(w)
        ws = compute_word_score(wf, score)
        {wf, ws}
      end)
      |> Enum.unzip()

    dfs(
      0,
      length(words),
      word_freqs,
      word_scores,
      letters_freq,
      List.duplicate(0, 26),
      0
    )
  end

  defp freq_array(chars) do
    Enum.reduce(chars, List.duplicate(0, 26), fn ch, acc ->
      idx =
        case ch do
          <<c>> -> c - ?a
          c when is_integer(c) -> c - ?a
        end

      List.update_at(acc, idx, &(&1 + 1))
    end)
  end

  defp freq_string(str) do
    str
    |> String.to_charlist()
    |> Enum.reduce(List.duplicate(0, 26), fn c, acc ->
      idx = c - ?a
      List.update_at(acc, idx, &(&1 + 1))
    end)
  end

  defp compute_word_score(freqs, score) do
    Enum.reduce(0..25, 0, fn i, sum ->
      sum + Enum.at(freqs, i) * Enum.at(score, i)
    end)
  end

  defp dfs(idx, n, word_freqs, word_scores, letters_freq, cur_counts, cur_score) do
    if idx == n do
      cur_score
    else
      # Skip current word
      max_score = dfs(idx + 1, n, word_freqs, word_scores, letters_freq, cur_counts, cur_score)

      wfreq = Enum.at(word_freqs, idx)

      can_use =
        Enum.all?(0..25, fn i ->
          Enum.at(cur_counts, i) + Enum.at(wfreq, i) <= Enum.at(letters_freq, i)
        end)

      if can_use do
        new_counts =
          Enum.map(0..25, fn i -> Enum.at(cur_counts, i) + Enum.at(wfreq, i) end)

        include_score =
          dfs(
            idx + 1,
            n,
            word_freqs,
            word_scores,
            letters_freq,
            new_counts,
            cur_score + Enum.at(word_scores, idx)
          )

        if include_score > max_score, do: include_score, else: max_score
      else
        max_score
      end
    end
  end
end
```
