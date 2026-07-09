# 1817. Finding the Users Active Minutes

## Cpp

```cpp
class Solution {
public:
    vector<int> findingUsersActiveMinutes(vector<vector<int>>& logs, int k) {
        unordered_map<int, unordered_set<int>> userTimes;
        for (const auto& log : logs) {
            int id = log[0];
            int t = log[1];
            userTimes[id].insert(t);
        }
        vector<int> answer(k, 0);
        for (auto& [id, times] : userTimes) {
            int uam = static_cast<int>(times.size());
            if (uam >= 1 && uam <= k) {
                answer[uam - 1]++;
            }
        }
        return answer;
    }
};
```

## Java

```java
class Solution {
    public int[] findingUsersActiveMinutes(int[][] logs, int k) {
        java.util.Map<Integer, java.util.Set<Integer>> userMinutes = new java.util.HashMap<>();
        for (int[] log : logs) {
            int id = log[0];
            int time = log[1];
            userMinutes.computeIfAbsent(id, v -> new java.util.HashSet<>()).add(time);
        }
        int[] answer = new int[k];
        for (java.util.Set<Integer> minutes : userMinutes.values()) {
            int uam = minutes.size();
            if (uam >= 1 && uam <= k) {
                answer[uam - 1]++;
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict

        user_minutes = defaultdict(set)
        for uid, minute in logs:
            user_minutes[uid].add(minute)

        ans = [0] * k
        for minutes in user_minutes.values():
            uam = len(minutes)
            if 1 <= uam <= k:
                ans[uam - 1] += 1

        return ans
```

## Python3

```python
from typing import List

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_minutes = {}
        for uid, minute in logs:
            if uid not in user_minutes:
                user_minutes[uid] = set()
            user_minutes[uid].add(minute)
        
        ans = [0] * k
        for minutes in user_minutes.values():
            uam = len(minutes)
            if 1 <= uam <= k:
                ans[uam - 1] += 1
        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int id;
    int time;
} Log;

static int cmpLog(const void *a, const void *b) {
    const Log *la = (const Log *)a;
    const Log *lb = (const Log *)b;
    if (la->id != lb->id)
        return (la->id < lb->id) ? -1 : 1;
    if (la->time != lb->time)
        return (la->time < lb->time) ? -1 : 1;
    return 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findingUsersActiveMinutes(int** logs, int logsSize, int* logsColSize, int k, int* returnSize){
    if (logsSize == 0) {
        *returnSize = k;
        int *ans = calloc(k, sizeof(int));
        return ans;
    }
    
    Log *arr = malloc(logsSize * sizeof(Log));
    for (int i = 0; i < logsSize; ++i) {
        arr[i].id   = logs[i][0];
        arr[i].time = logs[i][1];
    }
    
    qsort(arr, logsSize, sizeof(Log), cmpLog);
    
    int *answer = calloc(k, sizeof(int));
    
    int i = 0;
    while (i < logsSize) {
        int curId = arr[i].id;
        int uam = 0;
        int prevTime = -1; // times are >=1
        while (i < logsSize && arr[i].id == curId) {
            if (arr[i].time != prevTime) {
                ++uam;
                prevTime = arr[i].time;
            }
            ++i;
        }
        if (uam > 0 && uam <= k) {
            answer[uam - 1] += 1;
        }
    }
    
    free(arr);
    *returnSize = k;
    return answer;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[] FindingUsersActiveMinutes(int[][] logs, int k) {
        var userMinutes = new Dictionary<int, HashSet<int>>();
        foreach (var log in logs) {
            int id = log[0];
            int time = log[1];
            if (!userMinutes.TryGetValue(id, out var minutes)) {
                minutes = new HashSet<int>();
                userMinutes[id] = minutes;
            }
            minutes.Add(time);
        }

        int[] answer = new int[k];
        foreach (var minutes in userMinutes.Values) {
            int uam = minutes.Count;
            if (uam >= 1 && uam <= k) {
                answer[uam - 1]++;
            }
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} logs
 * @param {number} k
 * @return {number[]}
 */
var findingUsersActiveMinutes = function(logs, k) {
    const userMap = new Map(); // id -> Set of unique minutes
    for (const [id, time] of logs) {
        if (!userMap.has(id)) {
            userMap.set(id, new Set());
        }
        userMap.get(id).add(time);
    }
    
    const answer = Array(k).fill(0);
    for (const minutesSet of userMap.values()) {
        const uam = minutesSet.size;
        if (uam >= 1 && uam <= k) {
            answer[uam - 1] += 1;
        }
    }
    return answer;
};
```

## Typescript

```typescript
function findingUsersActiveMinutes(logs: number[][], k: number): number[] {
    const userMap = new Map<number, Set<number>>();
    for (const [id, time] of logs) {
        let minutes = userMap.get(id);
        if (!minutes) {
            minutes = new Set<number>();
            userMap.set(id, minutes);
        }
        minutes.add(time);
    }
    const answer = new Array(k).fill(0);
    for (const minutes of userMap.values()) {
        const uam = minutes.size;
        if (uam >= 1 && uam <= k) {
            answer[uam - 1]++;
        }
    }
    return answer;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[][] $logs
     * @param Integer $k
     * @return Integer[]
     */
    function findingUsersActiveMinutes($logs, $k) {
        $userMap = [];
        foreach ($logs as $log) {
            $id = $log[0];
            $time = $log[1];
            if (!isset($userMap[$id])) {
                $userMap[$id] = [];
            }
            $userMap[$id][$time] = true;
        }

        $ans = array_fill(0, $k, 0);
        foreach ($userMap as $times) {
            $cnt = count($times);
            if ($cnt >= 1 && $cnt <= $k) {
                $ans[$cnt - 1]++;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func findingUsersActiveMinutes(_ logs: [[Int]], _ k: Int) -> [Int] {
        var userMap = [Int: Set<Int>]()
        for log in logs {
            let id = log[0]
            let time = log[1]
            userMap[id, default: Set<Int>()].insert(time)
        }
        var answer = Array(repeating: 0, count: k)
        for times in userMap.values {
            let cnt = times.count
            if cnt > 0 && cnt <= k {
                answer[cnt - 1] += 1
            }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findingUsersActiveMinutes(logs: Array<IntArray>, k: Int): IntArray {
        val userMap = HashMap<Int, MutableSet<Int>>()
        for (log in logs) {
            val id = log[0]
            val time = log[1]
            val minutes = userMap.getOrPut(id) { HashSet() }
            minutes.add(time)
        }
        val answer = IntArray(k)
        for (minutes in userMap.values) {
            val uam = minutes.size
            if (uam <= k) {
                answer[uam - 1]++
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> findingUsersActiveMinutes(List<List<int>> logs, int k) {
    final Map<int, Set<int>> userMap = {};
    for (var log in logs) {
      int id = log[0];
      int time = log[1];
      userMap.putIfAbsent(id, () => <int>{}).add(time);
    }
    List<int> ans = List.filled(k, 0);
    for (var minutes in userMap.values) {
      int uam = minutes.length;
      if (uam >= 1 && uam <= k) {
        ans[uam - 1] += 1;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func findingUsersActiveMinutes(logs [][]int, k int) []int {
    userMinutes := make(map[int]map[int]struct{})
    for _, log := range logs {
        id, t := log[0], log[1]
        if _, ok := userMinutes[id]; !ok {
            userMinutes[id] = make(map[int]struct{})
        }
        userMinutes[id][t] = struct{}{}
    }

    ans := make([]int, k)
    for _, minutes := range userMinutes {
        uam := len(minutes)
        if uam >= 1 && uam <= k {
            ans[uam-1]++
        }
    }
    return ans
}
```

## Ruby

```ruby
require 'set'

def finding_users_active_minutes(logs, k)
  user_times = {}
  logs.each do |id, time|
    (user_times[id] ||= Set.new).add(time)
  end

  ans = Array.new(k, 0)
  user_times.each_value do |times|
    uam = times.size
    ans[uam - 1] += 1 if uam <= k
  end
  ans
end
```

## Scala

```scala
object Solution {
    def findingUsersActiveMinutes(logs: Array[Array[Int]], k: Int): Array[Int] = {
        import scala.collection.mutable
        val userMap = mutable.Map[Int, mutable.Set[Int]]()
        for (log <- logs) {
            val id = log(0)
            val time = log(1)
            val set = userMap.getOrElseUpdate(id, mutable.Set[Int]())
            set += time
        }
        val ans = Array.fill(k)(0)
        for ((_, minutes) <- userMap) {
            val uam = minutes.size
            if (uam >= 1 && uam <= k) ans(uam - 1) += 1
        }
        ans
    }
}
```

## Rust

```rust
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn finding_users_active_minutes(logs: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let mut user_minutes: HashMap<i32, HashSet<i32>> = HashMap::new();
        for log in logs.iter() {
            let id = log[0];
            let time = log[1];
            user_minutes.entry(id).or_insert_with(HashSet::new).insert(time);
        }
        let mut answer = vec![0i32; k as usize];
        for minutes in user_minutes.values() {
            let uam = minutes.len() as i32;
            if uam >= 1 && uam <= k {
                answer[(uam - 1) as usize] += 1;
            }
        }
        answer
    }
}
```

## Racket

```racket
(define/contract (finding-users-active-minutes logs k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof exact-integer?))
  (let ((user-minutes (make-hash))) ; id -> hash of minutes
    (for ([log logs])
      (define id (car log))
      (define minute (cadr log))
      (define mins (hash-ref user-minutes id #f))
      (if mins
          (hash-set! mins minute #t)
          (let ((new (make-hash)))
            (hash-set! new minute #t)
            (hash-set! user-minutes id new))))
    (define ans (make-vector k 0))
    (for ([mins (in-hash-values user-minutes)])
      (define uam (hash-count mins))
      (when (and (>= uam 1) (<= uam k))
        (vector-set! ans (- uam 1) (+ 1 (vector-ref ans (- uam 1))))))
    (vector->list ans)))
```

## Erlang

```erlang
-spec finding_users_active_minutes(Logs :: [[integer()]], K :: integer()) -> [integer()].
finding_users_active_minutes(Logs, K) ->
    UserMap = lists:foldl(
        fun([Id, Time], Acc) ->
            Minutes = maps:get(Id, Acc, #{}),
            NewMinutes = Minutes#{Time => true},
            Acc#{Id => NewMinutes}
        end,
        #{},
        Logs
    ),
    CountMap = maps:fold(
        fun(_Id, Minutes, CAcc) ->
            UAM = maps:size(Minutes),
            Prev = maps:get(UAM, CAcc, 0),
            CAcc#{UAM => Prev + 1}
        end,
        #{},
        UserMap
    ),
    [maps:get(I, CountMap, 0) || I <- lists:seq(1, K)].
```

## Elixir

```elixir
defmodule Solution do
  @spec finding_users_active_minutes(logs :: [[integer]], k :: integer) :: [integer]
  def finding_users_active_minutes(logs, k) do
    user_map =
      Enum.reduce(logs, %{}, fn [id, time], acc ->
        Map.update(acc, id,
          MapSet.new([time]),
          fn set -> MapSet.put(set, time) end)
      end)

    count_map =
      Enum.reduce(user_map, %{}, fn {_id, times}, cnt_acc ->
        uam = MapSet.size(times)

        if uam <= k do
          Map.update(cnt_acc, uam, 1, &(&1 + 1))
        else
          cnt_acc
        end
      end)

    for i <- 1..k, do: Map.get(count_map, i, 0)
  end
end
```
