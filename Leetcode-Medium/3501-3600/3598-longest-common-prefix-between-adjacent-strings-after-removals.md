# 3598. Longest Common Prefix Between Adjacent Strings After Removals

## Cpp

```cpp
class Solution {
public:
    int lcpStr(const string& a, const string& b) {
        int m = min(a.size(), b.size());
        int i = 0;
        while (i < m && a[i] == b[i]) ++i;
        return i;
    }
    
    vector<int> longestCommonPrefix(vector<string>& words) {
        int n = words.size();
        if (n == 1) return vector<int>(1, 0);
        
        vector<int> lcp(n - 1);
        for (int i = 0; i < n - 1; ++i) {
            lcp[i] = lcpStr(words[i], words[i + 1]);
        }
        
        vector<int> prefMax(n - 1), suffMax(n - 1);
        prefMax[0] = lcp[0];
        for (int i = 1; i < n - 1; ++i) {
            prefMax[i] = max(prefMax[i - 1], lcp[i]);
        }
        suffMax[n - 2] = lcp[n - 2];
        for (int i = n - 3; i >= 0; --i) {
            suffMax[i] = max(suffMax[i + 1], lcp[i]);
        }
        
        vector<int> ans(n, 0);
        for (int i = 0; i < n; ++i) {
            int left = (i - 2 >= 0) ? prefMax[i - 2] : 0;
            int right = (i + 1 <= n - 2) ? suffMax[i + 1] : 0;
            int best = max(left, right);
            if (i - 1 >= 0 && i + 1 < n) {
                int cross = lcpStr(words[i - 1], words[i + 1]);
                best = max(best, cross);
            }
            ans[i] = best;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] longestCommonPrefix(String[] words) {
        int n = words.length;
        int[] answer = new int[n];
        if (n <= 2) {
            // No adjacent pairs remain after any removal
            return answer;
        }

        int m = n - 1; // number of original adjacent pairs
        int[] pre = new int[m];
        for (int i = 0; i < m; i++) {
            pre[i] = lcp(words[i], words[i + 1]);
        }

        int[] prefMax = new int[m];
        prefMax[0] = pre[0];
        for (int i = 1; i < m; i++) {
            prefMax[i] = Math.max(prefMax[i - 1], pre[i]);
        }

        int[] suffMax = new int[m];
        suffMax[m - 1] = pre[m - 1];
        for (int i = m - 2; i >= 0; i--) {
            suffMax[i] = Math.max(suffMax[i + 1], pre[i]);
        }

        for (int i = 0; i < n; i++) {
            int left = (i - 2 >= 0) ? prefMax[i - 2] : 0;
            int right = (i + 1 <= m - 1) ? suffMax[i + 1] : 0;
            int maxOther = Math.max(left, right);

            int cross = 0;
            if (i - 1 >= 0 && i + 1 < n) {
                cross = lcp(words[i - 1], words[i + 1]);
            }

            answer[i] = Math.max(maxOther, cross);
        }
        return answer;
    }

    private int lcp(String a, String b) {
        int len = Math.min(a.length(), b.length());
        int i = 0;
        while (i < len && a.charAt(i) == b.charAt(i)) {
            i++;
        }
        return i;
    }
}
```

## Python

```python
class Solution(object):
    def longestCommonPrefix(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(words)
        if n <= 2:
            return [0] * n

        # helper to compute LCP length of two strings
        def lcp(a, b):
            m = min(len(a), len(b))
            i = 0
            while i < m and a[i] == b[i]:
                i += 1
            return i

        # precompute LCP for original adjacent pairs
        adj = [lcp(words[i], words[i + 1]) for i in range(n - 1)]

        # prefix max of adj
        pre_max = [0] * (n - 1)
        pre_max[0] = adj[0]
        for i in range(1, n - 1):
            pre_max[i] = pre_max[i - 1] if pre_max[i - 1] > adj[i] else adj[i]

        # suffix max of adj
        suf_max = [0] * (n - 1)
        suf_max[-1] = adj[-1]
        for i in range(n - 3, -1, -1):
            suf_max[i] = suf_max[i + 1] if suf_max[i + 1] > adj[i] else adj[i]

        ans = [0] * n
        for i in range(n):
            cur = 0
            # max from left side excluding pairs (i-2,i-1) that involve removed element
            if i - 2 >= 0:
                cur = pre_max[i - 2]
            # max from right side excluding pair (i,i+1)
            if i + 1 <= n - 2:
                right = suf_max[i + 1]
                if right > cur:
                    cur = right
            # new adjacent pair formed by words[i-1] and words[i+1]
            if 0 < i < n - 1:
                new_lcp = lcp(words[i - 1], words[i + 1])
                if new_lcp > cur:
                    cur = new_lcp
            ans[i] = cur

        return ans
```

## Python3

```python
class Solution:
    def longestCommonPrefix(self, words):
        from typing import List

        def lcp(a: str, b: str) -> int:
            m = min(len(a), len(b))
            i = 0
            while i < m and a[i] == b[i]:
                i += 1
            return i

        n = len(words)
        if n <= 2:
            return [0] * n

        # pre[i] = lcp between words[i] and words[i+1]
        pre = [lcp(words[i], words[i + 1]) for i in range(n - 1)]

        pref_max = [0] * (n - 1)
        cur = 0
        for i in range(n - 1):
            cur = max(cur, pre[i])
            pref_max[i] = cur

        suff_max = [0] * (n - 1)
        cur = 0
        for i in range(n - 2, -1, -1):
            cur = max(cur, pre[i])
            suff_max[i] = cur

        ans = [0] * n
        for i in range(n):
            best = 0
            # max from left side (pre indices < i-1)
            if i - 2 >= 0:
                best = max(best, pref_max[i - 2])
            # max from right side (pre indices > i)
            if i + 1 <= n - 2:
                best = max(best, suff_max[i + 1])
            # new pair formed by skipping i
            if 0 < i < n - 1:
                best = max(best, lcp(words[i - 1], words[i + 1]))
            ans[i] = best

        return ans
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* longestCommonPrefix(char** words, int wordsSize, int* returnSize) {
    *returnSize = wordsSize;
    if (wordsSize == 0) {
        return NULL;
    }
    int *ans = (int *)malloc(sizeof(int) * wordsSize);
    if (wordsSize <= 2) {
        for (int i = 0; i < wordsSize; ++i) ans[i] = 0;
        return ans;
    }

    int n = wordsSize;
    int m = n - 1;                     // number of adjacent pairs
    int *lcp = (int *)malloc(sizeof(int) * m);
    for (int i = 0; i < m; ++i) {
        const char *a = words[i];
        const char *b = words[i + 1];
        int cnt = 0;
        while (*a && *b && *a == *b) {
            ++cnt;
            ++a;
            ++b;
        }
        lcp[i] = cnt;
    }

    // prefix maximums
    int *pre = (int *)malloc(sizeof(int) * m);
    int cur = 0;
    for (int i = 0; i < m; ++i) {
        if (lcp[i] > cur) cur = lcp[i];
        pre[i] = cur;
    }
    // suffix maximums
    int *suf = (int *)malloc(sizeof(int) * m);
    cur = 0;
    for (int i = m - 1; i >= 0; --i) {
        if (lcp[i] > cur) cur = lcp[i];
        suf[i] = cur;
    }

    for (int i = 0; i < n; ++i) {
        int best = 0;

        // max from left side excluding pairs (i-1,i) and (i,i+1)
        if (i - 2 >= 0) {
            if (pre[i - 2] > best) best = pre[i - 2];
        }
        // max from right side
        if (i + 1 <= m - 1) {
            if (suf[i + 1] > best) best = suf[i + 1];
        }

        // new pair formed by words[i-1] and words[i+1]
        if (i > 0 && i < n - 1) {
            const char *a = words[i - 1];
            const char *b = words[i + 1];
            int cnt = 0;
            while (*a && *b && *a == *b) {
                ++cnt;
                ++a;
                ++b;
            }
            if (cnt > best) best = cnt;
        }

        ans[i] = best;
    }

    free(lcp);
    free(pre);
    free(suf);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] LongestCommonPrefix(string[] words)
    {
        int n = words.Length;
        int[] answer = new int[n];
        if (n == 1)
        {
            answer[0] = 0;
            return answer;
        }

        int m = n - 1; // number of original adjacent pairs
        int[] lcp = new int[m];
        for (int i = 0; i < m; i++)
            lcp[i] = CommonPrefix(words[i], words[i + 1]);

        int[] preMax = new int[m];
        int cur = 0;
        for (int i = 0; i < m; i++)
        {
            cur = Math.Max(cur, lcp[i]);
            preMax[i] = cur;
        }

        int[] suffMax = new int[m];
        cur = 0;
        for (int i = m - 1; i >= 0; i--)
        {
            cur = Math.Max(cur, lcp[i]);
            suffMax[i] = cur;
        }

        for (int i = 0; i < n; i++)
        {
            int maxOther = 0;

            // pairs completely to the left of removed index
            if (i - 2 >= 0)
                maxOther = Math.Max(maxOther, preMax[i - 2]);

            // pairs completely to the right of removed index
            if (i + 1 <= m - 1)
                maxOther = Math.Max(maxOther, suffMax[i + 1]);

            int newPair = 0;
            if (i - 1 >= 0 && i + 1 < n)
                newPair = CommonPrefix(words[i - 1], words[i + 1]);

            answer[i] = Math.Max(maxOther, newPair);
        }

        return answer;
    }

    private int CommonPrefix(string a, string b)
    {
        int len = Math.Min(a.Length, b.Length);
        int i = 0;
        while (i < len && a[i] == b[i])
            i++;
        return i;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number[]}
 */
var longestCommonPrefix = function(words) {
    const n = words.length;
    if (n === 1) return [0];
    
    // helper to compute LCP length of two strings
    const lcpLen = (a, b) => {
        const m = Math.min(a.length, b.length);
        let i = 0;
        while (i < m && a.charCodeAt(i) === b.charCodeAt(i)) i++;
        return i;
    };
    
    // precompute LCP for each adjacent pair
    const lcp = new Array(n - 1);
    for (let i = 0; i < n - 1; ++i) {
        lcp[i] = lcpLen(words[i], words[i + 1]);
    }
    
    // prefix max and suffix max of lcp array
    const preMax = new Array(n - 1);
    const sufMax = new Array(n - 1);
    for (let i = 0; i < n - 1; ++i) {
        preMax[i] = i === 0 ? lcp[0] : Math.max(preMax[i - 1], lcp[i]);
    }
    for (let i = n - 2; i >= 0; --i) {
        sufMax[i] = i === n - 2 ? lcp[i] : Math.max(sufMax[i + 1], lcp[i]);
    }
    
    const answer = new Array(n);
    for (let i = 0; i < n; ++i) {
        let maxOther = 0;
        if (i - 2 >= 0) maxOther = Math.max(maxOther, preMax[i - 2]);
        if (i + 1 <= n - 2) maxOther = Math.max(maxOther, sufMax[i + 1]);
        
        let newLcp = 0;
        if (i - 1 >= 0 && i + 1 < n) {
            newLcp = lcpLen(words[i - 1], words[i + 1]);
        }
        answer[i] = Math.max(maxOther, newLcp);
    }
    
    return answer;
};
```

## Typescript

```typescript
function longestCommonPrefix(words: string[]): number[] {
    const n = words.length;
    if (n <= 1) return new Array(n).fill(0);

    const lcpArr: number[] = new Array(n - 1);
    const lcpLen = (a: string, b: string): number => {
        const m = Math.min(a.length, b.length);
        let i = 0;
        while (i < m && a.charCodeAt(i) === b.charCodeAt(i)) i++;
        return i;
    };

    for (let i = 0; i < n - 1; ++i) {
        lcpArr[i] = lcpLen(words[i], words[i + 1]);
    }

    const preMax: number[] = new Array(n - 1);
    const sufMax: number[] = new Array(n - 1);
    for (let i = 0; i < n - 1; ++i) {
        preMax[i] = i === 0 ? lcpArr[0] : Math.max(preMax[i - 1], lcpArr[i]);
    }
    for (let i = n - 2; i >= 0; --i) {
        sufMax[i] = i === n - 2 ? lcpArr[n - 2] : Math.max(sufMax[i + 1], lcpArr[i]);
    }

    const answer: number[] = new Array(n);
    for (let i = 0; i < n; ++i) {
        let maxLeft = 0;
        if (i - 2 >= 0) maxLeft = preMax[i - 2];
        let maxRight = 0;
        if (i + 1 <= n - 2) maxRight = sufMax[i + 1];
        const maxExcl = Math.max(maxLeft, maxRight);

        let cand = 0;
        if (i > 0 && i < n - 1) {
            cand = lcpLen(words[i - 1], words[i + 1]);
        }

        answer[i] = Math.max(maxExcl, cand);
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer[]
     */
    function longestCommonPrefix($words) {
        $n = count($words);
        if ($n == 1) {
            return [0];
        }

        // helper to compute LCP length of two strings
        $lcpFunc = function(string $a, string $b): int {
            $len = min(strlen($a), strlen($b));
            for ($i = 0; $i < $len; $i++) {
                if ($a[$i] !== $b[$i]) {
                    return $i;
                }
            }
            return $len;
        };

        // precompute LCP for original adjacent pairs
        $lcpArr = [];
        for ($i = 0; $i < $n - 1; $i++) {
            $lcpArr[$i] = $lcpFunc($words[$i], $words[$i + 1]);
        }

        // prefix max
        $prefMax = [];
        $cur = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            $cur = max($cur, $lcpArr[$i]);
            $prefMax[$i] = $cur;
        }

        // suffix max
        $suffMax = array_fill(0, $n - 1, 0);
        $cur = 0;
        for ($i = $n - 2; $i >= 0; $i--) {
            $cur = max($cur, $lcpArr[$i]);
            $suffMax[$i] = $cur;
        }

        $answer = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $maxVal = 0;

            // left side max (pairs before i-1)
            if ($i - 2 >= 0) {
                $maxVal = max($maxVal, $prefMax[$i - 2]);
            }

            // right side max (pairs after i+1)
            if ($i + 1 <= $n - 2) {
                $maxVal = max($maxVal, $suffMax[$i + 1]);
            }

            // new pair formed by neighbors of removed element
            if ($i - 1 >= 0 && $i + 1 < $n) {
                $newLcp = $lcpFunc($words[$i - 1], $words[$i + 1]);
                $maxVal = max($maxVal, $newLcp);
            }

            $answer[$i] = $maxVal;
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func longestCommonPrefix(_ words: [String]) -> [Int] {
        let n = words.count
        if n == 1 { return [0] }
        
        // Convert each word to its UTF8 byte array for fast character access
        var bytesArr = [[UInt8]]()
        bytesArr.reserveCapacity(n)
        for w in words {
            bytesArr.append(Array(w.utf8))
        }
        
        let m = n - 1                     // number of adjacent pairs
        var lcpAdj = [Int](repeating: 0, count: m)
        if m > 0 {
            for i in 0..<m {
                let a = bytesArr[i]
                let b = bytesArr[i + 1]
                let minLen = a.count < b.count ? a.count : b.count
                var len = 0
                while len < minLen && a[len] == b[len] { len += 1 }
                lcpAdj[i] = len
            }
        }
        
        // Prefix and suffix maximums of lcpAdj
        var preMax = [Int](repeating: 0, count: m)
        var sufMax = [Int](repeating: 0, count: m)
        if m > 0 {
            preMax[0] = lcpAdj[0]
            if m >= 2 {
                for i in 1..<m {
                    preMax[i] = max(preMax[i - 1], lcpAdj[i])
                }
            }
            sufMax[m - 1] = lcpAdj[m - 1]
            if m >= 2 {
                var i = m - 2
                while true {
                    sufMax[i] = max(sufMax[i + 1], lcpAdj[i])
                    if i == 0 { break }
                    i -= 1
                }
            }
        }
        
        // Compute answer for each removal index
        var answer = [Int]()
        answer.reserveCapacity(n)
        for i in 0..<n {
            var best = 0
            
            // Max LCP from pairs unaffected by removing i
            if i - 2 >= 0 {
                best = max(best, preMax[i - 2])
            }
            if i + 1 <= m - 1 {               // i+1 corresponds to lcpAdj index
                best = max(best, sufMax[i + 1])
            }
            
            // New pair formed by words[i-1] and words[i+1]
            if i > 0 && i < n - 1 {
                let a = bytesArr[i - 1]
                let b = bytesArr[i + 1]
                let minLen = a.count < b.count ? a.count : b.count
                var len = 0
                while len < minLen && a[len] == b[len] { len += 1 }
                best = max(best, len)
            }
            
            answer.append(best)
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestCommonPrefix(words: Array<String>): IntArray {
        val n = words.size
        if (n == 1) return intArrayOf(0)
        // LCP for original adjacent pairs
        val adjLcp = IntArray(n - 1)
        for (i in 0 until n - 1) {
            adjLcp[i] = lcp(words[i], words[i + 1])
        }
        // Prefix max
        val prefMax = IntArray(n - 1)
        prefMax[0] = adjLcp[0]
        for (i in 1 until n - 1) {
            prefMax[i] = kotlin.math.max(prefMax[i - 1], adjLcp[i])
        }
        // Suffix max
        val suffMax = IntArray(n - 1)
        suffMax[n - 2] = adjLcp[n - 2]
        for (i in n - 3 downTo 0) {
            suffMax[i] = kotlin.math.max(suffMax[i + 1], adjLcp[i])
        }
        val answer = IntArray(n)
        for (i in 0 until n) {
            var best = 0
            if (i - 2 >= 0) best = prefMax[i - 2]
            if (i + 1 <= n - 2) best = kotlin.math.max(best, suffMax[i + 1])
            if (i > 0 && i < n - 1) {
                val newLcp = lcp(words[i - 1], words[i + 1])
                if (newLcp > best) best = newLcp
            }
            answer[i] = best
        }
        return answer
    }

    private fun lcp(a: String, b: String): Int {
        val limit = kotlin.math.min(a.length, b.length)
        var i = 0
        while (i < limit && a[i] == b[i]) i++
        return i
    }
}
```

## Dart

```dart
class Solution {
  int _lcp(String a, String b) {
    int len = a.length < b.length ? a.length : b.length;
    int i = 0;
    while (i < len && a.codeUnitAt(i) == b.codeUnitAt(i)) {
      i++;
    }
    return i;
  }

  List<int> longestCommonPrefix(List<String> words) {
    int n = words.length;
    if (n == 0) return [];
    if (n == 1) return [0];

    // LCP for original adjacent pairs
    List<int> adjLcp = List.filled(n - 1, 0);
    for (int i = 0; i < n - 1; i++) {
      adjLcp[i] = _lcp(words[i], words[i + 1]);
    }

    // Prefix max and suffix max of adjLcp
    List<int> preMax = List.filled(n - 1, 0);
    for (int i = 0; i < n - 1; i++) {
      if (i == 0) {
        preMax[i] = adjLcp[i];
      } else {
        preMax[i] = adjLcp[i] > preMax[i - 1] ? adjLcp[i] : preMax[i - 1];
      }
    }

    List<int> suffMax = List.filled(n - 1, 0);
    for (int i = n - 2; i >= 0; i--) {
      if (i == n - 2) {
        suffMax[i] = adjLcp[i];
      } else {
        suffMax[i] = adjLcp[i] > suffMax[i + 1] ? adjLcp[i] : suffMax[i + 1];
      }
    }

    List<int> answer = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      int maxWithout = 0;

      // Max from left side excluding pair (i-1,i)
      if (i - 2 >= 0) {
        maxWithout = preMax[i - 2];
      }

      // Max from right side excluding pair (i,i+1)
      if (i + 1 <= n - 2) {
        int rightMax = suffMax[i + 1];
        if (rightMax > maxWithout) maxWithout = rightMax;
      }

      // New pair formed by neighbors after removal
      if (i > 0 && i < n - 1) {
        int newLcp = _lcp(words[i - 1], words[i + 1]);
        if (newLcp > maxWithout) maxWithout = newLcp;
      }

      answer[i] = maxWithout;
    }

    return answer;
  }
}
```

## Golang

```go
func longestCommonPrefix(words []string) []int {
	n := len(words)
	if n == 0 {
		return []int{}
	}
	if n == 1 {
		return []int{0}
	}

	// helper to compute LCP length between two strings
	lcpLen := func(a, b string) int {
		minLen := len(a)
		if len(b) < minLen {
			minLen = len(b)
		}
		i := 0
		for i < minLen && a[i] == b[i] {
			i++
		}
		return i
	}

	// precompute LCP for each adjacent original pair
	lcp := make([]int, n-1)
	for i := 0; i < n-1; i++ {
		lcp[i] = lcpLen(words[i], words[i+1])
	}

	// prefix max and suffix max of lcp array
	prefMax := make([]int, n-1)
	suffMax := make([]int, n-1)

	for i := 0; i < n-1; i++ {
		if i == 0 {
			prefMax[i] = lcp[i]
		} else {
			if lcp[i] > prefMax[i-1] {
				prefMax[i] = lcp[i]
			} else {
				prefMax[i] = prefMax[i-1]
			}
		}
	}
	for i := n - 2; i >= 0; i-- {
		if i == n-2 {
			suffMax[i] = lcp[i]
		} else {
			if lcp[i] > suffMax[i+1] {
				suffMax[i] = lcp[i]
			} else {
				suffMax[i] = suffMax[i+1]
			}
		}
	}

	ans := make([]int, n)
	for i := 0; i < n; i++ {
		maxVal := 0

		// max from left side (indices <= i-2)
		if i-2 >= 0 {
			maxVal = prefMax[i-2]
		}
		// max from right side (indices >= i+1)
		if i+1 <= n-2 {
			if suffMax[i+1] > maxVal {
				maxVal = suffMax[i+1]
			}
		}
		// new adjacent pair formed by removing words[i]
		if i-1 >= 0 && i+1 < n {
			newL := lcpLen(words[i-1], words[i+1])
			if newL > maxVal {
				maxVal = newL
			}
		}
		ans[i] = maxVal
	}
	return ans
}
```

## Ruby

```ruby
def longest_common_prefix(words)
  n = words.length
  return [0] if n == 1

  m = n - 1
  lcp = Array.new(m, 0)

  (0...m).each do |i|
    a = words[i]
    b = words[i + 1]
    limit = a.length < b.length ? a.length : b.length
    j = 0
    while j < limit && a.getbyte(j) == b.getbyte(j)
      j += 1
    end
    lcp[i] = j
  end

  pref_max = Array.new(m, 0)
  suff_max = Array.new(m, 0)

  (0...m).each do |i|
    pref_max[i] = i.zero? ? lcp[0] : [pref_max[i - 1], lcp[i]].max
  end

  (m - 1).downto(0) do |i|
    suff_max[i] = i == m - 1 ? lcp[i] : [suff_max[i + 1], lcp[i]].max
  end

  ans = Array.new(n, 0)

  (0...n).each do |i|
    left_max = i - 2 >= 0 ? pref_max[i - 2] : 0
    right_max = i + 1 <= m - 1 ? suff_max[i + 1] : 0
    max_excluding = left_max > right_max ? left_max : right_max

    new_lcp = 0
    if i - 1 >= 0 && i + 1 < n
      a = words[i - 1]
      b = words[i + 1]
      limit = a.length < b.length ? a.length : b.length
      j = 0
      while j < limit && a.getbyte(j) == b.getbyte(j)
        j += 1
      end
      new_lcp = j
    end

    ans[i] = max_excluding > new_lcp ? max_excluding : new_lcp
  end

  ans
end
```

## Scala

```scala
object Solution {
  def longestCommonPrefix(words: Array[String]): Array[Int] = {
    val n = words.length
    if (n <= 2) return Array.fill(n)(0)

    // pre[i] = LCP of words[i] and words[i+1]
    val pre = new Array[Int](n - 1)
    var i = 0
    while (i < n - 1) {
      pre(i) = lcp(words(i), words(i + 1))
      i += 1
    }

    // prefixMax[j] = max of pre[0..j]
    val prefixMax = new Array[Int](n - 1)
    var cur = 0
    i = 0
    while (i < n - 1) {
      if (pre(i) > cur) cur = pre(i)
      prefixMax(i) = cur
      i += 1
    }

    // suffixMax[j] = max of pre[j..n-2]
    val suffixMax = new Array[Int](n - 1)
    cur = 0
    i = n - 2
    while (i >= 0) {
      if (pre(i) > cur) cur = pre(i)
      suffixMax(i) = cur
      i -= 1
    }

    val ans = new Array[Int](n)
    i = 0
    while (i < n) {
      var maxOther = 0
      // pairs completely to the left of removed index
      if (i - 2 >= 0) maxOther = prefixMax(i - 2)
      // pairs completely to the right of removed index
      if (i + 1 <= n - 2) {
        val right = suffixMax(i + 1)
        if (right > maxOther) maxOther = right
      }
      var newLcp = 0
      if (i > 0 && i < n - 1) newLcp = lcp(words(i - 1), words(i + 1))
      ans(i) = if (newLcp > maxOther) newLcp else maxOther
      i += 1
    }
    ans
  }

  private def lcp(a: String, b: String): Int = {
    val minLen = Math.min(a.length, b.length)
    var idx = 0
    while (idx < minLen && a.charAt(idx) == b.charAt(idx)) idx += 1
    idx
  }
}
```

## Rust

```rust
impl Solution {
    pub fn longest_common_prefix(words: Vec<String>) -> Vec<i32> {
        fn lcp(a: &[u8], b: &[u8]) -> usize {
            let mut i = 0;
            while i < a.len() && i < b.len() && a[i] == b[i] {
                i += 1;
            }
            i
        }

        let n = words.len();
        if n == 0 {
            return vec![];
        }

        // precompute LCP for original adjacent pairs
        let mut pref: Vec<usize> = Vec::with_capacity(n.saturating_sub(1));
        for i in 0..n.saturating_sub(1) {
            pref.push(lcp(words[i].as_bytes(), words[i + 1].as_bytes()));
        }

        // prefix max and suffix max of pref
        let mut left_max: Vec<usize> = vec![0; pref.len()];
        for i in 0..pref.len() {
            if i == 0 {
                left_max[i] = pref[i];
            } else {
                left_max[i] = left_max[i - 1].max(pref[i]);
            }
        }

        let mut right_max: Vec<usize> = vec![0; pref.len()];
        for i in (0..pref.len()).rev() {
            if i + 1 == pref.len() {
                right_max[i] = pref[i];
            } else {
                right_max[i] = right_max[i + 1].max(pref[i]);
            }
        }

        // compute answer for each removal
        let mut ans: Vec<i32> = Vec::with_capacity(n);
        for i in 0..n {
            let mut best: usize = 0;

            if i >= 2 && !pref.is_empty() {
                best = best.max(left_max[i - 2]);
            }
            if i + 1 <= n.saturating_sub(2) && !pref.is_empty() {
                best = best.max(right_max[i + 1]);
            }

            if i > 0 && i + 1 < n {
                let new_lcp = lcp(words[i - 1].as_bytes(), words[i + 1].as_bytes());
                best = best.max(new_lcp);
            }

            ans.push(best as i32);
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (longest-common-prefix words)
  (-> (listof string?) (listof exact-integer?))
  (let* ((n (length words))
         (words-v (list->vector words)))
    (if (= n 0)
        '()
        (let* ((pref (make-vector (max 0 (- n 1)) 0))
               (len-pref (vector-length pref)))
          ;; compute LCP for each original adjacent pair
          (define (lcplen a b)
            (let ((la (string-length a))
                  (lb (string-length b)))
              (let loop ((i 0))
                (if (or (= i la) (= i lb)
                        (not (char=? (string-ref a i) (string-ref b i))))
                    i
                    (loop (+ i 1))))))
          (for ([i (in-range (- n 1))])
            (vector-set! pref i
                         (lcplen (vector-ref words-v i)
                                 (vector-ref words-v (+ i 1)))))
          ;; prefix maximums
          (define left-max (make-vector len-pref 0))
          (when (> len-pref 0)
            (vector-set! left-max 0 (vector-ref pref 0))
            (for ([i (in-range 1 len-pref)])
              (vector-set! left-max i
                           (max (vector-ref left-max (- i 1))
                                (vector-ref pref i)))))
          ;; suffix maximums
          (define right-max (make-vector len-pref 0))
          (when (> len-pref 0)
            (vector-set! right-max (- len-pref 1) (vector-ref pref (- len-pref 1)))
            (for ([i (in-range (- len-pref 2) -1 -1)])
              (vector-set! right-max i
                           (max (vector-ref right-max (+ i 1))
                                (vector-ref pref i)))))
          ;; compute answer for each removal index
          (for/list ([i (in-range n)])
            (let* ((left (if (>= (- i 2) 0)
                             (vector-ref left-max (- i 2))
                             0))
                   (right (if (<= (+ i 1) (- len-pref 1))
                              (vector-ref right-max (+ i 1))
                              0))
                   (mid (if (and (> i 0) (< i (- n 1)))
                            (lcplen (vector-ref words-v (- i 1))
                                    (vector-ref words-v (+ i 1)))
                            0))
                   (ans (max left right mid)))
              ans))))))
```

## Erlang

```erlang
-spec longest_common_prefix(Words :: [unicode:unicode_binary()]) -> [integer()].
longest_common_prefix(Words) ->
    case length(Words) of
        0 -> [];
        1 -> [0];
        N ->
            WordsT = list_to_tuple(Words),
            PreLen = N - 1,
            PreList = compute_adjacent_lcp(WordsT, PreLen),
            PrefTuple = list_to_tuple(prefix_max_list(PreList)),
            SufTuple = list_to_tuple(suffix_max_list(PreList)),
            Lcp2Len = N - 2,
            Lcp2Tuple =
                case Lcp2Len > 0 of
                    true -> list_to_tuple(compute_gap_lcp(WordsT, Lcp2Len));
                    false -> {}
                end,
            compute_answers(N, PreLen, PrefTuple, SufTuple, Lcp2Len, Lcp2Tuple)
    end.

%% compute LCP for adjacent pairs (i,i+1)
compute_adjacent_lcp(_WordsT, 0) -> [];
compute_adjacent_lcp(WordsT, Len) ->
    lists:map(
      fun(I) -> lcp(element(I, WordsT), element(I + 1, WordsT)) end,
      lists:seq(1, Len)
    ).

%% compute LCP for pairs with one element between (i,i+2)
compute_gap_lcp(_WordsT, 0) -> [];
compute_gap_lcp(WordsT, Len) ->
    lists:map(
      fun(I) -> lcp(element(I, WordsT), element(I + 2, WordsT)) end,
      lists:seq(1, Len)
    ).

%% prefix maximums
prefix_max_list(List) -> prefix_max_list(List, 0, []).

prefix_max_list([], _CurMax, Acc) -> lists:reverse(Acc);
prefix_max_list([H|T], CurMax, Acc) ->
    NewMax = if H > CurMax -> H; true -> CurMax end,
    prefix_max_list(T, NewMax, [NewMax|Acc]).

%% suffix maximums
suffix_max_list(List) ->
    Rev = lists:reverse(List),
    RevSuf = suffix_max_rev(Rev, 0, []),
    lists:reverse(RevSuf).

suffix_max_rev([], _CurMax, Acc) -> Acc;
suffix_max_rev([H|T], CurMax, Acc) ->
    NewMax = if H > CurMax -> H; true -> CurMax end,
    suffix_max_rev(T, NewMax, [NewMax|Acc]).

%% compute final answers for each removal index
compute_answers(N, PreLen, PrefT, SufT, Lcp2Len, Lcp2T) ->
    lists:map(
      fun(I) -> answer_at(I, N, PreLen, PrefT, SufT, Lcp2Len, Lcp2T) end,
      lists:seq(1, N)
    ).

answer_at(I, N, PreLen, PrefT, SufT, Lcp2Len, Lcp2T) ->
    LeftIdx = I - 2,
    LeftMax = if LeftIdx >= 1 -> element(LeftIdx, PrefT); true -> 0 end,
    RightIdx = I + 1,
    RightMax = if RightIdx =< PreLen -> element(RightIdx, SufT); true -> 0 end,
    MaxExcl = erlang:max(LeftMax, RightMax),
    NewLcp =
        if I > 1, I < N ->
                Idx = I - 1,
                if Idx >= 1, Idx =< Lcp2Len -> element(Idx, Lcp2T); true -> 0 end;
           true -> 0
        end,
    erlang:max(MaxExcl, NewLcp).

%% longest common prefix of two binaries
lcp(Bin1, Bin2) -> lcp_bin(Bin1, Bin2, 0).

lcp_bin(<<Byte, Rest1/binary>>, <<Byte, Rest2/binary>>, Acc) ->
    lcp_bin(Rest1, Rest2, Acc + 1);
lcp_bin(_, _, Acc) -> Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_common_prefix(words :: [String.t()]) :: [integer()]
  def longest_common_prefix(words) do
    n = length(words)

    if n <= 1 do
      List.duplicate(0, n)
    else
      # Compute LCP for each adjacent pair
      {lcp_rev, _} =
        Enum.reduce(words, {[], nil}, fn word, {acc, prev} ->
          case prev do
            nil -> {acc, word}
            _ ->
              l = lcp_len(prev, word)
              {[l | acc], word}
          end
        end)

      lcp = Enum.reverse(lcp_rev)                # length n-1

      # Prefix max array
      pref_max =
        lcp
        |> Enum.reduce([], fn val, [] -> [val]; 
                               val, [prev_max | _] ->
                                 [if(val > prev_max, do: val, else: prev_max) | [prev_max | []]]
                             end)
        |> Enum.reverse()

      # Suffix max array
      suff_max =
        lcp
        |> Enum.reverse()
        |> Enum.reduce([], fn val, [] -> [val];
                               val, [prev_max | _] ->
                                 [if(val > prev_max, do: val, else: prev_max) | [prev_max | []]]
                             end)
        |> Enum.reverse()

      pref_t = List.to_tuple(pref_max)
      suff_t = List.to_tuple(suff_max)
      words_t = List.to_tuple(words)

      for i <- 0..(n - 1) do
        max_adj =
          cond do
            i == 0 ->
              if n - 2 >= 1, do: elem(suff_t, 1), else: 0

            i == n - 1 ->
              if n - 3 >= 0, do: elem(pref_t, n - 3), else: 0

            true ->
              left = if i - 2 >= 0, do: elem(pref_t, i - 2), else: 0
              right = if i + 1 <= n - 2, do: elem(suff_t, i + 1), else: 0
              max(left, right)
          end

        new_lcp =
          if i > 0 and i < n - 1 do
            w_left = elem(words_t, i - 1)
            w_right = elem(words_t, i + 1)
            lcp_len(w_left, w_right)
          else
            0
          end

        max(max_adj, new_lcp)
      end
    end
  end

  defp lcp_len(s1, s2), do: do_lcp(s1, s2, 0)

  defp do_lcp(<<c1, rest1::binary>>, <<c2, rest2::binary>>, acc) when c1 == c2,
    do: do_lcp(rest1, rest2, acc + 1)

  defp do_lcp(_, _, acc), do: acc
end
```
