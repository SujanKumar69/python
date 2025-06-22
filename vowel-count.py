def count_voewls(string):
    vowels = 'aeiouAEIOU'
    count = 0
    
    for char in string:
        if char in vowels:
            count += 1
    return count

input_string=input("Enter any string ")
vowels = count_voewls(input_string)
print("vowels in ",vowels)
