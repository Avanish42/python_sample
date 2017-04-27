def sortList(list):
    print("i function {0}".format(list[0]))
    newList=[]
    for each in list:
        print("each Element :: ",each)






myList=[]
listElement=0   
count=0
num =int(input("number of ele"))
for counter in range(num):

    print("enter the {0}th  value :".format(count))
    listElement=int(input())
    count=count+1
    myList.append(listElement)

# print(myList)
sortList(myList)
