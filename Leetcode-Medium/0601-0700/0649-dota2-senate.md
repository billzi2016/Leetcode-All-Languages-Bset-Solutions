# 0649. Dota2 Senate

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string predictPartyVictory(string senate) {
        int n = senate.size();
        queue<int> qR, qD;
        for (int i = 0; i < n; ++i) {
            if (senate[i] == 'R') qR.push(i);
            else qD.push(i);
        }
        while (!qR.empty() && !qD.empty()) {
            int r = qR.front(); qR.pop();
            int d = qD.front(); qD.pop();
            if (r < d) {
                qR.push(r + n);
            } else {
                qD.push(d + n);
            }
        }
        return qR.empty() ? "Dire" : "Radiant";
    }
};
```

## Java

```java
class Solution {
    public String predictPartyVictory(String senate) {
        int n = senate.length();
        java.util.ArrayDeque<Integer> rQueue = new java.util.ArrayDeque<>();
        java.util.ArrayDeque<Integer> dQueue = new java.util.ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (senate.charAt(i) == 'R') {
                rQueue.add(i);
            } else {
                dQueue.add(i);
            }
        }
        while (!rQueue.isEmpty() && !dQueue.isEmpty()) {
            int rIdx = rQueue.poll();
            int dIdx = dQueue.poll();
            if (rIdx < dIdx) {
                rQueue.add(rIdx + n);
            } else {
                dQueue.add(dIdx + n);
            }
        }
        return rQueue.isEmpty() ? "Dire" : "Radiant";
    }
}
```

## Python

```python
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        from collections import deque
        n = len(senate)
        radiant = deque()
        dire = deque()
        for i, ch in enumerate(senate):
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)
        return "Radiant" if radiant else "Dire"
```

## Python3

```python
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        n = len(senate)
        radiant = deque()
        dire = deque()
        for i, ch in enumerate(senate):
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)
        return "Radiant" if radiant else "Dire"
```

## C

```c
#include <string.h>
#include <stdlib.h>

char* predictPartyVictory(char* senate) {
    int n = strlen(senate);
    int capacity = 2 * n + 5;
    int *queueR = (int*)malloc(sizeof(int) * capacity);
    int *queueD = (int*)malloc(sizeof(int) * capacity);
    int rHead = 0, rTail = 0, dHead = 0, dTail = 0;

    for (int i = 0; i < n; ++i) {
        if (senate[i] == 'R')
            queueR[rTail++] = i;
        else
            queueD[dTail++] = i;
    }

    while (rHead < rTail && dHead < dTail) {
        int rIdx = queueR[rHead++];
        int dIdx = queueD[dHead++];
        if (rIdx < dIdx)
            queueR[rTail++] = rIdx + n;  // Radiant bans Dire
        else
            queueD[dTail++] = dIdx + n;  // Dire bans Radiant
    }

    free(queueR);
    free(queueD);
    return (rHead < rTail) ? "Radiant" : "Dire";
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public string PredictPartyVictory(string senate) {
        int n = senate.Length;
        var radiant = new Queue<int>();
        var dire = new Queue<int>();

        for (int i = 0; i < n; i++) {
            if (senate[i] == 'R')
                radiant.Enqueue(i);
            else
                dire.Enqueue(i);
        }

        while (radiant.Count > 0 && dire.Count > 0) {
            int rIdx = radiant.Dequeue();
            int dIdx = dire.Dequeue();

            if (rIdx < dIdx) {
                // Radiant bans Dire
                radiant.Enqueue(rIdx + n);
            } else {
                // Dire bans Radiant
                dire.Enqueue(dIdx + n);
            }
        }

        return radiant.Count > 0 ? "Radiant" : "Dire";
    }
}
```

## Javascript

```javascript
/**
 * @param {string} senate
 * @return {string}
 */
var predictPartyVictory = function(senate) {
    const n = senate.length;
    const radiant = [];
    const dire = [];
    
    for (let i = 0; i < n; i++) {
        if (senate[i] === 'R') {
            radiant.push(i);
        } else {
            dire.push(i);
        }
    }
    
    let rPos = 0, dPos = 0;
    while (rPos < radiant.length && dPos < dire.length) {
        const rIdx = radiant[rPos++];
        const dIdx = dire[dPos++];
        if (rIdx < dIdx) {
            // Radiant bans Dire
            radiant.push(rIdx + n);
        } else {
            // Dire bans Radiant
            dire.push(dIdx + n);
        }
    }
    
    return rPos < radiant.length ? "Radiant" : "Dire";
};
```

## Typescript

```typescript
function predictPartyVictory(senate: string): string {
    const n = senate.length;
    const radiant: number[] = [];
    const dire: number[] = [];

    for (let i = 0; i < n; i++) {
        if (senate[i] === 'R') {
            radiant.push(i);
        } else {
            dire.push(i);
        }
    }

    while (radiant.length && dire.length) {
        const rIdx = radiant.shift()!;
        const dIdx = dire.shift()!;

        if (rIdx < dIdx) {
            radiant.push(rIdx + n);
        } else {
            dire.push(dIdx + n);
        }
    }

    return radiant.length ? "Radiant" : "Dire";
}
```

## Php

```php
class Solution {

    /**
     * @param String $senate
     * @return String
     */
    function predictPartyVictory($senate) {
        $n = strlen($senate);
        $queueR = new SplQueue();
        $queueD = new SplQueue();

        for ($i = 0; $i < $n; $i++) {
            if ($senate[$i] === 'R') {
                $queueR->enqueue($i);
            } else {
                $queueD->enqueue($i);
            }
        }

        while (!$queueR->isEmpty() && !$queueD->isEmpty()) {
            $r = $queueR->dequeue();
            $d = $queueD->dequeue();

            if ($r < $d) {
                // Radiant bans Dire
                $queueR->enqueue($r + $n);
            } else {
                // Dire bans Radiant
                $queueD->enqueue($d + $n);
            }
        }

        return $queueR->isEmpty() ? "Dire" : "Radiant";
    }
}
```

## Swift

```swift
class Solution {
    func predictPartyVictory(_ senate: String) -> String {
        let n = senate.count
        var radiant = [Int]()
        var dire = [Int]()
        
        for (i, ch) in senate.enumerated() {
            if ch == "R" {
                radiant.append(i)
            } else {
                dire.append(i)
            }
        }
        
        var rPtr = 0
        var dPtr = 0
        
        while rPtr < radiant.count && dPtr < dire.count {
            let rIdx = radiant[rPtr]
            let dIdx = dire[dPtr]
            
            if rIdx < dIdx {
                radiant.append(rIdx + n)
            } else {
                dire.append(dIdx + n)
            }
            rPtr += 1
            dPtr += 1
        }
        
        return rPtr < radiant.count ? "Radiant" : "Dire"
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun predictPartyVictory(senate: String): String {
        val n = senate.length
        val radiant = java.util.ArrayDeque<Int>()
        val dire = java.util.ArrayDeque<Int>()
        for (i in 0 until n) {
            if (senate[i] == 'R') {
                radiant.add(i)
            } else {
                dire.add(i)
            }
        }
        while (!radiant.isEmpty() && !dire.isEmpty()) {
            val rIdx = radiant.poll()
            val dIdx = dire.poll()
            if (rIdx < dIdx) {
                radiant.add(rIdx + n)
            } else {
                dire.add(dIdx + n)
            }
        }
        return if (!radiant.isEmpty()) "Radiant" else "Dire"
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  String predictPartyVictory(String senate) {
    int n = senate.length;
    Queue<int> radiant = Queue<int>();
    Queue<int> dire = Queue<int>();

    for (int i = 0; i < n; i++) {
      if (senate[i] == 'R') {
        radiant.addLast(i);
      } else {
        dire.addLast(i);
      }
    }

    while (radiant.isNotEmpty && dire.isNotEmpty) {
      int rIdx = radiant.removeFirst();
      int dIdx = dire.removeFirst();

      if (rIdx < dIdx) {
        // Radiant bans Dire
        radiant.addLast(rIdx + n);
      } else {
        // Dire bans Radiant
        dire.addLast(dIdx + n);
      }
    }

    return radiant.isNotEmpty ? "Radiant" : "Dire";
  }
}
```

## Golang

```go
func predictPartyVictory(senate string) string {
    n := len(senate)
    var qR, qD []int
    for i, c := range senate {
        if c == 'R' {
            qR = append(qR, i)
        } else {
            qD = append(qD, i)
        }
    }

    for len(qR) > 0 && len(qD) > 0 {
        r := qR[0]
        d := qD[0]
        qR = qR[1:]
        qD = qD[1:]

        if r < d {
            qR = append(qR, r+n)
        } else {
            qD = append(qD, d+n)
        }
    }

    if len(qR) > 0 {
        return "Radiant"
    }
    return "Dire"
}
```

## Ruby

```ruby
def predict_party_victory(senate)
  n = senate.length
  r_queue = []
  d_queue = []

  senate.each_char.with_index do |c, i|
    if c == 'R'
      r_queue << i
    else
      d_queue << i
    end
  end

  while !r_queue.empty? && !d_queue.empty?
    r_idx = r_queue.shift
    d_idx = d_queue.shift
    if r_idx < d_idx
      r_queue << r_idx + n
    else
      d_queue << d_idx + n
    end
  end

  r_queue.empty? ? "Dire" : "Radiant"
end
```

## Scala

```scala
object Solution {
    def predictPartyVictory(senate: String): String = {
        import scala.collection.mutable.Queue
        val n = senate.length
        val radiant = Queue[Int]()
        val dire = Queue[Int]()
        for (i <- 0 until n) {
            if (senate(i) == 'R') radiant.enqueue(i)
            else dire.enqueue(i)
        }
        while (radiant.nonEmpty && dire.nonEmpty) {
            val rIdx = radiant.dequeue()
            val dIdx = dire.dequeue()
            if (rIdx < dIdx) {
                radiant.enqueue(rIdx + n)
            } else {
                dire.enqueue(dIdx + n)
            }
        }
        if (radiant.nonEmpty) "Radiant" else "Dire"
    }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn predict_party_victory(senate: String) -> String {
        let n = senate.len();
        let mut radiant: VecDeque<usize> = VecDeque::new();
        let mut dire: VecDeque<usize> = VecDeque::new();

        for (i, c) in senate.chars().enumerate() {
            if c == 'R' {
                radiant.push_back(i);
            } else {
                dire.push_back(i);
            }
        }

        while !radiant.is_empty() && !dire.is_empty() {
            let r_idx = radiant.pop_front().unwrap();
            let d_idx = dire.pop_front().unwrap();

            if r_idx < d_idx {
                radiant.push_back(r_idx + n);
            } else {
                dire.push_back(d_idx + n);
            }
        }

        if !radiant.is_empty() {
            "Radiant".to_string()
        } else {
            "Dire".to_string()
        }
    }
}
```

## Racket

```racket
(require racket/queue)

(define/contract (predict-party-victory senate)
  (-> string? string?)
  (let* ([n (string-length senate)]
         [queue-r (make-queue)]
         [queue-d (make-queue)])
    (for ([i (in-range n)])
      (cond [(char=? (string-ref senate i) #\R) (enqueue! queue-r i)]
            [(char=? (string-ref senate i) #\D) (enqueue! queue-d i)]))
    (let loop ()
      (if (or (queue-empty? queue-r) (queue-empty? queue-d))
          (if (queue-empty? queue-r) "Dire" "Radiant")
          (begin
            (define r-index (dequeue! queue-r))
            (define d-index (dequeue! queue-d))
            (if (< r-index d-index)
                (enqueue! queue-r (+ r-index n))
                (enqueue! queue-d (+ d-index n)))
            (loop))))))
```

## Erlang

```erlang
-module(solution).
-export([predict_party_victory/1]).

-spec predict_party_victory(Senate :: unicode:unicode_binary()) -> unicode:unicode_binary().
predict_party_victory(Senate) ->
    N = byte_size(Senate),
    {RQueue0, DQueue0} = init_queues(Senate, N, queue:new(), queue:new()),
    simulate(RQueue0, DQueue0, N).

init_queues(Bin, Len, RQ, DQ) ->
    init_queues(0, Bin, Len, RQ, DQ).

init_queues(Index, _Bin, Len, RQ, DQ) when Index >= Len ->
    {RQ, DQ};
init_queues(Index, Bin, Len, RQ, DQ) ->
    Char = binary:at(Bin, Index),
    case Char of
        $R -> init_queues(Index + 1, Bin, Len, queue:in(Index, RQ), DQ);
        $D -> init_queues(Index + 1, Bin, Len, RQ, queue:in(Index, DQ))
    end.

simulate(RQueue, DQueue, N) ->
    case {queue:is_empty(RQueue), queue:is_empty(DQueue)} of
        {true, false} -> <<"Dire">>;
        {false, true} -> <<"Radiant">>;
        _ ->
            {{value, RIdx}, RRest} = queue:out(RQueue),
            {{value, DIdx}, DRest} = queue:out(DQueue),
            if
                RIdx < DIdx ->
                    NewRQueue = queue:in(RIdx + N, RRest),
                    simulate(NewRQueue, DRest, N);
                true ->
                    NewDQueue = queue:in(DIdx + N, DRest),
                    simulate(RRest, NewDQueue, N)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec predict_party_victory(senate :: String.t()) :: String.t()
  def predict_party_victory(senate) do
    n = String.length(senate)

    {r_queue, d_queue} =
      senate
      |> String.graphemes()
      |> Enum.with_index()
      |> Enum.reduce({:queue.new(), :queue.new()}, fn
        {"R", i}, {rq, dq} -> {:queue.in(i, rq), dq}
        {"D", i}, {rq, dq} -> {rq, :queue.in(i, dq)}
      end)

    case simulate(r_queue, d_queue, n) do
      :radiant -> "Radiant"
      :dire -> "Dire"
    end
  end

  defp simulate(rq, dq, n) do
    cond do
      :queue.is_empty(rq) -> :dire
      :queue.is_empty(dq) -> :radiant
      true ->
        {{:value, r_idx}, rq_rest} = :queue.out(rq)
        {{:value, d_idx}, dq_rest} = :queue.out(dq)

        if r_idx < d_idx do
          new_rq = :queue.in(r_idx + n, rq_rest)
          simulate(new_rq, dq_rest, n)
        else
          new_dq = :queue.in(d_idx + n, dq_rest)
          simulate(rq_rest, new_dq, n)
        end
    end
  end
end
```
