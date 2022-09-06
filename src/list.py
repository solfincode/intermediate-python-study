fruits = ["apple", "banana", "strawberry", "blueberry"]

# printout fruits
print("fruits are ", fruits)

# list
second_item = fruits[1]
print("second item is", second_item)

# loop statement
for fruit in fruits:
    print(fruit)

# length of list
print("total item in the list is", len(fruits))

# insert item in the 2nd
fruits.insert(1, "coldberry")
print("insert coldberry -", fruits)

# pop - blueberry which is last item will be gone
fruits.pop()
print("pop blueberry -", fruits)

# reverse
fruits.reverse()
print("reversed order -", fruits)

# slice
sliced = fruits[1:4]
print("sliced - ", sliced)

# append
fruits.append(sliced)
print("appended - ", fruits)
