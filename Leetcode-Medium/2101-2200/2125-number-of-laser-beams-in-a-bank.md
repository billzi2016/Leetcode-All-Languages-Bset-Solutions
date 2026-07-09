# 2125. Number of Laser Beams in a Bank

## Cpp

```cpp
class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        long long ans = 0;
        int prev = 0;
        for (const string& row : bank) {
            int cnt = 0;
            for (char c : row) if (c == '1') ++cnt;
            if (cnt > 0) {
                ans += static_cast<long long>(prev) * cnt;
                prev = cnt;
            }
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    public int numberOfBeams(String[] bank) {
        int prev = 0;
        int ans = 0;
        for (String row : bank) {
            int cnt = 0;
            for (int i = 0; i < row.length(); i++) {
                if (row.charAt(i) == '1') {
                    cnt++;
                }
            }
            if (cnt > 0) {
                ans += prev * cnt;
                prev = cnt;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        prev = 0
        ans = 0
        for row in bank:
            cnt = row.count('1')
            if cnt:
                ans += prev * cnt
                prev = cnt
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0
        for row in bank:
            cnt = row.count('1')
            if cnt:
                ans += prev * cnt
                prev = cnt
        return ans
```

## C

```c
int numberOfBeams(char** bank, int bankSize) {
    long long ans = 0;
    int prev = 0;
    for (int i = 0; i < bankSize; ++i) {
        int cnt = 0;
        char *row = bank[i];
        while (*row) {
            if (*row == '1') ++cnt;
            ++row;
        }
        if (cnt > 0) {
            ans += (long long)prev * cnt;
            prev = cnt;
        }
    }
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumberOfBeams(string[] bank)
    {
        long ans = 0;
        int prev = 0;
        foreach (var row in bank)
        {
            int cnt = 0;
            foreach (char c in row)
                if (c == '1')
                    cnt++;
            if (cnt > 0)
            {
                ans += (long)prev * cnt;
                prev = cnt;
            }
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} bank
 * @return {number}
 */
var numberOfBeams = function(bank) {
    let prev = 0;
    let ans = 0;
    for (const row of bank) {
        let cnt = 0;
        for (const ch of row) {
            if (ch === '1') cnt++;
        }
        if (cnt > 0) {
            ans += prev * cnt;
            prev = cnt;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function numberOfBeams(bank: string[]): number {
    let prev = 0;
    let ans = 0;
    for (const row of bank) {
        let cnt = 0;
        for (let i = 0; i < row.length; ++i) {
            if (row[i] === '1') cnt++;
        }
        if (cnt > 0) {
            ans += prev * cnt;
            prev = cnt;
        }
    }
    return ans;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param String[] $bank
     * @return int
     */
    function numberOfBeams($bank) {
        $prev = 0;
        $ans = 0;
        foreach ($bank as $row) {
            $count = substr_count($row, '1');
            if ($count > 0) {
                $ans += $prev * $count;
                $prev = $count;
            }
        }
        return $ans;
    }
}
?>
```

## Swift

```swift
class Solution {
    func numberOfBeams(_ bank: [String]) -> Int {
        var prev = 0
        var ans = 0
        for row in bank {
            var cnt = 0
            for ch in row {
                if ch == "1" { cnt += 1 }
            }
            if cnt > 0 {
                ans += prev * cnt
                prev = cnt
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfBeams(bank: Array<String>): Int {
        var prev = 0
        var ans = 0
        for (row in bank) {
            var cnt = 0
            for (ch in row) {
                if (ch == '1') cnt++
            }
            if (cnt > 0) {
                ans += prev * cnt
                prev = cnt
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int numberOfBeams(List<String> bank) {
    int prev = 0;
    int ans = 0;
    for (final row in bank) {
      int count = 0;
      for (int i = 0; i < row.length; ++i) {
        if (row.codeUnitAt(i) == 49) { // '1'
          count++;
        }
      }
      if (count > 0) {
        ans += prev * count;
        prev = count;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func numberOfBeams(bank []string) int {
    prev := 0
    ans := 0
    for _, row := range bank {
        cnt := 0
        for _, ch := range row {
            if ch == '1' {
                cnt++
            }
        }
        if cnt > 0 {
            ans += prev * cnt
            prev = cnt
        }
    }
    return ans
}
```

## Ruby

```ruby
def number_of_beams(bank)
  prev = 0
  ans = 0
  bank.each do |row|
    cnt = row.count('1')
    if cnt > 0
      ans += prev * cnt
      prev = cnt
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def numberOfBeams(bank: Array[String]): Int = {
        var prev = 0
        var ans: Long = 0L
        for (row <- bank) {
            val cnt = row.count(_ == '1')
            if (cnt > 0) {
                ans += prev.toLong * cnt
                prev = cnt
            }
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_beams(bank: Vec<String>) -> i32 {
        let mut prev = 0i32;
        let mut ans = 0i32;
        for row in bank.iter() {
            let count = row.bytes().filter(|&c| c == b'1').count() as i32;
            if count > 0 {
                ans += prev * count;
                prev = count;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (number-of-beams bank)
  (-> (listof string?) exact-integer?)
  (let loop ((rows bank) (prev 0) (ans 0))
    (if (null? rows)
        ans
        (let* ((row (car rows))
               (count (for/sum ([c (in-string row)]) (if (char=? c #\1) 1 0))))
          (if (= count 0)
              (loop (cdr rows) prev ans)
              (loop (cdr rows) count (+ ans (* prev count))))))))
```

## Erlang

```erlang
-spec number_of_beams(Bank :: [unicode:unicode_binary()]) -> integer().
number_of_beams(Bank) ->
    {_, Ans} = lists:foldl(
        fun(Row, {Prev, Acc}) ->
            Count = count_ones(Row),
            case Count of
                0 -> {Prev, Acc};
                _ -> {Count, Acc + Prev * Count}
            end
        end,
        {0, 0},
        Bank
    ),
    Ans.

count_ones(<<>>) -> 0;
count_ones(<<C, Rest/binary>>) ->
    (if C =:= $1 -> 1; true -> 0 end) + count_ones(Rest).
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_beams(bank :: [String.t]) :: integer
  def number_of_beams(bank) do
    {ans, _prev} =
      Enum.reduce(bank, {0, 0}, fn row, {acc, prev} ->
        cnt = String.count(row, "1")

        if cnt == 0 do
          {acc, prev}
        else
          {acc + prev * cnt, cnt}
        end
      end)

    ans
  end
end
```
