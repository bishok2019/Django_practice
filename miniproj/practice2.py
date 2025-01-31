# k = ['a','b', 'c', 'd', 'e','f','g']
# v= [0,1,2,3,4,5,]

#List(CRUD)
# print([i**2 for i in v])
# result = []
# for i in v:
#     result.append(i*2)
# print(result)
# print('',[val for val in  v if val%2== 0])
# print([i for i in range(0,10,3)])
# print('coordinte',[(x,y) for x in range(1) for y in range(2)])

# lis = [(x,y) for x in range(1) for y in range(2)]
# print(lis)
# result = [val for row in lis for val in row]
# print(result)
# convert2set = set(result)
# print(convert2set)
# convert2list=list(convert2set)
# print(convert2list)
    
# print(matrix0)
# print(matrix1)
# import random

# print([i for i in range(3)])
# x=[i for i in range(3)]
# print(x[0])
# x=[[i for i in range(3)] for i in range(3)]
# print(x[0])
# x.append('y')
# print(x)
# x[0].append('y')
# print(x)
# x[0].remove('y')
# print(x)
# x.pop(2)
# print(x)
# for i in x:
#     i.remove(1)
#     print(x)
# print([[i for i in range(3)] for i in range(5)])

# row=([[random.randint(0,6) for i in range(6)] for i in range(7)])
# for matrix in row:
#     print(matrix)
# x=[i for i in range(3)]
# print(x)
# x[0]=2
# print(x)

# Tuple(CRUD)
y=(0,1,2,9,98,3,4,5,6)
(a,*b,*c,d)=y
print(b)
print(c)

# z=tuple(i for i in range(6))
# for i in y:
#     print(i)
# f=(y,z)
# my_list=list(z)
# my_list[4]=6
# z=tuple(my_list)

# print(z)
# print(f)
# print(f[1])
# print(y[1]) # accessing element inside y
# print(y[:4])# accessing a elements of y from 0-3

# convert tuple intolist
# t=(1,2,3,4)
# l=[]
# for i in t:
#     l.append(i)
# print(l)
# t2=(4,5,6,7)

# l1=['a','c','s',9]
# l.append(l1)
# l.extend(l1)
# print(l)

# tuple_list = ([1,2,3],4,5,6,7,8)
# print(tuple_list[0][1])
# tuple_list[0].append(11)
# print(tuple_list)

# list_tuple = [1,2,3,(4,5,6)]
# list_tuple[0] = 8
# print(list_tuple)

#dictComprehension
# print(dict(zip(k,v)))

##########             SET
# my_set={i for i in range(5)}
# print('my_set:',my_set)
# my_set.add(20)
# print(my_set)
#convert set to list
# my_list=list(my_set)
# print(my_list)
# my_list.append(30)
# print(my_list)

# another_set={i for i in range(6)}
# print('another_set:',another_set)
# my_another_list=list(another_set)
# my_another_list.append(10)
# print(my_another_list)
# my_set.add(11)
# x=my_set.union(another_set)
# print('union of:',x)
# final_set={None}
# y=final_set.union(my_set,another_set)
# print(y)
# my_set.update(another_set)
# my_set.discard(6)
# print(my_set)
# removed_item = my_set.pop()
# print(removed_item)

# my_string = "hello w0rld"
# new_string = my_string[:4] + my_string[7:]
# # new_string = my_string[:4]
# print(new_string)


################ DICT ###########################
# key=(1,2,3,4,5,6,7,8,9)
# value = ('a','s:','d','f''f''g','h','j''j','k','l')
# my_dict ={k:v for k,v in zip(key,value)}
# my_dict = {zip(key,value)}
# my_dict = dict(zip(key,value))
# print(my_dict)
# my_dict[4] = 'f' # modify 
# print(my_dict)
# my_dict.pop(1) # delete the  item by key
# print(my_dict)
# my_dict.popitem() # delete the last item
# my_dict.remove()
# print(my_dict)
# print(my_dict)
# print(my_dict.items())