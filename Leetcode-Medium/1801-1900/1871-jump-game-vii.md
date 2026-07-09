# 1871. Jump Game VII

## Cpp

```cpp
class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int n = s.size();
        vector<int> dp(n, 0), pref(n, 0);
        dp[0] = 1;
        pref[0] = 1;
        for (int i = 1; i < n; ++i) {
            if (s[i] == '0') {
                int left = i - maxJump;
                int right = i - minJump;
                if (right >= 0) {
                    left = max(left, 0);
                    int sum = pref[right] - (left > 0 ? pref[left - 1] : 0);
                    if (sum > 0) dp[i] = 1;
                }
            }
            pref[i] = pref[i - 1] + dp[i];
        }
        return dp[n - 1] == 1;
    }
};
```

## Java

```java
class Solution {
    public boolean canReach(String s, int minJump, int maxJump) {
        int n = s.length();
        boolean[] dp = new boolean[n];
        int[] pre = new int[n];
        dp[0] = true;
        pre[0] = 1;
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == '0') {
                int left = i - maxJump;
                int right = i - minJump;
                if (right >= 0) {
                    int lIdx = Math.max(left, 0);
                    int count = pre[right] - (lIdx > 0 ? pre[lIdx - 1] : 0);
                    dp[i] = count > 0;
                }
            }
            pre[i] = pre[i - 1] + (dp[i] ? 1 : 0);
        }
        return dp[n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        dp = [False] * n
        dp[0] = True
        cnt = 0  # number of reachable positions within the current window

        for i in range(1, n):
            # add position that just entered the window
            if i - minJump >= 0 and dp[i - minJump]:
                cnt += 1
            # remove position that just left the window
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                cnt -= 1

            if s[i] == '0' and cnt > 0:
                dp[i] = True

        return dp[-1]
```

## Python3

```python
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        window = 0
        for i in range(1, n):
            if i - minJump >= 0:
                window += dp[i - minJump]
            if i - maxJump - 1 >= 0:
                window -= dp[i - maxJump - 1]
            if s[i] == '0' and window > 0:
                dp[i] = 1
        return bool(dp[-1])
```

## C

```c
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool canReach(char* s, int minJump, int maxJump) {
    int n = strlen(s);
    bool *dp = (bool *)calloc(n, sizeof(bool));
    dp[0] = true;
    int cnt = 0; // number of reachable positions in current window

    for (int i = 1; i < n; ++i) {
        if (i - minJump >= 0) {
            cnt += dp[i - minJump];
        }
        if (i - maxJump - 1 >= 0) {
            cnt -= dp[i - maxJump - 1];
        }
        if (s[i] == '0' && cnt > 0) {
            dp[i] = true;
        }
    }

    bool result = dp[n - 1];
    free(dp);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CanReach(string s, int minJump, int maxJump)
    {
        int n = s.Length;
        bool[] reachable = new bool[n];
        reachable[0] = true;
        int windowCount = 0;

        for (int i = 1; i < n; i++)
        {
            int addIdx = i - minJump;
            if (addIdx >= 0 && reachable[addIdx])
                windowCount++;

            int removeIdx = i - maxJump - 1;
            if (removeIdx >= 0 && reachable[removeIdx])
                windowCount--;

            if (s[i] == '0' && windowCount > 0)
                reachable[i] = true;
        }

        return reachable[n - 1];
    }
}
```

## Javascript

```javascript
var canReach = function(s, minJump, maxJump) {
    const n = s.length;
    const reachable = new Uint8Array(n);
    reachable[0] = 1;
    let cnt = 0;
    for (let i = 1; i < n; ++i) {
        const left = i - maxJump;
        const right = i - minJump;
        if (right >= 0) cnt += reachable[right];
        if (left - 1 >= 0) cnt -= reachable[left - 1];
        if (s.charAt(i) === '0' && cnt > 0) reachable[i] = 1;
    }
    return !!reachable[n - 1];
};
```

## Typescript

```typescript
function canReach(s: string, minJump: number, maxJump: number): boolean {
    const n = s.length;
    const reachable = new Uint8Array(n);
    reachable[0] = 1;
    let windowSum = 0;

    for (let i = 1; i < n; i++) {
        if (i - minJump >= 0) {
            windowSum += reachable[i - minJump];
        }
        if (i - maxJump - 1 >= 0) {
            windowSum -= reachable[i - maxJump - 1];
        }

        if (s.charAt(i) === '0' && windowSum > 0) {
            reachable[i] = 1;
        }
    }

    return reachable[n - 1] === 1;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $minJump
     * @param Integer $maxJump
     * @return Boolean
     */
    function canReach($s, $minJump, $maxJump) {
        $n = strlen($s);
        $dp = array_fill(0, $n, false);
        $dp[0] = true;
        $pre = 0; // number of reachable positions in the current sliding window

        for ($i = 1; $i < $n; $i++) {
            $addIdx = $i - $minJump;
            if ($addIdx >= 0 && $dp[$addIdx]) {
                $pre++;
            }

            $removeIdx = $i - $maxJump - 1;
            if ($removeIdx >= 0 && $dp[$removeIdx]) {
                $pre--;
            }

            if ($s[$i] === '0' && $pre > 0) {
                $dp[$i] = true;
            }
        }

        return $dp[$n - 1];
    }
}
```

## Swift

```swift
class Solution {
    func canReach(_ s: String, _ minJump: Int, _ maxJump: Int) -> Bool {
        let chars = Array(s)
        let n = chars.count
        var reachable = [Bool](repeating: false, count: n)
        reachable[0] = true
        var windowCount = 0
        
        for i in 1..<n {
            // index that enters the sliding window
            if i - minJump >= 0 && reachable[i - minJump] {
                windowCount += 1
            }
            // index that leaves the sliding window
            if i - maxJump - 1 >= 0 && reachable[i - maxJump - 1] {
                windowCount -= 1
            }
            if chars[i] == "0" && windowCount > 0 {
                reachable[i] = true
            }
        }
        return reachable[n - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canReach(s: String, minJump: Int, maxJump: Int): Boolean {
        val n = s.length
        val reachable = BooleanArray(n)
        reachable[0] = true
        var windowCount = 0
        for (i in 1 until n) {
            if (i - minJump >= 0 && reachable[i - minJump]) {
                windowCount++
            }
            if (i - maxJump - 1 >= 0 && reachable[i - maxJump - 1]) {
                windowCount--
            }
            if (s[i] == '0' && windowCount > 0) {
                reachable[i] = true
            }
        }
        return reachable[n - 1]
    }
}
```

## Dart

```dart
class Solution {
  bool canReach(String s, int minJump, int maxJump) {
    int n = s.length;
    List<bool> reachable = List.filled(n, false);
    reachable[0] = true;
    int good = 0; // number of reachable positions in the current window

    for (int i = 1; i < n; ++i) {
      if (i - minJump >= 0 && reachable[i - minJump]) {
        good++;
      }
      if (i - maxJump - 1 >= 0 && reachable[i - maxJump - 1]) {
        good--;
      }
      if (s.codeUnitAt(i) == 48 && good > 0) { // '0' ASCII code is 48
        reachable[i] = true;
      }
    }

    return reachable[n - 1];
  }
}
```

## Golang

```go
func canReach(s string, minJump int, maxJump int) bool {
    n := len(s)
    if s[n-1] != '0' {
        return false
    }
    reachable := make([]int, n)
    prefix := make([]int, n)
    reachable[0] = 1
    prefix[0] = 1

    for i := 1; i < n; i++ {
        if s[i] == '0' {
            left := i - maxJump
            if left < 0 {
                left = 0
            }
            right := i - minJump
            if right >= 0 && left <= right {
                sum := prefix[right]
                if left > 0 {
                    sum -= prefix[left-1]
                }
                if sum > 0 {
                    reachable[i] = 1
                }
            }
        }
        prefix[i] = prefix[i-1] + reachable[i]
    }
    return reachable[n-1] == 1
}
```

## Ruby

```ruby
def can_reach(s, min_jump, max_jump)
  n = s.length
  dp = Array.new(n, false)
  dp[0] = true
  cnt = 0

  (min_jump...n).each do |i|
    cnt += 1 if dp[i - min_jump]

    remove_idx = i - max_jump - 1
    cnt -= 1 if remove_idx >= 0 && dp[remove_idx]

    dp[i] = true if s.getbyte(i) == 48 && cnt > 0
  end

  dp[n - 1]
end
```

## Scala

```scala
object Solution {
    def canReach(s: String, minJump: Int, maxJump: Int): Boolean = {
        val n = s.length
        val reachable = new Array[Boolean](n)
        reachable(0) = true
        var windowCount = 0

        for (i <- 1 until n) {
            // Add the position that becomes eligible for the window
            if (i - minJump >= 0 && reachable(i - minJump)) {
                windowCount += 1
            }
            // Remove the position that leaves the window
            if (i - maxJump - 1 >= 0 && reachable(i - maxJump - 1)) {
                windowCount -= 1
            }

            if (s.charAt(i) == '0' && windowCount > 0) {
                reachable(i) = true
            }
        }

        reachable(n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_reach(s: String, min_jump: i32, max_jump: i32) -> bool {
        let n = s.len();
        let bytes = s.as_bytes();
        let min = min_jump as usize;
        let max = max_jump as usize;

        let mut dp = vec![false; n];
        dp[0] = true;
        let mut cnt: i32 = 0;

        for i in 1..n {
            if i >= min && dp[i - min] {
                cnt += 1;
            }
            if i > max && dp[i - max - 1] {
                cnt -= 1;
            }
            if bytes[i] == b'0' && cnt > 0 {
                dp[i] = true;
            }
        }

        dp[n - 1]
    }
}
```

## Racket

```racket
(define/contract (can-reach s minJump maxJump)
  (-> string? exact-integer? exact-integer? boolean?)
  (let* ((n (string-length s))
         (reach (make-vector n #f)))
    (vector-set! reach 0 #t)
    (let loop ((i 1) (window 0))
      (if (= i n)
          (vector-ref reach (- n 1))
          (let* ((add-idx (- i minJump))
                 (remove-idx (- i maxJump 1))
                 (window-after-add
                  (if (and (>= add-idx 0) (vector-ref reach add-idx))
                      (+ window 1)
                      window))
                 (window-after-remove
                  (if (and (>= remove-idx 0) (vector-ref reach remove-idx))
                      (- window-after-add 1)
                      window-after-add))
                 (can (and (= (string-ref s i) #\0)
                           (> window-after-remove 0))))
            (vector-set! reach i can)
            (loop (+ i 1) window-after-remove))))))
```

## Erlang

```erlang
-spec can_reach(S :: binary(), MinJump :: integer(), MaxJump :: integer()) -> boolean().
can_reach(S, MinJump, MaxJump) ->
    N = byte_size(S),
    Reach0 = array:new(N, [{default,false}]),
    Reach1 = array:set(0, true, Reach0),
    {FinalReach,_} = loop(1, N, S, MinJump, MaxJump, Reach1, 0),
    array:get(N-1, FinalReach).

loop(I, N, _S, _MinJump, _MaxJump, Reach, Win) when I >= N ->
    {Reach, Win};
loop(I, N, S, MinJump, MaxJump, Reach, Win) ->
    %% add position that just entered the window
    Win1 = case I - MinJump >= 0 of
               true ->
                   case array:get(I - MinJump, Reach) of
                       true -> Win + 1;
                       false -> Win
                   end;
               false -> Win
           end,
    %% remove position that left the window
    Win2 = case I - MaxJump - 1 >= 0 of
               true ->
                   case array:get(I - MaxJump - 1, Reach) of
                       true -> Win1 - 1;
                       false -> Win1
                   end;
               false -> Win1
           end,
    Char = binary:at(S, I),
    ReachableI = (Win2 > 0) andalso (Char == $0),
    NewReach = array:set(I, ReachableI, Reach),
    loop(I + 1, N, S, MinJump, MaxJump, NewReach, Win2).
```

## Elixir

```elixir
defmodule Solution do
  @spec can_reach(s :: String.t(), min_jump :: integer, max_jump :: integer) :: boolean
  def can_reach(s, min_jump, max_jump) do
    len = byte_size(s)
    bytes = :binary.bin_to_list(s)
    s_arr = :array.from_list(bytes)

    dp = :array.new(len, default: 0)
    dp = :array.set(0, 1, dp)

    cnt = 0

    {dp_final, _} =
      Enum.reduce(1..(len - 1), {dp, cnt}, fn i, {arr, c} ->
        c =
          if i - min_jump >= 0 do
            if :array.get(i - min_jump, arr) == 1, do: c + 1, else: c
          else
            c
          end

        c =
          if i - max_jump - 1 >= 0 do
            if :array.get(i - max_jump - 1, arr) == 1, do: c - 1, else: c
          else
            c
          end

        reachable = c > 0 and :array.get(i, s_arr) == ?0
        arr = :array.set(i, if(reachable, do: 1, else: 0), arr)
        {arr, c}
      end)

    :array.get(len - 1, dp_final) == 1
  end
end
```
