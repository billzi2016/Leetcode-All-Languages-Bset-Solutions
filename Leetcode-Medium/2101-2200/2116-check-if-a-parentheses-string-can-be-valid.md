# 2116. Check if a Parentheses String Can Be Valid

## Cpp

```cpp
class Solution {
public:
    bool canBeValid(string s, string locked) {
        int n = s.size();
        if (n % 2) return false;
        int low = 0, high = 0;
        for (int i = 0; i < n; ++i) {
            if (locked[i] == '1') {
                if (s[i] == '(') {
                    ++low;
                    ++high;
                } else {
                    --low;
                    --high;
                }
            } else { // unlocked, can be either '(' or ')'
                --low;   // treat as ')'
                ++high;  // treat as '('
            }
            if (high < 0) return false;
            low = max(low, 0);
        }
        return low == 0;
    }
};
```

## Java

```java
class Solution {
    public boolean canBeValid(String s, String locked) {
        int n = s.length();
        if ((n & 1) == 1) return false; // odd length cannot be balanced
        
        // Left to right: treat unlocked as '(' to maximize opens
        int balance = 0;
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            if (locked.charAt(i) == '1') {
                if (ch == '(') balance++;
                else balance--;
            } else {
                // unlocked, assume it can be '('
                balance++;
            }
            if (balance < 0) return false; // too many ')'
        }
        
        // Right to left: treat unlocked as ')' to maximize closes
        balance = 0;
        for (int i = n - 1; i >= 0; i--) {
            char ch = s.charAt(i);
            if (locked.charAt(i) == '1') {
                if (ch == ')') balance++;
                else balance--;
            } else {
                // unlocked, assume it can be ')'
                balance++;
            }
            if (balance < 0) return false; // too many '('
        }
        
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        n = len(s)
        if n % 2 == 1:
            return False

        # forward pass: treat unlocked as '('
        balance = 0
        for i in range(n):
            if locked[i] == '1':
                if s[i] == '(':
                    balance += 1
                else:
                    balance -= 1
            else:
                # can be '(' to help prefix balance
                balance += 1
            if balance < 0:
                return False

        # backward pass: treat unlocked as ')'
        balance = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    balance += 1
                else:
                    balance -= 1
            else:
                # can be ')' to help suffix balance
                balance += 1
            if balance < 0:
                return False

        return True
```

## Python3

```python
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        # Left to right pass: treat unlocked as '(' when needed
        balance = 0   # net '(' minus ')'
        free = 0      # count of unlocked positions available as '('
        for i in range(n):
            if locked[i] == '0':
                free += 1
            else:
                if s[i] == '(':
                    balance += 1
                else:  # ')'
                    balance -= 1

            if balance < 0:
                need = -balance
                if free >= need:
                    free -= need
                    balance = 0
                else:
                    return False

        # Right to left pass: treat unlocked as ')' when needed
        balance = 0   # net ')' minus '('
        free = 0      # count of unlocked positions available as ')'
        for i in range(n - 1, -1, -1):
            if locked[i] == '0':
                free += 1
            else:
                if s[i] == ')':
                    balance += 1
                else:  # '('
                    balance -= 1

            if balance < 0:
                need = -balance
                if free >= need:
                    free -= need
                    balance = 0
                else:
                    return False

        return True
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool canBeValid(char* s, char* locked) {
    int n = strlen(s);
    if (n % 2 == 1) return false;

    int balance = 0;
    for (int i = 0; i < n; ++i) {
        if (locked[i] == '1') {
            if (s[i] == '(') ++balance;
            else --balance;
        } else {
            // unlocked, treat as '(' in forward pass
            ++balance;
        }
        if (balance < 0) return false;
    }

    balance = 0;
    for (int i = n - 1; i >= 0; --i) {
        if (locked[i] == '1') {
            if (s[i] == ')') ++balance;
            else --balance;
        } else {
            // unlocked, treat as ')' in reverse pass
            ++balance;
        }
        if (balance < 0) return false;
    }

    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CanBeValid(string s, string locked) {
        int n = s.Length;
        if ((n & 1) == 1) return false;

        int balance = 0;
        // Left to right: treat all unlocked as '('
        for (int i = 0; i < n; i++) {
            if (locked[i] == '1') {
                balance += s[i] == '(' ? 1 : -1;
            } else {
                // unlocked, assume '(' to maximize opens
                balance++;
            }
            if (balance < 0) return false;
        }

        balance = 0;
        // Right to left: treat all unlocked as ')'
        for (int i = n - 1; i >= 0; i--) {
            if (locked[i] == '1') {
                balance += s[i] == ')' ? 1 : -1;
            } else {
                // unlocked, assume ')' to maximize closes
                balance++;
            }
            if (balance < 0) return false;
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} locked
 * @return {boolean}
 */
var canBeValid = function(s, locked) {
    const n = s.length;
    if (n % 2 === 1) return false;

    // Forward pass: treat unlocked as '(' to avoid excess ')'
    let balance = 0;
    for (let i = 0; i < n; i++) {
        if (locked[i] === '1') {
            balance += s[i] === '(' ? 1 : -1;
        } else {
            // unlocked, assume '('
            balance++;
        }
        if (balance < 0) return false;
    }

    // Reverse pass: treat unlocked as ')' to avoid excess '('
    balance = 0;
    for (let i = n - 1; i >= 0; i--) {
        if (locked[i] === '1') {
            balance += s[i] === ')' ? 1 : -1;
        } else {
            // unlocked, assume ')'
            balance++;
        }
        if (balance < 0) return false;
    }

    return true;
};
```

## Typescript

```typescript
function canBeValid(s: string, locked: string): boolean {
    const n = s.length;
    if (n % 2 === 1) return false;

    // Left to right pass
    let bal = 0;   // unmatched '(' from locked positions
    let free = 0;  // count of unlocked positions that can act as '('
    for (let i = 0; i < n; i++) {
        if (locked[i] === '0') {
            free++;
        } else {
            bal += s[i] === '(' ? 1 : -1;
        }
        if (bal < 0) {
            if (free === 0) return false;
            free--;
            bal = 0; // use one unlocked as '('
        }
    }
    if (bal > free) return false; // remaining '(' need unlocked ')'

    // Right to left pass
    let balR = 0;   // unmatched ')' from locked positions
    let freeR = 0;  // count of unlocked positions that can act as ')'
    for (let i = n - 1; i >= 0; i--) {
        if (locked[i] === '0') {
            freeR++;
        } else {
            balR += s[i] === ')' ? 1 : -1;
        }
        if (balR < 0) {
            if (freeR === 0) return false;
            freeR--;
            balR = 0; // use one unlocked as ')'
        }
    }
    if (balR > freeR) return false;

    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $locked
     * @return Boolean
     */
    function canBeValid($s, $locked) {
        $n = strlen($s);
        if ($n % 2 == 1) {
            return false;
        }

        // Left to right pass: ensure no prefix has more ')' than possible '('
        $open = 0;   // unmatched '(' from locked positions
        $free = 0;   // count of unlocked positions that can be used as '(' or ')'
        for ($i = 0; $i < $n; ++$i) {
            if ($locked[$i] === '0') {
                $free++;
            } else {
                if ($s[$i] === '(') {
                    $open++;
                } else { // ')'
                    if ($open > 0) {
                        $open--;
                    } elseif ($free > 0) {
                        $free--;
                    } else {
                        return false;
                    }
                }
            }
        }
        // Remaining unmatched '(' must be covered by remaining free positions
        if ($open > $free) {
            return false;
        }

        // Right to left pass: ensure no suffix has more '(' than possible ')'
        $close = 0; // unmatched ')' from locked positions
        $free = 0;  // unlocked positions in this direction
        for ($i = $n - 1; $i >= 0; --$i) {
            if ($locked[$i] === '0') {
                $free++;
            } else {
                if ($s[$i] === ')') {
                    $close++;
                } else { // '('
                    if ($close > 0) {
                        $close--;
                    } elseif ($free > 0) {
                        $free--;
                    } else {
                        return false;
                    }
                }
            }
        }
        if ($close > $free) {
            return false;
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func canBeValid(_ s: String, _ locked: String) -> Bool {
        let n = s.count
        if n % 2 == 1 { return false }
        let sArr = Array(s)
        let lArr = Array(locked)

        var balance = 0
        for i in 0..<n {
            if lArr[i] == "1" {
                if sArr[i] == "(" {
                    balance += 1
                } else {
                    balance -= 1
                }
            } else {
                // treat unlocked as '(' to maximize opening count
                balance += 1
            }
            if balance < 0 { return false }
        }

        balance = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            if lArr[i] == "1" {
                if sArr[i] == ")" {
                    balance += 1
                } else {
                    balance -= 1
                }
            } else {
                // treat unlocked as ')' to maximize closing count
                balance += 1
            }
            if balance < 0 { return false }
        }

        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canBeValid(s: String, locked: String): Boolean {
        val n = s.length
        if (n % 2 == 1) return false

        var balance = 0
        for (i in 0 until n) {
            if (locked[i] == '1') {
                if (s[i] == '(') balance++ else balance--
            } else {
                // treat unlocked as '(' in forward pass
                balance++
            }
            if (balance < 0) return false
        }

        balance = 0
        for (i in n - 1 downTo 0) {
            if (locked[i] == '1') {
                if (s[i] == ')') balance++ else balance--
            } else {
                // treat unlocked as ')' in reverse pass
                balance++
            }
            if (balance < 0) return false
        }

        return true
    }
}
```

## Dart

```dart
class Solution {
  bool canBeValid(String s, String locked) {
    int n = s.length;
    if (n % 2 == 1) return false;

    // Forward pass: treat unlocked as '('
    int balance = 0;
    for (int i = 0; i < n; i++) {
      if (locked[i] == '1') {
        if (s[i] == '(') {
          balance++;
        } else {
          balance--;
        }
      } else {
        // unlocked, can be '('
        balance++;
      }
      if (balance < 0) return false;
    }

    // Backward pass: treat unlocked as ')'
    balance = 0;
    for (int i = n - 1; i >= 0; i--) {
      if (locked[i] == '1') {
        if (s[i] == ')') {
          balance++;
        } else {
          balance--;
        }
      } else {
        // unlocked, can be ')'
        balance++;
      }
      if (balance < 0) return false;
    }

    return true;
  }
}
```

## Golang

```go
func canBeValid(s string, locked string) bool {
	n := len(s)
	if n%2 == 1 {
		return false
	}
	balance := 0
	for i := 0; i < n; i++ {
		if locked[i] == '1' {
			if s[i] == '(' {
				balance++
			} else {
				balance--
			}
		} else {
			// treat unlocked as '(' to maximize opening brackets
			balance++
		}
		if balance < 0 {
			return false
		}
	}
	balance = 0
	for i := n - 1; i >= 0; i-- {
		if locked[i] == '1' {
			if s[i] == ')' {
				balance++
			} else {
				balance--
			}
		} else {
			// treat unlocked as ')' to maximize closing brackets
			balance++
		}
		if balance < 0 {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def can_be_valid(s, locked)
  n = s.length
  return false if n.odd?
  low = 0
  high = 0
  n.times do |i|
    if locked.getbyte(i) == 49 # '1'
      if s.getbyte(i) == 40   # '('
        low += 1
        high += 1
      else                    # ')'
        low -= 1
        high -= 1
      end
    else                       # unlocked, can be either '(' or ')'
      low -= 1
      high += 1
    end
    low = 0 if low < 0
    return false if high < 0
  end
  low == 0
end
```

## Scala

```scala
object Solution {
  def canBeValid(s: String, locked: String): Boolean = {
    val n = s.length
    if (n % 2 == 1) return false

    var balance = 0   // unmatched '(' count
    var free = 0      // unlocked positions that can act as '('
    for (i <- 0 until n) {
      if (locked.charAt(i) == '0') {
        free += 1
      } else {
        if (s.charAt(i) == '(') {
          balance += 1
        } else { // locked ')'
          if (balance > 0) {
            balance -= 1
          } else if (free > 0) {
            free -= 1 // use an unlocked position as '('
          } else {
            return false
          }
        }
      }
    }

    // Reverse pass to ensure remaining '(' can be matched by later unlocks turned into ')'
    balance = 0   // unmatched ')' count when scanning from right
    free = 0
    var i = n - 1
    while (i >= 0) {
      if (locked.charAt(i) == '0') {
        free += 1
      } else {
        if (s.charAt(i) == ')') {
          balance += 1
        } else { // locked '('
          if (balance > 0) {
            balance -= 1
          } else if (free > 0) {
            free -= 1 // use an unlocked position as ')'
          } else {
            return false
          }
        }
      }
      i -= 1
    }

    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn can_be_valid(s: String, locked: String) -> bool {
        let n = s.len();
        if n % 2 == 1 {
            return false;
        }
        let sb = s.as_bytes();
        let lb = locked.as_bytes();

        // Forward pass: treat unlocked as '('
        let mut balance: i32 = 0;
        for i in 0..n {
            if lb[i] == b'1' {
                if sb[i] == b'(' {
                    balance += 1;
                } else {
                    balance -= 1;
                }
            } else {
                // unlocked, can be '('
                balance += 1;
            }
            if balance < 0 {
                return false;
            }
        }

        // Backward pass: treat unlocked as ')'
        let mut balance: i32 = 0;
        for i in (0..n).rev() {
            if lb[i] == b'1' {
                if sb[i] == b')' {
                    balance += 1;
                } else {
                    balance -= 1;
                }
            } else {
                // unlocked, can be ')'
                balance += 1;
            }
            if balance < 0 {
                return false;
            }
        }

        true
    }
}
```

## Racket

```racket
(define/contract (can-be-valid s locked)
  (-> string? string? boolean?)
  (let ((n (string-length s)))
    (if (odd? n)
        #f
        (let loop ((i 0) (low 0) (high 0))
          (if (= i n)
              (= low 0)
              (let* ((lc (string-ref locked i))
                     (sc (string-ref s i))
                     (low2 (cond
                             [(char=? lc #\1)
                              (if (char=? sc #\()
                                  (+ low 1)
                                  (- low 1))]
                             [else (- low 1)]))
                     (high2 (cond
                              [(char=? lc #\1)
                               (if (char=? sc #\()
                                   (+ high 1)
                                   (- high 1))]
                              [else (+ high 1)])))
                (if (< high2 0)
                    #f
                    (loop (+ i 1) (max low2 0) high2)))))))))
```

## Erlang

```erlang
-module(solution).
-export([can_be_valid/2]).

-spec can_be_valid(S :: unicode:unicode_binary(), Locked :: unicode:unicode_binary()) -> boolean().
can_be_valid(S, Locked) ->
    N = byte_size(S),
    if
        N rem 2 =:= 1 ->
            false;
        true ->
            Slist = binary_to_list(S),
            Llist = binary_to_list(Locked),
            case forward(Slist, Llist, 0) of
                false -> false;
                true -> reverse_check(Slist, Llist)
            end
    end.

forward([], [], _) ->
    true;
forward([Sc|Ss], [Lc|Ls], Bal) ->
    NewBal = case Lc of
        $0 -> Bal + 1;               % unlocked, treat as '(' in forward pass
        $1 ->
            if Sc == $( -> Bal + 1;
               true   -> Bal - 1
            end
    end,
    if
        NewBal < 0 -> false;
        true      -> forward(Ss, Ls, NewBal)
    end.

reverse_check(Slist, Llist) ->
    rev_loop(lists:reverse(Slist), lists:reverse(Llist), 0).

rev_loop([], [], _) ->
    true;
rev_loop([Sc|Ss], [Lc|Ls], Bal) ->
    NewBal = case Lc of
        $0 -> Bal + 1;               % unlocked, treat as ')' in reverse pass
        $1 ->
            if Sc == $) -> Bal + 1;
               true   -> Bal - 1
            end
    end,
    if
        NewBal < 0 -> false;
        true      -> rev_loop(Ss, Ls, NewBal)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_be_valid(s :: String.t(), locked :: String.t()) :: boolean()
  def can_be_valid(s, locked) do
    n = byte_size(s)

    if rem(n, 2) == 1 do
      false
    else
      s_bytes = :binary.bin_to_list(s)
      l_bytes = :binary.bin_to_list(locked)

      {low, high, possible} =
        Enum.reduce_while(Enum.zip(s_bytes, l_bytes), {0, 0, true}, fn {c, lock},
                                                                      {low, high, _} ->
          {new_low, new_high} =
            if lock == ?1 do
              delta = if c == ?(, do: 1, else: -1)
              {low + delta, high + delta}
            else
              # unlocked position can be '(' or ')'
              {low - 1, high + 1}
            end

          adj_low = max(new_low, 0)

          if new_high < 0 do
            {:halt, {adj_low, new_high, false}}
          else
            {:cont, {adj_low, new_high, true}}
          end
        end)

      possible and low == 0
    end
  end
end
```
