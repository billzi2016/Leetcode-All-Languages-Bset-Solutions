# 1737. Change Minimum Characters to Satisfy One of Three Conditions

## Cpp

```cpp
class Solution {
public:
    int minCharacters(string a, string b) {
        const int ALPH = 26;
        vector<int> cntA(ALPH,0), cntB(ALPH,0);
        for(char ch: a) cntA[ch-'a']++;
        for(char ch: b) cntB[ch-'a']++;
        int nA = a.size(), nB = b.size();
        // prefix sums
        vector<int> prefA(ALPH,0), prefB(ALPH,0);
        prefA[0] = cntA[0];
        prefB[0] = cntB[0];
        for(int i=1;i<ALPH;i++){
            prefA[i] = prefA[i-1] + cntA[i];
            prefB[i] = prefB[i-1] + cntB[i];
        }
        int ans = INT_MAX;
        // condition 3: both strings become same single letter
        for(int c=0;c<ALPH;c++){
            int ops = (nA - cntA[c]) + (nB - cntB[c]);
            ans = min(ans, ops);
        }
        // conditions 1 and 2 using splits between i and i+1, i from 0 to 24
        for(int i=0;i<ALPH-1;i++){
            int aGreater = nA - prefA[i];   // chars in a > i
            int bLessEq = prefB[i];         // chars in b <= i
            ans = min(ans, aGreater + bLessEq); // condition 1: a < b
            
            int bGreater = nB - prefB[i];
            int aLessEq = prefA[i];
            ans = min(ans, bGreater + aLessEq); // condition 2: b < a
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minCharacters(String a, String b) {
        int[] cntA = new int[26];
        int[] cntB = new int[26];
        for (int i = 0; i < a.length(); i++) cntA[a.charAt(i) - 'a']++;
        for (int i = 0; i < b.length(); i++) cntB[b.charAt(i) - 'a']++;

        int totalA = a.length();
        int totalB = b.length();

        int[] prefA = new int[26];
        int[] prefB = new int[26];
        prefA[0] = cntA[0];
        prefB[0] = cntB[0];
        for (int i = 1; i < 26; i++) {
            prefA[i] = prefA[i - 1] + cntA[i];
            prefB[i] = prefB[i - 1] + cntB[i];
        }

        int ans = Integer.MAX_VALUE;

        // Condition 1: every char in a is less than every char in b
        for (int i = 0; i < 25; i++) {
            int changeA = totalA - prefA[i]; // chars > i in a
            int changeB = prefB[i];          // chars <= i in b
            ans = Math.min(ans, changeA + changeB);
        }

        // Condition 2: every char in b is less than every char in a
        for (int i = 0; i < 25; i++) {
            int changeB = totalB - prefB[i]; // chars > i in b
            int changeA = prefA[i];          // chars <= i in a
            ans = Math.min(ans, changeA + changeB);
        }

        // Condition 3: both strings consist of only one distinct (same) letter
        for (int i = 0; i < 26; i++) {
            int ops = (totalA - cntA[i]) + (totalB - cntB[i]);
            ans = Math.min(ans, ops);
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minCharacters(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        cntA = [0] * 26
        cntB = [0] * 26
        for ch in a:
            cntA[ord(ch) - 97] += 1
        for ch in b:
            cntB[ord(ch) - 97] += 1

        totalA, totalB = len(a), len(b)

        # prefix sums
        prefA = [0] * 26
        prefB = [0] * 26
        cur = 0
        for i in range(26):
            cur += cntA[i]
            prefA[i] = cur
        cur = 0
        for i in range(26):
            cur += cntB[i]
            prefB[i] = cur

        # condition 3: both strings become same single letter
        ans = float('inf')
        for i in range(26):
            ops = (totalA - cntA[i]) + (totalB - cntB[i])
            if ops < ans:
                ans = ops

        # condition 1: max(a) < min(b)
        for t in range(25):  # t from 'a' to 'y'
            ops = (totalA - prefA[t]) + prefB[t]
            if ops < ans:
                ans = ops

        # condition 2: max(b) < min(a)
        for t in range(25):
            ops = (totalB - prefB[t]) + prefA[t]
            if ops < ans:
                ans = ops

        return ans
```

## Python3

```python
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        cntA = [0] * 26
        cntB = [0] * 26
        for ch in a:
            cntA[ord(ch) - 97] += 1
        for ch in b:
            cntB[ord(ch) - 97] += 1

        prefA = [0] * 26
        prefB = [0] * 26
        prefA[0] = cntA[0]
        prefB[0] = cntB[0]
        for i in range(1, 26):
            prefA[i] = prefA[i - 1] + cntA[i]
            prefB[i] = prefB[i - 1] + cntB[i]

        lenA, lenB = len(a), len(b)
        ans = float('inf')

        # condition 1: all a < all b
        for t in range(25):  # up to 'y'
            ops = (lenA - prefA[t]) + prefB[t]
            if ops < ans:
                ans = ops

        # condition 2: all b < all a
        for t in range(25):
            ops = (lenB - prefB[t]) + prefA[t]
            if ops < ans:
                ans = ops

        # condition 3: both strings consist of the same single letter
        for i in range(26):
            ops = (lenA - cntA[i]) + (lenB - cntB[i])
            if ops < ans:
                ans = ops

        return ans
```

## C

```c
#include <string.h>

int minCharacters(char* a, char* b) {
    int cntA[26] = {0}, cntB[26] = {0};
    for (char *p = a; *p; ++p) cntA[*p - 'a']++;
    for (char *p = b; *p; ++p) cntB[*p - 'a']++;

    int lenA = 0, lenB = 0;
    for (int i = 0; i < 26; ++i) {
        lenA += cntA[i];
        lenB += cntB[i];
    }

    int prefA[26], prefB[26];
    int sumA = 0, sumB = 0;
    for (int i = 0; i < 26; ++i) {
        sumA += cntA[i];
        prefA[i] = sumA;
        sumB += cntB[i];
        prefB[i] = sumB;
    }

    int ans = lenA + lenB; // worst case

    // Condition 1: all chars in a < all chars in b
    for (int p = 0; p < 25; ++p) {
        int ops = (lenA - prefA[p]) + prefB[p];
        if (ops < ans) ans = ops;
    }

    // Condition 2: all chars in b < all chars in a
    for (int p = 0; p < 25; ++p) {
        int ops = (lenB - prefB[p]) + prefA[p];
        if (ops < ans) ans = ops;
    }

    // Condition 3: both strings consist of the same single character
    for (int c = 0; c < 26; ++c) {
        int ops = (lenA - cntA[c]) + (lenB - cntB[c]);
        if (ops < ans) ans = ops;
    }

    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinCharacters(string a, string b)
    {
        int[] freqA = new int[26];
        int[] freqB = new int[26];

        foreach (char ch in a) freqA[ch - 'a']++;
        foreach (char ch in b) freqB[ch - 'a']++;

        int lenA = a.Length;
        int lenB = b.Length;

        int[] prefA = new int[26];
        int[] prefB = new int[26];

        prefA[0] = freqA[0];
        prefB[0] = freqB[0];
        for (int i = 1; i < 26; i++)
        {
            prefA[i] = prefA[i - 1] + freqA[i];
            prefB[i] = prefB[i - 1] + freqB[i];
        }

        int ans = int.MaxValue;

        // Condition 3: both strings consist of the same single letter
        for (int i = 0; i < 26; i++)
        {
            int ops = (lenA - freqA[i]) + (lenB - freqB[i]);
            if (ops < ans) ans = ops;
        }

        // Conditions 1 and 2: split point between letters
        for (int x = 0; x < 25; x++) // up to 'y' as split, since need a letter greater than x
        {
            int ops1 = (lenA - prefA[x]) + prefB[x]; // all a > x, all b <= x
            if (ops1 < ans) ans = ops1;

            int ops2 = (lenB - prefB[x]) + prefA[x]; // all b > x, all a <= x
            if (ops2 < ans) ans = ops2;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} a
 * @param {string} b
 * @return {number}
 */
var minCharacters = function(a, b) {
    const freqA = new Array(26).fill(0);
    const freqB = new Array(26).fill(0);
    for (let i = 0; i < a.length; ++i) {
        freqA[a.charCodeAt(i) - 97]++;
    }
    for (let i = 0; i < b.length; ++i) {
        freqB[b.charCodeAt(i) - 97]++;
    }
    const lenA = a.length;
    const lenB = b.length;

    // prefix sums: cum[i] = total count of letters <= i
    const cumA = new Array(26).fill(0);
    const cumB = new Array(26).fill(0);
    cumA[0] = freqA[0];
    cumB[0] = freqB[0];
    for (let i = 1; i < 26; ++i) {
        cumA[i] = cumA[i - 1] + freqA[i];
        cumB[i] = cumB[i - 1] + freqB[i];
    }

    let ans = Number.MAX_SAFE_INTEGER;

    // Condition 3: both strings become the same single character
    for (let c = 0; c < 26; ++c) {
        const changes = (lenA - freqA[c]) + (lenB - freqB[c]);
        if (changes < ans) ans = changes;
    }

    // Condition 1: all a chars < all b chars
    for (let i = 0; i < 25; ++i) { // split between i and i+1
        const changeA = lenA - cumA[i];   // a chars > i
        const changeB = cumB[i];          // b chars <= i
        const total = changeA + changeB;
        if (total < ans) ans = total;
    }

    // Condition 2: all b chars < all a chars
    for (let i = 0; i < 25; ++i) {
        const changeB = lenB - cumB[i];   // b chars > i
        const changeA = cumA[i];          // a chars <= i
        const total = changeA + changeB;
        if (total < ans) ans = total;
    }

    return ans;
};
```

## Typescript

```typescript
function minCharacters(a: string, b: string): number {
    const freqA = new Array(26).fill(0);
    const freqB = new Array(26).fill(0);
    for (let i = 0; i < a.length; ++i) freqA[a.charCodeAt(i) - 97]++;
    for (let i = 0; i < b.length; ++i) freqB[b.charCodeAt(i) - 97]++;

    const prefA = new Array(26).fill(0);
    const prefB = new Array(26).fill(0);
    prefA[0] = freqA[0];
    prefB[0] = freqB[0];
    for (let i = 1; i < 26; ++i) {
        prefA[i] = prefA[i - 1] + freqA[i];
        prefB[i] = prefB[i - 1] + freqB[i];
    }

    const lenA = a.length;
    const lenB = b.length;
    let ans = Number.MAX_SAFE_INTEGER;

    // Condition 3: both strings become the same single character
    for (let c = 0; c < 26; ++c) {
        const ops = (lenA - freqA[c]) + (lenB - freqB[c]);
        if (ops < ans) ans = ops;
    }

    // Conditions 1 and 2: max(a) < min(b) or max(b) < min(a)
    for (let t = 0; t < 25; ++t) {
        const ops1 = (lenA - prefA[t]) + prefB[t]; // make all a <= t, b > t
        if (ops1 < ans) ans = ops1;

        const ops2 = prefA[t] + (lenB - prefB[t]); // make all b <= t, a > t
        if (ops2 < ans) ans = ops2;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $a
     * @param String $b
     * @return Integer
     */
    function minCharacters($a, $b) {
        $lenA = strlen($a);
        $lenB = strlen($b);
        $cntA = array_fill(0, 26, 0);
        $cntB = array_fill(0, 26, 0);

        for ($i = 0; $i < $lenA; $i++) {
            $idx = ord($a[$i]) - 97;
            $cntA[$idx]++;
        }
        for ($i = 0; $i < $lenB; $i++) {
            $idx = ord($b[$i]) - 97;
            $cntB[$idx]++;
        }

        // Prefix sums
        $prefA = array_fill(0, 26, 0);
        $prefB = array_fill(0, 26, 0);
        $prefA[0] = $cntA[0];
        $prefB[0] = $cntB[0];
        for ($i = 1; $i < 26; $i++) {
            $prefA[$i] = $prefA[$i - 1] + $cntA[$i];
            $prefB[$i] = $prefB[$i - 1] + $cntB[$i];
        }

        $ans = PHP_INT_MAX;

        // Condition 3: both strings consist of a single same letter
        for ($c = 0; $c < 26; $c++) {
            $ops = ($lenA - $cntA[$c]) + ($lenB - $cntB[$c]);
            if ($ops < $ans) $ans = $ops;
        }

        // Conditions 1 and 2: using split point p (0..24)
        for ($p = 0; $p < 25; $p++) {
            // Condition 1: max(a) < min(b)
            $ops1 = ($lenA - $prefA[$p]) + $prefB[$p];
            if ($ops1 < $ans) $ans = $ops1;

            // Condition 2: max(b) < min(a)
            $ops2 = ($lenB - $prefB[$p]) + $prefA[$p];
            if ($ops2 < $ans) $ans = $ops2;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minCharacters(_ a: String, _ b: String) -> Int {
        var countA = [Int](repeating: 0, count: 26)
        var countB = [Int](repeating: 0, count: 26)
        
        for scalar in a.unicodeScalars {
            let idx = Int(scalar.value - 97)
            countA[idx] += 1
        }
        for scalar in b.unicodeScalars {
            let idx = Int(scalar.value - 97)
            countB[idx] += 1
        }
        
        let lenA = a.count
        let lenB = b.count
        
        var prefA = [Int](repeating: 0, count: 26)
        var prefB = [Int](repeating: 0, count: 26)
        prefA[0] = countA[0]
        prefB[0] = countB[0]
        for i in 1..<26 {
            prefA[i] = prefA[i - 1] + countA[i]
            prefB[i] = prefB[i - 1] + countB[i]
        }
        
        var answer = Int.max
        
        // Condition 3: both strings consist of the same single character
        for i in 0..<26 {
            let ops = (lenA - countA[i]) + (lenB - countB[i])
            if ops < answer { answer = ops }
        }
        
        // Conditions 1 and 2: strict ordering using a split point p ('a'..'y')
        for p in 0..<25 {
            // Condition 1: max(a) < min(b)
            let ops1 = (lenA - prefA[p]) + prefB[p]
            if ops1 < answer { answer = ops1 }
            
            // Condition 2: max(b) < min(a)
            let ops2 = (lenB - prefB[p]) + prefA[p]
            if ops2 < answer { answer = ops2 }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minCharacters(a: String, b: String): Int {
        val cntA = IntArray(26)
        val cntB = IntArray(26)
        for (ch in a) cntA[ch - 'a']++
        for (ch in b) cntB[ch - 'a']++

        val totalA = a.length
        val totalB = b.length

        var ans = Int.MAX_VALUE
        var cumA = 0
        var cumB = 0

        for (i in 0 until 26) {
            // Condition 3: both strings consist of only one distinct letter i
            val opsSame = (totalA - cntA[i]) + (totalB - cntB[i])
            if (opsSame < ans) ans = opsSame

            cumA += cntA[i]
            cumB += cntB[i]

            if (i < 25) {
                // Condition 1: all letters in a <= i, all letters in b > i
                val ops1 = (totalA - cumA) + cumB
                if (ops1 < ans) ans = ops1

                // Condition 2: all letters in b <= i, all letters in a > i
                val ops2 = (totalB - cumB) + cumA
                if (ops2 < ans) ans = ops2
            }
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minCharacters(String a, String b) {
    List<int> cntA = List.filled(26, 0);
    List<int> cntB = List.filled(26, 0);

    for (int i = 0; i < a.length; i++) {
      cntA[a.codeUnitAt(i) - 97]++;
    }
    for (int i = 0; i < b.length; i++) {
      cntB[b.codeUnitAt(i) - 97]++;
    }

    int totalA = a.length;
    int totalB = b.length;

    List<int> prefA = List.filled(26, 0);
    List<int> prefB = List.filled(26, 0);

    int sum = 0;
    for (int i = 0; i < 26; i++) {
      sum += cntA[i];
      prefA[i] = sum;
    }
    sum = 0;
    for (int i = 0; i < 26; i++) {
      sum += cntB[i];
      prefB[i] = sum;
    }

    int ans = 1 << 30;

    // Condition 3: both strings consist of the same single character
    for (int c = 0; c < 26; c++) {
      int changes = (totalA - cntA[c]) + (totalB - cntB[c]);
      if (changes < ans) ans = changes;
    }

    // Conditions 1 and 2: strict ordering between the two strings
    for (int t = 0; t < 25; t++) {
      int changes1 = (totalA - prefA[t]) + prefB[t]; // a chars > t, b chars <= t
      if (changes1 < ans) ans = changes1;

      int changes2 = (totalB - prefB[t]) + prefA[t]; // b chars > t, a chars <= t
      if (changes2 < ans) ans = changes2;
    }

    return ans;
  }
}
```

## Golang

```go
func minCharacters(a string, b string) int {
	cntA := [26]int{}
	cntB := [26]int{}
	for _, ch := range a {
		cntA[ch-'a']++
	}
	for _, ch := range b {
		cntB[ch-'a']++
	}

	prefA := make([]int, 26)
	prefB := make([]int, 26)

	sum := 0
	for i := 0; i < 26; i++ {
		sum += cntA[i]
		prefA[i] = sum
	}
	sum = 0
	for i := 0; i < 26; i++ {
		sum += cntB[i]
		prefB[i] = sum
	}

	totalA := len(a)
	totalB := len(b)

	const inf = int(^uint(0) >> 1) // max int
	ans := inf

	// Condition 1: all a < all b
	for t := 0; t < 25; t++ { // threshold up to 'y'
		changesA := totalA - prefA[t] // chars in a greater than t
		changesB := prefB[t]          // chars in b less or equal to t
		if cur := changesA + changesB; cur < ans {
			ans = cur
		}
	}

	// Condition 2: all b < all a
	for t := 0; t < 25; t++ {
		changesB := totalB - prefB[t] // chars in b greater than t
		changesA := prefA[t]          // chars in a less or equal to t
		if cur := changesA + changesB; cur < ans {
			ans = cur
		}
	}

	// Condition 3: both strings consist of one distinct letter
	for c := 0; c < 26; c++ {
		cur := (totalA - cntA[c]) + (totalB - cntB[c])
		if cur < ans {
			ans = cur
		}
	}

	return ans
}
```

## Ruby

```ruby
def min_characters(a, b)
  cnt_a = Array.new(26, 0)
  cnt_b = Array.new(26, 0)

  a.each_byte { |c| cnt_a[c - 97] += 1 }
  b.each_byte { |c| cnt_b[c - 97] += 1 }

  total_a = a.length
  total_b = b.length

  pref_a = Array.new(26, 0)
  pref_b = Array.new(26, 0)

  sum = 0
  cnt_a.each_with_index do |v, i|
    sum += v
    pref_a[i] = sum
  end

  sum = 0
  cnt_b.each_with_index do |v, i|
    sum += v
    pref_b[i] = sum
  end

  ans = Float::INFINITY

  # Condition 3: both strings become a single identical character
  26.times do |ch|
    ops = (total_a - cnt_a[ch]) + (total_b - cnt_b[ch])
    ans = ops if ops < ans
  end

  # Condition 1: every char in a is less than every char in b
  (0..24).each do |t|
    ops = (total_a - pref_a[t]) + pref_b[t]
    ans = ops if ops < ans
  end

  # Condition 2: every char in b is less than every char in a
  (0..24).each do |t|
    ops = (total_b - pref_b[t]) + pref_a[t]
    ans = ops if ops < ans
  end

  ans.to_i
end
```

## Scala

```scala
object Solution {
    def minCharacters(a: String, b: String): Int = {
        val freqA = new Array[Int](26)
        val freqB = new Array[Int](26)

        for (ch <- a) freqA(ch - 'a') += 1
        for (ch <- b) freqB(ch - 'a') += 1

        val prefA = new Array[Int](26)
        val prefB = new Array[Int](26)

        var sum = 0
        for (i <- 0 until 26) {
            sum += freqA(i)
            prefA(i) = sum
        }
        sum = 0
        for (i <- 0 until 26) {
            sum += freqB(i)
            prefB(i) = sum
        }

        val lenA = a.length
        val lenB = b.length
        var ans = Int.MaxValue

        // Condition 1: every char in a < every char in b
        for (c <- 0 until 25) {
            val ops = (lenA - prefA(c)) + prefB(c)
            if (ops < ans) ans = ops
        }

        // Condition 2: every char in b < every char in a
        for (c <- 0 until 25) {
            val ops = (lenB - prefB(c)) + prefA(c)
            if (ops < ans) ans = ops
        }

        // Condition 3: both strings consist of the same single letter
        for (i <- 0 until 26) {
            val ops = (lenA - freqA(i)) + (lenB - freqB(i))
            if (ops < ans) ans = ops
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_characters(a: String, b: String) -> i32 {
        let mut cnt_a = [0i32; 26];
        let mut cnt_b = [0i32; 26];

        for ch in a.bytes() {
            cnt_a[(ch - b'a') as usize] += 1;
        }
        for ch in b.bytes() {
            cnt_b[(ch - b'a') as usize] += 1;
        }

        let total_a = a.len() as i32;
        let total_b = b.len() as i32;

        // prefix sums
        let mut pref_a = [0i32; 26];
        let mut pref_b = [0i32; 26];
        let mut sum = 0;
        for i in 0..26 {
            sum += cnt_a[i];
            pref_a[i] = sum;
        }
        sum = 0;
        for i in 0..26 {
            sum += cnt_b[i];
            pref_b[i] = sum;
        }

        let mut ans = i32::MAX;

        // Condition 3: both strings consist of the same single letter
        for i in 0..26 {
            let ops = (total_a - cnt_a[i]) + (total_b - cnt_b[i]);
            if ops < ans {
                ans = ops;
            }
        }

        // Conditions 1 and 2: split point between letters (up to 'y')
        for i in 0..25 { // i from 0 ('a') to 24 ('y')
            // Condition 1: all chars in a < all chars in b
            let ops1 = (total_a - pref_a[i]) + pref_b[i];
            if ops1 < ans {
                ans = ops1;
            }
            // Condition 2: all chars in b < all chars in a
            let ops2 = (total_b - pref_b[i]) + pref_a[i];
            if ops2 < ans {
                ans = ops2;
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (min-characters a b)
  (-> string? string? exact-integer?)
  (let* ((lenA (string-length a))
         (lenB (string-length b))
         (freqA (make-vector 26 0))
         (freqB (make-vector 26 0)))
    ;; count frequencies in a
    (for ([i (in-range lenA)])
      (let* ((ch (string-ref a i))
             (idx (- (char->integer ch) (char->integer #\a))))
        (vector-set! freqA idx (+ 1 (vector-ref freqA idx)))))
    ;; count frequencies in b
    (for ([i (in-range lenB)])
      (let* ((ch (string-ref b i))
             (idx (- (char->integer ch) (char->integer #\a))))
        (vector-set! freqB idx (+ 1 (vector-ref freqB idx)))))
    ;; prefix sums
    (define prefA (make-vector 26 0))
    (define prefB (make-vector 26 0))
    (let loop ((i 0) (sumA 0) (sumB 0))
      (when (< i 26)
        (set! sumA (+ sumA (vector-ref freqA i)))
        (set! sumB (+ sumB (vector-ref freqB i)))
        (vector-set! prefA i sumA)
        (vector-set! prefB i sumB)
        (loop (+ i 1) sumA sumB)))
    ;; compute minimal operations
    (define INF 1000000000)
    (define ans INF)
    ;; condition 3: both strings consist of a single same letter
    (for ([c (in-range 26)])
      (let ((ops (+ (- lenA (vector-ref freqA c))
                    (- lenB (vector-ref freqB c)))))
        (when (< ops ans) (set! ans ops))))
    ;; condition 1 and 2: a < b or b < a
    (for ([p (in-range 25)]) ; pivots from 'a' to 'y'
      (let* ((ops1 (+ (- lenA (vector-ref prefA p))
                      (vector-ref prefB p)))   ; all a <= p, b > p
             (ops2 (+ (- lenB (vector-ref prefB p))
                      (vector-ref prefA p)))) ; all b <= p, a > p
        (when (< ops1 ans) (set! ans ops1))
        (when (< ops2 ans) (set! ans ops2))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([min_characters/2]).

-spec min_characters(A :: unicode:unicode_binary(), B :: unicode:unicode_binary()) -> integer().
min_characters(A, B) ->
    LenA = byte_size(A),
    LenB = byte_size(B),
    CountA = build_counts(A),
    CountB = build_counts(B),

    {Cond1Min, Cond2Min} = loop_min(0, LenA, LenB, CountA, CountB, 0, 0, LenA + LenB, LenA + LenB),

    Cond3Min = cond3_min(LenA, LenB, CountA, CountB),

    lists:min([Cond1Min, Cond2Min, Cond3Min]).

build_counts(Binary) ->
    Tuple0 = erlang:make_tuple(26, 0),
    build_counts(binary_to_list(Binary), Tuple0).

build_counts([], Tuple) -> Tuple;
build_counts([Char | Rest], Tuple) ->
    Index = Char - $a + 1,
    Old = element(Index, Tuple),
    NewTuple = setelement(Index, Tuple, Old + 1),
    build_counts(Rest, NewTuple).

loop_min(T, LenA, LenB, CountA, CountB, PrefA, PrefB, Min1, Min2) when T > 24 ->
    {Min1, Min2};
loop_min(T, LenA, LenB, CountA, CountB, PrefA, PrefB, Min1, Min2) ->
    Index = T + 1,
    CA = element(Index, CountA),
    CB = element(Index, CountB),

    NewPrefA = PrefA + CA,
    NewPrefB = PrefB + CB,

    ChangesA1 = LenA - NewPrefA,
    ChangesB1 = NewPrefB,
    Total1 = ChangesA1 + ChangesB1,
    NewMin1 = if Total1 < Min1 -> Total1; true -> Min1 end,

    ChangesA2 = NewPrefA,
    ChangesB2 = LenB - NewPrefB,
    Total2 = ChangesA2 + ChangesB2,
    NewMin2 = if Total2 < Min2 -> Total2; true -> Min2 end,

    loop_min(T + 1, LenA, LenB, CountA, CountB, NewPrefA, NewPrefB, NewMin1, NewMin2).

cond3_min(LenA, LenB, CountA, CountB) ->
    Values = [ (LenA - element(I, CountA)) + (LenB - element(I, CountB))
               || I <- lists:seq(1, 26) ],
    lists:min(Values).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_characters(a :: String.t(), b :: String.t()) :: integer()
  def min_characters(a, b) do
    cnt_a = count_freq(a)
    cnt_b = count_freq(b)

    len_a = String.length(a)
    len_b = String.length(b)

    # Condition 3: both strings consist of the same single character
    cond3 =
      Enum.min(
        for i <- 0..25 do
          (len_a - Enum.at(cnt_a, i)) + (len_b - Enum.at(cnt_b, i))
        end
      )

    prefix_a = prefix_sums(cnt_a)
    prefix_b = prefix_sums(cnt_b)

    max_ops = len_a + len_b

    {cond1, cond2} =
      Enum.reduce(0..24, {max_ops, max_ops}, fn k, {best1, best2} ->
        ops1 = (len_a - Enum.at(prefix_a, k)) + Enum.at(prefix_b, k)
        ops2 = Enum.at(prefix_a, k) + (len_b - Enum.at(prefix_b, k))
        {min(best1, ops1), min(best2, ops2)}
      end)

    Enum.min([cond3, cond1, cond2])
  end

  defp count_freq(str) do
    zero = List.duplicate(0, 26)

    :binary.bin_to_list(str)
    |> Enum.reduce(zero, fn byte, acc ->
      idx = byte - ?a
      List.update_at(acc, idx, &(&1 + 1))
    end)
  end

  defp prefix_sums(arr) do
    {list, _} =
      Enum.map_reduce(arr, 0, fn x, acc ->
        new = acc + x
        {new, new}
      end)

    list
  end
end
```
