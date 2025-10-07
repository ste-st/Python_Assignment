class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road!")


class Plane(Vehicle):
    def move(self):
        print("✈️ Flying through the sky!")


class Boat(Vehicle):
    def move(self):
        print("🛥️ Sailing on the water!")


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
