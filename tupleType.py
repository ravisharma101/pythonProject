# Tuple is like  a  list except it is immutable
# Insertion order is maintained
# Allow Duplicates
# Add heterogeneous elements

# Empty Tuple
empty_tuple=()
print(empty_tuple)

# Non Empty Tuple
f_tuple=(40,60,40,'XYZ')
print(f_tuple)

# To declare a single valued tuple/list use , after the element
s_tup=(4,)
print(s_tup)

print(f_tuple[3])
print(f_tuple*3)

#We can not use slicing in  tuples

print(f_tuple.count(40))

# Convert a list into tuple

t_list=[67,58,24,56]
l_tuple=tuple(t_list)
print(l_tuple)