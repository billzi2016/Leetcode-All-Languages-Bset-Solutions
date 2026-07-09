# 3324. Find the Sequence of Strings Appeared on the Screen

## Cpp

```cpp
class Solution {
public:
    vector<string> stringSequence(string target) {
        vector<string> ans;
        string cur;
        for (char c : target) {
            cur.push_back('a');
            ans.push_back(cur);
            while (cur.back() < c) {
                cur.back()++;
                ans.push_back(cur);
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> stringSequence(String target) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        // First key press: append 'a'
        sb.append('a');
        result.add(sb.toString());

        int n = target.length();
        for (int i = 0; i < n; i++) {
            // Increment the last character until it matches target[i]
            while (sb.charAt(i) != target.charAt(i)) {
                char c = sb.charAt(i);
                c++; // move to next alphabet letter
                sb.setCharAt(i, c);
                result.add(sb.toString());
            }
            // If more characters are needed, append a new 'a'
            if (i + 1 < n) {
                sb.append('a');
                result.add(sb.toString());
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def stringSequence(self, target):
        """
        :type target: str
        :rtype: List[str]
        """
        res = []
        cur = ""
        for ch in target:
            # press key 1: append 'a'
            cur += 'a'
            res.append(cur)
            # press key 2 enough times to reach desired character
            inc = ord(ch) - ord('a')
            for _ in range(inc):
                cur = cur[:-1] + chr(ord(cur[-1]) + 1)
                res.append(cur)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def stringSequence(self, target: str) -> List[str]:
        result = []
        current = ""
        for ch in target:
            # press key 1: append 'a'
            current += 'a'
            result.append(current)
            # press key 2 as needed to reach desired character
            while current[-1] != ch:
                # increment last character
                last_char = chr(ord(current[-1]) + 1)
                current = current[:-1] + last_char
                result.append(current)
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <string>

static char* copyStr(const std::string& s) {
    char* p = (char*)malloc(s.size() + 1);
    memcpy(p, s.c_str(), s.size() + 1);
    return p;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** stringSequence(char* target, int* returnSize) {
    int n = (int)strlen(target);
    // Upper bound on number of strings
    int maxSize = 0;
    for (int i = 0; i < n; ++i) {
        maxSize += 1 + (target[i] - 'a');
    }
    char** ans = (char**)malloc(sizeof(char*) * maxSize);
    int idx = 0;
    std::string cur;

    for (int i = 0; i < n; ++i) {
        if ((int)cur.size() < i + 1) {
            cur.push_back('a');
            ans[idx++] = copyStr(cur);
        }
        while (cur.back() != target[i]) {
            cur.back() = cur.back() + 1;
            ans[idx++] = copyStr(cur);
        }
    }

    *returnSize = idx;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    public IList<string> StringSequence(string target) {
        var result = new List<string>();
        var sb = new StringBuilder();
        for (int i = 0; i < target.Length; i++) {
            if (sb.Length == i) {
                sb.Append('a');
                result.Add(sb.ToString());
            }
            while (sb[i] != target[i]) {
                sb[i] = (char)(sb[i] + 1);
                result.Add(sb.ToString());
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} target
 * @return {string[]}
 */
var stringSequence = function(target) {
    const res = [];
    let cur = "";
    for (let i = 0; i < target.length; i++) {
        // Append 'a' until we have a position for the current character
        while (cur.length < i + 1) {
            cur += 'a';
            res.push(cur);
        }
        // Increment the last character until it matches target[i]
        while (cur[cur.length - 1] !== target[i]) {
            const nextChar = String.fromCharCode(cur.charCodeAt(cur.length - 1) + 1);
            cur = cur.slice(0, -1) + nextChar;
            res.push(cur);
        }
    }
    return res;
};
```

## Typescript

```typescript
function stringSequence(target: string): string[] {
    const result: string[] = [];
    const current: string[] = [];

    for (let i = 0; i < target.length; i++) {
        // key 1: append 'a'
        current.push('a');
        result.push(current.join(''));

        // key 2: increment last character until it matches target[i]
        while (current[current.length - 1] < target[i]) {
            const nextChar = String.fromCharCode(
                current[current.length - 1].charCodeAt(0) + 1
            );
            current[current.length - 1] = nextChar;
            result.push(current.join(''));
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $target
     * @return String[]
     */
    function stringSequence($target) {
        $res = [];
        $cur = '';
        $n = strlen($target);
        for ($i = 0; $i < $n; $i++) {
            // Append 'a' until we have the required length
            while (strlen($cur) < $i + 1) {
                $cur .= 'a';
                $res[] = $cur;
            }
            // Increment last character to match target[i]
            $desired = $target[$i];
            while ($cur[strlen($cur) - 1] !== $desired) {
                $lastIdx = strlen($cur) - 1;
                $cur[$lastIdx] = chr(ord($cur[$lastIdx]) + 1);
                $res[] = $cur;
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func stringSequence(_ target: String) -> [String] {
        var result = [String]()
        var current = ""
        let aValue = UnicodeScalar("a").value
        for ch in target {
            // Key 1: append 'a'
            current.append("a")
            result.append(current)
            
            // Number of increments needed to reach the desired character
            let steps = Int(ch.unicodeScalars.first!.value - aValue)
            if steps > 0 {
                var lastVal = aValue
                for _ in 0..<steps {
                    lastVal += 1
                    let idx = current.index(before: current.endIndex)
                    current.replaceSubrange(idx...idx, with: String(UnicodeScalar(lastVal)!))
                    result.append(current)
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
    fun stringSequence(target: String): List<String> {
        val result = mutableListOf<String>()
        val sb = StringBuilder()
        for (ch in target) {
            // press key 1: append 'a'
            sb.append('a')
            result.add(sb.toString())
            // press key 2 as needed to reach desired character
            while (sb[sb.length - 1] < ch) {
                val lastIdx = sb.length - 1
                sb.setCharAt(lastIdx, (sb[lastIdx].code + 1).toChar())
                result.add(sb.toString())
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> stringSequence(String target) {
    List<String> result = [];
    List<int> codes = []; // offsets from 'a' (0..25)

    for (int i = 0; i < target.length; i++) {
      // Key 1: append an 'a'
      codes.add(0);
      result.add(_buildString(codes));

      int need = target.codeUnitAt(i) - 97; // desired offset
      while (codes.last < need) {
        // Key 2: increment the last character
        codes[codes.length - 1] += 1;
        result.add(_buildString(codes));
      }
    }

    return result;
  }

  String _buildString(List<int> codes) {
    return String.fromCharCodes(codes.map((c) => c + 97));
  }
}
```

## Golang

```go
func stringSequence(target string) []string {
    var res []string
    cur := make([]byte, 0, len(target))
    for i := 0; i < len(target); i++ {
        // press key 1: append 'a'
        cur = append(cur, 'a')
        res = append(res, string(cur))
        // press key 2 until the last character matches target[i]
        for cur[len(cur)-1] < target[i] {
            cur[len(cur)-1]++
            res = append(res, string(cur))
        }
    }
    return res
}
```

## Ruby

```ruby
def string_sequence(target)
  res = []
  cur = ""
  target.each_char do |c|
    cur << 'a'
    res << cur.dup
    while cur[-1].ord < c.ord
      cur[-1] = (cur[-1].ord + 1).chr
      res << cur.dup
    end
  end
  res
end
```

## Scala

```scala
object Solution {
    def stringSequence(target: String): List[String] = {
        val result = scala.collection.mutable.ListBuffer[String]()
        val sb = new StringBuilder()
        for (ch <- target) {
            // press key 1: append 'a'
            sb.append('a')
            result += sb.toString()
            // press key 2 until last character matches ch
            while (sb.charAt(sb.length - 1) != ch) {
                val idx = sb.length - 1
                sb.setCharAt(idx, (sb.charAt(idx) + 1).toChar)
                result += sb.toString()
            }
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn string_sequence(target: String) -> Vec<String> {
        let mut result = Vec::new();
        let mut cur: Vec<u8> = Vec::new();

        for ch in target.bytes() {
            // press key 1: append 'a'
            cur.push(b'a');
            result.push(String::from_utf8(cur.clone()).unwrap());

            // press key 2 repeatedly until the last character matches ch
            while *cur.last().unwrap() < ch {
                if let Some(last) = cur.last_mut() {
                    *last += 1;
                }
                result.push(String::from_utf8(cur.clone()).unwrap());
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (string-sequence target)
  (-> string? (listof string?))
  (let* ((n (string-length target))
         (cur "")
         (res '()))
    (for ([i (in-range n)])
      (when (= (string-length cur) i)
        (set! cur (string-append cur "a"))
        (set! res (cons cur res)))
      (let loop ()
        (define last-char (string-ref cur (- (string-length cur) 1)))
        (when (char<? last-char (string-ref target i))
          (define new-char (integer->char (+ 1 (char->integer last-char))))
          (set! cur (string-append (substring cur 0 (- (string-length cur) 1)) (string new-char)))
          (set! res (cons cur res))
          (loop))))
    (reverse res)))
```

## Erlang

```erlang
-spec string_sequence(Target :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
string_sequence(Target) ->
    Codes = unicode:characters_to_list(Target),
    {RevResult, _} = lists:foldl(
        fun(C, {AccRes, Cur}) ->
            % Append 'a'
            NewCur1 = Cur ++ [$a],
            Bin1 = unicode:characters_to_binary(NewCur1),
            Acc1 = [Bin1 | AccRes],
            % Increment last character until it matches C
            inc_until(NewCur1, C, Acc1)
        end,
        {[], []},
        Codes
    ),
    lists:reverse(RevResult).

%% Helper to increment the last character until it reaches TargetChar.
-spec inc_until(Cur :: [integer()], TargetChar :: integer(), Acc :: [unicode:unicode_binary()]) ->
          {[unicode:unicode_binary()], [integer()]}.
inc_until(Cur, TargetChar, Acc) ->
    case lists:last(Cur) of
        L when L < TargetChar ->
            NewLast = L + 1,
            NewCur = replace_last(Cur, NewLast),
            Bin = unicode:characters_to_binary(NewCur),
            inc_until(NewCur, TargetChar, [Bin | Acc]);
        _ ->
            {Acc, Cur}
    end.

%% Replace the last element of a list with NewVal.
-spec replace_last([integer()], integer()) -> [integer()].
replace_last(List, NewVal) ->
    Rev = lists:reverse(List),
    [_Old|RestRev] = Rev,
    NewRev = [NewVal | RestRev],
    lists:reverse(NewRev).
```

## Elixir

```elixir
defmodule Solution do
  @spec string_sequence(target :: String.t()) :: [String.t()]
  def string_sequence(target) do
    chars = String.to_charlist(target)

    {rev_list, _} =
      Enum.reduce(chars, {[], ""}, fn target_c, {list_rev, cur} ->
        # press key1: append 'a'
        cur = cur <> "a"
        list_rev = [cur | list_rev]

        if target_c > ?a do
          Enum.reduce((?a + 1)..target_c, {cur, list_rev}, fn code, {cstr, lrev} ->
            prefix = :binary.part(cstr, 0, byte_size(cstr) - 1)
            new_str = <<prefix::binary, code>>
            {new_str, [new_str | lrev]}
          end)
        else
          {cur, list_rev}
        end
      end)

    Enum.reverse(rev_list)
  end
end
```
