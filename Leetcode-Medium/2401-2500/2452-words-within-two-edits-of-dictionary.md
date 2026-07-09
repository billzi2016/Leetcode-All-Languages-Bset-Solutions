# 2452. Words Within Two Edits of Dictionary

## Cpp

```cpp
class Solution {
public:
    vector<string> twoEditWords(vector<string>& queries, vector<string>& dictionary) {
        vector<string> result;
        for (const string& q : queries) {
            bool ok = false;
            for (const string& d : dictionary) {
                int diff = 0;
                for (size_t i = 0; i < q.size(); ++i) {
                    if (q[i] != d[i]) {
                        ++diff;
                        if (diff > 2) break;
                    }
                }
                if (diff <= 2) {
                    ok = true;
                    break;
                }
            }
            if (ok) result.push_back(q);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<String> twoEditWords(String[] queries, String[] dictionary) {
        java.util.List<String> result = new java.util.ArrayList<>();
        for (String q : queries) {
            boolean ok = false;
            for (String d : dictionary) {
                int diff = 0;
                for (int i = 0; i < q.length(); i++) {
                    if (q.charAt(i) != d.charAt(i)) {
                        diff++;
                        if (diff > 2) break;
                    }
                }
                if (diff <= 2) {
                    ok = true;
                    break;
                }
            }
            if (ok) result.add(q);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        res = []
        for q in queries:
            for d in dictionary:
                diff = 0
                # early exit if more than 2 differences
                for c1, c2 in zip(q, d):
                    if c1 != c2:
                        diff += 1
                        if diff > 2:
                            break
                if diff <= 2:
                    res.append(q)
                    break
        return res
```

## Python3

```python
from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for q in queries:
            for d in dictionary:
                diff = 0
                for c1, c2 in zip(q, d):
                    if c1 != c2:
                        diff += 1
                        if diff > 2:
                            break
                if diff <= 2:
                    res.append(q)
                    break
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** twoEditWords(char** queries, int queriesSize, char** dictionary, int dictionarySize, int* returnSize) {
    char **result = (char **)malloc(sizeof(char*) * queriesSize);
    int count = 0;
    
    for (int i = 0; i < queriesSize; ++i) {
        const char *q = queries[i];
        for (int j = 0; j < dictionarySize; ++j) {
            const char *d = dictionary[j];
            int diff = 0;
            while (*q && *d) {
                if (*q != *d) {
                    ++diff;
                    if (diff > 2) break;
                }
                ++q;
                ++d;
            }
            // reset pointers for next dictionary word
            q = queries[i];
            if (diff <= 2) {
                result[count++] = queries[i];
                break;
            }
        }
    }
    
    *returnSize = count;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<string> TwoEditWords(string[] queries, string[] dictionary) {
        var result = new List<string>();
        foreach (var q in queries) {
            bool ok = false;
            foreach (var d in dictionary) {
                int diff = 0;
                for (int i = 0; i < q.Length && diff <= 2; i++) {
                    if (q[i] != d[i]) diff++;
                }
                if (diff <= 2) {
                    ok = true;
                    break;
                }
            }
            if (ok) result.Add(q);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} queries
 * @param {string[]} dictionary
 * @return {string[]}
 */
var twoEditWords = function(queries, dictionary) {
    const result = [];
    for (const q of queries) {
        let match = false;
        for (const d of dictionary) {
            let diff = 0;
            for (let i = 0; i < q.length && diff <= 2; i++) {
                if (q[i] !== d[i]) diff++;
            }
            if (diff <= 2) {
                match = true;
                break;
            }
        }
        if (match) result.push(q);
    }
    return result;
};
```

## Typescript

```typescript
function twoEditWords(queries: string[], dictionary: string[]): string[] {
    const res: string[] = [];
    
    for (const q of queries) {
        let ok = false;
        for (const d of dictionary) {
            let diff = 0;
            for (let i = 0; i < q.length && diff <= 2; i++) {
                if (q[i] !== d[i]) diff++;
            }
            if (diff <= 2) {
                ok = true;
                break;
            }
        }
        if (ok) res.push(q);
    }
    
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $queries
     * @param String[] $dictionary
     * @return String[]
     */
    function twoEditWords($queries, $dictionary) {
        $result = [];
        foreach ($queries as $q) {
            foreach ($dictionary as $d) {
                $len = strlen($q);
                $diff = 0;
                for ($i = 0; $i < $len; $i++) {
                    if ($q[$i] !== $d[$i]) {
                        $diff++;
                        if ($diff > 2) {
                            break;
                        }
                    }
                }
                if ($diff <= 2) {
                    $result[] = $q;
                    break;
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
    func twoEditWords(_ queries: [String], _ dictionary: [String]) -> [String] {
        var result = [String]()
        for query in queries {
            let qChars = Array(query)
            outerLoop: for dictWord in dictionary {
                let dChars = Array(dictWord)
                var diff = 0
                for i in 0..<qChars.count {
                    if qChars[i] != dChars[i] {
                        diff += 1
                        if diff > 2 { break }
                    }
                }
                if diff <= 2 {
                    result.append(query)
                    break outerLoop
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun twoEditWords(queries: Array<String>, dictionary: Array<String>): List<String> {
        val result = mutableListOf<String>()
        for (q in queries) {
            outer@ for (d in dictionary) {
                var diff = 0
                for (i in q.indices) {
                    if (q[i] != d[i]) {
                        diff++
                        if (diff > 2) break
                    }
                }
                if (diff <= 2) {
                    result.add(q)
                    break@outer
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
  List<String> twoEditWords(List<String> queries, List<String> dictionary) {
    List<String> result = [];
    for (var query in queries) {
      bool matchFound = false;
      for (var word in dictionary) {
        int diff = 0;
        for (int i = 0; i < query.length && diff <= 2; i++) {
          if (query.codeUnitAt(i) != word.codeUnitAt(i)) diff++;
        }
        if (diff <= 2) {
          matchFound = true;
          break;
        }
      }
      if (matchFound) result.add(query);
    }
    return result;
  }
}
```

## Golang

```go
func twoEditWords(queries []string, dictionary []string) []string {
	var result []string
	for _, q := range queries {
		for _, d := range dictionary {
			diff := 0
			for i := 0; i < len(q); i++ {
				if q[i] != d[i] {
					diff++
					if diff > 2 {
						break
					}
				}
			}
			if diff <= 2 {
				result = append(result, q)
				break
			}
		}
	}
	return result
}
```

## Ruby

```ruby
def two_edit_words(queries, dictionary)
  result = []
  queries.each do |q|
    match = dictionary.any? do |d|
      diff = 0
      q.length.times do |i|
        diff += 1 if q[i] != d[i]
        break if diff > 2
      end
      diff <= 2
    end
    result << q if match
  end
  result
end
```

## Scala

```scala
object Solution {
    def twoEditWords(queries: Array[String], dictionary: Array[String]): List[String] = {
        def withinTwo(a: String, b: String): Boolean = {
            var cnt = 0
            var i = 0
            val n = a.length
            while (i < n && cnt <= 2) {
                if (a.charAt(i) != b.charAt(i)) cnt += 1
                i += 1
            }
            cnt <= 2
        }

        val result = scala.collection.mutable.ListBuffer[String]()
        for (q <- queries) {
            if (dictionary.exists(d => withinTwo(q, d))) {
                result += q
            }
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn two_edit_words(queries: Vec<String>, dictionary: Vec<String>) -> Vec<String> {
        let mut result = Vec::new();
        for q in &queries {
            'dict_loop: for d in &dictionary {
                let qb = q.as_bytes();
                let db = d.as_bytes();
                let mut diff = 0;
                for i in 0..qb.len() {
                    if qb[i] != db[i] {
                        diff += 1;
                        if diff > 2 {
                            continue 'dict_loop;
                        }
                    }
                }
                // found a dictionary word within two edits
                result.push(q.clone());
                break;
            }
        }
        result
    }
}
```

## Racket

```racket
(define (hamming<=2 s t)
  (let ((len (string-length s)))
    (let loop ((i 0) (cnt 0))
      (cond
        [(> cnt 2) #f]
        [(= i len) #t]
        [else (loop (+ i 1)
                    (if (char=? (string-ref s i) (string-ref t i))
                        cnt
                        (+ cnt 1)))]))))

(define (within-two? q dict)
  (let loop ((ds dict))
    (cond [(null? ds) #f]
          [(hamming<=2 q (car ds)) #t]
          [else (loop (cdr ds))])))

(define/contract (two-edit-words queries dictionary)
  (-> (listof string?) (listof string?) (listof string?))
  (filter (lambda (q) (within-two? q dictionary)) queries))
```

## Erlang

```erlang
-module(solution).
-export([two_edit_words/2]).

-spec two_edit_words(Queries :: [unicode:unicode_binary()], Dictionary :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
two_edit_words(Queries, Dictionary) ->
    lists:reverse(
      lists:foldl(fun(Q, Acc) ->
          case has_match(Q, Dictionary) of
              true -> [Q | Acc];
              false -> Acc
          end
      end, [], Queries)
    ).

has_match(Query, Dictionary) ->
    lists:any(fun(DictWord) -> mismatches(Query, DictWord) =< 2 end, Dictionary).

mismatches(<<>>, <<>>) -> 0;
mismatches(<<C1, Rest1/binary>>, <<C2, Rest2/binary>>) ->
    Diff = if C1 =:= C2 -> 0; true -> 1 end,
    Diff + mismatches(Rest1, Rest2).
```

## Elixir

```elixir
defmodule Solution do
  @spec two_edit_words(queries :: [String.t()], dictionary :: [String.t()]) :: [String.t()]
  def two_edit_words(queries, dictionary) do
    Enum.filter(queries, fn q ->
      Enum.any?(dictionary, fn d -> hamming_distance(q, d) <= 2 end)
    end)
  end

  defp hamming_distance(a, b) do
    a_chars = String.to_charlist(a)
    b_chars = String.to_charlist(b)

    Enum.zip(a_chars, b_chars)
    |> Enum.reduce_while(0, fn {c1, c2}, acc ->
      if c1 != c2 do
        new_acc = acc + 1

        if new_acc > 2,
          do: {:halt, new_acc},
          else: {:cont, new_acc}
      else
        {:cont, acc}
      end
    end)
  end
end
```
