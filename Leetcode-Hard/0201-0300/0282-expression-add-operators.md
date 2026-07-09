# 0282. Expression Add Operators

## Cpp

```cpp
class Solution {
public:
    vector<string> addOperators(string num, int target) {
        vector<string> res;
        dfs(num, 0, 0LL, 0LL, "", (long long)target, res);
        return res;
    }
private:
    void dfs(const string& num, int pos, long long curVal, long long lastOperand,
             const string& expr, long long target, vector<string>& res) {
        if (pos == (int)num.size()) {
            if (curVal == target) {
                res.push_back(expr);
            }
            return;
        }
        for (int i = pos; i < (int)num.size(); ++i) {
            // Skip numbers with leading zeros
            if (i != pos && num[pos] == '0') break;
            string curStr = num.substr(pos, i - pos + 1);
            long long curNum = stoll(curStr);
            if (pos == 0) {
                dfs(num, i + 1, curNum, curNum, curStr, target, res);
            } else {
                dfs(num, i + 1, curVal + curNum, curNum,
                    expr + "+" + curStr, target, res);
                dfs(num, i + 1, curVal - curNum, -curNum,
                    expr + "-" + curStr, target, res);
                long long newVal = curVal - lastOperand + lastOperand * curNum;
                dfs(num, i + 1, newVal, lastOperand * curNum,
                    expr + "*" + curStr, target, res);
            }
        }
    }
};
```

## Java

```java
class Solution {
    public List<String> addOperators(String num, int target) {
        List<String> results = new ArrayList<>();
        if (num == null || num.length() == 0) return results;
        dfs(num, target, 0, 0L, 0L, new StringBuilder(), results);
        return results;
    }

    private void dfs(String num, int target, int index,
                     long curVal, long prevOperand,
                     StringBuilder path, List<String> results) {
        if (index == num.length()) {
            if (curVal == target) {
                results.add(path.toString());
            }
            return;
        }

        int len = path.length();
        for (int i = index; i < num.length(); i++) {
            // avoid numbers with leading zeros
            if (i != index && num.charAt(index) == '0') break;

            String curStr = num.substring(index, i + 1);
            long curNum = Long.parseLong(curStr);

            if (index == 0) {
                // first number, no operator preceding it
                path.append(curStr);
                dfs(num, target, i + 1, curNum, curNum, path, results);
                path.setLength(len);
            } else {
                // addition
                path.append('+').append(curStr);
                dfs(num, target, i + 1, curVal + curNum, curNum, path, results);
                path.setLength(len);

                // subtraction
                path.append('-').append(curStr);
                dfs(num, target, i + 1, curVal - curNum, -curNum, path, results);
                path.setLength(len);

                // multiplication
                path.append('*').append(curStr);
                long newVal = curVal - prevOperand + prevOperand * curNum;
                dfs(num, target, i + 1, newVal, prevOperand * curNum, path, results);
                path.setLength(len);
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        n = len(num)

        def backtrack(index, expr, value, last):
            if index == n:
                if value == target:
                    res.append(expr)
                return

            for i in range(index, n):
                # avoid numbers with leading zeros
                if i != index and num[index] == '0':
                    break
                cur_str = num[index:i+1]
                cur = int(cur_str)

                if index == 0:
                    backtrack(i + 1, cur_str, cur, cur)
                else:
                    # addition
                    backtrack(i + 1, expr + '+' + cur_str, value + cur, cur)
                    # subtraction
                    backtrack(i + 1, expr + '-' + cur_str, value - cur, -cur)
                    # multiplication
                    new_value = value - last + last * cur
                    backtrack(i + 1, expr + '*' + cur_str, new_value, last * cur)

        backtrack(0, "", 0, 0)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)

        def dfs(index: int, path: str, eval_val: int, last: int):
            if index == n:
                if eval_val == target:
                    res.append(path)
                return

            for i in range(index, n):
                # Skip numbers with leading zero
                if i != index and num[index] == '0':
                    break
                cur_str = num[index:i + 1]
                cur = int(cur_str)

                if index == 0:
                    dfs(i + 1, cur_str, cur, cur)
                else:
                    dfs(i + 1, path + '+' + cur_str, eval_val + cur, cur)
                    dfs(i + 1, path + '-' + cur_str, eval_val - cur, -cur)
                    # For multiplication, adjust the previous operand
                    dfs(i + 1, path + '*' + cur_str,
                        eval_val - last + last * cur,
                        last * cur)

        dfs(0, "", 0, 0)
        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>

static void addResult(char ***res, int *size, int *cap, const char *expr, int len) {
    if (*size >= *cap) {
        *cap = (*cap) * 2;
        *res = (char **)realloc(*res, (*cap) * sizeof(char *));
    }
    char *s = (char *)malloc(len + 1);
    memcpy(s, expr, len);
    s[len] = '\0';
    (*res)[*size] = s;
    (*size)++;
}

static void dfs(const char *num, int n, int pos,
                long long curVal, long long lastOperand,
                char *expr, int exprLen,
                char ***res, int *size, int *cap,
                int target) {
    if (pos == n) {
        if (curVal == target) {
            addResult(res, size, cap, expr, exprLen);
        }
        return;
    }

    for (int i = pos; i < n; ++i) {
        // avoid numbers with leading zeros
        if (i > pos && num[pos] == '0')
            break;

        int curNumLen = i - pos + 1;
        char curStr[12];
        memcpy(curStr, num + pos, curNumLen);
        curStr[curNumLen] = '\0';
        long long operand = atoll(curStr);

        if (pos == 0) {
            // first number, no operator
            int newLen = curNumLen;
            memcpy(expr, curStr, curNumLen);
            dfs(num, n, i + 1, operand, operand,
                expr, newLen, res, size, cap, target);
        } else {
            int prevLen = exprLen;

            // '+'
            expr[exprLen++] = '+';
            memcpy(expr + exprLen, curStr, curNumLen);
            exprLen += curNumLen;
            dfs(num, n, i + 1, curVal + operand, operand,
                expr, exprLen, res, size, cap, target);
            exprLen = prevLen;

            // '-'
            expr[exprLen++] = '-';
            memcpy(expr + exprLen, curStr, curNumLen);
            exprLen += curNumLen;
            dfs(num, n, i + 1, curVal - operand, -operand,
                expr, exprLen, res, size, cap, target);
            exprLen = prevLen;

            // '*'
            expr[exprLen++] = '*';
            memcpy(expr + exprLen, curStr, curNumLen);
            exprLen += curNumLen;
            long long newCur = curVal - lastOperand + lastOperand * operand;
            long long newLast = lastOperand * operand;
            dfs(num, n, i + 1, newCur, newLast,
                expr, exprLen, res, size, cap, target);
            exprLen = prevLen;
        }
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** addOperators(char* num, int target, int* returnSize) {
    int n = (int)strlen(num);
    *returnSize = 0;
    int capacity = 128;
    char **result = (char **)malloc(capacity * sizeof(char *));
    char expr[32]; // sufficient for max length (2*10)

    dfs(num, n, 0, 0, 0, expr, 0, &result, returnSize, &capacity, target);
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    public IList<string> AddOperators(string num, int target)
    {
        var result = new List<string>();
        if (string.IsNullOrEmpty(num))
            return result;
        DFS(num, 0, 0L, 0L, "", (long)target, result);
        return result;
    }

    private void DFS(string num, int pos, long eval, long multed, string path, long target, List<string> res)
    {
        if (pos == num.Length)
        {
            if (eval == target)
                res.Add(path);
            return;
        }

        for (int i = pos; i < num.Length; ++i)
        {
            // prevent numbers with leading zeros
            if (i != pos && num[pos] == '0')
                break;

            string curStr = num.Substring(pos, i - pos + 1);
            long cur = long.Parse(curStr);

            if (pos == 0)
            {
                // first number, pick it without any operator
                DFS(num, i + 1, cur, cur, curStr, target, res);
            }
            else
            {
                DFS(num, i + 1, eval + cur, cur, path + "+" + curStr, target, res);
                DFS(num, i + 1, eval - cur, -cur, path + "-" + curStr, target, res);
                // multiplication: undo the previous operand and apply multiplication
                DFS(num, i + 1, eval - multed + multed * cur, multed * cur, path + "*" + curStr, target, res);
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @param {number} target
 * @return {string[]}
 */
var addOperators = function(num, target) {
    const res = [];
    const n = num.length;
    
    const dfs = (index, path, evalVal, prevNum) => {
        if (index === n) {
            if (evalVal === target) res.push(path);
            return;
        }
        for (let i = index; i < n; i++) {
            // skip numbers with leading zero
            if (i > index && num[index] === '0') break;
            const curStr = num.slice(index, i + 1);
            const cur = Number(curStr);
            
            if (index === 0) {
                dfs(i + 1, curStr, cur, cur);
            } else {
                dfs(i + 1, path + '+' + curStr, evalVal + cur, cur);
                dfs(i + 1, path + '-' + curStr, evalVal - cur, -cur);
                // multiplication: undo previous operand effect
                dfs(i + 1, path + '*' + curStr, evalVal - prevNum + prevNum * cur, prevNum * cur);
            }
        }
    };
    
    dfs(0, '', 0, 0);
    return res;
};
```

## Typescript

```typescript
function addOperators(num: string, target: number): string[] {
    const results: string[] = [];
    const n = num.length;

    function dfs(index: number, expr: string, value: number, prev: number): void {
        if (index === n) {
            if (value === target) {
                results.push(expr);
            }
            return;
        }

        for (let i = index; i < n; i++) {
            // Skip numbers with leading zero
            if (i !== index && num[index] === '0') break;

            const curStr = num.substring(index, i + 1);
            const curNum = Number(curStr);

            if (index === 0) {
                // First number, pick it without any operator.
                dfs(i + 1, curStr, curNum, curNum);
            } else {
                // Addition
                dfs(i + 1, expr + '+' + curStr, value + curNum, curNum);
                // Subtraction
                dfs(i + 1, expr + '-' + curStr, value - curNum, -curNum);
                // Multiplication
                dfs(
                    i + 1,
                    expr + '*' + curStr,
                    value - prev + prev * curNum,
                    prev * curNum
                );
            }
        }
    }

    dfs(0, '', 0, 0);
    return results;
}
```

## Php

```php
class Solution {
    /**
     * @param String $num
     * @param Integer $target
     * @return String[]
     */
    public function addOperators($num, $target) {
        $this->result = [];
        $this->dfs($num, $target, 0, "", 0, 0);
        return $this->result;
    }

    private $result = [];

    private function dfs($num, $target, $pos, $path, $eval, $multed) {
        $len = strlen($num);
        if ($pos == $len) {
            if ($eval === $target) {
                $this->result[] = $path;
            }
            return;
        }

        for ($i = $pos; $i < $len; $i++) {
            // Skip numbers with leading zero
            if ($i != $pos && $num[$pos] == '0') {
                break;
            }

            $curStr = substr($num, $pos, $i - $pos + 1);
            $curVal = intval($curStr);

            if ($pos == 0) {
                // First number, no operator preceding it
                $this->dfs($num, $target, $i + 1, $curStr, $curVal, $curVal);
            } else {
                // Addition
                $this->dfs($num, $target, $i + 1, $path . '+' . $curStr, $eval + $curVal, $curVal);
                // Subtraction
                $this->dfs($num, $target, $i + 1, $path . '-' . $curStr, $eval - $curVal, -$curVal);
                // Multiplication
                $newEval = $eval - $multed + ($multed * $curVal);
                $newMulted = $multed * $curVal;
                $this->dfs($num, $target, $i + 1, $path . '*' . $curStr, $newEval, $newMulted);
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func addOperators(_ num: String, _ target: Int) -> [String] {
        let digits = Array(num)
        let n = digits.count
        var results = [String]()
        let targetVal = Int64(target)

        func dfs(_ index: Int, _ path: String, _ eval: Int64, _ multed: Int64) {
            if index == n {
                if eval == targetVal {
                    results.append(path)
                }
                return
            }

            var curStr = ""
            for i in index..<n {
                // prevent numbers with leading zeros
                if i != index && digits[index] == "0" { break }
                curStr.append(digits[i])
                guard let curVal = Int64(curStr) else { continue }

                if index == 0 {
                    dfs(i + 1, curStr, curVal, curVal)
                } else {
                    dfs(i + 1, path + "+" + curStr, eval + curVal, curVal)
                    dfs(i + 1, path + "-" + curStr, eval - curVal, -curVal)
                    let newEval = eval - multed + multed * curVal
                    let newMulted = multed * curVal
                    dfs(i + 1, path + "*" + curStr, newEval, newMulted)
                }
            }
        }

        dfs(0, "", 0, 0)
        return results
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun addOperators(num: String, target: Int): List<String> {
        val result = mutableListOf<String>()
        if (num.isEmpty()) return result
        val n = num.length

        fun dfs(index: Int, path: StringBuilder, eval: Long, multed: Long) {
            if (index == n) {
                if (eval == target.toLong()) {
                    result.add(path.toString())
                }
                return
            }
            for (i in index until n) {
                // skip numbers with leading zero
                if (i != index && num[index] == '0') break
                val curStr = num.substring(index, i + 1)
                val cur = curStr.toLong()
                val len = path.length

                if (index == 0) {
                    // first operand, no operator preceding it
                    path.append(curStr)
                    dfs(i + 1, path, cur, cur)
                    path.setLength(len)
                } else {
                    // addition
                    path.append('+').append(curStr)
                    dfs(i + 1, path, eval + cur, cur)
                    path.setLength(len)

                    // subtraction
                    path.append('-').append(curStr)
                    dfs(i + 1, path, eval - cur, -cur)
                    path.setLength(len)

                    // multiplication
                    path.append('*').append(curStr)
                    dfs(i + 1, path, eval - multed + multed * cur, multed * cur)
                    path.setLength(len)
                }
            }
        }

        dfs(0, StringBuilder(), 0L, 0L)
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> addOperators(String num, int target) {
    List<String> ans = [];

    void dfs(int index, String path, int eval, int multed) {
      if (index == num.length) {
        if (eval == target) {
          ans.add(path);
        }
        return;
      }

      for (int i = index; i < num.length; i++) {
        // Skip numbers with leading zero
        if (i != index && num[index] == '0') break;

        String curStr = num.substring(index, i + 1);
        int curVal = int.parse(curStr);

        if (index == 0) {
          dfs(i + 1, curStr, curVal, curVal);
        } else {
          // addition
          dfs(i + 1, path + '+' + curStr, eval + curVal, curVal);
          // subtraction
          dfs(i + 1, path + '-' + curStr, eval - curVal, -curVal);
          // multiplication
          int newEval = eval - multed + multed * curVal;
          int newMulted = multed * curVal;
          dfs(i + 1, path + '*' + curStr, newEval, newMulted);
        }
      }
    }

    dfs(0, '', 0, 0);
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"strconv"
)

func addOperators(num string, target int) []string {
	var res []string
	n := len(num)
	if n == 0 {
		return res
	}
	tgt := int64(target)

	var dfs func(pos int, path string, eval int64, multed int64)
	dfs = func(pos int, path string, eval int64, multed int64) {
		if pos == n {
			if eval == tgt {
				res = append(res, path)
			}
			return
		}
		for i := pos; i < n; i++ {
			// avoid numbers with leading zeros
			if i > pos && num[pos] == '0' {
				break
			}
			curStr := num[pos : i+1]
			val, _ := strconv.ParseInt(curStr, 10, 64)

			if pos == 0 {
				dfs(i+1, curStr, val, val)
			} else {
				dfs(i+1, path+"+"+curStr, eval+val, val)
				dfs(i+1, path+"-"+curStr, eval-val, -val)
				dfs(i+1, path+"*"+curStr, eval-multed+multed*val, multed*val)
			}
		}
	}

	dfs(0, "", 0, 0)
	return res
}
```

## Ruby

```ruby
def add_operators(num, target)
  results = []

  dfs = nil
  dfs = lambda do |index, expr, value, prev|
    if index == num.length
      results << expr if value == target
      return
    end

    (index...num.length).each do |i|
      # skip numbers with leading zeros
      break if i != index && num[index] == '0'

      cur_str = num[index..i]
      cur_val = cur_str.to_i

      if index.zero?
        dfs.call(i + 1, cur_str, cur_val, cur_val)
      else
        # addition
        dfs.call(i + 1, expr + '+' + cur_str, value + cur_val, cur_val)
        # subtraction
        dfs.call(i + 1, expr + '-' + cur_str, value - cur_val, -cur_val)
        # multiplication
        new_value = value - prev + prev * cur_val
        dfs.call(i + 1, expr + '*' + cur_str, new_value, prev * cur_val)
      end
    end
  end

  dfs.call(0, '', 0, 0)
  results
end
```

## Scala

```scala
import scala.collection.mutable.ListBuffer
import scala.util.control.Breaks.{breakable, break}

object Solution {
  def addOperators(num: String, target: Int): List[String] = {
    val n = num.length
    val res = ListBuffer[String]()
    val tgt = target.toLong

    def backtrack(index: Int, expr: String, value: Long, last: Long): Unit = {
      if (index == n) {
        if (value == tgt) res += expr
        return
      }
      breakable {
        for (i <- index until n) {
          // Skip numbers with leading zeros
          if (i != index && num.charAt(index) == '0') {
            break
          }
          val curStr = num.substring(index, i + 1)
          val cur = curStr.toLong
          if (index == 0) {
            backtrack(i + 1, curStr, cur, cur)
          } else {
            backtrack(i + 1, expr + "+" + curStr, value + cur, cur)
            backtrack(i + 1, expr + "-" + curStr, value - cur, -cur)
            backtrack(i + 1, expr + "*" + curStr, value - last + last * cur, last * cur)
          }
        }
      }
    }

    backtrack(0, "", 0L, 0L)
    res.toList
  }
}
```

## Rust

```rust
use std::vec::Vec;

impl Solution {
    pub fn add_operators(num: String, target: i32) -> Vec<String> {
        let mut results = Vec::new();
        if num.is_empty() {
            return results;
        }
        let bytes = num.as_bytes();
        let n = bytes.len();
        let target_i64 = target as i64;
        let mut expr = String::new();

        fn dfs(
            bytes: &[u8],
            num_str: &str,
            target: i64,
            pos: usize,
            eval: i64,
            multed: i64,
            expr: &mut String,
            results: &mut Vec<String>,
        ) {
            if pos == bytes.len() {
                if eval == target {
                    results.push(expr.clone());
                }
                return;
            }

            let mut cur = 0i64;
            for i in pos..bytes.len() {
                // avoid numbers with leading zeros
                if i > pos && bytes[pos] == b'0' {
                    break;
                }
                cur = cur * 10 + (bytes[i] - b'0') as i64;
                let cur_str = &num_str[pos..i + 1];
                let len_before = expr.len();

                if pos == 0 {
                    // first number, no operator
                    expr.push_str(cur_str);
                    dfs(bytes, num_str, target, i + 1, cur, cur, expr, results);
                    expr.truncate(len_before);
                } else {
                    // '+'
                    expr.push('+');
                    expr.push_str(cur_str);
                    dfs(
                        bytes,
                        num_str,
                        target,
                        i + 1,
                        eval + cur,
                        cur,
                        expr,
                        results,
                    );
                    expr.truncate(len_before);

                    // '-'
                    expr.push('-');
                    expr.push_str(cur_str);
                    dfs(
                        bytes,
                        num_str,
                        target,
                        i + 1,
                        eval - cur,
                        -cur,
                        expr,
                        results,
                    );
                    expr.truncate(len_before);

                    // '*'
                    expr.push('*');
                    expr.push_str(cur_str);
                    let new_eval = eval - multed + multed * cur;
                    dfs(
                        bytes,
                        num_str,
                        target,
                        i + 1,
                        new_eval,
                        multed * cur,
                        expr,
                        results,
                    );
                    expr.truncate(len_before);
                }
            }
        }

        dfs(&bytes, &num, target_i64, 0, 0, 0, &mut expr, &mut results);
        results
    }
}
```

## Racket

```racket
(define/contract (add-operators num target)
  (-> string? exact-integer? (listof string?))
  (let* ((n (string-length num))
         (result '()))
    (define (dfs idx path eval prev)
      (if (= idx n)
          (when (= eval target)
            (set! result (cons path result)))
          (for ([end (in-range (+ idx 1) (+ n 1))])
            (let* ((curStr (substring num idx end))
                   (len (- end idx)))
              (when (or (= len 1) (not (char=? (string-ref curStr 0) #\0)))
                (let ((curNum (string->number curStr)))
                  (if (= idx 0)
                      (dfs end curStr curNum curNum)
                      (begin
                        (dfs end (string-append path "+" curStr) (+ eval curNum) curNum)
                        (dfs end (string-append path "-" curStr) (- eval curNum) (- curNum))
                        (let ((newEval (- eval prev))
                              (mult (* prev curNum)))
                          (dfs end (string-append path "*" curStr) (+ newEval mult) mult))))))))))
    (dfs 0 "" 0 0)
    (reverse result)))
```

## Erlang

```erlang
-module(solution).
-export([add_operators/2]).

-spec add_operators(Num :: unicode:unicode_binary(), Target :: integer()) -> [unicode:unicode_binary()].
add_operators(Num, Target) ->
    Digits = binary_to_list(Num),
    Len = length(Digits),
    lists:reverse(dfs(0, <<>>, 0, 0, Digits, Len, Target, [])).

%% dfs(Index, ExprBin, Value, Prev, Digits, Len, Target, Acc)
dfs(Index, _ExprBin, _Value, _Prev, _Digits, Len, _Target, Acc) when Index == Len ->
    Acc;
dfs(Index, ExprBin, Value, Prev, Digits, Len, Target, Acc) ->
    loop(Index, Index, ExprBin, Value, Prev, Digits, Len, Target, Acc).

%% loop(Start, I, ExprBin, Value, Prev, Digits, Len, Target, Acc)
loop(_Start, I, _ExprBin, _Value, _Prev, _Digits, Len, _Target, Acc) when I >= Len ->
    Acc;
loop(Start, I, ExprBin, Value, Prev, Digits, Len, Target, Acc) ->
    SubLen = I - Start + 1,
    SubList = lists:sublist(Digits, Start + 1, SubLen),
    case SubList of
        [$0 | Rest] when length(Rest) > 0 ->
            %% leading zero not allowed; stop extending this operand
            Acc;
        _ ->
            Num = list_to_integer(SubList),
            SubBin = list_to_binary(SubList),
            NewAcc =
                if Start == 0 ->
                    dfs(I + 1, SubBin, Num, Num, Digits, Len, Target, Acc);
                   true ->
                    ExprPlus = <<ExprBin/binary, $+, SubBin/binary>>,
                    Acc1 = dfs(I + 1, ExprPlus, Value + Num, Num, Digits, Len, Target, Acc),
                    ExprMinus = <<ExprBin/binary, $-, SubBin/binary>>,
                    Acc2 = dfs(I + 1, ExprMinus, Value - Num, -Num, Digits, Len, Target, Acc1),
                    ExprMul = <<ExprBin/binary, $*, SubBin/binary>>,
                    NewPrev = Prev * Num,
                    NewVal = Value - Prev + NewPrev,
                    dfs(I + 1, ExprMul, NewVal, NewPrev, Digits, Len, Target, Acc2)
                end,
            loop(Start, I + 1, ExprBin, Value, Prev, Digits, Len, Target, NewAcc)
    end.

%% When all digits are used, check if expression evaluates to target
dfs(Index, ExprBin, Value, _Prev, _Digits, Len, Target, Acc) when Index == Len ->
    case Value =:= Target of
        true -> [ExprBin | Acc];
        false -> Acc
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec add_operators(num :: String.t(), target :: integer) :: [String.t()]
  def add_operators(num, target) do
    len = String.length(num)
    res = dfs(num, len, 0, "", 0, 0, target, [])
    Enum.reverse(res)
  end

  # Base case: all digits processed
  defp dfs(_num, _len, pos, expr, cur_val, _last_operand, target, acc) when pos == _len do
    if cur_val == target do
      [expr | acc]
    else
      acc
    end
  end

  # Recursive case: try all possible next operands
  defp dfs(num, len, pos, expr, cur_val, last_operand, target, acc) do
    Enum.reduce(pos..(len - 1), acc, fn i, acc_inner ->
      sub_len = i - pos + 1
      part = String.slice(num, pos, sub_len)

      # Skip numbers with leading zeros
      if String.length(part) > 1 and String.starts_with?(part, "0") do
        acc_inner
      else
        val = String.to_integer(part)

        if pos == 0 do
          # First operand, no operator preceding it
          dfs(num, len, i + 1, part, val, val, target, acc_inner)
        else
          # '+'
          acc_plus =
            dfs(
              num,
              len,
              i + 1,
              expr <> "+" <> part,
              cur_val + val,
              val,
              target,
              acc_inner
            )

          # '-'
          acc_minus =
            dfs(
              num,
              len,
              i + 1,
              expr <> "-" <> part,
              cur_val - val,
              -val,
              target,
              acc_plus
            )

          # '*', adjust for precedence using last_operand
          new_cur = cur_val - last_operand + last_operand * val
          new_last = last_operand * val

          dfs(
            num,
            len,
            i + 1,
            expr <> "*" <> part,
            new_cur,
            new_last,
            target,
            acc_minus
          )
        end
      end
    end)
  end
end
```
