h = int(input("Tedade tuple ha ra vared konid: ")) 
tuples_list = [] 
for _ in range(h): 
    tup = tuple(map(int, input("Tuple ra vared konid (ba fasele joda konid): ").split())) 
    tuples_list.append(tup) 
sorted_list = sorted(tuples_list, key=lambda k: k[1]) 
print("List-e moratab shode:", sorted_list)