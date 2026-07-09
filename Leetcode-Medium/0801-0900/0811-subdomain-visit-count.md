# 0811. Subdomain Visit Count

## Cpp

```cpp
class Solution {
public:
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        unordered_map<string, long long> cntMap;
        for (const string& entry : cpdomains) {
            size_t spacePos = entry.find(' ');
            int count = stoi(entry.substr(0, spacePos));
            const string& domain = entry.substr(spacePos + 1);
            for (size_t i = 0; i < domain.size(); ++i) {
                if (i == 0 || domain[i - 1] == '.') {
                    cntMap[domain.substr(i)] += count;
                }
            }
        }
        vector<string> result;
        result.reserve(cntMap.size());
        for (const auto& kv : cntMap) {
            result.push_back(to_string(kv.second) + " " + kv.first);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<String> subdomainVisits(String[] cpdomains) {
        java.util.Map<String, Integer> countMap = new java.util.HashMap<>();
        for (String cp : cpdomains) {
            int spaceIdx = cp.indexOf(' ');
            int cnt = Integer.parseInt(cp.substring(0, spaceIdx));
            String domain = cp.substring(spaceIdx + 1);
            String[] parts = domain.split("\\.");
            String sub = "";
            for (int i = parts.length - 1; i >= 0; --i) {
                if (sub.isEmpty()) {
                    sub = parts[i];
                } else {
                    sub = parts[i] + "." + sub;
                }
                countMap.put(sub, countMap.getOrDefault(sub, 0) + cnt);
            }
        }
        java.util.List<String> result = new java.util.ArrayList<>();
        for (java.util.Map.Entry<String, Integer> entry : countMap.entrySet()) {
            result.add(entry.getValue() + " " + entry.getKey());
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counts = {}
        for entry in cpdomains:
            cnt_str, domain = entry.split()
            cnt = int(cnt_str)
            parts = domain.split('.')
            for i in range(len(parts)):
                sub = '.'.join(parts[i:])
                counts[sub] = counts.get(sub, 0) + cnt
        return [f"{c} {d}" for d, c in counts.items()]
```

## Python3

```python
from collections import defaultdict
from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)
        for entry in cpdomains:
            cnt_str, domain = entry.split()
            cnt = int(cnt_str)
            parts = domain.split('.')
            for i in range(len(parts)):
                sub = '.'.join(parts[i:])
                counts[sub] += cnt
        return [f"{cnt} {dom}" for dom, cnt in counts.items()]
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** subdomainVisits(char** cpdomains, int cpdomainsSize, int* returnSize) {
    typedef struct {
        char *key;
        int val;
    } Entry;

    int cap = 128;
    Entry *entries = (Entry *)malloc(cap * sizeof(Entry));
    int sz = 0;

    for (int i = 0; i < cpdomainsSize; ++i) {
        char *space = strchr(cpdomains[i], ' ');
        if (!space) continue;
        int cnt = atoi(cpdomains[i]);
        char *domainStart = space + 1;

        char buf[128];
        strncpy(buf, domainStart, sizeof(buf) - 1);
        buf[sizeof(buf) - 1] = '\0';

        char *sub = buf;
        while (1) {
            // add cnt to map for sub
            int found = 0;
            for (int j = 0; j < sz; ++j) {
                if (strcmp(entries[j].key, sub) == 0) {
                    entries[j].val += cnt;
                    found = 1;
                    break;
                }
            }
            if (!found) {
                if (sz == cap) {
                    cap <<= 1;
                    entries = (Entry *)realloc(entries, cap * sizeof(Entry));
                }
                entries[sz].key = strdup(sub);
                entries[sz].val = cnt;
                ++sz;
            }

            char *dot = strchr(sub, '.');
            if (!dot) break;
            sub = dot + 1;
        }
    }

    char **result = (char **)malloc(sz * sizeof(char *));
    for (int i = 0; i < sz; ++i) {
        int needed = snprintf(NULL, 0, "%d %s", entries[i].val, entries[i].key);
        result[i] = (char *)malloc(needed + 1);
        sprintf(result[i], "%d %s", entries[i].val, entries[i].key);
        free(entries[i].key); // clean up key strings
    }
    free(entries);

    *returnSize = sz;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution
{
    public IList<string> SubdomainVisits(string[] cpdomains)
    {
        var counts = new Dictionary<string, int>();
        foreach (var entry in cpdomains)
        {
            int spaceIdx = entry.IndexOf(' ');
            int cnt = int.Parse(entry.Substring(0, spaceIdx));
            string domain = entry.Substring(spaceIdx + 1);
            var parts = domain.Split('.');

            for (int i = 0; i < parts.Length; i++)
            {
                string sub = string.Join(".", parts, i, parts.Length - i);
                if (counts.ContainsKey(sub))
                    counts[sub] += cnt;
                else
                    counts[sub] = cnt;
            }
        }

        var result = new List<string>();
        foreach (var kvp in counts)
        {
            result.Add($"{kvp.Value} {kvp.Key}");
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} cpdomains
 * @return {string[]}
 */
var subdomainVisits = function(cpdomains) {
    const counts = new Map();
    
    for (const entry of cpdomains) {
        const [cntStr, domain] = entry.split(' ');
        const cnt = parseInt(cntStr, 10);
        let cur = domain;
        while (true) {
            counts.set(cur, (counts.get(cur) || 0) + cnt);
            const dotIdx = cur.indexOf('.');
            if (dotIdx === -1) break;
            cur = cur.substring(dotIdx + 1);
        }
    }
    
    const result = [];
    for (const [dom, cnt] of counts.entries()) {
        result.push(`${cnt} ${dom}`);
    }
    return result;
};
```

## Typescript

```typescript
function subdomainVisits(cpdomains: string[]): string[] {
    const counts = new Map<string, number>();
    for (const entry of cpdomains) {
        const [cntStr, domain] = entry.split(' ');
        const cnt = Number(cntStr);
        const parts = domain.split('.');
        for (let i = 0; i < parts.length; i++) {
            const sub = parts.slice(i).join('.');
            counts.set(sub, (counts.get(sub) ?? 0) + cnt);
        }
    }
    const result: string[] = [];
    for (const [sub, cnt] of counts.entries()) {
        result.push(`${cnt} ${sub}`);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $cpdomains
     * @return String[]
     */
    function subdomainVisits($cpdomains) {
        $counts = [];
        foreach ($cpdomains as $entry) {
            [$cntStr, $domain] = explode(' ', $entry);
            $cnt = intval($cntStr);
            $parts = explode('.', $domain);
            $len = count($parts);
            for ($i = 0; $i < $len; $i++) {
                $sub = implode('.', array_slice($parts, $i));
                if (!isset($counts[$sub])) {
                    $counts[$sub] = 0;
                }
                $counts[$sub] += $cnt;
            }
        }
        $result = [];
        foreach ($counts as $sub => $cnt) {
            $result[] = $cnt . ' ' . $sub;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func subdomainVisits(_ cpdomains: [String]) -> [String] {
        var counts = [String: Int]()
        
        for entry in cpdomains {
            let parts = entry.split(separator: " ")
            guard parts.count == 2,
                  let cnt = Int(parts[0]) else { continue }
            let domain = String(parts[1])
            let fragments = domain.split(separator: ".")
            
            for i in 0..<fragments.count {
                let subdomain = fragments[i...].joined(separator: ".")
                counts[subdomain, default: 0] += cnt
            }
        }
        
        return counts.map { "\($0.value) \($0.key)" }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun subdomainVisits(cpdomains: Array<String>): List<String> {
        val counts = HashMap<String, Int>()
        for (cp in cpdomains) {
            val parts = cp.split(" ")
            val cnt = parts[0].toInt()
            val domain = parts[1]
            val fragments = domain.split(".")
            var sub = ""
            for (i in fragments.indices.reversed()) {
                sub = if (sub.isEmpty()) fragments[i] else "${fragments[i]}.$sub"
                counts[sub] = counts.getOrDefault(sub, 0) + cnt
            }
        }
        val result = ArrayList<String>()
        for ((d, c) in counts) {
            result.add("$c $d")
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> subdomainVisits(List<String> cpdomains) {
    final Map<String, int> counts = {};
    for (var cp in cpdomains) {
      final spaceIdx = cp.indexOf(' ');
      final cnt = int.parse(cp.substring(0, spaceIdx));
      final domain = cp.substring(spaceIdx + 1);
      final parts = domain.split('.');
      for (int i = 0; i < parts.length; ++i) {
        final sub = parts.sublist(i).join('.');
        counts[sub] = (counts[sub] ?? 0) + cnt;
      }
    }
    return counts.entries.map((e) => '${e.value} ${e.key}').toList();
  }
}
```

## Golang

```go
import (
	"fmt"
	"strconv"
	"strings"
)

func subdomainVisits(cpdomains []string) []string {
	counts := make(map[string]int)
	for _, cp := range cpdomains {
		parts := strings.SplitN(cp, " ", 2)
		cnt, _ := strconv.Atoi(parts[0])
		domain := parts[1]
		frags := strings.Split(domain, ".")
		for i := 0; i < len(frags); i++ {
			sub := strings.Join(frags[i:], ".")
			counts[sub] += cnt
		}
	}
	res := make([]string, 0, len(counts))
	for d, c := range counts {
		res = append(res, fmt.Sprintf("%d %s", c, d))
	}
	return res
}
```

## Ruby

```ruby
def subdomain_visits(cpdomains)
  counts = Hash.new(0)
  cpdomains.each do |entry|
    count_str, domain = entry.split(' ')
    cnt = count_str.to_i
    cur = domain
    loop do
      counts[cur] += cnt
      dot_idx = cur.index('.')
      break unless dot_idx
      cur = cur[(dot_idx + 1)..-1]
    end
  end
  counts.map { |d, c| "#{c} #{d}" }
end
```

## Scala

```scala
object Solution {
    def subdomainVisits(cpdomains: Array[String]): List[String] = {
        val counts = scala.collection.mutable.Map[String, Int]()
        for (cp <- cpdomains) {
            val parts = cp.split(" ")
            val cnt = parts(0).toInt
            val domainParts = parts(1).split("\\.")
            for (i <- domainParts.indices) {
                val sub = domainParts.slice(i, domainParts.length).mkString(".")
                counts(sub) = counts.getOrElse(sub, 0) + cnt
            }
        }
        counts.map { case (sub, cnt) => s"$cnt $sub" }.toList
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn subdomain_visits(cpdomains: Vec<String>) -> Vec<String> {
        let mut counts: HashMap<String, i32> = HashMap::new();
        for cp in cpdomains {
            let (cnt_str, domain) = cp.split_once(' ').unwrap();
            let cnt: i32 = cnt_str.parse().unwrap();
            let parts: Vec<&str> = domain.split('.').collect();
            for i in 0..parts.len() {
                let sub = parts[i..].join(".");
                *counts.entry(sub).or_insert(0) += cnt;
            }
        }
        counts.into_iter()
            .map(|(d, c)| format!("{} {}", c, d))
            .collect()
    }
}
```

## Racket

```racket
#lang racket

(require racket/string
         racket/list)

(define/contract (subdomain-visits cpdomains)
  (-> (listof string?) (listof string?))
  (let ([counts (make-hash)])
    (for ([entry cpdomains])
      (define parts (string-split entry)) ; ["count" "domain"]
      (define cnt   (string->number (first parts)))
      (define domain (second parts))
      (define frags (string-split domain "."))
      (for ([i (in-range (length frags))])
        (define sub (string-join (drop frags i) "."))
        (hash-set! counts sub (+ cnt (hash-ref counts sub 0)))))
    (map (lambda (kv)
           (format "~a ~a" (cdr kv) (car kv)))
         (hash->list counts))))
```

## Erlang

```erlang
-module(solution).
-export([subdomain_visits/1]).

-spec subdomain_visits(Cpdomains :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
subdomain_visits(Cpdomains) ->
    Map = lists:foldl(fun process_cp/2, #{}, Cpdomains),
    maps:fold(
        fun(Domain, Count, Acc) ->
            CntBin = integer_to_binary(Count),
            [<<CntBin/binary, $ , Domain/binary>> | Acc]
        end,
        [],
        Map).

process_cp(Cp, AccMap) ->
    [CntBin, Domain] = binary:split(Cp, <<" ">>, []),
    Count = binary_to_integer(CntBin),
    Frags = binary:split(Domain, <<".">>, [global]),
    RevFrags = lists:reverse(Frags),
    {_, NewMap} = lists:foldl(
        fun(Frag, {AccBin, M}) ->
            NewBin = case AccBin of
                        <<>> -> Frag;
                        _ -> <<Frag/binary, $., AccBin/binary>>
                     end,
            UpdatedM = maps:update_with(NewBin, fun(V) -> V + Count end, Count, M),
            {NewBin, UpdatedM}
        end,
        {<<>>, AccMap},
        RevFrags
    ),
    NewMap.
```

## Elixir

```elixir
defmodule Solution do
  @spec subdomain_visits(cpdomains :: [String.t]) :: [String.t]
  def subdomain_visits(cpdomains) do
    counts =
      Enum.reduce(cpdomains, %{}, fn entry, acc ->
        [cnt_str, domain] = String.split(entry, " ")
        cnt = String.to_integer(cnt_str)
        parts = String.split(domain, ".")

        Enum.reduce(0..(length(parts) - 1), acc, fn i, inner_acc ->
          subdomain = parts |> Enum.slice(i, length(parts) - i) |> Enum.join(".")
          Map.update(inner_acc, subdomain, cnt, &(&1 + cnt))
        end)
      end)

    Enum.map(counts, fn {subdomain, cnt} -> "#{cnt} #{subdomain}" end)
  end
end
```
