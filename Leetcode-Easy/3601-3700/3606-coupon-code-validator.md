# 3606. Coupon Code Validator

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> validateCoupons(vector<string>& code, vector<string>& businessLine, vector<bool>& isActive) {
        unordered_map<string,int> order = {
            {"electronics",0},
            {"grocery",1},
            {"pharmacy",2},
            {"restaurant",3}
        };
        vector<pair<int,string>> valid;
        int n = code.size();
        for (int i = 0; i < n; ++i) {
            if (!isActive[i]) continue;
            const string& c = code[i];
            if (c.empty()) continue;
            bool ok = true;
            for (unsigned char ch : c) {
                if (!(isalnum(ch) || ch == '_')) { ok = false; break; }
            }
            if (!ok) continue;
            auto it = order.find(businessLine[i]);
            if (it == order.end()) continue;
            valid.emplace_back(it->second, c);
        }
        sort(valid.begin(), valid.end(), [](const pair<int,string>& a, const pair<int,string>& b){
            if (a.first != b.first) return a.first < b.first;
            return a.second < b.second;
        });
        vector<string> res;
        res.reserve(valid.size());
        for (auto& p : valid) res.push_back(p.second);
        return res;
    }
};
```

## Java

```java
class Solution {
    public List<String> validateCoupons(String[] code, String[] businessLine, boolean[] isActive) {
        int n = code.length;
        // Define priority order
        java.util.Map<String, Integer> priority = new java.util.HashMap<>();
        priority.put("electronics", 0);
        priority.put("grocery", 1);
        priority.put("pharmacy", 2);
        priority.put("restaurant", 3);

        List<Coupon> valid = new java.util.ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (!isActive[i]) continue;
            String c = code[i];
            if (c == null || c.isEmpty()) continue;
            if (!c.matches("[A-Za-z0-9_]+")) continue;
            String bl = businessLine[i];
            if (!priority.containsKey(bl)) continue;
            valid.add(new Coupon(bl, c));
        }

        java.util.Collections.sort(valid, (a, b) -> {
            int p1 = priority.get(a.business);
            int p2 = priority.get(b.business);
            if (p1 != p2) return Integer.compare(p1, p2);
            return a.code.compareTo(b.code);
        });

        List<String> result = new java.util.ArrayList<>();
        for (Coupon cp : valid) {
            result.add(cp.code);
        }
        return result;
    }

    private static class Coupon {
        String business;
        String code;
        Coupon(String business, String code) {
            this.business = business;
            this.code = code;
        }
    }
}
```

## Python

```python
class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        allowed = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        valid = []
        for c, b, a in zip(code, businessLine, isActive):
            if not a:
                continue
            if not c:
                continue
            if any(not (ch.isalnum() or ch == '_') for ch in c):
                continue
            if b not in allowed:
                continue
            valid.append((allowed[b], c))
        valid.sort(key=lambda x: (x[0], x[1]))
        return [c for _, c in valid]
```

## Python3

```python
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        allowed_lines = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        valid = []
        for c, b, act in zip(code, businessLine, isActive):
            if not act:
                continue
            if not c:
                continue
            # check allowed characters: alphanumeric or underscore
            if not all(ch.isalnum() or ch == '_' for ch in c):
                continue
            if b not in allowed_lines:
                continue
            valid.append((allowed_lines[b], c))
        # sort by business line priority then code lexicographically
        valid.sort(key=lambda x: (x[0], x[1]))
        return [c for _, c in valid]
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct {
    char *code;
    int priority;
} Coupon;

static int getPriority(const char *s) {
    if (strcmp(s, "electronics") == 0) return 0;
    if (strcmp(s, "grocery") == 0)     return 1;
    if (strcmp(s, "pharmacy") == 0)   return 2;
    if (strcmp(s, "restaurant") == 0) return 3;
    return -1;
}

static bool isValidCode(const char *s) {
    if (!s || s[0] == '\0') return false;
    for (; *s; ++s) {
        unsigned char c = (unsigned char)*s;
        if (!(isalnum(c) || c == '_')) return false;
    }
    return true;
}

static int cmpCoupon(const void *a, const void *b) {
    const Coupon *ca = (const Coupon *)a;
    const Coupon *cb = (const Coupon *)b;
    if (ca->priority != cb->priority)
        return ca->priority - cb->priority;
    return strcmp(ca->code, cb->code);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** validateCoupons(char** code, int codeSize,
                       char** businessLine, int businessLineSize,
                       bool* isActive, int isActiveSize,
                       int* returnSize) {
    int n = codeSize;  // all sizes are equal per constraints
    Coupon *tmp = (Coupon *)malloc(n * sizeof(Coupon));
    int cnt = 0;

    for (int i = 0; i < n; ++i) {
        if (!isActive[i]) continue;
        if (!isValidCode(code[i])) continue;
        int pr = getPriority(businessLine[i]);
        if (pr == -1) continue;
        tmp[cnt].code = code[i];
        tmp[cnt].priority = pr;
        ++cnt;
    }

    qsort(tmp, cnt, sizeof(Coupon), cmpCoupon);

    char **res = (char **)malloc(cnt * sizeof(char *));
    for (int i = 0; i < cnt; ++i) {
        size_t len = strlen(tmp[i].code);
        res[i] = (char *)malloc((len + 1) * sizeof(char));
        strcpy(res[i], tmp[i].code);
    }

    free(tmp);
    *returnSize = cnt;
    return res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<string> ValidateCoupons(string[] code, string[] businessLine, bool[] isActive) {
        var priority = new Dictionary<string, int>(StringComparer.Ordinal) {
            { "electronics", 0 },
            { "grocery", 1 },
            { "pharmacy", 2 },
            { "restaurant", 3 }
        };

        var valid = new List<(int pri, string cod)>();

        for (int i = 0; i < code.Length; i++) {
            if (!isActive[i]) continue;

            string c = code[i];
            if (string.IsNullOrEmpty(c)) continue;

            bool ok = true;
            foreach (char ch in c) {
                if (!(char.IsLetterOrDigit(ch) || ch == '_')) {
                    ok = false;
                    break;
                }
            }
            if (!ok) continue;

            if (!priority.TryGetValue(businessLine[i], out int pri)) continue;

            valid.Add((pri, c));
        }

        var result = valid
            .OrderBy(p => p.pri)
            .ThenBy(p => p.cod, StringComparer.Ordinal)
            .Select(p => p.cod)
            .ToList();

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} code
 * @param {string[]} businessLine
 * @param {boolean[]} isActive
 * @return {string[]}
 */
var validateCoupons = function(code, businessLine, isActive) {
    const allowedLines = ["electronics", "grocery", "pharmacy", "restaurant"];
    const priority = {
        "electronics": 0,
        "grocery": 1,
        "pharmacy": 2,
        "restaurant": 3
    };
    const valid = [];
    const codePattern = /^[A-Za-z0-9_]+$/;
    
    for (let i = 0; i < code.length; ++i) {
        if (!isActive[i]) continue;
        const c = code[i];
        if (c.length === 0 || !codePattern.test(c)) continue;
        const bl = businessLine[i];
        if (!priority.hasOwnProperty(bl)) continue;
        valid.push({bl, code: c});
    }
    
    valid.sort((a, b) => {
        const pDiff = priority[a.bl] - priority[b.bl];
        if (pDiff !== 0) return pDiff;
        return a.code < b.code ? -1 : a.code > b.code ? 1 : 0;
    });
    
    return valid.map(item => item.code);
};
```

## Typescript

```typescript
function validateCoupons(code: string[], businessLine: string[], isActive: boolean[]): string[] {
    const allowedLines = new Set(["electronics", "grocery", "pharmacy", "restaurant"]);
    const lineOrder: Record<string, number> = {
        electronics: 0,
        grocery: 1,
        pharmacy: 2,
        restaurant: 3
    };
    const valid: { bl: string; cd: string }[] = [];

    const codeRegex = /^[A-Za-z0-9_]+$/;

    for (let i = 0; i < code.length; i++) {
        if (!isActive[i]) continue;
        const c = code[i];
        if (c.length === 0 || !codeRegex.test(c)) continue;
        const bl = businessLine[i];
        if (!allowedLines.has(bl)) continue;
        valid.push({ bl, cd: c });
    }

    valid.sort((a, b) => {
        const diff = lineOrder[a.bl] - lineOrder[b.bl];
        if (diff !== 0) return diff;
        return a.cd < b.cd ? -1 : a.cd > b.cd ? 1 : 0;
    });

    return valid.map(v => v.cd);
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $code
     * @param String[] $businessLine
     * @param Boolean[] $isActive
     * @return String[]
     */
    function validateCoupons($code, $businessLine, $isActive) {
        $order = [
            "electronics" => 0,
            "grocery" => 1,
            "pharmacy" => 2,
            "restaurant" => 3
        ];
        $valid = [];
        $n = count($code);
        for ($i = 0; $i < $n; ++$i) {
            if (!$isActive[$i]) continue;
            $c = $code[$i];
            if ($c === '' || !preg_match('/^[A-Za-z0-9_]+$/', $c)) continue;
            $b = $businessLine[$i];
            if (!isset($order[$b])) continue;
            $valid[] = ['bl' => $b, 'code' => $c];
        }
        usort($valid, function ($a, $b) use ($order) {
            $pa = $order[$a['bl']];
            $pb = $order[$b['bl']];
            if ($pa !== $pb) {
                return $pa <=> $pb;
            }
            return strcmp($a['code'], $b['code']);
        });
        $result = [];
        foreach ($valid as $item) {
            $result[] = $item['code'];
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func validateCoupons(_ code: [String], _ businessLine: [String], _ isActive: [Bool]) -> [String] {
        let priority: [String:Int] = [
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        ]
        let allowedSet = CharacterSet.alphanumerics.union(CharacterSet(charactersIn: "_"))
        var valid: [(Int, String)] = []
        
        for i in 0..<code.count {
            guard isActive[i] else { continue }
            let c = code[i]
            guard !c.isEmpty else { continue }
            // ensure all characters are alphanumeric or underscore
            if c.rangeOfCharacter(from: allowedSet.inverted) != nil { continue }
            guard let pr = priority[businessLine[i]] else { continue }
            valid.append((pr, c))
        }
        
        valid.sort {
            if $0.0 != $1.0 {
                return $0.0 < $1.0
            } else {
                return $0.1 < $1.1
            }
        }
        
        return valid.map { $0.1 }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validateCoupons(code: Array<String>, businessLine: Array<String>, isActive: BooleanArray): List<String> {
        val priority = mapOf(
            "electronics" to 0,
            "grocery" to 1,
            "pharmacy" to 2,
            "restaurant" to 3
        )
        val valid = mutableListOf<Pair<Int, String>>()
        for (i in code.indices) {
            if (!isActive[i]) continue
            val c = code[i]
            if (c.isEmpty()) continue
            var ok = true
            for (ch in c) {
                if (!(ch.isLetterOrDigit() || ch == '_')) {
                    ok = false
                    break
                }
            }
            if (!ok) continue
            val pr = priority[businessLine[i]] ?: continue
            valid.add(pr to c)
        }
        valid.sortWith(compareBy<Pair<Int, String>> { it.first }.thenBy { it.second })
        return valid.map { it.second }
    }
}
```

## Dart

```dart
class _Coupon {
  final String business;
  final String code;
  _Coupon(this.business, this.code);
}

class Solution {
  List<String> validateCoupons(List<String> code, List<String> businessLine, List<bool> isActive) {
    const Map<String, int> order = {
      'electronics': 0,
      'grocery': 1,
      'pharmacy': 2,
      'restaurant': 3
    };
    final RegExp pattern = RegExp(r'^[A-Za-z0-9_]+$');
    List<_Coupon> valid = [];

    for (int i = 0; i < code.length; i++) {
      if (!isActive[i]) continue;
      String c = code[i];
      if (c.isEmpty) continue;
      if (!pattern.hasMatch(c)) continue;
      String b = businessLine[i];
      if (!order.containsKey(b)) continue;
      valid.add(_Coupon(b, c));
    }

    valid.sort((a, b) {
      int cmp = order[a.business]!.compareTo(order[b.business]!);
      if (cmp != 0) return cmp;
      return a.code.compareTo(b.code);
    });

    return valid.map((e) => e.code).toList();
  }
}
```

## Golang

```go
package main

import "sort"

type coupon struct {
	priority int
	code     string
}

func validateCoupons(code []string, businessLine []string, isActive []bool) []string {
	priorityMap := map[string]int{
		"electronics": 0,
		"grocery":     1,
		"pharmacy":    2,
		"restaurant":  3,
	}
	var list []coupon
	for i := 0; i < len(code); i++ {
		if !isActive[i] {
			continue
		}
		c := code[i]
		if len(c) == 0 {
			continue
		}
		valid := true
		for j := 0; j < len(c); j++ {
			ch := c[j]
			if (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || (ch >= '0' && ch <= '9') || ch == '_' {
				continue
			}
			valid = false
			break
		}
		if !valid {
			continue
		}
		bl := businessLine[i]
		p, ok := priorityMap[bl]
		if !ok {
			continue
		}
		list = append(list, coupon{priority: p, code: c})
	}
	sort.Slice(list, func(i, j int) bool {
		if list[i].priority != list[j].priority {
			return list[i].priority < list[j].priority
		}
		return list[i].code < list[j].code
	})
	res := make([]string, len(list))
	for i, v := range list {
		res[i] = v.code
	}
	return res
}
```

## Ruby

```ruby
def validate_coupons(code, business_line, is_active)
  priority = {
    "electronics" => 0,
    "grocery" => 1,
    "pharmacy" => 2,
    "restaurant" => 3
  }

  valid = []
  code.each_index do |i|
    next unless is_active[i]
    next if code[i].empty?
    next unless code[i] =~ /\A\w+\z/
    next unless priority.key?(business_line[i])

    valid << [priority[business_line[i]], code[i]]
  end

  valid.sort_by { |p, c| [p, c] }.map { |_, c| c }
end
```

## Scala

```scala
object Solution {
    def validateCoupons(code: Array[String], businessLine: Array[String], isActive: Array[Boolean]): List[String] = {
        val priority = Map(
            "electronics" -> 0,
            "grocery"     -> 1,
            "pharmacy"    -> 2,
            "restaurant"  -> 3
        )
        val valid = for {
            i <- code.indices
            if isActive(i)
            c = code(i)
            bl = businessLine(i)
            if c.nonEmpty && c.matches("^[A-Za-z0-9_]+$")
            if priority.contains(bl)
        } yield (bl, c)

        valid.sortBy { case (bl, c) => (priority(bl), c) }.map(_._2).toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn validate_coupons(code: Vec<String>, business_line: Vec<String>, is_active: Vec<bool>) -> Vec<String> {
        let mut valid = Vec::new();
        for i in 0..code.len() {
            if !is_active[i] {
                continue;
            }
            let c = &code[i];
            if c.is_empty() {
                continue;
            }
            if !c.chars().all(|ch| ch.is_ascii_alphanumeric() || ch == '_') {
                continue;
            }
            let priority = match business_line[i].as_str() {
                "electronics" => 0,
                "grocery" => 1,
                "pharmacy" => 2,
                "restaurant" => 3,
                _ => continue,
            };
            valid.push((priority, c.clone()));
        }
        valid.sort_by(|a, b| {
            if a.0 != b.0 {
                a.0.cmp(&b.0)
            } else {
                a.1.cmp(&b.1)
            }
        });
        valid.into_iter().map(|(_, code)| code).collect()
    }
}
```

## Racket

```racket
(define/contract (validate-coupons code businessLine isActive)
  (-> (listof string?) (listof string?) (listof boolean?) (listof string?))
  (let* ((allowed-lines '("electronics" "grocery" "pharmacy" "restaurant"))
         (prio (hash "electronics" 0
                     "grocery" 1
                     "pharmacy" 2
                     "restaurant" 3)))
    (define (valid-code? s)
      (and (> (string-length s) 0)
           (for/and ([ch (in-string s)])
             (or (char-alphabetic? ch)
                 (char-numeric? ch)
                 (char=? ch #\_)))))
    (define pairs
      (let loop ((i 0) (acc '()))
        (if (= i (length code))
            (reverse acc)
            (let ((c (list-ref code i))
                  (b (list-ref businessLine i))
                  (a (list-ref isActive i)))
              (if (and a
                       (member b allowed-lines string=?)
                       (valid-code? c))
                  (loop (+ i 1) (cons (list b c) acc))
                  (loop (+ i 1) acc))))))
    (define sorted-pairs
      (sort pairs
            (lambda (p1 p2)
              (let* ((bl1 (first p1))
                     (code1 (second p1))
                     (bl2 (first p2))
                     (code2 (second p2))
                     (pr1 (hash-ref prio bl1))
                     (pr2 (hash-ref prio bl2)))
                (if (= pr1 pr2)
                    (string<? code1 code2)
                    (< pr1 pr2))))))
    (map second sorted-pairs)))
```

## Erlang

```erlang
-module(solution).
-export([validate_coupons/3]).

-spec validate_coupons(Code :: [unicode:unicode_binary()], BusinessLine :: [unicode:unicode_binary()], IsActive :: [boolean()]) -> [unicode:unicode_binary()].
validate_coupons(Code, BusinessLine, IsActive) ->
    Allowed = #{<<"electronics">> => 0,
                <<"grocery">> => 1,
                <<"pharmacy">> => 2,
                <<"restaurant">> => 3},
    Pairs = collect_valid(lists:zip3(Code, BusinessLine, IsActive), Allowed),
    Sorted = lists:sort(Pairs),
    [C || {_P, C} <- Sorted].

collect_valid([], _Allowed) -> [];
collect_valid([{CodeBin,BLineBin,Active}|Rest], Allowed) ->
    case is_valid_coupon(CodeBin, BLineBin, Active, Allowed) of
        true ->
            Priority = maps:get(BLineBin, Allowed),
            [{Priority, CodeBin} | collect_valid(Rest, Allowed)];
        false ->
            collect_valid(Rest, Allowed)
    end.

is_valid_coupon(CodeBin, BLineBin, true, Allowed) ->
    case (byte_size(CodeBin) > 0) andalso maps:is_key(BLineBin, Allowed) of
        true ->
            case re:run(CodeBin, "^[A-Za-z0-9_]+$", [{capture, none}]) of
                match -> true;
                nomatch -> false
            end;
        false -> false
    end;
is_valid_coupon(_, _, _, _) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec validate_coupons(code :: [String.t()], business_line :: [String.t()], is_active :: [boolean]) :: [String.t()]
  def validate_coupons(code, business_line, is_active) do
    priority = %{
      "electronics" => 0,
      "grocery" => 1,
      "pharmacy" => 2,
      "restaurant" => 3
    }

    Enum.zip([code, business_line, is_active])
    |> Enum.filter(fn {c, b, a} ->
      a and
        c != "" and
        Regex.match?(~r/^[A-Za-z0-9_]+$/, c) and
        Map.has_key?(priority, b)
    end)
    |> Enum.sort_by(fn {c, b, _a} -> {Map.get(priority, b), c} end)
    |> Enum.map(fn {c, _b, _a} -> c end)
  end
end
```
