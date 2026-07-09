# 0844. Backspace String Compare

## Cpp

```cpp
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        int i = (int)s.size() - 1;
        int j = (int)t.size() - 1;
        while (i >= 0 || j >= 0) {
            int skipS = 0;
            while (i >= 0) {
                if (s[i] == '#') {
                    ++skipS;
                    --i;
                } else if (skipS > 0) {
                    --skipS;
                    --i;
                } else {
                    break;
                }
            }
            int skipT = 0;
            while (j >= 0) {
                if (t[j] == '#') {
                    ++skipT;
                    --j;
                } else if (skipT > 0) {
                    --skipT;
                    --j;
                } else {
                    break;
                }
            }
            char chS = i >= 0 ? s[i] : '\0';
            char chT = j >= 0 ? t[j] : '\0';
            if (i >= 0 && j >= 0) {
                if (chS != chT) return false;
            } else {
                if (i >= 0 || j >= 0) return false;
            }
            --i;
            --j;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean backspaceCompare(String s, String t) {
        int i = s.length() - 1;
        int j = t.length() - 1;
        while (i >= 0 || j >= 0) {
            i = nextValidCharIndex(s, i);
            j = nextValidCharIndex(t, j);
            if (i < 0 && j < 0) return true;
            if (i < 0 || j < 0) return false;
            if (s.charAt(i) != t.charAt(j)) return false;
            i--;
            j--;
        }
        return true;
    }

    private int nextValidCharIndex(String str, int index) {
        int skip = 0;
        while (index >= 0) {
            char c = str.charAt(index);
            if (c == '#') {
                skip++;
                index--;
            } else {
                if (skip > 0) {
                    skip--;
                    index--;
                } else {
                    break;
                }
            }
        }
        return index;
    }
}
```

## Python

```python
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            # Find next valid character in s
            skip = 0
            while i >= 0:
                if s[i] == '#':
                    skip += 1
                    i -= 1
                elif skip > 0:
                    skip -= 1
                    i -= 1
                else:
                    break
            # Find next valid character in t
            skip = 0
            while j >= 0:
                if t[j] == '#':
                    skip += 1
                    j -= 1
                elif skip > 0:
                    skip -= 1
                    j -= 1
                else:
                    break

            # Compare characters
            ch_s = s[i] if i >= 0 else None
            ch_t = t[j] if j >= 0 else None
            if ch_s != ch_t:
                return False

            i -= 1
            j -= 1

        return True
```

## Python3

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            # find next valid char in s
            skip = 0
            while i >= 0:
                if s[i] == '#':
                    skip += 1
                    i -= 1
                elif skip > 0:
                    skip -= 1
                    i -= 1
                else:
                    break
            # find next valid char in t
            skip = 0
            while j >= 0:
                if t[j] == '#':
                    skip += 1
                    j -= 1
                elif skip > 0:
                    skip -= 1
                    j -= 1
                else:
                    break
            # compare characters
            c1 = s[i] if i >= 0 else None
            c2 = t[j] if j >= 0 else None
            if c1 != c2:
                return False
            i -= 1
            j -= 1
        return True
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool backspaceCompare(char* s, char* t) {
    int i = (int)strlen(s) - 1;
    int j = (int)strlen(t) - 1;

    while (i >= 0 || j >= 0) {
        int skip = 0;
        while (i >= 0) {
            if (s[i] == '#') {
                skip++;
                i--;
            } else if (skip > 0) {
                skip--;
                i--;
            } else {
                break;
            }
        }

        skip = 0;
        while (j >= 0) {
            if (t[j] == '#') {
                skip++;
                j--;
            } else if (skip > 0) {
                skip--;
                j--;
            } else {
                break;
            }
        }

        if (i < 0 && j < 0) return true;
        if (i < 0 || j < 0) return false;
        if (s[i] != t[j]) return false;

        i--;
        j--;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool BackspaceCompare(string s, string t)
    {
        int i = s.Length - 1;
        int j = t.Length - 1;

        while (i >= 0 || j >= 0)
        {
            int skipS = 0;
            while (i >= 0)
            {
                if (s[i] == '#')
                {
                    skipS++;
                    i--;
                }
                else if (skipS > 0)
                {
                    skipS--;
                    i--;
                }
                else
                {
                    break;
                }
            }

            int skipT = 0;
            while (j >= 0)
            {
                if (t[j] == '#')
                {
                    skipT++;
                    j--;
                }
                else if (skipT > 0)
                {
                    skipT--;
                    j--;
                }
                else
                {
                    break;
                }
            }

            char chS = i >= 0 ? s[i] : '\0';
            char chT = j >= 0 ? t[j] : '\0';

            if (i >= 0 && j >= 0)
            {
                if (chS != chT) return false;
            }
            else
            {
                if (i >= 0 || j >= 0) return false;
            }

            i--;
            j--;
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    const nextValidIndex = (str, idx) => {
        let skip = 0;
        while (idx >= 0) {
            if (str[idx] === '#') {
                skip++;
                idx--;
            } else if (skip > 0) {
                skip--;
                idx--;
            } else {
                break;
            }
        }
        return idx;
    };
    
    let i = s.length - 1;
    let j = t.length - 1;
    
    while (i >= 0 || j >= 0) {
        i = nextValidIndex(s, i);
        j = nextValidIndex(t, j);
        
        const chS = i >= 0 ? s[i] : null;
        const chT = j >= 0 ? t[j] : null;
        
        if (chS !== chT) return false;
        
        i--;
        j--;
    }
    
    return true;
};
```

## Typescript

```typescript
function backspaceCompare(s: string, t: string): boolean {
    let i = s.length - 1;
    let j = t.length - 1;
    let skipS = 0;
    let skipT = 0;

    while (i >= 0 || j >= 0) {
        // Find next valid character in s
        while (i >= 0) {
            if (s[i] === '#') {
                skipS++;
                i--;
            } else if (skipS > 0) {
                skipS--;
                i--;
            } else {
                break;
            }
        }

        // Find next valid character in t
        while (j >= 0) {
            if (t[j] === '#') {
                skipT++;
                j--;
            } else if (skipT > 0) {
                skipT--;
                j--;
            } else {
                break;
            }
        }

        const charS = i >= 0 ? s[i] : null;
        const charT = j >= 0 ? t[j] : null;

        if (charS !== charT) return false;

        i--;
        j--;
    }

    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function backspaceCompare($s, $t) {
        $i = strlen($s) - 1;
        $j = strlen($t) - 1;

        while ($i >= 0 || $j >= 0) {
            $skip = 0;
            while ($i >= 0) {
                if ($s[$i] === '#') {
                    $skip++;
                    $i--;
                } elseif ($skip > 0) {
                    $skip--;
                    $i--;
                } else {
                    break;
                }
            }

            $skip = 0;
            while ($j >= 0) {
                if ($t[$j] === '#') {
                    $skip++;
                    $j--;
                } elseif ($skip > 0) {
                    $skip--;
                    $j--;
                } else {
                    break;
                }
            }

            $c1 = $i >= 0 ? $s[$i] : null;
            $c2 = $j >= 0 ? $t[$j] : null;

            if ($c1 !== $c2) {
                return false;
            }

            $i--;
            $j--;
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func backspaceCompare(_ s: String, _ t: String) -> Bool {
        var i = s.endIndex
        var j = t.endIndex
        
        func nextValidChar(_ str: String, _ idx: inout String.Index) -> Character? {
            var skip = 0
            while idx > str.startIndex {
                idx = str.index(before: idx)
                let ch = str[idx]
                if ch == "#" {
                    skip += 1
                } else {
                    if skip > 0 {
                        skip -= 1
                    } else {
                        return ch
                    }
                }
            }
            return nil
        }
        
        while true {
            let c1 = nextValidChar(s, &i)
            let c2 = nextValidChar(t, &j)
            
            if c1 == nil && c2 == nil { return true }
            if c1 == nil || c2 == nil { return false }
            if c1! != c2! { return false }
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun backspaceCompare(s: String, t: String): Boolean {
        var i = s.length - 1
        var j = t.length - 1

        while (i >= 0 || j >= 0) {
            i = nextValidCharIndex(s, i)
            j = nextValidCharIndex(t, j)

            if (i < 0 && j < 0) return true
            if (i < 0 || j < 0) return false
            if (s[i] != t[j]) return false

            i--
            j--
        }
        return true
    }

    private fun nextValidCharIndex(str: String, startIdx: Int): Int {
        var idx = startIdx
        var skip = 0
        while (idx >= 0) {
            if (str[idx] == '#') {
                skip++
                idx--
            } else {
                if (skip > 0) {
                    skip--
                    idx--
                } else {
                    break
                }
            }
        }
        return idx
    }
}
```

## Dart

```dart
class Solution {
  bool backspaceCompare(String s, String t) {
    int i = s.length - 1;
    int j = t.length - 1;

    while (i >= 0 || j >= 0) {
      i = _nextValidCharIndex(s, i);
      j = _nextValidCharIndex(t, j);

      if (i < 0 && j < 0) return true;
      if (i < 0 || j < 0) return false;
      if (s[i] != t[j]) return false;

      i--;
      j--;
    }
    return true;
  }

  int _nextValidCharIndex(String str, int index) {
    int skip = 0;
    while (index >= 0) {
      if (str[index] == '#') {
        skip++;
        index--;
      } else if (skip > 0) {
        skip--;
        index--;
      } else {
        break;
      }
    }
    return index;
  }
}
```

## Golang

```go
func backspaceCompare(s string, t string) bool {
	i := len(s) - 1
	j := len(t) - 1

	for i >= 0 || j >= 0 {
		skip := 0
		for i >= 0 {
			if s[i] == '#' {
				skip++
				i--
			} else if skip > 0 {
				skip--
				i--
			} else {
				break
			}
		}

		skip = 0
		for j >= 0 {
			if t[j] == '#' {
				skip++
				j--
			} else if skip > 0 {
				skip--
				j--
			} else {
				break
			}
		}

		if i >= 0 && j >= 0 {
			if s[i] != t[j] {
				return false
			}
		} else if i >= 0 || j >= 0 {
			return false
		}
		i--
		j--
	}
	return true
}
```

## Ruby

```ruby
def backspace_compare(s, t)
  i = s.length - 1
  j = t.length - 1

  while i >= 0 || j >= 0
    skip = 0
    while i >= 0
      if s.getbyte(i) == 35 # '#'
        skip += 1
        i -= 1
      elsif skip > 0
        skip -= 1
        i -= 1
      else
        break
      end
    end

    skip = 0
    while j >= 0
      if t.getbyte(j) == 35 # '#'
        skip += 1
        j -= 1
      elsif skip > 0
        skip -= 1
        j -= 1
      else
        break
      end
    end

    c1 = i >= 0 ? s.getbyte(i) : nil
    c2 = j >= 0 ? t.getbyte(j) : nil

    return false if c1 != c2

    i -= 1
    j -= 1
  end

  true
end
```

## Scala

```scala
object Solution {
  def backspaceCompare(s: String, t: String): Boolean = {
    var i = s.length - 1
    var j = t.length - 1

    def nextValidIndex(str: String, idx: Int): Int = {
      var k = idx
      var skip = 0
      while (k >= 0) {
        if (str.charAt(k) == '#') {
          skip += 1
          k -= 1
        } else if (skip > 0) {
          skip -= 1
          k -= 1
        } else {
          return k
        }
      }
      -1
    }

    while (i >= 0 || j >= 0) {
      i = nextValidIndex(s, i)
      j = nextValidIndex(t, j)

      if (i < 0 && j < 0) return true
      if (i < 0 || j < 0) return false
      if (s.charAt(i) != t.charAt(j)) return false

      i -= 1
      j -= 1
    }
    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn backspace_compare(s: String, t: String) -> bool {
        let s_chars: Vec<char> = s.chars().collect();
        let t_chars: Vec<char> = t.chars().collect();

        let mut i: isize = s_chars.len() as isize - 1;
        let mut j: isize = t_chars.len() as isize - 1;

        // Helper closure to get next valid character from the end
        fn next_valid(chars: &Vec<char>, idx: &mut isize) -> Option<char> {
            let mut skip = 0;
            while *idx >= 0 {
                let c = chars[*idx as usize];
                if c == '#' {
                    skip += 1;
                } else if skip > 0 {
                    skip -= 1;
                } else {
                    *idx -= 1;
                    return Some(c);
                }
                *idx -= 1;
            }
            None
        }

        loop {
            let c1 = next_valid(&s_chars, &mut i);
            let c2 = next_valid(&t_chars, &mut j);

            match (c1, c2) {
                (None, None) => return true,
                (Some(ch1), Some(ch2)) if ch1 == ch2 => continue,
                _ => return false,
            }
        }
    }
}
```

## Racket

```racket
(define/contract (backspace-compare s t)
  (-> string? string? boolean?)
  (let* ((len-s (string-length s))
         (len-t (string-length t)))
    (define (next-valid-index str idx)
      (let loop ((i idx) (skip 0))
        (cond [(< i 0) -1]
              [(char=? (string-ref str i) #\#)
               (loop (- i 1) (+ skip 1))]
              [(> skip 0)
               (loop (- i 1) (- skip 1))]
              [else i])))
    (let loop ((i (sub1 len-s)) (j (sub1 len-t)))
      (let* ((ni (next-valid-index s i))
             (nj (next-valid-index t j)))
        (cond [(and (= ni -1) (= nj -1)) #t]
              [(or (= ni -1) (= nj -1)) #f]
              [else
               (if (char=? (string-ref s ni) (string-ref t nj))
                   (loop (- ni 1) (- nj 1))
                   #f)])))))
```

## Erlang

```erlang
-spec backspace_compare(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> boolean().
backspace_compare(S, T) ->
    cmp(S, byte_size(S) - 1, T, byte_size(T) - 1).

cmp(_S, Si, _T, Ti) when Si < 0, Ti < 0 ->
    true;
cmp(S, Si, T, Ti) ->
    {Sc, SNext} = find_next(S, Si),
    {Tc, TNext} = find_next(T, Ti),
    case {Sc, Tc} of
        {undefined, undefined} -> true;
        {undefined, _} -> false;
        {_, undefined} -> false;
        {SChar, TChar} when SChar =:= TChar ->
            cmp(S, SNext, T, TNext);
        _ -> false
    end.

find_next(_Bin, Index) when Index < 0 ->
    {undefined, -1};
find_next(Bin, Index) ->
    go_find(Bin, Index, 0).

go_find(_Bin, Index, _Back) when Index < 0 ->
    {undefined, -1};
go_find(Bin, Index, Back) ->
    Char = binary:at(Bin, Index),
    if
        Char == $# ->
            go_find(Bin, Index - 1, Back + 1);
        Back > 0 ->
            go_find(Bin, Index - 1, Back - 1);
        true ->
            {Char, Index - 1}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec backspace_compare(s :: String.t(), t :: String.t()) :: boolean()
  def backspace_compare(s, t) do
    process(s) == process(t)
  end

  defp process(str) do
    str
    |> String.graphemes()
    |> Enum.reduce([], fn
      "#", [_ | rest] -> rest
      "#", [] -> []
      ch, acc -> [ch | acc]
    end)
    |> Enum.reverse()
  end
end
```
