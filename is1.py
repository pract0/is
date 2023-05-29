string = input("Enter a String : ")
result_and = ""
result_or = ""

for char in string:
    and_val = ord(char) & 127
    xor_val = ord(char) ^ 127

    result_and += chr(and_val)
    result_or += chr(xor_val)

print("Original String : "+string)
print("And string : "+ result_and)
print("XOR string : "+ result_or)
