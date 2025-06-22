first_set = {23,42,57,65,78,83,29}
second_set = {57,83,27,69,73,43,48}
result = first_set.intersection(second_set)
print("intersection",result)
for item in result:
    first_set.remove(item)
    second_set.remove(item)
print(first_set)
print(second_set)
