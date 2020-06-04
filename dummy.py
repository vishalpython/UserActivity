import copy
list1=[10,[1,2],30]
list2=copy.copy(list1)

list2[1][0]=5
print(list2)
print(list1)