lucky_numbers = [4, 8, 15, 16, 23, 42]
cities = ["Tumkur", "Bangalore", "Kochi", "Tokyo", "Boston", "New York", "Prague", "Brno"]

cities.append("San Fransisco")

cities.sort()
print("Sorted list is ", cities)

cities.reverse()
print("Reversed sorted list is ", cities)

cities_copy = cities.copy()
print("Copied cities list is ", cities_copy)

cities.extend(lucky_numbers)
print("Lists are appended", cities)

cities.insert(1, "Bellur")
print("Bellur is added", cities)

cities.remove("Kochi")
print("Kochi is removed", cities)

print("Index of Bangalore is ", cities.index("Bangalore"))

cities.clear()
print("List is cleared", cities)

lucky_numbers.pop()
print("Last element is popped", lucky_numbers)

lucky_numbers.append(4)
print("Number of occurance of 4 is ", lucky_numbers.count(4))

