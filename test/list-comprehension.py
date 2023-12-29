dict = {0: 23, 1: 23, 2: 34}
list1=[2,3,55]
# count=0
# for x, y in dict.items():
#     list1[count]=y
#     count+=1
    
list1 = [x for x in dict.values()]

print(list1)