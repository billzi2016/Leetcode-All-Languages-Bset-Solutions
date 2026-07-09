# 2383. Minimum Hours of Training to Win a Competition

## Cpp

```cpp
class Solution {
public:
    int minNumberOfHours(int initialEnergy, int initialExperience, vector<int>& energy, vector<int>& experience) {
        long long totalEnergyNeeded = 0;
        for (int e : energy) totalEnergyNeeded += e;
        // Need strictly more than total consumption
        int energyHours = max(0LL, totalEnergyNeeded + 1 - initialEnergy);
        
        int expHours = 0;
        long long curExp = initialExperience;
        for (size_t i = 0; i < experience.size(); ++i) {
            if (curExp <= experience[i]) {
                int need = (int)(experience[i] + 1 - curExp);
                expHours += need;
                curExp += need;
            }
            curExp += experience[i];
        }
        return energyHours + expHours;
    }
};
```

## Java

```java
class Solution {
    public int minNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        int hours = 0;
        long curEnergy = initialEnergy; // use long to avoid overflow though not needed
        long curExp = initialExperience;
        for (int i = 0; i < energy.length; i++) {
            if (curEnergy <= energy[i]) {
                int need = (int)(energy[i] - curEnergy + 1);
                hours += need;
                curEnergy += need;
            }
            if (curExp <= experience[i]) {
                int need = (int)(experience[i] - curExp + 1);
                hours += need;
                curExp += need;
            }
            // defeat opponent
            curEnergy -= energy[i];
            curExp += experience[i];
        }
        return hours;
    }
}
```

## Python

```python
class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        hours = 0
        cur_energy = initialEnergy
        cur_exp = initialExperience

        for e, exp in zip(energy, experience):
            if cur_energy <= e:
                need = e - cur_energy + 1
                hours += need
                cur_energy += need
            if cur_exp <= exp:
                need = exp - cur_exp + 1
                hours += need
                cur_exp += need

            # defeat opponent
            cur_energy -= e
            cur_exp += exp

        return hours
```

## Python3

```python
from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        hours = 0
        cur_energy = initialEnergy
        cur_exp = initialExperience
        
        for e, exp in zip(energy, experience):
            if cur_energy <= e:
                need = e - cur_energy + 1
                hours += need
                cur_energy += need
            if cur_exp <= exp:
                need = exp - cur_exp + 1
                hours += need
                cur_exp += need
            cur_energy -= e
            cur_exp += exp
        
        return hours
```

## C

```c
int minNumberOfHours(int initialEnergy, int initialExperience, int* energy, int energySize, int* experience, int experienceSize) {
    int curE = initialEnergy;
    int curX = initialExperience;
    int hours = 0;
    for (int i = 0; i < energySize; ++i) {
        if (curE <= energy[i]) {
            int need = energy[i] - curE + 1;
            hours += need;
            curE += need;
        }
        if (curX <= experience[i]) {
            int need = experience[i] - curX + 1;
            hours += need;
            curX += need;
        }
        curE -= energy[i];
        curX += experience[i];
    }
    return hours;
}
```

## Csharp

```csharp
public class Solution {
    public int MinNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        int hours = 0;
        long curEnergy = initialEnergy;
        long curExp = initialExperience;
        for (int i = 0; i < energy.Length; i++) {
            if (curEnergy <= energy[i]) {
                long need = energy[i] - curEnergy + 1;
                hours += (int)need;
                curEnergy += need;
            }
            if (curExp <= experience[i]) {
                long need = experience[i] - curExp + 1;
                hours += (int)need;
                curExp += need;
            }
            curEnergy -= energy[i];
            curExp += experience[i];
        }
        return hours;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} initialEnergy
 * @param {number} initialExperience
 * @param {number[]} energy
 * @param {number[]} experience
 * @return {number}
 */
var minNumberOfHours = function(initialEnergy, initialExperience, energy, experience) {
    // Energy training: need total sum + 1
    const totalEnergyNeeded = energy.reduce((sum, val) => sum + val, 0) + 1;
    let hours = Math.max(0, totalEnergyNeeded - initialEnergy);
    
    // Experience training: greedy per opponent
    let curExp = initialExperience;
    for (let i = 0; i < experience.length; ++i) {
        if (curExp <= experience[i]) {
            const need = experience[i] - curExp + 1;
            hours += need;
            curExp += need;
        }
        curExp += experience[i];
    }
    
    return hours;
};
```

## Typescript

```typescript
function minNumberOfHours(initialEnergy: number, initialExperience: number, energy: number[], experience: number[]): number {
    let hours = 0;
    
    // Energy requirement: need total sum + 1
    const totalEnergyNeeded = energy.reduce((sum, val) => sum + val, 0) + 1;
    if (initialEnergy < totalEnergyNeeded) {
        hours += totalEnergyNeeded - initialEnergy;
    }
    
    // Experience requirement: greedy increase when needed
    let curExp = initialExperience;
    for (let i = 0; i < experience.length; i++) {
        if (curExp <= experience[i]) {
            const need = experience[i] - curExp + 1;
            hours += need;
            curExp += need;
        }
        curExp += experience[i];
    }
    
    return hours;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $initialEnergy
     * @param Integer $initialExperience
     * @param Integer[] $energy
     * @param Integer[] $experience
     * @return Integer
     */
    function minNumberOfHours($initialEnergy, $initialExperience, $energy, $experience) {
        $hours = 0;
        $curE = $initialEnergy;
        $curX = $initialExperience;
        $n = count($energy);
        for ($i = 0; $i < $n; $i++) {
            if ($curE <= $energy[$i]) {
                $need = $energy[$i] - $curE + 1;
                $hours += $need;
                $curE += $need;
            }
            if ($curX <= $experience[$i]) {
                $need = $experience[$i] - $curX + 1;
                $hours += $need;
                $curX += $need;
            }
            // defeat opponent
            $curE -= $energy[$i];
            $curX += $experience[$i];
        }
        return $hours;
    }
}
```

## Swift

```swift
class Solution {
    func minNumberOfHours(_ initialEnergy: Int, _ initialExperience: Int, _ energy: [Int], _ experience: [Int]) -> Int {
        // Energy part: need total sum + 1
        let totalEnergy = energy.reduce(0, +)
        var hours = max(0, totalEnergy + 1 - initialEnergy)
        
        // Experience part: simulate and train when needed
        var curExp = initialExperience
        var expHours = 0
        for i in 0..<experience.count {
            if curExp <= experience[i] {
                let need = experience[i] + 1 - curExp
                expHours += need
                curExp += need
            }
            curExp += experience[i]
        }
        return hours + expHours
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minNumberOfHours(initialEnergy: Int, initialExperience: Int, energy: IntArray, experience: IntArray): Int {
        var hours = 0
        var curEnergy = initialEnergy
        var curExp = initialExperience

        // Ensure enough energy to be strictly greater than total sum of opponent energies
        val requiredEnergy = energy.sum() + 1
        if (curEnergy < requiredEnergy) {
            hours += requiredEnergy - curEnergy
            curEnergy = requiredEnergy
        }

        for (i in energy.indices) {
            // Ensure enough experience to beat current opponent
            if (curExp <= experience[i]) {
                val need = experience[i] + 1 - curExp
                hours += need
                curExp += need
            }
            // Defeat the opponent
            curExp += experience[i]
            curEnergy -= energy[i]
        }

        return hours
    }
}
```

## Dart

```dart
class Solution {
  int minNumberOfHours(int initialEnergy, int initialExperience, List<int> energy, List<int> experience) {
    int totalEnergy = 0;
    for (int e in energy) {
      totalEnergy += e;
    }
    int requiredEnergy = totalEnergy + 1;
    int hours = 0;
    if (initialEnergy < requiredEnergy) {
      hours += requiredEnergy - initialEnergy;
    }

    int curExp = initialExperience;
    for (int i = 0; i < experience.length; ++i) {
      if (curExp <= experience[i]) {
        int need = experience[i] - curExp + 1;
        hours += need;
        curExp += need;
      }
      curExp += experience[i];
    }

    return hours;
  }
}
```

## Golang

```go
func minNumberOfHours(initialEnergy int, initialExperience int, energy []int, experience []int) int {
    totalEnergy := 0
    for _, e := range energy {
        totalEnergy += e
    }
    hours := 0
    if initialEnergy <= totalEnergy {
        need := totalEnergy + 1 - initialEnergy
        hours += need
    }

    curExp := initialExperience
    for i, exp := range experience {
        if curExp <= exp {
            diff := exp + 1 - curExp
            hours += diff
            curExp += diff
        }
        curExp += exp
        _ = energy[i] // silence unused variable warning if any
    }
    return hours
}
```

## Ruby

```ruby
def min_number_of_hours(initial_energy, initial_experience, energy, experience)
  total_needed_energy = energy.sum + 1
  added_energy = [0, total_needed_energy - initial_energy].max

  cur_exp = initial_experience
  added_experience = 0

  experience.each_with_index do |exp_i, idx|
    if cur_exp <= exp_i
      need = exp_i + 1 - cur_exp
      added_experience += need
      cur_exp += need
    end
    cur_exp += exp_i
  end

  added_energy + added_experience
end
```

## Scala

```scala
object Solution {
    def minNumberOfHours(initialEnergy: Int, initialExperience: Int, energy: Array[Int], experience: Array[Int]): Int = {
        var hours = 0

        // Energy requirement: need total sum + 1
        val requiredEnergy = energy.sum + 1
        if (initialEnergy < requiredEnergy) {
            hours += requiredEnergy - initialEnergy
        }

        // Experience requirement: greedy increase when needed
        var curExp = initialExperience
        for (i <- energy.indices) {
            if (curExp <= experience(i)) {
                val need = experience(i) - curExp + 1
                hours += need
                curExp += need
            }
            curExp += experience(i)
        }

        hours
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_number_of_hours(initial_energy: i32, initial_experience: i32, energy: Vec<i32>, experience: Vec<i32>) -> i32 {
        let mut hours = 0;
        let mut cur_energy = initial_energy;
        let mut cur_exp = initial_experience;

        for (e, exp) in energy.iter().zip(experience.iter()) {
            if cur_energy <= *e {
                let need = *e - cur_energy + 1;
                hours += need;
                cur_energy += need;
            }
            if cur_exp <= *exp {
                let need = *exp - cur_exp + 1;
                hours += need;
                cur_exp += need;
            }
            cur_energy -= *e;
            cur_exp += *exp;
        }

        hours
    }
}
```

## Racket

```racket
(define/contract (min-number-of-hours initialEnergy initialExperience energy experience)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((total-energy (apply + energy))
         (energy-needed (max 0 (- (+ total-energy 1) initialEnergy))))
    (let loop ((idx 0)
               (cur-exp initialExperience)
               (hours energy-needed))
      (if (= idx (length energy))
          hours
          (let* ((opp-exp (list-ref experience idx))
                 (need (max 0 (- (+ opp-exp 1) cur-exp)))
                 (new-hours (+ hours need))
                 (new-cur-exp (+ cur-exp need opp-exp)))
            (loop (add1 idx) new-cur-exp new-hours))))))
```

## Erlang

```erlang
-spec min_number_of_hours(InitialEnergy :: integer(), InitialExperience :: integer(),
                           Energy :: [integer()], Experience :: [integer()]) -> integer().
min_number_of_hours(InitialEnergy, InitialExperience, Energy, Experience) ->
    loop(Energy, Experience, InitialEnergy, InitialExperience, 0).

loop([], [], _CurE, _CurX, Acc) ->
    Acc;
loop([E|Es], [X|Xs], CurE, CurX, Acc) ->
    {NeedE, NewCurE} =
        if
            CurE > E -> {0, CurE};
            true ->
                Need = E - CurE + 1,
                {Need, CurE + Need}
        end,
    {NeedX, NewCurX} =
        if
            CurX > X -> {0, CurX};
            true ->
                Need = X - CurX + 1,
                {Need, CurX + Need}
        end,
    TotalAcc = Acc + NeedE + NeedX,
    UpdatedE = NewCurE - E,
    UpdatedX = NewCurX + X,
    loop(Es, Xs, UpdatedE, UpdatedX, TotalAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_number_of_hours(initial_energy :: integer, initial_experience :: integer, energy :: [integer], experience :: [integer]) :: integer
  def min_number_of_hours(initial_energy, initial_experience, energy, experience) do
    total_needed_energy = Enum.sum(energy) + 1
    extra_energy = max(0, total_needed_energy - initial_energy)

    {total_hours, _final_exp} =
      Enum.zip(energy, experience)
      |> Enum.reduce({extra_energy, initial_experience}, fn {_e, exp_i},
                                                          {hours, cur_exp} ->
        if cur_exp > exp_i do
          {hours, cur_exp + exp_i}
        else
          need = exp_i - cur_exp + 1
          {hours + need, cur_exp + need + exp_i}
        end
      end)

    total_hours
  end
end
```
