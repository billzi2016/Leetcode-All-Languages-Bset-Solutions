# 2030. Smallest K-Length Subsequence With Occurrences of a Letter

## Cpp

```cpp
class Solution {
public:
    string smallestSubsequence(string s, int k, char letter, int repetition) {
        int n = s.size();
        vector<int> suff(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            suff[i] = suff[i + 1] + (s[i] == letter);
        }
        vector<char> st;
        int cntLetter = 0;
        for (int i = 0; i < n; ++i) {
            char c = s[i];
            // try to pop larger chars while we can still satisfy constraints
            while (!st.empty() && st.back() > c &&
                   (int)st.size() - 1 + (n - i) >= k) {
                int newCnt = cntLetter - (st.back() == letter);
                if (newCnt + suff[i] >= repetition) {
                    if (st.back() == letter) --cntLetter;
                    st.pop_back();
                } else break;
            }
            if ((int)st.size() == k) continue; // already full
            if (c == letter) {
                st.push_back(c);
                ++cntLetter;
            } else {
                int neededLetters = repetition - cntLetter;
                if (neededLetters < 0) neededLetters = 0;
                int slotsAfterPush = k - ((int)st.size() + 1);
                // ensure enough slots remain for required letters
                if (slotsAfterPush >= neededLetters) {
                    st.push_back(c);
                }
            }
        }
        // In case we have more than k characters (should not happen), truncate.
        return string(st.begin(), st.begin() + k);
    }
};
```

## Java

```java
class Solution {
    public String smallestSubsequence(String s, int k, char letter, int repetition) {
        int n = s.length();
        int[] suffix = new int[n + 1];
        for (int i = n - 1; i >= 0; --i) {
            suffix[i] = suffix[i + 1] + (s.charAt(i) == letter ? 1 : 0);
        }

        char[] stack = new char[k];
        int top = 0;
        int cntLetter = 0;

        for (int i = 0; i < n; ++i) {
            char c = s.charAt(i);

            while (top > 0) {
                char topChar = stack[top - 1];
                if (topChar <= c) break;

                // enough characters left to fill k after popping
                int remainingChars = n - i;
                if ((top - 1) + remainingChars < k) break;

                // repetition feasibility after popping
                int cntAfterPop = cntLetter - (topChar == letter ? 1 : 0);
                int needRepAfterPop = Math.max(0, repetition - cntAfterPop);
                if (needRepAfterPop > suffix[i]) break;

                top--;
                if (topChar == letter) cntLetter--;
            }

            if (top < k) {
                if (c == letter) {
                    stack[top++] = c;
                    cntLetter++;
                } else {
                    int needRepNow = Math.max(0, repetition - cntLetter);
                    // ensure enough slots remain for required letters
                    if ((k - (top + 1)) >= needRepNow) {
                        stack[top++] = c;
                    }
                }
            }
        }

        return new String(stack, 0, k);
    }
}
```

## Python

```python
class Solution(object):
    def smallestSubsequence(self, s, k, letter, repetition):
        """
        :type s: str
        :type k: int
        :type letter: str
        :type repetition: int
        :rtype: str
        """
        n = len(s)
        total_letter = s.count(letter)
        remaining_letter = total_letter  # letters still in the suffix (including current)
        have_letter = 0
        stack = []

        for i, c in enumerate(s):
            # Try to pop larger characters while we can still fulfill length and repetition constraints
            while stack and c < stack[-1] and len(stack) - 1 + (n - i) >= k:
                top = stack[-1]
                if top == letter:
                    # After popping this required letter, can we still meet the needed repetitions?
                    if have_letter - 1 + remaining_letter >= repetition:
                        stack.pop()
                        have_letter -= 1
                    else:
                        break
                else:
                    stack.pop()
            # Decide whether to push current character
            if len(stack) < k:
                if c == letter:
                    stack.append(c)
                    have_letter += 1
                else:
                    # Ensure enough slots remain for the required letters
                    if k - len(stack) > repetition - have_letter:
                        stack.append(c)
            # Current character is now processed, update remaining count of target letters
            if c == letter:
                remaining_letter -= 1

        return ''.join(stack[:k])
```

## Python3

```python
class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n = len(s)
        # suffix count of required letter
        suff = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff[i] = suff[i + 1] + (s[i] == letter)

        stack = []
        cntL = 0  # number of 'letter' in stack

        for i, c in enumerate(s):
            # try to pop larger characters while keeping feasibility
            while stack:
                top = stack[-1]
                if top <= c:
                    break
                # after popping, can we still reach length k?
                if len(stack) - 1 + (n - i) < k:
                    break
                # after popping, can we still satisfy repetition requirement?
                cntL_if_pop = cntL - (top == letter)
                if cntL_if_pop + suff[i] < repetition:
                    break
                stack.pop()
                if top == letter:
                    cntL -= 1

            # decide whether to push current character
            if len(stack) < k:
                if c == letter:
                    stack.append(c)
                    cntL += 1
                else:
                    neededL = max(0, repetition - cntL)
                    slots_left = k - (len(stack) + 1)
                    if slots_left >= neededL:
                        stack.append(c)

        return ''.join(stack)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char* smallestSubsequence(char* s, int k, char letter, int repetition) {
    int n = (int)strlen(s);
    int *suf = (int *)malloc((n + 1) * sizeof(int));
    suf[n] = 0;
    for (int i = n - 1; i >= 0; --i) {
        suf[i] = suf[i + 1] + (s[i] == letter);
    }

    char *stack = (char *)malloc(k * sizeof(char));
    int sz = 0;
    int curRep = 0;

    for (int i = 0; i < n; ++i) {
        char c = s[i];
        while (sz > 0 && stack[sz - 1] > c &&
               (sz - 1 + (n - i) >= k) &&
               (curRep - (stack[sz - 1] == letter) + suf[i] >= repetition)) {
            if (stack[sz - 1] == letter) curRep--;
            sz--;
        }

        if (sz < k) {
            bool mustTake = false;
            if (c == letter && curRep < repetition) {
                if (curRep + suf[i + 1] < repetition) {
                    mustTake = true; // not enough letters later
                }
            }
            int remain = n - i;               // characters including current
            if (!mustTake && sz + (remain - 1) >= k) {
                continue;                     // we can afford to skip this character
            }
            stack[sz++] = c;
            if (c == letter) curRep++;
        }
    }

    char *res = (char *)malloc((k + 1) * sizeof(char));
    memcpy(res, stack, k);
    res[k] = '\0';

    free(stack);
    free(suf);
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string SmallestSubsequence(string s, int k, char letter, int repetition) {
        int n = s.Length;
        int[] suffixTarget = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            suffixTarget[i] = suffixTarget[i + 1] + (s[i] == letter ? 1 : 0);
        }

        var stack = new System.Collections.Generic.List<char>(k);
        int cntLetterInStack = 0;

        for (int i = 0; i < n; i++) {
            char c = s[i];

            while (stack.Count > 0 && stack[stack.Count - 1] > c) {
                // Check if we can pop this character
                int sz = stack.Count;
                // Length feasibility after popping
                if ((sz - 1) + (n - i) < k) break;

                // Repetition feasibility after popping
                int cntAfterPop = cntLetterInStack - (stack[sz - 1] == letter ? 1 : 0);
                if (cntAfterPop + suffixTarget[i] < repetition) break;

                // Perform pop
                char popped = stack[sz - 1];
                if (popped == letter) cntLetterInStack--;
                stack.RemoveAt(sz - 1);
            }

            if (stack.Count < k) {
                int newCnt = cntLetterInStack + (c == letter ? 1 : 0);
                int needSlots = k - (stack.Count + 1);
                // Ensure we can still satisfy repetition and length constraints
                if (newCnt + suffixTarget[i + 1] >= repetition && needSlots <= n - i - 1) {
                    stack.Add(c);
                    cntLetterInStack = newCnt;
                }
            }
        }

        // In case of any excess (should not happen), trim to k
        while (stack.Count > k) {
            if (stack[stack.Count - 1] == letter && cntLetterInStack > repetition) cntLetterInStack--;
            stack.RemoveAt(stack.Count - 1);
        }

        return new string(stack.ToArray());
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @param {character} letter
 * @param {number} repetition
 * @return {string}
 */
var smallestSubsequence = function(s, k, letter, repetition) {
    const n = s.length;
    // suffix count of required letter
    const suff = new Array(n + 1);
    suff[n] = 0;
    for (let i = n - 1; i >= 0; --i) {
        suff[i] = suff[i + 1] + (s[i] === letter ? 1 : 0);
    }

    const stack = [];
    let cntLetter = 0; // number of 'letter' in current stack

    for (let i = 0; i < n; ++i) {
        const c = s[i];

        // Try to pop larger characters while keeping feasibility
        while (stack.length > 0 && stack[stack.length - 1] > c) {
            const top = stack[stack.length - 1];
            // length feasibility after popping
            if (stack.length - 1 + (n - i) < k) break;
            // letter count feasibility after popping a required letter
            if (top === letter) {
                const needAfterPop = repetition - (cntLetter - 1);
                if (needAfterPop > suff[i]) break; // not enough letters left
            }
            stack.pop();
            if (top === letter) cntLetter--;
        }

        // Decide whether to push current character
        if (stack.length < k) {
            const needLetter = repetition - cntLetter;
            const futureLetters = suff[i + 1];
            if (c === letter) {
                stack.push(c);
                cntLetter++;
            } else {
                if (needLetter <= futureLetters) {
                    stack.push(c);
                }
            }
        }
    }

    return stack.join('');
};
```

## Typescript

```typescript
function smallestSubsequence(s: string, k: number, letter: string, repetition: number): string {
    const n = s.length;
    const suffix = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; --i) {
        suffix[i] = suffix[i + 1] + (s.charAt(i) === letter ? 1 : 0);
    }

    const stack: string[] = [];
    let cntLetter = 0;

    for (let i = 0; i < n; ++i) {
        const c = s.charAt(i);

        while (
            stack.length > 0 &&
            stack[stack.length - 1] > c
        ) {
            const afterPopLen = stack.length - 1;
            const remainingChars = n - i; // includes current character
            if (afterPopLen + remainingChars < k) break;

            const topChar = stack[stack.length - 1];
            const newLetterCount = cntLetter - (topChar === letter ? 1 : 0);
            if (newLetterCount + suffix[i] < repetition) break;

            const popped = stack.pop()!;
            if (popped === letter) cntLetter--;
        }

        if (stack.length < k) {
            const newLetterCount = cntLetter + (c === letter ? 1 : 0);
            const neededAfterPush = repetition - newLetterCount;
            const remainingTargetAfter = suffix[i + 1];
            if (neededAfterPush <= remainingTargetAfter) {
                stack.push(c);
                if (c === letter) cntLetter++;
            }
        }
    }

    return stack.slice(0, k).join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @param String $letter
     * @param Integer $repetition
     * @return String
     */
    function smallestSubsequence($s, $k, $letter, $repetition) {
        $n = strlen($s);
        // suffix count of required letter
        $suffix = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; --$i) {
            $suffix[$i] = $suffix[$i + 1] + ($s[$i] === $letter ? 1 : 0);
        }

        $stack = [];
        $stackSize = 0;
        $cntLetterInStack = 0;

        for ($i = 0; $i < $n; ++$i) {
            $c = $s[$i];

            // Try to pop larger characters while keeping feasibility
            while ($stackSize > 0) {
                $top = $stack[$stackSize - 1];
                if ($top <= $c) {
                    break;
                }
                $newSize = $stackSize - 1;
                $remainingChars = $n - $i; // includes current character
                if ($newSize + $remainingChars < $k) {
                    break;
                }
                $cntAfterPop = $cntLetterInStack - ($top === $letter ? 1 : 0);
                if ($cntAfterPop + $suffix[$i] < $repetition) {
                    break;
                }
                // pop
                array_pop($stack);
                $stackSize--;
                if ($top === $letter) {
                    $cntLetterInStack--;
                }
            }

            // Decide whether to push current character
            if ($stackSize < $k) {
                $cntAfterPush = $cntLetterInStack + ($c === $letter ? 1 : 0);
                $slotsLeft = $k - ($stackSize + 1);          // slots remaining after this push
                $lettersRemaining = $suffix[$i + 1];         // required letters still available later
                $remainingCharsAfter = $n - $i - 1;           // characters left after current

                if (
                    $cntAfterPush + $lettersRemaining >= $repetition &&          // enough letters overall
                    ($repetition - $cntAfterPush) <= $slotsLeft &&               // needed letters fit in remaining slots
                    $remainingCharsAfter >= $slotsLeft                           // enough total chars left
                ) {
                    $stack[] = $c;
                    $stackSize++;
                    if ($c === $letter) {
                        $cntLetterInStack++;
                    }
                }
            }
        }

        return implode('', $stack);
    }
}
```

## Swift

```swift
class Solution {
    func smallestSubsequence(_ s: String, _ k: Int, _ letter: Character, _ repetition: Int) -> String {
        let bytes = Array(s.utf8)
        let n = bytes.count
        guard let targetByte = letter.asciiValue else { return "" }
        
        var totalLetterCount = 0
        for b in bytes where b == targetByte {
            totalLetterCount += 1
        }
        
        var stack = [UInt8]()
        var cntLetterInStack = 0
        var seenLetter = 0
        
        for i in 0..<n {
            let c = bytes[i]
            let remaining = n - i - 1   // characters after current
            
            while let last = stack.last, last > c {
                // check if we can still reach length k after popping
                if (stack.count - 1 + remaining + 1) < k { break }
                
                // if the popped char is the required letter, ensure enough letters remain later
                if last == targetByte {
                    let futureLetterCount = totalLetterCount - seenLetter
                    if (cntLetterInStack - 1 + futureLetterCount) < repetition { break }
                }
                
                stack.removeLast()
                if last == targetByte { cntLetterInStack -= 1 }
            }
            
            // decide to push current character
            if stack.count < k {
                if c == targetByte {
                    stack.append(c)
                    cntLetterInStack += 1
                } else {
                    let need = repetition - cntLetterInStack   // still needed letters
                    // after pushing this non‑letter, ensure enough slots remain for required letters
                    if (k - (stack.count + 1)) >= need {
                        stack.append(c)
                    }
                }
            }
            
            if c == targetByte { seenLetter += 1 }
        }
        
        return String(bytes: stack, encoding: .utf8) ?? ""
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun smallestSubsequence(s: String, k: Int, letter: Char, repetition: Int): String {
        val n = s.length
        val suffix = IntArray(n + 1)
        for (i in n - 1 downTo 0) {
            suffix[i] = suffix[i + 1] + if (s[i] == letter) 1 else 0
        }

        val stack = ArrayDeque<Char>()
        var cntLetterInStack = 0

        for (i in 0 until n) {
            val c = s[i]

            // Try to pop larger characters while keeping feasibility
            while (!stack.isEmpty()) {
                val top = stack.peekLast()
                if (top <= c) break

                // length feasibility after popping
                if (stack.size - 1 + (n - i) < k) break

                // letter count feasibility after popping
                if (top == letter && cntLetterInStack - 1 + suffix[i] < repetition) break

                stack.pollLast()
                if (top == letter) cntLetterInStack--
            }

            // Decide whether to push current character
            if (stack.size < k) {
                val needAfterPush = repetition - (cntLetterInStack + if (c == letter) 1 else 0)
                if (needAfterPush <= suffix[i + 1]) {
                    stack.addLast(c)
                    if (c == letter) cntLetterInStack++
                }
            }
        }

        // Build result string
        val sb = StringBuilder()
        for (ch in stack) sb.append(ch)
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String smallestSubsequence(String s, int k, String letter, int repetition) {
    final n = s.length;
    final target = letter.codeUnitAt(0);
    final codes = s.codeUnits;
    final suffix = List<int>.filled(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
      suffix[i] = suffix[i + 1] + (codes[i] == target ? 1 : 0);
    }

    final List<int> stack = [];
    int cntLetterInStack = 0;

    for (int i = 0; i < n; ++i) {
      final c = codes[i];
      while (stack.isNotEmpty && stack.last > c) {
        // Can we pop?
        final newLen = stack.length - 1;
        final remainingChars = n - i; // includes current character
        if (newLen + remainingChars < k) break;

        final top = stack.last;
        int cntAfterPop = cntLetterInStack - ((top == target) ? 1 : 0);
        int needLetters = repetition - cntAfterPop;
        if (needLetters < 0) needLetters = 0;
        if (needLetters > suffix[i]) break;

        // pop
        stack.removeLast();
        if (top == target) cntLetterInStack--;
      }

      if (stack.length < k) {
        int cntIfPush = cntLetterInStack + ((c == target) ? 1 : 0);
        int needAfterPush = repetition - cntIfPush;
        if (needAfterPush < 0) needAfterPush = 0;
        int remLettersAfter = suffix[i + 1];
        if (needAfterPush <= remLettersAfter) {
          stack.add(c);
          if (c == target) cntLetterInStack++;
        }
      }
    }

    if (stack.length > k) {
      stack.removeRange(k, stack.length);
    }
    return String.fromCharCodes(stack);
  }
}
```

## Golang

```go
func smallestSubsequence(s string, k int, letter byte, repetition int) string {
	n := len(s)
	// suffix[i] = number of occurrences of 'letter' in s[i:]
	suffix := make([]int, n+1)
	for i := n - 1; i >= 0; i-- {
		suffix[i] = suffix[i+1]
		if s[i] == letter {
			suffix[i]++
		}
	}

	stack := make([]byte, 0, k)
	cntLetter := 0

	for i := 0; i < n; i++ {
		c := s[i]

		// Try to pop larger characters while keeping feasibility
		for len(stack) > 0 && stack[len(stack)-1] > c {
			top := stack[len(stack)-1]
			// After popping, can we still fill k positions?
			if len(stack)-1+(n-i) < k {
				break
			}
			// If the popped character is the required letter, ensure enough letters remain
			if top == letter {
				if (cntLetter-1)+suffix[i] < repetition {
					break
				}
			}
			// Pop
			stack = stack[:len(stack)-1]
			if top == letter {
				cntLetter--
			}
		}

		if len(stack) < k {
			if c == letter {
				stack = append(stack, c)
				cntLetter++
			} else {
				needRem := repetition - cntLetter
				if k-(len(stack)+1) >= needRem {
					stack = append(stack, c)
				}
			}
		}
	}

	return string(stack[:k])
}
```

## Ruby

```ruby
def smallest_subsequence(s, k, letter, repetition)
  chars = s.chars
  n = chars.length
  suff = Array.new(n + 1, 0)
  (n - 1).downto(0) do |i|
    suff[i] = suff[i + 1] + (chars[i] == letter ? 1 : 0)
  end

  stack = []
  cnt_letter = 0

  (0...n).each do |i|
    c = chars[i]

    while !stack.empty? && c < stack[-1] && (stack.size - 1 + (n - i) >= k)
      top = stack[-1]
      cnt_after_pop = cnt_letter - (top == letter ? 1 : 0)
      break if cnt_after_pop + suff[i] < repetition
      stack.pop
      cnt_letter = cnt_after_pop
    end

    if stack.size < k
      new_cnt = cnt_letter + (c == letter ? 1 : 0)
      if new_cnt + suff[i + 1] >= repetition
        stack << c
        cnt_letter = new_cnt
      end
    end
  end

  stack.join
end
```

## Scala

```scala
object Solution {
    def smallestSubsequence(s: String, k: Int, letter: Char, repetition: Int): String = {
        val n = s.length
        var totalLetter = 0
        for (ch <- s) if (ch == letter) totalLetter += 1
        var lettersRemaining = totalLetter

        val stack = new scala.collection.mutable.ArrayBuffer[Char]()
        var cntLetterInStack = 0

        for (i <- 0 until n) {
            val c = s.charAt(i)

            while (stack.nonEmpty && stack.last > c &&
                   (stack.size - 1 + (n - i) >= k) &&
                   (stack.last != letter || cntLetterInStack - 1 + lettersRemaining >= repetition)) {
                if (stack.last == letter) cntLetterInStack -= 1
                stack.remove(stack.size - 1)
            }

            if (stack.size < k) {
                val needLetter = math.max(0, repetition - cntLetterInStack)
                val needSlot = k - stack.size
                if (c == letter) {
                    stack.append(c)
                    cntLetterInStack += 1
                } else if (needSlot > needLetter) {
                    stack.append(c)
                }
            }

            if (c == letter) lettersRemaining -= 1
        }

        val sb = new StringBuilder(k)
        for (i <- 0 until k) sb.append(stack(i))
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_subsequence(s: String, k: i32, letter: char, repetition: i32) -> String {
        let chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        let mut suffix = vec![0usize; n + 1];
        for i in (0..n).rev() {
            suffix[i] = suffix[i + 1] + if chars[i] == letter { 1 } else { 0 };
        }

        let k_usize = k as usize;
        let rep_usize = repetition as usize;

        let mut stack: Vec<char> = Vec::with_capacity(k_usize);
        let mut cnt_target_in_stack: usize = 0;

        for i in 0..n {
            let c = chars[i];
            // Try to pop larger characters while we can still fulfill constraints
            while let Some(&top) = stack.last() {
                if top > c && stack.len() - 1 + (n - i) >= k_usize {
                    let new_cnt_target = cnt_target_in_stack - if top == letter { 1 } else { 0 };
                    let needed = if rep_usize > new_cnt_target {
                        rep_usize - new_cnt_target
                    } else {
                        0
                    };
                    // suffix[i] includes current character and all after it
                    if needed <= suffix[i] {
                        stack.pop();
                        cnt_target_in_stack = new_cnt_target;
                    } else {
                        break;
                    }
                } else {
                    break;
                }
            }

            // Decide whether to push current character
            if stack.len() < k_usize {
                let possible_targets =
                    cnt_target_in_stack + if c == letter { 1 } else { 0 } + suffix[i + 1];
                if possible_targets >= rep_usize {
                    stack.push(c);
                    if c == letter {
                        cnt_target_in_stack += 1;
                    }
                }
            }
        }

        // Truncate in case of any excess (should not happen)
        if stack.len() > k_usize {
            stack.truncate(k_usize);
        }

        stack.iter().collect()
    }
}
```

## Racket

```racket
(define/contract (smallest-subsequence s k letter repetition)
  (-> string? exact-integer? char? exact-integer? string?)
  (let* ((n (string-length s))
         (suff (make-vector (+ n 1) 0)))
    ;; suffix counts of `letter`
    (for ([i (in-range (sub1 n) -1 -1)])
      (vector-set! suff i
        (+ (vector-ref suff (+ i 1))
           (if (char=? (string-ref s i) letter) 1 0))))
    (define stack (make-vector n))   ; enough capacity
    (define sz 0)
    (define cntLetterInStack 0)
    (for ([i (in-range n)])
      (define c (string-ref s i))
      ;; try to pop while it improves lexicographic order and feasibility remains
      (let loop ()
        (when (and (> sz 0)
                   (> (char->integer (vector-ref stack (- sz 1))) (char->integer c)))
          (define topChar (vector-ref stack (- sz 1)))
          (define newSz (- sz 1))
          (define needSlotsAfterPop (- k newSz))
          (define remaining (- n i)) ; characters left including current `c`
          (when (and (<= needSlotsAfterPop remaining)
                     (let* ((cntIfPopped cntLetterInStack)
                            (cntIfPopped (if (char=? topChar letter) (- cntIfPopped 1) cntIfPopped))
                            (remainingLetter (+ (if (char=? c letter) 1 0)
                                                (vector-ref suff (+ i 1))))
                            (needLetterAfterPop (max 0 (- repetition cntIfPopped))))
                       (>= remainingLetter needLetterAfterPop)))
            ;; pop
            (set! sz newSz)
            (when (char=? topChar letter)
              (set! cntLetterInStack (- cntLetterInStack 1)))
            (loop)))))
      ;; push current character if we still need more characters
      (when (< sz k)
        (vector-set! stack sz c)
        (set! sz (+ sz 1))
        (when (char=? c letter)
          (set! cntLetterInStack (+ cntLetterInStack 1)))))
    ;; build result string from first `k` elements of the stack
    (let ((res (make-string k)))
      (for ([i (in-range k)])
        (string-set! res i (vector-ref stack i)))
      res)))
```

## Erlang

```erlang
-module(solution).
-export([smallest_subsequence/4]).

-spec smallest_subsequence(S :: unicode:unicode_binary(), K :: integer(), Letter :: char(), Repetition :: integer()) -> unicode:unicode_binary().
smallest_subsequence(S, K, Letter, Repetition) ->
    CharList = binary_to_list(S),
    N = length(CharList),
    TotalLetter = count_letter(CharList, Letter, 0),
    FinalStack = process(CharList, 0, [], 0, 0, TotalLetter, K, Repetition, Letter, N),
    list_to_binary(lists:reverse(FinalStack)).

count_letter([], _Letter, Acc) -> Acc;
count_letter([C|Rest], Letter, Acc) ->
    NewAcc = if C == Letter -> Acc + 1; true -> Acc end,
    count_letter(Rest, Letter, NewAcc).

process([], _Pos, Stack, _Len, _Lcnt, _RemLetter, _K, _Repetition, _Letter, _N) ->
    Stack;
process([C|Rest], Pos, Stack, Len, Lcnt, RemLetter0, K, Repetition, Letter, N) ->
    % remaining count of 'letter' after current character
    RemLetter = if C == Letter -> RemLetter0 - 1; true -> RemLetter0 end,
    RemPos = N - Pos - 1,
    {Stack2, Len2, Lcnt2} = pop_while(Stack, Len, Lcnt, C, RemPos, RemLetter, K, Repetition, Letter),
    % decide whether to push current character
    case Len2 < K of
        true ->
            if C == Letter ->
                    NewStack = [C|Stack2],
                    NewLen = Len2 + 1,
                    NewLcnt = Lcnt2 + 1;
               true ->
                    %% can we afford a non‑letter here?
                    if (K - Len2) > (Repetition - Lcnt2) ->
                            NewStack = [C|Stack2],
                            NewLen = Len2 + 1,
                            NewLcnt = Lcnt2;
                       true ->
                            NewStack = Stack2,
                            NewLen = Len2,
                            NewLcnt = Lcnt2
                    end
            end;
        false ->
            NewStack = Stack2,
            NewLen = Len2,
            NewLcnt = Lcnt2
    end,
    process(Rest, Pos + 1, NewStack, NewLen, NewLcnt, RemLetter, K, Repetition, Letter, N).

pop_while(Stack, Len, Lcnt, C, RemPos, RemLetter, K, Repetition, Letter) ->
    case Stack of
        [] -> {Stack, Len, Lcnt};
        [Top|Rest] when Top > C,
                        (Len - 1 + (RemPos + 1) >= K),
                        (Lcnt - (if Top == Letter -> 1 else 0 end)
                         + (if C == Letter -> 1 else 0 end)
                         + RemLetter >= Repetition) ->
            NewLcnt = Lcnt - (if Top == Letter -> 1 else 0 end),
            pop_while(Rest, Len - 1, NewLcnt, C, RemPos, RemLetter, K, Repetition, Letter);
        _ -> {Stack, Len, Lcnt}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_subsequence(String.t(), integer, char, integer) :: String.t()
  def smallest_subsequence(s, k, letter, repetition) do
    target = if is_integer(letter), do: <<letter>>, else: letter

    chars = String.codepoints(s)
    n = length(chars)

    total_letter = Enum.count(chars, fn x -> x == target end)

    {stack, _stack_len, _letters_in_stack, _letters_seen} =
      Enum.with_index(chars)
      |> Enum.reduce({[], 0, 0, 0}, fn {c, i},
            {stk, slen, lins, lseen} ->
        # pop while possible
        {stk, slen, lins} =
          try_pop(stk, slen, lins, c, i, n, total_letter,
                  lseen, k, target, repetition)

        # decide to push current character
        {new_stk, new_slen, new_lins} =
          if slen < k do
            cond do
              c == target ->
                {[c | stk], slen + 1, lins + 1}

              true ->
                needed = repetition - lins

                if (k - (slen + 1)) >= needed do
                  {[c | stk], slen + 1, lins}
                else
                  {stk, slen, lins}
                end
            end
          else
            {stk, slen, lins}
          end

        new_lseen = if c == target, do: lseen + 1, else: lseen
        {new_stk, new_slen, new_lins, new_lsee n} = {new_stk, new_slen, new_lins, new_lseen}
      end)

    stack |> Enum.reverse() |> Enum.join()
  end

  defp try_pop(stack, slen, lins, c, i, n, total_letter,
               letters_seen, k, target, repetition) do
    case stack do
      [] ->
        {stack, slen, lins}

      [top | rest] ->
        if top > c and (slen - 1 + (n - i)) >= k do
          new_lins = lins - (if top == target, do: 1, else: 0)
          remaining_letter = total_letter - letters_seen

          if new_lins + remaining_letter >= repetition do
            try_pop(rest, slen - 1, new_lins, c, i, n,
                    total_letter, letters_seen, k, target, repetition)
          else
            {stack, slen, lins}
          end
        else
          {stack, slen, lins}
        end
    end
  end
end
```
