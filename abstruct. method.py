from abc import ABC,abstractmethod
class Abs_class(ABC):
    def print(self,x):
        print("Passed value:",x)

    #Abstruct method
    @abstractmethod
    def task(self):
        print("We are inside abstract method")

class test_class(Abs_class):
    def task(self):
        print("We are inside test_class task")
test_obj = test_class()
test_obj.print(100)
test_obj.task()