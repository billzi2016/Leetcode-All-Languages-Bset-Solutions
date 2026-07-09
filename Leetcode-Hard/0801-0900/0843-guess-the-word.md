# 0843. Guess the Word

## Cpp

```cpp
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *   public:
 *     int guess(string word);
 * };
 */
class Solution {
public:
    int match(const string& a, const string& b) {
        int cnt = 0;
        for (int i = 0; i < 6; ++i)
            if (a[i] == b[i]) ++cnt;
        return cnt;
    }
    
    void findSecretWord(vector<string>& words, Master& master) {
        vector<string> candidates = words;
        for (int attempt = 0; attempt < 10 && !candidates.empty(); ++attempt) {
            // Choose the word with minimal worst-case partition size
            string guessWord;
            int bestScore = INT_MAX;
            for (const string& w : candidates) {
                vector<int> freq(7, 0);
                for (const string& other : candidates) {
                    if (w == other) continue;
                    ++freq[match(w, other)];
                }
                int worst = *max_element(freq.begin(), freq.end());
                if (worst < bestScore) {
                    bestScore = worst;
                    guessWord = w;
                }
            }
            
            int matches = master.guess(guessWord);
            if (matches == 6) return; // guessed correctly
            
            vector<string> next;
            for (const string& w : candidates) {
                if (match(w, guessWord) == matches)
                    next.push_back(w);
            }
            candidates.swap(next);
        }
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public void findSecretWord(String[] words, Master master) {
        List<String> candidates = new ArrayList<>(Arrays.asList(words));
        for (int attempt = 0; attempt < 10 && !candidates.isEmpty(); attempt++) {
            String guess = selectBest(candidates);
            int matches = master.guess(guess);
            if (matches == 6) return;
            List<String> next = new ArrayList<>();
            for (String w : candidates) {
                if (match(w, guess) == matches) {
                    next.add(w);
                }
            }
            candidates = next;
        }
    }

    private String selectBest(List<String> candidates) {
        int minMax = Integer.MAX_VALUE;
        String best = null;
        for (String w : candidates) {
            int[] count = new int[7]; // match counts from 0 to 6
            for (String o : candidates) {
                if (w.equals(o)) continue;
                int m = match(w, o);
                count[m]++;
            }
            int maxGroup = 0;
            for (int c : count) {
                if (c > maxGroup) maxGroup = c;
            }
            if (maxGroup < minMax) {
                minMax = maxGroup;
                best = w;
            }
        }
        return best;
    }

    private int match(String a, String b) {
        int cnt = 0;
        for (int i = 0; i < 6; i++) {
            if (a.charAt(i) == b.charAt(i)) cnt++;
        }
        return cnt;
    }
}
```

## Python

```python
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master(object):
#     def guess(self, word):
#         """
#         :type word: str
#         :rtype int
#         """

class Solution(object):
    def findSecretWord(self, words, master):
        """
        :type words: List[str]
        :type master: Master
        :rtype: None
        """
        def match(w1, w2):
            cnt = 0
            for a, b in zip(w1, w2):
                if a == b:
                    cnt += 1
            return cnt

        candidates = words[:]
        attempts = 0
        while attempts < 10 and candidates:
            # Minimax: choose word with minimal worst-case group size
            best_word = None
            min_max_group = float('inf')
            for w in candidates:
                groups = [0] * 7  # possible matches 0..6
                for other in candidates:
                    if w == other:
                        continue
                    m = match(w, other)
                    groups[m] += 1
                worst = max(groups)
                if worst < min_max_group:
                    min_max_group = worst
                    best_word = w
            attempts += 1
            matches = master.guess(best_word)
            if matches == 6:
                return
            # filter candidates with same match count to the guessed word
            candidates = [w for w in candidates if match(w, best_word) == matches]
```

## Python3

```python
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

from typing import List

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def match(a: str, b: str) -> int:
            return sum(c1 == c2 for c1, c2 in zip(a, b))

        candidates = words[:]
        while candidates:
            # Choose the guess that minimizes the worst-case size of remaining candidates
            best_word = None
            min_max_group = float('inf')
            for w in candidates:
                groups = [0] * 7
                for other in candidates:
                    if w == other:
                        continue
                    groups[match(w, other)] += 1
                worst = max(groups)
                if worst < min_max_group:
                    min_max_group = worst
                    best_word = w

            matches = master.guess(best_word)
            if matches == 6:
                return
            # Keep only words that would give the same match count with the guessed word
            candidates = [w for w in candidates if match(w, best_word) == matches]
```

## C

```c
#include <limits.h>
#include <string.h>

int matchCount(const char *a, const char *b) {
    int cnt = 0;
    for (int i = 0; i < 6; ++i)
        if (a[i] == b[i]) ++cnt;
    return cnt;
}

/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * int guess(struct Master*, char *word);
 */
void findSecretWord(char **words, int wordsSize, struct Master *master) {
    int candidates[100];
    for (int i = 0; i < wordsSize; ++i) candidates[i] = i;
    int candCount = wordsSize;

    while (candCount > 0) {
        int bestIdx = -1;
        int bestScore = INT_MAX;

        // Choose the guess that minimizes the worst-case group size
        for (int i = 0; i < candCount; ++i) {
            int idx = candidates[i];
            int groups[7] = {0};

            for (int j = 0; j < candCount; ++j) {
                if (i == j) continue;
                int m = matchCount(words[idx], words[candidates[j]]);
                groups[m]++;
            }

            int worst = 0;
            for (int k = 0; k <= 6; ++k)
                if (groups[k] > worst) worst = groups[k];

            if (worst < bestScore) {
                bestScore = worst;
                bestIdx = idx;
            }
        }

        int matches = master->guess(master, words[bestIdx]);
        if (matches == 6) return; // guessed correctly

        // Filter candidates that have the same match count with the guess
        int newCandidates[100];
        int newCount = 0;
        for (int i = 0; i < candCount; ++i) {
            int idx = candidates[i];
            if (matchCount(words[bestIdx], words[idx]) == matches) {
                newCandidates[newCount++] = idx;
            }
        }

        memcpy(candidates, newCandidates, sizeof(int) * newCount);
        candCount = newCount;
    }
}
```

## Csharp

```csharp
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *     public int Guess(string word);
 * }
 */
using System;
using System.Collections.Generic;

class Solution {
    public void FindSecretWord(string[] words, Master master) {
        List<string> candidates = new List<string>(words);
        while (candidates.Count > 0) {
            string guess = "";
            int minMaxGroup = int.MaxValue;
            foreach (var w in candidates) {
                int[] groups = new int[7];
                foreach (var other in candidates) {
                    if (w == other) continue;
                    int m = Match(w, other);
                    groups[m]++;
                }
                int worst = 0;
                for (int i = 0; i <= 6; i++) {
                    if (groups[i] > worst) worst = groups[i];
                }
                if (worst < minMaxGroup) {
                    minMaxGroup = worst;
                    guess = w;
                }
            }

            int matches = master.Guess(guess);
            if (matches == 6) return;

            List<string> next = new List<string>();
            foreach (var w in candidates) {
                if (Match(guess, w) == matches) {
                    next.Add(w);
                }
            }
            candidates = next;
        }
    }

    private int Match(string a, string b) {
        int cnt = 0;
        for (int i = 0; i < 6; i++) {
            if (a[i] == b[i]) cnt++;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * // This is the master's API interface.
 * // You should not implement it, or speculate about its implementation
 * function Master() {
 *
 *     @param {string} word
 *     @return {integer}
 *     this.guess = function(word) {
 *         ...
 *     };
 * };
 */
/**
 * @param {string[]} words
 * @param {Master} master
 * @return {void}
 */
var findSecretWord = function(words, master) {
    const match = (a, b) => {
        let cnt = 0;
        for (let i = 0; i < 6; ++i) if (a[i] === b[i]) ++cnt;
        return cnt;
    };
    
    let candidates = words.slice();
    // allowed guesses are at most 10 according to constraints
    for (let attempt = 0; attempt < 10 && candidates.length > 0; ++attempt) {
        // choose the word with minimal worst-case remaining size
        let bestWord = null;
        let minWorst = Infinity;
        for (const w of candidates) {
            const groups = new Array(7).fill(0);
            for (const other of candidates) {
                groups[match(w, other)]++;
            }
            const worst = Math.max(...groups);
            if (worst < minWorst) {
                minWorst = worst;
                bestWord = w;
            }
        }
        const matches = master.guess(bestWord);
        if (matches === 6) return; // guessed correctly
        candidates = candidates.filter(w => match(w, bestWord) === matches);
    }
};
```

## Typescript

```typescript
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *     guess(word: string): number {}
 * }
 */

function findSecretWord(words: string[], master: Master): void {
    const match = (a: string, b: string): number => {
        let cnt = 0;
        for (let i = 0; i < 6; ++i) {
            if (a[i] === b[i]) cnt++;
        }
        return cnt;
    };

    let candidates = words.slice();

    for (let attempts = 0; attempts < 10 && candidates.length > 0; ++attempts) {
        // Choose the word that minimizes the worst-case size of remaining candidates
        let bestWord = "";
        let minMaxGroup = Number.MAX_SAFE_INTEGER;

        for (const w of candidates) {
            const freq = new Array(7).fill(0); // match counts from 0 to 6
            for (const other of candidates) {
                if (w === other) continue;
                const m = match(w, other);
                freq[m]++;
            }
            let maxGroup = 0;
            for (let k = 0; k <= 6; ++k) {
                if (freq[k] > maxGroup) maxGroup = freq[k];
            }
            if (maxGroup < minMaxGroup) {
                minMaxGroup = maxGroup;
                bestWord = w;
            }
        }

        const matches = master.guess(bestWord);
        if (matches === 6) return; // guessed correctly

        candidates = candidates.filter(word => match(word, bestWord) === matches);
    }
}
```

## Php

```php
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface Master {
 *     function guess($word) {}
 * }
 */

class Solution {
    /**
     * @param String[] $words
     * @param Master $master
     * @return void
     */
    function findSecretWord($words, $master) {
        $candidates = $words;
        while (true) {
            // Choose the guess that minimizes the worst-case size of remaining candidates
            $guess = '';
            $minMax = PHP_INT_MAX;
            foreach ($candidates as $w) {
                $counts = array_fill(0, 7, 0);
                foreach ($candidates as $other) {
                    if ($w === $other) continue;
                    $cnt = $this->match($w, $other);
                    $counts[$cnt]++;
                }
                $worst = max($counts);
                if ($worst < $minMax) {
                    $minMax = $worst;
                    $guess = $w;
                }
            }

            $matches = $master->guess($guess);
            if ($matches == 6) {
                return; // secret word found
            }

            // Filter candidates that would give the same match count with the guessed word
            $newCandidates = [];
            foreach ($candidates as $w) {
                if ($this->match($w, $guess) == $matches) {
                    $newCandidates[] = $w;
                }
            }
            $candidates = $newCandidates;
        }
    }

    private function match(string $a, string $b): int {
        $cnt = 0;
        for ($i = 0; $i < 6; $i++) {
            if ($a[$i] === $b[$i]) {
                $cnt++;
            }
        }
        return $cnt;
    }
}
```

## Swift

```swift
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *     public func guess(word: String) -> Int {}
 * }
 */
class Solution {
    private func match(_ a: String, _ b: String) -> Int {
        let arrA = Array(a)
        let arrB = Array(b)
        var cnt = 0
        for i in 0..<6 {
            if arrA[i] == arrB[i] { cnt += 1 }
        }
        return cnt
    }

    func findSecretWord(_ words: [String], _ master: Master) {
        var possible = words
        // The problem guarantees we can solve within 10 guesses.
        for _ in 0..<10 {
            // Choose the guess that minimizes the maximum group size after the guess.
            var bestWord = ""
            var minMaxGroupSize = Int.max

            for w in possible {
                var groups = [Int](repeating: 0, count: 7) // match counts from 0 to 6
                for other in possible {
                    let m = match(w, other)
                    groups[m] += 1
                }
                if let worst = groups.max(), worst < minMaxGroupSize {
                    minMaxGroupSize = worst
                    bestWord = w
                }
            }

            let matches = master.guess(word: bestWord)
            if matches == 6 { return } // guessed correctly

            // Filter candidates that would give the same match count with the guess.
            possible = possible.filter { match($0, bestWord) == matches }
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findSecretWord(words: Array<String>, master: Master) {
        var possible = words.toMutableList()
        repeat(10) {
            var guess = ""
            var minMax = Int.MAX_VALUE
            for (w in possible) {
                val groups = IntArray(7)
                for (v in possible) {
                    if (w == v) continue
                    groups[matchCount(w, v)]++
                }
                val worst = groups.maxOrNull() ?: 0
                if (worst < minMax) {
                    minMax = worst
                    guess = w
                }
            }
            val matches = master.guess(guess)
            if (matches == 6) return
            val next = mutableListOf<String>()
            for (w in possible) {
                if (matchCount(w, guess) == matches) {
                    next.add(w)
                }
            }
            possible = next
        }
    }

    private fun matchCount(a: String, b: String): Int {
        var cnt = 0
        for (i in 0 until 6) {
            if (a[i] == b[i]) cnt++
        }
        return cnt
    }
}
```

## Golang

```go
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * type Master struct {
 * }
 *
 * func (this *Master) Guess(word string) int {}
 */

func findSecretWord(words []string, master *Master) {
    const maxAttempts = 10

    match := func(a, b string) int {
        cnt := 0
        for i := 0; i < 6; i++ {
            if a[i] == b[i] {
                cnt++
            }
        }
        return cnt
    }

    for attempt := 0; attempt < maxAttempts && len(words) > 0; attempt++ {
        // Choose the guess that minimizes the worst-case size of remaining candidates.
        bestIdx := -1
        minWorst := len(words) + 1

        for i, w := range words {
            groups := make([]int, 7)
            for _, other := range words {
                if w == other {
                    continue
                }
                m := match(w, other)
                groups[m]++
            }
            worst := 0
            for _, sz := range groups {
                if sz > worst {
                    worst = sz
                }
            }
            if worst < minWorst {
                minWorst = worst
                bestIdx = i
            }
        }

        guess := words[bestIdx]
        matches := master.Guess(guess)
        if matches == 6 {
            return
        }

        // Filter candidates that would give the same match count with this guess.
        var next []string
        for _, w := range words {
            if match(w, guess) == matches {
                next = append(next, w)
            }
        }
        words = next
    }
}
```

## Ruby

```ruby
def find_secret_word(words, master)
  match = ->(a, b) {
    cnt = 0
    6.times { |i| cnt += 1 if a[i] == b[i] }
    cnt
  }

  loop do
    min_max = Float::INFINITY
    best = nil

    words.each do |w|
      buckets = Array.new(7, 0)
      words.each do |other|
        next if w == other
        buckets[match.call(w, other)] += 1
      end
      worst = buckets.max
      if worst < min_max
        min_max = worst
        best = w
      end
    end

    matches = master.guess(best)
    return if matches == 6
    words = words.select { |w| match.call(w, best) == matches }
  end
end
```

## Scala

```scala
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *
 *   def guess(word: String): Int = {}
 *
 * }
 */
object Solution {
  def findSecretWord(words: Array[String], master: Master): Unit = {
    def matchCount(a: String, b: String): Int = {
      var cnt = 0
      var i = 0
      while (i < 6) {
        if (a.charAt(i) == b.charAt(i)) cnt += 1
        i += 1
      }
      cnt
    }

    var candidates = words
    for (_ <- 0 until 10) {
      var bestWord = ""
      var minMaxGroup = Int.MaxValue

      for (w <- candidates) {
        val groups = new Array[Int](7)
        for (v <- candidates) {
          groups(matchCount(w, v)) += 1
        }
        val worst = groups.max
        if (worst < minMaxGroup) {
          minMaxGroup = worst
          bestWord = w
        }
      }

      val matches = master.guess(bestWord)
      if (matches == 6) return

      candidates = candidates.filter(w => matchCount(w, bestWord) == matches)
    }
  }
}
```

## Rust

```rust
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * struct Master;
 * impl Master {
 *     fn guess(&self, word: String) -> i32;
 * };
 */

impl Solution {
    pub fn find_secret_word(words: Vec<String>, master: &Master) {
        fn match_count(a: &String, b: &String) -> i32 {
            let mut cnt = 0;
            for (c1, c2) in a.as_bytes().iter().zip(b.as_bytes()) {
                if c1 == c2 {
                    cnt += 1;
                }
            }
            cnt
        }

        let mut candidates = words;

        for _ in 0..10 {
            let n = candidates.len();
            if n == 0 {
                break;
            }

            // Choose the guess that minimizes the worst-case remaining candidates
            let mut best_idx = 0usize;
            let mut min_max_group = usize::MAX;

            for i in 0..n {
                let mut groups = [0usize; 7];
                for j in 0..n {
                    let m = match_count(&candidates[i], &candidates[j]) as usize;
                    groups[m] += 1;
                }
                let max_group = *groups.iter().max().unwrap();
                if max_group < min_max_group {
                    min_max_group = max_group;
                    best_idx = i;
                }
            }

            let guess_word = candidates[best_idx].clone();
            let matches = master.guess(guess_word.clone()) as usize;

            if matches == 6 {
                return;
            }

            // Keep only words that would give the same match count with the guessed word
            candidates.retain(|w| match_count(w, &guess_word) as usize == matches);
        }
    }
}
```
