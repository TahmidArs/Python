def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>=2 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    print("list of words with first and last letters same:\n",lst)
    return ctr
count=match_words(["abc","cfc","aba","xyz","1221",])
print("Numbers of words having first and last character same:",count)