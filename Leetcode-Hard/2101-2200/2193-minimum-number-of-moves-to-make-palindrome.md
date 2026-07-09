# 2193. Minimum Number of Moves to Make Palindrome

## Cpp

```cpp
class Solution {
public:
    int minMovesToMakePalindrome(string s) {
        long long moves = 0;
        int l = 0, r = (int)s.size() - 1;
        while (l < r) {
            if (s[l] == s[r]) {
                ++l;
                --r;
                continue;
            }
            int k = r;
            while (k > l && s[k] != s[l]) --k;
            if (k == l) { // unique middle character
                swap(s[l], s[l + 1]);
                ++moves;
            } else {
                for (int i = k; i < r; ++i) {
                    swap(s[i], s[i + 1]);
                    ++moves;
                }
                ++l;
                --r;
            }
        }
        return (int)moves;
    }
};
```

## Java

```java
class Solution {
    public int minMovesToMakePalindrome(String s) {
        char[] arr = s.toCharArray();
        int n = arr.length;
        int i = 0, j = n - 1;
        int moves = 0;
        while (i < j) {
            if (arr[i] == arr[j]) {
                i++;
                j--;
                continue;
            }
            int k = j;
            while (k > i && arr[k] != arr[i]) {
                k--;
            }
            if (k == i) { // no matching character, this char must be the middle one
                // swap it with its next neighbor
                char temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
                moves++;
            } else {
                // bring arr[k] to position j by swapping adjacent characters
                while (k < j) {
                    char temp = arr[k];
                    arr[k] = arr[k + 1];
                    arr[k + 1] = temp;
                    k++;
                    moves++;
                }
                i++;
                j--;
            }
        }
        return moves;
    }
}
```

## Python

```python
class Solution(object):
    def minMovesToMakePalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = list(s)
        i, j = 0, len(arr) - 1
        moves = 0
        while i < j:
            if arr[i] == arr[j]:
                i += 1
                j -= 1
                continue
            # find matching character for arr[i] from the right side
            k = j
            while k > i and arr[k] != arr[i]:
                k -= 1
            if k == i:  # this char must be the middle one
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                moves += 1
            else:
                # bring arr[k] to position j by adjacent swaps
                while k < j:
                    arr[k], arr[k + 1] = arr[k + 1], arr[k]
                    moves += 1
                    k += 1
                i += 1
                j -= 1
        return moves
```

## Python3

```python
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        lst = list(s)
        left, right = 0, len(lst) - 1
        moves = 0
        while left < right:
            if lst[left] == lst[right]:
                left += 1
                right -= 1
                continue
            i = right
            while i > left and lst[i] != lst[left]:
                i -= 1
            if i == left:  # unique middle character
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                moves += 1
            else:
                while i < right:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    moves += 1
                    i += 1
                left += 1
                right -= 1
        return moves
```

## C

```c
#include <string.h>
#include <stdlib.h>

int minMovesToMakePalindrome(char* s) {
    int n = (int)strlen(s);
    char *a = (char *)malloc(n + 1);
    memcpy(a, s, n + 1);

    long long moves = 0;
    int i = 0, j = n - 1;

    while (i < j) {
        if (a[i] == a[j]) {
            ++i;
            --j;
            continue;
        }

        int k = j;
        while (k > i && a[k] != a[i]) {
            --k;
        }

        if (k == i) {  // character at i is the middle one
            char tmp = a[i];
            a[i] = a[i + 1];
            a[i + 1] = tmp;
            ++moves;
        } else {
            while (k < j) {
                char tmp = a[k];
                a[k] = a[k + 1];
                a[k + 1] = tmp;
                ++moves;
                ++k;
            }
            ++i;
            --j;
        }
    }

    free(a);
    return (int)moves;
}
```

## Csharp

```csharp
public class Solution {
    public int MinMovesToMakePalindrome(string s) {
        var chars = new System.Collections.Generic.List<char>(s);
        int i = 0, j = chars.Count - 1;
        long moves = 0;
        while (i < j) {
            if (chars[i] == chars[j]) {
                i++;
                j--;
                continue;
            }
            int k = j;
            while (k > i && chars[k] != chars[i]) k--;
            if (k == i) { // unique middle character
                var tmp = chars[i];
                chars[i] = chars[i + 1];
                chars[i + 1] = tmp;
                moves++;
            } else {
                for (int l = k; l < j; l++) {
                    var tmp = chars[l];
                    chars[l] = chars[l + 1];
                    chars[l + 1] = tmp;
                }
                moves += (j - k);
                i++;
                j--;
            }
        }
        return (int)moves;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minMovesToMakePalindrome = function(s) {
    const arr = s.split('');
    let left = 0;
    let right = arr.length - 1;
    let moves = 0;

    while (left < right) {
        if (arr[left] === arr[right]) {
            left++;
            right--;
            continue;
        }

        // Find matching character for arr[left] from the right side
        let i = right;
        while (i > left && arr[i] !== arr[left]) {
            i--;
        }

        if (i === left) {
            // No match found; this char must be the middle one.
            // Swap it towards the center by one position.
            [arr[left], arr[left + 1]] = [arr[left + 1], arr[left]];
            moves++;
        } else {
            // Bring the matching character to the right end
            for (let j = i; j < right; j++) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                moves++;
            }
            left++;
            right--;
        }
    }

    return moves;
};
```

## Typescript

```typescript
function minMovesToMakePalindrome(s: string): number {
    const arr = s.split('');
    let i = 0;
    let j = arr.length - 1;
    let moves = 0;

    while (i < j) {
        if (arr[i] === arr[j]) {
            i++;
            j--;
            continue;
        }

        // Find matching character for arr[i] from the right side
        let k = j;
        while (k > i && arr[k] !== arr[i]) {
            k--;
        }

        if (k === i) {
            // No match found; this char must be the middle one.
            // Swap it one step towards the center.
            const temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
            moves++;
        } else {
            // Bring the matching character at position k to position j
            while (k < j) {
                const temp = arr[k];
                arr[k] = arr[k + 1];
                arr[k + 1] = temp;
                k++;
                moves++;
            }
            i++;
            j--;
        }
    }

    return moves;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minMovesToMakePalindrome($s) {
        $arr = str_split($s);
        $n = count($arr);
        $left = 0;
        $right = $n - 1;
        $moves = 0;

        while ($left < $right) {
            if ($arr[$left] === $arr[$right]) {
                $left++;
                $right--;
                continue;
            }

            // Find matching character for arr[left] from right side
            $k = $right - 1;
            while ($k > $left && $arr[$k] !== $arr[$left]) {
                $k--;
            }

            if ($k == $left) { // No matching char, this must be the middle one
                // Swap arr[left] with its next character
                [$arr[$left], $arr[$left + 1]] = [$arr[$left + 1], $arr[$left]];
                $moves++;
            } else {
                // Bring the matching character to position right by swapping adjacent chars
                while ($k < $right) {
                    [$arr[$k], $arr[$k + 1]] = [$arr[$k + 1], $arr[$k]];
                    $moves++;
                    $k++;
                }
                $left++;
                $right--;
            }
        }

        return $moves;
    }
}
```

## Swift

```swift
class Solution {
    func minMovesToMakePalindrome(_ s: String) -> Int {
        var chars = Array(s)
        var i = 0
        var j = chars.count - 1
        var moves = 0
        
        while i < j {
            if chars[i] == chars[j] {
                i += 1
                j -= 1
            } else {
                var k = j
                while k > i && chars[k] != chars[i] {
                    k -= 1
                }
                if k == i {
                    // No matching character; this char must be the middle one.
                    chars.swapAt(i, i + 1)
                    moves += 1
                } else {
                    // Bring the matching character to position j.
                    while k < j {
                        chars.swapAt(k, k + 1)
                        moves += 1
                        k += 1
                    }
                    i += 1
                    j -= 1
                }
            }
        }
        
        return moves
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMovesToMakePalindrome(s: String): Int {
        val arr = s.toCharArray()
        var left = 0
        var right = arr.size - 1
        var moves = 0
        while (left < right) {
            if (arr[left] == arr[right]) {
                left++
                right--
            } else {
                var k = right
                while (k > left && arr[k] != arr[left]) {
                    k--
                }
                if (k == left) {
                    // No matching character; swap with next character
                    val temp = arr[left]
                    arr[left] = arr[left + 1]
                    arr[left + 1] = temp
                    moves++
                } else {
                    while (k < right) {
                        val temp = arr[k]
                        arr[k] = arr[k + 1]
                        arr[k + 1] = temp
                        moves++
                        k++
                    }
                    left++
                    right--
                }
            }
        }
        return moves
    }
}
```

## Dart

```dart
class Solution {
  int minMovesToMakePalindrome(String s) {
    List<String> arr = s.split('');
    int left = 0;
    int right = arr.length - 1;
    int moves = 0;

    while (left < right) {
      if (arr[left] == arr[right]) {
        left++;
        right--;
        continue;
      }

      int k = right;
      while (k > left && arr[k] != arr[left]) {
        k--;
      }

      if (k == left) {
        // No matching character; swap with next to move towards center
        var temp = arr[left];
        arr[left] = arr[left + 1];
        arr[left + 1] = temp;
        moves++;
      } else {
        // Bring the matching character at k to position right
        while (k < right) {
          var temp = arr[k];
          arr[k] = arr[k + 1];
          arr[k + 1] = temp;
          moves++;
          k++;
        }
        left++;
        right--;
      }
    }

    return moves;
  }
}
```

## Golang

```go
func minMovesToMakePalindrome(s string) int {
	b := []byte(s)
	moves := 0
	left, right := 0, len(b)-1

	for left < right {
		if b[left] == b[right] {
			left++
			right--
			continue
		}
		i := right
		for i > left && b[i] != b[left] {
			i--
		}
		if i == left { // character at left is the middle one
			b[i], b[i+1] = b[i+1], b[i]
			moves++
		} else {
			for j := i; j < right; j++ {
				b[j], b[j+1] = b[j+1], b[j]
				moves++
			}
			left++
			right--
		}
	}
	return moves
}
```

## Ruby

```ruby
def min_moves_to_make_palindrome(s)
  arr = s.chars
  left = 0
  right = arr.length - 1
  moves = 0

  while left < right
    if arr[left] == arr[right]
      left += 1
      right -= 1
    else
      k = right - 1
      while k > left && arr[k] != arr[left]
        k -= 1
      end

      if k == left
        # unique middle character, swap it towards center
        arr[left], arr[left + 1] = arr[left + 1], arr[left]
        moves += 1
      else
        while k < right
          arr[k], arr[k + 1] = arr[k + 1], arr[k]
          moves += 1
          k += 1
        end
        left += 1
        right -= 1
      end
    end
  end

  moves
end
```

## Scala

```scala
object Solution {
    def minMovesToMakePalindrome(s: String): Int = {
        val arr = s.toCharArray
        var i = 0
        var j = arr.length - 1
        var moves = 0
        while (i < j) {
            if (arr(i) == arr(j)) {
                i += 1
                j -= 1
            } else {
                var k = j - 1
                while (k > i && arr(k) != arr(i)) {
                    k -= 1
                }
                if (k == i) {
                    // move the unmatched character towards center
                    val tmp = arr(i)
                    arr(i) = arr(i + 1)
                    arr(i + 1) = tmp
                    moves += 1
                } else {
                    while (k < j) {
                        val tmp = arr(k)
                        arr(k) = arr(k + 1)
                        arr(k + 1) = tmp
                        moves += 1
                        k += 1
                    }
                    i += 1
                    j -= 1
                }
            }
        }
        moves
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_moves_to_make_palindrome(s: String) -> i32 {
        let mut chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        if n <= 1 {
            return 0;
        }
        let mut left: usize = 0;
        let mut right: usize = n - 1;
        let mut moves: i32 = 0;

        while left < right {
            if chars[left] == chars[right] {
                left += 1;
                right -= 1;
            } else {
                // Find a matching character for chars[left] from the right side
                let mut k = right;
                while k > left && chars[k] != chars[left] {
                    k -= 1;
                }
                if k == left {
                    // No match found; this char must be the middle one.
                    chars.swap(left, left + 1);
                    moves += 1;
                } else {
                    // Bring the matching character to position 'right' by adjacent swaps
                    while k < right {
                        chars.swap(k, k + 1);
                        moves += 1;
                        k += 1;
                    }
                    left += 1;
                    right -= 1;
                }
            }
        }

        moves
    }
}
```

## Racket

```racket
(define/contract (min-moves-to-make-palindrome s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (vec (list->vector (string->list s))))
    (define (swap! a b)
      (let ((tmp (vector-ref vec a)))
        (vector-set! vec a (vector-ref vec b))
        (vector-set! vec b tmp)))
    (let loop ((i 0) (j (- n 1)) (moves 0))
      (cond
        [(>= i j) moves]
        [(char=? (vector-ref vec i) (vector-ref vec j))
         (loop (+ i 1) (- j 1) moves)]
        [else
         (let ((k (let search ((p j))
                    (if (= p i)
                        p
                        (if (char=? (vector-ref vec p) (vector-ref vec i))
                            p
                            (search (- p 1)))))))
           (if (= k i)
               (begin
                 (swap! i (+ i 1))
                 (loop i j (+ moves 1)))
               (let move ((p k) (m moves))
                 (if (= p j)
                     (loop (+ i 1) (- j 1) m)
                     (begin
                       (swap! p (+ p 1))
                       (move (+ p 1) (+ m 1))))))])))))
```

## Erlang

```erlang
-module(solution).
-export([min_moves_to_make_palindrome/1]).

-spec min_moves_to_make_palindrome(S :: unicode:unicode_binary()) -> integer().
min_moves_to_make_palindrome(S) ->
    List = unicode:characters_to_list(S),
    process(List, 0).

%% Recursive processing of the current list and accumulated moves
process([], Moves) -> Moves;
process([_], Moves) -> Moves;
process(L, Moves) ->
    First = hd(L),
    RevL = lists:reverse(L),
    Last = hd(RevL),
    case First == Last of
        true ->
            %% Remove matching ends
            Tail = tl(L),                     % drop first
            RevTail = lists:reverse(Tail),
            [_|MidRev] = RevTail,             % drop last (originally Last)
            NewL = lists:reverse(MidRev),
            process(NewL, Moves);
        false ->
            N = length(L),
            MatchPos = find_match(L, N - 1, First),
            case MatchPos of
                undefined ->
                    %% Unique middle character: swap it one step towards center
                    [Second|Rest] = tl(L),
                    NewL = [Second, First | Rest],
                    process(NewL, Moves + 1);
                K ->
                    Swaps = N - K,
                    Prefix = lists:sublist(L, K - 1),
                    Suffix = lists:nthtail(K, L),   % elements after position K
                    TempL = Prefix ++ Suffix ++ [First],
                    %% Remove the now matching ends
                    Tail2 = tl(TempL),
                    RevTail2 = lists:reverse(Tail2),
                    [_|MidRev2] = RevTail2,
                    NewL = lists:reverse(MidRev2),
                    process(NewL, Moves + Swaps)
            end
    end.

%% Find the rightmost position (starting from Pos down to 2) where Char occurs.
find_match(_List, Pos, _Char) when Pos < 2 -> undefined;
find_match(List, Pos, Char) ->
    case lists:nth(Pos, List) of
        Char -> Pos;
        _ -> find_match(List, Pos - 1, Char)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_moves_to_make_palindrome(s :: String.t()) :: integer()
  def min_moves_to_make_palindrome(s) do
    chars = String.graphemes(s)
    {moves, _} = process(chars, 0, length(chars) - 1, 0)
    moves
  end

  # Base case: pointers have crossed or met
  defp process(chars, left, right, moves) when left >= right do
    {moves, chars}
  end

  # Characters already match, move inward
  defp process(chars, left, right, moves) do
    if Enum.at(chars, left) == Enum.at(chars, right) do
      process(chars, left + 1, right - 1, moves)
    else
      k = find_match(chars, left, right - 1)

      if k == left do
        # No matching character on the right side; this char belongs to the middle.
        chars2 = swap(chars, left, left + 1)
        process(chars2, left, right, moves + 1)
      else
        {chars2, added} = bring_to_right(chars, k, right)
        process(chars2, left + 1, right - 1, moves + added)
      end
    end
  end

  # Find the index of a character matching chars[left] searching from idx downwards.
  defp find_match(_chars, left, idx) when idx <= left, do: left

  defp find_match(chars, left, idx) do
    if Enum.at(chars, idx) == Enum.at(chars, left) do
      idx
    else
      find_match(chars, left, idx - 1)
    end
  end

  # Move the character at position k to position right by adjacent swaps.
  defp bring_to_right(chars, k, right) when k == right do
    {chars, 0}
  end

  defp bring_to_right(chars, k, right) do
    chars2 = swap(chars, k, k + 1)
    {final_chars, added} = bring_to_right(chars2, k + 1, right)
    {final_chars, added + 1}
  end

  # Swap elements at positions i and j in the list.
  defp swap(list, i, j) do
    vi = Enum.at(list, i)
    vj = Enum.at(list, j)

    list
    |> List.replace_at(i, vj)
    |> List.replace_at(j, vi)
  end
end
```
