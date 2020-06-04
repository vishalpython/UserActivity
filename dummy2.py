import copy
list1=[10,1,30]
list2=copy.copy(list1)

list2[1]=5
print(list2)
print(list1)
