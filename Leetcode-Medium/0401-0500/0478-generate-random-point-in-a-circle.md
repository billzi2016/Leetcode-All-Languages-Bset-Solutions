# 0478. Generate Random Point in a Circle

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double radius, x_center, y_center;
    mt19937 gen;
    uniform_real_distribution<double> dist01;
    uniform_real_distribution<double> angleDist;

    Solution(double radius_, double x_center_, double y_center_)
        : radius(radius_), x_center(x_center_), y_center(y_center_),
          gen(random_device{}()), dist01(0.0, 1.0), angleDist(0.0, 2 * acos(-1)) {}

    vector<double> randPoint() {
        double theta = angleDist(gen);
        double r = sqrt(dist01(gen)) * radius;
        return {x_center + r * cos(theta), y_center + r * sin(theta)};
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj->randPoint();
 */
```

## Java

```java
class Solution {
    private final double radius;
    private final double x_center;
    private final double y_center;
    private final java.util.Random rand;

    public Solution(double radius, double x_center, double y_center) {
        this.radius = radius;
        this.x_center = x_center;
        this.y_center = y_center;
        this.rand = new java.util.Random();
    }

    public double[] randPoint() {
        double angle = rand.nextDouble() * 2.0 * Math.PI;
        double distance = Math.sqrt(rand.nextDouble()) * radius;
        double x = x_center + distance * Math.cos(angle);
        double y = y_center + distance * Math.sin(angle);
        return new double[]{x, y};
    }
}
```

## Python

```python
import math
import random

class Solution(object):
    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        theta = random.random() * 2 * math.pi
        r = math.sqrt(random.random()) * self.radius
        return [self.xc + r * math.cos(theta), self.yc + r * math.sin(theta)]
```

## Python3

```python
import random
import math
from typing import List

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self) -> List[float]:
        theta = random.random() * 2 * math.pi
        r = math.sqrt(random.random()) * self.radius
        return [self.xc + r * math.cos(theta), self.yc + r * math.sin(theta)]
```

## C

```c
#include <stdlib.h>
#include <math.h>
#include <time.h>

#ifndef M_PI
#define M_PI acos(-1.0)
#endif

typedef struct {
    double radius;
    double x_center;
    double y_center;
} Solution;

Solution* solutionCreate(double radius, double x_center, double y_center) {
    Solution *obj = (Solution*)malloc(sizeof(Solution));
    obj->radius = radius;
    obj->x_center = x_center;
    obj->y_center = y_center;
    srand((unsigned)time(NULL));
    return obj;
}

double* solutionRandPoint(Solution* obj, int* retSize) {
    double theta = ((double)rand() / RAND_MAX) * 2.0 * M_PI;
    double u = (double)rand() / RAND_MAX;
    double r = sqrt(u) * obj->radius;
    double x = obj->x_center + r * cos(theta);
    double y = obj->y_center + r * sin(theta);
    
    double* point = (double*)malloc(2 * sizeof(double));
    point[0] = x;
    point[1] = y;
    *retSize = 2;
    return point;
}

void solutionFree(Solution* obj) {
    free(obj);
}
```

## Csharp

```csharp
public class Solution
{
    private readonly double _radius;
    private readonly double _xCenter;
    private readonly double _yCenter;
    private readonly Random _rand;

    public Solution(double radius, double x_center, double y_center)
    {
        _radius = radius;
        _xCenter = x_center;
        _yCenter = y_center;
        _rand = new Random();
    }

    public double[] RandPoint()
    {
        double angle = _rand.NextDouble() * 2.0 * Math.PI;
        double distance = Math.Sqrt(_rand.NextDouble()) * _radius;
        double x = _xCenter + distance * Math.Cos(angle);
        double y = _yCenter + distance * Math.Sin(angle);
        return new double[] { x, y };
    }
}
```

## Javascript

```javascript
/**
 * @param {number} radius
 * @param {number} x_center
 * @param {number} y_center
 */
var Solution = function(radius, x_center, y_center) {
    this.radius = radius;
    this.xc = x_center;
    this.yc = y_center;
};

/**
 * @return {number[]}
 */
Solution.prototype.randPoint = function() {
    const angle = Math.random() * 2 * Math.PI;
    const distance = this.radius * Math.sqrt(Math.random());
    const x = this.xc + distance * Math.cos(angle);
    const y = this.yc + distance * Math.sin(angle);
    return [x, y];
};
```

## Typescript

```typescript
class Solution {
    private radius: number;
    private x_center: number;
    private y_center: number;

    constructor(radius: number, x_center: number, y_center: number) {
        this.radius = radius;
        this.x_center = x_center;
        this.y_center = y_center;
    }

    randPoint(): number[] {
        const angle = Math.random() * 2 * Math.PI;
        const distance = Math.sqrt(Math.random()) * this.radius;
        const x = this.x_center + distance * Math.cos(angle);
        const y = this.y_center + distance * Math.sin(angle);
        return [x, y];
    }
}
```

## Php

```php
class Solution {
    private float $radius;
    private float $x_center;
    private float $y_center;

    /**
     * @param Float $radius
     * @param Float $x_center
     * @param Float $y_center
     */
    function __construct($radius, $x_center, $y_center) {
        $this->radius = (float)$radius;
        $this->x_center = (float)$x_center;
        $this->y_center = (float)$y_center;
    }

    /**
     * @return Float[]
     */
    function randPoint() {
        // Generate a uniform random angle between 0 and 2π
        $theta = 2.0 * M_PI * (mt_rand() / mt_getrandmax());
        // Generate radius with sqrt to ensure uniform distribution over area
        $r = sqrt(mt_rand() / mt_getrandmax()) * $this->radius;
        $x = $this->x_center + $r * cos($theta);
        $y = $this->y_center + $r * sin($theta);
        return [(float)$x, (float)$y];
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * $obj = new Solution($radius, $x_center, $y_center);
 * $ret_1 = $obj->randPoint();
 */
```

## Swift

```swift
import Foundation

class Solution {
    private let radius: Double
    private let xCenter: Double
    private let yCenter: Double

    init(_ radius: Double, _ x_center: Double, _ y_center: Double) {
        self.radius = radius
        self.xCenter = x_center
        self.yCenter = y_center
    }

    func randPoint() -> [Double] {
        let angle = Double.random(in: 0..<2 * .pi)
        let distance = sqrt(Double.random(in: 0...1)) * radius
        let x = xCenter + distance * cos(angle)
        let y = yCenter + distance * sin(angle)
        return [x, y]
    }
}
```

## Kotlin

```kotlin
import kotlin.math.*
import kotlin.random.Random

class Solution(private val radius: Double, private val x_center: Double, private val y_center: Double) {

    fun randPoint(): DoubleArray {
        val angle = Random.nextDouble(0.0, 2 * Math.PI)
        val distance = sqrt(Random.nextDouble()) * radius
        return doubleArrayOf(
            x_center + distance * cos(angle),
            y_center + distance * sin(angle)
        )
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = Solution(radius, x_center, y_center)
 * var param_1 = obj.randPoint()
 */
```

## Dart

```dart
import 'dart:math';

class Solution {
  final double _radius;
  final double _xCenter;
  final double _yCenter;
  final Random _rand = Random();

  Solution(double radius, double x_center, double y_center)
      : _radius = radius,
        _xCenter = x_center,
        _yCenter = y_center;

  List<double> randPoint() {
    final double angle = _rand.nextDouble() * 2 * pi;
    final double distance = sqrt(_rand.nextDouble()) * _radius;
    final double x = _xCenter + distance * cos(angle);
    final double y = _yCenter + distance * sin(angle);
    return [x, y];
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = Solution(radius, x_center, y_center);
 * List<double> param1 = obj.randPoint();
 */
```

## Golang

```go
import (
	"math"
	"math/rand"
	"time"
)

type Solution struct {
	radius   float64
	x_center float64
	y_center float64
}

func Constructor(radius float64, x_center float64, y_center float64) Solution {
	return Solution{radius: radius, x_center: x_center, y_center: y_center}
}

func (this *Solution) RandPoint() []float64 {
	angle := rand.Float64() * 2 * math.Pi
	dist := this.radius * math.Sqrt(rand.Float64())
	x := this.x_center + dist*math.Cos(angle)
	y := this.y_center + dist*math.Sin(angle)
	return []float64{x, y}
}

func init() {
	rand.Seed(time.Now().UnixNano())
}
```

## Ruby

```ruby
class Solution
=begin
    :type radius: Float
    :type x_center: Float
    :type y_center: Float
=end
  def initialize(radius, x_center, y_center)
    @radius = radius
    @x_center = x_center
    @y_center = y_center
  end

=begin
    :rtype: Float[]
=end
  def rand_point
    theta = Random.rand * 2 * Math::PI
    r = Math.sqrt(Random.rand) * @radius
    [@x_center + r * Math.cos(theta), @y_center + r * Math.sin(theta)]
  end
end
```

## Scala

```scala
import java.util.concurrent.ThreadLocalRandom

class Solution(_radius: Double, _x_center: Double, _y_center: Double) {
  private val radius = _radius
  private val xCenter = _x_center
  private val yCenter = _y_center

  def randPoint(): Array[Double] = {
    val rnd = ThreadLocalRandom.current()
    val angle = rnd.nextDouble() * 2.0 * Math.PI
    val distance = Math.sqrt(rnd.nextDouble()) * radius
    Array(xCenter + distance * Math.cos(angle), yCenter + distance * Math.sin(angle))
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * val obj = new Solution(radius, x_center, y_center)
 * val param_1 = obj.randPoint()
 */
```

## Rust

```rust
extern crate rand;
use rand::Rng;
use std::f64::consts::PI;

struct Solution {
    radius: f64,
    x_center: f64,
    y_center: f64,
}

impl Solution {
    fn new(radius: f64, x_center: f64, y_center: f64) -> Self {
        Solution { radius, x_center, y_center }
    }

    fn rand_point(&self) -> Vec<f64> {
        let mut rng = rand::thread_rng();
        let theta = rng.gen_range(0.0..2.0 * PI);
        let u: f64 = rng.gen_range(0.0..1.0);
        let r = self.radius * u.sqrt();
        let x = self.x_center + r * theta.cos();
        let y = self.y_center + r * theta.sin();
        vec![x, y]
    }
}
```

## Racket

```racket
(define solution%
  (class object%
    (super-new)
    
    ; radius : flonum?
    ; x_center : flonum?
    ; y_center : flonum?
    (init-field
      radius
      x_center
      y_center)
    
    ; rand-point : -> (listof flonum?)
    (define/public (rand-point)
      (let* ([theta (* 2.0 pi (random))]
             [r (* radius (sqrt (random)))])
        (list (+ x_center (* r (cos theta)))
              (+ y_center (* r (sin theta))))))))
```

## Erlang

```erlang
-spec solution_init_(Radius :: float(), X_center :: float(), Y_center :: float()) -> any().
solution_init_(Radius, X_center, Y_center) ->
    put(radius, Radius),
    put(x_center, X_center),
    put(y_center, Y_center),
    %% Seed the random generator for this process
    Seed = {erlang:monotonic_time(),
            erlang:unique_integer([monotonic]),
            node()},
    rand:seed(exsplus, Seed).

-spec solution_rand_point() -> [float()].
solution_rand_point() ->
    Radius = get(radius),
    Xc = get(x_center),
    Yc = get(y_center),
    Angle = rand:uniform() * 2 * math:pi(),
    R = math:sqrt(rand:uniform()) * Radius,
    X = Xc + R * math:cos(Angle),
    Y = Yc + R * math:sin(Angle),
    [X, Y].
```

## Elixir

```elixir
defmodule Solution do
  @spec init_(radius :: float, x_center :: float, y_center :: float) :: any
  def init_(radius, x_center, y_center) do
    # Seed the random generator for this process
    :rand.seed(:exsplus, :erlang.monotonic_time())
    Process.put(:circle_data, {radius, x_center, y_center})
    :ok
  end

  @spec rand_point() :: [float]
  def rand_point() do
    {r, cx, cy} = Process.get(:circle_data)

    theta = :rand.uniform() * 2.0 * :math.pi()
    distance = :math.sqrt(:rand.uniform()) * r

    x = cx + distance * :math.cos(theta)
    y = cy + distance * :math.sin(theta)

    [x, y]
  end
end
```
