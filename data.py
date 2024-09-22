import pandas as pd
import matplotlib.pyplot as plt


def bar():
    data1 = input("Enter the index number of the data which lays on x-axis : ")
    xlbl=input("Enter the heading of that index : ")
    x_data=int(data1)
    first = df.iloc[0:,x_data].tolist()

    data2 = input("Enter the index number of the data which lays on y-axis : ")
    ylbl=input("Enter the heading of that index : ")
    y_data=int(data2)
    second = df.iloc[0:,y_data].tolist()

    lbl = input("Enter topic name of your data : ")
    #creating bar graph
    plt.bar(first,second,label=f'{lbl}',color='red')

    #set x and y axis labels
    plt.xlabel(f'{xlbl}')
    plt.ylabel(f'{ylbl}')

    #set company title
    title = input("Enter your company name : ")
    plt.title(f'{title}')

    #show legend
    plt.legend()

    #display the graph
    plt.show()
def line():
     #plot() function is used to create the line chart
    data1 = input("Enter the index number of the data which lays on x-axis : ")
    xlbl=input("Enter the heading of that index : ")
    x_data=int(data1)
    first = df.iloc[0:,x_data].tolist()

    data2 = input("Enter the index number of the data which lays on y-axis : ")
    ylbl=input("Enter the heading of that index : ")
    y_data=int(data2)
    second = df.iloc[0:,y_data].tolist()

    plt.plot(first,second,'red')
    #set company title
    title = input("Enter the title of the data : ")
    plt.title(f'{title}')
    plt.show()
# def pie():
#     #plot() function is used to create the line chart
#     data1 = input("Enter the index number of the column which is name or id  : ")
#     x_data=int(data1)
#     first = df.iloc[0:,x_data].tolist()
#     second=[50,20,15,15]
#     cols=['green','red','yellow','blue']
#     plt.pie(second,labels=first,colors=cols,startangle=90,explode=(0,0.2,0,0),shadow=True,autopct='%.1f%%')
#     title = input("Enter the title of the program ")
#     plt.title(f"{title}")
#     plt.legend()
#     plt.show()

#taking the path of the file
a = input("Enter your exact file location  make sure your file is saved as csv ex(D:\ filename.csv) : ")
#creating data frame of the input file
df = pd.read_csv(f"{a}")
print(df) #printing the data

graph = input("Tell me in which format you want to represent your data (bar,pie,line) : ")

if(graph == 'bar'):
    bar()
elif(graph == 'line'):
   line()
# elif(graph == 'pie'):
#    pie()
else:
    print("invalid input")
