# 1604. Alert Using Same Key-Card Three or More Times in a One Hour Period

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> alertNames(vector<string>& keyName, vector<string>& keyTime) {
        unordered_map<string, vector<int>> mp;
        int n = keyName.size();
        for (int i = 0; i < n; ++i) {
            const string& name = keyName[i];
            const string& t = keyTime[i];
            int minutes = stoi(t.substr(0,2)) * 60 + stoi(t.substr(3,2));
            mp[name].push_back(minutes);
        }
        vector<string> alerts;
        for (auto& kv : mp) {
            auto& times = kv.second;
            sort(times.begin(), times.end());
            for (int i = 0; i + 2 < (int)times.size(); ++i) {
                if (times[i+2] - times[i] <= 60) {
                    alerts.push_back(kv.first);
                    break;
                }
            }
        }
        sort(alerts.begin(), alerts.end());
        return alerts;
    }
};
```

## Java

```java
class Solution {
    public List<String> alertNames(String[] keyName, String[] keyTime) {
        Map<String, List<Integer>> map = new HashMap<>();
        int n = keyName.length;
        for (int i = 0; i < n; i++) {
            String name = keyName[i];
            String timeStr = keyTime[i];
            int minutes = ((timeStr.charAt(0) - '0') * 10 + (timeStr.charAt(1) - '0')) * 60
                        + (timeStr.charAt(3) - '0') * 10 + (timeStr.charAt(4) - '0');
            map.computeIfAbsent(name, k -> new ArrayList<>()).add(minutes);
        }
        
        Set<String> alertSet = new HashSet<>();
        for (Map.Entry<String, List<Integer>> entry : map.entrySet()) {
            List<Integer> times = entry.getValue();
            Collections.sort(times);
            for (int i = 0; i + 2 < times.size(); i++) {
                if (times.get(i + 2) - times.get(i) <= 60) {
                    alertSet.add(entry.getKey());
                    break;
                }
            }
        }
        
        List<String> result = new ArrayList<>(alertSet);
        Collections.sort(result);
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict

        # Convert times to minutes and group by name
        times_by_name = defaultdict(list)
        for name, t in zip(keyName, keyTime):
            h, m = map(int, t.split(':'))
            minutes = h * 60 + m
            times_by_name[name].append(minutes)

        alerted = set()
        # Check each person's sorted times with sliding window of size 3
        for name, lst in times_by_name.items():
            if len(lst) < 3:
                continue
            lst.sort()
            for i in range(len(lst) - 2):
                if lst[i + 2] - lst[i] <= 60:
                    alerted.add(name)
                    break

        return sorted(alerted)
```

## Python3

```python
from typing import List

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        from collections import defaultdict

        def to_minutes(t: str) -> int:
            h, m = t.split(':')
            return int(h) * 60 + int(m)

        times_by_name = defaultdict(list)
        for name, t in zip(keyName, keyTime):
            times_by_name[name].append(to_minutes(t))

        alerted = []
        for name, minutes in times_by_name.items():
            minutes.sort()
            for i in range(len(minutes) - 2):
                if minutes[i + 2] - minutes[i] <= 60:
                    alerted.append(name)
                    break

        return sorted(alerted)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include "uthash.h"

/* Hash table entry for each person */
typedef struct {
    char *name;          /* key */
    int  *times;         /* dynamic array of minutes */
    int   cnt;           /* number of stored times */
    int   cap;           /* capacity of the array */
    UT_hash_handle hh;   /* makes this structure hashable */
} Person;

/* Comparator for qsort on integers */
static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

/* Comparator for qsort on strings */
static int cmp_str(const void *a, const void *b) {
    const char * const *pa = a;
    const char * const *pb = b;
    return strcmp(*pa, *pb);
}

/* Convert "HH:MM" to minutes since midnight */
static int time_to_min(const char *s) {
    int h = (s[0] - '0') * 10 + (s[1] - '0');
    int m = (s[3] - '0') * 10 + (s[4] - '0');
    return h * 60 + m;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** alertNames(char** keyName, int keyNameSize, char** keyTime, int keyTimeSize, int* returnSize) {
    Person *people = NULL;          /* hash table head */
    for (int i = 0; i < keyNameSize; ++i) {
        const char *name = keyName[i];
        int minutes = time_to_min(keyTime[i]);

        Person *p = NULL;
        HASH_FIND_STR(people, name, p);
        if (!p) {
            p = (Person *)malloc(sizeof(Person));
            p->name = strdup(name);
            p->cnt = 0;
            p->cap = 4;
            p->times = (int *)malloc(p->cap * sizeof(int));
            HASH_ADD_KEYPTR(hh, people, p->name, strlen(p->name), p);
        }
        if (p->cnt == p->cap) {
            p->cap <<= 1;
            p->times = (int *)realloc(p->times, p->cap * sizeof(int));
        }
        p->times[p->cnt++] = minutes;
    }

    /* Prepare result array */
    int distinct = HASH_COUNT(people);
    char **result = (char **)malloc(distinct * sizeof(char *));
    int resCnt = 0;

    Person *p, *tmp;
    HASH_ITER(hh, people, p, tmp) {
        qsort(p->times, p->cnt, sizeof(int), cmp_int);
        for (int i = 0; i + 2 < p->cnt; ++i) {
            if (p->times[i + 2] - p->times[i] <= 60) {
                result[resCnt++] = strdup(p->name);
                break;
            }
        }
    }

    /* Sort the resulting names alphabetically */
    qsort(result, resCnt, sizeof(char *), cmp_str);

    *returnSize = resCnt;

    /* Cleanup hash table (optional for LeetCode) */
    HASH_ITER(hh, people, p, tmp) {
        HASH_DEL(people, p);
        free(p->times);
        free(p->name);
        free(p);
    }

    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<string> AlertNames(string[] keyName, string[] keyTime) {
        var map = new Dictionary<string, List<int>>();
        for (int i = 0; i < keyName.Length; i++) {
            int minutes = ParseMinutes(keyTime[i]);
            if (!map.TryGetValue(keyName[i], out var list)) {
                list = new List<int>();
                map[keyName[i]] = list;
            }
            list.Add(minutes);
        }

        var alerted = new HashSet<string>();
        foreach (var kvp in map) {
            var times = kvp.Value;
            times.Sort();
            for (int i = 0; i + 2 < times.Count; i++) {
                if (times[i + 2] - times[i] <= 60) {
                    alerted.Add(kvp.Key);
                    break;
                }
            }
        }

        var result = alerted.ToList();
        result.Sort(StringComparer.Ordinal);
        return result;
    }

    private int ParseMinutes(string time) {
        // time format "HH:MM"
        int hour = (time[0] - '0') * 10 + (time[1] - '0');
        int minute = (time[3] - '0') * 10 + (time[4] - '0');
        return hour * 60 + minute;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} keyName
 * @param {string[]} keyTime
 * @return {string[]}
 */
var alertNames = function(keyName, keyTime) {
    const map = new Map();
    for (let i = 0; i < keyName.length; ++i) {
        const name = keyName[i];
        const t = keyTime[i];
        const [h, m] = t.split(':');
        const minutes = Number(h) * 60 + Number(m);
        if (!map.has(name)) map.set(name, []);
        map.get(name).push(minutes);
    }
    
    const alerted = [];
    for (const [name, times] of map.entries()) {
        times.sort((a, b) => a - b);
        for (let i = 0; i + 2 < times.length; ++i) {
            if (times[i + 2] - times[i] <= 60) {
                alerted.push(name);
                break;
            }
        }
    }
    
    alerted.sort();
    return alerted;
};
```

## Typescript

```typescript
function alertNames(keyName: string[], keyTime: string[]): string[] {
    const toMinutes = (t: string): number => {
        const [h, m] = t.split(':').map(Number);
        return h * 60 + m;
    };

    const map = new Map<string, number[]>();
    for (let i = 0; i < keyName.length; ++i) {
        const name = keyName[i];
        const time = toMinutes(keyTime[i]);
        if (!map.has(name)) map.set(name, []);
        map.get(name)!.push(time);
    }

    const alerted: string[] = [];
    for (const [name, times] of map.entries()) {
        times.sort((a, b) => a - b);
        for (let i = 0; i + 2 < times.length; ++i) {
            if (times[i + 2] - times[i] <= 60) {
                alerted.push(name);
                break;
            }
        }
    }

    alerted.sort();
    return alerted;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $keyName
     * @param String[] $keyTime
     * @return String[]
     */
    function alertNames($keyName, $keyTime) {
        $map = [];
        $n = count($keyName);
        for ($i = 0; $i < $n; $i++) {
            $name = $keyName[$i];
            $timeStr = $keyTime[$i];
            $hh = intval(substr($timeStr, 0, 2));
            $mm = intval(substr($timeStr, 3, 2));
            $minutes = $hh * 60 + $mm;
            $map[$name][] = $minutes;
        }

        $alert = [];
        foreach ($map as $name => $times) {
            sort($times);
            $len = count($times);
            for ($i = 0; $i + 2 < $len; $i++) {
                if ($times[$i + 2] - $times[$i] <= 60) {
                    $alert[] = $name;
                    break;
                }
            }
        }

        sort($alert, SORT_STRING);
        return $alert;
    }
}
```

## Swift

```swift
class Solution {
    func alertNames(_ keyName: [String], _ keyTime: [String]) -> [String] {
        var userTimes = [String: [Int]]()
        
        for i in 0..<keyName.count {
            let name = keyName[i]
            let timeStr = keyTime[i]
            let parts = timeStr.split(separator: ":")
            let minutes = Int(parts[0])! * 60 + Int(parts[1])!
            userTimes[name, default: []].append(minutes)
        }
        
        var alerted = [String]()
        
        for (name, times) in userTimes {
            if times.count < 3 { continue }
            let sortedTimes = times.sorted()
            var found = false
            for i in 0..<(sortedTimes.count - 2) {
                if sortedTimes[i + 2] - sortedTimes[i] <= 60 {
                    alerted.append(name)
                    found = true
                    break
                }
            }
            if found { continue }
        }
        
        return alerted.sorted()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun alertNames(keyName: Array<String>, keyTime: Array<String>): List<String> {
        val map = HashMap<String, MutableList<Int>>()
        for (i in keyName.indices) {
            val name = keyName[i]
            val t = keyTime[i]
            // parse "HH:MM" without split for speed
            val minutes = ((t[0] - '0') * 10 + (t[1] - '0')) * 60 +
                          ((t[3] - '0') * 10 + (t[4] - '0'))
            map.getOrPut(name) { mutableListOf() }.add(minutes)
        }

        val alerted = mutableListOf<String>()
        for ((name, times) in map) {
            if (times.size < 3) continue
            times.sort()
            var i = 0
            while (i + 2 < times.size) {
                if (times[i + 2] - times[i] <= 60) {
                    alerted.add(name)
                    break
                }
                i++
            }
        }
        return alerted.sorted()
    }
}
```

## Dart

```dart
class Solution {
  List<String> alertNames(List<String> keyName, List<String> keyTime) {
    // Map each name to a list of minutes when the card was used
    final Map<String, List<int>> usage = {};
    for (int i = 0; i < keyName.length; ++i) {
      final String name = keyName[i];
      final String timeStr = keyTime[i];
      final int minutes = _toMinutes(timeStr);
      usage.putIfAbsent(name, () => []).add(minutes);
    }

    final Set<String> alerted = {};

    // Check each person's sorted times for any 3 uses within a 60‑minute window
    usage.forEach((String name, List<int> times) {
      times.sort();
      for (int i = 0; i + 2 < times.length; ++i) {
        if (times[i + 2] - times[i] <= 60) {
          alerted.add(name);
          break;
        }
      }
    });

    final List<String> result = alerted.toList()..sort();
    return result;
  }

  int _toMinutes(String time) {
    // time format "HH:MM"
    final int hour = int.parse(time.substring(0, 2));
    final int minute = int.parse(time.substring(3, 5));
    return hour * 60 + minute;
  }
}
```

## Golang

```go
package main

import (
	"sort"
	"strconv"
	"strings"
)

func alertNames(keyName []string, keyTime []string) []string {
	// Map each name to list of minutes
	userTimes := make(map[string][]int)
	for i, name := range keyName {
		t := keyTime[i]
		parts := strings.Split(t, ":")
		hour, _ := strconv.Atoi(parts[0])
		minute, _ := strconv.Atoi(parts[1])
		total := hour*60 + minute
		userTimes[name] = append(userTimes[name], total)
	}

	alertSet := make(map[string]struct{})
	for name, times := range userTimes {
		if len(times) < 3 {
			continue
		}
		sort.Ints(times)
		for i := 0; i+2 < len(times); i++ {
			if times[i+2]-times[i] <= 60 {
				alertSet[name] = struct{}{}
				break
			}
		}
	}

	result := make([]string, 0, len(alertSet))
	for name := range alertSet {
		result = append(result, name)
	}
	sort.Strings(result)
	return result
}
```

## Ruby

```ruby
def alert_names(key_name, key_time)
  user_times = Hash.new { |h, k| h[k] = [] }

  key_name.each_with_index do |name, idx|
    t = key_time[idx]
    minutes = t[0..1].to_i * 60 + t[3..4].to_i
    user_times[name] << minutes
  end

  alerted = []

  user_times.each do |name, times|
    next if times.size < 3
    times.sort!
    (0..times.size - 3).each do |i|
      if times[i + 2] - times[i] <= 60
        alerted << name
        break
      end
    end
  end

  alerted.sort
end
```

## Scala

```scala
object Solution {
    def alertNames(keyName: Array[String], keyTime: Array[String]): List[String] = {
        import scala.collection.mutable

        val timesByName = mutable.Map[String, mutable.ArrayBuffer[Int]]()
        for (i <- keyName.indices) {
            val name = keyName(i)
            val t = keyTime(i)
            val hour = (t.charAt(0) - '0') * 10 + (t.charAt(1) - '0')
            val minute = (t.charAt(3) - '0') * 10 + (t.charAt(4) - '0')
            val totalMinutes = hour * 60 + minute
            timesByName.getOrElseUpdate(name, mutable.ArrayBuffer[Int]()) += totalMinutes
        }

        val alerted = mutable.ArrayBuffer[String]()
        for ((name, buf) <- timesByName) {
            if (buf.length >= 3) {
                val sortedTimes = buf.sorted
                var i = 0
                var found = false
                while (!found && i + 2 < sortedTimes.length) {
                    if (sortedTimes(i + 2) - sortedTimes(i) <= 60) {
                        alerted += name
                        found = true
                    }
                    i += 1
                }
            }
        }

        alerted.sorted.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn alert_names(key_name: Vec<String>, key_time: Vec<String>) -> Vec<String> {
        use std::collections::{HashMap, BTreeSet};

        let mut map: HashMap<String, Vec<i32>> = HashMap::new();
        for (name, time) in key_name.into_iter().zip(key_time.into_iter()) {
            let parts: Vec<&str> = time.split(':').collect();
            let h: i32 = parts[0].parse().unwrap();
            let m: i32 = parts[1].parse().unwrap();
            let minutes = h * 60 + m;
            map.entry(name).or_default().push(minutes);
        }

        let mut alerts: BTreeSet<String> = BTreeSet::new();

        for (name, mut times) in map {
            if times.len() < 3 {
                continue;
            }
            times.sort_unstable();
            for i in 0..times.len() - 2 {
                if times[i + 2] - times[i] <= 60 {
                    alerts.insert(name);
                    break;
                }
            }
        }

        alerts.into_iter().collect()
    }
}
```

## Racket

```racket
(require racket/hash)

(define (time-to-min t)
  (+ (* (string->number (substring t 0 2)) 60)
     (string->number (substring t 3))))

(define (has-alert? vec)
  (let ([len (vector-length vec)])
    (let loop ((i 0))
      (cond [(> i (- len 3)) #f]
            [(<= (- (vector-ref vec (+ i 2))
                    (vector-ref vec i)) 60) #t]
            [else (loop (+ i 1))]))))

(define/contract (alert-names keyName keyTime)
  (-> (listof string?) (listof string?) (listof string?))
  (let ([ht (make-hash)])
    (for ([name keyName] [t keyTime])
      (define minute (time-to-min t))
      (hash-set! ht name (cons minute (hash-ref ht name null))))
    (define alerts '())
    (for ([pair (in-hash ht)])
      (define name (car pair))
      (define times (sort (cdr pair) <))
      (when (and (>= (length times) 3)
                 (has-alert? (list->vector times)))
        (set! alerts (cons name alerts))))
    (sort alerts string<?)))
```

## Erlang

```erlang
-module(solution).
-export([alert_names/2]).

-spec alert_names(KeyName :: [unicode:unicode_binary()], KeyTime :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
alert_names(KeyName, KeyTime) ->
    Pairs = lists:zip(KeyName, KeyTime),
    NameMap = lists:foldl(fun({Name, TimeStr}, Acc) ->
        Minutes = parse_time(TimeStr),
        Times = maps:get(Name, Acc, []),
        maps:put(Name, [Minutes | Times], Acc)
    end, #{}, Pairs),

    AlertNames = maps:fold(fun(Name, TimesRev, Acc) ->
        Times = lists:sort(TimesRev),
        case has_alert(Times) of
            true -> [Name | Acc];
            false -> Acc
        end
    end, [], NameMap),

    lists:sort(AlertNames).

parse_time(Time) ->
    <<H1, H2, $:, M1, M2>> = Time,
    ((H1 - $0) * 10 + (H2 - $0)) * 60 + ((M1 - $0) * 10 + (M2 - $0)).

has_alert(Times) ->
    has_alert_window(Times).

has_alert_window([A, B, C | Rest]) ->
    if
        C - A =< 60 -> true;
        true -> has_alert_window([B, C | Rest])
    end;
has_alert_window(_) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec alert_names(key_name :: [String.t()], key_time :: [String.t()]) :: [String.t()]
  def alert_names(key_name, key_time) do
    name_times =
      Enum.zip(key_name, key_time)
      |> Enum.reduce(%{}, fn {name, time_str}, acc ->
        minutes = parse_time(time_str)

        Map.update(acc, name, [minutes], fn list -> [minutes | list] end)
      end)

    name_times
    |> Enum.filter(fn {_name, times} ->
      sorted = Enum.sort(times)
      has_three_in_one_hour?(sorted)
    end)
    |> Enum.map(fn {name, _} -> name end)
    |> Enum.sort()
  end

  defp parse_time(<<h::binary-size(2), ?:, m::binary-size(2)>>) do
    String.to_integer(h) * 60 + String.to_integer(m)
  end

  defp has_three_in_one_hour?(times) do
    len = length(times)

    if len < 3 do
      false
    else
      check_triplet(times, 0, len)
    end
  end

  defp check_triplet(_times, i, len) when i > len - 3, do: false

  defp check_triplet(times, i, len) do
    if Enum.at(times, i + 2) - Enum.at(times, i) <= 60 do
      true
    else
      check_triplet(times, i + 1, len)
    end
  end
end
```
