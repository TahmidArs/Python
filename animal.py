from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        #abstract method
        #should be implemented by all sub classes
        pass
class human(animal):
    def move(self):
        print("I can walk and run")

class dog(animal):
    def move(self):
        print("I can walk and run")

class tiger(animal):
    def move(self):
        print("I can roar")

class lion(animal):
    def move(self):
        print("I can roar")

h=human(
)
k=dog()
m=tiger()
l=lion()
h.move()
m.move()
k.move()
l.move()