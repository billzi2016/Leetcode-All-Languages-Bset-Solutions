# 0816. Ambiguous Coordinates

## Cpp

```cpp
class Solution {
public:
    vector<string> ambiguousCoordinates(string s) {
        string inner = s.substr(1, s.size() - 2);
        int n = inner.size();
        vector<string> result;
        for (int i = 1; i < n; ++i) {
            string leftPart = inner.substr(0, i);
            string rightPart = inner.substr(i);
            vector<string> leftOpts = gen(leftPart);
            vector<string> rightOpts = gen(rightPart);
            for (const string& l : leftOpts) {
                for (const string& r : rightOpts) {
                    result.push_back("(" + l + ", " + r + ")");
                }
            }
        }
        return result;
    }

private:
    vector<string> gen(const string& t) {
        vector<string> res;
        int len = t.size();
        // integer representation
        if (len == 1 || t[0] != '0') {
            res.push_back(t);
        }
        // decimal representations
        for (int i = 1; i < len; ++i) {
            string left = t.substr(0, i);
            string right = t.substr(i);
            if ((left.size() == 1 || left[0] != '0') && right.back() != '0') {
                res.push_back(left + "." + right);
            }
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> ambiguousCoordinates(String s) {
        String t = s.substring(1, s.length() - 1);
        int n = t.length();
        List<String> ans = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            String leftPart = t.substring(0, i);
            String rightPart = t.substring(i);
            List<String> leftVals = generate(leftPart);
            List<String> rightVals = generate(rightPart);
            for (String l : leftVals) {
                for (String r : rightVals) {
                    ans.add("(" + l + ", " + r + ")");
                }
            }
        }
        return ans;
    }

    private List<String> generate(String num) {
        List<String> res = new ArrayList<>();
        int len = num.length();
        // integer form
        if (len == 1 || num.charAt(0) != '0') {
            res.add(num);
        }
        // decimal forms
        for (int i = 1; i < len; i++) {
            String left = num.substring(0, i);
            String right = num.substring(i);
            if ((left.charAt(0) == '0' && left.length() > 1)) continue;
            if (right.charAt(right.length() - 1) == '0') continue;
            res.add(left + "." + right);
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def ambiguousCoordinates(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def gen(part):
            n = len(part)
            res = []
            # integer representation (no leading zeros unless single zero)
            if part[0] != '0' or part == "0":
                res.append(part)
            # decimal representations
            for i in range(1, n):
                left = part[:i]
                right = part[i:]
                # left side cannot have leading zeros unless it is exactly "0"
                if (left[0] != '0' or left == "0") and right[-1] != '0':
                    res.append(left + '.' + right)
            return res

        inner = s[1:-1]
        ans = []
        for i in range(1, len(inner)):
            left_part = inner[:i]
            right_part = inner[i:]
            left_opts = gen(left_part)
            right_opts = gen(right_part)
            for l in left_opts:
                for r in right_opts:
                    ans.append("(%s, %s)" % (l, r))
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        inner = s[1:-1]
        n = len(inner)
        
        def gen(num: str) -> List[str]:
            res = []
            # integer form
            if not (len(num) > 1 and num[0] == '0'):
                res.append(num)
            # decimal forms
            for i in range(1, len(num)):
                left, right = num[:i], num[i:]
                # left part cannot have leading zeros unless it's exactly "0"
                if len(left) > 1 and left[0] == '0':
                    continue
                # right part cannot end with zero
                if right[-1] == '0':
                    continue
                res.append(f"{left}.{right}")
            return res
        
        ans = []
        for i in range(1, n):
            left_part = inner[:i]
            right_part = inner[i:]
            left_options = gen(left_part)
            right_options = gen(right_part)
            for l in left_options:
                for r in right_options:
                    ans.append(f"({l}, {r})")
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/* Generate all valid representations of a numeric substring s[start..end-1] */
static char **gen(const char *s, int start, int end, int *cnt) {
    int len = end - start;
    /* Upper bound for number of possibilities: at most len (integer + decimals) */
    char **res = (char **)malloc(sizeof(char *) * (len * 2 + 2));
    *cnt = 0;

    if (len == 1) {
        char *num = (char *)malloc(2);
        num[0] = s[start];
        num[1] = '\0';
        res[(*cnt)++] = num;
        return res;
    }

    /* Integer form (no leading zero) */
    if (s[start] != '0') {
        char *num = (char *)malloc(len + 1);
        memcpy(num, s + start, len);
        num[len] = '\0';
        res[(*cnt)++] = num;
    }

    /* Decimal forms */
    if (s[end - 1] != '0') {               // fractional part must not end with zero
        for (int i = 1; i < len; ++i) {    // split after i digits
            if (s[start] == '0' && i > 1) continue; // leading zeros before decimal are illegal
            int leftLen = i;
            int rightLen = len - i;
            char *num = (char *)malloc(leftLen + 1 + rightLen + 1);
            memcpy(num, s + start, leftLen);
            num[leftLen] = '.';
            memcpy(num + leftLen + 1, s + start + i, rightLen);
            num[leftLen + 1 + rightLen] = '\0';
            res[(*cnt)++] = num;
        }
    }

    return res;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** ambiguousCoordinates(char* s, int* returnSize) {
    int n = (int)strlen(s);
    int innerLen = n - 2;                     // length without surrounding parentheses
    int capacity = 2000;
    char **ans = (char **)malloc(sizeof(char *) * capacity);
    int total = 0;

    for (int leftLen = 1; leftLen < innerLen; ++leftLen) {
        int cntL, cntR;
        char **listL = gen(s, 1, 1 + leftLen, &cntL);
        char **listR = gen(s, 1 + leftLen, n - 1, &cntR);

        for (int i = 0; i < cntL; ++i) {
            for (int j = 0; j < cntR; ++j) {
                int need = (int)strlen(listL[i]) + (int)strlen(listR[j]) + 4; // "(, )" and '\0'
                char *coord = (char *)malloc(need);
                snprintf(coord, need, "(%s, %s)", listL[i], listR[j]);
                if (total >= capacity) {
                    capacity *= 2;
                    ans = (char **)realloc(ans, sizeof(char *) * capacity);
                }
                ans[total++] = coord;
            }
        }

        for (int i = 0; i < cntL; ++i) free(listL[i]);
        for (int j = 0; j < cntR; ++j) free(listR[j]);
        free(listL);
        free(listR);
    }

    *returnSize = total;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> AmbiguousCoordinates(string s) {
        string inner = s.Substring(1, s.Length - 2);
        int n = inner.Length;
        List<string> result = new List<string>();
        for (int i = 1; i < n; i++) {
            string leftPart = inner.Substring(0, i);
            string rightPart = inner.Substring(i);
            var leftOptions = GenerateNumbers(leftPart);
            var rightOptions = GenerateNumbers(rightPart);
            foreach (var l in leftOptions) {
                foreach (var r in rightOptions) {
                    result.Add($"({l}, {r})");
                }
            }
        }
        return result;
    }

    private List<string> GenerateNumbers(string s) {
        List<string> list = new List<string>();
        int len = s.Length;

        // Whole number without decimal point
        if (len == 1 || s[0] != '0') {
            list.Add(s);
        }

        // Decimal numbers
        for (int i = 1; i < len; i++) {
            string intPart = s.Substring(0, i);
            string fracPart = s.Substring(i);

            // Integer part cannot have leading zeros unless it is exactly "0"
            if (intPart.Length > 1 && intPart[0] == '0') continue;
            // Fractional part cannot end with zero
            if (fracPart[fracPart.Length - 1] == '0') continue;

            list.Add(intPart + "." + fracPart);
        }

        return list;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var ambiguousCoordinates = function(s) {
    // Remove surrounding parentheses
    const t = s.slice(1, -1);
    const n = t.length;
    const result = [];

    // Generate all valid representations for a numeric substring
    const generate = (numStr) => {
        const res = [];
        const len = numStr.length;

        // Whole integer form (no leading zeros unless single digit)
        if (len === 1 || numStr[0] !== '0') {
            res.push(numStr);
        }

        // Decimal forms
        for (let i = 1; i < len; ++i) {
            const left = numStr.slice(0, i);
            const right = numStr.slice(i);

            // Integer part before decimal cannot have leading zeros unless it's "0"
            if (left.length > 1 && left[0] === '0') continue;
            // Fractional part cannot end with zero
            if (right[right.length - 1] === '0') continue;

            res.push(left + '.' + right);
        }
        return res;
    };

    for (let i = 1; i < n; ++i) {
        const leftStr = t.slice(0, i);
        const rightStr = t.slice(i);

        const leftOpts = generate(leftStr);
        const rightOpts = generate(rightStr);

        for (const l of leftOpts) {
            for (const r of rightOpts) {
                result.push(`(${l}, ${r})`);
            }
        }
    }

    return result;
};
```

## Typescript

```typescript
function ambiguousCoordinates(s: string): string[] {
    const inner = s.slice(1, -1);
    const n = inner.length;
    const result: string[] = [];

    function generate(t: string): string[] {
        const out: string[] = [];
        const len = t.length;

        // integer representation
        if (t[0] !== '0' || len === 1) {
            out.push(t);
        }

        // decimal representations
        for (let i = 1; i < len; ++i) {
            const left = t.slice(0, i);
            const right = t.slice(i);
            if ((left[0] === '0' && left.length > 1)) continue;
            if (right[right.length - 1] === '0') continue;
            out.push(left + '.' + right);
        }
        return out;
    }

    for (let i = 1; i < n; ++i) {
        const leftPart = inner.slice(0, i);
        const rightPart = inner.slice(i);
        const leftOpts = generate(leftPart);
        const rightOpts = generate(rightPart);
        for (const l of leftOpts) {
            for (const r of rightOpts) {
                result.push(`(${l}, ${r})`);
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
     * @param String $s
     * @return String[]
     */
    function ambiguousCoordinates($s) {
        $inner = substr($s, 1, -1);
        $n = strlen($inner);
        $result = [];

        for ($i = 1; $i < $n; $i++) {
            $leftStr = substr($inner, 0, $i);
            $rightStr = substr($inner, $i);

            $leftOpts = $this->generate($leftStr);
            $rightOpts = $this->generate($rightStr);

            foreach ($leftOpts as $l) {
                foreach ($rightOpts as $r) {
                    $result[] = "({$l}, {$r})";
                }
            }
        }

        return $result;
    }

    private function generate(string $t): array {
        $len = strlen($t);
        $list = [];

        if ($len == 1) {
            $list[] = $t;
            return $list;
        }

        // Leading zero case
        if ($t[0] === '0') {
            // Only a decimal representation is possible, and it must not end with zero
            if ($t[$len - 1] !== '0') {
                $list[] = "0." . substr($t, 1);
            }
            return $list;
        }

        // Trailing zero case: only integer representation allowed
        if ($t[$len - 1] === '0') {
            $list[] = $t;
            return $list;
        }

        // No leading or trailing zeros: integer and all possible decimals
        $list[] = $t; // integer form
        for ($i = 1; $i < $len; $i++) {
            $left = substr($t, 0, $i);
            $right = substr($t, $i);
            $list[] = $left . "." . $right;
        }

        return $list;
    }
}
```

## Swift

```swift
class Solution {
    func ambiguousCoordinates(_ s: String) -> [String] {
        let inner = String(s.dropFirst().dropLast())
        let chars = Array(inner)
        var result = [String]()
        let n = chars.count
        for i in 1..<n {
            let leftStr = String(chars[0..<i])
            let rightStr = String(chars[i..<n])
            let leftOptions = generate(leftStr)
            let rightOptions = generate(rightStr)
            for l in leftOptions {
                for r in rightOptions {
                    result.append("(\(l), \(r))")
                }
            }
        }
        return result
    }

    private func generate(_ s: String) -> [String] {
        var res = [String]()
        let n = s.count
        if n == 0 { return res }
        if n == 1 {
            res.append(s)
            return res
        }
        // integer without decimal allowed only if no leading zero
        if s.first! != "0" {
            res.append(s)
        }
        // decimals: insert point at any position
        let chars = Array(s)
        for i in 1..<n {
            let left = String(chars[0..<i])
            let right = String(chars[i..<n])
            // integer part validation
            if left.first! == "0" && left.count > 1 {
                continue
            }
            // fractional part cannot end with '0'
            if right.last! == "0" {
                continue
            }
            res.append("\(left).\(right)")
        }
        return res
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun ambiguousCoordinates(s: String): List<String> {
        val inner = s.substring(1, s.length - 1)
        val n = inner.length
        val result = mutableListOf<String>()
        for (i in 1 until n) {
            val leftPart = inner.substring(0, i)
            val rightPart = inner.substring(i)
            val leftOptions = generate(leftPart)
            val rightOptions = generate(rightPart)
            for (l in leftOptions) {
                for (r in rightOptions) {
                    result.add("($l, $r)")
                }
            }
        }
        return result
    }

    private fun generate(str: String): List<String> {
        val res = mutableListOf<String>()
        if (str.length == 1) {
            res.add(str)
            return res
        }
        // integer without decimal point, allowed only if no leading zero
        if (str[0] != '0') {
            res.add(str)
        }
        // decimals
        for (i in 1 until str.length) {
            val left = str.substring(0, i)
            val right = str.substring(i)
            // integer part cannot have leading zeros unless it is exactly "0"
            if (left.length > 1 && left[0] == '0') continue
            // fractional part cannot end with zero
            if (right.last() == '0') continue
            res.add("$left.$right")
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<String> ambiguousCoordinates(String s) {
    String str = s.substring(1, s.length - 1);
    int n = str.length;
    List<String> ans = [];

    List<String> generate(String num) {
      List<String> res = [];
      int len = num.length;
      if (len == 1) {
        res.add(num);
        return res;
      }
      // integer without leading zero
      if (num[0] != '0') {
        res.add(num);
      }
      // decimals
      for (int i = 1; i < len; ++i) {
        String left = num.substring(0, i);
        String right = num.substring(i);
        if (left.length > 1 && left[0] == '0') continue;
        if (right[right.length - 1] == '0') continue;
        res.add(left + '.' + right);
      }
      return res;
    }

    for (int i = 1; i < n; ++i) {
      String leftPart = str.substring(0, i);
      String rightPart = str.substring(i);
      List<String> leftList = generate(leftPart);
      List<String> rightList = generate(rightPart);
      for (String l in leftList) {
        for (String r in rightList) {
          ans.add('($l, $r)');
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
func ambiguousCoordinates(s string) []string {
    inner := s[1 : len(s)-1]
    m := len(inner)
    var res []string

    // generate all valid representations for a numeric substring
    gen := func(t string) []string {
        n := len(t)
        var out []string
        // whole number without decimal point
        if !(n > 1 && t[0] == '0') {
            out = append(out, t)
        }
        // with decimal point
        for i := 1; i < n; i++ {
            intPart := t[:i]
            fracPart := t[i:]
            if intPart[0] == '0' && len(intPart) > 1 {
                continue
            }
            if fracPart[len(fracPart)-1] == '0' {
                continue
            }
            out = append(out, intPart+"."+fracPart)
        }
        return out
    }

    for i := 1; i < m; i++ {
        leftStr := inner[:i]
        rightStr := inner[i:]
        leftOpts := gen(leftStr)
        rightOpts := gen(rightStr)
        for _, l := range leftOpts {
            for _, r := range rightOpts {
                res = append(res, "("+l+", "+r+")")
            }
        }
    }

    return res
}
```

## Ruby

```ruby
def generate(num)
  res = []
  n = num.length
  if n == 1
    res << num
    return res
  end

  # integer without leading zero
  res << num if num[0] != '0'

  # decimals
  (1...n).each do |i|
    left = num[0, i]
    right = num[i, n - i]
    next if left.length > 1 && left[0] == '0'      # leading zero in integer part
    next if right[-1] == '0'                      # trailing zero in fractional part
    res << "#{left}.#{right}"
  end

  res
end

def ambiguous_coordinates(s)
  s = s[1...-1]  # strip parentheses
  n = s.length
  ans = []

  (1...n).each do |i|
    left_str = s[0, i]
    right_str = s[i, n - i]

    left_opts = generate(left_str)
    right_opts = generate(right_str)

    left_opts.each do |l|
      right_opts.each do |r|
        ans << "(#{l}, #{r})"
      end
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
  def ambiguousCoordinates(s: String): List[String] = {
    val inner = s.substring(1, s.length - 1)
    val n = inner.length
    val result = scala.collection.mutable.ListBuffer[String]()

    def gen(num: String): List[String] = {
      val buf = scala.collection.mutable.ListBuffer[String]()
      // integer form (no leading zeros unless single digit)
      if (!(num.length > 1 && num.charAt(0) == '0')) {
        buf += num
      }
      // decimal forms
      for (i <- 1 until num.length) {
        val left = num.substring(0, i)
        val right = num.substring(i)
        // left part cannot have leading zeros unless single digit
        if (!(left.length > 1 && left.charAt(0) == '0')) {
          // right part cannot end with zero
          if (right.last != '0') {
            buf += s"$left.$right"
          }
        }
      }
      buf.toList
    }

    for (i <- 1 until n) {
      val leftStr = inner.substring(0, i)
      val rightStr = inner.substring(i)
      val leftOpts = gen(leftStr)
      val rightOpts = gen(rightStr)
      for (l <- leftOpts; r <- rightOpts) {
        result += s"($l, $r)"
      }
    }

    result.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn ambiguous_coordinates(s: String) -> Vec<String> {
        fn generate(num: &str) -> Vec<String> {
            let n = num.len();
            let mut res = Vec::new();

            // integer representation
            if n == 1 || !num.starts_with('0') {
                res.push(num.to_string());
            }

            // decimal representations
            for i in 1..n {
                let left = &num[..i];
                let right = &num[i..];

                // left part must be "0" or not start with '0'
                if left.starts_with('0') && left != "0" {
                    continue;
                }
                // right part cannot end with '0'
                if right.ends_with('0') {
                    continue;
                }

                res.push(format!("{}.{}", left, right));
            }

            res
        }

        let inner = &s[1..s.len() - 1];
        let n = inner.len();
        let mut ans = Vec::new();

        for i in 1..n {
            let left_str = &inner[..i];
            let right_str = &inner[i..];

            let left_opts = generate(left_str);
            let right_opts = generate(right_str);

            for l in &left_opts {
                for r in &right_opts {
                    ans.push(format!("({{}, {}})", l, r));
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(require racket/contract)

(define (gen-representations t)
  (let* ((len (string-length t))
         (res '()))
    (if (= len 1)
        (list t)
        (begin
          ;; integer without decimal point
          (when (or (= len 1) (not (char=? (string-ref t 0) #\0)))
            (set! res (cons t res)))
          ;; decimals
          (for ([i (in-range 1 len)])
            (let* ((left  (substring t 0 i))
                   (right (substring t i len)))
              (when (and (or (= (string-length left) 1)
                             (not (char=? (string-ref left 0) #\0)))
                         (not (char=? (string-ref right
                                                   (- (string-length right) 1)) #\0)))
                (set! res (cons (string-append left "." right) res)))))
          (reverse res)))))

(define/contract (ambiguous-coordinates s)
  (-> string? (listof string?))
  (let* ((inner (substring s 1 (- (string-length s) 1)))
         (n (string-length inner)))
    (for*/list ([i (in-range 1 n)]
                [x (in-list (gen-representations (substring inner 0 i)))]
                [y (in-list (gen-representations (substring inner i n)))])
      (string-append "(" x ", " y ")"))))
```

## Erlang

```erlang
-module(solution).
-export([ambiguous_coordinates/1]).

-spec ambiguous_coordinates(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
ambiguous_coordinates(S) ->
    Len = byte_size(S),
    Inner = binary:part(S, 1, Len - 2),
    Ilen = byte_size(Inner),
    lists:foldl(
        fun(I, Acc) ->
            LeftBin = binary:part(Inner, 0, I),
            RightBin = binary:part(Inner, I, Ilen - I),
            Llist = gen(LeftBin),
            Rlist = gen(RightBin),
            NewCoords = [<<$(, L/binary, $,, $\s, R/binary, $)>> || L <- Llist, R <- Rlist],
            NewCoords ++ Acc
        end,
        [],
        lists:seq(1, Ilen - 1)
    ).

gen(Bin) ->
    Len = byte_size(Bin),
    case Len of
        1 -> [Bin];
        _ ->
            First = binary:at(Bin, 0),
            Last = binary:at(Bin, Len - 1),
            cond_generate(First, Last, Bin)
    end.

cond_generate($0, $0, _) ->
    [];
cond_generate($0, _, Bin) ->
    RestLen = byte_size(Bin) - 1,
    RestBin = binary:part(Bin, 1, RestLen),
    case binary:at(RestBin, RestLen - 1) of
        $0 -> [];
        _ -> [<<$0, $., RestBin/binary>>]
    end;
cond_generate(_, $0, Bin) ->
    [Bin];
cond_generate(_, _, Bin) ->
    Len = byte_size(Bin),
    Decimals = lists:foldl(
        fun(K, Acc) ->
            Left = binary:part(Bin, 0, K),
            Right = binary:part(Bin, K, Len - K),
            [<<Left/binary, $., Right/binary>> | Acc]
        end,
        [],
        lists:seq(1, Len - 1)
    ),
    [Bin | Decimals].
```

## Elixir

```elixir
defmodule Solution do
  @spec ambiguous_coordinates(s :: String.t) :: [String.t]
  def ambiguous_coordinates(s) do
    inner = String.slice(s, 1, String.length(s) - 2)
    len = String.length(inner)

    for i <- 1..(len - 1),
        left <- possible(String.slice(inner, 0, i)),
        right <- possible(String.slice(inner, i, len - i)) do
      "(" <> left <> ", " <> right <> ")"
    end
  end

  defp possible(t) do
    l = String.length(t)

    cond do
      l == 1 ->
        [t]

      String.starts_with?(t, "0") and String.ends_with?(t, "0") ->
        []

      String.starts_with?(t, "0") ->
        ["0." <> String.slice(t, 1..-1)]

      String.ends_with?(t, "0") ->
        [t]

      true ->
        decimals =
          for i <- 1..(l - 1) do
            prefix = String.slice(t, 0, i)
            suffix = String.slice(t, i, l - i)
            prefix <> "." <> suffix
          end

        [t | decimals]
    end
  end
end
```
