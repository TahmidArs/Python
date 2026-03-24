import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,20,15,25,30]

#Line with Points
plt.plot(x,y,marker='o')

plt.title("Line Plot with Data Points")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()

months=[1,2,3,4,5]
sales=[100,150,130,170,200]

#Bar Graph
plt.bar(months,sales)
plt.title('Monthly Sales(Bar Graph)')
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()
