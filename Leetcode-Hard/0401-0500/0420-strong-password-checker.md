# 0420. Strong Password Checker

## Cpp

```cpp
class Solution {
public:
    int strongPasswordChecker(string password) {
        int n = password.size();
        bool hasLower = false, hasUpper = false, hasDigit = false;
        for (char c : password) {
            if ('a' <= c && c <= 'z') hasLower = true;
            else if ('A' <= c && c <= 'Z') hasUpper = true;
            else if ('0' <= c && c <= '9') hasDigit = true;
        }
        int missingTypes = (!hasLower) + (!hasUpper) + (!hasDigit);
        
        // If length is less than 6, we can only insert characters.
        if (n < 6) {
            return max(missingTypes, 6 - n);
        }
        
        // Find repeating sequences of length >=3
        vector<int> repeats;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && password[j] == password[i]) ++j;
            int len = j - i;
            if (len >= 3) repeats.push_back(len);
            i = j;
        }
        
        // Count replacements needed to fix repeats
        int replace = 0;
        for (int len : repeats) replace += len / 3;
        
        // If length is within allowed range, answer is max of missing types and replacements
        if (n <= 20) {
            return max(missingTypes, replace);
        }
        
        // Length > 20: need deletions
        int over = n - 20;
        int left = over;
        
        // Sort repeats by len % 3 to prioritize deletions that reduce replacements most
        sort(repeats.begin(), repeats.end(),
             [](int a, int b) { return (a % 3) < (b % 3); });
        
        // First pass: use deletions to reduce replacements where len%3 == 0 (need 1 deletion)
        for (int &len : repeats) {
            if (left <= 0) break;
            if (len < 3) continue;
            int need = (len % 3 == 0) ? 1 : ((len % 3 == 1) ? 2 : 3);
            // For len%3==0 we delete 1, for len%3==1 delete 2, else we'll handle later
            if (need > left) continue;
            int del = min(need, left);
            len -= del;
            left -= del;
        }
        
        // Second pass: apply remaining deletions to any repeats
        for (int &len : repeats) {
            if (left <= 0) break;
            if (len < 3) continue;
            int del = min(len - 2, left); // keep at least length 2 to avoid creating new repeat groups
            len -= del;
            left -= del;
        }
        
        // Recalculate replacements after deletions
        replace = 0;
        for (int len : repeats) replace += len / 3;
        
        return over + max(missingTypes, replace);
    }
};
```

## Java

```java
class Solution {
    public int strongPasswordChecker(String password) {
        int n = password.length();
        boolean hasLower = false, hasUpper = false, hasDigit = false;
        for (char c : password.toCharArray()) {
            if (Character.isLowerCase(c)) hasLower = true;
            else if (Character.isUpperCase(c)) hasUpper = true;
            else if (Character.isDigit(c)) hasDigit = true;
        }
        int missing = (hasLower ? 0 : 1) + (hasUpper ? 0 : 1) + (hasDigit ? 0 : 1);

        // collect lengths of repeating sequences
        java.util.List<Integer> repeats = new java.util.ArrayList<>();
        int i = 0;
        while (i < n) {
            int j = i;
            while (j < n && password.charAt(j) == password.charAt(i)) j++;
            int len = j - i;
            if (len >= 3) repeats.add(len);
            i = j;
        }

        if (n < 6) {
            return Math.max(missing, 6 - n);
        } else if (n <= 20) {
            int replace = 0;
            for (int len : repeats) replace += len / 3;
            return Math.max(missing, replace);
        } else {
            int delete = n - 20;
            int[] modCounts = new int[3];
            int replace = 0;
            for (int len : repeats) {
                replace += len / 3;
                modCounts[len % 3]++;
            }

            // Use deletions to reduce replacements
            int use = Math.min(modCounts[0], delete);
            replace -= use;
            delete -= use;

            use = Math.min(modCounts[1] * 2, delete);
            replace -= use / 2;
            delete -= use;

            replace -= delete / 3;
            if (replace < 0) replace = 0;

            return (n - 20) + Math.max(missing, replace);
        }
    }
}
```

## Python

```python
class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        n = len(password)
        has_lower = any('a' <= c <= 'z' for c in password)
        has_upper = any('A' <= c <= 'Z' for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing_type = 3 - (has_lower + has_upper + has_digit)

        # collect repeating sequences lengths
        repeats = []
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            length = j - i
            if length >= 3:
                repeats.append(length)
            i = j

        if n < 6:
            return max(missing_type, 6 - n)

        replace = 0
        if n <= 20:
            # no deletions needed, just replacements
            for l in repeats:
                replace += l // 3
            return max(missing_type, replace)

        # n > 20 : need deletions
        delete = n - 20

        # first reduce sequences where len % 3 == 0
        for idx in range(len(repeats)):
            if delete <= 0:
                break
            if repeats[idx] >= 3 and repeats[idx] % 3 == 0:
                dec = min(delete, 1)
                repeats[idx] -= dec
                delete -= dec

        # then sequences where len % 3 == 1
        for idx in range(len(repeats)):
            if delete <= 0:
                break
            if repeats[idx] >= 3 and repeats[idx] % 3 == 1:
                dec = min(delete, 2)
                repeats[idx] -= dec
                delete -= dec

        # finally, any sequence, remove in chunks of 3
        for idx in range(len(repeats)):
            if delete <= 0:
                break
            if repeats[idx] >= 3:
                # we can delete up to length-2 characters without eliminating the repeat entirely
                need = repeats[idx] - 2
                dec = min(delete, need)
                repeats[idx] -= dec
                delete -= dec

        replace = 0
        for l in repeats:
            if l >= 3:
                replace += l // 3

        return (n - 20) + max(missing_type, replace)
```

## Python3

```python
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        has_lower = any('a' <= c <= 'z' for c in password)
        has_upper = any('A' <= c <= 'Z' for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing_types = 3 - (has_lower + has_upper + has_digit)

        # Find repeating sequences
        repeats = []
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            length = j - i
            if length >= 3:
                repeats.append(length)
            i = j

        if n < 6:
            return max(missing_types, 6 - n)

        if n <= 20:
            replace = sum(l // 3 for l in repeats)
            return max(missing_types, replace)

        # n > 20
        delete_needed = n - 20
        total_replace = sum(l // 3 for l in repeats)

        cnt_mod = [0, 0, 0]  # counts of sequences with len%3 == 0,1,2
        for l in repeats:
            cnt_mod[l % 3] += 1

        # Use deletions to reduce replacements
        # First, target mod 0 sequences (need 1 deletion per reduction)
        use = min(cnt_mod[0], delete_needed)
        total_replace -= use
        delete_needed -= use
        cnt_mod[0] -= use

        # Next, target mod 1 sequences (need 2 deletions per reduction)
        use = min(cnt_mod[1] * 2, delete_needed)
        total_replace -= use // 2
        delete_needed -= use
        cnt_mod[1] -= use // 2

        # Remaining deletions affect all groups; each 3 deletions reduce one replacement
        total_replace -= delete_needed // 3
        # Ensure non-negative
        if total_replace < 0:
            total_replace = 0

        return (n - 20) + max(missing_types, total_replace)
```

## C

```c
#include <string.h>
#include <stdbool.h>

int strongPasswordChecker(char* password) {
    int n = strlen(password);
    bool hasLower = false, hasUpper = false, hasDigit = false;
    for (int i = 0; i < n; ++i) {
        if (password[i] >= 'a' && password[i] <= 'z') hasLower = true;
        else if (password[i] >= 'A' && password[i] <= 'Z') hasUpper = true;
        else if (password[i] >= '0' && password[i] <= '9') hasDigit = true;
    }
    int missing = (!hasLower) + (!hasUpper) + (!hasDigit);
    
    // collect repeating sequences
    int lens[50];
    int m = 0;
    for (int i = 0; i < n;) {
        int j = i;
        while (j < n && password[j] == password[i]) ++j;
        int len = j - i;
        if (len >= 3) lens[m++] = len;
        i = j;
    }
    
    if (n < 6) {
        return missing > (6 - n) ? missing : (6 - n);
    } else if (n <= 20) {
        int replace = 0;
        for (int i = 0; i < m; ++i) replace += lens[i] / 3;
        return missing > replace ? missing : replace;
    } else {
        int over_len = n - 20;
        int replace = 0;
        for (int i = 0; i < m; ++i) replace += lens[i] / 3;
        
        // first, reduce replacements by deletions in sequences where len % 3 == 0
        for (int i = 0; i < m && over_len > 0; ++i) {
            if (lens[i] < 3) continue;
            if (lens[i] % 3 != 0) continue;
            lens[i]--;
            over_len--;
            replace--; // one deletion reduces a needed replacement
        }
        // second, sequences where len % 3 == 1
        for (int i = 0; i < m && over_len > 0; ++i) {
            if (lens[i] < 3) continue;
            if (lens[i] % 3 != 1) continue;
            int del = over_len >= 2 ? 2 : over_len;
            lens[i] -= del;
            over_len -= del;
            if (del == 2) replace--; // two deletions reduce a replacement
        }
        // third, remaining sequences
        for (int i = 0; i < m && over_len > 0; ++i) {
            if (lens[i] < 3) continue;
            int can_del = lens[i] - 2;
            int del = over_len < can_del ? over_len : can_del;
            replace -= del / 3;
            over_len -= del;
        }
        // any leftover deletions just reduce length
        return (n - 20) + (missing > replace ? missing : replace);
    }
}
```

## Csharp

```csharp
public class Solution {
    public int StrongPasswordChecker(string password) {
        int n = password.Length;
        bool hasLower = false, hasUpper = false, hasDigit = false;
        foreach (char c in password) {
            if (c >= 'a' && c <= 'z') hasLower = true;
            else if (c >= 'A' && c <= 'Z') hasUpper = true;
            else if (c >= '0' && c <= '9') hasDigit = true;
        }
        int missingTypes = (hasLower ? 0 : 1) + (hasUpper ? 0 : 1) + (hasDigit ? 0 : 1);

        // Find repeating sequences
        var repeats = new System.Collections.Generic.List<int>();
        for (int i = 0; i < n;) {
            int j = i;
            while (j < n && password[j] == password[i]) j++;
            int len = j - i;
            if (len >= 3) repeats.Add(len);
            i = j;
        }

        if (n < 6) {
            return System.Math.Max(missingTypes, 6 - n);
        }

        int replace = 0;
        int[] modCounts = new int[3]; // counts of sequences by length % 3
        foreach (int len in repeats) {
            replace += len / 3;
            modCounts[len % 3]++;
        }

        if (n <= 20) {
            return System.Math.Max(missingTypes, replace);
        }

        int deletions = n - 20;
        // Use deletions to reduce replacements
        // First, target sequences where len % 3 == 0 (need 1 deletion per reduction)
        int use = System.Math.Min(modCounts[0], deletions);
        replace -= use;
        deletions -= use;

        // Next, target sequences where len % 3 == 1 (need 2 deletions per reduction)
        use = System.Math.Min(modCounts[1] * 2, deletions);
        replace -= use / 2;
        deletions -= use;

        // Remaining deletions can reduce replacements by 3 deletions each
        replace -= deletions / 3;

        if (replace < 0) replace = 0;

        return (n - 20) + System.Math.Max(missingTypes, replace);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} password
 * @return {number}
 */
var strongPasswordChecker = function(password) {
    const n = password.length;
    let missing = 0;
    if (!/[a-z]/.test(password)) missing++;
    if (!/[A-Z]/.test(password)) missing++;
    if (!/[0-9]/.test(password)) missing++;

    // count repeating sequences
    let replace = 0;      // total replacements needed for repeats
    let oneMod = 0;       // counts of sequences where len % 3 == 0
    let twoMod = 0;       // counts of sequences where len % 3 == 1

    for (let i = 0; i < n;) {
        let j = i;
        while (j < n && password[j] === password[i]) j++;
        const len = j - i;
        if (len >= 3) {
            replace += Math.floor(len / 3);
            if (len % 3 === 0) oneMod++;
            else if (len % 3 === 1) twoMod++;
        }
        i = j;
    }

    if (n < 6) {
        return Math.max(missing, 6 - n);
    } else if (n <= 20) {
        return Math.max(missing, replace);
    } else {
        let deleteCount = n - 20;

        // Use deletions on sequences where len % 3 == 0
        let use = Math.min(oneMod, deleteCount);
        replace -= use;
        deleteCount -= use;

        // Use deletions on sequences where len % 3 == 1 (need two deletions to reduce a replacement)
        use = Math.min(twoMod * 2, deleteCount);
        replace -= Math.floor(use / 2);
        deleteCount -= use;

        // Remaining deletions can reduce replacements by three deletions per reduction
        replace -= Math.floor(deleteCount / 3);

        if (replace < 0) replace = 0;
        return (n - 20) + Math.max(missing, replace);
    }
};
```

## Typescript

```typescript
function strongPasswordChecker(password: string): number {
    const n = password.length;
    let hasLower = false, hasUpper = false, hasDigit = false;
    for (const ch of password) {
        if (ch >= 'a' && ch <= 'z') hasLower = true;
        else if (ch >= 'A' && ch <= 'Z') hasUpper = true;
        else if (ch >= '0' && ch <= '9') hasDigit = true;
    }
    const missingTypes = (hasLower ? 0 : 1) + (hasUpper ? 0 : 1) + (hasDigit ? 0 : 1);
    if (n < 6) {
        return Math.max(missingTypes, 6 - n);
    }

    // collect lengths of repeating sequences
    const repeats: number[] = [];
    let i = 0;
    while (i < n) {
        let j = i;
        while (j < n && password[j] === password[i]) j++;
        const len = j - i;
        if (len >= 3) repeats.push(len);
        i = j;
    }

    let replace = 0;
    for (const len of repeats) {
        replace += Math.floor(len / 3);
    }

    if (n <= 20) {
        return Math.max(missingTypes, replace);
    }

    const deleteCount = n - 20;
    let remainDelete = deleteCount;

    // Reduce sequences where len % 3 == 0
    for (let idx = 0; idx < repeats.length && remainDelete > 0; idx++) {
        if (repeats[idx] >= 3 && repeats[idx] % 3 === 0) {
            repeats[idx]--;
            remainDelete--;
            replace--; // one replacement saved
        }
    }

    // Reduce sequences where len % 3 == 1
    for (let idx = 0; idx < repeats.length && remainDelete > 0; idx++) {
        if (repeats[idx] >= 3 && repeats[idx] % 3 === 1) {
            const del = Math.min(2, remainDelete);
            repeats[idx] -= del;
            remainDelete -= del;
            if (del === 2) replace--; // saved one replacement
        }
    }

    // Use remaining deletions on the rest of the sequences
    replace = Math.max(0, replace - Math.floor(remainDelete / 3));

    return deleteCount + Math.max(missingTypes, replace);
}
```

## Php

```php
class Solution {

    /**
     * @param String $password
     * @return Integer
     */
    function strongPasswordChecker($password) {
        $n = strlen($password);
        $hasLower = preg_match('/[a-z]/', $password) ? 1 : 0;
        $hasUpper = preg_match('/[A-Z]/', $password) ? 1 : 0;
        $hasDigit = preg_match('/[0-9]/', $password) ? 1 : 0;
        $missingTypes = 3 - ($hasLower + $hasUpper + $hasDigit);

        // Find repeating sequences
        $repeats = [];
        $i = 2;
        while ($i < $n) {
            if ($password[$i] === $password[$i-1] && $password[$i-1] === $password[$i-2]) {
                $len = 3;
                while ($i + 1 < $n && $password[$i+1] === $password[$i]) {
                    $len++;
                    $i++;
                }
                $repeats[] = $len;
            }
            $i++;
        }

        if ($n < 6) {
            return max($missingTypes, 6 - $n);
        }

        // Initial replacements needed for repeats
        $replace = 0;
        foreach ($repeats as $len) {
            $replace += intdiv($len, 3);
        }

        if ($n <= 20) {
            return max($missingTypes, $replace);
        }

        // Need deletions
        $delete = $n - 20;

        // Optimize deletions on repeats
        $lens = $repeats;
        usort($lens, function($a, $b) {
            return ($a % 3) <=> ($b % 3);
        });

        // First pass: use deletions to reduce replacements efficiently
        foreach ($lens as &$len) {
            if ($delete <= 0) break;
            if ($len < 3) continue;
            $mod = $len % 3;
            $need = $mod === 0 ? 1 : ($mod === 1 ? 2 : 3);
            $del = min($need, $delete);
            $len -= $del;
            $delete -= $del;
        }
        // Second pass: apply any remaining deletions
        foreach ($lens as &$len) {
            if ($delete <= 0) break;
            if ($len < 3) continue;
            $del = min($delete, $len - 2);
            $len -= $del;
            $delete -= $del;
        }

        // Recalculate replacements after deletions
        $replace = 0;
        foreach ($lens as $len) {
            if ($len >= 3) {
                $replace += intdiv($len, 3);
            }
        }

        return ($n - 20) + max($missingTypes, $replace);
    }
}
```

## Swift

```swift
class Solution {
    func strongPasswordChecker(_ password: String) -> Int {
        let n = password.count
        var hasLower = false, hasUpper = false, hasDigit = false
        for ch in password {
            if ch.isLowercase { hasLower = true }
            else if ch.isUppercase { hasUpper = true }
            else if ch.isNumber { hasDigit = true }
        }
        let missingTypes = (hasLower ? 0 : 1) + (hasUpper ? 0 : 1) + (hasDigit ? 0 : 1)
        
        var repeats = [Int]()
        let chars = Array(password)
        var i = 0
        while i < n {
            var j = i
            while j < n && chars[j] == chars[i] {
                j += 1
            }
            let len = j - i
            if len >= 3 { repeats.append(len) }
            i = j
        }
        
        if n < 6 {
            return max(missingTypes, 6 - n)
        } else if n <= 20 {
            var replace = 0
            for len in repeats {
                replace += len / 3
            }
            return max(missingTypes, replace)
        } else {
            let overLen = n - 20
            var replace = 0
            var cntMod = [0, 0, 0]   // counts of sequences with length % 3 == 0,1,2
            for len in repeats {
                replace += len / 3
                cntMod[len % 3] += 1
            }
            var deletions = overLen
            
            let use0 = min(cntMod[0], deletions)
            replace -= use0
            deletions -= use0
            
            let use1 = min(cntMod[1] * 2, deletions)
            replace -= use1 / 2
            deletions -= use1
            
            replace -= deletions / 3
            if replace < 0 { replace = 0 }
            
            return overLen + max(missingTypes, replace)
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun strongPasswordChecker(password: String): Int {
        val n = password.length
        var hasLower = false
        var hasUpper = false
        var hasDigit = false
        for (c in password) {
            when {
                c.isLowerCase() -> hasLower = true
                c.isUpperCase() -> hasUpper = true
                c.isDigit() -> hasDigit = true
            }
        }
        val missingTypes = (if (hasLower) 0 else 1) + (if (hasUpper) 0 else 1) + (if (hasDigit) 0 else 1)

        if (n < 6) {
            return maxOf(missingTypes, 6 - n)
        }

        // Find repeating sequences of length >=3
        val repeats = mutableListOf<Int>()
        var i = 2
        while (i < n) {
            if (password[i] == password[i - 1] && password[i - 1] == password[i - 2]) {
                var j = i + 1
                while (j < n && password[j] == password[i]) {
                    j++
                }
                val len = j - (i - 2)
                repeats.add(len)
                i = j
            } else {
                i++
            }
        }

        if (n <= 20) {
            var replace = 0
            for (len in repeats) {
                replace += len / 3
            }
            return maxOf(missingTypes, replace)
        }

        var delete = n - 20
        var replace = 0
        val cnt = IntArray(3)
        for (len in repeats) {
            replace += len / 3
            cnt[len % 3]++
        }

        // Reduce replacements by deletions targeting sequences with specific mod values
        var use = minOf(cnt[0], delete)
        replace -= use
        delete -= use

        use = minOf(cnt[1] * 2, delete)
        replace -= use / 2
        delete -= use

        replace -= delete / 3
        if (replace < 0) replace = 0

        return (n - 20) + maxOf(missingTypes, replace)
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int strongPasswordChecker(String password) {
    int n = password.length;
    bool hasLower = false, hasUpper = false, hasDigit = false;
    for (int i = 0; i < n; i++) {
      int c = password.codeUnitAt(i);
      if (c >= 97 && c <= 122) hasLower = true;
      else if (c >= 65 && c <= 90) hasUpper = true;
      else if (c >= 48 && c <= 57) hasDigit = true;
    }
    int missingTypes = (hasLower ? 0 : 1) + (hasUpper ? 0 : 1) + (hasDigit ? 0 : 1);

    List<int> repeats = [];
    int i = 0;
    while (i < n) {
      int j = i;
      while (j < n && password[j] == password[i]) j++;
      int len = j - i;
      if (len >= 3) repeats.add(len);
      i = j;
    }

    int replace = 0;
    for (int len in repeats) {
      replace += len ~/ 3;
    }

    if (n < 6) {
      return max(missingTypes, 6 - n);
    } else if (n <= 20) {
      return max(missingTypes, replace);
    } else {
      int del = n - 20;
      repeats.sort((a, b) => (a % 3).compareTo(b % 3));

      for (int idx = 0; idx < repeats.length && del > 0; idx++) {
        int len = repeats[idx];
        if (len < 3) continue;
        int mod = len % 3;
        if (mod == 0) {
          int use = min(1, del);
          repeats[idx] -= use;
          del -= use;
          replace--;
        } else if (mod == 1) {
          int use = min(2, del);
          if (use == 2) {
            repeats[idx] -= use;
            del -= use;
            replace--;
          }
        }
      }

      replace = max(0, replace - del ~/ 3);
      return (n - 20) + max(missingTypes, replace);
    }
  }
}
```

## Golang

```go
func strongPasswordChecker(password string) int {
    n := len(password)
    lower, upper, digit := false, false, false
    for i := 0; i < n; i++ {
        c := password[i]
        if c >= 'a' && c <= 'z' {
            lower = true
        } else if c >= 'A' && c <= 'Z' {
            upper = true
        } else if c >= '0' && c <= '9' {
            digit = true
        }
    }
    missing := 0
    if !lower {
        missing++
    }
    if !upper {
        missing++
    }
    if !digit {
        missing++
    }

    // collect lengths of repeating sequences
    repeats := []int{}
    for i := 0; i < n; {
        j := i
        for j < n && password[j] == password[i] {
            j++
        }
        length := j - i
        if length >= 3 {
            repeats = append(repeats, length)
        }
        i = j
    }

    if n < 6 {
        needInsert := 6 - n
        if missing > needInsert {
            return missing
        }
        return needInsert
    }

    if n <= 20 {
        replace := 0
        for _, l := range repeats {
            replace += l / 3
        }
        if replace < missing {
            return missing
        }
        return replace
    }

    // n > 20
    deleteCount := n - 20
    // Reduce replacements using deletions
    // First handle groups where len%3 == 0 (need 1 deletion to reduce a replacement)
    for i := 0; i < len(repeats) && deleteCount > 0; i++ {
        if repeats[i] < 3 || repeats[i]%3 != 0 {
            continue
        }
        repeats[i]--
        deleteCount--
    }
    // Then groups where len%3 == 1 (need 2 deletions)
    for i := 0; i < len(repeats) && deleteCount > 0; i++ {
        if repeats[i] < 3 || repeats[i]%3 != 1 {
            continue
        }
        del := 2
        if deleteCount < del {
            del = deleteCount
        }
        repeats[i] -= del
        deleteCount -= del
    }
    // Finally, any groups (need 3 deletions per reduction)
    for i := 0; i < len(repeats) && deleteCount > 0; i++ {
        if repeats[i] < 3 {
            continue
        }
        // maximum deletions we can apply while keeping length >= 2
        maxDel := repeats[i] - 2
        if maxDel > deleteCount {
            maxDel = deleteCount
        }
        // reduce in chunks of 3 as much as possible
        del := maxDel
        repeats[i] -= del
        deleteCount -= del
    }

    replace := 0
    for _, l := range repeats {
        if l >= 3 {
            replace += l / 3
        }
    }

    if replace < missing {
        replace = missing
    }
    return (n - 20) + replace
}
```

## Ruby

```ruby
def strong_password_checker(password)
  n = password.length
  missing_lower = password =~ /[a-z]/ ? 0 : 1
  missing_upper = password =~ /[A-Z]/ ? 0 : 1
  missing_digit = password =~ /\d/ ? 0 : 1
  missing_types = missing_lower + missing_upper + missing_digit

  repeat_lengths = []
  i = 0
  while i < n
    j = i
    j += 1 while j < n && password[j] == password[i]
    len = j - i
    repeat_lengths << len if len >= 3
    i = j
  end

  if n < 6
    return [missing_types, 6 - n].max
  elsif n <= 20
    replace_needed = repeat_lengths.sum { |len| len / 3 }
    return [missing_types, replace_needed].max
  else
    delete_needed = n - 20

    # Reduce replacements by deletions: prioritize sequences with mod 0, then 1, then 2.
    repeat_lengths.each_with_index do |len, idx|
      break if delete_needed == 0
      next unless len >= 3 && (len % 3).zero?
      del = [delete_needed, 1].min
      repeat_lengths[idx] -= del
      delete_needed -= del
    end

    repeat_lengths.each_with_index do |len, idx|
      break if delete_needed == 0
      next unless len >= 3 && (len % 3) == 1
      del = [delete_needed, 2].min
      repeat_lengths[idx] -= del
      delete_needed -= del
    end

    repeat_lengths.each_with_index do |len, idx|
      while delete_needed > 0 && repeat_lengths[idx] >= 3
        del = [delete_needed, 3].min
        repeat_lengths[idx] -= del
        delete_needed -= del
      end
    end

    replace_needed = repeat_lengths.sum { |len| len / 3 }
    return (n - 20) + [missing_types, replace_needed].max
  end
end
```

## Scala

```scala
object Solution {
    def strongPasswordChecker(password: String): Int = {
        val n = password.length
        var hasLower = false
        var hasUpper = false
        var hasDigit = false
        for (ch <- password) {
            if (ch >= 'a' && ch <= 'z') hasLower = true
            else if (ch >= 'A' && ch <= 'Z') hasUpper = true
            else if (ch >= '0' && ch <= '9') hasDigit = true
        }
        val missingTypes = (if (!hasLower) 1 else 0) + (if (!hasUpper) 1 else 0) + (if (!hasDigit) 1 else 0)

        if (n < 6) {
            return Math.max(missingTypes, 6 - n)
        }

        // collect lengths of repeating sequences
        val repeats = scala.collection.mutable.ArrayBuffer[Int]()
        var i = 0
        while (i < n) {
            val startChar = password.charAt(i)
            var j = i
            while (j < n && password.charAt(j) == startChar) {
                j += 1
            }
            val len = j - i
            if (len >= 3) repeats += len
            i = j
        }

        if (n <= 20) {
            var replace = 0
            for (len <- repeats) replace += len / 3
            return Math.max(missingTypes, replace)
        } else {
            val overLen = n - 20
            var delete = overLen

            // sort groups by length % 3 to prioritize deletions that reduce replacements most
            val arr = repeats.toArray
            java.util.Arrays.sort(arr, (a: Int, b: Int) => (a % 3) - (b % 3))

            for (idx <- arr.indices if delete > 0) {
                var len = arr(idx)
                if (len < 3) {
                    // nothing to do
                } else {
                    val mod = len % 3
                    if (mod == 0 && delete >= 1) {
                        arr(idx) = len - 1
                        delete -= 1
                    } else if (mod == 1 && delete >= 2) {
                        arr(idx) = len - 2
                        delete -= 2
                    } else if (mod == 2 && delete >= 3) {
                        arr(idx) = len - 3
                        delete -= 3
                    }
                }
            }

            var replace = 0
            for (len <- arr) {
                if (len >= 3) replace += len / 3
            }

            // any remaining deletions can further reduce replacements
            replace -= Math.min(replace, delete / 3)

            overLen + Math.max(missingTypes, replace)
        }
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn strong_password_checker(password: String) -> i32 {
        let bytes = password.as_bytes();
        let n = bytes.len();

        // character type checks
        let mut has_lower = false;
        let mut has_upper = false;
        let mut has_digit = false;
        for &c in bytes {
            if c >= b'a' && c <= b'z' {
                has_lower = true;
            } else if c >= b'A' && c <= b'Z' {
                has_upper = true;
            } else if c >= b'0' && c <= b'9' {
                has_digit = true;
            }
        }
        let missing = (!has_lower as i32) + (!has_upper as i32) + (!has_digit as i32);

        // collect lengths of repeating sequences
        let mut repeats: Vec<i32> = Vec::new();
        let mut i = 0usize;
        while i < n {
            let mut j = i + 1;
            while j < n && bytes[j] == bytes[i] {
                j += 1;
            }
            let len = (j - i) as i32;
            if len >= 3 {
                repeats.push(len);
            }
            i = j;
        }

        if n < 6 {
            return std::cmp::max(missing, (6 - n) as i32);
        } else if n <= 20 {
            let replace: i32 = repeats.iter().map(|&len| len / 3).sum();
            return std::cmp::max(missing, replace);
        } else {
            let mut delete = (n - 20) as i32;
            // prioritize deletions that reduce replacements most
            repeats.sort_by_key(|&len| len % 3);

            // first: sequences where len % 3 == 0
            for idx in 0..repeats.len() {
                if delete == 0 { break; }
                if repeats[idx] % 3 == 0 {
                    let del = std::cmp::min(1, delete);
                    repeats[idx] -= del;
                    delete -= del;
                }
            }

            // second: sequences where len % 3 == 1
            for idx in 0..repeats.len() {
                if delete == 0 { break; }
                if repeats[idx] % 3 == 1 {
                    let del = std::cmp::min(2, delete);
                    repeats[idx] -= del;
                    delete -= del;
                }
            }

            // third: any remaining deletions
            for idx in 0..repeats.len() {
                if delete == 0 { break; }
                while repeats[idx] >= 3 && delete > 0 {
                    let del = std::cmp::min(3, delete);
                    repeats[idx] -= del;
                    delete -= del;
                }
            }

            let replace: i32 = repeats.iter().map(|&len| len / 3).sum();
            (n as i32 - 20) + std::cmp::max(missing, replace)
        }
    }
}
```

## Racket

```racket
(define/contract (strong-password-checker password)
  (-> string? exact-integer?)
  (let* ((n (string-length password))
         ;; character type flags
         (lower #f) (upper #f) (digit #f))
    ;; scan for required types
    (for ([i (in-range n)])
      (let ((c (string-ref password i)))
        (cond [(and (char>=? c #\a) (char<=? c #\z)) (set! lower #t)]
              [(and (char>=? c #\A) (char<=? c #\Z)) (set! upper #t)]
              [(and (char>=? c #\0) (char<=? c #\9)) (set! digit #t)])))
    (define missing (+ (if lower 0 1) (if upper 0 1) (if digit 0 1)))
    ;; collect lengths of repeating sequences (len >=3)
    (define repeats '())
    (let loop ((i 0) (prev #\null) (cnt 0))
      (if (= i n)
          (when (>= cnt 3) (set! repeats (cons cnt repeats)))
          (let ((c (string-ref password i)))
            (if (and (> cnt 0) (char=? c prev))
                (loop (+ i 1) c (+ cnt 1))
                (begin
                  (when (>= cnt 3) (set! repeats (cons cnt repeats)))
                  (loop (+ i 1) c 1))))))
    (cond
      [(< n 6)
       (max missing (- 6 n))]
      [(<= n 20)
       (define replace 0)
       (for ([len repeats])
         (set! replace (+ replace (quotient len 3))))
       (max missing replace)]
      [else ; n > 20
       (define del-needed (- n 20))
       (define v (list->vector repeats))
       (define m (vector-length v))
       ;; first pass: sequences where len % 3 == 0
       (for ([i (in-range m)])
         (when (> del-needed 0)
           (let ((len (vector-ref v i)))
             (when (and (>= len 3) (= (modulo len 3) 0))
               (set! len (- len 1))
               (vector-set! v i len)
               (set! del-needed (- del-needed 1))))))
       ;; second pass: sequences where len % 3 == 1
       (for ([i (in-range m)])
         (when (> del-needed 0)
           (let ((len (vector-ref v i)))
             (when (and (>= len 3) (= (modulo len 3) 1))
               (define d (min 2 del-needed))
               (set! len (- len d))
               (vector-set! v i len)
               (set! del-needed (- del_needed d))))))
       ;; third pass: apply remaining deletions anywhere
       (for ([i (in-range m)])
         (when (> del-needed 0)
           (let ((len (vector-ref v i)))
             (when (>= len 3)
               (define d (min (- len 2) del-needed))
               (set! len (- len d))
               (vector-set! v i len)
               (set! del_needed (- del_needed d))))))
       ;; compute replacements after deletions
       (define replace 0)
       (for ([i (in-range m)])
         (let ((len (vector-ref v i)))
           (when (>= len 3)
             (set! replace (+ replace (quotient len 3))))))
       (+ (- n 20) (max missing replace)))])))
```

## Erlang

```erlang
-module(solution).
-export([strong_password_checker/1]).

-spec strong_password_checker(Password :: unicode:unicode_binary()) -> integer().
strong_password_checker(Password) ->
    Chars = unicode:characters_to_list(Password),
    N = length(Chars),

    HasLower = lists:any(fun(C) -> C >= $a, C =< $z end, Chars),
    HasUpper = lists:any(fun(C) -> C >= $A, C =< $Z end, Chars),
    HasDigit = lists:any(fun(C) -> C >= $0, C =< $9 end, Chars),

    MissingTypes = (if not HasLower -> 1; true -> 0 end)
                 + (if not HasUpper -> 1; true -> 0 end)
                 + (if not HasDigit -> 1; true -> 0 end),

    case N of
        Len when Len < 6 ->
            max(MissingTypes, 6 - Len);
        Len when Len =< 20 ->
            {ReplaceSum, _C0, _C1, _C2} = repeat_info(Chars),
            max(MissingTypes, ReplaceSum);
        _ ->
            DeleteNeeded = N - 20,
            {ReplaceSum, C0, C1, C2} = repeat_info(Chars),

            Use0 = min(C0, DeleteNeeded),
            RepAfter0 = ReplaceSum - Use0,
            DelAfter0 = DeleteNeeded - Use0,

            Use1 = min(C1, DelAfter0 div 2),
            RepAfter1 = RepAfter0 - Use1,
            DelAfter1 = DelAfter0 - Use1 * 2,

            Use2 = DelAfter1 div 3,
            FinalReplace = max(RepAfter1 - Use2, 0),

            DeleteNeeded + max(MissingTypes, FinalReplace)
    end.

-spec repeat_info([integer()]) -> {integer(), integer(), integer(), integer()}.
repeat_info([]) ->
    {0,0,0,0};
repeat_info([First|Rest]) ->
    process(Rest, First, 1, 0, 0, 0, 0).

-spec process([integer()], integer(), integer(),
              integer(), integer(), integer(), integer())
      -> {integer(), integer(), integer(), integer()}.
process([], _Prev, RunLen, RepAcc, C0, C1, C2) ->
    if RunLen >= 3 ->
            Rep = RepAcc + (RunLen div 3),
            Mod = RunLen rem 3,
            case Mod of
                0 -> {Rep, C0+1, C1,   C2};
                1 -> {Rep, C0,   C1+1, C2};
                2 -> {Rep, C0,   C1,   C2+1}
            end;
       true ->
            {RepAcc, C0, C1, C2}
    end;
process([H|T], Prev, RunLen, RepAcc, C0, C1, C2) when H =:= Prev ->
    process(T, Prev, RunLen + 1, RepAcc, C0, C1, C2);
process([H|T], _Prev, RunLen, RepAcc, C0, C1, C2) ->
    {RepAcc1, C0a, C1a, C2a} =
        if RunLen >= 3 ->
                Rep = RepAcc + (RunLen div 3),
                Mod = RunLen rem 3,
                case Mod of
                    0 -> {Rep, C0+1, C1,   C2};
                    1 -> {Rep, C0,   C1+1, C2};
                    2 -> {Rep, C0,   C1,   C2+1}
                end;
           true ->
                {RepAcc, C0, C1, C2}
        end,
    process(T, H, 1, RepAcc1, C0a, C1a, C2a).

-spec min(integer(), integer()) -> integer().
min(A,B) -> erlang:min(A,B).

-spec max(integer(), integer()) -> integer().
max(A,B) -> erlang:max(A,B).
```

## Elixir

```elixir
defmodule Solution do
  @spec strong_password_checker(password :: String.t()) :: integer()
  def strong_password_checker(password) do
    n = String.length(password)

    has_lower = Regex.match?(~r/[a-z]/, password)
    has_upper = Regex.match?(~r/[A-Z]/, password)
    has_digit = Regex.match?(~r/\d/, password)

    missing =
      (if has_lower, do: 0, else: 1) +
        (if has_upper, do: 0, else: 1) +
        (if has_digit, do: 0, else: 1)

    # collect lengths of repeating sequences (len >= 3)
    chars = String.graphemes(password)

    {lens_rev, {_prev, cnt}} =
      Enum.reduce(chars, {[], {nil, 0}}, fn ch, {lens, {prev, c}} ->
        if ch == prev do
          {lens, {prev, c + 1}}
        else
          lens2 = if c >= 3, do: [c | lens], else: lens
          {lens2, {ch, 1}}
        end
      end)

    lengths =
      if cnt >= 3, do: [cnt | lens_rev], else: lens_rev

    cond do
      n < 6 ->
        max(missing, 6 - n)

      n <= 20 ->
        replace = Enum.reduce(lengths, 0, fn l, acc -> acc + div(l, 3) end)
        max(missing, replace)

      true ->
        delete_needed = n - 20

        {replace, cnt0, cnt1} =
          Enum.reduce(lengths, {0, 0, 0}, fn l, {rep, c0, c1} ->
            rep2 = rep + div(l, 3)

            case rem(l, 3) do
              0 -> {rep2, c0 + 1, c1}
              1 -> {rep2, c0, c1 + 1}
              _ -> {rep2, c0, c1}
            end
          end)

        use0 = min(cnt0, delete_needed)
        replace1 = replace - use0
        del_left1 = delete_needed - use0

        use1 = min(cnt1, div(del_left1, 2))
        replace2 = replace1 - use1
        del_left2 = del_left1 - use1 * 2

        replace3 = replace2 - div(del_left2, 3)
        final_replace = max(replace3, 0)

        delete_needed + max(missing, final_replace)
    end
  end
end
```
