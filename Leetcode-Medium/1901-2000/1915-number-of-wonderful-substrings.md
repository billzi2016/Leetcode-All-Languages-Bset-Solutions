# 1915. Number of Wonderful Substrings

## Cpp

```cpp
class Solution {
public:
    long long wonderfulSubstrings(string word) {
        const int MAX_MASK = 1 << 10; // 1024
        vector<long long> cnt(MAX_MASK, 0);
        cnt[0] = 1;
        int mask = 0;
        long long ans = 0;
        for (char ch : word) {
            int bit = ch - 'a';
            mask ^= (1 << bit);
            ans += cnt[mask];
            for (int i = 0; i < 10; ++i) {
                ans += cnt[mask ^ (1 << i)];
            }
            ++cnt[mask];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long wonderfulSubstrings(String word) {
        int mask = 0;
        long[] cnt = new long[1 << 10];
        cnt[0] = 1; // empty prefix
        long ans = 0;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            mask ^= 1 << (ch - 'a');
            ans += cnt[mask]; // all even counts
            for (int b = 0; b < 10; b++) {
                ans += cnt[mask ^ (1 << b)]; // exactly one odd count
            }
            cnt[mask]++;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq = [0] * 1024  # 2^10 possible masks
        freq[0] = 1  # empty prefix
        mask = 0
        ans = 0
        for ch in word:
            mask ^= 1 << (ord(ch) - ord('a'))
            ans += freq[mask]
            # substrings with exactly one odd character
            for i in range(10):
                ans += freq[mask ^ (1 << i)]
            freq[mask] += 1
        return ans
```

## Python3

```python
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        freq = [0] * 1024  # 2^10 possible masks
        freq[0] = 1
        mask = 0
        ans = 0
        for ch in word:
            mask ^= 1 << (ord(ch) - ord('a'))
            ans += freq[mask]
            m = mask
            for i in range(10):
                ans += freq[m ^ (1 << i)]
            freq[mask] += 1
        return ans
```

## C

```c
#include <stddef.h>

long long wonderfulSubstrings(char * word){
    const int MAX_MASK = 1 << 10; // 1024
    long long freq[MAX_MASK];
    for (int i = 0; i < MAX_MASK; ++i) freq[i] = 0;
    freq[0] = 1; // empty prefix

    int mask = 0;
    long long ans = 0;

    for (char *p = word; *p != '\0'; ++p){
        int idx = *p - 'a';
        mask ^= (1 << idx);

        ans += freq[mask]; // all even
        for (int i = 0; i < 10; ++i){
            ans += freq[mask ^ (1 << i)];
        }

        freq[mask] += 1;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public long WonderfulSubstrings(string word)
    {
        const int ALPH = 10;
        int size = 1 << ALPH;
        long[] freq = new long[size];
        freq[0] = 1;

        int mask = 0;
        long ans = 0;

        foreach (char ch in word)
        {
            int bit = ch - 'a';
            mask ^= 1 << bit;

            ans += freq[mask];
            for (int i = 0; i < ALPH; ++i)
            {
                ans += freq[mask ^ (1 << i)];
            }

            freq[mask]++;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var wonderfulSubstrings = function(word) {
    const freq = new Uint32Array(1 << 10);
    freq[0] = 1;
    let mask = 0;
    let ans = 0;
    for (let i = 0; i < word.length; ++i) {
        const bit = word.charCodeAt(i) - 97; // 'a' -> 0
        mask ^= (1 << bit);
        ans += freq[mask];
        for (let b = 0; b < 10; ++b) {
            ans += freq[mask ^ (1 << b)];
        }
        freq[mask] += 1;
    }
    return ans;
};
```

## Typescript

```typescript
function wonderfulSubstrings(word: string): number {
    const MAX_MASK = 1 << 10; // 1024
    const freq = new Array<number>(MAX_MASK).fill(0);
    freq[0] = 1;
    let mask = 0;
    let ans = 0;

    for (let i = 0; i < word.length; ++i) {
        const bit = word.charCodeAt(i) - 97; // 'a' -> 0
        mask ^= (1 << bit);

        // substrings with all even counts
        ans += freq[mask];

        // substrings with exactly one odd count
        for (let b = 0; b < 10; ++b) {
            ans += freq[mask ^ (1 << b)];
        }

        freq[mask] += 1;
    }

    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param String $word
     * @return Integer
     */
    function wonderfulSubstrings($word) {
        $freq = array_fill(0, 1 << 10, 0);
        $freq[0] = 1;
        $mask = 0;
        $ans = 0;
        $len = strlen($word);
        for ($i = 0; $i < $len; $i++) {
            $ch = $word[$i];
            $mask ^= (1 << (ord($ch) - 97));
            $ans += $freq[$mask];
            for ($b = 0; $b < 10; $b++) {
                $tmp = $mask ^ (1 << $b);
                $ans += $freq[$tmp];
            }
            $freq[$mask] += 1;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func wonderfulSubstrings(_ word: String) -> Int {
        var freq = [Int](repeating: 0, count: 1 << 10)
        var mask = 0
        var result = 0
        freq[0] = 1
        
        for byte in word.utf8 {
            let idx = Int(byte - 97) // 'a' ASCII is 97
            mask ^= (1 << idx)
            
            // substrings with all even counts
            result += freq[mask]
            
            // substrings with exactly one odd count
            var i = 0
            while i < 10 {
                result += freq[mask ^ (1 << i)]
                i += 1
            }
            
            freq[mask] += 1
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun wonderfulSubstrings(word: String): Long {
        val freq = LongArray(1 shl 10)
        var mask = 0
        var ans = 0L
        freq[0] = 1L
        for (ch in word) {
            val bit = ch.code - 'a'.code
            mask = mask xor (1 shl bit)
            ans += freq[mask]
            for (i in 0 until 10) {
                ans += freq[mask xor (1 shl i)]
            }
            freq[mask]++
        }
        return ans
    }
}
```

## Golang

```go
func wonderfulSubstrings(word string) int64 {
    var freq [1024]int64
    mask := 0
    freq[0] = 1
    var ans int64

    for _, ch := range word {
        idx := int(ch - 'a')
        mask ^= 1 << idx

        ans += freq[mask]
        for i := 0; i < 10; i++ {
            ans += freq[mask^(1<<i)]
        }

        freq[mask]++
    }
    return ans
}
```

## Ruby

```ruby
# @param {String} word
# @return {Integer}
def wonderful_substrings(word)
  freq = Hash.new(0)
  mask = 0
  ans = 0
  freq[0] = 1

  word.each_byte do |b|
    idx = b - 97 # 'a'.ord == 97
    mask ^= (1 << idx)

    ans += freq[mask]
    10.times do |i|
      ans += freq[mask ^ (1 << i)]
    end

    freq[mask] += 1
  end

  ans
end
```

## Scala

```scala
object Solution {
    def wonderfulSubstrings(word: String): Long = {
        val freq = new Array[Long](1 << 10)
        var mask = 0
        var ans: Long = 0L
        freq(0) = 1L
        for (c <- word) {
            val idx = c - 'a'
            mask ^= (1 << idx)
            ans += freq(mask)
            var i = 0
            while (i < 10) {
                ans += freq(mask ^ (1 << i))
                i += 1
            }
            freq(mask) += 1L
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn wonderful_substrings(word: String) -> i64 {
        let mut cnt = vec![0i64; 1 << 10];
        cnt[0] = 1;
        let mut mask: usize = 0;
        let mut ans: i64 = 0;
        for b in word.bytes() {
            let idx = (b - b'a') as usize;
            mask ^= 1 << idx;
            ans += cnt[mask];
            for k in 0..10 {
                ans += cnt[mask ^ (1 << k)];
            }
            cnt[mask] += 1;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (wonderful-substrings word)
  (-> string? exact-integer?)
  (let* ([cnt (make-vector 1024 0)]
         [_ (vector-set! cnt 0 1)]
         [mask 0]
         [ans 0])
    (for ([c (in-string word)])
      (set! mask
            (bitwise-xor mask
                         (arithmetic-shift 1
                                            (- (char->integer c)
                                               (char->integer #\a)))))
      ;; substrings with all even counts
      (set! ans (+ ans (vector-ref cnt mask)))
      ;; substrings with exactly one odd count
      (for ([i (in-range 10)])
        (let ([m2 (bitwise-xor mask (arithmetic-shift 1 i))])
          (set! ans (+ ans (vector-ref cnt m2)))))
      (vector-set! cnt mask (+ 1 (vector-ref cnt mask))))
    ans))
```
