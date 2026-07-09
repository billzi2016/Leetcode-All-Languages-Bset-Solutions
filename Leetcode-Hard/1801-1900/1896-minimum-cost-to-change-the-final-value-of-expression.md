# 1896. Minimum Cost to Change the Final Value of Expression

## Cpp

```cpp
class Solution {
public:
    int minOperationsToFlip(string expression) {
        const int INF = 1e9;
        auto combine = [&](pair<int,int> L, pair<int,int> R, char op) -> pair<int,int> {
            int res0 = INF, res1 = INF;
            // original operator
            if (op == '&') {
                res0 = min({L.first + R.first, L.first + R.second, L.second + R.first});
                res1 = L.second + R.second;
            } else { // '|'
                res0 = L.first + R.first;
                res1 = min({L.second + R.second, L.second + R.first, L.first + R.second});
            }
            // flipped operator (cost +1)
            char op2 = (op == '&') ? '|' : '&';
            if (op2 == '&') {
                int r0 = min({L.first + R.first, L.first + R.second, L.second + R.first});
                int r1 = L.second + R.second;
                res0 = min(res0, r0 + 1);
                res1 = min(res1, r1 + 1);
            } else {
                int r0 = L.first + R.first;
                int r1 = min({L.second + R.second, L.second + R.first, L.first + R.second});
                res0 = min(res0, r0 + 1);
                res1 = min(res1, r1 + 1);
            }
            return {res0, res1};
        };
        
        vector<pair<int,int>> vals;
        vector<char> ops;
        auto applyOp = [&]() {
            char op = ops.back(); ops.pop_back();
            auto right = vals.back(); vals.pop_back();
            auto left = vals.back(); vals.pop_back();
            vals.push_back(combine(left, right, op));
        };
        
        for (char c : expression) {
            if (c == '0' || c == '1') {
                if (c == '0')
                    vals.emplace_back(0, 1); // cost to be 0 is 0, to be 1 is 1
                else
                    vals.emplace_back(1, 0); // cost to be 0 is 1, to be 1 is 0
            } else if (c == '(') {
                ops.push_back(c);
            } else if (c == ')') {
                while (!ops.empty() && ops.back() != '(') applyOp();
                if (!ops.empty() && ops.back() == '(') ops.pop_back(); // remove '('
            } else { // '&' or '|'
                while (!ops.empty() && ops.back() != '(') applyOp();
                ops.push_back(c);
            }
        }
        while (!ops.empty()) applyOp();
        
        auto finalPair = vals.back();
        int original = (finalPair.first == 0 ? 0 : 1); // the value with zero cost
        return original == 0 ? finalPair.second : finalPair.first;
    }
};
```

## Java

```java
class Solution {
    public int minOperationsToFlip(String expression) {
        Deque<int[]> valStack = new ArrayDeque<>();
        Deque<Character> opStack = new ArrayDeque<>();

        for (int i = 0; i < expression.length(); ++i) {
            char c = expression.charAt(i);
            if (c == '0' || c == '1') {
                int[] costs = new int[2];
                if (c == '0') {
                    costs[0] = 0;
                    costs[1] = 1;
                } else {
                    costs[0] = 1;
                    costs[1] = 0;
                }
                valStack.push(costs);
            } else if (c == '(') {
                opStack.push(c);
            } else if (c == ')') {
                while (opStack.peek() != '(') {
                    applyOp(valStack, opStack);
                }
                opStack.pop(); // pop '('
            } else if (c == '&' || c == '|') {
                while (!opStack.isEmpty() && opStack.peek() != '(') {
                    applyOp(valStack, opStack);
                }
                opStack.push(c);
            }
        }

        while (!opStack.isEmpty()) {
            applyOp(valStack, opStack);
        }

        int[] finalCosts = valStack.pop();
        return finalCosts[0] == 0 ? finalCosts[1] : finalCosts[0];
    }

    private void applyOp(Deque<int[]> valStack, Deque<Character> opStack) {
        char op = opStack.pop();
        int[] right = valStack.pop();
        int[] left = valStack.pop();

        // keep original operator
        int[] keep = compute(op, left, right);
        // flip operator
        char flippedOp = (op == '&') ? '|' : '&';
        int[] flip = compute(flippedOp, left, right);

        int cost0 = Math.min(keep[0], flip[0] + 1);
        int cost1 = Math.min(keep[1], flip[1] + 1);
        valStack.push(new int[]{cost0, cost1});
    }

    private int[] compute(char op, int[] L, int[] R) {
        int c0, c1;
        if (op == '&') {
            c1 = L[1] + R[1];
            c0 = Math.min(Math.min(L[0] + R[0], L[0] + R[1]), L[1] + R[0]);
        } else { // '|'
            c0 = L[0] + R[0];
            c1 = Math.min(Math.min(L[1] + R[1], L[0] + R[1]), L[1] + R[0]);
        }
        return new int[]{c0, c1};
    }
}
```

## Python

```python
class Solution(object):
    def minOperationsToFlip(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        def combine(op, left, right):
            l0, l1 = left
            r0, r1 = right
            if op == '&':
                # keep '&'
                cost0_orig = min(l0 + r0, l0 + r1, l1 + r0)
                cost1_orig = l1 + r1
                # flip to '|'
                cost0_flip = l0 + r0
                cost1_flip = min(l1 + r1, l1 + r0, l0 + r1)
            else:  # op == '|'
                # keep '|'
                cost0_orig = l0 + r0
                cost1_orig = min(l1 + r1, l1 + r0, l0 + r1)
                # flip to '&'
                cost0_flip = min(l0 + r0, l0 + r1, l1 + r0)
                cost1_flip = l1 + r1
            c0 = min(cost0_orig, cost0_flip + 1)
            c1 = min(cost1_orig, cost1_flip + 1)
            return (c0, c1)

        vals = []
        ops = []
        i, n = 0, len(expression)
        while i < n:
            ch = expression[i]
            if ch == '(':
                ops.append(ch)
                i += 1
            elif ch == ')':
                while ops and ops[-1] != '(':
                    op = ops.pop()
                    right = vals.pop()
                    left = vals.pop()
                    vals.append(combine(op, left, right))
                ops.pop()  # remove '('
                i += 1
            elif ch in '&|':
                while ops and ops[-1] in '&|':
                    op = ops.pop()
                    right = vals.pop()
                    left = vals.pop()
                    vals.append(combine(op, left, right))
                ops.append(ch)
                i += 1
            else:  # '0' or '1'
                if ch == '0':
                    vals.append((0, 1))  # cost to be 0 is 0, to be 1 is 1
                else:
                    vals.append((1, 0))
                i += 1

        while ops:
            op = ops.pop()
            right = vals.pop()
            left = vals.pop()
            vals.append(combine(op, left, right))

        final0, final1 = vals[-1]
        # The current value has zero cost; flip it.
        return final1 if final0 == 0 else final0
```

## Python3

```python
class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        # helper to combine two subexpressions with an operator
        def combine(l0, l1, r0, r1, op):
            if op == '&':
                keep0 = min(l0 + min(r0, r1), r0 + min(l0, l1))
                keep1 = l1 + r1
                # flipped to '|'
                flip0 = l0 + r0
                flip1 = min(l1 + min(r0, r1), r1 + min(l0, l1))
            else:  # op == '|'
                keep1 = min(l1 + min(r0, r1), r1 + min(l0, l1))
                keep0 = l0 + r0
                # flipped to '&'
                flip1 = l1 + r1
                flip0 = min(l0 + min(r0, r1), r0 + min(l0, l1))
            return min(keep0, flip0 + 1), min(keep1, flip1 + 1)

        vals = []   # stack of (cost0, cost1)
        ops = []    # stack of operators and '('

        def apply():
            op = ops.pop()
            r0, r1 = vals.pop()
            l0, l1 = vals.pop()
            vals.append(combine(l0, l1, r0, r1, op))

        i = 0
        n = len(expression)
        while i < n:
            ch = expression[i]
            if ch == '0':
                vals.append((0, 1))
            elif ch == '1':
                vals.append((1, 0))
            elif ch in '&|':
                # left-to-right: resolve previous operators of same precedence
                while ops and ops[-1] in '&|':
                    apply()
                ops.append(ch)
            elif ch == '(':
                ops.append(ch)
            else:  # ')'
                while ops and ops[-1] != '(':
                    apply()
                ops.pop()  # remove '('
            i += 1

        while ops:
            apply()

        final0, final1 = vals[0]
        # original value is whichever cost is zero
        return final1 if final0 == 0 else final0
```

## C

```c
#include <string.h>
#include <stdlib.h>

typedef struct {
    int c[2];   // c[0]: min ops to make value 0, c[1]: min ops to make value 1
} Node;

static const int INF = 1000000000;

static Node combine(Node a, Node b, char op) {
    Node res;
    int best0 = INF, best1 = INF;
    // without changing operator
    for (int lv = 0; lv <= 1; ++lv) {
        for (int rv = 0; rv <= 1; ++rv) {
            int out = (op == '&') ? (lv & rv) : (lv | rv);
            int cost = a.c[lv] + b.c[rv];
            if (out == 0) {
                if (cost < best0) best0 = cost;
            } else {
                if (cost < best1) best1 = cost;
            }
        }
    }
    // with changing operator (cost +1)
    char op2 = (op == '&') ? '|' : '&';
    int best0b = INF, best1b = INF;
    for (int lv = 0; lv <= 1; ++lv) {
        for (int rv = 0; rv <= 1; ++rv) {
            int out = (op2 == '&') ? (lv & rv) : (lv | rv);
            int cost = a.c[lv] + b.c[rv] + 1;
            if (out == 0) {
                if (cost < best0b) best0b = cost;
            } else {
                if (cost < best1b) best1b = cost;
            }
        }
    }
    res.c[0] = (best0 < best0b) ? best0 : best0b;
    res.c[1] = (best1 < best1b) ? best1 : best1b;
    return res;
}

int minOperationsToFlip(char* expression) {
    int n = strlen(expression);
    Node *valStack = (Node*)malloc(sizeof(Node) * (n + 5));
    char *opStack = (char*)malloc(sizeof(char) * (n + 5));
    int vtop = 0, otop = 0;

    for (int i = 0; i < n; ++i) {
        char ch = expression[i];
        if (ch == '0' || ch == '1') {
            Node node;
            node.c[0] = (ch == '0') ? 0 : 1;
            node.c[1] = (ch == '1') ? 0 : 1;
            valStack[vtop++] = node;

            while (vtop >= 2 && otop > 0 && opStack[otop - 1] != '(') {
                Node b = valStack[--vtop];
                Node a = valStack[--vtop];
                char oper = opStack[--otop];
                Node c = combine(a, b, oper);
                valStack[vtop++] = c;
            }
        } else if (ch == '(') {
            opStack[otop++] = ch;
        } else if (ch == ')') {
            while (otop > 0 && opStack[otop - 1] != '(') {
                Node b = valStack[--vtop];
                Node a = valStack[--vtop];
                char oper = opStack[--otop];
                Node c = combine(a, b, oper);
                valStack[vtop++] = c;
            }
            if (otop > 0 && opStack[otop - 1] == '(') otop--; // pop '('

            while (vtop >= 2 && otop > 0 && opStack[otop - 1] != '(') {
                Node b = valStack[--vtop];
                Node a = valStack[--vtop];
                char oper = opStack[--otop];
                Node c = combine(a, b, oper);
                valStack[vtop++] = c;
            }
        } else if (ch == '&' || ch == '|') {
            opStack[otop++] = ch;
        }
    }

    while (otop > 0) {
        Node b = valStack[--vtop];
        Node a = valStack[--vtop];
        char oper = opStack[--otop];
        Node c = combine(a, b, oper);
        valStack[vtop++] = c;
    }

    Node finalNode = valStack[0];
    int original = (finalNode.c[0] == 0) ? 0 : 1;
    int answer = finalNode.c[original ^ 1];

    free(valStack);
    free(opStack);
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinOperationsToFlip(string expression) {
        Stack<int[]> vals = new Stack<int[]>();
        Stack<char> ops = new Stack<char>();

        void Apply() {
            var right = vals.Pop();
            var left = vals.Pop();
            char op = ops.Pop();
            vals.Push(Combine(left, right, op));
        }

        int[] Combine(int[] left, int[] right, char op) {
            int l0 = left[0], l1 = left[1];
            int r0 = right[0], r1 = right[1];

            int keep0, keep1;
            if (op == '&') {
                // result 0: left 0 or right 0
                keep0 = Math.Min(l0 + Math.Min(r0, r1), r0 + Math.Min(l0, l1));
                // result 1: both 1
                keep1 = l1 + r1;
            } else { // '|'
                // result 0: both 0
                keep0 = l0 + r0;
                // result 1: left 1 or right 1
                keep1 = Math.Min(l1 + Math.Min(r0, r1), r1 + Math.Min(l0, l1));
            }

            int flip0, flip1;
            if (op == '&') {
                // flipped to '|'
                int f0 = l0 + r0;                                   // both 0
                int f1 = Math.Min(l1 + Math.Min(r0, r1), r1 + Math.Min(l0, l1));
                flip0 = f0 + 1;
                flip1 = f1 + 1;
            } else {
                // flipped to '&'
                int f0 = Math.Min(l0 + Math.Min(r0, r1), r0 + Math.Min(l0, l1));
                int f1 = l1 + r1;
                flip0 = f0 + 1;
                flip1 = f1 + 1;
            }

            return new int[] { Math.Min(keep0, flip0), Math.Min(keep1, flip1) };
        }

        foreach (char c in expression) {
            if (c == '0' || c == '1') {
                int val = c - '0';
                int[] arr = new int[2];
                arr[val] = 0;
                arr[1 - val] = 1; // flip the digit
                vals.Push(arr);
            } else if (c == '(') {
                ops.Push(c);
            } else if (c == ')') {
                while (ops.Peek() != '(') Apply();
                ops.Pop(); // remove '('
            } else if (c == '&' || c == '|') {
                while (ops.Count > 0 && ops.Peek() != '(') Apply();
                ops.Push(c);
            }
        }

        while (ops.Count > 0) Apply();

        int[] finalCost = vals.Pop();
        int originalValue = finalCost[0] == 0 ? 0 : 1;
        return originalValue == 0 ? finalCost[1] : finalCost[0];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} expression
 * @return {number}
 */
var minOperationsToFlip = function(expression) {
    const valStack = []; // each element: [cost0, cost1]
    const opStack = [];

    const combine = (op, left, right) => {
        let cost0Orig, cost1Orig, cost0Flip, cost1Flip;
        if (op === '&') {
            // original '&'
            cost0Orig = Math.min(
                left[0] + Math.min(right[0], right[1]),
                right[0] + Math.min(left[0], left[1])
            );
            cost1Orig = left[1] + right[1];
            // flipped to '|'
            cost0Flip = left[0] + right[0]; // both 0 for '|'
            cost1Flip = Math.min(
                left[1] + Math.min(right[0], right[1]),
                right[1] + Math.min(left[0], left[1])
            );
        } else { // op === '|'
            // original '|'
            cost1Orig = Math.min(
                left[1] + Math.min(right[0], right[1]),
                right[1] + Math.min(left[0], left[1])
            );
            cost0Orig = left[0] + right[0];
            // flipped to '&'
            cost1Flip = left[1] + right[1]; // both 1 for '&'
            cost0Flip = Math.min(
                left[0] + Math.min(right[0], right[1]),
                right[0] + Math.min(left[0], left[1])
            );
        }
        const cost0 = Math.min(cost0Orig, (cost0Flip !== undefined ? cost0Flip + 1 : Infinity));
        const cost1 = Math.min(cost1Orig, (cost1Flip !== undefined ? cost1Flip + 1 : Infinity));
        return [cost0, cost1];
    };

    for (let i = 0; i < expression.length; ++i) {
        const ch = expression[i];
        if (ch === '0' || ch === '1') {
            const pair = ch === '0' ? [0, 1] : [1, 0];
            valStack.push(pair);
            while (opStack.length && opStack[opStack.length - 1] !== '(') {
                const oper = opStack.pop();
                const right = valStack.pop();
                const left = valStack.pop();
                valStack.push(combine(oper, left, right));
            }
        } else if (ch === '(') {
            opStack.push(ch);
        } else if (ch === '&' || ch === '|') {
            opStack.push(ch);
        } else if (ch === ')') {
            while (opStack.length && opStack[opStack.length - 1] !== '(') {
                const oper = opStack.pop();
                const right = valStack.pop();
                const left = valStack.pop();
                valStack.push(combine(oper, left, right));
            }
            // pop the '('
            if (opStack.length) opStack.pop();
        }
    }

    while (opStack.length) {
        const oper = opStack.pop();
        const right = valStack.pop();
        const left = valStack.pop();
        valStack.push(combine(oper, left, right));
    }

    const finalPair = valStack[0];
    // The side with zero cost corresponds to the original evaluation.
    return finalPair[0] === 0 ? finalPair[1] : finalPair[0];
};
```

## Typescript

```typescript
function minOperationsToFlip(expression: string): number {
    const valStack: number[][] = [];
    const opStack: string[] = [];

    const combine = (L: number[], R: number[], op: string): number[] => {
        let keep0: number, keep1: number;
        if (op === '&') {
            // result 1
            keep1 = L[1] + R[1];
            // result 0
            const leftZero = L[0] + Math.min(R[0], R[1]);
            const rightZero = R[0] + Math.min(L[0], L[1]);
            keep0 = Math.min(leftZero, rightZero);
        } else { // '|'
            // result 0
            keep0 = L[0] + R[0];
            // result 1
            const leftOne = L[1] + Math.min(R[0], R[1]);
            const rightOne = R[1] + Math.min(L[0], L[1]);
            keep1 = Math.min(leftOne, rightOne);
        }

        // flip operator
        const flippedOp = op === '&' ? '|' : '&';
        let flip0: number, flip1: number;
        if (flippedOp === '&') {
            flip1 = L[1] + R[1];
            const leftZeroF = L[0] + Math.min(R[0], R[1]);
            const rightZeroF = R[0] + Math.min(L[0], L[1]);
            flip0 = Math.min(leftZeroF, rightZeroF);
        } else {
            flip0 = L[0] + R[0];
            const leftOneF = L[1] + Math.min(R[0], R[1]);
            const rightOneF = R[1] + Math.min(L[0], L[1]);
            flip1 = Math.min(leftOneF, rightOneF);
        }
        flip0 += 1;
        flip1 += 1;

        return [Math.min(keep0, flip0), Math.min(keep1, flip1)];
    };

    const apply = () => {
        const op = opStack.pop()!;
        const right = valStack.pop()!;
        const left = valStack.pop()!;
        valStack.push(combine(left, right, op));
    };

    for (let i = 0; i < expression.length; i++) {
        const ch = expression[i];
        if (ch === '0' || ch === '1') {
            if (ch === '0') {
                valStack.push([0, 1]);
            } else {
                valStack.push([1, 0]);
            }
        } else if (ch === '(') {
            opStack.push(ch);
        } else if (ch === '&' || ch === '|') {
            while (opStack.length && opStack[opStack.length - 1] !== '(') {
                apply();
            }
            opStack.push(ch);
        } else if (ch === ')') {
            while (opStack.length && opStack[opStack.length - 1] !== '(') {
                apply();
            }
            opStack.pop(); // remove '('
        }
    }

    while (opStack.length) {
        apply();
    }

    const finalPair = valStack.pop()!;
    return Math.min(finalPair[0], finalPair[1]);
}
```

## Php

```php
class Solution {
    /**
     * @param String $expression
     * @return Integer
     */
    function minOperationsToFlip($expression) {
        $vals = []; // stack of dp arrays [cost0, cost1]
        $ops  = []; // stack of operators and '('

        $len = strlen($expression);
        for ($i = 0; $i < $len; $i++) {
            $ch = $expression[$i];
            if ($ch === '0' || $ch === '1') {
                // dp[0] = cost to make value 0, dp[1] = cost to make value 1
                $dp = [$ch === '0' ? 0 : 1, $ch === '1' ? 0 : 1];
                $vals[] = $dp;
            } elseif ($ch === '&' || $ch === '|') {
                while (!empty($ops) && end($ops) !== '(') {
                    $this->applyOp($vals, $ops);
                }
                $ops[] = $ch;
            } elseif ($ch === '(') {
                $ops[] = $ch;
            } else { // ')'
                while (!empty($ops) && end($ops) !== '(') {
                    $this->applyOp($vals, $ops);
                }
                array_pop($ops); // pop '('
            }
        }

        while (!empty($ops)) {
            $this->applyOp($vals, $ops);
        }

        $final = array_pop($vals);
        return $final[0] === 0 ? $final[1] : $final[0];
    }

    private function applyOp(&$vals, &$ops) {
        $op = array_pop($ops);
        $right = array_pop($vals);
        $left  = array_pop($vals);

        $INF = PHP_INT_MAX;
        $res = [$INF, $INF]; // [cost0, cost1]

        foreach ([$op => 0, ($op === '&' ? '|' : '&') => 1] as $effectiveOp => $flipCost) {
            if ($effectiveOp === '&') {
                // result 1 only when both are 1
                $c1 = $left[1] + $right[1];
                // result 0 when at least one is 0
                $c0 = min(
                    $left[0] + $right[0],
                    $left[0] + $right[1],
                    $left[1] + $right[0]
                );
            } else { // '|'
                // result 0 only when both are 0
                $c0 = $left[0] + $right[0];
                // result 1 when at least one is 1
                $c1 = min(
                    $left[1] + $right[1],
                    $left[1] + $right[0],
                    $left[0] + $right[1]
                );
            }
            $res[0] = min($res[0], $c0 + $flipCost);
            $res[1] = min($res[1], $c1 + $flipCost);
        }

        $vals[] = $res;
    }
}
```

## Swift

```swift
class Solution {
    func minOperationsToFlip(_ expression: String) -> Int {
        var values = [(zero: Int, one: Int)]()
        var ops = [Character]()
        let chars = Array(expression)
        var i = 0
        
        func apply() {
            guard let op = ops.popLast() else { return }
            let right = values.removeLast()
            let left = values.removeLast()
            var resZero = Int.max
            var resOne = Int.max
            
            if op == "&" {
                // keep '&'
                let keepZero = min(min(left.zero + right.zero, left.zero + right.one), left.one + right.zero)
                let keepOne = left.one + right.one
                // flip to '|', cost +1
                let flipZero = left.zero + right.zero + 1
                let flipOne = min(min(left.one + right.zero, left.zero + right.one), left.one + right.one) + 1
                resZero = min(keepZero, flipZero)
                resOne = min(keepOne, flipOne)
            } else { // '|'
                // keep '|'
                let keepZero = left.zero + right.zero
                let keepOne = min(min(left.one + right.zero, left.zero + right.one), left.one + right.one)
                // flip to '&', cost +1
                let flipZero = min(min(left.zero + right.zero, left.zero + right.one), left.one + right.zero) + 1
                let flipOne = left.one + right.one + 1
                resZero = min(keepZero, flipZero)
                resOne = min(keepOne, flipOne)
            }
            
            values.append((zero: resZero, one: resOne))
        }
        
        while i < chars.count {
            let ch = chars[i]
            if ch == "0" || ch == "1" {
                if ch == "0" {
                    values.append((zero: 0, one: 1))
                } else {
                    values.append((zero: 1, one: 0))
                }
                i += 1
            } else if ch == "(" {
                ops.append(ch)
                i += 1
            } else if ch == ")" {
                while let last = ops.last, last != "(" {
                    apply()
                }
                if !ops.isEmpty { ops.removeLast() } // pop '('
                i += 1
            } else if ch == "&" || ch == "|" {
                while let last = ops.last, last != "(" {
                    apply()
                }
                ops.append(ch)
                i += 1
            } else {
                i += 1
            }
        }
        
        while !ops.isEmpty {
            apply()
        }
        
        let finalPair = values.last!
        return finalPair.zero == 0 ? finalPair.one : finalPair.zero
    }
}
```

## Kotlin

```kotlin
import java.util.ArrayDeque

class Solution {
    fun minOperationsToFlip(expression: String): Int {
        val values = ArrayDeque<IntArray>()
        val ops = ArrayDeque<Char>()

        fun combine(a: IntArray, b: IntArray, op: Char): IntArray {
            var cost0: Int
            var cost1: Int

            if (op == '&') {
                // keep '&'
                cost0 = minOf(
                    a[0] + minOf(b[0], b[1]),
                    b[0] + minOf(a[0], a[1])
                )
                cost1 = a[1] + b[1]
            } else { // '|'
                // keep '|'
                cost0 = a[0] + b[0]
                cost1 = minOf(
                    a[1] + minOf(b[0], b[1]),
                    b[1] + minOf(a[0], a[1])
                )
            }

            // flip operator
            val flippedOp = if (op == '&') '|' else '&'
            var cost0Flip: Int
            var cost1Flip: Int
            if (flippedOp == '&') {
                cost0Flip = minOf(
                    a[0] + minOf(b[0], b[1]),
                    b[0] + minOf(a[0], a[1])
                )
                cost1Flip = a[1] + b[1]
            } else { // '|'
                cost0Flip = a[0] + b[0]
                cost1Flip = minOf(
                    a[1] + minOf(b[0], b[1]),
                    b[1] + minOf(a[0], a[1])
                )
            }
            cost0 = minOf(cost0, cost0Flip + 1)
            cost1 = minOf(cost1, cost1Flip + 1)

            return intArrayOf(cost0, cost1)
        }

        fun applyOp() {
            val op = ops.pop()
            val right = values.pop()
            val left = values.pop()
            values.push(combine(left, right, op))
        }

        var i = 0
        while (i < expression.length) {
            when (val c = expression[i]) {
                '0', '1' -> {
                    if (c == '0') {
                        values.push(intArrayOf(0, 1))
                    } else {
                        values.push(intArrayOf(1, 0))
                    }
                }
                '(' -> ops.push(c)
                '&', '|' -> {
                    while (!ops.isEmpty() && ops.peek() != '(') {
                        applyOp()
                    }
                    ops.push(c)
                }
                ')' -> {
                    while (ops.peek() != '(') {
                        applyOp()
                    }
                    ops.pop() // remove '('
                }
            }
            i++
        }

        while (!ops.isEmpty()) {
            applyOp()
        }

        val result = values.pop()
        return if (result[0] == 0) result[1] else result[0]
    }
}
```

## Dart

```dart
class Solution {
  int minOperationsToFlip(String expression) {
    List<List<int>> valStack = [];
    List<String> opStack = [];

    for (int i = 0; i < expression.length; i++) {
      String ch = expression[i];
      if (ch == '0' || ch == '1') {
        int cost0 = ch == '0' ? 0 : 1;
        int cost1 = ch == '1' ? 0 : 1;
        valStack.add([cost0, cost1]);
        while (opStack.isNotEmpty && opStack.last != '(') {
          _apply(valStack, opStack);
        }
      } else if (ch == '&' || ch == '|') {
        opStack.add(ch);
      } else if (ch == '(') {
        opStack.add(ch);
      } else if (ch == ')') {
        while (opStack.isNotEmpty && opStack.last != '(') {
          _apply(valStack, opStack);
        }
        if (opStack.isNotEmpty && opStack.last == '(') {
          opStack.removeLast();
        }
        while (opStack.isNotEmpty && opStack.last != '(') {
          _apply(valStack, opStack);
        }
      }
    }

    while (opStack.isNotEmpty) {
      _apply(valStack, opStack);
    }

    List<int> finalCost = valStack.last;
    return finalCost[0] == 0 ? finalCost[1] : finalCost[0];
  }

  void _apply(List<List<int>> valStack, List<String> opStack) {
    String op = opStack.removeLast();
    List<int> right = valStack.removeLast();
    List<int> left = valStack.removeLast();
    valStack.add(_combine(op, left, right));
  }

  List<int> _combine(String op, List<int> left, List<int> right) {
    int l0 = left[0], l1 = left[1];
    int r0 = right[0], r1 = right[1];

    // keep operator
    int keep0, keep1;
    if (op == '&') {
      keep1 = l1 + r1;
      keep0 = _min3(l0 + r0, l0 + r1, l1 + r0);
    } else { // '|'
      keep0 = l0 + r0;
      keep1 = _min3(l1 + r1, l1 + r0, l0 + r1);
    }

    // flipped operator
    String flipped = op == '&' ? '|' : '&';
    int flip0, flip1;
    if (flipped == '&') {
      flip1 = l1 + r1;
      flip0 = _min3(l0 + r0, l0 + r1, l1 + r0);
    } else { // '|'
      flip0 = l0 + r0;
      flip1 = _min3(l1 + r1, l1 + r0, l0 + r1);
    }

    int final0 = keep0 < (flip0 + 1) ? keep0 : (flip0 + 1);
    int final1 = keep1 < (flip1 + 1) ? keep1 : (flip1 + 1);

    return [final0, final1];
  }

  int _min3(int a, int b, int c) {
    int m = a < b ? a : b;
    return m < c ? m : c;
  }
}
```

## Golang

```go
func minOperationsToFlip(expression string) int {
	type node struct {
		zero, one int
	}
	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}
	combine := func(a, b node, op byte) node {
		if op == '&' {
			zero := min(a.zero+min(b.zero, b.one), b.zero+min(a.zero, a.one))
			one := a.one + b.one
			return node{zero, one}
		}
		// op == '|'
		zero := a.zero + b.zero
		one := min(a.one+min(b.zero, b.one), b.one+min(a.zero, a.one))
		return node{zero, one}
	}

	vals := []node{}
	ops := []byte{}

	for i := 0; i < len(expression); i++ {
		c := expression[i]
		switch c {
		case '0':
			vals = append(vals, node{0, 1})
		case '1':
			vals = append(vals, node{1, 0})
		case '&', '|':
			ops = append(ops, c)
		case '(':
			ops = append(ops, c)
		case ')':
			for len(ops) > 0 && ops[len(ops)-1] != '(' {
				op := ops[len(ops)-1]
				ops = ops[:len(ops)-1]

				b := vals[len(vals)-1]
				vals = vals[:len(vals)-1]
				a := vals[len(vals)-1]
				vals = vals[:len(vals)-1]

				vals = append(vals, combine(a, b, op))
			}
			if len(ops) > 0 && ops[len(ops)-1] == '(' {
				ops = ops[:len(ops)-1]
			}
		}
	}

	for len(ops) > 0 {
		op := ops[len(ops)-1]
		ops = ops[:len(ops)-1]

		b := vals[len(vals)-1]
		vals = vals[:len(vals)-1]
		a := vals[len(vals)-1]
		vals = vals[:len(vals)-1]

		vals = append(vals, combine(a, b, op))
	}

	res := vals[0]
	if res.zero == 0 {
		return res.one
	}
	return res.zero
}
```

## Ruby

```ruby
def min_operations_to_flip(expression)
  val_stack = []
  op_stack = []

  combine = lambda do |left, right, op|
    l0, l1 = left
    r0, r1 = right
    if op == '&'
      zero = [l0 + [r0, r1].min, r0 + [l0, l1].min].min
      one  = l1 + r1
    else # '|'
      zero = l0 + r0
      one  = [l1 + [r0, r1].min, r1 + [l0, l1].min].min
    end
    [zero, one]
  end

  apply_top = lambda do
    op = op_stack.pop
    right = val_stack.pop
    left = val_stack.pop
    val_stack << combine.call(left, right, op)
  end

  expression.each_char do |ch|
    case ch
    when '0'
      val_stack << [0, 1]
    when '1'
      val_stack << [1, 0]
    when '('
      op_stack << ch
    when ')'
      while op_stack[-1] != '('
        apply_top.call
      end
      op_stack.pop # remove '('
    when '&', '|'
      while !op_stack.empty? && op_stack[-1] != '('
        apply_top.call
      end
      op_stack << ch
    end
  end

  while !op_stack.empty?
    apply_top.call
  end

  cost0, cost1 = val_stack.pop
  cost0.zero? ? cost1 : cost0
end
```

## Scala

```scala
import scala.collection.mutable.ArrayDeque

object Solution {
  def minOperationsToFlip(expression: String): Int = {
    val vals = new ArrayDeque[(Int, Int)]()
    val ops = new ArrayDeque[Char]()

    def combine(l: (Int, Int), r: (Int, Int), op: Char): (Int, Int) = {
      val (l0, l1) = l
      val (r0, r1) = r
      var res0 = Int.MaxValue
      var res1 = Int.MaxValue
      if (op == '&') {
        // keep '&'
        val keep0 = math.min(l0 + math.min(r0, r1), r0 + math.min(l0, l1))
        val keep1 = l1 + r1
        // flip to '|'
        val flip0 = l0 + r0 + 1
        val flip1 = math.min(l1 + math.min(r0, r1), r1 + math.min(l0, l1)) + 1
        res0 = math.min(keep0, flip0)
        res1 = math.min(keep1, flip1)
      } else { // '|'
        // keep '|'
        val keep0 = l0 + r0
        val keep1 = math.min(l1 + math.min(r0, r1), r1 + math.min(l0, l1))
        // flip to '&'
        val flip0 = math.min(l0 + math.min(r0, r1), r0 + math.min(l0, l1)) + 1
        val flip1 = l1 + r1 + 1
        res0 = math.min(keep0, flip0)
        res1 = math.min(keep1, flip1)
      }
      (res0, res1)
    }

    def applyPending(): Unit = {
      while (ops.nonEmpty && ops.last != '(') {
        val op = ops.removeLast()
        val right = vals.removeLast()
        val left = vals.removeLast()
        vals.append(combine(left, right, op))
      }
    }

    for (ch <- expression) {
      ch match {
        case '0' => vals.append((0, 1))
        case '1' => vals.append((1, 0))
        case '(' => ops.append('(')
        case '&' | '|' =>
          applyPending()
          ops.append(ch)
        case ')' =>
          applyPending()
          if (ops.nonEmpty && ops.last == '(') ops.removeLast()
      }
    }

    applyPending()

    val (cost0, cost1) = vals.last
    if (cost0 == 0) cost1 else cost0
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations_to_flip(expression: String) -> i32 {
        fn combine(l: (i32, i32), r: (i32, i32), op: char) -> (i32, i32) {
            let (l0, l1) = l;
            let (r0, r1) = r;

            // cost when keeping the operator
            let (keep0, keep1) = match op {
                '&' => {
                    let cost1 = l1 + r1;
                    let cost0 = std::cmp::min(l0 + r0,
                                 std::cmp::min(l0 + r1, l1 + r0));
                    (cost0, cost1)
                }
                '|' => {
                    let cost0 = l0 + r0;
                    let cost1 = std::cmp::min(l1 + r1,
                                 std::cmp::min(l1 + r0, l0 + r1));
                    (cost0, cost1)
                }
                _ => unreachable!(),
            };

            // cost when flipping the operator (extra 1 operation)
            let flipped_op = if op == '&' { '|' } else { '&' };
            let (flip0, flip1) = match flipped_op {
                '&' => {
                    let cost1 = l1 + r1;
                    let cost0 = std::cmp::min(l0 + r0,
                                 std::cmp::min(l0 + r1, l1 + r0));
                    (cost0, cost1)
                }
                '|' => {
                    let cost0 = l0 + r0;
                    let cost1 = std::cmp::min(l1 + r1,
                                 std::cmp::min(l1 + r0, l0 + r1));
                    (cost0, cost1)
                }
                _ => unreachable!(),
            };

            let final0 = std::cmp::min(keep0, flip0 + 1);
            let final1 = std::cmp::min(keep1, flip1 + 1);
            (final0, final1)
        }

        fn apply(vals: &mut Vec<(i32, i32)>, ops: &mut Vec<char>) {
            let right = vals.pop().unwrap();
            let left = vals.pop().unwrap();
            let op = ops.pop().unwrap();
            vals.push(combine(left, right, op));
        }

        let mut vals: Vec<(i32, i32)> = Vec::new(); // (cost to 0, cost to 1)
        let mut ops: Vec<char> = Vec::new();

        for ch in expression.chars() {
            match ch {
                '0' => vals.push((0, 1)),
                '1' => vals.push((1, 0)),
                '(' => ops.push('('),
                ')' => {
                    while *ops.last().unwrap() != '(' {
                        apply(&mut vals, &mut ops);
                    }
                    ops.pop(); // remove '('
                }
                '&' | '|' => {
                    while let Some(&top) = ops.last() {
                        if top == '(' {
                            break;
                        }
                        apply(&mut vals, &mut ops);
                    }
                    ops.push(ch);
                }
                _ => {}
            }
        }

        while !ops.is_empty() {
            apply(&mut vals, &mut ops);
        }

        let (c0, c1) = vals.pop().unwrap();
        if c0 == 0 { c1 } else { c0 }
    }
}
```

## Racket

```racket
(define/contract (min-operations-to-flip expression)
  (-> string? exact-integer?)
  (let* ((n (string-length expression))
         ;; leaf costs
         (leaf
          (lambda (ch)
            (if (char=? ch #\0) (list 0 1) (list 1 0))))
         ;; cost for a given operator without flipping it
         (op-costs
          (lambda (op left right)
            (let* ((l0 (first left)) (l1 (second left))
                   (r0 (first right)) (r1 (second right)))
              (if (char=? op #\&)
                  (list (min (+ l0 (min r0 r1))
                             (+ r0 (min l0 l1)))
                        (+ l1 r1))
                  (list (+ l0 r0)
                        (min (+ l1 (min r0 r1))
                             (+ r1 (min l0 l1))))))))
         ;; combine two sub‑expressions with possible operator flip
         (combine
          (lambda (left right op)
            (let* ((keep (op-costs op left right))
                   (flip-op (if (char=? op #\&) #\| #\&))
                   (flip (op-costs flip-op left right)))
              (list (min (first keep) (+ 1 (first flip)))
                    (min (second keep) (+ 1 (second flip))))))))
    ;; stacks
    (let ((vals '())
          (ops '()))
      (define (push-val v) (set! vals (cons v vals)))
      (define (pop-val)
        (let ((v (car vals))) (set! vals (cdr vals)) v))
      (define (push-op o) (set! ops (cons o ops)))
      (define (pop-op)
        (let ((o (car ops))) (set! ops (cdr ops)) o))
      (define (apply-op)
        (let* ((op (pop-op))
               (right (pop-val))
               (left (pop-val))
               (combined (combine left right op)))
          (push-val combined)))
      ;; main scan
      (let loop ((i 0))
        (when (< i n)
          (let ((c (string-ref expression i)))
            (cond [(or (char=? c #\0) (char=? c #\1))
                   (push-val (leaf c))]
                  [(char=? c #\()
                   (push-op c)]
                  [(or (char=? c #\&) (char=? c #\|))
                   ;; apply previous operators of equal precedence
                   (let recur ()
                     (when (and (pair? ops) (not (eq? (car ops) '(')))
                       (apply-op)
                       (recur)))
                   (push-op c)]
                  [(char=? c #\))
                   (let recur ()
                     (when (and (pair? ops) (not (eq? (car ops) '(')))
                       (apply-op)
                       (recur)))
                   ;; discard the matching '('
                   (set! ops (cdr ops))]))
          (loop (+ i 1))))
      ;; apply remaining operators
      (let recur ()
        (when (pair? ops)
          (apply-op)
          (recur)))
      (let ((result (car vals))
            (cost0 (first result))
            (cost1 (second result)))
        (if (= cost0 0) cost1 cost0)))))
```

## Erlang

```erlang
-module(solution).
-export([min_operations_to_flip/1]).

-spec min_operations_to_flip(Expression :: unicode:unicode_binary()) -> integer().
min_operations_to_flip(Expression) ->
    Chars = unicode:characters_to_list(Expression),
    {ZeroCost, OneCost} = parse(Chars, [], []),
    case ZeroCost of
        0 -> OneCost;
        _ -> ZeroCost
    end.

%% Parsing the expression using two stacks: Ops and Values.
parse([], Ops, Values) ->
    finalize(Ops, Values);
parse([C | Rest], Ops, Values) when C == $0; C == $1 ->
    Pair = case C of
               $0 -> {0, 1};
               $1 -> {1, 0}
           end,
    parse(Rest, Ops, [Pair | Values]);
parse([C | Rest], Ops, Values) when C == $&; C == $| ->
    {NewOps, NewVals} = apply_until_paren(Ops, Values),
    parse(Rest, [C | NewOps], NewVals);
parse([$ ( | Rest], Ops, Values) ->
    parse(Rest, [$ ( | Ops], Values);
parse([$) | Rest], Ops, Values) ->
    {OpsAfterParen, ValsAfter} = apply_until_left_paren(Ops, Values),
    parse(Rest, OpsAfterParen, ValsAfter).

%% Apply remaining operators after full traversal.
finalize([], [Result]) -> Result;
finalize(Ops, Values) ->
    {NewOps, NewVals} = apply_top_op(Ops, Values),
    finalize(NewOps, NewVals).

%% Apply operators until encountering '(' or stack empty.
apply_until_paren([$( | _] = Ops, Values) -> {Ops, Values};
apply_until_paren([], Values) -> {[], Values};
apply_until_paren(Ops, Values) ->
    case hd(Ops) of
        $( -> {Ops, Values};
        _Op ->
            {NewOps, NewVals} = apply_top_op(Ops, Values),
            apply_until_paren(NewOps, NewVals)
    end.

%% Apply operators until '(' is removed (used when encountering ')').
apply_until_left_paren([$( | RestOps], Values) -> {RestOps, Values};
apply_until_left_paren([], _) -> erlang:error(bad_expression);
apply_until_left_paren(Ops, Values) ->
    {NewOps, NewVals} = apply_top_op(Ops, Values),
    apply_until_left_paren(NewOps, NewVals).

%% Apply the top operator on the two most recent values.
apply_top_op([Op | RestOps], [Right, Left | RestVals]) ->
    NewPair = apply_op(Op, Left, Right),
    {RestOps, [NewPair | RestVals]}.

%% Compute DP costs for a node given its operator and children's costs.
apply_op($&, {L0, L1}, {R0, R1}) ->
    Keep0 = min3(L0 + R0, L0 + R1, L1 + R0),
    Keep1 = L1 + R1,
    Flip0 = L0 + R0,
    Flip1 = min3(L1 + R1, L0 + R1, L1 + R0),
    Cost0 = erlang:min(Keep0, 1 + Flip0),
    Cost1 = erlang:min(Keep1, 1 + Flip1),
    {Cost0, Cost1};
apply_op($|, {L0, L1}, {R0, R1}) ->
    Keep0 = L0 + R0,
    Keep1 = min3(L1 + R1, L0 + R1, L1 + R0),
    Flip0 = min3(L0 + R0, L0 + R1, L1 + R0),
    Flip1 = L1 + R1,
    Cost0 = erlang:min(Keep0, 1 + Flip0),
    Cost1 = erlang:min(Keep1, 1 + Flip1),
    {Cost0, Cost1}.

%% Helper to compute minimum of three integers.
min3(A, B, C) ->
    MinAB = if A < B -> A; true -> B end,
    if MinAB < C -> MinAB; true -> C end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations_to_flip(expression :: String.t) :: integer
  def min_operations_to_flip(expression) do
    chars = :binary.bin_to_list(expression)

    {val_stack, op_stack} =
      Enum.reduce(chars, {[], []}, fn ch, {vs, os} ->
        cond do
          ch == ?0 or ch == ?1 ->
            pair = if ch == ?0, do: {0, 1}, else: {1, 0}
            {[pair | vs], os}

          ch == ?( ->
            {vs, [? ( | os]}

          ch == ?) ->
            {new_vs, new_os} = apply_until(vs, os, fn op -> op != ?( end)
            # pop '('
            [_paren | rest_os] = new_os
            {new_vs, rest_os}

          ch == ?& or ch == ?| ->
            {vs2, os2} = apply_until(vs, os, fn op -> op != ?( end)
            {vs2, [ch | os2]}
        end
      end)

    {final_vs, _} = apply_until(val_stack, op_stack, fn _ -> true end)
    [{c0, c1}] = final_vs

    if c0 == 0 do
      c1
    else
      c0
    end
  end

  defp apply_until(vs, [], _cond), do: {vs, []}

  defp apply_until(vs, [op | rest] = os, cond_fun) do
    if cond_fun.(op) do
      vs1 = apply_op(vs, op)
      apply_until(vs1, rest, cond_fun)
    else
      {vs, os}
    end
  end

  defp apply_op([right, left | rest], op) do
    {new0, new1} = combine(left, right, op)
    [{new0, new1} | rest]
  end

  defp combine({l0, l1}, {r0, r1}, ?&) do
    orig0 = min(l0 + r0, min(l0 + r1, l1 + r0))
    orig1 = l1 + r1
    flip0 = 1 + (l0 + r0)
    flip1 = 1 + min(l1 + r1, min(l1 + r0, l0 + r1))
    {min(orig0, flip0), min(orig1, flip1)}
  end

  defp combine({l0, l1}, {r0, r1}, ?|) do
    orig1 = min(l1 + r1, min(l1 + r0, l0 + r1))
    orig0 = l0 + r0
    flip1 = 1 + (l1 + r1)
    flip0 = 1 + min(l0 + r0, min(l0 + r1, l1 + r0))
    {min(orig0, flip0), min(orig1, flip1)}
  end
end
```
