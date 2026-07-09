# 2900. Longest Unequal Adjacent Groups Subsequence I

## Cpp

```cpp
class Solution {
public:
    vector<string> getLongestSubsequence(vector<string>& words, vector<int>& groups) {
        int n = words.size();
        vector<string> ans;
        if (n == 0) return ans;
        ans.push_back(words[0]);
        for (int i = 1; i < n; ++i) {
            if (groups[i] != groups[i - 1]) {
                ans.push_back(words[i]);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public List<String> getLongestSubsequence(String[] words, int[] groups) {
        List<String> result = new ArrayList<>();
        if (words == null || words.length == 0) {
            return result;
        }
        result.add(words[0]);
        for (int i = 1; i < groups.length; i++) {
            if (groups[i] != groups[i - 1]) {
                result.add(words[i]);
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        result = []
        prev = None
        for w, g in zip(words, groups):
            if prev is None or g != prev:
                result.append(w)
                prev = g
        return result
```

## Python3

```python
from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []
        last_group = None
        for word, grp in zip(words, groups):
            if last_group is None or grp != last_group:
                result.append(word)
                last_group = grp
        return result
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** getLongestSubsequence(char** words, int wordsSize, int* groups, int groupsSize, int* returnSize) {
    // Allocate maximum possible size
    char **res = (char **)malloc(sizeof(char*) * wordsSize);
    int cnt = 0;
    for (int i = 0; i < groupsSize; ++i) {
        if (i == 0 || groups[i] != groups[i - 1]) {
            res[cnt++] = words[i];
        }
    }
    *returnSize = cnt;
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<string> GetLongestSubsequence(string[] words, int[] groups) {
        var result = new List<string>();
        if (words == null || groups == null || words.Length == 0) return result;
        result.Add(words[0]);
        for (int i = 1; i < groups.Length; i++) {
            if (groups[i] != groups[i - 1]) {
                result.Add(words[i]);
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {number[]} groups
 * @return {string[]}
 */
var getLongestSubsequence = function(words, groups) {
    const result = [];
    if (words.length === 0) return result;
    result.push(words[0]);
    for (let i = 1; i < groups.length; i++) {
        if (groups[i] !== groups[i - 1]) {
            result.push(words[i]);
        }
    }
    return result;
};
```

## Typescript

```typescript
function getLongestSubsequence(words: string[], groups: number[]): string[] {
    const result: string[] = [];
    for (let i = 0; i < words.length; i++) {
        if (i === 0 || groups[i] !== groups[i - 1]) {
            result.push(words[i]);
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
     * @param Integer[] $groups
     * @return String[]
     */
    function getLongestSubsequence($words, $groups) {
        $n = count($words);
        if ($n === 0) {
            return [];
        }
        $result = [$words[0]];
        for ($i = 1; $i < $n; $i++) {
            if ($groups[$i] !== $groups[$i - 1]) {
                $result[] = $words[$i];
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func getLongestSubsequence(_ words: [String], _ groups: [Int]) -> [String] {
        var ans = [String]()
        guard !words.isEmpty else { return ans }
        ans.append(words[0])
        for i in 1..<groups.count {
            if groups[i] != groups[i - 1] {
                ans.append(words[i])
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getLongestSubsequence(words: Array<String>, groups: IntArray): List<String> {
        val result = mutableListOf<String>()
        if (words.isEmpty()) return result
        result.add(words[0])
        for (i in 1 until words.size) {
            if (groups[i] != groups[i - 1]) {
                result.add(words[i])
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> getLongestSubsequence(List<String> words, List<int> groups) {
    List<String> result = [];
    for (int i = 0; i < words.length; i++) {
      if (i == 0 || groups[i] != groups[i - 1]) {
        result.add(words[i]);
      }
    }
    return result;
  }
}
```

## Golang

```go
func getLongestSubsequence(words []string, groups []int) []string {
    if len(words) == 0 {
        return nil
    }
    res := make([]string, 0, len(words))
    res = append(res, words[0])
    for i := 1; i < len(groups); i++ {
        if groups[i] != groups[i-1] {
            res = append(res, words[i])
        }
    }
    return res
}
```

## Ruby

```ruby
def get_longest_subsequence(words, groups)
  result = []
  groups.each_index do |i|
    if i == 0 || groups[i] != groups[i - 1]
      result << words[i]
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def getLongestSubsequence(words: Array[String], groups: Array[Int]): List[String] = {
        val result = scala.collection.mutable.ListBuffer[String]()
        if (words.nonEmpty) {
            result += words(0)
            for (i <- 1 until groups.length) {
                if (groups(i) != groups(i - 1)) {
                    result += words(i)
                }
            }
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        let n = words.len();
        if n == 0 {
            return Vec::new();
        }
        let mut ans = Vec::with_capacity(n);
        ans.push(words[0].clone());
        for i in 1..n {
            if groups[i] != groups[i - 1] {
                ans.push(words[i].clone());
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (get-longest-subsequence words groups)
  (-> (listof string?) (listof exact-integer?) (listof string?))
  (let loop ((i 0) (prev-group #f) (acc '()))
    (if (= i (length words))
        (reverse acc)
        (let ((curr-group (list-ref groups i)))
          (if (or (not prev-group) (not (= curr-group prev-group)))
              (loop (+ i 1) curr-group
                    (cons (list-ref words i) acc))
              (loop (+ i 1) prev-group acc))))))
```

## Erlang

```erlang
-spec get_longest_subsequence(Words :: [unicode:unicode_binary()], Groups :: [integer()]) -> [unicode:unicode_binary()].
get_longest_subsequence(Words, Groups) ->
    case lists:zip(Words, Groups) of
        [] -> [];
        [{FirstWord, FirstGroup} | Rest] ->
            build(Rest, FirstGroup, [FirstWord])
    end.

build([], _PrevGroup, Acc) ->
    lists:reverse(Acc);
build([{Word, Group} | Tail], PrevGroup, Acc) ->
    if
        Group =/= PrevGroup ->
            build(Tail, Group, [Word | Acc]);
        true ->
            build(Tail, PrevGroup, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_longest_subsequence(words :: [String.t()], groups :: [integer]) :: [String.t()]
  def get_longest_subsequence(words, groups) do
    case words do
      [] -> []
      [first_word | _] ->
        n = length(words)

        if n == 1 do
          words
        else
          first_group = hd(groups)

          {rev_res, _} =
            Enum.reduce(1..(n - 1), {[first_word], first_group}, fn i,
                                                                   {list_rev, prev_group} ->
              cur_group = Enum.at(groups, i)

              if cur_group != prev_group do
                {[Enum.at(words, i) | list_rev], cur_group}
              else
                {list_rev, prev_group}
              end
            end)

          Enum.reverse(rev_res)
        end
    end
  end
end
```
