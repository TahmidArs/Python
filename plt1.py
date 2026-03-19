import matplotlib.pyplot as plt

student_names=['a', 'b', 'c','d','e','f','g','h','i','j']
student_marks=[35,50,25,40,45,25,40,25,45,35]

marks_perc=[]

for x in student_marks:
    res=(x/50)*100
    marks_perc.append(res)

print(marks_perc)

#line chart
def marks_line_chart():
    plt.plot(student_names,student_marks)
    plt.title('Students Marks Graph')
    plt.xlabel('Students Names')
    plt.ylabel('Student Marks')
    plt.show()

marks_line_chart()

#bar chart
def marks_bar_chart():
    plt.bar(student_names,student_marks)
    plt.title('Students Marks Graph')
    plt.xlabel('Students Names')
    plt.ylabel('Student Marks')
    plt.show()

marks_bar_chart()