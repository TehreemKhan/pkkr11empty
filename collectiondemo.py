# # # # myFruitList = ["apple", "banana", "cherry", ['a',1], True, 1]
# # # # # l=list()
# # # # # print(myFruitList)
# # # # # print(myFruitList[0:4])
# # # # # print(myFruitList[0:])
# # # # # print(myFruitList[:3])
# # # # # print(myFruitList[3:4])
# # # # # l2 = myFruitList[-2]
# # # # # print(type(myFruitList))
# # # # # print(len(myFruitList))
# # # # # s=myFruitList[len(myFruitList)-1]
# # # # l=[3,4,1,2]
# # # # l[1]="A"
# # # # print(l)
# # # # # l.sort()
# # # # # l.reverse()
# # # # # print(l.index(4))
# # # # # l.insert(2,5)
# # # # l2=l.copy()
# # # # print(l)
# # # # print(l2)
# # # # l2.append(7)
# # # # print(l)
# # # # print(l2)
# # #
# # # l=[2,3,4,1,2,2,3]
# # # print(l)
# # # s=set(l)
# # # print(s)
# # # l2=list(s)
# # # print(type(l2))
# # # # s = {1,2,3,4,2}
# # # # s2 = {1,2,3,4,7,8}
# # # # print(s.add(5))
# # # # # print(s.union(s2))
# # # # print(s.)
# # # # print(type(s))
# # # # s1="asdf"
# # # # for x in [12,2,0,4]:
# # # #     print(x)
# #
# # # t=tuple([1,2])
# # t=(3,4,5,6)
# # print(t)
# # a,b,c,d=t
# # # a=t[0]
# # b=t[1]
# # print(a)
# # print(b)
# # print(c)
# # print(d)
# # # print(t[-1])
# # # print(type(t))
#
#
# d={1:"one",2:"two",3:300, 3:[1,2,3,],"k1":"v1", True:"one"}
# # # print(d[True])
# # d["newkey"]=100
# # d[5]="fie]ve"
# # print(d)
#
# print(d.items())
# print(d.keys())
# # print(type(d.items()))
# for k,v in d.items():
#     print(k)
#     print(v)

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))