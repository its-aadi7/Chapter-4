friends = ["Apple", "Oranges", 5, 354.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Aadi")
print(friends)

l1 = [1, 34, 62, 2, 6, 11]
# l1.sort()
# l1.reverse()
# l1.insert(3, 33333) # Insert 33333 such thsi it is in the list is 3
# print(l1.pop(3)) # It will directly show the no which is on the index value 3
value = l1.pop(3) # The pop can be written as value = l1.pop(3)
print(value)
# l1.pop(3) # It will remove the value of the index value 3.
print(l1) 
l1.remove(62)
print(l1)
l1.clear()