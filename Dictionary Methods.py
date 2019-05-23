dic = {
    'Name' : 'Sadiq',
    'Age' : 25 ,
    'Phone' : 32323 ,
    'Address' : 'Karachi'
}


ndic = dic.copy()
print(ndic)


k = ('K1' , 'K2' , 'K3')
i = "BALOCH"
s = dict.fromkeys(k,i)
print(s)

n = dic.get('Name')
print(n)

print(dic.keys())

print(dic.items())

pp = dic.pop('Age')
print(pp)

pi = dic.popitem()
print(pi) #print the last Value of Dictionary

sd = dic.setdefault('Name',"Baloch")
print(sd)

dic.update({'Blood':'A+'})
print(dic)


print(dic.values())

dic.clear()
print(dic)

