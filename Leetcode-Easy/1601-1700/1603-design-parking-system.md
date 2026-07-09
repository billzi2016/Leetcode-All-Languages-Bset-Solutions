# 1603. Design Parking System

## Cpp

```cpp
class ParkingSystem {
public:
    ParkingSystem(int big, int medium, int small) {
        slots[0] = big;
        slots[1] = medium;
        slots[2] = small;
    }
    
    bool addCar(int carType) {
        if (carType < 1 || carType > 3) return false;
        int idx = carType - 1;
        if (slots[idx] > 0) {
            --slots[idx];
            return true;
        }
        return false;
    }
private:
    int slots[3]{0,0,0};
};
```

## Java

```java
class ParkingSystem {
    private final int[] slots;

    public ParkingSystem(int big, int medium, int small) {
        slots = new int[]{big, medium, small};
    }

    public boolean addCar(int carType) {
        int idx = carType - 1;
        if (slots[idx] > 0) {
            slots[idx]--;
            return true;
        }
        return false;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */
```

## Python

```python
class ParkingSystem(object):
    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.spots = [big, medium, small]

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        idx = carType - 1
        if self.spots[idx] > 0:
            self.spots[idx] -= 1
            return True
        return False
```

## Python3

```python
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        idx = carType - 1
        if self.slots[idx] > 0:
            self.slots[idx] -= 1
            return True
        return False
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int slots[3];
} ParkingSystem;

ParkingSystem* parkingSystemCreate(int big, int medium, int small) {
    ParkingSystem *obj = (ParkingSystem*)malloc(sizeof(ParkingSystem));
    if (!obj) return NULL;
    obj->slots[0] = big;
    obj->slots[1] = medium;
    obj->slots[2] = small;
    return obj;
}

bool parkingSystemAddCar(ParkingSystem* obj, int carType) {
    if (carType < 1 || carType > 3) return false;
    int idx = carType - 1;
    if (obj->slots[idx] > 0) {
        obj->slots[idx]--;
        return true;
    }
    return false;
}

void parkingSystemFree(ParkingSystem* obj) {
    free(obj);
}
```

## Csharp

```csharp
public class ParkingSystem
{
    private readonly int[] _slots;

    public ParkingSystem(int big, int medium, int small)
    {
        _slots = new int[3];
        _slots[0] = big;
        _slots[1] = medium;
        _slots[2] = small;
    }

    public bool AddCar(int carType)
    {
        int index = carType - 1;
        if (_slots[index] > 0)
        {
            _slots[index]--;
            return true;
        }
        return false;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj.AddCar(carType);
 */
```

## Javascript

```javascript
/**
 * @param {number} big
 * @param {number} medium
 * @param {number} small
 */
var ParkingSystem = function(big, medium, small) {
    this.spots = [big, medium, small];
};

/** 
 * @param {number} carType
 * @return {boolean}
 */
ParkingSystem.prototype.addCar = function(carType) {
    const idx = carType - 1;
    if (this.spots[idx] > 0) {
        this.spots[idx]--;
        return true;
    }
    return false;
};
```

## Typescript

```typescript
class ParkingSystem {
    private slots: number[];

    constructor(big: number, medium: number, small: number) {
        this.slots = [big, medium, small];
    }

    addCar(carType: number): boolean {
        const idx = carType - 1;
        if (this.slots[idx] > 0) {
            this.slots[idx]--;
            return true;
        }
        return false;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = new ParkingSystem(big, medium, small)
 * var param_1 = obj.addCar(carType)
 */
```

## Php

```php
class ParkingSystem {
    /**
     * @var array
     */
    private $slots;

    /**
     * @param Integer $big
     * @param Integer $medium
     * @param Integer $small
     */
    public function __construct($big, $medium, $small) {
        $this->slots = [$big, $medium, $small];
    }

    /**
     * @param Integer $carType
     * @return Boolean
     */
    public function addCar($carType) {
        $idx = $carType - 1;
        if ($this->slots[$idx] > 0) {
            $this->slots[$idx]--;
            return true;
        }
        return false;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * $obj = new ParkingSystem($big, $medium, $small);
 * $ret_1 = $obj->addCar($carType);
 */
```

## Swift

```swift
class ParkingSystem {
    private var slots: [Int]

    init(_ big: Int, _ medium: Int, _ small: Int) {
        self.slots = [big, medium, small]
    }

    func addCar(_ carType: Int) -> Bool {
        let index = carType - 1
        if slots[index] > 0 {
            slots[index] -= 1
            return true
        }
        return false
    }
}
```

## Kotlin

```kotlin
class ParkingSystem(big: Int, medium: Int, small: Int) {
    private val empty = intArrayOf(big, medium, small)

    fun addCar(carType: Int): Boolean {
        val idx = carType - 1
        return if (empty[idx] > 0) {
            empty[idx]--
            true
        } else {
            false
        }
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = ParkingSystem(big, medium, small)
 * var param_1 = obj.addCar(carType)
 */
```

## Dart

```dart
class ParkingSystem {
  late List<int> _slots;

  ParkingSystem(int big, int medium, int small) {
    _slots = [big, medium, small];
  }

  bool addCar(int carType) {
    if (_slots[carType - 1] > 0) {
      _slots[carType - 1]--;
      return true;
    }
    return false;
  }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = ParkingSystem(big, medium, small);
 * bool param1 = obj.addCar(carType);
 */
```

## Golang

```go
type ParkingSystem struct {
	slots []int
}

func Constructor(big int, medium int, small int) ParkingSystem {
	return ParkingSystem{slots: []int{big, medium, small}}
}

func (this *ParkingSystem) AddCar(carType int) bool {
	idx := carType - 1
	if this.slots[idx] > 0 {
		this.slots[idx]--
		return true
	}
	return false
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * obj := Constructor(big, medium, small);
 * param_1 := obj.AddCar(carType);
 */
```

## Ruby

```ruby
class ParkingSystem
  # :type big: Integer
  # :type medium: Integer
  # :type small: Integer
  def initialize(big, medium, small)
    @slots = [big, medium, small]
  end

  # :type car_type: Integer
  # :rtype: Boolean
  def add_car(car_type)
    idx = car_type - 1
    if @slots[idx] > 0
      @slots[idx] -= 1
      true
    else
      false
    end
  end
end

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem.new(big, medium, small)
# param_1 = obj.add_car(car_type)
```

## Scala

```scala
class ParkingSystem(_big: Int, _medium: Int, _small: Int) {
  private val slots = Array(_big, _medium, _small)

  def addCar(carType: Int): Boolean = {
    val idx = carType - 1
    if (slots(idx) > 0) {
      slots(idx) -= 1
      true
    } else {
      false
    }
  }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * val obj = new ParkingSystem(big, medium, small)
 * val param_1 = obj.addCar(carType)
 */
```

## Rust

```rust
use std::cell::RefCell;

struct ParkingSystem {
    slots: RefCell<[i32; 3]>,
}

impl ParkingSystem {
    fn new(big: i32, medium: i32, small: i32) -> Self {
        ParkingSystem {
            slots: RefCell::new([big, medium, small]),
        }
    }

    fn add_car(&self, car_type: i32) -> bool {
        let idx = (car_type - 1) as usize;
        let mut slots = self.slots.borrow_mut();
        if slots[idx] > 0 {
            slots[idx] -= 1;
            true
        } else {
            false
        }
    }
}
```

## Racket

```racket
(define parking-system%
  (class object%
    (super-new)

    ; big : exact-integer?
    ; medium : exact-integer?
    ; small : exact-integer?
    (init-field
      big
      medium
      small)

    ; add-car : exact-integer? -> boolean?
    (define/public (add-car car-type)
      (cond [(= car-type 1)
             (if (> big 0)
                 (begin (set! big (- big 1)) #t)
                 #f)]
            [(= car-type 2)
             (if (> medium 0)
                 (begin (set! medium (- medium 1)) #t)
                 #f)]
            [(= car-type 3)
             (if (> small 0)
                 (begin (set! small (- small 1)) #t)
                 #f)]
            [else #f])))))
```

## Erlang

```erlang
-module(solution).
-export([parking_system_init_/3, parking_system_add_car/1]).

-spec parking_system_init_(Big :: integer(), Medium :: integer(), Small :: integer()) -> any().
parking_system_init_(Big, Medium, Small) ->
    put(parking_slots, {Big, Medium, Small}),
    ok.

-spec parking_system_add_car(CarType :: integer()) -> boolean().
parking_system_add_car(CarType) ->
    Slots = get(parking_slots),
    Available = element(CarType, Slots),
    if
        Available > 0 ->
            NewSlots = setelement(CarType, Slots, Available - 1),
            put(parking_slots, NewSlots),
            true;
        true ->
            false
    end.
```

## Elixir

```elixir
defmodule ParkingSystem do
  @spec init_(big :: integer, medium :: integer, small :: integer) :: any
  def init_(big, medium, small) do
    Process.put(:parking_slots, [big, medium, small])
  end

  @spec add_car(car_type :: integer) :: boolean
  def add_car(car_type) do
    slots = Process.get(:parking_slots, [0, 0, 0])
    idx = car_type - 1

    case Enum.at(slots, idx) do
      n when n > 0 ->
        updated = List.replace_at(slots, idx, n - 1)
        Process.put(:parking_slots, updated)
        true

      _ ->
        false
    end
  end
end
```
