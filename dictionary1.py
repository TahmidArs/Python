student_data={'id1':{'name':['Sara'],'class':['V'],'subject_integration':['math,english,science']},'id2':{'name':['David'],'class':['Vi'],'subject_integration':['math,english,science']},'id3':{'name':['henry'],'class':['Vii'],'subject_integration':['math,english,science']},'id4':{'name':['nick'],'class':['Viii'],'subject_integration':['math,english,science']}}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)