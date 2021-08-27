# """
# thing = {'a':1}
# values=thing.values()
# total=sum(values)+int(input())
# print(total)
#
# if int(input()):
#     self.quantity["quantity"] = temp + int(input())
#     print(self.quantity)
# """
# """
# import random
# n = random.randint(0,10000)
# print(n)
# """
# """
# import collections.abc
#
# def update(d, u):
#     for k, v in u.items():
#         if isinstance(v, collections.abc.Mapping):
#             d[k] = update(d.get(k, {}), v)
#         else:
#             d[k] = v
#     print(d)
# d=input("Enter keys:=")
# u=int(input("Enter values:="))
# """
# """
# d={}
# n=int(input())
# for i in range(0,n):
#     keys=input("Enter the keys:")
#     value=int(input("Enter the values:="))
#     d[keys]=value
# print(d)
# """
# """
# list=[[1,2,3][1,2,3]]
# print(sum(list))
# """
#
# # from functools import reduce as rahul
# #
# # def nested_sum(seq):
# #     print(rahul(lambda a,b: a+(nested_sum(b) if isinstance(b, list) else b), seq))
# #
# # nested_sum([[2,4,5],[4,6,8],[3,6,9]])
#
# list=[1,2,3,4]
# for i in range(len(list)):
#     print(list[i])

# lis =  [1,2,3,4,5]
#
# for x in lis:
#     print(x)
#     input("")

ke = {"a":1}
dict ={1:{2:{3:'a',4:'b'},5:[{6:'c'},{6:'d'}]}}
# dict[ke["a"]][5].append({8:'e'})

#print(dict)
for key,values in dict.items():
    for val in values.get(5):
        print(key,values.get(2).get(3),values.get(2).get(4),val.get(6))

#1,a,b,c
#1,a,b,d

