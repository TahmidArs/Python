class pair_elements:
    def twoSum(Self,nums,targets):
        #create an empty dictionary
        lookup= {}
        #iterate through the tuple
        for i,num in enumerate(nums):
            if targets-num in lookup:
                return (lookup[targets-num],i)
            lookup[num]=i
value=int(input("Enter sum for which you want to make the search:"))
print("index1=%d,index2=%d" %pair_elements().twoSum(10,20,30,40,50,60,70,80),value)