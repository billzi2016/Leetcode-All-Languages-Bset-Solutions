# 1629. Slowest Key

## Cpp

```cpp
#include <vector>
#include <string>

class Solution {
public:
    char slowestKey(std::vector<int>& releaseTimes, std::string keysPressed) {
        int n = releaseTimes.size();
        int longest = releaseTimes[0];
        char ans = keysPressed[0];
        for (int i = 1; i < n; ++i) {
            int duration = releaseTimes[i] - releaseTimes[i - 1];
            if (duration > longest || (duration == longest && keysPressed[i] > ans)) {
                longest = duration;
                ans = keysPressed[i];
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public char slowestKey(int[] releaseTimes, String keysPressed) {
        int n = releaseTimes.length;
        char slowest = keysPressed.charAt(0);
        int maxDuration = releaseTimes[0];
        for (int i = 1; i < n; i++) {
            int duration = releaseTimes[i] - releaseTimes[i - 1];
            char key = keysPressed.charAt(i);
            if (duration > maxDuration || (duration == maxDuration && key > slowest)) {
                maxDuration = duration;
                slowest = key;
            }
        }
        return slowest;
    }
}
```

## Python

```python
class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        max_duration = releaseTimes[0]
        slowest_key = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > max_duration or (duration == max_duration and keysPressed[i] > slowest_key):
                max_duration = duration
                slowest_key = keysPressed[i]
        return slowest_key
```

## Python3

```python
from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        slowest = keysPressed[0]
        max_duration = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > max_duration or (duration == max_duration and keysPressed[i] > slowest):
                max_duration = duration
                slowest = keysPressed[i]
        return slowest
```

## C

```c
char slowestKey(int* releaseTimes, int releaseTimesSize, char* keysPressed) {
    int longest = releaseTimes[0];
    char ans = keysPressed[0];
    for (int i = 1; i < releaseTimesSize; ++i) {
        int duration = releaseTimes[i] - releaseTimes[i - 1];
        if (duration > longest || (duration == longest && keysPressed[i] > ans)) {
            longest = duration;
            ans = keysPressed[i];
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public char SlowestKey(int[] releaseTimes, string keysPressed)
    {
        int n = releaseTimes.Length;
        char slowest = keysPressed[0];
        int longest = releaseTimes[0];

        for (int i = 1; i < n; i++)
        {
            int duration = releaseTimes[i] - releaseTimes[i - 1];
            char currentKey = keysPressed[i];

            if (duration > longest || (duration == longest && currentKey > slowest))
            {
                longest = duration;
                slowest = currentKey;
            }
        }

        return slowest;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} releaseTimes
 * @param {string} keysPressed
 * @return {character}
 */
var slowestKey = function(releaseTimes, keysPressed) {
    let longest = releaseTimes[0];
    let result = keysPressed[0];
    for (let i = 1; i < releaseTimes.length; i++) {
        const duration = releaseTimes[i] - releaseTimes[i - 1];
        const key = keysPressed[i];
        if (duration > longest || (duration === longest && key > result)) {
            longest = duration;
            result = key;
        }
    }
    return result;
};
```

## Typescript

```typescript
function slowestKey(releaseTimes: number[], keysPressed: string): string {
    let longestPress = releaseTimes[0];
    let slowestKey = keysPressed[0];
    for (let i = 1; i < releaseTimes.length; i++) {
        const duration = releaseTimes[i] - releaseTimes[i - 1];
        const key = keysPressed[i];
        if (duration > longestPress || (duration === longestPress && key > slowestKey)) {
            longestPress = duration;
            slowestKey = key;
        }
    }
    return slowestKey;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $releaseTimes
     * @param String $keysPressed
     * @return String
     */
    function slowestKey($releaseTimes, $keysPressed) {
        $n = count($releaseTimes);
        $slowest = $keysPressed[0];
        $longest = $releaseTimes[0];

        for ($i = 1; $i < $n; $i++) {
            $duration = $releaseTimes[$i] - $releaseTimes[$i - 1];
            $key = $keysPressed[$i];
            if ($duration > $longest || ($duration == $longest && $key > $slowest)) {
                $longest = $duration;
                $slowest = $key;
            }
        }

        return $slowest;
    }
}
```

## Swift

```swift
class Solution {
    func slowestKey(_ releaseTimes: [Int], _ keysPressed: String) -> Character {
        let keys = Array(keysPressed)
        var maxDuration = releaseTimes[0]
        var result = keys[0]
        for i in 1..<releaseTimes.count {
            let duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > maxDuration || (duration == maxDuration && keys[i] > result) {
                maxDuration = duration
                result = keys[i]
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun slowestKey(releaseTimes: IntArray, keysPressed: String): Char {
        var maxDuration = releaseTimes[0]
        var result = keysPressed[0]
        for (i in 1 until releaseTimes.size) {
            val duration = releaseTimes[i] - releaseTimes[i - 1]
            val key = keysPressed[i]
            if (duration > maxDuration || (duration == maxDuration && key > result)) {
                maxDuration = duration
                result = key
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  String slowestKey(List<int> releaseTimes, String keysPressed) {
    int maxDuration = releaseTimes[0];
    String slowest = keysPressed[0];

    for (int i = 1; i < releaseTimes.length; i++) {
      int duration = releaseTimes[i] - releaseTimes[i - 1];
      String curKey = keysPressed[i];
      if (duration > maxDuration ||
          (duration == maxDuration && curKey.codeUnitAt(0) > slowest.codeUnitAt(0))) {
        maxDuration = duration;
        slowest = curKey;
      }
    }

    return slowest;
  }
}
```

## Golang

```go
func slowestKey(releaseTimes []int, keysPressed string) byte {
    if len(releaseTimes) == 0 || len(keysPressed) == 0 {
        return 0
    }
    longest := releaseTimes[0]
    ans := keysPressed[0]
    for i := 1; i < len(releaseTimes); i++ {
        duration := releaseTimes[i] - releaseTimes[i-1]
        if duration > longest || (duration == longest && keysPressed[i] > ans) {
            longest = duration
            ans = keysPressed[i]
        }
    }
    return ans
}
```

## Ruby

```ruby
def slowest_key(release_times, keys_pressed)
  max_duration = release_times[0]
  slowest = keys_pressed[0]

  (1...release_times.length).each do |i|
    duration = release_times[i] - release_times[i - 1]
    if duration > max_duration || (duration == max_duration && keys_pressed[i] > slowest)
      max_duration = duration
      slowest = keys_pressed[i]
    end
  end

  slowest
end
```

## Scala

```scala
object Solution {
    def slowestKey(releaseTimes: Array[Int], keysPressed: String): Char = {
        var maxDuration = releaseTimes(0)
        var result = keysPressed.charAt(0)
        for (i <- 1 until releaseTimes.length) {
            val duration = releaseTimes(i) - releaseTimes(i - 1)
            val key = keysPressed.charAt(i)
            if (duration > maxDuration || (duration == maxDuration && key > result)) {
                maxDuration = duration
                result = key
            }
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn slowest_key(release_times: Vec<i32>, keys_pressed: String) -> char {
        let bytes = keys_pressed.as_bytes();
        let mut max_duration = release_times[0];
        let mut result = bytes[0] as char;
        for i in 1..release_times.len() {
            let duration = release_times[i] - release_times[i - 1];
            let key = bytes[i] as char;
            if duration > max_duration || (duration == max_duration && key > result) {
                max_duration = duration;
                result = key;
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (slowest-key releaseTimes keysPressed)
  (-> (listof exact-integer?) string? char?)
  (let* ((first-duration (car releaseTimes))
         (slowest-char   (string-ref keysPressed 0)))
    (let loop ((prev first-duration)
               (rest (cdr releaseTimes))
               (idx 1)
               (slowest slowest-char)
               (maxd first-duration))
      (if (null? rest)
          slowest
          (let* ((curr-time (car rest))
                 (duration (- curr-time prev))
                 (curr-char (string-ref keysPressed idx))
                 (new-slowest (if (or (> duration maxd)
                                      (and (= duration maxd) (char>? curr-char slowest)))
                                  curr-char
                                  slowest))
                 (new-maxd   (if (or (> duration maxd)
                                      (and (= duration maxd) (char>? curr-char slowest)))
                                  duration
                                  maxd)))
            (loop curr-time (cdr rest) (+ idx 1) new-slowest new-maxd))))))
```

## Erlang

```erlang
-module(solution).
-export([slowest_key/2]).

-spec slowest_key(ReleaseTimes :: [integer()], KeysPressed :: unicode:unicode_binary()) -> char().
slowest_key([], _Keys) ->
    0;
slowest_key([FirstTime | RestTimes], KeysPressed) ->
    FirstChar = binary:at(KeysPressed, 0),
    loop(RestTimes, KeysPressed, 1, FirstTime, FirstTime, FirstChar).

loop([], _Keys, _Idx, _PrevTime, _MaxDur, MaxChar) ->
    MaxChar;
loop([CurrTime | Rest], Keys, Idx, PrevTime, MaxDur, MaxChar) ->
    Char = binary:at(Keys, Idx),
    Dur = CurrTime - PrevTime,
    {NewMaxDur, NewMaxChar} =
        if
            Dur > MaxDur -> {Dur, Char};
            Dur == MaxDur andalso Char > MaxChar -> {Dur, Char};
            true -> {MaxDur, MaxChar}
        end,
    loop(Rest, Keys, Idx + 1, CurrTime, NewMaxDur, NewMaxChar).
```

## Elixir

```elixir
defmodule Solution do
  @spec slowest_key(release_times :: [integer], keys_pressed :: String.t) :: char
  def slowest_key(release_times, keys_pressed) do
    keys = String.graphemes(keys_pressed)

    # Initial values from the first key press
    max_duration = hd(release_times)
    slowest_key = List.first(keys)

    {_, result_key, _} =
      Enum.reduce(
        Enum.zip(tl(release_times), tl(keys)),
        {max_duration, slowest_key, hd(release_times)},
        fn {curr_time, key}, {cur_max, cur_key, prev_time} ->
          duration = curr_time - prev_time

          cond do
            duration > cur_max ->
              {duration, key, curr_time}

            duration == cur_max and key > cur_key ->
              {duration, key, curr_time}

            true ->
              {cur_max, cur_key, curr_time}
          end
        end
      )

    result_key
  end
end
```
