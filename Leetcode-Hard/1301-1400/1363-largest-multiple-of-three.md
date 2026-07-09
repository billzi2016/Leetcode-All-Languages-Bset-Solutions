# 1363. Largest Multiple of Three

## Cpp

```cpp
class Solution {
public:
    string largestMultipleOfThree(vector<int>& digits) {
        int cnt[10] = {0};
        long long sum = 0;
        for (int d : digits) {
            cnt[d]++;
            sum += d;
        }
        int mod = sum % 3;
        auto remove_one = [&](int rem) -> bool {
            for (int i = 0; i <= 9; ++i) {
                if (i % 3 == rem && cnt[i] > 0) {
                    cnt[i]--;
                    return true;
                }
            }
            return false;
        };
        auto remove_two = [&](int rem) -> bool {
            int removed = 0;
            for (int repeat = 0; repeat < 2; ++repeat) {
                bool found = false;
                for (int i = 0; i <= 9; ++i) {
                    if (i % 3 == rem && cnt[i] > 0) {
                        cnt[i]--;
                        removed++;
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    // rollback any removals
                    for (int j = 0; j <= 9; ++j) {
                        while (removed > 0 && cnt[j] < 0) { /* never happens */ }
                    }
                    return false;
                }
            }
            return true;
        };
        if (mod == 1) {
            if (!remove_one(1)) {
                remove_two(2);
            }
        } else if (mod == 2) {
            if (!remove_one(2)) {
                remove_two(1);
            }
        }
        string res;
        for (int i = 9; i >= 0; --i) {
            res.append(cnt[i], char('0' + i));
        }
        if (res.empty()) return "";
        if (res[0] == '0') return "0";
        return res;
    }
};
```

## Java

```java
class Solution {
    public String largestMultipleOfThree(int[] digits) {
        int[] cnt = new int[10];
        int sum = 0;
        for (int d : digits) {
            cnt[d]++;
            sum += d;
        }
        int mod = sum % 3;
        if (mod != 0) {
            boolean removedOne = false;
            // try to remove one smallest digit with remainder == mod
            for (int i = 0; i <= 9; i++) {
                if (i % 3 == mod && cnt[i] > 0) {
                    cnt[i]--;
                    removedOne = true;
                    break;
                }
            }
            if (!removedOne) {
                // need to remove two digits with remainder == (3 - mod)
                int targetRem = (3 - mod) % 3;
                int need = 2;
                for (int i = 0; i <= 9 && need > 0; i++) {
                    while (cnt[i] > 0 && i % 3 == targetRem && need > 0) {
                        cnt[i]--;
                        need--;
                    }
                }
                if (need > 0) {
                    return "";
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int d = 9; d >= 0; d--) {
            while (cnt[d]-- > 0) {
                sb.append(d);
            }
        }

        if (sb.length() == 0) return "";
        // If the highest digit is '0', all digits are zero.
        if (sb.charAt(0) == '0') return "0";
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        cnt = [0] * 10
        total = 0
        for d in digits:
            cnt[d] += 1
            total += d

        mod = total % 3

        def remove_one(rem):
            # rem is remainder we need to remove (1 or 2)
            for digit in range(1, 10):
                if digit % 3 == rem and cnt[digit] > 0:
                    cnt[digit] -= 1
                    return True
            return False

        def remove_two(rem):
            # remove two digits each with remainder rem
            removed = 0
            for _ in range(2):
                found = False
                for digit in range(1, 10):
                    if digit % 3 == rem and cnt[digit] > 0:
                        cnt[digit] -= 1
                        removed += 1
                        found = True
                        break
                if not found:
                    # rollback any removals done in this attempt
                    for d in range(10):
                        cnt[d] += (cnt[d] < 0) * -cnt[d]  # no need, we will handle by returning False
                    return False
            return True

        if mod == 1:
            if not remove_one(1):
                # try removing two digits with remainder 2
                # need to actually remove two smallest such digits
                removed = 0
                for _ in range(2):
                    found = False
                    for digit in range(1, 10):
                        if digit % 3 == 2 and cnt[digit] > 0:
                            cnt[digit] -= 1
                            removed += 1
                            found = True
                            break
                    if not found:
                        # cannot fix, restore any removals (though we will end up empty)
                        for d in range(10):
                            cnt[d] += 0
                        return ""
        elif mod == 2:
            if not remove_one(2):
                removed = 0
                for _ in range(2):
                    found = False
                    for digit in range(1, 10):
                        if digit % 3 == 1 and cnt[digit] > 0:
                            cnt[digit] -= 1
                            removed += 1
                            found = True
                            break
                    if not found:
                        return ""

        # Build result string
        res_parts = []
        for d in range(9, -1, -1):
            if cnt[d]:
                res_parts.append(str(d) * cnt[d])
        if not res_parts:
            return ""
        result = "".join(res_parts)
        # handle all zeros case
        if result[0] == '0':
            return "0"
        return result
```

## Python3

```python
from typing import List

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        count = [0] * 10
        total = 0
        for d in digits:
            count[d] += 1
            total += d

        mod = total % 3
        if mod != 0:
            def remove(rem: int, need: int) -> bool:
                left = need
                for v in range(10):
                    if v % 3 == rem:
                        while count[v] > 0 and left > 0:
                            count[v] -= 1
                            left -= 1
                            if left == 0:
                                break
                return left == 0

            if mod == 1:
                if not remove(1, 1):
                    if not remove(2, 2):
                        return ""
            else:  # mod == 2
                if not remove(2, 1):
                    if not remove(1, 2):
                        return ""

        # build result string in descending order
        res_parts = []
        for v in range(9, -1, -1):
            if count[v]:
                res_parts.append(str(v) * count[v])
        if not res_parts:
            return ""
        result = "".join(res_parts)
        # handle all zeros case
        if result[0] == '0':
            return "0"
        return result
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

char* largestMultipleOfThree(int* digits, int digitsSize) {
    int freq[10] = {0};
    int sum = 0;
    for (int i = 0; i < digitsSize; ++i) {
        int d = digits[i];
        freq[d]++;
        sum += d;
    }
    int rem = sum % 3;

    if (rem == 1) {
        bool removed = false;
        for (int d = 1; d <= 9 && !removed; ++d) {
            if (d % 3 == 1 && freq[d] > 0) {
                freq[d]--;
                removed = true;
            }
        }
        if (!removed) {
            int need = 2;
            for (int d = 1; d <= 9 && need > 0; ++d) {
                while (need > 0 && freq[d] > 0 && d % 3 == 2) {
                    freq[d]--;
                    need--;
                }
            }
            if (need != 0) {
                char* empty = (char*)malloc(1);
                empty[0] = '\0';
                return empty;
            }
        }
    } else if (rem == 2) {
        bool removed = false;
        for (int d = 2; d <= 9 && !removed; ++d) {
            if (d % 3 == 2 && freq[d] > 0) {
                freq[d]--;
                removed = true;
            }
        }
        if (!removed) {
            int need = 2;
            for (int d = 1; d <= 9 && need > 0; ++d) {
                while (need > 0 && freq[d] > 0 && d % 3 == 1) {
                    freq[d]--;
                    need--;
                }
            }
            if (need != 0) {
                char* empty = (char*)malloc(1);
                empty[0] = '\0';
                return empty;
            }
        }
    }

    int total = 0;
    for (int i = 0; i < 10; ++i) total += freq[i];
    if (total == 0) {
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    char* ans = (char*)malloc(total + 1);
    int idx = 0;
    for (int d = 9; d >= 0; --d) {
        while (freq[d] > 0) {
            ans[idx++] = '0' + d;
            freq[d]--;
        }
    }
    ans[idx] = '\0';

    if (ans[0] == '0') {   // all zeros
        ans[1] = '\0';
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public string LargestMultipleOfThree(int[] digits) {
        int[] cnt = new int[10];
        int sum = 0;
        foreach (int d in digits) {
            cnt[d]++;
            sum += d;
        }
        int mod = sum % 3;
        if (mod != 0) {
            bool adjusted = false;
            if (mod == 1) {
                // try to remove one digit with remainder 1
                for (int i = 1; i <= 9; i++) {
                    if (i % 3 == 1 && cnt[i] > 0) {
                        cnt[i]--;
                        adjusted = true;
                        break;
                    }
                }
                if (!adjusted) {
                    int removed = 0;
                    for (int i = 1; i <= 9 && removed < 2; i++) {
                        while (cnt[i] > 0 && i % 3 == 2 && removed < 2) {
                            cnt[i]--;
                            removed++;
                        }
                    }
                    if (removed != 2) return "";
                }
            } else { // mod == 2
                for (int i = 1; i <= 9; i++) {
                    if (i % 3 == 2 && cnt[i] > 0) {
                        cnt[i]--;
                        adjusted = true;
                        break;
                    }
                }
                if (!adjusted) {
                    int removed = 0;
                    for (int i = 1; i <= 9 && removed < 2; i++) {
                        while (cnt[i] > 0 && i % 3 == 1 && removed < 2) {
                            cnt[i]--;
                            removed++;
                        }
                    }
                    if (removed != 2) return "";
                }
            }
        }

        var sb = new System.Text.StringBuilder();
        for (int d = 9; d >= 0; d--) {
            while (cnt[d] > 0) {
                sb.Append((char)('0' + d));
                cnt[d]--;
            }
        }
        string res = sb.ToString();
        if (res.Length == 0) return "";
        if (res[0] == '0') return "0";
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} digits
 * @return {string}
 */
var largestMultipleOfThree = function(digits) {
    const cnt = new Array(10).fill(0);
    let sum = 0;
    for (const d of digits) {
        cnt[d]++;
        sum += d;
    }
    const mod = sum % 3;
    if (mod !== 0) {
        const removeOne = (m) => {
            for (let i = 0; i <= 9; i++) {
                if (i % 3 === m && cnt[i] > 0) {
                    cnt[i]--;
                    return true;
                }
            }
            return false;
        };
        const removeTwo = (m) => {
            const removed = [];
            for (let i = 0; i <= 9; i++) {
                while (cnt[i] > 0 && i % 3 === m && removed.length < 2) {
                    cnt[i]--;
                    removed.push(i);
                }
                if (removed.length === 2) break;
            }
            if (removed.length === 2) return true;
            // revert if not enough
            for (const v of removed) cnt[v]++;
            return false;
        };
        if (mod === 1) {
            if (!removeOne(1)) removeTwo(2);
        } else { // mod === 2
            if (!removeOne(2)) removeTwo(1);
        }
    }
    const result = [];
    for (let i = 9; i >= 0; i--) {
        while (cnt[i]-- > 0) result.push(i);
    }
    if (result.length === 0) return "";
    if (result[0] === 0) return "0";
    return result.join('');
};
```

## Typescript

```typescript
function largestMultipleOfThree(digits: number[]): string {
    const cnt = new Array(10).fill(0);
    let sum = 0;
    for (const d of digits) {
        cnt[d]++;
        sum += d;
    }
    const mod = sum % 3;

    const adjust = (): boolean => {
        if (mod === 0) return true;
        if (mod === 1) {
            // try remove one digit with remainder 1
            for (let d = 0; d <= 9; d++) {
                if (d % 3 === 1 && cnt[d] > 0) {
                    cnt[d]--;
                    return true;
                }
            }
            // else remove two digits with remainder 2
            let removed = 0;
            for (let d = 0; d <= 9 && removed < 2; d++) {
                while (cnt[d] > 0 && d % 3 === 2 && removed < 2) {
                    cnt[d]--;
                    removed++;
                }
            }
            return removed === 2;
        } else { // mod === 2
            for (let d = 0; d <= 9; d++) {
                if (d % 3 === 2 && cnt[d] > 0) {
                    cnt[d]--;
                    return true;
                }
            }
            let removed = 0;
            for (let d = 0; d <= 9 && removed < 2; d++) {
                while (cnt[d] > 0 && d % 3 === 1 && removed < 2) {
                    cnt[d]--;
                    removed++;
                }
            }
            return removed === 2;
        }
    };

    if (!adjust()) return "";

    let result = "";
    for (let d = 9; d >= 0; d--) {
        if (cnt[d] > 0) {
            result += d.toString().repeat(cnt[d]);
        }
    }

    if (result.length === 0) return "";
    if (result[0] === '0') return "0";
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $digits
     * @return String
     */
    function largestMultipleOfThree($digits) {
        $cnt = array_fill(0, 10, 0);
        $sum = 0;
        foreach ($digits as $d) {
            $cnt[$d]++;
            $sum += $d;
        }

        $mod = $sum % 3;
        if ($mod !== 0) {
            $remove = function($rem, $k) use (&$cnt) {
                $removed = 0;
                for ($i = 0; $i < 10 && $removed < $k; $i++) {
                    if ($i % 3 == $rem) {
                        while ($cnt[$i] > 0 && $removed < $k) {
                            $cnt[$i]--;
                            $removed++;
                        }
                    }
                }
                return $removed === $k;
            };

            $success = false;
            if ($mod == 1) {
                $success = $remove(1, 1);
                if (!$success) {
                    $success = $remove(2, 2);
                }
            } else { // $mod == 2
                $success = $remove(2, 1);
                if (!$success) {
                    $success = $remove(1, 2);
                }
            }

            if (!$success) {
                return "";
            }
        }

        $res = "";
        for ($i = 9; $i >= 0; $i--) {
            if ($cnt[$i] > 0) {
                $res .= str_repeat((string)$i, $cnt[$i]);
            }
        }

        if ($res === "") {
            return "";
        }
        // If the highest digit is '0', all digits are zero.
        if ($res[0] === '0') {
            return "0";
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func largestMultipleOfThree(_ digits: [Int]) -> String {
        var cnt = Array(repeating: 0, count: 10)
        var sum = 0
        for d in digits {
            cnt[d] += 1
            sum += d
        }
        let mod = sum % 3
        if mod != 0 {
            func remove(_ rem: Int, _ k: Int) -> Bool {
                var need = k
                for i in 0...9 where i % 3 == rem && need > 0 {
                    while cnt[i] > 0 && need > 0 {
                        cnt[i] -= 1
                        need -= 1
                    }
                }
                return need == 0
            }
            var success = false
            if mod == 1 {
                success = remove(1, 1)
                if !success { success = remove(2, 2) }
            } else { // mod == 2
                success = remove(2, 1)
                if !success { success = remove(1, 2) }
            }
            if !success {
                return ""
            }
        }
        
        var result = ""
        for i in stride(from: 9, through: 0, by: -1) {
            if cnt[i] > 0 {
                let digitStr = String(i)
                result += String(repeating: digitStr, count: cnt[i])
            }
        }
        if result.isEmpty { return "" }
        if result.first == "0" { return "0" }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestMultipleOfThree(digits: IntArray): String {
        val cnt = IntArray(10)
        var sum = 0
        for (d in digits) {
            cnt[d]++
            sum += d
        }
        val mod = sum % 3
        if (mod != 0) {
            fun remove(rem: Int, needCount: Int): Boolean {
                var need = needCount
                for (i in 0..9) {
                    if (i % 3 == rem) {
                        while (cnt[i] > 0 && need > 0) {
                            cnt[i]--
                            need--
                        }
                        if (need == 0) break
                    }
                }
                return need == 0
            }
            val possible = when (mod) {
                1 -> remove(1, 1) || remove(2, 2)
                else -> remove(2, 1) || remove(1, 2) // mod == 2
            }
            if (!possible) return ""
        }
        val sb = StringBuilder()
        for (i in 9 downTo 0) {
            repeat(cnt[i]) { sb.append(i) }
        }
        if (sb.isEmpty()) return ""
        if (sb[0] == '0') return "0"
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String largestMultipleOfThree(List<int> digits) {
    List<int> cnt = List.filled(10, 0);
    int sum = 0;
    for (int d in digits) {
      cnt[d]++;
      sum += d;
    }
    int mod = sum % 3;

    bool possible = true;
    if (mod == 1) {
      if (!_remove(cnt, [1, 4, 7], 1)) {
        if (!_remove(cnt, [2, 5, 8], 2)) {
          possible = false;
        }
      }
    } else if (mod == 2) {
      if (!_remove(cnt, [2, 5, 8], 1)) {
        if (!_remove(cnt, [1, 4, 7], 2)) {
          possible = false;
        }
      }
    }

    if (!possible) return "";

    StringBuffer sb = StringBuffer();
    for (int d = 9; d >= 0; d--) {
      for (int i = 0; i < cnt[d]; i++) {
        sb.write(d);
      }
    }
    String res = sb.toString();
    if (res.isEmpty) return "";
    if (res[0] == '0') return "0";
    return res;
  }

  bool _remove(List<int> cnt, List<int> candidates, int need) {
    for (int i = 0; i < need; i++) {
      bool removed = false;
      for (int d in candidates) {
        if (cnt[d] > 0) {
          cnt[d]--;
          removed = true;
          break;
        }
      }
      if (!removed) return false;
    }
    return true;
  }
}
```

## Golang

```go
func largestMultipleOfThree(digits []int) string {
    cnt := make([]int, 10)
    sum := 0
    for _, d := range digits {
        cnt[d]++
        sum += d
    }
    mod := sum % 3
    if mod != 0 {
        // try to remove one digit with remainder == mod
        removed := false
        for i := 0; i <= 9 && !removed; i++ {
            if i%3 == mod && cnt[i] > 0 {
                cnt[i]--
                removed = true
            }
        }
        if !removed {
            // need to remove two digits with remainder == (3 - mod)
            need := 2
            target := (3 - mod) % 3
            for i := 0; i <= 9 && need > 0; i++ {
                for cnt[i] > 0 && i%3 == target && need > 0 {
                    cnt[i]--
                    need--
                }
            }
            if need != 0 {
                return ""
            }
        }
    }

    // build result in descending order
    var sb []byte
    for d := 9; d >= 0; d-- {
        for i := 0; i < cnt[d]; i++ {
            sb = append(sb, byte('0'+d))
        }
    }
    if len(sb) == 0 {
        return ""
    }
    if sb[0] == '0' { // all zeros
        return "0"
    }
    return string(sb)
}
```

## Ruby

```ruby
def largest_multiple_of_three(digits)
  cnt = Array.new(10, 0)
  sum = 0
  digits.each do |d|
    cnt[d] += 1
    sum += d
  end

  mod = sum % 3
  if mod != 0
    removed = false
    if mod == 1
      [1, 4, 7].each do |d|
        if cnt[d] > 0
          cnt[d] -= 1
          removed = true
          break
        end
      end
      unless removed
        need = 2
        removed_cnt = 0
        [2, 5, 8].each do |d|
          while cnt[d] > 0 && removed_cnt < need
            cnt[d] -= 1
            removed_cnt += 1
          end
          break if removed_cnt == need
        end
        removed = (removed_cnt == need)
      end
    else # mod == 2
      [2, 5, 8].each do |d|
        if cnt[d] > 0
          cnt[d] -= 1
          removed = true
          break
        end
      end
      unless removed
        need = 2
        removed_cnt = 0
        [1, 4, 7].each do |d|
          while cnt[d] > 0 && removed_cnt < need
            cnt[d] -= 1
            removed_cnt += 1
          end
          break if removed_cnt == need
        end
        removed = (removed_cnt == need)
      end
    end
    return "" unless removed
  end

  result = ""
  9.downto(0) { |d| result << d.to_s * cnt[d] }

  return "" if result.empty?
  return "0" if result[0] == '0'
  result
end
```

## Scala

```scala
object Solution {
    def largestMultipleOfThree(digits: Array[Int]): String = {
        val cnt = new Array[Int](10)
        var sum = 0
        for (d <- digits) {
            cnt(d) += 1
            sum += d
        }

        def remove(rem: Int, need: Int): Boolean = {
            var remaining = need
            var d = 0
            while (d <= 9 && remaining > 0) {
                if (d % 3 == rem && cnt(d) > 0) {
                    val take = math.min(cnt(d), remaining)
                    cnt(d) -= take
                    remaining -= take
                }
                d += 1
            }
            remaining == 0
        }

        sum % 3 match {
            case 1 =>
                if (!remove(1, 1)) {
                    // try removing two digits with remainder 2
                    remove(2, 2)
                }
            case 2 =>
                if (!remove(2, 1)) {
                    // try removing two digits with remainder 1
                    remove(1, 2)
                }
            case _ => // already divisible by 3
        }

        val sb = new StringBuilder
        for (d <- 9 to 0 by -1) {
            var i = cnt(d)
            while (i > 0) {
                sb.append(('0' + d).toChar)
                i -= 1
            }
        }

        if (sb.isEmpty) ""
        else if (sb.charAt(0) == '0') "0"
        else sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn largest_multiple_of_three(digits: Vec<i32>) -> String {
        let mut cnt = [0usize; 10];
        let mut sum = 0i32;
        for &d in &digits {
            let di = d as usize;
            cnt[di] += 1;
            sum += d;
        }
        let r = (sum % 3 + 3) % 3; // ensure non‑negative

        if r == 1 {
            // try to remove one digit with remainder 1
            let mut removed = false;
            for d in 0..=9 {
                if d % 3 == 1 && cnt[d] > 0 {
                    cnt[d] -= 1;
                    removed = true;
                    break;
                }
            }
            if !removed {
                // need to remove two digits with remainder 2
                let mut need = 2;
                for d in 0..=9 {
                    while need > 0 && cnt[d] > 0 && d % 3 == 2 {
                        cnt[d] -= 1;
                        need -= 1;
                    }
                    if need == 0 {
                        break;
                    }
                }
                if need != 0 {
                    return String::new();
                }
            }
        } else if r == 2 {
            // try to remove one digit with remainder 2
            let mut removed = false;
            for d in 0..=9 {
                if d % 3 == 2 && cnt[d] > 0 {
                    cnt[d] -= 1;
                    removed = true;
                    break;
                }
            }
            if !removed {
                // need to remove two digits with remainder 1
                let mut need = 2;
                for d in 0..=9 {
                    while need > 0 && cnt[d] > 0 && d % 3 == 1 {
                        cnt[d] -= 1;
                        need -= 1;
                    }
                    if need == 0 {
                        break;
                    }
                }
                if need != 0 {
                    return String::new();
                }
            }
        }

        // build the result string in descending order
        let mut res = String::new();
        for d in (0..=9).rev() {
            for _ in 0..cnt[d] {
                res.push((b'0' + d as u8) as char);
            }
        }

        if res.is_empty() {
            return String::new();
        }
        // if the number consists only of zeros, return "0"
        if res.chars().next().unwrap() == '0' {
            return "0".to_string();
        }
        res
    }
}
```

## Racket

```racket
(define/contract (largest-multiple-of-three digits)
  (-> (listof exact-integer?) string?)
  (let* ((cnt (make-vector 10 0))
         (sum (foldl (lambda (d acc) 
                       (vector-set! cnt d (+ (vector-ref cnt d) 1))
                       (+ acc d))
                     0
                     digits))
         (mod (remainder sum 3)))
    (define (remove-k! rem k)
      (let loop ((d 0) (need k))
        (cond [(= need 0) #t]
              [(> d 9)   #f]
              [else
               (if (and (= (modulo d 3) rem) (> (vector-ref cnt d) 0))
                   (begin
                     (vector-set! cnt d (- (vector-ref cnt d) 1))
                     (loop d (- need 1)))
                   (loop (+ d 1) need))])))
    (cond [(= mod 1)
           (if (remove-k! 1 1)
               (void)
               (remove-k! 2 2))]
          [(= mod 2)
           (if (remove-k! 2 1)
               (void)
               (remove-k! 1 2))]
          [else (void)])
    ;; build result string in descending order
    (let ((result
            (let loop ((d 9) (acc ""))
              (if (< d 0)
                  acc
                  (let* ((c (vector-ref cnt d))
                         (segment (make-string c (integer->char (+ #\0 d)))))
                    (loop (- d 1) (string-append segment acc)))))))
      (cond [(zero? (string-length result)) ""]
            [(char=? (string-ref result 0) #\0) "0"]
            [else result]))))
```

## Erlang

```erlang
-module(solution).
-export([largest_multiple_of_three/1]).

-spec largest_multiple_of_three(Digits :: [integer()]) -> unicode:unicode_binary().
largest_multiple_of_three(Digits) ->
    Counts0 = list_to_tuple(lists:duplicate(10, 0)),
    Counts = lists:foldl(fun(D, Acc) ->
                Index = D + 1,
                Old = element(Index, Acc),
                setelement(Index, Acc, Old + 1)
            end, Counts0, Digits),
    Sum = lists:sum(Digits),
    Rem = Sum rem 3,
    FinalCounts = case Rem of
        0 -> Counts;
        1 ->
            case remove_one_digit(1, Counts) of
                {ok, C1} -> C1;
                error ->
                    case remove_n_digits(2, 2, Counts) of
                        {ok, C2} -> C2;
                        error -> Counts
                    end
            end;
        2 ->
            case remove_one_digit(2, Counts) of
                {ok, C1} -> C1;
                error ->
                    case remove_n_digits(1, 2, Counts) of
                        {ok, C2} -> C2;
                        error -> Counts
                    end
            end
    end,
    Iolist = [lists:duplicate(Cnt, D+$0) ||
                D <- lists:seq(9,0,-1),
                (Cnt = element(D+1, FinalCounts)) > 0],
    ResultBin = iolist_to_binary(Iolist),
    case ResultBin of
        <<>> -> <<>>;
        <<$0,_/binary>> -> <<"0">>;
        _ -> ResultBin
    end.

remove_one_digit(Mod, Counts) ->
    case find_smallest(Mod, Counts) of
        {ok, D} ->
            NewCounts = setelement(D+1, Counts, element(D+1, Counts)-1),
            {ok, NewCounts};
        error -> error
    end.

remove_n_digits(_Mod, 0, Counts) -> {ok, Counts};
remove_n_digits(Mod, N, Counts) when N > 0 ->
    case find_smallest(Mod, Counts) of
        {ok, D} ->
            C = element(D+1, Counts),
            NewCounts = setelement(D+1, Counts, C-1),
            remove_n_digits(Mod, N-1, NewCounts);
        error -> error
    end.

find_smallest(Mod, Counts) -> find_smallest(0, Mod, Counts).

find_smallest(Digit, Mod, Counts) when Digit =< 9 ->
    case (Digit rem 3 == Mod) andalso element(Digit+1, Counts) > 0 of
        true -> {ok, Digit};
        false -> find_smallest(Digit+1, Mod, Counts)
    end;
find_smallest(_, _, _) -> error.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_multiple_of_three(digits :: [integer]) :: String.t()
  def largest_multiple_of_three(digits) do
    counts =
      Enum.reduce(digits, List.duplicate(0, 10), fn d, acc ->
        List.update_at(acc, d, &(&1 + 1))
      end)

    total_sum = Enum.sum(digits)
    mod = rem(total_sum, 3)

    {new_counts, possible} =
      cond do
        mod == 0 ->
          {counts, true}

        mod == 1 ->
          {c1, ok1} = remove_one(counts, 1)

          if ok1 do
            {c1, true}
          else
            {c2, ok2} = remove_two(counts, 2)
            {c2, ok2}
          end

        mod == 2 ->
          {c1, ok1} = remove_one(counts, 2)

          if ok1 do
            {c1, true}
          else
            {c2, ok2} = remove_two(counts, 1)
            {c2, ok2}
          end
      end

    unless possible do
      ""
    else
      result =
        for d <- 9..0,
            cnt = Enum.at(new_counts, d),
            _ <- 1..cnt,
            do: Integer.to_string(d)
        |> Enum.join()

      cond do
        result == "" -> ""
        String.starts_with?(result, "0") -> "0"
        true -> result
      end
    end
  end

  defp remove_one(counts, target_mod) do
    {new_counts, removed} =
      Enum.reduce_while(0..9, {counts, false}, fn d, {c, _} ->
        if rem(d, 3) == target_mod and Enum.at(c, d) > 0 do
          updated = List.update_at(c, d, &(&1 - 1))
          {:halt, {updated, true}}
        else
          {:cont, {c, false}}
        end
      end)

    {new_counts, removed}
  end

  defp remove_two(counts, target_mod) do
    {c1, ok1} = remove_one(counts, target_mod)

    if ok1 do
      {c2, ok2} = remove_one(c1, target_mod)
      {c2, ok2}
    else
      {counts, false}
    end
  end
end
```
