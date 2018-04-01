from LinkedList import LinkedList

my_list = LinkedList()

my_list.add("A")
my_list.add("B")
my_list.add("C")
my_list.add("D")

print(my_list.to_array())
print("Current size: " + str(my_list.get_size()))
print("First element: " + my_list.get_first())
print("Last element: " + my_list.get_last())
print("")

my_list.add("E")

print(my_list.to_array())
print("Current size: " + str(my_list.get_size()))
print("First element: " + my_list.get_first())
print("Last element: " + my_list.get_last())
print("")

my_list.remove_first()

print(my_list.to_array())
print("Current size: " + str(my_list.get_size()))
print("First element: " + my_list.get_first())
print("Last element: " + my_list.get_last())
print("")

my_list.remove_last()

print(my_list.to_array())
print("Current size: " + str(my_list.get_size()))
print("First element: " + my_list.get_first())
print("Last element: " + my_list.get_last())
print("")

my_list.remove_first()

print(my_list.to_array())
print("Current size: " + str(my_list.get_size()))
print("First element: " + my_list.get_first())
print("Last element: " + my_list.get_last())
print("")

my_list.remove_last()

print(my_list.to_array())
print("Current size: " + str(my_list.get_size()))
print("First element: " + my_list.get_first())
print("Last element: " + my_list.get_last())
print("")

my_list.remove_first()

print(my_list.to_array())
print("Current size: " + str(my_list.get_size()))
print("")