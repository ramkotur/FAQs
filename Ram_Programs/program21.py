# a=[1,2,3,1,2]
# a=list(filter(lambda x:x%2==0,a))
# print(a)
#----------------------------------

# -- Remove all duplicate records -----
# a=[1,1,2,3,4,2]
# a=list(filter(lambda x:a.count(x)==1,set(a)))
# print (a)

# a=[x for x in range(10)]
# # print (a)
#
# b=[x for x in a if x %2==0]
# print(b)

# a= [1,2,3,1]
# b=list(filter(lambda x:a.count(x) == 1,a))
# print(b)

# a="abc"
# print(a[::-1])

#--- Revers Word ----
# a="ram mohan kotur"
# b=a.split()
# b=b[::-1]
# b=' '.join(b)
# print (b)

# a= lambda x,y:x+y
# print(a(10,20))

# ----- Remove Duplicate values -------
a=[1,2,2,3,4,4]
b=set(a)
print(b)




