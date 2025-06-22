def replace_ch(string, ch1, ch2):
    result = ""
    for char in string:
        if char == ch1:
            result += ch2
        elif char == ch2:
            result += ch1
        else:
            result += char
    return result

string = input("Enter a string: ")
ch1 = input("Enter the first character to replace: ")
ch2 = input("Enter the second character to replace: ")

print(replace_ch(string, ch1, ch2))
