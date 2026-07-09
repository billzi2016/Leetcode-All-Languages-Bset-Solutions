# 1419. Minimum Number of Frogs Croaking

## Cpp

```cpp
class Solution {
public:
    int minNumberOfFrogs(string croakOfFrogs) {
        // order: c r o a k
        int stage[5] = {0, 0, 0, 0, 0};
        auto idx = [&](char ch)->int{
            switch(ch){
                case 'c': return 0;
                case 'r': return 1;
                case 'o': return 2;
                case 'a': return 3;
                case 'k': return 4;
            }
            return -1;
        };
        int cur = 0, maxFrogs = 0;
        for(char ch : croakOfFrogs){
            int i = idx(ch);
            if(i == 0){ // start of a new croak
                stage[0]++;
                cur++;
                if(cur > maxFrogs) maxFrogs = cur;
            }else{
                if(stage[i-1] == 0) return -1; // no frog to advance
                stage[i-1]--;
                if(i == 4){
                    // croak completed
                    cur--;
                }else{
                    stage[i]++;
                }
            }
        }
        if(cur != 0) return -1;
        return maxFrogs;
    }
};
```

## Java

```java
class Solution {
    public int minNumberOfFrogs(String croakOfFrogs) {
        int[] cnt = new int[4]; // stages: c, r, o, a
        int maxFrogs = 0;
        for (char ch : croakOfFrogs.toCharArray()) {
            switch (ch) {
                case 'c':
                    cnt[0]++;
                    break;
                case 'r':
                    if (cnt[0] == 0) return -1;
                    cnt[0]--;
                    cnt[1]++;
                    break;
                case 'o':
                    if (cnt[1] == 0) return -1;
                    cnt[1]--;
                    cnt[2]++;
                    break;
                case 'a':
                    if (cnt[2] == 0) return -1;
                    cnt[2]--;
                    cnt[3]++;
                    break;
                case 'k':
                    if (cnt[3] == 0) return -1;
                    cnt[3]--;
                    break;
                default:
                    return -1;
            }
            int current = cnt[0] + cnt[1] + cnt[2] + cnt[3];
            if (current > maxFrogs) maxFrogs = current;
        }
        // all stages must be completed
        if (cnt[0] != 0 || cnt[1] != 0 || cnt[2] != 0 || cnt[3] != 0) return -1;
        return maxFrogs;
    }
}
```

## Python

```python
class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        cnt = [0] * 4  # c, r, o, a stages
        cur = 0
        max_frogs = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                cnt[0] += 1
                cur += 1
                if cur > max_frogs:
                    max_frogs = cur
            elif ch == 'r':
                if cnt[0] == 0:
                    return -1
                cnt[0] -= 1
                cnt[1] += 1
            elif ch == 'o':
                if cnt[1] == 0:
                    return -1
                cnt[1] -= 1
                cnt[2] += 1
            elif ch == 'a':
                if cnt[2] == 0:
                    return -1
                cnt[2] -= 1
                cnt[3] += 1
            else:  # ch == 'k'
                if cnt[3] == 0:
                    return -1
                cnt[3] -= 1
                cur -= 1
        if cur != 0 or any(cnt):
            return -1
        return max_frogs
```

## Python3

```python
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        order = {'c':0,'r':1,'o':2,'a':3,'k':4}
        cnt = [0]*5
        max_frogs = 0
        for ch in croakOfFrogs:
            idx = order[ch]
            if idx == 0:  # 'c'
                cnt[0] += 1
            else:
                if cnt[idx-1] == 0:
                    return -1
                cnt[idx-1] -= 1
                if idx < 4:   # not 'k', move to next stage
                    cnt[idx] += 1
            # current active frogs are those in stages c,r,o,a (not yet finished)
            active = sum(cnt[:4])
            if active > max_frogs:
                max_frogs = active
        # after processing, there should be no unfinished croaks
        if any(cnt[i] != 0 for i in range(4)):
            return -1
        return max_frogs
```

## C

```c
int minNumberOfFrogs(char* croakOfFrogs) {
    int stage[4] = {0, 0, 0, 0}; // c, r, o, a
    int max_frogs = 0;
    for (char *p = croakOfFrogs; *p; ++p) {
        char ch = *p;
        if (ch == 'c') {
            stage[0]++;
            int active = stage[0] + stage[1] + stage[2] + stage[3];
            if (active > max_frogs) max_frogs = active;
        } else if (ch == 'r') {
            if (stage[0] == 0) return -1;
            stage[0]--;
            stage[1]++;
        } else if (ch == 'o') {
            if (stage[1] == 0) return -1;
            stage[1]--;
            stage[2]++;
        } else if (ch == 'a') {
            if (stage[2] == 0) return -1;
            stage[2]--;
            stage[3]++;
        } else if (ch == 'k') {
            if (stage[3] == 0) return -1;
            stage[3]--;
        } else {
            return -1;
        }
    }
    if (stage[0] || stage[1] || stage[2] || stage[3]) return -1;
    return max_frogs;
}
```

## Csharp

```csharp
public class Solution {
    public int MinNumberOfFrogs(string croakOfFrogs) {
        int cntC = 0, cntR = 0, cntO = 0, cntA = 0;
        int maxFrogs = 0;
        foreach (char ch in croakOfFrogs) {
            switch (ch) {
                case 'c':
                    cntC++;
                    break;
                case 'r':
                    if (cntC == 0) return -1;
                    cntC--;
                    cntR++;
                    break;
                case 'o':
                    if (cntR == 0) return -1;
                    cntR--;
                    cntO++;
                    break;
                case 'a':
                    if (cntO == 0) return -1;
                    cntO--;
                    cntA++;
                    break;
                case 'k':
                    if (cntA == 0) return -1;
                    cntA--;
                    break;
                default:
                    return -1;
            }
            int current = cntC + cntR + cntO + cntA;
            if (current > maxFrogs) maxFrogs = current;
        }
        if (cntC != 0 || cntR != 0 || cntO != 0 || cntA != 0) return -1;
        return maxFrogs == 0 ? 0 : maxFrogs;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} croakOfFrogs
 * @return {number}
 */
var minNumberOfFrogs = function(croakOfFrogs) {
    const cnt = {c:0, r:0, o:0, a:0, k:0};
    const order = {'c':0,'r':1,'o':2,'a':3,'k':4};
    const stages = ['c','r','o','a','k'];
    let curFrogs = 0;
    let maxFrogs = 0;
    
    for (let ch of croakOfFrogs) {
        cnt[ch]++;
        if (ch !== 'c') {
            const prev = stages[order[ch] - 1];
            if (cnt[prev] < cnt[ch]) return -1; // invalid sequence
        }
        if (ch === 'c') {
            curFrogs++;
            if (curFrogs > maxFrogs) maxFrogs = curFrogs;
        } else if (ch === 'k') {
            curFrogs--;
        }
    }
    
    // all counts must be equal, meaning every croak completed
    const finalCount = cnt['c'];
    if (cnt['r'] !== finalCount || cnt['o'] !== finalCount ||
        cnt['a'] !== finalCount || cnt['k'] !== finalCount) {
        return -1;
    }
    
    return maxFrogs;
};
```

## Typescript

```typescript
function minNumberOfFrogs(croakOfFrogs: string): number {
    const cnt = [0, 0, 0, 0]; // stages for 'c','r','o','a'
    let ongoing = 0;
    let maxFrogs = 0;

    for (const ch of croakOfFrogs) {
        if (ch === 'c') {
            cnt[0]++;
            ongoing++;
            if (ongoing > maxFrogs) maxFrogs = ongoing;
        } else if (ch === 'r') {
            if (cnt[0] === 0) return -1;
            cnt[0]--;
            cnt[1]++;
        } else if (ch === 'o') {
            if (cnt[1] === 0) return -1;
            cnt[1]--;
            cnt[2]++;
        } else if (ch === 'a') {
            if (cnt[2] === 0) return -1;
            cnt[2]--;
            cnt[3]++;
        } else if (ch === 'k') {
            if (cnt[3] === 0) return -1;
            cnt[3]--;
            ongoing--;
        } else {
            // invalid character, though per constraints shouldn't happen
            return -1;
        }
    }

    if (ongoing !== 0) return -1;
    return maxFrogs;
}
```

## Php

```php
class Solution {

    /**
     * @param String $croakOfFrogs
     * @return Integer
     */
    function minNumberOfFrogs($croakOfFrogs) {
        $cnt = ['c'=>0, 'r'=>0, 'o'=>0, 'a'=>0, 'k'=>0];
        $active = 0;
        $maxFrogs = 0;
        $len = strlen($croakOfFrogs);
        for ($i = 0; $i < $len; $i++) {
            $ch = $croakOfFrogs[$i];
            switch ($ch) {
                case 'c':
                    $cnt['c']++;
                    $active++;
                    if ($active > $maxFrogs) {
                        $maxFrogs = $active;
                    }
                    break;
                case 'r':
                    if ($cnt['c'] == 0) return -1;
                    $cnt['c']--;
                    $cnt['r']++;
                    break;
                case 'o':
                    if ($cnt['r'] == 0) return -1;
                    $cnt['r']--;
                    $cnt['o']++;
                    break;
                case 'a':
                    if ($cnt['o'] == 0) return -1;
                    $cnt['o']--;
                    $cnt['a']++;
                    break;
                case 'k':
                    if ($cnt['a'] == 0) return -1;
                    $cnt['a']--;
                    $active--;
                    break;
                default:
                    return -1;
            }
        }
        // after processing, all counts except completed must be zero
        foreach (['c','r','o','a'] as $stage) {
            if ($cnt[$stage] != 0) return -1;
        }
        return $maxFrogs;
    }
}
```

## Swift

```swift
class Solution {
    func minNumberOfFrogs(_ croakOfFrogs: String) -> Int {
        let order: [Character] = ["c", "r", "o", "a", "k"]
        var idxMap = [Character: Int]()
        for (i, ch) in order.enumerated() {
            idxMap[ch] = i
        }
        
        var cnt = Array(repeating: 0, count: 5)
        var currentActive = 0
        var maxFrogs = 0
        
        for ch in croakOfFrogs {
            guard let idx = idxMap[ch] else { return -1 }
            if idx == 0 {
                cnt[0] += 1
                currentActive += 1
                if currentActive > maxFrogs {
                    maxFrogs = currentActive
                }
            } else {
                if cnt[idx - 1] == 0 {
                    return -1
                }
                cnt[idx - 1] -= 1
                if idx == 4 {
                    // finished a croak
                    currentActive -= 1
                } else {
                    cnt[idx] += 1
                }
            }
        }
        
        return currentActive == 0 ? maxFrogs : -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minNumberOfFrogs(croakOfFrogs: String): Int {
        val cnt = IntArray(5)
        var ongoing = 0
        var answer = 0
        for (ch in croakOfFrogs) {
            val idx = when (ch) {
                'c' -> 0
                'r' -> 1
                'o' -> 2
                'a' -> 3
                'k' -> 4
                else -> -1
            }
            if (idx == -1) return -1
            if (idx == 0) {
                cnt[0]++
                ongoing++
                if (ongoing > answer) answer = ongoing
            } else {
                if (cnt[idx - 1] == 0) return -1
                cnt[idx - 1]--
                if (idx == 4) {
                    ongoing--
                } else {
                    cnt[idx]++
                }
            }
        }
        for (i in 0..3) {
            if (cnt[i] != 0) return -1
        }
        if (ongoing != 0) return -1
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minNumberOfFrogs(String croakOfFrogs) {
    List<int> cnt = List.filled(5, 0);
    int current = 0;
    int maxFrogs = 0;
    for (int i = 0; i < croakOfFrogs.length; ++i) {
      String ch = croakOfFrogs[i];
      switch (ch) {
        case 'c':
          cnt[0]++;
          current++;
          if (current > maxFrogs) maxFrogs = current;
          break;
        case 'r':
          cnt[1]++;
          if (cnt[1] > cnt[0]) return -1;
          break;
        case 'o':
          cnt[2]++;
          if (cnt[2] > cnt[1]) return -1;
          break;
        case 'a':
          cnt[3]++;
          if (cnt[3] > cnt[2]) return -1;
          break;
        case 'k':
          cnt[4]++;
          if (cnt[4] > cnt[3]) return -1;
          current--;
          break;
        default:
          return -1;
      }
    }
    if (current != 0) return -1;
    for (int j = 1; j < 5; ++j) {
      if (cnt[j] != cnt[0]) return -1;
    }
    return maxFrogs;
  }
}
```

## Golang

```go
func minNumberOfFrogs(croakOfFrogs string) int {
    // cnt[0]: waiting for 'r' after 'c'
    // cnt[1]: waiting for 'o' after 'r'
    // cnt[2]: waiting for 'a' after 'o'
    // cnt[3]: waiting for 'k' after 'a'
    cnt := make([]int, 4)
    cur, maxFrogs := 0, 0

    for _, ch := range croakOfFrogs {
        switch ch {
        case 'c':
            cnt[0]++
            cur++
            if cur > maxFrogs {
                maxFrogs = cur
            }
        case 'r':
            if cnt[0] == 0 {
                return -1
            }
            cnt[0]--
            cnt[1]++
        case 'o':
            if cnt[1] == 0 {
                return -1
            }
            cnt[1]--
            cnt[2]++
        case 'a':
            if cnt[2] == 0 {
                return -1
            }
            cnt[2]--
            cnt[3]++
        case 'k':
            if cnt[3] == 0 {
                return -1
            }
            cnt[3]--
            cur--
        default:
            return -1
        }
    }

    if cur != 0 {
        return -1
    }
    for _, v := range cnt {
        if v != 0 {
            return -1
        }
    }
    return maxFrogs
}
```

## Ruby

```ruby
def min_number_of_frogs(croak_of_frogs)
  order = {'c' => 0, 'r' => 1, 'o' => 2, 'a' => 3, 'k' => 4}
  cnt = Array.new(5, 0)
  max_frogs = 0

  croak_of_frogs.each_char do |ch|
    idx = order[ch]
    return -1 if idx.nil?

    if idx == 0
      cnt[0] += 1
      cur_active = cnt[0] - cnt[4]
      max_frogs = cur_active if cur_active > max_frogs
    else
      prev = idx - 1
      return -1 if cnt[prev] == 0
      cnt[prev] -= 1
      cnt[idx] += 1
    end
  end

  # All frogs must have finished their croak
  (0..3).each { |i| return -1 unless cnt[i].zero? }
  max_frogs
end
```

## Scala

```scala
object Solution {
    def minNumberOfFrogs(croakOfFrogs: String): Int = {
        val idxMap = Map('c' -> 0, 'r' -> 1, 'o' -> 2, 'a' -> 3, 'k' -> 4)
        val cnt = new Array[Int](5) // counts for stages c,r,o,a,k (k not really used)
        var active = 0
        var maxActive = 0

        for (ch <- croakOfFrogs) {
            idxMap.get(ch) match {
                case Some(0) => // 'c' starts a new croak
                    cnt(0) += 1
                    active += 1
                    if (active > maxActive) maxActive = active
                case Some(idx) =>
                    val prev = idx - 1
                    if (cnt(prev) == 0) return -1 // no frog to advance
                    cnt(prev) -= 1
                    if (idx < 4) {
                        cnt(idx) += 1 // move to next stage
                    } else { // 'k' finishes a croak
                        active -= 1
                    }
                case None => return -1 // invalid character, though per constraints shouldn't happen
            }
        }

        // any unfinished croaks?
        for (i <- 0 until 4) {
            if (cnt(i) != 0) return -1
        }

        maxActive
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_number_of_frogs(croak_of_frogs: String) -> i32 {
        let mut c = 0;
        let mut r = 0;
        let mut o = 0;
        let mut a = 0;
        let mut max_frogs = 0;

        for ch in croak_of_frogs.chars() {
            match ch {
                'c' => {
                    c += 1;
                }
                'r' => {
                    if c == 0 {
                        return -1;
                    }
                    c -= 1;
                    r += 1;
                }
                'o' => {
                    if r == 0 {
                        return -1;
                    }
                    r -= 1;
                    o += 1;
                }
                'a' => {
                    if o == 0 {
                        return -1;
                    }
                    o -= 1;
                    a += 1;
                }
                'k' => {
                    if a == 0 {
                        return -1;
                    }
                    a -= 1;
                }
                _ => return -1,
            }

            let active = c + r + o + a;
            if active > max_frogs {
                max_frogs = active;
            }
        }

        if c == 0 && r == 0 && o == 0 && a == 0 {
            max_frogs as i32
        } else {
            -1
        }
    }
}
```

## Racket

```racket
(define/contract (min-number-of-frogs croakOfFrogs)
  (-> string? exact-integer?)
  (let* ([cnt (make-vector 4 0)]) ; indices: 0=c,1=r,2=o,3=a
    (let loop ((i 0) (active 0) (max-active 0))
      (if (= i (string-length croakOfFrogs))
          (if (and (= active 0)
                   (= (vector-ref cnt 0) 0)
                   (= (vector-ref cnt 1) 0)
                   (= (vector-ref cnt 2) 0)
                   (= (vector-ref cnt 3) 0))
              max-active
              -1)
          (let ((ch (string-ref croakOfFrogs i)))
            (cond
              [(char=? ch #\c)
               (vector-set! cnt 0 (+ (vector-ref cnt 0) 1))
               (loop (+ i 1) (+ active 1) (max max-active (+ active 1)))]
              
              [(char=? ch #\r)
               (if (= (vector-ref cnt 0) 0)
                   -1
                   (begin
                     (vector-set! cnt 0 (- (vector-ref cnt 0) 1))
                     (vector-set! cnt 1 (+ (vector-ref cnt 1) 1))
                     (loop (+ i 1) active max-active))))]
              
              [(char=? ch #\o)
               (if (= (vector-ref cnt 1) 0)
                   -1
                   (begin
                     (vector-set! cnt 1 (- (vector-ref cnt 1) 1))
                     (vector-set! cnt 2 (+ (vector-ref cnt 2) 1))
                     (loop (+ i 1) active max-active))))]
              
              [(char=? ch #\a)
               (if (= (vector-ref cnt 2) 0)
                   -1
                   (begin
                     (vector-set! cnt 2 (- (vector-ref cnt 2) 1))
                     (vector-set! cnt 3 (+ (vector-ref cnt 3) 1))
                     (loop (+ i 1) active max-active))))]
              
              [(char=? ch #\k)
               (if (= (vector-ref cnt 3) 0)
                   -1
                   (begin
                     (vector-set! cnt 3 (- (vector-ref cnt 3) 1))
                     (loop (+ i 1) (- active 1) max-active))))]
              
              [else -1])))))
```

## Erlang

```erlang
-spec min_number_of_frogs(CroakOfFrogs :: unicode:unicode_binary()) -> integer().
min_number_of_frogs(CroakOfFrogs) ->
    case process(CroakOfFrogs, 0, 0, 0, 0, 0) of
        {ok, Max} -> Max;
        error -> -1
    end.

process(<<>>, C, R, O, A, Max) ->
    if C =:= 0, R =:= 0, O =:= 0, A =:= 0 ->
            {ok, Max};
       true ->
            error
    end;
process(<<Char, Rest/binary>>, C, R, O, A, Max) ->
    case Char of
        $c ->
            NewC = C + 1,
            Active = NewC + R + O + A,
            NewMax = erlang:max(Active, Max),
            process(Rest, NewC, R, O, A, NewMax);
        $r ->
            if C > 0 ->
                    NewC = C - 1,
                    NewR = R + 1,
                    Active = NewC + NewR + O + A,
                    NewMax = erlang:max(Active, Max),
                    process(Rest, NewC, NewR, O, A, NewMax);
               true -> error
            end;
        $o ->
            if R > 0 ->
                    NewR = R - 1,
                    NewO = O + 1,
                    Active = C + NewR + NewO + A,
                    NewMax = erlang:max(Active, Max),
                    process(Rest, C, NewR, NewO, A, NewMax);
               true -> error
            end;
        $a ->
            if O > 0 ->
                    NewO = O - 1,
                    NewA = A + 1,
                    Active = C + R + NewO + NewA,
                    NewMax = erlang:max(Active, Max),
                    process(Rest, C, R, NewO, NewA, NewMax);
               true -> error
            end;
        $k ->
            if A > 0 ->
                    NewA = A - 1,
                    Active = C + R + O + NewA,
                    NewMax = erlang:max(Active, Max),
                    process(Rest, C, R, O, NewA, NewMax);
               true -> error
            end;
        _ -> error
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_number_of_frogs(croak_of_frogs :: String.t) :: integer
  def min_number_of_frogs(croak_of_frogs) do
    result =
      croak_of_frogs
      |> String.graphemes()
      |> Enum.reduce_while({0, %{c: 0, r: 0, o: 0, a: 0, k: 0}}, fn ch, {max_frogs, cnts} ->
        case ch do
          "c" ->
            new_cnts = Map.update!(cnts, :c, &(&1 + 1))
            active = new_cnts.c + new_cnts.r + new_cnts.o + new_cnts.a
            {:cont, {max(max_frogs, active), new_cnts}}

          "r" ->
            if cnts.c == 0 do
              {:halt, -1}
            else
              new_cnts =
                cnts
                |> Map.update!(:c, &(&1 - 1))
                |> Map.update!(:r, &(&1 + 1))

              active = new_cnts.c + new_cnts.r + new_cnts.o + new_cnts.a
              {:cont, {max(max_frogs, active), new_cnts}}
            end

          "o" ->
            if cnts.r == 0 do
              {:halt, -1}
            else
              new_cnts =
                cnts
                |> Map.update!(:r, &(&1 - 1))
                |> Map.update!(:o, &(&1 + 1))

              active = new_cnts.c + new_cnts.r + new_cnts.o + new_cnts.a
              {:cont, {max(max_frogs, active), new_cnts}}
            end

          "a" ->
            if cnts.o == 0 do
              {:halt, -1}
            else
              new_cnts =
                cnts
                |> Map.update!(:o, &(&1 - 1))
                |> Map.update!(:a, &(&1 + 1))

              active = new_cnts.c + new_cnts.r + new_cnts.o + new_cnts.a
              {:cont, {max(max_frogs, active), new_cnts}}
            end

          "k" ->
            if cnts.a == 0 do
              {:halt, -1}
            else
              new_cnts =
                cnts
                |> Map.update!(:a, &(&1 - 1))
                |> Map.update!(:k, &(&1 + 1))

              active = new_cnts.c + new_cnts.r + new_cnts.o + new_cnts.a
              {:cont, {max(max_frogs, active), new_cnts}}
            end

          _ ->
            {:halt, -1}
        end
      end)

    case result do
      -1 ->
        -1

      {max_frogs, final_counts} ->
        if final_counts.c == 0 and final_counts.r == 0 and final_counts.o == 0 and final_counts.a == 0 do
          max_frogs
        else
          -1
        end
    end
  end
end
```
