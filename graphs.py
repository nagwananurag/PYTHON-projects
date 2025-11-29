import matplotlib.pyplot as plt


x= (1,2,3,4)

y= (6,7,8,9)


plt.plot(x,y)
plt.title("student subject vs marks")
plt.xlabel("subject")

plt.ylabel("marks")
plt.show()


subject = ("chemistry","physics","english","maths")
marks = ("81","85","40","65")
plt.bar(x,y)



plt.title("student sub vs marks")

plt.xlabel("subject")
plt.ylabel("marks")
plt.show()