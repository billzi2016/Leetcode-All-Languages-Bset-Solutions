# 2491. Divide Players Into Teams of Equal Skill

## Cpp

```cpp
class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        int n = skill.size();
        sort(skill.begin(), skill.end());
        long long target = (long long)skill[0] + skill[n - 1];
        long long totalChemistry = 0;
        for (int i = 0; i < n / 2; ++i) {
            if ((long long)skill[i] + skill[n - 1 - i] != target) return -1;
            totalChemistry += (long long)skill[i] * skill[n - 1 - i];
        }
        return totalChemistry;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public long dividePlayers(int[] skill) {
        int n = skill.length;
        Arrays.sort(skill);
        int target = skill[0] + skill[n - 1];
        long totalChemistry = 0L;
        for (int i = 0; i < n / 2; i++) {
            if (skill[i] + skill[n - 1 - i] != target) {
                return -1;
            }
            totalChemistry += (long) skill[i] * skill[n - 1 - i];
        }
        return totalChemistry;
    }
}
```

## Python

```python
class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        n = len(skill)
        target = skill[0] + skill[-1]
        total = 0
        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != target:
                return -1
            total += skill[i] * skill[n - 1 - i]
        return total
```

## Python3

```python
from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        target = skill[0] + skill[-1]
        total = 0
        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != target:
                return -1
            total += skill[i] * skill[n - 1 - i]
        return total
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

long long dividePlayers(int* skill, int skillSize) {
    if (skillSize % 2 != 0) return -1;
    qsort(skill, (size_t)skillSize, sizeof(int), cmp_int);
    
    int target = skill[0] + skill[skillSize - 1];
    long long totalChemistry = 0;
    
    for (int i = 0; i < skillSize / 2; ++i) {
        int left = skill[i];
        int right = skill[skillSize - 1 - i];
        if (left + right != target) return -1;
        totalChemistry += (long long)left * right;
    }
    
    return totalChemistry;
}
```

## Csharp

```csharp
public class Solution
{
    public long DividePlayers(int[] skill)
    {
        int n = skill.Length;
        System.Array.Sort(skill);
        int target = skill[0] + skill[n - 1];
        long total = 0;
        for (int i = 0; i < n / 2; i++)
        {
            if (skill[i] + skill[n - 1 - i] != target)
                return -1;
            total += (long)skill[i] * skill[n - 1 - i];
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} skill
 * @return {number}
 */
var dividePlayers = function(skill) {
    skill.sort((a, b) => a - b);
    const n = skill.length;
    const target = skill[0] + skill[n - 1];
    let total = 0;
    for (let i = 0; i < n / 2; i++) {
        if (skill[i] + skill[n - 1 - i] !== target) return -1;
        total += skill[i] * skill[n - 1 - i];
    }
    return total;
};
```

## Typescript

```typescript
function dividePlayers(skill: number[]): number {
    const n = skill.length;
    skill.sort((a, b) => a - b);
    const target = skill[0] + skill[n - 1];
    let totalChemistry = 0;
    for (let i = 0; i < n / 2; i++) {
        const left = skill[i];
        const right = skill[n - 1 - i];
        if (left + right !== target) return -1;
        totalChemistry += left * right;
    }
    return totalChemistry;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $skill
     * @return Integer
     */
    function dividePlayers($skill) {
        $n = count($skill);
        sort($skill, SORT_NUMERIC);
        $target = $skill[0] + $skill[$n - 1];
        $totalChemistry = 0;
        for ($i = 0; $i < $n / 2; $i++) {
            $j = $n - 1 - $i;
            if ($skill[$i] + $skill[$j] !== $target) {
                return -1;
            }
            $totalChemistry += $skill[$i] * $skill[$j];
        }
        return $totalChemistry;
    }
}
```

## Swift

```swift
class Solution {
    func dividePlayers(_ skill: [Int]) -> Int {
        let n = skill.count
        var sortedSkills = skill.sorted()
        let targetSum = sortedSkills[0] + sortedSkills[n - 1]
        var totalChemistry = 0
        
        for i in 0..<(n / 2) {
            let left = sortedSkills[i]
            let right = sortedSkills[n - 1 - i]
            if left + right != targetSum {
                return -1
            }
            totalChemistry += left * right
        }
        
        return totalChemistry
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun dividePlayers(skill: IntArray): Long {
        skill.sort()
        val n = skill.size
        val target = skill[0] + skill[n - 1]
        var total = 0L
        var i = 0
        var j = n - 1
        while (i < j) {
            if (skill[i] + skill[j] != target) return -1L
            total += skill[i].toLong() * skill[j].toLong()
            i++
            j--
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int dividePlayers(List<int> skill) {
    int n = skill.length;
    skill.sort();
    int target = skill[0] + skill[n - 1];
    int totalChemistry = 0;
    for (int i = 0; i < n ~/ 2; i++) {
      int a = skill[i];
      int b = skill[n - 1 - i];
      if (a + b != target) return -1;
      totalChemistry += a * b;
    }
    return totalChemistry;
  }
}
```

## Golang

```go
package main

import (
	"sort"
)

func dividePlayers(skill []int) int64 {
	n := len(skill)
	if n%2 != 0 {
		return -1
	}
	sort.Ints(skill)
	target := skill[0] + skill[n-1]
	var total int64 = 0
	for i := 0; i < n/2; i++ {
		if skill[i]+skill[n-1-i] != target {
			return -1
		}
		total += int64(skill[i]) * int64(skill[n-1-i])
	}
	return total
}
```

## Ruby

```ruby
def divide_players(skill)
  skill.sort!
  n = skill.length
  target = skill[0] + skill[-1]
  total = 0
  (0...(n / 2)).each do |i|
    return -1 if skill[i] + skill[n - 1 - i] != target
    total += skill[i] * skill[n - 1 - i]
  end
  total
end
```

## Scala

```scala
object Solution {
    def dividePlayers(skill: Array[Int]): Long = {
        java.util.Arrays.sort(skill)
        val n = skill.length
        val target = skill(0) + skill(n - 1)
        var total: Long = 0L
        var i = 0
        while (i < n / 2) {
            val j = n - 1 - i
            if (skill(i) + skill(j) != target) return -1L
            total += skill(i).toLong * skill(j)
            i += 1
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn divide_players(skill: Vec<i32>) -> i64 {
        let n = skill.len();
        if n % 2 != 0 {
            return -1;
        }
        let mut s = skill;
        s.sort_unstable();
        let target = s[0] + s[n - 1];
        let mut total: i64 = 0;
        for i in 0..n / 2 {
            if s[i] + s[n - 1 - i] != target {
                return -1;
            }
            total += (s[i] as i64) * (s[n - 1 - i] as i64);
        }
        total
    }
}
```

## Racket

```racket
(define/contract (divide-players skill)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort skill <))
         (n (length sorted)))
    (if (= (modulo n 2) 1)
        -1
        (let ((target (+ (first sorted) (list-ref sorted (- n 1)))))
          (define (loop left right remaining acc)
            (cond
              [(= remaining 0) acc]
              [else
               (let ((a (car left))
                     (b (car right)))
                 (if (not (= (+ a b) target))
                     -1
                     (let ((new-acc (+ acc (* a b))))
                       (loop (cdr left) (cdr right) (- remaining 1) new-acc))))]))
          (loop sorted (reverse sorted) (/ n 2) 0)))))
```

## Erlang

```erlang
-spec divide_players(Skill :: [integer()]) -> integer().
divide_players(Skill) ->
    Sorted = lists:sort(Skill),
    N = length(Sorted),
    Target = hd(Sorted) + lists:nth(N, Sorted),
    RevSorted = lists:reverse(Sorted),
    process_pairs(Sorted, RevSorted, Target, N div 2, 0).

process_pairs(_L1, _L2, _Target, 0, Acc) ->
    Acc;
process_pairs([H1|T1], [H2|T2], Target, Count, Acc) ->
    case H1 + H2 of
        S when S =:= Target ->
            process_pairs(T1, T2, Target, Count - 1, Acc + H1 * H2);
        _ -> -1
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec divide_players(skill :: [integer]) :: integer
  def divide_players(skill) do
    sorted = Enum.sort(skill)
    n = length(sorted)

    target = List.first(sorted) + List.last(sorted)

    Enum.reduce_while(0..(div(n, 2) - 1), 0, fn i, acc ->
      a = Enum.at(sorted, i)
      b = Enum.at(sorted, n - 1 - i)

      if a + b != target do
        {:halt, -1}
      else
        {:cont, acc + a * b}
      end
    end)
  end
end
```
