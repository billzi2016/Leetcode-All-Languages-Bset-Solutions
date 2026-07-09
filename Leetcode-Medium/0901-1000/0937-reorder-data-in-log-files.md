# 0937. Reorder Data in Log Files

## Cpp

```cpp
class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        auto isDigitLog = [](const string& log) -> bool {
            size_t pos = log.find(' ');
            // The character right after the space determines the type
            return isdigit(log[pos + 1]);
        };
        
        stable_sort(logs.begin(), logs.end(),
            [&](const string& a, const string& b) {
                size_t posA = a.find(' ');
                size_t posB = b.find(' ');
                bool digitA = isdigit(a[posA + 1]);
                bool digitB = isdigit(b[posB + 1]);
                
                if (!digitA && !digitB) { // both letter-logs
                    string contentA = a.substr(posA + 1);
                    string contentB = b.substr(posB + 1);
                    if (contentA != contentB)
                        return contentA < contentB;
                    // contents equal, compare identifiers
                    return a.substr(0, posA) < b.substr(0, posB);
                }
                // letter-logs come before digit-logs
                return (!digitA && digitB);
            });
        return logs;
    }
};
```

## Java

```java
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String[] reorderLogFiles(String[] logs) {
        Arrays.sort(logs, new Comparator<String>() {
            @Override
            public int compare(String log1, String log2) {
                int idx1 = log1.indexOf(' ');
                int idx2 = log2.indexOf(' ');
                String id1 = log1.substring(0, idx1);
                String id2 = log2.substring(0, idx2);
                String rest1 = log1.substring(idx1 + 1);
                String rest2 = log2.substring(idx2 + 1);
                boolean isDigit1 = Character.isDigit(rest1.charAt(0));
                boolean isDigit2 = Character.isDigit(rest2.charAt(0));

                if (!isDigit1 && !isDigit2) {
                    int cmp = rest1.compareTo(rest2);
                    if (cmp != 0) return cmp;
                    return id1.compareTo(id2);
                }
                if (!isDigit1 && isDigit2) return -1;
                if (isDigit1 && !isDigit2) return 1;
                // both digit-logs, maintain original order
                return 0;
            }
        });
        return logs;
    }
}
```

## Python

```python
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def sort_key(log):
            identifier, rest = log.split(" ", 1)
            # Digit-log if first character of the rest is a digit
            if rest[0].isdigit():
                return (1,)
            # Letter-log
            return (0, rest, identifier)
        return sorted(logs, key=sort_key)
```

## Python3

```python
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sort_key(log: str):
            identifier, rest = log.split(" ", 1)
            if rest[0].isdigit():
                return (1,)
            return (0, rest, identifier)
        return sorted(logs, key=sort_key)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct {
    char *full;      // original log string
    int idx;         // original position
    int isLetter;    // 1 if letter-log, 0 if digit-log
    char *content;   // pointer to content part (after identifier and space)
    char *id;        // null‑terminated identifier
} Log;

static int logCmp(const void *a, const void *b) {
    const Log *l1 = (const Log *)a;
    const Log *l2 = (const Log *)b;

    if (l1->isLetter && l2->isLetter) {
        int c = strcmp(l1->content, l2->content);
        if (c != 0) return c;
        return strcmp(l1->id, l2->id);
    }
    if (l1->isLetter && !l2->isLetter) return -1;
    if (!l1->isLetter && l2->isLetter) return 1;
    /* both digit-logs: preserve original order */
    return l1->idx - l2->idx;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** reorderLogFiles(char** logs, int logsSize, int* returnSize) {
    if (logsSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    Log *arr = (Log *)malloc(sizeof(Log) * logsSize);
    for (int i = 0; i < logsSize; ++i) {
        arr[i].full = logs[i];
        arr[i].idx = i;

        char *space = strchr(logs[i], ' ');
        int idLen = space - logs[i];

        /* copy identifier */
        arr[i].id = (char *)malloc(idLen + 1);
        memcpy(arr[i].id, logs[i], idLen);
        arr[i].id[idLen] = '\0';

        arr[i].content = space + 1;
        arr[i].isLetter = !isdigit((unsigned char)arr[i].content[0]);
    }

    qsort(arr, logsSize, sizeof(Log), logCmp);

    char **result = (char **)malloc(sizeof(char *) * logsSize);
    for (int i = 0; i < logsSize; ++i) {
        result[i] = arr[i].full;
        free(arr[i].id);   /* identifier no longer needed */
    }

    free(arr);
    *returnSize = logsSize;
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public string[] ReorderLogFiles(string[] logs) {
        var letterLogs = new List<string>();
        var digitLogs = new List<string>();

        foreach (var log in logs) {
            int idx = log.IndexOf(' ');
            if (idx == -1) {
                digitLogs.Add(log);
                continue;
            }
            string rest = log.Substring(idx + 1);
            if (char.IsDigit(rest[0]))
                digitLogs.Add(log);
            else
                letterLogs.Add(log);
        }

        letterLogs.Sort((a, b) => {
            int i1 = a.IndexOf(' ');
            int i2 = b.IndexOf(' ');
            string id1 = a.Substring(0, i1);
            string id2 = b.Substring(0, i2);
            string rest1 = a.Substring(i1 + 1);
            string rest2 = b.Substring(i2 + 1);

            int cmp = String.Compare(rest1, rest2, StringComparison.Ordinal);
            if (cmp != 0) return cmp;
            return String.Compare(id1, id2, StringComparison.Ordinal);
        });

        var result = new List<string>(logs.Length);
        result.AddRange(letterLogs);
        result.AddRange(digitLogs);
        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} logs
 * @return {string[]}
 */
var reorderLogFiles = function(logs) {
    const isDigitLog = (log) => {
        const firstSpace = log.indexOf(' ');
        // check the first character after identifier
        return /\d/.test(log[firstSpace + 1]);
    };
    
    logs.sort((a, b) => {
        const aIdx = a.indexOf(' ');
        const bIdx = b.indexOf(' ');
        const aId = a.substring(0, aIdx);
        const bId = b.substring(0, bIdx);
        const aRest = a.substring(aIdx + 1);
        const bRest = b.substring(bIdx + 1);
        const aIsDigit = /^\d/.test(aRest);
        const bIsDigit = /^\d/.test(bRest);
        
        if (!aIsDigit && !bIsDigit) {
            // both letter-logs: compare content then identifier
            if (aRest < bRest) return -1;
            if (aRest > bRest) return 1;
            if (aId < bId) return -1;
            if (aId > bId) return 1;
            return 0;
        }
        // one letter-log and one digit-log
        if (!aIsDigit && bIsDigit) return -1; // a comes before b
        if (aIsDigit && !bIsDigit) return 1;  // b comes before a
        // both digit-logs: maintain original order (stable sort)
        return 0;
    });
    
    return logs;
};
```

## Typescript

```typescript
function reorderLogFiles(logs: string[]): string[] {
    const letterLogs: string[] = [];
    const digitLogs: string[] = [];

    for (const log of logs) {
        const firstSpace = log.indexOf(' ');
        const rest = log.slice(firstSpace + 1);
        if (rest[0] >= '0' && rest[0] <= '9') {
            digitLogs.push(log);
        } else {
            letterLogs.push(log);
        }
    }

    letterLogs.sort((a, b) => {
        const iA = a.indexOf(' ');
        const iB = b.indexOf(' ');
        const idA = a.slice(0, iA);
        const idB = b.slice(0, iB);
        const contentA = a.slice(iA + 1);
        const contentB = b.slice(iB + 1);

        if (contentA < contentB) return -1;
        if (contentA > contentB) return 1;
        // contents are equal, compare identifiers
        if (idA < idB) return -1;
        if (idA > idB) return 1;
        return 0;
    });

    return [...letterLogs, ...digitLogs];
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $logs
     * @return String[]
     */
    function reorderLogFiles($logs) {
        $letter = [];
        $digit = [];

        foreach ($logs as $log) {
            $pos = strpos($log, ' ');
            $content = substr($log, $pos + 1);
            if (ctype_digit($content[0])) {
                $digit[] = $log;
            } else {
                $letter[] = $log;
            }
        }

        usort($letter, function ($a, $b) {
            $posA = strpos($a, ' ');
            $idA = substr($a, 0, $posA);
            $contentA = substr($a, $posA + 1);

            $posB = strpos($b, ' ');
            $idB = substr($b, 0, $posB);
            $contentB = substr($b, $posB + 1);

            $cmp = strcmp($contentA, $contentB);
            if ($cmp !== 0) {
                return $cmp;
            }
            return strcmp($idA, $idB);
        });

        return array_merge($letter, $digit);
    }
}
```

## Swift

```swift
class Solution {
    func reorderLogFiles(_ logs: [String]) -> [String] {
        var letterLogs: [(id: String, content: String, full: String)] = []
        var digitLogs: [String] = []

        for log in logs {
            guard let spaceIdx = log.firstIndex(of: " ") else { continue }
            let id = String(log[..<spaceIdx])
            let restStart = log.index(after: spaceIdx)
            let content = String(log[restStart...])

            if let firstChar = content.first, firstChar.isNumber {
                digitLogs.append(log)
            } else {
                letterLogs.append((id, content, log))
            }
        }

        letterLogs.sort {
            if $0.content != $1.content {
                return $0.content < $1.content
            } else {
                return $0.id < $1.id
            }
        }

        let orderedLetters = letterLogs.map { $0.full }
        return orderedLetters + digitLogs
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reorderLogFiles(logs: Array<String>): Array<String> {
        return logs.sortedWith { a, b ->
            val partsA = a.split(" ", limit = 2)
            val partsB = b.split(" ", limit = 2)

            val isDigitA = partsA[1][0].isDigit()
            val isDigitB = partsB[1][0].isDigit()

            when {
                !isDigitA && !isDigitB -> {
                    val cmp = partsA[1].compareTo(partsB[1])
                    if (cmp != 0) cmp else partsA[0].compareTo(partsB[0])
                }
                !isDigitA && isDigitB -> -1
                isDigitA && !isDigitB -> 1
                else -> 0 // both digit logs, preserve original order
            }
        }.toTypedArray()
    }
}
```

## Dart

```dart
class Solution {
  List<String> reorderLogFiles(List<String> logs) {
    List<String> letterLogs = [];
    List<String> digitLogs = [];

    for (var log in logs) {
      int idx = log.indexOf(' ');
      String rest = log.substring(idx + 1);
      if (_isDigitLog(rest)) {
        digitLogs.add(log);
      } else {
        letterLogs.add(log);
      }
    }

    letterLogs.sort((a, b) {
      int idxA = a.indexOf(' ');
      int idxB = b.indexOf(' ');
      String idA = a.substring(0, idxA);
      String idB = b.substring(0, idxB);
      String restA = a.substring(idxA + 1);
      String restB = b.substring(idxB + 1);
      int cmp = restA.compareTo(restB);
      if (cmp != 0) return cmp;
      return idA.compareTo(idB);
    });

    return [...letterLogs, ...digitLogs];
  }

  bool _isDigitLog(String content) {
    if (content.isEmpty) return false;
    int code = content.codeUnitAt(0);
    return code >= 48 && code <= 57; // '0'..'9'
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

func reorderLogFiles(logs []string) []string {
	type Log struct {
		raw      string
		id       string
		rest     string
		isLetter bool
	}
	n := len(logs)
	parsed := make([]Log, n)
	for i, log := range logs {
		idx := strings.IndexByte(log, ' ')
		id := log[:idx]
		rest := log[idx+1:]
		isLetter := false
		if len(rest) > 0 {
			c := rest[0]
			if !(c >= '0' && c <= '9') {
				isLetter = true
			}
		}
		parsed[i] = Log{raw: log, id: id, rest: rest, isLetter: isLetter}
	}

	sort.SliceStable(parsed, func(i, j int) bool {
		a := parsed[i]
		b := parsed[j]
		if a.isLetter && !b.isLetter {
			return true
		}
		if !a.isLetter && b.isLetter {
			return false
		}
		if a.isLetter && b.isLetter {
			if a.rest != b.rest {
				return a.rest < b.rest
			}
			return a.id < b.id
		}
		// both digit logs, preserve original order
		return false
	})

	res := make([]string, n)
	for i, p := range parsed {
		res[i] = p.raw
	}
	return res
}
```

## Ruby

```ruby
def reorder_log_files(logs)
  letter_logs = []
  digit_logs = []

  logs.each do |log|
    identifier, rest = log.split(' ', 2)
    if rest[0] =~ /\d/
      digit_logs << log
    else
      letter_logs << [identifier, rest, log]
    end
  end

  letter_logs.sort! do |a, b|
    if a[1] == b[1]
      a[0] <=> b[0]
    else
      a[1] <=> b[1]
    end
  end

  letter_logs.map { |_, _, log| log } + digit_logs
end
```

## Scala

```scala
object Solution {
  def reorderLogFiles(logs: Array[String]): Array[String] = {
    val (letterLogs, digitLogs) = logs.partition { log =>
      val idx = log.indexOf(' ')
      !log.charAt(idx + 1).isDigit
    }

    val sortedLetters = letterLogs.sortWith { (a, b) =>
      val Array(idA, contA) = a.split(" ", 2)
      val Array(idB, contB) = b.split(" ", 2)
      if (contA != contB) contA < contB else idA < idB
    }

    sortedLetters ++ digitLogs
  }
}
```

## Rust

```rust
use std::cmp::Ordering;

fn split_log(log: &str) -> (&str, &str) {
    let i = log.find(' ').unwrap();
    let (id, rest) = log.split_at(i);
    let rest = &rest[1..];
    (id, rest)
}

impl Solution {
    pub fn reorder_log_files(mut logs: Vec<String>) -> Vec<String> {
        logs.sort_by(|a, b| {
            let (id_a, rest_a) = split_log(a);
            let (id_b, rest_b) = split_log(b);
            let a_is_digit = rest_a.as_bytes()[0].is_ascii_digit();
            let b_is_digit = rest_b.as_bytes()[0].is_ascii_digit();

            if !a_is_digit && !b_is_digit {
                match rest_a.cmp(rest_b) {
                    Ordering::Equal => id_a.cmp(id_b),
                    other => other,
                }
            } else if a_is_digit && b_is_digit {
                Ordering::Equal
            } else if !a_is_digit && b_is_digit {
                Ordering::Less
            } else {
                Ordering::Greater
            }
        });
        logs
    }
}
```

## Racket

```racket
#lang racket

(require racket/string)

(define/contract (reorder-log-files logs)
  (-> (listof string?) (listof string?))
  (letrec
      ((letter-log?
        (lambda (log)
          (let* ([pos (string-index-of log #\space)]
                 [rest (substring log (+ pos 1))]
                 [first-char (string-ref rest 0)])
            (not (char-numeric? first-char)))))
       
       (split-log
        (lambda (log)
          (let ([pos (string-index-of log #\space)])
            (values (substring log 0 pos)
                    (substring log (+ pos 1))))))
       
       (letter-compare
        (lambda (a b)
          (call-with-values
              (lambda () (split-log a))
            (lambda (id-a cont-a)
              (call-with-values
                  (lambda () (split-log b))
                (lambda (id-b cont-b)
                  (if (string=? cont-a cont-b)
                      (string<? id-a id-b)
                      (string<? cont-a cont-b)))))))))
       
    (let loop ((remaining logs) (letters '()) (digits '()))
      (cond [(null? remaining)
             (let ([sorted-letters (sort letters letter-compare)])
               (append sorted-letters (reverse digits)))]
            [else
             (let ([log (car remaining)])
               (if (letter-log? log)
                   (loop (cdr remaining) (cons log letters) digits)
                   (loop (cdr remaining) letters (cons log digits))))]))))
```

## Erlang

```erlang
-module(solution).
-export([reorder_log_files/1]).

-spec reorder_log_files(Logs :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
reorder_log_files(Logs) ->
    {LetterTuples, DigitLogs} = split_logs(Logs, [], []),
    SortedLetters = lists:sort(fun compare/2, LetterTuples),
    LetterSorted = [Log || {_Content, _Id, Log} <- SortedLetters],
    LetterSorted ++ DigitLogs.

split_logs([], LettersAcc, DigitsAcc) ->
    {lists:reverse(LettersAcc), lists:reverse(DigitsAcc)};
split_logs([Log | Rest], LettersAcc, DigitsAcc) ->
    case binary:match(Log, <<" ">>) of
        {Pos, _Len} ->
            Identifier = binary:part(Log, 0, Pos),
            ContentStart = Pos + 1,
            ContentSize = byte_size(Log) - ContentStart,
            Content = binary:part(Log, ContentStart, ContentSize),
            case is_digit_log(Content) of
                true -> split_logs(Rest, LettersAcc, [Log | DigitsAcc]);
                false -> split_logs(Rest, [{Content, Identifier, Log} | LettersAcc], DigitsAcc)
            end;
        nomatch ->
            % Should not occur per problem constraints
            split_logs(Rest, LettersAcc, DigitsAcc)
    end.

is_digit_log(Content) ->
    case binary:first(Content) of
        C when C >= $0, C =< $9 -> true;
        _ -> false
    end.

compare({C1, I1, _}, {C2, I2, _}) ->
    if
        C1 < C2 -> true;
        C1 > C2 -> false;
        true -> I1 =< I2
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec reorder_log_files(logs :: [String.t]) :: [String.t]
  def reorder_log_files(logs) do
    {letter_logs, digit_logs} =
      Enum.reduce(logs, {[], []}, fn log, {letters, digits} ->
        if digit_log?(log) do
          {letters, [log | digits]}
        else
          {[log | letters], digits}
        end
      end)

    digit_logs = Enum.reverse(digit_logs)
    letter_logs = Enum.reverse(letter_logs)

    sorted_letters =
      Enum.sort(letter_logs, fn a, b ->
        [id_a, rest_a] = String.split(a, " ", parts: 2)
        [id_b, rest_b] = String.split(b, " ", parts: 2)

        case String.compare(rest_a, rest_b) do
          :lt -> true
          :gt -> false
          :eq ->
            case String.compare(id_a, id_b) do
              :lt -> true
              _ -> false
            end
        end
      end)

    sorted_letters ++ digit_logs
  end

  defp digit_log?(log) do
    [_id, rest] = String.split(log, " ", parts: 2)

    case String.at(rest, 0) do
      nil -> false
      c when c >= "0" and c <= "9" -> true
      _ -> false
    end
  end
end
```
