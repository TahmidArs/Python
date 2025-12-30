test_dict={'I':1,'am':2,'Tahmid':3}
print("The original dictionary is:"+str(test_dict))
k=3
res=0
for i in test_dict:
    if test_dict[i]==k:
        res+=1
print("Frequency of k is:"+str(res))