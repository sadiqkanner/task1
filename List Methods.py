Mylist = ['ABC','EFG','XYZ']

Mylist.append('SADIQ')
print(Mylist)

a = Mylist.copy()
print(a)

a.clear()
print(a)

print(Mylist.count(a))
print(Mylist)

NewList = ['SK','BALOCH']
NewList.extend(Mylist)
print(NewList)

i = NewList.index('XYZ')
print(i)

NewList.insert(0,'PIAIC')
print(NewList)

NewList.pop()
print(NewList)

NewList.remove('SK')
print(NewList)

NewList.reverse()
print(NewList)

NewList.sort()
print(NewList)