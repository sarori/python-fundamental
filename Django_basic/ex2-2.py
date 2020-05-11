class Car():
    def __init__(self, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def start(self):
        print(self.doors)
        print("I started")
    
    def __str__(self):
        return f"Car with {self.wheels} wheels"

class Convertible(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "Taking off"
    
    def __str__(self):
        return f"Car with NO ROOF"




porche = Car(color="green", price="$40")      #porche는 Car class로 만든 instance이다.
print(porche.color, porche.price)
porche.color = "Red"    #확장시키는 것도 가능

ferrari = Car()
ferrari.color = "Yellow"

porche.start()
print(porche)
print(porche.__str__())
print(porche.color, porche.price)

mini = Car()
print(mini.color, mini.price)

#inheritance
mini = Convertible(color="blue", price="$30")
mini.take_off()
print(mini)
