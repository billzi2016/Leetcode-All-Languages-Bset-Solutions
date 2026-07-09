# 2217. Find Palindrome With Fixed Length

## Cpp

```cpp
class Solution {
public:
    vector<long long> kthPalindrome(vector<int>& queries, int intLength) {
        int half = (intLength + 1) / 2;
        long long start = 1;
        for (int i = 0; i < half - 1; ++i) start *= 10; // 10^{half-1}
        long long maxCount = 9 * start; // total palindromes of this length
        
        vector<long long> ans;
        ans.reserve(queries.size());
        for (int q : queries) {
            if ((long long)q > maxCount) {
                ans.push_back(-1);
                continue;
            }
            long long firstHalf = start + q - 1;
            string s = to_string(firstHalf);
            string rev = s;
            if (intLength % 2 == 1) rev.pop_back(); // omit middle digit for odd length
            reverse(rev.begin(), rev.end());
            string palStr = s + rev;
            ans.push_back(stoll(palStr));
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long[] kthPalindrome(int[] queries, int intLength) {
        int n = queries.length;
        long[] ans = new long[n];
        int halfLen = (intLength + 1) / 2;

        long start = 1L;
        for (int i = 1; i < halfLen; i++) {
            start *= 10L;
        }
        long total = 9L * start; // number of palindromes of this length

        for (int i = 0; i < n; i++) {
            long k = queries[i];
            if (k > total) {
                ans[i] = -1L;
                continue;
            }
            long firstHalf = start + k - 1;
            String s = Long.toString(firstHalf);
            StringBuilder sb = new StringBuilder(s);
            int revStart = (intLength % 2 == 0) ? s.length() - 1 : s.length() - 2;
            for (int j = revStart; j >= 0; --j) {
                sb.append(s.charAt(j));
            }
            ans[i] = Long.parseLong(sb.toString());
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def kthPalindrome(self, queries, intLength):
        """
        :type queries: List[int]
        :type intLength: int
        :rtype: List[int]
        """
        half = (intLength + 1) // 2
        start = 10 ** (half - 1)
        max_cnt = 9 * 10 ** (half - 1)
        res = []
        for k in queries:
            if k > max_cnt:
                res.append(-1)
                continue
            first = start + k - 1
            s = str(first)
            if intLength % 2 == 0:
                pal = s + s[::-1]
            else:
                pal = s + s[-2::-1]
            res.append(int(pal))
        return res
```

## Python3

```python
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half = (intLength + 1) // 2
        start = 10 ** (half - 1)
        max_cnt = 9 * 10 ** (half - 1)
        res = []
        for k in queries:
            if k > max_cnt:
                res.append(-1)
                continue
            first_half_num = start + k - 1
            s = str(first_half_num)
            if intLength % 2 == 0:
                pal = s + s[::-1]
            else:
                pal = s + s[-2::-1]
            res.append(int(pal))
        return res
```

## C

```c
#include <stdlib.h>

long long* kthPalindrome(int* queries, int queriesSize, int intLength, int* returnSize) {
    *returnSize = queriesSize;
    long long *ans = (long long*)malloc(sizeof(long long) * queriesSize);
    
    int half = (intLength + 1) / 2;
    long long start = 1;
    for (int i = 1; i < half; ++i) {
        start *= 10LL;               // 10^(half-1)
    }
    long long maxCount = 9LL * start; // total palindromes of this length
    
    for (int i = 0; i < queriesSize; ++i) {
        int k = queries[i];
        if ((long long)k > maxCount) {
            ans[i] = -1;
            continue;
        }
        long long firstHalf = start + (long long)k - 1LL;
        long long pal = firstHalf;
        long long revPart = firstHalf;
        if (intLength % 2 == 1) {
            revPart /= 10; // skip middle digit for odd length
        }
        while (revPart > 0) {
            pal = pal * 10 + (revPart % 10);
            revPart /= 10;
        }
        ans[i] = pal;
    }
    
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public long[] KthPalindrome(int[] queries, int intLength)
    {
        int n = queries.Length;
        long[] ans = new long[n];
        int halfLen = (intLength + 1) / 2;
        long start = (long)Math.Pow(10, halfLen - 1); // smallest first half
        long maxCount = 9 * start; // total palindromes of this length

        for (int i = 0; i < n; i++)
        {
            int k = queries[i];
            if (k > maxCount)
            {
                ans[i] = -1;
                continue;
            }

            long half = start + k - 1;
            string s = half.ToString();

            if (intLength % 2 == 0)
            {
                char[] rev = s.ToCharArray();
                Array.Reverse(rev);
                ans[i] = long.Parse(s + new string(rev));
            }
            else
            {
                string left = s.Substring(0, s.Length - 1);
                char[] rev = left.ToCharArray();
                Array.Reverse(rev);
                ans[i] = long.Parse(s + new string(rev));
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} queries
 * @param {number} intLength
 * @return {number[]}
 */
var kthPalindrome = function(queries, intLength) {
    const halfLen = Math.ceil(intLength / 2);
    const base = Math.pow(10, halfLen - 1); // smallest prefix without leading zero
    const maxCount = 9 * base; // total palindromes of this length
    
    const res = new Array(queries.length);
    
    for (let i = 0; i < queries.length; ++i) {
        const k = queries[i];
        if (k > maxCount) {
            res[i] = -1;
            continue;
        }
        const prefixNum = base + k - 1;
        const s = String(prefixNum);
        const rev = s.split('').reverse().join('');
        let palStr;
        if (intLength % 2 === 0) {
            palStr = s + rev;
        } else {
            palStr = s + rev.slice(1); // omit middle digit duplicate
        }
        res[i] = Number(palStr);
    }
    
    return res;
};
```

## Typescript

```typescript
function kthPalindrome(queries: number[], intLength: number): number[] {
    const halfLen = Math.ceil(intLength / 2);
    const base = Math.pow(10, halfLen - 1);
    const total = 9 * base;
    const result: number[] = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const k = queries[i];
        if (k > total) {
            result[i] = -1;
            continue;
        }
        const firstHalfNum = base + k - 1;
        const s = firstHalfNum.toString();
        const rev = s.split('').reverse().join('');
        let palindromeStr: string;
        if (intLength % 2 === 0) {
            palindromeStr = s + rev;
        } else {
            palindromeStr = s + rev.slice(1);
        }
        result[i] = Number(palindromeStr);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $queries
     * @param Integer $intLength
     * @return Integer[]
     */
    function kthPalindrome($queries, $intLength) {
        $halfLen = intdiv($intLength + 1, 2);
        $start = (int)pow(10, $halfLen - 1);
        $maxHalf = (int)pow(10, $halfLen) - 1;
        $result = [];

        foreach ($queries as $k) {
            $half = $start + $k - 1;
            if ($half > $maxHalf) {
                $result[] = -1;
                continue;
            }
            $s = (string)$half;
            if ($intLength % 2 == 0) {
                $rev = strrev($s);
            } else {
                $rev = strrev(substr($s, 0, -1));
            }
            $palindrome = (int)($s . $rev);
            $result[] = $palindrome;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func kthPalindrome(_ queries: [Int], _ intLength: Int) -> [Int] {
        let half = (intLength + 1) / 2
        var base = 1
        if half > 1 {
            for _ in 1..<(half) {
                base *= 10
            }
        }
        let total = 9 * base
        var answer = [Int]()
        answer.reserveCapacity(queries.count)
        
        for k in queries {
            if k > total {
                answer.append(-1)
                continue
            }
            let firstHalf = base + (k - 1)
            var s = String(firstHalf)
            var rev = String(s.reversed())
            if intLength % 2 == 1 {
                rev.removeFirst()
            }
            let palindromeStr = s + rev
            answer.append(Int(palindromeStr)!)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kthPalindrome(queries: IntArray, intLength: Int): LongArray {
        val half = (intLength + 1) / 2
        var start = 1L
        repeat(half - 1) { start *= 10L }          // 10^(half-1)
        val maxCount = 9L * start                  // total palindromes of this length

        val result = LongArray(queries.size)
        for (i in queries.indices) {
            val k = queries[i].toLong()
            if (k > maxCount) {
                result[i] = -1L
                continue
            }
            var firstHalf = start + k - 1          // the left part of palindrome
            var palindrome = firstHalf
            var revPart = if (intLength % 2 == 0) firstHalf else firstHalf / 10

            while (revPart > 0) {
                palindrome = palindrome * 10 + (revPart % 10)
                revPart /= 10
            }
            result[i] = palindrome
        }
        return result
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  List<int> kthPalindrome(List<int> queries, int intLength) {
    int half = (intLength + 1) >> 1; // ceil(intLength/2)
    int start = pow(10, half - 1).toInt(); // smallest prefix without leading zero
    int maxCount = 9 * pow(10, half - 1).toInt(); // total palindromes of this length

    List<int> result = [];
    for (int k in queries) {
      if (k > maxCount) {
        result.add(-1);
        continue;
      }
      int prefix = start + k - 1;
      String s = prefix.toString();
      String revPart;
      if (intLength % 2 == 0) {
        revPart = s.split('').reversed.join('');
      } else {
        revPart = s.substring(0, s.length - 1).split('').reversed.join('');
      }
      result.add(int.parse(s + revPart));
    }
    return result;
  }
}
```

## Golang

```go
func kthPalindrome(queries []int, intLength int) []int64 {
	type int64Slice = []int64
	half := (intLength + 1) / 2

	start := pow10(half - 1)
	limit := pow10(half)

	ans := make(int64Slice, len(queries))
	for i, q := range queries {
		k := int64(q)
		first := start + k - 1
		if first >= limit {
			ans[i] = -1
			continue
		}
		s := strconv.FormatInt(first, 10)

		var sb strings.Builder
		sb.WriteString(s)

		revStart := len(s) - 1
		if intLength%2 == 1 {
			revStart = len(s) - 2 // skip middle digit for odd length
		}
		for j := revStart; j >= 0; j-- {
			sb.WriteByte(s[j])
		}

		pal, _ := strconv.ParseInt(sb.String(), 10, 64)
		ans[i] = pal
	}
	return ans
}

func pow10(n int) int64 {
	var res int64 = 1
	for i := 0; i < n; i++ {
		res *= 10
	}
	return res
}
```

## Ruby

```ruby
# @param {Integer[]} queries
# @param {Integer} int_length
# @return {Integer[]}
def kth_palindrome(queries, int_length)
  half_len = (int_length + 1) / 2
  start = 10 ** (half_len - 1)
  max_count = 9 * (10 ** (half_len - 1))
  result = []

  queries.each do |k|
    if k > max_count
      result << -1
    else
      first_half = start + k - 1
      s = first_half.to_s
      rev = int_length.even? ? s.reverse : s[0...-1].reverse
      result << (s + rev).to_i
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def kthPalindrome(queries: Array[Int], intLength: Int): Array[Long] = {
        val half = (intLength + 1) / 2
        val start = Math.pow(10, half - 1).toLong
        val limit = Math.pow(10, half).toLong - 1
        queries.map { q =>
            val firstHalf = start + q.toLong - 1
            if (firstHalf > limit) -1L
            else {
                val s = firstHalf.toString
                val rev = if (intLength % 2 == 0) s.reverse else s.dropRight(1).reverse
                (s + rev).toLong
            }
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn kth_palindrome(queries: Vec<i32>, int_length: i32) -> Vec<i64> {
        let l = int_length as usize;
        let half_len = (l + 1) / 2;
        // smallest number with half_len digits and no leading zero
        let start = 10_i64.pow((half_len - 1) as u32);
        // total possible palindromes of this length
        let max_count = 9_i64 * start;

        let mut result = Vec::with_capacity(queries.len());
        for &q in queries.iter() {
            let k = q as i64;
            if k > max_count {
                result.push(-1);
                continue;
            }
            // construct the first half
            let first_half_num = start + (k - 1);
            let s = first_half_num.to_string();
            let rev_part: String = if l % 2 == 0 {
                s.chars().rev().collect()
            } else {
                s[..s.len() - 1].chars().rev().collect()
            };
            let palindrome_str = format!("{}{}", s, rev_part);
            let palindrome: i64 = palindrome_str.parse().unwrap();
            result.push(palindrome);
        }
        result
    }
}
```

## Racket

```racket
(define (reverse-str s)
  (list->string (reverse (string->list s))))

(define/contract (kth-palindrome queries intLength)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((half-len (quotient (+ intLength 1) 2))
         (base (expt 10 (- half-len 1))) ; smallest first half
         (total (* 9 base)))
    (map (lambda (k)
           (if (> k total)
               -1
               (let* ((first-half (+ base (- k 1)))
                      (s (number->string first-half))
                      (rev-part (if (even? intLength)
                                    (reverse-str s)
                                    (reverse-str (substring s 0 (- (string-length s) 1))))))
                 (string->number (string-append s rev-part)))))
         queries)))
```

## Erlang

```erlang
-module(solution).
-export([kth_palindrome/2]).

-spec kth_palindrome(Queries :: [integer()], IntLength :: integer()) -> [integer()].
kth_palindrome(Queries, IntLength) ->
    HalfLen = (IntLength + 1) div 2,
    Base = trunc(math:pow(10, HalfLen - 1)),
    Total = 9 * Base,
    lists:map(
      fun(K) ->
          if K > Total -> -1;
             true ->
                 FirstHalf = Base + K - 1,
                 Str = integer_to_list(FirstHalf),
                 PalStr =
                   case IntLength rem 2 of
                       0 ->
                           Rev = lists:reverse(Str),
                           Str ++ Rev;
                       _ ->
                           RevFull = lists:reverse(Str),
                           RevDrop = tl(RevFull),
                           Str ++ RevDrop
                   end,
                 list_to_integer(PalStr)
          end
      end, Queries).
```

## Elixir

```elixir
defmodule Solution do
  @spec kth_palindrome(queries :: [integer], int_length :: integer) :: [integer]
  def kth_palindrome(queries, int_length) do
    half = div(int_length + 1, 2)
    start = pow10(half - 1)
    max_count = 9 * start

    Enum.map(queries, fn k ->
      if k > max_count do
        -1
      else
        prefix = start + k - 1
        build_palindrome(prefix, int_length)
      end
    end)
  end

  defp pow10(0), do: 1
  defp pow10(exp) when exp > 0 do
    Enum.reduce(1..exp, 1, fn _, acc -> acc * 10 end)
  end

  defp build_palindrome(prefix, len) do
    s = Integer.to_string(prefix)

    rev =
      if rem(len, 2) == 0 do
        String.reverse(s)
      else
        s
        |> String.slice(0..-2)
        |> String.reverse()
      end

    (s <> rev) |> String.to_integer()
  end
end
```
