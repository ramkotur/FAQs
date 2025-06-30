
# def show(a,b):
#     return a+b
# print (show(10,2))
#
# def show1(a,b) -> int:
#     return a+b
# print(show1(1,2))
#

# rng = range(1,10)
# for i in rng:
#     print(i)
# print(list(rng))

# for i in range(1,10,2):
#     print(i)

#------------ Map Function ------------

# strings = ["my","aa","bb","cc"]
# l = map(len,strings)
# print(list(l))

#--------------lambda function ------------
# l = map(lambda  x: x+"s",strings)
# print(list(l))

# -----------------------
# strings = ["my","aa","bb","ccc"]
# l = filter(lambda x: len(x) > 2,strings)
# print (list(l))

# #----- List / array and Tupple example ------------
# #---- Array Example ---
# a=[1,2,3,4]
# a[0]=9
# print (a)
#
# #--- Tuple example----
# b=(1,2,3,4)
# # b[0]=9 -- you can not change the value
# print(b)
#
# # --- Add List and Tupple ---
# c=a+list(b)
# print(c)
#
# # -------------------------------------------------
# #-------- Merge two dictionaries ------------
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

print(dict1)
merged = dict1 | dict2
print(merged)
