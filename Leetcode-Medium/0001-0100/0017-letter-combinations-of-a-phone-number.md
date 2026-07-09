# 0017. Letter Combinations of a Phone Number

## Cpp

```cpp
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        static const vector<string> map = {
            "",     // 0
            "",     // 1
            "abc",  // 2
            "def",  // 3
            "ghi",  // 4
            "jkl",  // 5
            "mno",  // 6
            "pqrs", // 7
            "tuv",  // 8
            "wxyz"  // 9
        };
        vector<string> res;
        string cur;
        function<void(int)> dfs = [&](int idx) {
            if (idx == digits.size()) {
                res.push_back(cur);
                return;
            }
            const string& letters = map[digits[idx] - '0'];
            for (char ch : letters) {
                cur.push_back(ch);
                dfs(idx + 1);
                cur.pop_back();
            }
        };
        dfs(0);
        return res;
    }
};
```

## Java

```java
class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.isEmpty()) return result;
        String[] map = new String[]{
            "",     // 0
            "",     // 1
            "abc",  // 2
            "def",  // 3
            "ghi",  // 4
            "jkl",  // 5
            "mno",  // 6
            "pqrs", // 7
            "tuv",  // 8
            "wxyz"  // 9
        };
        backtrack(digits, 0, new StringBuilder(), result, map);
        return result;
    }
    
    private void backtrack(String digits, int index, StringBuilder path,
                           List<String> result, String[] map) {
        if (index == digits.length()) {
            result.add(path.toString());
            return;
        }
        String letters = map[digits.charAt(index) - '0'];
        for (int i = 0; i < letters.length(); i++) {
            path.append(letters.charAt(i));
            backtrack(digits, index + 1, path, result, map);
            path.deleteCharAt(path.length() - 1);
        }
    }
}
```

## Python

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []
        path = []

        def backtrack(idx):
            if idx == len(digits):
                res.append(''.join(path))
                return
            for ch in phone[digits[idx]]:
                path.append(ch)
                backtrack(idx + 1)
                path.pop()

        backtrack(0)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res: List[str] = []
        path: List[str] = []
        
        def backtrack(index: int) -> None:
            if index == len(digits):
                res.append(''.join(path))
                return
            for ch in phone[digits[index]]:
                path.append(ch)
                backtrack(index + 1)
                path.pop()
        
        backtrack(0)
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

static void backtrack(const char *digits, int len, int pos,
                      const char **map, char *combo,
                      char **res, int *idx) {
    if (pos == len) {
        res[*idx] = (char *)malloc((len + 1) * sizeof(char));
        strcpy(res[*idx], combo);
        (*idx)++;
        return;
    }
    const char *letters = map[digits[pos] - '0'];
    for (int i = 0; letters[i]; ++i) {
        combo[pos] = letters[i];
        backtrack(digits, len, pos + 1, map, combo, res, idx);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** letterCombinations(char* digits, int* returnSize) {
    if (!digits || *digits == '\0') {
        *returnSize = 0;
        return NULL;
    }

    const char *map[10] = {
        "",     // 0
        "",     // 1
        "abc",  // 2
        "def",  // 3
        "ghi",  // 4
        "jkl",  // 5
        "mno",  // 6
        "pqrs", // 7
        "tuv",  // 8
        "wxyz"  // 9
    };

    int len = (int)strlen(digits);
    int total = 1;
    for (int i = 0; i < len; ++i) {
        total *= (int)strlen(map[digits[i] - '0']);
    }

    char **res = (char **)malloc(total * sizeof(char *));
    char *combo = (char *)malloc((len + 1) * sizeof(char));
    combo[len] = '\0';

    int idx = 0;
    backtrack(digits, len, 0, map, combo, res, &idx);
    free(combo);

    *returnSize = idx;
    return res;
}
```

## Csharp

```csharp
using System.Collections.Generic;
using System.Text;

public class Solution {
    public IList<string> LetterCombinations(string digits) {
        if (string.IsNullOrEmpty(digits)) return new List<string>();
        
        var map = new Dictionary<char, string> {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        
        var result = new List<string>();
        var path = new StringBuilder();
        
        void Backtrack(int index) {
            if (index == digits.Length) {
                result.Add(path.ToString());
                return;
            }
            
            string letters = map[digits[index]];
            foreach (char c in letters) {
                path.Append(c);
                Backtrack(index + 1);
                path.Length--; // backtrack
            }
        }
        
        Backtrack(0);
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (!digits.length) return [];
    const map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    };
    const result = [];
    const backtrack = (index, path) => {
        if (index === digits.length) {
            result.push(path);
            return;
        }
        const letters = map[digits[index]];
        for (let i = 0; i < letters.length; i++) {
            backtrack(index + 1, path + letters[i]);
        }
    };
    backtrack(0, '');
    return result;
};
```

## Typescript

```typescript
function letterCombinations(digits: string): string[] {
    if (digits.length === 0) return [];
    const phone = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"];
    const result: string[] = [];

    const backtrack = (idx: number, path: string) => {
        if (idx === digits.length) {
            result.push(path);
            return;
        }
        const letters = phone[digits.charCodeAt(idx) - 48];
        for (let i = 0; i < letters.length; i++) {
            backtrack(idx + 1, path + letters[i]);
        }
    };

    backtrack(0, "");
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $digits
     * @return String[]
     */
    function letterCombinations($digits) {
        if ($digits === '') {
            return [];
        }
        $map = [
            '2' => ['a','b','c'],
            '3' => ['d','e','f'],
            '4' => ['g','h','i'],
            '5' => ['j','k','l'],
            '6' => ['m','n','o'],
            '7' => ['p','q','r','s'],
            '8' => ['t','u','v'],
            '9' => ['w','x','y','z']
        ];
        $res = [];
        $len = strlen($digits);
        $dfs = function($index, $path) use (&$dfs, &$res, $digits, $map, $len) {
            if ($index === $len) {
                $res[] = $path;
                return;
            }
            $digit = $digits[$index];
            foreach ($map[$digit] as $ch) {
                $dfs($index + 1, $path . $ch);
            }
        };
        $dfs(0, '');
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func letterCombinations(_ digits: String) -> [String] {
        if digits.isEmpty { return [] }
        let phoneMap: [Character: [String]] = [
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        ]
        var result = [String]()
        var path = ""
        let digitsArray = Array(digits)
        
        func backtrack(_ index: Int) {
            if index == digitsArray.count {
                result.append(path)
                return
            }
            let digit = digitsArray[index]
            guard let letters = phoneMap[digit] else { return }
            for letter in letters {
                path.append(letter)
                backtrack(index + 1)
                path.removeLast()
            }
        }
        
        backtrack(0)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun letterCombinations(digits: String): List<String> {
        if (digits.isEmpty()) return emptyList()
        val map = arrayOf(
            "",     // 0
            "",     // 1
            "abc",  // 2
            "def",  // 3
            "ghi",  // 4
            "jkl",  // 5
            "mno",  // 6
            "pqrs", // 7
            "tuv",  // 8
            "wxyz"  // 9
        )
        val result = mutableListOf<String>()
        val path = StringBuilder()
        fun backtrack(index: Int) {
            if (index == digits.length) {
                result.add(path.toString())
                return
            }
            val letters = map[digits[index] - '0']
            for (ch in letters) {
                path.append(ch)
                backtrack(index + 1)
                path.deleteCharAt(path.length - 1)
            }
        }
        backtrack(0)
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> letterCombinations(String digits) {
    if (digits.isEmpty) return [];

    const Map<String, String> phoneMap = {
      '2': 'abc',
      '3': 'def',
      '4': 'ghi',
      '5': 'jkl',
      '6': 'mno',
      '7': 'pqrs',
      '8': 'tuv',
      '9': 'wxyz',
    };

    final List<String> result = [];

    void backtrack(int index, String path) {
      if (index == digits.length) {
        result.add(path);
        return;
      }
      final letters = phoneMap[digits[index]]!;
      for (int i = 0; i < letters.length; i++) {
        backtrack(index + 1, path + letters[i]);
      }
    }

    backtrack(0, '');
    return result;
  }
}
```

## Golang

```go
func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}
	mapping := []string{
		"",    // 0
		"",    // 1
		"abc", // 2
		"def", // 3
		"ghi", // 4
		"jkl", // 5
		"mno", // 6
		"pqrs",// 7
		"tuv", // 8
		"wxyz",// 9
	}
	var res []string
	var backtrack func(int, string)
	backtrack = func(pos int, cur string) {
		if pos == len(digits) {
			res = append(res, cur)
			return
		}
		letters := mapping[digits[pos]-'0']
		for i := 0; i < len(letters); i++ {
			backtrack(pos+1, cur+string(letters[i]))
		}
	}
	backtrack(0, "")
	return res
}
```

## Ruby

```ruby
def letter_combinations(digits)
  return [] if digits.empty?
  map = {
    '2' => %w[a b c],
    '3' => %w[d e f],
    '4' => %w[g h i],
    '5' => %w[j k l],
    '6' => %w[m n o],
    '7' => %w[p q r s],
    '8' => %w[t u v],
    '9' => %w[w x y z]
  }
  result = []
  backtrack = nil
  backtrack = lambda do |idx, path|
    if idx == digits.length
      result << path.join('')
    else
      map[digits[idx]].each do |ch|
        path << ch
        backtrack.call(idx + 1, path)
        path.pop
      end
    end
  end
  backtrack.call(0, [])
  result
end
```

## Scala

```scala
object Solution {
    def letterCombinations(digits: String): List[String] = {
        if (digits.isEmpty) return Nil
        val mapping = Array(
            "abc",  //2
            "def",  //3
            "ghi",  //4
            "jkl",  //5
            "mno",  //6
            "pqrs", //7
            "tuv",  //8
            "wxyz"  //9
        )
        val sb = new StringBuilder
        val result = scala.collection.mutable.ListBuffer[String]()

        def backtrack(idx: Int): Unit = {
            if (idx == digits.length) {
                result += sb.toString()
                return
            }
            val chars = mapping(digits.charAt(idx) - '2')
            var i = 0
            while (i < chars.length) {
                sb.append(chars.charAt(i))
                backtrack(idx + 1)
                sb.setLength(sb.length - 1)
                i += 1
            }
        }

        backtrack(0)
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits.is_empty() {
            return Vec::new();
        }
        let map = ["", "", "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"];
        let bytes = digits.as_bytes();

        fn backtrack(
            idx: usize,
            digits: &[u8],
            map: &[&str; 10],
            cur: &mut String,
            res: &mut Vec<String>,
        ) {
            if idx == digits.len() {
                res.push(cur.clone());
                return;
            }
            let digit = (digits[idx] - b'0') as usize;
            let letters = map[digit];
            for ch in letters.chars() {
                cur.push(ch);
                backtrack(idx + 1, digits, map, cur, res);
                cur.pop();
            }
        }

        let mut res = Vec::new();
        let mut cur = String::new();
        backtrack(0, bytes, &map, &mut cur, &mut res);
        res
    }
}
```

## Racket

```racket
(define/contract (letter-combinations digits)
  (-> string? (listof string?))
  (if (string-empty? digits)
      '()
      (let* ([digit->letters
              (hash '#\2 "abc"
                    '#\3 "def"
                    '#\4 "ghi"
                    '#\5 "jkl"
                    '#\6 "mno"
                    '#\7 "pqrs"
                    '#\8 "tuv"
                    '#\9 "wxyz")])
        (let loop ((i 0) (combos (list "")))
          (if (= i (string-length digits))
              combos
              (let* ([digit (string-ref digits i)]
                     [letters (hash-ref digit->letters digit)])
                (define new-combos
                  (apply append
                         (for/list ([prefix combos])
                           (for/list ([ch (in-string letters)])
                             (string-append prefix (string ch))))))
                (loop (+ i 1) new-combos)))))))
```

## Erlang

```erlang
-module(solution).
-export([letter_combinations/1]).

-spec letter_combinations(Digits :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
letter_combinations(Digits) when is_binary(Digits) ->
    case Digits of
        <<>> -> [];
        _ ->
            DigitList = binary_to_list(Digits),
            lists:foldl(fun(D, Acc) ->
                Letters = digit_letters(D),
                combine(Acc, Letters)
            end,
            [<<>>],
            DigitList)
    end.

digit_letters($2) -> [$a,$b,$c];
digit_letters($3) -> [$d,$e,$f];
digit_letters($4) -> [$g,$h,$i];
digit_letters($5) -> [$j,$k,$l];
digit_letters($6) -> [$m,$n,$o];
digit_letters($7) -> [$p,$q,$r,$s];
digit_letters($8) -> [$t,$u,$v];
digit_letters($9) -> [$w,$x,$y,$z];
digit_letters(_) -> [].

combine(Acc, Letters) ->
    [ <<Prev/binary, L>> || Prev <- Acc, L <- Letters ].
```

## Elixir

```elixir
defmodule Solution do
  @spec letter_combinations(digits :: String.t()) :: [String.t()]
  def letter_combinations(digits) when digits == "" do
    []
  end

  def letter_combinations(digits) do
    mapping = %{
      "2" => ["a", "b", "c"],
      "3" => ["d", "e", "f"],
      "4" => ["g", "h", "i"],
      "5" => ["j", "k", "l"],
      "6" => ["m", "n", "o"],
      "7" => ["p", "q", "r", "s"],
      "8" => ["t", "u", "v"],
      "9" => ["w", "x", "y", "z"]
    }

    digits
    |> String.graphemes()
    |> Enum.reduce([""], fn digit, acc ->
      letters = Map.get(mapping, digit, [])
      for combo <- acc, letter <- letters do
        combo <> letter
      end
    end)
  end
end
```
