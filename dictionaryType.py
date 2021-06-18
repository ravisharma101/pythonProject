# {key:value}
dict={1:'John',2:'Bob',3:'Bill',4:'Ted'}

print(dict)
print(dict.items())

k=dict.keys()
for i in k:
    print(i)

v=dict.values()
for i in v:
    print(i)

print(dict[2])
del dict[2]
print(dict)