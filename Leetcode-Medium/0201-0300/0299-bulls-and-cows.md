# 0299. Bulls and Cows

## Cpp

```cpp
class Solution {
public:
    string getHint(string secret, string guess) {
        int bulls = 0, cows = 0;
        int cnt[10] = {0};
        for (int i = 0; i < (int)secret.size(); ++i) {
            if (secret[i] == guess[i]) {
                ++bulls;
            } else {
                int s = secret[i] - '0';
                int g = guess[i] - '0';
                if (cnt[s] < 0) ++cows;   // a previous guess digit waiting for this secret digit
                if (cnt[g] > 0) ++cows;   // a previous secret digit waiting for this guess digit
                ++cnt[s];
                --cnt[g];
            }
        }
        return to_string(bulls) + "A" + to_string(cows) + "B";
    }
};
```

## Java

```java
class Solution {
    public String getHint(String secret, String guess) {
        int bulls = 0;
        int[] cntSecret = new int[10];
        int[] cntGuess = new int[10];
        int n = secret.length();
        for (int i = 0; i < n; i++) {
            char s = secret.charAt(i);
            char g = guess.charAt(i);
            if (s == g) {
                bulls++;
            } else {
                cntSecret[s - '0']++;
                cntGuess[g - '0']++;
            }
        }
        int cows = 0;
        for (int d = 0; d < 10; d++) {
            cows += Math.min(cntSecret[d], cntGuess[d]);
        }
        return bulls + "A" + cows + "B";
    }
}
```

## Python

```python
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cnt_secret = [0] * 10
        cnt_guess = [0] * 10

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                cnt_secret[ord(s) - ord('0')] += 1
                cnt_guess[ord(g) - ord('0')] += 1

        cows = sum(min(cs, cg) for cs, cg in zip(cnt_secret, cnt_guess))
        return f"{bulls}A{cows}B"
```

## Python3

```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        # counts for digits 0-9
        s_counts = [0] * 10
        g_counts = [0] * 10

        for sc, gc in zip(secret, guess):
            if sc == gc:
                bulls += 1
            else:
                s_counts[ord(sc) - ord('0')] += 1
                g_counts[ord(gc) - ord('0')] += 1

        cows = sum(min(s_counts[i], g_counts[i]) for i in range(10))
        return f"{bulls}A{cows}B"
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char* getHint(char* secret, char* guess) {
    int len = strlen(secret);
    int bulls = 0;
    int cntS[10] = {0}, cntG[10] = {0};

    for (int i = 0; i < len; ++i) {
        if (secret[i] == guess[i]) {
            ++bulls;
        } else {
            ++cntS[secret[i] - '0'];
            ++cntG[guess[i] - '0'];
        }
    }

    int cows = 0;
    for (int d = 0; d < 10; ++d) {
        if (cntS[d] && cntG[d]) {
            cows += cntS[d] < cntG[d] ? cntS[d] : cntG[d];
        }
    }

    char* result = (char*)malloc(20);
    sprintf(result, "%dA%dB", bulls, cows);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string GetHint(string secret, string guess)
    {
        int bulls = 0;
        int[] countSecret = new int[10];
        int[] countGuess = new int[10];

        for (int i = 0; i < secret.Length; i++)
        {
            if (secret[i] == guess[i])
            {
                bulls++;
            }
            else
            {
                countSecret[secret[i] - '0']++;
                countGuess[guess[i] - '0']++;
            }
        }

        int cows = 0;
        for (int d = 0; d < 10; d++)
        {
            cows += Math.Min(countSecret[d], countGuess[d]);
        }

        return $"{bulls}A{cows}B";
    }
}
```

## Javascript

```javascript
/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    let bulls = 0;
    const cntSecret = new Array(10).fill(0);
    const cntGuess = new Array(10).fill(0);
    
    for (let i = 0; i < secret.length; i++) {
        if (secret[i] === guess[i]) {
            bulls++;
        } else {
            cntSecret[secret.charCodeAt(i) - 48]++;
            cntGuess[guess.charCodeAt(i) - 48]++;
        }
    }
    
    let cows = 0;
    for (let d = 0; d < 10; d++) {
        cows += Math.min(cntSecret[d], cntGuess[d]);
    }
    
    return `${bulls}A${cows}B`;
};
```

## Typescript

```typescript
function getHint(secret: string, guess: string): string {
    let bulls = 0;
    const secretCnt = new Array(10).fill(0);
    const guessCnt = new Array(10).fill(0);
    for (let i = 0; i < secret.length; i++) {
        if (secret[i] === guess[i]) {
            bulls++;
        } else {
            secretCnt[secret.charCodeAt(i) - 48]++;
            guessCnt[guess.charCodeAt(i) - 48]++;
        }
    }
    let cows = 0;
    for (let d = 0; d < 10; d++) {
        cows += Math.min(secretCnt[d], guessCnt[d]);
    }
    return `${bulls}A${cows}B`;
}
```

## Php

```php
class Solution {

    /**
     * @param String $secret
     * @param String $guess
     * @return String
     */
    function getHint($secret, $guess) {
        $bulls = 0;
        $len = strlen($secret);
        $secretCount = array_fill(0, 10, 0);
        $guessCount = array_fill(0, 10, 0);

        for ($i = 0; $i < $len; $i++) {
            if ($secret[$i] === $guess[$i]) {
                $bulls++;
            } else {
                $sIdx = intval($secret[$i]);
                $gIdx = intval($guess[$i]);
                $secretCount[$sIdx]++;
                $guessCount[$gIdx]++;
            }
        }

        $cows = 0;
        for ($d = 0; $d < 10; $d++) {
            $cows += min($secretCount[$d], $guessCount[$d]);
        }

        return $bulls . 'A' . $cows . 'B';
    }
}
```

## Swift

```swift
class Solution {
    func getHint(_ secret: String, _ guess: String) -> String {
        let s = Array(secret)
        let g = Array(guess)
        var bulls = 0
        var secretCount = [Int](repeating: 0, count: 10)
        var guessCount = [Int](repeating: 0, count: 10)

        for i in 0..<s.count {
            if s[i] == g[i] {
                bulls += 1
            } else {
                if let sv = s[i].wholeNumberValue {
                    secretCount[sv] += 1
                }
                if let gv = g[i].wholeNumberValue {
                    guessCount[gv] += 1
                }
            }
        }

        var cows = 0
        for d in 0..<10 {
            cows += min(secretCount[d], guessCount[d])
        }

        return "\(bulls)A\(cows)B"
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getHint(secret: String, guess: String): String {
        var bulls = 0
        val secretCount = IntArray(10)
        val guessCount = IntArray(10)

        for (i in secret.indices) {
            if (secret[i] == guess[i]) {
                bulls++
            } else {
                secretCount[secret[i] - '0']++
                guessCount[guess[i] - '0']++
            }
        }

        var cows = 0
        for (d in 0..9) {
            cows += kotlin.math.min(secretCount[d], guessCount[d])
        }

        return "${bulls}A${cows}B"
    }
}
```

## Dart

```dart
class Solution {
  String getHint(String secret, String guess) {
    int bulls = 0;
    List<int> sCount = List.filled(10, 0);
    List<int> gCount = List.filled(10, 0);
    for (int i = 0; i < secret.length; i++) {
      if (secret[i] == guess[i]) {
        bulls++;
      } else {
        sCount[secret.codeUnitAt(i) - 48]++;
        gCount[guess.codeUnitAt(i) - 48]++;
      }
    }
    int cows = 0;
    for (int d = 0; d < 10; d++) {
      cows += sCount[d] < gCount[d] ? sCount[d] : gCount[d];
    }
    return '${bulls}A${cows}B';
  }
}
```

## Golang

```go
import "fmt"

func getHint(secret string, guess string) string {
	bulls := 0
	var cntSecret [10]int
	var cntGuess [10]int

	for i := 0; i < len(secret); i++ {
		if secret[i] == guess[i] {
			bulls++
		} else {
			cntSecret[secret[i]-'0']++
			cntGuess[guess[i]-'0']++
		}
	}

	cows := 0
	for d := 0; d < 10; d++ {
		if cntSecret[d] < cntGuess[d] {
			cows += cntSecret[d]
		} else {
			cows += cntGuess[d]
		}
	}

	return fmt.Sprintf("%dA%dB", bulls, cows)
}
```

## Ruby

```ruby
def get_hint(secret, guess)
  bulls = 0
  secret_counts = Array.new(10, 0)
  guess_counts = Array.new(10, 0)

  secret.each_char.with_index do |ch, i|
    if ch == guess[i]
      bulls += 1
    else
      secret_counts[ch.to_i] += 1
      guess_counts[guess[i].to_i] += 1
    end
  end

  cows = 0
  10.times { |d| cows += [secret_counts[d], guess_counts[d]].min }

  "#{bulls}A#{cows}B"
end
```

## Scala

```scala
object Solution {
    def getHint(secret: String, guess: String): String = {
        var bulls = 0
        val cntSecret = new Array[Int](10)
        val cntGuess = new Array[Int](10)

        for (i <- secret.indices) {
            if (secret(i) == guess(i)) {
                bulls += 1
            } else {
                cntSecret(secret(i) - '0') += 1
                cntGuess(guess(i) - '0') += 1
            }
        }

        var cows = 0
        for (d <- 0 until 10) {
            cows += math.min(cntSecret(d), cntGuess(d))
        }

        s"${bulls}A${cows}B"
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_hint(secret: String, guess: String) -> String {
        let s = secret.as_bytes();
        let g = guess.as_bytes();
        let mut bulls = 0;
        let mut cnt_s = [0i32; 10];
        let mut cnt_g = [0i32; 10];

        for i in 0..s.len() {
            if s[i] == g[i] {
                bulls += 1;
            } else {
                cnt_s[(s[i] - b'0') as usize] += 1;
                cnt_g[(g[i] - b'0') as usize] += 1;
            }
        }

        let mut cows = 0;
        for d in 0..10 {
            cows += std::cmp::min(cnt_s[d], cnt_g[d]);
        }

        format!("{}A{}B", bulls, cows)
    }
}
```

## Racket

```racket
(define/contract (get-hint secret guess)
  (-> string? string? string?)
  (let* ((n (string-length secret))
         (secret-count (make-vector 10 0))
         (guess-count (make-vector 10 0)))
    (let loop ((i 0) (bulls 0))
      (if (= i n)
          (let ((cows
                 (let sum ((d 0) (acc 0))
                   (if (= d 10)
                       acc
                       (sum (+ d 1) (+ acc (min (vector-ref secret-count d)
                                                (vector-ref guess-count d))))))))
            (string-append (number->string bulls) "A"
                           (number->string cows) "B"))
          (let ((s-ch (string-ref secret i))
                (g-ch (string-ref guess i)))
            (if (char=? s-ch g-ch)
                (loop (+ i 1) (+ bulls 1))
                (begin
                  (let* ((s-d (- (char->integer s-ch) (char->integer #\0)))
                         (g-d (- (char->integer g-ch) (char->integer #\0))))
                    (vector-set! secret-count s-d (+ 1 (vector-ref secret-count s-d)))
                    (vector-set! guess-count g-d (+ 1 (vector-ref guess-count g-d))))
                  (loop (+ i 1) bulls))))))))
```

## Erlang

```erlang
-module(solution).
-export([get_hint/2]).

-spec get_hint(Secret :: unicode:unicode_binary(), Guess :: unicode:unicode_binary()) -> unicode:unicode_binary().
get_hint(Secret, Guess) ->
    S = binary_to_list(Secret),
    G = binary_to_list(Guess),
    {Bull, MapS, MapG} = count(S, G, 0, #{}, #{}),
    Cow = cows(MapS, MapG),
    list_to_binary(integer_to_list(Bull) ++ "A" ++ integer_to_list(Cow) ++ "B").

count([], [], Bull, M1, M2) ->
    {Bull, M1, M2};
count([Sh|St], [Gh|Gt], BullAcc, M1, M2) ->
    if
        Sh =:= Gh ->
            count(St, Gt, BullAcc + 1, M1, M2);
        true ->
            NewM1 = maps:update_with(Sh, fun(V) -> V + 1 end, 1, M1),
            NewM2 = maps:update_with(Gh, fun(V) -> V + 1 end, 1, M2),
            count(St, Gt, BullAcc, NewM1, NewM2)
    end.

cows(MapS, MapG) ->
    lists:foldl(fun(Digit, Acc) ->
        CountS = maps:get(Digit, MapS, 0),
        CountG = maps:get(Digit, MapG, 0),
        Acc + min(CountS, CountG)
    end, 0, lists:seq($0, $9)).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_hint(secret :: String.t, guess :: String.t) :: String.t
  def get_hint(secret, guess) do
    {bulls, s_map, g_map} =
      secret
      |> String.graphemes()
      |> Enum.zip(String.graphemes(guess))
      |> Enum.reduce({0, %{}, %{}}, fn {s_char, g_char}, {b, sm, gm} ->
        if s_char == g_char do
          {b + 1, sm, gm}
        else
          {
            b,
            Map.update(sm, s_char, 1, &(&1 + 1)),
            Map.update(gm, g_char, 1, &(&1 + 1))
          }
        end
      end)

    cows =
      Enum.reduce(s_map, 0, fn {digit, cnt_s}, acc ->
        cnt_g = Map.get(g_map, digit, 0)
        acc + min(cnt_s, cnt_g)
      end)

    "#{bulls}A#{cows}B"
  end
end
```
