tuplex=("tuple",False,3.5,14)
print(tuplex)
tuplex=(5,56,53,2)
print(tuplex)
#tuples are immutable so you can not add new elments
#using merge of tuples with the+ operator you can add an new element and it will create a new tuple
tuplex=tuplex+(3,)
print(tuplex)
tuple1=(50,7,34,50,60)
print(tuple1.count(50))
tuplex=(2,3,4,5,6,7,8,9,1)
slice_tuple=tuplex[2:7]
print(slice_tuple)
slice_tuple=tuplex[:4]
print(slice_tuple)