# 3102. Minimize Manhattan Distances

## Cpp

```cpp
class Solution {
public:
    int minimumDistance(vector<vector<int>>& points) {
        int n = points.size();
        vector<long long> u(n), v(n);
        for (int i = 0; i < n; ++i) {
            long long x = points[i][0];
            long long y = points[i][1];
            u[i] = x - y;
            v[i] = x + y;
        }
        const long long INF = (1LL<<60);
        long long maxU = -INF, minU = INF, secMaxU = -INF, secMinU = INF;
        long long maxV = -INF, minV = INF, secMaxV = -INF, secMinV = INF;
        int cntMaxU = 0, cntMinU = 0, cntMaxV = 0, cntMinV = 0;
        // first pass: find extremes and their counts
        for (int i = 0; i < n; ++i) {
            if (u[i] > maxU) { maxU = u[i]; cntMaxU = 1; }
            else if (u[i] == maxU) cntMaxU++;
            if (u[i] < minU) { minU = u[i]; cntMinU = 1; }
            else if (u[i] == minU) cntMinU++;

            if (v[i] > maxV) { maxV = v[i]; cntMaxV = 1; }
            else if (v[i] == maxV) cntMaxV++;
            if (v[i] < minV) { minV = v[i]; cntMinV = 1; }
            else if (v[i] == minV) cntMinV++;
        }
        // second pass: find secondary extremes
        for (int i = 0; i < n; ++i) {
            if (u[i] != maxU && u[i] > secMaxU) secMaxU = u[i];
            if (u[i] != minU && u[i] < secMinU) secMinU = u[i];

            if (v[i] != maxV && v[i] > secMaxV) secMaxV = v[i];
            if (v[i] != minV && v[i] < secMinV) secMinV = v[i];
        }
        // handle case where no secondary extreme exists
        if (secMaxU == -INF) secMaxU = maxU;
        if (secMinU == INF)  secMinU = minU;
        if (secMaxV == -INF) secMaxV = maxV;
        if (secMinV == INF)  secMinV = minV;

        long long answer = INF;
        for (int i = 0; i < n; ++i) {
            long long curMaxU = (u[i] == maxU && cntMaxU == 1) ? secMaxU : maxU;
            long long curMinU = (u[i] == minU && cntMinU == 1) ? secMinU : minU;
            long long curMaxV = (v[i] == maxV && cntMaxV == 1) ? secMaxV : maxV;
            long long curMinV = (v[i] == minV && cntMinV == 1) ? secMinV : minV;

            long long rangeU = curMaxU - curMinU;
            long long rangeV = curMaxV - curMinV;
            long long curDist = max(rangeU, rangeV);
            if (curDist < answer) answer = curDist;
        }
        return (int)answer;
    }
};
```

## Java

```java
class Solution {
    public int minimumDistance(int[][] points) {
        int n = points.length;
        long[] u = new long[n];
        long[] v = new long[n];
        for (int i = 0; i < n; i++) {
            long x = points[i][0];
            long y = points[i][1];
            u[i] = x - y;
            v[i] = x + y;
        }

        // extremes for u
        long maxU = Long.MIN_VALUE, secondMaxU = Long.MIN_VALUE;
        int cntMaxU = 0;
        long minU = Long.MAX_VALUE, secondMinU = Long.MAX_VALUE;
        int cntMinU = 0;

        // extremes for v
        long maxV = Long.MIN_VALUE, secondMaxV = Long.MIN_VALUE;
        int cntMaxV = 0;
        long minV = Long.MAX_VALUE, secondMinV = Long.MAX_VALUE;
        int cntMinV = 0;

        for (int i = 0; i < n; i++) {
            long valU = u[i];
            if (valU > maxU) {
                secondMaxU = maxU;
                maxU = valU;
                cntMaxU = 1;
            } else if (valU == maxU) {
                cntMaxU++;
            } else if (valU > secondMaxU) {
                secondMaxU = valU;
            }

            if (valU < minU) {
                secondMinU = minU;
                minU = valU;
                cntMinU = 1;
            } else if (valU == minU) {
                cntMinU++;
            } else if (valU < secondMinU) {
                secondMinU = valU;
            }

            long valV = v[i];
            if (valV > maxV) {
                secondMaxV = maxV;
                maxV = valV;
                cntMaxV = 1;
            } else if (valV == maxV) {
                cntMaxV++;
            } else if (valV > secondMaxV) {
                secondMaxV = valV;
            }

            if (valV < minV) {
                secondMinV = minV;
                minV = valV;
                cntMinV = 1;
            } else if (valV == minV) {
                cntMinV++;
            } else if (valV < secondMinV) {
                secondMinV = valV;
            }
        }

        long answer = Long.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            long curMaxU = (u[i] == maxU && cntMaxU == 1) ? secondMaxU : maxU;
            long curMinU = (u[i] == minU && cntMinU == 1) ? secondMinU : minU;

            long curMaxV = (v[i] == maxV && cntMaxV == 1) ? secondMaxV : maxV;
            long curMinV = (v[i] == minV && cntMinV == 1) ? secondMinV : minV;

            long rangeU = curMaxU - curMinU;
            long rangeV = curMaxV - curMinV;
            long curDist = Math.max(rangeU, rangeV);
            if (curDist < answer) {
                answer = curDist;
            }
        }

        return (int) answer;
    }
}
```

## Python

```python
class Solution(object):
    def minimumDistance(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        u = [0] * n
        v = [0] * n
        for i, (x, y) in enumerate(points):
            u[i] = x + y
            v[i] = x - y

        INF = 10**20

        # For u
        min1_u = INF
        min2_u = INF
        cnt_min1_u = 0
        max1_u = -INF
        max2_u = -INF
        cnt_max1_u = 0

        for val in u:
            if val < min1_u:
                min2_u = min1_u
                min1_u = val
                cnt_min1_u = 1
            elif val == min1_u:
                cnt_min1_u += 1
            elif val < min2_u:
                min2_u = val

            if val > max1_u:
                max2_u = max1_u
                max1_u = val
                cnt_max1_u = 1
            elif val == max1_u:
                cnt_max1_u += 1
            elif val > max2_u:
                max2_u = val

        # For v
        min1_v = INF
        min2_v = INF
        cnt_min1_v = 0
        max1_v = -INF
        max2_v = -INF
        cnt_max1_v = 0

        for val in v:
            if val < min1_v:
                min2_v = min1_v
                min1_v = val
                cnt_min1_v = 1
            elif val == min1_v:
                cnt_min1_v += 1
            elif val < min2_v:
                min2_v = val

            if val > max1_v:
                max2_v = max1_v
                max1_v = val
                cnt_max1_v = 1
            elif val == max1_v:
                cnt_max1_v += 1
            elif val > max2_v:
                max2_v = val

        ans = INF
        for i in range(n):
            cur_min_u = min1_u if not (u[i] == min1_u and cnt_min1_u == 1) else min2_u
            cur_max_u = max1_u if not (u[i] == max1_u and cnt_max1_u == 1) else max2_u
            cur_min_v = min1_v if not (v[i] == min1_v and cnt_min1_v == 1) else min2_v
            cur_max_v = max1_v if not (v[i] == max1_v and cnt_max1_v == 1) else max2_v

            range_u = cur_max_u - cur_min_u
            range_v = cur_max_v - cur_min_v
            candidate = range_u if range_u > range_v else range_v
            if candidate < ans:
                ans = candidate

        return int(ans)
```

## Python3

```python
from typing import List

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        n = len(points)
        u = [0] * n
        v = [0] * n
        for i, (x, y) in enumerate(points):
            u[i] = x + y
            v[i] = x - y

        INF_NEG = -10**20
        INF_POS = 10**20

        # max_u and second max
        max_u = INF_NEG
        cnt_max_u = 0
        sec_max_u = INF_NEG
        min_u = INF_POS
        cnt_min_u = 0
        sec_min_u = INF_POS

        max_v = INF_NEG
        cnt_max_v = 0
        sec_max_v = INF_NEG
        min_v = INF_POS
        cnt_min_v = 0
        sec_min_v = INF_POS

        for val in u:
            if val > max_u:
                sec_max_u = max_u
                max_u = val
                cnt_max_u = 1
            elif val == max_u:
                cnt_max_u += 1
            elif val > sec_max_u:
                sec_max_u = val

            if val < min_u:
                sec_min_u = min_u
                min_u = val
                cnt_min_u = 1
            elif val == min_u:
                cnt_min_u += 1
            elif val < sec_min_u:
                sec_min_u = val

        for val in v:
            if val > max_v:
                sec_max_v = max_v
                max_v = val
                cnt_max_v = 1
            elif val == max_v:
                cnt_max_v += 1
            elif val > sec_max_v:
                sec_max_v = val

            if val < min_v:
                sec_min_v = min_v
                min_v = val
                cnt_min_v = 1
            elif val == min_v:
                cnt_min_v += 1
            elif val < sec_min_v:
                sec_min_v = val

        answer = INF_POS
        for i in range(n):
            cur_max_u = max_u if not (u[i] == max_u and cnt_max_u == 1) else sec_max_u
            cur_min_u = min_u if not (u[i] == min_u and cnt_min_u == 1) else sec_min_u

            cur_max_v = max_v if not (v[i] == max_v and cnt_max_v == 1) else sec_max_v
            cur_min_v = min_v if not (v[i] == min_v and cnt_min_v == 1) else sec_min_v

            dist = max(cur_max_u - cur_min_u, cur_max_v - cur_min_v)
            if dist < answer:
                answer = dist

        return answer
```

## C

```c
#include <limits.h>
#include <stdlib.h>

int minimumDistance(int** points, int pointsSize, int* pointsColSize) {
    if (pointsSize <= 2) return 0;
    
    long long *p = (long long*)malloc(sizeof(long long) * pointsSize);
    long long *q = (long long*)malloc(sizeof(long long) * pointsSize);
    
    // extremes for p
    long long max1_p = LLONG_MIN, max2_p = LLONG_MIN;
    int cnt_max1_p = 0;
    long long min1_p = LLONG_MAX, min2_p = LLONG_MAX;
    int cnt_min1_p = 0;
    
    // extremes for q
    long long max1_q = LLONG_MIN, max2_q = LLONG_MIN;
    int cnt_max1_q = 0;
    long long min1_q = LLONG_MAX, min2_q = LLONG_MAX;
    int cnt_min1_q = 0;
    
    for (int i = 0; i < pointsSize; ++i) {
        long long x = points[i][0];
        long long y = points[i][1];
        p[i] = x + y;
        q[i] = x - y;
        
        // update max/min for p
        if (p[i] > max1_p) {
            max2_p = max1_p;
            max1_p = p[i];
            cnt_max1_p = 1;
        } else if (p[i] == max1_p) {
            cnt_max1_p++;
        } else if (p[i] > max2_p) {
            max2_p = p[i];
        }
        
        if (p[i] < min1_p) {
            min2_p = min1_p;
            min1_p = p[i];
            cnt_min1_p = 1;
        } else if (p[i] == min1_p) {
            cnt_min1_p++;
        } else if (p[i] < min2_p) {
            min2_p = p[i];
        }
        
        // update max/min for q
        if (q[i] > max1_q) {
            max2_q = max1_q;
            max1_q = q[i];
            cnt_max1_q = 1;
        } else if (q[i] == max1_q) {
            cnt_max1_q++;
        } else if (q[i] > max2_q) {
            max2_q = q[i];
        }
        
        if (q[i] < min1_q) {
            min2_q = min1_q;
            min1_q = q[i];
            cnt_min1_q = 1;
        } else if (q[i] == min1_q) {
            cnt_min1_q++;
        } else if (q[i] < min2_q) {
            min2_q = q[i];
        }
    }
    
    long long answer = LLONG_MAX;
    
    for (int i = 0; i < pointsSize; ++i) {
        // remaining extremes for p
        long long cur_max_p, cur_min_p;
        if (p[i] == max1_p) {
            cur_max_p = (cnt_max1_p > 1) ? max1_p : max2_p;
        } else {
            cur_max_p = max1_p;
        }
        if (p[i] == min1_p) {
            cur_min_p = (cnt_min1_p > 1) ? min1_p : min2_p;
        } else {
            cur_min_p = min1_p;
        }
        long long range_p = cur_max_p - cur_min_p;
        
        // remaining extremes for q
        long long cur_max_q, cur_min_q;
        if (q[i] == max1_q) {
            cur_max_q = (cnt_max1_q > 1) ? max1_q : max2_q;
        } else {
            cur_max_q = max1_q;
        }
        if (q[i] == min1_q) {
            cur_min_q = (cnt_min1_q > 1) ? min1_q : min2_q;
        } else {
            cur_min_q = min1_q;
        }
        long long range_q = cur_max_q - cur_min_q;
        
        long long cand = range_p > range_q ? range_p : range_q;
        if (cand < answer) answer = cand;
    }
    
    free(p);
    free(q);
    return (int)answer;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MinimumDistance(int[][] points) {
        int n = points.Length;
        long[] u = new long[n];
        long[] v = new long[n];
        for (int i = 0; i < n; i++) {
            long x = points[i][0];
            long y = points[i][1];
            u[i] = x + y;
            v[i] = x - y;
        }

        // For u
        long maxU = long.MinValue, secondMaxU = long.MinValue;
        int cntMaxU = 0;
        long minU = long.MaxValue, secondMinU = long.MaxValue;
        int cntMinU = 0;

        // For v
        long maxV = long.MinValue, secondMaxV = long.MinValue;
        int cntMaxV = 0;
        long minV = long.MaxValue, secondMinV = long.MaxValue;
        int cntMinV = 0;

        for (int i = 0; i < n; i++) {
            // u
            if (u[i] > maxU) {
                secondMaxU = maxU;
                maxU = u[i];
                cntMaxU = 1;
            } else if (u[i] == maxU) {
                cntMaxU++;
            } else if (u[i] > secondMaxU) {
                secondMaxU = u[i];
            }

            if (u[i] < minU) {
                secondMinU = minU;
                minU = u[i];
                cntMinU = 1;
            } else if (u[i] == minU) {
                cntMinU++;
            } else if (u[i] < secondMinU) {
                secondMinU = u[i];
            }

            // v
            if (v[i] > maxV) {
                secondMaxV = maxV;
                maxV = v[i];
                cntMaxV = 1;
            } else if (v[i] == maxV) {
                cntMaxV++;
            } else if (v[i] > secondMaxV) {
                secondMaxV = v[i];
            }

            if (v[i] < minV) {
                secondMinV = minV;
                minV = v[i];
                cntMinV = 1;
            } else if (v[i] == minV) {
                cntMinV++;
            } else if (v[i] < secondMinV) {
                secondMinV = v[i];
            }
        }

        long answer = long.MaxValue;

        for (int i = 0; i < n; i++) {
            long curMaxU = (u[i] == maxU && cntMaxU == 1) ? secondMaxU : maxU;
            long curMinU = (u[i] == minU && cntMinU == 1) ? secondMinU : minU;

            long curMaxV = (v[i] == maxV && cntMaxV == 1) ? secondMaxV : maxV;
            long curMinV = (v[i] == minV && cntMinV == 1) ? secondMinV : minV;

            long rangeU = curMaxU - curMinU;
            long rangeV = curMaxV - curMinV;
            long curAns = Math.Max(rangeU, rangeV);
            if (curAns < answer) answer = curAns;
        }

        return (int)answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} points
 * @return {number}
 */
var minimumDistance = function(points) {
    const n = points.length;
    const u = new Array(n);
    const v = new Array(n);
    
    let maxU1 = -Infinity, maxU2 = -Infinity, cntMaxU1 = 0;
    let minU1 = Infinity,  minU2 = Infinity,  cntMinU1 = 0;
    let maxV1 = -Infinity, maxV2 = -Infinity, cntMaxV1 = 0;
    let minV1 = Infinity,  minV2 = Infinity,  cntMinV1 = 0;
    
    for (let i = 0; i < n; ++i) {
        const x = points[i][0];
        const y = points[i][1];
        const ui = x - y;
        const vi = x + y;
        u[i] = ui;
        v[i] = vi;
        
        // max U
        if (ui > maxU1) {
            maxU2 = maxU1;
            maxU1 = ui;
            cntMaxU1 = 1;
        } else if (ui === maxU1) {
            cntMaxU1++;
        } else if (ui > maxU2) {
            maxU2 = ui;
        }
        // min U
        if (ui < minU1) {
            minU2 = minU1;
            minU1 = ui;
            cntMinU1 = 1;
        } else if (ui === minU1) {
            cntMinU1++;
        } else if (ui < minU2) {
            minU2 = ui;
        }
        // max V
        if (vi > maxV1) {
            maxV2 = maxV1;
            maxV1 = vi;
            cntMaxV1 = 1;
        } else if (vi === maxV1) {
            cntMaxV1++;
        } else if (vi > maxV2) {
            maxV2 = vi;
        }
        // min V
        if (vi < minV1) {
            minV2 = minV1;
            minV1 = vi;
            cntMinV1 = 1;
        } else if (vi === minV1) {
            cntMinV1++;
        } else if (vi < minV2) {
            minV2 = vi;
        }
    }
    
    let answer = Infinity;
    for (let i = 0; i < n; ++i) {
        const curMaxU = (u[i] === maxU1 && cntMaxU1 === 1) ? maxU2 : maxU1;
        const curMinU = (u[i] === minU1 && cntMinU1 === 1) ? minU2 : minU1;
        const curMaxV = (v[i] === maxV1 && cntMaxV1 === 1) ? maxV2 : maxV1;
        const curMinV = (v[i] === minV1 && cntMinV1 === 1) ? minV2 : minV1;
        
        const distU = curMaxU - curMinU;
        const distV = curMaxV - curMinV;
        const d = Math.max(distU, distV);
        if (d < answer) answer = d;
    }
    
    return answer;
};
```

## Typescript

```typescript
function minimumDistance(points: number[][]): number {
    const n = points.length;
    const u = new Array<number>(n);
    const v = new Array<number>(n);
    for (let i = 0; i < n; i++) {
        const x = points[i][0];
        const y = points[i][1];
        u[i] = x - y;
        v[i] = x + y;
    }

    const preMaxU = new Array<number>(n);
    const preMinU = new Array<number>(n);
    const preMaxV = new Array<number>(n);
    const preMinV = new Array<number>(n);
    for (let i = 0; i < n; i++) {
        if (i === 0) {
            preMaxU[i] = u[i];
            preMinU[i] = u[i];
            preMaxV[i] = v[i];
            preMinV[i] = v[i];
        } else {
            preMaxU[i] = Math.max(preMaxU[i - 1], u[i]);
            preMinU[i] = Math.min(preMinU[i - 1], u[i]);
            preMaxV[i] = Math.max(preMaxV[i - 1], v[i]);
            preMinV[i] = Math.min(preMinV[i - 1], v[i]);
        }
    }

    const sufMaxU = new Array<number>(n);
    const sufMinU = new Array<number>(n);
    const sufMaxV = new Array<number>(n);
    const sufMinV = new Array<number>(n);
    for (let i = n - 1; i >= 0; i--) {
        if (i === n - 1) {
            sufMaxU[i] = u[i];
            sufMinU[i] = u[i];
            sufMaxV[i] = v[i];
            sufMinV[i] = v[i];
        } else {
            sufMaxU[i] = Math.max(sufMaxU[i + 1], u[i]);
            sufMinU[i] = Math.min(sufMinU[i + 1], u[i]);
            sufMaxV[i] = Math.max(sufMaxV[i + 1], v[i]);
            sufMinV[i] = Math.min(sufMinV[i + 1], v[i]);
        }
    }

    let ans = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < n; i++) {
        let maxU: number, minU: number, maxV: number, minV: number;
        if (i === 0) {
            maxU = sufMaxU[1];
            minU = sufMinU[1];
            maxV = sufMaxV[1];
            minV = sufMinV[1];
        } else if (i === n - 1) {
            maxU = preMaxU[n - 2];
            minU = preMinU[n - 2];
            maxV = preMaxV[n - 2];
            minV = preMinV[n - 2];
        } else {
            maxU = Math.max(preMaxU[i - 1], sufMaxU[i + 1]);
            minU = Math.min(preMinU[i - 1], sufMinU[i + 1]);
            maxV = Math.max(preMaxV[i - 1], sufMaxV[i + 1]);
            minV = Math.min(preMinV[i - 1], sufMinV[i + 1]);
        }
        const rangeU = maxU - minU;
        const rangeV = maxV - minV;
        const cur = Math.max(rangeU, rangeV);
        if (cur < ans) ans = cur;
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function minimumDistance($points) {
        $n = count($points);
        $u = [];
        $v = [];

        $minU = PHP_INT_MAX;
        $secondMinU = PHP_INT_MAX;
        $cntMinU = 0;

        $maxU = -PHP_INT_MAX - 1;
        $secondMaxU = -PHP_INT_MAX - 1;
        $cntMaxU = 0;

        $minV = PHP_INT_MAX;
        $secondMinV = PHP_INT_MAX;
        $cntMinV = 0;

        $maxV = -PHP_INT_MAX - 1;
        $secondMaxV = -PHP_INT_MAX - 1;
        $cntMaxV = 0;

        for ($i = 0; $i < $n; ++$i) {
            $x = $points[$i][0];
            $y = $points[$i][1];
            $ui = $x - $y;
            $vi = $x + $y;
            $u[] = $ui;
            $v[] = $vi;

            // minU, secondMinU, cntMinU
            if ($ui < $minU) {
                $secondMinU = $minU;
                $minU = $ui;
                $cntMinU = 1;
            } elseif ($ui == $minU) {
                $cntMinU++;
            } elseif ($ui < $secondMinU) {
                $secondMinU = $ui;
            }

            // maxU, secondMaxU, cntMaxU
            if ($ui > $maxU) {
                $secondMaxU = $maxU;
                $maxU = $ui;
                $cntMaxU = 1;
            } elseif ($ui == $maxU) {
                $cntMaxU++;
            } elseif ($ui > $secondMaxU) {
                $secondMaxU = $ui;
            }

            // minV, secondMinV, cntMinV
            if ($vi < $minV) {
                $secondMinV = $minV;
                $minV = $vi;
                $cntMinV = 1;
            } elseif ($vi == $minV) {
                $cntMinV++;
            } elseif ($vi < $secondMinV) {
                $secondMinV = $vi;
            }

            // maxV, secondMaxV, cntMaxV
            if ($vi > $maxV) {
                $secondMaxV = $maxV;
                $maxV = $vi;
                $cntMaxV = 1;
            } elseif ($vi == $maxV) {
                $cntMaxV++;
            } elseif ($vi > $secondMaxV) {
                $secondMaxV = $vi;
            }
        }

        $answer = PHP_INT_MAX;

        for ($i = 0; $i < $n; ++$i) {
            $curMinU = ($u[$i] == $minU && $cntMinU == 1) ? $secondMinU : $minU;
            $curMaxU = ($u[$i] == $maxU && $cntMaxU == 1) ? $secondMaxU : $maxU;

            $curMinV = ($v[$i] == $minV && $cntMinV == 1) ? $secondMinV : $minV;
            $curMaxV = ($v[$i] == $maxV && $cntMaxV == 1) ? $secondMaxV : $maxV;

            $distU = $curMaxU - $curMinU;
            $distV = $curMaxV - $curMinV;
            $candidate = $distU > $distV ? $distU : $distV;

            if ($candidate < $answer) {
                $answer = $candidate;
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func minimumDistance(_ points: [[Int]]) -> Int {
        let n = points.count
        var p = [Int](repeating: 0, count: n)
        var q = [Int](repeating: 0, count: n)

        var maxP = Int.min, secondMaxP = Int.min, cntMaxP = 0
        var minP = Int.max, secondMinP = Int.max, cntMinP = 0

        var maxQ = Int.min, secondMaxQ = Int.min, cntMaxQ = 0
        var minQ = Int.max, secondMinQ = Int.max, cntMinQ = 0

        for i in 0..<n {
            let x = points[i][0]
            let y = points[i][1]
            let pi = x + y
            let qi = x - y
            p[i] = pi
            q[i] = qi

            if pi > maxP {
                secondMaxP = maxP
                maxP = pi
                cntMaxP = 1
            } else if pi == maxP {
                cntMaxP += 1
            } else if pi > secondMaxP {
                secondMaxP = pi
            }

            if pi < minP {
                secondMinP = minP
                minP = pi
                cntMinP = 1
            } else if pi == minP {
                cntMinP += 1
            } else if pi < secondMinP {
                secondMinP = pi
            }

            if qi > maxQ {
                secondMaxQ = maxQ
                maxQ = qi
                cntMaxQ = 1
            } else if qi == maxQ {
                cntMaxQ += 1
            } else if qi > secondMaxQ {
                secondMaxQ = qi
            }

            if qi < minQ {
                secondMinQ = minQ
                minQ = qi
                cntMinQ = 1
            } else if qi == minQ {
                cntMinQ += 1
            } else if qi < secondMinQ {
                secondMinQ = qi
            }
        }

        var answer = Int.max

        for i in 0..<n {
            let curMaxP: Int = (p[i] == maxP && cntMaxP == 1) ? secondMaxP : maxP
            let curMinP: Int = (p[i] == minP && cntMinP == 1) ? secondMinP : minP
            let curMaxQ: Int = (q[i] == maxQ && cntMaxQ == 1) ? secondMaxQ : maxQ
            let curMinQ: Int = (q[i] == minQ && cntMinQ == 1) ? secondMinQ : minQ

            let rangeP = curMaxP - curMinP
            let rangeQ = curMaxQ - curMinQ
            let candidate = max(rangeP, rangeQ)
            if candidate < answer {
                answer = candidate
            }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumDistance(points: Array<IntArray>): Int {
        val n = points.size
        val u = LongArray(n)
        val v = LongArray(n)

        var maxU = Long.MIN_VALUE
        var minU = Long.MAX_VALUE
        var maxV = Long.MIN_VALUE
        var minV = Long.MAX_VALUE

        var cntMaxU = 0
        var cntMinU = 0
        var cntMaxV = 0
        var cntMinV = 0

        for (i in 0 until n) {
            val x = points[i][0].toLong()
            val y = points[i][1].toLong()
            u[i] = x - y
            v[i] = x + y

            when {
                u[i] > maxU -> {
                    maxU = u[i]
                    cntMaxU = 1
                }
                u[i] == maxU -> cntMaxU++
            }
            when {
                u[i] < minU -> {
                    minU = u[i]
                    cntMinU = 1
                }
                u[i] == minU -> cntMinU++
            }

            when {
                v[i] > maxV -> {
                    maxV = v[i]
                    cntMaxV = 1
                }
                v[i] == maxV -> cntMaxV++
            }
            when {
                v[i] < minV -> {
                    minV = v[i]
                    cntMinV = 1
                }
                v[i] == minV -> cntMinV++
            }
        }

        var secMaxU = Long.MIN_VALUE
        var secMinU = Long.MAX_VALUE
        var secMaxV = Long.MIN_VALUE
        var secMinV = Long.MAX_VALUE

        for (i in 0 until n) {
            if (u[i] != maxU) secMaxU = kotlin.math.max(secMaxU, u[i])
            if (u[i] != minU) secMinU = kotlin.math.min(secMinU, u[i])
            if (v[i] != maxV) secMaxV = kotlin.math.max(secMaxV, v[i])
            if (v[i] != minV) secMinV = kotlin.math.min(secMinV, v[i])
        }

        var answer = Long.MAX_VALUE
        for (i in 0 until n) {
            var curMaxU = maxU
            var curMinU = minU
            var curMaxV = maxV
            var curMinV = minV

            if (u[i] == maxU && cntMaxU == 1) curMaxU = secMaxU
            if (u[i] == minU && cntMinU == 1) curMinU = secMinU
            if (v[i] == maxV && cntMaxV == 1) curMaxV = secMaxV
            if (v[i] == minV && cntMinV == 1) curMinV = secMinV

            val d = kotlin.math.max(curMaxU - curMinU, curMaxV - curMinV)
            answer = kotlin.math.min(answer, d)
        }

        return answer.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int minimumDistance(List<List<int>> points) {
    int n = points.length;
    List<int> u = List.filled(n, 0);
    List<int> v = List.filled(n, 0);

    const int INF = 1 << 60;

    int maxU = -INF, secondMaxU = -INF, cntMaxU = 0;
    int minU = INF, secondMinU = INF, cntMinU = 0;
    int maxV = -INF, secondMaxV = -INF, cntMaxV = 0;
    int minV = INF, secondMinV = INF, cntMinV = 0;

    for (int i = 0; i < n; ++i) {
      int x = points[i][0];
      int y = points[i][1];
      int ui = x - y;
      int vi = x + y;
      u[i] = ui;
      v[i] = vi;

      // maxU
      if (ui > maxU) {
        secondMaxU = maxU;
        maxU = ui;
        cntMaxU = 1;
      } else if (ui == maxU) {
        cntMaxU++;
      } else if (ui > secondMaxU) {
        secondMaxU = ui;
      }

      // minU
      if (ui < minU) {
        secondMinU = minU;
        minU = ui;
        cntMinU = 1;
      } else if (ui == minU) {
        cntMinU++;
      } else if (ui < secondMinU) {
        secondMinU = ui;
      }

      // maxV
      if (vi > maxV) {
        secondMaxV = maxV;
        maxV = vi;
        cntMaxV = 1;
      } else if (vi == maxV) {
        cntMaxV++;
      } else if (vi > secondMaxV) {
        secondMaxV = vi;
      }

      // minV
      if (vi < minV) {
        secondMinV = minV;
        minV = vi;
        cntMinV = 1;
      } else if (vi == minV) {
        cntMinV++;
      } else if (vi < secondMinV) {
        secondMinV = vi;
      }
    }

    int answer = INF;

    for (int i = 0; i < n; ++i) {
      int curMaxU = (u[i] == maxU && cntMaxU == 1) ? secondMaxU : maxU;
      int curMinU = (u[i] == minU && cntMinU == 1) ? secondMinU : minU;
      int curMaxV = (v[i] == maxV && cntMaxV == 1) ? secondMaxV : maxV;
      int curMinV = (v[i] == minV && cntMinV == 1) ? secondMinV : minV;

      int diffU = curMaxU - curMinU;
      int diffV = curMaxV - curMinV;
      int cur = diffU > diffV ? diffU : diffV;
      if (cur < answer) answer = cur;
    }

    return answer;
  }
}
```

## Golang

```go
func minimumDistance(points [][]int) int {
	n := len(points)
	u := make([]int, n)
	v := make([]int, n)

	maxInt := int(^uint(0) >> 1)
	minInt := -maxInt - 1

	// extremes for u
	maxU, secondMaxU, cntMaxU := minInt, minInt, 0
	minU, secondMinU, cntMinU := maxInt, maxInt, 0
	// extremes for v
	maxV, secondMaxV, cntMaxV := minInt, minInt, 0
	minV, secondMinV, cntMinV := maxInt, maxInt, 0

	for i, p := range points {
		x, y := p[0], p[1]
		ui := x - y
		vi := x + y
		u[i] = ui
		v[i] = vi

		// update for u
		if ui > maxU {
			secondMaxU = maxU
			maxU = ui
			cntMaxU = 1
		} else if ui == maxU {
			cntMaxU++
		} else if ui > secondMaxU {
			secondMaxU = ui
		}

		if ui < minU {
			secondMinU = minU
			minU = ui
			cntMinU = 1
		} else if ui == minU {
			cntMinU++
		} else if ui < secondMinU {
			secondMinU = ui
		}

		// update for v
		if vi > maxV {
			secondMaxV = maxV
			maxV = vi
			cntMaxV = 1
		} else if vi == maxV {
			cntMaxV++
		} else if vi > secondMaxV {
			secondMaxV = vi
		}

		if vi < minV {
			secondMinV = minV
			minV = vi
			cntMinV = 1
		} else if vi == minV {
			cntMinV++
		} else if vi < secondMinV {
			secondMinV = vi
		}
	}

	ans := maxInt
	for i := 0; i < n; i++ {
		curMaxU, curMinU := maxU, minU
		if u[i] == maxU && cntMaxU == 1 {
			curMaxU = secondMaxU
		}
		if u[i] == minU && cntMinU == 1 {
			curMinU = secondMinU
		}

		curMaxV, curMinV := maxV, minV
		if v[i] == maxV && cntMaxV == 1 {
			curMaxV = secondMaxV
		}
		if v[i] == minV && cntMinV == 1 {
			curMinV = secondMinV
		}

		diffU := curMaxU - curMinU
		diffV := curMaxV - curMinV
		curr := diffU
		if diffV > curr {
			curr = diffV
		}
		if curr < ans {
			ans = curr
		}
	}
	return ans
}
```

## Ruby

```ruby
def minimum_distance(points)
  n = points.length
  u = Array.new(n)
  v = Array.new(n)

  points.each_with_index do |p, i|
    x, y = p
    u[i] = x + y
    v[i] = x - y
  end

  neg_inf = -(1 << 60)
  pos_inf = 1 << 60

  max_u_val = neg_inf
  max_u_cnt = 0
  second_max_u = neg_inf

  min_u_val = pos_inf
  min_u_cnt = 0
  second_min_u = pos_inf

  max_v_val = neg_inf
  max_v_cnt = 0
  second_max_v = neg_inf

  min_v_val = pos_inf
  min_v_cnt = 0
  second_min_v = pos_inf

  n.times do |i|
    val = u[i]
    if val > max_u_val
      second_max_u = max_u_val
      max_u_val = val
      max_u_cnt = 1
    elsif val == max_u_val
      max_u_cnt += 1
    elsif val > second_max_u
      second_max_u = val
    end

    if val < min_u_val
      second_min_u = min_u_val
      min_u_val = val
      min_u_cnt = 1
    elsif val == min_u_val
      min_u_cnt += 1
    elsif val < second_min_u
      second_min_u = val
    end

    valv = v[i]
    if valv > max_v_val
      second_max_v = max_v_val
      max_v_val = valv
      max_v_cnt = 1
    elsif valv == max_v_val
      max_v_cnt += 1
    elsif valv > second_max_v
      second_max_v = valv
    end

    if valv < min_v_val
      second_min_v = min_v_val
      min_v_val = valv
      min_v_cnt = 1
    elsif valv == min_v_val
      min_v_cnt += 1
    elsif valv < second_min_v
      second_min_v = valv
    end
  end

  ans = pos_inf
  n.times do |i|
    cur_max_u = (u[i] == max_u_val && max_u_cnt == 1) ? second_max_u : max_u_val
    cur_min_u = (u[i] == min_u_val && min_u_cnt == 1) ? second_min_u : min_u_val
    cur_max_v = (v[i] == max_v_val && max_v_cnt == 1) ? second_max_v : max_v_val
    cur_min_v = (v[i] == min_v_val && min_v_cnt == 1) ? second_min_v : min_v_val

    cur = [cur_max_u - cur_min_u, cur_max_v - cur_min_v].max
    ans = cur if cur < ans
  end

  ans
end
```

## Scala

```scala
object Solution {
    def minimumDistance(points: Array[Array[Int]]): Int = {
        val n = points.length
        val u = new Array[Int](n)
        val v = new Array[Int](n)

        var maxU1 = Int.MinValue
        var cntMaxU1 = 0
        var maxU2 = Int.MinValue
        var minU1 = Int.MaxValue
        var cntMinU1 = 0
        var minU2 = Int.MaxValue

        var maxV1 = Int.MinValue
        var cntMaxV1 = 0
        var maxV2 = Int.MinValue
        var minV1 = Int.MaxValue
        var cntMinV1 = 0
        var minV2 = Int.MaxValue

        var i = 0
        while (i < n) {
            val x = points(i)(0)
            val y = points(i)(1)
            val ui = x - y
            val vi = x + y
            u(i) = ui
            v(i) = vi

            // maxU
            if (ui > maxU1) {
                maxU2 = maxU1
                maxU1 = ui
                cntMaxU1 = 1
            } else if (ui == maxU1) {
                cntMaxU1 += 1
            } else if (ui > maxU2) {
                maxU2 = ui
            }

            // minU
            if (ui < minU1) {
                minU2 = minU1
                minU1 = ui
                cntMinU1 = 1
            } else if (ui == minU1) {
                cntMinU1 += 1
            } else if (ui < minU2) {
                minU2 = ui
            }

            // maxV
            if (vi > maxV1) {
                maxV2 = maxV1
                maxV1 = vi
                cntMaxV1 = 1
            } else if (vi == maxV1) {
                cntMaxV1 += 1
            } else if (vi > maxV2) {
                maxV2 = vi
            }

            // minV
            if (vi < minV1) {
                minV2 = minV1
                minV1 = vi
                cntMinV1 = 1
            } else if (vi == minV1) {
                cntMinV1 += 1
            } else if (vi < minV2) {
                minV2 = vi
            }

            i += 1
        }

        if (maxU2 == Int.MinValue) maxU2 = maxU1
        if (minU2 == Int.MaxValue) minU2 = minU1
        if (maxV2 == Int.MinValue) maxV2 = maxV1
        if (minV2 == Int.MaxValue) minV2 = minV1

        var ans: Long = Long.MaxValue
        i = 0
        while (i < n) {
            val curMaxU = if (u(i) == maxU1 && cntMaxU1 == 1) maxU2 else maxU1
            val curMinU = if (u(i) == minU1 && cntMinU1 == 1) minU2 else minU1
            val curMaxV = if (v(i) == maxV1 && cntMaxV1 == 1) maxV2 else maxV1
            val curMinV = if (v(i) == minV1 && cntMinV1 == 1) minV2 else minV1

            val dU = curMaxU - curMinU
            val dV = curMaxV - curMinV
            val d = Math.max(dU, dV).toLong
            if (d < ans) ans = d
            i += 1
        }
        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_distance(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        let mut us = Vec::with_capacity(n);
        let mut vs = Vec::with_capacity(n);
        for p in &points {
            let x = p[0] as i64;
            let y = p[1] as i64;
            us.push(x - y);
            vs.push(x + y);
        }

        fn extremes(arr: &[i64]) -> (i64, usize, i64, i64, usize, i64) {
            // (max1, cnt_max1, max2, min1, cnt_min1, min2)
            let mut max1 = i64::MIN;
            let mut max2 = i64::MIN;
            let mut cnt_max1: usize = 0;
            let mut min1 = i64::MAX;
            let mut min2 = i64::MAX;
            let mut cnt_min1: usize = 0;

            for &v in arr.iter() {
                if v > max1 {
                    max2 = max1;
                    max1 = v;
                    cnt_max1 = 1;
                } else if v == max1 {
                    cnt_max1 += 1;
                } else if v > max2 {
                    max2 = v;
                }

                if v < min1 {
                    min2 = min1;
                    min1 = v;
                    cnt_min1 = 1;
                } else if v == min1 {
                    cnt_min1 += 1;
                } else if v < min2 {
                    min2 = v;
                }
            }
            (max1, cnt_max1, max2, min1, cnt_min1, min2)
        }

        let (max_u, cnt_max_u, second_max_u, min_u, cnt_min_u, second_min_u) = extremes(&us);
        let (max_v, cnt_max_v, second_max_v, min_v, cnt_min_v, second_min_v) = extremes(&vs);

        let mut answer = i64::MAX;
        for i in 0..n {
            let u = us[i];
            let v = vs[i];

            let cur_max_u = if u == max_u && cnt_max_u == 1 { second_max_u } else { max_u };
            let cur_min_u = if u == min_u && cnt_min_u == 1 { second_min_u } else { min_u };

            let cur_max_v = if v == max_v && cnt_max_v == 1 { second_max_v } else { max_v };
            let cur_min_v = if v == min_v && cnt_min_v == 1 { second_min_v } else { min_v };

            let diff_u = cur_max_u - cur_min_u;
            let diff_v = cur_max_v - cur_min_v;
            let d = if diff_u > diff_v { diff_u } else { diff_v };
            if d < answer {
                answer = d;
            }
        }

        answer as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-distance points)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((n (length points))
         (us (make-vector n))
         (vs (make-vector n)))
    (define INF 1152921504606846976) ; large enough integer
    (define min_u INF)
    (define cnt_min_u 0)
    (define second_min_u INF)
    (define max_u (- INF))
    (define cnt_max_u 0)
    (define second_max_u (- INF))
    (define min_v INF)
    (define cnt_min_v 0)
    (define second_min_v INF)
    (define max_v (- INF))
    (define cnt_max_v 0)
    (define second_max_v (- INF))
    (for ([p points] [i (in-naturals)])
      (let* ((x (first p))
             (y (second p))
             (u (- x y))
             (v (+ x y)))
        (vector-set! us i u)
        (vector-set! vs i v)
        ;; update min_u
        (cond [(< u min_u) (begin
                             (set! second_min_u min_u)
                             (set! min_u u)
                             (set! cnt_min_u 1))]
              [(= u min_u) (set! cnt_min_u (+ cnt_min_u 1))]
              [(< u second_min_u) (set! second_min_u u)])
        ;; update max_u
        (cond [(> u max_u) (begin
                             (set! second_max_u max_u)
                             (set! max_u u)
                             (set! cnt_max_u 1))]
              [(= u max_u) (set! cnt_max_u (+ cnt_max_u 1))]
              [(> u second_max_u) (set! second_max_u u)])
        ;; update min_v
        (cond [(< v min_v) (begin
                             (set! second_min_v min_v)
                             (set! min_v v)
                             (set! cnt_min_v 1))]
              [(= v min_v) (set! cnt_min_v (+ cnt_min_v 1))]
              [(< v second_min_v) (set! second_min_v v)])
        ;; update max_v
        (cond [(> v max_v) (begin
                             (set! second_max_v max_v)
                             (set! max_v v)
                             (set! cnt_max_v 1))]
              [(= v max_v) (set! cnt_max_v (+ cnt_max_v 1))]
              [(> v second_max_v) (set! second_max_v v)])))
    ;; compute answer
    (define best INF)
    (for ([i (in-range n)])
      (let* ((u (vector-ref us i))
             (v (vector-ref vs i))
             (range_u (cond [(and (= u min_u) (= cnt_min_u 1)) (- max_u second_min_u)]
                           [(and (= u max_u) (= cnt_max_u 1)) (- second_max_u min_u)]
                           [else (- max_u min_u)]))
             (range_v (cond [(and (= v min_v) (= cnt_min_v 1)) (- max_v second_min_v)]
                           [(and (= v max_v) (= cnt_max_v 1)) (- second_max_v min_v)]
                           [else (- max_v min_v)]))
             (cand (max range_u range_v)))
        (when (< cand best)
          (set! best cand))))
    best))
```

## Erlang

```erlang
-module(solution).
-export([minimum_distance/1]).
-include_lib("stdlib/include/ms_transform.hrl").
-define(INF, 10000000000).

-spec minimum_distance(Points :: [[integer()]]) -> integer().
minimum_distance(Points) ->
    UVs = [ {X - Y, X + Y} || [X,Y] <- Points ],
    case UVs of
        [] -> 0;
        [{U0,V0}|Rest] ->
            MaxU = U0, CntMaxU = 1, SecondMaxU = -?INF,
            MinU = U0, CntMinU = 1, SecondMinU = ?INF,
            MaxV = V0, CntMaxV = 1, SecondMaxV = -?INF,
            MinV = V0, CntMinV = 1, SecondMinV = ?INF,
            {FinalMaxU, FinalCntMaxU, FinalSecondMaxU,
             FinalMinU, FinalCntMinU, FinalSecondMinU,
             FinalMaxV, FinalCntMaxV, FinalSecondMaxV,
             FinalMinV, FinalCntMinV, FinalSecondMinV} =
                scan_stats(Rest,
                           MaxU, CntMaxU, SecondMaxU,
                           MinU, CntMinU, SecondMinU,
                           MaxV, CntMaxV, SecondMaxV,
                           MinV, CntMinV, SecondMinV),
            compute_min(UVs,
                        FinalMaxU, FinalCntMaxU, FinalSecondMaxU,
                        FinalMinU, FinalCntMinU, FinalSecondMinU,
                        FinalMaxV, FinalCntMaxV, FinalSecondMaxV,
                        FinalMinV, FinalCntMinV, FinalSecondMinV)
    end.

scan_stats([], MaxU,CntMaxU,SecondMaxU,
               MinU,CntMinU,SecondMinU,
               MaxV,CntMaxV,SecondMaxV,
               MinV,CntMinV,SecondMinV) ->
    {MaxU, CntMaxU, SecondMaxU,
     MinU, CntMinU, SecondMinU,
     MaxV, CntMaxV, SecondMaxV,
     MinV, CntMinV, SecondMinV};

scan_stats([{U,V}|Rest],
           MaxU,CntMaxU,SecondMaxU,
           MinU,CntMinU,SecondMinU,
           MaxV,CntMaxV,SecondMaxV,
           MinV,CntMinV,SecondMinV) ->

    {NewMaxU, NewCntMaxU, NewSecondMaxU} =
        if U > MaxU ->
                {U, 1, MaxU};
            U == MaxU ->
                {MaxU, CntMaxU + 1, SecondMaxU};
            true ->
                if U > SecondMaxU ->
                        {MaxU, CntMaxU, U};
                    true ->
                        {MaxU, CntMaxU, SecondMaxU}
                end
        end,

    {NewMinU, NewCntMinU, NewSecondMinU} =
        if U < MinU ->
                {U, 1, MinU};
            U == MinU ->
                {MinU, CntMinU + 1, SecondMinU};
            true ->
                if U < SecondMinU ->
                        {MinU, CntMinU, U};
                    true ->
                        {MinU, CntMinU, SecondMinU}
                end
        end,

    {NewMaxV, NewCntMaxV, NewSecondMaxV} =
        if V > MaxV ->
                {V, 1, MaxV};
            V == MaxV ->
                {MaxV, CntMaxV + 1, SecondMaxV};
            true ->
                if V > SecondMaxV ->
                        {MaxV, CntMaxV, V};
                    true ->
                        {MaxV, CntMaxV, SecondMaxV}
                end
        end,

    {NewMinV, NewCntMinV, NewSecondMinV} =
        if V < MinV ->
                {V, 1, MinV};
            V == MinV ->
                {MinV, CntMinV + 1, SecondMinV};
            true ->
                if V < SecondMinV ->
                        {MinV, CntMinV, V};
                    true ->
                        {MinV, CntMinV, SecondMinV}
                end
        end,

    scan_stats(Rest,
               NewMaxU, NewCntMaxU, NewSecondMaxU,
               NewMinU, NewCntMinU, NewSecondMinU,
               NewMaxV, NewCntMaxV, NewSecondMaxV,
               NewMinV, NewCntMinV, NewSecondMinV).

compute_min(UVs,
            MaxU, CntMaxU, SecondMaxU,
            MinU, CntMinU, SecondMinU,
            MaxV, CntMaxV, SecondMaxV,
            MinV, CntMinV, SecondMinV) ->
    compute_min_loop(UVs,
                     MaxU, CntMaxU, SecondMaxU,
                     MinU, CntMinU, SecondMinU,
                     MaxV, CntMaxV, SecondMaxV,
                     MinV, CntMinV, SecondMinV,
                     ?INF).

compute_min_loop([], _MaxU,_CntMaxU,_SecondMaxU,
                 _MinU,_CntMinU,_SecondMinU,
                 _MaxV,_CntMaxV,_SecondMaxV,
                 _MinV,_CntMinV,_SecondMinV,
                 Best) ->
    Best;

compute_min_loop([{U,V}|Rest],
                 MaxU, CntMaxU, SecondMaxU,
                 MinU, CntMinU, SecondMinU,
                 MaxV, CntMaxV, SecondMaxV,
                 MinV, CntMinV, SecondMinV,
                 Best) ->

    CurMaxU = case (U == MaxU andalso CntMaxU =:= 1) of
                  true -> SecondMaxU;
                  false -> MaxU
              end,
    CurMinU = case (U == MinU andalso CntMinU =:= 1) of
                  true -> SecondMinU;
                  false -> MinU
              end,
    CurMaxV = case (V == MaxV andalso CntMaxV =:= 1) of
                  true -> SecondMaxV;
                  false -> MaxV
              end,
    CurMinV = case (V == MinV andalso CntMinV =:= 1) of
                  true -> SecondMinV;
                  false -> MinV
              end,

    DiffU = CurMaxU - CurMinU,
    DiffV = CurMaxV - CurMinV,
    Candidate = if DiffU > DiffV -> DiffU; true -> DiffV end,
    NewBest = if Candidate < Best -> Candidate; true -> Best end,
    compute_min_loop(Rest,
                     MaxU, CntMaxU, SecondMaxU,
                     MinU, CntMinU, SecondMinU,
                     MaxV, CntMaxV, SecondMaxV,
                     MinV, CntMinV, SecondMinV,
                     NewBest).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_distance(points :: [[integer]]) :: integer
  def minimum_distance(points) do
    inf = 1_000_000_0000

    {uv_rev,
     max_u, cnt_max_u, second_max_u,
     min_u, cnt_min_u, second_min_u,
     max_v, cnt_max_v, second_max_v,
     min_v, cnt_min_v, second_min_v} =
      Enum.reduce(points, {[], -inf, 0, -inf,
                           inf, 0, inf,
                           -inf, 0, -inf,
                           inf, 0, inf},
        fn [x, y],
           {uv_acc,
            max_u, cnt_max_u, second_max_u,
            min_u, cnt_min_u, second_min_u,
            max_v, cnt_max_v, second_max_v,
            min_v, cnt_min_v, second_min_v} ->

          u = x - y
          v = x + y

          # update max_u
          {max_u, cnt_max_u, second_max_u} =
            cond do
              u > max_u -> {u, 1, max_u}
              u == max_u -> {max_u, cnt_max_u + 1, second_max_u}
              u > second_max_u -> {max_u, cnt_max_u, u}
              true -> {max_u, cnt_max_u, second_max_u}
            end

          # update min_u
          {min_u, cnt_min_u, second_min_u} =
            cond do
              u < min_u -> {u, 1, min_u}
              u == min_u -> {min_u, cnt_min_u + 1, second_min_u}
              u < second_min_u -> {min_u, cnt_min_u, u}
              true -> {min_u, cnt_min_u, second_min_u}
            end

          # update max_v
          {max_v, cnt_max_v, second_max_v} =
            cond do
              v > max_v -> {v, 1, max_v}
              v == max_v -> {max_v, cnt_max_v + 1, second_max_v}
              v > second_max_v -> {max_v, cnt_max_v, v}
              true -> {max_v, cnt_max_v, second_max_v}
            end

          # update min_v
          {min_v, cnt_min_v, second_min_v} =
            cond do
              v < min_v -> {v, 1, min_v}
              v == min_v -> {min_v, cnt_min_v + 1, second_min_v}
              v < second_min_v -> {min_v, cnt_min_v, v}
              true -> {min_v, cnt_min_v, second_min_v}
            end

          {[{u, v} | uv_acc],
           max_u, cnt_max_u, second_max_u,
           min_u, cnt_min_u, second_min_u,
           max_v, cnt_max_v, second_max_v,
           min_v, cnt_min_v, second_min_v}
        end)

    # reverse to original order
    uv = Enum.reverse(uv_rev)

    sec_max_u = if second_max_u == -inf, do: max_u, else: second_max_u
    sec_min_u = if second_min_u == inf, do: min_u, else: second_min_u
    sec_max_v = if second_max_v == -inf, do: max_v, else: second_max_v
    sec_min_v = if second_min_v == inf, do: min_v, else: second_min_v

    Enum.reduce(uv, inf, fn {u, v}, best ->
      cur_max_u = if u == max_u && cnt_max_u == 1, do: sec_max_u, else: max_u
      cur_min_u = if u == min_u && cnt_min_u == 1, do: sec_min_u, else: min_u

      cur_max_v = if v == max_v && cnt_max_v == 1, do: sec_max_v, else: max_v
      cur_min_v = if v == min_v && cnt_min_v == 1, do: sec_min_v, else: min_v

      d = max(cur_max_u - cur_min_u, cur_max_v - cur_min_v)
      if d < best, do: d, else: best
    end)
  end
end
```
