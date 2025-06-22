first_set={23,42,65,57,78,83,29}
print("first set ",first_set)
second_set={57,83,27,69,73,43,48}
print("second set ",second_set)
result = first_set.intersection(second_set)
print("intersection ",result)
for item in result:
    first_set.remove(item)
    second_set.remove(item)
print(first_set)
print(second_set)
