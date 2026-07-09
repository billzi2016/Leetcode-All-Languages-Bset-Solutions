# 0087. Scramble String

## Cpp

```cpp
class Solution {
public:
    bool isScramble(string s1, string s2) {
        int n = s1.size();
        if (n != (int)s2.size()) return false;
        // Optional quick check: character counts must match
        vector<int> cnt(26, 0);
        for (char c : s1) ++cnt[c - 'a'];
        for (char c : s2) --cnt[c - 'a'];
        for (int v : cnt) if (v != 0) return false;

        // dp[len][i][j] -> bool
        vector<vector<vector<char>>> dp(n + 1,
            vector<vector<char>>(n, vector<char>(n, 0)));

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                dp[1][i][j] = (s1[i] == s2[j]);

        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i + len <= n; ++i) {
                for (int j = 0; j + len <= n; ++j) {
                    bool ok = false;
                    for (int k = 1; k < len && !ok; ++k) {
                        // without swap
                        if (dp[k][i][j] && dp[len - k][i + k][j + k]) {
                            ok = true;
                            break;
                        }
                        // with swap
                        if (dp[k][i][j + len - k] && dp[len - k][i + k][j]) {
                            ok = true;
                            break;
                        }
                    }
                    dp[len][i][j] = ok;
                }
            }
        }
        return dp[n][0][0];
    }
};
```

## Java

```java
class Solution {
    public boolean isScramble(String s1, String s2) {
        int n = s1.length();
        if (n != s2.length()) return false;
        // dp[len][i][j] : whether s1[i..i+len-1] can be scrambled to s2[j..j+len-1]
        boolean[][][] dp = new boolean[n + 1][n][n];
        // base case len = 1
        for (int i = 0; i < n; i++) {
            char c1 = s1.charAt(i);
            for (int j = 0; j < n; j++) {
                dp[1][i][j] = c1 == s2.charAt(j);
            }
        }
        // lengths from 2 to n
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len <= n; i++) {
                for (int j = 0; j + len <= n; j++) {
                    boolean can = false;
                    // try all possible split positions
                    for (int k = 1; k < len && !can; k++) {
                        // without swap
                        if (dp[k][i][j] && dp[len - k][i + k][j + k]) {
                            can = true;
                            break;
                        }
                        // with swap
                        if (dp[k][i][j + len - k] && dp[len - k][i + k][j]) {
                            can = true;
                            break;
                        }
                    }
                    dp[len][i][j] = can;
                }
            }
        }
        return dp[n][0][0];
    }
}
```

## Python

```python
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        n = len(s1)
        if s1 == s2:
            return True
        # quick character count check
        if sorted(s1) != sorted(s2):
            return False

        # dp[length][i][j] -> bool
        dp = [[[False] * n for _ in range(n)] for __ in range(n + 1)]

        # base case length = 1
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]

        # build up for lengths >= 2
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    # try all possible splits
                    for split in range(1, length):
                        if (dp[split][i][j] and dp[length - split][i + split][j + split]) \
                           or (dp[split][i][j + length - split] and dp[length - split][i + split][j]):
                            dp[length][i][j] = True
                            break  # no need to check further splits

        return dp[n][0][0]
```

## Python3

```python
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        n = len(s1)
        if sorted(s1) != sorted(s2):
            return False

        dp = [[[False] * n for _ in range(n)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    ok = False
                    for l in range(1, length):
                        if (dp[l][i][j] and dp[length - l][i + l][j + l]) or \
                           (dp[l][i][j + length - l] and dp[length - l][i + l][j]):
                            ok = True
                            break
                    dp[length][i][j] = ok

        return dp[n][0][0]
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool isScramble(char* s1, char* s2) {
    int n = strlen(s1);
    if (n != (int)strlen(s2)) return false;
    static bool dp[31][30][30];
    // base case length 1
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            dp[1][i][j] = (s1[i] == s2[j]);
        }
    }
    // lengths from 2 to n
    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i + len <= n; ++i) {
            for (int j = 0; j + len <= n; ++j) {
                dp[len][i][j] = false;
                for (int k = 1; k < len; ++k) {
                    // without swap
                    if (dp[k][i][j] && dp[len - k][i + k][j + k]) {
                        dp[len][i][j] = true;
                        break;
                    }
                    // with swap
                    if (dp[k][i][j + len - k] && dp[len - k][i + k][j]) {
                        dp[len][i][j] = true;
                        break;
                    }
                }
            }
        }
    }
    return dp[n][0][0];
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsScramble(string s1, string s2)
    {
        if (s1.Length != s2.Length) return false;
        int n = s1.Length;
        if (n == 0) return true;

        // Quick character count check to prune impossible cases
        var cnt = new int[26];
        for (int i = 0; i < n; i++)
        {
            cnt[s1[i] - 'a']++;
            cnt[s2[i] - 'a']--;
        }
        foreach (var c in cnt) if (c != 0) return false;

        bool[,,] dp = new bool[n + 1, n, n];

        // Base case: length 1
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                dp[1, i, j] = s1[i] == s2[j];
            }
        }

        // Build up DP for lengths >= 2
        for (int len = 2; len <= n; len++)
        {
            for (int i = 0; i <= n - len; i++)
            {
                for (int j = 0; j <= n - len; j++)
                {
                    bool can = false;
                    for (int k = 1; k < len && !can; k++)
                    {
                        // No swap case
                        if (dp[k, i, j] && dp[len - k, i + k, j + k])
                        {
                            can = true;
                            break;
                        }
                        // Swap case
                        if (dp[k, i, j + len - k] && dp[len - k, i + k, j])
                        {
                            can = true;
                            break;
                        }
                    }
                    dp[len, i, j] = can;
                }
            }
        }

        return dp[n, 0, 0];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var isScramble = function(s1, s2) {
    if (s1.length !== s2.length) return false;
    const n = s1.length;

    // Quick character count check
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < n; i++) {
        cnt[s1.charCodeAt(i) - 97]++;
        cnt[s2.charCodeAt(i) - 97]--;
    }
    if (cnt.some(v => v !== 0)) return false;

    // dp[length][i][j] -> whether s1[i..i+length) can be scrambled to s2[j..j+length)
    const dp = Array.from({ length: n + 1 }, () =>
        Array.from({ length: n }, () => new Array(n).fill(false))
    );

    // Base case: length = 1
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            dp[1][i][j] = s1[i] === s2[j];
        }
    }

    // Build up DP for lengths >= 2
    for (let len = 2; len <= n; len++) {
        for (let i = 0; i + len <= n; i++) {
            for (let j = 0; j + len <= n; j++) {
                let ok = false;
                for (let k = 1; k < len && !ok; k++) {
                    // No swap case
                    if (dp[k][i][j] && dp[len - k][i + k][j + k]) {
                        ok = true;
                        break;
                    }
                    // Swap case
                    if (dp[k][i][j + len - k] && dp[len - k][i + k][j]) {
                        ok = true;
                        break;
                    }
                }
                dp[len][i][j] = ok;
            }
        }
    }

    return dp[n][0][0];
};
```

## Typescript

```typescript
function isScramble(s1: string, s2: string): boolean {
    const n = s1.length;
    if (n !== s2.length) return false;
    // quick character count check
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < n; ++i) {
        cnt[s1.charCodeAt(i) - 97]++;
        cnt[s2.charCodeAt(i) - 97]--;
    }
    if (cnt.some(v => v !== 0)) return false;

    // dp[len][i][j]: whether s1[i..i+len) can be scrambled to s2[j..j+len)
    const dp: boolean[][][] = Array.from({ length: n + 1 }, () =>
        Array.from({ length: n }, () => new Array(n).fill(false))
    );

    // base case len = 1
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            dp[1][i][j] = s1[i] === s2[j];
        }
    }

    // build up lengths
    for (let len = 2; len <= n; ++len) {
        for (let i = 0; i + len <= n; ++i) {
            for (let j = 0; j + len <= n; ++j) {
                let can = false;
                for (let k = 1; k < len && !can; ++k) { // split length k
                    // without swap
                    if (dp[k][i][j] && dp[len - k][i + k][j + k]) {
                        can = true;
                        break;
                    }
                    // with swap
                    if (dp[k][i][j + len - k] && dp[len - k][i + k][j]) {
                        can = true;
                        break;
                    }
                }
                dp[len][i][j] = can;
            }
        }
    }

    return dp[n][0][0];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function isScramble($s1, $s2) {
        $n = strlen($s1);
        if ($n !== strlen($s2)) {
            return false;
        }
        if ($s1 === $s2) {
            return true;
        }

        // dp[length][i][j] => bool
        $dp = [];

        // base case length = 1
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $dp[1][$i][$j] = ($s1[$i] === $s2[$j]);
            }
        }

        // lengths from 2 to n
        for ($len = 2; $len <= $n; $len++) {
            for ($i = 0; $i <= $n - $len; $i++) {
                for ($j = 0; $j <= $n - $len; $j++) {
                    $dp[$len][$i][$j] = false;
                    // try all possible splits
                    for ($k = 1; $k < $len; $k++) {
                        // without swap
                        if (!empty($dp[$k][$i][$j]) && !empty($dp[$len - $k][$i + $k][$j + $k])) {
                            $dp[$len][$i][$j] = true;
                            break;
                        }
                        // with swap
                        if (!empty($dp[$k][$i][$j + $len - $k]) && !empty($dp[$len - $k][$i + $k][$j])) {
                            $dp[$len][$i][$j] = true;
                            break;
                        }
                    }
                }
            }
        }

        return $dp[$n][0][0] ?? false;
    }
}
```

## Swift

```swift
class Solution {
    func isScramble(_ s1: String, _ s2: String) -> Bool {
        let n = s1.count
        if n != s2.count { return false }
        if s1 == s2 { return true }
        
        let arr1 = Array(s1)
        let arr2 = Array(s2)
        
        // dp[length][i][j] indicates whether s1[i..i+length) can be scrambled to s2[j..j+length)
        var dp = Array(repeating: Array(repeating: Array(repeating: false, count: n), count: n), count: n + 1)
        
        // Base case length = 1
        for i in 0..<n {
            for j in 0..<n {
                dp[1][i][j] = arr1[i] == arr2[j]
            }
        }
        
        if n == 1 { return dp[1][0][0] }
        
        // Build up DP for lengths from 2 to n
        if n > 1 {
            for length in 2...n {
                for i in 0...(n - length) {
                    for j in 0...(n - length) {
                        var can = false
                        for split in 1..<length {
                            // No swap case
                            if dp[split][i][j] && dp[length - split][i + split][j + split] {
                                can = true
                                break
                            }
                            // Swap case
                            if dp[split][i][j + length - split] && dp[length - split][i + split][j] {
                                can = true
                                break
                            }
                        }
                        dp[length][i][j] = can
                    }
                }
            }
        }
        
        return dp[n][0][0]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isScramble(s1: String, s2: String): Boolean {
        val n = s1.length
        if (n != s2.length) return false

        // dp[length][i][j] indicates whether s1[i..i+length-1] can be scrambled to s2[j..j+length-1]
        val dp = Array(n + 1) { Array(n) { BooleanArray(n) } }

        // Base case: length == 1
        for (i in 0 until n) {
            for (j in 0 until n) {
                dp[1][i][j] = s1[i] == s2[j]
            }
        }

        // Build up DP for lengths from 2 to n
        for (len in 2..n) {
            for (i in 0..n - len) {
                for (j in 0..n - len) {
                    var can = false
                    for (k in 1 until len) {
                        // No swap case
                        if (dp[k][i][j] && dp[len - k][i + k][j + k]) {
                            can = true
                            break
                        }
                        // Swap case
                        if (dp[k][i][j + len - k] && dp[len - k][i + k][j]) {
                            can = true
                            break
                        }
                    }
                    dp[len][i][j] = can
                }
            }
        }

        return dp[n][0][0]
    }
}
```

## Dart

```dart
class Solution {
  bool isScramble(String s1, String s2) {
    int n = s1.length;
    if (n != s2.length) return false;
    // dp[length][i][j] -> whether s1[i..i+length) can be scrambled to s2[j..j+length)
    List<List<List<bool>>> dp = List.generate(
        n + 1, (_) => List.generate(n, (_) => List.filled(n, false)));

    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        dp[1][i][j] = s1[i] == s2[j];
      }
    }

    for (int len = 2; len <= n; ++len) {
      for (int i = 0; i <= n - len; ++i) {
        for (int j = 0; j <= n - len; ++j) {
          bool can = false;
          for (int split = 1; split < len && !can; ++split) {
            // without swap
            if (dp[split][i][j] &&
                dp[len - split][i + split][j + split]) {
              can = true;
              break;
            }
            // with swap
            if (dp[split][i][j + len - split] &&
                dp[len - split][i + split][j]) {
              can = true;
              break;
            }
          }
          dp[len][i][j] = can;
        }
      }
    }

    return dp[n][0][0];
  }
}
```

## Golang

```go
func isScramble(s1 string, s2 string) bool {
    if len(s1) != len(s2) {
        return false
    }
    n := len(s1)
    // dp[length][i][j] indicates whether s1[i:i+length] can be scrambled to s2[j:j+length]
    dp := make([][][]bool, n+1)
    for l := 0; l <= n; l++ {
        dp[l] = make([][]bool, n)
        for i := 0; i < n; i++ {
            dp[l][i] = make([]bool, n)
        }
    }

    // Base case: length == 1
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            dp[1][i][j] = s1[i] == s2[j]
        }
    }

    // Build up DP for lengths from 2 to n
    for length := 2; length <= n; length++ {
        for i := 0; i+length <= n; i++ {
            for j := 0; j+length <= n; j++ {
                for split := 1; split < length; split++ {
                    // No swap case
                    if dp[split][i][j] && dp[length-split][i+split][j+split] {
                        dp[length][i][j] = true
                        break
                    }
                    // Swap case
                    if dp[split][i][j+length-split] && dp[length-split][i+split][j] {
                        dp[length][i][j] = true
                        break
                    }
                }
            }
        }
    }

    return dp[n][0][0]
}
```

## Ruby

```ruby
def is_scramble(s1, s2)
  n = s1.length
  return false unless n == s2.length
  return false unless s1.chars.sort == s2.chars.sort

  dp = Array.new(n + 1) { Array.new(n) { Array.new(n, false) } }

  (0...n).each do |i|
    (0...n).each do |j|
      dp[1][i][j] = (s1[i] == s2[j])
    end
  end

  (2..n).each do |len|
    (0..(n - len)).each do |i|
      (0..(n - len)).each do |j|
        found = false
        (1...len).each do |k|
          if dp[k][i][j] && dp[len - k][i + k][j + k]
            found = true
            break
          end
          if dp[k][i][j + len - k] && dp[len - k][i + k][j]
            found = true
            break
          end
        end
        dp[len][i][j] = found
      end
    end
  end

  dp[n][0][0]
end
```

## Scala

```scala
object Solution {
  def isScramble(s1: String, s2: String): Boolean = {
    val n = s1.length
    if (n != s2.length) return false
    if (s1 == s2) return true
    // quick character count check
    if (s1.sorted != s2.sorted) return false

    val dp = Array.ofDim[Boolean](n + 1, n, n)

    for (i <- 0 until n; j <- 0 until n) {
      dp(1)(i)(j) = s1.charAt(i) == s2.charAt(j)
    }

    for (len <- 2 to n) {
      for (i <- 0 to n - len) {
        for (j <- 0 to n - len) {
          var found = false
          var split = 1
          while (split < len && !found) {
            if ((dp(split)(i)(j) && dp(len - split)(i + split)(j + split)) ||
                (dp(split)(i)(j + len - split) && dp(len - split)(i + split)(j))) {
              found = true
            }
            split += 1
          }
          dp(len)(i)(j) = found
        }
      }
    }

    dp(n)(0)(0)
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn is_scramble(s1: String, s2: String) -> bool {
        let n = s1.len();
        if n != s2.len() {
            return false;
        }
        if s1 == s2 {
            return true;
        }

        // Quick character count check
        let mut cnt = [0i32; 26];
        for &b in s1.as_bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        for &b in s2.as_bytes() {
            cnt[(b - b'a') as usize] -= 1;
        }
        if cnt.iter().any(|&x| x != 0) {
            return false;
        }

        let bytes1 = s1.as_bytes();
        let bytes2 = s2.as_bytes();

        // dp[len][i][j] == true if s1[i..i+len] can be scrambled to s2[j..j+len]
        let mut dp = vec![vec![vec![false; n]; n]; n + 1];

        for i in 0..n {
            for j in 0..n {
                dp[1][i][j] = bytes1[i] == bytes2[j];
            }
        }

        for len in 2..=n {
            for i in 0..=n - len {
                for j in 0..=n - len {
                    let mut ok = false;
                    for k in 1..len {
                        if (dp[k][i][j] && dp[len - k][i + k][j + k])
                            || (dp[k][i][j + len - k] && dp[len - k][i + k][j])
                        {
                            ok = true;
                            break;
                        }
                    }
                    dp[len][i][j] = ok;
                }
            }
        }

        dp[n][0][0]
    }
}
```

## Racket

```racket
(define/contract (is-scramble s1 s2)
  (-> string? string? boolean?)
  (let* ((n (string-length s1)))
    (if (not (= n (string-length s2))) 
        #f
        (let ((dp (make-vector (+ n 1) #f)))
          ;; allocate dp[len][i][j] matrices
          (for ([len (+ n 1)])
            (let ((mat (make-vector n #f)))
              (for ([i n])
                (vector-set! mat i (make-vector n #f)))
              (vector-set! dp len mat)))
          ;; base case length = 1
          (for ([i (in-range n)])
            (for ([j (in-range n)])
              (let ((row (vector-ref (vector-ref dp 1) i)))
                (vector-set! row j (= (string-ref s1 i) (string-ref s2 j))))))
          ;; DP over lengths
          (for ([len (in-range 2 (+ n 1))])
            (for ([i (in-range 0 (+ (- n len) 1))])
              (for ([j (in-range 0 (+ (- n len) 1))])
                (let ((found #f))
                  (for ([k (in-range 1 len)] #:break found)
                    (define left k)
                    (define right (- len k))
                    ;; no swap case
                    (when (and (vector-ref (vector-ref (vector-ref dp left) i) j)
                               (vector-ref (vector-ref (vector-ref dp right) (+ i left)) (+ j left)))
                      (set! found #t))
                    ;; swap case
                    (when (and (not found)
                               (vector-ref (vector-ref (vector-ref dp left) i) (+ j right))
                               (vector-ref (vector-ref (vector-ref dp right) (+ i left)) j))
                      (set! found #t)))
                  (when found
                    (let ((row (vector-ref (vector-ref dp len) i)))
                      (vector-set! row j #t)))))))
          ;; final answer
          (vector-ref (vector-ref (vector-ref dp n) 0) 0)))))
```

## Erlang

```erlang
-spec is_scramble(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
is_scramble(S1, S2) ->
    L1 = binary_to_list(S1),
    L2 = binary_to_list(S2),
    N = length(L1),
    case N == length(L2) of
        false -> false;
        true ->
            DP0 = maps:new(),
            DP1 = init_base(N, L1, L2, DP0),
            DPF = fill_dp(N, DP1),
            maps:get({N, 0, 0}, DPF, false)
    end.

%% initialize dp for length 1
init_base(N, L1, L2, DP) ->
    lists:foldl(
      fun(I, AccI) ->
          lists:foldl(
            fun(J, AccJ) ->
                C1 = lists:nth(I + 1, L1),
                C2 = lists:nth(J + 1, L2),
                maps:put({1, I, J}, C1 == C2, AccJ)
            end,
            AccI,
            seq(0, N - 1))
      end,
      DP,
      seq(0, N - 1)).

%% fill dp for lengths 2..N
fill_dp(N, DP) ->
    lists:foldl(
      fun(Len, AccLen) -> update_len(Len, N, AccLen) end,
      DP,
      seq(2, N)).

update_len(Len, N, DP) ->
    MaxIdx = N - Len,
    lists:foldl(
      fun(I, AccI) ->
          lists:foldl(
            fun(J, AccJ) ->
                Val = check_split(Len, I, J, DP),
                maps:put({Len, I, J}, Val, AccJ)
            end,
            AccI,
            seq(0, MaxIdx))
      end,
      DP,
      seq(0, MaxIdx)).

check_split(Len, I, J, DP) ->
    check_split(1, Len - 1, Len, I, J, DP).

check_split(NewLen, Max, Len, I, J, DP) when NewLen =< Max ->
    case (maps:get({NewLen, I, J}, DP) andalso maps:get({Len - NewLen, I + NewLen, J + NewLen}, DP))
          orelse (maps:get({NewLen, I, J + Len - NewLen}, DP) andalso maps:get({Len - NewLen, I + NewLen, J}, DP)) of
        true -> true;
        false -> check_split(NewLen + 1, Max, Len, I, J, DP)
    end;
check_split(_, _, _, _, _, _) -> false.

%% helper to generate a sequence [From..To]
seq(From, To) when From =< To ->
    lists:seq(From, To);
seq(_, _) -> [].
```

## Elixir

```elixir
defmodule Solution do
  @spec is_scramble(s1 :: String.t(), s2 :: String.t()) :: boolean()
  def is_scramble(s1, s2) do
    n = byte_size(s1)

    if n != byte_size(s2) do
      false
    else
      base =
        for i <- 0..(n - 1),
            j <- 0..(n - 1) do
          {{1, i, j}, :binary.at(s1, i) == :binary.at(s2, j)}
        end
        |> Enum.into(%{})

      dp =
        Enum.reduce(2..n, base, fn len, dp_acc ->
          new_entries =
            for i <- 0..(n - len),
                j <- 0..(n - len) do
              result =
                Enum.any?(1..(len - 1), fn k ->
                  cond1 =
                    Map.get(dp_acc, {k, i, j}, false) and
                      Map.get(dp_acc, {len - k, i + k, j + k}, false)

                  cond2 =
                    Map.get(dp_acc, {k, i, j + len - k}, false) and
                      Map.get(dp_acc, {len - k, i + k, j}, false)

                  cond1 or cond2
                end)

              {{len, i, j}, result}
            end
            |> Enum.into(%{})

          Map.merge(dp_acc, new_entries)
        end)

      Map.get(dp, {n, 0, 0}, false)
    end
  end
end
```
