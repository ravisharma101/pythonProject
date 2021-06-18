bytes_list=[10,20,30,40,234]
print(type(bytes_list))

# We can't perform indexing and addition to the bytes
b=bytes(bytes_list)
print(type(b))
#print(b)

# We can add or modify an element to the bytearray
a=bytearray(bytes_list)
print(type(a))
a[2]=22

# Slicing and repetition is not allowed in any of them