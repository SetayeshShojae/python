list1 = list(map(int, input("List aval ra vared kon (ba faseleh joda kon): ").split())) 
list2 = list(map(int, input("List dovom ra vared kon (ba faseleh joda kon): ").split())) 
result = list(map(lambda l,m: l + m, list1, list2)) 
print("natijeh list : ", result)