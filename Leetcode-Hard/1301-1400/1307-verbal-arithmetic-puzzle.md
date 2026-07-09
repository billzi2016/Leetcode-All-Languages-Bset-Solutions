# 1307. Verbal Arithmetic Puzzle

## Cpp

```cpp
class Solution {
public:
    bool isSolvable(vector<string>& words, string result) {
        int n = words.size();
        // Count unique characters
        vector<int> seen(26, 0);
        for (auto &w : words)
            for (char c : w) seen[c - 'A'] = 1;
        for (char c : result) seen[c - 'A'] = 1;
        int uniq = 0;
        for (int v : seen) if (v) ++uniq;
        if (uniq > 10) return false; // more letters than digits
        
        // Prepare reversed words for column-wise processing
        vector<string> revWords(n);
        for (int i = 0; i < n; ++i) {
            revWords[i] = string(words[i].rbegin(), words[i].rend());
        }
        string revResult(result.rbegin(), result.rend());
        
        // Leading zero constraints
        bool nonZero[26] = {false};
        for (auto &w : words)
            if (w.size() > 1) nonZero[w[0] - 'A'] = true;
        if (result.size() > 1) nonZero[result[0] - 'A'] = true;
        
        int assign[26];
        fill(begin(assign), end(assign), -1);
        bool used[10] = {false};
        int maxLen = revResult.size();
        
        function<bool(int,int,int)> dfs = [&](int col, int row, int carry) -> bool {
            if (col == maxLen) {
                // all columns processed; ensure no remaining carry and all higher word digits are zero
                return carry == 0;
            }
            if (row < n) { // process each addend word at this column
                if (col >= (int)revWords[row].size()) {
                    // no character in this word for current column
                    return dfs(col, row + 1, carry);
                }
                char ch = revWords[row][col];
                int idx = ch - 'A';
                if (assign[idx] != -1) {
                    return dfs(col, row + 1, carry + assign[idx]);
                } else {
                    for (int d = 0; d <= 9; ++d) {
                        if (used[d]) continue;
                        if (d == 0 && nonZero[idx]) continue;
                        assign[idx] = d;
                        used[d] = true;
                        if (dfs(col, row + 1, carry + d)) return true;
                        assign[idx] = -1;
                        used[d] = false;
                    }
                    return false;
                }
            } else { // all addends processed, handle result digit
                int sum = carry;
                int expectedDigit = sum % 10;
                int newCarry = sum / 10;
                
                if (col >= (int)revResult.size()) {
                    // No character in result at this column; must be zero
                    if (expectedDigit != 0) return false;
                    return dfs(col + 1, 0, newCarry);
                }
                
                char chRes = revResult[col];
                int idxR = chRes - 'A';
                if (assign[idxR] != -1) {
                    if (assign[idxR] != expectedDigit) return false;
                    return dfs(col + 1, 0, newCarry);
                } else {
                    if (used[expectedDigit]) return false;
                    if (expectedDigit == 0 && nonZero[idxR]) return false;
                    assign[idxR] = expectedDigit;
                    used[expectedDigit] = true;
                    if (dfs(col + 1, 0, newCarry)) return true;
                    assign[idxR] = -1;
                    used[expectedDigit] = false;
                    return false;
                }
            }
        };
        
        return dfs(0, 0, 0);
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private String[] words;
    private String result;
    private int[] assign = new int[26];
    private boolean[] used = new boolean[10];
    private boolean[] leading = new boolean[26];
    private int maxLen;

    public boolean isSolvable(String[] words, String result) {
        this.words = words;
        this.result = result;
        Arrays.fill(assign, -1);

        for (String w : words) {
            if (w.length() > 1) leading[w.charAt(0) - 'A'] = true;
        }
        if (result.length() > 1) leading[result.charAt(0) - 'A'] = true;

        maxLen = result.length();
        for (String w : words) maxLen = Math.max(maxLen, w.length());

        boolean[] seen = new boolean[26];
        int uniq = 0;
        for (String w : words) {
            for (char c : w.toCharArray()) {
                if (!seen[c - 'A']) { seen[c - 'A'] = true; uniq++; }
            }
        }
        for (char c : result.toCharArray()) {
            if (!seen[c - 'A']) { seen[c - 'A'] = true; uniq++; }
        }
        if (uniq > 10) return false;

        return dfs(0, 0, 0);
    }

    private boolean dfs(int col, int row, int carry) {
        if (col == maxLen) return carry == 0;

        if (row < words.length) {
            String w = words[row];
            if (col >= w.length()) return dfs(col, row + 1, carry);
            char ch = w.charAt(w.length() - 1 - col);
            int idx = ch - 'A';
            int val = assign[idx];
            if (val != -1) {
                return dfs(col, row + 1, carry + val);
            } else {
                for (int d = 0; d <= 9; d++) {
                    if (used[d]) continue;
                    if (d == 0 && leading[idx]) continue;
                    assign[idx] = d;
                    used[d] = true;
                    if (dfs(col, row + 1, carry + d)) return true;
                    assign[idx] = -1;
                    used[d] = false;
                }
                return false;
            }
        } else {
            if (col >= result.length()) {
                int expected = carry % 10;
                if (expected != 0) return false;
                return dfs(col + 1, 0, carry / 10);
            }
            char ch = result.charAt(result.length() - 1 - col);
            int idx = ch - 'A';
            int val = assign[idx];
            int expected = carry % 10;
            int newCarry = carry / 10;
            if (val != -1) {
                if (val != expected) return false;
                return dfs(col + 1, 0, newCarry);
            } else {
                if (used[expected]) return false;
                if (expected == 0 && leading[idx]) return false;
                assign[idx] = expected;
                used[expected] = true;
                boolean ok = dfs(col + 1, 0, newCarry);
                if (ok) return true;
                assign[idx] = -1;
                used[expected] = false;
                return false;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def isSolvable(self, words, result):
        """
        :type words: List[str]
        :type result: str
        :rtype: bool
        """
        # reverse strings for column-wise processing (least significant first)
        rev_words = [w[::-1] for w in words]
        rev_res = result[::-1]

        max_len = max(max(len(w) for w in words), len(result))

        # letters that cannot be assigned zero (leading characters)
        leading = set()
        for w in words:
            if len(w) > 1:
                leading.add(w[0])
        if len(result) > 1:
            leading.add(result[0])

        assign = {}
        used = [False] * 10

        # depth-first search column by column
        def dfs(col, row, carry):
            if col == max_len:               # processed all columns
                return carry == 0

            if row < len(rev_words):         # process each addend word in this column
                w = rev_words[row]
                if col >= len(w):            # no character at this position
                    return dfs(col, row + 1, carry)
                ch = w[col]
                if ch in assign:
                    return dfs(col, row + 1, carry + assign[ch])
                else:
                    for d in range(10):
                        if used[d]:
                            continue
                        if d == 0 and ch in leading:
                            continue
                        assign[ch] = d
                        used[d] = True
                        if dfs(col, row + 1, carry + d):
                            return True
                        del assign[ch]
                        used[d] = False
                    return False

            else:                             # all addends processed, handle result digit
                expected_digit = carry % 10
                new_carry = carry // 10

                if col >= len(rev_res):      # no character in result at this column
                    if expected_digit != 0:
                        return False
                    return dfs(col + 1, 0, new_carry)

                ch_res = rev_res[col]
                if ch_res in assign:
                    if assign[ch_res] != expected_digit:
                        return False
                    return dfs(col + 1, 0, new_carry)
                else:
                    d = expected_digit
                    if used[d]:
                        return False
                    if d == 0 and ch_res in leading:
                        return False
                    assign[ch_res] = d
                    used[d] = True
                    if dfs(col + 1, 0, new_carry):
                        return True
                    del assign[ch_res]
                    used[d] = False
                    return False

        return dfs(0, 0, 0)
```

## Python3

```python
from typing import List

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        # collect unique characters
        uniq = set(''.join(words) + result)
        if len(uniq) > 10:
            return False

        # leading characters cannot be zero (if length > 1)
        leading = set()
        for w in words:
            if len(w) > 1:
                leading.add(w[0])
        if len(result) > 1:
            leading.add(result[0])

        n = len(words)
        rev_words = [w[::-1] for w in words]
        rev_res = result[::-1]

        max_len = max(max(len(w) for w in words), len(result))

        assign = {}
        used = [False] * 10

        # recursive processing of each column
        def backtrack(col: int, carry: int) -> bool:
            if col == max_len:
                return carry == 0

            # process all words at this column
            def dfs_word(i: int, total: int) -> bool:
                if i == n:
                    # handle result character
                    ch_res = rev_res[col] if col < len(rev_res) else None
                    expected_digit = total % 10
                    new_carry = total // 10

                    if ch_res is None:
                        if expected_digit != 0:
                            return False
                        return backtrack(col + 1, new_carry)

                    if ch_res in assign:
                        if assign[ch_res] != expected_digit:
                            return False
                        return backtrack(col + 1, new_carry)
                    else:
                        if used[expected_digit]:
                            return False
                        if expected_digit == 0 and ch_res in leading:
                            return False
                        assign[ch_res] = expected_digit
                        used[expected_digit] = True
                        ok = backtrack(col + 1, new_carry)
                        if not ok:
                            del assign[ch_res]
                            used[expected_digit] = False
                        return ok

                ch = rev_words[i][col] if col < len(rev_words[i]) else None
                if ch is None:
                    return dfs_word(i + 1, total)

                if ch in assign:
                    return dfs_word(i + 1, total + assign[ch])

                for d in range(10):
                    if used[d]:
                        continue
                    if d == 0 and ch in leading:
                        continue
                    assign[ch] = d
                    used[d] = True
                    if dfs_word(i + 1, total + d):
                        return True
                    del assign[ch]
                    used[d] = False
                return False

            return dfs_word(0, carry)

        return backtrack(0, 0)
```

## C

```c
#include <stdbool.h>
#include <string.h>

static int assignMap[26];
static bool usedDigit[10];
static bool leadingChar[26];
static int *wordLen;
static char **gWords;
static int gWordsSize;
static char *gResult;
static int resultLen;
static int maxCol;

static bool dfs(int col, int row, int carry) {
    if (col == maxCol) {
        return carry == 0;
    }
    if (row < gWordsSize) {
        int idx = wordLen[row] - 1 - col;
        if (idx < 0) {
            return dfs(col, row + 1, carry);
        }
        char ch = gWords[row][idx];
        int id = ch - 'A';
        if (assignMap[id] != -1) {
            return dfs(col, row + 1, carry + assignMap[id]);
        } else {
            for (int d = 0; d <= 9; ++d) {
                if (usedDigit[d]) continue;
                if (d == 0 && leadingChar[id]) continue;
                assignMap[id] = d;
                usedDigit[d] = true;
                if (dfs(col, row + 1, carry + d)) return true;
                assignMap[id] = -1;
                usedDigit[d] = false;
            }
            return false;
        }
    } else {
        int idxRes = resultLen - 1 - col;
        int expectedDigit = carry % 10;
        int newCarry = carry / 10;
        if (idxRes < 0) {
            if (expectedDigit != 0) return false;
            return dfs(col + 1, 0, newCarry);
        }
        char chRes = gResult[idxRes];
        int idRes = chRes - 'A';
        if (assignMap[idRes] != -1) {
            if (assignMap[idRes] != expectedDigit) return false;
            return dfs(col + 1, 0, newCarry);
        } else {
            if (usedDigit[expectedDigit]) return false;
            if (expectedDigit == 0 && leadingChar[idRes]) return false;
            assignMap[idRes] = expectedDigit;
            usedDigit[expectedDigit] = true;
            bool ok = dfs(col + 1, 0, newCarry);
            if (ok) return true;
            assignMap[idRes] = -1;
            usedDigit[expectedDigit] = false;
            return false;
        }
    }
}

bool isSolvable(char** words, int wordsSize, char* result) {
    gWords = words;
    gWordsSize = wordsSize;
    gResult = result;

    // initialize
    for (int i = 0; i < 26; ++i) assignMap[i] = -1, leadingChar[i] = false;
    for (int d = 0; d < 10; ++d) usedDigit[d] = false;

    bool present[26] = {false};
    int uniqueCount = 0;

    // compute lengths and leading chars
    wordLen = (int*)malloc(sizeof(int) * wordsSize);
    for (int i = 0; i < wordsSize; ++i) {
        wordLen[i] = (int)strlen(words[i]);
        if (wordLen[i] > 1) {
            leadingChar[words[i][0] - 'A'] = true;
        }
        for (int j = 0; j < wordLen[i]; ++j) {
            int id = words[i][j] - 'A';
            if (!present[id]) { present[id] = true; uniqueCount++; }
        }
    }

    resultLen = (int)strlen(result);
    if (resultLen > 1) leadingChar[result[0] - 'A'] = true;
    for (int j = 0; j < resultLen; ++j) {
        int id = result[j] - 'A';
        if (!present[id]) { present[id] = true; uniqueCount++; }
    }

    if (uniqueCount > 10) {
        free(wordLen);
        return false;
    }

    // determine max columns to process
    maxCol = resultLen;
    for (int i = 0; i < wordsSize; ++i)
        if (wordLen[i] > maxCol) maxCol = wordLen[i];
    // one extra column may be needed for final carry
    maxCol += 1;

    bool ans = dfs(0, 0, 0);
    free(wordLen);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    private string[] words;
    private string result;
    private int maxLen;
    private readonly int[] assign = new int[26];
    private readonly bool[] used = new bool[10];
    private readonly bool[] nonZero = new bool[26];

    public bool IsSolvable(string[] words, string result) {
        this.words = words;
        this.result = result;

        for (int i = 0; i < 26; i++) assign[i] = -1;

        foreach (var w in words) {
            if (w.Length > 1) nonZero[w[0] - 'A'] = true;
        }
        if (result.Length > 1) nonZero[result[0] - 'A'] = true;

        var set = new System.Collections.Generic.HashSet<char>();
        foreach (var w in words) foreach (char c in w) set.Add(c);
        foreach (char c in result) set.Add(c);
        if (set.Count > 10) return false;

        maxLen = result.Length;
        foreach (var w in words) if (w.Length > maxLen) maxLen = w.Length;

        return Dfs(0, 0, 0);
    }

    private char GetChar(string s, int col) {
        int idx = s.Length - 1 - col;
        return idx < 0 ? '\0' : s[idx];
    }

    private bool Dfs(int col, int wordIdx, int sum) {
        if (col == maxLen) {
            return sum == 0;
        }
        if (wordIdx < words.Length) {
            char c = GetChar(words[wordIdx], col);
            if (c == '\0') {
                return Dfs(col, wordIdx + 1, sum);
            }
            int li = c - 'A';
            int val = assign[li];
            if (val != -1) {
                return Dfs(col, wordIdx + 1, sum + val);
            }
            for (int d = 0; d <= 9; ++d) {
                if (used[d]) continue;
                if (d == 0 && nonZero[li]) continue;
                assign[li] = d;
                used[d] = true;
                if (Dfs(col, wordIdx + 1, sum + d)) return true;
                assign[li] = -1;
                used[d] = false;
            }
            return false;
        } else {
            char rc = GetChar(result, col);
            int expected = sum % 10;
            int newCarry = sum / 10;
            if (rc == '\0') {
                if (expected != 0) return false;
                return Dfs(col + 1, 0, newCarry);
            }
            int li = rc - 'A';
            int val = assign[li];
            if (val != -1) {
                if (val != expected) return false;
                return Dfs(col + 1, 0, newCarry);
            }
            if (used[expected]) return false;
            if (expected == 0 && nonZero[li]) return false;
            assign[li] = expected;
            used[expected] = true;
            bool ok = Dfs(col + 1, 0, newCarry);
            assign[li] = -1;
            used[expected] = false;
            return ok;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {string} result
 * @return {boolean}
 */
var isSolvable = function(words, result) {
    const nWords = words.length;
    // collect unique letters
    const uniq = new Set();
    for (const w of words) for (const ch of w) uniq.add(ch);
    for (const ch of result) uniq.add(ch);
    if (uniq.size > 10) return false; // more than digits

    // leading letters cannot be zero (if length > 1)
    const leading = new Set();
    for (const w of words) if (w.length > 1) leading.add(w[0]);
    if (result.length > 1) leading.add(result[0]);

    const assign = {};               // letter -> digit
    const used = Array(10).fill(false);

    const maxLen = Math.max(...words.map(w => w.length), result.length);

    function getChar(str, col) {
        const idx = str.length - 1 - col;
        return idx >= 0 ? str[idx] : null;
    }

    // dfs over columns (col) and words within column (idx)
    function dfs(col, idx, sum) {
        if (col === maxLen) {
            // all columns processed; final carry must be zero
            return sum === 0;
        }
        if (idx < nWords) {
            const ch = getChar(words[idx], col);
            if (!ch) {
                // no character in this word at this column
                return dfs(col, idx + 1, sum);
            }
            if (assign.hasOwnProperty(ch)) {
                return dfs(col, idx + 1, sum + assign[ch]);
            } else {
                for (let d = 0; d <= 9; ++d) {
                    if (used[d]) continue;
                    if (d === 0 && leading.has(ch)) continue;
                    assign[ch] = d;
                    used[d] = true;
                    if (dfs(col, idx + 1, sum + d)) return true;
                    delete assign[ch];
                    used[d] = false;
                }
                return false;
            }
        } else {
            // process result character for this column
            const chRes = getChar(result, col);
            const digit = sum % 10;
            const nextCarry = Math.floor(sum / 10);

            if (!chRes) {
                // no character means implied zero
                if (digit !== 0) return false;
                return dfs(col + 1, 0, nextCarry);
            }

            if (assign.hasOwnProperty(chRes)) {
                if (assign[chRes] !== digit) return false;
                return dfs(col + 1, 0, nextCarry);
            } else {
                if (used[digit]) return false;
                if (digit === 0 && leading.has(chRes)) return false;
                assign[chRes] = digit;
                used[digit] = true;
                if (dfs(col + 1, 0, nextCarry)) return true;
                delete assign[chRes];
                used[digit] = false;
                return false;
            }
        }
    }

    return dfs(0, 0, 0);
};
```

## Typescript

```typescript
function isSolvable(words: string[], result: string): boolean {
    const n = words.length;
    const maxLen = Math.max(...words.map(w => w.length), result.length);
    const revWords = words.map(w => w.split('').reverse());
    const revResult = result.split('').reverse();

    // letters that cannot be assigned 0 (leading letters of multi‑letter numbers)
    const leading = new Set<string>();
    for (const w of words) {
        if (w.length > 1) leading.add(w[0]);
    }
    if (result.length > 1) leading.add(result[0]);

    const assign = new Array(26).fill(-1);
    const used = new Array(10).fill(false);

    function dfs(pos: number, idx: number, sum: number, carry: number): boolean {
        if (pos === maxLen) {
            return carry === 0;
        }

        // Process each addend word for this column
        if (idx < n) {
            const w = revWords[idx];
            if (pos >= w.length) {
                // No character in this word at current position
                return dfs(pos, idx + 1, sum, carry);
            }
            const ch = w[pos];
            const ci = ch.charCodeAt(0) - 65;
            const val = assign[ci];
            if (val !== -1) {
                return dfs(pos, idx + 1, sum + val, carry);
            } else {
                for (let d = 0; d <= 9; ++d) {
                    if (used[d]) continue;
                    if (d === 0 && leading.has(ch)) continue;
                    assign[ci] = d;
                    used[d] = true;
                    if (dfs(pos, idx + 1, sum + d, carry)) return true;
                    assign[ci] = -1;
                    used[d] = false;
                }
                return false;
            }
        }

        // All addend words processed for this column; handle result digit
        const total = sum + carry;
        const expectedDigit = total % 10;
        const newCarry = Math.floor(total / 10);

        if (pos >= revResult.length) {
            // No character in result at this position, it must be zero
            if (expectedDigit !== 0) return false;
            return dfs(pos + 1, 0, 0, newCarry);
        }

        const chRes = revResult[pos];
        const ciRes = chRes.charCodeAt(0) - 65;
        const valRes = assign[ciRes];

        if (valRes !== -1) {
            if (valRes !== expectedDigit) return false;
            return dfs(pos + 1, 0, 0, newCarry);
        } else {
            if (used[expectedDigit]) return false;
            if (expectedDigit === 0 && leading.has(chRes)) return false;
            assign[ciRes] = expectedDigit;
            used[expectedDigit] = true;
            if (dfs(pos + 1, 0, 0, newCarry)) return true;
            assign[ciRes] = -1;
            used[expectedDigit] = false;
            return false;
        }
    }

    return dfs(0, 0, 0, 0);
}
```

## Php

```php
class Solution {
    private array $words;
    private string $result;
    private int $maxLen;
    private int $wCount;
    private array $lead = [];          // letters that cannot be zero
    private array $char2digit = [];   // mapping letter => digit
    private array $usedDigits;        // bool[10]

    /**
     * @param String[] $words
     * @param String $result
     * @return Boolean
     */
    function isSolvable($words, $result) {
        $this->words = $words;
        $this->result = $result;
        $this->wCount = count($words);
        $this->maxLen = strlen($result);
        foreach ($words as $w) {
            $len = strlen($w);
            if ($len > $this->maxLen) $this->maxLen = $len;
        }

        // leading letters (first character of each word/result)
        foreach ($words as $w) {
            $ch = $w[0];
            $this->lead[$ch] = true;
        }
        $this->lead[$result[0]] = true;

        $this->usedDigits = array_fill(0, 10, false);
        $this->char2digit = [];

        return $this->dfs(0, 0, 0);
    }

    private function getCharAt(string $word, int $col): ?string {
        $idx = strlen($word) - 1 - $col;
        if ($idx < 0) return null;
        return $word[$idx];
    }

    private function dfs(int $col, int $row, int $carry): bool {
        // all columns processed
        if ($col == $this->maxLen) {
            return $carry == 0;
        }

        // processing words rows
        if ($row < $this->wCount) {
            $ch = $this->getCharAt($this->words[$row], $col);
            if ($ch === null) {
                // no contribution from this word at this column
                return $this->dfs($col, $row + 1, $carry);
            }

            if (array_key_exists($ch, $this->char2digit)) {
                $digit = $this->char2digit[$ch];
                return $this->dfs($col, $row + 1, $carry + $digit);
            } else {
                // try all possible digits
                for ($d = 0; $d <= 9; $d++) {
                    if ($this->usedDigits[$d]) continue;
                    if ($d == 0 && isset($this->lead[$ch])) continue;

                    // assign
                    $this->char2digit[$ch] = $d;
                    $this->usedDigits[$d] = true;

                    if ($this->dfs($col, $row + 1, $carry + $d)) {
                        return true;
                    }

                    // backtrack
                    unset($this->char2digit[$ch]);
                    $this->usedDigits[$d] = false;
                }
                return false;
            }
        } else { // handle result character for this column
            $ch = $this->getCharAt($this->result, $col);
            $expectedDigit = $carry % 10;
            $newCarry = intdiv($carry, 10);

            if ($ch === null) {
                // no letter in result at this position; expected digit must be zero
                if ($expectedDigit != 0) return false;
                return $this->dfs($col + 1, 0, $newCarry);
            }

            if (array_key_exists($ch, $this->char2digit)) {
                $digit = $this->char2digit[$ch];
                if ($digit != $expectedDigit) return false;
                return $this->dfs($col + 1, 0, $newCarry);
            } else {
                // need to assign expected digit to this letter
                if ($this->usedDigits[$expectedDigit]) return false;
                if ($expectedDigit == 0 && isset($this->lead[$ch])) return false;

                $this->char2digit[$ch] = $expectedDigit;
                $this->usedDigits[$expectedDigit] = true;

                $res = $this->dfs($col + 1, 0, $newCarry);
                if ($res) return true;

                // backtrack
                unset($this->char2digit[$ch]);
                $this->usedDigits[$expectedDigit] = false;
                return false;
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func isSolvable(_ words: [String], _ result: String) -> Bool {
        var allChars = Set<Character>()
        for w in words { for ch in w { allChars.insert(ch) } }
        for ch in result { allChars.insert(ch) }

        if allChars.count > 10 { return false }

        var charToIdx = [Character:Int]()
        var idx = 0
        for ch in allChars {
            charToIdx[ch] = idx
            idx += 1
        }

        var leading = Set<Character>()
        for w in words where w.count > 1 {
            leading.insert(w.first!)
        }
        if result.count > 1 { leading.insert(result.first!) }

        let maxLen = max(words.map { $0.count }.max() ?? 0, result.count)

        let wordChars: [[Character]] = words.map { Array($0) }
        let resultChars = Array(result)

        var assign = Array(repeating: -1, count: allChars.count)
        var used = Array(repeating: false, count: 10)

        func dfs(_ col: Int, _ row: Int, _ sum: Int) -> Bool {
            if col == maxLen { return sum == 0 }

            if row < wordChars.count {
                let w = wordChars[row]
                let pos = w.count - 1 - col
                if pos < 0 {
                    return dfs(col, row + 1, sum)
                }
                let ch = w[pos]
                guard let li = charToIdx[ch] else { return false }

                if assign[li] != -1 {
                    return dfs(col, row + 1, sum + assign[li])
                } else {
                    for d in 0...9 where !used[d] {
                        if d == 0 && leading.contains(ch) { continue }
                        assign[li] = d
                        used[d] = true
                        if dfs(col, row + 1, sum + d) { return true }
                        assign[li] = -1
                        used[d] = false
                    }
                    return false
                }
            } else {
                let pos = resultChars.count - 1 - col
                let expected = sum % 10
                let carry = sum / 10

                if pos < 0 {
                    if expected != 0 { return false }
                    return dfs(col + 1, 0, carry)
                }

                let ch = resultChars[pos]
                guard let li = charToIdx[ch] else { return false }

                if assign[li] != -1 {
                    if assign[li] != expected { return false }
                    return dfs(col + 1, 0, carry)
                } else {
                    if used[expected] { return false }
                    if expected == 0 && leading.contains(ch) { return false }
                    assign[li] = expected
                    used[expected] = true
                    let ok = dfs(col + 1, 0, carry)
                    if ok { return true }
                    assign[li] = -1
                    used[expected] = false
                    return false
                }
            }
        }

        return dfs(0, 0, 0)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isSolvable(words: Array<String>, result: String): Boolean {
        // Collect unique characters
        val charIndex = mutableMapOf<Char, Int>()
        for (w in words) {
            for (c in w) {
                if (!charIndex.containsKey(c)) {
                    charIndex[c] = charIndex.size
                }
            }
        }
        for (c in result) {
            if (!charIndex.containsKey(c)) {
                charIndex[c] = charIndex.size
            }
        }
        val nChars = charIndex.size
        // Leading letters cannot be zero
        val leading = BooleanArray(nChars)
        for (w in words) {
            if (w.isNotEmpty()) leading[charIndex[w[0]]!!] = true
        }
        if (result.isNotEmpty()) leading[charIndex[result[0]]!!] = true

        val assign = IntArray(nChars) { -1 }
        val used = BooleanArray(10)

        val maxLen = maxOf(words.maxOf { it.length }, result.length)

        fun dfs(col: Int, row: Int, carry: Int): Boolean {
            if (col == maxLen) {
                return carry == 0
            }
            if (row < words.size) {
                val w = words[row]
                if (col >= w.length) {
                    // No character in this word at current column
                    return dfs(col, row + 1, carry)
                }
                val ch = w[w.length - 1 - col]
                val idx = charIndex.getValue(ch)
                val assigned = assign[idx]
                if (assigned != -1) {
                    return dfs(col, row + 1, carry + assigned)
                } else {
                    for (d in 0..9) {
                        if (!used[d]) {
                            if (d == 0 && leading[idx]) continue
                            used[d] = true
                            assign[idx] = d
                            if (dfs(col, row + 1, carry + d)) return true
                            used[d] = false
                            assign[idx] = -1
                        }
                    }
                    return false
                }
            } else {
                // Process result character at this column
                val sum = carry
                val digitNeeded = sum % 10
                val newCarry = sum / 10

                if (col >= result.length) {
                    // No result character; digit must be zero
                    if (digitNeeded != 0) return false
                    return dfs(col + 1, 0, newCarry)
                }

                val ch = result[result.length - 1 - col]
                val idx = charIndex.getValue(ch)
                val assigned = assign[idx]

                if (assigned != -1) {
                    if (assigned != digitNeeded) return false
                    return dfs(col + 1, 0, newCarry)
                } else {
                    if (used[digitNeeded]) return false
                    if (digitNeeded == 0 && leading[idx]) return false
                    used[digitNeeded] = true
                    assign[idx] = digitNeeded
                    if (dfs(col + 1, 0, newCarry)) return true
                    used[digitNeeded] = false
                    assign[idx] = -1
                    return false
                }
            }
        }

        return dfs(0, 0, 0)
    }
}
```

## Dart

```dart
class Solution {
  bool isSolvable(List<String> words, String result) {
    // Collect unique letters
    final Set<String> uniq = {};
    for (var w in words) {
      for (int i = 0; i < w.length; ++i) uniq.add(w[i]);
    }
    for (int i = 0; i < result.length; ++i) uniq.add(result[i]);

    final List<String> letters = uniq.toList();
    final int n = letters.length;
    if (n > 10) return false;

    // Map letter to its index in letters list
    final Map<String, int> idxMap = {};
    for (int i = 0; i < n; ++i) idxMap[letters[i]] = i;

    // Leading zero constraints: true means cannot be assigned 0
    final List<bool> noZero = List.filled(n, false);
    void markNoZero(String s) {
      if (s.length > 1) {
        final int id = idxMap[s[0]]!;
        noZero[id] = true;
      }
    }

    for (var w in words) markNoZero(w);
    markNoZero(result);

    // Assignment arrays
    final List<int> assign = List.filled(n, -1);
    final List<bool> used = List.filled(10, false);
    bool solved = false;

    bool checkSolution() {
      // Build char->digit map for quick lookup
      final List<int> charMap = List.filled(26, -1);
      for (int i = 0; i < n; ++i) {
        charMap[letters[i].codeUnitAt(0) - 65] = assign[i];
      }

      int sum = 0;
      for (var w in words) {
        int val = 0;
        for (int i = 0; i < w.length; ++i) {
          val = val * 10 + charMap[w.codeUnitAt(i) - 65];
        }
        sum += val;
      }

      int resVal = 0;
      for (int i = 0; i < result.length; ++i) {
        resVal = resVal * 10 + charMap[result.codeUnitAt(i) - 65];
      }

      return sum == resVal;
    }

    bool dfs(int pos) {
      if (solved) return true;
      if (pos == n) {
        solved = checkSolution();
        return solved;
      }
      for (int d = 0; d <= 9; ++d) {
        if (used[d]) continue;
        if (d == 0 && noZero[pos]) continue;
        assign[pos] = d;
        used[d] = true;
        if (dfs(pos + 1)) return true;
        assign[pos] = -1;
        used[d] = false;
      }
      return false;
    }

    dfs(0);
    return solved;
  }
}
```

## Golang

```go
func isSolvable(words []string, result string) bool {
    // maximum distinct letters <=10
    const alphabet = 26
    assign := make([]int, alphabet)
    for i := 0; i < alphabet; i++ {
        assign[i] = -1
    }
    used := make([]bool, 10)

    leading := make([]bool, alphabet)
    // mark leading letters (cannot be zero if length > 1)
    for _, w := range words {
        if len(w) > 1 {
            leading[w[0]-'A'] = true
        }
    }
    if len(result) > 1 {
        leading[result[0]-'A'] = true
    }

    // compute max column length
    maxLen := len(result)
    for _, w := range words {
        if len(w) > maxLen {
            maxLen = len(w)
        }
    }

    var dfs func(col, idx, sum, carry int) bool
    dfs = func(col, idx, sum, carry int) bool {
        // finished all columns
        if col == maxLen {
            return carry == 0
        }

        // process each word at current column
        if idx < len(words) {
            w := words[idx]
            if col >= len(w) {
                // no character in this word for this column
                return dfs(col, idx+1, sum, carry)
            }
            ch := w[len(w)-1-col] - 'A'
            d := assign[ch]
            if d != -1 {
                return dfs(col, idx+1, sum+d, carry)
            }
            // try all possible digits
            for dig := 0; dig <= 9; dig++ {
                if used[dig] {
                    continue
                }
                if dig == 0 && leading[ch] {
                    continue
                }
                assign[ch] = dig
                used[dig] = true
                if dfs(col, idx+1, sum+dig, carry) {
                    return true
                }
                assign[ch] = -1
                used[dig] = false
            }
            return false
        }

        // all words processed for this column, handle result character
        total := sum + carry
        expected := total % 10
        newCarry := total / 10

        if col >= len(result) {
            // no result digit at this position; must be zero
            if expected != 0 {
                return false
            }
            return dfs(col+1, 0, 0, newCarry)
        }

        ch := result[len(result)-1-col] - 'A'
        d := assign[ch]
        if d != -1 {
            if d != expected {
                return false
            }
            return dfs(col+1, 0, 0, newCarry)
        }
        // need to assign expected digit to this character
        if used[expected] {
            return false
        }
        if expected == 0 && leading[ch] {
            return false
        }
        assign[ch] = expected
        used[expected] = true
        if dfs(col+1, 0, 0, newCarry) {
            return true
        }
        assign[ch] = -1
        used[expected] = false
        return false
    }

    return dfs(0, 0, 0, 0)
}
```

## Ruby

```ruby
def is_solvable(words, result)
  n = words.size
  leading = {}
  words.each { |w| leading[w[0]] = true if w.length > 1 }
  leading[result[0]] = true if result.length > 1

  rev_words = words.map(&:reverse)
  rev_result = result.reverse
  max_len = [rev_words.map(&:length).max, rev_result.length].max

  assign = {}
  used = Array.new(10, false)

  solve = nil
  solve = lambda do |col, row, carry|
    if col == max_len
      return carry.zero?
    end

    if row < n
      if col >= rev_words[row].length
        return solve.call(col, row + 1, carry)
      else
        ch = rev_words[row][col]
        if assign.key?(ch)
          return solve.call(col, row + 1, carry + assign[ch])
        else
          (0..9).each do |d|
            next if used[d]
            next if d.zero? && leading[ch]

            assign[ch] = d
            used[d] = true
            if solve.call(col, row + 1, carry + d)
              return true
            end
            used[d] = false
            assign.delete(ch)
          end
          return false
        end
      end
    else
      sum = carry
      expected = sum % 10
      new_carry = sum / 10

      if col >= rev_result.length
        return false unless expected.zero?
        return solve.call(col + 1, 0, new_carry)
      else
        ch = rev_result[col]
        if assign.key?(ch)
          return false unless assign[ch] == expected
          return solve.call(col + 1, 0, new_carry)
        else
          return false if used[expected] || (expected.zero? && leading[ch])

          assign[ch] = expected
          used[expected] = true
          if solve.call(col + 1, 0, new_carry)
            return true
          end
          used[expected] = false
          assign.delete(ch)
          return false
        end
      end
    end
  end

  solve.call(0, 0, 0)
end
```

## Scala

```scala
object Solution {
  def isSolvable(words: Array[String], result: String): Boolean = {
    // collect unique characters
    val uniq = scala.collection.mutable.LinkedHashSet[Char]()
    words.foreach(_.foreach(uniq.add))
    result.foreach(uniq.add)

    if (uniq.size > 10) return false

    val charToIdx = new scala.collection.mutable.HashMap[Char, Int]()
    var cnt = 0
    for (c <- uniq) {
      charToIdx(c) = cnt
      cnt += 1
    }
    val n = uniq.size
    val assign = Array.fill[Int](n)(-1)
    val used   = Array.fill[Boolean](10)(false)

    // leading zero restriction
    val noZero = Array.fill[Boolean](n)(false)
    for (w <- words) if (w.length > 1) noZero(charToIdx(w.charAt(0))) = true
    if (result.length > 1) noZero(charToIdx(result.charAt(0))) = true

    // reversed indices per word
    val wordsRev: Array[Array[Int]] = words.map { w =>
      val arr = new Array[Int](w.length)
      for (i <- 0 until w.length) arr(i) = charToIdx(w.charAt(w.length - 1 - i))
      arr
    }

    // reversed result indices
    val resRev: Array[Int] = {
      val arr = new Array[Int](result.length)
      for (i <- 0 until result.length) arr(i) = charToIdx(result.charAt(result.length - 1 - i))
      arr
    }

    val maxLen = math.max(words.map(_.length).max, result.length)

    def solve(pos: Int, carry: Int): Boolean = {
      if (pos == maxLen) return carry == 0

      var sum = carry
      val colLetters = scala.collection.mutable.ArrayBuffer[Int]()

      for (wArr <- wordsRev) {
        if (pos < wArr.length) {
          val idx = wArr(pos)
          if (assign(idx) != -1) sum += assign(idx)
          else colLetters += idx
        }
      }

      val resIdxOpt: Option[Int] =
        if (pos < resRev.length) Some(resRev(pos)) else None

      def dfsAssign(i: Int, curSum: Int): Boolean = {
        if (i == colLetters.size) {
          val expected = curSum % 10
          val newCarry = curSum / 10
          resIdxOpt match {
            case Some(ridx) =>
              if (assign(ridx) != -1) {
                if (assign(ridx) == expected) solve(pos + 1, newCarry)
                else false
              } else {
                if (used(expected)) false
                else if (expected == 0 && noZero(ridx)) false
                else {
                  assign(ridx) = expected
                  used(expected) = true
                  val ok = solve(pos + 1, newCarry)
                  if (!ok) {
                    assign(ridx) = -1
                    used(expected) = false
                  }
                  ok
                }
              }
            case None =>
              if (expected != 0) false else solve(pos + 1, newCarry)
          }
        } else {
          val idx = colLetters(i)
          for (d <- 0 to 9) {
            if (!used(d)) {
              if (d == 0 && noZero(idx)) {}
              else {
                assign(idx) = d
                used(d) = true
                if (dfsAssign(i + 1, curSum + d)) return true
                assign(idx) = -1
                used(d) = false
              }
            }
          }
          false
        }
      }

      dfsAssign(0, sum)
    }

    solve(0, 0)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn is_solvable(words: Vec<String>, result: String) -> bool {
        use std::collections::{HashMap, HashSet};

        // collect unique letters
        let mut uniq = HashSet::new();
        for w in &words {
            for ch in w.chars() {
                uniq.insert(ch);
            }
        }
        for ch in result.chars() {
            uniq.insert(ch);
        }
        if uniq.len() > 10 {
            return false;
        }

        // map each letter to an index 0..k-1
        let mut char_to_idx = HashMap::new();
        let mut idx = 0usize;
        for &ch in uniq.iter() {
            char_to_idx.insert(ch, idx);
            idx += 1;
        }
        let k = idx;

        // leading letters cannot be zero (if length > 1)
        let mut leading = vec![false; k];
        for w in &words {
            if w.len() > 1 {
                let first = w.chars().next().unwrap();
                leading[char_to_idx[&first]] = true;
            }
        }
        if result.len() > 1 {
            let first = result.chars().next().unwrap();
            leading[char_to_idx[&first]] = true;
        }

        let n_words = words.len();
        let max_len = std::cmp::max(
            words.iter().map(|w| w.len()).max().unwrap_or(0),
            result.len(),
        );

        // reversed representation: column 0 is least significant digit
        let mut words_rev: Vec<Vec<Option<usize>>> = vec![vec![None; max_len]; n_words];
        for (i, w) in words.iter().enumerate() {
            for (pos, ch) in w.chars().rev().enumerate() {
                let id = char_to_idx[&ch];
                words_rev[i][pos] = Some(id);
            }
        }

        let mut result_rev: Vec<Option<usize>> = vec![None; max_len];
        for (pos, ch) in result.chars().rev().enumerate() {
            let id = char_to_idx[&ch];
            result_rev[pos] = Some(id);
        }

        // assignment state
        let mut assign: Vec<i32> = vec![-1; k];
        let mut used: [bool; 10] = [false; 10];

        fn dfs(
            col: usize,
            row: usize,
            sum: i32,
            carry: i32,
            words_rev: &Vec<Vec<Option<usize>>>,
            result_rev: &Vec<Option<usize>>,
            n_words: usize,
            assign: &mut Vec<i32>,
            used: &mut [bool; 10],
            leading: &Vec<bool>,
            max_len: usize,
        ) -> bool {
            if col == max_len {
                return carry == 0;
            }
            if row < n_words {
                match words_rev[row][col] {
                    None => dfs(
                        col,
                        row + 1,
                        sum,
                        carry,
                        words_rev,
                        result_rev,
                        n_words,
                        assign,
                        used,
                        leading,
                        max_len,
                    ),
                    Some(ch_idx) => {
                        let val = assign[ch_idx];
                        if val != -1 {
                            return dfs(
                                col,
                                row + 1,
                                sum + val,
                                carry,
                                words_rev,
                                result_rev,
                                n_words,
                                assign,
                                used,
                                leading,
                                max_len,
                            );
                        } else {
                            for d in 0..10 {
                                if !used[d] && !(d == 0 && leading[ch_idx]) {
                                    used[d] = true;
                                    assign[ch_idx] = d as i32;
                                    if dfs(
                                        col,
                                        row + 1,
                                        sum + d as i32,
                                        carry,
                                        words_rev,
                                        result_rev,
                                        n_words,
                                        assign,
                                        used,
                                        leading,
                                        max_len,
                                    ) {
                                        return true;
                                    }
                                    assign[ch_idx] = -1;
                                    used[d] = false;
                                }
                            }
                            return false;
                        }
                    }
                }
            } else {
                // handle result digit
                let total = sum + carry;
                match result_rev[col] {
                    Some(ch_idx) => {
                        let expected = (total % 10) as i32;
                        let new_carry = total / 10;
                        let val = assign[ch_idx];
                        if val != -1 {
                            if val == expected {
                                return dfs(
                                    col + 1,
                                    0,
                                    0,
                                    new_carry,
                                    words_rev,
                                    result_rev,
                                    n_words,
                                    assign,
                                    used,
                                    leading,
                                    max_len,
                                );
                            } else {
                                return false;
                            }
                        } else {
                            let d = expected as usize;
                            if used[d] || (d == 0 && leading[ch_idx]) {
                                return false;
                            }
                            used[d] = true;
                            assign[ch_idx] = expected;
                            let res = dfs(
                                col + 1,
                                0,
                                0,
                                new_carry,
                                words_rev,
                                result_rev,
                                n_words,
                                assign,
                                used,
                                leading,
                                max_len,
                            );
                            if res {
                                return true;
                            }
                            assign[ch_idx] = -1;
                            used[d] = false;
                            return false;
                        }
                    }
                    None => {
                        // no character in result at this column, digit must be zero
                        let expected = (total % 10) as i32;
                        if expected != 0 {
                            return false;
                        }
                        let new_carry = total / 10;
                        return dfs(
                            col + 1,
                            0,
                            0,
                            new_carry,
                            words_rev,
                            result_rev,
                            n_words,
                            assign,
                            used,
                            leading,
                            max_len,
                        );
                    }
                }
            }
        }

        dfs(
            0,
            0,
            0,
            0,
            &words_rev,
            &result_rev,
            n_words,
            &mut assign,
            &mut used,
            &leading,
            max_len,
        )
    }
}
```

## Racket

```racket
(define/contract (is-solvable words result)
  (-> (listof string?) string? boolean?)
  (let* ((all-chars
           (let loop ((ws words) (acc '()))
             (if (null? ws)
                 acc
                 (loop (cdr ws)
                       (append (string->list (car ws)) acc)))))
         (unique-chars
           (remove-duplicates all-chars char=?))
         (unique-chars
           (let loop ((lst unique-chars) (seen '()) (out '()))
             (cond [(null? lst) (reverse out)]
                   [(member (car lst) seen)
                    (loop (cdr lst) seen out)]
                   [else
                    (loop (cdr lst) (cons (car lst) seen) (cons (car lst) out))])))
         (n (length unique-chars)))
    (if (> n 10)
        #f
        (let* ((char->idx (make-hash))
               (_ (for ([c unique-chars] [i (in-naturals)])
                    (hash-set! char->idx c i))))
               (assign (make-vector n -1))
               (used (make-vector 10 #f))
               (leading? (let ((set (make-hash)))
                           (for ([w words])
                             (when (> (string-length w) 1)
                               (hash-set! set (string-ref w 0) #t)))
                           (when (> (string-length result) 1)
                             (hash-set! set (string-ref result 0) #t))
                           (lambda (ch) (hash-has-key? set ch))))
               (max-len
                 (apply max (cons (string-length result)
                                  (map string-length words)))))
          (letrec
              ((solve
                (lambda (pos carry)
                  (if (= pos max-len)
                      (= carry 0)
                      (let* ((word-chars
                               (for/list ([w words]
                                          #:when (>= (- (string-length w) 1 pos) 0))
                                 (string-ref w (- (string-length w) 1 pos))))
                             (result-char
                               (let* ((idx (- (string-length result) 1 pos)))
                                 (if (>= idx 0)
                                     (string-ref result idx)
                                     #f))))
                        (letrec
                            ((assign-word-chars
                               (lambda (i sum)
                                 (if (= i (length word-chars))
                                     ; handle result character
                                     (let* ((total (+ sum carry))
                                            (digit-needed (modulo total 10))
                                            (new-carry (quotient total 10)))
                                       (if (eq? result-char #f)
                                           (and (= digit-needed 0)
                                                (solve (+ pos 1) new-carry))
                                           (let* ((idx (hash-ref char->idx result-char))
                                                  (cur (vector-ref assign idx)))
                                             (cond
                                               [(>= cur 0)
                                                (if (= cur digit-needed)
                                                    (solve (+ pos 1) new-carry)
                                                    #f)]
                                               [else
                                                (if (or (vector-ref used digit-needed)
                                                        (and (= digit-needed 0) (leading? result-char)))
                                                    #f
                                                    (begin
                                                      (vector-set! assign idx digit-needed)
                                                      (vector-set! used digit-needed #t)
                                                      (let ((res (solve (+ pos 1) new-carry)))
                                                        (unless res
                                                          (vector-set! assign idx -1)
                                                          (vector-set! used digit-needed #f))
                                                        res))))])))
                                     ; process next word character
                                     (let* ((ch (list-ref word-chars i))
                                            (idx (hash-ref char->idx ch))
                                            (cur (vector-ref assign idx)))
                                       (if (>= cur 0)
                                           (assign-word-chars (+ i 1) (+ sum cur))
                                           (let loop ((d 0))
                                             (cond [(= d 10) #f]
                                                   [(or (vector-ref used d)
                                                        (and (= d 0) (leading? ch)))
                                                    (loop (+ d 1))]
                                                   [else
                                                    (begin
                                                      (vector-set! assign idx d)
                                                      (vector-set! used d #t)
                                                      (if (assign-word-chars (+ i 1) (+ sum d))
                                                          #t
                                                          (begin
                                                            (vector-set! assign idx -1)
                                                            (vector-set! used d #f)
                                                            (loop (+ d 1)))))]))))))))
                          )
                        (assign-word-chars 0 0))))))
            (solve 0 0)))))))
```

## Erlang

```erlang
-module(solution).
-export([is_solvable/2]).

-spec is_solvable(Words :: [unicode:unicode_binary()], Result :: unicode:unicode_binary()) -> boolean().
is_solvable(Words, Result) ->
    AllChars = lists:foldl(fun(W, Acc) -> unicode:characters_to_list(W) ++ Acc end, [], Words)
               ++ unicode:characters_to_list(Result),
    UniqueChars = lists:usort(AllChars),
    case length(UniqueChars) > 10 of
        true -> false;
        false ->
            CharMap = maps:from_list(lists:zip(UniqueChars,
                                               lists:seq(0, length(UniqueChars) - 1))),
            LeadingSet = build_leading_set(Words ++ [Result], CharMap),
            MaxLenWords = lists:max([length(unicode:characters_to_list(W)) || W <- Words]),
            MaxLenRes = length(unicode:characters_to_list(Result)),
            MaxLen = erlang:max(MaxLenWords, MaxLenRes),

            WordsRev = [pad_rev(W, CharMap, MaxLen) || W <- Words],
            ResultRev = pad_rev(Result, CharMap, MaxLen),

            dfs(0, 0, #{}, 0, WordsRev, ResultRev, LeadingSet)
    end.

build_leading_set(StrList, CharMap) ->
    lists:foldl(fun(Str, Acc) ->
        Chars = unicode:characters_to_list(Str),
        case length(Chars) > 1 of
            true ->
                FirstChar = hd(Chars),
                Idx = maps:get(FirstChar, CharMap),
                maps:put(Idx, true, Acc);
            false -> Acc
        end
    end, #{}, StrList).

pad_rev(Str, CharMap, MaxLen) ->
    Chars = unicode:characters_to_list(Str),
    RevChars = lists:reverse(Chars),
    RevIdxs = [maps:get(C, CharMap) || C <- RevChars],
    PadLen = MaxLen - length(RevIdxs),
    Pad = lists:duplicate(PadLen, -1),
    RevIdxs ++ Pad.

dfs(Pos, Carry, AssignMap, UsedMask, WordsRev, ResultRev, LeadingSet) ->
    MaxLen = length(ResultRev),
    if Pos == MaxLen ->
            Carry == 0;
       true ->
            WordIdxs = [lists:nth(Pos + 1, RevWord) || RevWord <- WordsRev],
            ResIdx = lists:nth(Pos + 1, ResultRev),

            {SumKnown, CountMap, UnknownIndices} =
                process_column(WordIdxs, AssignMap, [], #{}, 0),

            case ResIdx of
                -1 ->
                    UpdatedUnknown = UnknownIndices,
                    UpdatedCountMap = CountMap;
                _ ->
                    case maps:get(ResIdx, AssignMap, undefined) of
                        undefined ->
                            UpdatedUnknown = lists:usort([ResIdx | UnknownIndices]),
                            UpdatedCountMap = CountMap;
                        _Digit ->
                            UpdatedUnknown = UnknownIndices,
                            UpdatedCountMap = CountMap
                    end
            end,

            assign_unknowns(UpdatedUnknown, Pos, SumKnown, UpdatedCountMap,
                            ResIdx, AssignMap, UsedMask, Carry,
                            WordsRev, ResultRev, LeadingSet)
    end.

process_column([], _AssignMap, UnknownAcc, CountMapAcc, SumKnown) ->
    {SumKnown, CountMapAcc, lists:usort(UnknownAcc)};
process_column([Idx | Rest], AssignMap, UnknownAcc, CountMapAcc, SumKnown) ->
    case Idx of
        -1 -> process_column(Rest, AssignMap, UnknownAcc, CountMapAcc, SumKnown);
        _ ->
            case maps:get(Idx, AssignMap, undefined) of
                undefined ->
                    PrevCount = maps:get(Idx, CountMapAcc, 0),
                    NewCountMap = maps:put(Idx, PrevCount + 1, CountMapAcc),
                    process_column(Rest, AssignMap, [Idx | UnknownAcc],
                                   NewCountMap, SumKnown);
                Digit when is_integer(Digit) ->
                    process_column(Rest, AssignMap, UnknownAcc,
                                   CountMapAcc, SumKnown + Digit)
            end
    end.

assign_unknowns([], Pos, SumSoFar, _CountMap, ResIdx, AssignMap, UsedMask,
               Carry, WordsRev, ResultRev, LeadingSet) ->
    ResultDigit = case ResIdx of
        -1 -> 0;
        _ -> maps:get(ResIdx, AssignMap)
    end,
    Total = SumSoFar + Carry,
    if (Total rem 10) =:= ResultDigit ->
            NewCarry = Total div 10,
            dfs(Pos + 1, NewCarry, AssignMap, UsedMask,
                WordsRev, ResultRev, LeadingSet);
       true -> false
    end;
assign_unknowns([Idx | Rest], Pos, SumSoFar, CountMap, ResIdx, AssignMap,
               UsedMask, Carry, WordsRev, ResultRev, LeadingSet) ->
    Count = maps:get(Idx, CountMap, 0),
    lists:any(fun(Digit) ->
        MaskBit = 1 bsl Digit,
        (UsedMask band MaskBit) =:= 0 andalso
        not (Digit == 0 andalso maps:is_key(Idx, LeadingSet)) andalso
        NewAssignMap = maps:put(Idx, Digit, AssignMap),
        NewUsedMask = UsedMask bor MaskBit,
        NewSum = SumSoFar + Count * Digit,
        assign_unknowns(Rest, Pos, NewSum, CountMap, ResIdx,
                        NewAssignMap, NewUsedMask, Carry,
                        WordsRev, ResultRev, LeadingSet)
    end, lists:seq(0, 9)).
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec is_solvable(words :: [String.t()], result :: String.t()) :: boolean()
  def is_solvable(words, result) do
    letters = (words ++ [result]) |> Enum.flat_map(&String.graphemes/1) |> Enum.uniq()

    if length(letters) > 10 do
      false
    else
      non_zero_set =
        (Enum.map(words, fn w -> String.at(w, 0) end) ++ [String.at(result, 0)])
        |> MapSet.new()

      words_rev = Enum.map(words, fn w -> String.graphemes(w) |> Enum.reverse() end)
      result_rev = String.graphemes(result) |> Enum.reverse()
      max_len = Enum.max(Enum.map(words, &String.length/1) ++ [String.length(result)])

      solve(0, 0, %{}, 0, words_rev, result_rev, max_len, non_zero_set)
    end
  end

  defp solve(pos, carry, assign, used, words_rev, result_rev, max_len, non_zero) do
    if pos == max_len do
      carry == 0
    else
      process_word(0, pos, carry, 0, assign, used, words_rev, result_rev, max_len, non_zero)
    end
  end

  defp process_word(idx, pos, carry, sum, assign, used, words_rev, result_rev, max_len, non_zero) do
    if idx == length(words_rev) do
      expected = rem(sum + carry, 10)
      new_carry = div(sum + carry, 10)

      result_letter =
        if pos < length(result_rev), do: Enum.at(result_rev, pos), else: nil

      cond do
        result_letter == nil ->
          if expected != 0 do
            false
          else
            solve(pos + 1, new_carry, assign, used, words_rev, result_rev, max_len, non_zero)
          end

        Map.has_key?(assign, result_letter) ->
          d = Map.get(assign, result_letter)

          if d == expected do
            solve(pos + 1, new_carry, assign, used, words_rev, result_rev, max_len, non_zero)
          else
            false
          end

        true ->
          if (used &&& (1 <<< expected)) != 0 or
               (expected == 0 and MapSet.member?(non_zero, result_letter)) do
            false
          else
            new_assign = Map.put(assign, result_letter, expected)
            new_used = used ||| (1 <<< expected)

            solve(pos + 1, new_carry, new_assign, new_used, words_rev, result_rev, max_len, non_zero)
          end
      end
    else
      word_rev = Enum.at(words_rev, idx)

      if pos >= length(word_rev) do
        process_word(idx + 1, pos, carry, sum, assign, used, words_rev, result_rev, max_len, non_zero)
      else
        letter = Enum.at(word_rev, pos)

        case Map.fetch(assign, letter) do
          {:ok, d} ->
            process_word(idx + 1, pos, carry, sum + d, assign, used, words_rev, result_rev, max_len, non_zero)

          :error ->
            Enum.reduce_while(0..9, false, fn dig, _acc ->
              if (used &&& (1 <<< dig)) != 0 do
                {:cont, false}
              else
                if dig == 0 and MapSet.member?(non_zero, letter) do
                  {:cont, false}
                else
                  new_assign = Map.put(assign, letter, dig)
                  new_used = used ||| (1 <<< dig)

                  case process_word(
                         idx + 1,
                         pos,
                         carry,
                         sum + dig,
                         new_assign,
                         new_used,
                         words_rev,
                         result_rev,
                         max_len,
                         non_zero
                       ) do
                    true -> {:halt, true}
                    false -> {:cont, false}
                  end
                end
              end
            end)
        end
      end
    end
  end
end
```
