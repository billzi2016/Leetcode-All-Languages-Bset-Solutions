# 2933. High-Access Employees

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> findHighAccessEmployees(vector<vector<string>>& access_times) {
        unordered_map<string, vector<int>> mp;
        for (const auto& rec : access_times) {
            const string& name = rec[0];
            const string& t = rec[1];
            int hour = stoi(t.substr(0, 2));
            int minute = stoi(t.substr(2, 2));
            mp[name].push_back(hour * 60 + minute);
        }
        vector<string> ans;
        for (auto& [name, times] : mp) {
            sort(times.begin(), times.end());
            if (times.size() < 3) continue;
            bool high = false;
            for (size_t i = 0; i + 2 < times.size(); ++i) {
                if (times[i + 2] - times[i] < 60) {
                    high = true;
                    break;
                }
            }
            if (high) ans.push_back(name);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> findHighAccessEmployees(List<List<String>> access_times) {
        Map<String, List<Integer>> map = new HashMap<>();
        for (List<String> entry : access_times) {
            String name = entry.get(0);
            String timeStr = entry.get(1);
            int hour = Integer.parseInt(timeStr.substring(0, 2));
            int minute = Integer.parseInt(timeStr.substring(2, 4));
            int totalMinutes = hour * 60 + minute;
            map.computeIfAbsent(name, k -> new ArrayList<>()).add(totalMinutes);
        }

        List<String> result = new ArrayList<>();
        for (Map.Entry<String, List<Integer>> e : map.entrySet()) {
            List<Integer> times = e.getValue();
            Collections.sort(times);
            boolean high = false;
            for (int i = 0; i + 2 < times.size(); i++) {
                if (times.get(i + 2) - times.get(i) < 60) {
                    high = true;
                    break;
                }
            }
            if (high) {
                result.add(e.getKey());
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findHighAccessEmployees(self, access_times):
        """
        :type access_times: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict

        emp_times = defaultdict(list)
        for name, t in access_times:
            minutes = int(t[:2]) * 60 + int(t[2:])
            emp_times[name].append(minutes)

        high_access = []
        for name, times in emp_times.items():
            if len(times) < 3:
                continue
            times.sort()
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] < 60:
                    high_access.append(name)
                    break

        return high_access
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        emp_times = defaultdict(list)
        for name, t in access_times:
            minutes = int(t[:2]) * 60 + int(t[2:])
            emp_times[name].append(minutes)

        high_access = []
        for name, times in emp_times.items():
            times.sort()
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] < 60:
                    high_access.append(name)
                    break
        return high_access
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *name;
    int *times;
    int cnt;
    int cap;
} Employee;

static int cmp_int(const void *a, const void *b) {
    return (*(int *)a) - (*(int *)b);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findHighAccessEmployees(char*** access_times, int access_timesSize, int* access_timesColSize, int* returnSize) {
    (void)access_timesColSize; // unused
    Employee *emps = NULL;
    int empCap = 0, empCnt = 0;

    for (int i = 0; i < access_timesSize; ++i) {
        char *name = access_times[i][0];
        char *tstr = access_times[i][1];

        int hour = (tstr[0] - '0') * 10 + (tstr[1] - '0');
        int minute = (tstr[2] - '0') * 10 + (tstr[3] - '0');
        int totalMin = hour * 60 + minute;

        // find employee
        int idx = -1;
        for (int j = 0; j < empCnt; ++j) {
            if (strcmp(emps[j].name, name) == 0) {
                idx = j;
                break;
            }
        }
        if (idx == -1) {
            // add new employee
            if (empCnt == empCap) {
                empCap = empCap ? empCap * 2 : 4;
                emps = realloc(emps, empCap * sizeof(Employee));
            }
            idx = empCnt++;
            emps[idx].name = strdup(name);
            emps[idx].cnt = 0;
            emps[idx].cap = 4;
            emps[idx].times = malloc(emps[idx].cap * sizeof(int));
        }

        // add time
        Employee *e = &emps[idx];
        if (e->cnt == e->cap) {
            e->cap *= 2;
            e->times = realloc(e->times, e->cap * sizeof(int));
        }
        e->times[e->cnt++] = totalMin;
    }

    char **result = malloc(empCnt * sizeof(char*));
    int resIdx = 0;

    for (int i = 0; i < empCnt; ++i) {
        Employee *e = &emps[i];
        qsort(e->times, e->cnt, sizeof(int), cmp_int);
        int high = 0;
        for (int j = 0; j + 2 < e->cnt; ++j) {
            if (e->times[j + 2] - e->times[j] < 60) {
                high = 1;
                break;
            }
        }
        if (high) {
            result[resIdx++] = e->name; // reuse allocated name
        } else {
            free(e->name);
        }
        free(e->times);
    }

    free(emps);
    *returnSize = resIdx;
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> FindHighAccessEmployees(IList<IList<string>> access_times) {
        var dict = new Dictionary<string, List<int>>();
        foreach (var entry in access_times) {
            string name = entry[0];
            string t = entry[1];
            int hour = (t[0] - '0') * 10 + (t[1] - '0');
            int minute = (t[2] - '0') * 10 + (t[3] - '0');
            int totalMinutes = hour * 60 + minute;
            if (!dict.ContainsKey(name)) dict[name] = new List<int>();
            dict[name].Add(totalMinutes);
        }

        var result = new List<string>();
        foreach (var kvp in dict) {
            var times = kvp.Value;
            times.Sort();
            for (int i = 0; i + 2 < times.Count; ++i) {
                if (times[i + 2] - times[i] < 60) {
                    result.Add(kvp.Key);
                    break;
                }
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[][]} access_times
 * @return {string[]}
 */
var findHighAccessEmployees = function(access_times) {
    const empMap = new Map();
    for (const [name, timeStr] of access_times) {
        const minutes = parseInt(timeStr.slice(0, 2), 10) * 60 + parseInt(timeStr.slice(2), 10);
        if (!empMap.has(name)) empMap.set(name, []);
        empMap.get(name).push(minutes);
    }
    const result = [];
    for (const [name, times] of empMap.entries()) {
        times.sort((a, b) => a - b);
        for (let i = 0; i + 2 < times.length; ++i) {
            if (times[i + 2] - times[i] < 60) {
                result.push(name);
                break;
            }
        }
    }
    return result;
};
```

## Typescript

```typescript
function findHighAccessEmployees(access_times: string[][]): string[] {
    const employeeMap = new Map<string, number[]>();
    for (const [name, timeStr] of access_times) {
        const hour = parseInt(timeStr.slice(0, 2), 10);
        const minute = parseInt(timeStr.slice(2), 10);
        const totalMinutes = hour * 60 + minute;
        if (!employeeMap.has(name)) employeeMap.set(name, []);
        employeeMap.get(name)!.push(totalMinutes);
    }

    const result: string[] = [];
    for (const [name, times] of employeeMap.entries()) {
        times.sort((a, b) => a - b);
        for (let i = 0; i + 2 < times.length; i++) {
            if (times[i + 2] - times[i] < 60) {
                result.push(name);
                break;
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
     * @param String[][] $access_times
     * @return String[]
     */
    function findHighAccessEmployees($access_times) {
        $map = [];
        foreach ($access_times as $entry) {
            [$name, $timeStr] = $entry;
            $hour = intval(substr($timeStr, 0, 2));
            $minute = intval(substr($timeStr, 2, 2));
            $total = $hour * 60 + $minute;
            if (!isset($map[$name])) {
                $map[$name] = [];
            }
            $map[$name][] = $total;
        }

        $result = [];

        foreach ($map as $name => $times) {
            sort($times, SORT_NUMERIC);
            $n = count($times);
            $i = 0;
            for ($j = 0; $j < $n; $j++) {
                while ($times[$j] - $times[$i] >= 60) {
                    $i++;
                }
                if ($j - $i + 1 >= 3) {
                    $result[] = $name;
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
    func findHighAccessEmployees(_ access_times: [[String]]) -> [String] {
        var dict = [String: [Int]]()
        
        for entry in access_times {
            let name = entry[0]
            let timeStr = entry[1]
            let hour = Int(timeStr.prefix(2))!
            let minute = Int(timeStr.suffix(2))!
            let totalMinutes = hour * 60 + minute
            dict[name, default: []].append(totalMinutes)
        }
        
        var result = [String]()
        
        for (name, var times) in dict {
            if times.count < 3 { continue }
            times.sort()
            for i in 0..<(times.count - 2) {
                if times[i + 2] - times[i] < 60 {
                    result.append(name)
                    break
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
    fun findHighAccessEmployees(access_times: List<List<String>>): List<String> {
        val map = mutableMapOf<String, MutableList<Int>>()
        for (entry in access_times) {
            val name = entry[0]
            val timeStr = entry[1]
            val minutes = (timeStr.substring(0, 2).toInt() * 60) + timeStr.substring(2, 4).toInt()
            map.computeIfAbsent(name) { mutableListOf() }.add(minutes)
        }
        val result = mutableListOf<String>()
        for ((name, timesList) in map) {
            if (timesList.size < 3) continue
            timesList.sort()
            var i = 0
            for (j in timesList.indices) {
                while (i <= j && timesList[j] - timesList[i] >= 60) {
                    i++
                }
                if (j - i + 1 >= 3) {
                    result.add(name)
                    break
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
  List<String> findHighAccessEmployees(List<List<String>> access_times) {
    final Map<String, List<int>> employeeTimes = {};
    for (var entry in access_times) {
      final String name = entry[0];
      final String timeStr = entry[1];
      final int minutes =
          int.parse(timeStr.substring(0, 2)) * 60 + int.parse(timeStr.substring(2));
      employeeTimes.putIfAbsent(name, () => []).add(minutes);
    }

    final List<String> result = [];
    for (var e in employeeTimes.entries) {
      final List<int> times = e.value;
      times.sort();
      for (int i = 0; i + 2 < times.length; ++i) {
        if (times[i + 2] - times[i] < 60) {
          result.add(e.key);
          break;
        }
      }
    }

    return result;
  }
}
```

## Golang

```go
import (
	"sort"
	"strconv"
)

func findHighAccessEmployees(access_times [][]string) []string {
	nameToTimes := make(map[string][]int)
	for _, entry := range access_times {
		name := entry[0]
		tStr := entry[1]
		hour, _ := strconv.Atoi(tStr[:2])
		minute, _ := strconv.Atoi(tStr[2:])
		total := hour*60 + minute
		nameToTimes[name] = append(nameToTimes[name], total)
	}

	var result []string
	for name, times := range nameToTimes {
		if len(times) < 3 {
			continue
		}
		sort.Ints(times)
		for i := 0; i+2 < len(times); i++ {
			if times[i+2]-times[i] < 60 {
				result = append(result, name)
				break
			}
		}
	}
	return result
}
```

## Ruby

```ruby
def find_high_access_employees(access_times)
  groups = Hash.new { |h, k| h[k] = [] }
  access_times.each do |name, time_str|
    minutes = time_str[0..1].to_i * 60 + time_str[2..3].to_i
    groups[name] << minutes
  end

  result = []
  groups.each do |name, times|
    next if times.size < 3
    times.sort!
    (0..times.size - 3).each do |i|
      if times[i + 2] - times[i] < 60
        result << name
        break
      end
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def findHighAccessEmployees(access_times: List[List[String]]): List[String] = {
        import scala.collection.mutable.{Map => MutableMap, ArrayBuffer, Set => MutableSet}
        val employeeTimes = MutableMap.empty[String, ArrayBuffer[Int]]
        for (entry <- access_times) {
            val name = entry(0)
            val t = entry(1)
            val hour = t.substring(0, 2).toInt
            val minute = t.substring(2, 4).toInt
            val total = hour * 60 + minute
            employeeTimes.getOrElseUpdate(name, ArrayBuffer.empty[Int]) += total
        }

        val highAccess = MutableSet.empty[String]

        for ((name, buf) <- employeeTimes) {
            val times = buf.sorted
            var i = 0
            while (i + 2 < times.length && !highAccess.contains(name)) {
                if (times(i + 2) - times(i) < 60) {
                    highAccess += name
                } else {
                    i += 1
                }
            }
        }

        highAccess.toList
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn find_high_access_employees(access_times: Vec<Vec<String>>) -> Vec<String> {
        fn parse_time(s: &str) -> i32 {
            let hour: i32 = s[0..2].parse().unwrap();
            let minute: i32 = s[2..4].parse().unwrap();
            hour * 60 + minute
        }

        let mut map: HashMap<String, Vec<i32>> = HashMap::new();

        for entry in access_times.iter() {
            let name = &entry[0];
            let time_str = &entry[1];
            let t = parse_time(time_str);
            map.entry(name.clone()).or_default().push(t);
        }

        let mut result: Vec<String> = Vec::new();

        for (name, times) in map.iter_mut() {
            if times.len() < 3 {
                continue;
            }
            times.sort_unstable();
            let len = times.len();
            for i in 0..len - 2 {
                if times[i + 2] - times[i] < 60 {
                    result.push(name.clone());
                    break;
                }
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (find-high-access-employees access_times)
  (-> (listof (listof string?)) (listof string?))
  (let ([tbl (make-hash)])
    ;; group minutes per employee
    (for-each
     (lambda (pair)
       (let* ([name (list-ref pair 0)]
              [time (list-ref pair 1)]
              [hour (string->number (substring time 0 2))]
              [minute (string->number (substring time 2 4))]
              [mins (+ (* hour 60) minute)])
         (hash-update! tbl name (lambda (lst) (cons mins lst)) '())))
     access_times)
    ;; collect high‑access employees
    (let loop ((names (hash-keys tbl)) (acc '()))
      (if (null? names)
          (reverse acc)
          (let* ([name (car names)]
                 [times (sort (hash-ref tbl name) <)])
            (if (and (>= (length times) 3)
                     (let inner ((i 0))
                       (cond
                         [(> (+ i 2) (- (length times) 1)) #f]
                         [(< (- (list-ref times (+ i 2))
                                (list-ref times i)) 60) #t]
                         [else (inner (+ i 1))])))
                (loop (cdr names) (cons name acc))
                (loop (cdr names) acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_high_access_employees/1]).

-spec find_high_access_employees(Access_times :: [[unicode:unicode_binary()]]) ->
    [unicode:unicode_binary()].
find_high_access_employees(Access_times) ->
    NameMap = lists:foldl(
        fun([Name, TimeStr], Acc) ->
            TimeInt = time_to_int(TimeStr),
            Updated = [TimeInt | maps:get(Name, Acc, [])],
            maps:put(Name, Updated, Acc)
        end,
        #{},
        Access_times),

    maps:fold(
        fun(Name, TimesRev, Res) ->
            Sorted = lists:sort(TimesRev),
            case has_three_within_one_hour(Sorted) of
                true -> [Name | Res];
                false -> Res
            end
        end,
        [],
        NameMap).

time_to_int(TimeStr) when is_binary(TimeStr) ->
    <<H1, H2, M1, M2>> = TimeStr,
    Hour = (H1 - $0) * 10 + (H2 - $0),
    Min = (M1 - $0) * 10 + (M2 - $0),
    Hour * 60 + Min.

has_three_within_one_hour(Times) ->
    case length(Times) >= 3 of
        true -> check_window(Times);
        false -> false
    end.

check_window([A, _, C | Rest]) when C - A < 60 -> true;
check_window([_, B, C | Rest]) -> check_window([B, C | Rest]);
check_window(_) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_high_access_employees(access_times :: [[String.t]]) :: [String.t]
  def find_high_access_employees(access_times) do
    name_to_times =
      Enum.reduce(access_times, %{}, fn [name, time_str], acc ->
        minutes = parse_time(time_str)
        Map.update(acc, name, [minutes], &[minutes | &1])
      end)

    Enum.reduce(name_to_times, [], fn {name, times}, res ->
      sorted = Enum.sort(times)

      if three_within_one_hour?(sorted) do
        [name | res]
      else
        res
      end
    end)
  end

  defp parse_time(<<h1, h2, m1, m2>>),
    do: (String.to_integer(<<h1, h2>>) * 60) + String.to_integer(<<m1, m2>>)

  defp three_within_one_hour?(times) when length(times) < 3, do: false

  defp three_within_one_hour?(times) do
    len = length(times)

    Enum.any?(0..(len - 3), fn i ->
      Enum.at(times, i + 2) - Enum.at(times, i) < 60
    end)
  end
end
```
