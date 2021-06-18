# Sets does not allow duplicate elements
# If we add duplicate element while declaring it will omit it in printing
# Set does not guarantee any order
# Set does not allow slicing indexing and repetition
s_first={10,20,30,40,40,'abc'}
print(s_first)
s_first.update([80,90])
print(s_first)
s_first.remove(30)
print(s_first)

# Frozen Set once we convert a set into frozen set we can not update/remove element from it

f=frozenset(s_first)

