# 0949. Largest Time for Given Digits

## Cpp

```cpp
class Solution {
public:
    string largestTimeFromDigits(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int best = -1;
        do {
            int hour = arr[0] * 10 + arr[1];
            int minute = arr[2] * 10 + arr[3];
            if (hour < 24 && minute < 60) {
                int total = hour * 60 + minute;
                if (total > best) best = total;
            }
        } while (next_permutation(arr.begin(), arr.end()));
        
        if (best == -1) return "";
        int h = best / 60;
        int m = best % 60;
        char buf[6];
        snprintf(buf, sizeof(buf), "%02d:%02d", h, m);
        return string(buf);
    }
};
```

## Java

```java
class Solution {
    public String largestTimeFromDigits(int[] arr) {
        int max = -1;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) if (j != i) {
                for (int k = 0; k < 4; k++) if (k != i && k != j) {
                    int l = 6 - i - j - k; // remaining index
                    int hour = arr[i] * 10 + arr[j];
                    int minute = arr[k] * 10 + arr[l];
                    if (hour < 24 && minute < 60) {
                        int total = hour * 60 + minute;
                        if (total > max) {
                            max = total;
                        }
                    }
                }
            }
        }
        if (max == -1) return "";
        int hh = max / 60;
        int mm = max % 60;
        return String.format("%02d:%02d", hh, mm);
    }
}
```

## Python

```python
class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        import itertools
        max_time = -1
        for perm in itertools.permutations(arr):
            hour = perm[0] * 10 + perm[1]
            minute = perm[2] * 10 + perm[3]
            if hour < 24 and minute < 60:
                total = hour * 60 + minute
                if total > max_time:
                    max_time = total
        if max_time == -1:
            return ""
        hh, mm = divmod(max_time, 60)
        return "{:02d}:{:02d}".format(hh, mm)
```

## Python3

```python
from typing import List
import itertools

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time = -1
        for perm in itertools.permutations(arr):
            hour = perm[0] * 10 + perm[1]
            minute = perm[2] * 10 + perm[3]
            if hour < 24 and minute < 60:
                total = hour * 60 + minute
                if total > max_time:
                    max_time = total
        if max_time == -1:
            return ""
        hh, mm = divmod(max_time, 60)
        return f"{hh:02d}:{mm:02d}"
```

## C

```c
#include <stdio.h>
#include <stdlib.h>

char* largestTimeFromDigits(int* arr, int arrSize) {
    int maxTotal = -1;
    int bestHour = 0, bestMinute = 0;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) if (j != i) {
            int hour = arr[i] * 10 + arr[j];
            if (hour >= 24) continue;
            for (int k = 0; k < 4; ++k) if (k != i && k != j) {
                for (int l = 0; l < 4; ++l) if (l != i && l != j && l != k) {
                    int minute = arr[k] * 10 + arr[l];
                    if (minute >= 60) continue;
                    int total = hour * 60 + minute;
                    if (total > maxTotal) {
                        maxTotal = total;
                        bestHour = hour;
                        bestMinute = minute;
                    }
                }
            }
        }
    }
    if (maxTotal == -1) {
        char *empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    char *result = (char*)malloc(6); // "HH:MM" + null terminator
    sprintf(result, "%02d:%02d", bestHour, bestMinute);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string LargestTimeFromDigits(int[] arr)
    {
        int maxTotal = -1;

        void Swap(int i, int j)
        {
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }

        void Backtrack(int idx)
        {
            if (idx == 4)
            {
                int hour = arr[0] * 10 + arr[1];
                int minute = arr[2] * 10 + arr[3];
                if (hour < 24 && minute < 60)
                {
                    int total = hour * 60 + minute;
                    if (total > maxTotal) maxTotal = total;
                }
                return;
            }

            for (int i = idx; i < 4; i++)
            {
                Swap(idx, i);
                Backtrack(idx + 1);
                Swap(idx, i);
            }
        }

        Backtrack(0);

        if (maxTotal == -1) return "";
        int bestHour = maxTotal / 60;
        int bestMinute = maxTotal % 60;
        return $"{bestHour:D2}:{bestMinute:D2}";
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {string}
 */
var largestTimeFromDigits = function(arr) {
    let maxTotal = -1;
    const used = new Array(4).fill(false);
    const perm = new Array(4);
    
    function backtrack(pos) {
        if (pos === 4) {
            const hour = perm[0] * 10 + perm[1];
            const minute = perm[2] * 10 + perm[3];
            if (hour < 24 && minute < 60) {
                const total = hour * 60 + minute;
                if (total > maxTotal) maxTotal = total;
            }
            return;
        }
        for (let i = 0; i < 4; i++) {
            if (!used[i]) {
                used[i] = true;
                perm[pos] = arr[i];
                backtrack(pos + 1);
                used[i] = false;
            }
        }
    }
    
    backtrack(0);
    
    if (maxTotal === -1) return "";
    const hh = Math.floor(maxTotal / 60).toString().padStart(2, '0');
    const mm = (maxTotal % 60).toString().padStart(2, '0');
    return `${hh}:${mm}`;
};
```

## Typescript

```typescript
function largestTimeFromDigits(arr: number[]): string {
    let maxTotal = -1;
    const used = new Array(4).fill(false);
    const perm = new Array<number>(4);

    function dfs(pos: number): void {
        if (pos === 4) {
            const hour = perm[0] * 10 + perm[1];
            const minute = perm[2] * 10 + perm[3];
            if (hour < 24 && minute < 60) {
                const total = hour * 60 + minute;
                if (total > maxTotal) maxTotal = total;
            }
            return;
        }
        for (let i = 0; i < 4; i++) {
            if (!used[i]) {
                used[i] = true;
                perm[pos] = arr[i];
                dfs(pos + 1);
                used[i] = false;
            }
        }
    }

    dfs(0);

    if (maxTotal === -1) return "";
    const hh = Math.floor(maxTotal / 60).toString().padStart(2, '0');
    const mm = (maxTotal % 60).toString().padStart(2, '0');
    return `${hh}:${mm}`;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer[] $arr
     * @return String
     */
    function largestTimeFromDigits($arr) {
        $max = -1;
        for ($i = 0; $i < 4; ++$i) {
            for ($j = 0; $j < 4; ++$j) {
                if ($j == $i) continue;
                for ($k = 0; $k < 4; ++$k) {
                    if ($k == $i || $k == $j) continue;
                    // remaining index
                    $l = 6 - $i - $j - $k; // sum of 0+1+2+3 = 6
                    $hour = $arr[$i] * 10 + $arr[$j];
                    if ($hour >= 24) continue;
                    $minute = $arr[$k] * 10 + $arr[$l];
                    if ($minute >= 60) continue;
                    $total = $hour * 60 + $minute;
                    if ($total > $max) {
                        $max = $total;
                    }
                }
            }
        }
        if ($max == -1) {
            return "";
        }
        $hh = intdiv($max, 60);
        $mm = $max % 60;
        return sprintf("%02d:%02d", $hh, $mm);
    }
}
?>
```

## Swift

```swift
import Foundation

class Solution {
    func largestTimeFromDigits(_ arr: [Int]) -> String {
        var maxTotal = -1
        for i in 0..<4 {
            for j in 0..<4 where j != i {
                for k in 0..<4 where k != i && k != j {
                    let l = 6 - i - j - k
                    if l == i || l == j || l == k { continue }
                    let hour = arr[i] * 10 + arr[j]
                    let minute = arr[k] * 10 + arr[l]
                    if hour < 24 && minute < 60 {
                        let total = hour * 60 + minute
                        if total > maxTotal {
                            maxTotal = total
                        }
                    }
                }
            }
        }
        if maxTotal == -1 {
            return ""
        } else {
            let hour = maxTotal / 60
            let minute = maxTotal % 60
            return String(format: "%02d:%02d", hour, minute)
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestTimeFromDigits(arr: IntArray): String {
        var max = -1
        val used = BooleanArray(4)
        val path = IntArray(4)

        fun backtrack(depth: Int) {
            if (depth == 4) {
                val hour = path[0] * 10 + path[1]
                val minute = path[2] * 10 + path[3]
                if (hour < 24 && minute < 60) {
                    val total = hour * 60 + minute
                    if (total > max) max = total
                }
                return
            }
            for (i in 0 until 4) {
                if (!used[i]) {
                    used[i] = true
                    path[depth] = arr[i]
                    backtrack(depth + 1)
                    used[i] = false
                }
            }
        }

        backtrack(0)

        return if (max == -1) "" else String.format("%02d:%02d", max / 60, max % 60)
    }
}
```

## Dart

```dart
class Solution {
  String largestTimeFromDigits(List<int> arr) {
    int maxTime = -1;
    String best = '';
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        if (j == i) continue;
        for (int k = 0; k < 4; k++) {
          if (k == i || k == j) continue;
          for (int l = 0; l < 4; l++) {
            if (l == i || l == j || l == k) continue;
            int hour = arr[i] * 10 + arr[j];
            int minute = arr[k] * 10 + arr[l];
            if (hour < 24 && minute < 60) {
              int total = hour * 60 + minute;
              if (total > maxTime) {
                maxTime = total;
                best =
                    '${hour.toString().padLeft(2, '0')}:${minute.toString().padLeft(2, '0')}';
              }
            }
          }
        }
      }
    }
    return best;
  }
}
```

## Golang

```go
import "fmt"

func largestTimeFromDigits(arr []int) string {
	max := -1
	for i := 0; i < 4; i++ {
		for j := 0; j < 4; j++ {
			if j == i {
				continue
			}
			for k := 0; k < 4; k++ {
				if k == i || k == j {
					continue
				}
				l := 6 - i - j - k // remaining index
				hour := arr[i]*10 + arr[j]
				minute := arr[k]*10 + arr[l]
				if hour < 24 && minute < 60 {
					total := hour*60 + minute
					if total > max {
						max = total
					}
				}
			}
		}
	}
	if max == -1 {
		return ""
	}
	h := max / 60
	m := max % 60
	return fmt.Sprintf("%02d:%02d", h, m)
}
```

## Ruby

```ruby
def largest_time_from_digits(arr)
  max_time = -1
  arr.permutation.each do |p|
    hour = p[0] * 10 + p[1]
    minute = p[2] * 10 + p[3]
    if hour < 24 && minute < 60
      total = hour * 60 + minute
      max_time = total if total > max_time
    end
  end
  return "" if max_time == -1
  format("%02d:%02d", max_time / 60, max_time % 60)
end
```

## Scala

```scala
object Solution {
    def largestTimeFromDigits(arr: Array[Int]): String = {
        var best = -1
        val a = arr.clone()
        def swap(i: Int, j: Int): Unit = {
            val tmp = a(i)
            a(i) = a(j)
            a(j) = tmp
        }
        def backtrack(pos: Int): Unit = {
            if (pos == 4) {
                val hour = a(0) * 10 + a(1)
                val minute = a(2) * 10 + a(3)
                if (hour < 24 && minute < 60) {
                    val total = hour * 60 + minute
                    if (total > best) best = total
                }
            } else {
                for (i <- pos until 4) {
                    swap(pos, i)
                    backtrack(pos + 1)
                    swap(pos, i)
                }
            }
        }
        backtrack(0)
        if (best == -1) "" else f"${best / 60}%02d:${best % 60}%02d"
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_time_from_digits(arr: Vec<i32>) -> String {
        let mut max_time = -1;
        let mut best_h = 0;
        let mut best_m = 0;
        for i in 0..4 {
            for j in 0..4 {
                if i == j { continue; }
                let hour = arr[i] * 10 + arr[j];
                if hour >= 24 { continue; }
                for k in 0..4 {
                    if k == i || k == j { continue; }
                    for l in 0..4 {
                        if l == i || l == j || l == k { continue; }
                        let minute = arr[k] * 10 + arr[l];
                        if minute >= 60 { continue; }
                        let total = hour * 60 + minute;
                        if total > max_time {
                            max_time = total;
                            best_h = hour;
                            best_m = minute;
                        }
                    }
                }
            }
        }
        if max_time == -1 {
            "".to_string()
        } else {
            format!("{:02}:{:02}", best_h, best_m)
        }
    }
}
```

## Racket

```racket
(require racket/list)

(define (permute lst)
  (if (null? lst)
      (list '())
      (apply append
             (for/list ([i (in-range (length lst))])
               (let* ((x (list-ref lst i))
                      (rest (append (take lst i) (drop lst (+ i 1)))))
                 (map (lambda (p) (cons x p)) (permute rest)))))))

(define/contract (largest-time-from-digits arr)
  (-> (listof exact-integer?) string?)
  (let* ((perms (permute arr))
         (best
          (foldl
           (lambda (p acc)
             (let* ((h (+ (* 10 (first p)) (second p)))
                    (m (+ (* 10 (third p)) (fourth p))))
               (if (and (< h 24) (< m 60))
                   (let ((total (+ (* h 60) m)))
                     (if (> total (car acc))
                         (list total h m)
                         acc))
                   acc)))
           (list -1 0 0)
           perms)))
    (if (= (car best) -1)
        ""
        (format "~02d:~02d" (cadr best) (caddr best)))))
```

## Erlang

```erlang
-module(solution).
-export([largest_time_from_digits/1]).

-spec largest_time_from_digits(Arr :: [integer()]) -> unicode:unicode_binary().
largest_time_from_digits(Arr) ->
    Perms = permutations(Arr),
    {BestTotal, BestH, BestM} = find_best(Perms, -1, 0, 0),
    case BestTotal of
        -1 -> <<>>;
        _ -> list_to_binary(io_lib:format("~2..0B:~2..0B", [BestH, BestM]))
    end.

permutations([]) -> [[]];
permutations(List) ->
    [ [X|Rest] || X <- List,
                 Rest <- permutations(lists:delete(X, List)) ].

find_best([], BestTotal, BestH, BestM) -> {BestTotal, BestH, BestM};
find_best([P|Rest], BestTotal, BestH, BestM) ->
    [H1,H2,M1,M2] = P,
    Hour = H1*10 + H2,
    Minute = M1*10 + M2,
    if
        Hour < 24, Minute < 60 ->
            Total = Hour*60 + Minute,
            if Total > BestTotal ->
                find_best(Rest, Total, Hour, Minute);
               true ->
                find_best(Rest, BestTotal, BestH, BestM)
            end;
        true ->
            find_best(Rest, BestTotal, BestH, BestM)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_time_from_digits(arr :: [integer]) :: String.t()
  def largest_time_from_digits(arr) do
    {_, ans} =
      Enum.reduce(permutations(arr), {-1, ""}, fn
        [h1, h2, m1, m2], {max_total, best_str} ->
          hour = h1 * 10 + h2
          minute = m1 * 10 + m2

          if hour < 24 and minute < 60 do
            total = hour * 60 + minute

            if total > max_total do
              formatted =
                :io_lib.format("~2..0B:~2..0B", [hour, minute])
                |> List.to_string()

              {total, formatted}
            else
              {max_total, best_str}
            end
          else
            {max_total, best_str}
          end
      end)

    ans
  end

  defp permutations([]), do: [[]]

  defp permutations(list) do
    for i <- 0..length(list) - 1,
        {elem, rest} = List.pop_at(list, i),
        perm <- permutations(rest),
        do: [elem | perm]
  end
end
```
