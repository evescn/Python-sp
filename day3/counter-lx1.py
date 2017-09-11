import collections

obj = collections.Counter('aaabbccsdfsdfdfsdfsdf')
print(obj)
ret1 = obj.most_common(2)
print(ret1)

#for item in obj.elements():
    # print(item)

for k,v in obj.items():
    print(k,v)


