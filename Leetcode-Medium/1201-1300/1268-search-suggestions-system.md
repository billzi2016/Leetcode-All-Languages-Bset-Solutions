# 1268. Search Suggestions System

## Cpp

```cpp
class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(), products.end());
        vector<vector<string>> result;
        string prefix;
        for (char c : searchWord) {
            prefix.push_back(c);
            auto it = lower_bound(products.begin(), products.end(), prefix);
            vector<string> suggestions;
            for (int i = 0; i < 3 && it != products.end(); ++i, ++it) {
                if (it->compare(0, prefix.size(), prefix) == 0)
                    suggestions.push_back(*it);
                else
                    break;
            }
            result.push_back(move(suggestions));
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        Arrays.sort(products);
        List<List<String>> result = new ArrayList<>();
        int start = 0;
        int n = products.length;

        for (int i = 0; i < searchWord.length(); i++) {
            String prefix = searchWord.substring(0, i + 1);
            start = lowerBound(products, prefix, start);
            List<String> suggestions = new ArrayList<>();
            for (int j = start; j < Math.min(start + 3, n); j++) {
                if (products[j].startsWith(prefix)) {
                    suggestions.add(products[j]);
                } else {
                    break;
                }
            }
            result.add(suggestions);
        }

        return result;
    }

    private int lowerBound(String[] arr, String target, int lo) {
        int hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid].compareTo(target) < 0) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
```

## Python

```python
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        import bisect
        res = []
        prefix = ''
        start = 0
        for ch in searchWord:
            prefix += ch
            i = bisect.bisect_left(products, prefix, lo=start)
            suggestions = []
            for j in range(i, min(i + 3, len(products))):
                if products[j].startswith(prefix):
                    suggestions.append(products[j])
                else:
                    break
            res.append(suggestions)
            start = i
        return res
```

## Python3

```python
from typing import List
import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            start = bisect.bisect_left(products, prefix)
            suggestions = []
            for i in range(start, min(start + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
            result.append(suggestions)
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>

/* Helper to duplicate a string */
static char *myStrdup(const char *s) {
    size_t len = strlen(s);
    char *copy = (char *)malloc(len + 1);
    if (copy) memcpy(copy, s, len + 1);
    return copy;
}

/* Comparator for qsort: lexicographic order */
static int cmp_str(const void *a, const void *b) {
    const char *sa = *(const char **)a;
    const char *sb = *(const char **)b;
    return strcmp(sa, sb);
}

/* Lower bound: first index where arr[idx] >= prefix (considering only len characters) */
static int lower_bound(char **arr, int n, const char *prefix, int len) {
    int l = 0, r = n;
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (strncmp(arr[mid], prefix, len) < 0)
            l = mid + 1;
        else
            r = mid;
    }
    return l;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char ***suggestedProducts(char **products, int productsSize, char *searchWord,
                          int *returnSize, int **returnColumnSizes) {
    /* Sort products lexicographically */
    qsort(products, (size_t)productsSize, sizeof(char *), cmp_str);

    int m = (int)strlen(searchWord);
    *returnSize = m;
    *returnColumnSizes = (int *)malloc(m * sizeof(int));
    char ***result = (char ***)malloc(m * sizeof(char **));

    for (int i = 1; i <= m; ++i) {
        int start = lower_bound(products, productsSize, searchWord, i);
        int cnt = 0;
        result[i - 1] = (char **)malloc(3 * sizeof(char *));
        for (int j = start; j < productsSize && cnt < 3; ++j) {
            if (strncmp(products[j], searchWord, i) == 0) {
                result[i - 1][cnt++] = myStrdup(products[j]);
            } else {
                break;
            }
        }
        (*returnColumnSizes)[i - 1] = cnt;
    }

    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<string>> SuggestedProducts(string[] products, string searchWord) {
        Array.Sort(products, StringComparer.Ordinal);
        int n = products.Length;
        var result = new List<IList<string>>();
        
        for (int i = 1; i <= searchWord.Length; i++) {
            string prefix = searchWord.Substring(0, i);
            int lo = 0, hi = n;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (String.CompareOrdinal(products[mid], prefix) < 0)
                    lo = mid + 1;
                else
                    hi = mid;
            }
            
            var suggestions = new List<string>();
            for (int j = lo; j < Math.Min(lo + 3, n); j++) {
                if (products[j].StartsWith(prefix, StringComparison.Ordinal))
                    suggestions.Add(products[j]);
            }
            result.Add(suggestions);
        }
        
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} products
 * @param {string} searchWord
 * @return {string[][]}
 */
var suggestedProducts = function(products, searchWord) {
    products.sort();
    const result = [];
    let prefix = '';
    for (let i = 0; i < searchWord.length; ++i) {
        prefix += searchWord[i];
        const start = lowerBound(products, prefix);
        const suggestions = [];
        for (let j = start; j < Math.min(start + 3, products.length); ++j) {
            if (products[j].startsWith(prefix)) {
                suggestions.push(products[j]);
            } else {
                break;
            }
        }
        result.push(suggestions);
    }
    return result;
};

function lowerBound(arr, target) {
    let left = 0, right = arr.length;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}
```

## Typescript

```typescript
function suggestedProducts(products: string[], searchWord: string): string[][] {
    products.sort();
    const res: string[][] = [];
    let startIdx = 0;
    for (let i = 1; i <= searchWord.length; ++i) {
        const prefix = searchWord.slice(0, i);
        // binary search for the first index >= prefix
        let l = startIdx, r = products.length;
        while (l < r) {
            const m = Math.floor((l + r) / 2);
            if (products[m] < prefix) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        startIdx = l; // next searches can start from here
        const suggestions: string[] = [];
        for (let j = startIdx; j < Math.min(startIdx + 3, products.length); ++j) {
            if (products[j].startsWith(prefix)) {
                suggestions.push(products[j]);
            } else {
                break;
            }
        }
        res.push(suggestions);
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $products
     * @param String $searchWord
     * @return String[][]
     */
    function suggestedProducts($products, $searchWord) {
        sort($products, SORT_STRING);
        $n = count($products);
        $result = [];
        $prefix = '';
        $left = 0; // lower bound start for next iteration

        foreach (str_split($searchWord) as $ch) {
            $prefix .= $ch;
            $len = strlen($prefix);

            // binary search for first index >= prefix
            $l = $left;
            $r = $n;
            while ($l < $r) {
                $mid = intdiv($l + $r, 2);
                $sub = substr($products[$mid], 0, $len);
                if (strcmp($sub, $prefix) < 0) {
                    $l = $mid + 1;
                } else {
                    $r = $mid;
                }
            }

            $start = $l;
            $left = $start; // next search can start from here

            $suggestions = [];
            for ($i = $start; $i < $n && count($suggestions) < 3; $i++) {
                if (strpos($products[$i], $prefix) === 0) {
                    $suggestions[] = $products[$i];
                } else {
                    break;
                }
            }

            $result[] = $suggestions;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func suggestedProducts(_ products: [String], _ searchWord: String) -> [[String]] {
        let sorted = products.sorted()
        var answer: [[String]] = []
        let length = searchWord.count
        for i in 1...length {
            let prefix = String(searchWord.prefix(i))
            var suggestions: [String] = []
            var idx = lowerBound(sorted, prefix)
            while idx < sorted.count && suggestions.count < 3 {
                if sorted[idx].hasPrefix(prefix) {
                    suggestions.append(sorted[idx])
                } else {
                    break
                }
                idx += 1
            }
            answer.append(suggestions)
        }
        return answer
    }
    
    private func lowerBound(_ arr: [String], _ target: String) -> Int {
        var left = 0
        var right = arr.count
        while left < right {
            let mid = (left + right) / 2
            if arr[mid] < target {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun suggestedProducts(products: Array<String>, searchWord: String): List<List<String>> {
        val sorted = products.sorted()
        val n = sorted.size
        val result = mutableListOf<List<String>>()
        var prefix = ""
        for (ch in searchWord) {
            prefix += ch
            // lower bound binary search for the current prefix
            var left = 0
            var right = n
            while (left < right) {
                val mid = (left + right) ushr 1
                if (sorted[mid] < prefix) {
                    left = mid + 1
                } else {
                    right = mid
                }
            }
            val suggestions = mutableListOf<String>()
            var i = left
            while (i < n && suggestions.size < 3) {
                if (sorted[i].startsWith(prefix)) {
                    suggestions.add(sorted[i])
                } else {
                    break
                }
                i++
            }
            result.add(suggestions)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<List<String>> suggestedProducts(List<String> products, String searchWord) {
    products.sort();
    List<List<String>> result = [];
    for (int i = 1; i <= searchWord.length; ++i) {
      String prefix = searchWord.substring(0, i);
      int idx = _lowerBound(products, prefix);
      List<String> suggestions = [];
      for (int j = idx;
          j < products.length && suggestions.length < 3;
          ++j) {
        if (products[j].startsWith(prefix)) {
          suggestions.add(products[j]);
        } else {
          break;
        }
      }
      result.add(suggestions);
    }
    return result;
  }

  int _lowerBound(List<String> arr, String target) {
    int left = 0;
    int right = arr.length;
    while (left < right) {
      int mid = (left + right) >> 1;
      if (arr[mid].compareTo(target) < 0) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return left;
  }
}
```

## Golang

```go
package main

import (
	"sort"
	"strings"
)

func suggestedProducts(products []string, searchWord string) [][]string {
	sort.Strings(products)
	result := make([][]string, 0, len(searchWord))
	for i := 1; i <= len(searchWord); i++ {
		prefix := searchWord[:i]
		start := sort.Search(len(products), func(j int) bool { return products[j] >= prefix })
		suggestions := make([]string, 0, 3)
		for j := start; j < len(products) && len(suggestions) < 3; j++ {
			if strings.HasPrefix(products[j], prefix) {
				suggestions = append(suggestions, products[j])
			} else {
				break
			}
		}
		result = append(result, suggestions)
	}
	return result
}
```

## Ruby

```ruby
def lower_bound(arr, target)
  left = 0
  right = arr.length
  while left < right
    mid = (left + right) / 2
    if arr[mid] < target
      left = mid + 1
    else
      right = mid
    end
  end
  left
end

def suggested_products(products, search_word)
  products.sort!
  n = products.length
  result = []
  prefix = ''
  search_word.each_char do |ch|
    prefix << ch
    start_idx = lower_bound(products, prefix)
    suggestions = []
    i = start_idx
    while i < n && suggestions.size < 3
      break unless products[i].start_with?(prefix)
      suggestions << products[i]
      i += 1
    end
    result << suggestions
  end
  result
end
```

## Scala

```scala
object Solution {
  def suggestedProducts(products: Array[String], searchWord: String): List[List[String]] = {
    val sorted = products.sorted
    val n = sorted.length
    val result = scala.collection.mutable.ListBuffer[List[String]]()
    val prefixBuilder = new StringBuilder

    for (ch <- searchWord) {
      prefixBuilder.append(ch)
      val prefix = prefixBuilder.toString()

      // lower bound binary search
      var l = 0
      var r = n
      while (l < r) {
        val mid = (l + r) >>> 1
        if (sorted(mid) < prefix) l = mid + 1 else r = mid
      }

      val suggestions = scala.collection.mutable.ListBuffer[String]()
      var idx = l
      while (idx < n && suggestions.size < 3) {
        val word = sorted(idx)
        if (word.startsWith(prefix)) {
          suggestions += word
        } else {
          // No further words will match the prefix
          idx = n
        }
        idx += 1
      }

      result += suggestions.toList
    }

    result.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn suggested_products(products: Vec<String>, search_word: String) -> Vec<Vec<String>> {
        let mut products = products;
        products.sort();
        let mut result: Vec<Vec<String>> = Vec::new();
        let mut prefix = String::new();

        for ch in search_word.chars() {
            prefix.push(ch);
            // Find the first index where product >= prefix
            let idx = match products.binary_search_by(|s| s.as_str().cmp(&prefix)) {
                Ok(pos) => pos,
                Err(pos) => pos,
            };
            let mut suggestions: Vec<String> = Vec::new();
            for j in idx..std::cmp::min(idx + 3, products.len()) {
                if products[j].starts_with(&prefix) {
                    suggestions.push(products[j].clone());
                } else {
                    break;
                }
            }
            result.push(suggestions);
        }

        result
    }
}
```

## Racket

```racket
(define (starts-with? s prefix)
  (and (<= (string-length prefix) (string-length s))
       (let ((len (string-length prefix)))
         (string=? (substring s 0 len) prefix))))

(define/contract (suggested-products products searchWord)
  (-> (listof string?) string? (listof (listof string?)))
  (let* ((sorted (sort products string<?))
         (vec (list->vector sorted))
         (n (vector-length vec))
         (lenSW (string-length searchWord)))
    (let loop ((i 1) (results '()))
      (if (> i lenSW)
          (reverse results)
          (let* ((prefix (substring searchWord 0 i))
                 ;; lower bound binary search
                 (start (let lower ((lo 0) (hi n))
                          (if (= lo hi)
                              lo
                              (let* ((mid (quotient (+ lo hi) 2))
                                     (mid-val (vector-ref vec mid)))
                                (if (string<? mid-val prefix)
                                    (lower (+ mid 1) hi)
                                    (lower lo mid))))))
                 ;; collect up to three suggestions starting with prefix
                 (suggestions
                  (let collect ((j start) (cnt 0) (acc '()))
                    (if (or (= j n) (= cnt 3))
                        (reverse acc)
                        (let ((word (vector-ref vec j)))
                          (if (starts-with? word prefix)
                              (collect (+ j 1) (+ cnt 1) (cons word acc))
                              (reverse acc)))))))
            (loop (+ i 1) (cons suggestions results)))))))
```

## Erlang

```erlang
-spec suggested_products(Products :: [unicode:unicode_binary()], SearchWord :: unicode:unicode_binary()) -> [[unicode:unicode_binary()]].
suggested_products(Products, SearchWord) ->
    Sorted = lists:sort(Products),
    Prefixes = prefixes(SearchWord),
    [suggest_for_prefix(Sorted, P) || P <- Prefixes].

prefixes(Word) ->
    Len = byte_size(Word),
    lists:map(fun(I) -> binary:part(Word, {0, I}) end,
              lists:seq(1, Len)).

suggest_for_prefix(Sorted, Prefix) ->
    Dropped = drop_until_match(Sorted, Prefix),
    take_up_to_three(Dropped, Prefix, []).

drop_until_match([], _Prefix) -> [];
drop_until_match([H|T], Prefix) ->
    case starts_with(H, Prefix) of
        true -> [H|T];
        false -> drop_until_match(T, Prefix)
    end.

take_up_to_three(_, _, Acc) when length(Acc) =:= 3 ->
    lists:reverse(Acc);
take_up_to_three([], _Prefix, Acc) ->
    lists:reverse(Acc);
take_up_to_three([H|T], Prefix, Acc) ->
    case starts_with(H, Prefix) of
        true -> take_up_to_three(T, Prefix, [H|Acc]);
        false -> lists:reverse(Acc)
    end.

starts_with(Bin, Prefix) ->
    PLen = byte_size(Prefix),
    BLen = byte_size(Bin),
    if BLen < PLen -> false;
       true ->
           case binary:part(Bin, {0, PLen}) of
               Prefix -> true;
               _ -> false
           end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec suggested_products(products :: [String.t()], search_word :: String.t()) :: [[String.t()]]
  def suggested_products(products, search_word) do
    sorted = Enum.sort(products)
    max_len = String.length(search_word)

    1..max_len
    |> Enum.map(fn i ->
      prefix = binary_part(search_word, 0, i)
      start_idx = lower_bound(sorted, prefix, 0, length(sorted))
      sorted
      |> Enum.slice(start_idx, 3)
      |> Enum.filter(&String.starts_with?(&1, prefix))
    end)
  end

  defp lower_bound(arr, target, low, high) when low < high do
    mid = div(low + high, 2)

    if Enum.at(arr, mid) >= target do
      lower_bound(arr, target, low, mid)
    else
      lower_bound(arr, target, mid + 1, high)
    end
  end

  defp lower_bound(_arr, _target, low, _high), do: low
end
```
