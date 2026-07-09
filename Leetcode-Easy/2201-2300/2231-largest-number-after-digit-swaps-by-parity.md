# 2231. Largest Number After Digit Swaps by Parity

## Cpp

```cpp
class Solution {
public:
    int largestInteger(int num) {
        string s = to_string(num);
        vector<char> evenDigits, oddDigits;
        for (char c : s) {
            if ((c - '0') % 2 == 0)
                evenDigits.push_back(c);
            else
                oddDigits.push_back(c);
        }
        sort(evenDigits.begin(), evenDigits.end(), greater<char>());
        sort(oddDigits.begin(), oddDigits.end(), greater<char>());
        int ei = 0, oi = 0;
        string res;
        res.reserve(s.size());
        for (char c : s) {
            if ((c - '0') % 2 == 0)
                res.push_back(evenDigits[ei++]);
            else
                res.push_back(oddDigits[oi++]);
        }
        return stoi(res);
    }
};
```

## Java

```java
class Solution {
    public int largestInteger(int num) {
        String s = Integer.toString(num);
        int[] oddCount = new int[10];
        int[] evenCount = new int[10];
        for (int i = 0; i < s.length(); i++) {
            int d = s.charAt(i) - '0';
            if ((d & 1) == 0) {
                evenCount[d]++;
            } else {
                oddCount[d]++;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            int curDigit = s.charAt(i) - '0';
            if ((curDigit & 1) == 0) { // even position
                for (int d = 9; d >= 0; d--) {
                    if ((d & 1) == 0 && evenCount[d] > 0) {
                        sb.append(d);
                        evenCount[d]--;
                        break;
                    }
                }
            } else { // odd position
                for (int d = 9; d >= 0; d--) {
                    if ((d & 1) == 1 && oddCount[d] > 0) {
                        sb.append(d);
                        oddCount[d]--;
                        break;
                    }
                }
            }
        }
        return Integer.parseInt(sb.toString());
    }
}
```

## Python

```python
class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num))
        odds, evens = [], []
        for ch in digits:
            d = ord(ch) - 48
            if d % 2:
                odds.append(d)
            else:
                evens.append(d)
        odds.sort(reverse=True)
        evens.sort(reverse=True)
        i_odd = i_even = 0
        result = []
        for ch in digits:
            d = ord(ch) - 48
            if d % 2:
                result.append(str(odds[i_odd]))
                i_odd += 1
            else:
                result.append(str(evens[i_even]))
                i_even += 1
        return int(''.join(result))
```

## Python3

```python
class Solution:
    def largestInteger(self, num: int) -> int:
        s = list(str(num))
        evens = sorted([int(ch) for ch in s if int(ch) % 2 == 0], reverse=True)
        odds = sorted([int(ch) for ch in s if int(ch) % 2 == 1], reverse=True)
        ei = oi = 0
        res = []
        for ch in s:
            d = int(ch)
            if d % 2 == 0:
                res.append(str(evens[ei]))
                ei += 1
            else:
                res.append(str(odds[oi]))
                oi += 1
        return int(''.join(res))
```

## C

```c
#include <string.h>
#include <stdlib.h>

static int cmp_desc(const void *a, const void *b) {
    return *(const int *)b - *(const int *)a;
}

int largestInteger(int num) {
    char s[12];
    sprintf(s, "%d", num);
    int n = strlen(s);
    int even[10], odd[10];
    int eCnt = 0, oCnt = 0;

    for (int i = 0; i < n; ++i) {
        int d = s[i] - '0';
        if (d % 2 == 0)
            even[eCnt++] = d;
        else
            odd[oCnt++] = d;
    }

    qsort(even, eCnt, sizeof(int), cmp_desc);
    qsort(odd, oCnt, sizeof(int), cmp_desc);

    int eIdx = 0, oIdx = 0;
    long long res = 0;

    for (int i = 0; i < n; ++i) {
        int d = s[i] - '0';
        int nd = (d % 2 == 0) ? even[eIdx++] : odd[oIdx++];
        res = res * 10 + nd;
    }

    return (int)res;
}
```

## Csharp

```csharp
public class Solution {
    public int LargestInteger(int num) {
        string s = num.ToString();
        var evens = new List<char>();
        var odds = new List<char>();
        foreach (char c in s) {
            if (((c - '0') % 2) == 0)
                evens.Add(c);
            else
                odds.Add(c);
        }
        evens.Sort((a, b) => b.CompareTo(a));
        odds.Sort((a, b) => b.CompareTo(a));
        int eIdx = 0, oIdx = 0;
        var sb = new System.Text.StringBuilder();
        foreach (char c in s) {
            if (((c - '0') % 2) == 0)
                sb.Append(evens[eIdx++]);
            else
                sb.Append(odds[oIdx++]);
        }
        return int.Parse(sb.ToString());
    }
}
```

## Javascript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var largestInteger = function(num) {
    const digits = String(num).split('').map(Number);
    const evens = [];
    const odds = [];
    
    for (const d of digits) {
        if (d % 2 === 0) evens.push(d);
        else odds.push(d);
    }
    
    evens.sort((a, b) => b - a);
    odds.sort((a, b) => b - a);
    
    let eIdx = 0, oIdx = 0;
    const result = digits.map(d => {
        if (d % 2 === 0) return evens[eIdx++];
        else return odds[oIdx++];
    }).join('');
    
    return Number(result);
};
```

## Typescript

```typescript
function largestInteger(num: number): number {
    const digits = Array.from(String(num));
    const odds: string[] = [];
    const evens: string[] = [];

    for (const d of digits) {
        if ((Number(d) & 1) === 1) {
            odds.push(d);
        } else {
            evens.push(d);
        }
    }

    odds.sort((a, b) => Number(b) - Number(a));
    evens.sort((a, b) => Number(b) - Number(a));

    let oddIdx = 0;
    let evenIdx = 0;

    const result = digits.map(d => {
        if ((Number(d) & 1) === 1) {
            return odds[oddIdx++];
        } else {
            return evens[evenIdx++];
        }
    }).join('');

    return Number(result);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function largestInteger($num) {
        $digits = str_split((string)$num);
        $evens = [];
        $odds = [];

        foreach ($digits as $d) {
            $digit = intval($d);
            if (($digit & 1) === 0) {
                $evens[] = $digit;
            } else {
                $odds[] = $digit;
            }
        }

        rsort($evens);
        rsort($odds);

        $eIdx = 0;
        $oIdx = 0;

        foreach ($digits as &$d) {
            $digit = intval($d);
            if (($digit & 1) === 0) {
                $d = (string)$evens[$eIdx++];
            } else {
                $d = (string)$odds[$oIdx++];
            }
        }

        return intval(implode('', $digits));
    }
}
```

## Swift

```swift
class Solution {
    func largestInteger(_ num: Int) -> Int {
        var chars = Array(String(num))
        var evens: [Character] = []
        var odds: [Character] = []
        
        for ch in chars {
            if let val = ch.wholeNumberValue {
                if val % 2 == 0 {
                    evens.append(ch)
                } else {
                    odds.append(ch)
                }
            }
        }
        
        evens.sort { ($0.wholeNumberValue ?? 0) > ($1.wholeNumberValue ?? 0) }
        odds.sort { ($0.wholeNumberValue ?? 0) > ($1.wholeNumberValue ?? 0) }
        
        var eIdx = 0
        var oIdx = 0
        
        for i in 0..<chars.count {
            if let val = chars[i].wholeNumberValue {
                if val % 2 == 0 {
                    chars[i] = evens[eIdx]
                    eIdx += 1
                } else {
                    chars[i] = odds[oIdx]
                    oIdx += 1
                }
            }
        }
        
        return Int(String(chars))!
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestInteger(num: Int): Int {
        val digits = num.toString().toCharArray()
        val evens = mutableListOf<Char>()
        val odds = mutableListOf<Char>()
        for (c in digits) {
            if ((c - '0') % 2 == 0) evens.add(c) else odds.add(c)
        }
        evens.sortDescending()
        odds.sortDescending()
        var eIdx = 0
        var oIdx = 0
        val sb = StringBuilder()
        for (c in digits) {
            if ((c - '0') % 2 == 0) {
                sb.append(evens[eIdx++])
            } else {
                sb.append(odds[oIdx++])
            }
        }
        return sb.toString().toInt()
    }
}
```

## Dart

```dart
class Solution {
  int largestInteger(int num) {
    String s = num.toString();
    List<int> evens = [];
    List<int> odds = [];

    for (int i = 0; i < s.length; i++) {
      int d = int.parse(s[i]);
      if (d % 2 == 0) {
        evens.add(d);
      } else {
        odds.add(d);
      }
    }

    evens.sort((a, b) => b - a);
    odds.sort((a, b) => b - a);

    int evenIdx = 0;
    int oddIdx = 0;
    StringBuffer sb = StringBuffer();

    for (int i = 0; i < s.length; i++) {
      int d = int.parse(s[i]);
      if (d % 2 == 0) {
        sb.write(evens[evenIdx++]);
      } else {
        sb.write(odds[oddIdx++]);
      }
    }

    return int.parse(sb.toString());
  }
}
```

## Golang

```go
package main

import "sort"

func largestInteger(num int) int {
	if num == 0 {
		return 0
	}
	var digits []int
	n := num
	for n > 0 {
		digits = append(digits, n%10)
		n /= 10
	}
	for i, j := 0, len(digits)-1; i < j; i, j = i+1, j-1 {
		digits[i], digits[j] = digits[j], digits[i]
	}

	var evens []int
	var odds []int
	for _, d := range digits {
		if d%2 == 0 {
			evens = append(evens, d)
		} else {
			odds = append(odds, d)
		}
	}
	sort.Slice(evens, func(i, j int) bool { return evens[i] > evens[j] })
	sort.Slice(odds, func(i, j int) bool { return odds[i] > odds[j] })

	eIdx, oIdx := 0, 0
	result := 0
	for _, d := range digits {
		var nd int
		if d%2 == 0 {
			nd = evens[eIdx]
			eIdx++
		} else {
			nd = odds[oIdx]
			oIdx++
		}
		result = result*10 + nd
	}
	return result
}
```

## Ruby

```ruby
def largest_integer(num)
  chars = num.to_s.chars
  odds = []
  evens = []

  chars.each do |c|
    d = c.ord - 48
    if d.even?
      evens << d
    else
      odds << d
    end
  end

  odds.sort!.reverse!
  evens.sort!.reverse!

  odd_idx = 0
  even_idx = 0

  result = chars.map do |c|
    d = c.ord - 48
    if d.even?
      val = evens[even_idx]
      even_idx += 1
      (val + 48).chr
    else
      val = odds[odd_idx]
      odd_idx += 1
      (val + 48).chr
    end
  end

  result.join.to_i
end
```

## Scala

```scala
object Solution {
    def largestInteger(num: Int): Int = {
        val chars = num.toString.toCharArray
        val evens = scala.collection.mutable.ArrayBuffer[Int]()
        val odds = scala.collection.mutable.ArrayBuffer[Int]()

        for (c <- chars) {
            val d = c - '0'
            if ((d & 1) == 0) evens += d else odds += d
        }

        val sortedEvens = evens.sorted(Ordering[Int].reverse)
        val sortedOdds = odds.sorted(Ordering[Int].reverse)

        var eIdx = 0
        var oIdx = 0
        val sb = new StringBuilder

        for (c <- chars) {
            val d = c - '0'
            if ((d & 1) == 0) {
                sb.append(sortedEvens(eIdx))
                eIdx += 1
            } else {
                sb.append(sortedOdds(oIdx))
                oIdx += 1
            }
        }

        sb.toString().toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_integer(num: i32) -> i32 {
        let s = num.to_string();
        let mut digits: Vec<u8> = s.bytes().map(|b| b - b'0').collect();

        let mut evens: Vec<u8> = digits.iter().cloned().filter(|d| d % 2 == 0).collect();
        let mut odds: Vec<u8> = digits.iter().cloned().filter(|d| d % 2 != 0).collect();

        evens.sort_unstable_by(|a, b| b.cmp(a));
        odds.sort_unstable_by(|a, b| b.cmp(a));

        let mut even_idx = 0usize;
        let mut odd_idx = 0usize;
        let mut result: i64 = 0;

        for d in digits.iter() {
            let nd = if d % 2 == 0 {
                let v = evens[even_idx];
                even_idx += 1;
                v
            } else {
                let v = odds[odd_idx];
                odd_idx += 1;
                v
            };
            result = result * 10 + nd as i64;
        }

        result as i32
    }
}
```

## Racket

```racket
(define/contract (largest-integer num)
  (-> exact-integer? exact-integer?)
  (let* ((digits (map (lambda (c) (- (char->integer c) 48))
                      (string->list (number->string num))))
         (evens (filter even? digits))
         (odds (filter odd? digits))
         (sorted-evens (sort evens >))
         (sorted-odds (sort odds >)))
    (let loop ((ds digits) (e sorted-evens) (o sorted-odds) (acc '()))
      (if (null? ds)
          (foldl (lambda (d a) (+ (* a 10) d)) 0 (reverse acc))
          (let* ((d (car ds))
                 (parity (modulo d 2))
                 (new-digit (if (= parity 0) (car e) (car o)))
                 (e' (if (= parity 0) (cdr e) e))
                 (o' (if (= parity 1) (cdr o) o)))
            (loop (cdr ds) e' o' (cons new-digit acc)))))))
```

## Erlang

```erlang
-spec largest_integer(Num :: integer()) -> integer().
largest_integer(Num) ->
    DigitsChars = integer_to_list(Num),
    Digits = [C - $0 || C <- DigitsChars],
    Odds = [D || D <- Digits, D rem 2 =:= 1],
    Evens = [D || D <- Digits, D rem 2 =:= 0],
    SortedOdds = lists:sort(fun(A,B) -> A > B end, Odds),
    SortedEvens = lists:sort(fun(A,B) -> A > B end, Evens),
    NewDigits = build(Digits, SortedOdds, SortedEvens),
    lists:foldl(fun(Acc,D) -> Acc*10 + D end, 0, NewDigits).

build([], _, _) ->
    [];
build([D|Rest], OddsSorted, EvensSorted) ->
    case D rem 2 of
        1 ->
            [H|T] = OddsSorted,
            [H | build(Rest, T, EvensSorted)];
        0 ->
            [H|T] = EvensSorted,
            [H | build(Rest, OddsSorted, T)]
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_integer(num :: integer) :: integer
  def largest_integer(num) do
    digits = Integer.digits(num)

    evens = digits |> Enum.filter(&rem(&1, 2) == 0) |> Enum.sort(&>=/2)
    odds = digits |> Enum.filter(&rem(&1, 2) == 1) |> Enum.sort(&>=/2)

    final_digits = build(digits, evens, odds)

    Enum.reduce(final_digits, 0, fn d, acc -> acc * 10 + d end)
  end

  defp build([], _evens, _odds), do: []
  defp build([d | rest], evens, odds) do
    if rem(d, 2) == 0 do
      [h | t] = evens
      [h | build(rest, t, odds)]
    else
      [h | t] = odds
      [h | build(rest, evens, t)]
    end
  end
end
```
