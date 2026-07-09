# 0030. Substring with Concatenation of All Words

## Cpp

```cpp
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> result;
        int n = s.size();
        int m = words.size();
        if (m == 0) return result;
        int len = words[0].size();
        long totalLen = 1L * m * len;
        if (n < totalLen) return result;

        unordered_map<string, int> target;
        for (const string& w : words) ++target[w];

        for (int offset = 0; offset < len; ++offset) {
            int left = offset;
            int count = 0;
            unordered_map<string, int> window;
            for (int j = offset; j + len <= n; j += len) {
                string cur = s.substr(j, len);
                if (target.find(cur) != target.end()) {
                    ++window[cur];
                    ++count;

                    while (window[cur] > target[cur]) {
                        string leftWord = s.substr(left, len);
                        --window[leftWord];
                        --count;
                        left += len;
                    }

                    if (count == m) {
                        result.push_back(left);
                        // move left forward to look for next possible window
                        string leftWord = s.substr(left, len);
                        --window[leftWord];
                        --count;
                        left += len;
                    }
                } else {
                    window.clear();
                    count = 0;
                    left = j + len;
                }
            }
        }

        return result;
    }
};
```

## Java

```java
class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        if (s == null || s.length() == 0 || words == null || words.length == 0) {
            return result;
        }
        int wordLen = words[0].length();
        int numWords = words.length;
        int totalLen = wordLen * numWords;
        if (s.length() < totalLen) {
            return result;
        }

        Map<String, Integer> target = new HashMap<>();
        for (String w : words) {
            target.put(w, target.getOrDefault(w, 0) + 1);
        }

        for (int offset = 0; offset < wordLen; offset++) {
            int left = offset;
            int count = 0;
            Map<String, Integer> window = new HashMap<>();

            for (int j = offset; j + wordLen <= s.length(); j += wordLen) {
                String sub = s.substring(j, j + wordLen);
                if (!target.containsKey(sub)) {
                    window.clear();
                    count = 0;
                    left = j + wordLen;
                    continue;
                }

                window.put(sub, window.getOrDefault(sub, 0) + 1);
                count++;

                while (window.get(sub) > target.get(sub)) {
                    String leftWord = s.substring(left, left + wordLen);
                    int cnt = window.get(leftWord);
                    if (cnt == 1) {
                        window.remove(leftWord);
                    } else {
                        window.put(leftWord, cnt - 1);
                    }
                    left += wordLen;
                    count--;
                }

                if (count == numWords) {
                    result.add(left);
                    // move left to look for next possible start
                    String leftWord = s.substring(left, left + wordLen);
                    int cnt = window.get(leftWord);
                    if (cnt == 1) {
                        window.remove(leftWord);
                    } else {
                        window.put(leftWord, cnt - 1);
                    }
                    left += wordLen;
                    count--;
                }
            }
        }

        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        if total_len > len(s):
            return []

        from collections import Counter
        target = Counter(words)
        res = []

        for offset in range(word_len):
            left = offset
            cur_counter = Counter()
            count = 0
            # slide window by word_len steps
            for j in range(offset, len(s) - word_len + 1, word_len):
                w = s[j:j + word_len]
                if w in target:
                    cur_counter[w] += 1
                    count += 1
                    # shrink left side while exceed allowed frequency
                    while cur_counter[w] > target[w]:
                        left_word = s[left:left + word_len]
                        cur_counter[left_word] -= 1
                        left += word_len
                        count -= 1
                    if count == num_words:
                        res.append(left)
                else:
                    # reset window
                    cur_counter.clear()
                    count = 0
                    left = j + word_len
        return res
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        n = len(s)
        if total_len > n:
            return []

        need = Counter(words)
        res = []

        for offset in range(word_len):
            left = offset
            cur_counter = Counter()
            matched = 0
            # slide window by word length
            for j in range(offset, n - word_len + 1, word_len):
                w = s[j:j + word_len]
                if w in need:
                    cur_counter[w] += 1
                    matched += 1
                    while cur_counter[w] > need[w]:
                        left_word = s[left:left + word_len]
                        cur_counter[left_word] -= 1
                        matched -= 1
                        left += word_len
                    if matched == num_words:
                        res.append(left)
                else:
                    cur_counter.clear()
                    matched = 0
                    left = j + word_len

        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *key;
    int count;
    int used;   // 0 = empty, 1 = occupied
} Entry;

typedef struct {
    Entry *table;
    size_t size;
    unsigned mask;
    int wordLen;
} HashMap;

/* djb2 hash for a string of given length */
static unsigned hash_str(const char *s, int len) {
    unsigned h = 5381;
    for (int i = 0; i < len; ++i)
        h = ((h << 5) + h) + (unsigned)(s[i]);
    return h;
}

/* insert or increase count of a word in the hashmap */
static int hashmap_put(HashMap *hm, const char *key) {
    unsigned h = hash_str(key, hm->wordLen) & hm->mask;
    while (hm->table[h].used) {
        if (strcmp(hm->table[h].key, key) == 0) {
            hm->table[h].count++;
            return (int)h;
        }
        h = (h + 1) & hm->mask;
    }
    hm->table[h].used = 1;
    hm->table[h].key = (char *)key;   // original pointer is valid for whole call
    hm->table[h].count = 1;
    return (int)h;
}

/* lookup index of a substring (not null‑terminated) */
static int hashmap_get_idx(HashMap *hm, const char *sub) {
    unsigned h = hash_str(sub, hm->wordLen) & hm->mask;
    while (hm->table[h].used) {
        if (strncmp(hm->table[h].key, sub, hm->wordLen) == 0)
            return (int)h;
        h = (h + 1) & hm->mask;
    }
    return -1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findSubstring(char* s, char** words, int wordsSize, int* returnSize) {
    int wordLen = (int)strlen(words[0]);
    int totalLen = wordLen * wordsSize;
    int n = (int)strlen(s);
    *returnSize = 0;
    if (n < totalLen)
        return NULL;

    /* build hashmap of required word counts */
    size_t tblSize = 1;
    while (tblSize < (size_t)wordsSize * 2) tblSize <<= 1;
    HashMap hm;
    hm.size = tblSize;
    hm.mask = (unsigned)(tblSize - 1);
    hm.wordLen = wordLen;
    hm.table = calloc(tblSize, sizeof(Entry));

    for (int i = 0; i < wordsSize; ++i)
        hashmap_put(&hm, words[i]);

    int *result = malloc(sizeof(int) * n);   // maximum possible size
    int resCnt = 0;

    int *curCount = calloc(hm.size, sizeof(int));

    for (int offset = 0; offset < wordLen; ++offset) {
        memset(curCount, 0, hm.size * sizeof(int));
        int left = offset;
        int matched = 0;

        for (int right = offset; right + wordLen <= n; right += wordLen) {
            const char *sub = s + right;
            int idx = hashmap_get_idx(&hm, sub);
            if (idx == -1) {                     // invalid word, reset window
                memset(curCount, 0, hm.size * sizeof(int));
                matched = 0;
                left = right + wordLen;
                continue;
            }

            curCount[idx]++;
            if (curCount[idx] <= hm.table[idx].count)
                matched++;
            else {
                /* too many of this word, shrink from left */
                while (curCount[idx] > hm.table[idx].count) {
                    const char *leftWord = s + left;
                    int lIdx = hashmap_get_idx(&hm, leftWord);
                    curCount[lIdx]--;
                    if (curCount[lIdx] < hm.table[lIdx].count)
                        matched--;
                    left += wordLen;
                }
            }

            if (matched == wordsSize) {
                result[resCnt++] = left;

                /* move window forward by one word */
                const char *leftWord = s + left;
                int lIdx = hashmap_get_idx(&hm, leftWord);
                curCount[lIdx]--;
                matched--;
                left += wordLen;
            }
        }
    }

    free(curCount);
    free(hm.table);

    if (resCnt == 0) {
        free(result);
        *returnSize = 0;
        return NULL;
    }

    *returnSize = resCnt;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> FindSubstring(string s, string[] words) {
        var result = new List<int>();
        if (string.IsNullOrEmpty(s) || words == null || words.Length == 0)
            return result;

        int wordLen = words[0].Length;
        int numWords = words.Length;
        int totalLen = wordLen * numWords;
        if (s.Length < totalLen)
            return result;

        var target = new Dictionary<string, int>();
        foreach (var w in words) {
            if (target.ContainsKey(w))
                target[w]++;
            else
                target[w] = 1;
        }

        for (int offset = 0; offset < wordLen; offset++) {
            int left = offset, right = offset, count = 0;
            var window = new Dictionary<string, int>();

            while (right + wordLen <= s.Length) {
                string word = s.Substring(right, wordLen);
                right += wordLen;

                if (!target.ContainsKey(word)) {
                    window.Clear();
                    count = 0;
                    left = right;
                    continue;
                }

                if (!window.ContainsKey(word))
                    window[word] = 0;
                window[word]++;
                count++;

                while (window[word] > target[word]) {
                    string leftWord = s.Substring(left, wordLen);
                    window[leftWord]--;
                    left += wordLen;
                    count--;
                }

                if (count == numWords) {
                    result.Add(left);
                }
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */
var findSubstring = function(s, words) {
    const result = [];
    if (!s || words.length === 0) return result;
    
    const wordLen = words[0].length;
    const wordCount = words.length;
    const totalLen = wordLen * wordCount;
    if (s.length < totalLen) return result;
    
    // Build need map
    const need = new Map();
    for (const w of words) {
        need.set(w, (need.get(w) || 0) + 1);
    }
    
    // Iterate over each possible offset within word length
    for (let offset = 0; offset < wordLen; offset++) {
        let left = offset;
        let count = 0;
        const windowMap = new Map();
        
        for (let j = offset; j + wordLen <= s.length; j += wordLen) {
            const curWord = s.substring(j, j + wordLen);
            
            if (need.has(curWord)) {
                windowMap.set(curWord, (windowMap.get(curWord) || 0) + 1);
                count++;
                
                // Shrink from left if we have excess of current word
                while (windowMap.get(curWord) > need.get(curWord)) {
                    const leftWord = s.substring(left, left + wordLen);
                    windowMap.set(leftWord, windowMap.get(leftWord) - 1);
                    left += wordLen;
                    count--;
                }
                
                // When we have exactly the needed number of words
                if (count === wordCount) {
                    result.push(left);
                    
                    // Move left forward to look for next possible start
                    const leftWord = s.substring(left, left + wordLen);
                    windowMap.set(leftWord, windowMap.get(leftWord) - 1);
                    left += wordLen;
                    count--;
                }
            } else {
                // Reset the window
                windowMap.clear();
                count = 0;
                left = j + wordLen;
            }
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function findSubstring(s: string, words: string[]): number[] {
    const result: number[] = [];
    if (words.length === 0 || s.length === 0) return result;

    const wordLen = words[0].length;
    const wordCount = words.length;
    const totalLen = wordLen * wordCount;
    if (s.length < totalLen) return result;

    const need = new Map<string, number>();
    for (const w of words) {
        need.set(w, (need.get(w) ?? 0) + 1);
    }

    for (let offset = 0; offset < wordLen; offset++) {
        let left = offset;
        let right = offset;
        const window = new Map<string, number>();
        let matched = 0;

        while (right + wordLen <= s.length) {
            const curWord = s.substring(right, right + wordLen);
            right += wordLen;

            if (!need.has(curWord)) {
                window.clear();
                matched = 0;
                left = right;
                continue;
            }

            window.set(curWord, (window.get(curWord) ?? 0) + 1);
            matched++;

            while ((window.get(curWord) ?? 0) > (need.get(curWord) ?? 0)) {
                const leftWord = s.substring(left, left + wordLen);
                window.set(leftWord, (window.get(leftWord) ?? 0) - 1);
                left += wordLen;
                matched--;
            }

            if (matched === wordCount) {
                result.push(left);
                const leftWord = s.substring(left, left + wordLen);
                window.set(leftWord, (window.get(leftWord) ?? 0) - 1);
                left += wordLen;
                matched--;
            }
        }
    }

    return result;
};
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String[] $words
     * @return Integer[]
     */
    function findSubstring($s, $words) {
        $wordLen = strlen($words[0]);
        $numWords = count($words);
        $totalLen = $wordLen * $numWords;
        $sLen = strlen($s);
        if ($sLen < $totalLen) {
            return [];
        }

        // frequency map of required words
        $need = [];
        foreach ($words as $w) {
            if (isset($need[$w])) {
                $need[$w]++;
            } else {
                $need[$w] = 1;
            }
        }

        $result = [];

        for ($i = 0; $i < $wordLen; $i++) {
            $left = $i;
            $count = 0;
            $curr = [];

            for ($j = $i; $j <= $sLen - $wordLen; $j += $wordLen) {
                $word = substr($s, $j, $wordLen);

                if (!isset($need[$word])) {
                    // reset window
                    $curr = [];
                    $count = 0;
                    $left = $j + $wordLen;
                    continue;
                }

                $curr[$word] = ($curr[$word] ?? 0) + 1;
                $count++;

                while ($curr[$word] > $need[$word]) {
                    $leftWord = substr($s, $left, $wordLen);
                    $curr[$leftWord]--;
                    $count--;
                    $left += $wordLen;
                }

                if ($count == $numWords) {
                    $result[] = $left;

                    // move left forward to search for next possible window
                    $leftWord = substr($s, $left, $wordLen);
                    $curr[$leftWord]--;
                    $count--;
                    $left += $wordLen;
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findSubstring(_ s: String, _ words: [String]) -> [Int] {
        guard !words.isEmpty else { return [] }
        let wordLen = words[0].count
        let nWords = words.count
        let totalLen = wordLen * nWords
        if s.count < totalLen { return [] }

        var target = [String:Int]()
        for w in words {
            target[w, default: 0] += 1
        }

        var result = [Int]()
        let chars = Array(s)
        let sCount = chars.count

        func getWord(_ start: Int) -> String {
            return String(chars[start..<start + wordLen])
        }

        for offset in 0..<wordLen {
            var left = offset
            var curCount = [String:Int]()
            var count = 0
            var j = offset
            while j + wordLen <= sCount {
                let sub = getWord(j)
                if target[sub] != nil {
                    curCount[sub, default: 0] += 1
                    count += 1

                    while curCount[sub]! > target[sub]! {
                        let leftWord = getWord(left)
                        curCount[leftWord]! -= 1
                        if curCount[leftWord]! == 0 {
                            curCount.removeValue(forKey: leftWord)
                        }
                        left += wordLen
                        count -= 1
                    }

                    if count == nWords {
                        result.append(left)
                        let leftWord = getWord(left)
                        curCount[leftWord]! -= 1
                        if curCount[leftWord]! == 0 {
                            curCount.removeValue(forKey: leftWord)
                        }
                        left += wordLen
                        count -= 1
                    }
                } else {
                    curCount.removeAll()
                    count = 0
                    left = j + wordLen
                }
                j += wordLen
            }
        }

        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findSubstring(s: String, words: Array<String>): List<Int> {
        if (words.isEmpty() || s.isEmpty()) return emptyList()
        val wordLen = words[0].length
        val wordCount = words.size
        val totalLen = wordLen * wordCount
        if (s.length < totalLen) return emptyList()

        val target = HashMap<String, Int>()
        for (w in words) {
            target[w] = target.getOrDefault(w, 0) + 1
        }

        val result = ArrayList<Int>()

        for (offset in 0 until wordLen) {
            var left = offset
            var right = offset
            var matched = 0
            val window = HashMap<String, Int>()

            while (right + wordLen <= s.length) {
                val word = s.substring(right, right + wordLen)
                right += wordLen

                if (!target.containsKey(word)) {
                    window.clear()
                    matched = 0
                    left = right
                    continue
                }

                window[word] = window.getOrDefault(word, 0) + 1
                matched++

                while (window[word]!! > target[word]!!) {
                    val leftWord = s.substring(left, left + wordLen)
                    window[leftWord] = window[leftWord]!! - 1
                    matched--
                    left += wordLen
                }

                if (matched == wordCount) {
                    result.add(left)
                    // slide one word forward
                    val leftWord = s.substring(left, left + wordLen)
                    window[leftWord] = window[leftWord]!! - 1
                    matched--
                    left += wordLen
                }
            }
        }

        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findSubstring(String s, List<String> words) {
    if (words.isEmpty || s.isEmpty) return [];

    int wordLen = words[0].length;
    int totalWords = words.length;
    int substringSize = wordLen * totalWords;
    if (s.length < substringSize) return [];

    // Build target frequency map
    final Map<String, int> target = {};
    for (var w in words) {
      target[w] = (target[w] ?? 0) + 1;
    }

    final List<int> result = [];

    // Iterate over each possible offset within word length
    for (int offset = 0; offset < wordLen; offset++) {
      int left = offset;
      int count = 0;
      final Map<String, int> window = {};

      for (int j = offset; j + wordLen <= s.length; j += wordLen) {
        String curWord = s.substring(j, j + wordLen);

        if (!target.containsKey(curWord)) {
          // Reset the window
          window.clear();
          count = 0;
          left = j + wordLen;
          continue;
        }

        // Add current word to window
        window[curWord] = (window[curWord] ?? 0) + 1;
        count++;

        // If there are more occurrences than needed, shrink from left
        while (window[curWord]! > target[curWord]!) {
          String leftWord = s.substring(left, left + wordLen);
          window[leftWord] = window[leftWord]! - 1;
          count--;
          left += wordLen;
        }

        // When we have a valid concatenation
        if (count == totalWords) {
          result.add(left);

          // Move left forward to look for next possible window
          String leftWord = s.substring(left, left + wordLen);
          window[leftWord] = window[leftWord]! - 1;
          count--;
          left += wordLen;
        }
      }
    }

    return result;
  }
}
```

## Golang

```go
func findSubstring(s string, words []string) []int {
	if len(words) == 0 || len(s) == 0 {
		return []int{}
	}
	wordLen := len(words[0])
	numWords := len(words)
	totalLen := wordLen * numWords
	if totalLen > len(s) {
		return []int{}
	}

	need := make(map[string]int, numWords)
	for _, w := range words {
		need[w]++
	}

	var res []int
	for offset := 0; offset < wordLen; offset++ {
		left := offset
		count := 0
		cur := make(map[string]int)

		for j := offset; j+wordLen <= len(s); j += wordLen {
			w := s[j : j+wordLen]
			if _, ok := need[w]; !ok {
				cur = make(map[string]int)
				count = 0
				left = j + wordLen
				continue
			}
			cur[w]++
			count++

			for cur[w] > need[w] {
				lw := s[left : left+wordLen]
				cur[lw]--
				count--
				left += wordLen
			}

			if count == numWords {
				res = append(res, left)
				lw := s[left : left+wordLen]
				cur[lw]--
				count--
				left += wordLen
			}
		}
	}
	return res
}
```

## Ruby

```ruby
def find_substring(s, words)
  return [] if s.empty? || words.empty?
  word_len = words[0].length
  num_words = words.length
  total_len = word_len * num_words
  return [] if s.length < total_len

  target = Hash.new(0)
  words.each { |w| target[w] += 1 }

  result = []

  (0...word_len).each do |i|
    left = i
    count = 0
    cur = Hash.new(0)

    j = i
    while j + word_len <= s.length
      w = s[j, word_len]
      if target.key?(w)
        cur[w] += 1
        count += 1

        while cur[w] > target[w]
          left_word = s[left, word_len]
          cur[left_word] -= 1
          left += word_len
          count -= 1
        end

        if count == num_words
          result << left
          left_word = s[left, word_len]
          cur[left_word] -= 1
          left += word_len
          count -= 1
        end
      else
        cur.clear
        count = 0
        left = j + word_len
      end

      j += word_len
    end
  end

  result
end
```

## Scala

```scala
object Solution {
  def findSubstring(s: String, words: Array[String]): List[Int] = {
    if (words.isEmpty) return Nil
    val wordLen = words(0).length
    val numWords = words.length
    val totalLen = wordLen * numWords
    if (s.length < totalLen) return Nil

    val target = scala.collection.mutable.Map[String, Int]()
    for (w <- words) {
      target(w) = target.getOrElse(w, 0) + 1
    }

    import scala.collection.mutable.{Map => MutableMap, ListBuffer}
    val result = ListBuffer[Int]()

    for (offset <- 0 until wordLen) {
      var left = offset
      var matched = 0
      val windowCount = MutableMap[String, Int]()
      var j = offset
      while (j <= s.length - wordLen) {
        val sub = s.substring(j, j + wordLen)
        if (target.contains(sub)) {
          windowCount(sub) = windowCount.getOrElse(sub, 0) + 1
          if (windowCount(sub) <= target(sub)) {
            matched += 1
          } else {
            while (windowCount(sub) > target(sub)) {
              val leftWord = s.substring(left, left + wordLen)
              windowCount(leftWord) = windowCount(leftWord) - 1
              if (windowCount(leftWord) < target.getOrElse(leftWord, 0)) matched -= 1
              left += wordLen
            }
          }

          if (matched == numWords) {
            result += left
            val leftWord = s.substring(left, left + wordLen)
            windowCount(leftWord) = windowCount(leftWord) - 1
            matched -= 1
            left += wordLen
          }
        } else {
          windowCount.clear()
          matched = 0
          left = j + wordLen
        }
        j += wordLen
      }
    }

    result.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn find_substring(s: String, words: Vec<String>) -> Vec<i32> {
        use std::collections::HashMap;
        let n = s.len();
        if words.is_empty() {
            return vec![];
        }
        let word_len = words[0].len();
        let m = words.len();
        let total_len = word_len * m;
        if total_len > n {
            return vec![];
        }

        // frequency map of required words
        let mut need: HashMap<String, i32> = HashMap::new();
        for w in &words {
            *need.entry(w.clone()).or_insert(0) += 1;
        }

        let mut result: Vec<i32> = Vec::new();

        // slide over each possible offset modulo word_len
        for offset in 0..word_len {
            let mut left = offset;
            let mut count = 0usize;
            let mut cur: HashMap<String, i32> = HashMap::new();
            let mut j = offset;

            while j + word_len <= n {
                let sub = &s[j..j + word_len];
                if need.contains_key(sub) {
                    // add current word
                    *cur.entry(sub.to_string()).or_insert(0) += 1;
                    count += 1;

                    // shrink window if this word appears too many times
                    while let Some(&need_cnt) = need.get(sub) {
                        let cur_cnt = *cur.get(sub).unwrap_or(&0);
                        if cur_cnt > need_cnt {
                            let left_word = &s[left..left + word_len];
                            if let Some(v) = cur.get_mut(left_word) {
                                *v -= 1;
                            }
                            left += word_len;
                            count -= 1;
                        } else {
                            break;
                        }
                    }

                    // when we have a valid window
                    if count == m {
                        result.push(left as i32);
                        // move left forward to look for next possible window
                        let left_word = &s[left..left + word_len];
                        if let Some(v) = cur.get_mut(left_word) {
                            *v -= 1;
                        }
                        left += word_len;
                        count -= 1;
                    }
                } else {
                    // reset window
                    cur.clear();
                    count = 0;
                    left = j + word_len;
                }

                j += word_len;
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (find-substring s words)
  (-> string? (listof string?) (listof exact-integer?))
  (let* ((word_len (if (null? words) 0 (string-length (car words))))
         (num_words (length words))
         (total_len (* word_len num_words)))
    (if (or (= word_len 0) (> total_len (string-length s)))
        '()
        (let ((need (make-hash)))
          (for ([w words])
            (hash-set! need w (+ (hash-ref need w 0) 1)))
          (define result '())
          (let loop-offset ((offset 0))
            (when (< offset word_len)
              (let* ((left offset)
                     (count 0)
                     (cur (make-hash)))
                (let loop-j ((j offset))
                  (when (<= (+ j word_len) (string-length s))
                    (define sub (substring s j (+ j word_len)))
                    (if (hash-has-key? need sub)
                        (begin
                          (hash-set! cur sub (+ (hash-ref cur sub 0) 1))
                          (set! count (+ count 1))
                          (let shrink ((sub sub))
                            (when (> (hash-ref cur sub 0) (hash-ref need sub 0))
                              (define left-word (substring s left (+ left word_len)))
                              (hash-set! cur left-word (- (hash-ref cur left-word) 1))
                              (set! count (- count 1))
                              (set! left (+ left word_len))
                              (shrink sub))))
                          (when (= count num_words)
                            (set! result (cons left result))
                            (define left-word (substring s left (+ left word_len)))
                            (hash-set! cur left-word (- (hash-ref cur left-word) 1))
                            (set! count (- count 1))
                            (set! left (+ left word_len))))
                        (begin
                          (set! cur (make-hash))
                          (set! count 0)
                          (set! left (+ j word_len)))))
                    (loop-j (+ j word_len)))))
              (loop-offset (+ offset 1)))
          (reverse result))))))
```

## Erlang

```erlang
-module(solution).
-export([find_substring/2]).

-spec find_substring(S :: unicode:unicode_binary(), Words :: [unicode:unicode_binary()]) -> [integer()].
find_substring(S, Words) ->
    case Words of
        [] -> [];
        _ ->
            WordLen = byte_size(hd(Words)),
            NumWords = length(Words),
            TotalLen = WordLen * NumWords,
            Slen = byte_size(S),
            if Slen < TotalLen ->
                    [];
               true ->
                    TargetMap = build_map(Words, #{}),
                    Offsets = lists:seq(0, WordLen - 1),
                    Indices = lists:foldl(fun(Off, Acc) ->
                        slide_window(Off, S, Slen, WordLen, NumWords, TargetMap) ++ Acc
                    end, [], Offsets),
                    lists:sort(Indices)
            end
    end.

build_map([], Map) -> Map;
build_map([W|Rest], Map) ->
    Count = maps:get(W, Map, 0),
    build_map(Rest, maps:put(W, Count + 1, Map)).

slide_window(Offset, S, Slen, WordLen, NumWords, TargetMap) ->
    slide(Offset, Offset, S, Slen, WordLen, NumWords, TargetMap, #{}, 0).

slide(Left, Right, S, Slen, WordLen, NumWords, TargetMap, CurMap, Matched) ->
    if Right + WordLen =< Slen ->
            Word = binary:part(S, Right, WordLen),
            case maps:is_key(Word, TargetMap) of
                true ->
                    Count = maps:get(Word, CurMap, 0) + 1,
                    NewCurMap = maps:put(Word, Count, CurMap),
                    NewMatched = Matched + 1,
                    {FinalLeft, FinalCurMap, FinalMatched} =
                        case Count > maps:get(Word, TargetMap) of
                            true ->
                                shrink_left(Left, WordLen, S, TargetMap, NewCurMap, NewMatched, Word);
                            false ->
                                {Left, NewCurMap, NewMatched}
                        end,
                    Rest = slide(FinalLeft, Right + WordLen, S, Slen, WordLen, NumWords, TargetMap, FinalCurMap, FinalMatched),
                    if FinalMatched == NumWords -> [FinalLeft | Rest]; true -> Rest end;
                false ->
                    slide(Right + WordLen, Right + WordLen, S, Slen, WordLen, NumWords, TargetMap, #{}, 0)
            end;
       true -> []
    end.

shrink_left(Left, WordLen, S, TargetMap, CurMap, Matched, ExceedWord) ->
    case maps:get(ExceedWord, CurMap) =< maps:get(ExceedWord, TargetMap) of
        true -> {Left, CurMap, Matched};
        false ->
            LeftWord = binary:part(S, Left, WordLen),
            CountL = maps:get(LeftWord, CurMap),
            NewCountL = CountL - 1,
            NewCurMap = if NewCountL == 0 -> maps:remove(LeftWord, CurMap); true -> maps:put(LeftWord, NewCountL, CurMap) end,
            NewMatched = Matched - 1,
            shrink_left(Left + WordLen, WordLen, S, TargetMap, NewCurMap, NewMatched, ExceedWord)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_substring(s :: String.t(), words :: [String.t()]) :: [integer]
  def find_substring(s, words) do
    wlen = String.length(List.first(words))
    n_words = length(words)
    total_len = wlen * n_words
    s_len = String.length(s)

    if s_len < total_len do
      []
    else
      target_counts =
        Enum.reduce(words, %{}, fn w, acc -> Map.update(acc, w, 1, &(&1 + 1)) end)

      results =
        Enum.reduce(0..(wlen - 1), [], fn offset, acc ->
          indices = slide_offset(s, s_len, wlen, n_words, target_counts, offset)
          acc ++ indices
        end)

      Enum.sort(results)
    end
  end

  defp slide_offset(s, s_len, wlen, n_words, target_counts, offset) do
    positions = for i <- offset..(s_len - wlen)//wlen, do: i

    {_, _, _, res} =
      Enum.reduce(positions, {offset, %{}, 0, []}, fn i,
                                                    {left, cur_counts, cnt, acc} ->
        sub = String.slice(s, i, wlen)

        if Map.has_key?(target_counts, sub) do
          # add current word
          cur_counts1 = Map.update(cur_counts, sub, 1, &(&1 + 1))
          cnt_temp = cnt + 1

          {new_left, new_counts, cnt2} =
            if cur_counts1[sub] > target_counts[sub] do
              {adj_left, adj_counts} =
                adjust_left(s, wlen, target_counts, cur_counts1, left, sub)

              removed = div(adj_left - left, wlen)
              {adj_left, adj_counts, cnt_temp - removed}
            else
              {left, cur_counts1, cnt_temp}
            end

          if cnt2 == n_words do
            # record start index
            acc = [new_left | acc]

            # slide window forward by one word
            left_word = String.slice(s, new_left, wlen)
            updated_counts = Map.update!(new_counts, left_word, &(&1 - 1))
            {new_left + wlen, updated_counts, cnt2 - 1, acc}
          else
            {new_left, new_counts, cnt2, acc}
          end
        else
          # reset window
          {i + wlen, %{}, 0, acc}
        end
      end)

    Enum.reverse(res)
  end

  defp adjust_left(s, wlen, target_counts, cur_counts, left, over_word) do
    if Map.get(cur_counts, over_word, 0) <= Map.get(target_counts, over_word, 0) do
      {left, cur_counts}
    else
      left_word = String.slice(s, left, wlen)
      new_counts = Map.update!(cur_counts, left_word, &(&1 - 1))
      adjust_left(s, wlen, target_counts, new_counts, left + wlen, over_word)
    end
  end
end
```
