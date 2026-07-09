# 1138. Alphabet Board Path

## Cpp

```cpp
class Solution {
public:
    string alphabetBoardPath(string target) {
        vector<pair<int,int>> pos(26);
        for (int i = 0; i < 26; ++i) {
            int r = i / 5;
            int c = i % 5;
            if (r == 5) c = 0; // only 'z' at (5,0)
            pos[i] = {r, c};
        }
        string ans;
        int curR = 0, curC = 0;
        for (char ch : target) {
            auto [tr, tc] = pos[ch - 'a'];
            if (tr == 5) { // moving to 'z', horizontal first
                while (curC > tc) { ans.push_back('L'); --curC; }
                while (curC < tc) { ans.push_back('R'); ++curC; }
                while (curR > tr) { ans.push_back('U'); --curR; }
                while (curR < tr) { ans.push_back('D'); ++curR; }
            } else {
                while (curR > tr) { ans.push_back('U'); --curR; }
                while (curR < tr) { ans.push_back('D'); ++curR; }
                while (curC > tc) { ans.push_back('L'); --curC; }
                while (curC < tc) { ans.push_back('R'); ++curC; }
            }
            ans.push_back('!');
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String alphabetBoardPath(String target) {
        int[] rows = new int[26];
        int[] cols = new int[26];
        for (int i = 0; i < 26; i++) {
            if (i == 25) { // 'z'
                rows[i] = 5;
                cols[i] = 0;
            } else {
                rows[i] = i / 5;
                cols[i] = i % 5;
            }
        }

        StringBuilder sb = new StringBuilder();
        int curR = 0, curC = 0;

        for (char ch : target.toCharArray()) {
            int idx = ch - 'a';
            int tr = rows[idx];
            int tc = cols[idx];

            // move up first
            while (curR > tr) {
                sb.append('U');
                curR--;
            }
            // move left
            while (curC > tc) {
                sb.append('L');
                curC--;
            }
            // move right
            while (curC < tc) {
                sb.append('R');
                curC++;
            }
            // move down
            while (curR < tr) {
                sb.append('D');
                curR++;
            }

            sb.append('!');
        }

        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        pos = {}
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                pos[ch] = (i, j)

        cur_r, cur_c = 0, 0
        res = []
        for ch in target:
            tr, tc = pos[ch]
            dr, dc = tr - cur_r, tc - cur_c

            if ch == 'z':
                # move horizontally first then down
                if dc < 0:
                    res.append('L' * (-dc))
                elif dc > 0:
                    res.append('R' * dc)
                if dr > 0:
                    res.append('D' * dr)
                if dr < 0:
                    res.append('U' * (-dr))
            else:
                if dr < 0:
                    res.append('U' * (-dr))
                if dc < 0:
                    res.append('L' * (-dc))
                if dc > 0:
                    res.append('R' * dc)
                if dr > 0:
                    res.append('D' * dr)

            res.append('!')
            cur_r, cur_c = tr, tc

        return ''.join(res)
```

## Python3

```python
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        pos = {}
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                pos[ch] = (i, j)
        cur_r, cur_c = 0, 0
        ans = []
        for ch in target:
            tr, tc = pos[ch]
            while cur_r > tr:
                ans.append('U')
                cur_r -= 1
            while cur_c > tc:
                ans.append('L')
                cur_c -= 1
            while cur_r < tr:
                ans.append('D')
                cur_r += 1
            while cur_c < tc:
                ans.append('R')
                cur_c += 1
            ans.append('!')
        return ''.join(ans)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char *alphabetBoardPath(char *target) {
    int len = strlen(target);
    int capacity = len * 15 + 1; // sufficient buffer
    char *res = (char *)malloc(capacity);
    int pos = 0;
    int cur_r = 0, cur_c = 0;

    for (int i = 0; i < len; ++i) {
        int idx = target[i] - 'a';
        int tr = idx / 5;
        int tc = idx % 5;

        while (cur_r > tr) { res[pos++] = 'U'; cur_r--; }
        while (cur_c > tc) { res[pos++] = 'L'; cur_c--; }
        while (cur_r < tr) { res[pos++] = 'D'; cur_r++; }
        while (cur_c < tc) { res[pos++] = 'R'; cur_c++; }

        res[pos++] = '!';
    }
    res[pos] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string AlphabetBoardPath(string target) {
        // Precompute positions for each letter
        var pos = new (int row, int col)[26];
        for (int i = 0; i < 26; i++) {
            int r = i / 5;
            int c = i % 5;
            if (i == 25) { // 'z' is at (5,0)
                r = 5;
                c = 0;
            }
            pos[i] = (r, c);
        }

        var sb = new System.Text.StringBuilder();
        int curRow = 0, curCol = 0;

        foreach (char ch in target) {
            var (tr, tc) = pos[ch - 'a'];
            // Move up
            while (curRow > tr) {
                sb.Append('U');
                curRow--;
            }
            // Move left
            while (curCol > tc) {
                sb.Append('L');
                curCol--;
            }
            // Move down
            while (curRow < tr) {
                sb.Append('D');
                curRow++;
            }
            // Move right
            while (curCol < tc) {
                sb.Append('R');
                curCol++;
            }
            sb.Append('!');
        }

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} target
 * @return {string}
 */
var alphabetBoardPath = function(target) {
    const pos = {};
    for (let i = 0; i < 26; ++i) {
        const r = Math.floor(i / 5);
        const c = i % 5;
        pos[String.fromCharCode(97 + i)] = [r, c];
    }
    let curR = 0, curC = 0;
    let res = '';
    for (const ch of target) {
        const [tr, tc] = pos[ch];
        const dr = tr - curR;
        const dc = tc - curC;
        if (dr < 0) res += 'U'.repeat(-dr);
        if (dc < 0) res += 'L'.repeat(-dc);
        if (dr > 0) res += 'D'.repeat(dr);
        if (dc > 0) res += 'R'.repeat(dc);
        res += '!';
        curR = tr;
        curC = tc;
    }
    return res;
};
```

## Typescript

```typescript
function alphabetBoardPath(target: string): string {
    const pos = new Map<string, [number, number]>();
    const boardRows = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"];
    for (let r = 0; r < boardRows.length; ++r) {
        const row = boardRows[r];
        for (let c = 0; c < row.length; ++c) {
            pos.set(row[c], [r, c]);
        }
    }

    let curR = 0, curC = 0;
    let result = '';
    for (const ch of target) {
        const [tr, tc] = pos.get(ch)!;

        while (curR > tr) { result += 'U'; curR--; }
        while (curC > tc) { result += 'L'; curC--; }
        while (curR < tr) { result += 'D'; curR++; }
        while (curC < tc) { result += 'R'; curC++; }

        result += '!';
    }
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param String $target
     * @return String
     */
    function alphabetBoardPath($target) {
        $result = '';
        $curRow = 0;
        $curCol = 0;
        $n = strlen($target);
        for ($i = 0; $i < $n; $i++) {
            $ch = $target[$i];
            $idx = ord($ch) - ord('a');
            $tgtRow = intdiv($idx, 5);
            $tgtCol = $idx % 5;
            $dr = $tgtRow - $curRow;
            $dc = $tgtCol - $curCol;
            if ($dr < 0) {
                $result .= str_repeat('U', -$dr);
            }
            if ($dc < 0) {
                $result .= str_repeat('L', -$dc);
            }
            if ($dr > 0) {
                $result .= str_repeat('D', $dr);
            }
            if ($dc > 0) {
                $result .= str_repeat('R', $dc);
            }
            $result .= '!';
            $curRow = $tgtRow;
            $curCol = $tgtCol;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func alphabetBoardPath(_ target: String) -> String {
        var positions = [(Int, Int)](repeating: (0, 0), count: 26)
        for i in 0..<26 {
            let r = i / 5
            let c = i % 5
            positions[i] = (r, c)
        }
        
        var curR = 0
        var curC = 0
        var result = ""
        
        for ch in target {
            let idx = Int(ch.asciiValue! - Character("a").asciiValue!)
            let (tr, tc) = positions[idx]
            
            if tr < curR {
                result += String(repeating: "U", count: curR - tr)
            }
            if tc < curC {
                result += String(repeating: "L", count: curC - tc)
            }
            if tr > curR {
                result += String(repeating: "D", count: tr - curR)
            }
            if tc > curC {
                result += String(repeating: "R", count: tc - curC)
            }
            
            result.append("!")
            curR = tr
            curC = tc
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun alphabetBoardPath(target: String): String {
        val pos = Array(26) { IntArray(2) }
        for (i in 0 until 26) {
            val r = if (i == 25) 5 else i / 5
            val c = if (i == 25) 0 else i % 5
            pos[i][0] = r
            pos[i][1] = c
        }
        val sb = StringBuilder()
        var curR = 0
        var curC = 0
        for (ch in target) {
            val idx = ch - 'a'
            val tr = pos[idx][0]
            val tc = pos[idx][1]
            if (tr == 5 && tc == 0) { // moving to 'z', horizontal first
                while (curC > tc) { sb.append('L'); curC-- }
                while (curC < tc) { sb.append('R'); curC++ }
                while (curR > tr) { sb.append('U'); curR-- }
                while (curR < tr) { sb.append('D'); curR++ }
            } else {
                while (curR > tr) { sb.append('U'); curR-- }
                while (curR < tr) { sb.append('D'); curR++ }
                while (curC > tc) { sb.append('L'); curC-- }
                while (curC < tc) { sb.append('R'); curC++ }
            }
            sb.append('!')
        }
        return sb.toString()
    }
}
```

## Golang

```go
func alphabetBoardPath(target string) string {
    positions := make([][2]int, 26)
    board := []string{"abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"}
    for i, row := range board {
        for j, ch := range row {
            positions[ch-'a'] = [2]int{i, j}
        }
    }

    var sb strings.Builder
    r, c := 0, 0
    for _, ch := range target {
        tr, tc := positions[ch-'a'][0], positions[ch-'a'][1]

        for r > tr {
            sb.WriteByte('U')
            r--
        }
        for c > tc {
            sb.WriteByte('L')
            c--
        }
        for r < tr {
            sb.WriteByte('D')
            r++
        }
        for c < tc {
            sb.WriteByte('R')
            c++
        }
        sb.WriteByte('!')
    }
    return sb.String()
}
```

## Ruby

```ruby
def alphabet_board_path(target)
  board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
  pos = {}
  board.each_with_index do |row, r|
    row.chars.each_with_index { |ch, c| pos[ch] = [r, c] }
  end

  cur_r = 0
  cur_c = 0
  result = +""

  target.each_char do |ch|
    tr, tc = pos[ch]
    dr = tr - cur_r
    dc = tc - cur_c

    if ch == 'z'
      # move horizontally first, then vertically
      if dc < 0
        result << 'L' * (-dc)
      elsif dc > 0
        result << 'R' * dc
      end
      if dr < 0
        result << 'U' * (-dr)
      elsif dr > 0
        result << 'D' * dr
      end
    else
      # move vertically up first, then horizontally, then down
      if dr < 0
        result << 'U' * (-dr)
      end
      if dc < 0
        result << 'L' * (-dc)
      end
      if dr > 0
        result << 'D' * dr
      end
      if dc > 0
        result << 'R' * dc
      end
    end

    result << '!'
    cur_r, cur_c = tr, tc
  end

  result
end
```

## Scala

```scala
object Solution {
    def alphabetBoardPath(target: String): String = {
        val sb = new StringBuilder
        var curRow = 0
        var curCol = 0
        for (ch <- target) {
            val idx = ch - 'a'
            val tr = idx / 5
            val tc = idx % 5
            while (curRow > tr) { sb.append('U'); curRow -= 1 }
            while (curCol > tc) { sb.append('L'); curCol -= 1 }
            while (curRow < tr) { sb.append('D'); curRow += 1 }
            while (curCol < tc) { sb.append('R'); curCol += 1 }
            sb.append('!')
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn alphabet_board_path(target: String) -> String {
        // Precompute positions of each letter on the board.
        let mut pos = vec![(0i32, 0i32); 26];
        let rows = [
            "abcde",
            "fghij",
            "klmno",
            "pqrst",
            "uvwxy",
            "z",
        ];
        for (i, row) in rows.iter().enumerate() {
            for (j, ch) in row.chars().enumerate() {
                let idx = (ch as u8 - b'a') as usize;
                pos[idx] = (i as i32, j as i32);
            }
        }

        let mut cur_r = 0i32;
        let mut cur_c = 0i32;
        let mut ans = String::new();

        for ch in target.chars() {
            let idx = (ch as u8 - b'a') as usize;
            let (tr, tc) = pos[idx];

            // Move up first
            while cur_r > tr {
                ans.push('U');
                cur_r -= 1;
            }
            // Then left
            while cur_c > tc {
                ans.push('L');
                cur_c -= 1;
            }
            // Then down
            while cur_r < tr {
                ans.push('D');
                cur_r += 1;
            }
            // Finally right
            while cur_c < tc {
                ans.push('R');
                cur_c += 1;
            }

            ans.push('!');
        }

        ans
    }
}
```
