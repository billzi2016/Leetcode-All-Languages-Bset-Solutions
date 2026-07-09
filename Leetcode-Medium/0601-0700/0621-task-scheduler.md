# 0621. Task Scheduler

## Cpp

```cpp
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> freq(26, 0);
        for (char c : tasks) ++freq[c - 'A'];
        int maxFreq = 0, maxCount = 0;
        for (int f : freq) {
            if (f > maxFreq) {
                maxFreq = f;
                maxCount = 1;
            } else if (f == maxFreq) {
                ++maxCount;
            }
        }
        int part = (maxFreq - 1) * (n + 1) + maxCount;
        return max((int)tasks.size(), part);
    }
};
```

## Java

```java
class Solution {
    public int leastInterval(char[] tasks, int n) {
        if (n == 0) return tasks.length;
        int[] freq = new int[26];
        for (char c : tasks) {
            freq[c - 'A']++;
        }
        int maxFreq = 0;
        for (int f : freq) {
            if (f > maxFreq) maxFreq = f;
        }
        int maxCount = 0;
        for (int f : freq) {
            if (f == maxFreq) maxCount++;
        }
        int part = (maxFreq - 1) * (n + 1) + maxCount;
        return Math.max(part, tasks.length);
    }
}
```

## Python

```python
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - 65] += 1

        max_freq = max(freq)
        max_count = sum(1 for f in freq if f == max_freq)

        # The minimal length is either the total number of tasks,
        # or the arrangement based on the most frequent tasks.
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
```

## Python3

```python
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord('A')] += 1
        max_freq = max(freq)
        max_count = sum(1 for f in freq if f == max_freq)
        part_len = (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), part_len)
```

## C

```c
int leastInterval(char* tasks, int tasksSize, int n) {
    int freq[26] = {0};
    for (int i = 0; i < tasksSize; ++i) {
        freq[tasks[i] - 'A']++;
    }
    int maxFreq = 0;
    for (int i = 0; i < 26; ++i) {
        if (freq[i] > maxFreq) maxFreq = freq[i];
    }
    int countMax = 0;
    for (int i = 0; i < 26; ++i) {
        if (freq[i] == maxFreq) countMax++;
    }
    int part = (maxFreq - 1) * (n + 1) + countMax;
    return part > tasksSize ? part : tasksSize;
}
```

## Csharp

```csharp
public class Solution {
    public int LeastInterval(char[] tasks, int n) {
        int[] freq = new int[26];
        foreach (char c in tasks) {
            freq[c - 'A']++;
        }
        int maxFreq = 0;
        foreach (int f in freq) {
            if (f > maxFreq) maxFreq = f;
        }
        int maxCount = 0;
        foreach (int f in freq) {
            if (f == maxFreq) maxCount++;
        }
        int intervals = (maxFreq - 1) * (n + 1) + maxCount;
        return Math.Max(tasks.Length, intervals);
    }
}
```

## Javascript

```javascript
/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function(tasks, n) {
    const freq = new Array(26).fill(0);
    let maxFreq = 0;
    for (const t of tasks) {
        const idx = t.charCodeAt(0) - 65;
        freq[idx]++;
        if (freq[idx] > maxFreq) maxFreq = freq[idx];
    }
    let maxCount = 0;
    for (let f of freq) {
        if (f === maxFreq) maxCount++;
    }
    const part = (maxFreq - 1) * (n + 1) + maxCount;
    return Math.max(tasks.length, part);
};
```

## Typescript

```typescript
function leastInterval(tasks: string[], n: number): number {
    const freq = new Array(26).fill(0);
    for (const t of tasks) {
        freq[t.charCodeAt(0) - 65]++;
    }
    let maxFreq = 0;
    let maxCount = 0;
    for (const f of freq) {
        if (f > maxFreq) {
            maxFreq = f;
            maxCount = 1;
        } else if (f === maxFreq && f > 0) {
            maxCount++;
        }
    }
    const needed = (maxFreq - 1) * (n + 1) + maxCount;
    return Math.max(tasks.length, needed);
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $tasks
     * @param Integer $n
     * @return Integer
     */
    function leastInterval($tasks, $n) {
        $freq = array_fill(0, 26, 0);
        foreach ($tasks as $t) {
            $idx = ord($t) - 65;
            $freq[$idx]++;
        }
        $maxFreq = max($freq);
        $maxCount = 0;
        foreach ($freq as $f) {
            if ($f == $maxFreq) {
                $maxCount++;
            }
        }
        $part = ($maxFreq - 1) * ($n + 1) + $maxCount;
        return max(count($tasks), $part);
    }
}
```

## Swift

```swift
class Solution {
    func leastInterval(_ tasks: [Character], _ n: Int) -> Int {
        var freq = Array(repeating: 0, count: 26)
        let base = Int(("A".unicodeScalars.first!).value)
        for ch in tasks {
            let idx = Int(ch.unicodeScalars.first!.value) - base
            freq[idx] += 1
        }
        var maxFreq = 0
        for f in freq {
            if f > maxFreq { maxFreq = f }
        }
        var countMax = 0
        for f in freq where f == maxFreq {
            countMax += 1
        }
        let part = (maxFreq - 1) * (n + 1) + countMax
        return max(tasks.count, part)
    }
}
```

## Kotlin

```kotlin
import kotlin.math.max

class Solution {
    fun leastInterval(tasks: CharArray, n: Int): Int {
        val freq = IntArray(26)
        var maxFreq = 0
        for (c in tasks) {
            val idx = c - 'A'
            freq[idx]++
            if (freq[idx] > maxFreq) maxFreq = freq[idx]
        }
        var countMax = 0
        for (f in freq) {
            if (f == maxFreq) countMax++
        }
        return max(tasks.size, (maxFreq - 1) * (n + 1) + countMax)
    }
}
```

## Dart

```dart
class Solution {
  int leastInterval(List<String> tasks, int n) {
    List<int> freq = List.filled(26, 0);
    for (var t in tasks) {
      freq[t.codeUnitAt(0) - 65]++;
    }
    int maxFreq = 0;
    for (int f in freq) {
      if (f > maxFreq) maxFreq = f;
    }
    int maxCount = 0;
    for (int f in freq) {
      if (f == maxFreq) maxCount++;
    }
    int part = (maxFreq - 1) * (n + 1) + maxCount;
    return part > tasks.length ? part : tasks.length;
  }
}
```

## Golang

```go
func leastInterval(tasks []byte, n int) int {
	freq := [26]int{}
	maxFreq := 0
	for _, t := range tasks {
		idx := t - 'A'
		freq[idx]++
		if freq[idx] > maxFreq {
			maxFreq = freq[idx]
		}
	}
	countMax := 0
	for _, f := range freq {
		if f == maxFreq {
			countMax++
		}
	}
	part := (maxFreq-1)*(n+1) + countMax
	if len(tasks) > part {
		return len(tasks)
	}
	return part
}
```

## Ruby

```ruby
def least_interval(tasks, n)
  freq = Array.new(26, 0)
  tasks.each { |c| freq[c.ord - 65] += 1 }
  max_freq = freq.max
  max_count = freq.count(max_freq)
  part = (max_freq - 1) * (n + 1) + max_count
  [tasks.length, part].max
end
```

## Scala

```scala
object Solution {
    def leastInterval(tasks: Array[Char], n: Int): Int = {
        val freq = new Array[Int](26)
        for (c <- tasks) {
            freq(c - 'A') += 1
        }
        var maxFreq = 0
        var maxCount = 0
        for (f <- freq) {
            if (f > maxFreq) {
                maxFreq = f
                maxCount = 1
            } else if (f == maxFreq) {
                maxCount += 1
            }
        }
        val part = (maxFreq - 1) * (n + 1) + maxCount
        scala.math.max(tasks.length, part)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        let mut freq = [0i32; 26];
        for &c in tasks.iter() {
            freq[(c as u8 - b'A') as usize] += 1;
        }
        let max_freq = *freq.iter().max().unwrap();
        let max_count = freq.iter().filter(|&&f| f == max_freq).count() as i32;
        let part_len = n + 1;
        let needed = (max_freq - 1) * part_len + max_count;
        std::cmp::max(needed, tasks.len() as i32)
    }
}
```

## Racket

```racket
(define/contract (least-interval tasks n)
  (-> (listof char?) exact-integer? exact-integer?)
  (let* ((freq (make-vector 26 0))
         (len (length tasks)))
    ;; count frequencies
    (for ([c tasks])
      (let* ((idx (- (char->integer c) (char->integer #\A)))
             (new (+ 1 (vector-ref freq idx))))
        (vector-set! freq idx new)))
    ;; find max frequency and how many tasks have it
    (let loop ((i 0) (max-f 0) (max-cnt 0))
      (if (= i 26)
          (let* ((part (* (- max-f 1) (+ n 1)))
                 (ans (max len (+ part max-cnt))))
            ans)
          (let* ((cnt (vector-ref freq i))
                 (new-max-f (if (> cnt max-f) cnt max-f))
                 (new-max-cnt (cond
                               [(> cnt max-f) 1]
                               [(= cnt max-f) (+ max-cnt 1)]
                               [else max-cnt])))
            (loop (+ i 1) new-max-f new-max-cnt))))))
```

## Erlang

```erlang
-module(solution).
-export([least_interval/2]).

-spec least_interval(Tasks :: [char()], N :: integer()) -> integer().
least_interval(Tasks, N) ->
    Freq0 = erlang:make_tuple(26, 0),
    {Freq, MaxFreq} = lists:foldl(
        fun(Task, {Tuple, MF}) ->
            Idx = Task - $A + 1,
            Old = element(Idx, Tuple),
            NewCnt = Old + 1,
            NewTuple = setelement(Idx, Tuple, NewCnt),
            NewMF = if NewCnt > MF -> NewCnt; true -> MF end,
            {NewTuple, NewMF}
        end,
        {Freq0, 0},
        Tasks
    ),
    NumMax = length([1 || C <- tuple_to_list(Freq), C == MaxFreq]),
    Total = length(Tasks),
    Needed = (MaxFreq - 1) * (N + 1) + NumMax,
    erlang:max(Total, Needed).
```

## Elixir

```elixir
defmodule Solution do
  @spec least_interval(tasks :: [String.t()], n :: integer) :: integer
  def least_interval(tasks, n) do
    freq = Enum.reduce(tasks, %{}, fn task, acc ->
      Map.update(acc, task, 1, &(&1 + 1))
    end)

    values = Map.values(freq)
    max_freq = Enum.max(values)
    max_count = Enum.count(values, fn v -> v == max_freq end)

    part = (max_freq - 1) * (n + 1) + max_count
    len = length(tasks)

    if part > len, do: part, else: len
  end
end
```
