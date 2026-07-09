# 0336. Palindrome Pairs

## Cpp

```cpp
class Solution {
public:
    bool isPalindrome(const string& s, int l, int r) { // [l, r)
        while (l < r) {
            if (s[l++] != s[--r]) return false;
        }
        return true;
    }

    vector<vector<int>> palindromePairs(vector<string>& words) {
        unordered_map<string,int> idx;
        for (int i = 0; i < (int)words.size(); ++i) idx[words[i]] = i;

        vector<vector<int>> ans;
        for (int i = 0; i < (int)words.size(); ++i) {
            const string& w = words[i];
            int n = w.size();
            for (int cut = 0; cut <= n; ++cut) {
                // left = w[0,cut), right = w[cut,n)
                if (isPalindrome(w, 0, cut)) {
                    string revRight = w.substr(cut);
                    reverse(revRight.begin(), revRight.end());
                    auto it = idx.find(revRight);
                    if (it != idx.end() && it->second != i) {
                        ans.push_back({it->second, i});
                    }
                }
                if (cut != n && isPalindrome(w, cut, n)) { // right non‑empty
                    string revLeft = w.substr(0, cut);
                    reverse(revLeft.begin(), revLeft.end());
                    auto it = idx.find(revLeft);
                    if (it != idx.end() && it->second != i) {
                        ans.push_back({i, it->second});
                    }
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        Map<String, Integer> dict = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            dict.put(words[i], i);
        }
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            int len = word.length();
            for (int cut = 0; cut <= len; cut++) {
                String left = word.substring(0, cut);
                String right = word.substring(cut);
                
                if (isPalindrome(left)) {
                    String revRight = new StringBuilder(right).reverse().toString();
                    Integer j = dict.get(revRight);
                    if (j != null && j != i) {
                        res.add(Arrays.asList(j, i));
                    }
                }
                
                // avoid duplicates when right is empty
                if (right.length() > 0 && isPalindrome(right)) {
                    String revLeft = new StringBuilder(left).reverse().toString();
                    Integer j = dict.get(revLeft);
                    if (j != null && j != i) {
                        res.add(Arrays.asList(i, j));
                    }
                }
            }
        }
        return res;
    }
    
    private boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l++) != s.charAt(r--)) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        lookup = {w: i for i, w in enumerate(words)}
        res = []
        
        def is_pal(s):
            return s == s[::-1]
        
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                left = word[:j]
                right = word[j:]
                
                # If left part is palindrome, need a reversed right to put in front
                if is_pal(left):
                    rev_right = right[::-1]
                    idx = lookup.get(rev_right)
                    if idx is not None and idx != i:
                        res.append([idx, i])
                
                # If right part is palindrome, need a reversed left to put after
                # j != n avoids duplicates when right is empty (handled by left case)
                if j != n and is_pal(right):
                    rev_left = left[::-1]
                    idx = lookup.get(rev_left)
                    if idx is not None and idx != i:
                        res.append([i, idx])
        return res
```

## Python3

```python
class Solution:
    def palindromePairs(self, words):
        from collections import defaultdict
        word_index = {w: i for i, w in enumerate(words)}
        res = []
        def is_pal(s):
            return s == s[::-1]
        empty_idx = word_index.get("")
        if empty_idx is not None:
            for i, w in enumerate(words):
                if i != empty_idx and is_pal(w):
                    res.append([i, empty_idx])
                    res.append([empty_idx, i])
        for i, w in enumerate(words):
            n = len(w)
            for cut in range(n + 1):
                left, right = w[:cut], w[cut:]
                if is_pal(left):
                    rev = right[::-1]
                    j = word_index.get(rev)
                    if j is not None and j != i:
                        res.append([j, i])
                if cut != n and is_pal(right):
                    rev = left[::-1]
                    j = word_index.get(rev)
                    if j is not None and j != i:
                        res.append([i, j])
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    const char *key;
    int idx;
    struct Node *next;
} Node;

#define HASH_SIZE 20011

static unsigned int hash_func(const char *s) {
    unsigned long h = 5381;
    while (*s) {
        h = ((h << 5) + h) + (unsigned char)(*s);
        s++;
    }
    return (unsigned int)(h % HASH_SIZE);
}

static void hashmap_insert(Node **table, const char *key, int idx) {
    unsigned int h = hash_func(key);
    Node *node = (Node *)malloc(sizeof(Node));
    node->key = key;
    node->idx = idx;
    node->next = table[h];
    table[h] = node;
}

static int hashmap_find(Node **table, const char *key) {
    unsigned int h = hash_func(key);
    Node *cur = table[h];
    while (cur) {
        if (strcmp(cur->key, key) == 0)
            return cur->idx;
        cur = cur->next;
    }
    return -1;
}

static int is_palindrome(const char *s, int l, int r) {
    while (l < r) {
        if (s[l] != s[r]) return 0;
        ++l; --r;
    }
    return 1;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** palindromePairs(char** words, int wordsSize, int* returnSize, int*** returnColumnSizes) {
    Node **table = (Node **)calloc(HASH_SIZE, sizeof(Node *));
    for (int i = 0; i < wordsSize; ++i) {
        hashmap_insert(table, words[i], i);
    }

    int capacity = 256;
    int **res = (int **)malloc(capacity * sizeof(int *));
    int *colSizes = (int *)malloc(capacity * sizeof(int));
    int count = 0;

    char rev[302];

    for (int i = 0; i < wordsSize; ++i) {
        const char *w = words[i];
        int len = (int)strlen(w);
        for (int j = 0; j <= len; ++j) {
            // left part [0, j)
            if (is_palindrome(w, 0, j - 1)) {
                int rightLen = len - j;
                for (int k = 0; k < rightLen; ++k) {
                    rev[k] = w[len - 1 - k];
                }
                rev[rightLen] = '\0';
                int idx = hashmap_find(table, rev);
                if (idx != -1 && idx != i) {
                    if (count == capacity) {
                        capacity <<= 1;
                        res = (int **)realloc(res, capacity * sizeof(int *));
                        colSizes = (int *)realloc(colSizes, capacity * sizeof(int));
                    }
                    int *pair = (int *)malloc(2 * sizeof(int));
                    pair[0] = idx;
                    pair[1] = i;
                    res[count] = pair;
                    colSizes[count] = 2;
                    ++count;
                }
            }

            // right part [j, len)
            if (j != len && is_palindrome(w, j, len - 1)) {
                int leftLen = j;
                for (int k = 0; k < leftLen; ++k) {
                    rev[k] = w[j - 1 - k];
                }
                rev[leftLen] = '\0';
                int idx = hashmap_find(table, rev);
                if (idx != -1 && idx != i) {
                    if (count == capacity) {
                        capacity <<= 1;
                        res = (int **)realloc(res, capacity * sizeof(int *));
                        colSizes = (int *)realloc(colSizes, capacity * sizeof(int));
                    }
                    int *pair = (int *)malloc(2 * sizeof(int));
                    pair[0] = i;
                    pair[1] = idx;
                    res[count] = pair;
                    colSizes[count] = 2;
                    ++count;
                }
            }
        }
    }

    // free hashmap
    for (int h = 0; h < HASH_SIZE; ++h) {
        Node *cur = table[h];
        while (cur) {
            Node *tmp = cur;
            cur = cur->next;
            free(tmp);
        }
    }
    free(table);

    *returnSize = count;
    *returnColumnSizes = &colSizes;
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> PalindromePairs(string[] words) {
        var result = new List<IList<int>>();
        var dict = new Dictionary<string, int>();
        for (int i = 0; i < words.Length; i++) {
            dict[words[i]] = i;
        }

        for (int i = 0; i < words.Length; i++) {
            string word = words[i];
            int len = word.Length;
            for (int cut = 0; cut <= len; cut++) {
                string left = word.Substring(0, cut);
                string right = word.Substring(cut);

                // If left part is palindrome, we can attach reversed right in front
                if (IsPalindrome(left)) {
                    string revRight = Reverse(right);
                    if (dict.TryGetValue(revRight, out int j) && j != i) {
                        result.Add(new List<int> { j, i });
                    }
                }

                // If right part is palindrome and not empty, we can attach reversed left at the end
                if (right.Length > 0 && IsPalindrome(right)) {
                    string revLeft = Reverse(left);
                    if (dict.TryGetValue(revLeft, out int j) && j != i) {
                        result.Add(new List<int> { i, j });
                    }
                }
            }
        }

        return result;
    }

    private bool IsPalindrome(string s) {
        int l = 0, r = s.Length - 1;
        while (l < r) {
            if (s[l] != s[r]) return false;
            l++;
            r--;
        }
        return true;
    }

    private string Reverse(string s) {
        char[] arr = s.ToCharArray();
        Array.Reverse(arr);
        return new string(arr);
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number[][]}
 */
var palindromePairs = function(words) {
    const map = new Map();
    for (let i = 0; i < words.length; i++) {
        map.set(words[i], i);
    }
    
    const isPal = (s, l, r) => {
        while (l < r) {
            if (s[l] !== s[r]) return false;
            l++; r--;
        }
        return true;
    };
    
    const res = [];
    
    for (let i = 0; i < words.length; i++) {
        const w = words[i];
        const len = w.length;
        for (let cut = 0; cut <= len; cut++) {
            // prefix [0,cut), suffix [cut,len)
            // if prefix is palindrome, need reversed suffix in map
            if (isPal(w, 0, cut - 1)) {
                const revSuffix = w.slice(cut).split('').reverse().join('');
                if (map.has(revSuffix) && map.get(revSuffix) !== i) {
                    res.push([map.get(revSuffix), i]);
                }
            }
            // if suffix is palindrome, need reversed prefix in map
            // cut != len to avoid duplicates when both parts are empty
            if (cut !== len && isPal(w, cut, len - 1)) {
                const revPrefix = w.slice(0, cut).split('').reverse().join('');
                if (map.has(revPrefix) && map.get(revPrefix) !== i) {
                    res.push([i, map.get(revPrefix)]);
                }
            }
        }
    }
    
    return res;
};
```

## Typescript

```typescript
function palindromePairs(words: string[]): number[][] {
    const wordIndex = new Map<string, number>();
    for (let i = 0; i < words.length; i++) {
        wordIndex.set(words[i], i);
    }

    const isPalindrome = (s: string): boolean => {
        let l = 0, r = s.length - 1;
        while (l < r) {
            if (s.charAt(l) !== s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    };

    const reverse = (s: string): string => s.split('').reverse().join('');

    const result: number[][] = [];
    const seen = new Set<string>();

    for (let i = 0; i < words.length; i++) {
        const word = words[i];
        const len = word.length;
        for (let cut = 0; cut <= len; cut++) {
            const left = word.substring(0, cut);
            const right = word.substring(cut);

            // If left part is palindrome, need reversed right to prepend
            if (isPalindrome(left)) {
                const revRight = reverse(right);
                const j = wordIndex.get(revRight);
                if (j !== undefined && j !== i) {
                    const key = `${j}#${i}`;
                    if (!seen.has(key)) {
                        seen.add(key);
                        result.push([j, i]);
                    }
                }
            }

            // If right part is palindrome, need reversed left to append
            // cut != len avoids duplicate when both parts are empty
            if (cut !== len && isPalindrome(right)) {
                const revLeft = reverse(left);
                const j = wordIndex.get(revLeft);
                if (j !== undefined && j !== i) {
                    const key = `${i}#${j}`;
                    if (!seen.has(key)) {
                        seen.add(key);
                        result.push([i, j]);
                    }
                }
            }
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer[][]
     */
    function palindromePairs($words) {
        $wordIndex = [];
        foreach ($words as $i => $w) {
            $wordIndex[$w] = $i;
        }
        $res = [];

        foreach ($words as $i => $w) {
            $len = strlen($w);
            for ($cut = 0; $cut <= $len; $cut++) {
                $left = substr($w, 0, $cut);
                $right = substr($w, $cut);

                if ($this->isPal($left)) {
                    $revRight = strrev($right);
                    if (isset($wordIndex[$revRight]) && $wordIndex[$revRight] != $i) {
                        $res[] = [$wordIndex[$revRight], $i];
                    }
                }

                // avoid duplicate when right part is empty
                if ($cut != $len && $this->isPal($right)) {
                    $revLeft = strrev($left);
                    if (isset($wordIndex[$revLeft]) && $wordIndex[$revLeft] != $i) {
                        $res[] = [$i, $wordIndex[$revLeft]];
                    }
                }
            }
        }

        return $res;
    }

    private function isPal(string $s): bool {
        return $s === strrev($s);
    }
}
```

## Swift

```swift
class Solution {
    func palindromePairs(_ words: [String]) -> [[Int]] {
        var wordIndex = [String:Int]()
        for (i, w) in words.enumerated() {
            wordIndex[w] = i
        }
        
        var results = [[Int]]()
        // handle empty string case separately
        if let emptyIdx = wordIndex[""] {
            for (i, w) in words.enumerated() where i != emptyIdx && isPalindrome(w) {
                results.append([emptyIdx, i])
                results.append([i, emptyIdx])
            }
        }
        
        for (i, w) in words.enumerated() {
            let chars = Array(w)
            let len = chars.count
            if len == 0 { continue }
            
            for cut in 0...len {
                // left part [0, cut)
                var leftIsPal = true
                if cut > 0 {
                    leftIsPal = isPalindrome(chars, 0, cut - 1)
                }
                if leftIsPal {
                    let rightPart = String(chars[cut..<len])
                    let revRight = String(rightPart.reversed())
                    if let j = wordIndex[revRight], j != i {
                        results.append([j, i])
                    }
                }
                
                // right part [cut, len)
                if cut < len { // avoid duplicate when cut == len
                    var rightIsPal = isPalindrome(chars, cut, len - 1)
                    if rightIsPal {
                        let leftPart = String(chars[0..<cut])
                        let revLeft = String(leftPart.reversed())
                        if let j = wordIndex[revLeft], j != i {
                            results.append([i, j])
                        }
                    }
                }
            }
        }
        
        var seen = Set<String>()
        var unique = [[Int]]()
        for pair in results {
            let key = "\(pair[0])#\(pair[1])"
            if !seen.contains(key) {
                seen.insert(key)
                unique.append(pair)
            }
        }
        return unique
    }
    
    private func isPalindrome(_ s: String) -> Bool {
        let arr = Array(s)
        var l = 0, r = arr.count - 1
        while l < r {
            if arr[l] != arr[r] { return false }
            l += 1; r -= 1
        }
        return true
    }
    
    private func isPalindrome(_ chars: [Character], _ left: Int, _ right: Int) -> Bool {
        var i = left, j = right
        while i < j {
            if chars[i] != chars[j] { return false }
            i += 1; j -= 1
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun palindromePairs(words: Array<String>): List<List<Int>> {
        val indexMap = HashMap<String, Int>()
        for (i in words.indices) {
            indexMap[words[i]] = i
        }
        val result = mutableListOf<List<Int>>()
        val seen = HashSet<Pair<Int, Int>>()

        fun isPalindrome(s: String): Boolean {
            var l = 0
            var r = s.length - 1
            while (l < r) {
                if (s[l] != s[r]) return false
                l++
                r--
            }
            return true
        }

        for (i in words.indices) {
            val w = words[i]
            val len = w.length
            for (cut in 0..len) {
                val left = w.substring(0, cut)
                val right = w.substring(cut)

                if (isPalindrome(left)) {
                    val revRight = right.reversed()
                    val j = indexMap[revRight]
                    if (j != null && j != i) {
                        val pair = Pair(j, i)
                        if (seen.add(pair)) {
                            result.add(listOf(j, i))
                        }
                    }
                }

                if (right.isNotEmpty() && isPalindrome(right)) {
                    val revLeft = left.reversed()
                    val j = indexMap[revLeft]
                    if (j != null && j != i) {
                        val pair = Pair(i, j)
                        if (seen.add(pair)) {
                            result.add(listOf(i, j))
                        }
                    }
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
  List<List<int>> palindromePairs(List<String> words) {
    Map<String, int> dict = {};
    for (int i = 0; i < words.length; i++) {
      dict[words[i]] = i;
    }

    bool isPalindrome(String s) {
      int l = 0, r = s.length - 1;
      while (l < r) {
        if (s.codeUnitAt(l) != s.codeUnitAt(r)) return false;
        l++;
        r--;
      }
      return true;
    }

    String reverse(String s) => s.split('').reversed.join();

    List<List<int>> res = [];

    for (int i = 0; i < words.length; i++) {
      String word = words[i];
      int len = word.length;
      for (int j = 0; j <= len; j++) {
        String left = word.substring(0, j);
        String right = word.substring(j);

        if (isPalindrome(left)) {
          String revRight = reverse(right);
          int? idx = dict[revRight];
          if (idx != null && idx != i) {
            res.add([idx, i]);
          }
        }

        if (right.isNotEmpty && isPalindrome(right)) {
          String revLeft = reverse(left);
          int? idx = dict[revLeft];
          if (idx != null && idx != i) {
            res.add([i, idx]);
          }
        }
      }
    }

    return res;
  }
}
```

## Golang

```go
func palindromePairs(words []string) [][]int {
	type void struct{}
	_ = void{}
	
	// map word to its index
	wordIdx := make(map[string]int, len(words))
	for i, w := range words {
		wordIdx[w] = i
	}
	
	isPal := func(s string) bool {
		i, j := 0, len(s)-1
		for i < j {
			if s[i] != s[j] {
				return false
			}
			i++
			j--
		}
		return true
	}
	
	reverse := func(s string) string {
		b := []byte(s)
		n := len(b)
		for i := 0; i < n/2; i++ {
			b[i], b[n-1-i] = b[n-1-i], b[i]
		}
		return string(b)
	}
	
	var res [][]int
	for i, w := range words {
		n := len(w)
		for cut := 0; cut <= n; cut++ {
			left := w[:cut]
			right := w[cut:]
			
			if isPal(left) {
				revRight := reverse(right)
				if j, ok := wordIdx[revRight]; ok && j != i {
					res = append(res, []int{j, i})
				}
			}
			
			// avoid duplicate when right is empty (cut == n)
			if len(right) > 0 && isPal(right) {
				revLeft := reverse(left)
				if j, ok := wordIdx[revLeft]; ok && j != i {
					res = append(res, []int{i, j})
				}
			}
		}
	}
	return res
}
```

## Ruby

```ruby
def palindrome_pairs(words)
  # map word to its index
  idx_map = {}
  words.each_with_index { |w, i| idx_map[w] = i }

  # helper to check palindrome
  def is_pal?(s)
    s == s.reverse
  end

  result = []
  seen = Set.new

  add_pair = lambda do |a, b|
    pair = [a, b]
    unless seen.include?(pair)
      seen.add(pair)
      result << pair
    end
  end

  # handle empty string cases separately
  empty_idx = idx_map[""]
  if empty_idx
    words.each_with_index do |w, i|
      next if w.empty?
      add_pair.call(empty_idx, i) if is_pal?(w)
      add_pair.call(i, empty_idx) if is_pal?(w)
    end
  end

  words.each_with_index do |word, i|
    n = word.length
    (0..n).each do |cut|
      left = word[0...cut]
      right = cut == n ? "" : word[cut..-1]

      # if left part is palindrome, need reversed right as prefix
      if is_pal?(left)
        rev = right.reverse
        j = idx_map[rev]
        if j && j != i
          add_pair.call(j, i)
        end
      end

      # if right part is palindrome and not empty, need reversed left as suffix
      if cut != n && is_pal?(right)
        rev = left.reverse
        j = idx_map[rev]
        if j && j != i
          add_pair.call(i, j)
        end
      end
    end
  end

  result
end
```

## Scala

```scala
object Solution {
  def palindromePairs(words: Array[String]): List[List[Int]] = {
    val wordMap = words.zipWithIndex.toMap
    val result = scala.collection.mutable.ListBuffer[List[Int]]()
    for ((word, i) <- words.zipWithIndex) {
      val len = word.length
      for (cut <- 0 to len) {
        val left = word.substring(0, cut)
        val right = word.substring(cut)
        if (isPalindrome(left)) {
          val revRight = right.reverse
          wordMap.get(revRight).foreach { j =>
            if (j != i) result += List(j, i)
          }
        }
        if (right.nonEmpty && isPalindrome(right)) {
          val revLeft = left.reverse
          wordMap.get(revLeft).foreach { j =>
            if (j != i) result += List(i, j)
          }
        }
      }
    }
    result.toList
  }

  private def isPalindrome(s: String): Boolean = {
    var l = 0
    var r = s.length - 1
    while (l < r) {
      if (s.charAt(l) != s.charAt(r)) return false
      l += 1
      r -= 1
    }
    true
  }
}
```

## Rust

```rust
use std::collections::HashMap;

fn is_palindrome(s: &[u8]) -> bool {
    let mut l = 0;
    let mut r = s.len();
    while l < r {
        if s[l] != s[r - 1] {
            return false;
        }
        l += 1;
        r -= 1;
    }
    true
}

fn reverse_slice(s: &[u8]) -> String {
    s.iter().rev().map(|&c| c as char).collect()
}

impl Solution {
    pub fn palindrome_pairs(words: Vec<String>) -> Vec<Vec<i32>> {
        let mut map: HashMap<String, usize> = HashMap::new();
        for (i, w) in words.iter().enumerate() {
            map.insert(w.clone(), i);
        }

        let mut res: Vec<Vec<i32>> = Vec::new();

        for (i, w) in words.iter().enumerate() {
            let bytes = w.as_bytes();
            let len = bytes.len();
            for j in 0..=len {
                // left part [0, j), right part [j, len)
                if is_palindrome(&bytes[0..j]) {
                    let rev_right = reverse_slice(&bytes[j..len]);
                    if let Some(&idx) = map.get(&rev_right) {
                        if idx != i {
                            res.push(vec![idx as i32, i as i32]);
                        }
                    }
                }

                // avoid duplicate when j == len (right empty already handled)
                if j != len && is_palindrome(&bytes[j..len]) {
                    let rev_left = reverse_slice(&bytes[0..j]);
                    if let Some(&idx) = map.get(&rev_left) {
                        if idx != i {
                            res.push(vec![i as i32, idx as i32]);
                        }
                    }
                }
            }
        }

        res
    }
}
```

## Racket

```racket
#lang racket
(require racket/string)

(define (palindrome? s)
  (let loop ((l 0) (r (- (string-length s) 1)))
    (or (>= l r)
        (and (char=? (string-ref s l) (string-ref s r))
             (loop (+ l 1) (- r 1))))))

(define/contract (palindrome-pairs words)
  (-> (listof string?) (listof (listof exact-integer?)))
  (let* ((word->idx (make-hash))
         (n (length words)))
    ;; map each word to its index
    (for ([w words] [i (in-naturals)])
      (hash-set! word->idx w i))
    (define result '())
    (define seen (make-hash)) ; to avoid duplicates
    (for ([w words] [i (in-naturals)])
      (let ((len (string-length w)))
        (for ([j (in-range (+ len 1))])
          (define prefix (substring w 0 j))
          (define suffix (substring w j len))
          ;; case 1: prefix is palindrome, need reversed suffix before it
          (when (palindrome? prefix)
            (let* ((rev-suffix (string-reverse suffix))
                   (idx (and (hash-has-key? word->idx rev-suffix)
                             (hash-ref word->idx rev-suffix))))
              (when (and idx (not (= i idx)))
                (define key (cons idx i))
                (unless (hash-has-key? seen key)
                  (hash-set! seen key #t)
                  (set! result (cons (list idx i) result))))))
          ;; case 2: suffix is palindrome and not empty, need reversed prefix after it
          (when (and (< j len) (palindrome? suffix))
            (let* ((rev-prefix (string-reverse prefix))
                   (idx (and (hash-has-key? word->idx rev-prefix)
                             (hash-ref word->idx rev-prefix))))
              (when (and idx (not (= i idx)))
                (define key (cons i idx))
                (unless (hash-has-key? seen key)
                  (hash-set! seen key #t)
                  (set! result (cons (list i idx) result))))))))))
    (reverse result)))
```

## Erlang

```erlang
-spec palindrome_pairs([unicode:unicode_binary()]) -> [[integer()]].
palindrome_pairs(Words) ->
    Indices = lists:seq(0, length(Words) - 1),
    WordIdxs = lists:zip(Words, Indices),
    Map = maps:from_list(lists:map(fun({W, I}) -> {W, I} end, WordIdxs)),

    % main pairs from splits
    Pairs = lists:foldl(
        fun({Word, Index}, Acc) ->
            Len = byte_size(Word),
            Splits = [ {binary:part(Word, 0, I), binary:part(Word, I, Len - I)} ||
                       I <- lists:seq(0, Len) ],
            lists:foldl(
                fun({Left, Right}, Acc2) ->
                    RevRight = rev_bin(Right),
                    RevLeft  = rev_bin(Left),

                    Acc3 = case (is_palindrome(Left) andalso maps:is_key(RevRight, Map)) of
                        true ->
                            J = maps:get(RevRight, Map),
                            if J =/= Index -> [[J, Index] | Acc2]; true -> Acc2 end;
                        false -> Acc2
                    end,

                    case (is_palindrome(Right) andalso maps:is_key(RevLeft, Map)) of
                        true ->
                            J = maps:get(RevLeft, Map),
                            if J =/= Index -> [[Index, J] | Acc3]; true -> Acc3 end;
                        false -> Acc3
                    end
                end,
                Acc,
                Splits)
        end,
        [],
        WordIdxs),

    % handle empty string cases
    EmptyPairs =
        case maps:find(<<>>, Map) of
            {ok, EmptyIdx} ->
                lists:foldl(
                    fun({Word, I}, AccE) ->
                        if Word =/= <<>> andalso is_palindrome(Word) ->
                                [[EmptyIdx, I], [I, EmptyIdx] | AccE];
                           true -> AccE
                        end
                    end,
                    [],
                    WordIdxs);
            error -> []
        end,

    lists:usort(Pairs ++ EmptyPairs).

rev_bin(Bin) ->
    list_to_binary(lists:reverse(binary_to_list(Bin))).

is_palindrome(Bin) ->
    Bin =:= rev_bin(Bin).
```

## Elixir

```elixir
defmodule Solution do
  @spec palindrome_pairs(words :: [String.t]) :: [[integer]]
  def palindrome_pairs(words) do
    # Map each word to its index for O(1) lookups
    idx_map = Enum.with_index(words) |> Enum.into(%{}, fn {w, i} -> {w, i} end)

    pairs_set =
      Enum.reduce(Enum.with_index(words), MapSet.new(), fn {word, i}, acc ->
        len = String.length(word)

        0..len
        |> Enum.reduce(acc, fn cut, set_acc ->
          left = :binary.part(word, 0, cut)
          right = :binary.part(word, cut, len - cut)

          set_acc =
            if palindrome?(left) do
              rev_right = String.reverse(right)

              case Map.get(idx_map, rev_right) do
                nil -> set_acc
                j when j != i -> MapSet.put(set_acc, {i, j})
                _ -> set_acc
              end
            else
              set_acc
            end

          # Avoid duplicate work when cut == len (right is empty)
          if cut != len and palindrome?(right) do
            rev_left = String.reverse(left)

            case Map.get(idx_map, rev_left) do
              nil -> set_acc
              j when j != i -> MapSet.put(set_acc, {j, i})
              _ -> set_acc
            end
          else
            set_acc
          end
        end)
      end)

    pairs_set
    |> Enum.map(fn {a, b} -> [a, b] end)
  end

  defp palindrome?(s) do
    s == String.reverse(s)
  end
end
```
