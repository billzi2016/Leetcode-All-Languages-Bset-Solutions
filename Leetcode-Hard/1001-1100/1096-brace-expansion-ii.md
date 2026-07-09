# 1096. Brace Expansion II

## Cpp

```cpp
class Solution {
public:
    vector<string> braceExpansionII(string expression) {
        s = expression;
        n = s.size();
        int idx = 0;
        unordered_set<string> resultSet = parseExpression(idx);
        vector<string> result(resultSet.begin(), resultSet.end());
        sort(result.begin(), result.end());
        return result;
    }
private:
    string s;
    int n;
    
    unordered_set<string> parseExpression(int& i) {
        unordered_set<string> res = parseTerm(i);
        while (i < n && s[i] == ',') {
            ++i; // skip ','
            unordered_set<string> termSet = parseTerm(i);
            for (const string& str : termSet) {
                res.insert(str);
            }
        }
        return res;
    }
    
    unordered_set<string> parseTerm(int& i) {
        unordered_set<string> cur;
        cur.insert(""); // start with empty string for concatenation
        while (i < n && s[i] != '}' && s[i] != ',') {
            unordered_set<string> factorSet = parseFactor(i);
            unordered_set<string> next;
            for (const string& a : cur) {
                for (const string& b : factorSet) {
                    next.insert(a + b);
                }
            }
            cur.swap(next);
        }
        return cur;
    }
    
    unordered_set<string> parseFactor(int& i) {
        if (s[i] == '{') {
            ++i; // skip '{'
            unordered_set<string> inner = parseExpression(i);
            ++i; // skip '}'
            return inner;
        } else { // a single letter
            char c = s[i++];
            return unordered_set<string>{string(1, c)};
        }
    }
};
```

## Java

```java
class Solution {
    private int idx;

    public List<String> braceExpansionII(String expression) {
        idx = 0;
        Set<String> resultSet = parseExpression(expression);
        List<String> resultList = new ArrayList<>(resultSet);
        Collections.sort(resultList);
        return resultList;
    }

    // Parses an Expression: Term {',' Term}*
    private Set<String> parseExpression(String s) {
        Set<String> termSet = parseTerm(s);
        Set<String> result = new HashSet<>(termSet);
        while (idx < s.length() && s.charAt(idx) == ',') {
            idx++; // skip ','
            Set<String> nextTerm = parseTerm(s);
            result.addAll(nextTerm);
        }
        return result;
    }

    // Parses a Term: Factor {Factor}*
    private Set<String> parseTerm(String s) {
        Set<String> factorSet = parseFactor(s);
        while (idx < s.length()) {
            char c = s.charAt(idx);
            if (c == ',' || c == '}') break;
            Set<String> nextFactor = parseFactor(s);
            Set<String> combined = new HashSet<>();
            for (String a : factorSet) {
                for (String b : nextFactor) {
                    combined.add(a + b);
                }
            }
            factorSet = combined;
        }
        return factorSet;
    }

    // Parses a Factor: Letter | '{' Expression '}'
    private Set<String> parseFactor(String s) {
        char c = s.charAt(idx);
        if (c == '{') {
            idx++; // skip '{'
            Set<String> inner = parseExpression(s);
            idx++; // skip '}'
            return inner;
        } else { // single letter
            idx++;
            return new HashSet<>(Collections.singletonList(String.valueOf(c)));
        }
    }
}
```

## Python

```python
class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        self.s = expression
        self.n = len(expression)

        def parse_expr(i):
            # Parse Term then handle unions separated by ','
            cur_set, i = parse_term(i)
            while i < self.n and self.s[i] == ',':
                i += 1  # skip ','
                next_set, i = parse_term(i)
                cur_set |= next_set
            return cur_set, i

        def parse_term(i):
            # Concatenation of factors until '}' or ',' or end
            cur_set = {""}
            while i < self.n and self.s[i] not in '}.,':
                factor_set, i = parse_factor(i)
                new_set = set()
                for a in cur_set:
                    for b in factor_set:
                        new_set.add(a + b)
                cur_set = new_set
            return cur_set, i

        def parse_factor(i):
            if self.s[i] == '{':
                i += 1  # skip '{'
                inner_set, i = parse_expr(i)
                i += 1  # skip '}'
                return inner_set, i
            else:
                # single character
                return {self.s[i]}, i + 1

        result_set, _ = parse_expr(0)
        return sorted(result_set)
```

## Python3

```python
from typing import List, Set

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        self.s = expression
        self.n = len(expression)
        self.i = 0

        def parse_expr() -> Set[str]:
            # union of terms separated by ','
            res = parse_term()
            while self.i < self.n and self.s[self.i] == ',':
                self.i += 1  # skip ','
                term_set = parse_term()
                res |= term_set
            return res

        def parse_term() -> Set[str]:
            # concatenation of factors
            res: Set[str] = {""}
            while self.i < self.n and self.s[self.i] not in '},':
                factor_set = parse_factor()
                new_res = set()
                for a in res:
                    for b in factor_set:
                        new_res.add(a + b)
                res = new_res
            return res

        def parse_factor() -> Set[str]:
            if self.s[self.i] == '{':
                self.i += 1  # skip '{'
                inner = parse_expr()
                # expect '}'
                self.i += 1  # skip '}'
                return inner
            else:
                # read consecutive letters
                start = self.i
                while self.i < self.n and self.s[self.i].islower():
                    self.i += 1
                literal = self.s[start:self.i]
                return {literal}

        result_set = parse_expr()
        return sorted(result_set)
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char **arr;
    int size;
} Set;

static const char *g_expr;
static int g_len, g_pos;

/* Comparator for qsort */
static int cmp_str(const void *a, const void *b) {
    return strcmp(*(const char **)a, *(const char **)b);
}

/* Create a set containing a single string (copy of s) */
static Set make_set_single(const char *s) {
    Set res;
    res.size = 1;
    res.arr = malloc(sizeof(char *));
    res.arr[0] = strdup(s);
    return res;
}

/* Create a set containing the empty string "" (used as identity for concatenation) */
static Set make_set_empty() {
    Set res;
    res.size = 1;
    res.arr = malloc(sizeof(char *));
    res.arr[0] = strdup("");
    return res;
}

/* Union of two sorted unique sets, result is also sorted and unique.
   The strings themselves are not duplicated; ownership transferred to the result. */
static Set union_sets(Set a, Set b) {
    int i = 0, j = 0, k = 0;
    char **tmp = malloc((a.size + b.size) * sizeof(char *));
    while (i < a.size && j < b.size) {
        int c = strcmp(a.arr[i], b.arr[j]);
        if (c < 0) {
            tmp[k++] = a.arr[i++];
        } else if (c > 0) {
            tmp[k++] = b.arr[j++];
        } else { /* equal */
            tmp[k++] = a.arr[i];
            free(b.arr[j]);   // duplicate, free one copy
            i++; j++;
        }
    }
    while (i < a.size) tmp[k++] = a.arr[i++];
    while (j < b.size) tmp[k++] = b.arr[j++];
    char **finalArr = malloc(k * sizeof(char *));
    memcpy(finalArr, tmp, k * sizeof(char *));
    free(tmp);
    /* Free the old arrays (strings are now owned by finalArr) */
    free(a.arr);
    free(b.arr);
    Set res; res.arr = finalArr; res.size = k;
    return res;
}

/* Concatenation (Cartesian product) of two sets.
   New strings are allocated; after this call, caller should discard the original sets. */
static Set concat_sets(Set a, Set b) {
    int total = a.size * b.size;
    char **tmp = malloc(total * sizeof(char *));
    int idx = 0;
    for (int i = 0; i < a.size; ++i) {
        for (int j = 0; j < b.size; ++j) {
            size_t len1 = strlen(a.arr[i]);
            size_t len2 = strlen(b.arr[j]);
            char *s = malloc(len1 + len2 + 1);
            memcpy(s, a.arr[i], len1);
            memcpy(s + len1, b.arr[j], len2 + 1);
            tmp[idx++] = s;
        }
    }
    /* Free original strings and arrays */
    for (int i = 0; i < a.size; ++i) free(a.arr[i]);
    for (int j = 0; j < b.size; ++j) free(b.arr[j]);
    free(a.arr);
    free(b.arr);
    /* Sort and deduplicate */
    qsort(tmp, total, sizeof(char *), cmp_str);
    int uniq = 0;
    for (int i = 0; i < total; ++i) {
        if (uniq == 0 || strcmp(tmp[i], tmp[uniq - 1]) != 0) {
            tmp[uniq++] = tmp[i];
        } else {
            free(tmp[i]);   // duplicate
        }
    }
    char **finalArr = malloc(uniq * sizeof(char *));
    memcpy(finalArr, tmp, uniq * sizeof(char *));
    free(tmp);
    Set res; res.arr = finalArr; res.size = uniq;
    return res;
}

/* Forward declarations */
static Set parse_expression();
static Set parse_term();
static Set parse_factor();

/* expression ::= term (',' term)* */
static Set parse_expression() {
    Set result = parse_term();
    while (g_pos < g_len && g_expr[g_pos] == ',') {
        ++g_pos;  /* skip ',' */
        Set term = parse_term();
        result = union_sets(result, term);
    }
    return result;
}

/* term ::= factor+   (concatenation) */
static Set parse_term() {
    Set result = make_set_empty();   // identity for concatenation
    while (g_pos < g_len && g_expr[g_pos] != '}' && g_expr[g_pos] != ',') {
        Set f = parse_factor();
        Set combined = concat_sets(result, f);
        result = combined;
    }
    return result;
}

/* factor ::= letter | '{' expression '}' */
static Set parse_factor() {
    if (g_expr[g_pos] == '{') {
        ++g_pos;  /* skip '{' */
        Set inner = parse_expression();
        if (g_pos < g_len && g_expr[g_pos] == '}') ++g_pos;
        return inner;
    } else {   /* single lowercase letter */
        char buf[2];
        buf[0] = g_expr[g_pos++];
        buf[1] = '\0';
        return make_set_single(buf);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** braceExpansionII(char* expression, int* returnSize) {
    g_expr = expression;
    g_len = (int)strlen(expression);
    g_pos = 0;
    Set result = parse_expression();
    *returnSize = result.size;
    return result.arr;   /* caller will free each string and the array */
}
```

## Csharp

```csharp
public class Solution
{
    private string expr;
    private int idx;

    public IList<string> BraceExpansionII(string expression)
    {
        expr = expression;
        idx = 0;
        var resultSet = ParseExpression();
        return new List<string>(resultSet);
    }

    // Parses a union of terms separated by commas
    private SortedSet<string> ParseExpression()
    {
        var union = new SortedSet<string>();
        while (idx < expr.Length && expr[idx] != '}')
        {
            var termSet = ParseTerm();
            foreach (var w in termSet) union.Add(w);

            if (idx < expr.Length && expr[idx] == ',')
                idx++; // skip comma
            else
                break;
        }
        return union;
    }

    // Parses concatenation of factors
    private SortedSet<string> ParseTerm()
    {
        var cur = new SortedSet<string>();
        cur.Add(string.Empty); // start with empty string for product

        while (idx < expr.Length && expr[idx] != '}' && expr[idx] != ',')
        {
            var factorSet = ParseFactor();
            var next = new SortedSet<string>();
            foreach (var a in cur)
                foreach (var b in factorSet)
                    next.Add(a + b);
            cur = next;
        }
        return cur;
    }

    // Parses a single factor: either a letter or a brace-enclosed expression
    private SortedSet<string> ParseFactor()
    {
        if (expr[idx] == '{')
        {
            idx++; // skip '{'
            var inner = ParseExpression();
            idx++; // skip '}'
            return inner;
        }
        else
        {
            var set = new SortedSet<string>();
            set.Add(expr[idx].ToString());
            idx++;
            return set;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} expression
 * @return {string[]}
 */
var braceExpansionII = function(expression) {
    let i = 0;
    const n = expression.length;

    function parseExpr() {
        // Parse first term
        let res = parseTerm();
        // Union with subsequent terms separated by commas
        while (i < n && expression[i] === ',') {
            i++; // skip ','
            const termSet = parseTerm();
            for (const s of termSet) res.add(s);
        }
        return res;
    }

    function parseTerm() {
        // Concatenation of consecutive factors
        let res = new Set(['']);
        while (i < n && expression[i] !== '}' && expression[i] !== ',') {
            const factorSet = parseFactor();
            const next = new Set();
            for (const a of res) {
                for (const b of factorSet) {
                    next.add(a + b);
                }
            }
            res = next;
        }
        return res;
    }

    function parseFactor() {
        if (expression[i] === '{') {
            i++; // skip '{'
            const set = parseExpr();
            i++; // skip '}'
            return set;
        } else {
            const ch = expression[i];
            i++;
            return new Set([ch]);
        }
    }

    const resultSet = parseExpr();
    const ans = Array.from(resultSet);
    ans.sort();
    return ans;
};
```

## Typescript

```typescript
function braceExpansionII(expression: string): string[] {
    let i = 0;
    const n = expression.length;

    function parseExpression(): Set<string> {
        const res = new Set<string>();
        while (true) {
            const termSet = parseTerm();
            for (const s of termSet) res.add(s);
            if (i < n && expression[i] === ',') {
                i++; // skip comma
                continue;
            }
            break;
        }
        return res;
    }

    function parseTerm(): Set<string> {
        let res = new Set<string>(['']);
        while (i < n && expression[i] !== '}' && expression[i] !== ',') {
            const factorSet = parseFactor();
            const next = new Set<string>();
            for (const a of res) {
                for (const b of factorSet) {
                    next.add(a + b);
                }
            }
            res = next;
        }
        return res;
    }

    function parseFactor(): Set<string> {
        if (expression[i] === '{') {
            i++; // skip '{'
            const inner = parseExpression();
            i++; // skip '}'
            return inner;
        } else {
            const ch = expression[i];
            i++;
            return new Set<string>([ch]);
        }
    }

    const finalSet = parseExpression();
    const result = Array.from(finalSet);
    result.sort();
    return result;
}
```

## Php

```php
class Solution {
    private $s;
    private $len;

    /**
     * @param String $expression
     * @return String[]
     */
    function braceExpansionII($expression) {
        $this->s = $expression;
        $this->len = strlen($expression);
        $i = 0;
        $set = $this->parseExpression($i);
        $result = array_keys($set);
        sort($result, SORT_STRING);
        return $result;
    }

    private function parseExpression(&$i) {
        $result = $this->parseTerm($i);
        while ($i < $this->len && $this->s[$i] === ',') {
            $i++; // skip comma
            $next = $this->parseTerm($i);
            foreach ($next as $k => $_) {
                $result[$k] = true;
            }
        }
        return $result;
    }

    private function parseTerm(&$i) {
        $result = ['' => true];
        while ($i < $this->len && $this->s[$i] !== '}' && $this->s[$i] !== ',') {
            $factor = $this->parseFactor($i);
            $new = [];
            foreach ($result as $prefix => $_) {
                foreach ($factor as $suffix => $_2) {
                    $new[$prefix . $suffix] = true;
                }
            }
            $result = $new;
        }
        return $result;
    }

    private function parseFactor(&$i) {
        if ($this->s[$i] === '{') {
            $i++; // skip '{'
            $inner = $this->parseExpression($i);
            $i++; // skip '}'
            return $inner;
        } else {
            $ch = $this->s[$i];
            $i++;
            return [$ch => true];
        }
    }
}
```

## Swift

```swift
class Solution {
    func braceExpansionII(_ expression: String) -> [String] {
        let chars = Array(expression)
        var index = 0
        let n = chars.count
        
        func isLetter(_ ch: Character) -> Bool {
            let v = ch.unicodeScalars.first!.value
            return v >= 97 && v <= 122 // 'a' to 'z'
        }
        
        func combine(_ set1: Set<String>, _ set2: Set<String>) -> Set<String> {
            var result = Set<String>()
            for s1 in set1 {
                for s2 in set2 {
                    result.insert(s1 + s2)
                }
            }
            return result
        }
        
        func parseFactor() -> Set<String> {
            if chars[index] == "{" {
                index += 1 // skip '{'
                let inner = parseExpr()
                // assume current char is '}'
                index += 1 // skip '}'
                return inner
            } else {
                var start = index
                while index < n && isLetter(chars[index]) {
                    index += 1
                }
                let token = String(chars[start..<index])
                return Set([token])
            }
        }
        
        func parseTerm() -> Set<String> {
            var cur: Set<String> = Set([""])
            while index < n && chars[index] != "}" && chars[index] != "," {
                let factorSet = parseFactor()
                cur = combine(cur, factorSet)
            }
            return cur
        }
        
        func parseExpr() -> Set<String> {
            var result = Set<String>()
            while true {
                let termSet = parseTerm()
                result.formUnion(termSet)
                if index >= n || chars[index] == "}" {
                    break
                } else if chars[index] == "," {
                    index += 1 // skip ','
                }
            }
            return result
        }
        
        let finalSet = parseExpr()
        return finalSet.sorted()
    }
}
```

## Kotlin

```kotlin
class Solution {
    private var idx = 0
    private lateinit var expr: String

    fun braceExpansionII(expression: String): List<String> {
        expr = expression
        idx = 0
        val resultSet = parseExpression()
        return resultSet.sorted()
    }

    private fun parseExpression(): Set<String> {
        val res = mutableSetOf<String>()
        while (true) {
            val termSet = parseTerm()
            res.addAll(termSet)
            if (idx >= expr.length || expr[idx] != ',') break
            idx++ // skip comma
        }
        return res
    }

    private fun parseTerm(): Set<String> {
        var cur: Set<String> = setOf("")
        while (idx < expr.length && expr[idx] != '}' && expr[idx] != ',') {
            val factorSet = parseFactor()
            val next = mutableSetOf<String>()
            for (a in cur) {
                for (b in factorSet) {
                    next.add(a + b)
                }
            }
            cur = next
        }
        return cur
    }

    private fun parseFactor(): Set<String> {
        if (expr[idx] == '{') {
            idx++ // skip '{'
            val inner = parseExpression()
            idx++ // skip '}'
            return inner
        } else {
            val ch = expr[idx]
            idx++
            return setOf(ch.toString())
        }
    }
}
```

## Dart

```dart
class Solution {
  late String _s;
  int _pos = 0;

  List<String> braceExpansionII(String expression) {
    _s = expression;
    _pos = 0;
    Set<String> result = _parseExpression();
    var list = result.toList()..sort();
    return list;
  }

  Set<String> _parseExpression() {
    Set<String> res = <String>{};
    while (true) {
      Set<String> termSet = _parseTerm();
      res.addAll(termSet);
      if (_pos >= _s.length || _s[_pos] == '}') break;
      // must be ','
      if (_s[_pos] == ',') {
        _pos++;
      }
    }
    return res;
  }

  Set<String> _parseTerm() {
    Set<String> cur = <String>{''};
    while (_pos < _s.length && (_isLetter(_s[_pos]) || _s[_pos] == '{')) {
      Set<String> factorSet = _parseFactor();
      cur = _concat(cur, factorSet);
    }
    return cur;
  }

  Set<String> _parseFactor() {
    if (_s[_pos] == '{') {
      _pos++; // skip '{'
      Set<String> inner = _parseExpression();
      // skip '}'
      if (_pos < _s.length && _s[_pos] == '}') _pos++;
      return inner;
    } else {
      String ch = _s[_pos];
      _pos++;
      return {ch};
    }
  }

  bool _isLetter(String c) =>
      c.codeUnitAt(0) >= 'a'.codeUnitAt(0) && c.codeUnitAt(0) <= 'z'.codeUnitAt(0);

  Set<String> _concat(Set<String> a, Set<String> b) {
    var res = <String>{};
    for (var x in a) {
      for (var y in b) {
        res.add(x + y);
      }
    }
    return res;
  }
}
```

## Golang

```go
import (
	"sort"
)

type parser struct {
	expr string
	idx  int
}

func (p *parser) peek() byte {
	if p.idx >= len(p.expr) {
		return 0
	}
	return p.expr[p.idx]
}

func (p *parser) next() byte {
	ch := p.peek()
	p.idx++
	return ch
}

// parseExpr parses a union separated by commas and returns the set of strings.
func (p *parser) parseExpr() map[string]bool {
	result := make(map[string]bool)
	for {
		termSet := p.parseTerm()
		for w := range termSet {
			result[w] = true
		}
		if p.peek() != ',' {
			break
		}
		p.next() // skip ','
	}
	return result
}

// parseTerm parses concatenated factors until a comma or closing brace.
func (p *parser) parseTerm() map[string]bool {
	// start with empty string as identity for concatenation
	cur := map[string]bool{"" : true}
	for {
		ch := p.peek()
		if ch == 0 || ch == '}' || ch == ',' {
			break
		}
		factorSet := p.parseFactor()
		newCur := make(map[string]bool)
		for a := range cur {
			for b := range factorSet {
				newCur[a+b] = true
			}
		}
		cur = newCur
	}
	return cur
}

// parseFactor parses either a single letter or a brace-enclosed expression.
func (p *parser) parseFactor() map[string]bool {
	if p.peek() == '{' {
		p.next() // skip '{'
		inner := p.parseExpr()
		p.next() // skip '}'
		return inner
	}
	// must be a lowercase letter
	ch := string(p.next())
	return map[string]bool{ch: true}
}

func braceExpansionII(expression string) []string {
	p := &parser{expr: expression}
	set := p.parseExpr()
	res := make([]string, 0, len(set))
	for w := range set {
		res = append(res, w)
	}
	sort.Strings(res)
	return res
}
```

## Ruby

```ruby
require 'set'

def brace_expansion_ii(expression)
  s = expression
  n = s.length
  i = 0

  product = ->(a, b) {
    res = Set.new
    a.each { |x| b.each { |y| res.add(x + y) } }
    res
  }

  parse = nil
  parse_brace = nil

  parse = lambda do
    result = Set.new([''])
    while i < n && s[i] != '}' && s[i] != ','
      if s[i] == '{'
        i += 1
        sub = parse_brace.call
        i += 1 # skip '}'
      else
        ch = s[i]
        i += 1
        sub = Set.new([ch])
      end
      result = product.call(result, sub)
    end
    result
  end

  parse_brace = lambda do
    sets = []
    loop do
      sets << parse.call
      break if i >= n || s[i] == '}'
      i += 1 # skip ','
    end
    union = Set.new
    sets.each { |st| union.merge(st) }
    union
  end

  result_set = parse.call
  result_set.to_a.sort
end
```

## Scala

```scala
object Solution {
  def braceExpansionII(expression: String): List[String] = {
    val n = expression.length
    var idx = 0

    def parseExpr(): Set[String] = {
      var res = parseTerm()
      while (idx < n && expression(idx) == ',') {
        idx += 1
        val termSet = parseTerm()
        res = res ++ termSet
      }
      res
    }

    def parseTerm(): Set[String] = {
      var res: Set[String] = Set("")
      while (idx < n && expression(idx) != '}' && expression(idx) != ',') {
        val factorSet = parseFactor()
        val combined = for {
          a <- res
          b <- factorSet
        } yield a + b
        res = combined
      }
      res
    }

    def parseFactor(): Set[String] = {
      if (expression(idx) == '{') {
        idx += 1 // skip '{'
        val inner = parseExpr()
        idx += 1 // skip '}'
        inner
      } else {
        val sb = new StringBuilder
        while (idx < n && expression(idx).isLetter) {
          sb.append(expression(idx))
          idx += 1
        }
        Set(sb.toString)
      }
    }

    parseExpr().toList.sorted
  }
}
```

## Rust

```rust
impl Solution {
    pub fn brace_expansion_ii(expression: String) -> Vec<String> {
        use std::collections::BTreeSet;

        fn combine(a: &BTreeSet<String>, b: &BTreeSet<String>) -> BTreeSet<String> {
            let mut res = BTreeSet::new();
            for s1 in a.iter() {
                for s2 in b.iter() {
                    let mut new_s = String::with_capacity(s1.len() + s2.len());
                    new_s.push_str(s1);
                    new_s.push_str(s2);
                    res.insert(new_s);
                }
            }
            res
        }

        fn parse_union(chars: &Vec<char>, idx: &mut usize) -> BTreeSet<String> {
            let mut union_set = BTreeSet::new();
            loop {
                let part = parse_expr(chars, idx);
                for s in part {
                    union_set.insert(s);
                }
                if *idx < chars.len() && chars[*idx] == ',' {
                    *idx += 1; // skip comma
                } else {
                    break;
                }
            }
            union_set
        }

        fn parse_expr(chars: &Vec<char>, idx: &mut usize) -> BTreeSet<String> {
            let mut res = BTreeSet::new();
            res.insert(String::new());

            while *idx < chars.len() {
                match chars[*idx] {
                    '}' | ',' => break,
                    '{' => {
                        *idx += 1; // skip '{'
                        let sub = parse_union(chars, idx);
                        if *idx < chars.len() && chars[*idx] == '}' {
                            *idx += 1; // skip '}'
                        }
                        res = combine(&res, &sub);
                    }
                    c if c.is_ascii_lowercase() => {
                        let mut s = String::new();
                        while *idx < chars.len() && chars[*idx].is_ascii_lowercase() {
                            s.push(chars[*idx]);
                            *idx += 1;
                        }
                        let mut set = BTreeSet::new();
                        set.insert(s);
                        res = combine(&res, &set);
                    }
                    _ => {
                        *idx += 1; // ignore unexpected characters
                    }
                }
            }

            res
        }

        let chars: Vec<char> = expression.chars().collect();
        let mut idx = 0usize;
        let result_set = parse_expr(&chars, &mut idx);
        result_set.into_iter().collect()
    }
}
```

## Racket

```racket
(require racket/set)

(define/contract (brace-expansion-ii expression)
  (-> string? (listof string?))
  (let* ([len (string-length expression)]
         [pos (box 0)])
    (define (end?) (= (unbox pos) len))
    (define (peek) (if (end?) #\null (string-ref expression (unbox pos))))
    (define (consume)
      (begin0 (peek) (set-box! pos (+ (unbox pos) 1))))
    
    ;; Cartesian product of two sets, concatenating strings
    (define (concat-sets s1 s2)
      (for/set ([a s1] [b s2]) (string-append a b)))
    
    ;; Parse a single item: either a brace group or a literal string
    (define (parse-item)
      (cond [(char=? (peek) #\{)
             (consume)                     ; consume '{'
             (define inner (parse-union))
             (when (not (char=? (peek) #\}))
               (error "expected }"))
             (consume)                     ; consume '}'
             inner]
            [else
             (let ([start (unbox pos)])
               (let loop ()
                 (if (and (not (end?))
                          (let ([c (string-ref expression (unbox pos))])
                            (char-alphabetic? c)))
                     (begin (set-box! pos (+ (unbox pos) 1)) (loop))
                     (let ([sub (substring expression start (unbox pos))])
                       (if (string=? sub "")
                           (set)
                           (set sub))))))]))
    
    ;; Parse a union separated by commas
    (define (parse-union)
      (let loop ([acc (parse-expr)])
        (if (char=? (peek) #\,)
            (begin (consume) (loop (set-union acc (parse-expr))))
            acc)))
    
    ;; Parse concatenated sequence of items
    (define (parse-expr)
      (let loop ([acc (parse-item)])
        (cond [(or (end?) (member (peek) (list #\, #\}))) acc]
              [else (loop (concat-sets acc (parse-item)))])))
    
    ;; Start parsing the whole expression
    (define result (parse-expr))
    (when (not (end?))
      (error "unexpected trailing characters"))
    (let ([lst (set->list result)])
      (sort lst string<?))))
```

## Erlang

```erlang
-spec brace_expansion_ii(Expression :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
brace_expansion_ii(Expression) ->
    Chars = binary_to_list(Expression),
    {Set, _} = parse_expression(Chars),
    Binaries = [list_to_binary(Str) || Str <- Set],
    lists:usort(Binaries).

%% Parse a concatenated sequence of terms until ',' or '}' or end.
parse_expression(Chars) ->
    {Set1, Rest1} = parse_term(Chars),
    parse_expression_rest(Set1, Rest1).

parse_expression_rest(AccSet, Rest) ->
    case Rest of
        [] -> {AccSet, []};
        [$,|_] -> {AccSet, Rest};
        [$}|_] -> {AccSet, Rest};
        _ ->
            {Set2, Rest2} = parse_term(Rest),
            Combined = combine_sets(AccSet, Set2),
            parse_expression_rest(Combined, Rest2)
    end.

%% Parse a single term: either a letter or a brace-enclosed union.
parse_term([${|Rest]) ->
    {Set, AfterUnion} = parse_union(Rest),
    case AfterUnion of
        [$}|RestAfterBrace] -> {Set, RestAfterBrace};
        _ -> {Set, AfterUnion}
    end;
parse_term([Char|Rest]) when Char >= $a, Char =< $z ->
    {[ [Char] ], Rest};
parse_term([]) ->
    {[], []}.

%% Parse a union inside braces: expressions separated by commas.
parse_union(Chars) ->
    {Set1, Rest1} = parse_expression(Chars),
    parse_union_rest(Set1, Rest1).

parse_union_rest(AccSet, Rest) ->
    case Rest of
        [$,|RestAfterComma] ->
            {SetNext, RestAfterExpr} = parse_expression(RestAfterComma),
            NewAcc = union_sets(AccSet, SetNext),
            parse_union_rest(NewAcc, RestAfterExpr);
        _ -> % stop at '}'
            {AccSet, Rest}
    end.

%% Cartesian product concatenation of two sets.
combine_sets(SetA, SetB) ->
    [ A ++ B || A <- SetA, B <- SetB ].

%% Simple union (concatenation) of two lists; duplicates removed later.
union_sets(SetA, SetB) ->
    SetA ++ SetB.
```

## Elixir

```elixir
defmodule Solution do
  @spec brace_expansion_ii(expression :: String.t()) :: [String.t()]
  def brace_expansion_ii(expression) do
    {set, _} = parse_expression(expression, 0)
    set |> MapSet.to_list() |> Enum.sort()
  end

  # Parse a concatenation of factors until ',' or '}' or end of string.
  defp parse_expression(str, pos) do
    parse_concat(str, pos, MapSet.new([""]))
  end

  defp parse_concat(str, pos, acc_set) do
    len = byte_size(str)

    cond do
      pos >= len ->
        {acc_set, pos}

      true ->
        case String.at(str, pos) do
          "}" -> {acc_set, pos}
          "," -> {acc_set, pos}
          _ ->
            {factor_set, next_pos} = parse_factor(str, pos)
            combined = combine(acc_set, factor_set)
            parse_concat(str, next_pos, combined)
        end
    end
  end

  # Parse a single factor: either a letter or a brace-enclosed union.
  defp parse_factor(str, pos) do
    case String.at(str, pos) do
      "{" ->
        {set, new_pos} = parse_union(str, pos + 1)
        {set, new_pos}

      c when is_binary(c) and c =~ ~r/^[a-z]$/ ->
        {MapSet.new([c]), pos + 1}
    end
  end

  # Parse a union inside braces: expressions separated by commas.
  defp parse_union(str, pos) do
    {first_set, next_pos} = parse_expression(str, pos)
    union_rest(str, next_pos, first_set)
  end

  defp union_rest(str, pos, acc_set) do
    len = byte_size(str)

    cond do
      pos < len and String.at(str, pos) == "," ->
        {next_set, after_next} = parse_expression(str, pos + 1)
        new_acc = MapSet.union(acc_set, next_set)
        union_rest(str, after_next, new_acc)

      true ->
        # Expect closing '}'
        {acc_set, pos + 1}
    end
  end

  defp combine(set1, set2) do
    for a <- MapSet.to_list(set1),
        b <- MapSet.to_list(set2),
        into: MapSet.new(),
        do: a <> b
  end
end
```
