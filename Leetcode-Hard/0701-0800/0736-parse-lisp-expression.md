# 0736. Parse Lisp Expression

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    unordered_map<string, vector<int>> scope;
    
    void skipSpaces(const string& s, int& i) {
        while (i < (int)s.size() && s[i] == ' ') ++i;
    }
    
    string readWord(const string& s, int& i) {
        int start = i;
        while (i < (int)s.size() && s[i] != ' ' && s[i] != ')') ++i;
        return s.substr(start, i - start);
    }
    
    int getVar(const string& var) {
        return scope[var].back();
    }
    
    int eval(const string& s, int& i) {
        if (s[i] != '(') { // number or variable
            if (s[i] == '-' || isdigit(s[i])) {
                int sign = 1;
                if (s[i] == '-') { sign = -1; ++i; }
                int num = 0;
                while (i < (int)s.size() && isdigit(s[i])) {
                    num = num * 10 + (s[i] - '0');
                    ++i;
                }
                return sign * num;
            } else { // variable
                string var = readWord(s, i);
                return getVar(var);
            }
        }
        
        ++i; // skip '('
        string op = readWord(s, i);
        int result = 0;
        if (op == "add") {
            int a = eval(s, i);
            skipSpaces(s, i);
            int b = eval(s, i);
            result = a + b;
        } else if (op == "mult") {
            int a = eval(s, i);
            skipSpaces(s, i);
            int b = eval(s, i);
            result = a * b;
        } else { // let
            vector<string> assigned;
            while (true) {
                skipSpaces(s, i);
                if (s[i] == ')') { ++i; break; }
                
                // Determine if this is the final expression
                if (s[i] != '(' && isalpha(s[i])) {
                    int save = i;
                    string token = readWord(s, i); // could be var name or final expr
                    skipSpaces(s, i);
                    if (s[i] == ')' || s[i] == '\0') { // final expression (variable)
                        int val = getVar(token);
                        for (auto& v : assigned) scope[v].pop_back();
                        ++i; // consume ')'
                        return val;
                    } else {
                        // token is a variable name, next part is its value
                        string varName = token;
                        int valExpr = eval(s, i);
                        scope[varName].push_back(valExpr);
                        assigned.push_back(varName);
                        continue;
                    }
                } else { // final expression starts with '(' or number (including '-')
                    int val = eval(s, i);
                    for (auto& v : assigned) scope[v].pop_back();
                    skipSpaces(s, i);
                    if (s[i] == ')') ++i;
                    return val;
                }
            }
        }
        skipSpaces(s, i);
        if (s[i] == ')') ++i;
        return result;
    }
    
public:
    int evaluate(string expression) {
        int idx = 0;
        return eval(expression, idx);
    }
};
```

## Java

```java
class Solution {
    private String s;
    private int pos;
    private java.util.Map<String, java.util.Deque<Integer>> env = new java.util.HashMap<>();

    public int evaluate(String expression) {
        this.s = expression;
        this.pos = 0;
        return eval();
    }

    private int eval() {
        skipSpaces();
        if (s.charAt(pos) == '(') { // compound expression
            pos++; // skip '('
            String op = parseWord(); // operator: let, add, mult
            int result = 0;
            if ("let".equals(op)) {
                java.util.List<String> assignedVars = new java.util.ArrayList<>();
                while (true) {
                    skipSpaces();
                    if (s.charAt(pos) == ')') { // no more tokens
                        break;
                    }
                    int savedPos = pos;
                    String token = parseWord(); // could be var name or final expr start
                    skipSpaces();
                    if (s.charAt(pos) == ')' || s.charAt(pos) == '(') {
                        // this token is the final expression
                        pos = savedPos; // reset to start of token
                        result = eval();
                        break;
                    } else {
                        // assignment: token is variable name
                        String varName = token;
                        int value = eval(); // evaluate assigned expression
                        env.computeIfAbsent(varName, k -> new java.util.ArrayDeque<>()).push(value);
                        assignedVars.add(varName);
                    }
                }
                // pop assignments of this let scope
                for (String v : assignedVars) {
                    java.util.Deque<Integer> stack = env.get(v);
                    stack.pop();
                    if (stack.isEmpty()) {
                        env.remove(v);
                    }
                }
                skipSpaces(); // should be at ')'
                pos++; // consume ')'
            } else if ("add".equals(op)) {
                int e1 = eval();
                int e2 = eval();
                skipSpaces();
                pos++; // consume ')'
                result = e1 + e2;
            } else { // mult
                int e1 = eval();
                int e2 = eval();
                skipSpaces();
                pos++; // consume ')'
                result = e1 * e2;
            }
            return result;
        } else {
            // token is number or variable
            if (s.charAt(pos) == '-' || Character.isDigit(s.charAt(pos))) {
                int start = pos;
                while (pos < s.length() && (Character.isDigit(s.charAt(pos)) || s.charAt(pos) == '-')) {
                    pos++;
                }
                return Integer.parseInt(s.substring(start, pos));
            } else {
                String var = parseWord();
                java.util.Deque<Integer> stack = env.get(var);
                return stack.peek();
            }
        }
    }

    private void skipSpaces() {
        while (pos < s.length() && s.charAt(pos) == ' ') {
            pos++;
        }
    }

    private String parseWord() {
        int start = pos;
        while (pos < s.length() && s.charAt(pos) != ' ' && s.charAt(pos) != ')' && s.charAt(pos) != '(') {
            pos++;
        }
        return s.substring(start, pos);
    }
}
```

## Python

```python
class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        # Tokenize the input string into meaningful tokens.
        def tokenize(s):
            tokens = []
            i = 0
            n = len(s)
            while i < n:
                c = s[i]
                if c == '(' or c == ')':
                    tokens.append(c)
                    i += 1
                elif c == ' ':
                    i += 1
                else:
                    j = i
                    while j < n and s[j] not in (' ', '(', ')'):
                        j += 1
                    tokens.append(s[i:j])
                    i = j
            return tokens

        tokens = tokenize(expression)
        env = {}          # variable -> list of values (stack)
        idx = 0           # current token index

        def get_val(tok):
            if tok[0] == '-' or tok.isdigit():
                return int(tok)
            return env[tok][-1]

        def eval_expr():
            nonlocal idx
            tok = tokens[idx]
            if tok == '(':
                idx += 1                     # skip '('
                op = tokens[idx]
                idx += 1                     # move past operator

                if op == "let":
                    assigned = []
                    while True:
                        if tokens[idx] == ')':
                            # no expression left (should not happen)
                            idx += 1
                            break
                        # If next token starts a sub‑expression, it's the final expr.
                        if tokens[idx] == '(':
                            val = eval_expr()
                            # after evaluating, current token should be ')'
                            idx += 1  # skip closing ')'
                            break
                        # Look ahead to see if this token is the final expression.
                        if idx + 1 < len(tokens) and tokens[idx + 1] == ')':
                            val = get_val(tokens[idx])
                            idx += 2   # skip token and ')'
                            break
                        # Otherwise it's a variable name followed by an expression.
                        var = tokens[idx]
                        idx += 1
                        expr_val = eval_expr()
                        if var not in env:
                            env[var] = []
                        env[var].append(expr_val)
                        assigned.append(var)
                        # after evaluating, next token could be space (already removed) or ')'
                    # pop variables defined in this let scope
                    for v in reversed(assigned):
                        env[v].pop()
                        if not env[v]:
                            del env[v]
                    return val

                elif op == "add":
                    left = eval_expr()
                    right = eval_expr()
                    idx += 1   # skip ')'
                    return left + right

                else:  # mult
                    left = eval_expr()
                    right = eval_expr()
                    idx += 1   # skip ')'
                    return left * right
            else:
                idx += 1
                if tok[0] == '-' or tok.isdigit():
                    return int(tok)
                return env[tok][-1]

        return eval_expr()
```

## Python3

```python
class Solution:
    def evaluate(self, expression: str) -> int:
        s = expression
        n = len(s)
        env = {}

        def get_var(name):
            return env[name][-1]

        def parse(i: int):
            if s[i] != '(':
                j = i
                while j < n and s[j] not in (' ', ')'):
                    j += 1
                token = s[i:j]
                if token[0].isdigit() or token[0] == '-':
                    return int(token), j
                else:
                    return get_var(token), j

            # '(' case
            i += 1  # skip '('
            op_start = i
            while s[i] != ' ':
                i += 1
            op = s[op_start:i]

            if op == "let":
                assigned = []
                while True:
                    while i < n and s[i] == ' ':
                        i += 1
                    if s[i] == ')':
                        break

                    # final expression could start with '('
                    if s[i] == '(':
                        val, i = parse(i)
                        break

                    # read next token (could be var or number)
                    start = i
                    while i < n and s[i] not in (' ', ')'):
                        i += 1
                    token = s[start:i]

                    # look ahead to see if this is the final expression
                    j = i
                    while j < n and s[j] == ' ':
                        j += 1
                    if s[j] == ')':
                        # final expr
                        if token[0].isdigit() or token[0] == '-':
                            val = int(token)
                        else:
                            val = get_var(token)
                        i = j  # position at ')'
                        break
                    else:
                        # assignment var = expr
                        var = token
                        while i < n and s[i] == ' ':
                            i += 1
                        expr_val, i = parse(i)
                        env.setdefault(var, []).append(expr_val)
                        assigned.append(var)

                for v in reversed(assigned):
                    env[v].pop()
                    if not env[v]:
                        del env[v]
                i += 1  # skip ')'
                return val, i

            else:  # add or mult
                while s[i] == ' ':
                    i += 1
                left, i = parse(i)
                while s[i] == ' ':
                    i += 1
                right, i = parse(i)
                i += 1  # skip ')'
                return (left + right) if op == "add" else (left * right), i

        result, _ = parse(0)
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>

#define HASH_SIZE 4099

typedef struct Entry {
    char *key;
    int *stack;
    int sz;
    int cap;
    struct Entry *next;
} Entry;

static Entry *table[HASH_SIZE];

static unsigned long hash_str(const char *s) {
    unsigned long h = 5381;
    while (*s)
        h = ((h << 5) + h) + (unsigned char)*s++;
    return h % HASH_SIZE;
}

static Entry *getEntry(const char *key, int create) {
    unsigned long idx = hash_str(key);
    Entry *e = table[idx];
    while (e) {
        if (strcmp(e->key, key) == 0)
            return e;
        e = e->next;
    }
    if (!create)
        return NULL;
    e = (Entry *)malloc(sizeof(Entry));
    e->key = strdup(key);
    e->stack = NULL;
    e->sz = e->cap = 0;
    e->next = table[idx];
    table[idx] = e;
    return e;
}

static void pushVar(const char *var, int val) {
    Entry *e = getEntry(var, 1);
    if (e->sz == e->cap) {
        int newCap = e->cap ? e->cap * 2 : 4;
        e->stack = (int *)realloc(e->stack, newCap * sizeof(int));
        e->cap = newCap;
    }
    e->stack[e->sz++] = val;
}

static void popVar(Entry *e) {
    if (e && e->sz > 0)
        e->sz--;
}

/* forward declaration */
static int eval(const char *s, int *pos);

static void skipSpaces(const char *s, int *pos) {
    while (s[*pos] == ' ')
        (*pos)++;
}

static int readToken(const char *s, int *pos, char *buf, int bufsize) {
    int i = 0;
    while (s[*pos] && s[*pos] != ' ' && s[*pos] != ')') {
        if (i < bufsize - 1)
            buf[i++] = s[*pos];
        (*pos)++;
    }
    buf[i] = '\0';
    return i;
}

static int eval(const char *s, int *pos) {
    skipSpaces(s, pos);
    if (s[*pos] == '(') {                     // compound expression
        (*pos)++;                             // skip '('
        skipSpaces(s, pos);
        char op[8];
        readToken(s, pos, op, sizeof(op));
        if (strcmp(op, "add") == 0) {
            int v1 = eval(s, pos);
            int v2 = eval(s, pos);
            skipSpaces(s, pos);
            if (s[*pos] == ')')
                (*pos)++;
            return v1 + v2;
        } else if (strcmp(op, "mult") == 0) {
            int v1 = eval(s, pos);
            int v2 = eval(s, pos);
            skipSpaces(s, pos);
            if (s[*pos] == ')')
                (*pos)++;
            return v1 * v2;
        } else { // let
            Entry *assigned[200];
            int assignCnt = 0;
            while (1) {
                skipSpaces(s, pos);
                if (s[*pos] == ')') {          // no final expr (should not happen)
                    (*pos)++;
                    break;
                }
                /* decide whether next token is a variable name or the final expression */
                if (s[*pos] == '(' || s[*pos] == '-' ||
                    (s[*pos] >= '0' && s[*pos] <= '9')) {
                    int result = eval(s, pos);
                    skipSpaces(s, pos);
                    if (s[*pos] == ')')
                        (*pos)++;
                    for (int k = assignCnt - 1; k >= 0; --k)
                        popVar(assigned[k]);
                    return result;
                } else {
                    char var[64];
                    readToken(s, pos, var, sizeof(var));
                    int val = eval(s, pos);
                    Entry *e = getEntry(var, 1);
                    if (e->sz == e->cap) {
                        int newCap = e->cap ? e->cap * 2 : 4;
                        e->stack = (int *)realloc(e->stack, newCap * sizeof(int));
                        e->cap = newCap;
                    }
                    e->stack[e->sz++] = val;
                    assigned[assignCnt++] = e;
                }
            }
        }
    } else if (s[*pos] == '-' || (s[*pos] >= '0' && s[*pos] <= '9')) { // integer
        int sign = 1;
        if (s[*pos] == '-') {
            sign = -1;
            (*pos)++;
        }
        int num = 0;
        while (s[*pos] >= '0' && s[*pos] <= '9') {
            num = num * 10 + (s[*pos] - '0');
            (*pos)++;
        }
        return sign * num;
    } else { // variable
        char var[64];
        readToken(s, pos, var, sizeof(var));
        Entry *e = getEntry(var, 0);
        return e->stack[e->sz - 1];
    }
    return 0; // never reached
}

int evaluate(char* expression) {
    int pos = 0;
    return eval(expression, &pos);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private string expr;
    private int n;
    private Dictionary<string, Stack<int>> scope = new Dictionary<string, Stack<int>>();

    public int Evaluate(string expression) {
        expr = expression;
        n = expr.Length;
        int idx = 0;
        return Eval(ref idx);
    }

    private void SkipSpaces(ref int i) {
        while (i < n && expr[i] == ' ') i++;
    }

    private string ReadWord(ref int i) {
        SkipSpaces(ref i);
        int start = i;
        while (i < n && expr[i] != ' ' && expr[i] != ')' && expr[i] != '(') i++;
        return expr.Substring(start, i - start);
    }

    private int ReadNumber(ref int i) {
        SkipSpaces(ref i);
        int sign = 1;
        if (expr[i] == '-') { sign = -1; i++; }
        int val = 0;
        while (i < n && char.IsDigit(expr[i])) {
            val = val * 10 + (expr[i] - '0');
            i++;
        }
        return sign * val;
    }

    private int GetVar(string name) {
        if (scope.TryGetValue(name, out var st) && st.Count > 0)
            return st.Peek();
        return 0; // should not happen for valid input
    }

    private int Eval(ref int i) {
        SkipSpaces(ref i);
        if (expr[i] == '(') {
            i++; // skip '('
            string op = ReadWord(ref i);
            int result = 0;
            if (op == "add") {
                int a = Eval(ref i);
                int b = Eval(ref i);
                result = a + b;
            } else if (op == "mult") {
                int a = Eval(ref i);
                int b = Eval(ref i);
                result = a * b;
            } else { // let
                List<string> assigned = new List<string>();
                while (true) {
                    SkipSpaces(ref i);
                    if (i < n && expr[i] == ')') break; // safety

                    if (expr[i] == '(') {
                        result = Eval(ref i); // final expression is a subexpression
                        break;
                    }

                    string token = ReadWord(ref i);
                    SkipSpaces(ref i);

                    if (i < n && expr[i] == ')') {
                        // final expression is this token (number or variable)
                        if (char.IsDigit(token[0]) || token[0] == '-')
                            result = int.Parse(token);
                        else
                            result = GetVar(token);
                        break;
                    }

                    // token is a variable name for assignment
                    string varName = token;
                    int val = Eval(ref i);
                    if (!scope.ContainsKey(varName)) scope[varName] = new Stack<int>();
                    scope[varName].Push(val);
                    assigned.Add(varName);
                }
                // pop assignments to restore outer scopes
                for (int k = assigned.Count - 1; k >= 0; k--) {
                    string v = assigned[k];
                    scope[v].Pop();
                    if (scope[v].Count == 0) scope.Remove(v);
                }
            }
            SkipSpaces(ref i);
            if (i < n && expr[i] == ')') i++; // consume ')'
            return result;
        } else if (expr[i] == '-' || char.IsDigit(expr[i])) {
            return ReadNumber(ref i);
        } else {
            string var = ReadWord(ref i);
            return GetVar(var);
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} expression
 * @return {number}
 */
var evaluate = function(expression) {
    const s = expression;
    const n = s.length;
    const scope = new Map(); // var -> stack of values

    const getValue = (token) => {
        const c = token[0];
        if (c === '-' || (c >= '0' && c <= '9')) {
            return parseInt(token, 10);
        }
        const stack = scope.get(token);
        return stack[stack.length - 1];
    };

    const skipSpaces = (i) => {
        while (i < n && s[i] === ' ') i++;
        return i;
    };

    const readToken = (i) => {
        // reads until space or ')'
        let j = i;
        while (j < n && s[j] !== ' ' && s[j] !== ')') j++;
        return [s.slice(i, j), j];
    };

    const parse = (i) => {
        i = skipSpaces(i);
        if (s[i] !== '(') {
            // integer or variable
            const [tok, nxt] = readToken(i);
            return [getValue(tok), nxt];
        }

        // '(' expression
        i++; // skip '('
        i = skipSpaces(i);
        // read operator
        let opStart = i;
        while (i < n && s[i] !== ' ') i++;
        const op = s.slice(opStart, i);

        if (op === 'add' || op === 'mult') {
            // parse two sub-expressions
            const [v1, idx1] = parse(i);
            const [v2, idx2] = parse(idx1);
            let j = skipSpaces(idx2);
            // consume ')'
            if (s[j] === ')') j++;
            return [op === 'add' ? v1 + v2 : v1 * v2, j];
        }

        // let expression
        const assigned = []; // variables introduced in this let
        while (true) {
            i = skipSpaces(i);
            if (s[i] === ')') { // no more tokens, should not happen normally
                i++; // consume ')'
                break;
            }

            // If next token starts with '(' it's the final expression
            if (s[i] === '(') {
                const [val, nxt] = parse(i);
                i = nxt;
                i = skipSpaces(i);
                if (s[i] === ')') i++;
                // pop assignments
                for (const v of assigned) {
                    const st = scope.get(v);
                    st.pop();
                    if (st.length === 0) scope.delete(v);
                }
                return [val, i];
            }

            // read next token as string (could be variable name or final expr)
            const [tok, nxtPos] = readToken(i);
            i = nxtPos;
            i = skipSpaces(i);

            // If after this token we see ')' it's the final expression
            if (s[i] === ')') {
                const val = getValue(tok);
                i++; // consume ')'
                for (const v of assigned) {
                    const st = scope.get(v);
                    st.pop();
                    if (st.length === 0) scope.delete(v);
                }
                return [val, i];
            }

            // Otherwise tok is a variable name; parse its value expression
            const varName = tok;
            const [valExpr, nxt] = parse(i);
            i = nxt;

            if (!scope.has(varName)) scope.set(varName, []);
            scope.get(varName).push(valExpr);
            assigned.push(varName);
        }

        // Should never reach here; return dummy
        return [0, i];
    };

    const [result] = parse(0);
    return result;
};
```

## Typescript

```typescript
function evaluate(expression: string): number {
    const vars = new Map<string, number[]>();
    
    function skipSpaces(i: number): number {
        while (i < expression.length && expression[i] === ' ') i++;
        return i;
    }
    
    function parseToken(i: number): [string, number] {
        let start = i;
        while (i < expression.length && expression[i] !== ' ' && expression[i] !== ')') i++;
        return [expression.slice(start, i), i];
    }
    
    function isNumberChar(ch: string): boolean {
        return (ch >= '0' && ch <= '9') || ch === '-';
    }
    
    function getValue(token: string): number {
        if (isNumberChar(token[0])) return parseInt(token, 10);
        const stack = vars.get(token)!;
        return stack[stack.length - 1];
    }
    
    function evalExpr(i: number): [number, number] {
        i = skipSpaces(i);
        if (expression[i] === '(') { // compound expression
            i++; // skip '('
            const [op, afterOp] = parseToken(i);
            i = afterOp;
            if (op === 'let') {
                const assigned: string[] = [];
                while (true) {
                    i = skipSpaces(i);
                    if (expression[i] === ')') { // should not happen; handled later
                        i++; // consume ')'
                        break;
                    }
                    // Determine if next token is the final expression
                    if (expression[i] === '(') {
                        const [val, nxt] = evalExpr(i);
                        i = nxt;
                        // pop assignments of this let scope
                        for (const v of assigned) {
                            const st = vars.get(v)!;
                            st.pop();
                            if (st.length === 0) vars.delete(v);
                        }
                        i = skipSpaces(i);
                        if (expression[i] === ')') i++;
                        return [val, i];
                    } else {
                        const [tok, afterTok] = parseToken(i);
                        const lookahead = skipSpaces(afterTok);
                        if (expression[lookahead] === ')' ) { // final expression is tok
                            const val = getValue(tok);
                            for (const v of assigned) {
                                const st = vars.get(v)!;
                                st.pop();
                                if (st.length === 0) vars.delete(v);
                            }
                            i = lookahead + 1; // skip ')'
                            return [val, i];
                        } else { // assignment: var = expr
                            const varName = tok;
                            const [value, nxtPos] = evalExpr(afterTok);
                            if (!vars.has(varName)) vars.set(varName, []);
                            vars.get(varName)!.push(value);
                            assigned.push(varName);
                            i = nxtPos;
                        }
                    }
                }
            } else if (op === 'add' || op === 'mult') {
                const [v1, afterV1] = evalExpr(i);
                const [v2, afterV2] = evalExpr(afterV1);
                i = afterV2;
                i = skipSpaces(i);
                if (expression[i] === ')') i++;
                return [op === 'add' ? v1 + v2 : v1 * v2, i];
            }
        } else { // number or variable
            if (isNumberChar(expression[i])) {
                const start = i;
                while (i < expression.length && expression[i] !== ' ' && expression[i] !== ')') i++;
                return [parseInt(expression.slice(start, i), 10), i];
            } else {
                const start = i;
                while (i < expression.length && expression[i] !== ' ' && expression[i] !== ')') i++;
                const varName = expression.slice(start, i);
                return [getValue(varName), i];
            }
        }
        // unreachable
        return [0, i];
    }
    
    const [result, _] = evalExpr(0);
    return result;
}
```

## Php

```php
class Solution {
    private string $s;
    private int $n = 0;
    private int $i = 0;

    /**
     * @param String $expression
     * @return Integer
     */
    function evaluate($expression) {
        $this->s = $expression;
        $this->n = strlen($expression);
        $this->i = 0;
        $env = []; // variable => stack of values
        return $this->parseExpr($env);
    }

    private function skipSpaces(): void {
        while ($this->i < $this->n && $this->s[$this->i] === ' ') {
            $this->i++;
        }
    }

    private function parseTokenString(): string {
        $start = $this->i;
        while ($this->i < $this->n && $this->s[$this->i] !== ' ' && $this->s[$this->i] !== ')') {
            $this->i++;
        }
        return substr($this->s, $start, $this->i - $start);
    }

    private function getVarValue(string $var, array &$env): int {
        if (!isset($env[$var]) || empty($env[$var])) {
            return 0; // should not happen per problem guarantees
        }
        return end($env[$var]);
    }

    private function parseExpr(array &$env): int {
        $this->skipSpaces();
        if ($this->s[$this->i] === '(') {
            $this->i++; // skip '('
            $op = $this->parseTokenString(); // operator: add, mult, let
            if ($op === 'add') {
                $v1 = $this->parseExpr($env);
                $v2 = $this->parseExpr($env);
                $this->skipSpaces();
                $this->i++; // skip ')'
                return $v1 + $v2;
            } elseif ($op === 'mult') {
                $v1 = $this->parseExpr($env);
                $v2 = $this->parseExpr($env);
                $this->skipSpaces();
                $this->i++; // skip ')'
                return $v1 * $v2;
            } else { // let
                return $this->parseLet($env);
            }
        } else {
            $token = $this->parseTokenString();
            if ($token[0] === '-' || ctype_digit($token[0])) {
                return intval($token);
            } else {
                return $this->getVarValue($token, $env);
            }
        }
    }

    private function parseLet(array &$env): int {
        $assigned = []; // list of variables assigned in this let
        while (true) {
            $this->skipSpaces();
            if ($this->s[$this->i] === ')') { // no more tokens, should not occur normally
                break;
            }

            // Peek next token start character
            $ch = $this->s[$this->i];
            if ($ch >= 'a' && $ch <= 'z') {
                // Could be variable name or final expression (variable)
                $varNamePos = $this->i;
                $var = $this->parseTokenString(); // read word
                $this->skipSpaces();
                if ($this->s[$this->i] === ')') {
                    // Final expression is this variable
                    $value = $this->getVarValue($var, $env);
                    $this->i++; // skip ')'
                    foreach (array_reverse($assigned) as $v) {
                        array_pop($env[$v]);
                    }
                    return $value;
                } else {
                    // It's a variable assignment
                    $val = $this->parseExpr($env);
                    if (!isset($env[$var])) {
                        $env[$var] = [];
                    }
                    $env[$var][] = $val;
                    $assigned[] = $var;
                    continue;
                }
            } else {
                // Final expression (could be '(' or number)
                $value = $this->parseExpr($env);
                $this->skipSpaces();
                $this->i++; // skip ')'
                foreach (array_reverse($assigned) as $v) {
                    array_pop($env[$v]);
                }
                return $value;
            }
        }
        // Should not reach here; fallback
        foreach (array_reverse($assigned) as $v) {
            array_pop($env[$v]);
        }
        return 0;
    }
}
```

## Swift

```swift
class Solution {
    private var scopes: [String: [Int]] = [:]

    func evaluate(_ expression: String) -> Int {
        let chars = Array(expression)
        var idx = 0
        return eval(chars, &idx)
    }

    private func parseToken(_ s: [Character], _ i: inout Int) -> String {
        let start = i
        while i < s.count && s[i] != " " && s[i] != ")" {
            i += 1
        }
        return String(s[start..<i])
    }

    private func eval(_ s: [Character], _ i: inout Int) -> Int {
        if s[i] != "(" {
            let token = parseToken(s, &i)
            if let num = Int(token) {
                return num
            } else {
                return scopes[token]!.last!
            }
        }

        // '(' encountered
        i += 1                         // skip '('
        while i < s.count && s[i] == " " { i += 1 }
        let op = parseToken(s, &i)

        if op == "add" {
            while i < s.count && s[i] == " " { i += 1 }
            let v1 = eval(s, &i)
            while i < s.count && s[i] == " " { i += 1 }
            let v2 = eval(s, &i)
            while i < s.count && s[i] == " " { i += 1 }
            if i < s.count && s[i] == ")" { i += 1 }
            return v1 + v2
        } else if op == "mult" {
            while i < s.count && s[i] == " " { i += 1 }
            let v1 = eval(s, &i)
            while i < s.count && s[i] == " " { i += 1 }
            let v2 = eval(s, &i)
            while i < s.count && s[i] == " " { i += 1 }
            if i < s.count && s[i] == ")" { i += 1 }
            return v1 * v2
        } else { // let expression
            var assigned: [String] = []
            while true {
                while i < s.count && s[i] == " " { i += 1 }
                if i >= s.count { break }

                if s[i] == ")" {
                    i += 1
                    break
                }

                // Determine whether next token is the final expression
                if s[i] == "(" || s[i].isNumber || s[i] == "-" {
                    let result = eval(s, &i)
                    while i < s.count && s[i] == " " { i += 1 }
                    if i < s.count && s[i] == ")" { i += 1 }
                    // pop assignments of this let scope
                    for name in assigned.reversed() {
                        scopes[name]!.removeLast()
                        if scopes[name]!.isEmpty { scopes.removeValue(forKey: name) }
                    }
                    return result
                } else {
                    // variable name
                    let varName = parseToken(s, &i)
                    while i < s.count && s[i] == " " { i += 1 }

                    // If next char is ')', this variable itself is the final expression
                    if i < s.count && s[i] == ")" {
                        let result = scopes[varName]!.last!
                        i += 1
                        for name in assigned.reversed() {
                            scopes[name]!.removeLast()
                            if scopes[name]!.isEmpty { scopes.removeValue(forKey: name) }
                        }
                        return result
                    } else {
                        // assignment: evaluate value expression
                        let val = eval(s, &i)
                        scopes[varName, default: []].append(val)
                        assigned.append(varName)
                    }
                }
            }
            // Should never reach here for valid input
            return 0
        }
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    private lateinit var s: String
    private var i = 0
    private val vars = HashMap<String, ArrayDeque<Int>>()

    fun evaluate(expression: String): Int {
        s = expression
        i = 0
        return eval()
    }

    private fun skipSpaces() {
        while (i < s.length && s[i] == ' ') i++
    }

    private fun parseToken(): String {
        skipSpaces()
        val start = i
        while (i < s.length && s[i] != ' ' && s[i] != ')') i++
        return s.substring(start, i)
    }

    private fun isLetter(c: Char): Boolean = c in 'a'..'z'

    private fun getVarValue(name: String): Int {
        return vars[name]?.peek() ?: 0
    }

    private fun eval(): Int {
        skipSpaces()
        if (s[i] == '(') {
            i++ // consume '('
            val op = parseToken()
            return when (op) {
                "let" -> evalLet()
                "add" -> {
                    val v1 = eval()
                    val v2 = eval()
                    skipSpaces()
                    if (i < s.length && s[i] == ')') i++
                    v1 + v2
                }
                "mult" -> {
                    val v1 = eval()
                    val v2 = eval()
                    skipSpaces()
                    if (i < s.length && s[i] == ')') i++
                    v1 * v2
                }
                else -> 0
            }
        } else {
            val token = parseToken()
            return if (token[0].isDigit() || token[0] == '-') token.toInt() else getVarValue(token)
        }
    }

    private fun evalLet(): Int {
        val assigned = mutableListOf<String>()
        while (true) {
            skipSpaces()
            if (s[i] == ')') {
                i++ // consume ')'
                break
            }
            if (isLetter(s[i])) {
                val varName = parseToken()
                skipSpaces()
                if (s[i] == ')') {
                    val result = getVarValue(varName)
                    i++ // consume ')'
                    for (v in assigned.reversed()) {
                        vars[v]?.pop()
                        if (vars[v]?.isEmpty() == true) vars.remove(v)
                    }
                    return result
                } else {
                    val value = eval()
                    vars.getOrPut(varName) { ArrayDeque() }.push(value)
                    assigned.add(varName)
                }
            } else {
                val result = eval()
                skipSpaces()
                if (i < s.length && s[i] == ')') i++
                for (v in assigned.reversed()) {
                    vars[v]?.pop()
                    if (vars[v]?.isEmpty() == true) vars.remove(v)
                }
                return result
            }
        }
        // Should not reach here per problem guarantees
        return 0
    }
}
```

## Dart

```dart
class Solution {
  late String _s;
  int _i = 0;
  final Map<String, List<int>> _env = {};

  int evaluate(String expression) {
    _s = expression;
    _i = 0;
    _env.clear();
    return _eval();
  }

  void _skipSpaces() {
    while (_i < _s.length && _s[_i] == ' ') _i++;
  }

  bool _isDigit(String ch) => ch.codeUnitAt(0) >= 48 && ch.codeUnitAt(0) <= 57;

  String _parseWord() {
    int start = _i;
    while (_i < _s.length && _s[_i] != ' ' && _s[_i] != ')') _i++;
    return _s.substring(start, _i);
  }

  int _eval() {
    _skipSpaces();
    if (_s[_i] != '(') {
      // number or variable
      if (_s[_i] == '-' || _isDigit(_s[_i])) {
        int start = _i;
        _i++;
        while (_i < _s.length && _isDigit(_s[_i])) _i++;
        return int.parse(_s.substring(start, _i));
      } else {
        String varName = _parseWord();
        return _env[varName]!.last;
      }
    }

    // '(' expression
    _i++; // skip '('
    String op = _parseWord();

    if (op == 'add') {
      int v1 = _eval();
      int v2 = _eval();
      _skipSpaces();
      _i++; // skip ')'
      return v1 + v2;
    } else if (op == 'mult') {
      int v1 = _eval();
      int v2 = _eval();
      _skipSpaces();
      _i++; // skip ')'
      return v1 * v2;
    } else { // let
      List<String> assigned = [];
      while (true) {
        _skipSpaces();

        if (_s[_i] == '(') {
          int val = _eval(); // final expression
          _skipSpaces();
          _i++; // skip ')'
          for (var v in assigned) {
            _env[v]!.removeLast();
            if (_env[v]!.isEmpty) _env.remove(v);
          }
          return val;
        }

        int savedIdx = _i;
        String token = _parseWord(); // could be var name or final expr
        _skipSpaces();

        if (_s[_i] == ')') {
          // final expression is token
          int val;
          if (token.isNotEmpty && (token[0] == '-' || _isDigit(token[0]))) {
            val = int.parse(token);
          } else {
            val = _env[token]!.last;
          }
          _i++; // skip ')'
          for (var v in assigned) {
            _env[v]!.removeLast();
            if (_env[v]!.isEmpty) _env.remove(v);
          }
          return val;
        } else {
          // token is variable name for assignment
          String varName = token;
          int exprVal = _eval();
          assigned.add(varName);
          _env.putIfAbsent(varName, () => []).add(exprVal);
        }
      }
    }
  }
}
```

## Golang

```go
func evaluate(expression string) int {
	type envMap map[string][]int

	var skipSpaces func(s string, i *int)
	skipSpaces = func(s string, i *int) {
		for *i < len(s) && s[*i] == ' ' {
			*i++
		}
	}

	var parseWord func(s string, i *int) string
	parseWord = func(s string, i *int) string {
		start := *i
		for *i < len(s) && s[*i] != ' ' && s[*i] != ')' && s[*i] != '(' {
			*i++
		}
		return s[start:*i]
	}

	var eval func(s string, i *int, env envMap) int
	eval = func(s string, i *int, env envMap) int {
		skipSpaces(s, i)
		if s[*i] == '(' {
			*i++ // skip '('
			op := parseWord(s, i)

			var result int
			switch op {
			case "add":
				a := eval(s, i, env)
				b := eval(s, i, env)
				result = a + b
			case "mult":
				a := eval(s, i, env)
				b := eval(s, i, env)
				result = a * b
			default: // let
				var assigned []string
				for {
					skipSpaces(s, i)
					if s[*i] == ')' {
						break
					}
					// final expression starts with '(' or digit or '-'
					if s[*i] == '(' || s[*i] == '-' || (s[*i] >= '0' && s[*i] <= '9') {
						result = eval(s, i, env)
						break
					}
					// otherwise it's a variable name for assignment
					varName := parseWord(s, i)
					skipSpaces(s, i)
					val := eval(s, i, env)
					env[varName] = append(env[varName], val)
					assigned = append(assigned, varName)
				}
				// pop assignments of this let scope
				for _, v := range assigned {
					stack := env[v]
					if len(stack) == 1 {
						delete(env, v)
					} else {
						env[v] = stack[:len(stack)-1]
					}
				}
			}
			skipSpaces(s, i)
			*i++ // skip ')'
			return result
		}

		// number or variable
		if s[*i] == '-' || (s[*i] >= '0' && s[*i] <= '9') {
			start := *i
			*i++
			for *i < len(s) && s[*i] >= '0' && s[*i] <= '9' {
				*i++
			}
			val, _ := strconv.Atoi(s[start:*i])
			return val
		}

		// variable
		name := parseWord(s, i)
		stack := env[name]
		return stack[len(stack)-1]
	}

	idx := 0
	env := make(envMap)
	return eval(expression, &idx, env)
}
```

## Ruby

```ruby
def eval_expr(tokens, idx, env)
  token = tokens[idx]
  if token != '('
    if token[0] =~ /[-\d]/
      return [token.to_i, idx + 1]
    else
      return [env[token].last, idx + 1]
    end
  else
    op = tokens[idx + 1]
    case op
    when 'add'
      v1, nxt = eval_expr(tokens, idx + 2, env)
      v2, nxt = eval_expr(tokens, nxt, env)
      return [v1 + v2, nxt + 1] # skip ')'
    when 'mult'
      v1, nxt = eval_expr(tokens, idx + 2, env)
      v2, nxt = eval_expr(tokens, nxt, env)
      return [v1 * v2, nxt + 1]
    when 'let'
      assigned = []
      i = idx + 2
      loop do
        if tokens[i] == ')'
          break
        end
        # final expression detection
        if tokens[i] != '(' && (i + 1 < tokens.size) && tokens[i + 1] != ')'
          var_name = tokens[i]
          val, i = eval_expr(tokens, i + 2, env)
          env[var_name] << val
          assigned << var_name
        else
          val, i = eval_expr(tokens, i, env)
          break
        end
      end
      i += 1 # skip ')'
      assigned.reverse_each { |v| env[v].pop }
      return [val, i]
    else
      # unreachable for valid input
    end
  end
end

def evaluate(expression)
  tokens = []
  i = 0
  n = expression.length
  while i < n
    c = expression[i]
    if c == '(' || c == ')'
      tokens << c
      i += 1
    elsif c == ' '
      i += 1
    else
      j = i
      while j < n && expression[j] != ' ' && expression[j] != '(' && expression[j] != ')'
        j += 1
      end
      tokens << expression[i...j]
      i = j
    end
  end

  env = Hash.new { |h, k| h[k] = [] }
  val, _ = eval_expr(tokens, 0, env)
  val
end
```

## Scala

```scala
object Solution {
    def evaluate(expression: String): Int = {
        import scala.collection.mutable.{Map => MutableMap, Stack, ArrayBuffer}
        val env = MutableMap[String, Stack[Int]]()

        def eval(expr: String): Int = {
            if (expr(0) != '(') {
                // number or variable
                if (expr(0) == '-' || expr(0).isDigit) expr.toInt
                else env(expr).top
            } else {
                val inner = expr.substring(1, expr.length - 1)
                var bal = 0
                val tokens = ArrayBuffer[String]()
                var start = 0
                for (j <- 0 until inner.length) {
                    inner(j) match {
                        case '(' => bal += 1
                        case ')' => bal -= 1
                        case ' ' if bal == 0 =>
                            tokens += inner.substring(start, j)
                            start = j + 1
                        case _ => // ignore
                    }
                }
                tokens += inner.substring(start)

                tokens(0) match {
                    case "add" =>
                        eval(tokens(1)) + eval(tokens(2))
                    case "mult" =>
                        eval(tokens(1)) * eval(tokens(2))
                    case "let" =>
                        val assigned = ArrayBuffer[String]()
                        var idx = 1
                        while (idx < tokens.length - 1) {
                            val varName = tokens(idx)
                            val valueExpr = tokens(idx + 1)
                            val v = eval(valueExpr)
                            env.getOrElseUpdate(varName, Stack[Int]()).push(v)
                            assigned += varName
                            idx += 2
                        }
                        val result = eval(tokens.last)
                        for (varName <- assigned.reverse) {
                            val stack = env(varName)
                            stack.pop()
                            if (stack.isEmpty) env.remove(varName)
                        }
                        result
                }
            }
        }

        eval(expression)
    }
}
```

## Rust

```rust
use std::collections::HashMap;

struct Parser {
    chars: Vec<char>,
    pos: usize,
}

impl Parser {
    fn new(s: String) -> Self {
        Self { chars: s.chars().collect(), pos: 0 }
    }

    fn skip_spaces(&mut self) {
        while self.pos < self.chars.len() && self.chars[self.pos] == ' ' {
            self.pos += 1;
        }
    }

    fn read_word(&mut self) -> String {
        let start = self.pos;
        while self.pos < self.chars.len()
            && self.chars[self.pos] != ' '
            && self.chars[self.pos] != ')'
        {
            self.pos += 1;
        }
        self.chars[start..self.pos].iter().collect()
    }

    fn lookup(var: &str, env: &HashMap<String, Vec<i32>>) -> i32 {
        *env.get(var).unwrap().last().unwrap()
    }

    fn eval(&mut self, env: &mut HashMap<String, Vec<i32>>) -> i32 {
        self.skip_spaces();
        let c = self.chars[self.pos];
        if c == '(' {
            // compound expression
            self.pos += 1; // consume '('
            let op = self.read_word();
            match op.as_str() {
                "let" => self.eval_let(env),
                "add" => {
                    let a = self.eval(env);
                    self.skip_spaces();
                    let b = self.eval(env);
                    self.skip_spaces(); // should be ')'
                    if self.pos < self.chars.len() && self.chars[self.pos] == ')' {
                        self.pos += 1;
                    }
                    a + b
                }
                "mult" => {
                    let a = self.eval(env);
                    self.skip_spaces();
                    let b = self.eval(env);
                    self.skip_spaces(); // should be ')'
                    if self.pos < self.chars.len() && self.chars[self.pos] == ')' {
                        self.pos += 1;
                    }
                    a * b
                }
                _ => unreachable!(),
            }
        } else if c.is_ascii_digit() || c == '-' {
            let num_str = self.read_word();
            num_str.parse::<i32>().unwrap()
        } else {
            // variable
            let var = self.read_word();
            Self::lookup(&var, env)
        }
    }

    fn eval_let(&mut self, env: &mut HashMap<String, Vec<i32>>) -> i32 {
        let mut assigned_vars: Vec<String> = Vec::new();
        let mut result = 0;
        loop {
            self.skip_spaces();
            if self.pos >= self.chars.len() {
                break;
            }
            if self.chars[self.pos] == ')' {
                self.pos += 1; // consume ')'
                break;
            }

            if self.chars[self.pos].is_ascii_alphabetic() {
                // could be variable name or final expression (variable)
                let var = self.read_word();
                self.skip_spaces();
                if self.chars[self.pos] == ')' {
                    // final expression is a variable reference
                    result = Self::lookup(&var, env);
                    self.pos += 1; // consume ')'
                    break;
                }
                // assignment: evaluate value expression
                let val = self.eval(env);
                env.entry(var.clone()).or_insert_with(Vec::new).push(val);
                assigned_vars.push(var);
            } else {
                // final expression is an expression (number or '(')
                result = self.eval(env);
                self.skip_spaces();
                if self.pos < self.chars.len() && self.chars[self.pos] == ')' {
                    self.pos += 1; // consume ')'
                    break;
                }
            }
        }

        // pop assignments in reverse order
        for var in assigned_vars.iter().rev() {
            if let Some(stack) = env.get_mut(var) {
                stack.pop();
                if stack.is_empty() {
                    env.remove(var);
                }
            }
        }
        result
    }
}

impl Solution {
    pub fn evaluate(expression: String) -> i32 {
        let mut parser = Parser::new(expression);
        let mut env: HashMap<String, Vec<i32>> = HashMap::new();
        parser.eval(&mut env)
    }
}
```

## Racket

```racket
(define (skip-spaces s i)
  (let loop ((j i))
    (if (and (< j (string-length s))
             (char-whitespace? (string-ref s j)))
        (loop (+ j 1))
        j)))

(define (digit-char? c)
  (let ((code (char->integer c)))
    (and (>= code 48) (<= code 57))))

(define (read-token s i)
  (let loop ((j i) (chars '()))
    (if (or (= j (string-length s))
            (char-whitespace? (string-ref s j))
            (eqv? (string-ref s j) #\)))
        (values (list->string (reverse chars)) j)
        (loop (+ j 1) (cons (string-ref s j) chars)))))

(define (read-identifier s i)
  (let loop ((j i) (chars '()))
    (if (and (< j (string-length s))
             (char-alphabetic? (string-ref s j)))
        (loop (+ j 1) (cons (string-ref s j) chars))
        (values (list->string (reverse chars)) j))))

;; evaluate a token starting at i (number, variable or sub‑expression)
(define (eval-token s i env)
  (let ((i (skip-spaces s i)))
    (if (= i (string-length s))
        (error "unexpected end of input")
        (let ((ch (string-ref s i)))
          (cond
            [(char=? ch #\()
             (eval-expr s i env)]
            [else
             (define-values (tok nxt) (read-token s i))
             (if (or (digit-char? (string-ref tok 0))
                     (eqv? (string-ref tok 0) #\-))
                 (values (string->number tok) nxt)
                 (let ((stack (hash-ref env tok '())))
                   (if (null? stack)
                       (error "undefined variable")
                       (values (car stack) nxt))))])))))

;; evaluate a parenthesized expression starting at '('
(define (eval-expr s i env)
  ;; skip '('
  (let ((i (+ i 1)))
    (set! i (skip-spaces s i))
    (define-values (op nxt) (read-token s i))
    (set! i nxt)
    (cond
      [(string=? op "add")
       (define-values (v1 i1) (eval-token s i env))
       (define-values (v2 i2) (eval-token s i1 env))
       (set! i (skip-spaces s i2))
       (when (not (char=? (string-ref s i) #\))) (error "expected )"))
       (values (+ v1 v2) (+ i 1))]
      [(string=? op "mult")
       (define-values (v1 i1) (eval-token s i env))
       (define-values (v2 i2) (eval-token s i1 env))
       (set! i (skip-spaces s i2))
       (when (not (char=? (string-ref s i) #\))) (error "expected )"))
       (values (* v1 v2) (+ i 1))]
      [(string=? op "let")
       (let loop ((i (skip-spaces s i)) (vars '()))
         (set! i (skip-spaces s i))
         (when (char=? (string-ref s i) #\))
           (error "let missing final expression"))
         (define ch (string-ref s i))
         (if (char-alphabetic? ch)
             ;; variable assignment
             (begin
               (define-values (var i1) (read-identifier s i))
               (set! i (skip-spaces s i1))
               (define-values (val i2) (eval-token s i env))
               (hash-set! env var (cons val (hash-ref env var '())))
               (loop (skip-spaces s i2) (cons var vars)))
             ;; final expression
             (begin
               (define-values (val i1) (eval-token s i env))
               ;; pop variables introduced in this let
               (for ([v (in-list vars)])
                 (let ((stack (hash-ref env v)))
                   (if (null? (cdr stack))
                       (hash-remove! env v)
                       (hash-set! env v (cdr stack)))))
               (set! i (skip-spaces s i1))
               (when (not (char=? (string-ref s i) #\))) (error "expected )"))
               (values val (+ i 1))))))]
      [else (error "unknown operator")])))
       
(define (evaluate expression)
  (let ((env (make-hash)))
    (define-values (val _) (eval-token expression 0 env))
    val))
```

## Erlang

```erlang
-module(solution).
-export([evaluate/1]).

-spec evaluate(Expression :: unicode:unicode_binary()) -> integer().
evaluate(Expression) ->
    Str = binary_to_list(Expression),
    {Val, _Pos} = parse_expr(Str, 0, #{}),
    Val.

%% --------------------------------------------------------------------
%% Parsing entry
parse_expr(Str, Pos, Env) ->
    Pos1 = skip_spaces(Str, Pos),
    Char = get_char(Str, Pos1),
    case Char of
        $( ->
            parse_paren(Str, Pos1, Env);
        $- ;
        C when C >= $0, C =< $9 ->
            parse_number(Str, Pos1);
        _ ->
            {Var, NewPos} = parse_word(Str, Pos1),
            Value = maps:get(list_to_binary(Var), Env),
            {Value, NewPos}
    end.

%% --------------------------------------------------------------------
%% Parenthesized expressions
parse_paren(Str, Pos, Env) ->
    % '(' at Pos
    Pos1 = Pos + 1,
    Pos2 = skip_spaces(Str, Pos1),
    {OpList, OpEnd} = parse_word(Str, Pos2),
    Op = list_to_atom(OpList),
    case Op of
        add ->
            {V1, P1} = parse_expr(Str, OpEnd, Env),
            {V2, P2} = parse_expr(Str, P1, Env),
            P3 = skip_spaces(Str, P2),
            % consume ')'
            {V1 + V2, P3 + 1};
        mult ->
            {V1, P1} = parse_expr(Str, OpEnd, Env),
            {V2, P2} = parse_expr(Str, P1, Env),
            P3 = skip_spaces(Str, P2),
            {V1 * V2, P3 + 1};
        let ->
            let_process(Str, OpEnd, Env)
    end.

%% --------------------------------------------------------------------
%% Let processing
let_process(Str, Pos, Env) ->
    let_loop(Str, Pos, Env).

let_loop(Str, Pos, CurrEnv) ->
    Pos1 = skip_spaces(Str, Pos),
    Char = get_char(Str, Pos1),
    case Char of
        $) ->
            % should not happen (no final expression)
            {0, Pos1 + 1};
        $( ; $- ;
        C when C >= $0, C =< $9 ->
            %% Final expression is a number or sub‑expression
            {Val, NewPos} = parse_expr(Str, Pos1, CurrEnv),
            P2 = skip_spaces(Str, NewPos),
            {Val, P2 + 1};
        _Letter when (Char >= $a, Char =< $z) orelse (Char >= $A, Char =< $Z) ->
            %% Could be final variable or assignment
            {VarName, AfterVarPos} = parse_word(Str, Pos1),
            AfterVarSkip = skip_spaces(Str, AfterVarPos),
            NextChar = get_char(Str, AfterVarSkip),
            case NextChar of
                $) ->
                    %% Final expression is this variable
                    Val = maps:get(list_to_binary(VarName), CurrEnv),
                    {Val, AfterVarSkip + 1};
                _ ->
                    %% Assignment: VarName gets value of next expr
                    {ExprVal, ExprPos} = parse_expr(Str, AfterVarSkip, CurrEnv),
                    NewEnv = maps:put(list_to_binary(VarName), ExprVal, CurrEnv),
                    let_loop(Str, ExprPos, NewEnv)
            end
    end.

%% --------------------------------------------------------------------
%% Helpers

skip_spaces(Str, Pos) ->
    Len = length(Str),
    skip_spaces_loop(Str, Pos, Len).

skip_spaces_loop(_Str, Pos, Len) when Pos >= Len -> Pos;
skip_spaces_loop(Str, Pos, Len) ->
    case get_char(Str, Pos) of
        $\s -> skip_spaces_loop(Str, Pos + 1, Len);
        _   -> Pos
    end.

parse_word(Str, Pos) ->
    parse_word_collect(Str, Pos, []).

parse_word_collect(Str, Pos, Acc) ->
    Char = get_char(Str, Pos),
    case Char of
        $\s ; $) ->
            {lists:reverse(Acc), Pos};
        _ ->
            parse_word_collect(Str, Pos + 1, [Char | Acc])
    end.

parse_number(Str, Pos) ->
    case get_char(Str, Pos) of
        $- -> {Sign, Start} = {-1, Pos + 1},
              parse_digits(Str, Start, 0, Sign);
        _  -> parse_digits(Str, Pos, 0, 1)
    end.

parse_digits(Str, Pos, Acc, Sign) ->
    Char = get_char(Str, Pos),
    case Char >= $0 andalso Char =< $9 of
        true ->
            NewAcc = Acc * 10 + (Char - $0),
            parse_digits(Str, Pos + 1, NewAcc, Sign);
        false ->
            {Sign * Acc, Pos}
    end.

get_char(Str, Pos) ->
    Len = length(Str),
    if Pos < Len -> lists:nth(Pos + 1, Str);
       true      -> $\s
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec evaluate(expression :: String.t()) :: integer
  def evaluate(expression) do
    {value, _} = eval_expr(expression, 0, %{})
    value
  end

  # Evaluate an expression starting at index i with current environment env.
  defp eval_expr(str, i, env) do
    c = :binary.at(str, i)

    cond do
      c == ?\( ->
        parse_compound(str, i + 1, env)

      true ->
        {token, next_i} = read_token(str, i)
        value =
          case Integer.parse(token) do
            {num, ""} -> num
            _ -> lookup(token, env)
          end

        {value, next_i}
    end
  end

  # Parse a compound expression (add, mult, let) after '('.
  defp parse_compound(str, i, env) do
    {op, i2} = read_token(str, i)
    i2 = skip_spaces(str, i2)

    case op do
      "add" ->
        {v1, i3} = eval_expr(str, i2, env)
        i3 = skip_spaces(str, i3)
        {v2, i4} = eval_expr(str, i3, env)
        i4 = skip_spaces(str, i4)
        # assume next char is ')'
        {v1 + v2, i4 + 1}

      "mult" ->
        {v1, i3} = eval_expr(str, i2, env)
        i3 = skip_spaces(str, i3)
        {v2, i4} = eval_expr(str, i3, env)
        i4 = skip_spaces(str, i4)
        {v1 * v2, i4 + 1}

      "let" ->
        eval_let(str, i2, env)

      _ ->
        raise "unknown operator"
    end
  end

  # Evaluate a let expression starting at index i (right after the word "let").
  defp eval_let(str, i, env) do
    i = skip_spaces(str, i)
    {env_after, i_end, result, assigned} = let_process(str, i, env, [])
    # i_end points to ')'
    env_original = pop_assignments(env_after, assigned)
    {result, i_end + 1}
  end

  # Process tokens inside a let expression.
  defp let_process(str, i, env, assigned) do
    c = :binary.at(str, i)

    cond do
      c == ?\) ->
        # Should not happen; no final expression yet.
        {env, i, nil, assigned}

      true ->
        if c == ?\( or (c >= ?0 and c <= ?9) or c == ?- do
          # Final expression is an expression starting here.
          {val, new_i} = eval_expr(str, i, env)
          {env, new_i, val, assigned}
        else
          # Read a variable name.
          {var, next_i} = read_token(str, i)
          next_i = skip_spaces(str, next_i)

          if :binary.at(str, next_i) == ?\) do
            # Final expression is the variable itself.
            val = lookup(var, env)
            {env, next_i, val, assigned}
          else
            # Parse the value expression for assignment.
            {val_expr, after_val} = eval_expr(str, next_i, env)
            new_env = assign(var, val_expr, env)
            let_process(str, after_val, new_env, [var | assigned])
          end
        end
    end
  end

  # Skip spaces starting from index i.
  defp skip_spaces(str, i) do
    len = byte_size(str)

    if i < len and :binary.at(str, i) == ?\s do
      skip_spaces(str, i + 1)
    else
      i
    end
  end

  # Read a token (sequence of non-space, non-')' characters) starting at i.
  defp read_token(str, i) do
    {chars_rev, j} = read_token_acc(str, i, [])
    token = :binary.list_to_bin(Enum.reverse(chars_rev))
    {token, j}
  end

  defp read_token_acc(str, i, acc) when i < byte_size(str) do
    c = :binary.at(str, i)

    if c == ?\s or c == ?) do
      {acc, i}
    else
      read_token_acc(str, i + 1, [c | acc])
    end
  end

  defp read_token_acc(_, i, acc), do: {acc, i}

  # Lookup variable value from environment.
  defp lookup(var, env) do
    case Map.get(env, var) do
      [value | _] -> value
      nil -> raise "undefined variable #{var}"
    end
  end

  # Assign a variable in the environment (push onto its stack).
  defp assign(var, val, env) do
    stack = Map.get(env, var, [])
    Map.put(env, var, [val | stack])
  end

  # Pop assignments made in the current let scope.
  defp pop_assignments(env, []), do: env

  defp pop_assignments(env, [var | rest]) do
    case Map.get(env, var) do
      [_top | tail] ->
        new_env =
          if tail == [] do
            Map.delete(env, var)
          else
            Map.put(env, var, tail)
          end

        pop_assignments(new_env, rest)

      nil ->
        env
    end
  end
end
```
