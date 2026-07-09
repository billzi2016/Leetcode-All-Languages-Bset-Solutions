# 0842. Split Array into Fibonacci Sequence

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> splitIntoFibonacci(string num) {
        int n = num.size();
        const long long INT_MAX_VAL = INT_MAX;
        for (int i = 1; i <= min(10, n - 2); ++i) { // first number length
            if (num[0] == '0' && i > 1) break; // leading zero not allowed
            long long first = stoll(num.substr(0, i));
            if (first > INT_MAX_VAL) break;
            for (int j = i + 1; j <= min(i + 10, n - 1); ++j) { // second number length
                if (num[i] == '0' && j - i > 1) break; // leading zero not allowed
                long long second = stoll(num.substr(i, j - i));
                if (second > INT_MAX_VAL) break;
                
                vector<int> seq;
                seq.push_back((int)first);
                seq.push_back((int)second);
                
                int k = j;
                while (k < n) {
                    long long sum = (long long)seq[seq.size() - 1] + seq[seq.size() - 2];
                    if (sum > INT_MAX_VAL) break;
                    string sumStr = to_string(sum);
                    if (k + (int)sumStr.size() > n) break;
                    if (num.compare(k, sumStr.size(), sumStr) != 0) break;
                    seq.push_back((int)sum);
                    k += sumStr.size();
                }
                
                if (k == n && seq.size() >= 3) return seq;
            }
        }
        return {};
    }
};
```

## Java

```java
class Solution {
    public List<Integer> splitIntoFibonacci(String num) {
        int n = num.length();
        for (int i = 1; i <= Math.min(10, n - 2); i++) {
            // first number cannot have leading zeros
            if (num.charAt(0) == '0' && i > 1) break;
            long first = Long.parseLong(num.substring(0, i));
            if (first > Integer.MAX_VALUE) break;

            for (int j = i + 1; j <= i + Math.min(10, n - i - 1); j++) {
                if (j >= n) break;
                // second number cannot have leading zeros
                if (num.charAt(i) == '0' && j - i > 1) break;
                long second = Long.parseLong(num.substring(i, j));
                if (second > Integer.MAX_VALUE) break;

                List<Integer> seq = new ArrayList<>();
                seq.add((int) first);
                seq.add((int) second);

                int start = j;
                long a = first, b = second;
                while (start < n) {
                    long sum = a + b;
                    if (sum > Integer.MAX_VALUE) break;
                    String sumStr = Long.toString(sum);
                    if (!num.startsWith(sumStr, start)) break;
                    seq.add((int) sum);
                    start += sumStr.length();
                    a = b;
                    b = sum;
                }

                if (start == n && seq.size() >= 3) {
                    return seq;
                }
            }
        }
        return new ArrayList<>();
    }
}
```

## Python

```python
class Solution(object):
    def splitIntoFibonacci(self, num):
        """
        :type num: str
        :rtype: List[int]
        """
        n = len(num)
        max_int = 2**31 - 1

        # first number length i
        for i in range(1, min(10, n) + 1):  # at most 10 digits for 32-bit int
            if num[0] == '0' and i > 1:
                break
            first = int(num[:i])
            if first > max_int:
                break

            # second number length j-i
            for j in range(i + 1, min(i + 10, n) + 1):
                if num[i] == '0' and j - i > 1:
                    break
                second = int(num[i:j])
                if second > max_int:
                    break

                seq = [first, second]
                idx = j
                while idx < n:
                    nxt = seq[-1] + seq[-2]
                    if nxt > max_int:
                        break
                    nxt_str = str(nxt)
                    if not num.startswith(nxt_str, idx):
                        break
                    idx += len(nxt_str)
                    seq.append(nxt)

                if idx == n and len(seq) >= 3:
                    return seq

        return []
```

## Python3

```python
from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)
        MAX_INT = 2**31 - 1
        # first number length i
        for i in range(1, min(10, n - 1) + 1):
            if num[0] == '0' and i > 1:
                break
            first = int(num[:i])
            if first > MAX_INT:
                break
            # second number length j-i
            for j in range(i + 1, min(i + 10, n) + 1):
                if num[i] == '0' and j - i > 1:
                    break
                second = int(num[i:j])
                if second > MAX_INT:
                    break
                seq = [first, second]
                k = j
                while k < n:
                    nxt = seq[-1] + seq[-2]
                    if nxt > MAX_INT:
                        break
                    s = str(nxt)
                    if not num.startswith(s, k):
                        break
                    k += len(s)
                    seq.append(nxt)
                if k == n and len(seq) >= 3:
                    return seq
        return []
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int getNumber(const char *s, int start, int end, long long *out) {
    if (end - start > 1 && s[start] == '0') return 0;
    long long val = 0;
    for (int i = start; i < end; ++i) {
        val = val * 10 + (s[i] - '0');
        if (val > INT_MAX) return 0;
    }
    *out = val;
    return 1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* splitIntoFibonacci(char* num, int* returnSize) {
    int n = strlen(num);
    *returnSize = 0;
    if (n < 3) return NULL;

    int tmp[200]; // maximum possible length
    for (int i = 1; i <= n - 2; ++i) {               // first number length
        long long first;
        if (!getNumber(num, 0, i, &first)) break;   // leading zero or overflow

        for (int j = i + 1; j <= n - 1; ++j) {       // second number length
            long long second;
            if (!getNumber(num, i, j, &second)) break;

            int len = 0;
            tmp[len++] = (int)first;
            tmp[len++] = (int)second;

            int idx = j;
            long long a = first, b = second;
            while (idx < n) {
                long long c = a + b;
                if (c > INT_MAX) break;
                char buf[12];
                int l = sprintf(buf, "%lld", c);
                if (idx + l > n) break;
                if (strncmp(num + idx, buf, l) != 0) break;
                tmp[len++] = (int)c;
                idx += l;
                a = b;
                b = c;
            }
            if (idx == n) {
                int *res = (int *)malloc(len * sizeof(int));
                for (int k = 0; k < len; ++k) res[k] = tmp[k];
                *returnSize = len;
                return res;
            }
        }
    }
    return NULL;
}
```

## Csharp

```csharp
public class Solution
{
    private const long INT_MAX = int.MaxValue;

    public IList<int> SplitIntoFibonacci(string num)
    {
        int n = num.Length;
        var result = new List<int>();

        for (int i = 1; i <= Math.Min(10, n - 2); i++)
        {
            if (num[0] == '0' && i > 1) break;
            long first = Parse(num, 0, i);
            if (first > INT_MAX) break;

            for (int j = 1; j <= Math.Min(10, n - i - 1); j++)
            {
                if (num[i] == '0' && j > 1) break;
                long second = Parse(num, i, j);
                if (second > INT_MAX) break;

                result.Clear();
                result.Add((int)first);
                result.Add((int)second);

                if (BuildSequence(result, i + j, num))
                    return result;
            }
        }

        return new List<int>();
    }

    private bool BuildSequence(List<int> seq, int index, string s)
    {
        int n = s.Length;
        while (index < n)
        {
            long sum = (long)seq[seq.Count - 2] + seq[seq.Count - 1];
            if (sum > INT_MAX) return false;

            string sumStr = sum.ToString();
            if (!s.StartsWith(sumStr, index)) return false;

            seq.Add((int)sum);
            index += sumStr.Length;
        }

        return seq.Count >= 3 && index == n;
    }

    private long Parse(string s, int start, int length)
    {
        long val = 0;
        for (int i = start; i < start + length; i++)
        {
            val = val * 10 + (s[i] - '0');
        }
        return val;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @return {number[]}
 */
var splitIntoFibonacci = function(num) {
    const n = num.length;
    const MAX_INT = 2 ** 31 - 1;

    // helper to check leading zero rule and parse number
    const getNumber = (s, start, end) => {
        if (end - start > 1 && s[start] === '0') return null; // leading zero
        const val = Number(s.slice(start, end));
        if (val > MAX_INT) return null;
        return val;
    };

    for (let i = 1; i <= Math.min(10, n - 2); ++i) {          // first number length
        const first = getNumber(num, 0, i);
        if (first === null) break; // leading zero case, longer lengths also invalid

        for (let j = i + 1; j <= Math.min(i + 10, n - 1); ++j) { // second number length
            const second = getNumber(num, i, j);
            if (second === null) break;

            const seq = [first, second];
            let a = first, b = second;
            let idx = j;

            while (idx < n) {
                const sum = a + b;
                if (sum > MAX_INT) break;
                const sumStr = String(sum);
                if (!num.startsWith(sumStr, idx)) break;
                seq.push(sum);
                idx += sumStr.length;
                a = b;
                b = sum;
            }

            if (idx === n && seq.length >= 3) {
                return seq;
            }
        }
    }
    return [];
};
```

## Typescript

```typescript
function splitIntoFibonacci(num: string): number[] {
    const MAX_INT = 2 ** 31 - 1;
    const n = num.length;

    // first number length
    for (let i = 1; i <= Math.min(10, n - 2); i++) {
        if (num[0] === '0' && i > 1) break; // leading zero not allowed
        const aStr = num.slice(0, i);
        const a = Number(aStr);
        if (a > MAX_INT) break;

        // second number length
        for (let j = i + 1; j <= Math.min(i + 10, n - 1); j++) {
            if (num[i] === '0' && j - i > 1) break;
            const bStr = num.slice(i, j);
            const b = Number(bStr);
            if (b > MAX_INT) break;

            const seq: number[] = [a, b];
            let k = j; // current index in string

            while (k < n) {
                const next = seq[seq.length - 1] + seq[seq.length - 2];
                if (next > MAX_INT) break;
                const nextStr = String(next);
                if (!num.startsWith(nextStr, k)) break;
                seq.push(next);
                k += nextStr.length;
            }

            if (k === n && seq.length >= 3) {
                return seq;
            }
        }
    }

    return [];
}
```

## Php

```php
class Solution {

    /**
     * @param String $num
     * @return Integer[]
     */
    function splitIntoFibonacci($num) {
        $len = strlen($num);
        $MAX_INT = 2147483647;

        // first number length
        for ($i = 1; $i <= min(10, $len - 2); $i++) {
            if ($num[0] === '0' && $i > 1) break; // leading zero not allowed
            $firstStr = substr($num, 0, $i);
            $first = (int)$firstStr;
            if ($first > $MAX_INT) break;

            // second number length
            for ($j = 1; $j <= min(10, $len - $i - 1); $j++) {
                if ($num[$i] === '0' && $j > 1) break;
                $secondStr = substr($num, $i, $j);
                $second = (int)$secondStr;
                if ($second > $MAX_INT) break;

                $seq = [$first, $second];
                $k = $i + $j; // current position in string

                while ($k < $len) {
                    $sum = $seq[count($seq) - 1] + $seq[count($seq) - 2];
                    if ($sum > $MAX_INT) {
                        $seq = null;
                        break;
                    }
                    $sumStr = (string)$sum;
                    $sumLen = strlen($sumStr);
                    if ($k + $sumLen > $len) {
                        $seq = null;
                        break;
                    }
                    if (substr($num, $k, $sumLen) !== $sumStr) {
                        $seq = null;
                        break;
                    }
                    $seq[] = $sum;
                    $k += $sumLen;
                }

                if ($seq !== null && $k === $len && count($seq) >= 3) {
                    return $seq;
                }
            }
        }

        return [];
    }
}
```

## Swift

```swift
class Solution {
    func splitIntoFibonacci(_ num: String) -> [Int] {
        let chars = Array(num)
        let n = chars.count
        let maxLen = 10   // because Int32.max has 10 digits
        
        for i in 1...min(maxLen, n - 2) {
            if i > 1 && chars[0] == "0" { break }
            let firstStr = String(chars[0..<i])
            guard let firstVal64 = Int64(firstStr), firstVal64 <= Int32.max else { continue }
            
            for j in 1...min(maxLen, n - i - 1) {
                if j > 1 && chars[i] == "0" { break }
                let secondStr = String(chars[i..<i + j])
                guard let secondVal64 = Int64(secondStr), secondVal64 <= Int32.max else { continue }
                
                var seq: [Int] = [Int(firstVal64), Int(secondVal64)]
                var idx = i + j
                var a = firstVal64
                var b = secondVal64
                
                while idx < n {
                    let sum = a + b
                    if sum > Int32.max { break }
                    let sumStr = String(sum)
                    if idx + sumStr.count > n { break }
                    let sub = String(chars[idx..<idx + sumStr.count])
                    if sub != sumStr { break }
                    
                    seq.append(Int(sum))
                    idx += sumStr.count
                    a = b
                    b = sum
                }
                
                if idx == n {
                    return seq
                }
            }
        }
        return []
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun splitIntoFibonacci(num: String): List<Int> {
        val n = num.length
        for (i in 1 until n) {
            // first number cannot have leading zeros unless it is zero itself
            if (num[0] == '0' && i > 1) break
            val firstVal = num.substring(0, i).toLong()
            if (firstVal > Int.MAX_VALUE) break

            for (j in i + 1 until n) {
                // second number cannot have leading zeros unless it is zero itself
                if (num[i] == '0' && j - i > 1) break
                val secondVal = num.substring(i, j).toLong()
                if (secondVal > Int.MAX_VALUE) break

                val seq = mutableListOf<Int>()
                seq.add(firstVal.toInt())
                seq.add(secondVal.toInt())

                var k = j
                var a = firstVal
                var b = secondVal
                while (k < n) {
                    val sum = a + b
                    if (sum > Int.MAX_VALUE) break
                    val sumStr = sum.toString()
                    if (!num.startsWith(sumStr, k)) break
                    seq.add(sum.toInt())
                    k += sumStr.length
                    a = b
                    b = sum
                }
                if (k == n && seq.size >= 3) {
                    return seq
                }
            }
        }
        return emptyList()
    }
}
```

## Dart

```dart
class Solution {
  List<int> splitIntoFibonacci(String num) {
    const int MAX = 2147483647;
    int n = num.length;

    int maxFirstLen = n - 2 < 10 ? n - 2 : 10;
    for (int i = 1; i <= maxFirstLen; ++i) {
      // leading zero check for first number
      if (num[0] == '0' && i > 1) break;

      int first = int.parse(num.substring(0, i));
      if (first > MAX) break;

      int remaining = n - i;
      int maxSecondLen = remaining - 1 < 10 ? remaining - 1 : 10;
      for (int j = i + 1; j <= i + maxSecondLen; ++j) {
        // leading zero check for second number
        if (num[i] == '0' && j - i > 1) break;

        int second = int.parse(num.substring(i, j));
        if (second > MAX) break;

        List<int> seq = [first, second];
        int k = j;
        while (k < n) {
          int next = seq[seq.length - 2] + seq[seq.length - 1];
          if (next > MAX) break;
          String nxtStr = next.toString();
          if (!num.startsWith(nxtStr, k)) break;
          seq.add(next);
          k += nxtStr.length;
        }

        if (k == n && seq.length >= 3) {
          return seq;
        }
      }
    }
    return [];
  }
}
```

## Golang

```go
func splitIntoFibonacci(num string) []int {
	const maxInt = 2147483647
	n := len(num)

	// try all possible first and second numbers
	for i := 1; i <= min(10, n-2); i++ {
		if num[0] == '0' && i > 1 {
			break // leading zero not allowed
		}
		firstVal, ok := strToInt(num[:i])
		if !ok || firstVal > maxInt {
			continue
		}
		for j := i + 1; j <= min(i+10, n-1); j++ {
			if num[i] == '0' && (j-i) > 1 {
				break // leading zero not allowed
			}
			secondVal, ok2 := strToInt(num[i:j])
			if !ok2 || secondVal > maxInt {
				continue
			}

			seq := []int64{firstVal, secondVal}
			idx := j

			for idx < n {
				sum := seq[len(seq)-1] + seq[len(seq)-2]
				if sum > maxInt {
					break
				}
				sumStr := strconv.FormatInt(sum, 10)
				if idx+len(sumStr) > n || num[idx:idx+len(sumStr)] != sumStr {
					break
				}
				seq = append(seq, sum)
				idx += len(sumStr)
			}

			if idx == n && len(seq) >= 3 {
				res := make([]int, len(seq))
				for k, v := range seq {
					res[k] = int(v)
				}
				return res
			}
		}
	}
	return []int{}
}

// helper: convert numeric string to int64, assumes no leading zeros unless single '0'
func strToInt(s string) (int64, bool) {
	if len(s) == 0 {
		return 0, false
	}
	val, err := strconv.ParseInt(s, 10, 64)
	if err != nil {
		return 0, false
	}
	return val, true
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
```

## Ruby

```ruby
def split_into_fibonacci(num)
  max_int = 2**31 - 1
  n = num.length
  (1..[10, n].min).each do |i|
    next if i > 1 && num[0] == '0'
    a_str = num[0, i]
    a = a_str.to_i
    next if a > max_int

    (1..[10, n - i].min).each do |j|
      next if j > 1 && num[i] == '0'
      b_str = num[i, j]
      b = b_str.to_i
      next if b > max_int

      seq = [a, b]
      pos = i + j
      while pos < n
        c = seq[-2] + seq[-1]
        break if c > max_int
        c_str = c.to_s
        break unless num[pos, c_str.length] == c_str
        seq << c
        pos += c_str.length
      end

      return seq if pos == n && seq.length >= 3
    end
  end
  []
end
```

## Scala

```scala
object Solution {
  def splitIntoFibonacci(num: String): List[Int] = {
    val n = num.length
    val maxInt = Int.MaxValue.toLong

    var i = 1
    while (i < n) {
      // first number leading zero check
      if (num(0) == '0' && i > 1) return Nil
      val firstStr = num.substring(0, i)
      val first = firstStr.toLong
      if (first > maxInt) return Nil

      var j = i + 1
      while (j < n) {
        // second number leading zero check
        if (num(i) == '0' && j - i > 1) {
          j = n // break inner loop
        } else {
          val secondStr = num.substring(i, j)
          val second = secondStr.toLong
          if (second > maxInt) {
            j = n // break inner loop
          } else {
            val seq = scala.collection.mutable.ArrayBuffer[Long]()
            seq += first
            seq += second
            var k = j
            var valid = true
            while (k < n && valid) {
              val sum = seq(seq.length - 2) + seq(seq.length - 1)
              if (sum > maxInt) {
                valid = false
              } else {
                val sumStr = sum.toString
                if (k + sumStr.length <= n && num.startsWith(sumStr, k)) {
                  seq += sum
                  k += sumStr.length
                } else {
                  valid = false
                }
              }
            }
            if (valid && k == n && seq.length >= 3) {
              return seq.map(_.toInt).toList
            }
          }
        }
        j += 1
      }

      i += 1
    }
    Nil
  }
}
```

## Rust

```rust
impl Solution {
    pub fn split_into_fibonacci(num: String) -> Vec<i32> {
        let n = num.len();
        if n < 3 {
            return vec![];
        }
        // first number length i
        for i in 1..=std::cmp::min(10, n - 2) {
            // leading zero check for first number
            if i > 1 && &num[0..1] == "0" {
                break;
            }
            let s1 = &num[0..i];
            if s1.len() > 1 && s1.starts_with('0') {
                continue;
            }
            let a: i64 = match s1.parse() {
                Ok(v) => v,
                Err(_) => continue,
            };
            if a > i32::MAX as i64 {
                continue;
            }

            // second number length j (end index)
            for j in i + 1..=std::cmp::min(i + 10, n - 1) {
                let s2 = &num[i..j];
                if s2.len() > 1 && s2.starts_with('0') {
                    continue;
                }
                let b: i64 = match s2.parse() {
                    Ok(v) => v,
                    Err(_) => continue,
                };
                if b > i32::MAX as i64 {
                    continue;
                }

                let mut seq: Vec<i32> = vec![a as i32, b as i32];
                let (mut x, mut y) = (a, b);
                let mut pos = j;

                while pos < n {
                    let sum = x + y;
                    if sum > i32::MAX as i64 {
                        break;
                    }
                    let sum_str = sum.to_string();
                    let end = pos + sum_str.len();
                    if end > n || &num[pos..end] != sum_str {
                        break;
                    }
                    seq.push(sum as i32);
                    pos = end;
                    x = y;
                    y = sum;
                }

                if pos == n {
                    return seq;
                }
            }
        }
        vec![]
    }
}
```

## Racket

```racket
(define/contract (split-into-fibonacci num)
  (-> string? (listof exact-integer?))
  (let* ((n (string-length num))
         (max-len (min 10 n)) ; 2^31‑1 has at most 10 digits
         (int-max (- (expt 2 31) 1)))
    (define (valid-number? s)
      (or (= (string-length s) 1)
          (not (char=? (string-ref s 0) #\0))))
    (let loop-i ((i 1))
      (if (> i max-len)
          '()
          (let ((s1 (substring num 0 i)))
            (if (or (not (valid-number? s1))
                    (> (string->number s1) int-max))
                (loop-i (+ i 1))
                (let loop-j ((j 1))
                  (if (> j max-len)
                      (loop-i (+ i 1))
                      (let ((end2 (+ i j)))
                        (if (>= end2 n)
                            (loop-j (+ j 1))
                            (let ((s2 (substring num i end2)))
                              (if (or (not (valid-number? s2))
                                      (> (string->number s2) int-max))
                                  (loop-j (+ j 1))
                                  (let* ((first (string->number s1))
                                         (second (string->number s2)))
                                    (define (build a b pos acc)
                                      (if (= pos n)
                                          acc
                                          (let ((c (+ a b)))
                                            (if (> c int-max) #f
                                                (let* ((cs (number->string c))
                                                       (len (string-length cs)))
                                                  (if (and (<= (+ pos len) n)
                                                           (string=? (substring num pos (+ pos len)) cs))
                                                      (build b c (+ pos len) (append acc (list c)))
                                                      #f))))))
                                    (let ((result (build first second (+ i j) (list first second))))
                                      (if result
                                          result
                                          (loop-j (+ j 1)))))))))))))))))
```

## Erlang

```erlang
-module(solution).
-export([split_into_fibonacci/1]).

-define(INT_MAX, 2147483647).

split_into_fibonacci(Num) ->
    S = binary_to_list(Num),
    Len = length(S),
    MaxFirst = erlang:min(Len - 2, 10),
    case find_first(1, MaxFirst, S, Len) of
        {ok, Seq} -> Seq;
        error -> []
    end.

%% Try all possible lengths for the first number
find_first(I, MaxFirst, S, Len) when I =< MaxFirst ->
    case get_number(S, I) of
        {ok, N1} ->
            MaxSecond = erlang:min(Len - I, 10),
            case find_second(N1, I, 1, MaxSecond, S, Len) of
                {ok, Seq} -> {ok, Seq};
                error -> find_first(I + 1, MaxFirst, S, Len)
            end;
        _ ->
            find_first(I + 1, MaxFirst, S, Len)
    end;
find_first(_, _, _, _) ->
    error.

%% Try all possible lengths for the second number
find_second(N1, I, J, MaxSecond, S, Len) when J =< MaxSecond ->
    RestAfterFirst = lists:nthtail(I, S),
    case get_number(RestAfterFirst, J) of
        {ok, N2} ->
            Seq0 = [N1, N2],
            Pos = I + J,
            case build_seq(N1, N2, Seq0, Pos, S, Len) of
                {ok, FullSeq} -> {ok, FullSeq};
                error -> find_second(N1, I, J + 1, MaxSecond, S, Len)
            end;
        _ ->
            find_second(N1, I, J + 1, MaxSecond, S, Len)
    end;
find_second(_, _, _, _, _, _) ->
    error.

%% Build the rest of the sequence recursively
build_seq(_Prev2, _Prev1, Seq, Pos, _S, Len) when Pos == Len ->
    {ok, Seq};
build_seq(Prev2, Prev1, Seq, Pos, S, Len) ->
    Sum = Prev2 + Prev1,
    case Sum > ?INT_MAX of
        true -> error;
        false ->
            SumStr = integer_to_list(Sum),
            SumLen = length(SumStr),
            Rest = lists:nthtail(Pos, S),
            case lists:sublist(Rest, SumLen) of
                Candidate when length(Candidate) == SumLen,
                               Candidate =:= SumStr ->
                    NewPos = Pos + SumLen,
                    build_seq(Prev1, Sum, Seq ++ [Sum], NewPos, S, Len);
                _ -> error
            end
    end.

%% Parse a number of given length, checking leading zeros and overflow
get_number(List, Len) when length(List) >= Len ->
    Prefix = lists:sublist(List, Len),
    case Prefix of
        [$0 | _] when Len > 1 -> {error, leading_zero};
        _ ->
            try
                N = list_to_integer(Prefix),
                if N > ?INT_MAX -> {error, overflow}; true -> {ok, N} end
            catch _:badarg -> {error, bad}
            end
    end;
get_number(_, _) ->
    {error, short}.
```

## Elixir

```elixir
defmodule Solution do
  @spec split_into_fibonacci(num :: String.t()) :: [integer()]
  def split_into_fibonacci(num) do
    max_int = 2_147_483_647
    n = String.length(num)

    1..(n - 2)
    |> Enum.reduce_while([], fn i, _acc ->
      # first number cannot have leading zeros (unless it is "0")
      if i > 1 && String.at(num, 0) == "0" do
        {:cont, []}
      else
        first_str = String.slice(num, 0, i)
        {first_val, _} = Integer.parse(first_str)

        if first_val > max_int do
          {:cont, []}
        else
          (1..(n - i - 1))
          |> Enum.reduce_while([], fn j, _ ->
            # second number cannot have leading zeros (unless it is "0")
            if j > 1 && String.at(num, i) == "0" do
              {:cont, []}
            else
              second_str = String.slice(num, i, j)
              {second_val, _} = Integer.parse(second_str)

              if second_val > max_int do
                {:cont, []}
              else
                seq = [first_val, second_val]
                idx = i + j

                case build(num, idx, first_val, second_val, seq, max_int) do
                  nil -> {:cont, []}
                  result when length(result) >= 3 -> {:halt, result}
                  _ -> {:cont, []}
                end
              end
            end
          end)
          |> case do
            [] -> {:cont, []}
            res -> {:halt, res}
          end
        end
      end
    end)
    |> case do
      [] -> []
      list -> list
    end
  end

  defp build(num, idx, a, b, seq, max_int) do
    n = String.length(num)

    if idx == n do
      seq
    else
      sum = a + b

      if sum > max_int do
        nil
      else
        sum_str = Integer.to_string(sum)
        len = byte_size(sum_str)

        if idx + len <= n && String.slice(num, idx, len) == sum_str do
          build(num, idx + len, b, sum, seq ++ [sum], max_int)
        else
          nil
        end
      end
    end
  end
end
```
