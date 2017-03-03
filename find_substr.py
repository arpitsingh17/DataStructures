# finding substring in a string

#substring = "sd"
#string = "asdfg"

def findstr(string1, substring1):

    for i in range(len(string1) - len(substring1) + 1):
        if (string1[i:i+len(substring1)] == substring1):
            return i


print(findstr("asdfg","sd"))