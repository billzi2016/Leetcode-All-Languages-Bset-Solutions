# 2844. Minimum Operations to Make a Special Number

## Cpp

```cpp
class Solution {
public:
    int minimumOperations(string num) {
        int n = num.size();
        int ans = n; // worst case delete all digits
        vector<string> targets = {"00","25","50","75"};
        for (const string& t : targets) {
            char first = t[0], second = t[1];
            // find position of second digit from right
            for (int j = n - 1; j >= 0; --j) {
                if (num[j] != second) continue;
                // find first digit to the left of j
                for (int i = j - 1; i >= 0; --i) {
                    if (num[i] == first) {
                        ans = min(ans, n - i - 2);
                        break; // earliest i gives minimal deletions for this j
                    }
                }
            }
        }
        // keep a single zero if exists
        for (char c : num) {
            if (c == '0') {
                ans = min(ans, n - 1);
                break;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumOperations(String num) {
        int n = num.length();
        int ans = n; // maximum possible deletions
        String[] targets = {"00", "25", "50", "75"};
        for (String t : targets) {
            char first = t.charAt(0);
            char second = t.charAt(1);
            for (int j = n - 1; j >= 0; --j) {
                if (num.charAt(j) == second) {
                    for (int i = j - 1; i >= 0; --i) {
                        if (num.charAt(i) == first) {
                            ans = Math.min(ans, n - i - 2);
                            break; // closest i gives minimal deletions for this j
                        }
                    }
                }
            }
        }
        // Single zero case: keep one '0' and delete the rest
        if (num.indexOf('0') != -1) {
            ans = Math.min(ans, n - 1);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minimumOperations(self, num):
        """
        :type num: str
        :rtype: int
        """
        n = len(num)
        ans = n  # worst case: delete all digits to get 0
        # If there is any zero, we can keep one zero and delete the rest
        if '0' in num:
            ans = min(ans, n - 1)
        targets = ["00", "25", "50", "75"]
        for t in targets:
            last_digit = t[1]
            second_last = t[0]
            # find position of last digit (rightmost possible)
            j = n - 1
            while j >= 0:
                if num[j] == last_digit:
                    # look for second_last to the left of j
                    i = j - 1
                    while i >= 0:
                        if num[i] == second_last:
                            deletions = n - i - 2
                            ans = min(ans, deletions)
                            break
                        i -= 1
                j -= 1
        return ans
```

## Python3

```python
class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        ans = n  # worst case: delete all digits to get 0
        targets = ["00", "25", "50", "75"]
        for t in targets:
            a, b = t[0], t[1]
            # find rightmost occurrence of b
            j = -1
            for idx in range(n - 1, -1, -1):
                if num[idx] == b:
                    j = idx
                    break
            if j == -1:
                continue
            # find a to the left of j
            i = -1
            for idx in range(j - 1, -1, -1):
                if num[idx] == a:
                    i = idx
                    break
            if i == -1:
                continue
            deletions = n - i - 2
            ans = min(ans, deletions)
        # case of keeping a single zero
        if '0' in num:
            ans = min(ans, n - 1)
        return ans
```

## C

```c
#include <string.h>

int minimumOperations(char* num) {
    int n = strlen(num);
    int ans = n;  // worst case: delete all digits

    const char *targets[4] = {"00", "25", "50", "75"};
    for (int t = 0; t < 4; ++t) {
        char a = targets[t][0];
        char b = targets[t][1];

        int pos2 = -1;
        for (int i = n - 1; i >= 0; --i) {
            if (num[i] == b) {
                pos2 = i;
                break;
            }
        }
        if (pos2 == -1) continue;

        int pos1 = -1;
        for (int i = pos2 - 1; i >= 0; --i) {
            if (num[i] == a) {
                pos1 = i;
                break;
            }
        }
        if (pos1 == -1) continue;

        int deletions = n - pos1 - 2;
        if (deletions < ans) ans = deletions;
    }

    // Keep a single '0' to make the number zero
    for (int i = 0; i < n; ++i) {
        if (num[i] == '0') {
            if (n - 1 < ans) ans = n - 1;
            break;
        }
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumOperations(string num) {
        int n = num.Length;
        int ans = n; // worst case: delete all digits
        
        string[] targets = new string[] { "00", "25", "50", "75" };
        foreach (var t in targets) {
            char first = t[0];
            char second = t[1];
            for (int j = n - 1; j >= 0; --j) {
                if (num[j] != second) continue;
                for (int i = j - 1; i >= 0; --i) {
                    if (num[i] == first) {
                        int deletions = n - i - 2; // delete after j and between i and j
                        ans = Math.Min(ans, deletions);
                        break; // nearest i gives minimal deletions for this j
                    }
                }
            }
        }
        
        // Keep a single zero if it exists
        if (num.IndexOf('0') != -1) {
            ans = Math.Min(ans, n - 1);
        }
        
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @return {number}
 */
var minimumOperations = function(num) {
    const n = num.length;
    let ans = n; // worst case: delete all digits
    
    const targets = ["00", "25", "50", "75"];
    
    for (const t of targets) {
        const a = t[0], b = t[1];
        for (let i = 0; i < n; ++i) {
            if (num[i] !== a) continue;
            for (let j = i + 1; j < n; ++j) {
                if (num[j] === b) {
                    ans = Math.min(ans, n - i - 2);
                    break; // further j won't improve deletions for this i
                }
            }
        }
    }
    
    // Single zero case: keep one '0' and delete everything else
    if (num.includes('0')) {
        ans = Math.min(ans, n - 1);
    }
    
    return ans;
};
```

## Typescript

```typescript
function minimumOperations(num: string): number {
    const n = num.length;
    let ans = n; // worst case: delete all digits
    const targets = ["00", "25", "50", "75"];
    for (const t of targets) {
        const first = t[0];
        const second = t[1];
        for (let j = n - 1; j >= 0; --j) {
            if (num[j] !== second) continue;
            for (let i = j - 1; i >= 0; --i) {
                if (num[i] === first) {
                    const deletions = n - i - 2;
                    ans = Math.min(ans, deletions);
                    break; // larger i gives fewer deletions
                }
            }
        }
    }
    if (num.includes('0')) {
        ans = Math.min(ans, n - 1); // keep a single zero
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $num
     * @return Integer
     */
    function minimumOperations($num) {
        $n = strlen($num);
        $targets = ["00","25","50","75"];
        $ans = $n; // worst case: delete all digits
        
        // If there is at least one zero, we can keep a single zero
        if (strpos($num, '0') !== false) {
            $ans = min($ans, $n - 1);
        }
        
        for ($i = 0; $i < $n; ++$i) {
            for ($j = $i + 1; $j < $n; ++$j) {
                $pair = $num[$i] . $num[$j];
                if (in_array($pair, $targets, true)) {
                    // deletions needed to make these two the last digits
                    $ops = $n - $i - 2;
                    if ($ops < $ans) {
                        $ans = $ops;
                    }
                }
            }
        }
        
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumOperations(_ num: String) -> Int {
        let chars = Array(num)
        let n = chars.count
        var answer = n  // delete all digits
        
        // If there is at least one '0', we can keep that single zero.
        if chars.contains("0") {
            answer = min(answer, n - 1)
        }
        
        let targets: [(Character, Character)] = [("0","0"), ("2","5"), ("5","0"), ("7","5")]
        
        for (first, second) in targets {
            var j = n - 1
            while j >= 0 && chars[j] != second {
                j -= 1
            }
            if j < 0 { continue }   // second digit not found
            
            var i = j - 1
            while i >= 0 && chars[i] != first {
                i -= 1
            }
            if i < 0 { continue }   // first digit not found before second
            
            let deletions = n - i - 2
            answer = min(answer, deletions)
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumOperations(num: String): Int {
        val n = num.length
        var ans = n // worst case: delete all digits
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                when ("${num[i]}${num[j]}") {
                    "00", "25", "50", "75" -> {
                        ans = minOf(ans, n - i - 2)
                    }
                }
            }
        }
        if ('0' in num) {
            ans = minOf(ans, n - 1) // keep a single zero
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minimumOperations(String num) {
    int n = num.length;
    int ans = n; // worst case: delete all digits
    List<String> targets = ['00', '25', '50', '75'];
    for (String t in targets) {
      String a = t[0];
      String b = t[1];
      int posB = -1;
      for (int i = n - 1; i >= 0; --i) {
        if (num[i] == b) {
          posB = i;
          break;
        }
      }
      if (posB == -1) continue;
      int posA = -1;
      for (int i = posB - 1; i >= 0; --i) {
        if (num[i] == a) {
          posA = i;
          break;
        }
      }
      if (posA == -1) continue;
      int deletions = n - posA - 2;
      if (deletions < ans) ans = deletions;
    }
    // If no valid suffix found, try to keep a single zero
    if (ans == n) {
      for (int i = 0; i < n; ++i) {
        if (num[i] == '0') {
          ans = n - 1;
          break;
        }
      }
    }
    return ans;
  }
}
```

## Golang

```go
func minimumOperations(num string) int {
	n := len(num)
	ans := n // worst case: delete all digits
	targets := []string{"00", "25", "50", "75"}

	for _, t := range targets {
		found := false
		for j := n - 1; j >= 0 && !found; j-- {
			if num[j] != t[1] {
				continue
			}
			for i := j - 1; i >= 0; i-- {
				if num[i] == t[0] {
					deletions := n - i - 2
					if deletions < ans {
						ans = deletions
					}
					found = true
					break
				}
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def minimum_operations(num)
  n = num.length
  ans = n
  targets = ["00", "25", "50", "75"]
  targets.each do |t|
    a, b = t[0], t[1]
    j = nil
    (n - 1).downto(0) do |idx|
      if num[idx] == b
        j = idx
        break
      end
    end
    next unless j
    i = nil
    (j - 1).downto(0) do |idx|
      if num[idx] == a
        i = idx
        break
      end
    end
    next unless i
    deletions = n - i - 2
    ans = [ans, deletions].min
  end
  if num.include?('0')
    ans = [ans, n - 1].min
  end
  ans
end
```

## Scala

```scala
object Solution {
  def minimumOperations(num: String): Int = {
    val n = num.length
    var ans = n // delete all digits to get 0
    val targets = List(("0", "0"), ("2", "5"), ("5", "0"), ("7", "5"))
    for ((a, b) <- targets) {
      var j = -1
      var idx = n - 1
      while (idx >= 0 && j == -1) {
        if (num.charAt(idx) == b.charAt(0)) j = idx
        idx -= 1
      }
      if (j != -1) {
        var i = -1
        idx = j - 1
        while (idx >= 0 && i == -1) {
          if (num.charAt(idx) == a.charAt(0)) i = idx
          idx -= 1
        }
        if (i != -1) {
          ans = math.min(ans, n - i - 2)
        }
      }
    }
    // Keep a single zero if it exists
    if (num.contains('0')) {
      ans = math.min(ans, n - 1)
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_operations(num: String) -> i32 {
        let bytes = num.as_bytes();
        let n = bytes.len();
        let mut ans = n as i32; // worst case: delete all digits

        // possible endings for divisibility by 25
        let targets = [(b'0', b'0'), (b'2', b'5'), (b'5', b'0'), (b'7', b'5')];

        for i in 0..n {
            for j in i + 1..n {
                let a = bytes[i];
                let b = bytes[j];
                if targets.iter().any(|&(x, y)| x == a && y == b) {
                    let deletions = n - i - 2;
                    ans = ans.min(deletions as i32);
                }
            }
        }

        // If there is at least one '0', we can keep that single zero
        if bytes.iter().any(|&c| c == b'0') {
            ans = ans.min((n - 1) as i32);
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (minimum-operations num)
  (-> string? exact-integer?)
  (let* ((n (string-length num))
         (ans n)) ; worst case: delete all digits
    ;; check each valid suffix
    (for ([suffix (list "00" "25" "50" "75")])
      (let* ((c2 (string-ref suffix 1))
             (c1 (string-ref suffix 0))
             (j (let loop ((idx (- n 1)))
                  (cond [(< idx 0) #f]
                        [(char=? (string-ref num idx) c2) idx]
                        [else (loop (- idx 1))])))
             )
        (when j
          (let ((i (let loop ((idx (- j 1)))
                     (cond [(< idx 0) #f]
                           [(char=? (string-ref num idx) c1) idx]
                           [else (loop (- idx 1))]))))
            (when i
              (set! ans (min ans (- n i 2))))))))
    ;; consider keeping a single '0' (or deleting all to get 0)
    (let loop ((idx 0) (found #f))
      (cond [(>= idx n)
             (when found (set! ans (min ans (- n 1))))]
            [(char=? (string-ref num idx) #\0)
             (loop (+ idx 1) #t)]
            [else (loop (+ idx 1) found)]))
    ans)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_operations/1]).

-spec minimum_operations(Num :: unicode:unicode_binary()) -> integer().
minimum_operations(Num) ->
    Chars = binary_to_list(Num),
    N = length(Chars),
    Pairs = [{$0,$0}, {$2,$5}, {$5,$0}, {$7,$5}],
    Answer0 = N,
    Answer1 = lists:foldl(fun({F,S}, Acc) ->
        case find_last_index(Chars, S) of
            undefined -> Acc;
            J ->
                case find_last_before_index(Chars, F, J) of
                    undefined -> Acc;
                    I ->
                        Deletions = N - I - 2,
                        erlang:min(Acc, Deletions)
                end
        end
    end, Answer0, Pairs),
    Answer2 = if lists:member($0, Chars) -> erlang:min(Answer1, N-1); true -> Answer1 end,
    Answer2.

find_last_index(List, Target) ->
    find_last_index(List, Target, 0, undefined).

find_last_index([], _Target, _Idx, Result) -> Result;
find_last_index([H|T], Target, Idx, Result) ->
    NewResult = if H =:= Target -> Idx; true -> Result end,
    find_last_index(T, Target, Idx + 1, NewResult).

find_last_before_index(List, Target, Limit) ->
    find_last_before_index(List, Target, 0, Limit, undefined).

find_last_before_index([], _Target, _Idx, _Limit, Result) -> Result;
find_last_before_index([H|T], Target, Idx, Limit, Result) when Idx < Limit ->
    NewResult = if H =:= Target -> Idx; true -> Result end,
    find_last_before_index(T, Target, Idx + 1, Limit, NewResult);
find_last_before_index(_, _Target, _Idx, _Limit, Result) ->
    Result.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(num :: String.t) :: integer
  def minimum_operations(num) do
    chars = String.graphemes(num)
    n = length(chars)

    patterns = [{"0", "0"}, {"2", "5"}, {"5", "0"}, {"7", "5"}]
    max_ops = n + 1

    ans =
      Enum.reduce(patterns, max_ops, fn {x, y}, best ->
        Enum.reduce(0..(n - 2), best, fn i, acc_i ->
          Enum.reduce((i + 1)..(n - 1), acc_i, fn j, acc_j ->
            if Enum.at(chars, i) == x and Enum.at(chars, j) == y do
              deletions = n - i - 2
              min(acc_j, deletions)
            else
              acc_j
            end
          end)
        end)
      end)

    ans =
      if String.contains?(num, "0") do
        min(ans, n - 1)
      else
        ans
      end

    if ans == max_ops do
      n
    else
      ans
    end
  end
end
```
