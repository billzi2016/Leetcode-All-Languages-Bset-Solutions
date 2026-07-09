# 0488. Zuma Game

## Cpp

```cpp
class Solution {
public:
    int findMinStep(string board, string hand) {
        const string colors = "RYBGW";
        vector<int> cnt(5,0);
        for(char c: hand){
            cnt[colors.find(c)]++;
        }
        unordered_map<string,int> memo;
        const int INF = 1e9;
        
        function<string(const string&)> shrink = [&](const string& s)->string{
            string cur = s;
            bool changed = true;
            while(changed){
                changed = false;
                for(int i=0;i<(int)cur.size();){
                    int j=i+1;
                    while(j<(int)cur.size() && cur[j]==cur[i]) ++j;
                    if(j-i>=3){
                        cur.erase(i, j-i);
                        changed = true;
                        break; // restart scanning
                    }else{
                        i=j;
                    }
                }
            }
            return cur;
        };
        
        function<int(const string&)> dfs = [&](const string& b)->int{
            if(b.empty()) return 0;
            string key = b + "#";
            for(int v: cnt){
                key += to_string(v) + ",";
            }
            auto it = memo.find(key);
            if(it!=memo.end()) return it->second;
            
            int ans = INF;
            for(int ci=0; ci<5; ++ci){
                if(cnt[ci]==0) continue;
                char c = colors[ci];
                // try inserting at each position
                for(int i=0;i<= (int)b.size(); ++i){
                    // optimization: avoid redundant insertions where same color adjacent leads to same result
                    if(i>0 && b[i-1]==c) {
                        // skip unless this insertion creates a group of three directly
                        int left = i-1;
                        while(left>=0 && b[left]==c) --left;
                        int lenLeft = i-1-left;
                        // count same color to the right of insertion point
                        int right=i;
                        while(right<(int)b.size() && b[right]==c) ++right;
                        int lenRight = right-i;
                        if(lenLeft+lenRight+1 < 3) continue; // won't trigger elimination now
                    }
                    
                    string nb = b.substr(0,i) + c + b.substr(i);
                    string reduced = shrink(nb);
                    cnt[ci]--;
                    int sub = dfs(reduced);
                    if(sub!=INF){
                        ans = min(ans, 1+sub);
                    }
                    cnt[ci]++;
                }
            }
            memo[key]=ans;
            return ans;
        };
        
        int res = dfs(board);
        return res==INF ? -1 : res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int INF = 100;
    private final Map<String, Integer> memo = new HashMap<>();
    private final char[] colors = {'R', 'Y', 'B', 'G', 'W'};

    public int findMinStep(String board, String hand) {
        int[] cnt = new int[5];
        for (char c : hand.toCharArray()) {
            cnt[idx(c)]++;
        }
        int res = dfs(board, cnt);
        return res == INF ? -1 : res;
    }

    private int dfs(String board, int[] hand) {
        if (board.isEmpty()) return 0;
        String key = encode(board, hand);
        Integer cached = memo.get(key);
        if (cached != null) return cached;

        int ans = INF;
        for (int c = 0; c < 5; ++c) {
            if (hand[c] == 0) continue;
            char col = colors[c];
            for (int i = 0; i <= board.length(); ++i) {
                // avoid inserting same color consecutively without effect
                if (i > 0 && board.charAt(i - 1) == col) continue;
                String newBoard = board.substring(0, i) + col + board.substring(i);
                newBoard = reduce(newBoard);
                hand[c]--;
                int sub = dfs(newBoard, hand);
                if (sub != INF) {
                    ans = Math.min(ans, 1 + sub);
                }
                hand[c]++;
            }
        }

        memo.put(key, ans);
        return ans;
    }

    private String reduce(String s) {
        boolean changed = true;
        while (changed) {
            changed = false;
            StringBuilder sb = new StringBuilder();
            int i = 0;
            while (i < s.length()) {
                int j = i + 1;
                while (j < s.length() && s.charAt(j) == s.charAt(i)) j++;
                if (j - i >= 3) {
                    changed = true; // skip this group
                } else {
                    sb.append(s, i, j);
                }
                i = j;
            }
            s = sb.toString();
        }
        return s;
    }

    private int idx(char c) {
        switch (c) {
            case 'R': return 0;
            case 'Y': return 1;
            case 'B': return 2;
            case 'G': return 3;
            case 'W': return 4;
            default: return -1;
        }
    }

    private String encode(String board, int[] hand) {
        StringBuilder sb = new StringBuilder();
        sb.append(board).append('#');
        for (int i = 0; i < 5; ++i) {
            sb.append(hand[i]).append('#');
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        from functools import lru_cache

        colors = ['R', 'Y', 'B', 'G', 'W']
        idx = {c: i for i, c in enumerate(colors)}
        hand_cnt = [0] * 5
        for c in hand:
            hand_cnt[idx[c]] += 1

        def shrink(s):
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                if j - i >= 3:
                    return shrink(s[:i] + s[j:])
                i = j
            return s

        @lru_cache(None)
        def dfs(b, h):
            b = shrink(b)
            if not b:
                return 0
            ans = float('inf')
            n = len(b)
            i = 0
            while i < n:
                j = i
                while j < n and b[j] == b[i]:
                    j += 1
                cnt = j - i
                need = 3 - cnt
                if need > 0:
                    c_idx = idx[b[i]]
                    if h[c_idx] >= need:
                        new_hand = list(h)
                        new_hand[c_idx] -= need
                        new_board = b[:i] + b[j:]
                        sub = dfs(new_board, tuple(new_hand))
                        if sub != float('inf'):
                            ans = min(ans, sub + need)
                i = j
            return ans

        res = dfs(board, tuple(hand_cnt))
        return -1 if res == float('inf') else res
```

## Python3

```python
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        colors = ['R', 'Y', 'B', 'G', 'W']
        idx = {c:i for i,c in enumerate(colors)}
        hand_cnt = [0]*5
        for c in hand:
            hand_cnt[idx[c]] += 1

        def shrink(s: str) -> str:
            while True:
                i = 0
                new_s = []
                changed = False
                n = len(s)
                while i < n:
                    j = i
                    while j < n and s[j] == s[i]:
                        j += 1
                    if j - i >= 3:
                        changed = True
                    else:
                        new_s.append(s[i:j])
                    i = j
                if not changed:
                    break
                s = ''.join(new_s)
            return s

        from functools import lru_cache
        INF = float('inf')

        @lru_cache(None)
        def dfs(board_str: str, hand_state: tuple) -> int:
            if not board_str:
                return 0
            ans = INF
            n = len(board_str)
            hand_list = list(hand_state)

            for i in range(n + 1):
                left = board_str[i-1] if i > 0 else ''
                right = board_str[i] if i < n else ''
                for c_idx in range(5):
                    if hand_list[c_idx] == 0:
                        continue
                    c = colors[c_idx]
                    # prune: insertion must be adjacent to same color to possibly trigger elimination
                    if not (left == c or right == c):
                        continue
                    new_board = board_str[:i] + c + board_str[i:]
                    new_board = shrink(new_board)
                    hand_list[c_idx] -= 1
                    sub = dfs(new_board, tuple(hand_list))
                    if sub != INF:
                        ans = min(ans, 1 + sub)
                    hand_list[c_idx] += 1
            return ans

        res = dfs(board, tuple(hand_cnt))
        return -1 if res == INF else res
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define INF 1000
#define HASH_SIZE 20011

struct Entry {
    char *key;
    int val;
    struct Entry *next;
};

static struct Entry *table[HASH_SIZE];

static unsigned hash_str(const char *s) {
    unsigned h = 0;
    while (*s) {
        h = h * 131 + (unsigned)(*s);
        s++;
    }
    return h % HASH_SIZE;
}

static int getMemo(const char *key, int *outVal) {
    unsigned idx = hash_str(key);
    for (struct Entry *e = table[idx]; e; e = e->next) {
        if (strcmp(e->key, key) == 0) {
            *outVal = e->val;
            return 1;
        }
    }
    return 0;
}

static char *my_strdup(const char *s) {
    size_t n = strlen(s);
    char *p = (char *)malloc(n + 1);
    if (p) memcpy(p, s, n + 1);
    return p;
}

static void setMemo(const char *key, int val) {
    unsigned idx = hash_str(key);
    struct Entry *e = (struct Entry *)malloc(sizeof(struct Entry));
    e->key = my_strdup(key);
    e->val = val;
    e->next = table[idx];
    table[idx] = e;
}

/* Reduce the board by repeatedly removing groups of 3 or more same-colored balls */
static char *reduce_board(const char *s) {
    int n = (int)strlen(s);
    char buf[18];
    memcpy(buf, s, n + 1);
    while (1) {
        int i = 0, m = 0;
        int removed = 0;
        char tmp[18];
        while (i < n) {
            int j = i + 1;
            while (j < n && buf[j] == buf[i]) ++j;
            if (j - i >= 3) {
                removed = 1;               // this segment disappears
            } else {
                for (int k = i; k < j; ++k) tmp[m++] = buf[k];
            }
            i = j;
        }
        tmp[m] = '\0';
        if (!removed) {
            char *res = (char *)malloc(m + 1);
            memcpy(res, tmp, m + 1);
            return res;
        }
        memcpy(buf, tmp, m + 1);
        n = m;
    }
}

/* Depth‑first search with memoization */
static int dfs(char *board, int handCnt[5]) {
    if (board[0] == '\0') return 0;

    char key[32];
    int pos = 0;
    while (board[pos]) { key[pos] = board[pos]; ++pos; }
    key[pos++] = '|';
    for (int i = 0; i < 5; ++i) key[pos++] = '0' + handCnt[i];
    key[pos] = '\0';

    int memoVal;
    if (getMemo(key, &memoVal)) return memoVal;

    int ans = INF;
    int n = (int)strlen(board);

    for (int i = 0; i <= n; ++i) {
        for (int c = 0; c < 5; ++c) if (handCnt[c] > 0) {
            char col = "RYBGW"[c];
            int l = 0, r = 0;
            int idx = i - 1;
            while (idx >= 0 && board[idx] == col) { ++l; --idx; }
            idx = i;
            while (idx < n && board[idx] == col) { ++r; ++idx; }
            if (l + r < 2) continue;   // need at least two existing same‑colored balls

            char nb[18];
            int p = 0;
            for (int k = 0; k < i; ++k) nb[p++] = board[k];
            nb[p++] = col;
            for (int k = i; k < n; ++k) nb[p++] = board[k];
            nb[p] = '\0';

            char *reduced = reduce_board(nb);
            handCnt[c]--;
            int sub = dfs(reduced, handCnt);
            if (sub != INF && sub + 1 < ans) ans = sub + 1;
            handCnt[c]++;
            free(reduced);
        }
    }

    setMemo(key, ans);
    return ans;
}

int findMinStep(char *board, char *hand) {
    int handCnt[5] = {0};
    for (int i = 0; hand[i]; ++i) {
        switch (hand[i]) {
            case 'R': handCnt[0]++; break;
            case 'Y': handCnt[1]++; break;
            case 'B': handCnt[2]++; break;
            case 'G': handCnt[3]++; break;
            case 'W': handCnt[4]++; break;
        }
    }

    int res = dfs(board, handCnt);
    return (res >= INF) ? -1 : res;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    private const int INF = 1000;
    private readonly Dictionary<string, int> _memo = new Dictionary<string, int>();
    private readonly string _colors = "RYBGW";

    public int FindMinStep(string board, string hand) {
        int[] cnt = new int[5];
        foreach (char c in hand) {
            cnt[_colors.IndexOf(c)]++;
        }
        int res = Dfs(board, cnt);
        return res >= INF ? -1 : res;
    }

    private int Dfs(string board, int[] cnt) {
        if (board.Length == 0) return 0;
        string key = board + "#" + Encode(cnt);
        if (_memo.TryGetValue(key, out int cached)) return cached;

        int ans = INF;
        for (int i = 0; i < board.Length;) {
            int j = i;
            while (j < board.Length && board[j] == board[i]) j++;
            int len = j - i;
            int need = 3 - len; // balls needed to eliminate this group
            int colorIdx = _colors.IndexOf(board[i]);

            if (cnt[colorIdx] >= need) {
                cnt[colorIdx] -= need;
                string newBoard = board.Substring(0, i) + board.Substring(j);
                newBoard = Reduce(newBoard);
                int sub = Dfs(newBoard, cnt);
                if (sub < INF) ans = Math.Min(ans, need + sub);
                cnt[colorIdx] += need; // backtrack
            }
            i = j;
        }

        _memo[key] = ans;
        return ans;
    }

    private string Reduce(string s) {
        bool changed = true;
        while (changed) {
            changed = false;
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < s.Length;) {
                int j = i;
                while (j < s.Length && s[j] == s[i]) j++;
                if (j - i >= 3) {
                    // skip this group
                    changed = true;
                } else {
                    sb.Append(s.Substring(i, j - i));
                }
                i = j;
            }
            s = sb.ToString();
        }
        return s;
    }

    private string Encode(int[] cnt) {
        char[] arr = new char[5];
        for (int i = 0; i < 5; i++) arr[i] = (char)('0' + cnt[i]);
        return new string(arr);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} board
 * @param {string} hand
 * @return {number}
 */
var findMinStep = function(board, hand) {
    const colors = ['R','Y','B','G','W'];
    const idxMap = {'R':0,'Y':1,'B':2,'G':3,'W':4};
    const handCnt = new Array(5).fill(0);
    for (let ch of hand) handCnt[idxMap[ch]]++;

    const memo = new Map();

    function shrink(s) {
        let i = 0;
        while (i < s.length) {
            let j = i;
            while (j < s.length && s[j] === s[i]) j++;
            if (j - i >= 3) {
                s = s.slice(0, i) + s.slice(j);
                i = 0; // restart after removal
            } else {
                i = j;
            }
        }
        return s;
    }

    function dfs(bd, cnt) {
        if (bd.length === 0) return 0;
        const key = bd + '#' + cnt.join(',');
        if (memo.has(key)) return memo.get(key);
        let best = Infinity;

        for (let i = 0; i <= bd.length; i++) {
            for (let c = 0; c < 5; c++) {
                if (cnt[c] === 0) continue;
                const color = colors[c];
                // optional pruning: only insert where it can potentially help
                // skip if inserting does not create a group of at least two same-colored balls adjacent
                const leftSame = i > 0 && bd[i - 1] === color;
                const rightSame = i < bd.length && bd[i] === color;
                if (!leftSame && !rightSame) continue;

                cnt[c]--;
                const newBoard = bd.slice(0, i) + color + bd.slice(i);
                const afterShrink = shrink(newBoard);
                const sub = dfs(afterShrink, cnt);
                if (sub !== Infinity) {
                    best = Math.min(best, 1 + sub);
                }
                cnt[c]++;
            }
        }

        memo.set(key, best);
        return best;
    }

    const ans = dfs(board, handCnt);
    return ans === Infinity ? -1 : ans;
};
```

## Typescript

```typescript
function findMinStep(board: string, hand: string): number {
    const colorToIdx = (c: string): number => {
        switch (c) {
            case 'R': return 0;
            case 'Y': return 1;
            case 'B': return 2;
            case 'G': return 3;
            case 'W': return 4;
        }
        return -1;
    };
    const idxToColor = ['R', 'Y', 'B', 'G', 'W'];

    const handCnt = new Array(5).fill(0);
    for (const ch of hand) handCnt[colorToIdx(ch)]++;

    const memo = new Map<string, number>();
    const INF = Number.MAX_SAFE_INTEGER;

    function reduce(s: string): string {
        let i = 0;
        while (i < s.length) {
            let j = i + 1;
            while (j < s.length && s[j] === s[i]) j++;
            if (j - i >= 3) {
                // remove this segment and restart reduction
                return reduce(s.slice(0, i) + s.slice(j));
            }
            i = j;
        }
        return s;
    }

    function dfs(b: string, cnt: number[]): number {
        const key = b + '#' + cnt.join(',');
        if (memo.has(key)) return memo.get(key)!;
        if (b.length === 0) {
            memo.set(key, 0);
            return 0;
        }
        let ans = INF;

        for (let i = 0; i <= b.length; i++) {
            for (let c = 0; c < 5; c++) {
                if (cnt[c] === 0) continue;
                const color = idxToColor[c];
                // avoid inserting the same color consecutively at the same position
                if (i > 0 && b[i - 1] === color) continue;

                const newCnt = cnt.slice();
                newCnt[c]--;
                const newBoard = reduce(b.slice(0, i) + color + b.slice(i));
                const sub = dfs(newBoard, newCnt);
                if (sub !== INF) {
                    ans = Math.min(ans, 1 + sub);
                }
            }
        }

        memo.set(key, ans);
        return ans;
    }

    const res = dfs(board, handCnt);
    return res === INF ? -1 : res;
}
```

## Php

```php
class Solution {
    private $memo = [];

    /**
     * @param String $board
     * @param String $hand
     * @return Integer
     */
    function findMinStep($board, $hand) {
        $cnt = ['R'=>0,'Y'=>0,'B'=>0,'G'=>0,'W'=>0];
        $hLen = strlen($hand);
        for ($i = 0; $i < $hLen; $i++) {
            $c = $hand[$i];
            $cnt[$c]++;
        }
        $res = $this->dfs($board, $cnt);
        return $res === PHP_INT_MAX ? -1 : $res;
    }

    private function compress(string $s): string {
        while (true) {
            $n = strlen($s);
            $i = 0;
            $changed = false;
            while ($i < $n) {
                $j = $i + 1;
                while ($j < $n && $s[$j] === $s[$i]) $j++;
                if ($j - $i >= 3) {
                    $s = substr($s, 0, $i) . substr($s, $j);
                    $changed = true;
                    break;
                }
                $i = $j;
            }
            if (!$changed) break;
        }
        return $s;
    }

    private function dfs(string $board, array $cnt): int {
        if ($board === '') return 0;

        $key = $board . '#';
        foreach (['R','Y','B','G','W'] as $c) {
            $key .= $cnt[$c] . ',';
        }
        if (isset($this->memo[$key])) return $this->memo[$key];

        $ans = PHP_INT_MAX;
        $n = strlen($board);
        for ($i = 0; $i < $n;) {
            $j = $i + 1;
            while ($j < $n && $board[$j] === $board[$i]) $j++;
            $len = $j - $i;
            $c   = $board[$i];
            $need = 3 - $len; // balls needed to eliminate this group
            if ($cnt[$c] >= $need) {
                $use = max($need, 0);
                $newCnt = $cnt;
                if ($use > 0) $newCnt[$c] -= $use;

                $newBoard = substr($board, 0, $i) . substr($board, $j);
                $newBoard = $this->compress($newBoard);

                $temp = $this->dfs($newBoard, $newCnt);
                if ($temp !== PHP_INT_MAX) {
                    $ans = min($ans, $use + $temp);
                }
            }
            $i = $j;
        }

        $this->memo[$key] = $ans;
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    private let colors: [Character] = ["R","Y","B","G","W"]
    private var memo = [String:Int]()
    private let INF = 100
    
    func findMinStep(_ board: String, _ hand: String) -> Int {
        var handCounts = [Int](repeating: 0, count: 5)
        for ch in hand {
            if let idx = colorIndex(ch) {
                handCounts[idx] += 1
            }
        }
        let res = dfs(board, handCounts)
        return res >= INF ? -1 : res
    }
    
    private func dfs(_ board: String, _ handCounts: [Int]) -> Int {
        if board.isEmpty { return 0 }
        let key = board + "#" + handCounts.map{String($0)}.joined(separator:",")
        if let cached = memo[key] { return cached }
        
        var ans = INF
        let boardChars = Array(board)
        for i in 0...boardChars.count {
            for cIdx in 0..<5 where handCounts[cIdx] > 0 {
                var newHand = handCounts
                newHand[cIdx] -= 1
                var newBoardArr = boardChars
                newBoardArr.insert(colors[cIdx], at: i)
                let shrunk = shrink(String(newBoardArr))
                let sub = dfs(shrunk, newHand)
                if sub < INF {
                    ans = min(ans, 1 + sub)
                }
            }
        }
        memo[key] = ans
        return ans
    }
    
    private func shrink(_ s: String) -> String {
        var chars = Array(s)
        var i = 0
        while i < chars.count {
            var j = i + 1
            while j < chars.count && chars[j] == chars[i] {
                j += 1
            }
            if j - i >= 3 {
                chars.removeSubrange(i..<j)
                i = max(i - 1, 0)
            } else {
                i += 1
            }
        }
        return String(chars)
    }
    
    private func colorIndex(_ c: Character) -> Int? {
        switch c {
        case "R": return 0
        case "Y": return 1
        case "B": return 2
        case "G": return 3
        case "W": return 4
        default: return nil
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    private fun charToIdx(c: Char): Int = when (c) {
        'R' -> 0
        'Y' -> 1
        'B' -> 2
        'G' -> 3
        'W' -> 4
        else -> -1
    }

    private fun reduce(board: String): String {
        var s = board
        while (true) {
            val sb = StringBuilder()
            var i = 0
            var changed = false
            while (i < s.length) {
                var j = i
                while (j < s.length && s[j] == s[i]) j++
                if (j - i >= 3) {
                    changed = true
                } else {
                    sb.append(s, i, j)
                }
                i = j
            }
            if (!changed) return s
            s = sb.toString()
        }
    }

    fun findMinStep(board: String, hand: String): Int {
        val handCnt = IntArray(5)
        for (c in hand) handCnt[charToIdx(c)]++
        val startBoard = reduce(board)
        val memo = HashMap<String, Int>()
        val INF = 1 shl 30

        fun dfs(b: String, cnt: IntArray): Int {
            if (b.isEmpty()) return 0
            val key = b + "#" + cnt.joinToString(",")
            memo[key]?.let { return it }

            var ans = INF
            var i = 0
            while (i < b.length) {
                var j = i
                while (j < b.length && b[j] == b[i]) j++
                val len = j - i
                val need = 3 - len
                if (need > 0) {
                    val idx = charToIdx(b[i])
                    if (cnt[idx] >= need) {
                        cnt[idx] -= need
                        var newBoard = b.substring(0, i) + b.substring(j)
                        newBoard = reduce(newBoard)
                        val sub = dfs(newBoard, cnt)
                        if (sub != INF) {
                            ans = minOf(ans, sub + need)
                        }
                        cnt[idx] += need
                    }
                }
                i = j
            }

            memo[key] = ans
            return ans
        }

        val res = dfs(startBoard, handCnt)
        return if (res == INF) -1 else res
    }
}
```

## Dart

```dart
class Solution {
  late List<int> _handCount;
  final Map<String, int> _memo = {};
  static const int _INF = 1 << 30;

  int findMinStep(String board, String hand) {
    _handCount = List.filled(5, 0);
    for (int i = 0; i < hand.length; i++) {
      _handCount[_idx(hand[i])]++;
    }
    _memo.clear();
    int res = _dfs(board);
    return res == _INF ? -1 : res;
  }

  int _dfs(String board) {
    board = _shrink(board);
    if (board.isEmpty) return 0;
    String key = board + '#' + _handCount.join(',');
    if (_memo.containsKey(key)) return _memo[key]!;

    int ans = _INF;
    for (int i = 0; i < board.length;) {
      int j = i + 1;
      while (j < board.length && board[j] == board[i]) j++;
      int len = j - i;
      int need = 3 - len;
      int idx = _idx(board[i]);
      if (need > 0 && _handCount[idx] >= need) {
        _handCount[idx] -= need;
        String newBoard = board.substring(0, i) + board.substring(j);
        int temp = _dfs(newBoard);
        if (temp != _INF) ans = ans < temp + need ? ans : temp + need;
        _handCount[idx] += need;
      }
      i = j;
    }

    _memo[key] = ans;
    return ans;
  }

  String _shrink(String s) {
    bool changed = false;
    StringBuffer sb = StringBuffer();
    for (int i = 0; i < s.length;) {
      int j = i + 1;
      while (j < s.length && s[j] == s[i]) j++;
      if (j - i >= 3) {
        changed = true;
      } else {
        sb.write(s.substring(i, j));
      }
      i = j;
    }
    String res = sb.toString();
    return changed ? _shrink(res) : res;
  }

  int _idx(String c) {
    switch (c) {
      case 'R':
        return 0;
      case 'Y':
        return 1;
      case 'B':
        return 2;
      case 'G':
        return 3;
      case 'W':
        return 4;
    }
    return -1; // should never happen
  }
}
```

## Golang

```go
package main

import (
	"fmt"
)

var memo map[string]int
var colors = []byte{'R', 'Y', 'B', 'G', 'W'}

func findMinStep(board string, hand string) int {
	memo = make(map[string]int)
	var cnt [5]int
	for i := 0; i < len(hand); i++ {
		switch hand[i] {
		case 'R':
			cnt[0]++
		case 'Y':
			cnt[1]++
		case 'B':
			cnt[2]++
		case 'G':
			cnt[3]++
		case 'W':
			cnt[4]++
		}
	}
	res := dfs(board, cnt)
	if res == -1 {
		return -1
	}
	return res
}

func dfs(b string, hand [5]int) int {
	if b == "" {
		return 0
	}
	key := fmt.Sprintf("%s#%d%d%d%d%d", b, hand[0], hand[1], hand[2], hand[3], hand[4])
	if v, ok := memo[key]; ok {
		return v
	}
	const INF = 100
	best := INF

	for i := 0; i <= len(b); i++ {
		for ci := 0; ci < 5; ci++ {
			if hand[ci] == 0 {
				continue
			}
			c := colors[ci]
			// prune: need at least one adjacent same color to have chance of elimination
			if !(i > 0 && b[i-1] == c) && !(i < len(b) && b[i] == c) {
				continue
			}
			hand[ci]--
			newBoard := collapse(b[:i] + string(c) + b[i:])
			sub := dfs(newBoard, hand)
			if sub != -1 && 1+sub < best {
				best = 1 + sub
			}
			hand[ci]++
		}
	}

	if best == INF {
		memo[key] = -1
	} else {
		memo[key] = best
	}
	return memo[key]
}

// collapse removes any consecutive groups of three or more balls, repeatedly.
func collapse(s string) string {
	n := len(s)
	i := 0
	for i < n {
		j := i + 1
		for j < n && s[j] == s[i] {
			j++
		}
		if j-i >= 3 {
			// remove group and recurse on the new string
			return collapse(s[:i] + s[j:])
		}
		i = j
	}
	return s
}
```

## Ruby

```ruby
def find_min_step(board, hand)
  colors = ['R', 'Y', 'B', 'G', 'W']
  hand_counts = Array.new(5, 0)
  hand.each_char { |c| hand_counts[colors.index(c)] += 1 }

  memo = {}

  shrink = lambda do |s|
    loop do
      changed = false
      i = 0
      new_s = ''
      while i < s.length
        j = i + 1
        j += 1 while j < s.length && s[j] == s[i]
        if j - i >= 3
          changed = true
        else
          new_s << s[i...j]
        end
        i = j
      end
      break unless changed
      s = new_s
    end
    s
  end

  dfs = lambda do |b, cnt|
    return 0 if b.empty?
    key = b + '#' + cnt.join(',')
    return memo[key] if memo.key?(key)

    ans = Float::INFINITY

    (0..b.length).each do |i|
      colors.each_with_index do |col, idx|
        next if cnt[idx] == 0

        # check usefulness of this insertion
        left_len = 0
        l = i - 1
        while l >= 0 && b[l] == col
          left_len += 1
          l -= 1
        end
        right_len = 0
        r = i
        while r < b.length && b[r] == col
          right_len += 1
          r += 1
        end

        next if left_len + right_len < 2 && cnt[idx] < 2

        new_board = b[0...i] + col + b[i..-1]
        new_board = shrink.call(new_board)

        cnt[idx] -= 1
        sub = dfs.call(new_board, cnt)
        cnt[idx] += 1

        if sub != Float::INFINITY
          ans = [ans, 1 + sub].min
        end
      end
    end

    memo[key] = ans
    ans
  end

  res = dfs.call(board, hand_counts)
  res == Float::INFINITY ? -1 : res
end
```

## Scala

```scala
object Solution {
  def findMinStep(board: String, hand: String): Int = {
    val colors = "RYBGW"
    def idx(c: Char): Int = colors.indexOf(c)

    val cnt = Array.fill(5)(0)
    for (c <- hand) cnt(idx(c)) += 1

    import scala.collection.mutable
    val memo = mutable.Map[String, Int]()

    def compress(s: String): String = {
      var str = s
      var changed = true
      while (changed) {
        var i = 0
        val sb = new StringBuilder
        changed = false
        while (i < str.length) {
          var j = i + 1
          while (j < str.length && str.charAt(j) == str.charAt(i)) j += 1
          if (j - i >= 3) {
            changed = true
          } else {
            sb.append(str.substring(i, j))
          }
          i = j
        }
        str = sb.toString()
      }
      str
    }

    val INF = 1000

    def dfs(b: String): Int = {
      if (b.isEmpty) return 0
      val key = b + "#" + cnt.mkString(",")
      memo.getOrElseUpdate(key, {
        var ans = INF
        var i = 0
        while (i < b.length) {
          var j = i + 1
          while (j < b.length && b.charAt(j) == b.charAt(i)) j += 1
          val need = 3 - (j - i)
          if (need <= 2 && cnt(idx(b.charAt(i))) >= need) {
            cnt(idx(b.charAt(i))) -= need
            var newBoard = b.substring(0, i) + (b.charAt(i).toString * need) + b.substring(i)
            newBoard = compress(newBoard)
            val sub = dfs(newBoard)
            if (sub != INF) ans = math.min(ans, need + sub)
            cnt(idx(b.charAt(i))) += need
          }
          i = j
        }
        ans
      })
    }

    val res = dfs(board)
    if (res >= INF) -1 else res
  }
}
```

## Rust

```rust
use std::collections::HashMap;

const INF: i32 = 100;
static COLORS: [char; 5] = ['R', 'Y', 'B', 'G', 'W'];

fn shrink(s: &str) -> String {
    let mut cur = s.to_string();
    loop {
        let chars: Vec<char> = cur.chars().collect();
        let n = chars.len();
        let mut i = 0;
        let mut changed = false;
        let mut next = String::new();
        while i < n {
            let mut j = i + 1;
            while j < n && chars[j] == chars[i] {
                j += 1;
            }
            if j - i >= 3 {
                changed = true;
            } else {
                for k in i..j {
                    next.push(chars[k]);
                }
            }
            i = j;
        }
        if !changed {
            return cur;
        }
        cur = next;
    }
}

fn dfs(board: String, hand: [i32; 5], memo: &mut HashMap<String, i32>) -> i32 {
    if board.is_empty() {
        return 0;
    }
    // build key
    let mut key = board.clone();
    key.push('#');
    for cnt in hand.iter() {
        key.push_str(&cnt.to_string());
        key.push(',');
    }
    if let Some(&v) = memo.get(&key) {
        return v;
    }

    let n = board.len();
    let mut ans = INF;

    for i in 0..=n {
        for (ci, &c) in COLORS.iter().enumerate() {
            if hand[ci] == 0 {
                continue;
            }
            // insert c at position i
            let mut new_board = String::with_capacity(n + 1);
            new_board.push_str(&board[..i]);
            new_board.push(c);
            new_board.push_str(&board[i..]);

            let shrunk = shrink(&new_board);

            let mut new_hand = hand;
            new_hand[ci] -= 1;

            let sub = dfs(shrunk, new_hand, memo);
            if sub != INF {
                ans = ans.min(1 + sub);
            }
        }
    }

    memo.insert(key, ans);
    ans
}

impl Solution {
    pub fn find_min_step(board: String, hand: String) -> i32 {
        let mut hand_counts = [0i32; 5];
        for ch in hand.chars() {
            let idx = match ch {
                'R' => 0,
                'Y' => 1,
                'B' => 2,
                'G' => 3,
                'W' => 4,
                _ => continue,
            };
            hand_counts[idx] += 1;
        }
        let mut memo: HashMap<String, i32> = HashMap::new();
        let res = dfs(board, hand_counts, &mut memo);
        if res >= INF {
            -1
        } else {
            res
        }
    }
}
```

## Racket

```racket
(define (char->idx c)
  (cond [(char=? c #\R) 0]
        [(char=? c #\Y) 1]
        [(char=? c #\B) 2]
        [(char=? c #\G) 3]
        [else 4]))

(define (hand-decr hand idx)
  (let loop ((i 0) (lst hand) (out '()))
    (if (null? lst)
        (reverse out)
        (let ((v (car lst)))
          (loop (+ i 1) (cdr lst)
                (cons (if (= i idx) (- v 1) v) out))))))

(define (shrink s)
  (let loop ((str s))
    (let ((n (string-length str)))
      (let inner ((i 0) (changed #f) (out ""))
        (if (= i n)
            (if changed
                (loop out)
                out)
            (let* ((c (string-ref str i))
                   (j (let find ((k i))
                        (if (and (< k n) (char=? (string-ref str k) c))
                            (find (+ k 1))
                            k)))
                   (len (- j i)))
              (if (>= len 3)
                  (inner j #t out)
                  (inner j changed (string-append out (substring str i j))))))))))

(define/contract (find-min-step board hand)
  (-> string? string? exact-integer?)
  (let* ((vec (make-vector 5 0))
         (len-hand (string-length hand)))
    (for ([i (in-range len-hand)])
      (let* ((c (string-ref hand i))
             (idx (char->idx c)))
        (vector-set! vec idx (+ (vector-ref vec idx) 1))))
    (define hand-counts (vector->list vec))
    (define memo (make-hash))
    (define INF 1000)
    (define colors (list #\R #\Y #\B #\G #\W))
    (define (hand-key h)
      (format "~a,~a,~a,~a,~a"
              (list-ref h 0) (list-ref h 1) (list-ref h 2) (list-ref h 3) (list-ref h 4)))
    (letrec ((dfs (lambda (b hd)
                    (define key (string-append b "|" (hand-key hd)))
                    (if (hash-has-key? memo key)
                        (hash-ref memo key)
                        (begin
                          (define res
                            (cond [(zero? (string-length b)) 0]
                                  [else
                                   (let loop-pos ((pos 0) (best INF))
                                     (if (> pos (string-length b))
                                         best
                                         (let inner-loop ((cidx 0) (cur-best best))
                                           (if (= cidx 5)
                                               (loop-pos (+ pos 1) cur-best)
                                               (if (> (list-ref hd cidx) 0)
                                                   (let* ((ch (list-ref colors cidx))
                                                          (newb (string-append (substring b 0 pos)
                                                                               (string ch)
                                                                               (substring b pos)))
                                                          (shrun (shrink newb))
                                                          (newhd (hand-decr hd cidx))
                                                          (sub (dfs shrun newhd)))
                                                     (if (< sub INF)
                                                         (inner-loop (+ cidx 1) (min cur-best (+ 1 sub)))
                                                         (inner-loop (+ cidx 1) cur-best)))
                                                   (inner-loop (+ cidx 1) cur-best))))))]))
                          (hash-set! memo key res)
                          res)))))
      (let ((ans (dfs board hand-counts)))
        (if (>= ans INF) -1 ans)))))
```

## Erlang

```erlang
-module(solution).
-export([find_min_step/2]).

-define(INF, 1000).

-spec find_min_step(Board :: unicode:unicode_binary(), Hand :: unicode:unicode_binary()) -> integer().
find_min_step(BoardBin, HandBin) ->
    Board = binary_to_list(BoardBin),
    HandCounts = hand_counts_from_string(binary_to_list(HandBin)),
    {Res, _} = dfs(Board, HandCounts, #{}),
    case Res of
        ?INF -> -1;
        _ -> Res
    end.

%% Build hand counts tuple {R,Y,B,G,W}
hand_counts_from_string(Str) ->
    lists:foldl(fun(Char, Tuple) ->
        Pos = idx(Char),
        Count = element(Pos, Tuple),
        setelement(Pos, Tuple, Count + 1)
    end, {0,0,0,0,0}, Str).

idx($R) -> 1;
idx($Y) -> 2;
idx($B) -> 3;
idx($G) -> 4;
idx($W) -> 5.

%% Depth‑first search with memoization
dfs(Board, HandCounts, Memo) when Board == [] ->
    {0, Memo};
dfs(Board, HandCounts, Memo) ->
    Key = {list_to_binary(Board), HandCounts},
    case maps:find(Key, Memo) of
        {ok, Val} -> {Val, Memo};
        error ->
            Len = length(Board),
            Colors = [$R,$Y,$B,$G,$W],
            {MinRes, NewMemo} = dfs_positions(0, Len, Board, HandCounts, Memo, ?INF, Colors),
            UpdatedMemo = maps:put(Key, MinRes, NewMemo),
            {MinRes, UpdatedMemo}
    end.

%% Iterate over insertion positions
dfs_positions(Pos, MaxPos, _Board, _HandCounts, Memo, Min, _Colors) when Pos > MaxPos ->
    {Min, Memo};
dfs_positions(Pos, MaxPos, Board, HandCounts, Memo0, Min0, Colors) ->
    {Min1, Memo1} = dfs_colors_at_pos(Colors, 1, Pos, Board, HandCounts, Memo0, Min0),
    dfs_positions(Pos + 1, MaxPos, Board, HandCounts, Memo1, Min1, Colors).

%% Iterate over colors
dfs_colors_at_pos([], _Idx, _Pos, _Board, _HandCounts, Memo, Min) ->
    {Min, Memo};
dfs_colors_at_pos([Color|Rest], Idx, Pos, Board, HandCounts, Memo0, Min0) ->
    Count = element(Idx, HandCounts),
    case Count of
        0 ->
            dfs_colors_at_pos(Rest, Idx + 1, Pos, Board, HandCounts, Memo0, Min0);
        _ ->
            NewHand = setelement(Idx, HandCounts, Count - 1),
            NewBoard = insert_and_shrink(Board, Pos, Color),
            {SubRes, Memo1} = dfs(NewBoard, NewHand, Memo0),
            UpdatedMin = 
                case SubRes of
                    ?INF -> Min0;
                    _ ->
                        Val = SubRes + 1,
                        if Val < Min0 -> Val; true -> Min0 end
                end,
            dfs_colors_at_pos(Rest, Idx + 1, Pos, Board, HandCounts, Memo1, UpdatedMin)
    end.

%% Insert a ball and repeatedly eliminate groups >=3
insert_and_shrink(Board, Pos, Char) ->
    {Left, Right} = lists:split(Pos, Board),
    shrink(Left ++ [Char] ++ Right).

shrink(Board) ->
    case remove_once(Board) of
        {true, NewBoard} -> shrink(NewBoard);
        {false, Board} -> Board
    end.

%% Remove one pass of groups >=3
remove_once(List) -> remove_once(List, [], false).

remove_once([], RevAcc, Changed) ->
    {Changed, lists:reverse(RevAcc)};
remove_once([H|T], RevAcc, Changed) ->
    {Cnt, Rest} = count_same(T, H, 1),
    if Cnt >= 3 ->
            remove_once(Rest, RevAcc, true);
       true ->
            NewRevAcc = add_n_rev(H, Cnt, RevAcc),
            remove_once(Rest, NewRevAcc, Changed)
    end.

%% Count consecutive same chars; returns {Count, RestList}
count_same([], _Char, Count) -> {Count, []};
count_same([H|T], Char, Count) when H =:= Char ->
    count_same(T, Char, Count + 1);
count_same(Rest, _Char, Count) -> {Count, Rest}.

%% Add N copies of Char to reversed accumulator
add_n_rev(_Char, 0, Acc) -> Acc;
add_n_rev(Char, N, Acc) when N > 0 ->
    add_n_rev(Char, N - 1, [Char|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_min_step(board :: String.t(), hand :: String.t()) :: integer()
  def find_min_step(board, hand) do
    hand_counts =
      hand
      |> String.to_charlist()
      |> Enum.reduce(%{}, fn c, acc -> Map.update(acc, c, 1, &(&1 + 1)) end)

    {res, _} = dfs(board, hand_counts, %{})
    if res >= @inf, do: -1, else: res
  end

  @inf 1_000
  @colors [?R, ?Y, ?B, ?G, ?W]

  defp dfs(board, hand_counts, memo) do
    key = {board, hand_key(hand_counts)}
    case Map.fetch(memo, key) do
      {:ok, val} ->
        {val, memo}

      :error ->
        if board == "" do
          {0, Map.put(memo, key, 0)}
        else
          len = String.length(board)
          {best, new_memo} =
            Enum.reduce(0..len, {@inf, memo}, fn pos, {cur_best, cur_memo} ->
              Enum.reduce(@colors, {cur_best, cur_memo}, fn color, {inner_best, inner_memo} ->
                cnt = Map.get(hand_counts, color, 0)

                if cnt == 0 do
                  {inner_best, inner_memo}
                else
                  left_same =
                    pos > 0 and String.at(board, pos - 1) == <<color>>

                  right_same =
                    pos < len and String.at(board, pos) == <<color>>

                  if not (left_same or right_same) do
                    {inner_best, inner_memo}
                  else
                    new_board = insert_and_collapse(board, color, pos)
                    new_hand = Map.update!(hand_counts, color, &(&1 - 1))

                    {steps, updated_memo} = dfs(new_board, new_hand, inner_memo)

                    if steps < @inf do
                      min_steps = 1 + steps
                      {Enum.min(inner_best, min_steps), updated_memo}
                    else
                      {inner_best, updated_memo}
                    end
                  end
                end
              end)
            end)

          final_val = best
          {final_val, Map.put(new_memo, key, final_val)}
        end
    end
  end

  defp hand_key(counts) do
    {
      Map.get(counts, ?R, 0),
      Map.get(counts, ?Y, 0),
      Map.get(counts, ?B, 0),
      Map.get(counts, ?G, 0),
      Map.get(counts, ?W, 0)
    }
  end

  defp insert_and_collapse(board, color, pos) do
    lst = String.to_charlist(board)
    new_lst = List.insert_at(lst, pos, color)
    collapsed = collapse(new_lst)
    List.to_string(collapsed)
  end

  defp collapse(lst) do
    case remove_once(lst) do
      {new_lst, true} -> collapse(new_lst)
      {new_lst, false} -> new_lst
    end
  end

  defp remove_once(lst) do
    {rev_res, removed} = do_remove_once(lst, [], false)
    {Enum.reverse(rev_res), removed}
  end

  defp do_remove_once([], acc, removed), do: {acc, removed}

  defp do_remove_once([h | t], acc, removed) do
    {run, rest} = Enum.split_while(t, fn x -> x == h end)
    len = length(run) + 1

    if len >= 3 do
      do_remove_once(rest, acc, true)
    else
      new_acc = Enum.reduce(run, [h | acc], fn x, a -> [x | a] end)
      do_remove_once(rest, new_acc, removed)
    end
  end
end
```
