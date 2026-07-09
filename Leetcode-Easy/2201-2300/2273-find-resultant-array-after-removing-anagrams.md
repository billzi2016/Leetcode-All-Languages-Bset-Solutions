# 2273. Find Resultant Array After Removing Anagrams

## Cpp

```cpp
class Solution {
public:
    vector<string> removeAnagrams(vector<string>& words) {
        vector<string> result;
        vector<string> signatures;
        for (const string& w : words) {
            string sig = w;
            sort(sig.begin(), sig.end());
            if (!result.empty() && sig == signatures.back()) continue;
            result.push_back(w);
            signatures.push_back(std::move(sig));
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public List<String> removeAnagrams(String[] words) {
        List<String> result = new ArrayList<>();
        for (String word : words) {
            if (!result.isEmpty() && isAnagram(result.get(result.size() - 1), word)) {
                continue;
            }
            result.add(word);
        }
        return result;
    }

    private boolean isAnagram(String a, String b) {
        if (a.length() != b.length()) return false;
        char[] ca = a.toCharArray();
        char[] cb = b.toCharArray();
        java.util.Arrays.sort(ca);
        java.util.Arrays.sort(cb);
        return java.util.Arrays.equals(ca, cb);
    }
}
```

## Python

```python
class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        prev_key = None
        for w in words:
            cur_key = ''.join(sorted(w))
            if cur_key == prev_key:
                continue
            result.append(w)
            prev_key = cur_key
        return result
```

## Python3

```python
from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res: List[str] = []
        prev_key = ""
        for w in words:
            cur_key = ''.join(sorted(w))
            if not res or cur_key != prev_key:
                res.append(w)
                prev_key = cur_key
        return res
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static bool isAnagram(const char *a, const char *b) {
    int cnt[26] = {0};
    while (*a) {
        cnt[*a - 'a']++;
        a++;
    }
    while (*b) {
        cnt[*b - 'a']--;
        b++;
    }
    for (int i = 0; i < 26; ++i)
        if (cnt[i] != 0)
            return false;
    return true;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** removeAnagrams(char** words, int wordsSize, int* returnSize) {
    char **res = (char **)malloc(wordsSize * sizeof(char *));
    int idx = 0;
    for (int i = 0; i < wordsSize; ++i) {
        if (idx > 0 && isAnagram(words[i], res[idx - 1])) {
            continue; // skip current word
        }
        res[idx++] = words[i];
    }
    *returnSize = idx;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<string> RemoveAnagrams(string[] words)
    {
        var result = new List<string>();
        foreach (var w in words)
        {
            if (result.Count > 0 && AreAnagrams(result[result.Count - 1], w))
                continue;
            result.Add(w);
        }
        return result;
    }

    private bool AreAnagrams(string a, string b)
    {
        if (a.Length != b.Length) return false;
        var ca = a.ToCharArray();
        var cb = b.ToCharArray();
        Array.Sort(ca);
        Array.Sort(cb);
        for (int i = 0; i < ca.Length; i++)
            if (ca[i] != cb[i]) return false;
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {string[]}
 */
var removeAnagrams = function(words) {
    const result = [];
    let prevKey = '';
    for (const w of words) {
        const key = w.split('').sort().join('');
        if (result.length && key === prevKey) continue;
        result.push(w);
        prevKey = key;
    }
    return result;
};
```

## Typescript

```typescript
function removeAnagrams(words: string[]): string[] {
    const stack: { word: string; key: string }[] = [];
    for (const w of words) {
        const key = w.split('').sort().join('');
        if (stack.length && stack[stack.length - 1].key === key) continue;
        stack.push({ word: w, key });
    }
    return stack.map(item => item.word);
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $words
     * @return String[]
     */
    function removeAnagrams($words) {
        $result = [];
        foreach ($words as $word) {
            if (!empty($result)) {
                $last = end($result);
                if ($this->isAnagram($word, $last)) {
                    continue;
                }
            }
            $result[] = $word;
        }
        return $result;
    }

    private function isAnagram(string $a, string $b): bool {
        if (strlen($a) !== strlen($b)) {
            return false;
        }
        $arrA = str_split($a);
        $arrB = str_split($b);
        sort($arrA);
        sort($arrB);
        return $arrA === $arrB;
    }
}
```

## Swift

```swift
class Solution {
    func removeAnagrams(_ words: [String]) -> [String] {
        var result = [String]()
        var prevKey: String? = nil
        for word in words {
            let key = String(word.sorted())
            if let pk = prevKey, pk == key {
                continue
            }
            result.append(word)
            prevKey = key
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun removeAnagrams(words: Array<String>): List<String> {
        val result = mutableListOf<String>()
        var prevKey = ""
        for (word in words) {
            val key = word.toCharArray().sorted().joinToString("")
            if (result.isEmpty() || key != prevKey) {
                result.add(word)
                prevKey = key
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> removeAnagrams(List<String> words) {
    bool isAnagram(String a, String b) {
      if (a.length != b.length) return false;
      var listA = a.split('')..sort();
      var listB = b.split('')..sort();
      for (int i = 0; i < listA.length; i++) {
        if (listA[i] != listB[i]) return false;
      }
      return true;
    }

    List<String> result = [];
    for (var w in words) {
      if (result.isNotEmpty && isAnagram(result.last, w)) {
        continue; // delete current word
      }
      result.add(w);
    }
    return result;
  }
}
```

## Golang

```go
func removeAnagrams(words []string) []string {
	isAnagram := func(a, b string) bool {
		if len(a) != len(b) {
			return false
		}
		var cnt [26]int
		for i := 0; i < len(a); i++ {
			cnt[a[i]-'a']++
			cnt[b[i]-'a']--
		}
		for _, v := range cnt {
			if v != 0 {
				return false
			}
		}
		return true
	}

	res := make([]string, 0, len(words))
	for _, w := range words {
		if len(res) == 0 || !isAnagram(res[len(res)-1], w) {
			res = append(res, w)
		}
	}
	return res
}
```

## Ruby

```ruby
def remove_anagrams(words)
  result = []
  last_key = nil
  words.each do |w|
    cur_key = w.bytes.sort
    if !result.empty? && cur_key == last_key
      next
    else
      result << w
      last_key = cur_key
    end
  end
  result
end
```

## Scala

```scala
object Solution {
  def removeAnagrams(words: Array[String]): List[String] = {
    val result = scala.collection.mutable.ListBuffer[String]()
    var prevKey: String = null
    for (w <- words) {
      val key = w.sorted.mkString
      if (prevKey == null || key != prevKey) {
        result += w
        prevKey = key
      }
    }
    result.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn remove_anagrams(words: Vec<String>) -> Vec<String> {
        let mut result: Vec<String> = Vec::new();
        let mut last_key: Option<Vec<u8>> = None;
        for w in words.into_iter() {
            let mut key = w.as_bytes().to_vec();
            key.sort_unstable();
            if let Some(ref lk) = last_key {
                if *lk == key {
                    continue; // current word is an anagram of previous kept word
                }
            }
            last_key = Some(key);
            result.push(w);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (remove-anagrams words)
  (-> (listof string?) (listof string?))
  (let loop ((lst words) (prev #f) (acc '()))
    (if (null? lst)
        (reverse acc)
        (let* ((w (car lst))
               (can (list->string (sort (string->list w) char<?))))
          (if (and prev (string=? can prev))
              (loop (cdr lst) prev acc)
              (loop (cdr lst) can (cons w acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([remove_anagrams/1]).

-spec remove_anagrams(Words :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
remove_anagrams(Words) ->
    Stack = lists:foldl(
        fun(Word, Acc) ->
            Sorted = sort_word(Word),
            case Acc of
                [] ->
                    [{Word, Sorted} | Acc];
                [{_, PrevSorted} | _] when PrevSorted =:= Sorted ->
                    Acc;
                _ ->
                    [{Word, Sorted} | Acc]
            end
        end,
        [],
        Words
    ),
    lists:map(fun({W, _}) -> W end, lists:reverse(Stack)).

sort_word(Word) ->
    lists:sort(binary_to_list(Word)).
```

## Elixir

```elixir
defmodule Solution do
  @spec remove_anagrams(words :: [String.t()]) :: [String.t()]
  def remove_anagrams(words) do
    words
    |> Enum.reduce([], fn word, acc ->
      sorted = word |> String.graphemes() |> Enum.sort() |> Enum.join()

      case acc do
        [] -> [{word, sorted}]
        [{prev_word, prev_sorted} | _] = rev_acc ->
          if prev_sorted == sorted do
            rev_acc
          else
            [{word, sorted} | rev_acc]
          end
      end
    end)
    |> Enum.map(fn {w, _} -> w end)
    |> Enum.reverse()
  end
end
```
