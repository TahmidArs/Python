numbers1=[1,2,3,4,5]
numbers2=[2,3,4,5,6]
result=map(lambda x,y:x+y,numbers1,numbers2)
print(list(result))
nums=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq,nums))
print('Squares of numbers in list:',square)
