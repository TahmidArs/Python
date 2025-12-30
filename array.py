import array as arr
array_num=arr.array('i',[1,2,3,5,2,3])
print("Original array:",array_num)
print("Number of occurences of the number 3 in the said array is:",(array_num.count(3)))
array_num.reverse()
print("Reverse the order of items:",array_num)