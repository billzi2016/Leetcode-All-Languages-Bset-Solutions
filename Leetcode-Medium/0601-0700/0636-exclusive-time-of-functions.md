# 0636. Exclusive Time of Functions

## Cpp

```cpp
class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<long long> res(n, 0);
        vector<int> stk;
        int prev = 0;
        bool first = true;
        for (const string& log : logs) {
            // parse
            size_t p1 = log.find(':');
            size_t p2 = log.find(':', p1 + 1);
            int id = stoi(log.substr(0, p1));
            string type = log.substr(p1 + 1, p2 - p1 - 1);
            int ts = stoi(log.substr(p2 + 1));
            
            if (type == "start") {
                if (!stk.empty()) {
                    res[stk.back()] += (long long)ts - prev;
                }
                stk.push_back(id);
                prev = ts;
            } else { // end
                int curId = stk.back();
                stk.pop_back();
                res[curId] += (long long)ts - prev + 1;
                prev = ts + 1;
            }
        }
        vector<int> ans(n);
        for (int i = 0; i < n; ++i) ans[i] = (int)res[i];
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        int[] res = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        int prev = 0;
        for (String log : logs) {
            String[] parts = log.split(":");
            int id = Integer.parseInt(parts[0]);
            String type = parts[1];
            int time = Integer.parseInt(parts[2]);
            if ("start".equals(type)) {
                if (!stack.isEmpty()) {
                    res[stack.peek()] += time - prev;
                }
                stack.push(id);
                prev = time;
            } else { // end
                int curId = stack.pop();
                res[curId] += time - prev + 1;
                prev = time + 1;
                if (!stack.isEmpty()) {
                    // next interval will start from prev, handled in next iteration
                }
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fid_str, typ, t_str = log.split(':')
            fid = int(fid_str)
            cur = int(t_str)

            if typ == 'start':
                if stack:
                    # time spent by the function on top of stack until now
                    res[stack[-1]] += cur - prev_time
                stack.append(fid)
                prev_time = cur
            else:  # 'end'
                # current function ends at cur (inclusive)
                res[stack.pop()] += cur - prev_time + 1
                prev_time = cur + 1

        return res
```

## Python3

```python
from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fid_str, typ, time_str = log.split(':')
            fid = int(fid_str)
            cur_time = int(time_str)

            if typ == 'start':
                if stack:
                    res[stack[-1]] += cur_time - prev_time
                stack.append(fid)
                prev_time = cur_time
            else:  # 'end'
                # current function ends at cur_time inclusive
                res[stack.pop()] += cur_time - prev_time + 1
                prev_time = cur_time + 1

        return res
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* exclusiveTime(int n, char** logs, int logsSize, int* returnSize) {
    int *res = (int *)calloc(n, sizeof(int));
    int *stack = (int *)malloc(logsSize * sizeof(int));
    int top = -1;
    int prev = 0;

    for (int i = 0; i < logsSize; ++i) {
        char type[6];
        int id, t;
        sscanf(logs[i], "%d:%5[^:]:%d", &id, type, &t);
        if (type[0] == 's') { // "start"
            if (top != -1) {
                res[stack[top]] += t - prev;
            }
            stack[++top] = id;
            prev = t;
        } else { // "end"
            int cur = stack[top--];
            res[cur] += t - prev + 1;
            prev = t + 1;
        }
    }

    *returnSize = n;
    free(stack);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int[] ExclusiveTime(int n, IList<string> logs) {
        int[] result = new int[n];
        var stack = new System.Collections.Generic.Stack<int>();
        int prevTime = 0;
        bool first = true;

        foreach (var log in logs) {
            var parts = log.Split(':');
            int id = int.Parse(parts[0]);
            string type = parts[1];
            int time = int.Parse(parts[2]);

            if (type == "start") {
                if (stack.Count > 0) {
                    result[stack.Peek()] += time - prevTime;
                }
                stack.Push(id);
                prevTime = time;
            } else { // end
                int curId = stack.Pop();
                result[curId] += time - prevTime + 1;
                prevTime = time + 1;
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {string[]} logs
 * @return {number[]}
 */
var exclusiveTime = function(n, logs) {
    const result = new Array(n).fill(0);
    const stack = [];
    let prev = 0;
    
    for (const log of logs) {
        const [idStr, type, timeStr] = log.split(':');
        const id = Number(idStr);
        const time = Number(timeStr);
        
        if (type === 'start') {
            if (stack.length) {
                result[stack[stack.length - 1]] += time - prev;
            }
            stack.push(id);
            prev = time;
        } else { // end
            const curId = stack.pop();
            result[curId] += time - prev + 1;
            prev = time + 1;
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function exclusiveTime(n: number, logs: string[]): number[] {
    const res = new Array<number>(n).fill(0);
    const stack: number[] = [];
    let prev = 0;

    for (const log of logs) {
        const [idStr, type, timeStr] = log.split(':');
        const id = Number(idStr);
        const t = Number(timeStr);

        if (type === 'start') {
            if (stack.length > 0) {
                res[stack[stack.length - 1]] += t - prev;
            }
            stack.push(id);
            prev = t;
        } else { // end
            const curId = stack.pop()!;
            res[curId] += t - prev + 1;
            prev = t + 1;
        }
    }

    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param String[] $logs
     * @return Integer[]
     */
    function exclusiveTime($n, $logs) {
        $res = array_fill(0, $n, 0);
        $stack = [];
        $prev = 0;
        foreach ($logs as $log) {
            [$idStr, $type, $timeStr] = explode(':', $log);
            $id = intval($idStr);
            $time = intval($timeStr);
            if ($type === 'start') {
                if (!empty($stack)) {
                    $top = end($stack);
                    $res[$top] += $time - $prev;
                }
                $stack[] = $id;
                $prev = $time;
            } else { // end
                $top = array_pop($stack);
                $res[$top] += $time - $prev + 1;
                $prev = $time + 1;
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func exclusiveTime(_ n: Int, _ logs: [String]) -> [Int] {
        var result = Array(repeating: 0, count: n)
        var stack = [Int]()
        var prevTime = 0
        
        for log in logs {
            let parts = log.split(separator: ":")
            let id = Int(parts[0])!
            let type = parts[1]
            let time = Int(parts[2])!
            
            if type == "start" {
                if let last = stack.last {
                    result[last] += time - prevTime
                }
                stack.append(id)
                prevTime = time
            } else { // "end"
                let curId = stack.removeLast()
                result[curId] += time - prevTime + 1
                prevTime = time + 1
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun exclusiveTime(n: Int, logs: List<String>): IntArray {
        val result = IntArray(n)
        val stack = java.util.ArrayDeque<Int>()
        var prevTime = 0
        for (log in logs) {
            val parts = log.split(":")
            val id = parts[0].toInt()
            val type = parts[1]
            val time = parts[2].toInt()
            if (type == "start") {
                if (stack.isNotEmpty()) {
                    result[stack.peek()] += time - prevTime
                }
                stack.push(id)
                prevTime = time
            } else { // "end"
                val finishedId = stack.pop()
                result[finishedId] += time - prevTime + 1
                prevTime = time + 1
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> exclusiveTime(int n, List<String> logs) {
    List<int> result = List.filled(n, 0);
    List<int> stack = [];
    int prevTime = 0;

    for (String log in logs) {
      var parts = log.split(':');
      int id = int.parse(parts[0]);
      String type = parts[1];
      int time = int.parse(parts[2]);

      if (type == 'start') {
        if (stack.isNotEmpty) {
          result[stack.last] += time - prevTime;
        }
        stack.add(id);
        prevTime = time;
      } else { // end
        result[stack.last] += time - prevTime + 1;
        stack.removeLast();
        prevTime = time + 1;
      }
    }

    return result;
  }
}
```

## Golang

```go
func exclusiveTime(n int, logs []string) []int {
    res := make([]int, n)
    stack := []int{}
    prev := 0
    for _, log := range logs {
        parts := strings.Split(log, ":")
        id, _ := strconv.Atoi(parts[0])
        typ := parts[1]
        t, _ := strconv.Atoi(parts[2])

        if typ == "start" {
            if len(stack) > 0 {
                res[stack[len(stack)-1]] += t - prev
            }
            stack = append(stack, id)
            prev = t
        } else { // "end"
            top := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            res[top] += t - prev + 1
            prev = t + 1
        }
    }
    return res
}
```

## Ruby

```ruby
def exclusive_time(n, logs)
  result = Array.new(n, 0)
  stack = []
  prev_time = 0

  logs.each do |log|
    id_str, type, time_str = log.split(':')
    fid = id_str.to_i
    timestamp = time_str.to_i

    if type == 'start'
      unless stack.empty?
        result[stack[-1]] += timestamp - prev_time
      end
      stack << fid
      prev_time = timestamp
    else # 'end'
      cur = stack.pop
      result[cur] += timestamp - prev_time + 1
      prev_time = timestamp + 1
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def exclusiveTime(n: Int, logs: List[String]): Array[Int] = {
        val result = new Array[Long](n)
        import scala.collection.mutable.Stack
        val stack = new Stack[Int]()
        var prevTime = 0L

        for (log <- logs) {
            val parts = log.split(":")
            val id = parts(0).toInt
            val typ = parts(1)
            val time = parts(2).toLong

            if (typ == "start") {
                if (stack.nonEmpty) {
                    result(stack.top) += time - prevTime
                }
                stack.push(id)
                prevTime = time
            } else { // "end"
                val curId = stack.pop()
                result(curId) += time - prevTime + 1
                prevTime = time + 1
            }
        }

        result.map(_.toInt)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn exclusive_time(n: i32, logs: Vec<String>) -> Vec<i32> {
        let mut res = vec![0i32; n as usize];
        let mut stack: Vec<i32> = Vec::new();
        let mut prev = 0i32;

        for log in logs.iter() {
            let parts: Vec<&str> = log.split(':').collect();
            let id: i32 = parts[0].parse().unwrap();
            let typ = parts[1];
            let time: i32 = parts[2].parse().unwrap();

            if typ == "start" {
                if let Some(&top) = stack.last() {
                    res[top as usize] += time - prev;
                }
                stack.push(id);
                prev = time;
            } else { // "end"
                let top = stack.pop().unwrap();
                res[top as usize] += time - prev + 1;
                prev = time + 1;
            }
        }

        res
    }
}
```

## Racket

```racket
(require racket/string)

(define/contract (exclusive-time n logs)
  (-> exact-integer? (listof string?) (listof exact-integer?))
  (let* ((times (make-vector n 0))
         (stack '())
         (prev 0))
    (for ([log logs])
      (define parts (string-split log ":"))
      (define fid (string->number (list-ref parts 0)))
      (define typ (list-ref parts 1))
      (define ts (string->number (list-ref parts 2)))
      (cond
        [(string=? typ "start")
         (when (not (null? stack))
           (let* ((top-id (car stack))
                  (inc (- ts prev)))
             (vector-set! times top-id (+ (vector-ref times top-id) inc))))
         (set! stack (cons fid stack))
         (set! prev ts)]
        [(string=? typ "end")
         (define top-id (car stack))
         (let* ((inc (+ (- ts prev) 1)))
           (vector-set! times top-id (+ (vector-ref times top-id) inc)))
         (set! stack (cdr stack))
         (set! prev (+ ts 1))]))
    (for/list ([i (in-range n)]) (vector-ref times i))))
```

## Erlang

```erlang
-module(solution).
-export([exclusive_time/2]).

-spec exclusive_time(N :: integer(), Logs :: [unicode:unicode_binary()]) -> [integer()].
exclusive_time(N, Logs) ->
    Res0 = erlang:make_tuple(N, 0),
    process_logs(Logs, [], undefined, Res0).

process_logs([], _Stack, _Prev, Res) ->
    tuple_to_list(Res);
process_logs([Log|Rest], Stack, Prev, Res) ->
    {Id, Type, Ts} = parse_log(Log),
    case Type of
        start ->
            case Stack of
                [] ->
                    process_logs(Rest, [{Id, Ts}|Stack], Ts, Res);
                [{TopId,_}|_] ->
                    Delta = Ts - Prev,
                    Old = element(TopId+1, Res),
                    NewRes = setelement(TopId+1, Res, Old + Delta),
                    process_logs(Rest, [{Id, Ts}|Stack], Ts, NewRes)
            end;
        end ->
            [{Fid,_Start}|RestStack] = Stack,
            Delta = Ts - Prev + 1,
            Old = element(Fid+1, Res),
            NewRes = setelement(Fid+1, Res, Old + Delta),
            NewPrev = Ts + 1,
            process_logs(Rest, RestStack, NewPrev, NewRes)
    end.

parse_log(Log) ->
    [IdBin, TypeBin, TimeBin] = binary:split(Log, <<":">>, [global]),
    Id = erlang:binary_to_integer(IdBin),
    Type = case TypeBin of
        <<"start">> -> start;
        <<"end">> -> end
    end,
    Ts = erlang:binary_to_integer(TimeBin),
    {Id, Type, Ts}.
```

## Elixir

```elixir
defmodule Solution do
  @spec exclusive_time(n :: integer, logs :: [String.t]) :: [integer]
  def exclusive_time(n, logs) do
    {_, _, times} =
      Enum.reduce(logs, {[], 0, List.duplicate(0, n)}, fn log, {stack, prev, times} ->
        [fid_str, typ, ts_str] = String.split(log, ":")
        fid = String.to_integer(fid_str)
        ts = String.to_integer(ts_str)

        if typ == "start" do
          case stack do
            [] ->
              {[fid | stack], ts, times}
            [top | _] ->
              diff = ts - prev
              new_times = List.update_at(times, top, &(&1 + diff))
              {[fid | stack], ts, new_times}
          end
        else
          [top | rest] = stack
          diff = ts - prev + 1
          new_times = List.update_at(times, top, &(&1 + diff))
          {rest, ts + 1, new_times}
        end
      end)

    times
  end
end
```
