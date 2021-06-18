# Empty List
empty_list = []
print(empty_list)

# Non Empty List
non_empty_list = [10, 20, 'List', -10, 30.5]
print(non_empty_list)

# Fetching an element in a list using index
print(non_empty_list[2])

# Slicing in list
print(non_empty_list[1:4])
print(non_empty_list[::2])
print(non_empty_list[::-1])
print(non_empty_list[::-2])

# Replicating list
print(non_empty_list * 2)

# Combining two or more lists
letter=['a','b','c','d']
num=[1,2,3,4]
combined_list=letter+num
print(combined_list)

# Using iterable to make a list
iterable_number_list=list(range(20))
print(iterable_number_list)
iterable_character_list=list("Hello World")
print(iterable_character_list)

# Length of list
print(len(non_empty_list))

# To add an element at the end of list use append method
non_empty_list.append("Append element")
print(non_empty_list)

# To insert an element at a certain index use insert method
non_empty_list.insert(3, 99)
print(non_empty_list)

# to remove an item from a list use pop method if index is not passed it will remove the last element
# else if a index is passed it will then it will remove the element at that specific index
non_empty_list.pop()
print(non_empty_list)

# To remove the first occurrence of an element from the list using the value
# Remove method will return value error if value passed is missing
non_empty_list.remove("List")
print(non_empty_list)

# To remove an element using the index use the inbuilt  delete function and pass the index
# We can also delete multiple items using the del function this the difference between del function and pop method
# Example del(non_empty_list[1:3]) it will delete all element between 1 and 3
del (non_empty_list[1])
print(non_empty_list)

# To find an element in a list use index method it will return the index of the element
# Index method will return an error if element is not available to avoid this we can use in operator or count method
# print(non_empty_list.index(10))
if 'H' in iterable_character_list:
    print(iterable_character_list.index('l'))

# To remove all items from the list use clear method
# non_empty_list.clear()
# print(non_empty_list)

# To get the maximum & minimum from list use max/min function respectively
print(max(non_empty_list))
print(min(non_empty_list))

# To sort the list user sort method
non_empty_list.sort()
print(non_empty_list)

# To sort the list in reverse
# non_empty_list.sort(reverse=True)
# print(non_empty_list)
#  OR
non_empty_list.reverse()
print(non_empty_list)


# Unpacking of list : Assigning variable name to the each element in a list
# on the left side we have variable name and on the right we have list name
# no of variable name should be equal to list or we can divide list into elements and sublist
# using *other we are packing rest of the element of the list into "other" list
list_unpacking=[56,58,94,56,54,52,95]
first_element,second_element, *other_elements=list_unpacking
print(first_element,second_element,other_elements)

# Assigning last element of the list to a variable
first_element,*other_elements,last_element=list_unpacking
print(first_element,other_elements,last_element)

# Looping over a list
for character in iterable_character_list:
    print(character,end=" ")
print("\n")

# To get index of each item of a list
# Enumerate function will return a tuple with first element as index of an element
# And second element as the list element itself
#
# for variable in enumerate(iterable_character_list):
#     print(variable,variable[0],variable[1], end=" ")
# Better version of above code
for index, value in enumerate(iterable_character_list):
    print(index, value,end=" ")
