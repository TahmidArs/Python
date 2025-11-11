def cube(number):
    return number**1/3
def by_3(number):
    if number%3==0:
        return cube(number)
    else:
        return False
print(by_3(9))
print(by_3(4))
